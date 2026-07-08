---
date: 2026-04-29
corso: Metodi Statistici dell'Informazione
docente: Marco Lops
lezione: 17
tags: [MSI, test-ipotesi, gaussiana, poisson, neyman-pearson, statistica-sufficiente]
---

# 🧠 Lezione 17 — Test Continuo, Statistiche Sufficienti e Criterio di Neyman-Pearson

---

## 1. Estensione del Test di Ipotesi al Caso Continuo

> [!abstract] Essenza
> Nel caso continuo, le sommatorie della probabilità di decisione corretta si trasformano in integrali multivariati sullo spazio delle osservazioni $\mathbb{R}^n$.
> La probabilità di decisione corretta $P_c$ con $M$ ipotesi è:
> $$P_c = \sum_{i=1}^M \pi_i \int_{\Omega_i} f(\mathbf{x}^n | H_i) d\mathbf{x}^n$$
> Per massimizzare $P_c$ (riducendo al minimo la probabilità di errore $P_e$), ciascun vettore osservato $\mathbf{x}^n$ deve essere assegnato alla regione $\Omega_k$ in cui l'integrando $\pi_k f(\mathbf{x}^n | H_k)$ è massimo. 

La regola Bayesiana a minima probabilità di errore (MAP) per osservabili continui diventa:
$$\text{Decidi } H_k \iff k = \arg\max_{i} \pi_i f(\mathbf{x}^n | H_i)$$

Se le ipotesi sono a priori equiprobabili ($\pi_i = 1/M$), la regola si riduce alla massimizzazione della densità di verosimiglianza (Maximum Likelihood):
$$\text{Decidi } H_k \iff k = \arg\max_{i} f(\mathbf{x}^n | H_i)$$

---

## 2. Esempi Notevoli di Test di Ipotesi I.I.D. (Caso Binario)

### 2.1 Esempio 1: Test sulla Media di Gaussiane I.I.D. con Varianza Nota
Consideriamo osservazioni gaussiane i.i.d. sotto due ipotesi equiprobabili ($\pi_1 = \pi_2 = 1/2$):
- $H_1: X_i \sim \mathcal{N}(\mu_1, \sigma^2)$
- $H_2: X_i \sim \mathcal{N}(\mu_2, \sigma^2)$
Assumiamo $\mu_1 > \mu_2$.

#### Derivazione della Regola di Decisione (LRT)
Le PDF condizionate congiunte sono:
$$f(\mathbf{x}^n | H_j) = \left( \frac{1}{\sqrt{2\pi\sigma^2}} \right)^n \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu_j)^2 \right)$$

Il rapporto di verosimiglianza (Likelihood Ratio Test) impone:
$$\frac{f(\mathbf{x}^n | H_1)}{f(\mathbf{x}^n | H_2)} \underset{H_2}{\overset{H_1}{\gtrdot}} 1$$
Prendendo il logaritmo naturale:
$$\ln\left( \frac{f(\mathbf{x}^n | H_1)}{f(\mathbf{x}^n | H_2)} \right) = -\frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu_1)^2 + \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu_2)^2 \underset{H_2}{\overset{H_1}{\gtrdot}} 0$$
Espandendo i quadrati all'interno delle sommatorie:
$$\sum_{i=1}^n (x_i - \mu_1)^2 = \sum_{i=1}^n x_i^2 - 2\mu_1 \sum_{i=1}^n x_i + n\mu_1^2$$
$$\sum_{i=1}^n (x_i - \mu_2)^2 = \sum_{i=1}^n x_i^2 - 2\mu_2 \sum_{i=1}^n x_i + n\mu_2^2$$

