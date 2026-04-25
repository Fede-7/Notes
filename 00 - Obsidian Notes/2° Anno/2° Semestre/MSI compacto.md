# Capitolo 3: Elements of Probability

## Introduction

La probabilità è lo strumento matematico formale per modellare l'incertezza. Nelle telecomunicazioni e nell'informatica, l'incertezza è intrinseca al concetto stesso di informazione: se non vi fosse incertezza su ciò che viene trasmesso o memorizzato, non vi sarebbe informazione da trasferire. La probabilità permette di descrivere il passaggio da uno stato di incertezza a priori a uno stato di certezza a posteriori, pur rimanendo questa certezza quasi mai assoluta. Tutto ciò che rientra sotto il termine di machine learning, statistical learning, deep learning e reti neurali è costruito su questa base probabilistica.

## Sample Space and Events

> [!info] **Definizione: Esperimento**
> Un esperimento è un'operazione, o un insieme di operazioni, che conduce a uno tra tanti risultati possibili.

> [!info] **Definizione: Spazio dei campioni**
> Lo spazio dei campioni, indicato con $\Omega$, è l'insieme di tutti i possibili risultati di un esperimento.
> $$\Omega = \{\omega_1, \omega_2, \ldots\}$$

Lo spazio dei campioni può avere diverse nature. Può essere finito, come nel lancio di una moneta dove $\Omega = \{T, C\}$. Può essere numerabilmente infinito, come nel caso del numero di pacchetti in coda a un router, dove $\Omega = \mathbb{N}_0$. Infine, può essere non numerabile quando si modellano grandezze continue, come la tensione misurata ai capi di una resistenza dovuta al rumore termico, con $\Omega = \mathbb{R}$.

Nella pratica, qualunque misura fisica è razionale poiché gli strumenti hanno un numero finito di cifre significative. Tuttavia, quando i valori possibili sono così numerosi, conviene modellare il fenomeno come continuo e poi applicare una troncatura numerica. Il tempo viene solitamente schematizzato come continuo, anche se in applicazioni digitali è discretizzato.

> [!info] **Definizione: Evento**
> Un evento è un sottoinsieme di $\Omega$ definito da una proposizione. Un evento elementare è un singolo elemento di $\Omega$.

Un aspetto fondamentale è che l'evento è univocamente determinato dagli elementi di $\Omega$ che lo compongono, ma la proposizione che lo descrive non è univoca. La ridondanza del linguaggio naturale permette formulazioni differenti. Se si hanno in tasca 1, 2, 3, 4 o 5 euro, l'evento $\{1, 3, 5\}$ può essere descritto come "ho un numero dispari di euro", "non ho un numero pari di euro", oppure "ho 1 o 3 o 5 euro". Saper riformulare la proposizione in modo conveniente è spesso la chiave per risolvere un esercizio di probabilità.

Gli eventi hanno una nomenclatura specifica. L'evento certo è $\Omega$ stesso: ogni volta che si compie l'esperimento si ottiene un elemento di $\Omega$. L'evento impossibile è l'insieme vuoto $\emptyset$. L'evento complementare di $A$, indicato con $A^c$ o $\bar{A}$, contiene tutti gli elementi di $\Omega$ non appartenenti ad $A$. Due eventi $A$ e $B$ si dicono incompatibili se $A \cap B = \emptyset$. Si dice che $A$ implica $B$ se $A \subseteq B$: il verificarsi di $A$ implica necessariamente il verificarsi di $B$, ma non viceversa. Nel lancio di un dado, l'evento "esce 2" implica l'evento "esce un numero pari", ma non il contrario.

## Venn Diagrams and the Algebra of Events

Le operazioni sugli insiemi forniscono il linguaggio per combinare eventi. L'unione $A_1 \cup A_2$ è l'insieme degli elementi che appartengono ad almeno uno dei due insiemi. L'intersezione $A_1 \cap A_2$ contiene gli elementi che appartengono simultaneamente a entrambi. Il complemento $A_1^c$ contiene gli elementi di $\Omega$ non appartenenti ad $A_1$. La sottrazione $A_1 \setminus A_2$ equivale a $A_1 \cap A_2^c$.

Queste operazioni godono di proprietà fondamentali. Il doppio complemento restituisce l'insieme originario: $(A^c)^c = A$. Il complemento dello spazio intero è l'insieme vuoto: $\Omega^c = \emptyset$. L'unione di un evento con il suo complementare è l'evento certo: $A \cup A^c = \Omega$. Le leggi di De Morgan stabiliscono che $(A \cup B)^c = A^c \cap B^c$ e $(A \cap B)^c = A^c \cup B^c$.

