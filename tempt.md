# Appendici — Note MSI di Marco Lops

---

# Appendice A — Calcolo Combinatorio

## A.1 Definizioni Fondamentali

### Spazio dei Campioni
- **Simbolo:** $\Omega$
- **Definizione:** Insieme di tutti i risultati possibili di un esperimento
- **Assunzione nel corso:** Discreto (finito o numerabile)

### Evento
- Qualsiasi sottoinsieme di $\Omega$
- Un **evento elementare** $\omega \in \Omega$ è un singolo elemento di $\Omega$

---

## A.2 Richiami di Insiemistica

| Operazione | Notazione | Definizione |
$$
|---|---|---|
$$
| **Unione** | $A_1 \cup A_2$ | Contiene tutti gli elementi di $A_1$ e $A_2$ |
| **Intersezione** | $A_1 \cap A_2$ | Contiene solo gli elementi comuni |
| **Complemento** | $\overline{A}$ o $A^c$ | Elementi di $\Omega$ non in $A$ |
| **Sottrazione** | $A_1 \setminus A_2$ | $A_1 \cap \overline{A_2}$ |

### Leggi Fondamentali
$$
**De Morgan:**
$$
$$\overline{A_1 \cup A_2} = \overline{A_1} \cap \overline{A_2}$$
$$
**Associativa:**
$$
$$(A_1 \cup A_2) \cup A_3 = A_1 \cup (A_2 \cup A_3)$$
$$
**Distributiva:**
$$
$$A_1 \cup (\cap_{i=2}^{M} A_i) = \cap_{i=2}^{M} (A_1 \cup A_i)$$
---

## A.3 Nomenclatura Probabilistica

| Termine | Definizione |
$$
|---|---|
$$
| **Evento certo** | $\Omega$ |
| **Evento impossibile** | $\emptyset$ |
| **Eventi complementari** | $A$ e $A^c$ |
| **Mutuamente esclusivi** | $A \cap B = \emptyset$ |
| **$A$ implica $B$** | $A \subseteq B$ |

---

## A.4 Formule Combinatorie Essenziali

### Prodotto Cartesiano
$$|A_1 \times A_2 \times \cdots \times A_k| = \prod_{i=1}^{k} |A_i|$$
### Disposizioni (k-ple ordinate senza ripetizione)
Stringhe di lunghezza $k$ da $n$ elementi, ciascuno usato al massimo una volta:
$$D_{n,k} = \frac{n!}{(n-k)!} = n(n-1)(n-2) \cdots (n-k+1)$$
### Permutazioni
Caso particolare con $k=n$:
$$P_n = n! = n(n-1)(n-2) \cdots 1$$
### Combinazioni
Sottoinsiemi di cardinalità $k$ da $n$ elementi (ordine irrilevante):
$$C_{n,k} = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$
### Insieme delle Parti
Numero totale di sottoinsiemi di un insieme con $n$ elementi:
$$|\mathcal{P}(A)| = \sum_{k=0}^{n} \binom{n}{k} = 2^n$$
---

## A.5 Proprietà del Coefficiente Binomiale

- **Simmetria:** $\binom{n}{k} = \binom{n}{n-k}$
- **Ricorsione:** $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$
- **Teorema binomiale:** $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$
- **Somma:** $\sum_{k=0}^{n} \binom{n}{k} = 2^n$

---

# Appendice B — Probabilità di Base

## B.1 Assiomi di Kolmogorov

Per uno spazio dei campioni $\Omega$ e una famiglia $\mathcal{A}$ di eventi (σ-algebra):

1. **Non negatività:** $P(A) \geq 0$ per ogni $A \in \mathcal{A}$
2. **Normalizzazione:** $P(\Omega) = 1$
3. **Additività numerabile:** Se $\{A_i\}_{i=1}^{\infty}$ sono mutuamente esclusivi,
   $$P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$
---

## B.2 Proprietà Derivate

### Evento Complementare
$$P(A^c) = 1 - P(A)$$
### Evento Impossibile
$$P(\emptyset) = 0$$
### Unione di Due Eventi
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
**Caso di eventi mutuamente esclusivi:**
$$P(A \cup B) = P(A) + P(B) \quad \text{se } A \cap B = \emptyset$$
### Monotonia
Se $A \subseteq B$, allora $P(A) \leq P(B)$

### Disuguaglianza dell'Unione (Boole)
$$P\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i)$$
---

