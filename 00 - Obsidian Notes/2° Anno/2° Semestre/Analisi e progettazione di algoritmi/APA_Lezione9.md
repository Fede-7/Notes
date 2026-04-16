---
date: 2026-04-09
corso: Algoritmi e Principi dell'Informatica
docente: N/D
lezione: "Lower bound Ω(n log n) per il sorting comparison-based — caso peggiore e caso medio"
tags: [APA, lower-bound, sorting, alberi-decisione, caso-medio, caso-peggiore, mergesort, quicksort, percorso-esterno]
---

# APA — Lezione 9: Lower Bound $\Omega(n \log n)$ per il Sorting Comparison-Based

**Corso:** Algoritmi e Principi dell'Informatica

---

## Argomenti trattati

- Modello degli alberi di decisione per algoritmi di ordinamento per confronti
- Proprietà degli alberi di decisione: completezza, correttezza, numero minimo di foglie
- Esempio di albero di decisione per Insertion Sort con $n=3$
- Lower bound $\Omega(n \log n)$ per il caso peggiore
- Percorso esterno e lunghezza media dei percorsi
- Lower bound $\Omega(n \log n)$ per il caso medio
- Ottimalità di Merge Sort, Heap Sort e Quick Sort

---

## 1. Il problema e la motivazione

Sappiamo che Merge Sort e Heap Sort hanno complessità $\Theta(n \log n)$ nel caso peggiore, e Quick Sort nel caso medio. Ma questi algoritmi sono **ottimali**? Esiste un algoritmo di ordinamento per confronti asintoticamente migliore?

Per rispondere, occorre trovare un **lower bound** al tempo di esecuzione di qualsiasi algoritmo di ordinamento che usi solo confronti, indipendentemente dalla sua struttura sintattica.

> [!abstract] Obiettivo
> Dimostrare che qualsiasi algoritmo di ordinamento **comparison-based** richiede $\Omega(n \log n)$ confronti sia nel caso peggiore che nel caso medio, su input di dimensione $n$.

---

## 2. Il modello degli alberi di decisione

Ogni algoritmo di ordinamento per confronti, fissata la dimensione $n$ dell'input, realizza una sequenza di confronti binari: ogni confronto $A[i] \leq A[j]$ ha due esiti (vero/falso) e in base all'esito si sceglie il prossimo confronto.

> [!abstract] Definizione: Albero di decisione di ordine $n$
> **Fissati** $n$ e un algoritmo $A$, l'**albero di decisione di ordine $n$** di $A$ è un albero binario in cui:
> - ogni **nodo interno** contiene un confronto della forma $i{:}j$ (con $1 \leq i \neq j \leq n$), che rappresenta il confronto tra $A[i]$ e $A[j]$;
> - il **figlio sinistro** si segue se $A[i] \leq A[j]$, il **figlio destro** se $A[i] > A[j]$;
> - ogni **foglia** contiene la permutazione degli indici che costituisce la soluzione ordinata.

Ogni percorso radice-foglia corrisponde a un'esecuzione dell'algoritmo su un input specifico. La lunghezza del percorso è il numero di confronti effettuati.

**Proprietà chiave:**
- Il numero di confronti nel caso peggiore = **altezza** dell'albero.
- Il numero medio di confronti = **lunghezza media dei percorsi** (percorso esterno diviso numero di foglie).

---

## 3. Proprietà degli alberi di decisione

### Completezza: almeno $n!$ foglie

Per essere corretto, un albero di decisione deve contenere in almeno una foglia ogni possibile permutazione degli $n$ elementi. Se mancasse una permutazione $\pi$, esisterebbe un input la cui soluzione è $\pi$ e l'algoritmo non potrebbe rispondere correttamente.

Quindi: il numero di foglie $\geq n!$.

### Lunghezza minima dei percorsi: almeno $n-1$

Per ogni foglia dell'albero, il percorso radice-foglia deve contenere almeno un nodo che confronta ogni coppia di elementi **adiacenti** nella permutazione della foglia.

**Perché è necessario confrontare le coppie adiacenti?** Se $A$ e $B$ sono adiacenti nella soluzione ma non sono mai stati confrontati, allora l'insieme dei confronti effettuati è compatibile sia con la permutazione $\ldots A, B \ldots$ sia con $\ldots B, A \ldots$, quindi l'algoritmo non può distinguere tra le due e darebbe la risposta sbagliata per uno dei due input.

Poiché in una permutazione di $n$ elementi ci sono $n-1$ coppie adiacenti, ogni percorso ha lunghezza $\geq n-1$.

*(Nota: la transitività permette di non confrontare tutte le $\binom{n}{2}$ coppie, solo le adiacenti non deducibili per transitività.)*

---

## 4. Esempio: albero di decisione di Insertion Sort per $n=3$