Dal punto di vista formale, una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$ si chiama algebra se soddisfa due proprietà di chiusura. Primo, se $A_i$ e $A_j$ appartengono a $\mathcal{E}$, allora anche $A_i \cup A_j$ appartiene a $\mathcal{E}$ (chiusura rispetto all'unione). Secondo, se $A_i$ appartiene a $\mathcal{E}$, allora anche $A_i^c$ appartiene a $\mathcal{E}$ (chiusura rispetto alla complementazione).

Da queste due proprietà deriva automaticamente la chiusura rispetto all'intersezione. Applicando De Morgan, si ha $A \cap B = (A^c \cup B^c)^c$. Se $A$ e $B$ appartengono all'algebra, anche $A^c$ e $B^c$ vi appartengono per la chiusura rispetto alla complementazione. La loro unione $A^c \cup B^c$ appartiene all'algebra per la chiusura rispetto all'unione. Infine, il complemento di questa unione appartiene ancora all'algebra, quindi $A \cap B$ è nell'algebra. Lo stesso ragionamento mostra che anche la differenza $A \setminus B = A \cap B^c$ è chiusa.

Un'algebra garantisce quindi che tutte le operazioni insiemistiche restano nel dominio di definizione. Questo è cruciale per la definizione della probabilità: si deve poter calcolare la probabilità di qualunque combinazione di eventi, e l'algebra assicura che si rimane sempre nel dominio.

Quando lo spazio dei campioni è infinito numerabile, si richiede una proprietà più forte. Un'algebra si chiama $\sigma$-algebra se un'unione numerabile di suoi elementi è ancora un elemento dell'algebra. Formalmente, se $A_1, A_2, A_3, \ldots$ appartengono a $\mathcal{E}$, allora anche $\bigcup_{i=1}^{\infty} A_i$ appartiene a $\mathcal{E}$. Se lo spazio è finito, questa distinzione è irrilevante poiché le unioni finite sono già sufficienti. La $\sigma$-algebra diventa necessaria quando si lavora con processi che generano eventi infiniti numerabili, come contare le macchine che passano a un casello autostradale.

## Axioms of Probability

La teoria formale della probabilità si fonda sugli assiomi di Kolmogorov. Dato uno spazio dei campioni $\Omega$ e una $\sigma$-algebra $\mathcal{E}$ dei suoi sottoinsiemi, si definisce legge di probabilità una funzione $P : \mathcal{E} \to [0,1]$ che soddisfa tre assiomi fondamentali, con un quarto che estende il terzo al caso numerabile.

Il primo assioma è quello di non negatività: per ogni evento $A$ appartenente a $\mathcal{E}$, si ha $P(A) \geq 0$. La probabilità è sempre un numero reale non negativo.

Il secondo assioma è quello di normalizzazione: la probabilità dell'evento certo è unitaria, $P(\Omega) = 1$. Questo fissa la scala di misura della probabilità tra zero e uno.

Il terzo assioma è quello di additività: se $A$ e $B$ sono eventi disgiunti, cioè $A \cap B = \emptyset$, allora $P(A \cup B) = P(A) + P(B)$. La probabilità dell'unione di eventi incompatibili è la somma delle probabilità.

Il quarto assioma, chiamato anche assioma tre e mezzo, estende l'additività al caso numerabile: se $\{A_i\}_{i=1}^{\infty}$ è una successione di eventi a due a due disgiunti, allora la probabilità della loro unione è la somma delle singole probabilità.

La terna $(\Omega, \mathcal{E}, P)$ costituisce uno spazio di probabilità. La struttura della $\sigma$-algebra garantisce che tutte le operazioni insiemistiche restino nel dominio di definizione della funzione $P$, permettendo di calcolare la probabilità di qualunque combinazione di eventi.

Da questi assiomi si derivano tutte le proprietà della probabilità come teoremi dimostrabili. La probabilità dell'insieme vuoto è zero: $P(\emptyset) = P(\Omega^c) = 1 - P(\Omega) = 0$. La probabilità dell'evento complementare è $P(A^c) = 1 - P(A)$, poiché $A$ e $A^c$ sono disgiunti e la loro unione è $\Omega$.

La probabilità di $A \setminus B$ si ottiene scrivendo $A = (A \cap B) \cup (A \cap B^c)$, dove i due insiemi sono disgiunti. Per additività, $P(A) = P(A \cap B) + P(A \cap B^c)$, da cui $P(A \setminus B) = P(A) - P(A \cap B)$.

Per l'unione di due eventi qualsiasi, si scrive $A \cup B = A \cup (B \cap A^c)$, dove $A$ e $B \cap A^c$ sono disgiunti. Quindi $P(A \cup B) = P(A) + P(B \cap A^c)$. Ma $P(B \cap A^c) = P(B \setminus A) = P(B) - P(A \cap B)$, da cui segue la formula generale $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

Questa è la proprietà di subadditività: proprio come la misura di due insiemi che si sovrappongono non è la somma delle misure (si conta due volte l'intersezione), la probabilità di $A \cup B$ non è la semplice somma delle probabilità. La probabilità è una misura nel senso matematico del termine, subadditiva esattamente come qualsiasi misura geometrica.

## Sample Spaces Having Equally Likely Outcomes

Quando lo spazio dei campioni è finito e gli eventi elementari sono equiprobabili, la probabilità di un evento si determina come rapporto tra la cardinalità dell'evento e quella dello spazio campionario:

$$P(A) = \frac{|A|}{|\Omega|}$$

Questo riduce il calcolo della probabilità a un problema di enumerazione. L'analisi combinatoria fornisce gli strumenti per contare efficientemente gli elementi di insiemi complessi.

La regola fondamentale è quella del prodotto cartesiano. Dati $k$ insiemi $A_1, A_2, \ldots, A_k$ con cardinalità $|A_i| = n_i$, il prodotto cartesiano ha cardinalità uguale al prodotto delle cardinalità singole: $|A_1 \times A_2 \times \cdots \times A_k| = \prod_{i=1}^{k} n_i$. Questa è la formula base da cui derivano tutti i risultati di analisi combinatoria.

Il numero di $k$-uple ordinate con ripetizione scelte da un insieme di $n$ elementi è $n^k$. Ogni posizione si può riempire in $n$ modi indipendentemente dalle altre, quindi per il principio del prodotto si ha $n \times n \times \cdots \times n$ ($k$ volte).

Il numero di $k$-uple ordinate senza ripetizione, chiamate disposizioni semplici, è $D(n,k) = n(n-1)(n-2)\cdots(n-k+1) = \frac{n!}{(n-k)!}$. Il primo elemento si sceglie in $n$ modi, il secondo in $n-1$ (escludendo il primo già scelto), e così via fino al $k$-esimo che si sceglie in $n-k+1$ modi.

Quando $k = n$, si ottengono le permutazioni: $P(n) = n!$. Le permutazioni di $n$ elementi sono tutte le $n$-uple ordinate senza ripetizione degli $n$ elementi stessi.

Le $k$-uple non ordinate senza ripetizione, chiamate combinazioni, hanno cardinalità data dal coefficiente binomiale:

$$C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

Il ragionamento è il seguente: tra tutte le disposizioni semplici, ogni gruppo di $k!$ di esse (tutte le permutazioni degli stessi $k$ elementi) collassa in un'unica combinazione. Quindi il numero di combinazioni è il numero di disposizioni diviso per $k!$.

Queste formule si applicano direttamente al calcolo di probabilità quando gli esiti sono equiprobabili. Nel poker, la probabilità di ottenere colore (tutte e cinque le carte dello stesso seme) si calcola come rapporto tra il numero di mani con colore e il numero totale di mani possibili. Con un mazzo francese da 52 carte, il numero totale di mani di 5 carte è $\binom{52}{5}$. Il numero di mani con colore è $4 \cdot \binom{13}{5}$ (quattro semi, da ciascuno si scelgono 5 carte tra le 13 disponibili). La probabilità è quindi:

$$P(\text{colore}) = \frac{4 \cdot \binom{13}{5}}{\binom{52}{5}}$$

Un'applicazione importante è il conteggio delle sequenze binarie. Il numero di sequenze binarie di lunghezza $n$ con esattamente $k$ uni (e $n-k$ zeri) è esattamente $\binom{n}{k}$. Se tutti i bit fossero distinti ci sarebbero $n!$ permutazioni. Ma i $k$ uni sono indistinguibili tra loro, come pure gli $n-k$ zeri. Le $k!$ permutazioni degli uni e le $(n-k)!$ permutazioni degli zeri danno la stessa sequenza, quindi il numero di sequenze distinte è $\frac{n!}{k!(n-k)!}$.

Questo si generalizza al coefficiente multinomiale. Data una sequenza di lunghezza $n$ su un alfabeto di $m$ simboli, con $n_i$ occorrenze del simbolo $i$ (dove $\sum_i n_i = n$), il numero di sequenze distinte è:

$$\binom{n}{n_1, n_2, \ldots, n_m} = \frac{n!}{n_1! \cdot n_2! \cdots n_m!}$$

Questi conteggi sono fondamentali nella teoria dell'informazione per determinare quanti messaggi di lunghezza $n$ contengono esattamente $k$ simboli di un certo tipo, formando la base per il calcolo della capacità di un canale.

Un risultato elegante che discende dal coefficiente binomiale è la cardinalità dell'insieme delle parti. Dato un insieme $A$ con $m$ elementi, l'insieme delle parti $\mathcal{P}(A)$ (l'insieme di tutti i sottoinsiemi di $A$, inclusi $\emptyset$ e $A$ stesso) ha cardinalità:

$$|\mathcal{P}(A)| = 2^m$$

La dimostrazione è combinatoria. I sottoinsiemi di cardinalità $k$ sono esattamente le $k$-uple non ordinate senza ripetizione, quindi $\binom{m}{k}$. Sommando su tutti i possibili $k$ da 0 a $m$:

$$|\mathcal{P}(A)| = \sum_{k=0}^{m} \binom{m}{k}$$

Per il binomio di Newton con $a = b = 1$:

$$(a+b)^m = \sum_{k=0}^{m} \binom{m}{k} a^k b^{m-k}$$

ponendo $a = b = 1$ si ottiene:

$$2^m = \sum_{k=0}^{m} \binom{m}{k}$$

che dimostra il risultato.

## Conditional Probability

La probabilità condizionata modella il restringimento dello spazio dei campioni a un sottoinsieme determinato da una condizione. L'intuizione si comprende pensando a un database con tutti i residenti in Italia, con colonne per altezza, peso, colore degli occhi. La probabilità che il peso sia almeno 70 kg si calcola contando quanti record soddisfano questa condizione e dividendo per il totale. La probabilità condizionata che il peso sia almeno 70 kg dato che l'altezza è almeno 170 cm si calcola restringendo il database alle sole persone alte almeno 170 cm (eliminando tutti gli altri record), poi contando quanti di questi pesano almeno 70 kg e dividendo per la dimensione del database ristretto.

In termini di frequenza relativa, se si fanno $n$ prove e $A$ si verifica $N_A$ volte, la frequenza condizionale di $B$ dato $A$ è:

$$f_n(B \mid A) = \frac{N_{A \cap B}}{N_A} = \frac{N_{A \cap B}/n}{N_A/n} = \frac{f_n(A \cap B)}{f_n(A)}$$

Passando al limite, si ottiene la definizione formale.

> [!info] **Definizione: Probabilità condizionata**
> Dati due eventi $A$ e $B$ con $P(A) > 0$, la probabilità condizionata di $B$ dato $A$ è:
> $$P(B \mid A) = \frac{P(A \cap B)}{P(A)}$$

Il condizionamento cambia lo spazio di riferimento: da $\Omega$ si passa ad $A$ come nuovo universo. La probabilità a priori $P(\text{peso} \geq 70)$ include tutti gli italiani, mentre la probabilità a posteriori $P(\text{peso} \geq 70 \mid \text{altezza} \geq 170)$ è calcolata sul sottoinsieme delle persone alte, che mediamente pesano di più.

Dalla definizione si ricava la legge della probabilità composta:

$$P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$$

Questa esprime la probabilità dell'intersezione come prodotto della probabilità di un evento per la probabilità condizionale dell'altro dato il primo.

Un risultato fondamentale è che la probabilità condizionata $P(\cdot \mid A)$, fissato $A$ con $P(A) > 0$, è essa stessa una legge di probabilità che soddisfa tutti gli assiomi di Kolmogorov. La verifica è diretta. La non negatività è ovvia: $P(B \mid A) = P(A \cap B)/P(A) \geq 0$ come rapporto di quantità non negative. La normalizzazione vale perché $P(\Omega \mid A) = P(\Omega \cap A)/P(A) = P(A)/P(A) = 1$. L'additività per eventi disgiunti segue dal fatto che se $B$ e $C$ sono disgiunti, allora $B \cap A$ e $C \cap A$ sono disgiunti, quindi:

$$P(B \cup C \mid A) = \frac{P((B \cup C) \cap A)}{P(A)} = \frac{P((B \cap A) \cup (C \cap A))}{P(A)} = \frac{P(B \cap A) + P(C \cap A)}{P(A)} = P(B \mid A) + P(C \mid A)$$

Data una partizione di $\Omega$ in eventi disgiunti $\{E_1, E_2, \ldots, E_m\}$ la cui unione è $\Omega$, la probabilità di un qualunque evento $A$ si può scomporre come:

$$P(A) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)$$

Questa è la legge della probabilità totale. La derivazione parte dall'identità insiemistica:

$$A = A \cap \Omega = A \cap \left(\bigcup_{i=1}^{m} E_i\right) = \bigcup_{i=1}^{m} (A \cap E_i)$$

Gli insiemi $A \cap E_i$ sono a due a due disgiunti perché $E_i$ ed $E_j$ lo sono. Per additività:

$$P(A) = \sum_{i=1}^{m} P(A \cap E_i) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)$$

dove l'ultimo passaggio usa la definizione di probabilità condizionata. Questa legge è fondamentale perché permette di scomporre il calcolo di una probabilità difficile condizionando rispetto a una partizione che semplifica il problema.

La probabilità condizionata si estende naturalmente alle funzioni di massa di probabilità (PMF). Data una condizione $C$ con $P(C) > 0$, la PMF condizionata di una variabile aleatoria $X$ è:

$$p_{X \mid C}(k) = \frac{P(X=k, C)}{P(C)}$$

Se $k$ non appartiene all'insieme dei valori compatibili con $C$, questa probabilità è zero. Altrimenti, per i valori compatibili, la PMF viene rinormalizzata dividendo per $P(C)$.

## Bayes' Formula

Dalla legge della probabilità composta, usando la commutatività dell'intersezione, si ricava la legge di Bayes:

$$P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$$

Questa formula permette di invertire il condizionamento, passando da $P(A \mid B)$ a $P(B \mid A)$. È lo strumento fondamentale dell'inferenza statistica bayesiana.

Quando si lavora con una partizione $\{E_1, E_2, \ldots, E_m\}$ e si osserva un evento $A$, la legge di Bayes combinata con la probabilità totale fornisce:

$$P(E_i \mid A) = \frac{P(A \mid E_i) \cdot P(E_i)}{\sum_{j=1}^{m} P(A \mid E_j) \cdot P(E_j)}$$

Questa formulazione consente di aggiornare la conoscenza a priori di un fenomeno (le probabilità $P(E_i)$) alla luce di nuove evidenze sperimentali (l'osservazione di $A$), determinando la probabilità a posteriori $P(E_i \mid A)$.

Un esempio classico è il problema del bussolotto con dadi. Un bussolotto contiene due dadi indistinguibili: uno onesto (ogni faccia esce con probabilità $1/6$) e uno truccato (il 6 esce con probabilità $1/2$, le altre facce con probabilità $1/10$ ciascuna). Si estrae un dado casualmente e lo si lancia due volte, ottenendo la coppia $(5,5)$. Si vuole calcolare la probabilità che il dado estratto sia quello truccato.

Sia $T$ l'evento "dado truccato" e $O$ l'evento "dado onesto". La probabilità a priori è $P(T) = P(O) = 1/2$ (estrazione equiprobabile). Dato che si è estratto il dado truccato, i due lanci sono condizionalmente indipendenti (stesso dado lanciato due volte):

$$P(5,5 \mid T) = \frac{1}{10} \cdot \frac{1}{10} = \frac{1}{100}$$

Per il dado onesto:

$$P(5,5 \mid O) = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$$

La probabilità totale di osservare $(5,5)$ è:

$$P(5,5) = P(5,5 \mid T) \cdot P(T) + P(5,5 \mid O) \cdot P(O) = \frac{1}{100} \cdot \frac{1}{2} + \frac{1}{36} \cdot \frac{1}{2} = \frac{1}{200} + \frac{1}{72}$$

Riducendo a denominatore comune:

$$P(5,5) = \frac{36 + 100}{7200} = \frac{136}{7200} = \frac{17}{900}$$

La probabilità a posteriori che il dado sia truccato è:

$$P(T \mid 5,5) = \frac{P(5,5 \mid T) \cdot P(T)}{P(5,5)} = \frac{\frac{1}{200}}{\frac{17}{900}} = \frac{900}{200 \cdot 17} = \frac{9}{34} \approx 0{,}265$$

La probabilità che il dado sia truccato è scesa dal 50% iniziale al 26,5% circa. Questo ha senso: il 5 esce più facilmente con il dado onesto ($1/6 \approx 16{,}7\%$) che con il truccato ($1/10 = 10\%$), quindi osservare due 5 è evidenza a favore dell'ipotesi "dado onesto". Se fossero usciti due 6, il risultato sarebbe stato opposto.

## Independent Events

Due eventi $A$ e $B$ si dicono statisticamente indipendenti se e solo se:

$$P(A \cap B) = P(A) \cdot P(B)$$

Equivalentemente, se $P(B) > 0$, l'indipendenza vale se e solo se $P(A \mid B) = P(A)$: il verificarsi di $B$ non fornisce alcuna informazione sul verificarsi di $A$.

L'indipendenza è un concetto fondamentale perché senza ipotesi di indipendenza molte convergenze statistiche non valgono. La statistica inferenziale si fonda su ipotesi di indipendenza, o almeno di indipendenza asintotica (ergodicità). Se i campioni non sono indipendenti, la statistica descrittiva vale solo per quel campione specifico e non è generalizzabile.

Se $A$ e $B$ sono indipendenti, anche i loro complementari lo sono. La dimostrazione usa De Morgan:

$$P(A^c \cap B^c) = P((A \cup B)^c) = 1 - P(A \cup B) = 1 - P(A) - P(B) + P(A \cap B)$$

Sostituendo $P(A \cap B) = P(A) \cdot P(B)$ (dall'indipendenza):

$$= 1 - P(A) - P(B)(1 - P(A)) = (1 - P(A))(1 - P(B)) = P(A^c) \cdot P(B^c)$$

Quindi $A^c$ e $B^c$ sono indipendenti.

Per tre eventi $A$, $B$, $C$, l'indipendenza richiede che siano indipendenti a due a due e congiuntamente. Devono valere:

$$P(A \cap B) = P(A) \cdot P(B)$$
$$P(A \cap C) = P(A) \cdot P(C)$$
$$P(B \cap C) = P(B) \cdot P(C)$$
$$P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$$

L'indipendenza a coppie non implica l'indipendenza congiunta. Il controesempio classico è il bit di parità. Siano $X_1$ e $X_2$ due bit equiprobabili e indipendenti. Si definisce $X_3 = X_1 \oplus X_2$ (somma modulo 2). Ogni coppia di bit è indipendente: $X_1$ e $X_2$ per ipotesi, $X_1$ e $X_3$ perché se si conosce solo $X_1$ non si può dedurre nulla su $X_3$, analogamente per $X_2$ e $X_3$. Ma la terna non è indipendente: se si conoscono $X_1$ e $X_2$, il valore di $X_3$ è completamente determinato.

Per $n$ eventi, l'indipendenza richiede che per ogni sottoinsieme di indici $\{i_1, i_2, \ldots, i_k\}$ si abbia:

$$P(A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}) = P(A_{i_1}) \cdot P(A_{i_2}) \cdots P(A_{i_k})$$

Questa condizione deve valere per tutti i sottoinsiemi possibili, non solo per le coppie.

Dati $n$ eventi indipendenti $A_1, A_2, \ldots, A_n$ con $P(A_i) = p_i$, si possono calcolare diverse probabilità. La probabilità che non se ne verifichi nessuno è il prodotto delle probabilità complementari:

$$P\left(\bigcap_{i=1}^{n} A_i^c\right) = \prod_{i=1}^{n} (1 - p_i)$$

La probabilità che se ne verifichi almeno uno è il complementare:

$$P\left(\bigcup_{i=1}^{n} A_i\right) = 1 - \prod_{i=1}^{n} (1 - p_i)$$

La probabilità che se ne verifichi esattamente uno si ottiene sommando su tutti i casi in cui uno solo degli eventi si verifica:

$$P(\text{esattamente uno}) = \sum_{i=1}^{n} p_i \prod_{\substack{j=1 \\ j \neq i}}^{n} (1 - p_j)$$

Quando si lavora con problemi del tipo "almeno uno", "almeno due", "almeno $k$", conviene spesso calcolare la probabilità del complementare ("nessuno", "meno di $k$") e sottrarla da 1. Per esempio, la probabilità di ottenere almeno un 6 lanciando un dado onesto 5 volte è:

$$P(\text{almeno un 6}) = 1 - P(\text{nessun 6}) = 1 - \left(\frac{5}{6}\right)^5 \approx 0{,}598$$

---

# Capitolo 4: Random Variables and Expectation

## Random Variables

Tre esperimenti apparentemente diversi — lancio di una moneta (testa o croce), sorgente binaria (emette 0 o 1), lancio di un dado (risultato pari o dispari) — hanno tutti un esito binario. Codificando opportunamente i risultati, si possono trattare in modo unificato attraverso un'applicazione che associa a ogni esito dello spazio campione un valore numerico.

> [!info] **Definizione: Variabile aleatoria (caso discreto)**
> Dato uno spazio di probabilità $(\Omega, \mathcal{E}, P)$ discreto, una variabile aleatoria è un'applicazione $X : \Omega \to \mathcal{X}$ dove $\mathcal{X}$ è un insieme numerico chiamato alfabeto della variabile aleatoria. La funzione $X$ associa a ogni esito $\omega \in \Omega$ un valore numerico $X(\omega) \in \mathcal{X}$.

Le variabili aleatorie permettono di trattare in modo unificato esperimenti diversi che hanno la stessa struttura probabilistica. Ogni insieme discreto non numerico si può sempre descrivere attraverso un insieme di numeri interi, per esempio come puntatori a locazioni di memoria dove sono memorizzate le etichette. Quindi, quando lo spazio dei campioni è discreto, si possono indicizzare gli eventi elementari e la variabile aleatoria diventa semplicemente l'indice.

L'evento elementare nello spazio della variabile aleatoria è $\{X(\omega) = x\}$, cioè l'insieme di tutti gli $\omega$ tali che $X(\omega) = x$. La probabilità si trasporta dallo spazio originario al nuovo spazio numerico:

$$P(X = x) = P(\{\omega \in \Omega : X(\omega) = x\})$$

Nel lancio di un dado onesto, si può definire una variabile $X$ che assume valore 0 se esce pari e 1 se esce dispari. Poiché $\{2, 4, 6\}$ e $\{1, 3, 5\}$ hanno uguale probabilità $1/2$, si ha $P(X = 0) = P(X = 1) = 1/2$.

> [!info] **Definizione: PMF (Probability Mass Function)**
> Data una variabile aleatoria discreta $X$ con alfabeto $\mathcal{X} = \{x_1, x_2, \ldots, x_m\}$, la PMF è la sequenza:
> $$p_X(x_i) = P(X = x_i), \quad i = 1, 2, \ldots, m$$
> Una sequenza è una PMF valida se e solo se:
> 1. $p_X(x_i) \geq 0$ per ogni $i$
> 2. $\sum_{i=1}^{m} p_X(x_i) = 1$

Dalla non negatività e dalla normalizzazione segue automaticamente che $p_X(x_i) \leq 1$ per ogni $i$. La sequenza $(1/2, 1/4, 1/8, 1/8)$ è una PMF valida perché la somma è 1 e tutti i termini sono non negativi.

## Types of Random Variables

Le variabili aleatorie si classificano in base alla natura del loro alfabeto. Una variabile è discreta se l'alfabeto è finito o numerabilmente infinito. Una variabile è continua se assume valori in un continuo non numerabile, tipicamente un intervallo di numeri reali.

Per le variabili discrete, la probabilità di ogni singolo valore è ben definita tramite la PMF. Per le variabili continue, la probabilità di un singolo punto è zero, e si lavora invece con la densità di probabilità (PDF) che descrive la concentrazione di probabilità in ogni punto.

La distinzione è fondamentale perché gli strumenti matematici sono diversi. Per le discrete si usano somme, per le continue si usano integrali. Una variabile uniforme discreta su $\{1, 2, \ldots, M\}$ ha PMF $p_X(k) = 1/M$, mentre una variabile uniforme continua su $[a,b]$ ha PDF $f_X(x) = 1/(b-a)$ per $x \in [a,b]$ e zero altrove.

## Jointly Distributed Random Variables

In molte applicazioni si osservano più grandezze contemporaneamente. Su un database di persone, ogni estrazione casuale restituisce sia l'altezza $X$ che il peso $Y$: si ha un'applicazione dallo spazio dei campioni a una coppia ordinata $(X(\omega), Y(\omega))$.

> [!info] **Definizione: PMF congiunta**
> La PMF congiunta di $(X, Y)$ è la tabella:
> $$p_{XY}(x, y) = P(X = x, Y = y), \quad \forall x \in \mathcal{X}, y \in \mathcal{Y}$$
> Questa tabella ha $|\mathcal{X}| \times |\mathcal{Y}|$ entrate, tutte non negative, la cui somma è 1.

Dalla PMF congiunta si ricavano le PMF delle singole variabili per marginalizzazione:

$$p_X(x) = \sum_{y \in \mathcal{Y}} p_{XY}(x, y), \qquad p_Y(y) = \sum_{x \in \mathcal{X}} p_{XY}(x, y)$$

La congiunta implica univocamente le marginali, ma non viceversa: date le due PMF marginali, esistono in generale molte congiunte compatibili con esse. L'unica eccezione è il caso di indipendenza statistica.

### Independent Random Variables

> [!info] **Definizione: Indipendenza statistica**
> Due variabili aleatorie $X$ e $Y$ sono statisticamente indipendenti se e solo se la loro PMF congiunta si fattorizza nel prodotto delle marginali:
> $$p_{XY}(x, y) = p_X(x) \cdot p_Y(y), \quad \forall x \in \mathcal{X}, y \in \mathcal{Y}$$

Altezza e peso non sono indipendenti: se si sa che una persona è alta 170 cm, la distribuzione del peso condizionata è diversa dalla distribuzione marginale. La probabilità congiunta che una persona sia alta 170 cm e pesi 40 kg non è il prodotto delle probabilità marginali.

### Conditional Distributions

> [!info] **Definizione: PMF condizionale**
> La PMF condizionale di $X$ dato $Y$ è:
> $$p_{X|Y}(x|y) = P(X=x \mid Y=y) = \frac{p_{XY}(x,y)}{p_Y(y)}, \quad \text{per } p_Y(y) > 0$$

Per ogni $y$ fissato, questa è una legge di probabilità: $\sum_{x \in \mathcal{X}} p_{X|Y}(x|y) = 1$. La somma su tutti i valori di $y$ non è necessariamente 1. Nella rappresentazione tabellare, la somma per colonne (condizionamento fisso) fa 1, la somma per righe (condizionamento variabile) no.

Se $X$ e $Y$ sono indipendenti, allora $p_{X|Y}(x|y) = p_X(x)$: conoscere $Y$ non modifica la distribuzione di $X$.

La regola della catena per tre variabili è:

$$p_{XYZ}(x, y, z) = p_Z(z) \cdot p_{Y|Z}(y|z) \cdot p_{X|YZ}(x|y,z)$$

e vale per ogni permutazione degli indici. Si generalizza a $n$ variabili.

Una proprietà importante è che la marginalizzazione si può vedere come media. La PMF marginale di $X$ è la media rispetto a $Y$ della PMF condizionale di $X$ dato $Y$:

$$p_X(x) = \sum_{y \in \mathcal{Y}} p_{X|Y}(x|y) \cdot p_Y(y) = E_Y[p_{X|Y}(x|Y)]$$

Questo punto di vista ha applicazioni nella teoria delle code e nei processi di Poisson.

## Expectation

Il valore atteso nasce dalla statistica descrittiva. Ripetendo un esperimento $n$ volte e osservando i valori $x_1, x_2, \ldots, x_n$, la media campionaria è:

$$\bar{x}_n = \frac{1}{n} \sum_{i=1}^{n} x_i$$

Se l'alfabeto è $\mathcal{X} = \{a_1, a_2, \ldots, a_M\}$ e il valore $a_k$ compare $N_k$ volte (con $\sum_k N_k = n$), si può riscrivere:

$$\bar{x}_n = \sum_{k=1}^{M} \frac{N_k}{n} \cdot a_k = \sum_{k=1}^{M} f_n(a_k) \cdot a_k$$

dove $f_n(a_k) = N_k/n$ è la frequenza relativa. Per la legge dei grandi numeri, quando $n \to \infty$ la frequenza relativa converge alla probabilità: $f_n(a_k) \to P_X(a_k)$. Quindi:

$$\bar{x}_n \to \sum_{k=1}^{M} a_k \cdot P_X(a_k)$$

> [!info] **Definizione: Valore atteso**
> Il valore atteso (o media statistica) di una variabile aleatoria discreta $X$ con alfabeto $\mathcal{X}$ e PMF $p_X$ è:
> $$E[X] = \mu_X = \sum_{k} a_k \cdot p_X(a_k)$$

Il valore atteso è il baricentro della distribuzione: il punto verso cui converge la media campionaria quando si fanno tante prove. Non coincide in generale con la media aritmetica dei valori dell'alfabeto. La media statistica è una media pesata con pesi $p_X(a_k)$. Solo quando la distribuzione è uniforme (tutti i valori equiprobabili) le due medie coincidono.

Per una variabile di Bernoulli con $P(X=1) = p$ e $P(X=0) = 1-p$, il valore atteso è:

$$E[X] = 0 \cdot (1-p) + 1 \cdot p = p$$

La media di una Bernoulli è la probabilità di successo.

Per una variabile uniforme discreta su $\mathcal{X} = \{1, 2, \ldots, M\}$:

$$E[X] = \frac{1}{M} \sum_{k=1}^{M} k = \frac{1}{M} \cdot \frac{M(M+1)}{2} = \frac{M+1}{2}$$

dove si è usata la formula di Gauss per la somma dei primi $M$ interi: $\sum_{k=1}^{M} k = M(M+1)/2$. La media è il punto medio dell'intervallo.

Un risultato fondamentale è il teorema del calcolo della media per funzioni di variabili aleatorie.

> [!abstract] **Teorema: Media di funzioni**
> Data una variabile aleatoria $X$ con PMF $p_X$ e una funzione $g$, la media di $Y = g(X)$ è:
> $$E[g(X)] = \sum_{x \in \mathcal{X}} g(x) \cdot p_X(x)$$

Questo permette di calcolare $E[g(X)]$ senza costruire esplicitamente la PMF di $Y$: si lavora direttamente con la PMF di $X$. Il valore quadratico medio è un caso particolare con $g(x) = x^2$:

$$E[X^2] = \sum_{x} x^2 \cdot p_X(x)$$

Il valore efficace (root mean square) è $x_{\text{rms}} = \sqrt{E[X^2]}$.

## Properties of the Expected Value

Il valore atteso è un operatore lineare. Per costanti reali $a$ e $b$:

$$E[aX + b] = a \cdot E[X] + b$$

Il termine $b$ è deterministico e esce fuori dall'operatore aspettazione. Il fattore $a$ fattorizza perché moltiplicare ogni valore per $a$ moltiplica la somma pesata per $a$.

### Expected Value of Sums of Random Variables

La linearità si estende alle somme. Per qualunque coppia di variabili $X$ e $Y$ (non necessariamente indipendenti):

$$E[X + Y] = E[X] + E[Y]$$

Questa proprietà è fondamentale. Per la distribuzione binomiale $S_n = X_1 + X_2 + \cdots + X_n$ dove $X_i \sim \text{Ber}(p)$ sono indipendenti:

$$E[S_n] = \sum_{i=1}^{n} E[X_i] = \sum_{i=1}^{n} p = np$$

La media della binomiale è $np$ senza bisogno di calcolare direttamente la somma pesata sulla PMF.

Il teorema della media condizionale afferma che la media totale si può calcolare condizionando rispetto a una partizione:

$$E[X] = \sum_{i=1}^m P(E_i) \cdot E[X \mid E_i]$$

dove $\{E_1, E_2, \ldots, E_m\}$ è una partizione di $\Omega$. Questo permette di scomporre problemi complessi in sottoproblemi più semplici.

## Variance

La variabile centrata $X - \mu_X$ ha media nulla per costruzione. La varianza misura la sua "dimensione" tramite il valor quadratico medio:

> [!info] **Definizione: Varianza**
> La varianza di $X$ è:
> $$\sigma_X^2 = \text{Var}(X) = E[(X - \mu_X)^2] = \sum_{x} (x - \mu_X)^2 \cdot p_X(x)$$
> La deviazione standard è $\sigma_X = \sqrt{\sigma_X^2}$.

La varianza è sempre non negativa. Vale zero se e solo se la variabile è quasi certamente costante (uguale alla sua media).

Una formula alternativa molto utile è:

$$\sigma_X^2 = E[X^2] - \mu_X^2$$

che si dimostra sviluppando il quadrato:

$$E[(X-\mu_X)^2] = E[X^2 - 2\mu_X X + \mu_X^2] = E[X^2] - 2\mu_X^2 + \mu_X^2 = E[X^2] - \mu_X^2$$

La coppia $(\mu_X, \sigma_X)$ caratterizza globalmente la variabile aleatoria. Se $\sigma_X$ è molto più piccolo di $\mu_X$, la variabile è concentrata intorno alla media e la media è un buon predittore. Se $\sigma_X$ è comparabile o superiore a $\mu_X$, la variabile è molto aleatoria e osservare valori lontani dalla media è probabile.

La varianza gode di proprietà algebriche importanti:

$$\text{Var}(aX + b) = a^2 \text{Var}(X)$$

Questo si scompone in due proprietà. Primo, un termine additivo $b$ non cambia la varianza (invarianza per traslazione): sposta la distribuzione ma non la allarga. Secondo, un fattore moltiplicativo $a$ scala la varianza per $a^2$ (covarianza quadratica per scala).

## Covariance and Variance of Sums of Random Variables

> [!info] **Definizione: Covarianza**
> La covarianza tra $X$ e $Y$ è:
> $$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]$$

La covarianza misura il grado di co-variazione tra due variabili. Se è positiva, le deviazioni dalla media di $X$ e $Y$ tendono a essere dello stesso segno. Se è negativa, tendono a essere di segno opposto. Se è zero, non esiste una tendenza lineare di co-variazione.

Se $X$ e $Y$ sono indipendenti, allora $E[XY] = E[X]E[Y]$, quindi $\text{Cov}(X,Y) = 0$. L'indipendenza implica incorrelazione. Il viceversa non vale: variabili incorrelate non sono necessariamente indipendenti, salvo nel caso gaussiano.

> [!info] **Definizione: Coefficiente di correlazione**
> $$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

Questo coefficiente normalizza la covarianza rispetto alle scale delle due variabili. Per la disuguaglianza di Cauchy-Schwarz nello spazio delle variabili aleatorie, si ha:

$$-1 \leq \rho_{XY} \leq 1$$

I valori estremi corrispondono a relazioni lineari perfette: $\rho = 1$ se $Y = a + bX$ con $b > 0$, $\rho = -1$ se $b < 0$. Il valore $\rho = 0$ corrisponde all'incorrelazione.

Per la varianza di una somma, si ha:

$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$$

Se $X$ e $Y$ sono incorrelate (o indipendenti, che è condizione più forte), la varianza della somma è la somma delle varianze:

$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$$

Per un vettore aleatorio $\mathbf{x} = (X_1, X_2)^T$, la matrice di covarianza è:

$$K_{\mathbf{x}} = \begin{pmatrix} \sigma_{X_1}^2 & \text{Cov}(X_1, X_2) \\ \text{Cov}(X_1, X_2) & \sigma_{X_2}^2 \end{pmatrix}$$

Questa matrice è simmetrica e definita non negativa. Si generalizza a $n$ variabili con $K_{ij} = \text{Cov}(X_i, X_j)$.

## Moment Generating Functions

**Non ancora trattato**

## Chebyshev's Inequality and the Weak Law of Large Numbers

La disuguaglianza di Markov fornisce un limite superiore per variabili non negative. Per ogni $\delta > 0$:

$$P(X \geq \delta) \leq \frac{E[X]}{\delta}$$

Applicando Markov a $(X - \mu_X)^2$ si ottiene la disuguaglianza di Chebyshev.

> [!info] **Disuguaglianza di Chebyshev**
> Per ogni variabile aleatoria $X$ con media $\mu_X$ e deviazione standard $\sigma_X$, e per ogni $k > 0$:
> $$P(|X - \mu_X| \geq k\sigma_X) \leq \frac{1}{k^2}$$
> Equivalentemente:
> $$P(|X - \mu_X| < k\sigma_X) \geq 1 - \frac{1}{k^2}$$

Con $k = 2$, almeno il 75% dei dati cade entro 2 deviazioni standard dalla media. Con $k = 3$, almeno l'89% entro 3 deviazioni standard. Con $k = 10$, almeno il 99% entro 10 deviazioni standard. Questo vale indipendentemente dalla forma della distribuzione.

La frequenza di successo è essa stessa una variabile aleatoria:

$$F_n(A) = \frac{N_A(\omega)}{n}$$

dove $N_A$ è il numero di occorrenze di $A$ in $n$ prove. Se le prove sono indipendenti, $N_A \sim \text{Bin}(n, P(A))$, quindi:

$$E[F_n(A)] = P(A)$$
$$\text{Var}(F_n(A)) = \frac{P(A)(1-P(A))}{n}$$

Quando $n \to \infty$, la varianza tende a zero. Per Chebyshev, per ogni $\varepsilon > 0$:

$$P(|F_n(A) - P(A)| > \varepsilon) \leq \frac{\text{Var}(F_n(A))}{\varepsilon^2} = \frac{P(A)(1-P(A))}{n\varepsilon^2} \to 0$$

Questo è la legge debole dei grandi numeri: $F_n(A) \to P(A)$ in probabilità. Esiste anche una convergenza più forte (con probabilità 1), detta legge forte dei grandi numeri, che non è stata dimostrata formalmente ma garantisce che l'evento $F_n(A) \to P(A)$ ha probabilità esattamente 1.

La convergenza in media quadratica è quella per cui $E[(F_n(A) - P(A))^2] \to 0$, che coincide con la varianza di $F_n(A)$ poiché la media è $P(A)$. Convergenza con probabilità 1 e convergenza in media quadratica sono entrambe forti e implicano la convergenza in probabilità, ma non si implicano a vicenda.

---

# Capitolo 5: Special Random Variables

## The Bernoulli and Binomial Random Variables

> [!info] **Definizione: Distribuzione di Bernoulli**
> Una variabile $X$ segue una distribuzione di Bernoulli di parametro $p \in [0,1]$, indicato $X \sim \text{Ber}(p)$, se l'alfabeto è $\{0, 1\}$ e la PMF è:
> $$P_X(x) = p^x (1-p)^{1-x}, \quad x \in \{0,1\}$$
> dove 1 rappresenta il successo e 0 il fallimento.

Il parametro $p$ è la probabilità di successo. La media è $E[X] = p$.

> [!info] **Definizione: Distribuzione Binomiale**
> Siano $X_1, X_2, \ldots, X_n$ variabili i.i.d. (indipendenti e identicamente distribuite) con $X_i \sim \text{Ber}(p)$. La somma:
> $$S_n = X_1 + X_2 + \cdots + X_n$$
> conta il numero totale di successi in $n$ prove. Si ha $S_n \sim \text{Bin}(n, p)$ con PMF:
> $$P_{S_n}(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

La PMF si interpreta combinatoriamente. Il fattore $p^k (1-p)^{n-k}$ è la probabilità di una specifica sequenza con $k$ successi e $n-k$ fallimenti. Il coefficiente binomiale $\binom{n}{k}$ conta quante sequenze distinte hanno esattamente $k$ successi.

La normalizzazione segue dal binomio di Newton:

$$\sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = (p + (1-p))^n = 1$$

La media della binomiale è $E[S_n] = np$ per linearità del valore atteso. La varianza è $\text{Var}(S_n) = np(1-p)$.

### Computing the Binomial Distribution Function

**Non ancora trattato**

## The Poisson Random Variable

> [!info] **Definizione: Distribuzione di Poisson**
> Una variabile $X$ segue una distribuzione di Poisson di parametro $\lambda > 0$, indicato $X \sim \text{Poi}(\lambda)$, se l'alfabeto è $\mathbb{N}_0$ e la PMF è:
> $$P_X(k) = \frac{\lambda^k}{k!} e^{-\lambda}, \quad k = 0, 1, 2, \ldots$$

Il parametro $\lambda$ rappresenta il tasso medio di occorrenze nell'intervallo considerato. La distribuzione di Poisson modella eventi rari: fenomeni che singolarmente sono poco probabili ma vengono osservati su un numero enorme di occasioni. Applicazioni tipiche sono il numero di macchine che arrivano a un casello, il numero di pacchetti che arrivano a un router, il numero di persone che entrano in un ufficio postale.

La normalizzazione si verifica usando la serie esponenziale:

$$\sum_{k=0}^{\infty} \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^{\lambda} = 1$$

La media è $E[X] = \lambda$. La derivazione parte da:

$$E[X] = \sum_{k=0}^{\infty} k \cdot \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \sum_{k=1}^{\infty} k \cdot \frac{\lambda^k}{k!}$$

Semplificando $k$ con $k! = k \cdot (k-1)!$ ed estraendo un fattore $\lambda$:

$$= \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!} = \lambda e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^{j}}{j!} = \lambda e^{-\lambda} \cdot e^{\lambda} = \lambda$$

