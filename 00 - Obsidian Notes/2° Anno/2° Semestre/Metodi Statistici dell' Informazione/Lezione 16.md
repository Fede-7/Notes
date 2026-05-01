---
date: 2026-04-27
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 16
tags: [MSI, vettore-aleatorio, matrice-covarianza, correlazione, convoluzione, teorema-limite-centrale, sistemi-lineari]
---

# 14. Vettori Aleatori e Proprietà Multidimensionali

## 14.1 Vettori Aleatori Bidimensionali

Una coppia di variabili aleatorie può essere rappresentata come un **vettore aleatorio** $\mathbf{X} = (X_1, X_2)^T$. Il vettore delle medie è:

$$\boldsymbol{\mu} = E[\mathbf{X}] = \begin{pmatrix} E[X_1] \\ E[X_2] \end{pmatrix} = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}$$

La **matrice di covarianza** è una matrice $2 \times 2$ che racchiude tutte le informazioni sulla variabilità e la co-variabilità:

$$K = \text{Cov}(\mathbf{X}) = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T] = \begin{pmatrix} \sigma_1^2 & \text{Cov}(X_1, X_2) \\ \text{Cov}(X_1, X_2) & \sigma_2^2 \end{pmatrix}$$

dove $\text{Cov}(X_1, X_2) = E[(X_1 - \mu_1)(X_2 - \mu_2)]$ è la covarianza fra le due variabili, e $\sigma_i^2 = \text{Var}(X_i)$.

## 14.2 Coefficient di Correlazione

La **correlazione normalizzata** fra $X_1$ e $X_2$ è:

$$\rho_{12} = \frac{\text{Cov}(X_1, X_2)}{\sigma_1 \sigma_2}$$

Proprietà:
- $|\rho_{12}| \leq 1$ per la disuguaglianza di Cauchy-Schwarz.
- $\rho_{12} = 1$ se e solo se $X_2 = a X_1 + b$ con $a > 0$ (relazione lineare diretta).
- $\rho_{12} = -1$ se e solo se $X_2 = a X_1 + b$ con $a < 0$ (relazione lineare inversa).
- $\rho_{12} = 0$ se le variabili sono incorrelate (ma non necessariamente indipendenti).

> [!important] Correlazione vs. Indipendenza
> **L'indipendenza implica correlazione nulla**, ma il viceversa non è vero. Due variabili possono avere $\rho = 0$ (zero covarianza) pur essendo fortemente dipendenti tramite una relazione non lineare. L'unica eccezione è il caso gaussiano, dove incorrelazione equivale a indipendenza.

## 14.3 Generalizzazione a Vettori n-dimensionali

Per un vettore aleatorio $\mathbf{X} = (X_1, \ldots, X_n)^T$, la matrice di covarianza è $n \times n$:

$$K_{ij} = \text{Cov}(X_i, X_j)$$

Proprietà della matrice di covarianza:
- **Simmetria**: $K = K^T$ (poiché $\text{Cov}(X_i, X_j) = \text{Cov}(X_j, X_i)$).
- **Semidefinitezza positiva**: per ogni vettore $\mathbf{a}$, si ha $\mathbf{a}^T K \mathbf{a} \geq 0$. Questo garantisce che la matrice sia sempre invertibile (se non singolare).
- **Diagonale**: i termini sulla diagonale sono le varianze $K_{ii} = \sigma_i^2 \geq 0$.

La matrice di covarianza è fondamentale in **analisi dei componenti principali (PCA)**, **filtraggio ottimale (Kalman filter)**, e **stima MMSE** (Minimum Mean Square Error).

## 14.4 Operazione di Convoluzione

### Definizione

Date due funzioni integrabili $f$ e $g$, il **prodotto di convoluzione** è:

$$(f * g)(t) = \int_{-\infty}^{+\infty} f(\tau) \cdot g(t - \tau) \, d\tau = \int_{-\infty}^{+\infty} f(t - \tau) \cdot g(\tau) \, d\tau$$

La convoluzione è **commutativa**, **associativa** e **distributiva** rispetto alla somma.

