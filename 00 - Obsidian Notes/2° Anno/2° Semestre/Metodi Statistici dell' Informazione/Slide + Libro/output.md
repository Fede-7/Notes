## Elementi di Statistica inferenziale

Marco Lops 

lops@unina.it 

https://docenti.unina.it/marco.lops 

## Inferenza Bayesiana

Assumiamo di avere un campione di dimensione n, diciamo $\pmb { x } \in \mathbb { R } ^ { n }$ 

Assumiamo che questo campione sia il risultato di un esperimento casuale, il che significa che il ri-campionamento porterebbe a un set di risultati diverso, diciamo $\pmb { x } ^ { \prime } \in \mathbb { R } ^ { n }$; 

L'inferenza statistica è il processo di utilizzo dell'analisi dei dati per dedurre proprietà di una distribuzione di probabilità sottostante, ovvero definire una legge che qualsiasi campione - estratto casualmente - dovrebbe rispettare; 

La statistica inferenziale può essere contrastata con la statistica descrittiva. La statistica descrittiva si occupa esclusivamente delle proprietà dei dati osservati e non si basa sull'assunzione che i dati provengano da una popolazione più ampia.

Gli obiettivi di base dell'inferenza statistica sono il Test delle Ipotesi e la Stima dei Parametri. 

## Inferenza Bayesiana

Assumiamo di avere un set di dati $\pmb { x } ^ { n } \in \mathcal { X } ^ { n } \subseteq \mathbb { R } ^ { n }$; 

Sappiamo che la media campionaria è definita come 

$$
\overline {{x}} _ {n} = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i}
$$

La legge dei grandi numeri ci dice che ${ \overline { { X } } } _ { n } \to \mathbb { E } [ X ]$ (il tipo di convergenza dipende dalla legge statistica sottostante), nel senso che, denotando $X ^ { n }$ un campione casuale estratto dalla popolazione, abbiamo 

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} \to \mathbb {E} [ X ]
$$

La convergenza debole (cioè, convergenza in probabilità) ci dice che la frequenza dei campioni la cui media campionaria si discosta significativamente da $\mathbb { E } [ X ]$ è piccola quanto desideriamo; 

La convergenza forte afferma che nel limite la probabilità di discostarsi da $\mathbb { E } [ X ]$ è zero; 

La convergenza in media quadratica (Mean-Square convergence) afferma che 

$$
\lim _ {n} \mathbb {E} \left[ \left(\overline {{X}} _ {n} - \mathbb {E} [ X ]\right) ^ {2} \right] = 0
$$

## Inferenza Bayesiana

Assumiamo che $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$, con $\mathcal { X } = ( a _ { 1 } , \dotsc , a _ { M } )$ discreto e finito; 

sappiamo che 

$$
\overline {{x}} _ {n} = \sum_ {i = 1} ^ {M} a _ {i} f _ {n} (a _ {i})
$$

dove $f _ { n } ( a _ { i } )$ è la frazione dei valori del campione che producono $a _ { j }$; 

Sappiamo che, se $\boldsymbol { x } \in \mathcal { X }$ è una variabile casuale con pmf $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$, allora: 

$$
\mathbb {E} [ X ] = \sum_ {i = 1} ^ {M} a _ {i} p _ {X} (a _ {i})
$$

Di conseguenza, abbiamo 

$$
| \overline {{x}} _ {n} - \mathbb {E} [ X ] | \leq \sum_ {i = 1} ^ {M} | a _ {i} | | f _ {n} (a _ {i}) - p _ {X} (a _ {i}) |
$$

Si noti che se possiamo affermare che $f _ { n } ( a _ { i } ) \to p \chi ( a _ { i } )$ (in qualche senso), allora possiamo inferire che $\pmb { x } ^ { n }$ è un campione da una popolazione i cui elementi sono estratti da un vettore casuale $X ^ { n }$ con densità marginale $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$ 

## Inferenza Bayesiana

Assumiamo che $\pmb { x } ^ { n }$ sia estratto da $X ^ { n }$, un set di n variabili casuali iid con marginale sconosciuta $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$ • 

La frequenza di occorrenza dell'evento $X _ { k } = a _ { i }$ è essa stessa casuale. Se $N _ { j }$ è il numero di volte in cui $X _ { k } = a _ { i }$ nel nostro campione n-dimensionale, abbiamo: 

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

### Tipi di convergenza

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

abbiamo, per n crescentemente grandi: 

$$
\binom{n}{n q (a _ {i})} \sim 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))}
$$

### Tipi di convergenza

Consideriamo ora un valore $a _ { j }$ per il quale $q ( a _ { i } ) \neq p _ { X } ( a _ { i } )$ 

Quando n diventa grande abbiamo: 

$$
\begin{array}{r l} \operatorname * {P r} \big \{N _ {i} = n q (a _ {i}) \big \} & \sim 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} p _ {X} (a _ {i}) ^ {n q (a _ {i})} \left[ 1 - p _ {X} (a _ {i}) \right] ^ {n (1 - q (a _ {i}))} \\ & = 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} 2 ^ {n [ q (a _ {i}) \log p _ {X} (a _ {i}) + (1 - q (a _ {i})) \log (1 - p _ {X} (a _ {i})) ]} \\ & = 2 ^ {n \left[ q (a _ {i}) \log \frac {p _ {X} (a _ {i})}{q (a _ {i})} + (1 - q (a _ {i})) \log \frac {1 - p _ {X} (a _ {i})}{1 - q (a _ {i})} \right]} = 2 ^ {- n D _ {i}} \end{array}
$$

con 

$$
D _ {i} = q (a _ {i}) \log \frac {q (a _ {i})}{p _ {X} (a _ {i})} + [ 1 - q (a _ {i}) ] \log \frac {1 - q (a _ {i})}{1 - p _ {X} (a _ {i})} > 0
$$

Concludiamo quindi che la probabilità che la frequenza di occorrenza non sia uguale alla vera probabilità tende a zero esponenzialmente con n. 

Ciò implica che $f _ { n } ( a _ { i } ) \to p \chi ( a _ { i } )$ quasi certamente. 

# 6. Statistica Inferenziale e Stima

Assumiamo di avere un campione $\pmb { x } ^ { n } \in \mathcal { X } ^ { n } , \mathcal { X } = \{ a _ { 1 } , . . . , a _ { M } \}$ estratto da un vettore casuale $X ^ { n }$ di pmf sconosciuta; 

Se calcoliamo le frequenze di occorrenza: 

