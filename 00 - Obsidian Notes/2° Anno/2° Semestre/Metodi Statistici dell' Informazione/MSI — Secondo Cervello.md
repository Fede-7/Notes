---
tags: [MSI, secondo-cervello, master-guide]
corso: Metodi Statistici dell'Informazione
docente: Marco Lops
status: completo
---

# 🧠 MSI — Secondo Cervello

> [!abstract] Mappa Mentale del Corso
> Ogni sezione è una **parcella autonoma**. Leggi dall'alto verso il basso, segui i link `[[ ]]` per navigare tra concetti collegati. I callout colorano il tipo di informazione: **Ciano = essenza**, **Verde = formula/dato esatto**, **Rosso = metafora/esempio**, **Viola = trappola da evitare**.

```
PROBABILITÀ (fondamenta)
  ├── DISCRETO: PMF → Media → Varianza → Distribuzioni notevoli
  │       └── MULTIPLO: PMF congiunta → Indipendenza → Entropia → BSC
  ├── CONTINUO: PDF/CDF → Uniforme → Esponenziale → Gaussiana → TCL
  │       └── BIVARIATO: Densità congiunta → Matrice covarianza
  └── INFERENZIALE: Decisione (MAP/ML) → Test Ipotesi (NP) → Stima (MMSE/MAP)
```

---

# 🔵 PILASTRO I — Fondamenti: Contare e Misurare l'Incertezza

## 1.1 Perché la Probabilità?

> [!abstract] L'informazione nasce dall'incertezza
> - Telecomunicazioni = trasferisce informazione *nello spazio*
> - Informatica = trasferisce informazione *nel tempo* (compressione, memorizzazione)
> - **Probabilità** = lo strumento formale che modella questa incertezza
> - Se non c'è incertezza → zero informazione da trasmettere

> [!example] Pacco amazon già noto → zero informazione. Pacco-sorpresa → informazione massima.

---

## 1.2 Spazio dei Campioni e Eventi

> [!quote] Definizioni fondamentali
> - **Esperimento** = operazione con esiti multipli possibili
> - **$\Omega$** = spazio campionario = insieme di tutti gli esiti possibili
> - **Evento $A$** = sottoinsieme di $\Omega$
> - **Evento elementare** = un singolo $\omega \in \Omega$

**Operazioni su eventi (= operazioni insiemistiche):**

| Operazione | Formula | Significato |
|---|---|---|
| Unione | $A \cup B$ | $A$ oppure $B$ |
| Intersezione | $A \cap B$ | $A$ e $B$ |
| Complemento | $A^c$ | non $A$ |
| De Morgan | $(A \cup B)^c = A^c \cap B^c$ | complemento dell'unione |

> [!danger] Riformulare l'evento in modo conveniente è spesso la chiave dell'esercizio.

---

## 1.3 Analisi Combinatoria — Saper Contare

> [!abstract] Con eventi equiprobabili: $P(A) = |A|/|\Omega|$ → saper contare è tutto

| Tipo | Formula | Nome |
|---|---|---|
| Ordinate **con** ripetizione | $n^k$ | k-uple con ripetizione |
| Ordinate **senza** ripetizione | $\frac{n!}{(n-k)!}$ | Disposizioni semplici |
| Ordinate, $k=n$ | $n!$ | Permutazioni |
| **Non** ordinate senza ripetizione | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Combinazioni |

> [!quote] Binomio di Newton: $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ → numero di sottoinsiemi di $n$ elementi

> [!example] Trucco: da disposizioni $\frac{n!}{(n-k)!}$ → vuoi non ordinate? dividi per $k!$ → vuoi con ripetizione? ognuna riparte da $n$ → $n^k$

---

## 1.4 Probabilità: Assiomi di Kolmogorov

> [!abstract] Lo spazio di probabilità è la terna $(\Omega, \mathcal{E}, P)$
> - $\mathcal{E}$ = σ-algebra (chiusa per unioni numerabili e complementi)
> - $P : \mathcal{E} \to [0,1]$ = misura di probabilità

