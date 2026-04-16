---
date: 2026-03-10
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 3
tags:
  - MSI
  - probabilità
  - sigma-algebra
  - assiomi
  - Kolmogorov
  - Bayes
  - probabilità-totale
  - probabilità-composta
Professore: Marco Lops
---

# MSI --- Lezione 2: Teoria Assiomatica della Probabilita, Bayes e Variabili Aleatorie
---

>[!question] Argomenti trattati
> - Riepilogo dell'analisi combinatoria ($k$-uple ordinate, non ordinate, con/senza ripetizione, coefficiente binomiale)
> - Riepilogo della definizione frequentistica e delle proprietà derivate (complementare, unione, differenza)
> - Riepilogo della probabilità condizionata e della frequenza condizionale
> - Legge della probabilità composta e legge di Bayes (approccio frequentistico)
> - Legge della probabilità totale (partizioni di $\Omega$)
> - Limiti dell'approccio frequentistico e necessità della teoria formale
> - Algebra e $\sigma$-algebra di eventi: definizione e proprietà di chiusura
> - Spazio di probabilità $(\Omega, \mathcal{E}, P)$ e assiomi di Kolmogorov
> - Derivazione rigorosa delle proprietà della probabilità dagli assiomi
> - Indipendenza stocastica: definizione, proprietà dei complementari, indipendenza di $n$ eventi
> - Indipendenza a coppie vs. indipendenza congiunta: controesempio del bit di parità
> - Esercizio: probabilità con $n$ eventi indipendenti (nessuno, almeno uno, esattamente uno)
> - La probabilità condizionata come legge di probabilità (verifica degli assiomi)
> - Esercizio: bussolotto con dado onesto e dado truccato (applicazione di Bayes)
> - Introduzione alle variabili aleatorie discrete e alla PMF
> - Cenno al valore atteso

---
## Richiami :
### Analisi Combinatoria

Sotto l'ipotesi di equiprobabilità degli eventi elementari, la probabilità di un evento si determina come rapporto tra la cardinalità dell'evento e quella dello spazio campionario. Il problema si riduce dunque all'**enumerazione** degli elementi tramite gli strumenti dell'analisi combinatoria. Dato un insieme di $n$ elementi, si definiscono:

- **$k$-uple ordinate con ripetizione**: $n^k$.
- **$k$-uple ordinate di elementi distinti** (**disposizioni semplici**): $D_{n,k} = \frac{n!}{(n-k)!}$.
- **$k$-uple non ordinate** (**combinazioni semplici**): $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.

Il **coefficiente binomiale** $\binom{n}{k}$ esprime non solo il numero di sottoinsiemi di dimensione $k$, ma anche il numero di **sequenze binarie** di lunghezza $n$ contenenti esattamente $k$ uni, interpretazione fondamentale per la modellazione di processi a prove ripetute.

### Proprietà Derivate dalla Definizione Frequentistica

Assumendo la probabilità come limite della frequenza relativa di successo, $P(A) = \lim_{n \to \infty} $N_A$/n$, è possibile derivare le proprietà fondamentali del calcolo probabilistico trattandolo come una **misura** (analoga all'area geometrica) definita sugli insiemi:

1. **Evento complementare**: Poiché su $n$ prove il numero di insuccessi è $n - N_A$, si ha $P($A^c$) = 1 - P(A)$.
2. **Unione (Subadditività)**: Per due eventi $A, B$, il conteggio degli esiti favorevoli all'unione deve escludere la doppia computazione dell'intersezione:
   $$P(A \cup B) = P(A) + P(B) - P(A \cap B) \tag{2.1}$$
   Nel caso di **eventi incompatibili** ($A \cap B = \emptyset$), la (2.1) si riduce alla somma delle probabilità.
3. **Differenza**: La probabilità dell'evento $A \setminus B$ (esiti in $A$ che non appartengono a $B$) è pari a $P(A) - P(A \cap B)$.

### Probabilità Condizionata e Teorema di Bayes

La **frequenza condizionale** $f_n(A \mid B)$ modella il restringimento dello spazio dei campioni ai soli esiti che soddisfano la condizione $B$. Nell'ambito di questo "nuovo universo", si valuta la quota di esiti che soddisfano simultaneamente $A$.

> [!abstract] Definizione: Probabilità condizionata e Legge Composta
> Dato $P(B) > 0$, la probabilità condizionata è:
> $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$
> Da cui si deriva la **legge della probabilità composta**:
> $$P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B) \tag{2.2}$$
Dalla (2.2), sfruttando la commutatività dell'intersezione, si ricava la **Legge di Bayes**, strumento cardine dell'inferenza statistica che permette di invertire la direzione del condizionamento:

> [!abstract] Legge di Bayes
> $$P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$$
Questa formulazione consente di aggiornare la conoscenza *a priori* di un fenomeno ($P(B)$) alla luce di nuove evidenze sperimentali ($A$), determinando la probabilità *a posteriori* ($P(B \mid A)$).

---
## Legge della Probabilità Totale

> [!abstract] Definizione: Partizione
> Si definisce **partizione** di $\Omega$ una collezione di $m$ sottoinsiemi $\{E_1, E_2, \ldots, E_m\}$ tali che:
> 1. siano a due a due disgiunti: $E_i \cap E_j = \emptyset$ per $i \neq j$;
> 2. la loro unione sia l'intero spazio: $\bigcup_{i=1}^{m} E_i = \Omega$.

> [!example] Esempio concreto: i lastroni dell'aula
> I lastroni sul pavimento di un'aula sono una partizione della stanza: la loro unione copre tutta la stanza e due lastroni diversi non si sovrappongono (hanno intersezione nulla).

