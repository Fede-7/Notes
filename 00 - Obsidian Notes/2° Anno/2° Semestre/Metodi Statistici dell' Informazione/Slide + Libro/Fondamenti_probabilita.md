## Informazioni generali

• Docente: Marco Lops (IINF-03/A, ”Telecomunicazioni”). Perch`e? 

• Orario delle lezioni 

<table><tr><td>Giorno</td><td>Ora</td><td>Aula</td></tr><tr><td>Martedì</td><td>14,00 - 16,00</td><td>B-6</td></tr><tr><td>Giovedì</td><td>8,45 - 10,45</td><td>B-6</td></tr></table>

• Spiegazioni: Ci saranno degli orari uficiali, ma le interazioni potranno anche avvenire: 

† Al termine delle lezioni; 

† Su appuntamneto mediante Teams; 

† Su appuntamento dal vivo 

• Pertanto `e importante iscriversi al Team ”Calcolo delle Probabilit`a e Statistica”, il cui codice `e 8b1fgjq. 

• E anche opportuno iscriversi al corso sul sito web docenti.<sup>`</sup> 

## Organizzazione del corso

Il corso prevede 6 CFU (cio`e, 48 ore di lezione), tutte erogate frontalmente, eccezione fatta per lezioni di recupero, che saranno erogate a distanza. 

• Le lezioni saranno per circa due terzi (cio`e, 32 ore) di tipo teorico, mentre il restante terzo (cio`e, 16 ore) di tipo applicativo. 

• La verifica finale consister`a in una prova scritta, seguita da un colloquio orale. 

## Materiale didattico

• Slides preparate dal docente, scaricabili dal Team ”Metodi statistici per l’informazione” (codice team: 7p3013g); 

• Formati pdf delle lavagne - quando disponibili -, scaricabili dal Team ”Calcolo delle probabilit`a e statistica”; 

• Libri di testo consigliati: 

† Sulla Teoria della Probabilit`a: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/ecdaf8839691e0999f1b43f36d76f1bfee95ee104251fa6001323091b6b60edb.jpg)


† Sulla Statistica Inferenziale e descrittiva: 

Sheldon M. Ross,”Introduction to Probability and Statistics for Engineers and Scientists”, Elsevier. 

## Il corso di Calcolo delle Probabilit`a e Statisica

## Teoria della Probabilita

Analisi Combinatoria 

Variabili continue 

Prob. su spazi finiti 

Variabili multiple 

Variabili aleatorie discrete 

Processi Aleatori 

Informazione e sua misura Entropia Compressione Dati Mutua Informazione Divergenza 

Integrazione tra Teoria dell' Informazione Statistica Inferenziale 

## Elementi di Teoria della Probabilit`a

Marco Lops 

lops@unina.it 

https://docenti.unina.it/marco.lops 

## Definizioni

Esperimento: Operazione/azione - o insieme di operazioni/azioni - il cui esito d`a uno tra tanti risultati possibili; 

Spazio dei campioni - o spazio campione - comunemente denotato con Ω: insieme - non necessariamento numerico - di tutti i risultat possibili di un esperimento; 

Ω pu`o essere continuo o discreto: per il momento assumeremo che sia discreto, cio`e finito o numerabile. 

Evento: un qualunque sotto-insieme di Ω definito matematicamente da un insieme di suoi elementi e lessicalmente da una proposizione; 

Evento elementare: uno dei possibili |Ω| elementi di Ω. Si indica anche con $\omega \in \Omega$ 

Un evento `e univocamente individuato dagli elementi che lo compongono; 

Al contrario, la proposizione che lo definisce non `e unica. 

## Esempio #1 : lancio di una moneta

Lancio singolo: 

Spazio campione: $\Omega = \{ \mathsf { T e s t a } , { \mathsf { C r o c e } } \} = \{ T , C \} , | \Omega | = 2 ;$ 

Esempi di eventi: 

$$
A = \text {   Testa   } = \{T \} \quad B = \text {   Croce   } = \{C \} \quad \text {   Testa   o   Croce   } = A \cup B
$$

Lancio doppio 

Spazio campione: 

$$
\Omega = \{T T, T C, C T, C C \} = \{T, C \} \times \{T, C \} = \{T, C \} ^ {2}.
$$

Esempi di eventi: 

$$
A = \{\# \text { croci   dispari } \} = \{T C, C T \}
$$

$$
B = \{\text { N   e   s   s   u   n   a   c   r   o   c   e } \} = \{T T \}
$$

## Esempio # 2: lancio di un dado

Spazio campione: $\Omega = \{ 1 , 2 , 3 , 4 , 5 , 6 \} , | \Omega | = 6$ 

Esempi di eventi: 

A = Il risultato `e dispari = {1, 3, 5} B = Il risultato `e pari = {2, 4, 6} 

C = Il risultato `e dispari e ≤ 4 = {1, 3} D = Il risultato `e 6 = {6} 

Ognuno dei precedenti eventi pu`o essere associato a molte altre proposizioni che lo definiscono; 

Nota Bene: in entrambe le situazioni la proposizione che definisce un evento non `e univoca. 

## Esempio #3: Numero di pacchetti dati in coda ad un router

Spazio dei campioni: $\Omega = \{ 0 , 1 , 2 , 3 , . . . \} = \mathbb { N } _ { 0 } , | \Omega | = \infty .$ 

Esempi di eventi: 

A = {Ci sono meno di 6 pacchetti} = {0, 1, 2, 3, 4, 5} 

B = {# pacchetti dispari} = {1, 3, 5, . . . , (2k + 1), . . .} 

C = {# pacchetti dispari e minore di 6} = {1, 3, 5} = A ∩ B 

D = {# pacchetti pari o minore di $4 \} = \{ 1 , 2 , 3 , 6 , 8 , 1 0 , 1 2 , \ldots , 2 k , \ldots \}$ 

Dai precedenti esempi si vede che si possono definire nuovi eventi eseguendo delle operazioni tra altri eventi: le regole sono quelle classiche dell’insiemistica. 

## Qualche richiamo di insiemistica -1

Siano $\{ A _ { i } \} _ { i = 1 } ^ { M }$ M sotto-insiemi di un insieme $\Omega .$ . Definiamo: 

Unione tra due sotto-insiemi, $A _ { 1 } \cup A _ { 2 }$ , un sotto-insieme di $\Omega$ che contenga tutti gli elementi di $A _ { 1 }$ e quelli di $A _ { 2 }$ , ovviamente contando una sola volta quelli comuni; 

Complemento in $\Omega$ di un sotto-insieme $A _ { 1 }$ l’insieme $\overline { { A _ { 1 } } }$ che contiene tutti gli elementi di $\Omega$ che non appartengono a $A _ { 1 }$ ; ovviamente $\overline { { \Omega } } = \emptyset , \overline { { \overline { { A _ { 1 } } } } } = A _ { 1 } \mathrm { ~ e ~ } A _ { 1 } \cup \overline { { \overline { { A _ { 1 } } } } } = \Omega$ 

Intersezione tra due sotto-insiemi, $A _ { 1 } \cap A _ { 2 }$ , l’insieme che contiene tutti e soli gli elementi comuni a $A _ { 1 }$ e $A _ { 2 }$ 

Sottrazione tra due insiemi, $A _ { 1 } \setminus A _ { 2 }$ , l’insieme che contiene gl elementi di $A _ { 1 }$ che non appartengono a $A _ { 2 }$ . Ovviamente avremo: 

$$
A _ {1} \setminus A _ {2} = A _ {1} \cap \overline {{A _ {2}}}
$$

## Qualche richiamo di insiemistica -2

Relazione di De Morgan tra unione, intersezione e complementazione: 

$$
\overline {{A _ {1} \cup A _ {2}}} = \overline {{A _ {1}}} \cap \overline {{A _ {2}}} \Longrightarrow \overline {{\overline {{A _ {1}}} \cup \overline {{A _ {3}}}}} = A _ {1} \cap A _ {2}
$$

Propriet`a associativa di unione e intersezione: 

$$
\left(A _ {1} \cup A _ {2}\right) \cup A _ {3} = A _ {1} \cup \left(A _ {2} \cup A _ {3}\right) \quad \left(A _ {1} \cap A _ {2}\right) \cap A _ {3} = A _ {1} \cap \left(A _ {2} \cap A _ {3}\right)
$$

Propriet`a distributiva dell’unione rispetto all’intersezione e dell’intersezione rispetto all’unione: 

$$
A _ {1} \cup \left(\cap_ {i = 2} ^ {M} A _ {i}\right) = \cap_ {i = 2} ^ {M} \left(A _ {1} \cup A _ {i}\right)
$$

$$
A _ {1} \cap \left(\cup_ {i = 2} ^ {M} A _ {i}\right) = \cup_ {i = 2} ^ {M} \left(A _ {1} \cap A _ {i}\right)
$$

## Nomenclatura probabilistica

Ω si definisce evento certo; 

∅ si definisce evento impossibile; 

A e A si definiscono eventi complementari; 

Due eventi A e B tali che $A \cap B = \emptyset$ si definiscono incompatibili o mutuamente esclusivi; 

Se $A \subseteq B$ si dice che A implica B, cio`e il verificarsi di A implica che si verifichi B. 

## Qualche esempio

Con riferimento al lancio singolo di una moneta, T = {Risultato Testa} e C = {Risultato Croce} sono eventi complementari (e quindi mutuamente esclusivi), ${ \overline { { T } } } \cap { \overline { { C } } } = { \overline { { T \cup C } } } = { \overline { { \Omega } } } = \emptyset$ l’evento impossibile. 

Con riferimento a un lancio doppio, l’evento D = {Almeno una croce} `e incompatibile con {TT }, e pu`o essere espresso in vari modi: 

$$
D = \{C C, T C, C T \} = \overline {{T T}} = \Omega \setminus \{T T \} = \{C C \} \cup \{T C \} \cup \{C T \}
$$

Con riferimento all’esempio # 2 ed agli eventi l`ı definiti: A e B sono incompatibili (inoltre sono complementari, per cui $A \cup B = \Omega )$ , come incompatibili sono A e D e B e C ; inoltre C ⊆ A, cio`e C implica A. 

## Un esperimento semplice: lancio di un dado

Si supponga di lanciare un dado onesto n volte. Avremo quindi n risultati in $\Omega = \{ 1 , 2 , 3 , 4 , 5 , 6 \}$ : detto $n _ { j }$ il numero di volte (su n lanci) in cui il risultato `e i , ci si aspetta che, per n suficientemente grande, i valori di $n _ { j }$ siano all’incirca uguali, $\begin{array} { r } { n _ { i } \simeq \frac { n } { | \Omega | } = \frac { n } { 6 } } \end{array}$ . Definiamo i due sottoinsiemi $A = \{ 1 , 3 , 5 \} \in B = \{ 2 , 4 , 6 \}$ ; detti $ { n _ { A } } \in  { n _ { B } }$ il numero di prove in cui si verificano A e B rispettivamente avremo: 

$$
n _ {A} = n _ {1} + n _ {3} + n _ {5} \simeq n \frac {| A |}{| \Omega |} \quad n _ {B} = n _ {2} + n _ {4} + n _ {6} \simeq n \frac {| B |}{| \Omega |}
$$

Pertanto la frazione di volte in cui si verificano i due eventi si scrive: 

$$
\frac {n _ {A}}{n} \simeq \frac {| A |}{| \Omega |} = \frac {1}{2}
$$

$$
\frac {n _ {B}}{n} \simeq \frac {| B |}{| \Omega |} = \frac {1}{2}
$$

## Lancio di un dado due volte consecutive

L’esperimento ora consiste nel lanciare due volte consecutive il dado onesto e nel registrare gli esiti del primo e del secondo lancio. Lo spazio campione `e ora un insieme ordinato di 36 elementi: 

$$
\Omega = \{(1, 1), \dots , (1, 6), \dots (6, 1), \dots (6, 6) \}
$$

Per l’onest`a del dado, ci si attende che, per un numero di prove n suficientemente alto, ogni singola coppia esca all’incirca $\begin{array} { r } { \frac { n } { | \Omega | } = \frac { n } { 3 6 } } \end{array}$ volte. Sia A l’evento: 

$$
A = \{\text { Esce   almeno   un } 6 \} = \{(1, 6), \dots (5, 6), (6, 1), \dots (6, 6) \}
$$

Per lo stesso ragionamento condotto in precedenza, ci si aspetta che la frequenza con cui si verifica l’evento A in n prove sia: 

$$
\boxed {\frac {n _ {A}}{n} \simeq \frac {| A |}{| \Omega |} = \frac {1 1}{3 6}}
$$

## Spazi finiti con eventi elementari equivalenti

Sia Ω uno spazio dei campioni finito; 

Si assuma che tutti gli eventi elementari (cio`e, gli elementi di Ω) siano equivalenti, cio`e che non esista alcun elemento ”privilegiato” rispetto agli altri: questo equivale ad assumere che, eseguendo un numero suficientemente elevato di prove, ciascun evento elementare si verifichi un numero di volte approssimativamente uguale a quello di qualsiasi altro evento elementare; 

Detto $A \subseteq \Omega$ un qualsiasi evento, la frequenza di occorrenza di A gode della propriet`a: 

$$
f _ {n} (A) = \frac {n _ {A}}{n} \longrightarrow \frac {| A |}{| \Omega |}, \qquad n \to \infty
$$

Quindi per eventi equivalenti `e importante saper contare le cardinalit`a dei sotto-insiemi che definiscono gli eventi di interesse. 

La branca che si occupa di questo problema si chiama calcolo 

## Prodotti cartesiani

Si considerino k insiemi finiti, $A _ { 1 } , \ldots A _ { k }$ , non necessariamente distinti. 

Si definisce prodotto cartesiano $A ^ { ( k ) } = A _ { 1 } \times \ldots \times A _ { k }$ un insieme costituito dalle $k { \mathrm { - } } { \mathsf { p l e } }$ ordinate in cui il primo elemento appartenga a $A _ { 1 }$ , il secondo a $A _ { 2 }$ e cos`ı via. 

Siccome il primo elemento si pu`o scegliere in $| A _ { 1 } |$ | modi, il secondo $| A _ { 2 } |$ | e cos`ı via, avremo: 

$$
\boxed {\left| A ^ {(k)} \right| = \prod_ {i = 1} ^ {k} \left| A _ {i} \right|}
$$

Questa `e la relazione fondamentale del calcolo combinatorio, dalla quale molte altre formule di conteggio derivano. 

## k−ple ordinate senza ripetizione

Si supponga $A = \{ a _ { 1 } , \ldots a _ { n } \}$ 

Si vogliono contare le stringhe di lunghezza k di elementi di A in cu ogni elemento di A compaia una sola volta (cio`e, le ripetizioni non sono ammesse). 

Questo implica - nella formula precedente - che $\left| A _ { 1 } \right| = \left| A \right| = n ,$ $| A _ { 2 } | = n - 1 , \ldots , | A _ { k } | = n - k + 1$ 

Pertanto il richiesto numero `e 

$$
\left| A ^ {(k)} \right| = n (n - 1) (n - 2) \cdot \dots \cdot (n - k + 1) = \prod_ {i = 0} ^ {k - 1} (n - i)
$$

## k−ple ordinate con ripetizione

Si supponga $A = \{ a _ { 1 } , \ldots a _ { n } \}$ 

Si vogliono contare le stringhe di lunghezza k di elementi di A in cu ogni elemento di A possa ripetersi (cio`e le ripetizioni sono ammesse). 

Questo implica - nella formula precedente - che $| A _ { 1 } | = | A _ { 2 } | = \ldots = | A _ { k } | = | A | = n ,$ 

Pertanto il richiesto numero `e 

$$
\left| A ^ {(k)} \right| = n ^ {k}
$$

Esempio: il numero delle k−ple binarie `e il numero di k−ple ordinate con ripetizione prese dall’insieme di cardinalit`a due {0, 1} `e $2 ^ { k }$ 

## Permutazioni

Un caso particolare - ma molto rilevante - del calcolo precedente `e quando k = n. La domanda cui si vuole rispondere `e: 

Dato un insieme di n elementi, quante n−ple ordinate si possono formare? 

Risposta: E un caso speciale di enumerazione di<sup>`</sup> k−ple quando k = n, cio`e: 

# permutazioni di n elementi = n(n − 1) · . . . · 1 = n! 

Questo ci conduce immediatamente al concetto di combinazioni. 

## Combinazioni $( \overline { { G } } _ { m } ) _ { s } ^ { s }$

Le combinazioni $C _ { n , k }$ di ”n elementi su $k$ posti” `e il numero di $k { \mathrm { - } } { \mathsf { p l e } }$ non ordinate che si possono formare con n elementi (cio`e, il numero di sottoinsiemi di $\Omega$ di cardinalit`a $k )$ 

Pertanto, le $k !$ permutazioni di una stessa $k { \mathrm { - } } { \mathsf { p l a } }$ ordinata ”collassano” in un’unica combinazione. Questo comporta: 

$$
C _ {n, k} = \frac {n (n - 1) \cdot \ldots (n - k + 1)}{k !} = \frac {n !}{k ! (n - k) !} = \binom{n}{k}
$$

dove $\left( \begin{array} { l } { n } \\ { k } \end{array} \right)$ `e il coeficiente binomiale $( n , k )$ 

## Problema

Si considerino le 52 carte francesi con i quattro semi (Cuori (C), Fiori (F), Picche (P), Quadri (Q)). Si supponga di estrarre dal mazzo k carte, senza reinserirle dopo ogni estrazione. Si calcolino: 

a Il numero di possibili quaterne ordinate; 

b Il numero di quaterne non ordinate; 

c Il numero di quarterne (C,F,P,Q); 

d Il numero di cinquine non ordinate in cui compaiano esattamente due assi. 

a Si ponga $k = 4 \mathrm { ~ e ~ } n = 5 2$ nelle formula che conta le $k { \mathrm { - } } { \mathsf { p l e } }$ ordinate senza ripetizione. Si ha 

$$
5 2 \cdot 5 1 \cdot 5 0 \cdot 4 9 = 6 4 9 7 4 0 0
$$

b Le 4! permutazioni di ogni quaterna collassano in un’unica quaterna, per cui si ha $\begin{array} { r } { \frac { \bar { 5 } 2 \cdot 5 1 \cdot 5 0 \cdot 4 9 } { 4 ! } = \frac { 6 4 9 7 4 0 0 } { 2 4 } = 2 7 0 7 2 5 } \end{array}$ 

c Si usi la formula sulle k−ple ordinate per $| \Omega _ { i } | = 1 3 \ \mathsf { e }$ $k = 4$ , per cui si ha $1 3 ^ { 4 } = 2 8 5 6 1$ 

d Gli assi sono 4 per cui si possono combinare in ${ \left( \begin{array} { l } { 4 } \\ { 2 } \end{array} \right) } = 6$ modi. Le altre 48 carte possono combinarsi sui residui tre posti in ${ \left( \begin{array} { l } { 4 8 } \\ { 3 } \end{array} \right) } = 1 7 2 9 6$ modi, per cui abbiamo 

$$
\binom{4}{2} \binom{4 8}{3} = 6 9 1 8 4
$$

## Insieme delle parti di un insieme finito

Si consideri un insieme A con n elementi. 

L’insieme delle parti ${ \mathcal { P } } ( A )$ di $A \ \dot { \mathsf { e } }$ l’insieme di tutti i possibil sottoinsiemi di A. 

Negli insiemi ovviamente l’ordinamento non conta, per cui il numero di sottoinsiemi k−dimensionali di A `e 

$$
\binom{n}{k}
$$

Siccome tanto l’insieme vuoto (0-dimensionale) quanto A (n−dimensionale) sono sottoinsiemi di $A ,$ , avremo: 

$$
| \mathcal {P} (A) | = \sum_ {k = 0} ^ {n} \binom{n}{k} = 2 ^ {n}
$$

## Prove ripetute e conteggio dei successi

Si consideri una stringa binaria di lunghezza n che abbia k valori ”1” e (n − k) valori ”zero”. Si vuole contare quante stringhe di lunghezza n abbiano $k " 1 "$ e $( n - k ) \ " 0 ^ { \prime \prime }$ 

Si parta da una stringa qualsiasi contenente k uno e n − k ”zero” in date posizioni; 

Le permutazioni di questa stringa sono n!; 

Tuttavia tutte le k! permutazioni degli uno sulle k posizioni occupate gi`a da ”1” nella stringa originaria sono ineficaci (cio`e, portano alla stessa sequenza iniziale), per cui le permutazioni al netto di queste k! sono n!/k!. 

Analogamente sono ineficaci le (n − k)! permutazioni degli ”0” sulle posizioni che gi`a occupavano nella stringa iniziale, che porta in conto un’ulteriore divisione per $( n - k ) !$ !. 

In conclusione il numero richesto `e $\left( \begin{array} { l } { n } \\ { k } \end{array} \right)$ 

## Dalla frequenza alla probabilit`a

Dato uno spazio dei campioni discreto $\Omega$ e un suo qualunque sottoinsieme (o evento) A si definisce probabilit`a che occorra A i limite della frequenza di occorrenza di A quando il numero di esperimenti - o prove - tende all’infinito, cio`e: 

$$
\mathbb {P} (A) = \lim _ {n \rightarrow \infty} \frac {n _ {A}}{n}
$$

A questo punto il concetto di spazio finito con eventi elementari equivalenti diviene quello di spazio finito con eventi elementari equiprobabili. 

Si ha di conseguenza che, per uno spazio finito a eventi elementar equiprobabili vale la relazione generale: 

$$
\mathbb {P} (A) = \frac {| \Omega_ {A} |}{| \Omega |}
$$

dove $\Omega _ { A }$ contiene tutti gli eventi che comportano il verificarsi di A. 

## Esempio: I punteggi del Poker

Un giocatore estrae (senza reinserimento) 5 carte da un mazzo di carte da poker (contenente le carte dal 7 all’asso, per un totale di 8 × 4 = 32 carte). 

Calcolare le seguenti probabilit`a: 

a Coppia di assi e coppia qualsiasi; 

b Almeno tre assi; 

c Un tris qualsiasi (ma non un full n`e un poker); 

d Colore di picche o colore qualsiasi. 

## Soluzione - [a]

Lo spazio dei campioni `e -per tutti i casi - l’insieme di tutte le cinquine di elementi (ovviamente distinti), ma non importa l’ordine, per cui: 

$$
| \Omega | = \binom{3 2}{5} = \frac {3 2 !}{5 ! 2 7 !} = 2 0 1 3 7 6
$$

Sia $C _ { 2 } \subseteq \Omega$ l’insieme delle cinquine con due assi. Quindi due dei cinque post sono occupati da due dei 4 assi, mentre le altre 28 carte sono qualsiasi (questo include nel calcolo anche i full e le doppie coppie). Avremo: 

$$
| C _ {2} | = \binom{4}{2} \binom{2 8}{3} = 1 9 6 5 6 \to \mathbb {P} \{C _ {2} \} = 0. 0 9 7
$$

Volendo escludere la possibilit`a di punteggi pi`u alti della coppia d’assi, avremo che - ferme restando le due posizioni occupate da due assi - la terza pu`o essere occupata solo da 28 carte, la quarta da 24 e la quinta da 20, per cui: 

$$
\left| C _ {2} ^ {\prime} \right| = \binom{4}{2} \frac {2 8 \times 2 4 \times 2 0}{3 !} = 1 3 4 4 0 \rightarrow \mathbb {P} \{C _ {2} \} = 0. 0 6 7
$$

Se la coppia pu`o essere qualsiasi le precedenti probabilit`a vanno moltiplicate per 8. 

## Soluzione - [b]

Sia $C _ { 3 } \subseteq \Omega$ l’insieme di cinquine che contengono esattamente tre assi e quelle che ne contengono 4. 

Avremo: 

$$
\left| C _ {3} \right| = \overbrace {\binom{4}{3} \binom{2 8}{2}} ^ {3 \text {assi}} + \overbrace {\binom{4}{4} \binom{2 8}{1}} ^ {4 \text {assi}} = 1 5 1 2 + 2 8 = 1 5 4 0
$$

Siccome lo spazio dei campioni `e inalterato, la probabilit`a richiesta vale 

$$
\mathbb {P} \{C _ {3} \} = \frac {1 5 4 0}{2 0 1 3 7 6} = 0. 0 0 7 6
$$

## Soluzione - [c]

Sia $C _ { 3 } ^ { \prime } \subseteq \Omega$ l’insieme che contiene tutte le cinquine che diano un tris e le altre due carte diverse. Indichiamo on $C _ { 3 } ^ { \prime } ( 7 )$ l’insieme delle cinquine che contengono esattamente un tris di sette. Avremo: 

$$
\left| C _ {3} ^ {\prime} \right| = 8 \left| C _ {3} ^ {\prime} (7) \right|
$$

Per calcolare $\big | C _ { 3 } ^ { \prime } ( 7 ) \big |$ , sappiamo che 3 posizioni sono occupate da un sette (il che pu`o avvenire in ${ \left( \begin{array} { l } { 4 } \\ { 3 } \end{array} \right) } = 4 { \mathrm { ~ m o d i } } )$ , la quarta carta pu´o essere scelta in 28 modi e la quinta in 24. Siccome l’ordine non conta avremo: 

$$
\left| C _ {3} ^ {\prime} (7) \right| = 4 \frac {2 8 \times 2 4}{2} = 1 3 4 4 \rightarrow \mathbb {P} \left\{C _ {3} ^ {\prime} (7) \right\} = \frac {1 3 4 4}{2 0 1 3 7 6} = 0. 0 0 6 7
$$

La probabilit`a richiesta vale allora 

$$
\frac {8 \times 4 \times 2 8 \times 2 4}{2 0 1 3 7 6} = 0. 0 5 3
$$

## Soluzione - [d]

0 Sia $C _ { P } \subseteq \Omega$ l’insieme di tutte le possibili cinquine di carte di picche. Poich`e ci sono $^ 8$ carte di picche da distribuire su 5 posti con ordine inessenziale, avremo (N.B. Questo include le scale reali): 

$$
| C _ {P} | = \binom{8}{5} = 5 6 \to \mathbb {P} \{C _ {P} \} = \frac {5 6}{2 0 1 3 7 6} = 0. 0 0 0 2 7
$$

Pertanto la probabilit`a di un colore qualsiasi vale 

$$
\mathbb {P} \{\text { colore } \} = 0. 0 0 1 1
$$

Se vogliamo escludere le scale reali, dobbiamo togliere dalle cinquine tutte quelle che vedono le carte consecutive. Esistono 5 scale reali per ogni seme (dall minima, (A,7,8,9,10) alla massima $( 1 0 , \mathsf { J } , \mathsf { Q } , \mathsf { K } , \mathsf { A } ) )$ ), per cui in questo caso: 

$$
\left| C _ {P} \right| = 5 6 - 5 = 5 1 \rightarrow \mathbb {P} \left\{C _ {P} \right\} = \frac {5 1}{2 0 1 3 7 6} = 0. 0 0 0 2 5 \rightarrow \mathbb {P} \{\text { colore } \} = 0. 0 0 1
$$

## Frequenza di occorrenza e probabilit`a su Spazi finiti

Sia Ω uno spazio campione discreto (cio`e, finito o numerabile); 

Rimuoviamo ora l’ipotesi che gli eventi elementari siano equiprobabili; 

La definizione di probabilit`a data in precedenza vale ancora. In particolare: 

a $A \subseteq \Omega \ { \dot { \mathsf { e } } }$ un evento e si conducono n esperimenti; 

b Sia $\begin{array} { r } { n _ { A } = n _ { A } ( n ) } \end{array}$ il numero di volte in cui A si verifica; 

c Frequenza di occorrenza e probabilit`a si definiscono: 

$$
f _ {n} (A) = \frac {n _ {A}}{n} \quad \mathbb {P} (A) = \lim _ {n \rightarrow \infty} f _ {n} (A) = \lim _ {n \rightarrow \infty} \frac {n _ {A}}{n}
$$

d La principale diferenza con quanto visto prima `e che ora non `e pi`u vero in generale che $n _ { A } \simeq n | { \cal A } |$ 

Detto in altre parole, quando gli eventi elementari non sono equiprobabili, un evento $A \subseteq \Omega$ ha una misura diversa da quella - ordinaria - data dal numero de suoi elementi distinti; 

Quindi due eventi, $A \subseteq \Omega \mathrm { ~ e ~ } B \subseteq \Omega$ di uguale cardinalit`a $( | A | = | B | )$ possono avere ”pesi” (cio`e misure) diverse e le tecniche di conteggio non sono pi`u utili ai fini del calcolo della probabilit`a. 

## Un esempio: il dado truccato

