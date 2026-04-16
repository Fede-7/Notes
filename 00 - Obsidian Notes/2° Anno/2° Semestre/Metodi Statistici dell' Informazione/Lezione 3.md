---
date: 2026-03-11
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 3
tags:
  - MSI
  - variabili-aleatorie
  - valore-atteso
  - Bernoulli
  - binomiale
  - uniforme
  - Poisson
  - geometrica
  - Bayes
  - PMF-condizionata
  - outlier
Professore: Marco Lops
---

# MSI — Lezione 3: Valore Atteso e Distribuzioni Notevoli
---

>[!question] Argomenti trattati:
> - Definizione del valore atteso (media statistica) e motivazione tramite legge dei grandi numeri
> - Distribuzione di Bernoulli e distribuzione Binomiale: definizione, verifica PMF, media $= np$ (derivazione completa)
> - Connessione tra la Binomiale e i problemi di conteggio combinatorio
> - Distribuzione Uniforme discreta: definizione, media = media aritmetica dell'alfabeto
> - Formula di Gauss per la somma dei primi $n$ interi
> - Distribuzione di Poisson: definizione, verifica PMF tramite serie esponenziale, media $= \lambda$
> - Applicazioni della Poisson: code di traffico, router, uffici postali
> - Distribuzione Geometrica: tempo al primo successo, PMF, media $= 1/p$ (derivazione con serie geometrica)
> - Esercizio: 3 dadi (2 onesti, 1 truccato), applicazione del teorema di Bayes
> - Introduzione alla PMF condizionata
> - Cenni sugli outlier nell'analisi dei dati

---

## Valore Atteso (Media Statistica)

### Motivazione: dalla frequenza alla media

Nella lezione precedente abbiamo introdotto le variabili aleatorie discrete e la funzione massa di probabilità (PMF). Ora ci chiediamo: dato che una variabile aleatoria $X$ può assumere diversi valori, esiste un singolo numero che ne "riassuma" il comportamento medio?

L'idea nasce dalla statistica descrittiva. Supponiamo di ripetere un esperimento $n$ volte e di osservare i valori $x_1, x_2, \ldots, x_n$. La **media campionaria** (la media aritmetica delle osservazioni) è:

$$\bar{x}_n = \frac{1}{n} \sum_{i=1}^{n} x_i$$

Sia $\mathcal{X} = \{a_1, a_2, \ldots, a_M\}$ l'**alfabeto** di $X$, cioè l'insieme dei valori che $X$ può assumere. Se il valore $a_k$ compare $N_k$ volte nelle $n$ prove (dove $\sum_{k=1}^{M} N_k = n$), possiamo riscrivere la media campionaria raggruppando i termini uguali:

$$\bar{x}_n = \frac{1}{n} \sum_{k=1}^{M} N_k \cdot a_k = \sum_{k=1}^{M} \frac{N_k}{n} \cdot a_k = \sum_{k=1}^{M} f_n(a_k) \cdot a_k$$

dove $f_n(a_k) = N_k / n$ è la **frequenza relativa** del valore $a_k$ su $n$ prove. Per la **legge dei grandi numeri**, quando il numero di prove $n$ tende all'infinito, la frequenza relativa converge alla probabilità:

$$f_n(a_k) \xrightarrow{n \to \infty} P_X(a_k)$$

Quindi la media campionaria converge a un valore ben definito:

$$\bar{x}_n \xrightarrow{n \to \infty} \sum_{k=1}^{M} a_k \cdot P_X(a_k)$$

Questo limite è il **valore atteso** della variabile aleatoria.

> [!abstract] Definizione: Valore atteso (media statistica)
> Sia $X$ una variabile aleatoria discreta con alfabeto $\mathcal{X} = \{a_1, a_2, \ldots, a_M\}$ (finito o numerabile) e PMF $P_X(x)$. Il **valore atteso** (o **media statistica**, o **speranza matematica**) di $X$ è definito come:
> $$E[X] = \mu_X = \sum_{k=1}^{M} a_k \cdot P_X(a_k)$$
> dove $a_k$ sono i valori nell'alfabeto e $P_X(a_k)$ le rispettive probabilità. Il simbolo $E[\cdot]$ si legge "valore atteso di" oppure "aspettazione di"; $\mu_X$ è la notazione alternativa con la lettera greca mu.

> [!warning] Media statistica vs media aritmetica
> La media statistica **non** coincide in generale con la media aritmetica dei valori dell'alfabeto. La media aritmetica pesa tutti i valori allo stesso modo ($1/M$ ciascuno); la media statistica è una **media pesata** con pesi $P_X(a_k)$. Solo quando la distribuzione è uniforme (tutti i valori equiprobabili) le due medie coincidono.

