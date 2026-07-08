---
date: 2026-05-05
corso: Metodi Statistici dell'Informazione
docente: Marco Lops
lezione: 19
tags: [MSI, stima-bayesiana, mmse, map, beta-gamma, polarizzazione, consistenza]
---

# 🧠 Lezione 19 — Stimatore MAP, Esempio Completo (Sorgente Binaria) e Proprietà degli Stimatori

---

## 1. Stimatore MAP (Maximum A Posteriori) per Variabili Continue

> [!abstract] Essenza
> Nello stimare un parametro continuo $\theta$, non possiamo definire la probabilità di commettere un errore esatto $P(\hat{\theta} \neq \theta)$, poiché essa è sempre pari a 1.
> Possiamo invece definire una funzione di costo uniforme "hit-or-miss" su una tolleranza $\epsilon \to 0$:
> $$C(\theta - \hat{\theta}) = \begin{cases} 0 & |\theta - \hat{\theta}| \leq \epsilon/2 \\ 1 & |\theta - \hat{\theta}| > \epsilon/2 \end{cases}$$

Il rischio Bayesiano associato è la probabilità che lo stimatore disti da $\theta$ più di $\epsilon/2$:
$$R_B = P\left( |\theta - \hat{\theta}(\mathbf{X}^n)| > \frac{\epsilon}{2} \right) = 1 - \int_{\hat{\theta}-\epsilon/2}^{\hat{\theta}+\epsilon/2} f(\theta | \mathbf{x}^n) d\theta$$
Per massimizzare l'integrale a destra quando la tolleranza $\epsilon \to 0$, dobbiamo posizionare l'intervallo attorno al punto di massimo (la moda) della densità a posteriori:
$$\hat{\theta}_{MAP}(\mathbf{x}^n) = \arg\max_{\theta} f(\theta | \mathbf{x}^n)$$

Applicando il Teorema di Bayes e ignorando il denominatore $f(\mathbf{x}^n)$ (che non dipende da $\theta$):
$$\hat{\theta}_{MAP}(\mathbf{x}^n) = \arg\max_{\theta} \left[ f(\mathbf{x}^n | \theta) f_\theta(\theta) \right]$$
Spesso si preferisce massimizzare la funzione di log-verosimiglianza a posteriori (monotona):
$$\hat{\theta}_{MAP}(\mathbf{x}^n) = \arg\max_{\theta} \left[ \ln f(\mathbf{x}^n | \theta) + \ln f_\theta(\theta) \right]$$

---

## 2. Caso di Studio: Stima del Parametro di una Sorgente Binaria I.I.D.

### Setup del Problema
- **Osservazioni**: stringa binaria $\mathbf{x}^n$ con peso di Hamming $w_H$ (numero di $1$ su $n$ bit).
- **Parametro ignoto**: $\theta \in [0, 1]$, la probabilità che la sorgente generi $1$.
- **Prior**: distribuzione uniforme sul dominio del parametro:
  $$f_\theta(\theta) = 1 \cdot u(\theta) u(1-\theta)$$
- **Verosimiglianza (Bernoulli I.I.D.)**:
  $$P(\mathbf{x}^n | \theta) = \theta^{w_H} (1 - \theta)^{n - w_H}$$

### 2.1 Calcolo della Densità A Posteriori
La densità condizionata a posteriori è:
$$f(\theta | \mathbf{x}^n) = \frac{P(\mathbf{x}^n | \theta) f_\theta(\theta)}{\int_0^1 P(\mathbf{x}^n | \theta) f_\theta(\theta) d\theta} = \frac{\theta^{w_H} (1 - \theta)^{n - w_H}}{\int_0^1 \theta^{w_H} (1 - \theta)^{n - w_H} d\theta}$$

Per risolvere l'integrale a denominatore, utilizziamo la **funzione speciale Beta**:
$$B(a, b) = \int_0^1 t^{a-1} (1-t)^{b-1} dt = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$$
Nel nostro caso poniamo $a-1 = w_H \implies a = w_H+1$, e $b-1 = n - w_H \implies b = n - w_H + 1$.
Poiché gli argomenti sono interi, possiamo esprimere la funzione Gamma tramite i fattoriali ($\Gamma(k) = (k-1)!$):
$$\int_0^1 \theta^{w_H} (1 - \theta)^{n - w_H} d\theta = \frac{w_H! (n - w_H)!}{(n+1)!} = \frac{1}{(n+1)\binom{n}{w_H}}$$
La PDF a posteriori risulta quindi essere una densità Beta di parametri $(w_H+1, n-w_H+1)$:
$$f(\theta | \mathbf{x}^n) = (n+1)\binom{n}{w_H} \theta^{w_H} (1 - \theta)^{n - w_H} \quad (\forall \theta \in [0, 1])$$

---

### 2.2 Derivazione dello Stimatore MMSE
Lo stimatore MMSE è la media condizionata a posteriori:
$$\hat{\theta}_{MMSE}(\mathbf{x}^n) = E[\theta | \mathbf{x}^n] = \int_0^1 \theta f(\theta | \mathbf{x}^n) d\theta$$
$$E[\theta | \mathbf{x}^n] = (n+1)\binom{n}{w_H} \int_0^1 \theta^{w_H+1} (1 - \theta)^{n - w_H} d\theta$$
Risolvendo il nuovo integrale Beta con parametri $a = w_H+2$ e $b = n-w_H+1$:
$$\int_0^1 \theta^{w_H+1} (1 - \theta)^{n - w_H} d\theta = \frac{(w_H+1)! (n-w_H)!}{(n+2)!}$$
Sostituendo e semplificando i fattoriali:
$$\hat{\theta}_{MMSE}(\mathbf{x}^n) = \frac{(n+1)!}{w_H! (n-w_H)!} \cdot \frac{(w_H+1)! (n-w_H)!}{(n+2)!} = \frac{w_H + 1}{n + 2}$$