Supponiamo di avere - in analogia all’esempio $\# 2$ - un dado, ma questa volta truccato in modo che 5 volte su 6 esca il risultato 1. Si lanci il dado un’unica volta, per cu 

$$
\Omega = \{1, 2, 3, 4, 5, 6 \}
$$

Sia A = {Il risultato `e pari} = {2, 4, 6} e B = {Il risultato `e dispari} = {1, 3, 5}. Se $n _ { j }$ `e in numero di volte (su n prove) in cui esce il risultato $i ,$ avremo: 

$$
\sum_ {i = 1} ^ {6} n _ {i} = n, n _ {1} \simeq 5 \sum_ {i = 2} ^ {6} n _ {i} \quad \forall i \neq 1 \rightarrow \frac {n _ {1}}{n} = f _ {n} (1) = 5 \sum_ {i = 2} ^ {6} f _ {n} (i)
$$

$$
\mathbb {P} (\{1 \}) = 5 \sum_ {i = 2} ^ {6} \mathbb {P} (\{i \} _ {i \neq 1}) \quad \text { poichè } \sum_ {i = 1} ^ {6} f _ {n} (i) = 1 \to \sum_ {i = 1} ^ {6} \mathbb {P} (\{i \}) = 1
$$

$$
\mathbb {P} (\{1 \}) = \frac {5}{6} \qquad \mathbb {P} (\{i \} _ {i = 2, \ldots 6}) = \frac {1}{3 0}
$$

Quindi: 

$$
f _ {n} (A) = \frac {n _ {2} + n _ {4} + n _ {6}}{n} \rightarrow \frac {3}{3 0} = \frac {1}{1 0} \quad f _ {n} (A) = \frac {n _ {1} + n _ {3} + n _ {5}}{n} \rightarrow \frac {5}{6} + \frac {2}{3 0} = \frac {9}{1 0}
$$

laddove con tecniche di conteggio avremmo trovato che, essendo $| A | = | B | = | \Omega | / 2$ , le due probabilit`a sarebbero valse $_ { 1 / 2 . }$ . In altre parole, B ha ora una misura molto maggiore di A. 

## Alcune propriet`a della frequenza di occorrenza e della probabilit`a - 1

Siano $A \subseteq \Omega \mathrm { ~ e ~ } B \subseteq \Omega$ due eventi; 

Siano $n _ { A } = n _ { A } ( n ) \mathrm { ~ e ~ } n _ { B } = n _ { B } ( n )$ il numero di occorrenze su n prove, $f _ { n } ( A ) ~ \mathfrak { e }$ $f _ { n } ( B )$ le relative frequenze, e $\mathbb { P } ( A ) \thinspace \thinspace \mathbf { e } \thinspace \mathbb { P } ( B )$ i rispettivi limiti (cio`e le probabilit`a). 

Valgono le seguenti propriet`a: 

a Eventi complementari: 

$$
f _ {n} (\overline {{A}}) = \frac {n - n _ {A}}{n} = 1 - f _ {n} (A) \Longrightarrow \mathbb {P} (\overline {{A}}) = 1 - \mathbb {P} (A)
$$

## b Sub-additivit`a

$$
f _ {n} (A \cup B) = \frac {n _ {A U B}}{n} = \frac {n _ {A} + n _ {B} - n _ {A \cap B}}{n} = f _ {n} (A) + f _ {n} (B) - f _ {n} (A \cap B) \rightarrow
$$

$$
\mathbb {P} (A \cup B) = \mathbb {P} (A) + \mathbb {P} (B) - \mathbb {P} (A \cap B)
$$

Infatti, se A e B non sono incompatibili sommare semplicemente $n _ { A }$ e n equivarrebbe a contare due volte le occorrenze di entrambi (cio`e le occorrenze di $A \cap B )$ , il che spiega il termine sottrattivo 

## Alcune propriet`a della frequenza di occorrenza e della probabilit`a - 2

c Sottrazione tra insiem 

$$
f _ {n} (A \setminus B) = f _ {n} (A \cap \overline {{B}}) = \frac {n _ {A} - n _ {A \cap B}}{n} = f _ {n} (A) - f _ {n} (A \cap B) \rightarrow
$$

$$
\mathbb {P} (A \setminus B) = \mathbb {P} (A) - \mathbb {P} (A \cap B)
$$

Infatti, dovendosi verificare A ma non B, bisogna sottrarre a $n _ { A }$ il numero di esperimenti in cui si verificano entrambi, $n _ { A \cap B }$ 

d Evento certo ed evento impossibile. Banalmente: 

$$
f _ {n} (\Omega) = \frac {n}{n} = 1 \rightarrow \mathbb {P} (\Omega) = 1 \rightarrow \mathbb {P} (\emptyset) = \mathbb {P} (\overline {{\Omega}}) = 0
$$

Frequenze e probabilit`a condizionate 

Siano A e B due eventi che occorrano $n _ { A } \in n _ { B }$ volte su n esperimenti. Definiamo ora la frequenza di occorrenza di A condizionata a $B \texttt { - } f _ { n } ( A | B )$ - il rapporto tra il numero di prove in cui si verificano entramb $\left( n _ { A \cap B } \right)$ e il numero di volte in cui si verifica solo B, cio`e, formalmente: 

$$
f _ {n} (A | B) = \frac {n _ {A \cap B}}{n _ {B}} = \frac {n _ {(A \cap B)}}{n} \frac {n}{n _ {B}} = \frac {f _ {n} (A \cap B)}{f _ {n} (B)} \to \mathbb {P} (A | B) = \frac {\mathbb {P} (A \cap B)}{\mathbb {P} (B)}
$$

In altre parole, restringiamo il nostro campione di analisi solo agli n risultati che abbiano condotto al verificarsi di B. Ovviamente: 

$$
\mathbb {P} (B | A) = \frac {\mathbb {P} (A \cap B)}{\mathbb {P} (A)} \Leftrightarrow \mathbb {P} (A \cap B) = \mathbb {P} (B | A) \mathbb {P} (A) = \mathbb {P} (A | B) \mathbb {P} (B)
$$

L’ultima relazione prende anche il nome di legge della probabilit`a composta. 

## Legge della probabilit`a totale

Un’importante conseguenza della definizione di probabilit`a condizionata `e la legge della probabilit`a totale. 

Sia $\{ E _ { i } \} _ { i = 1 } ^ { M }$ una partizione di $\Omega _ { \ i }$ , cio`e: 

$$
\cup_ {i = 1} ^ {M} E _ {i} = \Omega \quad E _ {i} \cap E _ {j} = \emptyset \forall i \neq j
$$

Se $A \subseteq \Omega$ , avremo allora: 

$$
\mathbb {P} (A) = \mathbb {P} (A \cap \Omega) = \mathbb {P} (A \cap \cup_ {i = 1} ^ {M} E _ {i}) = \mathbb {P} \left(\cup_ {i = 1} ^ {M} A \cap E _ {i}\right)
$$

Essendo $E _ { i } \cap E _ { j } = \emptyset$ , avremo ovviamente che $( A \cap E _ { i } ) \cap ( A \cap E _ { j } ) = \emptyset$ , per cui: 

$$
\boxed {\mathbb {P} (A) = \sum_ {i = 1} ^ {M} \mathbb {P} \left(A \cap E _ {i}\right) = \sum_ {i = 1} ^ {M} \mathbb {P} \left(A | E _ {i}\right) \mathbb {P} \left(E _ {i}\right)}
$$

## Eventi Indipendenti

Due eventi, $A \subseteq \Omega \mathrm { ~ e ~ } B \subseteq \Omega$ si dicono indipendenti quando il verificarsi di uno non ha nessuna influenza sul verificarsi o meno dell’altro. 

In altre parole, due eventi $A \in B$ sono indipendenti se (e solo se) $\begin{array} { r } { f _ { n } ( A | B ) = f _ { n } ( A ) \mathrm { ~ e ~ } f _ { n } ( B | A ) = f _ { n } ( B ) . } \end{array}$ 

Pertanto, sfruttando la legge della probabilit`a composta (o, equivalentemente, la definizione di probabilit`a condizionata) avremo che, se $A \in B$ sono indipendenti: 

$$
f _ {n} (A \cap B) = f _ {n} (A) f _ {n} (B) \Leftrightarrow \mathbb {P} (A \cap B) = \mathbb {P} (A) \mathbb {P} (B)
$$

Esempio: Lancio di un dado onesto due volte consecutive. 

$$
\mathbb {P} (\{i, j \}) = \mathbb {P} (\{i \}) \mathbb {P} (\{j \}) = \frac {1}{6} \frac {1}{6} = \frac {1}{3 6}
$$

## L’approccio assiomatico alla teoria della probabilit`a

Si consideri una famiglia di sottoinsiemi di Ω, sia essa $\mathcal { E } = \{ A _ { 1 } , . . . , A _ { N } \}$ 

Si assuma che la famiglia E soddisfi le seguenti due propriet`a: 

† Essa `e chiusa rispetto all’unione, cio`e: 

$$
\text { se } \quad A _ {1} \in \mathcal {E}, A _ {2} \in \mathcal {E} \quad \Rightarrow A _ {1} \cup A _ {2} \in \mathcal {E};
$$

† Essa `e chiusa rispetto alla complementazione, cio`e: 

$$
\mathrm{se} \quad A _ {1} \in \mathcal {E} \quad \Rightarrow \overline {{A _ {1}}} \in \mathcal {E};
$$

Sotto le precedenti condizioni, E si definisce un’Algebra di sotto-insiemi di E, o algebra di eventi. 

Se la collezione E contiene un’infinit`a (numerabile) di elementi, allora E si definisce una σ−algebra se, oltre ad essere chiusa rispetto alla complementazione e all’unione, `e anche chiusa rispetto all’unione di un’infinit`a numerabile di suoi elementi. 

## Propriet`a delle Algebre

Se A, $B \in { \mathcal { E } }$ allora $A \cap B \in { \mathcal { E } }$ . Infatti, per la relazione di De Morgan abbiamo: 

$$
A \cap B = \overline {{\overline {{A}} \cup \overline {{B}}}} \in \mathcal {E} \quad \text { poichè } (\overline {{A}}, \overline {{B}}) \in \mathcal {E}
$$

Se A, $B \in { \mathcal { E } }$ allora $A \setminus B \in { \mathcal { E } }$ . Infatti: 

$A \setminus B = A \cap { \overline { { B } } } \in { \mathcal { E } }$ per la precedente propriet`a 

Se A `e un evento qualsiasi, allora la minima algebra che contiene A `e $\mathcal { E } = \{ A , \overline { { A } } , \Omega , \emptyset \}$ . Infatti: 

† A deve essere elemento di E per la chiusura rispetto alla complementazione; 

† $A \cup { \overline { { A } } } = \Omega$ deve essere un elemento di E per la propriet`a di chiusura rispetto all’unione e $\varnothing = { \overline { { \Omega } } }$ deve esso stesso appartenervi per la chiusura rispetto alla complementazione. 

## Spazi di probabilit`a

Si definisce legge di probabilit`a una funzione con dominio E e co-dominio [0, 1], cio`e: 

$$
\mathbb {P}: A \in \mathcal {E} \longrightarrow \mathbb {P} (A) \in [ 0, 1 ]
$$

che soddisfi i seguenti Assiomi di Kolmogorov: 

1. Non negativit`a, cio`e $\mathbb { P } ( A ) \geq 0 \ \forall A \in \mathcal { E }$ 

2. Normalizzazione, cio`e $\mathbb { P } ( \Omega ) = 1$ 

3. Sub-additivit`a, cio`e: 

A e B incompatibili $( A \cap B = \emptyset ) \ \Longrightarrow \mathbb { P } ( A \cup B ) = \mathbb { P } ( A ) + \mathbb { P } ( B )$ 

3a Numerabile additivit`a. Se $\{ B _ { n } \} _ { n \in \mathbb { N } } \ \dot { \textbf { e } }$ una collezione numerabile di eventi incompatibili, allora: 

$$
\mathbb {P} \left(\cup_ {n = 1} ^ {\infty} B _ {n}\right) = \sum_ {n = 1} ^ {\infty} \mathbb {P} \left(B _ {n}\right)
$$

La terna $( \Omega , { \mathcal { E } } , \mathbb { P } )$ si definisce Spazio di Probabilit`a. 

## Propriet`a delle leggi di probabilit`a (qualche esempio)

## † Eventi complementari:

$$
\mathbb {P} (\Omega) = \mathbb {P} (A \cup \overline {{A}}) = \mathbb {P} (A) + \mathbb {P} (\overline {{A}}) = 1 \implies \mathbb {P} (\overline {{A}}) = 1 - \mathbb {P} (A)
$$

† Sottrazione tra insiemi: 

$$
A = A \cap \Omega = A = A \cap (B \cup \overline {{B}}) = (A \cap B) \cup (A \cap \overline {{B}})
$$

Siccome $( A \cap B ) \in ( A \cap { \overline { { B } } } )$ sono incompatibili, allora ritroviamo la propriet`a $\mathbb { P } ( A \cap { \overline { { B } } } ) = \mathbb { P } ( A \setminus B ) = \mathbb { P } ( A ) - \mathbb { P } ( A \cap B )$ 

† Unione di eventi non incompatibil $( A \cap B \neq \varnothing )$ . Osserviamo preliminarmente che $A = A \cup \left( B \cap { \overline { { A } } } \right)$ , Per cu 

$$
\mathbb {P} (A) = \mathbb {P} (A) + \underbrace {\mathbb {P} (B \cap \overline {{A}})} _ {= \mathbb {P} (B) - \mathbb {P} (A \cap B)} = \mathbb {P} (A) + \mathbb {P} (B) - \mathbb {P} (A \cap B)
$$

## Esercizio

Dimostrare che se due eventi (A, B) sono indipendenti, lo sono anche i loro compementari. 

## Svolgimento

Dire che A e B sono indipendenti significa che $\mathbb { P } \left( A \cap B \right) = \mathbb { P } ( A ) \mathbb { P } ( B )$ per cui dobbiamo dimostrare che $\mathbb { P } \left( { \overline { { A } } } \cap { \overline { { B } } } \right) = \mathbb { P } ( { \overline { { A } } } ) \mathbb { P } ( { \overline { { B } } } )$ 

Ricordiamo che la relazione di De Morgan stabilisce che ${ \overline { { A } } } \cap { \overline { { B } } } = { \overline { { A \cup B } } }$ Pertanto avremo che 

$$
\mathbb {P} (\overline {{A}} \cap \overline {{B}}) = 1 - \mathbb {P} (A \cup B)
$$

Avremo quindi 

$$
\mathbb {P} \left(\overline {{A}} \cap \overline {{B}}\right) = 1 - \mathbb {P} (A) - \mathbb {P} (B) + \overbrace {\mathbb {P} (A \cap B)} ^ {= \mathbb {P} (A) \mathbb {P} (B)} =
$$

$$
1 - \mathbb {P} (A) - \mathbb {P} (B) (1 - \mathbb {P} (A)) = \underbrace {(1 - \mathbb {P} (A))} _ {\mathbb {P} (\overline {{A}})} \underbrace {(1 - \mathbb {P} (B))} _ {\mathbb {P} (\overline {{B}})} = \mathbb {P} (\overline {{A}}) \mathbb {P} (\overline {{B}})
$$

Si supponga che Ω sia un insieme numerico: in questo caso il risultato dell’esperimento `e evidentemente un numero; 

Esistono tuttavia molti casi di interesse (si pensi al lancio di una moneta o all’estrazione di carte da un mazzo) in cui $\Omega$ non `e un insieme numerico. 

Tuttavia, Ω pu`o sempre essere messo in corrispondenza con un insieme numerico discreto, secondo una corrispondenza: 

$$
X: \omega \in \Omega \rightarrow X (\omega) \in \mathcal {X} \subseteq \mathbb {R}
$$

La funzione $X ( \omega )$ si chiama variabile aleatoria. Il codominio di $X ( \omega )$ (necessariamente discreto) prende il nome di alfabeto di X . 

Gli eventi elementari ora divengono $X ( \omega ) = x , x \in \mathcal { X }$ 

le loro frequenze e probabilit`a saranno $f _ { n } ( x ) \in \mathbb { P } ( X = x )$ , rispettivamente 

Esempio: lancio singolo/doppio di una moneta onesta. 

singolo 

$$
X: \omega \in \{T, C \} \to X (\omega) \in \{0, 1 \}
$$

$$
\mathbb {P} (X = 0) = \mathbb {P} (X = 1) = \frac {1}{2}
$$

doppio 

$$
X: \omega \in \{T, C \} ^ {2} \rightarrow X (\omega) \in \{0, 1, 2, 3 \}
$$

$$
\mathbb {P} (X = i) = \frac {1}{4} \quad \forall i
$$

## La pmf/DF/pdf di una variabile aleatoria

La sequenza di numeri $\mathbb { P } ( X = x ) = p _ { X } ( x ) , x \in \mathcal { X }$ si chiama probability mass function (pmf) o Distribution Function (DF) o probability density function (pdf) della variabile aleatoria X . 

Ovviamente, date le propriet`a della probalilit`a: 

$$
p _ {X} (x) = \lim _ {n \rightarrow \infty} \frac {n _ {x}}{n} \rightarrow p _ {X} (x) \geq 0 \quad \sum_ {x \in \mathcal {X}} p _ {X} (x) = 1
$$

dove $n _ { x } = n _ { \{ X = x \} }$ rappresenta il numero di occorrenze dell’evento $\{ X = x \}$ 

Esempio: $\{ \mathcal { X } \} = \{ 1 , 2 , 3 , 4 \}$ . Pu`o $\bigl ( \textstyle { \frac { 1 } { 2 } } , \frac { 1 } { 4 } , \frac { 1 } { 8 } , \frac { 1 } { 8 } \bigr )$ essere una pdf? 

$$
p _ {X} (x) \geq 0 \quad \sum_ {x \in \mathcal {X}} p _ {X} (x) = \sum_ {i = 1} ^ {4} p _ {X} \left(x _ {i}\right) = \sum_ {i = 1} ^ {4} \mathbb {P} (X = i) = 1
$$

quindi la risposta `e s`ı! 

Per come `e stata definita, la probabilit`a `e una funzione definita su un insieme di sottoinsiemi di $\Omega$ e a valori in [0, 1], cio`e: 

$$
\mathbb {P}: A \subseteq \Omega \to \mathbb {P} (A) \in [ 0, 1 ]
$$

In realt`a, bisognerebbe strutturare $\Omega$ in modo opportuno (cio`e introdurre un’algebra d eventi), ma sorvoliamo. 

Il punto `e che, quando si passa alle variabili aleatorie la notazione corretta sarebbe: 

$$
\text { Probabilità } (X = x) = \mathbb {P} (\omega \in \Omega : X (\omega) = x)
$$

Per contro, noi usiamo la notazione semplificata $\mathbb { P } ( X = x )$ , talvolta ”complicandola” nella forma $\mathbb { P } ( \{ X = x \} )$ , che evoca che a rigore ci riferiamo a un insieme di punti d $\Omega .$ . Useremo queste notazioni intercambiabilmente ogni volta che non ci sia il pericolo di generare equivoci. 

## La media campionaria

Una variabile aleatoria X si dice caratterizzata se `e assegnata la sequenza de $| \mathcal { X } |$ valori della sua pmf; 

Esistono caratterizzazioni meno precise che sono spesso utili: una di queste `e la media campionaria, 

Si supponga di avere la variabile aleatoria $X ( \omega )$ e si supponga di compiere n esperimenti; 

La collezione dei risultati sar`a $[ X ( \omega _ { 1 } ) , \dots , X ( \omega _ { n } ) ]$ 

Una scelta naturale per avere un’idea del comportamento di $X ( \omega ) \ { \dot { \mathsf { e } } }$ eseguire la media campionaria delle misure, cio`e: 

$$
\boxed {\overline {{X _ {n}}} = \frac {1}{n} \sum_ {i = 1} ^ {n} X (\omega_ {i})}
$$

## La media statistica

Riconsideriamo la media campionaria 

$$
\overline {{X _ {n}}} = \frac {1}{n} \sum_ {i = 1} ^ {n} X (\omega_ {i})
$$

Naturalmente, siccome $X ( \omega _ { i } ) \in \mathcal { X } = \{ x _ { 1 } , . . . , x _ { M } \}$ , al crescere di n avremo che $X ( \omega )$ assumer`a $n _ { 1 }$ volte il valore $x _ { 1 } , \ n _ { 2 }$ il valore $x _ { 2 }$ e cos`ı via (il caso $M = \infty$ va trattato come caso limite). Quindi, pe $n  \infty ;$ 

$$
\boxed {\overline {{X _ {n}}} = \frac {1}{n} \sum_ {i = 1} ^ {M} n _ {i} x _ {i} = \sum_ {i = 1} ^ {M} x _ {i} f _ {n} (x _ {i}) \rightarrow \sum_ {i = 1} ^ {M} x _ {i} \mathbb {P} (X = x _ {i}) = \sum_ {i = 1} ^ {M} x _ {i} p _ {X} (x _ {i}) \stackrel {\text { def }} {=} \mathbb {E} [ X ]}
$$

dove ricordiamo che $\begin{array} { r } { f _ { n } ( x _ { i } ) = \frac { n _ { \{ X = x _ { i } \} } } { n } } \end{array}$ 

La quantit`a $\mathbb { E } \left[ X \right]$ si definisce media statistica della variabile aleatoria X . 

## Un esempio: il conteggio Bernoulliano - 1

Consideriamo il lancio per N volte di una moneta; 

La moneta d`a un risultato ”T” (testa) con frequenza che tende a $p < 1 \mathrm { ~ e ~ } ^ { \prime \prime } \mathsf { C } ^ { \prime \prime }$ (croce) con frequenza che tende a $q = 1 - p ;$ 

I lanci ovviamente sono indipendenti, nel senso che l’esito di ogni lancio non dipende da quelli precedenti e successivi; 

Quindi lo spazio campione `e l’insieme delle N-ple del tipo: 

$$
\underbrace {(C , C , T , T , C , \dots\dotsC , T , T)} _ {N}
$$

Definita $X _ { N } ( \omega )$ la variabile aleatoria che ”conta” il numero di ”T” (teste) che s realizzano in N lanci, se ne vuole una caratterizzazione. 

## Conteggio Bernoulliano - 2

## La variabile aleatoria $X : \Omega \longrightarrow \mathcal { X } \dot { \mathrm {  ~ e ~ } }$

$$
X _ {N}: \omega \in \{T, C \} ^ {N} \longrightarrow X _ {N} (\omega) \in \overbrace {\{0 , \dots , N \}} ^ {\mathcal {X}} \quad X _ {N} (\omega) = k \text {   se   } \omega \text {   contiene   } k \text { '' } T
$$

Ora consideriamo $\boldsymbol { \omega } = [ \underbrace { T , \dots , T } _ { \mathrm { ~ } } , \underbrace { C , \dots , C } _ { \mathrm { ~ } } ]$ . Per l’indipendenza dei lanci (vedi 

{z }<sub>k volte</sub> | {z }<sub>N−k volte</sub> 

slide 38) avremo: 

$$
\mathbb {P} (\omega) = \mathbb {P} (\underbrace {T \cap \ldots \cap T} _ {k \text { volte}} \cap \underbrace {C \cap \ldots \cap C} _ {N - k \text { volte }}) = p ^ {k} q ^ {N - k}
$$

Le sequenze che hanno k teste e $( N - k )$ croci sono dunque tutte equiprobabili e sono in numero $C _ { N , k } = \left( \begin{array} { c } { { N } } \\ { { k } } \end{array} \right)$ 

Sia $\Omega _ { N , k } = \cup _ { i } \{ \omega _ { i } ^ { * } \} _ { i = 1 } ^ { C _ { N , k } }$ l’insieme di queste sequenze. Avremo: 

$$
\mathbb {P} (X _ {N} = k) = p _ {X _ {N}} (k) = \mathbb {P} \left(\Omega_ {N, k}\right) = \mathbb {P} \left(\cup_ {i = 1} ^ {C _ {N, k}} \{\omega_ {i} ^ {*} \}\right)
$$

## Conteggio Bernoulliano - 3

Siccome gli eventi elementari sono sempre mutuamente esclusiv $\big ( \mathbb { P } \big ( \{ \omega _ { i } ^ { * } \} \cap \{ \omega _ { j } ^ { * } \} \big ) = 0$ $\forall \ : i \neq j$ , avremo (vedi slide 34): 

$$
p _ {X _ {N}} (k) = \sum_ {i = 1} ^ {C _ {N, k}} \mathbb {P} (\{\omega_ {i} ^ {*} \}) = \left( \begin{array}{c} N \\ k \end{array} \right) p ^ {k} q ^ {N - k}
$$

che prende il nome di pmf binomiale di parametri $N \in p$ (in breve, $X _ { N } \sim \smash { \mathcal { B } ( N , p ) ) }$ . Si noti: 

$$
p _ {X _ {N}} (k) \geq 0   \forall   k \quad \sum_ {x \in \mathcal {X}} p _ {X _ {N}} (x) = \sum_ {k = 0} ^ {N} \binom{N}{k} p ^ {k} q ^ {N - k} = (p + q) ^ {N} = 1
$$

Infine: 

$$
\mathbb {E} \left[ X _ {N} \right] = \sum_ {x \in \mathcal {X}} x p _ {X _ {N}} (x) = \sum_ {k = 0} ^ {N} k \binom{N}{k} p ^ {k} q ^ {N - k} = N p
$$

## La variabile Uniforme

Una variabile aleatoria X che assuma valore in un qualsiasi alfabeto $\mathcal { X }$ di cardinalit`a finita, $| { \mathcal { X } } | = M$ si dice uniformemente distribuita su $\mathcal { X }$ (in breve, $X \sim \mathcal { U } ( \mathcal { X } ) )$ ) se: 

$$
p _ {X} (x) = \mathbb {P} (X = x) = \frac {1}{M} \quad \forall x \in \mathcal {X}
$$

Ovviamente $p x ( x )$ soddisfa le condizioni necessarie per poter essere una pmf; 

Il calcolo della media `e immediato: 

$\mathbb { E } [ X ] = \sum _ { x \in \mathcal { X } } x p _ { X } ( x ) = \frac { 1 } { M } \sum _ { x \in \mathcal { X } } x =$ Media aritmetica dei valori dell’alfabeto 

Un caso interessante `e $\mathcal { X } = \{ 0 , 1 , \ldots , M - 1 \}$ . In questo caso: 

$$
\sum_ {x \in \mathcal {X}} x = \sum_ {i = 0} ^ {M - 1} i = \frac {M (M - 1)}{2} \Rightarrow \mathbb {E} [ X ] = \frac {M - 1}{2}
$$

## La variabile Poissoniana

Una variabile aleatoria X si dice Poissoniana di parametro λ (in breve, $X \sim \mathcal { P } ( \lambda ) )$ se: 

Il suo alfabeto `e $\mathcal { X } = \{ 0 , 1 , 2 , . . . \} = \mathbb { N } _ { 0 }$ 

La sua pmf `e data da: 

$$
p _ {X} (k) = \mathbb {P} (X = k) = \frac {\lambda^ {k}}{k !} e ^ {- \lambda}, \qquad k \in \mathbb {N} _ {0}
$$

Si noti che la precedente soddisfa le condizioni per poter essere una pmf, in quanto: 

$$
p _ {K} (k) \geq 0 \quad \sum_ {x \in \mathcal {X}} p _ {X} (x) = e ^ {- \lambda} \overbrace {\sum_ {k = 0} ^ {\infty} \frac {\lambda^ {k}}{k !}} ^ {e ^ {\lambda}} = 1
$$

La sua media vale 

$$
\mathbb {E} [ X ] = \sum_ {x \in \mathcal {X}} x p _ {X} (x) = e ^ {- \lambda} \sum_ {k = 1} ^ {\infty} k \frac {\lambda^ {k}}{k !} = \lambda e ^ {- \lambda} \sum_ {k = 1} ^ {\infty} \frac {\lambda^ {k - 1}}{(k - 1) !} = \lambda
$$

## Pmf e medie condizionali

Introduciamo l’argomento con un esercizio. 

