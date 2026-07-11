





> [!dim] Determinazione della Stima Bayes-Ottimale
> Data la struttura del rischio medio, per minimizzare l'errore su un campione specifico $\pmb{x}^n$, è sufficiente minimizzare l'integrale della funzione di costo pesata per la distribuzione a posteriori del parametro:
> $$\mathbb{E} \left[ C (\widehat{\Theta}(\pmb{X}^n) - \Theta) \right] = \sum_{\pmb{x}^n \in \mathcal{X}^n} p_{\pmb{X}^n}(\pmb{x}^n) \int C (\widehat{\theta}(\pmb{x}^n) - \theta) f_{\Theta | \pmb{X}^n} (\theta \mid \pmb{x}^n) d \theta$$.
> La stima puntuale Bayes-ottimale per un'osservazione $\pmb{x}^n$ è quindi:
> $$\widehat{\theta}(\pmb{x}^n) = \arg \min \int C (\widehat{\theta}(\pmb{x}^n) - \theta) f_{\Theta | \pmb{X}^n} (\theta \mid \pmb{x}^n) d \theta$$.