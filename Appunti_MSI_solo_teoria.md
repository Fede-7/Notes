```table-of-contents
```
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

## Il significato della varianza e della deviazione standard

Supponiamo di non avere una caratterizzazione completa di una variabile aleatoria $X$.

Se $\mathcal { X } \subseteq [ 0 , + \infty [$ (cioè la variabile è non negativa), la media $\mu x$ fornisce un'indicazione del suo comportamento, sebbene imprecisa. Se invece $X$ può assumere sia valori positivi che negativi, la media non costituisce un indicatore significativo per descrivere il comportamento della variabile aleatoria.

In entrambi i casi, è fondamentale determinare la probabilità di osservare valori di $X$ significativamente distanti dalla propria media. Nel caso in cui sia nota la coppia $( \mu _ { X } , \sigma _ { X } )$, tale analisi può essere condotta mediante la **Disuguaglianza di Chebyshev**:

$$
\mathbb {P} \left\{| X - \mu_ {X} | > k \sigma_ {X} \right\} = \mathbb {P} \left\{\mu_ {X} - k \sigma_ {X} \leq X \leq \mu_ {X} + k \sigma_ {X} \right\} \geq 1 - \frac {1}{k ^ {2}}
$$

Si deduce che un parametro fondamentale è il rapporto $\frac { \mu _ { X } } { \sigma _ { X } }$:
- Valori elevati di questo rapporto indicano una **pmf** (funzione di probabilità) molto concentrata intorno alla media (variabile "poco aleatoria").
- Valori bassi implicano un'elevata aleatorietà.

## La disuguaglianza di Chebyshev

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

## Quadro sintetico delle proprietà di media e varianza

### Proprietà della Media ($\mathbb{E}$)
*   **Linearità:** Se $(a, b)$ sono costanti reali:
$$\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$$
*(Dato che $\mathbb{E}[b] = b$)*

*   **Non-negatività:** Se $X(\omega) \geq 0$ per ogni $\omega \in \Omega$ (ovvero se $\mathcal{X} \subseteq [0, +\infty[$), allora:
$$\mathbb{E}[X] \geq 0$$
### Proprietà della Varianza ($\sigma^2$)
*   **Non-negatività:** La varianza è sempre non negativa:
$$\sigma_X^2 \geq 0$$
*(In quanto media della variabile non negativa $(X - \mu_X)^2$)*

*   **Trasformazione Lineare:** Se $Y = aX + b$, allora la varianza è:
$$\sigma_Y^2 = a^2 \sigma_X^2$$

>[!dim] Dimostrazione:
$$\mu_Y = a\mu_X + b$$
$$\mathbb{E}[Y^2] = \mathbb{E}[a^2X^2 + 2abX + b^2] = a^2\mathbb{E}[X^2] + 2ab\mathbb{E}[X] + b^2$$
$$\sigma_Y^2 = a^2\mathbb{E}[X^2] + 2ab\mu_X + b^2 - (a\mu_X + b)^2 = a^2\sigma_X^2$$
### Relazioni Correlate
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

##### Marginalizzazione
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

## Variabili indipendenti

Due variabili aleatorie $X \in \mathcal{X}$ e $Y \in \mathcal{Y}$ sono **indipendenti** $\iff$ gli eventi $\{X = x\}$ e $\{Y = y\}$ sono indipendenti.

Per due variabili indipendenti, la pmf congiunta si fattorizza nel prodotto delle rispettive marginali:
$$p_{X,Y}(x,y) = \mathbb{P}(\{X = x\} \cap \{Y = y\}) = \mathbb{P}(\{X = x\}) \mathbb{P}(\{Y = y\}) = p_X(x) p_Y(y)$$
Questo è l'unico caso in cui la conoscenza delle sole pmf marginali $p_X(x)$ e $p_Y(y)$ è sufficiente per determinare univocamente la pmf congiunta.

### Generalizzazione a $m$ variabili aleatorie
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

#### 1. Trasformazione Biunivoca (Inversa Unica)

Se la funzione $g(x,y)$ mappa ogni singola coppia del dominio $(x,y)$ in un valore di $z$ unico e distinto (ovvero la funzione è iniettiva sullo spazio di supporto), esiste un'unica coppia invertibile $(x(z), y(z))$ tale per cui $z = g(x, y)$.

In questo caso, la probabilità che $Z$ assuma il valore $z$ coincide esattamente con la probabilità congiunta dell'unico punto di partenza che lo ha generato:
$$p_Z(z) = \mathbb{P}(Z = z) = p_{X, Y}(x(z), y(z))$$
#### 2. Trasformazione Non Biunivoca (Collassamento delle Probabilità)

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

#### Generalizzazione a $m$ variabili

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


# Dal discreto al continuo
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

## La DF come pdf

### Ritorno sugli spazi discreti
Se $A \subseteq \Omega \ { \dot { \mathsf { e } } }$ un insieme discreto, la misura "ordinaria" è ovviamente $\mu _ { 0 } ( A ) = c ( A ) = | A |$, anche detta **misura di conteggio**. 

Siano $\omega \in \Omega$ e $X ( \omega _ { * } ) = X _ { * }$: la misura ordinaria di $\{ \omega _ { * } \}$ sarebbe ovviamente $c ( \{ \omega _ { * } \} ) = 1$. Una misura alternativa è $\mu _ { 1 } ( \omega _ { * } ) = \mathbb { P } ( \omega _ { * } : X ( \omega _ { * } ) = x _ { * } ) = p _ { X } ( x _ { * } )$.

Pertanto, la densità di $\mu _ { 1 } ( \omega _ { * } )$ rispetto a $\mu _ { 0 } ( \omega _ { * } ) \dot { \in } p _ { X } ( x _ { * } )$ può essere scritta (simbolicamente):

$$
p _ {X} (x _ {*}) = \left. \frac {d \mu_ {1} (\omega)}{d c (\omega)} \right| _ {\omega = \omega^ {*}}
$$

Se $A \subseteq \Omega \ \in X ( A ) = { \mathcal { X } } _ { A } \subseteq { \mathcal { X } }$, avremo allora:

$$
\mu_ {1} (A) = \mathbb {P} (A) = \int_ {A} d \mu_ {1} (\omega) = \int_ {\mathcal {X} _ {A}} p _ {X} (x) d c (x) = \sum_ {x \in \mathcal {X} _ {A}} p _ {X} (x)
$$

dove l’integrale è un integrale di Lebesgue rispetto alla misura di conteggio. 

In generale, la **Densità di Probabilità (DF)** è una particolare **pdf** (*probability density function*): ciò lascia intuire che tutte le proprietà dimostrate per le DF si estendono alle pdf e, con opportuni cambiamenti, a tutte le densità di una misura rispetto a un’altra.

## La Cumulative Distribution Function (CDF)

Si noti preliminarmente che $f _ { X } ( x ) , x \in \mathbb { R } \ { \dot { \mathrm { ~ e ~ } } }$ è perfettamente adeguata a caratterizzare $X$. Infatti:

$$
\operatorname{supp} \left[ f _ {X} (x) \right] = \mathcal {X} \quad \mathbb {P} \left(a _ {1} \leq X \leq a _ {2}\right) = \int_ {a _ {1}} ^ {a _ {2}} f _ {X} (t) d t
$$

dove $\text{supp}[g(\cdot)]$ indica il supporto della funzione $g ( \cdot )$.

Tuttavia, è invalso l’uso di caratterizzazioni alternative, tra cui la **Cumulative Distribution Function (CDF)**:

$$ F(x) = P(X \le x) \tag{3} $$

Talvolta si fa riferimento alla **Complementary Cumulative Distribution Function (CCDF)**:

$$ S(x) = P(X > x) \tag{4} $$

## Proprietà della CDF

Le proprietà derivano direttamente dalla definizione. In particolare:

- $F _ { X } ( x ) \in [ 0 , 1 ]$, in quanto rappresenta una probabilità;
- $F _ { X } ( - \infty ) = 0 \textsf { e } F _ { X } ( + \infty ) = 1$ (in quanto funzione integrale di una pdf);
- $F _ { X } ( x )$ è continua (in quanto funzione integrale di una funzione sommabile);
- $F _ { X } ( x )$ è crescente, in quanto l’integrando $f _ { X } ( \cdot ) \ \dot { \mathrm { e } }$ è non negativo;

Ovviamente risulta:

$$
\mathbb {P} \left(a _ {1} \leq X \leq a _ {2}\right) = \int_ {a _ {1}} ^ {a _ {2}} f _ {X} (t) d t = F _ {X} \left(a _ {2}\right) - F _ {X} \left(a _ {1}\right)
$$

> [!quote] Osservazione
> La CDF potrebbe definirsi anche per variabili discrete, nel qual caso la proprietà di continuità andrebbe "rimodulata". Tuttavia, la CDF di variabili discrete non $\grave { \mathbf { e } }$ una grandezza utile.

## Media statistica di variabili continue

Data una variabile aleatoria continua con pdf $f _ { X } ( x )$, definiamo la sua **media statistica** come:

$$
\mathbb {E} [ X ] = \mu_ {X} = \int_ {\mathbb {R}} x f _ {X} (x) d x
$$

Per giustificare questa definizione, si possono utilizzare diversi argomenti. Si consideri inizialmente una versione "quantizzata" di $X$ nella forma:

$$
X ^ {\Delta} = x _ {i} \in [ i \Delta , (i + 1) \Delta [ \text {se} i \Delta \leq X <   (i + 1) \Delta \rightarrow \mathbb {P} (X = x _ {i}) = \int_ {i \Delta} ^ {(i + 1) \Delta} f _ {X} (x) d x
$$

Ovviamente avremo:

$$
\mathbb {E} \left[ X ^ {\Delta} \right] = \sum_ {i = - \infty} ^ {\infty} x _ {i} \underbrace {\int_ {i \Delta} ^ {(i + 1) \Delta} f _ {X} (x) d x} _ {p _ {X \Delta} (x _ {i})}
$$

Infine, se $x f _ { X } ( x ) \ { \overset { } { \in } }$ è integrabile secondo Riemann:

$$
\mathbb {E} [ X ] = \lim _ {\Delta \rightarrow 0} \mathbb {E} [ X ^ {\Delta} ] = \lim _ {\Delta \rightarrow 0} \sum_ {i = - \infty} ^ {\infty} x _ {i} f _ {X} (x _ {i}) \Delta = \int_ {\mathbb {R}} x f _ {X} (x) d x
$$

Un’altra giustificazione deriva dalle considerazioni intuitive sulla riducibilità di una DF a una pdf. Infatti, se $\Omega \ { \dot { \mathsf { e } } }$ uno spazio discreto, sappiamo che:

$$
\mathbb {E} \left[ X \right] = \sum_ {x \in \mathcal {X}} x p _ {X} (x) = \int_ {\mathcal {X}} x f _ {X} (x) d c (x) = \int_ {\Omega} X (\omega) d \mu_ {1} (\omega)
$$

dove $\mu _ { 1 } ( \cdot ) \textsf { e }$ la misura di probabilità introdotta su $\Omega$ con densità (rispetto alla misura di conteggio) $\begin{array} { r } { \frac { d \mu _ { 1 } ( \omega ) } { d c ( \omega ) } = p _ { X } [ x ( \omega ) ] } \end{array}$.

Quindi, è possibile definire la media statistica di una variabile aleatoria (indipendentemente dal fatto che sia discreta o continua) nella forma:

$$ E[X] = \int_{\Omega} x \, dP(x) \tag{5} $$

dove l’integrale è un integrale di Lebesgue. Per $\Omega = \mathbb { R }$ avremo ovviamente $d \mu _ { 1 } ( \omega ) = f _ { X } ( x )$ $dx$, per cui:

$$
\mathbb {E} [ X ] = \int_ {\mathbb {R}} x f _ {X} (x) d x
$$

## Variabili Uniformi

Una **variabile aleatoria** $X$ si dice **uniformemente distribuita** su un intervallo $[a, b]$, $b \geq a \left( X \sim \mathcal { U } \left( a , b \right) \right)$ se: 

$$
f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{b - a} & x \in [ a, b ] \\ 0 & \text { altrove } \end{array} \right.
$$

Siccome $\text{supp}(X) = [a, b]$ $[ f _ { X } ( x ) ] = [ a , b ]$, tale è il suo alfabeto (cioè $X$ non assume valori esterni all’intervallo). La sua **CDF** si scrive quindi: 

$$
F _ {X} (x) = \int_ {- \infty} ^ {x} f _ {X} (t)   d t = \left\{ \begin{array}{l l} 0 & x <   a \\ \frac {x - a}{b - a} & a \leq x \leq b \\ 1 & x \geq b \end{array} \right.
$$

mentre la sua media statistica vale: 

$$
\mathbb {E} [ X ] = \int_ {a} ^ {b} \frac {x}{b - a} d x = \frac {b ^ {2} - a ^ {2}}{2 (b - a)} = \frac {a + b}{2}
$$

L’andamento di pdf e CDF sono mostrati nella successiva slide.

### pdf e CDF di variabili uniformi

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c3f6dc9e2a801980935c1605a6b11fb0b0f1678de5a63bed040d1bda1182b2e0.jpg)
Figura 1: pdf della variabile uniforme

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/e00a692547928dec972c2b70ba912cb5b50498747f1c6f2e70e64a8250e0a9f7.jpg)
Figura 2: CDF della variabile uniforme

## Variabili esponenziali

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

### pdf e CDF di variabili esponenziali

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/08ab3fd5b2e073a6d017a7f7cdf795cbed576c47f81a07d9415e45dde49d254f.jpg)
Figura 3: pdf della variabile esponenziale

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/d6303810f7e1eab90d297d7ecd1e8a382e49fb1d59f93cbc76fb80a71f91ff09.jpg)
Figura 4: CDF di $X \sim \varepsilon(\lambda)$

## Variabili laplaciane

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

### pdf e CDF di variabili laplaciane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/39f51fa4ff2eb7cb56cb12410ab682f44fdac428a7255317918a58910ce0f602.jpg)
Figura 5: pdf della variabile laplaciana

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/68af4a0c86ad1fc90ac3bdd3f5e7d395f93a4b0223313d87385837c55eea2f86.jpg)
Figura 6: CDF di $X \sim L(\lambda)$

## Variabili di Cauchy

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

### pdf e CDF di variabili di Cauchy

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/37f192a92d3c0821ce4b3c544298a2f503630eea2717b9e0dc1ae55d1dbeea9d.jpg)
Figura 7: pdf della variabile di Cauchy

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/da62d320d49b4d115fdd49c23baaf8c0b8c15ce9c200a43a8856f458817797aa.jpg)
Figura 8: CDF di $X \sim C(a, b)$

## pdf condizionate

In modo del tutto analogo a quanto fatto per le variabili discrete, potremo scrivere: 

$$
\mathbb {P} \left[ X \in \left(x - \frac {\Delta x}{2}, x - \frac {\Delta x}{2}\right) \mid A \right] = P _ {X} (x, \Delta x | A) \Rightarrow f _ {X | A} (x) = \lim _ {\Delta x \rightarrow 0} \frac {P _ {X} (x , \Delta x | A)}{\Delta x}
$$

o, anche: 

$$
F _ {X \mid A} (x) = \mathbb {P} (X \leq x \mid A) = \frac {\mathbb {P} (\{X \leq x \} \mid \cap A)}{\mathbb {P} (A)} \Rightarrow f _ {X \mid A} (x) = \frac {d F _ {X \mid A} (x)}{d x}
$$

