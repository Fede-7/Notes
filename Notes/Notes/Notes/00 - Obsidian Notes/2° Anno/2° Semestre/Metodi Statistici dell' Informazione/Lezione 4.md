---
date: 2026-03-17
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 4
tags:
  - MSI
  - variabili-aleatorie
  - funzioni-VA
  - valore-atteso
  - varianza
  - deviazione-standard
  - valore-quadratico-medio
  - RMS
  - media-condizionale
  - esercizi
  - Bernoulli
  - geometrica
  - Bayes
Professore: Marco Lops
---

# MSI — Lezione 4: Funzioni di Variabili Aleatorie, Varianza e Esercizi

---

>[!question] Argomenti trattati
> - Ripasso variabili notevoli: Binomiale, Uniforme, Poissoniana, Geometrica
> - PMF condizionata: ripasso e generalizzazione
> - Media condizionale e legge della probabilità totale per le medie
> - Funzioni di variabili aleatorie: $Y = g(X)$
  > 	- Caso biiettivo: reflagging dell'alfabeto
  > 	- Caso molti-a-uno: collasso delle probabilità
> - Teorema fondamentale del calcolo della media: $E[g(X)] = \sum_x g(x) p_X(x)$
> - Valore quadratico medio (RMS) e valore efficace
> - Varianza e deviazione standard
> - Relazione varianza-valore quadratico medio
> - Esercizi: dado truccato (3 dadi), vaccinazione (Binomiale), carte napoletane (non-geometrica)

---

## Ripasso: Variabili Notevoli

| Variabile | Alfabeto | PMF $p_X(k)$ | Media $E[X]$ |
|---|---|---|---|
| Binomiale $\mathcal{B}(n,p)$ | $\{0,\ldots,n\}$ | $\binom{n}{k} p^k (1-p)^{n-k}$ | $np$ |
| Uniforme su $m$ valori | $\{x_1,\ldots,x_m\}$ | $1/m$ | media aritmetica |
| Poissoniana $\mathcal{P}(\lambda)$ | $\mathbb{N}_0$ | $\lambda^k e^{-\lambda} / k!$ | $\lambda$ |
| Geometrica $\mathcal{G}(p)$ | $\{1,2,3,\ldots\}$ | $(1-p)^{k-1} p$ | $1/p$ |

---

## PMF Condizionata: Ripasso e Media Condizionale

### PMF condizionata a un evento

Data una condizione $C$ con $P(C) > 0$:

$$p_{X \mid C}(k) = \frac{P(X=k, C)}{P(C)} = \begin{cases} \dfrac{p_X(k)}{P(C)} & \text{se } k \in C \\ 0 & \text{altrimenti} \end{cases}$$

Questa è ancora una PMF valida. Applicazione in data analysis: **potatura degli outlier** (si escludono valori anomali imponendo una maschera di ammissibilità sul dominio).

### Media condizionale e scomposizione della media

Dato un evento $C$, la **media condizionale** di $X$ dato $C$ è:

$$E[X \mid C] = \sum_{x \in \mathcal{X}} x \cdot p_{X \mid C}(x)$$

Data una partizione $\{E_1, E_2, \ldots, E_m\}$ di $\Omega$ (eventi disgiunti la cui unione è $\Omega$), la media totale si decompone come:

$$\boxed{E[X] = \sum_{i=1}^m P(E_i) \cdot E[X \mid E_i]}$$

**Derivazione:** si applica la legge della probabilità totale alla PMF di $X$, moltiplicando per $x$ e sommando su tutti gli $x$.

> [!example] Esempio con Binomiale $\mathcal{B}(16, 1/3)$
> Partizione: $E_1 = \{X \leq 4\}$, $E_2 = \{X > 4\}$.
>
> $$E[X] = P(X \leq 4) \cdot E[X \mid X \leq 4] + P(X > 4) \cdot E[X \mid X > 4]$$

---

## Funzioni di Variabili Aleatorie: $Y = g(X)$

Se $X$ è una variabile aleatoria e $g$ è una funzione definita sull'alfabeto di $X$, allora $Y = g(X)$ è anch'essa una variabile aleatoria.

### Caso 1: Corrispondenza biiettiva ($|Y| = |X|$)