$$
f _ {n} (a _ {i}) = \frac {\# \text {   of   elements   equal   to   } a _ {i}}{n}, \qquad i = 1, \ldots , M
$$

abbiamo: 

$$
\operatorname * {P r} \left\{\lim _ {n \rightarrow \infty} \frac {N _ {i}}{n} = \lim _ {n \rightarrow \infty} f _ {n} (a _ {i}) \right\} = 1
$$

Ciò implica che qualsiasi altro campione, diciamo $\pmb { y } ^ { n }$, estratto dalla stessa popolazione mostrerà, per $n  \infty$, lo stesso comportamento statistico. 

Non c'è bisogno di dire che avremo che per ogni funzione $f ( \cdot )$ dei dati 

$$
\operatorname * {P r} \left\{\lim _ {n \rightarrow \infty} f (\boldsymbol {X} ^ {n}) = \lim _ {n \rightarrow \infty} f (\boldsymbol {x} ^ {n}) \right\} = 1
$$

Così, la media campionaria converge con probabilità uno alla media statistica della popolazione.Questa proprietà è anche definita nella statistica inferenziale come forte coerenza.

## Statistica Inferenziale

L'idea principale è che, una volta osservato un campione sufficientemente ampio di una data popolazione di dati, possiamo inferire un numero di caratteristiche che qualsiasi altro campione dovrebbe rispettare;

Alcune conoscenze pregresse riguardo alle statistiche della popolazione da cui il campione è estratto possono essere note a priori;

Ad esempio, potremmo assumere che il campione sia estratto da una popolazione la cui distribuzione è nota fino a un insieme di parametri;

Per iniziare, assumiamo che il campione sia noto come estratto da una famiglia di distribuzioni, indicizzata da un parametro $\theta$, che deve essere stimato;

Domanda: Come elaboriamo il dataset disponibile per inferire il valore del parametro?

### Teoria della decisione e Costi Bayesiani

Assumiamo di avere un dataset $\llbracket\text{MATHINLINE\_0204}\rrbracket$ che è una realizzazione di un vettore casuale $\llbracket\text{MATHINLINE\_0205}\rrbracket$;

Assumiamo che - in base allo stato della natura - i dati possano provenire da una qualsiasi delle $M$ diverse leggi di probabilità.

Abbiamo quindi un insieme di $M$ ipotesi diverse e mutuamente esclusive $\llbracket\text{MATHINLINE\_0206}\rrbracket$, ciascuna delle quali definisce una diversa legge condizionale per il set di dati, ovvero:

$\llbracket\text{MATHBLOCK\_0018}\rrbracket$

Assumiamo che il vettore casuale $\llbracket\text{MATHINLINE\_0207}\rrbracket$ sia estratto da una famiglia di distribuzioni con pmf $\llbracket\text{MATHINLINE\_0208}\rrbracket$, dove il valore di $\llbracket\text{MATHINLINE\_0209}\rrbracket$ è sconosciuto;

Assumiamo anche che le probabilità a priori - $\llbracket\text{MATHINLINE\_0210}\rrbracket$ - di questi stati della natura siano assegnate;

Una regola di decisione è una mappa:

$\llbracket\text{MATHBLOCK\_0019}\rrbracket$

che ci permette di decidere quale dei possibili stati della natura sia quello effettivamente in vigore.

### Teoria della decisione e Costi Bayesiani

Assumiamo di definire la seguente matrice di costo $\llbracket\text{MATHINLINE\_0211}\rrbracket$

$\llbracket\text{MATHBLOCK\_0020}\rrbracket$

dove $\llbracket\text{MATHINLINE\_0212}\rrbracket$ è il costo associato all'evento in cui prendiamo la decisione $\llbracket\text{MATHINLINE\_0213}\rrbracket$ e lo stato della natura è $\llbracket\text{MATHINLINE\_0214}\rrbracket$

Definiamo il rischio Bayesiano medio come:

$\llbracket\text{MATHBLOCK\_0021}\rrbracket$

Data una matrice di costo $C$, una regola di decisione ottimale è una mappa $\llbracket\text{MATHINLINE\_0215}\rrbracket$ che minimizza il rischio Bayesiano;

Si noti che, se $\llbracket\text{MATHINLINE\_0216}\rrbracket$, $M$ e $\llbracket\text{MATHINLINE\_0217}\rrbracket$, allora

$\llbracket\text{MATHBLOCK\_0022}\rrbracket$

ovvero il rischio Bayesiano medio coincide con la probabilità di commettere un errore di classificazione.

### Classificazione Binaria (Discreta e Continua)

Assumiamo per il momento che $\llbracket\text{MATHINLINE\_0218}\rrbracket$, che $\llbracket\text{MATHINLINE\_0219}\rrbracket$ e $\llbracket\text{MATHINLINE\_0220}\rrbracket$ in modo che

$\llbracket\text{MATHBLOCK\_0023}\rrbracket$

Progettare una regola di decisione implica determinare una partizione di $\llbracket\text{MATHINLINE\_0221}\rrbracket$ in due sottoinsiemi, $\llbracket\text{MATHINLINE\_0222}\rrbracket$ e $\llbracket\text{MATHINLINE\_0223}\rrbracket$, tali che

$\llbracket\text{MATHBLOCK\_0024}\rrbracket$

La corrispondente probabilità di errore è quindi scritta come:

$\llbracket\text{MATHBLOCK\_0025}\rrbracket$

Vogliamo determinare la legge di decisione ottimale (cioè, con la minima probabilità di errore) per questo problema di classificazione binaria.

## Classificazione Binaria: leggi di dati discreti

Assumiamo che le osservazioni $\llbracket\text{MATHINLINE\_0224}\rrbracket$ siano un vettore casuale discreto con pmf condizionali dati $\llbracket\text{MATHINLINE\_0225}\rrbracket$;

Abbiamo ovviamente $\llbracket\text{MATHINLINE\_0226}\rrbracket$ dove la probabilità di errore è scritta come

$\llbracket\text{MATHBLOCK\_0026}\rrbracket$

che è minima quando la quantità tra parentesi è massima.

Otteniamo quindi la seguente regola di decisione ottimale:

$\llbracket\text{MATHBLOCK\_0027}\rrbracket$

o equivalentemente

$\llbracket\text{MATHBLOCK\_0028}\rrbracket$

La quantità $\llbracket\text{MATHINLINE\_0227}\rrbracket$ sul lato sinistro (LHS) è chiamata rapporto di verosimiglianza tra le due ipotesi alternative.

### Classificazione Binaria (Discreta e Continua)

La precedente regola di decisione è nota anche come regola di decisione a Massima Probabilità a Posteriori (MAP), in quanto, dalla legge di Bayes:

$\llbracket\text{MATHBLOCK\_0029}\rrbracket$

mostrando che la regola decide per l'ipotesi la cui probabilità a posteriori data dai dati osservati è massima.

Nel caso speciale in cui le due ipotesi siano ugualmente probabili, la soglia è $\llbracket\text{MATHINLINE\_0228}\rrbracket$ e la regola di decisione diventa una regola di decisione a Massima Verosimiglianza (ML).

Poiché le probabilità di errore condizionali sono:

$\llbracket\text{MATHBLOCK\_0030}\rrbracket$

la probabilità di errore è

$\llbracket\text{MATHBLOCK\_0031}\rrbracket$

## Esempio: classificazione di sorgenti binarieAssumiamo che le osservazioni siano variabili binarie iid che possono provenire con probabilità uguali da una sorgente con ${ \mathbb { P } } \left\{ X _ { i } = 1 \right\} = p _ { 1 }$ o da una sorgente con ${ \mathbb { P } } \left\{ X _ { i } = 1 \right\} = p _ { 2 }$ , con $p _ { 1 } > p _ { 2 }$ 

Abbiamo quindi: 

$$
p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {i}) = p _ {i} ^ {w _ {H} (\boldsymbol {x} ^ {n})} (1 - p _ {i}) ^ {n - w _ {H} (\boldsymbol {x} ^ {n})}
$$

