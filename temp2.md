# Fondamenti Probabilità

## Definizioni

> **Esperimento**
> Un'operazione o un'azione (o un insieme di esse) il cui esito produce uno tra diversi risultati possibili. Ad esempio, il lancio di un dado è un esperimento poiché l'esito non è noto a priori ma appartiene a un insieme di possibilità predefinite.

> **Spazio dei campioni**
> Comunemente denotato con $\Omega$, rappresenta l'insieme (non necessariamente numerico) di tutti i risultati possibili di un esperimento. 
> Per il presente studio, si assume che lo spazio sia **discreto**, ovvero finito o numerabile.

> **Evento**
> Un qualunque sotto-insieme di $\Omega$ definito matematicamente da un insieme di suoi elementi e lessicalmente da una proposizione.

> **Evento elementare**
> Uno dei possibili $|\Omega|$ elementi di $\Omega$. Si indica anche con $\omega \in \Omega$.

> [!quote] Osservazione
> Un evento è univocamente individuato dagli elementi che lo compongono; al contrario, la proposizione che lo definisce non è unica.

## Qualche richiamo di insiemistica

Siano $\{ A _ { i } \} _ { i = 1 } ^ { M }$ $M$ sotto-insiemi di un insieme $\Omega .$. Definiamo:

1. **Unione** tra due sotto-insiemi, $A _ { 1 } \cup A _ { 2 }$, un sotto-insieme di $\Omega$ che contenga tutti gli elementi di $A _ { 1 }$ e quelli di $A _ { 2 }$, ovviamente contando una sola volta quelli comuni;
2. **Complemento** in $\Omega$ di un sotto-insieme $A _ { 1 }$ l’insieme $\overline { { A _ { 1 } } }$ che contiene tutti gli elementi di $\Omega$ che non appartengono a $A _ { 1 }$; ovviamente $\overline { { \Omega } } = \emptyset \space  , \overline { { \overline { { A _ { 1 } } } } } = A _ { 1 } \mathrm { ~ e ~ } A _ { 1 } \cup \overline { { \overline { { A _ { 1 } } } } } = \Omega$
3. **Intersezione** tra due sotto-insiemi, $A _ { 1 } \cap A _ { 2 }$, l’insieme che contiene tutti e soli gli elementi comuni a $A _ { 1 }$ e $A _ { 2 }$
4. **Sottrazione** tra due insiemi, $A _ { 1 } \setminus A _ { 2 }$, l’insieme che contiene gli elementi di $A _ { 1 }$ che non appartengono a $A _ { 2 }$. Ovviamente avremo:

$$
A _ {1} \setminus A _ {2} = A _ {1} \cap \overline {{A _ {2}}}
$$


5. Relazione di De Morgan tra unione, intersezione e complementazione:
$$
\overline {{A _ {1} \cup A _ {2}}} = \overline {{A _ {1}}} \cap \overline {{A _ {2}}} \Longrightarrow \overline {{\overline {{A _ {1}}} \cup \overline {{A _ {3}}}}} = A _ {1} \cap A _ {2}
$$

6. Proprietà associativa di unione e intersezione:
$$
\left(A _ {1} \cup A _ {2}\right) \cup A _ {3} = A _ {1} \cup \left(A _ {2} \cup A _ {3}\right) \quad \left(A _ {1} \cap A _ {2}\right) \cap A _ {3} = A _ {1} \cap \left(A _ {2} \cap A _ {3}\right)
$$

7. Proprietà distributiva dell’unione rispetto all’intersezione e dell’intersezione rispetto all’unione:
$$
A _ {1} \cup \left(\cap_ {i = 2} ^ {M} A _ {i}\right) = \cap_ {i = 2} ^ {M} \left(A _ {1} \cup A _ {i}\right)
$$
$$
A _ {1} \cap \left(\cup_ {i = 2} ^ {M} A _ {i}\right) = \cup_ {i = 2} ^ {M} \left(A _ {1} \cap A _ {i}\right)
$$

## Nomenclatura probabilistica

- $\Omega$ si definisce **evento certo**;
- $\emptyset \space$  si definisce **evento impossibile**;
- $A$ e $A^c$ si definiscono **eventi complementari**;
- Due eventi $A$ e $B$ tali che $A \cap B = \emptyset \space$  si definiscono **incompatibili** o **mutuamente esclusivi**;
- Se $A \subseteq B$ si dice che $A$ **implica** $B$, cioè il verificarsi di $A$ implica che si verifichi $B$.


## Spazi finiti con eventi elementari equivalenti

Sia $\Omega$ uno spazio dei campioni finito; 

Si assuma che tutti gli eventi elementari (cioè, gli elementi di $\Omega$) siano **equivalenti**, cioè che non esista alcun elemento ”privilegiato” rispetto agli altri: questo equivale ad assumere che, eseguendo un numero sufficientemente elevato di prove, ciascun evento elementare si verifichi un numero di volte approssimativamente uguale a quello di qualsiasi altro evento elementare; 

Detto $A \subseteq \Omega$ un qualsiasi evento, la frequenza di occorrenza di $A$ gode della proprietà: 

$$
f _ {n} (A) = \frac {n _ {A}}{n} \longrightarrow \frac {| A |}{| \Omega |}, \qquad n \to \infty
$$

Quindi per eventi equivalenti è importante saper contare le cardinalità dei sotto-insiemi che definiscono gli eventi di interesse. 

La branca che si occupa di questo problema si chiama **calcolo combinatorio**.

## Prodotti cartesiani

Si considerino $k$ insiemi finiti, $A _ { 1 } , \ldots A _ { k }$, non necessariamente distinti. 

> [!theorem] Prodotto Cartesiano
> *Definizione*: Si definisce prodotto cartesiano $A ^ { ( k ) } = A _ { 1 } \times \ldots \times A _ { k }$ un insieme costituito dalle $k { \mathrm { - } } { \mathsf { p l e } }$ ordinate in cui il primo elemento appartenga a $A _ { 1 }$, il secondo a $A _ { 2 }$ e così via. 

Siccome il primo elemento si può scegliere in $| A _ { 1 } |$ modi, il secondo $| A _ { 2 } |$ e così via, avremo: 

$$
\boxed {\left| A ^ {(k)} \right| = \prod_ {i = 1} ^ {k} \left| A _ {i} \right|}
$$

Questa è la relazione fondamentale del calcolo combinatorio, dalla quale molte altre formule di conteggio derivano. 

## k-ple ordinate senza ripetizione

Si supponga $A = \{ a _ { 1 } , \ldots a _ { n } \}$.

Si vogliono contare le stringhe di lunghezza $k$ di elementi di $A$ in cui ogni elemento di $A$ compaia una sola volta (cioè, le ripetizioni non sono ammesse). 

Questo implica - nella formula precedente - che $\left| A _ { 1 } \right| = \left| A \right| = n ,$ $| A _ { 2 } | = n - 1 , \ldots , | A _ { k } | = n - k + 1$.

Pertanto il richiesto numero è 

$$
\left| A ^ {(k)} \right| = n (n - 1) (n - 2) \cdot \dots \cdot (n - k + 1) = \prod_ {i = 0} ^ {k - 1} (n - i)
$$
## Permutazioni

Un caso particolare - ma molto rilevante - del calcolo precedente è quando $k = n$. La domanda cui si vuole rispondere è: 

Dato un insieme di $n$ elementi, quante $n$-ple ordinate si possono formare? 

Risposta: È un caso speciale di enumerazione di k-ple quando $k = n$, cioè: 

>permutazioni di $n$ elementi $= n(n - 1) \cdot \dots \cdot 1 = n!$

Questo ci conduce immediatamente al concetto di combinazioni. 

## Combinazioni $( \overline { { G } } _ { m } ) _ { s } ^ { s }$

> [!theorem] Combinazione
> **Definizione**: Una combinazione è una selezione di elementi da un insieme in cui l'ordine degli elementi non è rilevante. In pratica, si contano i sottogruppi possibili senza preoccuparsi della sequenza in cui sono stati scelti.
> 
> **Formalizzazione**: Il numero di combinazioni di $n$ elementi presi $k$ alla volta è dato dal coefficiente binomiale:
> $$ \binom{n}{k} = \frac{n!}{k!(n-k)!} $$

Le combinazioni $C _ { n , k }$ di ”$n$ elementi su $k$ posti” è il numero di $k { \mathrm { - } } { \mathsf { p l e } }$ non ordinate che si possono formare con $n$ elementi (cioè, il numero di sottoinsiemi di $\Omega$ di cardinalità $k )$).

Pertanto, le $k !$ permutazioni di una stessa $k { \mathrm { - } } { \mathsf { p l a } }$ ordinata ”collassano” in un’unica combinazione. Questo comporta: 

$$
C _ {n, k} = \frac {n (n - 1) \cdot \ldots (n - k + 1)}{k !} = \frac {n !}{k ! (n - k) !} = \binom{n}{k}
$$

dove $\left( \begin{array} { l } { n } \\ { k } \end{array} \right)$ è il coefficiente binomiale $( n , k )$.
## Insieme delle parti di un insieme finito

Si consideri un insieme $A$ con $n$ elementi. 

L’insieme delle parti ${ \mathcal { P } } ( A )$ di $A \ \dot { \mathsf { e } }$ è l’insieme di tutti i possibili sottoinsiemi di $A$. 

Negli insiemi ovviamente l’ordinamento non conta, per cui il numero di sottoinsiemi k-dimensionali di $A$ è 

$$
\binom{n}{k}
$$

Siccome tanto l’insieme vuoto (0-dimensionale) quanto $A$ (n-dimensionale) sono sottoinsiemi di $A ,$, avremo: 

$$
| \mathcal {P} (A) | = \sum_ {k = 0} ^ {n} \binom{n}{k} = 2 ^ {n}
$$

# Discreto
## Dalla frequenza alla probabilità

Dato uno spazio dei campioni discreto $\Omega$ e un suo qualunque sottoinsieme (o evento) $A$, si definisce **probabilità** che occorra $A$ come il limite della frequenza di occorrenza di $A$ quando il numero di esperimenti — o prove — tende all’infinito, cioè: 

$$
\mathbb {P} (A) = \lim _ {n \rightarrow \infty} \frac {n _ {A}}{n}
$$

A questo punto, il concetto di spazio finito con eventi elementari equivalenti diviene quello di **spazio finito con eventi elementari equiprobabili**.

Si ha di conseguenza che, per uno spazio finito a eventi elementari equiprobabili vale la relazione generale: 

$$
\mathbb {P} (A) = \frac {| \Omega_ {A} |}{| \Omega |}
$$

dove $\Omega _ { A }$ contiene tutti gli eventi che comportano il verificarsi di $A$. 

## Frequenza di occorrenza e probabilità su Spazi finiti

Sia $\Omega$ uno spazio campione discreto (cioè, finito o numerabile). Rimuovendo l’ipotesi che gli eventi elementari siano equiprobabili, la definizione di **probabilità** data in precedenza rimane valida. 

Si consideri un evento $A$ e si conducano $n$ esperimenti indipendenti. Sia $N_A$ il numero di volte in cui $A$ si verifica. Le frequenze di occorrenza e le probabilità si definiscono come segue:

$$
f _ {n} (A) = \frac {n _ {A}}{n} \quad \mathbb {P} (A) = \lim _ {n \rightarrow \infty} f _ {n} (A) = \lim _ {n \rightarrow \infty} \frac {n _ {A}}{n}
$$

La principale differenza rispetto al caso di equiprobabilità è che non è più vero in generale che $n _ { A } \simeq n | { \cal A } |$. 

> [!quote] Osservazione
> Quando gli eventi elementari non sono equiprobabili, un evento $A \subseteq \Omega$ ha una misura diversa da quella ordinaria data dal numero dei suoi elementi distinti. Di conseguenza, due eventi $A \subseteq \Omega \mathrm { ~ e ~ } B \subseteq \Omega$ di uguale cardinalità $( | A | = | B | )$ possono avere "pesi" (cioè misure) diversi e le tecniche di conteggio non sono più sufficienti ai fini del calcolo della probabilità.

## Alcune proprietà della frequenza di occorrenza e della probabilità 

Siano $A$ e $B$ due eventi. Siano $N_A$ e $N_B$ il numero di occorrenze su $n$ prove, $\frac{N_A}{n}$ e $\frac{N_B}{n}$ le relative frequenze, e $P(A)$ e $P(B)$ i rispettivi limiti (ovvero le probabilità). Valgono le seguenti proprietà:

### a Eventi complementari
$$
f _ {n} (\overline {{A}}) = \frac {n - n _ {A}}{n} = 1 - f _ {n} (A) \Longrightarrow \mathbb {P} (\overline {{A}}) = 1 - \mathbb {P} (A)
$$

### b Sub-additività
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) \tag{1}$$
$$
f _ {n} (A \cup B) = \frac {n _ {A U B}}{n} = \frac {n _ {A} + n _ {B} - n _ {A \cap B}}{n} = f _ {n} (A) + f _ {n} (B) - f _ {n} (A \cap B) \rightarrow
$$
$$
\mathbb {P} (A \cup B) = \mathbb {P} (A) + \mathbb {P} (B) - \mathbb {P} (A \cap B)
$$

Infatti, se $A$ e $B$ non sono incompatibili, sommare semplicemente $\frac{N_A}{n}$ e $\frac{N_B}{n}$ equivarrebbe a contare due volte le occorrenze di entrambi (cioè le occorrenze di $A \cap B )$), il che spiega il termine sottrattivo.

### c Sottrazione tra insiemi
$$P(A \setminus B) = P(A) - P(A \cap B) \tag{2}$$
$$
f _ {n} (A \setminus B) = f _ {n} (A \cap \overline {{B}}) = \frac {n _ {A} - n _ {A \cap B}}{n} = f _ {n} (A) - f _ {n} (A \cap B) \rightarrow
$$
$$
\mathbb {P} (A \setminus B) = \mathbb {P} (A) - \mathbb {P} (A \cap B)
$$

Infatti, dovendosi verificare $A$ ma non $B$, bisogna sottrarre a $\frac{N_A}{n}$ il numero di esperimenti in cui si verificano entrambi, $n _ { A \cap B }$.

### d Evento certo ed evento impossibile
Banalmente:

$$
f _ {n} (\Omega) = \frac {n}{n} = 1 \rightarrow \mathbb {P} (\Omega) = 1 \rightarrow \mathbb {P} (\emptyset \space ) = \mathbb {P} (\overline {{\Omega}}) = 0
$$

## Frequenze e probabilità condizionate

Siano $A$ e $B$ due eventi che occorrano $n _ { A } \in n _ { B }$ volte su $n$ esperimenti. Definiamo la **frequenza di occorrenza** di $A$ condizionata a $B \texttt { - } f _ { n } ( A | B )$ come il rapporto tra il numero di prove in cui si verificano entrambi $\left( n _ { A \cap B } \right)$ e il numero di volte in cui si verifica solo $B$, cioè, formalmente:

$$
f _ {n} (A | B) = \frac {n _ {A \cap B}}{n _ {B}} = \frac {n _ {(A \cap B)}}{n} \frac {n}{n _ {B}} = \frac {f _ {n} (A \cap B)}{f _ {n} (B)} \to \mathbb {P} (A | B) = \frac {\mathbb {P} (A \cap B)}{\mathbb {P} (B)}
$$

In altre parole, restringiamo il nostro campione di analisi solo agli $n$ risultati che abbiano condotto al verificarsi di $B$. Ovviamente:

$$
\mathbb {P} (B | A) = \frac {\mathbb {P} (A \cap B)}{\mathbb {P} (A)} \Leftrightarrow \mathbb {P} (A \cap B) = \mathbb {P} (B | A) \mathbb {P} (A) = \mathbb {P} (A | B) \mathbb {P} (B)
$$

L’ultima relazione prende anche il nome di **legge della probabilità composta**.

## Legge della probabilità totale

Un’importante conseguenza della definizione di probabilità condizionata è la **legge della probabilità totale**.

Sia $B_1, B_2, \dots, B_k$ una partizione di $\Omega$, cioè:

$$
\cup_ {i = 1} ^ {k} B _ {i} = \Omega \quad B _ {i} \cap B _ {j} = \emptyset \space \space ,  \forall \space i \neq j
$$

Se $A \subseteq \Omega$, avremo allora:

$$
\mathbb {P} (A) = \mathbb {P} (A \cap \Omega) = \mathbb {P} (A \cap \cup_ {i = 1} ^ {k} B _ {i}) = \mathbb {P} \left(\cup_ {i = 1} ^ {k} A \cap  B_ {i}\right)
$$

Essendo $B _ { i } \cap B _ { j } = \emptyset \space$, avremo ovviamente che $( A \cap B _ { i } ) \cap ( A \cap B_ { j } ) = \emptyset \space$, per cui:

$$
\boxed {\mathbb {P} (A) = \sum_ {i = 1} ^ {k} \mathbb {P} \left(A \cap B _ {i}\right) = \sum_ {i = 1} ^ {k} \mathbb {P} \left(A | B _ {i}\right) \mathbb {P} \left(B _ {i}\right)}
$$

## Eventi Indipendenti

Due eventi, $A \subseteq \Omega \mathrm { ~ e ~ } B \subseteq \Omega$ si dicono **indipendenti** quando il verificarsi di uno non ha nessuna influenza sul verificarsi o meno dell’altro. 

In altre parole, due eventi $A \in B$ sono indipendenti se (e solo se) $\begin{array} { r } { f _ { n } ( A | B ) = f _ { n } ( A ) \mathrm { ~ e ~ } f _ { n } ( B | A ) = f _ { n } ( B ) . } \end{array}$ 

Pertanto, sfruttando la legge della probabilità composta (o, equivalentemente, la definizione di probabilità condizionata) avremo che, se $A \in B$ sono indipendenti: 

$$
f _ {n} (A \cap B) = f _ {n} (A) f _ {n} (B) \Leftrightarrow \mathbb {P} (A \cap B) = \mathbb {P} (A) \mathbb {P} (B)
$$


## L’approccio assiomatico alla teoria della probabilità

