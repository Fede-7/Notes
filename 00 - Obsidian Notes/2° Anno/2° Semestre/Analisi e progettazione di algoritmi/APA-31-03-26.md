---
date: 2026-03-31
corso: Algoritmi e Principi dell'Informatica
docente: N/D
lezione: QuickSort — caso peggiore, analisi del caso medio, lower bound comparison-based
tags: [APA, quicksort, analisi-caso-medio, lower-bound, albero-decisione, induzione]
---

# APA — Lezione: QuickSort — Caso Peggiore, Caso Medio e Lower Bound

**Corso:** Algoritmi e Principi dell'Informatica

---

## Argomenti trattati

- Caso peggiore di QuickSort: $\Theta(n^2)$ con analisi dell'albero di ricorrenza
- Analisi intuitiva: sbilanciamento proporzionale porta sempre a $\Theta(n \log n)$
- Alternanza di partizionamenti buoni e cattivi: ancora $\Theta(n \log n)$
- Definizione formale del caso medio: rango del pivot, assunzione di randomizzazione
- Equazione di ricorrenza del tempo medio
- Dimostrazione per induzione che $T_M(n) = O(n \log n)$ con la tecnica della sommatoria per approssimazione
- Anticipazione: lower bound $\Omega(n \log n)$ per algoritmi comparison-based e alberi di decisione

---

## 1. Caso peggiore di QuickSort: $\Theta(n^2)$

Il caso peggiore si verifica quando `Partition` produce sempre partizioni di dimensioni $1$ e $n-1$ (pivot è sempre il minimo o il massimo). L'albero di ricorrenza è una "spina di pesce": ogni nodo interno ha un figlio foglia (dimensione 1) e un figlio interno (dimensione $n-i$).