dove $w _ { H } ( \pmb { x } ^ { n } )$ è il peso di Hamming della sequenza binaria osservata $\pmb { x } ^ { n }$ coincidente con il numero dei suoi 1. 

Il test di probabilità di errore minima è 

$$
\left(\frac {p _ {1}}{p _ {2}}\right) ^ {w _ {H} (x ^ {n})} \left[ \frac {(1 - p _ {1})}{(1 - p _ {2})} \right] ^ {n - w _ {H} (x ^ {n})} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 1
$$

o, equivalentemente 

$$
w _ {H} (\boldsymbol {x} ^ {n}) \ln \left(\frac {p _ {1}}{p _ {2}}\right) + (n - w _ {H} (\boldsymbol {x} ^ {n})) \ln \left(\frac {1 - p _ {1}}{1 - p _ {2}}\right) \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 0
$$

che si riduce a 

$$
w _ {H} \big (\boldsymbol {x} ^ {n} \big) \left[ \ln \left(\frac {p _ {1}}{1 - p _ {1}} \frac {1 - p _ {2}}{p _ {2}}\right) \right] \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} n \ln \left(\frac {1 - p _ {2}}{1 - p _ {1}}\right)
$$

### Classificazione Binaria (Discreta e Continua)

Si noti che, poiché $p _ { 1 } > p _ { 2 }$ , tutti i logaritmi sono non negativi; 

Il test può quindi essere riscritto nella forma 

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

### Classificazione Binaria (Discreta e Continua)

Assumiamo ora che i dati possano essere estratti da M possibili leggi di probabilità continue, dove ci viene fornito un insieme di funzioni di densità di probabilità condizionali candidate $\{ f _ { \pmb { X } ^ { n } | H _ { i } } ( \pmb { x } ^ { n } | \pmb { H } _ { i } ) \} _ { i = 1 } ^ { M }$ ; 

L'unica differenza con il caso discreto è che ora 

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

La quantità $L ( \pmb { x } ^ { n } )$ sul lato sinistro (LHS) è di nuovo chiamata rapporto di verosimiglianza tra le due ipotesi alternative. 

### Test di ipotesi e Neyman-Pearson

Assumiamo che il set di dati $\pmb { x } ^ { n }$ abbia la stessa probabilità di essere una realizzazione di un vettore casuale Gaussiano indipendente i cui elementi hanno la stessa varianza e medie diverse $\mu _ { 1 }$ e $\mu _ { 2 } < \mu _ { 1 }$ ; 

Poiché $\begin{array} { r } { f _ { X ^ { n } | H _ { i } } ( x ^ { n } | H _ { i } ) = \prod _ { k = 1 } ^ { n } \frac { 1 } { \sqrt { 2 \pi \sigma ^ { 2 } } } e ^ { - \frac { ( x _ { k } - \mu _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } } } \end{array}$ il test ottimo è scritto come 

$$
L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2})} = e ^ {\frac {\sum_ {k = 1} ^ {n} (x _ {k} - \mu_ {2}) ^ {2} - (x _ {k} - \mu_ {1}) ^ {2}}{2 \sigma^ {2}}} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 1
$$

Prendendo il logaritmo su entrambi i lati ed elaborando otteniamo il test equivalente 

$$
\frac {1}{n} \sum_ {k = 1} ^ {n} x _ {k} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} \frac {\mu_ {1} + \mu_ {2}}{2} = \eta
$$

Le quantità $\sum x _ { k }$ per questo problema e $w _ { H } ( \pmb x ^ { n } )$ per il precedente sono anche riferite come statistiche sufficienti nel linguaggio della statistica inferenziale. 

### Classificazione Binaria (Discreta e Continua)

Si noti che, sotto $H _ { j }$ , la statistica del test $\begin{array} { r } { Z _ { n } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } X _ { i } } \end{array}$ è Gaussiana con media e varianza date da: 

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

Poiché $\mu _ { 1 } - \mu _ { 2 } > 0$ , abbiamo anche $\mathbb { P } ( e | H _ { 1 } ) = \mathbb { P } ( e | H _ { 2 } ) = Q \left( { \sqrt { n } } { \frac { \mu _ { 1 } - \mu _ { 2 } } { 2 \sigma } } \right)$ , dove 

$$
\mathbb {P} (e) = Q \left(\sqrt {n} \frac {\mu_ {1} - \mu_ {2}}{2 \sigma}\right)\rightarrow 0 \quad \text { as } n \rightarrow \infty
$$

### Test di ipotesi e Neyman-Pearson

Esistono numerose situazioni in cui dobbiamo prendere una decisione tra due ipotesi, ma non abbiamo mezzi per assegnare la matrice dei costi C né le probabilità a priori; 

Gli esempi includono un numero di situazioni di interesse pratico, ovvero: 

Rilevamento precoce di minacce alla sicurezza di un'area pattugliata; 

Rilevamento di intrusioni in server/domini protetti su internet; 

Rilevamento (e localizzazione) di ostacoli nei sistemi Advance Driver Assistance Systems (ADAS); 

Controllo del traffico aereo; 

Innumerevoli applicazioni militari; 

In tutte le situazioni sopra citate, è praticamente impossibile assegnare un costo a un errore di giudizio sullo "stato della natura", ovvero a una decisione errata tra le due ipotesi "tutto normale" o "qualcosa sta accadendo"; 

È anche di poca importanza assegnare una probabilità a priori che "anomalie statistiche" nel set di dati siano presenti. 

### Test di ipotesi e Neyman-Pearson

0 Innanzitutto, definiamo un'ipotesi nulla, tradizionalmente denotata $H _ { 0 }$ , che il set di dati osservati $\pmb { x } ^ { n }$ sia una realizzazione di un vettore casuale con una distribuzione condizionale nota, con pmf/pdf $p _ { X ^ { n } | H _ { 0 } } ( { \pmb x } ^ { n } | H _ { 0 } ) / f _ { { \pmb X } ^ { n } | H _ { 0 } } ( { \pmb x } ^ { n } | H _ { 0 } )$ ; 

Vogliamo decidere se o meno, dati i dati osservati $\pmb { x } ^ { n }$ , l'ipotesi nulla debba essere rifiutata a favore di una legge diversa, diciamo $p _ { X ^ { n } \mid H _ { 1 } } ( { \pmb x } ^ { n } | H _ { 1 } ) / f _ { { \pmb X } ^ { n } \mid H _ { 1 } } ( { \pmb x } ^ { n } | H _ { 1 } )$ ;Per quanto riguarda la classificazione binaria, dobbiamo partizionare il dominio $\mathcal { X } ^ { n }$ in due regioni di decisione, ma il precedente framework di Bayes non è più applicabile qui a causa della mancanza di informazioni a priori sufficienti;

Nel progettare una regola di decisione (ovvero un test), definiamo quindi:

L'errore di tipo-I del test, o probabilità di falso allarme, come

$$
\mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 1 | H _ {0} \right\} = \left\{ \begin{array}{l l} \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0}) d \boldsymbol {x} ^ {n} & \text { Continuous   Data } \\ \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {1}} p _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0}) & \text { Discrete   Data } \end{array} \right.
$$