## B.3 Probabilità Condizionata

### Definizione
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \quad \text{con } P(B) > 0$$
### Regola della Moltiplicazione
$$P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)$$
### Legge della Probabilità Totale
Se $\{$B_1$, $B_2$, \ldots, B_n\}$ particella $\Omega$ (mutuamente esclusivi e esaustivi):
$$P(A) = \sum_{i=1}^{n} P(A \mid B_i) P(B_i)$$
---

## B.4 Teorema di Bayes
$$P(B \mid A) = \frac{P(A \mid B) P(B)}{P(A)}$$
Dove $P(A)$ può essere calcolato via legge della probabilità totale:
$$P(A) = \sum_{i=1}^{n} P(A \mid B_i) P(B_i)$$
Forma più generale:
$$P(B_j \mid A) = \frac{P(A \mid B_j) P(B_j)}{\sum_{i=1}^{n} P(A \mid B_i) P(B_i)}$$
---

## B.5 Indipendenza

### Indipendenza di Due Eventi
$$A \text{ e } B \text{ sono indipendenti} \iff P(A \cap B) = P(A) \cdot P(B)$$
**Equivalente:** $P(A \mid B) = P(A)$ (se $P(B) > 0$)

### Indipendenza Condizionata
$$P(A \cap B \mid C) = P(A \mid C) \cdot P(B \mid C)$$
### Indipendenza di n Eventi
Gli eventi $A_1, $A_2$, \ldots, A_n$ sono mutuamente indipendenti se:
$$P\left(\bigcap_{i \in S} A_i\right) = \prod_{i \in S} P(A_i)$$
per ogni sottoinsieme $S \subseteq \{1, 2, \ldots, n\}$ (inclusi sottoinsiemi di dimensione 1)

---

# Appendice C — Variabili Aleatorie Discrete

## C.1 Definizioni

### Variabile Aleatoria (v.a.)
Una funzione $X: \Omega \to \mathbb{R}$ che assegna un numero reale a ogni risultato di un esperimento.

### Supporto
$$\text{Supp}(X) = \{x : P(X=x) > 0\}$$
### Funzione di Massa di Probabilità (PMF)
$$p_X(x) = P(X = x)$$
Proprietà:
- $p_X(x) \geq 0$ per ogni $x$
- $\sum_{x \in \text{Supp}(X)} p_X(x) = 1$

### Funzione di Distribuzione Cumulativa (CDF)
$$F_X(x) = P(X \leq x) = \sum_{t \leq x} p_X(t)$$
---

## C.2 Momenti di v.a. Discrete

### Valore Atteso (Media)
$$E[X] = \sum_{x} x \cdot p_X(x)$$
Proprietà:
- **Linearità:** $E[aX + bY] = aE[X] + bE[Y]$
- **Monotonia:** Se $X \leq Y$ allora $E[X] \leq E[Y]$

### Varianza
$$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$
Proprietà:
- $\text{Var}(aX + b) = a^2 \text{Var}(X)$
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$
- Se $X, Y$ indipendenti: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$

### Deviazione Standard
$$\sigma_X = \sqrt{\text{Var}(X)}$$
### Covarianza
$$\text{Cov}(X,Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$
### Correlazione
$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} \in [-1, 1]$$
---

## C.3 Distribuzioni Discrete Notevoli

### Bernoulli($p$)
Rappresenta un singolo esperimento con esito successo/fallimento.

| Proprietà | Valore |
$$
|---|---|
$$
| **PMF** | $p_X(x) = p^x(1-p)^{1-x}$ per $x \in \{0,1\}$ |
| **E[X]** | $p$ |
| **Var(X)** | $p(1-p)$ |

### Binomiale($n, p$)
Numero di successi in $n$ prove indipendenti di Bernoulli.

| Proprietà | Valore |
$$
|---|---|
$$
| **PMF** | $p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}$ |
| **Supporto** | $\{0, 1, 2, \ldots, n\}$ |
| **E[X]** | $np$ |
| **Var(X)** | $np(1-p)$ |

### Poisson($\lambda$)
Approssima Binomiale per $n$ grande e $p$ piccolo ($np = \lambda$ costante).

| Proprietà | Valore |
$$
|---|---|
$$
| **PMF** | $p_X(k) = \frac{\lambda^k e^{-\lambda}}{k!}$ |
| **Supporto** | $\{0, 1, 2, \ldots\}$ |
| **E[X]** | $\lambda$ |
| **Var(X)** | $\lambda$ |

