---
date: 2026-04-14
corso: Algoritmi e Principi dell'Informatica
lezione: "Algoritmo di Dijkstra — Implementazione con heap di priorità e array associativi"
tags: [APA, Dijkstra, shortest-path, heap, priority-queue, array-associativi, grafi-pesati, rilassamento-archi]
---

# APA — Algoritmo di Dijkstra: Heap di Priorità e Array Associativi

**Corso:** Algoritmi e Principi dell'Informatica

---

## Argomenti trattati

- Ricapitolazione dell'algoritmo di Dijkstra e della strategia di rilassamento degli archi
- Problema di implementazione efficiente: ricerca del minimo in un insieme di vertici
- Naive vs ottimizzata: array lineare vs heap di priorità
- Struttura dati heap binario e operazioni (extract-min, decrease-key)
- Array associativi come implementazione di tabelle di accesso arbitrario
- Dualità albero-array per l'implementazione di heap
- Applicazione al calcolo dei percorsi minimi

---

## 1. Recap: Dijkstra e rilassamento degli archi

> [!info] Algoritmo di Dijkstra
> Calcola i **percorsi minimi** da una sorgente $S$ a tutti gli altri vertici in grafi con **pesi non negativi**.

**Idea principale:** mantenere due insiemi di vertici:
- **$S$**: vertici con stima corretta della distanza da $S$
- **$Q$**: vertici rimanenti, da processare

Ad ogni iterazione:
1. Estrarre da $Q$ il vertice $u$ con distanza minima $d[u]$
2. Aggiungere $u$ a $S$ (la sua stima è ormai corretta)
3. **Rilassare** gli archi uscenti da $u$: se $d[v] > d[u] + w(u,v)$, aggiornare $d[v]$

> [!info] Operazione di rilassamento
> ```
> relax(u, v, w):
>     if d[v] > d[u] + w(u, v):
>         d[v] ← d[u] + w(u, v)
>         parent[v] ← u
> ```

---

## 2. Il collo di bottiglia: ricerca del minimo

### Implementazione naïve: array non ordinato

```
Q = array di vertici, indicizzati da 0 a n-1
for each vertex u in V:
    d[u] ← ∞
d[s] ← 0

while Q not empty:
    u ← extract_min(Q)  // ← BOTTLENECK: O(n)
    S ← S ∪ {u}
    for each (u, v) in E[u]:
        relax(u, v, w(u,v))
```

> [!warning] Costo computazionale naïve
> - **Extract-min**: $O(n)$ per ogni vertice → $O(n^2)$ totale
> - **Rilassamenti**: $O(m)$ (un per arco)
> - **Totale: $\Theta(n^2 + m)$**
> 
> Per grafi sparsi ($m \approx n$), è **inaccettabile**.

### Il problema: ordine dinamico

Dopo il rilassamento, $d[v]$ cambia e l'ordine di $Q$ non è più valido. Mantenere $Q$ ordinato staticamente costerebbe $O(n \log n)$ all'inizio e $O(n)$ per ogni aggiornamento.

---

## 3. Soluzione: Heap di priorità (Priority Queue)

> [!info] Heap binario di minimo
> Una **heap binaria di minimo** è un albero binario completo in cui ogni nodo padre ha valore minore dei suoi figli. L'invariante è mantenuto da **sift-up** e **sift-down**.

**Operazioni principali e costi:**

| Operazione | Costo | Descrizione |
|---|---|---|
| `extract_min()` | $O(\log n)$ | Estrae la radice (elemento minimo) |
| `insert(x)` | $O(\log n)$ | Inserisce un elemento |
| `decrease_key(node, val)` | $O(\log n)$ | Diminuisce valore e risale se necessario |

**Rappresentazione in array:** per nodo in posizione $i$:
- Figli: posizioni $2i$ e $2i+1$
- Padre: posizione $\lfloor i/2 \rfloor$

### Dijkstra con heap: complessità migliorata

```
build_min_heap(Q)  // O(n)
while Q not empty:
    u ← extract_min(Q)      // O(log n)
    for each (u, v) in E[u]:
        if d[v] > d[u] + w(u, v):
            d[v] ← d[u] + w(u, v)
            decrease_key(Q, v, d[v])  // O(log n)
```

> [!info] Complessità totale con heap
> - **Extract-min**: $n$ volte → $O(n \log n)$
> - **Decrease-key**: al massimo una per ogni rilassamento → $O(m \log n)$
> - **Totale: $O((n + m) \log n)$**
> 
> Per grafi sparsi ($m = O(n)$): $O(n \log n)$ **asintoticamente ottimale** ✓

---

## 4. Array associativi e dualità albero-array

### Problema: indexing arbitrario

Nell'heap con array, gli indici sono $1, 2, \ldots, n$. Ma vogliamo indicizzare per **vertice** (stringa, nome, identificatore arbitrario).

