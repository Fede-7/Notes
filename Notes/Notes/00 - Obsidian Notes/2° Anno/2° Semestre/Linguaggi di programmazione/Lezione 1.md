---
date: 2026-03-12
corso: Linguaggi di Programmazione
docente: (da inserire)
lezione: 1
tags:
  - LP
  - semplicità
  - ortogonalità
  - tipi
  - astrazione
  - nomi
  - ambiente
  - scope
  - binding
  - blocchi
Professore: Bonatti
---

# LP — Lezione 1: Criteri di valutazione dei linguaggi, paradigmi a confronto, modello imperativo e ambiente

**Corso:** Linguaggi di Programmazione

---

## Argomenti trattati

- Riepilogo pipeline del compilatore e anticipazione dei concetti di ambiente e memoria
- Criteri di valutazione dei linguaggi: semplicita, astrazione, espressivita, ortogonalita, portabilita
- Zucchero sintattico
- Paradigmi di programmazione: imperativo, funzionale, logico, a oggetti, concorrente
- Confronto tra paradigmi: fattoriale e funzione membro
- Invertibilita dei programmi logici (Prolog)
- Modello imperativo: memoria come funzione, assegnamento
- Nomi, ambiente (environment) e memoria (store)
- Ambiente nei diversi paradigmi (imperativo, funzionale, logico)
- Valutazione di espressioni con puntatori: env e mem nel C

---

## Riepilogo: pipeline del compilatore

La lezione riprende dal diagramma di flusso del compilatore visto nella lezione precedente. Il docente anticipa che, oltre alle fasi gia discusse (analisi lessicale, sintattica, semantica, generazione del codice), verranno introdotti concetti astratti — come **ambiente** e **memoria** — che sono sia astrazioni concettuali visibili nella sintassi del linguaggio, sia strutture dati interne manipolate dal compilatore durante la generazione del codice.

---

## Criteri di valutazione dei linguaggi

Quando si sceglie o si progetta un linguaggio, esistono diversi **criteri di valutazione**. Non sono sempre allineati tra loro: migliorare uno puo peggiorare un altro.

### Semplicita: concisione vs leggibilita

> [!abstract] Definizione: Semplicita
> La semplicita di un linguaggio puo essere intesa in due accezioni distinte:
> - **Concisione**: capacita di esprimere funzionalita complesse in modo molto compatto.
> - **Leggibilita**: facilita con cui un programmatore riesce a comprendere codice scritto da altri.
>
> Le due accezioni **non sono necessariamente allineate**.

> [!example] N-Queens in Prolog
> Nel libro di Sterling e Shapiro si trova un codice Prolog che risolve il problema delle N regine (piazzare N regine su una scacchiera NxN senza che si attacchino) in circa **10 righe**. Tuttavia, comprendere quel codice richiede una conoscenza approfondita del paradigma logico e dell'unificazione.

> [!tip] Parole del Professore
> > [!quote]
> > "Quel codice che risolve il problema delle N regine e lungo 10 righe, una roba di questo genere. Pero io, che sono un esperto in linguaggi di programmazione logica, ci sono cresciuto --- per capire come funzionava ci ho passato il pomeriggio. Quindi concisione non vuol dire necessariamente leggibilita."

La semplicita puo anche significare **semplicita sintattica**: pochi costrutti, pochi modi di fare la stessa cosa, il che facilita l'apprendimento.

> [!warning] Esempio negativo: C++
> In C++ si possono creare record usando `struct` oppure `class`. Ci sono sovrapposizioni e tanti modi diversi di fare la stessa cosa. Questo riduce la semplicita sintattica.

### Astrazione

L'astrazione si declina in due forme:

| Tipo di astrazione | Descrizione | Evoluzione storica |
|---|---|---|
| **Astrazione sui dati** | Creare nuovi tipi di dati che nascondano i dettagli implementativi (encapsulation) | Dai record di COBOL alle classi Java |
| **Astrazione procedurale** | Generalizzare pezzi di codice in procedure riusabili | Dalle subroutine FORTRAN ai metodi OO |

