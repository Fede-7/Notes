## Unicità e Ottimalità degli Estimatori Bayesiani

>[!def] Condizione di Simmetria della Posterior
> Una distribuzione a posteriori $f_{\Theta|\boldsymbol{X}^n}(\theta|\boldsymbol{x}^n)$ si dice simmetrica rispetto alla sua media $\mu$ se soddisfa la seguente proprietà di invarianza rispetto al segno dell'errore:
> $$f_{\Theta|\boldsymbol{X}^n}(\theta - \mathbb{E}[\Theta|\boldsymbol{x}^n] | \boldsymbol{x}^n) = f_{\Theta|\boldsymbol{X}^n}(- \theta + \mathbb{E}[\Theta|\boldsymbol{x}^n] | \boldsymbol{x}^n)$$

>[!theorem] Ottimalità Universale dell'MMSE
> Sia $C(\cdot)$ una funzione di costo **pari e convessa**. Se la distribuzione a posteriori è simmetrica rispetto alla propria media, allora lo stimatore MMSE minimizza il rischio Bayesiano per **qualsiasi** funzione di costo appartenente a questa classe.

>[!tip] Coincidenza MMSE e MAP
> Sotto la medesima condizione di simmetria, lo stimatore MAP e lo stimatore MMSE coincidono:
> $$\widehat{\mu}_{\text{MAP}}(\boldsymbol{x}^n) = \widehat{\mu}_{\text{MMSE}}(\boldsymbol{x}^n)$$
> *Nota*: Sebbene la funzione di costo 0-1 (usata per il MAP) non sia differenziabile, la simmetria della posterior garantisce comunque l'allineamento tra moda (MAP) e media (MMSE).