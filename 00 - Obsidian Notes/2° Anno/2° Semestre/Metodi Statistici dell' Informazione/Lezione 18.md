---
date: 2026-04-30
corso: Metodi Statistici dell'Informazione
docente: Marco Lops
lezione: 18
tags: [MSI, neyman-pearson, laplace, stima-bayesiana, mmse, stima-condizionata]
---

# 🧠 Lezione 18 — Esercizi di Decisione e Introduzione alla Stima Bayesiana (MMSE)

---

## 1. Analisi di Test di Ipotesi Notevoli

### 1.1 Esempio 1: Test di Neyman-Pearson con Variabili Esponenziali
Siano $X_1, \dots, X_n$ osservazioni i.i.d. distribuite secondo leggi esponenziali sotto due ipotesi:
- Under $H_0$: $X_i \sim \text{Exp}(\lambda_0) \implies f(x_i | H_0) = \lambda_0 e^{-\lambda_0 x_i} u(x_i)$
- Under $H_1$: $X_i \sim \text{Exp}(\lambda_1) \implies f(x_i | H_1) = \lambda_1 e^{-\lambda_1 x_i} u(x_i)$
Assumiamo che $\lambda_0 > \lambda_1$ (il che significa che la media sotto $H_1$, pari a $1/\lambda_1$, è maggiore della media sotto $H_0$, pari a $1/\lambda_0$).

#### Calcolo del Rapporto di Verosimiglianza
Le PDF condizionate congiunte sono:
$$f(\mathbf{x}^n | H_j) = \lambda_j^n \exp\left( -\lambda_j \sum_{i=1}^n x_i \right) \quad (\forall x_i \geq 0)$$
Il rapporto di verosimiglianza è:
$$L(\mathbf{x}^n) = \frac{f(\mathbf{x}^n | H_1)}{f(\mathbf{x}^n | H_0)} = \left(\frac{\lambda_1}{\lambda_0}\right)^n \exp\left( (\lambda_0 - \lambda_1) \sum_{i=1}^n x_i \right) \underset{H_0}{\overset{H_1}{\gtrdot}} \eta$$
Prendendo il logaritmo naturale:
$$n \ln\left( \frac{\lambda_1}{\lambda_0} \right) + (\lambda_0 - \lambda_1) \sum_{i=1}^n x_i \underset{H_0}{\overset{H_1}{\gtrdot}} \ln\eta$$
Poiché $\lambda_0 > \lambda_1$, si ha $(\lambda_0 - \lambda_1) > 0$. Risolvendo per la somma delle osservazioni:
$$\sum_{i=1}^n x_i \underset{H_0}{\overset{H_1}{\gtrdot}} \frac{\ln\eta - n\ln(\lambda_1 / \lambda_0)}{\lambda_0 - \lambda_1} = \eta'$$

