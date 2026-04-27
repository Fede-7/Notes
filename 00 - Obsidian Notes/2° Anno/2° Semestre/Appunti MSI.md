# Appunti MSI — Metodi Statistici per l'Informazione

> [!info] **Informazioni sul corso**
> - **Docente:** Prof. Marco Lops (Telecomunicazioni)
> - **CFU:** 6 (48 ore frontali — ~32 ore teoria + ~16 ore applicativa)
> - **Esame:** Prova scritta + colloquio rapido
> - **Testi:**
>   - Ernesto Conte, *Fenomeni Aleatori* (teoria della probabilità)
>   - Sheldon Ross, *Introduction to Probability and Statistics for Engineers and Scientists*
> - **Orari:** Martedì 14:00–16:00 · Giovedì 08:45–10:45

*Vedi anche:* [[MSI compacto]] per la sintesi compatta degli stessi argomenti.

---

# Capitolo 3 — Elements of Probability

## 3.1 Introduction

### Perché la probabilità per informatici e ingegneri dell'informazione?

Il filo conduttore del corso è la parola **informazione**. Sia le telecomunicazioni che l'informatica trattano questo oggetto: le telecomunicazioni si occupano di trasferirla da un luogo a un altro (usando onde elettromagnetiche), mentre l'informatica si occupa di trasferirla nel tempo (memorizzazione, compressione dati, correzione degli errori).

**Osservazione fondamentale:** se non c'è incertezza su ciò che viene trasmesso, non c'è informazione.

> **Esempio:** Una sorgente binaria che trasmette sempre zero o sempre uno non trasporta alcuna informazione — non c'è incertezza a priori su cosa la sorgente trasmetterà, quindi non ha senso né trasmetterla né memorizzarla.

Intrinseco nel concetto di informazione c'è il concetto di **incertezza**. L'incertezza è intrinsecamente probabilistica: l'intero processo di trasferimento si traduce nel trasformare un'**incertezza a priori** in una **certezza a posteriori**. Da questo deriva che tutto ciò che oggi si chiama *machine learning*, *statistical learning*, *deep learning* e reti neurali è costruito su questa base probabilistica.

> [!tip] **Nota del prof.:** "Se vi parlano di statistica dicendo che è un'altra cosa rispetto alla probabilità, vuol dire che non conoscono la probabilità. La probabilità è la base con cui si costruisce tutto il mondo della statistica."

### Struttura e programma del corso

Il corso è organizzato in sei grandi blocchi tematici:

1. **Analisi combinatoria** — imparare a contare in modo efficace (§3.4)
2. **Teoria della probabilità su spazi finiti** — definizione assiomatica di Kolmogorov, variabili aleatorie discrete (§3.2–3.8, §4)
3. **Estensione al continuo** — PDF, CDF, integrali al posto di somme (§5)
4. **Processi aleatori** — cenni necessari per le applicazioni
5. **Informazione e sua misura** — entropia di Shannon, mutua informazione, il bit come unità di misura
6. **Statistica** — descrittiva e **inferenziale**; teoria della decisione; test di ipotesi; stima bayesiana e non bayesiana (§6–9)

> [!important] **Distinzione fondamentale nella statistica:**
> - **Descrittiva:** ho una popolazione e ne calcolo statistiche globali. Interessante, ma limitata.
> - **Inferenziale:** elaborando un campione, inferisco le caratteristiche di qualunque altro campione statisticamente omogeneo con esso. È la base di tutti gli algoritmi di *learning*: un buon algoritmo funziona su qualunque campione con certi parametri, non solo su quello di addestramento.
>
> La statistica inferenziale si divide in **bayesiana** (i parametri da stimare hanno una distribuzione a priori nota) e **non bayesiana** (questa informazione a priori non è disponibile).

> [!note] **Nota:** Esiste un'integrazione profonda tra teoria dell'informazione e statistica inferenziale, formalizzata dal risultato di Kaila (anni '69–'71, riscoperto negli anni 2000).

---

## 3.2 Sample Space and Relationships Between Events

### Spazio dei campioni

> [!info] **Definizione: Esperimento**
> Un **esperimento** è un'operazione, o un insieme di operazioni, che conduce a uno tra tanti risultati possibili.

> [!info] **Definizione: Spazio dei campioni**
> Lo **spazio dei campioni** (*sample space*), indicato con $\Omega$, è l'insieme — non necessariamente numerico — di tutti i possibili risultati di un esperimento.

