---
title: "Metodi Statistici per l'Informazione — Appunti Completi"
corso: "Metodi Statistici per l'Informazione"
docente: "Marco Lops"
crediti: "6 CFU"
anno: "2025-2026"
tags: [MSI, probabilità, statistica, variabili-aleatorie, inferenza, Shannon, processi]
status: completo
---

# Appunti Completi - Metodi Statistici per l'Informazione

**Corso:** Metodi Statistici per l'Informazione (AA 2025-2026)  
**Docente:** Prof. Marco Lops  
**Crediti:** 6 CFU  
**Email docente:** lops@unina.it  
**Modalità:** 20 Lezioni Frontali + Slide Ufficiali

---

## Indice Generale

**PARTE I — Fondamenti di Probabilità**
- Capitolo 1 — Analisi Combinatoria
- Capitolo 2 — Teoria Formale della Probabilità
- Capitolo 3 — Proprietà della Probabilità dagli Assiomi
- Capitolo 4 — Probabilità Condizionata e Inferenza
- Capitolo 5 — Indipendenza Stocastica

**PARTE II — Variabili Aleatorie Discrete**
- Capitolo 6 — Variabili Aleatorie Discrete e PMF
- Capitolo 7 — Valore Atteso e Momenti
- Capitolo 8 — Distribuzioni Discrete Notevoli
- Capitolo 9 — Funzioni di Variabili Aleatorie

**PARTE III — Disuguaglianze e Convergenza**
- Capitolo 10 — Disuguaglianze di Probabilità
- Capitolo 11 — Legge dei Grandi Numeri

**PARTE IV — Coppie e n-uple di Variabili Aleatorie Discrete**
- Capitolo 12 — PMF Congiunta e Indipendenza
- Capitolo 13 — Covarianza, Correlazione e Media Condizionale

**PARTE V — Variabili Aleatorie Continue**
- Capitolo 14 — Variabili Continue: CDF e PDF
- Capitolo 15 — Distribuzioni Continue Notevoli
- Capitolo 16 — PDF Condizionata e Variabili Continue Bivariate

**PARTE VI — Argomenti Avanzati**
- Capitolo 17 — Canale Binario Simmetrico ed Entropia di Shannon
- Capitolo 18 — Vettori Aleatori, Convoluzione e Teorema Centrale del Limite
- Capitolo 19 — Processi Stocastici

---

# PARTE I — Fondamenti di Probabilità

---

# Capitolo 1 — Analisi Combinatoria

*(Lezioni 0-1)*

## 1.1 Introduzione e Contesto

L'analisi combinatoria fornisce gli strumenti per **contare sistematicamente** gli elementi di insiemi finiti. In probabilità, questo è fondamentale quando lo spazio dei campioni è finito e gli eventi elementari sono equiprobabili:

$$P(A) = \frac{|A|}{|\Omega|}$$

dove $|A|$ è la cardinalità dell'evento A e $|\Omega|$ è la cardinalità totale dello spazio.

## 1.2 Regola del Prodotto Cartesiano

La base di ogni conteggio combinatorio è il **prodotto cartesiano**.

**Teorema:** Dati $k$ insiemi $A_1, A_2, \ldots, A_k$ con cardinalità $|A_i| = n_i$, il loro prodotto cartesiano ha cardinalità:

$$|A_1 \times A_2 \times \cdots \times A_k| = \prod_{i=1}^{k} n_i = n_1 \cdot n_2 \cdot \ldots \cdot n_k$$

**Intuizione:** Per ogni scelta del primo elemento (n₁ modi), posso scegliere il secondo elemento (n₂ modi), e così via. Totale: moltiplicazione.

**Esempio:** 
```
Lancio di una moneta (n=2 esiti: T, C) due volte:
Ω = {T,C} × {T,C} = {TT, TC, CT, CC}
|Ω| = 2 × 2 = 4
```

## 1.3 Disposizioni con Ripetizione

Le **k-uple ordinate con ripetizione** contano le sequenze ordinate di lunghezza k da un alfabeto di n elementi, permettendo ripetizioni.

**Formula:**
$$D'_{n,k} = n^k$$

**Dimostrazione:** Per ogni della k posizioni scelgo uno degli n elementi indipendentemente. Totale: $n \times n \times \cdots \times n$ (k volte) = $n^k$.

**Esempi:**
- Stringhe binarie di lunghezza 5: $2^5 = 32$
- Codici PIN a 4 cifre: $10^4 = 10.000$
- Proteine a 20 aminoacidi di lunghezza 100: $20^{100}$ (astronomico!)

## 1.4 Disposizioni Semplici (Senza Ripetizione)

Le **k-uple ordinate senza ripetizione** contano le sequenze di k elementi distinti da un alfabeto di n elementi.

**Formula:**
$$D_{n,k} = \frac{n!}{(n-k)!} = n(n-1)(n-2)\cdots(n-k+1)$$

**Dimostrazione:** 
- Primo elemento: n scelte
- Secondo elemento: n-1 scelte (uno già usato)
- k-esimo elemento: n-k+1 scelte
- Totale: $n \cdot (n-1) \cdot (n-2) \cdots (n-k+1) = \frac{n!}{(n-k)!}$

**Esempi:**
- Codici di 3 cifre DISTINTE da 0-9: $D_{10,3} = 10 \times 9 \times 8 = 720$
- Staffetta 3x100m (scegliere e ordinare 3 corridori da 8): $D_{8,3} = 8 \times 7 \times 6 = 336$

## 1.5 Permutazioni

Le **permutazioni** sono un caso speciale: ordinare TUTTI gli n elementi di un insieme.

**Formula:**
$$P_n = n! = D_{n,n} = n(n-1)(n-2)\cdots 1$$

**Esempi:**
- Ordinare 5 libri su uno scaffale: $5! = 120$
- Anagrammi della parola "ROMA": $4! = 24$

## 1.6 Combinazioni Semplici (Coefficiente Binomiale)

Le **combinazioni** contano i sottoinsiemi NON ordinati di dimensione k da un insieme di n elementi.

**Formula:**
$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

**Intuizione:** 
- Dispositioni semplici $D_{n,k}$ conta le sequenze ordinate.
- Se l'ordine non importa (sotto-insiemi), ogni insieme di k elementi corrisponde a k! sequenze diverse.
- Divido per k! per eliminare la sovra-conteggiatura.

$$\binom{n}{k} = \frac{D_{n,k}}{k!}$$

**Proprietà:**
- $\binom{n}{k} = \binom{n}{n-k}$ (simmetria)
- $\binom{n}{0} = \binom{n}{n} = 1$
- $\binom{n}{1} = n$
- $\binom{n}{n-1} = n$

