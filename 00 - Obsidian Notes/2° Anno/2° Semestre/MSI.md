# Analisi Critica e Approfondimenti al Report Tecnico

## Osservazioni Metodologiche Generali

Il report presenta un'architettura teorica solida e ben strutturata. Tuttavia, emergono alcune aree suscettibili di approfondimento e precisazione tecnica.

---
## Definizioni Fondamentali

### Esperimento

> [!abstract] Definizione
> Un **esperimento** è un'operazione (o insieme di operazioni) che conduce a **uno tra tanti risultati possibili**.

### Spazio dei Campioni $\Omega$

> [!abstract] Definizione
> Lo **spazio dei campioni** (o *sample space*) è l'insieme di **tutti i possibili risultati** di un esperimento. Si indica con $\Omega$.
$$\Omega = \{\omega_1, \omega_2, \ldots\}$$
Può essere:
- **Finito** → es. lancio di una moneta: $\Omega = \{T, C\}$
- **Numerabilmente infinito** → es. numero di pacchetti in coda: $\Omega = \mathbb{N}_0$
- **Non numerabile (continuo)** → es. tensione misurata ai capi di una resistenza (rumore termico): $\Omega = \mathbb{R}$

> [!note] Discreto vs Continuo nella pratica
> In realtà qualunque misura fisica è razionale (strumenti con cifre significative finite), ma quando i valori sono così tanti, si modella come continuo e poi si tronca. Il **tempo** viene solitamente schematizzato come continuo.

### Evento

> [!abstract] Definizione
> Un **evento** è un **sottoinsieme** di $\Omega$ definito da una proposizione.
> Un **evento elementare** è un singolo elemento di $\Omega$.

> [!warning] La proposizione non è unica!
> L'evento è univocamente determinato dagli elementi di $\Omega$ che lo compongono, ma la proposizione che lo descrive **non è univoca** (la ridondanza del linguaggio naturale lo permette).
>
> **Esempio:** ho in tasca 1, 2, 3, 4 o 5 euro. L'evento $\{1, 3, 5\}$ può essere descritto come:
> - "ho un numero dispari di euro"
> - "non ho un numero pari di euro"
> - "ho 1 o 3 o 5 euro"
>
> → Saper **riformulare** la proposizione in modo conveniente è spesso la chiave per risolvere un esercizio.
### Nomenclatura degli eventi

| Nome                     | Definizione                                                                              | Notazione         |
| ------------------------ | ---------------------------------------------------------------------------------------- | ----------------- |
| **Evento impossibile**   | Insieme vuoto                                                                            | $\emptyset$       |
| **Evento certo**         | $\Omega$ stesso — ogni volta che compie l'esperimento si ottiene un elemento di $\Omega$ | $\Omega$          |
| **Evento complementare** | $A^c$ = elementi di $\Omega$ non in $A$                                                  | $A^c$ o $\bar{A}$ |
| **Eventi incompatibili** | $A \cap B = \emptyset$                                                                   | —                 |
| **$A$ implica $B$**      | $A \subseteq B$ — il verificarsi di $A$ implica il verificarsi di $B$ (non viceversa)    | $A \subseteq B$   |

---

## Operazioni sugli Insiemi / Eventi

### Riassunto operazioni
1. $A_1 \cup A_2 = \{\omega \in \Omega \mid \omega \in A_1 \text{ oppure } \omega \in A_2\}$
2. $A_1 \cap A_2 = \{\omega \in \Omega \mid \omega \in A_1 \text{ e } \omega \in A_2\}$
3. $A_1^c = \{\omega \in \Omega \mid \omega \notin A_1\}$
4. $A_1 \setminus A_2 = A_1 \cap A_2^c$
### Proprietà utili

| Proprietà                | Formula                       |
| ------------------------ | ----------------------------- |
| Doppio complemento       | $($A^c$)^c = A$               |
| Complemento di $\Omega$  | $\Omega^c = \emptyset$        |
| Unione con complementare | $A \cup A^c = \Omega$         |
| De Morgan                | $(A \cup B)^c = A^c \cap B^c$ |
| De Morgan                | $(A \cap B)^c = A^c \cup B^c$ |

---

## Approccio Frequentistico alla Probabilità

### Frequenza di successo

