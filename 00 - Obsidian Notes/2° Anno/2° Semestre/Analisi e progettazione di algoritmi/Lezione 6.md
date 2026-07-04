---
date: 2026-03-24
corso: Algoritmi e Principi dell'Informatica
docente: N/D
lezione: Analisi HeapSort e introduzione QuickSort
tags: [APA, heap, heapsort, quicksort, analisi-asintotica]
---

# APA — Lezione 6: Analisi di HeapSort e Introduzione a QuickSort

**Corso:** Algoritmi e Principi dell'Informatica

---

## Argomenti trattati

- Analisi precisa del costo di `BuildHeap` (costruzione dello heap)
- Analisi precisa del costo di `HeapSort`
- Confronto tra le stime superiori e la complessità reale
- Introduzione a QuickSort: filosofia divide-et-impera
- Algoritmo `Partition` e suoi due requisiti fondamentali
- Stima del costo di `Partition`
- Impostazione dell'equazione di ricorrenza di QuickSort

---

## 1. Riepilogo: HeapSort e le sue componenti

HeapSort si basa su due procedure principali:

- **`Heapify(A, i)`** (`IPFI` nella notazione del prof): ripristina la proprietà di heap nel sottoalbero radicato in `i`, assumendo che i sottoalberi destro e sinistro siano già degli heap validi. Percorre un unico ramo verso il basso. Costo: $O(h)$, dove $h$ è l'altezza del nodo, con $h \leq \log_2 n$.
- **`BuildHeap(A)`**: costruisce un heap applicando `Heapify` a tutti i nodi interni, partendo dall'ultimo nodo interno fino alla radice.
- **`HeapSort(A)`**: chiama `BuildHeap`, poi esegue $n-1$ estrazioni del massimo (ciascuna seguita da `Heapify` sulla radice).

Le stime superiori che avevamo dato erano: $O(n \log n)$ sia per `BuildHeap` che per `HeapSort`, poiché entrambi chiamano `Heapify` un numero lineare di volte su alberi di altezza al più $\log n$. L'obiettivo di questa lezione è capire se queste stime sono **strette** (cioè $\Theta$) oppure approssimazioni per eccesso.

---

## 2. Analisi precisa di `BuildHeap`: costo $\Theta(n)$

### L'intuizione

`BuildHeap` applica `Heapify` a tutti i nodi interni, ma la **gran parte delle chiamate** avviene su nodi che sono radici di sottoalberi di altezza molto bassa. I nodi profondi (vicini alle foglie) sono molti, ma i loro sottoalberi sono piccoli. I nodi vicini alla radice (con sottoalberi alti) sono pochi.

> [!tip] Parole del Professore
> > [!quote]
> > "La stragrande maggioranza delle chiamate Heapify vengono fatte su heap in cui H è molto basso."

### La struttura dell'analisi

In un albero completo con $n$ nodi:

- Circa $n/2$ sono **foglie** (altezza 0 → nessuna chiamata `Heapify`)
- Circa $n/4$ sono **padri delle foglie** (altezza 1)
- Circa $n/8$ sono **padri dei padri delle foglie** (altezza 2)
- In generale, ci sono circa $n/2^{i+1}$ nodi di altezza $i$

Quindi il costo totale di `BuildHeap` nel caso peggiore è:

$$T_{\text{BuildHeap}} = \sum_{i=1}^{\lfloor \log_2 n \rfloor} \frac{n}{2^{i+1}} \cdot i = \frac{n}{2} \sum_{i=1}^{\lfloor \log_2 n \rfloor} \frac{i}{2^i}$$

### Calcolo della sommatoria $\sum_{i=0}^{\infty} \frac{i}{2^i}$

Partiamo dalla serie geometrica:

$$\sum_{i=0}^{\infty} x^i = \frac{1}{1-x}, \quad \text{per } 0 < x < 1$$

Notiamo che $\frac{i}{2^i} = i \cdot x^i$ con $x = \frac{1}{2}$. Ora, osserviamo che:

$$\frac{d}{dx} x^i = i \cdot x^{i-1}$$

Moltiplicando per $x$:

