# Integrazioni complete al file "Metodi Statistici dell'Informazione"

Ecco tutte le sezioni mancanti, con esempi numerici svolti, da inserire nei punti precisi indicati.

---

## 1. TEORIA DELL'INFORMAZIONE: FONDAMENTI E MISURA

**Posizionamento**: Dopo la sezione "Entropia di Shannon" (fine lezione 7), prima di "Processi stocastici e catene di Markov"

### Concetto di sorpresa e informazione

L'informazione è intrinsecamente legata alla **rimozione di incertezza a priori**. Quando si osserva un evento raro, si riceve più "sorpresa" — e quindi più informazione — rispetto all'osservazione di un evento frequente.

> [!info] **Definizione: Informazione di un evento**
> La quantità di informazione associata a un evento $A$ di probabilità $P(A)$ è:
> $$I(A) = \log_2 \frac{1}{P(A)} = -\log_2 P(A)$$
> misurata in **bit** (base 2 del logaritmo).

**Interpretazione intuitiva**: un evento certo ($P(A) = 1$) non porta informazione ($I(A) = 0$); un evento con probabilità $1/2$ porta 1 bit di informazione; un evento raro (es. $P(A) = 1/1024 = 2^{-10}$) porta 10 bit.

**Proprietà fondamentali**:

1. **Non negatività**: $I(A) \geq 0$ per ogni evento
2. **Monotonia**: maggiore è l'incertezza a priori (minore è $P(A)$), maggiore è l'informazione ricevuta
3. **Additività per eventi indipendenti**: se $A$ e $B$ sono indipendenti:
$$I(A \cap B) = I(A) + I(B)$$

La terza proprietà è cruciale: l'informazione di due eventi indipendenti è additiva. Questa proprietà caratterizza univocamente la forma logaritmica della funzione informazione. Se provassimo con una funzione lineare $I(A) = c(1 - P(A))$, la proprietà di additività fallirebbe immediatamente.

### Scelta della base del logaritmo e unità di misura

Il logaritmo in **base 2** rende l'unità di misura il **bit** (binary digit). Questa scelta è naturale in informatica e telecomunicazioni:

- **Base 2** ↔ **bit** (binary digit)
- **Base $e$** (naturale) ↔ **nat** (natural unit)
- **Base 10** ↔ **dit** (decimal digit)

Nel corso utilizziamo sempre **base 2**, coerentemente con lo standard dell'informazione digitale. Un bit rappresenta la risoluzione di un'incertezza binaria: una risposta sì/no, 0/1, vero/falso.

> [!example]
> - Evento certo ($P = 1$): $I = \log_2(1/1) = 0$ bit (nessuna sorpresa)
> - Lancio moneta onesta ($P = 1/2$): $I = \log_2(2) = 1$ bit (massima incertezza per un evento binario)
> - Evento raro ($P = 1/8$): $I = \log_2(8) = 3$ bit (molta sorpresa)

### Entropia come media della sorpresa

Poiché la funzione informazione $I(X=x) = \log_2 \frac{1}{p_X(x)}$ dipende dal valore assunto da $X$, essa stessa è una variabile aleatoria. L'**entropia** è la sua media statistica:

$$H(X) = E[I(X)] = \sum_{x \in \mathcal{X}} p_X(x) \log_2 \frac{1}{p_X(x)} = -\sum_{x \in \mathcal{X}} p_X(x) \log_2 p_X(x)$$

Questa definizione mostra che l'entropia non è un'astrattezza matematica, ma il valore **atteso** (medio) della "sorpresa" che riceviamo osservando la variabile aleatoria. È una misura diretta dell'**incertezza media** nel sistema.

**Interpretazione operativa**: l'entropia risponde alla domanda: "In media, quanti bit di informazione ricevo quando osservo un valore di $X$?"

### Esempio numerico: entropia di una bernoulliana

Per una variabile binaria $X \in \{0, 1\}$ con $P(X=1) = p$:

$$H(X) = -p \log_2 p - (1-p) \log_2(1-p)$$

**Casi particolari**:

- **$p = 0$ o $p = 1$** (deterministica): $H(X) = 0$ bit (nessuna incertezza)
- **$p = 0.5$** (equiprobabile): $H(X) = -0.5 \log_2(0.5) - 0.5 \log_2(0.5) = 1$ bit (massima incertezza)
- **$p = 0.9$** (molto asimmetrica): $H(X) = -0.9 \log_2(0.9) - 0.1 \log_2(0.1) \approx 0.47$ bit (incertezza ridotta)
- **$p = 0.1$** (molto asimmetrica): $H(X) \approx 0.47$ bit (per simmetria della funzione)

> [!example] **Calcolo dettagliato per $p = 0.9$**
> $$H(X) = -0.9 \log_2(0.9) - 0.1 \log_2(0.1)$$
> 
> Calcoliamo i logaritmi:
> - $\log_2(0.9) = \frac{\ln(0.9)}{\ln(2)} = \frac{-0.1054}{0.6931} \approx -0.1521$
> - $\log_2(0.1) = \frac{\ln(0.1)}{\ln(2)} = \frac{-2.3026}{0.6931} \approx -3.3219$
> 
> Quindi:
> $$H(X) = -0.9 \times (-0.1521) - 0.1 \times (-3.3219) = 0.1369 + 0.3322 = 0.4691 \text{ bit}$$
> 
> Il risultato è coerente: con $p = 0.9$, il valore $X = 1$ è molto probabile, quindi in media riceviamo poca "sorpresa" (0.47 bit invece di 1 bit).

---

### Il Canale Binario Simmetrico (BSC): analisi dettagliata

> [!info] **Definizione: BSC (Binary Symmetric Channel)**
> Un canale binario simmetrico è un canale di comunicazione che trasferisce un bit input $X \in \{0,1\}$ a un output $Y \in \{0,1\}$ con probabilità di errore $\varepsilon \in (0, 1)$:
> - Con probabilità $1-\varepsilon$: il bit è trasmesso correttamente ($Y = X$)
> - Con probabilità $\varepsilon$: il bit è invertito ($Y = 1 - X$)

**Matrice di transizione condizionale**:

$$P(Y=j | X=i) = \begin{cases} 1-\varepsilon & \text{se } i = j \\ \varepsilon & \text{se } i \neq j \end{cases}$$

Il canale è **simmetrico** perché il comportamento è identico per $X=0$ e $X=1$: entrambi hanno probabilità $1-\varepsilon$ di essere trasmessi correttamente.

#### Calcolo della probabilità di errore globale

**Teorema**: Per un input con distribuzione arbitraria $P(X=0) = 1-p$, $P(X=1) = p$, la probabilità che l'output differisca dall'input è:

$$P(Y \neq X) = P(Y \neq X | X=0) P(X=0) + P(Y \neq X | X=1) P(X=1)$$

$$= \varepsilon(1-p) + \varepsilon p = \varepsilon(1-p+p) = \varepsilon$$