### Espressivita e zucchero sintattico

L'espressivita misura quante cose un linguaggio puo esprimere e quanto facilmente. Le versioni recenti di Java, dopo le aggiunte fondamentali (tipi parametrici/generics, modello di sicurezza), hanno introdotto soprattutto **zucchero sintattico** (*syntactic sugar*).

> [!abstract] Definizione: Zucchero sintattico
> Un'abbreviazione che consente di scrivere in modo piu compatto e leggibile cose che il linguaggio gia supportava. **Non aggiunge funzionalita** al linguaggio: puo essere trattato con un preprocessore che espande le abbreviazioni nel vecchio linguaggio prima della compilazione.

### Ortogonalita

> [!abstract] Definizione: Ortogonalita
> Un linguaggio e **ortogonale** quando ha poche eccezioni alle proprie regole: e molto regolare, e dove si puo usare una categoria sintattica si possono usare tutte le sue istanziazioni. Dove trovo un identificatore, puo essere un identificatore qualsiasi; dove trovo una chiamata a funzione, puo essere una chiamata a qualsiasi funzione.

> [!tip] Parole del Professore
> > [!quote]
> > "I linguaggi moderni sono tutti molto ortogonali, perche vengono costruiti con grammatiche che dicono come ogni costrutto puo essere realizzato. Inizialmente, nel tempo di FORTRAN, i parser si scrivevano a mano e c'erano cose che si potevano usare in certi contesti ma non in altri."

### Portabilita e fattori esterni

La **portabilita** e fortemente influenzata dal tipo di implementazione (compilazione pura vs approccio ibrido bytecode+VM). Oltre ai criteri tecnici, la scelta di un linguaggio dipende anche da fattori esterni:

- Disponibilita di compilatori/interpreti per la piattaforma target
- Investimenti aziendali preesistenti nella formazione del personale
- Standard normativi (es. Ada era obbligatorio per il software federale USA)
- Qualita degli strumenti di supporto alla programmazione (IDE, debugger, ecc.)

---

## Paradigmi di programmazione

### I tre paradigmi fondamentali

| Paradigma | Modello di esecuzione | Concetto chiave |
|---|---|---|
| **Imperativo** | Sequenza di istruzioni che modificano lo stato della memoria | Assegnamento, cicli, evoluzione temporale |
| **Funzionale** | Valutazione di espressioni, niente assegnamenti | Ricorsione, immutabilita, funzioni |
| **Logico** | Dimostrazione di asserzioni logiche (implicazioni) | Predicati, unificazione, non-determinismo |

### Paradigmi trasversali

- **A oggetti**: struttura l'associazione tra dati e procedure. E ortogonale ai tre paradigmi fondamentali: esistono linguaggi imperativi a oggetti (Java, C++), funzionali a oggetti (OCaml, Haskell), logici a oggetti.
- **Concorrente/parallelo**: aggiunge costrutti per la sincronizzazione e la gestione di processi paralleli. Anche questo e trasversale: esistono linguaggi imperativi concorrenti, funzionali concorrenti, logici concorrenti.

---

## Confronto tra paradigmi: esempi

### Fattoriale

**Imperativo** --- ciclo con accumulatore:

```
function fact(n):
    accumulator := 1
    for i := 1 to n:
        accumulator := accumulator * i
    return accumulator
```

Il modello imperativo prevede un'**evoluzione dello stato della memoria**: le variabili `i` e `accumulator` cambiano valore ad ogni passo.

**Funzionale** --- ricorsione pura:

```
function fact(n):
    if n = 1 then 1
    else n * fact(n - 1)
```

Non c'e memoria che cambia. L'evoluzione temporale e rimpiazzata dallo **stack di attivazione**: ogni livello di ricorsione crea un nuovo ambiente con il proprio valore di `n`.