$$x \cdot \frac{d}{dx} x^i = i \cdot x^i$$

Quindi, per linearità dell'operatore di derivazione:

$$\sum_{i=0}^{\infty} i \cdot x^i = x \cdot \frac{d}{dx} \sum_{i=0}^{\infty} x^i = x \cdot \frac{d}{dx} \frac{1}{1-x} = x \cdot \frac{1}{(1-x)^2}$$

Per $x = \frac{1}{2}$:

$$\sum_{i=0}^{\infty} \frac{i}{2^i} = \frac{1/2}{(1/2)^2} = \frac{1/2}{1/4} = 2$$

### Risultato

$$T_{\text{BuildHeap}} \leq \frac{n}{2} \cdot 2 = n$$

Il costo è limitato superiormente da $n$, ed è anche $\Omega(n)$ (perché almeno $n/4$ chiamate richiedono almeno un confronto ciascuna). Quindi:

> [!abstract] Definizione: Complessità di `BuildHeap`
> $$T_{\text{BuildHeap}}(n) = \Theta(n)$$
> `BuildHeap` ha costo **lineare**, non $O(n \log n)$ come la stima grossolana suggeriva.

> [!tip] Coerenza con la ricerca del massimo
> Questo è coerente con il fatto che la ricerca del massimo in un array non ordinato richiede $\Theta(n)$: `BuildHeap` di fatto individua il massimo, e non si può fare meno di $n$ operazioni per costruire uno heap da zero.

---

## 3. Analisi precisa di `HeapSort`: costo $\Theta(n \log n)$

### La differenza con `BuildHeap`

In `HeapSort`, dopo aver costruito lo heap, si eseguono $n-1$ chiamate a `Heapify` sulla **radice** dell'heap residuo. La differenza cruciale è che qui le altezze dell'heap **decrescono lentamente**: ogni chiamata rimuove solo una foglia, quindi l'altezza dello heap si riduce di 1 solo dopo aver eliminato circa $n/2$ elementi.

Quindi:
- Le prime $\approx n/2$ chiamate a `Heapify` costano $h = \log_2 n$ nel caso peggiore
- Le successive $\approx n/4$ costano $h - 1$
- E così via

Il costo è:

$$T_{\text{HeapSort}} = \sum_{i=0}^{\lfloor \log_2 n \rfloor} \frac{n}{2^{i+1}} \cdot (h - i)$$

dove $h = \lfloor \log_2 n \rfloor$. Svolgendo:

$$= \frac{n}{2} \left[ h \sum_{i=0}^{h} \frac{1}{2^i} - \sum_{i=0}^{h} \frac{i}{2^i} \right]$$

Il primo termine converge a $h \cdot 2 = 2\log_2 n$, e il secondo a $2$ (come calcolato sopra). Quindi:

$$T_{\text{HeapSort}} = \Theta(n \log n)$$

> [!warning] La stima non era migliorabile per HeapSort
> Per `HeapSort`, al contrario di `BuildHeap`, la stima $O(n \log n)$ è **stretta**: almeno metà delle chiamate a `Heapify` costano $\log n$. Non si può fare di meglio (anticipazione: nessun algoritmo comparison-based può ordinare in meno di $\Theta(n \log n)$ confronti — lo dimostreremo più avanti).

---

## 4. Applicazioni delle code a priorità (anticipazione)

> *(questo verrà approfondito nelle prossime lezioni)*

La struttura dati heap è la base della **coda a priorità**: una struttura che mantiene un insieme di elementi con priorità, su cui le operazioni di inserimento e rimozione del massimo costano $O(\log n)$.

> [!example] Applicazione: algoritmo di Dijkstra
> La coda a priorità verrà usata per ottimizzare l'algoritmo di Dijkstra (percorso minimo in grafi pesati), già studiato nella prima parte del corso. La versione con heap riduce il costo delle operazioni di aggiornamento delle priorità.

---

## 5. QuickSort: introduzione

### Filosofia

QuickSort segue il paradigma **divide-et-impera**, come MergeSort: divide la sequenza in due parti, le ordina ricorsivamente, poi le ricombina.