> [!example] Esempio 1
> Per esempio, sia $X \sim L(\lambda)$ $X \sim { \mathcal { L } } ( \lambda ) \ { \textrm { e } } A = \{ - 1 \leq X \leq 2 \} \quad$. Avremo:
>
> $$
> F _ {X | \{- 1 \leq X \leq 2 \}} (x) = \frac {\mathbb {P} (\{X \leq x \} \cap \{- 1 \leq X \leq 2 \})}{F _ {X} (- 1 \leq X \leq 2)} = \left\{ \begin{array}{l l} 0 & x <   - 1 \\ \frac {F _ {X} (x) - F _ {X} (- 1)}{F _ {X} (2) - F _ {X} (- 1)} & - 1 \leq x \leq 2 \\ 1 & x \geq 2 \end{array} \right.
> $$
>
> $$
> f _ {X | \{- 1 \leq X \leq 2 \}} (x) = \left\{ \begin{array}{c l} \frac {f _ {X} (x)}{F _ {X} (2) - F _ {X} (- 1)} = \frac {\frac {\lambda}{2} e ^ {- \lambda | x |}}{1 - \frac {1}{2} e ^ {- 2 \lambda} + \frac {1}{2} e ^ {- \lambda}} & x \in (- 1, 2) \\ 0 & x \notin (- 1, 2) \end{array} \right.
> $$

### pdf e CDF condizionali di variabili Laplaciane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c9bb9b6105893847da5816e4162cf664c0a5d6c418d723bc46ff1a263cd47a27.jpg)
Figura 9: pdf condizionata della variabile laplaciana

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c151e31d1c7e39157c315436b8b74f28bd1d6631fb7d6d648dfe224e47f288e4.jpg)
Figura 10: CDF condizionata della variabile laplaciana

## Legge della probabilità totale per pdf e medie

In modo del tutto analogo al caso discreto (vedi slide 56) si può mostrare che, se $\{A_i\}$ $\{ E _ { m } \} _ { m = 1 } ^ { M }$ è una qualunque partizione di $\Omega$ $\Omega ,$, allora: 

$$
f _ {X} (x) = \sum_ {m = 1} ^ {M} f _ {X | E _ {m}} (x) \mathbb {P} (E _ {m}) \Longleftrightarrow F _ {X} (x) = \sum_ {m = 1} ^ {M} F _ {X | E _ {m}} (x) \mathbb {P} (E _ {m})
$$

Naturalmente, questo implica che per le medie valga un’analoga relazione (vedi slide 57): 

$$
\mathbb {E} \left[ X \right] = \sum_ {m = 1} ^ {M} \mathbb {E} \left[ X | E _ {m} \right] \mathbb {P} (E _ {m}) = \sum_ {m = 1} ^ {M} \mathbb {P} (E _ {m}) \int_ {\mathbb {R}} x f _ {X | E _ {m}} (x) d x
$$

Quindi, con riferimento all’esempio precedente con $X \sim L(\lambda)$ $\begin{array} { r } { X \sim \mathcal { L } ( \lambda ) } \end{array}$ 

$$
\mathbb {E} [ X ] = \mathbb {E} \left[ X | \{- 1 \leq X \leq 2 \} \right] \mathbb {P} (- 1 \leq X \leq 2) + \mathbb {E} \left[ X | \{X \notin [ - 1, 2 ] \} \right] \underbrace {\mathbb {P} (X \notin [ - 1 , 2 ])} _ {1 - \mathbb {P} (- 1 \leq X \leq 2)} = 0
$$

## Funzioni di variabili aleatorie continue -1

Quest’argomento riproduce — come problematica — quello già affrontato nel caso di variabili discrete (vedi slide 58 e seguenti).

Si assuma che $X$ $X = X ( \omega )$ sia una variabile aleatoria continua con alfabeto $\mathcal{X}$, pdf $f(x)$ $f _ { X } ( x ) \mathrm { ~ e ~ C D F ~ } F _ { X } ( x )$.

Sia $g$ $g ( \cdot )$ una funzione il cui insieme di definizione includa i punti di $\mathcal{X}$ $\mathcal { X } \mathrm { ~ - ~ } \mathsf { a }$ meno di un sottoinsieme a (misura di) probabilità nulla;

Si forma la nuova variabile aleatoria: 

$$
Y = g (X) = g [ X (\omega) ] \in \mathcal {Y} \quad \text {   dove   } \mathcal {Y} = g (\mathcal {X})
$$

> [!theorem] Problema
> Ricavare una caratterizzazione di $Y$ dalla caratterizzazione di $X$ in termini di pdf/CDF, $f_Y(y)$ $p _ { Y } ( y ) , y \in \mathcal { Y } ;$, media statistica, $E[Y]$ $\mathbb { E } [ Y ]$.

## Funzioni di variabili aleatorie continue -2

A differenza di quanto analizzato nel caso discreto, si distinguono tre casi principali relativi alla trasformazione di una variabile aleatoria continua $X$ tramite una funzione $y = g(x)$:

1. $g(x)$ è **biunivoca**, ovvero invertibile, continua e derivabile;
2. $g(x)$ è continua, derivabile e univoca — e quindi non invertibile — con $Y$ continuo;
3. $g(x)$ è univoca — e quindi non invertibile — con $Y$ discreto: quest’ultimo caso corrisponde a una **conversione** $\mathsf { A } / \mathsf { D }$ della variabile continua (ovvero una sua quantizzazione o compressione con perdite) in analogia a quanto visto nella conversione $\mathsf { A } / \mathsf { D }$ di segnali e sequenze deterministiche.

## Funzioni invertibili

Si ricorda che se $g(x)$ è invertibile, allora essa è **strettamente monotona** $\forall \space x \in { \mathcal { X } }$. Pertanto:

### Funzione strettamente crescente
Se $g(x)$ è strettamente crescente $( g ^ { \prime } ( x ) > 0 )$:

$$
F _ {Y} (y) = \mathbb {P} (Y \leq y) = \mathbb {P} (g (X) \leq y) = \mathbb {P} (X \leq g ^ {- 1} (y)) = F _ {X} [ g ^ {- 1} (y) ]
$$

$$
f _ {Y} (y) = \frac {d F _ {Y} (y)}{d y} = f _ {X} [ g ^ {- 1} (y) ] \frac {d g ^ {- 1} (y)}{d y} = \frac {f _ {X} [ g ^ {- 1} (y) ]}{g ^ {\prime} [ g ^ {- 1} (y) ]}
$$

### Funzione strettamente decrescente
Se $g(x)$ è strettamente decrescente $( g ^ { \prime } ( x ) < 0 )$:

$$
F _ {Y} (y) = \mathbb {P} (Y \leq y) = \mathbb {P} (g (X) \leq y) = \mathbb {P} (X \geq g ^ {- 1} (y)) = 1 - F _ {X} [ g ^ {- 1} (y) ]
$$

$$
f _ {Y} (y) = - \frac {d F _ {Y} (y)}{d y} = f _ {X} [ g ^ {- 1} (y) ] \frac {d g ^ {- 1} (y)}{d y} = \frac {f _ {X} [ g ^ {- 1} (y) ]}{- g ^ {\prime} [ g ^ {- 1} (y) ]}
$$

In entrambi i casi, la **pdf** (Probability Density Function) $f_Y(y)$ si scrive in forma unificata:

$$
f _ {Y} (y) = \frac {f _ {X} [ g ^ {- 1} (y) ]}{| g ^ {\prime} [ g ^ {- 1} (y) ] |}
$$

## Funzioni non invertibili

Si assuma ora che $g(x)$ non sia invertibile. Questo implica che:

$$
\forall \space y \in \mathcal {Y} \exists \{x _ {i} (y) \} _ {i = 1} ^ {M (y)}: g [ x _ {i} (y) ] = y
$$

Supponiamo, per fissare le idee, $g(x) = x^2$ (per $x \in \mathbb{R}$): questo implica che $g'(x) = 2x$, che si annulla in $x=0$; ovviamente, $g'(x)$ sarà positivo e $g(x)$ crescente per $x > 0$. La funzione ripassa per il valore $y=0$ (con derivata nulla) e si mantiene al di sotto di $y$ fino a $x=0$. Quindi (vedi figura nella prossima slide):

$$
F _ {Y} (y) = \mathbb {P} (Y \leq y) = \mathbb {P} \left(\left\{x _ {1} (y) \leq X \leq x _ {2} (y) \right\} \cup \left\{x _ {4} (y) \leq X \leq x _ {3} (y) \right\}\right) =
$$

$$
F _ {Y} [ x _ {2} (y) ] - F _ {Y} [ x _ {1} (y) ] + F _ {Y} [ x _ {4} (y) ] - F _ {Y} [ x _ {3} (y) ]
$$

dove si è ovviamente sfruttata la disgiunzione dei vari intervalli. Pertanto, derivando:

$$
f _ {Y} (y) = \sum_ {i = 1} ^ {4} (- 1) ^ {i} f _ {X} [ x _ {i} (y) ] x _ {i} ^ {\prime} (y) = \sum_ {i = 1} ^ {4} \frac {f _ {X} [ x _ {i} (y) ]}{| g ^ {\prime} [ x _ {i} (y) ] |}
$$

dove si è sfruttato il fatto che $g'(x) \neq 0$ quasi ovunque e che i segni sono alternati.

### Rappresentazione grafica
$$
f _ {Y} (y _ {1}) = \sum_ {i = 1} ^ {3} f _ {X} \left[ x _ {i} (y _ {1}) \right] \left| \frac {d x _ {i} (y)}{d y} \right| _ {y = y _ {1}} = \sum_ {i = 1} ^ {3} \frac {f _ {X} \left[ x _ {i} (y _ {1}) \right]}{\left| g ^ {\prime} [ x _ {i} (y _ {1}) ] \right|}
$$

$$
f _ {Y} (y _ {2}) = \sum_ {i = 1} ^ {2} f _ {X} \left[ x _ {i} (y _ {2}) \right] \left| \frac {d x _ {i} (y)}{d y} \right| _ {y = y _ {2}} = \sum_ {i = 1} ^ {2} \frac {f _ {X} \left[ x _ {i} (y _ {2}) \right]}{\left| g ^ {\prime} [ x _ {i} (y _ {2}) ] \right|}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/75daf37cde2197ea8b008ceadbbf1a23f380a8edcd7d8eeba4bc90f54e811575.jpg)
Figura 1: Rappresentazione della funzione non invertibile $g(x) = x^2$.

## Qualche esempio - 1

Sia $X$ una variabile aleatoria con pdf $f_X(x)$. Si considerino le trasformazioni $y = g(x)$. Vogliamo determinare le pdf di $Y$.

> [!example] Esempio 1
> Per $g(x) = e^x$, si ha che, poiché $g'(x) = e^x > 0$ e $g(x)$ è biunivoca per $x \in \mathbb{R}$, la pdf sarà:
>
> $$
> x ^ {2} = y \rightarrow x (y) = \sqrt {y} \rightarrow x ^ {\prime} (y) = \left. \frac {1}{g ^ {\prime} (x)} \right| _ {x = \sqrt {y}} = \left. \frac {1}{2 x} \right| _ {x = \sqrt {y}} = \frac {1}{2 \sqrt {y}}
> $$
>
> Quindi:
>
> $$
> f _ {Y _ {1}} (y) = \left. \lambda e ^ {- \lambda x} u (x) \right| _ {x = \sqrt {y}} x ^ {\prime} (y) = \frac {\lambda}{2 \sqrt {y}} e ^ {- \lambda \sqrt {y}} u (y)
> $$

Per $g(x) = x^2$, invece, essendo $g(x)$ non biunivoca e l’equazione $y = x^2$ avente due soluzioni $x = \pm\sqrt{y}$ per $y > 0$. Si noti inoltre che $f_X(x)$ è simmetrica rispetto a $x=0$, cioè $f_X(x) = f_X(-x)$. Quindi:

$$
f _ {Y _ {2}} (y) = \left[ \frac {f _ {X} (\sqrt {y})}{| g ^ {\prime} (\sqrt {y}) |} + \frac {f _ {X} (- \sqrt {y})}{| g ^ {\prime} (- \sqrt {y}) |} \right] u (y), \quad \text { poichè } \quad f _ {X} (x) = \frac {1}{\pi} \frac {1}{1 + x ^ {2}} \Rightarrow
$$

$$
f _ {Y _ {2}} (y) = \left(\frac {1}{2 \pi \sqrt {y}} \frac {1}{1 + y} + \frac {1}{2 \pi \sqrt {y}} \frac {1}{1 + y}\right) u (y) = \frac {1}{\pi \sqrt {y}} \frac {1}{1 + y} u (y)
$$

## Qualche esempio - 2

Sia $X$ una variabile aleatoria. Vogliamo la pdf di $Y = g(X)$, cioè assumiamo $y = g(x)$.

> [!example] Esempio 2
> Notiamo preliminarmente che $g'(x) \neq 0$ qualunque sia $x$. Inoltre, $g(x)$ è monotona crescente: potrebbe non essere strettamente crescente se $g(x)$ non fosse connesso, ma escludiamo questo caso.
>
> Avremo allora:
>
> $$
> g (x) = F _ {X} (x) \rightarrow x (y) = F _ {X} ^ {- 1} (y) \quad g ^ {\prime} (x) = f _ {X} (x) \Longrightarrow
> $$
>
> $$
> f _ {Y} (y) = \frac {f _ {X} \left[ F _ {X} ^ {- 1} (y) \right]}{f _ {X} \left[ F _ {X} ^ {- 1} (y) \right]} \Pi \left(y - \frac {1}{2}\right) = \Pi \left(y - \frac {1}{2}\right)
> $$
>
> cioè $f_Y(y) = f_X(g^{-1}(y)) \cdot |(g^{-1})'(y)|$ $Y \sim \mathcal { U } ( 0 , 1 )$.
>
> Quindi, se si ha una variabile aleatoria uniforme $X \sim U(0, 1)$, la trasformazione $g(x)$ genera una variabile aleatoria con pdf arbitraria $f_Y(y) = f_X(g^{-1}(y)) \cdot |(g^{-1})'(y)|$: questo ha delle notevoli conseguenze nelle procedure di simulazione dei sistemi numerici.

## Qualche esempio - 3

Sia $X$ una variabile aleatoria con pdf $f_X(x)$. Vogliamo la pdf di $Y = g(X)$.

> [!example] Esempio 3
> Notiamo preliminarmente che $g'(x) \neq 0$ e che la trasformazione non è biunivoca. Infatti:
>
> $$
> y = A \cos (2 \pi x + \varphi) \rightarrow 2 \pi x (y) + \varphi = \pm \arccos \left(\frac {x}{A}\right)
> $$
>
> Valutando la derivata dell’inversa si ha:
>
> $$
> \begin{array}{l} x ^ {\prime} (y) = \frac {1}{g ^ {\prime} (x)} \Big | _ {x = x (y)} = - \frac {1}{2 \pi A \sin (2 \pi x + \varphi)} \Big | _ {2 \pi x = \pm \arccos \left(\frac {y}{A}\right) - \varphi} = \\ = \pm \frac {1}{2 \pi A \sin [ \arccos (\frac {y}{A}) ]} = \pm \frac {1}{2 \pi A \sqrt {1 - (\frac {y}{A}) ^ {2}}} \end{array}
> $$
>
> Poiché $g'(x) \neq 0$, applicando le formule precedenti si ha:
>
> $$
> f _ {Y} (y) = \frac {1}{\pi A \sqrt {1 - \left(\frac {y}{A}\right) ^ {2}}}, \qquad y \in [ - A, A ]
> $$

# Conversione A/D di variabili aleatorie

Quando $X$ è una variabile continua e $Y$ è una variabile discreta, si ha una **conversione** $\mathsf { A } / \mathsf { D }$ di una quantità aleatoria (confronta anche l’ultima sezione della parte ”Conversione $\mathsf { A } / \mathsf { D } ^ { \prime \prime } )$").

Supponiamo di voler rappresentare $X$ con $R$ bit, ovvero con $M = 2 ^ { R }$ livelli. 

Definiamo una variabile aleatoria $\boldsymbol { Y } = \boldsymbol { g } ( \boldsymbol { X } )$ con $\mathcal { Y } = \{ y _ { 1 } , \dots , y _ { M } \}$. 

Definiamo una partizione di $X$ in $M$ intervalli, definiti dai punti $\{ x _ { i } \} _ { i = 1 } ^ { M + 1 }$. 

Si definisce rappresentazione a $R$ bit di $X$ la variabile aleatoria discreta: 

$$
Y = y _ {i} \quad \text { se } x _ {i} \leq X \leq x _ {i + 1} \quad i = 1, \dots , M
$$

La **pmf** (Probability Mass Function) di $Y$ quindi si scrive facilmente nella forma: 

$$
p _ {Y} (y _ {i}) = P _ {X} \left(\frac {x _ {i + 1} + x _ {i}}{2}; \frac {x _ {i + 1} - x _ {i}}{2}\right) = F _ {X} (x _ {i + 1}) - F _ {X} (x _ {i}), \quad i = 1, \ldots , M
$$

> [!quote] Osservazione
> Ovviamente tanto la partizione quanto i livelli di rappresentazione sono gradi di libertà a disposizione del progettista. 

## Media di funzioni di variabili aleatorie continue

Sia $X$ una variabile aleatoria continua con pdf $f_X(x)$ e sia $g(x)$ una funzione tale che $\mathcal { V } = g ( \mathcal { X } )$. Vogliamo estendere alle variabili continue il Teorema Fondamentale per il calcolo della media (vedi slide 60 e seguenti). Il risultato principale - diretta derivazione del caso discreto - è che, qualunque sia $g(x)$, vale:

$$
\mathbb {E} \left[ Y \right] = \mathbb {E} \left[ g (X) \right] = \int_ {\mathbb {R}} g (x) f _ {X} (x) d x
$$

Definiamo una versione quantizzata di $X$ a $M$ livelli, $x ^ { \Delta }$, in modo del tutto analogo a quanto fatto per ricavare la media di variabili continue (vedi slide 100). 

A questa applichiamo la trasformazione $g ( \cdot )$, ottenendo la variabile discreta ${ \cal Y } ^ { \Delta } = g ( X ^ { \Delta } )$: 

$$
X ^ {\Delta} = x _ {i} \in [ i \Delta , (i + 1) \Delta [ \quad i \Delta \leq X <   (i + 1) \Delta \Rightarrow g (X ^ {\Delta}) = g (x _ {i})
$$

Il teorema quindi segue - se $g ( x ) f _ { X } ( x )$ è Riemann-integrabile - dall’essere:

$$
\mathbb {E} \left[ Y \right] = \lim _ {\Delta \rightarrow 0} \mathbb {E} \left[ Y ^ {\Delta} \right] = \lim _ {\Delta \rightarrow 0} \sum_ {i = 1} ^ {M} g (x _ {i}) \underbrace {f _ {X} (x _ {i}) \Delta} _ {\simeq \mathbb {P} (i \Delta \leq X <   (i + 1) \Delta)} = \int_ {\mathbb {R}} g (x) f _ {X} (x)   d x
$$

## Valore quadratico medio e varianza di variabili continue

A questo punto è immediata la generalizzazione dei concetti introdotti per variabili discrete a variabili continue. 

Data una variabile aleatoria $X$ con media $\mu _ { X } = \operatorname { \mathbb { E } } [ X ]$, definiamo: 

Il **valore quadratico medio** (Mean Square) di $X$: 

$$
X _ {\mathrm{rms}} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] = \int_ {\mathbb {R}} x ^ {2} f _ {X} (x) d x
$$

Il **valore efficace** (root mean square, rms) di $X$: 

$$
X _ {\mathrm{rms}} = \sqrt {\mathbb {E} \left[ X ^ {2} \right]} = \sqrt {\int_ {\mathbb {R}} x ^ {2} f _ {X} (x) d x}
$$

La **varianza** di $X$: 

$$
\sigma_ {X} ^ {2} = \mathbb {E} \left[ (X - \mu_ {X}) ^ {2} \right] = \int_ {\mathbb {R}} (x ^ {2} + \mu_ {X} ^ {2} - 2 x \mu_ {X}) f _ {X} (x) d x = X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}
$$

La **deviazione standard** di $X$: 

$$
\sigma_ {X} = \sqrt {\sigma_ {X} ^ {2}} = \sqrt {\mathbb {E} [ X ^ {2} ] - \mu_ {X} ^ {2}} = \sqrt {X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}}
$$

> [!tip] Nota
> Tutte le proprietà della slide 68 valgono ovviamente anche per variabili continue. 

## Qualche esempio

> [!example] Esempio 1 (*Calcolo Media*)
> Sia $X$ una variabile aleatoria con pdf $f_X(x) = \frac{1}{2}$ per $x \in [-1, 1]$. Si ottiene facilmente: 
>
> $$
> \mu_ {X} = \frac {a + b}{2} \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {a ^ {2} + b ^ {2} + a b}{3} \qquad \sigma_ {X} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] - \mu_ {X} ^ {2} = \frac {(b - a) ^ {2}}{1 2}
> $$

> [!example] Esempio 2 (*Calcolo Varianza*)
> Sia $f_X(x) = x$ per $x \in [0, 1]$. Avremo: 
>
> $$
> \mu_ {X} = \frac {1}{\lambda} \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {2}{\lambda^ {2}} \qquad \sigma_ {X} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] - \mu_ {X} ^ {2} = \frac {1}{\lambda^ {2}}
> $$

> [!example] Esempio 3 (*Calcolo RMS*)
> Sia $f_X(x) = \frac{1}{2}$ per $x \in [0, 2]$. Avremo: 
>
> $$
> \mu_ {X} = 0 \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {2}{\lambda^ {2}} \qquad \sigma_ {X} ^ {2} = \mathbb {E} [ X ^ {2} ] = \frac {2}{\lambda^ {2}}
> $$

> [!example] Esempio 4 (*Caso non integrabile*)
> Sia $f_X(x) = \frac{1}{x^2}$ per $x \in [1, \infty)$. Non esistono in questo caso né la media, né la varianza, né, quindi, il valore rms o la deviazione standard. 

## Variabili continue multiple 

In perfetta analogia con quanto fatto per variabili discrete (vedi slide 69), una coppia di variabili continue (o variabile doppia) è definita nella forma: 

$$
X, Y: \omega \in \Omega \longrightarrow (X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y} \subseteq \mathbb {R} ^ {2}
$$

dove $\mathcal { X } \in \mathcal { V }$ sono gli alfabeti di $X$ e di $Y$ rispettivamente. 

Analogamente, date tre variabili aleatorie - a questo punto non importa più se tutte continue o meno $\begin{array} { r } { - X ( \omega ) \in \mathcal { X } , y ( \omega ) \in \mathcal { Y } , Z ( \omega ) \in \mathcal { Z } ; } \end{array}$ 

$$
X, Y, Z: \omega \in \Omega \longrightarrow (X (\omega), Y (\omega), Z (\omega)) \in \mathcal {X} \times \mathcal {Y} \times \mathcal {Z} \subseteq \mathbb {R} ^ {3}
$$

e, date $m$ variabili aleatorie $X _ { i } \in \mathcal { X } _ { i } \subseteq \mathbb { R }$, avremo la $m$-pla aleatoria: 

$$
X _ {1}, \dots , X _ {m}: \omega \in \Omega \longrightarrow (X _ {1} (\omega), \dots , X _ {m} (\omega)) \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {m} \subseteq \mathbb {R} ^ {m}
$$

## pdf congiunta di due variabili aleatorie

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

## Proprietà della pdf congiunta

La **pdf congiunta** $f _ { X , Y } ( x , y )$ condivide con la pmf congiunta $p x , \gamma ( x , y ) \textrm { - e }$, per alcune, con tutte le densità, le seguenti proprietà: 

### Proprietà di marginalizzazione

$$
\int_ {\mathbb {R}} f _ {X, Y} (x, y) d y = f _ {X} (x) \qquad \int_ {\mathbb {R}} f _ {X, Y} (x, y) d x = f _ {Y} (y)
$$

