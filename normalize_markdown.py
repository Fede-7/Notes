#!/usr/bin/env python3
import sys
import re
import argparse

def normalize_markdown(content: str) -> str:
    """
    Riparazione automatica dei Callout Markdown.

    Regola applicata: le righe composte SOLO da '$$' vengono accoppiate in
    ordine di apparizione (1a con 2a, 3a con 4a, ...), ossia apertura/
    chiusura dello stesso blocco formula. Se UNA delle due righe del paio è
    preceduta da '>', il '>' viene forzato anche sull'altra e su ogni riga
    di contenuto compresa tra le due (il corpo della formula), cosi'
    l'intero blocco resta correttamente dentro il callout.
    """
    content = content.replace("Cosa significa?", "")

    # Normalizza delimitatori math ridondanti: '$$$$' o '$$$' -> '$$'
    # (l'ordine conta: prima il caso a 4 simboli, poi quello a 3, altrimenti
    # '$$$$' verrebbe letto come due '$$' consecutivi e trattato male)
    content = content.replace("$$$$", "$$")
    content = content.replace("$$$", "$$")

    lines = content.split("\n")
    # riga fatta SOLO di '$$', con o senza '>' davanti
    delim_re = re.compile(r"^(?P<prefix>>\s*)?\$\$\s*$")

    delim_indices = []
    for idx, line in enumerate(lines):
        m = delim_re.match(line)
        if m:
            has_gt = m.group("prefix") is not None
            delim_indices.append((idx, has_gt))

    # accoppio per ordine di apparizione: 1a-2a = blocco 1 (apertura/chiusura),
    # 3a-4a = blocco 2, ecc. Il confine tra la chiusura di un blocco e
    # l'apertura del successivo (es. "> $$" seguito da "> $$" di un'altra
    # formula) NON è mai una coppia e quindi non va mai toccato qui.
    to_collapse = set()  # indici delle righe di chiusura da rimuovere (blocco vuoto)
    for k in range(0, len(delim_indices) - 1, 2):
        idx_open, gt_open = delim_indices[k]
        idx_close, gt_close = delim_indices[k + 1]

        if idx_close == idx_open + 1:
            # Blocco vuoto: apertura e chiusura sono la stessa coppia e non
            # hanno nessuna riga di formula in mezzo -> collassa in una sola '$$'.
            prefix = "> " if (gt_open or gt_close) else ""
            lines[idx_open] = f"{prefix}$$"
            to_collapse.add(idx_close)
        elif gt_open or gt_close:
            # Blocco con contenuto: se una delle due righe ha '>', lo forziamo
            # anche sull'altra e su tutto il contenuto in mezzo.
            for idx in range(idx_open, idx_close + 1):
                line = lines[idx]
                stripped = line.strip()
                if not stripped.startswith(">"):
                    lines[idx] = f"> {line}" if line else ">"

    if to_collapse:
        lines = [line for idx, line in enumerate(lines) if idx not in to_collapse]

    # Regola: se una riga è una didascalia "Tabella ..." ed è seguita
    # direttamente da una riga che inizia con '|' (riga di tabella), va
    # inserita una riga vuota di separazione tra le due (richiesto da
    # Markdown per riconoscere correttamente la tabella).
    prefix_re = re.compile(r"^(>+\s*)?")

    def split_prefix(line: str):
        m = prefix_re.match(line)
        prefix = m.group(1) or ""
        return prefix, line[len(prefix):]

    lines_with_tables = []
    for idx, line in enumerate(lines):
        lines_with_tables.append(line)

        prefix, rest = split_prefix(line)
        if rest.strip().startswith("Tabella") and idx + 1 < len(lines):
            next_prefix, next_rest = split_prefix(lines[idx + 1])
            if next_rest.lstrip().startswith("|"):
                blank = prefix.rstrip() if prefix.strip().startswith(">") else ""
                lines_with_tables.append(blank)

    lines = lines_with_tables

    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Normalizza la formattazione dei callout, dei blocchi math e delle tabelle in un file Markdown (stile Obsidian)."
    )
    parser.add_argument("input", help="File Markdown di input (usa '-' per leggere da stdin)")
    parser.add_argument("-o", "--output", help="File di output (default: stampa su stdout)", default=None)

    args = parser.parse_args()

    try:
        if args.input == "-":
            content = sys.stdin.read()
        else:
            with open(args.input, "r", encoding="utf-8") as f:
                content = f.read()
    except Exception as e:
        print(f"Errore nella lettura dell'input: {e}", file=sys.stderr)
        sys.exit(1)

    normalized_content = normalize_markdown(content)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(normalized_content)
            print(f"File normalizzato salvato in: {args.output}", file=sys.stderr)
        except Exception as e:
            print(f"Errore nel salvataggio dell'output: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(normalized_content, end="")

if __name__ == "__main__":
    main()