La differenza radicale rispetto a MergeSort sta in **quale fase è costosa**:

| | MergeSort | QuickSort |
|---|---|---|
| **Divide** | Banale: divide a metà con aritmetica | Costosa: riorganizza l'array |
| **Fusione (merge)** | Lineare: richiede confronti | Nulla: la fusione è vacua |

### L'idea chiave

QuickSort cerca di fare in modo che la fusione finale sia **inutile**: se ogni elemento nella partizione sinistra è $\leq$ di ogni elemento nella partizione destra, allora concatenare le due sequenze ordinate localmente produce già una sequenza globalmente ordinata.

> [!abstract] Definizione: Requisito di Partition
> L'algoritmo di suddivisione `Partition(A, p, r)` deve garantire due proprietà al termine della sua esecuzione, restituendo un indice $q$:
>
> **R1 (Correttezza):** Per ogni $i \in [p, q]$ e per ogni $j \in [q+1, r]$, $A[i] \leq A[j]$.
>
> **R2 (Terminazione):** $p \leq q < r$, cioè entrambe le partizioni sono non vuote.

R1 garantisce che la fusione sia vacua (correttezza). R2 garantisce che le chiamate ricorsive operino su sottosequenze strettamente più piccole (terminazione).

> [!warning] Perché R2 è indispensabile
> Se `Partition` potesse restituire $q = r$ (partizione destra vuota), la chiamata ricorsiva `QuickSort(A, q+1, r)` diventerebbe `QuickSort(A, r+1, r)`, che si riduce a se stessa se la sequenza originale aveva $p < r$ — loop infinito.

### Struttura dell'algoritmo

```python
def QuickSort(A, p, r):
    if p < r:                        # caso base: sequenza con < 2 elementi
        q = Partition(A, p, r)       # divide, garantendo R1 e R2
        QuickSort(A, p, q)           # ordina la partizione sinistra
        QuickSort(A, q+1, r)         # ordina la partizione destra
        # nessuna fusione necessaria!
```

La **correttezza** si dimostra per induzione: il caso base ($p \geq r$) è banale. Per $p < r$, `Partition` garantisce R1 e R2; per ipotesi induttiva le due chiamate ricorsive ordinano correttamente le sottosequenze (che sono strettamente più piccole per R2); R1 garantisce che la concatenazione è ordinata.

---

## 6. Algoritmo Partition

### Pivot e invariante

L'algoritmo sceglie un **pivot** $x = A[p]$ (il primo elemento della sequenza) e riorganizza gli elementi in modo che:

- Tutti gli elementi $\leq x$ vadano nella partizione sinistra
- Tutti gli elementi $\geq x$ vadano nella partizione destra
- Gli elementi $= x$ possono stare in entrambe le parti

> [!warning] Perché si usa $\leq$ e non $<$
> Se la sequenza contiene elementi duplicati (ad esempio tutti uguali), non è possibile costruire due partizioni non vuote tali che nessun elemento sia uguale in entrambe. Ammettere gli uguali su entrambi i lati è necessario. Di conseguenza R1 usa $\leq$, non $<$.

### Pseudocodice

```text
Partition(A, p, r):
    x = A[p]           // pivot: primo elemento
    i = p - 1          // indice che avanza da sinistra
    j = r + 1          // indice che arretra da destra

    repeat:
        repeat: j = j - 1  until A[j] <= x   // j si ferma su un elemento ≤ x
        repeat: i = i + 1  until A[i] >= x   // i si ferma su un elemento ≥ x
        if i < j:
            swap(A, i, j)
    until i >= j

    return j
```

> [!warning] Fermarsi sugli uguali è fondamentale
> Entrambi i `repeat` interni si fermano sugli elementi **uguali** al pivot. Se non ci si fermasse sugli uguali, in una sequenza di elementi tutti uguali, $i$ e $j$ attraverserebbero l'intera sequenza senza mai incontrarsi, portando a comportamenti scorretti o loop infiniti.

### Perché si restituisce $j$ e non $i$