Per cui caratterizzare congiuntamente $( X , Y )$ significa anche caratterizzarle marginalmente, mentre il viceversa non è necessariamente vero. 

### Indipendenza statistica

Due variabili aleatorie sono **indipendenti** se e solo se 

$$
f _ {X, Y} (x, y) = f _ {X} (x) f _ {Y} (y) \Longleftrightarrow F _ {X, Y} (x, y) = \mathbb {P} (X \leq x, Y \leq y) = F _ {X} (x) F _ {Y} (y)
$$

Più in generale, se $X _ { i } \sim f _ { X _ { i } } ( x ) , x \in \mathcal { X } _ { i }$, allora esse sono indipendenti se e solo se: 

$$
f _ {X _ {1}, \dots , X _ {m}} (x _ {1}, \dots , x _ {m}) = \prod_ {i = 1} ^ {m} f _ {X _ {i}} (x _ {i}), \qquad (x _ {1}, \dots , x _ {m}) \in \mathbb {R} ^ {m}
$$

## Le pdf condizionate

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

## Proprietà delle pdf condizionate

Data l’analogia con le variabili discrete, ci limitiamo qui a riscrivere le proprietà della slide 74. 

$f _ { X \mid Y } ( x | y )$ se $y$ resta fisso e $x$ varia in $X$ è una densità di probabilità, cioè: 

$$
f _ {X | Y} (x | y) \geq 0 \int_ {\mathbb {R}} f _ {X | Y} (x | y) d x = 1
$$

### Legge della probabilità totale per le pdf

$$
f _ {X} (x) = \int_ {\mathbb {R}} f _ {X, Y} (x, y) d y = \int_ {\mathbb {R}} f _ {X | Y} (x | y) f _ {Y} (y) d y
$$

$$
f _ {Y} (y) = \int_ {\mathbb {R}} f _ {X, Y} (x, y) d x = \int_ {\mathbb {R}} f _ {Y | X} (y | x) f _ {X} (x) d x
$$

### Leggi della probabilità composta e di Bayes per le densità

$$
f _ {X, Y} (x, y) = f _ {Y} (y) f _ {X | Y} (x | y) = f _ {X} (x) f _ {Y | X} (y | x) \Rightarrow f _ {Y | X} (y | x) = \frac {f _ {Y} (y) f _ {X | Y} (x | y)}{f _ {X} (x)}
$$

## Altre estensioni...

Come nel caso discreto, avremo: 

Se $Z = \boldsymbol { \mathrm { g } } ( \boldsymbol { X } , \boldsymbol { Y } )$ allora 

$$
\mathbb {E} [ Z ] = \int_ {\mathbb {R} ^ {2}} g (x, y) f _ {X}, \gamma (x, y) d x d y
$$

### Linearità della media

$$
\mathbb {E} \left[ \sum_ {i = 1} ^ {m} a _ {i} X _ {i} \right] = \sum_ {i = 1} ^ {m} a _ {i} \mathbb {E} \left[ X _ {i} \right]
$$

### Teorema della media condizionata

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

## Covarianza tra due variabili continue

Siano $( X , Y ) \sim f _ { X , Y } ( x , y )$. Denotiamo con $( \mu _ { X } , \mu _ { Y } )$ le rispettive medie e $( \sigma _ { X } ^ { 2 } , \sigma _ { Y } ^ { 2 } )$ le rispettive varianze. Avremo, in analogia al caso discreto: 

### Covarianza tra $X \in Y ;$

$$
\operatorname{COV} [ X, Y ] = \mathbb {E} \left[ (X - \mu_ {X}) (Y - \mu_ {Y}) \right] = \mathbb {E} [ X Y ] - \mu_ {X} \mu_ {Y}
$$

### Coefficiente di correlazione tra $X \textsf { e Y }$

$$
\rho_ {X, Y} = \frac {\operatorname{COV} [ X , Y ]}{\sigma_ {X} \sigma_ {Y}}, \quad \left| \rho_ {X, Y} \right| \leq 1
$$

### Incorrelazione tra $X \textsf { e } Y \colon { \mathsf { C O V } } [ X , Y ] = 0$

> [!quote] Osservazione
> Indipendenza implica incorrelazione, ma incorrelazione non implica indipendenza. 

## Variabili Gaussiane: Caratterizzazione marginale

Una variabile aleatoria $X _ { 0 } \in \mathcal { X } = \mathbb { R }$ si dice **Gaussiana** (o Normale) standard - $X _ { 0 } \sim \mathcal { N } ( 0 , 1 )$ se: 

$$
f _ {X _ {0}} (x _ {0}) = \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {x _ {0} ^ {2}}{2}}, \quad x \in \mathbb {R} \quad \Longrightarrow \quad \mathbb {E} [ X _ {0} ] = 0 \quad \sigma_ {X _ {0}} ^ {2} = \mathbb {E} [ X _ {0} ^ {2} ] = 1
$$

Consideriamo ora la variabile aleatoria $X = \sigma _ { X } X _ { 0 } + \mu _ { X } , \sigma _ { X } > 0 \mathrm { ~ e ~ } \mu _ { X } \in \mathbb { R }$. Applicando i risultati delle slide 114 e seguenti alla funzione lineare $g ( x ) = \sigma { x } { x } + \mu { x }$ otteniamo: 

$$
f _ {X} (x) = \frac {1}{\sqrt {2 \pi \sigma_ {X} ^ {2}}} e ^ {- \frac {(x - \mu_ {X}) ^ {2}}{2 \sigma_ {X} ^ {2}}}, \quad x \in \mathbb {R} \quad \Longrightarrow X \sim \mathcal {N} (\mu_ {X}, \sigma_ {X} ^ {2})
$$

dove ovviamente: 

$$
\mathbb {E} [ X ] = \mathbb {E} \left[ \sigma_ {X} X _ {0} + \mu_ {X} \right] = 0
$$

$$
\mathbb {E} \left[ (X - \mu_ {X}) ^ {2} \right] = \operatorname{VAR} \left[ \sigma_ {X} X _ {0} + \mu_ {X} \right] = \sigma_ {X} ^ {2}
$$

## Andamenti di pdf Gaussiane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/14bd5c980e8521e5eb02a7517ff1fac46626c196028264217617a09b4afc4823.jpg)
Figura 1: Andamenti di pdf Gaussiane.

## La funzione Q(x)

Sia $X _ { 0 } \sim \mathcal { N } ( 0 , 1 )$: nè la sua CDF né la sua CCDF sono note in forma esplicita, poiché $e ^ { - \gamma x ^ { 2 } }$ non ammette primitive elementari. 

Definiamo: 

$$
Q (x) \stackrel {\mathrm{def}} {=} \mathbb {P} (X \geq x) = 1 - F _ {X _ {0}} (x) = \frac {1}{\sqrt {2 \pi}} \int_ {x} ^ {\infty} e ^ {- \frac {t ^ {2}}{2}} d t
$$

per cui: 

$$
F _ {X _ {0}} (x) = 1 - Q (x) \quad P _ {X _ {0}} (x; \Delta x) = Q \left(x - \frac {\Delta x}{2}\right) - Q \left(x + \frac {\Delta x}{2}\right)
$$

Ovviamente, se $X \sim \mathcal { X } ( \mu _ { X } , \sigma _ { X } ^ { 2 } )$, avremo $X = X _ { 0 } \sigma _ { X } + \mu _ { X }$, per cui: 

$$
1 - F _ {X} (x) = \frac {1}{\sqrt {2 \pi \sigma_ {X} ^ {2}}} \int_ {x} ^ {\infty} e ^ {- \frac {(t - \mu_ {X}) ^ {2}}{2 \sigma_ {X} ^ {2}}} d t = Q \left(\frac {x - \mu_ {X}}{\sigma_ {X}}\right)
$$

Dato il suo uso frequente, nella prossima slide è presentato un diagramma della funzione $Q ( x ) , x \geq 0$. 

## Andamento di Q(x)

$$
Q (x) \sim \frac {1}{x \sqrt {2 \pi}} e ^ {- \frac {x ^ {2}}{2}} <   e ^ {- \frac {x ^ {2}}{2}}, \qquad x \to \infty
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9e014a72e6bb4cff5f6045f5e3af68f8479b85e9889bcb10a79b45de356eb16a.jpg)
Figura 2: Andamento di Q(x).

## Alcune utili proprietà della funzione Q(x)

Si noti preliminarmente che 

$$
Q (- \infty) = \frac {1}{\sqrt {2 \pi}} \int_ {\mathbb {R}} e ^ {- \frac {t ^ {2}}{2}} d x = 1 \qquad Q (\infty) = 0
$$

Inoltre: 

$$
\frac {d Q (x)}{d x} = - \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {x ^ {2}}{2}} <   0 \forall \space x \rightarrow Q (x) \text {   è   decrescente   in   } x
$$

### Simmetria

$$
Q (- x) = \frac {1}{\sqrt {2 \pi}} \int_ {- x} ^ {\infty} e ^ {- \frac {t ^ {2}}{2}} d t = 1 - \underbrace {\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {- x} e ^ {- \frac {t ^ {2}}{2}} d t} _ {= Q (x)} = 1 - Q (x)
$$

Se $X \sim \mathcal N ( \mu _ { X } , \sigma _ { X } ^ { 2 } )$ allora: 

$$
\mathbb {P} (X \geq \eta) = \mathbb {P} (X _ {0} \sigma_ {X} + \mu_ {X} \geq \eta) = \mathbb {P} (X _ {0} \geq \frac {\eta - \mu_ {X}}{\sigma_ {X}}) = Q (\frac {\eta - \mu_ {X}}{\sigma_ {X}})
$$

## Caratterizzazione congiunta di variabili Gaussiane

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

## Alcune proprietà della matrice di covarianza

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

## Variabili congiuntamente Gaussiane

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

## Richiami sulle variabili aleatorie

- Si consideri uno spazio di probabilità arbitrario, $\Omega , \tau , \mathbb { P }$, dove $\Omega \ { \dot { \mathbf { e } } }$ lo spazio dei campioni, $\mathcal{T}$ una $\sigma$-algebra di eventi di $\Omega \textsf { e l P } \colon { \mathcal { T } }  [ 0 , 1 ]$ una legge di probabilità. 

- Ricordiamo che una **variabile aleatoria** reale $X$ è una funzione (misurabile) definita come: 

$$
X: \omega \in \Omega \Longrightarrow X (\omega) \in \mathcal {X} \subseteq \mathbb {R}
$$

- La variabile aleatoria è discreta se tale è $X$, continua se tale è $X$. 

- Una coppia di variabili aleatorie è un’applicazione 

$$
X, Y: \omega \in \Omega \Longrightarrow (X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y} \subseteq \mathbb {R} ^ {2}
$$

- La variabile aleatoria $X$ si dice completamente caratterizzata se ne $\grave { \mathbf { e } }$ nota la **CDF** $F _ { X } ( x ) \circ$ - equivalentemente - la **DF** $p _ { X } ( x )$ o la **pdf** $f _ { X } ( x )$ nel caso discreto e continuo, rispettivamente: 

$$
F _ {X} (x) = \mathbb {P} \left\{X \leq x \right\} \forall \space x \in \mathbb {R} p _ {X} (x) = \mathbb {P} \left\{X = x \right\} \forall \space x \in \mathcal {X} f _ {X} (x) = \frac {d f _ {X} (x)}{d x}
$$

- Parallelamente, per la coppia $( X , Y )$ si ha: 

$$
F _ {X, Y} (x, y) = \mathbb {P} \left\{X \leq x, Y \leq y \right\} \forall \space (x, y) \in \mathbb {R} ^ {2} f _ {X, Y} (x, y) = \frac {\partial^ {2} F _ {X , Y} (x , y)}{\partial x \partial y}
$$

$$
p _ {X, Y} (x, y) = \mathbb {P} \{X = x, Y = y \} \forall \space x \in \mathcal {X} \times \mathcal {Y}
$$

## Vettori aleatori

- Una **n-pla aleatoria** è una ovvia generalizzazione del concetto di coppia di variabili aleatorie, cioè: 

$$
\left(X _ {1}, \dots , X _ {n}\right): \omega \in \Omega \Longrightarrow \boldsymbol {X} (\omega) = \left(X _ {1} (\omega), \dots , X _ {n} (\omega)\right) \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {n} \subseteq \mathbb {R} ^ {n}
$$

- Un vettore aleatorio si ottiene quindi facilmente come 

$$
\boldsymbol {X} (\omega) = \left[ X _ {1} (\omega), \dots , X _ {n} (\omega) \right] ^ {T} \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {n} \subseteq \mathbb {R} ^ {n}
$$

- Se gli alfabeti $\mathcal { X } _ { 1 } , \ldots \mathcal { X } _ { n }$ sono discreti, il vettore è discreto e si caratterizza mediante la DF congiunta; 

$$
p _ {\mathcal {X}} (\boldsymbol {x}) = p _ {\mathcal {X}} \left(x _ {1}, \dots , x _ {n}\right) = \mathbb {P} \left\{X _ {1} = x _ {1}, \dots , X _ {n} = x _ {n} \right\} \forall \space \boldsymbol {x} \in \mathcal {X} _ {1} \times \dots \mathcal {X} _ {n}
$$

dove $\pmb { x } = [ x _ { 1 } , \dots , x _ { n } ] ^ { T } \in \mathcal { X } _ { 1 } \times \dots \mathcal { X } _ { n }$ 

- Per alfabeti continui, avremo 

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

- Analogamente, per vettori continui avremo 

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \prod_ {i = 1} ^ {n} f _ {X _ {i} | X _ {i - 1}, \dots , X _ {1}} (x _ {i} | x _ {i - 1}, \dots , x _ {1})
$$

## Processi aleatori tempo-discreti

Si definisce **processo aleatorio tempo-discreto** un’applicazione che ad ogni elemento dello spazio campione fa corrispondere una successione:

$$
X: \omega \in \Omega \longrightarrow \{X (n, \omega) \} _ {n \in \mathbb {Z}}
$$

dove $\mathbb{Z}$ indica l’insieme degli interi.

> [!example] Esempio 1 (Realizzazioni di un processo tempo-discreto)
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

## Commenti e osservazioni

- Per ogni valore di $\omega \in \Omega$ il processo si realizza in una sequenza che assume valori nell’intervallo $[-1, 1]$;
- Fissando l’istante di tempo $n = n _ { 0 }$ e facendo variare $\omega \in \Omega$ otteniamo $X ( n _ { 0 } , \omega )$ che è una variabile aleatoria (visto che ”campionando verticalmente” il processo otteniamo che al variare di $\omega X ( n _ { 0 } , \omega )$ assume diverse determinazioni);
- La variabile aleatoria $X ( n _ { 0 } , \omega )$ ha una sua pdf, che in genere dipende da $\omega ;$;
- Se la pdf non dipende dall’istante di campionamento $\boldsymbol { n _ { 0 } }$, il processo si dice **stazionario al primo ordine**.
- Nel caso mostrato in figura, il processo è stato generato assumendolo stazionario e marginalmente uniforme in $[ - 0 . 5 , 0 . 5 ]$, cioè:

$$
f _ {X (n)} (x; n) = f _ {X (n)} (x) = \Pi (x - 0. 5)
$$

> [!quote] Osservazione
> Si noti che siccome
> 
> $$
> \mathbb {E} [ X (n) ] = \int_ {- \infty} ^ {\infty} x f _ {X (n)} (x; n) d x = \int_ {- 0, 5} ^ {0, 5} x \Pi (x - 0. 5) d x = 0
> $$
> 
> il processo è a media identicamente nulla.

## Un altro esempio: processo Gaussiano tempo-discreto

Come secondo esempio, consideriamo un processo tempo-discreto stazionario al primo ordine con pdf:

$$
f _ {X (n)} (x) = \frac {1}{\sqrt {2 \pi}} \exp \left[ - \frac {(x + 0 . 5) ^ {2}}{2} \right]
$$

quindi con densità marginale Gaussiana a media $-0.5$ e varianza unitaria. Otteniamo realizzazioni del tipo rappresentate in figura:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/48a5eafdb76a91cfaeec049306e38b42c43e3516620a31cd0a3e5059967ed7ab.jpg)
Figura 4: Realizzazione Gaussiana 1

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/51684a9d1e2c1908853f9b305d6cbfc31882599c788d4ca54497b82c5cfb42be.jpg)
Figura 5: Realizzazione Gaussiana 2

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/2c12f75b390651df009e373f8c5f9758ea1925d2f1a52f06939bfdc2260a96eb.jpg)
Figura 6: Realizzazione Gaussiana 3

## Caratterizzazione del secondo ordine del processo

- Un processo aleatorio si dice **caratterizzato al primo ordine** se ne è nota la pdf $f _ { X ( n ) } ( x ; n )$ per ogni $n$. Se il processo è stazionario al primo ordine, questo equivale ad assegnare un’unica pdf.
- Un processo aleatorio si dice **caratterizzato al secondo ordine** se ne è assegnata la pdf congiunta:

$$
f _ {X (n _ {1}), X (n _ {2})} \big (x _ {1}, x _ {2}; n _ {1}, n _ {2} \big), \quad \forall \space n _ {1}, n _ {2}
$$

- Un processo aleatorio si dice **stazionario al secondo ordine** se, per qualsiasi intero $h$, abbiamo:

$$
f _ {X (n _ {1}), X (n _ {2})} (x _ {1}, x _ {2}; n _ {1}, n _ {2}) = f _ {X (n _ {1} + h), X (n _ {2} + h)} (x _ {1}, x _ {2}; n _ {1}, n _ {2} + h)
$$

- In altre parole, un processo stazionario al secondo ordine è tale che la caratterizzazione congiunta di due suoi campioni dipende unicamente dalla loro ”distanza” temporale, ma non dalla loro posizione: in altre parole, la pdf congiunta è invariante ad atti di moto rigido dei due punti in anticipo o in ritardo.
- Ovviamente un processo stazionario al secondo ordine lo è anche al primo, ma non è vero il viceversa. Perchè?

## Caratterizzazione completa di un processo

Un processo aleatorio $X ( n )$ si dice **completamente caratterizzato** se, detto $M$ un intero arbitrario e detti $n _ { 1 } , \ldots , n _ { M }$ $M$ istanti arbitrari, il vettore aleatorio:

$$
\boldsymbol {X} = [ X (n _ {1}), \dots , X (n _ {M}) ] ^ {T}
$$

ha densità di probabilità $f _ { \pmb { X } } ( x _ { 1 } , \ldots , x _ { M } )$ nota.

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

Si definisce **processo ampiezza discreto** (o - per brevità - **processo discreto**) un processo aleatorio in cui le cui realizzazioni siano sequenze di numeri che possano assumere valore in un alfabeto discreto.

Un caso di importanza notevole è quello di un **processo indipendente binario**, $X ( n ) \in \{ - 1 , 1 \}$, con $\mathbb { P } \left\{ X ( n ) = 1 \right\} = \mathbb { P } \left\{ X ( n ) = 1 \right\} = { \frac { 1 } { 2 } }$, di cui le realizzazioni sono riportate in figura, anche detto **Processo di Bernoulli**.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/62faba250dc710ba5cb9fbd4a331bfdc4d2dc4cd5d3bd696b38454e5f14bc19a.jpg)
Figura 7: Realizzazioni del processo di Bernoulli

## Un altro esempio: Un processo quaternario

Un ulteriore esempio si ha considerando un **alfabeto quaternario**, per esempio $X ( n ) \in \{ - 2 , - 1 , 1 , 2 \}$, con livelli equiprobabili (per cui ${ \mathbb { P } } \left\{ X ( n ) = i \right\} = { \textstyle { \frac { 1 } { 4 } } } \ \forall \space i )$).