> [!tip]
> "La media statistica è il baricentro della distribuzione di probabilità: se mettete dei pesi sulle posizioni dell'asse reale, il baricentro cade dove c'è più massa di probabilità. È il numero verso cui converge la media campionaria quando fate tante prove."

---

## Distribuzione di Bernoulli

> [!abstract] Definizione: Variabile aleatoria di Bernoulli
> Una variabile aleatoria $X$ segue una **distribuzione di Bernoulli** di parametro $p \in [0,1]$, e si scrive $X \sim \text{Ber}(p)$, se:
> - L'alfabeto è $\mathcal{X} = \{0, 1\}$, dove $1$ rappresenta il **successo** e $0$ il **fallimento**
> - La PMF è:
> $$P_X(x) = \begin{cases} p & \text{se } x = 1 \\ 1-p = q & \text{se } x = 0 \end{cases}$$
> Il parametro $p$ è la **probabilità di successo** e $q = 1 - p$ la probabilità di fallimento.

**Scrittura compatta della PMF.** La PMF di Bernoulli si può esprimere in forma chiusa, valida per entrambi i valori dell'alfabeto con un'unica espressione:

$$P_X(x) = p^x (1-p)^{1-x}, \qquad x \in \{0,1\}$$

**Verifica:** per $x=1$ si ottiene $p^1 (1-p)^0 = p$; per $x=0$ si ottiene $p^0 (1-p)^1 = 1-p = q$. Corretto.

**Verifica della normalizzazione.** La somma di tutte le probabilità deve dare $1$:

$$\sum_{x \in \{0,1\}} P_X(x) = P_X(0) + P_X(1) = (1-p) + p = 1 \quad \checkmark$$

### Media della Bernoulli

Il valore atteso di $X \sim \text{Ber}(p)$ si calcola direttamente dalla definizione, sommando su tutti i valori dell'alfabeto:

$$E[X] = \sum_{x \in \{0,1\}} x \cdot P_X(x) = 0 \cdot (1-p) + 1 \cdot p = p$$

$$\boxed{E[X] = p}$$

La media di una Bernoulli è semplicemente la probabilità di successo.

> [!example] Esempio: lancio di una moneta
> Una moneta onesta ha probabilità $p = 0{,}5$ di dare testa (codificata come $X=1$). La media di $X$ è $E[X] = 0{,}5$: se lancio la moneta un numero enorme di volte e faccio la media dei risultati (0 e 1), il valore converge a $0{,}5$.

---

## Distribuzione Binomiale

> [!abstract] Definizione: Distribuzione Binomiale
> Siano $X_1, X_2, \ldots, X_n$ variabili aleatorie **i.i.d.** (indipendenti e identicamente distribuite), ciascuna con distribuzione $X_i \sim \text{Ber}(p)$. La variabile aleatoria:
> $$S_n = X_1 + X_2 + \cdots + X_n = \sum_{i=1}^{n} X_i$$
> conta il **numero totale di successi** in $n$ prove di Bernoulli indipendenti. Si dice che $S_n$ segue una **distribuzione Binomiale** di parametri $n$ (numero di prove) e $p$ (probabilità di successo nella singola prova):
> $$S_n \sim \text{Bin}(n, p)$$
> L'alfabeto è $\mathcal{X} = \{0, 1, 2, \ldots, n\}$ e la PMF è:
> $$P_{S_n}(k) = \binom{n}{k} p^k (1-p)^{n-k}, \qquad k = 0, 1, \ldots, n$$
> dove $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ è il **coefficiente binomiale**.

### Interpretazione combinatoria (connessione con il conteggio)

La PMF binomiale ha una struttura che si spiega interamente con gli strumenti dell'analisi combinatoria visti nelle prime lezioni:

- Il fattore $p^k (1-p)^{n-k}$ è la probabilità di una **specifica sequenza** di $n$ prove che contiene esattamente $k$ successi e $n-k$ fallimenti. Per l'indipendenza delle prove, le probabilità si moltiplicano.
- Il fattore $\binom{n}{k}$ conta il **numero di sequenze distinte** di lunghezza $n$ con esattamente $k$ successi (e $n-k$ fallimenti). Questo è esattamente il conteggio delle sequenze binarie con $k$ uni che avevamo derivato nella Lezione 2.

La PMF è quindi: (numero di sequenze favorevoli) $\times$ (probabilità di ciascuna sequenza).

### Verifica della normalizzazione

La somma di tutte le probabilità deve dare $1$. Applicando il Binomio di Newton con $a = p$ e $b = (1-p)$:

$$\sum_{k=0}^{n} P_{S_n}(k) = \sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = \big(p + (1-p)\big)^n = 1^n = 1 \quad \checkmark$$

