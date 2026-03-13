---
date: 2026-03-10
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 3
tags:
  - MSI
  - probabilità
  - sigma-algebra
  - Kolmogorov
  - assiomi
  - probabilità-condizionata
  - indipendenza
  - Bayes
  - probabilità-totale
  - variabili-aleatorie
  - PMF
---

# MSI — Lezione 3: Teoria Formale della Probabilita, Bayes e Variabili Aleatorie

**Docente:** Prof. Marco Lops | **Corso:** Metodi Statistici per l'Informazione | **CFU:** 6

---

## Argomenti trattati

- Riepilogo dell'analisi combinatoria ($k$-uple, permutazioni, coefficiente binomiale)
- Riepilogo delle proprieta derivate dalla definizione frequentistica
- Riepilogo della probabilita condizionata e della legge di Bayes
- Legge della probabilita totale (partizioni)
- Teoria formale: algebra e $\sigma$-algebra di eventi
- Spazio di probabilita e assiomi di Kolmogorov
- Derivazione delle proprieta dagli assiomi
- Indipendenza stocastica: definizione e proprieta
- Indipendenza a coppie vs. indipendenza congiunta (bit di parita)
- Esercizio: $n$ eventi indipendenti
- La probabilita condizionata come legge di probabilita
- Esercizio: bussolotto con dado onesto e dado truccato (Bayes)
- Introduzione alle variabili aleatorie e alla PMF

---

## Riepilogo: Analisi Combinatoria

Il professore apre la lezione richiamando i risultati fondamentali dell'analisi combinatoria trattati nelle lezioni precedenti.

Dato un insieme di $n$ elementi:

- Il numero di **$k$-uple ordinate di elementi distinti** (disposizioni semplici) e:

$$D_{n,k} = \frac{n!}{(n-k)!}$$

- Il numero di **$k$-uple ordinate con ripetizione** e:

$$n^k$$

- Il numero di **$k$-uple non ordinate** (combinazioni semplici) si ottiene dividendo le disposizioni per il numero di permutazioni di $k$ elementi, cioe $k!$:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

dove $\binom{n}{k}$ e il **coefficiente binomiale**, che conta anche il numero di sequenze binarie di lunghezza $n$ con esattamente $k$ uni.

> [!quote]
> "Aritmetica deriva dal greco *arithmos*, che vuol dire numero. Quindi questi esercizi numerologici, ho detto si, va bene, ma spesso gli eventi elementari non sono equiprobabili."

---

## Riepilogo: Proprieta dalla Definizione Frequentistica

Ricordando che la probabilita e definita come il limite della frequenza di successo:

$$P(A) = \lim_{n \to \infty} f_n(A) = \lim_{n \to \infty} \frac{N_A}{n}$$

dove $N_A$ e il numero di volte in cui l'evento $A$ si verifica su $n$ prove, si ricavano le seguenti proprieta come conseguenze delle operazioni tra insiemi:

### Evento complementare

Se $A$ si verifica $N_A$ volte su $n$ prove, il complementare $A^c$ si verifica $n - N_A$ volte:

$$P(A^c) = 1 - P(A)$$

### Unione di eventi (subadditivita)