**Esempi:**
- Mani di poker (52 carte, 5 per mano): $\binom{52}{5} = 2.598.960$
- Lotterie 6/90: $\binom{90}{6} = 622.614.630$
- Sottoinsiemi di un insieme di 10 elementi: $2^{10} = \binom{10}{0} + \binom{10}{1} + \cdots + \binom{10}{10}$

## 1.7 Interpretazione Binaria del Coefficiente Binomiale

Il numero di **sequenze binarie di lunghezza n con esattamente k uni** è:

$$\binom{n}{k}$$

**Ragionamento:** 
- Se tutti i bit fossero distinti: n! permutazioni
- Ma abbiamo k uni indistinguibili: dividere per k!
- E n-k zeri indistinguibili: dividere per (n-k)!
- Risultato: $\frac{n!}{k!(n-k)!} = \binom{n}{k}$

**Applicazione cruciale:** Questa interpretazione è fondamentale per la **Distribuzione Binomiale** (conteggio successi in n prove).

## 1.8 Coefficiente Multinomiale

**Generalizzazione:** Il numero di sequenze di lunghezza n su un alfabeto di m simboli, con $n_i$ occorrenze del simbolo i (dove $\sum_i n_i = n$), è:

$$\binom{n}{n_1, n_2, \ldots, n_m} = \frac{n!}{n_1! \cdot n_2! \cdots n_m!}$$

**Esempio:** Sequenze di 10 bit con 3 zeri, 4 uni, 2 due, 1 tre:
$$\binom{10}{3,4,2,1} = \frac{10!}{3! \cdot 4! \cdot 2! \cdot 1!} = \frac{3.628.800}{6 \cdot 24 \cdot 2 \cdot 1} = 12.600$$

## 1.9 Binomio di Newton

**Teorema:**
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$$

**Conseguenza immediata (a=b=1):**
$$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$

Questo dice che il numero di **sottoinsiemi** di un insieme di n elementi è $2^n$ (l'insieme delle parti).

**Dimostrazione di $2^n$:** Ogni elemento può stare o non stare nel sottoinsieme: 2 scelte per n elementi = $2^n$.

---

# Capitolo 2 — Teoria Formale della Probabilità

*(Lezioni 1-2)*

## 2.1 Concetti Base: Esperimento, Spazio, Evento

### Esperimento

Un **esperimento** è un'operazione che conduce a **uno tra tanti risultati possibili**.

### Spazio dei Campioni $\Omega$

Lo **spazio dei campioni** è l'insieme di **tutti i possibili esiti**.

$$\Omega = \{\omega_1, \omega_2, \ldots\}$$

**Tipi:**
- **Finito:** Moneta $\Omega = \{T, C\}$
- **Numerabilmente infinito:** Pacchetti in coda $\Omega = \mathbb{N}_0 = \{0,1,2,\ldots\}$
- **Continuo:** Rumore termico $\Omega = \mathbb{R}$

### Evento

Un **evento** è un **sottoinsieme di $\Omega$** descritto da una proposizione.

$$A \subseteq \Omega$$

Un **evento elementare** è un singolo elemento $\omega \in \Omega$.

**Nota critica:** L'evento è univocamente determinato dai suoi elementi, ma la proposizione che lo descrive **NON è unica**.

**Esempio:** Dado, evento $A = \{1,3,5\}$ può essere descritto come:
- "esce un numero dispari"
- "non esce un numero pari"
- "esce 1, 3 o 5"

**→ Riformulare la proposizione è spesso il 90% della soluzione!**

## 2.2 Nomenclatura degli Eventi

| Nome | Significato | Notazione |
|------|-------------|-----------|
| **Evento certo** | Si verifica sempre | $\Omega$ |
| **Evento impossibile** | Mai | $\emptyset$ |
| **Evento complementare** | Opposto di A | $A^c$ o $\bar{A}$ |
| **Eventi incompatibili** | Non possono accadere insieme | $A \cap B = \emptyset$ |
| **A implica B** | Se A accade, accade B | $A \subseteq B$ |

**Esempio — Dado:**
- $A$ = "esce 2", $B$ = "esce pari"
- $A \subseteq B$ (2 è pari, ma non tutti i pari sono 2)

## 2.3 Operazioni sugli Insiemi/Eventi

| Operazione | Definizione | Simbolo |
|-----------|------------|---------|
| **Unione** | A oppure B | $A \cup B$ |
| **Intersezione** | A e B insieme | $A \cap B$ |
| **Complemento** | Non A | $A^c$ |
| **Differenza** | A ma non B | $A \setminus B = A \cap B^c$ |

**Proprietà fondamentali:**

- **De Morgan**: $(A \cup B)^c = A^c \cap B^c$
- **De Morgan**: $(A \cap B)^c = A^c \cup B^c$
- **Associativa**: $(A \cup B) \cup C = A \cup (B \cup C)$
- **Distributiva**: $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

## 2.4 Approccio Frequentistico (Intuitivo)

La probabilità è il **limite della frequenza relativa** di successo:

$$P(A) = \lim_{n \to \infty} \frac{N_A}{n}$$

dove $N_A$ è il numero di volte che A si verifica su n prove indipendenti.

**Proprietà derivate:**

1. **Complementare**: $P(A^c) = 1 - P(A)$
2. **Unione**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
3. **Differenza**: $P(A \setminus B) = P(A) - P(A \cap B)$
4. **Incompatibili**: Se $A \cap B = \emptyset$, allora $P(A \cup B) = P(A) + P(B)$

**Limiti di questo approccio:**
- Circolarità: indipendenza è concetto probabilistico
- Convergenza non specificata
- Validità non garantita in generale

## 2.5 Algebra di Eventi

La probabilità deve essere definita su una famiglia di sottoinsiemi chiusa rispetto alle operazioni.

**Definizione: Algebra**

Una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$ è un'**algebra** se:
1. **Chiusura per unione**: se $A, B \in \mathcal{E}$, allora $A \cup B \in \mathcal{E}$
2. **Chiusura per complemento**: se $A \in \mathcal{E}$, allora $A^c \in \mathcal{E}$

**Conseguenza (De Morgan):** L'algebra è anche chiusa per intersezione e differenza.

**Esempio:** Dado, evento A = "pari". L'algebra minima contenente A è:
$$\mathcal{E}_{\min} = \{\emptyset, \Omega, A, A^c\} = \{\emptyset, \Omega, \{2,4,6\}, \{1,3,5\}\}$$

## 2.6 σ-Algebra

**Definizione: σ-algebra**

Un'algebra che è chiusa anche per **unioni numerabili**:

$$A_1, A_2, A_3, \ldots \in \mathcal{E} \Rightarrow \bigcup_{i=1}^{\infty} A_i \in \mathcal{E}$$

**Quando serve:** Quando $\Omega$ è numerabile (come il numero di pacchetti in coda).

## 2.7 Spazio di Probabilità e Assiomi di Kolmogorov

**Definizione: Legge di Probabilità**

Una funzione $P: \mathcal{E} \to [0,1]$ è una legge di probabilità se soddisfa gli **assiomi di Kolmogorov**:

**Assioma 1 — Non negatività:**
$$P(A) \geq 0 \quad \forall A \in \mathcal{E}$$

**Assioma 2 — Normalizzazione:**
$$P(\Omega) = 1$$

**Assioma 3 — Additività:**
Se $A, B$ disgiunti ($A \cap B = \emptyset$):
$$P(A \cup B) = P(A) + P(B)$$

**Assioma 3½ — σ-Additività:**
Se $\{A_i\}_{i=1}^{\infty}$ a due a due disgiunti:
$$P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

**Spazio di Probabilità:** La terna $(\Omega, \mathcal{E}, P)$.

## 2.8 Proprietà Derivate dagli Assiomi

Tutte le proprietà intuitivamente giuste discendono dai soli assiomi.

**Probabilità dell'impossibile:**
$$P(\emptyset) = 0$$

**Probabilità del complementare:**
$$P(A^c) = 1 - P(A)$$

**Monotonia:**
Se $A \subseteq B$, allora $P(A) \leq P(B)$

**Unione (subadditività):**
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

---

# Capitolo 3 — Probabilità Condizionata e Bayes

*(Lezioni 2-3)*

## 3.1 Probabilità Condizionata

Spesso vogliamo calcolare la probabilità di un evento A **dato che sappiamo** che l'evento B si è verificato.

**Intuizione:** Restringuiamo lo spazio ai soli esiti in B e chiediamo quale frazione soddisfa A.

**Definizione:**
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

**Legge della Probabilità Composta:**
$$P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)$$

