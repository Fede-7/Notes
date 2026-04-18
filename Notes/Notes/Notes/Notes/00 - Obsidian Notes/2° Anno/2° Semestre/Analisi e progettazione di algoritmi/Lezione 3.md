---
Date: 2026-03-12
Professore: Benerecetti
tags:
  - APA
---



# Lezione 3: Analisi di Insertion Sort e Introduzione a Merge Sort

---

## Argomenti trattati
- Ripresa dell'analisi del tempo di esecuzione di Insertion Sort
- Parametri $t_j$ per il numero di esecuzioni del ciclo while
- Derivazione di $T(n)$ per Insertion Sort con le sommatorie
- Caso migliore (array ordinato) $\Rightarrow$ tempo lineare
- Caso peggiore (array ordinato in ordine decrescente) $\Rightarrow$ tempo quadratico
- Analisi del caso medio tramite valore atteso e inversioni
- Introduzione al paradigma Divide et Impera
- Algoritmo Merge Sort: struttura ricorsiva, procedura di Merge
- Analisi del tempo di esecuzione di Merge Sort tramite albero di ricorrenza
- Equazione di ricorrenza $T(n) = 2T(n/2) + \Theta(n)$ e sua risoluzione

---

## Ripresa: tempo di esecuzione di Insertion Sort

Nella lezione precedente si era discusso come il comportamento di Insertion Sort dipenda dalla disposizione dei dati in input. Non contano i valori specifici, ma le **relazioni d'ordine** (posizioni relative) tra gli elementi, cioe le **permutazioni** possibili.

### Parametri $t_j$

