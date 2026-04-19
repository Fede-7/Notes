---
date: 2026-03-24
corso: Modelli Statistici e Probabilità
docente: N/D
lezione: PMF congiunta, variabili aleatorie multiple e indipendenza
tags:
  - PMF-congiunta
  - variabili-multiple
  - indipendenza
  - marginalizzazione
  - MSI
---
>[!question] Argomenti trattati
>- Riepilogo: caratterizzazione di una singola variabile aleatoria
>- Coppia di variabili aleatorie: definizione e PMF congiunta
>- Proprietà di marginalizzazione
>- Indipendenza statistica tra variabili aleatorie
>- Estensione a terne e n-uple di variabili aleatorie
>- PMF condizionale per coppie
>- Esempio: terne di bit (sorgente senza memoria vs. bit di parità)

---

## Riepilogo: singola variabile aleatoria

Una singola variabile aleatoria discreta $X$ è completamente caratterizzata dalla sua **PMF** (Probability Mass Function) $p_X(x)$, che assegna a ogni valore $x$ dell'alfabeto la probabilità $P(X = x)$.

Dalla PMF si derivano:

- **Media** (valore atteso): $E[X] = \sum_x x \cdot p_X(x)$
- **Teorema fondamentale per il calcolo della media**: $E[g(X)] = \sum_x g(x) \cdot p_X(x)$
- **Momenti**: $E[X^m]$ (momento di ordine $m$), $E[(X-E[X])^m]$ (momento centrale)
- **Varianza**: $\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$
- **Disuguaglianza di Chebyshev**: $P(|X - E[X]| \geq k\sigma) \leq \frac{1}{k^2}$, dove $\sigma$ è la deviazione standard

---


## Trasformazione di Densità (Introdotto dopo)

Questa sezione introduce il concetto cruciale per passare a variabili aleatorie continue. Se $X$ è una variabile aleatoria continua con densità $f_X(x)$ e $Y = g(X)$ dove $g$ è una trasformazione monotona e differenziabile, la densità di $Y$ si calcola come segue:

Se $g$ è **strettamente monotona** (crescente o decrescente), esiste una funzione inversa unica $x = g^{-1}(y)$. Per la regola della catena nel calcolo delle probabilità:

