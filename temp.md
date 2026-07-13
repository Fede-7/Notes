# Un approccio diverso: Statistica Descrittiva

In questa sezione i campioni sono **entità dati concrete** (non variabili casuali). Organizzi i dati in una matrice $\boldsymbol{X} \in \mathbb{R}^{n\times p}$ (features) e un vettore $\boldsymbol{y} \in \mathbb{R}^p$ (target/output).
**Modello lineare**:
$$
\boldsymbol{y} = \boldsymbol{X}^T\boldsymbol{a} + \boldsymbol{\epsilon}
$$
Cioè: ogni output è una combinazione lineare degli input, più un termine di errore $\boldsymbol{\epsilon}$.

## L'estimatore Least Squares (LS)

Per trovare i coefficienti $\boldsymbol{a}$, minimizzi l'errore quadratico totale: $\|\boldsymbol{X}^T\boldsymbol{a} - \boldsymbol{y}\|^2$.

Derivando rispetto ad $\boldsymbol{a}$ e uguagliando a zero:
$$
\nabla_{\boldsymbol{a}}\|\boldsymbol{X}^T\boldsymbol{a} - \boldsymbol{y}\|^2 = 2\boldsymbol{X}\boldsymbol{X}^T\boldsymbol{a} - 2\boldsymbol{X}\boldsymbol{y} = 0
$$
**Soluzione**:
$$
\boldsymbol{a}_{\mathrm{LS}}(p) = (\boldsymbol{X}(p)\boldsymbol{X}^T(p))^{-1}\boldsymbol{X}(p)\boldsymbol{y}(p)
$$
Questo richiede che $p \geq n$ affinché la matrice $\boldsymbol{X}\boldsymbol{X}^T$ sia invertibile. 
Per $p \to \infty$ emergono due scenari: 
- aggiornamento *continuo* con nuovi dati in arrivo, 
- *adattamento* a ambienti che cambiano nel tempo.

### LS Ricorsivo (Continuo)

Quando arriva un nuovo campione $\boldsymbol{x}^n(p+1)$ con label $\theta(p+1)$, in teoria devi ricalcolare l'intera inversione $(\boldsymbol{X}(p+1)\boldsymbol{X}^T(p+1))^{-1}$, il che costa $\mathcal{O}($n^3$)$ operazioni, troppo lento se i dati arrivano continuamente.

**Soluzione**: la **Formula di Sherman-Morrison** aggiorna la soluzione precedente senza ricalcolare tutto da capo.

#### La Formula di Sherman-Morrison

> [!theorem] Lemma
> Se $\boldsymbol{R}$ è invertibile e $\boldsymbol{u}, \boldsymbol{v}$ sono vettori colonna $n$-dimensionali:
> $$
> \left(\boldsymbol{R} + \boldsymbol{u}\boldsymbol{v}^T\right)^{-1} = \boldsymbol{R}^{-1} - \frac{\boldsymbol{R}^{-1}\boldsymbol{u}\boldsymbol{v}^T\boldsymbol{R}^{-1}}{1+\boldsymbol{v}^T\boldsymbol{R}^{-1}\boldsymbol{u}}
> $$

Applicando questo al tuo problema, poiché $\boldsymbol{R}(p+1) = \boldsymbol{R}(p) + \boldsymbol{x}^n(p+1)\boldsymbol{x}^{nT}(p+1)$:
$$
\boldsymbol{R}^{-1}(p+1) = \boldsymbol{R}^{-1}(p) - \frac{\boldsymbol{R}^{-1}(p)\,\boldsymbol{x}^n(p+1)\,\boldsymbol{x}^{nT}(p+1)\,\boldsymbol{R}^{-1}(p)}{1+K(p+1)}
$$
dove $K(p+1) = \boldsymbol{x}^{nT}(p+1)\boldsymbol{R}^{-1}(p)\boldsymbol{x}^n(p+1)$.

L'aggiornamento dei coefficienti diventa:
$$
\boldsymbol{a}(p+1) = \left[\boldsymbol{I}_n - \frac{\boldsymbol{R}^{-1}(p)\,\boldsymbol{x}^n(p+1)\,\boldsymbol{x}^{nT}(p+1)}{1+K(p+1)}\right]\!\left[\boldsymbol{a}(p) + \theta(p+1)\,\boldsymbol{R}^{-1}(p)\,\boldsymbol{x}^n(p+1)\right]
$$
**Vantaggio**: complessità $\mathcal{O}($n^2$)$, indipendente dal numero di dati $p$.

### LS Esponenziale (adattivo)

In ambienti che cambiano nel tempo, non tutti i dati hanno lo stesso valore. Usa una **media mobile esponenziale** con fattore di decadimento $w < 1$ che riduce il peso dei dati vecchi:
$$
\sum_{i=1}^p w^{p-i}\left[\boldsymbol{a}^T\boldsymbol{x}^n(i) - \theta(i)\right]^2
$$
Minimizzando questa somma pesata, ottieni l'**LS esponenzialmente pesato**:
$$
\boldsymbol{a} = \left[\sum_{i=1}^p w^{p-i}\boldsymbol{x}^n(i)\boldsymbol{x}^{nT}(i)\right]^{-1}\sum_{i=1}^p w^{p-i}\boldsymbol{x}^n(i)\theta(i)
$$
Anche questo è implementabile ricorsivamente usando Sherman-Morrison.

## LS con Bias (intercetta)

Spesso il modello include un termine costante:
$$
\widehat{\theta} = \boldsymbol{a}^T\boldsymbol{x}^n + b
$$
Per trovare sia $\boldsymbol{a}$ che $b$, **centra i dati** prima di calcolare: sottrai le medie da ogni feature e dal target.

Definisci i dati centrati come:
- $\boldsymbol{X}_0 = \boldsymbol{X} - \bar{\boldsymbol{x}}\mathbf{1}_p^T$ (feature minus their means)
- $\boldsymbol{y}_0 = \boldsymbol{y} - \tilde{\theta}\mathbf{1}_p$ (target minus its mean)

Allora:
$$
\boldsymbol{a}_{\mathrm{LS}} = (\boldsymbol{X}_0\boldsymbol{X}_0^T)^{-1}\boldsymbol{X}_0\boldsymbol{y}_0
$$
$$
b_{\mathrm{LS}} = \tilde{\theta} - \frac{1}{p}\mathbf{1}_p^T\boldsymbol{X}^T\boldsymbol{a}_{\mathrm{LS}}
$$
dove:
- $\tilde{\theta} = \frac{1}{p}\sum_i\theta(i)$ è la media dei target
- $\bar{x}_k = \frac{1}{p}\sum_i x_k(i)$ è la media della $k$-esima feature