> [!info] Array associativo
> Un **array associativo** (o hash map) è una struttura dati che mappa chiavi arbitrarie a valori, mantenendo accesso $O(1)$ in media.

**Esempi:** Python `dict`, Java `HashMap`, C++ `unordered_map`.

### Implementazione ibrida

Per mantenere $O(\log n)$ per accesso e aggiornamento:

1. **Albero di ricerca** (AVL, RB-tree) con heap ordinato per valore
2. **Array associativo** che mappa vertice → posizione nell'albero

```
position_map[vertex] → posizione_heap
```

> [!example] Algoritmo di aggiornamento
> ```
> search_and_update(vertex, new_value):
>     pos ← position_map[vertex]      // O(1) lookup
>     node ← tree[pos]
>     if new_value < node.value:
>         node.value ← new_value
>         sift_up(node)               // O(log n)
>         update_position_map(...)    // O(1)
> ```

**Invariante:** `position_map` rimane sempre sincronizzato con l'albero.

---

## 5. Esempio: esecuzione di Dijkstra su un grafo piccolo

Grafo con vertici $\{A, B, C\}$:
- $(A, B, 4)$, $(A, C, 2)$, $(B, C, 1)$, $(C, B, 3)$

Sorgente: $A$

> [!example] Esecuzione passo per passo

**Inizializzazione:**
```
d[A] = 0, d[B] = ∞, d[C] = ∞
Q = {A:0, B:∞, C:∞}
S = {}
```

**Iterazione 1:** extract_min(Q) → $(A, 0)$
```
S ← {A}
relax (A, B): d[B] = 0 + 4 = 4
relax (A, C): d[C] = 0 + 2 = 2
Q = {B:4, C:2}
```

**Iterazione 2:** extract_min(Q) → $(C, 2)$
```
S ← {A, C}
relax (C, B): d[B] = min(4, 2+3) = 4
Q = {B:4}
```

**Iterazione 3:** extract_min(Q) → $(B, 4)$
```
S ← {A, B, C}
Q = {}
Risultato: d[A]=0, d[B]=4, d[C]=2 ✓
```

---

## 6. Implementazione dettagliata: decrease_key

```java
void decrease_key(vertex v, double new_distance) {
    Node node = position_map[v];      // O(1)
    if (new_distance < node.distance) {
        node.distance = new_distance;
        sift_up(node);                // O(log n)
    }
}
```

> [!tip] Sift-up: l'algoritmo
> Dopo aver decrementato il valore, risaliamo l'albero finché l'invariante di heap è rispettato:
> ```
> sift_up(node):
>     while node.parent != null and node.distance < node.parent.distance:
>         swap(node, node.parent)
>         node ← node.parent
> ```

---

## 7. Confronto di implementazioni

| Struttura | Extract-min | Decrease-key | Dijkstra | Pratica |
|---|---|---|---|---|
| Array lineare | $O(n)$ | $O(1)$ | $O(n^2)$ | Pessimo per grafi sparsi |
| **Heap binario** | $O(\log n)$ | $O(\log n)$ | $O((n+m)\log n)$ | **Best practice** ✓ |
| Fibonacci heap | $O(1)$ amortized | $O(1)$ amortized | $O(m + n\log n)$ | Troppo complesso |

> [!tip] Regola pratica per l'esame
> **Per quasi tutti i grafi reali, usare heap binario.** La complessità teorica migliore di Fibonacci heap non compensa la complessità d'implementazione.

---

> [!abstract] Riepilogo: Punti Chiave
> 1. **Dijkstra naïve:** $O(n^2)$ — cercare minimo in array lineare è costoso
> 2. **Dijkstra con heap:** $O((n+m)\log n)$ — ottimale con operazione `decrease_key`
> 3. **Array associativi:** mappano chiavi arbitrarie a dati con accesso $O(1)$
> 4. **Dualità albero-array:** position_map sincronizzato con heap per accesso rapido ai nodi
> 5. **`decrease_key`:** diminuisce valore e risale → costo $O(\log n)$

---

> [!question] Domande d'esame frequenti
> - Perché Dijkstra naïve non funziona bene per grafi sparsi?
> - Come funziona l'operazione `decrease_key` in una heap?
> - Qual è il ruolo dell'array associativo (position_map)?
> - Dimostrare che la complessità di Dijkstra con heap è $O((n+m)\log n)$

> [!todo] Esercizi suggeriti
> - [ ] Implementare Dijkstra con heap binaria in C++ o Java
> - [ ] Misurare i tempi di esecuzione su grafi sparsi vs densi
> - [ ] Confrontare con altre strutture dati (Fibonacci heap, alberi bilanciati)

---

#APA #Dijkstra #shortest-path #heap #priority-queue #array-associativi