> [!abstract] Definizione:
> Si definisce $t_j$ come il **numero di esecuzioni del ciclo while** (riga 4 dell'algoritmo) per ciascun valore di $j$, con $j$ che va da $2$ a $n$.

Il valore di $t_j$ dipende dalla relazione che l'elemento in posizione $j$ ha con tutti gli elementi che lo precedono. Un'osservazione fondamentale e che:

> [!warning] Indipendenza dei parametri $t_j$
> I parametri $t_j$ sono **tra loro indipendenti**: il valore di $t_3$ dipende solo da $A[3]$ e dalla sua relazione con gli elementi precedenti, e non ha alcuna relazione con il valore di $t_2$, $t_4$, ecc. Questo vale in assenza di un **bias** (pregiudizio) nella scelta degli input.

### Espressione di $T(n)$ con i parametri $t_j$

Le righe 1, 2, 3 e 7 dell'algoritmo sono tutte eseguite un numero di volte lineare in $n$. Aggregandole:

$$T(n) = c \cdot n + c_4 \sum_{j=2}^{n} t_j + (c_5 + c_6) \sum_{j=2}^{n} (t_j - 1)$$

dove:
- $c \cdot n$ racchiude il contributo delle righe a costo lineare (righe 1, 2, 3, 7)
- $c_4 \sum_{j=2}^{n} t_j$ e il contributo della riga 4 (condizione del while)
- $(c_5 + c_6)\sum_{j=2}^{n}(t_j - 1)$ e il contributo delle righe 5 e 6 (corpo del while), eseguite una volta in meno rispetto alla condizione

La prima parte ($c \cdot n$) e **indipendente dai dati**, mentre le sommatorie dipendono dai valori di $t_j$.

---

## Limiti sui parametri $t_j$

Dall'analisi sintattica dell'algoritmo si ricavano i limiti:

$$1 \leq t_j \leq j \qquad \forall\, j \in \{2, \ldots, n\}$$

- **Limite inferiore** ($t_j \geq 1$): il while viene eseguito almeno una volta (per verificare che la condizione e falsa ed uscire).
- **Limite superiore** ($t_j \leq j$): nel caso peggiore, partendo con $i = j - 1$ e decrementando fino a $i = 0$, si fanno esattamente $j$ iterazioni.

---

## Caso migliore: array gia ordinato

### Ipotesi

$$t_j = 1 \quad \forall\, j \in \{2, \ldots, n\}$$

> [!example] Testimone: array ordinato in ordine crescente
> Se la sequenza e gia ordinata, per ogni $j$ l'elemento $A[j]$ e maggiore o uguale di tutti i precedenti. La condizione del while e immediatamente falsa $\Rightarrow$ $t_j = 1$.

### Calcolo di $T_{\text{best}}(n)$

Sostituendo $t_j = 1$ nell'espressione di $T(n)$:

$$T_{\text{best}}(n) = c \cdot n + c_4 \sum_{j=2}^{n} 1 + (c_5 + c_6) \sum_{j=2}^{n} (1 - 1)$$

La seconda sommatoria si annulla ($t_j - 1 = 0$ per ogni $j$):

$$T_{\text{best}}(n) = c \cdot n + c_4 \cdot (n - 1) = (c + c_4) \cdot n - c_4$$

$$\boxed{T_{\text{best}}(n) = \Theta(n)}$$

> [!warning] Insertion Sort e ottimale su input ordinati
> Questo algoritmo e particolarmente efficiente quando l'input e gia ordinato (o quasi ordinato). Non tutti gli algoritmi di ordinamento hanno questa proprieta.

---

## Caso peggiore: array ordinato in ordine decrescente

### Ipotesi

$$t_j = j \quad \forall\, j \in \{2, \ldots, n\}$$

> [!example] Testimone: array ordinato in ordine decrescente
> Se la sequenza e ordinata in ordine decrescente, per ogni $j$ l'elemento $A[j]$ e minore di **tutti** i precedenti. Il while scorre tutti gli elementi precedenti fino a $i = 0$, quindi $t_j = j$.

### Calcolo di $T_{\text{worst}}(n)$

Sostituendo $t_j = j$:

$$T_{\text{worst}}(n) = c \cdot n + c_4 \sum_{j=2}^{n} j + (c_5 + c_6) \sum_{j=2}^{n} (j - 1)$$

**Prima sommatoria** --- $\sum_{j=2}^{n} j$:

$$\sum_{j=2}^{n} j = \sum_{j=1}^{n} j - 1 = \frac{n(n+1)}{2} - 1$$

**Seconda sommatoria** --- $\sum_{j=2}^{n} (j-1)$:

Quando $j$ varia da $2$ a $n$, il termine $(j-1)$ varia da $1$ a $n-1$:

$$\sum_{j=2}^{n} (j - 1) = \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2}$$

Entrambe le sommatorie sono funzioni quadratiche in $n$, quindi:

$$\boxed{T_{\text{worst}}(n) = \Theta(n^2)}$$

---

## Caso medio: analisi probabilistica

Il caso migliore e il caso peggiore sono casi **estremi** e non necessariamente indicativi del comportamento generale. Si pone quindi il problema di capire come si comporta Insertion Sort **in media**, su un input arbitrario.

### Valore atteso di $t_j$

Sfruttando l'**indipendenza** dei parametri $t_j$ e l'assunzione che tutti i valori $t_j \in \{1, 2, \ldots, j\}$ siano **equiprobabili** (nessun bias negli input):

> [!abstract] Definizione:
> Il **valore atteso** di $t_j$ in condizioni di equiprobabilita e:
> $$E[t_j] = \sum_{i=1}^{j} i \cdot P(t_j = i) = \sum_{i=1}^{j} i \cdot \frac{1}{j} = \frac{1}{j} \sum_{i=1}^{j} i = \frac{1}{j} \cdot \frac{j(j+1)}{2} = \frac{j+1}{2}$$

In condizioni di equiprobabilita, il valore atteso coincide con la **media aritmetica**.

### Calcolo di $T_{\text{avg}}(n)$

Sostituendo $t_j = \frac{j+1}{2}$ e $t_j - 1 = \frac{j-1}{2}$:

$$T_{\text{avg}}(n) = c \cdot n + c_4 \sum_{j=2}^{n} \frac{j+1}{2} + (c_5 + c_6) \sum_{j=2}^{n} \frac{j-1}{2}$$

