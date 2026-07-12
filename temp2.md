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