Le realizzazioni del processo saranno quindi del tipo rappresentato in figura:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9f7957aa1d5176320b74eb7c6ea5945937ed809d0cfc9354252211d9f644fc02.jpg)
Figura 1: Realizzazioni di un processo quaternario.

## Caratterizzazione di processi discreti

Tutte le definizioni introdotte per i processi continui si estendono ai **processi discreti**, con la sola differenza che le densità di probabilità sono ora sostituite dalle **funzioni di massa di probabilità** (DF).

> [!theorem] Definizione: Funzione di Massa di Probabilità (DF)
> Intuitivamente, la DF indica la probabilità che una variabile aleatoria discreta assuma un valore specifico. Ad esempio, in un lancio di un dado, la DF assegna $1/6$ a ogni numero da 1 a 6.
>
> Formalmente, per una variabile aleatoria discreta $X$, la funzione di massa $p(x)$ è definita come:
> $$p(x) = P(X = x)$$

Un processo discreto si dice **stazionario in senso stretto** se, comunque si scelga un intero $M$, il vettore aleatorio $\pmb { X } = [ X ( n _ { 1 } ) , \dots , X ( n _ { M } )$ gode, per un $h$ arbitrario, della proprietà:

$$
\begin{array}{c} \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2}, \ldots X (n _ {M}) = x _ {M} \right\} \qquad = \\ \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2}, \ldots X (n _ {M} + h) = x _ {M} \right\} \end{array}
$$

Ovviamente, la stazionarietà di ordine $M$ implica quella di ogni ordine $\leq M$. In particolare, un processo stazionario ha una DF marginale indipendente dal tempo.

Un processo discreto che sia stazionario e indipendente gode ovviamente della proprietà:

$$
\mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2}, \dots X (n _ {M}) = x _ {M} \right\} = \prod_ {i = 1} ^ {M} \mathbb {P} \left\{X (n _ {i}) = x _ {i} \right\} = \prod_ {i = 1} ^ {M} p _ {X} (x _ {i})
$$

dove $p _ { X } ( \cdot )$ è la DF marginale (ovviamente indipendente dal tempo).

## Caratterizzazione sintetica dei vettori aleatori

Come per le variabili aleatorie, anche per i processi aleatori è possibile — a fronte di un’impossibilità di fornirne una caratterizzazione completa — definire una **caratterizzazione sintetica**, cioè assegnarne statistiche che siano significative.

In modo del tutto analogo al caso scalare, dove abbiamo visto che la coppia media-varianza $( \mu x , \sigma _ { X } ^ { 2 } )$ offre spesso importanti informazioni sul comportamento della variabile $X$, e al caso delle coppie, in cui la cinquina $( m u _ { X } , \sigma _ { X } , \mu _ { Y } , \sigma _ { Y } , \mathrm { C O V } ( X , Y )$ offre analoghe informazioni sulla coppia $(X, Y)$, per un vettore aleatorio $\pmb { X } = [ X _ { 1 } , \ldots , X _ { n } ] ^ { T }$ abbiamo:

###1 La media statistica
$$
\boldsymbol {\mu} _ {\boldsymbol {X}} = \left(\mathbb {E} \left[ X _ {1} \right], \dots , \mathbb {E} \left[ X _ {n} \right]\right) ^ {T}
$$

###2 La matrice di covarianza
La **matrice di covarianza**, $C _ { X } = \mathbb { E } \left[ \left( X - \mu _ { X } \right) \left( X - \mu _ { X } \right) ^ { T } \right]$, è definita come:

$$
\left( \begin{array}{c c c c} \sigma_ {X _ {1}} ^ {2} & \operatorname{COV} (X _ {1}, X _ {2}) & \dots & \operatorname{COV} (X _ {1}, X _ {n}) \\ \operatorname{COV} (X _ {2}, X _ {1}) & \sigma_ {X _ {1}} ^ {2} & \dots & \operatorname{COV} (X _ {2}, X _ {n}) \\ \dots & \dots & \dots & \dots \\ \operatorname{COV} (X _ {n}, X _ {1}) & \operatorname{COV} (X _ {n}, X _ {2}) & \dots & \sigma_ {X _ {n}} ^ {2} \end{array} \right)
$$

## Processi Stazionari in Senso Lato (SSL)

Focalizziamoci sui processi tempo discreti, ma quanto verrà detto vale anche per i processi tempo-continui. Abbiamo visto che un processo $X ( n ) \in { \mathcal { X } }$ è stazionario di ordine 2 se:

$$
\mathbb {P} \left\{X (n) = x \right\} = p _ {X} (x) \quad \forall \space x \text {e} \quad \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2} \right\} = \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2} \right\}
$$

Ovviamente la media $\begin{array} { r } { \mu _ { X } = \operatorname { \mathbb { E } } \left[ X ( n ) \right] = \sum _ { x \in \mathcal { X } } x p _ { X } ( x ) } \end{array}$ non dipende da $n ;$. Inoltre si noti che:

$$
\mathbb {E} \left[ X (n _ {1}) X (n _ {2}) \right] = \sum_ {x _ {1} \in \mathcal {X}} \sum_ {x _ {2} \in \mathcal {X}} x _ {1} x _ {2} \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2} \right\} =
$$
$$
\mathbb {E} \left[ X (n _ {1} + h) X (n _ {2} + h) \right] = \sum_ {x _ {1} \in \mathcal {X}} \sum_ {x _ {2} \in \mathcal {X}} x _ {1} x _ {2} \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2} \right\}
$$

Ciò significa che $\mathbb { E } \left[ X ( n _ { 1 } ) X ( n _ { 2 } ) \right]$ è funzione di $n _ { 2 } - n _ { 1 }$, ma non separatamente di $\boldsymbol { n } _ { 1 } \in \boldsymbol { n } _ { 2 }$.

Un processo $X ( n / t )$, continuo o discreto, non necessariamente stazionario al secondo ordine, si dice **stazionario in senso lato** se:

- La sua media non dipende dal tempo;
- La sua autocorrelazione soddisfa la condizione:

$$
R _ {X} \left(t _ {1} / n _ {1}, t _ {2} / n _ {2}\right) = \mathbb {E} \left[ X \left(t _ {1} / n _ {1}\right) X \left(t _ {2} / n _ {2}\right) \right] = R _ {X} \left(t _ {2} - t _ {1} / n _ {2} - n _ {1}\right)
$$

## Matrice di covarianza per processi SSL

Sia $X ( t / n )$ un processo SSL, continuo o discreto, e sia $\pmb { x } = [ X _ { 1 } , \ldots , X _ { M } ] ^ { T }$ un vettore aleatorio $M$-dimensionale di campioni di $X ( t / n )$, presi negli istanti $( t _ { 1 } , \dots , t _ { M } ) / ( n _ { 1 } , \dots , n _ { M } )$.

Ovviamente avremo che $\pmb { \mu } = \mathbb { E } \left[ \pmb { X } \right] = \mu \mathbf { 1 }$, con $\mu$ scalare e $1$ un vettore $M$-dimensionale di tutti $" \bf { 1 } ^ { \prime \prime }$.

Inoltre, avremo, per la condizione SSL:

$$
\mathbb {E} \left[ X _ {i} X _ {j} \right] = f (| i - j |) \quad \mathbb {E} \left[ X _ {i} ^ {2} \right] = \overline {{X ^ {2}}}, \operatorname{Var} (X _ {i}) = \overline {{X ^ {2}}} - \mu^ {2} = \sigma_ {X} ^ {2}
$$

Per cui, definendo $\begin{array} { r } { \rho _ { i , j } = \frac { \mathrm { C O V } ( X _ { i } , X _ { j } ) } { \sigma _ { X } ^ { 2 } } } \end{array}$ la matrice di covarianza assume la forma:

$$
\boldsymbol {C} _ {\boldsymbol {X}} = \sigma_ {\chi} ^ {2} \left( \begin{array}{c c c c c} 1 & \rho_ {1, 2} & \rho_ {1, 3} & \dots & \rho_ {1, M} \\ \rho_ {1, 2} & 1 & \rho_ {2, 3} & \dots & \rho_ {2, M} \\ \dots & \dots & \dots & \dots & \dots \\ \rho_ {1, M} & \rho_ {2, M} & \rho_ {3, M} & \dots & 1 \end{array} \right)
$$

Pertanto, la matrice di covarianza di un vettore tratto da un processo SSL è simmetrica.

> [!quote] Osservazione
> Se il passo di campionamento del processo è costante (cioè, $( t _ { i + 1 } - t _ { i } ) / ( n _ { i + 1 } - n _ { i } )$ costante $\forall \space i ,$), allora la matrice assume una forma di **Toeplitz**.

## Esercizio: La matrice di covarianza è sempre definita non-negativa

> [!example] Esercizio 1
> Si dimostri che la **matrice di covarianza** è una matrice definita non negativa.
>
> *Suggerimento: Considerare il prodotto scalare tra un vettore e la matrice applicato a un vettore arbitrario.*

Si ricorda che una matrice $A \in \mathbb{R}^{M \times M}$ è definita non negativa se, detto $x \in \mathbb{R}^M$ un qualunque vettore $M$-dimensionale risulta $x^T A x \geq 0$.

Consideriamo un vettore aleatorio $M$-dimensionale $X$ di media $\mu$ e matrice di covarianza $\Sigma$. La quantità $X^T \Sigma X$ è ovviamente una variabile aleatoria scalare con $\mathbb{E}[X^T \Sigma X] = \text{tr}(\Sigma \Sigma^T)$. Inoltre,

$$
\mathbb{E}[(X-\mu)^T \Sigma (X-\mu)] = \mathbb{E}[\sum_{i=1}^M \sum_{j=1}^M (X_i - \mu_i) \Sigma_{ij} (X_j - \mu_j)]
$$

Avremo allora la catena di disuguaglianze:

$$
\mathbb{E}[(X-\mu)^T \Sigma (X-\mu)] = \sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij} \mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)]
$$

$$
= \sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij} \Sigma_{ij} = \sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij}^2 \geq 0
$$

dove si è sfruttato il fatto che $\mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)] = \Sigma_{ij}$.

## Estensione ai processi continui: definizioni

Quanto detto sui processi ampiezza-discreti si estende ai processi ampiezza continui. Detto $X(t)$ tratto da un processo stazionario, la sua caratterizzazione implica l’assegnazione di una delle due funzioni:

$$
\mu(t) = \mathbb{E}[X(t)]
$$

$$
R(t_1, t_2) = \mathbb{E}[X(t_1)X(t_2)]
$$

dove $\mu(t)$ è la media e $R(t_1, t_2)$ è la funzione di autocorrelazione.

Ovviamente le definizioni di stazionarietà in senso lato e in senso stretto si estendono tal quali ai processi ampiezza continui.

## Un esempio: Processi Gaussiani

Un processo $X(t)$ si dice **Gaussiano** se un qualunque suo campione di dimensione $M$ definisce un vettore aleatorio $X$ Gaussiano.

Dato un vettore aleatorio $X$ con media e matrice di covarianza assegnati:

$$
\begin{cases} \mathbb{E}[X] = \mu \\ \text{Cov}(X) = \Sigma \end{cases}
$$

questo si dice Gaussiano se la sua pdf si scrive nella forma

$$
f(x) = \frac{1}{\sqrt{(2\pi)^M |\Sigma|}} \exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)\right)
$$

dove $|\Sigma|$ denota il determinante della matrice di covarianza.

## Proprietà dei processi Gaussiani

- La stazionarietà in senso lato implica quella in senso stretto. Si verifichi questo asserto ricordando che nel caso di stazionarietà in senso lato la matrice di covarianza ha struttura **Toeplitz**.
- Chiusura rispetto a trasformazioni lineari. Se $X$ è un vettore Gaussiano, $X \sim \mathcal{N}(\mu, \Sigma)$, allora, avremo

$$
AX + b \sim \mathcal{N}(A\mu + b, A\Sigma A^T)
$$

- Per un processo Gaussiano, incorrelazione implica indipendenza. Infatti, un processo incorrelato ha matrice di covarianza $\Sigma = \text{diag}(\sigma_1^2, \dots, \sigma_M^2)$. Sostituendo nella espressione di una pdf Gaussiana abbiamo

$$
f(x) = \prod_{i=1}^M \frac{1}{\sqrt{2\pi\sigma_i^2}} \exp\left(-\frac{(x_i-\mu_i)^2}{2\sigma_i^2}\right)
$$

## Tipi di convergenza

Sia $X_n$ una successione di variabili aleatorie con densità $f_n(x)$. Ci chiediamo come definire la convergenza di tale successione a un dato limite, sia esso $X$.

Ovviamente la forma più forte di convergenza è quella puntuale, vale a dire - ricordando che le variabili aleatorie sono in realtà funzioni - $P(\lim_{n \to \infty} X_n = X) = 1$, dove $\Omega$ lo spazio dei campioni dello spazio di probabilità sottostante.

Altre forme di convergenza più ”deboli” (con diversa gradazione) sono:
- La convergenza in distribuzione;
- La convergenza in probabilità;
- La convergenza in media quadratica;
- La convergenza quasi certa (o con probabilità 1).

## Convergenza in distribuzione

La successione $X_n$ si dice convergente in distribuzione alla variabile $X$ (e si scrive $X_n \xrightarrow{d} X$) se

$$
\lim_{n \to \infty} F_n(x) = F(x)
$$

dove l’uguaglianza vale in tutti gli insiemi di continuità di $F(x)$.

> [!theorem] Teorema (*Continuous Mapping*)
> Se $g$ è una funzione continua, allora si ha:
>
> $$
> X_n \xrightarrow{d} X \implies g(X_n) \xrightarrow{d} g(X)
> $$

> [!theorem] Teorema (*Continuità di Levy*)
> Definendo la funzione generatrice dei momenti (moment generating function, mgf)
>
> $$
> M_X(s) = \mathbb{E}[e^{sX}]
> $$
>
> per i valori di $s$ per cui l’integrale esiste, la convergenza puntuale di $M_{X_n}(s)$ a $M_X(s)$ implica $X_n \xrightarrow{d} X$ e viceversa.

## La funzione generatrice dei momenti

La **funzione generatrice dei momenti** (moment generating function, mgf) di una variabile aleatoria gode di alcune rilevanti proprietà. 

> [!quote] Proprietà di continuità
> Si nota che 
>
> $$
> \Phi_ {X} (s) = \int_ {\mathbb {R}} e ^ {s t} f _ {X} (t) d t, \text {   con   } f _ {X} \text {   sommabile }
> $$
>
> è funzione continua di $s$ nei punti in cui l’integrale esiste. 

Analogamente, si può facilmente verificare che: 

> [!theorem] Derivabilità della mgf
> Purché i momenti di ordine $r$ esistano, vale:
>
> $$
> \Phi_ {X} (0) = 1 \quad \Phi^ {\prime} (0) = \mathbb {E} [ X ] \quad \Phi_ {X} ^ {\prime \prime} (0) = \mathbb {E} [ X ^ {2} ] \dots \Phi_ {X} ^ {(r)} (0) = \mathbb {E} [ X ^ {r} ]
> $$

Pertanto, nelle condizioni precedenti, la mgf ammette il seguente sviluppo in serie di **MacLaurin**:

> [!example] Sviluppo in serie della mgf
> $$
> \Phi_ {X} (s) = \sum_ {n = 0} ^ {\infty} \frac {\mathbb {E} [ X ^ {n} ]}{n !} s ^ {n}
> $$
>
> Questo sviluppo spiega la denominazione di "mgf" (moment generating function), poiché i coefficienti della serie sono direttamente correlati ai momenti della variabile aleatoria.

---

# Elementi di Statistica inferenziale

## Alcune Definizioni

Assumiamo di avere un campione di dimensione $n$, diciamo $\pmb { x } \in \mathbb { R } ^ { n }$. 

Assumiamo che questo campione sia il risultato di un esperimento casuale, il che significa che il ri-campionamento porterebbe a un set di risultati differente, diciamo $\pmb { x } ^ { \prime } \in \mathbb { R } ^ { n }$.

> [!theorem] Inferenza Statistica
> **Inferenza statistica** è il processo di utilizzo dell'analisi dei dati per dedurre proprietà di una distribuzione di probabilità sottostante, ovvero definire una legge che qualsiasi campione — estratto casualmente — dovrebbe rispettare.
> 
> La statistica inferenziale può essere contrapposta alla **statistica descrittiva**. Quest'ultima si occupa esclusivamente delle proprietà dei dati osservati e non si basa sull'assunzione che i dati provengano da una popolazione più ampia.
> 
> Gli obiettivi di base dell'inferenza statistica sono:
> 1. Test delle Ipotesi.
> 2. Stima dei Parametri.

## Un esempio: la media campionaria

Assumiamo di avere un set di dati $\pmb { x } ^ { n } \in \mathcal { X } ^ { n } \subseteq \mathbb { R } ^ { n }$. 

Sappiamo che la **media campionaria** è definita come 

$$
\overline {{x}} _ {n} = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i}
$$

La **Legge dei Grandi Numeri** ci dice che ${ \overline { { X } } } _ { n } \to \mathbb { E } [ X ]$ (il tipo di convergenza dipende dalla legge statistica sottostante), nel senso che, denotando $X ^ { n }$ un campione casuale estratto dalla popolazione, abbiamo 

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} \to \mathbb {E} [ X ]
$$

> [!quote] Osservazione
> La **convergenza debole** (cioè, convergenza in probabilità) ci dice che la frequenza dei campioni la cui media campionaria si discosta significativamente da $\mathbb { E } [ X ]$ è piccola quanto desideriamo; 
> 
> La **convergenza forte** afferma che nel limite la probabilità di discostarsi da $\mathbb { E } [ X ]$ è zero; 
> 
> La **convergenza in media quadratica** (Mean-Square) afferma che 
> 
> $$
\lim _ {n} \mathbb {E} \left[ \left(\overline {{X}} _ {n} - \mathbb {E} [ X ]\right) ^ {2} \right] = 0
> $$

## La media campionaria - cont.

Assumiamo che $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$, con $\mathcal { X } = ( a _ { 1 } , \dotsc , a _ { M } )$ discreto e finito; 

sappiamo che 

$$
\overline {{x}} _ {n} = \sum_ {i = 1} ^ {M} a _ {i} f _ {n} (a _ {i})
$$

dove $f _ { n } ( a _ { i } )$ è la frazione dei valori del campione che producono $a _ { j }$. 

Sappiamo che, se $\boldsymbol { x } \in \mathcal { X }$ è una variabile casuale con pmf $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$, allora: 

$$
\mathbb {E} [ X ] = \sum_ {i = 1} ^ {M} a _ {i} p _ {X} (a _ {i})
$$

Di conseguenza, abbiamo 

$$
| \overline {{x}} _ {n} - \mathbb {E} [ X ] | \leq \sum_ {i = 1} ^ {M} | a _ {i} | | f _ {n} (a _ {i}) - p _ {X} (a _ {i}) |
$$

> [!quote] Osservazione
> Si noti che se possiamo affermare che $f _ { n } ( a _ { i } ) \to p \chi ( a _ { i } )$ (in qualche senso), allora possiamo inferire che $\pmb { x } ^ { n }$ è un campione da una popolazione i cui elementi sono estratti da un vettore casuale $X ^ { n }$ con densità marginale $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$.

## La distribuzione empirica

Assumiamo che $\pmb { x } ^ { n }$ sia estratto da $X ^ { n }$, un set di $n$ variabili casuali iid con marginale sconosciuto $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$. 

La frequenza di occorrenza dell'evento $X _ { k } = a _ { i }$ è essa stessa casuale. Se $N _ { j }$ è il numero di volte in cui $X _ { k } = a _ { i }$ nel nostro campione $n$-dimensionale, abbiamo: 