#### Caso a Singolo Campione ($n=1$)
Il test si riduce a:
$$x \underset{H_0}{\overset{H_1}{\gtrdot}} \eta'$$
Dato il vincolo sulla probabilità di Falso Allarme $P_{FA} = \alpha$, determiniamo la soglia $\eta'$ sotto $H_0$:
$$P(X > \eta' | H_0) = \int_{\eta'}^\infty \lambda_0 e^{-\lambda_0 x} dx = e^{-\lambda_0 \eta'} = \alpha$$
Risolvendo per $\eta'$:
$$\eta' = -\frac{1}{\lambda_0} \ln\alpha$$
La potenza del test $P_D = 1 - \beta$ (probabilità di rivelazione sotto $H_1$) è:
$$P_D = P(X > \eta' | H_1) = \int_{\eta'}^\infty \lambda_1 e^{-\lambda_1 x} dx = e^{-\lambda_1 \eta'}$$
Sostituendo $\eta'$:
$$P_D = e^{-\lambda_1 \left( -\frac{1}{\lambda_0} \ln\alpha \right)} = e^{\frac{\lambda_1}{\lambda_0} \ln\alpha} = \alpha^{\frac{\lambda_1}{\lambda_0}}$$

> [!green] Considerazione sulla Potenza
> Essendo $\lambda_1 < \lambda_0$, l'esponente $\frac{\lambda_1}{\lambda_0}$ è strettamente minore di $1$. Per piccoli valori di Falso Allarme $\alpha$ (es. $10^{-3}$), la potenza del test risulta significativamente superiore al valore del falso allarme (es. se $\lambda_1/\lambda_0 = 0.5$, allora $P_D = \sqrt{0.001} \approx 0.0316 \gg 0.001$).

---

### 1.2 Esempio 2: Rumore Laplaciano e Transizione della Decisione
Consideriamo un singolo campione osservato $Z$.
- Under $H_0$: $Z = N$, dove $N$ è un rumore laplaciano a media nulla.
  $$f_Z(z | H_0) = \frac{1}{2} e^{-|z|}$$
- Under $H_1$: $Z = N + 4$, ovvero c'è un segnale costante aggiunto pari a 4.
  $$f_Z(z | H_1) = \frac{1}{2} e^{-|z-4|}$$

#### Rapporto di Verosimiglianza Logaritmico
$$\Lambda(z) = \ln\left( \frac{f_Z(z | H_1)}{f_Z(z | H_0)} \right) = |z| - |z-4|$$

Analizziamo l'andamento della funzione $\Lambda(z)$ suddividendo l'asse reale in tre regioni:
1. Per $z < 0$:
   $$|z| = -z, \quad |z-4| = -(z-4) = 4-z \implies \Lambda(z) = -z - (4-z) = -4$$
2. Per $z > 4$:
   $$|z| = z, \quad |z-4| = z-4 \implies \Lambda(z) = z - (z-4) = 4$$
3. Per $0 \leq z \leq 4$:
   $$|z| = z, \quad |z-4| = 4-z \implies \Lambda(z) = z - (4-z) = 2z-4$$

Rappresentazione analitica della statistica di test $\Lambda(z)$:
$$\Lambda(z) = \begin{cases} -4 & z < 0 \\ 2z-4 & 0 \leq z \leq 4 \\ 4 & z > 4 \end{cases}$$

```
   Λ(z) ^
      4 |          _________ (z > 4)
        |         /
        |        /
      0 |-------/--------> z
        |      / 2
     -4 |_____/ (z < 0)
```

La decisione ottima Bayesiana confronta $\Lambda(z)$ con la soglia $\eta = \ln\left( \frac{\pi_0}{\pi_1} \right)$.

#### Analisi dei Regimi della Soglia
- **Soglia Elevata ($\eta > 4$)**:
  Poiché il valore massimo di $\Lambda(z)$ è $4$, se la soglia $\eta$ è maggiore di $4$, la condizione $\Lambda(z) > \eta$ non può mai essere soddisfatta. Decideremo **sempre $H_0$**.
  Ciò si verifica quando:
  $$\ln\left(\frac{\pi_0}{\pi_1}\right) > 4 \implies \frac{1-\pi_1}{\pi_1} > e^4 \implies \pi_1 < \frac{1}{1+e^4} \approx 0.018$$
  > [!warning] Trappola da evitare
  > Se la probabilità a priori del segnale è estremamente bassa ($\pi_1 < 1.8\%$), il sistema rigetterà sempre la presenza del segnale, ritenendo qualsiasi osservazione (anche superiore a 4) come una fluttuazione anomala del rumore laplaciano sotto $H_0$.

- **Ipotesi Equiprobabili ($\pi_0 = \pi_1 = 1/2 \implies \eta = 0$)**:
  Il test si riduce a:
  $$\Lambda(z) \underset{H_0}{\overset{H_1}{\gtrdot}} 0 \implies 2z-4 \underset{H_0}{\overset{H_1}{\gtrdot}} 0 \implies z \underset{H_0}{\overset{H_1}{\gtrdot}} 2$$
  La soglia ottima è il punto medio geometrico $z = 2$.

- **Caso di Soglia Asimmetrica ($z_{soglia} = 1$)**:
  Se volessimo impostare la soglia di decisione a $z = 1$, all'interno dell'intervallo lineare $[0,4]$:
  $$\Lambda(z) > \eta \implies 2z-4 > \eta \implies z > \frac{\eta+4}{2}$$
  Uguagliando la soglia a $1$:
  $$\frac{\eta+4}{2} = 1 \implies \eta = -2 \implies \ln\left( \frac{\pi_0}{1-\pi_0} \right) = -2 \implies \pi_0 = \frac{1}{1+e^2} \approx 0.12$$
  Dunque, la soglia ottima si sposta a $z = 1$ solo se la probabilità a priori dello stato di quiete $H_0$ è molto bassa ($\approx 12\%$), rendendo a priori molto probabile lo stato di perturbazione $H_1$.

---

## 2. Introduzione alla Teoria della Stima Bayesiana

> [!abstract] Essenza
> Nella **stima parametrica**, lo stato della natura è descritto da una variabile continua $\theta \in \Theta$.
> L'obiettivo è costruire una funzione delle sole osservazioni, detta **stimatore** $\hat{\theta}(\mathbf{x}^n)$, che approssimi il valore reale di $\theta$.

Nell'**approccio Bayesiano**, il parametro ignoto $\theta$ è modellato come una **variabile aleatoria continua** dotata di una densità di probabilità a priori nota $f_\theta(\theta)$.

### 2.1 Teorema di Bayes e Densità A Posteriori
Dato il vettore di osservazioni $\mathbf{x}^n$, la verosimiglianza dei dati è descritta dalla PDF condizionata $f(\mathbf{x}^n | \theta)$.
La densità di probabilità a posteriori del parametro $\theta$ date le osservazioni è:
$$f(\theta | \mathbf{x}^n) = \frac{f(\mathbf{x}^n | \theta) f_\theta(\theta)}{f(\mathbf{x}^n)} = \frac{f(\mathbf{x}^n | \theta) f_\theta(\theta)}{\int_{-\infty}^\infty f(\mathbf{x}^n | \theta) f_\theta(\theta) d\theta}$$

---

### 2.2 Stimatore MMSE (Minimum Mean Square Error)

Lo stimatore a minimo errore quadratico medio (MMSE) punta a minimizzare il **Rischio Medio Bayesiano** calcolato rispetto a una funzione di costo quadratica:
$$C(\theta - \hat{\theta}) = (\theta - \hat{\theta})^2 \implies R_B = E[(\theta - \hat{\theta}(\mathbf{X}^n))^2]$$

#### Derivazione dell'Ottimalità dello Stimatore MMSE
Esprimiamo il valore atteso sdoppiandolo mediante la proprietà del valore atteso condizionato:
$$E[(\theta - \hat{\theta}(\mathbf{X}^n))^2] = E_{\mathbf{X}}\left[ E_{\theta | \mathbf{X}}\left[ (\theta - \hat{\theta}(\mathbf{X}^n))^2 \Big| \mathbf{X}^n \right] \right]$$
Poiché la PDF esterna $f(\mathbf{x}^n)$ è non-negativa, per minimizzare l'intero valore atteso è sufficiente minimizzare l'integrale interno (rispetto a $\theta$) per ogni singola realizzazione osservata $\mathbf{x}^n$:
$$g(\hat{\theta}) = E_{\theta | \mathbf{X}} [(\theta - \hat{\theta})^2 | \mathbf{x}^n] = E[\theta^2 | \mathbf{x}^n] - 2\hat{\theta} E[\theta | \mathbf{x}^n] + \hat{\theta}^2$$
Derivando la funzione rispetto alla decisione $\hat{\theta}$ e ponendo la derivata pari a zero:
$$\frac{d g(\hat{\theta})}{d\hat{\theta}} = -2 E[\theta | \mathbf{x}^n] + 2\hat{\theta} = 0 \implies \hat{\theta}_{MMSE}(\mathbf{x}^n) = E[\theta | \mathbf{X}^n = \mathbf{x}^n]$$

> [!important] Teorema Fondamentale
> Lo stimatore a minimo errore quadratico medio (MMSE) coincide sempre con la **media condizionata** della distribuzione a posteriori del parametro date le osservazioni.
> Geometricamente rappresenta la proiezione ortogonale (regressione) di $\theta$ sullo spazio generato dalle osservazioni.