Lo spazio dei campioni può avere diverse nature:

| Tipo | Esempio |
|------|---------|
| **Finito** | Lancio di una moneta: $\Omega = \{T, C\}$ |
| **Infinito numerabile** | Numero di pacchetti in coda a un router: $\Omega = \mathbb{N}_0$ |
| **Continuo (non numerabile)** | Tensione ai capi di una resistenza (rumore termico): $\Omega = \mathbb{R}$ |

> [!note] **Sul continuo**
> Qualunque misura fisica è razionale (gli strumenti hanno un numero finito di cifre significative). Tuttavia, quando i valori possibili sono così numerosi, conviene modellarli come continui e poi applicare una troncatura numerica. Il tempo si schematizza quasi sempre come continuo.
>
> **Citazione del prof.:** *"Il discreto riempie la testa di idee, il continuo riempie la lavagna di formule. Ma se uno capisce bene le idee, le formule sono una conseguenza."*

**Esempi:**

- Lancio singolo di moneta: $\Omega = \{T, C\}$
- Lancio doppio di moneta: $\Omega = \{TT, TC, CT, CC\}$ — 4 elementi (l'ordine conta, è una sequenza temporale)
- Lancio di dado: $\Omega = \{1,2,3,4,5,6\}$, $|\Omega| = 6$
- Macchine su un'autostrada in un giorno (o pacchetti in coda a un router): $\Omega = \mathbb{N}_0 = \{0,1,2,\ldots\}$

### Definizione di Evento

> [!info] **Definizione: Evento**
> Un **evento** è un sottoinsieme di $\Omega$ definito da una proposizione.

> [!info] **Definizione: Evento elementare**
> Un **evento elementare** è un singolo elemento di $\Omega$.

**Proprietà cruciale:** Un evento è **univocamente determinato** dagli elementi di $\Omega$ che lo compongono, ma la **proposizione** che lo descrive **non è univoca** — la ridondanza del linguaggio naturale permette formulazioni diverse.

> **Esempio:** $\Omega = \{1,2,3,4,5\}$ (euro in tasca). L'evento $A = \{1,3,5\}$ può essere descritto come:
> - "Ho un numero dispari di euro in tasca"
> - "Non ho un numero pari di euro in tasca"
> - "Ho 1 euro, o 3 euro, o 5 euro"

> [!tip] **Strategia per gli esercizi**
> Risolvere un esercizio di probabilità su spazi discreti richiede spesso un unico vero sforzo: **riformulare la proposizione** che definisce l'evento in modo che la soluzione appaia chiara. Esempio classico: *"Qual è la probabilità che due persone in una classe di 30 abbiano lo stesso compleanno?"* — la chiave è riformulare la proposizione nel suo complementare.

### Nomenclatura degli eventi

| Nome | Simbolo | Definizione |
|------|---------|-------------|
| **Evento certo** | $\Omega$ | Si verifica sempre ad ogni esito |
| **Evento impossibile** | $\emptyset$ | Non si verifica mai |
| **Evento complementare** | $A^c$ o $\bar{A}$ | Tutti gli $\omega \in \Omega$ con $\omega \notin A$ |
| **Evento implicato** | $A \subseteq B$ | Il verificarsi di $A$ implica $B$, non viceversa |
| **Eventi incompatibili** | $A \cap B = \emptyset$ | Non possono verificarsi contemporaneamente |

**Esempi su lancio di dado:**
- "Esce 2" $= \{2\}$ implica "esce un numero pari" $= \{2,4,6\}$, ma non viceversa.

**Esempi su lancio doppio di moneta ($\Omega = \{TT, TC, CT, CC\}$):**
- "Esce almeno una croce" $D = \{TC, CT, CC\}$
- $D$ è **incompatibile** con $\{TT\}$ (esce testa-testa → nessuna croce)

**Esempi con $\Omega = \mathbb{N}_0$ (pacchetti):**
- "Meno di 6 pacchetti": $\{0,1,2,3,4,5\}$
- "Numero dispari di pacchetti": $\{1,3,5,7,\ldots\} = \{2k+1 \mid k \in \mathbb{N}_0\}$ — unione **numerabile** di eventi elementari
- "Numero pari **o** minore di 4": $\{0,1,2,3,4,6,8,\ldots\}$ — include 1 e 3 (dispari ma $< 4$) e 4 (pari e $\leq 4$)

### Algebra degli eventi — Richiami di teoria degli insiemi

Dati $m$ sottoinsiemi $A_1, A_2, \ldots, A_m$ di $\Omega$:

**Unione:** $A_1 \cup A_2$ — tutti gli elementi che appartengono ad almeno uno dei due insiemi (comuni contati una sola volta).

**Intersezione:** $A_1 \cap A_2$ — tutti e soli gli elementi comuni ad entrambi.

**Complemento:** $A_1^c$ — tutti gli elementi di $\Omega$ non in $A_1$.

**Sottrazione:** $A_1 \setminus A_2 = A_1 \cap A_2^c$ — gli elementi di $A_1$ che non appartengono ad $A_2$.

| Proprietà | Formula |
|-----------|---------|
| Doppio complemento | $(A^c)^c = A$ |
| Complemento di $\Omega$ | $\Omega^c = \emptyset$ |
| Unione con complementare | $A \cup A^c = \Omega$ |
| De Morgan (unione) | $(A \cup B)^c = A^c \cap B^c$ |
| De Morgan (intersezione) | $(A \cap B)^c = A^c \cup B^c$ |

> [!note] **$\sigma$-algebra**
> Quando $\Omega$ è infinito numerabile, la famiglia degli eventi deve essere una **$\sigma$-algebra**: chiusa non solo rispetto a unioni **finite**, ma rispetto a unioni **numerabili**. Questo è necessario per modellare eventi come $\{k \mid k \text{ dispari}\}$, che sono unioni infinite di eventi elementari.

---

## 3.3 Probability

**Non ancora trattato** formalmente in questa lezione. La definizione assiomatica di Kolmogorov verrà sviluppata nelle lezioni successive. *(Vedi [[MSI compacto]] §Axioms of Probability per la sintesi anticipata.)*

---

## 3.4 Sample Spaces Having Equally Likely Outcomes

### Motivazione e formula base

Quando lo spazio dei campioni è finito e gli eventi elementari sono tutti **equiprobabili**, la probabilità di un evento si calcola come:

$$P(A) = \frac{|A|}{|\Omega|}$$

Questo riduce il calcolo della probabilità a un problema di **conteggio**. La branca che si occupa di questo si chiama **analisi combinatoria** (o calcolo combinatorio).

### Approccio frequentistico (intuizione)

Prima della definizione formale, il prof. introduce la definizione **frequentistica**:

$$P(A) \approx \frac{N_A}{n} \xrightarrow{n \to \infty} \frac{|A|}{|\Omega|}$$

dove $N_A$ è il numero di occorrenze di $A$ su $n$ prove. La convergenza vale **solo se gli eventi elementari sono equiprobabili** e le prove sono **indipendenti**.

> [!warning] **Circolarità dell'approccio frequentistico**
> Definire la probabilità come limite di frequenze richiede il concetto di **indipendenza**, che è esso stesso probabilistico. È il "cane che si morde la coda". Per questo si usa poi la definizione assiomatica di Kolmogorov.

> [!caution] **Frequenza ≠ condizione sufficiente**
> Verificare che $N_{\text{dispari}} \approx N_{\text{pari}} \approx n/2$ non basta a dichiarare un dado onesto. Un dado con $P(1)=P(2)=1/4$ e $P(3)=P(4)=P(5)=P(6)=1/8$ ha comunque $P(\text{pari}) = P(\text{dispari}) = 1/2$, pur non essendo onesto.

### Analisi Combinatoria

#### Principio del prodotto cartesiano (regola fondamentale)

> [!abstract] **Teorema: Cardinalità del prodotto cartesiano**
> Dati $k$ insiemi finiti $A_1, A_2, \ldots, A_k$ con cardinalità $|A_i| = n_i$, la cardinalità del prodotto cartesiano è:
> $$|A_1 \times A_2 \times \cdots \times A_k| = \prod_{i=1}^{k} n_i$$

**Giustificazione:** Il primo elemento si sceglie in $n_1$ modi, il secondo in $n_2$ modi **indipendentemente**, …, il $k$-esimo in $n_k$ modi.

> **Attenzione:** Le $k$-uple sono **ordinate** — $(0,1) \neq (1,0)$.

**Esempio:** $\{0,1\} \times \{0,1\} = \{(0,0),(0,1),(1,0),(1,1)\}$ — $2 \times 2 = 4$ elementi.

#### Tabella riassuntiva

| Tipo di selezione | Formula | Nome |
|-------------------|---------|------|
| $k$-uple ordinate **con** ripetizione da $n$ | $n^k$ | — |
| $k$-uple ordinate **senza** ripetizione da $n$ | $\dfrac{n!}{(n-k)!}$ | Disposizioni semplici |
| $n$-uple ordinate **senza** ripetizione da $n$ | $n!$ | Permutazioni |
| $k$-uple **non ordinate** senza ripetizione da $n$ | $\dbinom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$ | Combinazioni (coeff. binomiale) |

#### Derivazione delle formule

**$k$-uple ordinate con ripetizione:** Ogni posizione si riempie in $n$ modi indipendentemente:
$$\underbrace{n \times n \times \cdots \times n}_{k} = n^k$$
*Esempio:* le sequenze binarie di lunghezza $k$ sono $2^k$.

**$k$-uple ordinate senza ripetizione:** Ogni volta che si pesca un elemento lo si rimuove:
$$n \times (n-1) \times (n-2) \times \cdots \times (n-k+1) = \frac{n!}{(n-k)!}$$

**Permutazioni** (caso $k = n$):
$$P(n) = n! = n(n-1)(n-2)\cdots 1$$

**Combinazioni:** Le $k$-uple **non ordinate** (dove $\{1,2,3\} = \{3,2,1\}$). Tra tutte le $\frac{n!}{(n-k)!}$ disposizioni semplici, ogni gruppo di $k!$ (tutte le permutazioni degli stessi $k$ elementi) corrisponde alla **stessa** combinazione:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

**Verifica ai casi limite:**
- $k=0$: $\binom{n}{0} = 1$ (solo $\emptyset$) ✓
- $k=n$: $\binom{n}{n} = 1$ (solo $A$ stesso) ✓
- $k=n-1$: $\binom{n}{n-1} = n$ (togliere un elemento alla volta) ✓

#### Cardinalità dell'insieme delle parti

> [!abstract] **Teorema**
> Dato un insieme $A$ con $m$ elementi:
> $$|\mathcal{P}(A)| = 2^m$$

**Dimostrazione:** I sottoinsiemi di $A$ con esattamente $k$ elementi sono $\binom{m}{k}$. Sommando su tutti i $k$:

$$|\mathcal{P}(A)| = \sum_{k=0}^{m} \binom{m}{k} \stackrel{\text{Newton}}{=} (1+1)^m = 2^m \qquad \square$$

Il **binomio di Newton** con $a=b=1$ garantisce l'ultima uguaglianza:
$$(a+b)^m = \sum_{k=0}^{m} \binom{m}{k} a^k b^{m-k}$$

#### Applicazione: probabilità di "colore" nel poker

Con un mazzo francese da 52 carte, $|\Omega| = \binom{52}{5}$ mani possibili. Le mani con "colore" (tutte 5 dello stesso seme): 4 semi × $\binom{13}{5}$ scelte per seme.

$$P(\text{colore}) = \frac{4 \cdot \binom{13}{5}}{\binom{52}{5}}$$

#### Nota finale: la martingala

Si può dimostrare con la teoria della probabilità che:
- Con patrimonio **infinito** e **nessun limite di puntata**, la martingala (raddoppio ad ogni perdita) batte matematicamente il banco.
- Con qualunque limite di puntata **finito**, a lungo andare si perde.

Questo è il motivo per cui tutti i casinò impongono un tetto massimo di puntata: non è arbitrario, è una conseguenza diretta della teoria della probabilità.

---

## 3.5 Conditional Probability

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Conditional Probability per la sintesi.)*