> [!info] Regola di Successione di Laplace
> Lo stimatore MMSE aggiunge un'operazione di regolarizzazione (o "smoothing") virtuale, sommando fittiziamente un successo e un fallimento alle osservazioni. Evita stime estreme ($0$ o $1$) in presenza di campioni ridotti.

---

### 2.3 Derivazione dello Stimatore MAP
Dobbiamo massimizzare la verosimiglianza a posteriori (essendo il prior uniforme):
$$\hat{\theta}_{MAP}(\mathbf{x}^n) = \arg\max_\theta \left[ \theta^{w_H} (1 - \theta)^{n - w_H} \right]$$
Prendendo il logaritmo:
$$g(\theta) = w_H \ln\theta + (n - w_H) \ln(1 - \theta)$$
Derivando rispetto a $\theta$ e uguagliando a zero:
$$\frac{d g(\theta)}{d\theta} = \frac{w_H}{\theta} - \frac{n - w_H}{1 - \theta} = 0 \implies w_H(1-\theta) = (n-w_H)\theta \implies \hat{\theta}_{MAP}(\mathbf{x}^n) = \frac{w_H}{n}$$

> [!important] Risultato
> Lo stimatore MAP coincide esattamente con la **frequenza relativa** (la proporzione empirica di successi osservati).

---

## 3. Proprietà delle Prestazioni degli Stimatori

Per valutare la bontà di uno stimatore, analizziamo il comportamento statistico dell'errore $\hat{\theta}(\mathbf{X}^n) - \theta$ al variare delle realizzazioni dei dati per un dato parametro reale $\theta$ (analisi condizionata a $\theta$).

### 3.1 Polarizzazione (Bias)
> [!info] Definizione
> La **polarizzazione (o bias)** di uno stimatore indica lo scostamento sistematico del valore atteso dello stimatore dal valore reale del parametro:
> $$B(\theta) = E[\hat{\theta}(\mathbf{X}^n) | \theta] - \theta$$
> - Se $B(\theta) = 0$ per ogni $\theta$, lo stimatore si dice **non polarizzato** (o corretto / unbiased).
> - Se $\lim_{n \to \infty} B(\theta) = 0$, lo stimatore si dice **asintoticamente non polarizzato**.

Sotto il vero parametro $\theta$, il peso di Hamming $w_H$ è una variabile binomiale di parametri $n$ e $\theta$, per cui il suo valore atteso è $E[w_H | \theta] = n\theta$.

#### Verifica del Bias per MAP
$$E[\hat{\theta}_{MAP} | \theta] = E\left[ \frac{w_H}{n} \Big| \theta \right] = \frac{n\theta}{n} = \theta$$
Lo stimatore MAP è **non polarizzato** (unbiased).

#### Verifica del Bias per MMSE
$$E[\hat{\theta}_{MMSE} | \theta] = E\left[ \frac{w_H + 1}{n + 2} \Big| \theta \right] = \frac{n\theta + 1}{n + 2} \neq \theta$$
Lo stimatore MMSE è **polarizzato** (biased). Tuttavia:
$$\lim_{n\to\infty} E[\hat{\theta}_{MMSE} | \theta] = \lim_{n\to\infty} \frac{n\theta + 1}{n + 2} = \theta$$
Lo stimatore MMSE è **asintoticamente non polarizzato**.

---

### 3.2 Consistenza
> [!info] Definizione
> Uno stimatore si dice **consistente in media quadratica** se l'errore quadratico medio (MSE) tende a zero al tendere all'infinito del numero di osservazioni:
> $$\lim_{n\to\infty} E[(\hat{\theta}_n - \theta)^2 | \theta] = 0$$

Per la disuguaglianza di Chebyshev, la consistenza in media quadratica implica la **consistenza in probabilità** (consistenza debole):
$$\lim_{n\to\infty} P(|\hat{\theta}_n - \theta| > \epsilon | \theta) = 0$$

#### Calcolo delle prestazioni medie (Errore Quadratico Medio)
Calcoliamo l'MSE medio integrando rispetto alla distribuzione uniforme del parametro $\theta \sim \mathcal{U}[0, 1]$:

- **Per lo stimatore MAP**:
  $$E[(\hat{\theta}_{MAP} - \theta)^2 | \theta] = \text{Var}\left( \frac{w_H}{n} \Big| \theta \right) = \frac{\theta(1-\theta)}{n}$$
  Calcolando l'MSE medio globale integrando sul prior:
  $$E[(\hat{\theta}_{MAP} - \theta)^2] = \int_0^1 \frac{\theta(1-\theta)}{n} d\theta = \frac{1}{n} \left[ \frac{\theta^2}{2} - \frac{\theta^3}{3} \right]_0^1 = \frac{1}{6n}$$

- **Per lo stimatore MMSE**:
  $$E[(\hat{\theta}_{MMSE} - \theta)^2] = \frac{1}{6(n+2)}$$

> [!green] Confronto e Ottimalità
> Poiché lo stimatore MMSE è progettato per minimizzare l'errore quadratico medio calcolato sulla PDF congiunta, si ha:
> $$E[(\hat{\theta}_{MMSE} - \theta)^2] = \frac{1}{6(n+2)} < \frac{1}{6n} = E[(\hat{\theta}_{MAP} - \theta)^2]$$
> Per ogni valore finito di $n$, lo stimatore MMSE garantisce sempre un errore quadratico medio inferiore rispetto allo stimatore MAP. Entrambi gli stimatori sono comunque **consistenti**, poiché l'errore decade a zero come $O(1/n)$.