**Esempi:**
- Dado: A = "esce 6", B = "esce pari"
  - $P(A \cap B) = P(\{6\}) = 1/6$
  - $P(B) = 3/6 = 1/2$
  - $P(A \mid B) = (1/6) / (1/2) = 1/3$ ✓ (su 3 pari, solo il 6)

## 3.2 Legge di Bayes

Dalla legge della probabilità composta, invertendo il condizionamento:

$$P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$$

**Terminologia:**
- $P(B)$: probabilità **a priori** (prima dell'evidenza)
- $P(A \mid B)$: **likelihood** (verosimiglianza)
- $P(B \mid A)$: probabilità **a posteriori** (dopo l'evidenza)

**Significato:** Usa la nuova evidenza A per aggiornare le credenze su B.

**Esempio — Test medico:**
- $B$ = "ha malattia"
- $A$ = "test positivo"
- $P(B)$ = 0.01 (1% della popolazione ha la malattia)
- $P(A \mid B)$ = 0.99 (sensibilità: 99% dei malati testano positivo)
- $P(A \mid B^c)$ = 0.05 (5% dei sani testano positivo per errore)

**Calcolo:**
$$P(A) = P(A \mid B) P(B) + P(A \mid B^c) P(B^c) = 0.99 \cdot 0.01 + 0.05 \cdot 0.99 = 0.0594$$

$$P(B \mid A) = \frac{0.99 \cdot 0.01}{0.0594} = 0.1667$$

**→ Anche con test positivo, probabilità reale di malattia è solo ~17%!**

## 3.3 Legge della Probabilità Totale

Se gli eventi $E_1, E_2, \ldots, E_m$ formano una **partizione** di $\Omega$ (sono disgiunti e coprono tutto):

$$P(A) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)$$

**Uso:** Scomponi il calcolo difficile in calcoli più semplici su casi particolari.

**Esempio — Controllo qualità:**
- 60% pezzi da fornace A, 40% da fornace B
- A ha tasso difetti 2%, B ha tasso 5%
- Probabilità pezzo difettoso:

$$P(\text{difetto}) = P(\text{difetto} \mid A) P(A) + P(\text{difetto} \mid B) P(B)$$
$$= 0.02 \cdot 0.6 + 0.05 \cdot 0.4 = 0.032 = 3.2\%$$

---

# Capitolo 4 — Indipendenza Stocastica

*(Lezione 3)*

## 4.1 Definizione di Indipendenza

**Definizione:** Due eventi A e B sono **statisticamente indipendenti** se:

$$P(A \cap B) = P(A) \cdot P(B)$$

**Interpretazione:** Sapere che B si è verificato **non cambia** la probabilità di A:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A) P(B)}{P(B)} = P(A)$$

## 4.2 Indipendenza dei Complementari

**Teorema:** Se A e B sono indipendenti, allora:
- $A^c$ e $B$ sono indipendenti
- $A$ e $B^c$ sono indipendenti  
- $A^c$ e $B^c$ sono indipendenti

## 4.3 Indipendenza di n Eventi

$n$ eventi $A_1, A_2, \ldots, A_n$ sono **mutuamente indipendenti** se per ogni sottoinsieme $\{i_1, i_2, \ldots, i_k\}$:

$$P(A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}) = P(A_{i_1}) \cdot P(A_{i_2}) \cdots P(A_{i_k})$$

**Attenzione:** Indipendenza a coppie $\neq$ indipendenza congiunta.

**Esempio — Bit di parità:**
- Tre bit $X_1, X_2, X_3$, tutti indipendenti, equiprobabili
- $A_1$ = "$X_1 = 1$", $A_2$ = "$X_2 = 1$", $A_3$ = "$X_1 \oplus X_2 = 1$" (XOR)
- $P(A_1) = P(A_2) = P(A_3) = 1/2$
- $P(A_1 \cap A_2) = 1/4 = P(A_1) P(A_2)$ ✓
- $P(A_1 \cap A_3) = 1/4 = P(A_1) P(A_3)$ ✓
- $P(A_2 \cap A_3) = 1/4 = P(A_2) P(A_3)$ ✓
- **MA** $P(A_1 \cap A_2 \cap A_3) = 0 \neq P(A_1) P(A_2) P(A_3) = 1/8$ ✗

→ Indipendenza a coppie ma non congiunta!

---

# PARTE II — Variabili Aleatorie Discrete

---

# Capitolo 5 — Variabili Aleatorie Discrete e PMF

*(Lezioni 3-4)*

## 5.1 Definizione di Variabile Aleatoria

Una **variabile aleatoria** X è una funzione che assegna a ogni esito elementare $\omega \in \Omega$ un valore numerico:

$$X: \Omega \to \mathbb{R}$$

**Esempio:**
- Lancio due monete: $\Omega = \{TT, TC, CT, CC\}$
- X = numero di teste: $X(TT) = 2, X(TC) = 1, X(CT) = 1, X(CC) = 0$

