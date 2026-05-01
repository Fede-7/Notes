---
date: 2026-04-27
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 12
tags: [MSI, markov, chebyshev, uniforme, laplace, distribuzione-continua, ineguaglianza-probabilistica]
---

# 10. Ineguaglianze di Probabilità e Distribuzioni Continue Notevoli

## 10.1 Ineguaglianza di Markov

Consideriamo una variabile aleatoria $X$ a valori non negativi con media finita $\mu_X = E[X]$. L'ineguaglianza di Markov fornisce un limite superiore alla probabilità che $X$ ecceda una soglia $\delta > 0$:

$$P(X \geq \delta) \leq \frac{E[X]}{\delta}$$

### Dimostrazione

Per ogni $\delta > 0$, definiamo l'evento $A = \{X \geq \delta\}$. Allora:

$$E[X] = \int_0^\infty x f_X(x) \, dx \geq \int_\delta^\infty x f_X(x) \, dx \geq \delta \int_\delta^\infty f_X(x) \, dx = \delta \cdot P(X \geq \delta)$$

Dividendo per $\delta$ si ottiene il risultato. La dimostrazione nel caso discreto è analoga, sostituendo l'integrale con una sommatoria.

### Osservazione sulla generalizzazione

L'ineguaglianza di Markov si generalizza a qualsiasi funzione monotona crescente $g : \mathbb{R}_{\geq 0} \to \mathbb{R}_{\geq 0}$:

$$P(X \geq \delta) = P(g(X) \geq g(\delta)) \leq \frac{E[g(X)]}{g(\delta)}$$

Questo è il motivo per cui l'ineguaglianza di Chebyshev, che considereremo di seguito, rappresenta una specializzazione della formula di Markov al caso $g(x) = (x - \mu_X)^2$.

## 10.2 Ineguaglianza di Chebyshev

Sia $X$ una variabile aleatoria con media $\mu_X$ e varianza $\sigma_X^2$ finita. L'ineguaglianza di Chebyshev limita la probabilità che $X$ devia dalla sua media di più di $k$ volte la deviazione standard:

$$P(|X - \mu_X| \geq k\sigma_X) \leq \frac{1}{k^2}$$

equivalentemente,

$$P(|X - \mu_X| \geq \delta) \leq \frac{\sigma_X^2}{\delta^2}$$

### Derivazione

Applichiamo l'ineguaglianza di Markov alla variabile aleatoria $Y = (X - \mu_X)^2$, che è non negativa:

$$P(Y \geq \delta^2) \leq \frac{E[Y]}{\delta^2} = \frac{\text{Var}(X)}{\delta^2}$$

Poiché $Y \geq \delta^2$ è equivalente a $|X - \mu_X| \geq \delta$, si ottiene il risultato.

> [!important] Universalità dell'ineguaglianza di Chebyshev
> A differenza di ineguaglianze specifiche per distribuzioni particolari (come la gaussiana), l'ineguaglianza di Chebyshev vale per qualsiasi distribuzione con varianza finita. Il prezzo è che il limite è spesso molto conservativo.

### Limiti practici

Nel caso continuo la dimostrazione è identica a quella nel caso discreto: basta sostituire la sommatoria con l'integrale. Per questo motivo, la coppia $(\mu_X, \sigma_X)$ fornisce una caratterizzazione globale di qualsiasi variabile aleatoria, discreta o continua, indipendentemente dalla distribuzione specifica.

## 10.3 Distribuzione Uniforme Continua

La distribuzione uniforme su un intervallo $[a, b]$ ha densità costante:

$$f_X(x) = \begin{cases} \dfrac{1}{b-a} & a \leq x \leq b \\ 0 & \text{altrove} \end{cases}$$

