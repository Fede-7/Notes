---
banner: "[[Banner_n1.jpg]]"
aliases:
---

- Strutture algebriche
- reticoli
- Relazioni D'equivalenza
- Th. Fondamentale aritmetica
- Definizione di Partizione 
-  Th. Fondamentale dellle Partizioni
-   Divisione Euclidea
- Th. di Bezout
-  Algebra di Boole
- coefficiente binomiale
- somma coefficienti binomiali
- Cardinalità partizioni di un'insieme

Buongiorno. In questa sede esporrò i concetti fondamentali dell'algebra richiesti, strutturando la trattazione in modo rigoroso e organico, come previsto per un colloquio d'esame.

### 1. Strutture Algebriche
Una **struttura algebrica** è definita formalmente come una sequenza composta da un insieme non vuoto, detto sostegno o supporto, e da una o più operazioni (siano esse interne o esterne) definite su di esso. Le operazioni interne $n$-arie sono funzioni che associano a $n$ elementi dell'insieme un altro elemento dell'insieme stesso. Esempi classici di strutture includono i **gruppi**, caratterizzati da un'operazione associativa, un elemento neutro e l'esistenza dell'inverso per ogni elemento, e gli **anelli**, che presentano due operazioni binarie (somma e prodotto) legate dalla proprietà distributiva.

### 2. Relazioni d'Equivalenza e Partizioni
Una relazione binaria su un insieme $S$ è detta **relazione d'equivalenza** se soddisfa tre proprietà fondamentali: **riflessività** ($aRa$), **simmetria** (se $aRb$ allora $bRa$) e **transitività** (se $aRb$ e $bRc$ allora $aRc$). Queste relazioni permettono di raggruppare gli elementi in **classi di equivalenza**, dove ogni classe $[a]_R$ contiene tutti gli elementi in relazione con $a$.

Parallelamente, una **partizione** di un insieme $S$ è definita come una famiglia di sottoinsiemi non vuoti di $S$, a due a due disgiunti, la cui unione ricostruisce l'intero insieme $S$. Il **Teorema Fondamentale delle Partizioni** (o delle relazioni d'equivalenza) sancisce una corrispondenza biunivoca tra questi due concetti: ogni relazione d'equivalenza induce una partizione (l'insieme quoziente $S/R$) e, viceversa, ogni partizione definisce una relazione d'equivalenza stabilendo che due elementi sono in relazione se appartengono allo stesso blocco.

### 3. Aritmetica: Divisione Euclidea, Bézout e FTA
Il **Teorema della Divisione Euclidea** afferma che, dati due interi $a$ e $b$ ($b \neq 0$), esistono e sono unici due interi $q$ (quoziente) e $r$ (resto) tali che $a = bq + r$, con il vincolo $0 \le r < |b|$. Da questo pilastro deriva l'**Identità di Bézout**, la quale stabilisce che il massimo comun divisore $d = MCD(a, b)$ può essere espresso come combinazione lineare intera di $a$ e $b$, ovvero esistono $x, y \in \mathbb{Z}$ tali che $ax + by = d$.

Questi strumenti permettono di dimostrare il **Teorema Fondamentale dell'Aritmetica**, il quale asserisce che ogni numero intero diverso da $0, 1, -1$ ammette una scomposizione in fattori primi. Tale decomposizione è **unica**, a meno dell'ordine dei fattori e del segno degli stessi.

### 4. Reticoli e Algebra di Boole
Un **reticolo** può essere definito in due modi equivalenti: come un insieme parzialmente ordinato (POSET) in cui ogni coppia di elementi $\{a, b\}$ possiede un estremo inferiore (infimum o *meet*, $\wedge$) e un estremo superiore (supremum o *join*, $\vee$), oppure come una struttura algebrica che soddisfa le leggi associative, commutative e di assorbimento.

Un'**Algebra di Boole** è un tipo speciale di reticolo che risulta essere sia **distributivo** che **complementato**. In tale struttura, ogni elemento $a$ possiede un unico complemento $a'$ tale che $a \wedge a' = 0$ e $a \vee a' = 1$, dove $0$ e $1$ sono rispettivamente il minimo e il massimo assoluti. L'esempio universale di Algebra di Boole è l'insieme delle parti $(P(S), \cup, \cap, ^c, \emptyset, S)$.

### 5. Calcolo Combinatorio e Cardinalità
Il **coefficiente binomiale** $\binom{n}{k}$ esprime il numero di possibili sottoinsiemi di cardinalità $k$ estraibili da un insieme di $n$ elementi ed è calcolato come $\frac{n!}{k!(n-k)!}$. Una proprietà fondamentale è data dalla **somma dei coefficienti binomiali**: $\sum_{k=0}^{n} \binom{n}{k} = 2^n$.

Infine, per quanto riguarda la **cardinalità**, il numero totale di sottoinsiemi di un insieme di ordine $n$ (ovvero la cardinalità dell'insieme delle parti $|P(S)|$) è esattamente $2^n$. Se invece ci riferiamo alla **cardinalità dell'insieme di tutte le partizioni** di un insieme, essa cresce rapidamente con l'ordine dell'insieme; ad esempio, per un insieme di 3 elementi, esistono esattamente 5 partizioni distinte.