### Media della Binomiale: derivazione completa

- **Metodo 1 — Per linearità del valore atteso.** Poiché $S_n = X_1 + X_2 + \cdots + X_n$ con $X_i \sim \text{Ber}(p)$ indipendenti, e poiché il valore atteso è un operatore **lineare** (la media di una somma è la somma delle medie):

$$E[S_n] = E\left[\sum_{i=1}^{n} X_i\right] = \sum_{i=1}^{n} E[X_i] = \sum_{i=1}^{n} p = np$$

$$\boxed{E[S_n] = np}$$

- **Metodo 2 — Calcolo diretto dalla definizione della PMF.** Si parte dalla definizione:

$$E[S_n] = \sum_{k=0}^{n} k \cdot \binom{n}{k} p^k (1-p)^{n-k}$$

Il termine con $k=0$ è nullo, quindi la somma parte da $k=1$:

$$= \sum_{k=1}^{n} k \cdot \frac{n!}{k!(n-k)!} \, p^k (1-p)^{n-k}$$

Semplifichiamo $k$ con $k! = k \cdot (k-1)!$:

$$= \sum_{k=1}^{n} \frac{n!}{(k-1)!(n-k)!} \, p^k (1-p)^{n-k}$$

Raccogliamo il fattore $np$ scrivendo $n! = n \cdot (n-1)!$ e $p^k = p \cdot p^{k-1}$:

$$= np \sum_{k=1}^{n} \frac{(n-1)!}{(k-1)!\big((n-1)-(k-1)\big)!} \, p^{k-1} (1-p)^{(n-1)-(k-1)}$$

Effettuiamo il cambio di indice $j = k-1$ e poniamo $m = n-1$:

$$= np \sum_{j=0}^{m} \binom{m}{j} p^j (1-p)^{m-j} = np \cdot \big(p + (1-p)\big)^m = np \cdot 1 = np$$

> I due metodi danno lo stesso risultato: $E[S_n] = np$.

