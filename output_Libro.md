# INTRODUZIONE ALLA PROBABILITÀ E STATISTICA PER INGEGNERI E SCIENTISTI

Terza Edizione 

# ELEMENTI DI PROBABILITÀ

## 3.1 INTRODUZIONE

Il concetto di probabilità di un particolare evento di un esperimento è soggetto a vari significati o interpretazioni. Ad esempio, se un geologo viene citato mentre afferma che "c'è una probabilità del 60 percento di trovare petrolio in una certa regione", probabilmente tutti noi abbiamo qualche idea intuitiva su ciò che viene detto. Infatti, la maggior parte di noi interpreterebbe probabilmente questa affermazione in uno dei due modi possibili: o immaginando che 

1. il geologo sente che, nel lungo periodo, nel 60 percento delle regioni le cui condizioni ambientali esterne sono molto simili alle condizioni prevalenti nella regione in esame, ci sarà del petrolio; oppure, immaginando che 

2. il geologo crede che sia più probabile che la regione contenga petrolio rispetto al fatto che non lo contenga; e in effetti .6 è una misura della credenza del geologo nell'ipotesi che la regione conterrà petrolio. 

Le due interpretazioni precedenti della probabilità di un evento sono definite come l'interpretazione della frequenza e l'interpretazione soggettiva (o personale) della probabilità. Nell'interpretazione della frequenza, la probabilità di un dato risultato di un esperimento è considerata come una "proprietà" di quel risultato. Si immagina che questa proprietà possa essere determinata operativamente dalla ripetizione continua dell'esperimento — la probabilità del risultato sarà quindi osservabile come la proporzione degli esperimenti che producono il risultato. Questa è l'interpretazione della probabilità più diffusa tra gli scienziati. 

Nell'interpretazione soggettiva, la probabilità di un risultato non è pensata come una proprietà del risultato ma è piuttosto considerata un'affermazione sulle credenze della persona che cita la probabilità, riguardante la possibilità che il risultato si verifichi. Pertanto, in questa interpretazione, la probabilità diventa un concetto soggettivo o personale e non ha significato al di fuori dell'espressione del grado di credenza di qualcuno. Questa interpretazione della probabilità è spesso preferita dai filosofi e da certi decisori economici. 

Indipendentemente dall'interpretazione che si dà alla probabilità, tuttavia, esiste un consenso generale sul fatto che la matematica della probabilità sia la stessa in entrambi i casi. Ad esempio, se pensate che la probabilità che domani piova sia .3 e sentite che la probabilità che sia nuvoloso ma senza pioggia è .2, allora dovreste sentire che la probabilità che sia nuvoloso o piovoso è .5 indipendentemente dalla vostra interpretazione individuale del concetto di probabilità. In questo capitolo, presentiamo le regole accettate, o assiomi, utilizzati nella teoria della probabilità. Come preliminare a questo, tuttavia, dobbiamo studiare il concetto di spazio campionario e gli eventi di un esperimento.

## 3.2 SPAZIO CAMPIONARIO ED EVENTI

Consideriamo un esperimento il cui risultato non è prevedibile con certezza in anticipo. Sebbene il risultato dell'esperimento non sarà noto in anticipo, supponiamo che l'insieme di tutti i possibili risultati sia noto. Questo insieme di tutti i possibili risultati di un esperimento è noto come spazio campionario dell'esperimento ed è denotato da S. Alcuni esempi sono i seguenti.

1. Se il risultato di un esperimento consiste nella determinazione del sesso di un neonato, allora

$$
S = \{g, b \}
$$

dove il risultato g significa che il bambino è una femmina e b che è un maschio.

2. Se l'esperimento consiste nello svolgimento di una corsa tra i sette cavalli aventi posizioni di partenza 1, 2, 3, 4, 5, 6, 7, allora

$$
S = \{\text { all   orderings   of } (1, 2, 3, 4, 5, 6, 7) \}
$$

Il risultato (2, 3, 1, 6, 5, 4, 7) significa, ad esempio, che il cavallo numero 2 è primo, poi il cavallo numero 3, poi il cavallo numero 1, e così via.

3. Supponiamo di essere interessati a determinare la quantità di dosaggio che deve essere somministrata a un paziente fino a quando tale paziente reagisce positivamente. Uno spazio campionario possibile per questo esperimento è lasciare che S consista in tutti i numeri positivi. Ovvero, poniamo che

$$
S = (0, \infty)
$$

dove il risultato sarebbe x se il paziente reagisse a un dosaggio di valore x ma non a nessun dosaggio inferiore.

Qualsiasi sottoinsieme E dello spazio campionario è noto come evento. Ovvero, un evento è un insieme costituito dai possibili risultati dell'esperimento. Se il risultato dell'esperimento è contenuto in E, allora diciamo che E si è verificato. Alcuni esempi di eventi sono i seguenti.

Nell'Esempio 1 se $E = \{ g \}$ , allora E è l'evento che il bambino è una femmina. Allo stesso modo, se $F = \{ b \}$ , allora F è l'evento che il bambino è un maschio.

Nell'Esempio 2 se

## E = {tutti gli esiti in S che iniziano con 3}

allora E è l'evento che il cavallo numero 3 vince la gara.

Per ogni due eventi E e F di uno spazio campionario S, definiamo il nuovo evento $E \cup F _ { : }$, chiamato unione degli eventi E e F, come composto da tutti gli esiti che sono in E o in F o in entrambi $E$ e F. Ovvero, l'evento $E \cup F$ si verificherà se si verifica E o $F$. Per esempio, nell'Esempio 1 se $E = \{ g \}$ e $F = \{ b \}$, allora $E \cup F = \{ g , b \}$. Ovvero, $E \cup F$ sarebbe l'intero spazio campionario S. Nell'Esempio 2 se E = {tutti gli esiti che iniziano con 6} è l'evento che il cavallo numero 6 vince e $F = \{ { \mathrm { a l l } } $ esiti che hanno 6 nella seconda posizione} è l'evento che il cavallo numero 6 arriva secondo, allora $E \cup F$ è l'evento che il cavallo numero 6 arriva primo o secondo.

Analogamente, per ogni due eventi E e $F ,$ possiamo anche definire il nuovo evento EF, chiamato intersezione di E e $F ,$ come composto da tutti gli esiti che sono sia in E che in F. Ovvero, l'evento EF si verificherà solo se si verificano sia E che F. Per esempio, nell'Esempio 3 se $E = ( 0 , 5 )$ è l'evento che il dosaggio richiesto è inferiore a 5 e $F = ( 2 , 1 0 )$ è l'evento che esso è compreso tra 2 e 10, allora $E F = ( 2 , 5 )$ è l'evento che il dosaggio richiesto è compreso tra 2 e 5. Nell'Esempio 2 se $E =$ {tutti gli esiti che terminano in 5} è l'evento che il cavallo numero 5 arriva ultimo e $F = \{ { \mathrm { a l l } } $ esiti che iniziano con 5} è l'evento che il cavallo numero 5 arriva primo, allora l'evento $E F$ non contiene alcun esito e quindi non può verificarsi. Per dare un nome a tale evento, lo chiameremo evento nullo e lo denoteremo con ∅. Quindi ∅ si riferisce all'evento composto da nessun esito. Se $E F = \emptyset$, implicando che E e F non possono verificarsi entrambi, allora E e F sono detti mutuamente esclusivi.

Per ogni evento $E ,$ definiamo l'evento $E ^ { c }$, riferito come complemento di $E ,$ come composto da tutti gli esiti nello spazio campionario S che non sono in E. Ovvero, $E ^ { c }$ si verificherà se e solo se E non si verifica. Nell'Esempio 1 se ${ \cal E } = \{ b \}$ è l'evento che il bambino è un maschio, allora $E ^ { c } = \{ g \}$ è l'evento che è una femmina. Si noti inoltre che poiché l'esperimento deve produrre qualche esito, ne consegue che $S ^ { c } = \emptyset$

Per ogni due eventi E e F, se tutti gli esiti in E sono anche in F, allora diciamo che E è contenuto in F e scriviamo $E \subset F$ (o equivalentemente, $F \supset E )$. Quindi se $E \subset F$, allora la verificazione di E implica necessariamente la verificazione di F. Se $E \subset F$ e $F \subset E$, allora diciamo che E e F sono uguali (o identici) e scriviamo $E = F$

Possiamo anche definire unioni e intersezioni di più di due eventi. In particolare, l'unione degli eventi $E _ { 1 } , E _ { 2 } , \ldots , E _ { n }$, denotata sia da $E _ { 1 } \cup E _ { 2 } \cup \ldots \cup E _ { n }$ che da $\cup _ { 1 } ^ { n } E _ { i }$, è definita come l'evento composto da tutti gli esiti che sono in $E _ { i }$ per almeno un $i = 1 , 2 , \ldots , n .$. Analogamente, l'intersezione degli eventi $E _ { i } , i = 1 , 2 , \ldots , n ,$, denotata da $E _ { 1 } E _ { 2 } \cdots E _ { n } ,$ è definita come l'evento composto da quegli esiti che sono in tutti gli eventi $E _ { i } , i = 1 , 2 , \ldots , n$. In altre parole, l'unione di $E _ { i }$ si verifica quando almeno uno degli eventi $E _ { i }$ si verifica; l'intersezione si verifica quando tutti gli eventi $E _ { i }$ si verificano.

## 3.3 DIAGRAMMI DI VENN E L'ALGEBRA DEGLI EVENTI

Una rappresentazione grafica degli eventi che è molto utile per illustrare le relazioni logiche tra di essi è il diagramma di Venn. Lo spazio campionario S è rappresentato come composto da tutti i punti in un grande rettangolo, e gli eventi $E , F , G , \ldots$ sono rappresentati come composti da tutti i punti in determinati cerchi all'interno del rettangolo. Gli eventi di interesse possono quindi essere indicati ombreggiando le regioni appropriate del diagramma. Ad esempio, nei tre diagrammi di Venn mostrati nella Figura 3.1, le aree ombreggiate rappresentano rispettivamente gli eventi $E \cup F , E F ,$ e $E ^ { c }$. Il diagramma di Venn della Figura 3.2 indica che $E \subset F .$

Le operazioni di formazione di unioni, intersezioni e complementari di eventi obbediscono a certe regole non dissimilarli alle regole dell'algebra. Ne elenciamo alcune.

$$
\begin{array}{l l l} \text {Commutative law} & E \cup F = F \cup E & E F = F E \\ \text {Associative law} & (E \cup F) \cup G = E \cup (F \cup G) & (E F) G = E (F G) \\ \text {Distributive law} & (E \cup F) G = E G \cup F G & E F \cup G = (E \cup G) (F \cup G) \end{array}
$$

Queste relazioni sono verificate mostrando che qualsiasi esito contenuto nell'evento sul lato sinistro dell'uguaglianza è anche contenuto nell'evento sul lato destro e viceversa. Un modo per mostrarlo è attraverso i diagrammi di Venn. Ad esempio, la legge distributiva può essere verificata dalla sequenza di diagrammi mostrata nella Figura 3.3.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/86c9ad5b3f7130e632f6e07c390840684d67e5e4a32b48dfc81caec2149d2ff0.jpg)



(a) Regione ombreggiata: E F



FIGURA 3.1 Diagrammi di Venn.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/53971b6ad96d49db4bf4ab3d75c975618c0b29ef4114eaec28b9c8939d26dc76.jpg)



(b) Regione ombreggiata: EF
![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/e5cf66ae65b562d3ce8847d57e4f584414963a191388085618e385f0582f4ed9.jpg)



(c) Regione ombreggiata: E<sup>c</sup>
![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/663b8d2437a1645c3333e5128bb1d62d51defee939f34a292b5340f6f91b4e0d.jpg)



FIGURA 3.2 Diagramma di Venn.



E ⊂F
## 3.4 Assiomi di Probabilità

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/f02d8a0fab141bc89aa0eb577736d46602d207954853357d048048ccee7c154c.jpg)



(a) Regione ombreggiata: EG
![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5921b4b7eb6ac9a7dca7d6a0968b0a68103e75808c10296af1b6f53e7e0d7fe0.jpg)



(b) Regione ombreggiata: FG
![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/02746014b2ea44c173a19b29547b259987bffc0a4962a6143ad0baf7ca1350a9.jpg)



(c) Regione ombreggiata: (E F)G (E F)G = EG FG



FIGURA 3.3 Dimostrazione della legge distributiva.


La seguente relazione utile tra le tre operazioni di base di formazione di unioni, intersezioni e complementari di eventi è nota come leggi di DeMorgan.

$$
\begin{array}{c} (E \cup F) ^ {c} = E ^ {c} F ^ {c} \\ (E F) ^ {c} = E ^ {c} \cup F ^ {c} \end{array}
$$

## 3.4 AXIOMI DI PROBABILITÀ

Sembra essere un fatto empirico che se un esperimento viene ripetuto continuamente nelle stesse esatte condizioni, allora per ogni evento E, la proporzione di tempo in cui il risultato è contenuto in E si avvicina a un certo valore costante all'aumentare del numero di ripetizioni. Ad esempio, se una moneta viene lanciata continuamente, allora la proporzione di lanci che risultano in testa si avvicinerà a un certo valore all'aumentare del numero di lanci. È questa frequenza limite costante che spesso abbiamo in mente quando parliamo della probabilità di un evento.

Da un punto di vista puramente matematico, supporremo che per ogni evento E di un esperimento avente uno spazio campionario S esista un numero, indicato da $P ( E )$ ), che sia in accordo con i seguenti tre assiomi.

ASSIOMA 1

$$
0 \leq P (E) \leq 1
$$

ASSIOMA 2

$$
P (S) = 1
$$

ASSIOMA 3

Per ogni sequenza di eventi mutuamente esclusivi $E _ { 1 } , E _ { 2 } , \ldots$ . (ovvero, eventi per i quali $E _ { i } E _ { j } = \theta$ quando $i \neq j )$ ,

$$
P \left(\bigcup_ {i = 1} ^ {n} E _ {i}\right) = \sum_ {i = 1} ^ {n} P (E _ {i}), \quad n = 1, 2, \dots , \infty
$$

Chiamiamo P(E ) la probabilità dell'evento E.

Così, l'Assioma 1 afferma che la probabilità che il risultato dell'esperimento sia contenuto in E è un numero compreso tra 0 e 1. L'Assioma 2 afferma che, con probabilità 1, il risultato sarà un membro dello spazio campionario S. L'Assioma 3 afferma che per ogni insieme di eventi mutuamente esclusivi la probabilità che almeno uno di questi eventi si verifichi è uguale alla somma delle loro rispettive probabilità.

Bisogna notare che se interpretiamo $P ( E )$ come la frequenza relativa dell'evento E quando viene eseguito un gran numero di ripetizioni dell'esperimento, allora $P ( E )$ soddisfarebbe effettivamente gli assiomi sopra indicati. Ad esempio, la proporzione (o frequenza) di tempo in cui il risultato è in E è chiaramente compresa tra 0 e 1, e la proporzione di tempo in cui è in S è 1 (poiché tutti i risultati sono in S). Inoltre, se E e F non hanno risultati in comune, allora la proporzione di tempo in cui il risultato è in E o in F è la somma delle loro rispettive frequenze. Come illustrazione di quest'ultima affermazione, supponiamo che l'esperimento consista nel lancio di una coppia di dadi e supponiamo che E sia l'evento in cui la somma è 2, 3 o 12 e F sia l'evento in cui la somma è 7 o 11. Allora se il risultato E si verifica per l'11 percento delle volte e il risultato F per il 22 percento delle volte, allora per il 33 percento delle volte il risultato sarà 2, 3, 12, 7 o 11.

Questi assiomi saranno ora utilizzati per dimostrare due semplici proposizioni riguardanti le probabilità. Notiamo innanzitutto che E e $E ^ { c }$ sono sempre mutuamente esclusivi, e poiché $E \cup E ^ { c } = S$ abbiamo dagli Assiomi 2 e 3 che

$$
1 = P (S) = P (E \cup E ^ {c}) = P (E) + P (E ^ {c})
$$

O equivalentemente, abbiamo quanto segue:

## PROPOSIZIONE 3.4.1

$$
P (E ^ {c}) = 1 - P (E)
$$

In altre parole, la Proposizione 3.4.1 afferma che la probabilità che un evento non si verifichi è 1 meno la probabilità che esso si verifichi. Ad esempio, se la probabilità di ottenere testa al lancio di una moneta è $\frac { 3 } { 8 }$ , la probabilità di ottenere croce deve essere $\frac { 5 } { 8 }$ .

La nostra seconda proposizione fornisce la relazione tra la probabilità dell'unione di due eventi in termini delle probabilità individuali e della probabilità dell'intersezione.

## PROPOSIZIONE 3.4.2

$$
P (E \cup F) = P (E) + P (F) - P (E F)
$$

## Dimostrazione

Questa proposizione è dimostrata più facilmente mediante l'uso di un diagramma di Venn come mostrato nella Figura 3.4. Poiché le regioni I, II e III sono mutuamente esclusive, ne consegue che

$$
\begin{array}{c} P (E \cup F) = P (\mathrm{I}) + P (\mathrm{II}) + P (\mathrm{III}) \\ P (E) = P (\mathrm{I}) + P (\mathrm{II}) \\ P (F) = P (\mathrm{II}) + P (\mathrm{III}) \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/564d23373d2c0461d4a181506e183073e81d52491e8f4cc8d6ee0d6c3e63f838.jpg)

## FIGURA 3.4

che mostra che 

$$
P (E \cup F) = P (E) + P (F) - P (\mathrm{II})
$$

e la dimostrazione è completa poiché $\mathrm { I I } = E F .$ 

EXAMPLE 3.4a Un totale del 28 percento dei maschi americani fuma sigarette, il 7 percento fuma sigari e il 5 percento fuma sia sigari che sigarette. Quale percentuale di maschi non fuma né sigari né sigarette? 

SOLUTION Sia E l'evento che un maschio scelto casualmente è un fumatore di sigarette e sia B l'evento che egli è un fumatore di sigari. Allora, la probabilità che questa persona sia un fumatore di sigarette o di sigari è 

$$
P (E \cup F) = P (E) + P (F) - P (E F) = . 0 7 +. 2 8 -. 0 5 = . 3
$$

Pertanto, la probabilità che la persona non sia un fumatore è .7, implicando che il 70 percento dei maschi americani non fuma né sigarette né sigari. ■ 

Le odds di un evento A sono definite da 

$$
\frac {P (A)}{P (A ^ {c})} = \frac {P (A)}{1 - P (A)}
$$

Pertanto, le odds di un evento A indicano quanto sia più probabile che A si verifichi rispetto al fatto che non si verifichi. Ad esempio, se $P ( A ) = 3 / 4$, allora $P ( A ) / ( 1 - P ( A ) ) = 3$, quindi le odds sono 3. Di conseguenza, è 3 volte più probabile che A si verifichi rispetto al fatto che non lo faccia. 

## 3.5 SPAZI CAMPIONARI CON ESITI EQUIPROBABILI

Per un gran numero di esperimenti, è naturale assumere che ogni punto nello spazio campionario abbia la stessa probabilità di verificarsi. Cioè, per molti esperimenti il cui spazio campionario S è un insieme finito, diciamo $S = \{ 1 , 2 , \dots , N \}$, è spesso naturale assumere che 

$$
P (\{1 \}) = P (\{2 \}) = \dots = P (\{N \}) = p \quad (\text { say })
$$

Ora segue dagli Assiomi 2 e 3 che 

$$
1 = P (S) = P (\{1 \}) + \dots + P (\{N \}) = N p
$$

che mostra che 

$$
P (\{i \}) = p = 1 / N
$$

Da questo, segue dall'Assioma 3 che per ogni evento E, 

$$
P (E) = \frac {\text { Number   of   points   in } E}{N}
$$

In parole, se assumiamo che ogni esito di un esperimento abbia la stessa probabilità di verificarsi, allora la probabilità di qualsiasi evento E è uguale alla proporzione di punti nello spazio campionario che sono contenuti in E. 

Pertanto, per calcolare le probabilità è spesso necessario essere in grado di contare efficacemente il numero di diversi modi in cui un dato evento può verificarsi. Per farlo, utilizzeremo la seguente regola. 

## PRINCIPIO BASE DEL CONTEGGIO

Supponiamo che debbano essere eseguiti due esperimenti. Allora, se l'esperimento 1 può dare come risultato uno qualsiasi dei m possibili esiti e se, per ogni esito dell'esperimento 1, ci sono n possibili esiti dell'esperimento 2, allora insieme ci sono mn possibili esiti dei due esperimenti. 

## Dimostrazione del Principio Base

Il principio base può essere dimostrato enumerando tutti i possibili esiti dei due esperimenti come segue: 

$$
\begin{array}{c} (1, 1), (1, 2), \ldots , (1, n) \\ (2, 1), (2, 2), \ldots , (2, n) \\ \vdots \\ (m, 1), (m, 2), \ldots , (m, n) \end{array}
$$

dove diciamo che l'esito è (i, j) se l'esperimento 1 produce il suo i-esimo possibile esito e l'esperimento 2 produce quindi il j-esimo dei suoi possibili esiti. Pertanto, l'insieme dei possibili esiti consiste in m righe, ciascuna riga contenente n elementi, il che dimostra il risultato. ■ 

EXAMPLE 3.5a Due palline vengono "estratte casualmente" da una ciotola contenente 6 palline bianche e 5 nere. Qual è la probabilità che una delle palline estratte sia bianca e l'altra nera? 

SOLUTION Se consideriamo significativo l'ordine in cui le palline vengono selezionate, allora poiché la prima pallina estratta può essere una qualsiasi delle 11 e la seconda una qualsiasi delle restanti 10, segue che lo spazio campionario consiste in $1 1 \cdot 1 0 = 1 1 0$ punti. Inoltre, ci sono $6 \cdot 5 = 3 0$ modi in cui la prima pallina selezionata è bianca e la seconda nera, e analogamente ci sono $5 \cdot 6 = 3 0$ modi in cui la prima pallina è nera e la seconda bianca. Pertanto, assumendo che "estratte casualmente" significhi che ciascuno dei 110 punti nello spazio campionario abbia la stessa probabilità di verificarsi, vediamo che la probabilità desiderata è 

$$
\frac {3 0 + 3 0}{1 1 0} = \frac {6}{1 1}
$$

Quando ci sono più di due esperimenti da eseguire, il principio base può essere generalizzato come segue:

## Principio di Base Generalizzato del Conteggio

Se $r$ esperimenti da eseguire sono tali che il primo possa dare uno qualsiasi dei $\cdot _ { n _ { 1 } }$ possibili risultati, e se per ciascuno di questi $\displaystyle n _ { 1 }$ possibili risultati ci sono $_ { n 2 }$ possibili risultati del secondo esperimento, e se per ciascuno dei possibili risultati dei primi due esperimenti ci sono $n _ { 3 }$ possibili risultati del terzo esperimento, e $\operatorname { i f } , \ldots$, allora ci sono in totale $n _ { 1 } \cdot n _ { 2 } \cdot \cdot \cdot n _ { r }$ possibili risultati degli $r$ esperimenti.

Come illustrazione di ciò, determiniamo il numero di modi diversi in cui $n$ oggetti distinti possono essere disposti in un ordine lineare. Ad esempio, quanti diversi arrangiamenti ordinati delle lettere a, b, c sono possibili? Per enumerazione diretta vediamo che ci sono $6 ;$, ovvero abc, acb, bac, bca, cab, cba. Ognuno di questi arrangiamenti ordinati è noto come permutazione. Pertanto, ci sono 6 possibili permutazioni di un insieme di 3 oggetti. Questo risultato potrebbe anche essere ottenuto dal principio di base, poiché il primo oggetto nella permutazione può essere uno qualsiasi dei 3, il secondo oggetto nella permutazione può quindi essere scelto da uno qualsiasi dei 2 rimanenti, e il terzo oggetto nella permutazione è quindi scelto dall'unico rimanente. Pertanto, ci sono $3 \cdot 2 \cdot 1 = 6$ possibili permutazioni.

Supponiamo ora di avere $n$ oggetti. Un ragionamento simile mostra che ci sono

$$
n (n - 1) (n - 2) \cdot \cdot \cdot 3 \cdot 2 \cdot 1
$$

diverse permutazioni degli $n$ oggetti. È conveniente introdurre la notazione $n!$, che si legge $^ { * } n$ "fattoriale", per l'espressione precedente. Cioè,

$$
n! = n (n - 1) (n - 2) \cdot \cdot \cdot 3 \cdot 2 \cdot 1
$$

Così, ad esempio, $1 ! = 1 , 2 ! = 2 \cdot 1 = 2 , 3 ! = 3 \cdot 2 \cdot 1 = 6 , 4 ! = 4 \cdot 3 \cdot 2 \cdot 1 = 2 4$, e così via. È conveniente definire $0! = 1$.

EXAMPLE 3.5b Il Sig. Jones ha 10 libri che intende mettere sulla sua libreria. Di questi, 4 sono libri di matematica, 3 sono libri di chimica, 2 sono libri di storia e 1 è un libro di lingue. Jones vuole disporre i suoi libri in modo che tutti i libri che trattano la stessa materia siano insieme sullo scaffale. Quanti diversi arrangiamenti sono possibili?

SOLUTION Ci sono $4! 3! 2! 1!$ arrangiamenti in cui i libri di matematica sono per primi in fila, poi i libri di chimica, poi i libri di storia e infine il libro di lingue. Allo stesso modo, per ogni possibile ordinamento delle materie, ci sono $4! 3! 2! 1!$ possibili arrangiamenti. Di conseguenza, poiché ci sono $4!$ possibili ordinamenti delle materie, la risposta desiderata è $4! 4! 3! 2! 1! = 6.912$. ■

EXAMPLE 3.5c Una classe di teoria della probabilità è composta da 6 uomini e 4 donne. Viene dato un esame e gli studenti vengono classificati in base alla loro prestazione. Supponendo che nessun studente ottenga lo stesso punteggio, (a) quanti diversi classifiche sono possibili? (b) Se tutti i classifiche sono considerate ugualmente probabili, qual è la probabilità che le donne ricevano i primi 4 punteggi?

## SOLUZIONE

(a) Poiché ogni classifica corrisponde a una particolare disposizione ordinata delle 10 persone, vediamo che la risposta a questa parte è $1 0 ! = 3 \mathrm { , } 6 2 8 \mathrm { , } 8 0 0$ 

(b) Poiché ci sono 4! possibili classifiche delle donne tra di loro e 6! possibili classifiche degli uomini tra di loro, dal principio di base segue che ci sono $( 6 ! ) ( 4 ! ) = ( 7 2 0 ) ( 2 4 ) = 1 7 { , } 2 8 0$ possibili classifiche in cui le donne ricevono i primi 4 punteggi. Pertanto, la probabilità desiderata è 

$$
\frac {6 ! 4 !}{1 0 !} = \frac {4 \cdot 3 \cdot 2 \cdot 1}{1 0 \cdot 9 \cdot 8 \cdot 7} = \frac {1}{2 1 0}
$$

Supponiamo ora di essere interessati a determinare il numero di diversi gruppi di r oggetti che potrebbero essere formati da un totale di n oggetti. Ad esempio, quanti diversi gruppi di tre potrebbero essere selezionati dai cinque elementi A, B, C, D, E? Per rispondere a questo, ragioniamo come segue. Poiché ci sono 5 modi per selezionare l'elemento iniziale, 4 modi per selezionare poi il prossimo elemento e 3 modi per selezionare infine l'ultimo elemento, ci sono quindi 5 · 4 · 3 modi di selezionare il gruppo di 3 quando l'ordine in cui gli elementi vengono selezionati è rilevante. Tuttavia, poiché ogni gruppo di 3, diciamo il gruppo composto dagli elementi A, B e C, sarà contato 6 volte (ovvero, tutte le permutazioni ABC, ACB, BAC, BCA, CAB, CBA saranno contate quando l'ordine di selezione è rilevante), segue che il numero totale di diversi gruppi che possono essere formati è $( 5 \cdot 4 \cdot 3 ) / ( 3 \cdot 2 \cdot 1 ) = 1 0$ 

In generale, poiché $n ( n - 1 ) \cdots ( n - r + 1 )$ rappresenta il numero di diversi modi in cui un gruppo di r elementi potrebbe essere selezionato da n elementi quando l'ordine di selezione è considerato rilevante (poiché il primo selezionato può essere uno qualsiasi dei n, e il secondo selezionato uno qualsiasi dei rimanenti n − 1, ecc.), e poiché ogni gruppo di r elementi sarà contato r! volte in questo conteggio, segue che il numero di diversi gruppi di r elementi che potrebbero essere formati da un insieme di n elementi è 

$$
{\frac {n (n - 1) \cdots (n - r + 1)}{r !}} = {\frac {n !}{(n - r) ! r !}}
$$

## NOTAZIONE E TERMINOLOGIA

Definiamo <sup>n</sup>, per $r \leq n ,$ da

$$
\binom {n} {r} = \frac {r !}{(n - r) ! r !}
$$

e chiamiamo $\binom { n } { r }$ il numero di combinazioni di n oggetti presi r alla volta.

Così, <sup>n</sup> rappresenta il numero di diversi gruppi di dimensione r che possono essere selezionati da un insieme di dimensione n quando l'ordine di selezione non è considerato rilevante. Ad esempio, ci sono

$$
\binom {8} {2} = \frac {8 \cdot 7}{2 \cdot 1} = 2 8
$$

diversi gruppi di dimensione 2 che possono essere scelti da un insieme di 8 persone, e

$$
\binom {1 0} {2} = \frac {1 0 \cdot 9}{2 \cdot 1} = 4 5
$$

diversi gruppi di dimensione 2 che possono essere scelti da un insieme di 10 persone. Inoltre, poiché $0 ! = 1$ si noti che

$$
\binom {n} {0} = \binom {n} {n} = 1
$$

ESEMPIO 3.5d Un comitato di dimensione 5 deve essere selezionato da un gruppo di 6 uomini e 9 donne. Se la selezione viene effettuata casualmente, qual è la probabilità che il comitato sia composto da 3 uomini e 2 donne?

SOLUZIONE Assumiamo che "selezionato casualmente" significhi che ciascuna delle $\binom { 1 5 } { 5 }$ combinazioni possibili abbia la stessa probabilità di essere selezionata. Pertanto, poiché ci sono $\binom { 6 } { 3 }$ scelte possibili di 3 uomini e $\binom { 9 } { 2 }$ scelte possibili di 2 donne, ne consegue che la probabilità desiderata è data da

$$
\frac {\binom {6} {3} \binom {9} {2}}{\binom {1 5} {5}} = \frac {2 4 0}{1 0 0 1}
$$

ESEMPIO 3.5e Da un insieme di n elementi deve essere selezionato un campione casuale di dimensione k. Qual è la probabilità che un dato elemento si trovi tra i k selezionati?

SOLUZIONE Il numero di diverse selezioni che contengono il dato elemento è ${ \binom { 1 } { 1 } } { \binom { n - 1 } { k - 1 } }$ Pertanto, la probabilità che un particolare elemento sia tra i k selezionati è

$$
\binom {n - 1} {k - 1} \bigg / \binom {n} {k} = \frac {(n - 1) !}{(n - k) ! (k - 1) !} \bigg / \frac {n !}{(n - k) ! k !} = \frac {k}{n}
$$

ESEMPIO 3.5f Una squadra di basket è composta da 6 giocatori neri e 6 bianchi. I giocatori devono essere accoppiati in gruppi di due per determinare i compagni di stanza. Se gli accoppiamenti vengono effettuati casualmente, qual è la probabilità che nessuno dei giocatori neri abbia un compagno di stanza bianco?

SOLUZIONE Iniziamo immaginando che le 6 coppie siano numerate — vale a dire, c'è una prima coppia, una seconda coppia, e così via. Poiché ci sono $\binom { 1 2 } { 2 }$ diverse scelte per una prima coppia; e per ogni scelta di una prima coppia ci sono $\textstyle { \binom { 1 0 } { 2 } }$ diverse scelte per una seconda coppia; e per ogni scelta delle prime 2 coppie ci sono $\binom { 8 } { 2 }$ scelte per una terza coppia; e così via, ne consegue dal principio fondamentale generale del conteggio che ci sono

$$
\binom {1 2} {2} \binom {1 0} {2} \binom {8} {2} \binom {6} {2} \binom {4} {2} \binom {2} {2} = \frac {1 2 !}{(2 !) ^ {6}}
$$

modi di dividere i giocatori in una prima coppia, una seconda coppia, e così via. Pertanto ci sono $( 1 2 ) ! / 2 ^ { 6 } 6 !$ modi di dividere i giocatori in 6 coppie (non ordinate) di 2 ciascuna. Inoltre, poiché ci sono, per lo stesso ragionamento, $6 ! / 2 ^ { 3 } 3 !$ modi di accoppiare i giocatori bianchi tra loro e $6 ! / 2 ^ { 3 } 3 !$ modi di accoppiare i giocatori neri tra loro, ne consegue che ci sono $( 6 ! / 2 ^ { 3 } 3 ! ) ^ { 2 }$ accoppiamenti che non risultano in alcuna coppia di compagni di stanza nero-bianco. Pertanto, se gli accoppiamenti vengono effettuati casualmente (in modo che tutti i risultati siano ugualmente probabili), allora la probabilità desiderata è

$$
\left(\frac {6 !}{2 ^ {3} 3 !}\right) ^ {2} / \frac {(1 2) !}{2 ^ {6} 6 !} = \frac {5}{2 3 1} = . 0 2 1 6
$$

Pertanto, ci sono approssimativamente solo due possibilità su cento che un accoppiamento casuale non risulterà in nessuno dei giocatori bianchi e neri che condividono la stanza. ■

ESEMPIO 3.5g Se n persone sono presenti in una stanza, qual è la probabilità che nessuna delle due festeggi il proprio compleanno lo stesso giorno dell'anno? Quanto grande deve essere n affinché questa probabilità sia inferiore a $\begin{array} { l } { { \displaystyle { \frac { 1 } { 2 } } ? } } \end{array}$

SOLUZIONE Poiché ogni persona può festeggiare il proprio compleanno in uno qualsiasi dei 365 giorni, ci sono in totale $( 3 6 5 ) ^ { n }$ risultati possibili. (Stiamo ignorando la possibilità che qualcuno sia nato il 29 febbraio.) Inoltre, ci sono (365)(364)(363)·(365−n+1) risultati possibili che non comportano che due persone abbiano lo stesso compleanno. Questo perché la prima persona potrebbe avere uno qualsiasi dei 365 compleanni, la persona successiva uno qualsiasi dei 364 giorni rimanenti, la successiva uno qualsiasi dei 363 rimanenti, e così via. Pertanto, assumendo che ogni risultato sia ugualmente probabile, vediamo che la probabilità desiderata è

$$
\frac {(3 6 5) (3 6 4) (3 6 3) \cdots (3 6 5 - n + 1)}{(3 6 5) ^ {n}}
$$

È un fatto piuttosto sorprendente che quando $n \geq 2 3$, questa probabilità è inferiore a $\frac { 1 } { 2 }$. Ovvero, se ci sono 23 o più persone in una stanza, allora la probabilità che almeno due di esse abbiano lo stesso compleanno supera $\frac { 1 } { 2 }$. Molte persone sono inizialmente sorprese da questo risultato, poiché 23 sembra così piccolo in relazione a 365, il numero di giorni dell'anno. Tuttavia, ogni coppia di individui ha una probabilità $\begin{array} { r } { \frac { 3 6 5 } { ( 3 6 5 ) ^ { 2 } } = \frac { 1 } { 3 6 5 } } \end{array}$ di avere lo stesso compleanno, e in un gruppo di 23 persone ci sono ${ \binom { 2 3 } { 2 } } = 2 5 3$ coppie diverse di individui. Guardato in questo modo, il risultato non sembra più così sorprendente. ■

## 3.6 PROBABILITÀ CONDIZIONALE

In questa sezione, introduciamo uno dei concetti più importanti di tutta la teoria della probabilità — quello della probabilità condizionale. La sua importanza è duplice. In primo luogo, siamo spesso interessati a calcolare le probabilità quando è disponibile qualche informazione parziale riguardante il risultato dell'esperimento, o a ricalcolarle alla luce di informazioni aggiuntive. In tali situazioni, le probabilità desiderate sono condizionali. In secondo luogo, come una sorta di bonus, spesso si scopre che il modo più semplice per calcolare la probabilità di un evento è prima "condizionare" sulla comparsa o non comparsa di un evento secondario.

Come illustrazione di una probabilità condizionale, supponiamo che si lanci una coppia di dadi. Lo spazio campionario S di questo esperimento può essere preso come il seguente insieme di 36 risultati

$$
S = \{(i, j), \quad i = 1, 2, 3, 4, 5, 6, \quad j = 1, 2, 3, 4, 5, 6 \}
$$

dove diciamo che il risultato è $( i , j )$ se il primo dado cade sul lato i e il secondo sul lato $j .$. Supponiamo ora che ciascuno dei 36 possibili risultati abbia la stessa probabilità di verificarsi e abbia quindi probabilità $\frac { 1 } { 3 6 }$. (In tale situazione diciamo che i dadi sono equi.) Supponiamo inoltre di osservare che il primo dado cade sul lato 3. Allora, data questa informazione, qual è la probabilità che la somma dei due dadi sia uguale a 8? Per calcolare questa probabilità, ragioniamo come segue: dato che il dado iniziale è un 3, possono esserci al massimo 6 possibili risultati del nostro esperimento, ovvero (3, 1), (3, 2), (3, 3), (3, 4), (3, 5) e (3, 6). Inoltre, poiché ciascuno di questi risultati aveva originariamente la stessa probabilità di verificarsi, dovrebbero ancora avere probabilità uguali. Cioè, dato che il primo dado è un 3, allora la probabilità (condizionale) di ciascuno dei risultati è $( 3 , 1 ) , ( 3 , 2 ) , ( 3 , 3 ) , ( 3 , 4 ) , ( 3 , 5 ) , ( 3 , 6 ) { \mathrm { i s } } { \frac { 1 } { 6 } } ,$, mentre la probabilità (condizionale) degli altri 30 punti nello spazio campionario è 0. Pertanto, la probabilità desiderata sarà $\frac { 1 } { 6 }$

Se facciamo in modo che E e F denotino, rispettivamente, l'evento che la somma dei dadi sia 8 e l'evento che il primo dado sia un 3, allora la probabilità appena ottenuta è chiamata probabilità condizionale di E dato che F si è verificato, ed è denotata da

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/fd3fed21a61bc7559d0beaa1204b9c4871bff13bba4eca9bbfcef3754586d272.jpg)



FIGURA 3.5 $\begin{array} { r } { \overline { { P ( E | F ) } } = \frac { P ( E F ) } { P ( F ) } , } \end{array}$


$$
P (E | F)
$$

Una formula generale per $P ( E | F )$ che sia valida per tutti gli eventi E e F è derivata nello stesso modo di quanto appena descritto. Ovvero, se l'evento F si verifica, allora affinché E si verifichi è necessario che la comparsa effettiva sia un punto sia in E che in $F ;$, cioè deve essere in EF. Ora, poiché sappiamo che F si è verificato, ne consegue che F diventa il nostro nuovo spazio campionario (ridotto) e quindi la probabilità che l'evento $E F$ si verifichi sarà uguale alla probabilità di EF relativa alla probabilità di F. Cioè,

$$
P (E | F) = \frac {P (E F)}{P (F)}\tag{3.6.1}
$$

Si noti che l'Equazione 3.6.1 è ben definita solo quando $P ( F ) > 0$ e quindi $P ( E | F )$ è definita solo quando $P ( F ) > 0$. (Vedere Figura 3.5.)

La definizione di probabilità condizionale data dall'Equazione 3.6.1 è coerente con l'interpretazione della probabilità come una frequenza relativa a lungo termine. Per vederlo, supponiamo che venga eseguito un gran numero n di ripetizioni dell'esperimento. Allora, poiché $P ( F )$ è la proporzione a lungo termine degli esperimenti in cui F si verifica, ne consegue che F si verificherà approssimativamente $n P ( F )$ volte. Allo stesso modo, in circa nP(EF) di questi esperimenti, si verificheranno sia E che F. Pertanto, degli approssimativamente $n P ( F )$ esperimenti il cui risultato è in F, approssimativamente $n P ( E F )$ di essi avranno anche il loro risultato in E. Cioè, per quegli esperimenti il cui risultato è in F, la proporzione il cui risultato è anche in E è approssimativamente

$$
\frac {n P (E F)}{n P (F)} = \frac {P (E F)}{P (F)}
$$

Poiché questa approssimazione diventa esatta man mano che $n$ diventa sempre più grande, ne consegue che (3.6.1) fornisce la definizione appropriata della probabilità condizionata di $E$ dato che $F$ si è verificata.

EXAMPLE 3.6a Un contenitore contiene 5 transistor difettosi (che falliscono immediatamente quando vengono messi in uso), 10 parzialmente difettosi (che falliscono dopo un paio d'ore di utilizzo) e 25 transistor accettabili. Un transistor viene scelto a caso dal contenitore e messo in uso. Se non fallisce immediatamente, qual è la probabilità che sia accettabile?

SOLUTION Poiché il transistor non è fallito immediatamente, sappiamo che non è uno dei 5 difettosi e quindi la probabilità desiderata è:

$$
\begin{array}{r l} & P \{\text { acceptable } | \text { not   defective } \} \\ & = \frac {P \{\text { acceptable,   not   defective } \}}{P \{\text { not   defective } \}} \\ & = \frac {P \{\text { acceptable } \}}{P \{\text { not   defective } \}} \end{array}
$$

dove l'ultima uguaglianza segue poiché il transistor sarà sia accettabile che non difettoso se è accettabile. Pertanto, assumendo che ciascuno dei 40 transistor abbia la stessa probabilità di essere scelto, otteniamo che

$$
P \{\text { acceptable } | \text { not   defective } \} = \frac {2 5 / 4 0}{3 5 / 4 0} = 5 / 7
$$

Bisogna notare che avremmo potuto derivare questa probabilità lavorando direttamente con lo spazio campionario ridotto. Ovvero, poiché sappiamo che il transistor scelto non è difettoso, il problema si riduce al calcolo della probabilità che un transistor, scelto a caso da un contenitore contenente 25 transistor accettabili e 10 parzialmente difettosi, sia accettabile. Questo è chiaramente uguale a $\frac { 2 5 } { 3 5 }$ . ■

EXAMPLE 3.6b L'organizzazione per cui lavora Jones sta organizzando una cena padre-figlio per i dipendenti che hanno almeno un figlio. Ognuno di questi dipendenti è invitato a partecipare insieme al figlio più giovane. Se si sa che Jones ha due figli, qual è la probabilità condizionata che siano entrambi maschi dato che è invitato alla cena? Assumere che lo spazio campionario $S$ sia dato da $S = \{ ( b , b ) , ( b , g ) , ( g , b ) , ( g , g ) \}$ e tutti gli esiti siano ugualmente probabili $[ ( b , g )$ significa, ad esempio, che il figlio più giovane è un maschio e il figlio più anziano è una femmina.

SOLUTION La conoscenza del fatto che Jones è stato invitato alla cena equivale a sapere che ha almeno un figlio maschio. Pertanto, ponendo $B$ come l'evento che entrambi i figli siano maschi, e $A$ l'evento che almeno uno di loro sia un maschio, abbiamo che la probabilità desiderata $P ( B | A )$ è data da

$$
\begin{array}{r l} P (B | A) & = \frac {P (B A)}{P (A)} \\ & = \frac {P (\{(b , b) \})}{P (\{(b , b) , (b , g) , (g , b) \})} \\ & = \frac {\frac {1}{4}}{\frac {3}{4}} = \frac {1}{3} \end{array}
$$

Molti lettori ragionano erroneamente che la probabilità condizionata di due maschi dato almeno uno sia $\frac { 1 } { 2 }$ , invece della corretta $\frac 1 3$ , poiché ragionano che il figlio di Jones non presente alla cena ha la stessa probabilità di essere un maschio o una femmina. Il loro errore, tuttavia, sta nel presumere che queste due possibilità siano ugualmente probabili. Ricordare che inizialmente c'erano quattro esiti ugualmente probabili. Ora l'informazione che almeno un figlio è un maschio equivale a sapere che l'esito non è $( g , g )$ . Pertanto ci restano i tre esiti ugualmente probabili $( b , b ) , ( b , g ) , ( g , b )$ , mostrando così che il figlio di Jones non presente alla cena ha il doppio della probabilità di essere una femmina rispetto a un maschio. ■

Moltiplicando entrambi i membri dell'Equazione 3.6.1 per $P(F)$ otteniamo che

$$
P (E F) = P (F) P (E | F)\tag{3.6.2}
$$

In parole, l'Equazione 3.6.2 afferma che la probabilità che si verifichino sia $E$ che $F$ è uguale alla probabilità che $F$ si verifichi moltiplicata per la probabilità condizionata di $E$ dato che $F$ si è verificata. L'Equazione 3.6.2 è spesso molto utile nel calcolare la probabilità dell'intersezione di eventi. Questo è illustrato dal seguente esempio.

EXAMPLE 3.6c La signora Perez ritiene che ci sia una probabilità del 30 percento che la sua azienda istabilisca una filiale a Phoenix. Se lo farà, è certa al 60 percento che sarà nominata manager di questa nuova operazione. Qual è la probabilità che Perez sarà il manager della filiale di Phoenix?

SOLUTION Se poniamo $B$ come l'evento che l'azienda istabilisca una filiale a Phoenix e $M$ l'evento che Perez venga nominata manager di Phoenix, allora la probabilità desiderata è $P(BM)$, che si ottiene come segue:

$$
\begin{array}{r l} P (B M) & = P (B) P (M | B) \\ & = (. 3) (. 6) \\ & = . 1 8 \end{array}
$$

Pertanto, c'è una probabilità dell'18 percento che Perez sarà il manager di Phoenix. ■

## 3.7 FORMULA DI BAYES

Siano E e F eventi. Possiamo esprimere E come

$$
E = E F \cup E F ^ {c}
$$

perché, affinché un punto sia in E, esso deve trovarsi sia in E che in F oppure essere in E ma non in F. (Vedere Figura 3.6.) Poiché EF e $E F ^ { c }$ sono chiaramente mutuamente esclusivi, abbiamo per l'Assioma 3 che

$$
\begin{array}{r l} & P (E) = P (E F) + P (E F ^ {c}) \\ & \quad = P (E | F) P (F) + P (E | F ^ {c}) P (F ^ {c}) \\ & \quad = P (E | F) P (F) + P (E | F ^ {c}) [ 1 - P (F) ] \end{array}\tag{3.7.1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/644dc66b5fd178d7cc1ec2ea5982f6c5ccb1a35a6c941e0c9f1aaa0e59a2ff3e.jpg)



FIGURA 3.6 E = EF ∪ EF <sup>c</sup> .


L'equazione 3.7.1 afferma che la probabilità dell'evento E è una media ponderata della probabilità condizionata di E dato che F si è verificato e della probabilità condizionata di E dato che F non si è verificato: ogni probabilità condizionata riceve lo stesso peso che l'evento su cui è condizionata ha di verificarsi. È una formula estremamente utile, poiché il suo utilizzo spesso ci consente di determinare la probabilità di un evento "condizionando" prima se un secondo evento si è verificato o meno. Ovvero, esistono molti casi in cui è difficile calcolare direttamente la probabilità di un evento, ma è semplice calcolarla una volta che sappiamo se un secondo evento si è verificato o meno.

EXAMPLE 3.7a Una compagnia di assicurazioni ritiene che le persone possano essere divise in due classi — quelle inclini agli incidenti e quelle che non lo sono. Le loro statistiche mostrano che una persona incline agli incidenti avrà un incidente in qualche momento entro un periodo fisso di 1 anno con probabilità .4, mentre questa probabilità scende a .2 per una persona non incline agli incidenti. Se assumiamo che il 30 percento della popolazione sia incline agli incidenti, qual è la probabilità che un nuovo assicurato abbia un incidente entro un anno dall'acquisto di una polizza?

SOLUTION Otteniamo la probabilità desiderata condizionando prima se l'assicurato è incline agli incidenti o meno. Sia $A _ { 1 }$ l'evento che l'assicurato avrà un incidente entro un anno dall'acquisto; e sia A l'evento che l'assicurato è incline agli incidenti. Pertanto, la probabilità desiderata, $P ( A _ { 1 } )$ ), è data da

$$
\begin{array}{c} P (A _ {1}) = P (A _ {1} | A) P (A) + P (A _ {1} | A ^ {c}) P (A ^ {c}) \\ = (. 4) (. 3) + (. 2) (. 7) = . 2 6 \quad \blacksquare \end{array}
$$

Nella serie successiva di esempi, indicheremo come rivalutare una valutazione iniziale della probabilità alla luce di informazioni aggiuntive (o nuove). Ovvero, mostreremo come incorporare nuove informazioni con una valutazione iniziale della probabilità per ottenere una probabilità aggiornata.

EXAMPLE 3.7b Riconsideriamo l'Esempio 3.7a e supponiamo che un nuovo assicurato abbia avuto un incidente entro un anno dall'acquisto della sua polizza. Qual è la probabilità che sia incline agli incidenti?

SOLUTION Inizialmente, al momento in cui l'assicurato ha acquistato la sua polizza, avevamo assunto che ci fosse una probabilità del 30 percento che fosse incline agli incidenti. Ovvero, $P ( A ) = . 3 .$

Tuttavia, sulla base del fatto che ha avuto un incidente entro un anno, rivalutiamo ora la sua probabilità di essere incline agli incidenti come segue.

$$
\begin{array}{r l} P (A | A _ {1}) & = \frac {P (A A _ {1})}{P (A _ {1})} \\ & = \frac {P (A) P (A _ {1} | A)}{P (A _ {1})} \\ & = \frac {(. 3) (. 4)}{. 2 6} = \frac {6}{1 3} = . 4 6 1 5 \end{array}
$$

EXAMPLE 3.7c Rispondendo a una domanda in un test a scelta multipla, uno studente conosce la risposta o indovina. Sia $\boldsymbol { \underline { P } }$ la probabilità che conosca la risposta e $1 - p$ la probabilità che indovini. Assumiamo che uno studente che indovina la risposta sarà corretto con probabilità 1/m, dove m è il numero di alternative a scelta multipla. Qual è la probabilità condizionata che uno studente conoscesse la risposta a una domanda dato che l'ha risposta correttamente?

SOLUTION Sia $C$ e K, rispettivamente, gli eventi che lo studente risponde correttamente alla domanda e l'evento che conosce effettivamente la risposta. Per calcolare

$$
P (K | C) = \frac {P (K C)}{P (C)}
$$

notiamo prima che

$$
\begin{array}{r l} P (K C) & = P (K) P (C | K) \\ & = p \cdot 1 \\ & = p \end{array}
$$

Per calcolare la probabilità che lo studente risponda correttamente, condizioniamo se conosce la risposta o meno. Ovvero,

$$
\begin{array}{c} {P (C) = P (C | K) P (K) + P (C | K ^ {c}) P (K ^ {c})} \\ {= p + (1 / m) (1 - p)} \end{array}
$$

Pertanto, la probabilità desiderata è data da

$$
P (K | C) = \frac {p}{p + (1 / m) (1 - p)} = \frac {m p}{1 + (m - 1) p}
$$

Così, ad esempio, se $\begin{array} { r } { m = 5 , p = \frac { 1 } { 2 } } \end{array}$ , allora la probabilità che uno studente conoscesse la risposta a una domanda a cui ha risposto correttamente è ${ \frac { 5 } { 6 } } .$ . ■

Esempio 3.7d Un test del sangue di laboratorio è efficace al 99 percento nel rilevare una determinata malattia quando questa è, di fatto, presente. Tuttavia, il test fornisce anche un risultato "falso positivo" per l'1 percento delle persone sane sottoposte a test. (Ciò significa che, se viene testata una persona sana, allora, con probabilità .01, il risultato del test implicherà che lei abbia la malattia.) Se lo .5 percento della popolazione ha effettivamente la malattia, qual è la probabilità che una persona abbia la malattia dato che il suo risultato del test è positivo?

SOLUZIONE Sia D l'evento che la persona testata ha la malattia e E l'evento che il suo risultato del test è positivo. La probabilità desiderata $P ( D | E )$ si ottiene da

$$
\begin{array}{r l} P (D | E) & = \frac {P (D E)}{P (E)} \\ & = \frac {P (E | D) P (D)}{P (E | D) P (D) + P (E | D ^ {c}) P (D ^ {c})} \\ & = \frac {(. 9 9) (. 0 0 5)}{(. 9 9) (. 0 0 5) + (. 0 1) (. 9 9 5)} \\ & = . 3 3 2 2 \end{array}
$$

Pertanto, solo il 33 percento delle persone i cui risultati del test sono positivi ha effettivamente la malattia. Poiché molti studenti sono spesso sorpresi da questo risultato (perché si aspettavano che questa cifra fosse molto più alta dato che il test del sangue sembra essere un buon test), probabilmente vale la pena presentare un secondo argomento che, sebbene meno rigoroso del precedente, è probabilmente più rivelatore. Lo facciamo ora.

Poiché lo .5 percento della popolazione ha effettivamente la malattia, ne consegue che, in media, 1 persona su ogni 200 testate la avrà. Il test confermerà correttamente che questa persona ha la malattia con probabilità .99. Pertanto, in media, su ogni 200 persone testate, il test confermerà correttamente che .99 persone hanno la malattia. D'altra parte, tra le (in media) 199 persone sane, il test dichiarerà erroneamente che (199) (.01) di queste persone hanno la malattia. Di conseguenza, per ogni .99 persona malata che il test dichiara correttamente come malata, ci sono (in media) 1.99 persone sane che il test dichiara erroneamente come malate. Pertanto, la proporzione di volte in cui il risultato del test è corretto quando dichiara che una persona è malata è

$$
\frac {. 9 9}{. 9 9 + 1 . 9 9} = . 3 3 2 2 \quad \blacksquare
$$

L'equazione 3.7.1 è utile anche quando si deve rivalutare le proprie probabilità (personali) alla luce di informazioni aggiuntive. Ad esempio, consideriamo i seguenti esempi.

Esempio 3.7e In una determinata fase di un'indagine criminale, l'ispettore incaricato è convinto al 60 percento della colpevolezza di un certo sospettato. Supponiamo ora che venga scoperta una nuova prova che mostra che il criminale possiede una certa caratteristica (come la mancata destrezza manuale, la calvizie, i capelli castani, ecc.). Se il 20 percento della popolazione possiede questa caratteristica, quanto sicuro della colpevolezza del sospettato dovrebbe essere ora l'ispettore se si scopre che il sospettato appartiene a questo gruppo?

SOLUZIONE Ponendo G per l'evento che il sospettato è colpevole e C per l'evento che possiede la caratteristica del criminale, abbiamo

$$
P (G | C) = \frac {P (G C)}{P (C)}
$$

Ora

$$
\begin{array}{r l} & P (G C) = P (G) P (C | G) \\ & \qquad = (. 6) (1) \\ & \qquad = . 6 \end{array}
$$

Per calcolare la probabilità che il sospettato abbia la caratteristica, condizioniamo sul fatto che sia colpevole o meno. Cioè,

$$
\begin{array}{r l} P (C) & = P (C | G) P (G) + P (C | G ^ {c}) P (G ^ {c}) \\ & = (1) (. 6) + (. 2) (. 4) \\ & = . 6 8 \end{array}
$$

dove abbiamo supposto che la probabilità che il sospettato abbia la caratteristica se è, di fatto, innocente sia pari a .2, la proporzione della popolazione che possiede la caratteristica. Di conseguenza

$$
P (G | C) = \frac {6 0}{6 8} = . 8 8 2
$$

e quindi l'ispettore dovrebbe ora essere sicuro all'88 percento della colpevolezza del sospettato. ■

Esempio 3.7e (continuazione) Supponiamo ora che la nuova prova sia soggetta a diverse interpretazioni possibili e, di fatto, mostri solo che è probabile al 90 percento che il criminale possieda questa certa caratteristica. In questo caso, quanto sarebbe probabile che il sospettato sia colpevole (supponendo, come prima, che abbia questa caratteristica)?

SOLUZIONE In questo caso, la situazione è come prima con l'eccezione che la probabilità che il sospettato abbia la caratteristica dato che è colpevole è ora .9 (anziché 1). Di conseguenza,

$$
\begin{array}{c} P (G | C) = \frac {P (G C)}{P (C)} \\ = \frac {P (G) P (C | G)}{P (C | G) P (G) + P (C | G ^ {c}) P (G ^ {c})} \end{array}
$$

$$
\begin{array}{l} = \frac {(. 6) (. 9)}{(. 9) (. 6) + (. 2) (. 4)} \\ = \frac {5 4}{6 2} = . 8 7 1 \end{array}
$$

che è leggermente inferiore rispetto al caso precedente (perché?). ■

L'equazione 3.7.1 può essere generalizzata nel seguente modo. Supponiamo che $F _ { 1 } , F _ { 2 } , \ldots , F _ { n }$ siano eventi mutuamente esclusivi tali che

$$
\bigcup_ {i = 1} ^ {n} F _ {i} = S
$$

In altre parole, esattamente uno degli eventi $F _ { 1 } , F _ { 2 } , \ldots , F _ { n }$ deve verificarsi. Scrivendo 

$$
E = \bigcup_ {i = 1} ^ {n} E F _ {i}
$$

e utilizzando il fatto che gli eventi $E F _ { i } , i = 1 , \dots , n$ sono mutuamente esclusivi, otteniamo che 

$$
\begin{array}{c} P (E) = \sum_ {i = 1} ^ {n} P (E F _ {i}) \\ = \sum_ {i = 1} ^ {n} P (E | F _ {i}) P (F _ {i}) \end{array}\tag{3.7.2}
$$

Così, l'Equazione 3.7.2 mostra come, per dati eventi $F _ { 1 } , F _ { 2 } , \ldots , F _ { n }$ di cui uno e un solo deve verificarsi, possiamo calcolare $P ( E )$ "condizionando" prima su quale dei $F _ { i }$ si verifichi. Ovvero, afferma che $P ( E )$ è uguale a una media ponderata di $P ( E | F _ { i } )$, con ogni termine pesato dalla probabilità dell'evento su cui è condizionato.

Supponiamo ora che $E$ si sia verificato e ci interessi determinare quale dei $F _ { j }$ si sia verificato anche. Dall'Equazione 3.7.2, abbiamo che 

$$
\begin{array}{c} P (F _ {j} | E) = \frac {P (E F _ {j})}{P (E)} \\ = \frac {P (E | F _ {j}) P (F _ {j})}{\sum_ {i = 1} ^ {n} P (E | F _ {i}) P (F _ {i})} \end{array}\tag{3.7.3}
$$

L'Equazione 3.7.3 è nota come formula di Bayes, dal filosofo inglese Thomas Bayes. Se pensiamo agli eventi $F _ { j }$ come possibili "ipotesi" su un determinato argomento, allora 

la formula di Bayes può essere interpretata come il modo in cui le opinioni su queste ipotesi sostenute prima dell'esperimento [ovvero, le $P ( F _ { j } ) ]$ ] dovrebbero essere modificate dalle prove dell'esperimento.

EXAMPLE 3.7f Un aereo è scomparso e si presume che fosse ugualmente probabile che sia precipitato in una qualsiasi delle tre regioni possibili. Sia $1 - \alpha _ { i }$ la probabilità che l'aereo venga trovato durante una ricerca nella i-esima regione quando l'aereo ${ \mathrm { i } } s ,$ di fatto, in quella regione, $i = 1 , 2 , 3$ . (Le costanti $\alpha _ { i }$ sono chiamate probabilità di mancato avvistamento perché rappresentano la probabilità di non vedere l'aereo; esse sono generalmente attribuibili alle condizioni geografiche e ambientali delle regioni.) Qual è la probabilità condizionata che l'aereo si trovi nella i-esima regione, dato che una ricerca della regione 1 non ha avuto successo, $i = 1 , 2 , 3 ?$ 

SOLUTION Sia $R _ { i } , i = 1 , 2 , 3$ l'evento che l'aereo si trova nella regione i; e sia E l'evento che una ricerca della regione 1 non ha avuto successo. Dalla formula di Bayes, otteniamo 

$$
\begin{array}{l} P (R _ {1} | E) = \frac {P (E R _ {1})}{P (E)} \\ \qquad = \frac {P (E | R _ {1}) P (R _ {1})}{\sum_ {i = 1} ^ {3} P (E | R _ {i}) P (R _ {i})} \\ \qquad = \frac {(\alpha_ {1}) (1 / 3)}{(\alpha_ {1}) (1 / 3) + (1) (1 / 3) + (1) (1 / 3)} \\ \qquad = \frac {\alpha_ {1}}{\alpha_ {1} + 2} \end{array}
$$

Per $j = 2 ,$ 3, 

$$
\begin{array}{r l} P (R _ {j} | E) & = \frac {P (E | R _ {j}) P (R _ {j})}{P (E)} \\ & = \frac {(1) (1 / 3)}{(\alpha_ {1}) 1 / 3 + 1 / 3 + 1 / 3} \\ & = \frac {1}{\alpha_ {1} + 2}, \qquad j = 2, 3 \end{array}
$$

Così, ad esempio, se $\alpha _ { 1 } = . 4 _ { \mathrm { : } }$ , allora la probabilità condizionata che l'aereo si trovi nella regione 1 dato che una ricerca di quella regione non lo ha scoperto è ${ \frac { 1 } { 6 } } .$ . ■ 

## 3.8 EVENTI INDIPENDENTI

Gli esempi precedenti in questo capitolo mostrano che $P ( E | F )$ , la probabilità condizionata di $E$ dato $F ,$ non è generalmente uguale a $P ( E )$ ), la probabilità non condizionata di E. In altre parole, sapere che F si è verificato cambia generalmente le probabilità di occorrenza di $E ' s$. Nei casi speciali in cui $P ( E | F )$ è effettivamente uguale a $P ( E )$ ), diciamo che E è indipendente da F. Ovvero, E è indipendente da F se la conoscenza del fatto che F si è verificato non cambia la probabilità che E si verifichi.

Poiché $P ( E | F ) = P ( E F ) / P ( F )$ , vediamo che E è indipendente da F se 

$$
P (E F) = P (E) P (F)\tag{3.8.1}
$$

Poiché questa equazione è simmetrica in E e F, essa mostra che ogni volta che E è indipendente da F, lo è anche F da E. Abbiamo quindi quanto segue.

## Definizione

Si dice che due eventi E e F sono indipendenti se vale l'Equazione 3.8.1. Due eventi E e F che non sono indipendenti sono detti dipendenti.

EXAMPLE 3.8a Una carta viene estratta a caso da un mazzo ordinario di 52 carte da gioco. Se A è l'evento in cui la carta estratta è un asso e H è l'evento in cui è di cuori, allora A e H sono indipendenti, poiché $\begin{array} { r } { P ( A H ) = \frac { 1 } { 5 2 } } \end{array}$ , mentre $\textstyle P ( A ) = { \frac { 4 } { 5 2 } }$ e $\begin{array} { r } { P ( H ) = \frac { 1 3 } { 5 2 } } \end{array}$ ■

EXAMPLE 3.8b Se facciamo in modo che E denoti l'evento in cui il prossimo presidente è un Repubblicano e F l'evento in cui ci sarà un forte terremoto entro il prossimo anno, allora la maggior parte delle persone sarebbe probabilmente disposta ad assumere che E e F siano indipendenti. Tuttavia, ci sarebbe probabilmente qualche controversia sul fatto che sia ragionevole assumere che E sia indipendente da G, dove G è l'evento in cui ci sarà una recessione entro i prossimi due anni. ■

Mostriamo ora che se E è indipendente da F allora E è anche indipendente da $F ^ { c }$ .

PROPOSTA 3.8.1 Se E e F sono indipendenti, allora lo sono anche E e $F ^ { c }$ .

## Dimostrazione

Assumiamo che E e F siano indipendenti. Poiché $E = E F \cup E F ^ { c }$ , e EF e $E F ^ { c }$ sono ovviamente mutuamente esclusivi, abbiamo che

$$
\begin{array}{r l} P (E) & = P (E F) + P (E F ^ {c}) \\ & = P (E) P (F) + P (E F ^ {c}) \quad \text { by   the   independence   of } E \text { and } F \end{array}
$$

o equivalentemente,

$$
\begin{array}{c} {P (E F ^ {c}) = P (E) (1 - P (F))} \\ {= P (E) P (F ^ {c})} \end{array}
$$

e il risultato è dimostrato. 

Pertanto, se E è indipendente da $F ,$ allora la probabilità dell'occorrenza di $E ' s$ non cambia in base all'informazione su se o meno $F$ si è verificata.

Supponiamo ora che E sia indipendente da $F$ e sia anche indipendente da $G .$ . E allora è necessariamente indipendente da $F G ?$ ? La risposta, in modo alquanto sorprendente, è no. Consideriamo il seguente esempio.

EXAMPLE 3.8c Due dadi equi vengono lanciati. Sia $E _ { 7 }$ l'evento in cui la somma dei dadi è 7. Sia F l'evento in cui il primo dado è uguale a 4 e sia $T$ l'evento in cui il secondo dado è uguale a 3. Ora si può dimostrare (vedere Problema 36) che $E _ { 7 }$ è indipendente da F e che $E _ { 7 }$ è anche indipendente da $T ;$ ma chiaramente $E _ { 7 }$ non è indipendente da $F T$ [poiché $P ( E _ { 7 } | F T ) = 1 ]$ ■

Sembrerebbe derivare dal precedente esempio che una definizione appropriata dell'indipendenza di tre eventi E, F e $G$ dovrebbe andare oltre il semplice assunto che tutte le coppie di eventi $\binom { 3 } { 2 }$ siano indipendenti. Siamo quindi portati alla seguente definizione.

## Definizione

I tre eventi E, F e G si dicono indipendenti se

$$
\begin{array}{c} {P (E F G) = P (E) P (F) P (G)} \\ {P (E F) = P (E) P (F)} \\ {P (E G) = P (E) P (G)} \\ {P (F G) = P (F) P (G)} \end{array}
$$

Si noti che se gli eventi E, F, G sono indipendenti, allora E sarà indipendente da qualsiasi evento formato da $F$ e G. Ad esempio, E è indipendente da $F \cup G$ poiché

$$
\begin{array}{r l} & P (E (F \cup G)) = P (E F \cup E G) \\ & \qquad = P (E F) + P (E G) - P (E F G) \\ & \qquad = P (E) P (F) + P (E) P (G) - P (E) P (F G) \\ & \qquad = P (E) [ P (F) + P (G) - P (F G) ] \\ & \qquad = P (E) P (F \cup G) \end{array}
$$

Naturalmente possiamo anche estendere la definizione di indipendenza a più di tre eventi. Gli eventi $E _ { 1 } , E _ { 2 } , \ldots , E _ { n }$ si dicono indipendenti se per ogni sottoinsieme $E _ { 1 ^ { \prime } } , E _ { 2 ^ { \prime } } , \ldots , E _ { r ^ { \prime } } , r \leq n _ { ! }$ , di questi eventi

$$
P (E _ {1 ^ {\prime}} E _ {2 ^ {\prime}} \cdot \cdot \cdot E _ {r ^ {\prime}}) = P (E _ {1 ^ {\prime}}) P (E _ {2 ^ {\prime}}) \cdot \cdot \cdot P (E _ {r ^ {\prime}})
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/caa38dcbcec1f6283bd404ec03a8228e93fdb49cd6e5df85ec23e25db7a788b0.jpg)



FIGURA 3.7 Sistema in parallelo: funziona se la corrente fluisce da A a B.


A volte accade che l'esperimento di probabilità in considerazione consista nell'esecuzione di una sequenza di sottoesperimenti. Ad esempio, se l'esperimento consiste nel lanciare continuamente una moneta, allora possiamo considerare ogni lancio come un sottoesperimento. In molti casi è ragionevole assumere che i risultati di qualsiasi gruppo di sottoesperimenti non abbiano alcun effetto sulle probabilità dei risultati degli altri sottoesperimenti. Se questo è il caso, allora diciamo che i sottoesperimenti sono indipendenti.

EXAMPLE 3.8d Un sistema composto da n componenti separati si dice essere un sistema in parallelo se funziona quando almeno una delle componenti funziona. (Vedere Figura 3.7.) Per tale sistema, se la componente i, indipendente dalle altre componenti, funziona con probabilità $p _ { i } , i = 1 , \ldots , n ,$ quale è la probabilità che il sistema funzioni?

SOLUTION Sia $A _ { i }$ l'evento che la componente i funziona. Allora

$$
\begin{array}{l} P \{\text {system functions} \} = 1 - P \{\text {system does not function} \} \\ \qquad = 1 - P \{\text {all components do not function} \} \\ \qquad = 1 - P \big (A _ {1} ^ {c} A _ {2} ^ {c} \dots A _ {n} ^ {c} \big) \\ \qquad = 1 - \prod_ {i = 1} ^ {n} (1 - p _ {i}) \quad \text {by independence} \end{array}
$$

EXAMPLE 3.8e Viene raccolta una serie di k coupon, ciascuno dei quali è indipendentemente un coupon di tipo $j$ con probabilità $\begin{array} { r } { p _ { j } , \sum _ { j = 1 } ^ { n } \ p _ { j } \ = \ 1 } \end{array}$. Trova la probabilità che la serie contenga un coupon di tipo j dato che contiene un coupon di tipo $i , i \neq j$

SOLUTION Sia $A _ { r }$ l'evento che la serie contiene un coupon di tipo r. Allora

$$
P (A _ {j} | A _ {i}) = \frac {P (A _ {j} A _ {i})}{P (A _ {i})}
$$

Per calcolare $P ( A _ { i } )$ e $P ( A _ { j } A _ { i } )$ , considera la probabilità dei loro complementari:

$$
\begin{array}{r l} & P (A _ {i}) = 1 - P (A _ {i} ^ {c}) \\ & \quad = 1 - P \{\text {no coupon is type} i \} \\ & \quad = 1 - (1 - p _ {i}) ^ {k} \end{array}
$$

$$
\begin{array}{r l} & P (A _ {i} A _ {j}) = 1 - P (A _ {i} ^ {c} \cup A _ {j} ^ {c}) \\ & \quad = 1 - [ P (A _ {i} ^ {c}) + P (A _ {j} ^ {c}) - P (A _ {i} ^ {c} A _ {j} ^ {c}) ] \\ & \quad = 1 - (1 - p _ {i}) ^ {k} - (1 - p _ {j}) ^ {k} + P \{\text { no   coupon   is   type } i \text { or   type } j \} \\ & \quad = 1 - (1 - p _ {i}) ^ {k} - (1 - p _ {j}) ^ {k} + (1 - p _ {i} - p _ {j}) ^ {k} \end{array}
$$

dove l'uguaglianza finale segue perché ciascuno dei k coupon è, indipendentemente, né di tipo i né di tipo j con probabilità $1 - p _ { i } - p _ { j }$. Di conseguenza,

$$
P (A _ {j} | A _ {i}) = \frac {1 - (1 - p _ {i}) ^ {k} - (1 - p _ {j}) ^ {k} + (1 - p _ {i} - p _ {j}) ^ {k}}{1 - (1 - p _ {i}) ^ {k}} \quad \blacksquare
$$

## Problemi

1. Una scatola contiene tre biglie — una rossa, una verde e una blu. Considera un esperimento che consiste nel prendere una biglia dalla scatola, poi rimetterla nella scatola e estrarre una seconda biglia dalla scatola. Descrivi lo spazio campionario. Ripeti per il caso in cui la seconda biglia viene estratta senza aver prima rimesso la prima biglia.

2. Un esperimento consiste nel lanciare una moneta tre volte. Qual è lo spazio campionario di questo esperimento? Quale evento corrisponde all'esperimento che risulta in più teste che code?

3. Sia $S = \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 \} , E = \{ 1 , 3 , 5 , 7 \} , F = \{ 7 , 4 , 6 \} , G = \{ 1 , 4 \}$ . Trova (a) EF; (c) $E G ^ { c } ;$ (e) $E ^ { c } ( F \cup G )$ ; (b) $E \cup F G ,$ (d) $E F ^ { c } \cup G ;$ (f ) $E G \cup F G .$

4. Vengono lanciati due dadi. Sia E l'evento che la somma dei dadi è dispari, sia F l'evento che il primo dado cade su 1, e sia G l'evento che la somma è 5. Descrivi gli eventi EF $E \cup F , F G , E F ^ { c } , E F G .$

5. Un sistema è composto da quattro componenti, ciascuna delle quali è o funzionante o guasta. Considera un esperimento che consiste nell'osservare lo stato di ogni componente, e sia il risultato dell'esperimento dato dal vettore $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } )$ dove x<sub>i</sub> è uguale a 1 se la componente i è funzionante ed è uguale a 0 se la componente i è guasta.

(a) Quanti risultati sono nello spazio campionario di questo esperimento?

(b) Supponiamo che il sistema funzionerà se le componenti 1 e 2 sono entrambe funzionanti, oppure se le componenti 3 e 4 sono entrambe funzionanti. Specifica tutti i risultati nell'evento in cui il sistema funziona.

(c) Sia E l'evento che le componenti 1 e 3 sono entrambe guaste. Quanti risultati sono contenuti nell'evento E?

## Problemi

6. Siano E, F, G tre eventi. Trova le espressioni per gli eventi che di E, F, G 

(a) solo E si verifica; 

(b) sia E che G si verificano ma non F; 

(c) almeno uno degli eventi si verifica; 

(d) almeno due degli eventi si verificano; 

(e) tutti e tre si verificano; 

(f) nessuno degli eventi si verifica; 

(g) al massimo uno di essi si verifica; 

(h) al massimo due di essi si verificano; 

(i) esattamente due di essi si verificano; 

(j) al massimo tre di essi si verificano. 

7. Trova espressioni semplici per gli eventi 

(a) $E \cup E ^ { c } ;$ 

(b) $E E ^ { c } ;$ 

(c) $( E \cup F ) ( E \cup F ^ { c } ) ;$ 

(d) $( E \cup F ) ( E ^ { c } \cup F ) E \cup F ^ { c } ) ;$ 

(e) $( E \cup F ) ( F \cup G ) .$ 

8. Usa i diagrammi di Venn (o qualsiasi altro metodo) per mostrare che 

(a) $E F \subset E , E \subset E \cup F ;$ 

(b) $\mathsf { i f } E \subset F \mathrm { ~ t h e n ~ } F ^ { c } \subset E ^ { c } ;$ 

(c) le leggi commutative sono valide; 

(d) le leggi associative sono valide; 

(e) $F = F E \cup F E ^ { c } ;$ 

(f) $E \cup F = E \cup E ^ { c } F ;$ 

(g) le leggi di DeMorgan sono valide. 

9. Per il seguente diagramma di Venn, descrivi in termini di E, F e G gli eventi indicati nel diagramma dai numeri romani da I a VII. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/c538e5321e194847fee6158dcba932ea4282d4d7ed7f9f7c31d1517ab210ddec.jpg)


10. Mostra che se $E \subset F$ allora $P ( E ) \leq P ( F )$ . (Suggerimento: Scrivi F come l'unione di due eventi mutuamente esclusivi, uno dei quali è E.) 

11. Dimostra la disuguaglianza di Boole, ovvero che 

$$
P \left(\bigcup_ {i = 1} ^ {n} E _ {i}\right) \leq \sum_ {i = 1} ^ {n} P (E _ {i})
$$

12. Se $P ( E ) ~ = ~ . 9$ e $P ( F ) ~ = ~ . 9  \it$, mostra che $P ( E F ) \ge . 8$ . In generale, dimostra la disuguaglianza di Bonferroni, ovvero che 

$$
P (E F) \geq P (E) + P (F) - 1
$$

13. Dimostra che 

(a) $P ( E F ^ { c } ) = P ( E ) - P ( E F )$ 

(b) $P ( E ^ { c } F ^ { c } ) = 1 - P ( E ) - P ( F ) + P ( E F )$ 

14. Mostra che la probabilità che esattamente uno degli eventi E o F si verifichi è uguale a $P ( E ) + P ( F ) - 2 P ( E F )$ 

15. Calcola ${ \binom { 9 } { 3 } } , { \binom { 9 } { 6 } } , { \binom { 7 } { 2 } } , { \binom { 7 } { 5 } } , { \binom { 1 0 } { 7 } }$ 

16. Mostra che 

$$
\binom{n}{r} = \binom{n}{n - r}
$$

Presenta ora un argomento combinatorio per quanto sopra spiegando perché una scelta di r elementi da un insieme di dimensione n è equivalente a una scelta di $n - r$ elementi da quell'insieme. 

17. Mostra che 

$$
\binom {n} {r} = \binom {n - 1} {r - 1} + \binom {n - 1} {r}
$$

Per un argomento combinatorio, considera un insieme di n elementi e fissa l'attenzione su uno di questi elementi. Quanti diversi insiemi di dimensione r contengono questo elemento, e quanti no? 

18. Un gruppo di 5 ragazzi e 10 ragazze è allineato in ordine casuale — vale a dire, si assume che ciascuna delle 15! permutazioni sia ugualmente probabile. 

(a) Qual è la probabilità che la persona nella 4ª posizione sia un ragazzo? 

(b) Che dire della persona nella 12ª posizione? 

(c) Qual è la probabilità che un particolare ragazzo sia nella 3ª posizione? 

19. Considera un insieme di 23 persone non correlate. Poiché ogni coppia di persone condivide lo stesso compleanno con probabilità 1/365, e ci sono ${ \binom { 2 3 } { 2 } } = 2 5 3$ coppie, perché la probabilità che almeno due persone abbiano lo stesso compleanno non è uguale a 253/365? 

20. Una città contiene 4 riparatori di televisori. Se si guastano 4 set, qual è la probabilità che vengano chiamati esattamente 2 dei riparatori? Quali assunzioni stai facendo? 

21. Una donna ha n chiavi, di cui una aprirà la sua porta. Se prova le chiavi a caso, scartando quelle che non funzionano, qual è la probabilità che aprirà la porta al suo k-esimo tentativo? E se non scarta le chiavi provate in precedenza? 

22. Un armadio contiene 8 paia di scarpe. Se vengono selezionate casualmente 4 scarpe, qual è la probabilità che ci sia (a) nessun paio completo e (b) esattamente 1 paio completo? 

23. Di tre carte, una è dipinta di rosso su entrambi i lati; una è dipinta di nero su entrambi i lati; e una è dipinta di rosso su un lato e nera sull'altro. Una carta viene scelta casualmente e posta su un tavolo. Se il lato rivolto verso l'alto è rosso, qual è la probabilità che anche l'altro lato sia rosso? 

24. Una coppia ha 2 figli. Qual è la probabilità che entrambi siano femmine se il primogenito è una femmina? 

25. Il cinquantadue per cento degli studenti di un certo college sono femmine. Il cinque per cento degli studenti in questo college studiano informatica. Il due per cento degli studenti sono donne che studiano informatica. Se uno studente viene selezionato a caso, trova la probabilità condizionata che

(a) questo studente è di sesso femminile, dato che lo studente si laurea in informatica; (b) questo studente si laurea in informatica, dato che lo studente è di sesso femminile. 

26. Un totale di 500 coppie di lavoratori sposati sono stati intervistati sui loro stipendi annuali, con i seguenti risultati. 

<table><tr><td rowspan="2">Moglie</td><td colspan="2">Marito</td></tr><tr><td>Meno di $25,000</td><td>More than $25,000</td></tr><tr><td>Meno di $25,000</td><td>212</td><td>198</td></tr><tr><td>More than $25,000</td><td>36</td><td>54</td></tr></table>

Così, ad esempio, in 36 delle coppie la moglie ha guadagnato di più e il marito ha guadagnato meno di $25,000. Se una delle coppie viene scelta casualmente, qual è 

(a) la probabilità che il marito guadagni meno di $25,000; 

(b) la probabilità condizionata che la moglie guadagni più di $25,000 dato che il marito guadagna più di tale importo; 

(c) la probabilità condizionata che la moglie guadagni più di $25,000 dato che il marito guadagna meno di tale importo? 

27. Ci sono due fabbriche locali che producono radio. Ogni radio prodotta presso la fabbrica A è difettosa con probabilità .05, mentre ognuna prodotta presso la fabbrica B è difettosa con probabilità .01. Supponiamo che tu acquisti due radio prodotte nella stessa fabbrica, che ha la stessa probabilità di essere stata la fabbrica A o la fabbrica B. Se la prima radio che controlli è difettosa, qual è la probabilità condizionata che anche l'altra sia difettosa? 

28. Vengono lanciati un dado rosso, un dado blu e un dado giallo (tutti a sei facce). Ci interessa la probabilità che il numero che appare sul dado blu sia minore di quello che appare sul dado giallo, il quale è minore di quello che appare sul dado rosso. (Ovvero, se B (R) [Y ] è il numero che appare sul dado blu (rosso) [giallo], allora ci interessa $P ( B < Y < R )$ . ) 

(a) Qual è la probabilità che nessun dado si fermi sullo stesso numero? 

(b) Dato che nessun dado si ferma sullo stesso numero, qual è la probabilità condizionata che $B < Y < R \Rsh$ 

(c) Qual è $P ( B < Y < R ) \vdots$ 

(d) Se consideriamo l'esito dell'esperimento come il vettore B, R, Y, quanti esiti ci sono nello spazio campionario? 

(e) Senza usare la risposta a (c), determina il numero di esiti che risultano in $B < Y < R$ 

(f ) Usa i risultati delle parti (d) e (e) per verificare la tua risposta alla parte (c). 

29. Chiedi al tuo vicino di annaffiare una pianta malata mentre sei in vacanza. Senza acqua morirà con probabilità .8; con acqua morirà con probabilità .15. Sei sicuro al 90 percento che il tuo vicino si ricorderà di annaffiare la pianta. 

(a) Qual è la probabilità che la pianta sia viva quando tornerai? 

(b) Se è morta, qual è la probabilità che il tuo vicino abbia dimenticato di annaffiarla? 

30. Due palline, ciascuna con la stessa probabilità di essere colorata rossa o blu, vengono messe in un'urna. Ad ogni stadio una delle palline viene scelta casualmente, il suo colore viene annotato e viene poi rimessa nell'urna. Se le prime due palline scelte sono colorate rosse, qual è la probabilità che 

(a) entrambe le palline nell'urna siano colorate rosse; 

(b) la prossima pallina scelta sarà rossa? 

31. Un totale di 600 delle 1.000 persone in una comunità per pensionati si classificano come Repubblicani, mentre gli altri si classificano come Democratici. In un'elezione locale in cui tutti hanno votato, 60 Repubblicani hanno votato per il candidato Democratico e 50 Democratici hanno votato per il candidato Repubblicano. Se un membro della comunità scelto casualmente ha votato per il Repubblicano, qual è la probabilità che sia un Democratico? 

32. Ognuna delle 2 palline viene dipinta di nero o oro e poi posta in un'urna. Supponiamo che ogni pallina sia colorata di nero con probabilità <sup>1</sup> , e che questi eventi siano indipendenti. 

(a) Supponiamo di ottenere l'informazione che la vernice oro è stata usata (e quindi almeno una delle palline è dipinta d'oro). Calcola la probabilità condizionata che entrambe le palline siano dipinte d'oro.

(b) Supponiamo ora che l'urna si ribalti e una pallina cada fuori. È dipinta d'oro. Qual è la probabilità che entrambe le palline siano d'oro in questo caso? Spiegate.

33. Ognuno dei 2 armadietti identici nell'aspetto ha 2 cassetti. L'armadietto A contiene una moneta d'argento in ogni cassetto, e l'armadietto B contiene una moneta d'argento in uno dei suoi cassetti e una moneta d'oro nell'altro. Viene selezionato casualmente un armadietto, ne viene aperto uno dei cassetti e viene trovata una moneta d'argento. Qual è la probabilità che ci sia una moneta d'argento nell'altro cassetto?

34. Il cancro alla prostata è il tipo di cancro più comune riscontrato nei maschi. Come indicatore del fatto che un uomo abbia il cancro alla prostata, i medici eseguono spesso un test che misura il livello della proteina PSA (antigene specifico della prostata) che viene prodotta solo dalla ghiandola prostatica. Sebbene livelli di PSA più elevati siano indicativi di cancro, il test è notoriamente inaffidabile. Infatti, la probabilità che un uomo non affetto da cancro abbia un livello di PSA elevato è approssimativamente .135, con questa probabilità che aumenta a circa .268 se l'uomo ha effettivamente il cancro. Se, sulla base di altri fattori, un medico è certo al 70 percento che un uomo abbia il cancro alla prostata, qual è la probabilità condizionata che egli abbia il cancro dato che

(a) il test indica un livello di PSA elevato;

(b) il test non indica un livello di PSA elevato?

Ripetete la precedente operazione, questa volta assumendo che il medico creda inizialmente che ci sia una probabilità del 30 percento che l'uomo abbia il cancro alla prostata.

35. Supponiamo che una compagnia assicurativa classifichi le persone in una di tre classi — rischi buoni, rischi medi e rischi cattivi. I loro registri indicano che le probabilità che persone a rischio buono, medio e cattivo siano coinvolte in un incidente in un arco di 1 anno sono, rispettivamente, .05, .15 e .30. Se il 20 percento della popolazione sono "rischi buoni", il 50 percento sono "rischi medi" e il 30 percento sono "rischi cattivi", quale proporzione di persone ha incidenti in un anno fisso? Se il titolare della polizza A non ha avuto incidenti nel 1987, qual è la probabilità che egli o ella sia un rischio buono (medio)?

36. Viene lanciata una coppia di dadi equi. Sia E l'evento che la somma dei dadi è uguale a 7.

(a) Mostrare che E è indipendente dall'evento che il primo dado si fermi su 4. (b) Mostrare che E è indipendente dall'evento che il secondo dado si fermi su 3.

37. La probabilità di chiusura del i-esimo relè nei circuiti mostrati è data da $\mathbf { \Delta } _ { p { i } } , { i } = 1 , 2 , 3 , 4 , 5$. Se tutti i relè funzionano indipendentemente, qual è la probabilità che una corrente fluisca tra A e B per i rispettivi circuiti?

38. Un sistema ingegneristico composto da n componenti si dice essere un sistema k-out-of-n $\left( k \ \leq \ n \right)$ se il sistema funziona se e solo se almeno k dei n componenti funzionano. Supponiamo che tutti i componenti funzionino indipendentemente l'uno dall'altro.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/3864db524bc1917b99c227ebcff0d2bcfef7fd35ea63ab05b11358da2d24e045.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/0460829353ef97530aecaba3063925e34255d28429312fa031e03725079edfdd.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/9cb1eb4034665234f86b6ecd0c2a1c5a15698db5eb563adb83bd18c84dc727ef.jpg)



(c)


(a) Se il i-esimo componente funziona con probabilità $P _ { i } , i = 1 , 2 , 3 , 4 ,$, calcolare la probabilità che un sistema 2-out-of-4 funzioni.

(b) Ripetere (a) per un sistema 3-out-of-5.

39. Vengono effettuate cinque lanci indipendenti di una moneta equa. Trovare la probabilità che

(a) i primi tre lanci siano uguali;

(b) o i primi tre lanci siano uguali, o gli ultimi tre lanci siano uguali;

(c) ci siano almeno due teste tra i primi tre lanci e almeno due code tra gli ultimi tre lanci.

40. Supponiamo che vengano eseguiti n tentativi indipendenti, ciascuno dei quali produce uno degli esiti 0, 1 o 2, con probabilità rispettive .3, .5 e .2. Trovare la probabilità che sia l'esito 1 che l'esito 2 si verifichino almeno una volta. (Suggerimento: Considerare la probabilità complementare.)

41. Un sistema in parallelo funziona ogni volta che almeno uno dei suoi componenti funziona. Considera un sistema in parallelo di $n$ componenti, e supponi che ogni componente funzioni indipendentemente con probabilità $\sup{1}$. Trova la probabilità condizionata che il componente 1 funzioni, dato che il sistema è funzionante.

42. Un certo organismo possiede una coppia di ciascuno dei 5 diversi geni (che chiameremo con le prime 5 lettere dell'alfabeto inglese). Ogni gene appare in 2 forme (che chiameremo con lettere minuscole e maiuscole). La lettera maiuscola sarà considerata il gene dominante nel senso che se un organismo possiede la coppia di geni xX, allora avrà esternamente l'aspetto del gene X. Ad esempio, se X sta per occhi marroni e x per occhi blu, allora un individuo che possiede la coppia di geni XX o xX avrà gli occhi marroni, mentre uno che possiede la coppia di geni xx avrà gli occhi blu. L'aspetto caratteristico di un organismo è chiamato suo fenotipo, mentre la sua costituzione genetica è chiamata genotipo. (Così 2 organismi con i rispettivi genotipi aA, bB, cc, dD, ee e AA, BB, cc, DD, ee avrebbero genotipi diversi ma lo stesso fenotipo.) In un accoppiamento tra 2 organismi, ciascuno contribuisce, casualmente, con una delle sue coppie di geni di ogni tipo. I 5 contributi di un organismo (uno di ciascuno dei 5 tipi) sono assunti come indipendenti e sono anche indipendenti dai contributi del suo compagno. In un accoppiamento tra organismi aventi i genotipi aA, bB, $c C ,$ dD, eE, e aa, bB, cc, Dd, ee, qual è la probabilità che la progenie (1) fenotipicamente, (2) genotipicamente somigli

(a) al primo genitore;

(b) al secondo genitore;

(c) a uno dei due genitori;

(d) a nessuno dei due genitori?

43. Tre prigionieri vengono informati dal loro carceriere che uno di loro è stato scelto a caso per essere giustiziato, e gli altri due saranno liberati. Il prigioniero A chiede al carceriere di dirgli in privato quale dei suoi compagni di cella sarà liberato, sostenendo che non ci sarebbe alcun danno nel divulgare questa informazione perché sa già che almeno uno dei due sarà liberato. Il carceriere si rifiuta di rispondere a questa domanda, sottolineando che se A sapesse quale dei suoi compagni di cella dovesse essere liberato, allora la sua probabilità di essere giustiziato salirebbe da $\frac 1 3$ a $\frac { 1 } { 2 }$ perché sarebbe allora uno dei due prigionieri. Cosa ne pensi del ragionamento del carceriere?

44. Sebbene entrambi i miei genitori abbiano gli occhi marroni, io ho gli occhi blu. Qual è la probabilità che mia sorella abbia gli occhi blu?

45. Viene raccolta una serie di $k$ coupon, ciascuno dei quali è indipendentemente un coupon di tipo $j$ con probabilità $p_{\text{sub}j}$, $\textstyle \sum _ { j = 1 } ^ { n } p _ { j } = 1$. Trova la probabilità che la serie contenga un coupon di tipo $i$ o di tipo $j$.

Questa Pagina È Intenzionalmente Lasciata Vuota

# VARIABILI CASUALI E ESPETTATIVA

## 4.1 VARIABILI CASUALI

Quando viene eseguito un esperimento casuale, spesso non ci interessa ogni dettaglio del risultato sperimentale ma solo il valore di una certa quantità numerica determinata dal risultato. Ad esempio, nel lancio di dadi siamo spesso interessati alla somma dei due dadi e non ci preoccupiamo realmente dei valori dei singoli dadi. Ovvero, potremmo essere interessati a sapere che la somma è 7 e non preoccuparci se il risultato effettivo sia stato (1, 6) o (2, 5) o (3, 4) o (4, 3) o (5, 2) o (6, 1). Inoltre, un ingegnere civile potrebbe non essere direttamente interessato alle quotidiane risalite e cali del livello dell'acqua di un bacino idrico (che possiamo considerare come il risultato sperimentale) ma potrebbe interessarsi solo al livello alla fine di una stagione piovosa. Queste quantità di interesse che sono determinate dal risultato dell'esperimento sono note come variabili casuali.

Poiché il valore di una variabile casuale è determinato dall'esito dell'esperimento, possiamo assegnare probabilità ai suoi possibili valori.

EXAMPLE 4.1a Ponendo $X$ per denotare la variabile casuale definita come la somma di due dadi equi, allora

$$
\begin{array}{r l} & P \{X = 2 \} = P \{(1, 1) \} = \frac {1}{3 6} \\ & P \{X = 3 \} = P \{(1, 2), (2, 1) \} = \frac {2}{3 6} \\ & P \{X = 4 \} = P \{(1, 3), (2, 2), (3, 1) \} = \frac {3}{3 6} \\ & P \{X = 5 \} = P \{(1, 4), (2, 3), (3, 2), (4, 1) \} = \frac {4}{3 6} \\ & P \{X = 6 \} = P \{(1, 5), (2, 4), (3, 3), (4, 2), (5, 1) \} = \frac {5}{3 6} \\ & P \{X = 7 \} = P \{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1) \} = \frac {6}{3 6} \end{array}\tag{4.1.1}
$$

$$
P \{X = 8 \} = P \{(2, 6), (3, 5), (4, 4), (5, 3), (6, 2) \} = \frac {5}{3 6}
$$

$$
P \{X = 9 \} = P \{(3, 6), (4, 5), (5, 4), (6, 3) \} = \frac {4}{3 6}
$$

$$
P \{X = 1 0 \} = P \{(4, 6), (5, 5), (6, 4) \} = \frac {3}{3 6}
$$

$$
P \{X = 1 1 \} = P \{(5, 6), (6, 5) \} = \frac {2}{3 6}
$$

$$
P \{X = 1 2 \} = P \{(6, 6) \} = \frac {1}{3 6}
$$

In altre parole, la variabile casuale $X$ può assumere qualsiasi valore intero tra 2 e 12 e la probabilità che assuma ciascun valore è data dall'Equazione 4.1.1. Poiché $X$ deve assumere un qualche valore, dobbiamo avere

$$
1 = P (S) = P \left(\bigcup_ {i = 2} ^ {1 2} \{X = i \}\right) = \sum_ {i = 2} ^ {1 2} P \{X = i \}
$$

che è facilmente verificabile dall'Equazione 4.1.1.

Un'altra variabile casuale di possibile interesse in questo esperimento è il valore del primo dado. Ponendo $Y$ per denotare questa variabile casuale, allora $Y$ ha la stessa probabilità di assumere uno qualsiasi dei valori da 1 a 6. Ovvero,

$$
P \{Y = i \} = 1 / 6, \qquad i = 1, 2, 3, 4, 5, 6
$$

EXAMPLE 4.1b Supponiamo che un individuo acquisti due componenti elettroniche, ciascuna delle quali può essere difettosa o accettabile. Inoltre, supponiamo che i quattro risultati possibili $- \ ( d , d ) , \ ( d , a ) , \ ( a , \ d ) , \ ( a , \ a )$ abbiano rispettive probabilità .09, .21, .21, .49 [dove (d, d) significa che entrambe le componenti sono difettose, (d, a) che la prima componente è difettosa e la seconda accettabile, e così via]. Se poniamo $X$ per denotare il numero di componenti accettabili ottenute nell'acquisto, allora $X$ è una variabile casuale che assume uno dei valori 0, 1, 2 con rispettive probabilità

$$
\begin{array}{l} {P \{X = 0 \} = . 0 9} \\ {P \{X = 1 \} = . 4 2} \\ {P \{X = 2 \} = . 4 9} \end{array}
$$

Se fossimo principalmente interessati a sapere se c'era almeno una componente accettabile, potremmo definire la variabile casuale $I$ da

$$
I = \left\{ \begin{array}{l l} 1 & \text { if } X = 1 \text { or } 2 \\ 0 & \text { if } X = 0 \end{array} \right.
$$

Se $A$ denota l'evento che venga ottenuta almeno una componente accettabile, allora la variabile casuale $I$ è chiamata variabile casuale indicatrice per l'evento $A$, poiché $I$ sarà uguale

## 4.1 Variabili Casuali

o 0 a seconda che A si verifichi. Le probabilità associate ai possibili valori di I sono

$$
\begin{array}{l} P \{I = 1 \} = . 9 1 \\ P \{I = 0 \} = . 0 9 \end{array}
$$

Nei due esempi precedenti, le variabili casuali di interesse assumevano un numero finito di possibili valori. Le variabili casuali il cui insieme di possibili valori può essere scritto come una sequenza finita $x _ { 1 } , \ldots , x _ { n } ,$ , o come una sequenza infinita $x _ { 1 } , . . .$ . sono dette discrete. Ad esempio, una variabile casuale il cui insieme di possibili valori è l'insieme degli interi non negativi è una variabile casuale discreta. Tuttavia, esistono anche variabili casuali che assumono un continuum di possibili valori. Queste sono note come variabili casuali continue. Un esempio è la variabile casuale che denota la durata della vita di un'auto, quando si assume che la durata della vita dell'auto possa assumere qualsiasi valore in qualche intervallo $( a , b )$ 

La funzione di distribuzione cumulata, o più semplicemente la funzione di distribuzione, F della variabile casuale X è definita per ogni numero reale x da

$$
F (x) = P \{X \leq x \}
$$

Ciò significa che $F ( x )$ è la probabilità che la variabile casuale X assuma un valore minore o uguale a x. 

Notazione: Useremo la notazione $X \sim F$ per indicare che F è la funzione di distribuzione di X . 

Tutte le domande di probabilità su X possono essere risposte in termini della sua funzione di distribuzione F . Ad esempio, supponiamo di voler calcolare $P \{ a < X \leq b \}$ }. Questo può essere ottenuto notando innanzitutto che l'evento $\{ X \leq b \}$ può essere espresso come l'unione dei due eventi mutuamente esclusivi $\{ X \leq a \}$ e $\{ a < X \leq b \}$ . Pertanto, applicando l'Assioma 3, otteniamo che

$$
P \{X \leq b \} = P \{X \leq a \} + P \{a <   X \leq b \}
$$

o 

$$
P \{a <   X \leq b \} = F (b) - F (a)
$$

EXAMPLE 4.1c Supponiamo che la variabile casuale X abbia la funzione di distribuzione 

$$
F (x) = \left\{ \begin{array}{l l} 0 & x \leq 0 \\ 1 - \exp \{- x ^ {2} \} & x > 0 \end{array} \right.
$$

Qual è la probabilità che X superi 1? 

SOLUTION La probabilità desiderata è calcolata come segue: 

$$
\begin{array}{r l} P \{X > 1 \} & = 1 - P \{X \leq 1 \} \\ & = 1 - F (1) \\ & = e ^ {- 1} \\ & = . 3 6 8 \quad \blacksquare \end{array}
$$

## 4.2 TIPOLOGIE DI VARIABILI CASUALI

Come menzionato in precedenza, una variabile casuale il cui insieme di possibili valori è una sequenza è detta discreta. Per una variabile casuale discreta X , definiamo la funzione di massa di probabilità $p ( a )$ di X da 

$$
p (a) = P \{X = a \}
$$

La funzione di massa di probabilità $p ( a )$ è positiva per al massimo un numero numerabile di valori di ${ \dot { \mathbf { \theta } } } _ { a . }$ Ciò significa che, se X deve assumere uno dei valori $x _ { 1 } , x _ { 2 } , \dotsc , x _ { 2 } ,$ , allora 

$$
\begin{array}{l l} p (x _ {i}) > 0, & \quad i = 1, 2, \ldots \\ p (x) = 0, & \quad \text { all   other   values   of } x \end{array}
$$

Poiché X deve assumere uno dei valori $x _ { i }$ , abbiamo 

$$
\sum_ {i = 1} ^ {\infty} p (x _ {i}) = 1
$$

EXAMPLE 4.2a Consideriamo una variabile casuale X che è uguale a 1, 2 o 3. Se sappiamo che 

$$
p (1) = \frac {1}{2} \qquad \mathrm{and} \qquad p (2) = \frac {1}{3}
$$

allora ne consegue (poiché $\begin{array} { r } { p ( 1 ) + p ( 2 ) + p ( 3 ) = 1 ) } \end{array}$ che 

$$
p (3) = \frac {1}{6}
$$

Un grafico di ${ p ( x ) }$ è presentato nella Figura 4.1. ■ 

La funzione di distribuzione cumulata F può essere espressa in termini di $\dot { p } ( \boldsymbol { x } )$ da 

$$
F (a) = \sum_ {\text { all } x \leq a} p (x)
$$

Se X è una variabile casuale discreta il cui insieme di possibili valori sono $x _ { 1 } , x _ { 2 } , x _ { 3 } , . . . ,$ dove $x _ { 1 } < x _ { 2 } < x _ { 3 } < \cdots$ , allora la sua funzione di distribuzione F è una funzione a gradini. Ciò significa che il valore di F è costante negli intervalli $[ x _ { i - 1 } , x _ { i } )$ e poi assume un gradino (o salto) di dimensione $ { p } ^ { (  { \boldsymbol { { x } } } _ { i } ) }$ ) in x<sub>i</sub> .

## 4.2 Tipi di Variabili Casuali

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/dd3884710344ac26139dcf40aaea00dccdce06a3e22608fc27a7ded098d6b49a.jpg)



FIGURA 4.1 Grafico di ( p)x, Esempio 4.2a.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/81535f5e479030e3402cf932872c032b9c2270aa9eac9202ba92b8c79b31a491.jpg)



FIGURA 4.2 Grafico di F (x).


Per esempio, supponiamo che X abbia una funzione di massa di probabilità data (come nell'Esempio 4.2a) da

$$
p (1) = \frac {1}{2}, \qquad p (2) = \frac {1}{3}, \qquad p (3) = \frac {1}{6}
$$

allora la funzione di distribuzione cumulata F di X è data da

$$
F (a) = \left\{ \begin{array}{l l} 0 & a <   1 \\ \frac {1}{2} & 1 \leq a <   2 \\ \frac {5}{6} & 2 \leq a <   3 \\ 1 & 3 \leq a \end{array} \right.
$$

Questo è presentato graficamente nella Figura 4.2.

Mentre l'insieme dei possibili valori di una variabile casuale discreta è una sequenza, spesso dobbiamo considerare variabili casuali il cui insieme di possibili valori è un intervallo. Sia X una tale variabile casuale. Diciamo che X è una variabile casuale continua se esiste una funzione non negativa $f ( x )$ , definita per tutti i reali $x \in ( - \infty , \infty )$ , avente la proprietà che per ogni insieme B di numeri reali

$$
P \{X \in B \} = \int_ {B} f (x) d x\tag{4.2.1}
$$

La funzione $f ( x )$ è chiamata funzione di densità di probabilità della variabile casuale X.

In parole, l'Equazione 4.2.1 afferma che la probabilità che X si trovi in B può essere ottenuta integrando la funzione di densità di probabilità sull'insieme B. Poiché X deve assumere qualche valore, $f ( x )$ deve soddisfare

$$
1 = P \{X \in (- \infty , \infty) \} = \int_ {- \infty} ^ {\infty} f (x) d x
$$

Tutte le affermazioni di probabilità su X possono essere risposte in termini di $f ( x )$. Per esempio, ponendo $\boldsymbol { B } = [ a , b ]$, otteniamo dall'Equazione 4.2.1 che

$$
P \{a \leq X \leq b \} = \int_ {a} ^ {b} f (x) d x\tag{4.2.2}
$$

Se poniamo $a = b$ in quanto sopra, allora

$$
P \{X = a \} = \int_ {a} ^ {a} f (x) d x = 0
$$

In parole, questa equazione afferma che la probabilità che una variabile casuale continua assuma un particolare valore è zero. (Vedi Figura 4.3.)

La relazione tra la distribuzione cumulata $F ( \cdot )$ e la densità di probabilità $f ( \cdot )$ è espressa da

$$
F (a) = P \{X \in (- \infty , a ] \} = \int_ {- \infty} ^ {a} f (x) d x
$$

Differenziando entrambi i lati si ottiene

$$
\frac {d}{d a} F (a) = f (a)
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/3330f23a1ea932505be76bbcec6ec6178b67c25e4ea227aa71daf3940c027c68.jpg)


$$
\text { FIGURE   4.3 } \quad \text { The   probability   density   function   } f (x) = \left\{ \begin{array}{l l} e ^ {- x} & x \geq 0 \\ 0 & x <   0 \end{array} \right..
$$

Ciò significa che la densità è la derivata della funzione di distribuzione cumulata. Un'interpretazione un po' più intuitiva della funzione di densità può essere ottenuta dall'Equazione 4.2.2 come segue:

$$
P \left\{a - \frac {\varepsilon}{2} \leq X \leq a + \frac {\varepsilon}{2} \right\} = \int_ {a - \varepsilon / 2} ^ {a + \varepsilon / 2} f (x) d x \approx \varepsilon f (a)
$$

quando ε è piccolo. In altre parole, la probabilità che X sia contenuto in un intervallo di lunghezza $\varepsilon$ attorno al punto a è approssimativamente $\varepsilon f ( a )$. Da questo, vediamo che $f ( a )$ è una misura di quanto sia probabile che la variabile casuale si trovi vicino ad a.

ESEMPIO 4.2b Supponiamo che $X$ sia una variabile casuale continua la cui funzione di densità di probabilità è data da

$$
f (x) = \left\{ \begin{array}{l l} C (4 x - 2 x ^ {2}) & 0 <   x <   2 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Qual è il valore di C?

(b) Trova $P \{ X > 1 \}$

SOLUZIONE (a) Poiché $f$ è una funzione di densità di probabilità, dobbiamo avere che $\textstyle \int _ { - \infty } ^ { \infty } f ( x ) d x = 1$, implicando che

$$
C \int_ {0} ^ {2} (4 x - 2 x ^ {2}) d x = 1
$$

o

$$
C \left[ 2 x ^ {2} - \frac {2 x ^ {3}}{3} \right] \Big | _ {x = 0} ^ {x = 2} = 1
$$

o

$$
C = \frac {3}{8}
$$

(b) Di conseguenza
$$
P \{X > 1 \} = \int_ {1} ^ {\infty} f (x) d x = \frac {3}{8} \int_ {1} ^ {2} (4 x - 2 x ^ {2}) d x = \frac {1}{2}
$$

## 4.3 VARIABILI CASUALI CONGIUNTAMENTE DISTRIBUITE

Per un dato esperimento, siamo spesso interessati non solo alle funzioni di distribuzione di probabilità delle singole variabili casuali, ma anche alle relazioni tra due o più variabili casuali. Ad esempio, in un esperimento sulle possibili cause del cancro, potremmo essere interessati alla relazione tra il numero medio di sigarette fumate quotidianamente e l'età in cui un individuo contrae il cancro. Allo stesso modo, un ingegnere potrebbe essere interessato alla relazione tra la resistenza al taglio e il diametro di una saldatura a punti in un campione di lamiera d'acciaio fabbricato.

Per specificare la relazione tra due variabili casuali, definiamo la funzione di distribuzione di probabilità cumulativa congiunta di X e Y come

$$
F (x, y) = P \{X \leq x, Y \leq y \}
$$

La conoscenza della funzione di distribuzione di probabilità congiunta consente, almeno in teoria, di calcolare la probabilità di qualsiasi affermazione riguardante i valori di X e Y. Ad esempio, la funzione di distribuzione di X — chiamiamola $F _ { X } -$ — può essere ottenuta dalla funzione di distribuzione congiunta F di X e Y come segue:

$$
\begin{array}{r l} & F _ {X} (x) = P \{X \leq x \} \\ & \quad = P \{X \leq x, Y <   \infty \} \\ & \quad = F (x, \infty) \end{array}
$$

Allo stesso modo, la funzione di distribuzione cumulativa di Y è data da

$$
F _ {Y} (y) = F (\infty , y)
$$

Nel caso in cui X e Y siano entrambi variabili casuali discrete i cui valori possibili siano, rispettivamente, $x _ { 1 } , x _ { 2 } , . . . ,$ e $y _ { 1 } , y _ { 2 } , . . . ,$ definiamo la funzione di massa di probabilità congiunta di X e $Y , p ( x _ { i } , y _ { j } )$, come

$$
p (x _ {i}, y _ {j}) = P \{X = x _ {i}, Y = y _ {j} \}
$$

Le singole funzioni di massa di probabilità di X e Y si ottengono facilmente dalla funzione di massa di probabilità congiunta attraverso il seguente ragionamento. Poiché Y deve assumere un valore $y_j$, ne consegue che l'evento $\{ X = x _ { i } \}$ può essere scritto come l'unione, su tutti i $j ,$ degli eventi mutuamente esclusivi $\{ X = x _ { i } , Y = y _ { j } \}$. Ovvero,

$$
\{X = x _ {i} \} = \bigcup_ {j} \{X = x _ {i}, Y = y _ {j} \}
$$

e quindi, utilizzando l'Assioma 3 della funzione di probabilità, vediamo che

$$
\begin{array}{c} P \{X = x _ {i} \} = P \left(\bigcup_ {j} \{X = x _ {i}, Y = y _ {j} \}\right) \\ = \sum_ {j} P \{X = x _ {i}, Y = y _ {j} \} \\ = \sum_ {j} p (x _ {i}, y _ {j}) \end{array}\tag{4.3.1}
$$

Allo stesso modo, possiamo ottenere $P \{ Y = y _ { j } \}$ sommando $/ ( x _ { i } , y _ { j } )$ su tutti i valori possibili di $x _ { i } ;$, cioè,

$$
\begin{array}{c} {P \{Y = y _ {j} \} =  \sum_ {i} P \{X = x _ {i}, Y = y _ {j} \}} \\ {=  \sum_ {i} p (x _ {i}, y _ {j})} \end{array}\tag{4.3.2}
$$

Pertanto, specificare la funzione di massa di probabilità congiunta determina sempre le singole funzioni di massa. Tuttavia, va notato che il contrario non è vero. In particolare, la conoscenza di $P \{ X = x _ { i } \}$ e $P \{ Y = y _ { j } \}$ non determina il valore di $P \{ X = x _ { i } , Y = y _ { j } \}$

ESEMPIO 4.3a Supponiamo che 3 batterie siano scelte casualmente da un gruppo di 3 nuove, 4 usate ma ancora funzionanti e 5 difettose. Se facciamo in modo che X e Y denotino, rispettivamente, il numero di batterie nuove e usate ma ancora funzionanti che vengono scelte, allora la funzione di massa di probabilità congiunta di X e $Y , _ { \mathcal { P } } ( i , j ) = \mathcal { P } \{ X = i , Y = j \}$ }, è data da

$$
\begin{array}{l} p (0, 0) = \binom {5} {3} \bigg / \binom {1 2} {3} = 1 0 / 2 2 0 \\ p (0, 1) = \binom {4} {1} \binom {5} {2} \bigg / \binom {1 2} {3} = 4 0 / 2 2 0 \\ p (0, 2) = \binom {4} {2} \binom {5} {1} \bigg / \binom {1 2} {3} = 3 0 / 2 2 0 \\ p (0, 3) = \binom {4} {3} \bigg / \binom {1 2} {3} = 4 / 2 2 0 \\ p (1, 0) = \binom {3} {1} \binom {5} {2} \bigg / \binom {1 2} {3} = 3 0 / 2 2 0 \\ p (1, 1) = \binom {3} {1} \binom {4} {1} \binom {5} {1} \bigg / \binom {1 2} {3} = 6 0 / 2 2 0 \\ p (1, 2) = \binom {3} {1} \binom {4} {2} \bigg / \binom {1 2} {3} = 1 8 / 2 2 0 \\ p (2, 0) = \binom {3} {2} \binom {5} {1} \bigg / \binom {1 2} {3} = 1 5 / 2 2 0 \\ p (2, 1) = \binom {3} {2} \binom {4} {1} \bigg / \binom {1 2} {3} = 1 2 / 2 2 0 \\ p (3, 0) = \binom {3} {3} \bigg / \binom {1 2} {3} = 1 / 2 2 0 \end{array}
$$

Queste probabilità possono essere espresse più facilmente in forma tabellare come mostrato nella Tabella 4.1.

<table><tr><td colspan="6">TABELLA 4.1 <eq>P\{X = i, Y = j\}</eq></td></tr><tr><td><eq>i</eq></td><td>0</td><td>1</td><td>2</td><td>3</td><td>Somma Riga= <eq>P\{X = i\}</eq></td></tr><tr><td>0</td><td><eq>\frac{10}{220}</eq></td><td><eq>\frac{40}{220}</eq></td><td><eq>\frac{30}{220}</eq></td><td><eq>\frac{4}{220}</eq></td><td><eq>\frac{84}{220}</eq></td></tr><tr><td>1</td><td><eq>\frac{30}{220}</eq></td><td><eq>\frac{60}{220}</eq></td><td><eq>\frac{18}{220}</eq></td><td>0</td><td><eq>\frac{108}{220}</eq></td></tr><tr><td>2</td><td><eq>\frac{15}{220}</eq></td><td><eq>\frac{12}{220}</eq></td><td>0</td><td>0</td><td><eq>\frac{27}{220}</eq></td></tr><tr><td>3</td><td><eq>\frac{1}{220}</eq></td><td>0</td><td>0</td><td>0</td><td><eq>\frac{1}{220}</eq></td></tr><tr><td>Somme Colonne = <eq>P\{Y = j\}</eq></td><td><eq>\frac{56}{220}</eq></td><td><eq>\frac{112}{220}</eq></td><td><eq>\frac{48}{220}</eq></td><td><eq>\frac{4}{220}</eq></td><td></td></tr></table>

Il lettore dovrebbe notare che la funzione di massa di probabilità di X è ottenuta calcolando le somme delle righe, in conformità con l'Equazione 4.3.1, mentre la funzione di massa di probabilità di Y è ottenuta calcolando le somme delle colonne, in conformità con l'Equazione 4.3.2. Poiché le singole funzioni di massa di probabilità di X e Y appaiono quindi nel margine di tale tabella, sono spesso definite come le funzioni di massa di probabilità marginali di X e Y, rispettivamente. Si deve notare che per verificare la correttezza di tale tabella potremmo sommare la riga marginale (o la colonna marginale) e verificare che la sua somma sia 1. (Perché la somma delle voci nella riga (o colonna) marginale deve essere uguale a 1?) ■ 


EXAMPLE 4.3b Supponiamo che il 15 percento delle famiglie in una determinata comunità non abbia figli, il 20 percento ne abbia 1, il 35 percento ne abbia 2 e il 30 percento ne abbia 3; supponiamo inoltre che ogni figlio abbia la stessa probabilità (e indipendentemente) di essere un maschio o una femmina. Se una famiglia viene scelta a caso da questa comunità, allora B, il numero di maschi, e G, il numero di femmine, in questa famiglia avranno la funzione di massa di probabilità congiunta mostrata nella Tabella 4.2.



TABELLA 4.2 P {B = i, G = j }


<table><tr><td>i\j</td><td>0</td><td>1</td><td>2</td><td>3</td><td>Somma Riga = P{B=i}</td></tr><tr><td>0</td><td>.15</td><td>.10</td><td>.0875</td><td>.0375</td><td>.3750</td></tr><tr><td>1</td><td>.10</td><td>.175</td><td>.1125</td><td>0</td><td>.3875</td></tr><tr><td>2</td><td>.0875</td><td>.1125</td><td>0</td><td>0</td><td>.2000</td></tr><tr><td>3</td><td>.0375</td><td>0</td><td>0</td><td>0</td><td>.0375</td></tr><tr><td>Colonna</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Somma =</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P{G=j}</td><td>.3750</td><td>.3875</td><td>.2000</td><td>.0375</td><td></td></tr></table>

Queste probabilità sono ottenute come segue: 

$$
\begin{array}{c} P \{B = 0, G = 0 \} = P \{\text {no children} \} \\ = . 1 5 \end{array}
$$

$$
\begin{array}{r l} P \{B = 0, G = 1 \} & = P \{1 \text {   girl   and   total   of   1   child } \} \\ & = P \{1 \text {   child } \} P \{1 \text {   girl   |   1   child } \} \\ & = (. 2 0) \left(\frac {1}{2}\right) = . 1 \end{array}
$$

$$
\begin{array}{r l} P \{B = 0, G = 2 \} & = P \{2 \text {   girls   and   total   of   } 2 \text {   children } \} \\ & = P \{2 \text {   children } \} P \{2 \text {   girls   } | 2 \text {   children } \} \\ & = (. 3 5) \left(\frac {1}{2}\right) ^ {2} = . 0 8 7 5 \end{array}
$$

$$
\begin{array}{r l} P \{B = 0, G = 3 \} & = P \{3 \text {   girls   and   total   of   } 3 \text {   children } \} \\ & = P \{3 \text {   children } \} P \{3 \text {   girls   } | 3 \text {   children } \} \\ & = (. 3 0) \left(\frac {1}{2}\right) ^ {3} = . 0 3 7 5 \end{array}
$$

Lasciamo al lettore il compito di verificare il resto della Tabella 4.2, che ci dice, tra le altre cose, che la famiglia scelta avrà almeno 1 femmina con probabilità .625. ■ 

Diciamo che X e $Y$ sono congiuntamente continue se esiste una funzione $f ( x , y )$ definita per tutti i reali x e $y ,$ avente la proprietà che per ogni insieme $C$ di coppie di numeri reali (ovvero, C è un insieme nel piano bidimensionale) 

$$
P \{(X, Y) \in C \} = \iint_ {(x, y) \in C} f (x, y) d x d y\tag{4.3.3}
$$

La funzione $f ( x , y )$ è chiamata funzione di densità di probabilità congiunta di X e Y. Se A e B sono qualsiasi insiemi di numeri reali, allora definendo $C = \{ ( x , y ) : x \in A , y \in B \}$, vediamo dall'Equazione 4.3.3 che 

$$
P \{X \in A, Y \in B \} = \int_ {B} \int_ {A} f (x, y) d x d y\tag{4.3.4}
$$

Poiché 

$$
\begin{array}{c} F (a, b) = P \{X \in (- \infty , a ], Y \in (- \infty , b ] \} \\ = \int_ {- \infty} ^ {b} \int_ {- \infty} ^ {a} f (x, y)   d x   d y \end{array}
$$

segue, dopo differenziazione, che 

$$
f (a, b) = \frac {\partial^ {2}}{\partial a \partial b} F (a, b)
$$

ovunque le derivate parziali siano definite. Un'altra interpretazione della funzione di densità congiunta è ottenuta dall'Equazione 4.3.4 come segue: 

$$
\begin{array}{c} P \{a <   X <   a + d a, b <   Y <   b + d b \} = \int_ {b} ^ {d + d b} \int_ {a} ^ {a + d a} f (x, y) d x d y \\ \approx f (a, b) d a d b \end{array}
$$

quando da e $d b$ sono piccoli e $f ( x , y )$ è continua in $a , b .$. Pertanto $f ( a , b )$ è una misura di quanto sia probabile che il vettore casuale $( X , Y )$ si trovi vicino a $( a , b )$ 

Se X e Y sono congiuntamente continue, esse sono individualmente continue, e le loro funzioni di densità di probabilità possono essere ottenute come segue: 

$$
\begin{array}{r l} & P \{X \in A \} = P \{X \in A, Y \in (- \infty , \infty) \} \\ & \qquad = \int_ {A} \int_ {- \infty} ^ {\infty} f (x, y) d y d x \\ & \qquad = \int_ {A} f _ {X} (x) d x \end{array}\tag{4.3.5}
$$

dove 

$$
f _ {X} (x) = \int_ {- \infty} ^ {\infty} f (x, y) d y
$$

è quindi la funzione di densità di probabilità di X. Allo stesso modo, la funzione di densità di probabilità di Y è data da 

$$
f _ {Y} (y) = \int_ {- \infty} ^ {\infty} f (x, y) d x\tag{4.3.6}
$$

EXAMPLE 4.3c La funzione di densità congiunta di X e Y è data da 

$$
f (x, y) = \left\{ \begin{array}{l l} 2 e ^ {- x} e ^ {- 2 y} & 0 <   x <   \infty , 0 <   y <   \infty \\ 0 & \text { otherwise } \end{array} \right.
$$

Calcola (a) $P \{ X > 1 , Y < 1 \}$ }; (b) $P \{ X < Y \}$ ; e (c) $P \{ X < a \}$ 

SOLUZIONE 

(a) 

$$
\begin{array}{l} P \{X > 1, Y <   1 \} = \int_ {0} ^ {1} \int_ {1} ^ {\infty} 2 e ^ {- x} e ^ {- 2 y} d x d y \\ \qquad = \int_ {0} ^ {1} 2 e ^ {- 2 y} (- e ^ {- x} | _ {1} ^ {\infty}) d y \\ \qquad = e ^ {- 1} \int_ {0} ^ {1} 2 e ^ {- 2 y} d y \\ \qquad = e ^ {- 1} (1 - e ^ {- 2}) \end{array}\tag{b}
$$

$$
\begin{array}{l} P \{X <   Y \} = \iint_ {(x, y): x <   y} 2 e ^ {- x} e ^ {- 2 y} d x d y \\ \qquad = \int_ {0} ^ {\infty} \int_ {0} ^ {y} 2 e ^ {- x} e ^ {- 2 y} d x d y \\ \qquad = \int_ {0} ^ {\infty} 2 e ^ {- 2 y} (1 - e ^ {- y}) d y \\ \qquad = \int_ {0} ^ {\infty} 2 e ^ {- 2 y} d y - \int_ {0} ^ {\infty} 2 e ^ {- 3 y} d y \\ \qquad = 1 - \frac {2}{3} \\ \qquad = \frac {1}{3} \end{array}
$$

(c) 

$$
\begin{array}{r l} P \{X <   a \} & = \int_ {0} ^ {a} \int_ {0} ^ {\infty} 2 e ^ {- 2 y} e ^ {- x} d y d x \\ & = \int_ {0} ^ {a} e ^ {- x} d x \\ & = 1 - e ^ {- a} \quad \blacksquare \end{array}
$$

## 4.3.1 Variabili Casuali Indipendenti

Le variabili casuali X e Y si dicono indipendenti se per ogni coppia di insiemi di numeri reali A e B

$$
P \{X \in A, Y \in B \} = P \{X \in A \} P \{Y \in B \}\tag{4.3.7}
$$

In altre parole, X e Y sono indipendenti se, per tutti A e B, gli eventi $E _ { A } = \{ X \in A \}$ e $F _ { B } = \{ Y \in B \}$ sono indipendenti. 

Si può dimostrare utilizzando i tre assiomi della probabilità che l'Equazione 4.3.7 seguirà se e solo se per tutti $a , b$

$$
P \{X \leq a, Y \leq b \} = P \{X \leq a \} P \{Y \leq b \}
$$

Pertanto, in termini della funzione di distribuzione congiunta F di X e ${ \cal Y } ,$, abbiamo che X e Y sono indipendenti se

$$
F (a, b) = F _ {X} (a) F _ {Y} (b) \qquad \mathrm{forall} a, b
$$

Quando X e Y sono variabili casuali discrete, la condizione di indipendenza dell'Equazione 4.3.7 è equivalente a

$$
p (x, y) = p _ {X} (x) p _ {Y} (y) \quad \text {   for   all   } x, y\tag{4.3.8}
$$

dove $\hbar X$ e $\hbar Y$ sono le funzioni di massa di probabilità di X e Y. L'equivalenza deriva dal fatto che, se l'Equazione 4.3.7 è soddisfatta, allora otteniamo l'Equazione 4.3.8 lasciando che A e B siano, rispettivamente, gli insiemi a un punto $A = \{ x \} , B = \{ y \}$. Inoltre, se l'Equazione 4.3.8 è valida, allora per ogni insieme A, B

$$
\begin{array}{r l} & P \{X \in A, Y \in B \} = \sum_ {y \in B} \sum_ {x \in A} p (x, y) \\ & \qquad = \sum_ {y \in B} \sum_ {x \in A} p _ {X} (x) p _ {Y} (y) \\ & \qquad = \sum_ {y \in B} p _ {Y} (y) \sum_ {x \in A} p _ {X} (x) \\ & \qquad = P \{Y \in B \} P \{X \in A \} \end{array}
$$

e quindi l'Equazione 4.3.7 è stabilita. 

Nel caso congiuntamente continuo, la condizione di indipendenza è equivalente a

$$
f (x, y) = f _ {X} (x) f _ {Y} (y) \quad \text {   for   all   } x, y
$$

In parole povere, X e Y sono indipendenti se la conoscenza del valore di una non cambia la distribuzione dell'altra. Le variabili casuali che non sono indipendenti si dicono dipendenti. 

EXAMPLE 4.3d Supponiamo che X e Y siano variabili casuali indipendenti aventi la comune funzione di densità

$$
f (x) = \left\{ \begin{array}{l l} e ^ {- x} & x > 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

Trovare la funzione di densità della variabile casuale $X / Y$

SOLUTION Iniziamo determinando la funzione di distribuzione di X /Y. Per $a > 0$

$$
\begin{array}{l} F _ {X / Y} (a) = P \{X / Y \leq a \} \\ = \iint_ {x / y \leq a} f (x, y) d x d y \\ = \iint_ {x / y \leq a} e ^ {- x} e ^ {- y} d x d y \\ = \int_ {0} ^ {\infty} \int_ {0} ^ {a y} e ^ {- x} e ^ {- y} d x d y \\ = \int_ {0} ^ {\infty} (1 - e ^ {- a y}) e ^ {- y} d y \\ = \left[ - e ^ {- y} + \frac {e ^ {- (a + 1) y}}{a + 1} \right] \Big | _ {0} ^ {\infty} \\ = 1 - \frac {1}{a + 1} \end{array}
$$

La derivazione fornisce che la funzione di densità di X /Y è data da

$$
f _ {X / Y} (a) = 1 / (a + 1) ^ {2}, \qquad 0 <   a <   \infty
$$

Possiamo anche definire distribuzioni di probabilità congiunte per n variabili casuali esattamente nello stesso modo in cui abbiamo fatto per $n = 2$. Ad esempio, la funzione di distribuzione di probabilità cumulativa congiunta $F ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$ delle n variabili casuali $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ è definita da

$$
F (a _ {1}, a _ {2}, \dots , a _ {n}) = P \{X _ {1} \leq a _ {1}, X _ {2} \leq a _ {2}, \dots , X _ {n} \leq a _ {n} \}
$$

Se queste variabili casuali sono discrete, definiamo la loro funzione di massa di probabilità congiunta $\ p ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ da

$$
p (x _ {1}, x _ {2}, \dots , x _ {n}) = P \{X _ {1} = x _ {1}, X _ {2} = x _ {2}, \dots , X _ {n} = x _ {n} \}
$$

Inoltre, le n variabili casuali si dicono congiuntamente continue se esiste una funzione $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$, chiamata funzione di densità di probabilità congiunta, tale che per ogni insieme C nello spazio n

$$
P \{(X _ {1}, X _ {2}, \dots , X _ {n}) \in C \} = \int \int_ {(x _ {1}, \dots , x _ {n}) \in C} \dots \int f (x _ {1}, \dots , x _ {n}) d x _ {1} d x _ {2} \dots d x _ {n}
$$

In particolare, per ogni n insiemi di numeri reali $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$

$$
\begin{array}{l} P \{X _ {1} \in A _ {1}, X _ {2} \in A _ {2}, \ldots , X _ {n} \in A _ {n} \} \\ = \int_ {A _ {n}} \int_ {A _ {n - 1}} \ldots \int_ {A _ {1}} f (x _ {1}, \ldots , x _ {n}) d x _ {1} d x _ {2} \ldots d x _ {n} \end{array}
$$

Il concetto di indipendenza può, naturalmente, essere definito anche per più di due variabili casuali. In generale, le n variabili casuali $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ si dicono indipendenti se, per tutti gli insiemi di numeri reali $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ 3

$$
P \{X _ {1} \in A _ {1}, X _ {2} \in A _ {2}, \ldots , X _ {n} \in A _ {n} \} = \prod_ {i = 1} ^ {n} P \{X _ {i} \in A _ {i} \}
$$

Come prima, si può dimostrare che questa condizione è equivalente a

$$
\begin{array}{l} P \{X _ {1} \leq a _ {1}, X _ {2} \leq a _ {2}, \dots , X _ {n} \leq a _ {n} \} \\ = \prod_ {i = 1} ^ {n} P \{X _ {1} \leq a _ {i} \} \quad \text { for   all } a _ {1}, a _ {2}, \dots , a _ {n} \end{array}
$$

Infine, diciamo che una collezione infinita di variabili casuali è indipendente se ogni sottocollezione finita di esse è indipendente. 

EXAMPLE 4.3e Supponiamo che le successive variazioni giornaliere del prezzo di un dato titolo siano assunte come variabili casuali indipendenti e identicamente distribuite con funzione di massa di probabilità data da

$$
P \{\text {daily change is} i \} = \left\{ \begin{array}{l l} - 3 & \text {with probability .05} \\ - 2 & \text {with probability .10} \\ - 1 & \text {with probability .20} \\ 0 & \text {with probability .30} \\ 1 & \text {with probability .20} \\ 2 & \text {with probability .10} \\ 3 & \text {with probability .05} \end{array} \right.
$$

Allora la probabilità che il prezzo del titolo aumenterà consecutivamente di 1, 2 e 0 punti nei prossimi tre giorni è

$$
P \{X _ {1} = 1, X _ {2} = 2, X _ {3} = 0 \} = (. 2 0) (. 1 0) (. 3 0) = . 0 0 6
$$

dove abbiamo lasciato che $X _ { i }$ denoti la variazione sul i-esimo giorno. ■

## *4.3.2 Distribuzioni Condizionali

La relazione tra due variabili casuali può spesso essere chiarita considerando la distribuzione condizionale di una data il valore dell'altra.

Ricordiamo che per due eventi $E$ e $F$, la probabilità condizionale di $E$ dato $F$ è definita, a condizione che $P ( F ) > 0$, da

$$
P (E | F) = \frac {P (E F)}{P (F)}
$$

Pertanto, se $X$ e $Y$ sono variabili casuali discrete, è naturale definire la funzione di massa di probabilità condizionale di $X$ dato che $Y = y ,$, da

$$
\begin{array}{c} p _ {X | Y} (x | y) = P \{X = x | Y = y \} \\ = \frac {P \{X = x , Y = y \}}{P \{Y = y \}} \\ = \frac {p (x , y)}{p _ {Y} (y)} \end{array}
$$

per tutti i valori di $y$ tali che $/ { Y } ( y ) > 0$ 

EXAMPLE 4.3f Se sappiamo, nell'Esempio 4.3b, che la famiglia scelta ha una bambina, calcola la funzione di massa di probabilità condizionale del numero di bambini nella famiglia. 

SOLUTION Notiamo prima dalla Tabella 4.2 che 

$$
P \{G = 1 \} = . 3 8 7 5
$$

Pertanto, 

$$
P \{B = 0 | G = 1 \} = \frac {P \{B = 0 , G = 1 \}}{P \{G = 1 \}} = \frac {. 1 0}{. 3 8 7 5} = 8 / 3 1
$$

$$
P \{B = 1 | G = 1 \} = \frac {P \{B = 1 , G = 1 \}}{P \{G = 1 \}} = \frac {. 1 7 5}{. 3 8 7 5} = 1 4 / 3 1
$$

$$
P \{B = 2 | G = 1 \} = \frac {P \{B = 2 , G = 1 \}}{P \{G = 1 \}} = \frac {. 1 1 2 5}{. 3 8 7 5} = 9 / 3 1
$$

$$
P \{B = 3 | G = 1 \} = \frac {P \{B = 3 , G = 1 \}}{P \{G = 1 \}} = 0
$$

Così, ad esempio, data 1 bambina, ci sono 23 possibilità su 31 che ci sarà anche almeno 1 bambino. ■ 

EXAMPLE 4.3g Supponiamo che $\phi ( x , y )$, la funzione di massa di probabilità congiunta di $X$ e ${ \cal Y } ,$, sia data da 

$$
p (0, 0) = . 4, \quad p (0, 1) = . 2, \quad p (1, 0) = . 1, \quad p (1, 1) = . 3.
$$

Calcola la funzione di massa di probabilità condizionale di $X$ dato che $Y = 1$ 

SOLUTION Notiamo prima che 

$$
P \{Y = 1 \} = \sum_ {x} p (x, 1) = p (0, 1) + p (1, 1) = . 5
$$

Pertanto, 

$$
P \{X = 0 | Y = 1 \} = \frac {p (0 , 1)}{P \{Y = 1 \}} = 2 / 5
$$

$$
P \{X = 1 | Y = 1 \} = \frac {p (1 , 1)}{P \{Y = 1 \}} = 3 / 5
$$

Se $X$ e $Y$ hanno una funzione di densità di probabilità congiunta $f ( x , y )$, allora la funzione di densità di probabilità condizionale di $X _ { i }$, dato che $Y = y$, è definita per tutti i valori di $y$ tali che $f _ { Y } ( y ) > 0$, da 

$$
f _ {X | Y} (x | y) = \frac {f (x , y)}{f _ {Y} (y)}
$$

Per motivare questa definizione, moltiplica il lato sinistro per $dx$ e il lato destro per $(dx $d y ) / d y$$ per ottenere 

$$
\begin{array}{c} f _ {X | Y} (x | y) d x = \frac {f (x , y) d x d y}{f _ {Y} (y) d y} \\ \approx \frac {P \{x \leq X \leq x + d x , y \leq Y \leq y + d y \}}{P \{y \leq Y \leq y + d y \}} \\ = P \{x \leq X \leq x + d y | y \leq Y \leq y + d y \} \end{array}
$$

In altre parole, per piccoli valori di $dx$ e $d y , f _ { X | Y } ( x | y )$ $dx$ rappresenta la probabilità condizionale che $X$ sia tra $x$ e $x + d x$, dato che $Y$ è tra $y$ e $y + d y$ 

L'uso delle densità condizionali ci permette di definire le probabilità condizionali di eventi associati a una variabile casuale quando ci viene fornito il valore di una seconda variabile casuale. Ovvero, se $X$ e $Y$ sono congiuntamente continue, allora, per ogni insieme $A$, 

$$
P \{X \in A | Y = y \} = \int_ {A} f _ {X | Y} (x | y) d x
$$

EXAMPLE 4.3h La densità congiunta di $X$ e $Y$ è data da 

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {1 2}{5} x (2 - x - y) & 0 <   x <   1, 0 <   y <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Calcola la densità condizionale di $X$, dato che $Y = y ,$, dove $0 < y < 1$ 

SOLUTION Per $0 < x < 1 , 0 < y < 1$, abbiamo 

$$
\begin{array}{r l} f _ {X | Y} (x | y) & = \frac {f (x , y)}{f _ {Y} (y)} \\ & = \frac {f (x , y)}{\int_ {- \infty} ^ {\infty} f (x , y) d x} \\ & = \frac {x (2 - x - y)}{\int_ {0} ^ {1} x (2 - x - y) d x} \\ & = \frac {x (2 - x - y)}{\frac {2}{3} - y / 2} \\ & = \frac {6 x (2 - x - y)}{4 - 3 y} \end{array}
$$

## 4.4 ESPERANZA

Uno dei concetti più importanti nella teoria della probabilità è quello dell'esperanza di una variabile casuale. Se $X$ è una variabile casuale discreta che assume i possibili valori $x _ { 1 } , x _ { 2 } , . . . ,$ allora l'esperanza o valore atteso di $X$, denotato da $E [ X ]$, è definito da

$$
E [ X ] = \sum_ {i} x _ {i} P \{X = x _ {i} \}
$$

In parole, il valore atteso di $X$ è una media ponderata dei possibili valori che $X$ può assumere, con ogni valore pesato dalla probabilità che $X$ lo assuma. Ad esempio, se la funzione di massa di probabilità di $X$ è data da

$$
p (0) = \frac {1}{2} = p (1)
$$

allora

$$
E [ X ] = 0 \left(\frac {1}{2}\right) + 1 \left(\frac {1}{2}\right) = \frac {1}{2}
$$

è semplicemente la media ordinaria dei due possibili valori 0 e 1 che $X$ può assumere. D'altro canto, se

$$
p (0) = \frac {1}{3}, \quad p (1) = \frac {2}{3}
$$

allora

$$
E [ X ] = 0 \left(\frac {1}{3}\right) + 1 \left(\frac {2}{3}\right) = \frac {2}{3}
$$

è una media ponderata dei due possibili valori 0 e 1 dove il valore 1 ha un peso doppio rispetto al valore 0 poiché $\rho ( 1 ) = 2 \rho ( 0 )$

Un'altra motivazione della definizione di speranza è fornita dall'interpretazione di frequenza delle probabilità. Questa interpretazione assume che se viene eseguita una sequenza infinita di repliche indipendenti di un esperimento, allora per qualsiasi evento $E ,$, la proporzione di tempo in cui si verifica $E$ sarà $P ( E )$. Ora, consideriamo una variabile casuale $X$ che deve assumere uno dei valori $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ con le rispettive probabilità $E [ X ]$ ; e pensiamo a $X$ come alla rappresentazione delle nostre vincite in un singolo gioco di fortuna. Ovvero, con probabilità $ { p } ^ { (  { \boldsymbol { { x } } } _ { i } ) }$ vinceremo $x _ { i }$ unità $i = 1 , 2 , \dots , n$. Ora, per l'interpretazione di frequenza, ne consegue che se giochiamo continuamente a questo gioco, allora la proporzione di tempo in cui vinceremo $x _ { i }$ sarà $ { p } (  { \boldsymbol { { x } } } _ { i } )$. Poiché questo è vero per tutti i $i , i = 1 , 2 , \ldots , n ,$ ne consegue che le nostre vincite medie per gioco saranno

$$
\sum_ {i = 1} ^ {n} x _ {i} p (x _ {i}) = E [ X ]
$$

Per vedere questo argomento più chiaramente, supponiamo di giocare $N$ partite dove $N$ è molto grande. Allora in circa $N p ( x _ { i } )$ di queste partite vinceremo $x _ { i }$, e quindi le nostre vincite totali nelle $N$ partite saranno

$$
\sum_ {i = 1} ^ {n} x _ {i} N _ {p} (x _ {i})
$$

implicando che le nostre vincite medie per gioco sono

$$
\sum_ {i = 1} ^ {n} \frac {x _ {i} N _ {p} (x _ {i})}{N} = \sum_ {i = 1} ^ {n} x _ {i} p (x _ {i}) = E [ X ]
$$

ESEMPIO 4.4a Trovare $E [X ]$ dove $X$ è il risultato quando lanciamo un dado equo.

SOLUZIONE Poiché $\begin{array} { r } { p ( 1 ) = p ( 2 ) = p ( 3 ) = p ( 4 ) = p ( 5 ) = p ( 6 ) = \frac { 1 } { 6 } } \end{array}$, otteniamo che

$$
E [ X ] = 1 \left(\frac {1}{6}\right) + 2 \left(\frac {1}{6}\right) + 3 \left(\frac {1}{6}\right) + 4 \left(\frac {1}{6}\right) + 5 \left(\frac {1}{6}\right) + 6 \left(\frac {1}{6}\right) = \frac {7}{2}
$$

Il lettore dovrebbe notare che, per questo esempio, il valore atteso di $X$ non è un valore che $X$ potrebbe eventualmente assumere. (Ovvero, il lancio di un dado non può portare a un risultato di 7/2.) Pertanto, sebbene chiamiamo $E [ X ]$ l'esperanza di $X _ { i }$, non dovrebbe essere interpretato come il valore che ci aspettiamo che $X$ abbia, bensì come il valore medio di $X$ in un gran numero di ripetizioni dell'esperimento. Ovvero, se lanciamo continuamente un dado equo, allora dopo un gran numero di lanci la media di tutti i risultati sarà approssimativamente 7/2. (Il lettore interessato dovrebbe provare questo come esperimento.) ■

ESEMPIO 4.4b Se $I$ è una variabile casuale indicatrice per l'evento $A$, cioè, se

$$
I = \left\{ \begin{array}{l l} 1 & \text { if   } A \text {   occurs } \\ 0 & \text { if   } A \text {   does   not   occur } \end{array} \right.
$$

allora

$$
E [ I ] = 1 P (A) + 0 P (A ^ {c}) = P (A)
$$

Pertanto, l'esperanza della variabile casuale indicatrice per l'evento $A$ è semplicemente la probabilità che si verifichi $A$. ■

ESEMPIO 4.4c Entropia Per una data variabile casuale $X$, quanta informazione è trasmessa nel messaggio che $X = x ?$ Iniziamo i nostri tentativi di quantificare questa affermazione concordando che la quantità di informazione nel messaggio che $X = x$ dovrebbe dipendere da quanto fosse probabile che $X$ fosse uguale a $x$. Inoltre, sembra ragionevole che più improbabile fosse che $X$ fosse uguale a $x$, più informativo sarebbe il messaggio. Ad esempio, se $X$ rappresenta la somma di due dadi equi, allora sembra esserci più informazione nel messaggio che $X$ è uguale a 12 rispetto a quanto ce ne sarebbe nel messaggio che $X$ è uguale a 7, poiché il primo evento ha probabilità $\frac { 1 } { 3 6 }$ e il secondo $\frac { 1 } { 6 }$

Denotiamo con $I ( \boldsymbol { p } )$ la quantità di informazione contenuta nel messaggio che un evento, la cui probabilità è ${ \boldsymbol { p } } ,$, si è verificato. Chiaramente $I ( \boldsymbol { p } )$ dovrebbe essere una funzione non negativa e decrescente di ${ \dot { \mathbf { \gamma } } } _ { \phi } .$. Per determinarne la forma, poniamo che X e Y siano variabili casuali indipendenti, e supponiamo che $P \{ X = x \} = p$ e $P \{ Y = y \} = q$. Quanta informazione è contenuta nel messaggio che X è uguale a x e Y è uguale a $y { \boldsymbol { ? } }$? Per rispondere a questo, si noti prima che la quantità di informazione nell'affermazione che X è uguale a x è $I ( \boldsymbol { p } )$. Inoltre, poiché la conoscenza del fatto che X è uguale a x non influisce sulla probabilità che Y sia uguale a $y$ (poiché $X$ e $Y$ sono indipendenti), sembra ragionevole che la quantità aggiuntiva di informazione contenuta nell'affermazione che $Y = y$ dovrebbe essere uguale a $I ( q )$. Pertanto, sembra che la quantità di informazione nel messaggio che X è uguale a x e Y è uguale a y sia $I ( p ) + I ( q )$. D'altra parte, tuttavia, abbiamo che

$$
P \{X = x, Y = y \} = P \{X = x \} P \{Y = y \} = p q
$$

il che implica che la quantità di informazione nel messaggio che X è uguale a x e Y è uguale a $y$ è $I ( \phi q )$. Di conseguenza, sembra che la funzione I debba soddisfare l'identità

$$
I (p q) = I (p) + I (q)
$$

Tuttavia, se definiamo la funzione G da

$$
G (p) = I (2 ^ {- p})
$$

allora vediamo dal sopra che

$$
\begin{array}{r l} & G (p + q) = I (2 ^ {- (p + q)}) \\ & \qquad = I (2 ^ {- p} 2 ^ {- q}) \\ & \qquad = I (2 ^ {- p}) + I (2 ^ {- q}) \\ & \qquad = G (p) + G (q) \end{array}
$$

Tuttavia, può essere dimostrato che le uniche funzioni (monotone) G che soddisfano la precedente relazione funzionale sono quelle della forma

$$
G (p) = c p
$$

per qualche costante c. Pertanto, dobbiamo avere che

$$
I (2 ^ {- p}) = c p
$$

o, ponendo $q = 2 ^ { - p }$

$$
I (q) = - c \log_ {2} (q)
$$

per qualche costante positiva c. È consuetudine porre $c = 1$ e dire che l'informazione è misurata in unità di bit (abbreviazione di binary digits).

Consideriamo ora una variabile casuale X, che deve assumere uno dei valori $x _ { 1 } , \ldots , x _ { n }$ con probabilità rispettive $\ p _ { 1 } , \ldots , \ p _ { n }$. Poiché $\log _ { 2 } ( \rho _ { i } )$ rappresenta l'informazione trasmessa dal messaggio che X è uguale a $x _ { i } ,$, ne consegue che la quantità di informazione attesa che sarà trasmessa quando il valore di X viene trasmesso è data da

$$
H (X) = - \sum_ {i = 1} ^ {n} p _ {i} \log_ {2} (p _ {i})
$$

La quantità $H ( X )$ è nota nella teoria dell'informazione come l'entropia della variabile casuale X. ■

Possiamo anche definire l'aspettativa di una variabile casuale continua. Supponiamo che X sia una variabile casuale continua con funzione di densità di probabilità f. Poiché, per dx piccolo

$$
f (x) d x \approx P \{x <   X <   x + d x \}
$$

ne consegue che una media ponderata di tutti i possibili valori di X, con il peso assegnato a x uguale alla probabilità che X sia vicino a x, è semplicemente l'integrale su tutti i $x \operatorname { o f } x f ( x )$ dx. Pertanto,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/8b4f0ec7a7dc15b9084049b7b275c0221662d3143c1a5d82048e6a77d18da8de.jpg)


## 4.5 Proprietà del Valore Atteso

è naturale definire il valore atteso di X da

$$
E [ X ] = \int_ {- \infty} ^ {\infty} x f (x) d x
$$

ESEMPIO 4.4d Supponiamo che vi aspettiate un messaggio in qualche momento dopo le 17:00. Dall'esperienza sapete che X, il numero di ore dopo le 17:00 fino all'arrivo del messaggio, è una variabile casuale con la seguente funzione di densità di probabilità:

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{1 . 5} & \text { if } 0 <   x <   1. 5 \\ 0 & \text { otherwise } \end{array} \right.
$$

La quantità di tempo attesa dopo le 17:00 fino all'arrivo del messaggio è data da

$$
E [ X ] = \int_ {0} ^ {1. 5} {\frac {x}{1 . 5}} d x = . 7 5
$$

Pertanto, in media, dovreste attendere tre quarti di ora. ■

## NOTE

(a) Il concetto di aspettativa è analogo al concetto fisico del centro di gravità di una distribuzione di massa. Consideriamo una variabile casuale discreta $X$ avente la funzione di massa di probabilità $P ( x _ { i } ) , i \geq 1$ . Se ora immaginiamo un'asta priva di peso in cui pesi con massa $P ( x _ { i } ) , i \geq 1$ sono situati nei punti $x _ { i } , i \geq 1$ (si veda la Figura 4.4), allora il punto in cui l'asta sarebbe in equilibrio è noto come centro di gravità. Per i lettori esperti di statica elementare, è ora una questione semplice dimostrare che questo punto si trova a $E [X ]$.* (b) $E [X ]$ ha le stesse unità di misura di $X$.

## 4.5 PROPRIETÀ DEL VALORE ATTESO

Supponiamo ora che ci sia data una variabile casuale $X$ e la sua distribuzione di probabilità (ovvero, la sua funzione di massa di probabilità nel caso discreto o la sua funzione di densità di probabilità nel caso continuo). Supponiamo inoltre che ci interessi calcolare non il valore atteso di $X$, ma il valore atteso di una funzione di $X ,$, diciamo $g ( X )$ . Come procediamo per farlo? Un modo è il seguente. Poiché $g ( X )$ ) è essa stessa una variabile casuale, deve avere una distribuzione di probabilità, che dovrebbe essere calcolabile dalla conoscenza della distribuzione di $X$. Una volta ottenuta la distribuzione di $g ( X )$ , possiamo quindi calcolare $E [ g ( X ) ]$ per la definizione di aspettativa.

EXAMPLE 4.5a Supponiamo che $X$ abbia la seguente funzione di massa di probabilità

$$
p (0) = . 2, \quad p (1) = . 5, \quad p (2) = . 3
$$

Calcolare $E [ X ^ { 2 } ]$

SOLUZIONE Ponendo $Y = X ^ { 2 }$ , abbiamo che $Y$ è una variabile casuale che può assumere uno dei valori $0 ^ { 2 } , 1 ^ { 2 } , \bar { 2 } ^ { 2 }$ con le rispettive probabilità

$$
\begin{array}{r} p _ {Y} (0) = P \{Y = 0 ^ {2} \} = . 2 \\ p _ {Y} (1) = P \{Y = 1 ^ {2} \} = . 5 \\ p _ {Y} (4) = P \{Y = 2 ^ {2} \} = . 3 \end{array}
$$

Pertanto,

$$
E [ X ^ {2} ] = E [ Y ] = 0 (. 2) + 1 (. 5) + 4 (. 3) = 1. 7
$$

EXAMPLE 4.5b Il tempo, in ore, necessario per individuare e riparare un guasto elettrico in una determinata fabbrica è una variabile casuale — chiamiamola $X$ — la cui funzione di densità è data da

$$
f _ {X} (x) = \left\{ \begin{array}{l l} 1 & \text { if } 0 <   x <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Se il costo coinvolto in un guasto di durata $x$ è $x ^ { 3 }$ , qual è il costo atteso di tale guasto?

SOLUZIONE Ponendo $Y = X ^ { 3 }$ per indicare il costo, calcoliamo prima la sua funzione di distribuzione come segue. Per $0 \leq a \leq 1$

$$
\begin{array}{r l} F _ {Y} (a) & = P \{Y \leq a \} \\ & = P \{X ^ {3} \leq a \} \\ & = P \{X \leq a ^ {1 / 3} \} \\ & = \int_ {0} ^ {a ^ {1 / 3}} d x \\ & = a ^ {1 / 3} \end{array}
$$

Differenziando $F _ { Y } ( a )$ , otteniamo la densità di $Y$ ,

$$
f _ {Y} (a) = \frac {1}{3} a ^ {- 2 / 3}, \quad 0 \leq a <   1
$$

Pertanto,

$$
\begin{array}{r l} E [ X ^ {3} ] & = E [ Y ] = \int_ {- \infty} ^ {\infty} a f _ {Y} (a) d a \\ & = \int_ {0} ^ {1} a \frac {1}{3} a ^ {- 2 / 3} d a \\ & = \frac {1}{3} \int_ {0} ^ {1} a ^ {1 / 3} d a \\ & = \frac {1}{3} \frac {3}{4} a ^ {4 / 3} | _ {0} ^ {1} \\ & = \frac {1}{4} \quad \blacksquare \end{array}
$$

Mentre la procedura precedente permetterà, in teoria, di calcolare sempre l'aspettativa di qualsiasi funzione di $X$ a partire dalla conoscenza della distribuzione di $X ,$ , esiste un modo più semplice per farlo. Supponiamo, ad esempio, che volessimo calcolare il valore atteso di $g ( X )$ . Poiché $g ( X )$ assume il valore $g ( X )$ quando $X = x ,$ , sembra intuitivo che $E [ g ( X ) ]$ debba essere una media ponderata dei possibili valori $g ( X )$ con, per un dato $x ,$ il peso assegnato a $g ( x )$ pari alla probabilità (o densità di probabilità nel caso continuo) che $X$ sia uguale a $x$. Infatti, può essere dimostrato che quanto sopra è vero e abbiamo quindi la seguente proposizione.

## PROPOSIZIONE 4.5.1 ASPETTATIVA DI UNA FUNZIONE DI UNA VARIABILE CASUALE

(a) Se $X$ è una variabile casuale discreta con funzione di massa di probabilità ${ p ( x ) }$ ), allora per ogni funzione a valori reali $g$ ,

$$
E [ g (X) ] = \sum_ {x} g (x) p (x)
$$

(b) Se $X$ è una variabile casuale continua con funzione di densità di probabilità $f ( x )$ , allora per ogni funzione a valori reali $g ,$ ,

$$
E [ g (X) ] = \int_ {- \infty} ^ {\infty} g (x) f (x) d x
$$

EXAMPLE 4.5c Applicando la Proposizione 4.5.1 all'Esempio 4.5a si ottiene

$$
E [ X ^ {2} ] = 0 ^ {2} (0. 2) + (1 ^ {2}) (0. 5) + (2 ^ {2}) (0. 3) = 1. 7
$$

che, naturalmente, concorda con il risultato derivato nell'Esempio 4.5a. ■

EXAMPLE 4.5d Applicando la proposizione all'Esempio 4.5b si ottiene

$$
\begin{array}{l} E [ X ^ {3} ] = \int_ {0} ^ {1} x ^ {3} d x \quad (\text { since } f (x) = 1, 0 <   x <   1) \\ = \frac {1}{4} \quad \blacksquare \end{array}
$$

Un corollario immediato della Proposizione 4.5.1 è il seguente.

## Corollario 4.5.2

Se a e b sono costanti, allora

$$
E [ a X + b ] = a E [ X ] + b
$$

Dimostrazione

Nel caso discreto,

$$
\begin{array}{r l} & E [ a X + b ] = \sum_ {x} (a x + b) p (x) \\ & \qquad = a \sum_ {x} x p (x) + b \sum_ {x} p (x) \\ & \qquad = a E [ X ] + b \end{array}
$$

Nel caso continuo,

$$
\begin{array}{r l} E [ a X + b ] & = \int_ {- \infty} ^ {\infty} (a x + b) f (x) d x \\ & = a \int_ {- \infty} ^ {\infty} x f (x) d x + b \int_ {- \infty} ^ {\infty} f (x) d x \\ & = a E [ X ] + b \quad \square \end{array}
$$

Se prendiamo $a = 0$ nel Corollario 4.5.2, vediamo che

$$
E [ b ] = b
$$

Ciò significa che il valore atteso di una costante è semplicemente il suo valore. (È intuitivo?) Inoltre, se prendiamo $b = 0$, otteniamo

$$
E [ a X ] = a E [ X ]
$$

o, in parole, il valore atteso di una costante moltiplicata per una variabile casuale è semplicemente la costante per il valore atteso della variabile casuale. Il valore atteso di una variabile casuale X, E [X], è anche definito come media o primo momento di X. La quantità $E [ X ^ { n } ] , n \geq 1$ è chiamata n-esimo momento di X. Per la Proposizione 4.5.1, notiamo che

$$
E [ X ^ {n} ] = \left\{ \begin{array}{l l} \sum_ {x} x ^ {n} p (x) & \text { if   } X \text {   is   discrete } \\ \int_ {- \infty} ^ {x} x ^ {n} f (x) d x & \text { if   } X \text {   is   continuous } \end{array} \right.
$$

## 4.5.1 Valore atteso di somme di variabili casuali

La versione bidimensionale della Proposizione 4.5.1 afferma che se $X$ e $Y$ sono variabili casuali e $g$ è una funzione di due variabili, allora

$$
\begin{array}{l l} E [ g (X, Y) ] = \sum_ {y} \sum_ {x} g (x, y) p (x, y) & \text { in   the   discrete   case } \\ = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} g (x, y) f (x, y) d x d y & \text { in   the   continuous   case } \end{array}
$$

Per esempio, ${ \mathrm { i f } } g ( X , Y ) = X + Y$ , quindi, nel caso continuo,

$$
\begin{array}{l} E [ X + Y ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} (x + y) f (x, y) d x d y \\ \qquad = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} x f (x, y) d x d y + \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} y f (x, y) d x d y \\ \qquad = E [ X ] + E [ Y ] \end{array}
$$

Un risultato simile può essere mostrato nel caso discreto e infatti, per qualsiasi variabile casuale $X$ e $Y _ { i }$ ,

$$
E [ X + Y ] = E [ X ] + E [ Y ]\tag{4.5.1}
$$

Applicando ripetutamente l'Equazione 4.5.1 possiamo mostrare che il valore atteso della somma di un numero qualsiasi di variabili casuali è uguale alla somma delle loro aspettative individuali.

Ad esempio,

$$
\begin{array}{r l} E [ X + Y + Z ] = E [ (X + Y) + Z ] & \\ = E [ X + Y ] + E [ Z ] & \text {by Equation 4.5.1} \\ = E [ X ] + E [ Y ] + E [ Z ] & \text {again by Equation 4.5.1} \end{array}
$$

E in generale, per ogni $n$,

$$
E [ X _ {1} + X _ {2} \dots + X _ {n} ] = E [ X _ {1} ] + E [ X _ {2} ] + \dots + E [ X _ {n} ]\tag{4.5.2}
$$

L'Equazione 4.5.2 è una formula estremamente utile la cui utilità sarà ora illustrata da una serie di esempi.

EXAMPLE 4.5e Una ditta di costruzioni ha recentemente inviato offerte per 3 lavori del valore (in profitti) 10, 20 e 40 (migliaia) di dollari. Se le sue probabilità di vincere i lavori sono rispettivamente .2, .8 e .3, qual è il profitto totale atteso della ditta?

SOLUTION Ponendo $X _ { i } , i = 1 , 2 , 3$ a denotare il profitto della ditta dal lavoro $i$, allora

$$
\mathrm{totalprofit} = X _ {1} + X _ {2} + X _ {3}
$$

e quindi

$$
E [ \mathrm{totalprofit} ] = E [ X _ {1} ] + E [ X _ {2} ] + E [ X _ {3} ]
$$

Ora

$$
\begin{array}{l} E [ X _ {1} ] = 1 0 (. 2) + 0 (. 8) = 2 \\ E [ X _ {2} ] = 2 0 (. 8) + 0 (. 2) = 1 6 \\ E [ X _ {3} ] = 4 0 (. 3) + 0 (. 7) = 1 2 \end{array}
$$

e quindi il profitto totale atteso della ditta è di 30 mila dollari. ■

EXAMPLE 4.5f Una segretaria ha digitato $N$ lettere insieme alle rispettive buste. Le buste si mescolano quando cadono sul pavimento. Se le lettere vengono inserite nelle buste mescolate in modo completamente casuale (ovvero, ogni lettera ha la stessa probabilità di finire in una qualsiasi delle buste), qual è il numero atteso di lettere che vengono inserite nelle buste corrette?

SOLUTION Ponendo $X$ a denotare il numero di lettere che vengono inserite nella busta corretta, possiamo calcolare più facilmente $E [X ]$ notando che

$$
X = X _ {1} + X _ {2} + \dots + X _ {N}
$$

dove

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   letter   is   placed   in   its   proper   envelope } \\ 0 & \text { otherwise } \end{array} \right.
$$

Ora, poiché la $i$-esima lettera ha la stessa probabilità di essere messa in una qualsiasi delle $N$ buste, ne consegue che

$$
P \{X _ {i} = 1 \} = P \{i t h l e t t e r i s i n i t s p r o p e r e n v e l o p e \} = 1 / N
$$

e quindi

$$
E [ X _ {i} ] = 1 P \{X _ {i} = 1 \} + 0 P \{X _ {i} = 0 \} = 1 / N
$$

Pertanto, dall'Equazione 4.5.2 otteniamo che

$$
E [ X ] = E \left[ X _ {1} \right] + \dots + E \left[ X _ {N} \right] = \left(\frac {1}{N}\right) N = 1
$$

Di conseguenza, indipendentemente dal numero di lettere, in media, esattamente una delle lettere sarà nella propria busta. ■

EXAMPLE 4.5g Supponiamo che ci siano 20 diversi tipi di coupon e supponiamo che ogni volta che si ottiene un coupon sia ugualmente probabile che sia di uno qualsiasi dei tipi. Calcola il numero atteso di diversi tipi contenuti in un set di 10 coupon.

SOLUTION Poniamo $X$ a denotare il numero di diversi tipi nel set di 10 coupon. Calcoliamo $E [X ]$ utilizzando la rappresentazione

$$
X = X _ {1} + \dots + X _ {2 0}
$$

dove

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   at   least   one   type } i \text { coupon   is   contained   in   the   set   of } 1 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

Ora

$$
\begin{array}{r l} E [ X _ {i} ] & = P \{X _ {i} = 1 \} \\ & = P \{\text { at   least   one   type } i \text { coupon   is   in   the   set   of } 1 0 \} \\ & = 1 - P \{\text { no   type } i \text { coupons   are   contained   in   the   set   of } 1 0 \} \\ & = 1 - \left(\frac {1 9}{2 0}\right) ^ {1 0} \end{array}
$$

quando l'ultima uguaglianza segue poiché ciascuno dei 10 coupon non sarà (indipendentemente) di tipo $i$ con probabilità $\frac { 1 9 } { 2 0 }$ . Pertanto,

$$
E [ X ] = E \left[ X _ {1} \right] + \dots + E \left[ X _ {2 0} \right] = 2 0 \left[ 1 - \left(\frac {1 9}{2 0}\right) ^ {1 0} \right] = 8. 0 2 5
$$

Una proprietà importante della media sorge quando si deve predire il valore di una variabile casuale. Ovvero, supponiamo che debba essere predetto il valore di una variabile casuale $X$. Se prediciamo che $X$ sarà uguale a $^ { c , }$ allora il quadrato dell'"errore" coinvolto sarà $( X - c ) ^ { 2 }$ Mostreremo ora che l'errore quadratico medio è minimizzato quando prediciamo che $X$ sarà uguale alla sua media $\mu .$ . Per vederlo, nota che per qualsiasi costante $c$

$$
\begin{array}{r l} & E [ (X - c) ^ {2} ] = E [ (X - \mu + \mu - c) ^ {2} ] \\ & \qquad = E [ (X - \mu) ^ {2} + 2 (\mu - c) (X - \mu) + (\mu - c) ^ {2} ] \\ & \qquad = E [ (X - \mu) ^ {2} ] + 2 (\mu - c) E [ X - \mu ] + (\mu - c) ^ {2} \\ & \qquad = E [ (X - \mu) ^ {2} ] + (\mu - c ^ {2}) \quad \text {since} \quad E [ X - \mu ] = E [ X ] - \mu = 0 \\ & \qquad \geq E [ (X - \mu) ^ {2} ] \end{array}
$$

Pertanto, il miglior predittore di una variabile casuale, in termini di minimizzazione del suo errore quadratico medio, è semplicemente la sua media.

## 4.6 VARIANZA

Data una variabile casuale X insieme alla sua funzione di distribuzione di probabilità, sarebbe estremamente utile se fossimo in grado di riassumere le proprietà essenziali della funzione di massa tramite certe misure opportunamente definite. Una di queste misure sarebbe $E [X ]$, il valore atteso di $X$. Tuttavia, mentre $E [X ]$ fornisce la media ponderata dei possibili valori di $X$, non ci dice nulla sulla variazione, o dispersione, di questi valori. Ad esempio, sebbene le seguenti variabili casuali $W, Y$ e $Z$ aventi funzioni di massa di probabilità determinate da

$$
W = 0 \quad \mathrm{withprobability1}
$$

$$
Y = \left\{ \begin{array}{c l} - 1 & \text {with probability} \frac {1}{2} \\ 1 & \text {with probability} \frac {1}{2} \end{array} \right.
$$

$$
Z = \left\{ \begin{array}{c l} - 1 0 0 & \text {with probability} \frac {1}{2} \\ 1 0 0 & \text {with probability} \frac {1}{2} \end{array} \right.
$$

abbiano tutte la stessa aspettativa — ovvero, 0 — vi è una dispersione molto maggiore nei possibili valori di $Y$ rispetto a quelli di $W$ (che è una costante) e nei possibili valori di $Z$ rispetto a quelli di $Y$ .

Poiché ci aspettiamo che $X$ assuma valori intorno alla sua media $E [ X ]$, sembrerebbe che un modo ragionevole per misurare la possibile variazione di $X$ sarebbe osservare quanto distanti siano $X$ dalla sua media in media. Un possibile modo per misurare questo sarebbe considerare la quantità $E [ | X - \mu | ]$, dove $\mu = E [ X ]$ e $[ X - \mu ]$ rappresenta il valore assoluto di $X - \mu$. Tuttavia, si scopre che è matematicamente scomodo gestire questa quantità e quindi viene solitamente considerata una quantità più trattabile — ovvero, l'aspettativa del quadrato della differenza tra $X$ e la sua media. Abbiamo quindi la seguente definizione.

## Definizione

Se $X$ è una variabile casuale con media $\mu _ { ; }$, allora la varianza di $X ,$, denotata da $\mathrm { V a r } ( X )$, è definita da

$$
\operatorname{Var} (X) = E [ (X - \mu) ^ {2} ]
$$

Una formula alternativa per $\mathrm { V a r } ( X )$ può essere derivata come segue:

$$
{ \begin{array}{r l} & {\operatorname{Var} (X) = E [ (X - \mu) ^ {2} ]} \\ & {\qquad = E [ X ^ {2} - 2 \mu X + \mu^ {2} ]} \\ & {\qquad = E [ X ^ {2} ] - E [ 2 \mu X ] + E [ \mu^ {2} ]} \\ & {\qquad = E [ X ^ {2} ] - 2 \mu E [ X ] + \mu^ {2}} \\ & {\qquad = E [ X ^ {2} ] - \mu^ {2}} \end{array} }
$$

ovvero,

$$
\operatorname{Var} (X) = E [ X ^ {2} ] - (E [ X ]) ^ {2}\tag{4.6.1}
$$

o, in parole, la varianza di $X$ è uguale al valore atteso del quadrato di $X$ meno il quadrato del valore atteso di $X$. Questo è, in pratica, spesso il modo più semplice per calcolare $\mathrm { V a r } ( X )$

ESEMPIO 4.6a Calcola $\mathrm { V a r } ( X )$ quando $X$ rappresenta l'esito quando lanciamo un dado equo.

SOLUZIONE Poiché $\begin{array} { r } { P \{ X = i \} = \frac { 1 } { 6 } , i = 1 , 2 , 3 , 4 , 5 , 6 , } \end{array}$, otteniamo

$$
\begin{array}{r l} E [ X ^ {2} ] & = \sum_ {i - 1} ^ {6} i ^ {2} P \{X = i \} \\ & = 1 ^ {2} \left(\frac {1}{6}\right) + 2 ^ {2} \left(\frac {1}{6}\right) + 3 ^ {2} \left(\frac {1}{6}\right) + 4 ^ {2} \left(\frac {1}{6}\right) + 5 ^ {2} \left(\frac {1}{6}\right) + 6 ^ {2} \left(\frac {1}{6}\right) \\ & = \frac {9 1}{6} \end{array}
$$

Pertanto, poiché è stato mostrato nell'Esempio 4.4a che $\begin{array} { r } { E [ X ] = \frac { 7 } { 2 } } \end{array}$, otteniamo dall'Equazione 4.6.1 che

$$
\begin{array}{r l} \operatorname{Var} (X) & = E [ X ^ {2} ] - (E [ X ]) ^ {2} \\ & = \frac {9 1}{6} - \left(\frac {7}{2}\right) ^ {2} = \frac {3 5}{1 2} \end{array}
$$

ESEMPIO 4.6b Varianza di una Variabile Casuale Indicatrice. Se, per qualche evento $A$,

$$
I = \left\{ \begin{array}{l l} 1 & \text { if   event   A   occurs } \\ 0 & \text { if   event   A   does   not   occur } \end{array} \right.
$$

allora

$$
\begin{array}{r l} \operatorname{Var} (I) & = E [ I ^ {2} ] - (E [ I ]) ^ {2} \\ & = E [ I ] - (E [ I ]) ^ {2} \quad \text { since } I ^ {2} = I (\text { as } 1 ^ {2} = 1 \text { and } 0 ^ {2} = 0) \\ & = E [ I ] (1 - E [ I ]) \\ & = P (A) [ 1 - P (A) ] \quad \text { since } E [ I ] = P (A) \text { from   Example   4.4b } \end{array}
$$

Un'identità utile riguardante le varianze è che per qualsiasi costanti $a$ e $b ,$

$$
\operatorname{Var} (a X + b) = a ^ {2} \operatorname{Var} (X)\tag{4.6.2}
$$

Per dimostrare l'Equazione 4.6.2, poniamo $\mu = E [ X ]$ e ricordiamo che $E [ a X + b ] = a \mu + b .$. Quindi, per la definizione di varianza, abbiamo

$$
\begin{array}{r l} & {\mathrm{Var} (a X + b) = E [ (a X + b - E [ a X + b ]) ^ {2} ]} \\ & {\qquad = E [ (a X + b - a \mu - b) ^ {2} ]} \\ & {\qquad = E [ (a X - a \mu) ^ {2} ]} \\ & {\qquad = E [ a ^ {2} (X - \mu) ^ {2} ]} \\ & {\qquad = a ^ {2} E [ (X - \mu) ^ {2} ]} \\ & {\qquad = a ^ {a} \mathrm{Var} (X)} \end{array}
$$

Specificando valori particolari per $a$ e $b$ nell'Equazione 4.6.2 si ottengono alcuni interessanti corollari. Ad esempio, impostando $a = 0$ nell'Equazione 4.6.2 otteniamo che

$$
\operatorname{Var} (b) = 0
$$

Ovvero, la varianza di una costante è 0. (È intuitivo?) Allo stesso modo, impostando $a = 1$ otteniamo

$$
\operatorname{Var} (X + b) = \operatorname{Var} (X)
$$

Ovvero, la varianza di una costante più una variabile casuale è uguale alla varianza della variabile casuale. (È intuitivo? Pensateci.) Infine, impostando $b = 0$ si ottiene

$$
\operatorname{Var} (a X) = a ^ {2} \operatorname{Var} (X)
$$

La quantità $\sqrt { \operatorname { V a r } ( X ) }$ è chiamata deviazione standard di $X$. La deviazione standard ha le stesse unità di misura della media.

## REMARCA

Analogamente alla media che è il centro di gravità di una distribuzione di massa, la varianza rappresenta, nella terminologia della meccanica, il momento d'inerzia.

## 4.7 COVARIANZA E VARIANZA DI SOMME DI VARIABILI CASUALI

Abbiamo mostrato nella Sezione 4.5 che l'aspettativa di una somma di variabili casuali è uguale alla somma delle loro aspettative. Il risultato corrispondente per le varianze, tuttavia, non è generalmente valido. Consideriamo

$$
\begin{array}{r l} \operatorname{Var} (X + X) & = \operatorname{Var} (2 X) \\ & = 2 ^ {2} \operatorname{Var} (X) \\ & = 4 \operatorname{Var} (X) \\ & \neq \operatorname{Var} (X) + \operatorname{Var} (X) \end{array}
$$

Esiste, tuttavia, un caso importante in cui la varianza di una somma di variabili casuali è uguale alla somma delle varianze; e questo accade quando le variabili casuali sono indipendenti. Prima di dimostrare ciò, tuttavia, definiamo il concetto di covarianza di due variabili casuali.

## Definizione

La covarianza di due variabili casuali X e Y, scritta Cov(X , Y ), è definita da

$$
\operatorname{Cov} (X, Y) = E [ (X - \mu_ {x}) (Y - \mu_ {y}) ]
$$

dove $\mu _ { x }$ e $\mu _ { y }$ sono le medie di X e Y, rispettivamente.

Un'espressione utile per $\operatorname { C o v } ( X , Y )$ può essere ottenuta espandendo il lato destro della definizione. Ciò produce

$$
\begin{array}{r} \operatorname{Cov} (X, Y) = E [ X Y - \mu_ {x} Y - \mu_ {y} X + \mu_ {x} \mu_ {y} ] \\ = E [ X Y ] - \mu_ {x} E [ Y ] - \mu_ {y} E [ X ] + \mu_ {x} \mu_ {y} \end{array}
$$

$$
\begin{array}{l} {= E [ X Y ] - \mu_ {x} \mu_ {y} - \mu_ {y} \mu_ {x} + \mu_ {x} \mu_ {y}} \\ {= E [ X Y ] - E [ X ] E [ Y ]} \end{array}\tag{4.7.1}
$$

Dalla sua definizione vediamo che la covarianza soddisfa le seguenti proprietà:

$$
\operatorname{Cov} (X, Y) = \operatorname{Cov} (Y, X)\tag{4.7.2}
$$

e

$$
\operatorname{Cov} (X, X) = \operatorname{Var} (X)\tag{4.7.3}
$$

Un'altra proprietà della covarianza, che deriva immediatamente dalla sua definizione, è che, per qualsiasi costante a,

$$
\operatorname{Cov} (a X, Y) = a \operatorname{Cov} (X, Y)\tag{4.7.4}
$$

La dimostrazione dell'Equazione 4.7.4 è lasciata come esercizio.

La covarianza, come l'aspettativa, possiede una proprietà additiva.

## Lemma 4.7.1

$$
\operatorname{Cov} (X + Z, Y) = \operatorname{Cov} (X, Y) + \operatorname{Cov} (Z, Y)
$$

Dimostrazione

$$
\begin{array}{r l} \operatorname{Cov} (X + Z, Y) & = E [ (X + Z) Y ] - E [ X + Z ] E [ Y ] \quad \text { from   Equation   4.7.1 } \\ & = E [ X Y ] + E [ Z Y ] - (E [ X ] + E [ Z ]) E [ Y ] \\ & = E [ X Y ] - E [ X ] E [ Y ] + E [ Z Y ] - E [ Z ] E [ Y ] \\ & = \operatorname{Cov} (X, Y) + \operatorname{Cov} (Z, Y) \quad \square \end{array}
$$

Il Lemma 4.7.1 può essere facilmente generalizzato (vedere Problema 48) per mostrare che

$$
\operatorname{Cov} \left(\sum_ {i = 1} ^ {n} X _ {i}, Y\right) = \sum_ {i = 1} ^ {n} \operatorname{Cov} (X _ {i}, Y)\tag{4.7.5}
$$

che dà origine al seguente.

PROPOSIZIONE 4.7.2

$$
\operatorname{Cov} \left(\sum_ {i = 1} ^ {n} X _ {i}, \sum_ {j = 1} ^ {m} Y _ {j}\right) = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \operatorname{Cov} (X _ {i}, Y _ {j})
$$

Dimostrazione

$$
\begin{array}{l} \text {   Proof   } \\ \operatorname{Cov} \left(\sum_ {i = 1} ^ {n} X _ {i}, \sum_ {j = 1} ^ {m} Y _ {j}\right) \\ = \sum_ {i = 1} ^ {n} \operatorname{Cov} \left(X _ {i}, \sum_ {j = 1} ^ {m} Y _ {j}\right) \quad \text { from   Equation   4.7.5 } \\ = \sum_ {i = 1} ^ {n} \operatorname{Cov} \left(\sum_ {j = 1} ^ {m} Y _ {j}, X _ {i}\right) \quad \text { by   the   symmetry   property   Equation   4.7.2 } \\ = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \operatorname{Cov} (Y _ {j}, X _ {i}) \quad \text { again   from   Equation   4.7.5 } \end{array}
$$

e il risultato segue ora applicando nuovamente la proprietà dell'Equazione 4.7.2. 

L'uso dell'Equazione 4.7.3 dà origine alla seguente formula per la varianza di una somma di variabili casuali.

Corollario 4.7.3

$$
\operatorname{Var}\left(\sum_{i = 1}^{n}X_{i}\right) = \sum_{i = 1}^{n}\operatorname{Var}(X_{i}) + \sum_{i = 1}^{n}\sum_{\substack{j = 1\\ j\neq i}}^{n}\operatorname{Cov}(X_{i},X_{j})
$$

## Dimostrazione

La dimostrazione segue direttamente dalla Proposizione 4.7.2 impostando $m = n ,$ , e $Y _ { j } = X _ { j }$ per $j = 1 , \dotsc , n .$ 

Nel caso di n = 2, il Corollario 4.7.3 fornisce che

$$
\operatorname{Var} (X + Y) = \operatorname{Var} (X) + \operatorname{Var} (Y) + \operatorname{Cov} (X, Y) + \operatorname{Cov} (Y, X)
$$

o, usando l'Equazione 4.7.2,

$$
\operatorname{Var} (X + Y) = \operatorname{Var} (X) + \operatorname{Var} (Y) + 2 \operatorname{Cov} (X, Y)\tag{4.7.6}
$$

## Teorema 4.7.4

Se X e Y sono variabili casuali indipendenti, allora

$$
\operatorname{Cov} (X, Y) = 0
$$

e quindi per $X _ { 1 } , \dots , X _ { n } $ indipendenti

$$
\operatorname{Var} \left(\sum_ {i = 1} ^ {n} X _ {i}\right) = \sum_ {i = 1} ^ {n} \operatorname{Var} (X _ {i})
$$

## Dimostrazione

Dobbiamo dimostrare che $E [ X Y ] = E [ X ] E [ Y ]$. Ora, nel caso discreto,

$$
\begin{array}{l} E [ X Y ] = \sum_ {j} \sum_ {i} x _ {i} y _ {j} P \{X = x _ {i}, Y = y _ {j} \} \\ \qquad = \sum_ {j} \sum_ {i} x _ {i} y _ {j} P \{X = x _ {i} \} P \{Y = y _ {j} \} \quad \text { by   independence } \\ \qquad = \sum_ {y} y _ {j} P \{Y = y _ {j} \} \sum_ {i} x _ {i} P \{X = x _ {i} \} \\ \qquad = E [ Y ] E [ X ] \end{array}
$$

Poiché un argomento simile vale in tutti gli altri casi, il risultato è dimostrato. 

ESEMPIO 4.7a Calcolare la varianza della somma ottenuta quando vengono effettuati 10 lanci indipendenti di un dado equo.

SOLUZIONE Ponendo $X _ { i }$ come l'esito del i-esimo lancio, abbiamo che

$$
\begin{array}{r l} \operatorname{Var} \left(\sum_ {1} ^ {1 0} X _ {i}\right) & = \sum_ {1} ^ {1 0} \operatorname{Var} (X _ {i}) \\ & = 1 0 \frac {3 5}{1 2} \quad \text { from   Example   4.6a } \\ & = \frac {1 7 5}{6} \quad \blacksquare \end{array}
$$

ESEMPIO 4.7b Calcolare la varianza del numero di teste risultanti da 10 lanci indipendenti di una moneta equa.

SOLUZIONE Ponendo

$$
I _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   the   } j \text { th   toss   lands   heads } \\ 0 & \text { if   the   } j \text { th   toss   lands   tails } \end{array} \right.
$$

allora il numero totale di teste è uguale a

$$
\sum_ {j = 1} ^ {1 0} I _ {j}
$$

Pertanto, dal Teorema 4.7.4,

$$
\operatorname{Var} \left(\sum_ {j = 1} ^ {1 0} I _ {j}\right) = \sum_ {j = 1} ^ {1 0} \operatorname{Var} (I _ {j})
$$

Ora, poiché $I _ { j }$ è una variabile casuale indicatrice per un evento avente probabilità $\frac { 1 } { 2 }$, segue dall'Esempio 4.6b che

$$
\operatorname{Var} (I _ {j}) = \frac {1}{2} \left(1 - \frac {1}{2}\right) = \frac {1}{4}
$$

e quindi

$$
\operatorname{Var} \left(\sum_ {j = 1} ^ {1 0} I _ {j}\right) = \frac {1 0}{4} \quad \blacksquare
$$

La covarianza di due variabili casuali è importante come indicatore della relazione tra esse. Ad esempio, consideriamo la situazione in cui X e Y sono variabili indicatrici per il verificarsi o meno degli eventi A e B. Ovvero, per gli eventi A e B, definiamo

$$
X = \left\{ \begin{array}{l l} 1 & \text { if   } A \text {   occurs } \\ 0 & \text { otherwise } \end{array} \right., \qquad Y = \left\{ \begin{array}{l l} 1 & \text { if   } B \text {   occurs } \\ 0 & \text { otherwise } \end{array} \right.
$$

e notiamo che

$$
X Y = \left\{ \begin{array}{l l} 1 & \text { if } X = 1, Y = 1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Pertanto,

$$
\begin{array}{r l} & {\operatorname{Cov} (X, Y) = E [ X Y ] - E [ X ] E [ Y ]} \\ & {\qquad = P \{X = 1, Y = 1 \} - P \{X = 1 \} P \{Y = 1 \}} \end{array}
$$

Da questo vediamo che

$$
\operatorname{Cov} (X, Y) > 0 \Leftrightarrow P \{X = 1, Y = 1 \} > P \{X = 1 \} P \{Y = 1 \}
$$

$$
\begin{array}{l} \Leftrightarrow \frac {P \{X = 1 , Y = 1 \}}{P \{X = 1 \}} > P \{Y = 1 \} \\ \Leftrightarrow P \{Y = 1 | X = 1 \} > P \{Y = 1 \} \end{array}
$$

Ovvero, la covarianza di X e Y è positiva se l'esito $X = 1$ rende più probabile che $Y = 1$ (il che, come si vede facilmente per simmetria, implica anche il contrario).

In generale, si può dimostrare che un valore positivo di $\operatorname { C o v } ( X , Y )$ è un'indicazione che Y tende ad aumentare come fa X, mentre un valore negativo indica che Y tende a diminuire all'aumentare di X. L'intensità della relazione tra X e Y è indicata dalla correlazione tra X e Y, una quantità adimensionale ottenuta dividendo la covarianza per il prodotto delle deviazioni standard di X e Y. Ovvero,

$$
\operatorname{Corr} (X, Y) = \frac {\operatorname{Cov} (X , Y)}{\sqrt {\operatorname{Var} (X) \operatorname{Var} (Y)}}
$$

Si può dimostrare (vedere Problema 49) che questa quantità ha sempre un valore compreso tra −1 e +1.

## 4.8 FUNZIONI GENERATRICI DEI MOMENTI

La funzione generatrice dei momenti $\phi ( t )$ della variabile casuale X è definita per tutti i valori t da

$$
\phi (t) = E [ e ^ {t X} ] = \left\{ \begin{array}{l l} \sum_ {x} e ^ {t x} p (x) & \text { if   } X \text {   is   discrete } \\ \int_ {- \infty} ^ {\infty} e ^ {t x} f (x)   d x & \text { if   } X \text {   is   continuous } \end{array} \right.
$$

Chiamiamo $\phi ( t )$ la funzione generatrice dei momenti perché tutti i momenti di X possono essere ottenuti differenziando successivamente $\phi ( t )$. Per esempio,

$$
\begin{array}{r} \phi^ {\prime} (t) = \frac {d}{d t} E [ e ^ {t X} ] \\ = E \left[ \frac {d}{d t} (e ^ {t X}) \right] \\ = E [ X e ^ {t X} ] \end{array}
$$

Pertanto,

$$
\phi^ {\prime} (0) = E [ X ]
$$

Analogamente,

$$
\begin{array}{r} \phi^ {\prime \prime} (t) = \frac {d}{d t} \phi^ {\prime} (t) \\ = \frac {d}{d t} E [ X e ^ {t X} ] \end{array}
$$

$$
= E \left[ \frac {d}{d t} (X e ^ {t X}) \right]
$$

$$
= E [ X ^ {2} e ^ {t X} ]
$$

e quindi

$$
\phi^ {\prime \prime} (0) = E [ X ^ {2} ]
$$

In generale, la n-esima derivata di $\phi ( t )$ valutata in $t = 0$ è uguale a $E [ X ^ { n } ]$; ovvero,

$$
\phi^ {n} (0) = E [ X ^ {n} ], \quad n \geq 1
$$

Una proprietà importante delle funzioni generatrici dei momenti è che la funzione generatrice dei momenti della somma di variabili casuali indipendenti è semplicemente il prodotto delle singole funzioni generatrici dei momenti. Per vederlo, supponiamo che X e Y siano indipendenti e abbiano rispettivamente funzioni generatrici dei momenti $\phi _ { X } ( t )$ e $\phi _ { Y } ( t )$. Allora $\phi _ { X + Y } ( t )$, la funzione generatrice dei momenti di $X + Y$, è data da

$$
\begin{array}{r l} & {\phi_ {X + Y} (t) = E [ e ^ {t (X + Y)} ]} \\ & {\qquad = E [ e ^ {t X} e ^ {t Y} ]} \\ & {\qquad = E [ e ^ {t X} ] E [ e ^ {t Y} ]} \\ & {\qquad = \phi_ {X} (t) \phi_ {Y} (t)} \end{array}
$$

dove l'uguaglianza penultima segue dal Teorema 4.7.4 poiché X e ${ \cal Y } ,$, e quindi $e ^ { t X }$ e $e ^ { t Y }$, sono indipendenti.

Un altro risultato importante è che la funzione generatrice dei momenti determina univocamente la distribuzione. Ovvero, esiste una corrispondenza uno-a-uno tra la funzione generatrice dei momenti e la funzione di distribuzione di una variabile casuale.

## 4.9 DISUGUAGLIANZA DI CHEBYSHEV E LA LEGGE DEGLI GRANDI NUMERI DEBOLE

Iniziamo questa sezione dimostrando un risultato noto come disuguaglianza di Markov.

## PROPOSIZIONE 4.9.1 DISUGUAGLIANZA DI MARKOV

Se X è una variabile casuale che assume solo valori non negativi, allora per ogni valore $a > 0$

$$
P \{X \geq a \} \leq \frac {E [ X ]}{a}
$$

## Dimostrazione

Forniamo una dimostrazione per il caso in cui X è continua con densità f.

$$
\begin{array}{l} E [ X ] = \int_ {0} ^ {\infty} x f (x) d x \\ \qquad = \int_ {0} ^ {a} x f (x) d x + \int_ {a} ^ {\infty} x f (x) d x \\ \qquad \geq \int_ {a} ^ {\infty} x f (x) d x \\ \qquad \geq \int_ {a} ^ {\infty} a f (x) d x \\ \qquad = a \int_ {a} ^ {\infty} f (x) d x \\ \qquad = a P \{X \geq a \} \end{array}
$$

e il risultato è dimostrato. 

Come corollario, otteniamo la Proposizione 4.9.2.

## PROPOSIZIONE 4.9.2 DISUGUAGLIANZA DI CHEBYSHEV

Se X è una variabile casuale con media $\mu$ e varianza $\sigma ^ { 2 }$, allora per ogni valore $k > 0$

$$
P \{| X - \mu | \geq k \} \leq \frac {\sigma^ {2}}{k ^ {2}}
$$

## Dimostrazione

Poiché $( X - \mu ) ^ { 2 }$ è una variabile casuale non negativa, possiamo applicare la disuguaglianza di Markov (con $a = k ^ { 2 } )$) per ottenere

$$
P \{(X - \mu) ^ {2} \geq k ^ {2} \} \leq \frac {E [ (X - \mu) ^ {2} ]}{k ^ {2}}\tag{4.9.1}
$$

Ma poiché $( X - \mu ) \geq k ^ { 2 }$ se e solo se $\mathrm { i f } \left| X - \mu \right| \geq k$, l'Equazione 4.9.1 è equivalente a

$$
P \{| X - \mu | \geq k \} \leq \frac {E [ (X - \mu) ^ {2} ]}{k ^ {2}} = \frac {\sigma^ {2}}{k ^ {2}}
$$

e la dimostrazione è completa. 

L'importanza delle disuguaglianze di Markov e di Chebyshev è che ci permettono di derivare dei limiti sulle probabilità quando sono note solo la media, o sia la media che la varianza, della distribuzione di probabilità. Naturalmente, se la distribuzione effettiva fosse nota, allora le probabilità desiderate potrebbero essere calcolate esattamente e non avremmo bisogno di ricorrere a dei limiti.

ESEMPIO 4.9a Supponiamo che sia noto che il numero di articoli prodotti in una fabbrica durante una settimana è una variabile casuale con media 50.

(a) Cosa si può dire sulla probabilità che la produzione di questa settimana superi 75?

(b) Se la varianza della produzione di una settimana è nota e uguale a 25, allora cosa si può dire sulla probabilità che la produzione di questa settimana sia compresa tra 40 e 60?

SOLUZIONE Sia X il numero di articoli che saranno prodotti in una settimana:

(a) Per la disuguaglianza di Markov

$$
P \{X > 7 5 \} \leq \frac {E [ X ]}{7 5} = \frac {5 0}{7 5} = \frac {2}{3}
$$

(b) Per la disuguaglianza di Chebyshev

$$
P \{| X - 5 0 | \geq 1 0 \} \leq \frac {\sigma^ {2}}{1 0 ^ {2}} = \frac {1}{4}
$$

Pertanto

$$
P \{| X - 5 0 | <   1 0 \} \geq 1 - \frac {1}{4} = \frac {3}{4}
$$

e così la probabilità che la produzione di questa settimana sia compresa tra 40 e 60 è almeno .75. ■

Sostituendo k con kσ nell'Equazione 4.9.1, possiamo scrivere la disuguaglianza di Chebyshev come

$$
P \{| X - \mu | > k \sigma \} \leq 1 / k ^ {2}
$$

Pertanto essa afferma che la probabilità che una variabile casuale differisca dalla sua media di più di k deviazioni standard è limitata da $1 / k ^ { 2 }$

Concluderemo questa sezione utilizzando la disuguaglianza di Chebyshev per dimostrare la legge debole dei grandi numeri, la quale afferma che la probabilità che la media dei primi n termini in una sequenza di variabili casuali indipendenti e identicamente distribuite differisca dalla sua media di più di ε tende a 0 quando n tende all'infinito.

## Teorema 4.9.3 La Legge Debole dei Grandi Numeri

Sia $X _ { 1 } , X _ { 2 } , \ldots$ , una sequenza di variabili casuali indipendenti e identicamente distribuite, ciascuna con media $E [ X _ { i } ] = \mu$. Allora, per ogni $\varepsilon > 0$ ,

$$
P \left\{\left| \frac {X _ {1} + \cdots + X _ {n}}{n} - \mu \right| > \varepsilon \right\}\rightarrow 0 \quad \text { as } n \rightarrow \infty
$$

## Dimostrazione

Dimostreremo il risultato solo sotto l'assunzione aggiuntiva che le variabili casuali abbiano una varianza finita $\sigma ^ { 2 }$. Ora, poiché

$$
E \left[ \frac {X _ {1} + \cdots + X _ {n}}{n} \right] = \mu \quad \text { and } \quad \operatorname{Var} \left(\frac {X _ {1} + \cdots + X _ {n}}{n}\right) = \frac {\sigma^ {2}}{n}
$$

segue dalla disuguaglianza di Chebyshev che

$$
P \left\{\left| \frac {X _ {1} + \cdots + X _ {n}}{n} - \mu \right| > \epsilon \right\} \leq \frac {\sigma^ {2}}{n \epsilon^ {2}}
$$

e il risultato è dimostrato. 

Per un'applicazione della precedente, supponiamo che venga eseguita una sequenza di prove indipendenti. Sia E un evento fisso e denominiamo con $P ( E )$ la probabilità che E si verifichi in una data prova. Ponendo

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   } E \text {   occurs   on   trial   } i \\ 0 & \text { if   } E \text {   does   not   occur   on   trial   } i \end{array} \right.
$$

segue che $X _ { 1 } + X _ { 2 } + \cdots + X _ { n }$ rappresenta il numero di volte in cui E si verifica nelle prime n prove. Poiché $E [ X _ { i } ] = P ( E )$, segue quindi dalla legge debole dei grandi numeri che per ogni numero positivo ε, non importa quanto piccolo, la probabilità che la proporzione delle prime n prove in cui E si verifica differisca da $P ( E )$ di più di ε tende a 0 all'aumentare di n.

## Problemi

1. Cinque uomini e 5 donne sono classificati in base ai loro punteggi in un esame. Si assuma che nessun punteggio sia uguale e che tutte le 10! possibili classifiche siano ugualmente probabili. Sia X la posizione più alta ottenuta da una donna (ad esempio, $X = 2$ se la persona in prima posizione fosse un uomo e la successiva fosse una donna). Trova $\textstyle P \{ X = i \} , i = 1 , 2 , 3 , \dotsc , 8 , 9 , 1 0 .$ 

2. Sia X la differenza tra il numero di croci e il numero di teste ottenute quando una moneta viene lanciata n volte. Quali sono i possibili valori di X? 

3. Nel Problema 2, se si assume che la moneta sia equa, per $n = 3$, quali sono le probabilità associate ai valori che X può assumere? 

4. La funzione di distribuzione della variabile casuale X è data da

$$
F (x) = \left\{ \begin{array}{l l} 0 & x <   0 \\ \frac {x}{2} & 0 \leq x <   1 \\ \frac {2}{3} & 1 \leq x <   2 \\ \frac {1 1}{1 2} & 2 \leq x <   3 \\ 1 & 3 \leq x \end{array} \right.
$$

(a) Disegna questa funzione di distribuzione. 

(b) Qual è $\begin{array} { r } { P \{ X > \frac { 1 } { 2 } \} ; } \end{array}$ 

(c) Qual è $P \{ 2 < \bar { X } \leq 4 \} \ddagger$ 

(d) Qual è $P \{ X < 3 \} \colon$ 

(e) Qual è $P \{ X = 1 \} \colon$ 

5. Supponiamo che ti venga data la funzione di distribuzione F di una variabile casuale X. Spiega come potresti determinare $P \{ X = 1 \}$ }. (Suggerimento: Dovrai usare il concetto di limite.) 

6. La quantità di tempo, in ore, in cui un computer funziona prima di guastarsi è una variabile casuale continua con funzione di densità di probabilità data da

$$
f (x) = \left\{ \begin{array}{l l} \lambda e ^ {- x / 1 0 0} & x \geq 0 \\ 0 & x <   0 \end{array} \right.
$$

Qual è la probabilità che un computer funzioni tra 50 e 150 ore prima di guastarsi? Qual è la probabilità che funzioni per meno di 100 ore? 

7. La durata in ore di un certo tipo di valvola radio è una variabile casuale avente una funzione di densità di probabilità data da

$$
f (x) = \left\{ \begin{array}{l l} 0 & x \leq 1 0 0 \\ \frac {1 0 0}{x ^ {2}} & x > 1 0 0 \end{array} \right.
$$

Qual è la probabilità che esattamente 2 di 5 tali valvole in un set radio debbano essere sostituite entro le prime 150 ore di funzionamento? Si assuma che gli eventi $E _ { i } , i = 1 , 2 , 3 , 4 , 5$, ovvero che la i-esima valvola debba essere sostituita entro questo tempo, siano indipendenti. 

8. Se la funzione di densità di X è uguale a

$$
f (x) = \left\{ \begin{array}{l l} c e ^ {- 2 x} & 0 <   x <   \infty \\ 0 & x <   0 \end{array} \right.
$$

trova c. Qual è $P \{ X > 2 \} \colon$ 

9. Si sa che un contenitore di 5 transistor ne contiene 3 difettosi. I transistor devono essere testati, uno alla volta, fino a quando quelli difettosi non vengono identificati. Denota con $N _ { 1 }$ il numero di test effettuati fino a quando il primo difettoso viene individuato e con $N _ { 2 }$ il numero di test aggiuntivi fino a quando il secondo difettoso viene individuato; trova la funzione di massa di probabilità congiunta di $N _ { 1 }$ e $N _ { 2 }$ 

10. La funzione di densità di probabilità congiunta di X e Y è data da

$$
f (x, y) = \frac {6}{7} \left(x ^ {2} + \frac {x y}{2}\right), \quad 0 <   x <   1, \quad 0 <   y <   2
$$

(a) Verifica che questa sia effettivamente una funzione di densità congiunta. 

(b) Calcola la funzione di densità di X. 

(c) Trova $P \{ X > Y \}$ 

11. Siano $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ variabili casuali indipendenti, ciascuna avente una distribuzione uniforme su (0, 1). Sia M = massimo $( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } )$ . Mostra che la funzione di distribuzione di $M , F _ { M } ( \cdot )$, è data da

$$
F _ {M} (x) = x ^ {n}, \quad 0 \leq x \leq 1
$$

Qual è la funzione di densità di probabilità di M? 

12. La densità congiunta di X e Y è data da

$$
f (x, y) = \left\{ \begin{array}{l l} x e ^ {(- x + y)} & x > 0, y > 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Calcola la densità di X. 

(b) Calcola la densità di Y. 

(c) X e Y sono indipendenti? 

13. La densità congiunta di X e Y è

$$
f (x, y) = \left\{ \begin{array}{l l} 2 & 0 <   x <   y, 0 <   y <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Calcola la densità di X. 

(b) Calcola la densità di Y. 

(c) X e Y sono indipendenti? 

14. Se la funzione di densità congiunta di X e Y si scompone in una parte che dipende solo da x e una che dipende solo da y, mostra che X e Y sono indipendenti. Ovvero, se

$$
f (x, y) = k (x) l (y), \quad - \infty <   x <   \infty , \quad - \infty <   y <   \infty
$$

mostra che X e Y sono indipendenti. 

15. Il Problema 14 è coerente con i risultati dei Problemi 12 e 13? 

16. Supponiamo che X e Y siano variabili casuali continue indipendenti. Mostra che

$$
(\mathbf {a}) P \{X + Y \leq a \} = \int_ {- \infty} ^ {\infty} F _ {X} (a - y) f _ {Y} (y) d y
$$

(b) $P \{ X \leq Y \} = \int _ { - \infty } ^ { \infty } F _ { X } ( y ) f _ { Y } ( y ) d y$ 

dove $f _ { Y }$ è la funzione di densità di $Y ,$, e $F _ { X }$ è la funzione di distribuzione di $X .$ .

17. Quando una corrente I (misurata in ampere) scorre attraverso una resistenza R (misurata in ohm), la potenza generata (misurata in watt) è data da $W = I ^ { 2 } R$ . Supponiamo che I e R siano variabili casuali indipendenti con densità 

$$
\begin{array}{l} f _ {I} (x) = 6 x (1 - x) \quad 0 \leq x \leq 1 \\ f _ {R} (x) = 2 x \quad 0 \leq x \leq 1 \end{array}
$$

Determinare la funzione di densità di $W .$ . 

18. Nell'Esempio 4.3b, determinare la funzione di massa di probabilità condizionata della dimensione di una famiglia scelta casualmente contenente 2 bambine. 

19. Calcolare la funzione di densità condizionata di X dato $Y = y$ in (a) Problema 10 e (b) Problema 13. 

20. Mostrare che X e Y sono indipendenti se e solo se 

(a) ${ P _ { X / Y } } ^ { ( x / y ) } = p _ { X } ( x )$ nel caso discreto 

(b) $f _ { X / Y } { } ^ { ( x / y ) } = f _ { X } ( x )$ nel caso continuo 

21. Calcolare il valore atteso della variabile casuale nel Problema 1. 

22. Calcolare il valore atteso della variabile casuale nel Problema 3. 

23. Ogni notte diversi meteorologi ci forniscono la "probabilità" che pioverà il giorno successivo. Per giudicare quanto queste persone predicano bene, assegneremo a ciascuno di loro un punteggio come segue: se un meteorologo dice che pioverà con probabilità ${ \boldsymbol { p } } ,$ allora riceverà un punteggio di 

$$
\begin{array}{l l} 1 - (1 - p) ^ {2} & \text {if it does rain} \\ 1 - p ^ {2} & \text {if it does not rain} \end{array}
$$

Annoteremo quindi i punteggi in un determinato intervallo di tempo e concluderemo che il meteorologo con il punteggio medio più alto è il miglior predittore del meteo. Supponiamo ora che un dato meteorologo sia a conoscenza di ciò e voglia quindi massimizzare il proprio punteggio atteso. Se questo individuo crede davvero che pioverà domani con probabilità $\boldsymbol { p } ^ { * }$ , quale valore di p dovrebbe affermare per massimizzare il punteggio atteso? 

24. Una compagnia di assicurazioni stipula una polizza secondo la quale un importo di denaro A deve essere pagato se si verifica un evento E entro un anno. Se la compagnia stima che E si verificherà entro un anno con probabilità ${ \boldsymbol { p } } ,$ quanto dovrebbe addebitare al cliente affinché il suo profitto atteso sia del 10 percento di A? 

25. Un totale di 4 autobus che trasportano 148 studenti della stessa scuola arrivano a uno stadio di football. Gli autobus trasportano, rispettivamente, 40, 33, 25 e 50 studenti. Uno degli studenti viene selezionato casualmente. Sia X il numero di studenti che erano sull'autobus che trasportava lo studente selezionato casualmente. Uno dei 4 autisti viene anche selezionato casualmente. Sia Y il numero di studenti sul suo autobus. 

(a) Quale tra E [X ] o E [Y ] pensate sia maggiore? Perché? 

(b) Calcolare E[X ] e E[Y ]. 

26. Supponiamo che due squadre giochino una serie di partite che terminano quando una di esse ha vinto i giochi i. Supponiamo che ogni partita giocata sia, indipendentemente, vinta dalla squadra A con probabilità $\mathbf { \nabla } ^ { p . }$ Trovare il numero atteso di partite giocate quando $i = 2$ Mostrare inoltre che questo numero è massimizzato quando $\textstyle { p = { \frac { 1 } { 2 } } }$ 

27. La funzione di densità di X è data da 

$$
f (x) = \left\{ \begin{array}{l l} a + b x ^ {2} & 0 \leq x \leq 1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Se $\begin{array} { r } { E [ X ] = \frac { 3 } { 5 } } \end{array}$ , trovare $a , b .$ 

28. La durata della vita in ore delle lampade elettroniche è una variabile casuale avente una funzione di densità di probabilità data da 

$$
f (x) = a ^ {2} x e ^ {- a x}, \quad x \geq 0
$$

Calcolare la durata della vita attesa di tale lampada. 

29. Siano $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ variabili casuali indipendenti aventi la comune funzione di densità 

$$
f (x) = \left\{ \begin{array}{l l} 1 & 0 <   x <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Trovare (a) $E [ \operatorname { M a x } ( X _ { i } , \dots , X _ { n } ) ]$ e (b) $E [ \mathrm { M i n } ( X _ { 1 } , \dots , X _ { n } ) ]$ 

30. Supponiamo che X abbia la funzione di densità 

$$
f (x) = \left\{ \begin{array}{l l} 1 & 0 <   x <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Calcolare $E [ X ^ { n } ] \left( \mathbf { a } \right)$ calcolando la densità di $X _ { n }$ e usando poi la definizione di aspettativa e (b) usando la Proposizione 4.5.1. 

31. Il tempo necessario per riparare un computer personale è una variabile casuale la cui densità, in ore, è data da 

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{2} & 0 <   x <   2 \\ 0 & \text { otherwise } \end{array} \right.
$$

Il costo della riparazione dipende dal tempo impiegato ed è uguale a $4 0 + 3 0 { \sqrt { x } }$ quando il tempo è x. Calcolare il costo atteso per riparare un computer personale. 

32. Se $E [ X ] = 2$ e $E [ X ^ { 2 } ] = 8$ , calcolare (a) $E [ ( 2 + 4 X ) ^ { 2 } ) ]$ e (b) $E [ X ^ { 2 } + ( X + 1 ) ^ { 2 } ]$

33. Dieci palline vengono scelte casualmente da un'urna contenente 17 palline bianche e 23 palline nere. Sia X il numero di palline bianche scelte. Calcola $E [ X ]$

(a) definendo le appropriate variabili indicatrici $X _ { i } , i = 1 , \dotsc , 1 0$ in modo che

$$
X = \sum_ {i = 1} ^ {1 0} X _ {i}
$$

(b) definendo le appropriate variabili indicatrici $Y _ { i } , = 1 , \dots , 1 7$ in modo che

$$
X = \sum_ {i = 1} ^ {1 7} Y _ {i}
$$

34. Se X è una variabile casuale continua avente funzione di distribuzione $F _ { ; }$, allora la sua mediana è definita come il valore di m per cui

$$
F (m) = 1 / 2
$$

Trova la mediana delle variabili casuali con funzione di densità

(a) $f ( x ) = e ^ { - x } , \quad x \geq 0 ;$

(b) $f ( x ) = 1 , \quad 0 \leq x \leq 1 .$

35. La mediana, come la media, è importante nel predire il valore di una variabile casuale. Mentre nel testo è stato mostrato che la media di una variabile casuale è il miglior predittore dal punto di vista della minimizzazione del valore atteso del quadrato dell'errore, la mediana è il miglior predittore se si vuole minimizzare il valore atteso dell'errore assoluto. Ovvero, $E [ | X - c | ]$ è minimizzato quando $c$ è la mediana della funzione di distribuzione di X. Dimostra questo risultato quando X è continua con funzione di distribuzione $F$ e funzione di densità $f .$. (Suggerimento: Scrivi

$$
\begin{array}{r l} & E [ | X - c | ] = \int_ {- \infty} ^ {\infty} | x - c | f (x) d x \\ & \qquad = \int_ {- \infty} ^ {c} | x - c | f (x) d x + \int_ {c} ^ {\infty} | x - c | f (x) d x \\ & \qquad = \int_ {- \infty} ^ {c} (c - x) f (x) d x + \int_ {c} ^ {\infty} (x - c) f (x) d x \\ & \qquad = c F (c) - \int_ {- \infty} ^ {c} x f (x) d x + \int_ {c} ^ {\infty} x f (x) d x - c [ 1 - F (c) ] \end{array}
$$

Ora, usa il calcolo per trovare il valore minimizzante di $c . )$

36. Diciamo che $m _ { \phi }$ è il percentile 100p della funzione di distribuzione F se

$$
F (m _ {p}) = p
$$

Trova $m _ { \phi }$ per la distribuzione avente funzione di densità

$$
f (x) = 2 e ^ {- 2 x}, \quad x \geq 0
$$

37. Una comunità consiste in 100 coppie sposate. Se durante un dato anno 50 dei membri della comunità muoiono, qual è il numero atteso di matrimoni che rimangono intatti? Assumi che l'insieme delle persone che muoiono sia ugualmente probabile per qualsiasi dei $\left( { 2 0 0 } \atop 5 0 \right)$ gruppi di dimensione 50. (Suggerimento: Per i = 1, . . . , 100 poniamo

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   neither   member   of   couple } i \text { dies } \\ 0 & \text { otherwise } \end{array} \right.
$$

38. Calcola l'aspettativa e la varianza del numero di successi in n prove indipendenti, ciascuna delle quali produce un successo con probabilità $\scriptstyle { \boldsymbol { p } } .$. L'indipendenza è necessaria?

39. Supponiamo che X abbia la stessa probabilità di assumere uno qualsiasi dei valori 1, 2, 3, 4. Calcola (a) E [X ] e (b) Var(X ).

40. Sia $p _ { i } = P \{ X = i \}$ e supponiamo che $p _ { 1 } + p _ { 2 } + p _ { 3 } = 1$. Se $E [ X ] = 2$, quali valori di $\cdot _ { p 1 } , _ { \ l } p _ { 2 } , _ { \ l } p _ { 3 }$ (a) massimizzano e (b) minimizzano Var(X )?

41. Calcola la media e la varianza del numero di teste che appaiono in 3 lanci di una moneta equa.

42. Dimostra che per ogni variabile casuale X

$$
E [ X ^ {2} ] \geq (E [ X ]) ^ {2}
$$

Quando si ha l'uguaglianza?

43. Una variabile casuale X, che rappresenta il peso (in once) di un articolo, ha funzione di densità data da f (z),

$$
f (z) = \left\{ \begin{array}{l l} (z - 8) & \text { for } 8 \leq z \leq 9 \\ (1 0 - z) & \text { for } 9 <   z \leq 1 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Calcola la media e la varianza della variabile casuale X.

(b) Il produttore vende l'articolo a un prezzo fisso di $2.00. Garantisce il rimborso del denaro dell'acquisto a qualsiasi cliente che trovi il peso del suo articolo inferiore a 8.25 oz. Il suo costo di produzione è correlato al peso dell'articolo dalla relazione x/15 + .35. Trova il profitto atteso per articolo.

44. Supponiamo che la durezza Rockwell X e la perdita per abrasione Y di un campione (dati codificati) abbiano una densità congiunta data da

$$
f _ {X Y} (u, v) = \left\{ \begin{array}{l l} u + v & \text { for } 0 \leq u, v \leq 1 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Trova le densità marginali di X e $Y .$

(b) Trova E(X ) e $\mathrm { V a r } ( X )$

45. Un prodotto è classificato in base al numero di difetti che contiene e alla fabbrica che lo produce. Sia $X _ { 1 }$ e $X _ { 2 }$ le variabili casuali che rappresentano il numero di difetti per unità (assumendo i possibili valori 0, 1, 2 o 3) e il numero della fabbrica (assumendo i possibili valori 1 o 2), rispettivamente. Le voci nella tabella rappresentano la funzione di massa di probabilità congiunta di un prodotto scelto casualmente.

<table><tr><td><eq>X_1</eq></td><td><eq>X_2</eq></td><td>1</td><td>2</td></tr><tr><td>0</td><td></td><td><eq>\frac{1}{8}</eq></td><td><eq>\frac{1}{16}</eq></td></tr><tr><td>1</td><td></td><td><eq>\frac{1}{16}</eq></td><td><eq>\frac{1}{16}</eq></td></tr><tr><td>2</td><td></td><td><eq>\frac{3}{16}</eq></td><td><eq>\frac{1}{8}</eq></td></tr><tr><td>3</td><td></td><td><eq>\frac{1}{8}</eq></td><td><eq>\frac{1}{4}</eq></td></tr></table>

(a) Trova le distribuzioni di probabilità marginali di $X _ { 1 }$ e $X _ { 2 }$ . 

(b) Trova E [(X )], E [(X )], Var(X ), Var(X ) e $\mathrm { C o v } ( X _ { 1 } , X _ { 2 } )$ 

46. Una macchina produce un prodotto che viene sottoposto a screening (ispezione al 100 percento) prima di essere spedito. Lo strumento di misura è tale che è difficile leggere tra 1 e $1 { \frac { 1 } { 3 } }$ (dati codificati). Dopo che il processo di screening ha avuto luogo, la dimensione misurata ha densità 

$$
f (z) = \left\{ \begin{array}{l l} k z ^ {2} & \text { for } 0 \leq z \leq 1 \\ 1 & \text { for } 1 <   z \leq 1 \frac {1}{3} \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Trova il valore di $k .$ 

(b) Quale frazione degli articoli ricadrà al di fuori della "twilight zone" (ricadrà tra 0 e 1)? 

(c) Trova la media e la varianza di questa variabile casuale. 

47. Verifica l'Equazione 4.7.4. 

48. Dimostra l'Equazione 4.7.5 utilizzando l'induzione matematica. 

49. Sia X una variabile con varianza $\sigma _ { x } ^ { 2 }$ e sia Y una variabile con varianza $\sigma _ { y } ^ { 2 }$ . Partendo da 

$$
0 \leq \operatorname{Var} (X / \sigma_ {x} + Y / \sigma_ {y})
$$

mostra che 

$$
- 1 \leq \operatorname{Corr} (X, Y)
$$

Ora usando il fatto che 

$$
0 \leq \operatorname{Var} (X / \sigma_ {x} - Y / \sigma_ {y})
$$

concludi che 

$$
- 1 \leq \operatorname{Corr} (X, Y) \leq 1
$$

Utilizzando il risultato che $\mathrm { V a r } ( Z ) ~ = ~ 0$ implica che $Z$ sia costante, argomenta che se $\operatorname { C o r r } ( X , Y ) = 1 \ \mathrm { o r } - 1$ allora X e Y sono correlate da 

$$
Y = a + b x
$$

dove il segno di $b$ è positivo quando la correlazione è 1 e negativo quando è −1. 

50. Considera n prove indipendenti, ciascuna delle quali produce uno dei risultati $i , i =$ 1, 2, 3, con probabilità rispettive $\begin{array} { r } { p _ { 1 } , p _ { 2 } , p _ { 3 } , \sum _ { i = 1 } ^ { 3 } \gamma _ { i } = 1 } \end{array}$ . Sia $N _ { i }$ il numero di prove che producono il risultato i, e mostra che $\operatorname { C o v } ( N _ { 1 } , N _ { 2 } ) = - n p _ { 1 } p _ { 2 }$ Spiega anche perché è intuitivo che questa covarianza sia negativa. (Suggerimento: Per $i =$ $1 , \ldots , n ,$ , poniamo 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   trial   } i \text {   results   in   outcome   } 1 \\ 0 & \text { if   trial   } i \text {   does   not   result   in   outcome   } 1 \end{array} \right.
$$

Analogamente, per $j = 1 , \dots , n ,$ , poniamo 

$$
Y _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   trial   } j \text {   results   in   outcome   } 2 \\ 0 & \text { if   trial   } j \text {   does   not   result   in   outcome   } 2 \end{array} \right.
$$

Argomenta che 

$$
N _ {1} = \sum_ {i = 1} ^ {n} X _ {i}, \quad N _ {2} = \sum_ {j = 1} ^ {n} Y _ {j}
$$

Poi usa la Proposizione 4.7.2 e il Teorema 4.7.4.) 

51. Nell'Esempio 4.5f, calcola $\operatorname { C o v } ( X _ { i } , X _ { j } )$ e usa questo risultato per mostrare che $\mathrm { V a r } ( X ) = 1$ 

52. Se $X _ { 1 }$ e $X _ { 2 }$ hanno la stessa funzione di distribuzione di probabilità, mostra che 

$$
\operatorname{Cov} (X _ {1} - X _ {2}, X _ {1} + X _ {2}) = 0
$$

Nota che non viene assunta l'indipendenza. 

53. Supponiamo che X abbia la funzione di densità 

$$
f (x) = e ^ {- x}, \quad x > 0
$$

Calcola la funzione generatrice dei momenti di X e usa il tuo risultato per determinare la sua media e varianza. Verifica la tua risposta per la media tramite un calcolo diretto. 

54. Se la funzione di densità di X è 

$$
f (x) = 1, \quad 0 <   x <   1
$$

determina $E [ e ^ { t X } ]$ . Differenzia per ottenere $E [ X ^ { n } ]$ e poi verifica la tua risposta. 

55. Supponiamo che X sia una variabile casuale con media e varianza entrambe uguali a 20. Cosa si può dire su $P \{ 0 \leq X \leq 4 0 \}$ ? 

56. Dalla precedente esperienza, un professore sa che il punteggio del test di uno studente che sostiene il suo esame finale è una variabile casuale con media 75. 

(a) Fornisci un limite superiore alla probabilità che il punteggio del test di uno studente superi 85. 

Supponiamo inoltre che il professore sappia che la varianza del punteggio del test di uno studente sia uguale a 25. 

(b) Cosa si può dire sulla probabilità che uno studente ottenga un punteggio tra 65 e 85? 

(c) Quanti studenti dovrebbero sostenere l'esame per garantire, con probabilità almeno .9, che la media della classe sia entro 5 da 75? 

57. Siano X e Y aventi rispettive funzioni di distribuzione $F _ { X }$ e $F _ { Y }$ , e supponiamo che per alcune costanti a e $b > 0$ 

$$
F _ {X} (x) = F _ {Y} \left(\frac {x - a}{b}\right)
$$

(a) Determina E [X ] in termini di E [Y ].

(b) Determina Var(X ) in termini di $\mathrm { V a r } ( Y )$ 

Suggerimento: X ha la stessa distribuzione di quale altra variabile casuale? 

# VARIABILI CASUALI SPECIALI

Determinati tipi di variabili casuali si presentano ripetutamente nelle applicazioni. In questo capitolo, ne studieremo una varietà.

## 5.1 LE VARIABILI CASUALI DI BERNOULLI E BINOMIALI

Supponiamo che venga eseguita una prova, o un esperimento, il cui risultato può essere classificato come un "successo" o come un "fallimento". Se poniamo X = 1 quando il risultato è un successo e $X = 0$ quando è un fallimento, allora la funzione di massa di probabilità di X è data da

$$
\begin{array}{l} {P \{X = 0 \} = 1 - p} \\ {P \{X = 1 \} = p} \end{array}\tag{5.1.1}
$$

dove $\phi , 0 \le { \cal P } \le 1$ , è la probabilità che la prova sia un "successo." 

Una variabile casuale X si dice essere una variabile casuale di Bernoulli (in onore del matematico svizzero James Bernoulli) se la sua funzione di massa di probabilità è data dalle Equazioni 5.1.1 per alcuni ${ \boldsymbol { p } } \in ( 0 , 1 )$ . Il suo valore atteso è

$$
E [ X ] = 1 \cdot P \{X = 1 \} + 0 \cdot P \{X = 0 \} = p
$$

Ciò significa che l'aspettativa di una variabile casuale di Bernoulli è la probabilità che la variabile casuale sia uguale a 1. 

Supponiamo ora che debbano essere eseguite n prove indipendenti, ciascuna delle quali produce un "successo" con probabilità p e un "fallimento" con probabilità $1 - p ,$. Se X rappresenta il numero di successi che si verificano nelle n prove, allora X si dice essere una variabile casuale binomiale con parametri $( n , p )$ 

La funzione di massa di probabilità di una variabile casuale binomiale con parametri n e $\boldsymbol { \mathscr { P } }$ è data da

$$
P \{X = i \} = \binom {n} {i} p ^ {i} (1 - p) ^ {n - i}, \quad i = 0, 1, \ldots , n\tag{5.1.2}
$$

dove $\binom { n } { i } = n ! / [ i ! ( n - i ) ! ]$ è il numero di diversi gruppi di $i$ oggetti che possono essere scelti da un insieme di n oggetti. La validità dell'Equazione 5.1.2 può essere verificata notando prima che la probabilità di qualsiasi sequenza particolare delle n esitazioni contenenti $i$ successi e $n - i$ fallimenti è, per l'indipendenza assunta delle prove, $p ^ { i } ( 1 - p ) ^ { n - i }$ L'Equazione 5.1.2 segue quindi poiché ci sono $\binom { n } { i }$ diverse sequenze dei n risultati che portano a i successi e $n - i$ fallimenti — il che può forse essere visto più facilmente notando che ci sono $\binom { n } { i }$ diverse selezioni delle i prove che risultano in successi. Ad esempio, se $n = 5 , i = 2$ , allora ci sono $\textstyle { \binom { 5 } { 2 } }$ scelte delle due prove che devono risultare in successi — ovvero, uno qualsiasi dei risultati

$$
\begin{array}{l l l} (s, s, f, f, f) & (f, s, s, f, f) & (f, f, s, f, s) \\ (s, f, s, f, f) & (f, s, f, s, f) \\ (s, f, f, s, f) & (f, s, f, f, s) & (f, f, f, s, s) \\ (s, f, f, f, s) & (f, f, s, s, f) \end{array}
$$

dove il risultato $( f , s , f , s , f )$ significa, ad esempio, che i due successi sono apparsi nelle prove 2 e 4. Poiché ciascuno dei $\textstyle { \binom { 5 } { 2 } }$ risultati ha probabilità $ { p ^ { 2 } ( 1 - p ) ^ { 3 } }$ , vediamo che la probabilità di un totale di 2 successi in 5 prove indipendenti è ${ \binom { 5 } { 2 } } p ^ { 2 } ( 1 - p ) ^ { 3 }$ . Si noti che, per il teorema binomiale, le probabilità sommano a 1, cioè,

$$
\sum_ {i = 0} ^ {\infty} p (i) = \sum_ {i = 0} ^ {n} {\binom {n} {i}} p ^ {i} (1 - p) ^ {n - i} = [ p + (1 - p) ] ^ {n} = 1
$$

Le funzioni di massa di probabilità di tre variabili casuali binomiali con rispettivi parametri (10, .5), (10, .3) e (10, .6) sono presentate nella Figura 5.1. La prima di queste è simmetrica rispetto al valore .5, mentre la seconda è in qualche modo pesata, o asimmetrica, verso valori più bassi e la terza verso valori più alti. 

EXAMPLE 5.1a È noto che i dischi prodotti da una certa azienda saranno difettosi con probabilità .01 indipendentemente l'uno dall'altro. L'azienda vende i dischi in confezioni da 10 e offre una garanzia di rimborso se al massimo 1 dei 10 dischi è difettoso. Quale proporzione di confezioni viene restituita? Se qualcuno acquista tre confezioni, qual è la probabilità che esattamente una di esse venga restituita? 

SOLUTION Se X è il numero di dischi difettosi in una confezione, allora assumendo che i clienti approfittino sempre della garanzia, ne consegue che X è una variabile casuale binomiale con parametri (10, .01). Di conseguenza la probabilità che una confezione debba essere sostituita è 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5d1d72e949afd376f7f0f7e5d263bdb4706e2ea49a1e361c458661793f90412c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/0eeb9633576b2d79af4b76b46d6f400cc7b53ad8c707049b38551f201b923ee8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/3cd5c6dd1e6515523c6f072d9465228f14dff2ee76b560199e2af608f9bc9988.jpg)



FIGURE 5.1 Funzioni di massa di probabilità binomiali.


$$
\begin{array}{l} P \{X > 1 \} = 1 - P \{X = 0 \} - P \{X = 1 \} \\ \qquad = 1 - \binom {1 0} {0} (. 0 1) ^ {0} (. 9 9) ^ {1 0} - \binom {1 0} {1} (. 0 1) ^ {1} (. 9 9) ^ {9} \approx . 0 0 5 \end{array}
$$

Poiché ogni confezione dovrà, indipendentemente, essere sostituita con probabilità .005, ne consegue dalla legge dei grandi numeri che nel lungo periodo lo .5 percento delle confezioni dovrà essere sostituito.

Dal precedente segue che il numero di pacchi che la persona dovrà restituire è una variabile casuale binomiale con parametri $n = 3$ e $\begin{array} { r } { \ p = . 0 0 5 } \end{array}$. Pertanto, la probabilità che esattamente uno dei tre pacchi venga restituito è $\left( { \begin{array} { l } { 3 } \\ { 1 } \end{array} } \right) ( . 0 0 5 ) ( . 9 9 5 ) ^ { 2 } =$ .015. ■ 

EXAMPLE 5.1b Il colore degli occhi è determinato da una singola coppia di geni, con il gene per gli occhi marroni dominante rispetto a quello per gli occhi azzurri. Ciò significa che un individuo che possiede due geni per gli occhi azzurri avrà gli occhi azzurri, mentre uno che possiede due geni per gli occhi marroni o un gene per gli occhi marroni e uno per gli occhi azzurri avrà gli occhi marroni. Quando due persone si accoppiano, la prole risultante riceve un gene scelto casualmente da ciascuna delle coppie di geni dei genitori. Se il figlio più grande di una coppia di genitori con gli occhi marroni ha gli occhi azzurri, qual è la probabilità che esattamente due dei quattro altri figli (nessuno dei quali è un gemello) di questa coppia abbiano anche gli occhi azzurri? 

SOLUTION Per iniziare, si noti che poiché il figlio più grande ha gli occhi azzurri, ne consegue che entrambi i genitori devono avere un gene per gli occhi azzurri e uno per gli occhi marroni. (Perché se uno dei due avesse due geni per gli occhi marroni, allora ogni figlio riceverebbe almeno un gene per gli occhi marroni e avrebbe quindi gli occhi marroni.) La probabilità che una prole di questa coppia abbia gli occhi azzurri è uguale alla probabilità che riceva il gene per gli occhi azzurri da entrambi i genitori, che è $\textstyle { \left( { \frac { 1 } { 2 } } \right) } \left( { \frac { 1 } { 2 } } \right) = { \frac { 1 } { 4 } }$. Di conseguenza, poiché ciascuno degli altri quattro figli avrà gli occhi azzurri con probabilità $\textstyle { \frac { 1 } { 4 } } ;$, ne consegue che la probabilità che esattamente due di loro abbiano questo colore degli occhi è 

$$
\binom {4} {2} (1 / 4) ^ {2} (3 / 4) ^ {2} = 2 7 / 1 2 8 \quad \blacksquare
$$

EXAMPLE 5.1c Un sistema di comunicazioni consiste in n componenti, ognuno dei quali funzionerà, indipendentemente, con probabilità $\scriptstyle { \boldsymbol { \phi } } .$. Il sistema totale sarà in grado di operare efficacemente se almeno la metà dei suoi componenti funziona. 

(a) Per quali valori di $\boldsymbol { \mathscr { P } }$ un sistema a 5 componenti ha maggiori probabilità di operare efficacemente rispetto a un sistema a 3 componenti? 

(b) In generale, quando un sistema a $2 k + 1$ componenti è migliore di un sistema a $2 k - 1$ componenti?

## SOLUZIONE

(a) Poiché il numero di componenti funzionanti è una variabile casuale binomiale con parametri $( n , p )$, ne consegue che la probabilità che un sistema a 5 componenti sia efficace è 

$$
\binom {5} {3} p ^ {3} (1 - p) ^ {2} + \binom {5} {4} p ^ {4} (1 - p) + p ^ {5}
$$

mentre la probabilità corrispondente per un sistema a 3 componenti è 

$$
\binom {3} {2} p ^ {2} (1 - p) + p ^ {3}
$$

Pertanto, il sistema a 5 componenti è migliore se 

$$
1 0 p ^ {3} (1 - p) ^ {2} + 5 p ^ {4} (1 - p) + p ^ {5} \geq 3 p ^ {2} (1 - p) + p ^ {3}
$$

che si riduce a 

$$
3 (p - 1) ^ {2} (2 p - 1) \geq 0
$$

o 

$$
p \geq \frac {1}{2}
$$

(b) In generale, un sistema con $2 k + 1$ componenti sarà migliore di uno con $2 k - 1$ componenti se (e solo se) $\begin{array} { r } { p \geq \frac { 1 } { 2 } } \end{array}$. Per dimostrarlo, consideriamo un sistema di $2 k + 1$ componenti e poniamo che X denoti il numero dei primi $2 k - 1$ che funzionano. Allora 

$$
P _ {2 k + 1} (\mathrm{effective}) = P \{X \geq k + 1 \} + P \{X = k \} (1 - (1 - p) ^ {2}) + P \{X = k - 1 \} p ^ {2}
$$

che segue poiché il sistema a componenti $2 k + 1$ sarà efficace se (1) $X \geq k + 1$ ; 

(2) $X = k$ e almeno una delle restanti 2 componenti funziona; o 

(3) $X = k - 1$ e entrambe le successive 2 funzionano. 

Poiché 

$$
\begin{array}{c} P _ {2 k - 1} (\text { effective }) = P \{X \geq k \} \\ = P \{X = k \} + P \{X \geq k + 1 \} \end{array}
$$

otteniamo che 

$$
\begin{array}{l} P _ {2 k + 1} (\text {effective}) - P _ {2 k - 1} (\text {effective}) \\ \quad = P \{X = k - 1 \} p ^ {2} - (1 - p) ^ {2} P \{X = k \} \\ \quad = \binom {2 k - 1} {k - 1} p ^ {k - 1} (1 - p) ^ {k} p ^ {2} - (1 - p) ^ {2} \binom {2 k - 1} {k} p ^ {k} (1 - p) ^ {k - 1} \\ \quad = \binom {2 k - 1} {k} p ^ {k} (1 - p) ^ {k} [ p - (1 - p) ] \qquad \text {since} \binom {2 k - 1} {k - 1} = \binom {2 k - 1} {k} \\ \quad \geq 0 \Leftrightarrow p \geq \frac {1}{2} \quad \blacksquare \end{array}
$$

EXAMPLE 5.1d Supponiamo che il 10 percento dei chip prodotti da un produttore di hardware per computer siano difettosi. Se ordiniamo 100 di questi chip, X, il numero di quelli difettosi che riceviamo, sarà una variabile casuale binomiale? 

SOLUZIONE La variabile casuale X sarà una variabile casuale binomiale con parametri (100, .1) se ogni chip ha probabilità .9 di essere funzionante e se il funzionamento dei chip successivi è indipendente. Se questa sia un'ipotesi ragionevole quando sappiamo che il 10 percento dei chip prodotti sono difettosi dipende da fattori aggiuntivi. Ad esempio, supponiamo che tutti i chip prodotti in un determinato giorno siano sempre o funzionanti o difettosi (con il 90 percento dei giorni che risultano in chip funzionanti). In questo caso, se sappiamo che tutti i nostri 100 chip sono stati fabbricati lo stesso giorno, allora X non sarà una variabile casuale binomiale. Questo accade poiché l'indipendenza dei chip successivi non è valida. Infatti, in questo caso, avremmo 

$$
\begin{array}{c} P \{X = 1 0 0 \} = . 1 \\ P \{X = 0 \} = . 9 \end{array}
$$

Poiché una variabile casuale binomiale X, con parametri n e ${ \boldsymbol { p } } ,$ rappresenta il numero di successi in n prove indipendenti, ciascuna avente probabilità di successo ${ \boldsymbol { p } } ,$, possiamo rappresentare X come segue: 

$$
X = \sum_ {i = 1} ^ {n} X _ {i}\tag{5.1.3}
$$

dove 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   trial   is   a   success } \\ 0 & \text { otherwise } \end{array} \right.
$$

Poiché le $X _ { i } , i = 1 , \dotsc , n$ sono variabili casuali di Bernoulli indipendenti, abbiamo che 

$$
\begin{array}{c} {E [ X _ {i} ] = P \{X _ {i} = 1 \} = p} \\ {\mathrm{Var} (X _ {i}) = E [ X _ {i} ^ {2} ] - p ^ {2}} \\ {= p (1 - p)} \end{array}
$$

dove l'ultima uguaglianza segue poiché $X _ { i } ^ { 2 } = X _ { i } ;$, e quindi $E [ X _ { i } ^ { 2 } ] = E [ X _ { i } ] = p ,$ 

Utilizzando la rappresentazione dell'Equazione 5.1.3, è ora una questione facile calcolare la media e la varianza di X: 

$$
\begin{array}{c} E [ X ] = \sum_ {i = 1} ^ {n} E [ X _ {i} ] \\ = n p \end{array}
$$

$$
\begin{array}{l l} \operatorname{Var} (X) = \sum_ {i = 1} ^ {n} \operatorname{Var} (X _ {i}) & \text { since   the } X _ {i} \text { are   independent } \\ = n p (1 - p) \end{array}
$$

Se $X _ { 1 }$ e $X _ { 2 }$ sono variabili casuali binomiali indipendenti aventi rispettivi parametri $( n _ { i } , p ) , i = 1 , 2$, allora la loro somma è binomiale con parametri $( n _ { 1 } + n _ { 2 } , p )$. Ciò può essere visto più facilmente notando che poiché $X _ { i } , i = 1 , 2$, rappresenta il numero di successi in $n _ { i }$ prove indipendenti ciascuna delle quali è un successo con probabilità ${ \boldsymbol { p } } ,$ allora $X _ { 1 } + X _ { 2 }$ rappresenta il numero di successi in $n _ { 1 } + n _ { 2 }$ prove indipendenti ciascuna delle quali è un successo con probabilità $\mathbf { \nabla } ^ { p . }$ Pertanto, $X _ { 1 } + X _ { 2 }$ è binomiale con parametri $( n _ { 1 } + n _ { 2 } , p )$

## 5.1.1 Calcolo della funzione di distribuzione binomiale

Supponiamo che X sia binomiale con parametri $( n , p )$. La chiave per calcolare la sua funzione di distribuzione

$$
P \{X \leq i \} = \sum_ {k = 0} ^ {i} {\binom {n} {k}} p ^ {k} (1 - p) ^ {n - k}, \qquad i = 0, 1, \ldots , n
$$

è utilizzare la seguente relazione tra $P \{ X = k + 1 \}$ e $P \{ X = k \}$ :

$$
P \{X = k + 1 \} = \frac {p}{1 - p} \frac {n - k}{k + 1} P \{X = k \}\tag{5.1.4}
$$

La dimostrazione di questa equazione è lasciata come esercizio.

EXAMPLE 5.1e Sia X una variabile casuale binomiale con parametri $n = 6 , \phi = . 4$. Allora, partendo da $P \{ X = 0 \} = ( . 6 ) ^ { 6 }$ e utilizzando ricorsivamente l'Equazione 5.1.4, otteniamo

$$
\begin{array}{l} P \{X = 0 \} = (. 6) ^ {6} = . 0 4 6 7 \\ P \{X = 1 \} = \frac {4}{6} \frac {6}{1} P \{X = 0 \} = . 1 8 6 6 \\ P \{X = 2 \} = \frac {4}{6} \frac {5}{2} P \{X = 1 \} = . 3 1 1 0 \\ P \{X = 3 \} = \frac {4}{6} \frac {4}{3} P \{X = 2 \} = . 2 7 6 5 \\ P \{X = 4 \} = \frac {4}{6} \frac {3}{4} P \{X = 3 \} = . 1 3 8 2 \\ P \{X = 5 \} = \frac {4}{6} \frac {2}{5} P \{X = 4 \} = . 0 3 6 9 \\ P \{X = 6 \} = \frac {4}{6} \frac {1}{6} P \{X = 5 \} = . 0 0 4 1. \end{array}
$$

Il disco di testo utilizza l'Equazione 5.1.4 per calcolare le probabilità binomiali. Utilizzandolo, si inseriscono i parametri binomiali n e $\boldsymbol { \mathscr { P } }$ e un valore i, e il programma calcola le probabilità che una variabile casuale binomiale $( n , p )$ sia uguale a e minore o uguale a i.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/c760367d170666d6fe0108a81cc617d241f69497684645f25af6a9bb4b2bbec2.jpg)



FIGURE 5.2


EXAMPLE 5.1f Se X è una variabile casuale binomiale con parametri $n = 1 0 0$ e $ p = . 7 5$ trova $P \{ X = 7 0 \}$ e $P \{ X \leq 7 0 \}$

SOLUTION Il disco di testo fornisce le risposte mostrate nella Figura 5.2. ■

## 5.2 LA VARIABILE CASUALE DI POISSON

Una variabile casuale X, che assume uno dei valori 0, 1, $2 , \ldots ,$ si dice essere una variabile casuale di Poisson con parametro $\lambda , \lambda > 0$, se la sua funzione di massa di probabilità è data da

$$
P \{X = i \} = e ^ {- \lambda} \frac {\lambda^ {i}}{i !}, \qquad i = 0, 1, \ldots\tag{5.2.1}
$$

Il simbolo e rappresenta una costante approssimativamente uguale a 2.7183. È una famosa costante in matematica, intitolata al matematico svizzero L. Euler, ed è anche la base del cosiddetto logaritmo naturale.

L'equazione 5.2.1 definisce una funzione di massa di probabilità, poiché

$$
\sum_ {i = 0} ^ {\infty} p (i) = e ^ {- \lambda} \sum_ {i = 0} ^ {\infty} \lambda^ {i} / i! = e ^ {- \lambda} e ^ {\lambda} = 1
$$

Un grafico di questa funzione di massa quando $\lambda = 4$ è fornito nella Figura 5.3.

La distribuzione di probabilità di Poisson è stata introdotta da S. D. Poisson in un libro che scrisse trattando l'applicazione della teoria della probabilità a cause legali, processi penali e simili. Questo libro, pubblicato nel 1837, era intitolato Recherches sur la probabilité des jugements en matière criminelle et en matière civile.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5c04de0ee9e3ebb27466fb2a39c621eb39a86a081e40ae8e2fd59f9be16acd37.jpg)



FIGURA 5.3 La funzione di massa di probabilità di Poisson con $\lambda = 4 .$


Come preludio alla determinazione della media e della varianza di una variabile casuale di Poisson, determiniamo prima la sua funzione generatrice dei momenti.

$$
\begin{array}{l} \phi (t) = E [ e ^ {t X} ] \\ \qquad = \sum_ {i = 0} ^ {\infty} e ^ {t i} e ^ {- \lambda} \lambda^ {i} / i! \\ \qquad = e ^ {- \lambda} \sum_ {i = 0} ^ {\infty} (\lambda e ^ {t}) ^ {i} / i! \\ \qquad = e ^ {- \lambda} e ^ {\lambda e ^ {t}} \\ \qquad = \exp \{\lambda (e ^ {t} - 1) \} \end{array}
$$

La derivazione produce

$$
\begin{array}{r l} & {\phi^ {\prime} (t) = \lambda e ^ {t} \exp \{\lambda (e ^ {t} - 1) \}} \\ & {\phi^ {\prime \prime} (t) = (\lambda e ^ {t}) ^ {2} \exp \{\lambda (e ^ {t} - 1) \} + \lambda e ^ {t} \exp \{\lambda (e ^ {t} - 1) \}} \end{array}
$$

Valutando a $t = 0$ si ottiene che

$$
E [ X ] = \phi^ {\prime} (0) = \lambda
$$

$$
\begin{array}{r} \operatorname{Var} (X) = \phi^ {\prime \prime} (0) - (E [ X ]) ^ {2} \\ = \lambda^ {2} + \lambda - \lambda^ {2} = \lambda \end{array}
$$

Così sia la media che la varianza di una variabile casuale di Poisson sono uguali al parametro λ.

La variabile casuale di Poisson ha un'ampia gamma di applicazioni in una varietà di aree perché può essere utilizzata come approssimazione per una variabile casuale binomiale con parametri $( n , p )$ quando n è grande e $\boldsymbol { \underline { P } }$ è piccolo. Per vederlo, supponiamo che X sia una variabile casuale binomiale con parametri $( n , p )$ e poniamo $\lambda = n p$. Allora

$$
\begin{array}{r l} P \{X = i \} & = \frac {n !}{(n - 1) ! i !} p ^ {i} (1 - p) ^ {n - i} \\ & = \frac {n !}{(n - 1) ! i !} \left(\frac {\lambda}{n}\right) ^ {i} \left(1 - \frac {\lambda}{n}\right) ^ {n - i} \\ & = \frac {n (n - 1) \ldots (n - i + 1)}{n ^ {i}} \frac {\lambda^ {i}}{i !} \frac {(1 - \lambda / n) ^ {n}}{(1 - \lambda / n) ^ {i}} \end{array}
$$

Ora, per n grande e $\boldsymbol { \mathscr { P } }$ piccolo,

$$
\left(1 - \frac {\lambda}{n}\right) ^ {n} \approx e ^ {- \lambda} \quad \frac {n (n - 1) \ldots (n - i + 1)}{n ^ {i}} \approx 1 \quad \left(1 - \frac {\lambda}{n}\right) ^ {i} \approx 1
$$

Pertanto, per n grande e $\boldsymbol { \underline { P } }$ piccolo,

$$
P \{X = i \} \approx e ^ {- \lambda} \frac {\lambda^ {i}}{i !}
$$

In altre parole, se vengono eseguiti n tentativi indipendenti, ciascuno dei quali produce un "successo" con probabilità ${ \boldsymbol { p } } ,$, allora quando n è grande e $\boldsymbol { \underline { P } }$ piccolo, il numero di successi che si verificano è approssimativamente una variabile casuale di Poisson con media $\lambda = n p$

Alcuni esempi di variabili casuali che solitamente obbediscono, a una buona approssimazione, alla legge di probabilità di Poisson (ovvero, solitamente obbediscono all'Equazione 5.2.1 per qualche valore di λ) sono:

1. Il numero di errori di stampa su una pagina (o un gruppo di pagine) di un libro.

2. Il numero di persone in una comunità che raggiungono i 100 anni di età.

3. Il numero di numeri di telefono errati che vengono composti in un giorno.

4. Il numero di transistor che falliscono nel loro primo giorno di utilizzo.

5. Il numero di clienti che entrano in un ufficio postale in un dato giorno.

6. Il numero di particelle α scaricate in un periodo di tempo fisso da una certa particella radioattiva.

Ciascuno dei precedenti, e numerose altre variabili casuali, è approssimativamente di Poisson per la stessa ragione — ovvero, a causa dell'approssimazione di Poisson della binomiale. Ad esempio, possiamo supporre che esista una piccola probabilità p che ogni lettera digitata su una pagina sia stampata in modo errato, e quindi il numero di errori di stampa su una data pagina sarà approssimativamente di Poisson con media $\lambda = n p$ dove n è il (presumibilmente) grande numero di lettere su quella pagina. Allo stesso modo, possiamo supporre che ogni persona in una data comunità, indipendentemente, abbia una piccola probabilità p di raggiungere l'età di 100 anni, e quindi il numero di persone che lo faranno avrà approssimativamente una distribuzione di Poisson con media np dove n è il grande numero di persone nella comunità. Lasciamo al lettore il compito di ragionare sul perché le restanti variabili casuali negli esempi da 3 a 6 dovrebbero avere approssimativamente una distribuzione di Poisson.

Esempio 5.2a Supponiamo che il numero medio di incidenti che si verificano settimanalmente su un particolare tratto di autostrada sia uguale a 3. Calcolare la probabilità che ci sia almeno un incidente questa settimana.

SOLUZIONE Sia $X$ il numero di incidenti che si verificano sul tratto di autostrada in questione durante questa settimana. Poiché è ragionevole supporre che vi sia un gran numero di auto che transitano lungo quel tratto, ciascuna con una piccola probabilità di essere coinvolta in un incidente, il numero di tali incidenti dovrebbe essere approssimativamente distribuito secondo una distribuzione di Poisson. Pertanto,

$$
\begin{array}{r l} P \{X \geq 1 \} & = 1 - P \{X = 0 \} \\ & = 1 - e ^ {- 3} \frac {3 ^ {0}}{0 !} \\ & = 1 - e ^ {- 3} \\ & \approx . 9 5 0 2 \quad \blacksquare \end{array}
$$

Esempio 5.2b Supponiamo che la probabilità che un articolo prodotto da una certa macchina sia difettoso sia .1. Trovare la probabilità che un campione di 10 articoli contenga al massimo un articolo difettoso. Assumere che la qualità degli articoli successivi sia indipendente.

SOLUZIONE La probabilità desiderata è $\textstyle { \binom { 1 0 } { 0 } } ( . 1 ) ^ { 0 } ( . 9 ) ^ { 1 0 } + { \binom { 1 0 } { 1 } } ( . 1 ) ^ { 1 } ( . 9 ) ^ { 9 } = . 7 3 6 1$, mentre l'approssimazione di Poisson fornisce il valore

$$
e ^ {- 1} \frac {1 ^ {0}}{0 !} + e ^ {- 1} \frac {1 ^ {1}}{1 !} = 2 e ^ {- 1} \approx . 7 3 5 8
$$

Esempio 5.2c Considerare un esperimento che consiste nel contare il numero di particelle $\alpha$ emesse in un intervallo di un secondo da un grammo di materiale radioattivo. Se sappiamo dall'esperienza passata che, in media, vengono emesse 3.2 tali particelle $\alpha$, quale sarebbe una buona approssimazione della probabilità che non compaiano più di 2 particelle $\alpha$?

SOLUZIONE Se pensiamo al grammo di materiale radioattivo come composto da un gran numero $n$ di atomi, ciascuno dei quali ha la probabilità $3.2/n$ di disintegrarsi e emettere una particella $\alpha$ durante il secondo considerato, allora vediamo che, con una approssimazione molto vicina, il numero di particelle $\alpha$ emesse sarà una variabile casuale di Poisson con parametro $\lambda = 3 . 2$. Pertanto la probabilità desiderata è

$$
\begin{array}{r l} P \{X \leq 2 \} & = e ^ {- 3. 2} + 3. 2 e ^ {- 3. 2} + \frac {(3 . 2) ^ {2}}{2} e ^ {- 3. 2} \\ & = . 3 8 2 \quad \blacksquare \end{array}
$$

Esempio 5.2d Se il numero medio di sinistri gestiti giornalmente da una compagnia di assicurazione è 5, quale proporzione di giorni ha meno di 3 sinistri? Qual è la probabilità che ci saranno 4 sinistri esattamente in 3 dei prossimi 5 giorni? Assumere che il numero di sinistri in giorni diversi sia indipendente.

SOLUZIONE Poiché la compagnia probabilmente assicura un gran numero di clienti, ciascuno con una piccola probabilità di presentare un sinistro in un dato giorno, è ragionevole supporre che il numero di sinistri gestiti giornalmente, chiamiamolo $X$, sia una variabile casuale di Poisson. Poiché $E ( X ) = 5$, la probabilità che ci siano meno di 3 sinistri in un dato giorno è

$$
\begin{array}{r l} P \{X \leq 3 \} & = P \{X = 0 \} + P \{X = 1 \} + P \{X = 2 \} \\ & = e ^ {- 5} + e ^ {- 5} \frac {5 ^ {1}}{1 !} + e ^ {- 5} \frac {5 ^ {2}}{2 !} \\ & = \frac {3 7}{2} e ^ {- 5} \\ & \approx . 1 2 4 7 \end{array}
$$

Poiché ogni dato giorno avrà meno di 3 sinistri con probabilità .125, segue, dalla legge dei grandi numeri, che nel lungo periodo il 12.5 percento dei giorni avrà meno di 3 sinistri.

Dall'indipendenza assunta del numero di sinistri su giorni successivi segue che il numero di giorni in un intervallo di 5 giorni che ha esattamente 4 sinistri è una variabile casuale binomiale con parametri 5 e $P \{ X = 4 \}$. Poiché

$$
P \{X = 4 \} = e ^ {- 5} \frac {5 ^ {4}}{4 !} \approx . 1 7 5 5
$$

segue che la probabilità che 3 dei prossimi 5 giorni abbiano 4 sinistri è uguale a

$$
\binom {5} {3} (. 1 7 5 5) ^ {3} (. 8 2 4 5) ^ {2} \approx . 0 3 6 7 \quad \blacksquare
$$

Si può dimostrare che il risultato dell'approssimazione di Poisson è valido anche in condizioni più generali di quelle menzionate finora. Ad esempio, supponiamo che debbano essere eseguiti $n$ tentativi indipendenti, con il $i$-esimo tentativo che risulta in un successo con probabilità $p _ { i } , i = 1 , \ldots , n .$. Allora si può dimostrare che se $n$ è grande e ogni $\mathbf { \nabla } \phi _ { i }$ è piccolo, allora il numero di tentativi riusciti è approssimativamente distribuito secondo una distribuzione di Poisson con media uguale a $\sum _ { i = 1 } ^ { n } p _ { i }$. In effetti, questo risultato rimarrà talvolta vero anche quando i tentativi non sono indipendenti, purché la loro dipendenza sia "debole". Ad esempio, consideriamo il seguente esempio.

Esempio 5.2e A una festa $n$ persone mettono i loro cappelli al centro di una stanza, dove i cappelli vengono mescolati insieme. Ogni persona sceglie quindi casualmente un cappello. Se $X$ denota il numero di persone che scelgono il proprio cappello allora, per grandi $^ { n , }$ si può dimostrare che $X$ ha approssimativamente una distribuzione di Poisson con media 1. Per vedere perché questo potrebbe essere vero, poniamo

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   person   selects   his   or   her   own   hat } \\ 0 & \text { otherwise } \end{array} \right.
$$

Allora possiamo esprimere X come 

$$
X = X _ {1} + \dots + X _ {n}
$$

e quindi X può essere considerato come rappresentante il numero di "successi" in n "prove" dove la prova $i$ è detta un successo se la $i$-esima persona sceglie il proprio cappello. Ora, poiché la $i$-esima persona ha la stessa probabilità di finire con uno qualsiasi dei $n$ cappelli, uno dei quali è il proprio, ne consegue che 

$$
P \{X _ {i} = 1 \} = \frac {1}{n}\tag{5.2.2}
$$

Supponiamo ora che $i \neq j$ e consideriamo la probabilità condizionata che la $i$-esima persona scelga il proprio cappello dato che la $j$-esima persona lo fa — cioè, consideriamo $P \{ X _ { i } = 1 | X _ { j } = 1 \}$ Ora dato che la $j$-esima persona seleziona effettivamente il proprio cappello, ne consegue che l'individuo $i$ ha la stessa probabilità di finire con uno qualsiasi dei rimanenti $n - 1$, uno dei quali è il proprio. Pertanto, ne consegue che 

$$
P \{X _ {i} = 1 | X _ {j} = 1 \} = \frac {1}{n - 1}\tag{5.2.3}
$$

Così, vediamo dalle Equazioni 5.2.2 e 5.2.3 che mentre le prove non sono indipendenti, la loro dipendenza è piuttosto debole [poiché, se la suddetta probabilità condizionata fosse uguale a $1/n$ invece di $1 / ( n - 1 )$), allora le prove $i$ e $j$ sarebbero indipendenti]; e quindi non è affatto sorprendente che X abbia approssimativamente una distribuzione di Poisson. Il fatto che $E [ X ] = 1$ segue poiché 

$$
\begin{array}{r l} E [ X ] & = E [ X _ {1} + \dots + X _ {n} ] \\ & = E [ X _ {1} ] + \dots + E [ X _ {n} ] \\ & = n \left(\frac {1}{n}\right) = 1 \end{array}
$$

L'ultima uguaglianza segue poiché, dall'Equazione 5.2.2, 

$$
E [ X _ {i} ] = P \{X _ {i} = 1 \} = \frac {1}{n}
$$

La distribuzione di Poisson possiede la proprietà riproduttiva che la somma di variabili casuali di Poisson indipendenti è anche una variabile casuale di Poisson. Per vederlo, supponiamo che $X _ { 1 }$ e $X _ { 2 }$ siano variabili casuali di Poisson indipendenti aventi rispettive medie $\lambda _ { 1 }$ e $\lambda _ { 2 }$. Allora la funzione generatrice dei momenti di $X _ { 1 } + X _ { 2 }$ è la seguente: 

$$
\begin{array}{l} E [ e ^ {t (X _ {1} + X _ {2})} ] = E [ e ^ {t X _ {1}} e ^ {t X _ {2}} ] \\ \qquad = E [ e ^ {t X _ {1}} ] E [ e ^ {t} X _ {2} ] \qquad \text { by   independence } \\ \qquad = \exp \{\lambda_ {1} (e ^ {t} - 1) \} \exp \{\lambda_ {2} (e ^ {t} - 1) \} \\ \qquad = \exp \{(\lambda_ {1} + \lambda_ {2}) (e ^ {t} - 1) \} \end{array}
$$

Poiché $\exp($\{ ( \lambda _ { 1 } + \lambda _ { 2 } ) ( e ^ { t } - 1 ) \}$)$ è la funzione generatrice dei momenti di una variabile casuale di Poisson avente media $\lambda _ { 1 } + \lambda _ { 2 }$, possiamo concludere, dal fatto che la funzione generatrice dei momenti specifica univocamente la distribuzione, che $X _ { 1 } + X _ { 2 }$ è di Poisson con media $\lambda _ { 1 } + \lambda _ { 2 }$ 

EXAMPLE 5.2f È stato stabilito che il numero di stereofoni difettosi prodotti quotidianamente in un certo impianto è distribuito secondo una distribuzione di Poisson con media $4 .$. In un arco di 2 giorni, qual è la probabilità che il numero di stereofoni difettosi non superi 3? 

SOLUTION Assumendo che $X _ { 1 }$, il numero di difettosi prodotti durante il primo giorno, sia indipendente da $X _ { 2 }$, il numero prodotto durante il secondo giorno, allora $X _ { 1 } + X _ { 2 }$ è di Poisson con media 8. Pertanto, 

$$
P \{X _ {1} + X _ {2} \leq 3 \} = \sum_ {i = 0} ^ {3} e ^ {- 8} \frac {8 ^ {i}}{i !} = . 0 4 2 3 8
$$

Consideriamo ora una situazione in cui si verificherà un numero casuale, chiamiamolo N, di eventi, e supponiamo che ciascuno di questi eventi sarà indipendentemente un evento di tipo 1 con probabilità $\cdot \mathbf { \nabla } _ { \mathbf { \phi } } ^ { p }$ o un evento di tipo 2 con probabilità $1 - p$. Sia $N _ { 1 }$ e $N _ { 2 }$ denotino, rispettivamente, i numeri di eventi di tipo 1 e di tipo 2 che si verificano. (Così $N = N _ { 1 } + N _ { 2 } . )$ Se N è distribuito secondo una distribuzione di Poisson con media $\lambda _ { i }$, allora la funzione di massa di probabilità congiunta di $N _ { 1 }$ e $N _ { 2 }$ si ottiene come segue. 

$$
\begin{array}{r l} & P \{N _ {1} = n, N _ {2} = m \} = P \{N _ {1} = n, N _ {2} = m, N = n + m \} \\ & \qquad = P \{N _ {1} = n, N _ {2} = m | N = n + m \} P \{N = n + m \} \\ & \qquad = P \{N _ {1} = n, N _ {2} = m | N = n + m \} e ^ {- \lambda} \frac {\lambda^ {n + m}}{(n + m) !} \end{array}
$$

Ora, dato un totale di $n + m$ eventi, poiché ciascuno di questi eventi è indipendentemente di tipo 1 con probabilità ${ \boldsymbol { p } } ,$ ne consegue che la probabilità condizionata che ci siano esattamente $n$ eventi di tipo 1 (e $m$ eventi di tipo 2) è la probabilità che una variabile casuale binomiale $( n + m , p )$ sia uguale a $n$. Di conseguenza, 

$$
\begin{array}{c} P \{N _ {1} = n, N _ {2} = m \} = \frac {(n + m) !}{n ! m !} p ^ {n} (1 - p) ^ {m} e ^ {- \lambda} \frac {\lambda^ {n + m}}{(n + m) !} \\ = e ^ {- \lambda p} \frac {(\lambda p) ^ {n}}{n !} e ^ {- \lambda (1 - p)} \frac {(\lambda (1 - p)) ^ {m}}{m !} \end{array}\tag{5.2.4}
$$

La funzione di massa di probabilità di $N _ { 1 }$ è quindi 

$$
\begin{array}{l} P \{N _ {1} = n \} = \sum_ {m = 0} ^ {\infty} P \{N _ {1} = n, N _ {2} = m \} \\ \qquad = e ^ {- \lambda p} \frac {(\lambda p) ^ {n}}{n !} \sum_ {m = 0} ^ {\infty} e ^ {- \lambda (1 - p)} \frac {(\lambda (1 - p)) ^ {m}}{m !} \\ \qquad = e ^ {- \lambda p} \frac {(\lambda p) ^ {n}}{n !} \end{array}\tag{5.2.5}
$$

Analogamente, 

$$
P \{N _ {2} = m \} = \sum_ {n = 0} ^ {\infty} P \{N _ {1} = n, N _ {2} = m \} = e ^ {- \lambda (1 - p)} \frac {(\lambda (1 - p)) ^ {m}}{m !}\tag{5.2.6}
$$

Ora ne consegue dalle Equazioni 5.2.4, 5.2.5 e 5.2.6, che $N _ { 1 }$ e $N _ { 2 }$ sono variabili casuali di Poisson indipendenti con rispettive medie $\lambda _ { P }$ e $\lambda ( 1 - p )$

Il risultato precedente si generalizza quando ciascuno dei eventi di numero di Poisson può essere classificato in una qualsiasi delle $r$ categorie, producendo la seguente importante proprietà della distribuzione di Poisson: Se ciascuno dei eventi di numero di Poisson avente media $\lambda$ è classificato indipendentemente come appartenente a uno dei tipi $1 , \ldots , r ,$ con probabilità rispettive $\begin{array} { r } { p 1 , \dotsc , \dotsc , \dotsc , \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc } \end{array}$, allora i numeri di eventi di tipo $1 , \ldots , r$ sono variabili casuali di Poisson indipendenti con medie rispettive $\lambda p _ { 1 } , \ldots , \lambda p _ { r }$ 

## 5.2.1 Calcolo della Funzione di Distribuzione di Poisson

Se $X$ è di Poisson con media $\lambda$, allora 

$$
\frac {P \{X = i + 1 \}}{P \{X = i \}} = \frac {e ^ {- \lambda} \lambda^ {i + 1} / (i + 1) !}{e ^ {- \lambda} \lambda^ {i} / i !} = \frac {\lambda}{i + 1}\tag{5.2.7}
$$

Partendo da $P \{ X = 0 \} = e ^ { - \lambda }$, possiamo usare l'Equazione 5.2.7 per calcolare successivamente 

$$
P \{X = 1 \} = \lambda P \{X = 0 \}
$$

$$
P \{X = 2 \} = \frac {\lambda}{2} P \{X = 1 \}
$$

$$
P \{X = i + 1 \} = \frac {\lambda}{i + 1} P \{X = i \}
$$

Il testo disk include un programma che utilizza l'Equazione 5.2.7 per calcolare le probabilità di Poisson.

## 5.3 LA VARIABILE CASUALE Ipergeometrica

Un contenitore contiene $N + M$ batterie, di cui N sono di qualità accettabile e le altre M sono difettose. Un campione di dimensione n deve essere scelto casualmente (senza reinserimento) nel senso che l'insieme delle batterie campionate ha la stessa probabilità di essere qualsiasi dei $\scriptstyle { \binom { \lambda - M + M } { n } }$ sottoinsiemi di dimensione n. Se poniamo X come il numero di batterie accettabili nel campione, allora

$$
P \{X = i \} = \frac {\binom {N} {i} \binom {M} {n - i}}{\binom {N + M} {n}}, \qquad i = 0, 1, \ldots , \min (N, n) ^ {*}\tag{5.3.1}
$$

Qualsiasi variabile casuale X la cui funzione di massa di probabilità è data dall'Equazione 5.3.1 è detta una variabile casuale ipergeometrica con parametri $N , M , n .$

ESEMPIO 5.3a I componenti di un sistema a 6 componenti devono essere scelti casualmente da un contenitore di 20 componenti usati. Il sistema risultante sarà funzionale se almeno 4 dei suoi 6 componenti sono in condizioni di funzionamento. Se 15 dei 20 componenti nel contenitore sono in condizioni di funzionamento, qual è la probabilità che il sistema risultante sia funzionale?

SOLUZIONE Se X è il numero di componenti funzionanti scelti, allora X è ipergeometrica con parametri 15, 5, 6. La probabilità che il sistema sia funzionale è

$$
\begin{array}{l} P \{X \geq 4 \} = \sum_ {i = 4} ^ {6} P \{X = i \} \\ = \frac {\binom {1 5} {4} \binom {5} {2} + \binom {1 5} {5} \binom {5} {1} + \binom {1 5} {6} \binom {5} {0}}{\binom {2 0} {6}} \\ \approx . 8 6 8 7 \quad \blacksquare \end{array}
$$

Per calcolare la media e la varianza di una variabile casuale ipergeometrica la cui funzione di massa di probabilità è data dall'Equazione 5.3.1, immaginiamo che le batterie siano estratte sequenzialmente e poniamo

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   selection   is   acceptable } \\ 0 & \text { otherwise } \end{array} \right.
$$

Ora, poiché la i-esima selezione ha la stessa probabilità di essere qualsiasi delle $N + M$ batterie, di cui N sono accettabili, ne consegue che

$$
P \{X _ {i} = 1 \} = \frac {N}{N + M}\tag{5.3.2}
$$

Inoltre, per $i \neq j$

$$
\begin{array}{r} P \{X _ {i} = 1, X _ {j} = 1 \} = P \{X _ {i} = 1 \} P \{X _ {j} = 1 | X _ {i} = 1 \} \\ = \frac {N}{N + M} \frac {N - 1}{N + M - 1} \end{array}\tag{5.3.3}
$$

che segue poiché, dato che la i-esima selezione è accettabile, la j-esima selezione ha la stessa probabilità di essere qualsiasi delle altre $N + M - 1$ batterie di cui $N - 1$ sono accettabili.

Per calcolare la media e la varianza di $X ,$ il numero di batterie accettabili nel campione di dimensione n, si usi la rappresentazione

$$
X = \sum_ {i = 1} ^ {n} X _ {i}
$$

Questo fornisce

$$
E [ X ] = \sum_ {i = 1} ^ {n} E [ X _ {i} ] = \sum_ {i = 1} ^ {n} P \{X _ {i} = 1 \} = \frac {n N}{N + M}\tag{5.3.4}
$$

Inoltre, il Corollario 4.7.3 per la varianza di una somma di variabili casuali fornisce

$$
\operatorname{Var} (X) = \sum_ {i = 1} ^ {n} \operatorname{Var} \left(X _ {i}\right) + 2 \sum_ {1 \leq i <   j \leq n} \operatorname{Cov} \left(X _ {i}, X _ {j}\right)\tag{5.3.5}
$$

Ora, $X _ { i }$ è una variabile casuale di Bernoulli e quindi

$$
\operatorname{Var} (X _ {i}) = P \{X _ {i} = 1 \} (1 - P \{X _ {i} = 1 \}) = \frac {N}{N + M} \frac {M}{N + M}\tag{5.3.6}
$$

Inoltre, per $i < j$

$$
\operatorname{Cov} (X _ {i}, X _ {j}) = E [ X _ {i} X _ {j} ] - E [ X _ {i} ] E [ X _ {j} ]
$$

Ora, poiché sia $X _ { i }$ che $X _ { j }$ sono variabili casuali di Bernoulli (ovvero, 0 - 1), ne consegue che $X _ { i } X _ { j }$ è una variabile casuale di Bernoulli, e quindi

$$
\begin{array}{r l} E [ X _ {i} X _ {j} ] & = P \{X _ {i} X _ {j} = 1 \} \\ & = P \{X _ {i} = 1, X _ {j} = 1 \} \\ & = \frac {N (N - 1)}{(N + M) (N + M - 1)} \quad \text { from   Equation   5.3.3 } \end{array}\tag{5.3.7}
$$

Quindi dall'Equazione 5.3.2 e da quanto sopra vediamo che per $i \neq j ,$

$$
\begin{array}{r} \mathrm{Cov} (X _ {i}, X _ {j}) = \frac {N (N - 1)}{(N + M) (N + M - 1)} - \left(\frac {N}{N + M}\right) ^ {2} \\ = \frac {- N M}{(N + M) ^ {2} (N + M - 1)} \end{array}
$$

Pertanto, poiché ci sono $\textstyle { \binom { n } { 2 } }$ termini nella seconda somma sul lato destro dell'Equazione 5.3.5, otteniamo dall'Equazione 5.3.6

$$
\begin{array}{c} \operatorname{Var} (X) = \frac {n N M}{(N + M) ^ {2}} - \frac {n (n - 1) N M}{(N + M) ^ {2} (N + M - 1)} \\ = \frac {n N M}{(N + M) ^ {2}} \left(1 - \frac {n - 1}{N + M - 1}\right) \end{array}\tag{5.3.8}
$$

Se poniamo $ p = N / ( N + M )$ come la proporzione di batterie nel contenitore che sono accettabili, possiamo riscrivere le Equazioni 5.3.4 e 5.3.8 come segue.

$$
\begin{array}{c} {E (X) = n p} \\ {\mathrm{Var} (X) = n p (1 - p) \left[ 1 - \frac {n - 1}{N + M - 1} \right]} \end{array}
$$

Si noti che, per un ${ \boldsymbol { p } } ,$ fisso mentre $N + M$ aumenta a ∞, $\mathrm { V a r } ( X )$ converge a $n p ( 1 - p )$, che è la varianza di una variabile casuale binomiale con parametri $( n , p )$ (Perché ci si aspettava questo?)

ESEMPIO 5.3b Un numero sconosciuto, diciamo $N ,$ di animali abita una certa regione. Per ottenere alcune informazioni sulla dimensione della popolazione, gli ecologisti eseguono spesso il seguente esperimento: catturano prima un numero, diciamo $r ,$ di questi animali, li segnano in qualche modo e li rilasciano. Dopo aver permesso agli animali marcati il tempo di disperdersi in tutta la regione, viene effettuata una nuova cattura di dimensione, diciamo, n. Poniamo X come il numero di animali marcati in questa seconda cattura. Se assumiamo che la popolazione di animali nella regione sia rimasta fissa tra il momento delle due catture e che ogni volta che un animale veniva catturato fosse ugualmente probabile che fosse qualsiasi degli animali rimanenti non catturati, ne consegue che X è una variabile casuale ipergeometrica tale che

$$
P \{X = i \} = \frac {\binom {r} {i} \binom {N - r} {n - i}}{\binom {N} {n}} \equiv P _ {i} (N)
$$

Supponiamo ora che X sia osservato uguale a i. Cioè, la frazione $i/n$ degli animali nella seconda cattura era contrassegnata. Prendendo questo come un'approssimazione di $r/N$, la proporzione di animali nella regione che sono contrassegnati, otteniamo la stima $rn/i$ del numero di animali nella regione. Ad esempio, se inizialmente vengono catturati, contrassegnati e poi rilasciati $r = 5 0$ animali, e una successiva cattura di $n = 1 0 0$ animali rivela $X = 2 5$ di essi che erano contrassegnati, allora stimeremmo il numero di animali nella regione a circa 200. ■

Esiste una relazione tra variabili casuali binomiali e la distribuzione ipergeometrica che ci sarà utile nello sviluppo di un test statistico riguardante due popolazioni binomiali.

EXAMPLE 5.3c Siano X e Y variabili casuali binomiali indipendenti aventi rispettivi parametri $( n , p )$ e $( m , p )$. La funzione di massa di probabilità condizionata di X dato che $X + Y = k$ è la seguente.

$$
\begin{array}{l} P \{X = i | X + Y = k \} = \frac {P \{X = i , X + Y = k \}}{P \{X + Y = k \}} \\ \qquad = \frac {P \{X = i , Y = k - i \}}{P \{X + Y = k \}} \\ \qquad = \frac {P \{X = i \} P \{Y = k - i \}}{P \{X + Y = k \}} \\ \qquad = \frac {\binom {n} {i} p ^ {i} (1 - p) ^ {n - i} \binom {m} {k - i} p ^ {k - i} (1 - p) ^ {m - (k - i)}}{\binom {n + m} {k} p ^ {k} (1 - p) ^ {n + m - k}} \\ \qquad = \frac {\binom {n} {i} \binom {m} {k - i}}{\binom {n + m} {k}} \end{array}
$$

dove l'uguaglianza penultima ha utilizzato il fatto che $X + Y$ è binomiale con parametri $( n + m , p )$. Di conseguenza, vediamo che la distribuzione condizionata di X dato il valore di $X + Y$ è ipergeometrica.

Vale la pena notare che quanto sopra è piuttosto intuitivo. Supponiamo che vengano eseguiti $n + m$ tentativi indipendenti, ciascuno dei quali ha la stessa probabilità di essere un successo; sia X il numero di successi nei primi n tentativi, e sia Y il numero di successi negli ultimi m tentativi. Dato un totale di k successi nei $n + m$ tentativi, è piuttosto intuitivo che ogni sottogruppo di $k$ tentativi abbia la stessa probabilità di consistere in quei tentativi che hanno prodotto successi. Cioè, i k tentativi di successo sono distribuiti come una selezione casuale di k dei $n + m$ tentativi, e quindi il numero di quelli provenienti dai primi n tentativi è ipergeometrico. ■

## 5.4 LA VARIABILE CASUALE UNIFORME

Si dice che una variabile casuale X è distribuita uniformemente sull'intervallo $[ \alpha , \beta ]$ se la sua funzione di densità di probabilità è data da

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{\beta - \alpha} & \text { if } \alpha \leq x \leq \beta \\ 0 & \text { otherwise } \end{array} \right.
$$

Un grafico di questa funzione è riportato nella Figura 5.4. Si noti che quanto sopra soddisfa i requisiti per essere una funzione di densità di probabilità poiché

$$
\frac {1}{\beta - \alpha} \int_ {\alpha} ^ {\beta} d x = 1
$$

La distribuzione uniforme emerge nella pratica quando supponiamo che una certa variabile casuale abbia la stessa probabilità di trovarsi vicino a qualsiasi valore nell'intervallo $[ \alpha , \beta ]$ 

La probabilità che X si trovi in qualsiasi sottointervallo di $[ \alpha , \beta ]$ è uguale alla lunghezza di quel sottointervallo divisa per la lunghezza dell'intervallo $[ \alpha , \beta ]$. Ciò deriva dal fatto che quando $[ a , \ b ]$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/4d1e9a34841b6c1eede31a835566690337c565714db16fa79a6523d582139589.jpg)



FIGURA 5.4 Grafico di f (x) per una uniforme [α, β].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/97a977f1d044c78b50fbc6f89bd2e5eed1929b318da0217ce9c2be8079784cf6.jpg)



FIGURA 5.5 Probabilità di una variabile casuale uniforme.


è un sottointervallo di $[ \alpha , \beta ]$ (si veda la Figura 5.5), 

$$
\begin{array}{c} {P \{a <   X <   b \} = \frac {1}{\beta - \alpha} \int_ {a} ^ {b} d x} \\ {= \frac {b - a}{\beta - \alpha}} \end{array}
$$

ESEMPIO 5.4a Se X è distribuita uniformemente sull'intervallo [0, 10], calcola la probabilità che (a) $2 < X < 9 .$ , (b) 1 < X < 4, (c) X < 5, (d) X > 6. 

SOLUZIONE Le rispettive risposte sono (a) 7/10, (b) 3/10, (c) 5/10, (d) 4/10. ■ 

ESEMPIO 5.4b Gli autobus arrivano a una fermata specificata a intervalli di 15 minuti a partire dalle 7:00. Ovvero, arrivano alle 7:00, 7:15, 7:30, 7:45 e così via. Se un passeggero arriva alla fermata in un momento distribuito uniformemente tra le 7:00 e le 7:30, trova la probabilità che aspetti

(a) meno di 5 minuti per un autobus; 

(b) almeno 12 minuti per un autobus. 

SOLUZIONE Sia X il tempo in minuti dopo le 7:00 in cui il passeggero arriva alla fermata. Poiché X è una variabile casuale uniforme sull'intervallo (0, 30), ne consegue che il passeggero dovrà attendere meno di 5 minuti se arriva tra le 7:10 e le 7:15 o tra le 7:25 e le 7:30. Pertanto, la probabilità desiderata per (a) è

$$
P \{1 0 <   X <   1 5 \} + P \{2 5 <   X <   3 0 \} = \frac {5}{3 0} + \frac {5}{3 0} = \frac {1}{3}
$$

Allo stesso modo, dovrebbe attendere almeno 12 minuti se arriva tra le 7:00 e le 7:03 o tra le 7:15 e le 7:18, e quindi la probabilità per (b) è

$$
P \{0 <   X <   3 \} + P \{1 5 <   X <   1 8 \} = \frac {3}{3 0} + \frac {3}{3 0} = \frac {1}{5}
$$

La media di una variabile casuale uniforme $[ \alpha , \beta ]$ è

$$
\begin{array}{r l} E [ X ] & = \int_ {\alpha} ^ {\beta} \frac {x}{\beta - \alpha} d x \\ & = \frac {\beta^ {2} - \alpha^ {2}}{2 (\beta - \alpha)} \\ & = \frac {(\beta - \alpha) (\beta + \alpha)}{2 (\beta - \alpha)} \end{array}
$$

o 

$$
E [ X ] = \frac {\alpha + \beta}{2}
$$

$\mathrm { O r } ,$ in altre parole, il valore atteso di una variabile casuale uniforme $[ \alpha , \beta ]$ è uguale al punto medio dell'intervallo $[ \alpha , \beta ]$, che è chiaramente ciò che ci si aspetterebbe. (Perché?) 

La varianza è calcolata come segue. 

$$
\begin{array}{r l} E [ X ^ {2} ] & = \frac {1}{\beta - \alpha} \int_ {\alpha} ^ {\beta} x ^ {2} d x \\ & = \frac {\beta^ {3} - \alpha^ {3}}{3 (\beta - \alpha)} \\ & = \frac {\beta^ {2} + \alpha \beta + \alpha^ {2}}{3} \end{array}
$$

e quindi 

$$
\begin{array}{r l} \operatorname{Var} (X) & = \frac {\beta^ {2} + \alpha \beta + \alpha^ {2}}{3} - \left(\frac {\alpha + \beta}{2}\right) ^ {2} \\ & = \frac {\alpha^ {2} + \beta^ {2} - 2 \alpha \beta}{1 2} \\ & = \frac {(\beta - \alpha) ^ {2}}{1 2} \end{array}
$$

ESEMPIO 5.4c La corrente in un diodo a semiconduttore è spesso misurata dall'equazione di Shockley

$$
I = I _ {0} (e ^ {a V} - 1)
$$

dove V è la tensione ai capi del diodo; $I _ { 0 }$ è la corrente inversa; $^ { a }$ è una costante; e I è la corrente risultante del diodo. Trova $E [ I ]$ se $a = 5 , I _ { 0 } = 1 0 ^ { - 6 }$, e V è distribuita uniformemente su (1, 3). 

SOLUZIONE 

$$
\begin{array}{r l} & E [ I ] = E [ I _ {0} (e ^ {a V} - 1) ] \\ & \quad = I _ {0} E [ e ^ {a V} - 1 ] \\ & \quad = I _ {0} (E [ e ^ {a V} ] - 1) \\ & \quad = 1 0 ^ {- 6} \int_ {1} ^ {3} e ^ {5 x} \frac {1}{2} d x - 1 0 ^ {- 6} \\ & \quad = 1 0 ^ {- 7} (e ^ {1 5} - e ^ {5}) - 1 0 ^ {- 6} \\ & \approx . 3 2 6 9 \quad \blacksquare \end{array}
$$

Il valore di una variabile casuale uniforme (0, 1) è chiamato numero casuale. La maggior parte dei sistemi informatici ha una subroutine integrata per generare (con un alto livello di approssimazione) sequenze di numeri casuali indipendenti — ad esempio, la Tabella 5.1 presenta un set di numeri casuali indipendenti generati da un personal computer IBM. I numeri casuali sono piuttosto utili in probabilità e statistica perché il loro uso consente di stimare empiricamente varie probabilità e aspettative.


TABELLA 5.1 Una Tabella di Numeri Casuali

<table><tr><td>.68587</td><td>.25848</td><td>.85227</td><td>.78724</td><td>.05302</td><td>.70712</td><td>.76552</td><td>.70326</td><td>.80402</td><td>.49479</td></tr><tr><td>.73253</td><td>.41629</td><td>.37913</td><td>.00236</td><td>.60196</td><td>.59048</td><td>.59946</td><td>.75657</td><td>.61849</td><td>.90181</td></tr><tr><td>.84448</td><td>.42477</td><td>.94829</td><td>.86678</td><td>.14030</td><td>.04072</td><td>.45580</td><td>.36833</td><td>.10783</td><td>.33199</td></tr><tr><td>.49564</td><td>.98590</td><td>.92880</td><td>.69970</td><td>.83898</td><td>.21077</td><td>.71374</td><td>.85967</td><td>.20857</td><td>.51433</td></tr><tr><td>.68304</td><td>.46922</td><td>.14218</td><td>.63014</td><td>.50116</td><td>.33569</td><td>.97793</td><td>.84637</td><td>.27681</td><td>.04354</td></tr><tr><td>.76992</td><td>.70179</td><td>.75568</td><td>.21792</td><td>.50646</td><td>.07744</td><td>.38064</td><td>.06107</td><td>.41481</td><td>.93919</td></tr><tr><td>.37604</td><td>.27772</td><td>.75615</td><td>.51157</td><td>.73821</td><td>.29928</td><td>.62603</td><td>.06259</td><td>.21552</td><td>.72977</td></tr><tr><td>.43898</td><td>.06592</td><td>.44474</td><td>.07517</td><td>.44831</td><td>.01337</td><td>.04538</td><td>.15198</td><td>.50345</td><td>.65288</td></tr><tr><td>.86039</td><td>.28645</td><td>.44931</td><td>.59203</td><td>.98254</td><td>.56697</td><td>.55897</td><td>.25109</td><td>.47585</td><td>.59524</td></tr><tr><td>.28877</td><td>.84966</td><td>.97319</td><td>.66633</td><td>.71350</td><td>.28403</td><td>.28265</td><td>.61379</td><td>.13886</td><td>.78325</td></tr><tr><td>.44973</td><td>.12332</td><td>.16649</td><td>.88908</td><td>.31019</td><td>.33358</td><td>.68401</td><td>.10177</td><td>.92873</td><td>.13065</td></tr><tr><td>.42529</td><td>.37593</td><td>.90208</td><td>.50331</td><td>.37531</td><td>.72208</td><td>.42884</td><td>.07435</td><td>.58647</td><td>.84972</td></tr><tr><td>.82004</td><td>.74696</td><td>.10136</td><td>.35971</td><td>.72014</td><td>.08345</td><td>.49366</td><td>.68501</td><td>.14135</td><td>.15718</td></tr><tr><td>.67090</td><td>.08493</td><td>.47151</td><td>.06464</td><td>.14425</td><td>.28381</td><td>.40455</td><td>.87302</td><td>.07135</td><td>.04507</td></tr><tr><td>.62825</td><td>.83809</td><td>.37425</td><td>.17693</td><td>.69327</td><td>.04144</td><td>.00924</td><td>.68246</td><td>.48573</td><td>.24647</td></tr><tr><td>.10720</td><td>.89919</td><td>.90448</td><td>.80838</td><td>.70997</td><td>.98438</td><td>.51651</td><td>.71379</td><td>.10830</td><td>.69984</td></tr><tr><td>.69854</td><td>.89270</td><td>.54348</td><td>.22658</td><td>.94233</td><td>.08889</td><td>.52655</td><td>.83351</td><td>.73627</td><td>.39018</td></tr><tr><td>.71460</td><td>.25022</td><td>.06988</td><td>.64146</td><td>.69407</td><td>.39125</td><td>.10090</td><td>.08415</td><td>.07094</td><td>.14244</td></tr><tr><td>.69040</td><td>.33461</td><td>.79399</td><td>.22664</td><td>.68810</td><td>.56303</td><td>.65947</td><td>.88951</td><td>.40180</td><td>.87943</td></tr><tr><td>.13452</td><td>.36642</td><td>.98785</td><td>.62929</td><td>.88509</td><td>.64690</td><td>.38981</td><td>.99092</td><td>.91137</td><td>.02411</td></tr><tr><td>.94232</td><td>.91117</td><td>.98610</td><td>.71605</td><td>.89560</td><td>.92921</td><td>.51481</td><td>.20016</td><td>.56769</td><td>.60462</td></tr><tr><td>.99269</td><td>.98876</td><td>.47254</td><td>.93637</td><td>.83954</td><td>.60990</td><td>.10353</td><td>.13206</td><td>.33480</td><td>.29440</td></tr><tr><td>.75323</td><td>.86974</td><td>.91355</td><td>.12780</td><td>.01906</td><td>.96412</td><td>.61320</td><td>.47629</td><td>.33890</td><td>.22099</td></tr><tr><td>.75003</td><td>.98538</td><td>.63622</td><td>.94890</td><td>.96744</td><td>.73870</td><td>.72527</td><td>.17745</td><td>.01151</td><td>.47200</td></tr></table>

Per un'illustrazione dell'uso dei numeri casuali, supponiamo che un centro medico stia pianificando di testare un nuovo farmaco progettato per ridurre i livelli di colesterolo nel sangue dei suoi utenti. Per testarne l'efficacia, il centro medico ha reclutato 1.000 volontari per essere soggetti del test. Per tenere conto della possibilità che i livelli di colesterolo nel sangue dei soggetti possano essere influenzati da fattori esterni al test (come il cambiamento delle condizioni meteorologiche), è stato deciso di dividere i volontari in 2 gruppi di dimensione 500 — un gruppo di trattamento a cui verrà somministrato il farmaco e un gruppo di controllo a cui verrà somministrato un placebo. Né ai volontari né agli amministratori del farmaco verrà detto chi appartiene a ciascun gruppo (tale test è chiamato test in doppio cieco). Resta da determinare quali dei volontari debbano essere scelti per costituire il gruppo di trattamento. Chiaramente, si vorrebbe che il gruppo di trattamento e il gruppo di controllo fossero il più simili possibile in tutti gli aspetti, ad eccezione del fatto che i membri del primo gruppo devono ricevere il farmaco mentre quelli dell'altro gruppo ricevono un placebo; così sarà possibile concludere che qualsiasi differenza nella risposta tra i gruppi sia effettivamente dovuta al farmaco. Esiste un accordo generale sul fatto che il modo migliore per ottenere questo sia scegliere i 500 volontari per il gruppo di trattamento in modo completamente casuale. Ovvero, la scelta dovrebbe essere fatta in modo che ciascuno dei $\dot { ( } _ { 5 0 0 } ^ { 1 0 0 0 } )$ sottoinsiemi di 500 volontari abbia la stessa probabilità di costituire il gruppo di controllo. Come può essere realizzato questo?

*EXAMPLE 5.4d Choosing a Random Subset From a set of n elements — numbered $1 , 2 , \ldots , n -$ supponiamo di voler generare un sottoinsieme casuale di dimensione k che debba essere scelto in modo tale che ciascuno dei <sup>n</sup> sottoinsiemi abbia la stessa probabilità di essere il sottoinsieme scelto. Come possiamo fare?

Per rispondere a questa domanda, lavoriamo a ritroso e supponiamo di aver effettivamente generato casualmente un tale sottoinsieme di dimensione k. Ora per ogni $j = 1 , \dotsc , n ;$ , impostiamo

$$
I _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   element   } j \text {   is   in   the   subset } \\ 0 & \text { otherwise } \end{array} \right.
$$

e calcoliamo la distribuzione condizionata di $I _ { j }$ dato $I _ { 1 } , \ldots , I _ { j - 1 }$ . Per iniziare, si noti che la probabilità che l'elemento 1 sia nel sottoinsieme di dimensione k è chiaramente k/n (che può essere vista sia notando che c'è una probabilità 1/n che l'elemento 1 sarebbe stato il j-esimo elemento scelto, $j = 1 , \dotsc , k ;$ o notando che la proporzione di risultati della selezione casuale che comporta la scelta dell'elemento 1 è $\begin{array} { r } { \left( \mathbf { \Phi } _ { 1 } ^ { 1 } \right) \left( \mathbf { \Phi } _ { k - 1 } ^ { n - 1 } \right) / \left( \mathbf { \Phi } _ { k } ^ { n } \right) = k / n ) } \end{array}$ . Pertanto, abbiamo che

$$
P \{I _ {1} = 1 \} = k / n\tag{5.4.1}
$$

Per calcolare la probabilità condizionata che l'elemento 2 sia nel sottoinsieme dato $I _ { 1 }$ , si noti che se $I _ { 1 } = 1$ , allora oltre all'elemento 1 i restanti $k - 1$ membri del sottoinsieme sarebbero stati scelti "a caso" dagli altri n − 1 elementi (nel senso che ciascuno dei sottoinsiemi di dimensione $k - 1$ dei numeri $2 , \ldots , n$ ha la stessa probabilità di essere gli altri elementi del sottoinsieme). Di conseguenza, abbiamo che

$$
P \{I _ {2} = 1 | I _ {1} = 1 \} = \frac {k - 1}{n - 1}\tag{5.4.2}
$$

Analogamente, se l'elemento 1 non è nel sottogruppo, allora i k membri del sottogruppo sarebbero stati scelti "a caso" dagli altri $n - 1$ elementi, e quindi

$$
P \{I _ {2} = 1 | I _ {1} = 0 \} = \frac {k}{n - 1}\tag{5.4.3}
$$

Dalle Equazioni 5.4.2 e 5.4.3, vediamo che

$$
P \{I _ {2} = 1 | I _ {1} \} = \frac {k - I _ {1}}{n - 1}
$$

In generale, abbiamo che

$$
P \{I _ {j} = 1 | I _ {1}, \ldots , I _ {j - 1} \} = \frac {k - \sum_ {i = 1} ^ {j - 1} I _ {i}}{n - j + 1}, \quad j = 2, \ldots , n\tag{5.4.4}
$$

La formula precedente segue poiché $\begin{array} { r } { \sum _ { i = 1 } ^ { j - 1 } I _ { i } } \end{array}$ rappresenta il numero dei primi $j - 1$ elementi inclusi nel sottoinsieme, e quindi dato $I _ { 1 } , \ldots , I _ { j - 1 }$ rimangono $k - \sum _ { i = 1 } ^ { j - 1 } I _ { i }$ elementi da selezionare dai restanti $n - ( j - 1 )$

Poiché $P \{ U < a \} = a , 0 \leq a \leq 1$ , quando U è una variabile casuale uniforme (0, 1), le Equazioni 5.4.1 e 5.4.4 portano al seguente metodo per generare un sottoinsieme casuale di dimensione k da un insieme di n elementi: ovvero, generare una sequenza di (al massimo n) numeri casuali $U _ { 1 } , U _ { 2 } , . . .$ . e impostare

$$
I _ {1} = \left\{ \begin{array}{l l} 1 & \text { if } U _ {1} <   \frac {k}{n} \\ 0 & \text { otherwise } \end{array} \right.
$$

$$
I _ {2} = \left\{ \begin{array}{l l} 1 & \text { if } U _ {2} <   \frac {k - I _ {1}}{n - 1} \\ 0 & \text { otherwise } \end{array} \right.
$$

$$
I _ {j} = \left\{ \begin{array}{l l} 1 & \text { if } U _ {j} <   \frac {k - I _ {1} - \cdots - I _ {j - 1}}{n - j + 1} \\ 0 & \text { otherwise } \end{array} \right.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/bd825c6087892ed4277daf3e33f005d20da2a786e9df87d7bce84e907e472e7f.jpg)



FIGURA 5.6 Diagramma ad albero.


Questo processo si arresta quando $I _ { 1 } + \cdot \cdot \cdot + I _ { j } = k$ e il sottoinsieme casuale consiste nei $k$ elementi il cui valore I è uguale a 1. Ovvero, ${ \cal { S } } \doteq \{ i : I _ { i } = 1 \}$ è il sottoinsieme.

Ad esempio, se $k = 2 , n = 5$, allora il diagramma ad albero della Figura 5.6 illustra la tecnica sopra descritta. Il sottoinsieme casuale $S$ è dato dalla posizione finale sull'albero. Si noti che la probabilità di finire in una qualsiasi posizione finale data è uguale a $1 / 1 0$, che può essere vista moltiplicando le probabilità di muoversi attraverso l'albero fino al punto finale desiderato. Ad esempio, la probabilità di terminare nel punto contrassegnato con $S \ = \ \{ 2 , 4 \}$ è $P \{ U _ { 1 } \ >$ $. 4 ) P \{ U _ { 2 } < . 5 \} P \{ \hat { U _ { 3 } } > \textstyle { \frac { 1 } { 3 } } \} P \{ U _ { 4 } > \textstyle { \frac { 1 } { 2 } } \} = ( . 6 ) ( . 5 ) \hat { \left( \frac { 2 } { 3 } \right) } \left( \textstyle { \frac { 1 } { 2 } } \right) = . 1$

Come indicato nel diagramma ad albero (si vedano i rami più a destra che risultano in $S = \{ 4 , 5 \} )$) possiamo smettere di generare numeri casuali quando il numero di posti rimanenti nel sottoinsieme da scegliere è uguale al numero rimanente di elementi. Ovvero, la procedura generale si arresterebbe ogni volta che $\begin{array} { r } { \sum _ { i = 1 } ^ { j } I _ { i } = k \mathrm { ~ o r ~ } \sum _ { i = 1 } ^ { j } I _ { i } = k - ( n - j ) } \end{array}$. Nel secondo caso, $S = \{ i \leq j : I _ { i } = 1 , j + 1 , \ldots , n \}$ ■

EXAMPLE 5.4e Si dice che il vettore casuale $X, Y$ ha una distribuzione uniforme sulla regione bidimensionale $R$ se la sua funzione di densità congiunta è costante per i punti in $R$, ed è 0 per i punti all'esterno di $R$. Ovvero, se

$$
f (x, y) = \left\{ \begin{array}{l l} c & \text { if } (x, y) \in R \\ 0 & \text { if   otherwise } \end{array} \right.
$$

Poiché

$$
\begin{array}{l} 1 = \int_ {R} f (x, y) d x d y \\ = \int_ {R} c d x d y \\ = c \times \text {Area of} R \end{array}
$$

segue che

$$
c = \frac {1}{\mathrm{Areaof} R}
$$

Per qualsiasi regione $A \subset R ,$

$$
\begin{array}{l} P \{(X, Y) \in A \} = \int \int_ {(x, y) \in A} f (x, y) d x d y \\ = \int \int_ {(x, y) \in A} c d x d y \\ = \frac {\text { Area   of } A}{\text { Area   of } R} \end{array}
$$

Supponiamo ora che $X, Y$ sia distribuito uniformemente sulla seguente regione rettangolare $R$:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/4d29ee76ff5246f39ef92efb22b8f828fb9c87b153f280761c7e2a5fffe29dea.jpg)


La sua funzione di densità congiunta è

$$
f (x, y) = \left\{ \begin{array}{l l} c & \text { if } 0 \leq x \leq a,   0 \leq y \leq b \\ 0 & \text { otherwise } \end{array} \right.
$$

dove $\begin{array} { r } { c = { \frac { 1 } { \mathrm { A r e a } \ o f \ r e c t a n g l e } } = { \frac { 1 } { a b } } } \end{array}$. In questo caso, $X$ e $Y$ sono variabili casuali uniformi indipendenti. Per mostrarlo, si noti che per $0 \leq x \leq a , 0 \leq y \leq b$

$$
P \{X \leq x, Y \leq y \} = c \int_ {0} ^ {x} \int_ {0} ^ {y} d y d x = \frac {x y}{a b}\tag{5.4.5}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/e9356d1795e37dc4fd15f1b4082edafc40d814a0e60460b553f4fbbfd569294c.jpg)



FIGURA 5.7 La funzione di densità normale $( a )$ con $\mu = 0 , \sigma = 1$ e (b) con arbitrari $\mu$ e $\sigma ^ { 2 }$.


Impostando prima $y = b ;$, e poi impostando $x = a ;$, nel precedente mostra che

$$
P \{X \leq x \} = \frac {x}{a}, P \{Y \leq y \} = \frac {y}{b}\tag{5.4.6}
$$

Pertanto, dalle Equazioni 5.4.5 e 5.4.6 possiamo concludere che $X$ e $Y$ sono indipendenti, con $X$ uniforme su $( 0 , a )$ e $Y$ uniforme su $( 0 , b )$ ■

## 5.5 VARIABILI CASUALI NORMALI

Si dice che una variabile casuale è distribuita normalmente con i parametri $\mu$ e $\sigma ^ { 2 }$, e scriviamo $X \sim { \mathcal { N } } ( \mu , \sigma ^ { 2 } )$, se la sua densità è

$$
f (x) = \frac {1}{\sqrt {2 \pi} \sigma} e ^ {- (x - \mu) ^ {2} / 2 \sigma^ {2}}, \qquad - \infty <   x <   \infty^ {*}
$$

La densità normale $f ( x )$ è una curva a forma di campana che è simmetrica rispetto a $\mu$ e che raggiunge il suo valore massimo di 1/σ $\sqrt { 2 \pi } \approx 0 . 3 9 9 / \sigma$ in $x = \mu$ (vedere Figura 5.7).

La distribuzione normale fu introdotta dal matematico francese Abraham de Moivre nel 1733 e da lui utilizzata per approssimare le probabilità associate a variabili casuali binomiali quando il parametro binomiale n è grande. Questo risultato fu successivamente esteso da Laplace e altri ed è ora incluso in un teorema di probabilità noto come teorema del limite centrale, che fornisce una base teorica all'osservazione empirica spesso citata secondo cui, in pratica, molti fenomeni casuali obbediscono, almeno approssimativamente, a una distribuzione di probabilità normale. Alcuni esempi di questo comportamento sono l'altezza di una persona, la velocità in qualsiasi direzione di una molecola in un gas e l'errore commesso nella misurazione di una quantità fisica.

La funzione generatrice dei momenti di una variabile casuale normale con parametri $\mu$ e $\sigma ^ { 2 }$ è derivata come segue:

$$
\begin{array}{l} \phi (t) = E [ e ^ {t X} ] \\ \quad = \frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} e ^ {t x} e ^ {- (x - \mu) ^ {2} / 2 \sigma^ {2}} d x \\ \quad = \frac {1}{\sqrt {2 \pi}} e ^ {\mu t} \int_ {- \infty} ^ {\infty} e ^ {t \sigma y} e ^ {- y ^ {2} / 2} d y \qquad \text { by   letting } y = \frac {x - \mu}{\sigma} \\ \quad = \frac {e ^ {\mu t}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \exp \left\{- \left[ \frac {y ^ {2} - 2 t \sigma y}{2} \right] \right\} d y \\ \quad = \frac {e ^ {\mu t}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \exp \left\{- \frac {(y - t \sigma) ^ {2}}{2} + \frac {t ^ {2} \sigma^ {2}}{2} \right\} d y \\ \quad = \exp \left\{\mu t + \frac {\sigma^ {2} t ^ {2}}{2} \right\} \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} e ^ {- (y - t \sigma) ^ {2} / 2} d y \\ \quad = \exp \left\{\mu t + \frac {\sigma^ {2} t ^ {2}}{2} \right\} \end{array}\tag{5.5.1}
$$

dove l'ultima uguaglianza segue poiché

$$
\frac {1}{\sqrt {2 \pi}} e ^ {- (y - t \sigma) ^ {2} / 2}
$$

è la densità di una variabile casuale normale (con parametri tσ e 1) e la sua integrale deve quindi essere uguale a 1.

Differenziando l'Equazione 5.5.1, otteniamo

$$
\begin{array}{l} \phi^ {\prime} (t) = (\mu + t \sigma^ {2}) \exp \left\{\mu t + \sigma^ {2} \frac {t ^ {2}}{2} \right\} \\ \phi^ {\prime \prime} (t) = \sigma^ {2} \exp \left\{\mu t + \sigma^ {2} \frac {t ^ {2}}{2} \right\} + \exp \left\{\mu t + \sigma^ {2} \frac {t ^ {2}}{2} \right\} (\mu + t \sigma^ {2}) ^ {2} \end{array}
$$

Pertanto,

$$
\begin{array}{c} {E [ X ] = \phi^ {\prime} (0) = \mu} \\ {E [ X ^ {2} ] = \phi^ {\prime \prime} (0) = \sigma^ {2} + \mu^ {2}} \end{array}
$$

e quindi

$$
\begin{array}{c} {E [ X ] = \mu} \\ {\mathrm{Var} (X) = E [ X ^ {2} ] - (E [ X ]) ^ {2} = \sigma^ {2}} \end{array}
$$

Così $\mu$ e $\sigma ^ { 2 }$ rappresentano rispettivamente la media e la varianza della distribuzione.

Un fatto importante sulle variabili casuali normali è che se X è normale con media $\mu$ e varianza $\sigma ^ { 2 }$, allora $Y = \alpha X + \beta$ è normale con media $\alpha \mu + \beta$ e varianza $\alpha ^ { 2 } \sigma ^ { 2 }$. Il fatto che ciò sia così può essere facilmente visto utilizzando le funzioni generatrici dei momenti come segue.

$$
\begin{array}{r l} & E [ e ^ {t (\alpha X + \beta)} ] = e ^ {t \beta} E [ e ^ {\alpha t X} ] \\ & \qquad = e ^ {t \beta} \exp \{\mu \alpha t + \sigma^ {2} (\alpha t) ^ {2} / 2 \} \quad \mathrm{fromEquation5.5.1} \\ & \qquad = \exp \{(\beta + \mu \alpha) t + \alpha^ {2} \sigma^ {2} t ^ {2} / 2 \} \end{array}
$$

Poiché l'equazione finale è la funzione generatrice dei momenti della variabile casuale normale con media $\beta + \mu \alpha$ e varianza $\alpha ^ { 2 } \bar { \sigma } ^ { 2 }$, il risultato segue.

Dal precedente segue che se $X \sim { \mathcal { N } } ( \mu , \sigma ^ { 2 } )$, allora

$$
Z = \frac {X - \mu}{\sigma}
$$

è una variabile casuale normale con media 0 e varianza 1. Tale variabile casuale $Z$ si dice avere una distribuzione normale standard, o unitaria. Sia $\Phi ( \cdot )$ la sua funzione di distribuzione. Ovvero,

$$
\Phi (x) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} e ^ {- y ^ {2} / 2} d y, \qquad - \infty <   x <   \infty
$$

Questo risultato secondo cui $Z = ( X - \mu ) / \sigma$ ha una distribuzione normale standard quando X è normale con parametri $\mu$ e $\sigma ^ { 2 }$ è piuttosto importante, poiché ci consente di scrivere tutte le affermazioni di probabilità su X in termini di probabilità per Z. Ad esempio, per ottenere $P \{ X < b \}$, notiamo che X sarà minore di b se e solo se $( X - \mu ) / \sigma$ è minore di $( b - \mu ) / \sigma$, e quindi

$$
\begin{array}{c} P \{X <   b \} = P \left\{\frac {X - \mu}{\sigma} <   \frac {b - \mu}{\sigma} \right\} \\ = \Phi \left(\frac {b - \mu}{\sigma}\right) \end{array}
$$

Allo stesso modo, per ogni $a < b _ { ; }$

$$
\begin{array}{r l} P \{a <   X <   b \} & = P \left\{\frac {a - \mu}{\sigma} <   \frac {X - \mu}{\sigma} <   \frac {b - \mu}{\sigma} \right\} \\ & = P \left\{\frac {a - \mu}{\sigma} <   Z <   \frac {b - \mu}{\sigma} \right\} \\ & = P \left\{Z <   \frac {b - \mu}{\sigma} \right\} - P \left\{Z <   \frac {a - \mu}{\sigma} \right\} \\ & = \Phi \left(\frac {b - \mu}{\sigma}\right) - \Phi \left(\frac {a - \mu}{\sigma}\right) \end{array}
$$

## 5.5 Variabili Casuali Normali

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/7e8686cc4d542af30f85ea6d4f7a0fc6d6357167d986706b3a1bd472bd68d0df.jpg)



FIGURA 5.8 Probabilità normali standard.


Ci resta da calcolare $\Phi ( x )$ . Questo è stato ottenuto tramite un'approssimazione e i risultati sono presentati nella Tabella A1 dell'Appendice, che tabula $\Phi ( x )$ (con un livello di accuratezza a 4 cifre) per un'ampia gamma di valori non negativi di x. Inoltre, il Programma 5.5a del disco di testo può essere utilizzato per ottenere (x).

Mentre la Tabella A1 tabula (x) solo per valori non negativi di x, possiamo anche ottenere $\Phi ( - x )$ dalla tabella facendo uso della simmetria (rispetto a 0) della funzione di densità di probabilità normale standard. Ovvero, per $x > 0$ , se Z rappresenta una variabile casuale normale standard, allora (vedere Figura 5.8)

$$
\begin{array}{r l} \Phi (- x) & = P \{Z <   - x \} \\ & = P \{Z > x \} \quad \text { by   symmetry } \\ & = 1 - \Phi (x) \end{array}
$$

Così, ad esempio,

$$
P \{Z <   - 1 \} = \Phi (- 1) = 1 - \Phi (1) = 1 -. 8 4 1 3 = . 1 5 8 7
$$

ESEMPIO 5.5a Se X è una variabile casuale normale con media $\mu ~ = ~ 3$ e varianza $\sigma ^ { 2 } = 1 6 ,$ trovare

(a) $P \{ X < 1 1 \}$ ;

(b) $P \{ X > - 1 \}$ ;

(c) $P \{ 2 < X < 7 \}$

SOLUZIONE

(a)

$$
\begin{array}{c} P \{X <   1 1 \} = P \left\{\frac {X - 3}{4} <   \frac {1 1 - 3}{4} \right\} \\ = \Phi (2) \\ = . 9 7 7 2 \end{array}\tag{b}
$$

$$
\begin{array}{c} P \{X > - 1 \} = P \left\{\frac {X - 3}{4} > \frac {- 1 - 3}{4} \right\} \\ = P \{Z > - 1 \} \end{array}
$$

$$
\begin{array}{l} {= P \{Z <   1 \}} \\ {= . 8 4 1 3} \end{array}\tag{c}
$$

$$
\begin{array}{r l} P \{2 <   X <   7 \} & = P \left\{\frac {2 - 3}{4} <   \frac {X - 3}{4} <   \frac {7 - 3}{4} \right\} \\ & = \Phi (1) - \Phi (- 1 / 4) \\ & = \Phi (1) - (1 - \Phi (1 / 4)) \\ & = . 8 4 1 3 +. 5 9 8 7 - 1 = . 4 4 0 0 \end{array}
$$

ESEMPIO 5.5b Supponiamo che un messaggio binario — "0" o "1" — debba essere trasmesso via cavo dalla posizione A alla posizione B. Tuttavia, i dati inviati via cavo sono soggetti a una perturbazione di rumore del canale e quindi per ridurre la possibilità di errore, il valore 2 viene inviato via cavo quando il messaggio è "1" e il valore −2 viene inviato quando il messaggio è "0". Se $x , x = \pm 2$ è il valore inviato alla posizione A, allora R, il valore ricevuto alla posizione B, è dato da $R = x + N$ , dove N è la perturbazione di rumore del canale. Quando il messaggio viene ricevuto alla posizione B, il ricevitore lo decodifica secondo la seguente regola:

$$
\begin{array}{l} \text { if } R \geq . 5, \text { then   ``1'' is concluded } \\ \text { if } R <  . 5, \text { then   ``0'' is concluded } \end{array}
$$

Poiché il rumore del canale è spesso distribuito normalmente, determineremo le probabilità di errore quando N è una variabile casuale normale standard.

Esistono due tipi di errori che possono verificarsi: uno è che il messaggio "1" possa essere erroneamente concluso come "0" e l'altro che "0" sia erroneamente concluso come "1". Il primo tipo di errore si verificherà se il messaggio è $^ { \mathfrak { s } } 1 ^ { \mathfrak { p } }$ e $2 + N < . 5$ , mentre il secondo si verificherà se il messaggio è $^ { \ast } 0 ^ { \ast }$ e $- 2 + N \ge . 5$

Pertanto,

$$
\begin{array}{r l} P \{\text {error} | \text {message is "1"} \} & = P \{N <   - 1. 5 \} \\ & = 1 - \Phi (1. 5) = . 0 6 6 8 \end{array}
$$

e

$$
\begin{array}{r l} P \{\text { error } | \text { message   is   ``0'' } \} & = P \{N > 2. 5 \} \\ & = 1 - \Phi (2. 5) = . 0 0 6 2 \end{array}
$$

ESEMPIO 5.5c La potenza W dissipata in un resistore è proporzionale al quadrato della tensione V. Ovvero,

$$
W = r V ^ {2}
$$

dove r è una costante. $\operatorname { I f } r = 3$ , e V può essere assunto (con una molto buona approssimazione) come una variabile casuale normale con media 6 e deviazione standard 1, trovare

(a) $E [ W ]$

(b) $P \{ W > 1 2 0 \}$

SOLUZIONE

(a)

$$
\begin{array}{r l} & E [ W ] = E [ 3 V ^ {2} ] \\ & \quad = 3 E [ V ^ {2} ] \\ & \quad = 3 (\mathrm{Var} [ V ] + E ^ {2} [ V ]) \\ & \quad = 3 (1 + 3 6) = 1 1 1 \end{array}
$$

(b)

$$
\begin{array}{r l} P \{W > 1 2 0 \} & = P \{3 V ^ {2} > 1 2 0 \} \\ & = P \{V > \sqrt {4 0} \} \\ & = P \{V - 6 > \sqrt {4 0} - 6 \} \\ & = P \{Z >. 3 2 4 6 \} \\ & = 1 - \Phi (. 3 2 4 6) \\ & = . 3 7 2 7 \quad \blacksquare \end{array}
$$

Un altro risultato importante è che la somma di variabili casuali normali indipendenti è anche una variabile casuale normale. Per vederlo, supponiamo che $X _ { i } , i = 1 , \dotsc , n ,$ siano indipendenti, con $X _ { i }$ normale con media $\mu _ { i }$ e varianza $\sigma _ { i } ^ { 2 }$ . La funzione generatrice dei momenti di $\sum _ { i = 1 } ^ { n } X _ { i }$ è la seguente.

$$
\begin{array}{l} E \left[ \exp \left\{t \sum_ {i = 1} ^ {n} X _ {i} \right\} \right] = E \big [ e ^ {t X _ {1}} e ^ {t X _ {2}} \dots e ^ {t X _ {n}} \big ] \\ = \prod_ {i = 1} ^ {n} E \big [ e ^ {t X _ {i}} \big ] \quad \text { by   independence } \\ = \prod_ {i = 1} ^ {n} e ^ {\mu_ {i} t + \sigma_ {i} ^ {2} t ^ {2} / 2} \\ = e ^ {\mu t + \sigma^ {2} t ^ {2} / 2} \end{array}
$$

dove

$$
\mu = \sum_ {i = 1} ^ {n} \mu_ {i}, \quad \sigma^ {2} = \sum_ {i = 1} ^ {n} \sigma_ {i} ^ {2}
$$

Pertanto, $\sum _ { i = 1 } ^ { n } X _ { i }$ ha la stessa funzione generatrice dei momenti di una variabile casuale normale avente media $\mu$ e varianza $\sigma ^ { 2 }$ . Di conseguenza, dalla corrispondenza uno-a-uno tra funzioni generatrici dei momenti e distribuzioni, possiamo concludere che $\sum _ { i = 1 } ^ { n } X _ { i }$ è normale con media $\textstyle \sum _ { i = 1 } ^ { n } \mu _ { i }$ e varianza $\textstyle \sum _ { i = 1 } ^ { n } \sigma _ { i } ^ { 2 }$

ESEMPIO 5.5d I dati della National Oceanic and Atmospheric Administration indicano che le precipitazioni annuali a Los Angeles sono una variabile casuale normale con una media di 12,08 pollici e una deviazione standard di 3,1 pollici.

(a) Trovare la probabilità che le precipitazioni totali durante i prossimi 2 anni supereranno i 25 pollici.

(b) Trovare la probabilità che le precipitazioni del prossimo anno superino quelle dell'anno successivo di più di 3 pollici.

Assumere che i totali delle precipitazioni per i prossimi 2 anni siano indipendenti.

SOLUZIONE Sia $X _ { 1 }$ e $X _ { 2 }$ i totali delle precipitazioni per i prossimi 2 anni.

(a) Poiché $X _ { 1 } + X _ { 2 }$ è normale con media 24,16 e varianza $2 ( 3 . 1 ) ^ { 2 } = 1 9 . 2 2$, ne consegue che

$$
\begin{array}{r l} P \{X _ {1} + X _ {2} > 2 5 \} & = P \left\{\frac {X _ {1} + X _ {2} - 2 4 . 1 6}{\sqrt {1 9 . 2 2}} > \frac {2 5 - 2 4 . 1 6}{\sqrt {1 9 . 2 2}} \right\} \\ & = P \{Z >. 1 9 1 6 \} \\ & \approx . 4 2 4 0 \end{array}
$$

(b) Poiché $- X _ { 2 }$ è una variabile casuale normale con media −12,08 e varianza $( - 1 ) ^ { 2 } ( 3 . 1 ) ^ { 2 }$, ne consegue che $X _ { 1 } - X _ { 2 }$ è normale con media 0 e varianza 19,22. Pertanto,

$$
\begin{array}{r l} P \{X _ {1} > X _ {2} + 3 \} & = P \{X _ {1} - X _ {2} > 3 \} \\ & = P \left\{\frac {X _ {1} - X _ {2}}{\sqrt {1 9 . 2 2}} > \frac {3}{\sqrt {1 9 . 2 2}} \right\} \\ & = P \{Z >. 6 8 4 3 \} \\ & \approx . 2 4 6 9 \end{array}
$$

Così, c'è una probabilità del 42,4 percento che il totale delle precipitazioni a Los Angeles durante i prossimi 2 anni superi i 25 pollici, e c'è una probabilità del 24,69 percento che le precipitazioni del prossimo anno superino quelle dell'anno successivo di più di 3 pollici. ■

Per $\alpha \in ( 0 , 1 )$, sia ${ z } _ { \alpha }$ tale che

$$
P \{Z > z _ {\alpha} \} = 1 - \Phi (z _ {\alpha}) = \alpha
$$

Ovvero, la probabilità che una variabile casuale normale standard sia maggiore di $z _ { \alpha }$ è uguale a α (vedere Figura 5.9.)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/21186f20f3756c61f29db59e0da56e21ae44525ef85bb7e4dd4eb4c31128f67d.jpg)



FIGURA 5.9 $P \{ Z > z _ { \alpha } \} = \alpha .$


Il valore di $z _ { \alpha }$ può, per qualsiasi α, essere ottenuto dalla Tabella A1. Ad esempio, poiché

$$
\begin{array}{r l} & 1 - \Phi (1. 6 4 5) = . 0 5 \\ & 1 - \Phi (1. 9 6) = . 0 2 5 \\ & 1 - \Phi (2. 3 3) = . 0 1 \end{array}
$$

ne consegue che

$$
z _ {. 0 5} = 1. 6 4 5, \qquad z _ {. 0 2 5} = 1. 9 6, \qquad z _ {. 0 1} = 2. 3 3
$$

Il Programma 5.5b sul disco di testo può anche essere utilizzato per ottenere il valore di $z _ { \alpha }$. Poiché

$$
P \{Z <   z _ {\alpha} \} = 1 - \alpha
$$

ne consegue che per il 100(1 − α) percento delle volte una variabile casuale normale standard sarà minore di ${ z } _ { \alpha }$. Di conseguenza, chiamiamo ${ z } _ { \alpha }$ il percentile $1 0 0 ( 1 - \alpha )$ della distribuzione normale standard.

## 5.6 VARIABILI CASUALI ESPONENZIALI

Una variabile casuale continua la cui funzione di densità di probabilità è data, per alcuni $\lambda > 0$, da

$$
f (x) = \left\{ \begin{array}{l l} \lambda e ^ {- \lambda x} & \text {if} x \geq 0 \\ 0 & \text {if} x <   0 \end{array} \right.
$$

si dice essere una variabile casuale esponenziale (o, più semplicemente, si dice che è distribuita esponenzialmente) con parametro λ. La funzione di distribuzione cumulata $F ( x )$ di una variabile casuale esponenziale è data da

$$
\begin{array}{l} F (x) = P \{X \leq x \} \\ = \int_ {0} ^ {x} \lambda e ^ {- \lambda y} d y \\ = 1 - e ^ {- \lambda x}, \qquad x \geq 0 \end{array}
$$

La distribuzione esponenziale sorge spesso, in pratica, come la distribuzione della quantità di tempo fino a quando si verifica un evento specifico. Ad esempio, la quantità di tempo (a partire da ora) fino a quando si verifica un terremoto, o fino a quando scoppia una nuova guerra, o fino a quando una chiamata telefonica che si riceve si rivela essere un numero errato sono tutte variabili casuali che tendono in pratica ad avere distribuzioni esponenziali (vedere la Sezione 5.6.1 per una spiegazione).

La funzione generatrice dei momenti dell'esponenziale è data da

$$
\begin{array}{r l} & {\phi (t) = E [ e ^ {t X} ]} \\ & {\qquad = \int_ {0} ^ {\infty} e ^ {t x} \lambda e ^ {- \lambda x} d x} \\ & {\qquad = \lambda \int_ {0} ^ {\infty} e ^ {- (\lambda - t) x} d x} \\ & {\qquad = \frac {\lambda}{\lambda - t}, \qquad t <   \lambda} \end{array}
$$

La derivazione produce

$$
\begin{array}{r} \phi^ {\prime} (t) = \frac {\lambda}{(\lambda - t) ^ {2}} \\ \phi^ {\prime \prime} (t) = \frac {2 \lambda}{(\lambda - t) ^ {3}} \end{array}
$$

e quindi

$$
\begin{array}{c} {E [ X ] = \phi^ {\prime} (0) = 1 / \lambda} \\ {\mathrm{Var} (X) = \phi^ {\prime \prime} (0) - (E [ X ]) ^ {2}} \\ {= 2 / \lambda^ {2} - 1 / \lambda^ {2}} \\ {= 1 / \lambda^ {2}} \end{array}
$$

Pertanto λ è il reciproco della media, e la varianza è uguale al quadrato della media.

La proprietà chiave di una variabile casuale esponenziale è che essa è priva di memoria (memoryless), dove diciamo che una variabile casuale non negativa X è priva di memoria se

$$
P \{X > s + t | X > t \} = P \{X > s \} \quad \text {   for   all   } s, t \geq 0\tag{5.6.1}
$$

Per capire perché l'Equazione 5.6.1 è chiamata proprietà priva di memoria, immaginiamo che X rappresenti la durata del tempo in cui un certo articolo funziona prima di guastarsi. Ora consideriamo la probabilità che un articolo che è ancora funzionante all'età t continuerà a funzionare per almeno un tempo aggiuntivo s. Poiché questo sarà il caso se la durata totale di funzionamento dell'articolo supera $t + s$ dato che l'articolo è ancora funzionante a t, vediamo che

$$
\begin{array}{r l} & P \{\text { additional   functional   life   of } t \text {-unit - old   item   exceeds } s \} \\ & = P \{X > t + s | X > t \} \end{array}
$$

Così, vediamo che l'Equazione 5.6.1 afferma che la distribuzione della vita funzionale aggiuntiva di un articolo di età t è la stessa di un nuovo articolo — in altre parole, quando l'Equazione 5.6.1 è soddisfatta, non c'è bisogno di ricordare l'età di un articolo funzionante poiché finché è ancora funzionante è "come nuovo".

La condizione nell'Equazione 5.6.1 è equivalente a

$$
\frac {P \{X > s + t , X > t \}}{P \{X > t \}} = P \{X > s \}
$$

o

$$
P \{X > s + t \} = P \{X > s \} P \{X > t \}\tag{5.6.2}
$$

Quando X è una variabile casuale esponenziale, allora

$$
P \{X > x \} = e ^ {- \lambda x}, \qquad x > 0
$$

e quindi l'Equazione 5.6.2 è soddisfatta (poiché $e ^ { - \lambda ( s + t ) } = e ^ { - \lambda s } e ^ { - \lambda t } )$ ). Di conseguenza, le variabili casuali distribuite esponenzialmente sono prive di memoria (e infatti può essere dimostrato che esse sono le uniche variabili casuali che sono prive di memoria).

EXAMPLE 5.6a Supponiamo che il numero di miglia che un'auto può percorrere prima che la sua batteria si esaurisca sia distribuito esponenzialmente con un valore medio di 10.000 miglia. Se una persona desidera fare un viaggio di 5.000 miglia, qual è la probabilità che sarà in grado di completare il suo viaggio senza dover sostituire la batteria dell'auto? Cosa si può dire quando la distribuzione non è esponenziale?

SOLUTION Segue, dalla proprietà priva di memoria della distribuzione esponenziale, che la durata di vita rimanente (in miglia migliaia) della batteria è esponenziale con parametro $\lambda = 1 / 1 0$ . Pertanto la probabilità desiderata è

$$
\begin{array}{r l} P \{\text {remaining lifetime} > 5 \} & = 1 - F (5) \\ & = e ^ {- 5 \lambda} \\ & = e ^ {- 1 / 2} \approx . 6 0 4 \end{array}
$$

Tuttavia, se la distribuzione della durata di vita F non è esponenziale, allora la probabilità pertinente è

$$
P \{\text { lifetime } > t + 5 | \text { lifetime } > t \} = \frac {1 - F (t + 5)}{1 - F (t)}
$$

dove t è il numero di miglia che la batteria era stata utilizzata prima dell'inizio del viaggio. Pertanto, se la distribuzione non è esponenziale, sono necessarie informazioni aggiuntive (ovvero, t) prima che la probabilità desiderata possa essere calcolata. ■

Per un'altra illustrazione della proprietà priva di memoria, considerare il seguente esempio.

Esempio 5.6b Una squadra di lavoratori dispone di 3 macchine intercambiabili, di cui 2 devono essere funzionanti affinché la squadra possa svolgere il proprio lavoro. Quando in uso, ogni macchina funzionerà per un tempo distribuito esponenzialmente con parametro $\lambda$ prima di guastarsi. I lavoratori decidono inizialmente di utilizzare le macchine A e B e di tenere la macchina C in riserva per sostituire quella di A o B che si guasta per prima. Saranno quindi in grado di continuare a lavorare fino a quando una delle macchine rimanenti non si guasterà. Quando la squadra è costretta a interrompere il lavoro perché solo una delle macchine non si è ancora guastata, qual è la probabilità che la macchina ancora operativa sia la macchina C?

SOLUZIONE Questa domanda può essere facilmente risposta, senza alcuna necessità di calcoli, invocando la proprietà di assenza di memoria della distribuzione esponenziale. L'argomentazione è la seguente: consideriamo il momento in cui la macchina C viene messa in uso per la prima volta. In quel momento, o A o B si sono appena guastati e l'altra — chiamiamola macchina 0 — sarà ancora funzionante. Ora, anche se 0 sarebbe già stata funzionante per un certo periodo di tempo, dalla proprietà di assenza di memoria della distribuzione esponenziale, ne consegue che la sua durata di vita rimanente ha la stessa distribuzione di quella di una macchina che viene appena messa in uso. Pertanto, le durate di vita rimanenti della macchina 0 e della macchina C hanno la stessa distribuzione e quindi, per simmetria, la probabilità che 0 fallirà prima di C è $\frac { 1 } { 2 }$ . ■

La seguente proposizione presenta un'altra proprietà della distribuzione esponenziale.

PROPOSIZIONE 5.6.1 Se $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ sono variabili casuali esponenziali indipendenti con parametri rispettivi $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$, allora $\min $( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } )$$ è esponenziale con parametro $\sum _ { t = 1 } ^ { n } \lambda _ { i }$

## Dimostrazione

Poiché il valore minimo di un insieme di numeri è maggiore di $x$ se e solo se tutti i valori sono maggiori di $x$, abbiamo

$$
\begin{array}{l} P \{\min (X _ {1}, X _ {2}, \ldots , X _ {n}) > x \} = P \{X _ {1} > x, X _ {2} > x, \ldots , X _ {n} > x \} \\ = \prod_ {i = 1} ^ {n} P \{X _ {i} > x \} \quad \text { by   independence } \end{array}
$$

$$
\begin{array}{l} = \prod_ {i = 1} ^ {n} e ^ {- \lambda_ {i} x} \\ = e ^ {- \sum_ {i = 1} ^ {n} \lambda_ {i} x} \quad \square \end{array}
$$

Esempio 5.6c Un sistema in serie è un sistema che necessita di tutti i suoi componenti funzionanti affinché il sistema stesso sia funzionale. Per un sistema in serie a $n$ componenti in cui le durate di vita dei componenti sono variabili casuali esponenziali indipendenti con parametri rispettivi $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$, qual è la probabilità che il sistema sopravviva per un tempo $t ?$

SOLUZIONE Poiché la vita del sistema è uguale alla durata di vita minima dei componenti, dalla Proposizione 5.6.1 ne consegue che

$$
P \{\text { system   life   exceeds } t \} = e ^ {- \sum_ {i} \lambda_ {i} t}
$$

Un'altra proprietà utile delle variabili casuali esponenziali è che $cX$ è esponenziale con parametro $\lambda / c$ quando $X$ è esponenziale con parametro $\lambda ,$, e $c > 0$. Ciò deriva dal fatto che

$$
\begin{array}{r} P \{c X \leq x \} = P \{X \leq x / c \} \\ = 1 - e ^ {- \lambda x / c} \end{array}
$$

Il parametro $\lambda$ è chiamato tasso (rate) della distribuzione esponenziale.

## *5.6.1 Il processo di Poisson

Supponiamo che degli "eventi" si verifichino in punti temporali casuali, e sia $N(t)$ il numero di eventi che si verificano nell'intervallo di tempo $[0, t]$. Questi eventi sono detti costituire un processo di Poisson con tasso $\lambda , \lambda > 0$, se

(a) $N ( 0 ) = 0$ 

(b) Il numero di eventi che si verificano in intervalli di tempo disgiunti è indipendente. 

(c) La distribuzione del numero di eventi che si verificano in un dato intervallo dipende solo dalla lunghezza dell'intervallo e non dalla sua posizione. 

$$
\text {(d)} \lim _ {b \to 0} \frac {P \{N (b) = 1 \}}{b} = \lambda
$$

$$
\text {(e)} \lim _ {b \to 0} \frac {P \{N (b) \geq 2 \}}{b} = 0
$$

Pertanto, la Condizione (a) afferma che il processo inizia al tempo 0. La Condizione (b), l'ipotesi di incrementi indipendenti, afferma ad esempio che il numero di eventi entro il tempo $t$ [ovvero, $N ( t ) ]$ è indipendente dal numero di eventi che si verificano tra $t$ e $t + s$ [ovvero, $N ( t + s ) - N ( t ) ]$. La Condizione (c), l'ipotesi di incrementi stazionari, afferma che la distribuzione di probabilità di $N ( t + s ) - N ( t )$ è la stessa per tutti i valori di $t$. Le Condizioni (d) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/f544095cf7a49c6dd9a7b2160d65a1ba64441b04ba77dfa4b3487a5a7c9885bc.jpg)



FIGURE 5.10


e (e) affermano che in un piccolo intervallo di lunghezza $h$, la probabilità che si verifichi un evento è approssimativamente $\lambda h$, mentre la probabilità di 2 o più eventi è approssimativamente 0. 

Mostreremo ora che queste ipotesi implicano che il numero di eventi che si verificano in qualsiasi intervallo di lunghezza $t$ è una variabile casuale di Poisson con parametro $\lambda t$. Per essere precisi, chiamiamo l'intervallo $[0, t]$ e denominiamo con $N ( t )$ il numero di eventi che si verificano in quell'intervallo. Per ottenere un'espressione per $P \{ N ( t ) = k \}$, iniziamo suddividendo l'intervallo $[0, t]$ in $n$ sottointervalli non sovrapposti, ciascuno di lunghezza $t/n$ (Figura 5.10). Ora ci saranno $k$ eventi in $[0, t]$ se:

(i) $N(t)$ è uguale a $k$ e c'è al massimo un evento in ogni sottointervallo; 

(ii) $N(t)$ è uguale a $k$ e almeno uno dei sottointervalli contiene 2 o più eventi. 

Poiché queste due possibilità sono chiaramente mutuamente esclusive, e poiché la Condizione (i) è equivalente all'affermazione che $k$ dei $n$ sottointervalli contengono esattamente 1 evento e gli altri $n - k$ contengono 0 eventi, abbiamo che

$$
\begin{array}{r l} P \{N (t) = k \} & = P \{k \text {   of   the   } n \text {   subintervals   contain   exactly   1   event } \\ & \quad \text { and   the   other   } n - k \text {   contain   0   events } \} + P \{N (t) = k \\ & \quad \text { and   at   least   1   subinterval   contains   2   or   more   events } \} \end{array}\tag{5.6.3}
$$

Ora può essere dimostrato, utilizzando la Condizione (e), che

$$
\begin{array}{r l} P \{N (t) = k \text {   and   at   least   1   subinterval   contains   2   or   more   events } \} \\ & \longrightarrow 0 \text {   as   } n \to \infty \end{array}\tag{5.6.4}
$$

Inoltre, dalle Condizioni (d) e (e) segue che

$$
\begin{array}{c} P \{\text {   exactly   1   event   in   a   subinterval   } \} \approx \frac {\lambda t}{n} \\ P \{0 \text {   events   in   a   subinterval   } \} \approx 1 - \frac {\lambda t}{n} \end{array}
$$

Pertanto, poiché i numeri di eventi che si verificano in diversi sottointervalli sono indipendenti [dalla Condizione (b)], segue che

P{k dei sottointervalli contengono esattamente 1 evento e gli altri $n - k$ contengono 0 eventi} 

$$
\approx \binom {n} {k} \left(\frac {\lambda t}{n}\right) ^ {k} \left(1 - \frac {\lambda t}{n}\right) ^ {n - k}\tag{5.6.5}
$$

con l'approssimazione che diventa esatta quando il numero di sottointervalli, $n$, tende a $\infty$. Tuttavia, la probabilità nell'Equazione 5.6.5 è semplicemente la probabilità che una variabile casuale binomiale con parametri $n$ e $p = \lambda t / n$ sia uguale a $k$. Pertanto, man mano che $n$ diventa sempre più grande, questa si avvicina alla probabilità che una variabile casuale di Poisson con media $n \lambda t / n = \lambda t$ sia uguale a $k$. Di conseguenza, dalle Equazioni 5.6.3, 5.6.4 e 5.6.5, vediamo facendo tendere $n$ a $\infty$ che

$$
P \{N (t) = k \} = e ^ {- \lambda t} \frac {(\lambda t) ^ {k}}{k !}
$$

Abbiamo dimostrato: 

PROPOSIZIONE 5.6.2 Per un processo di Poisson con tasso $\lambda$ 

$$
P \{N (t) = k \} = e ^ {- \lambda t} \frac {(\lambda t) ^ {k}}{k !}, \quad k = 0, 1, \ldots
$$

Ovvero, il numero di eventi in qualsiasi intervallo di lunghezza $t$ ha una distribuzione di Poisson con media $\lambda t$ 

Per un processo di Poisson, sia $X _ { 1 }$ il tempo del primo evento. Inoltre, per $n > 1$ sia $X _ { n }$ il tempo trascorso tra $( n - 1 ) s \mathrm { t }$ e l'n-esimo evento. La sequenza $\{ X _ { n } , n = 1 , 2 , \ldots \}$ è chiamata la sequenza dei tempi di arrivo intersecanti (interarrival times). Ad esempio, se $X _ { 1 } = 5$ e $X _ { 2 } = 1 0$, allora il primo evento del processo di Poisson si sarebbe verificato al tempo 5 e il secondo al tempo 15.

Determiniamo ora la distribuzione di $X _ { n }$. Per farlo, notiamo innanzitutto che l'evento $\{ X _ { 1 } \ > \ t \}$ si verifica se e solo se non si verificano eventi del processo di Poisson nell'intervallo [0, t] e quindi,

$$
P \{X _ {1} > t \} = P \{N (t) = 0 \} = e ^ {- \lambda t}
$$

Pertanto, $X _ { 1 }$ ha una distribuzione esponenziale con media $1 / \lambda$. Per ottenere la distribuzione di $X _ { 2 }$, notiamo che

$$
\begin{array}{c} P \{X _ {2} > t | X _ {1} = s \} = P \{0 \text {   events   in   } (s, s + t ] | X _ {1} = s \} \\ = P \{0 \text {   events   in   } (s, s + t ] \} \\ = e ^ {- \lambda t} \end{array}
$$

dove le ultime due equazioni derivano da incrementi indipendenti e stazionari. Di conseguenza, dal precedente concludiamo che $X _ { 2 }$ è anche una variabile casuale esponenziale con media $1 / \lambda$, e inoltre, che $X _ { 2 }$ è indipendente da $X _ { 1 }$. Ripetendo lo stesso argomento si ottiene:

PROPOSIZIONE 5.6.3 $X _ { 1 } , X _ { 2 } , . . .$ . sono variabili casuali esponenziali indipendenti, ciascuna con media $1 / \lambda$

## *5.7 LA DISTRIBUZIONE GAMMA

Si dice che una variabile casuale ha una distribuzione gamma con parametri $( \alpha , \lambda ) , \lambda > 0$ $\alpha > 0$, se la sua funzione di densità è data da

$$
f (x) = \left\{ \begin{array}{l l} \frac {\lambda e ^ {- \lambda x} (\lambda x) ^ {\alpha - 1}}{\Gamma (\alpha)} & x \geq 0 \\ 0 & x <   0 \end{array} \right.
$$

dove

$$
\begin{array}{l} \Gamma (\alpha) = \int_ {0} ^ {\infty} \lambda e ^ {- \lambda x} (\lambda x) ^ {\alpha - 1} d x \\ = \int_ {0} ^ {\infty} e ^ {- y} y ^ {\alpha - 1} d y \quad \text {(by letting y = \lambda x)} \end{array}
$$

La formula dell'integrazione per parti  $u d \nu = u \nu - \int$ v du fornisce, con $u = y ^ { \alpha - 1 } , d \nu = e ^ { - y } d y$ $\nu = - e ^ { - y }$, che per $\alpha > 1$

$$
\begin{array}{c} \int_ {0} ^ {\infty} e ^ {- y} y ^ {\alpha - 1} d y = - e ^ {- y} y ^ {\alpha - 1} \Big | _ {y = 0} ^ {y = \infty} + \int_ {0} ^ {\infty} e ^ {- y} (\alpha - 1) y ^ {\alpha - 2} d y \\ = (\alpha - 1) \int_ {0} ^ {\infty} e ^ {- y} y ^ {\alpha - 2} d y \end{array}
$$

o

$$
\Gamma (\alpha) = (\alpha - 1) \Gamma (\alpha - 1)\tag{5.7.1}
$$

Quando α è un intero — diciamo, α = n — possiamo iterare il precedente per ottenere che

$$
\begin{array}{l l} \Gamma (n) = (n - 1) \Gamma (n - 1) \\ \quad = (n - 1) (n - 2) \Gamma (n - 2) & \text { by   letting } \alpha = n - 1 \text { in   Eq.5.7.1 } \\ \quad = (n - 1) (n - 2) (n - 3) \Gamma (n - 3) & \text { by   letting } \alpha = n - 2 \text { in   Eq.5.7.1 } \\ \vdots \\ \quad = (n - 1)! \Gamma (1) \end{array}
$$

Poiché

$$
\Gamma (1) = \int_ {0} ^ {\infty} e ^ {- y} d y = 1
$$

vediamo che

$$
\Gamma (n) = (n - 1)!
$$

La funzione $\Gamma ( \alpha )$ è chiamata funzione gamma.

Si noti che quando $\alpha = 1$, la distribuzione gamma si riduce all'esponenziale con media $1 / \lambda$

La funzione generatrice dei momenti di una variabile casuale gamma X con parametri $( \alpha , \lambda )$ si ottiene come segue:

$$
\begin{array}{l} \phi (t) = E [ e ^ {t X} ] \\ \quad = \frac {\lambda^ {\alpha}}{\Gamma (\alpha)} \int_ {0} ^ {\infty} e ^ {t x} e ^ {- \lambda x} x ^ {\alpha - 1} d x \\ \quad = \frac {\lambda^ {\alpha}}{\Gamma (\alpha)} \int_ {0} ^ {\infty} e ^ {- (\lambda - t) x} x ^ {\alpha - 1} d x \\ \quad = \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha} \frac {1}{\Gamma (\alpha)} \int_ {0} ^ {\infty} e ^ {- y} y ^ {\alpha - 1} d y \quad [ \text { by } y = (\lambda - t) x ] \\ \quad = \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha} \end{array}\tag{5.7.2}
$$

La derivazione dell'Equazione 5.7.2 fornisce

$$
\begin{array}{c} \phi^ {\prime} (t) = \frac {\alpha \lambda^ {\alpha}}{(\lambda - t) ^ {\alpha + 1}} \\ \phi^ {\prime \prime} (t) = \frac {\alpha (\alpha + 1) \lambda^ {\alpha}}{(\lambda - t) ^ {\alpha + 2}} \end{array}
$$

Pertanto,

$$
\begin{array}{c} E [ X ] = \phi^ {\prime} (0) = \frac {\alpha}{\lambda} \\ \operatorname{Var} (X) = E [ X ^ {2} ] - (E [ X ]) ^ {2} \\ = \phi^ {\prime \prime} (0) - \left(\frac {\alpha}{\lambda}\right) ^ {2} \\ = \frac {\alpha (\alpha + 1)}{\lambda^ {2}} - \frac {\alpha^ {2}}{\lambda^ {2}} = \frac {\alpha}{\lambda^ {2}} \end{array}\tag{5.7.3}
$$

(5.7.4)

Una proprietà importante della gamma è che se $X _ { 1 }$ e $X _ { 2 }$ sono variabili casuali gamma indipendenti aventi rispettivi parametri $( \alpha _ { 1 } , \lambda )$ e $( \alpha _ { 2 } , \lambda )$, allora $X _ { 1 } + X _ { 2 }$ è una variabile casuale gamma con parametri $( \alpha _ { 1 } + \alpha _ { 2 } , \lambda )$. Questo risultato segue facilmente poiché

$$
\begin{array}{r} \phi_ {X _ {1} + X _ {2}} (t) = E [ e ^ {t (X _ {1} + X _ {2})} ] \\ = \phi_ {X _ {1}} (t) \phi_ {X _ {2}} (t) \end{array}\tag{5.7.5}
$$

$$
\begin{array}{l} = \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha_ {1}} \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha_ {2}} \quad \text { from   Equation   5.7.2 } \\ = \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha_ {1} + \alpha_ {2}} \end{array}
$$

che si vede essere la funzione generatrice dei momenti di una variabile casuale gamma $( \alpha _ { 1 } + \alpha _ { 2 } , \lambda )$. Poiché una funzione generatrice dei momenti caratterizza univocamente una distribuzione, il risultato ne consegue.

Il risultato precedente si generalizza facilmente per fornire la seguente proposizione.

PROPOSIZIONE 5.7.1 Se $X _ { i } , i = 1 , \ldots , n$ sono variabili casuali gamma indipendenti con rispettivi parametri $( \alpha _ { i } , \lambda )$, allora $\sum _ { i = 1 } ^ { n } X _ { i }$ è gamma con parametri $\textstyle \sum _ { i = 1 } ^ { n } \alpha _ { i } , \lambda$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/f2d6f093d358647bfea2150453f366649c165decf9f4c2f21581fb72721ac2ce.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/271939ccec2414e7d9810692d667065edfdcb37bfb11b6326f127e6de772d055.jpg)



FIGURA 5.11 Grafici della densità gamma (α, 1) per (a) α = .5, 2, 3, 4, 5 e (b) α = 50.


Poiché la distribuzione gamma con parametri (1, λ) si riduce all'esponenziale con tasso λ, abbiamo così dimostrato il seguente risultato utile.

## Corollario 5.7.2

Se $X _ { 1 } , \ldots , X _ { n }$ sono variabili casuali esponenziali indipendenti, ciascuna avente tasso $\lambda ,$, allora $\sum _ { i = 1 } ^ { n } X _ { i }$ è una variabile casuale gamma con parametri $( n , \lambda )$

ESEMPIO 5.7a La durata della vita di una batteria è distribuita esponenzialmente con tasso λ. Se uno stereo a cassette richiede una batteria per funzionare, allora il tempo totale di riproduzione che si può ottenere da un totale di n batterie è una variabile casuale gamma con parametri $( n , \lambda )$ ■

La Figura 5.11 presenta un grafico della densità gamma (α, 1) per una varietà di valori di α. Si noti che man mano che α diventa grande, la densità inizia a somigliare alla densità normale. Questo è spiegato teoricamente dal teorema del limite centrale, che sarà presentato nel capitolo successivo.

## 5.8 DISTRIBUZIONI DERIVANTI DALLA NORMALE

## 5.8.1 La Distribuzione Chi-Quadrato

## Definizione

Se $Z _ { 1 } , Z _ { 2 } , \ldots , Z _ { n }$ sono variabili casuali normali standard indipendenti, allora X, definita da

$$
X = Z _ {1} ^ {2} + Z _ {2} ^ {2} + \dots + Z _ {n} ^ {2}\tag{5.8.1}
$$

si dice avere una distribuzione chi-quadrato con n gradi di libertà. Useremo la notazione

$$
X \sim \chi_ {n} ^ {2}
$$

per indicare che X ha una distribuzione chi-quadrato con n gradi di libertà.

La distribuzione chi-quadrato ha la proprietà additiva che se $X _ { 1 }$ e $X _ { 2 }$ sono variabili casuali chi-quadrato indipendenti con $n _ { 1 }$ e $n _ { 2 }$ gradi di libertà, rispettivamente, allora $X _ { 1 } + X _ { 2 }$ è chi-quadrato con $n _ { 1 } + n _ { 2 }$ gradi di libertà. Ciò può essere dimostrato formalmente sia mediante l'uso delle funzioni generatrici dei momenti o, più facilmente, notando che $X _ { 1 } + X _ { 2 }$ è la somma dei quadrati di $n _ { 1 } + n _ { 2 }$ normali standard indipendenti e quindi ha una distribuzione chi-quadrato con $n _ { 1 } + n _ { 2 }$ gradi di libertà.

Se X è una variabile casuale chi-quadrato con n gradi di libertà, allora per ogni $\alpha \in ( 0 , 1 )$ ), la quantità $\chi _ { \alpha , n } ^ { 2 }$ è definita in modo tale che

$$
P \{X \geq \chi_ {\alpha , n} ^ {2} \} = \alpha
$$

Questo è illustrato nella Figura 5.12.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/dbe728258b553b28165702ac84d80f4b59096faaa5ab4a41375a84c7198d0e73.jpg)



FIGURA 5.12 La funzione di densità chi-quadrato con 8 gradi di libertà.


Nella Tabella A2 dell'Appendice, elenciamo $\chi _ { \alpha , n } ^ { 2 }$ per una varietà di valori di α e n (inclusi tutti quelli necessari per risolvere i problemi ed esempi in questo testo). Inoltre, i Programmi 5.8.1a e 5.8.1b sul disco del testo possono essere utilizzati per ottenere le probabilità chi-quadrato e i valori di $\chi _ { \alpha , n } ^ { 2 } .$

EXAMPLE 5.8a Determina $P \{ \chi _ { 2 6 } ^ { 2 } \leq 3 0 \}$ quando $\chi _ { 2 6 } ^ { 2 }$ è una variabile casuale chi-quadrato con 26 gradi di libertà.

SOLUTION L'uso del Programma 5.8.1a fornisce il risultato

$$
P \{\chi_ {2 6} ^ {2} \leq 3 0 \} = . 7 3 2 5
$$

EXAMPLE 5.8b Trova $\chi _ { . 0 5 , 1 5 } ^ { 2 }$

SOLUTION Usa il Programma 5.8.1b per ottenere:

$$
\chi_ {. 0 5, 1 5} ^ {2} = 2 4. 9 9 6 \quad \blacksquare
$$

EXAMPLE 5.8c Supponiamo di tentare di localizzare un bersaglio in uno spazio tridimensionale, e che i tre errori di coordinata (in metri) del punto scelto siano variabili casuali normali indipendenti con media 0 e deviazione standard 2. Trova la probabilità che la distanza tra il punto scelto e il bersaglio superi i 3 metri.

SOLUTION Se D è la distanza, allora

$$
D ^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2} + X _ {3} ^ {2}
$$

dove $X _ { i }$ è l'errore nella i-esima coordinata. Poiché $Z _ { i } = X _ { i } / 2 , i = 1 , 2 , 3$ , sono tutte variabili casuali normali standard, ne consegue che

$$
\begin{array}{r l} P \{D ^ {2} > 9 \} & = P \{Z _ {1} ^ {2} + Z _ {2} ^ {2} + Z _ {3} ^ {2} > 9 / 4 \} \\ & = P \{\chi_ {3} ^ {2} > 9 / 4 \} \\ & = . 5 2 2 2 \end{array}
$$

dove l'ultima uguaglianza è stata ottenuta dal Programma 5.8.1a. ■

## *5.8.1.1 LA RELAZIONE TRA VARIABILI CASUALI CHI-QUADRATO E GAMMA

Calcoliamo la funzione generatrice dei momenti di una variabile casuale chi-quadrato con $n$ gradi di libertà. Per iniziare, abbiamo, quando $n = 1$, che 

$$
\begin{array}{l} E [ e ^ {t X} ] = E [ e ^ {t Z ^ {2}} ] \text {where} Z \sim \mathcal {N} (0, 1) \\ \qquad = \int_ {- \infty} ^ {\infty} e ^ {t x ^ {2}} f _ {Z} (x) d x \\ \qquad = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} e ^ {t x ^ {2}} e ^ {- x ^ {2} / 2} d x \\ \qquad = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} (1 - 2 t) / 2} d x \\ \qquad = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} / 2 \bar {\sigma} ^ {2}} d x \quad \text {where} \bar {\sigma} ^ {2} = (1 - 2 t) ^ {- 1} \\ \qquad = (1 - 2 t) ^ {- 1 / 2} \frac {1}{\sqrt {2 \pi} \bar {\sigma}} \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} / 2 \bar {\sigma} ^ {2}} d x \\ \qquad = (1 - 2 t) ^ {- 1 / 2} \end{array}\tag{5.8.2}
$$

dove l'ultima uguaglianza segue poiché l'integrale della densità normale $( 0 , \bar { \sigma } ^ { 2 } )$ è uguale a 1. Di conseguenza, nel caso generale di $n$ gradi di libertà 

$$
\begin{array}{l} E [ e ^ {t X} ] = E \left[ e ^ {t \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}} \right] \\ \qquad = E \left[ \prod_ {i = 1} ^ {n} e ^ {t Z _ {i} ^ {2}} \right] \\ \qquad = \prod_ {i = 1} ^ {n} E [ e ^ {t Z _ {i} ^ {2}} ] \quad \text { by   independence   of   the } Z _ {i} \\ \qquad = (1 - 2 t) ^ {- n / 2} \quad \text { from   Equation   5.8.2 } \end{array}
$$

Tuttavia, riconosciamo $[ 1 / ( 1 - 2 t ) ] ^ { n / 2 }$ come la funzione generatrice dei momenti di una variabile casuale gamma con parametri ($n/2$, $1/2$). Pertanto, per l'unicità delle funzioni generatrici dei momenti, ne consegue che queste due distribuzioni — chi-quadrato con $n$ gradi di libertà e gamma con parametri $_ { n / 2 }$ e $1/2$ — sono identiche, e così possiamo 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/a709b691f0bc6bc90e20882bda502c0eb4ff099e49270c000222d274e914ec31.jpg)



FIGURE 5.13 La funzione di densità chi-quadrato con $n$ gradi di libertà


concludere che la densità di $X$ è data da 

$$
f (x) = \frac {\frac {1}{2} e ^ {- x / 2} \left(\frac {x}{2}\right) ^ {(n / 2) - 1}}{\Gamma \left(\frac {n}{2}\right)}, \quad x > 0
$$

Le funzioni di densità chi-quadrato aventi rispettivamente 1, 3 e 10 gradi di libertà sono riportate nella Figura 5.13. 

Riconsideriamo l'Esempio 5.8c, questa volta supponendo che il bersaglio sia situato nel piano bidimensionale. 

EXAMPLE 5.8d Quando tentiamo di localizzare un bersaglio in uno spazio bidimensionale, supponiamo che gli errori di coordinata siano variabili casuali normali indipendenti con media 0 e deviazione standard 2. Trovare la probabilità che la distanza tra il punto scelto e il bersaglio superi 3. 

SOLUTION Se $D$ è la distanza e $X _ { i } , i = 1 , 2$ sono gli errori di coordinata, allora 

$$
D ^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2}
$$

Poiché $Z _ { i } = X _ { i } / 2 , i = 1$, 2, sono variabili casuali normali standard, otteniamo 

$$
P \{D ^ {2} > 9 \} = P \{Z _ {1} ^ {2} + Z _ {2} ^ {2} > 9 / 4 \} = P \{\chi_ {2} ^ {2} > 9 / 4 \} = e ^ {- 9 / 8} \approx . 3 2 4 7
$$

dove il calcolo precedente ha utilizzato il fatto che la distribuzione chi-quadrato con 2 gradi di libertà è la stessa della distribuzione esponenziale con parametro $1/2$. ■ 

Poiché la distribuzione chi-quadrato con $n$ gradi di libertà è identica alla distribuzione gamma con parametri $\alpha = n / 2$ e $\lambda = 1 / 2$, dalle Equazioni 5.7.3 e 5.7.4 ne consegue che la media e la varianza di una variabile casuale $X$ avente questa distribuzione sono 

$$
E [ X ] = n, \qquad \operatorname{Var} (X) = 2 n
$$

## 5.8.2 La distribuzione <sub>t</sub>

Se Z e $\chi _ { n } ^ { 2 }$ sono variabili casuali indipendenti, con Z che segue una distribuzione normale standard e $\chi _ { n } ^ { 2 }$ che segue una distribuzione chi-quadrato con n gradi di libertà, allora la variabile casuale $T _ { n }$ definita da

$$
T _ {n} = \frac {Z}{\sqrt {\chi_ {n} ^ {2} / n}}
$$

si dice avere una distribuzione t con n gradi di libertà. Un grafico della funzione di densità di $T _ { n }$ è fornito nella Figura 5.14 per $n = 1 , 5 ,$ , e 10.

Come la densità normale standard, la densità t è simmetrica rispetto a zero. Inoltre, man mano che n diventa più grande, essa diventa sempre più simile a una densità normale standard. Per capire perché, ricordiamo che $\chi _ { n } ^ { 2 }$ può essere espressa come la somma dei quadrati di n normali standard, e quindi

$$
\frac {\chi_ {n} ^ {2}}{n} = \frac {Z _ {1} ^ {2} + \cdots + Z _ {n} ^ {2}}{n}
$$

dove $Z _ { 1 } , \ldots , Z _ { n }$ sono variabili casuali normali standard indipendenti. Segue ora dalla legge debole dei grandi numeri che, per grandi $n , \ \chi _ { n } ^ { 2 } / n$ sarà, con probabilità vicina a 1, approssimativamente uguale a $E [ Z _ { i } ^ { 2 } ] = 1$ . Di conseguenza, per n grande, $T _ { n } \stackrel { \cdot } { = } Z / \sqrt { \chi _ { n } ^ { 2 } / n }$ avrà approssimativamente la stessa distribuzione di $Z$

La Figura 5.15 mostra un grafico della funzione di densità t con 5 gradi di libertà confrontato con la densità normale standard. Si noti che la densità t ha "code" più spesse, indicando una maggiore variabilità, rispetto alla densità normale.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/dcee156f28f299d9f86fefeb4f847d2c23b37b8d55468cbea9af52ba1a99e6b9.jpg)



FIGURA 5.14 Funzione di densità di T<sub>n</sub>.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/9ff37b85b1c11232d33116a455497c5a47afa221bfb3e1205607a763c2640612.jpg)



FIGURA 5.15 Confronto tra la densità normale standard e la densità $o f T _ { 5 }$


Si può dimostrare che la media e la varianza di $T _ { n }$ sono uguali a

$$
\begin{array}{c} {E [ T _ {n} ] = 0, \qquad n > 1} \\ {\mathrm{Var} (T _ {n}) = \frac {n}{n - 2}, \qquad n > 2} \end{array}
$$

Pertanto, la varianza di $T _ { n }$ diminuisce a 1 — la varianza di una variabile casuale normale standard — man mano che n aumenta a ∞. Per $\alpha , 0 < \alpha < 1$ , poniamo $t _ { \alpha , n }$ tale che

$$
P \{T _ {n} \geq t _ {\alpha , n} \} = \alpha
$$

Segue dalla simmetria rispetto a zero della funzione di densità t che $- T _ { n }$ ha la stessa distribuzione di $T _ { n } ,$ , e quindi

$$
\begin{array}{r l} & {\alpha = P \{- T _ {n} \geq t _ {\alpha , n} \}} \\ & {\quad = P \{T _ {n} \leq - t _ {\alpha , n} \}} \\ & {\quad = 1 - P \{T _ {n} > - t _ {\alpha , n} \}} \end{array}
$$

Pertanto,

$$
P \{T _ {n} \geq - t _ {\alpha , n} \} = 1 - \alpha
$$

portando alla conclusione che

$$
- t _ {\alpha , n} = t _ {1 - \alpha , n}
$$

che è illustrato nella Figura 5.16.

I valori di $t _ { \alpha , n }$ per una varietà di valori di n e α sono stati tabulati nella Tabella A3 nell'Appendice. Inoltre, i Programmi 5.8.2a e 5.8.2b sul disco del testo calcolano la funzione di distribuzione t e i valori $t _ { \alpha , n }$ , rispettivamente.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/48052340fb4d4c9da8b3f3dd80b680e4dc01fff68c3b352b03f0b19f7a3e02f9.jpg)


FIGURA 5.16 $t _ { 1 - \alpha , n } = - t _ { \alpha , n } .$ 

ESEMPIO 5.8e Trovare (a) $P \{ T _ { 1 2 } \leq 1 . 4 \}$ e (b) t<sub>.025,9</sub>.

SOLUZIONE Eseguire i Programmi 5.8.2a e 5.8.2b per ottenere i risultati.

(a) .9066 (b) 2.2625 ■

## 5.8.3 La distribuzione <sub>F</sub>

Se $\operatorname { I f } \chi _ { n } ^ { 2 }$ e $\chi _ { m } ^ { 2 }$ sono variabili casuali chi-quadrato indipendenti con n e m gradi di libertà, rispettivamente, allora la variabile casuale $F _ { n , m }$ definita da 

$$
F _ {n, m} = \frac {\chi_ {n} ^ {2} / n}{\chi_ {m} ^ {2} / m}
$$

si dice avere una distribuzione F con n e m gradi di libertà. 

Per ogni $\alpha \in ( 0 , 1 )$, sia $F _ { \alpha , n , m }$ tale che 

$$
P \{F _ {n, m} > F _ {\alpha , n, m} \} = \alpha
$$

Questo è illustrato nella Figura 5.17. 

Le quantità $F _ { \alpha , n , m }$ sono tabulate nella Tabella A4 dell'Appendice per diversi valori di n, m e $\alpha \leq \frac { 1 } { 2 }$. Se si desidera $F _ { \alpha , n , m }$ quando $\alpha > \frac { 1 } { 2 }$, può essere ottenuta utilizzando le 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/316ba6076bd80bc49a2af871cbc0f6598fd7fb0485652f93b9556cb71f4eb065.jpg)



FIGURE 5.17 Funzione di densità di F<sub>n,m</sub>.


seguenti uguaglianze: 

$$
\begin{array}{r l} & {\alpha = P \left\{\frac {\chi_ {n} ^ {2} / n}{\chi_ {m} ^ {2} / m} > F _ {\alpha , n, m} \right\}} \\ & {\qquad = P \left\{\frac {\chi_ {m} ^ {2} / m}{\chi_ {n} ^ {2} / n} <   \frac {1}{F _ {\alpha , n , m}} \right\}} \\ & {\qquad = 1 - P \left\{\frac {\chi_ {m} ^ {2} / m}{\chi_ {n} ^ {2} / n} \geq \frac {1}{F _ {\alpha , n , m}} \right\}} \end{array}
$$

o, equivalentemente, 

$$
P \left\{\frac {\chi_ {m} ^ {2} / m}{\chi_ {n} ^ {2} / n} \geq \frac {1}{F _ {\alpha , n , m}} \right\} = 1 - \alpha\tag{5.8.3}
$$

Ma poiché $( \chi _ { m } ^ { 2 } / m ) / ( \chi _ { n } ^ { 2 } / n )$ ha una distribuzione F con gradi di libertà m e n, ne consegue che 

$$
1 - \alpha = P \left\{\frac {\chi_ {m} ^ {2} / m}{\chi_ {n} ^ {2} / n} \geq F _ {1 - \alpha , m, n} \right\}
$$

implicando, dall'Equazione 5.8.3, che 

$$
\frac {1}{F _ {\alpha , n , m}} = F _ {1 - \alpha , m, n}
$$

Così, per esempio, $F _ { \cdot 9 , 5 , 7 } = 1 / F _ { \cdot 1 , 7 , 5 } = 1 / 3 . 3 7 = . 2 9 6 7$ dove il valore di $F _ { . 1 , 7 , 5 }$ è stato ottenuto dalla Tabella A4 dell'Appendice. 

Il Programma 5.8.3 calcola la funzione di distribuzione di $F _ { n , m }$ 

EXAMPLE 5.8f Determinare $P \{ F _ { 6 , 1 4 } \leq 1 . 5 \}$ 

SOLUTION Eseguire il Programma 5.8.3 per ottenere la soluzione .7518. ■ 

## *5.9 LA DISTRIBUZIONE LOGISTICA

Si dice che una variabile casuale X ha una distribuzione logistica con parametri $\mu$ e $\nu > 0$ se la sua funzione di distribuzione è 

$$
F (x) = \frac {e ^ {(x - \mu) / v}}{1 + e ^ {(x - \mu) / v}}, \qquad - \infty <   x <   \infty
$$

Differenziando $F ( x ) = 1 - 1 / ( 1 + e ^ { ( x - \mu ) / \nu } )$ si ottiene la funzione di densità 

$$
f (x) = \frac {e ^ {(x - \mu) / \nu}}{\nu (1 + e ^ {(x - \mu) / \nu}) ^ {2}}, \qquad - \infty <   x <   \infty
$$

Per ottenere la media di una variabile casuale logistica, 

$$
E [ X ] = \int_ {- \infty} ^ {\infty} x \frac {e ^ {(x - \mu) / \nu}}{\nu (1 + e ^ {(x - \mu) / \nu}) ^ {2}} d x
$$

effettuare la sostituzione $y = ( x - \mu ) / \nu$. Questo produce 

$$
\begin{array}{c} E [ X ] = \nu \int_ {- \infty} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y + \mu \int_ {- \infty} ^ {\infty} \frac {e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y \\ = \nu \int_ {- \infty} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y + \mu \end{array}\tag{5.9.1}
$$

dove l'uguaglianza precedente utilizza il fatto che $e ^ { y } / ( ( 1 + e ^ { y } ) ^ { 2 } )$ è la funzione di densità di una variabile casuale logistica con parametri $\mu = 0 , \upsilon = 1$ (una tale variabile casuale è chiamata logistica standard) e quindi si integra a 1. Ora, 

$$
\begin{array}{r l} & {\int_ {- \infty} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y = \int_ {- \infty} ^ {0} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y + \int_ {0} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y} \\ & {\qquad = - \int_ {0} ^ {\infty} \frac {x e ^ {- x}}{(1 + e ^ {- x}) ^ {2}} d x + \int_ {0} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y} \\ & {\qquad = - \int_ {0} ^ {\infty} \frac {x e ^ {x}}{(e ^ {x} + 1) ^ {2}} d x + \int_ {0} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y} \\ & {\qquad = 0} \end{array}\tag{5.9.2}
$$

dove la seconda uguaglianza è ottenuta effettuando la sostituzione $x = - y$, e la terza moltiplicando il numeratore e il denominatore per $e ^ { 2 x }$. Dalle Equazioni 5.9.1 e 5.9.2 otteniamo 

$$
E [ X ] = \mu
$$

Così $\mu$ è la media della logistica; v è chiamato parametro di dispersione.

## Problemi

1. Un sistema satellitare è composto da 4 componenti e può funzionare adeguatamente se almeno 2 delle 4 componenti sono in condizioni di funzionamento. Se ogni componente è, indipendentemente, in condizioni di funzionamento con probabilità .6, qual è la probabilità che il sistema funzioni adeguatamente? 

2. Un canale di comunicazione trasmette i digiti 0 e 1. Tuttavia, a causa delle interferenze statiche, il digito trasmesso viene ricevuto in modo errato con probabilità .2. Supponiamo di voler trasmettere un messaggio importante composto da un unico digito binario. Per ridurre la probabilità di errore, trasmettiamo 00000 invece di 0 e 11111 invece di 1. Se il ricevitore del messaggio utilizza la decodifica a "maggioranza", qual è la probabilità che il messaggio venga decodificato in modo errato? Quali assunzioni di indipendenza state facendo? (Per decodifica a maggioranza intendiamo che il messaggio viene decodificato come $^ { \mathfrak { e } } 0 ^ { \mathfrak { p } }$ se ci sono almeno tre zeri nel messaggio ricevuto e come $^ { \mathfrak { s } } 1 ^ { \mathfrak { p } }$ altrimenti.)   
 
3. Se ogni elettore vota per la Proposizione A con probabilità .7, qual è la probabilità che esattamente 7 di 10 elettori votino per questa proposizione? 
 
4. Supponiamo che un particolare tratto (come il colore degli occhi o la destrezza con la mano sinistra) di una persona sia classificato sulla base di una coppia di geni, e supponiamo che d rappresenti un gene dominante e r un gene recessivo. Pertanto, una persona con geni dd è di pura dominanza, una con rr è di pura recessività e una con rd è ibrida. La pura dominanza e l'ibrido sono simili nell'aspetto. I figli ricevono 1 gene da ciascun genitore. Se, per quanto riguarda un particolare tratto, 2 genitori ibridi hanno un totale di 4 figli, qual è la probabilità che 3 dei 4 figli abbiano l'aspetto esteriore del gene dominante? 
 
5. È richiesto che almeno la metà dei motori di un aereo funzionino affinché esso possa operare. Se ogni motore funziona indipendentemente con probabilità p, per quali valori di p un aereo a 4 motori ha maggiori probabilità di operare rispetto a un aereo a 2 motori? 
 
6. Sia X una variabile casuale binomiale con 

$$
E [ X ] = 7 \quad \mathrm{and} \quad \operatorname{Var} (X) = 2. 1
$$

Trova 

(a) $P \{ X = 4 \} ;$ 

(b) $P \{ X > 1 2 \} .$ 

7. Se X e Y sono variabili casuali binomiali con parametri rispettivi $( n , p )$ e $( n , 1 - p )$ , verifica e spiega le seguenti identità: 

(a) $P \{ X \leq i \} = P \{ Y \geq n - i \}$ ; 

(a) $P \{ X = k \} = P \{ Y = n - k \}$ 

8. Se X è una variabile casuale binomiale con parametri n e ${ \boldsymbol { p } } ,$ , dove $0 < p < 1$ mostra che 

$$
P \{X = k + 1 \} = \frac {p}{1 - p} \frac {n - k}{k + 1} P \{X = k \}, k = 0, 1, \dots , n - 1.
$$

(b) Mentre k va da 0 a $n , P \{ X = k \}$ prima aumenta e poi diminuisce, raggiungendo il suo valore massimo quando k è l'intero più grande minore o uguale a $( n + 1 ) p$ 
 
9. Deriva la funzione generatrice dei momenti di una variabile casuale binomiale e poi usa il tuo risultato per verificare le formule per la media e la varianza date nel testo. 
 
10. Confronta l'approssimazione di Poisson con la corretta probabilità binomiale per i seguenti casi: 

(a) $P \{ X = 2 \} { \mathrm { w h e n } } n = 1 0 , p = . 1 ;$ 

(b) $P \{ X = 0 \}$ quando n = 10, p = .1; 

(c) $P \{ X = 4 \}$ quando $n = 9 , p = . 2 .$ 

11. Se acquisti un biglietto della lotteria in 50 lotterie, in ciascuna delle quali la tua possibilità di vincere un premio è $\frac { 1 } { 1 0 0 }$ , qual è la probabilità (approssimativa) che vincerai un premio (a) almeno una volta, (b) esattamente una volta e (c) almeno due volte? 
 
12. Il numero di volte in cui un individuo contrae un raffreddore in un dato anno è una variabile casuale di Poisson con parametro $\lambda = 3$ . Supponiamo che un nuovo farmaco miracoloso (basato su grandi quantità di vitamina C) sia stato appena immesso sul mercato, il quale riduce il parametro di Poisson a $\lambda = 2$ per il 75 percento della popolazione. Per l'altro 25 percento della popolazione, il farmaco non ha alcun effetto apprezzabile sui raffreddori. Se un individuo prova il farmaco per un anno e ha 0 raffreddori in quel periodo, quanto è probabile che il farmaco sia benefico per lui o lei? 
 
13. Negli anni '80, in media 121,95 lavoratori morivano sul lavoro ogni settimana. Fornisci stime per le seguenti quantità:

(a) la proporzione di settimane che hanno 130 morti o più;

(b) la proporzione di settimane che hanno 100 morti o meno.

Spiega il tuo ragionamento.

14. Circa 80.000 matrimoni si sono svolti nello stato di New York lo scorso anno. Stima la probabilità che per almeno una di queste coppie

(a) entrambi i partner siano nati il 30 aprile;

(b) entrambi i partner abbiano festeggiato il proprio compleanno lo stesso giorno dell'anno.

Indica le tue ipotesi.

15. Il gioco della frustrazione solitaire si gioca girando le carte di un mazzo di 52 carte da gioco mescolate casualmente una alla volta. Prima di girare la prima carta, dì ace; prima di girare la seconda carta, dì due, prima di girare la terza carta, dì tre. Continua in questo modo (dicendo di nuovo ace prima di girare la quattordicesima carta, e così via). Perdi se giri una carta che corrisponde a ciò che hai appena detto. Usa il paradigma di Poisson per approssimare la probabilità di vincere. (La probabilità effettiva è .01623.)

16. La probabilità di errore nella trasmissione di un bit binario su un canale di comunicazione è $1 / 1 0 ^ { 3 }$. Scrivi un'espressione per la probabilità esatta di più di 3 errori quando si trasmette un blocco di $1 0 ^ { 3 }$ bit. Qual è il suo valore approssimativo? Assumi l'indipendenza.

17. Se X è una variabile casuale di Poisson con media $\lambda$, mostra che $P \{ X = i \}$ aumenta inizialmente e poi diminuisce all'aumentare di i, raggiungendo il suo valore massimo quando i è l'intero più grande minore o uguale a $\lambda$.

18. Un appaltatore acquista un carico di 100 transistor. È sua politica testarne 10 e tenere il carico solo se almeno 9 dei 10 sono in condizioni di funzionamento. Se il carico contiene 20 transistor difettosi, qual è la probabilità che venga tenuto?

19. Sia X una variabile casuale ipergeometrica con parametri n, m e k. Ovvero,

$$
P \{X = i \} = \frac {\binom {n} {i} \binom {m} {k - i}}{\binom {n + m} {k}}, \qquad i = 0, 1, \ldots , \min (k, n)
$$

(a) Deriva una formula per $P \{ X = i \}$ in termini di $P \{ X = i - 1 \}$

(b) Usa la parte (a) per calcolare $P \{ X = i \}$ per $i = { 0 , 1 , 2 , 3 , 4 , 5 }$ quando $n = m = 1 0$ $k = 5$ , partendo da $P \{ X = 0 \}$

(c) Basandoti sulla ricorsione nella parte (a), scrivi un programma per calcolare la funzione di distribuzione ipergeometrica.

(d) Usa il tuo programma della parte (c) per calcolare $P \{ X \leq 1 0 \}$ quando $n = m = 3 0$ $k = 1 5$

20. Vengono eseguiti consecutivamente prove indipendenti, ognuna delle quali è un successo con probabilità p. Sia X la prima prova che risulta in un successo. Ovvero, X sarà uguale a k se le prime $k - 1$ prove sono tutte fallimenti e la k-esima è un successo. X è chiamata una variabile casuale geometrica. Calcola

(a) $P \{ X = k \} , k = 1 , 2 , . . . ;$

(b) E[X].

Sia Y il numero di prove necessarie per ottenere r successi. Y è chiamata una variabile casuale binomiale negativa. Calcola

(c) $P \{ Y = k \} , k = r , r + 1 , \dots .$

(Suggerimento: affinché Y sia uguale a k, quanti successi devono risultare nelle prime $k - 1$ prove e quale deve essere il risultato della prova k?)

(d) Mostra che

$$
E [ Y ] = r / p
$$

(Suggerimento: Scrivi $Y = Y _ { 1 } + \dots + Y _ { r }$ dove $Y _ { i }$ è il numero di prove necessarie per passare da un totale di i − 1 a un totale di i successi.)

21. Se U è distribuita uniformemente su (0, 1), mostra che $a + ( b - a ) U$ è uniforme su $( a , b )$

22. Arrivi a una fermata dell'autobus alle 10:00, sapendo che l'autobus arriverà in un momento distribuito uniformemente tra le 10:00 e le 10:30. Qual è la probabilità che dovrai aspettare più di 10 minuti? Se alle 10:15 l'autobus non è ancora arrivato, qual è la probabilità che dovrai aspettare almeno altri 10 minuti?

23. Se X è una variabile casuale normale con parametri $\mu = 1 0 , \sigma ^ { 2 } = 3 6$ , calcola (a) $P \{ X > 5 \}$ ; (b) $P \{ 4 < X < 1 6 \}$ ; (c) $P \{ X < 8 \} ;$ (d) $P \{ X < 2 0 \} ;$ (e) $P \{ X > 1 6 \}$

24. I punteggi del test di matematica dello Scholastic Aptitude Test nella popolazione degli studenti dell'ultimo anno delle scuole superiori seguono una distribuzione normale con media 500 e deviazione standard 100. Se vengono scelti casualmente cinque studenti, trova la probabilità che (a) tutti abbiano ottenuto un punteggio inferiore a 600 e (b) esattamente tre di loro abbiano ottenuto un punteggio superiore a 640.

25. Le precipitazioni annuali (in pollici) in una determinata regione sono distribuite normalmente con $\mu = 4 0 , \sigma = 4$. Qual è la probabilità che in 2 dei prossimi 4 anni le precipitazioni superino i 50 pollici? Assumere che le precipitazioni in anni diversi siano indipendenti.

26. La larghezza di uno slot di una forgiatura in duraluminio (in pollici) è distribuita normalmente con $\mu = . 9 0 0 0$ e $\sigma = . 0 0 3 0$. I limiti di specifica sono stati forniti come $. 9 0 0 0 { \scriptstyle \pm . 0 0 5 0 }$. Quale percentuale di forgiature risulterà difettosa? Qual è il valore massimo consentito di $\sigma$ che permetterà non più di 1 difettoso su 100 quando le larghezze sono distribuite normalmente con $\mu = . 9 0 0 0$ e $\sigma = . 0 0 3 0 ?$.

27. Un certo tipo di lampadina ha un output distribuito normalmente con media 2.000 end foot candles e deviazione standard 85 end foot candles. Determina un limite di specifica inferiore L in modo che solo il 5 percento delle lampadine prodotte sia difettoso. (Ovvero, determina L in modo che $P \{ X \ge L \} = . 9 5$, dove X è l'output di una lampadina.)

28. Un produttore produce bulloni che devono avere un diametro compreso tra 1,19 e 1,21 pollici. Se il suo processo di produzione comporta un diametro del bullone distribuito normalmente con media 1,20 pollici e deviazione standard .005, quale percentuale di bulloni non rispetterà le specifiche?

29. Sia $\begin{array} { r } { I = \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } / 2 } d x } \end{array}$

(a) Mostra che per ogni $\mu$ e $\sigma$

$$
\frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} e ^ {- (x - \mu) ^ {2} / 2 \sigma^ {2}} d x = 1
$$

è equivalente a $I = \sqrt { 2 \pi }$

(b) Mostra che $I = \sqrt { 2 \pi }$ scrivendo

$$
I ^ {2} = \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} / 2} d x \int_ {- \infty} ^ {\infty} e ^ {- y ^ {2} / 2} d y = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} e ^ {- (x ^ {2} + y ^ {2}) / 2} d x d y
$$

e poi valutando l'integrale doppio mediante un cambio di variabili in coordinate polari. (Ovvero, sia $x = r \cos \theta , y = r \sin \theta , d x d y = r d r d \theta . )$

30. Si dice che una variabile casuale X ha una distribuzione lognormale se $\log X$ è distribuita normalmente. Se X è lognormale con $E [ \log X ] = \mu$ e $\mathrm { V a r } ( \log \bar { X } ) = \sigma ^ { 2 }$, determina la funzione di distribuzione di X. Ovvero, qual è $P \{ X \leq x \} \colon$

31. Le durate di vita dei chip informatici interattivi prodotti da un certo produttore di semiconduttori sono distribuite normalmente avendo una media di $4 . 4 \times 1 0 ^ { 6 }$ ore con una deviazione standard di $3 \times 1 0 ^ { 5 }$ ore. Se un produttore di mainframe richiede che almeno il 90 percento dei chip da un grande lotto abbiano durate di vita di almeno $4 . 0 \times 1 0 ^ { 6 }$ ore, dovrebbe contrattare con l'azienda di semiconduttori?

32. Nel Problema 31, qual è la probabilità che un lotto di 100 chip contenga almeno 4 le cui durate di vita siano inferiori a $3 . 8 \times 1 0 ^ { 6 }$ ore?

33. La durata di vita di un tubo della figura di una televisione a colori è una variabile casuale normale con media 8,2 anni e deviazione standard 1,4 anni. Quale percentuale di tali tubi dura

(a) più di 10 anni;

(b) meno di 5 anni;

(c) tra 5 e 10 anni?

34. Le precipitazioni annuali a Cincinnati sono distribuite normalmente con media 40,14 pollici e deviazione standard 8,7 pollici.

(a) Qual è la probabilità che le precipitazioni di quest'anno superino i 42 pollici?

(b) Qual è la probabilità che la somma delle precipitazioni dei prossimi 2 anni superi gli 84 pollici?

(c) Qual è la probabilità che la somma delle precipitazioni dei prossimi 3 anni superi i 126 pollici?

(d) Per le parti (b) e (c), quali assunzioni di indipendenza stai facendo?

35. L'altezza delle donne adulte negli Stati Uniti è distribuita normalmente con media 64,5 pollici e deviazione standard 2,4 pollici. Trova la probabilità che una donna scelta casualmente sia

(a) più bassa di 63 pollici;

(b) più bassa di 70 pollici;

(c) tra 63 e 70 pollici.

(d) Alice è alta 72 pollici. Quale percentuale di donne è più bassa di Alice?

(e) Trova la probabilità che la media delle altezze di due donne scelte casualmente superi le 66 pollici.

(f) Ripeti la parte (e) per quattro donne scelte casualmente.

36. Un test del QI produce punteggi distribuiti normalmente con valore medio 100 e deviazione standard 14,2. In quale intervallo si trova l'1 superiore di tutti i punteggi?

37. Il tempo (in ore) richiesto per riparare una macchina è una variabile casuale distribuita esponenzialmente con parametro $\lambda = 1$

(a) Qual è la probabilità che un tempo di riparazione superi le 2 ore?

(b) Qual è la probabilità condizionata che una riparazione richieda almeno 3 ore, dato che la sua durata supera le 2 ore?

38. Il numero di anni in cui funziona una radio è distribuito esponenzialmente con parametro $\begin{array} { r } { \lambda = \frac { 1 } { 8 } } \end{array}$. Se Jones acquista una radio usata, qual è la probabilità che funzionerà dopo altri 10 anni?

39. Jones calcola che il numero totale di miglia in migliaia che un'auto usata può percorrere prima di dover essere rottamata è una variabile casuale esponenziale con parametro $\frac { 1 } { 2 0 }$. Smith ha un'auto usata che sostiene essere stata percorsa solo 10.000 miglia. Se Jones acquista l'auto, qual è la probabilità che otterrà almeno 20.000 miglia aggiuntive? Ripeti sotto l'ipotesi che il chilometraggio della vita dell'auto non sia distribuito esponenzialmente ma sia (in miglia in migliaia) distribuito uniformemente su (0, 40).

*40. Siano $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ i primi n tempi di interarrivo di un processo di Poisson e sia $\begin{array} { r } { S _ { n } = \sum _ { i = 1 } ^ { n } X _ { i } } \end{array}$

(a) Qual è l'interpretazione di $S _ { n } ?$

(b) Dimostra che i due eventi $\{ S _ { n } \leq t \}$ e $\{ N ( t ) \geq n \}$ sono identici.

(c) Usa la parte (b) per mostrare che

$$
P \{S _ {n} \leq t \} = 1 - \sum_ {j = 0} ^ {n - 1} e ^ {- \lambda t} (\lambda t) ^ {j} / j!
$$

(d) Differenziando la funzione di distribuzione di $S _ { n }$ data nella parte (c), concludi che $S _ { n }$ è una variabile casuale gamma con parametri n e λ. (Questo risultato deriva anche dal Corollario 5.7.2.)

*41. I terremoti si verificano in una determinata regione in conformità con un processo di Poisson con tasso 5 all'anno.

(a) Qual è la probabilità che ci siano almeno due terremoti nella prima metà del 2010?

(b) Supponendo che l'evento nella parte (a) si verifichi, qual è la probabilità che non ci siano terremoti durante i primi 9 mesi del 2011?

(c) Supponendo che l'evento nella parte (a) si verifichi, qual è la probabilità che ci siano almeno quattro terremoti nei primi 9 mesi dell'anno 2010?

*42. Quando si spara a un bersaglio in un piano bidimensionale, supponi che la distanza di errore orizzontale sia distribuita normalmente con media 0 e varianza 4 e sia indipendente dalla distanza di errore verticale, che è anch'essa distribuita normalmente con media 0 e varianza 4. Sia D la distanza tra il punto in cui atterra il colpo e il bersaglio.

Trova $E [ D ]$

43. Se X è una variabile casuale chi-quadrato con 6 gradi di libertà, trova

(a) $P \{ X \leq 6 \} ;$

(b) $P \{ 3 \leq X \leq 9 \}$

44. Se X e Y sono variabili casuali chi-quadrato indipendenti con 3 e 6 gradi di libertà, rispettivamente, determina la probabilità che $X + Y$ superi 10.

45. Mostra che $\Gamma ( 1 / 2 ) = { \sqrt { \pi } }$ (Suggerimento: Valuta $\int _ { 0 } ^ { \infty } e ^ { - x } x ^ { - 1 / 2 }$ dx lasciando $x = y ^ { 2 } / 2$ $d x = y d y . )$

46. Se T ha una distribuzione t con 8 gradi di libertà, trova (a) $P \{ T \geq 1 \}$ (b) $P \{ T \leq 2 \}$ , e (c) $P \{ - 1 < T < 1 \}$

47. Se $T _ { n }$ ha una distribuzione t con n gradi di libertà, mostra che $T _ { n } ^ { 2 }$ ha una distribuzione F con 1 e n gradi di libertà.

48. Sia sia la funzione di distribuzione normale standard. Se, per costanti a e $b > 0$

$$
P \{X \leq x \} = \Phi \left(\frac {x - a}{b}\right)
$$

caratterizza la distribuzione di X.

# DISTRIBUZIONI DELLE STATISTICHE DI CAMPIONAMENTO

## 6.1 INTRODUZIONE

La scienza della statistica si occupa di trarre conclusioni dai dati osservati. Ad esempio, una situazione tipica in uno studio tecnologico si presenta quando ci si trova di fronte a una vasta collezione, o popolazione, di elementi che hanno valori misurabili associati ad essi. Campionando adeguatamente da questa collezione e analizzando poi gli elementi campionati, si spera di essere in grado di trarre alcune conclusioni sulla collezione nel suo insieme.

Per utilizzare i dati del campione per fare inferenze su un'intera popolazione, è necessario formulare alcune ipotesi sulla relazione tra le due. Una di queste ipotesi, che è spesso piuttosto ragionevole, è che esista una distribuzione di probabilità (di popolazione) sottostante tale per cui i valori misurabili degli elementi nella popolazione possono essere considerati come variabili casuali indipendenti aventi questa distribuzione. Se i dati del campione vengono quindi scelti in modo casuale, è ragionevole supporre che anche essi siano valori indipendenti della distribuzione.

## Definizione

Se $X _ { 1 } , \ldots , X _ { n }$ sono variabili casuali indipendenti aventi una distribuzione comune $F$, allora diciamo che esse costituiscono un campione (talvolta chiamato campione casuale) dalla distribuzione $F$.

Nella maggior parte delle applicazioni, la distribuzione della popolazione $F$ non sarà completamente specificata e si tenterà di utilizzare i dati per trarre inferenze su $F$. A volte si supporrà che $F$ sia specificata fino ad alcuni parametri ignoti (ad esempio, si potrebbe supporre che $F$ sia una funzione di distribuzione normale con media e varianza sconosciute, o che sia una funzione di distribuzione di Poisson la cui media non è data), e in altre occasioni si potrebbe assumere che quasi nulla sia noto su $F$ (tranne forse il presupposto che sia una distribuzione continua o discreta). I problemi in cui la forma della distribuzione sottostante è specificata fino a un insieme di parametri ignoti sono chiamati problemi di inferenza parametrica, mentre quelli in cui non viene assunto nulla sulla forma di $F$ sono chiamati problemi di inferenza non parametrica.

EXAMPLE 6.1a Supponiamo che sia stato appena installato un nuovo processo per produrre chip per computer, e supponiamo che i successivi chip prodotti da questo nuovo processo avranno durate utili indipendenti con una distribuzione comune sconosciuta $F .$ Ragioni fisiche a volte suggeriscono la forma parametrica della distribuzione $F ;$ ad esempio, può portarci a credere che $F$ sia una distribuzione normale, o che $F$ sia una distribuzione esponenziale. In tali casi, ci troviamo di fronte a un problema statistico parametrico in cui vorremmo utilizzare i dati osservati per stimare i parametri di $F .$ Ad esempio, se si assumesse che $F$ sia una distribuzione normale, vorremmo stimarne la media e la varianza; se si assumesse che $F$ sia esponenziale, vorremmo stimarne la media. In altre situazioni, potrebbe non esserci alcuna giustificazione fisica per supporre che $F$ abbia alcuna forma particolare; in questo caso il problema di trarre inferenze su $F$ costituirebbe un problema di inferenza non parametrica. ■

In questo capitolo, ci occuperemo delle distribuzioni di probabilità di certe statistiche che derivano da un campione, dove una statistica è una variabile casuale il cui valore è determinato dai dati del campione. Due statistiche importanti che discuteremo sono la media campionaria e la varianza campionaria. Nella Sezione 6.2, consideriamo la media campionaria e ne deriviamo l'aspettativa e la varianza. Notiamo che quando la dimensione del campione è almeno moderatamente grande, la distribuzione della media campionaria è approssimativamente normale. Ciò deriva dal teorema del limite centrale, uno dei risultati teorici più importanti in probabilità, che viene discusso nella Sezione 6.3. Nella Sezione $6 . 4 ,$, introduciamo la varianza campionaria e ne determiniamo il valore atteso. Nella Sezione 6.5, supponiamo che la distribuzione della popolazione sia normale e presentiamo la distribuzione congiunta della media campionaria e della varianza campionaria. Nella Sezione $6 . 6 ,$ supponiamo di prelevare campioni da una popolazione finita di elementi e spieghiamo cosa significhi che il campione sia un "campione casuale". Quando la dimensione della popolazione è grande in relazione alla dimensione del campione, spesso la trattiamo come se fosse di dimensione infinita; questo viene illustrato e le sue conseguenze vengono discusse.

## 6.2 LA MEDIA CAMPIONARIA

Consideriamo una popolazione di elementi, ciascuno dei quali ha un valore numerico associato. Ad esempio, la popolazione potrebbe consistere negli adulti di una determinata comunità e il valore associato a ogni adulto potrebbe essere il suo reddito annuo, o l'altezza, o l'età, e così via. Spesso supponiamo che il valore associato a qualsiasi membro della popolazione possa essere considerato come il valore di una variabile casuale avente aspettativa $\mu$ e varianza $\sigma ^ { 2 }$ . Le quantità $\mu$ e $\sigma ^ { 2 }$ sono chiamate rispettivamente media della popolazione e varianza della popolazione. Sia $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ un campione di valori da questa popolazione. La media campionaria è definita da

$$
\overline {{X}} = \frac {X _ {1} + \cdots + X _ {n}}{n}
$$

Poiché il valore della media campionaria $\overline { { X } }$ è determinato dai valori della variabile casuale nel campione, ne consegue che $\overline { { X } }$ è anche una variabile casuale. Il suo valore atteso e la sua varianza si ottengono come segue:

$$
\begin{array}{r l} & E [ \overline {{X}} ] = E \left[ \frac {X _ {1} + \cdots + X _ {n}}{n} \right] \\ & \qquad = \frac {1}{n} (E [ X _ {1} ] + \dots + E [ X _ {n} ]) \\ & \qquad = \mu \end{array}
$$

e

$$
\begin{array}{l} \operatorname{Var} (\overline {{X}}) = \operatorname{Var} \left(\frac {X _ {1} + \cdots + X _ {n}}{n}\right) \\ \qquad = \frac {1}{n ^ {2}} [ \operatorname{Var} (X _ {1}) + \dots + \operatorname{Var} (X _ {n}) ] \quad \text { by   independence } \\ \qquad = \frac {n \sigma^ {2}}{n ^ {2}} \\ \qquad = \frac {\sigma^ {2}}{n} \end{array}
$$

dove $\mu$ e $\sigma ^ { 2 }$ sono rispettivamente la media e la varianza della popolazione. Pertanto, il valore atteso della media campionaria è la media della popolazione $\mu$, mentre la sua varianza è $1 / n$ volte la varianza della popolazione. Di conseguenza, possiamo concludere che X è anche centrata attorno alla media della popolazione $\mu _ { ; }$, ma la sua dispersione diventa sempre più ridotta all'aumentare della dimensione del campione. La Figura 6.1 riporta la funzione di densità di probabilità della media campionaria da una popolazione normale standard per una varietà di dimensioni del campione.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/4914d03d97fcba5f3903a8266833452c61d67fcb38bb2ae3d6ac272f10020e02.jpg)



FIGURA 6.1 Densità delle medie campionarie da una popolazione normale standard.


## 6.3 IL TEOREMA DEL LIMITE CENTRALE

In questa sezione, considereremo uno dei risultati più notevoli della probabilità — ovvero, il teorema del limite centrale. In parole povere, questo teorema afferma che la somma di un gran numero di variabili casuali indipendenti ha una distribuzione approssimativamente normale. Pertanto, non solo fornisce un metodo semplice per calcolare le probabilità approssimate per somme di variabili casuali indipendenti, ma aiuta anche a spiegare il fatto notevole che le frequenze empiriche di così tante popolazioni naturali presentino una curva a forma di campana (ovvero, una normale).

Nella sua forma più semplice, il teorema del limite centrale è il seguente:

## Teorema 6.3.1 Il Teorema del Limite Centrale

Sia $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ una sequenza di variabili casuali indipendenti e identicamente distribuite, ciascuna con media µ e varianza $\sigma ^ { 2 }$. Allora per n grande, la distribuzione di 

$$
X _ {1} + \dots + X _ {n}
$$

è approssimativamente normale con media nµ e varianza $n \sigma ^ { 2 }$ 

Dal teorema del limite centrale segue che 

$$
\frac {X _ {1} + \cdots + X _ {n} - n \mu}{\sigma \sqrt {n}}
$$

è approssimativamente una variabile casuale normale standard; quindi, per n grande, 

$$
P \left\{\frac {X _ {1} + \cdots + X _ {n} - n \mu}{\sigma \sqrt {n}} <   x \right\} \approx P \{Z <   x \}
$$

dove Z è una variabile casuale normale standard. 

ESEMPIO 6.3a Una compagnia di assicurazioni ha 25.000 assicurati di polizze auto. Se il sinistro annuale di un assicurato è una variabile casuale con media 320 e deviazione standard 540, approssima la probabilità che il sinistro annuale totale superi gli 8,3 milioni. 

SOLUZIONE Sia X il sinistro annuale totale. Numeriamo gli assicurati e sia $X _ { i }$ il sinistro annuale dell'assicurato i. Con $n = 2 5 , 0 0 0$, abbiamo dal teorema del limite centrale che $\begin{array} { r } { X = \sum _ { i = 1 } ^ { n } X _ { i } } \end{array}$ avrà approssimativamente una distribuzione normale con media $3 2 0 \times 2 5 , 0 0 0 = 8 \times 1 0 ^ { 6 }$ e deviazione standard $5 4 0 { \sqrt { 2 5 , 0 0 0 } } = 8 . 5 3 8 1 \times 1 0 ^ { 4 }$. Pertanto, 

$$
\begin{array}{c} P \{X > 8. 3 \times 1 0 ^ {6} \} = P \left\{\frac {X - 8 \times 1 0 ^ {6}}{8 . 5 3 8 1 \times 1 0 ^ {4}} > \frac {8 . 3 \times 1 0 ^ {6} - 8 \times 1 0 ^ {6}}{8 . 5 3 8 1 \times 1 0 ^ {4}} \right\} \\ = P \left\{\frac {X - 8 \times 1 0 ^ {6}}{8 . 5 3 8 1 \times 1 0 ^ {4}} > \frac {. 3 \times 1 0 ^ {6}}{8 . 5 3 8 1 \times 1 0 ^ {4}} \right\} \end{array}
$$

$$
\begin{array}{l l} \approx P \{Z > 3. 5 1 \} & \text { where } Z \text { is   a   standard   normal } \\ \approx . 0 0 0 2 3 \end{array}
$$

Così, ci sono solo 2,3 possibilità su 10.000 che il sinistro annuale totale superi gli 8,3 milioni. ■ 

ESEMPIO 6.3b Gli ingegneri civili ritengono che W, la quantità di peso (in unità di 1.000 libbre) che una determinata campata di un ponte può sopportare senza che si verifichino danni strutturali, sia distribuita normalmente con media 400 e deviazione standard 40. Supponiamo che il peso (ancora, in unità di 1.000 libbre) di un'auto sia una variabile casuale con media 3 e deviazione standard .3. Quante auto dovrebbero trovarsi sulla campata del ponte affinché la probabilità di danni strutturali superi .1? 

SOLUZIONE Sia $P _ { n }$ la probabilità di danni strutturali quando ci sono n auto sul ponte. Ovvero, 

$$
\begin{array}{c} {P _ {n} = P \{X _ {1} + \dots + X _ {n} \geq W \}} \\ {= P \{X _ {1} + \dots + X _ {n} - W \geq 0 \}} \end{array}
$$

dove $X _ { i }$ è il peso della i-esima auto, $i = 1 , \ldots , n .$. Ora segue dal teorema del limite centrale che $\textstyle \sum _ { i = 1 } ^ { n } X _ { i }$ è approssimativamente normale con media $3 n$ e varianza .09n. Di conseguenza, poiché W è indipendente da $X _ { i } , i = 1 , \dotsc , n ,$ ed è anche normale, segue che $\textstyle \sum _ { i = 1 } ^ { n } X _ { i } - W$ è approssimativamente normale, con media e varianza date da 

$$
\begin{array}{l} E \left[ \sum_ {1} ^ {n} X _ {i} - W \right] = 3 n - 4 0 0 \\ \operatorname{Var} \left(\sum_ {1} ^ {n} X _ {i} - W\right) = \operatorname{Var} \left(\sum_ {1} ^ {n} X _ {i}\right) + \operatorname{Var} (W) = . 0 9 n + 1, 6 0 0 \end{array}
$$

Pertanto, se poniamo 

$$
Z = \frac {\sum_ {i = 1} ^ {n} X _ {i} - W - (3 n - 4 0 0)}{\sqrt {. 0 9 n + 1 , 6 0 0}}
$$

allora 

$$
P _ {n} = P \left\{Z \geq \frac {- (3 n - 4 0 0)}{\sqrt {. 0 9 n + 1 , 6 0 0}} \right\}
$$

dove $Z$ è approssimativamente una variabile casuale normale standard. Ora $P \{ Z \ge 1 . 2 8 \} \approx . 1$ e quindi se il numero di auto n è tale che 

$$
\frac {4 0 0 - 3 n}{\sqrt {. 0 9 n + 1 , 6 0 0}} \leq 1. 2 8
$$

o 

$$
n \geq 1 1 7
$$

allora c'è almeno 1 possibilità su 10 che si verifichino danni strutturali. ■ 

Il teorema del limite centrale è illustrato dal Programma 6.1 sul disco di testo. Questo programma traccia la funzione di massa di probabilità della somma di n variabili casuali indipendenti e identicamente distribuite che assumono ciascuna uno dei valori 0, 1, 2, 3, 4. Quando lo si utilizza, si inseriscono le probabilità di questi cinque valori e il valore desiderato di n. Le figure 6.2(a)–(f) mostrano il grafico risultante per un set specificato di probabilità quando $n = 1 , 3 , 5 , 1 0 , 2 5 , 1 0 0$ 

Una delle applicazioni più importanti del teorema del limite centrale riguarda le variabili casuali binomiali. Poiché una tale variabile casuale X avente parametri $( n , p )$ rappresenta il numero di successi in n prove indipendenti quando ogni prova è un successo con probabilità ${ \boldsymbol { p } } ,$ possiamo esprimerla come 

$$
X = X _ {1} + \dots + X _ {n}
$$

dove 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   trial   is   a   success } \\ 0 & \text { otherwise } \end{array} \right.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/df1add087b00aa8ea4aa2fd6a4af72a577067dedd810bf88dd37ada06147264a.jpg)



(a)



FIGURA 6.2 (a) n = 1, (b) n = 3, (c) n = 5, (d ) n = 10, (e) n = 25, ( f ) n = 100.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/1e62daf8c43226eb6fa46fdf5ea92c68d806cfab1bd97c9c38328c372775341a.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/7ae7a934eb43ec268f761e4ac39b80621b00c91fddad7797273e240598a263e0.jpg)



(c)



FIGURA 6.2 (continuazione)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/e09a03ab5f2c9165eca3cc63b48cbc182efb0ec0884f58fe944ef2cfdd404c8b.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5ace1d5a76beefcede8a8bb0e2439477fdeb82ab332b7533970e32ffb46f2737.jpg)



(e)



FIGURA 6.2 (continuazione)


(f) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/b9c56511932d7857d69d3d112714eab8ffd5ebce361a9ae4fb5b0a9a112a2c27.jpg)



FIGURA 6.2 (continuazione)


Poiché 

$$
E [ X _ {i} ] = p, \quad \operatorname{Var} (X _ {i}) = p (1 - p)
$$

dal teorema del limite centrale segue che per $n$ grande

$$
\frac {X - n p}{\sqrt {n p (1 - p)}}
$$

sarà approssimativamente una variabile casuale normale standard [si veda la Figura 6.3, che illustra graficamente come la funzione di massa di probabilità di una variabile casuale binomiale $( n , p )$ diventi sempre più "normale" man mano che $n$ diventa più grande].

EXAMPLE 6.3c La dimensione ideale di una classe del primo anno in un determinato college è di 150 studenti. Il college, sapendo dall'esperienza passata che, in media, solo il 30 percento di coloro che vengono ammessi frequenterà effettivamente, utilizza una politica di approvazione delle domande di 450 studenti. Calcolare la probabilità che più di 150 studenti del primo anno frequentino questo college.

SOLUTION Sia $X$ il numero di studenti che frequentano; assumendo che ogni candidato ammesso frequenti indipendentemente, segue che $X$ è una variabile casuale binomiale con parametri $n = 4 5 0$ e $ { p } = . 3$. Poiché la binomiale è una distribuzione discreta e la normale una distribuzione continua, è meglio calcolare $P \{ X = i \} \arg \{ i - . 5 < X < i + . 5 \}$ quando si applica l'approssimazione normale (questo è chiamato correzione di continuità). Ciò fornisce l'approssimazione

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/9e5920d005804034f91605b7f9bc82c397319e321e85dfa4bb8c5fedefe0235b.jpg)



FIGURE 6.3 Funzioni di massa di probabilità binomiali che convergono alla densità normale.


$$
\begin{array}{c} P \{X > 1 5 0. 5 \} = P \left\{\frac {X - (4 5 0) (. 3)}{\sqrt {4 5 0 (. 3) (. 7)}} \geq \frac {1 5 0 . 5 - (4 5 0) (. 3)}{\sqrt {4 5 0 (. 3) (. 7)}} \right\} \\ \approx P \{Z > 1. 5 9 \} = . 0 6 \end{array}
$$

Pertanto, solo il $^ 6$ percento delle volte più di 150 dei primi 450 accettati frequentano effettivamente. ■

Bisogna notare che ora abbiamo due possibili approssimazioni per le probabilità binomiali: l'approssimazione di Poisson, che fornisce una buona approssimazione quando $n$ è grande e $\boldsymbol { \mathit { p } }$ piccolo, e l'approssimazione normale, che può essere dimostrata essere piuttosto buona quando $n p ( 1 - p )$ è grande. [L'approssimazione normale sarà, in generale, piuttosto buona per valori di $n$ che soddisfano $n p ( 1 - p ) \geq 1 0 . ]$

## 6.3.1 Distribuzione Approssimativa della Media Campionaria

Sia $X _ { 1 } , \ldots , X _ { n }$ un campione di una popolazione avente media $\mu$ e varianza $\sigma ^ { 2 }$ . Il teorema del limite centrale può essere utilizzato per approssimare la distribuzione della media campionaria

$$
\overline {{X}} = \sum_ {i = 1} ^ {n} X _ {i} / n
$$

Poiché un multiplo costante di una variabile casuale normale è anch'esso normale, dal teorema del limite centrale segue che X sarà approssimativamente normale quando la dimensione del campione n è grande. Poiché la media campionaria ha valore atteso $\mu$ e deviazione standard $\sigma / { \sqrt { n } }$ , ne consegue che

$$
\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}}
$$

ha approssimativamente una distribuzione normale standard.

ESEMPIO 6.3d I pesi di una popolazione di lavoratori hanno media 167 e deviazione standard 27.

(a) Se viene scelto un campione di 36 lavoratori, approssima la probabilità che la media campionaria dei loro pesi si trovi tra 163 e 170.

(b) Ripeti la parte (a) quando il campione è di dimensione 144.

SOLUZIONE Sia $Z$ una variabile casuale normale standard.

(a) Dal teorema del limite centrale segue che $\overline { { X } }$ è approssimativamente normale con media 167 e deviazione standard $2 7 / \sqrt { 3 6 } = 4 . 5$ . Pertanto,

$$
\begin{array}{l} P \{1 6 3 <   \overline {{X}} <   1 7 0 \} = P \left\{\frac {1 6 3 - 1 6 7}{4 . 5} <   \frac {\overline {{X}} - 1 6 7}{4 . 5} <   \frac {1 7 0 - 1 6 7}{4 . 5} \right\} \\ = P \left\{-. 8 8 8 9 <   \frac {\overline {{X}} - 1 6 7}{4 . 5} <  . 8 8 8 9 \right\} \\ \approx 2 P \{Z <  . 8 8 8 9 \} - 1 \\ \approx . 6 2 5 9 \end{array}
$$

(b) Per un campione di dimensione 144, la media campionaria sarà approssimativamente normale con media 167 e deviazione standard $2 7 / \sqrt { 1 4 4 } = 2 . 2 5$ . Pertanto,

$$
\begin{array}{l} P \{1 6 3 <   \overline {{X}} <   1 7 0 \} = P \left\{\frac {1 6 3 - 1 6 7}{2 . 2 5} <   \frac {\overline {{X}} - 1 6 7}{2 . 2 5} <   \frac {1 7 0 - 1 6 7}{2 . 2 5} \right\} \\ \qquad = P \left\{- 1. 7 7 7 8 <   \frac {\overline {{X}} - 1 6 7}{4 . 5} <   1. 7 7 7 8 \right\} \\ \qquad \approx 2 P \{Z <   1. 7 7 7 8 \} - 1 \\ \qquad \approx . 9 2 4 6 \end{array}
$$

Pertanto, aumentare la dimensione del campione da 36 a 144 aumenta la probabilità da .6259 a .9246. ■

ESEMPIO 6.3e Un astronomo vuole misurare la distanza dal suo osservatorio a una stella lontana. Tuttavia, a causa delle perturbazioni atmosferiche, qualsiasi misurazione non fornirà la distanza esatta d. Di conseguenza, l'astronomo ha deciso di effettuare una serie di misurazioni e poi utilizzare il loro valore medio come stima della distanza effettiva. Se l'astronomo crede che i valori delle misurazioni successive siano variabili casuali indipendenti con una media di d anni luce e una deviazione standard di 2 anni luce, quante misurazioni deve effettuare per essere certo almeno al 95 percento che la sua stima sia accurata entro ± .5 anni luce?

SOLUZIONE Se l'astronomo effettua n misurazioni, allora ${ \overline { { X } } } ,$ , la media campionaria di queste misurazioni, sarà approssimativamente una variabile casuale normale con media d e deviazione standard $2 / { \sqrt { n } } .$ . Pertanto, la probabilità che essa si trovi tra $d \pm . 5$ si ottiene come segue:

$$
\begin{array}{r l r} & & P \{-. 5 <   \overline {{X}} - d <  . 5 \} = P \left\{\frac {- . 5}{2 / \sqrt {n}} <   \frac {\overline {{X}} - d}{2 / \sqrt {n}} <   \frac {. 5}{2 / \sqrt {n}} \right\} \\ & & \approx P \{- \sqrt {n} / 4 <   Z <   \sqrt {n} / 4 \} \\ & & = 2 P \{Z <   \sqrt {n} / 4 \} - 1 \end{array}
$$

dove $Z$ è una variabile casuale normale standard.

Pertanto, l'astronomo dovrebbe effettuare n misurazioni, dove n è tale che

$$
2 P \{Z <   \sqrt {n} / 4 \} - 1 \geq . 9 5
$$

o, equivalentemente,

$$
P \{Z <   \sqrt {n} / 4 \} \geq . 9 7 5
$$

Poiché $P \{ Z < 1 . 9 6 \} = . 9 7 5$ , ne consegue che n dovrebbe essere scelto in modo che

$$
\sqrt {n} / 4 \geq 1. 9 6
$$

Ciò significa che sono necessarie almeno 62 osservazioni. ■

## 6.3.2 Quanto Grande Deve Essere il Campione?

Il teorema del limite centrale lascia aperta la questione di quanto debba essere grande la dimensione del campione n affinché l'approssimazione normale sia valida, e in effetti la risposta dipende dalla distribuzione della popolazione dei dati del campione. Ad esempio, se la distribuzione della popolazione sottostante è normale, allora anche la media campionaria X sarà normale indipendentemente dalla dimensione del campione. Una regola generale è che si può essere fiduciosi dell'approssimazione normale ogni volta che la dimensione del campione n è almeno 30. Cioè, praticamente parlando, non importa quanto la distribuzione della popolazione sottostante sia non normale, la media campionaria di un campione di dimensione almeno 30 sarà approssimativamente normale. Nella maggior parte dei casi, l'approssimazione normale è valida per dimensioni del campione molto più piccole. Infatti, un campione di dimensione 5 spesso basterà affinché l'approssimazione sia valida. La Figura 6.4 presenta la distribuzione delle medie campionarie da una distribuzione di popolazione esponenziale per campioni di dimensioni $n = 1 , 5 , 1 0$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/ae7fa3269a062370e8a0296dc26c2da70a35da6c159af771c113a31137267ee7.jpg)



FIGURA 6.4 Densità della media di n variabili casuali esponenziali aventi media 1.

## 6.4 LA VARIANZA DEL CAMPIONE

Sia $X _ { 1 } , \ldots , X _ { n }$ un campione casuale da una distribuzione con media $\mu$ e varianza $\sigma ^ { 2 }$ . Sia $\overline { { X } }$ la media campionaria, e ricordiamo la seguente definizione dalla Sezione 2.3.2.

## Definizione

La statistica $S ^ { 2 }$ , definita da

$$
S ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{n - 1}
$$

è chiamata varianza del campione. $S = \sqrt { S ^ { 2 } }$ è chiamata deviazione standard del campione.

Per calcolare $E [ S ^ { 2 } ]$ , utilizziamo un'identità dimostrata nella Sezione 2.3.2: per qualsiasi numero $x _ { 1 } , \ldots , x _ { n }$

$$
\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}
$$

dove $\textstyle { \overline { { x } } } = \sum _ { i = 1 } ^ { n } x _ { i } / n$ . Da questa identità segue che

$$
(n - 1) S ^ {2} = \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - n \overline {{X}} ^ {2}
$$

Prendendo le aspettative di entrambi i lati dei risultati precedenti, utilizzando il fatto che per qualsiasi variabile casuale $W , E [ W ^ { 2 } ] = \mathrm { V a r } ( W ) \mathbf { \hat { \mu } } + ( E [ W ] ) ^ { 2 }$

$$
\begin{array}{r l} (n - 1) E [ S ^ {2} ] & = E \left[ \sum_ {i = 1} ^ {n} X _ {i} ^ {2} \right] - n E [ \overline {{X}} ^ {2} ] \\ & = n E [ X _ {1} ^ {2} ] - n E [ \overline {{X}} ^ {2} ] \\ & = n \mathrm{Var} (X _ {1}) + n (E [ X _ {1} ]) ^ {2} - n \mathrm{Var} (\overline {{X}}) - n (E [ \overline {{X}} ]) ^ {2} \\ & = n \sigma^ {2} + n \mu^ {2} - n (\sigma^ {2} / n) - n \mu^ {2} \\ & = (n - 1) \sigma^ {2} \end{array}
$$

o

$$
E [ S ^ {2} ] = \sigma^ {2}
$$

Ciò significa che il valore atteso della varianza del campione $S ^ { 2 }$ è uguale alla varianza della popolazione $\sigma ^ { 2 }$ .

## 6.5 DISTRIBUZIONI CAMPIONARIE DA UNA POPOLAZIONE NORMALE

Sia $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ un campione da una popolazione normale avente media $\mu$ e varianza $\sigma ^ { 2 }$ Ciò significa che sono indipendenti e $X _ { i } \sim \mathcal { N } ( \mu , \sigma ^ { 2 } ) , i = 1 , . . . , n .$ . Inoltre, siano

$$
\overline {{X}} = \sum_ {i = 1} ^ {n} X _ {i} / n
$$

e

$$
S ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{n - 1}
$$

a denotare rispettivamente la media campionaria e la varianza del campione. Vorremmo calcolare le loro distribuzioni.

## 6.5.1 Distribuzione della Media Campionaria

Poiché la somma di variabili casuali normali indipendenti è distribuita normalmente, segue che $\overline { { X } }$ è normale con media

$$
E [ \overline {{X}} ] = \sum_ {i = 1} ^ {n} \frac {E [ X _ {i} ]}{n} = \mu
$$

e varianza

$$
\operatorname{Var} (\overline {{X}}) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \operatorname{Var} (X _ {i}) = \sigma^ {2} / n
$$

Ciò significa che ${ \overline { { X } } } ,$ , la media del campione, è normale con una media uguale alla media della popolazione ma con una varianza ridotta di un fattore $1 / n$ . Da questo segue che

$$
\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}}
$$

è una variabile casuale normale standard.

## 6.5.2 Distribuzione Congiunta di $\bar { \pmb { \chi } }$ e $\pmb { S } ^ { 2 }$

In questa sezione, non otteniamo solo la distribuzione della varianza del campione $S ^ { 2 }$ , ma scopriamo anche un fatto fondamentale sulle popolazioni normali — ovvero, che $\overline { { X } }$ e $S ^ { 2 }$ sono indipendenti con $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 }$ avente una distribuzione chi-quadrato con $n - 1$ gradi di libertà.

Per iniziare, per numeri $x _ { 1 } , \ldots , x _ { n }$ , poniamo $y _ { i } = x _ { i } - \mu , i = 1 , \ldots , n ,$ . Allora, come ${ \overline { { y } } } = { \overline { { x } } } - \mu$ segue dall'identità

$$
\sum_ {i = 1} ^ {n} (y _ {i} - \bar {y}) ^ {2} = \sum_ {i = 1} ^ {n} y _ {i} ^ {2} - n \bar {y} ^ {2}
$$

che

$$
\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} = \sum_ {i = 1} ^ {n} (x _ {i} - \mu) ^ {2} - n (\overline {{x}} - \mu) ^ {2}
$$

Ora, se $X _ { 1 } , \ldots , X _ { n }$ è un campione da una popolazione normale avente media $\mu$ varianza $\sigma ^ { 2 }$ , allora otteniamo dall'identità precedente che

$$
\frac {\sum_ {i = 1} ^ {n} (X _ {i} - \mu) ^ {2}}{\sigma^ {2}} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{\sigma^ {2}} + \frac {n (\overline {{X}} - \mu) ^ {2}}{\sigma^ {2}}
$$

o, equivalentemente,

$$
\sum_ {i = 1} ^ {n} \left(\frac {X _ {i} - \mu}{\sigma}\right) ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{\sigma^ {2}} + \left[ \frac {\sqrt {n} (\overline {{X}} - \mu)}{\sigma} \right] ^ {2}\tag{6.5.1}
$$

Poiché $( X _ { i } - \mu ) / \sigma , i = 1 , \ldots , n$ sono normali standard indipendenti, segue che il lato sinistro dell'Equazione 6.5.1 è una variabile casuale chi-quadrato con n gradi di libertà. Inoltre, come mostrato nella Sezione 6.5.1, $\bar { \sqrt { n } } ( \overline { { X } } - \mu ) / \sigma$ è una variabile casuale normale standard e quindi il suo quadrato è una variabile casuale chi-quadrato con 1 grado di libertà. Pertanto, l'Equazione 6.5.1 mette in relazione una variabile casuale chi-quadrato avente n gradi di libertà con la somma di due variabili casuali, una delle quali è chi-quadrato con 1 grado di libertà. Ma è stato stabilito che la somma di due variabili casuali chi-quadrato indipendenti è anche chi-quadrato con un grado di libertà uguale alla somma dei due gradi di libertà. Pertanto, sembrerebbe che ci sia una possibilità ragionevole che i due termini sul lato destro dell'Equazione 6.5.1 siano indipendenti, con $\scriptstyle \sum _ { i = 1 } ^ { n } ( X _ { i } - { \overline { { X } } } ) ^ { 2 } / \sigma ^ { 2 }$ avente una distribuzione chi-quadrato con $n - 1$ gradi di libertà. Poiché questo risultato può effettivamente essere stabilito, abbiamo il seguente risultato fondamentale.

## Teorema 6.5.1

Se $X _ { 1 } , \ldots , X _ { n }$ è un campione da una popolazione normale con media $\mu$ e varianza $\sigma ^ { 2 }$ , allora $\overline { { X } }$ e $S ^ { 2 }$ sono variabili casuali indipendenti, con $\overline { { X } }$ normale con media $\mu$ e varianza $\sigma ^ { 2 } / n$ e $\ C n - 1 ) S ^ { 2 } / \sigma ^ { 2 }$ chi-quadrato con $n - 1$ gradi di libertà. 

Il Teorema 6.5.1 non fornisce solo le distribuzioni di $\overline { { X } }$ e $S ^ { 2 }$ per una popolazione normale, ma stabilisce anche il fatto importante che esse siano indipendenti. Infatti, si scopre che questa indipendenza di $\hat { \overline { { X } } }$ e $S ^ { 2 }$ è una proprietà unica della distribuzione normale. La sua importanza diventerà evidente nei capitoli successivi. 

EXAMPLE 6.5a Il tempo impiegato da un'unità centrale di elaborazione per processare un certo tipo di lavoro è distribuito normalmente con media 20 secondi e deviazione standard 3 secondi. Se viene osservato un campione di $1 5$ di tali lavori, qual è la probabilità che la varianza del campione superi 12? 

SOLUTION Poiché il campione è di dimensione $n = 1 5$ e $\sigma ^ { 2 } = 9$ , scriviamo 

$$
\begin{array}{r l} P \{S ^ {2} > 1 2 \} & = P \left\{\frac {1 4 S ^ {2}}{9} > \frac {1 4}{9}. 1 2 \right\} \\ & = P \{\chi_ {1 4} ^ {2} > 1 8. 6 7 \} \\ & = 1 -. 8 2 2 1 \quad \text { from   Program   5.8.1a } \\ & = . 1 7 7 9 \quad \blacksquare \end{array}
$$

Il seguente corollario del Teorema 6.5.1 sarà piuttosto utile nei capitoli successivi. 

## Corollario 6.5.2

Sia $X _ { i } , \ldots , X _ { n }$ un campione da una popolazione normale con media $\mu$ . Se $\overline { { X } }$ denota la media campionaria e S la deviazione standard campionaria, allora 

$$
\sqrt {n} \frac {(\overline {{X}} - \mu)}{S} \sim t _ {n - 1}
$$

Ciò significa che ${ \sqrt { n } } ( { \overline { { X } } } - \mu ) / S$ ha una distribuzione t con $n - 1$ gradi di libertà. 

## Dimostrazione

Ricordiamo che una variabile casuale t con n gradi di libertà è definita come la distribuzione di 

$$
\frac {Z}{\sqrt {\chi_ {n} ^ {2} / n}}
$$

dove $Z$ è una variabile casuale normale standard indipendente da $\chi _ { n } ^ { 2 } ,$ , una variabile casuale chi-quadrato con n gradi di libertà. Ne consegue quindi dal Teorema 6.5.1 che 

$$
\frac {\sqrt {n} (\overline {{X}} - \mu) / \sigma}{\sqrt {S ^ {2} / \sigma^ {2}}} = \sqrt {n} \frac {(\overline {{X}} - \mu)}{S}
$$

è una variabile casuale t con $n - 1$ gradi di libertà. 

## 6.6 CAMPIONAMENTO DA UNA POPOLAZIONE FINITA

Consideriamo una popolazione di N elementi, e supponiamo che $\boldsymbol { \mathit { p } }$ sia la proporzione della popolazione che possiede una determinata caratteristica di interesse; vale a dire, $N p$ elementi hanno questa caratteristica, e $N ( 1 - p )$ non la hanno. Un campione di dimensione n da questa popolazione è detto un campione casuale se viene scelto in modo tale che ciascuno dei $\binom { \bar { N } } { n }$ sottoinsiemi della popolazione di dimensione n abbia la stessa probabilità di essere il campione. Ad esempio, se la popolazione consiste nei tre elementi $a , b , c ,$ allora un campione casuale di dimensione 2 è uno scelto in modo che ciascuno dei sottoinsiemi $\{ a , b \} , \{ a , c \}$ e $\{ b , c \}$ abbia la stessa probabilità di essere il campione. Un sottoinsieme casuale può essere scelto sequenzialmente lasciando che il suo primo elemento abbia la stessa probabilità di essere uno qualsiasi dei N elementi della popolazione, quindi lasciando che il suo secondo elemento abbia la stessa probabilità di essere uno qualsiasi dei rimanenti $N - 1$ elementi della popolazione, e così via.

Supponiamo ora che un campione casuale di dimensione n sia stato scelto da una popolazione di dimensione N. Per $i = 1 , \ldots , n ,$, poniamo

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   member   of   the   sample   has   the   characteristic } \\ 0 & \text { otherwise } \end{array} \right.
$$

Consideriamo ora la somma dei $X _ { i } ;$, cioè, consideriamo

$$
X = X _ {1} + X _ {2} + \dots + X _ {n}
$$

Poiché il termine $X _ { i }$ contribuisce con 1 alla somma se l'i-esimo membro del campione possiede la caratteristica e 0 altrimenti, ne consegue che X è uguale al numero di membri del campione che possiedono la caratteristica. Inoltre, la media campionaria

$$
\overline {{X}} = X / n = \sum_ {i = 1} ^ {n} X _ {i} / n
$$

è uguale alla proporzione dei membri del campione che possiedono la caratteristica.

Consideriamo ora le probabilità associate alle statistiche X e ${ \overline { { X } } } .$. Per iniziare, si noti che poiché ciascuno dei $N$ membri della popolazione ha la stessa probabilità di essere l'i-esimo membro del campione, ne consegue che

$$
P \{X _ {i} = 1 \} = \frac {N p}{N} = p
$$

Inoltre,

$$
P \{X _ {i} = 0 \} = 1 - P \{X _ {i} = 1 \} = 1 - p
$$

Ciò significa che ogni $X _ { i }$ è uguale a 1 o 0 con le rispettive probabilità $\boldsymbol { \mathscr { P } }$ e $1 - p .$

Bisogna notare che le variabili casuali $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ non sono indipendenti. Ad esempio, poiché la seconda selezione ha la stessa probabilità di essere uno qualsiasi dei N membri della popolazione, dei quali $N p$ hanno la caratteristica, ne consegue che la probabilità che la seconda selezione abbia la caratteristica è $N p / N = p .$. Cioè, senza alcuna conoscenza dell'esito della prima selezione,

$$
P \{X _ {2} = 1 \} = p
$$

Tuttavia, la probabilità condizionata che $X _ { 2 } = 1$, dato che la prima selezione ha la caratteristica, è

$$
P \{X _ {2} = 1 | X _ {1} = 1 \} = \frac {N p - 1}{N - 1}
$$

che si osserva notando che se la prima selezione ha la caratteristica, allora la seconda selezione ha la stessa probabilità di essere uno qualsiasi dei rimanenti $N - 1$ elementi, dei quali $N p - 1$ hanno la caratteristica. Allo stesso modo, la probabilità che la seconda selezione abbia la caratteristica dato che la prima non la possiede è

$$
P \{X _ {2} = 1 | X _ {1} = 0 \} = \frac {N p}{N - 1}
$$

Così, sapere se il primo elemento del campione casuale ha la caratteristica o meno cambia la probabilità per il prossimo elemento. Tuttavia, quando la dimensione della popolazione N è grande rispetto alla dimensione del campione n, questo cambiamento sarà molto lieve. Ad esempio, se $N = 1 , 0 0 0 , { \mathrm { } } p = . 4$, allora

$$
P \{X _ {2} = 1 | X _ {1} = 1 \} = \frac {3 9 9}{9 9 9} = . 3 9 9 4
$$

che è molto vicino alla probabilità non condizionata che $X _ { 2 } = 1$; ovvero,

$$
P \{X _ {2} = 1 \} = . 4
$$

Allo stesso modo, la probabilità che il secondo elemento del campione abbia la caratteristica dato che il primo non la possiede è

$$
P \{X _ {2} = 1 | X _ {1} = 0 \} = \frac {4 0 0}{9 9 9} = . 4 0 0 4
$$

che è di nuovo molto vicino a $\cdot ^ { 4 . }$

In effetti, si può dimostrare che quando la dimensione della popolazione $N$ è grande rispetto alla dimensione del campione $^ { n , }$ allora $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ sono approssimativamente indipendenti. Ora se pensiamo a ogni $X _ { i }$ come rappresentativo del risultato di una prova che è un successo se $X _ { i }$ è uguale a 1 e un fallimento altrimenti, ne consegue che $\textstyle X = \sum _ { i = 1 } ^ { n } X _ { i }$ può essere considerato come rappresentativo del numero totale di successi in $\mathscr { n }$ prove. Pertanto, se i $X _ { i }$ fossero indipendenti, allora $X$ sarebbe una variabile casuale binomiale con parametri $n$ e $\scriptstyle { \boldsymbol { p } } .$. In altre parole, quando la dimensione della popolazione $N$ è grande in relazione alla dimensione del campione $^ { n , }$ allora la distribuzione del numero di membri del campione che possiedono la caratteristica è approssimativamente quella di una variabile casuale binomiale con parametri $n$ e $\scriptstyle { \boldsymbol { \hat { p } } } .$.

## REMARCA

Naturalmente, $X$ è una variabile casuale ipergeometrica (Sezione 5.4); e quindi quanto sopra mostra che un'ipergeometrica può essere approssimata da una variabile casuale binomiale quando il numero scelto è piccolo in relazione al numero totale di elementi.

Per il resto di questo testo, supporràmo che la popolazione sottostante sia grande in relazione alla dimensione del campione e prenderemo la distribuzione di $X$ come binomiale.

Utilizzando le formule fornite nella Sezione 5.1 per la media e la deviazione standard di una variabile casuale binomiale, vediamo che

$$
E [ X ] = n p \quad \mathrm{and} \quad S D (X) = \sqrt {n p (1 - p)}
$$

Poiché ${ \overline { { X } } } _ { i }$, la proporzione del campione che ha la caratteristica, è uguale a $X / n ,$, vediamo dal precedente che

$$
E [ \overline {{X}} ] = E [ X ] / n = p
$$

e

$$
S D (\overline {{X}}) = S D (X) / n = \sqrt {p (1 - p) / n}
$$

ESEMPIO 6.6a Supponiamo che il 45 percento della popolazione favorisca un certo candidato in una prossima elezione. Se viene scelto un campione casuale di dimensione 200, trovare

(a) il valore atteso e la deviazione standard del numero di membri del campione che favoriscono il candidato;

(b) la probabilità che più della metà dei membri del campione favoriscano il candidato.

SOLUZIONE

(a) Il valore atteso e la deviazione standard della proporzione che favorisce il candidato sono

$$
E [ X ] = 2 0 0 (. 4 5) = 9 0, \quad S D (X) = \sqrt {2 0 0 (. 4 5) (1 - . 4 5)} = 7. 0 3 5 6
$$

(b) Poiché $X$ è binomiale con parametri 200 e .45, il testo del disco fornisce la soluzione

$$
P \{X \geq 1 0 1 \} = . 0 6 8 1
$$

Se questo programma non fosse disponibile, allora potrebbe essere utilizzata l'approssimazione normale alla binomiale (Sezione 6.3):

$$
\begin{array}{r l} P \{X \geq 1 0 1 \} & = P \{X \geq 1 0 0. 5 \} \quad (\text { the   continuity   correction }) \\ & = P \left\{\frac {X - 9 0}{7 . 0 3 5 6} \geq \frac {1 0 0 . 5 - 9 0}{7 . 0 3 5 6} \right\} \\ & \approx P \{Z \geq 1. 4 9 2 4 \} \\ & \approx . 0 6 7 8 \end{array}
$$

La soluzione ottenuta tramite l'approssimazione normale è corretta a 3 cifre decimali. ■

Anche quando ogni elemento della popolazione ha più di due valori possibili, rimane comunque vero che se la dimensione della popolazione è grande in relazione alla dimensione del campione, allora i dati del campione possono essere considerati come variabili casuali indipendenti dalla distribuzione della popolazione.

ESEMPIO 6.6b Secondo il World Livestock Situation del Dipartimento dell'Agricoltura degli Stati Uniti, il paese con il maggior consumo pro capite di carne di maiale è la Danimarca. Nel 1994, la quantità di carne di maiale consumata da una persona residente in Danimarca aveva un valore medio di 147 libbre con una deviazione standard di 62 libbre. Se viene scelto un campione casuale di 25 danesi, approssimare la probabilità che la quantità media di carne di maiale consumata dai membri di questo gruppo nel 1994 abbia superato le 150 libbre.

SOLUZIONE Se poniamo $X _ { i }$ come la quantità consumata dall'i-esimo membro del campione, $i = 1 , \ldots , 2 5$, allora la probabilità desiderata è

$$
P \left\{\frac {X _ {1} + \cdots + X _ {2 5}}{2 5} > 1 5 0 \right\} = P \{\overline {{{X}}} > 1 5 0 \}
$$

dove $\overline { { X } }$ è la media campionaria dei 25 valori del campione. Poiché possiamo considerare le $X _ { i }$ come variabili casuali indipendenti con media $1 4 7$ e deviazione standard $6 2 ,$, ne consegue dal teorema del limite centrale che la loro media campionaria sarà approssimativamente normale con media $1 4 7$ e deviazione standard 62/5. Pertanto, con $Z$ come variabile casuale normale standard, abbiamo

$$
\begin{array}{c} P \{\overline {{X}} > 1 5 0 \} = P \left\{\frac {\overline {{X}} - 1 4 7}{1 2 . 4} > \frac {1 5 0 - 1 4 7}{1 2 . 4} \right\} \\ \approx P \{Z >. 2 4 2 \} \\ \approx . 4 0 4 \quad \blacksquare \end{array}
$$

## Problemi

1. Tracciare la funzione di massa di probabilità della media campionaria di $X _ { 1 } , \ldots , X _ { n }$, quando

(a) $n = 2 ;$ 

(a) $n = 3 .$ 

Assumere che la funzione di massa di probabilità di $X _ { i }$ sia 

$$
P \{X = 0 \} = . 2, P \{X = 1 \} = . 3, P \{X = 3 \} = . 5
$$

In entrambi i casi, determinare $E [ { \overline { { X } } } ]$ e $\mathrm { V a r } ( { \overline { { X } } } )$ 

2. Se vengono lanciati 10 dadi equi, approssimare la probabilità che la somma dei valori ottenuti (che varia da 20 a 120) sia compresa tra 30 e 40 inclusi. 

3. Approssimare la probabilità che la somma di 16 variabili casuali uniformi indipendenti (0, 1) superi 10. 

4. Una ruota della roulette ha 38 caselle, numerate 0, 00 e da 1 a 36. Se scommetti 1 su un numero specificato, vinci 35 se la pallina della roulette atterra su quel numero o perdi 1 se non lo fa. Se continui a effettuare tali scommesse, approssimare la 

probabilità che 

(a) tu stia vincendo dopo 34 scommesse; 

(b) tu stia vincendo dopo 1.000 scommesse; 

(c) tu stia vincendo dopo 100.000 scommesse. 

Assumere che ogni lancio della pallina della roulette abbia la stessa probabilità di atterrare su uno qualsiasi dei 38 numeri. 

5. Un dipartimento stradale ha abbastanza sale per gestire un totale di 80 pollici di neve. Supponiamo che la quantità giornaliera di neve abbia una media di 1,5 pollici e una deviazione standard di 0,3 pollici. 

(a) Approssimare la probabilità che il sale a disposizione sarà sufficiente per i prossimi 50 giorni. 

(b) Quale assunzione hai fatto nel risolvere la parte (a)? 

(c) Pensi che questa assunzione sia giustificata? Spiega brevemente. 

6. Cinquanta numeri vengono arrotondati all'intero più vicino e poi sommati. Se gli errori di arrotondamento individuali sono distribuiti uniformemente tra −0,5 e 0,5, qual è la probabilità approssimativa che la somma risultante differisca dalla somma esatta di più di 3? 

7. Un dado a sei facce, in cui ogni faccia ha la stessa probabilità di apparire, viene lanciato ripetutamente finché il totale di tutti i lanci non supera 400. Approssimare la probabilità che ciò richiederà più di 140 lanci. 

8. La quantità di tempo in cui funziona un certo tipo di batteria è una variabile casuale con media di 5 settimane e deviazione standard di 1,5 settimane. In caso di guasto, viene immediatamente sostituita da una nuova batteria. Approssimare la probabilità che saranno necessarie 13 o più batterie in un anno. 

9. La durata di vita di un certo componente elettrico è una variabile casuale con media di 100 ore e deviazione standard di 20 ore. Se vengono testati 16 di tali componenti, trovare la probabilità che la media campionaria sia 

(a) inferiore a 104; 

(b) compresa tra 98 e 104 ore. 

10. Una società di tabacco afferma che la quantità di nicotina nelle sue sigarette è una variabile casuale con media di 2,2 mg e deviazione standard di 0,3 mg. Tuttavia, il contenuto medio di nicotina del campione di 100 sigarette scelte casualmente era di 3,1 mg. Qual è la probabilità approssimativa che la media campionaria sarebbe stata alta quanto o più di 3,1 se le affermazioni della società fossero vere? 

11. La durata di vita (in ore) di un tipo di lampadina elettrica ha valore atteso 500 e deviazione standard 80. Approssimare la probabilità che la media campionaria di n di tali lampadine sia maggiore di 525 quando 

(a) $n = 4 ;$ 

(b) $n = 1 6 ;$ 

(c) $n = 3 6 ;$ 

(d) $n = 6 4 .$ 

12. Un istruttore sa dall'esperienza passata che i punteggi degli studenti agli esami hanno media 77 e deviazione standard 15. Attualmente l'istruttore sta insegnando due classi separate — una di dimensione 25 e l'altra di dimensione 64. 

(a) Approssimare la probabilità che il punteggio medio del test nella classe di dimensione 25 si trovi tra 72 e 82. 

(b) Ripetere la parte (a) per una classe di dimensione 64. 

(c) Qual è la probabilità approssimativa che il punteggio medio del test nella classe di dimensione 25 sia superiore a quello della classe di dimensione 64? 

(d) Supponiamo che i punteggi medi nelle due classi siano 76 e 83. Quale classe, quella di dimensione 25 o quella di dimensione 64, pensi fosse più probabile che avesse una media di 83?

13. Se X è binomiale con parametri $n = 1 5 0 , \mathrm { { } } p = . 6 ,$, calcola il valore esatto di $P \{ X \leq 8 0 \}$ e confrontalo con la sua approssimazione normale sia (a) facendo uso della correzione di continuità e (b) non facendone uso.

14. Ogni chip di computer prodotto in un determinato impianto sarà, indipendentemente, difettoso con probabilità .25. Se viene testato un campione di 1.000 chip, qual è la probabilità approssimativa che meno di 200 chip siano difettosi?

15. Una squadra di basket di un club giocherà una stagione di 60 partite. Trentadue di queste partite sono contro squadre di classe A e 28 sono contro squadre di classe B. Gli esiti di tutte le partite sono indipendenti. La squadra vincerà ogni partita contro un avversario di classe A con probabilità .5, e vincerà ogni partita contro un avversario di classe B con probabilità .7. Sia X il numero totale di vittorie nella stagione.

(a) X è una variabile casuale binomiale?

(b) Siano $X _ { A }$ e $X _ { B }$ rispettivamente il numero di vittorie contro le squadre di classe A e di classe B. Quali sono le distribuzioni di $X _ { A }$ e $X _ { B } ?$

(c) Qual è la relazione tra $X _ { A } , X _ { B }$ e X?

(d) Approssima la probabilità che la squadra vinca 40 o più partite.

16. Argomenta, basandoti sul teorema del limite centrale, che una variabile casuale di Poisson con media λ avrà approssimativamente una distribuzione normale con media e varianza entrambe uguali a λ quando λ è grande. Se X è di Poisson con media 100, calcola la probabilità esatta che X sia minore o uguale a 116 e confrontala con la sua approssimazione normale sia quando viene utilizzata una correzione di continuità sia quando non lo è. La convergenza di Poisson alla normale è indicata nella Figura 6.5.

17. Usa il disco di testo per calcolare $P \{ X \leq 1 0 \}$ quando X è una variabile casuale binomiale con parametri $n = 1 0 0 , p = . 1$. Ora confronta questo con la sua (a) approssimazione di Poisson e (b) normale. Utilizzando l'approssimazione normale, scrivi la probabilità desiderata come $P \{ X < 1 0 . 5 \}$ in modo da utilizzare la correzione di continuità.


Poisson (10)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5505e6e79df55a10d19c04620cbe5a93568b584f985db361c371053b4f9b71b5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/ad60f52045dfa08e1b78361134df0ddc9c58eb1a1060a38e29f9501bc8f943da.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/1c09cefaa01eb84b74c74bc73d11388f9af8ed848286867c0cca733aaffb549b.jpg)



FIGURA 6.5 Funzioni di massa di probabilità di Poisson.


18. La temperatura alla quale un termostato scatta è distribuita normalmente con varianza $\scriptstyle { \hat { \sigma } } ^ { 2 }$. Se il termostato deve essere testato cinque volte, trova

(a) $P \{ S ^ { 2 } / \sigma ^ { 2 } \le 1 . 8 \}$

(b) $P \{ . 8 5 \leq S ^ { 2 } / \sigma ^ { 2 } \leq 1 . 1 5 \}$

dove $S ^ { 2 }$ è la varianza campionaria dei cinque valori dei dati.

19. Nel Problema 18, quanto grande dovrebbe essere il campione per garantire che la probabilità nella parte (a) sia almeno .95?

20. Considera due campioni indipendenti — il primo di dimensione 10 da una popolazione normale con varianza 4 e il secondo di dimensione 5 da una popolazione normale con varianza 2. Calcola la probabilità che la varianza campionaria del secondo campione superi quella del primo. (Suggerimento: Relazionala alla distribuzione F.)

21. Il dodici per cento della popolazione è mancino. Trova la probabilità che ci siano tra 10 e 14 mancini in un campione casuale di 100 membri di questa popolazione. Ovvero, trova $P \{ 1 0 \leq X \leq 1 4 \}$, dove X è il numero di mancini nel campione.

22. Il cinquantadue per cento dei residenti di una certa città sono favorevoli all'insegnamento dell'evoluzione nelle scuole superiori. Trova o approssima la probabilità che almeno il 50 per cento di un campione casuale di dimensione n sia favorevole all'insegnamento dell'evoluzione, quando

(a) n = 10;

(b) $n = 1 0 0 ;$

(c) $n = 1 , 0 0 0 ;$

(d) $n = 1 0 , 0 0 0 .$

23. La seguente tabella fornisce le percentuali di individui, categorizzati per genere, che seguono certe pratiche sanitarie negative. Supponiamo che venga scelto un campione casuale di 300 uomini. Approssima la probabilità che

(a) almeno 150 di loro mangino raramente la colazione;

(b) meno di 100 di loro fumino.

<table><tr><td></td><td>Dorme 6 Ore o Meno per Notte</td><td>Fumatore</td><td>Raramente Fa Colazione</td><td>È Sovrappeso del 20 Percento o Più</td></tr><tr><td>Uomini</td><td>22.7</td><td>28.4</td><td>45.4</td><td>29.6</td></tr><tr><td>Donne</td><td>21.4</td><td>22.8</td><td>42.0</td><td>25.6</td></tr></table>


Fonte: US National Center for Health Statistics. Health Promotion and Disease Prevention. 1990 


24. (Usa la tabella del Problema 23.) Supponiamo che venga scelto un campione casuale di 300 donne. Approssima la probabilità che

(a) almeno 60 di loro siano in sovrappeso del 20 percento o più;

(b) meno di 50 di loro dormano 6 ore o meno ogni notte.

25. (Usa la tabella del Problema 23.) Supponiamo che vengano scelti campioni casuali di 300 donne e di 300 uomini. Approssima la probabilità che più donne che uomini raramente facciano colazione.

26. La seguente tabella utilizza dati del 1989 riguardanti le percentuali di lavoratori a tempo pieno uomini e donne i cui stipendi annuali rientrano in diverse fasce salariali. Supponiamo che siano stati scelti campioni casuali di 1.000 uomini e 1.000 donne. Usa la tabella per approssimare la probabilità che

(a) almeno la metà delle donne abbia guadagnato meno di $20.000;

(b) più della metà degli uomini abbia guadagnato $20.000 o più;

(c) più della metà delle donne e più della metà degli uomini abbiano guadagnato $20.000 o più;

(d) 250 o meno delle donne abbiano guadagnato almeno $25.000;

(e) almeno 200 degli uomini abbiano guadagnato $50.000 o più;

(f) più donne che uomini abbiano guadagnato tra $20,000 and $24,999

<table><tr><td>Fascia di Guadagno</td><td>Percentuale di Donne</td><td>Percentuale di Uomini</td></tr><tr><td>$4,999 or less</td><td>2.8</td><td>1.8</td></tr><tr><td>$5,000 a $9,999</td><td>10.4</td><td>4.7</td></tr><tr><td>$10,000 a $19,999</td><td>41.0</td><td>23.1</td></tr><tr><td>$20,000 a $25,000</td><td>16.5</td><td>13.4</td></tr><tr><td>$25,000 a $49,999</td><td>26.3</td><td>42.1</td></tr><tr><td>$50,000 e oltre</td><td>3.0</td><td>14.9</td></tr></table>


Fonte: U.S. Department of Commerce, Bureau of the Census.


27. Nel 1995 la percentuale della forza lavoro che apparteneva a un sindacato era del 14,9. Se cinque lavoratori fossero stati scelti casualmente in quell'anno, quale sarebbe la probabilità che nessuno di loro appartenesse a un sindacato? Confronta la tua risposta con quella che sarebbe stata per l'anno 1945, quando un massimo storico del 35,5 percento della forza lavoro apparteneva a un sindacato.

28. La media campionaria e la deviazione standard campionaria di tutti i punteggi degli studenti di San Francisco nel più recente esame Scholastic Aptitude Test in matematica erano 517 e 120. Approssima la probabilità che un campione casuale di 144 studenti avrebbe un punteggio medio superiore a

(a) 507;

(b) 517;

(c) 537;

(d) 550.

29. Lo stipendio medio dei neolaureati con laurea in ingegneria chimica è $43,600, with a standard deviation of $3,200. Approssima la probabilità che lo stipendio medio di un campione di 12 ingegneri chimici recentemente laureati superi i $45,000.

30. Un certo componente è critico per il funzionamento di un sistema elettrico e deve essere sostituito immediatamente in caso di guasto. Se la durata media di questo tipo di componente è di 100 ore e la sua deviazione standard è di 30 ore, quanti componenti devono essere in magazzino affinché la probabilità che il sistema sia in continuo funzionamento per le prossime 2000 ore sia almeno .95?

Questa Pagina È Intenzionalmente Lasciata Vuota

## STIMA DEI PARAMETRI

## 7.1 INTRODUZIONE

Sia $X _ { 1 } , \ldots , X _ { n }$ un campione casuale da una distribuzione $F _ { \theta }$ che è specificata fino a un vettore di parametri sconosciuti $\theta$. Ad esempio, il campione potrebbe provenire da una distribuzione di Poisson il cui valore medio è sconosciuto; oppure potrebbe provenire da una distribuzione normale avente una media e una varianza sconosciute. Mentre nella teoria della probabilità è consuetudine supporre che tutti i parametri di una distribuzione siano noti, il contrario è vero in statistica, dove un problema centrale è utilizzare i dati osservati per trarre inferenze sui parametri sconosciuti.

Nella Sezione 7.2, presentiamo il metodo della massima verosimiglianza per determinare stimatori di parametri sconosciuti. Le stime così ottenute sono chiamate stime puntuali, poiché specificano una singola quantità come stima di $\theta$. Nella Sezione 7.3, consideriamo il problema di ottenere stime intervallari. In questo caso, invece di specificare un certo valore come nostra stima di $\theta$, specifichiamo un intervallo in cui stimiamo che si trovi $\theta$. Inoltre, consideriamo la questione di quanta confidenza possiamo attribuire a tale stima intervallare. Illustriamo mostrando come ottenere una stima intervallare della media sconosciuta di una distribuzione normale la cui varianza è specificata. Consideriamo poi una varietà di problemi di stima intervallare. Nella Sezione 7.3.1, presentiamo una stima intervallare della media di una distribuzione normale la cui varianza è sconosciuta. Nella Sezione 7.3.2, otteniamo una stima intervallare della varianza di una distribuzione normale. Nella Sezione 7.4, determiniamo una stima intervallare per la differenza di due medie normali, sia quando le loro varianze sono assunte come note e sia quando sono assunte come sconosciute (sebbene nell'ultimo caso supponiamo che le varianze sconosciute siano uguali). Nelle Sezioni 7.5 e nella Sezione opzionale 7.6, presentiamo stime intervallari della media di una variabile casuale di Bernoulli e della media di una variabile casuale esponenziale.

Nella Sezione opzionale 7.7, torniamo al problema generale di ottenere stime puntuali di parametri sconosciuti e mostriamo come valutare uno stimatore considerando il suo errore quadratico medio (mean square error). Viene discusso il bias di uno stimatore e viene esplorata la sua relazione con l'errore quadratico medio.

Nella Sezione opzionale $7 . 8 ,$, consideriamo il problema di determinare una stima di un parametro sconosciuto quando è disponibile qualche informazione a priori. Questo è l'approccio Bayesiano, che suppone che prima di osservare i dati, informazioni su $\theta$ siano sempre disponibili per il decisore, e che queste informazioni possano essere espresse in termini di una distribuzione di probabilità su $\theta$. In tale situazione, mostriamo come calcolare lo stimatore Bayesiano, che è lo stimatore la cui distanza quadratica attesa da $\theta$ è minima.

## 7.2 STIMATORI DI MASSIMA VEROSIMILITUDINE

Qualsiasi statistica utilizzata per stimare il valore di un parametro sconosciuto θ è chiamata stimatore di θ. Il valore osservato dello stimatore è chiamato stima. Ad esempio, come vedremo, il comune stimatore della media di una popolazione normale, basato su un campione $X _ { 1 } , \ldots , X _ { n }$ da quella popolazione, è la media campionaria $\overline { { X } } = \textstyle \sum _ { i } X _ { i } / n$. Se un campione di dimensione 3 fornisce i dati $X _ { 1 } = 2 , X _ { 2 } = 3 , X _ { 3 } = 4$, allora la stima della media della popolazione, risultante dallo stimatore X, è il valore 3.

Supponiamo che le variabili casuali $X _ { 1 } , \ldots , X _ { n }$, la cui distribuzione congiunta è assunta come nota eccetto per un parametro sconosciuto θ, debbano essere osservate. Il problema di interesse è utilizzare i valori osservati per stimare $\theta .$. Ad esempio, le $\vec { X _ { i } ^ { \ : \prime } s }$ potrebbero essere variabili casuali esponenziali indipendenti, ciascuna avente la stessa media sconosciuta $\theta .$. In questo caso, la funzione di densità congiunta delle variabili casuali sarebbe data da

$$
\begin{array}{l} f (x _ {1}, x _ {2}, \dots , x _ {n}) \\ = f _ {X _ {1}} (x _ {1}) f _ {X _ {2}} (x _ {2}) \dots f _ {X _ {n}} (x _ {n}) \\ = \frac {1}{\theta} e ^ {- x _ {1} / \theta} \frac {1}{\theta} e ^ {- x _ {2} / \theta} \dots \frac {1}{\theta} e ^ {- x _ {n} / \theta}, \quad 0 <   x _ {i} <   \infty , i = 1, \dots , n \\ = \frac {1}{\theta^ {n}} \exp \left\{- \sum_ {1} ^ {n} x _ {i} / \theta \right\}, \quad 0 <   x _ {i} <   \infty , i = 1, \dots , n \end{array}
$$

e l'obiettivo sarebbe quello di stimare θ dai dati osservati $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$

Un particolare tipo di stimatore, noto come stimatore di massima verosimiglitudine, è ampiamente utilizzato in statistica. Esso si ottiene ragionando come segue. $\operatorname { L e t } f ( x _ { 1 } , \dots , x _ { n } | \theta )$ ) denota la funzione di massa di probabilità congiunta delle variabili casuali $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ quando sono discrete, e sia essa la loro funzione di densità di probabilità congiunta quando sono variabili casuali congiuntamente continue. Poiché $\theta$ è assunto come sconosciuto, scriviamo anche $f$ come funzione di $\theta .$. Ora, poiché $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ rappresenta la verosimiglitudine che i valori $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ saranno osservati quando θ è il valore vero del parametro, sembrerebbe che una stima ragionevole di $\theta$ sarebbe quel valore che fornisce la massima verosimiglitudine dei valori osservati. In altre parole, la stima di massima verosimiglitudine $\hat { \theta }$ è definita come quel valore di $\theta$ che massimizza $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ dove $x _ { 1 } , \ldots , x _ { n }$ sono i valori osservati. La funzione $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ è spesso definita come la funzione di verosimiglitudine di θ.

Nel determinare il valore che massimizza $\theta ,$, è spesso utile utilizzare il fatto che $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ e log[ $f ( x _ { 1 } , \dots , x _ { n } | \theta ) ]$ hanno il loro massimo allo stesso valore di $\theta$. Pertanto, possiamo anche ottenere $\hat { \theta }$ massimizzando log $\mathcal { f } ( x _ { 1 } , \dots , x _ { n } | \theta ) ]$

EXAMPLE 7.2a Stimatore di Massima Verosimiglitudine di un Parametro di Bernoulli Supponiamo che vengano eseguiti n tentativi indipendenti, ciascuno dei quali è un successo con probabilità ${ \boldsymbol { p } } ,$. Qual è lo stimatore di massima verosimiglitudine di $\dot { \boldsymbol { p } } \colon$

SOLUZIONE I dati consistono nei valori di $X _ { 1 } , \ldots , X _ { n }$ dove

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   trial   } i \text {   is   a   success } \\ 0 & \text { otherwise } \end{array} \right.
$$

Ora

$$
P \{X _ {i} = 1 \} = p = 1 - P \{X _ {i} = 0 \}
$$

che può essere espresso sinteticamente come

$$
P \{X _ {i} = x \} = p ^ {x} (1 - p) ^ {1 - x}, \quad x = 0, 1
$$

Pertanto, per l'indipendenza assunta dei tentativi, la verosimiglitudine (ovvero, la funzione di massa di probabilità congiunta) dei dati è data da

$$
\begin{array}{r l} & f (x _ {1}, \ldots , x _ {n} | p) = P \{X _ {1} = x _ {1}, \ldots , X _ {n} = x _ {n} | p \} \\ & \qquad = p ^ {x _ {1}} (1 - p) ^ {1 - x _ {1}} \dots p ^ {x _ {n}} (1 - p) ^ {1 - x _ {n}} \\ & \qquad = p ^ {\Sigma_ {1} ^ {n} x _ {i}} (1 - p) ^ {n - \Sigma_ {1} ^ {n} x _ {i}}, \quad x _ {i} = 0, 1, \quad i = 1, \ldots , n \end{array}
$$

Per determinare il valore di $\dot { \mathbf { \rho } } _ { p }$ che massimizza la verosimiglitudine, si prendono prima i logaritmi per ottenere

$$
\log f (x _ {1}, \dots , x _ {n} | p) = \sum_ {1} ^ {n} x _ {i} \log p + \left(n - \sum_ {1} ^ {n} x _ {i}\right) \log (1 - p)
$$

La derivazione produce

$$
\frac {d}{d p} \log f (x _ {1}, \dots , x _ {n} | p) = \frac {\sum_ {1} ^ {n} x _ {i}}{p} - \frac {(n - \sum_ {1} ^ {n} x _ {i})}{1 - p}
$$

Uguagliando a zero e risolvendo, otteniamo che la stima di massima verosimiglitudine $\hat { \boldsymbol { p } }$ soddisfa

$$
\frac {\sum_ {1} ^ {n} x _ {i}}{\hat {p}} = \frac {n - \sum_ {1} ^ {n} x _ {i}}{1 - \hat {p}}
$$

o

$$
\hat {p} = \frac {\sum_ {i = 1} ^ {n} x _ {i}}{n}
$$

Pertanto, lo stimatore di massima verosimiglitudine della media sconosciuta di una distribuzione di Bernoulli è dato da

$$
d (X _ {1}, \ldots , X _ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}
$$

Poiché $\sum _ { i = 1 } ^ { n } X _ { i }$ è il numero di prove riuscite, vediamo che il stimatore di massima verosimiglianza di $\dot { \mathbf { \Omega } } _ { p }$ è uguale alla proporzione delle prove osservate che risultano in successi. Per esempio, supponiamo che ogni chip RAM (random access memory) prodotto da un determinato produttore sia, indipendentemente, di qualità accettabile con probabilità $\scriptstyle { \boldsymbol { p } } .$. Allora se su un campione di 1.000 testati ne sono accettabili 921, ne consegue che la stima di massima verosimiglianza di $\dot { \boldsymbol { p } }$ è .921. ■

EXAMPLE 7.2b A due correttori di bozze è stato dato lo stesso manoscritto da leggere. Se il correttore di bozze 1 ha trovato $n _ { 1 }$ errori, e il correttore di bozze 2 ha trovato $n _ { 2 }$ errori, con $_ { n _ { 1 , 2 } }$ di questi errori trovati da entrambi i correttori, stima $N ,$ il numero totale di errori presenti nel manoscritto.

SOLUTION Prima di poter stimare N dobbiamo fare alcune assunzioni sul modello di probabilità sottostante. Supponiamo quindi che i risultati dei correttori di bozze siano indipendenti e che ogni errore nel manoscritto sia trovato indipendentemente dal correttore di bozze i con probabilità $\ p _ { i } , i = 1 , 2$

Per stimare $N ,$ inizieremo derivando un estimatore di $\displaystyle { \phi _ { 1 } }$. Per farlo, si noti che ciascuno dei $n _ { 2 }$ errori trovati dal lettore 2 sarà, indipendentemente, trovato dal correttore di bozze 1 con probabilità $\mathbf { \nabla } \phi _ { i } .$. Poiché il correttore di bozze 1 ha trovato $_ { n _ { 1 , 2 } }$ di quegli $n _ { 2 }$ errori, una stima ragionevole di $\dot { p } _ { 1 }$ è data da

$$
\hat {p} _ {1} = \frac {n _ {1 , 2}}{n _ {2}}
$$

Tuttavia, poiché il correttore di bozze 1 ha trovato $n _ { 1 }$ degli N errori nel manoscritto, è ragionevole supporre che $\displaystyle { \phi _ { 1 } }$ sia anche approssimativamente uguale a $\textstyle { \frac { n _ { 1 } } { N } }$. Pareggiando questo a $\hat { p } _ { 1 }$ si ottiene che

$$
\frac {n _ {1 , 2}}{n _ {2}} \approx \frac {n _ {1}}{N}
$$

o

$$
N \approx \frac {n _ {1} n _ {2}}{n _ {1 , 2}}
$$

Poiché la stima precedente è simmetrica in $n _ { 1 }$ e $n _ { 2 }$, ne consegue che è la stessa indipendentemente da quale correttore di bozze venga designato come correttore di bozze 1.

Un'applicazione interessante della precedente si è verificata quando due team di ricercatori hanno recentemente annunciato di aver decodificato la sequenza del codice genetico umano. Come parte del loro lavoro, entrambi i team hanno stimato che il genoma umano fosse composto da circa 33.000 geni. Poiché entrambi i team sono arrivati indipendentemente allo stesso numero, molti scienziati hanno trovato questo numero credibile. Tuttavia, la maggior parte degli scienziati è rimasta piuttosto sorpresa da questo numero relativamente piccolo di geni; per confronto, è solo circa il doppio di quelli che possiede una mosca della frutta. Tuttavia, un'ispezione più attenta dei risultati ha indicato che i due gruppi concordavano solo sull'esistenza di circa 17.000 geni. (Ovvero, 17.000 geni sono stati trovati da entrambi i team.) Pertanto, sulla base del nostro estimatore precedente, stimeremmo che il numero effettivo di geni, invece di essere 33.000, sia

$$
\frac {n _ {1} n _ {2}}{n _ {1 , 2}} = \frac {3 3 , 0 0 0 \times 3 3 , 0 0 0}{1 7 , 0 0 0} \approx 6 4, 0 0 0
$$

(Poiché c'è qualche controversia sul fatto che alcuni dei geni dichiarati trovati siano effettivamente geni, 64.000 dovrebbe probabilmente essere considerato come un limite superiore al numero effettivo di geni.)

L'approccio di stima utilizzato quando ci sono due correttori non funziona quando ci sono $m$ correttori, quando $m > 2$. Infatti, se per ogni $i ,$ lasciamo che $\hat { \ b { p } } _ { i }$ sia la frazione degli errori trovati da almeno uno degli altri correttori $j ,$ $( j \neq i )$, che sono anche trovati da $i ,$ e poi impostiamo tale valore uguale a $\frac { n _ { i } } { N }$, allora la stima di $N ,$, ovvero $\frac { n _ { i } } { \hat { \rho } _ { i } }$, differirebbe per diversi valori di $i .$. Inoltre, con questo approccio è possibile che si verifichi che $\hat { p } _ { i } > \hat { p } _ { j }$ anche se il correttore $i$ trova meno errori rispetto al correttore $j .$. Ad esempio, per $m = 3$ supponiamo che i correttori 1 e 2 trovino esattamente lo stesso set di 10 errori, mentre il correttore 3 ne trova 20 con solo 1 in comune con il set di errori trovati dagli altri. Allora, poiché il correttore 1 (e 2) ha trovato 10 dei 29 errori trovati da almeno uno degli altri correttori, $\hat { p } _ { i } = 1 0 / 2 9 , i = 1 , 2$. D'altra parte, poiché il correttore 3 ha trovato solo 1 dei 10 errori trovati dagli altri, $\hat { p } _ { 3 } = 1 / 1 0$. Pertanto, sebbene il correttore 3 abbia trovato il doppio del numero di errori rispetto al correttore 1, la stima di $\mathit { p 3 }$ è inferiore a quella di $\dot { p } _ { 1 }$. Per ottenere stime più ragionevoli, potremmo prendere i valori precedenti di $\hat { p } _ { i } , i = 1 , \ldots , m$, come stime preliminari di $\mathbf { \nabla } \phi _ { i }$. Ora, sia $n _ { f }$ il numero di errori che sono trovati da almeno un correttore. Poiché $n_f/N$ è la frazione di errori che sono trovati da almeno un correttore, questo dovrebbe essere approssimativamente uguale a $\textstyle 1 - \prod _ { i = 1 } ^ { m } ( 1 - p _ { i } )$, la probabilità che un errore sia trovato da almeno un correttore. Pertanto, abbiamo

$$
{\frac {n _ {f}}{N}} \approx 1 - \prod_ {i = 1} ^ {m} (1 - p _ {i})
$$

suggerendo che $N \approx \hat { N }$, dove

$$
\hat {N} = \frac {n _ {f}}{1 - \prod_ {i = 1} ^ {m} (1 - \hat {p} _ {i})}\tag{7.2.1}
$$

Con questa stima di $N$, possiamo quindi resettare le nostre stime di $\mathbf { \nabla } _ { \mathbf { \beta } } ^ { \mathbf { \gamma } _ { \mathbf { \beta } } ^ { \mathbf { \gamma } _ { \mathbf { \hat { \varepsilon } } } ^ { \mathbf { \varepsilon } } } }$ utilizzando

$$
\hat {p} _ {i} = \frac {n _ {i}}{\hat {N}}, \quad i = 1, \ldots , m\tag{7.2.2}
$$

Possiamo quindi riesstimare $N$ utilizzando il nuovo valore (7.2.1). (La stima non deve necessariamente fermarsi qui; ogni volta che otteniamo una nuova stima $\hat { N }$ di $N$ possiamo usare (7.2.2) per ottenere nuove stime di $\mathbf { \nabla } _ { \mathbf { \mathit { p } } _ { i } }$, che possono poi essere utilizzate per ottenere una nuova stima di $N ,$ e così via.) ■

ESEMPIO 7.2c Stimatore di Massima Verosimiglianza di un Parametro di Poisson Supponiamo che $X _ { 1 } , \ldots , X _ { n }$ siano variabili casuali di Poisson indipendenti, ciascuna con media $\lambda .$. Determinate lo stimatore di massima verosimiglianza di $\lambda$.

SOLUZIONE La funzione di verosimiglianza è data da

$$
\begin{array}{c} f (x _ {1}, \ldots , x _ {n} | \lambda) = \frac {e ^ {- \lambda} \lambda^ {x _ {1}}}{x _ {1} !} \dots \frac {e ^ {- \lambda} \lambda^ {x _ {n}}}{x _ {n} !} \\ = \frac {e ^ {- n \lambda} \lambda^ {\sum_ {1} ^ {n} x _ {i}}}{x _ {1} ! \ldots x _ {n} !} \end{array}
$$

Pertanto,

$$
\log f (x _ {1}, \dots , x _ {n} | \lambda) = - n \lambda + \sum_ {1} ^ {n} x _ {i} \log \lambda - \log c
$$

dove $c = \prod _ { i = 1 } ^ { n }$ $x$ ! non dipende da $\lambda ,$ e

$$
{\frac {d}{d \lambda}} \log f (x _ {1}, \ldots , x _ {n} | \lambda) = - n + {\frac {\sum_ {1} ^ {n} x _ {i}}{\lambda}}
$$

Uguagliando a zero, otteniamo che la stima di massima verosimiglianza $\hat { \lambda }$ è uguale a

$$
\hat {\lambda} = \frac {\sum_ {1} ^ {n} x _ {i}}{n}
$$

e quindi lo stimatore di massima verosimiglianza è dato da

$$
d (X _ {1}, \ldots , X _ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}
$$

Ad esempio, supponiamo che il numero di persone che entrano in un determinato esercizio commerciale in qualsiasi giorno sia una variabile casuale di Poisson con media sconosciuta $\lambda$, che deve essere stimata. Se dopo 20 giorni un totale di 857 persone sono entrate nell'esercizio, allora la stima di massima verosimiglianza di $\lambda$ è $8 5 7 / 2 0 \ = \ 4 2 . 8 5$. Ciò significa che stimiamo che in media 42,85 clienti entreranno nell'esercizio in un dato giorno. ■

ESEMPIO 7.2d Il numero di incidenti stradali a Berkeley, California, in 10 giorni non piovosi scelti casualmente nel 1998 è il seguente:

$$
4, 0, 6, 5, 2, 1, 2, 0, 4, 3
$$

Utilizzate questi dati per stimare la proporzione di giorni non piovosi che hanno avuto 2 o meno incidenti in quell'anno.

SOLUZIONE Poiché c'è un gran numero di conducenti, ognuno dei quali ha una piccola probabilità di essere coinvolto in un incidente in un dato giorno, sembra ragionevole assumere che il numero giornaliero di incidenti stradali sia una variabile casuale di Poisson. Poiché

$$
\overline {{{X}}} = \frac {1}{1 0} \sum_ {i = 1} ^ {1 0} X _ {i} = 2. 7
$$

ne consegue che la stima di massima verosimiglianza della media di Poisson è 2.7. Poiché la proporzione a lungo termine dei giorni non piovosi che hanno 2 o meno incidenti è uguale a $P \{ X \leq 2 \}$ dove X è il numero casuale di incidenti in un giorno, ne consegue che la stima desiderata è

$$
e ^ {- 2. 7} (1 + 2. 7 + (2. 7) ^ {2} / 2) = . 4 9 3 6
$$

Ciò significa che stimiamo che poco meno della metà dei giorni non piovosi abbia avuto 2 o meno incidenti. ■

EXAMPLE 7.2e Maximum Likelihood Estimator in a Normal Population Supponiamo che $X _ { 1 } , \ldots , X _ { n }$ siano variabili casuali normali indipendenti, ciascuna con media sconosciuta $\mu$ e deviazione standard sconosciuta $\sigma$. La densità congiunta è data da

$$
\begin{array}{c} f (x _ {1}, \ldots , x _ {n} | \mu , \sigma) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} \exp \left[ \frac {- (x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}} \right] \\ = \left(\frac {1}{2 \pi}\right) ^ {n / 2} \frac {1}{\sigma^ {n}} \exp \left[ \frac {- \sum_ {1} ^ {n} (x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}} \right] \end{array}
$$

Il logaritmo della verosimiglianza è quindi dato da

$$
\log f (x _ {1}, \ldots , x _ {n} | \mu , \sigma) = - \frac {n}{2} \log (2 \pi) - n \log \sigma - \frac {\sum_ {1} ^ {n} (x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}}
$$

Al fine di trovare il valore di ${ \bf \dot { \boldsymbol \mu } } _ { \mu }$ e $\sigma$ che massimizzi quanto sopra, calcoliamo

$$
\begin{array}{l} \frac {\partial}{\partial \mu} \log f (x _ {1}, \ldots , x _ {n} | \mu , \sigma) = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \mu)}{\sigma^ {2}} \\ \frac {\partial}{\partial \sigma} \log f (x _ {1}, \ldots , x _ {n} | \mu , \sigma) = - \frac {n}{\sigma} + \frac {\sum_ {1} ^ {n} (x _ {i} - \mu) ^ {2}}{\sigma^ {3}} \end{array}
$$

Uguagliando queste equazioni a zero si ottiene che

$$
\hat {\mu} = \sum_ {i = 1} ^ {n} x _ {i} / n
$$

e

$$
\hat {\sigma} = \left[ \sum_ {i = 1} ^ {n} (x _ {i} - \hat {\mu}) ^ {2} / n \right] ^ {1 / 2}
$$

Pertanto, gli stimatori di massima verosimiglianza di $\mu$ e $\sigma$ sono dati, rispettivamente, da

$$
\overline {{X}} \quad \text { and } \quad \left[ \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2} / n \right] ^ {1 / 2}\tag{7.2.3}
$$

Bisogna notare che lo stimatore di massima verosimiglianza della deviazione standard $\sigma$ differisce dalla deviazione standard del campione

$$
S = \left[ \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2} / (n - 1) \right] ^ {1 / 2}
$$

nel fatto che il denominatore nell'Equazione 7.2.3 è $\sqrt { n }$ anziché $\sqrt { n - 1 }$. Tuttavia, per n di dimensioni ragionevoli, questi due stimatori di $\dot { } \sigma$ saranno approssimativamente uguali. ■

EXAMPLE 7.2f La legge di frammentazione di Kolmogorov afferma che la dimensione di una singola particella in una grande collezione di particelle risultanti dalla frammentazione di un composto minerale avrà una distribuzione approssimativamente lognormale, dove si dice che una variabile casuale X ha una distribuzione lognormale se log(X) ha una distribuzione normale. La legge, che è stata prima notata empiricamente e poi successivamente dotata di una base teorica da Kolmogorov, è stata applicata a una varietà di studi ingegneristici. Ad esempio, è stata utilizzata nell'analisi della dimensione di particelle d'oro scelte casualmente da una collezione di sabbia d'oro. Un'applicazione meno ovvia della legge è stata a uno studio del rilascio di stress nelle zone di faglia sismica (vedere Lomnitz, C., “Global Tectonics and Earthquake Risk,” Developments in Geotectonics, Elsevier, Amsterdam, 1979).

Supponiamo che un campione di 10 grani di sabbia metallica prelevati da una grande pila di sabbia abbiano lunghezze rispettive (in millimetri):

$$
2. 2, 3. 4, 1. 6, 0. 8, 2. 7, 3. 3, 1. 6, 2. 8, 2. 5, 1. 9
$$

Stima la percentuale di grani di sabbia nell'intera pila la cui lunghezza è compresa tra 2 e 3 mm.

SOLUTION Prendendo il logaritmo naturale di questi 10 valori di dati, si ottiene il seguente set di dati trasformati

$$
. 7 8 8 5, 1. 2 2 3 8,. 4 7 0 0, -. 2 2 3 1,. 9 9 3 3, 1. 1 9 3 9,. 4 7 0 0, 1. 0 2 9 6,. 9 1 6 3,. 6 4 1 9
$$

Poiché la media del campione e la deviazione standard del campione di questi dati sono

$$
\overline {{{{x}}}} = . 7 5 0 4, \quad s = . 4 3 5 1
$$

ne consegue che il logaritmo della lunghezza di un grano scelto casualmente ha una distribuzione normale con media approssimativamente uguale a .7504 e con deviazione standard approssimativamente uguale a .4351. Pertanto, se X è la lunghezza del grano, allora

$$
\begin{array}{l} P \{2 <   X <   3 \} = P \{\log (2) <   \log (X) <   \log (3) \} \\ \qquad = P \left\{\frac {\log (2) - . 7 5 0 4}{. 4 3 5 1} <   \frac {\log (X) - . 7 5 0 4}{. 4 3 5 1} <   \frac {\log (3) - . 7 5 0 4}{. 4 3 5 1} \right\} \\ \qquad = P \left\{-. 1 3 1 6 <   \frac {\log (X) - . 7 5 0 4}{. 4 3 5 1} <  . 8 0 0 3 \right\} \\ \qquad \approx \Phi (. 8 0 0 3) - \Phi (-. 1 3 1 6) \\ \qquad = . 3 4 0 5 \quad \blacksquare \end{array}
$$

In tutti gli esempi precedenti, lo stimatore di massima verosimiglianza della media della popolazione si è rivelato essere la media del campione $\overline { { X } }$. Per mostrare che questa non è sempre la situazione, consideriamo il seguente esempio.

EXAMPLE 7.2g Estimating the Mean of a Uniform Distribution Supponiamo che $X _ { 1 } , \ldots , X _ { n }$ costituiscano un campione da una distribuzione uniforme su $( 0 , \theta )$ ), dove $\theta$ è sconosciuto. La loro densità congiunta è quindi

$$
f (x _ {1}, x _ {2}, \dots , x _ {n} | \theta) = \left\{ \begin{array}{l l} \frac {1}{\theta^ {n}} & 0 <   x _ {i} <   \theta , \quad i = 1, \dots , n \\ 0 & \text { otherwise } \end{array} \right.
$$

Questa densità è massimizzata scegliendo $\theta$ il più piccolo possibile. Poiché $\theta$ deve essere almeno grande quanto tutti i valori osservati $x _ { i } ,$, ne consegue che la scelta più piccola possibile di $\ni$ è uguale a max $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$. Pertanto, lo stimatore di massima verosimiglianza di $\cdot _ { \theta }$ è

$$
\hat {\theta} = \max (X _ {1}, X _ {2}, \ldots , X _ {n})
$$