> [!quote]
> L'approccio assiomatico **non** definisce cos'è la probabilità nel mondo reale, ma stabilisce le **regole matematiche** che deve rispettare per essere definita tale.

Si consideri una famiglia di sottoinsiemi di $\Omega$, sia essa $\mathcal { E } = \{ A _ { 1 } , . . . , A _ { N } \}$ 

Si assuma che la famiglia $E$ soddisfi le seguenti due proprietà: 

1. Essa è chiusa rispetto all’unione, cioè: 
$$
\text { se } \quad A _ {1} \in \mathcal {E}, A _ {2} \in \mathcal {E} \quad \Rightarrow A _ {1} \cup A _ {2} \in \mathcal {E};
$$

2. Essa è chiusa rispetto alla complementazione, cioè: 
$$
\mathrm{se} \quad A _ {1} \in \mathcal {E} \quad \Rightarrow \overline {{A _ {1}}} \in \mathcal {E};
$$

Sotto le precedenti condizioni, $E$ si definisce un’**Algebra di sotto-insiemi** di $\Omega$, o algebra di eventi. 

Se la collezione $E$ contiene un’infinità (numerabile) di elementi, allora $E$ si definisce una **$\sigma$-algebra** se:
- chiusa rispetto alla complementazione e all’unione
- chiusa rispetto all’unione di un’infinità numerabile di suoi elementi. 

## Proprietà delle Algebre

a. Se $A \in E$, allora $B \in { \mathcal { E } }$ $\implies$ $A \cap B \in { \mathcal { E } }$. Infatti, per la relazione di De Morgan abbiamo: 

$$
A \cap B = \overline {{\overline {{A}} \cup \overline {{B}}}} \in \mathcal {E} \quad \text { poichè } (\overline {{A}}, \overline {{B}}) \in \mathcal {E}
$$

b. Se $A \in E$, allora $B \in { \mathcal { E } }$ $\implies$ $A \setminus B \in { \mathcal { E } }$. Infatti: 

$A \setminus B = A \cap { \overline { { B } } } \in { \mathcal { E } }$ per la precedente proprietà.

c. Se $A$ è un evento qualsiasi, allora la minima algebra che contiene $A$ è $\mathcal { E } = \{ A , \overline { { A } } , \Omega , \emptyset \space  \}$. Infatti: 

- $A$ deve essere elemento di $E$ per la chiusura rispetto alla complementazione; 
- $A \cup { \overline { { A } } } = \Omega$ deve essere un elemento di $E$ per la proprietà di chiusura rispetto all’unione e $\varnothing = { \overline { { \Omega } } }$ deve esso stesso appartenervi per la chiusura rispetto alla complementazione. 

## Spazi di probabilità

Si definisce **legge di probabilità** una funzione con dominio $E$ e co-dominio $[0, 1]$, cioè: 

$$
\mathbb {P}: A \in \mathcal {E} \longrightarrow \mathbb {P} (A) \in [ 0, 1 ]
$$

che soddisfi i seguenti :

> [!theorem] **Assiomi di Kolmogorov**: 
> 1. Non negatività, cioè $\mathbb { P } ( A ) \geq 0 \ \forall \space A \in \mathcal { E }$ 
> 2. Normalizzazione, cioè $\mathbb { P } ( \Omega ) = 1$ 
> 3. Sub-additività, cioè: 
A e B incompatibili $\implies$ $( A \cap B = \emptyset \space  ) \ \Longrightarrow \mathbb { P } ( A \cup B ) = \mathbb { P } ( A ) + \mathbb { P } ( B )$ 
>
> 	3a. **Numerabile additività**. Se $\{ B _ { n } \} _ { n \in \space \mathbb { N } } \ \dot { \textbf { e } }$ una collezione numerabile di eventi incompatibili, allora: 
>
>$$
\mathbb {P} \left(\cup_ {n = 1} ^ {\infty} B _ {n}\right) = \sum_ {n = 1} ^ {\infty} \mathbb {P} \left(B _ {n}\right)
>$$

La terna $(\Omega, E, P)$ si definisce **Spazio di Probabilità**. 

## Proprietà delle leggi di probabilità ("""dimosrazioni""")

### Eventi complementari
$$
\mathbb {P} (\Omega) = \mathbb {P} (A \cup \overline {{A}}) = \mathbb {P} (A) + \mathbb {P} (\overline {{A}}) = 1 \implies \mathbb {P} (\overline {{A}}) = 1 - \mathbb {P} (A)
$$

### Sottrazione tra insiemi
$$
A = A \cap \Omega = A = A \cap (B \cup \overline {{B}}) = (A \cap B) \cup (A \cap \overline {{B}})
$$

Siccome $( A \cap B ) \in ( A \cap { \overline { { B } } } )$ sono incompatibili, allora ritroviamo la proprietà $\mathbb { P } ( A \cap { \overline { { B } } } ) = \mathbb { P } ( A \setminus B ) = \mathbb { P } ( A ) - \mathbb { P } ( A \cap B )$. 

### Unione di eventi non incompatibili
$( A \cap B \neq \varnothing )$ . Osserviamo preliminarmente che $A = A \cup \left( B \cap { \overline { { A } } } \right)$, per cui:

$$
\mathbb {P} (A) = \mathbb {P} (A) + \underbrace {\mathbb {P} (B \cap \overline {{A}})} _ {= \mathbb {P} (B) - \mathbb {P} (A \cap B)} = \mathbb {P} (A) + \mathbb {P} (B) - \mathbb {P} (A \cap B)
$$
## Variabile Aleatoria

Una **variabile aleatoria** è una funzione che associa a ogni possibile risultato elementare $\omega$ di un esperimento casuale un numero reale $x$.

In termini formali, data uno spazio campionario $\Omega$, una variabile aleatoria $X$ è una funzione:
$$X: \Omega \to \mathbb{R}$$
tale che a ogni esito $\omega \in \Omega$ corrisponda un unico valore $x = X(\omega) \in \mathbb{R}$.

## Strumenti per descrivere la distribuzione di X

La sequenza di numeri $\mathbb { P } ( X = x ) = p _ { X } ( x ) , x \in \mathcal { X }$ si chiama **probability mass function** (pmf) o **Distribution Function** (DF) o **probability density function** (pdf) della variabile aleatoria $X$. 

Ovviamente, date le proprietà della probabilità: 

$$
p _ {X} (x) = \lim _ {n \rightarrow \infty} \frac {n _ {x}}{n} \rightarrow p _ {X} (x) \geq 0 , \quad \sum_ {x \in \mathcal {X}} p _ {X} (x) = 1
$$

dove $n _ { x } = n _ { \{ X = x \} }$ rappresenta il numero di occorrenze dell’evento $\{ X = x \}$.


Per come è stata definita, la probabilità è una funzione definita su un insieme di sottoinsiemi di $\Omega$ e ha valori in $[0, 1]$, cioè: 

$$
\mathbb {P}: A \subseteq \Omega \to \mathbb {P} (A) \in [ 0, 1 ]
$$

In realtà, bisognerebbe strutturare $\Omega$ in modo opportuno (cioè introdurre un’algebra di eventi), ma sorvoliamo. 

Il punto è che, quando si passa alle variabili aleatorie la notazione corretta sarebbe: 

$$
\text { Probabilità } (X = x) = \mathbb {P} (\omega \in \Omega : X (\omega) = x)
$$

Per contro, noi usiamo la notazione semplificata $\mathbb { P } ( X = x )$, talvolta ”complicandola” nella forma $\mathbb { P } ( \{ X = x \} )$, che evoca che a rigore ci riferiamo a un insieme di punti di $\Omega .$. Useremo queste notazioni intercambiabilmente ogni volta che non ci sia il pericolo di generare equivoci. 

> [!quote] Osservazione sull'uso del linguaggio tecnico
> Nel gergo comune dell'ingegneria elettronica e delle telecomunicazioni, le espressioni "la pdf di $X$" o "la DF di $X$" vengono spesso utilizzate in modo colloquiale come sinonimi generici per indicare la legge di distribuzione della variabile aleatoria $X$, indipendentemente dal fatto che essa sia descritta da una funzione di massa (pmf), una densità (pdf) o una funzione cumulativa (DF).
>> [!def] Probability Mass Function (pmf)
>> La **funzione di massa di probabilità** $p_X(x)$ è definita per le variabili aleatorie discrete come:
>> $$p_X(x) = \mathbb{P}(X = x)$$
>
>> [!def] Probability Density Function (pdf)
>> La **funzione di densità di probabilità** $f_X(x)$ è definita per le variabili aleatorie continue e descrive la distribuzione della probabilità tramite l'area sottesa alla curva:
>> $$\mathbb{P}(a \leq X \leq b) = \int_{a}^{b} f_X(x) \, dx$$
>
>> [!def] Funzione di Ripartizione (DF)
>> La **funzione di ripartizione** $F_X(x)$ è una funzione cumulativa che indica la probabilità che la variabile aleatoria $X$ assuma un valore minore o uguale a $x$:
>> $$F_X(x) = \mathbb{P}(X \leq x)$$
>> La DF può essere ricavata dalle altre funzioni di distribuzione in base alla natura della variabile:
>> 1. **Caso Discreto:** La DF è la somma cumulativa delle masse di probabilità:
   $$F_X(x) = \sum_{x_i \leq x} p_X(x_i)$$
 2. **Caso Continuo:** La DF è l'integrale della densità fino al punto $x$:
    >>$$F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt$$

## La media campionaria

Una variabile aleatoria $X$ si dice **caratterizzata** se conosci tutto quello che c'è da sapere dal punto di vista probabilistico su quella variabile; 

Esistono caratterizzazioni meno precise che sono spesso utili: una di queste è la **media campionaria**.

Si supponga di avere la variabile aleatoria $X ( \omega )$ e si supponga di compiere $n$ esperimenti; 

La collezione dei risultati sarà $[ X ( \omega _ { 1 } ) , \dots , X ( \omega _ { n } ) ]$ 

Una scelta naturale per avere un’idea del comportamento di $X ( \omega ) \ { \dot { \mathsf { e } } }$ eseguire la media campionaria delle misure, cioè:

$$
\boxed {\overline {{X _ {n}}} = \frac {1}{n} \sum_ {i = 1} ^ {n} X (\omega_ {i})}
$$

## La media statistica / Valore atteso

Riconsideriamo la media campionaria 

$$
\overline {{X _ {n}}} = \frac {1}{n} \sum_ {i = 1} ^ {n} X (\omega_ {i})
$$

Naturalmente, siccome $X ( \omega _ { i } ) \in \mathcal { X } = \{ x _ { 1 } , . . . , x _ { M } \}$, al crescere di $n$ avremo che $X ( \omega )$ assumerà $n _ { 1 }$ volte il valore $x _ { 1 } , \ n _ { 2 }$ il valore $x _ { 2 }$ e così via (il caso $M = \infty$ va trattato come caso limite). Quindi, per $n \to  \infty ;$ 

$$
\boxed {\overline {{X _ {n}}} = \frac {1}{n} \sum_ {i = 1} ^ {M} n _ {i} x _ {i} = \sum_ {i = 1} ^ {M} x _ {i} f _ {n} (x _ {i}) \rightarrow \sum_ {i = 1} ^ {M} x _ {i} \mathbb {P} (X = x _ {i}) = \sum_ {i = 1} ^ {M} x _ {i} p _ {X} (x _ {i}) \stackrel {\text { def }} {=} \mathbb {E} [ X ]}
$$

dove ricordiamo che $\begin{array} { r } { f _ { n } ( x _ { i } ) = \frac { n _ { \{ X = x _ { i } \} } } { n } } \end{array}$ 

La quantità $\mathbb { E } \left[ X \right]$ si definisce **media statistica** della variabile aleatoria $X$.

> [!tip] Legge dei Grandi Numeri
> Man mano che le osservazioni crescono, la media si avvicina al valore atteso teorico.
## La variabile Uniforme

Una variabile aleatoria $X$ che assuma valore in un qualsiasi alfabeto $\mathcal { X }$ di cardinalità finita, $| { \mathcal { X } } | = M$, si dice **uniformemente distribuita** su $\mathcal { X }$ (in breve, $X \sim \mathcal { U } ( \mathcal { X } ) )$) se: 

$$
p _ {X} (x) = \mathbb {P} (X = x) = \frac {1}{M} \quad \forall \space x \in \mathcal {X}
$$

Ovviamente $p x ( x )$ soddisfa le condizioni necessarie per poter essere una pmf; 

Il calcolo della media è immediato: 

$$E[X] = \frac{1}{n} \sum_{i=1}^n x_i$$
$\mathbb { E } [ X ] = \sum _ { x \in \mathcal { X } } x p _ { X } ( x ) = \frac { 1 } { M } \sum _ { x \in \mathcal { X } } x =$ Media aritmetica dei valori dell’alfabeto 

## La variabile Poissoniana

Una variabile aleatoria $X$ si dice **Poissoniana** di parametro $\lambda$ (in breve, $X \sim \mathcal { P } ( \lambda ) )$) se: 

1. Il suo alfabeto è $\mathcal { X } = \{ 0 , 1 , 2 , . . . \} = \mathbb { N } _ { 0 }$ 

2. La sua pmf è data da: 

$$P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$$
$$
p _ {X} (k) = \mathbb {P} (X = k) = \frac {\lambda^ {k}}{k !} e ^ {- \lambda}, \qquad k \in \mathbb {N} _ {0}
$$

Si noti che la precedente soddisfa le condizioni per poter essere una pmf, in quanto: 

$$\sum_{k=0}^\infty \frac{e^{-\lambda} \lambda^k}{k!} = e^{-\lambda} \sum_{k=0}^\infty \frac{\lambda^k}{k!} = e^{-\lambda} e^\lambda = 1$$
$$
p _ {K} (k) \geq 0 \quad \sum_ {x \in \mathcal {X}} p _ {X} (x) = e ^ {- \lambda} \overbrace {\sum_ {k = 0} ^ {\infty} \frac {\lambda^ {k}}{k !}} ^ {e ^ {\lambda}} = 1
$$

La sua media vale 

$$E[X] = \lambda$$
$$
\mathbb {E} [ X ] = \sum_ {x \in \mathcal {X}} x p _ {X} (x) = e ^ {- \lambda} \sum_ {k = 1} ^ {\infty} k \frac {\lambda^ {k}}{k !} = \lambda e ^ {- \lambda} \sum_ {k = 1} ^ {\infty} \frac {\lambda^ {k - 1}}{(k - 1) !} = \lambda
$$

## PMF condizionali

La pmf di una variabile aleatoria qualsiasi $X$ condizionata a un qualsiasi evento $A \subseteq \Omega$ a probabilità non nulla nella forma: 

$$P(X=x | A) = \frac{P(\{X=x\} \cap A)}{P(A)}$$
$$
p _ {X \mid A} (x) = \mathbb {P} (x \mid A) = \frac {\mathbb {P} (\{X = x \} \cap A)}{\mathbb {P} (A)} \quad x \in \mathcal {X}
$$

Ovviamente, $p _ { X \mid A } ( x )$ al variare di $x$ in $X$ con $A$ prefissato è una pmf.

## Regola della probabilità totale per le pmf

Ricordiamo che, per un qualunque evento $C \subseteq \Omega$ e per una qualunque partizione $\{ E \} _ { i = 1 } ^ { M }$ si ha: 

$$
\mathbb {P} (C) = \sum_ {i = 1} ^ {M} \mathbb {P} (C | E _ {i}) \mathbb {P} (E _ {i})
$$

> [!rb] R.B.
> Sappiamo che la probabilità che avvengano contemporaneamente $A$ e $B_i$ si può scrivere come:
> 
> $$\mathbb{P}(A \cap B_i) = \mathbb{P}(A | B_i) \cdot \mathbb{P}(B_i)$$

Pertanto, specializzando la precedente a $C = \{ X = x \}$ si ha: 

$$
\mathbb {P} (X = x) = p _ {X} (x) = \sum_ {i = 1} ^ {M} \mathbb {P} (\{X = x \} | E _ {i}) \mathbb {P} (E _ {i}) = \sum_ {i = 1} ^ {M} p _ {X | E _ {i}} (x) \mathbb {P} (E _ {i})
$$

## Medie condizionali

Un analogo sviluppo è possibile sulle medie. Infatti: 

$$
\mathbb {E} [ X ] = \sum_ {x \in \mathcal {X}} x p _ {X} (x) = \sum_ {x \in \mathcal {X}} x \sum_ {i = 1} ^ {M} p _ {X | E _ {i}} (x) \mathbb {P} (E _ {i}) =
$$

$$
\boxed {\sum_ {i = 1} ^ {I} \mathbb {P} (E _ {i}) \underbrace {\sum_ {x \in \mathcal {X}} x p _ {X | E _ {i}} (x)} _ {\mathbb {E} [ X | E _ {i} ]}}
$$

dove quindi si è definita la media condizionata 

$$
\boxed {\mathbb {E} \left[ X | E _ {i} \right] = \sum_ {x \in \mathcal {X}} x p _ {X | E _ {i}} (x)}
$$

## Funzioni di variabili aleatorie

Si assuma che:
- $X = X ( \omega )$ sia una variabile aleatoria con alfabeto $X$ con pmf $\{ p _{X} \} _ { x \in \mathcal { X } }$ 
- $g(\cdot)$ una funzione il cui insieme di definizione includa i punti di $X$ 
- Si forma la nuova variabile aleatoria: 

$$
Y = g (X) = g [ X (\omega) ] \in \mathcal {Y} \quad \text {   dove   } \mathcal {Y} = g (\mathcal {X})
$$
> La pmf $p_Y(y)$ descrive la distribuzione di probabilità di $Y$ a partire dai valori di $X$.

Problema: Ricavare una caratterizzazione di $Y$ dalla caratterizzazione di $X$ in termini di 

- pmf, $p _ { Y } ( y ) , \space y  \in \mathcal { Y }$ 

- media statistica, $\begin{array} { r } { \mathbb { E } [ Y ] = \sum _ { y \in \mathcal { Y } } y p _ { Y } ( y ) } \end{array}$ 

### PMF
Distinguiamo due casi:

a) $\{ g ( x ) \} _ { x \in \mathcal { X } }$ biunivoca, cioè: 

$$
| \mathcal {Y} | = | \mathcal {X} | \Leftrightarrow \forall \space y \in \mathcal {Y} \text {   è   definita   } x = g ^ {- 1} (y)
$$

b) $\{ g ( x ) \} _ { x \in \mathcal { X } }$ univoca, cioè associa a più valori di $X$ un solo valore di $Y$: 

$$
\mathcal {X} = \{x _ {1}, \dots , x _ {n} \} \quad \mathcal {Y} = \{y _ {1}, \dots , y _ {m} \} \quad n > m
$$

Nel caso [a] si tratta solo di una ridenominazione dell’alfabeto: 

$$
p _ {Y} (y _ {i}) = \mathbb {P} (Y = g (x _ {i})) = \mathbb {P} (X = g ^ {- 1} (y _ {i})) = \mathbb {P} (X = x _ {i}) = p _ {X} (x _ {i})
$$

Nel caso [b] vale la precedente relazione per tutti i punti di $Y$ in cui $g ( y ) \ { \dot { \mathsf { e } } }$ invertibile. Per un punto $y _ { k }$ tale che $g ( x _ { 1 } ^ { ( k ) } ) = g ( x _ { 2 } ^ { ( k ) } ) = \ldots = g ( x _ { { L _ { k } } } ^ { ( k ) } ) = y _ { k }$ avremo: 

$$
p _ {Y} (y _ {k}) = \mathbb {P} \left(\cup_ {i = 1} ^ {L _ {k}} \{X = x _ {i} ^ {(k)} \}\right) = \sum_ {i = 1} ^ {L _ {k}} \mathbb {P} \left(X = x _ {i} ^ {(k)}\right) = \sum_ {i = 1} ^ {L _ {k}} p _ {X} (x _ {i} ^ {(k)})
$$

### Media di funzioni di variabili aleatorie

Cominciamo con il seguire la stessa suddivisione introdotta per il caso delle pmf. 

Funzioni biunivoche - In questo caso c’è solo una ridenominazione dell’alfabeto, per cui: 

$$
\mathbb {E} [ Y ] = \sum_ {y \in \mathcal {Y}} y p _ {Y} (y) = \mathbb {E} [ g (X) ] = \sum_ {x \in \mathcal {X}} g (x) p _ {X} (x)\tag{1}
$$

Funzioni univoche - Avremo in questo caso: 

$$
\mathbb {E} [ Y ] = \sum_ {y \in \mathcal {Y}} y p _ {Y} (y) = \sum_ {y \in \mathcal {Y}} \sum_ {x: y = g (x)} g (x) p _ {X} (x)\tag{2}
$$

Si noti comunque che l’equazione (1) include l’equazione (2) come caso speciale. In conclusione adottiamo la forma generale (1) che prende anche il nome di Teorema fondamentale per il calcolo della media.

> [!theorem] Teorema (*Fondamentale per il calcolo della media*)
>  La media di una funzione di una variabile aleatoria può essere calcolata come la media condizionata dei valori della funzione:
> 
> $$E[g(X)] = \sum_{y} g(y) P(Y=y)$$
> (dove $Y = g(X)$)

### Valore quadratico medio e varianza di una variabile aleatoria

Data una variabile aleatoria $X \sim p _ { X } ( x ) , x \in \mathcal { X }$ , con media $\mu _ { X } = \operatorname { \mathbb { E } } [ X ]$ definiamo: 

Il **valore quadratico medio** (Mean Square) di $X$ : 

$$
X _ {\text { rms }} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] = \sum_ {x \in \mathcal {X}} x ^ {2} p _ {X} (x)
$$

Il **valore efficace** (root mean square, rms) di $X$ : 

$$
X _ {\text { rms }} = \sqrt {\mathbb {E} \left[ X ^ {2} \right]} = \sqrt {\sum_ {x \in \mathcal {X}} x ^ {2} p _ {X} (x)}
$$

La **varianza** di $X$ : 

$$
\sigma_ {X} ^ {2} = \mathbb {E} \left[ (X - \mu_ {X}) ^ {2} \right] = \sum_ {x \in \mathcal {X}} (x ^ {2} + \mu_ {X} ^ {2} - 2 x \mu_ {X}) p _ {X} (x) = X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}
$$

La **deviazione standard** di $X$ : 

$$
\sigma_ {X} = \sqrt {\sigma_ {X} ^ {2}} = \sqrt {\mathbb {E} [ X ^ {2} ] - \mu_ {X} ^ {2}} = \sqrt {X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}}
$$

### Il significato della varianza e della deviazione standard

Supponiamo di non avere una caratterizzazione completa di una variabile aleatoria $X$.

