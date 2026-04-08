---
Date: 2026-03-10
Professore: Benerecetti
tags:
  - APA
---



# Lezione 2: Ottimizzazioni della Sottosequenza Massima e Introduzione all'Ordinamento

---

## Argomenti trattati
- Riepilogo del problema della sottosequenza contigua di somma massima e dell'algoritmo cubico
- Prima ottimizzazione: eliminazione del ciclo interno con somma incrementale $\to O(n^2)$
- Seconda ottimizzazione: algoritmo lineare (Kadane) con scarto di sottosequenze a prefisso negativo $\to O(n)$
- Dimostrazione di correttezza dell'algoritmo lineare
- Confronto tra le due strategie di ottimizzazione: riduzione del costo per soluzione vs riduzione dello spazio di ricerca
- Introduzione al problema dell'ordinamento: definizione formale, permutazioni, inversioni
- Insertion Sort: algoritmo, analisi parametrica e dipendenza dai dati
- Analisi per casi: caso migliore, caso peggiore, caso medio

---

## Riepilogo: il problema della sottosequenza contigua di somma massima

> [!abstract] Definizione:
> Data una sequenza $A = A_1, A_2, \ldots, A_n$ di $n$ numeri (positivi, negativi o nulli), una **sottosequenza contigua** (o *infisso*) e individuata da una coppia di indici $(i, j)$ con $1 \leq i \leq j \leq n$. Il valore della sottosequenza e:
> $$S(i, j) = \sum_{k=i}^{j} A_k$$
> **Obiettivo:** trovare $\max_{i \leq j} S(i, j)$, con la convenzione che la sottosequenza vuota ha somma $0$.

Nella lezione precedente abbiamo visto che:

- Ogni sottosequenza contigua non vuota e univocamente determinata da una coppia $(i, j)$ con $i \leq j$.
- Il numero di tali coppie e $\frac{n(n+1)}{2} = \Theta(n^2)$.
- L'algoritmo **naif** (forza bruta) genera tutte le coppie $(i, j)$ e per ciascuna calcola la somma con un ciclo interno su $k$, ottenendo tre cicli annidati.

### Algoritmo 1: Forza bruta — $\Theta(n^3)$

```python
def max_subarray_cubic(A):
    n = len(A)
    max_sum = 0

    for i in range(1, n+1):
        for j in range(i, n+1):
            s = 0
            for k in range(i, j+1):
                s = s + A[k]
            if s > max_sum:
                max_sum = s

    return max_sum
```

Il tempo di esecuzione e:
$$T(n) = \sum_{i=1}^{n} \sum_{j=i}^{n} (j - i + 1) = \Theta(n^3)$$

---

## Prima ottimizzazione: eliminazione del ciclo interno — $\Theta(n^2)$

### Osservazione chiave

Quando il ciclo esterno su $i$ e fissato e $j$ avanza di $1$, l'algoritmo cubico ricalcola da zero l'intera somma $\sum_{k=i}^{j} A_k$. Questo e lavoro inutile, perche se conosciamo la somma della sottosequenza precedente possiamo estenderla in tempo costante:

$$S(i, j+1) = S(i, j) + A_{j+1}$$

Cioe basta sommare il nuovo elemento al valore gia calcolato. Il ciclo interno su $k$ diventa superfluo.

### L'idea: somma incrementale

- Ogni volta che cambia $i$ (nuovo punto di inizio), si reinizializza $\text{sum} = 0$.
- Finche $i$ resta fisso e $j$ avanza, si aggiorna $\text{sum} = \text{sum} + A_j$.
- La variabile `sum` e **persistente** tra le iterazioni di $j$: non viene azzerata ad ogni passo, ma solo quando cambia $i$.

### Algoritmo 2: Somma incrementale — $\Theta(n^2)$

```python
def max_subarray_quadratic(A):
    n = len(A)
    max_sum = 0

    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum = sum + A[j]
            if sum > max_sum:
                max_sum = sum

    return max_sum
```

### Analisi della complessita