La potenza del test, ovvero:

$$
1 - \beta = \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 1 | H _ {1} \right\} = \left\{ \begin{array}{l l} \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) d \boldsymbol {x} ^ {n} \\ \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {1}} p _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) \end{array} \right.
$$

Dati Continui

Dati Discreti

### Test di ipotesi e Neyman-Pearson

Dato il framework delineato nella slide precedente, un test di Neyman-Pearson è il risultato della seguente ottimizzazione vincolata:

$$
\text { Determine } \Omega_ {1} \colon \left\{ \begin{array}{l l} 1 - \beta & \text { maximum } \\ \text { subject   to } & \text { type - 1   error } \leq \alpha \end{array} \right.
$$

L'esistenza della soluzione di tale problema vincolato costituisce il nucleo del lemma di Neyman-Pearson;

Il test risultante è il test del rapporto di verosimiglianza (likelihood ratio test)

$$
L \left(\boldsymbol {x} ^ {n}\right) \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta L \left(\boldsymbol {x} ^ {n}\right) = \left\{ \begin{array}{l l} \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (x ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {0}} (x ^ {n} | H _ {0})} & \text { Continuous   data } \\ \frac {p _ {\boldsymbol {X} ^ {n} | H _ {1}} (x ^ {n} | H _ {1})}{p _ {\boldsymbol {X} ^ {n} | H _ {0}} (x ^ {n} | H _ {0})} & \text { Discrete   data } \end{array} \right.
$$

La soglia $\eta$ dovrebbe essere scelta come soluzione dell'equazione:

$$
\mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) > \eta | H _ {0} \right\} = \alpha
$$

Si noti che l'applicazione di qualsiasi funzione monotonicamente crescente a entrambi i lati del test precedente non ne altera l'ottimalità, per cui possiamo introdurre equivalentemente la log-verosimiglianza ln $L \left( \pmb { x } ^ { n } \right) = \Lambda ( \pmb { x } ^ { n } )$ e confrontarla con una soglia determinata in modo nuovo.

### Test di ipotesi e Neyman-Pearson

Assumiamo che l'ipotesi nulla sia che le osservazioni siano iid Gaussiane con media zero e varianza data, ovvero $X _ { i } \sim \mathcal { N } ( 0 , \sigma ^ { 2 } )$, mentre la sua alternativa è $X _ { i } \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$;

Seguendo la slide 18, il test del rapporto di verosimiglianza si legge

$$
L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0})} = e ^ {\frac {\sum_ {k = 1} ^ {n} (x _ {k} - \mu) ^ {2} - x _ {k} ^ {2}}{2 \sigma^ {2}}} \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta
$$

dove ora η dovrebbe essere scelto in modo da soddisfare il vincolo.

Prendendo il logaritmo su entrambi i lati, semplificando e assorbendo in una nuova soglia (sconosciuta) $\eta ^ { \prime }$ tutte le quantità indipendenti dai dati, otteniamo il test equivalente

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta^ {\prime}
$$

dove $\eta ^ { \prime }$ dovrebbe essere scelto in modo da garantire che la probabilità di errore di tipo-I sia uguale al valore di progetto α.

### Test di ipotesi e Neyman-Pearson

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

## Inferenza Bayesiana

Assumiamo di avere un dataset $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ che è una realizzazione di un vettore casuale $X ^ { n }$;

Assumiamo che il vettore casuale $X ^ { n }$ sia estratto da una famiglia di distribuzioni con pmf/pdf $p _ { X ^ { n } | \Theta } ( \pmb { x } ^ { n } | \theta ) / f _ { \pmb { X } ^ { n } | \Theta } ( \pmb { x } ^ { n } | \theta )$, dove il valore di $\theta$ è sconosciuto;

θ è tipicamente un parametro continuo, che può essere una realizzazione di una variabile casuale continua Θ con marginale nota $f _ { \Theta } ( \theta )$ (impostazione Bayesiana) o una quantità deterministica sconosciuta che assume valori in un insieme continuo;

Domanda: Come stimiamo θ basandoci sul campione raccolto?

Si osservi che, nell'impostazione Bayesiana, l'applicazione diretta della regola di Bayes fornisce:

$$
f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) = \left\{ \begin{array}{c} p _ {\boldsymbol {X} ^ {n} | \Theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) \\ \hline \int p _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \\ f _ {\boldsymbol {X} ^ {n} | \Theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) \\ \hline \int f _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \end{array} \right.
$$

dati discreti

dati continui

Si osservi che, se $\Theta$ è discreto, quanto sopra diventa un problema di classificazione. Si noti inoltre che nell'equazione sopra abbiamo usato il fatto che

$$
p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \int p _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \quad f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \int f _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta
$$

## Inferenza Bayesiana

Un estimatore del parametro $\theta$ è una variabile casuale ${ \widehat { \Theta } } ( X ^ { n } )$ — le cui realizzazioni sono $\widehat { \theta } ( { \pmb x } ^ { n } )$ — che tenta di "indovinare" il valore di $\theta$ basandosi su un'osservazione $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$

Al fine di progettare un estimatore, definiamo prima un Risk di Bayes medio, ovvero:

$$
\mathcal {R} = \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right] = \mathbb {E} _ {\boldsymbol {X} ^ {n}} \left[ \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \mid \boldsymbol {X} ^ {n} \right] \right]
$$

dove $C ( \cdot )$ è una funzione di costo adeguatamente definita.

Un estimatore ottimo è quello che minimizza il risk di Bayes, ovvero:

$$
\widehat {\Theta} _ {\text { opt }} (\boldsymbol {X} ^ {n}) = \arg \min \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right]
$$

Poiché

$$
\mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right] = \sum_ {\boldsymbol {x} ^ {n} \in \mathcal {X} ^ {n}} p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) \int C (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta
$$

una stima Bayes-ottimale operante su un campione osservato $\pmb { x } ^ { n }$ è definita come:

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \arg \min \int C (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta
$$## Estimatore del Minimo Errore Quadratico Medio (MMSEE)

Assumiamo che $C ( \widehat { \Theta } ( X ^ { n } ) - \Theta ) = ( \widehat { \Theta } ( X ^ { n } ) - \Theta ) ^ { 2 }$ 

L'estimatore Bayes-ottimale può essere derivato come la soluzione dell'equazione 

$$
\frac {\partial}{\partial \widehat {\theta} (\boldsymbol {x} ^ {n})} \int (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) ^ {2} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta = 0
$$

Otteniamo quindi la stima 

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \int \theta f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta = \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ]
$$

che corrisponde certamente a un minimo data la convessità del rischio di Bayes scelto. 

### Estimatori (MMSE, MAP)

Assumiamo che $X ^ { n } \in \{ 0 , 1 \} ^ { n }$ sia condizionalmente Bernoulli con parametro $\beta ,$, con $B \sim \mathcal { U } ( 0 , 1 )$ 

Il peso di Hamming $w ( \pmb { x } ^ { n } )$ di una sequenza binaria è il numero di uno che contiene. Abbiamo: 

$$
p _ {\boldsymbol {X} ^ {n} | B} (\boldsymbol {x} ^ {n} | \beta) = \beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}
$$

Facendo la media su B otteniamo la legge non condizionata: 

