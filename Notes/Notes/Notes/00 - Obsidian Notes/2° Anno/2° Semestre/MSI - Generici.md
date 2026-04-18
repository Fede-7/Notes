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

# 1. Fondamenti di Teoria della Probabilità

La teoria della probabilità costituisce l'impalcatura matematica necessaria per modellare l'incertezza, un concetto intrinseco alla definizione stessa di informazione. In ambito ingegneristico, la distinzione tra telecomunicazioni e informatica risiede nella natura del trasferimento dell'informazione: le prime la veicolano nello spazio, la seconda nel tempo (attraverso la memorizzazione). In entrambi i casi, l'incertezza *a priori* deve essere trasformata in certezza *a posteriori*. Qualunque sistema di *machine learning* o elaborazione dei segnali moderno è costruito su basi probabilistiche.

## 1.1 Esperimento, Spazio dei Campioni ed Eventi

Ogni teoria matematica della probabilità parte dalla definizione di **esperimento**, ovvero un'operazione che conduce a uno tra più risultati possibili. L'insieme di tutti i risultati elementari $\omega$ è definito **spazio dei campioni** (*sample space*) e indicato con $\Omega$. 

Dalla struttura di $\Omega$ dipende la natura del modello: esso può essere **finito** (lancio di una moneta), **numerabilmente infinito** (numero di pacchetti in una coda) o **non numerabile** (misura di una tensione elettrica). Un **evento** è un sottoinsieme di $\Omega$ definito da una proposizione logica. È cruciale notare che la proposizione non è univoca; la ridondanza del linguaggio naturale permette descrizioni diverse dello stesso insieme di esiti. La capacità di riformulare queste proposizioni in forme analiticamente convenienti rappresenta spesso la chiave per la risoluzione di problemi complessi.

> [!abstract] Definizione: Nomenclatura degli eventi
> - **Evento certo**: coincide con $\Omega$ stesso.
> - **Evento impossibile**: coincide con l'insieme vuoto $\emptyset$.
> - **Eventi incompatibili**: due eventi $A$ e $B$ tali che $A \cap B = \emptyset$.
> - **Inclusione**: se $A \subseteq B$, il verificarsi di $A$ implica necessariamente il verificarsi di $B$.

## 1.2 Approcci alla Definizione di Probabilità

L'approccio **frequentistico** definisce la probabilità come il limite della frequenza relativa di successo dell'evento $A$ su $n$ prove indipendenti:
$$f_n(A) = \frac{N_A}{n} \xrightarrow{n \to \infty} P(A) \tag{1.1}$$
Sebbene intuitivo, questo approccio è logicamente circolare, poiché presuppone il concetto di indipendenza, che è esso stesso probabilistico. Per superare tale limite, si adotta la **definizione assiomatica di Kolmogorov**, che tratta la probabilità come una misura definita su una $\sigma$-algebra $\mathcal{E}$ di sottoinsiemi di $\Omega$.

> [!abstract] Assiomi di Kolmogorov
> Una legge di probabilità è una funzione $P: \mathcal{E} \to [0,1]$ che soddisfa:
> 1. **Non negatività**: $P(A) \geq 0$ per ogni $A \in \mathcal{E}$.
> 2. **Normalizzazione**: $P(\Omega) = 1$.
> 3. **$\sigma$-additività**: Per ogni successione di eventi $\{A_i\}$ disgiunti, $P(\bigcup_{i=1}^\infty $A_i$) = \sum_{i=1}^\infty P($A_i$)$.

Dagli assiomi derivano le proprietà fondamentali, tra cui la **subadditività** per l'unione di eventi non disgiunti: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

## 1.3 Calcolo Combinatorio e Probabilità su Spazi Finiti

Negli spazi campionari finiti dove gli eventi elementari sono equiprobabili, la probabilità di un evento $A$ è il rapporto tra la sua cardinalità $|A|$ e quella dello spazio totale $|\Omega|$. Il calcolo si riduce dunque a un problema di enumerazione efficiente tramite l'analisi combinatoria.

La regola fondamentale è la **regola del prodotto**, secondo cui se una scelta può essere fatta in $n$ modi e una successiva in $m$, le combinazioni totali sono $n \cdot m$. Da qui si derivano le **disposizioni** (sequenze ordinate) e le **combinazioni** (sottoinsiemi non ordinati).

> [!abstract] Definizione: Coefficiente Binomiale
> Il numero di modi in cui è possibile scegliere $k$ elementi da un insieme di $n$ senza considerare l'ordine è dato dal coefficiente binomiale:
> $$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$
Questo strumento è essenziale per il calcolo delle probabilità in giochi come il *poker* o nel conteggio di sequenze binarie con un numero fissato di errori.

# 2. Condizionamento e Indipendenza