> [!example] Esempio: vaccino
> Un vaccino ha efficacia $p = 0{,}95$ (probabilità che un singolo vaccinato sviluppi l'immunità). Su $n = 1000$ vaccinati, il numero atteso di soggetti protetti è:
> $$E[S_{1000}] = 1000 \cdot 0{,}95 = 950$$

> [!example] Esempio: roulette
> Alla roulette europea, il rosso esce con probabilità $p = 18/37$ (ci sono 18 numeri rossi su 37 caselle totali). In $n = 37$ giri, il numero atteso di uscite del rosso è:
> $$E[S_{37}] = 37 \cdot \frac{18}{37} = 18$$
> Notiamo che la roulette non è un gioco equo: con 18 rossi, 18 neri e 1 zero verde, il banco ha un leggero vantaggio.

---

## Distribuzione Uniforme Discreta

> [!abstract] Definizione: Distribuzione Uniforme Discreta
> Una variabile aleatoria $X$ segue una **distribuzione uniforme discreta** sull'alfabeto $\mathcal{X} = \{a_1, a_2, \ldots, a_M\}$ se tutti i valori sono equiprobabili:
> $$P_X(a_k) = \frac{1}{M}, \qquad k = 1, 2, \ldots, M$$
> dove $M = |\mathcal{X}|$ è la **cardinalità** dell'alfabeto (il numero di valori possibili).

**Verifica della normalizzazione:**

$$\sum_{k=1}^{M} P_X(a_k) = \sum_{k=1}^{M} \frac{1}{M} = M \cdot \frac{1}{M} = 1 \quad \checkmark$$

### Media della Uniforme Discreta

Il valore atteso si calcola applicando la definizione:

$$E[X] = \sum_{k=1}^{M} a_k \cdot \frac{1}{M} = \frac{1}{M} \sum_{k=1}^{M} a_k = \frac{a_1 + a_2 + \cdots + a_M}{M}$$

> [!warning] La media della uniforme coincide con la media aritmetica dell'alfabeto
> Nel caso uniforme — e **solo** nel caso uniforme — la media statistica coincide con la media aritmetica dei valori dell'alfabeto. Per qualunque altra distribuzione, i valori con probabilità maggiore "pesano" di più e spostano la media verso di sé.

### Formula di Gauss

Quando l'alfabeto è $\mathcal{X} = \{1, 2, \ldots, M\}$ (i primi $M$ interi positivi), per calcolare la somma $1 + 2 + \cdots + M$ si usa la celebre **formula di Gauss**:

$$\sum_{k=1}^{M} k = \frac{M(M+1)}{2}$$

> [!tip]
> "La scoprì Gauss a sei anni, quando il maestro gli chiese di sommare i numeri da 1 a 100 pensando di tenerlo occupato per un'ora. Gauss scrisse l'ultimo numero accanto al primo, il penultimo accanto al secondo... e si accorse che ogni coppia faceva 101. Cinquanta coppie: $50 \times 101 = 5050$. Il maestro rimase a bocca aperta."

**Dimostrazione.** Sia $S = 1 + 2 + \cdots + M$. Scriviamo la somma due volte, una in ordine crescente e una in ordine decrescente:

$$S = 1 + 2 + \cdots + (M-1) + M$$

$$S = M + (M-1) + \cdots + 2 + 1$$

Sommando termine a termine, ogni coppia dà $(M+1)$, e le coppie sono $M$:

$$2S = \underbrace{(M+1) + (M+1) + \cdots + (M+1)}_{M \text{ volte}} = M(M+1)$$

Da cui $S = \frac{M(M+1)}{2}$.

> [!example] Esempio: dado onesto
> Un dado onesto a 6 facce ha $\mathcal{X} = \{1, 2, 3, 4, 5, 6\}$ e distribuzione uniforme ($P_X(k) = 1/6$ per ogni faccia $k$). Il valore atteso è:
> $$E[X] = \frac{1}{6} \sum_{k=1}^{6} k = \frac{1}{6} \cdot \frac{6 \cdot 7}{2} = \frac{42}{12} = 3{,}5$$
> Il valore $3{,}5$ **non appartiene all'alfabeto**: la media è un indice sintetico che indica il baricentro della distribuzione, non necessariamente un valore che la variabile può assumere.

**Formula generale.** Per una variabile uniforme su $\{1, 2, \ldots, M\}$, la media è:

$$E[X] = \frac{1}{M} \cdot \frac{M(M+1)}{2} = \frac{M+1}{2}$$

---

## Distribuzione di Poisson

> [!abstract] Definizione: Distribuzione di Poisson
> Una variabile aleatoria $X$ segue una **distribuzione di Poisson** di parametro $\lambda > 0$, e si scrive $X \sim \text{Poi}(\lambda)$, se:
> - L'alfabeto è $\mathcal{X} = \{0, 1, 2, 3, \ldots\} = \mathbb{N}_0$ (l'insieme dei naturali incluso lo zero, cioè **numerabilmente infinito**)
> - La PMF è:
> $$P_X(k) = \frac{\lambda^k}{k!} \, e^{-\lambda}, \qquad k = 0, 1, 2, \ldots$$
> Il parametro $\lambda$ (lettera greca lambda) rappresenta il **tasso medio** di occorrenze nell'intervallo di tempo (o spazio) considerato. Il simbolo $e \approx 2{,}718$ è il numero di Nepero, base del logaritmo naturale; $k!$ è il fattoriale di $k$ (con la convenzione $0! = 1$).

### Verifica della normalizzazione tramite serie esponenziale

La somma di tutte le probabilità deve dare $1$. Per verificarlo, ricordiamo lo sviluppo in **serie di Taylor dell'esponenziale**:

$$e^{\lambda} = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!}$$

Questa serie converge per ogni $\lambda \in \mathbb{R}$. Applicandola alla somma delle probabilità:

$$\sum_{k=0}^{\infty} P_X(k) = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} \, e^{-\lambda} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^{\lambda} = e^0 = 1 \quad \checkmark$$

Il fattore $e^{-\lambda}$ è proprio la costante di normalizzazione che rende la PMF una distribuzione di probabilità valida.

### Media della Poisson: $E[X] = \lambda$ (derivazione completa)

Partiamo dalla definizione di valore atteso per una variabile con alfabeto infinito numerabile:

$$E[X] = \sum_{k=0}^{\infty} k \cdot \frac{\lambda^k}{k!} \, e^{-\lambda}$$

Il termine con $k=0$ dà contributo nullo ($0 \cdot P_X(0) = 0$), quindi la somma parte da $k=1$:

$$= e^{-\lambda} \sum_{k=1}^{\infty} k \cdot \frac{\lambda^k}{k!}$$

Semplifichiamo $k$ con il fattoriale, usando $k! = k \cdot (k-1)!$:

$$= e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!}$$

Estraiamo un fattore $\lambda$ dal numeratore, scrivendo $\lambda^k = \lambda \cdot \lambda^{k-1}$:

$$= \lambda \, e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}$$

Effettuiamo il cambio di indice $j = k-1$ (quando $k=1$ si ha $j=0$; quando $k \to \infty$ si ha $j \to \infty$):

$$= \lambda \, e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^{j}}{j!} = \lambda \, e^{-\lambda} \cdot e^{\lambda} = \lambda \cdot 1 = \lambda$$