Supponiamo che $X \sim B \left( 1 6 , \frac { 1 } { 3 } \right)$ , cio`e: 

$$
\mathcal {X} = \{0, 1, \dots , 1 6 \}
$$

$$
p _ {X} (k) = \binom{1 6}{k} \left(\frac {1}{3}\right) ^ {k} \left(\frac {2}{3}\right) ^ {1 6 - k} \mathbb {E} [ X ] = \frac {1 6}{3}
$$

Supponiamo ora di assumere che sia verificata la condizione $X > 4 ;$ : ci chiediamo come si distribuisca X sotto questa condizione. 

Dal punto di vista fisico significa considerare un insieme di n esperimenti, scartare i valori di X che siano inferiori a 5 e valutare le probabilit`a dei residui dodici valori sul campione cos`ı ridotto. 

Possiamo quindi calcolare: 

$$
p _ {X \mid X > 4} (k) = \mathbb {P} (X = k \mid X > 4) = \frac {\mathbb {P} (\{X = k \} \cap \{X > 4 \})}{\mathbb {P} (\{X > 4 \})} =
$$

$$
= \left\{ \begin{array}{c c} \frac {p _ {X} (k)}{\mathbb {P} (\{X > 4 \})} = \frac {p _ {X} (k)}{\sum_ {i = 5} ^ {1 6} p _ {X} (i)} & k \in \{5, \ldots , 1 6 \} \\ 0 & k <   5 \end{array} \right.
$$

## Pmf e medie condizionali

Si noti che la pmf condizionale trovata `e una pmf. Infatti: 

$$
p _ {X \mid X > 4} (k) \geq 0 \quad \text { e } \quad \sum_ {k \in \mathbb {Z}} p _ {X \mid X > 4} (k) = \sum_ {k = 5} ^ {1 6} \frac {p _ {X} (k)}{\sum_ {i = 5} ^ {1 6} p _ {X} (i)} = 1
$$

Siamo quindi ora in grado di definire la pmf di una variabile aleatoria qualsiasi X condizionata a un qualsiasi evento $A \subseteq \Omega$ a probabilit`a non nulla nella forma: 

$$
p _ {X \mid A} (x) = \mathbb {P} (x \mid A) = \frac {\mathbb {P} (\{X = x \} \cap A)}{\mathbb {P} (A)} \quad x \in \mathcal {X}
$$

Ovviamente, $p _ { X \mid A } ( x )$ al variare di x in X con A prefissato `e una pmf; 

Nella prossima slide si mostrano gli andamenti delle pmf condizionali d $X \sim \dot { B } \left( 1 6 , \frac { 1 } { 3 } \right)$ condizionate all’evento $A = \{ X > 4 \} \ e \ B = \{ 2 \leq X \leq 6 \}$ 

## Andamenti delle pmf e pmf condizionali

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/3953309ceb6f3537284ae0699eabe52cb82506d6ad8a48b4cf7add134b70a9c4.jpg)



pmf e pmf condizionale di X ∼ B (16, 1)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/1505d7f1c8d7e5072fd4a5ff4df58e490794d1f37dbf350dc82422eb0f117252.jpg)


## Regola della probabilit`a totale per le pmf

Ricordiamo che (vedi slide 37), per un qualunque evento $C \subseteq \Omega$ e per una qualunque partizione $\{ E \} _ { i = 1 } ^ { M }$ si ha: 

$$
\mathbb {P} (C) = \sum_ {i = 1} ^ {M} \mathbb {P} (C | E _ {i}) \mathbb {P} (E _ {i})
$$

Pertanto, specializzando la precedente a $C = \{ X = x \}$ si ha: 

$$
\mathbb {P} (X = x) = p _ {X} (x) = \sum_ {m = 1} ^ {M} \mathbb {P} (\{X = x \} | E _ {m}) \mathbb {P} (E _ {m}) = \sum_ {m = 1} ^ {M} p _ {X | E _ {m}} (x) \mathbb {P} (E _ {m})
$$

Con riferimento all’esempio precedente, quindi: 

$$
p _ {X} (k) = p _ {X | X > 4} (k) \mathbb {P} (X > 4) + p _ {X | X \leq 4} (k) \mathbb {P} (X \leq 4) =
$$

$$
p _ {X \mid 2 \leq X \leq 6} (k) \mathbb {P} (2 \leq X \leq 6) + p _ {X \mid X \leq 1} (k) \mathbb {P} (X \leq 1) + p _ {X \mid X \geq 7} (k) \mathbb {P} (X \geq 7)
$$

essendo 

$$
\bullet \quad \Omega = E _ {1} \cup E _ {2} = \{X > 4 \} \cup \{X \leq 4 \}, E _ {1} \cap E _ {2} = \emptyset ;
$$

$$
\bullet \quad \Omega = E _ {1} ^ {\prime} \cup E _ {2} ^ {\prime} \cup E _ {3} ^ {\prime} = \{2 \leq X \leq 6 \} \cup \{X \leq 1 \} \cup \{X \geq 7 \}, E _ {i} ^ {\prime} \cap E _ {j} ^ {\prime} = \emptyset \forall i \neq j.
$$

## Medie e medie condizionali

Un analogo sviluppo `e possibile sulle medie. Infatti: 

$$
\mathbb {E} [ X ] = \sum_ {x \in \mathcal {X}} x p _ {X} (x) = \sum_ {x \in \mathcal {X}} x \sum_ {m = 1} ^ {M} p _ {X | E _ {m}} (x) \mathbb {P} (E _ {m}) =
$$

$$
\boxed {\sum_ {m = 1} ^ {M} \mathbb {P} (E _ {m}) \underbrace {\sum_ {x \in \mathcal {X}} x p _ {X | E _ {m}} (x)} _ {\mathbb {E} [ X | E _ {m} ]}}
$$

dove quindi si `e definita la media condizionata 

$$
\boxed {\mathbb {E} \left[ X | E _ {m} \right] = \sum_ {x \in \mathcal {X}} x p _ {X | E _ {m}} (x)}
$$

Si applichi questa formula agli esempi precedenti per ritrovare che, se $X \sim \mathcal { B } \left( 1 6 , p \right)$ 

$$
\mathbb {E} [ X ] = \mathbb {P} (X \leq 4) \mathbb {E} [ X | X \leq 4 ] + \mathbb {P} (X > 4) \mathbb {E} [ X | X > 4 ] =
$$

$$
\mathbb {P} (X \in \{2, 3, 4, 5, 6 \}) \mathbb {E} [ X | X \in \{2, 3, 4, 5, 6 \} ] + \mathbb {P} (X \notin \{2, 3, 4, 5, 6 \}) \mathbb {E} [ X | X \notin \{2, 3, 4, 5, 6 \} ]
$$

## Funzioni di variabili aleatorie -1

Si assuma che $X = X ( \omega )$ sia una variabile aleatoria con alfabeto X con pmf $\{ p \chi ( x ) \} _ { x \in \mathcal { X } }$ ; 

Sia g(·) una funzione il cui insieme di definizione includa i punti di X ; 

Si forma la nuova variabile aleatoria: 

$$
Y = g (X) = g [ X (\omega) ] \in \mathcal {Y} \quad \text {   dove   } \mathcal {Y} = g (\mathcal {X})
$$

Problema: Ricavare una caratterizzazione di Y dalla caratterizzazione di X in termini di 

pmf, $p _ { Y } ( y ) , y \in \mathcal { Y }$ 

media statistica, $\begin{array} { r } { \mathbb { E } [ Y ] = \sum _ { y \in \mathcal { Y } } y p _ { Y } ( y ) } \end{array}$ 

## Funzioni di variabili aleatorie -2

## Distinguiamo due casi:

a $\{ g ( x ) \} _ { x \in \mathcal { X } }$ biunivoca, cio`e: 

$$
| \mathcal {Y} | = | \mathcal {X} | \Leftrightarrow \forall y \in \mathcal {Y} \text {   è   definita   } x = g ^ {- 1} (y)
$$

b $\{ g ( x ) \} _ { x \in \mathcal { X } }$ univoca, cio`e associa a pi`u valori di X un solo valore d Y: 

$$
\mathcal {X} = \{x _ {1}, \dots , x _ {n} \} \quad \mathcal {Y} = \{y _ {1}, \dots , y _ {m} \} \quad n > m
$$

Nel caso [a] si tratta solo di una ridenominazione dell’alfabeto: 

$$
p _ {Y} (y _ {i}) = \mathbb {P} (Y = g (x _ {i})) = \mathbb {P} (X = g ^ {- 1} (y _ {i})) = \mathbb {P} (X = x _ {i}) = p _ {X} (x _ {i})
$$

Nel caso [b] vale la precedente relazione per tutti i punti di Y in cu $g ( y ) \ { \dot { \mathsf { e } } }$ invertibile. Per un punto $y _ { k }$ tale che $g ( x _ { 1 } ^ { ( k ) } ) = g ( x _ { 2 } ^ { ( k ) } ) = \ldots = g ( x _ { { L _ { k } } } ^ { ( k ) } ) = y _ { k }$ avremo: 

$$
p _ {Y} (y _ {k}) = \mathbb {P} \left(\cup_ {i = 1} ^ {L _ {k}} \{X = x _ {i} ^ {(k)} \}\right) = \sum_ {i = 1} ^ {L _ {k}} \mathbb {P} \left(X = x _ {i} ^ {(k)}\right) = \sum_ {i = 1} ^ {L _ {k}} p _ {X} (x _ {i} ^ {(k)})
$$

## Media di funzioni di variabili aleatorie

Cominciamo con il seguire la stessa suddivisione introdotta per il caso delle pmf. 

Funzioni biunivoche - In questo caso c’`e solo una ridenominazione dell’alfabeto, per cui: 

$$
\mathbb {E} [ Y ] = \sum_ {y \in \mathcal {Y}} y p _ {Y} (y) = \mathbb {E} [ g (X) ] = \sum_ {x \in \mathcal {X}} g (x) p _ {X} (x)\tag{1}
$$

Funzioni univoche - Avremo in questo caso: 

$$
\mathbb {E} [ Y ] = \sum_ {y \in \mathcal {Y}} y p _ {Y} (y) = \sum_ {y \in \mathcal {Y}} \sum_ {x: y = g (x)} g (x) p _ {X} (x)\tag{2}
$$

Si noti comunque che l’equazione (1) include l’equazione (2) come caso speciale. In conclusione adottiamo la forma generale (1) che prende anche il nome di Teorema fondamentale per il calcolo della media 

## Qualche esempio

Sia $X \sim \mathcal { U } ( \{ - 2 , - 1 , 0 , 2 \}$ 

Si trovi la pmf delle due variabili aleatorie: 

$$
Y _ {1} = X ^ {2} (Y = g (X), g (x) = x ^ {2}) \text {e} Y _ {2} = 3 \sin \left(\frac {2 \pi}{5} X\right) (Y = g (X), g (x) = \sin \left(\frac {2 \pi}{5} x\right)
$$

$Y _ { 1 }$ Avremo $\mathcal { V } _ { 1 } = \{ 0 , 1 , 4 \} , | \mathcal { V } _ { 1 } | = | \{ 0 , 1 , 4 \} | = 3 < | \mathcal { X } | = 4$ , per cui: 

$$
p _ {Y _ {1}} (0) = \mathbb {P} (X = 0) = \frac {1}{4} = p _ {Y _ {1}} (1) = \mathbb {P} (X = 1) = \frac {1}{4}
$$

$$
p _ {Y _ {1}} (2) = \mathbb {P} \left(\{X = - 2 \} \cup \{X = 2 \}\right) = \mathbb {P} (X = - 2) + \mathbb {P} (X = 2) = \frac {1}{2}
$$

$$
Y _ {2} \mathcal {Y} _ {2} = \left\{\overbrace {- 3 \sin \left(\frac {2 \pi}{5}\right)} ^ {- 2. 8 5}, \overbrace {- 3 \sin \left(\frac {4 \pi}{5}\right)} ^ {- 1. 7 4}, 0, \overbrace {3 \sin \left(\frac {4 \pi}{5}\right)} ^ {1. 7 4} \right\},
$$

$$
| \mathcal {Y} _ {2} | = 4 = | \mathcal {X} |:
$$

$$
p _ {Y _ {2}} (- 0. 9 5) = p _ {Y _ {2}} (\pm 0. 5 8) = p _ {Y _ {2}} (0) = \frac {1}{4} \Rightarrow Y _ {2} \sim \mathcal {U} \left(\mathcal {Y} _ {2}\right)
$$

## Valore quadratico medio e varianza di una variabile aleatoria

Data una variabile aleatoria $X \sim p _ { X } ( x ) , x \in \mathcal { X }$ , con media $\mu _ { X } = \operatorname { \mathbb { E } } [ X ]$ definiamo: 

Il valore quadratico medio (Mean Square) di X : 

$$
X _ {\text { rms }} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] = \sum_ {x \in \mathcal {X}} x ^ {2} p _ {X} (x)
$$

Il valore eficace (root mean square, rms) di X : 

$$
X _ {\text { rms }} = \sqrt {\mathbb {E} \left[ X ^ {2} \right]} = \sqrt {\sum_ {x \in \mathcal {X}} x ^ {2} p _ {X} (x)}
$$

La varianza di X : 

$$
\sigma_ {X} ^ {2} = \mathbb {E} \left[ (X - \mu_ {X}) ^ {2} \right] = \sum_ {x \in \mathcal {X}} (x ^ {2} + \mu_ {X} ^ {2} - 2 x \mu_ {X}) p _ {X} (x) = X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}
$$

La deviazione standard di X : 

$$
\sigma_ {X} = \sqrt {\sigma_ {X} ^ {2}} = \sqrt {\mathbb {E} [ X ^ {2} ] - \mu_ {X} ^ {2}} = \sqrt {X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}}
$$

## Esempio # 1: X ∼ B(N, p).

Si noti che, per $N = 1$ , abbiamo: 

$$
\mathbb {E} [ X ] = p, \quad \mathbb {E} [ X ^ {2} ] = 1 \times p + 0 \times (1 - p) = p, \quad \sigma_ {X} ^ {2} = p - p ^ {2} = p (1 - p), \quad \sigma_ {X} = \sqrt {p (1 - p)}
$$

In generale: 

$$
\overbrace {\mathbb {E} [ X ^ {2} ]} ^ {\sum_ {x \in \mathcal {X}} x ^ {2} p _ {X} (x)} = \sum_ {k = 0} ^ {N} k ^ {2} \binom{N}{k} p ^ {k} (1 - p) ^ {N - k} = \sum_ {k = 1} ^ {N} k \frac {N !}{(k - 1) ! (N - k) !} p ^ {k} q ^ {N - k}
$$

$$
= N p \left[ \frac {d}{d p} \sum_ {k = 1} ^ {N} \frac {(N - 1) !}{(k - 1) ! (N - k) !} p ^ {k} q ^ {N - k} \right] _ {q = 1 - p} = N p (1 - p) + \overbrace {N ^ {2} p ^ {2}} ^ {\mu_ {\chi} ^ {2}}
$$

per cui: 

$$
X _ {\mathrm{rms}} ^ {2} = N p (1 - p) + N ^ {2} p ^ {2} \quad \sigma_ {X} ^ {2} = N p (1 - p) \quad X _ {\mathrm{rms}} = \sqrt {N p (1 - p) + N ^ {2} p ^ {2}} \quad \sigma_ {X} = \sqrt {N p (1 - p)}
$$

## Esempio #2: variabile uniforme

Sia $X \sim \mathcal { U } ( \{ 0 , \dots , M - 1 \} )$ ), per cui $\begin{array} { r } { \mu _ { X } = \operatorname { \mathbb { E } } [ X ] = \frac { M - 1 } { 2 } } \end{array}$ . Il valore MS si scrive: 

$$
X _ {\mathrm{rms}} ^ {2} = \frac {1}{M} \sum_ {k = 1} ^ {M - 1} k ^ {2} = \frac {(M - 1) (2 M - 1)}{6}
$$

dove si `e sfruttato il fatto che: 

$$
\sum_ {i = 1} ^ {n} i ^ {2} = \frac {n (n + 1) (2 n + 1)}{6}
$$

Avremo quindi: 

$$
\sigma_ {X} ^ {2} = \frac {M (2 M - 1)}{6} - \frac {(M - 1) ^ {2}}{4} = \frac {M ^ {2} - 1}{1 2}
$$

$$
X _ {\mathrm{rms}} = \sqrt {\frac {M (2 M - 1)}{6}}
$$

$$
\sigma_ {X} = \sqrt {\frac {M ^ {2} - 1}{1 2}}
$$

## Esempio #3: variabile di Poisson

Sia $\begin{array} { r } { X \sim \mathcal { P } ( \lambda ) } \end{array}$ , per cui $\mu _ { X } = \operatorname { \mathbb { E } } [ X ] = \lambda$ . Il valore MS si scrive: 

$$
X _ {\mathrm{rms}} ^ {2} = e ^ {- \lambda} \sum_ {k = 1} ^ {\infty} k ^ {2} \frac {\lambda^ {k}}{k !} = e ^ {- \lambda} \sum_ {k = 1} ^ {\infty} k \frac {\lambda^ {k}}{(k - 1) !} = \lambda e ^ {- \lambda} \frac {d}{d \lambda} \left[ \sum_ {k = 1} ^ {\infty} \frac {\lambda^ {k}}{(k - 1) !} \right] =
$$

$$
\lambda e ^ {- \lambda} \frac {d}{d \lambda} \left[ \lambda \sum_ {k = 1} ^ {\infty} \frac {\lambda^ {k - 1}}{(k - 1) !} \right] = \lambda e ^ {- \lambda} \frac {d}{d \lambda} \left[ \lambda e ^ {\lambda} \right] = \lambda e ^ {- \lambda} \left[ e ^ {\lambda} + \lambda e ^ {\lambda} \right] = \lambda + \lambda^ {2}
$$

Quindi: 

$$
\sigma_ {X} ^ {2} = \lambda \quad X _ {\mathrm{rms}} = \sqrt {\lambda + \lambda^ {2}} \quad \sigma_ {X} = \sqrt {\lambda}
$$

Si noti che per una poissoniana la media e la varianza coincidono! 

## Il significato della varianza e della deviazione standard.

Supponiamo di non avere una caratterizzazione completa di una variabile aleatoria X ; 

Se $\mathcal { X } \subseteq [ 0 , + \infty [$ (cio`e la variabile `e non negativa) la media $\mu x$ ci d`a un’idea del suo comportamento, anche se imprecisa; 

Se invece X pu`o assumere sia valori positivi che negativi, la media non `e un indicatore significativo che possa dare informazioni sul comportamento della variabile aleatoria; 

In entrambi i casi `e comunque importante sapere quanto probabile sia osservare valori di X pi`u o meno lontani dalla sua media; 

Questo - nel caso si conosca la coppia $( \mu _ { X } , \sigma _ { X } )$ - pu`o avvenire in virt`u della Disuguaglianza di Chebyshev : 

$$
\mathbb {P} \left\{| X - \mu_ {X} | > k \sigma_ {X} \right\} = \mathbb {P} \left\{\mu_ {X} - k \sigma_ {X} \leq X \leq \mu_ {X} + k \sigma_ {X} \right\} \geq 1 - \frac {1}{k ^ {2}}
$$

Si capisce quindi che un parametro fondamentale `e il rapporto $\frac { \mu _ { X } } { \sigma _ { X } }$ : valori elevat di questo rapporto indicano una pmf molto concentrata intorno alla media (cio`e una variabile ”poco aleatoria”), mentre valori bassi implicano un’elevata aleatorietà. 

## La disuguaglianza di Chebyshev

Sia $Z$ una variabile non negativa definita su un alfabeto discreto ${ \mathcal { Z } } \subseteq [ 0 , + \infty [$ secondo una pmf $p _ { Z } ( z )$ 

Si valuti la probabilit`a che $Z$ sia non inferirore a un qualunque valore $\delta \in { \mathcal { Z } }$ 

$$
\mathbb {P} (Z \geq \delta) = \sum_ {z: z \geq \delta} p _ {Z} (z) \stackrel {{a}} {{\leq}} \sum_ {z: z \geq \delta} \left(\frac {z}{\delta}\right) ^ {2} p _ {Z} (z) \stackrel {{b}} {{\leq}} \sum_ {z \in \mathcal {Z}} \left(\frac {z}{\delta}\right) ^ {2} p _ {Z} (z) \stackrel {{c}} {{=}} \frac {\mathbb {E} [ Z ^ {2} ]}{\delta^ {2}}\tag{3}
$$

a Deriva dall’essere $\begin{array} { r } { \left( \frac { z } { \delta } \right) ^ { 2 } \geq 1 } \end{array}$ per $z \geq \delta ;$ 

b Deriva dal fatto che estendendo la sommatoria su tutto $\mathcal { Z }$ si aggiungono termini non negativi; 

c Deriva dalla definizione di valore quadratico medio. 

La disuguaglianza di Chebyshev si ricava quindi ponendo $Z = | X - \mu x | \geq 0$ e $\delta = k \sigma _ { X }$ nella (3), nonch`e notando che con questa scelt 

$$
\mathbb {E} [ Z ^ {2} ] = \mathbb {E} [ | X - \mu_ {X} | ^ {2} ] = \mathbb {E} [ (X - \mu_ {X}) ^ {2} ] = \sigma_ {X} ^ {2}.
$$

## Quadro sintetico delle propriet`a di media e varianza

Se (a, b) sono costanti reali ${ \mathbb E } [ a X + b ] = a { \mathbb E } [ X ] + b$ , visto che $\mathbb { E } [ b ] = b ;$ 

Se $X ( \omega ) \geq 0 \ \forall \omega \in \Omega$ (cio`e, se $\mathcal { X } \subseteq [ 0 , + \infty [ )$ , allora $\mathbb { E } [ X ] \geq 0 ;$ 

● $\sigma _ { X } ^ { 2 } \geq 0$ (in quanto media della variabile non negativa $( X - \mu _ { X } ) ^ { 2 } )$ 

Se $\boldsymbol { Y } = \boldsymbol { a } \boldsymbol { X } + \boldsymbol { b }$ , allora $\sigma _ { Y } ^ { 2 } = a ^ { 2 } \sigma _ { X } ^ { 2 }$ . Infatti: 

$$
\mu_ {Y} = a \mu_ {X} + b, \quad \mathbb {E} [ Y ^ {2} ] = \mathbb {E} [ a ^ {2} X ^ {2} + 2 a b X + b ^ {2} ] = a ^ {2} \mathbb {E} [ X ^ {2} ] + 2 a b \mathbb {E} [ X ] + b ^ {2}
$$

$$
\sigma_ {Y} ^ {2} = a ^ {2} \mathbb {E} [ X ^ {2} ] + 2 a b \mu_ {X} + b ^ {2} - (a \mu_ {X} + b) ^ {2} = a ^ {2} \sigma_ {X} ^ {2}
$$

Come conseguenza delle precedenti relazioni si ha anche: 

$$
\mathbb {E} [ Y ^ {2} ] = Y _ {\mathrm{rms}} ^ {2} = a ^ {2} X _ {\mathrm{rms}} ^ {2} + 2 a b \mu_ {X} + b ^ {2}
$$

Si noti infine che per variabili a media nulla $( \mu x = 0 )$ , abbiamo $\sigma _ { X } ^ { 2 } = X _ { \mathrm { r m s } } ^ { 2 }$ 

## Definizione di variabili multiple

Formalmente, una coppia di variabili aleatorie (o variabile doppia) `e definita - in analogia con quelle singole - nella forma: 

$$
X, Y: \omega \in \Omega \longrightarrow (X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y} \subseteq \mathbb {R} ^ {2}
$$

dove $\mathcal { X } \in \mathcal { V }$ sono gli alfabeti di X e di Y rispettivamente. 

In altre parole, il risultato di un esperimento $\omega _ { * }$ non `e un unico valore 

$X ( \omega _ { * } ) = x _ { * } \in \mathcal { X }$ , ma una coppia ordinata $( X ( \omega _ { * } ) , Y ( \omega _ { * } ) ) = ( x _ { * } , y _ { * } )$ , che quindi varia nel prodotto cartesiano $\mathcal { X } \times \mathcal { V }$ . Per esempio: 

Si consideri un elenco di tutti i residenti in Italia a una certa data, corredato di dati quali altezza (X ), peso (Y ), et`a (Z ); 

Si scelga un residente a caso e se ne leggano l’altezza 

$X ( \omega ) \in \{ 3 0 \mathsf { c m } , 3 1 \mathsf { c m } , \hdots 2 1 0 \mathsf { c m } \}$ , il peso $Y ( \omega ) \in \{ 0 . 5 \ : \mathrm { k g } , 0 . 6 \ : \mathrm { k g } , . \hdots 1 7 0 \ : \mathrm { k g } \}$ l’et`a $Z ( \omega ) \in \{ 0 \mathrm { a n n i , 0 . 5 a n n i , \dots 1 1 0 a n n i } \}$ 

## Possibili coppie sono

$$
(X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y}, \quad (X (\omega), Z (\omega)) \in \mathcal {X} \times \mathcal {Z}, \quad (Y (\omega), Z (\omega)) \in \mathcal {Y} \times \mathcal {Z}
$$

$( X ( \omega ) , Y ( \omega ) , Z ( \omega ) ) \in \mathcal { X } \times \mathcal { Y } \times \mathcal { Z } \ \dot { \rho }$ una terna di variabili aleatorie. 

## pmf/DF/pdf congiunta

Si supponga di considerare la coppia $( X , Y )$ (nel caso precedente, altezza e peso di un residente scelto a caso); 

Si eseguano n esperimenti (nel caso precedente, si scelga per n volte a caso un nome dell’elenco); 

Si registrino i relativi valori di $\{ ( \boldsymbol { X } ( \omega _ { i } ) , \boldsymbol { Y } ( \omega _ { i } ) ) \} _ { i = 1 } ^ { n }$ (nel caso precedente, altezza e peso del residente di volta in volta scelto); 

Si indichi con $n _ { X = x , Y = y } = n _ { X = x , Y = y } ( n )$ il numero di volte in cui $X = x \in$ Y = y (nel caso precedente, il numero di volte in cui l’utente scelto a caso ha una altezza x e un peso y); 

Ovviamente, l’evento $\{ X = x \} \cap \{ Y = y \}$ occorre $n x { = } x , Y { = } y$ volte su n esperimenti. Definiamo allora la seguente $\mathsf { p m f / D F / p d f }$ congiunta delle due variabili aleatorie $X \textsf { e Y }$ 

$$
p _ {X, Y} (x, y) = \mathbb {P} \left(\{X = x \} \cap \{Y = y \}\right) = \lim _ {n \rightarrow \infty} \frac {n _ {X = x , Y = y}}{n}, \quad (x, y) \in \mathcal {X} \times \mathcal {Y}
$$

In altre parole, $p x , v ( x , y ) \ { \dot { \mathbf { e } } }$ una tabella di $| \mathcal { X } | | \mathcal { D } |$ numeri che - ovviamente - gode di opportune propriet`a. 

## Propriet`a della pmf congiunta

$\begin{array} { r } { p x , \gamma \geq 0 \in \sum _ { x \in \mathcal { X } } \sum _ { y \in \mathcal { Y } } p x , \gamma ( x , y ) = 1 } \end{array}$ . Infatti: 

$$
1 = \mathbb {P} (\Omega) = \mathbb {P} \left(\cup_ {x \in \mathcal {X}} \cup_ {y \in \mathcal {Y}} \{X = x, Y = y \}\right) = \sum_ {x \in \mathcal {X}} \sum_ {y \in \mathcal {Y}} \underbrace {\mathbb {P} \left(\{X = x , Y = y \}\right)} _ {p _ {X, Y} (x, y)}
$$

essendo l’evento elementare $\{ X = x , Y = y \}$ incompatibile con ogni altro evento elementare $\{ X = x ^ { \prime } , Y = y ^ { \prime } \}$ con $x \neq x ^ { \prime } \mathtt { e } / \circ y \neq y ^ { \prime }$ 

Si noti che $\cup _ { x \in \mathcal { X } } \{ X = x \} = \Omega \textsf { e } \cup _ { y \in \mathcal { Y } } = \Omega$ , per cui: 

$$
\{X = x \} = \{X = x \} \cap \Omega = \{X = x \} \cap \cup_ {y \in \mathcal {Y}} \{Y = y \} = \cup_ {y \in \mathcal {Y}} \{X = x \} \cap \{Y = y \}
$$

$$
\Longrightarrow \mathbb {P} (\{X = x \}) = \mathbb {P} \left(\cup_ {y \in \mathcal {Y}} \{\{X = x \} \cap \{Y = y \} \}\right) = \sum_ {y \in \mathcal {Y}} \mathbb {P} \left(\{X = x \} \cap \{Y = y \}\right)
$$

Si ha quindi la propriet`a di marginalizzazione: 

$$
\sum_ {y \in \mathcal {Y}} p _ {X, Y} (x, y) = p _ {X} (x) \quad \sum_ {x \in \mathcal {X}} p _ {X, Y} (x, y) = p _ {Y} (y)
$$

per cui caratterizzare congiuntamente (X , Y ) significa anche caratterizzarle marginalmente, mentre il viceversa non `e necessariamente vero. 

## Variabili indipendenti

Due varibili aleatorie $X \in \mathcal { X } \mathrm { ~ e ~ } Y \in \mathcal { Y }$ sono indipendenti se (e solo se) gli event $\{ X = x \} \mathrm { ~ e ~ } \{ Y = y \}$ sono indipendenti; 

Per due variabili indipendenti la pmf congiunta si fattorizza nel prodotto delle marginali: 

$$
p _ {X, Y} (x, y) = \mathbb {P} (\{X = x \} \cap \{Y = y \}) = \mathbb {P} (\{X = x \}) \mathbb {P} (\{Y = y \}) = p _ {X} (x) p _ {Y} (y)
$$

Questo `e l’unico caso in cui assegnare le due pmf marginali $p x ( x ) \mathrm { ~ e ~ } p _ { Y } ( y )$ equivale ad assegnare la pmf congiunta. 

Siccome il concetto di pmf congiunta si generalizza a una m−pla di variabili aleatorie $( X _ { 1 } , \ldots , X _ { m } ) \in { \mathcal { X } } _ { 1 } \times \ldots \times { \mathcal { X } } _ { m } \subseteq \mathbb { R } ^ { m }$ mediante la pmf congiunta: 

$$
p _ {X _ {1}, \dots X _ {m}} (x _ {1}, \dots , x _ {m}) = \mathbb {P} \left(\{X _ {1} = x _ {1} \}, \dots , \{X _ {m} = x _ {m} \}\right)
$$

cos`ı si generalizza il concetto di indipendenza: 

$$
p _ {X _ {1}, \dots , X _ {m}} (x _ {1}, \dots , x _ {m}) = \mathbb {P} \left(\left\{X _ {1} = x _ {1} \right\}, \dots , \left\{X _ {m} = x _ {m} \right\}\right) =
$$

$$
\prod_ {i = 1} ^ {m} \mathbb {P} \left(\left\{X _ {i} = x _ {i} \right\}\right) = \prod_ {i = 1} ^ {m} p _ {X _ {i}} \left(x _ {i}\right)
$$

## Le pmf condizionate

Si considerino varibili aleatorie $X \in \mathcal { X } \mathrm { ~ e ~ } Y \in \mathcal { Y }$ con assegnata pmf congiunta $p _ { X , Y } ( x , y )$ ; 

Applichiamo all’evento $\{ X = x , Y = y \} = \{ X = x \} \cap \{ Y = y \}$ la legge della probabilit`a composta (vedi slide 36): 

$$
p _ {X, Y} (x, y) = \mathbb {P} \left(\{X = x \} \cap \{Y = y \}\right) = \overbrace {\mathbb {P} \left(\{Y = y \} | \{X = x \}\right)} ^ {p _ {Y | X} (y | x)} \overbrace {\mathbb {P} \left(\{X = x \}\right)} ^ {p _ {X} (x)}
$$

$p _ { Y \mid X } ( y | x )$ `e la legge di probabilita condizionata (o pmf condizionata) di Y dato $x ;$ 

Come la legge congiunta, $p _ { Y \mid X } ( y | x )$ `e una tabella di $| \mathcal { X } | | \mathcal { D } |$ numeri che soddisfa alcune propriet`a; 

Ovviamente, abbiamo: 

$$
p _ {Y \mid X} (y \mid x) p _ {X} (x) = p _ {X \mid Y} (x \mid y) p _ {Y} (y) \Longrightarrow
$$

$$
p _ {X \mid Y} (x \mid y) = \frac {p _ {Y \mid X} (y \mid x) p _ {X} (x)}{p _ {Y} (y)}
$$

(Legge di Bayes) 

## Alcune propriet`a delle pmf condizionate

$p _ { Y \mid X } ( y | x )$ se x resta fisso e y varia in Y `e una legge di probabilit`a. Infatti: 

$$
p _ {Y | X} (y | x) \geq 0 \quad \sum_ {y \in \mathcal {Y}} p _ {Y | X} (y | x) = \mathbb {P} \left(\cup_ {y \in \mathcal {Y}} \{Y = y \} | \{X = x \}\right) = \mathbb {P} (\Omega | \{X = x \}) = 1
$$

La propriet`a di marginalizzazione della pmf congiunta (vedi slide 71) si scrive in termini di pmf condizionali nella forma: 

$$
p _ {X} (x) = \sum_ {y \in \mathcal {Y}} p _ {X, Y} (x, y) = \sum_ {y \in \mathcal {Y}} p _ {X | Y} (x | y) p _ {Y} (y)
$$

$$
p _ {Y} (y) = \sum_ {x \in \mathcal {X}} p _ {X, Y} (x, y) = \sum_ {x \in \mathcal {X}} p _ {Y | X} (y | x) p _ {X} (x)
$$

Si noti che questa non `e altro che la legge della probabilit`a totale (vedi slide 37) scritta, per la prima equazione, per l’evento $\{ X = x \}$ rispetto alla partizione $\Omega = \cup _ { y \in \mathcal { y } } \{ Y = y \}$ e, per la seconda equazione, per l’evento $\{ Y = y \}$ rispetto alla partizione $\Omega = \cup _ { x \in { \mathcal { X } } } \{ X = x \}$ 

Si noti, infine, che se $X \textsf { e Y }$ sono indipendenti: 

$$
p _ {Y | X} (y | x) = p _ {Y} (y)
$$

$$
p _ {X \mid Y} (x \mid y) = p _ {X} (x)
$$

## Generalizzando...

Si consideri una terna di variabili aleatorie (X , Y , Z ), distribuite secondo $p x , Y , Z ( x , y , z ) , ( x , y , z ) \in \mathcal { X } \times \mathcal { Y } \times \mathcal { Z } .$ 

Usando consecutivamente la legge della probabilit`a composta, otteniamo: 

$$
\mathbb {P} (X = x, Y = y, Z = z) = \mathbb {P} (X = x, Y = y | Z = z) \mathbb {P} (Z = z) =
$$

$$
\mathbb {P} (X = x \mid Z = z, Y = y) \mathbb {P} (Y = y \mid Z = z) \mathbb {P} (Z = z)
$$

che ci introduce alla ”regola della catena” (ogni permutazione dei pedici e degl argomenti `e ovviamente possibile): 

$$
p _ {X \mid Y, Z} (x \mid y, z) = \frac {p _ {X , Y \mid Z} (x , y \mid z)}{p _ {Y \mid Z} (y \mid z)} \rightarrow p _ {X, Y, Z} (x, y, z) = p _ {Z} (z) p _ {Y \mid Z} (y \mid z) p _ {X \mid Y, Z} (x \mid y, z)
$$

La terna `e dunque indipendente se e e solo se $p _ { X | Y , Z } ( x | y , z ) = p _ { X } ( x )$ 

$$
p _ {Y | X, Z} (y | x, z) = p _ {Y} (y) \in p _ {Z | X, Y} (z | x, y) = p _ {Z} (z).
$$

## Esempio: Emissione di 3 bit da una sorgente binaria

Si consideri una sorgente binaria che emetta tre bit, siano ess $\left( B _ { 1 } , B _ { 2 } , B _ { 3 } \right)$ $B _ { i } \in \{ 0 , 1 \}$ ; 

Si assegnano le due leggi congiunte $p _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } ) \in q _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ della tabella $( 0 < \alpha < 1 )$ 

Dire se $( B _ { 1 } , B _ { 2 } ) , ( B _ { 1 } , B _ { 3 } ) , ( B _ { 2 } , B _ { 3 } ) , ( B _ { 1 } , B _ { 2 } , B _ { 3 } )$ sono o meno indipendent secondo $p _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } ) / q _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ 

