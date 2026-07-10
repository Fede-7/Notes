# Parametri del Test di Ipotesi

> [!def] Ipotesi Nulla ($H_0$) e Decisione
> Assunzione di base secondo cui il dataset osservato $\pmb { x } ^ { n }$ è la realizzazione di un vettore casuale con distribuzione nota $p _ { X ^ { n } | H _ { 0 } }$ (o $f _ { { \pmb X } ^ { n } | H _ { 0 } }$). Il test mira a decidere se rifiutare $H_0$ a favore di un'ipotesi alternativa $H_1$ tramite una partizione del dominio $\mathcal{X}^n$ in regioni di decisione.

> [!theorem] Errore di tipo-I (Falso Allarme)
> Rappresenta la probabilità di rifiutare $H_0$ quando essa è in realtà vera (ovvero assegnare i dati alla regione di rifiuto $\Omega_1$):
> $$
> \mathbb{P} \{D(\boldsymbol{X}^n) = 1 | H_0\} = \begin{cases} \int_{\Omega_1} f_{\boldsymbol{X}^n | H_0} (\boldsymbol{x}^n | H_0) d \boldsymbol{x}^n & \text{Dati Continui} \\ \sum_{\boldsymbol{x}^n \in \Omega_1} p_{\boldsymbol{X}^n | H_0} (\boldsymbol{x}^n | H_0) & \text{Dati Discreti} \end{cases}
> $$


> [!theorem] Potenza del test
> Rappresenta la capacità del test di rifiutare correttamente l'ipotesi nulla quando è falsa ($H_1$ vera):
> $$
> 1 - \beta = \mathbb{P} \{D(\boldsymbol{X}^n) = 1 | H_1\} = \begin{cases} \int_{\Omega_1} f_{\boldsymbol{X}^n | H_1} (\boldsymbol{x}^n | H_1) d \boldsymbol{x}^n & \text{Dati Continui} \\ \sum_{\boldsymbol{x}^n \in \Omega_1} p_{\boldsymbol{X}^n | H_1} (\boldsymbol{x}^n | H_1) & \text{Dati Discreti} \end{cases}
> $$