Se $\mathcal { X } \subseteq [ 0 , + \infty [$ (cioè la variabile è non negativa), la media $\mu x$ fornisce un'indicazione del suo comportamento, sebbene imprecisa. Se invece $X$ può assumere sia valori positivi che negativi, la media non costituisce un indicatore significativo per descrivere il comportamento della variabile aleatoria.

In entrambi i casi, è fondamentale determinare la probabilità di osservare valori di $X$ significativamente distanti dalla propria media. Nel caso in cui sia nota la coppia $( \mu _ { X } , \sigma _ { X } )$, tale analisi può essere condotta mediante la **Disuguaglianza di Chebyshev**:

$$
\mathbb {P} \left\{| X - \mu_ {X} | > k \sigma_ {X} \right\} = \mathbb {P} \left\{\mu_ {X} - k \sigma_ {X} \leq X \leq \mu_ {X} + k \sigma_ {X} \right\} \geq 1 - \frac {1}{k ^ {2}}
$$

Si deduce che un parametro fondamentale è il rapporto $\frac { \mu _ { X } } { \sigma _ { X } }$:
- Valori elevati di questo rapporto indicano una **pmf** (funzione di probabilità) molto concentrata intorno alla media (variabile "poco aleatoria").
- Valori bassi implicano un'elevata aleatorietà.

### La disuguaglianza di Chebyshev

Sia $Z$ una variabile non negativa definita su un alfabeto discreto ${ \mathcal { Z } } \subseteq [ 0 , + \infty [$ secondo una pmf $p _ { Z } ( z )$. Si valuti la probabilità che $Z$ sia non inferiore a un qualunque valore $\delta \in { \mathcal { Z } }$:

$$
\mathbb {P} (Z \geq \delta) = \sum_ {z: z \geq \delta} p _ {Z} (z) \stackrel {{a}} {{\leq}} \sum_ {z: z \geq \delta} \left(\frac {z}{\delta}\right) ^ {2} p _ {Z} (z) \stackrel {{b}} {{\leq}} \sum_ {z \in \mathcal {Z}} \left(\frac {z}{\delta}\right) ^ {2} p _ {Z} (z) \stackrel {{c}} {{=}} \frac {\mathbb {E} [ Z ^ {2} ]}{\delta^ {2}}\tag{3}
$$

Le diverse componenti della derivazione sono le seguenti:
1. Il punto (a) deriva dall'essere $\begin{array} { r } { \left( \frac { z } { \delta } \right) ^ { 2 } \geq 1 } \end{array}$ per $z \geq \delta ;$.
2. Il punto (b) deriva dal fatto che, estendendo la sommatoria su tutto $\mathcal { Z }$, si aggiungono termini non negativi.
3. Il punto (c) deriva dalla definizione di valore quadratico medio.

La disuguaglianza di Chebyshev si ricava ponendo $Z = | X - \mu x | \geq 0$ e $\delta = k \sigma _ { X }$ nella equazione (3), notando che con questa scelta:

$$
\mathbb {E} [ Z ^ {2} ] = \mathbb {E} [ | X - \mu_ {X} | ^ {2} ] = \mathbb {E} [ (X - \mu_ {X}) ^ {2} ] = \sigma_ {X} ^ {2}.
$$

### Quadro sintetico delle proprietà di media e varianza

#### Proprietà della Media ($\mathbb{E}$)
*   **Linearità:** Se $(a, b)$ sono costanti reali:
$$\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$$
*(Dato che $\mathbb{E}[b] = b$)*

*   **Non-negatività:** Se $X(\omega) \geq 0$ per ogni $\omega \in \Omega$ (ovvero se $\mathcal{X} \subseteq [0, +\infty[$), allora:
$$\mathbb{E}[X] \geq 0$$
#### Proprietà della Varianza ($\sigma^2$)
*   **Non-negatività:** La varianza è sempre non negativa:
$$\sigma_X^2 \geq 0$$
*(In quanto media della variabile non negativa $(X - \mu_X)^2$)*

*   **Trasformazione Lineare:** Se $Y = aX + b$, allora la varianza è:
$$\sigma_Y^2 = a^2 \sigma_X^2$$

>[!dim] Dimostrazione:
$$\mu_Y = a\mu_X + b$$
$$\mathbb{E}[Y^2] = \mathbb{E}[a^2X^2 + 2abX + b^2] = a^2\mathbb{E}[X^2] + 2ab\mathbb{E}[X] + b^2$$
$$\sigma_Y^2 = a^2\mathbb{E}[X^2] + 2ab\mu_X + b^2 - (a\mu_X + b)^2 = a^2\sigma_X^2$$
#### Relazioni Correlate
Come conseguenza delle relazioni precedenti, si ottiene anche:
$$\mathbb{E}[Y^2] = Y_{\text{rms}}^2 = a^2 X_{\text{rms}}^2 + 2ab\mu_X + b^2$$
**Nota finale:** Per variabili a media nulla ($\mu_X = 0$), vale la relazione:
$$\sigma_X^2 = X_{\text{rms}}^2$$
## Definizione di variabili multiple

Formalmente, una coppia di variabili aleatorie (o **variabile doppia**) è definita — in analogia con le variabili singole — nella forma:

$$
X, Y: \omega \in \Omega \longrightarrow (X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y} \subseteq \mathbb {R} ^ {2}
$$

dove $\mathcal { X } \in \mathcal { V }$ sono gli alfabeti di $X$ e di $Y$ rispettivamente.

In altre parole, il risultato di un esperimento $\omega _ { * }$ non è un unico valore $X ( \omega _ { * } ) = x _ { * } \in \mathcal { X }$, ma una coppia ordinata $( X ( \omega _ { * } ) , Y ( \omega _ { * } ) ) = ( x _ { * } , y _ { * } )$, che varia nel prodotto cartesiano $\mathcal { X } \times \mathcal { V }$.

### pmf/DF/pdf congiunta
$$p_{X,Y}(x,y) = \mathbb{P}(\{X = x\} \cap \{Y = y\}) = \lim_{n \to \infty} \frac{n_{X=x, Y=y}}{n}, \quad (x,y) \in \mathcal{X} \times \mathcal{Y}$$
In altre parole, $p_{X,Y}(x,y)$ è una tabella di $|\mathcal{X}| \cdot |\mathcal{Y}|$ numeri che — ovviamente — gode di opportune proprietà.

#### Proprietà

Le proprietà fondamentali della pmf congiunta (identiche alla pmf classica) sono:
$$p_{X,Y}(x,y) \geq 0 \quad \text{e} \quad \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p_{X,Y}(x,y) = 1$$

>[!dim] Dimostrazione:
$$1 = \mathbb{P}(\Omega) = \mathbb{P}\left(\bigcup_{x \in \mathcal{X}} \bigcup_{y \in \mathcal{Y}} \{X = x, Y = y\}\right) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} \underbrace{\mathbb{P}(\{X = x, Y = y\})}_{p_{X,Y}(x,y)}$$
Questo perché l'evento elementare $\{X = x, Y = y\}$ è incompatibile con ogni altro evento elementare $\{X = x', Y = y'\}$ per $x \neq x'$ e/o $y \neq y'$.

###### Marginalizzazione
> Si usa per sapere la probabilità di una variabile aleatoria indipendentemente dall' altra. (riga o colonna della tabella di cui parlavamo)

Si noti che $\bigcup_{x \in \mathcal{X}} \{X = x\} = \Omega$ e $\bigcup_{y \in \mathcal{Y}} \{Y = y\} = \Omega$, per cui:
$$\{X = x\} = \{X = x\} \cap \Omega = \{X = x\} \cap \bigcup_{y \in \mathcal{Y}} \{Y = y\} = \bigcup_{y \in \mathcal{Y}} (\{X = x\} \cap \{Y = y\})$$
Da cui deriva:
$$\sum_{y \in \mathcal{Y}} p_{X,Y}(x,y) = p_X(x)$$
$$\Longrightarrow \mathbb{P}(\{X = x\}) = \mathbb{P}\left(\bigcup_{y \in \mathcal{Y}} \{\{X = x\} \cap \{Y = y\}\}\right) = \sum_{y \in \mathcal{Y}} \mathbb{P}(\{X = x\} \cap \{Y = y\})$$
Si ha quindi la proprietà di **marginalizzazione**:
$$\sum_{y \in \mathcal{Y}} p_{X,Y}(x,y) = p_X(x) \quad \text{e} \quad \sum_{x \in \mathcal{X}} p_{X,Y}(x,y) = p_Y(y)$$
**Conclusione:**
Caratterizzare congiuntamente $(X, Y)$ significa anche caratterizzarle marginalmente, mentre il viceversa non è necessariamente vero.

### Variabili indipendenti

Due variabili aleatorie $X \in \mathcal{X}$ e $Y \in \mathcal{Y}$ sono **indipendenti** $\iff$ gli eventi $\{X = x\}$ e $\{Y = y\}$ sono indipendenti.

Per due variabili indipendenti, la pmf congiunta si fattorizza nel prodotto delle rispettive marginali:
$$p_{X,Y}(x,y) = \mathbb{P}(\{X = x\} \cap \{Y = y\}) = \mathbb{P}(\{X = x\}) \mathbb{P}(\{Y = y\}) = p_X(x) p_Y(y)$$
Questo è l'unico caso in cui la conoscenza delle sole pmf marginali $p_X(x)$ e $p_Y(y)$ è sufficiente per determinare univocamente la pmf congiunta.

#### Generalizzazione a m variabili aleatorie
Poiché il concetto di pmf congiunta si estende a una $m$-pla di variabili aleatorie $(X_1, \dots, X_m) \in \mathcal{X}_1 \times \dots \times \mathcal{X}_m \subseteq \mathbb{R}^m$ attraverso la seguente definizione:
$$p_{X_1, \dots, X_m}(x_1, \dots, x_m) = \mathbb{P}(\{X_1 = x_1\} \cap \dots \cap \{X_m = x_m\})$$
il concetto di indipendenza può essere generalizzato analogamente:
$$p_{X_1, \dots, X_m}(x_1, \dots, x_m) = \prod_{i=1}^m p_{X_i}(x_i)$$
Che può essere espresso formalmente come:
$$\prod_{i=1}^m \mathbb{P}(\{X_i = x_i\}) = \prod_{i=1}^m p_{X_i}(x_i)$$
### Le pmf condizionate

Si considerino variabili aleatorie $X \in \mathcal{X}$ e $Y \in \mathcal{Y}$ con assegnata pmf congiunta $p_{X,Y}(x,y)$.

Applicando all'evento $\{X = x, Y = y\} = \{X = x\} \cap \{Y = y\}$ la legge della probabilità composta:
$$
p_{X,Y}(x,y) = \mathbb{P}(\{X = x\} \cap \{Y = y\}) = \underbrace{\mathbb{P}(\{Y = y\} \mid \{X = x\})}_{p_{Y|X}(y|x)} \cdot \underbrace{\mathbb{P}(\{X = x\})}_{p_X(x)}
$$
$p_{Y|X}(y|x)$ è la **legge di probabilità condizionata** (o pmf condizionata) di $Y$ dato $x$. Come la legge congiunta, $p_{Y|X}(y|x)$ è una tabella di $|\mathcal{X}| \cdot |\mathcal{Y}|$ numeri che soddisfa alcune proprietà fondamentali.

Dalla definizione di probabilità condizionata, abbiamo:
$$p_{Y|X}(y|x) p_X(x) = p_{X|Y}(x|y) p_Y(y)$$
Da cui si ricavano le seguenti formule:
$$p_{Y|X}(y|x) = \frac{p_{X,Y}(x, y)}{p_X(x)}$$
$$p_{X|Y}(x|y) = \frac{p_{Y|X}(y|x) p_X(x)}{p_Y(y)}$$
> [!theorem] Legge di Bayes
> $$
> p_{X|Y}(x|y) = \frac{p_{Y|X}(y|x) p_X(x)}{p_Y(y)}
> $$

#### Alcune proprietà

Se fissiamo $x$ e facciamo variare $y \in \mathcal{Y}$, la funzione $p_{Y|X}(y|x)$ definisce una legge di probabilità. Infatti:
$$
p_{Y|X}(y|x) \geq 0, \quad \sum_{y \in \mathcal{Y}} p_{Y|X}(y|x) = \mathbb{P}\left(\bigcup_{y \in \mathcal{Y}} \{Y = y\} \mid \{X = x\}\right) = \mathbb{P}(\Omega \mid \{X = x\}) = 1
$$
La proprietà di marginalizzazione della pmf congiunta può essere espressa in termini di pmf condizionate come segue:
$$p_X(x) = \sum_{y \in \mathcal{Y}} p_{X,Y}(x,y) = \sum_{y \in \mathcal{Y}} p_{X|Y}(x|y) p_Y(y)$$
E viceversa:
$$p_{X,Y}(x,y) = p_{Y|X}(y|x) p_X(x)$$
$$p_Y(y) = \sum_{x \in \mathcal{X}} p_{X,Y}(x,y) = \sum_{x \in \mathcal{X}} p_{Y|X}(y|x) p_X(x)$$

>[!rb] R.B.
>Si noti che queste espressioni non sono altro che la **legge della probabilità totale** applicata rispettivamente:
> 1. Per l'evento $\{X=x\}$ rispetto alla partizione $\Omega = \bigcup_{y \in \mathcal{Y}} \{Y=y\}$.
> 2. Per l'evento $\{Y=y\}$ rispetto alla partizione $\Omega = \bigcup_{x \in \mathcal{X}} \{X=x\}$.

Infine, se le variabili $X$ e $Y$ sono **indipendenti**, le pmf condizionate si semplificano nelle rispettive marginali:
$$p_{Y|X}(y|x) = p_Y(y) \quad \text{e} \quad p_{X|Y}(x|y) = p_X(x)$$
#### Generalizzazione

Si consideri una terna di variabili aleatorie $(X, Y, Z)$ distribuite secondo la pmf congiunta $p_{X,Y,Z}(x,y,z)$, dove $(x,y,z) \in \mathcal{X} \times \mathcal{Y} \times \mathcal{Z}$.

Applicando consecutivamente la regola della probabilità composta, otteniamo diverse scomposizioni:
$$
p_{X,Y,Z}(x, y, z) = p_{Z|X,Y}(z|x,y) p_{Y|X}(y|x) p_X(x)
$$
$$
p_{X,Y,Z}(x, y, z) = p_{X|Y,Z}(x|y,z) p_{Y|Z}(y|z) p_Z(z)
$$
Queste formulazioni introducono la
>[!def] **Regola della catena** 
>(dove ogni permutazione dei pedici e degli argomenti è possibile). 
>Ad esempio:
$$p_{X|Y,Z}(x|y,z) = \frac{p_{X,Y|Z}(x,y|z)}{p_{Y|Z}(y|z)} \implies p_{X,Y,Z}(x,y,z) = p_Z(z) p_{Y|Z}(y|z) p_{X|Y,Z}(x|y,z)$$
La terna è **indipendente** $\iff$ le pmf condizionate coincidono con le marginali:
$$p_{X|Y,Z}(x|y,z) = p_X(x), \quad p_{Y|X,Z}(y|x,z) = p_Y(y), \quad p_{Z|X,Y}(z|x,y) = p_Z(z)$$
In questo caso, la pmf congiunta si riduce al prodotto delle marginali:
$$p_{X,Y,Z}(x,y,z) = p_X(x) p_Y(y) p_Z(z)$$
## Funzioni di variabili doppie

Data una **variabile casuale doppia discreta** $(X, Y)$ regolata da una funzione di massa di probabilità (pmf) congiunta $p_{X,Y}(x, y)$, definita su $\mathcal{X} \times \mathcal{Y}$, si consideri una nuova variabile casuale discreta $Z$ come trasformazione deterministica delle prime due attraverso una funzione scalare $g(x, y)$:
$$Z = g(X, Y)$$
L'obiettivo è determinare la legge di probabilità (pmf) della nuova variabile $Z$, indicata come $p_Z(z)$, a partire dalla conoscenza della pmf congiunta $p_{X,Y}(x, y)$. Tale determinazione dipende dalla natura della funzione $g(x,y)$:

#### Trasformazione Biunivoca (Inversa Unica)

Se la funzione $g(x,y)$ mappa ogni singola coppia del dominio $(x,y)$ in un valore di $z$ unico e distinto (ovvero la funzione è iniettiva sullo spazio di supporto), esiste un'unica coppia invertibile $(x(z), y(z))$ tale per cui $z = g(x, y)$.

In questo caso, la probabilità che $Z$ assuma il valore $z$ coincide esattamente con la probabilità congiunta dell'unico punto di partenza che lo ha generato:
$$p_Z(z) = \mathbb{P}(Z = z) = p_{X, Y}(x(z), y(z))$$
#### Trasformazione Non Biunivoca (Collassamento delle Probabilità)

Se la funzione $g(x,y)$ assegna lo stesso valore $z$ a più coppie distinte $(x,y)$ (trasformazione *molti-a-uno*), si verifica un fenomeno di **collassamento (o accumulo) delle probabilità**.

Per determinare la probabilità del punto $z$, è necessario individuare l'insieme di controimmagini $\mathcal{A}(z)$, definito come il sottoinsieme dello spazio di supporto contenente tutte le coppie che producono come output esattamente $z$:
$$\mathcal{A}(z) = \{ (x, y) \in \mathcal{X} \times \mathcal{Y} : g(x, y) = z \}$$
La pmf di $Z$ si ottiene applicando il principio di additività, ovvero **sommando** le probabilità congiunte di tutte le coppie appartenenti a tale insieme:
$$p_Z(z) = \sum_{(x, y) \in \mathcal{A}(z)} p_{X, Y}(x, y)$$

### Media / Valore Atteso

Nel contesto delle trasformazioni multivariate, data una **coppia di variabili casuali discrete** $(X, Y)$ regolata da una legge congiunta $p_{X,Y}(x, y)$, è possibile calcolare il valore atteso di una nuova variabile $Z = g(X, Y)$ senza doverne prima ricavare la funzione di massa di probabilità (pmf).

> [!rb] R.B. : Teorema del Calcolo della Media
> Il valore atteso (o media statistica) di una funzione di due variabili casuali discrete si ottiene calcolando la media ponderata dei valori assunti dalla funzione $g(x,y)$, utilizzando come pesi le rispettive probabilità congiunte:
> 
> $$ \mathbb{E}[Z] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} g(x, y) p_{X,Y}(x, y) = \sum_{(x, y) \in \mathcal{X} \times \mathcal{Y}} g(x, y) p_{X,Y}(x, y) $$
#### Proprietà: Il caso della combinazione lineare

Un'applicazione di fondamentale importanza riguarda il caso in cui la trasformazione sia una **combinazione lineare** del tipo $Z = aX + bY$, dove $a$ e $b$ sono costanti deterministiche. 

Sfruttando la proprietà distributiva delle sommatorie e la definizione di pmf marginale, si dimostra formalmente la **linearità del valore atteso**:
$$ \mathbb{E}[aX + bY] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (ax + by) p_{X,Y}(x, y) $$
Sviluppando il prodotto e separando i termini:
$$ = a \sum_{x \in \mathcal{X}} x \underbrace{\sum_{y \in \mathcal{Y}} p_{X,Y}(x, y)}_{p_{X}(x)} + b \sum_{y \in \mathcal{Y}} y \underbrace{\sum_{x \in \mathcal{X}} p_{X,Y}(x, y)}_{p_{Y}(y)} $$
$$ = a \mathbb{E}[X] + b \mathbb{E}[Y] $$
> [!quote] Conseguenza Teorica
> Il valore atteso di una combinazione lineare di variabili casuali è uguale alla combinazione lineare dei loro singoli valori attesi, **indipendentemente dal fatto che le variabili siano statisticamente indipendenti o dipendenti**.

#### Generalizzazione a m variabili

Il principio di linearità si estende per induzione a un numero qualsiasi $m$ di variabili aleatorie $\{X_i\}_{i=1}^m$ regolate da una pmf congiunta arbitraria $p_{X_1, \dots, X_m}(x_1, \dots, x_m)$:
$$ \mathbb{E}\left[ \sum_{i=1}^m a_i X_i \right] = \sum_{i=1}^m a_i \mathbb{E}[X_i] $$
### Teorema della Media Condizionata

Considerando la variabile casuale $Z = g(X, Y)$, possiamo esprimere il suo valore atteso utilizzando la legge di probabilità congiunta $p_{X,Y}(x, y)$ e la sua scomposizione in termini condizionali:
$$
\mathbb{E}[g(X, Y)] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} g(x, y) \underbrace{p_{X,Y}(x, y)}_{p_{X|Y}(x|y) p_Y(y)}
$$
Riorganizzando le sommatorie, otteniamo:
$$
\mathbb{E}[g(X, Y)] = \sum_{y \in \mathcal{Y}} p_Y(y) \sum_{x \in \mathcal{X}} g(x, y) p_{X|Y}(x|y) = \sum_{y \in \mathcal{Y}} h(y) p_Y(y)
$$
In questa espressione, $h(y)$ rappresenta il valore atteso della funzione $g$ condizionato a un valore fissato di $Y$:
$$
h(y) = \mathbb{E}[g(X, Y) | Y = y] \implies h(Y) = \mathbb{E}[g(X, Y) | Y]
$$
Sostituendo questa definizione nell'equazione precedente, si ottiene la formula fondamentale:
$$
\mathbb{E}[g(X, Y)] = \mathbb{E}\left[\space \mathbb{E}[g(X, Y) | Y] \space \right]
$$
Questa relazione è nota come 
>[!theorem] **Teorema della Media Condizionata** (o *Law of Iterated Expectations*)
> Il valore atteso globale $=$valore atteso del valore atteso condizionato. 
> È possibile scambiare i ruoli di $X$ e $Y$ analogamente, ottenendo: $$\mathbb{E}[g(X, Y)] = \mathbb{E}[\mathbb{E}[g(X, Y) | X]]$$

## La covarianza tra due variabili aleatorie

Sia $(X, Y) \sim p_{X,Y}(x, y)$ con $(x, y) \in \mathcal{X} \times \mathcal{Y}$. 

Mentre le coppie $(\mu_X, \sigma_X^2)$ e $(\mu_Y, \sigma_Y^2)$ forniscono informazioni globali sulle distribuzioni marginali $p_X(x)$ e $p_Y(y)$, l'equivalente per le **pmf** (Probability Mass Functions) congiunte è la **covarianza**. Essa misura il grado di dipendenza lineare tra $X$ e $Y$.

> [!def] Covarianza
> La covarianza è una misura statistica che indica la **direzione** della relazione lineare tra due variabili aleatorie.
> * Se positiva, le variabili tendono a crescere insieme
> * Se negativa, tendono a muoversi in direzioni opposte
> 
> Formalmente:
> $$\operatorname{COV}[X, Y] = \mathbb{E}\left[ (X - \mu_X)(Y - \mu_Y) \right] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (x - \mu_X)(y - \mu_Y) p_{X,Y}(x, y)$$
> 
> 
 
> [!def] Correlazione (Cross-correlazione)
> La correlazione tra $X$ e $Y$ (indicata con $R_{X,Y}$) è una misura statistica che quantifica la relazione tra due variabili aleatorie attraverso il valore atteso del loro prodotto. 
>> Intuitivamente, indica quanto le due variabili tendano a variare insieme in modo concorde.
> 
> Formalmente (per variabili discrete):
> $$R_{X,Y} = \mathbb{E}[XY] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} x y p_{X,Y}(x, y)$$

#### Rappresentazione della Covarianza
```easy-tikz
{
  "dimension": false,
  "documentSetup": true,
  "title": "Covarianza (Dipendenza dalla Scala)",
  "size_x_cm": 10,
  "size_y_cm": 10,
  "show_axis_label": true,
  "axis_label_x": "X",
  "axis_label_y": "Y",
  "documentClose": true,
  "showAxis": true,
  "gridSize": 5,
  "xmin": "-10",
  "xmax": "10",
  "ymin": "-10",
  "ymax": "10",
  "axis_style": "box",
  "functions": [
    {
      "expression": "2*x",
      "domain": "-5:5",
      "showLegend": true,
      "color": "blue",
      "thickness": "thick",
      "name": "Scala Ampia (Covarianza Maggiore)"
    },
    {
      "expression": "0.5*x",
      "domain": "-8:8",
      "showLegend": true,
      "color": "orange",
      "thickness": "thick",
      "name": "Scala Ridotta (Covarianza Minore)"
    }
  ],
  "rotationX": 0,
  "rotationZ": 0,
  "coordinateSystem": "cartesian"
}

```
#### Rappresentazione della Correlazione
```easy-tikz
{
  "dimension": false,
  "documentSetup": true,
  "title": "Correlazione (Standardizzata tra -1 e 1)",
  "size_x_cm": 10,
  "size_y_cm": 10,
  "show_axis_label": true,
  "axis_label_x": "X",
  "axis_label_y": "Y",
  "documentClose": true,
  "showAxis": true,
  "gridSize": 5,
  "xmin": "-5",
  "xmax": "5",
  "ymin": "-5",
  "ymax": "5",
  "axis_style": "box",
  "functions": [
    {
      "expression": "x",
      "domain": "-4:4",
      "showLegend": true,
      "color": "green",
      "thickness": "thick",
      "name": "Relazione Perfetta (R = 1)"
    },
    {
      "expression": "x + 0.3*sin(4*x)",
      "domain": "-4:4",
      "showLegend": true,
      "color": "purple",
      "thickness": "thin",
      "name": "Dispersione/Rumore (R < 1)"
    }
  ],
  "rotationX": 0,
  "rotationZ": 0,
  "coordinateSystem": "cartesian"
}

```

### Proprietà della covarianza

#### a) Relazione tra momento di ordine 2 e covarianza
Sfruttando la linearità del valore atteso, possiamo scomporre la covarianza come segue:
$$\operatorname{COV}[X, Y] = \mathbb{E}[XY - \mu_X Y - \mu_Y X + \mu_X \mu_Y] = \mathbb{E}[XY] - \mu_X \mu_Y$$
Si noti che se almeno una delle due variabili ha media nulla ($\mu_X=0$ o $\mu_Y=0$), allora $\operatorname{COV}[X, Y] = \mathbb{E}[XY]$.

#### b) Incorrelazione vs Indipendenza
Due variabili con *covarianza nulla* sono dette **incorrelate**. È fondamentale ricordare che:
*   **Indipendenza $\Rightarrow$ Incorrelazione**: Se $X$ e $Y$ sono indipendenti, la loro pmf congiunta è il prodotto delle marginali $p_{X,Y}(x,y) = p_X(x)p_Y(y)$.
*   **Incorrelazione $\nRightarrow$ Indipendenza**: Due variabili possono essere incorrelate ma comunque dipendenti (ad esempio in relazioni non lineari).

>[!dim] Dimostrazione per variabili indipendenti:
$$\operatorname{COV}[X, Y] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (x - \mu_X)(y - \mu_Y) p_X(x)p_Y(y)$$
$$= \left( \sum_{x \in \mathcal{X}} (x - \mu_X) p_X(x) \right) \left( \sum_{y \in \mathcal{Y}} (y - \mu_Y) p_Y(y) \right) = \mathbb{E}[X - \mu_X] \cdot \mathbb{E}[Y - \mu_Y] = 0 \cdot 0 = 0$$

#### c) Coefficiente di Correlazione (Coefficiente di Pearson)
Si può dimostrare che $|\operatorname{COV}[X, Y]| \leq \sigma_X \sigma_Y$. Utilizzando la proprietà della non-negatività del valore atteso:
>[!dim]
$$0 \leq \mathbb{E} \left[ \left( \frac{X - \mu_X}{\sigma_X} \pm \frac{Y - \mu_Y}{\sigma_Y} \right)^2 \right] = \underbrace{\mathbb{E} \left[ \left(\frac{X - \mu_X}{\sigma_X}\right)^2 \right]}_{1} + \underbrace{\mathbb{E} \left[ \left(\frac{Y - \mu_Y}{\sigma_Y}\right)^2 \right]}_{1} \pm 2 \mathbb{E} \left[ \frac{(X - \mu_X)(Y - \mu_Y)}{\sigma_X \sigma_Y} \right]$$
$$= 2 \pm 2 \frac{\operatorname{COV}[X, Y]}{\sigma_X \sigma_Y}$$
Da cui deriva che $-1 \leq \frac{\operatorname{COV}[X, Y]}{\sigma_X \sigma_Y} \leq 1$. La quantità $\rho_{X,Y}$ è definita come **coefficiente di correlazione**:
$$\rho_{X,Y} = \frac{\operatorname{COV}[X, Y]}{\sigma_X \sigma_Y} \in [-1, 1]$$

#### b) Varianza di una combinazione lineare
Definendo $Z = aX + bY$, dove $\mu_Z = a\mu_X + b\mu_Y$, la varianza di $Z$ è:
$$\sigma_Z^2 = \mathbb{E}[Z^2] - \mu_Z^2 = \mathbb{E}[(aX + bY)^2] - (a\mu_X + b\mu_Y)^2$$
Sviluppando i termini e applicando la linearità:
$$\sigma_Z^2 = a^2 \sigma_X^2 + b^2 \sigma_Y^2 + 2ab \operatorname{COV}[X, Y]$$


# Continuo
## Introduzione alle Variabili Continue

Quando passiamo a un campo di definizione $\Omega \subseteq \mathbb{R}$, l'approccio frequentista basato su singoli punti perde significato. Poiché la probabilità che una variabile continua $X$ assuma un valore esatto è nulla ($\mathbb{P}(X=x)=0$), l'analisi deve spostarsi dai singoli punti agli **intervalli**.

## Frequenza e Probabilità negli Intervalli
### Frequenza

Sia $x \in \mathcal{X}$ il punto di interesse e $\Delta x$ l'ampiezza dell'intorno. Su $n$ esperimenti, definiamo la **frequenza relativa** nell'intervallo $[x - \frac{\Delta x}{2}$, x + $\frac{\Delta x}{2}]$ come:
$$f_n(x; \Delta x) = \frac{n_{\left\{x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2}\right\}}}{n}$$
Al limite per $n \to \infty$, questa frequenza definisce la **probabilità dell'intervallo**:
$$\mathbb{P}\left(X \in \left[x - \frac{\Delta x}{2}, x + \frac{\Delta x}{2}\right]\right) = P_X(x; \Delta x) = \lim_{n \to \infty} f_n(x; \Delta x)$$

### PDF

> [!def] Definizione: Densità di probabilità
> La **densità di probabilità** (probability density function, pdf) della variabile aleatoria continua $X$ è la funzione: 
>
> $$
> f _ {X} (x) = \lim _ {\Delta x \rightarrow 0} \frac {\mathbb {P} \left(x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2}\right)}{\Delta x} = \lim _ {\Delta x \rightarrow 0} \frac {P _ {X} (x ; \Delta x)}{\Delta x}
> $$
>
> Intuitivamente, la densità rappresenta la "concentrazione" di probabilità in un punto specifico. Poiché la probabilità di una singola istantanea per una variabile continua è nulla, la pdf indica quanto è probabile che la variabile cada in un intervallo infinitesimo attorno a quel punto.

Grazie al *Teorema Fondamentale del Calcolo Integrale*, la probabilità che la variabile $X$ cada in un generico intervallo $[a, b]$ si ottiene integrando la densità:

