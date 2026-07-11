## Analisi delle Prestazioni degli Estimatori: Distorsione e Consistenza

>[!def] Caratterizzazione del Parametro $B$ e dell'Errore
> Si analizzano le proprietà di distorsione (bias) e consistenza degli stimatori rispetto a un parametro casuale $B$, fondate sulla scomposizione dell'Errore Quadratico Medio: $\text{MSE} = \text{Bias}^2 + \text{Varianza}$.
> * **Media a priori**: $\mathbb{E}[B] = \int_{0}^{1} \beta \, d\beta = \frac{1}{2}$
> * **Momento secondo a priori**: $\mathbb{E}[B^2] = \frac{1}{3}$
> * **Varianza a priori**: $\sigma_{B}^2 = \frac{1}{12}$

>[!dim] Calcolo dei momenti della statistica $w(\boldsymbol{X}^n)$
> Sfruttando la legge delle aspettative iterate rispetto a $B$:
> * **Media**:
>   $$\mathbb{E}[w(\boldsymbol{X}^n)] = \mathbb{E}\left[ \overbrace{\mathbb{E}[w(\boldsymbol{X}^n) \mid B]}^{nB} \right] = n \mathbb{E}[B] = \frac{n}{2}$$
> * **Momento secondo**:
>   $$\mathbb{E}[w^2(\boldsymbol{X}^n)] = \mathbb{E}\left[ \overbrace{\mathbb{E}[w^2(\boldsymbol{X}^n) \mid B]}^{nB(1 - B) + n^2B^2} \right] = \frac{n}{6} + \frac{n^2}{3}$$
> * **Varianza**:
>   $$\sigma_{w(\boldsymbol{X}^n)}^2 = \frac{n}{6}\left(1 + \frac{n}{2}\right)$$

>[!theorem] Analisi del Bias e dell'Errore Quadratico Medio (MSE)
> 
> ### 1. Stimatore MMSE ($\hat{B}_{\text{MMSE}}$)
> * **Media condizionata**: $\mathbb{E}[\hat{B}_{\text{MMSE}}(\boldsymbol{X}^n) \mid B = \beta] = \frac{n\beta + 1}{n + 2}$
> * **Media totale**: $\mathbb{E}[\hat{B}_{\text{MMSE}}(\boldsymbol{X}^n)] = \frac{\frac{n}{2} + 1}{n + 2} \neq \mathbb{E}[B] \implies$ **Distorto (Biased)**
> * **MSE dello stimatore**:
>   $$\mathbb{E}\left[(\hat{B}_{\text{MMSE}}(\boldsymbol{X}^n) - B)^2\right] = \overline{{e^2}}_{\text{MMSE}} = \frac{n - 2}{6(n + 2)^2}$$
> 
> ### 2. Stimatore MAP ($\hat{B}_{\text{MAP}}$)
> * **Media condizionata**: $\mathbb{E}[\hat{B}_{\text{MAP}}(\boldsymbol{X}^n) \mid B = \beta] = \beta$
> * **Media totale**: $\mathbb{E}[\hat{B}_{\text{MAP}}(\boldsymbol{X}^n)] = \frac{\frac{n}{2}}{n} = \frac{1}{2} = \mathbb{E}[B] \implies$ **Non distorto (Unbiased)**
> * **MSE dello stimatore**:
>   $$\mathbb{E}\left[(\hat{B}_{\mathrm{MAP}}(\boldsymbol{X}^n) - B)^2\right] = \overline{{e^2}}_{\mathrm{MAP}} = \frac{1}{6n}$$
> 
> ### Dominanza energetica dell'MMSE
> Per qualsiasi dimensione del campione $n$, vale la relazione di ottimalità globale dell'MMSE:
> $$\overline{{e^2}}_{\text{MMSE}} < \overline{{e^2}}_{\text{MAP}} \quad \forall n$$

>[!def] Analisi Asintotica e Consistenza ($n \to \infty$)
> Al crescere del campione, l'errore sistematico e l'errore casuale decadono secondo tre livelli di consistenza:
> 
> 1. **Consistenza in Media Quadratica (MS):** I rispettivi MSE tendono a zero ($\lim_{n \to \infty} \overline{{e^2}} = 0$). Di conseguenza, l'MMSE è **asintoticamente non distorto**:
>    $$\lim_{n \to \infty} \mathbb{E}[\hat{B}_{\text{MMSE}}(\boldsymbol{X}^n)] = \lim_{n \to \infty} \frac{\frac{n}{2} + 1}{n + 2} = \frac{1}{2} = \mathbb{E}[B]$$
> 
> 2. **Consistenza Debole (In Probabilità):** Sfruttando la disuguaglianza di Chebyshev, la convergenza MS garantisce che:
>    $$\forall \epsilon > 0, \quad \lim_{n \to \infty} \Pr \{ | \hat{B}(\boldsymbol{X}^n) - B | > \epsilon \} = 0 \iff \hat{B}(\boldsymbol{X}^n) \overset{P}{\to} B$$
> 
> 3. **Consistenza Forte (Quasi Certa):** Entrambi gli stimatori convergono al valore vero con probabilità 1:
>    $$\Pr \{ \lim_{n \to \infty} \hat{B}(\boldsymbol{X}^n) = B \} = 1 \iff \hat{B}(\boldsymbol{X}^n) \overset{\text{q.c.}}{\to} B$$