La distribuzione di Poisson gode di una proprietà di chiusura: se $N \sim \text{Poi}(\lambda)$ e si estrae ogni elemento con probabilità $p$ indipendentemente, il numero di elementi estratti $M$ è anch'esso Poisson con media $\lambda p$. Questo si dimostra condizionando su $N$ e applicando la legge della probabilità totale.

### Computing the Poisson Distribution Function

**Non ancora trattato**

## The Hypergeometric Random Variable

**Non ancora trattato**

## The Uniform Random Variable

Per le variabili discrete, una variabile è uniforme su $\mathcal{X} = \{a_1, \ldots, a_M\}$ se tutti i valori sono equiprobabili:

$$p_X(a_k) = \frac{1}{M}$$

La media è la media aritmetica dell'alfabeto. Per $\mathcal{X} = \{1, 2, \ldots, M\}$:

$$E[X] = \frac{1}{M} \sum_{k=1}^{M} k = \frac{M+1}{2}$$

Per le variabili continue, una variabile è uniforme sull'intervallo $[a,b]$ se la densità di probabilità è:

$$f_X(x) = \begin{cases} \frac{1}{b-a} & a \leq x \leq b \\ 0 & \text{altrove} \end{cases}$$

La funzione di distribuzione cumulativa (CDF) è:

$$F_X(x) = \begin{cases} 0 & x < a \\ \frac{x-a}{b-a} & a \leq x \leq b \\ 1 & x > b \end{cases}$$

La CDF ha andamento a rampa lineare con pendenza $1/(b-a)$.

Il valore atteso si calcola come:

$$E[X] = \int_a^b x \cdot \frac{1}{b-a} dx = \frac{1}{b-a} \cdot \frac{b^2 - a^2}{2} = \frac{a+b}{2}$$

La varianza è:

$$\text{Var}(X) = \frac{(b-a)^2}{12}$$

## Normal Random Variables

**Non ancora trattato** (menzionato come gaussiana nelle lezioni ma non sviluppato formalmente)

## Exponential Random Variables

> [!info] **Definizione: Distribuzione esponenziale**
> Una variabile $X$ è esponenziale di parametro $\lambda > 0$, indicato $X \sim \text{Exp}(\lambda)$, se la densità di probabilità è:
> $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{cases}$$

Il parametro $\lambda$ è il tasso di arrivo. La distribuzione esponenziale modella il tempo di attesa di un evento raro in un processo senza memoria, come il tempo fino al prossimo arrivo in una coda poissoniana.

La CDF è:

$$F_X(x) = \begin{cases} 0 & x < 0 \\ 1 - e^{-\lambda x} & x \geq 0 \end{cases}$$