$$\boxed{E[X] = \lambda}$$

La media della Poisson è esattamente il parametro $\lambda$: un risultato elegante che conferma l'interpretazione di $\lambda$ come tasso medio.

> [!tip]
> "La Poisson è la distribuzione delle cose rare: eventi che singolarmente sono poco probabili, ma che vengono osservati su un numero enorme di occasioni. Quante macchine passano al casello in un minuto? Quanti pacchetti arrivano al router in un millisecondo? Quante persone entrano all'ufficio postale in un'ora? Tutte Poisson."

### Applicazioni della distribuzione di Poisson

> [!example] Esempio: code di traffico
> Al casello autostradale, in media arrivano $\lambda = 4$ auto al minuto. Il numero di auto che arrivano in un dato minuto si modella come $X \sim \text{Poi}(4)$. La probabilità che in un minuto ne arrivino esattamente $k = 6$ è:
> $$P(X = 6) = \frac{4^6}{6!} \, e^{-4} = \frac{4096}{720} \cdot e^{-4} \approx 5{,}689 \cdot 0{,}0183 \approx 0{,}104 \approx 10{,}4\%$$

> [!example] Esempio: pacchetti al router
> Un router di rete riceve in media $\lambda = 100$ pacchetti al millisecondo. La variabile aleatoria "numero di pacchetti ricevuti in un millisecondo" segue una $\text{Poi}(100)$. Il valore atteso è $E[X] = 100$ pacchetti/ms. Questo modello di Poisson è fondamentale nel **dimensionamento delle code** nei sistemi di rete: permette di calcolare la probabilità che il buffer del router si saturi e inizi a perdere pacchetti.

> [!example] Esempio: ufficio postale
> All'ufficio postale entrano in media $\lambda = 3$ clienti ogni 10 minuti. La probabilità che non entri **nessuno** in un intervallo di 10 minuti è:
> $$P(X = 0) = \frac{3^0}{0!} \, e^{-3} = 1 \cdot e^{-3} \approx 0{,}050 = 5\%$$
> Mentre la probabilità che ne entrino esattamente 3 (il valore medio) è:
> $$P(X = 3) = \frac{3^3}{3!} \, e^{-3} = \frac{27}{6} \cdot e^{-3} \approx 4{,}5 \cdot 0{,}050 \approx 0{,}224 \approx 22{,}4\%$$

### La Poisson come limite della Binomiale

> [!warning] Approssimazione di Poisson alla Binomiale
> Quando $n$ è molto grande e $p$ è molto piccolo, con il prodotto $\lambda = np$ che resta finito, la distribuzione Binomiale $\text{Bin}(n, p)$ è ben approssimata dalla Poisson $\text{Poi}(\lambda)$:
> $$\binom{n}{k} p^k (1-p)^{n-k} \approx \frac{\lambda^k}{k!} \, e^{-\lambda}, \qquad \text{per } n \to \infty,\; p \to 0,\; np = \lambda$$
> Questa approssimazione è molto utile nella pratica, perché evita di calcolare coefficienti binomiali con $n$ enorme.

---

## Distribuzione Geometrica

> [!abstract] Definizione: Distribuzione Geometrica
> Una variabile aleatoria $X$ segue una **distribuzione Geometrica** di parametro $p \in (0,1]$, e si scrive $X \sim \text{Geo}(p)$, se rappresenta il **numero di prove necessarie per ottenere il primo successo** in una sequenza di prove di Bernoulli indipendenti, ciascuna con probabilità di successo $p$.
> - L'alfabeto è $\mathcal{X} = \{1, 2, 3, \ldots\}$ (numerabilmente infinito: il primo successo potrebbe teoricamente non arrivare mai)
> - La PMF è:
> $$P_X(k) = (1-p)^{k-1} \, p, \qquad k = 1, 2, 3, \ldots$$
> dove $(1-p)^{k-1}$ è la probabilità di $k-1$ fallimenti consecutivi e $p$ è la probabilità del successo alla $k$-esima prova.

**Interpretazione.** Per ottenere il primo successo esattamente alla prova numero $k$, devono verificarsi:
- $k-1$ fallimenti consecutivi, ciascuno con probabilità $q = 1-p$
- Seguiti da $1$ successo, con probabilità $p$

Per l'**indipendenza** delle prove, le probabilità si moltiplicano: $\underbrace{q \cdot q \cdots q}_{k-1} \cdot \, p = q^{k-1} \, p$.

### Verifica della normalizzazione (serie geometrica)

Ricordiamo la formula della **serie geometrica**: per $|r| < 1$:

$$\sum_{k=0}^{\infty} r^k = \frac{1}{1-r}$$

