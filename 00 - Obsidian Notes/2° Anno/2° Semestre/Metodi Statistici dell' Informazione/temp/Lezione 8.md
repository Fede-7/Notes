---
date: 2026-04-09
corso: Metodi Statistici dell'Informazione
docente: N/D
lezione: "CDF, distribuzioni continue notevoli e PDF condizionata"
tags: [MSI, CDF, PDF, distribuzione-uniforme, distribuzione-esponenziale, laplace, pdf-condizionata, media-continua]
---
>[!question] Argomenti trattati
>- Definizione formale di CDF (Cumulative Distribution Function) e sue proprietà
>- Relazione fondamentale tra CDF e PDF
>- CDF di una variabile discreta (esempio bernoulliano)
>- Variabile uniforme: PDF, CDF e valore atteso
>- Derivazione del valore atteso per variabili continue tramite quantizzazione
>- Variabile esponenziale: PDF, CDF e valore atteso
>- Variabile di Laplace (doppia esponenziale): PDF e CDF
>- Introduzione alla PDF e CDF condizionate

---

## 1. Cumulative Distribution Function (CDF)

### Definizione

> [!abstract] Definizione: CDF
> La **funzione di distribuzione cumulativa** di una variabile aleatoria $X$ è la funzione $F_X : \mathbb{R} \to [0,1]$ definita da:
> $$F_X(x) = P(X \leq x) \quad \forall x \in \mathbb{R}$$

La CDF è definita per **qualsiasi** variabile aleatoria, discreta o continua.

### Proprietà della CDF

**1. Valori agli estremi:**

$$F_X(-\infty) = 0 \qquad F_X(+\infty) = 1$$

$F_X(-\infty) = P(X \leq -\infty) = 0$ perché nessuna variabile può assumere un valore inferiore a $-\infty$. Analogamente $F_X(+\infty) = 1$.

**2. Monotonia crescente:** se $x_2 > x_1$ allora $F_X(x_2) \geq F_X(x_1)$.

*Dimostrazione:* $P(X \leq x_2) = P(X \leq x_1) + P(x_1 < X \leq x_2)$. Poiché la seconda probabilità è $\geq 0$, segue che $F_X(x_2) \geq F_X(x_1)$.

**3. Continuità a destra:** il valore in un punto è uguale al suo limite destro. *(Proprietà tecnica che non viene dimostrata.)*

### Relazione tra CDF e PDF

Per variabili continue, la CDF è l'integrale della PDF:

$$F_X(x) = \int_{-\infty}^{x} f_X(t)\, dt$$

Derivando si ottiene:

$$f_X(x) = \frac{d}{dx} F_X(x)$$

La CDF è monotona crescente, quindi la sua derivata è sempre $\geq 0$, il che conferma che la PDF è non negativa. Conoscere la CDF equivale a conoscere la PDF e viceversa: si può passare liberamente da una all'altra.