**Approssimazione:** Se $X \sim \text{Bin}(n,p)$ con $n \to \infty$, $p \to 0$ e $np = \lambda$, allora $X$ converge in distribuzione a Poisson($\lambda$).

### Geometrica($p$)
Numero di prove fino al primo successo.

| Proprietà | Valore |
$$
|---|---|
$$
| **PMF** | $p_X(k) = (1-p)^{k-1} p$ per $k \geq 1$ |
| **E[X]** | $1/p$ |
| **Var(X)** | $(1-p)/p^2$ |

**Proprietà di assenza di memoria:** $P(X > m+n \mid X > n) = P(X > m)$

### Uniforme Discreta
Su $\{1, 2, \ldots, n\}$.

| Proprietà | Valore |
$$
|---|---|
$$
| **PMF** | $p_X(k) = 1/n$ |
| **E[X]** | $(n+1)/2$ |
| **Var(X)** | $($n^2$-1)/12$ |

---

# Appendice D — Variabili Aleatorie Continue

## D.1 Definizioni

### Funzione Densità di Probabilità (PDF)
$$f_X(x) \text{ tale che } P(a \leq X \leq b) = \int_a^b f_X(x) dx$$
Proprietà:
- $f_X(x) \geq 0$ per ogni $x$
- $\int_{-\infty}^{\infty} f_X(x) dx = 1$
- $P(X = x) = 0$ per ogni $x$ (no atomi)

### Funzione di Distribuzione Cumulativa (CDF)
$$F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(t) dt$$
Relazione inversa: $f_X(x) = \frac{d}{dx} F_X(x)$

---

## D.2 Momenti di v.a. Continue

### Valore Atteso
$$E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$$
### Varianza
$$\text{Var}(X) = \int_{-\infty}^{\infty} (x - E[X])^2 f_X(x) dx = E[X^2] - (E[X])^2$$
### Momenti Generici
$$E[X^n] = \int_{-\infty}^{\infty} x^n f_X(x) dx$$
---

## D.3 Distribuzioni Continue Notevoli

### Uniforme($a, b$)
Probabilità costante su intervallo $[a,b]$.

| Proprietà | Valore |
$$
|---|---|
$$
| **PDF** | $f_X(x) = \frac{1}{b-a}$ per $x \in [a,b]$ |
| **CDF** | $F_X(x) = \frac{x-a}{b-a}$ |
| **E[X]** | $\frac{a+b}{2}$ |
| **Var(X)** | $\frac{(b-a)^2}{12}$ |

### Esponenziale($\lambda$)
Tempo di attesa tra eventi rari; assenza di memoria.

| Proprietà | Valore |
$$
|---|---|
$$
| **PDF** | $f_X(x) = \lambda e^{-\lambda x}$ per $x \geq 0$ |
| **CDF** | $F_X(x) = 1 - e^{-\lambda x}$ |
| **E[X]** | $1/\lambda$ |
| **Var(X)** | $1/\lambda^2$ |

**Proprietà:** $P(X > s+t \mid X > s) = P(X > t)$ (assenza di memoria)

### Normale($\mu, \sigma^2$)
Distribuzione gaussiana; modella fenomeni naturali.

| Proprietà | Valore |
$$
|---|---|
$$
| **PDF** | $f_X(x) = \frac{1}{$\sqrt{2\pi\sigma^2}$} \exp\left(-$\frac{(x-\mu)^2}{2\sigma^2}$\right)$ |
| **E[X]** | $\mu$ |
| **Var(X)** | $\sigma^2$ |

**Notazione:** $X \sim \mathcal{N}(\mu, \sigma^2)$

**Standardizzazione:** $Z = $\frac{X - \mu}{\sigma}$ \sim \mathcal{N}(0,1)$ (normale standard)

### Gamma($\alpha, \beta$)
Generalizzazione dell'esponenziale.

| Proprietà | Valore |
$$
|---|---|
$$
| **PDF** | $f_X(x) = $\frac{\beta^\alpha}{\Gamma(\alpha)}$ x^{\alpha-1} e^{-\beta x}$ per $x > 0$ |
| **E[X]** | $\alpha/\beta$ |
| **Var(X)** | $\alpha/\beta^2$ |
$$
**Casi speciali:**
$$
- $\alpha = 1$: Esponenziale($\beta$)
- $\alpha = n/2$, $\beta = 1/2$: Chi-quadrato($n$)