Sia $q = 1-p$. Poiché $p \in (0,1]$, si ha $q \in [0,1)$ e quindi $|q| < 1$:

$$\sum_{k=1}^{\infty} P_X(k) = \sum_{k=1}^{\infty} q^{k-1} \, p = p \sum_{j=0}^{\infty} q^j = p \cdot \frac{1}{1-q} = p \cdot \frac{1}{p} = 1 \quad \checkmark$$

dove nel secondo passaggio abbiamo posto $j = k-1$.

### Media della Geometrica: $E[X] = 1/p$ (derivazione completa)

Partiamo dalla definizione:

$$E[X] = \sum_{k=1}^{\infty} k \cdot q^{k-1} \, p = p \sum_{k=1}^{\infty} k \cdot q^{k-1}$$

Per calcolare la somma $\sum_{k=1}^{\infty} k \cdot q^{k-1}$, usiamo un trucco fondamentale: riconosciamo che è la **derivata** della serie geometrica rispetto a $q$.

**Passo 1.** Partiamo dalla serie geometrica:

$$\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}$$

**Passo 2.** Deriviamo entrambi i membri rispetto a $q$. A sinistra, la derivata di $q^k$ è $k \cdot q^{k-1}$ (il termine $k=0$ scompare perché la derivata di $1$ è $0$):

$$\frac{d}{dq}\sum_{k=0}^{\infty} q^k = \sum_{k=1}^{\infty} k \cdot q^{k-1}$$

A destra:

$$\frac{d}{dq}\left(\frac{1}{1-q}\right) = \frac{1}{(1-q)^2}$$

**Passo 3.** Quindi:

$$\sum_{k=1}^{\infty} k \cdot q^{k-1} = \frac{1}{(1-q)^2}$$

**Passo 4.** Sostituendo nella formula della media e ricordando che $1-q = p$:

$$E[X] = p \cdot \frac{1}{(1-q)^2} = p \cdot \frac{1}{p^2} = \frac{1}{p}$$

$$\boxed{E[X] = \frac{1}{p}}$$

> [!example] Esempio: roulette — tempo alla prima vincita
> Un giocatore scommette sul rosso alla roulette europea ($p = 18/37 \approx 0{,}486$). In media, quante giocate deve fare per vincere la prima volta?
> $$E[X] = \frac{1}{18/37} = \frac{37}{18} \approx 2{,}06 \text{ giocate}$$

> [!example] Esempio: lancio di un dado — aspettare il 6
> Qual è il numero medio di lanci di un dado onesto necessari per ottenere il primo $6$? Qui $p = 1/6$:
> $$E[X] = \frac{1}{1/6} = 6 \text{ lanci}$$

> [!warning] Proprietà di assenza di memoria (memoryless)
> La distribuzione geometrica gode della **proprietà di assenza di memoria**: il fatto di aver già fallito $n$ prove non cambia la distribuzione del tempo residuo al primo successo.
> $$P(X > n + m \mid X > n) = P(X > m), \qquad \forall\, n, m \geq 0$$
> Intuitivamente: "le prove passate non influenzano il futuro". Se sto aspettando il primo $6$ e ho già fatto 10 lanci senza successo, il numero medio di lanci rimanenti è ancora $6$, non $6 - 10$. La geometrica è l'**unica** distribuzione discreta con questa proprietà.

---

## Esercizio: Tre Dadi e il Teorema di Bayes

### Testo del problema

Si dispone di 3 dadi: **2 onesti** (ciascuna faccia esce con probabilità $1/6$) e **1 truccato** (il $6$ esce con probabilità $1/2$, le altre 5 facce escono con probabilità $1/10$ ciascuna). Si sceglie un dado a caso con uguale probabilità ($1/3$ per ciascun dado) e lo si lancia una volta. Esce il numero $6$.

**Domanda:** qual è la probabilità che il dado utilizzato sia quello truccato?

### Soluzione con il teorema di Bayes

**Definizione degli eventi:**
- $T$: il dado scelto è quello truccato
- $O$: il dado scelto è uno dei due onesti
- $S$: il risultato del lancio è $6$ (il "sei")

**Passo 1 — Probabilità a priori.** Prima del lancio, non abbiamo alcuna informazione su quale dado sia stato scelto. La scelta è equiprobabile fra i 3 dadi:

$$P(T) = \frac{1}{3}, \qquad P(O) = \frac{2}{3}$$

**Passo 2 — Verosimiglianze (likelihood).** La probabilità di osservare $6$ dato il tipo di dado scelto:

$$P(S \mid T) = \frac{1}{2} \qquad \text{(il dado truccato fa uscire il 6 con probabilità 1/2)}$$

$$P(S \mid O) = \frac{1}{6} \qquad \text{(un dado onesto fa uscire il 6 con probabilità 1/6)}$$