Il numero di volte in cui si verifica $A \cup B$ e $N_A + N_B - N_{A \cap B}$ (per non contare due volte l'intersezione):

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Se $A$ e $B$ sono **eventi incompatibili** ($A \cap B = \emptyset$):

$$P(A \cup B) = P(A) + P(B)$$

### Differenza di eventi

Il numero di volte in cui si verifica $A$ ma non $B$ e $N_A - N_{A \cap B}$:

$$P(A \setminus B) = P(A) - P(A \cap B)$$

> [!tip] La probabilita come misura
> La probabilita si comporta esattamente come una misura di area: l'area di $A \cup B$ non e la somma delle aree se i due insiemi si sovrappongono; bisogna sottrarre l'intersezione contata due volte.

---

## Riepilogo: Probabilita Condizionata

La **frequenza condizionale** di $A$ dato $B$ si costruisce restringendo l'analisi ai soli elementi che soddisfano la condizione $B$:

$$f_n(A \mid B) = \frac{N_{A \cap B}}{N_B} = \frac{N_{A \cap B}/n}{N_B/n} = \frac{f_n(A \cap B)}{f_n(B)}$$

Passando al limite:

> [!abstract] Definizione: Probabilita condizionata
> $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0$$
> La probabilita che si verifichi $A$, dato che si e verificato $B$, e il rapporto tra la probabilita che si verifichino entrambi e la probabilita di $B$.

Scambiando $A$ e $B$:

$$P(B \mid A) = \frac{P(A \cap B)}{P(A)}$$

Da cui si ricava la **legge della probabilita composta**:

$$P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$$

### Legge di Bayes

Uguagliando le due espressioni di $P(A \cap B)$:

> [!abstract] Definizione: Legge di Bayes
> $$P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$$
> Se si conoscono le probabilita $P(A)$, $P(B)$ e la condizionale $P(A \mid B)$, si puo ricavare la condizionale inversa $P(B \mid A)$.

> [!quote]
> "Dalla legge di Bayes ha preso nome tutta la statistica bayesiana."

---

## Legge della Probabilita Totale

> [!abstract] Definizione: Partizione
> Si definisce **partizione** di $\Omega$ una collezione di $m$ sottoinsiemi $\{E_1, E_2, \ldots, E_m\}$ tali che:
> 1. siano a due a due disgiunti: $E_i \cap E_j = \emptyset$ per $i \neq j$;
> 2. la loro unione sia l'intero spazio: $\bigcup_{i=1}^{m} E_i = \Omega$.

> [!example] Esempio concreto
> I lastroni sul pavimento di un'aula sono una partizione della stanza: la loro unione copre tutta la stanza e due lastroni diversi non si sovrappongono.

Dato un qualunque evento $A$:

$$A = A \cap \Omega = A \cap \left(\bigcup_{i=1}^{m} E_i\right) = \bigcup_{i=1}^{m} (A \cap E_i)$$

Poiche gli insiemi $A \cap E_i$ e $A \cap E_j$ sono **disgiunti** (in quanto $E_i$ e $E_j$ non hanno elementi comuni), la probabilita dell'unione e la somma:

$$P(A) = \sum_{i=1}^{m} P(A \cap E_i)$$

Usando la definizione di probabilita condizionata, $P(A \cap E_i) = P(A \mid E_i) \cdot P(E_i)$:

> [!abstract] Definizione: Legge della probabilita totale
> $$P(A) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)$$
> La probabilita di un evento $A$ si puo scomporre condizionando rispetto a una partizione dello spazio dei campioni.

> [!quote]
> "Questa legge, ragazzi, e importantissima. Si usa in tutti i calcoli probabilistici, in quasi tutti, perche a volte devo calcolare la probabilita di un evento ed e difficile, pero se mi metto in certe condizioni la devo scomporre in calcoli piu semplici."

---

## Teoria Formale della Probabilita

Tutte le proprieta ricavate finora derivano dalla definizione frequentistica (limite della frequenza di successo), che pero e matematicamente imprecisa. Si passa ora alla **definizione assiomatica**.

### Algebra di eventi

Dato uno spazio dei campioni $\Omega$, consideriamo una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$.

> [!abstract] Definizione: Algebra
> Una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$ si chiama **algebra** se soddisfa due proprieta:
> 1. **Chiusura rispetto all'unione:** se $A_i \in \mathcal{E}$ e $A_j \in \mathcal{E}$, allora $A_i \cup A_j \in \mathcal{E}$;
> 2. **Chiusura rispetto alla complementazione:** se $A_i \in \mathcal{E}$, allora $A_i^c \in \mathcal{E}$.

### Chiusura rispetto all'intersezione (dimostrazione)

L'algebra e chiusa anche rispetto all'intersezione. Lo si dimostra usando le **leggi di De Morgan**.

La legge di De Morgan afferma:

$$(A \cup B)^c = A^c \cap B^c$$

Complementando entrambi i membri:

$$A \cap B = (A^c \cup B^c)^c$$

Allora, se $A \in \mathcal{E}$ e $B \in \mathcal{E}$:
1. $A^c \in \mathcal{E}$ e $B^c \in \mathcal{E}$ (chiusura per complementazione);
2. $A^c \cup B^c \in \mathcal{E}$ (chiusura per unione);
3. $(A^c \cup B^c)^c \in \mathcal{E}$ (chiusura per complementazione).

Quindi $A \cap B \in \mathcal{E}$.

### Chiusura rispetto alla differenza