### Beta($\alpha, \beta$)
Supporto su $(0,1)$; utile per probabilità.

| Proprietà | Valore |
$$
|---|---|
$$
| **PDF** | $f_X(x) = $\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}$ x^{\alpha-1}(1-x)^{\beta-1}$ |
| **E[X]** | $\frac{\alpha}{\alpha+\beta}$ |
| **Var(X)** | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ |

---

# Appendice E — Coppie di Variabili Aleatorie

## E.1 Funzione di Massa Congiunta (caso discreto)
$$p_{X,Y}(x,y) = P(X=x, Y=y)$$
Proprietà:
- $p_{X,Y}(x,y) \geq 0$
- $\sum_{x,y} p_{X,Y}(x,y) = 1$

### Marginali
$$p_X(x) = \sum_y p_{X,Y}(x,y), \quad p_Y(y) = \sum_x p_{X,Y}(x,y)$$
### Condizionate
$$p_{X \mid Y}(x \mid y) = \frac{p_{X,Y}(x,y)}{p_Y(y)}$$
---

## E.2 Funzione Densità Congiunta (caso continuo)
$$P((X,Y) \in A) = \iint_A f_{X,Y}(x,y) \, dx \, dy$$
### Marginali
$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy$$
### Condizionate
$$f_{X \mid Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$$
---

## E.3 Indipendenza

**Caso discreto:** $p_{X,Y}(x,y) = p_X(x) \cdot p_Y(y)$ per tutti $x,y$

**Caso continuo:** $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$ per tutti $x,y$

**Conseguenza:** Se $X,Y$ indipendenti, allora:
- $E[XY] = E[X] \cdot E[Y]$
- $\text{Cov}(X,Y) = 0$
- $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$

---

## E.4 Funzioni di Variabili Aleatorie

### Z = g(X)
$$
**Caso discreto:**
$$
$$p_Z(z) = \sum_{x: g(x)=z} p_X(x)$$
**Caso continuo (se $g$ monotona):**
$$f_Z(z) = f_X(g^{-1}(z)) \left|\frac{d}{dz} g^{-1}(z)\right|$$
### Trasformazione Generale (X, Y) → (U, V)
$$f_{U,V}(u,v) = f_{X,Y}(x(u,v), y(u,v)) \left|J\right|$$
dove $J$ è lo Jacobiano:
$$J = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$
---

# Appendice F — Convergenza e Teoremi Limite

## F.1 Modi di Convergenza

### Convergenza in Probabilità
$$X_n \xrightarrow{P} X \quad \iff \quad \forall \epsilon > 0, \quad \lim_{n \to \infty} P(|X_n - X| > \epsilon) = 0$$
### Convergenza in Distribuzione
$$X_n \xrightarrow{d} X \quad \iff \quad \lim_{n \to \infty} F_{X_n}(t) = F_X(t) \quad \forall t$$
**Relazione:** Convergenza in probabilità $\Rightarrow$ Convergenza in distribuzione

---

## F.2 Legge dei Grandi Numeri (LGN)

Sia $\{X_i\}$ una successione di v.a. i.i.d. con media $\mu$ finita.

### LGN Debole (in probabilità)
$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu$$
### LGN Forte (quasi certamente)
$$P\left(\lim_{n \to \infty} \bar{X}_n = \mu\right) = 1$$
---

## F.3 Teorema Centrale del Limite (TCL)

Sia $\{X_i\}$ una successione di v.a. i.i.d. con media $\mu$ e varianza $\sigma^2$ finite.
$$\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)$$
Equivalentemente:
$$\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} \mathcal{N}(0, \sigma^2)$$
**Applicazione:** Per $n$ grande,
$$P(a \leq \bar{X}_n \leq b) \approx \Phi\left(\frac{b-\mu}{\sigma/\sqrt{n}}\right) - \Phi\left(\frac{a-\mu}{\sigma/\sqrt{n}}\right)$$
dove $\Phi$ è la CDF della normale standard.

---

## F.4 Disuguaglianze Utili