Sostituendo e semplificando il termine comune $\sum x_i^2$:
$$\frac{1}{2\sigma^2} \left[ 2(\mu_1 - \mu_2) \sum_{i=1}^n x_i - n(\mu_1^2 - \mu_2^2) \right] \underset{H_2}{\overset{H_1}{\gtrdot}} 0$$
Moltiplicando per $\frac{2\sigma^2}{n}$:
$$\frac{2(\mu_1 - \mu_2)}{n} \sum_{i=1}^n x_i - (\mu_1^2 - \mu_2^2) \underset{H_2}{\overset{H_1}{\gtrdot}} 0$$
Sapendo che $\mu_1^2 - \mu_2^2 = (\mu_1 - \mu_2)(\mu_1 + \mu_2)$ e che per ipotesi $\mu_1 > \mu_2$ (dunque $\mu_1 - \mu_2 > 0$), possiamo dividere per $2(\mu_1 - \mu_2)$ isolando la media campionaria $\bar{X}_n$:
$$\bar{X}_n = \frac{1}{n} \sum_{i=1}^n x_i \underset{H_2}{\overset{H_1}{\gtrdot}} \frac{\mu_1 + \mu_2}{2}$$

> [!important] Concetto di Statistica Sufficiente
> Non è necessario conoscere ogni singola componente del vettore $\mathbf{x}^n$ per decidere in modo ottimo. Tutta l'informazione rilevante per il test è racchiusa nella sola **media campionaria $\bar{X}_n$**. Qualsiasi altra statistica (es. varianza campionaria o i singoli ordinamenti dei dati) rappresenta rumore irrilevante ai fini della decisione.

#### Calcolo della Probabilità di Errore ($Pe$)
La statistica sufficiente $\bar{X}_n$ è una combinazione lineare di gaussiane indipendenti, quindi è anch'essa gaussiana:
- Sotto $H_1$: $\bar{X}_n \sim \mathcal{N}\left(\mu_1, \frac{\sigma^2}{n}\right)$
- Sotto $H_2$: $\bar{X}_n \sim \mathcal{N}\left(\mu_2, \frac{\sigma^2}{n}\right)$

Dato che la soglia ottima è $\eta = \frac{\mu_1 + \mu_2}{2}$, l'errore sotto $H_1$ (decidere $H_2$) è:
$$P(d(\mathbf{X}^n)=2 | H_1) = P\left( \bar{X}_n < \frac{\mu_1 + \mu_2}{2} \Big| H_1 \right)$$
Normalizzando la variabile ponendo $Z = \frac{\bar{X}_n - \mu_1}{\sigma / \sqrt{n}} \sim \mathcal{N}(0,1)$:
$$P\left( Z < \frac{\frac{\mu_1 + \mu_2}{2} - \mu_1}{\sigma / \sqrt{n}} \right) = P\left( Z < -\frac{\mu_1 - \mu_2}{2\sigma / \sqrt{n}} \right) = \Phi\left( -\frac{\sqrt{n}(\mu_1 - \mu_2)}{2\sigma} \right) = Q\left( \frac{\sqrt{n}(\mu_1 - \mu_2)}{2\sigma} \right)$$
dove $Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^\infty e^{-t^2/2} dt$ è la funzione Q-Gaussiana.
Per simmetria, $P(d(\mathbf{X}^n)=1 | H_2)$ fornisce lo stesso risultato. Essendo le ipotesi equiprobabili:
$$P_e = Q\left( \frac{\sqrt{n}(\mu_1 - \mu_2)}{2\sigma} \right)$$

> [!green] Dinamica dell'Errore
> All'aumentare del numero di campioni $n$, la probabilità di errore decresce in modo **esponenziale**. Ciò è coerente con la legge dei grandi numeri: la varianza della media campionaria collassa a zero, separando nettamente le distribuzioni delle due ipotesi.

---

### 2.2 Esempio 2: Test su Variabili di Poisson I.I.D.
- $H_1: X_i \sim \text{Poisson}(\lambda_1)$
- $H_2: X_i \sim \text{Poisson}(\lambda_2)$
Assumiamo $\lambda_1 > \lambda_2$ e ipotesi equiprobabili ($\pi_1 = \pi_2 = 1/2$).