Analogamente, $A \setminus B = A \cap B^c$: poiche $B^c \in \mathcal{E}$ e l'intersezione e chiusa, si ha $A \setminus B \in \mathcal{E}$.

> [!tip] Tutte le operazioni insiemistiche restano nell'algebra
> Unione, intersezione, complementazione e differenza di elementi dell'algebra producono sempre elementi dell'algebra. Questo garantisce che si possa calcolare la funzione di probabilita su qualunque combinazione di eventi.

### La piu piccola algebra contenente un evento

> [!example] Esempio: dado e evento "risultato pari"
> Sia $\Omega = \{1,2,3,4,5,6\}$ e $A = \{2,4,6\}$ l'evento "risultato pari". La piu piccola algebra che contiene $A$ e:
> $$\mathcal{E} = \{\emptyset,\; \Omega,\; A,\; A^c\}$$
> Infatti:
> - se c'e $A$, ci deve essere il suo complemento $A^c = \{1,3,5\}$;
> - se c'e $A$ e $A^c$, la loro unione $A \cup A^c = \Omega$ deve appartenere;
> - se c'e $\Omega$, il suo complemento $\emptyset$ deve appartenere.
>
> L'insieme delle parti $2^\Omega$ e anch'esso un'algebra, ma e molto piu grande del necessario.

### Sigma-algebra ($\sigma$-algebra)

> [!abstract] Definizione: $\sigma$-algebra
> Un'algebra $\mathcal{E}$ si chiama **$\sigma$-algebra** se un'**unione numerabile** di suoi elementi e ancora un elemento dell'algebra:
> $$A_1, A_2, A_3, \ldots \in \mathcal{E} \quad \Longrightarrow \quad \bigcup_{i=1}^{\infty} A_i \in \mathcal{E}$$

> [!warning] Algebra vs. $\sigma$-algebra
> Un'algebra garantisce la chiusura per unioni **finite**. Una $\sigma$-algebra estende questa garanzia a unioni **numerabili** (infinite ma contabili). La distinzione e rilevante quando lo spazio dei campioni e numerabile (ad esempio, contare le macchine su un'autostrada: l'evento puo essere $\{0\}, \{1\}, \{2\}, \ldots$ fino a infinito).

> [!quote]
> "Sigma perche? Forse sommatoria, no? Simbolo della somma."

---

## Spazio di Probabilita e Assiomi di Kolmogorov

> [!abstract] Definizione: Legge di probabilita (Kolmogorov)
> Dato uno spazio dei campioni $\Omega$ e una $\sigma$-algebra $\mathcal{E}$, si definisce **legge di probabilita** una funzione
> $$P : \mathcal{E} \to [0,1]$$
> che soddisfa i seguenti **assiomi di Kolmogorov**:
>
> **Assioma 1 — Non negativita:**
> $$P(A) \geq 0 \quad \forall\, A \in \mathcal{E}$$
>
> **Assioma 2 — Normalizzazione:**
> $$P(\Omega) = 1$$
>
> **Assioma 3 — $\sigma$-additivita (subadditivita):**
> Se $A$ e $B$ sono eventi disgiunti ($A \cap B = \emptyset$):
> $$P(A \cup B) = P(A) + P(B)$$
>
> **Assioma 3½ — Estensione numerabile:**
> Se $\{A_i\}_{i=1}^{\infty}$ e una successione di eventi a due a due disgiunti:
> $$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

La terna $(\Omega, \mathcal{E}, P)$ prende il nome di **spazio di probabilita**.

> [!warning] Perche la $\sigma$-algebra?
> La struttura della $\sigma$-algebra garantisce che tutte le operazioni insiemistiche restino nel dominio di definizione della funzione $P$. Senza questa struttura, non si potrebbe essere certi di poter calcolare $P$ su combinazioni arbitrarie di eventi.

---

## Derivazione delle Proprieta dagli Assiomi

Il professore mostra come le proprieta ricavate in modo "facile" dalla definizione frequentistica si dimostrino ora rigorosamente a partire dai soli assiomi di Kolmogorov.

### Probabilita di $A \setminus B$

Si parte dall'identita insiemistica:

$$A = A \cap \Omega = A \cap (B \cup B^c) = (A \cap B) \cup (A \cap B^c)$$

dove $(A \cap B)$ e $(A \cap B^c)$ sono **disgiunti** (il primo contiene elementi in $B$, il secondo no). Per la $\sigma$-additivita:

$$P(A) = P(A \cap B) + P(A \cap B^c)$$

Ma $A \cap B^c = A \setminus B$, quindi:

$$\boxed{P(A \setminus B) = P(A) - P(A \cap B)}$$

### Probabilita di $A \cup B$

Si scrive:

$$A \cup B = A \cup (B \cap A^c)$$

dove $A$ e $B \cap A^c$ sono disgiunti (il secondo contiene solo elementi di $B$ che non appartengono ad $A$). Quindi:

$$P(A \cup B) = P(A) + P(B \cap A^c)$$

Ma dalla proprieta appena dimostrata, $P(B \cap A^c) = P(B \setminus A) = P(B) - P(A \cap B)$:

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

### Probabilita dell'evento complementare

$A \cup A^c = \Omega$, e $A$ e $A^c$ sono incompatibili. Per la $\sigma$-additivita e la normalizzazione:

$$P(A) + P(A^c) = P(\Omega) = 1 \quad \Longrightarrow \quad \boxed{P(A^c) = 1 - P(A)}$$

### Probabilita dell'evento impossibile

L'insieme vuoto e il complemento di $\Omega$:

$$P(\emptyset) = P(\Omega^c) = 1 - P(\Omega) = 1 - 1 = 0$$

> [!quote]
> "Riprendo il giro per dirvi quanto e pesante questo. Abbiamo trovato le cose prima, le abbiamo trovate in modo facile. Ora dimostrarle diventa un giochino, perche gia sappiamo il risultato che dobbiamo tirare."

---

## Indipendenza Stocastica

> [!abstract] Definizione: Indipendenza stocastica
> Due eventi $A, B \in \mathcal{E}$ si dicono **statisticamente indipendenti** se:
> $$P(A \cap B) = P(A) \cdot P(B)$$

> [!quote]
> "La nozione di indipendenza e fondamentale e moltissima statistica inferenziale si fonda su ipotesi di indipendenza, perche senza indipendenza una serie di convergenze [non valgono]."

### Indipendenza dei complementari

**Teorema:** Se $A$ e $B$ sono indipendenti, allora anche $A^c$ e $B^c$ sono indipendenti.

**Dimostrazione.** Per le leggi di De Morgan:

$$A^c \cap B^c = (A \cup B)^c$$

Quindi:

$$P(A^c \cap B^c) = P\big((A \cup B)^c\big) = 1 - P(A \cup B)$$

Sostituendo la formula dell'unione:

$$= 1 - P(A) - P(B) + P(A \cap B)$$

Poiche $A$ e $B$ sono indipendenti, $P(A \cap B) = P(A) \cdot P(B)$:

$$= 1 - P(A) - P(B) + P(A) \cdot P(B)$$

$$= \big(1 - P(A)\big)\big(1 - P(B)\big) = P(A^c) \cdot P(B^c)$$

$$\boxed{P(A^c \cap B^c) = P(A^c) \cdot P(B^c)}$$

### Indipendenza di $n$ eventi

> [!abstract] Definizione: Indipendenza di $n$ eventi
> Una $n$-upla di eventi $A_1, A_2, \ldots, A_n$ e una **$n$-upla indipendente** se gli eventi sono indipendenti a 2 a 2, a 3 a 3, ..., e a $n$ a $n$. Cioe, per ogni sottoinsieme $\{i_1, i_2, \ldots, i_k\} \subseteq \{1, \ldots, n\}$:
> $$P(A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}) = P(A_{i_1}) \cdot P(A_{i_2}) \cdots P(A_{i_k})$$
>
> L'indipendenza di ordine $n$ implica quella di ordine inferiore (da $n-1$ fino a $2$), ma **non vale il viceversa**.

> [!warning] Indipendenza a coppie $\not\Rightarrow$ indipendenza congiunta
> L'indipendenza a coppie non implica l'indipendenza della terna (o della $n$-upla). Un controesempio classico e il **bit di parita**.

### Esempio: il bit di parita

Siano $X_1$ e $X_2$ due bit equiprobabili e indipendenti, ciascuno con valore $0$ o $1$ con probabilita $\frac{1}{2}$. Si definisce il bit di parita:

$$X_3 = X_1 \oplus X_2$$