Questo algoritmo ha esattamente la stessa struttura del conteggio delle coppie $(i, j)$ con $i \leq j$: due cicli annidati, con il corpo interno a **tempo costante** (un'addizione e un confronto). Il numero di iterazioni e:
$$T(n) = \sum_{i=1}^{n} (n - i + 1) = \frac{n(n+1)}{2} = \Theta(n^2)$$

> [!warning] Limiti dell'approccio quadratico
> Poiche il numero di sottosequenze contigue e $\Theta(n^2)$, qualsiasi algoritmo che le esamini **tutte** non potra fare meglio di $\Theta(n^2)$, anche se il costo di analisi di ciascuna e $O(1)$. Per scendere sotto il quadratico, bisogna **non esaminare tutte le sottosequenze** — e garantire formalmente che quelle scartate non contengano la soluzione ottima.

---

## Seconda ottimizzazione: algoritmo lineare (Kadane) — $\Theta(n)$

### L'idea: ridurre lo spazio di ricerca

L'unico modo per scendere sotto $\Theta(n^2)$ e **non analizzare tutte le sottosequenze**, scartandone alcune con la certezza di non perdere quella ottima. Si tratta di ridurre lo spazio di ricerca da quadratico a lineare.

### Proprieta fondamentale: scarto delle sottosequenze con prefisso negativo

> [!abstract] Definizione:
> Usiamo la notazione abbreviata $A(i, j) = \sum_{k=i}^{j} A_k$ per indicare la somma dell'infisso tra le posizioni $i$ e $j$.

Supponiamo di trovarci nella seguente situazione: esiste un indice $r$ tale che:

1. Per ogni $l$ con $i \leq l < r$, tutti i prefissi sono non negativi: $A(i, l) \geq 0$
2. Ma l'intera sottosequenza fino a $r$ e negativa: $A(i, r) < 0$

> [!warning] Conseguenza cruciale
> In questa situazione, **ogni sottosequenza che parte da un punto $z$ nell'intervallo $[i, r]$ e si estende oltre $r$** e dominata da una sottosequenza che parte da $r+1$.
>
> Formalmente: per ogni $z \in [i, r]$ e ogni $q > r$:
> $$A(z, q) < A(r+1, q)$$
> Quindi e inutile considerare qualsiasi sottosequenza che contenga un infisso di somma negativa.

### Dimostrazione

> [!example] Esempio concreto della situazione
> ```
> Posizioni:   i       ...      r-1    r
> Valori:      3       -2        1    -5
> ```
> - $A(i, i) = 3 \geq 0$
> - $A(i, i+1) = 3 - 2 = 1 \geq 0$
> - $A(i, i+2) = 3 - 2 + 1 = 2 \geq 0$
> - $A(i, r) = 3 - 2 + 1 - 5 = -3 < 0$
>
> Qualsiasi sottosequenza che parta tra $i$ e $r$ ed arrivi oltre $r$ sara peggiore di quella che parte da $r+1$.

La dimostrazione procede in due passi.

**Passo 1:** Mostriamo che $A(z, r) < 0$ per ogni $z \in [i, r]$.

Scomponiamo:
$$A(i, r) = A(i, z-1) + A(z, r)$$

Per ipotesi, $A(i, z-1) \geq 0$ (perche $z - 1 < r$ e tutti i prefissi da $i$ sono non negativi). Poiche $A(i, r) < 0$, necessariamente:
$$A(z, r) = A(i, r) - A(i, z-1) \leq A(i, r) < 0$$

**Passo 2:** Mostriamo che $A(z, q) < A(r+1, q)$ per ogni $q > r$.

Scomponiamo la sottosequenza $A(z, q)$ in due parti:
$$A(z, q) = A(z, r) + A(r+1, q)$$

Poiche dal Passo 1 sappiamo che $A(z, r) < 0$, otteniamo:
$$A(z, q) = \underbrace{A(z, r)}_{< \; 0} + A(r+1, q) < A(r+1, q)$$

Dunque qualsiasi sottosequenza che includa la parte fino a $r$ e strettamente peggiore di quella che parte da $r+1$. $\square$

> [!warning] L'osservazione vale per OGNI punto di inizio nell'intervallo $[i, r]$
> Non si tratta solo di scartare le estensioni della sottosequenza che parte da $i$: **qualsiasi** sottosequenza che parta da un qualunque punto $z$ tra $i$ e $r$ e si estenda oltre $r$ e dominata. Questo e cio che permette di saltare l'intero intervallo e ripartire da $r+1$, eliminando un numero quadratico di sottosequenze e ottenendo un tempo lineare.

### Algoritmo 3: Algoritmo lineare (Kadane) — $\Theta(n)$

L'idea dell'algoritmo e la seguente:
- Si parte con $i = 1$ e si estende $j$ progressivamente.
- Finche $\text{sum} \geq 0$, si continua ad estendere (aggiungendo $A_j$ alla somma corrente).
- Ogni volta che si estende, si verifica se il nuovo valore di `sum` e il migliore trovato finora.
- Appena $\text{sum} < 0$, si sa che nessuna estensione della sottosequenza corrente (che parte da $i$) potra essere ottimale. Si **resetta** `sum = 0` e si sposta $i$ a $j + 1$, ripartendo da li.

```python
def max_subarray_linear(A):
    n = len(A)
    max_sum = 0
    sum = 0
    # start_i = 1  # punto di inizio della sottosequenza corrente

    for j in range(1, n+1):
        sum = sum + A[j]
        if sum < 0:
            sum = 0
            # start_i = j + 1  # reset: riparto dalla posizione successiva
        elif sum > max_sum:
            max_sum = sum
            # max_i = start_i  # aggiorno gli estremi della migliore
            # max_j = j

    return max_sum
```

> [!example] Traccia del funzionamento
> Quando `sum` diventa negativo, il reset corrisponde a dire: "la sottosequenza che partiva da $i$ e arrivava fino a $j$ ha somma negativa, quindi qualsiasi estensione sara peggiore di ripartire da $j+1$". Si riparte dalla **sottosequenza vuota** che inizia in $j+1$ (con somma $0$).
>
> Se si vogliono anche gli indici della sottosequenza ottimale, basta mantenere le variabili `start_i`, `max_i`, `max_j` (indicate come commenti nel codice).

### Analisi della complessita

L'algoritmo ha un **unico ciclo `for`** su $j$ che va da $1$ a $n$. Il corpo del ciclo esegue operazioni a tempo costante (un'addizione, uno o due confronti, eventualmente un'assegnazione).

$$T(n) = \sum_{j=1}^{n} O(1) = \Theta(n)$$

> [!abstract] Definizione:
> L'algoritmo e **ottimo**: il tempo $\Theta(n)$ e un **limite inferiore naturale** per questo problema, perche qualsiasi algoritmo deve almeno leggere tutti gli $n$ elementi della sequenza (non si puo sapere a priori quali siano rilevanti). Fare meglio di $O(n)$ e impossibile.

---

## Confronto delle tre versioni

| Versione | Complessita | Strategia |
|---|---|---|
| Forza bruta | $\Theta(n^3)$ | Genera tutte le coppie, calcola ogni somma da zero |
| Somma incrementale | $\Theta(n^2)$ | Genera tutte le coppie, riusa la somma precedente |
| Kadane (lineare) | $\Theta(n)$ | Esamina solo sottosequenze con prefissi non negativi |

### Due filosofie di ottimizzazione

> [!warning] Distinzione fondamentale tra le due ottimizzazioni
> **Prima ottimizzazione (da cubico a quadratico):** lo spazio di ricerca resta lo stesso (tutte le $\Theta(n^2)$ sottosequenze). Si ottimizza il **costo di calcolo** del valore associato a ciascuna soluzione, sfruttando la relazione tra soluzioni adiacenti ($S(i, j+1) = S(i, j) + A_{j+1}$).
>
> **Seconda ottimizzazione (da quadratico a lineare):** si **riduce lo spazio di ricerca**, eliminando intere famiglie di sottosequenze con la garanzia formale che non contengano la soluzione ottima. Il numero di sottosequenze esaminate scende da $\Theta(n^2)$ a $O(n)$.

> [!example] Analogia con i problemi di ottimizzazione
> In un problema di ottimizzazione ci sono **soluzioni ammissibili** (qui: tutte le sottosequenze contigue) e si cerca quella **ottima** (di somma massima).
> - La prima strategia mantiene lo stesso insieme di soluzioni ammissibili e velocizza la valutazione di ciascuna.
> - La seconda strategia riduce l'insieme di soluzioni esplorate, dimostrando che quelle scartate non possono essere ottime.

---

## Approccio alla progettazione di algoritmi

Il percorso seguito per il problema della sottosequenza massima illustra una metodologia generale:

1. **Partire da una soluzione naif** (forza bruta): corretta per costruzione (esamina tutto), ma inefficiente.
2. **Ottimizzare preservando la correttezza**: prima si trova una soluzione corretta, poi si cerca di renderla piu efficiente.
3. **Individuare sorgenti di inefficienza**:
   - *Operazioni ridondanti*: ricalcolo di somme gia note $\to$ eliminazione del ciclo interno.
   - *Soluzioni inutili*: sottosequenze che non possono essere ottime $\to$ riduzione dello spazio di ricerca.

> [!warning] Ordine corretto nella progettazione
> Non si parte cercando la soluzione piu efficiente per poi verificarne la correttezza. Si parte dalla **correttezza** e si migliora progressivamente l'**efficienza**.

---

## Introduzione al problema dell'ordinamento

### Definizione formale

> [!abstract] Definizione:
> Data una sequenza $A = (a_1, a_2, \ldots, a_n)$ di $n$ elementi appartenenti a un dominio $D$ (ad esempio $\mathbb{Z}$) dotato di una **relazione d'ordine totale** $\leq$ (riflessiva, antisimmetrica, transitiva e totale), il problema dell'ordinamento richiede di trovare una **permutazione** $\sigma: \{1, \ldots, n\} \to \{1, \ldots, n\}$ biiettiva tale che:
> $$a_{\sigma(k)} \leq a_{\sigma(k+1)} \quad \text{per ogni } k \in \{1, \ldots, n-1\}$$

In altre parole, la sequenza riordinata $a_{\sigma(1)}, a_{\sigma(2)}, \ldots, a_{\sigma(n)}$ rispetta la relazione d'ordine.

> [!warning] La notazione con indici annidati
> La notazione $a_{\sigma(k)}$ puo confondere: $\sigma$ non e un numero, ma una **funzione** (o equivalentemente un array di indici). Il valore $\sigma(k)$ indica quale posizione dell'array originale va messa in posizione $k$ nell'array ordinato.

### Approccio esaustivo: generare tutte le permutazioni

L'approccio di forza bruta sarebbe: generare tutte le possibili permutazioni di $n$ elementi, e per ciascuna verificare se rispetta l'ordinamento (costo lineare $O(n)$).

Il tempo totale sarebbe:
$$T(n) = n! \cdot n$$

> [!warning] Il fattoriale cresce enormemente
> Il numero di permutazioni $n!$ e enorme. Tramite l'approssimazione di Stirling:
> $$n! \approx \sqrt{2\pi n} \cdot \left(\frac{n}{e}\right)^n$$
> Si puo mostrare che $n!$ sta tra $(n/2)^{n/2}$ e $n^n$:
> $$(n/2)^{n/2} \leq n! \leq n^n$$
> Entrambi i limiti sono molto piu grandi di $2^n$, rendendo questo approccio totalmente impraticabile.

### Il concetto di inversione

> [!abstract] Definizione:
> Data una sequenza $A = (a_1, \ldots, a_n)$, un'**inversione** e una coppia di indici $(i, j)$ tale che:
> $$i < j \quad \text{e} \quad a_i > a_j$$
> Cioe due elementi che si trovano nell'ordine sbagliato rispetto alla relazione $\leq$.

Se non esistono inversioni, la sequenza e gia ordinata. Il numero massimo di inversioni e:
$$\binom{n}{2} = \frac{n(n-1)}{2} = \Theta(n^2)$$

(Si usa il minore stretto $i < j$, quindi il conteggio e $n(n-1)/2$ anziche $n(n+1)/2$.)

Molti algoritmi di ordinamento operano **eliminando inversioni**: individuano coppie fuori ordine e le correggono con uno swap. Poiche sistemare un'inversione costa $O(1)$ e ce ne sono al piu $O(n^2)$, si ottiene immediatamente un limite superiore di $O(n^2)$ per questa famiglia di algoritmi.

---

## Insertion Sort

### Idea intuitiva

Insertion Sort simula il modo in cui molti giocatori di carte ordinano le proprie carte: si scorrono le carte da sinistra a destra, e ogni nuova carta viene **inserita nella posizione corretta** all'interno della parte gia ordinata.

- Si parte dall'idea che un singolo elemento e gia ordinato.
- Ad ogni passo si prende l'elemento successivo e lo si inserisce nella posizione giusta nella sottosequenza gia ordinata, estendendola di un elemento.

> [!warning] Insertion Sort vs Selection Sort
> - **Insertion Sort**: sceglie l'elemento (il prossimo nella sequenza) e cerca la **posizione corretta** nella parte ordinata.
> - **Selection Sort**: sceglie la posizione (la prossima da riempire) e cerca l'**elemento corretto** nella parte non ordinata.

### Algoritmo

```python
def insertion_sort(A, n):
    for j in range(2, n+1):        # j = 2, 3, ..., n
        x = A[j]                   # elemento da inserire
        i = j - 1                  # ultimo indice della parte ordinata
        while i > 0 and A[i] > x:  # scorre all'indietro cercando la posizione
            A[i+1] = A[i]          # sposta l'elemento a destra
            i = i - 1              # decrementa l'indice
        A[i+1] = x                 # inserisce x nella posizione corretta
```

### Funzionamento dettagliato

Ad ogni iterazione del ciclo esterno (indice $j$):

1. La sottosequenza $A[1 \ldots j-1]$ e **gia ordinata** (invariante di ciclo).
2. Si salva $x = A[j]$ (l'elemento da inserire) e si pone $i = j - 1$.
3. Il ciclo `while` confronta $x$ con gli elementi della parte ordinata, procedendo all'indietro:
   - Se $A[i] > x$: si sposta $A[i]$ di una posizione a destra ($A[i+1] = A[i]$) e si decrementa $i$.
   - Se $A[i] \leq x$ oppure $i = 0$: si e trovata la posizione corretta.
4. Si inserisce $x$ in posizione $i + 1$:
   - Se $i = 0$, la posizione corretta e la prima ($1 = 0 + 1$).
   - Altrimenti, la posizione corretta e subito dopo l'ultimo elemento $\leq x$.

---

## Analisi di Insertion Sort

### Il problema: dipendenza dai dati

> [!warning] Il tempo di esecuzione dipende dai dati, non solo dalla dimensione
> A differenza degli algoritmi visti in precedenza (dove il tempo dipendeva solo da $n$), in Insertion Sort il numero di iterazioni del ciclo `while` dipende da **quali valori** sono contenuti nella sequenza e dal loro **ordine relativo**.
>
> Due sequenze della stessa lunghezza possono avere tempi di esecuzione molto diversi. Ad esempio, una sequenza gia ordinata e una in ordine inverso richiedono tempi radicalmente differenti.

### Analisi parametrica

Per ciascun valore di $j$ (da $2$ a $n$), definiamo il parametro $t_j$ come il **numero di iterazioni del ciclo `while`** quando l'indice esterno vale $j$. Questi parametri catturano la dipendenza dai dati.

Il tempo di esecuzione complessivo puo essere scritto come:
$$T(n; t_2, t_3, \ldots, t_n) = c_1 \cdot n + (c_2 + c_3 + c_7)(n-1) + c_4 \sum_{j=2}^{n} t_j + (c_5 + c_6) \sum_{j=2}^{n} (t_j - 1)$$

dove $c_1, c_2, \ldots, c_7$ sono le costanti associate al costo di ciascuna linea di codice.

> [!warning] I parametri $t_j$ sono indipendenti tra loro
> Il valore di $t_j$ dipende dalla posizione relativa di $A[j]$ rispetto agli elementi gia ordinati $A[1 \ldots j-1]$. Non c'e alcuna relazione tra $t_j$ e $t_{j'}$ per $j \neq j'$: un parametro puo valere $1$ (l'elemento e gia al posto giusto) e un altro puo valere $j-1$ (l'elemento va spostato all'inizio).