Il fattore $\frac{1}{2}$ si fattorizza fuori. La sommatoria $\sum_{j=2}^{n}(j-1) = \frac{n(n-1)}{2}$ e stata gia calcolata (caso peggiore). La sommatoria $\sum_{j=2}^{n}(j+1)$ e anch'essa quadratica:

$$\sum_{j=2}^{n}(j+1) = \sum_{j=2}^{n} j + \sum_{j=2}^{n} 1 = \left(\frac{n(n+1)}{2} - 1\right) + (n-1)$$

Tutti i termini sono quadratici in $n$, quindi:

$$\boxed{T_{\text{avg}}(n) = \Theta(n^2)}$$

> [!warning] Il caso medio e quadratico come il caso peggiore
> La media e dominata dai comportamenti quadratici: i casi lineari (input quasi ordinati) sono **cosi pochi** che il loro contributo non e sufficiente ad abbassare la media. La maggior parte degli input produce un comportamento di ordine $\Theta(n^2)$.

---

## Argomento alternativo: le inversioni

> [!abstract] Definizione:
> Un'**inversione** e una coppia di indici $(i, j)$ con $i < j$ tale che $A[i] > A[j]$, cioe una coppia di elementi "fuori ordine".

### Proprieta fondamentali

- Il **numero massimo** di inversioni (caso peggiore) e $\frac{n(n-1)}{2} = \Theta(n^2)$, corrispondente a tutte le coppie $(i,j)$ con $i < j$.
- Insertion Sort **risolve esattamente un'inversione** ad ogni operazione nel corpo del while.
- Quindi il numero totale di operazioni e proporzionale al numero di inversioni.

### Numero medio di inversioni

Ogni coppia $(i, j)$ con $i < j$ e un'inversione oppure no. In assenza di bias, le due possibilita sono **equiprobabili** ($p = \frac{1}{2}$). Le coppie totali sono $\frac{n(n-1)}{2}$, quindi:

$$E[\text{inversioni}] = \frac{1}{2} \cdot \frac{n(n-1)}{2} = \frac{n(n-1)}{4} = \Theta(n^2)$$

Poiche Insertion Sort risolve un'inversione alla volta, il tempo medio e $\Theta(n^2)$, confermando il risultato precedente.

---

## Riepilogo Insertion Sort

| Caso | Valore di $t_j$ | $T(n)$ | Testimone |
|------|-----------------|--------|-----------|
| Migliore | $t_j = 1$ | $\Theta(n)$ | Array ordinato crescente |
| Peggiore | $t_j = j$ | $\Theta(n^2)$ | Array ordinato decrescente |
| Medio | $t_j = \frac{j+1}{2}$ | $\Theta(n^2)$ | Input generico (equiprobabile) |

> Insertion Sort e un algoritmo **quadratico**: il caso migliore lineare si verifica solo su input gia ordinati, ma la stragrande maggioranza degli input produce un comportamento quadratico.

---

## Introduzione al Divide et Impera

### Il paradigma

> [!abstract] Definizione:
> Il **Divide et Impera** (Divide and Conquer) e un paradigma di progettazione algoritmica basato sulla **decomposizione ricorsiva**: il problema viene scomposto in sottoproblemi **dello stesso tipo** ma di **dimensione inferiore**.

A differenza delle decomposizioni viste in precedenza (es. sottosequenza massima, conteggio coppie), dove i sottoproblemi erano di natura diversa dal problema originale, nel Divide et Impera i sottoproblemi sono **istanze piu piccole dello stesso problema**.

### Schema generale

```
DivideEtImpera(A, n):
    se n e sufficientemente piccolo (caso base):
        restituisci la soluzione banale
    altrimenti:
        decomponi l'input in parti piu piccole (es. A1, A2)
        S1 = DivideEtImpera(A1)
        S2 = DivideEtImpera(A2)
        combina S1 e S2 per ottenere la soluzione S di A
        restituisci S
```

