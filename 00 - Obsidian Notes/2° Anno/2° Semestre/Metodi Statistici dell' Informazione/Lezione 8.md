---
date: 2026-03-31
corso: Modelli Statistici e Probabilità
docente: N/D
lezione: Teorema della media condizionale, covarianza, correlazione e introduzione alle variabili continue
tags: [MSP, media-condizionale, covarianza, correlazione, matrice-covarianza, variabili-continue, densita-probabilita]
---

# MSP — Lezione 8: Media Condizionale, Covarianza e Introduzione alle Variabili Continue
---

>[!question] Argomenti trattati
>- Riepilogo: PMF congiunta, marginalizzazione, indipendenza, PMF condizionale
>- Teorema della media condizionale (law of total expectation)
>- Esercizio: distribuzione del numero di pacchetti in errore (Poissonian → Poissonian)
>- Covarianza tra due variabili aleatorie
>- Coefficiente di correlazione e sue proprietà ($\rho \in [-1, 1]$)
>- Dimostrazione algebrica e geometrica (Cauchy-Schwarz) di $|\rho| \leq 1$
>- Matrice di covarianza per vettori aleatori
>- Introduzione alle variabili aleatorie continue: densità di probabilità

---

## Riepilogo rapido: PMF congiunta e condizionale

- **PMF congiunta** di $(X, Y)$: tabella di $|\mathcal{X}| \times |\mathcal{Y}|$ numeri non negativi che sommano a 1.
- **Marginalizzazione**: $p_X(x) = \sum_y p_{XY}(x,y)$ e $p_Y(y) = \sum_x p_{XY}(x,y)$.
- **Indipendenza**: $p_{XY}(x,y) = p_X(x) \cdot p_Y(y)$.
- **PMF condizionale**: $p_{X|Y}(x|y) = \frac{p_{XY}(x,y)}{p_Y(y)}$. Per $Y$ fisso è una legge di probabilità.
- **Legge di Bayes**: $p_{X|Y}(x|y) \cdot p_Y(y) = p_{Y|X}(y|x) \cdot p_X(x)$.
- **Indipendenza condizionale e catene di Markov**: $(X_1, X_2, X_3)$ è una catena di Markov se $X_1$ e $X_3$ sono condizionalmente indipendenti dato $X_2$.

---

## Teorema della media condizionale

La proprietà di marginalizzazione si può rileggere in termini di valor medio:

$$p_X(x) = \sum_y p_{XY}(x,y) = \sum_y p_{X|Y}(x|y) \cdot p_Y(y)$$

Il secondo membro è la media (rispetto a $Y$) della PMF condizionale di $X$ dato $Y$:

$$p_X(x) = E_Y\!\left[p_{X|Y}(x|Y)\right]$$

> [!abstract] Teorema della media condizionale
> Siano $X$ e $Y$ variabili aleatorie con PMF congiunta. Allora:
> $$E[g(X,Y)] = E_Y\!\left[E_{X|Y}\!\left[g(X,Y) \mid Y\right]\right]$$
> Cioè, la media di una funzione di $(X,Y)$ si può calcolare come media rispetto a $Y$ della media condizionale rispetto a $X$ dato $Y$.

**Linearità della media**: per qualsiasi $a, b$:

$$E[aF(X) + bG(Y)] = a \cdot E[F(X)] + b \cdot E[G(Y)]$$

La dimostrazione usa la proprietà di marginalizzazione e non richiede l'indipendenza di $X$ e $Y$.

---

## Esercizio: distribuzione poissoniana dell'errore

**Setup**: Una coda di un router ha $N$ pacchetti, con $N \sim \text{Poisson}(\lambda)$:

$$P(N=k) = \frac{\lambda^k}{k!} e^{-\lambda}, \quad k \geq 0$$

Una frazione $p$ dei pacchetti è in errore, indipendentemente. Sia $M$ il numero di pacchetti in errore. Trovare $P(M = m)$.

**Soluzione tramite media condizionale**:

$$P(M=m) = \sum_{n=0}^{\infty} P(M=m | N=n) \cdot P(N=n)$$

Dato $N = n$, ogni pacchetto è in errore con probabilità $p$ indipendentemente: quindi $M | N=n \sim \text{Binomiale}(n, p)$.

$$P(M=m | N=n) = \binom{n}{m} p^m (1-p)^{n-m}, \quad m \leq n$$

Sostituendo e svolgendo il calcolo (con la sostituzione $\ell = n - m$):

$$P(M=m) = \frac{(\lambda p)^m}{m!} e^{-\lambda p}$$

> [!abstract] Risultato: proprietà di chiusura della distribuzione di Poisson
> $$M \sim \text{Poisson}(\lambda p)$$
> La somma di una variabile poissoniana con $N$ prove bernoulliane indipendenti di parametro $p$ è ancora poissoniana, con media $\lambda p$.

