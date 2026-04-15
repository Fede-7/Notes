---
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
periodo: Marzo 2026
tags:
  - probabilità
  - statistica
  - informazione
  - machine-learning
  - segnali
---

# 1. Fondamenti di Calcolo delle Probabilità

Il concetto di informazione è intrinsecamente legato a quello di incertezza. In ambito informatico e delle telecomunicazioni, il trasferimento di dati può avvenire nello spazio (comunicazione) o nel tempo (memorizzazione). Se non vi fosse incertezza sul messaggio ricevuto o recuperato, non vi sarebbe alcuna informazione utile da trasmettere. La **probabilità** costituisce lo strumento formale necessario per modellare tale incertezza e rappresenta la base teorica su cui poggiano discipline moderne come il *machine learning* e l'inferenza statistica.

## 1.1 Spazio dei Campioni ed Eventi

Ogni analisi probabilistica inizia con la definizione di un **esperimento**, ovvero un'operazione che conduce a uno tra più risultati possibili.

> [!abstract] Definizione: Spazio dei Campioni $\Omega$
> Lo **spazio dei campioni** (o *sample space*) è l'insieme di tutti i possibili esiti elementari $\omega$ di un esperimento. Un **evento** è un sottoinsieme di $\Omega$.

Lo spazio dei campioni può essere di tre tipologie:
1. **Finito**: ad esempio il lancio di un dado ($\Omega = \{1, 2, 3, 4, 5, 6\}$).
2. **Numerabilmente infinito**: ad esempio il numero di pacchetti che arrivano a un router ($\Omega = \mathbb{N}_0$).
3. **Non numerabile (continuo)**: ad esempio la tensione di rumore ai capi di un resistore ($\Omega = \mathbb{R}$).

È fondamentale osservare che la proposizione che descrive un evento non è univoca, data la ridondanza del linguaggio naturale. L'evento è definito unicamente dall'insieme di esiti che lo compongono, ma saper riformulare la proposizione in modo logico è spesso la chiave per la risoluzione di problemi complessi.

## 1.2 Approccio Frequentistico e Assiomi di Kolmogorov

Storicamente, la probabilità di un evento $A$ è stata introdotta tramite la **frequenza di successo** su $n$ prove indipendenti:
$$f_n(A) = \frac{N_A}{n} \tag{1.1}$$
dove $N_A$ è il numero di volte in cui $A$ si è verificato. Sebbene intuitivo, l'approccio frequentistico soffre di circolarità logica, poiché richiede il concetto di indipendenza, che è a sua volta un concetto probabilistico. La teoria moderna risolve il problema tramite l'assiomatizzazione di Kolmogorov.

> [!abstract] Teorema: Assiomi di Kolmogorov
> Dato uno spazio $\Omega$ e una $\sigma$-algebra $\mathcal{E}$ di suoi sottoinsiemi, una legge di probabilità $P$ è una funzione $P: \mathcal{E} \to [0,1]$ tale che:
> 1. **Non negatività**: $P(A) \geq 0$ per ogni $A \in \mathcal{E}$.
> 2. **Normalizzazione**: $P(\Omega) = 1$.
> 3. **$\sigma$-additività**: Per ogni successione di eventi $\{A_i\}$ a due a due disgiunti, $P(\bigcup $A_i$) = \sum P($A_i$)$.

Dagli assiomi derivano proprietà fondamentali quali la probabilità del complementare $P($A^c$) = 1 - P(A)$ e la formula dell'unione (subadditività):
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) \tag{1.2}$$
## 1.3 Probabilità Condizionata e Bayes

L'introduzione di una condizione equivale a un restringimento dello spazio dei campioni. Se sappiamo che si è verificato l'evento $B$, l'unico modo in cui $A$ può verificarsi è tramite l'intersezione $A \cap B$.

> [!abstract] Definizione: Probabilità Condizionata
> La probabilità di $A$ dato $B$ è definita come:
> $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$
Dalla definizione segue la **Legge di Bayes**, pilastro dell'inferenza statistica, che permette di aggiornare una conoscenza *a priori* $P(B)$ in una conoscenza *a posteriori* $P(B|A)$ dopo aver osservato un dato $A$:
$$P(B \mid A) = \frac{P(A \mid B) P(B)}{P(A)} \tag{1.3}$$
# 2. Variabili Aleatorie Discrete

Le **variabili aleatorie** (VA) permettono di associare un valore numerico agli esiti di un esperimento, unificando trattazioni di fenomeni fisicamente diversi ma probabilisticamente equivalenti.

## 2.1 Caratterizzazione tramite PMF e Valore Atteso

Una VA discreta $X$ è caratterizzata dalla sua **Probability Mass Function** (PMF), definita come $p_X(x) = P(X = x)$. La PMF deve essere non negativa e sommare a 1 su tutto l'alfabeto $\mathcal{X}$.

L'indice sintetico principale di una VA è il **valore atteso** (o media statistica), che rappresenta il baricentro della distribuzione:
$$E[X] = \mu_X = \sum_{x \in \mathcal{X}} x \cdot p_X(x) \tag{2.1}$$
## 2.2 Modelli di Distribuzione Notevoli

### 2.2.1 Distribuzione Binomiale
Modella il numero di successi in $n$ prove indipendenti di Bernoulli (esito binario con probabilità $p$).

> [!abstract] PMF Binomiale: $X \sim \mathcal{B}(n, p)$
> $$p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}$$
> con $E[X] = np$.

### 2.2.2 Distribuzione di Poisson
Modella il numero di occorrenze di eventi rari in un intervallo continuo (es. pacchetti in un router, chiamate a un centralino).