#### Derivazione del Test
La PMF di una singola osservazione poissoniana è:
$$P(X_i = x_i | H_j) = \frac{\lambda_j^{x_i}}{x_i!} e^{-\lambda_j}$$
La PMF congiunta di $n$ campioni indipendenti è:
$$P(\mathbf{x}^n | H_j) = \prod_{i=1}^n \frac{\lambda_j^{x_i}}{x_i!} e^{-\lambda_j} = e^{-n\lambda_j} \frac{\lambda_j^{\sum x_i}}{\prod x_i!}$$
Il rapporto di verosimiglianza ML esclude i denominatori comuni $\prod x_i!$:
$$\frac{e^{-n\lambda_1} \lambda_1^{\sum x_i}}{e^{-n\lambda_2} \lambda_2^{\sum x_i}} \underset{H_2}{\overset{H_1}{\gtrdot}} 1$$
Prendendo il logaritmo naturale:
$$-n(\lambda_1 - \lambda_2) + \left(\sum_{i=1}^n x_i\right) \ln\left( \frac{\lambda_1}{\lambda_2} \right) \underset{H_2}{\overset{H_1}{\gtrdot}} 0$$
Essendo $\lambda_1 > \lambda_2$, abbiamo $\ln(\lambda_1 / \lambda_2) > 0$. Dividendo:
$$\bar{X}_n = \frac{1}{n} \sum_{i=1}^n x_i \underset{H_2}{\overset{H_1}{\gtrdot}} \frac{\lambda_1 - \lambda_2}{\ln(\lambda_1 / \lambda_2)}$$

#### Somma di Poissoniane Indipendenti
> [!green] Teorema
> Se $X_1 \sim \text{Poisson}(\lambda_1)$ e $X_2 \sim \text{Poisson}(\lambda_2)$ sono indipendenti, la loro somma $Z = X_1 + X_2$ è poissoniana con parametro $\lambda_1 + \lambda_2$.
> 
> *Dimostrazione:*
> $$P(Z = m) = \sum_{l=0}^m P(X_1 = m-l) P(X_2 = l) = \sum_{l=0}^m \frac{\lambda_1^{m-l}}{(m-l)!} e^{-\lambda_1} \frac{\lambda_2^l}{l!} e^{-\lambda_2}$$
> Moltiplicando e dividendo per $m!$:
> $$P(Z = m) = \frac{e^{-(\lambda_1+\lambda_2)}}{m!} \sum_{l=0}^m \frac{m!}{l!(m-l)!} \lambda_2^l \lambda_1^{m-l} = \frac{(\lambda_1 + \lambda_2)^m}{m!} e^{-(\lambda_1+\lambda_2)}$$

Pertanto, la somma totale $Y = \sum_{i=1}^n X_i$ è distribuita come:
- Sotto $H_1$: $Y \sim \text{Poisson}(n\lambda_1)$
- Sotto $H_2$: $Y \sim \text{Poisson}(n\lambda_2)$

Definendo la soglia intera per la somma come $K_{soglia} = \left\lfloor n \frac{\lambda_1 - \lambda_2}{\ln(\lambda_1 / \lambda_2)} \right\rfloor$, la probabilità di errore è:
$$P_e = \frac{1}{2} \sum_{k=0}^{K_{soglia}} \frac{(n\lambda_1)^k}{k!} e^{-n\lambda_1} + \frac{1}{2} \sum_{k=K_{soglia}+1}^\infty \frac{(n\lambda_2)^k}{k!} e^{-n\lambda_2}$$

---

### 2.3 Esempio 3: Test sulla Varianza di Gaussiane a Media Nulla
- $H_1: X_i \sim \mathcal{N}(0, \sigma_1^2)$
- $H_2: X_i \sim \mathcal{N}(0, \sigma_2^2)$
Assumiamo $\sigma_1^2 > \sigma_2^2$ e ipotesi equiprobabili.