**Passo 3 — Probabilità totale.** La probabilità complessiva di osservare $6$ (indipendentemente dal dado) si calcola con il **teorema della probabilità totale**:

$$P(S) = P(S \mid T) \cdot P(T) + P(S \mid O) \cdot P(O) = \frac{1}{2} \cdot \frac{1}{3} + \frac{1}{6} \cdot \frac{2}{3}$$

$$= \frac{1}{6} + \frac{2}{18} = \frac{1}{6} + \frac{1}{9} = \frac{3}{18} + \frac{2}{18} = \frac{5}{18}$$

**Passo 4 — Applicazione del teorema di Bayes.** La probabilità **a posteriori** che il dado sia truccato, dato che è uscito $6$:

$$P(T \mid S) = \frac{P(S \mid T) \cdot P(T)}{P(S)} = \frac{\frac{1}{2} \cdot \frac{1}{3}}{\frac{5}{18}} = \frac{\frac{1}{6}}{\frac{5}{18}} = \frac{1}{6} \cdot \frac{18}{5} = \frac{18}{30} = \frac{3}{5}$$

$$\boxed{P(T \mid S) = \frac{3}{5} = 60\%}$$

**Verifica di coerenza.** Calcoliamo anche $P(O \mid S)$ per verificare che le probabilità a posteriori sommino a $1$:

$$P(O \mid S) = \frac{P(S \mid O) \cdot P(O)}{P(S)} = \frac{\frac{1}{6} \cdot \frac{2}{3}}{\frac{5}{18}} = \frac{\frac{2}{18}}{\frac{5}{18}} = \frac{2}{5} = 40\%$$

$$P(T \mid S) + P(O \mid S) = \frac{3}{5} + \frac{2}{5} = 1 \quad \checkmark$$

> [!warning] L'aggiornamento bayesiano: a priori vs a posteriori
> Prima del lancio, la probabilità che il dado fosse truccato era $P(T) = 1/3 \approx 33\%$. Dopo aver osservato l'uscita del $6$, la probabilità è salita a $P(T \mid S) = 3/5 = 60\%$. L'osservazione ha **aggiornato** la nostra credenza: poiché il $6$ è molto più probabile con il dado truccato ($1/2$ vs $1/6$), la sua uscita è un'evidenza a favore dell'ipotesi "dado truccato".

> [!tip]
> "Bayes è questo: prima di vedere i dati avete un'opinione — la probabilità a priori. Poi vedete i dati e aggiornate l'opinione — ottenete la probabilità a posteriori. Se i dati sono coerenti con la vostra ipotesi, la probabilità sale; se non lo sono, scende. Questo è il cuore dell'inferenza statistica."

---

## PMF Condizionata

### Definizione formale

> [!abstract] Definizione: PMF condizionata
> Sia $X$ una variabile aleatoria discreta con alfabeto $\mathcal{X}$ e sia $A$ un evento con $P(A) > 0$. La **PMF condizionata** di $X$ dato l'evento $A$ è:
> $$P_{X \mid A}(x) = P(X = x \mid A) = \frac{P\big(\{X = x\} \cap A\big)}{P(A)}, \qquad x \in \mathcal{X}$$
> dove $\{X = x\}$ è l'evento "la variabile aleatoria $X$ assume il valore $x$".
>
> La PMF condizionata è essa stessa una PMF valida: è non-negativa e la somma su tutto l'alfabeto dà $1$.

**Interpretazione.** Condizionare all'evento $A$ equivale a **restringere** lo spazio dei campioni $\Omega$ al sottoinsieme $A$ e ricalcolare le probabilità nel nuovo universo. I valori di $X$ che sono incompatibili con $A$ ricevono probabilità condizionata nulla; quelli compatibili vedono la loro probabilità aumentare proporzionalmente.

> [!example] Esempio: dado condizionato a "pari"
> Sia $X$ il risultato di un dado onesto. La PMF incondizionata è $P_X(k) = 1/6$ per $k = 1, 2, \ldots, 6$.
>
> Supponiamo di sapere che è uscito un numero **pari**: $A = \{2, 4, 6\}$, con $P(A) = 3/6 = 1/2$. La PMF condizionata è:
> $$P_{X \mid A}(k) = \begin{cases} \displaystyle\frac{1/6}{1/2} = \frac{1}{3} & \text{se } k \in \{2, 4, 6\} \\[6pt] 0 & \text{se } k \in \{1, 3, 5\} \end{cases}$$
> Lo spazio dei campioni si è ristretto da $\{1, 2, 3, 4, 5, 6\}$ a $\{2, 4, 6\}$: i tre valori pari diventano equiprobabili tra loro, con probabilità $1/3$ ciascuno.