<table><tr><td><eq>(b_1, b_2, b_3)</eq></td><td><eq>p_{B_1, B_2, B_3}(b_1, b_2, b_3)</eq></td><td><eq>q_{B_1, B_2, B_3}(b_1, b_2, b_3)</eq></td></tr><tr><td>000</td><td><eq>(1 - \alpha)^3</eq></td><td><eq>(1 - \alpha)^2</eq></td></tr><tr><td>001</td><td><eq>\alpha(1 - \alpha)^2</eq></td><td>0</td></tr><tr><td>010</td><td><eq>\alpha(1 - \alpha)^2</eq></td><td>0</td></tr><tr><td>011</td><td><eq>\alpha^2(1 - \alpha)</eq></td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>100</td><td><eq>\alpha(1 - \alpha)^2</eq></td><td>0</td></tr><tr><td>101</td><td><eq>\alpha^2(1 - \alpha)</eq></td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>110</td><td><eq>\alpha^2(1 - \alpha)</eq></td><td><eq>\alpha^2</eq></td></tr><tr><td>111</td><td><eq>\alpha^3</eq></td><td>0</td></tr></table>

## Marginalizzazione di $\textcircled { 1 } \textcircled { 2 } \textcircled { 3 } \textcircled { 2 } \textcircled { 2 } \textcircled { 1 } \textcircled { 2 } \textcircled { 2 } \textcircled { 2 } \textcircled { 2 } \textcircled { 2 } \textcircled { 2 } \textcircled { 2 }$

Cominciamo con il trovare la congiunta di tutte le possibili coppie secondo $p _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ . Ricordiamo la propriet`a di marginalizzazione: 

$$
p _ {B _ {1}, B _ {2}} (b _ {1}, b _ {2}) = p _ {B _ {1}, B _ {2}, B _ {3}} (b _ {1}, b _ {2}, 0) + p _ {B _ {1}, B _ {2}, B _ {3}} (b _ {1}, b _ {2}, 1)
$$

e analoghe 

otteniamo le congiunte: 

<table><tr><td><eq>(b_1, b_2)</eq></td><td><eq>p_{B_1, B_2}(b_1, b_2)</eq></td></tr><tr><td>00</td><td><eq>(1 - \alpha)^2</eq></td></tr><tr><td>01</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>10</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>11</td><td><eq>\alpha^2</eq></td></tr></table>


Con un’ulteriore marginalizzazione: 


<table><tr><td><eq>(b_1, b_3)</eq></td><td><eq>p_{B_1, B_3}(b_1, b_3)</eq></td></tr><tr><td>00</td><td><eq>(1 - \alpha)^2</eq></td></tr><tr><td>01</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>10</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>11</td><td><eq>\alpha^2</eq></td></tr></table>

<table><tr><td><eq>(b_2, b_3)</eq></td><td><eq>p_{B_2, B_3}(b_2, b_3)</eq></td></tr><tr><td>00</td><td><eq>(1 - \alpha)^2</eq></td></tr><tr><td>01</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>10</td><td><eq>\alpha(1 - \alpha)^2</eq></td></tr><tr><td>11</td><td><eq>\alpha^2</eq></td></tr></table>

$$
p _ {B _ {1}} (b _ {1}) = p _ {B _ {1}, B _ {2}} (b _ {1}, 0) + p _ {B _ {1}, B _ {2}} (b _ {1}, 1)
$$

e analoghe 

<table><tr><td>$ b_{1} $</td><td>$ p_{B_{1}}(b_{1}) $</td></tr><tr><td>0</td><td>$ (1-\alpha) $</td></tr><tr><td>1</td><td>$ \alpha $</td></tr></table>

<table><tr><td><eq>b_2</eq></td><td><eq>p_{B_2}(b_2)</eq></td></tr><tr><td>0</td><td><eq>(1 - \alpha)</eq></td></tr><tr><td>1</td><td><eq>\alpha</eq></td></tr></table>

<table><tr><td>$ b_{3} $</td><td>$ p_{B_{3}}(b_{3}) $</td></tr><tr><td>0</td><td>$ (1-\alpha) $</td></tr><tr><td>1</td><td>$ \alpha $</td></tr></table>

## Marginalizzazione di $\textcircled { 4 } \textcircled { 1 2 } \textcircled { 1 2 } \textcircled { 1 2 } \textcircled { 1 6 } \textcircled { 2 } \textcircled { 6 } \textcircled { 6 } \textcircled { 6 }$

Procedendo nello stesso modo otteniamo le congiunte: 

<table><tr><td><eq>(b_1, b_2)</eq></td><td><eq>q_{B_1, B_2}(b_1, b_2)</eq></td></tr><tr><td>00</td><td><eq>(1 - \alpha)^2</eq></td></tr><tr><td>01</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>10</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>11</td><td><eq>\alpha^2</eq></td></tr></table>

<table><tr><td><eq>(b_1, b_3)</eq></td><td><eq>q_{B_1, B_3}(b_1, b_3)</eq></td></tr><tr><td>00</td><td><eq>(1 - \alpha)^2</eq></td></tr><tr><td>01</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>10</td><td><eq>\alpha^2</eq></td></tr><tr><td>11</td><td><eq>\alpha(1 - \alpha)</eq></td></tr></table>

<table><tr><td><eq>(b_2, b_3)</eq></td><td><eq>q_{B_2, B_3}(b_2, b_3)</eq></td></tr><tr><td>00</td><td><eq>(1 - \alpha)^2</eq></td></tr><tr><td>01</td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>10</td><td><eq>\alpha^2</eq></td></tr><tr><td>11</td><td><eq>\alpha(1 - \alpha)^2</eq></td></tr></table>

E le marginali: 

<table><tr><td><eq>b_1</eq></td><td><eq>q_{B_1}(b_1)</eq></td></tr><tr><td>0</td><td><eq>(1 - \alpha)</eq></td></tr><tr><td>1</td><td><eq>\alpha</eq></td></tr></table>

<table><tr><td><eq>b_2</eq></td><td><eq>q_{B_2}(b_2)</eq></td></tr><tr><td>0</td><td><eq>(1 - \alpha)</eq></td></tr><tr><td>1</td><td><eq>\alpha</eq></td></tr></table>

<table><tr><td>$ b_{3} $</td><td>$ q_{B_{3}}(b_{3}) $</td></tr><tr><td>0</td><td>$ (1-\alpha) $</td></tr><tr><td>1</td><td>$ \alpha $</td></tr></table>

ome mai alcune delle congiunte a coppie e le marginali coincidono, ma le pmf delle terne sono diverse Qual `e il mistero? 

## Soluzione

Si vede facilmente che, per quanto riguarda $p _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ , abbiamo: 

$$
p _ {B _ {1}, B _ {2}, B _ {3}} (b _ {1}, b _ {2}, b _ {3}) = \prod p _ {B _ {i}} (b _ {i}) \Rightarrow p _ {B _ {m}, B _ {k}} (b _ {m}, b _ {k}) = p _ {B _ {m}} (b _ {m}) p _ {B _ {k}} (b _ {k}) \forall m \neq k
$$

quindi $p _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ implica l’indipendenza statistica della intera terna. 

Viceversa, per $q _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ si ha: 

$$
q _ {B _ {m}, B _ {k}} (b _ {m}, b _ {k}) = q _ {B _ {m}} (b _ {m}) q _ {B _ {k}} (b _ {k}) m = 1, k = 2 \quad q _ {B _ {1}, B _ {2}, B _ {3}} (b _ {1}, b _ {2}, b _ {3}) \neq \prod q _ {B _ {i}} (b _ {i})
$$

quindi le variabili $B _ { 1 } , B _ { 2 }$ sono indipendenti, ma non lo `e la terna, n`e lo sono $B _ { 1 } , B _ { 3 } \circ B _ { 2 } , B _ { 3 }$ . Infatti, per esempio: 

$$
p _ {B _ {3} = 1 \mid B _ {1} = 1, B _ {2} = 1} = \frac {p _ {B _ {1} , B _ {2} , B _ {3}} (1 , 1 , 1)}{p _ {B _ {1} , B _ {2}} (1 , 1)} = \frac {\alpha^ {3}}{\alpha^ {2}} = \alpha = p _ {B _ {3}} (1)
$$

$$
q _ {B _ {3} = 1 | B _ {1} = 1, B _ {2} = 1} = \frac {q _ {B _ {1} , B _ {2} , B _ {3}} (1 , 1 , 1)}{q _ {B _ {1} , B _ {2}} (1 , 1)} = 0 \neq q _ {B _ {3}} (1)
$$

Si vede facilmente che $B _ { 3 } = B _ { 1 } \oplus B _ { 2 }$ `e un bit di parit`a. 

## Funzioni di variabili doppie

Sia $( X , Y ) \sim p x , Y ( x , y ) ( x , y ) \in \mathcal { X } \times \mathcal { Y }$ una variabile doppia con pmf $p _ { X , Y } ( x , y )$ ; 

Sia $g ( x , y )$ una funzione di due variabili il cui dominio di esistenza includa $\mathcal { X } \times \mathcal { N } ;$ 

Si vuole caratterizzare $Z = \boldsymbol { \mathrm { g } } ( \boldsymbol { X } , \boldsymbol { Y } )$ in termini di pmf e media statistica. 

a Si determini l’alfabeto Z. Se $| \mathcal { Z } | = | \mathcal { X } | | \mathcal { V } |$ |, allora - seguendo i ragionamento della slide 59 - avremo che esiste un unico punto $( x ( z ) , y ( z ) ) : z = g ( x , y )$ , per cui: 

$$
\mathbb {P} (Z = z) = p _ {Z} (z) = p _ {X, Y} [ x (z), y (z) ]
$$

b Se $| \mathcal { Z } | < | \mathcal { X } | | \mathcal { V } |$ |, varr`a la precedente per i punti in cui l’inversa `e unica, mentre per i punti in cui l’inversa non esiste ci sar`a un ”collassamento delle probabilit`a”: 

$$
\operatorname{Se} g (x, y) = z \text { per } (x, y) \in \mathcal {A} (z) \subseteq \mathcal {X} \times \mathcal {Y} \Rightarrow p _ {Z} (z) = \sum_ {x, y \in \mathcal {A} (z)} p _ {X, Y} (x, y)
$$

## Un esempio

Si considerino due variabili doppie, $( X _ { 1 } , Y _ { 1 } ) \in \{ 0 , 1 \} ^ { 2 } \mathrm { ~ e ~ } ( X _ { 2 } , Y _ { 2 } ) \in \{ - 1 , 1 \} ^ { 2 }$ . Le pmf congiunte sono quelle riportate di seguito: 

<table><tr><td><eq>(x_1, y_1)</eq></td><td><eq>p_{X_1}, y_1(x_1, y_1)</eq></td></tr><tr><td>00</td><td><eq>\frac{1}{3}</eq></td></tr><tr><td>01</td><td><eq>\frac{2}{9}</eq></td></tr><tr><td>10</td><td><eq>\frac{1}{9}</eq></td></tr><tr><td>11</td><td><eq>\frac{1}{3}</eq></td></tr></table>

<table><tr><td><eq>(x_2, y_2)</eq></td><td><eq>p_{X_2}, Y_2(x_2, y_2)</eq></td></tr><tr><td>(-1,-1)</td><td><eq>\frac{1}{4}</eq></td></tr><tr><td>(-1,1)</td><td><eq>\frac{1}{2}</eq></td></tr><tr><td>(1,-1)</td><td><eq>\frac{1}{8}</eq></td></tr><tr><td>(1,1)</td><td><eq>\frac{1}{8}</eq></td></tr></table>

Si caratterizzino le due variabili aleatorie $Z _ { 1 } = 3 X _ { 1 } ^ { 2 } + Y _ { 1 } \thinspace \thinspace \thinspace e \thinspace Z _ { 2 } = 3 X _ { 2 } ^ { 2 } + Y _ { 2 }$ 

Si noti che $| \mathcal { Z } _ { 1 } | = | \{ 0 , 1 , 3 , 4 \} | = | \{ 0 , 1 \} | ^ { 2 }$ , per cui la corrispondenza `e biunivoca. 

$$
p _ {Z _ {1}} (0) = p _ {X _ {1}, Y _ {1}} (0, 0) = \frac {1}{3} \quad p _ {Z _ {1}} (1) = p _ {X _ {1}, Y _ {1}} (0, 1) = \frac {2}{9}
$$

$$
p _ {Z _ {1}} (3) = p _ {X _ {1}, Y _ {1}} (1, 0) = \frac {1}{9} \quad p _ {Z _ {1}} (4) = p _ {X _ {1}, Y _ {1}} (1, 1) = \frac {1}{3}
$$

Viceversa, $| \mathcal { Z } _ { 2 } | = | \{ 2 , 4 \} | < | \{ 0 , 1 \} | ^ { 2 }$ , per cui: 

$$
p _ {Z _ {2}} (2) = p _ {X _ {2}, Y _ {2}} (1, - 1) + p _ {X _ {2}, Y _ {2}} (- 1, - 1) = \frac {3}{8}
$$

$$
p _ {Z _ {2}} (4) = p _ {X _ {2}, Y _ {2}} (- 1, 1) + p _ {X _ {2}, Y _ {2}} (1, 1) = \frac {5}{8}
$$

## Media di funzioni di variabili doppie

Con riferimento alla trasformazione generica $Z = \boldsymbol { \mathrm { g } } ( \boldsymbol { X } , \boldsymbol { Y } )$ si vede immediatamente che il Teorema Fondamentale per il calcolo della Media (vedi slide 60) si traduce in: 

$$
\mathbb {E} [ Z ] = \sum_ {x \in \mathcal {X}} \sum_ {y \in \mathcal {Y}} g (x, y) p _ {X, Y} (x, y) = \sum_ {(x, y) \in \mathcal {X} \times \mathcal {Y}} g (x, y) p _ {X, Y} (x, y)
$$

Si noti che, se $Z = a X + b Y$ , con a e b costanti deterministiche, allora: 

$$
\mathbb {E} [ a X + b Y ] = \sum_ {x \in \mathcal {X}} \sum_ {y \in \mathcal {Y}} (a x + b y) p _ {X, Y} (x, y) = a \sum_ {x \in \mathcal {X}} x \overbrace {\sum_ {y \in \mathcal {Y}} p _ {X , Y} (x , y)} ^ {p _ {X} (x)} +
$$

$$
+ b \sum_ {y \in \mathcal {Y}} y \overbrace {\sum_ {x \in \mathcal {X}} p _ {X , Y} (x , y)} ^ {p _ {Y} (y)} = a \mathbb {E} [ X ] + b \mathbb {E} [ Y ]
$$

Pi`u in generale, se $\{ X _ { i } \} _ { i = 1 } ^ { m }$ sono m variabili aleatorie con pmf $p _ { X _ { 1 } , \ldots , X _ { m } } ( x _ { 1 } , \ldots , x _ { m } )$ 

$$
\mathbb {E} \left[ \sum_ {i = 1} ^ {m} a _ {i} X _ {i} \right] = \sum_ {i = 1} ^ {m} a _ {i} \mathbb {E} \left[ X _ {i} \right]
$$

## Teorema della media condizionata

Con riferimento a $Z = \boldsymbol { \mathrm { g } } ( \boldsymbol { X } , \boldsymbol { Y } )$ osserviamo che: 

$$
\mathbb {E} \left[ Z \right] = \mathbb {E} \left[ g (X, Y) \right] = \sum_ {x \in \mathcal {X}} \sum_ {y \in \mathcal {Y}} g (x, y) \overbrace {p _ {X , Y} (x , y)} ^ {p _ {X | Y} (x | y) p _ {Y} (y)} =
$$

$$
\sum_ {y \in \mathcal {Y}} p _ {Y} (y) \sum_ {x \in \mathcal {X}} g (x, y) p _ {X | Y} (x | y) = \sum_ {y \in \mathcal {Y}} h (y) p _ {Y} (y)
$$

Nella precedente, $h ( y )$ rappresenta la media di $g ( X , y )$ eseguita rispetto alla pmf condizionata $p _ { X \mid Y } ( x | y )$ . Cio`e: 

$$
h (y) = \mathbb {E} [ g (X, Y) | Y = y ] \Longrightarrow h (Y) = \mathbb {E} [ g (X, Y) | Y ] \Longrightarrow
$$

$$
\mathbb {E} \left[ g (X, Y) \right] = \mathbb {E} \left[ h (Y) \right] = \mathbb {E} \left[ \mathbb {E} \left[ g (X, Y) | Y \right] \right]
$$

che prende il nome di Teorema della Media Condizionata, visto che $\mathbb { E } \left[ g ( X , Y ) | Y \right]$ `e la media di $g ( X , Y )$ condizionata a Y . Ovviamente i ruoli di $X \textsf { e Y }$ si possono scambiare. 

## Esempio di applicazione - 1

Torniamo all’esempio della slide 81. Ovviamente avremo: 

$$
\mathbb {E} \left[ Z _ {1} \right] = \frac {2}{9} + \frac {3}{9} + \frac {4}{3} = \frac {1 7}{9} \quad \mathbb {E} \left[ Z _ {2} \right] = \frac {1 3}{4}
$$

Il teorema della media condizionata si scrive: 

$$
\mathbb {E} \left[ Z _ {1} \right] = \mathbb {E} \left[ \mathbb {E} \left[ Z _ {1} | Y _ {1} \right] \right]
$$

$$
\mathbb {E} \left[ Z _ {2} \right] = \mathbb {E} \left[ \mathbb {E} \left[ Z _ {2} | Y _ {2} \right] \right]
$$