L'informazione acquisita durante un esperimento modifica la nostra percezione dell'incertezza. Analiticamente, questo fenomeno si traduce nel concetto di **probabilità condizionata**, che opera una restrizione dello spazio dei campioni $\Omega$ a un sottoinsieme $B$, considerato come nuovo "universo di riferimento".

## 2.1 Probabilità Condizionata e Legge di Bayes

La probabilità dell'evento $A$ dato il verificarsi di $B$ è definita dal rapporto tra la probabilità della loro intersezione e la probabilità della condizione:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \tag{2.1}$$
Dalla commutatività dell'intersezione si deriva la **legge della probabilità composta**: $P(A \cap B) = P(A \mid B)P(B) = P(B \mid A)P(A)$. Uguagliando queste espressioni si ottiene la **Legge di Bayes**, pilastro dell'inferenza statistica:
$$P(B \mid A) = \frac{P(A \mid B)P(B)}{P(A)} \tag{2.2}$$
Bayes permette l'aggiornamento delle credenze: $P(B)$ è la probabilità *a priori*, mentre $P(B|A)$ è la probabilità *a posteriori* ottenuta dopo aver osservato il dato $A$. Se l'osservazione è coerente con l'ipotesi, la probabilità aumenta.

## 2.2 Legge della Probabilità Totale

In molti problemi complessi è difficile calcolare $P(A)$ direttamente. Si ricorre dunque a una **partizione** dello spazio $\Omega$ in eventi mutuamente esclusivi ed esaustivi $\{$E_1$, $E_2$, \ldots, E_m\}$.

> [!abstract] Teorema della Probabilità Totale
> La probabilità di un evento $A$ può essere calcolata mediando le probabilità condizionate rispetto a una partizione:
> $$P(A) = \sum_{i=1}^m P(A \mid E_i)P(E_i)$$
Questa legge è fondamentale nella modellazione di canali di comunicazione, dove si condiziona l'uscita rispetto ai possibili simboli trasmessi all'ingresso.

## 2.3 Indipendenza Stocastica

Due eventi $A$ e $B$ si dicono **indipendenti** se il verificarsi di uno non fornisce alcuna informazione sul verificarsi dell'altro. Formalmente, $P(A|B) = P(A)$, che implica la fattorizzazione della probabilità congiunta: $P(A \cap B) = P(A)P(B)$.

> [!warning] Attenzione: Indipendenza a coppie vs congiunta
> L'indipendenza a coppie tra tre eventi $(A, B, C)$ non garantisce l'indipendenza della terna. Un esempio classico è il *bit di parità*: conoscere un singolo bit non dà informazioni sul terzo, ma conoscerne due determina deterministicamente l'ultimo.

# 3. Variabili Aleatorie Discrete

Una **variabile aleatoria** (VA) è un'applicazione che associa a ogni esito $\omega \in \Omega$ un valore numerico in un alfabeto $\mathcal{X}$. Questo permette di trattare esperimenti diversi (monete, dadi, segnali binari) con un linguaggio matematico unificato.

## 3.1 Probability Mass Function (PMF) e Valore Atteso

La VA discreta è completamente caratterizzata dalla sua **PMF** $p_X(x) = P(X = x)$. Essa deve essere non negativa e normalizzata a uno. Il parametro descrittivo principale è il **valore atteso** $E[X]$, che rappresenta il baricentro della distribuzione:
$$E[X] = \mu_X = \sum_{x \in \mathcal{X}} x \cdot p_X(x) \tag{3.1}$$
Per la legge dei grandi numeri, la media aritmetica di $n$ prove converge al valore atteso per $n$ che tende all'infinito. La media non deve essere necessariamente un valore appartenente all'alfabeto (si pensi al valore medio $3{,}5$ di un dado onesto).

## 3.2 Distribuzioni Discrete Notevoli

- **Bernoulli** $\text{Ber}(p)$: modella un singolo esperimento con successo (1) o fallimento (0). La media è $p$.
- **Binomiale** $\text{Bin}(n, p)$: somma di $n$ variabili di Bernoulli indipendenti. Conta il numero di successi in $n$ prove.
- **Poisson** $\text{Poi}(\lambda)$: descrive il numero di eventi rari che si verificano in un intervallo fissato. È fondamentale nella teoria delle code e nel traffico di rete. La sua proprietà distintiva è che media e varianza coincidono con $\lambda$.
- **Geometrica** $\text{Geo}(p)$: modella il tempo di attesa per il primo successo. Gode della proprietà di **assenza di memoria**, ovvero il futuro non dipende dal numero di fallimenti già accumulati.

> [!tip] Osservazione: Outlier
> La media è estremamente sensibile agli *outlier* (valori anomali). In distribuzioni asimmetriche o con code pesanti, la **mediana** risulta spesso un indicatore più robusto del centro della distribuzione.

# 4. Momenti e Trasformazioni di Variabili Aleatorie