> [!warning] Relazione fondamentale
> Passare dall'imperativo al funzionale (e viceversa) si riduce a trasformare **iterazioni in ricorsioni**. Lavorare nel paradigma funzionale significa: niente assegnamenti, ergo niente cicli (un ciclo richiede una variabile che cambia valore; senza assegnamenti, la condizione e sempre vera o sempre falsa).

### Funzione `member(x, L)`

Verifica se l'elemento `x` compare nella lista `L`. Funzioni ausiliarie presupposte: `vuota(L)`, `testa(L)` (primo elemento), `coda(L)` (tutto cio che segue il primo elemento).

**Imperativo (pseudocodice / C)**:

```
procedure member(x, L):
    L1 := L
    while not vuota(L1) and testa(L1) != x:
        L1 := coda(L1)
    return not vuota(L1)
```

```c
bool member(int x, list L) {
    list L1 = L;
    while (!empty(L1) && x != head(L1))
        L1 = tail(L1);
    return !empty(L1);
}
```

> [!tip] Parole del Professore
> > [!quote]
> > "Questi due programmi hanno esattamente la stessa struttura. Cosa cambia? I blocchi con indentazione vs parentesi graffe, il terminatore punto-e-virgola, NOT vs punto esclamativo. Ma sono dettagli sintattici. Lo stesso paradigma vuol dire che lo stesso problema ha le stesse soluzioni algoritmiche."

**Funzionale (pseudocodice / Lisp)**:

```
function member(x, L):
    if vuota(L) then false
    else if testa(L) = x then true
    else member(x, coda(L))
```

```lisp
(defun member (x L)
  (cond ((null L) nil)
        ((equal x (first L)) t)
        (t (member x (rest L)))))
```

> [!tip] Parole del Professore
> > [!quote]
> > "Le parentesi di Lisp derivano dal fatto che e un linguaggio nato in accademia, dove si sono semplificati la vita nella costruzione del parser scegliendo questa sintassi molto semplice a liste. L'intenzione era metterci una sintassi piu amichevole all'esterno. Non e mai successo."