per cui occorre calcolare $p _ { X _ { 1 } | Y _ { 1 } } ( x _ { 1 } | y _ { 1 } ) , p _ { Y _ { 1 } } ( y _ { 1 } ) , p _ { X _ { 2 } | Y _ { 2 } } ( x _ { 2 } | y _ { 2 } , p _ { Y _ { 2 } } ( y _ { 2 } )$ Dal momento che 

$$
p _ {X _ {1} | Y _ {1}} (x _ {1} | y _ {1}) = \frac {p _ {X _ {1} , Y _ {1}} (x _ {1} , y _ {1})}{p _ {Y _ {1}} (y _ {1})} \quad p _ {X _ {2} | Y _ {2}} (x _ {2} | y _ {2}) = \frac {p _ {X _ {2} , Y _ {2}} (x _ {2} , y _ {2})}{p _ {Y _ {2}} (y _ {2})}
$$

calcoliamo innanzitutto $p _ { Y _ { 1 } } ( y _ { 1 } ) \mathtt { e } p _ { Y _ { 2 } } ( y _ { 2 } )$ mediante marginalizzazione delle relative congiunte. 

## Esempio di applicazione - 2

$$
p _ {Y _ {1}} (0) = p _ {X _ {1}, Y _ {1}} (0, 0) + p _ {X _ {1}, Y _ {1}} (1, 0) = \frac {4}{9} \quad p _ {Y _ {1}} (1) = 1 - p _ {Y _ {1}} (0) = \frac {5}{9}
$$

$$
p _ {Y _ {2}} (- 1) = p _ {X _ {2}, Y _ {2}} (- 1, - 1) + p _ {X _ {2}, Y _ {2}} (1, - 1) = \frac {3}{8} \quad p _ {Y _ {2}} (1) = 1 - p _ {Y _ {2}} (- 1) = \frac {5}{8}
$$

Pertanto le condizionali si scrivono: 

<table><tr><td><eq>(x_1, y_1)</eq></td><td><eq>p_{X_1}|_{Y_1}(x_1|y_1)</eq></td></tr><tr><td>00</td><td><eq>\frac{1}{3} \frac{9}{4} = \frac{3}{4}</eq></td></tr><tr><td>01</td><td><eq>\frac{2}{9} \frac{9}{5} = \frac{2}{5}</eq></td></tr><tr><td>10</td><td><eq>\frac{1}{9} \frac{9}{4} = \frac{1}{4}</eq></td></tr><tr><td>11</td><td><eq>\frac{1}{3} \frac{9}{5} = \frac{3}{5}</eq></td></tr></table>

<table><tr><td><eq>(x_{2},y_{2})</eq></td><td><eq>pX_{2}|Y_{2}(x_{2}|y_{2})</eq></td></tr><tr><td>(-1,-1)</td><td><eq>\frac{1}{4}\frac{8}{3}=\frac{2}{3}</eq></td></tr><tr><td>(-1,1)</td><td><eq>\frac{1}{2}\frac{8}{5}=\frac{4}{5}</eq></td></tr><tr><td>(1,-1)</td><td><eq>\frac{1}{8}\frac{8}{3}=\frac{1}{3}</eq></td></tr><tr><td>(1,1)</td><td><eq>\frac{1}{8}\frac{8}{5}=\frac{1}{5}</eq></td></tr></table>

Ci limitamo all’applicazione a $Z _ { 1 }$ , lasciando per esercizio l’applicazione a $Z _ { 2 }$ 

$$
\mathbb {E} \left[ Z _ {1} | Y _ {1} = 0 \right] = \mathbb {E} \left[ 3 X _ {1} ^ {2} + Y _ {1} | Y _ {1} = 0 \right] = \mathbb {E} \left[ 3 X _ {1} ^ {2} | Y _ {1} = 0 \right] = 3 p _ {X _ {1} | Y _ {1}} (1 | 0) = \frac {3}{4}
$$

$$
\mathbb {E} \left[ Z _ {1} | Y _ {1} = 1 \right] = 3 \mathbb {E} \left[ X _ {1} ^ {2} | Y _ {1} = 1 \right] + 1 = 3 p _ {X _ {1} | Y _ {1}} (1 | 1) + 1 = \frac {1 4}{5} \Longrightarrow
$$

$$
\mathbb {E} \left[ Z _ {1} \right] = p _ {Y _ {1}} (0) \mathbb {E} \left[ Z _ {1} | Y _ {1} = 0 \right] + p _ {Y _ {1}} (1) \mathbb {E} \left[ Z _ {1} | Y _ {1} = 1 \right] = \frac {4}{9} \frac {3}{4} + \frac {5}{9} \frac {1 4}{5} = \frac {1 7}{9}
$$

## La covarianza tra due variabili aleatorie - 1

Sia $( X , Y ) \sim p { x , } \{ x , y \} , ( x , y ) \in \mathcal { X } \times \mathcal { Y } ;$ 

Abbiamo visto che le coppie $( \mu _ { X } , \sigma _ { X } ^ { 2 } ) \textsf { e } ( \mu _ { Y } , \sigma _ { Y } ^ { 2 } )$ contengono delle informazion globali - ancorch`e sommarie - delle due marginal $p _ { X } ( x ) \mathrm { ~ e ~ } p _ { Y } ( y )$ 

L’equivalente per le pmf congiunte `e la covarianza, che d`a un’idea - ancora abbastanza sommaria - del grado di ”dipendenza” tra X e Y . 

## Definizioni

Si definisce correlazione tra $X \in Y$ la quantit`a: 

$$
R _ {X, Y} = \mathbb {E} [ X Y ] = \sum_ {x \in \mathcal {X}} \sum_ {y \in \mathcal {Y}} x y p _ {X, Y} (x, y)
$$

Si definisce covarianza di X e Y la quantit`a: 

$$
\sigma_ {X, Y} ^ {2} = \operatorname{COV} [ X, Y ] = \mathbb {E} \left[ (X - \mu_ {X}) (Y - \mu_ {Y}) \right] =
$$

$$
\sum_ {x \in \mathcal {X}} \sum_ {y \in \mathcal {Y}} (x - \mu_ {X}) (y - \mu_ {Y}) p _ {X, Y} (x, y)
$$

## Propriet`a della covarianza - 1

## [a] Relazione tra correlazione e covarianza:

$$
\operatorname{COV} [ X, Y ] = \mathbb {E} [ X Y - \mu_ {X} Y - \mu_ {Y} X + \mu_ {X} \mu_ {Y} ] = \overbrace {\mathbb {E} [ X Y ]} ^ {R _ {X, Y}} - \mu_ {X} \mu_ {Y}
$$

dove si `e sfruttata la linearit`a della media. Si noti che se almeno una delle due variabil ha media nulla $\mathsf { C O V } [ X , Y ] = R x , Y$ 

[b] Due variabili che abbiano covarianza nulla si dicono incorrelate. Si noti che variabili indipendenti sono sempre incorrelate, ma la proposizione non si inverte, nel senso che l’incorrelazione non implica in genere l’indipendenza. 

$$
(X, Y) \sim p _ {X} (x) p _ {Y} (y) \Longrightarrow \operatorname{COV} [ X, Y ] = \sum_ {x \in \mathcal {X}} \sum_ {y \in \mathcal {Y}} (x - \mu_ {X}) (y - \mu_ {Y}) p _ {X} (x) p _ {Y} (y)
$$

$$
= \sum_ {x \in \mathcal {X}} (x - \mu_ {X}) p _ {X} (x) \sum_ {y \in \mathcal {Y}} (y - \mu_ {Y}) p _ {Y} (y) = \mathbb {E} [ X - \mu_ {X} ] \mathbb {E} [ Y - \mu_ {Y} ] = 0
$$

## Propriet`a della covarianza - 2

$$
| \operatorname{COV} [ X, Y ] | \leq \sigma_ {X} \sigma_ {Y}
$$

Questo potrebbe dimostrarsi con la disuguaglianza di Schwartz. Qui preferiamo un’altra strada. Si noti che: 

$$
0 \leq \mathbb {E} \left[ \left(\frac {X - \mu_ {X}}{\sigma_ {X}} \pm \frac {Y - \mu_ {Y}}{\sigma_ {Y}}\right) ^ {2} \right] = \overbrace {\mathbb {E} \left[ \left(\frac {X - \mu_ {X}}{\sigma_ {X}}\right) ^ {2} \right]} ^ {= 1} + \overbrace {\mathbb {E} \left[ \left(\frac {Y - \mu_ {Y}}{\sigma_ {Y}}\right) ^ {2} \right]}
$$

$$
\pm 2 \mathbb {E} \left[ \left(\frac {X - \mu_ {X}}{\sigma_ {X}} \frac {Y - \mu_ {Y}}{\sigma_ {Y}}\right) \right] = 2 \pm 2 \frac {\operatorname{COV} [ X , Y ]}{\sigma_ {X} \sigma_ {Y}} \Longrightarrow - 1 \leq \frac {\operatorname{COV} [ X , Y ]}{\sigma_ {X} \sigma_ {X}} \leq 1
$$

La quantit`a $\begin{array} { r } { \rho _ { X , Y } = \frac { \mathsf { C O V } [ X , Y ] } { \sigma _ { X } \sigma _ { Y } } \in [ - 1 , 1 ] } \end{array}$ si definisce coeficiente di covarianza (ma pi`u spesso di correlazione). 

Infine, definendo $Z = a X + b Y$ , per cui $\mu _ { Z } = a \mu _ { X } + b \mu _ { Y }$ , avremo: 

$$
\sigma_ {Z} ^ {2} = \mathbb {E} [ Z ^ {2} ] - \mu_ {Z} ^ {2} = \mathbb {E} [ a X + b Y ] - (a \mu_ {X} + b \mu_ {Y}) ^ {2} =
$$

$$
= a ^ {2} \sigma_ {X} ^ {2} + b ^ {2} \sigma_ {Y} ^ {2} + 2 a b \mathrm{COV} [ X, Y ]
$$

## Esempio

Date le due pmf congiunte dell’esempio della slide 81 definire quale delle due leggi d probabilit`a congiunta d`a luogo a maggiore coeficiente di correlazione. Ricordiamo che 

<table><tr><td><eq>(x_1, y_1)</eq></td><td><eq>p_{X_1}, y_1(x_1, y_1)</eq></td></tr><tr><td>00</td><td><eq>\frac{1}{3}</eq></td></tr><tr><td>01</td><td><eq>\frac{2}{9}</eq></td></tr><tr><td>10</td><td><eq>\frac{1}{9}</eq></td></tr><tr><td>11</td><td><eq>\frac{1}{3}</eq></td></tr></table>

<table><tr><td><eq>(x_2, y_2)</eq></td><td><eq>pX_2, Y_2(x_2, y_2)</eq></td></tr><tr><td>(-1,-1)</td><td><eq>\frac{1}{4}</eq></td></tr><tr><td>(-1,1)</td><td><eq>\frac{1}{2}</eq></td></tr><tr><td>(1,-1)</td><td><eq>\frac{1}{8}</eq></td></tr><tr><td>(1,1)</td><td><eq>\frac{1}{8}</eq></td></tr></table>

Pertanto le marginali di $X _ { 1 } , X _ { 2 } , Y _ { 1 } \in Y _ { 2 }$ si scrivono: 

<table><tr><td><eq>X_1</eq></td><td><eq>p_{X_1}(x_1)</eq></td></tr><tr><td>0</td><td><eq>\frac{5}{9}</eq></td></tr><tr><td>1</td><td><eq>\frac{4}{9}</eq></td></tr></table>

<table><tr><td><eq>Y_1</eq></td><td><eq>p_{Y_1}(y_1)</eq></td></tr><tr><td>0</td><td><eq>\frac{4}{9}</eq></td></tr><tr><td>1</td><td><eq>\frac{5}{9}</eq></td></tr></table>

<table><tr><td><eq>X_{2}</eq></td><td><eq>p_{X_{2}}(x_{2})</eq></td></tr><tr><td>-1</td><td><eq>\frac{3}{4}</eq></td></tr><tr><td>1</td><td><eq>\frac{1}{4}</eq></td></tr></table>

<table><tr><td><eq>Y_2</eq></td><td><eq>p_{Y_2}(y_2)</eq></td></tr><tr><td>-1</td><td><eq>\frac{3}{8}</eq></td></tr><tr><td>1</td><td><eq>\frac{5}{8}</eq></td></tr></table>

$$
\mathbb {E} [ X _ {1} ] = \mu_ {X _ {1}} = \frac {4}{9}
$$

$$
\mathbb {E} [ Y _ {1} ] = \mu_ {Y _ {1}} = \frac {5}{9}
$$

$$
\mathbb {E} [ X _ {2} ] = \mu_ {X _ {2}} = - \frac {1}{2}
$$

$$
\mathbb {E} [ Y _ {2} ] = \mu_ {Y _ {2}} = \frac {1}{4}
$$

$$
\sigma_ {X _ {1}} ^ {2} = \mathbb {E} [ X _ {1} ^ {2} ] - \mu_ {X _ {1}} ^ {2} = 0. 2 4 7
$$

$$
\sigma_ {Y _ {1}} ^ {2} = \mathbb {E} [ Y _ {1} ^ {2} ] - \mu_ {Y _ {1}} ^ {2} = 0. 2 4 7
$$

$$
\sigma_ {X _ {2}} ^ {2} = \frac {3}{4}
$$

$$
\sigma_ {Y _ {2}} ^ {2} = \frac {1 5}{1 6} = 0. 9 3 7 5
$$

## Esempio (continuazione)

Passiamo ora al calcolo delle covarianze. Avremo: 

$$
\mathbb {E} [ X _ {1} Y _ {1} ] = p x _ {1}, y _ {1} (1, 1) = \frac {1}{3} \Longrightarrow \operatorname{COV} (X _ {1}, Y _ {1}) = \frac {1}{3} - \frac {2 0}{8 1} = \frac {7}{8 1} = 0. 0 8 6
$$

$$
\begin{array}{c} \mathbb {E} [ X _ {2} Y _ {2} ] = p x _ {2}, y _ {2} (- 1, - 1) - p x _ {2}, y _ {2} (- 1, 1) - p x _ {2}, y _ {2} (1, - 1) + p x _ {2}, y _ {2} (1, 1) = \frac {3}{8} - \frac {5}{8} = - \frac {1}{4} \\ \implies \text { COV } (X _ {2}, Y _ {2}) = - \frac {1}{4} + \frac {1}{8} = - \frac {1}{8} \end{array}
$$

Quindi: 

$$
\rho_ {X _ {1}, Y _ {1}} = \frac {\operatorname{COV} \left(X _ {1} , Y _ {1}\right)}{\sigma_ {X _ {1}} \sigma_ {Y _ {1}}} = 0. 3 4 8 \quad \rho_ {X _ {2}, Y _ {2}} = \frac {\operatorname{COV} \left(X _ {2} , Y _ {2}\right)}{\sigma_ {X _ {2}} \sigma_ {Y _ {2}}} = - 0. 1 4 9
$$

Essendo $| \rho _ { X _ { 1 } , Y _ { 1 } } | > | \rho _ { X _ { 2 } , Y _ { 2 } } |$ , la coppia $( X _ { 1 } , Y _ { 1 } )$ risulta a correlazione assoluta maggiore. Si tenga per`o presente che l’essere negativamente correlate implica che ci si aspetta che $X _ { 2 }$ e $Y _ { 2 }$ abbiano segno diverso e che diversi siano i segni delle deviazion dalle rispettive medie! 

## Qualche considerazione iniziale

Rimuoviamo ora l’ipotesi che lo spazio dei campioni Ω sia discreto. 

In particolare, supponiamo d’ora in poi che $\Omega \subseteq \mathbb { R }$ sia un sottoinsieme continuo dell’insieme reale; 

Ω potrebbe essere quindi esso stesso lo spazio delle misure osservabili oppure potrebbe essere il dominio di una applicazione: 

$$
X: \omega \in \Omega \to X (\omega) \in \mathcal {X}
$$

Naturalmente, su X non varr`a pi`u la limitazione che esso sia un insieme finito; 

Spesso accade che $X ( \omega ) = \omega \in \mathcal { X } = \Omega .$ 

## Esempio

La tensione misurata a vuoto ai capi di un carico resistivo `e sempre non nulla per efetto dell’agitazione termica degli elettroni. 

a Si assuma di misurare n volte tale tensione: avremmo ovviamente che $X ( \omega ) = \omega = x \in \mathbb { R }$ e i risultati delle misure saranno $\{ x _ { i } \} _ { i = 1 } ^ { n }$ 

b Si supponga di misurare la potenza trasferita al carico resistivo R. In questo caso lo spazio campione sar`a ancora Ω, ma la corrispondente variabile aleatoria sar`a $X ( \omega ) = \omega ^ { 2 } / R = x \in \mathbb { R }$ 

## Qualche considerazione iniziale

Continuando con l’esempio precedente, `e chiaro che gli eventi elementar saranno in entrambi i casi $\{ X ( \omega _ { i } ) = x _ { i } \}$ ; 

Si potrebbe quindi essere tentati di definire: 

$$
\mathbb {P} \left(X = x _ {i}\right) = \lim _ {n \rightarrow \infty} \frac {n _ {X = x _ {i}}}{n}
$$

dove, come nel caso discreto, ${ \boldsymbol { n } } _ { X = x _ { i } }$ rappresenta il numero di occorrenze dell’evento al pedice; 

Il problema di questa definizione - peraltro corretta - `e che, se $X ( \omega _ { i } ) \in X ( \omega _ { j } )$ sono due realizzazioni distinte di una variabile aleatoria reale non saremo mai in grado di misurarle con esattezza: dovremmo infatti disporre di uno strumento a precisione infinita e - anche in questo caso - l’evento $\{ X ( \omega _ { i } ) = X ( \omega _ { j } ) \}$ } sarebbe impossibile; 

Quello che possiamo dire `e se la misura $X ( \omega _ { j } )$ cada o meno in un intorno della misura $X ( \omega _ { i } )$ 

Quindi, se $X ( \omega )$ `e una variabile aleatoria continua, gli eventi elementar $\{ X ( \omega ) = x \}$ hanno - a meno di casi degeneri - probabilit`a nulla. 

## Esperimenti e variabili continue

Supponiamo di compiere n esperimenti, cos`ı da disporre di una collezione $\{ X ( \omega _ { i } ) \}$ di osservazioni di una variabile aleatoria continua $X ( \omega )$ 

Sia $x \in \mathcal { X }$ : ci chiediamo quale sia la frequenza di coccorrenza dell’evento {X cade in un intorno di dimensione $\Delta x { \mathrm { \sf ~ d i ~ } } x \}$ . In conformit`a a quanto fatto in precedenza, avremo: 

$$
f _ {n} (x; \Delta x) = \frac {n _ {\{x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \}}}{n}
$$

dove ora $\begin{array} { r } { \begin{array} { r } { n _ { \{ x - \frac { \Delta x } { 2 } \leq X \leq x + \frac { \Delta x } { 2 } \} } } \end{array} } \end{array}$ `e il numero di volte (su n esperimenti) in cu osserviamo $\begin{array} { r } { x - \frac { \Delta x } { 2 } \leq X ( \omega ) \leq x + \frac { \Delta x } { 2 } } \end{array}$ 

Possiamo allora definire la probabilit`a dell’evento $\begin{array} { r } { \left\{ x - \frac { \Delta x } { 2 } \leq X \leq x + \frac { \Delta x } { 2 } \right\} } \end{array}$ nella forma usuale (si riguardi l’avvertenza sulle notazioni della slide 45): 

$$
\mathbb {P} \left(\omega \in \Omega : \left\{x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \right\}\right) = \mathbb {P} \left(X \in \left[ x - \frac {\Delta x}{2}, x + \frac {\Delta x}{2} \right]\right) =
$$

$$
P _ {X} (x; \Delta x) = \lim _ {n \to \infty} f _ {n} (x; \Delta x)
$$

## Densit`a di probabilit`a (probability density function, pdf)

Si definisce densit`a di probabilit`a (probability density function, pdf) della variabile aleatoria continua X la funzione: 

$$
f _ {X} (x) = \lim _ {\Delta x \rightarrow 0} \frac {\mathbb {P} \left(x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2}\right)}{\Delta x} = \lim _ {\Delta x \rightarrow 0} \frac {P _ {X} (x ; \Delta x)}{\Delta x}
$$

Per il teorema fondamentale del calcolo integrale abbiamo quindi: 

$$
\mathbb {P} \left(x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2}\right) = \int_ {x - \frac {\Delta x}{2}} ^ {x + \frac {\Delta x}{2}} f _ {X} (t) d t
$$

Le densit`a di probabilit`a devono soddisfare dei vincoli costitutivi, cio`e: 

a $f _ { X } ( x ) \geq 0 \forall x \in \mathbb { R }$ : infatti il suo integrale su un qualunque intervallo non pu`o essere negativo. Basterebbe, in linea di principio, una non-negativit`a quasi ovunque. 

b $f _ { X } ( x )$ `e sommabile su <sup>R</sup> e a integrale unitario. Infatti: 

$$
\int_ {- \infty} ^ {+ \infty} f _ {X} (t) d t = \mathbb {P} (X \in \mathbb {R}) = 1
$$

## Qualche commento intuitivo sulla pdf -1

Supponiamo di considerare un oggetto qualsiasi C, che occupi quindi un continuum di punti, $C \subseteq \mathbb { R } ^ { 3 }$ ; 

Esistono vari modi di ”misurarne” la dimensione, per esempio la Massa (M) e il volume (V ). 

Il criterio di misura (in breve, la misura - $\mu - )$ deve per`o soddisfare tre requisiti: 1) $\mu ( A ) \geq 0 \forall A \subseteq C$ ; 

2) $\mu ( \varnothing ) = 0 ;$ 

3) Se $A _ { 1 } \subseteq C , A _ { 2 } \subseteq C : A _ { 1 } \cap A _ { 2 } = \varnothing$ allora $\mu ( A _ { 1 } \cup A _ { 2 } ) = \mu ( A _ { 1 } ) + \mu ( A _ { 2 } )$ 

Si noti che sia $M ( A )$ che $V ( A )$ soddisfano queste condizioni; 

Si consideri allora $P = ( x , y , z ) \in C$ e un suo intorno $\mathcal { T } ( P )$ (per esempio, una piccola sfera). Si definisce densit`a dell’oggetto C nel punto P la quantit`a: 

$$
\rho (\boldsymbol {P}) = \lim _ {V (\mathcal {I} (\boldsymbol {P})) \rightarrow 0} \frac {M (\mathcal {I} (\boldsymbol {P}))}{V (\mathcal {I} (\boldsymbol {P}))} \rightarrow M (A) = \int_ {A} \rho (\boldsymbol {P}) d V (\mathcal {I} (\boldsymbol {P})) = \int_ {A} \rho (x, y, z) d x d y d z
$$

che potremmo definire mdf, mass density function. 

La nozione si generalizza a insiemi arbitrari. Ovviamente, occorrer`a comunque definire per un insieme ”non canonico” la nozione di intorno (e quindi dare all’insieme una struttura topologica) e strutturare il dominio su cui si applica la funzione ”misura” in modo adeguato, - cio`e introdurre uno spazio di misura - ma questo esula dallo scopo del corso. 

## Qualche commento intuitivo sulla pdf - 2

## Torniamo ora a Ω che - per evitare complicazioni topologiche - assumeremo coincidente con <sup>R</sup>.

Il modo ordinario di misurare sottoinsiemi di $\Omega$ (cio`e, intervalli) `e la misura d Lebesgue, cio`e la loro lunghezza: $\begin{array} { r } { \mu _ { 0 } \left( \left[ x - \frac { \Delta x } { 2 } , x + \frac { \Delta _ { x } } { 2 } \right] \right) = \Delta x ; } \end{array}$ 

Un modo ”alternativo” potrebbe essere: $\begin{array} { r } { \mu _ { 1 } \left( \left[ x - \frac { \Delta x } { 2 } , x + \frac { \Delta x } { 2 } \right] \right) = P _ { X } ( x ; \Delta x ) , } \end{array}$ purch`e, ovviamente, $\mu _ { 1 }$ soddisfi le condizioni per essere una misura. 

All’uopo notiamo che: 

$$
a \mu_ {1} (A) \geq 0 \forall A \subseteq \Omega ;
$$

b Se $A _ { 1 } \cap A _ { 2 } = \emptyset$ allora $\begin{array} { r } { X ( A _ { 1 } ) = \left( \left[ x _ { 1 } - \frac { \Delta _ { x } } { 2 } , x _ { 1 } + \frac { \Delta _ { x } } { 2 } \right] \right) } \end{array}$ $\begin{array} { r } { X ( A _ { 2 } ) = \left( \left[ x _ { 2 } - \frac { \Delta _ { x } } { 2 } , x _ { 2 } + \frac { \Delta _ { x } } { 2 } \right] \right) \mathbb { I } } \end{array}$ e i due intervalli sono disgiunti, per cui: 

$$
\mu_ {1} (A _ {1} \cup A _ {2}) = \mathbb {P} (A _ {1} \cup A _ {2}) = P _ {X} (x _ {1}; \Delta x) + P _ {X} (x _ {2}; \Delta x)
$$

c Infine $\mu _ { 1 } ( \varnothing ) = \operatorname { \mathbb { P } } ( \varnothing ) = \operatorname { \mathbb { P } } ( X \notin \mathbb { R } ) = 0 ;$ 

Quindi, come per massa-volume in ${ \mathbb { R } } ^ { 3 }$ , avremo: 

$$
f _ {X} (x) = \lim _ {\mu_ {0} \left(\left[ x - \frac {\Delta x}{2}, x + \frac {\Delta x}{2} \right]\right)\rightarrow 0} \frac {\mu_ {1} \left(\left[ x - \frac {\Delta x}{2} , x + \frac {\Delta x}{2} \right]\right)}{\mu_ {0} \left(\left[ x - \frac {\Delta x}{2} , x + \frac {\Delta x}{2} \right]\right)} = \lim _ {\Delta x \rightarrow 0} \frac {P _ {X} (x ; \Delta x)}{\Delta x}
$$

## La DF come pdf

## Ritorniamo un momento sugli spazi discreti.

Se $A \subseteq \Omega \ { \dot { \mathsf { e } } }$ un insieme discreto, la misura ”ordinaria” `e ovviamente $\mu _ { 0 } ( A ) = c ( A ) = | A |$ , anche detta ”misura di conteggio”. 

Sia $\omega \in \Omega$ e sia $X ( \omega _ { * } ) = X _ { * }$ : la misura ordinaria di $\{ \omega _ { * } \}$ sarebbe ovviamente $c ( \{ \omega _ { * } \} ) = 1$ . Una misura alternativa `e $\mu _ { 1 } ( \omega _ { * } ) = \mathbb { P } ( \omega _ { * } : X ( \omega _ { * } ) = x _ { * } ) = p _ { X } ( x _ { * } )$ 

Pertanto la densit`a d $\mu _ { 1 } ( \omega _ { * } )$ rispetto a $\mu _ { 0 } ( \omega _ { * } ) \dot { \in } p _ { X } ( x _ { * } )$ e possiamo scrivere (simbolicamente): 

$$
p _ {X} (x _ {*}) = \left. \frac {d \mu_ {1} (\omega)}{d c (\omega)} \right| _ {\omega = \omega^ {*}}
$$

Se $A \subseteq \Omega \ \in X ( A ) = { \mathcal { X } } _ { A } \subseteq { \mathcal { X } }$ , avremo allora: 

$$
\mu_ {1} (A) = \mathbb {P} (A) = \int_ {A} d \mu_ {1} (\omega) = \int_ {\mathcal {X} _ {A}} p _ {X} (x) d c (x) = \sum_ {x \in \mathcal {X} _ {A}} p _ {X} (x)
$$

dove l’integrale `e un integrale di Lebesgue rispetto alla misura di conteggio. 

Quindi, in generale la DF `e una particolare pdf: questo lascia intuire che tutte le propriet`a dimostrate per le DF si estendono alle pdf (e, con opportun cambiamenti, a tutte le densit`a di una misura rispetto a un’altra). 

## La Cumulative Distribution Function (CDF)

Si noti preliminarmente che $f _ { X } ( x ) , x \in \mathbb { R } \ { \dot { \mathrm { ~ e ~ } } }$ perfettamente adeguata a caratterizzare X . Infatti: 

$$
\operatorname{supp} \left[ f _ {X} (x) \right] = \mathcal {X} \quad \mathbb {P} \left(a _ {1} \leq X \leq a _ {2}\right) = \int_ {a _ {1}} ^ {a _ {2}} f _ {X} (t) d t
$$

dove supp[g(·)] indica il supporto della funzione $g ( \cdot )$ 

Tuttavia `e invalso l’uso di caratterizzazioni alternative, e tra queste la Cumulative Distribution Function (CDF): 

$$
F _ {X} (x) = \mathbb {P} (- \infty <   X \leq x) = \int_ {- \infty} ^ {x} f _ {X} (t) d t \rightarrow f _ {X} (x) = \frac {d F _ {X} (x)}{d x}
$$

Talvolta si fa riferimento alla Complementary Cumulative Distribution Function (CCDF): 

$$
\overline {{F}} _ {X} (x) = \mathbb {P} (X > x) = \int_ {x} ^ {\infty} f _ {X} (t) d t = 1 - F _ {X} (x) \rightarrow f _ {X} (x) = - \frac {d \overline {{F}} _ {X} (x)}{d x}
$$

## Propriet`a della CDF

Le propriet`a derivano banalmente dalla definizione. In particolare: 

$F _ { X } ( x ) \in [ 0 , 1 ]$ , in quanto `e una probabilit`a; 

$F _ { X } ( - \infty ) = 0 \textsf { e } F _ { X } ( + \infty ) = 1$ (in quanto funzione integrale di una pdf); 

$F _ { X } ( x )$ `e continua (in quanto funzione integrale di una funzione sommabile); 

$F _ { X } ( x )$ `e crescente, in quanto l’integrando $f _ { X } ( \cdot ) \ \dot { \mathrm { e } }$ non negativo; 

Ovviamente risulta 

$$
\mathbb {P} \left(a _ {1} \leq X \leq a _ {2}\right) = \int_ {a _ {1}} ^ {a _ {2}} f _ {X} (t) d t = F _ {X} \left(a _ {2}\right) - F _ {X} \left(a _ {1}\right)
$$

Nota Bene La CDF potrebbe definirsi anche per variabili discrete, nel qual caso la propriet`a di continuit`a andrebbe ”rimodulata”. Tuttavia la CDF di variabili discrete non $\grave { \mathbf { e } }$ una grandezza utile. 

## Media statistica di variabili continue - 1

Data una variabile aleatoria continua con pdf $f _ { X } ( x )$ , definiamo la sua media statistica come: 

$$
\mathbb {E} [ X ] = \mu_ {X} = \int_ {\mathbb {R}} x f _ {X} (x) d x
$$

Per giustificare questa definizione, possiamo usare vari argomenti. 

Si cominci con il considerare una versione ”quantizzata di X nella forma: 

$$
X ^ {\Delta} = x _ {i} \in [ i \Delta , (i + 1) \Delta [ \text {se} i \Delta \leq X <   (i + 1) \Delta \rightarrow \mathbb {P} (X = x _ {i}) = \int_ {i \Delta} ^ {(i + 1) \Delta} f _ {X} (x) d x
$$

Ovviamente avremo: 

$$
\mathbb {E} \left[ X ^ {\Delta} \right] = \sum_ {i = - \infty} ^ {\infty} x _ {i} \underbrace {\int_ {i \Delta} ^ {(i + 1) \Delta} f _ {X} (x) d x} _ {p _ {X \Delta} (x _ {i})}
$$

Infine, se $x f _ { X } ( x ) \ { \overset { } { \in } }$ integrabile secondo Riemann: 

$$
\mathbb {E} [ X ] = \lim _ {\Delta \rightarrow 0} \mathbb {E} [ X ^ {\Delta} ] = \lim _ {\Delta \rightarrow 0} \sum_ {i = - \infty} ^ {\infty} x _ {i} f _ {X} (x _ {i}) \Delta = \int_ {\mathbb {R}} x f _ {X} (x) d x
$$

## Media statistica di variabili continue - 2

Un’altra giustificazione `e quella alla luce delle considerazioni intuitive sulla riducibilit`a di una DF a una pdf. Infatti, se $\Omega \ { \dot { \mathsf { e } } }$ uno spazio discreto, sappiamo che: 

$$
\mathbb {E} \left[ X \right] = \sum_ {x \in \mathcal {X}} x p _ {X} (x) = \int_ {\mathcal {X}} x f _ {X} (x) d c (x) = \int_ {\Omega} X (\omega) d \mu_ {1} (\omega)
$$

dove $\mu _ { 1 } ( \cdot ) \textsf { e }$ la misura di probabilit`a introdotta su $\Omega$ con densit`a (rispetto alla misura di conteggio) $\begin{array} { r } { \frac { d \mu _ { 1 } ( \omega ) } { d c ( \omega ) } = p _ { X } [ x ( \omega ) ] } \end{array}$ 

Quindi possiamo definire la media statistica di una variabile aleatoria (non importa se discreta o continua) nella forma 

$$
\mathbb {E} [ X ] = \int_ {\Omega} X (\omega) d \mu_ {1} (\omega)
$$

dove l’integrale `e un integrale di Lebesgue. Per $\Omega = \mathbb { R }$ avremo ovviamente $d \mu _ { 1 } ( \omega ) = f _ { X } ( x )$ dx, per cui 

$$
\mathbb {E} [ X ] = \int_ {\mathbb {R}} x f _ {X} (x) d x
$$

## Variabili Uniformi

Una variabile aleatoria X si dice uniformemente distribuita su un intervallo [a, b], $b \geq a \left( X \sim \mathcal { U } \left( a , b \right) \right)$ se: 

$$
f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{b - a} & x \in [ a, b ] \\ 0 & \text { altrove } \end{array} \right.
$$

Siccome supp $[ f _ { X } ( x ) ] = [ a , b ]$ , tale `e il suo alfabeto (cio`e X non assume valori esterni all’intervallo). La sua CDF si scrive quindi: 

$$
F _ {X} (x) = \int_ {- \infty} ^ {x} f _ {X} (t)   d t = \left\{ \begin{array}{l l} 0 & x <   a \\ \frac {x - a}{b - a} & a \leq x \leq b \\ 1 & x \geq b \end{array} \right.
$$

mentre la sua media statistica vale: 

$$
\mathbb {E} [ X ] = \int_ {a} ^ {b} \frac {x}{b - a} d x = \frac {b ^ {2} - a ^ {2}}{2 (b - a)} = \frac {a + b}{2}
$$

L’andamento di pdf e CDF sono mostrati nella successiva slide 

## pdf e CDF di variabili uniformi

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c3f6dc9e2a801980935c1605a6b11fb0b0f1678de5a63bed040d1bda1182b2e0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/e00a692547928dec972c2b70ba912cb5b50498747f1c6f2e70e64a8250e0a9f7.jpg)


Variabili esponenziali 

Una variabile aleatoria X si dice esponenziale con parametro $\lambda \left( X \sim { \mathcal { E } } ( \lambda ) \right)$ ) se ha una pdf: 