**Media:** $E[X] = \frac{a+b}{2}$ (il punto medio dell'intervallo).

**Varianza:** $\text{Var}(X) = \frac{(b-a)^2}{12}$.

### Applicazione: Quantizzazione uniforme

Nella rappresentazione numerica di segnali analogici, un quantizzatore uniforme divide un intervallo $[a, b]$ in $M = 2^R$ livelli di ampiezza $\Delta = \frac{b-a}{M}$. L'errore di quantizzazione (differenza tra il valore continuo e il suo rappresentante quantizzato) può essere modellato come uniformemente distribuito su $[-\frac{\Delta}{2}, \frac{\Delta}{2}]$.

L'errore quadratico medio (distorsione) risulta:

$$\text{Distorsione} = \text{Var}(\text{errore}) = \frac{\Delta^2}{12}$$

Questo risultato è fondamentale nella teoria della codifica. Se le statistiche dei dati non sono uniformi, un quantizzatore non uniforme (quantizzazione adattativa) può ridurre significativamente la distorsione. Tecniche moderne di compressione utilizzano quantizzatori vettoriali, che operano su blocchi di dati invece che su singoli campioni, ottenendo prestazioni teoricamente ottimali.

> [!tip] Osservazione su quantizzazione uniforme vs. adattativa
> La quantizzazione uniforme è appropriata solo quando i dati seguono una distribuzione uniforme, una situazione rara nella pratica. Se i dati hanno una distribuzione nota (ad esempio gaussiana), è ottimo concentrare i livelli di quantizzazione dove la densità di probabilità è maggiore. Se la distribuzione è sconosciuta, un algoritmo di apprendimento statistico (ad es. k-means clustering) può stimare i livelli di quantizzazione adattativi in modo automatico durante l'addestramento.

## 10.4 Distribuzione di Laplace (Doppia Esponenziale)

La distribuzione di Laplace con parametro $\lambda > 0$ ha densità:

$$f_X(x) = \frac{\lambda}{2} e^{-\lambda|x|}$$

**CDF:**

$$F_X(x) = \begin{cases} \dfrac{1}{2} e^{\lambda x} & x < 0 \\ 1 - \dfrac{1}{2} e^{-\lambda x} & x \geq 0 \end{cases}$$

**Media:** $E[X] = 0$ (per simmetria).

**Varianza:** $\text{Var}(X) = \frac{2}{\lambda^2}$.

La distribuzione di Laplace modella fenomeni con code più pesanti dell'esponenziale (asimmetrico), come il rumore impulsivo (ad es. atmosferico) nei sistemi di telecomunicazione. In contrasto, la distribuzione gaussiana (che vedremo in seguito) è più lieve nelle code ed è appropriata per il rumore termico.

### Distribuzioni con varianza infinita

La distribuzione di Cauchy, definita da $f_X(x) = \frac{1}{\pi(1 + x^2)}$, è un esempio notevole di variabile aleatoria continua senza varianza finita. Le sue code decadono così lentamente che $E[X^2] = \infty$. Fenomeni fisici modellati da Cauchy (come il rumore atmosferico da fulmine) hanno potenza infinita e non ammettono caratterizzazione tramite i momenti ordinari.

## 10.5 PDF Condizionata

Data una variabile aleatoria $X$ con PDF $f_X(x)$ e un evento $A$ con $P(A) > 0$, la **PDF condizionata** è:

$$f_{X|A}(x) = \begin{cases} \dfrac{f_X(x)}{P(A)} & x \in A \\ 0 & x \notin A \end{cases}$$

In altri termini, la PDF condizionata è proporzionale alla PDF originale, confinata al supporto di $A$ e riscalata affinché l'integrale faccia 1.

### Esempio: Distribuzione triangolare condizionata

Consideriamo una variabile aleatoria $X$ con supporto $[-3, -1] \cup [1, 3]$, con densità costante $\frac{1}{4}$ su $[-3, -1]$ e triangolare su $[1, 3]$. Calcoliamo la PDF condizionata all'evento $A = \{X \leq 0\}$.

$$P(A) = P(X \in [-3, -1]) = \frac{1}{4} \cdot 2 = \frac{1}{2}$$

Per $x \in [-3, -1]$:

$$f_{X|A}(x) = \frac{1/4}{1/2} = \frac{1}{2}$$

La PDF condizionata è uniforme su $[-3, -1]$ con densità doppia rispetto all'originale, poiché le osservazioni negative rappresentano la metà della probabilità totale. Per $x > 0$, invece, $f_{X|A}(x) = 0$.

La media condizionata è:

$$E[X | A] = \int_{-3}^{-1} x \cdot \frac{1}{2} \, dx = \frac{1}{2} \cdot \frac{x^2}{2} \Big|_{-3}^{-1} = \frac{1}{2} \cdot \frac{9 - 1}{2} = 2$$

Per simmetria, $E[X | X > 0] = 2$ e $E[X] = E[X | A] P(A) + E[X | A^c] P(A^c) = (-2) \cdot \frac{1}{2} + 2 \cdot \frac{1}{2} = 0$.

---

#MSI #ineguaglianza-markov #ineguaglianza-chebyshev #distribuzione-uniforme #distribuzione-laplace #quantizzazione #PDF-condizionata
