#!/usr/bin/env python3
"""
Usa LM Studio come backend (server locale compatibile OpenAI) per
ristrutturare note Markdown secondo la Style Guide definita in SYSTEM_PROMPT
(pensato per l'export Obsidian -> PDF).

Uso:
    python Formatta_Slide.py input.md                        # stampa su stdout
    python Formatta_Slide.py input.md -o output.md           # scrive su file (incrementale)
    python Formatta_Slide.py input.md --host http://localhost:1234
    python Formatta_Slide.py input.md --model mistral-7b-instruct
    python Formatta_Slide.py input.md --chunk-size 3000
    python Formatta_Slide.py input.md --max-tokens 4096 --max-retries 3
    python Formatta_Slide.py input.md --resume stato.json    # riprende da dove si era fermato
    python Formatta_Slide.py input.md --dry-run              # mostra i chunk senza chiamare il modello

Dipendenze:
    solo libreria standard (urllib, logging, time, json, pathlib)
"""

import sys
import re
import time
import logging
import argparse
import textwrap
import json
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# ---------------------------------------------------------------------------
# Costanti / defaults
# ---------------------------------------------------------------------------

DEFAULT_HOST        = "http://localhost:1234"   # porta default di LM Studio
DEFAULT_MODEL       = ""      # LM Studio ignora il nome se c'è un solo modello caricato
MAX_TOKENS          = 8192
DEFAULT_TEMPERATURE = 0.3
DEFAULT_TOP_P       = 0.9
DEFAULT_TIMEOUT     = 300     # secondi per singola richiesta HTTP (non-streaming)
DEFAULT_MAX_RETRIES = 2       # tentativi aggiuntivi oltre al primo

SYSTEM_PROMPT = textwrap.dedent(r"""\
Sei un editor specializzato nella trasformazione di slide universitarie convertite in Markdown in appunti di studio compatti, completi e autosufficienti.

Il tuo obiettivo è produrre un testo che uno studente possa usare direttamente per prepararsi a un esame, senza bisogno di consultare il materiale originale.

---

### PRINCIPI FONDAMENTALI

**Mantieni sempre:**
- Definizioni formali di concetti, termini tecnici e teorie
- Spiegazioni del "perché" un concetto esiste o è rilevante
- Esempi del mondo reale che ancorino un concetto astratto alla realtà
- Tabelle comparative e di sintesi (sono strumenti di studio ad alta densità)
- Formule, condizioni di equilibrio, relazioni matematiche chiave
- Distinzioni critiche tra concetti simili (es. "non confondere X con Y")
- Avvertenze ("Attenzione") che evidenziano errori comuni o eccezioni importanti
- Esercizi con soluzione esplicita (se presenti): sono utilissimi per la preparazione
- Struttura gerarchica del documento (titoli, sottotitoli, liste puntate)

**Elimina sempre:**
- Frasi introduttive di contesto accademico del tipo "In questa lezione vedremo...", "Come abbiamo detto...", "Ricordiamo che..."
- Sezioni "Collegamenti" / "Richiede: [...] / Usato in: [...]" — sono metadati pedagogici, non contenuto
- Blocchi "Perché serve" ridondanti quando il concetto principale li ingloba già nella definizione
- Riferimenti a immagini e figure non presenti nel testo (es. `![Figura](url)`, `Figura 1: ...`, `Figura N: ...`) — le immagini non sono nel documento testuale
- URL grezzi e link non cliccabili
- Frasi conclusive retoriche e di chiusura salvo contengano informazioni sostanziali non dette altrove
- Ripetizioni: se un concetto è già spiegato in un blocco `[!important]`, non replicarlo nel paragrafo successivo
- Intestazioni vuote o sezioni che contengono solo rimandi ad altre sezioni

---

### REGOLE DI FORMATTAZIONE OUTPUT

1. **Conserva i blocchi callout Obsidian** (`> [!important]`, `> [!warning]`, `> [!example]`) solo se contengono contenuto sostanziale. Unifica callout multipli dello stesso tipo sullo stesso concetto in un unico blocco.
2. **Le tabelle vanno sempre conservate** nella loro struttura originale, rimuovendo solo colonne o righe palesemente ridondanti o decorative.
3. **Le formule matematiche** (inline `$...$` o display `$$...$$`) vanno conservate intatte — non riscrivere mai una formula in prosa.
4. **Non alterare i blocchi protetti** dal preprocessore: i placeholder `[[[TIPO_NNNN]]]` devono essere copiati invariati nell'output.
5. **Mantieni la gerarchia dei titoli** (H1, H2, H3) dell'originale, a meno che una sezione venga eliminata interamente — in quel caso sopprimila anche nella struttura.
6. **Non aggiungere mai contenuto** che non sia già presente nell'input: niente integrazioni, niente commenti dell'editor, niente sommari generati da te.
7. **Non modificare la lingua** del testo: se l'input è in italiano, l'output è in italiano.

---

### CALIBRAZIONE DELLA DENSITÀ

Il testo finale deve essere:
- **Più corto dell'originale** (obiettivo: riduzione del 25–40% del conteggio caratteri)
- **Non più corto del necessario**: ogni taglio deve essere giustificato da ridondanza o inutilità per lo studio individuale
- **Autosufficiente**: uno studente che legge solo questo testo deve poter rispondere alle domande d'esame standard sul blocco trattato
""")