$$
f _ {X} (x) = \lambda e ^ {- \lambda x} u (x), \quad u (x) \text {   gradino   unitario   continuo   }
$$

per cui sup $[ f _ { X } ( x ) ] = [ 0 , \infty [ ,$ il che implica $X \geq 0$ 

La sua CDF vale dunque: 

$$
F _ {X} (x) = \int_ {0} ^ {x} \lambda e ^ {- \lambda t} d t = \left(1 - e ^ {- \lambda x}\right) u (x)
$$

La sua media vale infine: 

$$
\mathbb {E} [ X ] = \lambda \int_ {0} ^ {\infty} x e ^ {- \lambda x} d x = \frac {1}{\lambda}
$$

I relativi andamenti sono mostrati nella prossima slide. 

## pdf e CDF di variabili esponenziali

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/08ab3fd5b2e073a6d017a7f7cdf795cbed576c47f81a07d9415e45dde49d254f.jpg)



CDF di X ∼ ε(λ)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/d6303810f7e1eab90d297d7ecd1e8a382e49fb1d59f93cbc76fb80a71f91ff09.jpg)


## Variabili laplaciane

Una variabile aleatoria X si dice laplaciana con parametro $\lambda \left( X \sim { \mathcal { L } } ( \lambda ) \right)$ se ha una pdf: 

$$
f _ {X} (x) = \frac {\lambda}{2} e ^ {- \lambda | x |}
$$

per cui supp $[ f _ { X } ( x ) ] = \mathbb { R }$ , il che implica X pu`o assumere qualunque valore reale.. La sua CDF vale dunque: 

$$
F _ {X} (x) = \int_ {- \infty} ^ {x} \frac {\lambda}{2} e ^ {- \lambda | t |}   d t = \left\{ \begin{array}{l l} \frac {\lambda}{2} \int_ {- \infty} e ^ {\lambda t}   d t = \frac {1}{2} e ^ {\lambda x} & x \leq 0 \\ \frac {\lambda}{2} \left[ \int_ {- \infty} ^ {0} e ^ {\lambda t}   d t + \int_ {0} ^ {x} e ^ {- \lambda t}   d t \right] = 1 - \frac {1}{2} e ^ {- \lambda x} & x \geq 0 \end{array} \right.
$$

La sua media `e nulla, come sempre accade per le pdf pari. Infatti: 

$$
\mathbb {E} [ X ] = \frac {\lambda}{2} \int_ {- \infty} ^ {\infty} x e ^ {- \lambda | x |} d x = 0
$$

I relativi andamenti sono mostrati nella prossima slide. 

## pdf e CDF di variabili laplaciane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/39f51fa4ff2eb7cb56cb12410ab682f44fdac428a7255317918a58910ce0f602.jpg)



CDF di X ~ L(λ)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/68af4a0c86ad1fc90ac3bdd3f5e7d395f93a4b0223313d87385837c55eea2f86.jpg)


## Variabili di Cauchy

Una variabile aleatoria X si dice di Cauchy con parametr1 $( a , b ) \ ( \boldsymbol { X } \sim \mathcal { C } ( a , b ) )$ se ha una pdf: 

$$
f _ {X} (x) = \frac {1}{b \pi} \frac {1}{1 + \left(\frac {x - a}{b}\right) ^ {2}}
$$

per cui supp $[ f _ { X } ( x ) ] = \mathbb { R }$ , il che implica X pu`o assumere qualunque valore reale.. La sua CDF vale dunque: 

$$
F _ {X} (x) = \frac {1}{b \pi} \int_ {- \infty} ^ {x} \frac {d t}{1 + \left(\frac {t - a}{b}\right) ^ {2}} d t = \frac {1}{2} + \frac {1}{\pi} \arctan \left(\frac {x - a}{b}\right)
$$

La sua media non `e definita, perch`e $x f _ { X } ( x )$ non `e integrabile. Tuttavia `e definibile un punto di simmetria mediante il seguente integrale a valor principale: 

$$
\frac {1}{b \pi} \lim _ {H \to \infty} \int_ {- H} ^ {H} \frac {x}{1 + \left(\frac {x - a}{b}\right) ^ {2}} d x = a
$$

I relativi andamenti sono mostrati nella prossima slide. 

## pdf e CDF di variabili di Cauchy

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/37f192a92d3c0821ce4b3c544298a2f503630eea2717b9e0dc1ae55d1dbeea9d.jpg)



CDF di X ∼ C(a, b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/da62d320d49b4d115fdd49c23baaf8c0b8c15ce9c200a43a8856f458817797aa.jpg)


## pdf condizionate

In modo del tutto analogo a quanto fatto per le variabili discrete, potremo scrivere: 

$$
\mathbb {P} \left[ X \in \left(x - \frac {\Delta x}{2}, x - \frac {\Delta x}{2}\right) \mid A \right] = P _ {X} (x, \Delta x | A) \Rightarrow f _ {X | A} (x) = \lim _ {\Delta x \rightarrow 0} \frac {P _ {X} (x , \Delta x | A)}{\Delta x}
$$

o, anche: 

$$
F _ {X \mid A} (x) = \mathbb {P} (X \leq x \mid A) = \frac {\mathbb {P} (\{X \leq x \} \mid \cap A)}{\mathbb {P} (A)} \Rightarrow f _ {X \mid A} (x) = \frac {d F _ {X \mid A} (x)}{d x}
$$

Per esempio, sia $X \sim { \mathcal { L } } ( \lambda ) \ { \textrm { e } } A = \{ - 1 \leq X \leq 2 \} \quad$ . Avremo: 

$$
F _ {X | \{- 1 \leq X \leq 2 \}} (x) = \frac {\mathbb {P} (\{X \leq x \} \cap \{- 1 \leq X \leq 2 \})}{F _ {X} (- 1 \leq X \leq 2)} = \left\{ \begin{array}{l l} 0 & x <   - 1 \\ \frac {F _ {X} (x) - F _ {X} (- 1)}{F _ {X} (2) - F _ {X} (- 1)} & - 1 \leq x \leq 2 \\ 1 & x \geq 2 \end{array} \right.
$$

$$
f _ {X | \{- 1 \leq X \leq 2 \}} (x) = \left\{ \begin{array}{c l} \frac {f _ {X} (x)}{F _ {X} (2) - F _ {X} (- 1)} = \frac {\frac {\lambda}{2} e ^ {- \lambda | x |}}{1 - \frac {1}{2} e ^ {- 2 \lambda} + \frac {1}{2} e ^ {- \lambda}} & x \in (- 1, 2) \\ 0 & x \notin (- 1, 2) \end{array} \right.
$$

## pdf e CDF condizionali di variabili Laplaciane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c9bb9b6105893847da5816e4162cf664c0a5d6c418d723bc46ff1a263cd47a27.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c151e31d1c7e39157c315436b8b74f28bd1d6631fb7d6d648dfe224e47f288e4.jpg)


## Legge della probabilit`a totale per pdf e medie

In modo del tutto analogo al caso discreto (vedi slide 56) si pu`o mostrare che, se $\{ E _ { m } \} _ { m = 1 } ^ { M }$ `e una qualunque partizione di $\Omega ,$ , allora: 

$$
f _ {X} (x) = \sum_ {m = 1} ^ {M} f _ {X | E _ {m}} (x) \mathbb {P} (E _ {m}) \Longleftrightarrow F _ {X} (x) = \sum_ {m = 1} ^ {M} F _ {X | E _ {m}} (x) \mathbb {P} (E _ {m})
$$

Naturalmente, questo implica che per le medie valga un’analoga relazione (vedi slide 57): 

$$
\mathbb {E} \left[ X \right] = \sum_ {m = 1} ^ {M} \mathbb {E} \left[ X | E _ {m} \right] \mathbb {P} (E _ {m}) = \sum_ {m = 1} ^ {M} \mathbb {P} (E _ {m}) \int_ {\mathbb {R}} x f _ {X | E _ {m}} (x) d x
$$

Quindi, con riferimento all’esempio precedente con $\begin{array} { r } { X \sim \mathcal { L } ( \lambda ) } \end{array}$ 

$$
\mathbb {E} [ X ] = \mathbb {E} \left[ X | \{- 1 \leq X \leq 2 \} \right] \mathbb {P} (- 1 \leq X \leq 2) + \mathbb {E} \left[ X | \{X \notin [ - 1, 2 ] \} \right] \underbrace {\mathbb {P} (X \notin [ - 1 , 2 ])} _ {1 - \mathbb {P} (- 1 \leq X \leq 2)} = 0
$$

## Funzioni di variabili aleatorie continue -1

Quest’argomento riproduce - come problematica - quello gi`a afrontato nel caso d variabili discrete (vedi slide 58 e seguenti). 

Si assuma che $X = X ( \omega )$ sia una variabile aleatoria continua con alfabeto X , pdf $f _ { X } ( x ) \mathrm { ~ e ~ C D F ~ } F _ { X } ( x )$ 

Sia $g ( \cdot )$ una funzione il cui insieme di definizione includa i punti d $\mathcal { X } \mathrm { ~ - ~ } \mathsf { a }$ meno di un sottoinsieme a (misura di) probabilit`a nulla; 

Si forma la nuova variabile aleatoria: 

$$
Y = g (X) = g [ X (\omega) ] \in \mathcal {Y} \quad \text {   dove   } \mathcal {Y} = g (\mathcal {X})
$$

Problema: Ricavare una caratterizzazione di Y dalla caratterizzazione di X in termini di 

pdf/CDF, $p _ { Y } ( y ) , y \in \mathcal { Y } ;$ 

media statistica, $\mathbb { E } [ Y ]$ 

## Funzioni di variabili aleatorie continue -2

A diferenza di quanto fatto nel caso discreto (vedi slide 59 e seguenti), qu distinguiamo tre casi: 

a $\{ g ( x ) \} _ { x \in \mathcal { X } }$ biunivoca, cio`e invertibile $\forall x ,$ , continua e derivabile; 

b $\{ g ( x ) \} _ { x \in \mathcal { X } }$ continua, derivabile e univoca - e quindi non invertibile - con Y continuo; 

$\{ g ( x ) \} _ { x \in \mathcal { X } }$ univoca - e quindi non invertivile - con Y discreto: quest’ultimo caso corrisponde ad una conversione $\mathsf { A } / \mathsf { D }$ della variabile continua (cio`e una sua quantizzazione ovvero compressione con perdite) in analogia a quanto visto nella conversione $\mathsf { A } / \mathsf { D }$ di segnali e sequenza deterministiche. 

## Funzioni invertibili

Ricordiamo che se $y = g ( x )$ `e invertibile, allora essa $\grave { \mathbf { e } }$ strettamente monotona $\forall x \in { \mathcal { X } }$ . Pertanto: 

$g ( x )$ strettamente crescente $( g ^ { \prime } ( x ) > 0 )$ 

$$
F _ {Y} (y) = \mathbb {P} (Y \leq y) = \mathbb {P} (g (X) \leq y) = \mathbb {P} (X \leq g ^ {- 1} (y)) = F _ {X} [ g ^ {- 1} (y) ]
$$

$$
f _ {Y} (y) = \frac {d F _ {Y} (y)}{d y} = f _ {X} [ g ^ {- 1} (y) ] \frac {d g ^ {- 1} (y)}{d y} = \frac {f _ {X} [ g ^ {- 1} (y) ]}{g ^ {\prime} [ g ^ {- 1} (y) ]}
$$

● $g ( x )$ strettamente decrescente $( g ^ { \prime } ( x ) < 0 )$ 

$$
F _ {Y} (y) = \mathbb {P} (Y \leq y) = \mathbb {P} (g (X) \leq y) = \mathbb {P} (X \geq g ^ {- 1} (y)) = 1 - F _ {X} [ g ^ {- 1} (y) ]
$$

$$
f _ {Y} (y) = - \frac {d F _ {Y} (y)}{d y} = f _ {X} [ g ^ {- 1} (y) ] \frac {d g ^ {- 1} (y)}{d y} = \frac {f _ {X} [ g ^ {- 1} (y) ]}{- g ^ {\prime} [ g ^ {- 1} (y) ]}
$$

per cui la pdf $f _ { Y } ( y )$ si scrive in forma unificata: 

$$
f _ {Y} (y) = \frac {f _ {X} [ g ^ {- 1} (y) ]}{| g ^ {\prime} [ g ^ {- 1} (y) ] |}
$$

## Funzioni non invertibili

Si assuma ora che $y = g ( x )$ non sia invertibile. Questo implica che: 

$$
\forall y \in \mathcal {Y} \exists \{x _ {i} (y) \} _ {i = 1} ^ {M (y)}: g [ x _ {i} (y) ] = y
$$

Supponiamo, per fissare le idee, $M ( y ) = 4 , g ^ { \prime } ( x _ { 1 } ) < 0$ : questo implica che $\boldsymbol { g } ( \boldsymbol { x } ) \le \boldsymbol { y }$ $x _ { 1 } ( y ) \leq y \leq x _ { 2 } ( y )$ ; ovviamente, $g ^ { \prime } { \left( x _ { 2 } { \left( y \right) } \right) }$ sar`a positivo e $\boldsymbol { g } ( \boldsymbol { x } ) > y$ per $x _ { 2 } ( y ) \le y \le x _ { 3 } ( y )$ . La funzione ripassa per il valore $g ( x _ { 3 } ( y ) ) = y$ (con derivata negativa) e si mantiene al di sotto di y fino a $x _ { 4 } ( y )$ . Quindi (vedi figura nella prossima slide): 

$$
F _ {Y} (y) = \mathbb {P} (Y \leq y) = \mathbb {P} \left(\left\{x _ {1} (y) \leq X \leq x _ {2} (y) \right\} \cup \left\{x _ {4} (y) \leq X \leq x _ {3} (y) \right\}\right) =
$$

$$
F _ {Y} [ x _ {2} (y) ] - F _ {Y} [ x _ {1} (y) ] + F _ {Y} [ x _ {4} (y) ] - F _ {Y} [ x _ {3} (y) ]
$$

dove si `e ovviamente sfruttata la disgiunzione dei vari intervalli. Pertanto, derivando: 

$$
f _ {Y} (y) = \sum_ {i = 1} ^ {4} (- 1) ^ {i} f _ {X} [ x _ {i} (y) ] x _ {i} ^ {\prime} (y) = \sum_ {i = 1} ^ {4} \frac {f _ {X} [ x _ {i} (y) ]}{| g ^ {\prime} [ x _ {i} (y) ] |}
$$

dove si `e sfruttato il fatto che $\begin{array} { r } { x ^ { \prime } ( y ) = \frac { 1 } { g ^ { \prime } [ g ^ { - 1 } ( y ) ] } } \end{array}$ e che i segni sono alternati. 

## Funzioni non invertibili

$$
f _ {Y} (y _ {1}) = \sum_ {i = 1} ^ {3} f _ {X} \left[ x _ {i} (y _ {1}) \right] \left| \frac {d x _ {i} (y)}{d y} \right| _ {y = y _ {1}} = \sum_ {i = 1} ^ {3} \frac {f _ {X} \left[ x _ {i} (y _ {1}) \right]}{\left| g ^ {\prime} [ x _ {i} (y _ {1}) ] \right|}
$$

$$
f _ {Y} (y _ {2}) = \sum_ {i = 1} ^ {2} f _ {X} \left[ x _ {i} (y _ {2}) \right] \left| \frac {d x _ {i} (y)}{d y} \right| _ {y = y _ {2}} = \sum_ {i = 1} ^ {2} \frac {f _ {X} \left[ x _ {i} (y _ {2}) \right]}{\left| g ^ {\prime} [ x _ {i} (y _ {2}) ] \right|}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/75daf37cde2197ea8b008ceadbbf1a23f380a8edcd7d8eeba4bc90f54e811575.jpg)


## Qualche esempio - 1

Sia $g ( x ) = x ^ { 2 }$ , si considerino $X _ { 1 } \sim \mathcal { E } ( \lambda ) \ \mathrm { ~ e ~ } X _ { 2 } \sim \mathcal { C } ( 0 , 1 )$ . Vogliamo determinare le pdf di $Y _ { 1 } = g ( X _ { 1 } ) = X _ { 1 } ^ { 2 } \mathrm { ~ e ~ } Y _ { 2 } = g ( X _ { 2 } ) = X _ { 2 } ^ { 2 }$ 

