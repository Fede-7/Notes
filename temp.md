# Capitolo 6: Stimatori Bayesiani Ottimi

> [!def] Estimatore MMSE (Minimum Mean Square Error)
> Estimatore che minimizza il valore atteso del quadrato dell'errore (costo quadratico). Corrisponde matematicamente alla **media della distribuzione a posteriori**.

> [!dim] Derivazione dell'MMSEE
> Assunta la funzione di costo $C(\widehat{\Theta} - \Theta) = (\widehat{\Theta} - \Theta)^2$, la stima ottimale si ricava annullando la derivata del rischio rispetto alla stima puntuale:
> $$\frac {\partial}{\partial \widehat {\theta} (\boldsymbol {x} ^ {n})} \int (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) ^ {2} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta = 0$$
> **Risultato:**
> $$\widehat {\theta} (\boldsymbol {x} ^ {n}) = \int \theta f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta = \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ]$$

---

> [!def] Estimatore MAP (Maximum A Posteriori)
> Metodo di stima che massimizza la probabilità a posteriori del parametro. Rappresenta il valore più probabile (la **moda**) data l'osservazione dei dati.

> [!dim] Derivazione del MAPE
> Si adotta una funzione di costo uniforme "0-1" (funzione porta $\Pi$) che assegna costo nullo se l'errore è contenuto in un intorno $\epsilon$ e costo unitario altrimenti:
> $$C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) = \Pi \left(\frac {\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta}{\epsilon}\right)$$
> Per $\epsilon$ arbitrariamente piccola, la regola seleziona il picco della densità a posteriori:
> $$\widehat {\theta} (\boldsymbol {x} ^ {n}) = \arg \max_{\theta} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n})$$

---

> [!rb] Applicazione: Modello Bernoulli Composto
> Dato un campione $\pmb{x}^n \in \{0, 1\}^n$ con peso di Hamming $w(\pmb{x}^n)$ (numero di successi), si ottengono le seguenti stime per il parametro $\beta$:
> - **Stima MAP:** $\widehat{\beta}_{\mathrm{MAP}} (\pmb{x}^n) = \frac{w(\pmb{x}^n)}{n}$
> - **Stima MMSE:** $\widehat{\beta}_{\text{MMSE}}(\boldsymbol{x}^n) = \frac{w(\pmb{x}^n) + 1}{n + 2}$