Le fasi dipendenti dal problema specifico sono:
1. **Decomposizione** dell'input
2. **Combinazione** (fusione) delle soluzioni parziali

Le chiamate ricorsive sono indipendenti dal problema: applicano lo stesso algoritmo ai sottoproblemi creati.

---

## Merge Sort

### Idea dell'algoritmo

Applicando il Divide et Impera al problema dell'ordinamento:

1. **Caso base**: se la sequenza ha un solo elemento ($n = 1$), e gia ordinata.
2. **Divide**: dividi la sequenza in due meta (circa) uguali.
3. **Impera**: ordina ricorsivamente ciascuna meta.
4. **Combina**: fondi (**merge**) le due meta ordinate in un'unica sequenza ordinata.

> [!warning] Perche serve il merge?
> La divisione e "naive": si prende semplicemente il punto di mezzo dell'array. Le due parti vengono ordinate internamente dalla ricorsione, ma **tra loro non c'e alcuna garanzia d'ordine**. Serve quindi un'operazione di fusione di due sequenze ordinate in un'unica sequenza ordinata.

### Pseudocodice di Merge Sort

```
MergeSort(A, p, r):
    if p < r:
        q = floor((p + r) / 2)
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)
```

- $p$ e $r$ sono gli indici che delimitano la sottosequenza corrente
- $q$ e l'indice di mezzo
- La chiamata iniziale e `MergeSort(A, 1, n)` (oppure `MergeSort(A, 0, n-1)`)
- La dimensione del sottoproblema e $n = r - p + 1$
- Il caso base si verifica quando $p = r$ (un solo elemento): non c'e nulla da fare

---

## Procedura Merge

### Idea