$$
p \mathbf {x} ^ {n} (\mathbf {x} ^ {n}) = \int_ {0} ^ {1} \beta^ {w (\mathbf {x} ^ {n})} (1 - \beta) ^ {n - w (\mathbf {x} ^ {n})} d \beta = \frac {\Gamma (w + 1) \Gamma (n - w + 1)}{\Gamma (n + 2)} = \frac {1}{\binom{n + 1}{w (\mathbf {x} ^ {n})}}
$$

La legge condizionata è quindi 

$$
f _ {B | \boldsymbol {X} ^ {n}} (\beta | \boldsymbol {x} ^ {n}) = \frac {\beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}}{p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})} = \frac {\beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}}{\binom{n + 1}{w (\boldsymbol {x} ^ {n})}}
$$

### Estimatori (MMSE, MAP)

La stima MMSE è quindi 

$$
\frac {1}{p \boldsymbol {x} ^ {n} (\boldsymbol {x} ^ {n})} \int_ {0} ^ {1} \beta^ {w (\boldsymbol {x} ^ {n}) + 1} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})} d \beta
$$

Risolvendo l'integrale si ottiene

$$
\hat {\beta} _ {\text {MMSE}} (\boldsymbol {x} ^ {n}) = \frac {\Gamma (w + 2) \Gamma (n - w + 1)}{\Gamma (n + 3)} \frac {1}{\binom{n + 1}{w (\boldsymbol {x} ^ {n})}} = \frac {w (\boldsymbol {x} ^ {n}) + 1}{n + 2}
$$

che è la stima ottenuta attraverso l'estimatore MMSE: 

$$
\hat {B} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) = \frac {w (\boldsymbol {X} ^ {n}) + 1}{n + 2}
$$

## Estimatore a Massima Verosimiglianza a Posteriori (MAPE)

Assumiamo ora la seguente funzione di costo: 

$$
C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) = \Pi \left(\frac {\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta}{\epsilon}\right) = \left\{ \begin{array}{l l} 0 & \left| \widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta \right| <   \frac {\epsilon}{2} \\ 1 & \text { otherwise } \end{array} \right.
$$

È ovvio che, poiché  è arbitrariamente piccola, ciò si traduce nell'estimatore MAP 

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

### Estimatori (MMSE, MAP)

Notiamo preliminarmente che: 

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

Concludiamo che l'MMSEE è un estimatore distorto (biased), mentre il MAP non lo è; 

Si noti che l'MMSEE è asintoticamente non distorto, poiché l'errore sistematico svanisce all'aumentare di n. 

### Estimatori (MMSE, MAP)

Dopo lunghi - seppur elementari - calcoli, troviamo: 

$$
\mathbb {E} \left[ (B _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) - B) ^ {2} \right] = \overline {{e ^ {2}}} _ {\text { MMSE }} = \frac {n - 2}{6 (n + 2) ^ {2}}
$$

$$
\mathbb {E} \left[ (B _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) - B) ^ {2} \right] = \overline {{e ^ {2}}} _ {\mathrm{MAP}} = \frac {1}{6 n}
$$

Non c'è bisogno di dire che abbiamo $\overline { { e ^ { 2 } } } _ { \mathsf { M M S E } } < \overline { { e ^ { 2 } } } _ { \mathsf { M A P } } \ \forall n$ 

Poiché entrambi gli MSE tendono a zero all'aumentare di n, abbiamo che i due estimatori sono definiti MS consistenti, nel senso che l'errore casuale ha un valore MS asintoticamente zero; 

Sfruttando la disuguaglianza di Tchebyshev, abbiamo che entrambi gli estimatori tendono a B in probabilità (consistenza, detta anche consistenza debole). Se ${ \widehat { B } } ( X ^ { n } )$ è uno dei due estimatori, abbiamo quindi: 

$$
\forall \epsilon > 0 \quad \lim _ {n \rightarrow \infty} \operatorname * {P r} \left\{\left| \widehat {B} (\boldsymbol {X} ^ {n}) - B \right| > \epsilon \right\} = 0
$$

Si può dimostrare che entrambi gli estimatori sono fortemente consistenti, nel senso che ${ \widehat { B } } ( X ^ { n } ) \to B$ quasi certamente. 

## Inferenza Bayesiana

Consideriamo un campione $\pmb { x } ^ { n }$ estratto da un vettore casuale $\pmb { X } ^ { n } \in \mathcal { X } ^ { n } \subseteq \mathbb { R } ^ { n }$ 

$\mathcal { X } ^ { n }$ può essere discreto o continuo, ma assumiamo che $X ^ { n }$ abbia una pdf (pmf, nel caso discreto) nota appartenere a una famiglia con prior nota. Quindi, assumiamo la conoscenza della pdf congiunta $f _ { \pmb { X } ^ { n } , \Theta } ( \pmb { x } ^ { n } , \theta )$ e del parametro prio $f _ { \Theta } ( \theta )$ 

Vogliamo inferire il valore del parametro di $\theta$ per la realizzazione osservata $\pmb { x } ^ { n }$. La stima MMSE e la stima MAP sono quindi definite come 

$$
\widehat {\theta} _ {\mathrm{MMSE}} (\boldsymbol {x} ^ {n}) = \mathbb {E} \left[ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right] = \int \theta f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta , \quad \widehat {\theta} _ {\mathrm{MAP}} (\boldsymbol {x} ^ {n}) = \arg \max _ {\theta} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n})
$$

Un estimatore è non distorto (unbiased) se $\mathbb { E } \left[ \widehat { \Theta } ( \pmb { \cal X } ^ { n } ) - \Theta \right] = 0 ;$ 

Un estimatore è asintoticamente non distorto se è non distorto solo nel limite di una dimensione campionaria infinita; 

Un estimatore è consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ in probabilità; 

Un estimatore è MS consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ in media quadratica; 

Un estimatore è fortemente consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ quasi certamente. 

### Estimatori (MMSE, MAP)

Sia $\pmb { x } ^ { n }$ estratto da $X ^ { n }$ con: 

$$
f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \exp \left[ - \frac {(x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}} \right]
$$

Sia $\mu$ una realizzazione di $M \sim \mathcal N ( 0 , \sigma _ { M } ^ { 2 } )$ 

Vogliamo inferire il valore $\mu$ di M appartenente all'osservazione $\pmb { x } ^ { n }$ di $X ^ { n }$ 

Si noti che la densità a posteriori della media è: 

$$
f _ {M | \boldsymbol {X} ^ {n}} (\mu | \boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) f _ {M} (\mu)}{f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})} = \mathcal {N} \left(\frac {\sum_ {i = 1} ^ {n} x _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}, \frac {1}{\frac {n}{\sigma^ {2}} + \frac {1}{\sigma_ {M} ^ {2}}}\right)
$$

In altre parole, il prior coniugato della media di una distribuzione Gaussiana è di nuovo Gaussiano; 

Abbiamo quindi che la stima MMSE della media è 

$$
\widehat {\mu} _ {\text { MMSE }} (\boldsymbol {x} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} x _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}} \Longleftrightarrow \widehat {M} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}
$$

Consideriamo ora la stima MAP. Possiamo ovviamente scrivere 