>**Derivazione.** Dato un qualunque evento $A$:

$$A = A \cap \Omega = A \cap \left(\bigcup_{i=1}^{m} E_i\right) = \bigcup_{i=1}^{m} (A \cap E_i)$$

dove si e usata la proprietà distributiva dell'intersezione rispetto all'unione. Gli insiemi $A \cap E_i$ e $A \cap E_j$ (con $i \neq j$) sono **disgiunti**: $A \cap E_i$ contiene tutti e soli gli elementi che appartengono sia ad $A$ che ad $E_i$, mentre $A \cap E_j$ contiene quelli che appartengono sia ad $A$ che ad $E_j$; ma $E_i$ e $E_j$ non hanno elementi comuni perchè formano una partizione. Quindi:

$$P(A) = \sum_{i=1}^{m} P(A \cap E_i)$$

Usando la definizione di probabilità condizionata, $P(A \cap E_i) = P(A \mid E_i) \cdot P(E_i)$:

> [!abstract] Definizione: Legge della probabilità totale
> $$P(A) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)$$
> La probabilità di un evento $A$ si puo scomporre condizionando rispetto a una partizione dello spazio dei campioni.

> [!tip] Parole del Professore
> > [!tip]
> > "Questa legge, ragazzi, e importantissima. Si usa in tutti i calcoli probabilistici, in quasi tutti, perche a volte devo calcolare la probabilità di un evento ed e difficile, pero se mi metto in certe condizioni la devo scomporre in calcoli piu semplici. La useremo, la vedremo, ve la farò vedere negli esercizi."

---

## Limiti dell'Approccio Frequentistico

Tutte le proprietà ricavate finora --- *complementare, unione, differenza, probabilità condizionata, legge di Bayes, legge della probabilità totale* --- derivano dalla definizione frequentistica (limite della frequenza di successo) e sono conseguenze delle proprietà delle operazioni tra insiemi.

Tuttavia questa impostazione presenta due problemi fondamentali:

1. **Convergenza non specificata:** non si e detto in che senso la frequenza di successo converge a un valore stabile; le prove devono essere indipendenti, ma l'indipendenza e essa stessa un concetto probabilistico (circolarità).
2. **Generalità non garantita:** non c'e a priori nessuna garanzia che le proprietà trovate sotto certe ipotesi valgano in generale.

> [!tip] Parole del Professore
> > [!tip]
> > "Io vi ho promesso che vi avrei definito in modo piu rigoroso la probabilità. Tutto questo zoppica dal punto di vista non solo matematico, ma concettuale."

---

## Teoria Formale: Algebra di Eventi

### Algebra

Dato uno spazio dei campioni $\Omega$, consideriamo una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$.

> [!abstract] Definizione: Algebra
> Una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$ si chiama **algebra** se soddisfa due proprietà:
> 1. **Chiusura rispetto all'unione:** se $A_i \in \mathcal{E}$ e $A_j \in \mathcal{E}$, allora $A_i \cup A_j \in \mathcal{E}$;
> 2. **Chiusura rispetto alla complementazione:** se $A_i \in \mathcal{E}$, allora $A_i^c \in \mathcal{E}$.

#### Chiusura rispetto all'intersezione (dimostrazione via De Morgan)

Il professore chiede alla classe se l'algebra contiene anche l'intersezione di due suoi elementi, e guida la dimostrazione usando le **leggi di De Morgan**.

La legge di De Morgan afferma:

$$(A \cup B)^c = A^c \cap B^c$$

Complementando entrambi i membri:

$$A \cap B = (A^c \cup B^c)^c$$

Allora, se $A \in \mathcal{E}$ e $B \in \mathcal{E}$:

1. $A^c \in \mathcal{E}$ e $B^c \in \mathcal{E}$ (chiusura per complementazione);
2. $A^c \cup B^c \in \mathcal{E}$ (chiusura per unione);
3. $(A^c \cup B^c)^c \in \mathcal{E}$ (chiusura per complementazione).

Quindi $A \cap B \in \mathcal{E}$. L'algebra e **chiusa anche rispetto all'intersezione**.

#### Chiusura rispetto alla differenza

Analogamente, $A \setminus B = A \cap B^c$: poiche $B^c \in \mathcal{E}$ (chiusura per complementazione) e l'intersezione e chiusa, si ha $A \setminus B \in \mathcal{E}$.

> [!warning] Tutte le operazioni insiemistiche restano nell'algebra
> Unione, intersezione, complementazione e differenza di elementi dell'algebra producono sempre elementi dell'algebra. Questo garantisce che la funzione di probabilità possa essere calcolata su qualunque combinazione di eventi: si resta sempre nel dominio di definizione.

### Esercizio: La piu piccola algebra contenente un evento

> [!example] Esempio: dado e evento "risultato pari"
> Sia $\Omega = \{1,2,3,4,5,6\}$ e $A = \{2,4,6\}$ l'evento "risultato pari". La piu piccola algebra che contiene $A$ e:
> $$\mathcal{E}_{\min} = \{\emptyset,\; \Omega,\; A,\; A^c\}$$
> Costruzione passo per passo:
> - se c'e $A$, ci deve essere il suo complemento $A^c = \{1,3,5\}$;
> - se ci sono $A$ e $A^c$, la loro unione $A \cup A^c = \Omega$ deve appartenere;
> - se c'e $\Omega$, il suo complemento $\emptyset$ deve appartenere.
>
> L'insieme delle parti $2^\Omega$ e anch'esso un'algebra, ma e molto piu grande del necessario. Piu piccola di questi quattro elementi non e possibile.