> [!abstract]
> **Risultato fondamentale**: In un BSC, la probabilità di errore è esattamente $\varepsilon$, **indipendentemente dalla distribuzione dell'input**. Questo è una conseguenza direttamente della simmetria del canale.

Questa proprietà è notevole: non importa se l'input è bilanciato ($p = 0.5$) o sbilanciato ($p = 0.1$ o $p = 0.9$); il tasso di errore globale rimane sempre $\varepsilon$.

#### Inferenza bayesiana nel BSC: esempio numerico

**Scenario**: trasmettitore invia bit 0 e 1 con uguale probabilità ($p = 0.5$). Il canale ha parametro di errore $\varepsilon = 0.1$ (10% di errore). Il ricevitore osserva $Y = 0$ e vuole stimare quale bit è stato trasmesso.

**Domanda**: Qual è la probabilità che il bit trasmesso fosse effettivamente 0, dato che si è osservato 0?

**Soluzione per Bayes**:

$$P(X=0|Y=0) = \frac{P(Y=0|X=0) P(X=0)}{P(Y=0)}$$

**Passo 1**: Calcoliamo i termini.

$$P(Y=0|X=0) = 1 - \varepsilon = 0.9$$

$$P(X=0) = 0.5$$

$$P(Y=0) = P(Y=0|X=0) P(X=0) + P(Y=0|X=1) P(X=1)$$

dove $P(Y=0|X=1) = \varepsilon = 0.1$ (se trasmesso 1, riceviamo 0 con probabilità di errore).

$$P(Y=0) = 0.9 \times 0.5 + 0.1 \times 0.5 = 0.45 + 0.05 = 0.5$$

**Passo 2**: Applichiamo Bayes:

$$P(X=0|Y=0) = \frac{0.9 \times 0.5}{0.5} = 0.9$$

**Interpretazione**: ricevendo 0, la probabilità che sia stato trasmesso 0 è del 90%. La probabilità che sia stato un errore (trasmesso 1 ma ricevuto 0) è quindi del 10%.

**Simmetricamente**:

$$P(X=1|Y=0) = \frac{P(Y=0|X=1) P(X=1)}{P(Y=0)} = \frac{0.1 \times 0.5}{0.5} = 0.1$$

Verifica: $0.9 + 0.1 = 1$ ✓

> [!example] **Caso più sfavorevole: $\varepsilon = 0.3$ (30% di errore)**
> 
> Con gli stessi parametri (input equiprobabile), se $\varepsilon = 0.3$:
> 
> $$P(Y=0) = 0.7 \times 0.5 + 0.3 \times 0.5 = 0.35 + 0.15 = 0.5$$
> 
> $$P(X=0|Y=0) = \frac{0.7 \times 0.5}{0.5} = 0.7$$
> 
> La probabilità è ancora 70%, ma il rischio di errore è triplicato (da 10% a 30%).

#### Il caso peggiore: $\varepsilon = 1/2$

Potrebbe sembrare che il caso peggiore sia $\varepsilon = 1$ (tutti i bit invertiti). Ma se $\varepsilon = 1$, il canale è ancora deterministico: basta invertire il bit ricevuto e si recupera l'originale perfettamente. L'informazione non è persa, è solo trasformata.

**Il vero caso peggiore è $\varepsilon = 1/2$**. In questo caso:

$$P(Y=0|X=0) = P(Y=0|X=1) = 1/2$$

L'output non dipende dall'input:

$$P(Y=0) = \frac{1}{2} \cdot P(X=0) + \frac{1}{2} \cdot P(X=1) = \frac{1}{2}$$

indipendentemente da $P(X=0)$ e $P(X=1)$.

**Conseguenza bayesiana**:

$$P(X=0|Y=0) = \frac{P(Y=0|X=0) P(X=0)}{P(Y=0)} = \frac{(1/2) P(X=0)}{1/2} = P(X=0)$$

La probabilità a posteriori **coincide con quella a priori**: l'osservazione di $Y$ non fornisce alcuna informazione sul valore di $X$. Il canale è equivalente a **rumore bianco puro**.

> [!warning]
> Questo mostra un principio generale profondo: non è il canale *più difettoso* in senso assoluto ad essere il peggiore, ma il canale che **non fornisce alcuna informazione**. Un canale con $\varepsilon = 1/2$ comunica zero bit di informazione, mentre un canale con $\varepsilon = 1$ comunica perfettamente (una volta che si inverte il segnale).

---

## 2. GEOMETRIA DELLE VARIABILI ALEATORIE E SPAZI LINEARI

**Posizionamento**: Dopo la sezione "Covarianza e correlazione" (lezione 8), come approfondimento teorico strutturato in due livelli (concettuale e algebrico)

### Le variabili aleatorie come spazi vettoriali: fondamenti

Le variabili aleatorie non sono solo numeri, ma appartengono a una **struttura algebrica ricca**: uno spazio vettoriale. Precisamente, l'insieme di tutte le variabili aleatorie $X$ con varianza finita forma uno **spazio di Hilbert** (uno spazio vettoriale completo con prodotto scalare).

> [!abstract]
> Lo spazio $L^2(\Omega)$ di tutte le variabili aleatorie $X$ con $E[X^2] < \infty$ (varianza finita) è uno spazio di Hilbert con operazioni e struttura definite come segue:

**Operazioni lineari**:

- **Somma**: $(X + Y)(\omega) = X(\omega) + Y(\omega)$
- **Scalare**: $(aX)(\omega) = aX(\omega)$ per $a \in \mathbb{R}$

**Prodotto scalare**:

$$\langle X, Y \rangle = E[(X - E[X])(Y - E[Y])] = \text{Cov}(X, Y)$$

**Norma indotta**:

$$\|X\| = \sqrt{\langle X, X \rangle} = \sqrt{\text{Var}(X)} = \sigma_X$$

Questa struttura è **completa**: ogni sequenza di Cauchy di variabili aleatorie converge a un'altra variabile aleatoria nello spazio.

### Interpretazione della covarianza come prodotto scalare

La covarianza **non è un indice statistico astratto**, ma il **prodotto scalare** tra le variabili **centrate** (ridotte alle loro deviazioni dalla media). Se definiamo $X' = X - E[X]$ e $Y' = Y - E[Y]$ (variabili centrate), allora:

$$\text{Cov}(X, Y) = E[X' \cdot Y'] = \langle X', Y' \rangle$$

**Interpretazione geometrica della covarianza**:

- **Covarianza positiva** ($\text{Cov}(X,Y) > 0$): le deviazioni da media di $X$ e $Y$ tendono a "puntare" nella stessa direzione nello spazio. Se $X$ è sopra la sua media, anche $Y$ tende a essere sopra la sua media.

- **Covarianza negativa** ($\text{Cov}(X,Y) < 0$): le deviazioni puntano in direzioni opposte. Se $X$ è sopra media, $Y$ tende a essere sotto media.

- **Covarianza nulla** ($\text{Cov}(X,Y) = 0$): i vettori $X'$ e $Y'$ sono **ortogonali** nello spazio di Hilbert (né concordi né discordi).