### Connessione con l'esercizio dei dadi e Bayes

Nell'esercizio con i 3 dadi, il passaggio dalla probabilità a priori alla probabilità a posteriori è esattamente un condizionamento:

- **PMF a priori** del tipo di dado: $P(T) = 1/3$, $P(O) = 2/3$
- **PMF a posteriori** (condizionata all'uscita del $6$): $P(T \mid S) = 3/5$, $P(O \mid S) = 2/5$

Il teorema di Bayes fornisce il meccanismo per passare dalla PMF incondizionata alla PMF condizionata quando l'evento di condizionamento riguarda un'osservazione e si vuole aggiornare la distribuzione su un'ipotesi.

**In generale**, se $H_1, H_2, \ldots, H_n$ sono ipotesi mutualmente esclusive ed esaustive (una partizione dello spazio), e $D$ è un dato osservato:

$$P(H_i \mid D) = \frac{P(D \mid H_i) \cdot P(H_i)}{\sum_{j=1}^{n} P(D \mid H_j) \cdot P(H_j)}$$

Questa formula consente di passare dalla PMF a priori $\{P(H_i)\}$ alla PMF a posteriori $\{P(H_i \mid D)\}$.

---

## Cenni sugli Outlier nell'Analisi dei Dati

> [!warning] Outlier e sensibilità della media
> La media statistica è molto sensibile ai **valori anomali** (outlier). Un singolo valore estremo nella distribuzione (o nel campione) può spostare significativamente la media, rendendola un indicatore poco rappresentativo del "centro" della distribuzione. Nella pratica dell'analisi dei dati, questo è un problema serio.

> [!example] Esempio: stipendi in un'azienda
> In un'azienda ci sono 9 dipendenti con stipendio annuo di 30.000 euro e 1 dirigente con stipendio di 300.000 euro. La media degli stipendi è:
> $$\bar{x} = \frac{9 \cdot 30.000 + 300.000}{10} = \frac{270.000 + 300.000}{10} = \frac{570.000}{10} = 57.000 \text{ euro}$$
> Ma 57.000 euro non rappresenta nessuno: il 90% dei dipendenti guadagna circa la metà della media, e il dirigente guadagna più di cinque volte la media. La **mediana** (30.000 euro, il valore che divide la distribuzione a metà) sarebbe in questo caso un indicatore molto più informativo.

Per questo motivo, nella pratica, accanto alla media si calcolano sempre altri indicatori:

- La **mediana**: il valore che divide la distribuzione a metà (il 50% dei dati sta sopra, il 50% sotto). È robusta rispetto agli outlier.
- La **varianza** (che vedremo nelle prossime lezioni): misura la dispersione dei dati attorno alla media. Se la varianza è alta, la media da sola è poco informativa.

> [!tip]
> "Se uno mette la testa nel forno e i piedi nel congelatore, in media sta bene. Ecco perché la media da sola non basta: bisogna sempre guardare anche quanto i dati si disperdono attorno ad essa."

---

> [!abstract] Punti chiave della lezione
> - Il **valore atteso** $E[X] = \sum_k a_k P_X(a_k)$ è il baricentro della distribuzione e il limite della media campionaria per la legge dei grandi numeri.
> - **Bernoulli** $\text{Ber}(p)$: l'esperimento più semplice (successo/fallimento), con media $E[X] = p$.
> - **Binomiale** $\text{Bin}(n,p)$: somma di $n$ Bernoulli indipendenti, PMF $= \binom{n}{k}p^k(1-p)^{n-k}$, media $= np$.
> - **Uniforme** discreta: tutti i valori equiprobabili, media = media aritmetica dell'alfabeto.
> - **Poisson** $\text{Poi}(\lambda)$: distribuzione degli eventi rari, PMF $= \frac{\lambda^k}{k!}e^{-\lambda}$, media $= \lambda$. Si applica a code, traffico, reti.
> - **Geometrica** $\text{Geo}(p)$: tempo al primo successo, PMF $= (1-p)^{k-1}p$, media $= 1/p$. Unica distribuzione discreta con assenza di memoria.
> - Il **teorema di Bayes** permette di aggiornare la probabilità a priori di un'ipotesi dopo aver osservato dei dati, ottenendo la probabilità a posteriori.
> - La **PMF condizionata** restringe lo spazio dei campioni e ridistribuisce le probabilità.
> - La media è sensibile agli **outlier**: nella pratica va sempre affiancata da mediana e varianza.

---
#MSI #variabili-aleatorie #valore-atteso #Bernoulli #binomiale #uniforme #Poisson #geometrica #Bayes #PMF-condizionata #outlier 

---