> [!quote] I 3 Assiomi di Kolmogorov
> 1. **Non-negatività**: $P(A) \geq 0$
> 2. **Normalizzazione**: $P(\Omega) = 1$
> 3. **σ-additività**: se $A_i$ disgiunti → $P\!\left(\bigcup_i A_i\right) = \sum_i P(A_i)$

| Da questi 3 assiomi si derivano TUTTE le proprietà: | |
|---|---|
| Complemento | $P(A^c) = 1 - P(A)$ |
| Impossibile | $P(\emptyset) = 0$ |
| Unione | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |

> [!danger] $P(A) = 0$ ≠ evento impossibile. L'evento può accadere ma con frequenza nulla. Si dice "quasi certamente" (q.c.).

---

## 1.5 Probabilità Condizionata e Leggi Derivate

> [!abstract] Condizionare = restringere lo spazio campionario da $\Omega$ ad $A$
> $$P(B \mid A) = \frac{P(A \cap B)}{P(A)}, \qquad P(A) > 0$$

> [!example] Database italiano: $P(\text{peso} \geq 70)$ = guardo tutto il db. $P(\text{peso} \geq 70 \mid \text{altezza} \geq 170)$ = filtro prima le persone alte.

> [!quote] Legge della Probabilità Composta
> $$P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$$

> [!quote] Legge della Probabilità Totale — se $\{E_i\}$ è una partizione di $\Omega$
> $$P(A) = \sum_{i} P(A \mid E_i) \cdot P(E_i)$$

> [!quote] Teorema di Bayes — inverte la direzione del condizionamento
> $$P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$$
> **Significato**: aggiorna la prob. a priori $P(B)$ con le evidenze ($A$) → ottieni la prob. a posteriori.

---

## 1.6 Indipendenza Stocastica

> [!abstract] $A \perp B$ ↔ sapere $A$ non cambia la probabilità di $B$
> $$P(A \cap B) = P(A) \cdot P(B) \quad \Longleftrightarrow \quad P(B \mid A) = P(B)$$

> [!danger] Indipendenza a coppie ≠ indipendenza congiunta
> **Bit di parità**: $X_1, X_2$ indipendenti; $X_3 = X_1 \oplus X_2$. Ogni coppia è indipendente, ma la terna non lo è: noti $X_1$ e $X_2$ → $X_3$ è determinato.

> [!quote] Trucco "almeno uno": usa il complementare
> $$P(\text{almeno uno}) = 1 - P(\text{nessuno}) = 1 - \prod_i (1 - p_i)$$

---

# 🔵 PILASTRO II — Variabili Aleatorie Discrete

## 2.1 Cos'è una VA

> [!abstract] VA = funzione che porta l'incertezza nel dominio numerico
> $X : \Omega \to \mathcal{X}$ — unifica esperimenti strutturalmente identici.

## 2.2 PMF

> [!quote] $p_X(x) = P(X = x)$. Valida ↔ non-negativa e somma = 1

## 2.3 Valore Atteso

> [!abstract] Media = baricentro della distribuzione, limite della media campionaria
> $$E[X] = \mu_X = \sum_{x \in \mathcal{X}} x \cdot p_X(x)$$

> [!quote] Teorema Fondamentale: $E[g(X)] = \sum_{x} g(x) \cdot p_X(x)$ — non serve la PMF di $g(X)$

> [!danger] Media statistica ≠ media aritmetica. Coincidono SOLO nella distribuzione uniforme.

## 2.4 Varianza

> [!quote] $\sigma_X^2 = E[(X - \mu_X)^2] = E[X^2] - \mu_X^2$
> - $E[aX + b] = aE[X] + b$
> - $\text{Var}(aX+b) = a^2 \text{Var}(X)$ (invariante per traslazione, covariante per scala)

## 2.5 Disuguaglianze Fondamentali

> [!quote] Markov (VA non negative): $P(X \geq \delta) \leq \frac{E[X]}{\delta}$

> [!quote] Chebyshev (universale, qualunque distribuzione con varianza finita):
> $$P(|X - \mu_X| \geq k\sigma_X) \leq \frac{1}{k^2}$$

---

## 2.6 Distribuzioni Discrete Notevoli

### Bernoulli Ber$(p)$
> [!quote] Alfabeto $\{0,1\}$. $p_X(1)=p$, $p_X(0)=1-p$. $E[X] = p$