```
              2:1
            ≤/    \>
          3:1       3:2
         ≤/  \>    ≤/  \>
       3:2   [213] [132] [321]
      ≤/ \>
    [123] [132]... 
```

*(Schema semplificato.)* L'albero ha esattamente $3! = 6$ foglie, una per ogni permutazione di tre elementi. Ogni foglia si raggiunge dopo almeno $n-1 = 2$ confronti. L'altezza è 3, che corrisponde al caso peggiore di Insertion Sort su 3 elementi.

---

## 5. Lower bound $\Omega(n \log n)$ per il caso peggiore

**Obiettivo:** dimostrare che l'altezza $h$ di qualsiasi albero di decisione di ordine $n$ è $\Omega(n \log n)$.

**Dimostrazione:**

Un albero binario di altezza $h$ ha al più $2^h$ foglie. Ogni albero di decisione di ordine $n$ deve avere almeno $n!$ foglie. Quindi:

$$n! \leq 2^h \implies h \geq \log_2(n!)$$

Rimane da stimare $\log_2(n!)$ dal basso. Si divide la produttoria a metà:

$$n! = \prod_{i=1}^{n} i \geq \prod_{i=\lceil n/2 \rceil}^{n} i \geq \prod_{i=\lceil n/2 \rceil}^{n} \frac{n}{2} = \left(\frac{n}{2}\right)^{n/2}$$

Quindi:

$$\log_2(n!) \geq \frac{n}{2} \log_2\!\left(\frac{n}{2}\right) = \frac{n}{2}(\log_2 n - 1) = \Omega(n \log n)$$

> [!abstract] Risultato: lower bound caso peggiore
> Per qualsiasi algoritmo di ordinamento comparison-based, il numero di confronti nel caso peggiore è:
> $$T_{\text{worst}}(n) = \Omega(n \log n)$$
> Gli algoritmi **ottimali per il caso peggiore** tra quelli visti sono **Merge Sort** e **Heap Sort**: entrambi hanno $\Theta(n \log n)$ nel caso peggiore.

---

## 6. Lower bound $\Omega(n \log n)$ per il caso medio

### Il percorso esterno come misura del caso medio

Se l'albero di decisione ha $z$ foglie $f_1, \ldots, f_z$ e $\pi(f_i)$ è il percorso dalla radice a $f_i$, il numero medio di confronti è:

$$\text{lunghezza media} = \frac{1}{z} \sum_{i=1}^{z} |\pi(f_i)| = \frac{PE(T)}{z}$$

dove $PE(T) = \sum_{i=1}^{z} |\pi(f_i)|$ è il **percorso esterno** di $T$.

Per minimizzare il numero medio di confronti con $z = n!$ foglie fissato, occorre **minimizzare $PE(T)$**.

### L'albero con il minimo percorso esterno

> [!abstract] Proprietà: albero con minimo percorso esterno
> L'albero binario con $z$ foglie che minimizza il percorso esterno è quello in cui **tutte le foglie si trovano a profondità $h$ o $h-1$** (dove $h$ è l'altezza), analogamente agli alberi completi.

**Dimostrazione (informale):** si mostra che qualsiasi scostamento da questa proprietà (es. spostare una foglia da profondità $h$ a $h+1$) peggiora il percorso esterno. In particolare, se si eliminano due foglie a profondità $h$ (creando una foglia-padre a $h-1$) e si aggiungono due nuove foglie a $h+1$ per mantenere lo stesso numero di foglie, il percorso esterno aumenta esattamente di 1.

### Calcolo del percorso esterno ottimo

Sia $n_h$ il numero di foglie a profondità $h$ e $n_{h-1}$ quello a profondità $h-1$. Due equazioni:

$$n_h + n_{h-1} = n! \qquad \text{(tutte le foglie)}$$

$$n_h + 2n_{h-1} = 2^h \qquad \text{(albero pieno di altezza } h \text{ avrebbe } 2^h \text{ foglie)}$$

La seconda equazione deriva dal fatto che se tutte le foglie a $h-1$ avessero due figli, si avrebbe un albero pieno di altezza $h$. Risolvendo il sistema:

$$n_{h-1} = 2^h - n!, \qquad n_h = 2n! - 2^h$$

Il percorso esterno ottimo è quindi:

$$PE(T) = h \cdot n_h + (h-1) \cdot n_{h-1} = h \cdot n! - 2^h + n! \cdot (h-1) - n_{h-1}(h-1)$$

Semplificando:

$$\boxed{PE(T) = h \cdot n! - 2^h + n!}$$

*(I calcoli intermedi espandono e semplificano i termini; il risultato netto è questo.)*

### Stima dell'altezza $h$