### Markov
Per v.a. non negativa $X$ e $a > 0$:
$$P(X \geq a) \leq \frac{E[X]}{a}$$
### Chebyshev
Per v.a. con media $\mu$ e varianza $\sigma^2$:
$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$
### Hoeffding
Per somma di v.a. indipendenti in $[$a_i$, b_i]$:
$$P\left(\left|\sum_{i=1}^n (X_i - E[X_i])\right| \geq t\right) \leq 2\exp\left(-\frac{2t^2}{\sum_{i=1}^n (b_i-a_i)^2}\right)$$
### Chernoff
Per $S_n = \sum_{i=1}^n X_i$ con $X_i$ i.i.d. e $E[X_i] = \mu$:
$$P(S_n \geq na) \leq \inf_{t > 0} e^{-t(na)} M(t)^n$$
dove $M(t) = E[e^{tX_i}]$ è la funzione generatrice dei momenti.

---

# Appendice G — Vettori Aleatori

## G.1 Notazione Matriciale

Vettore aleatorio $n$-dimensionale:
$$\mathbf{X} = \begin{bmatrix} X_1 \\ X_2 \\ \vdots \\ X_n \end{bmatrix}$$
### Valore Atteso
$$\boldsymbol{\mu} = E[\mathbf{X}] = \begin{bmatrix} E[X_1] \\ E[X_2] \\ \vdots \\ E[X_n] \end{bmatrix}$$
### Matrice di Covarianza
$$\boldsymbol{\Sigma} = \text{Cov}(\mathbf{X}) = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]$$
Elemento generico: $\Sigma_{ij} = \text{Cov}($X_i$, $X_j$)$

Proprietà:
- Simmetrica: $\boldsymbol{\Sigma}^T = \boldsymbol{\Sigma}$
- Semidefinita positiva: $\mathbf{v}^T \boldsymbol{\Sigma} \mathbf{v} \geq 0$ per ogni $\mathbf{v}$

---

## G.2 Trasformazioni Lineari

Se $\mathbf{Y} = \mathbf{A} \mathbf{X} + \mathbf{b}$ con $\mathbf{A}$ matrice $m \times n$ e $\mathbf{b}$ vettore $m$:
$$E[\mathbf{Y}] = \mathbf{A} E[\mathbf{X}] + \mathbf{b}$$
$$\text{Cov}(\mathbf{Y}) = \mathbf{A} \text{Cov}(\mathbf{X}) \mathbf{A}^T$$
---

## G.3 Normale Multivariata

$\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ ha densità:
$$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\boldsymbol{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x}-\boldsymbol{\mu})\right)$$
Proprietà:
- Marginali: $X_i \sim \mathcal{N}(\mu_i, \Sigma_{ii})$
- Trasformazioni lineari: Se $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$, allora $\mathbf{Y} \sim \mathcal{N}(\mathbf{A}\boldsymbol{\mu}+\mathbf{b}, \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^T)$
- Indipendenza ⟷ Incorrelazione (caso Gaussiano)

---

# Appendice H — Processi Stocastici Discreti

## H.1 Definizioni Base

### Processo Stocastico
Famiglia di v.a. indicizzate dal tempo: $\{X_n\}_{n \in T}$ (con $T$ discreto nel nostro caso)

### Stazionarietà (in senso stretto)
La distribuzione congiunta di $(X_{n}, X_{n+1}, \ldots, X_{n+k})$ è indipendente da $n$ per ogni $k$.

### Stazionarietà in Senso Debole
- $E[X_n] = \mu$ costante
- $\text{Cov}($X_n$, X_{n+h}) = \gamma(h)$ dipende solo da $h$

---

## H.2 Funzione di Autocorrelazione

### Autocovarianza
$$\gamma(h) = \text{Cov}(X_n, X_{n+h}) = E[(X_n - \mu)(X_{n+h} - \mu)]$$
Proprietà:
- $\gamma(0) = \text{Var}($X_n$) = \sigma^2$
- $\gamma(-h) = \gamma(h)$ (simmetria)
- $|\gamma(h)| \leq \gamma(0)$

### Autocorrelazione
$$\rho(h) = \frac{\gamma(h)}{\gamma(0)} = \frac{\gamma(h)}{\sigma^2}$$
Proprietà: $\rho(0) = 1$ e $|\rho(h)| \leq 1$

---

## H.3 Catene di Markov

### Definizione
Un processo stocastico $\{X_n\}$ è una catena di Markov se:
$$P(X_{n+1} = j \mid X_n = i, X_{n-1}, \ldots, X_0) = P(X_{n+1} = j \mid X_n = i)$$
(il futuro dipende solo dal presente, non dal passato)