### Binomiale Bin$(n,p)$ — somma di $n$ Bernoulli i.i.d.
> [!quote] $$P(S_n = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad E[S_n] = np$$

### Uniforme Discreta
> [!quote] $p_X(a_k) = 1/M$. $E[X] =$ media aritmetica dell'alfabeto. Su $\{1,\ldots,M\}$: $E[X] = (M+1)/2$

### Poisson Poi$(\lambda)$ — eventi rari in un intervallo
> [!quote] $$P(X=k) = \frac{\lambda^k}{k!}e^{-\lambda}, \quad E[X] = \lambda$$
> Somma di Poi indipendenti: $\text{Poi}(\lambda_1) + \text{Poi}(\lambda_2) = \text{Poi}(\lambda_1+\lambda_2)$

### Geometrica Geo$(p)$ — tempo al primo successo
> [!quote] $$P(X=k) = (1-p)^{k-1}p, \quad E[X] = \frac{1}{p}$$
> **Assenza di memoria** (unica discreta con questa proprietà): $P(X > n+m \mid X > n) = P(X > m)$

---

## 2.7 PMF Condizionata e Media Condizionale

> [!quote] $p_{X|C}(x) = P(X=x,C)/P(C)$ — è una PMF valida sul supporto di $C$

> [!quote] Scomposizione della media per partizione $\{E_i\}$:
> $$E[X] = \sum_{i} P(E_i) \cdot E[X \mid E_i]$$

## 2.8 Covarianza e Correlazione

> [!quote] $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$
> $$\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}, \quad -1 \leq \rho_{XY} \leq 1$$

> [!danger] Indipendenza → incorrelazione. Ma incorrelazione NON → indipendenza. Eccezione: nel caso gaussiano sono equivalenti.

---

# 🔵 PILASTRO III — Variabili Multiple Discrete e Teoria dell'Informazione

## 3.1 PMF Congiunta

> [!abstract] Per due VA serve la tabella congiunta — le marginali da sole non bastano
> $$p_{XY}(x,y) = P(X=x, Y=y) \geq 0, \quad \sum_{x,y} p_{XY}(x,y) = 1$$

> [!danger] Congiunta → Marginali (sempre). Marginali → Congiunta (solo se indipendenti)

## 3.2 Marginalizzazione

> [!quote] $p_X(x) = \sum_y p_{XY}(x,y)$ — somma sulla variabile "non voluta"

> [!quote] Marginalizzazione come media: $p_X(x) = E_Y[p_{X|Y}(x \mid Y)]$

## 3.3 Indipendenza tra VA

> [!quote] $X \perp Y \iff p_{XY}(x,y) = p_X(x) \cdot p_Y(y) \quad \forall x,y$

## 3.4 PMF Condizionale

> [!quote] $p_{X|Y}(x|y) = p_{XY}(x,y)/p_Y(y)$
> Ogni colonna somma a 1 (condizionamento fisso). Le righe NO.

## 3.5 Catene di Markov

> [!abstract] Markov = il futuro dipende SOLO dallo stato presente, non dalla storia
> $$P(X_{n+1} \mid X_n, X_{n-1}, \ldots) = P(X_{n+1} \mid X_n)$$

> [!quote] Indipendenza condizionale: $X_1 \perp X_3 \mid X_2$ nelle catene di Markov

---

## 3.6 Entropia di Shannon

> [!abstract] Informazione di un evento: $I(A) = -\log_2 P(A)$ [bit]
> - Evento certo ($P=1$): $I=0$ bit
> - Evento raro ($P=1/1024$): $I=10$ bit

> [!quote] Entropia = informazione media di una sorgente
> $$H(X) = -\sum_{x} p_X(x) \log_2 p_X(x) \quad \text{[bit]}$$
> - $H = 0$ ↔ $X$ deterministica
> - $H$ massima ↔ $X$ uniforme: $H_{max} = \log_2 |\mathcal{X}|$
> - Bernoulli con $p=1/2$: $H=1$ bit (massimo per binaria)

> [!example] File compresso idealmente: ogni bit è equiprobabile e indipendente → $H=1$ bit/bit → non comprimibile ulteriormente.