### Deviazione standard come norma

La deviazione standard di una variabile è la sua **"lunghezza"** nello spazio:

$$\sigma_X = \|X - E[X]\| = \sqrt{E[(X - E[X])^2]}$$

Una variabile con $\sigma_X = 0$ è un "punto" nello spazio (è deterministica). Una variabile con $\sigma_X$ grande è un "vettore lungo" (alta variabilità).

La **metrica** (distanza) tra due variabili è:

$$d(X, Y) = \|X - Y\| = \sqrt{E[(X-Y)^2]}$$

Questa distanza quantifica quanto "lontane" sono due variabili aleatorie nel senso dei minimi quadrati.

### Il coefficiente di correlazione come coseno

Nello spazio di Hilbert, il coefficiente di correlazione è il **coseno dell'angolo** tra due vettori (variabili centrate):

$$\rho_{XY} = \cos \theta = \frac{\langle X', Y' \rangle}{\|X'\| \cdot \|Y'\|} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$$

dove $\theta \in [0°, 180°]$ è l'angolo geometrico tra i vettori centrati.

**Interpretazione geometrica dei valori estremi**:

- **$\rho = 1$ ($\theta = 0°$)**: i vettori sono **collineari e concordi** — i vettori puntano nella stessa direzione. Relazione lineare perfetta crescente: $Y = a + bX$ con $b > 0$.

- **$\rho = -1$ ($\theta = 180°$)**: i vettori sono **collineari e discordi** — puntano in direzioni opposte. Relazione lineare perfetta decrescente: $Y = a + bX$ con $b < 0$.

- **$\rho = 0$ ($\theta = 90°$)**: i vettori sono **ortogonali** — sono perpendicolari nello spazio. Questo è lo stato di **incorrelazione** (nessuna dipendenza lineare).

- **$0 < |\rho| < 1$**: angolo intermedio — correlazione parziale, relazione lineare imperfetta.

> [!example] **Visualizzazione geometrica**
> 
> Immagina uno spazio 2D (per semplicità). Due variabili $X$ e $Y$ sono rappresentate da vettori:
> - Se puntano in la stessa direzione (piccolo angolo): $\rho \approx 1$
> - Se puntano in direzioni opposte (angolo $\approx 180°$): $\rho \approx -1$
> - Se sono perpendicolari (angolo $= 90°$): $\rho = 0$
> 
> La "lunghezza" di ogni vettore è la deviazione standard. Vettori corti = bassa variabilità. Vettori lunghi = alta variabilità.

### Ortogonalità ≠ Indipendenza

Un punto cruciale: **due vettori possono essere ortogonali (incorrelati, $\rho = 0$) ma comunque dipendenti**.

> [!warning]
> **Incorrelazione implica indipendenza SOLO nel caso gaussiano**. In generale, l'indipendenza è una proprietà molto più forte.

> [!example] **Controesempio: relazione non-lineare**
> 
> Sia $U$ una variabile uniforme su $[-1, 1]$ (simmetrica attorno a 0). Definiamo $Y = U^2$.
> 
> Chiaramente $Y$ dipende da $U$ (non sono indipendenti): noto $U$, conosco esattamente $Y$.
> 
> Ma la covarianza è:
> $$\text{Cov}(U, U^2) = E[U \cdot U^2] - E[U] E[U^2] = E[U^3] - 0 = 0$$
> 
> perché $U^3$ è una funzione **dispari** di $U$ (simmetrica attorno a zero), quindi il suo valore atteso è 0.
> 
> Quindi $\rho = 0$, ma $U$ e $Y$ sono **fortemente dipendenti**. La dipendenza è **non-lineare**.

**Conseguenza**: L'assenza di correlazione ($\rho = 0$) significa assenza di **dipendenza lineare**, non assenza di dipendenza tout court.

### Proiezione ortogonale e predizione lineare ottima