> [!abstract] PMF di Poisson: $X \sim \text{Poi}(\lambda)$
> $$p_X(k) = \frac{\lambda^k}{k!} e^{-\lambda}$$
> con $E[X] = \lambda$.

La Poissoniana è il limite della Binomiale quando $n \to \infty$ e $p \to 0$, mantenendo costante il prodotto $np = \lambda$.

### 2.2.3 Distribuzione Geometrica
Rappresenta il numero di prove necessarie per ottenere il primo successo. È l'unica distribuzione discreta a godere della proprietà di **assenza di memoria**: il fallimento delle prove passate non influenza la probabilità del successo futuro.

> [!abstract] PMF Geometrica: $X \sim \text{Geo}(p)$
> $$p_X(k) = (1-p)^{k-1} p$$
> con $E[X] = 1/p$.

# 3. Caratterizzazione del Secondo Ordine e Funzioni di VA

## 3.1 Trasformazioni di Variabili Aleatorie
Data una VA $X$ e una funzione $g(\cdot)$, la nuova variabile $Y = g(X)$ eredita la statistica di $X$. Se $g$ è molti-a-uno, la PMF di $Y$ in un punto $y$ è data dalla somma delle probabilità di tutti gli $x$ tali che $g(x)=y$.
Il calcolo della media di una funzione non richiede necessariamente la PMF di $Y$, grazie al **teorema fondamentale del calcolo della media**:
$$E[g(X)] = \sum_{x \in \mathcal{X}} g(x) p_X(x) \tag{3.1}$$
## 3.2 Varianza e Disuguaglianza di Chebyshev
Mentre la media indica la posizione, la **varianza** $\sigma_X^2$ misura la dispersione dei valori attorno ad essa:
$$\sigma_X^2 = E[(X - \mu_X)^2] = E[X^2] - \mu_X^2 \tag{3.2}$$
Il valore $\sigma_X$ è detto deviazione standard. La sua importanza è sancita dalla **disuguaglianza di Chebyshev**, che fornisce un limite superiore alla probabilità che una VA si discosti dalla media, indipendentemente dalla sua distribuzione:
$$P(|X - \mu_X| \geq k\sigma_X) \leq \frac{1}{k^2} \tag{3.3}$$
Questa disuguaglianza giustifica formalmente la **Legge dei Grandi Numeri**: al crescere del numero di prove $n$, la frequenza di successo si concentra intorno alla probabilità teorica poiché la sua varianza decade come $1/n$.

# 4. Variabili Multiple e Teoria dell'Informazione

## 4.1 PMF Congiunta e Marginalizzazione
Nello studio di coppie di variabili $(X, Y)$, la caratterizzazione completa è fornita dalla **PMF congiunta** $p_{XY}(x, y)$. Da essa si ricavano le **marginali** sommando rispetto all'altra variabile:
$$p_X(x) = \sum_{y \in \mathcal{Y}} p_{XY}(x, y) \tag{4.1}$$
Due variabili sono **indipendenti** se e solo se la congiunta è il prodotto delle marginali: $p_{XY}(x, y) = p_X(x)p_Y(y)$.

## 4.2 Correlazione e Covarianza
La **covarianza** misura il legame lineare tra due variabili:
$$\text{Cov}(X, Y) = E[XY] - E[X]E[Y] \tag{4.2}$$
Il **coefficiente di correlazione** $\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$ normalizza tale legame nell'intervallo $[-1, 1]$. L'indipendenza implica l'incorrelazione ($\rho=0$), ma il viceversa non è generalmente vero.

## 4.3 Entropia di Shannon
L'entropia $H(X)$ misura l'incertezza media di una sorgente di informazione in bit:

> [!abstract] Definizione: Entropia
> $$H(X) = - \sum_{x \in \mathcal{X}} p_X(x) \log_2 p_X(x)$$
L'entropia è massima per distribuzioni uniformi e nulla per variabili deterministiche. Essa rappresenta il limite teorico alla compressione dei dati senza perdita di informazione.

# 5. Variabili Aleatorie Continue

Nello spazio continuo, la probabilità di un singolo punto è nulla. Si introduce quindi la **Funzione Densità di Probabilità** (PDF).

## 5.1 PDF e CDF
La **Cumulative Distribution Function** (CDF) è definita come $F_X(x) = P(X \leq x)$. Per variabili continue, la PDF $f_X(x)$ è la derivata della CDF:
$$f_X(x) = \frac{d}{dx} F_X(x) \quad \Rightarrow \quad P(a \leq X \leq b) = \int_a^b f_X(x) dx \tag{5.1}$$
## 5.2 Modelli Continui Notevoli

1. **Uniforme $U(a, b)$**: Densità costante $1/(b-a)$ nell'intervallo.
2. **Esponenziale $\text{Exp}(\lambda)$**: Modella il tempo di attesa tra eventi di Poisson. Gode della proprietà di assenza di memoria nel continuo.
3. **Laplaciana**: Caratterizzata da una densità a "doppia vela" $f_X(x) = $\frac{\lambda}{2}$ e^{-\lambda|x|}$, spesso usata per modellare segnali audio o errori con code pesanti.
4. **Gaussiana (Normale)**: Per il **Teorema del Limite Centrale**, la somma di un grande numero di variabili i.i.d. tende a una distribuzione gaussiana, rendendola il modello ubiquitario per il rumore termico e i fenomeni naturali.

> [!tip] Osservazione: Il Valore Modale
> In ambito continuo, il valore in cui la PDF è massima non è il "più probabile" (avendo ogni punto probabilità zero), ma è correttamente definito **moda** o valore modale, indicando la zona di massima concentrazione di probabilità.

---