> [!tip] Parole del Professore
> > [!tip]
> > "Non vi fate mai spaventare dai paroloni della matematica."

---

## $\sigma$-Algebra

> [!abstract] Definizione: $\sigma$-algebra
> Un'algebra $\mathcal{E}$ si chiama **$\sigma$-algebra** se un'**unione numerabile** di suoi elementi e ancora un elemento dell'algebra:
> $$A_1, A_2, A_3, \ldots \in \mathcal{E} \quad \Longrightarrow \quad \bigcup_{i=1}^{\infty} A_i \in \mathcal{E}$$

> [!warning] Algebra vs. $\sigma$-algebra
> Un'algebra garantisce la chiusura per unioni **finite**. Una $\sigma$-algebra estende questa garanzia a unioni **numerabili** (infinite ma contabili). La distinzione e rilevante quando lo spazio dei campioni e numerabile.

> [!example] Perche serve la $\sigma$-algebra
> Siamo sull'autostrada e contiamo le macchine. Gli eventi elementari sono "non passa nessuna macchina", "passa una macchina", "passano due macchine", eccetera, fino potenzialmente a infinito. Per ogni insieme di questi eventi devo poter fare l'unione, anche all'infinito. Se $\Omega$ e finito, la $\sigma$-algebra non aggiunge nulla rispetto all'algebra, perche le unioni finite sono gia sufficienti; la $\sigma$-algebra diventa necessaria quando $\Omega$ e numerabile.

---

## Spazio di Probabilità e Assiomi di Kolmogorov

A questo punto si dispone di uno spazio dei campioni $\Omega$ e di una $\sigma$-algebra $\mathcal{E}$ dei sottoinsiemi di $\Omega$.

> [!abstract] Definizione: Legge di probabilità (Kolmogorov)
> Dato uno spazio dei campioni $\Omega$ e una $\sigma$-algebra $\mathcal{E}$, si definisce **legge di probabilità** una funzione
> $$P : \mathcal{E} \to [0,1]$$
> che soddisfa i seguenti **assiomi di Kolmogorov** ("tre assiomi e mezzo"):
>
> - **Assioma 1 --- Non negatività:**
> $$P(A) \geq 0 \quad \forall\, A \in \mathcal{E}$$
>
> - **Assioma 2 --- Normalizzazione:**
> $$P(\Omega) = 1$$
>
> - **Assioma 3 --- Additività (o subadditività):**
> Se $A$ e $B$ sono eventi disgiunti ($A \cap B = \emptyset$):
> $$P(A \cup B) = P(A) + P(B)$$
>
> - **Assioma 3$\frac{1}{2}$ --- $\sigma$-additività (estensione numerabile):**
> Se $\{A_i\}_{i=1}^{\infty}$ e una successione di eventi a due a due disgiunti:
> $$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

La terna $(\Omega, \mathcal{E}, P)$ prende il nome di **spazio di probabilità**.

> [!warning] Perche la struttura della $\sigma$-algebra è necessaria
> La $\sigma$-algebra garantisce che tutte le operazioni insiemistiche (unione, intersezione, complementazione, differenza) restino nel dominio di definizione della funzione $P$. Senza questa struttura, non si potrebbe essere certi di poter calcolare $P$ su combinazioni arbitrarie di eventi. 
> Come dice il professore: "i matematici pensano: io resto nel dominio di definizione dell'algebra."

> [!tip] Parole del Professore
> > [!tip]
> > "Vedete che noi abbiamo fatto tutto questo ambaradan. Dice, ma e tutta questa cosa complicata? Tu metti le tue prove, fatti la frequenza di successo... Tutto quello che abbiamo ricavato, qua non c'e niente. Io ti faccio vedere che tutto quello che tu hai ricavato prima, usando quella definizione, se volete, un po' farlocca di probabilità, io te lo ricavo come unica conseguenza degli assiomi di Kolmogorov."

---

## Derivazione delle Proprietà dagli Assiomi

Il professore mostra come le proprietà ricavate in modo "facile" dalla definizione frequentistica si dimostrino ora rigorosamente a partire dai **soli** assiomi di Kolmogorov.

### Probabilità di $A \setminus \space B$

Si parte dall'identità insiemistica:

$$A = A \cap \Omega = A \cap (B \cup B^c) = (A \cap B) \cup (A \cap B^c)$$

dove si e usata la proprietà distributiva dell'intersezione rispetto all'unione. Ora si osserva che:

- $(A \cap B)$ contiene tutti e soli gli elementi che appartengono sia ad $A$ che a $B$;
- $(A \cap B^c)$ contiene tutti e soli gli elementi che appartengono ad $A$ ma **non** a $B$.

Questi due insiemi sono **disgiunti**. Per l'assioma 3 ($\sigma$-additività):

$$P(A) = P(A \cap B) + P(A \cap B^c)$$

Ma $A \cap B^c = A \setminus B$, quindi:

$$\boxed{P(A \setminus B) = P(A) - P(A \cap B)}$$

> [!tip] Osservazione
> E la stessa formula trovata prima con la definizione frequentistica, ma ora e dimostrata rigorosamente a partire dagli assiomi.

### Probabilità di $A \cup B$

Si scrive:

$$A \cup B = A \cup (B \cap A^c)$$

dove $A$ e $B \cap A^c$ (gli elementi di $B$ che non appartengono ad $A$) sono **disgiunti**. Quindi per l'assioma 3:

$$P(A \cup B) = P(A) + P(B \cap A^c)$$