$$
\operatorname * {P r} \left\{N _ {i} = k \right\} = \binom{n}{k} p _ {X} (a _ {i}) ^ {k} \left[ 1 - p _ {X} (a _ {i}) \right] ^ {n - k}
$$

Poiché 

$$
\mathbb {E} \left[ \frac {N _ {i}}{n} \right] = p _ {X} (a _ {i}), \quad \text { var } \left[ \frac {N _ {i}}{n} \right] = \frac {p _ {X} (a _ {i}) (1 - p _ {X} (a _ {i}))}{n}
$$

abbiamo che $\begin{array} { r } { \frac { N _ { i } } { n }  p _ { X } ( a _ { i } ) } \end{array}$ in media quadratica, cioè: 

$$
\lim _ {n \rightarrow \infty} \mathbb {E} \left[\left(\frac {N _ {i}}{n} - p _ {X} (a _ {i})\right) ^ {2} \right] = 0
$$

## Convergenza quasi certa

Assumiamo che $\{ q ( a _ { i } ) \}$ sia qualsiasi altra pmf su $\mathcal { X }$ differente dalla vera distribuzione $p _ { X } { \left( a _ { i } \right) }$ in almeno due elementi. Abbiamo: 

$$
\operatorname * {P r} \left\{N _ {i} = n q (a _ {i}) \right\} = \binom{n}{n q (a _ {i})} p _ {X} (a _ {i}) ^ {n q (a _ {i})} \left[ 1 - p _ {X} (a _ {i}) \right] ^ {n (1 - q (a _ {i}))}
$$

Utilizzando il limite 

$$
\sqrt {\frac {n}{8 k (n - k)}} \leq \binom{n}{k} 2 ^ {- n H \left(\frac {k}{n}\right)} \leq \sqrt {\frac {n}{\pi k (n - k)}}
$$

abbiamo, impostando $k = n q ( a _ { i } )$ 

$$
\begin{array}{c} \sqrt {\frac {1}{8 n q (a _ {i}) (1 - q (a _ {i}))}} \leq \binom{n}{n q (a _ {i})} 2 ^ {- n \left[ q (a _ {i}) \log \frac {1}{q (a _ {i})} + (1 - q (a _ {i})) \log \frac {1}{1 - q (a _ {i})} \right]} \\ \leq \sqrt {\frac {1}{\pi n q (a _ {i}) (1 - q (a _ {i}))}} \end{array}
$$

abbiamo, per $n$ crescentemente grandi: 

$$
\binom{n}{n q (a _ {i})} \sim 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))}
$$

## Convergenza quasi certa - cont.

Consideriamo ora un valore $a _ { j }$ per il quale $q ( a _ { i } ) \neq p _ { X } ( a _ { i } )$ 

Quando $n$ diventa grande abbiamo: 

$$
\begin{array}{r l} \operatorname * {P r} \big \{N _ {i} = n q (a _ {i}) \big \} & \sim 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} p _ {X} (a _ {i}) ^ {n q (a _ {i})} \left[ 1 - p _ {X} (a _ {i}) \right] ^ {n (1 - q (a _ {i}))} \\ & = 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} 2 ^ {n [ q (a _ {i}) \log p _ {X} (a _ {i}) + (1 - q (a _ {i})) \log (1 - p _ {X} (a _ {i})) ]} \\ & = 2 ^ {n \left[ q (a _ {i}) \log \frac {p _ {X} (a _ {i})}{q (a _ {i})} + (1 - q (a _ {i})) \log \frac {1 - p _ {X} (a _ {i})}{1 - q (a _ {i})} \right]} = 2 ^ {- n D _ {i}} \end{array}
$$

con 

$$
D _ {i} = q (a _ {i}) \log \frac {q (a _ {i})}{p _ {X} (a _ {i})} + [ 1 - q (a _ {i}) ] \log \frac {1 - q (a _ {i})}{1 - p _ {X} (a _ {i})} > 0
$$

Concludiamo quindi che la probabilità che la frequenza di occorrenza non sia uguale alla vera probabilità tende a zero esponenzialmente con $n$. 

Ciò implica che $f _ { n } ( a _ { i } ) \to p \chi ( a _ { i } )$ quasi certamente.

## Commenti

Si consideri un campione $\mathbf{x}$ $\pmb { x } ^ { n } \in \mathcal { X } ^ { n } , \mathcal { X } = \{ a _ { 1 } , . . . , a _ { M } \}$ estratto da un vettore casuale $\mathbf{X}$ $X ^ { n }$ di **pmf** (Probability Mass Function) sconosciuta.

Se si calcolano le frequenze di occorrenza:

$$
f _ {n} (a _ {i}) = \frac {\# \text {   of   elements   equal   to   } a _ {i}}{n}, \qquad i = 1, \ldots , M
$$

si ottengono:

$$
\operatorname * {P r} \left\{\lim _ {n \rightarrow \infty} \frac {N _ {i}}{n} = \lim _ {n \rightarrow \infty} f _ {n} (a _ {i}) \right\} = 1
$$

Ciò implica che qualsiasi altro campione, ad esempio $\mathbf{y}$ $\pmb { y } ^ { n }$, estratto dalla stessa popolazione mostrerà, per $n \to \infty$ $n  \infty$, lo stesso comportamento statistico. 

Non è necessario specificare che per ogni funzione $f$ $f ( \cdot )$ dei dati:

$$
\operatorname * {P r} \left\{\lim _ {n \rightarrow \infty} f (\boldsymbol {X} ^ {n}) = \lim _ {n \rightarrow \infty} f (\boldsymbol {x} ^ {n}) \right\} = 1
$$

di conseguenza, la media campionaria converge con probabilità uno alla media statistica della popolazione. Questa proprietà è definita nelle statistiche inferenziali come **forte coerenza**.

> [!theorem] Forte Coerenza
> In statistica, un estimatore è forte coerente se converge quasi certamente (con probabilità 1) al valore vero del parametro che intende stimare all'aumentare della dimensione del campione.

## Statistiche Inferenziali

L'idea principale risiede nel fatto che, una volta osservato un campione sufficientemente ampio di una data popolazione di dati, è possibile inferire un numero di caratteristiche che qualsiasi altro campione dovrebbe rispettare.

Alcune conoscenze pregresse riguardo alle statistiche della popolazione da cui il campione è estratto possono essere note a priori; ad esempio, si può assumere che il campione sia estratto da una popolazione la cui distribuzione è nota fino a un insieme di parametri.

Per iniziare, si assume che il campione sia noto come estratto da una famiglia di distribuzioni, indicizzata da un parametro $\theta$ $\theta$, che deve essere stimato.

**Domanda:** Come elaboriamo il dataset disponibile per inferire il valore del parametro?

## Impostazione Bayesiana: Regola di decisione

Si assuma di avere un dataset $\mathbf{x}$ $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ che è una realizzazione di un vettore casuale $\mathbf{X}$ $X ^ { n }$. Si assuma che, in base allo stato della natura, i dati possano provenire da una qualsiasi delle $K$ $M$ diverse leggi di probabilità.

Abbiamo quindi un insieme di $K$ $M$ ipotesi diverse e mutuamente esclusive $\omega_k \in \Omega$ $\{ H _ { i } \} _ { i = 1 } ^ { M }$, ciascuna delle quali definisce una diversa legge condizionale per il set di dati, ovvero:

$$
p _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {x} ^ {n} \mid H _ {i}\right), \quad i = 1, \dots , M
$$

Si assuma che il vettore casuale $\mathbf{x}$ $X ^ { n }$ sia estratto da una famiglia di distribuzioni con pmf $p(\mathbf{x}|\theta)$ $p _ { X ^ { n } | \Theta } ( { \pmb x } ^ { n } | \theta )$, dove il valore di $\theta$ $\theta$ è sconosciuto. Si assuma inoltre che le probabilità a priori $P(\omega_k)$ $\{ p ( H _ { i } ) \} _ { i = 1 } ^ { M }$ di questi stati della natura siano assegnate.

Una **regola di decisione** è una mappa:

$$
D: \mathbf {x} ^ {n} \in \mathcal {X} ^ {n} \Longrightarrow D (\mathbf {x} ^ {n}) \in \{1, \dots , M \}
$$

che permette di decidere quale dei possibili stati della natura sia quello effettivamente in vigore.

## Costi Bayesiani

Si definisca la seguente matrice di costo $C$ $M \times M$:

$$
\boldsymbol {C} = \left[ \begin{array}{c c c c} C _ {1, 1} & C _ {1, 2} & \ldots & C _ {1, M} \\ \ldots & \ldots & \ldots & \ldots \\ C _ {M, 1} & C _ {M, 2} & \ldots & C _ {M, M} \end{array} \right]
$$

dove $C(\omega_k, a_j)$ $C _ { i , j }$ è il costo associato all'evento in cui si prende la decisione $a_j$ $D ( \pmb { x } ^ { n } ) = i$ mentre lo stato della natura è $\omega_k$ $H _ { j }$.

Si definisce il **rischio Bayesiano medio** come:

$$
\mathcal {R} = \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {M} C _ {i, j} \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = i, H = H _ {j} \right\}
$$

Data una matrice di costo $C$ $C$, una regola di decisione ottimale è una mappa $\delta$ $D ( \pmb { x } ^ { n } )$ che minimizza il rischio Bayesiano.

> [!quote] Osservazione
> Se $C(\omega_k, a_j) = 0$ per $j=k$ e $C(\omega_k, a_j) = 1$ per $j \neq k$, allora
>
> $$
> R = \sum_{k=1}^K P(\omega_k) \sum_{j=1}^K P(a_j|\omega_k) C(\omega_k, a_j)
> $$
>
> ovvero il rischio Bayesiano medio coincide con la probabilità di commettere un errore di classificazione.

## Problema di Classificazione Binaria

Si assuma per il momento che $K=2$, che $\omega_1$ e $\omega_2$ $C _ { 1 , 1 } = C _ { 2 , 2 } = 0$ e $C _ { 1 , 2 } = C _ { 2 , 1 } = 1$ in modo che:

$$
\mathcal {R} = \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 2, H _ {1} \right\} + \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 1, H _ {2} \right\} = \mathbb {P} (e)
$$

Progettare una regola di decisione implica determinare una partizione di $\mathcal{X}$ $\mathcal { X } ^ { n }$ in due sottoinsiemi, $R_1$ $\Omega _ { 1 }$ e $R_2$ $\Omega _ { 2 }$, tali che:

$$
D (\boldsymbol {x} ^ {n}) = \left\{ \begin{array}{l l} 1 & \text { if } \boldsymbol {x} ^ {n} \in \Omega_ {1} \\ 2 & \text { if } \boldsymbol {x} ^ {n} \in \Omega_ {2} \end{array} \right.
$$

La corrispondente probabilità di errore è quindi scritta come:

$$
\mathbb {P} (e) = \mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {1}, H _ {2} \right\} + \mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {2}, H _ {1} \right\}
$$

L'obiettivo è determinare la legge di decisione ottimale (ovvero con la minima probabilità di errore) per questo problema di classificazione binaria.

# Classificazione Binaria: leggi di dati discreti

Assumiamo che le osservazioni $X ^ { n }$ siano un **vettore casuale discreto** con pmf condizionali dati $p { \pmb X } ^ { m } \big ( { \pmb x } ^ { n } | H _ { i } \big )$.

Abbiamo ovviamente $\begin{array} { r } { \mathbb { P } \left\{ \pmb { X } ^ { n } \in \Omega _ { i } , H _ { j } \right\} = \pmb { 1 } - \sum _ { \pmb { x } ^ { n } \in \Omega _ { i } } p ( H _ { i } ) \mathbb { P } \left\{ \pmb { X } ^ { n } = \pmb { x } ^ { n } | H _ { i } \right\} } \end{array}$ dove la probabilità di errore è scritta come

$$
\mathbb {P} (e) = 1 - \left[ \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {1}} p \left(H _ {1}\right) \mathbb {P} \left\{\boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \mid H _ {1} \right\} + \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {2}} p \left(H _ {2}\right) \mathbb {P} \left\{\boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \mid H _ {2} \right\} \right]
$$

che è minima quando la quantità tra parentesi è massima. Otteniamo quindi la seguente regola di decisione ottimale:

$$
\boldsymbol {x} ^ {n} \in \Omega_ {i} \text {   iff   } p _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) P (H _ {1}) > p _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2}) P (H _ {2})
$$

o equivalentemente

$$
L (\boldsymbol {x} ^ {n}) = \frac {p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {1})}{p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {2})} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} \frac {P (H _ {2})}{P (H _ {1})} = \eta
$$

> [!quote] Osservazione
> La quantità $L ( \pmb { x } ^ { n } )$ sul lato sinistro (LHS) è chiamata **rapporto di verosimiglianza** tra le due ipotesi alternative.

## Alcuni commenti

La precedente regola di decisione è nota anche come regola di decisione a **Massima Probabilità a Posteriori** (MAP), in quanto, per la legge di Bayes:

$$
\mathbb {P} \left\{H = H _ {i} | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right\} = \frac {\mathbb {P} \left\{\boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \mid H _ {i} \right\} P (H _ {i})}{\mathbb {P} \left\{\boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right\}} = \frac {p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} \mid H _ {i}) P (H _ {i})}{p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})}
$$

mostrando che la regola decide per l'ipotesi la cui probabilità a posteriori dati i dati osservati è massima.

Nel caso speciale in cui le due ipotesi siano ugualmente probabili, la soglia è $\eta = 1$ e la regola di decisione diventa una regola di decisione a **Massima Verosimiglianza** (ML).

Poiché le probabilità di errore condizionali sono:

$$
P (e | H _ {1}) = \mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) <   \eta | H _ {1} \right\} \quad P (e | H _ {2}) = \mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) > \eta | H _ {2} \right\}
$$

la probabilità di errore è

$$
\mathbb {P} (e) = P \left(H _ {1}\right) P \left(e \mid H _ {1}\right) + P \left(H _ {2}\right) P \left(e \mid H _ {2}\right)
$$

## Esempio: classificazione di sorgenti binarie

> [!example] Esempio 1 (Classificazione di sorgenti binarie)
> Assumiamo che le osservazioni siano variabili binarie iid che possono provenire con probabilità uguali da una sorgente con ${ \mathbb { P } } \left\{ X _ { i } = 1 \right\} = p _ { 1 }$ o da una sorgente con ${ \mathbb { P } } \left\{ X _ { i } = 1 \right\} = p _ { 2 }$, con $p _ { 1 } > p _ { 2 }$.
>
> Abbiamo quindi:
>
> $$
> p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {i}) = p _ {i} ^ {w _ {H} (\boldsymbol {x} ^ {n})} (1 - p _ {i}) ^ {n - w _ {H} (\boldsymbol {x} ^ {n})}
> $$
>
> dove $w _ { H } ( \pmb { x } ^ { n } )$ è il **peso di Hamming** della sequenza binaria osservata $\pmb { x } ^ { n }$ coincidente con il numero dei suoi 1.
>
> Il test di probabilità di errore minima è
>
> $$
> \left(\frac {p _ {1}}{p _ {2}}\right) ^ {w _ {H} (x ^ {n})} \left[ \frac {(1 - p _ {1})}{(1 - p _ {2})} \right] ^ {n - w _ {H} (x ^ {n})} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 1
> $$
>
> o, equivalentemente
>
> $$
> w _ {H} (\boldsymbol {x} ^ {n}) \ln \left(\frac {p _ {1}}{p _ {2}}\right) + (n - w _ {H} (\boldsymbol {x} ^ {n})) \ln \left(\frac {1 - p _ {1}}{1 - p _ {2}}\right) \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 0
> $$
>
> che si riduce a
>
> $$
> w _ {H} \big (\boldsymbol {x} ^ {n} \big) \left[ \ln \left(\frac {p _ {1}}{1 - p _ {1}} \frac {1 - p _ {2}}{p _ {2}}\right) \right] \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} n \ln \left(\frac {1 - p _ {2}}{1 - p _ {1}}\right)
> $$

## Valutazione delle prestazioni

Si noti che, poiché $p _ { 1 } > p _ { 2 }$, tutti i logaritmi sono non negativi; il test può quindi essere riscritto nella forma

$$
w _ {H} (x ^ {n}) \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} n \frac {\ln \left(\frac {1 - p _ {2}}{1 - p _ {1}}\right)}{\ln \left(\frac {p _ {1}}{1 - p _ {1}} \frac {1 - p _ {2}}{p _ {2}}\right)} = \eta_ {1}
$$

Assumendo che $\eta _ { 1 }$ non sia intero, le probabilità di errore condizionali sotto le due ipotesi alternative sono scritte come:

$$
\mathbb {P} (e | H _ {1}) = \mathbb {P} \left\{  w _ {H} (\boldsymbol {X} ^ {n}) <   \eta_ {1}   |   H _ {1} \right\} = \sum_ {i = 0} ^ {\lfloor \eta_ {1} \rfloor} \binom{n}{i} p _ {1} ^ {i} (1 - p _ {1}) ^ {n - i}
$$

$$
\mathbb {P} (e | H _ {2}) = \mathbb {P} \left\{w _ {H} (\boldsymbol {X} ^ {n}) > \eta_ {1} | H _ {2} \right\} = \sum_ {i = \lfloor \eta_ {1} \rfloor + 1} ^ {n} \binom{n}{i} p _ {2} ^ {i} (1 - p _ {2}) ^ {n - i}
$$

dove la probabilità di errore letta è

$$
\mathbb {P} (e) = \frac {1}{2} \mathbb {P} (e | H _ {1}) + \frac {1}{2} \mathbb {P} (e | H _ {2})
$$

## Classificazione binaria: legge dei dati continui

Assumiamo ora che i dati possano essere estratti da $M$ possibili leggi di probabilità continue, dove ci viene fornito un insieme di funzioni di densità di probabilità condizionali candidate $\{ f _ { \pmb { X } ^ { n } | H _ { i } } ( \pmb { x } ^ { n } | \pmb { H } _ { i } ) \} _ { i = 1 } ^ { M }$. L'unica differenza con il caso discreto è che ora

$$
\mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {1} | H _ {1} \right\} = \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {1}} \left(\boldsymbol {x} ^ {n} | H _ {1}\right) d \boldsymbol {x} ^ {n} \quad \mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {2} | H _ {2} \right\} = \int_ {\Omega_ {2}} f _ {\boldsymbol {X} ^ {n} | H _ {2}} \left(\boldsymbol {x} ^ {n} | H _ {2}\right) d \boldsymbol {x} ^ {n}
$$

Pertanto, seguendo la stessa linea di pensiero del caso discreto, otteniamo che il test di probabilità di errore minima è scritto come

$$
\boldsymbol {x} ^ {n} \in \Omega_ {i} \text {   iff   } f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) P (H _ {1}) > f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {2}) P (H _ {2})
$$

o equivalentemente

$$
L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2})} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} \frac {P (H _ {2})}{P (H _ {1})} = \eta
$$

La quantità $L ( \pmb { x } ^ { n } )$ sul lato sinistro (LHS) è di nuovo chiamata **rapporto di verosimiglianza** tra le due ipotesi alternative.

## Esempio: test della media di una popolazione Gaussiana