L'albero con minimo percorso esterno è "quasi completo" (foglie a profondità $h$ o $h-1$). Poiché ogni nodo interno ha esattamente 2 figli, un albero binario con $n!$ foglie ha $2n!-1$ nodi totali. L'altezza di un albero quasi completo con $m$ nodi è $h = \lceil \log_2 m \rceil \approx \log_2(n!)$ (a meno di $\pm 1$).

Quindi $h = \lceil \log_2(n!) \rceil$ e $2^h \leq 2 \cdot n!$ (perché $h$ è l'intero più piccolo tale che $2^h \geq n!$).

### Il numero medio di confronti è $\Omega(n \log n)$

$$\frac{PE(T)}{n!} = h - \frac{2^h}{n!} + 1$$

Poiché $h = \lceil \log_2(n!) \rceil$, si ha $2^h = n! \cdot 2^\epsilon$ con $0 \leq \epsilon < 1$, quindi $\frac{2^h}{n!} = 2^\epsilon \leq 2$. Pertanto:

$$\frac{PE(T)}{n!} = \lceil \log_2(n!) \rceil - 2^\epsilon + 1 = \Theta(\log(n!)) = \Omega(n \log n)$$

usando la stima $\log_2(n!) = \Omega(n \log n)$ già dimostrata sopra.

> [!abstract] Risultato: lower bound caso medio
> Per qualsiasi algoritmo di ordinamento comparison-based, il numero medio di confronti è:
> $$T_{\text{avg}}(n) = \Omega(n \log n)$$
> Gli algoritmi **ottimali per il caso medio** sono **Merge Sort**, **Heap Sort** e **Quick Sort**: tutti e tre hanno $\Theta(n \log n)$ nel caso medio.

---

## 7. Riepilogo: ottimalità degli algoritmi

| Algoritmo | Caso peggiore | Caso medio | Ottimale pegg. | Ottimale medio |
|---|---|---|---|---|
| Merge Sort | $\Theta(n \log n)$ | $\Theta(n \log n)$ | ✓ | ✓ |
| Heap Sort | $\Theta(n \log n)$ | $\Theta(n \log n)$ | ✓ | ✓ |
| Quick Sort | $\Theta(n^2)$ | $\Theta(n \log n)$ | ✗ | ✓ |
| Insertion Sort | $\Theta(n^2)$ | $\Theta(n^2)$ | ✗ | ✗ |

**Lower bound per il caso migliore:** ogni algoritmo deve fare almeno $n-1$ confronti (occorre verificare almeno tutte le coppie adiacenti), quindi $T_{\text{best}}(n) = \Omega(n)$.

---

## 8. Il significato del risultato

> [!tip] Parole del Professore
> > [!tip]
> > "Il fatto che voi non riusciate a trovare un algoritmo migliore non significa che non esista. O c'è un'argomentazione sufficientemente astratta che vi permette di quantificare su tutti i possibili modi di risolvere, oppure non avete modo di rispondere."

La tecnica usata — astrarsi dalla struttura sintattica degli algoritmi e ragionare sulle classi di equivalenza definite dall'albero di decisione — è un esempio di **approccio information-theoretic**: si ragiona sul numero di output distinti che l'algoritmo deve essere in grado di produrre e si deduce il numero minimo di confronti necessari per discriminarli tutti.

Questo è diverso dall'analisi sintattica dei singoli algoritmi. Due algoritmi con alberi di decisione identici sono equivalenti dal punto di vista della complessità, anche se scritti in modo diverso. La tecnica permette di affermare che **nessun** algoritmo comparison-based può fare asintoticamente meglio di $n \log n$, anche uno ancora non scoperto.

---

> [!abstract] Punti chiave della lezione
> - Ogni algoritmo comparison-based per ordinamento ha un unico albero di decisione di ordine $n$: i percorsi nell'albero corrispondono alle esecuzioni.
> - L'altezza dell'albero = complessità caso peggiore; la lunghezza media dei percorsi = complessità caso medio.
> - Poiché ci sono $n!$ permutazioni distinte, l'albero ha almeno $n!$ foglie, e questo implica altezza $\geq \log_2(n!) = \Omega(n \log n)$.
> - L'albero che minimizza il percorso esterno ha foglie a profondità $h$ o $h-1$; calcolando il percorso esterno ottimo si ottiene che il numero medio di confronti è anch'esso $\Omega(n \log n)$.
> - Merge Sort e Heap Sort sono ottimali nel caso peggiore; Merge Sort, Heap Sort e Quick Sort sono ottimali nel caso medio.

## Prossimi argomenti

- [ ] Code a priorità (heap) e applicazione all'algoritmo di Dijkstra
- [ ] Relazione tra algoritmi ricorsivi e iterativi: trasformazione sistematica
- [ ] Tecniche di progettazione di algoritmi (divide et impera, programmazione dinamica)

#APA #lower-bound #sorting #alberi-decisione #caso-medio #caso-peggiore #mergesort #quicksort #percorso-esterno