> [!tip] Strategia pratica
> Quando si lavora con variabili continue, a volte è più comodo definire la CDF (un'operazione di probabilità, quindi sempre ben definita) e poi derivarla per ottenere la PDF. Questo evita di ragionare direttamente sulla "densità" come concetto astratto.

---

## 2. CDF di una variabile discreta: esempio bernoulliano

La CDF si applica anche alle variabili discrete, anche se si usa raramente rispetto alla PMF.

> [!example] CDF di una variabile di Bernoulli
> Sia $X \sim \text{Bernoulli}(p)$, quindi $P(X=0) = 1-p$ e $P(X=1) = p$.
>
> $$F_X(x) = \begin{cases} 0 & x < 0 \\ 1-p & 0 \leq x < 1 \\ 1 & x \geq 1 \end{cases}$$
>
> Il grafico è una **funzione a scalini**: parte da 0, fa un salto di ampiezza $1-p$ in $x=0$, rimane costante, poi fa un salto di ampiezza $p$ in $x=1$ e arriva a 1. L'ampiezza dei salti corrisponde esattamente ai valori della PMF. Questo è il motivo per cui si preferisce usare la PMF per le variabili discrete.

---

## 3. Variabile aleatoria uniforme

> [!abstract] Definizione: Variabile uniforme $U(a,b)$
> La variabile $X$ è **uniforme** nell'intervallo $[a, b]$ se la sua PDF è:
> $$f_X(x) = \begin{cases} \frac{1}{b-a} & a \leq x \leq b \\ 0 & \text{altrove} \end{cases}$$

**Verifica che sia una PDF valida:** l'integrale è l'area di un rettangolo di base $b-a$ e altezza $\frac{1}{b-a}$, che vale 1. ✓

**CDF:**

$$F_X(x) = \begin{cases} 0 & x < a \\ \dfrac{x-a}{b-a} & a \leq x \leq b \\ 1 & x > b \end{cases}$$

La CDF ha un andamento a **rampa** lineare tra $a$ e $b$ con pendenza $\frac{1}{b-a}$, che corrisponde al valore della PDF (derivata della CDF).

**Valore atteso:**

$$E[X] = \int_a^b x \cdot \frac{1}{b-a}\, dx = \frac{1}{b-a} \cdot \frac{b^2 - a^2}{2} = \frac{a+b}{2}$$

Il valore atteso è il punto medio dell'intervallo, come intuitivamente atteso.

---

## 4. Come si definisce il valore atteso nel caso continuo

### Derivazione via quantizzazione

Per comprendere perché il valore atteso di una variabile continua è $\int x f_X(x)\, dx$, si parte dalla quantizzazione. Si divide il supporto di $X$ in sottointervalli di ampiezza $\delta$ e si approssima $X$ con la variabile discreta $X_\delta$ che assume il valore centrale $x_i$ dell'$i$-esimo intervallo.

$X_\delta$ è discreta, quindi:
$$E[X_\delta] = \sum_i x_i \cdot P(X_\delta = x_i) = \sum_i x_i \cdot f_X(c_i) \cdot \delta$$

dove $c_i$ è un punto del sottointervallo $i$ per il teorema del valor medio. Questa è per definizione la somma di Riemann di $\int x\, f_X(x)\, dx$. Quando $\delta \to 0$, $X_\delta \to X$ e:

$$E[X] = \int_{-\infty}^{+\infty} x\, f_X(x)\, dx$$

> [!info] Implicazione pratica: la quantizzazione vettoriale
> Shannon (1948) dimostrò che per digitalizzare dati analogici in modo ottimo non conviene quantizzare campione per campione, ma blocchi di dati grandi tutti insieme (**quantizzazione vettoriale**). Un quantizzatore su $\mathbb{R}^n$ è asintoticamente molto più efficiente di $n$ quantizzatori scalari indipendenti. Questo è il fondamento della codifica a blocchi usata in tutti i sistemi di compressione moderni.

---

## 5. Variabile esponenziale

> [!abstract] Definizione: Variabile esponenziale $\text{Exp}(\lambda)$
> La variabile $X$ è **esponenziale** di parametro $\lambda > 0$ se:
> $$f_X(x) = \lambda e^{-\lambda x} \cdot U(x), \quad x \in [0, +\infty)$$
> dove $U(x)$ è la funzione gradino unitario (vale 1 per $x \geq 0$, 0 altrove).

**CDF:**

$$F_X(x) = \begin{cases} 0 & x < 0 \\ 1 - e^{-\lambda x} & x \geq 0 \end{cases}$$

*Derivazione:* $F_X(x) = \int_0^x \lambda e^{-\lambda t}\, dt = [-e^{-\lambda t}]_0^x = 1 - e^{-\lambda x}$.

**Valore atteso:**

$$E[X] = \int_0^{+\infty} x\, \lambda e^{-\lambda x}\, dx = \lambda \cdot \frac{1}{\lambda^2} \cdot 1! = \frac{1}{\lambda}$$

usando l'integrale notevole $\int_0^\infty x^m e^{-ax}\, dx = \frac{(m-1)!}{a^m}$ (funzione Gamma di Eulero).

**Effetto di $\lambda$:** più $\lambda$ è grande, più la PDF decade rapidamente verso zero (la media $1/\lambda$ è piccola). Per la normalizzazione, la PDF parte da un valore più alto nell'origine se $\lambda$ è grande.

> [!warning] La PDF non è una probabilità
> $f_X(0) = \lambda$, che può essere maggiore di 1 (per $\lambda > 1$). La PDF non è una probabilità; è la *densità* di probabilità. La probabilità si calcola come area sotto la curva su un intervallo.

---

## 6. Variabile di Laplace (doppia esponenziale)

> [!abstract] Definizione: Variabile di Laplace $\text{Laplace}(\lambda)$
> La variabile $X$ è **laplaciana** di parametro $\lambda > 0$ se:
> $$f_X(x) = \frac{\lambda}{2} e^{-\lambda|x|}, \quad x \in \mathbb{R}$$

La PDF è una funzione **pari** ($f_X(x) = f_X(-x)$) con forma a "vela": due esponenziali specchiate rispetto all'origine.

**CDF** — per sfruttare la parità si divide il calcolo in due regioni:

$$F_X(x) = \begin{cases} \dfrac{1}{2} e^{\lambda x} & x \leq 0 \\[6pt] 1 - \dfrac{1}{2} e^{-\lambda x} & x > 0 \end{cases}$$

L'andamento è di tipo **sigmoidale** (a S rovesciata): parte da 0 a $-\infty$, ha un punto di flesso in $x=0$ dove vale $1/2$, e sale asintoticamente a 1. Tutte le CDF di variabili con supporto tutto $\mathbb{R}$ hanno questo andamento sigmoidale.

> [!tip] Tecnica per le funzioni pari
> Per integrare funzioni pari su $(-\infty, x_0)$ con $x_0 \leq 0$: l'intervallo è tutto negativo, quindi $|t| = -t$ e si applica la formula dell'esponenziale con segno positivo. Per $x_0 > 0$: si spezza l'integrale in $(-\infty, 0)$ e $(0, x_0)$.

---

## 7. Valore atteso della variabile uniforme (ripasso con formula integrale)

$$E[X] = \int_a^b x \cdot \frac{1}{b-a}\, dx = \frac{1}{b-a} \cdot \left[\frac{x^2}{2}\right]_a^b = \frac{b^2 - a^2}{2(b-a)} = \frac{(b-a)(b+a)}{2(b-a)} = \frac{a+b}{2}$$

---

## 8. PDF condizionata: introduzione

Analogamente al caso discreto, si può condizionare una PDF a un evento $A$.

> [!abstract] Definizione: CDF e PDF condizionate
> Data una variabile continua $X$ e un evento $A$, la **CDF condizionata** è:
> $$F_{X|A}(x) = P(X \leq x \mid A) = \frac{P(X \leq x, A)}{P(A)}$$
> La **PDF condizionata** si ottiene derivando:
> $$f_{X|A}(x) = \frac{d}{dx} F_{X|A}(x)$$

La convenienza di lavorare con la CDF è che $P(X \leq x \mid A)$ è sempre ben definita tramite la definizione di probabilità condizionata, senza dover ragionare direttamente sulla densità.

> [!example] PDF condizionata di una Laplace
> Sia $X \sim \text{Laplace}(\lambda)$ e $A = \{-1 \leq X \leq 2\}$. Si vuole $f_{X|A}(x)$.
>
> $P(A) = F_X(2) - F_X(-1) = \left(1 - \frac{1}{2}e^{-2\lambda}\right) - \frac{1}{2}e^{-\lambda}$.
>
> Per $x < -1$: $P(X \leq x, A) = 0$, quindi $F_{X|A}(x) = 0$.
> Per $-1 \leq x \leq 2$: $P(X \leq x, A) = P(-1 \leq X \leq x) = F_X(x) - F_X(-1)$, quindi $F_{X|A}(x) = \frac{F_X(x) - F_X(-1)}{P(A)}$.
> Per $x > 2$: $F_{X|A}(x) = 1$.
>
> La PDF condizionata si ottiene derivando rispetto a $x$.

**Motivazione pratica:** in un sistema radar si possono pre-filtrare i ritorni considerando solo quelli la cui ampiezza supera una soglia. Si lavora così con una statistica condizionata, che deve essere tenuta in conto nella progettazione dell'elaborazione successiva.

---

> [!abstract] Punti chiave della lezione
> - La CDF $F_X(x) = P(X \leq x)$ è definita per qualsiasi variabile aleatoria; è monotona crescente, vale 0 a $-\infty$ e 1 a $+\infty$.
> - PDF e CDF sono equivalenti: $f_X(x) = F_X'(x)$ e $F_X(x) = \int_{-\infty}^x f_X(t)\, dt$.
> - Il valore atteso continuo $E[X] = \int x f_X(x)\, dx$ si giustifica come limite di medie di variabili quantizzate.
> - Uniforme $U(a,b)$: media $\frac{a+b}{2}$, CDF lineare. Esponenziale $\text{Exp}(\lambda)$: media $\frac{1}{\lambda}$, CDF $1-e^{-\lambda x}$. Laplace $(\lambda)$: PDF simmetrica, CDF sigmoidale.
> - La PDF condizionata si definisce tramite la CDF condizionata, senza problemi di definizione.

---
#MSI #CDF #PDF #distribuzione-uniforme #distribuzione-esponenziale #laplace #media-continua #pdf-condizionata

___