**C in stile funzionale** (senza assegnamenti, con l'operatore ternario):

```c
bool member(int x, list L) {
    return empty(L) ? false :
           x == head(L) ? true :
           member(x, tail(L));
}
```

**Logico (Prolog)**:

```prolog
member(X, [X | _]).
member(X, [_ | L]) :- member(X, L).
```

Il primo assioma dice: per ogni X e L, X e membro della lista che comincia con X. Il secondo dice: se X e membro di L (la coda), allora e anche membro di qualunque lista che ha L come coda.

> [!warning] Differenza radicale
> In Prolog non si dice **come** risolvere il problema, ma **cos'e** una soluzione. L'interprete applica le regole logiche cercando di dimostrare l'asserzione richiesta.

### Invertibilita dei programmi logici

> [!abstract] Definizione: Invertibilita
> Nei programmi logici **non c'e distinzione tra input e output**. Se un argomento e fissato (costante), funge da input; se e lasciato come variabile libera, diventa un output che il sistema calcola.

Esempi di uso di `member` in Prolog:

| Chiamata             | Significato                    | Risultato       |            |                     |
| -------------------- | ------------------------------ | --------------- | ---------- | ------------------- |
| `member(2, [1,2,3])` | 2 compare nella lista?         | `yes`           |            |                     |
| `member(0, [1,2,3])` | 0 compare nella lista?         | `no`            |            |                     |
| `member(X, [1,2,3])` | Quali X compaiono nella lista? | `X=1; X=2; X=3` |            |                     |
| `member(1, L)`       | Quali liste contengono 1?      | `L=[1           | _]; L=[_,1 | _]; ...` (infinite) |

> [!tip] Parole del Professore
> > [!quote]
> > "Lo stesso codice lo posso usare come funzione booleana, come generatore, come iteratore. Con poche righe si fa una semplice AI per giocare a Tris, dove lo stesso pezzo di codice lo uso per valutare strategie vincenti, per giocare, per esplorare le mosse successive."

### Conclusione sui paradigmi

> [!tip] Parole del Professore
> > [!quote]
> > "Imparato a risolvere il problema in un linguaggio, so risolverlo in qualunque linguaggio dello stesso paradigma. La curva di apprendimento si accelera molto: devo soltanto andarmi a vedere il manuale."

Oltre al paradigma, contano anche: il **sistema di tipi**, la **gestione delle eccezioni**, il supporto alla **concorrenza**.

---

## Il modello imperativo: memoria, nomi e ambiente

### La memoria come funzione

> [!abstract] Definizione: Memoria (store)
> Nel modello imperativo, la memoria e concettualmente una funzione:
>
> **mem : Locazione -> Valore**
>
> Data una locazione (indirizzo), restituisce il valore contenuto in quella cella. Viene modificata dalle **assegnazioni**.

### Assegnamento in notazione BNF

```
<assegnazione> ::= <nome> <operatore_assegnamento> <espressione>
```

Dove `<nome>`, `<operatore_assegnamento>` e `<espressione>` sono categorie sintattiche. In Pascal: `A := B + C`. In C: `A = B + C`.

**Semantica dell'assegnamento**: si calcola il valore di `<espressione>` e lo si memorizza nella locazione corrispondente a `<nome>`. Dopo l'esecuzione: `mem(locazione_del_nome) = valore_dell'espressione`.

### Dai nomi alle locazioni: l'ambiente (environment)

Nei linguaggi di alto livello, non si lavora con indirizzi numerici ma con **nomi** (identificatori). Per passare dal nome al valore servono **due passi**.

> [!abstract] Definizione: Ambiente (environment)
> L'ambiente e una funzione:
>
> **env : Nome -> Locazione**
>
> Associa ogni identificatore alla locazione di memoria corrispondente. E l'associazione tra il nome e cio che rappresenta.

Per ottenere il valore di una variabile `x` nel paradigma imperativo:

```
valore(x) = mem(env(x))
```

Composizione di due funzioni: prima si trova la locazione (`env`), poi si legge il contenuto (`mem`).

### Ambiente nei diversi paradigmi

| Paradigma | env mappa... | Memoria separata? |
|---|---|---|
| **Imperativo** | Nome -> Locazione (poi mem: Locazione -> Valore) | Si, `mem` e separata e mutabile |
| **Funzionale** | Nome -> Valore (direttamente) | No, non c'e memoria mutabile |
| **Logico** | Comportamento piu complesso: variabili passano da "non definite" a "definite" | Meccanismo diverso |

> [!warning] Proprieta fondamentale
> L'ambiente (`env`) e **immutabile** all'interno di un singolo contesto di esecuzione. Finche resto dentro una funzione, l'associazione nome-locazione non cambia. Cio che cambia e il **contenuto della memoria** (`mem`), modificato dagli assegnamenti. Quando si entra in un nuovo blocco o si fa una chiamata ricorsiva, si passa a un **ambiente diverso**.

> [!tip] Parole del Professore
> > [!quote]
> > "Quando faccio una chiamata al fattoriale, `n` viene associato dall'ambiente direttamente a 4 e non cambia per tutta l'esecuzione di quel livello di ricorsione. Quando faccio la chiamata ricorsiva e dentro `n` diventa 3, quello e un altro `n` perche sta in un altro contesto, in un ambiente diverso."

---

## Left-value e right-value: l'assegnamento nel dettaglio

Nell'assegnamento `x = x + 1`:

- La `x` **a sinistra** indica la **locazione** dove salvare il risultato: il compilatore calcola `env(x)`.
- La `x` **a destra** indica il **valore** della variabile: il compilatore calcola `mem(env(x))`.

> [!warning] Regola generale
> A **sinistra** dell'assegnamento serve solo l'indirizzo (un `mem` in meno). A **destra** serve il valore completo. Quando la stessa espressione compare a sinistra anziche a destra, si toglie un livello di `mem`.

### Esempi con i puntatori in C

**`x = y`** (assegnamento semplice):
- Sinistra: `env(x)` --- serve solo l'indirizzo di `x`
- Destra: `mem(env(y))` --- serve il valore di `y`

**`x = &y`** (indirizzo di `y`):
- Sinistra: `env(x)`
- Destra: `env(y)` --- non serve `mem`, basta la locazione

> [!warning] Errore di tipo: `&x` a sinistra
> `&(&x)` non e possibile. L'operatore `&` (che corrisponde a `env`) vuole un **nome**, non una locazione. `&x` a destra restituisce gia una locazione; applicare `&` a una locazione e un errore di tipo.

**`*p = x`** (scrittura tramite puntatore):
- Sinistra: `mem(env(p))` --- si legge il contenuto di `p` (che e un indirizzo) e quello diventa la locazione target
- Destra: `mem(env(x))` --- il valore di `x`

**`x = *p`** (lettura tramite puntatore):
- Sinistra: `env(x)`
- Destra: `mem(mem(env(p)))` --- si segue la catena: dove sta `p`, cosa contiene (un indirizzo), cosa contiene quell'indirizzo (il valore)

**`x = **p`** (doppia dereferenziazione):
- Destra: `mem(mem(mem(env(p))))` --- tre livelli di `mem`

> [!warning] Regola fondamentale: `env(mem(...))` non esiste mai
> `env` vuole un **nome** (un simbolo del codice sorgente). `mem` restituisce un **valore** (un dato a runtime). Scrivere `env(mem(...))` e sempre un errore concettuale: i due domini sono incompatibili.

> [!tip] Parole del Professore
> > [!quote]
> > "Quando ci dovete ragionare, partite dall'inizio della catena dei puntatori, da quello esplicito che sta li col nome, e procedete incrementalmente."

---

## Esercizi tipici d'esame

Il docente segnala che un esercizio ricorrente nel compito e:

1. **Da C a env/mem**: data un'istruzione C con puntatori, scrivere la traduzione in termini di `env` e `mem` (separatamente per parte sinistra e destra).
2. **Da env/mem a C**: data un'espressione in termini di `env` e `mem`, scrivere un possibile assegnamento C corrispondente.

Per la prossima lezione: esercitarsi con **vettori** (`a[i]`), **dereferenziazioni di espressioni**, e la relazione tra sintassi array e sintassi puntatori in C (entrambe applicabili sia a vettori sia a puntatori, ma tradotte diversamente dal compilatore).

---

> [!abstract] Punti chiave della lezione
> - I criteri di valutazione di un linguaggio (semplicita, astrazione, espressivita, ortogonalita, portabilita) possono essere in tensione tra loro: la concisione non implica leggibilita.
> - Lo zucchero sintattico non aggiunge potere espressivo: e trattabile con un preprocessore.
> - Il paradigma determina radicalmente il modo di pensare al problema; all'interno dello stesso paradigma, le soluzioni sono strutturalmente isomorfe tra linguaggi diversi.
> - In Prolog, non c'e distinzione tra input e output (invertibilita): lo stesso codice si usa come test, generatore, o risolutore.
> - Nel modello imperativo, il valore di una variabile si ottiene componendo due funzioni: `env` (nome -> locazione) e `mem` (locazione -> valore).
> - `env` e immutabile dentro un contesto; `mem` e mutabile (modificata dagli assegnamenti).
> - Nei puntatori C: a sinistra dell'assegnamento c'e sempre un `mem` in meno rispetto a destra. `env(mem(...))` non e mai corretto.

## Prossimi argomenti

- [ ] Traduzione env/mem per vettori e dereferenziazioni di espressioni
- [ ] Relazione tra sintassi array e sintassi puntatori in C
- [ ] Approfondimento su scope statico e dinamico
- [ ] Blocchi, dichiarazioni e regole di visibilita

---

#LP #semplicità #ortogonalità #tipi #astrazione #nomi #ambiente #scope #binding #blocchi #paradigmi #Prolog #invertibilità #puntatori