Se $g$ è una biiezione (ogni valore di $X$ mappa in un valore distinto di $Y$), allora:

$$p_Y(g(x_i)) = p_X(x_i)$$

Si tratta di un semplice **reflagging dell'alfabeto**: le probabilità sono invariate, cambiano solo le etichette dei valori.

> [!example] $Y = 4X$, con $X \in \{-2,-1,1,2\}$ e $p_X = \{1/8, 1/4, 1/4, 3/8\}$
> L'alfabeto di $Y$ è $\{-8,-4,4,8\}$ con le stesse probabilità.

### Caso 2: Corrispondenza molti-a-uno ($|Y| < |X|$)

Più valori di $X$ collassano in uno stesso valore di $Y$. Le probabilità corrispondenti si sommano:

$$p_Y(y_k) = \sum_{\{x : g(x) = y_k\}} p_X(x)$$

> [!example] $Y = |X|$, con $X \in \{-2,-1,1,2\}$
> $Y \in \{1, 2\}$.
> $p_Y(1) = p_X(-1) + p_X(1) = 1/4 + 1/4 = 1/2$
> $p_Y(2) = p_X(-2) + p_X(2) = 1/8 + 3/8 = 1/2$
> Media: $E[Y] = 1 \cdot 1/2 + 2 \cdot 1/2 = 3/2$

---

## Teorema Fondamentale del Calcolo della Media

> [!abstract] Teorema
> Data una variabile aleatoria $X$ con PMF $p_X$ e una funzione $g$, la media di $Y = g(X)$ è:
>
> $$\boxed{E[g(X)] = \sum_{x \in \mathcal{X}} g(x) \cdot p_X(x)}$$
>
> indipendentemente dal fatto che $g$ sia biiettiva o molti-a-uno.

Questo teorema è fondamentale perché permette di calcolare $E[g(X)]$ **senza costruire esplicitamente la PMF di $Y$**: si lavora direttamente con la PMF di $X$.

**Dimostrazione (caso molti-a-uno):** i valori che collassano nello stesso punto di $Y$ hanno tutti lo stesso $g(x)$; la somma su $x$ è quindi equivalente alla somma su $y$ (le probabilità si sommano automaticamente).

---

## Valore Quadratico Medio (RMS)

### Definizione

Il **valore quadratico medio** di $X$ è:

$$E[X^2] = \sum_{x \in \mathcal{X}} x^2 \cdot p_X(x)$$

Il **valore efficace** (root mean square) è:

$$x_{\text{rms}} = \sqrt{E[X^2]}$$

> [!note] Terminologia RMS
> Il termine inglese "root mean square" indica che si prende la **radice** del valor medio del **quadrato**. La notazione $x_{\text{rms}}^2 = E[X^2]$ (il quadrato del valore efficace = valore quadratico medio) può essere fonte di confusione.

> [!example] Corrente alternata e valore efficace
> La corrente sinusoidale ha **media nulla** (le semionde positive e negative si cancellano). La corrente efficace $I_{\text{rms}} = I_0 / \sqrt{2}$ è quella che determina la potenza dissipata: $P = I_{\text{rms}}^2 \cdot R$. Una presa con corrente media zero può essere letale se il valore efficace è diverso da zero.

### Machine Learning: minimizzazione dell'errore quadratico medio

L'errore quadratico medio (MSE) è la funzione costo standard nel ML:

$$\text{MSE} = E\left[(X - \hat{X})^2\right]$$

Vantaggi: è **convessa** (forma a coppa con un unico minimo globale), derivabile e trattabile analiticamente. I problemi di ottimizzazione convessa convergono a soluzioni ottimali globali, a differenza di quelli concavi che hanno massimi unici ma sono usati quando si massimizza una figura di merito.

---

## Varianza e Deviazione Standard

### Definizione

La **variabile centrata** $X - \mu_X$ ha media nulla per costruzione. La sua "dimensione" è misurata dalla **varianza**:

$$\sigma_X^2 = E\left[(X - \mu_X)^2\right] = \sum_{x} (x - \mu_X)^2 \cdot p_X(x) \geq 0$$

La **deviazione standard** è $\sigma_X = \sqrt{\sigma_X^2}$.

### Relazione con il valore quadratico medio

$$\boxed{\sigma_X^2 = E[X^2] - \mu_X^2}$$