Ma dalla proprietà appena dimostrata, $P(B \cap A^c) = P(B \setminus A) = P(B) - P(A \cap B)$ (si invertono i ruoli di $A$ e $B$ nella formula precedente):

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

### Probabilità dell'evento complementare

L'evento $A$ e il suo complementare $A^c$ soddisfano $A \cup A^c = \Omega$ e sono incompatibili ($A \cap A^c = \emptyset$). Per l'assioma 3 (additività) e l'assioma 2 (normalizzazione):

$$P(A) + P(A^c) = P(A \cup A^c) = P(\Omega) = 1$$

$$\boxed{P(A^c) = 1 - P(A)}$$

### Probabilità dell'evento impossibile

L'insieme vuoto $\emptyset$ e il complemento di $\Omega$:

$$P(\emptyset) = P(\Omega^c) = 1 - P(\Omega) = 1 - 1 = 0$$

> [!warning] Terminologia
> L'insieme vuoto $\emptyset$ si chiama **evento impossibile**; lo spazio dei campioni $\Omega$ si chiama **evento certo**.

> [!tip] Parole del Professore
> > [!tip]
> > "Riprendo il giro per dirvi quanto e pesante questo. Abbiamo trovato le cose prima, le abbiamo trovate in modo facile. Ora dimostrarle diventa un giochino, perche gia sappiamo il risultato che dobbiamo tirare."

---

## Indipendenza Stocastica

> [!abstract] Definizione: Indipendenza stocastica
> Due eventi $A, B \in \mathcal{E}$ si dicono **statisticamente indipendenti** se:
> $$P(A \cap B) = P(A) \cdot P(B)$$

> [!tip] Parole del Professore
> > [!tip]
> > "La nozione di indipendenza e fondamentale e moltissima statistica inferenziale si fonda su ipotesi di indipendenza, perche senza indipendenza una serie di convergenze [non valgono]. Voi avete dei grandi database, giocate quei file Excel per ricavarvi una serie di parametri globali. E ci sono delle ipotesi alla base: ipotesi di ergodicità, che a loro volta indicano ipotesi di indipendenza, per lo meno tra campioni sufficientemente lontani. Se no, la statistica descrittiva vale solo per quel campione di dati. Non e generalizzabile."

### Indipendenza dei complementari

**Teorema:** Se $A$ e $B$ sono statisticamente indipendenti, allora anche $A^c$ e $B^c$ sono statisticamente indipendenti.

**Dimostrazione.** Per le leggi di De Morgan:

$$A^c \cap B^c = (A \cup B)^c$$

Quindi:

$$P(A^c \cap B^c) = P\big((A \cup B)^c\big) = 1 - P(A \cup B)$$

Sostituendo la formula dell'unione:

$$= 1 - P(A) - P(B) + P(A \cap B)$$

Poiche $A$ e $B$ sono indipendenti, $P(A \cap B) = P(A) \cdot P(B)$:

$$= 1 - P(A) - P(B) + P(A) \cdot P(B)$$

Raccogliendo:

$$= 1 - P(A) - P(B)\big(1 - P(A)\big) = \big(1 - P(A)\big)\big(1 - P(B)\big) = P(A^c) \cdot P(B^c)$$

$$\boxed{P(A^c \cap B^c) = P(A^c) \cdot P(B^c) \quad \checkmark}$$

### Indipendenza di $n$ eventi

> [!abstract] Definizione: Indipendenza di $n$ eventi
> Tre eventi $A$, $B$ e $C$ si dicono **indipendenti** se lo sono **a 2 a 2** e **a 3 a 3**:
> $$P(A \cap B) = P(A) \cdot P(B), \quad P(A \cap C) = P(A) \cdot P(C), \quad P(B \cap C) = P(B) \cdot P(C)$$
> $$P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$$
>
> In generale, una $n$-upla di eventi $A_1, A_2, \ldots, A_n$ e una **$n$-upla indipendente** se per ogni sottoinsieme $\{i_1, i_2, \ldots, i_k\} \subseteq \{1, \ldots, n\}$:
> $$P(A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}) = P(A_{i_1}) \cdot P(A_{i_2}) \cdots P(A_{i_k})$$
>
> L'indipendenza di ordine $n$ implica quella di ordine inferiore (da $n-1$ fino a $2$), **ma non vale il viceversa**.

> [!warning] Indipendenza a coppie $\not\Rightarrow$ indipendenza congiunta
> L'indipendenza a coppie **non** implica l'indipendenza della terna (o della $n$-upla). Un controesempio classico e il **bit di parità**.

#### Controesempio: il bit di parità

> [!example] Il bit di parità
> Siano $X_1$ e $X_2$ due bit equiprobabili e indipendenti, ciascuno con valore $0$ o $1$ con probabilità $\frac{1}{2}$. Si definisce il **bit di parità**:
> $$X_3 = X_1 \oplus X_2$$
> dove $\oplus$ denota la **somma modulo 2** (operazione XOR): $X_3 = 0$ se $X_1$ e $X_2$ sono uguali, $X_3 = 1$ se sono diversi, in modo che il numero di uni nella terna $(X_1, X_2, X_3)$ sia sempre pari.
>
> **Risultato:**
> - $X_1$ e $X_2$ sono **indipendenti** (per ipotesi);
> - $X_1$ e $X_3$ sono **indipendenti**;
> - $X_2$ e $X_3$ sono **indipendenti**;
> - ma la terna $(X_1, X_2, X_3)$ **non** e indipendente.
>
> **Perche?** Se si conoscono sia $X_1$ che $X_2$, il valore di $X_3$ e **completamente determinato** ($X_3 = X_1 \oplus X_2$). La probabilità non si puo fattorizzare: $P(X_1 = x_1, X_2 = x_2, X_3 = x_3) \neq P(X_1 = x_1) \cdot P(X_2 = x_2) \cdot P(X_3 = x_3)$. Ma se si conosce **uno solo** dei due bit, non si puo dedurre nulla sul terzo.