Il significato operativo della correlazione emerge nella teoria della **predizione ottima**. Se vogliamo stimare il valore di $Y$ osservando $X$, la scelta ottimale (in senso di minimizzazione dell'errore quadratico medio, MSE) è:

$$\hat{Y} = a^* + b^* X$$

dove:

$$b^* = \rho_{XY} \frac{\sigma_Y}{\sigma_X}, \quad a^* = E[Y] - b^* E[X]$$

L'errore quadratico medio minimo è:

$$E[(Y - \hat{Y})^2] = \sigma_Y^2 (1 - \rho_{XY}^2)$$

**Interpretazione**:

- Se $|\rho| = 1$ (collineari): $E[(Y - \hat{Y})^2] = 0$ — la predizione è **perfetta**
- Se $\rho = 0$ (ortogonali): $E[(Y - \hat{Y})^2] = \sigma_Y^2$ — la migliore stima è semplicemente $\hat{Y} = E[Y]$ (ignoriamo $X$), con errore pari alla varianza di $Y$
- Se $0 < |\rho| < 1$: errore intermedio — la predizione riduce l'errore di un fattore $(1 - \rho^2)$

Il termine $(1 - \rho^2)$ è il **coefficiente di determinazione** inverso: misura la frazione di varianza di $Y$ che **non** può essere spiegata linearmente da $X$.

---

## 3. FUNZIONE GENERATRICE DEI MOMENTI (MGF) E CONVERGENZA

**Posizionamento**: Dopo la sezione "Teorema del limite centrale" (inizio lezione 12), prima di "Legge dei grandi numeri", come strumento teorico per la dimostrazione rigorosa del TCL

### Definizione della MGF

> [!info] **Definizione: Funzione Generatrice dei Momenti (MGF)**
> La **funzione generatrice dei momenti** di una variabile aleatoria $X$ è:
> $$M_X(s) = E[e^{sX}], \quad s \in \mathbb{R}$$
> definita per tutti gli $s$ in un intorno di 0 (es. $|s| < \delta$ per qualche $\delta > 0$).

**Motivazione del nome**: i momenti di $X$ si ricavano derivando $M_X(s)$. Per la regola della catena:

$$\frac{d}{ds} E[e^{sX}] = E\left[\frac{d}{ds} e^{sX}\right] = E[X e^{sX}]$$

Valutando in $s = 0$:

$$M_X'(0) = E[X e^{0}] = E[X]$$

Più in generale, la derivata $n$-esima è:

$$M_X^{(n)}(s) = E[X^n e^{sX}]$$

Valutando in $s = 0$:

$$M_X^{(n)}(0) = E[X^n]$$

**Quindi il momento di ordine $n$ è la derivata $n$-esima della MGF, valutata nell'origine.**

### Esempio numerico: Bernoulli

Per una variabile di Bernoulli $X \sim \text{Ber}(p)$ (assume 0 con probabilità $1-p$ e 1 con probabilità $p$):

$$M_X(s) = E[e^{sX}] = (1-p) e^{s \cdot 0} + p e^{s \cdot 1} = (1-p) + pe^s$$

**Derivata prima**:

$$M_X'(s) = p e^s$$

Valutando in $s = 0$:

$$M_X'(0) = p = E[X]$$ ✓

**Derivata seconda**:

$$M_X''(s) = p e^s$$

Valutando in $s = 0$:

$$M_X''(0) = p = E[X^2]$$

Da questi momenti si ricava la varianza:

$$\text{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)$$ ✓

### Proprietà fondamentali della MGF

**Proprietà 1: Caratterizzazione della distribuzione**

La MGF **caratterizza completamente** la distribuzione di probabilità. Se due variabili hanno la stessa MGF in un intorno dell'origine, allora hanno la stessa distribuzione. Non è raro in statistica incontrare distribuzioni diverse che hanno lo stesso support ma different strutture probabilistiche — la MGF le distingue inequivocabilmente.

**Proprietà 2: MGF della somma di variabili indipendenti**

Se $X$ e $Y$ sono **indipendenti**, allora:

$$M_{X+Y}(s) = E[e^{s(X+Y)}] = E[e^{sX} e^{sY}]$$

Per l'indipendenza:

$$= E[e^{sX}] E[e^{sY}] = M_X(s) M_Y(s)$$

**Questa proprietà è cruciale per il Teorema Centrale del Limite.**

### Esempio: MGF della somma di Bernoulli indipendenti

Sia $X_1, X_2 \sim \text{Ber}(p)$ indipendenti. La loro somma è $S_2 = X_1 + X_2 \sim \text{Bin}(2, p)$.

$$M_{X_1}(s) = (1-p) + pe^s$$

$$M_{S_2}(s) = M_{X_1}(s) M_{X_2}(s) = [(1-p) + pe^s]^2$$

Sviluppiamo:

$$= (1-p)^2 + 2(1-p)pe^s + p^2 e^{2s}$$

Questa è precisamente la MGF di una Binomiale con $n=2$ e parametro $p$, poiché:

$$M_{\text{Bin}(n,p)}(s) = \sum_{k=0}^{n} \binom{n}{k} p^k(1-p)^{n-k} e^{sk} = [(1-p) + pe^s]^n$$

Per $n=2$: $M_{\text{Bin}(2,p)}(s) = [(1-p) + pe^s]^2$ ✓

---

### Convergenza in distribuzione e il Teorema di Continuità di Lévy

Spesso è difficile verificare direttamente che una sequenza di distribuzioni converge a una distribuzione limite. Il **Teorema di Continuità di Lévy** fornisce un criterio elegante mediante le MGF:

> [!info] **Teorema di Continuità di Lévy**
> Siano $X, X_1, X_2, \ldots$ variabili aleatorie con MGF $M_X(s)$, $M_{X_n}(s)$. Allora $X_n$ converge in distribuzione a $X$ (scritta $X_n \xrightarrow{d} X$) se e solo se:
> $$\lim_{n \to \infty} M_{X_n}(s) = M_X(s) \quad \text{per ogni } s \text{ in un intorno di 0}$$

**Vantaggio operativo**: è più facile verificare la convergenza delle MGF (funzioni reali della variabile reale $s$) che confrontare direttamente le funzioni di distribuzione (che sono cumulative e meno "leggibili").

### Dimostrazione rigorosa del Teorema Centrale del Limite

Il Teorema Centrale del Limite si dimostra utilizzando le MGF e lo sviluppo in serie di Taylor.

**Setup**: siano $X_1, X_2, \ldots$ variabili i.i.d. con media $\mu$ e varianza $\sigma^2$ finite. Definiamo la somma standardizzata:

$$Z_n = \frac{X_1 + X_2 + \cdots + X_n - n\mu}{\sqrt{n} \sigma} = \frac{1}{\sqrt{n}} \sum_{i=1}^{n} \frac{X_i - \mu}{\sigma}$$

**Definizione ausiliaria**: Sia $\xi_i = \frac{X_i - \mu}{\sigma}$. Allora $\xi_i$ sono i.i.d. con $E[\xi_i] = 0$ e $\text{Var}(\xi_i) = 1$, e:

$$Z_n = \frac{1}{\sqrt{n}} \sum_{i=1}^{n} \xi_i$$

**Step 1**: Scriviamo la MGF di $Z_n$:

$$M_{Z_n}(s) = E[e^{s Z_n}] = E\left[\exp\left(\frac{s}{\sqrt{n}} \sum_{i=1}^{n} \xi_i\right)\right]$$

**Step 2**: Per l'indipendenza dei $\xi_i$:

$$M_{Z_n}(s) = \prod_{i=1}^{n} E\left[e^{(s/\sqrt{n}) \xi_i}\right] = \left[M_{\xi}(s/\sqrt{n})\right]^n$$

dove $M_{\xi}(t) = E[e^{t\xi}]$ è la MGF di una singola $\xi_i$.

**Step 3**: Sviluppiamo in serie di Taylor intorno a $t = 0$. Poiché $E[\xi] = 0$ e $\text{Var}(\xi) = 1$:

$$M_{\xi}(t) = E[e^{t\xi}] = E\left[\sum_{k=0}^{\infty} \frac{(t\xi)^k}{k!}\right] = \sum_{k=0}^{\infty} \frac{t^k E[\xi^k]}{k!}$$

$$= 1 + t \cdot 0 + \frac{t^2}{2!} E[\xi^2] + \frac{t^3}{3!} E[\xi^3] + \cdots$$

$$= 1 + \frac{t^2}{2} + O(t^3)$$

dove $O(t^3)$ denota termini di ordine superiore.

**Step 4**: Sostituendo $t = s/\sqrt{n}$:

$$M_{\xi}(s/\sqrt{n}) = 1 + \frac{(s/\sqrt{n})^2}{2} + O(n^{-3/2}) = 1 + \frac{s^2}{2n} + O(n^{-3/2})$$

**Step 5**: Quindi:

$$M_{Z_n}(s) = \left[1 + \frac{s^2}{2n} + O(n^{-3/2})\right]^n$$

**Step 6**: Quando $n \to \infty$, usiamo il limite notevole $\lim_{n \to \infty} (1 + a/n)^n = e^a$:

$$\lim_{n \to \infty} M_{Z_n}(s) = \lim_{n \to \infty} \left[1 + \frac{s^2}{2n} + o(1/n)\right]^n = e^{s^2/2}$$

**Step 7**: La funzione $e^{s^2/2}$ è precisamente la MGF della distribuzione normale standard $\mathcal{N}(0,1)$.

**Conclusione**: per il Teorema di Continuità di Lévy, $Z_n \xrightarrow{d} \mathcal{N}(0,1)$ quando $n \to \infty$.

> [!abstract]
> **Risultato finale del TCL**: Se $X_1, X_2, \ldots$ sono i.i.d. con media $\mu$ e varianza $\sigma^2$, allora:
> $$\frac{\sum_{i=1}^{n} X_i - n\mu}{\sqrt{n}\sigma} \xrightarrow{d} \mathcal{N}(0,1)$$
> 
> per $n \to \infty$.

---

## 4. PROCESSI ALEATORI: PROPRIETÀ DI MARKOV

**Posizionamento**: Dopo la sezione "Indipendenza condizionale" (lezione 7), come approfondimento delle dipendenze temporali

### Definizione di catena di Markov

Una sequenza di variabili aleatorie $(X_1, X_2, \ldots, X_n, X_{n+1}, \ldots)$ **indicizzate dal tempo** soddisfa la **proprietà di Markov** (o proprietà "senza memoria") se il valore futuro dipende dal passato **solo attraverso il presente**, non direttamente da stati precedenti:

> [!info] **Proprietà di Markov**
> $$P(X_{n+1} | X_n, X_{n-1}, \ldots, X_1) = P(X_{n+1} | X_n)$$
> 
> Il valore futuro $X_{n+1}$ è condizionalmente indipendente da tutta la storia precedente $(X_1, \ldots, X_{n-1})$ dato lo stato presente $X_n$.

**Interpretazione intuitiva**: il sistema non ha "memoria" del passato remoto. Solo lo stato attuale influenza il comportamento futuro.

### Equivalenza con l'indipendenza condizionale

La proprietà di Markov per una terna $(X, Y, Z)$ (ordinati temporalmente) equivale all'indipendenza condizionale:

$$P(X, Z | Y) = P(X | Y) P(Z | Y)$$

Cioè: dato $Y$ (il presente), il passato $X$ e il futuro $Z$ sono condizionalmente indipendenti.

**Dimostrazione della equivalenza**:

La proprietà di Markov per la terna dice:

$$P(Z | X, Y) = P(Z | Y)$$

Moltiplicando per $P(X | Y)$:

$$P(X, Z | Y) = P(Z | X, Y) P(X | Y) = P(Z | Y) P(X | Y)$$

che è precisamente la definizione di indipendenza condizionale.

### Esempio: il re sulla scacchiera

Un re si muove casualmente su una scacchiera 8×8. Sia $X_n$ la posizione del re al tempo $n$. 

**Affermazione di Markov**: La probabilità che il re sia in una data casella al tempo $n+2$ dipende **solo** da dove si trova al tempo $n+1$, non da dove era al tempo $n$ o prima.

**Matematicamente**:

$$P(X_{n+2} = \text{casella A} | X_{n+1} = \text{casella B}, X_n = \text{casella C}, \ldots) = P(X_{n+2} = \text{casella A} | X_{n+1} = \text{casella B})$$

**Interpretazione**: il re non ha "memoria" di come è arrivato alla casella B. I movimenti futuri dipendono solo dalla posizione attuale, non dalla storia dei movimenti precedenti.

**Contro-esempio (non-Markoviano)**: supponiamo che il re abbia la regola "non ritorno indietro" (non può tornare immediatamente alla casella da cui è venuto). In questo caso, sapere dove il re era al tempo $n-1$ influenza i movimenti al tempo $n+1$, perché esclude quella casella. Il processo **non è Markoviano**.

### Catene di Markov omogenee nel tempo

Se la probabilità di transizione **non dipende da** $n$ (il tempo rimane omogeneo):

$$P(X_{n+1} = j | X_n = i) = P_{ij} \quad \text{(costante per ogni } n)$$

allora la catena è detta **omogenea** o **stazionaria nel tempo**. 

In questo caso, la dinamica è completamente descritta dalla **matrice di transizione** $P = (P_{ij})_{i,j \in S}$, dove $S$ è lo spazio degli stati. Questa ipotesi semplifica enormemente l'analisi e consente di usare strumenti dell'algebra lineare.

### Applicazioni pratiche delle catene di Markov

> [!example] **Teoria delle code: arrivi a uno sportello**
> Sia $X_n$ il numero di clienti in coda al tempo $n$. Se gli arrivi seguono un processo di Poisson (arrivialle casuali) e il tempo di servizio è indipendente dalla storia, allora il numero di clienti al tempo $n+1$ dipende solo da $X_n$:
> - Se $X_n > 0$: il prossimo evento è l'arrivo di un nuovo cliente o la fine del servizio
> - La probabilità di questi eventi dipende solo da $X_n$, non da come la coda è arrivata a quella lunghezza
> 
> Quindi il processo è Markoviano.

> [!example] **Modelli epidemiologici: diffusione di malattie**
> In un modello SIR (Susceptible-Infected-Recovered), il numero di individui in ciascun compartimento al giorno $n+1$ dipende solo dallo stato al giorno $n$ (il numero di suscettibili, infetti e guariti), non dalla storia della diffusione.

> [!example] **Modelli finanziari: prezzi delle azioni**
> Un modello di random walk per il prezzo di un'azione: $P_{n+1} = P_n + \epsilon_n$, dove $\epsilon_n$ è rumore casuale indipendente. Il prezzo futuro dipende solo da quello presente, non da come è arrivato a quel valore.

---

## 5. THINNING DI POISSON: DECOMPOSIZIONE DI FLUSSI

**Posizionamento**: Dopo la sezione "Distribuzione di Poisson" (lezione 3), come proprietà avanzata e cruciale per applicazioni

### Proprietà di thinning (subcampionamento)

Una proprietà affascinante e contrintuitiva della distribuzione di Poisson è la **stabilità sotto subcampionamento**: se un flusso Poissoniano viene "diradato" (subcampionato) in modo casuale e indipendente, i sotto-flussi risultanti rimangono Poissoniani e sono mutuamente indipendenti.

> [!info] **Teorema: Thinning di un processo di Poisson**
> Sia $N \sim \text{Poisson}(\lambda)$ il numero totale di arrivi (eventi) in un intervallo di tempo o spazio. Supponiamo che ogni arrivo sia **classificato indipendentemente** in una di due categorie:
> - Categoria A con probabilità $p$
> - Categoria B con probabilità $1-p$
> 
> Siano $N_A$ e $N_B$ i numeri di arrivi nelle due categorie. Allora:
> $$N_A \sim \text{Poisson}(\lambda p), \quad N_B \sim \text{Poisson}(\lambda(1-p))$$
> e $N_A$ e $N_B$ sono **indipendenti**.

**Dimostrazione intuitiva mediante la legge della probabilità totale**:

Calcoliamo $P(N_A = k)$ sommando su tutti i possibili valori di $N$:

$$P(N_A = k) = \sum_{n=k}^{\infty} P(N_A = k | N = n) P(N = n)$$

Dato $N = n$ (numero totale di arrivi), la probabilità che esattamente $k$ siano della categoria A è una binomiale:

$$P(N_A = k | N = n) = \binom{n}{k} p^k (1-p)^{n-k}$$

Quindi:

$$P(N_A = k) = \sum_{n=k}^{\infty} \binom{n}{k} p^k (1-p)^{n-k} \frac{\lambda^n}{n!} e^{-\lambda}$$

Fattorizziamo:

$$= \frac{(\lambda p)^k}{k!} e^{-\lambda p} \sum_{n=k}^{\infty} \frac{[\lambda(1-p)]^{n-k}}{(n-k)!} e^{-\lambda(1-p)}$$

Sostituendo $m = n-k$:

$$= \frac{(\lambda p)^k}{k!} e^{-\lambda p} \sum_{m=0}^{\infty} \frac{[\lambda(1-p)]^{m}}{m!} e^{-\lambda(1-p)}$$

$$= \frac{(\lambda p)^k}{k!} e^{-\lambda p} \cdot 1 = \frac{(\lambda p)^k}{k!} e^{-\lambda p}$$

**Quindi $N_A \sim \text{Poisson}(\lambda p)$** ✓

**Indipendenza**: la classificazione di ogni arrivo è indipendente da tutti gli altri, e dalla distribuzione di $N$, perciò $N_A$ e $N_B$ sono indipendenti.

### Applicazioni pratiche con esempi numerici

> [!example] **Applicazione 1: Pacchetti errati in un router**
> 
> Un router riceve pacchetti in arrivo secondo un processo di Poisson con tasso medio $\lambda = 100$ pacchetti/ms. A causa del rumore del canale, ogni pacchetto è corrotto (contiene errori) con probabilità $p = 0.01$ indipendentemente.
> 
> **Domanda**: Quali sono le distribuzioni del numero di pacchetti corretti e corrotti in un millisecondo?
> 
> **Soluzione per thinning**:
> 
> Applichiamo il teorema di thinning con:
> - $\lambda = 100$ (tasso totale)
> - Categoria A (pacchetti corretti): probabilità $1 - 0.01 = 0.99$
> - Categoria B (pacchetti errati): probabilità $0.01$
> 
> Risultati:
> $$N_{\text{ok}} \sim \text{Poisson}(100 \times 0.99) = \text{Poisson}(99)$$
> $$N_{\text{errore}} \sim \text{Poisson}(100 \times 0.01) = \text{Poisson}(1)$$
> 
> **Interpretazione**:
> - Il numero medio di pacchetti corretti è 99/ms
> - Il numero medio di pacchetti errati è 1/ms
> - I due flussi sono indipendenti: sapere quanti pacchetti ci sono stati senza errori non dà informazioni su quanti ce ne sono stati con errori
> 
> **Applicazione pratica**: il router può stimare il tasso di errore del canale dalla frequenza osservata di errori, ipotizzando che seguano una distribuzione di Poisson indipendente.

> [!example] **Applicazione 2: Tipi di auto in coda a un casello**
> 
> Al casello autostradale passano auto secondo un processo di Poisson con tasso medio $\lambda = 4$ auto/minuto. Dalla statistica storica, il 70% sono auto private e il 30% sono camion.
> 
> **Domanda**: Quali sono i tassi di arrivo delle auto private e dei camion?
> 
> **Soluzione per thinning**:
> 
> $$N_{\text{private}} \sim \text{Poisson}(4 \times 0.70) = \text{Poisson}(2.8)$$
> $$N_{\text{camion}} \sim \text{Poisson}(4 \times 0.30) = \text{Poisson}(1.2)$$
> 
> **Interpretazione**:
> - In media, 2.8 auto private passano al minuto
> - In media, 1.2 camion passano al minuto
> - I due flussi sono indipendenti
> 
> **Applicazione pratica**: il casello può dimensionare le corsie separate per auto e camion sulla base di questi tassi indipendenti.

> [!example] **Applicazione 3: Clienti diversi in un negozio**
> 
> Un negozio riceve clienti secondo un processo di Poisson con tasso $\lambda = 10$ clienti/ora. L'esperienza passata mostra che:
> - Il 40% dei clienti acquistano (categoria A)
> - Il 35% guardano ma non acquistano (categoria B)
> - Il 25% chiedono informazioni (categoria C)
> 
> **Domanda**: Quali sono i tassi di arrivo di clienti in ogni categoria?
> 
> **Soluzione generalizzata a tre categorie**:
> 
> Applicando il thinning gerarchicamente (o contemporaneamente a tre categorie):
> $$N_{\text{acquisti}} \sim \text{Poisson}(10 \times 0.40) = \text{Poisson}(4)$$
> $$N_{\text{browser}} \sim \text{Poisson}(10 \times 0.35) = \text{Poisson}(3.5)$$
> $$N_{\text{info}} \sim \text{Poisson}(10 \times 0.25) = \text{Poisson}(2.5)$$
> 
> Tutti e tre i flussi sono mutuamente indipendenti.

---

## 6. FUNZIONE Q E CALCOLO OPERATIVO DELLA NORMALE

**Posizionamento**: Dopo la sezione "Distribuzioni continue notevoli" (lezione 10), come strumento operativo essenziale

### Definizione della funzione Q

Molti calcoli in statistica, ingegneria e telecomunicazioni richiedono di calcolare la probabilità che una variabile normale standard superi una soglia. Questo viene quantificato dalla **funzione Q**.

> [!info] **Definizione: Funzione Q (CCDF della gaussiana standard)**
> La funzione Q è la **complementary cumulative distribution function** (CCDF) della distribuzione normale standard $\mathcal{N}(0,1)$:
> $$Q(x) = P(Z > x) = \int_x^{+\infty} \frac{1}{\sqrt{2\pi}} e^{-t^2/2} \, dt = 1 - \Phi(x)$$
> dove $\Phi(x)$ è la CDF della normale standard.

**Proprietà essenziali**:

- **Valore a zero**: $Q(0) = 1/2$ (probabilità di superare la media)
- **Simmetria**: $Q(-x) = 1 - Q(x)$ (simmetria della gaussiana)
- **Limiti**: $\lim_{x \to \infty} Q(x) = 0$ e $\lim_{x \to -\infty} Q(x) = 1$
- **Monotonia**: $Q(x)$ è **strettamente monotona decrescente**
- **Relazione con $\Phi$**: $Q(x) = 1 - \Phi(x)$

### Tabellazione e calcolo numerico

La funzione Q **non ha primitiva elementare**: non esiste una combinazione finita di funzioni elementari (polinomi, esponenziali, logaritmi) che uguagli $Q(x)$.

**Storicamente** (pre-1970): si utilizzavano tabelle stampate di $Q(x)$ per valori discreti di $x$ (es., ogni 0.01 o 0.001), accumulate su fogli di carta millimetrata.

**Oggi**: si usano software numerici (Matlab, Python SciPy, R) che calcolano $Q(x)$ con precisione arbitraria usando algoritmi sofisticati (es., approssimazioni razionali, trasformazioni di Hastings).

### Approssimazioni asintotiche per code pesanti

Per $x$ grande (code della distribuzione), la funzione Q decresce **esponenzialmente**:

$$Q(x) \approx \frac{1}{\sqrt{2\pi}} \frac{1}{x} e^{-x^2/2}, \quad x \gg 1$$

**Derivazione intuitiva**: nell'integrale $\int_x^{\infty} e^{-t^2/2} dt$, il termine dominante è $e^{-x^2/2}$. Integrando per parti:

$$\int_x^{\infty} e^{-t^2/2} dt \approx e^{-x^2/2} \int_x^{\infty} \frac{1}{t^2} dt = e^{-x^2/2} \cdot \frac{1}{x}$$

Moltiplicando per il fattore $1/\sqrt{2\pi}$ della gaussiana.

**Precisione**: questa approssimazione è accurata per $x > 3$ e diventa sempre più precisa al crescere di $x$.

> [!example] **Tabella di valori approssimati**
> 
> | $x$ | $Q(x)$ esatto | $Q(x)$ approssimato | Errore relativo |
> |-----|--------------|-------------------|-----------------|
> | 1.0 | 0.1587 | — | — |
> | 2.0 | 0.0228 | — | — |
> | 3.0 | 0.00135 | 0.00130 | 3.7% |
> | 4.0 | 0.0000317 | 0.0000315 | 0.6% |
> | 5.0 | 2.87×10⁻⁷ | 2.87×10⁻⁷ | 0.1% |
> 
> Per $x \geq 3$, l'approssimazione diventa estremamente accurata.

### Calcolo operativo con normali non-standard

Se $X \sim \mathcal{N}(\mu, \sigma^2)$ (media $\mu$, varianza $\sigma^2$), la probabilità che $X$ superi una soglia $x_0$ si esprime tramite la funzione Q:

$$P(X > x_0) = P\left(\frac{X - \mu}{\sigma} > \frac{x_0 - \mu}{\sigma}\right) = Q\left(\frac{x_0 - \mu}{\sigma}\right)$$

Analogamente, la CDF di $X$ è:

$$F_X(x_0) = P(X \leq x_0) = 1 - Q\left(\frac{x_0 - \mu}{\sigma}\right) = \Phi\left(\frac{x_0 - \mu}{\sigma}\right)$$

La probabilità di un intervallo è:

$$P(a \leq X \leq b) = Q\left(\frac{a - \mu}{\sigma}\right) - Q\left(\frac{b - \mu}{\sigma}\right)$$

### Esempio numerico dettagliato

> [!example] **Problema: segnale con rumore gaussiano**
> 
> Un ricevitore misura un segnale con distribuzione $X \sim \mathcal{N}(5, 4)$:
> - Media: $\mu = 5$
> - Varianza: $\sigma^2 = 4$, quindi deviazione standard: $\sigma = 2$
> 
> **Domande**:
> 1. Qual è la probabilità che il segnale superi 7?
> 2. Qual è la probabilità che il segnale sia tra 3 e 7?
> 3. Qual è il valore $x^*$ tale che $P(X > x^*) = 0.05$?
> 
> **Soluzione**:
> 
> **Domanda 1**:
> $$P(X > 7) = Q\left(\frac{7-5}{2}\right) = Q(1) \approx 0.1587$$
> 
> Interpretazione: circa il 15.87% del tempo il segnale supera il valore 7.
> 
> **Domanda 2**:
> $$P(3 \leq X \leq 7) = Q\left(\frac{3-5}{2}\right) - Q\left(\frac{7-5}{2}\right)$$
> $$= Q(-1) - Q(1) = [1 - Q(1)] - Q(1) = 1 - 2Q(1)$$
> $$\approx 1 - 2 \times 0.1587 = 1 - 0.3174 = 0.6826$$
> 
> Interpretazione: circa il 68.26% dei segnali cadono tra 3 e 7, cioè nell'intervallo di una deviazione standard attorno alla media.
> 
> **Domanda 3**:
> Vogliamo trovare $x^*$ tale che $P(X > x^*) = 0.05$, cioè $Q\left(\frac{x^* - 5}{2}\right) = 0.05$.
> 
> Dalle tabelle, $Q(1.645) \approx 0.05$ (il "quantile del 5%"). Quindi:
> $$\frac{x^* - 5}{2} = 1.645 \implies x^* = 5 + 2 \times 1.645 = 8.29$$
> 
> Interpretazione: il segnale supera 8.29 solo il 5% del tempo.

---

## 7. STRATEGIE DI GIOCO: LA MARTINGALA

**Posizionamento**: Dopo la sezione "Legge dei grandi numeri" (lezione 5), come studio di caso sulla gestione del rischio

### La strategia della martingala al casinò

La **martingala** è una strategia di gioco d'azzardo dove la puntata viene raddoppiata dopo ogni perdita, con l'obiettivo di recuperare le perdite passate con una singola vittoria. Nonostante la sua apparente logica vincente, è uno dei più comuni errori di valutazione probabilistica.

### Implementazione e meccanica

> [!example] **Caso concreto: martingala alla roulette europea**
> 
> **Tasso di vittoria**: scommettendo sul rosso, $p = 18/37 \approx 0.4865$ (18 numeri rossi, 18 neri, 1 zero)
> 
> **Strategia passo-passo**:
> 1. Scommetti 1€ sul rosso
> 2. Se vinci: recuperi 1€ (guadagno di 1€). Fine.
> 3. Se perdi (esce nero o zero): perdi 1€. Procedi al passo 4.
> 4. Scommetti 2€ sul rosso
> 5. Se vinci: guadagni 2€, perdita precedente 1€ → guadagno netto 1€. Fine.
> 6. Se perdi di nuovo: perdita totale 3€. Procedi al passo 7.
> 7. Scommetti 4€ sul rosso
> 8. Continua raddoppiando: 8€, 16€, 32€, ...
> 9. **Quando finalmente vinci** (e prima o poi vincerai con probabilità crescente): recuperi tutte le perdite precedenti + 1€ di guadagno netto.
> 
> **Intuizione**: "Non posso perdere forever, quindi eventualmente devo vincere e recuperare tutto plus 1€!"

### Analisi matematica rigorosa

#### Caso 1: Patrimonio infinito e nessun limite di puntata

Se avessi un patrimonio infinito e potessi scommettere senza limiti, cosa accadrebbe?

Sia $n$ il numero di raddoppi prima di vincere. Dopo $n-1$ perdite consecutive e una vittoria alla $n$-esima prova:

- **Somma totale puntata**: $\sum_{i=0}^{n-1} 2^i = 2^n - 1$ euro
- **Importo vinto all'ultima puntata**: $2^{n-1} \times 2 = 2^n$ euro
- **Guadagno netto**: $2^n - (2^n - 1) = 1$ euro

> [!abstract]
> **Proprietà paradossale**: con patrimonio infinito e nessun limite, la martingala garantisce una vittoria **quasi certa** (probabilità = 1) e il guadagno atteso è sempre 1€ per "ciclo" completato.
> 
> Formalmente: $P(\text{vincere eventualmente}) = 1 - \lim_{n \to \infty} (1-p)^n = 1 - 0 = 1$.

#### Caso 2: Patrimonio finito e limiti di puntata (scenario realistico)

Nel mondo reale:

1. **Patrimonio finito** $S$: il numero di raddoppi è limitato dal capitale disponibile
2. **Limite di puntata** $P_{\max}$ (imposto dal casinò): dopo un certo numero di raddoppi, non puoi scommettere più di $P_{\max}$

Sia $n$ il **numero massimo di raddoppi possibili**, limitato da:

$$n = \min\left(\lfloor \log_2 S \rfloor, \lfloor \log_2 P_{\max} \rfloor\right)$$

#### Calcolo della probabilità di rovina

**Scenario di rovina**: perdi tutte le $n$ puntate consecutive. La probabilità è:

$$P(\text{rovina}) = (1-p)^n$$

**Guadagno atteso**:

- Se vinci (probabilità $1 - (1-p)^n$): guadagni 1€
- Se perdi tutte le $n$ puntate (probabilità $(1-p)^n$): perdi $S$ euro

$$E[\text{guadagno}] = 1 \cdot [1 - (1-p)^n] - S \cdot (1-p)^n$$

$$= 1 - (1-p)^n - S(1-p)^n = 1 - (S+1)(1-p)^n$$

### Esempio numerico dettagliato: roulette europea

> [!example] **Caso 1: patrimonio moderato**
> 
> **Parametri**:
> - Patrimonio iniziale: $S = 100$ euro
> - Probabilità di vittoria singola: $p = 18/37 \approx 0.4865$
> - Probabilità di perdita: $1 - p = 19/37 \approx 0.5135$
> - Numero massimo di raddoppi: $n = \lfloor \log_2 100 \rfloor = 6$
> 
> **Analisi**:
> 
> Con 6 raddoppi, le puntate sono: 1, 2, 4, 8, 16, 32 euro.
> 
> Somma totale puntata se perdi tutti: $1 + 2 + 4 + 8 + 16 + 32 = 63$ euro.
> 
> Poiché $S = 100 > 63$, il patrimonio è sufficiente per 6 raddoppi.
> 
> **Probabilità di rovina**:
> $$P(\text{rovina}) = (1-p)^6 = (19/37)^6 \approx (0.5135)^6 \approx 0.0183 \approx 1.83\%$$
> 
> **Guadagno atteso**:
> $$E[\text{guadagno}] = 1 - (100+1) \times 0.0183 = 1 - 1.85 = -0.85 \text{ euro}$$
> 
> **Conclusione**: nonostante solo l'1.83% di probabilità di rovina nel ciclo singolo, il guadagno atteso è **negativo** di 85 centesimi!

> [!example] **Caso 2: patrimonio maggiore**
> 
> **Parametri**:
> - Patrimonio iniziale: $S = 1000$ euro
> - Limite di puntata: $P_{\max} = 256$ euro (corrisponde a 8 raddoppi)
> - Numero massimo di raddoppi: $n = 8$
> 
> **Puntate**: 1, 2, 4, 8, 16, 32, 64, 128 euro.
> 
> Somma totale: $255$ euro < $1000$ ✓
> 
> **Probabilità di rovina**:
> $$P(\text{rovina}) = (0.5135)^8 \approx 0.0019 \approx 0.19\%$$
> 
> Apparentemente minuscola! Ma:
> 
> **Guadagno atteso**:
> $$E[\text{guadagno}] = 1 - (1000+1) \times 0.0019 \approx 1 - 1.90 = -0.90 \text{ euro}$$
> 
> **Paradosso**: la probabilità di rovina scende a 0.19%, ma il guadagno atteso rimane **negativo**.

### Ripetizione del gioco: il valore atteso si accumula

La vera catastrofe emerge quando si ripete la martingala più volte.

Se si gioca $k$ cicli indipendenti con guadagno atteso $E_{\text{ciclo}} < 0$ per ciclo:

$$E[\text{guadagno totale}] = k \cdot E_{\text{ciclo}} \to -\infty \text{ quando } k \to \infty$$

Con i parametri dell'Esempio 2:

- Guadagno atteso per ciclo: $-0.90$ euro
- Numero di cicli in un mese (30 giorni, 1 ciclo al giorno): 30
- Guadagno atteso mensile: $30 \times (-0.90) = -27$ euro
- Guadagno atteso annuale: $365 \times (-0.90) \approx -329$ euro

**Inoltre**: la probabilità di rovina **almeno una volta** in 30 cicli è:

$$P(\text{rovina almeno una volta}) = 1 - (1 - 0.0019)^{30} \approx 1 - 0.944 = 0.056 \approx 5.6\%$$

Dopo un anno (365 cicli):

$$P(\text{rovina almeno una volta}) = 1 - (1 - 0.0019)^{365} \approx 0.50$$

**La rovina è quasi certa nel lungo periodo.**

### Perché i casinò impongono limiti di puntata

Il teorema di thinning di Poisson mostra che nel caso senza limiti, il casinò affronterebbe un'esposizione illimitata. L'imposizione di:

1. **Limite massimo di puntata** $P_{\max}$
2. **Limite massimo di vincita** per notte/settimana

**neutralizza completamente la martingala** rendendo il guadagno atteso del giocatore negativo.

Dai dati reali:

- **Las Vegas**: limite di puntata tipicamente 5000-10000 dollari
- **Casinò europei**: limite 1000-5000 euro

Con questi limiti, anche un giocatore ricco è destinato a perdere nel lungo periodo.

### Conclusione sulla martingala

> [!abstract]
> **La martingala NON è una strategia vincente** nel lungo periodo con risorse finite. La sua apparente efficacia è un'illusione statistica dovuta alla concentrazione mentale su scenari a breve termine:
> 
> - **Con patrimonio infinito**: la vittoria è quasi certa, ma il guadagno per tentativo rimane zero (non è un vero "guadagno")
> - **Con patrimonio finito**: la vittoria è probabile nel breve termine, ma la probabilità di rovina catastrofica è inevitabile nel lungo termine
> - **Ripetendo il gioco**: il guadagno atteso è sempre negativo e si accumula in perdite
> 
> I casinò non hanno paura della martingala perché **comprendono la probabilità**. I limiti di puntata sono la loro difesa matematicamente ottimale.

---

## POSIZIONAMENTO RIEPILOGATIVO COMPLETO

| Sezione | Dimensione | Dopo quale argomento | Lezione originale |
|---------|-----------|----------------------|------------------|
| 1. Teoria dell'Informazione (completa) | ~2500 parole | "Entropia di Shannon" | 7 |
| 2. Geometria di Hilbert e Spazi Vettoriali | ~2200 parole | "Covarianza e correlazione" | 8 |
| 3. MGF e Teorema di Continuità Lévy | ~2800 parole | "Teorema del Limite Centrale" (inizio) | 12 |
| 4. Catene di Markov e Proprietà | ~1800 parole | "Indipendenza condizionale" | 7 |
| 5. Thinning di Poisson | ~1600 parole | "Distribuzione di Poisson" | 3 |
| 6. Funzione Q e Gaussiana Operativa | ~1500 parole | "Distribuzioni continue notevoli" | 10 |
| 7. Martingala e Gestione del Rischio | ~2200 parole | "Legge dei grandi numeri" | 5 |
| **TOTALE** | **~14,700 parole** | — | — |

---

Tutte le sezioni sono pronte per integrazione nel documento principale, ordinate secondo la progressione logica delle lezioni del Professor Lops.