### Limiti dei parametri

Per ogni $j$, il parametro $t_j$ soddisfa:
$$1 \leq t_j \leq j$$

- **Minimo** ($t_j = 1$): il ciclo `while` esegue un solo confronto (la condizione e subito falsa), cioe $A[j]$ e gia nella posizione corretta (e maggiore o uguale di $A[j-1]$).
- **Massimo** ($t_j = j$): il ciclo `while` scorre l'intera parte ordinata e si ferma solo quando $i = 0$, cioe $A[j]$ e il piu piccolo di tutti.

### Caso migliore: sequenza gia ordinata — $\Theta(n)$

Se la sequenza e **gia ordinata**, allora per ogni $j$: $A[j] \geq A[j-1]$, dunque $t_j = 1$:
$$\sum_{j=2}^{n} t_j = \sum_{j=2}^{n} 1 = n - 1$$

Il tempo di esecuzione diventa:
$$T_{\text{best}}(n) = c_1 n + (c_2 + c_3 + c_7)(n-1) + c_4(n-1) + (c_5 + c_6) \cdot 0 = \Theta(n)$$

### Caso peggiore: sequenza in ordine inverso — $\Theta(n^2)$

Se la sequenza e in **ordine decrescente**, allora per ogni $j$: $A[j]$ e piu piccolo di tutti gli elementi precedenti, dunque $t_j = j$:
$$\sum_{j=2}^{n} t_j = \sum_{j=2}^{n} j = \frac{n(n+1)}{2} - 1 = \Theta(n^2)$$

