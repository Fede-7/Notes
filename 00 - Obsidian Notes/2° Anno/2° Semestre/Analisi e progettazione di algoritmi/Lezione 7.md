---
date: 2026-03-26
corso: Algoritmi e Principi dell'Informatica
docente: N/D
lezione: QuickSort — correttezza di Partition e analisi del tempo di esecuzione
tags: [APA, quicksort, partition, analisi-asintotica, ricorrenza]
---

# APA — Lezione 7: QuickSort — Correttezza di Partition e Analisi

**Corso:** Algoritmi e Principi dell'Informatica

---

## Argomenti trattati

- Dimostrazione che `Partition` soddisfa R1 (correttezza) e R2 (terminazione)
- Proprietà di terminazione dell'algoritmo: somma di incrementi e decrementi
- Perché si restituisce `j` e non `i`
- Impostazione dell'equazione di ricorrenza di QuickSort parametrica sull'input
- Anticipazione: analisi caso peggiore, migliore e medio

---

## 1. Riepilogo: `Partition` e i suoi requisiti

Dalla lezione precedente, `Partition(A, p, r)` con pivot $x = A[p]$ deve garantire:

- **R1**: per ogni $i \in [p, q]$ e ogni $j \in [q+1, r]$: $A[i] \leq A[j]$
- **R2**: $p \leq q < r$ (entrambe le partizioni non vuote)

L'algoritmo usa due indici $i$ (da sinistra) e $j$ (da destra) che convergono:

```text
Partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    repeat:
        repeat: j = j - 1  until A[j] <= x
        repeat: i = i + 1  until A[i] >= x
        if i < j: swap(A, i, j)
    until i >= j
    return j
```

---

## 2. Terminazione: la somma degli incrementi è lineare

### Quante volte si eseguono i `repeat` interni?

Non è scritto da nessuna parte che $i$ si fermi quando supera $j$, né viceversa. Potremmo quindi chiederci: i due indici possono "sorpassarsi" di molto?

**Proprietà chiave**: all'inizio di ogni iterazione del `repeat` esterno, tutto ciò che è a sinistra di $i$ è $\geq x$, e tutto ciò che è a destra di $j$ è $\leq x$. In particolare:

- Quando $j$ decrementa nella prossima iterazione, troverà sicuramente l'elemento in posizione $i$ (che è $\leq x$, oppure qualcosa ancora più piccolo prima di $i$). Quindi $j$ non può oltrepassare $i$ di più di 1.
- Simmetricamente, $i$ si ferma sulla posizione appena successiva a $j$ se $j$ si è già fermato su $i$.

**Conclusione**: la somma totale degli incrementi di $i$ e dei decrementi di $j$ è al più $n + 1$. Quindi il `repeat` esterno esegue al più $n/2$ iterazioni, e il numero totale di operazioni è $O(n)$.

> [!abstract] Proprietà: costo di Partition
> $$T_{\text{Partition}}(n) = \Theta(n)$$

---

## 3. Correttezza: perché si restituisce $j$ e non $i$

Quando l'algoritmo termina ($i \geq j$), gli invarianti garantiscono:

- Tutto ciò che è a sinistra di $i$ (incluso $i$) ha valore $\geq x$.

  Ma $i$ si ferma su un elemento $\geq x$: se quell'elemento è **strettamente maggiore** di $x$, non può stare nella partizione sinistra (che deve contenere solo elementi $\leq x$).

- Tutto ciò che è a destra di $j$ (incluso $j$) ha valore $\leq x$.

  $j$ si ferma su un elemento $\leq x$: questo elemento **può** stare nella partizione sinistra.

Pertanto restituire $q = j$ garantisce che $A[p..q]$ contiene solo elementi $\leq x$ (R1, lato sinistro) e $A[q+1..r]$ contiene solo elementi $\geq x$ (R1, lato destro).

### Verifica di R2