dove $\oplus$ denota la **somma modulo 2** (XOR): $X_3 = 0$ se $X_1$ e $X_2$ sono uguali, $X_3 = 1$ se sono diversi, in modo che il numero di uni nella terna $(X_1, X_2, X_3)$ sia sempre pari.

Risultato:
- $X_1$ e $X_2$ sono **indipendenti**;
- $X_1$ e $X_3$ sono **indipendenti**;
- $X_2$ e $X_3$ sono **indipendenti**;
- ma la terna $(X_1, X_2, X_3)$ **non** e indipendente.

> [!tip] Perche la terna non e indipendente
> Se si conoscono sia $X_1$ che $X_2$, il valore di $X_3$ e completamente determinato ($X_3 = X_1 \oplus X_2$). La probabilita non si fattorizza: $P(X_1 = x_1, X_2 = x_2, X_3 = x_3) \neq P(X_1 = x_1) \cdot P(X_2 = x_2) \cdot P(X_3 = x_3)$ in generale. Conoscere uno solo dei due bit non da informazione sul terzo, ma conoscerli entrambi si.

---

## Esercizio: $n$ Eventi Indipendenti

Siano $A_1, A_2, \ldots, A_n$ eventi indipendenti, con $P(A_i) = p_i$. Si calcolino:

### 1. Probabilita che non se ne verifichi nessuno

L'evento "non si verifica nessuno" e $A_1^c \cap A_2^c \cap \cdots \cap A_n^c$. Poiche gli $A_i$ sono indipendenti, anche i complementari lo sono:

$$\boxed{P\!\left(\bigcap_{i=1}^{n} A_i^c\right) = \prod_{i=1}^{n} (1 - p_i)}$$

### 2. Probabilita che se ne verifichi almeno uno

L'evento "almeno uno" e il complementare di "nessuno":

$$\boxed{P\!\left(\bigcup_{i=1}^{n} A_i\right) = 1 - \prod_{i=1}^{n} (1 - p_i)}$$

### 3. Probabilita che se ne verifichi esattamente uno (non importa quale)

L'evento "esattamente uno" e l'unione disgiunta:

$$(A_1 \cap A_2^c \cap \cdots \cap A_n^c) \;\cup\; (A_1^c \cap A_2 \cap A_3^c \cap \cdots \cap A_n^c) \;\cup\; \cdots \;\cup\; (A_1^c \cap \cdots \cap A_{n-1}^c \cap A_n)$$

Questi $n$ eventi sono **disgiunti**, quindi:

$$\boxed{P(\text{esattamente uno}) = \sum_{i=1}^{n} p_i \prod_{\substack{j=1 \\ j \neq i}}^{n} (1 - p_j)}$$

> [!quote]
> "E solo logica, ragazzi, pero vi dico anche che questa logica non la dovete dimenticare, perche poi quando andiamo sulle variabili aleatorie e un po' piu numerica la cosa, pero dovete sempre ricordarvi questa logica."

---

## La Probabilita Condizionata come Legge di Probabilita

Un risultato importante: **fissato $B$ con $P(B) > 0$**, la funzione $P(\cdot \mid B)$ soddisfa gli assiomi di Kolmogorov ed e quindi una legge di probabilita a tutti gli effetti.

**Verifica dei tre assiomi:**

**Assioma 1 (Non negativita):** $P(A \mid B) = \frac{P(A \cap B)}{P(B)} \geq 0$, poiche rapporto di due quantita non negative.

**Assioma 2 (Normalizzazione):**

$$P(\Omega \mid B) = \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1$$

**Assioma 3 ($\sigma$-additivita):** Siano $A$ e $C$ eventi disgiunti ($A \cap C = \emptyset$):

$$P(A \cup C \mid B) = \frac{P\big((A \cup C) \cap B\big)}{P(B)} = \frac{P\big((A \cap B) \cup (C \cap B)\big)}{P(B)}$$

Ma se $A \cap C = \emptyset$, allora $(A \cap B) \cap (C \cap B) = \emptyset$, quindi:

$$= \frac{P(A \cap B) + P(C \cap B)}{P(B)} = \frac{P(A \cap B)}{P(B)} + \frac{P(C \cap B)}{P(B)} = P(A \mid B) + P(C \mid B)$$

Dunque $P(\cdot \mid B)$ e una legge di probabilita.

### Conseguenza per l'indipendenza