> [!abstract] Definizione
> Dati $n$ esperimenti **indipendenti** (l'esito di uno non influenza gli altri), si definisce **frequenza di successo** dell'evento $A$ su $n$ prove:
>
> $$f_n(A) = \frac{N_A}{n}$$
>
> dove $N_A$ è il numero di volte in cui si è verificato $A$.

Per un dado **onesto** (eventi elementari equiprobabili):
$$\lim_{n \to \infty} f_n(A) = \frac{|A|}{|\Omega|}$$
> [!warning] Il cane che si morde la coda
> La definizione frequentistica usa implicitamente il concetto di **indipendenza** — che è esso stesso un concetto probabilistico. È una definizione un po' autoriflessiva: per questo il prof darà anche una definizione più rigorosa (assiomatica).

> [!example] Verifica dell'onestà di un dado
> Lancio $n$ volte, conto $N_1, N_2, \ldots, N_6$. Il dado è (probabilmente) onesto se:
> $$\frac{N_i}{n} \approx \frac{1}{6} \quad \forall i$$
> Non è una condizione *sufficiente* (i singoli potrebbero compensarsi), ma è *necessaria*.

---


## 1. Analisi Combinatoria: Integrazioni Necessarie

### 1.1 Distinzione tra Modelli con/senza Reinserimento

Il report menziona le **disposizioni con ripetizione** ($n^k$) ma non esplicita sufficientemente il modello di **combinazioni con ripetizione**:

$$C^*_{n,k} = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n-1)!}$$

**Caso d'uso**: Distribuzione di $k$ oggetti indistinguibili in $n$ contenitori distinti (problema stars-and-bars).

### 1.2 Principio di Inclusione-Esclusione

Per eventi non disgiunti, la formula dell'unione si generalizza:

$$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i} P(A_i) - \sum_{i<j} P(A_i \cap A_j) + \sum_{i<j<k} P(A_i \cap A_j \cap A_k) - \cdots$$

**Applicazione**: Calcolo della probabilità che almeno una carta sia un asso in una mano di 5 carte.

---

## 2. Assiomi di Kolmogorov: Precisazioni Tecniche

### 2.1 σ-Algebra e Misurabilità

Il report omette la definizione formale dello spazio di probabilità $(\Omega, \mathcal{F}, P)$, dove:

- $\mathcal{F}$ è una **σ-algebra** su $\Omega$
- Gli eventi devono appartenere a $\mathcal{F}$ per essere misurabili

**Implicazione pratica**: Non tutti i sottoinsiemi di $\Omega$ sono necessariamente eventi (rilevante in spazi continui).

### 2.2 Convergenza Frequentista

La definizione frequentista richiede precisazione:

$$P(A) = \lim_{n \to \infty} \frac{n_A}{n} \quad \text{(convergenza quasi certa per la Legge dei Grandi Numeri)}$$

**Nota**: La convergenza è garantita con probabilità 1, non in senso deterministico.

---

## 3. Teorema di Bayes: Estensioni e Applicazioni

### 3.1 Correzione nell'Esempio del Dado Truccato

**Verifica dei calcoli**:

Per il dado truccato $D_t$: $P(5|D_t) = \frac{1}{10}$

$$P(55|D_t) = \left(\frac{1}{10}\right)^2 = 0.01 \quad \checkmark$$

Per il dado onesto:

$$P(55|D_o) = \left(\frac{1}{6}\right)^2 = \frac{1}{36} \approx 0.0278$$

Applicando Bayes:

$$P(D_t|55) = \frac{0.01 \times 0.5}{0.01 \times 0.5 + 0.0278 \times 0.5} = \frac{0.005}{0.0189} \approx 0.265$$

**Interpretazione**: L'osservazione di due "5" consecutivi riduce la probabilità posteriore che il dado sia truccato (da 0.5 a 0.265), poiché l'evento è *più verosimile* con il dado onesto.

### 3.2 Inference Bayesiana Sequenziale

Dopo osservazione multipla, aggiornamento iterativo:

$$P(H|E_1, E_2) \propto P(E_2|H, E_1) P(H|E_1)$$

---

## 4. Variabili Aleatorie: Approfondimenti

### 4.1 Funzione di Ripartizione (CDF)

Complemento essenziale alla PMF:

$$F_X(x) = P(X \leq x) = \sum_{x_i \leq x} p_X(x_i)$$

**Proprietà**:
- Monotona non decrescente
- $\lim_{x \to -\infty} F_X(x) = 0$, $\lim_{x \to +\infty} F_X(x) = 1$
- Continua a destra con limiti sinistri