## 5.2 Variabili Aleatorie Discrete

Una variabile aleatoria è **discreta** se può assumere un insieme **finito o numerabile** di valori.

$$\mathcal{X} = \{a_1, a_2, \ldots\} \subseteq \mathbb{R}$$

L'insieme $\mathcal{X}$ si chiama **alfabeto** di X.

## 5.3 Probability Mass Function (PMF)

La **PMF** di X è la funzione che associa a ogni valore la probabilità:

$$P_X(x) = P(X = x) = P(\{\omega \in \Omega : X(\omega) = x\})$$

**Proprietà (conseguenza degli assiomi):**

1. $P_X(x) \geq 0$ per ogni $x \in \mathcal{X}$
2. $\sum_{x \in \mathcal{X}} P_X(x) = 1$ (normalizzazione)

**Esempio — Lancio dado onesto:**
$$P_X(x) = \begin{cases} 1/6 & \text{se } x \in \{1,2,3,4,5,6\} \\ 0 & \text{altrimenti} \end{cases}$$

## 5.4 Cumulative Distribution Function (CDF)

La **CDF** è la probabilità cumulativa:

$$F_X(x) = P(X \leq x) = \sum_{a \leq x} P_X(a)$$

**Proprietà:**
- $F_X$ è non-decrescente
- $F_X(-\infty) = 0$, $F_X(+\infty) = 1$
- $P(a < X \leq b) = F_X(b) - F_X(a)$

---

# Capitolo 6 — Valore Atteso e Momenti

*(Lezioni 4-5)*

## 6.1 Valore Atteso (Media Statistica)

**Motivazione:** La **media campionaria** converge (per legge dei grandi numeri) a:

$$E[X] = \sum_{x \in \mathcal{X}} x \cdot P_X(x)$$

**Definizione: Valore Atteso**

$$\boxed{E[X] = \mu_X = \sum_{x} x \cdot P_X(x)}$$

**Interpretazione:** È il "baricentro" della distribuzione di probabilità, il valore verso cui converge la media campionaria quando il numero di osservazioni tende a infinito.

**Proprietà di linearità (cruciale):**

$$E[aX + bY] = aE[X] + bE[Y]$$

Questa proprietà vale indipendentemente dall'indipendenza di X e Y!

**Esempio:**
- Dado equo: $E[X] = 1 \cdot (1/6) + 2 \cdot (1/6) + \cdots + 6 \cdot (1/6) = (1+2+\cdots+6)/6 = 21/6 = 3.5$

## 6.2 Varianza

La **varianza** misura quanto i valori si disperso attorno alla media.

**Definizione:**
$$\text{Var}(X) = E[(X - \mu_X)^2] = E[X^2] - (E[X])^2$$

**Formula alternativa (più facile computazione):**
$$\text{Var}(X) = E[X^2] - \mu_X^2$$

dove $E[X^2] = \sum_x x^2 P_X(x)$.

**Proprietà:**
- $\text{Var}(aX + b) = a^2 \text{Var}(X)$
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ **se X, Y indipendenti**

## 6.3 Deviazione Standard

$$\sigma_X = \sqrt{\text{Var}(X)}$$

Ha le stesse unità di X (a differenza della varianza).

## 6.4 Momenti

Il **k-esimo momento** è:
$$E[X^k] = \sum_x x^k P_X(x)$$

Il **k-esimo momento centrale** è:
$$E[(X - \mu)^k] = \sum_x (x - \mu)^k P_X(x)$$

**Uso:** Il 3° momento centrale (diviso per $\sigma^3$) misura l'asimmetria (**skewness**); il 4° misura la "pesantezza delle code" (**kurtosis**).

---

# Capitolo 7 — Distribuzioni Discrete Notevoli

*(Lezioni 4-5)*

## 7.1 Distribuzione di Bernoulli

**Definizione:** Una prova con due soli esiti: successo (1) e fallimento (0).

$$X \sim \text{Ber}(p), \quad p \in [0,1]$$

**PMF:**
$$P_X(x) = \begin{cases} p & \text{se } x = 1 \\ 1-p & \text{se } x = 0 \end{cases} = p^x(1-p)^{1-x}$$

**Media e Varianza:**
- $E[X] = p$
- $\text{Var}(X) = p(1-p)$

**Esempi:** Lancio moneta, singolo clic pubblicità, singolo test medico.

## 7.2 Distribuzione Binomiale

**Definizione:** Numero di successi in $n$ prove **indipendenti** di Bernoulli.

$$S_n = X_1 + X_2 + \cdots + X_n, \quad X_i \sim \text{Ber}(p)$$

$$S_n \sim \text{Bin}(n,p)$$

**PMF:**
$$P_{S_n}(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

**Interpretazione combinatoria:**
- $\binom{n}{k}$ = numero di sequenze di n prove con esattamente k successi
- $p^k(1-p)^{n-k}$ = probabilità di ciascuna sequenza

**Media e Varianza:**
- $E[S_n] = np$
- $\text{Var}(S_n) = np(1-p)$

**Derivazione della media (metodo 1 — linearità):**
$$E[S_n] = E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i] = np$$

**Verifica normalizzazione (binomio di Newton):**
$$\sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} = (p + (1-p))^n = 1$$

**Esempio:** Test vaccino, p=0.95, n=1000 vaccinati
- Numero atteso di protetti: $E[S] = 1000 \cdot 0.95 = 950$

## 7.3 Distribuzione Uniforme Discreta

**Definizione:** Tutti i valori dell'alfabeto $\mathcal{X} = \{a_1, \ldots, a_M\}$ sono equiprobabili.

$$P_X(a_k) = \frac{1}{M} \quad \forall k$$

**Media:**
$$E[X] = \frac{a_1 + a_2 + \cdots + a_M}{M}$$