$$
\ln f _ {M | \boldsymbol {X} ^ {n}} (\mu | \boldsymbol {x} ^ {n}) = \ln f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) + \ln f _ {M} (\mu) - \ln f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})
$$Massimizzando rispetto a $\mu$ otteniamo il stimatore MAP 

$$
\widehat {\mu} _ {\text {MAP}} (\boldsymbol {x} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}} \Longleftrightarrow \widehat {M} _ {\text {MAP}} (\boldsymbol {X} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}
$$

che coincide con l'MMSEE!! 

Domanda: è casuale o c'è un motivo più profondo per la coincidenza di questi due stimatori? 

### Estimatori (MMSE, MAP)

Sia C (·) una funzione di costo arbitraria dell'errore di stima; 

Assumiamo che C(·) sia pari e convessa e che $f _ { \Theta | , X ^ { n } } ( \theta | \pmb { x } ^ { n } )$ sia simmetrica rispetto alla sua media $\mathbb { E } \left[ \Theta | \pmb { X } ^ { n } = \pmb { x } ^ { n } \right]$, ovvero: 

$$
f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta - \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ] | \boldsymbol {x} ^ {n}) = f _ {\Theta | \boldsymbol {X} ^ {n}} (- \theta + \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ] | \boldsymbol {x} ^ {n})
$$

Allora l'MMSEE minimizza il rischio Bayesiano per qualsiasi funzione di costo in questa classe. 

La dimostrazione è semplice ed è omessa qui. 

Si noti che, rigorosamente parlando, la funzione di costo 0 − 1 che porta a uno stimatore MAP non è differenziabile. 

Tuttavia, può essere dimostrato che, sotto la condizione di simmetria sopra indicata sulla distribuzione a posteriori, abbiamo 

$$
\widehat {\mu} _ {\text { MAP }} (\boldsymbol {x} ^ {n}) = \widehat {\mu} _ {\text { MMSE }} (\boldsymbol {x} ^ {n})
$$

## Inferenza non Bayesiana: Stima di parametri non casuali

Assumiamo ora che le osservazioni $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ siano estratte da una famiglia di pdf, $f _ { { \pmb X } ^ { n } } \big ( { \pmb x } ^ { n } ; { \boldsymbol \theta } \big )$; 

Assumiamo che θ sia deterministico e sconosciuto: equivalentemente, possiamo assumere che non abbiamo informazioni a priori sufficienti per assegnare un prior $f _ { \Theta } ( \theta )$ ); 

Assumiamo che lo spazio dei parametri sia S; 

Definiamo la verosimiglianza del parametro θ, dato che le osservazioni $\pmb { x } ^ { n }$ sono disponibili, la funzione: 

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

## Inferenza non Bayesiana

Data uno stimatore $\Theta ( { \pmb x } ^ { n } )$ del parametro non casuale $\theta ,$, abbiamo: 

$$
\mathbb {E} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \theta + b _ {n} (\theta)
$$

con $b _ { n } ( \theta )$ il bias dello stimatore; 

Lo stimatore è non distorto (unbiased) se $b _ { n } ( \theta ) = 0$, mentre è solo asintoticamente non distorto se $b _ { n } ( \theta )$ diventa trascurabile con $n ;$ 

L'errore casuale dello stimatore è solitamente quantificato tramite il suo valore Mean Square, ovvero: 

$$
\mathbb {E} \left[ (\Theta (\boldsymbol {X} ^ {n}) - \theta) ^ {2} \right] = \overline {{e _ {n} ^ {2}}}
$$

Uno stimatore MMSE non distorto di $\theta$ è uno stimatore che minimizza la varianza: 

$$
\operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \Theta^ {2} (\boldsymbol {X} ^ {n}) \right] - \theta^ {2}
$$

Uno stimatore è debolmente consistente se $\Theta ( { \pmb x } ^ { n } ) \to \theta$ in probabilità, fortemente consistente se $\Theta ( { \pmb x } ^ { n } ) \to \theta$ quasi certamente, MS consistente se $\overline { { e _ { n } ^ { 2 } } } \to 0$ 

### Limite di Cramér-Rao

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

### Limite di Cramér-Rao

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

### Limite di Cramér-Rao

Elaborando le derivazioni precedenti, otteniamo un limite inferiore imbattibile alla varianza di qualsiasi stimatore del parametro non casuale $\theta$ nella forma: 

$$
\operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] \geq \frac {\left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2}}{\mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right]} = \frac {\left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2}}{I _ {n} (\theta)}
$$

La quantità $I _ { n } ( \theta )$ è definita come Informazione di Fisher, e obbedisce alla seguente identità: 

$$
I _ {n} (\theta) = \mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right] = - \mathbb {E} \left[ \frac {\partial^ {2} \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta^ {2}} \right]
$$

### Limite di Cramér-Rao

Come anticipato, lo stimatore $\Theta ( { \pmb x } ^ { n } )$ è non distorto se <sup>E</sup> $[ \Theta ( { \pmb x } ^ { n } ) ] = \theta$ 

In questa situazione, abbiamo che 

$$
\mathbb {E} \left[ (\Theta (\boldsymbol {X} ^ {n}) - \theta) ^ {2} \right] = \operatorname{Var} [ \Theta (\boldsymbol {X} ^ {n}) ] \geq \frac {1}{I _ {n} (\theta)}
$$

Così il Limite di Cramér-Rao (CRB) diventa un limite inferiore imbattibile all'MSE di qualsiasi stimatore. 

Uno stimatore non distorto il cui MSE è uguale al CRB è definito efficiente 

Fatto importante: Se esiste uno stimatore efficiente per un dato problema di stima non Bayesiana, questo coincide necessariamente con lo stimatore ML. 

## Un esempio: inferire la frequenza del cifrario di una sorgente senza memoriaConsideriamo inizialmente $\pmb { x } ^ { n } \in \{ 0 , 1 \} ^ { n }$ , estratto da $\pmb { X } ^ { n } \sim  { \mathcal { B } } ( 1 , \beta )$ , $\beta$ sconosciuto; 

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

## Inferenza non Bayesiana

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

Concludiamo che la MLE della frequenza di cifratura è efficiente. 

## Inferenza Bayesiana

Assumiamo ora di avere m parametri casuali, $\pmb { \theta } [ \theta _ { 1 } , \ldots , \theta _ { m } ] ^ { T }$ estratti da una pdf nota $f _ { \Theta } ( \pmb { \theta } )$ e un set di dati $\pmb { x } ^ { n }$ estratti da una pdf condizionale $f _ { { \pmb X } ^ { n } | \pmb \theta } ( { \pmb x } ^ { n } | \pmb \theta )$ 

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

### Estimatori (MMSE, MAP)

Assumiamo che la funzione di costo sia 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = \sum_ {i = 1} ^ {m} \left(\theta_ {i} - \widehat {\theta} _ {i} (\boldsymbol {x} ^ {n}))\right)
$$

Poiché il problema di minimizzazione è disgiunto (cioè, separabile), abbiamo: 

$$
\widehat {\theta} _ {i} (\boldsymbol {x} ^ {n}) = \mathbb {E} \left[ \Theta_ {i} | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right] = \int \theta_ {i} f _ {\theta_ {i} | \boldsymbol {X} ^ {n}} (\theta_ {i} | \boldsymbol {x} ^ {n}) d \theta_ {i}
$$