---

## 3.6 Bayes' Formula

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Bayes' Formula per la sintesi.)*

---

## 3.7 Independent Events

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Independent Events per la sintesi.)*

---

## 3.8 Law of Total Probability

**Non ancora trattato** come sezione autonoma. *(Trattato come parte della probabilità condizionata — vedi [[MSI compacto]] §Conditional Probability.)*

---

# Capitolo 4 — Random Variables and Expectation

## 4.1 Random Variables

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Random Variables.)*

---

## 4.2 Discrete Random Variables

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Types of Random Variables.)*

---

## 4.3 Expected Value

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Expectation.)*

---

## 4.4 Expectation of a Function of a Random Variable

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Properties of the Expected Value.)*

---

## 4.5 Variance

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Variance.)*

---

## 4.6 The Bernoulli and Binomial Random Variables

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §The Bernoulli and Binomial Random Variables.)*

---

## 4.7 The Poisson Random Variable

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §The Poisson Random Variable.)*

---

## 4.8 Moment Generating Functions

**Non ancora trattato.**

---

## 4.9 The Weak Law of Large Numbers

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Chebyshev's Inequality and the Weak Law of Large Numbers.)*

---

# Capitolo 5 — Special Random Variables

## 5.1 The Normal Random Variable

**Non ancora trattato.**