> [!abstract] Teorema Fondamentale della Trasformazione di Densità
> $$\boxed{f_Y(y) = f_X(g^{-1}(y)) \cdot \left|\frac{d}{dy} g^{-1}(y)\right| = \frac{f_X(x)}{|g'(x)|} \bigg|_{x = g^{-1}(y)}}$$
>
> dove il termine $|g'(x)|^{-1}$ è il **fattore jacobiano** che tiene conto della dilatazione/compressione della trasformazione.

**Intuizione:** quando $g$ dilata lo spazio (aumenta le distanze), la concentrazione di probabilità diminuisce, quindi la densità deve diminuire. Il fattore jacobiano compensa questa variazione.

> [!example] Trasformazione $Y = aX + b$
> Se $X \sim \mathcal{N}(\mu, \sigma^2)$ e $Y = aX + b$ con $a > 0$:
> $$x = \frac{y - b}{a}, \quad \frac{dx}{dy} = \frac{1}{a}$$
> $$f_Y(y) = f_X\left(\frac{y-b}{a}\right) \cdot \frac{1}{|a|} = \frac{1}{\sigma\sqrt{2\pi}|a|} \exp\left(-\frac{1}{2\sigma^2}\left(\frac{y-b}{a} - \mu\right)^2\right)$$
> che si riconosce come una gaussiana con media $a\mu + b$ e deviazione standard $|a|\sigma$.

---

## Entropia di Shannon (Introdotto dopo)

### Informazione contenuta in un evento

L'**entropia** è un concetto fondamentale nella teoria dell'informazione, introdotto da Claude Shannon nel 1948. Misura il grado di **incertezza** o **contenuto informativo** di una fonte di dati.

Dato un evento $A$ di probabilità $P(A)$, la quantità di informazione ricevuta dal verificarsi di $A$ è misurata dalla funzione:

$$I(A) = \log_2 \frac{1}{P(A)} = -\log_2 P(A)$$

Questa funzione soddisfa tre proprietà naturali:

1. **Non negativa**: $I(A) \geq 0$ (evento impossibile o certo raramente porta informazione).
2. **Decrescente nella probabilità**: più rare l'evento, più informazione contiene. Un evento frequente ("il Sole sorgerà domani") porta poca informazione.
3. **Additiva per eventi indipendenti**: $I(A \cap B) = I(A) + I(B)$ se $A$ e $B$ sono indipendenti.

La base 2 del logaritmo rende l'unità di misura il **bit** (binary digit): un evento certo e uno impossibile corrispondono rispettivamente a 0 e $+\infty$ bit.

> [!example] Esempi interpretativi
> - Evento certo ($P(A) = 1$): $I(A) = -\log_2 1 = 0$ bit (informazione nulla: non apprendiamo nulla di nuovo).
> - Moneta equilibrata ($P(A) = 1/2$): $I(A) = -\log_2(1/2) = 1$ bit (informazione massima per un evento binario).
> - Evento molto raro ($P(A) = 1/1024 = 2^{-10}$): $I(A) = 10$ bit (informazione molto alta).

### Entropia di una variabile aleatoria discreta

Poiché $I(X=x) = -\log_2 p_X(x)$ è essa stessa una variabile aleatoria (dipende dal valore assunto da $X$), l'**entropia** è definita come la sua **media statistica**:

> [!abstract] Definizione: Entropia di Shannon
> L'entropia di una variabile aleatoria discreta $X$ con PMF $p_X(x)$ è:
> $$\boxed{H(X) = -\sum_{x \in \mathcal{X}} p_X(x) \log_2 p_X(x)}$$
> Alternativamente: $H(X) = E\left[-\log_2 p_X(X)\right]$.
> Si misura in **bit** (con logaritmo in base 2).

L'entropia risponde alla domanda: **quanti bit in media** serve trasferire (o memorizzare) per codificare il valore di $X$?

**Proprietà fundamentali:**

- **Non negativa**: $H(X) \geq 0$, con $H(X) = 0$ se e solo se $X$ è deterministica (assume un valore con probabilità 1).
- **Massimizzata dall'uniforme**: data un alfabeto di cardinalità $n$, l'entropia è massima quando $p_X(x) = 1/n$ per ogni $x$, e vale $H_{\max} = \log_2 n$.
- **Sotto-additività per variabili indipendenti**: $H(X, Y) \leq H(X) + H(Y)$, con uguaglianza se $X$ e $Y$ sono indipendenti.

### Entropia di variabili comuni

| Variabile | Alfabeto | PMF | Entropia massima |
|---|---|---|---|
| Bernoulliana | $\{0, 1\}$ | $p, 1-p$ | $H_{\max} = 1$ bit a $p = 1/2$ |
| Uniforme su $n$ valori | $\{1, \ldots, n\}$ | $1/n$ | $H_{\max} = \log_2 n$ bit |
| Poissoniana $\mathcal{P}(\lambda)$ | $\mathbb{N}_0$ | $\lambda^k e^{-\lambda}/k!$ | Infinito (alfabeto infinito) |

> [!example] Entropia di una Bernoulliana
> Per $X \in \{0, 1\}$ con $P(X=1) = p$:
> $$H(X) = -p \log_2 p - (1-p) \log_2(1-p)$$
> A $p = 1/2$ (equiprobabile): $H(1/2, 1/2) = -\frac{1}{2} \log_2(1/2) - \frac{1}{2} \log_2(1/2) = 1$ bit.
> A $p = 0.9$ (molto asimmetrica): $H(0.9, 0.1) \approx 0.47$ bit.
> A $p = 1$ (deterministica): $H(1, 0) = 0$ bit.

### Implicazione nella compressione di dati

Un **file compresso ideale** è una sequenza binaria in cui ogni bit è ugualmente probabile di essere 0 o 1 (**equiprobabile**) e i bit sono statisticamente indipendenti. In questo caso, ogni bit trasferisce 1 bit di informazione nel senso di Shannon, e non è possibile comprimere ulteriormente.

Se il file ha caratteri con frequenze diverse (es. lettera 'e' più frequente), l'entropia è inferiore a 1 bit per carattere, e **la compressione (es. Huffman coding) può ridurre la media di bit utilizzati**.

---



### Motivazione

In molte applicazioni si osservano più grandezze contemporaneamente sullo stesso esperimento. Per esempio, su un database di persone, ogni estrazione casuale restituisce sia l'altezza $X$ che il peso $Y$: si ha un'**applicazione dallo spazio dei campioni a una coppia ordinata** $(X(\omega), Y(\omega))$.

> [!abstract] Definizione: Coppia di variabili aleatorie
> Dato uno spazio di probabilità $(\Omega, \mathcal{F}, P)$, una **coppia di variabili aleatorie** $(X, Y)$ è un'applicazione:
> $$\omega \mapsto (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y}$$
> dove $\mathcal{X}$ e $\mathcal{Y}$ sono gli alfabeti (insiemi di valori possibili) di $X$ e $Y$ rispettivamente.

### PMF congiunta

> [!abstract] Definizione: PMF congiunta
> La **PMF congiunta** di $(X, Y)$ è la tabella:
> $$p_{XY}(x, y) = P(X = x, Y = y), \quad \forall x \in \mathcal{X}, y \in \mathcal{Y}$$
> Questa tabella ha $|\mathcal{X}| \times |\mathcal{Y}|$ entrate, tutte non negative, la cui somma è 1:
> $$\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p_{XY}(x, y) = 1$$

> [!example] Esempio: due variabili binarie
> $X_1, X_2 \in \{0, 1\}$. La tabella seguente è una PMF congiunta valida:
>
> |  | $X_2=0$ | $X_2=1$ |
> |---|---|---|
> | $X_1=0$ | $1/4$ | $1/8$ |
> | $X_1=1$ | $1/8$ | $1/2$ |
>
> Verifica: $1/4 + 1/8 + 1/8 + 1/2 = 1$. ✓

---

## Marginalizzazione

Dalla PMF congiunta si ricavano le PMF delle singole variabili, dette **PMF marginali**:

$$p_X(x) = \sum_{y \in \mathcal{Y}} p_{XY}(x, y), \qquad p_Y(y) = \sum_{x \in \mathcal{X}} p_{XY}(x, y)$$

**Dimostrazione**: L'evento $\{X = x\}$ è l'unione disgiunta degli eventi $\{X = x, Y = y\}$ al variare di $y$. Per l'assioma di additività di Kolmogorov: $P(X=x) = \sum_y P(X=x, Y=y)$.

> [!info] Asimmetria congiunta ↔ marginali
> - Congiunta **implica** marginali: data la PMF congiunta, le marginali sono univocamente determinate (per somma).
> - Marginali **non implicano** congiunta: date le due PMF marginali, esistono in generale molte congiunte compatibili con esse.
>
> L'unica eccezione è il caso di indipendenza statistica (vedi §4).

---

## Indipendenza statistica

> [!abstract] Definizione: Indipendenza statistica
> Due variabili aleatorie $X$ e $Y$ sono **statisticamente indipendenti** se e solo se la loro PMF congiunta si fattorizza nel prodotto delle marginali:
> $$p_{XY}(x, y) = p_X(x) \cdot p_Y(y), \quad \forall x \in \mathcal{X}, y \in \mathcal{Y}$$
> Equivalentemente: conoscere il valore assunto da $X$ non modifica la distribuzione di probabilità di $Y$ e viceversa.

> [!example] Altezza e peso: variabili dipendenti
> Altezza e peso non sono indipendenti: se so che una persona è alta 1,70 m, la distribuzione del peso condizionata è diversa dalla distribuzione marginale del peso. La probabilità congiunta che una persona sia alta 1,70 m **e** pesi 40 kg non è il prodotto delle probabilità marginali.

> [!example] Verifica sull'esempio binario
> Dalle marginali: $p_{X_1}(0) = 1/4 + 1/8 = 3/8$, $p_{X_2}(0) = 1/4 + 1/8 = 3/8$.
>
> Se fossero indipendenti: $p_{X_1 X_2}(0,0) = 3/8 \cdot 3/8 = 9/64 \neq 1/4$.
>
> Quindi $X_1$ e $X_2$ non sono indipendenti in questo esempio.

---

## PMF condizionale

> [!abstract] Definizione: PMF condizionale
> La **PMF condizionale di $X$ dato $Y$** è:
> $$p_{X|Y}(x|y) = P(X=x \mid Y=y) = \frac{p_{XY}(x,y)}{p_Y(y)}, \quad \text{per ogni } y \text{ con } p_Y(y) > 0$$

**Proprietà**: Per ogni $y$ fissato, $\sum_{x \in \mathcal{X}} p_{X|Y}(x|y) = 1$ (è una legge di probabilità). La somma su tutti i valori di $y$ non è necessariamente 1.

> [!warning] Organizzazione della tabella condizionale
> Nella tabella $p_{X|Y}(x|y)$: la **somma per colonne** (condizionamento fisso) fa 1. La **somma per righe** (condizionamento varia) non fa 1.

> [!example] PMF condizionale sull'esempio binario
> $p_{X_2}(0) = 3/8$, $p_{X_2}(1) = 5/8$.
>
> | | $X_2=0$ | $X_2=1$ |
> |---|---|---|
> | $p_{X_1|X_2}(0|\cdot)$ | $(1/4)/(3/8) = 2/3$ | $(1/8)/(5/8) = 1/5$ |
> | $p_{X_1|X_2}(1|\cdot)$ | $(1/8)/(3/8) = 1/3$ | $(1/2)/(5/8) = 4/5$ |
>
> Colonne: $2/3 + 1/3 = 1$ ✓, $1/5 + 4/5 = 1$ ✓. Righe: $2/3 + 1/5 = 13/15 \neq 1$.

**Relazione con l'indipendenza**: Se $X$ e $Y$ sono indipendenti, allora $p_{X|Y}(x|y) = p_X(x)$: conoscere $Y$ non modifica la distribuzione di $X$.

---

## Estensione a n-uple di variabili aleatorie

Il caso di due variabili si generalizza naturalmente.

> [!abstract] Definizione: PMF congiunta di ordine $n$
> Date $n$ variabili aleatorie $X_1, X_2, \ldots, X_n$ con alfabeti $\mathcal{X}_1, \ldots, \mathcal{X}_n$, la PMF congiunta è:
> $$p_{X_1 \cdots X_n}(x_1, \ldots, x_n) = P(X_1 = x_1, X_2 = x_2, \ldots, X_n = x_n)$$
> È una tabella di $|\mathcal{X}_1| \times \cdots \times |\mathcal{X}_n|$ numeri non negativi che si sommano a 1.

**Marginalizzazione gerarchica**: Una PMF di ordine $n$ implica tutte le PMF di ordine inferiore. Sommando su tutti i valori di $X_k$, si ottiene la PMF congiunta delle restanti $n-1$ variabili.

> [!info] La gerarchia va solo verso il basso
> La conoscenza di ordine $n$ implica la conoscenza di ordine $n-1$, $n-2$, ..., fino a 1. Non vale il contrario: le marginali di ordine inferiore non determinano quella di ordine superiore (salvo indipendenza).

### Esempio: terne di bit

> [!example] Due leggi di probabilità per terne binarie
> Si considerano tre variabili aleatorie binarie $X_1, X_2, X_3 \in \{0, 1\}$, con $p \in (0,1)$.
>
> **Prima legge (sorgente senza memoria)**:
> $$p_{X_1 X_2 X_3}(x_1, x_2, x_3) = p^{k} (1-p)^{3-k}$$
> dove $k$ è il numero di 1 nella terna. In questa legge i tre bit sono **indipendenti**: la probabilità di ogni terna è il prodotto delle probabilità dei singoli bit ($p$ per 1, $1-p$ per 0).
>
> **Seconda legge (bit di parità)**:
> Le terne con numero dispari di 1 hanno probabilità 0. Le terne con numero pari di 1 hanno probabilità $p^k (1-p)^{2-k}$ (per $k = 0, 2$).
>
> In questa seconda legge, $X_3$ è il **bit di parità** dei primi due: è deterministicamente uguale a $X_1 \oplus X_2$. I bit $X_1$ e $X_2$ sono indipendenti, ma $X_3$ è dipendente dagli altri due.
>
> **Entrambe le leggi hanno le stesse marginali**: $p_{X_i}(0) = 1-p$, $p_{X_i}(1) = p$ per $i = 1, 2, 3$. Eppure modellano fenomeni radicalmente diversi.

Questo esempio mostra concretamente che scegliere una legge di probabilità congiunta significa **modellare un fenomeno fisico** specifico. Leggi diverse con le stesse marginali corrispondono a fenomeni diversi.

---

## Regola della catena e marginalizzazione come media

### Regola della catena

Per tre variabili aleatorie:

$$p_{XYZ}(x, y, z) = p_Z(z) \cdot p_{Y|Z}(y|z) \cdot p_{X|YZ}(x|y,z)$$

e analogamente per ogni permutazione degli indici. La regola si generalizza a $n$ variabili.

### Marginalizzazione come media statistica

Si può riscrivere la marginalizzazione come:

$$p_X(x) = \sum_{y \in \mathcal{Y}} p_{X|Y}(x|y) \cdot p_Y(y) = E_Y[p_{X|Y}(x|Y)]$$

Cioè, la PMF marginale di $X$ è la **media rispetto a $Y$** della PMF condizionale di $X$ dato $Y$. Questo punto di vista ha applicazioni importanti nella teoria delle code e nei processi di Poisson (da approfondire).

---

> [!abstract] Punti chiave della lezione
> - Una coppia di variabili aleatorie è caratterizzata dalla PMF congiunta: una tabella di $|\mathcal{X}| \times |\mathcal{Y}|$ numeri non negativi che sommano a 1.
> - Dalla congiunta si ricavano le marginali per somma (marginalizzazione). Il viceversa non vale in generale.
> - Due variabili sono indipendenti se e solo se la congiunta si fattorizza nel prodotto delle marginali.
> - La PMF condizionale $p_{X|Y}(x|y)$ è una legge di probabilità per $Y$ fisso, non per tutte le coppie $(x,y)$.
> - Una PMF di ordine $n$ implica tutte le PMF di ordine inferiore; una caratterizzazione di ordine superiore implica quelle di ordine inferiore.

---

#MSP #PMF-congiunta #marginalizzazione #indipendenza #variabili-multiple #probabilita

---