dove l'estimatore vettoriale MMSE si legge: 

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \mathbb {E} \left[ \Theta | \boldsymbol {X} ^ {n} \right]
$$

### Estimatori (MMSE, MAP)

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

## Inferenza non Bayesiana

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

## Estimatori LMMSE lineari

0 Iniziamo con un semplice problema scalare. Assumiamo che $\pmb { x } ^ { n }$ sia il campione osservato, estratto da $X ^ { n }$ , e assumiamo di voler progettare un estimatore lineare di un parametro casuale $\Theta ,$ , distribuito secondo una legge nota, nella forma: 

$$
\widehat {\Theta} (\boldsymbol {X} ^ {n}) = \boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b \quad \boldsymbol {a} \in \mathbb {R} ^ {n}
$$

Un estimatore Linear MMSE (LMMSE) seleziona il vettore a e la costante b in modo da minimizzare l'MMSE 

$$
\mathbb {E} \left[ (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) ^ {2} \right] = \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right]
$$

che è uguale a 

$$
\boldsymbol {a} ^ {T} \boldsymbol {R} \boldsymbol {a} + b ^ {2} + \mathbb {E} [ \Theta^ {2} ] - 2 b (\overline {{{\Theta}}}) - 2 \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} \Theta ] - 2 b \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ]
$$

dove $\pmb { R } = \mathbb { E } \left[ \pmb { X } ^ { n } \pmb { X } ^ { n T } \right]$ è la matrice di correlazione del vettore casuale $X ^ { n }$ 

## Estimatori LMMSE lineari (cont.)

Annullando il gradiente rispetto a a e la derivata rispetto a $b$ otteniamo: 

$$
\nabla_ {\boldsymbol {a}} \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \mathbb {E} [ \boldsymbol {X} ^ {n} \Theta ] = 0
$$

$$
\frac {\partial \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right]}{\partial b} = 2 b - 2 \overline {{\Theta}} - 2 \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ] = 0
$$

## Inferenza non Bayesiana

$$
b _ {\text { LMMSE }} = \mathbb {E} [ \Theta ] - \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ]
$$

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \boldsymbol {a} ^ {T} \left(\boldsymbol {X} ^ {n} - \mathbb {E} \left[ \boldsymbol {X} ^ {n} \right]\right) + \mathbb {E} [ \Theta ]
$$

che, reinserito nell'MSE dimostra che a dovrebbe minimizzare 

$$
\left\| \boldsymbol {a} ^ {T} \left(\boldsymbol {X} ^ {n} - \mathbb {E} \left[ \boldsymbol {X} ^ {n} \right]\right) + (\Theta - \mathbb {E} [ \Theta ]) \right\| ^ {2}
$$

Di conseguenza, denotando $\pmb { M } = \mathbb { E } \left[ ( \pmb { X } ^ { n } - \mathbb { E } [ \pmb { X } ^ { n } ] ) ( \pmb { X } ^ { n } - \mathbb { E } [ \pmb { X } ^ { n } ] ) ^ { T } \right]$ la matrice di covarianza di $X ^ { n }$ , l'estimatore LMMSE si legge 

$$
\boldsymbol {a} _ {\text { LMMSE }} = \boldsymbol {M} ^ {- 1} \mathbb {E} \left[ \left(\boldsymbol {X} ^ {n} - \mathbb {E} [ \boldsymbol {X} ^ {n} ]\right) (\Theta - \mathbb {E} [ \Theta ]) \right] = \boldsymbol {M} ^ {- 1} \boldsymbol {s}
$$

### Adattività e Algoritmo del Gradiente

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

### Adattività e Algoritmo del Gradiente

L'errore alla (n + 1)-es iterazione si legge 

$$
\boldsymbol {\epsilon} ^ {(n + 1)} = \boldsymbol {a} ^ {(n + 1)} - \boldsymbol {a} _ {\text { LMMSE }} = \boldsymbol {a} ^ {(n)} - \boldsymbol {a} _ {\text { LMMSE }} - \gamma \boldsymbol {M} (\boldsymbol {a} ^ {(n)} - \boldsymbol {a} _ {\text { LMMSE }}) = (\boldsymbol {I} - \gamma \boldsymbol {M}) \boldsymbol {\epsilon} ^ {(n)}
$$

Di conseguenza abbiamo 

$$
\boldsymbol {\epsilon} ^ {(n + 1)} = (\boldsymbol {I} - \gamma \boldsymbol {M}) ^ {n} \boldsymbol {\epsilon} ^ {(1)} = \boldsymbol {U} (\boldsymbol {I} - \gamma \boldsymbol {\Lambda}) ^ {n} \boldsymbol {U} ^ {T}
$$

dove Λ è la matrice diagonale dei valori propri di M e U contiene i suoi autovettori. 

L'errore converge quindi a zero se il modulo massimo dei valori propri o $\pmb { I } - \gamma \pmb { M }$ è minore di uno, ovvero: 

$$
- 1 <   1 - \gamma \lambda_ {M A X} <   1 \Longrightarrow 0 <   \gamma <   \frac {2}{\lambda_ {M A X}}
$$

## Un approccio diverso: statistica descrittivaLasciamo ora da parte la probabilità. Supponiamo invece di passare alla statistica descrittiva, in cui i campioni contano per ciò che sono e non sono considerati realizzazioni di vettori casuali:

Definiamo un dataset di addestramento come una collezione di $p$ campioni $n$-dimensionali, che possono essere organizzati nella matrice $n \times p$:

$$
\boldsymbol {X} = \left[ \begin{array}{c c c} x _ {1} (1) & \dots & x _ {1} (p) \\ \dots & \dots & \dots \\ x _ {n} (1) & \dots & x _ {n} (p) \end{array} \right] \in \mathbb {R} ^ {n \times p}
$$

Supponiamo di conoscere $p$ valori misurati del parametro $\theta _ { r }$, ciascuno corrispondente a uno dei $p$ campioni $n$-dimensionali del training set, i.e.:

$$
\boldsymbol {y} = [ \theta (1), \dots , \theta (p) ] \in \mathbb {R} ^ {p}
$$

Vogliamo adattare i dati a un modello lineare nella forma

$$
\theta (i) = \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) + \epsilon_ {n}
$$

con $\epsilon _ { n }$ che incapsula l'errore.

### Minimi Quadrati (Least Squares)

Poiché abbiamo un dataset $p$-dimensionale, vogliamo selezionare $a$ in modo tale da minimizzare:

$$
\parallel \epsilon_ {n} \parallel^ {2} = \sum_ {i = 1} ^ {p} \left[ \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) - \theta (i) \right] ^ {2}
$$

Il nostro problema è selezionare $a$ e $b$ in modo ottimizzato. Notiamo preliminarmente che

$$
\sum_ {i = 1} ^ {p} \left[ \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) - \theta (i) \right] ^ {2} = \| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \| ^ {2}
$$

Notiamo che

$$
\| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \| ^ {2} = \boldsymbol {a} ^ {T} \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {a} + \| \boldsymbol {y} \| ^ {2} - 2 \boldsymbol {a} ^ {T} \boldsymbol {X} \boldsymbol {y}
$$