Dobbiamo mostrare che $p \leq j < r$. Questo segue dall'osservazione precedente sulla terminazione: $i$ e $j$ non si possono separare di più di 1, e dato che partono rispettivamente da $p-1$ e $r+1$, almeno un'iterazione deve avvenire. In particolare, $j$ non può mai raggiungere $p-1$ (c'è sempre almeno un elemento $\leq x$ nell'array, cioè $x$ stesso), né $i$ può rimanere a $p$ se $j$ arriva fino lì (perché $i$ si incrementa comunque almeno una volta).

> [!warning] Aspetto critico: fermarsi sugli uguali
> Se i `repeat` interni non si fermassero sugli uguali al pivot, su un array di tutti elementi uguali $i$ e $j$ si attraverserebbero completamente senza mai fermarsi, o si fermerebbero ai bordi, violando R2. Il fatto di fermarsi sugli uguali garantisce che le due partizioni siano sempre non vuote.

---

## 4. Equazione di ricorrenza di QuickSort

### Il problema: dipendenza dall'input

A differenza di MergeSort (che divide sempre a metà), QuickSort produce due partizioni la cui dimensione dipende dall'input. Se $k$ è la dimensione della partizione sinistra ($k \in \{1, \ldots, n-1\}$), l'equazione di ricorrenza è:

$$T(n) = \begin{cases} \Theta(1) & \text{se } n \leq 1 \\ \Theta(n) + T(k) + T(n-k) & \text{se } n > 1 \end{cases}$$

Il valore di $k$ dipende dall'input fornito a ogni singola chiamata ricorsiva — è diverso a ogni livello dell'albero delle chiamate. Quindi questa equazione è parametrica non solo su $n$, ma su un insieme di parametri $k_1, k_2, \ldots$ (uno per ogni nodo dell'albero di ricorsione).

### Tre regimi di analisi

Come per InsertionSort, occorre distinguere tra:

**Caso peggiore**: il pivot è sempre il minimo o il massimo dell'array, producendo partizioni di dimensioni 1 e $n-1$:

$$T_{\text{worst}}(n) = \Theta(n) + T(1) + T(n-1) = \Theta(n) + T(n-1)$$

Questa è la stessa ricorrenza di InsertionSort nel caso peggiore, che si risolve in $T(n) = \Theta(n^2)$.

> [!example] Quando si verifica il caso peggiore
> Se il pivot è sempre $A[p]$ (primo elemento) e l'array è già ordinato (crescente o decrescente), il pivot sarà sempre il minimo o il massimo — le partizioni avranno sempre 1 e $n-1$ elementi. Questo degrada QuickSort a $O(n^2)$.

**Caso migliore**: il pivot è sempre la mediana, producendo due partizioni di dimensione $n/2$:

$$T_{\text{best}}(n) = \Theta(n) + 2T(n/2)$$

Per il Teorema Master (caso 2): $T(n) = \Theta(n \log n)$.

**Caso medio**: in media su tutti i possibili input, il tempo atteso è $\Theta(n \log n)$. Questo verrà dimostrato nelle lezioni successive.

> [!tip] Parole del Professore
> > [!tip]
> > "Dovremo fare analisi di caso migliore, caso peggiore e eventualmente caso medio, analogamente a quanto fatto con InsertionSort."

---

> [!abstract] Punti chiave della lezione
> - `Partition` termina in $\Theta(n)$: la somma degli incrementi di $i$ e dei decrementi di $j$ è al più $n+1$.
> - Si restituisce $j$ perché si ferma su un elemento $\leq x$ (corretto per la partizione sinistra); $i$ si ferma su un elemento $\geq x$ che potrebbe essere troppo grande.
> - Fermarsi sugli uguali è fondamentale per garantire R2 su array con elementi duplicati.
> - L'equazione di ricorrenza di QuickSort è parametrica sull'input: il caso peggiore è $\Theta(n^2)$, il migliore e la media sono $\Theta(n \log n)$.

## Prossimi argomenti

- [ ] Soluzione formale dell'equazione di ricorrenza nel caso peggiore e medio di QuickSort
- [ ] Varianti di QuickSort per evitare il caso peggiore (pivot casuale, mediana di tre)
- [ ] Lower bound $\Omega(n \log n)$ per algoritmi comparison-based

#APA #quicksort #partition #analisi-asintotica #ricorrenza #caso-peggiore