---

## Esercizio: $n$ Eventi Indipendenti

Siano $A_1, A_2, \ldots, A_n$ eventi indipendenti, con $P(A_i) = p_i$. Si calcolino:

### 1. Probabilità che non se ne verifichi nessuno

L'evento "non si verifica nessuno" equivale a: non si verifica $A_1$, **e** non si verifica $A_2$, **e** ... **e** non si verifica $A_n$, cioe $A_1^c \cap A_2^c \cap \cdots \cap A_n^c$.

Poiche gli $A_i$ sono indipendenti, abbiamo dimostrato che anche i loro complementari sono indipendenti. Quindi la probabilità dell'intersezione e il prodotto:

$$\boxed{P\!\left(\bigcap_{i=1}^{n} A_i^c\right) = \prod_{i=1}^{n} (1 - p_i)}$$

### 2. Probabilità che se ne verifichi almeno uno

L'evento "almeno uno" e il **complementare** dell'evento "nessuno": se ne verifica almeno uno se non e vero che non se ne verifica nessuno.

$$\boxed{P\!\left(\bigcup_{i=1}^{n} A_i\right) = 1 - \prod_{i=1}^{n} (1 - p_i)}$$

### 3. Probabilità che se ne verifichi esattamente uno (non importa quale)

L'evento "esattamente uno" si traduce come: **o** si verifica $A_1$ ma non $A_2, A_3, \ldots, A_n$; **oppure** non si verifica $A_1$ ma si verifica $A_2$ e non $A_3, \ldots, A_n$; **oppure** ... **oppure** non si verificano $A_1, \ldots, A_{n-1}$ ma si verifica $A_n$.

Formalmente:

$$(A_1 \cap A_2^c \cap \cdots \cap A_n^c) \;\cup\; (A_1^c \cap A_2 \cap A_3^c \cap \cdots \cap A_n^c) \;\cup\; \cdots \;\cup\; (A_1^c \cap \cdots \cap A_{n-1}^c \cap A_n)$$

Questi $n$ eventi sono **disgiunti** (nel primo c'e $A_1$, nel secondo c'e $A_2$ ma non $A_1$, ecc.), quindi per la $\sigma$-additività e l'indipendenza:

$$\boxed{P(\text{esattamente uno}) = \sum_{i=1}^{n} p_i \prod_{\substack{j=1 \\ j \neq i}}^{n} (1 - p_j)}$$

> [!tip] Parole del Professore
> > [!tip]
> > "E solo logica, ragazzi, pero vi dico anche che questa logica non la dovete dimenticare, perche poi quando andiamo sulle variabili aleatorie e un po' piu numerica la cosa, pero dovete sempre ricordarvi questa logica. Dovete formulare opportunamente le proposizioni."

---

## La Probabilità Condizionata come Legge di Probabilità

Un risultato importante: **fissato $B$ con $P(B) > 0$**, la funzione $P(\cdot \mid B)$ soddisfa gli assiomi di Kolmogorov ed e quindi una legge di probabilità a tutti gli effetti.

**Verifica dei tre assiomi:**

**Assioma 1 (Non negatività):** $P(A \mid B) = \frac{P(A \cap B)}{P(B)} \geq 0$, poiche rapporto di due quantità non negative.

**Assioma 2 (Normalizzazione):**

$$P(\Omega \mid B) = \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1 \quad \checkmark$$

**Assioma 3 ($\sigma$-additività):** Siano $A$ e $C$ eventi disgiunti ($A \cap C = \emptyset$):

$$P(A \cup C \mid B) = \frac{P\big((A \cup C) \cap B\big)}{P(B)} = \frac{P\big((A \cap B) \cup (C \cap B)\big)}{P(B)}$$

Ma se $A \cap C = \emptyset$, allora $(A \cap B)$ e $(C \cap B)$ sono disgiunti: $A \cap B$ contiene tutti e soli gli elementi che appartengono a $B$ e ad $A$, $C \cap B$ contiene quelli che appartengono a $B$ e a $C$, ma $A$ e $C$ non hanno elementi comuni. Quindi:

$$= \frac{P(A \cap B) + P(C \cap B)}{P(B)} = \frac{P(A \cap B)}{P(B)} + \frac{P(C \cap B)}{P(B)} = P(A \mid B) + P(C \mid B) \quad \checkmark$$

Dunque $P(\cdot \mid B)$ e una legge di probabilità.

### Conseguenza per l'indipendenza

Se $A$ e $B$ sono indipendenti:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A) \cdot P(B)}{P(B)} = P(A)$$

Il verificarsi di $B$ **non influisce minimamente** sulla probabilità di $A$: la probabilità condizionata coincide con quella incondizionata.

> [!example] Piove a Napoli, Portici e Kathmandu
> Sia $A$ = "piove a Napoli", $B$ = "piove a Portici", $C$ = "piove a Kathmandu".
> - $P(A \mid B) \neq P(A)$: se piove a Portici, e piu probabile che piova anche a Napoli (eventi **dipendenti**).
> - $P(A \mid C) \approx P(A)$: sapere che piove a Kathmandu non da informazione utile sulla pioggia a Napoli (eventi approssimativamente **indipendenti**).
>
> La probabilità a priori $P(A)$ si calcola guardando i record storici: quante volte ha piovuto a Napoli il 10 marzo, diviso il numero totale di anni registrati.