> [!example] Esempio 2 (Test della media di una popolazione Gaussiana)
> Assumiamo che il set di dati $\pmb { x } ^ { n }$ abbia la stessa probabilità di essere una realizzazione di un vettore casuale Gaussiano indipendente i cui elementi hanno la stessa varianza e medie diverse $\mu _ { 1 }$ e $\mu _ { 2 } < \mu _ { 1 }$.
>
> Poiché $\begin{array} { r } { f _ { X ^ { n } | H _ { i } } ( x ^ { n } | H _ { i } ) = \prod _ { k = 1 } ^ { n } \frac { 1 } { \sqrt { 2 \pi \sigma ^ { 2 } } } e ^ { - \frac { ( x _ { k } - \mu _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } } } \end{array}$ il test ottimo è scritto come
>
> $$
> L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2})} = e ^ {\frac {\sum_ {k = 1} ^ {n} (x _ {k} - \mu_ {2}) ^ {2} - (x _ {k} - \mu_ {1}) ^ {2}}{2 \sigma^ {2}}} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 1
> $$
>
> Prendendo il logaritmo su entrambi i lati ed elaborando otteniamo il test equivalente
>
> $$
> \frac {1}{n} \sum_ {k = 1} ^ {n} x _ {k} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} \frac {\mu_ {1} + \mu_ {2}}{2} = \eta
> $$
>
> Le quantità $\sum x _ { k }$ per questo problema e $w _ { H } ( \pmb x ^ { n } )$ per il precedente sono anche riferite come **statistiche sufficienti** nel linguaggio della statistica inferenziale.

## Valutazione delle prestazioni

Si noti che, sotto $H _ { j }$, la statistica del test $\begin{array} { r } { Z _ { n } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } X _ { i } } \end{array}$ è Gaussiana con media e varianza date da:

$$
\mathbb {E} [ Z _ {n} | H _ {i} ] = \mu_ {i} \quad \sigma_ {Z _ {n}} ^ {2} = \frac {\sigma^ {2}}{n} \quad w h y?
$$

Di conseguenza le probabilità di errore condizionali sono 

$$
\mathbb {P} (e | H _ {1}) = \mathbb {P} \left\{Z _ {n} <   \eta | H _ {1} \right\} = 1 - Q \left(\frac {\eta - \mu_ {1}}{\sigma_ {Z _ {n}}}\right) = 1 - Q \left(\sqrt {n} \frac {\mu_ {2} - \mu_ {1}}{2 \sigma}\right)
$$

$$
\mathbb {P} (e | H _ {2}) = \mathbb {P} \left\{Z _ {n} > \eta | H _ {2} \right\} = Q \left(\frac {\eta - \mu_ {2}}{\sigma_ {Z _ {n}}}\right) = Q \left(\sqrt {n} \frac {\mu_ {1} - \mu_ {2}}{2 \sigma}\right)
$$

Poiché $\mu _ { 1 } - \mu _ { 2 } > 0$, abbiamo anche $\mathbb { P } ( e | H _ { 1 } ) = \mathbb { P } ( e | H _ { 2 } ) = Q \left( { \sqrt { n } } { \frac { \mu _ { 1 } - \mu _ { 2 } } { 2 \sigma } } \right)$, dove 

$$
\mathbb {P} (e) = Q \left(\sqrt {n} \frac {\mu_ {1} - \mu_ {2}}{2 \sigma}\right)\rightarrow 0 \quad \text { as } n \rightarrow \infty
$$

## Test di ipotesi: introduzione

Esistono numerose situazioni in cui è necessario prendere una decisione tra due ipotesi, pur non disponendo dei mezzi per assegnare la matrice di costo $C$ né le probabilità a priori. 

Gli esempi includono diverse situazioni di interesse pratico, quali: 
- Rilevamento precoce di minacce alla sicurezza di un'area pattugliata; 
- Rilevamento di intrusioni in server/domini protetti su internet; 
- Rilevamento (e localizzazione) di ostacoli nei sistemi **Advance Driver Assistance Systems** (ADAS); 
- Controllo del traffico aereo; 
- Innumerevoli applicazioni militari.

In tutte le situazioni sopra citate, risulta praticamente impossibile assegnare un costo a un errore di giudizio sullo "stato della natura", ovvero a una decisione errata tra le due ipotesi "tutto normale" o "qualcosa sta accadendo". È inoltre di poca importanza assegnare una probabilità a priori che "anomalie statistiche" siano presenti nel set di dati.

## Definizioni nel test di ipotesi

> [!theorem] Ipotesi Nulla ($H_0$)
> L'**ipotesi nulla**, tradizionalmente denotata $H _ { 0 }$, è l'assunzione di base che il set di dati osservati $\pmb { x } ^ { n }$ sia una realizzazione di un vettore casuale con una distribuzione condizionale nota, con pmf/pdf $p _ { X ^ { n } | H _ { 0 } } ( { \pmb x } ^ { n } | H _ { 0 } ) / f _ { { \pmb X } ^ { n } | H _ { 0 } } ( { \pmb x } ^ { n } | H _ { 0 } )$.

Vogliamo decidere se o meno, dati i dati osservati $\pmb { x } ^ { n }$, l'ipotesi nulla debba essere rifiutata a favore di una legge diversa, diciamo $p _ { X ^ { n } \mid H _ { 1 } } ( { \pmb x } ^ { n } | H _ { 1 } ) / f _ { { \pmb X } ^ { n } \mid H _ { 1 } } ( { \pmb x } ^ { n } | H _ { 1 } )$. Per quanto riguarda la classificazione binaria, è necessario partizionare il dominio $\mathcal { X } ^ { n }$ in due regioni di decisione; tuttavia, il precedente framework di Bayes non è applicabile in questo contesto a causa della mancanza di informazioni a priori sufficienti.

Nel progettare una regola di decisione (ovvero, un test), si definiscono i seguenti parametri:

> [!theorem] Errore di tipo-I
> L'**errore di tipo-I** del test, o probabilità di falso allarme, è definito come:
> 
> $$
> \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 1 | H _ {0} \right\} = \left\{ \begin{array}{l l} \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0}) d \boldsymbol {x} ^ {n} & \text { Continuous   Data } \\ \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {1}} p _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0}) & \text { Discrete   Data } \end{array} \right.
> $$

> [!theorem] Potenza del test
> La **potenza del test** rappresenta la capacità del test di rifiutare correttamente l'ipotesi nulla quando essa è falsa ed è definita come:
> 
> $$
> 1 - \beta = \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 1 | H _ {1} \right\} = \left\{ \begin{array}{l l} \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) d \boldsymbol {x} ^ {n} \\ \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {1}} p _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) \end{array} \right.
> $$

### Dati Continui
### Dati Discreti

## Test di Neyman-Pearson

Dato il framework delineato precedentemente, un test di Neyman-Pearson è il risultato della seguente ottimizzazione vincolata:

$$
\text { Determine } \Omega_ {1} \colon \left\{ \begin{array}{l l} 1 - \beta & \text { maximum } \\ \text { subject   to } & \text { type - 1   error } \leq \alpha \end{array} \right.
$$

L'esistenza della soluzione di tale problema vincolato costituisce il nucleo del **Lemma di Neyman-Pearson**. Il test risultante è il test del rapporto di verosimiglianza (*likelihood ratio test*):

$$
L \left(\boldsymbol {x} ^ {n}\right) \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta L \left(\boldsymbol {x} ^ {n}\right) = \left\{ \begin{array}{l l} \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (x ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {0}} (x ^ {n} | H _ {0})} & \text { Continuous   data } \\ \frac {p _ {\boldsymbol {X} ^ {n} | H _ {1}} (x ^ {n} | H _ {1})}{p _ {\boldsymbol {X} ^ {n} | H _ {0}} (x ^ {n} | H _ {0})} & \text { Discrete   data } \end{array} \right.
$$

La soglia $\eta$ dovrebbe essere scelta come soluzione dell'equazione:

$$
\mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) > \eta | H _ {0} \right\} = \alpha
$$

> [!quote] Osservazione
> L'applicazione di qualsiasi funzione monotonicamente crescente a entrambi i lati del test precedente non ne altera l'ottimalità. Pertanto, è possibile introdurre equivalentemente il log-likelihood $\ln$ $L \left( \pmb { x } ^ { n } \right) = \Lambda ( \pmb { x } ^ { n } )$ e confrontarlo con una soglia determinata in modo nuovo.

## Esempio: test della media di una popolazione Gaussiana

Assumiamo che l'ipotesi nulla sia che le osservazioni siano iid Gaussiane con media zero e varianza data, ovvero $X _ { i } \sim \mathcal { N } ( 0 , \sigma ^ { 2 } )$, mentre la sua alternativa è $X _ { i } \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$.

Seguendo la slide 18, il test del rapporto di verosimiglianza si legge:

$$
L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0})} = e ^ {\frac {\sum_ {k = 1} ^ {n} (x _ {k} - \mu) ^ {2} - x _ {k} ^ {2}}{2 \sigma^ {2}}} \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta
$$

dove $\eta$ deve essere scelto in modo da soddisfare il vincolo. Prendendo il logaritmo su entrambi i lati, semplificando e assorbendo in una nuova soglia (sconosciuta) $\eta ^ { \prime }$ tutte le quantità indipendenti dai dati, si ottiene il test equivalente:

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta^ {\prime}
$$

dove $\eta ^ { \prime }$ deve essere scelto in modo da garantire che la probabilità di errore di tipo-I sia uguale al valore di progetto $\alpha$.

## Prestazioni del test

Dobbiamo prima impostare la soglia di rilevamento. Si noti che la statistica del test, sotto $H _ { 0 }$, è Gaussiana con media zero e varianza $\frac { \sigma ^ { 2 } } { n }$ (vedere slide 18). Di conseguenza:

$$
\mathbb {P} \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} > \eta^ {\prime} | H _ {0} \right\} = Q \left(\frac {\sqrt {n} \eta^ {\prime}}{\sigma}\right) = \alpha \Longrightarrow \eta^ {\prime} = \frac {\sigma}{\sqrt {n}} Q ^ {- 1} (\alpha)
$$

Per valutare la potenza del test, notiamo che, sotto $H _ { 1 }$, la statistica del test è Gaussiana con media $\mu$ e varianza $\frac { \sigma ^ { 2 } } { n }$, per cui:

$$
1 - \beta = \mathbb {P} \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} > \eta^ {\prime} | H _ {1} \right\} = Q \left(\sqrt {n} \frac {\eta^ {\prime} - \mu}{\sigma}\right)
$$

Vale la pena notare che, per $n  \infty , \eta ^ { \prime }  0$ per ogni $\alpha ,$ affinché

$$
\lim _ {n \rightarrow \infty} 1 - \beta = \lim _ {n \rightarrow \infty} Q \left(\sqrt {n} \frac {\eta^ {\prime} (n) - \mu}{\sigma}\right) = 1
$$

ovvero arriviamo alla prestazione ideale $\alpha = 0 , 1 - \beta = 1$

## Stima dei parametri: generalità

Assumiamo di avere un dataset $\mathbf{X}$ $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ che è una realizzazione di un vettore casuale $\mathbf{X}$ $X ^ { n }$;

Assumiamo che il vettore casuale $\mathbf{X}$ $X ^ { n }$ sia estratto da una famiglia di distribuzioni con pmf/pdf $p(\mathbf{x}|\theta)$ $p _ { X ^ { n } | \Theta } ( \pmb { x } ^ { n } | \theta ) / f _ { \pmb { X } ^ { n } | \Theta } ( \pmb { x } ^ { n } | \theta )$, dove il valore di $\theta$ $\theta$ è sconosciuto;

$\theta$ è tipicamente un parametro continuo, che può essere una realizzazione di una variabile casuale continua $\Theta$ con marginale noto $p(\theta)$ $f _ { \Theta } ( \theta )$ (impostazione Bayesiana) o una quantità deterministica sconosciuta che assume valori in un insieme continuo;

Domanda: Come stimiamo $\theta$ basandoci sul campione raccolto?

Si noti che, nell'impostazione Bayesiana, l'applicazione diretta della regola di Bayes produce:

$$
f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) = \left\{ \begin{array}{c} p _ {\boldsymbol {X} ^ {n} | \Theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) \\ \hline \int p _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \\ f _ {\boldsymbol {X} ^ {n} | \Theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) \\ \hline \int f _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \end{array} \right.
$$

> [!quote] Osservazione
> Se $\mathbf{X}$ $\Theta$ è discreto, quanto sopra diventa un problema di classificazione. Si noti inoltre che nell'equazione sopra abbiamo usato il fatto che
> 
> $$
> p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \int p _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \quad f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \int f _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta
> $$

## Stima dei Parametri

> [!theorem] Definizione (Estimatore)
> Un **estimatore** del parametro $\theta$ $\theta$ è una variabile casuale $\hat{\theta}$ ${ \widehat { \Theta } } ( X ^ { n } )$ — le cui realizzazioni sono $\hat{\theta}(\mathbf{x})$ $\widehat { \theta } ( { \pmb x } ^ { n } )$ — che tenta di "indovinare" il valore di $\theta$ $\theta$ basandosi su un'osservazione $\mathbf{x}$ $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$.

Al fine di progettare un estimatore, definiamo prima un **Bayes Risk** medio, ovvero:

$$
\mathcal {R} = \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right] = \mathbb {E} _ {\boldsymbol {X} ^ {n}} \left[ \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \mid \boldsymbol {X} ^ {n} \right] \right]
$$

dove $L(\theta, \hat{\theta})$ $C ( \cdot )$ è una funzione di costo adeguatamente definita.

Un estimatore ottimo è quello che minimizza il Bayes risk, ovvero:

$$
\widehat {\Theta} _ {\text { opt }} (\boldsymbol {X} ^ {n}) = \arg \min \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right]
$$

Poiché

$$
\mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right] = \sum_ {\boldsymbol {x} ^ {n} \in \mathcal {X} ^ {n}} p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) \int C (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta
$$

una stima Bayes-ottimale operante su un campione osservato $\mathbf{x}$ $\pmb { x } ^ { n }$ è definita come:

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \arg \min \int C (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta
$$

## Estimatore del Minimo Errore Quadratico Medio (MMSEE)

Assumiamo che $L(\theta, \hat{\theta}) = (\theta - \hat{\theta})^2$ $C ( \widehat { \Theta } ( X ^ { n } ) - \Theta ) = ( \widehat { \Theta } ( X ^ { n } ) - \Theta ) ^ { 2 }$.

L'estimatore Bayes-ottimale può essere derivato come la soluzione dell'equazione 

$$
\frac {\partial}{\partial \widehat {\theta} (\boldsymbol {x} ^ {n})} \int (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) ^ {2} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta = 0
$$

Otteniamo quindi la stima 

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \int \theta f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta = \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ]
$$

che corrisponde certamente a un minimo data la convessità del rischio Bayes scelto. 

## Esempio: Bernoulli Composta

> [!example] Esempio 1 (Bernoulli Composta)
> Assumiamo che $\mathbf{X}$ $X ^ { n } \in \{ 0 , 1 \} ^ { n }$ sia condizionalmente Bernoulli con parametro $\theta$ $\beta ,$, con $p(\theta)$ $B \sim \mathcal { U } ( 0 , 1 )$.
> 
> Il peso di Hamming $w(\mathbf{x})$ $w ( \pmb { x } ^ { n } )$ di una sequenza binaria è il numero di uno che contiene. Abbiamo: 
> 
> $$
> p _ {\boldsymbol {X} ^ {n} | B} (\boldsymbol {x} ^ {n} | \beta) = \beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}
> $$
> 
> Facendo la media su $\mathbf{B}$ otteniamo la legge incondizionata: 
> 
> $$
> p \mathbf {x} ^ {n} (\mathbf {x} ^ {n}) = \int_ {0} ^ {1} \beta^ {w (\mathbf {x} ^ {n})} (1 - \beta) ^ {n - w (\mathbf {x} ^ {n})} d \beta = \frac {\Gamma (w + 1) \Gamma (n - w + 1)}{\Gamma (n + 2)} = \frac {1}{\binom{n + 1}{w (\mathbf {x} ^ {n})}}
> $$
> 
> La legge condizionale è quindi 
> 
> $$
> f _ {B | \boldsymbol {X} ^ {n}} (\beta | \boldsymbol {x} ^ {n}) = \frac {\beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}}{p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})} = \frac {\beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}}{\binom{n + 1}{w (\boldsymbol {x} ^ {n})}}
> $$

## Esempio: Bernoulli Composta - cont.)

> [!example] Esempio 2 (Bernoulli Composta - cont.)
> La stima MMSE è quindi 
> 
> $$
> \frac {1}{p \boldsymbol {x} ^ {n} (\boldsymbol {x} ^ {n})} \int_ {0} ^ {1} \beta^ {w (\boldsymbol {x} ^ {n}) + 1} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})} d \beta
> $$
> 
> Risolvendo l'integrale si ottiene
> 
> $$
> \hat {\beta} _ {\text {MMSE}} (\boldsymbol {x} ^ {n}) = \frac {\Gamma (w + 2) \Gamma (n - w + 1)}{\Gamma (n + 3)} \frac {1}{\binom{n + 1}{w (\boldsymbol {x} ^ {n})}} = \frac {w (\boldsymbol {x} ^ {n}) + 1}{n + 2}
> $$
> 
> che è la stima ottenuta tramite l'estimatore MMSE: 
> 
> $$
> \hat {B} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) = \frac {w (\boldsymbol {X} ^ {n}) + 1}{n + 2}
> $$

## Estimatore Maximum A Posteriori (MAPE)

Assumiamo ora la seguente funzione di costo: 

$$
C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) = \Pi \left(\frac {\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta}{\epsilon}\right) = \left\{ \begin{array}{l l} 0 & \left| \widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta \right| <   \frac {\epsilon}{2} \\ 1 & \text { otherwise } \end{array} \right.
$$

È ovvio che, poiché $\epsilon$ è arbitrariamente piccola, ciò si traduce nell'estimatore MAP 

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \arg \max f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n})
$$

Applicando questo estimatore al problema precedente (Bernoulli composta) otteniamo la stima: 

$$
\widehat {\beta} _ {\mathrm{MAP}} (\pmb {x} ^ {n}) = \frac {w (\pmb {x} ^ {n})}{n}
$$

Di conseguenza, l'estimatore MAP del parametro sconosciuto è 

$$
\widehat {B} _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) = \frac {w (\boldsymbol {X} ^ {n})}{n}
$$

## Prestazioni dell'Estimatore: Errore Sistematico (Bias)

Si analizzano preliminarmente le proprietà di distorsione degli stimatori considerati.

$$
\mathbb {E} \left[ B \right] = \int_ {0} ^ {1} \beta d \beta = \frac {1}{2}, \quad \mathbb {E} \left[ B ^ {2} \right] = \frac {1}{3}, \quad \sigma_ {B} ^ {2} = \frac {1}{1 2}
$$

Poiché 

$$
\mathbb {E} \left[ w (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \overbrace {\mathbb {E} \left[ w (\boldsymbol {X} ^ {n}) | B \right]} ^ {n B} \right] = \frac {n}{2}, \quad \mathbb {E} \left[ w ^ {2} (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \overbrace {\mathbb {E} \left[ w (\boldsymbol {X} ^ {n}) | B \right]} ^ {n B (1 - B) + n ^ {2} B ^ {2}} \right] = \frac {n}{6} + \frac {n ^ {2}}{3}
$$

dove $\begin{array} { r } { \sigma _ { w ( X ^ { n } ) } ^ { 2 } = \frac { n } { 6 } \left( 1 + \frac { n } { 2 } \right) } \end{array}$ 

Per l'MMSEE: 

$$
\mathbb {E} \left[ \hat {B} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) | B = \beta \right] = \frac {n \beta + 1}{n + 2}, \quad \mathbb {E} \left[ \hat {B} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) \right] = \frac {\frac {n}{2} + 1}{n + 2}
$$

Per il MAPE: 

$$
\mathbb {E} \left[ \hat {B} _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) | B = \beta \right] = \beta ,
$$

$$
\mathbb {E} \left[ \hat {B} _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) \right] = \frac {\frac {n}{2}}{n} = \frac {1}{2}
$$