che si ottiene integrando:

$$F_X(x) = \int_0^x \lambda e^{-\lambda t} dt = [-e^{-\lambda t}]_0^x = 1 - e^{-\lambda x}$$

Il valore atteso è:

$$E[X] = \int_0^{+\infty} x \cdot \lambda e^{-\lambda x} dx = \frac{1}{\lambda}$$

Se $\lambda$ è grande, la media $1/\lambda$ è piccola (decadimento veloce). Se $\lambda$ è piccolo, la media è grande (decadimento lento).

La proprietà fondamentale dell'esponenziale è l'assenza di memoria:

$$P(X > s + t \mid X > s) = P(X > t)$$

Il processo "dimentica" il tempo già trascorso. Questa è l'unica distribuzione continua con questa proprietà.

### The Poisson Process

**Non ancora trattato** (menzionato ma non sviluppato)

## The Gamma Distribution

**Non ancora trattato**

## Distributions Arising from the Normal

**Non ancora trattato**

## The Logistics Distribution

**Non ancora trattato**

---

# Capitolo 6: Distributions of Sampling Statistics

## Introduction

**Non ancora trattato**

## The Sample Mean

**Parzialmente trattato**: La convergenza della frequenza di successo alla probabilità è stata dimostrata nella Lezione 5, ma non è stato sviluppato il concetto generale di distribuzione della media campionaria.

## The Central Limit Theorem

**Menzionato nella Lezione 8 ma non sviluppato formalmente**

Il Teorema del Limite Centrale afferma che la somma di variabili i.i.d., opportunamente standardizzata, tende a una distribuzione gaussiana. Non è stato dimostrato nelle lezioni disponibili.

### Approximate Distribution of the Sample Mean

**Non ancora trattato**

### How Large a Sample is Needed?

**Non ancora trattato**

## The Sample Variance

**Non ancora trattato**

## Sampling Distributions from a Normal Population

**Non ancora trattato**

## Sampling from a Finite Population

**Non ancora trattato**

---

# Capitolo 7: Parameter Estimation

**Interamente non ancora trattato**

---

# Capitolo 8: Hypothesis Testing

**Interamente non ancora trattato**

---

# Capitolo 9: Regression

**Interamente non ancora trattato**