---

## 5.2 The Exponential Random Variable

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §Exponential Random Variables.)*

---

## 5.3 The Hypergeometric Random Variable

**Non ancora trattato.**

---

## 5.4 The Discrete Uniform Random Variable

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §The Uniform Random Variable.)*

---

## 5.5 The Poisson Process

**Non ancora trattato.**

---

## 5.6 The Uniform Random Variable

**Non ancora trattato** in questa lezione. *(Vedi [[MSI compacto]] §The Uniform Random Variable.)*

---

## 5.7 The Gamma Distribution

**Non ancora trattato.**

---

## 5.8 Distributions Arising from the Normal

**Non ancora trattato.**

---

## 5.9 The Logistics Distribution

**Non ancora trattato.**

---

# Capitolo 6 — Distributions of Sampling Statistics

## 6.1 Introduction

**Non ancora trattato.**

---

## 6.2 The Sample Mean

**Parzialmente trattato** (la convergenza della frequenza alla probabilità è stata accennata nell'approccio frequentistico — §3.4). La distribuzione della media campionaria non è stata sviluppata formalmente.

---

## 6.3 The Central Limit Theorem

**Non ancora trattato.**

---

## 6.4 Sample Variance

**Non ancora trattato.**

---

## 6.5 Sampling Distributions from a Normal Population

**Non ancora trattato.**

---

## 6.6 Sampling from a Finite Population

**Non ancora trattato.**

---

# Capitolo 7 — Parameter Estimation

## 7.1 Introduction

**Non ancora trattato.**

---

## 7.2 Maximum Likelihood Estimators

**Non ancora trattato.**

---

## 7.3 Interval Estimates

**Non ancora trattato.**

---

## 7.4 Estimating the Difference in Means of Two Normal Populations

**Non ancora trattato.**

---

## 7.5 Interval Estimates of Population Variances

**Non ancora trattato.**

---

## 7.6 Estimating the Unknown Bernoulli Parameter

**Non ancora trattato.**

---

## 7.7 Interval Estimates of the Mean of a Poisson Distribution

**Non ancora trattato.**

---

## 7.8 Bayes Estimators

**Non ancora trattato.**

---

# Capitolo 8 — Hypothesis Testing

## 8.1 Introduction

**Non ancora trattato.**

---

## 8.2 Significance Levels

**Non ancora trattato.**

---

## 8.3 Tests Concerning the Mean of a Normal Population

**Non ancora trattato.**

---

## 8.4 Testing the Equality of Means of Two Normal Populations

**Non ancora trattato.**

---

## 8.5 Tests Concerning the Variance of a Normal Population

**Non ancora trattato.**

---

## 8.6 Tests Concerning Bernoulli Parameters

**Non ancora trattato.**

---

## 8.7 Tests Concerning Poisson Parameters

**Non ancora trattato.**

---

# Capitolo 9 — Regression

## 9.1 Introduction

**Non ancora trattato.**

---

## 9.2 Least Squares Estimators of the Regression Parameters

**Non ancora trattato.**

---

## 9.3 Distribution of the Estimators

**Non ancora trattato.**

---

## 9.4 Statistical Inferences about the Regression Parameters

**Non ancora trattato.**

---

## 9.5 The Coefficient of Determination and the Sample Correlation Coefficient

**Non ancora trattato.**

---

## 9.6 Analysis of Residuals: Assessing the Model

**Non ancora trattato.**

---

## 9.7 Transforming to Linearity

**Non ancora trattato.**

---

## 9.8 Weighted Least Squares

**Non ancora trattato.**

---

## 9.9 Polynomial Regression

**Non ancora trattato.**

---

## 9.10 Multiple Linear Regression

**Non ancora trattato.**

---

## 9.11 Logistic Regression Models for Binary Output Data

**Non ancora trattato.**
