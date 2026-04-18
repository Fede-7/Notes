# Lezione Bonus (18): Introduzione alla Teoria dei Grafi

**Data:** 22/05/2025 (come da note)
**Argomenti:** Problema Ponti di Königsberg, Definizione Grafo non orientato, Vertici, Lati, Grado, Teorema Somma Gradi, Vertici Dispari, Grafi Regolari, Grafi Completi, Cammini, Connessione, Componenti Connesse, Alberi, Circuiti Euleriani, Grafo Complementare, Multigrafi.

#tag/theory-of-graphs #tag/eulerian-circuits #tag/trees #tag/graph-connectivity #tag/algebra-avanzata

---

## 1. Il Problema dei Ponti di Königsberg (Eulero, 1736)

*   **Contesto Storico (Pag 1):** La città di Königsberg aveva 7 ponti che collegavano due isole e le sponde del fiume Pregel. Il problema era: è possibile fare una passeggiata attraversando ogni ponte una e una sola volta?
    *   Eulero dimostrò che non era possibile e, nel farlo, pose le basi della teoria dei grafi.
*   **Modellizzazione con Grafo (Pag 1):**
    *   Le aree di terra (A, B, C, D) diventano i **nodi** (o **vertici**) del grafo.
    *   I ponti (1, 2, 3, 4, 5, 6, 7) diventano gli **archi** (o **lati**) che collegano i nodi.
    *   ![Ponti di Königsberg e Grafo Relativo](https://www.ilpost.it/wp-content/uploads/2023/02/27/1677510150-sette-ponti-3.jpg)

---

## 2. Definizioni Fondamentali dei Grafi (Non Orientati)

*   **Relazione Binaria per Grafi Semplici (Pag 2):**
    *   Un grafo semplice può essere visto come una coppia $(V, \mathcal{R})$ dove $V \neq \emptyset$ è l'insieme dei **vertici** e $\mathcal{R}$ è una relazione binaria su $V$ che è:
        1.  **Antiriflessiva:** $\forall v \in V, \neg(v \mathcal{R} v)$ (non ci sono cappi/loop, cioè lati che collegano un vertice a se stesso).
        2.  **Simmetrica:** $\forall v, w \in V, v \mathcal{R} w \implies w \mathcal{R} v$ (se v è collegato a w, allora w è collegato a v; i lati non hanno una direzione).
    *   Il **grafo della relazione** $G \subseteq V \times V$ contiene le coppie $(v, w)$ tali che $v \mathcal{R} w$.
    *   Per un grafo non orientato, se $(v, w) \in G$, allora anche $(w, v) \in G$.

*   **Definizione Formale di Grafo (Non Orientato Semplice) (Pag 3):**
    *   Un **grafo** $G$ è una coppia $(V, L)$ dove:
        *   $V$ è un insieme finito e non vuoto di elementi chiamati **vertici** (o nodi).
        *   $L$ è un insieme di sottoinsiemi di $V$ di cardinalità 2, chiamati **lati** (o archi, spigoli).
            *   Un lato $l \in L$ è della forma $\{v, w\}$ con $v, w \in V$ e $v \neq w$. Questo rappresenta un collegamento non orientato tra $v$ e $w$.
            *   Notazione: $L \subseteq P_2(V)$, dove $P_2(V)$ è l'insieme di tutti i sottoinsiemi di $V$ con esattamente 2 elementi.
            *   Se $|V|=n$, allora $|P_2(V)| = \binom{n}{2} = \frac{n(n-1)}{2}$ (numero massimo di lati in un grafo semplice con $n$ vertici).
    *   **Esempio (Pag 3):** $V=\{a, b, c\}$, $L = \{ \{a, b\}, \{a, c\} \}$.
        *   Questo grafo ha 3 vertici. Il vertice $a$ è collegato a $b$ e a $c$. $b$ e $c$ non sono collegati tra loro.
        
    *   Un **grafo** $G$ è una coppia $(V, L)$ dove:
        *   $V$ è un insieme finito e non vuoto di elementi chiamati **vertici** (o nodi).
        *   $L$ è un insieme di sottoinsiemi di $V$ di cardinalità 2, chiamati **lati** (o archi, spigoli).
            *   Un lato $l \in L$ è della forma $\{v, w\}$ con $v, w \in V$ e $v \neq w$. Questo rappresenta un collegamento non orientato tra $v$ e $w$.
            *   Notazione: $L \subseteq P_2(V)$, dove $P_2(V)$ è l'insieme di tutti i sottoinsiemi di $V$ con esattamente 2 elementi.
            *   Se $|V|=n$, allora $|P_2(V)| = \binom{n}{2} = \frac{n(n-1)}{2}$ (numero massimo di lati in un grafo semplice con $n$ vertici).
	    *   **Esempio (Pag 3):** $V=\{a, b, c\}$, $L = \{ \{a, b\}, \{a, c\} \}$.
        *   Questo grafo ha 3 vertici. Il vertice $a$ è collegato a $b$ e a $c$. $b$ e $c$ non sono collegati tra loro.
        *   ```mermaid
            graph TD;
                a --- b;
                a --- c;
            ```

*   **Grado di un Vertice (Pag 4):**
    *   Il **grado** di un vertice $v \in V$, denotato $d(v)$ (o $\text{deg}(v)$), è il numero di lati incidenti a $v$.
    *   In un grafo semplice, è il numero di vertici adiacenti a $v$.
    *   **Vertice Isolato:** Un vertice $v$ è isolato se $d(v)=0$.
    *   **Esempio (Pag 4):** $V=\{a, b, c, d, e\}$, $L=\{l_1=\{a,b\}, l_2=\{b,c\}, l_3=\{a,d\}, l_4=\{c,d\}, l_5=\{d,e\}\}$.
        *   $d(a)=2$ (lati $l_1, l_3$)
        *   $d(b)=2$ (lati $l_1, l_2$)
        *   $d(c)=2$ (lati $l_2, l_4$)
        *   $d(d)=3$ (lati $l_3, l_4, l_5$)
        *   $d(e)=1$ (lato $l_5$)
        *   Se ci fosse un vertice $f$ non collegato, $d(f)=0$.

*   **Teorema della Somma dei Gradi (Handshaking Lemma) (Pag 4-5):**
    In ogni grafo $G=(V, L)$, la somma dei gradi di tutti i vertici è uguale al doppio del numero dei lati:
    $$ \sum_{v \in V} d(v) = 2 |L| $$
    *   **Idea della Dimostrazione:** Ogni lato $\{u, v\}$ contribuisce con 1 al grado di $u$ e con 1 al grado di $v$. Quindi, sommando i gradi, ogni lato viene contato due volte.

*   **Corollario: Numero di Vertici di Grado Dispari (Pag 5):**
    In ogni grafo finito, il numero di vertici con grado dispari è **pari**.
    *   **Idea della Dimostrazione:** Sia $V_1$ l'insieme dei vertici di grado dispari e $V_2$ quello dei vertici di grado pari.
        *   $\sum_{v \in V} d(v) = \sum_{v \in V_1} d(v) + \sum_{v \in V_2} d(v) = 2|L|$.
        *   $\sum_{v \in V_2} d(v)$ è una somma di numeri pari, quindi è pari.
        *   Poiché $2|L|$ è pari, anche $\sum_{v \in V_1} d(v)$ deve essere pari.
        *   Una somma di numeri dispari è pari se e solo se il numero di termini (dispari) è pari.
        *   Quindi $|V_1|$ (il numero di vertici di grado dispari) deve essere pari.

[[Teoria dei Grafi]] [[Grado (teoria dei grafi)]] [[Lemma della stretta di mano]]

---

## 3. Tipi Speciali di Grafi

*   **Grafo Regolare (Pag 6):** Un grafo $G=(V, L)$ è **k-regolare** (o regolare di grado k) se ogni vertice ha grado $k$: $\forall v \in V, d(v)=k$.
    *   Esempi: Un ciclo $C_n$ ($n \ge 3$) è 2-regolare. Un grafo completo $K_n$ è $(n-1)$-regolare.

*   **Grafo Completo $K_n$ (Pag 6-7):**
    *   Un grafo $G=(V, L)$ con $|V|=n$ vertici è **completo** se ogni coppia di vertici distinti è collegata da un lato.
    *   È $(n-1)$-regolare.
    *   Il numero di lati in $K_n$ è $|L| = \binom{n}{2} = \frac{n(n-1)}{2}$.
    *   $K_1$: un punto. $K_2$: un segmento. $K_3$: un triangolo. $K_4$: un quadrato con le diagonali. $K_5$: un pentagono con tutte le diagonali.

*   **Esercizio (Pag 8):** Esiste un grafo $G=(V,L)$ con $|V|=7$ e $|L|=23$?
    *   Il numero massimo di lati in un grafo semplice con 7 vertici è $\binom{7}{2} = \frac{7 \cdot 6}{2} = 21$.
    *   Poiché $23 > 21$, **NO**, un tale grafo semplice non può esistere. (Potrebbe esistere come multigrafo).

[[Grafo regolare]] [[Grafo completo]]

---

## 4. Cammini e Connessione

*   **Cammino (Path) (Pag 8):** Un **cammino** da un vertice $v$ a un vertice $w$ è una sequenza di lati $\{l_1, l_2, ..., l_t\}$ tale che:
    *   $v$ è un estremo di $l_1$.
    *   $w$ è un estremo di $l_t$.
    *   Per ogni $i=1, ..., t-1$, il lato $l_i$ e il lato $l_{i+1}$ condividono un vertice (sono consecutivi).
    *   Più formalmente, una sequenza di vertici $(v_0, v_1, ..., v_t)$ tale che $v_0=v$, $v_t=w$, e $\{v_{i-1}, v_i\} \in L$ per ogni $i=1, ..., t$.
    *   $t$ è la **lunghezza** del cammino (numero di lati).

*   **Grafo Connesso (Pag 9):** Un grafo $G=(V, L)$ è **connesso** se per ogni coppia di vertici distinti $u, v \in V$, esiste un cammino tra $u$ e $v$.
    *   Se un grafo non è connesso, si divide in più "pezzi" connessi.

*   **Componente Connessa (Pag 9):** Una **componente connessa** di un grafo $G$ è un sottografo connesso massimale. (Massimale significa che non può essere esteso aggiungendo altri vertici/lati del grafo originale mantenendo la connessione).
    *   Un grafo è connesso se e solo se ha una sola componente connessa.
    *   **Esempio (Pag 9):** Un grafo con vertici $\{a,b,c,d,e,f,g,h,i,l,m\}$ può avere componenti connesse come $\{a,b,c,d\}$, $\{e,f,g,h\}$, $\{i,l\}$, $\{m\}$.

[[Cammino (teoria dei grafi)]] [[Grafo connesso]] [[Componente connessa (teoria dei grafi)]]

---

## 5. Alberi

Una classe importante di grafi connessi.

*   **Definizione (Pag 10):** Un grafo connesso $G=(V, L)$ è un **albero** se è **privo di circuiti** (o cicli).
    *   Un **circuito** (o ciclo) è un cammino che inizia e finisce nello stesso vertice, senza ripetere lati (e, in un grafo semplice, senza ripetere vertici intermedi).
*   Una **foresta** è un grafo privo di circuiti (le sue componenti connesse sono alberi).

*   **Teorema (Caratterizzazioni degli Alberi, Pag 16):** Sia $G=(V, L)$ un grafo con $|V|=n$ vertici. Le seguenti affermazioni sono equivalenti:
    1.  $G$ è un albero (connesso e aciclico).
    2.  Per ogni coppia di vertici distinti $a, b \in V$, esiste un **unico** cammino tra $a$ e $b$.
    3.  $G$ è connesso, e se si rimuove un qualsiasi lato $l \in L$, il grafo $G'=(V, L \setminus \{l\})$ non è più connesso. (Minimamente connesso).
    4.  $G$ è privo di circuiti, e se si aggiunge un qualsiasi lato $\{u, v\} \notin L$ (tra vertici $u,v$ esistenti), il grafo $G'=(V, L \cup \{\{u,v\}\})$ contiene un circuito. (Massimamente aciclico).

*   **Teorema (Proprietà degli Alberi, Pag 17):** Sia $G=(V, L)$ un grafo con $|V|=n$ vertici. Le seguenti affermazioni sono equivalenti:
    1.  $G$ è un albero.
    2.  $G$ è privo di circuiti e ha $|L|=n-1$ lati.
    3.  $G$ è connesso e ha $|L|=n-1$ lati.

[[Albero (teoria dei grafi)]] [[Circuito (teoria dei grafi)]]

---

## 6. Cammini e Circuiti Euleriani

Ricollegandoci al problema dei Ponti di Königsberg.

*   **Multigrafo (Pag 13):** Un grafo in cui sono ammessi **lati multipli** tra la stessa coppia di vertici e/o **cappi** (lati che collegano un vertice a se stesso).
    *   Per i multigrafi, la definizione di lato come insieme di 2 vertici non basta. Si introduce una funzione $\varphi: L \to P_{\le 2}(V)$ che associa a ogni lato l'insieme dei suoi estremi.
    *   Il grado di un vertice è il numero di "estremità" di lati che incidono su di esso (un cappio conta 2 per il grado del suo vertice).

*   **Cammino Euleriano:** Un cammino in un (multi)grafo che attraversa **ogni lato esattamente una volta**.
*   **Circuito Euleriano:** Un cammino euleriano che è anche un circuito (inizia e finisce nello stesso vertice).

*   **Teorema di Eulero (Pag 14):** Un multigrafo finito $G$ (privo di vertici isolati) possiede un **circuito euleriano** se e solo se:
    1.  $G$ è **connesso**.
    2.  Tutti i suoi vertici hanno **grado pari**.
*   **Corollario:** Un multigrafo finito $G$ (privo di vertici isolati) possiede un **cammino euleriano** (ma non un circuito) se e solo se:
    1.  $G$ è **connesso**.
    2.  Ha **esattamente due** vertici di grado dispari (questi saranno l'inizio e la fine del cammino).

*   **Ponti di Königsberg (Pag 1):**
    *   Vertice A: grado 5 (dispari)
    *   Vertice B: grado 3 (dispari)
    *   Vertice C: grado 3 (dispari)
    *   Vertice D: grado 3 (dispari)
    *   Ci sono 4 vertici di grado dispari. Quindi non esiste né un circuito euleriano né un cammino euleriano.

[[Cammino euleriano]] [[Teorema di Eulero (teoria dei grafi)]]

---

## 7. Altri Concetti

*   **Teorema (Pag 11):** Sia $G=(V,L)$ un grafo finito con grado minimo dei vertici $d_{min} > 0$. Allora:
    1.  $G$ possiede un cammino di lunghezza almeno $d_{min}$.
    2.  Se $d_{min} \ge 2$, allora $G$ possiede un circuito di lunghezza almeno $d_{min}+1$.

*   **Grafo Complementare (Pag 12):** Dato un grafo semplice $G=(V, L)$, il suo grafo complementare $\bar{G}=(V, \bar{L})$ ha lo stesso insieme di vertici $V$, e un lato $\{u, v\}$ è in $\bar{L}$ se e solo se $\{u, v\}$ non è in $L$.
    *   $L \cap \bar{L} = \emptyset$.
    *   $L \cup \bar{L} = P_2(V)$ (l'insieme di tutti i possibili lati, cioè $K_{|V|}$).

[[Grafo complementare]]

---

> [!SUMMARY] Riepilogo Veloce Lezione Bonus (Grafi)
> *   Il problema dei **Ponti di Königsberg** ha dato origine alla teoria dei grafi.
> *   Abbiamo definito un **grafo semplice non orientato** $(V, L)$ e concetti come **grado**, **somma dei gradi** (pari al doppio dei lati), e il fatto che i **vertici di grado dispari sono in numero pari**.
> *   Abbiamo visto **grafi regolari** e **grafi completi** $K_n$.
> *   Abbiamo definito **cammini**, **connessione** e **componenti connesse**.
> *   Gli **alberi** sono grafi connessi aciclici, con $|L|=|V|-1$.
> *   Un (multi)grafo ha un **circuito euleriano** $\iff$ è connesso e tutti i vertici hanno grado pari.
> *   Abbiamo accennato al **grafo complementare**.

> [!TIP] Prossimi Passi
> *   La teoria dei grafi è vasta! Si potrebbero esplorare grafi orientati, pesati, algoritmi su grafi (ricerca cammini minimi, alberi ricoprenti, flusso massimo), colorazione, isomorfismo tra grafi.
> *   Rifletti su come le proprietà delle relazioni binarie (riflessiva, simmetrica, transitiva) si collegano alla struttura dei grafi.