---

## 3.7 Canale Binario Simmetrico (BSC)

> [!abstract] Modello di canale rumoroso: flip di bit con probabilità $\varepsilon$
> $$P(\text{errore}) = \varepsilon \quad \text{(indipendente dalla distribuzione dell'input)}$$

> [!danger] Il caso peggiore è $\varepsilon = 1/2$ (non $\varepsilon = 1$!)
> Con $\varepsilon=1$: inverto l'output e recupero tutto. Con $\varepsilon=1/2$: $Y$ è indipendente da $X$ → zero informazione trasmessa.

---

# 🔵 PILASTRO IV — Variabili Aleatorie Continue

## 4.1 Il Passaggio al Continuo

> [!abstract] Nel continuo: $P(X = x) = 0$ per ogni singolo punto. La probabilità si assegna ad intervalli.

> [!danger] La PDF non è una probabilità — è una densità. Può essere $> 1$. La probabilità è l'AREA sotto la curva.

## 4.2 CDF

> [!quote] $F_X(x) = P(X \leq x)$ — definita per qualsiasi VA
> - $F_X(-\infty) = 0$, $F_X(+\infty) = 1$, monotona crescente
> - $P(a < X \leq b) = F_X(b) - F_X(a)$

## 4.3 PDF

> [!quote] $f_X(x) = F_X'(x)$, $\quad F_X(x) = \int_{-\infty}^x f_X(t)dt$
> $$E[X] = \int_{-\infty}^{+\infty} x \cdot f_X(x) \, dx$$

---

## 4.4 Distribuzioni Continue Notevoli

### Uniforme $U(a,b)$
> [!quote] $f_X(x) = \frac{1}{b-a}$ su $[a,b]$. $E[X] = \frac{a+b}{2}$. $\text{Var}(X) = \frac{(b-a)^2}{12}$
> CDF = rampa lineare da 0 a 1.

### Esponenziale Exp$(\lambda)$ — tempo di attesa Poissoniano
> [!quote] $f_X(x) = \lambda e^{-\lambda x}$ per $x \geq 0$. $F_X(x) = 1 - e^{-\lambda x}$. $E[X] = 1/\lambda$
> **Assenza di memoria** (unica continua con questa proprietà) → parallelo con [[#Geometrica Geo$(p)$]]

### Laplace Lap$(\lambda)$ — doppia esponenziale
> [!quote] $f_X(x) = \frac{\lambda}{2}e^{-\lambda|x|}$. $E[X]=0$. $\text{Var}(X) = 2/\lambda^2$
> Code più pesanti della gaussiana → modella rumore impulsivo.

---

## 4.5 PDF Condizionata

> [!quote] Dato evento $A$: $f_{X|A}(x) = f_X(x)/P(A)$ per $x \in A$, 0 altrove
> Si restringe il supporto e si riscala per normalizzare.

---

## 4.6 Variabili Continue Bivariate

> [!quote] PDF congiunta: $f_{X,Y}(x,y) \geq 0$, $\iint f_{X,Y} = 1$
> - Marginali: $f_X(x) = \int f_{X,Y}(x,y)dy$
> - Indipendenza: $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$
> - Condizionale: $f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y)$
> - CDF → PDF: $f_{X,Y} = \frac{\partial^2 F_{X,Y}}{\partial x \partial y}$

> [!danger] Gli integrali $n$-pli con $n>2$ sono rari in pratica. Cerca sempre simmetrie o condizionamenti per evitarli.

---

# 🔵 PILASTRO V — Vettori Aleatori, Convoluzione e Processi

## 5.1 Vettori Aleatori e Matrice di Covarianza

> [!abstract] Per $n$ VA congiunte → si usa la notazione vettoriale
> $$\mathbf{X} = (X_1, \ldots, X_n)^T, \quad \boldsymbol{\mu} = E[\mathbf{X}]$$

> [!quote] Matrice di Covarianza $K$ (simmetrica, semidefinita positiva)
> $$K_{ij} = \text{Cov}(X_i, X_j), \quad K_{ii} = \sigma_i^2$$
> Fondamentale per: PCA, Filtro di Kalman, Stima MMSE.

> [!quote] Correlazione normalizzata
> $$\rho_{12} = \frac{\text{Cov}(X_1, X_2)}{\sigma_1 \sigma_2}, \quad -1 \leq \rho_{12} \leq 1$$
> $\rho = \pm 1$ ↔ relazione lineare perfetta. $\rho = 0$ ↔ incorrelate (non necessariamente indipendenti).

---

## 5.2 Convoluzione — Somma di VA Indipendenti

> [!abstract] Se $X \perp Y$ continue, la PDF della somma $Z = X + Y$ è la convoluzione delle PDF
> $$(f_X * f_Y)(z) = \int_{-\infty}^{+\infty} f_X(x) \cdot f_Y(z-x) \, dx$$

> [!example] Applicazioni: sistemi lineari (LTI), CNN (reti neurali convoluzionali), filtraggio audio/immagini.

---

## 5.3 Teorema Centrale del Limite (TCL)

> [!abstract] Somma di tante VA i.i.d. → converge alla Gaussiana, qualunque sia la distribuzione originale
> Siano $X_1, \ldots, X_n$ i.i.d. con media $\mu$ e varianza $\sigma^2$. Per $n \to \infty$:
> $$Z_n = \frac{\sum_i X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)$$

> [!example] Il rumore termico è gaussiano perché è la somma di milioni di eventi di scattering indipendenti — nessuno è dominante, tutti contribuiscono ugualmente.

> [!quote] Convergenze: più forte → più debole
> - Con prob. 1 (Legge Forte GN) → in probabilità (Legge Debole GN)
> - In media quadratica → in probabilità
> - Le prime due non si implicano a vicenda

---

## 5.4 Processi Stocastici

> [!abstract] Processo stocastico = famiglia di VA indicizzate dal tempo $\{X(t)\}$
> - Fissa $t$ → VA (istantanea)
> - Fissa $\omega$ → realizzazione/traiettoria (funzione deterministica del tempo)

**Tipi:**
- **Discreto** ($\mathcal{T} = \mathbb{N}$): sequenze — prezzi azionari, campioni audio
- **Continuo** ($\mathcal{T} = \mathbb{R}$): traiettorie — rumore termico, moto Browniano

> [!quote] Processo di Poisson con intensità $\lambda$
> $$P(N(t) = k) = \frac{(\lambda t)^k}{k!} e^{-\lambda t}$$
> Incrementi indipendenti e stazionari, assenza di memoria.

> [!quote] Stazionarietà in senso lato (WSS)
> - $E[X(t)]$ costante nel tempo
> - $\text{Var}(X(t))$ costante nel tempo
> - $\text{Cov}(X(t_1), X(t_2))$ dipende solo da $t_1 - t_2$

---

# 🔵 PILASTRO VI — Statistica Inferenziale

## 6.1 Due Rami dell'Inferenza

> [!abstract] Statistica inferenziale = bottom-up: dai dati si inferisce la popolazione
> - **Test di Ipotesi**: decidere in quale stato discreto si trova la natura ($H_1, \ldots, H_M$)
> - **Stima Parametrica**: determinare il valore continuo di un parametro nascosto $\theta$

> [!danger] Statistica descrittiva ≠ inferenziale
> La statistica descrittiva ("Excel") descrive solo il campione osservato. L'inferenziale **generalizza** a tutta la popolazione futura con gli stessi parametri statistici.

---

## 6.2 Convergenze di Successioni di VA

> [!quote] Tre tipi di convergenza (dal più forte al più debole)
> 1. **Con probabilità 1** (Legge Forte GN): $P\!\left(\lim_{n\to\infty} Y_n = Y\right) = 1$
> 2. **In media quadratica**: $\lim_{n\to\infty} E[(Y_n - Y)^2] = 0$ → implica conv. in prob.
> 3. **In probabilità** (Legge Debole GN): $\lim_{n\to\infty} P(|Y_n - Y| > \varepsilon) = 0$
> 4. **In distribuzione** (TCL): la CDF di $Y_n$ converge a quella di $Y$ (la più debole)

> [!quote] Legge Debole dei Grandi Numeri — dimostrazione via Chebyshev
> La media campionaria $\bar{X}_n = \frac{1}{n}\sum X_i$ ha:
> $$E[\bar{X}_n] = \mu, \quad \text{Var}(\bar{X}_n) = \frac{\sigma^2}{n} \xrightarrow{n\to\infty} 0$$
> Per Chebyshev: $P(|\bar{X}_n - \mu| > \varepsilon) \leq \frac{\sigma^2}{n\varepsilon^2} \to 0$ → **converge in probabilità a $\mu$**.

---

## 6.3 Test di Ipotesi Bayesiano

### Setup generale

> [!abstract] Il problema: i dati $\mathbf{x}^n$ sono generati da quale ipotesi $H_i$?
> - **Osservabili**: $\mathbf{x}^n \in \mathcal{X}^n$ (vettore di $n$ campioni)
> - **Ipotesi**: $H_1, \ldots, H_M$ (stati della natura mutualmente esclusivi)
> - **Verosimiglianza**: $P(\mathbf{x}^n \mid H_i)$ (PMF) o $f(\mathbf{x}^n \mid H_i)$ (PDF)
> - **Probabilità a priori**: $\pi_i = P(H_i)$, con $\sum_i \pi_i = 1$

### Rischio Bayesiano

> [!quote] Matrice dei costi $C_{ij}$ = costo di decidere $H_i$ quando è vera $H_j$
> $$R_B = \sum_{i,j} c_{ij} P(\text{decide } H_i, H_j \text{ vera})$$
> La regola ottima **minimizza** $R_B$.

### Regola MAP (Minimum Probability of Error)

> [!quote] Con costi $c_{ii}=0$, $c_{ij}=1$ per $i\neq j$: minimizzare $R_B$ = minimizzare $P_e$

> [!quote] Regola MAP (Maximum A Posteriori)
> $$\text{Decide } H_k \iff k = \arg\max_i \pi_i \cdot f(\mathbf{x}^n \mid H_i) = \arg\max_i P(H_i \mid \mathbf{x}^n)$$
> Scegli l'ipotesi con la **probabilità a posteriori massima**.

> [!quote] Regola ML (Maximum Likelihood) — caso speciale di MAP con $\pi_i$ uguali
> $$\text{Decide } H_k \iff k = \arg\max_i f(\mathbf{x}^n \mid H_i)$$
> Si usa quando non si conoscono le probabilità a priori o sono equiprobabili.

---

## 6.4 Likelihood Ratio Test (LRT)

> [!abstract] Per $M=2$ ipotesi, MAP si riduce al confronto del rapporto di verosimiglianza
> $$L(\mathbf{x}^n) = \frac{f(\mathbf{x}^n \mid H_1)}{f(\mathbf{x}^n \mid H_0)} \underset{H_0}{\overset{H_1}{\gtrless}} \eta, \quad \eta = \frac{\pi_0}{\pi_1}$$
> In pratica si usa il **log-LRT** (logaritmo monotono crescente — non cambia la decisione).

---

## 6.5 Esempio: Test sulla Media di Gaussiane I.I.D.

> [!abstract] $H_1: X_i \sim \mathcal{N}(\mu_1, \sigma^2)$ vs $H_0: X_i \sim \mathcal{N}(\mu_0, \sigma^2)$, con $\mu_1 > \mu_0$, $\pi_1 = \pi_0$

> [!quote] Derivazione del test ottimo (ML/LRT)
> Calcolando il log-LRT e semplificando i termini comuni in $\sum x_i^2$:
> $$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n x_i \underset{H_0}{\overset{H_1}{\gtrless}} \frac{\mu_1 + \mu_0}{2}$$
> La **statistica sufficiente** è la media campionaria $\bar{X}_n$.

> [!abstract] Concetto di Statistica Sufficiente
> Tutta l'informazione rilevante per la decisione ottima è condensata in una funzione scalare dei dati. Qualunque altra elaborazione è ridondante.

> [!quote] Probabilità di errore del test Gaussiano
> Sotto $H_j$: $\bar{X}_n \sim \mathcal{N}(\mu_j, \sigma^2/n)$. Normalizzando:
> $$P_e = Q\!\left(\frac{\sqrt{n}(\mu_1 - \mu_0)}{2\sigma}\right), \quad Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^\infty e^{-t^2/2}dt$$
> All'aumentare di $n$: $P_e \to 0$ **esponenzialmente**. ← Il potere della LLN.

---

## 6.6 Esempi di Statistiche Sufficienti

| Distribuzione | Statistica Sufficiente |
|---|---|
| Gaussiane, test sulla media | Media campionaria $\bar{X}_n$ |
| Poisson, test sulla media | Somma $\sum X_i$ (che è Poi$(n\lambda)$) |
| Gaussiane a media nulla, test sulla varianza | Momento secondo $\frac{1}{n}\sum X_i^2$ (Chi-quadro) |

---

## 6.7 Criterio di Neyman-Pearson

> [!abstract] Si usa quando non si conoscono le probabilità a priori né i costi
> Si fissa l'ipotesi nulla $H_0$ ("quiete") e l'alternativa $H_1$ ("segnale").

> [!quote] Tipi di errore
> - **Falso Allarme** (Errore tipo I): $P_{FA} = P(\text{decide }H_1 \mid H_0) = \alpha$
> - **Mancata Rivelazione** (Errore tipo II): $P_M = P(\text{decide }H_0 \mid H_1) = \beta$
> - **Potenza** (Probabilità di Rivelazione): $P_D = 1 - \beta$

> [!danger] Non si può minimizzare $\alpha$ e $\beta$ contemporaneamente
> Decidere sempre $H_1$ → $P_M = 0$ ma $P_{FA} = 1$. Decidere sempre $H_0$ → $P_{FA} = 0$ ma $P_M = 1$.

> [!quote] Lemma di Neyman-Pearson — il test ottimo sotto il vincolo $P_{FA} \leq \alpha_0$
> $$L(\mathbf{x}^n) = \frac{f(\mathbf{x}^n \mid H_1)}{f(\mathbf{x}^n \mid H_0)} \underset{H_0}{\overset{H_1}{\gtrless}} \eta$$
> dove $\eta$ si sceglie per soddisfare **esattamente** $P_{FA} = \alpha_0$:
> $$P(L(\mathbf{X}^n) > \eta \mid H_0) = \alpha_0$$

---

## 6.8 Teoria della Stima Bayesiana

> [!abstract] La stima parametrica: $\theta$ è continuo e ignoto, si stima da $\mathbf{x}^n$
> Nell'approccio Bayesiano: $\theta$ è una **VA continua** con densità a priori nota $f_\theta(\theta)$.

> [!quote] Teorema di Bayes per la densità a posteriori
> $$f(\theta \mid \mathbf{x}^n) = \frac{f(\mathbf{x}^n \mid \theta) \cdot f_\theta(\theta)}{f(\mathbf{x}^n)}$$

---

## 6.9 Stimatore MMSE

> [!abstract] MMSE = Minimum Mean Square Error — minimizza $E[(\theta - \hat{\theta})^2]$

> [!quote] Teorema Fondamentale dello Stimatore MMSE
> $$\hat{\theta}_{MMSE}(\mathbf{x}^n) = E[\theta \mid \mathbf{X}^n = \mathbf{x}^n]$$
> Lo stimatore ottimo (a minimo MSE) è la **media condizionata a posteriori**.

> [!example] Derivazione: $E[(\theta-\hat\theta)^2] = E_X[E_{\theta|X}[(\theta-\hat\theta)^2|X]]$. Per minimizzare l'integrale esterno, si minimizza per ogni $x^n$ → il minimo è la media condizionale $E[\theta|x^n]$.

---

## 6.10 Stimatore MAP (per parametri continui)

> [!abstract] MAP continuo: usa la funzione di costo "hit-or-miss" (tolleranza $\epsilon \to 0$)
> Il test ottimo è la **moda** della distribuzione a posteriori:
> $$\hat{\theta}_{MAP}(\mathbf{x}^n) = \arg\max_\theta f(\theta \mid \mathbf{x}^n) = \arg\max_\theta \left[\ln f(\mathbf{x}^n \mid \theta) + \ln f_\theta(\theta)\right]$$

---

## 6.11 Caso di Studio: Sorgente Bernoulli con Prior Uniforme

> [!abstract] Setup: $n$ bit i.i.d. con probabilità di $1$ pari a $\theta \in [0,1]$ ignoto. Prior: $\theta \sim U[0,1]$.

> [!quote] Verosimiglianza (Bernoulli i.i.d.)
> $$P(\mathbf{x}^n \mid \theta) = \theta^{w_H}(1-\theta)^{n-w_H}$$
> dove $w_H = \sum x_i$ è il **Peso di Hamming** (numero di $1$ nella stringa).

> [!quote] Distribuzione a posteriori (Beta)
> $$f(\theta \mid \mathbf{x}^n) = (n+1)\binom{n}{w_H} \theta^{w_H}(1-\theta)^{n-w_H}$$
> Questa è una distribuzione **Beta** di parametri $(w_H+1, n-w_H+1)$.

> [!quote] Confronto MMSE vs MAP
> $$\hat\theta_{MMSE} = \frac{w_H + 1}{n + 2} \qquad \hat\theta_{MAP} = \frac{w_H}{n}$$
> - **MAP** = frequenza relativa (stimatore ovvio, non polarizzato)
> - **MMSE** = aggiunge un successo e un fallimento virtuali (regola di Laplace) — MSE globale inferiore

---

## 6.12 Proprietà degli Stimatori

### Bias (Polarizzazione)

> [!quote] $B(\theta) = E[\hat{\theta}(\mathbf{X}^n) \mid \theta] - \theta$
> - **Non polarizzato** (unbiased): $B(\theta) = 0$ per ogni $\theta$
> - **Asintoticamente non polarizzato**: $B(\theta) \to 0$ per $n \to \infty$

| Stimatore | Bias |
|---|---|
| MAP = $w_H/n$ | $B=0$ (non polarizzato) |
| MMSE = $(w_H+1)/(n+2)$ | $B = \frac{1-2\theta}{n+2} \neq 0$, ma $\to 0$ per $n\to\infty$ |

### Consistenza

> [!quote] Uno stimatore è **consistente** se il MSE $\to 0$ per $n \to \infty$
> $$\lim_{n\to\infty} E[(\hat\theta_n - \theta)^2 \mid \theta] = 0$$
> Per Chebyshev: consistenza in MSE → consistenza in probabilità.

> [!quote] MSE globale (mediato sul prior $U[0,1]$)
> $$E[(\hat\theta_{MMSE} - \theta)^2] = \frac{1}{6(n+2)} < \frac{1}{6n} = E[(\hat\theta_{MAP} - \theta)^2]$$
> Per ogni $n$ finito: **MMSE batte MAP** nel MSE globale. Entrambi sono consistenti ($\sim 1/n$).

---

# 🔗 Mappa Zettelkasten — Connessioni Chiave

| Concetto | Si collega a |
|---|---|
| Legge dei Grandi Numeri | [[#2.3 Valore Atteso]], [[#6.2 Convergenze di Successioni di VA]] |
| Binomiale = somma di Bernoulli | [[#2.6.1 Bernoulli Ber$(p)$]], [[#2.6.2 Binomiale Bin$(n,p)$]] |
| Poisson = limite della Binomiale | [[#2.6.4 Poisson Poi$(\lambda)$]] |
| Geometrica discreta ~ Esponenziale continua | [[#2.6.5 Geometrica Geo$(p)$]], [[#4.4 Distribuzioni Continue Notevoli]] |
| Probabilità a posteriori | [[#1.5 Probabilità Condizionata]], [[#6.8 Teoria della Stima Bayesiana]] |
| MAP classifica/stima | [[#6.3 Test di Ipotesi Bayesiano]], [[#6.10 Stimatore MAP (per parametri continui)]] |
| TCL → Gaussiana ubiqua | [[#5.3 Teorema Centrale del Limite (TCL)]], [[#6.5 Esempio: Test sulla Media di Gaussiane I.I.D.]] |
| Chebyshev dimostra LGN e consistenza | [[#2.5 Disuguaglianze Fondamentali]], [[#6.12 Proprietà degli Stimatori]] |
| Statistica sufficiente | [[#6.5 Esempio: Test sulla Media di Gaussiane I.I.D.]], [[#6.6 Esempi di Statistiche Sufficienti]] |