**Dimostrazione:**

$$E[(X-\mu_X)^2] = E[X^2 - 2\mu_X X + \mu_X^2] = E[X^2] - 2\mu_X^2 + \mu_X^2 = E[X^2] - \mu_X^2$$

### Interpretazione fisica: media e varianza come coppia

La coppia $(\mu_X, \sigma_X)$ caratterizza globalmente la variabile aleatoria:

- **$\sigma_X \ll \mu_X$:** la variabile è concentrata intorno alla media → la media è un buon predittore
- **$\sigma_X \gg \mu_X$:** la variabile è dispersa → la media non descrive bene il comportamento tipico

Il rapporto $\mu_X / \sigma_X$ (inverso del coefficiente di variazione) misura il "segnale rispetto al rumore" della variabile aleatoria.

> [!example] Confronto
> Sia $X$ una variabile con media 100€ e deviazione standard 1 centesimo: praticamente deterministica, la media descrive la situazione quasi perfettamente. Se invece $\sigma_X = 40€$: alta aleatorietà, la situazione economica "istantanea" può essere molto diversa dalla media.

---

## Esercizi Svolti

### Esercizio 1: Tre Dadi — Probabilità di Ottenere 12

**Setup:** urna con 3 dadi: $D_0$ (onesto), $D_1$ ($P(1)=u$, altri equiprobabili), $D_6$ ($P(6)=u$, altri equiprobabili). Si estraggono **2 dadi** e si lanciano.

Per $D_1$: $P(i\neq 1) = (1-u)/5$. Per $D_6$: $P(i\neq 6) = (1-u)/5$.

Le coppie estratte ($D_0 D_1$, $D_0 D_6$, $D_1 D_6$) sono equiprobabili con prob. $1/3$ ciascuna. Per la legge della probabilità totale:

$$P(12) = \frac{1}{3}\left[\frac{1}{6} \cdot \frac{1-u}{5} + \frac{1}{6} \cdot u + \frac{1-u}{5} \cdot u\right] = \frac{1 + 10u - 6u^2}{90}$$

**Domanda 2:** $P(12) = 2/36 = 1/18$ → risolve $6u^2 - 10u + 4 = 0$ → $u_1 = 1$, $u_2 = 2/3$.

**Domanda 3:** massimizzare $P(12)$. La funzione è concava, il massimo è in $u^* = 10/12 = 5/6$, con $P(12)_{\max} \approx 0{,}0584$.

---

### Esercizio 2: Vaccinazione — Variabile Binomiale $\mathcal{B}(10, 0{,}9)$

10 bambini vaccinati, vaccino efficace nel 90% dei casi, indipendentemente. $X$ = numero di bambini immunizzati.

**a)** Tutti immunizzati:

$$P(X=10) = 0{,}9^{10} \approx 0{,}349$$

**b)** Almeno 8 immunizzati:

$$P(X \geq 8) = \binom{10}{8}(0{,}9)^8(0{,}1)^2 + \binom{10}{9}(0{,}9)^9(0{,}1) + (0{,}9)^{10}$$

**c)** Numero medio: $E[X] = 10 \cdot 0{,}9 = 9$.

---

### Esercizio 3: Carte Napoletane — Distribuzione Non-Standard

**Setup:** mazzo da 40 carte napoletane (10 denari + 30 altre). Due giocatori estraggono **senza reinserire**. Vince chi per primo estrae un denaro. $X$ = numero di estrazioni.

**Alfabeto:** $\mathcal{X} = \{1, 2, \ldots, 31\}$.

> [!warning] Non è una geometrica!
> La geometrica richiede prove indipendenti. Qui le estrazioni sono **dipendenti**: ogni carta estratta riduce il mazzo e cambia le probabilità per le estrazioni successive.

**Calcolo di $P(X = 4)$** con la probabilità composta:

$$P(X=4) = \frac{30}{40} \cdot \frac{29}{39} \cdot \frac{28}{38} \cdot \frac{10}{37}$$

**Chi vince il primo giocatore?** Vince se $X$ è dispari (estrae alle posizioni 1, 3, 5, ...):

$$P(\text{vince il 1° giocatore}) = \sum_{\substack{i \text{ dispari} \\ 1 \leq i \leq 31}} p_X(i)$$