> [!example] Applicazione pratica
> Se le macchine in coda a un semaforo seguono una distribuzione di Poisson di media 10, e il 20% sono di fabbricazione italiana, allora le macchine italiane in coda seguono una Poisson di media 2. Questa proprietà rende la distribuzione di Poisson estremamente utile nella teoria delle code.

---

## Covarianza

> [!abstract] Definizione: Covarianza
> Date due variabili aleatorie $X$ e $Y$, la **covarianza** è:
> $$\text{Cov}(X,Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - \mu_X \mu_Y$$
> dove $\mu_X = E[X]$ e $\mu_Y = E[Y]$.

La seconda formula si ottiene sviluppando il prodotto e usando la linearità della media.

**Se $X$ e $Y$ sono indipendenti**:

$$\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = E[X]E[Y] - E[X]E[Y] = 0$$

Le variabili indipendenti sono **incorrelate** (covarianza nulla).

> [!warning] Incorrelate $\not\Rightarrow$ Indipendenti
> La covarianza nulla non implica l'indipendenza. Si può costruire un esempio di variabili dipendenti con covarianza zero. L'implicazione vale solo nel caso gaussiano.

**Interpretazione**: la covarianza è positiva se deviazioni positive di $X$ dalla sua media tendono ad accompagnarsi a deviazioni positive di $Y$; negativa se tendono a essere di segno opposto.

---

## Coefficiente di correlazione

> [!abstract] Definizione: Coefficiente di correlazione
> $$\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$$
> dove $\sigma_X, \sigma_Y$ sono le deviazioni standard di $X$ e $Y$.

**Proprietà**: $-1 \leq \rho_{XY} \leq 1$.

### Dimostrazione algebrica

Consideriamo $Z = \frac{X - \mu_X}{\sigma_X} \pm \frac{Y - \mu_Y}{\sigma_Y}$. Poiché $E[Z^2] \geq 0$:

$$E[Z^2] = E\!\left[\left(\frac{X-\mu_X}{\sigma_X}\right)^2\right] \pm 2 E\!\left[\frac{(X-\mu_X)(Y-\mu_Y)}{\sigma_X\sigma_Y}\right] + E\!\left[\left(\frac{Y-\mu_Y}{\sigma_Y}\right)^2\right] = 1 \pm 2\rho_{XY} + 1 \geq 0$$

Quindi $2 \pm 2\rho_{XY} \geq 0$, cioè $-1 \leq \rho_{XY} \leq 1$.

### Dimostrazione geometrica (Cauchy-Schwarz)

L'insieme delle variabili aleatorie con varianza finita forma uno spazio vettoriale con prodotto scalare $\langle X, Y \rangle = \text{Cov}(X,Y)$ e norma $\|X\| = \sigma_X$. Per la disuguaglianza di Cauchy-Schwarz:

$$|\langle X, Y \rangle| \leq \|X\| \cdot \|Y\| \implies |\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y \implies |\rho_{XY}| \leq 1$$

**Uguaglianza**: $\rho = 1$ sse $X - \mu_X = k(Y - \mu_Y)$ con $k > 0$ (proporzionalità diretta). $\rho = -1$ sse $k < 0$ (proporzionalità inversa).

Il coefficiente di correlazione è un **indice di predecibilità lineare**: misura quanto bene $Y$ può essere predetto da $X$ con una relazione affine. Non misura predecibilità non-lineare.

---

## Matrice di covarianza

Per un vettore aleatorio $\mathbf{x} = (X_1, X_2)^T$, si definisce la **matrice di covarianza**:

$$K_{\mathbf{x}} = E\!\left[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^T\right] = \begin{pmatrix} \sigma_{X_1}^2 & \text{Cov}(X_1, X_2) \\ \text{Cov}(X_1, X_2) & \sigma_{X_2}^2 \end{pmatrix}$$

**Proprietà**: la matrice di covarianza è **definita non negativa** (semidefinita positiva), cioè $\mathbf{a}^T K \mathbf{a} \geq 0$ per ogni vettore $\mathbf{a}$.

Il caso si generalizza a $n$ variabili: la matrice $K$ è $n \times n$, con $K_{ij} = \text{Cov}(X_i, X_j)$.

> [!info] Importanza nella data analysis e nel machine learning
> La matrice di covarianza è fondamentale in machine learning, analisi dei componenti principali (PCA), stima MMSE (Minimum Mean Square Error) e in generale in tutti i metodi statistici che lavorano con vettori di dati. Se $K$ è diagonale, le variabili sono incorrelate.

---

## Introduzione alle variabili aleatorie continue

### Perché le variabili continue

In molte applicazioni fisiche e ingegneristiche, la variabile aleatoria assume valori in un continuo (reali, non numerabili). Per esempio, la tensione di rumore ai capi di un conduttore è una variabile continua: ogni misura dà un valore diverso, e se si avesse uno strumento a precisione infinita si osserverebbero numeri reali, non razionali.

### Il problema della PMF per variabili continue

Per una variabile aleatoria continua, la probabilità che assuma un valore esatto è zero:

$$P(X = x_0) = 0 \quad \forall x_0$$

Questo perché i valori reali in un intervallo sono non numerabili, e assegnare una probabilità finita a ogni punto violerebbe la normalizzazione. Quindi la PMF (definita per valori discreti) non si può usare direttamente.

### Densità di probabilità

Analogia con la densità di massa in fisica: la densità è definita come il limite del rapporto tra la massa di un segmento e la sua lunghezza quando il segmento tende a zero.

In modo analogo, si definisce la **funzione densità di probabilità (PDF)**:

$$f_X(x) = \lim_{\delta x \to 0} \frac{P(x - \delta x/2 \leq X \leq x + \delta x/2)}{\delta x}$$

> [!abstract] Definizione: Densità di probabilità
> La funzione $f_X : \mathbb{R} \to \mathbb{R}$ è la **densità di probabilità** di $X$ se:
> $$P(a \leq X \leq b) = \int_a^b f_X(x)\, dx$$
> con $f_X(x) \geq 0$ e $\int_{-\infty}^{+\infty} f_X(x)\, dx = 1$.

> [!warning] La densità non è una probabilità
> $f_X(x_0)$ non è la probabilità che $X = x_0$. La probabilità di un singolo punto è 0. La densità è la "concentrazione" di probabilità in un intorno di $x_0$: più è alta, più è probabile trovare $X$ vicino a $x_0$.

> [!tip] Parole del Professore
> > [!quote]
> > "Chiamare il massimo della densità il 'valore più probabile' mi dà una pugnalata a sangue freddo. Il massimo della densità si chiama correttamente il valore modale."

La teoria sarà ripresa in dettaglio nella prossima lezione, con il concetto di **funzione di distribuzione cumulativa (CDF)** e con tutti gli strumenti del caso continuo.

## Teorema del Limite Centrale (CLT) (Introdotto dopo)

### Enunciato informale

Il **Teorema del Limite Centrale** è uno dei risultati fondamentali della probabilità e della statistica. In forma semplificata, esso afferma che:

> [!abstract] Teorema del Limite Centrale (versione semplice)
> Siano $X_1, X_2, \ldots, X_n$ variabili aleatorie **indipendenti identicamente distribuite** (i.i.d.) con media $\mu$ e varianza $\sigma^2$ finite. Allora, per $n$ grande, la **somma standardizzata**:
> $$Z_n = \frac{\sum_{i=1}^{n} X_i - n\mu}{\sqrt{n}\sigma}$$
> tende a una **distribuzione Gaussiana** di media 0 e varianza 1 (distribuzione normale standard $\mathcal{N}(0,1)$).

In altre parole, le variabili aleatorie originali possono avere qualunque distribuzione; purché siano indipendenti e identicamente distribuite, la loro somma (opportunamente standardizzata) tende a una gaussiana.

### Implicazione pratica

Se $S_n = X_1 + X_2 + \cdots + X_n$, allora per $n$ grande:

$$S_n \approx \mathcal{N}(n\mu, n\sigma^2)$$

Cioè: media $n\mu$ e varianza $n\sigma^2$.

> [!example] Lanciamento di un dado
> Un dado onesto ha media $\mu = 3.5$ e varianza $\sigma^2 \approx 2.917$. Se si lanciano 100 dadi indipendenti e si sommano i risultati:
> - Media della somma: $100 \times 3.5 = 350$
> - Varianza della somma: $100 \times 2.917 = 291.7$
> - Deviazione standard: $\sqrt{291.7} \approx 17$
> Per il CLT, la distribuzione della somma è **approssimativamente gaussiana**.

### Perché è così importante

Il CLT giustifica l'uso diffuso della distribuzione gaussiana in statistica, anche quando i dati individuali non sono gaussiani. Medietà aritmetica di dati i.i.d. tende a essere gaussiana (normalizzata): questo è il fondamento dell'**inferenza statistica** mediante intervalli di confidenza e test d'ipotesi.

---

## Distribuzione Esponenziale (Introdotto dopo)

### Motivazione e definizione

La distribuzione esponenziale modella il **tempo di attesa** tra eventi successivi in un processo di Poisson. È la distribuzione continua dell'assenza di memoria (analoga alla distribuzione geometrica nel caso discreto).

> [!abstract] Definizione: Distribuzione Esponenziale
> Una variabile aleatoria continua $X$ segue una **distribuzione esponenziale** di parametro $\lambda > 0$ (indicato $X \sim \text{Exp}(\lambda)$) se la sua **densità di probabilità** è:
> $$\boxed{f_X(x) = \lambda e^{-\lambda x}, \quad x \geq 0}$$
> Per $x < 0$: $f_X(x) = 0$.

**Parametro $\lambda$:** il **tasso di arrivo** o **intensità** del processo di Poisson. Un valore $\lambda$ grande significa eventi frequenti (tempo di attesa breve); un valore piccolo significa eventi rari (tempo di attesa lungo).

### Proprietà principali

**Media e Varianza:**

$$E[X] = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}$$

