
> [!def] Classificazione Binaria (Caso Continuo)
> Procedura per decidere tra $M$ ipotesi mutuamente esclusive basandosi su funzioni di densità di probabilità (pdf) condizionate $\{ f_{\pmb{X}^n | H_i} (\pmb{x}^n | $H_i$) \}_{i = 1}^M$.

### Definizione delle Probabilità di Regione
A differenza del caso discreto, la probabilità che un vettore casuale appartenga a una determinata regione di decisione $\Omega_i$ viene calcolata tramite l'integrazione della sua pdf condizionata:
$$\mathbb{P} \left\{\boldsymbol{X}^n \in \Omega_1 | H_1 \right\} = \int_{\Omega_1} f_{\boldsymbol{X}^n | H_1} \left(\boldsymbol{x}^n | H_1\right) d \boldsymbol{x}^n$$
$$\mathbb{P} \left\{\boldsymbol{X}^n \in \Omega_2 | H_2 \right\} = \int_{\Omega_2} f_{\boldsymbol{X}^n | H_2} \left(\boldsymbol{x}^n | H_2\right) d \boldsymbol{x}^n$$.

### Regola di Decisione Ottima
> [!theorem] Criterio della Probabilità di Errore Minima
> Per minimizzare l'errore, il test assegna il dataset osservato $\pmb{x}^n$ alla regione $\Omega_i$ se e solo se la verosimiglianza pesata dell'ipotesi è superiore a quella alternativa:
> $$\boldsymbol{x}^n \in \Omega_i \text { iff } f_{\boldsymbol{X}^n | H_1} (\boldsymbol{x}^n | H_1) P(H_1) > f_{\boldsymbol{X}^n | H_2} (\boldsymbol{x}^n | H_2) P(H_2)$$.

### Rapporto di Verosimiglianza
> [!dim] Formulazione del Test Rapporto di Verosimiglianza
> La regola di decisione può essere espressa confrontando il rapporto tra le densità di probabilità (LHS) con una soglia $\eta$ definita dal rapporto delle probabilità a priori:
> $$L (\boldsymbol{x}^n) = \frac{f_{\boldsymbol{X}^n | H_1} (\boldsymbol{x}^n | H_1)}{f_{\boldsymbol{X}^n | H_2} (\boldsymbol{x}^n | H_2)} \underset{H_2}{\overset{H_1}{\gtrless}} \frac{P (H_2)}{P (H_1)} = \eta$$.

> [!def] Rapporto di Verosimiglianza ($L$)
> Quantità che rappresenta il rapporto tra la probabilità di osservare i dati sotto l'ipotesi $H_1$ rispetto all'ipotesi $H_2$.