(media aritmetica dell'alfabeto)

**Caso particolare:** $\mathcal{X} = \{1, 2, \ldots, M\}$

$$E[X] = \sum_{k=1}^M k \cdot \frac{1}{M} = \frac{1}{M} \cdot \frac{M(M+1)}{2} = \frac{M+1}{2}$$

**Formula di Gauss:** $\sum_{k=1}^M k = \frac{M(M+1)}{2}$

**Varianza:**
$$\text{Var}(X) = \frac{M^2 - 1}{12}$$

**Esempi:** Dado equo, scelta casuale uniforme da un insieme.

## 7.4 Distribuzione di Poisson

**Contesto:** Conta eventi rari in un intervallo di tempo/spazio fisso.

**Definizione:** Parametro $\lambda > 0$

$$X \sim \text{Poi}(\lambda)$$

**PMF:**
$$P_X(k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$

**Verifica normalizzazione (serie esponenziale):**
$$\sum_{k=0}^\infty P_X(k) = e^{-\lambda} \sum_{k=0}^\infty \frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^\lambda = 1$$

**Media e Varianza:**
- $E[X] = \lambda$
- $\text{Var}(X) = \lambda$

(La Poisson ha media = varianza!)

**Approssimazione della Binomiale:** Se $n \to \infty$, $p \to 0$, ma $np = \lambda$ costante:
$$\text{Bin}(n,p) \approx \text{Poi}(np)$$

**Esempi:**
- Numero di client che arrivano a un'agenzia in un'ora
- Numero di errori di trasmissione su un canale
- Numero di difetti in un pezzo di tessuto

**Applicazione pratica:** Se conosci $\lambda$ (tasso medio), puoi calcolare probabilità di osservare k eventi.

## 7.5 Distribuzione Geometrica

**Contesto:** Numero di prove prima del primo successo in prove Bernoulli indipendenti.

**Definizione:**
$$X = \text{numero di prove fino al primo successo}$$

**PMF:**
$$P_X(k) = (1-p)^{k-1} \cdot p, \quad k = 1, 2, 3, \ldots$$

**Interpretazione:** k-1 fallimenti seguiti da 1 successo.

**Media:**
$$E[X] = \frac{1}{p}$$

Derivazione: $E[X] = \sum_{k=1}^\infty k (1-p)^{k-1} p = p \sum_{k=1}^\infty k (1-p)^{k-1}$.

Usando la serie $\sum_{k=1}^\infty k x^{k-1} = \frac{1}{(1-x)^2}$:

$$E[X] = p \cdot \frac{1}{(1-(1-p))^2} = p \cdot \frac{1}{p^2} = \frac{1}{p}$$

**Varianza:**
$$\text{Var}(X) = \frac{1-p}{p^2}$$

**Proprietà "memoryless" (assenza di memoria):**
$$P(X > n+k \mid X > n) = P(X > k)$$

Il futuro non dipende da quanto tempo è già passato!

**Esempio:** Quanti lanci di una moneta (p=0.5) prima di ottenere testa?
- Aspettativa: $E[X] = 1/0.5 = 2$ lanci

---

# Capitolo 8 — Funzioni di Variabili Aleatorie

*(Lezione 5-6)*

## 8.1 Trasformazione di una Variabile Aleatoria

Se X è una variabile aleatoria e $g: \mathbb{R} \to \mathbb{R}$ è una funzione, allora $Y = g(X)$ è ancora una variabile aleatoria.

**Problema:** Data PMF di X, trovare PMF di Y.

## 8.2 Caso: Funzione Invertibile

Se $g$ è **invertibile** (uno-a-uno), allora per ogni valore $y$ esiste un unico $x$ tale che $y = g(x)$:

$$P_Y(y) = P_X(g^{-1}(y))$$

**Esempio:** $X \sim \text{Uni}\{0,1,2\}$, $Y = 2X$

- $P_Y(0) = P_X(0) = 1/3$
- $P_Y(2) = P_X(1) = 1/3$
- $P_Y(4) = P_X(2) = 1/3$

## 8.3 Caso: Funzione Non Invertibile

Se più valori di X danno lo stesso Y, sommiamo le probabilità:

$$P_Y(y) = \sum_{x: g(x) = y} P_X(x)$$

**Esempio:** $X \sim \text{Uni}\{-1, 0, 1\}$, $Y = X^2$

- $P_Y(0) = P_X(0) = 1/3$
- $P_Y(1) = P_X(-1) + P_X(1) = 1/3 + 1/3 = 2/3$

## 8.4 Valore Atteso di una Funzione di Variabile Aleatoria

**Formula (LOTUS — Law Of The Unconscious Statistician):**

$$E[g(X)] = \sum_x g(x) P_X(x)$$

NON devi calcolare PMF di Y: puoi calcolarlo direttamente dalla PMF di X!

**Esempi:**
- $E[X^2] = \sum_x x^2 P_X(x)$
- $E[e^{tX}] = \sum_x e^{tx} P_X(x)$ (funzione generatrice dei momenti)

---

# PARTE III — Disuguaglianze e Convergenza

---

# Capitolo 9 — Disuguaglianze di Probabilità

*(Lezione 7)*

## 9.1 Disuguaglianza di Markov

**Teorema:** Per una variabile aleatoria **non-negativa** $X \geq 0$ e $a > 0$:

$$P(X \geq a) \leq \frac{E[X]}{a}$$

**Intuizione:** Se la media è piccola, la probabilità di valori grandi è piccola.

**Esempio:** Numero medio di errori = 10. Probabilità di ≥ 100 errori è al massimo 10/100 = 0.1 (10%).

## 9.2 Disuguaglianza di Chebyshev

**Teorema:** Per qualunque variabile aleatoria X e $k > 0$:

$$P(|X - E[X]| \geq k\sigma) \leq \frac{1}{k^2}$$

dove $\sigma = \sqrt{\text{Var}(X)}$.

**Forme equivalenti:**
- $P(|X - \mu| \geq \epsilon) \leq \frac{\sigma^2}{\epsilon^2}$
- Almeno $(1 - 1/k^2)$ della probabilità è entro $k\sigma$ dalla media

**Esempi numerici:**
- $k=2$: almeno 75% della probabilità entro 2 deviazioni standard
- $k=3$: almeno 89% della probabilità entro 3 deviazioni standard

**Validità generale:** A differenza della gaussiana, Chebyshev funziona per **qualunque** distribuzione!

## 9.3 Disuguaglianza di Hoeffding (e Chernoff)

Per somme di variabili aleatorie indipendenti e limitate, convergono ancora più rapidamente.

$$P\left(\left|\frac{S_n}{n} - \mu\right| \geq \epsilon\right) \leq 2 \exp\left(-2n\epsilon^2/(b-a)^2\right)$$

La probabilità **decresce esponenzialmente** con n.

---

# Capitolo 10 — Legge dei Grandi Numeri

*(Lezione 8)*

## 10.1 Convergenza in Probabilità

Una successione di variabili aleatorie $X_1, X_2, \ldots$ **converge in probabilità** a un valore $c$ se:

$$\lim_{n \to \infty} P(|X_n - c| > \epsilon) = 0 \quad \forall \epsilon > 0$$

Si scrive: $X_n \xrightarrow{P} c$ oppure $\text{plim} X_n = c$.

## 10.2 Legge Debole dei Grandi Numeri (WLLN)

**Teorema:** Siano $X_1, X_2, \ldots$ variabili aleatorie **i.i.d.** (indipendenti, stessa distribuzione) con media $\mu$ e varianza finita. La media campionaria:

$$\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$$

converge in probabilità a $\mu$:

$$\bar{X}_n \xrightarrow{P} \mu$$

**Dimostrazione (via Chebyshev):**
- $E[\bar{X}_n] = \mu$
- $\text{Var}(\bar{X}_n) = \frac{\sigma^2}{n}$

Per Chebyshev:
$$P(|\bar{X}_n - \mu| \geq \epsilon) \leq \frac{\sigma^2}{n\epsilon^2} \to 0 \text{ quando } n \to \infty$$

## 10.3 Legge Forte dei Grandi Numeri (SLLN)

**Convergenza quasi sicura:** $X_n \xrightarrow{a.s.} c$ significa

$$P\left(\lim_{n \to \infty} X_n = c\right) = 1$$

**Teorema (SLLN):** Sotto le stesse ipotesi di WLLN:

$$\bar{X}_n \xrightarrow{a.s.} \mu$$

Con probabilità 1, la media campionaria converge a $\mu$.

**Differenza WLLN vs SLLN:**
- WLLN: singoli $\bar{X}_n$ si avvicinano a $\mu$
- SLLN: l'intera sequenza converge

SLLN è più forte.

## 10.4 Significato per l'Inferenza Statistica

La LGN giustifica il passaggio da **frequenza empirica** a **probabilità teorica**:

$$f_n(A) = \frac{N_A}{n} \xrightarrow{P} P(A)$$

Quando il campione è grande, la frequenza osservata è una stima affidabile della vera probabilità.

**Implicazione:** La statistica descrittiva su grandi dataset ha senso!

---

# PARTE IV — Coppie e n-uple di Variabili Aleatorie Discrete

---

# Capitolo 11 — PMF Congiunta e Indipendenza

*(Lezioni 9-10)*

## 11.1 Distribuzione Congiunta

Dati due variabili aleatorie X e Y (possibilmente su spazi diversi), la **PMF congiunta** è:

$$P_{X,Y}(x,y) = P(X = x, Y = y)$$

**Proprietà:**
- $P_{X,Y}(x,y) \geq 0$
- $\sum_x \sum_y P_{X,Y}(x,y) = 1$

## 11.2 Distribuzioni Marginali

Sommando sulla seconda variabile:

$$P_X(x) = \sum_y P_{X,Y}(x,y)$$

$$P_Y(y) = \sum_x P_{X,Y}(x,y)$$

Si recuperano le distribuzioni individuali.

## 11.3 PMF Condizionata

$$P_{X \mid Y}(x \mid y) = \frac{P_{X,Y}(x,y)}{P_Y(y)}, \quad P_Y(y) > 0$$

## 11.4 Indipendenza

X e Y sono **indipendenti** se:

$$P_{X,Y}(x,y) = P_X(x) \cdot P_Y(y) \quad \forall x, y$$

Equivalentemente: $P_{X \mid Y}(x \mid y) = P_X(x)$ (sapere Y non cambia X).

---

# Capitolo 12 — Covarianza, Correlazione e Media Condizionale

*(Lezione 10)*

## 12.1 Covarianza

$$\text{Cov}(X,Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$

**Proprietà:**
- Se X, Y indipendenti, allora $\text{Cov}(X,Y) = 0$ (ma non viceversa!)
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$

## 12.2 Correlazione

$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sqrt{\text{Var}(X) \text{Var}(Y)}} \in [-1, 1]$$

- $\rho = 1$: correlazione positiva perfetta
- $\rho = -1$: correlazione negativa perfetta
- $\rho = 0$: non correlati (ma potrebbero non essere indipendenti!)

## 12.3 Media Condizionale (Regressione)

$$E[Y \mid X = x] = \sum_y y \cdot P_{Y \mid X}(y \mid x)$$

**Proprietà torre (law of iterated expectations):**

$$E[Y] = E[E[Y \mid X]]$$

Si calcola prima la media condizionale dato X, poi si integra (prende media) su X.

---

# PARTE V — Variabili Aleatorie Continue

---

# Capitolo 13 — Variabili Continue: CDF e PDF

*(Lezioni 11-12)*

## 13.1 Variabili Aleatorie Continue

Una variabile aleatoria è **continua** se il suo spazio è un intervallo $[a,b]$ o $\mathbb{R}$.

**Cruciale:** $P(X = x) = 0$ per ogni singolo punto x (probabilità concentrata su insiemi innumerevoli).

## 13.2 Cumulative Distribution Function (CDF)

$$F_X(x) = P(X \leq x)$$

**Proprietà:**
- Non-decrescente
- $F_X(-\infty) = 0$, $F_X(+\infty) = 1$
- Continua a destra

## 13.3 Probability Density Function (PDF)

La **PDF** è la derivata della CDF:

$$f_X(x) = \frac{dF_X(x)}{dx}$$

**Proprietà:**
- $f_X(x) \geq 0$
- $\int_{-\infty}^{+\infty} f_X(x) dx = 1$ (normalizzazione)
- $P(a < X \leq b) = \int_a^b f_X(x) dx$

**Nota:** $f_X(x)$ è una **densità**, non una probabilità. $f_X(x) dx$ è la probabilità infinitesimale di un intervallino.

## 13.4 Valore Atteso e Varianza

$$E[X] = \int_{-\infty}^{+\infty} x f_X(x) dx$$

$$\text{Var}(X) = E[X^2] - (E[X])^2, \quad E[X^2] = \int_{-\infty}^{+\infty} x^2 f_X(x) dx$$

---

# Capitolo 14 — Distribuzioni Continue Notevoli

*(Lezioni 12-13)*

## 14.1 Distribuzione Uniforme Continua

**Definizione:** Su un intervallo $[a, b]$

$$X \sim \text{Uni}(a,b)$$

**PDF:**
$$f_X(x) = \begin{cases} \frac{1}{b-a} & \text{se } a \leq x \leq b \\ 0 & \text{altrimenti} \end{cases}$$

**Media:**
$$E[X] = \frac{a+b}{2}$$

**Varianza:**
$$\text{Var}(X) = \frac{(b-a)^2}{12}$$

## 14.2 Distribuzione Esponenziale

**Contesto:** Tempo di attesa per il primo evento in un processo Poisson.

**Definizione:** Parametro $\lambda > 0$

$$X \sim \text{Exp}(\lambda)$$

**PDF:**
$$f_X(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

**Media:**
$$E[X] = \frac{1}{\lambda}$$

**Varianza:**
$$\text{Var}(X) = \frac{1}{\lambda^2}$$

**Proprietà memoryless:**
$$P(X > s+t \mid X > s) = P(X > t)$$

Il futuro non dipende dal passato!

**CDF:**
$$F_X(x) = 1 - e^{-\lambda x}$$

## 14.3 Distribuzione Normale (Gaussiana)

**Distribuzione più importante in statistica!**

**Definizione:** Parametri $\mu \in \mathbb{R}$, $\sigma > 0$

$$X \sim \mathcal{N}(\mu, \sigma^2)$$

**PDF:**
$$f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

**Media e Varianza:**
- $E[X] = \mu$
- $\text{Var}(X) = \sigma^2$

**Proprietà:**
- Simmetrica attorno a $\mu$
- ~68% della probabilità entro $\mu \pm \sigma$
- ~95% entro $\mu \pm 2\sigma$
- ~99.7% entro $\mu \pm 3\sigma$

**Standarizzazione:** $Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0,1)$

Permette di tabellare una sola gaussiana (standard).

**Somma di gaussiane:** Se $X_i \sim \mathcal{N}(\mu_i, \sigma_i^2)$ indipendenti:

$$\sum_{i=1}^n a_i X_i \sim \mathcal{N}\left(\sum a_i \mu_i, \sum a_i^2 \sigma_i^2\right)$$

## 14.4 Distribuzione Chi-Quadrato

**Definizione:** Somma dei quadrati di k gaussiane standard indipendenti

$$\chi^2_k = Z_1^2 + Z_2^2 + \cdots + Z_k^2, \quad Z_i \sim \mathcal{N}(0,1)$$

**Media:** $E[\chi^2_k] = k$

**Varianza:** $\text{Var}(\chi^2_k) = 2k$

**Uso:** Test di ipotesi, intervalli di confidenza per varianze.

## 14.5 Distribuzione t di Student

**Contesto:** Quando la varianza è sconosciuta, la statistica test segue una t.

**Definizione:** Parametro $\nu$ (gradi di libertà)

$$T_\nu = \frac{Z}{\sqrt{\chi^2_\nu / \nu}}$$

dove $Z \sim \mathcal{N}(0,1)$ e $\chi^2_\nu$ sono indipendenti.

**Proprietà:**
- Simmetrica attorno a 0
- Code più pesanti della normale
- Per $\nu \to \infty$: $T_\nu \to \mathcal{N}(0,1)$

---

# Capitolo 15 — PDF Condizionata e Variabili Continue Bivariate

*(Lezione 14)*

## 15.1 PDF Condizionata

$$f_{X \mid Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}, \quad f_Y(y) > 0$$

## 15.2 PDF Congiunta

Data PDF congiunta $f_{X,Y}(x,y)$, le marginali sono:

$$f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y) dy$$

$$f_Y(y) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y) dx$$