Il tempo di esecuzione diventa:
$$T_{\text{worst}}(n) = \Theta(n^2)$$

### Riepilogo dell'analisi per casi

| Caso | Condizione | $t_j$ | $\sum t_j$ | Complessita |
|---|---|---|---|---|
| Migliore | Sequenza gia ordinata | $t_j = 1$ | $n - 1$ | $\Theta(n)$ |
| Peggiore | Sequenza in ordine inverso | $t_j = j$ | $\Theta(n^2)$ | $\Theta(n^2)$ |

> [!warning] Significato dell'analisi per casi
> - Se caso migliore e caso peggiore fossero **asintoticamente equivalenti** ($\Theta(f(n))$ per la stessa $f$), avremmo determinato il tempo di esecuzione dell'algoritmo.
> - Quando sono **diversi** (come qui: $\Theta(n)$ vs $\Theta(n^2)$), si pone il problema dell'**analisi del caso medio**, che richiede tecniche probabilistiche e combinatorie piu avanzate.

### Input realmente diversi

> [!abstract] Definizione:
> Fissata la dimensione $n$, gli input realmente diversi per Insertion Sort corrispondono alle **permutazioni** di $n$ elementi: cio che conta non sono i valori assoluti degli elementi, ma il loro **ordine relativo**. Due sequenze con lo stesso ordine relativo (ad esempio $[1, 3, 2]$ e $[10, 30, 20]$) produrranno esattamente lo stesso numero di operazioni.
>
> Il numero di permutazioni di $n$ elementi e $n!$, quindi per ogni $n$ ci sono al piu $n!$ comportamenti distinti dell'algoritmo.