Se $A$ e $B$ sono indipendenti:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A) \cdot P(B)}{P(B)} = P(A)$$

Il verificarsi di $B$ non influisce minimamente sulla probabilita di $A$: la probabilita condizionata coincide con quella incondizionata.

> [!example] Piove a Napoli, Portici e Kathmandu
> Sia $A$ = "piove a Napoli", $B$ = "piove a Portici", $C$ = "piove a Kathmandu".
> - $P(A \mid B) \neq P(A)$: se piove a Portici, e piu probabile che piova anche a Napoli (eventi dipendenti).
> - $P(A \mid C) \approx P(A)$: sapere che piove a Kathmandu non da informazione utile sulla pioggia a Napoli (eventi approssimativamente indipendenti).
>
> La probabilita a priori $P(A)$ si calcola guardando i record storici: quante volte ha piovuto a Napoli il 10 marzo, diviso il numero totale di anni registrati.

> [!warning] Spazio di probabilita e modellazione
> Tutti gli spazi di probabilita sono matematicamente equivalenti. Ad esempio, per il lancio di una moneta:
> - $P(\text{testa}) = 1, \; P(\text{croce}) = 0$ e legittimo (moneta con due teste);
> - $P(\text{testa}) = P(\text{croce}) = \frac{1}{2}$ e legittimo (moneta onesta).
>
> La scelta della legge di probabilita non e un problema matematico ma di **modellazione**: bisogna scegliere la legge che meglio descrive l'esperimento reale. Se si sbaglia la legge, non si sbaglia matematicamente, ma le predizioni non aderiscono alla realta. Questo e il compito dell'**inferenza statistica**.

---

## Esercizio: Bussolotto con Dado Onesto e Dado Truccato

> [!example] Enunciato
> Un bussolotto contiene due dadi indistinguibili per colore e peso. Un dado e **onesto**, l'altro e **truccato** in modo che il $6$ esca con probabilita $\frac{1}{2}$ e tutti gli altri risultati siano equiprobabili. Si estrae un dado e lo si lancia **due volte**, ottenendo la coppia $(5, 5)$. Qual e la probabilita che il dado estratto sia quello truccato?

### Modellazione del dado truccato

Per il **dado onesto** $D_O$:

$$P(X = i \mid D_O) = \frac{1}{6}, \quad i = 1, 2, \ldots, 6$$

Per il **dado truccato** $D_T$, la probabilita che esca $6$ e $\frac{1}{2}$ e gli altri risultati sono equiprobabili. Per l'assioma di normalizzazione:

$$P(\Omega) = P(X = 6) + \sum_{i=1}^{5} P(X = i) = \frac{1}{2} + 5p = 1 \quad \Longrightarrow \quad p = \frac{1}{10}$$

Quindi:

$$P(X = i \mid D_T) = \begin{cases} \dfrac{1}{2} & \text{se } i = 6 \\[6pt] \dfrac{1}{10} & \text{se } i \neq 6 \end{cases}$$

### Applicazione di Bayes

Sia $A$ = "il dado estratto e truccato" e $B$ = "la coppia di lanci da $(5,5)$". Si vuole calcolare $P(A \mid B)$.

Per la **legge di Bayes**:

$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

**Calcolo di $P(B \mid A)$:** dato che il dado e truccato, i due lanci sono indipendenti:

$$P(5,5 \mid D_T) = \frac{1}{10} \cdot \frac{1}{10} = \frac{1}{100}$$

**Calcolo di $P(B \mid D_O)$:** dato che il dado e onesto:

$$P(5,5 \mid D_O) = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$$

**Probabilita a priori:** i dadi sono indistinguibili, quindi $P(D_T) = P(D_O) = \frac{1}{2}$.

**Calcolo di $P(B)$** con la legge della probabilita totale (la partizione e $\{D_O, D_T\}$):

$$P(B) = P(5,5 \mid D_O) \cdot P(D_O) + P(5,5 \mid D_T) \cdot P(D_T) = \frac{1}{36} \cdot \frac{1}{2} + \frac{1}{100} \cdot \frac{1}{2}$$

$$= \frac{1}{2}\left(\frac{1}{36} + \frac{1}{100}\right) = \frac{1}{2} \cdot \frac{100 + 36}{3600} = \frac{136}{7200} = \frac{17}{900}$$

**Risultato:**