$$
\mathbb {P} \left(x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2}\right) = \int_ {x - \frac {\Delta x}{2}} ^ {x + \frac {\Delta x}{2}} f _ {X} (t) d t
$$

#### Vincoli fondamentali

Affinché una funzione sia una valida pdf, deve soddisfare due proprietà:

1. **Non-negatività:** $f_X(x) \geq 0 \quad \forall x \in \mathbb{R}$
2. **Normalizzazione:** L'area sottesa dalla curva sull'intero dominio deve essere unitaria:
$$\int_{-\infty}^{+\infty} f_X(t) \, dt = 1$$

## Nota di raccordo 

>[!rb] **(Discreto vs Continuo):**
> Sia nel caso discreto che in quello continuo, la probabilità di un evento $A$ si ottiene "sommando" i contributi di densità:
> * **Nel discreto:** Sommiamo le probabilità puntuali: $\mathbb{P}(A) = \sum_{x \in A} p_X(x)$
> * **Nel continuo:** Integriamo la densità: $\mathbb{P}(A) = \int_{A} f_X(x) \, dx$
> 
> 
> In entrambi i casi, la densità è ciò che ci permette di passare dalla teoria alla capacità di calcolare effettivamente la probabilità di un evento.


## La Cumulative Distribution Function (CDF)

Oltre alla densità di probabilità (PDF), si usa spesso la **Funzione di Ripartizione (CDF)**, che indica la probabilità che la variabile $X$ sia inferiore o uguale a un certo valore $x$:
$$ F_X(x) = \mathbb{P}(-\infty < X \le x) = \int_{-\infty}^{x} f_X(t) \, dt \implies f_X(x) = \frac{dF_X(x)}{dx} $$
Esiste anche la **CCDF (Complementare)**, che indica la probabilità che $X$ sia maggiore di $x$:
$$ \overline{F}_X(x) = \mathbb{P}(X > x) = \int_{x}^{\infty} f_X(t) \, dt = 1 - F_X(x) \implies f_X(x) = -\frac{d\overline{F}_X(x)}{dx} $$

### Proprietà
- $F _ { X } ( x ) \in [ 0 , 1 ]$, in quanto rappresenta una probabilità;
- $F _ { X } ( - \infty ) = 0 \textsf { e } F _ { X } ( + \infty ) = 1$ (in quanto funzione integrale di una pdf);
- $F _ { X } ( x )$ è continua (in quanto funzione integrale di una funzione sommabile);
- $F _ { X } ( x )$ è crescente, in quanto l’integrando $f _ { X } ( \cdot ) \ \dot { \mathrm { e } }$ è non negativo;

**Concetto chiave**:
$F(x)$ è la "probabilità accumulata" fino al punto $x$.

* **Calcolo degli intervalli:** Per trovare la probabilità che $X$ sia compreso tra $a_1$ e $a_2$, non serve necessariamente calcolare l'integrale della PDF; basta la differenza tra i valori della CDF:
$$\mathbb {P} \left(a _ {1} \leq X \leq a _ {2}\right) = \int_ {a _ {1}} ^ {a _ {2}} f _ {X} (t) d t = F _ {X} \left(a _ {2}\right) - F _ {X} \left(a _ {1}\right)$$


> [!quote] Osservazione
>  La CDF è definita anche per variabili discrete, ma in ambito operativo è uno strumento utilizzato quasi esclusivamente con variabili continue.*

## Media statistica di variabili continue

Data una variabile aleatoria continua con pdf $f _ { X } ( x )$, definiamo la sua **media statistica** come:

$$
\mathbb {E} [ X ] = \mu_ {X} = \int_ {\mathbb {R}} x f _ {X} (x) d x
$$

Per giustificare questa definizione, si possono utilizzare diversi argomenti:

>[!dim] Dimostrazione 1: Dal discreto al continuo tramite il limite di una sommatoria
>Per giustificare l'integrale, si quantizza $X$ in intervalli $\Delta$. Se $x_i$ è il valore rappresentativo dell'intervallo $[i\Delta, (i+1)\Delta)$, allora:
>$$
X ^ {\Delta} = x _ {i} \in [ i \Delta , (i + 1) \Delta
>$$
>Se $\quad i \Delta \leq X <   (i + 1) \Delta$
>$$
 \mathbb {P} (X = x _ {i}) = \int_ {i \Delta} ^ {(i + 1) \Delta} f _ {X} (x) d x
>$$
>
>Ovviamente avremo:
>
>$$
\mathbb {E} \left[ X ^ {\Delta} \right] = \sum_ {i = - \infty} ^ {\infty} x _ {i} \underbrace {\int_ {i \Delta} ^ {(i + 1) \Delta} f _ {X} (x) d x} _ {p _ {X \Delta} (x _ {i})}
>$$
>
>Passando al limite per $\Delta \to 0$, la sommatoria converge all'integrale di Riemann:
>
>$$
\mathbb {E} [ X ] = \lim _ {\Delta \rightarrow 0} \mathbb {E} [ X ^ {\Delta} ] = \lim _ {\Delta \rightarrow 0} \sum_ {i = - \infty} ^ {\infty} x _ {i} f _ {X} (x _ {i}) \Delta = \int_ {\mathbb {R}} x f _ {X} (x) d x
>$$

>[!dim] Dimostrazione 2: Visione Unificata (Integrale di Lebesgue)
In termini generali, si definisce la media tramite l'integrale di Lebesgue rispetto alla misura di probabilità $P$:
$$\mathbb{E}[X] = \int_{\Omega} X(\omega) \, dP(\omega)$$
> * Nel caso **discreto**, l'integrale si riduce alla sommatoria $\sum x p(x)$.
> * Nel caso **continuo**, dato che $dP(\omega) = f_X(x)dx$, l'integrale diventa la classica formula dell'integrale di Riemann. Questa notazione è unificata e indipendente dalla natura della variabile.

## Tipi di Variabili
### Variabili Uniformi

Una **variabile aleatoria** $X$ si dice **uniformemente distribuita** su un intervallo $[a, b]$, $b \geq a \left( X \sim \mathcal { U } \left( a , b \right) \right)$ se: 

$$
f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{b - a} & x \in [ a, b ] \\ 0 & \text { altrove } \end{array} \right.
$$

> Siccome $\text{supp}(X) = [a, b]$ $[ f _ { X } ( x ) ] = [ a , b ]$, tale è il suo alfabeto (cioè $X$ non assume valori esterni all’intervallo). 

La sua **CDF** si scrive quindi: 

$$
F _ {X} (x) = \int_ {- \infty} ^ {x} f _ {X} (t)   d t = \left\{ \begin{array}{l l} 0 & x <   a \\ \frac {x - a}{b - a} & a \leq x \leq b \\ 1 & x \geq b \end{array} \right.
$$

mentre la sua media statistica vale: 

$$
\mathbb {E} [ X ] = \int_ {a} ^ {b} \frac {x}{b - a} d x = \frac {b ^ {2} - a ^ {2}}{2 (b - a)} = \frac {a + b}{2}
$$

L’andamento di pdf e CDF sono mostrati nella successiva slide.

#### pdf e CDF di variabili uniformi

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c3f6dc9e2a801980935c1605a6b11fb0b0f1678de5a63bed040d1bda1182b2e0.jpg)
Figura 1: pdf della variabile uniforme

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/e00a692547928dec972c2b70ba912cb5b50498747f1c6f2e70e64a8250e0a9f7.jpg)
Figura 2: CDF della variabile uniforme

### Variabili esponenziali

Una variabile aleatoria $X$ si dice **esponenziale** con parametro $\lambda > 0$ $\lambda \left( X \sim { \mathcal { E } } ( \lambda ) \right)$ se ha una pdf: 

$$
f _ {X} (x) = \lambda e ^ {- \lambda x} u (x), \quad u (x) \text {   gradino   unitario   continuo   }
$$

per cui $\text{supp}(X) = [0, +\infty)$ $[ f _ { X } ( x ) ] = [ 0 , \infty [ ,$, il che implica $X \geq 0$. La sua CDF vale dunque: 

$$
F _ {X} (x) = \int_ {0} ^ {x} \lambda e ^ {- \lambda t} d t = \left(1 - e ^ {- \lambda x}\right) u (x)
$$

La sua media vale infine: 

$$
\mathbb {E} [ X ] = \lambda \int_ {0} ^ {\infty} x e ^ {- \lambda x} d x = \frac {1}{\lambda}
$$

I relativi andamenti sono mostrati nella prossima slide.

#### pdf e CDF di variabili esponenziali

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/08ab3fd5b2e073a6d017a7f7cdf795cbed576c47f81a07d9415e45dde49d254f.jpg)
Figura 3: pdf della variabile esponenziale

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/d6303810f7e1eab90d297d7ecd1e8a382e49fb1d59f93cbc76fb80a71f91ff09.jpg)
Figura 4: CDF di $X \sim \varepsilon(\lambda)$

### Variabili laplaciane

Una variabile aleatoria $X$ si dice **laplaciana** con parametro $\lambda > 0$ $\lambda \left( X \sim { \mathcal { L } } ( \lambda ) \right)$ se ha una pdf: 

$$
f _ {X} (x) = \frac {\lambda}{2} e ^ {- \lambda | x |}
$$

per cui $\text{supp}(X) = \mathbb{R}$ $[ f _ { X } ( x ) ] = \mathbb { R }$, il che implica $X$ può assumere qualunque valore reale. La sua CDF vale dunque: 

$$
F _ {X} (x) = \int_ {- \infty} ^ {x} \frac {\lambda}{2} e ^ {- \lambda | t |}   d t = \left\{ \begin{array}{l l} \frac {\lambda}{2} \int_ {- \infty} e ^ {\lambda t}   d t = \frac {1}{2} e ^ {\lambda x} & x \leq 0 \\ \frac {\lambda}{2} \left[ \int_ {- \infty} ^ {0} e ^ {\lambda t}   d t + \int_ {0} ^ {x} e ^ {- \lambda t}   d t \right] = 1 - \frac {1}{2} e ^ {- \lambda x} & x \geq 0 \end{array} \right.
$$

La sua media è nulla, come sempre accade per le pdf pari. Infatti: 

$$
E[X] = \int_{-\infty}^{+\infty} x f(x) dx = 0 \tag{1}
$$
$$
\mathbb {E} [ X ] = \frac {\lambda}{2} \int_ {- \infty} ^ {\infty} x e ^ {- \lambda | x |} d x = 0
$$

I relativi andamenti sono mostrati nella prossima slide.

#### pdf e CDF di variabili laplaciane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/39f51fa4ff2eb7cb56cb12410ab682f44fdac428a7255317918a58910ce0f602.jpg)
Figura 5: pdf della variabile laplaciana

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/68af4a0c86ad1fc90ac3bdd3f5e7d395f93a4b0223313d87385837c55eea2f86.jpg)
Figura 6: CDF di $X \sim L(\lambda)$

### Variabili di Cauchy

Una variabile aleatoria $X$ si dice di **Cauchy** con parametri $x_0$ e $\gamma > 0$ $( a , b ) \ ( \boldsymbol { X } \sim \mathcal { C } ( a , b ) )$ se ha una pdf: 

$$
f _ {X} (x) = \frac {1}{b \pi} \frac {1}{1 + \left(\frac {x - a}{b}\right) ^ {2}}
$$

per cui $\text{supp}(X) = \mathbb{R}$ $[ f _ { X } ( x ) ] = \mathbb { R }$, il che implica $X$ può assumere qualunque valore reale. La sua CDF vale dunque: 

$$
F _ {X} (x) = \frac {1}{b \pi} \int_ {- \infty} ^ {x} \frac {d t}{1 + \left(\frac {t - a}{b}\right) ^ {2}} d t = \frac {1}{2} + \frac {1}{\pi} \arctan \left(\frac {x - a}{b}\right)
$$

La sua media non è definita, perché $\int_{-\infty}^{+\infty} |x| f(x) dx$ $x f _ { X } ( x )$ non è integrabile. Tuttavia è definibile un punto di simmetria mediante il seguente integrale a valore principale: 

$$
\frac {1}{b \pi} \lim _ {H \to \infty} \int_ {- H} ^ {H} \frac {x}{1 + \left(\frac {x - a}{b}\right) ^ {2}} d x = a
$$

I relativi andamenti sono mostrati nella prossima slide.

#### pdf e CDF di variabili di Cauchy

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/37f192a92d3c0821ce4b3c544298a2f503630eea2717b9e0dc1ae55d1dbeea9d.jpg)
Figura 7: pdf della variabile di Cauchy

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/da62d320d49b4d115fdd49c23baaf8c0b8c15ce9c200a43a8856f458817797aa.jpg)
Figura 8: CDF di $X \sim C(a, b)$

## PDF Condizionata: $f_{X|A}(x)$

Il concetto di probabilità condizionata si estende al caso continuo in modo intuitivo.

### 1. Definizione tramite Limite (Approccio locale)

Analogamente al caso discreto, la **PDF** condizionata esprime la densità di probabilità di $X$ sapendo che si è verificato l'evento $A$:
$$f_{X|A}(x) = \lim_{\Delta x \to 0} \frac{\mathbb{P}(x - \frac{\Delta x}{2} < X \leq x + \frac{\Delta x}{2} \mid A)}{\Delta x}$$
### 2. Definizione tramite CDF (Approccio operativo)

È spesso più semplice passare attraverso la Funzione di Ripartizione condizionata:
$$F_{X|A}(x) = \mathbb{P}(X \leq x \mid A) = \frac{\mathbb{P}(\{X \leq x\} \cap A)}{\mathbb{P}(A)}$$
Da cui si ricava la densità(pdf) derivando rispetto a $x$:
$$f_{X|A}(x) = \frac{d}{dx} F_{X|A}(x)$$

## Legge della probabilità totale per PDF, CDF e Medie

>[!rb] R.B.
>In modo del tutto analogo al caso discreto.
*Data una partizione dello spazio campionario $\Omega$ costituita dagli eventi $\{E_m\}_{m=1}^M$ (con $\mathbb{P}($E_m$) > 0$), valgono le seguenti relazioni:*

 **1. Densità e Ripartizione:**