### Matrice di Transizione
$$\mathbf{P} = [p_{ij}] \quad \text{dove} \quad p_{ij} = P(X_{n+1} = j \mid X_n = i)$$
Proprietà:
- Righe sommano a 1: $\sum_j p_{ij} = 1$
- Elementi non negativi: $p_{ij} \geq 0$

### Distribuzione al passo $n$
$$\boldsymbol{\pi}^{(n)} = \boldsymbol{\pi}^{(0)} \mathbf{P}^n$$
dove $\boldsymbol{\pi}^{(0)}$ è la distribuzione iniziale.

### Distribuzione Stazionaria
Soluzione di $\boldsymbol{\pi} = \boldsymbol{\pi} \mathbf{P}$ con $\sum_i \pi_i = 1$.

Se esiste ed è unica, per molte catene:
$$\lim_{n \to \infty} \boldsymbol{\pi}^{(n)} = \boldsymbol{\pi}$$
indipendentemente dallo stato iniziale.

---

# Appendice I — Teoria dell'Informazione

## I.1 Entropia

### Entropia di Shannon (base 2)
Per v.a. discreta $X$:
$$H(X) = -\sum_{x} P(X=x) \log_2 P(X=x)$$
**Unità:** bit (bit di incertezza)

### Proprietà
- $H(X) \geq 0$ con uguaglianza iff $X$ è deterministica
- $H(X) \leq \log_2 |\text{Supp}(X)|$ con uguaglianza se $X$ uniforme
- Per due variabili: $H(X,Y) = H(X) + H(Y \mid X)$

### Entropia Condizionata
$$H(X \mid Y) = -\sum_{y} P(Y=y) \sum_{x} P(X=x \mid Y=y) \log_2 P(X=x \mid Y=y)$$
---

## I.2 Informazione Mutua

### Definizione
$$I(X;Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X)$$
Misura quanto la conoscenza di $Y$ riduce l'incertezza su $X$.

### Proprietà
- $I(X;Y) = I(Y;X)$ (simmetria)
- $I(X;Y) \geq 0$ con uguaglianza iff $X,Y$ indipendenti
- $I(X;Y) = \sum_{x,y} P(x,y) \log_2 \frac{P(x,y)}{P(x)P(y)}$

---

## I.3 Capacità di Canale

### Canale Simmetrico Binario (BSC)
Trasmette 0 o 1 con probabilità di errore $p$.
$$
**Capacità:**
$$$$C = 1 - H(p)$$ bit per uso del canale

dove $H(p) = -p \log_2 p - (1-p) \log_2(1-p)$ è l'entropia di Bernoulli($p$).

Casi limite:
- $p = 0$ (no errori): $C = 1$ bit
- $p = 1/2$ (rumore totale): $C = 0$ bit

### Capacità Generale
$$C = \max_{p_X(x)} I(X;Y)$$
dove il massimo è su tutte le possibili distribuzioni di input.

---

# Appendice J — Stima Parametrica

## J.1 Stimatori

### Stima Puntuale
Dato campione $(x_1, \ldots, x_n)$, lo stimatore $\hat{\theta}$ è una funzione dei dati.

### Proprietà degli Stimatori
$$
**Correttezza (Unbiasedness):**
$$
$$E[\hat{\theta}] = \theta$$
$$
**Consistenza:**
$$
$$\hat{\theta}_n \xrightarrow{P} \theta \quad \text{per } n \to \infty$$
$$
**Efficienza:**
$$
Varianza minima tra stimatori corretti.

---

## J.2 Metodo della Massima Verosimiglianza (MLE)

### Funzione di Verosimiglianza
$$L(\theta; x_1, \ldots, x_n) = \prod_{i=1}^n f(x_i; \theta)$$
o nel caso discreto:
$$L(\theta; x_1, \ldots, x_n) = \prod_{i=1}^n P(X_i = x_i; \theta)$$
### Stima MLE
$$\hat{\theta}_{\text{MLE}} = \arg\max_\theta L(\theta) = \arg\max_\theta \ell(\theta)$$
dove $\ell(\theta) = \log L(\theta)$ è la log-verosimiglianza.

### Proprietà
- Asintoticamente corretto e consistente
- Asintoticamente normale: $\sqrt{n}(\hat{\theta} - \theta) \xrightarrow{d} \mathcal{N}(0, I(\theta)^{-1})$

dove $I(\theta)$ è l'informazione di Fisher.

---