# Il template è ora una singola istruzione coerente, senza contraddizioni.
CHUNK_PROMPT_TEMPLATE = textwrap.dedent(r"""\
Di seguito trovi un blocco di testo estratto da appunti universitari in formato Markdown.
Possono essere presenti placeholder nella forma `[[[TIPO_NNNN]]]` che rappresentano
elementi protetti (formule, codice, URL): NON modificarli, copiali identici dove si trovano.

Il tuo compito è riscrivere questo blocco applicando le istruzioni del system prompt:
elimina il rumore accademico, consolida le ripetizioni, rimuovi i metadati pedagogici
(sezioni "Collegamenti", "Perché serve" ridondanti, riferimenti a immagini assenti).

Vincoli assoluti:
- Rispondi SOLO con il Markdown riformattato, senza preamboli né spiegazioni
- NON aggiungere testo che non sia già nel blocco
- NON inserire titoli o sezioni aggiuntive rispetto all'originale
- I placeholder `[[[TIPO_NNNN]]]` devono apparire invariati nell'output

--- BEGIN CHUNK ---
{chunk}
--- END CHUNK ---
""")

# ---------------------------------------------------------------------------
# Protezione dei blocchi da non alterare
# ---------------------------------------------------------------------------

PLACEHOLDER_RE = re.compile(r'\[\[\[[A-Z]+_\d{4}\]\]\]')

# L'ordine conta: i pattern più "larghi" (blocchi multiriga) devono
# essere applicati prima di quelli inline, altrimenti un `$$` display
# viene prima "tagliato" dal pattern inline `$...$`.
PROTECTED_PATTERNS: List[Tuple[re.Pattern, str]] = [
    # Front-matter YAML/TOML (deve essere primo: copre '---\n...\n---')
    (re.compile(r'^---\n.*?\n---\n', re.DOTALL | re.MULTILINE), "FRONTMATTER"),
    # Immagini Markdown standard: ![ alt ]( path ) — protegge l'intera riga
    # PRIMA dei pattern URL, altrimenti la URL dentro la parentesi verrebbe
    # mascherata lasciando '![alt]([[[URL_0000]]])' che il modello riscrive.
    (re.compile(r'!\[[^\]]*\]\([^)]*\)'), "IMAGE"),
    # Immagini in stile "bare" usate da alcuni convertitori: !https://...
    # (senza la sintassi '[alt](url)'); le proteggiamo come unità intera.
    (re.compile(r'!https?://\S+'), "IMAGE"),
    # Blocchi di codice con backtick tripli
    (re.compile(r'```[\s\S]*?```', re.DOTALL), "CODEBLOCK"),
    # Blocchi di codice con tilde tripla
    (re.compile(r'~~~[\s\S]*?~~~', re.DOTALL), "TILDEBLOCK"),
    # Formule matematiche display ($$…$$) — PRIMA di MATHINLINE
    (re.compile(r'\$\$[\s\S]*?\$\$', re.DOTALL), "MATHBLOCK"),
    # Formule LaTeX \[…\]
    (re.compile(r'\\\[[\s\S]*?\\\]', re.DOTALL), "LATEXBLOCK"),
    # Formule inline ($…$) — DOPO MATHBLOCK
    (re.compile(r'\$[^$\n]+\$'), "MATHINLINE"),
    # Formule LaTeX \(…\)
    (re.compile(r'\\\([\s\S]*?\\\)'), "LATEXINLINE"),
    # Codice inline (backtick singolo)
    (re.compile(r'`[^`\n]+`'), "CODEINLINE"),
    # URL nudi (http/https/ftp) — DOPO IMAGE
    (re.compile(r'https?://\S+|ftp://\S+'), "URL"),
]