Quindi la deviazione standard è $\sigma_X = 1/\lambda$, uguale alla media (caso di alta variabilità relativa).

**Funzione di distribuzione cumulativa (CDF):**

$$F_X(x) = P(X \leq x) = 1 - e^{-\lambda x}, \quad x \geq 0$$

**Proprietà di assenza di memoria:**

$$P(X > s + t | X > s) = P(X > t)$$

Questa proprietà dice che se un evento non è stato osservato in tempo $s$, la distribuzione del "tempo aggiuntivo" rimane esponenziale con lo stesso parametro. Questa è la **proprietà caratteristica** dell'esponenziale tra tutte le distribuzioni continue.

> [!example] Tempo di vita di una componente elettronica
> Se I guasti seguono un processo con tasso di arrivo $\lambda = 0.01$ guasti/ora, allora il tempo medio di vita è $1/0.01 = 100$ ore. Il tempo rimanente di vita di una componente che ha già funzionato per 50 ore ha lo stesso distribution (assenza di memoria).

### Relazione con la Poissoniana

Se il numero di eventi in un intervallo di tempo $[0, t]$ segue una distribuzione di Poisson con media $\lambda t$, il tempo $X$ tra due eventi successivi segue una distribuzione esponenziale di parametro $\lambda$.

---