$$\boxed{P(D_T \mid 5,5) = \frac{\frac{1}{100} \cdot \frac{1}{2}}{\frac{17}{900}} = \frac{\frac{1}{200}}{\frac{17}{900}} = \frac{900}{200 \cdot 17} = \frac{9}{34} \approx 0{,}265}$$

> [!tip] Interpretazione
> La probabilita a posteriori che il dado sia truccato ($\approx 26{,}5\%$) e **minore** della probabilita a priori ($50\%$). Questo ha senso: il $5$ esce piu facilmente con il dado onesto ($\frac{1}{6} \approx 16{,}7\%$) che con il truccato ($\frac{1}{10} = 10\%$), quindi osservare due $5$ rende piu probabile che il dado sia quello onesto. Se fossero usciti due $6$, il risultato sarebbe stato opposto.

### Variante: reinserimento del dado

Se dopo il primo lancio si **rimette il dado nel bussolotto**, si mescola e si estrae nuovamente, i due lanci diventano **incondizionalmente indipendenti** (non solo condizionalmente). In tal caso la probabilita di ottenere $5$ in un singolo lancio e:

$$P(X = 5) = P(5 \mid D_T) \cdot P(D_T) + P(5 \mid D_O) \cdot P(D_O) = \frac{1}{10} \cdot \frac{1}{2} + \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{2}\left(\frac{1}{10} + \frac{1}{6}\right) = \frac{1}{2} \cdot \frac{4}{15} = \frac{2}{15}$$

E la probabilita della coppia $(5,5)$ e semplicemente il **quadrato**:

$$P(5,5) = \left(\frac{2}{15}\right)^2 = \frac{4}{225}$$

> [!warning] Indipendenza condizionale vs. incondizionale
> - **Stesso dado, due lanci:** i lanci sono **condizionalmente indipendenti** dato il tipo di dado ($D_T$ o $D_O$), ma **non** incondizionalmente indipendenti. $P(5,5 \mid D_T) = P(5 \mid D_T)^2$, ma $P(5,5) \neq P(5)^2$.
> - **Reinserimento del dado:** ogni lancio e un esperimento identico e completamente ripristinato, quindi i lanci sono **incondizionalmente indipendenti** e $P(5,5) = P(5)^2$.

---

## Introduzione alle Variabili Aleatorie

### Motivazione

Tre esperimenti apparentemente diversi:
1. Lancio di una moneta: testa o croce;
2. Sorgente binaria: emette $0$ o $1$;
3. Lancio di un dado: risultato pari o dispari.

Tutti hanno un esito **binario**. Codificando opportunamente (testa $\to 0$, croce $\to 1$; pari $\to 0$, dispari $\to 1$), si possono trattare in modo **unificato**.

> [!abstract] Definizione: Variabile aleatoria (caso discreto)
> Dato uno spazio di probabilita $(\Omega, \mathcal{E}, P)$ discreto, una **variabile aleatoria** e un'applicazione
> $$X : \Omega \to \mathcal{X}$$
> dove $\mathcal{X}$ e un insieme numerico chiamato **alfabeto** della variabile aleatoria. La funzione $X$ associa ad ogni esito $\omega \in \Omega$ un valore numerico $X(\omega) \in \mathcal{X}$.

> [!tip] Perche le variabili aleatorie sono utili
> Consentono di trattare in modo unificato esperimenti diversi che hanno la stessa struttura probabilistica. Ogni insieme discreto non numerico si puo sempre descrivere attraverso un insieme di numeri interi (ad esempio, puntatori a locazioni di memoria dove sono memorizzate le etichette).

### Evento elementare nello spazio della variabile aleatoria

L'evento elementare diventa $\{X(\omega) = x\}$, cioe l'insieme di tutti gli $\omega \in \Omega$ tali che $X(\omega) = x$:

$$P(X = x) = P\!\big(\{\omega \in \Omega : X(\omega) = x\}\big)$$

> [!example] Parita del lancio di un dado
> Sia $\Omega = \{1,2,3,4,5,6\}$ e si definisca $X(\omega) = 0$ se $\omega$ e pari, $X(\omega) = 1$ se $\omega$ e dispari. Allora:
> $$P(X = 0) = P(\{2,4,6\}) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} = \frac{1}{2}$$
> $$P(X = 1) = 1 - P(X = 0) = \frac{1}{2}$$