### Minimi Quadrati (Least Squares)

Differenziando rispetto a $a$ si ottiene così

$$
\nabla_ {a} \left\| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \right\| ^ {2} = 2 \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {a} - 2 \boldsymbol {X} \boldsymbol {y} = 0
$$

che produce

$$
\boldsymbol {a} _ {\mathrm{LS}} = \left(\boldsymbol {X} \boldsymbol {X} ^ {T}\right) ^ {- 1} \boldsymbol {X} \boldsymbol {y}
$$

richiedendo che $( { \pmb x } { \pmb x } ^ { T } )$ sia invertibile $( \mathsf { i . e . , } \ p \geq n )$

Per riferimento futuro, denominiamo questa stima basata su un campione $p$-dimensionale come

$$
\boldsymbol {a} _ {\mathrm{LS}} (p) = \left(\boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p)\right) ^ {- 1} \boldsymbol {X} (p) \boldsymbol {y} (p)
$$

Supponiamo di avere un'osservazione dell'ambiente a orizzonte infinito, in modo che la dimensione del campione $p$ possa aumentare;

Consideriamo due scenari, i.e.:

a Vogliamo migliorare progressivamente la nostra stima aggiungendo più osservazioni;

b Vogliamo adattarci a condizioni potenzialmente variabili "dimenticando" le vecchie osservazioni al fine di pesare più significativamente le nuove osservazioni.

Possiamo regolare l'estimatore LS in modo tale da tenere conto di entrambe le situazioni sopra citate, e possiamo farlo con una complessità limitata.

### Minimi Quadrati (Least Squares)

Supponiamo $p \geq n$ e supponiamo di aver valutato

$$
\boldsymbol {a} _ {\mathrm{LS}} (p) = \left[ \boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p) \right] ^ {- 1} \boldsymbol {X} (p) \boldsymbol {y} (p)
$$

Supponiamo di avere un nuovo vettore nel dataset, diciamo $\pmb { x } ^ { n } ( p + 1 )$, e una nuova osservazione, $\theta ( p + 1 )$.

La nuova stima sarebbe

$$
\boldsymbol {a} _ {\mathrm{LS}} (p + 1) = \left[ \boldsymbol {X} (p + 1) \boldsymbol {X} ^ {T} (p + 1) \right] ^ {- 1} \boldsymbol {X} (p + 1) \boldsymbol {y} (p + 1)
$$

Domanda: Dobbiamo ricalcolare tutto da zero?

Notiamo che l'operazione di inversione comporta una complessità $\mathcal { O } ( n ^ { 3 } )$, mentre l'operazione di prodotto di matrici ha una complessità $\mathcal { O } ( n p )$ (in termini di moltiplicazioni).

### Formula di Sherman-Morrison

Sia $R$ una matrice invertibile di ordine $n ;$

Siano $u$ e $v$ vettori colonna $n$-dimensionali;

Abbiamo il seguente lemma di inversione di matrice con aggiornamento rank-1:

$$
\left(\boldsymbol {R} + \boldsymbol {u v} ^ {T}\right) ^ {- 1} = \boldsymbol {R} ^ {- 1} - \frac {\boldsymbol {R} ^ {- 1} \boldsymbol {u v} ^ {T} \boldsymbol {R} ^ {- 1}}{1 + \boldsymbol {u} ^ {T} \boldsymbol {R} ^ {- 1} \boldsymbol {v}}
$$

## Generalità - Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation

## Inferenza non Bayesiana

## Inferenza non Bayesiana

$$
\underbrace {\boldsymbol {X} (p + 1) \boldsymbol {X} ^ {T} (p + 1)} _ {\boldsymbol {R} (p + 1)} = \sum_ {i = 1} ^ {p + 1} \boldsymbol {x} ^ {n} (i) \boldsymbol {x} ^ {n T} (i) = \underbrace {\boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p)} _ {\boldsymbol {R} (p)} + \boldsymbol {x} ^ {n} (p + 1) \boldsymbol {x} ^ {n T} (p + 1)
$$

Di conseguenza

$$
\boldsymbol {R} ^ {- 1} (p + 1) = \boldsymbol {R} ^ {- 1} (p) - \frac {\boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1) \boldsymbol {x} ^ {n T} (p + 1) \boldsymbol {R} ^ {- 1} (p)}{1 + K (p + 1)}
$$

con

$$
K (p + 1) = \boldsymbol {x} ^ {n T} (p + 1) \boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1)
$$

## Inferenza non Bayesiana

## Inferenza non Bayesiana

$$
\boldsymbol {X} (p + 1) = \left[ \boldsymbol {X} (p) \boldsymbol {x} ^ {n} (p + 1) \right], \quad \boldsymbol {y} (p + 1) = \left[ \boldsymbol {y} (p) \theta (p + 1) \right] ^ {T}
$$

implicando

$$
\boldsymbol {X} (p + 1) \boldsymbol {y} (p + 1) = \boldsymbol {X} (p) \boldsymbol {y} (p) + \theta (p + 1) \boldsymbol {x} ^ {n} (p + 1)
$$

Poiché ${ \pmb a } ( p + 1 ) = { \pmb R } ^ { - 1 } ( p + 1 ) { \pmb X } ( p + 1 ) { \pmb y } ( p + 1 )$, abbiamo

$$
\boldsymbol {a} (p + 1) = \left[ \boldsymbol {I} _ {n} - \frac {\boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1)}{1 + K (p + 1)} \boldsymbol {x} ^ {n T} (p + 1) \right]
$$

$$
\left[ \boldsymbol {a} (p) + \theta (p + 1) \boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1) \right]
$$

che ha una complessità $\mathcal { O } ( n ^ { 2 } )$, indipendente (e non scalabile con) $p .$

### Minimi Quadrati (Least Squares)

Al fine di gestire situazioni in cui l'ambiente circostante può essere (lentamente) variabile nel tempo, potremmo voler forzare i "dati vecchi" a pesare meno dei dati "freschi".

Un modo possibile per farlo è tramite la media mobile esponenziale, la cui idea principale è adottare la seguente funzione di costo:

$$
\sum_ {i = 1} ^ {p} w ^ {p - i} \left[ \pmb {\mathscr {a}} ^ {T} \pmb {x} ^ {n} (i) - \theta (i) \right] ^ {2}
$$

Il peso $w < 1$ regola quanto velocemente viene dimenticato il passato.

Minimizzando rispetto a $a$ si ottiene l'LS mediato esponenzialmente:

$$
\boldsymbol {a} = \left[ \sum_ {i = 1} ^ {p} w ^ {p - i} \boldsymbol {x} ^ {n} (i) \boldsymbol {x} ^ {n T} (i) \right] ^ {- 1} \sum_ {i = 1} ^ {p} w ^ {p - i} \boldsymbol {x} ^ {n} (i) \theta (i)
$$

stesso suscettibile di un'implementazione ricorsiva alla luce del lemma di Sherman-Morrison.

## Inferenza non Bayesiana

Supponiamo ora che, sotto le stesse condizioni viste sopra, vogliamo trovare un LS nella forma più generale

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} + b
$$

Calcoli lunghi, seppur semplici, portano alla forma LMS generale

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