## J.3 Informazione di Fisher
$$I(\theta) = -E\left[\frac{d^2 \log f(X;\theta)}{d\theta^2}\right] = E\left[\left(\frac{d \log f(X;\theta)}{d\theta}\right)^2\right]$$
Per campione di $n$ i.i.d.:
$$I_n(\theta) = n \cdot I(\theta)$$
---

# Appendice K — Stima MMSE e LS

## K.1 Stimatore MMSE

Problema: Stimare $\theta$ da osservazione $Y$ minimizzando MSE.

### Stimatore Ottimale
$$\hat{\theta}_{\text{MMSE}} = E[\theta \mid Y]$$
Minimizza:
$$\text{MSE} = E[(\hat{\theta} - \theta)^2]$$
### Nel Caso Gaussiano
Se $(Y, \theta)$ sono congiuntamente Gaussiani:
$$\hat{\theta}_{\text{MMSE}} = \mu_\theta + \frac{\sigma_{Y\theta}}{\sigma_Y^2}(Y - \mu_Y)$$
Errore:
$$\text{MMSE} = \sigma_\theta^2 - \frac{\sigma_{Y\theta}^2}{\sigma_Y^2} = \sigma_\theta^2(1 - \rho^2)$$
dove $\rho$ è correlazione tra $Y$ e $\theta$.

---

## K.2 Stimatore dei Minimi Quadrati Lineari (LMMSE)

Assumiamo relazione lineare:
$$\hat{\theta} = aY + b$$
### Coefficienti Ottimali
$$a = \frac{\text{Cov}(Y, \theta)}{\text{Var}(Y)} = \frac{\sigma_{Y\theta}}{\sigma_Y^2}$$
$$b = \mu_\theta - a \mu_Y$$
### Errore LMMSE
$$\text{LMMSE} = \text{Var}(\theta) - \frac{\sigma_{Y\theta}^2}{\sigma_Y^2} = \sigma_\theta^2(1 - \rho^2)$$
**Nota:** Nel caso Gaussiano, LMMSE = MMSE.

---

## K.3 Least Squares Ricorsivo

Dato dataset $n$-dimensionale con $p$ campioni, si minimizza:
$$\|\mathbf{X}^T\mathbf{a} - \mathbf{y}\|^2$$
### Soluzione LS
$$\mathbf{a}_{\text{LS}}(p) = (\mathbf{X}(p)\mathbf{X}^T(p))^{-1}\mathbf{X}(p)\mathbf{y}(p)$$
### Aggiornamento Ricorsivo (Sherman-Morrison)
Quando arriva nuovo campione $\mathbf{x}^n(p+1)$:
$$\mathbf{R}^{-1}(p+1) = \mathbf{R}^{-1}(p) - \frac{\mathbf{R}^{-1}(p)\mathbf{x}^n(p+1)\mathbf{x}^{nT}(p+1)\mathbf{R}^{-1}(p)}{1 + K(p+1)}$$
dove $K(p+1) = \mathbf{x}^{nT}(p+1)\mathbf{R}^{-1}(p)\mathbf{x}^n(p+1)$
$$\mathbf{a}(p+1) = \mathbf{a}(p) + \mathbf{R}^{-1}(p+1)\mathbf{x}^n(p+1)[\theta(p+1) - \mathbf{x}^{nT}(p+1)\mathbf{a}(p)]$$
**Vantaggi:** Complessità $\mathcal{O}(n^2)$ invece di $\mathcal{O}(n^3)$ di reinversione

---

# Appendice L — Tabelle di Riferimento Rapido

## L.1 Simboli Comuni

| Simbolo | Significato | Contesto |
$$
|---------|------------|---------|
$$
| $\Omega$ | Spazio dei campioni | Probabilità di base |
| $\mathcal{F}$ o $\mathcal{A}$ | σ-algebra di eventi | Spazi di probabilità |
| $P(A)$ | Probabilità di evento $A$ | Assiomi di Kolmogorov |
| $X$ | Variabile aleatoria | Variabili discrete/continue |
| $E[X]$ | Valore atteso (media) | Momenti |
| $\text{Var}(X)$ | Varianza | Dispersione |
| $\sigma$ | Deviazione standard | $\sqrt{\text{Var}(X)}$ |
| $\sigma^2$ | Varianza | Matrici di covarianza |
| $\rho$ | Correlazione | Relazione tra due v.a. |
| $\sim$ | "segue distribuzione" | Notazione |
| $\xrightarrow{P}$ | Converge in probabilità | Convergenza |
| $\xrightarrow{d}$ | Converge in distribuzione | TCL |
| $\mathcal{N}(\mu, \sigma^2)$ | Distribuzione normale | Gaussiana |
| $I(X;Y)$ | Informazione mutua | Teoria dell'informazione |
| $H(X)$ | Entropia | Shannon |