Per $Y _ { 1 }$ , si ha che, poich`e $\mathcal { X } _ { 1 } = [ 0 , \infty [ \mathrm { ~ e ~ p o i c h \dot { e } ~ }$ $\ g ( x ) = x ^ { 2 }$ `e biunivoca per $x \ge 0$ , sar`a: 

$$
x ^ {2} = y \rightarrow x (y) = \sqrt {y} \rightarrow x ^ {\prime} (y) = \left. \frac {1}{g ^ {\prime} (x)} \right| _ {x = \sqrt {y}} = \left. \frac {1}{2 x} \right| _ {x = \sqrt {y}} = \frac {1}{2 \sqrt {y}}
$$

Quindi: 

$$
f _ {Y _ {1}} (y) = \left. \lambda e ^ {- \lambda x} u (x) \right| _ {x = \sqrt {y}} x ^ {\prime} (y) = \frac {\lambda}{2 \sqrt {y}} e ^ {- \lambda \sqrt {y}} u (y)
$$

Per $Y _ { 2 }$ , invece, essendo $\mathcal { X } _ { 2 } = \mathbb { R } , g ( x ) = x ^ { 2 }$ non `e biunivoca e l’equazione $x ^ { 2 } = y$ ha due soluzioni, $x ( y ) = \pm { \sqrt { y } }$ . Si noti inoltre che $\mathcal { Y } = [ 0 , + \infty [$ [, cio`e $Y \geq 0$ . Quindi: 

$$
f _ {Y _ {2}} (y) = \left[ \frac {f _ {X} (\sqrt {y})}{| g ^ {\prime} (\sqrt {y}) |} + \frac {f _ {X} (- \sqrt {y})}{| g ^ {\prime} (- \sqrt {y}) |} \right] u (y), \quad \text { poichè } \quad f _ {X} (x) = \frac {1}{\pi} \frac {1}{1 + x ^ {2}} \Rightarrow
$$

$$
f _ {Y _ {2}} (y) = \left(\frac {1}{2 \pi \sqrt {y}} \frac {1}{1 + y} + \frac {1}{2 \pi \sqrt {y}} \frac {1}{1 + y}\right) u (y) = \frac {1}{\pi \sqrt {y}} \frac {1}{1 + y} u (y)
$$

## Qualche esempio - 2

Sia $X \sim f _ { X } ( x )$ . Vogliamo la pdf di $\boldsymbol { Y } = \boldsymbol { F } _ { \boldsymbol { X } } ( \boldsymbol { X } )$ , cio`e assumiamo $g ( x ) = F _ { X } ( x )$ 

0 Notiamo preliminarmente che $\mathcal { V } = [ 0 , 1 ]$ qualunque sia $\mathcal { X }$ . Inoltre, $g ( x ) \ { \dot { \mathsf { e } } }$ monotona crescente: potrebbe non essere strettamente crescente se $\mathcal { X }$ non $\grave { \mathbf { e } }$ connesso, ma escludiamo questo caso. 

Avremo allora: 

$$
g (x) = F _ {X} (x) \rightarrow x (y) = F _ {X} ^ {- 1} (y) \quad g ^ {\prime} (x) = f _ {X} (x) \Longrightarrow
$$

$$
f _ {Y} (y) = \frac {f _ {X} \left[ F _ {X} ^ {- 1} (y) \right]}{f _ {X} \left[ F _ {X} ^ {- 1} (y) \right]} \Pi \left(y - \frac {1}{2}\right) = \Pi \left(y - \frac {1}{2}\right)
$$

cio`e $Y \sim \mathcal { U } ( 0 , 1 )$ 

Quindi, se si ha una variabile aleatoria uniforme $U \sim \mathcal { U } ( 0 , 1 )$ , la trasformazione $X = F _ { X } ^ { - 1 } ( U )$ genera una variabile aleatoria con pdf arbitraria $f _ { X } ( x )$ : Questo ha delle notevoli conseguenze nelle procedure di simulazione dei sistemi numerici. 

## Qualche esempio - 3

Sia $\begin{array} { r } { X \sim \mathcal { U } \left( - \frac { 1 } { 2 } , \frac { 1 } { 2 } \right) , g ( x ) = A \cos ( 2 \pi x + \varphi ) } \end{array}$ : Vogliamo la pdf di $Y = A \cos ( 2 \pi X + \varphi )$ 

Notiamo preliminarmente che $\mathcal { V } = [ - A , A ]$ e che la trasformazione non $\grave { \mathbf { e } }$ biunivoca. Infatti: 

$$
y = A \cos (2 \pi x + \varphi) \rightarrow 2 \pi x (y) + \varphi = \pm \arccos \left(\frac {x}{A}\right)
$$

Valutando la derivata dell’inversa si ha: 

$$
\begin{array}{l} x ^ {\prime} (y) = \frac {1}{g ^ {\prime} (x)} \Big | _ {x = x (y)} = - \frac {1}{2 \pi A \sin (2 \pi x + \varphi)} \Big | _ {2 \pi x = \pm \arccos \left(\frac {y}{A}\right) - \varphi} = \\ = \pm \frac {1}{2 \pi A \sin [ \arccos (\frac {y}{A}) ]} = \pm \frac {1}{2 \pi A \sqrt {1 - (\frac {y}{A}) ^ {2}}} \end{array}
$$

Poich`e $\begin{array} { r } { f _ { X } ( x ) = \Pi \left( x - \frac { 1 } { 2 } \right) } \end{array}$ , applicando le formule precedenti si ha 

$$
f _ {Y} (y) = \frac {1}{\pi A \sqrt {1 - \left(\frac {y}{A}\right) ^ {2}}}, \qquad y \in [ - A, A ]
$$

## Conversione A/D di variabili aleatorie

Quando X `e continua e Y discreta si ha una conversione $\mathsf { A } / \mathsf { D }$ di una quantit`a aleatoria (confronta anche l’ultima sezione della parte ”Conversione $\mathsf { A } / \mathsf { D } ^ { \prime \prime } )$ 

Supponiamo di voler rappresentare (con perdite) X con R bit, cio`e con $M = 2 ^ { R }$ livelli; 

Definiamo una variabile aleatoria $\boldsymbol { Y } = \boldsymbol { g } ( \boldsymbol { X } )$ con $\mathcal { Y } = \{ y _ { 1 } , \dots , y _ { M } \}$ 

Definiamo una partizione di X in M intervalli, definiti dai punt $\{ x _ { i } \} _ { i = 1 } ^ { M + 1 }$ ; 

Si definisce rappresentazione a R bit di X la variabile aleatoria discreta: 

$$
Y = y _ {i} \quad \text { se } x _ {i} \leq X \leq x _ {i + 1} \quad i = 1, \dots , M
$$

La pmf di Y quindi si scrive facilmente nella forma: 

$$
p _ {Y} (y _ {i}) = P _ {X} \left(\frac {x _ {i + 1} + x _ {i}}{2}; \frac {x _ {i + 1} - x _ {i}}{2}\right) = F _ {X} (x _ {i + 1}) - F _ {X} (x _ {i}), \quad i = 1, \ldots , M
$$

Ovviamente tanto la partizione quanto i livelli di rappresentazione sono gradi d libert`a a disposizione del progettista. 

## Media di funzioni di variabili aleatorie continue

Sia $X \sim f _ { X } ( x )$ e sia $Y = g ( X )$ , con $\mathcal { V } = g ( \mathcal { X } )$ . Vogliamo estendere alle variabili continue il Teorema Fondamentale per il calcolo della media (vedi slide 60 e seguenti). Il risultato principale - diretta derivazione del caso discreto - `e che, qualunque sia $g ( x )$ 

$$
\mathbb {E} \left[ Y \right] = \mathbb {E} \left[ g (X) \right] = \int_ {\mathbb {R}} g (x) f _ {X} (x) d x
$$

Definiamo una versione quantizzata di X a M livelli, $x ^ { \Delta }$ , in modo del tutto analogo a quanto fatto per ricavare la media di variabili continue (vedi slide 100); 

A questa applichiamo la trasformazione $g ( \cdot )$ , ottenendo la variabile discreta ${ \cal Y } ^ { \Delta } = g ( X ^ { \Delta } )$ : 

$$
X ^ {\Delta} = x _ {i} \in [ i \Delta , (i + 1) \Delta [ \quad i \Delta \leq X <   (i + 1) \Delta \Rightarrow g (X ^ {\Delta}) = g (x _ {i})
$$

Il teorema quindi segue - se $g ( x ) f _ { X } ( x )$ `e Riemann-integrabile - dall’essere: 

$$
\mathbb {E} \left[ Y \right] = \lim _ {\Delta \rightarrow 0} \mathbb {E} \left[ Y ^ {\Delta} \right] = \lim _ {\Delta \rightarrow 0} \sum_ {i = 1} ^ {M} g (x _ {i}) \underbrace {f _ {X} (x _ {i}) \Delta} _ {\simeq \mathbb {P} (i \Delta \leq X <   (i + 1) \Delta)} = \int_ {\mathbb {R}} g (x) f _ {X} (x)   d x
$$

## Valore quadratico medio e varianza di variabili continue

E a questo punto immediata la generalizzazione dei concetti introdotti nella slide 62<sup>`</sup> per variabili discrete a variabili continue. 

Data una variabile aleatoria $X \sim f _ { X } ( x ) , x \in \mathcal { X }$ , con media $\mu _ { X } = \operatorname { \mathbb { E } } [ X ]$ definiamo: 

Il valore quadratico medio (Mean Square) di X : 

$$
X _ {\mathrm{rms}} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] = \int_ {\mathbb {R}} x ^ {2} f _ {X} (x) d x
$$

Il valore eficace (root mean square, rms) di X : 

$$
X _ {\mathrm{rms}} = \sqrt {\mathbb {E} \left[ X ^ {2} \right]} = \sqrt {\int_ {\mathbb {R}} x ^ {2} f _ {X} (x) d x}
$$

La varianza di X : 

$$
\sigma_ {X} ^ {2} = \mathbb {E} \left[ (X - \mu_ {X}) ^ {2} \right] = \int_ {\mathbb {R}} (x ^ {2} + \mu_ {X} ^ {2} - 2 x \mu_ {X}) f _ {X} (x) d x = X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}
$$

La deviazione standard di X : 

$$
\sigma_ {X} = \sqrt {\sigma_ {X} ^ {2}} = \sqrt {\mathbb {E} [ X ^ {2} ] - \mu_ {X} ^ {2}} = \sqrt {X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}}
$$

Tutte le propriet`a della slide 68 ovviamente valgono per variabili continue. 

## Qualche esempio

Sia $X \sim \mathcal { U } ( a , b )$ . Si ottiene facilmente: 

$$
\mu_ {X} = \frac {a + b}{2} \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {a ^ {2} + b ^ {2} + a b}{3} \qquad \sigma_ {X} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] - \mu_ {X} ^ {2} = \frac {(b - a) ^ {2}}{1 2}
$$

Sia $\begin{array} { r } { X \sim \mathcal { E } ( \lambda ) } \end{array}$ . Avremo: 

$$
\mu_ {X} = \frac {1}{\lambda} \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {2}{\lambda^ {2}} \qquad \sigma_ {X} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] - \mu_ {X} ^ {2} = \frac {1}{\lambda^ {2}}
$$

Sia $\begin{array} { r } { X \sim \mathcal { L } ( \lambda ) } \end{array}$ . Avremo: 

$$
\mu_ {X} = 0 \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {2}{\lambda^ {2}} \qquad \sigma_ {X} ^ {2} = \mathbb {E} [ X ^ {2} ] = \frac {2}{\lambda^ {2}}
$$

Sia $X \sim \mathcal { C } ( a , b )$ : Non esistono in questo caso n`e la media, n`e la varianza, n`e, quindi, valore rms o deviazione standard. 

Variabili continue multiple 

In perfetta analogia con quanto fatto per variabili discrete (vedi slide 69), una coppia di variabili continue (o variabile doppia) `e definita nella forma: 

$$
X, Y: \omega \in \Omega \longrightarrow (X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y} \subseteq \mathbb {R} ^ {2}
$$

dove $\mathcal { X } \in \mathcal { V }$ sono gli alfabeti di X e di Y rispettivamente. 

Analogamente, date tre variabili aleatorie - a questo punto non importa pi`u se tutte continue o meno $\begin{array} { r } { - X ( \omega ) \in \mathcal { X } , y ( \omega ) \in \mathcal { Y } , Z ( \omega ) \in \mathcal { Z } ; } \end{array}$ 

$$
X, Y, Z: \omega \in \Omega \longrightarrow (X (\omega), Y (\omega), Z (\omega)) \in \mathcal {X} \times \mathcal {Y} \times \mathcal {Z} \subseteq \mathbb {R} ^ {3}
$$

e, date m variabili aleatorie $X _ { i } \in \mathcal { X } _ { i } \subseteq \mathbb { R }$ , avremo la m−pla aleatoria: 

$$
X _ {1}, \dots , X _ {m}: \omega \in \Omega \longrightarrow (X _ {1} (\omega), \dots , X _ {m} (\omega)) \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {m} \subseteq \mathbb {R} ^ {m}
$$

## pdf congiunta di due variabili aleatorie

Si consideri una coppia di variabili continue, $X \in \mathcal { X } \mathrm { ~ e ~ } Y \in \mathcal { Y }$ , la loro pdf congiunta s definisce in perfetta analogia con la pdf di variabili continue singole (vedi slide 94): 

$$
\begin{array}{l} f _ {X, Y} (x, y) = \lim _ {\Delta x \to 0} \lim _ {\Delta y \to 0} \frac {\mathbb {P} \left(\left\{x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \right\} \cap \left\{y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2} \right\}\right)}{\Delta x \Delta_ {y}} \\ = \lim _ {\Delta x \to 0} \lim _ {\Delta y \to 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{\Delta x \Delta y} \quad (x, y) \in \mathcal {X} \times \mathcal {Y} \end{array}
$$

Per il teorema fondamentale del calcolo integrale abbiamo quindi che, se $C \subseteq \mathcal { X } \times \mathcal { y }$ 

$$
\mathbb {P} ((X, Y) \in C) = \int_ {C} f _ {X, Y} (x, y) d x d y
$$

Le densit`a di probabilit`a congiunte devono soddisfare dei vincoli costitutivi - simili a quelli delle densit`a marginali: 

$$
a f _ {X, Y} (x, y) \geq 0 \forall (x, y) \in \mathbb {R} ^ {2};
$$

b $f _ { X , Y } ( x , y )$ `e sommabile su $\mathbb { R } ^ { 2 }$ e a integrale unitario. Infatti: 

$$
\int_ {\mathbb {R} ^ {2}} f _ {X, Y} (x, y) d x d y = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} f _ {X, Y} (x, y) d x d y = \mathbb {P} ((X, Y) \in \mathbb {R} ^ {2}) = 1
$$

## Propriet`a della pdf congiunta

La pdf congiunta $f _ { X , Y } ( x , y )$ condivide con la pmf congiunta $p x , \gamma ( x , y ) \textrm { - e }$ , per alcune, con tutte le densit`a - le seguenti propriet`a: 

Propriet`a di marginalizzazione: 

$$
\int_ {\mathbb {R}} f _ {X, Y} (x, y) d y = f _ {X} (x) \qquad \int_ {\mathbb {R}} f _ {X, Y} (x, y) d x = f _ {Y} (y)
$$

per cui caratterizzare congiuntamente $( X , Y )$ significa anche caratterizzarle marginalmente, mentre il viceversa non `e necessariamente vero. 

Indipendenza statistica: due variabili aleatorie sono indipendenti se e solo se 

$$
f _ {X, Y} (x, y) = f _ {X} (x) f _ {Y} (y) \Longleftrightarrow F _ {X, Y} (x, y) = \mathbb {P} (X \leq x, Y \leq y) = F _ {X} (x) F _ {Y} (y)
$$

Pi`u in generale, se $X _ { i } \sim f _ { X _ { i } } ( x ) , x \in \mathcal { X } _ { i }$ , allora esse sono indipendenti se e solo se: 

$$
f _ {X _ {1}, \dots , X _ {m}} (x _ {1}, \dots , x _ {m}) = \prod_ {i = 1} ^ {m} f _ {X _ {i}} (x _ {i}), \qquad (x _ {1}, \dots , x _ {m}) \in \mathbb {R} ^ {m}
$$

## Le pdf condizionate

Si considerino varibili aleatorie $X \in \mathcal { X } \mathrm { ~ e ~ } Y \in \mathcal { Y }$ con assegnata pdf congiunta $f _ { X , Y } ( x , y )$ 

La pdf condizionata di X dato Y si pu`o definire a partire dalla seguente quantit`a (vedi slide 110): 

$$
\mathbb {P} \left(x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \mid y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2}\right) = \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{P _ {Y} (y ; \Delta y)}
$$

Pertanto la densit`a di X condizionata all’evento $\begin{array} { r } { \left\{ y - \frac { \Delta y } { 2 } \leq Y \leq y + \frac { \Delta y } { 2 } \right\} } \end{array}$ `e: 

$$
\lim _ {\Delta x \rightarrow 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{\Delta x P _ {Y} (y ; \Delta y)} = f _ {X | \{y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2} \}} (x | y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2})
$$

Facendo dunque tendere $\Delta y$ a zero, otteniamo: 

$$
f _ {X \mid Y} (x \mid y) = \lim _ {\Delta x \rightarrow 0} \lim _ {\Delta y \rightarrow 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{P _ {Y} (y ; \Delta y)} = \frac {f _ {X , Y} (x , y)}{f _ {Y} (y)}
$$

che, come c’era da attendersi, riproduce l’analoga definizione per la pmf condizionale che, d’altronde, `e essa stessa una densit`a. 

Di conseguenza tutte le propriet`a delle pmf condizionali si estendono alle pdf condizionali. 

## Propriet`a delle pdf condizionate

Data l’analogia con le variabili discrete, ci limitiamo qui a riscrivere le propriet`a della slide 74 

$f _ { X \mid Y } ( x | y )$ se y resta fisso e x varia in X `e una densit`a di probabilit`a, cio`e: 

$$
f _ {X | Y} (x | y) \geq 0 \int_ {\mathbb {R}} f _ {X | Y} (x | y) d x = 1
$$

Legge della probabilit`a totale per le pdf: 

$$
f _ {X} (x) = \int_ {\mathbb {R}} f _ {X, Y} (x, y) d y = \int_ {\mathbb {R}} f _ {X | Y} (x | y) f _ {Y} (y) d y
$$

$$
f _ {Y} (y) = \int_ {\mathbb {R}} f _ {X, Y} (x, y) d x = \int_ {\mathbb {R}} f _ {Y | X} (y | x) f _ {X} (x) d x
$$

Leggi della probabilit`a composta e di Bayes per le densit`a: 

$$
f _ {X, Y} (x, y) = f _ {Y} (y) f _ {X | Y} (x | y) = f _ {X} (x) f _ {Y | X} (y | x) \Rightarrow f _ {Y | X} (y | x) = \frac {f _ {Y} (y) f _ {X | Y} (x | y)}{f _ {X} (x)}
$$

## Altre estensioni...

Come nel caso discreto, avremo: 

Se $Z = \boldsymbol { \mathrm { g } } ( \boldsymbol { X } , \boldsymbol { Y } )$ allora 

$$
\mathbb {E} [ Z ] = \int_ {\mathbb {R} ^ {2}} g (x, y) f _ {X}, \gamma (x, y) d x d y
$$

Linearit`a della media: 

$$
\mathbb {E} \left[ \sum_ {i = 1} ^ {m} a _ {i} X _ {i} \right] = \sum_ {i = 1} ^ {m} a _ {i} \mathbb {E} \left[ X _ {i} \right]
$$

Teorema della media condizionata: 

$$
\mathbb {E} \left[ g (X, Y) \right] = \mathbb {E} \left[ \mathbb {E} \left[ g (X, Y) | Y \right] \right]
$$

dove: 

$$
\mathbb {E} \left[ g (X, Y) | Y = y \right] = \int_ {\mathbb {R}} g (x, y) f _ {X | Y} (x | y) d x = \mathbb {E} \left[ h (Y (\omega)) \right] \Longleftrightarrow
$$

$$
h \left[ Y (\omega) \right] = \int_ {\mathbb {R}} g (x, Y) f _ {X | Y} (x | Y) d x
$$

## Covarianza tra due variabili continue

Siano $( X , Y ) \sim f _ { X , Y } ( x , y )$ . Denotiamo con $( \mu _ { X } , \mu _ { Y } )$ le rispettive medie e $( \sigma _ { X } ^ { 2 } , \sigma _ { Y } ^ { 2 } )$ le rispettive varianze. Avremo, in analogia al caso discreto: 

Covarianza tra $X \in Y ;$ 

$$
\operatorname{COV} [ X, Y ] = \mathbb {E} \left[ (X - \mu_ {X}) (Y - \mu_ {Y}) \right] = \mathbb {E} [ X Y ] - \mu_ {X} \mu_ {Y}
$$

coeficiente di correlazione tra $X \textsf { e Y }$ 

$$
\rho_ {X, Y} = \frac {\operatorname{COV} [ X , Y ]}{\sigma_ {X} \sigma_ {Y}}, \quad \left| \rho_ {X, Y} \right| \leq 1
$$

Incorrelazione tra $X \textsf { e } Y \colon { \mathsf { C O V } } [ X , Y ] = 0$ 

Indipendenza implica incorrelazione, ma incorrelazione non implica indipendenza. 

## Variabili Gaussiane: Caratterizzazione marginale

Una variabile aleatoria $X _ { 0 } \in \mathcal { X } = \mathbb { R }$ si dice Gaussiana (o Normale) standard - $X _ { 0 } \sim \mathcal { N } ( 0 , 1 )$ se: 

$$
f _ {X _ {0}} (x _ {0}) = \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {x _ {0} ^ {2}}{2}}, \quad x \in \mathbb {R} \quad \Longrightarrow \quad \mathbb {E} [ X _ {0} ] = 0 \quad \sigma_ {X _ {0}} ^ {2} = \mathbb {E} [ X _ {0} ^ {2} ] = 1
$$

Consideriamo ora la variabile aleatoria $X = \sigma _ { X } X _ { 0 } + \mu _ { X } , \sigma _ { X } > 0 \mathrm { ~ e ~ } \mu _ { X } \in \mathbb { R }$ . Applicando i risultati delle slide 114 e seguenti alla funzione lineare $g ( x ) = \sigma { x } { x } + \mu { x }$ otteniamo: 

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


## La funzione Q(x)

Sia $X _ { 0 } \sim \mathcal { N } ( 0 , 1 )$ : n`e la sua CDF n`e la sua CCDF sono note in forma esplicita, poich`e $e ^ { - \gamma x ^ { 2 } }$ non ammette primitive elementari. 

Definiamo: 

$$
Q (x) \stackrel {\mathrm{def}} {=} \mathbb {P} (X \geq x) = 1 - F _ {X _ {0}} (x) = \frac {1}{\sqrt {2 \pi}} \int_ {x} ^ {\infty} e ^ {- \frac {t ^ {2}}{2}} d t
$$

per cui: 

$$
F _ {X _ {0}} (x) = 1 - Q (x) \quad P _ {X _ {0}} (x; \Delta x) = Q \left(x - \frac {\Delta x}{2}\right) - Q \left(x + \frac {\Delta x}{2}\right)
$$

Ovviamente, se $X \sim \mathcal { X } ( \mu _ { X } , \sigma _ { X } ^ { 2 } )$ , avremo $X = X _ { 0 } \sigma _ { X } + \mu _ { X }$ , per cui: 

$$
1 - F _ {X} (x) = \frac {1}{\sqrt {2 \pi \sigma_ {X} ^ {2}}} \int_ {x} ^ {\infty} e ^ {- \frac {(t - \mu_ {X}) ^ {2}}{2 \sigma_ {X} ^ {2}}} d t = Q \left(\frac {x - \mu_ {X}}{\sigma_ {X}}\right)
$$

Dato il suo uso frequente, nella prossima slide `e presentato un diagramma della funzione $Q ( x ) , x \geq 0$ 

## Andamento di Q(x)

$$
Q (x) \sim \frac {1}{x \sqrt {2 \pi}} e ^ {- \frac {x ^ {2}}{2}} <   e ^ {- \frac {x ^ {2}}{2}}, \qquad x \to \infty
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9e014a72e6bb4cff5f6045f5e3af68f8479b85e9889bcb10a79b45de356eb16a.jpg)


## Alcune utili propriet`a della funzione Q(x)

Si noti preliminarmente che 

$$
Q (- \infty) = \frac {1}{\sqrt {2 \pi}} \int_ {\mathbb {R}} e ^ {- \frac {t ^ {2}}{2}} d x = 1 \qquad Q (\infty) = 0
$$

Inoltre: 

$$
\frac {d Q (x)}{d x} = - \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {x ^ {2}}{2}} <   0 \forall x \rightarrow Q (x) \text {   è   decrescente   in   } x
$$

Simmetria: 

$$
Q (- x) = \frac {1}{\sqrt {2 \pi}} \int_ {- x} ^ {\infty} e ^ {- \frac {t ^ {2}}{2}} d t = 1 - \underbrace {\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {- x} e ^ {- \frac {t ^ {2}}{2}} d t} _ {= Q (x)} = 1 - Q (x)
$$

Se $X \sim \mathcal N ( \mu _ { X } , \sigma _ { X } ^ { 2 } )$ allora: 

$$
\mathbb {P} (X \geq \eta) = \mathbb {P} (X _ {0} \sigma_ {X} + \mu_ {X} \geq \eta) = \mathbb {P} (X _ {0} \geq \frac {\eta - \mu_ {X}}{\sigma_ {X}}) = Q (\frac {\eta - \mu_ {X}}{\sigma_ {X}})
$$

## Caratterizzazione congiunta di variabili Gaussiane

Siano $X _ { 1 } \sim \mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) \in X _ { 2 } \sim \mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$ . Noi sappiamo che: 

$$
\sigma_ {1} ^ {2} = \mathbb {E} \left[ (X _ {1} - \mu_ {1}) ^ {2} \right] \quad \sigma_ {2} ^ {2} = \mathbb {E} \left[ (X _ {2} - \mu_ {2}) ^ {2} \right] \quad \rho_ {1, 2} = \overbrace {\frac {\mathbb {E} \left[ (X _ {1} - \mu_ {1}) (X _ {2} - \mu_ {2}) \right]}{\sigma_ {1} \sigma_ {2}}} ^ {\mathrm{COV} (X _ {1}, X _ {2})}
$$

rappresenta una caratterizzazione ”globale” (cio`e incompleta) della coppia $( X _ { 1 } , X _ { 2 } )$ Organizziamo tale coppia in un vettore colonna $\pmb { X } = ( X _ { 1 } \pmb { X } _ { 2 } ) ^ { T }$ . Ovviamente, $\pmb { x } \in \mathbb { R } ^ { 2 \times 1 }$ `e un vettore bidimensionale aleatorio, la cui media `e essa stessa un vettore, $\mu _ { X } = ( \mu _ { 1 } \mu _ { 2 } ) ^ { T }$ 

Definiamo Matrice di covarianza del vettore X la matrice $\kappa _ { X } \in \mathbb R ^ { 2 \times 2 }$ 

$$
\boldsymbol {K} _ {\boldsymbol {X}} \stackrel {{\text { def }}} {{=}} \mathbb {E} \left[ (\boldsymbol {X} - \boldsymbol {\mu} _ {\boldsymbol {X}}) (\boldsymbol {X} - \boldsymbol {\mu} _ {\boldsymbol {X}}) ^ {T} \right] = \mathbb {E} \left[ \binom{X _ {1} - \mu_ {1}}{X _ {2} - \mu_ {2}} (X _ {1} - \mu_ {1} X _ {2} - \mu_ {2}) \right] =
$$

$$
= \mathbb {E} \left[ \begin{array}{c c} (X _ {1} - \mu_ {1}) ^ {2} & (X _ {1} - \mu_ {1}) (X _ {2} - \mu_ {2}) \\ (X _ {2} - \mu_ {2}) (X _ {1} - \mu_ {1}) & (X _ {2} - \mu_ {2}) ^ {2} \end{array} \right] = \left( \begin{array}{c c} \sigma_ {1} ^ {2} & \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ \sigma_ {1} \sigma_ {2} \rho_ {1, 2} & \sigma_ {2} ^ {2} \end{array} \right)
$$

## Alcune propriet`a della matrice di covarianza

Poich`e $| \boldsymbol { K } \boldsymbol { x } | = \sigma _ { 1 } ^ { 2 } \sigma _ { 2 } ^ { 2 } \bigl ( 1 - \rho _ { 1 , 2 } ^ { 2 } \bigr ) \geq 0 , \boldsymbol { K } \boldsymbol { x }$ `e definita non negativa; 

Se $\rho _ { 1 , 2 } \neq \pm 1 \kappa _ { x }$ `e invertibile e ha inversa definita positiva: 

$$
\boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} = \frac {1}{\sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})} \left( \begin{array}{c c} \sigma_ {2} ^ {2} & - \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ - \sigma_ {1} \sigma_ {2} \rho_ {1, 2} & \sigma_ {1} ^ {2} \end{array} \right)
$$

$\kappa _ { x }$ `e simmetrica; 

Ovviamente, se $\pmb { z } = [ z _ { 1 } z _ { 2 } ] ^ { T } \in \mathbb { R } ^ { 2 \times 1 }$ 

$$
\boldsymbol {z} ^ {T} \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} \boldsymbol {z} \geq 0 \quad \forall \boldsymbol {z} \in \mathbb {R} ^ {2 \times 1}
$$

Se $X _ { 1 } \texttt { e } X _ { 2 }$ sono incorrelate allora $\rho _ { 1 , 2 } = 0$ , per cui $\kappa _ { x }$ diventa la matrice diagonale: 

$$
\boldsymbol {K} _ {\boldsymbol {X}} = \left( \begin{array}{c c} \sigma_ {1} ^ {2} & 0 \\ 0 & \sigma_ {2} ^ {2} \end{array} \right) \Longrightarrow \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} = \left( \begin{array}{c c} \frac {1}{\sigma_ {1} ^ {2}} & 0 \\ 0 & \frac {1}{\sigma_ {2} ^ {2}} \end{array} \right)
$$

## Variabili congiuntamente Gaussiane

Le due variabili $X _ { 1 } \sim \mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) \in X _ { 2 } \sim \mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$ si dicono congiuntamente Gaussiane se la loro pdf congiunta - cio`e la pdf del vettore $\pmb { X } = ( X _ { 1 } X _ { 2 } ) ^ { T }$ - si scrive: 

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \frac {1}{2 \pi | \boldsymbol {K} _ {\boldsymbol {X}} | ^ {1 / 2}} \exp \left[ - \frac {1}{2} (\boldsymbol {x} - \boldsymbol {\mu} _ {\boldsymbol {X}}) ^ {T} \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} (\boldsymbol {x} - \boldsymbol {\mu} _ {\boldsymbol {X}}) \right] = f _ {X _ {1}, X _ {2}} (x _ {1}, x _ {2}) =
$$

$$
\frac {1}{2 \pi \sqrt {\sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})}} \exp \left[ - \frac {\sigma_ {2} ^ {2} (x _ {1} - \mu_ {1}) ^ {2} + \sigma_ {1} ^ {2} (x _ {2} - \mu_ {2}) ^ {2} - 2 \rho_ {1 , 2} (x _ {1} - \mu_ {1}) (x _ {2} - \mu_ {2})}{2 \sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})} \right]
$$

In questo caso si pu`o usare la notazione abbreviata $\pmb { X } \sim \mathcal { N } ( \pmb { \mu } \pmb { x } , \pmb { K } \pmb { x } )$ 

Nel caso speciale $\rho _ { 1 , 2 } = 0$ , la precedente d`a: 

$$
f _ {\pmb {X}} (\pmb {x}) = f _ {X _ {1}, X _ {2}} (x _ {1}, x _ {2}) = \frac {1}{2 \pi \sqrt {\sigma_ {1} ^ {2} \sigma_ {2} ^ {2}}} e ^ {- \frac {(x _ {1} - \mu_ {1}) ^ {2}}{2 \sigma_ {1} ^ {2}} - \frac {(x _ {2} - \mu_ {2}) ^ {2}}{2 \sigma_ {2} ^ {2}}} = f _ {X _ {1}} (x _ {1}) f _ {X _ {2}} (x _ {2})
$$

cio`e se due variabili sono congiuntamente Gaussiane (e solo in questo caso) l’incorrelazione implica l’indipendenza statistica! 

## Propriet`a di chiusura rispetto a trasformazioni lineari

Se $\pmb { x } \sim \mathcal { N } ( \pmb { \mu } \pmb { x } , \pmb { K } \pmb { x } )$ allora ogni trasformazione lineare di X d`a luogo a un nuovo vettore Gaussiano. 

Focalizziamoci prima su una semplice combinazione lineare di $X _ { 1 } \texttt { e } X _ { 2 }$ . Avremo che: 

$$
\begin{array}{c} Z = a _ {1} X _ {1} + a _ {2} X _ {2} \Rightarrow \mu_ {Z} = a _ {1} \mu_ {1} + a _ {2} \mu_ {2} \quad \sigma_ {Z} ^ {2} = a _ {1} ^ {2} \sigma_ {1} ^ {2} + a _ {2} ^ {2} \sigma_ {2} ^ {2} + 2 a _ {1} a _ {2} \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ \boxed {Z \sim \mathcal {N} (\mu_ {Z}, \sigma_ {Z} ^ {2})} \end{array}
$$

Pi`u in generale, se $\pmb { Z } = \pmb { A } \pmb { X } + \pmb { b }$ , con $\pmb { A } \in \mathbb { R } ^ { 2 \times 2 } \mathrm { ~ e ~ } \pmb { b } \in \mathbb { R } ^ { 2 \times 1 }$ allora: 

$$
\mu_ {Z} = A \mu_ {X} + b
$$

$$
\mathbb {E} \left[ (Z - \mu_ {Z}) (Z - \mu_ {Z}) ^ {T} \right] = A K _ {X} A ^ {T} = K _ {Z}
$$

$$
\mathbf {Z} \sim \mathcal {N} (\boldsymbol {\mu_ {Z}}, \mathbf {K _ {Z}})
$$

## Richiami sulle variabili aleatorie

• Si consideri uno spazio di probabilit`a arbitrario, $\Omega , \tau , \mathbb { P }$ , dove $\Omega \ { \dot { \mathbf { e } } }$ lo spazio dei campioni, T una σ−algebra di eventi di $\Omega \textsf { e l P } \colon { \mathcal { T } }  [ 0 , 1 ]$ una legge di probabilit`a. 

• Ricordiamo che una variabile aleatoria reale X `e una funzione (misurabile) definita come: 

$$
X: \omega \in \Omega \Longrightarrow X (\omega) \in \mathcal {X} \subseteq \mathbb {R}
$$

• La variabile aleatoria `e discreta se tale `e X , continua se tale `e X . 

• Una coppia di variabili aleatorie `e un’applicazione 

$$
X, Y: \omega \in \Omega \Longrightarrow (X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y} \subseteq \mathbb {R} ^ {2}
$$

• La variabile aleatoria X si dice completamente caratterizzata se ne $\grave { \mathbf { e } }$ nota la CDF $F _ { X } ( x ) \circ$ - equivalentemente - la DF $p _ { X } ( x )$ o la pdf $f _ { X } ( x )$ nel caso discreto e continuo, rispettivamente: 

$$
F _ {X} (x) = \mathbb {P} \left\{X \leq x \right\} \forall x \in \mathbb {R} p _ {X} (x) = \mathbb {P} \left\{X = x \right\} \forall x \in \mathcal {X} f _ {X} (x) = \frac {d f _ {X} (x)}{d x}
$$

• Parallelamente, per la coppia $( X , Y )$ si ha: 

$$
F _ {X, Y} (x, y) = \mathbb {P} \left\{X \leq x, Y \leq y \right\} \forall (x, y) \in \mathbb {R} ^ {2} f _ {X, Y} (x, y) = \frac {\partial^ {2} F _ {X , Y} (x , y)}{\partial x \partial y}
$$

$$
p _ {X, Y} (x, y) = \mathbb {P} \{X = x, Y = y \} \forall x \in \mathcal {X} \times \mathcal {Y}
$$

## Vettori aleatori

• Una n-pla aleatoria `e una ovvia generalizzazione del concetto di coppia d variabili aleatorie, cio`e: 

$$
\left(X _ {1}, \dots , X _ {n}\right): \omega \in \Omega \Longrightarrow \boldsymbol {X} (\omega) = \left(X _ {1} (\omega), \dots , X _ {n} (\omega)\right) \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {n} \subseteq \mathbb {R} ^ {n}
$$

• Un vettore aleatorio si ottiene quindi facilmente come 

$$
\boldsymbol {X} (\omega) = \left[ X _ {1} (\omega), \dots , X _ {n} (\omega) \right] ^ {T} \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {n} \subseteq \mathbb {R} ^ {n}
$$

• Se gli alfabeti $\mathcal { X } _ { 1 } , \ldots \mathcal { X } _ { n }$ sono discreti, il vettore `e discreto e si caratterizza mediante la DF congiunta; 

$$
p _ {\mathcal {X}} (\boldsymbol {x}) = p _ {\mathcal {X}} \left(x _ {1}, \dots , x _ {n}\right) = \mathbb {P} \left\{X _ {1} = x _ {1}, \dots , X _ {n} = x _ {n} \right\} \forall \boldsymbol {x} \in \mathcal {X} _ {1} \times \dots \mathcal {X} _ {n}
$$

dove $\pmb { x } = [ x _ { 1 } , \dots , x _ { n } ] ^ { T } \in \mathcal { X } _ { 1 } \times \dots \mathcal { X } _ { n }$ 

• Per alfabeti continui, avremo 

$$
F _ {\boldsymbol {X}} (\boldsymbol {x}) = \mathbb {P} \left\{X _ {1} \leq x _ {1}, \dots , X _ {n} \leq x _ {n} \right\} \forall \boldsymbol {x} \in \mathbb {R} ^ {n} \quad f _ {\boldsymbol {X}} (\boldsymbol {x}) = \frac {\partial^ {n} F _ {\boldsymbol {X}} (\boldsymbol {x})}{\partial x _ {1} \dots \partial x _ {n}}
$$

dove $\pmb { x } = [ x _ { 1 } , \dots , x _ { n } ] ^ { T } \in \mathbb { R } ^ { n }$ 

