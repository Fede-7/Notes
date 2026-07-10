# Capitolo 1: Fondamenti di Calcolo delle Probabilità

## 1.1 Definizioni di Base
> [!def] Esperimento e Spazio Campione
> Un **esperimento** è un'operazione il cui esito dà uno tra più risultati possibili. Lo **spazio campione ($\Omega$)** è l'insieme di tutti i risultati possibili. Un **evento** è un qualunque sottoinsieme di $\Omega$.

## 1.2 Tecniche di Conteggio
> [!theorem] Formule Fondamentali di Calcolo Combinatorio
> - **Prodotto Cartesiano**: $|A^{(k)}| = \prod_{i=1}^k |Ai|$.
> - **$k$-ple ordinate senza ripetizione**: $n(n-1)\dots(n-k+1)$.
> - **$k$-ple ordinate con ripetizione**: $n^k$.
> - **Permutazioni**: $n!$.
> - **Combinazioni**: $C_{n,k} = \binom{n}{k} = \frac{n!}{k!(n-k)!}$.

## 1.3 Assiomi e Leggi di Probabilità
> [!def] Probabilità (Limite della Frequenza)
> $P(A) = \lim_{n \to \infty} \frac{n_A}{n}$. Per eventi equiprobabili: $P(A) = \frac{|\Omega_A|}{|\Omega|}$.

> [!theorem] Assiomi di Kolmogorov
> 1. $P(A) \geq 0$.
> 2. $P(\Omega) = 1$.
> 3. Se $A \cap B = \emptyset \implies P(A \cup B) = P(A) + P(B)$.

---

# Capitolo 2: Variabili Aleatorie e Distribuzioni Notevoli

## 2.1 Caratterizzazione delle Variabili Aleatorie (V.A.)
> [!def] Variabile Aleatoria
> Funzione $X: \omega \in \Omega \to X(\omega) \in \mathcal{X} \subseteq \mathbb{R}$.
> - **PMF (Discrete)**: $p_X(x) = P(X = x)$.
> - **PDF (Continue)**: $f_X(x) = \lim_{\Delta x \to 0} \frac{P(x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2})}{\Delta x}$.
> - **CDF**: $F_X(x) = P(X \leq x) = \int_{-\infty}^x f_X(t) dt$.

> [!theorem] Indicatori Statistici
> - **Media**: $E[X] = \sum x p_X(x)$ (discreto) o $\int x f_X(x) dx$ (continuo).
> - **Varianza**: $\sigma^2_X = E[(X - \mu_X)^2] = E[X^2] - \mu_X^2$.

## 2.2 Modelli di Distribuzione
### 2.2.1 Variabili Discrete
- **Binomiale $B(N, p)$**: $p_X(k) = \binom{N}{k} p^k (1-p)^{N-k}$.
- **Poissoniana $P(\lambda)$**: $p_X(k) = \frac{\lambda^k}{k!} e^{-\lambda}$.
### 2.2.2 Variabili Continue
- **Uniforme $U(a, b)$**: $f_X(x) = \frac{1}{b-a}$ per $x \in [a, b]$.
- **Gaussiana $N(\mu, \sigma^2)$**: $f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$.
- **Esponenziale $\mathcal{E}(\lambda)$**: $f_X(x) = \lambda e^{-\lambda x} u(x)$.

---

# Capitolo 3: Variabili Multiple e Vettori Aleatori

## 3.1 Caratterizzazione Congiunta
> [!def] PDF Congiunta
> $f_{X,Y}(x, y) = \lim_{\Delta x, \Delta y \to 0} \frac{P(x \pm \frac{\Delta x}{2}, y \pm \frac{\Delta y}{2})}{\Delta x \Delta y}$.
> - **Marginalizzazione**: $f_X(x) = \int f_{X,Y}(x, y) dy$.
> - **Indipendenza**: $f_{X,Y}(x, y) = f_X(x) f_Y(y)$.

## 3.2 Relazioni tra Variabili
> [!theorem] Covarianza e Correlazione
> - **Covarianza**: $COV[X,Y] = E[XY] - \mu_X \mu_Y$.
> - **Coefficiente di correlazione**: $\rho_{X,Y} = \frac{COV[X,Y]}{\sigma_X \sigma_Y} \in [-1, 1]$.