---

> [!summary] Punti chiave della lezione
> 1. **Da $\Theta(n^3)$ a $\Theta(n^2)$**: eliminando il ciclo interno e mantenendo la somma incrementale tra iterazioni successive di $j$, si riduce il costo di valutazione di ogni sottosequenza da $O(n)$ a $O(1)$.
> 2. **Da $\Theta(n^2)$ a $\Theta(n)$ (Kadane)**: dimostrando che ogni sottosequenza contenente un prefisso di somma negativa e subottimale, si riduce lo spazio di ricerca da $\Theta(n^2)$ a $O(n)$ sottosequenze. L'algoritmo e **ottimo** (limite inferiore $\Omega(n)$).
> 3. **Due strategie di ottimizzazione**: (a) ridurre il costo per soluzione, (b) ridurre il numero di soluzioni esaminate. La seconda e piu potente ma richiede una dimostrazione di correttezza.
> 4. **Ordinamento**: definito formalmente come ricerca di una permutazione biiettiva che rispetti $\leq$. Il concetto di inversione (coppia fuori ordine) fornisce un approccio naturale: al piu $n(n-1)/2$ inversioni $\to$ approccio quadratico.
> 5. **Insertion Sort**: algoritmo semplice ed efficiente per piccoli input. Il tempo di esecuzione dipende dai dati: $\Theta(n)$ nel caso migliore, $\Theta(n^2)$ nel caso peggiore.
> 6. **Analisi parametrica**: quando il tempo dipende dai dati, si introducono parametri $t_j$ e si studiano caso migliore e caso peggiore come istanze concrete che realizzano gli estremi.

---

## Prossimi argomenti
- [ ] Analisi del caso medio di Insertion Sort
- [ ] Algoritmi di ordinamento basati su divide et impera (Merge Sort)
- [ ] Equazioni di ricorrenza per algoritmi ricorsivi
- [ ] Metodi generali di risoluzione delle ricorrenze

---

#APA #sottosequenza-massima #Kadane #algoritmo-lineare #ordinamento #insertion-sort #analisi-per-casi #inversioni #permutazioni