## 15.3 Indipendenza

X e Y continui indipendenti ⟺

$$f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$$

---

# PARTE VI — Argomenti Avanzati

---

# Capitolo 16 — Canale Binario Simmetrico ed Entropia di Shannon

*(Lezione 15)*

## 16.1 Canale Binario Simmetrico (BSC)

Un **canale** è un sistema di comunicazione con:
- Input X ∈ {0,1}
- Output Y ∈ {0,1}
- Probabilità di errore p

**Modello:** Con probabilità p, il bit si inverte; con probabilità 1-p, passa inalterato.

$$P(Y = 0 \mid X = 1) = p$$
$$P(Y = 1 \mid X = 0) = p$$

## 16.2 Entropia di Shannon

L'**entropia** misura l'incertezza di una variabile aleatoria.

**Definizione:**
$$H(X) = -\sum_x P(x) \log_2 P(x)$$

(il log è in base 2, unità = bit)

**Proprietà:**
- $H(X) \geq 0$
- $H(X) = 0$ ⟺ X è deterministica
- $H(X)$ massima quando X è uniforme

**Interpretazione:** Numero medio di bit necessario per codificare X.

## 16.3 Entropia Congiunta e Condizionata

$$H(X,Y) = -\sum_x \sum_y P(x,y) \log P(x,y)$$