Si conclude che l'**MMSEE** è un estimatore distorto (*biased*), mentre il **MAP** non lo è. 

> [!quote] Osservazione
> L'MMSEE è asintoticamente non distorto, poiché l'errore sistematico svanisce all'aumentare di $n$.

## Errori Casuali: Consistenza

A seguito dei calcoli relativi alla varianza e all'errore casuale, si ottengono i seguenti risultati: 

$$
\mathbb {E} \left[ (B _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) - B) ^ {2} \right] = \overline {{e ^ {2}}} _ {\text { MMSE }} = \frac {n - 2}{6 (n + 2) ^ {2}}
$$

$$
\mathbb {E} \left[ (B _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) - B) ^ {2} \right] = \overline {{e ^ {2}}} _ {\mathrm{MAP}} = \frac {1}{6 n}
$$

Si osserva che $\overline { { e ^ { 2 } } } _ { \mathsf { M M S E } } < \overline { { e ^ { 2 } } } _ { \mathsf { M A P } } \ \forall \space n$ 

Poiché entrambi gli MSE tendono a zero all'aumentare di $n$, i due stimatori sono definiti **MS consistenti**, nel senso che l'errore casuale ha un valore MS asintoticamente zero. 

Sfruttando la disuguaglianza di Tchebyshev, si deduce che entrambi gli estimatori tendono a $B$ in probabilità (consistenza, nota anche come consistenza debole). Se ${ \widehat { B } } ( X ^ { n } )$ è uno dei due estimatori, si ha: 

$$
\forall \space \epsilon > 0 \quad \lim _ {n \rightarrow \infty} \operatorname * {P r} \left\{\left| \widehat {B} (\boldsymbol {X} ^ {n}) - B \right| > \epsilon \right\} = 0
$$

Si può dimostrare che entrambi gli estimatori sono **fortemente consistenti**, nel senso che ${ \widehat { B } } ( X ^ { n } ) \to B$ quasi certamente.

## Definizioni Generali

Consideriamo un campione $\mathbf{X}$ estratto da un vettore casuale $\mathbf{Y}$. 

$\mathcal { X } ^ { n }$ può essere discreto o continuo, ma si assume che $X ^ { n }$ abbia una pdf (pmf, nel caso discreto) nota appartenere a una famiglia con prior nota. Si assume quindi la conoscenza della pdf congiunta $f _ { \pmb { X } ^ { n } , \Theta } ( \pmb { x } ^ { n } , \theta )$ e del parametro prior $f _ { \Theta } ( \theta )$. 

L'obiettivo è inferire il valore del parametro di $\theta$ per la realizzazione osservata $\pmb { x } ^ { n }$. La stima MMSE e la stima MAP sono quindi definite come:

$$
\widehat {\theta} _ {\mathrm{MMSE}} (\boldsymbol {x} ^ {n}) = \mathbb {E} \left[ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right] = \int \theta f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta , \quad \widehat {\theta} _ {\mathrm{MAP}} (\boldsymbol {x} ^ {n}) = \arg \max _ {\theta} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n})
$$

> [!theorem] Non distorto (Unbiased)
> Un estimatore è non distorto (*unbiased*) se $\mathbb { E } \left[ \widehat { \Theta } ( \pmb { \cal X } ^ { n } ) - \Theta \right] = 0 ;$.

> [!theorem] Asintoticamente non distorto
> Un estimatore è asintoticamente non distorto se è non distorto solo nel limite di una dimensione del campione infinita.

> [!theorem] Consistente
> Un estimatore è consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ in probabilità.

> [!theorem] MS Consistente
> Un estimatore è MS consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ in media quadratica.

> [!theorem] Fortemente Consistente
> Un estimatore è fortemente consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ quasi certamente.

## Un esempio: Osservazioni Gaussiane con media casuale

Sia $x$ estratto da $y$ con: 

$$
f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \exp \left[ - \frac {(x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}} \right]
$$

Sia $\mathbf{x}$ una realizzazione di $\mathbf{y}$. 

Vogliamo inferire il valore $\mu$ di $M$ appartenente all'osservazione $\mathbf{x}$ di $\mathbf{y}$. 

Si noti che la densità a posteriori della media è: 

$$
f _ {M | \boldsymbol {X} ^ {n}} (\mu | \boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) f _ {M} (\mu)}{f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})} = \mathcal {N} \left(\frac {\sum_ {i = 1} ^ {n} x _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}, \frac {1}{\frac {n}{\sigma^ {2}} + \frac {1}{\sigma_ {M} ^ {2}}}\right)
$$

In altri termini, il prior coniugato della media di una distribuzione Gaussiana è nuovamente Gaussiano. 

Abbiamo quindi che la stima MMSE della media è: 

$$
\widehat {\mu} _ {\text { MMSE }} (\boldsymbol {x} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} x _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}} \Longleftrightarrow \widehat {M} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}
$$

Consideriamo ora la stima MAP. È possibile scrivere: 

$$
\ln f _ {M | \boldsymbol {X} ^ {n}} (\mu | \boldsymbol {x} ^ {n}) = \ln f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) + \ln f _ {M} (\mu) - \ln f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})
$$

Massimizzando rispetto a $\mu$ si ottiene lo stimatore MAP: 

$$
\widehat {\mu} _ {\text {MAP}} (\boldsymbol {x} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}} \Longleftrightarrow \widehat {M} _ {\text {MAP}} (\boldsymbol {X} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}
$$

che coincide con l'MMSEE. 

> [!quote] Osservazione
> È casuale o esiste un motivo più profondo per la coincidenza di questi due stimatori?

## Unicità degli stimatori Bayesiani

Sia $C(\cdot)$ una funzione di costo arbitraria dell'errore di stima. 

Si assuma che $C(\cdot)$ sia pari e convessa e che $\mathbf{y}$ sia simmetrica rispetto alla sua media $\mu$, ovvero: 

$$
f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta - \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ] | \boldsymbol {x} ^ {n}) = f _ {\Theta | \boldsymbol {X} ^ {n}} (- \theta + \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ] | \boldsymbol {x} ^ {n})
$$

Allora l'MMSEE minimizza il rischio Bayesiano per qualsiasi funzione di costo in questa classe. 

La dimostrazione è omessa in questo testo. 

Si noti che, rigorosamente parlando, la funzione di costo 0-1 che porta a uno stimatore MAP non è differenziabile. Tuttavia, può essere dimostrato che, sotto la condizione di simmetria sopra indicata sulla distribuzione a posteriori, si ha: 

$$
\widehat {\mu} _ {\text { MAP }} (\boldsymbol {x} ^ {n}) = \widehat {\mu} _ {\text { MMSE }} (\boldsymbol {x} ^ {n})
$$

# Inferenza non Bayesiana: Stima di parametri non casuali

Assumiamo ora che le osservazioni $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ siano estratte da una famiglia di pdf, $f _ { { \pmb X } ^ { n } } \big ( { \pmb x } ^ { n } ; { \boldsymbol \theta } \big )$; 

Assumiamo che $\theta$ sia deterministico e sconosciuto: equivalentemente, possiamo assumere che non abbiamo informazioni a priori sufficienti per assegnare un prior $f _ { \Theta } ( \theta )$ ); 

Assumiamo che lo spazio dei parametri sia $S$; 

Definiamo la **verosimiglianza** del parametro $\theta$, dato che le osservazioni $\pmb { x } ^ { n }$ sono disponibili, la funzione: 

$$
L (\theta ; \boldsymbol {x} ^ {n}) = f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta)
$$

o, equivalentemente, la log-verosimiglianza la funzione 

$$
\Lambda (\theta ; \boldsymbol {x} ^ {n}) = \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta)
$$

Una stima di Massima Verosimiglianza (ML) di $\theta$ è 

$$
\widehat {\theta} _ {\mathrm{ML}} \left(\boldsymbol {x} ^ {n}\right) = \arg \max _ {\theta \in \mathcal {S}} \log f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {x} ^ {n}; \theta\right)
$$

ed è una realizzazione dello stimatore di Massima Verosimiglianza (MLE): 

$$
\widehat {\Theta} _ {M L} \left(\boldsymbol {X} ^ {n}\right) = \arg \max _ {\theta \in \mathcal {S}} \log f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {X} ^ {n}; \theta\right)
$$

## Inferenza non Bayesiana: Misure di prestazione

Data uno stimatore $\Theta ( { \pmb x } ^ { n } )$ del parametro non casuale $\theta ,$, abbiamo: 

$$
\mathbb {E} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \theta + b _ {n} (\theta)
$$

con $b _ { n } ( \theta )$ il **bias** dello stimatore; 

Lo stimatore è non distorto (unbiased) se $b _ { n } ( \theta ) = 0$, mentre è solo asintoticamente non distorto se $b _ { n } ( \theta )$ diventa infinitesimale con $n ;$ 

L'errore casuale dello stimatore è solitamente quantificato tramite il suo valore Mean Square, ovvero: 

$$
\mathbb {E} \left[ (\Theta (\boldsymbol {X} ^ {n}) - \theta) ^ {2} \right] = \overline {{e _ {n} ^ {2}}}
$$

Uno stimatore MMSE non distorto di $\theta$ è uno stimatore che minimizza la varianza: 

$$
\operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \Theta^ {2} (\boldsymbol {X} ^ {n}) \right] - \theta^ {2}
$$

Uno stimatore è debolmente consistente se $\Theta ( { \pmb x } ^ { n } ) \to \theta$ in probabilità, fortemente consistente se $\Theta ( { \pmb x } ^ { n } ) \to \theta$ quasi certamente, MS consistente se $\overline { { e _ { n } ^ { 2 } } } \to 0$ 

## Limite di Cramér-Rao - Fatti preliminari

Sia $\pmb { x } ^ { n }$ un campione estratto da un vettore casuale ${ \pmb X } ^ { n } \sim f _ { { \pmb X } ^ { n } } ( { \pmb x } ^ { n } ; { \pmb \theta } )$ con $\theta$ non casuale; 

Consideriamo l'identità 

$$
\int_ {\mathbb {R} ^ {n}} f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {x} ^ {n}; \theta\right) d \boldsymbol {x} ^ {n} = 1
$$

Dopo la differenziazione rispetto a $\theta$ della precedente abbiamo 

$$
\begin{array}{c} \int_ {\mathbb {R} ^ {n}} \frac {\partial f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} d \boldsymbol {x} ^ {n} = \int_ {\mathbb {R} ^ {n}} \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta) d \boldsymbol {x} ^ {n} \\ = \mathbb {E} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = 0 \end{array}
$$

Differenziando ancora abbiamo: 

$$
\begin{array}{c} \mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right] = \text {var} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = \\ = - \mathbb {E} \left[ \frac {\partial^ {2} \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta^ {2}} \right] \end{array}
$$

## Limite di Cramér-Rao - Derivazione

Sia $\widehat { \Theta } ( X ^ { n } )$ uno stimatore del parametro non casuale $\theta$ con: 

$$
\mathbb {E} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \int_ {\mathbb {R} ^ {n}} \widehat {\Theta} (\boldsymbol {X} ^ {n}) f _ {\boldsymbol {X} ^ {n}} (x ^ {n}; \theta) d x ^ {n} = \theta + b _ {n} (\theta)
$$

Differenziando rispetto a $\theta$ l'identità precedente abbiamo 

$$
\begin{array}{l} \mathbb {E} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] \\ \int_ {\mathbb {R} ^ {n}} \Theta (x ^ {n}) \frac {\partial f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)}{\partial \theta}   d x ^ {n} = \overbrace {\int_ {\mathbb {R} ^ {n}} \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)}{\partial \theta} f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)   d x ^ {n}} \\ \text { COV } \left[ \Theta (\boldsymbol {X} ^ {n}), \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = 1 + b _ {n} ^ {\prime} (\theta) \end{array}
$$

Applicando la diseguaglianza di Cauchy-Schwarz, otteniamo finalmente 

$$
\left| \operatorname{COV} \left[ \Theta (\boldsymbol {X} ^ {n}), \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] \right| ^ {2} = \left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2} \leq \operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] \operatorname{Var} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right]
$$

## Limite di Cramér-Rao - Ulteriori discussioni

Elaborando le derivazioni precedenti, otteniamo un limite inferiore imbattibile alla varianza di qualsiasi stimatore del parametro non casuale $\theta$ nella forma: 

$$
\operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] \geq \frac {\left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2}}{\mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right]} = \frac {\left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2}}{I _ {n} (\theta)}
$$

La quantità $I _ { n } ( \theta )$ è definita come **Informazione di Fisher**, e obbedisce alla seguente identità: 

$$
I _ {n} (\theta) = \mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right] = - \mathbb {E} \left[ \frac {\partial^ {2} \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta^ {2}} \right]
$$

## Limite di Cramér-Rao - Stimatori non distorti

Come anticipato, lo stimatore $\Theta ( { \pmb x } ^ { n } )$ è non distorto se $\mathbb{E}$ $[ \Theta ( { \pmb x } ^ { n } ) ] = \theta$ 

In questa situazione, abbiamo che 

$$
\mathbb {E} \left[ (\Theta (\boldsymbol {X} ^ {n}) - \theta) ^ {2} \right] = \operatorname{Var} [ \Theta (\boldsymbol {X} ^ {n}) ] \geq \frac {1}{I _ {n} (\theta)}
$$

Così il Limite di Cramér-Rao (CRB) diventa un limite inferiore imbattibile all'MSE di qualsiasi stimatore. 

Uno stimatore non distorto il cui MSE è uguale al CRB è definito **efficiente** 

> [!theorem] Fatto importante
> Se esiste uno stimatore efficiente per un dato problema di stima non Bayesiana, questo coincide necessariamente con lo stimatore ML. 

## Un esempio: inferire la frequenza del cifrario di una sorgente senza memoria

Consideriamo inizialmente $\pmb { x } ^ { n } \in \{ 0 , 1 \} ^ { n }$ , estratto da $\pmb { X } ^ { n } \sim  { \mathcal { B } } ( 1 , \beta )$ , $\beta$ sconosciuto; 

Abbiamo visto che, se $w ( \pmb { x } ^ { n } )$ è il peso di Hamming della sequenza osservata, allora: 

$$
p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}
$$

La stima ML viene quindi trovata come: 

$$
\frac {\partial \log p _ {X ^ {n}} (x ^ {n})}{\partial \beta} = 0 \Longrightarrow \widehat {\beta} _ {\mathrm{ML}} (x ^ {n}) = \frac {w (x ^ {n})}{n}
$$

L'estimatore $\begin{array} { r } { \beta ( \pmb { X } ^ { n } ) = \frac { w ( \pmb { X } ^ { n } ) } { n } } \end{array}$ è tale che: 

$$
\mathbb {E} \left[ \frac {w (\boldsymbol {X} ^ {n})}{n} \right] = \beta  ,
$$

$$
\operatorname{var} \left[ \frac {w (\boldsymbol {X} ^ {n})}{n} \right] = \frac {\beta (1 - \beta)}{n}
$$

Di conseguenza, è non distorto (unbiased) e MS consistente. È efficiente?

## Frequenza di cifratura - cont.

Si noti che abbiamo: 

$$
\log p _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {X} ^ {n}; \beta\right) = w \left(\boldsymbol {X} ^ {n}\right) \log \beta + [ n - w \left(\boldsymbol {X} ^ {n}\right) ] \log (1 - \beta)
$$

Pertanto abbiamo: 

$$
\frac {\partial p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \beta)}{\partial \beta} = \frac {w (\boldsymbol {X} ^ {n})}{\beta} - \frac {n - w (\boldsymbol {X} ^ {n})}{1 - \beta}
$$

$$
\frac {\partial^ {2} p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \beta)}{\partial \beta^ {2}} = - \frac {w (\boldsymbol {X} ^ {n})}{\beta^ {2}} - \frac {n - w (\boldsymbol {X} ^ {n})}{(1 - \beta) ^ {2}}
$$

Poiché $\mathbb { E } [ w ( \pmb { X } ^ { n } ) ] = \pmb { n } \beta$ , abbiamo: 

$$
I _ {n} (\beta) = \frac {n}{\beta} + \frac {n}{1 - \beta} = \frac {n}{\beta (1 - \beta)} \Longrightarrow \mathrm{CRB} = \frac {\beta (1 - \beta)}{n}
$$

Concludiamo che la **MLE** (Maximum Likelihood Estimation) della frequenza di cifratura è efficiente. 

## Parametri multipli - inferenza Bayesiana

Assumiamo ora di avere $m$ parametri casuali, $\pmb { \theta } [ \theta _ { 1 } , \ldots , \theta _ { m } ] ^ { T }$ estratti da una pdf nota $f _ { \Theta } ( \pmb { \theta } )$ e un set di dati $\pmb { x } ^ { n }$ estratti da una pdf condizionale $f _ { { \pmb X } ^ { n } | \pmb \theta } ( { \pmb x } ^ { n } | \pmb \theta )$.

Definiamo una funzione di costo 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = C \left(\theta_ {1} - \widehat {\theta} _ {1}, \dots , \theta_ {m} - \widehat {\theta} _ {m}\right)
$$

Un estimatore Bayes-ottimale può essere trovato risolvendo il problema di minimizzazione: 

$$
\widehat {\boldsymbol {\theta}} (\boldsymbol {x} ^ {n}): \quad \mathbb {E} \left[ C (\boldsymbol {\Theta} - \widehat {\boldsymbol {\Theta}} (\boldsymbol {X} ^ {n})) \right] = 0
$$

Utilizzando la stessa procedura del caso a parametro singolo otteniamo quindi: 

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \arg \min \int_ {\mathbb {R} ^ {m}} C \left(\boldsymbol {\theta} - \widehat {\theta} \left(\boldsymbol {X} ^ {n}\right)\right) f _ {\Theta | \boldsymbol {X} ^ {n}} \left(\boldsymbol {\theta} \mid \boldsymbol {X} ^ {n}\right) d \boldsymbol {\theta}
$$

## L'estimatore MMSE

> [!theorem] Estimatore MMSE
> L'**MMSE** (Minimum Mean Square Error) è l'estimatore che minimizza il valore atteso del quadrato dell'errore tra la stima e il valore reale.
> 
> Formalizzazione:
> $$ \hat{\theta}_{MMSE} = \arg\min_{\hat{\theta}} E[||\theta - \hat{\theta}||^2] $$

Assumiamo che la funzione di costo sia 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = \sum_ {i = 1} ^ {m} \left(\theta_ {i} - \widehat {\theta} _ {i} (\boldsymbol {x} ^ {n}))\right)
$$

Poiché il problema di minimizzazione è disgiunto (ovvero, separabile), abbiamo: 

$$
\widehat {\theta} _ {i} (\boldsymbol {x} ^ {n}) = \mathbb {E} \left[ \Theta_ {i} | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right] = \int \theta_ {i} f _ {\theta_ {i} | \boldsymbol {X} ^ {n}} (\theta_ {i} | \boldsymbol {x} ^ {n}) d \theta_ {i}
$$

dove l'estimatore vettoriale MMSE si legge: 

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \mathbb {E} \left[ \Theta | \boldsymbol {X} ^ {n} \right]
$$

## L'estimatore MAP

> [!theorem] Estimatore MAP
> La **MAP** (Maximum A Posteriori) è un metodo di stima che massimizza la probabilità a posteriori del parametro, combinando la verosimiglianza dei dati con la conoscenza a priori sulla distribuzione dei parametri.
> 
> Formalizzazione:
> $$ \hat{\theta}_{MAP} = \arg\max_{\theta} p(\theta | \mathbf{x}) $$

Se assumiamo 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = \sum_ {i = 1} ^ {m} \Pi \left(\frac {\theta_ {i} - \widehat {\theta} _ {i} (\boldsymbol {x} ^ {n})}{\epsilon}\right)
$$