## Legge di Bayes per vettori aleatori

• Consideriamo un vettore aleatorio discreto con pmf $p _ { X } ( { \pmb x } )$ . Sappiamo che la Legge di Bayes assicura che 

$$
\mathbb {P} (A \cap B) = \mathbb {P} (A | B) \mathbb {P} (B)
$$

• Posto $A = \{ X _ { n } = x _ { n } , \ldots , X _ { 2 } = x _ { 2 } \} \textsf { e } B = \{ X _ { 1 } = x _ { 1 } \}$ avremo 

$$
p _ {\boldsymbol {X}} (\boldsymbol {x}) = \mathbb {P} \left\{X _ {n} = x _ {n}, \dots , X _ {2} = x _ {2} | X _ {1} = x _ {1} \right\} \mathbb {P} \left\{X _ {1} = x _ {1} \right\}
$$

• Iterando il ragionamento avremo la regola della catena: 

$$
\begin{array}{c} p _ {X} (x) = \mathbb {P} \{X _ {1} = x _ {1} \} \mathbb {P} \left\{X _ {2} = x _ {2} | X _ {1} = x _ {1} \right\} \dots \mathbb {P} \left\{X _ {n} = x _ {n} | X _ {n - 1} = x _ {n - 1}, \ldots , X _ {1} = x _ {1} \right\} \\ = \prod_ {i = 1} ^ {n} p _ {X _ {i} | X _ {i - 1}, \ldots , X _ {1}} (x _ {i} | x _ {i - 1}, \ldots , x _ {1}), \qquad p _ {X _ {1} | X _ {0}} (x _ {1} | x _ {0}) = p _ {X _ {1}} (x _ {1}) \end{array}
$$

• Analogamente, per vettori continui avremo 

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \prod_ {i = 1} ^ {n} f _ {X _ {i} | X _ {i - 1}, \dots , X _ {1}} (x _ {i} | x _ {i - 1}, \dots , x _ {1})
$$

## Processi aleatori tempo-discreti

Si definisce processo aleatorio tempo-discreto un’applicazione che ad ogn elemento dello spazio campione fa corrispondere una successione: 

$$
X: \omega \in \Omega \longrightarrow \{X (n, \omega) \} _ {n \in \mathbb {Z}}
$$

dove <sup>Z</sup> indica l’insieme degli interi. 

• Di seguito sono riportate tre realizzazioni di un processo tempo-discreto. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/7e76ee276ef5ef4aa0a28d11f4fc129e3b4bfc5e7363b6e3ebb01def91168f7a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/eef731154ce7b72b160d3d277cbe6b34a0a3867f94f145234edd9dd15d98f5db.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/057411ab0f31edbb00e115bfa3816d1d5e5f1c3faed5ab464cbf318ca0bb423a.jpg)


## Commenti e osservazioni

• Per ogni valore di $\omega \in \Omega$ il processo si realizza in una sequenza che assume valori nell’intervallo [−1, 1]; 

Fissando l’istante di tempo $n = n _ { 0 }$ e facendo variare $\omega \in \Omega$ otteniamo $X ( n _ { 0 } , \omega )$ che `e una variabile aleatoria (visto che ”campionando verticalmente” il processo otteniamo che al variare di $\omega X ( n _ { 0 } , \omega )$ assume diverse determinazioni); 

• La variabile aleatoria $X ( n _ { 0 } , \omega )$ ha una sua pdf, che in genere dipende da $\omega ;$ 

• Se la pdf non dipende dall’istante di campionamento $\boldsymbol { n _ { 0 } }$ , il processo si dice stazionario al primo ordine. 

• Nel caso mostrato in figura, il processo `e stato generato assumendolo stazionario e marginalmente uniforme in $[ - 0 . 5 , 0 . 5 ]$ , cio`e 

$$
f _ {X (n)} (x; n) = f _ {X (n)} (x) = \Pi (x - 0. 5)
$$

• Si noti che siccome 

$$
\mathbb {E} [ X (n) ] = \int_ {- \infty} ^ {\infty} x f _ {X (n)} (x; n) d x = \int_ {- 0, 5} ^ {0, 5} x \Pi (x - 0. 5) d x = 0
$$

il processo `e a media identicamente nulla. 

## Un altro esempio: processo Gaussiano tempo-discreto

• Come secondo esempio, consideriamo un processo tempo-discreto stazionario al primo ordine con pdf 

$$
f _ {X (n)} (x) = \frac {1}{\sqrt {2 \pi}} \exp \left[ - \frac {(x + 0 . 5) ^ {2}}{2} \right]
$$

quindi con densit`a marginale Gaussiana a media −0.5 e varianza unitaria. Otteniamo realizzazioni del tipo rappresentate in figura 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/48a5eafdb76a91cfaeec049306e38b42c43e3516620a31cd0a3e5059967ed7ab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/51684a9d1e2c1908853f9b305d6cbfc31882599c788d4ca54497b82c5cfb42be.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/2c12f75b390651df009e373f8c5f9758ea1925d2f1a52f06939bfdc2260a96eb.jpg)


## Caratterizzazione del secondo ordine del processo

• Un processo aleatorio si dice caratterizzato al primo ordine se ne `e nota la pdf $f _ { X ( n ) } ( x ; n )$ per ogni n. Se il processo `e stazionario al primo ordine, questo equivale ad assegnare un’unica pdf. 

• Un processo aleatorio si dice caratterizzato al secondo ordine se ne `e assegnata la pdf congiunta 

$$
f _ {X (n _ {1}), X (n _ {2})} \big (x _ {1}, x _ {2}; n _ {1}, n _ {2} \big), \quad \forall n _ {1}, n _ {2}
$$

• Un processo aleatorio si dice stazionario al secondo ordine se, per qualsias intero h, abbiamo: 

$$
f _ {X (n _ {1}), X (n _ {2})} (x _ {1}, x _ {2}; n _ {1}, n _ {2}) = f _ {X (n _ {1} + h), X (n _ {2} + h)} (x _ {1}, x _ {2}; n _ {1}, n _ {2} + h)
$$

• In altre parole, un processo stazionario al secondo ordine `e tale che la caratterizzazione congiunta di due suoi campioni dipende unicamente dalla loro ”distanza” temporale, ma non dalla loro posizione: in altre parole, la pdf congiunta `e invariante ad atti di moto rigido dei due punti in anticipo o in ritardo. 

• Ovviamente un processo stazionario al secondo ordine lo `e anche al primo, ma non `e vero il viceversa Perch`e?. 

## Caratterizzazione completa di un processo

• Un processo aleatorio $X ( n )$ si dice completamente caratterizzato se, detto M un intero arbitrario e detti $n _ { 1 } , \ldots , n _ { M }$ M istanti arbitrari, il vettore aleatorio 

$$
\boldsymbol {X} = [ X (n _ {1}), \dots , X (n _ {M}) ] ^ {T}
$$

ha densit`a di probabilit`a $f _ { \pmb { X } } ( x _ { 1 } , \ldots , x _ { M } )$ nota. 

Un processo aleatorio si dice stazionario in senso stretto di ordine M se la sua densit`a di probabilit`a di ordine M `e invariante per traslazione, cio`e: 

$$
\begin{array}{c} f _ {X (n _ {1}), \ldots , X (n _ {M})} (x _ {1}, \ldots , x _ {M}; n _ {1}, \ldots , n _ {M}) = \\ f _ {X (n _ {1} + h), \ldots , X (n _ {M} + h)} (x _ {1}, \ldots , x _ {M}; n _ {1} + h, \ldots , n _ {M} + h) \end{array}
$$

• Un processo stazionario di ordine M lo `e di qualunque ordine $i \leq M$ 

• Un processo si dice indipendente (o a campioni indipendenti) se, comunque si scelga un intero M, il vettore $\pmb { X } = [ X ( n _ { 1 } ) , \dots , X ( n _ { M } ) ] ^ { T }$ è costituito da variabil aleatorie indipendenti, cio`e: 

$$
f _ {X (n _ {1}), \dots , X (n _ {M})} (x _ {1}, \dots , x _ {M}) = f _ {X (n _ {1})} (x _ {1}) f _ {X (n _ {2})} (x _ {2}) \dots f _ {X (n _ {M})} (x _ {M}) = \prod_ {i = 1} ^ {M} f _ {X (n _ {i})} (x _ {i})
$$

## Processi discreti

• Si definisce processo ampiezza discreto o - per brevit`a - processo discreto un processo aleatorio in cui le cui realizzazioni siano sequenze di numeri che possano assumere valore in un alfabeto discreto. 

• Un caso di importanza notevole `e quello di un processo indipendente binario, $X ( n ) \in \{ - 1 , 1 \}$ , con $\mathbb { P } \left\{ X ( n ) = 1 \right\} = \mathbb { P } \left\{ X ( n ) = 1 \right\} = { \frac { 1 } { 2 } }$ , di cui le realizzazion sono riportate in figura, anche detto Processo di Bernoulli. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/62faba250dc710ba5cb9fbd4a331bfdc4d2dc4cd5d3bd696b38454e5f14bc19a.jpg)


## Un altro esempio: Un processo quaternario

• Un ulteriore esempio si ha considerando un alfabeto quaternario, per esempio $X ( n ) \in \{ - 2 , - 1 , 1 , 2 \}$ , con livelli equiprobabili (per cu ${ \mathbb { P } } \left\{ X ( n ) = i \right\} = { \textstyle { \frac { 1 } { 4 } } } \ \forall i )$ 

• Le realizzazioni del processo saranno quindi del tipo rappresentato in figura 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9f7957aa1d5176320b74eb7c6ea5945937ed809d0cfc9354252211d9f644fc02.jpg)


## Caratterizzazione di processi discreti

Tutte le definizioni introdotte per i processi continui si estendono ai process discreti, con la sola diferenza che le densit`a di probabilit`a sono ora sostituite dalle DF; 

• Per esempio, un processo discreto si dice stazionario in senso stretto se, comunque si scelga un intero M, il vettore aleatorio $\pmb { X } = [ X ( n _ { 1 } ) , \dots , X ( n _ { M } )$ gode, per un h arbitrario, della propriet`a: 

$$
\begin{array}{c} \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2}, \ldots X (n _ {M}) = x _ {M} \right\} \qquad = \\ \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2}, \ldots X (n _ {M} + h) = x _ {M} \right\} \end{array}
$$

• Ovviamente, la stazionariet`a di ordine M implica quella di ogni ordine $\leq M$ . In particolare, un processo stazionario ha una DF marginale indipendente dal tempo. 

• Un processo discreto che sia stazionario e indipendente ovviamente gode della propriet`a: 

$$
\mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2}, \dots X (n _ {M}) = x _ {M} \right\} = \prod_ {i = 1} ^ {M} \mathbb {P} \left\{X (n _ {i}) = x _ {i} \right\} = \prod_ {i = 1} ^ {M} p _ {X} (x _ {i})
$$

dove $p _ { X } ( \cdot )$ `e la DF marginale (ovviamente indipendente dal tempo) 

## Caratterizzazione sintetica dei vettori aleatori

Come per le variabili aleatorie, anche per i processi aleatori `e possibile - a fronte di un’impossibilit`a di fornirne una caratterizzazione completa - definire una caratterizzazione sintetica, cio`e assegnarne statistiche che siano significative. 

• In modo del tutto analogo al caso scalare, dove abbiamo visto che la coppia media-varianza $( \mu x , \sigma _ { X } ^ { 2 } )$ ofre spesso importanti informazioni sul comportamento della variabile X , e al caso delle coppie, in cui la cinquina $( m u _ { X } , \sigma _ { X } , \mu _ { Y } , \sigma _ { Y } , \mathrm { C O V } ( X , Y )$ ofre analoghe informazioni sulla coppia (X , Y ), per u vettore alatorio $\pmb { X } = [ X _ { 1 } , \ldots , X _ { n } ] ^ { T }$ abbiamo 

## † la media statistica

$$
\boldsymbol {\mu} _ {\boldsymbol {X}} = \left(\mathbb {E} \left[ X _ {1} \right], \dots , \mathbb {E} \left[ X _ {n} \right]\right) ^ {T}
$$

† la matrice di covarianza, $C _ { X } = \mathbb { E } \left[ \left( X - \mu _ { X } \right) \left( X - \mu _ { X } \right) ^ { T } \right]$ 

$$
\left( \begin{array}{c c c c} \sigma_ {X _ {1}} ^ {2} & \operatorname{COV} (X _ {1}, X _ {2}) & \dots & \operatorname{COV} (X _ {1}, X _ {n}) \\ \operatorname{COV} (X _ {2}, X _ {1}) & \sigma_ {X _ {1}} ^ {2} & \dots & \operatorname{COV} (X _ {2}, X _ {n}) \\ \dots & \dots & \dots & \dots \\ \operatorname{COV} (X _ {n}, X _ {1}) & \operatorname{COV} (X _ {n}, X _ {2}) & \dots & \sigma_ {X _ {n}} ^ {2} \end{array} \right)
$$

## Processi Stazionari in Senso Lato (SSL)

• Focalizziamoci sui processi tempo discreti, ma quanto verr`a detto vale anche per i processi tempo-continui. 

• Abbiamo visto che un processo $X ( n ) \in { \mathcal { X } }$ `e stazionario di ordine 2 se: 

$$
\mathbb {P} \left\{X (n) = x \right\} = p _ {X} (x) \quad \forall x \text {e} \quad \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2} \right\} = \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2} \right\}
$$

• Ovviamente la media $\begin{array} { r } { \mu _ { X } = \operatorname { \mathbb { E } } \left[ X ( n ) \right] = \sum _ { x \in \mathcal { X } } x p _ { X } ( x ) } \end{array}$ non dipende da $n ;$ 

• Inoltre si noti che 

$$
\mathbb {E} \left[ X (n _ {1}) X (n _ {2}) \right] = \sum_ {x _ {1} \in \mathcal {X}} \sum_ {x _ {2} \in \mathcal {X}} x _ {1} x _ {2} \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2} \right\} =
$$

$$
\mathbb {E} \left[ X (n _ {1} + h) X (n _ {2} + h) \right] = \sum_ {x _ {1} \in \mathcal {X}} \sum_ {x _ {2} \in \mathcal {X}} x _ {1} x _ {2} \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2} \right\}
$$

che significa che $\mathbb { E } \left[ X ( n _ { 1 } ) X ( n _ { 2 } ) \right]$ `e funzione di $n _ { 2 } - n _ { 1 }$ , ma non separatamente di $\boldsymbol { n } _ { 1 } \in \boldsymbol { n } _ { 2 }$ 

• Un processo $X ( n / t )$ , continuo o disceto, non necessariamente stazionario al secondo ordine, si dice stazionario in senso lato se 

† La sua media non dipende dal tempo; 

† la sua autocorrelazione soddisfa la condizione 

$$
R _ {X} \left(t _ {1} / n _ {1}, t _ {2} / n _ {2}\right) = \mathbb {E} \left[ X \left(t _ {1} / n _ {1}\right) X \left(t _ {2} / n _ {2}\right) \right] = R _ {X} \left(t _ {2} - t _ {1} / n _ {2} - n _ {1}\right)
$$

## Matrice di covarianza per processi SSL

• Sia $X ( t / n )$ un processo SSL, continuo o discreto, e sia $\pmb { x } = [ X _ { 1 } , \ldots , X _ { M } ] ^ { T }$ un vettore aleatorio M dimensionale di campioni di $X ( t / n )$ , presi negli istanti $( t _ { 1 } , \hdots , t _ { M } ) / ( n _ { 1 } , \hdots , n _ { M } )$ 

• Ovviamente avremo che $\pmb { \mu } = \mathbb { E } \left[ \pmb { X } \right] = \mu \mathbf { 1 }$ , con $\mu$ scalare e 1 un vettore M−dimensionale di tutt $" \bf { 1 } ^ { \prime \prime }$ 

• Inoltre, avremo, per la condizione SSL: 

$$
\mathbb {E} \left[ X _ {i} X _ {j} \right] = f (| i - j |) \quad \mathbb {E} \left[ X _ {i} ^ {2} \right] = \overline {{X ^ {2}}}, \operatorname{Var} (X _ {i}) = \overline {{X ^ {2}}} - \mu^ {2} = \sigma_ {X} ^ {2}
$$

per cui, definendo $\begin{array} { r } { \rho _ { i , j } = \frac { \mathrm { C O V } ( X _ { i } , X _ { j } ) } { \sigma _ { X } ^ { 2 } } } \end{array}$ la matrice di covarianza assume la forma 

$$
\boldsymbol {C} _ {\boldsymbol {X}} = \sigma_ {\chi} ^ {2} \left( \begin{array}{c c c c c} 1 & \rho_ {1, 2} & \rho_ {1, 3} & \dots & \rho_ {1, M} \\ \rho_ {1, 2} & 1 & \rho_ {2, 3} & \dots & \rho_ {2, M} \\ \dots & \dots & \dots & \dots & \dots \\ \rho_ {1, M} & \rho_ {2, M} & \rho_ {3, M} & \dots & 1 \end{array} \right)
$$

• Pertanto la matrice di covarianza di un vettore tratto da un processo SSL `e simmetrica. 

• Si noti che se il passo di campionamento del processo `e costante (cio`e, $( t _ { i + 1 } - t _ { i } ) / ( n _ { i + 1 } - n _ { i } )$ costante $\forall i ,$ , allora la matrice assume una forma di Toeplitz. 

## Esercizio: La matrice di covarianza `e sempre definita non-negativa

• Ricordiamo che una matrice $\pmb { C } \in \mathbb { R } ^ { M \times M }$ `e definita non negativa se, detto $\pmb q \in \mathbb { R } ^ { M }$ un qualunque vettore M−dimensionale risulta $\pmb q ^ { T } \pmb { C q } \geq 0$ 

• Consideriamo un vettore aleatorio M−dimensionale X di media $\mu \in$ matrice d covarianza $c _ { x }$ . La quantit`a $\pmb { q } ^ { T } \pmb { X }$ `e ovviamente una variabile aleatoria scalare con $\mathbb { E } \left[ { \pmb q } ^ { T } { \pmb X } \right] = { \pmb q } ^ { T } \pmb { \mu }$ . Inoltre 

$$
\mathbb {E} \left[ \left(\boldsymbol {q} ^ {T} \boldsymbol {X}\right) ^ {2} \right] = \mathbb {E} \left[ \boldsymbol {q} ^ {T} \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {q} \right] = \boldsymbol {q} ^ {T} \mathbb {E} \left[ \boldsymbol {X} \boldsymbol {X} ^ {T} \right] \boldsymbol {q}
$$

• Avremo allora la catena di disuguaglianze: 

$$
0 \leq \operatorname{Var} \left(\boldsymbol {q} ^ {T} \boldsymbol {X}\right) = \boldsymbol {q} ^ {T} \mathbb {E} \left[ \boldsymbol {X} \boldsymbol {X} ^ {T} \right] \boldsymbol {q} - \left(\boldsymbol {q} ^ {T} \boldsymbol {\mu}\right) ^ {2} =
$$

$$
\boldsymbol {q} ^ {T} \mathbb {E} \left[ \boldsymbol {X} \boldsymbol {X} ^ {T} \right] \boldsymbol {q} - \boldsymbol {q} ^ {T} \mu \mu^ {T} \boldsymbol {q} = \boldsymbol {q} ^ {T} \underbrace {\left(\mathbb {E} \left[ \boldsymbol {X} \boldsymbol {X} ^ {T} \right] - \mu \mu^ {T}\right)} _ {c _ {\chi}} \boldsymbol {q}
$$

dove si `e sfruttato il fatto che 

$$
\boldsymbol {C} _ {\boldsymbol {X}} = \mathbb {E} \left[ (\boldsymbol {X} - \boldsymbol {\mu}) (\boldsymbol {X} - \boldsymbol {\mu}) ^ {T} \right] = \mathbb {E} \left[ \boldsymbol {X} \boldsymbol {X} ^ {T} \right] - \boldsymbol {\mu} \boldsymbol {\mu} ^ {T}
$$

## Estensione ai processi continui: definizioni

• Quanto detto sui processi ampiezza-discreti si estende ai processi ampiezza continui; 

• Detto $\pmb { X } = [ X ( t _ { 1 } / n _ { 1 } ) , \dots X ( t _ { M } / n _ { M } )$ tratto da un processo $X / t / n )$ , la sua caratterizzazione implica l’assegnazione di una delle due funzioni: 

$$
F _ {\boldsymbol {X}} \left(x _ {1}, \dots , x _ {M}\right) = F _ {\boldsymbol {X}} (\boldsymbol {x}) = \mathbb {P} \left\{X _ {1} \leq x _ {1}, \dots , X _ {M} \leq x _ {M} \right\}
$$

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \lim _ {V (\Delta \boldsymbol {x}) \rightarrow 0} \frac {\mathbb {P} _ {\boldsymbol {X}} (\boldsymbol {x} , \Delta \boldsymbol {x})}{V (\Delta \boldsymbol {x})} = \frac {\partial^ {M} F _ {\boldsymbol {X}} (\boldsymbol {x})}{\partial x _ {1} \partial x _ {2} \dots \partial x _ {M}}
$$

dove $\Delta \boldsymbol { x } = ( \Delta x _ { 1 } , \ldots , \Delta x _ { M } ) , V ( \Delta x ) = \Delta x _ { 1 } \cdot \cdot \cdot \Delta x _ { M } \in$ 

$$
\mathbb {P} _ {\boldsymbol {X}} (\boldsymbol {x}, \Delta \boldsymbol {x}) = \mathbb {P} \left\{x _ {1} - \frac {\Delta x _ {1}}{2} \leq X _ {1} \leq x _ {1} + \frac {\Delta x _ {1}}{2}, \dots , x _ {M} - \frac {\Delta x _ {M}}{2} \leq X _ {M} \leq x _ {M} + \frac {\Delta x _ {M}}{2} \right\}
$$

• Ovviamente le definizioni di stazionariet`a in senso lato e in senso stretto si estendono tal quali ai processi ampiezza continui. 

## Un esempio: Processi Gaussiani

• Un processo $X ( t / n )$ si dice Gaussiano se un qualungue suo campione d dimensione M definisce un vettore aleatorio X Gaussiano. 

• Dato un vettore aleatorio X con media e matrice di covarianza assegnati: 

$$
\boldsymbol {\mu} _ {\boldsymbol {X}} = \mathbb {E} [ \boldsymbol {X} ] \quad \boldsymbol {C} _ {\boldsymbol {X}} = \mathbb {E} \left[ (\boldsymbol {X} - \boldsymbol {\mu}) (\boldsymbol {X} - \boldsymbol {\mu}) ^ {T} \right]
$$

questo si dice Gaussiano se la sua pdf si scrive nella forma 

$$
\frac {1}{(2 \pi) ^ {M / 2} | \boldsymbol {C} _ {\boldsymbol {X}} | ^ {1 / 2}} \exp \left[ - \frac {1}{2} (\boldsymbol {x} - \boldsymbol {\mu}) ^ {T} \boldsymbol {C} _ {\boldsymbol {X}} ^ {- 1} (\boldsymbol {x} - \boldsymbol {\mu}) \right], \quad \boldsymbol {x} \in \mathbb {R} ^ {M}
$$

dove $| c \pmb { x } |$ denota il determinante della matrice di covarianza. 

## Propriet`a dei processi Gaussiani

• La stazionariet`a in senso lato implica quella in senso stretto. Si verifichi questo asserto ricordando che nel caso di stazionariet`a in senso lato la matrice di covarianza ha struttura Toeplitz; 

• Chiusura rispetto a trasformazioni lineari. Se X `e un vettore Gaussiano, $\pmb { x } \sim \mathcal { N } ( \pmb { \mu } , \pmb { C } )$ , allora, avremo 

$$
\boldsymbol {Y} = \boldsymbol {A} \boldsymbol {X} + \boldsymbol {u} \sim \mathcal {N} (\boldsymbol {A} \boldsymbol {\mu} + \boldsymbol {u}, \boldsymbol {A} \boldsymbol {C} \boldsymbol {A} ^ {T})
$$

• Per un processo Gaussiano, incorrelazione implica indipendenza. Infatti, un processo incorrelato ha marice di covarianza $\pmb { C } = \mathrm { d i a g } ( \sigma _ { 1 } ^ { 2 } , \dots , \sigma _ { M } ^ { 2 } )$ . Sostituendc nella espressione di una pdf Gaussiana abbiamo 

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \left(\prod_ {i = 1} ^ {M} \frac {1}{\sigma_ {i} \sqrt {2 \pi}}\right) \exp \left[ - \sum_ {i = 1} ^ {M} \frac {(x _ {i} - \mu_ {i}) ^ {2}}{2 \sigma_ {i} ^ {2}} \right] = \prod_ {i = 1} ^ {M} f _ {X _ {i}} (x _ {i})
$$

## Tipi di convergenza

• Sia $\{ X _ { n } \}$ una successione di variabili aleatorie con densit`a $\{ f _ { X _ { n } } \} \in \mathsf { C D F } \left\{ F _ { X _ { n } } \right\}$ 

• Ci chiediamo come definire la convergenza di tale successione a un dato limite, sia esso X . 

• Ovviamente la forma pi`u forte di convergenza `e quella puntuale, vale a dire - ricordando che le variabili aleatorie sono in realt`a funzioni - $\operatorname* { l i m } _ { n } X _ { n } ( \omega ) = X ( \omega )$ $\forall \omega \in \Omega$ , dove $\Omega \ { \dot { \mathsf { e } } }$ lo spazio dei campioni dello spazio di probabilit`a sottostante. 

• Altre forme di convergenza pi`u ”deboli” (con diversa gradiazione) sono: 

† La convergenza in distribuzione; 

† La convergenza in probabilit`a; 

† La convergenza in media quadratica; 

† La convergenza quasi certa (o con probabilit`a 1); 

## Convergenza in distribuzione

• La successione $\{ X _ { n } \}$ si dice convergente in distribuzione alla variabile X (e si scrive $x _ { n } { \overset { d } { \to } } X$ se 

$$
\lim _ {n \rightarrow \infty} F _ {X _ {n}} (x) = F _ {X} (x), \text { per   vettori: } \lim _ {n \rightarrow \infty} \mathbb {P} \left\{\boldsymbol {X} _ {n} \in A \right\} = \mathbb {P} \left\{\boldsymbol {X} \in A \right\}, A \subseteq \mathbb {R} ^ {M}
$$

dove l’uguaglianza vale in tutti gli insiemi di continuit`a di $F _ { X }$ 

• Il teorema cosiddetto del ”continuous mapping” stabilisce che, se $\boldsymbol { \mathsf { \Pi } } _ { \boldsymbol { \mathsf { \Pi } } } ^ { g \ \star }$ una finzione continua, allora si ha: 

$$
X _ {n} \xrightarrow {d} X \Longrightarrow g (X _ {n}) \xrightarrow {d} g (X)
$$

• Il teorema di continuit`a di Levy stabilisce che, definendo la funzione generatrice dei momenti (moment generating function, mgf) 

$$
\Phi_ {n} (s) = \mathbb {E} \left[ e ^ {s f X _ {n}} \right] \quad \Phi_ {X} (s) = \mathbb {E} \left[ e ^ {s X} \right]
$$

per i valori di s per cui l’integrale esiste, la convergenza puntuale di $\Phi _ { n } ( s )$ a Φ(s) implica $\boldsymbol { X _ { n } } \overset { d } { \to } \boldsymbol { X } \mathrm { ~ e ~ }$ viceversa. 

## La funzione generatrice dei momenti

• La funzione generatrice dei momenti (moment generating function, mgf) di una variabile aleatoria gode di alcune rilevanti propriet`a. Notiamo che 

$$
\Phi_ {X} (s) = \int_ {\mathbb {R}} e ^ {s t} f _ {X} (t) d t, \text {   con   } f _ {X} \text {   sommabile }
$$

`e funzione continua di s nei punti in cui l’integrale esiste. 

• Analogamente si pu`o facilmente verificare che: 

$$
\Phi_ {X} (0) = 1 \quad \Phi^ {\prime} (0) = \mathbb {E} [ X ] \quad \Phi_ {X} ^ {\prime \prime} (0) = \mathbb {E} [ X ^ {2} ] \dots \Phi_ {X} ^ {(r)} (0) = \mathbb {E} [ X ^ {r} ]
$$

purch`e i momenti di ordine r esistano. 

• Pertanto, nelle condizioni precedenti, la mgf ammette il seguente sviluppo in serie di Mc Laurir 

$$
\Phi_ {X} (s) = \sum_ {n = 0} ^ {\infty} \frac {\mathbb {E} [ X ^ {n} ]}{n !} s ^ {n}
$$

il che spiega il nome ”mgf”. 