## Teorema di Continuità di Lévy e Convergenza in Distribuzione (Introdotto dopo)

### Funzione generatrice dei momenti (MGF)

La **Funzione Generatrice dei Momenti (MGF)** è uno strumento potente per lo studio della convergenza di distribuzioni:

> [!abstract] Definizione: MGF
> Sia $X$ una variabile aleatoria. La sua **funzione generatrice dei momenti** è:
> $$M_X(t) = E[e^{tX}], \quad t \in \mathbb{R}$$
> (quando l'aspettazione esiste in un intorno di $t=0$).

**Proprietà:**
- I **momenti** di $X$ si ricavano dalle derivate di $M_X(t)$: $E[X^k] = \frac{d^k M_X}{dt^k}(0)$.
- Se la MGF esiste e è unica, determina completamente la distribuzione di $X$.

### Teorema di Continuità di Lévy

> [!abstract] Teorema di Continuità di Lévy
> Siano $X, X_1, X_2, \ldots$ variabili aleatorie. Allora:
> $$X_n \xrightarrow{d} X \quad \text{(convergenza in distribuzione)}$$
> se e solo se:
> $$M_{X_n}(t) \to M_X(t) \quad \text{per ogni } t$$

**Interpretazione:** è più facile controllare la convergenza delle MGF che confrontare le funzioni di distribuzione direttamente.

### Applicazione al CLT

Per dimostrare rigorosamente il **Teorema del Limite Centrale**, si calcola la MGF della somma standardizzata e si mostra che converge alla MGF della gaussiana standard $\mathcal{N}(0,1)$, che è $M(t) = e^{t^2/2}$.

> [!info] Criterio di convergenza in pratica
> Per verificare se una sequenza di distribuzioni converge a quella di una variabile aleatoria nota (es. gaussiana), calcolare le MGF e controllare se la convergenza vale punto per punto.

---


---

> [!abstract] Punti chiave della lezione
> - Il teorema della media condizionale permette di calcolare la media totale condizionando su una variabile ausiliaria, scomponendo problemi complessi in sottoproblemi più semplici.
> - La distribuzione di Poisson è chiusa rispetto al subcampionamento bernoulliano: $N \sim \text{Poisson}(\lambda)$ e $M|N \sim \text{Bin}(N,p)$ implicano $M \sim \text{Poisson}(\lambda p)$.
> - La covarianza misura la co-variazione lineare tra due variabili; il coefficiente di correlazione la normalizza in $[-1,1]$.
> - Indipendenza $\Rightarrow$ incorrelazione, ma non viceversa (eccetto nel caso gaussiano).
> - La matrice di covarianza è semidefinita positiva e fondamentale in statistica multivariata e machine learning.
> - Per variabili continue, la probabilità di un singolo punto è 0; si lavora con la densità di probabilità e con probabilità di intervalli.

---

#MSP #covarianza #correlazione #matrice-covarianza #media-condizionale #variabili-continue #densita-probabilita #CLT #teorema-limite-centrale #distribuzione-esponenziale #MGF

---