> [!warning] Spazio di probabilità e modellazione
> Tutti gli spazi di probabilità sono **matematicamente equivalenti**. Per il lancio di una moneta:
> - $P(\text{testa}) = 1, \; P(\text{croce}) = 0$ e legittimo (moneta con due teste);
> - $P(\text{testa}) = P(\text{croce}) = \frac{1}{2}$ e legittimo (moneta onesta).
>
> La scelta della legge di probabilità non e un problema matematico ma di **modellazione**: bisogna scegliere la legge che meglio descrive l'esperimento reale. Se si sbaglia la legge, non si sbaglia matematicamente, ma le predizioni non aderiscono alla realtà. Questo e il compito dell'**inferenza statistica**.

---

## Esercizio: Bussolotto con Dado Onesto e Dado Truccato

> [!example] Enunciato
> Un bussolotto contiene due dadi indistinguibili per colore e peso. Un dado e **onesto**, l'altro e **truccato** in modo che il $6$ esca con probabilità $\frac{1}{2}$ e tutti gli altri risultati siano equiprobabili. Si estrae un dado e lo si lancia **due volte**, ottenendo la coppia $(5, 5)$. Qual e la probabilità che il dado estratto sia quello truccato?

### Modellazione del dado truccato

Per il **dado onesto** $D_O$, tutti i risultati sono equiprobabili:

$$P(X = i \mid D_O) = \frac{1}{6}, \quad i = 1, 2, \ldots, 6$$

Per il **dado truccato** $D_T$, la probabilità che esca $6$ e $\frac{1}{2}$ e gli altri risultati sono equiprobabili tra loro. Per trovare queste probabilità, si impone l'**assioma di normalizzazione** (la somma di tutte le probabilità deve valere $1$):

$$P(\Omega) = P(X = 6) + \sum_{i=1}^{5} P(X = i) = \frac{1}{2} + 5p = 1 \quad \Longrightarrow \quad p = \frac{1}{10}$$

Quindi:

$$P(X = i \mid D_T) = \begin{cases} \dfrac{1}{2} & \text{se } i = 6 \\[6pt] \dfrac{1}{10} & \text{se } i \neq 6 \end{cases}$$

### Impostazione con Bayes

Sia $A$ = "il dado estratto e truccato" e $B$ = "i due lanci danno $(5,5)$". Si vuole calcolare $P(A \mid B)$.

Per la **legge di Bayes**:

$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

### Calcolo di $P(B \mid A)$: probabilità di $(5,5)$ con il dado truccato

Dato che si e estratto il dado truccato, i due lanci sono **condizionalmente indipendenti** (lo stesso dado viene lanciato due volte):

$$P(5,5 \mid D_T) = \frac{1}{10} \cdot \frac{1}{10} = \frac{1}{100}$$

### Calcolo di $P(B \mid D_O)$: probabilità di $(5,5)$ con il dado onesto

$$P(5,5 \mid D_O) = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$$

### Probabilità a priori

I dadi sono indistinguibili, quindi si estraggono con uguale probabilità:

$$P(D_T) = P(D_O) = \frac{1}{2}$$

### Calcolo di $P(B)$ con la legge della probabilità totale

La partizione e $\{D_O, D_T\}$ (i due eventi sono mutuamente esclusivi):

$$P(B) = P(5,5 \mid D_O) \cdot P(D_O) + P(5,5 \mid D_T) \cdot P(D_T) = \frac{1}{36} \cdot \frac{1}{2} + \frac{1}{100} \cdot \frac{1}{2}$$

$$= \frac{1}{2}\left(\frac{1}{36} + \frac{1}{100}\right) = \frac{1}{2} \cdot \frac{100 + 36}{3600} = \frac{136}{7200} = \frac{17}{900}$$

### Risultato

$$\boxed{P(D_T \mid 5,5) = \frac{\frac{1}{100} \cdot \frac{1}{2}}{\frac{17}{900}} = \frac{\frac{1}{200}}{\frac{17}{900}} = \frac{900}{200 \cdot 17} = \frac{9}{34} \approx 0{,}265}$$

> [!tip] Interpretazione
> La probabilità a posteriori che il dado sia truccato ($\approx 26{,}5\%$) e **minore** della probabilità a priori ($50\%$). Questo ha senso: il $5$ esce piu facilmente con il dado onesto ($\frac{1}{6} \approx 16{,}7\%$) che con il truccato ($\frac{1}{10} = 10\%$), quindi osservare due $5$ rende piu probabile che il dado sia quello onesto. Se fossero usciti due $6$, il risultato sarebbe stato opposto.

### Variante: reinserimento del dado

Il professore discute una variante proposta da uno studente: dopo il primo lancio si **rimette il dado nel bussolotto**, si mescola e si estrae nuovamente.

In questo caso i due lanci diventano **incondizionalmente indipendenti** (non solo condizionalmente), perche si ripristinano esattamente le stesse condizioni iniziali. La probabilità di ottenere $5$ in un singolo lancio si calcola con la legge della probabilità totale:

$$P(X = 5) = P(5 \mid D_T) \cdot P(D_T) + P(5 \mid D_O) \cdot P(D_O) = \frac{1}{10} \cdot \frac{1}{2} + \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{2}\left(\frac{1}{10} + \frac{1}{6}\right) = \frac{1}{2} \cdot \frac{4}{15} = \frac{2}{15}$$

E la probabilità della coppia $(5,5)$ e semplicemente il **quadrato**:

$$P(5,5) = \left(\frac{2}{15}\right)^2 = \frac{4}{225}$$

> [!warning] Indipendenza condizionale vs. incondizionale
> - **Stesso dado, due lanci:** i lanci sono **condizionalmente indipendenti** dato il tipo di dado ($D_T$ o $D_O$), ma **non** incondizionalmente indipendenti. Si puo scrivere $P(5,5 \mid D_T) = P(5 \mid D_T)^2$, ma $P(5,5) \neq P(5)^2$.
> - **Reinserimento del dado:** ogni lancio e un esperimento completamente ripristinato, quindi i lanci sono **incondizionalmente indipendenti** e $P(5,5) = P(5)^2$.

---

## Introduzione alle Variabili Aleatorie

### Motivazione: tre esperimenti, un unico trattamento

Il professore introduce le variabili aleatorie partendo da un'osservazione pratica. Tre esperimenti apparentemente diversi:

1. **Lancio di una moneta:** testa o croce;
2. **Sorgente binaria:** emette $0$ o $1$;
3. **Lancio di un dado:** risultato pari o dispari.

hanno tutti un esito **binario**. Codificando opportunamente (testa $\to 0$, croce $\to 1$; pari $\to 0$, dispari $\to 1$), si possono trattare in modo **unificato** attraverso un'applicazione che associa ad ogni esito dello spazio campione un valore numerico.

> [!abstract] Definizione: Variabile aleatoria (caso discreto)
> Dato uno spazio di probabilità $(\Omega, \mathcal{E}, P)$ discreto, una **variabile aleatoria** e un'applicazione
> $$X : \Omega \to \mathcal{X}$$
> dove $\mathcal{X}$ e un insieme numerico chiamato **alfabeto** della variabile aleatoria. La funzione $X$ associa ad ogni esito $\omega \in \Omega$ un valore numerico $X(\omega) \in \mathcal{X}$.

> [!tip] Perche le variabili aleatorie sono utili
> Consentono di trattare in modo unificato esperimenti diversi che hanno la stessa struttura probabilistica. Ogni insieme discreto non numerico si puo sempre descrivere attraverso un insieme di numeri interi (ad esempio, puntatori a locazioni di memoria dove sono memorizzate le etichette). Quindi, quando lo spazio dei campioni e discreto, si possono indicizzare gli eventi elementari e la variabile aleatoria diventa semplicemente l'indice che denota quell'evento elementare.

> [!example] Stringhe binarie di lunghezza $k$
> Le stringhe binarie di lunghezza $k$ sono $2^k$. Ciascuna stringa puo essere memorizzata in una locazione di memoria; la variabile aleatoria assume il valore $i$ dove $i$ e il puntatore alla locazione della $i$-esima configurazione. Si ottiene cosi una variabile aleatoria che assume $2^k$ possibili valori.

### Cenno alla misurabilità

Il professore accenna al fatto che, per essere rigorosi, una variabile aleatoria deve essere un'**applicazione misurabile**: l'anti-immagine di ogni evento concernente $X$ deve essere un elemento della $\sigma$-algebra. Questa condizione garantisce che si possa calcolare la probabilità che $X$ assuma certi valori. Tuttavia, per il livello del corso, e sufficiente la definizione semplificata.

> [!tip] Parole del Professore
> > [!tip]
> > "Queste cose le ho studiate perche mi sono servite per la mia ricerca, e manco sono sicuro che mi siano servite veramente perche il mio advisor di dottorato era sadico e mi metteva in mano certi libri. Pero se uno deve fare ricerca in questo campo, e bene che certe cose le faccia."

### Evento elementare nello spazio della variabile aleatoria

L'evento elementare diventa $\{X(\omega) = x\}$, cioe l'insieme di tutti gli $\omega \in \Omega$ tali che $X(\omega) = x$:

$$P(X = x) = P\!\big(\{\omega \in \Omega : X(\omega) = x\}\big)$$

La probabilità si "trasporta" dallo spazio di probabilità originario al nuovo spazio numerico.

> [!example] Parità del lancio di un dado onesto
> Sia $\Omega = \{1,2,3,4,5,6\}$ e si definisca:
> $$X(\omega) = \begin{cases} 0 & \text{se } \omega \in \{2,4,6\} \text{ (risultato pari)} \\ 1 & \text{se } \omega \in \{1,3,5\} \text{ (risultato dispari)} \end{cases}$$
> Allora, poiche il dado e onesto e gli eventi $\{2\}, \{4\}, \{6\}$ sono incompatibili:
> $$P(X = 0) = P(\{2,4,6\}) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} = \frac{1}{2}$$
> $$P(X = 1) = 1 - P(X = 0) = \frac{1}{2}$$
> Essendo la variabile binaria, una volta calcolata una probabilità non c'e bisogno di calcolare l'altra.

> [!example] Doppio lancio di una moneta onesta
> $\Omega = \{TT, TC, CT, CC\}$ (dove $T$ = testa, $C$ = croce). Si puo definire una variabile aleatoria $X$ che assume i valori $\{0, 1, 2, 3\}$ (oppure $\{1, 2, 3, 4\}$, la scelta e arbitraria), ciascuno con probabilità $\frac{1}{4}$ per una moneta onesta: $P = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.

---

## Probability Mass Function (PMF)