Il contributo del livello $i$ è $n - i$ (la dimensione dell'unico nodo interno a quel livello). Sommando:

$$T_{\text{worst}}(n) = n + \sum_{i=1}^{h} (n - i) = n + (n-1) + (n-2) + \cdots + 1 = \Theta(n^2)$$

> [!abstract] Complessità caso peggiore
> $$T_{\text{QuickSort, worst}}(n) = \Theta(n^2)$$
> QuickSort nel caso peggiore è asintoticamente equivalente a InsertionSort o SelectionSort.

> [!example] Quando si verifica il caso peggiore
> Se il pivot è sempre `A[p]` (primo elemento) e l'array è già ordinato (crescente o decrescente), il pivot è sempre il minimo o il massimo: le partizioni saranno sempre $1$ e $n-1$. Per questo il pivot casuale è preferibile in pratica.

---

## 2. Sbilanciamento proporzionale: ancora $\Theta(n \log n)$

### Caso con partizioni $n/10$ e $9n/10$

Ipotizziamo che ogni chiamata a `Partition` produca sempre partizioni di dimensioni $n/10$ e $9n/10$. L'albero di ricorrenza è irregolare: il ramo destro (più lungo) ha altezza $\log_{10/9} n$, quello sinistro $\log_{10} n$.

Fintanto che il livello è "pieno" (tutti i nodi presenti), la somma degli input di quel livello è sempre $n$ (gli input si distribuiscono ma la loro somma si conserva). Il costo per livello è quindi $\Theta(n)$.

Le altezze dei due estremi:

$$h_{\min} = \log_{10} n, \quad h_{\max} = \log_{10/9} n$$

Entrambe sono $\Theta(\log n)$ (con basi diverse, ma il cambio di base introduce solo una costante moltiplicativa). Quindi:

$$T(n) = \Theta(n \cdot h_{\max}) = \Theta(n \log n)$$

### Generalizzazione: qualsiasi $\alpha \in (0,1)$

Per qualsiasi costante $\alpha$ con $0 < \alpha < 1$, se le partizioni sono sempre $\alpha n$ e $(1-\alpha)n$, si ottiene $T(n) = \Theta(n \log n)$.

> [!important] Il sbilanciamento proporzionale non peggiora l'andamento asintotico
> Finché le due partizioni hanno dimensioni che sono entrambe frazioni costanti di $n$, l'algoritmo rimane $\Theta(n \log n)$. Solo quando una partizione è di dimensione costante (es. 1) si degrada a $\Theta(n^2)$.

### Alternanza di partizioni perfette e pessime

Se QuickSort alterna livelli perfettamente bilanciati ($n/2, n/2$) e livelli completamente sbilanciati ($1, n-1$), ogni due livelli la dimensione si dimezza. L'altezza diventa $2 \log_2 n$ invece di $\log_2 n$: il fattore 2 è una costante, quindi:

$$T(n) = \Theta(n \cdot 2 \log_2 n) = \Theta(n \log n)$$

> [!quote]
> "Non è facile rovinare l'andamento del caso migliore in vari modi in cui ho provato ad avvicinarmi. Quindi sembra che questo algoritmo tendenzialmente si comporti sempre così."

---

## 3. Analisi formale del caso medio

### Assunzioni

1. Tutti gli elementi della sequenza sono **distinti** (no duplicati). Più duplicati ci sono, più il comportamento si avvicina al caso migliore.
2. Prima di chiamare `Partition`, si sceglie il pivot **casualmente** (swap con `A[p]`): ogni elemento ha la stessa probabilità $1/n$ di essere il pivot.

### Rango del pivot

> [!abstract] Definizione: Rango
> Il **rango** di un elemento $x$ rispetto a una sequenza $A[p..r]$ è il numero di elementi di $A[p..r]$ che sono $\leq x$.

Sotto le assunzioni (tutti distinti, pivot casuale), il rango $r$ del pivot è uniformemente distribuito in $\{1, 2, \ldots, n\}$, e determina univocamente le dimensioni delle due partizioni:
- Partizione sinistra: $r - 1$ elementi (rango 1 → 0 elementi a sinistra; rango $r$ → $r-1$ elementi a sinistra, ma il pivot va a destra salvo che sia il minimo assoluto)

In realtà, per la struttura di `Partition`: rango 1 → $q = p$ (tutto a destra), rango 2 → 1 elemento a sinistra, ..., rango $n$ → $n-1$ elementi a sinistra.

### Equazione di ricorrenza del tempo medio

Chiamiamo $T_M(n)$ il tempo medio di QuickSort su input di dimensione $n$. Mediando su tutti i possibili ranghi del pivot (con probabilità uniforme $1/n$ ciascuno):

$$T_M(n) = \frac{1}{n} \sum_{r=1}^{n} \left[ T_M(q_r) + T_M(n - q_r) + \Theta(n) \right]$$

dove $q_r$ è la dimensione della partizione sinistra quando il rango è $r$. Riorganizzando (i valori $q_r$ quando $r$ va da 2 a $n$ percorrono tutti i valori da 1 a $n-1$):

$$\boxed{T_M(n) = \frac{2}{n} \sum_{q=1}^{n-1} T_M(q) + \Theta(n)}$$

---

## 4. Dimostrazione che $T_M(n) = O(n \log n)$

### Teorema

Esiste una costante $c > 0$ tale che per ogni $n \geq 2$: $T_M(n) \leq c \cdot n \log_2 n$.

### Dimostrazione per induzione

**Caso base** ($n = 2$): $T_M(2) = \frac{2}{2} T_M(1) + \Theta(2) = \Theta(1) + \Theta(2) = c_1 + k$ per costanti $c_1, k$. Si deve trovare $c$ tale che $c_1 + k \leq c \cdot 2 \log_2 2 = 2c$. Basta scegliere $c \geq (c_1 + k)/2$.

**Caso induttivo** ($n > 2$): per ipotesi induttiva, $T_M(q) \leq c \cdot q \log_2 q$ per ogni $q < n$. Sostituendo:

$$T_M(n) \leq \frac{2}{n} \sum_{q=1}^{n-1} c \cdot q \log_2 q + kn = \frac{2c}{n} \sum_{q=1}^{n-1} q \log_2 q + kn$$

dove $k$ è la costante di Partition. Dobbiamo mostrare che questo è $\leq c \cdot n \log_2 n$, cioè:

$$\frac{2c}{n} \sum_{q=1}^{n-1} q \log_2 q + kn \leq c \cdot n \log_2 n$$

Equivalentemente, è sufficiente trovare un maggiorante per $\sum_{q=1}^{n-1} q \log_2 q$.

### Maggiorazione della sommatoria $\sum_{q=1}^{n-1} q \log_2 q$

**Prima approssimazione (troppo grossolana)**:

$$\sum_{q=1}^{n-1} q \log_2 q \leq \log_2 n \sum_{q=1}^{n-1} q = \log_2 n \cdot \frac{n(n-1)}{2} \approx \frac{n^2 \log n}{2}$$

Sostituendo: $T_M(n) \lesssim cn\log n - \frac{cn\log n}{?}$... questo maggiorante è troppo grande (porta a $\frac{2c}{n} \cdot \frac{n^2 \log n}{2} = cn \log n$, senza margine per $kn$).

**Seconda approssimazione (raffinata — dividiamo la somma in due parti)**:

$$\sum_{q=1}^{n-1} q \log_2 q = \sum_{q=1}^{\lfloor n/2 \rfloor - 1} q \log_2 q + \sum_{q=\lfloor n/2 \rfloor}^{n-1} q \log_2 q$$

Per la prima parte, ogni $\log_2 q \leq \log_2(n/2) = \log_2 n - 1$. Per la seconda, ogni $\log_2 q \leq \log_2 n$. Quindi:

$$\leq (\log_2 n - 1) \sum_{q=1}^{\lfloor n/2 \rfloor - 1} q + \log_2 n \sum_{q=\lfloor n/2 \rfloor}^{n-1} q$$

$$= \log_2 n \sum_{q=1}^{n-1} q - \sum_{q=1}^{\lfloor n/2 \rfloor - 1} q \leq \frac{n^2 \log_2 n}{2} - \frac{(n/2)(n/2 - 1)}{2} \leq \frac{n^2 \log_2 n}{2} - \frac{n^2}{8}$$

> [!warning] Sottrarre richiede attenzione al verso della disuguaglianza
> Per trovare un **maggiorante** di $A - B$, si deve trovare un **minorante** di $B$ (sottrarre di meno porta a un valore più grande). Quindi si usa $\sum_{q=1}^{\lfloor n/2 \rfloor - 1} q \geq \sum_{q=1}^{n/2 - 1} q$, non il contrario.

### Completamento della dimostrazione

Sostituendo il maggiorante nella disuguaglianza:

$$T_M(n) \leq \frac{2c}{n} \left(\frac{n^2 \log_2 n}{2} - \frac{n^2}{8}\right) + kn = cn \log_2 n - \frac{cn}{4} + kn$$

Dobbiamo avere $cn \log_2 n - \frac{cn}{4} + kn \leq cn \log_2 n$, cioè:

$$-\frac{cn}{4} + kn \leq 0 \implies c \geq 4k$$

Quindi la condizione $c \geq 4k$ (dove $k$ è la costante di Partition) è sufficiente. Unendo con il vincolo del caso base ($c \geq (c_1 + k)/2$), basta scegliere:

$$c = \max\left\{\frac{c_1 + k}{2},\ 4k\right\}$$

Questa costante esiste, è positiva, e vale per tutti gli $n \geq 2$.

> [!abstract] Risultato: complessità del caso medio
> $$T_M(n) = \Theta(n \log n)$$
> Il caso medio di QuickSort è $\Theta(n \log n)$, identico al caso migliore. Questo spiega perché QuickSort è considerato uno dei migliori algoritmi di ordinamento nella pratica: nonostante il caso peggiore sia $\Theta(n^2)$, il comportamento medio è ottimale.

Confronto con InserionSort: per InsertionSort il caso medio e il caso peggiore coincidono ($\Theta(n^2)$), quindi si comporta quasi sempre in modo pessimo. Per QuickSort, il caso peggiore è raro (e si può evitare con la scelta casuale del pivot).

---

## 5. Lower bound: nessun algoritmo comparison-based può fare meglio di $\Theta(n \log n)$

### Il problema

Vogliamo dimostrare che per qualsiasi algoritmo di ordinamento che usa solo confronti tra elementi, il tempo nel caso peggiore (e nel caso medio) è $\Omega(n \log n)$.

### Alberi di decisione (introduzione)

Un algoritmo di ordinamento per confronti può essere modellato come una sequenza di confronti binari: ogni confronto $A[i] \leq A[j]$ ha due esiti (vero/falso), e in base all'esito si sceglie il confronto successivo.

Fissato $n$ e fissato l'algoritmo $A$, esiste un unico **albero di decisione** che descrive tutti i possibili percorsi di esecuzione di $A$ su input di dimensione $n$. Ogni nodo interno rappresenta un confronto; ogni foglia rappresenta un ordinamento determinato.

> [!example] Connessione con il tempo di esecuzione
> Il numero di confronti effettuati su un input specifico è la lunghezza del percorso radice-foglia corrispondente. Il caso peggiore corrisponde alla foglia più profonda: l'altezza dell'albero di decisione. La dimostrazione del lower bound consiste nel dimostrare che l'altezza di qualsiasi albero di decisione per un algoritmo di ordinamento di $n$ elementi è $\Omega(n \log n)$.

*(La dimostrazione completa verrà svolta dopo Pasqua)*

---

> [!summary] Punti chiave della lezione
> - Il caso peggiore di QuickSort è $\Theta(n^2)$ (pivot sempre estremo), ma questo è raro con la scelta casuale del pivot.
> - Qualsiasi sbilanciamento proporzionale (es. 1/10 e 9/10) mantiene la complessità a $\Theta(n \log n)$.
> - Il caso medio è $\Theta(n \log n)$, dimostrato per induzione con la tecnica della sommatoria in due parti.
> - La tecnica di approssimazione delle sommatorie (dividere in due parti e approssimare ciascuna con limiti diversi) è utile per altre dimostrazioni.
> - Il lower bound $\Omega(n \log n)$ per gli algoritmi comparison-based sarà dimostrato tramite gli alberi di decisione.

## Prossimi argomenti (dopo Pasqua)

- [ ] Dimostrazione formale del lower bound $\Omega(n \log n)$ tramite alberi di decisione
- [ ] Algoritmi di ordinamento in tempo lineare (con vincoli sui valori)

#APA #quicksort #analisi-caso-medio #lower-bound #albero-decisione #induzione