$$f_X(x) = \sum_{m=1}^{M} f_{X|E_m}(x) \mathbb{P}(E_m) \quad \longleftrightarrow \quad F_X(x) = \sum_{m=1}^{M} F_{X|E_m}(x) \mathbb{P}(E_m)$$
 
 **2. Valore Atteso (Legge dell'Aspettativa Totale):**
$$\mathbb{E}[X] = \sum_{m=1}^{M} \mathbb{E}[X|E_m] \mathbb{P}(E_m)$$
 
 
 *Dove la media condizionata è calcolata come:*
$$\mathbb{E}[X|E_m] = \int_{-\infty}^{+\infty} x f_{X|E_m}(x) dx$$
 
 
## Funzioni di variabili aleatorie continue

Data una variabile aleatoria continua $X$ con densità di probabilità $f_X(x)$ e funzione di ripartizione $F_X(x)$, consideriamo la trasformazione:

$$
Y = g (X) = g [ X (\omega) ] \in \mathcal {Y} \quad \text {   dove   } \mathcal {Y} = g (\mathcal {X})
$$

A differenza di quanto analizzato nel caso discreto, si distinguono tre casi principali :
1. $g(x)$ è **biunivoca** $\implies$ invertibile, continua e derivabile;
2. $g(x)$ è **continua, derivabile e univoca $\implies$** **non** invertibile con $Y$ **continuo**;
3. $g(x)$ è **univoca** $\implies$ **non** invertibile con $Y$ **discreto**
	>Quest’ultimo caso corrisponde a una **conversione** $\mathsf { A } / \mathsf { D }$ della variabile continua (ovvero una sua quantizzazione o compressione con perdite) in analogia a quanto visto nella conversione $\mathsf { A } / \mathsf { D }$ di segnali e sequenze deterministiche.

### Funzioni invertibili

Si ricorda che se $g(x)$ è invertibile, allora essa è **strettamente monotona** $\forall \space x \in { \mathcal { X } }$. 

>[!def] PDF formula unica
>In entrambi i casi, la **pdf** (Probability Density Function) $f_Y(y)$ si scrive in forma unificata:
>$$
f _ {Y} (y) = \frac {f _ {X} [ g ^ {- 1} (y) ]}{| g ^ {\prime} [ g ^ {- 1} (y) ] |}
>$$
>>[!quote] Nota:
>>Il valore assoluto al denominatore ci assicura la non negatività della PDF e quindi stabilire se un funzione è crescente o decrescente.
#### Funzione strettamente crescente
Se $g(x)$ è strettamente crescente $( g ^ { \prime } ( x ) > 0 )$:

$$
F _ {Y} (y) = \mathbb {P} (Y \leq y) = \mathbb {P} (g (X) \leq y) = \mathbb {P} (X \leq g ^ {- 1} (y)) = F _ {X} [ g ^ {- 1} (y) ]
$$

$$
f _ {Y} (y) = \frac {d F _ {Y} (y)}{d y} \longleftrightarrow f _ {X} [ g ^ {- 1} (y) ] \frac {d g ^ {- 1} (y)}{d y} = \frac {f _ {X} [ g ^ {- 1} (y) ]}{g ^ {\prime} [ g ^ {- 1} (y) ]}
$$

#### Funzione strettamente decrescente
Se $g(x)$ è strettamente decrescente $( g ^ { \prime } ( x ) < 0 )$:

$$
F _ {Y} (y) = \mathbb {P} (Y \leq y) = \mathbb {P} (g (X) \leq y) = \mathbb {P} (X \geq g ^ {- 1} (y)) = 1 - F _ {X} [ g ^ {- 1} (y) ]
$$

$$
f _ {Y} (y) = - \frac {d F _ {Y} (y)}{d y} \longleftrightarrow f _ {X} [ g ^ {- 1} (y) ] \frac {d g ^ {- 1} (y)}{d y} = \frac {f _ {X} [ g ^ {- 1} (y) ]}{- g ^ {\prime} [ g ^ {- 1} (y) ]}
$$




### Funzioni non invertibili

Se $g(x)$ non è invertibile, un valore $y$ può essere generato da più valori $x$. Sia $\{x_i(y)\}$ l'insieme dei punti tali che $g[x_i(y)] = y$.

> [!def] PDF per funzioni non invertibili
> Se la funzione è derivabile e $g'(x) \neq 0$ quasi ovunque, la pdf risultante è la somma dei contributi locali:
> $$f_Y(y) = \sum_{i} \frac{f_X[x_i(y)]}{|g'[x_i(y)]|}$$
> 
> 
#### Procedura operativa

Non applicare la formula diretta. Per calcolare la densità di probabilità $f_Y(y)$:

1. **Parti dalla CDF**:
$$F_Y(y) = \mathbb{P}(Y \le y) = \mathbb{P}(g(X) \le y)$$
2. **Esplicita l'evento**: Risolvi la disequazione $g(X) \le y$ per trovare gli intervalli di $X$ corrispondenti.
3. **Calcola la probabilità**: Somma le probabilità degli intervalli trovati usando $F_X(x)$ o integrando $f_X(x)$.
4. **Deriva**: Ottieni $f_Y(y) = \frac{d F_Y(y)}{d y}$.
#### Rappresentazione grafica
$$
f _ {Y} (y _ {1}) = \sum_ {i = 1} ^ {3} f _ {X} \left[ x _ {i} (y _ {1}) \right] \left| \frac {d x _ {i} (y)}{d y} \right| _ {y = y _ {1}} = \sum_ {i = 1} ^ {3} \frac {f _ {X} \left[ x _ {i} (y _ {1}) \right]}{\left| g ^ {\prime} [ x _ {i} (y _ {1}) ] \right|}
$$

$$
f _ {Y} (y _ {2}) = \sum_ {i = 1} ^ {2} f _ {X} \left[ x _ {i} (y _ {2}) \right] \left| \frac {d x _ {i} (y)}{d y} \right| _ {y = y _ {2}} = \sum_ {i = 1} ^ {2} \frac {f _ {X} \left[ x _ {i} (y _ {2}) \right]}{\left| g ^ {\prime} [ x _ {i} (y _ {2}) ] \right|}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/75daf37cde2197ea8b008ceadbbf1a23f380a8edcd7d8eeba4bc90f54e811575.jpg)
Figura 1: Rappresentazione della funzione non invertibile $g(x) = boh$.
 
## Conversione A/D di variabili aleatorie

Si ha una conversione Analogico/Digitale quando una variabile continua $X$ viene mappata in una variabile discreta $Y$.
**Procedimento:**
1. **Parametri:** Si sceglie una rappresentazione a $R$ bit, ottenendo $M = 2^R$ livelli di uscita.
2. **Partizione:** Il dominio di $X$ viene diviso in $M$ intervalli tramite i punti $\{x_i\}_{i=1}^{M+1}$.
3. **Mappatura:** La variabile discreta $Y$ assume il valore $y_i$ se $X$ cade nell'intervallo corrispondente:
$$Y = y_i \quad \text{se} \quad x_i \leq X < x_{i+1} \quad (i = 1, \dots, M)$$

**Calcolo della PMF di $Y$:**
La probabilità che $Y$ assuma il valore $y_i$ è pari alla probabilità che $X$ cada nell'intervallo $[$x_i$, x_{i+1})$:
$$p_Y(y_i) = F_X(x_{i+1}) - F_X(x_i)$$
*Nota: La scelta dei livelli $y_i$ e della partizione $\{x_i\}$ è a discrezione del progettista.*
Ecco una sintesi operativa, pulita dal rumore accademico e pronta per essere inserita in Obsidian.

## Media di funzioni di variabili aleatorie

Per una variabile aleatoria continua $X$ con pdf $f_X(x)$, il valore atteso di una sua funzione $Y = g(X)$ si calcola come:
$$\mathbb{E}[g(X)] = \int_{-\mathbb{R}} g(x) f_X(x) dx$$
*(Il risultato deriva dal limite per $\Delta \to 0$ della versione quantizzata della variabile).*

## Valore quadratico medio e Varianza

Generalizzazione dei concetti per variabili continue, data la media $\mu_X = \mathbb{E}[X]$:

### 1. Valore Quadratico Medio (Mean Square)
$$X_{\text{rms}}^2 = \mathbb{E}[X^2] = \int_{-\mathbb{R}} x^2 f_X(x) dx$$
### 2. Valore Efficace (RMS - Root Mean Square)
$$X_{\text{rms}} = \sqrt{\mathbb{E}[X^2]} = \sqrt{\int_{-\mathbb{R}} x^2 f_X(x) dx}$$
### 3. Varianza ($\sigma_X^2$)

Misura la dispersione attorno alla media. Si calcola preferibilmente con la formula:
$$\sigma_X^2 = \mathbb{E}[(X - \mu_X)^2] = X_{\text{rms}}^2 - \mu_X^2$$
### 4. Deviazione Standard ($\sigma_X$)
$$\sigma_X = \sqrt{\sigma_X^2} = \sqrt{X_{\text{rms}}^2 - \mu_X^2}$$
> [!info] Nota
> Tutte le proprietà di linearità e invarianza valide per le variabili discrete si applicano analogamente anche al caso continuo.
## Variabili continue multiple 

Il concetto di variabile singola si estende naturalmente a più variabili (vettori aleatori) mappando l'evento $\omega \in \Omega$ in uno spazio multidimensionale $\mathbb{R}^m$.

>[!def]
Dato un insieme di $m$ variabili aleatorie $X_1, \dots, X_m$, il vettore aleatorio è definito come:
>$$(X_1, \dots, X_m) : \omega \in \Omega \longrightarrow (X_1(\omega), \dots, X_m(\omega)) \in \mathcal{X}_1 \times \dots \times \mathcal{X}_m \subseteq \mathbb{R}^m$$
#### Casi particolari

* **Variabile doppia (coppia):**
$$(X, Y) : \omega \in \Omega \longrightarrow (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y} \subseteq \mathbb{R}^2$$

* **Variabile tripla (terna):**
$$(X, Y, Z) : \omega \in \Omega \longrightarrow (X(\omega), Y(\omega), Z(\omega)) \in \mathcal{X} \times \mathcal{Y} \times \mathcal{Z} \subseteq \mathbb{R}^3$$


> [!info] Nota
> La definizione non dipende dalla natura delle variabili (continue o discrete); la struttura rimane valida per qualsiasi combinazione di variabili aleatorie.
### pdf congiunta di due variabili aleatorie

Si consideri una coppia di variabili continue, $X \in \mathcal { X } \mathrm { ~ e ~ } Y \in \mathcal { Y }$, la loro **pdf congiunta** $f_{X,Y}(x,y)$ si definisce in perfetta analogia con la pdf di variabili continue singole (vedi slide 94): 

$$
\begin{array}{l} f _ {X, Y} (x, y) = \lim _ {\Delta x \to 0} \lim _ {\Delta y \to 0} \frac {\mathbb {P} \left(\left\{x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \right\} \cap \left\{y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2} \right\}\right)}{\Delta x \Delta_ {y}} \\ = \lim _ {\Delta x \to 0} \lim _ {\Delta y \to 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{\Delta x \Delta y} \quad (x, y) \in \mathcal {X} \times \mathcal {Y} \end{array}
$$

Per il teorema fondamentale del calcolo integrale abbiamo quindi che, se $C \subseteq \mathcal { X } \times \mathcal { y }$ 

$$
\mathbb {P} ((X, Y) \in C) = \int_ {C} f _ {X, Y} (x, y) d x d y
$$

Le densità di probabilità congiunte devono soddisfare dei vincoli costitutivi - simili a quelli delle densità marginali: 

$$
a f _ {X, Y} (x, y) \geq 0 \forall \space (x, y) \in \mathbb {R} ^ {2};
$$

$b$ $f _ { X , Y } ( x , y )$ è sommabile su $\mathbb { R } ^ { 2 }$ e a integrale unitario. Infatti: 

$$
\int_ {\mathbb {R} ^ {2}} f _ {X, Y} (x, y) d x d y = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} f _ {X, Y} (x, y) d x d y = \mathbb {P} ((X, Y) \in \mathbb {R} ^ {2}) = 1
$$

#### Proprietà della pdf congiunta

La **pdf congiunta** $f _ { X , Y } ( x , y )$ condivide con la pmf congiunta $p x , \gamma ( x , y ) \textrm { - e }$, per alcune, con tutte le densità, le seguenti proprietà: 

##### Proprietà di marginalizzazione

$$
\int_ {\mathbb {R}} f _ {X, Y} (x, y) d y = f _ {X} (x) \qquad \int_ {\mathbb {R}} f _ {X, Y} (x, y) d x = f _ {Y} (y)
$$

Per cui caratterizzare congiuntamente $( X , Y )$ significa anche caratterizzarle marginalmente, mentre il viceversa non è necessariamente vero. 

##### Indipendenza statistica

Due variabili aleatorie sono **indipendenti** se e solo se 

$$
f _ {X, Y} (x, y) = f _ {X} (x) f _ {Y} (y) \Longleftrightarrow F _ {X, Y} (x, y) = \mathbb {P} (X \leq x, Y \leq y) = F _ {X} (x) F _ {Y} (y)
$$

Più in generale, se $X _ { i } \sim f _ { X _ { i } } ( x ) , x \in \mathcal { X } _ { i }$, allora esse sono indipendenti se e solo se: 

$$
f _ {X _ {1}, \dots , X _ {m}} (x _ {1}, \dots , x _ {m}) = \prod_ {i = 1} ^ {m} f _ {X _ {i}} (x _ {i}), \qquad (x _ {1}, \dots , x _ {m}) \in \mathbb {R} ^ {m}
$$

### Le pdf condizionate

Si considerino variabili aleatorie $X \in \mathcal { X } \mathrm { ~ e ~ } Y \in \mathcal { Y }$ con assegnata pdf congiunta $f _ { X , Y } ( x , y )$. 

La **pdf condizionata** di $X$ dato $Y$ si può definire a partire dalla seguente quantità (vedi slide 110): 

$$
\mathbb {P} \left(x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \mid y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2}\right) = \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{P _ {Y} (y ; \Delta y)}
$$

Pertanto la densità di $X$ condizionata all’evento $\begin{array} { r } { \left\{ y - \frac { \Delta y } { 2 } \leq Y \leq y + \frac { \Delta y } { 2 } \right\} } \end{array}$ è: 

$$
\lim _ {\Delta x \rightarrow 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{\Delta x P _ {Y} (y ; \Delta y)} = f _ {X | \{y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2} \}} (x | y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2})
$$

Facendo dunque tendere $\Delta y$ a zero, otteniamo: 

$$
f _ {X \mid Y} (x \mid y) = \lim _ {\Delta x \rightarrow 0} \lim _ {\Delta y \rightarrow 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{P _ {Y} (y ; \Delta y)} = \frac {f _ {X , Y} (x , y)}{f _ {Y} (y)}
$$

che, come c’era da attendersi, riproduce l’analoga definizione per la pmf condizionale che, d’altronde, è essa stessa una densità. 

Di conseguenza tutte le proprietà delle pmf condizionali si estendono alle pdf condizionali. 

#### Proprietà delle pdf condizionate

Data l’analogia con le variabili discrete, ci limitiamo qui a riscrivere le proprietà della slide 74. 

$f _ { X \mid Y } ( x | y )$ se $y$ resta fisso e $x$ varia in $X$ è una densità di probabilità, cioè: 

$$
f _ {X | Y} (x | y) \geq 0 \int_ {\mathbb {R}} f _ {X | Y} (x | y) d x = 1
$$

##### Legge della probabilità totale per le pdf

$$
f _ {X} (x) = \int_ {\mathbb {R}} f _ {X, Y} (x, y) d y = \int_ {\mathbb {R}} f _ {X | Y} (x | y) f _ {Y} (y) d y
$$

$$
f _ {Y} (y) = \int_ {\mathbb {R}} f _ {X, Y} (x, y) d x = \int_ {\mathbb {R}} f _ {Y | X} (y | x) f _ {X} (x) d x
$$

##### Leggi della probabilità composta e di Bayes per le densità

$$
f _ {X, Y} (x, y) = f _ {Y} (y) f _ {X | Y} (x | y) = f _ {X} (x) f _ {Y | X} (y | x) \Rightarrow f _ {Y | X} (y | x) = \frac {f _ {Y} (y) f _ {X | Y} (x | y)}{f _ {X} (x)}
$$

Come nel caso discreto, avremo: 

Se $Z = \boldsymbol { \mathrm { g } } ( \boldsymbol { X } , \boldsymbol { Y } )$ allora 

$$
\mathbb {E} [ Z ] = \int_ {\mathbb {R} ^ {2}} g (x, y) f _ {X}, \gamma (x, y) d x d y
$$

##### Linearità della media

$$
\mathbb {E} \left[ \sum_ {i = 1} ^ {m} a _ {i} X _ {i} \right] = \sum_ {i = 1} ^ {m} a _ {i} \mathbb {E} \left[ X _ {i} \right]
$$

##### Teorema della media condizionata

> [!theorem] Teorema (*Media Condizionata*)
> Enunciato: 
> $$
> \mathbb {E} \left[ g (X, Y) \right] = \mathbb {E} \left[ \mathbb {E} \left[ g (X, Y) | Y \right] \right]
> $$
>
> dove: 
> $$
> \mathbb {E} \left[ g (X, Y) | Y = y \right] = \int_ {\mathbb {R}} g (x, y) f _ {X | Y} (x | y) d x = \mathbb {E} \left[ h (Y (\omega)) \right] \Longleftrightarrow
> $$
>
> $$
> h \left[ Y (\omega) \right] = \int_ {\mathbb {R}} g (x, Y) f _ {X | Y} (x | Y) d x
> $$

### Covarianza tra due variabili continue

Siano $( X , Y ) \sim f _ { X , Y } ( x , y )$. Denotiamo con $( \mu _ { X } , \mu _ { Y } )$ le rispettive medie e $( \sigma _ { X } ^ { 2 } , \sigma _ { Y } ^ { 2 } )$ le rispettive varianze. Avremo, in analogia al caso discreto: 

#### Covarianza tra X e Y

$$
\operatorname{COV} [ X, Y ] = \mathbb {E} \left[ (X - \mu_ {X}) (Y - \mu_ {Y}) \right] = \mathbb {E} [ X Y ] - \mu_ {X} \mu_ {Y}
$$

#### Coefficiente di correlazione tra X e Y

$$
\rho_ {X, Y} = \frac {\operatorname{COV} [ X , Y ]}{\sigma_ {X} \sigma_ {Y}}, \quad \left| \rho_ {X, Y} \right| \leq 1
$$

#### Incorrelazione tra X e Y

> [!quote] Osservazione
> Indipendenza implica incorrelazione, ma incorrelazione non implica indipendenza. 

## Variabili Gaussiane: Caratterizzazione marginale

Una variabile aleatoria $X _ { 0 } \in \mathcal { X } = \mathbb { R }$ si dice **Gaussiana** (o Normale) standard - $X _ { 0 } \sim \mathcal { N } ( 0 , 1 )$ se: 

$$
f _ {X _ {0}} (x _ {0}) = \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {x _ {0} ^ {2}}{2}}, \quad x \in \mathbb {R} \quad \Longrightarrow \quad \mathbb {E} [ X _ {0} ] = 0 \quad \sigma_ {X _ {0}} ^ {2} = \mathbb {E} [ X _ {0} ^ {2} ] = 1
$$

>[!dim] dimostrazione della densità della variabile aleatoria Normale (o Gaussiana) generica.
>Partendo da $X_0 \sim \mathcal{N}(0, 1)$ con $f_{X_0}($x_0) = \frac{1}{$\sqrt{2 \pi}$} e^{-$\frac{x_0^2}{2}$}$ e applicando la trasformazione lineare $X = \sigma_X $X_0$ + \mu_X$:
>1. **Inversa e Derivata:**
$$x_0 = g^{-1}(x) = \frac{x - \mu_X}{\sigma_X} \implies \left| \frac{d}{dx} g^{-1}(x) \right| = \frac{1}{\sigma_X}$$
>2. **Cambio di Variabile ($f_X(x) = f_{X_0}(g^{-1}(x)) \cdot | \frac{d}{dx} g^{-1}(x) |$):**
$$f_X(x) = \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} \left(\frac{x - \mu_X}{\sigma_X}\right)^2} \cdot \frac{1}{\sigma_X} = \frac{1}{\sqrt{2 \pi \sigma_ {X} ^ {2}}} e ^ {- \frac {(x - \mu_ {X}) ^ {2}}{2 \sigma_ {X} ^ {2}}} \implies X \sim \mathcal{N}(\mu_X, \sigma_X^2)$$
>3. **Momenti Corretti:**
$$\mathbb{E}[X] = \sigma_X \mathbb{E}[X_0] + \mu_X = \mu_X \quad \text{(refuso slide: } \neq 0\text{)}$$
$$\operatorname{VAR}[X] = \operatorname{VAR}[\sigma_X X_0 + \mu_X] = \sigma_X^2 \operatorname{VAR}[X_0] = \sigma_X^2$$

### Andamenti di pdf Gaussiane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/14bd5c980e8521e5eb02a7517ff1fac46626c196028264217617a09b4afc4823.jpg)
Figura 1: Andamenti di pdf Gaussiane.

### La funzione Q(x)

Sia $X_0 \sim \mathcal{N}(0, 1)$ una variabile casuale normale standard. Poiché l'integrale della funzione $e^{-\frac{t^2}{2}}$ non ammette primitive elementari, la sua funzione di ripartizione (CDF) e la sua funzione complementare (CCDF) non possono essere espresse in forma chiusa.

Per questo motivo, si definisce la **funzione $Q(x)$**:
$$Q(x) \stackrel{\text{def}}{=} \mathbb{P}(X_0 \geq x) = 1 - F_{X_0}(x) = \frac{1}{\sqrt{2\pi}} \int_x^\infty e^{-\frac{t^2}{2}} dt$$