$$H(X \mid Y) = \sum_y P(y) H(X \mid Y=y)$$

**Chain rule:**
$$H(X,Y) = H(Y) + H(X \mid Y)$$

## 16.4 Informazione Mutua

$$I(X;Y) = H(X) - H(X \mid Y)$$

Misura quanto Y dice su X.

**Proprietà:**
- $I(X;Y) \geq 0$
- $I(X;Y) = I(Y;X)$ (simmetria)
- $I(X;Y) = 0$ ⟺ X, Y indipendenti

## 16.5 Capacità del Canale

La **capacità** di un canale è il massimo di informazione che può essere trasmesso in modo affidabile.

$$C = \max_P I(X;Y)$$

dove il massimo è su tutte le distribuzioni possibili dell'input X.

**Per BSC:**
$$C = 1 - H(p) \text{ bit}$$

dove $H(p) = -p \log_2 p - (1-p) \log_2(1-p)$ è l'entropia binaria.

**Esempio:**
- $p = 0$: $C = 1$ bit (nessun errore, puoi trasmettere tutto)
- $p = 0.5$: $C = 0$ bit (il canale inverte casualmente, inutile)
- $p = 0.1$: $C \approx 0.53$ bit

---

# Capitolo 17 — Vettori Aleatori, Convoluzione e Teorema Centrale del Limite

*(Lezione 16)*

## 17.1 Vettore Aleatorio

Un **vettore aleatorio** è un vettore di variabili aleatorie:

$$\mathbf{X} = (X_1, X_2, \ldots, X_n)$$

**PMF congiunta (caso discreto):**
$$P_{\mathbf{X}}(\mathbf{x}) = P(X_1 = x_1, X_2 = x_2, \ldots, X_n = x_n)$$

**PDF congiunta (caso continuo):**
$$f_{\mathbf{X}}(\mathbf{x}) = f(x_1, x_2, \ldots, x_n)$$

## 17.2 Somma di Variabili Aleatorie Indipendenti

Se $S = X_1 + X_2 + \cdots + X_n$ con $X_i$ i.i.d., la PDF/PMF di S è dato dalla **convoluzione**.

**Caso discreto:**
$$P_S(s) = \sum_x P_{X_1}(x) P_{X_2}(s-x)$$

(per n=2)

**Caso continuo:**
$$f_S(s) = \int_{-\infty}^{+\infty} f_{X_1}(x) f_{X_2}(s-x) dx$$

## 17.3 Teorema Centrale del Limite (CLT)

**Teorema (versione semplice):** Sia $X_1, X_2, \ldots$ una sequenza di v.a. **i.i.d.** con media $\mu$ e varianza $\sigma^2 < \infty$. Allora:

$$\frac{S_n - n\mu}{\sqrt{n}\sigma} = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)$$

dove $\xrightarrow{d}$ significa convergenza in distribuzione.

**Interpretazione:** La media campionaria di un campione grande è approssimativamente normale, **indipendentemente dalla distribuzione originale**!

**Formula pratica:** Per n grande:

$$\bar{X}_n \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$

**Importanza:** Giustifica l'uso della gaussiana nella statistica, anche quando la popolazione non è normale!