> [!abstract] Definizione: PMF (funzione di massa di probabilità)
> Data una variabile aleatoria discreta $X$ con alfabeto $\mathcal{X} = \{x_1, x_2, \ldots, x_m\}$ (dove $m = |\mathcal{X}|$ e la cardinalità dell'alfabeto), la **PMF** (Probability Mass Function) e la sequenza:
> $$p_X(x_i) = P(X = x_i), \quad i = 1, 2, \ldots, m$$
>
> Una sequenza di $m$ numeri e una PMF valida **se e solo se**:
> 1. $p_X(x_i) \geq 0$ per ogni $i$ (non negatività --- Assioma 1 di Kolmogorov);
> 2. $\displaystyle\sum_{i=1}^{m} p_X(x_i) = 1$ (normalizzazione --- Assioma 2 di Kolmogorov).
>
> Dalla normalizzazione e dalla non negatività segue automaticamente che $p_X(x_i) \leq 1$ per ogni $i$ (la somma di numeri positivi e $1$, quindi ogni singolo numero e al piu $1$).

> [!example] Verifica di una PMF
> La sequenza $\left(\frac{1}{2},\; \frac{1}{4},\; \frac{1}{8},\; \frac{1}{8}\right)$ e una PMF valida?
> $$\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} = \frac{4}{8} + \frac{2}{8} + \frac{1}{8} + \frac{1}{8} = \frac{8}{8} = 1 \quad \checkmark$$
> Tutti i termini sono non negativi e la somma e $1$: **si**, e una PMF valida.

> [!example] PMF del lancio singolo e del doppio lancio
> - **Lancio singolo** di una moneta onesta: la PMF e $\left(\frac{1}{2},\; \frac{1}{2}\right)$, due valori (variabile binaria).
> - **Doppio lancio** di una moneta onesta: la PMF e $\left(\frac{1}{4},\; \frac{1}{4},\; \frac{1}{4},\; \frac{1}{4}\right)$, quattro valori.

---

## Cenno al Valore Atteso (Media)

Il professore anticipa brevemente il concetto di **valore atteso**. Per una variabile aleatoria binaria $X$ con $P(X = 0) = P(X = 1) = \frac{1}{2}$, chiede alla classe: "Qual e la media di questa variabile aleatoria?"

La risposta e $\frac{1}{2}$, e il ragionamento frequentistico che porta a questa risposta e il seguente:

Se si fanno $n$ prove e si osservano le realizzazioni $X(\omega_1), X(\omega_2), \ldots, X(\omega_n)$, la **media aritmetica** e:

$$\bar{X}_n = \frac{1}{n} \sum_{k=1}^{n} X(\omega_k) = \frac{1}{n}\big(0 \cdot n_0 + 1 \cdot n_1\big) = \frac{n_1}{n}$$

dove $n_0$ e il numero di volte in cui esce $0$ e $n_1 = n - n_0$ e il numero di volte in cui esce $1$. Quando $n \to \infty$:

$$\bar{X}_n \xrightarrow{n \to \infty} 0 \cdot P(X=0) + 1 \cdot P(X=1) = \frac{1}{2} \stackrel{\text{def}}{=} E[X]$$

> [!tip] Parole del Professore
> > [!tip]
> > "Voi avete automaticamente detto, guarda, se io faccio $n$ prove, la meta delle volte mi viene $0$, la meta delle volte mi viene $1$. Voi ragionate inevitabilmente sulla frequenza di successo."

> [!warning] Attenzione
> Il risultato $E[X] = \frac{1}{2}$ vale perche la variabile e **equiprobabile**. Il fatto che la media aritmetica converga al valore atteso e un risultato profondo che sarà formalizzato nelle lezioni successive.

---

> [!abstract] Punti chiave della lezione
> - Le proprietà della probabilità derivate dalla frequenza di successo sono confermate dalla teoria assiomatica, dove diventano **teoremi** dimostrabili dai soli assiomi di Kolmogorov.
> - Un'**algebra** e una collezione di sottoinsiemi chiusa rispetto a unione e complementazione; la chiusura rispetto a intersezione e differenza segue dalle leggi di De Morgan.
> - Una **$\sigma$-algebra** estende la chiusura a unioni numerabili, ed e necessaria quando $\Omega$ e infinito numerabile.
> - Lo **spazio di probabilità** $(\Omega, \mathcal{E}, P)$ e il fondamento rigoroso della probabilità: $P$ deve soddisfare non negatività, normalizzazione e $\sigma$-additività.
> - La **legge della probabilità composta** esprime $P(A \cap B)$ come $P(A) \cdot P(B \mid A)$ o $P(B) \cdot P(A \mid B)$.
> - La **legge di Bayes** consente di invertire il condizionamento: da $P(A \mid B)$ a $P(B \mid A)$.
> - La **legge della probabilità totale** permette di scomporre $P(A)$ condizionando rispetto a una partizione.
> - L'**indipendenza stocastica** e definita da $P(A \cap B) = P(A) \cdot P(B)$; se due eventi sono indipendenti, lo sono anche i loro complementari.
> - L'**indipendenza a coppie** non implica l'indipendenza congiunta (controesempio: bit di parità).
> - La **probabilità condizionata** $P(\cdot \mid B)$ e essa stessa una legge di probabilità (soddisfa tutti gli assiomi di Kolmogorov).
> - Una **variabile aleatoria** e un'applicazione da $\Omega$ a un insieme numerico; la **PMF** ne caratterizza completamente la distribuzione nel caso discreto.
> - La **media aritmetica** delle osservazioni converge al valore atteso $E[X]$, concetto che sarà formalizzato nelle prossime lezioni.

---

#MSI #probabilità #sigma-algebra #assiomi #Kolmogorov #Bayes #probabilità-totale #probabilità-composta #indipendenza #variabili-aleatorie #PMF #partizione

---