> [!example] Doppio lancio di una moneta onesta
> $\Omega = \{TT, TC, CT, CC\}$. Si puo definire una variabile aleatoria $X$ che assume i valori $\{0, 1, 2, 3\}$ (o $\{1, 2, 3, 4\}$), ciascuno con probabilita $\frac{1}{4}$ per una moneta onesta.

### Probability Mass Function (PMF)

> [!abstract] Definizione: PMF (funzione di massa di probabilita)
> Data una variabile aleatoria discreta $X$ con alfabeto $\mathcal{X} = \{x_1, x_2, \ldots, x_m\}$, la **PMF** e la sequenza:
> $$p_X(x_i) = P(X = x_i), \quad i = 1, 2, \ldots, m$$
>
> Una sequenza di $m$ numeri e una PMF valida se e solo se:
> 1. $p_X(x_i) \geq 0$ per ogni $i$ (non negativita);
> 2. $\displaystyle\sum_{i=1}^{m} p_X(x_i) = 1$ (normalizzazione).
>
> Dalla normalizzazione e dalla non negativita segue automaticamente che $p_X(x_i) \leq 1$.

> [!example] Verifica di una PMF
> La sequenza $\left(\frac{1}{2},\; \frac{1}{4},\; \frac{1}{8},\; \frac{1}{8}\right)$ e una PMF valida?
> $$\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} = \frac{4}{8} + \frac{2}{8} + \frac{1}{8} + \frac{1}{8} = \frac{8}{8} = 1 \quad \checkmark$$
> Tutti i termini sono non negativi e la somma e $1$: si, e una PMF valida.

### Cenno alla media

Il professore anticipa brevemente il concetto di **valore atteso** (media). Per una variabile aleatoria binaria $X$ con $P(X = 0) = P(X = 1) = \frac{1}{2}$:

$$E[X] = \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^{n} X(\omega_k) = 0 \cdot \frac{n_0}{n} + 1 \cdot \frac{n_1}{n} \xrightarrow{n \to \infty} 0 \cdot P(X=0) + 1 \cdot P(X=1) = \frac{1}{2}$$

dove $n_0$ e il numero di volte in cui esce $0$ e $n_1$ il numero di volte in cui esce $1$ su $n$ prove. La media aritmetica delle osservazioni converge al **valore atteso** della variabile aleatoria.

> [!quote]
> "Voi avete automaticamente detto, guarda, se io faccio $n$ prove, la meta delle volte mi viene $0$, la meta delle volte mi viene $1$. Voi ragionate inevitabilmente sulla frequenza di successo."

---

> [!summary] Punti chiave della lezione
> - Le proprieta della probabilita derivate dalla frequenza di successo sono confermate dalla teoria assiomatica, dove diventano **teoremi** dimostrabili dagli assiomi di Kolmogorov.
> - Una **$\sigma$-algebra** garantisce che tutte le operazioni insiemistiche restino nel dominio della funzione di probabilita.
> - Lo **spazio di probabilita** $(\Omega, \mathcal{E}, P)$ e il fondamento rigoroso: $P$ deve soddisfare non negativita, normalizzazione e $\sigma$-additivita.
> - La **legge della probabilita totale** permette di scomporre il calcolo di $P(A)$ condizionando rispetto a una partizione.
> - La **legge di Bayes** consente di invertire il condizionamento: da $P(A \mid B)$ a $P(B \mid A)$.
> - L'**indipendenza a coppie** non implica l'indipendenza congiunta (controesempio: bit di parita).
> - La **probabilita condizionata** $P(\cdot \mid B)$ e essa stessa una legge di probabilita (soddisfa gli assiomi di Kolmogorov).
> - Una **variabile aleatoria** e un'applicazione da $\Omega$ a un insieme numerico; la **PMF** ne caratterizza completamente la distribuzione nel caso discreto.

## Prossimi argomenti

- [ ] Ripasso e ulteriori esercizi su probabilita condizionata, Bayes e indipendenza
- [ ] Approfondimento sulle variabili aleatorie discrete
- [ ] Valore atteso e momenti
- [ ] Variabili aleatorie congiunte

---

#MSI #probabilità #sigma-algebra #Kolmogorov #assiomi #Bayes #probabilità-totale #indipendenza #variabili-aleatorie #PMF #partizione #complementare