**Quand'è "grande"?**
- Se popolazione è simmetrica: n ≥ 30
- Se popolazione è skewed: n ≥ 100-200
- Se popolazione è uniform: n ≥ 10

---

# Capitolo 18 — Processi Stocastici

*(Lezione 17-18)*

## 18.1 Definizione di Processo Stocastico

Un **processo stocastico** è una raccolta di variabili aleatorie indicizzate dal tempo (o spazio):

$$\{X_t\}_{t \in T}$$

dove T è generalmente $\mathbb{N}_0$ (tempo discreto) o $[0, \infty)$ (tempo continuo).

**Interpretazione:** Ad ogni istante t, la variabile $X_t$ rappresenta lo stato del sistema.

## 18.2 Catene di Markov Discrete

Una **catena di Markov** è un processo stocastico **senza memoria**:

$$P(X_{n+1} = j \mid X_n = i, X_{n-1}, \ldots, X_0) = P(X_{n+1} = j \mid X_n = i)$$

Il futuro dipende **solo dallo stato presente**, non dalla storia.

**Matrice di transizione:** Stato da i a j con probabilità $P_{ij}$.

$$\mathbf{P} = \begin{pmatrix} P_{11} & P_{12} & \cdots \\ P_{21} & P_{22} & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}$$

Ogni riga è una PMF (somma a 1).

## 18.3 Distribuzione Stazionaria

Una distribuzione $\boldsymbol{\pi}$ è **stazionaria** se:

$$\boldsymbol{\pi}^T \mathbf{P} = \boldsymbol{\pi}^T$$

Inoltre, se la catena è **aperiodica e irriducibile**, la distribuzione stazionaria è **unica** e:

$$\lim_{n \to \infty} P^n = \text{matrice con tutte le righe = } \boldsymbol{\pi}^T$$

## 18.4 Processi Poisson Continui

Un **processo di Poisson** è un processo stocastico a tempo continuo che conta il numero di eventi rari.

**Proprietà:**
- Incrementi stazionari: il numero di eventi in (t, t+s) dipende solo da s
- Incrementi indipendenti: numeri di eventi in intervalli disgiunti sono indipendenti
- Ogni incremento è Poisson: $X(t) \sim \text{Poi}(\lambda t)$

**Tempo tra arrivi:** Il tempo tra eventi consecutivi è esponenziale con parametro $\lambda$.

**Applicazioni:** Arrivi a un ufficio, crash di server, difetti in una corda, etc.

---

# Appendice A — Riepilogo Concetti Chiave

## A.1 Analisi Combinatoria

- **Prodotto cartesiano:** $n_1 \times n_2 \times \cdots \times n_k$
- **Disposizioni con ripetizione:** $n^k$
- **Disposizioni semplici:** $\frac{n!}{(n-k)!}$
- **Combinazioni:** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$
- **Coefficiente multinomiale:** $\frac{n!}{n_1! n_2! \cdots n_m!}$

## A.2 Probabilità di Base

- **Assiomi di Kolmogorov:** Non negatività, Normalizzazione, Additività
- **Complementare:** $P(A^c) = 1 - P(A)$
- **Unione:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Condizionata:** $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$
- **Bayes:** $P(B \mid A) = \frac{P(A \mid B) P(B)}{P(A)}$

## A.3 Distribuzioni Discrete Notevoli

| Distribuzione | PMF | Media | Varianza | Uso |
|---|---|---|---|---|
| **Bernoulli(p)** | $p^x(1-p)^{1-x}$ | $p$ | $p(1-p)$ | Singolo successo/fallimento |
| **Bin(n,p)** | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | Conteggio successi |
| **Poi($\lambda$)** | $\frac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ | Eventi rari |
| **Geom(p)** | $(1-p)^{k-1}p$ | $1/p$ | $(1-p)/p^2$ | Primo successo |

## A.4 Distribuzioni Continue Notevoli

| Distribuzione | PDF | Media | Varianza | Uso |
|---|---|---|---|---|
| **Uni(a,b)** | $\frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | Scelta uniforme |
| **Exp($\lambda$)** | $\lambda e^{-\lambda x}$ | $1/\lambda$ | $1/\lambda^2$ | Tempo di attesa |
| **N($\mu, \sigma^2$)** | $\frac{1}{\sqrt{2\pi\sigma^2}} e^{-(x-\mu)^2/(2\sigma^2)}$ | $\mu$ | $\sigma^2$ | Fenomeni naturali |

## A.5 Proprietà Fondamentali

- **Linearità del valore atteso:** $E[aX + bY] = aE[X] + bE[Y]$
- **Varianza della somma:** $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$
- **Se X, Y indipendenti:** $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$
- **Legge dei grandi numeri:** $\bar{X}_n \xrightarrow{P} E[X]$
- **Teorema centrale del limite:** $\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)$

## A.6 Informazione e Shannon

- **Entropia:** $H(X) = -\sum_x P(x) \log_2 P(x)$ (misura incertezza)
- **Informazione mutua:** $I(X;Y) = H(X) - H(X \mid Y)$
- **Capacità canale BSC:** $C = 1 - H(p)$ bit

---

# Appendice B — Tabelle di Riferimento Rapido

## B.1 Simboli Comuni

| Simbolo | Significato |
|---------|------------|
| $\Omega$ | Spazio dei campioni |
| $X$ | Variabile aleatoria |
| $P(A)$ | Probabilità di evento A |
| $E[X]$ | Valore atteso (media) |
| $\text{Var}(X)$ | Varianza |
| $\sigma$ | Deviazione standard |
| $\mathcal{N}(\mu,\sigma^2)$ | Distribuzione normale |
| $\sim$ | "segue distribuzione" |
| $\approx$ | "approssimativamente" |
| $\xrightarrow{P}$ | Converge in probabilità |

## B.2 Formule Algebriche Utili

- **Gauss:** $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$
- **Serie geometrica:** $\sum_{k=0}^{\infty} r^k = \frac{1}{1-r}$ per $|r| < 1$
- **Serie esponenziale:** $e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}$
- **Binomio Newton:** $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$

## B.3 Costanti Importanti

- $e \approx 2.71828$
- $\pi \approx 3.14159$
- $\sqrt{2} \approx 1.41421$

---

**Fine Appunti Completi - Metodi Statistici per l'Informazione**

*Documento completato: 23 Maggio 2026*  
*Basato su: 20 Lezioni Frontali + Slide Ufficiali + Libro Didattico*  
*Docente: Prof. Marco Lops*  
*Crediti: 6 CFU*

**Ultima revisione**: Capitoli 1-18 + Appendici A-B completamente espansi con definizioni, esempi, diagrammi, formule, e applicazioni pratiche.
