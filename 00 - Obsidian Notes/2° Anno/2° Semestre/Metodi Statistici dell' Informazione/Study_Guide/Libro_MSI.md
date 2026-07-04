---
title: "Metodi Statistici per l'Informazione — Libro Didattico"
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
tags: [MSI, libro, probabilità, variabili-aleatorie, inferenza]
---

# Metodi Statistici per l'Informazione

## Indice

**PARTE I — Fondamenti di Probabilità**
- [Capitolo 1 — Analisi Combinatoria](Libro_MSI.md#capitolo-1--analisi-combinatoria)
- [Capitolo 2 — Teoria Formale della Probabilità](Libro_MSI.md#capitolo-2--teoria-formale-della-probabilità)
- [Capitolo 3 — Proprietà della Probabilità dagli Assiomi](Libro_MSI.md#capitolo-3--proprietà-della-probabilità-dagli-assiomi)
- [Capitolo 4 — Probabilità Condizionata e Inferenza](Libro_MSI.md#capitolo-4--probabilità-condizionata-e-inferenza)
- [Capitolo 5 — Indipendenza Stocastica](Libro_MSI.md#capitolo-5--indipendenza-stocastica)

**PARTE II — Variabili Aleatorie Discrete**
- [Capitolo 6 — Variabili Aleatorie Discrete e PMF](Libro_MSI.md#capitolo-6--variabili-aleatorie-discrete-e-pmf)
- [Capitolo 7 — Valore Atteso e Momenti](Libro_MSI.md#capitolo-7--valore-atteso-e-momenti)
- [Capitolo 8 — Distribuzioni Discrete Notevoli](Libro_MSI.md#capitolo-8--distribuzioni-discrete-notevoli)
- [Capitolo 9 — Funzioni di Variabili Aleatorie](Libro_MSI.md#capitolo-9--funzioni-di-variabili-aleatorie)

**PARTE III — Disuguaglianze e Convergenza**
- [Capitolo 10 — Disuguaglianze di Probabilità](Libro_MSI.md#capitolo-10--disuguaglianze-di-probabilità)
- [Capitolo 11 — Legge dei Grandi Numeri](Libro_MSI.md#capitolo-11--legge-dei-grandi-numeri)

**PARTE IV — Coppie e n-uple di Variabili Aleatorie Discrete**
- [Capitolo 12 — PMF Congiunta e Indipendenza](Libro_MSI.md#capitolo-12--pmf-congiunta-e-indipendenza)
- [Capitolo 13 — Covarianza, Correlazione e Media Condizionale](Libro_MSI.md#capitolo-13--covarianza-correlazione-e-media-condizionale)

**PARTE V — Variabili Aleatorie Continue**
- [Capitolo 14 — Variabili Continue: CDF e PDF](Libro_MSI.md#capitolo-14--variabili-continue-cdf-e-pdf)
- [Capitolo 15 — Distribuzioni Continue Notevoli](Libro_MSI.md#capitolo-15--distribuzioni-continue-notevoli)
- [Capitolo 16 — PDF Condizionata e Variabili Continue Bivariate](Libro_MSI.md#capitolo-16--pdf-condizionata-e-variabili-continue-bivariate)

**PARTE VI — Argomenti Avanzati**
- [Capitolo 17 — Canale Binario Simmetrico ed Entropia di Shannon](Libro_MSI.md#capitolo-17--canale-binario-simmetrico-ed-entropia-di-shannon)
- [Capitolo 18 — Vettori Aleatori, Convoluzione e Teorema Centrale del Limite](Libro_MSI.md#capitolo-18--vettori-aleatori-convoluzione-e-teorema-centrale-del-limite)
- [Capitolo 19 — Processi Stocastici](Libro_MSI.md#capitolo-19--processi-stocastici)

---

# PARTE I — Fondamenti di Probabilità

---

## Capitolo 1 — Analisi Combinatoria

Sotto l'ipotesi di **equiprobabilità** degli eventi elementari, la probabilità di un evento si riduce al rapporto tra il numero di casi favorevoli e il numero di casi possibili. Il problema si riconduce quindi all'**enumerazione** sistematica degli elementi tramite gli strumenti dell'analisi combinatoria.

Dato un insieme di $n$ elementi distinti, si definiscono le seguenti strutture combinatorie.

> [!abstract] Definizione: $k$-uple ordinate con ripetizione
> Il numero di sequenze ordinate di lunghezza $k$ scelte da $n$ elementi, con possibilità di ripetere lo stesso elemento, è:
> $$n^k$$

> [!abstract] Definizione: Disposizioni semplici ($k$-uple ordinate senza ripetizione)
> Il numero di sequenze ordinate di lunghezza $k$ scelte da $n$ elementi distinti, senza ripetizione, è:
> $$D_{n,k} = \frac{n!}{(n-k)!}$$

> [!abstract] Definizione: Combinazioni semplici (Coefficiente Binomiale)
> Il numero di sottoinsiemi di dimensione $k$ estratti da un insieme di $n$ elementi (senza ripetizione, senza ordine) è:
> $$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

Il coefficiente binomiale $\binom{n}{k}$ ha un'interpretazione duplice: conta sia i sottoinsiemi di dimensione $k$ sia il numero di **sequenze binarie** di lunghezza $n$ contenenti esattamente $k$ uni. Quest'ultima interpretazione è fondamentale per la modellazione di processi a prove ripetute (vedi Distribuzione Binomiale).

**Formula di Gauss.** Per calcolare la somma dei primi $M$ interi positivi, si usa la formula:

$$\sum_{k=1}^{M} k = \frac{M(M+1)}{2}$$

*Dimostrazione.* Sia $S = 1 + 2 + \cdots + M$. Scriviamo $S$ due volte, una in ordine crescente e una in ordine decrescente, e sommiamo termine a termine: ogni coppia vale $M+1$, e le coppie sono $M$. Quindi $2S = M(M+1)$, da cui la formula. $\square$

---

## Capitolo 2 — Teoria Formale della Probabilità

### 2.1 Limiti dell'Approccio Frequentistico

La probabilità può essere introdotta in modo intuitivo come limite della frequenza relativa di successo:

$$P(A) \stackrel{\text{def}}{=} \lim_{n \to \infty} \frac{N_A}{n}$$

dove $N_A$ è il numero di volte che l'evento $A$ si verifica su $n$ prove. Questa definizione, tuttavia, presenta due problemi fondamentali:

1. **Convergenza non specificata:** non è definito in che senso la frequenza converge; le prove devono essere indipendenti, ma l'indipendenza è essa stessa un concetto probabilistico (circolarità).
2. **Generalità non garantita:** non vi è garanzia a priori che le proprietà trovate sotto queste ipotesi valgano in ogni contesto.

La risposta a queste difficoltà è la **teoria assiomatica di Kolmogorov**, che definisce la probabilità in modo rigoroso.

### 2.2 Algebra di Eventi

Dato uno spazio dei campioni $\Omega$, è necessario definire su quale famiglia di sottoinsiemi di $\Omega$ la probabilità sia definita.

> [!abstract] Definizione: Algebra
> Una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$ è un'**algebra** se soddisfa due proprietà:
> 1. **Chiusura rispetto all'unione:** se $A, B \in \mathcal{E}$, allora $A \cup B \in \mathcal{E}$.
> 2. **Chiusura rispetto alla complementazione:** se $A \in \mathcal{E}$, allora $A^c \in \mathcal{E}$.

**Proprietà derivate.** Un'algebra è automaticamente chiusa anche rispetto a intersezione e differenza:

- **Chiusura rispetto all'intersezione:** Per le leggi di De Morgan, $(A^c \cup B^c)^c = A \cap B$. Poiché $A^c, B^c \in \mathcal{E}$ (complementazione) e $A^c \cup B^c \in \mathcal{E}$ (unione), allora $A \cap B = (A^c \cup B^c)^c \in \mathcal{E}$ (complementazione). $\square$
- **Chiusura rispetto alla differenza:** $A \setminus B = A \cap B^c$; poiché $B^c \in \mathcal{E}$ e l'intersezione è chiusa, $A \setminus B \in \mathcal{E}$. $\square$

> [!example] La più piccola algebra contenente un evento
> Sia $\Omega = \{1,2,3,4,5,6\}$ e $A = \{2,4,6\}$. La più piccola algebra che contiene $A$ è:
> $$\mathcal{E}_{\min} = \{\emptyset,\; \Omega,\; A,\; A^c\}$$
> Essa contiene $A$, il suo complemento $A^c = \{1,3,5\}$, la loro unione $A \cup A^c = \Omega$ e il complemento di $\Omega$, ossia $\emptyset$.

### 2.3 $\sigma$-Algebra

> [!abstract] Definizione: $\sigma$-algebra
> Un'algebra $\mathcal{E}$ è una **$\sigma$-algebra** se è chiusa anche rispetto a unioni **numerabili**:
> $$A_1, A_2, A_3, \ldots \in \mathcal{E} \quad \Longrightarrow \quad \bigcup_{i=1}^{\infty} A_i \in \mathcal{E}$$

> [!warning] Algebra vs. $\sigma$-algebra
> Un'algebra garantisce la chiusura per unioni **finite**. Una $\sigma$-algebra estende questa garanzia a unioni **numerabili** (infinite ma contabili). La distinzione è rilevante solo quando lo spazio dei campioni $\Omega$ è numerabilmente infinito (ad es., $\Omega = \mathbb{N}$). Se $\Omega$ è finito, le due nozioni coincidono.

### 2.4 Assiomi di Kolmogorov

> [!abstract] Definizione: Spazio di Probabilità e Assiomi di Kolmogorov
> Dato uno spazio dei campioni $\Omega$ e una $\sigma$-algebra $\mathcal{E}$ sui suoi sottoinsiemi, si definisce **legge di probabilità** una funzione
> $$P : \mathcal{E} \to [0,1]$$
> che soddisfa i seguenti **assiomi di Kolmogorov**:
>
> - **Assioma 1 — Non negatività:**
> $$P(A) \geq 0 \quad \forall\, A \in \mathcal{E}$$
>
> - **Assioma 2 — Normalizzazione:**
> $$P(\Omega) = 1$$
>
> - **Assioma 3 — Additività finita:**
> Se $A \cap B = \emptyset$, allora $P(A \cup B) = P(A) + P(B)$.
>
> - **Assioma $3\frac{1}{2}$ — $\sigma$-additività (estensione numerabile):**
> Se $\{A_i\}_{i=1}^{\infty}$ è una successione di eventi a due a due disgiunti, allora:
> $$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

La terna $(\Omega, \mathcal{E}, P)$ prende il nome di **spazio di probabilità**.

---

## Capitolo 3 — Proprietà della Probabilità dagli Assiomi

Tutte le proprietà della probabilità si dimostrano rigorosamente dai soli assiomi di Kolmogorov.

### 3.1 Probabilità di $A \setminus B$

**Dimostrazione.** Dall'identità insiemistica $A = (A \cap B) \cup (A \cap B^c)$, dove i due insiemi sono disgiunti, per l'Assioma 3:
$$P(A) = P(A \cap B) + P(A \cap B^c)$$
Poiché $A \cap B^c = A \setminus B$:

$$\boxed{P(A \setminus B) = P(A) - P(A \cap B)}$$

### 3.2 Probabilità dell'Evento Complementare

Poiché $A \cup A^c = \Omega$ e $A \cap A^c = \emptyset$, per l'Assioma 3 e l'Assioma 2:
$$P(A) + P(A^c) = P(\Omega) = 1$$

$$\boxed{P(A^c) = 1 - P(A)}$$

### 3.3 Probabilità dell'Evento Impossibile

$$P(\emptyset) = P(\Omega^c) = 1 - P(\Omega) = 1 - 1 = 0$$

> [!warning] Terminologia
> L'insieme vuoto $\emptyset$ si chiama **evento impossibile**; lo spazio dei campioni $\Omega$ si chiama **evento certo**.

### 3.4 Probabilità dell'Unione

**Dimostrazione.** $A \cup B = A \cup (B \cap A^c)$, dove $A$ e $B \cap A^c$ sono disgiunti. Per l'Assioma 3:
$$P(A \cup B) = P(A) + P(B \cap A^c)$$
Dalla proprietà 3.1 (con $B$ e $A$ scambiati): $P(B \cap A^c) = P(B) - P(A \cap B)$. Quindi:

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

Nel caso di eventi incompatibili ($A \cap B = \emptyset$), la formula si riduce a $P(A \cup B) = P(A) + P(B)$.

---

## Capitolo 4 — Probabilità Condizionata e Inferenza

### 4.1 Probabilità Condizionata e Legge della Probabilità Composta

> [!abstract] Definizione: Probabilità Condizionata
> Dato $P(B) > 0$, la **probabilità condizionata** di $A$ dato $B$ è:
> $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$
> Da cui si ricava la **legge della probabilità composta**:
> $$P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$$

### 4.2 Legge di Bayes

Dalla legge della probabilità composta, sfruttando la commutatività dell'intersezione ($A \cap B = B \cap A$):

> [!abstract] Legge di Bayes
> $$P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$$

Questa formula permette di **invertire il condizionamento**: aggiorna la probabilità *a priori* $P(B)$ alla luce di una nuova evidenza $A$, ottenendo la probabilità *a posteriori* $P(B \mid A)$.

### 4.3 Legge della Probabilità Totale

> [!abstract] Definizione: Partizione
> Una collezione $\{E_1, E_2, \ldots, E_m\}$ è una **partizione** di $\Omega$ se:
> 1. gli insiemi sono a due a due disgiunti: $E_i \cap E_j = \emptyset$ per $i \neq j$;
> 2. la loro unione è l'intero spazio: $\bigcup_{i=1}^{m} E_i = \Omega$.

**Derivazione.** Per distributività, $A = A \cap \Omega = \bigcup_{i=1}^{m} (A \cap E_i)$. I sottoinsiemi $A \cap E_i$ sono disgiunti (perché gli $E_i$ lo sono), quindi per la $\sigma$-additività:

$$P(A) = \sum_{i=1}^{m} P(A \cap E_i)$$

Usando $P(A \cap E_i) = P(A \mid E_i) \cdot P(E_i)$:

> [!abstract] Legge della Probabilità Totale
> $$P(A) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)$$

### 4.4 La Probabilità Condizionata come Legge di Probabilità

**Teorema.** Fissato un evento $B$ con $P(B) > 0$, la funzione $P(\cdot \mid B)$ soddisfa tutti gli assiomi di Kolmogorov ed è quindi una legge di probabilità a tutti gli effetti.

*Dimostrazione.*
- **Non negatività:** $P(A \mid B) = P(A \cap B)/P(B) \geq 0$, rapporto di non negativi.
- **Normalizzazione:** $P(\Omega \mid B) = P(\Omega \cap B)/P(B) = P(B)/P(B) = 1$.
- **$\sigma$-additività:** Se $A \cap C = \emptyset$, allora $(A \cap B) \cap (C \cap B) = \emptyset$, e quindi $P(A \cup C \mid B) = P(A \mid B) + P(C \mid B)$. $\square$

### 4.5 Esercizio: Dado Onesto e Dado Truccato (Bussolotto)

> [!example] Enunciato
> Un bussolotto contiene due dadi indistinguibili. Un dado è **onesto** ($P(i \mid D_O) = 1/6$ per ogni $i$), l'altro è **truccato** con $P(6 \mid D_T) = 1/2$ e $P(i \mid D_T) = 1/10$ per $i \neq 6$ (dalla normalizzazione: $1/2 + 5p = 1 \Rightarrow p = 1/10$). Si estrae un dado e lo si lancia due volte, ottenendo $(5,5)$. Qual è la probabilità che il dado sia quello truccato?

**Soluzione.** Sia $A = \{$dado truccato$\}$ e $B = \{(5,5)\}$. Per Bayes:

$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

- $P(A) = P(D_O) = 1/2$ (estrazioni equiprobabili).
- $P(B \mid D_T) = (1/10)^2 = 1/100$.
- $P(B \mid D_O) = (1/6)^2 = 1/36$.
- Per la legge della probabilità totale: $P(B) = \frac{1}{2} \cdot \frac{1}{36} + \frac{1}{2} \cdot \frac{1}{100} = \frac{1}{2} \cdot \frac{136}{3600} = \frac{17}{900}$.

$$\boxed{P(D_T \mid 5,5) = \frac{(1/100) \cdot (1/2)}{17/900} = \frac{9}{34} \approx 26{,}5\%}$$

L'osservazione di due "5" rende il dado onesto più probabile (il 5 ha probabilità 1/6 con il dado onesto contro 1/10 con il truccato), quindi la probabilità a posteriori scende dalla *a priori* del 50%.

---

## Capitolo 5 — Indipendenza Stocastica

### 5.1 Definizione

> [!abstract] Definizione: Indipendenza Stocastica
> Due eventi $A, B \in \mathcal{E}$ sono **statisticamente indipendenti** se:
> $$P(A \cap B) = P(A) \cdot P(B)$$

Se $A$ e $B$ sono indipendenti, si verifica che $P(A \mid B) = P(A)$: la conoscenza di $B$ non modifica la probabilità di $A$.

### 5.2 Indipendenza dei Complementari

**Teorema.** Se $A$ e $B$ sono indipendenti, allora anche $A^c$ e $B^c$ sono indipendenti.

*Dimostrazione.* Per le leggi di De Morgan, $A^c \cap B^c = (A \cup B)^c$. Quindi:
$$P(A^c \cap B^c) = 1 - P(A \cup B) = 1 - P(A) - P(B) + P(A \cap B)$$
Usando $P(A \cap B) = P(A) P(B)$:
$$= 1 - P(A) - P(B)(1 - P(A)) = (1 - P(A))(1 - P(B)) = P(A^c) P(B^c) \quad \square$$

### 5.3 Indipendenza di $n$ eventi

> [!abstract] Definizione: $n$-upla indipendente
> Una famiglia $\{A_1, A_2, \ldots, A_n\}$ è una **$n$-upla indipendente** se per ogni sottoinsieme di indici $\{i_1, \ldots, i_k\} \subseteq \{1, \ldots, n\}$:
> $$P(A_{i_1} \cap \cdots \cap A_{i_k}) = P(A_{i_1}) \cdots P(A_{i_k})$$
>
> L'indipendenza di ordine $n$ implica quella di ogni ordine inferiore, ma **non vale il viceversa**.

> [!warning] Indipendenza a coppie $\not\Rightarrow$ indipendenza congiunta
> Siano $X_1, X_2$ bit equiprobabili e indipendenti in $\{0,1\}$, e sia $X_3 = X_1 \oplus X_2$ (XOR, bit di parità). Allora ogni coppia $(X_i, X_j)$ è indipendente, ma la terna $(X_1, X_2, X_3)$ **non** è indipendente: conoscendo $X_1$ e $X_2$, il valore di $X_3$ è completamente determinato.

### 5.4 Esercizio: $n$ eventi indipendenti

Siano $A_1, \ldots, A_n$ indipendenti con $P(A_i) = p_i$.

**1. Probabilità che non se ne verifichi nessuno:**
$$P\!\left(\bigcap_{i=1}^{n} A_i^c\right) = \prod_{i=1}^{n} (1 - p_i)$$

**2. Probabilità che se ne verifichi almeno uno:**
$$P\!\left(\bigcup_{i=1}^{n} A_i\right) = 1 - \prod_{i=1}^{n} (1 - p_i)$$

**3. Probabilità che se ne verifichi esattamente uno:**
$$P(\text{esattamente uno}) = \sum_{i=1}^{n} p_i \prod_{\substack{j=1 \\ j \neq i}}^{n} (1 - p_j)$$

*Nota.* Gli $n$ eventi $(A_1 \cap A_2^c \cap \cdots \cap A_n^c)$, $(A_1^c \cap A_2 \cap A_3^c \cap \cdots)$, ecc., sono a due a due disgiunti; la formula segue dalla $\sigma$-additività e dall'indipendenza.

---

> [!abstract] Punti chiave — Parte I
> - Gli **assiomi di Kolmogorov** (non negatività, normalizzazione, $\sigma$-additività) sono l'unico fondamento rigoroso della teoria della probabilità.
> - Tutte le proprietà classiche (probabilità del complementare, dell'unione, $P(\emptyset) = 0$, ecc.) sono **teoremi** dimostrabili dagli assiomi.
> - La **legge di Bayes** aggiorna la probabilità a priori alla luce di nuove osservazioni.
> - La **legge della probabilità totale** scompone $P(A)$ condizionando su una partizione.
> - L'**indipendenza a coppie** non implica l'indipendenza congiunta.

---

# PARTE II — Variabili Aleatorie Discrete

---

## Capitolo 6 — Variabili Aleatorie Discrete e PMF

### 6.1 Definizione

Esperimenti molto diversi (lancio di una moneta, sorgente binaria, parità di un dado) possono avere la stessa struttura probabilistica. Le **variabili aleatorie** formalizzano questa unificazione.

> [!abstract] Definizione: Variabile aleatoria discreta
> Dato uno spazio di probabilità $(\Omega, \mathcal{E}, P)$, una **variabile aleatoria discreta** è un'applicazione
> $$X : \Omega \to \mathcal{X}$$
> dove $\mathcal{X} = \{x_1, x_2, \ldots\}$ è un insieme numerabile chiamato **alfabeto** di $X$. La funzione $X$ assegna ad ogni esito $\omega \in \Omega$ un valore numerico $X(\omega)$.

La probabilità si "trasporta" dallo spazio originale al nuovo spazio numerico:
$$P(X = x) = P\!\big(\{\omega \in \Omega : X(\omega) = x\}\big)$$

### 6.2 Funzione Massa di Probabilità (PMF)

> [!abstract] Definizione: PMF
> Data una variabile aleatoria discreta $X$ con alfabeto $\mathcal{X} = \{x_1, \ldots, x_m\}$, la **PMF** (Probability Mass Function) è la funzione:
> $$p_X(x_i) = P(X = x_i), \quad i = 1, 2, \ldots, m$$
>
> Una sequenza di $m$ numeri è una PMF valida **se e solo se**:
> 1. $p_X(x_i) \geq 0$ per ogni $i$ (non negatività);
> 2. $\sum_{i=1}^{m} p_X(x_i) = 1$ (normalizzazione).

> [!example] Parità del lancio di un dado onesto
> Sia $\Omega = \{1,2,3,4,5,6\}$ e $X(\omega) = 0$ se $\omega$ è pari, $X(\omega) = 1$ se $\omega$ è dispari. Allora $p_X(0) = p_X(1) = 1/2$.

---

## Capitolo 7 — Valore Atteso e Momenti

### 7.1 Valore Atteso (Media Statistica)

**Motivazione frequentistica.** Dopo $n$ prove, la media campionaria è $\bar{x}_n = \sum_{k} a_k \cdot f_n(a_k)$, dove $f_n(a_k) = N_k/n$ è la frequenza relativa del valore $a_k$. Per la **legge dei grandi numeri**, $f_n(a_k) \to P_X(a_k)$ quando $n \to \infty$, quindi $\bar{x}_n$ converge a un valore determinato.

> [!abstract] Definizione: Valore Atteso
> Sia $X$ una variabile aleatoria discreta con alfabeto $\mathcal{X} = \{a_1, \ldots, a_M\}$ e PMF $P_X$. Il **valore atteso** (o **media statistica**, o **speranza matematica**) è:
> $$E[X] = \mu_X = \sum_{k=1}^{M} a_k \cdot P_X(a_k)$$

> [!warning] Media statistica vs. media aritmetica
> La media statistica è una **media pesata** con pesi $P_X(a_k)$. Solo nel caso uniforme (tutti i valori equiprobabili) le due coincidono.

### 7.2 Teorema Fondamentale del Calcolo della Media

> [!abstract] Teorema
> Per una variabile aleatoria $X$ con PMF $p_X$ e una funzione $g$, la media di $Y = g(X)$ è:
> $$\boxed{E[g(X)] = \sum_{x \in \mathcal{X}} g(x) \cdot p_X(x)}$$
> indipendentemente dalla struttura di $g$ (biiettiva o molti-a-uno).

Questo teorema è fondamentale perché permette di calcolare $E[g(X)]$ **senza costruire esplicitamente la PMF di $Y$**.

### 7.3 Varianza e Deviazione Standard

> [!abstract] Definizione: Varianza e Deviazione Standard
> Sia $\mu_X = E[X]$. La **varianza** di $X$ è:
> $$\sigma_X^2 = E\!\left[(X - \mu_X)^2\right] = \sum_{x} (x - \mu_X)^2 \cdot p_X(x) \geq 0$$
> La **deviazione standard** è $\sigma_X = \sqrt{\sigma_X^2}$.

**Relazione varianza–valore quadratico medio:**

$$\boxed{\sigma_X^2 = E[X^2] - \mu_X^2}$$

*Dimostrazione.* Sviluppando: $E[(X-\mu_X)^2] = E[X^2 - 2\mu_X X + \mu_X^2] = E[X^2] - 2\mu_X^2 + \mu_X^2 = E[X^2] - \mu_X^2$. $\square$

**Valore efficace (RMS):** $x_{\text{rms}} = \sqrt{E[X^2]}$.

### 7.4 Proprietà Algebriche di Media e Varianza

Per costanti $a, b \in \mathbb{R}$:

$$E[aX + b] = a \cdot E[X] + b$$

$$\sigma_{aX+b}^2 = a^2 \sigma_X^2$$

*Dimostrazione della proprietà della varianza.* $E[(aX+b - (a\mu_X+b))^2] = E[(a(X-\mu_X))^2] = a^2 E[(X-\mu_X)^2] = a^2 \sigma_X^2$. $\square$

**Interpretazione.** La varianza è **invariante per traslazione** (il termine $b$ non cambia la dispersione) e **scala con $a^2$** (un fattore moltiplicativo $a$ dilata o comprime la distribuzione).

### 7.5 Media Condizionale e Legge della Probabilità Totale per le Medie

> [!abstract] Teorema della Media Condizionale (Law of Total Expectation)
> Data una partizione $\{E_1, \ldots, E_m\}$ di $\Omega$:
> $$E[X] = \sum_{i=1}^m P(E_i) \cdot E[X \mid E_i]$$
> dove $E[X \mid E_i] = \sum_{x} x \cdot p_{X \mid E_i}(x)$ è la **media condizionale** di $X$ dato $E_i$.

*Derivazione.* Si applica la legge della probabilità totale alla PMF condizionata di $X$, si moltiplica per $x$ e si somma su tutti i valori dell'alfabeto.

### 7.6 PMF Condizionata

> [!abstract] Definizione: PMF Condizionata
> Sia $X$ una variabile aleatoria discreta e $A$ un evento con $P(A) > 0$. La **PMF condizionata** di $X$ dato $A$ è:
> $$P_{X \mid A}(x) = P(X = x \mid A) = \frac{P(\{X = x\} \cap A)}{P(A)}, \qquad x \in \mathcal{X}$$
>
> Per ogni $x$ incompatibile con $A$: $P_{X \mid A}(x) = 0$. La PMF condizionata è una PMF valida (non negativa, si somma a 1).

---

## Capitolo 8 — Distribuzioni Discrete Notevoli

### 8.1 Distribuzione di Bernoulli: $X \sim \text{Ber}(p)$

> [!abstract] Definizione
> $X \sim \text{Ber}(p)$ con $p \in [0,1]$ se l'alfabeto è $\{0, 1\}$ e:
> $$P_X(x) = p^x (1-p)^{1-x}, \quad x \in \{0,1\}$$
> Il valore $1$ è il **successo** (probabilità $p$), il valore $0$ è il **fallimento** (probabilità $q = 1-p$).

**Media:** $E[X] = 0 \cdot (1-p) + 1 \cdot p = p$.

**Verifica normalizzazione:** $(1-p) + p = 1$. ✓

### 8.2 Distribuzione Binomiale: $S_n \sim \text{Bin}(n, p)$

> [!abstract] Definizione
> Siano $X_1, \ldots, X_n$ i.i.d. con $X_i \sim \text{Ber}(p)$. La variabile $S_n = \sum_{i=1}^n X_i$ conta il numero totale di successi in $n$ prove indipendenti e segue una **distribuzione Binomiale**:
> $$S_n \sim \text{Bin}(n, p)$$
> L'alfabeto è $\{0, 1, \ldots, n\}$ e la PMF è:
> $$P_{S_n}(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

**Interpretazione combinatoria:** $p^k(1-p)^{n-k}$ è la probabilità di una specifica sequenza con $k$ successi; $\binom{n}{k}$ conta il numero di tali sequenze.

**Verifica normalizzazione:** $\sum_{k=0}^n \binom{n}{k}p^k(1-p)^{n-k} = (p + (1-p))^n = 1$. ✓

**Media — due metodi:**

- *Metodo 1 (linearità):* $E[S_n] = \sum_{i=1}^n E[X_i] = np$.
- *Metodo 2 (calcolo diretto):* Il termine $k=0$ è nullo; semplificando $k$ con $k!$ e raccogliendo $np$:

$$E[S_n] = \sum_{k=1}^{n} k \binom{n}{k} p^k (1-p)^{n-k} = np \sum_{j=0}^{m} \binom{m}{j} p^j (1-p)^{m-j} = np$$

dove $m = n-1$ e $j = k-1$.

$$\boxed{E[S_n] = np}$$

> [!example] Vaccino con efficacia $p = 0{,}95$, $n = 1000$ vaccinati
> $E[S_{1000}] = 1000 \cdot 0{,}95 = 950$ soggetti attesi con immunità.

### 8.3 Distribuzione Uniforme Discreta

> [!abstract] Definizione
> $X$ segue una **distribuzione uniforme discreta** su $\mathcal{X} = \{a_1, \ldots, a_M\}$ se:
> $$P_X(a_k) = \frac{1}{M}, \quad k = 1, \ldots, M$$

**Media:** $E[X] = \frac{1}{M} \sum_{k=1}^M a_k = \frac{a_1 + \cdots + a_M}{M}$ (media aritmetica dell'alfabeto).

Per $\mathcal{X} = \{1, 2, \ldots, M\}$, usando la formula di Gauss:

$$E[X] = \frac{1}{M} \cdot \frac{M(M+1)}{2} = \frac{M+1}{2}$$

> [!example] Dado onesto ($M = 6$): $E[X] = 7/2 = 3{,}5$.

### 8.4 Distribuzione di Poisson: $X \sim \text{Poi}(\lambda)$

> [!abstract] Definizione
> $X \sim \text{Poi}(\lambda)$ con $\lambda > 0$ se l'alfabeto è $\mathbb{N}_0 = \{0, 1, 2, \ldots\}$ e:
> $$P_X(k) = \frac{\lambda^k}{k!} e^{-\lambda}, \quad k = 0, 1, 2, \ldots$$

**Verifica normalizzazione:** $\sum_{k=0}^\infty \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \cdot e^\lambda = 1$. ✓

**Media — derivazione completa:**

$$E[X] = \sum_{k=0}^\infty k \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \sum_{k=1}^\infty \frac{\lambda^k}{(k-1)!} = \lambda e^{-\lambda} \sum_{j=0}^\infty \frac{\lambda^j}{j!} = \lambda e^{-\lambda} e^\lambda = \lambda$$

$$\boxed{E[X] = \lambda}$$

**Approssimazione Poisson della Binomiale.** Per $n \to \infty$, $p \to 0$ con $np = \lambda$ costante:

$$\binom{n}{k} p^k (1-p)^{n-k} \approx \frac{\lambda^k}{k!} e^{-\lambda}$$

**Proprietà di chiusura (subcampionamento bernoulliano).** Se $N \sim \text{Poi}(\lambda)$ e $M \mid N = n \sim \text{Bin}(n, p)$, allora $M \sim \text{Poi}(\lambda p)$.

*Dimostrazione.* $P(M=m) = \sum_{n=m}^\infty \binom{n}{m} p^m (1-p)^{n-m} \frac{\lambda^n}{n!} e^{-\lambda}$. Effettuando la sostituzione $\ell = n - m$ e riconoscendo la serie esponenziale, si ottiene $P(M=m) = \frac{(\lambda p)^m}{m!} e^{-\lambda p}$. $\square$

> [!example] Applicazioni della Poisson
> La Poisson modella fenomeni dove singoli eventi sono rari ma vengono osservati su un numero enorme di occasioni: arrivi di auto al casello, pacchetti al router, clienti in un ufficio postale.

### 8.5 Distribuzione Geometrica: $X \sim \text{Geo}(p)$

> [!abstract] Definizione
> $X \sim \text{Geo}(p)$ con $p \in (0,1]$ rappresenta il **numero di prove necessarie per il primo successo** in una sequenza di prove di Bernoulli indipendenti. L'alfabeto è $\{1, 2, 3, \ldots\}$ e:
> $$P_X(k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$

**Interpretazione.** Per ottenere il primo successo alla prova $k$: $k-1$ fallimenti consecutivi (ciascuno con probabilità $q = 1-p$) seguiti da un successo.

**Verifica normalizzazione:** $\sum_{k=1}^\infty q^{k-1} p = p \cdot \frac{1}{1-q} = 1$. ✓

**Media — derivazione con derivata della serie geometrica:**

$$E[X] = p \sum_{k=1}^\infty k \cdot q^{k-1}$$

Partendo da $\sum_{k=0}^\infty q^k = \frac{1}{1-q}$ e derivando rispetto a $q$:

$$\frac{d}{dq}\left(\frac{1}{1-q}\right) = \frac{1}{(1-q)^2} = \sum_{k=1}^\infty k \cdot q^{k-1}$$

Quindi $E[X] = p \cdot \frac{1}{(1-q)^2} = p \cdot \frac{1}{p^2} = \frac{1}{p}$.

$$\boxed{E[X] = \frac{1}{p}}$$

> [!warning] Proprietà di Assenza di Memoria (Memoryless)
> $$P(X > n + m \mid X > n) = P(X > m), \quad \forall\, n, m \geq 0$$
> La distribuzione geometrica è l'**unica** distribuzione discreta con questa proprietà: il numero di prove rimanenti ha sempre la stessa distribuzione, indipendentemente da quante prove siano già state effettuate senza successo.

---

## Capitolo 9 — Funzioni di Variabili Aleatorie

Se $X$ è una variabile aleatoria con PMF $p_X$ e $g$ è una funzione sull'alfabeto di $X$, allora $Y = g(X)$ è anch'essa una variabile aleatoria.

### 9.1 Caso Biiettivo

Se $g$ è una biiezione (ogni valore di $X$ mappa in un valore distinto di $Y$), le probabilità sono invariate:

$$p_Y(g(x_i)) = p_X(x_i)$$

Si tratta di un semplice **reflagging** (ridenominazione) dell'alfabeto.

### 9.2 Caso Molti-a-Uno

Se più valori di $X$ collassano nello stesso valore di $Y$, le probabilità corrispondenti si sommano:

$$p_Y(y) = \sum_{\{x \,:\, g(x) = y\}} p_X(x)$$

> [!example] $Y = |X|$, con $X \in \{-2,-1,1,2\}$ e $p_X = (1/8, 1/4, 1/4, 3/8)$
> $Y \in \{1, 2\}$:
> - $p_Y(1) = p_X(-1) + p_X(1) = 1/4 + 1/4 = 1/2$
> - $p_Y(2) = p_X(-2) + p_X(2) = 1/8 + 3/8 = 1/2$
> Media: $E[Y] = 1 \cdot 1/2 + 2 \cdot 1/2 = 3/2$.

---

# PARTE III — Disuguaglianze e Convergenza

---

## Capitolo 10 — Disuguaglianze di Probabilità

### 10.1 Disuguaglianza di Markov

> [!abstract] Disuguaglianza di Markov
> Per ogni variabile aleatoria **non negativa** $Y$ e ogni $\delta > 0$:
> $$P(Y \geq \delta) \leq \frac{E[Y]}{\delta}$$

*Dimostrazione (caso continuo, discreta è analoga).* $E[Y] = \int_0^\infty y f_Y(y)\, dy \geq \int_\delta^\infty y f_Y(y)\, dy \geq \delta \int_\delta^\infty f_Y(y)\, dy = \delta \cdot P(Y \geq \delta)$. $\square$

**Generalizzazione.** Per ogni $g$ monotona crescente e non negativa: $P(X \geq \delta) = P(g(X) \geq g(\delta)) \leq E[g(X)]/g(\delta)$.

### 10.2 Disuguaglianza di Chebyshev

> [!abstract] Disuguaglianza di Chebyshev
> Per ogni variabile aleatoria $X$ con media $\mu_X$ e deviazione standard $\sigma_X > 0$, e per ogni $k > 0$:
> $$P\!\left(|X - \mu_X| \geq k\sigma_X\right) \leq \frac{1}{k^2}$$
> Equivalentemente: $P\!\left(|X - \mu_X| < k\sigma_X\right) \geq 1 - \frac{1}{k^2}$.

*Derivazione.* Applicare Markov alla variabile non negativa $Z = (X - \mu_X)^2$ con soglia $\delta = (k\sigma_X)^2$:
$$P((X-\mu_X)^2 \geq k^2\sigma_X^2) \leq \frac{E[(X-\mu_X)^2]}{k^2 \sigma_X^2} = \frac{\sigma_X^2}{k^2 \sigma_X^2} = \frac{1}{k^2}$$
Poiché $(X-\mu_X)^2 \geq k^2\sigma_X^2$ equivale a $|X-\mu_X| \geq k\sigma_X$, si ottiene il risultato. $\square$

> [!important] Universalità di Chebyshev
> La disuguaglianza vale per **qualsiasi distribuzione** con varianza finita, indipendentemente dalla sua forma. È però spesso conservativa: per distribuzioni gaussiane, il 99,7% dei dati è entro $3\sigma$, ma Chebyshev garantisce solo $1 - 1/9 \approx 88{,}9\%$.

Tabella applicativa:

| $k$ | Limite Chebyshev | Interpretazione |
|---|---|---|
| $k=2$ | $P(\|X-\mu\| \geq 2\sigma) \leq 1/4$ | Al più il 25% dei dati oltre $2\sigma$ |
| $k=3$ | $P(\|X-\mu\| \geq 3\sigma) \leq 1/9$ | Al più l'11% dei dati oltre $3\sigma$ |
| $k=10$ | $P(\|X-\mu\| \geq 10\sigma) \leq 1/100$ | Al più l'1% dei dati oltre $10\sigma$ |

---

## Capitolo 11 — Legge dei Grandi Numeri

### 11.1 La Frequenza di Successo come Variabile Aleatoria

Si effettuano $n$ prove indipendenti e si conta quante volte l'evento $A$ si verifica. La **frequenza di successo** è:

$$F_n(A) = \frac{N_A}{n}$$

dove $N_A$ è il numero di occorrenze di $A$. Poiché le prove sono indipendenti, $N_A \sim \text{Bin}(n, P(A))$. Quindi:

$$E[F_n(A)] = \frac{E[N_A]}{n} = P(A)$$

$$\text{Var}(F_n(A)) = \frac{\text{Var}(N_A)}{n^2} = \frac{n P(A)(1-P(A))}{n^2} = \frac{P(A)(1-P(A))}{n}$$

### 11.2 Convergenza

Quando $n \to \infty$:

$$\lim_{n \to \infty} \text{Var}(F_n(A)) = 0$$

La varianza nulla implica che la variabile si concentra attorno alla sua media $P(A)$. Più precisamente, si hanno tre forme di convergenza:

> [!abstract] Legge dei Grandi Numeri
> **Convergenza in media quadratica:**
> $$E\!\left[(F_n(A) - P(A))^2\right] = \text{Var}(F_n(A)) \to 0$$
>
> **Convergenza in probabilità** (da Chebyshev): per ogni $\varepsilon > 0$:
> $$P(|F_n(A) - P(A)| > \varepsilon) \leq \frac{P(A)(1-P(A))}{n\varepsilon^2} \to 0$$
>
> **Legge forte dei grandi numeri:** $P\!\left(\lim_{n \to \infty} F_n(A) = P(A)\right) = 1$ (convergenza quasi certa; non dimostrata qui).

Le implicazioni tra le forme di convergenza sono:

```
Convergenza con probabilità 1 ──┐
                                 ├──► Convergenza in probabilità
Convergenza in media quadratica ─┘
```

Le due forme forti (quasi certa e in media quadratica) implicano entrambe la convergenza in probabilità, ma non si implicano a vicenda.

Questo risultato **giustifica matematicamente** la definizione frequentistica di probabilità: la frequenza di successo converge alla probabilità sia in media quadratica che in probabilità.

---

# PARTE IV — Coppie e n-uple di Variabili Aleatorie Discrete

---

## Capitolo 12 — PMF Congiunta e Indipendenza

### 12.1 PMF Congiunta

> [!abstract] Definizione: Coppia di variabili aleatorie e PMF congiunta
> Dato uno spazio di probabilità $(\Omega, \mathcal{F}, P)$, una **coppia di variabili aleatorie** $(X, Y)$ è un'applicazione $\omega \mapsto (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y}$.
>
> La **PMF congiunta** è:
> $$p_{XY}(x, y) = P(X = x, Y = y), \quad x \in \mathcal{X},\; y \in \mathcal{Y}$$
>
> È una tabella di $|\mathcal{X}| \times |\mathcal{Y}|$ numeri non negativi che sommano a 1:
> $$\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p_{XY}(x, y) = 1$$

### 12.2 Marginalizzazione

> [!abstract] Distribuzioni Marginali
> $$p_X(x) = \sum_{y \in \mathcal{Y}} p_{XY}(x, y), \qquad p_Y(y) = \sum_{x \in \mathcal{X}} p_{XY}(x, y)$$

*Dimostrazione.* $\{X = x\}$ è l'unione disgiunta degli eventi $\{X = x, Y = y\}$ al variare di $y$. Per la $\sigma$-additività: $P(X=x) = \sum_y P(X=x, Y=y)$. $\square$

> [!info] Asimmetria congiunta ↔ marginali
> - Dalla **congiunta** si ricavano **univocamente** le marginali (per somma).
> - Dalle **marginali** non si può ricostruire la congiunta (esistono in generale molte congiunte compatibili con le stesse marginali). L'unica eccezione è il caso di indipendenza.

### 12.3 Indipendenza Statistica

> [!abstract] Definizione: Indipendenza
> Due variabili aleatorie $X$ e $Y$ sono **statisticamente indipendenti** se e solo se:
> $$p_{XY}(x, y) = p_X(x) \cdot p_Y(y) \quad \forall\, x \in \mathcal{X},\; y \in \mathcal{Y}$$

Equivalentemente: la PMF condizionale di $X$ dato $Y$ coincide con la marginale di $X$, cioè conoscere il valore di $Y$ non modifica la distribuzione di $X$.

### 12.4 PMF Condizionale

> [!abstract] Definizione: PMF Condizionale
> $$p_{X|Y}(x \mid y) = P(X = x \mid Y = y) = \frac{p_{XY}(x, y)}{p_Y(y)}, \quad p_Y(y) > 0$$

Per ogni $y$ fissato, $\sum_x p_{X|Y}(x \mid y) = 1$: è una legge di probabilità in $x$.

> [!warning] Organizzazione della tabella
> Nella tabella $p_{X|Y}(x \mid y)$: la **somma per colonne** (a $y$ fissato) vale 1; la **somma per righe** (a $x$ fissato) non vale 1 in generale.

### 12.5 Regola della Catena

Per tre variabili aleatorie $X$, $Y$, $Z$:

$$p_{XYZ}(x,y,z) = p_Z(z) \cdot p_{Y|Z}(y \mid z) \cdot p_{X|YZ}(x \mid y,z)$$

e tutte le permutazioni degli indici sono valide. La regola si generalizza a $n$ variabili.

### 12.6 Marginalizzazione come Media Statistica

$$p_X(x) = \sum_y p_{X|Y}(x \mid y) \cdot p_Y(y) = E_Y\!\left[p_{X|Y}(x \mid Y)\right]$$

La PMF marginale di $X$ è la **media rispetto a $Y$** della PMF condizionale di $X$ dato $Y$.

### 12.7 Estensione a $n$-uple

> [!abstract] PMF congiunta di ordine $n$
> La PMF congiunta di $(X_1, \ldots, X_n)$ è:
> $$p_{X_1 \cdots X_n}(x_1, \ldots, x_n) = P(X_1 = x_1, \ldots, X_n = x_n)$$
>
> **Marginalizzazione gerarchica:** una PMF di ordine $n$ implica tutte le PMF di ordine inferiore. La gerarchia va solo verso il basso: dalla congiunta di ordine $n$ si ricavano quelle di ordine $n-1$, ma non viceversa.

### 12.8 Indipendenza Condizionale e Catene di Markov

> [!abstract] Definizione: Indipendenza Condizionale
> $X_1$ e $X_3$ sono **condizionalmente indipendenti dato $X_2$** se:
> $$p_{X_1 X_3 | X_2}(x_1, x_3 \mid x_2) = p_{X_1|X_2}(x_1 \mid x_2) \cdot p_{X_3|X_2}(x_3 \mid x_2)$$

Questo è diverso dall'indipendenza marginale: $X_1$ e $X_3$ possono essere dipendenti, ma diventano indipendenti condizionatamente a $X_2$.

> [!abstract] Proprietà di Markov
> Una sequenza $X_1, X_2, \ldots, X_n$ soddisfa la **proprietà di Markov** se:
> $$P(X_{n+1} \mid X_n, X_{n-1}, \ldots, X_1) = P(X_{n+1} \mid X_n)$$
> Il futuro dipende dal passato solo attraverso il presente.

---

## Capitolo 13 — Covarianza, Correlazione e Media Condizionale

### 13.1 Covarianza

> [!abstract] Definizione: Covarianza
> $$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]$$

- **Covarianza positiva:** deviazioni positive di $X$ tendono ad accompagnare deviazioni positive di $Y$.
- **Covarianza negativa:** le deviazioni tendono ad essere di segno opposto.
- **Covarianza nulla (incorrelazione):** assenza di tendenza lineare di co-variazione.

**Indipendenza $\Rightarrow$ Incorrelazione:** Se $X$ e $Y$ sono indipendenti, $E[XY] = E[X]E[Y]$, quindi $\text{Cov}(X,Y) = 0$.

> [!warning] Incorrelazione $\not\Rightarrow$ Indipendenza
> La covarianza nulla non implica l'indipendenza in generale. Un controesempio: sia $U$ simmetrica intorno a 0 e $Y = U^2$. Allora $\text{Cov}(U, Y) = E[U^3] - E[U] E[U^2] = 0$ (per simmetria), ma $Y$ è funzione deterministica di $U$. L'implicazione vale nel caso gaussiano.

### 13.2 Coefficiente di Correlazione

> [!abstract] Definizione: Coefficiente di Correlazione
> $$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

**Proprietà fondamentale:** $-1 \leq \rho_{XY} \leq 1$.

*Dimostrazione algebrica.* Consideriamo $Z_{\pm} = \frac{X-\mu_X}{\sigma_X} \pm \frac{Y-\mu_Y}{\sigma_Y}$. Poiché $E[Z_\pm^2] \geq 0$:

$$E[Z_\pm^2] = 1 \pm 2\rho_{XY} + 1 \geq 0 \quad \Rightarrow \quad -1 \leq \rho_{XY} \leq 1 \quad \square$$

*Dimostrazione via Cauchy-Schwarz.* Le variabili aleatorie con varianza finita formano uno spazio vettoriale con prodotto scalare $\langle X', Y' \rangle = \text{Cov}(X, Y)$ (su variabili centrate). La disuguaglianza di Cauchy-Schwarz dà $|\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y$. $\square$

**Valori estremi:** $\rho = 1$ sse $Y = aX + b$ con $a > 0$; $\rho = -1$ sse $a < 0$; $\rho = 0$ indica assenza di relazione lineare.

### 13.3 Matrice di Covarianza

Per un vettore aleatorio $\mathbf{X} = (X_1, \ldots, X_n)^T$:

$$K = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T], \quad K_{ij} = \text{Cov}(X_i, X_j)$$

**Proprietà:** $K$ è **simmetrica** ($K = K^T$) e **semidefinita positiva** ($\mathbf{a}^T K \mathbf{a} \geq 0$ per ogni $\mathbf{a}$). Se $K$ è diagonale, le variabili sono incorrelate.

La matrice di covarianza è fondamentale in PCA (Analisi delle Componenti Principali), filtraggio ottimale di Kalman, e stima MMSE.

### 13.4 Teorema della Media Condizionale (forma generale)

> [!abstract] Teorema della Media Condizionale
> Per variabili aleatorie $X$ e $Y$ con PMF congiunta:
> $$E[g(X,Y)] = E_Y\!\left[E_{X|Y}\!\left[g(X,Y) \mid Y\right]\right]$$
> La media si può calcolare come media rispetto a $Y$ della media condizionale rispetto a $X$ dato $Y$.

---

# PARTE V — Variabili Aleatorie Continue

---

## Capitolo 14 — Variabili Continue: CDF e PDF

### 14.1 Motivazione

In molte applicazioni (tensione di rumore, posizione di una particella, misure fisiche), la variabile aleatoria assume valori in un continuo. Per una variabile continua:

$$P(X = x_0) = 0 \quad \forall\, x_0 \in \mathbb{R}$$

I valori reali su un intervallo sono non numerabili, e assegnare probabilità finite ai singoli punti violerebbe la normalizzazione. Le probabilità vengono assegnate ad **intervalli**, non a punti.

### 14.2 Funzione di Distribuzione Cumulativa (CDF)

> [!abstract] Definizione: CDF
> La **funzione di distribuzione cumulativa** di $X$ è:
> $$F_X(x) = P(X \leq x) \quad \forall\, x \in \mathbb{R}$$
> La CDF è definita per qualsiasi variabile aleatoria, discreta o continua.

**Proprietà:**
1. $F_X(-\infty) = 0$, $F_X(+\infty) = 1$.
2. **Monotonia crescente:** $x_1 < x_2 \Rightarrow F_X(x_1) \leq F_X(x_2)$. *(Poiché $P(X \leq x_2) = P(X \leq x_1) + P(x_1 < X \leq x_2) \geq P(X \leq x_1)$.)*
3. **Continuità a destra** (proprietà tecnica).
4. **Probabilità di intervalli:** $P(a < X \leq b) = F_X(b) - F_X(a)$.

> [!example] CDF di una variabile di Bernoulli $\text{Ber}(p)$
> $$F_X(x) = \begin{cases} 0 & x < 0 \\ 1-p & 0 \leq x < 1 \\ 1 & x \geq 1 \end{cases}$$
> Il grafico è una funzione a scalini; le ampiezze dei salti corrispondono ai valori della PMF.

### 14.3 Funzione Densità di Probabilità (PDF)

> [!abstract] Definizione: PDF
> La **funzione densità di probabilità** è la derivata della CDF:
> $$f_X(x) = \frac{d}{dx} F_X(x)$$
>
> **Relazione inversa:**
> $$F_X(x) = \int_{-\infty}^{x} f_X(t)\, dt$$

**Proprietà:**
1. **Non negatività:** $f_X(x) \geq 0$ (la CDF è monotona, quindi la sua derivata è non negativa).
2. **Normalizzazione:** $\int_{-\infty}^{+\infty} f_X(x)\, dx = 1$.
3. **Probabilità di intervalli:** $P(a \leq X \leq b) = \int_a^b f_X(x)\, dx$.

> [!warning] La PDF non è una probabilità
> $f_X(x_0)$ può essere maggiore di 1 (ad es., per $\text{Exp}(\lambda)$ con $\lambda > 1$ si ha $f_X(0) = \lambda > 1$). La PDF è una **densità** di probabilità; la probabilità è l'**area** sotto la curva su un intervallo.

### 14.4 Valore Atteso via Quantizzazione

Si divide il supporto di $X$ in intervalli di ampiezza $\delta$ e si approssima $X$ con la variabile discreta $X_\delta$ che assume il valore centrale $x_i$ di ogni intervallo:

$$E[X_\delta] = \sum_i x_i \cdot P(X_\delta = x_i) = \sum_i x_i \cdot f_X(c_i) \cdot \delta$$

Questa è la somma di Riemann di $\int x f_X(x)\, dx$. Per $\delta \to 0$:

$$\boxed{E[X] = \int_{-\infty}^{+\infty} x\, f_X(x)\, dx}$$

Più in generale, $E[g(X)] = \int_{-\infty}^{+\infty} g(x)\, f_X(x)\, dx$.

---

## Capitolo 15 — Distribuzioni Continue Notevoli

### 15.1 Distribuzione Uniforme: $X \sim U(a,b)$

> [!abstract] Definizione
> $$f_X(x) = \begin{cases} \dfrac{1}{b-a} & a \leq x \leq b \\ 0 & \text{altrove} \end{cases}$$

**CDF:**
$$F_X(x) = \begin{cases} 0 & x < a \\ \dfrac{x-a}{b-a} & a \leq x \leq b \\ 1 & x > b \end{cases}$$

La CDF è una **rampa lineare** da 0 a 1 nell'intervallo $[a,b]$.

**Media:**
$$E[X] = \int_a^b x \cdot \frac{1}{b-a}\, dx = \frac{b^2 - a^2}{2(b-a)} = \frac{a+b}{2}$$

**Varianza:**
$$\text{Var}(X) = \frac{(b-a)^2}{12}$$

**Applicazione: errore di quantizzazione.** Un quantizzatore uniforme divide un intervallo in $M = 2^R$ livelli di ampiezza $\Delta = (b-a)/M$. L'errore di quantizzazione è uniformemente distribuito su $[-\Delta/2, \Delta/2]$, con errore quadratico medio (distorsione):

$$\text{MSE}_{\text{quantizzazione}} = \frac{\Delta^2}{12}$$

### 15.2 Distribuzione Esponenziale: $X \sim \text{Exp}(\lambda)$

> [!abstract] Definizione
> $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{cases}$$

**CDF:**
$$F_X(x) = \begin{cases} 0 & x < 0 \\ 1 - e^{-\lambda x} & x \geq 0 \end{cases}$$

*Derivazione:* $F_X(x) = \int_0^x \lambda e^{-\lambda t}\, dt = [-e^{-\lambda t}]_0^x = 1 - e^{-\lambda x}$.

**Media:** $E[X] = 1/\lambda$ (derivata per parti; si usa $\int_0^\infty x e^{-ax}\, dx = 1/a^2$).

**Varianza:** $\text{Var}(X) = 1/\lambda^2$.

**Relazione con il processo di Poisson.** Se il numero di eventi in $[0,t]$ segue $\text{Poi}(\lambda t)$, il tempo tra due eventi successivi segue $\text{Exp}(\lambda)$.

> [!warning] Proprietà di Assenza di Memoria (caso continuo)
> $$P(X > s+t \mid X > s) = P(X > t)$$
> La distribuzione esponenziale è l'**unica** distribuzione continua con questa proprietà (analoga alla geometrica nel caso discreto).

### 15.3 Distribuzione di Laplace: $X \sim \text{Laplace}(\lambda)$

> [!abstract] Definizione
> $$f_X(x) = \frac{\lambda}{2} e^{-\lambda|x|}, \quad x \in \mathbb{R}$$

La PDF è una funzione **pari** (simmetrica rispetto all'origine), a forma di "vela invertita" (doppia esponenziale).

**CDF:**
$$F_X(x) = \begin{cases} \dfrac{1}{2} e^{\lambda x} & x \leq 0 \\[4pt] 1 - \dfrac{1}{2} e^{-\lambda x} & x > 0 \end{cases}$$

L'andamento è **sigmoidale**: parte da 0, ha un punto di flesso in $x = 0$ dove vale $1/2$, e tende asintoticamente a 1.

**Media:** $E[X] = 0$ (per simmetria).

**Varianza:** $\text{Var}(X) = 2/\lambda^2$.

> [!tip] Tecnica per funzioni pari
> Per integrare funzioni pari su $(-\infty, x_0)$: se $x_0 \leq 0$ usare $|t| = -t$; se $x_0 > 0$ spezzare l'integrale in $(-\infty, 0)$ e $(0, x_0)$.

**Confronto con la Gaussiana.** La Laplace ha **code più pesanti** (decadimento esponenziale $e^{-\lambda|x|}$) rispetto alla Gaussiana (decadimento gaussiano $e^{-x^2/(2\sigma^2)}$). Modella rumore impulsivo (es. rumore atmosferico) meglio della Gaussiana, che è appropriata per il rumore termico.

### 15.4 Distribuzione di Cauchy

La distribuzione di Cauchy è definita da $f_X(x) = \frac{1}{\pi(1+x^2)}$. È un esempio di variabile continua senza varianza finita: le code decadono così lentamente che $E[X^2] = \infty$. I momenti ordinari non esistono, il che rende inapplicabili i metodi basati su media e varianza.

---

## Capitolo 16 — PDF Condizionata e Variabili Continue Bivariate

### 16.1 PDF Condizionata a un Evento

> [!abstract] Definizione: CDF e PDF Condizionate
> Data $X$ continua e un evento $A$ con $P(A) > 0$:
> $$F_{X|A}(x) = P(X \leq x \mid A) = \frac{P(X \leq x,\; A)}{P(A)}$$
> La **PDF condizionata** si ottiene derivando:
> $$f_{X|A}(x) = \frac{d}{dx} F_{X|A}(x)$$

Per un evento della forma $A = \{X \in B\}$, la PDF condizionata è proporzionale alla PDF originale ristretta al supporto di $A$ e riscalata per normalizzazione:

$$f_{X|A}(x) = \begin{cases} \dfrac{f_X(x)}{P(A)} & x \in A \\ 0 & x \notin A \end{cases}$$

> [!example] Uniforme condizionata
> $X \sim U(0,10)$, $A = \{X > 3\}$. $P(A) = 7/10$.
> Per $x \in (3,10)$: $f_{X|A}(x) = (1/10)/(7/10) = 1/7$.
> La PDF condizionata è $U(3,10)$: l'intervallo si restringe, ma la normalizzazione è preservata.

### 16.2 Variabili Continue Bivariate

> [!abstract] Definizione: PDF congiunta bivariata
> Una coppia $(X,Y)$ di variabili continue è caratterizzata dalla **PDF congiunta**:
> $$f_{X,Y}(x, y) \geq 0, \quad \iint_{\mathbb{R}^2} f_{X,Y}(x, y)\, dx\, dy = 1$$
> La probabilità di una regione $C \subset \mathbb{R}^2$ è: $P((X,Y) \in C) = \iint_C f_{X,Y}(x,y)\, dx\, dy$.

**CDF congiunta:**
$$F_{X,Y}(x, y) = \int_{-\infty}^x \int_{-\infty}^y f_{X,Y}(u, v)\, dv\, du$$

La PDF si recupera dalla CDF via derivata parziale mista: $f_{X,Y}(x,y) = \frac{\partial^2 F_{X,Y}}{\partial x \partial y}$.

**Marginali:**
$$f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x, y)\, dy, \quad f_Y(y) = \int_{-\infty}^{+\infty} f_{X,Y}(x, y)\, dx$$

**Indipendenza:** $X$ e $Y$ sono indipendenti sse $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$.

> [!example] Test di indipendenza
> Se $f_{X,Y}(x,y) = g(x) \cdot h(y)$ con $g, h \geq 0$, allora $X$ e $Y$ sono indipendenti. Basta normalizzare ciascun fattore: $f_X(x) = g(x) / c_1$ e $f_Y(y) = h(y) / c_2$ con $c_1 c_2 = 1$.

**Densità condizionale:**
$$f_{X|Y}(x \mid y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}, \quad f_Y(y) > 0$$

Per $y$ fissato, è una PDF in $x$ (si integra a 1 su $\mathbb{R}$).

### 16.3 Trasformazione di Densità

Se $X$ è una variabile continua con PDF $f_X$ e $Y = g(X)$ dove $g$ è strettamente monotona e differenziabile, la PDF di $Y$ si calcola tramite la **formula del cambio di variabile**:

> [!abstract] Teorema: Trasformazione di Densità
> Se $g$ è strettamente monotona, la PDF di $Y = g(X)$ è:
> $$f_Y(y) = f_X\!\left(g^{-1}(y)\right) \cdot \left|\frac{d}{dy} g^{-1}(y)\right| = \frac{f_X(x)}{|g'(x)|}\bigg|_{x = g^{-1}(y)}$$
> Il fattore $|g'(x)|^{-1}$ è il **fattore Jacobiano** che compensa la dilatazione o compressione introdotta dalla trasformazione.

**Intuizione.** La probabilità sull'evento $\{y \leq Y \leq y + dy\}$ deve coincidere con quella su $\{x : g(x) \in [y, y+dy]\}$. Se $g$ è crescente, questo equivale a $\{g^{-1}(y) \leq X \leq g^{-1}(y+dy)\}$, il cui "spessore" approssimato è $dy/|g'(x)|$.

> [!example] Trasformazione lineare $Y = aX + b$ con $a > 0$
> $g^{-1}(y) = (y-b)/a$, $dg^{-1}/dy = 1/a$. Quindi:
> $$f_Y(y) = \frac{1}{a} f_X\!\left(\frac{y-b}{a}\right)$$
> Se $X \sim \mathcal{N}(\mu, \sigma^2)$, il risultato è $Y \sim \mathcal{N}(a\mu+b, a^2\sigma^2)$: la famiglia gaussiana è chiusa rispetto alle trasformazioni lineari.

---

# PARTE VI — Argomenti Avanzati

---

## Capitolo 17 — Canale Binario Simmetrico ed Entropia di Shannon

### 17.1 Canale Binario Simmetrico (BSC)

Un **canale di comunicazione** trasmette un bit $X \in \{0,1\}$ producendo un'uscita $Y \in \{0,1\}$. Il canale è **binario simmetrico** con parametro $\varepsilon \in [0,1]$ se:

$$p_{Y|X}(0 \mid 0) = p_{Y|X}(1 \mid 1) = 1-\varepsilon$$
$$p_{Y|X}(1 \mid 0) = p_{Y|X}(0 \mid 1) = \varepsilon$$

Il parametro $\varepsilon$ è la **probabilità di errore** su singolo bit.

**Probabilità di errore (globale).** Sia $P(X=1) = p$. Per la legge della probabilità totale:

$$P(\text{errore}) = P(Y \neq X) = \varepsilon(1-p) + \varepsilon p = \varepsilon$$

La probabilità di errore è $\varepsilon$ indipendentemente dalla distribuzione dell'ingresso.

**Inferenza con Bayes.** Data $Y = 0$, la probabilità che fosse $X = 0$ è:

$$P(X=0 \mid Y=0) = \frac{(1-\varepsilon)(1-p)}{(1-\varepsilon)(1-p) + \varepsilon p}$$

**Caso peggiore.** Il caso peggiore non è $\varepsilon = 1$ (il canale sarebbe ancora usabile invertendo il bit ricevuto), bensì $\varepsilon = 1/2$: il bit ricevuto è statisticamente indipendente dal bit trasmesso e non fornisce alcuna informazione.

### 17.2 Entropia di Shannon

**Misura dell'informazione.** L'informazione ricevuta dall'osservazione di un evento $A$ con probabilità $P(A)$ deve soddisfare:
1. Non negativa: $I(A) \geq 0$.
2. Decrescente nella probabilità: più raro l'evento, più informazione porta.
3. Additiva per eventi indipendenti: $I(A \cap B) = I(A) + I(B)$ se $A \perp B$.

L'unica funzione che soddisfa tutte e tre le proprietà è:

$$I(A) = \log_2 \frac{1}{P(A)} = -\log_2 P(A)$$

Con logaritmo in base 2, l'unità è il **bit**.

> [!example] Esempi
> - Evento certo ($P = 1$): $I = 0$ bit (nessuna informazione).
> - Moneta equilibrata ($P = 1/2$): $I = 1$ bit.
> - Evento raro ($P = 1/1024 = 2^{-10}$): $I = 10$ bit.

**Entropia.** Poiché $I(X = x) = -\log_2 p_X(x)$ è essa stessa una variabile aleatoria, l'**entropia** è la sua media statistica:

> [!abstract] Definizione: Entropia di Shannon
> $$H(X) = E\!\left[-\log_2 p_X(X)\right] = -\sum_{x \in \mathcal{X}} p_X(x) \log_2 p_X(x)$$
> Si misura in **bit** con logaritmo in base 2.

**Proprietà fondamentali:**
- $H(X) \geq 0$, con $H(X) = 0$ sse $X$ è deterministica.
- $H(X)$ è massima per la distribuzione uniforme: $H_{\max} = \log_2 |\mathcal{X}|$ bit.
- $H(X,Y) \leq H(X) + H(Y)$, con uguaglianza sse $X$ e $Y$ sono indipendenti.

> [!example] Entropia di una Bernoulli
> Per $X \in \{0,1\}$ con $P(X=1) = p$:
> $$H(X) = -p \log_2 p - (1-p) \log_2(1-p)$$
> $H(X) = 0$ per $p \in \{0,1\}$ (caso deterministico), $H(X) = 1$ bit per $p = 1/2$ (massimo).

**Implicazione per la compressione.** Un file compresso idealmente è una sequenza binaria con bit equiprobabili e statisticamente indipendenti (entropia = 1 bit per bit). Se i caratteri hanno frequenze diverse, l'entropia è inferiore a $\log_2 |\mathcal{X}|$ e la compressione (es. codifica di Huffman) riduce il numero medio di bit per simbolo.

---

## Capitolo 18 — Vettori Aleatori, Convoluzione e Teorema Centrale del Limite

### 18.1 Vettori Aleatori

Un vettore aleatorio $\mathbf{X} = (X_1, \ldots, X_n)^T$ ha:
- **Vettore delle medie:** $\boldsymbol{\mu} = E[\mathbf{X}] = (\mu_1, \ldots, \mu_n)^T$.
- **Matrice di covarianza:** $K = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]$, con $K_{ij} = \text{Cov}(X_i, X_j)$.

$K$ è simmetrica e semidefinita positiva ($\mathbf{a}^T K \mathbf{a} \geq 0$ per ogni $\mathbf{a}$, come segue dal fatto che $\text{Var}(\mathbf{a}^T \mathbf{X}) \geq 0$).

### 18.2 Convoluzione e Densità della Somma

> [!abstract] Definizione: Convoluzione
> Il **prodotto di convoluzione** di due funzioni integrabili $f$ e $g$ è:
> $$(f * g)(t) = \int_{-\infty}^{+\infty} f(\tau)\, g(t-\tau)\, d\tau$$

**Motivazione probabilistica.** Se $X$ e $Y$ sono variabili aleatorie continue indipendenti con densità $f_X$ e $f_Y$, la densità della somma $Z = X + Y$ è:

$$f_Z(z) = (f_X * f_Y)(z) = \int_{-\infty}^{+\infty} f_X(x)\, f_Y(z-x)\, dx$$

La convoluzione è **commutativa**, **associativa** e **distributiva** rispetto alla somma.

**Applicazione ai sistemi LTI.** La relazione ingresso-uscita di un sistema lineare tempo-invariante è descritta dalla convoluzione dell'ingresso con la risposta all'impulso. In frequenza (dominio di Laplace), la convoluzione diventa moltiplicazione: $\mathcal{L}\{f * g\} = \mathcal{L}\{f\} \cdot \mathcal{L}\{g\}$.

### 18.3 Teorema Centrale del Limite (TCL)

> [!abstract] Teorema Centrale del Limite
> Siano $X_1, X_2, \ldots, X_n$ variabili aleatorie **i.i.d.** con media $\mu$ e varianza $\sigma^2 < \infty$. Allora, per $n \to \infty$, la somma standardizzata:
> $$Z_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}}$$
> converge in distribuzione a $\mathcal{N}(0,1)$ (distribuzione gaussiana standard).

**Corollario.** Per $n$ grande: $S_n = \sum_{i=1}^n X_i \approx \mathcal{N}(n\mu, n\sigma^2)$.

**Significato.** Il TCL spiega l'ubiquità della distribuzione gaussiana: ogniqualvolta un fenomeno è la sovrapposizione di molti contributi elementari indipendenti (rumore termico come somma di eventi di scattering, errori di misura, ecc.), il risultato è approssimativamente gaussiano, indipendentemente dalla forma delle distribuzioni individuali.

> [!example] 100 lanci di dado
> Un dado onesto ha $\mu = 3{,}5$ e $\sigma^2 = 35/12 \approx 2{,}917$. La somma di 100 lanci ha media $350$, varianza $291{,}7$, deviazione standard $\approx 17$, ed è approssimativamente $\mathcal{N}(350, 291{,}7)$.

---

## Capitolo 19 — Processi Stocastici

### 19.1 Definizione

> [!abstract] Definizione: Processo Stocastico
> Dato uno spazio di probabilità $(\Omega, \mathcal{F}, P)$, un **processo stocastico** è una famiglia di variabili aleatorie indicizzate dal tempo:
> $$\{X(t) : t \in \mathcal{T}\}$$
> dove $\mathcal{T}$ è un insieme di indici ($\mathbb{N}$ per tempo discreto, $\mathbb{R}$ o $[0, T]$ per tempo continuo).

Il processo dipende da due variabili:
- Fissato $t$, variando $\omega$: si ottiene la variabile aleatoria $X(t, \cdot)$.
- Fissato $\omega$, variando $t$: si ottiene una **realizzazione** (o **traiettoria**) $X(\cdot, \omega)$.

### 19.2 Tempo Discreto vs. Continuo

**Tempo discreto** ($\mathcal{T} = \mathbb{N}$ o $\mathbb{Z}$): le realizzazioni sono sequenze numeriche $(x_1, x_2, x_3, \ldots)$.
*Esempi:* prezzi azionari giornalieri, campioni audio digitali, code di pacchetti.

**Tempo continuo** ($\mathcal{T} = \mathbb{R}_{\geq 0}$): le realizzazioni sono funzioni continue del tempo $t \mapsto X(t, \omega)$.
*Esempi:* voltaggio di rumore termico, moto browniano, intensità luminosa.

### 19.3 Caratterizzazione Statistica

Una caratterizzazione completa richiede:
1. **Medie al primo ordine:** $\mu_X(t) = E[X(t)]$ e $\text{Var}(X(t))$ per ogni $t$.
2. **Medie al secondo ordine:** $\text{Cov}(X(t_1), X(t_2))$ per ogni coppia $(t_1, t_2)$.
3. **Densità congiunte finito-dimensionali:** $f_{X(t_1), \ldots, X(t_n)}$ per ogni $n$ e ogni scelta di tempi.

### 19.4 Stazionarietà

Un processo è **stazionario in senso stretto** se le proprietà statistiche sono invarianti per traslazioni temporali:

$$P(X(t_1) \leq x_1, \ldots, X(t_n) \leq x_n) = P(X(t_1+\tau) \leq x_1, \ldots, X(t_n+\tau) \leq x_n)$$

Un processo è **stazionario in senso lato (WSS)** se:
- $E[X(t)]$ è costante.
- $\text{Var}(X(t))$ è costante.
- $\text{Cov}(X(t_1), X(t_2))$ dipende solo da $t_2 - t_1$.

La stazionarietà semplifica enormemente l'analisi: processi reali su scale temporali limitate sono spesso approssimati come stazionari.

### 19.5 Processo di Poisson

Il **processo di Poisson** con intensità $\lambda > 0$ conta il numero di eventi in intervalli di tempo. Se $N(t)$ è il numero di eventi in $[0, t]$:

$$P(N(t) = k) = \frac{(\lambda t)^k}{k!} e^{-\lambda t}, \quad k = 0, 1, 2, \ldots$$

**Proprietà caratteristiche:**
- **Incrementi indipendenti:** il numero di eventi in intervalli disgiunti sono variabili indipendenti.
- **Incrementi stazionari:** la distribuzione del numero di eventi in $[t, t+s]$ dipende solo da $s$, non da $t$.
- **Assenza di memoria:** la probabilità del prossimo evento non dipende dagli eventi passati.
- **Tempo intereventuale:** il tempo tra due eventi successivi segue $\text{Exp}(\lambda)$.

### 19.6 Processi Gaussiani

Un processo è **gaussiano** se ogni combinazione lineare di variabili del processo è una gaussiana. I processi gaussiani sono completamente caratterizzati dalle funzioni:
- $\mu_X(t) = E[X(t)]$: funzione di media.
- $\gamma(t_1, t_2) = \text{Cov}(X(t_1), X(t_2))$: funzione di autocovarianza.

I processi gaussiani generalizzano la distribuzione normale alle funzioni del tempo e trovano applicazione nel filtraggio ottimale (filtro di Kalman) e nel machine learning (Gaussian Process Regression).

---

*Fine del testo.*

---

#MSI #libro #probabilità #variabili-aleatorie #inferenza #kolmogorov #bayes #distribuzioni #covarianza #CLT #processi-stocastici