---

## L.2 Formule Algebriche Utili
$$
| Formula | Valore/Uso |
$$
$$
|---------|-----------|
$$
| Somma di Gauss | $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ |
| Somma quadrati | $\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$ |
| Serie geometrica | $\sum_{k=0}^{\infty} r^k = \frac{1}{1-r}$ per $\|r\| < 1$ |
| Serie esponenziale | $e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}$ |
| Teorema binomiale | $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$ |
| Espansione $\ln(1+x)$ | $\ln(1+x) = \sum_{k=1}^{\infty} \frac{(-1)^{k-1}}{k} x^k$ per $\|x\| < 1$ |
| Fattoriale di Stirling | $n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$ |

---

## L.3 Costanti Importanti

| Costante | Valore | Note |
$$
|----------|--------|-------|
$$
| $e$ | $2.71828\ldots$ | Base logaritmo naturale |
| $\pi$ | $3.14159\ldots$ | Circonferenza di cerchio unitario |
| $\sqrt{2}$ | $1.41421\ldots$ | $\approx 1.414$ |
| $\sqrt{3}$ | $1.73205\ldots$ | $\approx 1.732$ |
| $\phi$ (aureo) | $1.61803\ldots$ | $(1+\sqrt{5})/2$ |
| $\gamma$ (Eulero-Mascheroni) | $0.57721\ldots$ | $\lim_{n \to \infty}(H_n - \ln n)$ |

---

## L.4 Quantili della Normale Standard

| Probabilità | $P(Z \leq z)$ | Valore $z$ |
$$
|---|---|---|
$$
| $0.50$ | $50\%$ | $0.000$ |
| $0.68$ | $68\%$ | $\pm 1.000$ |
| $0.90$ | $90\%$ | $1.282$ |
| $0.95$ | $95\%$ | $1.645$ |
| $0.975$ | $97.5\%$ | $1.960$ |
| $0.99$ | $99\%$ | $2.326$ |
| $0.995$ | $99.5\%$ | $2.576$ |

(Ricorda: Per $Z \sim \mathcal{N}(0,1)$, $P(Z \leq z) = \Phi(z)$)

---

## L.5 Approssimazioni Utili

- **Binomiale → Normale:** Se $X \sim \text{Bin}(n,p)$ con $np(1-p) \geq 5$, allora $X \approx \mathcal{N}(np, np(1-p))$
- **Binomiale → Poisson:** Se $X \sim \text{Bin}(n,p)$ con $n$ grande e $p$ piccolo, allora $X \approx \text{Poi}(np)$
- **Poisson → Normale:** Se $X \sim \text{Poi}(\lambda)$ con $\lambda$ grande, allora $X \approx \mathcal{N}(\lambda, \lambda)$

---

## L.6 Identità Matriciali Utili

| Identità | Condizioni |
$$
|----------|-----------|
$$
| $(AB)^T = B^T A^T$ | Dimensioni compatibili |
| $(\mathbf{A}^{-1})^T = (\mathbf{A}^T)^{-1}$ | $\mathbf{A}$ invertibile |
| $\text{tr}(\mathbf{A}\mathbf{B}) = \text{tr}(\mathbf{B}\mathbf{A})$ | Dimensioni compatibili |
| $\nabla_{\mathbf{x}} (\mathbf{a}^T \mathbf{x}) = \mathbf{a}$ | Derivata di forma lineare |
| $\nabla_{\mathbf{x}} (\mathbf{x}^T \mathbf{A} \mathbf{x}) = 2\mathbf{A}\mathbf{x}$ | $\mathbf{A}$ simmetrica |
| $\|\\mathbf{A}\mathbf{x}\\|^2 = \mathbf{x}^T \mathbf{A}^T \mathbf{A} \mathbf{x}$ | Norma euclidea |

---
$$
**Fine delle Appendici**
$$
---

*Nota: Queste appendici sintetizzano i concetti principali trattati negli appunti del corso MSI. Per dettagli, dimostrazioni ed esempi, fare riferimento al corpo principale delle dispense.*