Da questa definizione si ottengono facilmente le seguenti relazioni:
*   **Funzione di ripartizione:** $F_{X_0}(x) = 1 - Q(x)$
*   **Probabilità in un intervallo:** $\mathbb{P}_{X_0}(x; \Delta x) = Q\left(x - \frac{\Delta x}{2}\right) - Q\left(x + \frac{\Delta x}{2}\right)$

Per una variabile casuale generale $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$, che può essere espressa come $X = X_0 \sigma_X + \mu_X$, la probabilità complementare è data da:
$$1 - F_X(x) = Q\left(\frac{x - \mu_X}{\sigma_X}\right)$$

Il comportamento della funzione $Q(x)$ per $x \geq 0$ è illustrato nel diagramma nella slide successiva.

#### Andamento di Q(x)

$$
Q (x) \sim \frac {1}{x \sqrt {2 \pi}} e ^ {- \frac {x ^ {2}}{2}} <   e ^ {- \frac {x ^ {2}}{2}}, \qquad x \to \infty
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9e014a72e6bb4cff5f6045f5e3af68f8479b85e9889bcb10a79b45de356eb16a.jpg)
Figura 2: Andamento di Q(x).

### Alcune utili proprietà della funzione Q(x)

Si considerino preliminarmente i valori limite della funzione:
$$Q(-\infty) = \frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} e^{-\frac{t^2}{2}} dt = 1 \qquad \text{e} \qquad Q(+\infty) = 0$$

Inoltre, derivando la funzione $Q(x)$, si ottiene:
$$\frac{dQ(x)}{dx} = -\frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} < 0 \quad \forall x \in \mathbb{R}$$
Questo conferma che $Q(x)$ è una funzione strettamente decrescente.

#### Simmetria
La funzione $Q(x)$ soddisfa la seguente proprietà di simmetria:
$$Q(-x) = \frac{1}{\sqrt{2\pi}} \int_{-x}^\infty e^{-\frac{t^2}{2}} dt = 1 - Q(x)$$

#### Generalizzazione
Per una variabile casuale $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$, la probabilità che $X$ superi un valore $\eta$ può essere espressa in termini della funzione $Q$ come segue:
$$\mathbb{P}(X \geq \eta) = \mathbb{P}\left(X_0 \sigma_X + \mu_X \geq \eta\right) = \mathbb{P}\left(X_0 \geq \frac{\eta - \mu_X}{\sigma_X}\right) = Q\left(\frac{\eta - \mu_X}{\sigma_X}\right)$$

### Caratterizzazione congiunta di variabili Gaussiane

Siano $X _ { 1 } \sim \mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) \in X _ { 2 } \sim \mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$. Noi sappiamo che: 

$$
\sigma_ {1} ^ {2} = \mathbb {E} \left[ (X _ {1} - \mu_ {1}) ^ {2} \right] \quad \sigma_ {2} ^ {2} = \mathbb {E} \left[ (X _ {2} - \mu_ {2}) ^ {2} \right] \quad \rho_ {1, 2} = \overbrace {\frac {\mathbb {E} \left[ (X _ {1} - \mu_ {1}) (X _ {2} - \mu_ {2}) \right]}{\sigma_ {1} \sigma_ {2}}} ^ {\mathrm{COV} (X _ {1}, X _ {2})}
$$

rappresenta una caratterizzazione ”globale” (cioè incompleta) della coppia $( X _ { 1 } , X _ { 2 } )$. Organizziamo tale coppia in un vettore colonna $\pmb { X } = ( X _ { 1 } \pmb { X } _ { 2 } ) ^ { T }$. Ovviamente, $\pmb { x } \in \mathbb { R } ^ { 2 \times 1 }$ è un **vettore bidimensionale aleatorio**, la cui media è essa stessa un vettore, $\mu _ { X } = ( \mu _ { 1 } \mu _ { 2 } ) ^ { T }$.

Definiamo **Matrice di covarianza** del vettore $X$ la matrice $\kappa _ { X } \in \mathbb R ^ { 2 \times 2 }$:

$$
\boldsymbol {K} _ {\boldsymbol {X}} \stackrel {{\text { def }}} {{=}} \mathbb {E} \left[ (\boldsymbol {X} - \boldsymbol {\mu} _ {\boldsymbol {X}}) (\boldsymbol {X} - \boldsymbol {\mu} _ {\boldsymbol {X}}) ^ {T} \right] = \mathbb {E} \left[ \binom{X _ {1} - \mu_ {1}}{X _ {2} - \mu_ {2}} (X _ {1} - \mu_ {1} X _ {2} - \mu_ {2}) \right] =
$$

$$
\Sigma = E[(X - \mu)(X - \mu)^T] \tag{1}
$$

$$
= \mathbb {E} \left[ \begin{array}{c c} (X _ {1} - \mu_ {1}) ^ {2} & (X _ {1} - \mu_ {1}) (X _ {2} - \mu_ {2}) \\ (X _ {2} - \mu_ {2}) (X _ {1} - \mu_ {1}) & (X _ {2} - \mu_ {2}) ^ {2} \end{array} \right] = \left( \begin{array}{c c} \sigma_ {1} ^ {2} & \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ \sigma_ {1} \sigma_ {2} \rho_ {1, 2} & \sigma_ {2} ^ {2} \end{array} \right)
$$

#### Alcune proprietà della matrice di covarianza

Poiché $| \boldsymbol { K } \boldsymbol { x } | = \sigma _ { 1 } ^ { 2 } \sigma _ { 2 } ^ { 2 } \bigl ( 1 - \rho _ { 1 , 2 } ^ { 2 } \bigr ) \geq 0 , \boldsymbol { K } \boldsymbol { x }$ è definita non negativa; 

Se $\rho _ { 1 , 2 } \neq \pm 1 \kappa _ { x }$ è invertibile e ha inversa definita positiva: 

$$
\boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} = \frac {1}{\sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})} \left( \begin{array}{c c} \sigma_ {2} ^ {2} & - \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ - \sigma_ {1} \sigma_ {2} \rho_ {1, 2} & \sigma_ {1} ^ {2} \end{array} \right)
$$

$\kappa _ { x }$ è simmetrica; 

Ovviamente, se $\pmb { z } = [ z _ { 1 } z _ { 2 } ] ^ { T } \in \mathbb { R } ^ { 2 \times 1 }$ 

$$
\boldsymbol {z} ^ {T} \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} \boldsymbol {z} \geq 0 \quad \forall \space \boldsymbol {z} \in \mathbb {R} ^ {2 \times 1}
$$

Se $X _ { 1 } \texttt { e } X _ { 2 }$ sono incorrelate allora $\rho _ { 1 , 2 } = 0$, per cui $\kappa _ { x }$ diventa la matrice diagonale: 

$$
\boldsymbol {K} _ {\boldsymbol {X}} = \left( \begin{array}{c c} \sigma_ {1} ^ {2} & 0 \\ 0 & \sigma_ {2} ^ {2} \end{array} \right) \Longrightarrow \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} = \left( \begin{array}{c c} \frac {1}{\sigma_ {1} ^ {2}} & 0 \\ 0 & \frac {1}{\sigma_ {2} ^ {2}} \end{array} \right)
$$

#### Variabili congiuntamente Gaussiane

Le due variabili $X _ { 1 } \sim \mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) \in X _ { 2 } \sim \mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$ si dicono **congiuntamente Gaussiane** se la loro pdf congiunta - cioè la pdf del vettore $\pmb { X } = ( X _ { 1 } X _ { 2 } ) ^ { T }$ - si scrive: 

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \frac {1}{2 \pi | \boldsymbol {K} _ {\boldsymbol {X}} | ^ {1 / 2}} \exp \left[ - \frac {1}{2} (\boldsymbol {x} - \boldsymbol {\mu} _ {\boldsymbol {X}}) ^ {T} \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} (\boldsymbol {x} - \boldsymbol {\mu} _ {\boldsymbol {X}}) \right] = f _ {X _ {1}, X _ {2}} (x _ {1}, x _ {2}) =
$$

$$
f(x_1, x_2) = \frac{1}{2\pi \sqrt{|\Sigma|}} \exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)\right) \tag{2}
$$

$$
\frac {1}{2 \pi \sqrt {\sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})}} \exp \left[ - \frac {\sigma_ {2} ^ {2} (x _ {1} - \mu_ {1}) ^ {2} + \sigma_ {1} ^ {2} (x _ {2} - \mu_ {2}) ^ {2} - 2 \rho_ {1 , 2} (x _ {1} - \mu_ {1}) (x _ {2} - \mu_ {2})}{2 \sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})} \right]
$$

In questo caso si può usare la notazione abbreviata $\pmb { X } \sim \mathcal { N } ( \pmb { \mu } \pmb { x } , \pmb { K } \pmb { x } )$:

> [!example] Notazione abbreviata
> $X \sim \mathcal{N}(\mu, \Sigma)$

Nel caso speciale $\rho _ { 1 , 2 } = 0$, la precedente dà: 

$$
f _ {\pmb {X}} (\pmb {x}) = f _ {X _ {1}, X _ {2}} (x _ {1}, x _ {2}) = \frac {1}{2 \pi \sqrt {\sigma_ {1} ^ {2} \sigma_ {2} ^ {2}}} e ^ {- \frac {(x _ {1} - \mu_ {1}) ^ {2}}{2 \sigma_ {1} ^ {2}} - \frac {(x _ {2} - \mu_ {2}) ^ {2}}{2 \sigma_ {2} ^ {2}}} = f _ {X _ {1}} (x _ {1}) f _ {X _ {2}} (x _ {2})
$$

cioè se due variabili sono congiuntamente Gaussiane (e solo in questo caso) l’incorrelazione implica l’indipendenza statistica! 

## Proprietà di chiusura rispetto a trasformazioni lineari

Se $\pmb { x } \sim \mathcal { N } ( \pmb { \mu } \pmb { x } , \pmb { K } \pmb { x } )$ allora ogni trasformazione lineare di $X$ dà luogo a un nuovo vettore Gaussiano. 

Focalizziamoci prima su una semplice combinazione lineare di $X _ { 1 } \texttt { e } X _ { 2 }$. Avremo che: 

$$
\begin{array}{c} Z = a _ {1} X _ {1} + a _ {2} X _ {2} \Rightarrow \mu_ {Z} = a _ {1} \mu_ {1} + a _ {2} \mu_ {2} \quad \sigma_ {Z} ^ {2} = a _ {1} ^ {2} \sigma_ {1} ^ {2} + a _ {2} ^ {2} \sigma_ {2} ^ {2} + 2 a _ {1} a _ {2} \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ \boxed {Z \sim \mathcal {N} (\mu_ {Z}, \sigma_ {Z} ^ {2})} \end{array}
$$

Più in generale, se $\pmb { Z } = \pmb { A } \pmb { X } + \pmb { b }$, con $\pmb { A } \in \mathbb { R } ^ { 2 \times 2 } \mathrm { ~ e ~ } \pmb { b } \in \mathbb { R } ^ { 2 \times 1 }$ allora: 

$$
\mu_ {Z} = A \mu_ {X} + b
$$

$$
\mu_{Y} = A \mu_{X} \tag{3}
$$

$$
\mathbb {E} \left[ (Z - \mu_ {Z}) (Z - \mu_ {Z}) ^ {T} \right] = A K _ {X} A ^ {T} = K _ {Z}
$$

$$
\Sigma_{Y} = A \Sigma_{X} A^T \tag{4}
$$

$$
\mathbf {Z} \sim \mathcal {N} (\boldsymbol {\mu_ {Z}}, \mathbf {K _ {Z}})
$$

# Vettori Aleatorei
### Ripasso
>[!rb] Definizione di Spazio di Probabilità
>
>
>* $\Omega$ è lo spazio dei campioni.
>* $\mathcal{T}$ è la $\sigma$-algebra degli eventi di $\Omega$.
>* $\mathbb{P} : \mathcal{T} \to [0, 1]$ è la legge di probabilità.

>[!rb] Variabili Aleatorie (VA)
>
>Una variabile aleatoria reale $X$ è una funzione misurabile definita come:
>
>$$X : \omega \in \Omega \longrightarrow X(\omega) \in \mathcal{X} \subseteq \mathbb{R}$$
>
>La VA è classificata come **discreta** o **continua** in base al dominio $\mathcal{X}$ dell'immagine.

>[!rb] Vettori Aleatori (Coppie)
>
>Una coppia di variabili aleatorie $(X, Y)$ è un'applicazione:
>
>$$(X, Y) : \omega \in \Omega \longrightarrow (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y} \subseteq \mathbb{R}^2$$
## Caratterizzazione completa
>[!def] Caratterizzazione completa
>
>Una VA si dice **completamente caratterizzata** quando sono note le funzioni di distribuzione:
>
>##### Caso Singolo (VA $X$)
>
>* **CDF** (Cumulative Distribution Function):
>$$F_X(x) = \mathbb{P}\{X \leq x\} \quad \forall x \in \mathbb{R}$$
>
>* **PMF** (Probability Mass Function - Discreto):
>$$p_X(x) = \mathbb{P}\{X = x\} \quad \forall x \in \mathcal{X}$$
>* PDF (Probability Density Function - Continuo):
>$$f_X(x) = \frac{dF_X(x)}{dx}$$
>
>##### Caso Congiunto (Coppia $(X, Y)$)
>* **CDF Congiunta**:
$$F_{X,Y}(x, y) = \mathbb{P}\{X \leq x, Y \leq y\} \quad \forall (x, y) \in \mathbb{R}^2$$
>
>* **PMF Congiunta** (Discreto):
$$p_{X,Y}(x, y) = \mathbb{P}\{X = x, Y = y\} \quad \forall (x, y) \in \mathcal{X} \times \mathcal{Y}$$
>
>* **PDF Congiunta** (Continuo):
$$f_{X,Y}(x, y) = \frac{\partial^2 F_{X,Y}(x, y)}{\partial x \partial y}$$

### Vettori aleatori

>[!def] Vettore aleatoreo
> Una **n-pla aleatoria** è una ovvia generalizzazione del concetto di coppia di variabili aleatorie, cioè: 
>
>$$
\left(X _ {1}, \dots , X _ {n}\right): \omega \in \Omega \Longrightarrow \boldsymbol {X} (\omega) = \left(X _ {1} (\omega), \dots , X _ {n} (\omega)\right) \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {n} \subseteq \mathbb {R} ^ {n}
>$$
>
> Un vettore aleatorio si ottiene quindi facilmente come 
>
>$$
\boldsymbol {X} (\omega) = \left[ X _ {1} (\omega), \dots , X _ {n} (\omega) \right] ^ {T} \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {n} \subseteq \mathbb {R} ^ {n}
>$$
#### Caso Discreto
 Se gli alfabeti $\mathcal { X } _ { 1 } , \ldots \mathcal { X } _ { n }$ sono discreti, il vettore è discreto e si caratterizza mediante la DF congiunta; 
$$
p _ {\mathcal {X}} (\boldsymbol {x}) = p _ {\mathcal {X}} \left(x _ {1}, \dots , x _ {n}\right) = \mathbb {P} \left\{X _ {1} = x _ {1}, \dots , X _ {n} = x _ {n} \right\} \forall \space \boldsymbol {x} \in \mathcal {X} _ {1} \times \dots \mathcal {X} _ {n}
$$
dove $\pmb { x } = [ x _ { 1 } , \dots , x _ { n } ] ^ { T } \in \mathcal { X } _ { 1 } \times \dots \mathcal { X } _ { n }$ 

#### Caso Continuo 
Per alfabeti continui, avremo 
$$
F _ {\boldsymbol {X}} (\boldsymbol {x}) = \mathbb {P} \left\{X _ {1} \leq x _ {1}, \dots , X _ {n} \leq x _ {n} \right\} \forall \space \boldsymbol {x} \in \mathbb {R} ^ {n} \quad f _ {\boldsymbol {X}} (\boldsymbol {x}) = \frac {\partial^ {n} F _ {\boldsymbol {X}} (\boldsymbol {x})}{\partial x _ {1} \dots \partial x _ {n}}
$$
dove $\pmb { x } = [ x _ { 1 } , \dots , x _ { n } ] ^ { T } \in \mathbb { R } ^ { n }$ 

## Legge di Bayes per vettori aleatori

- Consideriamo un vettore aleatorio discreto con pmf $p _ { X } ( { \pmb x } )$. Sappiamo che la **Legge di Bayes** assicura che 

$$
\mathbb {P} (A \cap B) = \mathbb {P} (A | B) \mathbb {P} (B)
$$

- Posto $A = \{ X _ { n } = x _ { n } , \ldots , X _ { 2 } = x _ { 2 } \} \textsf { e } B = \{ X _ { 1 } = x _ { 1 } \}$ avremo 

$$
p _ {\boldsymbol {X}} (\boldsymbol {x}) = \mathbb {P} \left\{X _ {n} = x _ {n}, \dots , X _ {2} = x _ {2} | X _ {1} = x _ {1} \right\} \mathbb {P} \left\{X _ {1} = x _ {1} \right\}
$$

- Iterando il ragionamento avremo la regola della catena: 

$$
\begin{array}{c} p _ {X} (x) = \mathbb {P} \{X _ {1} = x _ {1} \} \mathbb {P} \left\{X _ {2} = x _ {2} | X _ {1} = x _ {1} \right\} \dots \mathbb {P} \left\{X _ {n} = x _ {n} | X _ {n - 1} = x _ {n - 1}, \ldots , X _ {1} = x _ {1} \right\} \\ = \prod_ {i = 1} ^ {n} p _ {X _ {i} | X _ {i - 1}, \ldots , X _ {1}} (x _ {i} | x _ {i - 1}, \ldots , x _ {1}), \qquad p _ {X _ {1} | X _ {0}} (x _ {1} | x _ {0}) = p _ {X _ {1}} (x _ {1}) \end{array}
$$

>[!def] Vettori Continui
>$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \prod_ {i = 1} ^ {n} f _ {X _ {i} | X _ {i - 1}, \dots , X _ {1}} (x _ {i} | x _ {i - 1}, \dots , x _ {1})
>$$

# Processi aleatori tempo-discreti ( Previsioni )

Si definisce **processo aleatorio tempo-discreto** un’applicazione che ad ogni elemento dello spazio campione fa corrispondere una successione:

$$
X: \omega \in \Omega \longrightarrow \{X (n, \omega) \} _ {n \in \mathbb {Z}}
$$

dove $\mathbb{Z}$ indica l’insieme degli interi.

> [!example] Esempio (Realizzazioni di un processo tempo-discreto)
> Di seguito sono riportate tre realizzazioni di un processo tempo-discreto.
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/7e76ee276ef5ef4aa0a28d11f4fc129e3b4bfc5e7363b6e3ebb01def91168f7a.jpg)
> Figura 1: Realizzazione 1
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/eef731154ce7b72b160d3d277cbe6b34a0a3867f94f145234edd9dd15d98f5db.jpg)
> Figura 2: Realizzazione 2
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/057411ab0f31edbb00e115bfa3816d1d5e5f1c3faed5ab464cbf318ca0bb423a.jpg)
> Figura 3: Realizzazione 3

*   **Realizzazione**: Per ogni $\omega \in \Omega$, il processo si manifesta come una sequenza deterministica (es. nell'intervallo $[-1, 1]$).
*   **Campionamento Verticale**: Fissando il tempo $n = n_0$ e variando lo stato $\omega$, $X($n_0$, \omega)$ diventa una **variabile aleatoria**.
*   **PDF**: La variabile aleatoria campionata possiede una propria funzione di densità di probabilità.
*   **Stazionarietà del 1° ordine**: Si ha quando la PDF risulta indipendente dall'istante di campionamento $n_0$ scelto.

> [!quote] Osservazione
> Si noti che siccome
> 
> $$
> \mathbb {E} [ X (n) ] = \int_ {- \infty} ^ {\infty} x f _ {X (n)} (x; n) d x = \int_ {- 0, 5} ^ {0, 5} x \Pi (x - 0. 5) d x = 0
> $$
> 
> il processo è a media identicamente nulla.

## Caratterizzazione del secondo ordine del processo

>[!def] **caratterizzato al primo ordine** 
>Se ne è nota la pdf : $f _ { X ( n ) } ( x ; n )$ per ogni $n$. 
>Se il processo è stazionario al primo ordine, questo equivale ad assegnare un’unica pdf.

>[!def] **caratterizzato al secondo ordine** 
>Se ne è assegnata la pdf congiunta:
>
>$$
f _ {X (n _ {1}), X (n _ {2})} \big (x _ {1}, x _ {2}; n _ {1}, n _ {2} \big), \quad \forall \space n _ {1}, n _ {2}
>$$

>[!def] **stazionario al secondo ordine** 
>Se, per qualsiasi intero $h$, abbiamo:
>
>$$
f _ {X (n _ {1}), X (n _ {2})} (x _ {1}, x _ {2}; n _ {1}, n _ {2}) = f _ {X (n _ {1} + h), X (n _ {2} + h)} (x _ {1}, x _ {2}; n _ {1}, n _ {2} + h)
>$$

- In altre parole, un processo stazionario al secondo ordine è tale che la caratterizzazione congiunta di due suoi campioni dipende unicamente dalla loro ”distanza” temporale, ma non dalla loro posizione: in altre parole, la pdf congiunta è invariante ad atti di moto rigido dei due punti in anticipo o in ritardo.
  
>[!important] 
>Ovviamente un processo stazionario al secondo ordine lo è anche al primo, ma non è vero il viceversa. 
>>[!dim] Plus - non fatta a lezione:
>>*   **Gerarchia della stazionarietà:** Un processo stazionario di ordine $M$ lo è automaticamente per qualunque ordine inferiore $i \le M$.
>>*   **Perché il 2° ordine implica il 1°:** La stazionarietà di secondo ordine garantisce che la PDF congiunta di due campioni sia invariante per traslazione temporale. Poiché la PDF di primo ordine (marginale) può essere derivata dalla congiunta tramite marginalizzazione, anche essa risulterà necessariamente invariante.
>>*   **Perché il 1° ordine NON implica il 2°:** La stazionarietà di primo ordine impone solo che la PDF del singolo campione $X(n)$ resti costante nel tempo.
>>*   **Mancanza di vincoli relazionali:** Tale condizione non fornisce alcuna informazione sulla PDF congiunta tra due campioni $X($n_1$)$ e $X($n_2$)$. 
>>*   **Il limite del 1° ordine:** Di conseguenza, è possibile che le distribuzioni dei singoli punti siano identiche per ogni istante, ma che la loro relazione statistica (come interagiscono tra loro) cambi in base alla posizione assoluta nel tempo.

## Caratterizzazione completa di un processo

Un processo aleatorio $X ( n )$ si dice **completamente caratterizzato** se, detto $M$ un intero arbitrario e detti $n _ { 1 } , \ldots , n _ { M }$ $M$ istanti arbitrari, il vettore aleatorio:

$$
\boldsymbol {X} = [ X (n _ {1}), \dots , X (n _ {M}) ] ^ {T}
$$

ha densità di probabilità $f _ { \pmb { X } } ( x _ { 1 } , \ldots , x _ { M } )$ nota.

>[!rb] PDF nota:
>Una densità di probabilità si definisce nota quando la variabile aleatoria (o il processo) è **completamente caratterizzata** dal punto di vista probabilistico.
>
>Ecco gli schemi essenziali:
>
>*   **Variabile Aleatoria Singola**: è nota quando disponi della sua **PDF** ($f_X(x)$ per il continuo), della **PMF** ($p_X(x)$ per il discreto) o della **CDF** ($F_X(x)$).
>*   **Processo Aleatorio (1° ordine)**: la densità è nota se conosci la PDF $f_{X(n)}(x; n)$ per ogni istante temporale $n$.
>*   **Caratterizzazione Completa**: si ha quando è nota la densità di probabilità congiunta di un vettore di campioni preso a istanti arbitrari.
>*   **Stazionarietà**: se il processo è stazionario al primo ordine, conoscere la densità significa assegnare un'unica PDF valida per qualunque istante di tempo.

Un processo aleatorio si dice **stazionario in senso stretto di ordine $M$** se la sua densità di probabilità di ordine $M$ è invariante per traslazione, cioè:

$$
\begin{array}{c} f _ {X (n _ {1}), \ldots , X (n _ {M})} (x _ {1}, \ldots , x _ {M}; n _ {1}, \ldots , n _ {M}) = \\ f _ {X (n _ {1} + h), \ldots , X (n _ {M} + h)} (x _ {1}, \ldots , x _ {M}; n _ {1} + h, \ldots , n _ {M} + h) \end{array}
$$

- Un processo stazionario di ordine $M$ lo è di qualunque ordine $i \leq M$;
- Un processo si dice **indipendente** (o a campioni indipendenti) se, comunque si scelga un intero $M$, il vettore $\pmb { X } = [ X ( n _ { 1 } ) , \dots , X ( n _ { M } ) ] ^ { T }$ è costituito da variabili aleatorie indipendenti, cioè:

$$
f _ {X (n _ {1}), \dots , X (n _ {M})} (x _ {1}, \dots , x _ {M}) = f _ {X (n _ {1})} (x _ {1}) f _ {X (n _ {2})} (x _ {2}) \dots f _ {X (n _ {M})} (x _ {M}) = \prod_ {i = 1} ^ {M} f _ {X (n _ {i})} (x _ {i})
$$

## Processi discreti

Si definisce **processo ampiezza discreto** (o **processo discreto**) un processo aleatorio le cui realizzazioni sono sequenze di valori appartenenti a un alfabeto discreto

>[!example] Processo di Bernulli
>Un caso di importanza notevole è quello di un **processo indipendente binario**, $X ( n ) \in \{ - 1 , 1 \}$, con $\mathbb { P } \left\{ X ( n ) = 1 \right\} = \mathbb { P } \left\{ X ( n ) = 1 \right\} = { \frac { 1 } { 2 } }$, di cui le realizzazioni sono riportate in figura.
![image|441x363](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/62faba250dc710ba5cb9fbd4a331bfdc4d2dc4cd5d3bd696b38454e5f14bc19a.jpg)
>	Figura 7: Realizzazioni del processo di Bernoulli

### Caratterizzazione di processi discreti

Tutte le definizioni introdotte per i processi continui si estendono ai **processi discreti**, con la sola differenza che le densità di probabilità (PDF) sono ora sostituite dalle **funzioni di massa di probabilità** (PMF or DF). 
### Caratterizzazione sintetica dei vettori aleatori

In assenza di una caratterizzazione completa, il comportamento statistico di un vettore aleatorio $\pmb{X} = [$X_1$, \dots, X_n]^T$ si descrive tramite parametri sintetici.

#### 1. Vettore Media Statistica
Rappresenta la collezione dei valori attesi di ciascuna componente:
$$\boldsymbol{\mu}_{\boldsymbol{X}} = \left(\mathbb{E}[X_1], \dots, \mathbb{E}[X_n]\right)^T$$
#### 2. Matrice di Covarianza
Indica la dispersione e la dipendenza lineare tra le componenti del vettore. È definita come $C_X = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu}_{\boldsymbol{X}})(\boldsymbol{X} - \boldsymbol{\mu}_{\boldsymbol{X}})^T]$:
$$
C_X = \begin{pmatrix} 
\sigma_{X_1}^2 & \operatorname{COV}(X_1, X_2) & \dots & \operatorname{COV}(X_1, X_n) \\ 
\operatorname{COV}(X_2, X_1) & \sigma_{X_2}^2 & \dots & \operatorname{COV}(X_2, X_n) \\ 
\vdots & \vdots & \ddots & \vdots \\ 
\operatorname{COV}(X_n, X_1) & \operatorname{COV}(X_n, X_2) & \dots & \sigma_{X_n}^2 
\end{pmatrix}
$$
*   **Proprietà rilevanti**: La matrice è sempre **simmetrica** e **definita non-negativa**.
## Processi Stazionari in Senso Lato (SSL)

> Focalizziamoci sui processi tempo discreti, ma quanto verrà detto vale anche per i processi tempo-continui. 

>[!def] Definizione: Processo SSL
>Un processo (continuo o discreto) si definisce **stazionario in senso lato** se soddisfa due vincoli statistici meno restrittivi della SSS:
> 1.  **Media costante:** $\mathbb{E}[X(t/n)] = \mu$ (indipendente da $t$ o $n$).
> 2.  **Autocorrelazione invariante per traslazione:** La funzione di autocorrelazione dipende solo dalla differenza temporale $\tau$:
>$$R_X(t_1, t_2) = \mathbb{E}[X(t_1)X(t_2)] = R_X(t_2 - t_1)$$
### Matrice di covarianza per processi SSL

Sia $X ( t / n )$ un processo SSL, continuo o discreto, e sia $\pmb { x } = [ X _ { 1 } , \ldots , X _ { M } ] ^ { T }$ un vettore aleatorio $M$-dimensionale di campioni di $X ( t / n )$, presi negli istanti $( t _ { 1 } , \dots , t _ { M } ) / ( n _ { 1 } , \dots , n _ { M } )$.

#### Vettore Media
In un processo SSL la media $\mu$ è costante. Il vettore media $\pmb{\mu}_{\pmb{X}}$ si esprime come:
$$\pmb{\mu}_{\pmb{X}} = \mu \mathbf{1}$$
*   **$\mathbf{1}$**: Vettore unitario (tutte le componenti sono identiche a $\mu$).
  
#### Proprietà Statistiche dei Campioni
Dalla condizione SSL derivano:
*   **Correlazione**: $\mathbb{E}[X_i X_j] = f(|i - j|)$ (dipende solo dalla distanza temporale).
*   **Varianza costante**: $\operatorname{Var}($X_i$) = \sigma_X^2$.
*   **Coefficiente di correlazione**: $\rho_{i,j} = \frac{\operatorname{COV}(X_i, X_j)}{\sigma_X^2}$.

#### Struttura della Matrice di Covarianza
La matrice $C_X$ è legata ai coefficienti $\rho_{i,j}$ e assume questa forma:
$$
\boldsymbol {C} _ {\boldsymbol {X}} = \sigma_ {X} ^ {2} \begin{pmatrix} 1 & \rho_ {1, 2} & \dots & \rho_ {1, M} \\ \rho_ {1, 2} & 1 & \dots & \rho_ {2, M} \\ \vdots & \vdots & \ddots & \vdots \\ \rho_ {1, M} & \rho_ {2, M} & \dots & 1 \end{pmatrix}
$$

> [!quote] Osservazione
>*   **Simmetria**: $C_X$ è sempre simmetrica rispetto alla diagonale principale.
>*   **Matrice di Toeplitz**: Se il passo di campionamento è costante, gli elementi sulle diagonali parallele a quella principale sono uguali.
>*   **Definita non-negativa**: Il prodotto $x^T C_X x$ è sempre $\ge 0$.

## Estensione ai processi continui: definizioni

Le definizioni introdotte per i processi discreti si applicano identicamente ai processi ad ampiezza continua $X(t)$.

#### Caratterizzazione statistica
Per descrivere il processo è necessario assegnare due funzioni fondamentali:
*   **Media**: $\mu(t) = \mathbb{E}[X(t)]$
*   **Autocorrelazione**: $R(t_1, t_2) = \mathbb{E}[X(t_1)X(t_2)]$

### Proprietà dei processi Gaussiani

I processi Gaussiani sono fondamentali perché le loro caratteristiche statistiche sono interamente determinate dai parametri del primo e secondo ordine.

#### 1. Stazionarietà: SSL $\implies$ SSS
*   In un processo Gaussiano, la **stazionarietà in senso lato (SSL)** implica sempre la **stazionarietà in senso stretto (SSS)**.
*   Se il processo è SSL, la matrice di covarianza assume una struttura di **Toeplitz**.

#### 2. Chiusura rispetto a trasformazioni lineari
*   Ogni trasformazione lineare di un vettore Gaussiano produce un nuovo vettore Gaussiano.
*   Dato $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$, applicando la trasformazione $\mathbf{A}\mathbf{X} + \mathbf{b}$ si ottiene:
    $$\mathbf{A}\mathbf{X} + \mathbf{b} \sim \mathcal{N}(\mathbf{A}\boldsymbol{\mu} + \mathbf{b}, \mathbf{A}\Sigma\mathbf{A}^T)$$
#### 3. Incorrelazione e Indipendenza
*   **Proprietà esclusiva**: Per i processi Gaussiani, l'**incorrelazione implica l'indipendenza** statistica.
*   Se i campioni sono incorrelati, la matrice di covarianza è diagonale: $\Sigma = \text{diag}(\sigma_1^2, \dots, \sigma_M^2)$.
*   In questo caso, la PDF congiunta si fattorizza nel prodotto delle singole PDF marginali:
    $$f(\mathbf{x}) = \prod_{i=1}^M \frac{1}{\sqrt{2\pi\sigma_i^2}} \exp\left(-\frac{(x_i-\mu_i)^2}{2\sigma_i^2}\right)$$
# Tipi di convergenza

Sia $X_n$ una successione di variabili aleatorie con densità $f_n(x)$ che tende a un limite $X$.

### Gerarchia della convergenza
Le forme di convergenza variano per "forza" e gradazione:
*   **Puntuale (Più forte):** $P(\lim_{n \to \infty} X_n = X) = 1$. Le variabili aleatorie convergono come funzioni sullo spazio campionario $\Omega$.
*   **Quasi certa (o con probabilità 1):** Fondamentale per la *forte coerenza* degli stimatori.
*   **In media quadratica (Mean-Square):** $\lim_{n \to \infty} \mathbb{E} [(X_n - X)^2] = 0$.
*   **In probabilità:** Nota anche come *convergenza debole*.
*   **In distribuzione:** La forma più comune per l'analisi asintotica.
#### Convergenza in distribuzione ($X_n \xrightarrow{d} X$)

**Definizione:** La successione converge se il limite delle funzioni di ripartizione coincide con la funzione di ripartizione del limite nei suoi punti di continuità:
$$ \lim_{n \to \infty} F_n(x) = F(x) $$

> [!theorem] Teorema: Continuous Mapping
> Se $g$ è una funzione continua, la convergenza in distribuzione si conserva attraverso la trasformazione:
> $$ X_n \xrightarrow{d} X \implies g(X_n) \xrightarrow{d} g(X) $$

# La funzione generatrice dei momenti (MGF)

>[!def] **Definizione e Continuità**
>La MGF è definita dal valore atteso $\Phi_X(s) = \mathbb{E}[e^{sX}]$. È una funzione continua di $s$ in tutti i punti in cui l'integrale $\int_{\mathbb{R}} e^{st} f_X(t) dt$ esiste.

>[!important] **Proprietà Operative**
>*   **Calcolo rapido dei momenti:** Derivando la funzione e valutandola in $s=0$, si ottengono i momenti di ordine $r$ della variabile aleatoria.
> 	 *   $\Phi_X(0) = 1$.
> 	   *   $\Phi'_X(0) = \mathbb{E}[X]$ (Media).
> 	   *   $\Phi''_X(0) = \mathbb{E}[X^2]$ (utile per calcolare la Varianza).
> 	   *   $\Phi^{(r)}_X(0) = \mathbb{E}[X^r]$.
>   
>*   **Somma di variabili indipendenti:** La MGF della somma di variabili aleatorie indipendenti è pari al prodotto delle loro singole MGF.

>[!theorem] **Teoremi Fondamentali**
>*   **Sviluppo in serie (MacLaurin):** La funzione ammette uno sviluppo in serie $\Phi_X(s) = \sum_{n=0}^{\infty} \frac{\mathbb{E}[X^n]}{n!} s^n$. I coefficienti di questa serie sono legati biunivocamente ai momenti della variabile.
>*   **Continuità di Lévy:** La convergenza puntuale delle MGF di una successione ($M_{X_n}(s) \to M_X(s)$) è condizione necessaria e sufficiente per la convergenza in distribuzione della variabile ($X_n \xrightarrow{d} X$).

>[!rb] **Perché è utile?**
>Oltre a semplificare il calcolo dei momenti, la MGF caratterizza univocamente una distribuzione: se due variabili hanno la stessa MGF, possiedono la stessa funzione di ripartizione.