considerando la stessa procedura abbiamo 

$$
\widehat {\theta} _ {i} \left(\boldsymbol {x} ^ {n}\right): \quad \frac {\partial f _ {\Theta | \boldsymbol {X} ^ {n}} \left(\boldsymbol {\theta} \mid \boldsymbol {x} ^ {n}\right)}{\partial \theta_ {i}} \Bigg | _ {\theta_ {i} = \widehat {\theta} _ {i} \left(\boldsymbol {x} ^ {n}\right)} = 0
$$

Equivalentemente, abbiamo che la stima MAP risolve l'equazione: 

$$
\nabla_ {\boldsymbol {\theta}} f _ {\boldsymbol {\Theta} | \boldsymbol {X} ^ {n}} (\boldsymbol {\theta} | \boldsymbol {x} ^ {n}) \big | _ {\boldsymbol {\theta} = \widehat {\boldsymbol {\theta}} (x ^ {n})} = 0
$$

## Stima non Bayesiana di parametri multipli

Assumiamo ora che il vettore dei parametri $\pmb { \theta }$ sia reale e deterministico; 

Possiamo definire la funzione di log-verosimiglianza dei dati osservati, assunti estratti da una famiglia di distribuzioni $f _ { \pmb { X } ^ { n } } ( \pmb { x } ^ { n } ; \pmb { \theta } )$ come: 

$$
\Lambda (\boldsymbol {\theta}; \boldsymbol {x} ^ {n}) = \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}, \boldsymbol {\theta})
$$

Definiamo la stima Maximum-Likelihood del vettore $\pmb { \theta }$ come la soluzione dell'equazione: 

$$
\nabla_ {\boldsymbol {\theta}} \Lambda (\boldsymbol {\theta}; \boldsymbol {x} ^ {n}) | _ {\boldsymbol {\theta} = \widehat {\boldsymbol {\theta}} (\boldsymbol {x} ^ {n})} = 0
$$

L'estimatore corrispondente $\widehat { \Theta } ( X ^ { n } )$ è di nuovo definito come un estimatore Maximum Likelihood (ML) e gode di una serie di proprietà fondamentali. 

## Estimatori MMSE lineari

0 Iniziamo con un semplice problema scalare. Assumiamo che $\pmb { x } ^ { n }$ sia il campione osservato, estratto da $X ^ { n }$, e assumiamo di voler progettare un estimatore lineare di un parametro casuale $\Theta ,$, distribuito secondo una legge nota, nella forma: 

$$
\widehat {\Theta} (\boldsymbol {X} ^ {n}) = \boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b \quad \boldsymbol {a} \in \mathbb {R} ^ {n}
$$

Un estimatore **Linear MMSE** (LMMSE) seleziona il vettore $\mathbf{a}$ e la costante $b$ in modo da minimizzare l'MMSE 

$$
\mathbb {E} \left[ (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) ^ {2} \right] = \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right]
$$

che è uguale a 

$$
\boldsymbol {a} ^ {T} \boldsymbol {R} \boldsymbol {a} + b ^ {2} + \mathbb {E} [ \Theta^ {2} ] - 2 b (\overline {{{\Theta}}}) - 2 \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} \Theta ] - 2 b \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ]
$$

dove $\pmb { R } = \mathbb { E } \left[ \pmb { X } ^ { n } \pmb { X } ^ { n T } \right]$ è la matrice di correlazione del vettore casuale $X ^ { n }$.

## Estimatori MMSE lineari (cont.)

Annullando il gradiente rispetto ad $\mathbf{a}$ e la derivata rispetto a $b$ otteniamo: 

$$
\nabla_ {\boldsymbol {a}} \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \mathbb {E} [ \boldsymbol {X} ^ {n} \Theta ] = 0
$$

$$
\frac {\partial \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right]}{\partial b} = 2 b - 2 \overline {{\Theta}} - 2 \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ] = 0
$$

## Risolvendo per b si ottiene

$$
b _ {\text { LMMSE }} = \mathbb {E} [ \Theta ] - \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ]
$$

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \boldsymbol {a} ^ {T} \left(\boldsymbol {X} ^ {n} - \mathbb {E} \left[ \boldsymbol {X} ^ {n} \right]\right) + \mathbb {E} [ \Theta ]
$$

che, reinserito nell'MSE dimostra che $\mathbf{a}$ dovrebbe minimizzare 

$$
\left\| \boldsymbol {a} ^ {T} \left(\boldsymbol {X} ^ {n} - \mathbb {E} \left[ \boldsymbol {X} ^ {n} \right]\right) + (\Theta - \mathbb {E} [ \Theta ]) \right\| ^ {2}
$$

Di conseguenza, denotando $\pmb { M } = \mathbb { E } \left[ ( \pmb { X } ^ { n } - \mathbb { E } [ \pmb { X } ^ { n } ] ) ( \pmb { X } ^ { n } - \mathbb { E } [ \pmb { X } ^ { n } ] ) ^ { T } \right]$ la matrice di covarianza di $X ^ { n }$, l'estimatore LMMSE si legge 

$$
\boldsymbol {a} _ {\text { LMMSE }} = \boldsymbol {M} ^ {- 1} \mathbb {E} \left[ \left(\boldsymbol {X} ^ {n} - \mathbb {E} [ \boldsymbol {X} ^ {n} ]\right) (\Theta - \mathbb {E} [ \Theta ]) \right] = \boldsymbol {M} ^ {- 1} \boldsymbol {s}
$$

## L'algoritmo del gradiente

Assumiamo di voler risolvere iterativamente il problema LMMSE delineato in precedenza; 
Abbiamo visto che il gradiente dell'MSE è scritto come 

$$
\nabla_ {a} \mathbb {E} \left[ \left(\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta\right) ^ {2} \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \mathbb {E} \left[ \boldsymbol {X} ^ {n} \Theta \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \boldsymbol {s}
$$

con $\mathbb { E } \left[ \pmb { X } ^ { n } \Theta \right] = \pmb { s }$ noto; 

Consideriamo la seguente iterazione per determinare $\pmb { \alpha } _ { \mathrm { L M M S E } }$ 

$$
\boldsymbol {a} ^ {(n + 1)} = \boldsymbol {a} ^ {(n)} - \gamma (\boldsymbol {M a} ^ {(n)} - \boldsymbol {s})
$$

che può essere riscritta come 

$$
\boldsymbol {a} ^ {(n + 1)} = \boldsymbol {a} ^ {(n)} - \gamma \boldsymbol {M} \left(\boldsymbol {a} ^ {(n)} - \underbrace {\boldsymbol {M} ^ {- 1} \boldsymbol {s}} _ {\boldsymbol {a} _ {\text { LMMSE }}}\right)
$$

## L'algoritmo del Gradiente - cont.

L'errore alla $(n + 1)$-es iterazione si legge 

$$
\boldsymbol {\epsilon} ^ {(n + 1)} = \boldsymbol {a} ^ {(n + 1)} - \boldsymbol {a} _ {\text { LMMSE }} = \boldsymbol {a} ^ {(n)} - \boldsymbol {a} _ {\text { LMMSE }} - \gamma \boldsymbol {M} (\boldsymbol {a} ^ {(n)} - \boldsymbol {a} _ {\text { LMMSE }}) = (\boldsymbol {I} - \gamma \boldsymbol {M}) \boldsymbol {\epsilon} ^ {(n)}
$$

Di conseguenza abbiamo 

$$
\boldsymbol {\epsilon} ^ {(n + 1)} = (\boldsymbol {I} - \gamma \boldsymbol {M}) ^ {n} \boldsymbol {\epsilon} ^ {(1)} = \boldsymbol {U} (\boldsymbol {I} - \gamma \boldsymbol {\Lambda}) ^ {n} \boldsymbol {U} ^ {T}
$$

dove $\Lambda$ è la matrice diagonale dei valori propri di $M$ e $U$ contiene i suoi autovettori. 

L'errore converge quindi a zero se il modulo massimo dei valori propri o $\pmb { I } - \gamma \pmb { M }$ è minore di uno, cioè: 

$$
- 1 <   1 - \gamma \lambda_ {M A X} <   1 \Longrightarrow 0 <   \gamma <   \frac {2}{\lambda_ {M A X}}
$$

## Un approccio diverso: statistica descrittiva

In questa sezione si abbandona l'approccio probabilistico per adottare la **statistica descrittiva**, in cui i campioni sono considerati come entità dati e non come realizzazioni di vettori casuali.

Si definisce un *dataset* di addestramento come una collezione di $p$ campioni $n$-dimensionali, organizzabili nella matrice $n \times p$:

$$
\boldsymbol {X} = \left[ \begin{array}{c c c} x _ {1} (1) & \dots & x _ {1} (p) \\ \dots & \dots & \dots \\ x _ {n} (1) & \dots & x _ {n} (p) \end{array} \right] \in \mathbb {R} ^ {n \times p}
$$

Si supponga di conoscere $p$ valori misurati del parametro $\theta _ { r }$, ciascuno corrispondente a uno dei $p$ campioni $n$-dimensionali del *training set*, ovvero:

$$
\boldsymbol {y} = [ \theta (1), \dots , \theta (p) ] \in \mathbb {R} ^ {p}
$$

L'obiettivo è adattare i dati a un modello lineare nella forma:

$$ \mathbf{y} = \mathbf{X}\boldsymbol{\theta} + \boldsymbol{\epsilon} \tag{1} $$

dove $\epsilon _ { n }$ incapsula l'errore di modellazione.

## L'estimatore dei Minimi Quadrati (Least Squares)

Data la natura del dataset $p$-dimensionale, si procede alla selezione di $a$ al fine di minimizzare la seguente funzione di costo:

$$
\parallel \epsilon_ {n} \parallel^ {2} = \sum_ {i = 1} ^ {p} \left[ \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) - \theta (i) \right] ^ {2}
$$

Il problema consiste nel selezionare ottimamente $a$ e $b$. Preliminarmente, si osserva che:

$$
\sum_ {i = 1} ^ {p} \left[ \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) - \theta (i) \right] ^ {2} = \| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \| ^ {2}
$$

Si nota inoltre che:

$$
\| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \| ^ {2} = \boldsymbol {a} ^ {T} \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {a} + \| \boldsymbol {y} \| ^ {2} - 2 \boldsymbol {a} ^ {T} \boldsymbol {X} \boldsymbol {y}
$$

## L'estimatore dei Minimi Quadrati - cont.

Differenziando la funzione di costo rispetto a $a$, si ottiene:

$$
\nabla_ {a} \left\| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \right\| ^ {2} = 2 \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {a} - 2 \boldsymbol {X} \boldsymbol {y} = 0
$$

L'equazione risultante produce:

$$ (\mathbf{X}^T\mathbf{X})\boldsymbol{\theta} = \mathbf{X}^T\mathbf{y} \tag{2} $$

$$
\boldsymbol {a} _ {\mathrm{LS}} = \left(\boldsymbol {X} \boldsymbol {X} ^ {T}\right) ^ {- 1} \boldsymbol {X} \boldsymbol {y}
$$

Questa condizione richiede che la matrice $( { \pmb x } { \pmb x } ^ { T } )$ sia invertibile $( \mathsf { i . e . , } \ p \geq n )$. Per riferimento futuro, la stima basata su un campione $p$-dimensionale viene denominata:

$$ \boldsymbol{\theta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y} \tag{3} $$

$$
\boldsymbol {a} _ {\mathrm{LS}} (p) = \left(\boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p)\right) ^ {- 1} \boldsymbol {X} (p) \boldsymbol {y} (p)
$$

Si consideri un'osservazione dell'ambiente a orizzonte infinito, tale che la dimensione del campione $p$ possa aumentare indefinitamente. Si distinguono due scenari operativi:

1. Miglioramento progressivo della stima mediante l'aggiunta di nuove osservazioni;
2. Adattamento a condizioni variabili attraverso la "dimenticanza" delle osservazioni datate, al fine di pesare maggiormente i dati recenti.

È possibile regolare l'estimatore LS per gestire entrambi gli scenari con una complessità computazionale limitata.

## Apprendimento LS

Si supponga $p \geq n$ e che sia stata valutata la stima:

$$
\boldsymbol {a} _ {\mathrm{LS}} (p) = \left[ \boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p) \right] ^ {- 1} \boldsymbol {X} (p) \boldsymbol {y} (p)
$$

Considerando l'inserimento di un nuovo vettore nel dataset, denominato $\pmb { x } ^ { n } ( p + 1 )$, e una nuova osservazione $\theta ( p + 1 )$, la nuova stima sarebbe:

$$ \boldsymbol{\theta}_{new} = (\mathbf{X}_{new}^T\mathbf{X}_{new})^{-1}\mathbf{X}_{new}^T\mathbf{y}_{new} \tag{4} $$

$$
\boldsymbol {a} _ {\mathrm{LS}} (p + 1) = \left[ \boldsymbol {X} (p + 1) \boldsymbol {X} ^ {T} (p + 1) \right] ^ {- 1} \boldsymbol {X} (p + 1) \boldsymbol {y} (p + 1)
$$

> [!quote] Osservazione
> È necessario ricalcolare l'intera inversione di matrice per ogni nuovo dato?
> 
> L'operazione di inversione comporta una complessità $O(n^3)$, mentre il prodotto di matrici ha una complessità $O(n^2)$ (in termini di moltiplicazioni).

## La Formula di Sherman-Morrison

Sia $R$ una matrice invertibile di ordine $n ;$. Siano $u$ e $v$ vettori colonna $n$-dimensionali. Si applica il seguente lemma di inversione di matrice con aggiornamento *rank-1*:

$$
\left(\boldsymbol {R} + \boldsymbol {u v} ^ {T}\right) ^ {- 1} = \boldsymbol {R} ^ {- 1} - \frac {\boldsymbol {R} ^ {- 1} \boldsymbol {u v} ^ {T} \boldsymbol {R} ^ {- 1}}{1 + \boldsymbol {u} ^ {T} \boldsymbol {R} ^ {- 1} \boldsymbol {v}}
$$

## Generalità

*Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation*

## Applicazione

## Notare che

$$ \dots $$

$$
\underbrace {\boldsymbol {X} (p + 1) \boldsymbol {X} ^ {T} (p + 1)} _ {\boldsymbol {R} (p + 1)} = \sum_ {i = 1} ^ {p + 1} \boldsymbol {x} ^ {n} (i) \boldsymbol {x} ^ {n T} (i) = \underbrace {\boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p)} _ {\boldsymbol {R} (p)} + \boldsymbol {x} ^ {n} (p + 1) \boldsymbol {x} ^ {n T} (p + 1)
$$

Di conseguenza:

$$ \dots $$

$$
\boldsymbol {R} ^ {- 1} (p + 1) = \boldsymbol {R} ^ {- 1} (p) - \frac {\boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1) \boldsymbol {x} ^ {n T} (p + 1) \boldsymbol {R} ^ {- 1} (p)}{1 + K (p + 1)}
$$

con:

$$ \dots $$

$$
K (p + 1) = \boldsymbol {x} ^ {n T} (p + 1) \boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1)
$$

## Applicazione - cont.

## D'altra parte abbiamo

$$ \dots $$

$$
\boldsymbol {X} (p + 1) = \left[ \boldsymbol {X} (p) \boldsymbol {x} ^ {n} (p + 1) \right], \quad \boldsymbol {y} (p + 1) = \left[ \boldsymbol {y} (p) \theta (p + 1) \right] ^ {T}
$$

implicando:

$$ \dots $$

$$
\boldsymbol {X} (p + 1) \boldsymbol {y} (p + 1) = \boldsymbol {X} (p) \boldsymbol {y} (p) + \theta (p + 1) \boldsymbol {x} ^ {n} (p + 1)
$$

Poiché ${ \pmb a } ( p + 1 ) = { \pmb R } ^ { - 1 } ( p + 1 ) { \pmb X } ( p + 1 ) { \pmb y } ( p + 1 )$, si ottiene:

$$ \dots $$

$$
\boldsymbol {a} (p + 1) = \left[ \boldsymbol {I} _ {n} - \frac {\boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1)}{1 + K (p + 1)} \boldsymbol {x} ^ {n T} (p + 1) \right]
$$

$$ \dots $$

$$
\left[ \boldsymbol {a} (p) + \theta (p + 1) \boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1) \right]
$$

L'operazione presenta una complessità $\mathcal { O } ( n ^ { 2 } )$, risultando indipendente (e non scalabile con) $p .$.

## Adattività in LS

Al fine di gestire situazioni in cui l'ambiente circostante può essere (lentamente) variabile nel tempo, è opportuno forzare i dati storici a pesare meno rispetto ai dati più recenti ("freschi").

Un metodo per ottenere tale comportamento è l'utilizzo della **media mobile esponenziale**, la cui idea principale consiste nell'adottare la seguente funzione di costo:

$$
\sum_ {i = 1} ^ {p} w ^ {p - i} \left[ \pmb {\mathscr {a}} ^ {T} \pmb {x} ^ {n} (i) - \theta (i) \right] ^ {2}
$$

Il peso $w < 1$ regola la velocità con cui il passato viene "dimenticato" dal modello.

Minimizzando rispetto a $a$ si ottiene l'**LS mediato esponenzialmente**:

$$
\boldsymbol {a} = \left[ \sum_ {i = 1} ^ {p} w ^ {p - i} \boldsymbol {x} ^ {n} (i) \boldsymbol {x} ^ {n T} (i) \right] ^ {- 1} \sum_ {i = 1} ^ {p} w ^ {p - i} \boldsymbol {x} ^ {n} (i) \theta (i)
$$

Questa formulazione è suscettibile di un'implementazione ricorsiva grazie all'applicazione del lemma di Sherman-Morrison.

## Generalizzazione

Supponiamo ora che, mantenendo le stesse condizioni precedentemente analizzate, si desideri trovare un LS nella forma più generale:

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} + b
$$

Calcoli analitici, sebbene articolati, portano alla forma **LMS generale**:

$$
\boldsymbol {a} _ {\text { LMS }} = (\boldsymbol {X} _ {0} \boldsymbol {X} _ {0} ^ {T}) ^ {- 1} \boldsymbol {X} _ {0} \boldsymbol {y} _ {0}, \qquad b _ {\text { LMS }} = \underbrace {\frac {1}{p} \sum_ {i = 1} ^ {p} \theta (i)} _ {\widetilde {\theta}} - \frac {1}{p} \boldsymbol {1} _ {p} ^ {T} \boldsymbol {X} ^ {T} \boldsymbol {a} _ {\text { LMS }}
$$

dove ${ \bf 1 } _ { p }$ è un vettore di tutti uno $p -$ dimensionale e

$$
\boldsymbol {X} _ {0} = \left[ \begin{array}{c c c} x _ {1} (1) - \overline {{x}} _ {1} & \dots & x _ {1} (p) - \overline {{x}} _ {1} \\ \dots & \dots & \dots \\ x _ {n} (1) - \overline {{x}} _ {n} & \dots & x _ {n} (p) - \overline {{x}} _ {n} \end{array} \right] \in \mathbb {R} ^ {n \times p}, \quad \boldsymbol {y} _ {0} = \left[ y _ {1} - \overline {{\theta}}, \ldots , y _ {p} - \overline {{\theta}} \right] ^ {T}
$$

con

$$
\overline {{x}} _ {k} = \frac {1}{p} \sum_ {i = 1} ^ {p} x _ {k} (i) \Longleftrightarrow \overline {{\mathbf {x}}} = \frac {1}{p} \sum_ {i = 1} ^ {p} \mathbf {x} ^ {n} (i), \quad \mathbf {X} _ {0} = \mathbf {X} - \overline {{\mathbf {x}}} \mathbf {1} _ {p} ^ {T}
$$