La fusione di due sequenze ordinate puo essere fatta in **tempo lineare** usando un array ausiliario $B$ e tre indici che scorrono le tre sequenze (le due meta di $A$ e l'array $B$).

```
Merge(A, p, q, r):
    i = p              // indice per la prima meta [p..q]
    j = q + 1          // indice per la seconda meta [q+1..r]
    k = p              // indice per l'array ausiliario B

    // Fase 1: confronta e copia il minore
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]
            j = j + 1
        k = k + 1

    // Fase 2: copia gli elementi rimasti
    if i <= q:
        z = i
    else:
        z = j
    while k <= r:
        B[k] = A[z]
        z = z + 1
        k = k + 1

    // Fase 3: ricopia B in A
    for i = p to r:
        A[i] = B[i]
```

> [!example] Funzionamento del Merge
> Ad ogni iterazione del primo while si confrontano gli elementi correnti delle due sequenze. Il **minore** viene copiato in $B$ (per transitivita sara minore di tutti gli elementi successivi di entrambe le sequenze). Si incrementa l'indice della sequenza da cui si e prelevato l'elemento, e l'indice $k$ di $B$. Quando una delle due sequenze si esaurisce, si copiano in blocco gli elementi rimasti dell'altra. Infine si ricopia $B$ in $A$.

### Complessita di Merge

Il numero totale di **scritture in $B$** e esattamente $n = r - p + 1$:
- Il primo while effettua un certo numero $x$ di scritture
- Il secondo while effettua le rimanenti $n - x$ scritture
- Il ciclo finale effettua altre $n$ scritture (copia $B \to A$)

Ogni iterazione di ogni ciclo ha costo costante, quindi:

$$\boxed{T_{\text{merge}}(n) = \Theta(n)}$$

---

## Analisi del tempo di esecuzione di Merge Sort

### Equazione di ricorrenza

Per un algoritmo ricorsivo, il tempo di esecuzione si definisce in modo ricorsivo:

> [!abstract] Definizione:
> L'**equazione di ricorrenza** per Merge Sort e:
> $$T(n) = \begin{cases} 1 & \text{se } n = 1 \\ 2\,T\!\left(\frac{n}{2}\right) + \Theta(n) & \text{se } n > 1 \end{cases}$$
> dove:
> - $2\,T\!\left(\frac{n}{2}\right)$ rappresenta il costo delle **due chiamate ricorsive**, ciascuna su un input di dimensione $\frac{n}{2}$
> - $\Theta(n)$ e il **contributo locale** della chiamata: include il costo di Merge ($\Theta(n)$) e le istruzioni a tempo costante (assorbite dal $\Theta$)

L'**incognita** dell'equazione e la funzione $T$ stessa. Si cerca una funzione che soddisfi questa relazione.

### Albero di ricorrenza

> [!abstract] Definizione:
> L'**albero di ricorrenza** e un albero in cui ogni nodo rappresenta una chiamata ricorsiva. Ad ogni nodo si associa:
> - **Fuori**: la dimensione dell'input ricevuto
> - **Dentro**: il contributo locale (operazioni elementari non dovute a chiamate ricorsive)

Per calcolare $T(n)$, si sommano i contributi locali di **tutti i nodi** dell'albero.

#### Struttura dell'albero

L'albero e un **albero binario completo**:

```
Livello 0:           [n]                 contributo: n
                    /    \
Livello 1:      [n/2]    [n/2]           contributo: n/2 + n/2 = n
                /  \      /  \
Livello 2:  [n/4] [n/4] [n/4] [n/4]     contributo: 4 * n/4 = n
                ...
Livello i:  2^i nodi, ciascuno [n/2^i]   contributo: 2^i * n/2^i = n
                ...
Livello log n:  n nodi, ciascuno [1]      contributo: n * O(1) = O(n)
```

#### Input al livello $i$

Un nodo al livello $i$ riceve un input di dimensione:

$$\frac{n}{2^i}$$

Tutti i nodi allo **stesso livello** ricevono input della stessa dimensione, perche ogni nodo dimezza l'input per i propri figli.

#### Altezza dell'albero

Le foglie si trovano quando l'input raggiunge la dimensione del caso base ($n = 1$):

$$\frac{n}{2^i} = 1 \implies 2^i = n \implies i = \log_2 n$$

L'albero ha dunque $\log_2 n + 1$ livelli (da $0$ a $\log_2 n$).

#### Contributo per livello

Il contributo locale di un nodo al livello $i$ e proporzionale all'input ricevuto, cioe $\frac{n}{2^i}$ (perche Merge e lineare). Al livello $i$ ci sono $2^i$ nodi, quindi il contributo totale del livello $i$ e:

$$\text{contributo livello } i = 2^i \cdot \frac{n}{2^i} = n$$

> [!warning] Osservazione chiave
> Il contributo di **ogni livello** e esattamente $n$, indipendentemente dal livello. Il lavoro totale si distribuisce uniformemente tra i livelli.

### Calcolo del tempo totale

$$T(n) = \sum_{i=0}^{\log_2 n} n = n \cdot (\log_2 n + 1) = n \log_2 n + n$$

Applicando il metodo dei limiti: $\frac{n \log n + n}{n \log n} = 1 + \frac{1}{\log n} \to 1$, quindi:

$$\boxed{T(n) = \Theta(n \log n)}$$

---

## Merge Sort: assenza di dipendenza dall'input

> [!warning] Merge Sort non ha caso migliore/peggiore distinti
> A differenza di Insertion Sort, il tempo di esecuzione di Merge Sort e **indipendente dall'input**:
> - Il contributo locale di ogni nodo (il Merge) dipende solo dalla **dimensione** dell'input, non dai valori contenuti.
> - Nel Merge, il confronto `A[i] <= A[j]` porta a operazioni a tempo costante in entrambi i rami (if/else); il numero totale di scritture e sempre $n$.
> - Quindi: $T_{\text{best}}(n) = T_{\text{worst}}(n) = T_{\text{avg}}(n) = \Theta(n \log n)$.

---

## Confronto Insertion Sort vs Merge Sort

| Proprieta | Insertion Sort | Merge Sort |
|-----------|---------------|------------|
| Paradigma | Incrementale | Divide et Impera |
| Caso migliore | $\Theta(n)$ | $\Theta(n \log n)$ |
| Caso peggiore | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| Caso medio | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| Dipendenza dall'input | Si | No |
| Memoria aggiuntiva | $O(1)$ (in-place) | $O(n)$ (array $B$) |

> [!example] Merge Sort e asintoticamente migliore
> $n \log n = o(n^2)$, quindi Merge Sort e asintoticamente piu efficiente di Insertion Sort nel caso peggiore e medio. Insertion Sort e migliore solo nel caso di input gia ordinati ($\Theta(n)$ vs $\Theta(n \log n)$).

---

## Analisi di algoritmi ricorsivi: metodo generale

L'approccio usato per Merge Sort si generalizza a qualsiasi algoritmo ricorsivo:

1. **Estrarre l'equazione di ricorrenza** dall'algoritmo, identificando:
   - Il costo locale (istruzioni non ricorsive)
   - Le chiamate ricorsive e la dimensione degli input che ricevono
2. **Costruire l'albero di ricorrenza**, determinando:
   - Il contributo locale di ogni nodo
   - Il numero di nodi per livello
   - L'altezza dell'albero (quando si raggiunge il caso base)
3. **Sommare i contributi** livello per livello e poi tra i livelli

> [!abstract] Definizione:
> Il **tempo di esecuzione** di un algoritmo ricorsivo e:
> $$T(n) = \sum_{x \in \text{nodi dell'albero}} \text{contributo locale di } x$$
>
> Raggruppando per livelli:
> $$T(n) = \sum_{i=0}^{h} C(i)$$
> dove $h$ e l'altezza dell'albero e $C(i)$ e la somma dei contributi locali di tutti i nodi al livello $i$.

> [!warning] Differenza con gli algoritmi iterativi
> Negli algoritmi iterativi il numero di ripetizioni e determinato dal costrutto di ciclo. Negli algoritmi ricorsivi il numero di ripetizioni e determinato dal **numero di nodi** dell'albero di ricorrenza, e il contributo di ogni nodo puo variare in funzione dell'input ricevuto.

---

> [!summary] Punti chiave della lezione
> 1. **Insertion Sort --- caso migliore**: $t_j = 1$ per ogni $j$ (array ordinato) $\Rightarrow$ $T(n) = \Theta(n)$.
> 2. **Insertion Sort --- caso peggiore**: $t_j = j$ per ogni $j$ (array ordinato al contrario) $\Rightarrow$ $T(n) = \Theta(n^2)$.
> 3. **Insertion Sort --- caso medio**: il valore atteso $E[t_j] = \frac{j+1}{2}$ porta a $T(n) = \Theta(n^2)$. La conferma arriva anche dall'analisi delle inversioni: il numero medio di inversioni e $\frac{n(n-1)}{4} = \Theta(n^2)$.
> 4. **Divide et Impera**: paradigma di decomposizione ricorsiva in cui i sottoproblemi sono dello stesso tipo del problema originale.
> 5. **Merge Sort**: divide l'array a meta, ordina ricorsivamente le due meta, poi le fonde con Merge in tempo $\Theta(n)$.
> 6. **Equazione di ricorrenza**: $T(n) = 2T(n/2) + \Theta(n)$, risolta tramite albero di ricorrenza: ogni livello contribuisce $n$, ci sono $\log_2 n + 1$ livelli $\Rightarrow$ $T(n) = \Theta(n \log n)$.
> 7. **Merge Sort non dipende dall'input**: non esiste distinzione tra caso migliore, peggiore e medio.

---

## Prossimi argomenti
- [ ] Esercizi su equazioni di ricorrenza e loro risoluzione
- [ ] Casistiche piu generali per l'albero di ricorrenza
- [ ] Teorema Master per la risoluzione di equazioni di ricorrenza

---

#APA #insertion-sort #merge-sort #divide-et-impera #equazione-di-ricorrenza #albero-di-ricorrenza #caso-migliore #caso-peggiore #caso-medio #inversioni