### 4.2 Binomiale vs Poisson: Limite Asintotico

La distribuzione di Poisson emerge come limite della Binomiale quando $n \to \infty$, $p \to 0$, con $np = \lambda$ fissato:

$$\lim_{n \to \infty} \binom{n}{k} p^k (1-p)^{n-k} = \frac{\lambda^k e^{-\lambda}}{k!}$$

**Applicazione**: Modellazione di eventi rari su grandi popolazioni (difetti produttivi, decadimenti radioattivi).

---

## 5. Momenti e Disuguaglianze: Estensioni

### 5.1 Momenti Superiori

- **Momento $r$-esimo**: $E[X^r]$
- **Skewness** (asimmetria): $\gamma_1 = \frac{E[(X-\mu)^3]}{\sigma^3}$
- **Kurtosis** (curtosi): $\gamma_2 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3$

### 5.2 Disuguaglianza di Markov - Forma Generale

Per variabile aleatoria non negativa e funzione crescente $g$:

$$P(X \geq a) \leq \frac{E[g(X)]}{g(a)}$$

**Caso particolare** ($g(x) = x$):

$$P(X \geq a) \leq \frac{E[X]}{a}$$

### 5.3 Applicazione Pratica della Disuguaglianza di Chebyshev

**Problema**: Verificare il margine di errore in un sondaggio.

Con $n=400$ campioni, $\sigma^2 = 0.25$:

$$P(|\bar{X} - \mu| \geq 0.05) \leq \frac{0.25/400}{0.05^2} = 0.25$$

Garantisce che l'errore superi il 5% con probabilità massima 25%.

---

## 6. Variabili Multiple: Correlazione e Covarianza

### 6.1 Covarianza

Misura la tendenza di due variabili a variare congiuntamente:

$$\text{Cov}(X,Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$

**Proprietà**:
- $\text{Cov}(X,X) = \text{Var}(X)$
- Se $X$ e $Y$ indipendenti, allora $\text{Cov}(X,Y) = 0$ (non vale il viceversa)

### 6.2 Coefficiente di Correlazione

Normalizzazione della covarianza:

$$\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}, \quad -1 \leq \rho \leq 1$$

**Interpretazione**:
- $\rho = 1$: dipendenza lineare positiva perfetta
- $\rho = -1$: dipendenza lineare negativa perfetta
- $\rho = 0$: assenza di correlazione lineare

### 6.3 Esempio Numerico - Verifica Indipendenza

Dalla tabella fornita:

| X\Y | 0 | 1 | $P(X)$ |
|-----|-------|-------|--------|
| 0 | 1/4 | 1/8 | 3/8 |
| 1 | 1/8 | 1/2 | 5/8 |
| $P(Y)$ | 3/8 | 5/8 | 1 |

**Calcolo covarianza**:

$$E[XY] = 0 \cdot 0 \cdot \frac{1}{4} + 0 \cdot 1 \cdot \frac{1}{8} + 1 \cdot 0 \cdot \frac{1}{8} + 1 \cdot 1 \cdot \frac{1}{2} = \frac{1}{2}$$

$$E[X] = \frac{5}{8}, \quad E[Y] = \frac{5}{8}$$

$$\text{Cov}(X,Y) = \frac{1}{2} - \frac{5}{8} \cdot \frac{5}{8} = \frac{1}{2} - \frac{25}{64} = \frac{7}{64} \neq 0$$

**Conclusione**: Le variabili sono **dipendenti** e **positivamente correlate**.

---

## 7. Integrazioni Raccomandate

### Teoremi Limite
- **Legge dei Grandi Numeri** (debole e forte)
- **Teorema Centrale del Limite**: convergenza alla distribuzione normale

### Catene di Markov
Estensione della probabilità condizionata a processi stocastici:

$$P(X_{n+1} | X_n, X_{n-1}, \ldots, X_0) = P(X_{n+1} | X_n)$$

### Stima dei Parametri
- **Massima Verosimiglianza** (MLE)
- **Stimatori non distorti** e loro varianza minima

---

## Conclusioni

Il report costituisce una base teorica rigorosa. Le integrazioni suggerite ne aumenterebbero la completezza operativa, specialmente in contesti di inferenza statistica e machine learning, dove correlazione, momenti superiori e teoremi limite sono strumenti quotidiani di analisi.