Le verosimiglianze sono:
$$f(\mathbf{x}^n | H_j) = \left( \frac{1}{\sqrt{2\pi\sigma_j^2}} \right)^n \exp\left( -\frac{1}{2\sigma_j^2} \sum_{i=1}^n x_i^2 \right)$$
Applicando il log-LRT:
$$-n\ln(\sigma_1) - \frac{1}{2\sigma_1^2} \sum_{i=1}^n x_i^2 \underset{H_2}{\overset{H_1}{\gtrdot}} -n\ln(\sigma_2) - \frac{1}{2\sigma_2^2} \sum_{i=1}^n x_i^2$$
Isolando la somma dei quadrati:
$$\left( \frac{1}{2\sigma_2^2} - \frac{1}{2\sigma_1^2} \right) \sum_{i=1}^n x_i^2 \underset{H_2}{\overset{H_1}{\gtrdot}} n \ln\left( \frac{\sigma_1}{\sigma_2} \right)$$
Essendo $\sigma_1 > \sigma_2$, la parentesi a sinistra è strettamente positiva. Dividendo per essa e per $n$:
$$\frac{1}{n}\sum_{i=1}^n x_i^2 \underset{H_2}{\overset{H_1}{\gtrdot}} \frac{2\ln(\sigma_1 / \sigma_2)}{\frac{1}{\sigma_2^2} - \frac{1}{\sigma_1^2}}$$

> [!info] Interpretazione
> La statistica sufficiente è il **momento secondo campionario** $\frac{1}{n}\sum X_i^2$. La sua distribuzione sotto le due ipotesi è una riscalatura di una variabile aleatoria Chi-Quadro ($\chi^2$) con $n$ gradi di libertà.

---

## 3. Il Criterio di Neyman-Pearson

> [!abstract] Contesto
> Nei casi reali (es. radar militare o rilevamento epidemie), spesso **non conosciamo le probabilità a priori delle ipotesi** $\pi_j$ né disponiamo di una **matrice dei costi definita**.
> In tali scenari si introduce l'ipotesi nulla $H_0$ ("stato di quiete/assenza di segnale") e l'ipotesi alternativa $H_1$ ("anomalia/presenza di segnale").

### 3.1 Classificazione degli Errori
Assegnando lo spazio campionario alle regioni $\Omega_0$ (si decide per $H_0$) e $\Omega_1$ (si decide per $H_1$):
- **Errore di I Specie (Falso Allarme)**: decidere $H_1$ quando è vera $H_0$.
  $$P_{FA} = \alpha = \int_{\Omega_1} f(\mathbf{x}^n | H_0) d\mathbf{x}^n$$
- **Errore di II Specie (Mancata Rivelazione / Miss)**: decidere $H_0$ quando è vera $H_1$.
  $$P_{M} = \beta = \int_{\Omega_0} f(\mathbf{x}^n | H_1) d\mathbf{x}^n$$
- **Potenza del Test (Probabilità di Rivelazione / Detection)**: decidere $H_1$ quando è vera $H_1$.
  $$P_D = 1 - \beta = \int_{\Omega_1} f(\mathbf{x}^n | H_1) d\mathbf{x}^n$$

> [!danger] Trappola da evitare
> Non è possibile minimizzare contemporaneamente sia $\alpha$ che $\beta$. Ad esempio, decidendo sempre $H_1$ si ottiene $\beta = 0$ (massima potenza $P_D = 1$) ma al costo di generare un falso allarme costante $\alpha = 1$.

### 3.2 Formulazione del Criterio
Il criterio di Neyman-Pearson risolve questo trade-off vincolando la probabilità di falso allarme a non superare un livello di significatività massimo tollerabile $\alpha_0$, e massimizzando la potenza del test sotto tale vincolo:
$$\max_{\Omega_1} P_D \quad \text{s.t.} \quad P_{FA} \leq \alpha_0$$

### 3.3 Il Lemma di Neyman-Pearson
> [!important] Teorema
> Il test che massimizza la probabilità di rivelazione $P_D$ sotto il vincolo $P_{FA} \leq \alpha_0$ è il **Rapporto di Verosimiglianza (LRT)**:
> $$L(\mathbf{x}^n) = \frac{f(\mathbf{x}^n | H_1)}{f(\mathbf{x}^n | H_0)} \underset{H_0}{\overset{H_1}{\gtrdot}} \eta$$
> dove la soglia $\eta$ deve essere scelta in modo da soddisfare strettamente l'uguaglianza sul bordo del vincolo:
> $$P(L(\mathbf{X}^n) > \eta | H_0) = \alpha_0$$