### Motivazione probabilistica

Se $X$ e $Y$ sono variabili aleatorie continue indipendenti con densità $f_X$ e $f_Y$, la densità della somma $Z = X + Y$ è la convoluzione:

$$f_Z(z) = (f_X * f_Y)(z) = \int_{-\infty}^{+\infty} f_X(x) \cdot f_Y(z - x) \, dx$$

La convoluzione cattura come la "combinazione" di due fenomeni aleatori indipendenti si riflette nella distribuzione della loro somma.

### Applicazioni

- **Sistemi lineari tempo-invarianti (LTI)**: la relazione ingresso-uscita di un sistema LTI è descritta dalla convoluzione dell'ingresso con la risposta all'impulso del sistema.
- **Processamento di segnali**: filtraggio di immagini, audio e dati è implementato via convoluzione.
- **Reti neurali convoluzionali (CNN)**: gli strati convoluzionali eseguono prodotti di convoluzione discreti.

## 14.5 Trasformata di Laplace e Funzioni di Trasferimento

La **trasformata di Laplace** di una funzione $f(t)$ è:

$$F(s) = \mathcal{L}\{f\}(s) = \int_0^\infty f(t) e^{-st} \, dt$$

Proprietà fondamentale: la convoluzione nel dominio del tempo diventa **moltiplicazione** nel dominio di Laplace:

$$\mathcal{L}\{f * g\} = \mathcal{L}\{f\} \cdot \mathcal{L}\{g\}$$

Questa proprietà è cruciale per risolvere equazioni differenziali lineari a coefficienti costanti, trasformandole in equazioni algebriche nel dominio di Laplace.

## 14.6 Teorema Centrale del Limite

> [!abstract] Teorema Centrale del Limite (TCL)
> Siano $X_1, X_2, \ldots, X_n$ variabili aleatorie **indipendenti e identicamente distribuite** (i.i.d.) con media finita $\mu$ e varianza finita $\sigma^2$. Allora, per $n \to \infty$, la somma (riscalata e centrata)
> $$Z_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}}$$
> converge in distribuzione a una **gaussiana standard** $\mathcal{N}(0, 1)$.

### Significato pratico

Il TCL spiega perché la distribuzione gaussiana è ubiquitaria in natura: ogniqualvolta un fenomeno è la sovrapposizione di molti fenomeni elementari indipendenti (ad es., rumore termico come somma di migliaia di eventi di scattering), il risultato è approssimativamente gaussiano, indipendentemente dalle distribuzioni individuali dei componenti.

Applicazioni:
- **Teoria degli errori**: errori di misura frequentist sono generalmente gaussiani.
- **Control di qualità**: il TCL permette di stimare distribuzioni di media campionaria senza conoscere la distribuzione esatta dei dati.
- **Propagazione dell'incertezza**: quando si combinano misure indipendenti, l'incertezza risultante tende alla gaussiana.

### Velocità di convergenza

La convergenza è più rapida se le distribuzioni individuali sono già simmetriche. Se le $X_i$ hanno distribuzioni "pesanti" (con code molto pronunciate), servono più termini per la convergenza.

## 14.7 Cenno a Estensioni

### Variabili continue multivariate

L'intero framework (CDF congiunta, PDF congiunta, marginalizzazione, condizionamento, covarianza) si estende a $n$ variabili qualsiasi. Gli integrali diventano $n$-pli, ma la logica rimane identica.

### Convergenze e limiti

Oltre al TCL, esistono teoremi di limite più generali:
- **Legge dei grandi numeri**: la media campionaria converge alla media teorica quando $n \to \infty$.
- **Teorema di Slutsky**: regole per combinare limiti di sequenze di variabili aleatorie.
- **Convergenza in distribuzione, probabilità, e quasi-certamente**: diversi modi di formalizzare cosa significhi "convergere" per variabili aleatorie.

---

#MSI #vettore-aleatorio #matrice-covarianza #correlazione #convoluzione #teorema-limite-centrale #sistemi-lineari #trasformata-laplace
