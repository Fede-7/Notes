
## Definizioni Generali

**Setup**: campione $\boldsymbol{x}^n \in \mathcal{X}^n$ estratto da $\boldsymbol{X}^n$, con pdf congiunta $f_{\boldsymbol{X}^n,\Theta}(\boldsymbol{x}^n,\theta)$ e prior $f_\Theta(\theta)$ note. L'obiettivo è stimare $\theta$ data la realizzazione $\boldsymbol{x}^n$.

$$
\widehat{\theta}_{\mathrm{MMSE}}(\boldsymbol{x}^n) = \mathbb{E}[\Theta \mid \boldsymbol{X}^n = \boldsymbol{x}^n] = \int \theta\, f_{\Theta|\boldsymbol{X}^n}(\theta|\boldsymbol{x}^n)\,d\theta
$$

$$
\widehat{\theta}_{\mathrm{MAP}}(\boldsymbol{x}^n) = \arg\max_\theta\, f_{\Theta|\boldsymbol{X}^n}(\theta|\boldsymbol{x}^n)
$$

Proprietà degli stimatori:

> **Unbiased (non distorto)**
> $\mathbb{E}[\widehat{\Theta}(\boldsymbol{X}^n) - \Theta] = 0$

> **Asintoticamente unbiased**
> Vale solo nel limite $n \to \infty$.

> **Consistente / MS consistente / Fortemente consistente**
> $\widehat{\Theta}(\boldsymbol{X}^n) \to \Theta$ rispettivamente in probabilità, in media quadratica, quasi certamente.

## Unicità degli stimatori Bayesiani

Una distribuzione a posteriori $f_{\Theta|\boldsymbol{X}^n}(\theta|\boldsymbol{x}^n)$ si dice simmetrica rispetto alla sua media $\mu$ se soddisfa la seguente proprietà di invarianza rispetto al segno dell'errore: $$f_{\Theta|\boldsymbol{X}^n}(\theta - \mathbb{E}[\Theta|\boldsymbol{x}^n] | \boldsymbol{x}^n) = f_{\Theta|\boldsymbol{X}^n}(- \theta + \mathbb{E}[\Theta|\boldsymbol{x}^n] | \boldsymbol{x}^n)$$

>[!theorem] Ottimalità Universale dell'MMSE
> Sia $C(\cdot)$ una funzione di costo **pari e convessa**. 
> Se la distribuzione a posteriori è simmetrica rispetto alla propria media, allora lo stimatore MMSE minimizza il rischio Bayesiano per **qualsiasi** funzione di costo appartenente a questa classe (pari e convessa).

Sotto la medesima condizione di simmetria, lo stimatore MAP e lo stimatore MMSE coincidono: $$\widehat{\mu}_{\text{MAP}}(\boldsymbol{x}^n) = \widehat{\mu}_{\text{MMSE}}(\boldsymbol{x}^n)$$
*Nota*: Sebbene la funzione di costo 0-1 (usata per il MAP) non sia differenziabile, la simmetria della posterior garantisce comunque l'allineamento tra moda (MAP) e media (MMSE).


---

# Inferenza non Bayesiana: Stima di parametri non casuali

**Setup**: $\theta$ deterministico e sconosciuto (nessun prior). Osservazioni $\boldsymbol{x}^n$ da $f_{\boldsymbol{X}^n}(\boldsymbol{x}^n;\theta)$, spazio parametri $\mathcal{S}$.

> **Verosimiglianza / Log-verosimiglianza**
> $$L(\theta;\boldsymbol{x}^n) = f_{\boldsymbol{X}^n}(\boldsymbol{x}^n;\theta), \qquad \Lambda(\theta;\boldsymbol{x}^n) = \log f_{\boldsymbol{X}^n}(\boldsymbol{x}^n;\theta)$$

> **Stimatore ML**
> $$\widehat{\theta}_{\mathrm{ML}}(\boldsymbol{x}^n) = \arg\max_{\theta \in \mathcal{S}}\, \log f_{\boldsymbol{X}^n}(\boldsymbol{x}^n;\theta)$$

## Misure di prestazione

Dato uno stimatore $\widehat{\Theta}(\boldsymbol{X}^n)$ con bias $b_n(\theta)$:

$$
\mathbb{E}[\widehat{\Theta}(\boldsymbol{X}^n)] = \theta + b_n(\theta), \qquad \mathbb{E}\!\left[(\widehat{\Theta}(\boldsymbol{X}^n) - \theta)^2\right] = \overline{e_n^2}
$$

Uno stimatore unbiased MMSE minimizza la varianza $\operatorname{Var}[\widehat{\Theta}] = \mathbb{E}[\widehat{\Theta}^2] - \theta^2$. Consistenza: debole ($\to\theta$ in prob.), forte ($\to\theta$ q.c.), MS ($\overline{e_n^2}\to 0$).

## Limite di Cramér-Rao

### Fatti preliminari

Differenziando $\int f_{\boldsymbol{X}^n}(\boldsymbol{x}^n;\theta)\,d\boldsymbol{x}^n = 1$ rispetto a $\theta$:

$$
\mathbb{E}\!\left[\frac{\partial \log f_{\boldsymbol{X}^n}(\boldsymbol{X}^n;\theta)}{\partial\theta}\right] = 0
$$

Differenziando ancora:

$$
\mathbb{E}\!\left[\!\left(\frac{\partial \log f_{\boldsymbol{X}^n}(\boldsymbol{X}^n;\theta)}{\partial\theta}\right)^{\!2}\right] = -\mathbb{E}\!\left[\frac{\partial^2 \log f_{\boldsymbol{X}^n}(\boldsymbol{X}^n;\theta)}{\partial\theta^2}\right]
$$

### Derivazione

Differenziando rispetto a $\theta$ la definizione di bias si ottiene:

$$
\operatorname{Cov}\!\left[\widehat{\Theta}(\boldsymbol{X}^n),\;\frac{\partial \log f_{\boldsymbol{X}^n}(\boldsymbol{X}^n;\theta)}{\partial\theta}\right] = 1 + b_n'(\theta)
$$

Applicando Cauchy-Schwarz:

$$
\left[1 + b_n'(\theta)\right]^2 \leq \operatorname{Var}[\widehat{\Theta}(\boldsymbol{X}^n)]\cdot\operatorname{Var}\!\left[\frac{\partial \log f_{\boldsymbol{X}^n}(\boldsymbol{X}^n;\theta)}{\partial\theta}\right]
$$

### Risultato

> **Informazione di Fisher**
> $$I_n(\theta) = \mathbb{E}\!\left[\!\left(\frac{\partial \log f_{\boldsymbol{X}^n}(\boldsymbol{X}^n;\theta)}{\partial\theta}\right)^{\!2}\right] = -\mathbb{E}\!\left[\frac{\partial^2 \log f_{\boldsymbol{X}^n}(\boldsymbol{X}^n;\theta)}{\partial\theta^2}\right]$$

> [!theorem] Cramér-Rao Bound (CRB)
> $$\operatorname{Var}[\widehat{\Theta}(\boldsymbol{X}^n)] \geq \frac{[1+b_n'(\theta)]^2}{I_n(\theta)}$$
> Per stimatori **unbiased** ($b_n = 0$):
> $$\operatorname{Var}[\widehat{\Theta}] = \mathbb{E}\!\left[(\widehat{\Theta}-\theta)^2\right] \geq \frac{1}{I_n(\theta)}$$

> **Stimatore efficiente**
> Uno stimatore unbiased il cui MSE raggiunge il CRB.

> [!theorem]
> Se esiste uno stimatore efficiente per un dato problema di stima non bayesiana, coincide necessariamente con lo stimatore ML.

## Un esempio: Stima della frequenza Bernoulli

$\boldsymbol{X}^n \sim \mathcal{B}(1,\beta)$, $\beta$ sconosciuto; $w(\boldsymbol{x}^n)$ = peso di Hamming della sequenza.

$$
p_{\boldsymbol{X}^n}(\boldsymbol{x}^n;\beta) = \beta^{w(\boldsymbol{x}^n)}(1-\beta)^{n-w(\boldsymbol{x}^n)}
$$

Annullando la derivata della log-likelihood:

$$
\frac{\partial \log p_{\boldsymbol{X}^n}(\boldsymbol{x}^n;\beta)}{\partial\beta} = 0 \implies \widehat{\beta}_{\mathrm{ML}}(\boldsymbol{x}^n) = \frac{w(\boldsymbol{x}^n)}{n}
$$

Lo stimatore $\widehat{\beta} = w(\boldsymbol{X}^n)/n$ è unbiased e ha varianza $\beta(1-\beta)/n$. Per l'efficienza si calcola:

$$
I_n(\beta) = \frac{n}{\beta} + \frac{n}{1-\beta} = \frac{n}{\beta(1-\beta)} \implies \mathrm{CRB} = \frac{\beta(1-\beta)}{n}
$$

La varianza raggiunge il CRB: la MLE è **efficiente**.

---

# Stima a parametri multipli

## Inferenza Bayesiana

$\boldsymbol{\theta} = [\theta_1,\ldots,\theta_m]^T$ casuale con prior $f_\Theta(\boldsymbol{\theta})$; dati $\boldsymbol{x}^n$ da $f_{\boldsymbol{X}^n|\boldsymbol{\theta}}(\boldsymbol{x}^n|\boldsymbol{\theta})$. Lo stimatore ottimo minimizza:

$$
\widehat{\boldsymbol{\Theta}}(\boldsymbol{X}^n) = \arg\min\int_{\mathbb{R}^m} C\!\left(\boldsymbol{\theta} - \widehat{\boldsymbol{\theta}}(\boldsymbol{X}^n)\right) f_{\Theta|\boldsymbol{X}^n}(\boldsymbol{\theta}\mid\boldsymbol{X}^n)\,d\boldsymbol{\theta}
$$

### MMSE

Costo quadratico $C = \sum_i (\theta_i - \widehat{\theta}_i)^2$, problema separabile:

$$
\widehat{\theta}_i(\boldsymbol{x}^n) = \mathbb{E}[\Theta_i \mid \boldsymbol{X}^n = \boldsymbol{x}^n] \implies \widehat{\boldsymbol{\Theta}}(\boldsymbol{X}^n) = \mathbb{E}[\boldsymbol{\Theta}\mid\boldsymbol{X}^n]
$$

### MAP

Massimizza la posterior congiunta:

$$
\nabla_{\boldsymbol{\theta}}\, f_{\boldsymbol{\Theta}|\boldsymbol{X}^n}(\boldsymbol{\theta}|\boldsymbol{x}^n)\big|_{\boldsymbol{\theta}=\widehat{\boldsymbol{\theta}}} = \mathbf{0}
$$

## Stima non Bayesiana di parametri multipli

$\boldsymbol{\theta}$ reale e deterministico. La MLE risolve:

$$
\Lambda(\boldsymbol{\theta};\boldsymbol{x}^n) = \log f_{\boldsymbol{X}^n}(\boldsymbol{x}^n;\boldsymbol{\theta}), \qquad \nabla_{\boldsymbol{\theta}}\,\Lambda(\boldsymbol{\theta};\boldsymbol{x}^n)\big|_{\boldsymbol{\theta}=\widehat{\boldsymbol{\theta}}} = \mathbf{0}
$$

### Estimatore LMMSE

Stimatore nella forma $\widehat{\Theta}(\boldsymbol{X}^n) = \boldsymbol{a}^T\boldsymbol{X}^n + b$, con $\boldsymbol{a}\in\mathbb{R}^n$. Si minimizza:

$$
\mathbb{E}\!\left[(\boldsymbol{a}^T\boldsymbol{X}^n + b - \Theta)^2\right] = \boldsymbol{a}^T\boldsymbol{R}\boldsymbol{a} + b^2 + \mathbb{E}[\Theta^2] - 2b\overline{\Theta} - 2\boldsymbol{a}^T\mathbb{E}[\boldsymbol{X}^n\Theta] - 2b\boldsymbol{a}^T\mathbb{E}[\boldsymbol{X}^n]
$$

con $\boldsymbol{R} = \mathbb{E}[\boldsymbol{X}^n\boldsymbol{X}^{nT}]$ matrice di correlazione. Annullando le derivate rispetto a $\boldsymbol{a}$ e $b$:

$$
b_{\mathrm{LMMSE}} = \mathbb{E}[\Theta] - \boldsymbol{a}^T\mathbb{E}[\boldsymbol{X}^n]
$$

$$
\boldsymbol{a}_{\mathrm{LMMSE}} = \boldsymbol{M}^{-1}\boldsymbol{s}
$$

con $\boldsymbol{M} = \mathbb{E}[(\boldsymbol{X}^n - \mathbb{E}[\boldsymbol{X}^n])(\boldsymbol{X}^n - \mathbb{E}[\boldsymbol{X}^n])^T]$ covarianza di $\boldsymbol{X}^n$ e $\boldsymbol{s} = \mathbb{E}[(\boldsymbol{X}^n - \mathbb{E}[\boldsymbol{X}^n])(\Theta - \mathbb{E}[\Theta])]$.

### Algoritmo del gradiente

Il gradiente dell'MSE rispetto a $\boldsymbol{a}$ è $2\boldsymbol{M}\boldsymbol{a} - 2\boldsymbol{s}$. Iterazione:

$$
\boldsymbol{a}^{(k+1)} = \boldsymbol{a}^{(k)} - \gamma(\boldsymbol{M}\boldsymbol{a}^{(k)} - \boldsymbol{s})
$$

L'errore $\boldsymbol{\epsilon}^{(k)} = \boldsymbol{a}^{(k)} - \boldsymbol{a}_{\mathrm{LMMSE}}$ evolve come:

$$
\boldsymbol{\epsilon}^{(k+1)} = (\boldsymbol{I} - \gamma\boldsymbol{M})\boldsymbol{\epsilon}^{(k)} \implies \boldsymbol{\epsilon}^{(k)} = \boldsymbol{U}(\boldsymbol{I}-\gamma\boldsymbol{\Lambda})^{k-1}\boldsymbol{U}^T\boldsymbol{\epsilon}^{(1)}
$$

con $\boldsymbol{\Lambda}$ diagonale degli autovalori di $\boldsymbol{M}$ e $\boldsymbol{U}$ matrice degli autovettori. L'errore converge se:

$$
0 < \gamma < \frac{2}{\lambda_{\mathrm{MAX}}}
$$

---

# Un approccio diverso: Statistica Descrittiva

In questa sezione i campioni sono **entità dati** (non realizzazioni di v.c.). Dataset $\boldsymbol{X} \in \mathbb{R}^{n\times p}$, target $\boldsymbol{y} \in \mathbb{R}^p$. Modello lineare:

$$
\boldsymbol{y} = \boldsymbol{X}^T\boldsymbol{a} + \boldsymbol{\epsilon}
$$

## L'estimatore Least Squares (LS)

Si minimizza $\|\boldsymbol{X}^T\boldsymbol{a} - \boldsymbol{y}\|^2$. Differenziando rispetto a $\boldsymbol{a}$:

$$
\nabla_{\boldsymbol{a}}\|\boldsymbol{X}^T\boldsymbol{a} - \boldsymbol{y}\|^2 = 2\boldsymbol{X}\boldsymbol{X}^T\boldsymbol{a} - 2\boldsymbol{X}\boldsymbol{y} = 0
$$

$$
\boldsymbol{a}_{\mathrm{LS}}(p) = (\boldsymbol{X}(p)\boldsymbol{X}^T(p))^{-1}\boldsymbol{X}(p)\boldsymbol{y}(p)
$$

Richiede $p \geq n$ per l'invertibilità di $\boldsymbol{X}\boldsymbol{X}^T$. Per $p \to \infty$ si distinguono due scenari: aggiornamento progressivo con nuovi dati, o adattamento a condizioni variabili dimenticando i dati vecchi.

## Apprendimento LS (aggiornamento ricorsivo)

Aggiungendo il campione $\boldsymbol{x}^n(p+1)$ con label $\theta(p+1)$, la nuova stima richiederebbe ricalcolare $(\boldsymbol{X}(p+1)\boldsymbol{X}^T(p+1))^{-1}$.

> [!quote] Osservazione
> Ricalcolare l'inversione per ogni nuovo dato ha complessità $\mathcal{O}(n^3)$, mentre il prodotto di matrici è $\mathcal{O}(n^2)$. Si può fare di meglio con Sherman-Morrison.

## La Formula di Sherman-Morrison

> [!theorem] Lemma di inversione rank-1
> Sia $\boldsymbol{R}$ invertibile, $\boldsymbol{u}, \boldsymbol{v}$ vettori colonna $n$-dimensionali:
> $$\left(\boldsymbol{R} + \boldsymbol{u}\boldsymbol{v}^T\right)^{-1} = \boldsymbol{R}^{-1} - \frac{\boldsymbol{R}^{-1}\boldsymbol{u}\boldsymbol{v}^T\boldsymbol{R}^{-1}}{1+\boldsymbol{v}^T\boldsymbol{R}^{-1}\boldsymbol{u}}$$

## Applicazione

Poiché $\boldsymbol{R}(p+1) = \boldsymbol{R}(p) + \boldsymbol{x}^n(p+1)\boldsymbol{x}^{nT}(p+1)$, per Sherman-Morrison:

$$
\boldsymbol{R}^{-1}(p+1) = \boldsymbol{R}^{-1}(p) - \frac{\boldsymbol{R}^{-1}(p)\,\boldsymbol{x}^n(p+1)\,\boldsymbol{x}^{nT}(p+1)\,\boldsymbol{R}^{-1}(p)}{1+K(p+1)}
$$

con $K(p+1) = \boldsymbol{x}^{nT}(p+1)\boldsymbol{R}^{-1}(p)\boldsymbol{x}^n(p+1)$. L'aggiornamento di $\boldsymbol{a}$:

$$
\boldsymbol{a}(p+1) = \left[\boldsymbol{I}_n - \frac{\boldsymbol{R}^{-1}(p)\,\boldsymbol{x}^n(p+1)\,\boldsymbol{x}^{nT}(p+1)}{1+K(p+1)}\right]\!\left[\boldsymbol{a}(p) + \theta(p+1)\,\boldsymbol{R}^{-1}(p)\,\boldsymbol{x}^n(p+1)\right]
$$

Complessità: $\mathcal{O}(n^2)$, indipendente da $p$.

## Adattività in LS

Per ambienti variabili nel tempo si adotta la **media mobile esponenziale** con $w < 1$, che pesa meno i dati storici:

$$
\sum_{i=1}^p w^{p-i}\left[\boldsymbol{a}^T\boldsymbol{x}^n(i) - \theta(i)\right]^2
$$

Minimizzando si ottiene l'**LS esponenzialmente pesato**:

$$
\boldsymbol{a} = \left[\sum_{i=1}^p w^{p-i}\boldsymbol{x}^n(i)\boldsymbol{x}^{nT}(i)\right]^{-1}\sum_{i=1}^p w^{p-i}\boldsymbol{x}^n(i)\theta(i)
$$

Implementabile ricorsivamente via Sherman-Morrison.

## Generalizzazione: LS con bias

Modello $\widehat{\theta}(\boldsymbol{x}^n) = \boldsymbol{a}^T\boldsymbol{x}^n + b$. Operando su dati centrati ($\boldsymbol{X}_0 = \boldsymbol{X} - \bar{\boldsymbol{x}}\mathbf{1}_p^T$, $\boldsymbol{y}_0 = \boldsymbol{y} - \tilde{\theta}\mathbf{1}_p$):

$$
\boldsymbol{a}_{\mathrm{LMS}} = (\boldsymbol{X}_0\boldsymbol{X}_0^T)^{-1}\boldsymbol{X}_0\boldsymbol{y}_0, \qquad b_{\mathrm{LMS}} = \tilde{\theta} - \frac{1}{p}\mathbf{1}_p^T\boldsymbol{X}^T\boldsymbol{a}_{\mathrm{LMS}}
$$

con $\tilde{\theta} = \frac{1}{p}\sum_i\theta(i)$ media del target, $\bar{x}_k = \frac{1}{p}\sum_i x_k(i)$ medie delle feature, e $\boldsymbol{X}_0 = \boldsymbol{X} - \bar{\boldsymbol{x}}\mathbf{1}_p^T$.