---

# Capitolo 4: Fondamenti di Statistica Inferenziale

## 4.1 La Media Campionaria
> [!theorem] Legge dei Grandi Numeri
> La media campionaria $\overline{X}_n = \frac{1}{n} \sum X_i$ converge al valore atteso $E[X]$.
> - **Debole**: in probabilità.
> - **Forte**: quasi certamente (probabilità 1).

## 4.2 Distribuzione Empirica e Coerenza
> [!dim] Convergenza quasi certa delle frequenze
> La probabilità che la frequenza osservata $f_n(a_i)$ differisca dalla probabilità vera $p_X(a_i)$ decade esponenzialmente con $n$: $P \sim 2^{-n D_i}$, dove $D_i$ è la divergenza informativa. Questo implica che l'estimatore è **fortemente coerente**.

---

# Capitolo 5: Teoria della Decisione e Test delle Ipotesi

## 5.1 Regole di Decisione (Classificazione)
> [!def] Rapporto di Verosimiglianza ($L$)
> Dato un dataset $x^n$, per scegliere tra ipotesi $H_1$ e $H_2$ si usa:
> $L(x^n) = \frac{p(x^n|H_1)}{p(x^n|H_2)} \underset{H_2}{\overset{H_1}{\gtrless}} \frac{P(H_2)}{P(H_1)} = \eta$.

> [!theorem] Regole MAP e ML
> - **MAP (Maximum A-posteriori)**: Sceglie l'ipotesi con massima probabilità a posteriori.
> - **ML (Maximum Likelihood)**: Caso MAP con ipotesi equiprobabili ($\eta = 1$).

## 5.2 Test di Neyman-Pearson
> [!def] Errori del Test
> - **Tipo-I (Falso Allarme $\alpha$)**: $P(D=H_1 | H_0)$.
> - **Potenza ($1-\beta$)**: $P(D=H_1 | H_1)$.
> - **NP Lemma**: Per massimizzare la potenza dato un vincolo su $\alpha$, la regione ottima è definita dal rapporto di verosimiglianza $L(x^n) \geq \eta$.

---

# Capitolo 6: Teoria della Stima dei Parametri

## 6.1 Stima Bayesiana (Parametro Casuale $\Theta$)
> [!theorem] Stimatori Ottimi
> - **MMSE (Minimum Mean Square Error)**: Corrisponde alla media della distribuzione a posteriori: $\hat{\theta}_{MMSE} = \int \theta f_{\Theta|X^n}(\theta|x^n) d\theta$.
> - **MAP**: Corrisponde alla moda della distribuzione a posteriori: $\hat{\theta}_{MAP} = \arg \max f_{\Theta|X^n}(\theta|x^n)$.

## 6.2 Stima non Bayesiana (Parametro Deterministico $\theta$)
> [!def] Stima di Massima Verosimiglianza (MLE)
> $\hat{\theta}_{ML} = \arg \max \log f_{X^n}(x^n; \theta)$.

> [!theorem] Limite di Cramér-Rao (CRB)
> La varianza di un qualunque stimatore non distorto è limitata inferiormente dall'inverso dell'Informazione di Fisher $I_n(\theta)$:
> $Var[\hat{\Theta}] \geq \frac{1}{I_n(\theta)}$. Uno stimatore che raggiunge il CRB è detto **efficiente**.

## 6.3 Stima Lineare e Minimi Quadrati (LS)
> [!rb] LMMSE (Linear MMSE)
> Stimatore della forma $\hat{\Theta} = a^T X^n + b$. Ottimo: $a_{LMMSE} = M^{-1} s$.

> [!theorem] Minimi Quadrati (Least Squares)
> In ambito descrittivo, minimizza $\|\epsilon\|^2 = \|X^T a - y\|^2$.
> La soluzione è $a_{LS} = (X X^T)^{-1} X y$.

> [!dim] Sequential LS (Sherman-Morrison)
> Permette l'aggiornamento ricorsivo della stima senza reinvertire la matrice:
> $(R + uv^T)^{-1} = R^{-1} - \frac{R^{-1} uv^T R^{-1}}{1 + u^T R^{-1} v}$.