Spesso è necessario analizzare variabili ottenute come funzione di altre variabili, $Y = g(X)$. 

## 4.1 Teorema Fondamentale della Media

Il calcolo della media di $Y = g(X)$ non richiede la determinazione della PMF di $Y$, poiché si può operare direttamente su quella di $X$ attraverso il **teorema fondamentale**:
$$E[g(X)] = \sum_{x \in \mathcal{X}} g(x) p_X(x) \tag{4.1}$$
Questo teorema permette di definire il **valore quadratico medio** $E[X^2]$ e la **varianza** $\sigma_X^2$. Quest'ultima misura l'aleatorietà della variabile, ovvero la dispersione dei valori attorno alla media:
$$\sigma_X^2 = E[(X - \mu_X)^2] = E[X^2] - \mu_X^2 \tag{4.2}$$
Il valore efficace, o **RMS** (*Root Mean Square*), è la radice quadrata del valore quadratico medio e ha profonde implicazioni fisiche nella misura della potenza dei segnali.

## 4.2 Disuguaglianza di Chebyshev e Convergenza

La varianza definisce un limite superiore alla probabilità che una variabile si discosti dalla propria media.

> [!abstract] Disuguaglianza di Chebyshev
> Per ogni $k > 0$:
> $$P(|X - \mu_X| \geq k\sigma_X) \leq \frac{1}{k^2}$$
Questo risultato garantisce che la frequenza di successo $F_n(A)$ converga alla probabilità $P(A)$ sia in media quadratica che in probabilità. Al crescere di $n$, la varianza della frequenza decade come $1/n$, rendendo la variabile quasi deterministica e coincidente con la sua media.

# 5. Variabili Aleatorie Multiple e Teoria dell'Informazione

Quando si osservano più grandezze contemporaneamente, si definisce un vettore aleatorio caratterizzato dalla **PMF congiunta** $p_{XY}(x, y) = P(X=x, Y=y)$.

## 5.1 Marginalizzazione e Indipendenza

Dalla congiunta si ricavano le **marginali** sommando rispetto all'altra variabile: $p_X(x) = \sum_y p_{XY}(x, y)$. È fondamentale notare che la congiunta contiene informazioni sul legame tra le variabili che le marginali da sole non possono fornire, a meno che le variabili non siano indipendenti.

Il legame lineare tra due variabili è misurato dalla **covarianza** e dal **coefficiente di correlazione** $\rho_{XY} \in [-1, 1]$. L'indipendenza implica l'incorrelazione ($\rho=0$), ma il viceversa è falso, tranne che nel caso di variabili gaussiane.

## 5.2 Fondamenti di Teoria dell'Informazione

L'informazione contenuta in un evento è legata all'imprevedibilità del suo verificarsi. Claude Shannon definì l'informazione di un evento $A$ come $I(A) = \log_2(1/P(A))$. L'**entropia** $H(X)$ è la media statistica di tale informazione:
$$H(X) = - \sum_{x \in \mathcal{X}} p_X(x) \log_2 p_X(x) \tag{5.1}$$
L'entropia misura l'incertezza media in *bit*. Un file compresso ideale tende ad avere una distribuzione uniforme di bit, poiché l'entropia è massima quando tutti i simboli sono equiprobabili. In un **canale binario simmetrico** (BSC), l'entropia permette di quantificare la perdita di informazione dovuta al rumore.

# 6. Variabili Aleatorie Continue

Nel caso continuo, la probabilità che una VA assuma un valore esatto è nulla. Si introduce dunque la **Funzione Distribuzione Cumulativa** (CDF) $F_X(x) = P(X \leq x)$.

## 6.1 PDF e Valor Medio Integrale

La **densità di probabilità** (PDF) è la derivata della CDF: $f_X(x) = d/dx F_X(x)$. La probabilità di un intervallo $[a, b]$ è l'area sottesa dalla PDF in quell'intervallo. Il valore atteso nel continuo si ottiene per integrazione:
$$E[X] = \int_{-\infty}^\infty x f_X(x) dx \tag{6.1}$$
## 6.2 Modelli Continui e Quantizzazione

Le distribuzioni notevoli includono l'**uniforme**, l'**esponenziale** (tempo di attesa) e la **gaussiana** (normale). La distribuzione esponenziale è l'unica nel continuo a godere dell'assenza di memoria.

Un concetto fondamentale è quello della **quantizzazione**: per digitalizzare un segnale continuo, esso viene diviso in livelli. Shannon dimostrò che la quantizzazione di vettori di dati è asintoticamente più efficiente della quantizzazione scalare, principio alla base di standard come l'MP3 o l'H.264.

> [!warning] Attenzione: Densità vs Probabilità
> La PDF può assumere valori maggiori di 1. Essa non rappresenta una probabilità, ma una concentrazione di probabilità. Solo l'integrale della PDF ha un significato probabilistico diretto.