Quando l'algoritmo termina, $j$ si è fermato su un elemento $\leq x$, e tutto ciò che precede $j$ (incluso) è $\leq x$. Invece $i$ si è fermato su un elemento $\geq x$, che non può stare nella partizione sinistra se è strettamente maggiore. Restituire $j$ garantisce la partizione corretta.

> [!example] Esempio di esecuzione di Partition
> Sequenza: `[3, 2, 7, 1, 5, 3, 8]`, pivot $x = 3$.
>
> - Stato iniziale: `i = -1` (prima di $p$), `j = 7` (oltre $r$)
> - $j$ decrementa: si ferma su `A[5] = 3` ($\leq 3$); $i$ incrementa: si ferma su `A[0] = 3$ ($\geq 3$). Poiché `i = 0 < j = 5`, swap (no-op: stesso valore). Ripeti.
> - $j$ decrementa: si ferma su `A[3] = 1`; $i$ incrementa: si ferma su `A[2] = 7`. Poiché `i = 2 < j = 3`, swap → `[3, 2, 1, 7, 5, 3, 8]`
> - $j$ decrementa: si ferma su `A[2] = 1`; $i$ incrementa: si ferma su `A[3] = 7`. Ora `i = 3 > j = 2` → termina. Restituisce `q = j = 2`.
>
> Risultato: `A[0..2] = [3, 2, 1]` (tutti $\leq 3$), `A[3..6] = [7, 5, 3, 8]` (tutti $\geq 3$). R1 verificato.

### Costo di Partition

Gli indici $i$ e $j$ si muovono ciascuno in un'unica direzione (rispettivamente verso destra e verso sinistra), senza mai tornare indietro. La somma totale degli incrementi di $i$ e dei decrementi di $j$ è al massimo $n + 1$ (si possono superare di al più 1).

Ogni incremento/decremento ha costo costante. Quindi:

> [!abstract] Definizione: Costo di Partition
> $$T_{\text{Partition}}(n) = \Theta(n)$$

---

## 7. Equazione di ricorrenza di QuickSort

A differenza di MergeSort, in QuickSort la dimensione delle due sottosequenze **dipende dall'input** (non è garantita la divisione a metà). Se `Partition` restituisce $q$ tale che la partizione sinistra abbia $k$ elementi ($k \in [1, n-1]$), l'equazione di ricorrenza è:

$$T(n) = \begin{cases} \Theta(1) & \text{se } n \leq 1 \\ \Theta(n) + T(k) + T(n-k) & \text{altrimenti} \end{cases}$$

dove $k$ dipende dall'input. L'analisi richiede quindi di distinguere **caso peggiore**, **caso migliore** e **caso medio**, analogamente a quanto fatto per InsertionSort.

> [!info] Implicazione
> Il comportamento di QuickSort non dipende solo dalla dimensione dell'input, ma dai suoi **valori**. Se il pivot è sempre il minimo o il massimo, la partizione sarà sempre sbilanciata (1 elemento da un lato, $n-1$ dall'altro), degradando a $\Theta(n^2)$. La prossima lezione tratterà la soluzione di questa equazione di ricorrenza.

---

> [!abstract] Punti chiave della lezione
> - `BuildHeap` ha costo $\Theta(n)$, non $\Theta(n \log n)$: la maggior parte delle chiamate `Heapify` avviene su sottoalberi molto bassi.
> - `HeapSort` ha costo $\Theta(n \log n)$: la stima era stretta perché le prime $n/2$ chiamate costano ciascuna $\log n$.
> - QuickSort evita la fusione garantendo che ogni elemento della partizione sinistra sia $\leq$ di ogni elemento della destra.
> - `Partition` deve soddisfare R1 (correttezza della fusione) e R2 (terminazione della ricorsione).
> - `Partition` ha costo $\Theta(n)$ lineare sulla dimensione della sequenza.

## Prossimi argomenti

- [ ] Dimostrazione formale che `Partition` soddisfa R1 e R2
- [ ] Analisi del caso peggiore, migliore e medio di QuickSort
- [ ] Dimostrazione che nessun algoritmo comparison-based può ordinare in meno di $\Theta(n \log n)$ confronti

#APA #heap #heapsort #quicksort #analisi-asintotica #divide-et-impera