_URL_TRAILING_PUNCT = ".,;:!?)]}'\""


def protect_blocks(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Rimpiazza i blocchi da non alterare con placeholder ASCII univoci.
    Restituisce (testo_mascherato, dizionario_ripristino).
    """
    placeholders: Dict[str, str] = {}
    counter = [0]

    def make_placeholder(tag: str, original: str) -> str:
        key = f"[[[{tag}_{counter[0]:04d}]]]"
        placeholders[key] = original
        counter[0] += 1
        return key

    def replace_url(m: re.Match) -> str:
        url = m.group(0)
        trailing = ""
        while url and url[-1] in _URL_TRAILING_PUNCT:
            trailing = url[-1] + trailing
            url = url[:-1]
        if not url:
            return m.group(0)
        return make_placeholder("URL", url) + trailing

    for pattern, tag in PROTECTED_PATTERNS:
        if tag == "URL":
            text = pattern.sub(replace_url, text)
        else:
            def _replacer(m: re.Match, _tag: str = tag) -> str:
                return make_placeholder(_tag, m.group(0))
            text = pattern.sub(_replacer, text)

    return text, placeholders


def restore_blocks(text: str, placeholders: Dict[str, str]) -> Tuple[str, List[str]]:
    """
    Ripristina i placeholder con il contenuto originale.
    Usa un approccio a punto fisso per gestire placeholder annidati.
    Restituisce (testo_ripristinato, lista_placeholder_non_risolti).
    """
    if placeholders:
        max_iterations = len(placeholders) + 2
        for _ in range(max_iterations):
            changed = False
            for key, original in placeholders.items():
                if key in text:
                    text = text.replace(key, original)
                    changed = True
            if not changed:
                break
        else:
            logging.warning(
                "restore_blocks: raggiunto il limite di iterazioni; "
                "potrebbero restare token non risolti."
            )

    missing = PLACEHOLDER_RE.findall(text)
    return text, missing


# ---------------------------------------------------------------------------
# Chiamata al modello — supporto streaming
# ---------------------------------------------------------------------------

def call_lmstudio(
    host: str,
    model: str,
    system_prompt: str,
    user_message: str,
    *,
    max_tokens: int = MAX_TOKENS,
    temperature: float = DEFAULT_TEMPERATURE,
    top_p: float = DEFAULT_TOP_P,
    timeout: int = DEFAULT_TIMEOUT,
    max_retries: int = DEFAULT_MAX_RETRIES,
    stream: bool = True,
) -> str:
    """
    Chiama il server LM Studio (API compatibile OpenAI) via HTTP.

    Con stream=True (default) la risposta viene letta riga per riga (SSE):
    questo evita che il timeout HTTP scatti durante generazioni lunghe, perché
    ogni token ricevuto "resetta" il timer di inattività della connessione.
    Con stream=False si usa il comportamento originale (attesa dell'intera
    risposta): utile per modelli che non supportano lo streaming.
    """
    url = f"{host}/v1/chat/completions"
    payload = {
        "model": model or "local-model",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "stream": stream,
    }
    data_bytes = json.dumps(payload).encode("utf-8")

    last_error: Exception = RuntimeError("Nessun tentativo eseguito")
    total_attempts = max_retries + 1

    for attempt in range(1, total_attempts + 1):
        try:
            request = urllib.request.Request(
                url,
                data=data_bytes,
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if stream:
                    return _read_stream(response)
                else:
                    return _read_full(response)

        except urllib.error.URLError as e:
            last_error = ConnectionError(
                f"Non riesco a connettermi a {host}. "
                f"Assicurati che LM Studio sia in esecuzione.\nDettagli: {e}"
            )
        except json.JSONDecodeError as e:
            last_error = RuntimeError(f"Risposta non JSON da LM Studio: {e}")
        except Exception as e:  # noqa: BLE001
            last_error = RuntimeError(f"Errore nella comunicazione con LM Studio: {e}")

        if attempt < total_attempts:
            wait = min(2 ** attempt, 30)
            logging.warning(
                "Tentativo %d/%d fallito (%s); nuovo tentativo tra %ds…",
                attempt, total_attempts, last_error, wait,
            )
            time.sleep(wait)

    raise last_error


def _read_full(response) -> str:
    """Legge la risposta completa (non-streaming) e ritorna il testo generato."""
    data = json.loads(response.read().decode("utf-8"))
    if "error" in data:
        raise RuntimeError(f"Errore LM Studio: {data['error']}")
    if not data.get("choices"):
        raise RuntimeError("Risposta vuota da LM Studio")
    choice = data["choices"][0]
    if choice.get("finish_reason") == "length":
        logging.warning(
            "Risposta troncata (finish_reason=length): valuta di aumentare "
            "--max-tokens o ridurre --chunk-size."
        )
    return choice["message"]["content"]


def _read_stream(response) -> str:
    """
    Legge una risposta SSE (Server-Sent Events) riga per riga e riassembla
    il testo generato. Compatibile con l'API /v1/chat/completions di LM Studio
    con stream=true.

    Formato SSE atteso:
        data: {"choices":[{"delta":{"content":"token"},"finish_reason":null}]}
        data: [DONE]
    """
    parts: List[str] = []
    finish_reason: Optional[str] = None

    for raw_line in response:
        line = raw_line.decode("utf-8").rstrip("\r\n")
        if not line.startswith("data: "):
            continue
        payload = line[6:]  # rimuove "data: "
        if payload == "[DONE]":
            break
        try:
            event = json.loads(payload)
        except json.JSONDecodeError:
            continue
        if "error" in event:
            raise RuntimeError(f"Errore LM Studio (stream): {event['error']}")
        choices = event.get("choices", [])
        if not choices:
            continue
        choice = choices[0]
        delta = choice.get("delta", {})
        content = delta.get("content")
        if content:
            parts.append(content)
        if choice.get("finish_reason"):
            finish_reason = choice["finish_reason"]

    if finish_reason == "length":
        logging.warning(
            "Risposta troncata (finish_reason=length): valuta di aumentare "
            "--max-tokens o ridurre --chunk-size."
        )
    return "".join(parts)


# ---------------------------------------------------------------------------
# Chunking — sliding window con taglio all'indietro sull'header più vicino
# ---------------------------------------------------------------------------

_HEADER_LINE_RE = re.compile(r'(?m)^#{1,3}[ \t]+')


def split_into_chunks(text: str, max_chars: int) -> List[str]:
    """
    Divide il testo in chunk di ~max_chars caratteri, tagliando sempre
    appena prima dell'header (#/##/###) più vicino trovato cercando
    all'indietro dal punto di max_chars.

    Fallback quando nella finestra non ci sono header:
    1. Doppio a capo (confine di paragrafo)
    2. Singolo a capo (confine di riga)
    3. Taglio a max_chars (ultima risorsa)
    """
    text_stripped = text.strip()
    if not text_stripped:
        return []
    if len(text_stripped) <= max_chars:
        return [text_stripped]

    # Pre-calcola le posizioni di tutti gli header (una volta sola, O(n))
    header_starts = sorted(m.start() for m in _HEADER_LINE_RE.finditer(text))

    chunks: List[str] = []
    start = 0
    n = len(text)

    while start < n:
        if n - start <= max_chars:
            tail = text[start:].strip()
            if tail:
                chunks.append(tail)
            break

        end = start + max_chars

        # Binary search: trova l'ultimo header con posizione <= end e > start.
        # Usiamo due variabili distinte (lo/hi per la ricerca, idx per il
        # risultato) per evitare il bug della versione precedente dove `hi`
        # veniva modificato in-place e poi riusato in modo incoerente.
        cut = -1
        lo, hi = 0, len(header_starts) - 1
        best_idx = -1  # indice in header_starts dell'header candidato
        while lo <= hi:
            mid = (lo + hi) // 2
            if header_starts[mid] <= end:
                best_idx = mid
                lo = mid + 1
            else:
                hi = mid - 1
        # Cammina all'indietro da best_idx per trovare un header > start
        while best_idx >= 0 and header_starts[best_idx] <= start:
            best_idx -= 1
        if best_idx >= 0 and header_starts[best_idx] > start:
            cut = header_starts[best_idx]

        if cut > 0:
            chunk = text[start:cut].strip()
            if chunk:
                chunks.append(chunk)
            start = cut
            continue

        # Fallback 1: doppio a capo
        region = text[start:end]
        para = region.rfind('\n\n')
        if para > 0:
            chunk = text[start:start + para].strip()
            if chunk:
                chunks.append(chunk)
            start = start + para
            while start < n and text[start] in '\n\r\t ':
                start += 1
            continue

        # Fallback 2: singolo a capo
        nl = region.rfind('\n')
        if nl > 0:
            chunk = text[start:start + nl].strip()
            if chunk:
                chunks.append(chunk)
            start = start + nl + 1
            continue

        # Fallback 3: taglio a max_chars
        chunk = region.strip()
        if chunk:
            chunks.append(chunk)
        start = end

    logging.info("Chunking: %d chunk (max %d car ciascuno)", len(chunks), max_chars)
    for i, chunk in enumerate(chunks, 1):
        first_line = chunk.split('\n', 1)[0][:80]
        logging.info("  Chunk %d: %d car — %s", i, len(chunk), first_line)

    return chunks


# ---------------------------------------------------------------------------
# Stato di resume (checkpoint per elaborazioni lunghe)
# ---------------------------------------------------------------------------

class ResumeState:
    """
    Persiste i chunk già elaborati su disco (JSON) per poter riprendere
    un'elaborazione interrotta senza rifare le chiamate al modello.

    Formato del file JSON:
        {
            "source_hash": "<sha256 del testo sorgente>",
            "chunk_size": <int>,
            "chunks": ["chunk0_testo", "chunk1_testo", ...],
            "results": {"0": "chunk0_output", "2": "chunk2_output", ...}
        }

    I risultati sono indicizzati come stringhe perché JSON non supporta
    chiavi intere. L'hash del sorgente garantisce che il resume venga
    invalidato se il file di input cambia tra un'esecuzione e l'altra.
    """

    def __init__(self, path: Optional[str] = None):
        self.path = Path(path) if path else None
        self._data: Dict = {}

    @staticmethod
    def _hash(text: str) -> str:
        import hashlib
        return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

    def load(self, source: str, chunks: List[str], chunk_size: int) -> Dict[int, str]:
        """
        Carica i risultati già calcolati se il file di stato esiste e
        corrisponde al sorgente corrente. Restituisce un dizionario
        {indice_chunk: testo_risultato} con solo i chunk già completati.
        """
        if not self.path or not self.path.exists():
            return {}

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            logging.warning("Stato di resume non leggibile (%s): si riparte da zero.", e)
            return {}

        expected_hash = self._hash(source)
        if self._data.get("source_hash") != expected_hash:
            logging.warning(
                "Il file di stato non corrisponde al sorgente corrente "
                "(hash diverso): si riparte da zero."
            )
            return {}

        if self._data.get("chunk_size") != chunk_size:
            logging.warning(
                "Il file di stato usa chunk_size=%d, ora è %d: si riparte da zero.",
                self._data.get("chunk_size"), chunk_size,
            )
            return {}

        results = {int(k): v for k, v in self._data.get("results", {}).items()}
        if results:
            logging.info(
                "Resume: trovati %d chunk già elaborati su %d totali.",
                len(results), len(chunks),
            )
        return results

    def save(self, source: str, chunks: List[str], chunk_size: int,
             results: Dict[int, str]) -> None:
        if not self.path:
            return
        data = {
            "source_hash": self._hash(source),
            "chunk_size": chunk_size,
            "chunks": chunks,
            "results": {str(k): v for k, v in results.items()},
        }
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            logging.warning("Impossibile scrivere il file di stato: %s", e)


# ---------------------------------------------------------------------------
# Pipeline di ristrutturazione
# ---------------------------------------------------------------------------

def translate_chunk(host: str, model: str, chunk: str, *,
                    max_tokens: int, temperature: float, top_p: float,
                    timeout: int, max_retries: int, stream: bool) -> str:
    user_message = CHUNK_PROMPT_TEMPLATE.format(chunk=chunk)
    return call_lmstudio(
        host, model, SYSTEM_PROMPT, user_message,
        max_tokens=max_tokens, temperature=temperature, top_p=top_p,
        timeout=timeout, max_retries=max_retries, stream=stream,
    )


def process_markdown(
    source: str,
    host: str,
    model: str,
    chunk_size: int,
    out_fh=None,
    *,
    max_tokens: int = MAX_TOKENS,
    temperature: float = DEFAULT_TEMPERATURE,
    top_p: float = DEFAULT_TOP_P,
    timeout: int = DEFAULT_TIMEOUT,
    max_retries: int = DEFAULT_MAX_RETRIES,
    stream: bool = True,
    resume_state: Optional[ResumeState] = None,
    dry_run: bool = False,
) -> Tuple[str, List[str]]:
    """
    Pipeline:
      1. Proteggi blocchi speciali (placeholder ASCII)
      2. Suddividi in chunk sui confini di sezione/header
      3. (opzionale) Carica i risultati già calcolati dal file di stato
      4. Elabora ogni chunk via LM Studio (saltando quelli già completati)
      5. Ripristina i blocchi speciali chunk per chunk
      6. (opzionale) Salva lo stato dopo ogni chunk completato

    dry_run=True: stampa i chunk su stderr e restituisce il testo originale
    mascherato senza chiamare il modello.
    """
    masked, placeholders = protect_blocks(source)
    chunks = split_into_chunks(masked, chunk_size)
    total = len(chunks)

    if dry_run:
        logging.info("DRY RUN: %d chunk, nessuna chiamata al modello.", total)
        for i, chunk in enumerate(chunks, 1):
            print(f"\n{'='*60}\n# CHUNK {i}/{total} ({len(chunk)} car)\n{'='*60}", file=sys.stderr)
            print(chunk, file=sys.stderr)
        # Ripristina e restituisce il testo originale inalterato
        restored, missing = restore_blocks(masked, placeholders)
        return restored, missing

    # Carica checkpoint se disponibile
    already_done: Dict[int, str] = {}
    if resume_state:
        already_done = resume_state.load(source, chunks, chunk_size)

    all_missing: List[str] = []
    results: Dict[int, str] = dict(already_done)  # copia per non modificare l'originale
    output_parts: List[str] = []

    for i, chunk in enumerate(chunks):
        chunk_num = i + 1  # 1-based per i log

        if i in already_done:
            logging.info(
                "Chunk %d/%d: già elaborato (resume), salto.", chunk_num, total
            )
            restored, missing = restore_blocks(already_done[i], placeholders)
        else:
            logging.info(
                "Elaborazione chunk %d/%d (%d caratteri)…", chunk_num, total, len(chunk)
            )
            processed = translate_chunk(
                host, model, chunk,
                max_tokens=max_tokens, temperature=temperature, top_p=top_p,
                timeout=timeout, max_retries=max_retries, stream=stream,
            )
            restored, missing = restore_blocks(processed, placeholders)
            results[i] = processed  # salva il risultato NON ripristinato (per il resume)

            if resume_state:
                resume_state.save(source, chunks, chunk_size, results)

        if missing:
            logging.warning(
                "%d placeholder non risolti nel chunk %d: %s",
                len(missing), chunk_num, missing,
            )
            all_missing.extend(missing)

        output_parts.append(restored)

        if out_fh is not None:
            separator = "\n\n" if chunk_num > 1 else ""
            out_fh.write(separator + restored)
            out_fh.flush()

    return "\n\n".join(output_parts), all_missing


# ---------------------------------------------------------------------------
# Post-processing: riparazione sintattica del Markdown generato
# ---------------------------------------------------------------------------

def normalize_markdown(content: str) -> str:
    """
    Riparazione automatica del Markdown generato dal modello.

    Operazioni eseguite:
    1. Rimuove artefatti testuali noti ("Cosa significa?", eccessi di righe vuote)
    2. Normalizza delimitatori math ridondanti ('$$$' o '$$$$' → '$$')
    3. Forza il prefisso '>' sulle righe di blocchi '$$..$$' che si trovano
       dentro un callout Obsidian ma ne sono privi
    4. Collassa blocchi '$$' vuoti (apertura e chiusura su righe consecutive)
    5. Inserisce una riga vuota di separazione tra didascalie "Tabella N:" e
       la riga di pipe '|' che le segue (richiesto dal parser Markdown)

    NOTA: questa funzione non tocca i placeholder [[[TIPO_NNNN]]] perché
    restore_blocks() è già stato chiamato prima di arrivare qui.
    """
    content = re.sub(r'[ \t]*Cosa significa\?[ \t]*\n?', '', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.replace("$$$$", "$$")
    content = content.replace("$$$", "$$")

    lines = content.split("\n")

    delim_re = re.compile(r"^(?P<prefix>(?:\s*>)+\s*)?\$\$\s*$")
    callout_header_re = re.compile(r"^(?:\s*>)+\s*\[\s*!")
    boundary_re = re.compile(r"^\s*(#{1,3}\s|(?:\s*>)+\s*\[\s*!)")

    # Traccia se una riga si trova dentro un callout Obsidian attivo
    in_callout = [False] * len(lines)
    callout_flag = False
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if callout_header_re.match(stripped):
            callout_flag = True
        elif stripped == "":
            callout_flag = False
        in_callout[idx] = callout_flag

    delim_indices: List[Tuple[int, str]] = []
    for idx, line in enumerate(lines):
        m = delim_re.match(line)
        if m:
            prefix = m.group("prefix") or ""
            delim_indices.append((idx, prefix))

    if len(delim_indices) % 2 != 0:
        idx_last, _ = delim_indices[-1]
        logging.warning(
            "normalize_markdown: numero dispari di delimitatori '$$' "
            "(riga %d esclusa dall'accoppiamento, resta invariata).",
            idx_last + 1,
        )

    to_collapse: set = set()
    for k in range(0, len(delim_indices) - 1, 2):
        idx_open, prefix_open = delim_indices[k]
        idx_close, prefix_close = delim_indices[k + 1]
        gt_open, gt_close = bool(prefix_open), bool(prefix_close)

        if idx_close == idx_open + 1:
            # Blocco vuoto: collassa in una sola riga '$$'
            prefix = prefix_open if len(prefix_open) >= len(prefix_close) else prefix_close
            if not prefix and (gt_open or gt_close):
                prefix = "> "
            lines[idx_open] = f"{prefix}$$" if prefix else "$$"
            to_collapse.add(idx_close)
            continue

        if not (gt_open or gt_close) or not in_callout[idx_open]:
            continue

        suspect = any(
            boundary_re.match(lines[i]) for i in range(idx_open + 1, idx_close)
        )
        if suspect:
            logging.warning(
                "normalize_markdown: coppia '$$' righe %d-%d scartata "
                "(confine strutturale nel mezzo).", idx_open + 1, idx_close + 1,
            )
            continue

        prefix = prefix_open if prefix_open.strip() else prefix_close
        for idx in range(idx_open, idx_close + 1):
            line = lines[idx]
            if not line.strip().startswith(">"):
                lines[idx] = f"{prefix}{line}" if line else prefix.rstrip()

    if to_collapse:
        lines = [line for idx, line in enumerate(lines) if idx not in to_collapse]

    # Inserisce riga vuota tra "Tabella N: ..." e la riga di pipe '|' successiva
    prefix_re = re.compile(r"^((?:\s*>)+\s*)?")

    def split_prefix(line: str) -> Tuple[str, str]:
        m = prefix_re.match(line)
        prefix = m.group(1) or ""
        return prefix, line[len(prefix):]

    lines_out: List[str] = []
    for idx, line in enumerate(lines):
        lines_out.append(line)
        prefix, rest = split_prefix(line)
        if rest.strip().startswith("Tabella") and idx + 1 < len(lines):
            _, next_rest = split_prefix(lines[idx + 1])
            if next_rest.lstrip().startswith("|"):
                blank = prefix.rstrip() if prefix.strip().startswith(">") else ""
                lines_out.append(blank)

    return "\n".join(lines_out)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Ristruttura un file Markdown applicando una style guide "
            "accademica, usando LM Studio come backend locale."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Esempi:
              python Formatta_Slide.py appunti.md
              python Formatta_Slide.py appunti.md -o output.md
              python Formatta_Slide.py appunti.md --host http://localhost:1234
              python Formatta_Slide.py appunti.md --model mistral-7b-instruct-v0.2
              python Formatta_Slide.py appunti.md --chunk-size 3000
              python Formatta_Slide.py appunti.md --max-tokens 4096 --max-retries 3
              python Formatta_Slide.py appunti.md --resume stato.json -o output.md
              python Formatta_Slide.py appunti.md --dry-run
              python Formatta_Slide.py appunti.md --no-stream
        """),
    )
    parser.add_argument("input",
                        help="File Markdown di input")
    parser.add_argument("-o", "--output",
                        help="File di output (default: stdout). Scrittura incrementale chunk per chunk.",
                        default=None)
    parser.add_argument("--host",
                        default=DEFAULT_HOST,
                        metavar="URL",
                        help=f"Indirizzo del server LM Studio (default: {DEFAULT_HOST})")
    parser.add_argument("--model",
                        default=DEFAULT_MODEL,
                        metavar="NOME",
                        help="Nome del modello da usare (LM Studio di solito lo ignora con un solo modello caricato).")
    parser.add_argument("--chunk-size",
                        type=int,
                        default=4000,
                        metavar="N",
                        help="Caratteri max per chunk (default: 4000).")
    parser.add_argument("--max-tokens",
                        type=int,
                        default=MAX_TOKENS,
                        metavar="N",
                        help=f"Token massimi di output per chunk (default: {MAX_TOKENS}).")
    parser.add_argument("--temperature",
                        type=float,
                        default=DEFAULT_TEMPERATURE,
                        metavar="T",
                        help=f"Temperature di generazione (default: {DEFAULT_TEMPERATURE}).")
    parser.add_argument("--top-p",
                        type=float,
                        default=DEFAULT_TOP_P,
                        metavar="P",
                        help=f"Top-p di generazione (default: {DEFAULT_TOP_P}).")
    parser.add_argument("--timeout",
                        type=int,
                        default=DEFAULT_TIMEOUT,
                        metavar="SEC",
                        help=f"Timeout per richiesta HTTP in secondi (default: {DEFAULT_TIMEOUT}).")
    parser.add_argument("--max-retries",
                        type=int,
                        default=DEFAULT_MAX_RETRIES,
                        metavar="N",
                        help=f"Tentativi aggiuntivi in caso di errore di connessione (default: {DEFAULT_MAX_RETRIES}).")
    parser.add_argument("--resume",
                        default=None,
                        metavar="FILE",
                        help="File JSON di stato per riprendere un'elaborazione interrotta. "
                             "Viene creato/aggiornato automaticamente dopo ogni chunk completato.")
    parser.add_argument("--no-stream",
                        action="store_true",
                        help="Disabilita lo streaming SSE (attende l'intera risposta). "
                             "Utile se il modello non supporta stream=true.")
    parser.add_argument("--dry-run",
                        action="store_true",
                        help="Mostra i chunk su stderr senza chiamare il modello. "
                             "Utile per verificare il chunking prima di avviare l'elaborazione.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stderr)

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            source = f.read()
    except FileNotFoundError:
        logging.error("File non trovato: %s", args.input)
        sys.exit(1)
    except OSError as e:
        logging.error("Impossibile leggere %s: %s", args.input, e)
        sys.exit(1)

    resume_state = ResumeState(args.resume) if args.resume else None
    stream = not args.no_stream

    out_fh = None
    try:
        if args.output and not args.dry_run:
            out_fh = open(args.output, "w", encoding="utf-8")

        result, missing = process_markdown(
            source,
            host=args.host,
            model=args.model,
            chunk_size=args.chunk_size,
            out_fh=out_fh,
            max_tokens=args.max_tokens,
            temperature=args.temperature,
            top_p=args.top_p,
            timeout=args.timeout,
            max_retries=args.max_retries,
            stream=stream,
            resume_state=resume_state,
            dry_run=args.dry_run,
        )
    except Exception as e:
        logging.error("Errore: %s", e)
        sys.exit(1)
    finally:
        if out_fh:
            out_fh.close()

    if args.dry_run:
        logging.info("Dry run completato. Nessun file scritto.")
        return

    final_output = normalize_markdown(result)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(final_output)
        logging.info("Output scritto in: %s", args.output)
    else:
        print(final_output)

    if missing:
        logging.warning("%d placeholder non risolti in totale.", len(missing))


if __name__ == "__main__":
    main()
