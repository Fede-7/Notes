## Pagina 1

Informazioni generali

• Docente: Marco Lops (IINF-03/A, "Telecomunicazioni"). Perchè?
• Orario delle lezioni

| Giorno | Ora | Aula |
| :--- | :--- | :--- |
| Martedi | 14,00 - 16,00 | B-6 |
| Giovedi | 8,45 - 10,45 | B-6 |

• Spiegazioni: Ci saranno degli orari ufficiali, ma le interazioni potranno anche avvenire:
  † Al termine delle lezioni;
  † Su appuntamneto mediante Teams;
  † Su appuntamento dal vivo

• Pertanto è importante iscriversi al Team "Calcolo delle Probabilità e Statistica", il cui codice è 8b1fgjq.

• È anche opportuno iscriversi al corso sul sito web docenti.

---

## Pagina 2

Organizzazione del corso

• Il corso prevede 6 CFU (cioè, 48 ore di lezione), tutte erogate frontalmente, eccezione fatta per lezioni di recupero, che saranno erogate a distanza.

• Le lezioni saranno per circa due terzi (cioè, 32 ore) di tipo teorico, mentre il restante terzo (cioè, 16 ore) di tipo applicativo.

• La verifica finale consisterà in una prova scritta, seguita da un colloquio orale.

---

## Pagina 3

Materiale didattico

• Slides preparate dal docente, scaricabili dal Team "Metodi statistici per l'informazione" (codice team: 7p3013g);
• Formati pdf delle lavagne - quando disponibili -, scaricabili dal Team "Calcolo delle probabilità e statistica";
• Libri di testo consigliati:
  † Sulla Teoria della Probabilità:

  † Sulla Statistica Inferenziale e descrittiva:
  Sheldon M. Ross,"Introduction to Probability and Statistics for Engineers and Scientists", *Elsevier*.

---

## Pagina 4

Esperimenti e Eventi
Leggi di Probabilità su Spazi Campione discreti
Spazi Campione Continui
Processi Aleatori
Processi aleatori

Il corso di Calcolo delle Probabilità e Statisica

Teoria della Probabilità
Analisi Combinatoria
Prob. su spazi finiti
Variabili aleatori discrete
Variabili continue
Variabili multiple
Processi Aleatori

Informazione e sua misura
Entropia
Compressione Dati
Mutua Informazione
Divergenza

Statistica
Statistica inferenziale
Teoria della decisione
Inferenza Bayesiana e non
Stima ricorsiva

Integrazione tra
Teoria dell’Informazione e
Statistica Inferenziale

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statistici per l’Informazione - Marco Lops  4 / 161

---

## Pagina 5

Elementi di Teoria della Probabilità

Marco Lops

lops@unina.it
https://docenti.unina.it/marco.lops

---

## Pagina 6

Esperimenti e Eventi
Leggi di Probabilità su Spazi Campione discreti
Spazi Campione Continui
Processi Aleatori
Processi aleatori

Tecniche di conteggio

Definizioni

- Esperimento: Operazione/azione - o insieme di operazioni/azioni - il cui esito dà uno tra tanti risultati possibili;
- Spazio dei campioni - o spazio campione - comunemente denotato con Ω: insieme - non necessariamente numerico - di tutti i risultati possibili di un esperimento;
- Ω può essere continuo o discreto: per il momento assumeremo che sia discreto, cioè finito o numerabile.
- Evento: un qualunque sotto-insieme di Ω definito matematicamente da un insieme di suoi elementi e lessicalmente da una proposizione;
- Evento elementare: uno dei possibili |Ω| elementi di Ω. Si indica anche con ω ∈ Ω.
- Un evento è univocamente individuato dagli elementi che lo compongono;
- Al contrario, la proposizione che lo definisce non è unica.

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l’Informazione - Marco Lops 6 / 161

---

## Pagina 7

Esempio #1 : lancio di una moneta

- Lancio singolo:
  - Spazio campione: $\Omega = \{Testa, Croce\} = \{T, C\}$, $|\Omega| = 2$;
  - Esempi di eventi:
    $$A = Testa = \{T\} \quad B = Croce = \{C\} \quad Testa o Croce = A \cup B$$

- Lancio doppio
  - Spazio campione:
    $$\Omega = \{TT, TC, CT, CC\} = \{T, C\} \times \{T, C\} = \{T, C\}^2$$
  - Esempi di eventi:
    $$A = \{# croci dispari\} = \{TC, CT\}$$
    $$B = \{Nessuna croce\} = \{TT\}$$

---

## Pagina 8

Esempio # 2: lancio di un dado

- Spazio campione: $\Omega = \{1, 2, 3, 4, 5, 6\}$, $|\Omega| = 6$;
- Esempi di eventi:
  - $A = \text{II risultato è dispari} = \{1, 3, 5\}$
  - $B = \text{II risultato è pari} = \{2, 4, 6\}$
  - $C = \text{II risultato è dispari} \leq 4 = \{1, 3\}$
  - $D = \text{II risultato è 6} = \{6\}$
- Ognuno dei precedenti eventi può essere associato a molte altre proposizioni che lo definiscono;
- Nota Bene: in entrambe le situazioni la proposizione che definisce un evento non è univoca.

---

## Pagina 9

Esempio #3: Numero di pacchetti dati in coda ad un router

- Spazio dei campioni: $\Omega = \{0, 1, 2, 3, \ldots\} = \mathbb{N}_0$, $|\Omega| = \infty$.
- Esempi di eventi:
  - $A = \{Ci sono meno di 6 pacchetti\} = \{0, 1, 2, 3, 4, 5\}$
  - $B = \{# pacchetti dispari\} = \{1, 3, 5, \ldots, (2k + 1), \ldots\}$
  - $C = \{# pacchetti dispari e minore di 6\} = \{1, 3, 5\} = A \cap B$
  - $D = \{# pacchetti pari o minore di 4\} = \{1, 2, 3, 6, 8, 10, 12, \ldots, 2k, \ldots\}$
- Dai precedenti esempi si vede che si possono definire nuovi eventi eseguendo delle operazioni tra altri eventi: le regole sono quelle classiche dell’insiemistica.

---

## Pagina 10

Qualche richiamo di insiemistica -1

Siano $\{A_i\}_{i=1}^M$ $M$ sotto-insiemi di un insieme $\Omega$. Definiamo:

- Unione tra due sotto-insiemi, $A_1 \cup A_2$, un sotto-insieme di $\Omega$ che contenga tutti gli elementi di $A_1$ e quelli di $A_2$, ovviamente contando una sola volta quelli comuni;
- Complemento in $\Omega$ di un sotto-insieme $A_1$ l’insieme $\overline{A_1}$ che contiene tutti gli elementi di $\Omega$ che non appartengono a $A_1$; ovviamente $\overline{\Omega} = \emptyset$, $\overline{A_1} = A_1$ e $A_1 \cup \overline{A_1} = \Omega$.
- Intersezione tra due sotto-insiemi, $A_1 \cap A_2$, l’insieme che contiene tutti e soli gli elementi comuni a $A_1$ e $A_2$.
- Sottrazione tra due insiemi, $A_1 \setminus A_2$, l’insieme che contiene gli elementi di $A_1$ che non appartengono a $A_2$. Ovviamente avremo:

$$A_1 \setminus A_2 = A_1 \cap \overline{A_2}$$

---

## Pagina 11

Qualche richiamo di insiemistica -2

• Relazione di De Morgan tra unione, intersezione e complementazione:

$$\overline{A_1 \cup A_2} = \overline{A_1} \cap \overline{A_2} \implies \overline{A_1 \cup A_3} = A_1 \cap A_2$$

• Proprietà associativa di unione e intersezione:

$$(A_1 \cup A_2) \cup A_3 = A_1 \cup (A_2 \cup A_3) \quad (A_1 \cap A_2) \cap A_3 = A_1 \cap (A_2 \cap A_3)$$

• Proprietà distributiva dell'unione rispetto all'intersezione e dell'intersezione rispetto all'unione:

$$A_1 \cup \left( \cap_{i=2}^{M} A_i \right) = \cap_{i=2}^{M} (A_1 \cup A_i)$$

$$A_1 \cap \left( \cup_{i=2}^{M} A_i \right) = \cup_{i=2}^{M} (A_1 \cap A_i)$$

---

## Pagina 12

Nomenclatura probabilistica

- Ω si definisce evento certo;
- ∅ si definisce evento impossibile;
- A e $\bar{A}$ si definiscono eventi complementari;
- Due eventi $A$ e $B$ tali che $A \cap B = \emptyset$ si definiscono incompatibili o mutuamente esclusivi;
- Se $A \subseteq B$ si dice che $A$ implica $B$, cioè il verificarsi di $A$ implica che si verifici $B$.

---

## Pagina 13

Qualche esempio

- Con riferimento al lancio singolo di una moneta, $T = \{Risultato Testa\}$ e $C = \{Risultato Croce\}$ sono eventi complementari (e quindi mutuamente esclusivi), $\overline{T} \cap \overline{C} = \overline{T} \cup \overline{C} = \overline{\Omega} = \emptyset$ l'evento impossibile.

- Con riferimento a un lancio doppio, l'evento $D = \{Almeno una croce\}$ è incompatibile con $\{TT\}$, e può essere espresso in vari modi:

$$D = \{CC, TC, CT\} = \overline{TT} = \Omega \setminus \{TT\} = \{CC\} \cup \{TC\} \cup \{CT\}$$

- Con riferimento all'esempio # 2 ed agli eventi li definiti: $A \text{ e } B$ sono incompatibili (inoltre sono complementari, per cui $A \cup B = \Omega$), come incompatibili sono $A \text{ e } D \text{ e } B \text{ e } C$; inoltre $C \subseteq A$, cioè $C$ implica $A$.

---

## Pagina 14

Un esperimento semplice: lancio di un dado

Si supponga di lanciare un dado onesto $n$ volte. Avremo quindi $n$ risultati in $\Omega = \{1, 2, 3, 4, 5, 6\}$: detto $n_i$ il numero di volte (su $n$ lanci) in cui il risultato è $i$, ci si aspetta che, per $n$ sufficientemente grande, i valori di $n_i$ siano all’incirca uguali, $n_i \simeq \frac{n}{|\Omega|} = \frac{n}{6}$. Definiamo i due sottoinsiemi $A = \{1, 3, 5\}$ e $B = \{2, 4, 6\}$; detti $n_A e n_B$ il numero di prove in cui si verificano $A$ e $B$ rispettivamente avremo:

$$n_A = n_1 + n_3 + n_5 \simeq n \frac{|A|}{|\Omega|} \quad n_B = n_2 + n_4 + n_6 \simeq n \frac{|B|}{|\Omega|}$$

Pertanto la frazione di volte in cui si verificano i due eventi si scrive:

$$\frac{n_A}{n} \simeq \frac{|A|}{|\Omega|} = \frac{1}{2} \quad \frac{n_B}{n} \simeq \frac{|B|}{|\Omega|} = \frac{1}{2}$$

---

## Pagina 15

L’esperimento ora consiste nel lanciare due volte consecutive il dado onesto e nel registrare gli esiti del primo e del secondo lancio. Lo spazio campione è ora un insieme ordinato di 36 elementi:

$$\Omega = \{(1, 1), \ldots, (1, 6), \ldots (6, 1), \ldots (6, 6)\}$$

Per l’onestà del dado, ci si attende che, per un numero di prove $n$ sufficientemente alto, ogni singola coppia esca all’incirca $\frac{n}{|\Omega|} = \frac{n}{36}$ volte. Sia $A$ l’evento:

$$A = \{Esce almeno un 6\} = \{(1, 6), \ldots (5, 6), (6, 1), \ldots (6, 6)\}$$

Per lo stesso ragionamento condotto in precedenza, ci si aspetta che la frequenza con cui si verifica l’evento $A$ in $n$ prove sia:

$$\frac{n_A}{n} \approx \frac{|A|}{|\Omega|} = \frac{11}{36}$$

---

## Pagina 16

Spazi finiti con eventi elementari equivalenti

- Sia $\Omega$ uno spazio dei campioni finito;
- Si assuma che tutti gli *eventi elementari* (cioè, gli elementi di $\Omega$) siano *equivalenti*, cioè che non esista alcun elemento "privilegiato" rispetto agli altri: questo equivale ad assumere che, eseguendo un numero sufficientemente elevato di prove, ciascun evento elementare si verifici un numero di volte approssimativamente uguale a quello di qualsiasi altro evento elementare;
- Detto $A \subseteq \Omega$ un qualsiasi evento, la frequenza di occorrenza di $A$ gode della proprietà:

$$f_n(A) = \frac{n_A}{n} \rightarrow \frac{|A|}{|\Omega|}, \quad n \rightarrow \infty$$

- Quindi per eventi equivalenti è importante saper *contare* le cardinalità dei sotto-insiemi che definiscono gli eventi di interesse.
- La branca che si occupa di questo problema si chiama *calcolo combinatorio*

---

## Pagina 17

Si considerino $k$ insiemi finiti, $A_1, \ldots, A_k$, non necessariamente distinti.

- Si definisce prodotto cartesiano $A^{(k)} = A_1 \times \ldots \times A_k$ un insieme costituito dalle $k$-ple ordinate in cui il primo elemento appartenga a $A_1$, il secondo a $A_2$ e così via.
- Siccome il primo elemento si può scegliere in $|A_1|$ modi, il secondo in $|A_2|$ e così via, avremo:

$$\left| A^{(k)} \right| = \prod_{i=1}^{k} |A_i|$$

- Questa è la relazione fondamentale del calcolo combinatorio, dalla quale molte altre formule di conteggio derivano.

---

## Pagina 18

k–ple ordinate senza ripetizione

- Si supponga $A = \{a_1, \ldots, a_n\}$;
- Si vogliono contare le stringhe di lunghezza $k$ di elementi di $A$ in cui ogni elemento di $A$ compaia una sola volta (cioè, le ripetizioni non sono ammesse).
- Questo implica - nella formula precedente - che $|A_1| = |A| = n$, $|A_2| = n - 1, \ldots, |A_k| = n - k + 1$.
- Pertanto il richiesto numero è

$$\left| A^{(k)} \right| = n(n - 1)(n - 2) \cdots (n - k + 1) = \prod_{i=0}^{k-1} (n - i)$$

---

## Pagina 19

k–ple ordinate con ripetizione

- Si supponga $A = \{a_1, \ldots, a_n\}$;
- Si vogliono contare le stringhe di lunghezza $k$ di elementi di $A$ in cui ogni elemento di $A$ possa ripetersi (cioè le ripetizioni sono ammesse).
- Questo implica - nella formula precedente - che $|A_1| = |A_2| = \ldots = |A_k| = |A| = n$,
- Pertanto il richiesto numero è

$$|A^{(k)}| = n^k$$

- Esempio: il numero delle $k–ple binarie è il numero di $k–ple ordinate con ripetizione prese dall’insieme di cardinalità due $\{0, 1\}$ è $2^k$.

---

## Pagina 20

Un caso particolare - ma molto rilevante - del calcolo precedente è quando $k = n$. La domanda cui si vuole rispondere è:

- Dato un insieme di $n$ elementi, quante $n$–ple ordinate si possono formare?
- Risposta: È un caso speciale di enumerazione di $k$–ple quando $k = n$, cioè:

$$\# \text{ permutazioni di } n \text{ elementi} = n(n - 1) \cdot \ldots \cdot 1 = n!$$

Questo ci conduce immediatamente al concetto di combinazioni.

---

## Pagina 21

Combinazioni $C_{n,k}$

Le combinazioni $C_{n,k}$ di "n elementi su $k$ posti" è il numero di $k$-ple non ordinate che si possono formare con $n$ elementi (cioè, il numero di sottoinsiemi di $\Omega$ di cardinalità $k$).

Pertanto, le $k!$ permutazioni di una stessa $k$-pla ordinata "collassano" in un'unica combinazione. Questo comporta:

$$C_{n,k} = \frac{n(n-1) \cdots (n-k+1)}{k!} = \frac{n!}{k!(n-k)!} = \binom{n}{k}$$

dove $\binom{n}{k}$ è il coefficiente binomiale $(n,k)$.

---

## Pagina 22

Si considerino le 52 carte francesi con i quattro semi (Cuori (C), Fiori (F), Picche (P), Quadri (Q)). Si supponga di estrarre dal mazzo $k$ carte, senza reinserirle dopo ogni estrazione. Si calcolino:

a Il numero di possibili quaterne ordinate;
b Il numero di quaterne non ordinate;
c Il numero di quaterne (C,F,P,Q);
d Il numero di cinquine non ordinate in cui compaiano esattamente due assi.

---

## Pagina 23

Esperimenti e Eventi
Leggi di Probabilità su Spazi Campione discreti
Spazi Campione Continui
Processi Aleatori
Processi aleatori

Tecniche di conteggio

Soluzione

a Si ponga $k = 4$ e $n = 52$ nelle formula che conta le $k$-ple ordinate senza ripetizione. Si ha
$$52 \cdot 51 \cdot 50 \cdot 49 = 6497400$$

b Le 4! permutazioni di ogni quaterna collassano in un'unica quaterna, per cui si ha $\frac{52 \cdot 51 \cdot 50 \cdot 49}{4!} = \frac{6497400}{24} = 270725$.

c Si usi la formula sulle $k$-ple ordinate per $|\Omega_i| = 13$ e $k = 4$, per cui si ha $13^4 = 28561$.

d Gli assi sono 4 per cui si possono combinare in $\binom{4}{2} = 6$ modi. Le altre 48 carte possono combinarsi sui residui tre posti in $\binom{48}{3} = 17296$ modi, per cui abbiamo
$$\binom{4}{2} \binom{48}{3} = 69184$$

---

## Pagina 24

Insieme delle parti di un insieme finito

Si consideri un insieme $A$ con $n$ elementi.

- L’insieme delle parti $\mathcal{P}(A)$ di $A$ è l’insieme di tutti i possibili sottoinsiemi di $A$.
- Negli insiemi ovviamente l’ordinamento non conta, per cui il numero di sottoinsiemi $k$–dimensionali di $A$ è

$$\begin{pmatrix} n \\ k \end{pmatrix}$$

- Siccome tanto l’insieme vuoto (0-dimensionale) quanto $A$ ($n$–dimensionale) sono sottoinsiemi di $A$, avremo:

$$|\mathcal{P}(A)| = \sum_{k=0}^{n} \binom{n}{k} = 2^n$$

---

## Pagina 25

Prove ripetute e conteggio dei successi

Si consideri una stringa binaria di lunghezza $n$ che abbia $k$ valori "1" e $(n-k)$ valori "zero". Si vuole contare quante stringhe di lunghezza $n$ abbiano $k$ "1" e $(n-k)$ "0".

- Si parta da una stringa qualsiasi contenente $k$ uno e $n-k$ "zero" in date posizioni;
- Le permutazioni di questa stringa sono $n!$;
- Tuttavia tutte le $k!$ permutazioni degli uno sulle $k$ posizioni occupate già da "1" nella stringa originaria sono inefficaci (cioè, portano alla stessa sequenza iniziale), per cui le permutazioni al netto di queste $k!$ sono $n!/k!$.
- Analogamente sono inefficaci le $(n-k)!$ permutazioni degli "0" sulle posizioni che già occupavano nella stringa iniziale, che porta in conto un’ulteriore divisione per $(n-k)!$.
- In conclusione il numero richesto è $\binom{n}{k}$.

---

## Pagina 26

Dalla frequenza alla probabilità

- Dato uno spazio dei campioni discreto $\Omega$ e un suo qualunque sottoinsieme (o evento) $A$ si definisce probabilità che occorra $A$ il limite della frequenza di occorrenza di $A$ quando il numero di esperimenti - o prove - tende all’infinito, cioè:

$$\mathbb{P}(A) = \lim_{n \to \infty} \frac{n_A}{n}$$

- A questo punto il concetto di spazio finito con eventi elementari equivalenti diviene quello di spazio finito con eventi elementari equiprobabili.

- Si ha di conseguenza che, per uno spazio finito a eventi elementari equiprobabili vale la relazione generale:

$$\mathbb{P}(A) = \frac{|\Omega_A|}{|\Omega|}$$

dove $\Omega_A$ contiene tutti gli eventi che comportano il verificarsi di $A$.

---

## Pagina 27

Esempio: I punteggi del Poker

- Un giocatore estrae (senza reinserimento) 5 carte da un mazzo di carte da poker (contenente le carte dal 7 all’asso, per un totale di $8 \times 4 = 32$ carte).

- Calcolare le seguenti probabilità:

  a. Coppia di assi e coppia qualsiasi;
  b. Almeno tre assi;
  c. Un tris qualsiasi (ma non un full nè un poker);
  d. Colore di picche o colore qualsiasi.

---

## Pagina 28

Soluzione - [a]

Lo spazio dei campioni è -per tutti i casi - l’insieme di tutte le cinquine di elementi (ovviamente distinti), ma non importa l’ordine, per cui:

$$|\Omega| = \binom{32}{5} = \frac{32!}{5!27!} = 201376$$

Sia $C_2 \subseteq \Omega$ l’insieme delle cinquine con due assi. Quindi due dei cinque posti sono occupati da due dei 4 assi, mentre le altre 28 carte sono qualsiasi (questo include nel calcolo anche i full e le doppie coppie). Avremo:

$$|C_2| = \binom{4}{2} \binom{28}{3} = 19656 \rightarrow \mathbb{P}\{C_2\} = 0.097$$

Volendo escludere la possibilità di punteggi più alti della coppia d’assi, avremo che – ferme restando le due posizioni occupate da due assi – la terza può essere occupata solo da 28 carte, la quarta da 24 e la quinta da 20, per cui:

$$|C_2'| = \binom{4}{2} \frac{28 \times 24 \times 20}{3!} = 13440 \rightarrow \mathbb{P}\{C_2\} = 0.067$$

Se la coppia può essere qualsiasi le precedenti probabilità vanno multiplicate per 8.

---

## Pagina 29

Sia $C_3 \subseteq \Omega$ l’insieme di cinquine che contengono esattamente tre assi e quelle che ne contengono 4.

Avremo:

$$|C_3| = \overbrace{\begin{pmatrix} 4 \\ 3 \end{pmatrix}}^{3 \text{ assi}} \overbrace{\begin{pmatrix} 28 \\ 2 \end{pmatrix}}^{4 \text{ assi}} + \overbrace{\begin{pmatrix} 4 \\ 4 \end{pmatrix}}^{4 \text{ assi}} \overbrace{\begin{pmatrix} 28 \\ 1 \end{pmatrix}} = 1512 + 28 = 1540$$

Siccome lo spazio dei campioni è inalterato, la probabilità richiesta vale

$$\mathbb{P}\{C_3\} = \frac{1540}{201376} = 0.0076$$

---

## Pagina 30

Soluzione - [c]

- Sia $C_3' \subseteq \Omega$ l'insieme che contiene tutte le cinquine che diano un tris e le altre due carte diverse. Indichiamo on $C_3'(7)$ l'insieme delle cinquine che contengono esattamente un tris di sette. Avremo:

$$|C_3'| = 8 |C_3'(7)|$$

- Per calcolare $|C_3'(7)|$, sappiamo che 3 posizioni sono occupate da un sette (il che può avvenire in $\binom{4}{3} = 4$ modi), la quarta carta può essere scelta in 28 modi e la quinta in 24. Siccome l'ordine non conta avremo:

$$|C_3'(7)| = 4 \frac{28 \times 24}{2} = 1344 \rightarrow \mathbb{P}\{C_3'(7)\} = \frac{1344}{201376} = 0.0067$$

- La probabilità richiesta vale allora

$$\frac{8 \times 4 \times 28 \times 24}{201376} = 0.053$$

---

## Pagina 31

Sia $C_P \subseteq \Omega$ l’insieme di tutte le possibili cinquine di carte di picche. Poichè ci sono 8 carte di picche da distribuite su 5 posti con ordine inessenziale, avremo (N.B. Questo include le scale reali):

$$|C_P| = \binom{8}{5} = 56 \rightarrow \mathbb{P}\{C_P\} = \frac{56}{201376} = 0.00027$$

Pertanto la probabilità di un colore qualsiasi vale

$$\mathbb{P}\{colore\} = 0.0011$$

Se vogliamo escludere le scale reali, dobbiamo togliere dalle cinquine tutte quelle che vedono le carte consecutive. Esistono 5 scale reali per ogni seme (dalla minima, (A,7,8,9,10) alla massima (10,J,Q,K,A)), per cui in questo caso:

$$|C_P| = 56 - 5 = 51 \rightarrow \mathbb{P}\{C_P\} = \frac{51}{201376} = 0.00025 \rightarrow \mathbb{P}\{colore\} = 0.001$$

---

## Pagina 32

Frequenza di occorrenza e probabilità su Spazi finiti

- Sia $\Omega$ uno spazio campione discreto (cioè, finito o numerabile);
- Rimuoviamo ora l’ipotesi che gli eventi elementari siano equiprobabili;
- La definizione di probabilità data in precedenza vale ancora. In particolare:
  a $A \subseteq \Omega$ è un evento e si conducono $n$ esperimenti;
  b Sia $n_A = n_A(n)$ il numero di volte in cui $A$ si verifica;
  c Frequenza di occorrenza e probabilità si definiscono:

$$f_n(A) = \frac{n_A}{n} \quad \mathbb{P}(A) = \lim_{n \to \infty} f_n(A) = \lim_{n \to \infty} \frac{n_A}{n}$$

d La principale differenza con quanto visto prima è che ora non è più vero in generale che $n_A \approx n|A|$.

- Detto in altre parole, quando gli eventi elementari non sono equiprobabili, un evento $A \subseteq \Omega$ ha una misura diversa da quella - ordinaria - data dal numero dei suoi elementi distinti;
- Quindi due eventi, $A \subseteq \Omega$ e $B \subseteq \Omega$ di uguale cardinalità ($|A| = |B|$) possono avere "pesi" (cioè misure) diverse e le tecniche di conteggio non sono più utili ai fini del calcolo della probabilità.

---

## Pagina 33

Un esempio: il dado truccato

Supponiamo di avere - in analgia all’esempio #2 - un dado, ma questa volta truccato in modo che 5 volte su 6 esca il risultato 1. Si lanci il dado un’unica volta, per cui

$$\Omega = \{1, 2, 3, 4, 5, 6\}$$

Sia $A = \{II risultato è pari\} = \{2, 4, 6\}$ e $B = \{II risultato è dispari\} = \{1, 3, 5\}$. Se $n_i$ è in numero di volte (su $n$ prove) in cui esce il risultato $i$, avremo:

$$\sum_{i=1}^{6} n_i = n, \quad n_1 \approx 5 \sum_{i=2}^{6} n_i \quad \forall i \neq 1 \rightarrow \frac{n_1}{n} = f_n(1) = 5 \sum_{i=2}^{6} f_n(i)$$

$$\mathbb{P}(\{1\}) = 5 \sum_{i=2}^{6} \mathbb{P}(\{i\}_{i \neq 1}) \quad \text{poichè} \sum_{i=1}^{6} f_n(i) = 1 \rightarrow \sum_{i=1}^{6} \mathbb{P}(\{i\}) = 1$$

$$\mathbb{P}(\{1\}) = \frac{5}{6} \quad \mathbb{P}(\{i\}_{i=2,\dots,6}) = \frac{1}{30}$$

Quindi:

$$f_n(A) = \frac{n_2 + n_4 + n_6}{n} \rightarrow \frac{3}{30} = \frac{1}{10} \quad f_n(A) = \frac{n_1 + n_3 + n_5}{n} \rightarrow \frac{5}{6} + \frac{2}{30} = \frac{9}{10}$$

laddove con tecniche di conteggio avremmo trovato che, essendo $|A| = |B| = |\Omega|/2$, le due probabilità sarebbero valse 1/2. In altre parole, $B$ ha ora una misura molto maggiore di $A$.

---

## Pagina 34

Alcune proprietà della frequenza di occorrenza e della probabilità - 1

- Siano $A \subseteq \Omega$ e $B \subseteq \Omega$ due eventi;
- Siano $n_A = n_A(n)$ e $n_B = n_B(n)$ il numero di occorrenze su $n$ prove, $f_n(A)$ e $f_n(B)$ le relative frequenze, e $\mathbb{P}(A)$ e $\mathbb{P}(B)$ i rispettivi limiti (cioè le probabilità).

Valgono le seguenti proprietà:

a. Eventi complementari:

$$f_n(\overline{A}) = \frac{n - n_A}{n} = 1 - f_n(A) \implies \mathbb{P}(\overline{A}) = 1 - \mathbb{P}(A)$$

b. Sub-additività:

$$f_n(A \cup B) = \frac{n_{AUB}}{n} = \frac{n_A + n_B - n_{A \cap B}}{n} = f_n(A) + f_n(B) - f_n(A \cap B) \rightarrow \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$$

Infatti, se $A$ e $B$ non sono incompatibili sommare semplicemente $n_A$ e $n_B$ equivarrebbe a contare due volte le occorrenze di entrambi (cioè le occorrenze di $A \cap B$), il che spiega il termine sottrattivo.

---

## Pagina 35

Alcune proprietà della frequenza di occorrenza e della probabilità - 2

c Sottrazione tra insiemi

$$f_n(A \setminus B) = f_n(A \cap \overline{B}) = \frac{n_A - n_A \cap B}{n} = f_n(A) - f_n(A \cap B) \rightarrow$$

$$\mathbb{P}(A \setminus B) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$$

Infatti, dovendosi verificare $A$ ma non $B$, bisogna sortrarre a $n_A$ il numero di experimenti in cui si verificano entrambi, $n_A \cap B$.

d Evento certo ed evento impossibile. Banalmente:

$$f_n(\Omega) = \frac{n}{n} = 1 \rightarrow \mathbb{P}(\Omega) = 1 \rightarrow \mathbb{P}(\emptyset) = \mathbb{P}(\overline{\Omega}) = 0$$

---

## Pagina 36

Frequenze e probabilità condizionate

Siano $A$ e $B$ due eventi che occorrano $n_A$ e $n_B$ volte su $n$ experimenti. Definiamo ora la frequenza di occorrenza di $A$ condizionata a $B$ – $f_n(A|B)$ – il rapporto tra il numero di prove in cui si verificano entrambi ($n_A \cap B$) e il numero di volte in cui si verifica solo $B$, cioè, formalmente:

$$f_n(A|B) = \frac{n_A \cap B}{n_B} = \frac{n(A \cap B)}{n} \frac{n}{n_B} = \frac{f_n(A \cap B)}{f_n(B)} \rightarrow \mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$

In altre parole, restringiamo il nostro campione di analisi solo agli $n_B$ risultati che abbiano condotto al verificarsi di $B$. Ovviamente:

$$\mathbb{P}(B|A) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)} \Leftrightarrow \mathbb{P}(A \cap B) = \mathbb{P}(B|A)\mathbb{P}(A) = \mathbb{P}(A|B)\mathbb{P}(B)$$

L’ultima relazione prende anche il nome di legge della probabilità composta.

---

## Pagina 37

Un’importante conseguenza della definizione di probabilità condizionata è la legge della probabilità totale.

Sia $\{E_i\}_{i=1}^M$ una partizione di $\Omega$, cioè:

$$\cup_{i=1}^M E_i = \Omega \quad E_i \cap E_j = \emptyset \text{ for } i \neq j$$

Se $A \subseteq \Omega$, avremo allora:

$$\mathbb{P}(A) = \mathbb{P}(A \cap \Omega) = \mathbb{P}(A \cap \cup_{i=1}^M E_i) = \mathbb{P}\left(\cup_{i=1}^M A \cap E_i\right)$$

Essendo $E_i \cap E_j = \emptyset$, avremo ovviamente che $(A \cap E_i) \cap (A \cap E_j) = \emptyset$, per cui:

$$\mathbb{P}(A) = \sum_{i=1}^M \mathbb{P}(A \cap E_i) = \sum_{i=1}^M \mathbb{P}(A | E_i) \mathbb{P}(E_i)$$

---

## Pagina 38

Eventi Indipendenti

- Due eventi, $A \subseteq \Omega$ e $B \subseteq \Omega$ si dicono indipendenti quando il verificarsi di uno non ha nessuna influenza sul verificarsi o meno dell’altro.
- In altre parole, due eventi $A$ e $B$ sono indipendenti se (e solo se) $f_n(A|B) = f_n(A)$ e $f_n(B|A) = f_n(B)$.
- Pertanto, sfruttando la legge della probabilità composta (o, equivalentemente, la definizione di probabilità condizionata) avremo che, se $A$ e $B$ sono indipendenti:

$$f_n(A \cap B) = f_n(A)f_n(B) \Leftrightarrow \mathbb{P}(A \cap B) = \mathbb{P}(A) \mathbb{P}(B)$$

- Esempio: Lancia di un dado onesto due volte consecutive.

$$\mathbb{P}(\{i,j\}) = \mathbb{P}(\{i\})\mathbb{P}(\{j\}) = \frac{1}{6}\frac{1}{6} = \frac{1}{36}$$

---

## Pagina 39

L'approccio assiomatico alla teoria della probabilità

- Si consideri una famiglia di sottoinsiemi di $\Omega$, sia essa $\mathcal{E} = \{A_1, \ldots, A_N\}$;
- Si assuma che la famiglia $\mathcal{E}$ soddisfi le seguenti due proprietà:
  - Essa è *chiusa* rispetto all'unione, cioè:
    $$\text{se} \quad A_1 \in \mathcal{E}, A_2 \in \mathcal{E} \Rightarrow A_1 \cup A_2 \in \mathcal{E};$$
  - Essa è *chiusa* rispetto alla complementazione, cioè:
    $$\text{se} \quad A_1 \in \mathcal{E} \Rightarrow \overline{A_1} \in \mathcal{E};$$
- Sotto le precedenti condizioni, $\mathcal{E}$ si definisce un'*Algebra di sotto-insiemi di $\mathcal{E}$*, o algebra di eventi.
- Se la collezione $\mathcal{E}$ contiene un'infinità (numerabile) di elementi, allora $\mathcal{E}$ si definisce una $\sigma$-algebra se, oltre ad essere chiusa rispetto alla complementazione e all'unione, è anche chiusa rispetto all'unione di un'infinità numerabile di suoi elementi.

---

## Pagina 40

Proprietà delle Algebre

- Se $A, B \in \mathcal{E}$ allora $A \cap B \in \mathcal{E}$. Infatti, per la relazione di De Morgan abbiamo:

$$A \cap B = \overline{A} \cup \overline{B} \in \mathcal{E}$$

poichè $(\overline{A}, \overline{B}) \in \mathcal{E}$$

- Se $A, B \in \mathcal{E}$ allora $A \setminus B \in \mathcal{E}$. Infatti:

$$A \setminus B = A \cap \overline{B} \in \mathcal{E}$$

per la precedente proprietà

- Se $A$ è un evento qualsiasi, allora la minima algebra che contiene $A$ è $\mathcal{E} = \{A, \overline{A}, \Omega, \emptyset\}$. Infatti:

  - $\overline{A}$ deve essere elemento di $\mathcal{E}$ per la chiusura rispetto alla complementazione;
  - $A \cup \overline{A} = \Omega$ deve essere un elemento di $\mathcal{E}$ per la proprietà di chiusura rispetto all’unione e $\emptyset = \Omega$ deve esso stesso appartenervi per la chiusura rispetto alla complementazione.

---

## Pagina 41

Spazi di probabilità

- Si definisce legge di probabilità una funzione con dominio $\mathcal{E}$ e co-dominio $[0,1]$, cioè:
  $$\mathbb{P} : A \in \mathcal{E} \rightarrow \mathbb{P}(A) \in [0,1]$$
- che soddisfi i seguenti Assiomi di Kolmogorov:
  1. Non negatività, cioè $\mathbb{P}(A) \geq 0 \forall A \in \mathcal{E}$;
  2. Normalizzazione, cioè $\mathbb{P}(\Omega) = 1$
  3. Sub-additività, cioè:
    $$A \text{ e } B \text{ incompatibili} (A \cap B = \emptyset) \implies \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$$
- 3a Numerabile additività. Se $\{B_n\}_{n \in \mathbb{N}}$ è una collezione numerabile di eventi incompatibili, allora:
  $$\mathbb{P}(\cup_{n=1}^{\infty} B_n) = \sum_{n=1}^{\infty} \mathbb{P}(B_n)$$
- La terna $(\Omega, \mathcal{E}, \mathbb{P})$ si definisce Spazio di Probabilità.

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops  Metodi Statistici per l Informazione - Marco Lops 41 / 161

---

## Pagina 42

Un diverso approccio alla probabilità
Variabili Aleatorie Discrete
Variabili Aleatorie Discrete Doppie
Variabili Aleatorie Discrete Doppie

Proprietà delle leggi di probabilità (qualche esempio)

† Eventi complementari:

$$\mathbb{P}(\Omega) = \mathbb{P}(A \cup \bar{A}) = \mathbb{P}(A) + \mathbb{P}(\bar{A}) = 1 \implies \mathbb{P}(\bar{A}) = 1 - \mathbb{P}(A)$$

† Sottrazione tra insiemi:

$$A = A \cap \Omega = A = A \cap (B \cup \bar{B}) = (A \cap B) \cup (A \cap \bar{B})$$

Siccome $(A \cap B)$ e $(A \cap \bar{B})$ sono incompatibili, allora ritroviamo la proprietà $\mathbb{P}(A \cap \bar{B}) = \mathbb{P}(A \setminus B) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$.

† Unione di eventi non incompatibili $(A \cap B \neq \emptyset)$. Osserviamo preliminarmente che $A = A \cup (B \cap \bar{A})$, Per cui

$$\mathbb{P}(A) = \mathbb{P}(A) + \underbrace{\mathbb{P}(B \cap \bar{A})}_{= \mathbb{P}(B) - \mathbb{P}(A \cap B)} = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l Informazione - Marco Lops 42 / 161

---

## Pagina 43

Dimostrare che se due eventi $(A, B)$ sono indipendenti, lo sono anche i loro compementari.

Svolgimento

Dire che $A$ e $B$ sono indipendenti significa che $\mathbb{P}(A \cap B) = \mathbb{P}(A) \mathbb{P}(B)$, per cui dobbiamo dimostrare che $\mathbb{P}(\overline{A} \cap \overline{B}) = \mathbb{P}(\overline{A}) \mathbb{P}(\overline{B})$.

Ricordiamo che la relazione di De Morgan stabilisce che $\overline{A} \cap \overline{B} = \overline{A} \cup \overline{B}$. Pertanto avremo che

$$\mathbb{P}(\overline{A} \cap \overline{B}) = 1 - \mathbb{P}(A \cup B)$$

Avremo quindi

$$\mathbb{P}(\overline{A} \cap \overline{B}) = 1 - \mathbb{P}(A) - \mathbb{P}(B) + \overbrace{\mathbb{P}(A \cap B)}^{=\mathbb{P}(A) \mathbb{P}(B)} =$$

$$1 - \mathbb{P}(A) - \mathbb{P}(B)(1 - \mathbb{P}(A)) = \underbrace{(1 - \mathbb{P}(A))}_{\mathbb{P}(\overline{A})} \underbrace{(1 - \mathbb{P}(B))}_{\mathbb{P}(\overline{B})} = \mathbb{P}(\overline{A}) \mathbb{P}(\overline{B})$$

---

## Pagina 44

<table><thead><tr><th>Un diverso approccio alla probabilità</th></tr></thead><tbody><tr><td>Variabili Aleatorie Discrete</td></tr><tr><td>Variabili Aleatorie Discrete Doppie</td></tr><tr><td>Variabili Aleatorie Discrete Doppie</td></tr></tbody></table>

---

## Pagina 45

La sequenza di numeri $\mathbb{P}(X=x) = p_X(x)$, $x \in \mathcal{X}$ si chiama probability mass function (pmf) o Distribution Function (DF) o probability density function (pdf) della variabile aleatoria $X$.

Ovviamente, date le proprietà della probabilità:

$$p_X(x) = \lim_{n \to \infty} \frac{n_x}{n} \rightarrow p_X(x) \geq 0 \quad \sum_{x \in \mathcal{X}} p_X(x) = 1$$

dove $n_x = n_{\{X=x\}}$ rappresenta il numero di occorrenze dell’evento $\{X=x\}$.

Esempio: $\{\mathcal{X}\} = \{1, 2, 3, 4\}$. Può ($\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8}$) essere una pdf?

$$p_X(x) \geq 0 \quad \sum_{x \in \mathcal{X}} p_X(x) = \sum_{i=1}^{4} p_X(x_i) = \sum_{i=1}^{4} \mathbb{P}(X=i) = 1$$

quindi la risposta è si!

---

## Pagina 46

Un’avvertenza sulle notazioni

Per come è stata definita, la probabilità è una funzione definita su un insieme di sottoinsiemi di Ω e a valori in [0, 1],cioè:

$$\mathbb{P} : A \subseteq \Omega \rightarrow \mathbb{P}(A) \in [0, 1]$$

In realtà, bisognerebbe strutturare Ω in modo opportuno (cioè introdurre un’algebra di eventi), ma sorvoliamo. Il punto è che, quando si passa alle variabili aleatorie la notazione corretta sarebbe:

$$\text{Probabilità}(X = x) = \mathbb{P}(\omega \in \Omega : X(\omega) = x)$$

Per contro, noi usiamo la notazione semplificata $\mathbb{P}(X = x)$, talvolta "complicandola" nella forma $\mathbb{P}(\{X = x\})$, che evoca che a rigore ci riferiamo a un insieme di punti di Ω. Useremo queste notazioni intercambiabilmente ogni volta che non ci sia il pericolo di generare equivoci.

---

## Pagina 47

La media campionaria

- Una variabile aleatoria $X$ si dice caratterizzata se è assegnata la sequenza dei $|\mathcal{X}|$ valori della sua pmf;
- Esistono caratterizzazioni meno precise che sono spesso utili: una di queste è la media campionaria;
- Si supponga di avere la variabile aleatoria $X(\omega)$ e si supponga di compiere $n$ esperimenti;
- La collezione dei risultati sarà $[X(\omega_1), \ldots, X(\omega_n)]$.
- Una scelta naturale per avere un’idea del comportamento di $X(\omega)$ è eseguire la media campionaria delle misure, cioè:

$$\overline{X_n} = \frac{1}{n} \sum_{i=1}^{n} X(\omega_i)$$

---

## Pagina 48

La media statistica

Riconsideriamo la media campionaria

$$\overline{X_n} = \frac{1}{n} \sum_{i=1}^{n} X(\omega_i)$$

Naturalmente, siccome $X(\omega_i) \in \mathcal{X} = \{x_1, \ldots, x_M\}$, al crescere di $n$ avremo che $X(\omega)$ assumerà $n_1$ volte il valore $x_1$, $n_2$ il valore $x_2$ e così via (il caso $M = \infty$ va trattato come caso limite). Quindi, per $n \to \infty$:

$$\overline{X_n} = \frac{1}{n} \sum_{i=1}^{M} n_i x_i = \sum_{i=1}^{M} x_i f_n(x_i) \rightarrow \sum_{i=1}^{M} x_i \mathbb{P}(X = x_i) = \sum_{i=1}^{M} x_i p_X(x_i) \stackrel{\text{def}}{=} \mathbb{E}[X]$$

dove ricordiamo che $f_n(x_i) = \frac{n \{X = x_i\}}{n}$.

La quantità $\mathbb{E}[X]$ si definisce media statistica della variabile aleatoria $X$.

---

## Pagina 49

Un esempio: il conteggio Bernoulliano - 1

- Consideriamo il lancio per $N$ volte di una moneta;
- La moneta dall’un risultato "T" (testa) con frequenza che tende a $p < 1$ e "C" (croce) con frequenza che tende a $q = 1 - p$;
- I lanci ovviamente sono indipendenti, nel senso che l’esito di ogni lancio non dipende da quelli precedenti e successivi;
- Quindi lo spazio campione è l’insieme delle $N$-ple del tipo:

$$\underbrace{(C, C, T, T, C, \dots\dots, C, T, T)}_{N}$$

- Definita $X_N(\omega)$ la variabile aleatoria che "conta" il numero di "T" (teste) che si realizzano in $N$ lanci, se ne vuole una caratterizzazione.

---

## Pagina 50

Conteggio Bernoulliano - 2

La variabile aleatoria $X : \Omega \rightarrow \mathcal{X}$ è:

$$X_N : \omega \in \{T, C\}^N \rightarrow X_N(\omega) \in \overset{\mathcal{X}}{\{0, \dots, N\}} \quad X_N(\omega) = k \text{ se } \omega \text{ contiene } k \text{" } T"$$

Ora consideriamo $\omega = \underbrace{[T, \dots, T]}_{k \text{ volte}} \underbrace{C, \dots, C]}_{N-k \text{ volte}}$. Per l’indipendenza dei lanci (vedi slide 38) avremo:

$$\mathbb{P}(\omega) = \mathbb{P}(\underbrace{T \cap \dots \cap T}_{k \text{ volte}} \cap \underbrace{C \cap \dots \cap C]}_{N-k \text{ volte}} = p^k q^{N-k}$$

Le sequenze che hanno $k$ teste e $(N-k)$ croci sono dunque tutte equiprobabili e sono in numero $C_{N,k} = \binom{N}{k}$.

Sia $\Omega_{N,k} = \cup_i \{\omega_i^*\}_{i=1}^{C_{N,k}}$ l’insieme di queste sequenze. Avremo:

$$\mathbb{P}(X_N = k) = p_{X_N}(k) = \mathbb{P}(\Omega_{N,k}) = \mathbb{P}\left(\cup_{i=1}^{C_{N,k}} \{\omega_i^*\}\right)$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l’Informazione - Marco Lops 49 / 161

---

## Pagina 51

Siccome gli eventi elementari sono sempre mutuamente esclusivi ($\mathbb{P}(\{\omega_i^*\} \cap \{\omega_j^*\}) = 0$ $\forall i \neq j$, avremo (vedi slide 34):

$$p_{X_N}(k) = \sum_{i=1}^{C_N,k} \mathbb{P}(\{\omega_i^*\}) = \binom{N}{k} p^k q^{N-k}$$

che prende il nome di pmf binomiale di parametri $N$ e $p$ (in breve, $X_N \sim \mathcal{B}(N,p)$). Si noti:

$$p_{X_N}(k) \geq 0 \ \forall k \quad \sum_{x \in \mathcal{X}} p_{X_N}(x) = \sum_{k=0}^{N} \binom{N}{k} p^k q^{N-k} = (p+q)^N = 1$$

Infine:

$$\mathbb{E}[X_N] = \sum_{x \in \mathcal{X}} xp_{X_N}(x) = \sum_{k=0}^{N} k \binom{N}{k} p^k q^{N-k} = Np$$

---

## Pagina 52

La variabile Uniforme

Una variabile aleatoria $X$ che assuma valore in un qualsiasi alfabeto $X$ di cardinalità finita, $|\mathcal{X}| = M$ si dice uniformemente distribuita su $X$ (in breve, $X \sim U(\mathcal{X})$) se:

$$p_X(x) = \mathbb{P}(X = x) = \frac{1}{M} \quad \forall x \in \mathcal{X}$$

- Ovviamente $p_X(x)$ soddisfa le condizioni necessarie per poter essere una pmf;
- Il calcolo della media è immediato:

$$\mathbb{E}[X] = \sum_{x \in \mathcal{X}} xp_X(x) = \frac{1}{M} \sum_{x \in \mathcal{X}} x = \text{Media aritmetica dei valori dell'alfabeto}$$

- Un caso interessante è $\mathcal{X} = \{0, 1, \ldots, M-1\}$. In questo caso:

$$\sum_{x \in \mathcal{X}} x = \sum_{i=0}^{M-1} i = \frac{M(M-1)}{2} \Rightarrow \mathbb{E}[X] = \frac{M-1}{2}$$

---

## Pagina 53

La variabile Poissoniana

Una variabile aleatoria $X$ si dice Poissoniana di parametro $\lambda$ (in breve, $X \sim \mathcal{P}(\lambda)$) se:

- Il suo alfabeto è $\mathcal{X} = \{0, 1, 2, \ldots\} = \mathbb{N}_0$;
- La sua pmf è data da:

$$p_X(k) = \mathbb{P}(X = k) = \frac{\lambda^k}{k!} e^{-\lambda}, \quad k \in \mathbb{N}_0$$

Si noti che la precedente soddisfa le condizioni per poter essere una pmf, in quanto:

$$p_K(k) \geq 0 \quad \sum_{x \in \mathcal{X}} p_X(x) = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} = 1$$

La sua media vale

$$\mathbb{E}[X] = \sum_{x \in \mathcal{X}} xp_X(x) = e^{-\lambda} \sum_{k=1}^{\infty} k \frac{\lambda^k}{k!} = \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!} = \lambda$$

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statistici per l Informazione - Marco Lops  52 / 161

---

## Pagina 54

Introduciamo l’argomento con un esercizio.

- Supponiamo che $X \sim \mathcal{B}(16, \frac{1}{3})$, cioè:

$$\mathcal{X} = \{0, 1, \ldots, 16\} \quad p_X(k) = \binom{16}{k} \left(\frac{1}{3}\right)^k \left(\frac{2}{3}\right)^{16-k} \quad \mathbb{E}[X] = \frac{16}{3}$$

- Supponiamo ora di assumere che sia verificata la condizione $X > 4$: ci chiediamo come si distribuisca $X$ sotto questa condizione.

- Dal punto di vista fisico significa considerare un insieme di $n$ esperimenti, scartare i valori di $X$ che siano inferiore a 5 e valutare le probabilità dei residui dodici valori sul campione così ridotto.

- Possiamo quindi calcolare:

$$p_{X|X>4}(k) = \mathbb{P}(X = k|X > 4) = \frac{\mathbb{P}(\{X = k\} \cap \{X > 4\})}{\mathbb{P}(\{X > 4\})} = \left\{ \begin{array}{ll} \frac{p_X(k)}{\mathbb{P}(\{X > 4\})} = \frac{p_X(k)}{\sum_{i=5}^{16} p_X(i)} & k \in \{5, \ldots, 16\} \\ 0 & k < 5 \end{array} \right.$$

---

## Pagina 55

Pmf e medie condizionali

- Si noti che la pmf condizionale trovata è una pmf. Infatti:
  $$p_{X|X>4}(k) \geq 0 \quad \text{e} \quad \sum_{k \in \mathbb{Z}} p_{X|X>4}(k) = \sum_{k=5}^{16} \frac{p_X(k)}{\sum_{i=5}^{16} p_X(i)} = 1$$
- Siamo quindi ora in grado di definire la pmf di una variabile aleatoria qualsiasi $X$ condizionata a un qualsiasi evento $A \subseteq \Omega$ a probabilità non nulla nella forma:
  $$p_{X|A}(x) = \mathbb{P}(x|A) = \frac{\mathbb{P}(\{X=x\} \cap A)}{\mathbb{P}(A)} \quad x \in \mathcal{X}$$
- Ovviamente, $p_{X|A}(x)$ al variare di $x$ in $\mathcal{X}$ con $A$ prefissato è una pmf;
- Nella prossima slide si mostrano gli andamenti delle pmf condizionali di $X \sim \mathcal{B}(16, \frac{1}{3})$ condizionate all’evento $A = \{X > 4\}$ e $B = \{2 \leq X \leq 6\}$.

---

## Pagina 56

Andamenti delle pmf e pmf condizionali

Un diverso approccio alla probabilità
Variabili Aleatorie Discrete
Variabili Aleatorie Discrete Doppie
Variabili Aleatorie Discrete Doppie

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statistici per l’Informazione - Marco Lops  55 / 161

---

## Pagina 57

Regola della probabilità totale per le pmf

Ricordiamo che (vedi slide 37), per un qualunque evento $C \subseteq \Omega$ e per una qualunque partizione $\{E\}_{i=1}^{M}$ si ha:

$$\mathbb{P}(C) = \sum_{i=1}^{M} \mathbb{P}(C | E_i) \mathbb{P}(E_i)$$

Pertanto, specializzando la precedente a $C = \{X = x\}$ si ha:

$$\mathbb{P}(X = x) = p_X(x) = \sum_{m=1}^{M} \mathbb{P}(\{X = x\} | E_m) \mathbb{P}(E_m) = \sum_{m=1}^{M} p_X|E_m(x) \mathbb{P}(E_m)$$

Con riferimento all’esempio precedente, quindi:

$$p_X(k) = p_X|X > 4(k) \mathbb{P}(X > 4) + p_X|X \leq 4(k) \mathbb{P}(X \leq 4) =$$

$$p_X|2 \leq X \leq 6(k) \mathbb{P}(2 \leq X \leq 6) + p_X|X \leq 1(k) \mathbb{P}(X \leq 1) + p_X|X \geq 7(k) \mathbb{P}(X \geq 7)$$

essendo

- $\Omega = E_1 \cup E_2 = \{X > 4\} \cup \{X \leq 4\}, E_1 \cap E_2 = \emptyset$;
- $\Omega = E_1' \cup E_2' \cup E_3' = \{2 \leq X \leq 6\} \cup \{X \leq 1\} \cup \{X \geq 7\}, E_1' \cap E_2' = \emptyset \text{ for } i \neq j.$

---

## Pagina 58

Un analogo sviluppo è possibile sulle medie. Infatti:

$$\mathbb{E}[X] = \sum_{x \in \mathcal{X}} xp_X(x) = \sum_{m=1}^{M} p_{X|E_m}(x)\mathbb{P}(E_m) =$$

$$\sum_{m=1}^{M} \mathbb{P}(E_m) \sum_{x \in \mathcal{X}} xp_X|E_m(x)$$

dove quindi si è definita la media condizionata

$$\mathbb{E}[X|E_m] = \sum_{x \in \mathcal{X}} xp_X|E_m(x)$$

Si applicchi questa formula agli esempi precedenti per ritrovare che, se $X \sim \mathcal{B}(16, p)$:

$$\mathbb{E}[X] = \mathbb{P}(X \leq 4)\mathbb{E}[X|X \leq 4] + \mathbb{P}(X > 4)\mathbb{E}[X|X > 4] =$$

$$\mathbb{P}(X \in \{2, 3, 4, 5, 6\})\mathbb{E}[X|X \in \{2, 3, 4, 5, 6\}] + \mathbb{P}(X \notin \{2, 3, 4, 5, 6\})\mathbb{E}[X|X \notin \{2, 3, 4, 5, 6\}]$$

---

## Pagina 59

Funzioni di variabili aleatorie -1

- Si assuma che $X = X(\omega)$ sia una variabile aleatoria con alfabeto $\mathcal{X}$ con pmf $\{p_X(x)\}_{x \in \mathcal{X}}$;
- Sia $g(\cdot)$ una funzione il cui insieme di definizione includa i punti di $\mathcal{X}$;
- Si forma la nuova variabile aleatoria:

$$Y = g(X) = g[X(\omega)] \in \mathcal{Y} \quad \text{dove} \quad Y = g(\mathcal{X})$$

Problema: Ricavare una caratterizzazione di $Y$ dalla caratterizzazione di $X$ in termini di

- pmf, $p_Y(y)$, $y \in \mathcal{Y}$;
- media statistica, $\mathbb{E}[Y] = \sum_{y \in \mathcal{Y}} yp_Y(y).$

---

## Pagina 60

Funzioni di variabili aleatorie -2

Distinguiamo due casi:

a $\{g(x)\}_{x \in \mathcal{X}}$ biunivoca, cioè:

$$|Y| = |X| \Leftrightarrow \forall y \in \mathcal{Y} \text{ è definita} \quad x = g^{-1}(y)$$

b $\{g(x)\}_{x \in \mathcal{X}}$ univoca, cioè associa a più valori di $\mathcal{X}$ un solo valore di $\mathcal{Y}$:

$$\mathcal{X} = \{x_1, \ldots, x_n\} \quad \mathcal{Y} = \{y_1, \ldots, y_m\} \quad n > m$$

- Nel caso [a] si tratta solo di una ridenominazione dell’alfabeto:

$$p_Y(y_i) = \mathbb{P}(Y = g(x_i)) = \mathbb{P}(X = g^{-1}(y_i)) = \mathbb{P}(X = x_i) = p_X(x_i)$$

- Nel caso [b] vale la precedente relazione per tutti i punti di $\mathcal{Y}$ in cui $g(y)$ è invertibile. Per un punto $y_k$ tale che $g(x_1^{(k)}) = g(x_2^{(k)}) = \ldots = g(x_L^{(k)}) = y_k$ avremo:

$$p_Y(y_k) = \mathbb{P}\left(\bigcup_{i=1}^{L_k} \{X = x_i^{(k)}\}\right) = \sum_{i=1}^{L_k} \mathbb{P}\left(X = x_i^{(k)}\right) = \sum_{i=1}^{L_k} p_X(x_i^{(k)})$$

---

## Pagina 61

Cominciamo con il seguire la stessa suddivisione introdotta per il caso delle pmf.

- Funzioni biunivoche - In questo caso c’è solo una ridenominazione dell’alfabeto, per cui:
  $$\mathbb{E}[Y] = \sum_{y \in \mathcal{Y}} yp_Y(y) = \mathbb{E}[g(X)] = \sum_{x \in \mathcal{X}} g(x)p_X(x)$$  (1)

- Funzioni univoche - Avremo in questo caso:
  $$\mathbb{E}[Y] = \sum_{y \in \mathcal{Y}} yp_Y(y) = \sum_{y \in \mathcal{Y}} \sum_{x;y=g(x)} g(x)p_X(x)$$  (2)

- Si noti comunque che l’equazione (1) include l’equazione (2) come caso speciale. In conclusione adottiamo la forma generale (1) che prende anche il nome di Teorema fondamentale per il calcolo della media

---

## Pagina 62

Qualche esempio

- Sia $X \sim \mathcal{U}(\{-2, -1, 0, 2\})$;
- Si trovi la pmf delle variabili aleatorie:

$$Y_1 = X^2 \left( Y = g(X), g(x) = x^2 \right) \text{ e } Y_2 = 3 \sin \left( \frac{2\pi}{5} X \right) \left( Y = g(X), g(x) = \sin \left( \frac{2\pi}{5} x \right) \right)$$

$$Y_1 \text{ Avremo } \mathcal{Y}_1 = \{0, 1, 4\}, |\mathcal{Y}_1| = |\{0, 1, 4\}| = 3 < |\mathcal{X}| = 4, \text{ per cui:}$$

$$p_{Y_1}(0) = \mathbb{P}(X = 0) = \frac{1}{4} = p_{Y_1}(1) = \mathbb{P}(X = 1) = \frac{1}{4}$$

$$p_{Y_1}(2) = \mathbb{P}(\{X = -2\} \cup \{X = 2\}) = \mathbb{P}(X = -2) + \mathbb{P}(X = 2) = \frac{1}{2}$$

$$Y_2 \mathcal{Y}_2 = \left\{ \begin{array}{c} -3 \sin \left( \frac{2\pi}{5} \right), -3 \sin \left( \frac{4\pi}{5} \right), 0, 3 \sin \left( \frac{4\pi}{5} \right) \end{array} \right\},$$

$$|\mathcal{Y}_2| = 4 = |\mathcal{X}|:$$

$$p_{Y_2}(-0.95) = p_{Y_2}(\pm 0.58) = p_{Y_2}(0) = \frac{1}{4} \Rightarrow Y_2 \sim \mathcal{U}(\mathcal{Y}_2)$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per I Informazione - Marco Lops 61 / 161

---

## Pagina 63

Valore quadratico medio e varianza di una variabile aleatoria

Data una variabile aleatoria $X \sim p_X(x)$, $x \in \mathcal{X}$, con media $\mu_X = \mathbb{E}[X]$ definiamo:

- Il valore quadratico medio (Mean Square) di $X$:
  $$X^2_{\text{rms}} = \mathbb{E}[X^2] = \sum_{x \in \mathcal{X}} x^2 p_X(x)$$

- Il valore efficace (root mean square, rms) di $X$:
  $$X_{\text{rms}} = \sqrt{\mathbb{E}[X^2]} = \sqrt{\sum_{x \in \mathcal{X}} x^2 p_X(x)}$$

- La varianza di $X$:
  $$\sigma^2_X = \mathbb{E}[(X - \mu_X)^2] = \sum_{x \in \mathcal{X}} (x^2 + \mu_X^2 - 2x\mu_X)p_X(x) = X^2_{\text{rms}} - \mu_X^2$$

- La deviazione standard di $X$:
  $$\sigma_X = \sqrt{\sigma^2_X} = \sqrt{\mathbb{E}[X^2] - \mu_X^2} = X^2_{\text{rms}} - \mu_X^2$$

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops  Metodi Statistici per Il Informazione - Marco Lops 62 / 161

---

## Pagina 64

Esempio # 1: $X \sim \mathcal{B}(N, p)$.

Si noti che, per $N = 1$, abbiamo:

$$\mathbb{E}[X] = p, \quad \mathbb{E}[X^2] = 1 \times p + 0 \times (1 - p) = p, \quad \sigma_X^2 = p - p^2 = p(1 - p), \quad \sigma_X = \sqrt{p(1 - p)}$$

In generale:

$$\sum_{x \in \mathcal{X}} x^2 p_X(x)$$
$$\mathbb{E}[X^2] = \sum_{k=0}^{N} k^2 \binom{N}{k} p^k (1 - p)^{N-k} = \sum_{k=1}^{N} k \frac{N!}{(k-1)!(N-k)!} p^k q^{N-k}$$

$$= Np \left[ \frac{d}{dp} \sum_{k=1}^{N} \frac{(N-1)!}{(k-1)!(N-k)!} p^k q^{N-k} \right]_{q=1-p} = Np(1 - p) + \overbrace{N^2 p^2}^{\mu_X^2}$$

per cui:

$$X_{\text{rms}}^2 = Np(1 - p) + N^2 p^2 \quad \sigma_X^2 = Np(1 - p) \quad X_{\text{rms}} = \sqrt{Np(1 - p) + N^2 p^2} \quad \sigma_X = \sqrt{Np(1 - p)}$$

---

## Pagina 65

Esempio #2: variabile uniforme

Sia $X \sim \mathcal{U}(\{0, \ldots, M-1\})$, per cui $\mu_X = \mathbb{E}[X] = \frac{M-1}{2}$. Il valore MS si scrive:

$$X^2_{\text{rms}} = \frac{1}{M} \sum_{k=1}^{M-1} k^2 = \frac{(M-1)(2M-1)}{6}$$

dove si è sfruttato il fatto che:

$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$$

Avremo quindi:

$$\sigma_X^2 = \frac{M(2M-1)}{6} - \frac{(M-1)^2}{4} = \frac{M^2-1}{12}$$

$$X_{\text{rms}} = \sqrt{\frac{M(2M-1)}{6}} \quad \sigma_X = \sqrt{\frac{M^2-1}{12}}$$

---

## Pagina 66

Esempio #3: variabile di Poisson

Sia $X \sim \mathcal{P}(\lambda)$, per cui $\mu_X = \mathbb{E}[X] = \lambda$. Il valore MS si scrive:

$$X^2_{\text{rms}} = e^{-\lambda} \sum_{k=1}^{\infty} k^2 \frac{\lambda^k}{k!} = e^{-\lambda} \sum_{k=1}^{\infty} k \frac{\lambda^k}{(k-1)!} = \lambda e^{-\lambda} \frac{d}{d\lambda} \left[ \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!} \right] = \lambda e^{-\lambda} \frac{d}{d\lambda} \left[ \lambda e^{\lambda} \right] = \lambda e^{-\lambda} \left[ e^{\lambda} + \lambda e^{\lambda} \right] = \lambda + \lambda^2$$

Quindi:

$$\sigma_X^2 = \lambda \quad X_{\text{rms}} = \sqrt{\lambda + \lambda^2} \quad \sigma_X = \sqrt{\lambda}$$

Si noti che per una poissoniana la media e la varianza coincidono!

---

## Pagina 67

Il significato della varianza e della deviazione standard.

- Supponiamo di non avere una caratterizzazione completa di una variabile aleatoria $X$;
- Se $\mathcal{X} \subseteq [0, +\infty]$ (cioè la variabile è non negativa) la media $\mu_X$ ci dà un’idea del suo comportamento, anche se imprecisa;
- Se invece $X$ può assumere sia valori positivi che negativi, la media non è un indicatore significativo che possa dare informazioni sul comportamento della variabile aleatoria;
- In entrambi i casi è comunque importante sapere quanto probabile sia osservare valori di $X$ più o meno lontani dalla sua media;
- Questo - nel caso si conosca la coppia $(\mu_X, \sigma_X)$ - può avvenire in virtù della Disuguaglianza di Chebyshev:

$$\mathbb{P}\{|X - \mu_X| > k\sigma_X\} = \mathbb{P}\{\mu_X - k\sigma_X \leq X \leq \mu_X + k\sigma_X\} \geq 1 - \frac{1}{k^2}$$

- Si capisce quindi che un parametro fondamentale è il rapporto $\frac{\mu_X}{\sigma_X}$: valori elevati di questo rapporto indicano una pmf molto concentrata intorno alla media (cioè una variabile "poco aleatoria"), mentre valori bassi implicano un’elevata aleatorietà.

---

## Pagina 68

La disuguaglianza di Chebyshev

- Sia $Z$ una variabile non negativa definita su un alfabeto discreto $Z \subseteq [0, +\infty[$ secondo una pmf $p_Z(z)$;
- Si valuti la probabilità che $Z$ sia non inferiore a un qualunque valore $\delta \in Z$:

$$\mathbb{P}(Z \geq \delta) = \sum_{z:z \geq \delta} p_Z(z) \leq \sum_{z:z \geq \delta} \left(\frac{z}{\delta}\right)^2 p_Z(z) \leq \sum_{z \in \mathbb{Z}} \left(\frac{z}{\delta}\right)^2 p_Z(z) \stackrel{c}{=} \frac{\mathbb{E}[Z^2]}{\delta^2}$$

(3)

- a Deriva dall’essere $\left(\frac{z}{\delta}\right)^2 \geq 1$ per $z \geq \delta$;
- b Deriva dal fatto che estendendo la sommatoria su tutto $Z$ si aggiungono termini non negativi;
- c Deriva dalla definizione di valore quadraticico medio.

- La disuguaglianza di Chebyshev si ricava quindi ponendo $Z = |X - \mu_X| \geq 0$ e $\delta = k\sigma_X$ nella (3), nonchè notando che con questa scelta $\mathbb{E}[Z^2] = \mathbb{E}[|X - \mu_X|^2] = \mathbb{E}[(X - \mu_X)^2] = \sigma_X^2$.

---

## Pagina 69

Quadro sintetico delle proprietà di media e varianza

- Se $(a, b)$ sono costanti reali $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$, visto che $\mathbb{E}[b] = b$;
- Se $X(\omega) \geq 0$ $\forall \omega \in \Omega$ (cioè, se $\mathcal{X} \subseteq [0, +\infty]$), allora $\mathbb{E}[X] \geq 0$;
- $\sigma_X^2 \geq 0$ (in quanto media della variabile non negativa $(X - \mu_X)^2)$;
- Se $Y = aX + b$, allora $\sigma_Y^2 = a^2\sigma_X^2$. Infatti:

$$\mu_Y = a\mu_X + b, \quad \mathbb{E}[Y^2] = \mathbb{E}[a^2X^2 + 2abX + b^2] = a^2\mathbb{E}[X^2] + 2ab\mathbb{E}[X] + b^2$$

$$\sigma_Y^2 = a^2\mathbb{E}[X^2] + 2ab\mu_X + b^2 - (a\mu_X + b)^2 = a^2\sigma_X^2$$

- Come conseguenza delle precedenti relazioni si ha anche:

$$\mathbb{E}[Y^2] = Y_{\text{rms}}^2 = a^2X_{\text{rms}}^2 + 2ab\mu_X + b^2$$

- Si noti infine che per variabili a media nulla $(\mu_X = 0)$, abbiamo $\sigma_X^2 = X_{\text{rms}}^2$.

---

## Pagina 70

Definizione di variabili multiple

Formalmente, una copbia di variabili aleatorie (o variabile doppia) è definita - in analogia con quelle singole - nella forma:

$$X, Y : \omega \in \Omega \rightarrow (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y} \subseteq \mathbb{R}^2$$

dove $\mathcal{X}$ e $\mathcal{Y}$ sono gli alfabeti di $X$ e di $Y$ rispettivamente.

In altre parole, il risultato di un esperimento $\omega_*$ non è un unico valore $X(\omega_*) = x_* \in \mathcal{X}$, ma una copbia ordinata $(X(\omega_*), Y(\omega_*)) = (x_*, y_*)$, che quindi varia nel prodotto cartesiano $\mathcal{X} \times \mathcal{Y}$. Per esempio:

- Si consideri un elenco di tutti i residenti in Italia a una certa data, corredato di dati quali altezza $(X)$, peso $(Y)$, età $(Z)$;
- Si scelga un residente a caso e se ne leggano l'altezza $X(\omega) \in \{30 \text{ cm}, 31 \text{ cm}, \dots, 210 \text{ cm}\}$, il peso $Y(\omega) \in \{0.5 \text{ kg}, 0.6 \text{ kg}, \dots, 170 \text{ kg}\}$, l'età $Z(\omega) \in \{0 \text{ anni}, 0.5 \text{ anni}, \dots, 110 \text{ anni}\}$.
- Possibili coppie sono

$$(X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y}, \quad (X(\omega), Z(\omega)) \in \mathcal{X} \times \mathcal{Z}, \quad (Y(\omega), Z(\omega)) \in \mathcal{Y} \times \mathcal{Z}$$

$$(X(\omega), Y(\omega), Z(\omega)) \in \mathcal{X} \times \mathcal{Y} \times \mathcal{Z}$$ è una terna di variabili aleatorie.

---

## Pagina 71

<p>pmf/DF/pdf congiunta</p>

- Si supponga di considerare la coppia $(X, Y)$ (nel caso precedente, altezza e peso di un residente scelto a caso);
- Si eseguano $n$ experimenti (nel caso precedente, si scelga per $n$ volte a caso un nome dell’elenco);
- Si registrino i relativi valori di $\{(X(\omega_i), Y(\omega_i))\}_{i=1}^n$ (nel caso precedente, altezza e peso del residente di volta in volta scelto);
- Si indichi con $n_{X=x, Y=y} = n_{X=x, Y=y}(n)$ il numero di volte in cui $X = x$ e $Y = y$ (nel caso precedente, il numero di volte in cui l’utente scelto a caso ha una altezza $x$ e un peso $y$);
- Ovviamente, l’evento $\{X = x\} \cap \{Y = y\}$ occorre $n_{X=x, Y=y}$ volte su $n$ experimenti. Definiamo allora la seguente pmf/DF/pdf congiunta delle due variabili aleatorie $X$ e $Y$:

$$p_{X,Y}(x,y) = \mathbb{P}\{(X = x) \cap \{Y = y\}\} = \lim_{n \to \infty} \frac{n_{X=x, Y=y}}{n}, \quad (x,y) \in \mathcal{X} \times \mathcal{Y}$$

- In altre parole, $p_{X,Y}(x,y)$ è una tabella di $|\mathcal{X}||\mathcal{Y}|$ numeri che - ovviamente - gode di opportune proprietà.

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l’Informazione - Marco Lops 70 / 161

---

## Pagina 72

Proprietà della pmf congiunta

- $p_{X,Y} \geq 0$ e $\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p_{X,Y}(x,y) = 1$. Infatti:
  $$1 = \mathbb{P}(\Omega) = \mathbb{P}\left(\bigcup_{x \in \mathcal{X}} \bigcup_{y \in \mathcal{Y}} \{X = x, Y = y\}\right) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} \mathbb{P}\left(\{X = x, Y = y\}\right)$$
  essendo l’evento elementare $\{X = x, Y = y\}$ incompatibile con ogni altro evento elementare $\{X = x', Y = y'\}$ con $x \neq x'$ e $y \neq y'$.

- Si noti che $\bigcup_{x \in \mathcal{X}} \{X = x\} = \Omega$ e $\bigcup_{y \in \mathcal{Y}} = \Omega$, per cui:
  $$\{X = x\} = \{X = x\} \cap \Omega = \{X = x\} \cap \bigcup_{y \in \mathcal{Y}} \{Y = y\} = \bigcup_{y \in \mathcal{Y}} \{X = x\} \cap \{Y = y\}$$
  $$\implies \mathbb{P}\left(\{X = x\}\right) = \mathbb{P}\left(\bigcup_{y \in \mathcal{Y}} \{X = x\} \cap \{Y = y\}\right) = \sum_{y \in \mathcal{Y}} \mathbb{P}\left(\{X = x\} \cap \{Y = y\}\right)$$

- Si ha quindi la proprietà di marginalizzazione:
  $$\sum_{y \in \mathcal{Y}} p_{X,Y}(x,y) = p_{X}(x) \quad \sum_{x \in \mathcal{X}} p_{X,Y}(x,y) = p_{Y}(y)$$
  per cui caratterizzare congiuntamente $(X,Y)$ significa anche caratterizzare marginalmente, mentre il viceversa non è necessariamente vero.

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l’Informazione - Marco Lops 71 / 161

---

## Pagina 73

Variabili indipendenti

- Due variabili aleatorie $X \in \mathcal{X}$ e $Y \in \mathcal{Y}$ sono indipendenti se (e solo se) gli eventi $\{X = x\}$ e $\{Y = y\}$ sono indipendenti;
- Per due variabili indipendenti la pmf congiunta si fattorizza nel prodotto delle marginali:
  $$p_{X,Y}(x,y) = \mathbb{P}(\{X = x\} \cap \{Y = y\}) = \mathbb{P}(\{X = x\}) \mathbb{P}(\{Y = y\}) = p_{X}(x)p_{Y}(y)$$
- Questo è l’unico caso in cui assegnare le due pmf marginali, $p_{X}(x)$ e $p_{Y}(y)$, equivale ad assegnare la pmf congiunta.
- Siccome il concetto di pmf congiunta si generalizza a una $m$-pla di variabili aleatorie $(X_1, \ldots, X_m) \in \mathcal{X}_1 \times \ldots \times \mathcal{X}_m \subseteq \mathbb{R}^m$ mediante la pmf congiunta:
  $$p_{X_1, \ldots, X_m}(x_1, \ldots, x_m) = \mathbb{P}(\{X_1 = x_1\}, \ldots, \{X_m = x_m\})$$
così si generalizza il concetto di indipendenza:
  $$p_{X_1, \ldots, X_m}(x_1, \ldots, x_m) = \mathbb{P}(\{X_1 = x_1\}, \ldots, \{X_m = x_m\}) = \prod_{i=1}^{m} \mathbb{P}(\{X_i = x_i\}) = \prod_{i=1}^{m} p_{X_i}(x_i)$$

---

## Pagina 74

Le pmf condizionate

- Si considerino varibili aleatori $X \in \mathcal{X}$ e $Y \in \mathcal{Y}$ con assegnata pmf congiunta $p_{X,Y}(x,y)$;
- Applichiamo all’evento $\{X = x, Y = y\} = \{X = x\} \cap \{Y = y\}$ la legge della probabilità composta (vedi slide 36):

$$p_{X,Y}(x,y) = \mathbb{P}\left(\{X = x\} \cap \{Y = y\}\right) = \frac{p_{Y|X}(y|x)}{\mathbb{P}\left(\{Y = y\}\mid \{X = x\}\right)} \frac{p_{X}(x)}{\mathbb{P}\left(\{X = x\}\right)}$$

- $p_{Y|X}(y|x)$ è la legge di probabilità condizionata (o pmf condizionata) di $Y$ dato $X$;
- Come la legge congiunta, $p_{Y|X}(y|x)$ è una tabella di $|\mathcal{X}||\mathcal{Y}|$ numeri che soddisfa alcune proprietà;
- Ovviamente, abbiamo:

$$p_{Y|X}(y|x)p_{X}(x) = p_{X|Y}(x|y)p_{Y}(y) \implies$$

$$p_{X|Y}(x|y) = \frac{p_{Y|X}(y|x)p_{X}(x)}{p_{Y}(y)}$$

(Legge di Bayes)

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l’Informazione - Marco Lops 73 / 161

---

## Pagina 75

Alcune proprietà delle pmf condizionate

- $p_{Y|X}(y|x)$ se $x$ resta fisso e $y$ varia in $Y$ è una legge di probabilità. Infatti:

$$p_{Y|X}(y|x) \geq 0 \quad \sum_{y \in Y} p_{Y|X}(y|x) = \mathbb{P}\left(\cup_{y \in Y} \{Y = y\} \mid \{X = x\}\right) = \mathbb{P}(\Omega \mid \{X = x\}) = 1$$

- La proprietà di marginalizzazione della pmf congiunta (vedi slide 71) si scrive in termini di pmf condizionali nella forma:

$$p_X(x) = \sum_{y \in Y} p_X,Y(x,y) = \sum_{y \in Y} p_X|Y(x|y)p_Y(y)$$

$$p_Y(y) = \sum_{x \in X} p_X,Y(x,y) = \sum_{x \in X} p_Y|Y(x|y)p_X(x)$$

Si noti che questa non è altro che la legge della probabilità totale (vedi slide 37) scritta, per la prima equazione, per l'evento $\{X = x\}$ rispetto alla partizione $\Omega = \cup_{y \in Y} \{Y = y\}$ e, per la seconda equazione, per l'evento $\{Y = y\}$ rispetto alla partizione $\Omega = \cup_{x \in X} \{X = x\}$.

- Si noti, infine, che se $X$ e $Y$ sono indipendenti:

$$p_{Y|X}(y|x) = p_Y(y) \quad p_{X|Y}(x|y) = p_X(x)$$

---

## Pagina 76

Generalizzando…

• Si consideri una terna di variabili aleatorie $(X, Y, Z)$, distribuite secondo $p_{X, Y, Z}(x, y, z)$, $(x, y, z) \in \mathcal{X} \times \mathcal{Y} \times \mathcal{Z}$.

• Usando consecutivamente la legge della probabilità composta, otteniamo:

$$\mathbb{P}(X = x, Y = y, Z = z) = \mathbb{P}(X = x, Y = y|Z = z) \mathbb{P}(Z = z) =$$

$$\mathbb{P}(X = x|Z = z, Y = y) \mathbb{P}(Y = y|Z = z) \mathbb{P}(Z = z)$$

che ci introduce alla "regola della catena" (ogni permutazione dei pedici e degli argomenti è ovviamente possibile):

$$p_{X|Y, Z}(x|y, z) = \frac{p_{X, Y|Z}(x, y|z)}{p_{Y|Z}(y|z)} \rightarrow p_{X, Y, Z}(x, y, z) = p_{Z}(z)p_{Y|Z}(y|z)p_{X|Y, Z}(x|y, z)$$

• La terna è dunque indipendente se e e solo se $p_{X|Y, Z}(x|y, z) = p_{X}(x)$, $p_{Y|X, Z}(y|x, z) = p_{Y}(y)$ e $p_{Z|X, Y}(z|x, y) = p_{Z}(z)$.

---

## Pagina 77

Esempio: Emissione di 3 bit da una sorgente binaria

- Si consideri una sorgente binaria che emetta tre bit, siano essi $(B_1, B_2, B_3)$, $B_i \in \{0, 1\}$;
- Si assegnano le due leggi congiunte $p_{B_1, B_2, B_3}(b_1, b_2, b_3)$ e $q_{B_1, B_2, B_3}(b_1, b_2, b_3)$ della tabella $(0 < \alpha < 1)$;
- Dire se $(B_1, B_2), (B_1, B_3), (B_2, B_3), (B_1, B_2, B_3)$ sono o meno indipendenti secondo $p_{B_1, B_2, B_3}(b_1, b_2, b_3)/q_{B_1, B_2, B_3}(b_1, b_2, b_3)$.

| $(b_1, b_2, b_3)$ | $p_{B_1, B_2, B_3}(b_1, b_2, b_3)$ | $q_{B_1, B_2, B_3}(b_1, b_2, b_3)$ |
| :--- | :--- | :--- |
| 000 | $(1 - \alpha)^3$ | $(1 - \alpha)^2$ |
| 001 | $\alpha(1 - \alpha)^2$ | 0 |
| 010 | $\alpha(1 - \alpha)^2$ | 0 |
| 011 | $\alpha^2(1 - \alpha)$ | $\alpha(1 - \alpha)$ |
| 100 | $\alpha(1 - \alpha)^2$ | 0 |
| 101 | $\alpha^2(1 - \alpha)$ | $\alpha(1 - \alpha)$ |
| 110 | $\alpha^2(1 - \alpha)$ | $\alpha^2$ |
| 111 | $\alpha^3$ | 0 |

---

## Pagina 78

Marginalizzazione di $p_{B1, B2, B3}(b_1, b_2, b_3)$

- Cominciamo con il trovare la congiunta di tutte le possibili coppie secondo $p_{B1, B2, B3}(b_1, b_2, b_3)$. Ricordiamo la proprietà di marginalizzazione:

$$p_{B1, B2}(b_1, b_2) = p_{B1, B2, B3}(b_1, b_2, 0) + p_{B1, B2, B3}(b_1, b_2, 1)$$ e analoghe

otteniamo le congiunte:

| $(b_1, b_2)$ | $p_{B1, B2}(b_1, b_2)$ |
| :--- | :--- |
| $00$ | $(1 - \alpha)^2$ |
| $01$ | $\alpha(1 - \alpha)$ |
| $10$ | $\alpha(1 - \alpha)$ |
| $11$ | $\alpha^2$ |

| $(b_1, b_3)$ | $p_{B1, B3}(b_1, b_3)$ |
| :--- | :--- |
| $00$ | $(1 - \alpha)^2$ |
| $01$ | $\alpha(1 - \alpha)$ |
| $10$ | $\alpha(1 - \alpha)$ |
| $11$ | $\alpha^2$ |

| $(b_2, b_3)$ | $p_{B2, B3}(b_2, b_3)$ |
| :--- | :--- |
| $00$ | $(1 - \alpha)^2$ |
| $01$ | $\alpha(1 - \alpha)$ |
| $10$ | $\alpha(1 - \alpha)^2$ |
| $11$ | $\alpha^2$ |

- Con un'ulteriore marginalizzazione:

$$p_{B1}(b_1) = p_{B1, B2}(b_1, 0) + p_{B1, B2}(b_1, 1)$$ e analoghe

| $b_1$ | $p_{B1}(b_1)$ |
| :--- | :--- |
| 0 | $(1 - \alpha)$ |
| 1 | $\alpha$ |

| $b_2$ | $p_{B2}(b_2)$ |
| :--- | :--- |
| 0 | $(1 - \alpha)$ |
| 1 | $\alpha$ |

| $b_3$ | $p_{B3}(b_3)$ |
| :--- | :--- |
| 0 | $(1 - \alpha)$ |
| 1 | $\alpha$ |

---

## Pagina 79

Marginalizzazione di $q_{B_1,B_2,B_3}(b_1,b_2,b_3)$

- Procedendo nello stesso modo otteniamo le congiunte:
  $$\begin{array}{c c c c}
    (b_1,b_2) & q_{B_1,B_2}(b_1,b_2) \\
    00 & (1-\alpha)^2 \\
    01 & \alpha(1-\alpha) \\
    10 & \alpha(1-\alpha) \\
    11 & \alpha^2
  \end{array}$$

- E le marginali:
  $$\begin{array}{c c c c}
    b_1 & q_{B_1}(b_1) \\
    0 & (1-\alpha) \\
    1 & \alpha
  \end{array}$$

  $$\begin{array}{c c c c}
    b_2 & q_{B_2}(b_2) \\
    0 & (1-\alpha) \\
    1 & \alpha
  \end{array}$$

  $$\begin{array}{c c c c}
    b_3 & q_{B_3}(b_3) \\
    0 & (1-\alpha) \\
    1 & \alpha
  \end{array}$$

Come mai alcune delle congiunte a coppie e le marginali coincidono, ma le pmf delle terne sono diverse.

Qual è il mistero?

---

## Pagina 80

Soluzione

Si vede facilmente che, per quanto riguarda $p_{B_1,B_2,B_3}(b_1,b_2,b_3)$, abbiamo:

$$p_{B_1,B_2,B_3}(b_1,b_2,b_3) = \prod p_{B_i}(b_i) \Rightarrow p_{B_m,B_k}(b_m,b_k) = p_{B_m}(b_m)p_{B_k}(b_k) \forall m \neq k$$

quindi $p_{B_1,B_2,B_3}(b_1,b_2,b_3)$ implica l'indipendenza statistica della intera terna.

Viceversa, per $q_{B_1,B_2,B_3}(b_1,b_2,b_3)$ si ha:

$$q_{B_m,B_k}(b_m,b_k) = q_{B_m}(b_m)q_{B_k}(b_k) \ m = 1, \ k = 2 \quad q_{B_1,B_2,B_3}(b_1,b_2,b_3) \neq \prod q_{B_i}(b_i)$$

quindi le variabili $B_1, B_2$ sono indipendenti, ma non lo è la terna, nè lo sono $B_1, B_3$ o $B_2, B_3$. Infatti, per esempio:

$$p_{B_3=1}|B_1=1,B_2=1 = \frac{p_{B_1,B_2,B_3}(1,1,1)}{p_{B_1,B_2}(1,1)} = \frac{\alpha^3}{\alpha^2} = \alpha = p_{B_3}(1)$$

$$q_{B_3=1}|B_1=1,B_2=1 = \frac{q_{B_1,B_2,B_3}(1,1,1)}{q_{B_1,B_2}(1,1)} = 0 \neq q_{B_3}(1)$$

Si vede facilmente che $B_3 = B_1 \oplus B_2$ è un bit di parità.

---

## Pagina 81

Funzioni di variabili doppie

- Sia $(X, Y) \sim p_{X, Y}(x, y)(x, y) \in \mathcal{X} \times \mathcal{Y}$ una variabile doppia con pmf $p_{X, Y}(x, y)$;
- Sia $g(x, y)$ una funzione di due variabili il cui dominio di esistenza includa $\mathcal{X} \times \mathcal{Y}$;
- Si vuole caratterizzare $Z = g(X, Y)$ in termini di pmf e media statistica.

a. Si determini l’alfabeto $\mathcal{Z}$. Se $|Z| = |\mathcal{X}||\mathcal{Y}|$, allora - seguendo il ragionamento della slide 59 - avremo che esiste un unico punto $(x(z), y(z)) : z = g(x, y)$, per cui:

$$\mathbb{P}(Z = z) = p_Z(z) = p_{X, Y}[x(z), y(z)]$$

b. Se $|Z| < |\mathcal{X}||\mathcal{Y}|$, verrà la precedente per i punti in cui l’inversa è unica, mentre per i punti in cui l’inversa non esiste ci sarà un "collassamento delle probabilità":

$$\text{Se } g(x, y) = z \text{ per } (x, y) \in \mathcal{A}(z) \subseteq \mathcal{X} \times \mathcal{Y} \Rightarrow p_Z(z) = \sum_{x, y \in \mathcal{A}(z)} p_{X, Y}(x, y)$$

---

## Pagina 82

Un esempio

Si considerino due variabili doppie, $(X_1, Y_1) \in \{0, 1\}^2$ e $(X_2, Y_2) \in \{-1, 1\}^2$. Le pmf congiunte sono quelle riportate di seguito:

| $(x_1, y_1)$ | $p_{X_1, Y_1}(x_1, y_1)$ |
| :--- | :--- |
| 00 | $\frac{1}{2}$ |
| 01 | $\frac{1}{6}$ |
| 10 | $\frac{1}{3}$ |
| 11 | $\frac{1}{3}$ |

| $(x_2, y_2)$ | $p_{X_2, Y_2}(x_2, y_2)$ |
| :--- | :--- |
| $(-1, -1)$ | $\frac{1}{4}$ |
| $(-1, 1)$ | $\frac{1}{2}$ |
| $(1, -1)$ | $\frac{1}{6}$ |
| $(1, 1)$ | $\frac{1}{8}$ |

Si caratterizzino le due variabili aleatorie $Z_1 = 3X_1^2 + Y_1$ e $Z_2 = 3X_2^2 + Y_2$.

Si noti che $|Z_1| = |{0, 1, 3, 4}| = |{0, 1}|^2$, per cui la corrispondenza è biunivoca. Pertanto:

$$p_{Z_1}(0) = p_{X_1, Y_1}(0, 0) = \frac{1}{3} \quad p_{Z_1}(1) = p_{X_1, Y_1}(0, 1) = \frac{2}{9}$$

$$p_{Z_1}(3) = p_{X_1, Y_1}(1, 0) = \frac{1}{9} \quad p_{Z_1}(4) = p_{X_1, Y_1}(1, 1) = \frac{1}{3}$$

Viceversa, $|Z_2| = |{2, 4}| < |{0, 1}|^2$, per cui:

$$p_{Z_2}(2) = p_{X_2, Y_2}(1, -1) + p_{X_2, Y_2}(-1, -1) = \frac{3}{8}$$

$$p_{Z_2}(4) = p_{X_2, Y_2}(-1, 1) + p_{X_2, Y_2}(1, 1) = \frac{5}{8}$$

---

## Pagina 83

Media di funzioni di variabili doppie

Con riferimento alla trasformazione generica $Z = g(X, Y)$ si vede immediatamente che il Teorema Fondamentale per il calcolo della Media (vedi slide 60) si traduce in:

$$\mathbb{E}[Z] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} g(x, y)p_{X, Y}(x, y) = \sum_{(x, y) \in \mathcal{X} \times \mathcal{Y}} g(x, y)p_{X, Y}(x, y)$$

Si noti che, se $Z = aX + bY$, con $a$ e $b$ costanti deterministiche, allora:

$$\mathbb{E}[aX + bY] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (ax + by)p_{X, Y}(x, y) = a \sum_{x \in \mathcal{X}} x \sum_{y \in \mathcal{Y}} p_{X, Y}(x, y) + b \sum_{y \in \mathcal{Y}} y \sum_{x \in \mathcal{X}} p_{X, Y}(x, y) = a\mathbb{E}[X] + b\mathbb{E}[Y]$$

Più in generale, se $\{X_i\}_{i=1}^m$ sono $m$ variabili aleatori con pmf $p_{X_1}, \ldots, p_{X_m}$

$$\mathbb{E}\left[ \sum_{i=1}^m a_i X_i \right] = \sum_{i=1}^m a_i \mathbb{E}[X_i]$$

---

## Pagina 84

Teorema della media condizionata

Con riferimento a $Z = g(X, Y)$ osserviamo che:

$$\mathbb{E}[Z] = \mathbb{E}[g(X, Y)] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} g(x, y) \overbrace{p_{X|Y}(x|y)p_{Y|Y}(y)}^{p_{X|Y}(x|y)p_{Y|Y}(y)} =$$

$$\sum_{y \in \mathcal{Y}} p_{Y}(y) \sum_{x \in \mathcal{X}} g(x, y) p_{X|Y}(x|y) = \sum_{y \in \mathcal{Y}} h(y) p_{Y}(y)$$

- Nella precedente, $h(y)$ rappresenta la media di $g(X, y)$ eseguita rispetto alla pmf condizionata $p_{X|Y}(x|y)$. Cioè:

$$h(y) = \mathbb{E}[g(X, Y)|Y = y] \implies h(Y) = \mathbb{E}[g(X, Y)|Y] \implies$$

$$\mathbb{E}[g(X, Y)] = \mathbb{E}[h(Y)] = \mathbb{E}[\mathbb{E}[g(X, Y)|Y]]$$

che prende il nome di Teorema della Media Condizionata, visto che $\mathbb{E}[g(X, Y)|Y]$ è la media di $g(X, Y)$ condizionata a $Y$. Ovviamente i ruoli di $X$ e $Y$ si possono scambiare.

---

## Pagina 85

Esempio di applicazione - 1

Torniamo all’esempio della slide 81. Ovviamente avremo:

$$\mathbb{E}[Z_1] = \frac{2}{9} + \frac{3}{9} + \frac{4}{3} = \frac{17}{9} \quad \mathbb{E}[Z_2] = \frac{13}{4}$$

Il teorema della media condizionata si scrive:

$$\mathbb{E}[Z_1] = \mathbb{E}[\mathbb{E}[Z_1|Y_1]] \quad \mathbb{E}[Z_2] = \mathbb{E}[\mathbb{E}[Z_2|Y_2]]$$

per cui occorre calcolare $p_{X_1|Y_1}(x_1|y_1), p_{Y_1}(y_1), p_{X_2|Y_2}(x_2|y_2), p_{Y_2}(y_2)$. Dal momento che

$$p_{X_1|Y_1}(x_1|y_1) = \frac{p_{X_1,Y_1}(x_1,y_1)}{p_{Y_1}(y_1)} \quad p_{X_2|Y_2}(x_2|y_2) = \frac{p_{X_2,Y_2}(x_2,y_2)}{p_{Y_2}(y_2)}$$

calcoliamo innanzitutto $p_{Y_1}(y_1)$ e $p_{Y_2}(y_2)$ mediante marginalizzazione delle relative congiunte.

---

## Pagina 86

Esempio di applicazione - 2

$$p_{Y_1}(0) = p_{X_1, Y_1}(0, 0) + p_{X_1, Y_1}(1, 0) = \frac{4}{9} \quad p_{Y_1}(1) = 1 - p_{Y_1}(0) = \frac{5}{9}$$

$$p_{Y_2}(-1) = p_{X_2, Y_2}(-1, -1) + p_{X_2, Y_2}(1, -1) = \frac{3}{8} \quad p_{Y_2}(1) = 1 - p_{Y_2}(-1) = \frac{5}{8}$$

Pertanto le condizionali si scrivono:

| $(x_1, y_1)$ | $p_{X_1|Y_1}(x_1|y_1)$ |
| :--- | :--- |
| 00 | $\frac{3}{4} = \frac{3}{4}$ |
| 01 | $\frac{6}{5} = \frac{6}{5}$ |
| 10 | $\frac{1}{5} = \frac{1}{5}$ |
| 11 | $\frac{3}{5} = \frac{3}{5}$ |

| $(x_2, y_2)$ | $p_{X_2|Y_2}(x_2|y_2)$ |
| :--- | :--- |
| $(-1, -1)$ | $\frac{1}{5} = \frac{1}{5}$ |
| $(-1, 1)$ | $\frac{2}{5} = \frac{2}{5}$ |
| $(1, -1)$ | $\frac{1}{5} = \frac{1}{5}$ |
| $(1, 1)$ | $\frac{8}{5} = \frac{8}{5}$ |

Ci limitamo all’applicazione a $Z_1$, lasciando per esercizio l’applicazione a $Z_2$.

$$\mathbb{E}[Z_1|Y_1 = 0] = \mathbb{E}[3X_1^2 + Y_1|Y_1 = 0] = \mathbb{E}[3X_1^2|Y_1 = 0] = 3p_{X_1|Y_1}(1|0) = \frac{3}{4}$$

$$\mathbb{E}[Z_1|Y_1 = 1] = 3\mathbb{E}[X_1^2|Y_1 = 1] + 1 = 3p_{X_1|Y_1}(1|1) + 1 = \frac{14}{5} \implies$$

$$\mathbb{E}[Z_1] = p_{Y_1}(0)\mathbb{E}[Z_1|Y_1 = 0] + p_{Y_1}(1)\mathbb{E}[Z_1|Y_1 = 1] = \frac{4}{9}\frac{3}{4} + \frac{5}{9}\frac{14}{5} = \frac{17}{9}$$

---

## Pagina 87

La covarianza tra due variabili aleatorie - 1

- Sia $(X, Y) \sim p_{X, Y}(x, y)$, $(x, y) \in \mathcal{X} \times \mathcal{Y}$;
- Abbiamo visto che le coppie $(\mu_X, \sigma_X^2)$ e $(\mu_Y, \sigma_Y^2)$ contengono delle informazioni globali - ancorchè sommarie - delle due marginali $p_X(x)$ e $p_Y(y)$.
- L'equivalente per le pmf congiunte è la covarianza, che dallà un'idea - ancora abbastanza sommaria - del grado di "dipendenza" tra $X$ e $Y$.

Definizioni
- Si definisce *correlazione* tra $X$ e $Y$ la quantità:
$$R_{X, Y} = \mathbb{E}[XY] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} xyp_{X, Y}(x, y)$$
- Si definisce *covarianza* di $X$ e $Y$ la quantità:
$$\sigma_{X, Y}^2 = \text{COV}[X, Y] = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (x - \mu_X)(y - \mu_Y)p_{X, Y}(x, y)$$

---

## Pagina 88

Proprietà della covarianza - 1

[a] Relazione tra correlazione e covarianza:

$$\text{COV}[X, Y] = \mathbb{E}[XY - \mu_X Y - \mu_Y X + \mu_X \mu_Y] = \mathbb{E}[XY] - \mu_X \mu_Y$$

dove si è sfruttata la linearità della media. Si noti che se almeno una delle due variabili ha media nulla COV[X, Y] = $R_{X, Y}$.

[b] Due variabili che abbiano covarianza nulla si dicono incorrelate. Si noti che variabili indipendenti sono sempre incorrelate, ma la proposizione non si inverte, nel senso che l’incorrelazione non implica in genere l’indipendenza.

$$(X, Y) \sim p_X(x)p_Y(y) \implies \text{COV}[X, Y] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (x - \mu_X)(y - \mu_Y)p_X(x)p_Y(y)$$

$$= \sum_{x \in \mathcal{X}} (x - \mu_X)p_X(x) \sum_{y \in \mathcal{Y}} (y - \mu_Y)p_Y(y) = \mathbb{E}[X - \mu_X] \mathbb{E}[Y - \mu_Y] = 0$$

---

## Pagina 89

Proprietà della covarianza - 2

$$|\text{COV}[X, Y]| \leq \sigma_X \sigma_Y$$

Questo potrebbe dimostrarsi con la disuguaglianza di Schwartz. Qui preferiamo un’altra strada. Si noti che:

$$0 \leq \mathbb{E} \left[ \left( \frac{X - \mu_X}{\sigma_X} \pm \frac{Y - \mu_Y}{\sigma_Y} \right)^2 \right] = \mathbb{E} \left[ \left( \frac{X - \mu_X}{\sigma_X} \right)^2 \right] + \mathbb{E} \left[ \left( \frac{Y - \mu_Y}{\sigma_Y} \right)^2 \right]$$

$$\pm 2\mathbb{E} \left[ \left( \frac{X - \mu_X}{\sigma_X} \frac{Y - \mu_Y}{\sigma_Y} \right) \right] = 2 \pm 2 \frac{\text{COV}[X, Y]}{\sigma_X \sigma_Y} \implies -1 \leq \frac{\text{COV}[X, Y]}{\sigma_X \sigma_X} \leq 1$$

La quantità $\rho_{X, Y} = \frac{\text{COV}[X, Y]}{\sigma_X \sigma_Y} \in [-1, 1]$ si definisce coefficiente di covarianza (ma più spesso di correlazione).

Infine, definendo $Z = aX + bY$, per cui $\mu_Z = a\mu_X + b\mu_Y$, avremo:

$$\sigma_Z^2 = \mathbb{E} \left[ Z^2 \right] - \mu_Z^2 = \mathbb{E} \left[ aX + bY \right] - (a\mu_X + b\mu_Y)^2$$

$$= a^2 \sigma_X^2 + b^2 \sigma_Y^2 + 2ab\text{COV}[X, Y]$$

---

## Pagina 90

# Esempio

Date le due pmf congiunte dell’esempio della slide 81 defire quale delle due leggi di probabilità congiunta dall’luogo a maggiore coeffiente di correlazione. Ricordiamo che

$$\begin{array}{c|c}
(x_1, y_1) & p_{X_1, Y_1}(x_1, y_1) \\
00 & \frac{1}{3} \\
01 & \frac{2}{9} \\
10 & \frac{1}{9} \\
11 & \frac{3}{9}
\end{array}$$

$$\begin{array}{c|c}
(x_2, y_2) & p_{X_2, Y_2}(x_2, y_2) \\
(-1, -1) & \frac{1}{4} \\
(-1, 1) & \frac{1}{2} \\
(1, -1) & \frac{1}{8} \\
(1, 1) & \frac{1}{8}
\end{array}$$

Pertanto le marginali di $X_1$, $X_2$, $Y_1$ e $Y_2$ si scrivono:

$$\begin{array}{c|c}
X_1 & p_{X_1}(x_1) \\
0 & \frac{5}{9} \\
1 & \frac{4}{9}
\end{array}$$

$$\begin{array}{c|c}
Y_1 & p_{Y_1}(y_1) \\
0 & \frac{4}{9} \\
1 & \frac{4}{9}
\end{array}$$

$$\begin{array}{c|c}
X_2 & p_{X_2}(x_2) \\
-1 & \frac{2}{4} \\
1 & \frac{4}{4}
\end{array}$$

$$\begin{array}{c|c}
Y_2 & p_{Y_2}(y_2) \\
-1 & \frac{3}{8} \\
1 & \frac{8}{8}
\end{array}$$

$$\mathbb{E}[X_1] = \mu_X_1 = \frac{4}{9}$$

$$\mathbb{E}[Y_1] = \mu_Y_1 = \frac{5}{9}$$

$$\mathbb{E}[X_2] = \mu_X_2 = -\frac{1}{2}$$

$$\mathbb{E}[Y_2] = \mu_Y_2 = \frac{1}{4}$$

$$\sigma_X_1^2 = \mathbb{E}[X_1]^2 - \mu_X_1^2 = 0.247$$

$$\sigma_Y_1^2 = \mathbb{E}[Y_1]^2 - \mu_Y_1^2 = 0.247$$

$$\sigma_X_2^2 = \frac{3}{4}$$

$$\sigma_Y_2^2 = \frac{15}{16} = 0.9375$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops

Metodi Statistici per l’Informazione - Marco Lops 89 / 161

---

## Pagina 91

Passiamo ora al calcolo delle covarianze. Avremo:

$$\mathbb{E}[X_1 Y_1] = p_{X_1, Y_1}(1, 1) = \frac{1}{3} \implies \text{COV}(X_1, Y_1) = \frac{1}{3} - \frac{20}{81} = \frac{7}{81} = 0.086$$

$$\mathbb{E}[X_2 Y_2] = p_{X_2, Y_2}(-1, -1) - p_{X_2, Y_2}(-1, 1) - p_{X_2, Y_2}(1, -1) + p_{X_2, Y_2}(1, 1) = \frac{3}{8} - \frac{5}{8} = -\frac{1}{4}$$

$$\implies \text{COV}(X_2, Y_2) = -\frac{1}{4} + \frac{1}{8} = -\frac{1}{8}$$

Quindi:

$$\rho_{X_1, Y_1} = \frac{\text{COV}(X_1, Y_1)}{\sigma_{X_1} \sigma_{Y_1}} = 0.348$$

$$\rho_{X_2, Y_2} = \frac{\text{COV}(X_2, Y_2)}{\sigma_{X_2} \sigma_{Y_2}} = -0.149$$

Essendo $|\rho_{X_1, Y_1}| > |\rho_{X_2, Y_2}|$, la coppia $(X_1, Y_1)$ risulta a correlazione assoluta maggiore. Si tenga pero presente che l’essere *negativamente* correlate implica che ci si aspetta che $X_2$ e $Y_2$ abbiano segno diverso e che diversi siano i segni delle deviazioni dalle rispettive medie!

---

## Pagina 92

Qualche considerazione iniziale

- Rimuoviamo ora l’ipotesi che lo spazio dei campioni Ω sia discreto.
- In particolare, supponiamo d’ora in poi che Ω ⊆ ℝ sia un sottoinsieme continuo dell’insieme reale;
- Ω potrebbe essere quindi esso stesso lo spazio delle misure osservabili oppure potrebbe essere il dominio di una applicazione:

$$X : \omega \in \Omega \rightarrow X(\omega) \in \mathcal{X}$$

- Naturalmente, su $\mathcal{X}$ non varrà più la limitazione cheesso sia un insieme finito;
- Spesso accade che $X(\omega) = \omega$ e $\mathcal{X} = \Omega$.

Esempio

La tensione misurata a vuoto ai capi di un carico resistivo è sempre non nulla per effetto dell’agitazione termica degli elettroni.

a. Si assuma di misurare $n$ volte tale tensione: avremmo ovviamente che $X(\omega) = \omega = x \in \mathbb{R}$ e i risultati delle misure saranno $\{x_i\}_{i=1}^n$;

b. Si supponga di misurare la potenza trasferita al carico resistivo $R$. In questo caso lo spazio campione sarà ancora $\Omega$, ma la corrispondente variabile aleatoria sarà $X(\omega) = \omega^2/R = x \in \mathbb{R}$.

---

## Pagina 93

Qualche considerazione iniziale

- Continuando con l’esempio precedente, è chiaro che gli eventi elementari saranno in entrambi i casi $\{X(\omega_i) = x_i\}$;
- Si potrebbe quindi essere tentati di definire:

$$\mathbb{P}(X = x_i) = \lim_{n \to \infty} \frac{n_{X=x_i}}{n}$$

dove, come nel caso discreto, $n_{X=x_i}$ rappresenta il numero di occorrenze dell’evento al pedice;

- Il problema di questa definizione - peraltro corretta - è che, se $X(\omega_i)$ e $X(\omega_j)$ sono due realizzazioni distinte di una variabile aleatoria reale non saremo mai in grado di misurarle con esattezza: dovremmo infatti disporre di uno strumento a precisione infinita e - anche in questo caso - l’evento $\{X(\omega_i) = X(\omega_j)\}$ sarebbe impossibile;

- Quello che possiamo dire è se la misura $X(\omega_j)$ cada o meno in un intorno della misura $X(\omega_i)$.

- Quindi, se $X(\omega)$ è una variabile aleatoria continua, gli eventi elementari $\{X(\omega) = x\}$ hanno - a meno di casi degeneri - probabilità nulla.

---

## Pagina 94

Esperimenti e variabili continue

- Supponiamo di compiere $n$ esperimenti, così da disporre di una collezione $\{X(\omega_i)\}$ di osservazioni di una variabile aleatoria continua $X(\omega)$.
- Sia $x \in \mathcal{X}$: ci chiediamo quale sia la frequenza di coccorrenza dell’evento $\{X$ cade in un intorno di dimensione $\Delta x$ di $x\}$. In conformità a quanto fatto in precedenza, avremo:

$$f_n(x; \Delta x) = \frac{n}{\frac{1}{n} \left( x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2} \right)}$$

dove ora $n_{\{x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2}\}}$ è il numero di volte (su $n$ esperimenti) in cui osserviamo $x - \frac{\Delta x}{2} \leq X(\omega) \leq x + \frac{\Delta x}{2}$.

- Possiamo allora definire la probabilità dell’evento $\{x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2}\}$ nella forma usuale (si riguardi l’avvertenza sulle notazioni della slide 45):

$$\mathbb{P}\left( \omega \in \Omega : \left\{ x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2} \right\} \right) = \mathbb{P}\left( X \in \left[ x - \frac{\Delta x}{2}, x + \frac{\Delta x}{2} \right] \right) =$$

$$P_X(x; \Delta x) = \lim_{n \to \infty} f_n(x; \Delta x)$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l’Informazione - Marco Lops 93 / 161

---

## Pagina 95

Densità di probabilità (probability density function, pdf)

Si definisce densità di probabilità (probability density function, pdf) della variabile aleatoria continua $X$ la funzione:

$$f_X(x) = \lim_{\Delta x \to 0} \frac{\mathbb{P}\left(x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2}\right)}{\Delta x} = \lim_{\Delta x \to 0} \frac{P_X(x; \Delta x)}{\Delta x}$$

Per il teorema fondamentale del calcolo integrale abbiamo quindi:

$$\mathbb{P}\left(x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2}\right) = \int_{x - \frac{\Delta x}{2}}^{x + \frac{\Delta x}{2}} f_X(t) dt$$

Le densità di probabilità devono soddisfare dei vincoli costitutivi, cioè:

a. $f_X(x) \geq 0 \ \forall x \in \mathbb{R}$: infatti il suo integrale su un qualunque intervallo non può essere negativo. Basterebbe, in linea di principio, una non-negatività quasi ovunque.

b. $f_X(x)$ è sommabile su $\mathbb{R}$ e a integrale unitario. Infatti:

$$\int_{-\infty}^{+\infty} f_X(t) dt = \mathbb{P}(X \in \mathbb{R}) = 1$$

---

## Pagina 96

<table><thead><tr><th>Esperimenti e Eventi</th><th>densità di probabilità (pdf)</th></tr></thead><tbody><tr><td>Leggi di Probabilità su Spazi Campione Continui</td><td>Caratterizzazione di variabili continue</td></tr><tr><td>Spazi Campione Continui</td><td>Variabili Aleatore Continue Doppie</td></tr><tr><td>Processi Aleatori</td><td>Variabili aleatore Gaussiane</td></tr></tbody><tfoot><tr><td colspan="2">Qualche commento intuitivo sulla pdf -1</td></tr><tr><td colspan="2">- Supponiamo di considerare un oggetto qualsiasi $C$, che occupi quindi un continuum di punti, $C \subseteq \mathbb{R}^3$;</td></tr><tr><td colspan="2">- Esistono vari modi di "misurarne" la dimensione, per esempio la Massa ($M$) e il volume ($V$).</td></tr><tr><td colspan="2">- Il criterio di misura (in breve, la misura - $\mu$-) deve però soddisfare tre requisiti:</td></tr><tr><td colspan="2">1) $\mu(A) \geq 0 \forall A \subseteq C$;</td></tr><tr><td colspan="2">2) $\mu(\emptyset) = 0$;</td></tr><tr><td colspan="2">3) Se $A_1 \subseteq C, A_2 \subseteq C : A_1 \cap A_2 = \emptyset$ allora $\mu(A_1 \cup A_2) = \mu(A_1) + \mu(A_2)$.</td></tr><tr><td colspan="2">- Si noti che sia $M(A)$ che $V(A)$ soddisfano queste condizioni;</td></tr><tr><td colspan="2">- Si consideri allora $P = (x, y, z) \in C$ e un suo intorno $\mathcal{I}(P)$ (per esempio, una piccola sfera). Si definisce densità dell'oggetto $C$ nel punto $P$ la quantità:</td></tr><tr><td colspan="2">$$\rho(P) = \lim_{V(\mathcal{I}(P)) \to 0} \frac{M(\mathcal{I}(P))}{V(\mathcal{I}(P))} \to M(A) = \int_A \rho(P) dV(\mathcal{I}(P)) = \int_A \rho(x, y, z) dxdydz$$</td></tr><tr><td colspan="2">che potremmo definire mdf, mass density function.</td></tr><tr><td colspan="2">- La nozione si generalizza a insiemi arbitrari. Ovviamente, occorrà comunque definire per un insieme "non canonico" la nozione di intorno (e quindi dare all'insieme una struttura topologica) e strutturare il dominio su cui si applica la funzione "misura" in modo adeguato, - cioè introdurre uno spazio di misura - ma questo esula dallo scopo del corso.</td></tr></tbody></table>

---

## Pagina 97

Qualche commento intuitivo sulla pdf - 2

Torniamo ora a $\Omega$ che - per evitare complicazioni topologiche - assumeremo coincidente con $\mathbb{R}$.

- Il modo ordinario di misurare sottoinsiemi di $\Omega$ (cioè, intervalli) è la misura di Lebesgue, cioè la loro lunghezza: $\mu_0 \left( \left[ x - \frac{\Delta x}{2}, x + \frac{\Delta x}{2} \right] \right) = \Delta x$;
- Un modo "alternativo" potrebbe essere: $\mu_1 \left( \left[ x - \frac{\Delta x}{2}, x + \frac{\Delta x}{2} \right] \right) = P_X(x; \Delta x)$, purchè, ovviamente, $\mu_1$ soddisfi le condizioni per essere una misura.
- All’uopo notiamo che:

  a. $\mu_1(A) \geq 0 \forall A \subseteq \Omega$;
  b. Se $A_1 \cap A_2 = \emptyset$ allora $X(A_1) = \left( \left[ x_1 - \frac{\Delta x}{2}, x_1 + \frac{\Delta x}{2} \right] \right)$,
    $X(A_2) = \left( \left[ x_2 - \frac{\Delta x}{2}, x_2 + \frac{\Delta x}{2} \right] \right)] e i due intervalli sono disgiunti, per cui:
      $\mu_1(A_1 \cup A_2) = \mathbb{P}(A_1 \cup A_2) = P_X(x_1; \Delta x) + P_X(x_2; \Delta x)$
  c. Infine $\mu_1(\emptyset) = \mathbb{P}(\emptyset) = \mathbb{P}(X \notin \mathbb{R}) = 0$;
- Quindi, come per massa-volume in $\mathbb{R}^3$, avremo:

$$f_X(x) = \lim_{\mu_0 \left( \left[ x - \frac{\Delta x}{2}, x + \frac{\Delta x}{2} \right] \right) \to 0} \frac{\mu_1 \left( \left[ x - \frac{\Delta x}{2}, x + \frac{\Delta x}{2} \right] \right)}{\mu_0 \left( \left[ x - \frac{\Delta x}{2}, x + \frac{\Delta x}{2} \right] \right)} = \lim_{\Delta x \to 0} \frac{P_X(x; \Delta x)}{\Delta x}$$

---

## Pagina 98

La DF come pdf

Ritorniamo un momento sugli spazi discreti.

- Se $A \subseteq \Omega$ è un insieme discreto, la misura "ordinaria" è ovviamente $\mu_0(A) = c(A) = |A|$, anche detta "misura di conteggio".

- Sia $\omega \in \Omega$ e sia $X(\omega) = x_*$: la misura ordinaria di $\{\omega\}$ sarebbe ovviamente $c(\{\omega\}) = 1$. Una misura alternativa è $\mu_1(\omega) = \mathbb{P}(\omega : X(\omega) = x_*) = p_X(x_*)$.

- Pertanto la densità di $\mu_1(\omega)$ rispetto a $\mu_0(\omega)$ è $p_X(x_*)$ e possiamo scrivere (simbolicamente):

$$p_X(x_*) = \frac{d\mu_1(\omega)}{dc(\omega)} \bigg|_{\omega=\omega^*}$$

- Se $A \subseteq \Omega$ e $X(A) = \mathcal{X}_A \subseteq \mathcal{X}$, avremo allora:

$$\mu_1(A) = \mathbb{P}(A) = \int_A d\mu_1(\omega) = \int_{\mathcal{X}_A} p_X(x)dc(x) = \sum_{x \in \mathcal{X}_A} p_X(x)$$

dove l'integrale è un integrale di Lebesgue rispetto alla misura di conteggio.

- Quindi, in generale la DF è una particolare pdf: questo lascia intui che tutte le proprietà dimostrate per le DF si estendono alle pdf (e, con opportuni cambiamenti, a tutte le densità di una misura rispetto a un'altra).

---

## Pagina 99

La Cumulative Distribution Function (CDF)

- Si noti preliminarme che $f_X(x)$, $x \in \mathbb{R}$ è perfettamente adeguata a caratterizzare $X$. Infatti:

$$\text{supp} \left[ f_X(x) \right] = \mathcal{X} \quad \mathbb{P}\left( a_1 \leq X \leq a_2 \right) = \int_{a_1}^{a_2} f_X(t) \, dt$$

dove $\text{supp}[g(\cdot)]$ indica il supporto della funzione $g(\cdot)$.

- Tuttavia è invalso l'uso di caratterizzazione alternative, e tra queste la Cumulative Distribution Function (CDF):

$$F_X(x) = \mathbb{P}\left( -\infty < X \leq x \right) = \int_{-\infty}^{x} f_X(t) \, dt \rightarrow f_X(x) = \frac{dF_X(x)}{dx}$$

- Talvolta si fa riferimento alla Complementary Cumulative Distribution Function (CCDF):

$$\bar{F}_X(x) = \mathbb{P}\left( X > x \right) = \int_{x}^{\infty} f_X(t) \, dt = 1 - F_X(x) \rightarrow f_X(x) = -\frac{d\bar{F}_X(x)}{dx}$$

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops  Metodi Statistici per l'Informazione - Marco Lops  98 / 161

---

## Pagina 100

Le proprietà derivano banalmente dalla definizione. In particolare:

- $F_X(x) \in [0, 1]$, in quanto è una probabilità;
- $F_X(-\infty) = 0$ e $F_X(+\infty) = 1$ (in quanto funzione integrale di una pdf);
- $F_X(x)$ è continua (in quanto funzione integrale di una funzione sommabile);
- $F_X(x)$ è crescente, in quanto l'integrando $f_X(\cdot)$ è non negativo;
- Ovviamente risulta

$$\mathbb{P}(a_1 \leq X \leq a_2) = \int_{a_1}^{a_2} f_X(t) \, dt = F_X(a_2) - F_X(a_1)$$

*Nota Bene* La CDF potrebbe definirsi anche per variabili discrete, nel qual caso la proprietà di continuità andrebbe "rimodulata". Tuttavia la CDF di variabili discrete non è una grandezza utile.

---

## Pagina 101

Media statistica di variabili continue - 1

Data una variabile aleatoria continua con pdf $f_X(x)$, definiamo la sua media statistica come:

$$\mathbb{E}[X] = \mu_X = \int_{\mathbb{R}} xf_X(x) \, dx$$

Per giustificare questa definizione, possiamo usare vari argumenti.

- Si cominci con il considerare una versione "quantizzata di $X$ nella forma:

$$X^\Delta = x_i \in [i\Delta, (i+1)\Delta] \text{ se } i\Delta \leq X < (i+1)\Delta \rightarrow \mathbb{P}(X = x_i) = \int_{i\Delta}^{(i+1)\Delta} f_X(x) \, dx$$

- Ovviamente avremo:

$$\mathbb{E}[X^\Delta] = \sum_{i=-\infty}^{\infty} x_i \underbrace{\int_{i\Delta}^{(i+1)\Delta} f_X(x) \, dx}_{p_X\Delta(x_i)}$$

- Infine, se $xf_X(x)$ è integraibile secondo Riemann:

$$\mathbb{E}[X] = \lim_{\Delta \to 0} \mathbb{E}[X^\Delta] = \lim_{\Delta \to 0} \sum_{i=-\infty}^{\infty} x_i f_X(x_i) \Delta = \int_{\mathbb{R}} xf_X(x) \, dx$$

---

## Pagina 102

Un’altra giustificazione è quella alla luce delle considerazioni intuitive sulla riducibilità di una DF a una pdf. Infatti, se Ω è uno spazio discreto, sappiamo che:

$$\mathbb{E}[X] = \sum_{x \in \mathcal{X}} xp_X(x) = \int_{\mathcal{X}} xf_X(x)dc(x) = \int_{\Omega} X(\omega)d\mu_1(\omega)$$

dove $\mu_1(\cdot)$ è la misura di probabilità introdotta su Ω con densità (rispetto alla misura di conteggio) $\frac{d\mu_1(\omega)}{dc(\omega)} = p_X[x(\omega)]$.

Quindi possiamo definire la media statistica di una variabile aleatoria (non importa se discreta o continua) nella forma

$$\mathbb{E}[X] = \int_{\Omega} X(\omega)d\mu_1(\omega)$$

dove l’integrale è un integrale di Lebesgue. Per Ω = $\mathbb{R}$ avremo ovviamente $d\mu_1(\omega) = f_X(x)dx$, per cui

$$\mathbb{E}[X] = \int_{\mathbb{R}} xf_X(x)dx$$

---

## Pagina 103

Variabili Uniformi

Una variabile aleatoria $X$ si dice uniformemente distribuite su un intervallo $[a, b]$, $b \ge a$ ($X \sim \mathcal{U}(a, b)$) se:

$$f_X(x) = \begin{cases} \frac{1}{b-a} & x \in [a, b] \\ 0 & \text{altrove} \end{cases}$$

Siccome supp[$f_X(x)] = [a, b], tale è il suo alfabeto (cioè $X$ non assume valori esterni all'intervallo). La sua CDF si scrive quindi:

$$F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt = \begin{cases} 0 & x < a \\ \frac{x-a}{b-a} & a \leq x \leq b \\ 1 & x \ge b \end{cases}$$

mentre la sua media statistica vale:

$$\mathbb{E}[X] = \int_{a}^{b} \frac{x}{b-a} \, dx = \frac{b^2 - a^2}{2(b-a)} = \frac{a+b}{2}$$

L'andamento di pdf e CDF sono mostrati nella successiva slide.

---

## Pagina 104

Esperimenti e Eventi
Leggi di Probabilità su Spazi Campione Continui
Spazi Campione Continui
Processi Aleatori
Processi aleatori

densità di probabilità (pdf)
Caratterizzazione di variabili continue
Variabili Aleatore Continue Doppie
Variabili aleatore Gaussiane

pdf e CDF di variabili uniformi

pdf di $X \sim U(a, b)$

CDF di $X \sim U(a, b)$

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statistici per l’Informazione - Marco Lops 103 / 161

---

## Pagina 105

Variabili esponenziali

Una variabile aleatoria $X$ si dice esponenziale con parametro $\lambda (X \sim \mathcal{E}(\lambda))$ se ha una pdf:

$$f_X(x) = \lambda e^{-\lambda x} u(x), \quad u(x) \text{ gradino unitario continuo}$$

per cui supp[$f_X(x)] = [0, \infty[, il che implica $X \geq 0$.

La sua CDF vale dunque:

$$F_X(x) = \int_0^x \lambda e^{-\lambda t} dt = \left(1 - e^{-\lambda x}\right) u(x)$$

La sua media vale infine:

$$\mathbb{E}[X] = \lambda \int_0^\infty xe^{-\lambda x} dx = \frac{1}{\lambda}$$

I relativi andamenti sono mostrati nella prossima slide.

---

## Pagina 106

# pdf e CDF di variabili esponenziali

**Esperimenti e Eventi**

Leggi di Probabilità su Spazi Campione discreti

Spazi Campione Continui

Processi Aleatori

Processi aleatori

**densità di probabilità (pdf)**

**Caratterizzazione di variabili continue**

Variabili Aleatore Continue Doppie

Variabili aleatore Gaussiane

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statisticici per l'Informazione - Marco Lops 105 / 161

---

## Pagina 107

Variabili laplaciane

Una variabile aleatoria $X$ si dice laplaciana con parametro $\lambda$ ($X \sim \mathcal{L}(\lambda)$) se ha una pdf:

$$f_X(x) = \frac{\lambda}{2} e^{-\lambda|x|}$$

per cui supp[$f_X(x)] = \mathbb{R}$, il che implica $X$ può assumere qualunque valore reale..
La sua CDF vale dunque:

$$F_X(x) = \int_{-\infty}^{x} \frac{\lambda}{2} e^{-\lambda|t|} dt = \begin{cases} \frac{\lambda}{2} \int_{-\infty}^{x} e^{\lambda t} dt = \frac{1}{2} e^{\lambda x} & x \leq 0 \\ \frac{\lambda}{2} \left[ \int_{-\infty}^{0} e^{\lambda t} dt + \int_{0}^{x} e^{-\lambda t} dt \right] = 1 - \frac{1}{2} e^{-\lambda x} & x \geq 0 \end{cases}$$

La sua media è nulla, come sempre accade per le pdf pari. Infatti:

$$\mathbb{E}[X] = \frac{\lambda}{2} \int_{-\infty}^{\infty} xe^{-\lambda|x|} dx = 0$$

I relativi andamenti sono mostrati nella prossima slide.

---

## Pagina 108

Esperimenti e Eventi
Leggi di Probabilità su Spazi Campione discreti
Spazi Campione Continui
Processi Aleatori
Processi aleatori

densità di probabilità (pdf)
Caratterizzazione di variabili continue
Variabili Aleatore Continue Doppie
Variabili aleatore Gaussiane

pdf e CDF di variabili laplaciane

$$pdf di X \sim \mathcal{L}(\lambda)$$

$$CDF di X \sim \mathcal{L}(\lambda)$$

---

## Pagina 109

Variabili di Cauchy

Una variabile aleatoria $X$ si dice di Cauchy con parametr1 $(a, b)$ ($X \sim \mathcal{C}(a, b)$) se ha una pdf:

$$f_X(x) = \frac{1}{b\pi} \frac{1}{1 + \left(\frac{x-a}{b}\right)^2}$$

per cui supp[$f_X(x)] = \mathbb{R}$, il che implica $X$ può assumere qualunque valore reale..
La sua CDF vale dunque:

$$F_X(x) = \frac{1}{b\pi} \int_{-\infty}^{x} \frac{dt}{1 + \left(\frac{t-a}{b}\right)^2} dt = \frac{1}{2} + \frac{1}{\pi} \arctan \left(\frac{x-a}{b}\right)

La sua media non è definita, perchè $xf_X(x)$ non è integrable. Tuttavia è definibile un punto di simmetria mediante il seguente integrale a valor principale:

$$\frac{1}{b\pi} \lim_{H \to \infty} \int_{-H}^{H} \frac{x}{1 + \left(\frac{x-a}{b}\right)^2} dx = a$$

I relativi andamenti sono mostrati nella prossima slide.

---

## Pagina 110

pdf e CDF di variabili di Cauchy

Esperimenti e Eventi
Leggi di Probabilità su Spazi Campione discreti
Spazi Campione Continui
Processi Aleatori
Processi aleatori

densità di probabilità (pdf)
Caratterizzazione di variabili continue
Variabili Aleatore Continue Doppie
Variabili aleatore Gaussiane

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statisticici per l’Informazione - Marco Lops 109 / 161

---

## Pagina 111

In modo del tutto analogo a quanto fatto per le variabili discrete, potremo scrivere:

$$\mathbb{P}\left[ X \in \left( x - \frac{\Delta x}{2}, x - \frac{\Delta x}{2} \right) \mid A \right] = P_X(x, \Delta x|A) \Rightarrow f_{X|A}(x) = \lim_{\Delta x \to 0} \frac{P_X(x, \Delta x|A)}{\Delta x}$$

o, anche:

$$F_{X|A}(x) = \mathbb{P}\left( X \leq x \mid A \right) = \frac{\mathbb{P}\left( \{ X \leq x \} \cap A \right)}{\mathbb{P}(A)} \Rightarrow f_{X|A}(x) = \frac{dF_{X|A}(x)}{dx}$$

Per esempio, sia $X \sim \mathcal{L}(\lambda)$ e $A = \{-1 \leq X \leq 2\}$. Avremo:

$$F_{X|\{-1 \leq X \leq 2\}}(x) = \frac{\mathbb{P}\left( \{ X \leq x \} \cap \{-1 \leq X \leq 2\} \right)}{F_X(-1 \leq X \leq 2)} = \begin{cases} 0 & x < -1 \\ \frac{F_X(x) - F_X(-1)}{F_X(2) - F_X(-1)} & -1 \leq x \leq 2 \\ 1 & x \geq 2 \end{cases}$$

$$f_{X|\{-1 \leq X \leq 2\}}(x) = \begin{cases} \frac{f_X(x)}{F_X(2) - F_X(-1)} = \frac{\frac{\lambda}{2} e^{-\lambda|x|}}{1 - \frac{1}{2} e^{-2\lambda} + \frac{1}{2} e^{-\lambda}} & x \in (-1, 2) \\ 0 & x \notin (-1, 2) \end{cases}$$

---

## Pagina 112

pdf e CDF condizionali di variabili Laplaciane

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statistici per l’Informazione - Marco Lops 111 / 161

---

## Pagina 113

Legge della probabilità totale per pdf e medie

In modo del tutto analogo al caso discreto (vedi slide 56) si può mostrare che, se $\{E_m\}_{m=1}^M$ è una qualunque partizione di $\Omega$, allora:

$$f_X(x) = \sum_{m=1}^{M} f_X|E_m(x) \mathbb{P}(E_m) \iff F_X(x) = \sum_{m=1}^{M} F_X|E_m(x) \mathbb{P}(E_m)$$

Naturalmente, questo implica che per le medie valga un’analoga relazione (vedi slide 57):

$$\mathbb{E}[X] = \sum_{m=1}^{M} \mathbb{E}[X|E_m] \mathbb{P}(E_m) = \sum_{m=1}^{M} \mathbb{P}(E_m) \int_{\mathbb{R}} xf_X|E_m(x) dx$$

Quindi, con riferimento all’esempio precedente con $X \sim \mathcal{L}(\lambda)$:

$$\mathbb{E}[X] = \mathbb{E}[X|\{-1 \leq X \leq 2\}] \mathbb{P}(-1 \leq X \leq 2) + \mathbb{E}[X|\{X \notin [-1, 2]\}] \underbrace{\mathbb{P}(X \notin [-1, 2])}_{1-\mathbb{P}(-1 \leq X \leq 2)} = 0$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l’Informazione - Marco Lops 112 / 161

---

## Pagina 114

Quest’argomento riproduce - come problematica - quello già affrontato nel caso di variabili discrete (vedi slide 58 e seguenti).

- Si assuma che $X = X(\omega)$ sia una variabile aleatoria continua con alfabeto $\mathcal{X}$, pdf $f_X(x)$ e CDF $F_X(x)$;
- Sia $g(\cdot)$ una funzione il cui insieme di definizione inclusa i punti di $\mathcal{X}$ - a meno di un sottoinsieme a (misura di) probabilità nulla;
- Si forma la nuova variabile aleatoria:

$$Y = g(X) = g[X(\omega)] \in \mathcal{Y}$$

**Problema:** Ricavare una caratterizzazione di $Y$ dalla caratterizzazione di $X$ in termini di

- pdf/CDF, $p_Y(y)$, $y \in \mathcal{Y}$;
- media statistica, $\mathbb{E}[Y]$.

---

## Pagina 115

Funzioni di variabili aleatorie continue -2

A differenza di quanto fatto nel caso discreto (vedi slide 59 e seguenti), qui distinguiamo tre casi:

a $\{g(x)\}_{x \in \mathcal{X}}$ biunivoca, cioè invertibile $\forall x$, continua e derivabile;

b $\{g(x)\}_{x \in \mathcal{X}}$ continua, derivabile e univoca - e quindi non invertibile - con $\mathcal{Y}$ continuo;

c $\{g(x)\}_{x \in \mathcal{X}}$ univoca - e quindi non invertibile - con $\mathcal{Y}$ discreto: quest’ultimo caso corrisponde ad una conversione A/D della variabile continua (cioè una sua quantizzazione ovvero compressione con perdite) in analogia a quanto visto nella conversione A/D di segnali e sequenza deterministiche.

---

## Pagina 116

Ricordiamo che se $y = g(x)$ è invertibile, allora essa è strettamente monotona $\forall x \in \mathcal{X}$. Pertanto:

- $g(x)$ strettamente crescente ($g'(x) > 0$):
  $$F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(g(X) \leq y) = \mathbb{P}(X \leq g^{-1}(y)) = F_X \left[g^{-1}(y)\right]$$
  $$f_Y(y) = \frac{dF_Y(y)}{dy} = f_X \left[g^{-1}(y)\right] \frac{dg^{-1}(y)}{dy} = \frac{f_X \left[g^{-1}(y)\right]}{g' \left[g^{-1}(y)\right]}$$

- $g(x)$ strettamente decrescente ($g'(x) < 0$):
  $$F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(g(X) \leq y) = \mathbb{P}(X \geq g^{-1}(y)) = 1 - F_X \left[g^{-1}(y)\right]$$
  $$f_Y(y) = -\frac{dF_Y(y)}{dy} = f_X \left[g^{-1}(y)\right] \frac{dg^{-1}(y)}{dy} = \frac{f_X \left[g^{-1}(y)\right]}{-g' \left[g^{-1}(y)\right]}$$

per cui la pdf $f_Y(y)$ si scrive in forma unificata:

$$f_Y(y) = \frac{f_X \left[g^{-1}(y)\right]}{\left|g' \left[g^{-1}(y)\right]\right|}$$

---

## Pagina 117

Funzioni non invertibili

Si assuma ora che $y = g(x)$ non sia invertibile. Questo implica che:

$$\forall y \in \mathcal{Y} \quad \exists \{x_i(y)\}_{i=1}^{M(y)}: \quad g[x_i(y)] = y$$

Supponiamo, per fissare le idee, $M(y) = 4$, $g'(x_1) < 0$: questo implica che $g(x) \leq y$ $x_1(y) \leq y \leq x_2(y)$; ovviamente, $g'(x_2(y))$ sarà positivo e $g(x) > y$ per $x_2(y) \leq y \leq x_3(y)$. La funzione ripassa per il valore $g(x_3(y)) = y$ (con derivata negativa) e si mantiene al di sotto di $y$ fino a $x_4(y)$. Quindi (vedi figura nella prossima slide):

$$F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}\left(\{x_1(y) \leq X \leq x_2(y)\} \cup \{x_4(y) \leq X \leq x_3(y)\}\right) =$$

$$F_Y[x_2(y)] - F_Y[x_1(y)] + F_Y[x_4(y)] - F_Y[x_3(y)]$$

dove si è ovviamente sfruttata la disgiunzione dei vari intervalli. Pertanto, derivando:

$$f_Y(y) = \sum_{i=1}^{4} (-1)^i f_X[x_i(y)] x_i'(y) = \sum_{i=1}^{4} \frac{f_X[x_i(y)]}{|g'[x_i(y)]|}$$

dove si è sfruttato il fatto che $x'(y) = \frac{1}{g'[g^{-1}(y)]}$ e che i segni sono alternati.

---

## Pagina 118

Funzioni non invertibili

$$f_Y(y_1) = \sum_{i=1}^{3} f_X[x_i(y_1)] \left| \frac{dx_i(y)}{dy} \right|_{y=y_1} = \sum_{i=1}^{3} \frac{f_X[x_i(y_1)]}{|g'[x_i(y_1)]|}$$

$$f_Y(y_2) = \sum_{i=1}^{2} f_X[x_i(y_2)] \left| \frac{dx_i(y)}{dy} \right|_{y=y_2} = \sum_{i=1}^{2} \frac{f_X[x_i(y_2)]}{|g'[x_i(y_2)]|}$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops

Metodi Statistici per l’Informazione - Marco Lops 117 / 161

---

## Pagina 119

Qualche esempio - 1

Sia $g(x) = x^2$, si considerino $X_1 \sim \mathcal{E}(\lambda)$ e $X_2 \sim \mathcal{C}(0, 1)$. Vogliamo determinare le pdf di $Y_1 = g(X_1) = X_1^2$ e $Y_2 = g(X_2) = X_2^2$.

- Per $Y_1$, si ha che, poichè $\mathcal{X}_1 = [0, \infty[$ e poichè $g(x) = x^2$ è biunivoca per $x \geq 0$, sarà:

$$x^2 = y \rightarrow x(y) = \sqrt{y} \rightarrow x'(y) = \frac{1}{g'(x)} \bigg|_{x=\sqrt{y}} = \frac{1}{2x} \bigg|_{x=\sqrt{y}} = \frac{1}{2\sqrt{y}}$$

- Quindi:

$$f_{Y_1}(y) = \lambda e^{-\lambda x} u(x) \bigg|_{x=\sqrt{y}} x'(y) = \frac{\lambda}{2\sqrt{y}} e^{-\lambda \sqrt{y}} u(y)$$

- Per $Y_2$, invece, essendo $\mathcal{X}_2 = \mathbb{R}$, $g(x) = x^2$ non è biunivoca e l'equazione $x^2 = y$ ha due soluzioni, $x(y) = \pm \sqrt{y}$. Si noti inoltre che $Y = [0, +\infty[$, cioè $Y \geq 0$. Quindi:

$$f_{Y_2}(y) = \left[ \frac{f_X(\sqrt{y})}{|g'(\sqrt{y})|} + \frac{f_X(-\sqrt{y})}{|g'(-\sqrt{y})|} \right] u(y), \quad \text{poichè } f_X(x) = \frac{1}{\pi} \frac{1}{1+x^2} \Rightarrow$$

$$f_{Y_2}(y) = \left( \frac{1}{2\pi\sqrt{y}} \frac{1}{1+y} + \frac{1}{2\pi\sqrt{y}} \frac{1}{1+y} \right) u(y) = \frac{1}{\pi\sqrt{y}} \frac{1}{1+y} u(y)$$

---

## Pagina 120

Sia $X \sim f_X(x)$. Vogliamo la pdf di $Y = F_X(X)$,cioè assumiamo $g(x) = F_X(x)$.

- Notiamo preliminarme che $\mathcal{Y} = [0, 1]$ qualunque sia $\mathcal{X}$. Inoltre, $g(x)$ è monotona crescente: potrebbe non essere strettamente crescente se $\mathcal{X}$ non è connesso, ma escludiamo questo caso.

- Avremo allora:

$$g(x) = F_X(x) \rightarrow x(y) = F_X^{-1}(y) \quad g'(x) = f_X(x) \implies$$

$$f_Y(y) = \frac{f_X\left[F_X^{-1}(y)\right]}{f_X\left[F_X^{-1}(y)\right]} \Pi\left(y - \frac{1}{2}\right) = \Pi\left(y - \frac{1}{2}\right)$$

cioè $Y \sim \mathcal{U}(0, 1)$.

- Quindi, se si ha una variabile aleatoria uniforme $U \sim \mathcal{U}(0, 1)$, la trasformazione $X = F_X^{-1}(U)$ genera una variabile aleatoria con pdf arbitraria $f_X(x)$: Questo ha delle notevoli conseguenze nelle procedure di simulazione dei sistemi numerici.

---

## Pagina 121

Qualche esempio - 3

Sia $X \sim U\left(-\frac{1}{2}, \frac{1}{2}\right)$, $g(x) = A \cos(2\pi x + \varphi)$: Vogliamo la pdf di $Y = A \cos(2\pi X + \varphi)$.

- Notiamo preliminarmente che $\mathcal{Y} = [-A, A]$ e che la trasformazione non è biunivoca. Infatti:

$$y = A \cos(2\pi x + \varphi) \rightarrow 2\pi x(y) + \varphi = \pm \arccos\left(\frac{x}{A}\right)$$

- Valutando la derivata dell’inversa si ha:

$$x'(y) = \frac{1}{g'(x)} \bigg|_{x=x(y)} = -\frac{1}{2\pi A \sin(2\pi x + \varphi)} \bigg|_{2\pi x=\pm \arccos\left(\frac{x}{A}\right)-\varphi} = \pm \frac{1}{2\pi A \sin\left[\arccos\left(\frac{x}{A}\right)\right]} = \pm \frac{1}{2\pi A \sqrt{1-\left(\frac{x}{A}\right)^2}}$$

- Poichè $f_X(x) = \Pi\left(x-\frac{1}{2}\right)$, applicando le formule precedenti si ha

$$f_Y(y) = \frac{1}{\pi A \sqrt{1-\left(\frac{x}{A}\right)^2}}, \quad y \in [-A, A]$$

---

## Pagina 122

Conversione A/D di variabili aleatorie

Quando X è continua e Y discreta si ha una conversione A/D di una quantità aleatoria (confronta anche l'ultima sezione della parte "Conversione A/D").

- Supponiamo di voler rappresentare (con perdite) X con R bit, cioè con $M = 2^R$ livelli;
- Definiamo una variabile aleatoria $Y = g(X)$ con $Y = \{y_1, \ldots, y_M\}$;
- Definiamo una partizione di $X$ in M intervalli, definiti dai punti $\{x_i\}_{i=1}^{M+1}$;
- Si definisce rappresentazione a R bit di X la variabile aleatoria discreta:

$$Y = y_i \quad \text{se } x_i \leq X \leq x_{i+1} \quad i = 1, \ldots, M$$

- La pmf di Y quindi si scrive facilmente nella forma:

$$p_Y(y_i) = P_X \left( \frac{x_{i+1} + x_i}{2}; \frac{x_{i+1} - x_i}{2} \right) = F_X(x_{i+1}) - F_X(x_i), \quad i = 1, \ldots, M$$

- Ovviamente tanto la partizione quanto i livelli di rappresentazione sono gradi di libertà a disposizione del progettista.

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops  Metodi Statistici per l'Informazione - Marco Lops 121 / 161

---

## Pagina 123

Media di funzioni di variabili aleatorie continue

Sia $X \sim f_X(x)$ e sia $Y = g(X)$, con $\mathcal{Y} = g(\mathcal{X})$. Vogliamo estendere alle variabili continue il Teorema Fondamentale per il calcolo della media (vedi slide 60 e seguenti).

Il risultato principale - diretta derivazione del caso discreto - è che, qualunque sia $g(x)$:

$$\mathbb{E}[Y] = \mathbb{E}[g(X)] = \int_{\mathbb{R}} g(x)f_X(x) \, dx$$

- Definiamo una versione quantizzata di $X$ a $M$ livelli, $X^\Delta$, in modo del tutto analogo a quanto fatto per ricavare la media di variabili continue (vedi slide 100);
- A questa applicichiamo la trasformazione $g(\cdot)$, ottenendo la variabile discreta $Y^\Delta = g(X^\Delta)$:

$$X^\Delta = x_i \in [i\Delta, (i+1)\Delta] \quad i\Delta \leq X < (i+1)\Delta \Rightarrow g(X^\Delta) = g(x_i)$$

- Il teorema quindi segue - se $g(x)f_X(x)$ è Riemann-integrable - dall’essere:

$$\mathbb{E}[Y] = \lim_{\Delta \to 0} \mathbb{E}[Y^\Delta] = \lim_{\Delta \to 0} \sum_{i=1}^{M} g(x_i) \underbrace{f_X(x_i)}_{\simeq \mathbb{P}(i\Delta \leq X < (i+1)\Delta)} = \int_{\mathbb{R}} g(x)f_X(x) \, dx$$

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statistici per Il Informazione - Marco Lops 122 / 161

---

## Pagina 124

Valore quadratico medio e varianza di variabili continue

È a questo punto immediata la generalizzazione dei concetti introdotti nella slide 62 per variabili discrete a variabili continue.

Data una variabile aleatoria $X \sim f_X(x)$, $x \in \mathcal{X}$, con media $\mu_X = \mathbb{E}[X]$ definiamo:

- Il valore quadratico medio (Mean Square) di $X$:
  $$X^2_{\text{rms}} = \mathbb{E}[X^2] = \int_{\mathbb{R}} x^2 f_X(x) \, dx$$

- Il valore efficace (root mean square, rms) di $X$:
  $$X_{\text{rms}} = \sqrt{\mathbb{E}[X^2]} = \sqrt{\int_{\mathbb{R}} x^2 f_X(x) \, dx}$$

- La varianza di $X$:
  $$\sigma^2_X = \mathbb{E}[(X - \mu_X)^2] = \int_{\mathbb{R}} (x^2 + \mu_X^2 - 2x\mu_X) f_X(x) \, dx = X^2_{\text{rms}} - \mu_X^2$$

- La deviazione standard di $X$:
  $$\sigma_X = \sqrt{\sigma^2_X} = \sqrt{\mathbb{E}[X^2] - \mu_X^2} = \sqrt{X^2_{\text{rms}} - \mu_X^2}$$

Tutte le proprietà della slide 68 ovviamente valgono per variabili continue.

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops  Metodi Statistici per l'Informazione - Marco Lops 123 / 161

---

## Pagina 125

Qualche esempio

- Sia $X \sim \mathcal{U}(a, b)$. Si ottiene facilmente:
  $$\mu_X = \frac{a + b}{2} \quad \mathbb{E}[X^2] = \frac{a^2 + b^2 + ab}{3} \quad \sigma_X^2 = \mathbb{E}[X^2] - \mu_X^2 = \frac{(b - a)^2}{12}$$

- Sia $X \sim \mathcal{E}(\lambda)$. Avremo:
  $$\mu_X = \frac{1}{\lambda} \quad \mathbb{E}[X^2] = \frac{2}{\lambda^2} \quad \sigma_X^2 = \mathbb{E}[X^2] - \mu_X^2 = \frac{1}{\lambda^2}$$

- Sia $X \sim \mathcal{L}(\lambda)$. Avremo:
  $$\mu_X = 0 \quad \mathbb{E}[X^2] = \frac{2}{\lambda^2} \quad \sigma_X^2 = \mathbb{E}[X^2] = \frac{2}{\lambda^2}$$

- Sia $X \sim \mathcal{C}(a, b)$: Non esistono in questo caso nè la media, nè la varianza, nè, quindi, valore rms o deviazione standard.

---

## Pagina 126

Variabili continue multiple

In perfetta analogia con quanto fatto per variabili discrete (vedi slide 69), una coppia di variabili continue (o variabile doppia) è definita nella forma:

$$X, Y : \omega \in \Omega \rightarrow (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y} \subseteq \mathbb{R}^2$$

dove $\mathcal{X}$ e $\mathcal{Y}$ sono gli alfabeti di $X$ e di $Y$ rispettivamente. Analogamente, date tre variabili aleatorie - a questo punto non importa più se tutte continue o meno - $X(\omega) \in \mathcal{X}, y(\omega) \in \mathcal{Y}, Z(\omega) \in \mathcal{Z}$:

$$X, Y, Z : \omega \in \Omega \rightarrow (X(\omega), Y(\omega), Z(\omega)) \in \mathcal{X} \times \mathcal{Y} \times \mathcal{Z} \subseteq \mathbb{R}^3$$

e, date $m$ variabili aleatorie $X_i \in \mathcal{X}_i \subseteq \mathbb{R}$, avremo la $m$-pla aleatoria:

$$X_1, \ldots, X_m : \omega \in \Omega \rightarrow (X_1(\omega), \ldots, X_m(\omega)) \in \mathcal{X}_1 \times \ldots \times \mathcal{X}_m \subseteq \mathbb{R}^m$$

---

## Pagina 127

# pdf congiunta di due variabili aleatorie

Si consideri una coppia di variabili continue, $X \in \mathcal{X}$ e $Y \in \mathcal{Y}$, la loro pdf congiunta si definisce in perfetta analogia con la pdf di variabili continue singole (vedi slide 94):

$$f_{X,Y}(x,y) = \lim_{\Delta x \to 0} \lim_{\Delta y \to 0} \frac{\mathbb{P}\left(\left\{x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2}\right\} \cap \left\{y - \frac{\Delta y}{2} \leq Y \leq y + \frac{\Delta y}{2}\right\})}{\Delta x \Delta y}$$

$$= \lim_{\Delta x \to 0} \lim_{\Delta y \to 0} \frac{P_{X,Y}(x,y; \Delta x, \Delta y)}{\Delta x \Delta y} \quad (x,y) \in \mathcal{X} \times \mathcal{Y}$$

Per il teorema fondamentale del calcolo integrale abbiamo quindi che, se $C \subseteq \mathcal{X} \times \mathcal{Y}$:

$$\mathbb{P}((X,Y) \in C) = \int_C f_{X,Y}(x,y) \, dxdy$$

Le densità di probabilità congiunte devono soddisfare dei vincoli costitutivi - simili a quelli delle densità marginali:

a. $f_{X,Y}(x,y) \geq 0 \forall(x,y) \in \mathbb{R}^2$;
b. $f_{X,Y}(x,y)$ è sommabile su $\mathbb{R}^2$ e a integrale unitario. Infatti:

$$\int_{\mathbb{R}^2} f_{X,Y}(x,y) \, dxdy = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f_{X,Y}(x,y) \, dxdy = \mathbb{P}((X,Y) \in \mathbb{R}^2) = 1$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statistici per l Informazione - Marco Lops 126 / 161

---

## Pagina 128

Proprietà della pdf congiunta

La pdf congiunta $f_{X,Y}(x,y)$ condivide con la pmf congiunta $p_{X,Y}(x,y)$ - e, per alcune, con tutte le densità - le seguenti proprietà:

- Proprietà di marginalizzazione:
  $$\int_{\mathbb{R}} f_{X,Y}(x,y) \, dy = f_X(x) \quad \int_{\mathbb{R}} f_{X,Y}(x,y) \, dx = f_Y(y)$$
  per cui caratterizzare *congiuntamente* $(X,Y)$ significa anche caratterizzarle *marginalmente*, mentre il viceversa non è necessariamente vero.

- Indipendenza statistica: due variabili aleatorie sono indipendenti se e solo se
  $$f_{X,Y}(x,y) = f_X(x)f_Y(y) \iff F_{X,Y}(x,y) = \mathbb{P}(X \leq x, Y \leq y) = F_X(x)F_Y(y)$$

- Più in generale, se $X_i \sim f_{X_i}(x)$, $x \in \mathcal{X}_i$, allora esse sono indipendenti se e solo se:
  $$f_{X_1,\dots,x_m}(x_1,\dots,x_m) = \prod_{i=1}^{m} f_{X_i}(x_i), \quad (x_1,\dots,x_m) \in \mathbb{R}^m$$

Marco Lops  lops@unina.it https://docenti.unina.it/marco.lops Metodi Statisticici per l Informazione - Marco Lops 127 / 161

---

## Pagina 129

Le pdf condizionate

- Si considerino varibili aleatore $X \in \mathcal{X}$ e $Y \in \mathcal{Y}$ con assegnata pdf congiunta $f_{X,Y}(x,y)$;
- La pdf condizionata di $X$ dato $Y$ si può definire a partire dalla seguente quantità (vedi slide 110):

$$\mathbb{P} \left( x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2} \mid y - \frac{\Delta y}{2} \leq Y \leq y + \frac{\Delta y}{2} \right) = \frac{P_{X,Y}(x,y; \Delta x, \Delta y)}{P_{Y}(y; \Delta y)}$$

- Pertanto la densità di $X$ condizionata all’evento $\left\{ y - \frac{\Delta y}{2} \leq Y \leq y + \frac{\Delta y}{2} \right\}$ è:

$$\lim_{\Delta x \to 0} \frac{P_{X,Y}(x,y; \Delta x, \Delta y)}{\Delta x P_{Y}(y; \Delta y)} = f_{X \mid \left\{ y - \frac{\Delta y}{2} \leq Y \leq y + \frac{\Delta y}{2} \right\}} \left( x \mid y - \frac{\Delta y}{2} \leq Y \leq y + \frac{\Delta y}{2} \right)$$

- Facendo dunque tendere $\Delta y$ a zero, otteniamo:

$$f_{X \mid Y}(x \mid y) = \lim_{\Delta x \to 0} \lim_{\Delta y \to 0} \frac{P_{X,Y}(x,y; \Delta x, \Delta y)}{P_{Y}(y; \Delta y)} = \frac{f_{X,Y}(x,y)}{f_{Y}(y)}$$

che, come c’era da attendersi, riproduce l’analoga definizione per la pmf condizionale che, d’altronde, è essa stessa una densità.

- Di conseguenza tutte le proprietà delle pmf condizionali si estendono alle pdf condizionali.

---

## Pagina 130

Proprietà delle pdf condizionate

Data l’analogia con le variabili discrete, ci limitiamo qui a riscrivere le proprietà della slide 74

- $f_{X|Y}(x|y)$ se $y$ resta fisso e $x$ varia in $\mathcal{X}$ è una densità di probabilità, cioè:

$$f_{X|Y}(x|y) \geq 0 \quad \int_{\mathbb{R}} f_{X|Y}(x|y) \, dx = 1$$

- Legge della probabilità totale per le pdf:

$$f_X(x) = \int_{\mathbb{R}} f_X,Y(x,y) \, dy = \int_{\mathbb{R}} f_{X|Y}(x|y) f_Y(y) \, dy$$

$$f_Y(y) = \int_{\mathbb{R}} f_X,Y(x,y) \, dx = \int_{\mathbb{R}} f_{Y|X}(y|x) f_X(x) \, dx$$

- Leggi della probabilità composta e di Bayes per le densità:

$$f_{X,Y}(x,y) = f_Y(y) f_{X|Y}(x|y) = f_X(x) f_{Y|X}(y|x) \Rightarrow f_{Y|X}(y|x) = \frac{f_Y(y) f_{X|Y}(x|y)}{f_X(x)}$$

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops  Metodi Statistici per l’Informazione - Marco Lops 129 / 161

---

## Pagina 131

Altre estensioni...

Come nel caso discreto, avremo:

- Se $Z = g(X, Y)$ allora
  $$\mathbb{E}[Z] = \int_{\mathbb{R}^2} g(x, y) f_{X, Y}(x, y) \, dxdy$$
- Linearità della media:
  $$\mathbb{E}\left[\sum_{i=1}^{m} a_i X_i\right] = \sum_{i=1}^{m} a_i \mathbb{E}[X_i]$$
- Teorema della media condizionata:
  $$\mathbb{E}[g(X, Y)] = \mathbb{E}\left[\mathbb{E}[g(X, Y)|Y]\right]$$
dove:
  $$\mathbb{E}[g(X, Y)|Y = y] = \int_{\mathbb{R}} g(x, y) f_{X|Y}(x|y) \, dx = \mathbb{E}[h(Y(\omega))] \iff h[Y(\omega)] = \int_{\mathbb{R}} g(x, Y) f_{X|Y}(x|Y) \, dx$$

---

## Pagina 132

Covarianza tra due variabili continue

Siano $(X, Y) \sim f_{X, Y}(x, y)$. Denotiamo con $(\mu_X, \mu_Y)$ le rispettive medie e $(\sigma_X^2, \sigma_Y^2)$ le rispettive varianze. Avremo, in analogia al caso discreto:

- Covarianza tra $X$ e $Y$:
  $$\text{COV}[X, Y] = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = \mathbb{E}[XY] - \mu_X \mu_Y$$
- coefficiente di correlazione tra $X$ e $Y$:
  $$\rho_{X, Y} = \frac{\text{COV}[X, Y]}{\sigma_X \sigma_Y}, \quad |\rho_{X, Y}| \leq 1$$
- Incorrelazione tra $X$ e $Y$: $\text{COV}[X, Y] = 0$.
- Indipendenza implica incorrelazione, ma incorrelazione non implica indipendenza.

---

## Pagina 133

Variabili Gaussiane: Caratterizzazione marginale

Una variabile aleatoria $X_0 \in \mathcal{X} = \mathbb{R}$ si dice Gaussiana (o Normale) standard $X_0 \sim \mathcal{N}(0, 1)$ se:

$$f_X(x_0) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x_0^2}{2}}, \quad x \in \mathbb{R} \implies \mathbb{E}[X_0] = 0 \quad \sigma_X^2 = \mathbb{E}[X_0^2] = 1$$

Consideriamo ora la variabile aleatoria $X = \sigma_X X_0 + \mu_X$, $\sigma_X > 0$ e $\mu_X \in \mathbb{R}$. Applicando i risultati delle slide 114 e seguenti alla funzione lineare $g(x) = \sigma_X x + \mu_X$ otteniamo:

$$f_X(x) = \frac{1}{\sqrt{2\pi \sigma_X^2}} e^{-\frac{(x - \mu_X)^2}{2\sigma_X^2}}, \quad x \in \mathbb{R} \implies X \sim \mathcal{N}(\mu_X, \sigma_X^2)$$

dove ovviamente:

$$\mathbb{E}[X] = \mathbb{E}[\sigma_X X_0 + \mu_X] = 0 \quad \mathbb{E}[(X - \mu_X)^2] = \text{VAR}[\sigma_X X_0 + \mu_X] = \sigma_X^2$$

---

## Pagina 134

Andamenti di pdf Gaussiane

pdf di $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$

$$f_X(x)$$

$$\mu_X = -5$$
$$\mu_X = 0$$
$$\mu_X = 5$$

$$\sigma_X^2 = 0.5, 1, 2$$

Marco Lops  lops@unina.it  https://docenti.unina.it/marco.lops

Metodi Statisticici per l’Informazione - Marco Lops 133 / 161

---

## Pagina 135

La funzione $Q(x)$

Sia $X_0 \sim \mathcal{N}(0,1)$: nè la sua CDF nè la sua CCDF sono note in forma esplicita, poichè $e^{-\gamma x^2}$ non ammette primitive elementari.

Definiamo:

$$Q(x) \stackrel{\text{def}}{=} \mathbb{P}(X \ge x) = 1 - F_X_0(x) = \frac{1}{\sqrt{2\pi}} \int_x^\infty e^{-\frac{t^2}{2}} dt$$

per cui:

$$F_X_0(x) = 1 - Q(x) \quad P_X_0(x; \Delta x) = Q\left(x - \frac{\Delta x}{2}\right) - Q\left(x + \frac{\Delta x}{2}\right)$$

Ovviamente, se $X \sim \mathcal{X}(\mu_X, \sigma_X^2)$, avremo $X = X_0\sigma_X + \mu_X$, per cui:

$$1 - F_X(x) = \frac{1}{\sqrt{2\pi}\sigma_X^2} \int_x^\infty e^{-\frac{(t - \mu_X)^2}{2\sigma_X^2}} dt = Q\left(\frac{x - \mu_X}{\sigma_X}\right)$$

Dato il suo uso frequente, nella prossima slide è presentato un diagramma della funzione $Q(x)$, $x \ge 0$.

---

## Pagina 136

Andamento di $Q(x)$

$$Q(x) \sim \frac{1}{x\sqrt{2\pi}} e^{-\frac{x^2}{2}} < e^{-\frac{x^2}{2}}, \quad x \to \infty$$

Diagramma di $Q(x)$ per $x \geq 0$

---

## Pagina 137

Alcune utili proprietà della funzione $Q(x)$

- Si noti preliminarmente che
  $$Q(-\infty) = \frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} e^{-\frac{t^2}{2}} dx = 1 \quad Q(\infty) = 0$$
- Inoltre:
  $$\frac{dQ(x)}{dx} = -\frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} < 0 \text{ for } x \rightarrow Q(x) \text{ è decrescente in } x$$
- Simmetria:
  $$Q(-x) = \frac{1}{\sqrt{2\pi}} \int_{-x}^{\infty} e^{-\frac{t^2}{2}} dt = 1 - \underbrace{\frac{1}{\sqrt{2\pi}} \int_{-x}^{-x} e^{-\frac{t^2}{2}} dt}_{= Q(x)} = 1 - Q(x)$$
- Se $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$ allora:
  $$\mathbb{P}(X \geq \eta) = \mathbb{P}(X_0 \sigma_X + \mu_X \geq \eta) = \mathbb{P}\left(X_0 \geq \frac{\eta - \mu_X}{\sigma_X}\right) = Q\left(\frac{\eta - \mu_X}{\sigma_X}\right)$$

---

## Pagina 138

Caratterizzazione congiunta di variabili Gaussiane

Siano $X_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ e $X_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)$. Noi sappiamo che:

$$\sigma_1^2 = \mathbb{E} \left[ (X_1 - \mu_1)^2 \right] \quad \sigma_2^2 = \mathbb{E} \left[ (X_2 - \mu_2)^2 \right] \quad \rho_{1,2} = \frac{\text{COV}(X_1, X_2)}{\sigma_1 \sigma_2}$$

rappresenta una caratterizzazione "globale" (cioè incompleta) della copia $(X_1, X_2)$. Organizziamo tale copia in un vettore colonna $X = (X_1, X_2)^T$. Ovviamente, $X \in \mathbb{R}^{2 \times 1}$ è un vettore bidimensionale aleatorio, la cui media è essa stessa un vettore, $\mu_X = (\mu_1 \mu_2)^T$.

Definiamo $Matrice di covarianza$ del vettore $X$ la matrice $K_X \in \mathbb{R}^{2 \times 2}$:

$$K_X \stackrel{\text{def}}{=} \mathbb{E} \left[ (X - \mu_X)(X - \mu_X)^T \right] = \mathbb{E} \left[ \left( \begin{array}{cc} X_1 - \mu_1 \\ X_2 - \mu_2 \end{array} \right) (X_1 - \mu_1 X_2 - \mu_2) \right] =$$

$$= \mathbb{E} \left[ \begin{array}{cc} (X_1 - \mu_1)^2 & (X_1 - \mu_1)(X_2 - \mu_2) \\ (X_2 - \mu_2)(X_1 - \mu_1) & (X_2 - \mu_2)^2 \end{array} \right] = \left( \begin{array}{cc} \sigma_1^2 & \sigma_1 \sigma_2 \rho_{1,2} \\ \sigma_1 \sigma_2 \rho_{1,2} & \sigma_2^2 \end{array} \right)$$

---

## Pagina 139

Alcune proprietà della matrice di covarianza

- Poichè $|K_X| = \sigma_1^2 \sigma_2^2 (1 - \rho_{1,2}^2) \geq 0$, $K_X$ è definita non negativa;
- Se $\rho_{1,2} \neq \pm 1$ $K_X$ è invertibile e ha inversa definita positiva:

$$K_X^{-1} = \frac{1}{\sigma_1^2 \sigma_2^2 (1 - \rho_{1,2}^2)} \begin{pmatrix} \sigma_2^2 & -\sigma_1 \sigma_2 \rho_{1,2} \\ -\sigma_1 \sigma_2 \rho_{1,2} & \sigma_1^2 \end{pmatrix}$$

- $K_X$ è simmetrica;
- Ovviamente, se $z = [z_1 z_2]^T \in \mathbb{R}^{2 \times 1}$:

$$z^T K_X^{-1} z \geq 0 \quad \forall z \in \mathbb{R}^{2 \times 1}$$

- Se $X_1$ e $X_2$ sono incorrelate allora $\rho_{1,2} = 0$, per cui $K_X$ diventa la matrice diagonale:

$$K_X = \begin{pmatrix} \sigma_1^2 & 0 \\ 0 & \sigma_2^2 \end{pmatrix} \implies K_X^{-1} = \begin{pmatrix} \frac{1}{\sigma_1^2} & 0 \\ 0 & \frac{1}{\sigma_2^2} \end{pmatrix}$$

---

## Pagina 140

Variabili congiuntamente Gaussiane

Le due variabili $X_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ e $X_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)$ si dicono congiuntamente Gaussiane se la loro pdf congiunta - cioè la pdf del vettore $X = (X_1 X_2)^T$ - si scrive:

$$f_X(x) = \frac{1}{2\pi |K_X|^{1/2}} \exp \left[ -\frac{1}{2} (x - \mu_X)^T K_X^{-1} (x - \mu_X) \right] = f_{X_1, X_2}(x_1, x_2) = \frac{1}{2\pi \sqrt{\sigma_1^2 \sigma_2^2 (1 - \rho_{1,2}^2)}} \exp \left[ -\frac{\sigma_2^2 (x_1 - \mu_1)^2 + \sigma_1^2 (x_2 - \mu_2)^2 - 2\rho_{1,2} (x_1 - \mu_1) (x_2 - \mu_2)}{2\sigma_1^2 \sigma_2^2 (1 - \rho_{1,2}^2)} \right]$$

In questo caso si può usare la notazione abbreviata $X \sim \mathcal{N}(\mu_X, K_X)$. Nel caso speciale $\rho_{1,2} = 0$, la precedente dà:

$$f_X(x) = f_{X_1, X_2}(x_1, x_2) = \frac{1}{2\pi \sqrt{\sigma_1^2 \sigma_2^2}} e^{-\frac{(x_1 - \mu_1)^2}{2\sigma_1^2} - \frac{(x_2 - \mu_2)^2}{2\sigma_2^2}} = f_{X_1}(x_1) f_{X_2}(x_2)$$

cioè se due variabili sono congiuntamente Gaussiane (e solo in questo caso)

l’incorrelazione implica l’indipendenza statistica!

---

## Pagina 141

Proprietà di chiusura rispetto a trasformazioni lineari

Se $X \sim \mathcal{N}(\mu_X, K_X)$ allora ogni trasformazione lineare di $X$ dall’luogo a un nuovo vettore Gaussiano.

Focalizziamoci prima su una semplice combinazione lineare di $X_1$ e $X_2$. Avremo che:

$$Z = a_1X_1 + a_2X_2 \Rightarrow \mu_Z = a_1\mu_1 + a_2\mu_2 \quad \sigma_Z^2 = a_1^2\sigma_1^2 + a_2^2\sigma_2^2 + 2a_1a_2\sigma_1\sigma_2\rho_{1,2}$$

$$Z \sim \mathcal{N}(\mu_Z, \sigma_Z^2)$$

Più in generale, se $Z = AX + b$, con $A \in \mathbb{R}^{2 \times 2}$ e $b \in \mathbb{R}^{2 \times 1}$ allora:

$$\mu_Z = A\mu_X + b \quad \mathbb{E}[(Z - \mu_Z)(Z - \mu_Z)^T] = AK_XA^T = K_Z$$

$$Z \sim \mathcal{N}(\mu_Z, K_Z)$$

---

## Pagina 142

Richiami sulle variabili aleatorie

• Si consideri uno spazio di probabilità arbitrario, $\Omega, \mathcal{T}, \mathbb{P}$, dove $\Omega$ è lo spazio dei campioni, $\mathcal{T}$ una $\sigma$-algebra di eventi di $\Omega$ e $\mathbb{P} : \mathcal{T} \rightarrow [0, 1]$ una legge di probabilità.

• Ricordiamo che una variabile aleatoria reale $X$ è una funzione (misurabile) definita come:

$$X : \omega \in \Omega \implies X(\omega) \in \mathcal{X} \subseteq \mathbb{R}$$

• La variabile aleatoria è discreta se tale è $\mathcal{X}$, continua se tale è $\mathcal{X}$.

• Una coppia di variabili aleatoria è un’applicazione

$$X, Y : \omega \in \Omega \implies (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y} \subseteq \mathbb{R}^2$$

• La variabile aleatoria $X$ si dice completamente caratterizzata se ne è nota la CDF $F_X(x)$ o - equivalente - la DF $p_X(x)$ o la pdf $f_X(x)$ nel caso discreto e continuo, rispettivamente:

$$F_X(x) = \mathbb{P}\{X \leq x\} \quad \forall x \in \mathbb{R} \quad p_X(x) = \mathbb{P}\{X = x\} \quad \forall x \in \mathbb{X} \quad f_X(x) = \frac{df_X(x)}{dx}$$

• Parallelamente, per la coppia $(X, Y)$ si ha:

$$F_{X,Y}(x,y) = \mathbb{P}\{X \leq x, Y \leq y\} \quad \forall(x,y) \in \mathbb{R}^2 f_{X,Y}(x,y) = \frac{\partial^2 F_{X,Y}(x,y)}{\partial x \partial y}$$

$$p_{X,Y}(x,y) = \mathbb{P}\{X = x, Y = y\} \quad \forall x \in \mathcal{X} \times \mathcal{Y}$$

---

## Pagina 143

Vettori aleatori

- Una $n$-pla aleatoria è una ovvia generalizzazione del concetto di coppia di variabili aleatori,cioè:

$$\left(X_1, \ldots, X_n\right) : \omega \in \Omega \implies X(\omega) = \left(X_1(\omega), \ldots, X_n(\omega)\right) \in \mathcal{X}_1 \times \ldots \times \mathcal{X}_n \subseteq \mathbb{R}^n$$

- Un vettore aleatorio si ottiene quindi facilmente come

$$X(\omega) = \left[X_1(\omega), \ldots, X_n(\omega)\right]^T \in \mathcal{X}_1 \times \ldots \times \mathcal{X}_n \subseteq \mathbb{R}^n$$

- Se gli alfabeti $\mathcal{X}_1, \ldots, \mathcal{X}_n$ sono discreti, il vettore è discreto e si caratterizza mediante la DF congiunta;

$$p_X(x) = p_X(x_1, \ldots, x_n) = \mathbb{P}\left\{X_1 = x_1, \ldots, X_n = x_n\right\} \quad \forall x \in \mathcal{X}_1 \times \ldots \mathcal{X}_n$$

dove $x = [x_1, \ldots, x_n]^T \in \mathcal{X}_1 \times \ldots \mathcal{X}_n$.

- Per alfabeti continui, avremo

$$F_X(x) = \mathbb{P}\left\{X_1 \leq x_1, \ldots, X_n \leq x_n\right\} \quad \forall x \in \mathbb{R}^n$$

$$f_X(x) = \frac{\partial^n F_X(x)}{\partial x_1 \ldots \partial x_n}$$

dove $x = [x_1, \ldots, x_n]^T \in \mathbb{R}^n$.

---

## Pagina 144

Legge di Bayes per vettori aleatori

- Consideriamo un vettore aleatorio discreto con pmf $p_X(x)$. Sappiamo che la Legge di Bayes assicura che

$$\mathbb{P}(A \cap B) = \mathbb{P}(A|B) \mathbb{P}(B)$$

- Posto $A = \{X_n = x_n, \ldots, X_2 = x_2\}$ e $B = \{X_1 = x_1\}$ avremo

$$p_X(x) = \mathbb{P}\{X_n = x_n, \ldots, X_2 = x_2|X_1 = x_1\} \mathbb{P}\{X_1 = x_1\}$$

- Iterando il ragionamento avremo la regola della catena:

$$p_X(x) = \mathbb{P}\{X_1 = x_1\} \mathbb{P}\{X_2 = x_2|X_1 = x_1\} \cdots \mathbb{P}\{X_n = x_n|X_{n-1} = x_{n-1}, \ldots, X_1 = x_1\}$$

$$= \prod_{i=1}^{n} p_{X_i|X_{i-1}, \ldots, X_1}(x_i|x_{i-1}, \ldots, x_1), \quad p_{X_1|X_0}(x_1|x_0) = p_{X_1}(x_1)$$

- Analogamente, per vettori continui avremo

$$f_X(x) = \prod_{i=1}^{n} f_{X_i|X_{i-1}, \ldots, X_1}(x_i|x_{i-1}, \ldots, x_1)$$

---

## Pagina 145

Processi aleatori tempo-discreti

- Si definisce **processo aleatorio tempo-discreto** un’applicazione che ad ogni elemento dello spazio campione fa corrispondere una successione:

$$X : \omega \in \Omega \rightarrow \{X(n, \omega)\}_{n \in \mathbb{Z}}$$

dove $\mathbb{Z}$ indica l’insieme degli interi.

- Di seguito sono riportate tre realizzazioni di un processo tempo-discreto.

---

## Pagina 146

Commenti e osservazioni

• Per ogni valore di $\omega \in \Omega$ il processo si realizza in una sequenza che assume valori nell'intervalo $[-1, 1]$;

• Fissando l'istante di tempo $n = n_0$ e facendo variare $\omega \in \Omega$ otteniamo $X(n_0, \omega)$, che è una variabile aleatoria (visto che "campionando verticalmente" il processo otteniamo che al variare di $\omega X(n_0, \omega)$ assume diverse determinazioni);

• La variabile aleatoria $X(n_0, \omega)$ ha una sua pdf, che in genere dipende da $\omega$;

• Se la pdf non dipende dall'istante di campionamento $n_0$, il processo si dice stazionario al primo ordine;

• Nel caso mostrato in figura, il processo è stato generato assumendolo stazionario e marginalmente uniforme in $[-0.5, 0.5]$, cioè

$$f_X(n)(x; n) = f_X(n)(x) = \Pi(x - 0.5)$$

• Si noti che siccome

$$\mathbb{E}[X(n)] = \int_{-\infty}^{\infty} xf_X(n)(x; n) \, dx = \int_{-0.5}^{0.5} x\Pi(x - 0.5) \, dx = 0$$

il processo è a media identicamente nulla.

---

## Pagina 147

Un altro esempio: processo Gaussiano tempo-discreto

- Come secondo esempio, consideriamo un processo tempo-discreto stazionario al primo ordine con pdf

$$f_{X(n)}(x) = \frac{1}{\sqrt{2\pi}} \exp \left[ -\frac{(x + 0.5)^2}{2} \right]$$

quindi con densità marginale Gaussiana a media $-0.5$ e varianza unitaria. Otteniamo realizzazione del tipo rappresentate in figura

---

## Pagina 148

Caratterizzazione del secondo ordine del processo

- Un processo aleatorio si dice caratterizzato al primo ordine se ne è nota la pdf $f_{X(n)}(x; n)$ per ogni $n$. Se il processo è stazionario al primo ordine, questo equivale ad assegnare un’unica pdf.
- Un processo aleatorio si dice caratterizzato al secondo ordine se ne è assegnata la pdf congiunta
  $$f_{X(n1), X(n2)}(x1, x2; n1, n2), \quad \forall n1, n2$$
- Un processo aleatorio si dice stazionario al secondo ordine se, per qualsiasi intero $h$, abbiamo:
  $$f_{X(n1), X(n2)}(x1, x2; n1, n2) = f_{X(n1+h), X(n2+h)}(x1, x2; n1, n2 + h)$$
- In altre parole, un processo stazionario al secondo ordine è tale che la caratterizzazione congiunta di due suoi campioni dipende unicamente dalla loro "distanza" temporale, ma non dalla loro posizione: in altre parole, la pdf congiunta è invariante ad atti di moto rigido dei due punti in anticipo o in ritardo.
- Ovviamente un processo stazionario al secondo ordine lo è anche al primo, ma non èvero il viceversa Perchè?.

---

## Pagina 149

Caratterizzazione completa di un processo

• Un processo aleatorio $X(n)$ si dice completamente caratterizzato se, detto $M$ un intero arbitrario e detti $n_1, \ldots, n_M$ $M$ istanti arbitrari, il vettore aleatorio

$$X = [X(n_1), \ldots, X(n_M)]^T$$

ha densità di probabilità $f_X(x_1, \ldots, x_M)$ nota.

• Un processo aleatorio si dice *stazionario in senso stretto* di ordine $M$ se la sua densità di probabilità di ordine $M$ è invariante per traslazione, cioè:

$$f_X(n_1), \ldots, X(n_M)(x_1, \ldots, x_M; n_1, \ldots, n_M) =$$

$$f_X(n_1+h), \ldots, X(n_M+h)(x_1, \ldots, x_M; n_1+h, \ldots, n_M+h)$$

• Un processo stazionario di ordine $M$ lo è di qualunque ordine $i \leq M$.

• Un processo si dice *indipendente* (o a campioni indipendenti) se, comunque si scelga un intero $M$, il vettore $X = [X(n_1), \ldots, X(n_M)]^T$ è costituito da variabili aleatorie indipendenti, cioè:

$$f_X(n_1), \ldots, X(n_M)(x_1, \ldots, x_M) = f_X(n_1)(x_1)f_X(n_2)(x_2) \cdots f_X(n_M)(x_M) = \prod_{i=1}^{M} f_X(n_i)(x_i)$$

---

## Pagina 150

Processi discreti

• Si definisce processo ampiezza discreto o - per brevità - processo discreto un processo aleatorio in cui le cui realizzazione siano sequenze di numeri che possano assumere valore in un alfabeto discreto.
• Un caso di importanza notevole è quello di un processo indipendente binario, $X(n) \in \{-1, 1\}$, con $\mathbb{P}\{X(n) = 1\} = \mathbb{P}\{X(n) = 1\} = \frac{1}{2}$, di cui le realizzazioni sono riportate in figura, anche detto Processo di Bernoulli.

---

## Pagina 151

Un altro esempio: Un processo quaternario

- Un ulteriore esempio si ha considerando un alfabeto quaternario, per esempio $X(n) \in \{-2, -1, 1, 2\}$, con livelli equiprobabili (per cui $\mathbb{P}\{X(n) = i\} = \frac{1}{4} \forall i$).
- Le realizzazioni del processo saranno quindi del tipo rappresentato in figura

---

## Pagina 152

Caratterizzazione di processi discreti

• Tutte le definizioni introdotte per i processi continui si estendono ai processi discreti, con la sola differenza che le densità di probabilità sono ora sostituite dalle DF;

• Per esempio, un processo discreto si dice *stazionario in senso stretto* se, comunque si scelga un intero $M$, il vettore aleatorio $X = [X(n_1), \ldots, X(n_M)]$ gode, per un $h$ arbitrario, della proprietà:

$$\mathbb{P}\{X(n_1) = x_1, X(n_2) = x_2, \ldots, X(n_M) = x_M\} =$$

$$\mathbb{P}\{X(n_1 + h) = x_1, X(n_2 + h) = x_2, \ldots, X(n_M + h) = x_M\}$$

• Ovviamente, la stazionarietà di ordine $M$ implica quella di ogni ordine $\leq M$. In particolare, un processo stazionario ha una DF marginale indipendente dal tempo.

• Un processo discreto che sia *stazionario e indipendente* ovviamente gode della proprietà:

$$\mathbb{P}\{X(n_1) = x_1, X(n_2) = x_2, \ldots, X(n_M) = x_M\} = \prod_{i=1}^{M} \mathbb{P}\{X(n_i) = x_i\} = \prod_{i=1}^{M} p_X(x_i)$$

dove $p_X(\cdot)$ è la DF marginale (ovviamente indipendente dal tempo).

---

## Pagina 153

Caratterizzazione sintetica dei vettori aleatori

• Come per le variabili aleatorie, anche per i processi aleatori è possibile - a fronte di un’impossibilità di fornire una caratterizzazione completa - definire una caratterizzazione sintetica,cioè assegnarne statistiche che siano significative.

• In modo del tutto analogo al caso scalare, dove abbiamo visto che la copia media-varianza ($\mu_X, \sigma_X^2$) offre spesso importanti informazioni sul comportamento della variabile $X$, e al caso delle copie, in cui la cinquina ($mu_X, \sigma_X, \mu_Y, \sigma_Y$, COV($X, Y$) offre analoghe informazioni sulla copia ($X, Y$), per u vettore alatorio $X = [X_1, \ldots, X_n]^T$ abbiamo

† la media statistica

$$\mu_X = (\mathbb{E}[X_1], \ldots, \mathbb{E}[X_n])^T$$

† la matrice di covarianza, $C_X = \mathbb{E}\left[(X - \mu_X)(X - \mu_X)^T\right]$:

$$
\begin{pmatrix}
\sigma_X^2 & \text{COV}(X_1, X_2) & \cdots & \text{COV}(X_1, X_n) \\
\text{COV}(X_2, X_1) & \sigma_X^2 & \cdots & \text{COV}(X_2, X_n) \\
\cdots & \cdots & \cdots & \cdots \\
\text{COV}(X_n, X_1) & \text{COV}(X_n, X_2) & \cdots & \sigma_X^2
\end{pmatrix}
$$

---

## Pagina 154

Processi Stazionari in Senso Lato (SSL)

• Focalizziamoci sui processi tempo discreti, ma quanto verrà detto vale anche per i processi tempo-continui.
• Abbiamo visto che un processo $X(n) \in \mathcal{X}$ è stazionario di ordine 2 se:
$$\mathbb{P}\{X(n) = x\} = p_X(x) \quad \forall x \in \mathbb{P}\{X(n_1) = x_1, X(n_2) = x_2\} = \mathbb{P}\{X(n_1 + h) = x_1, X(n_2 + h) = x_2\}$$
• Ovviamente la media $\mu_X = \mathbb{E}[X(n)] = \sum_{x \in \mathcal{X}} xp_X(x)$ non dipende da $n$;
• Inoltre si noti che
$$\mathbb{E}[X(n_1)X(n_2)] = \sum_{x_1 \in \mathcal{X}} \sum_{x_2 \in \mathcal{X}} x_1x_2\mathbb{P}\{X(n_1) = x_1, X(n_2) = x_2\} = \mathbb{E}[X(n_1 + h)X(n_2 + h)] = \sum_{x_1 \in \mathcal{X}} \sum_{x_2 \in \mathcal{X}} x_1x_2\mathbb{P}\{X(n_1 + h) = x_1, X(n_2 + h) = x_2\}$$
che significa che $\mathbb{E}[X(n_1)X(n_2)]$ è funzione di $n_2 - n_1$, ma non separatamente di $n_1$ e $n_2$.

• Un processo $X(n/t)$, continuo o disceto, non necessariamente stazionario al secondo ordine, si dice stazionario in senso lato se
  † La sua media non dipende dal tempo;
  † la sua autocorrelazione soddisfa la condizione
$$R_X(t_1/n_1, t_2/n_2) = \mathbb{E}[X(t_1/n_1)X(t_2/n_2)] = R_X(t_2 - t_1/n_2 - n_1)$$

---

## Pagina 155

Matrice di covarianza per processi SSL

• Sia $X(t/n)$ un processo SSL, continuo o discreto, e sia $X = [X_1, \ldots, X_M]^T$ un vettore aleatorio $M$ dimensionale di campioni di $X(t/n)$, presi negli istanti $(t_1, \ldots, t_M)/(n_1, \ldots, n_M)$
• Ovviamente avremo che $\mu = \mathbb{E}[X] = \mu 1$, con $\mu$ scalare e 1 un vettore $M$-dimensionale di tutti "1".
• Inoltre, avremo, per la condizione SSL:

$$\mathbb{E}[X_i X_j] = f(|i - j|) \quad \mathbb{E}[X_i^2] = \overline{X^2}, \quad \text{Var}(X_i) = \overline{X^2} - \mu^2 = \sigma_X^2$$

per cui, definendo $\rho_{i,j} = \frac{\text{COV}(X_i, X_j)}{\sigma_X^2}$ la matrice di covarianza assume la forma

$$C_X = \sigma_X^2 \begin{pmatrix}
1 & \rho_{1,2} & \rho_{1,3} & \cdots & \rho_{1,M} \\
\rho_{1,2} & 1 & \rho_{2,3} & \cdots & \rho_{2,M} \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
\rho_{1,M} & \rho_{2,M} & \rho_{3,M} & \cdots & 1
\end{pmatrix}$$

• Pertanto la matrice di covarianza di un vettore tratto da un processo SSL è simmetrica.
• Si noti che se il passo di campionamento del processo è costante (cioè, $(t_{i+1} - t_i)/(n_{i+1} - n_i)$ costante $\forall i$, allora la matrice assume una forma di Toeplitz.

---

## Pagina 156

Esercizio: La matrice di covarianza è sempre definita non-negativa

- Ricordiamo che una matrice $C \in \mathbb{R}^{M \times M}$ è definita non negativa se, detto $q \in \mathbb{R}^M$ un qualunque vettore $M$-dimensione risulta $q^T C q \geq 0$.
- Consideriamo un vettore aleatorio $M$-dimensionale $X$ di media $\mu$ e matrice di covarianza $C_X$. La quantità $q^T X$ è ovviamente una variabile aleatoria scalare con $\mathbb{E} \left[ q^T X \right] = q^T \mu$. Inoltre

$$\mathbb{E} \left[ \left( q^T X \right)^2 \right] = \mathbb{E} \left[ q^T X X^T q \right] = q^T \mathbb{E} \left[ X X^T \right] q$$

- Avremo allora la catena di disuguaglianze:

$$0 \leq \text{Var} \left( q^T X \right) = q^T \mathbb{E} \left[ X X^T \right] q - \left( q^T \mu \right)^2 = q^T \mathbb{E} \left[ X X^T \right] q - q^T \mu \mu^T q = q^T \underbrace{\left( \mathbb{E} \left[ X X^T \right] - \mu \mu^T \right)}_{C_X} q$$

dove si è sfruttato il fatto

$$C_X = \mathbb{E} \left[ (X - \mu)(X - \mu)^T \right] = \mathbb{E} \left[ X X^T \right] - \mu \mu^T$$

---

## Pagina 157

Estensione ai processi continui: definizioni

• Quanto detto sui processi ampiezza-discreti si estende ai processi ampiezza continui;

• Detto $X = [X(t_1/n_1), \ldots, X(t_M/n_M)]$ tratto da un processo $X/t/n$, la sua caratterizzazione implica l’assegnazione di una delle due funzioni:

$$F_X(x_1, \ldots, x_M) = F_X(x) = \mathbb{P}\{X_1 \leq x_1, \ldots, X_M \leq x_M\}$$

$$f_X(x) = \lim_{V(\Delta x) \to 0} \frac{\mathbb{P}_X(x, \Delta x)}{V(\Delta x)} = \frac{\partial^M F_X(x)}{\partial x_1 \partial x_2 \ldots \partial x_M}$$

dove $\Delta x = (\Delta x_1, \ldots, \Delta x_M)$, $V(\Delta x) = \Delta x_1 \cdots \Delta x_M$ e:

$$\mathbb{P}_X(x, \Delta x) = \mathbb{P}\left\{x_1 - \frac{\Delta x_1}{2} \leq X_1 \leq x_1 + \frac{\Delta x_1}{2}, \ldots, x_M - \frac{\Delta x_M}{2} \leq X_M \leq x_M + \frac{\Delta x_M}{2}\right\}$$

• Ovviamente le definizioni di stazionarietà in senso lato e in senso stretto si estendono tal quali ai processi ampiezza continui.

---

## Pagina 158

Un esempio: Processi Gaussiani

- Un processo $X(t/n)$ si dice Gaussiano se un qualungue suo campione di dimensione $M$ definisce un vettore aleatorio $X$ Gaussiano.
- Dato un vettore aleatorio $X$ con media e matrice di covarianza assegnati:

$$\mu_X = \mathbb{E}[X] \quad C_X = \mathbb{E}\left[(X - \mu)(X - \mu)^T\right]$$

questo si dice Gaussiano se la sua pdf si scrive nella forma

$$\frac{1}{(2\pi)^{M/2}|C_X|^{1/2}} \exp \left[-\frac{1}{2}(x - \mu)^T C_X^{-1}(x - \mu)\right], \quad x \in \mathbb{R}^M$$

dove $|C_X|$ denota il determinante della matrice di covarianza.

---

## Pagina 159

Proprietà dei processi Gaussiani

• La stazionarietà in senso lato implica quella in senso stretto. Si verificchi questo asserto ricordando che nel caso di stazionarietà in senso lato la matrice di covarianza ha struttura Toeplitz;

• Chiusura rispetto a trasformazioni lineari. Se $X$ è un vettore Gaussiano, $X \sim \mathcal{N}(\mu, C)$, allora, avremo

$$Y = AX + u \sim \mathcal{N}\left(A\mu + u, ACA^T\right)$$

• Per un processo Gaussiano, incorrelazione implica indipendenza. Infatti, un processo incorrelato ha marice di covarianza $C = \text{diag}(\sigma_1^2, \ldots, \sigma_M^2)$. Sostituendo nella espressione di una pdf Gaussiana abbiamo

$$f_X(x) = \left( \prod_{i=1}^{M} \frac{1}{\sigma_i \sqrt{2\pi}} \right) \exp \left[ -\sum_{i=1}^{M} \frac{(x_i - \mu_i)^2}{2\sigma_i^2} \right] = \prod_{i=1}^{M} f_X_i(x_i)$$

---

## Pagina 160

Tipi di convergenza

• Sia $\{X_n\}$ una successione di variabili aleatorie con densità $\{f_{X_n}\}$ e CDF $\{F_{X_n}\}$.
• Ci chiediamo come definire la convergenza di tale successione a un dato limite, sia esso $X$.
• Ovviamente la forma più forte di convergenza è quella puntuale, vale a dire - ricordando che le variabili aleatorie sono in realtà funzioni - $\lim_n X_n(\omega) = X(\omega)$ $\forall \omega \in \Omega$, dove $\Omega$ è lo spazio dei campioni dello spazio di probabilità sottostante.
• Altre forme di convergenza più "deboli" (con diversa gradiazione) sono:

† La convergenza in distribuzione;
† La convergenza in probabilità;
† La convergenza in media quadratica;
† La convergenza quasi certa (o con probabilità 1);

---

## Pagina 161

Convergenza in distribuzione

• La successione $\{X_n\}$ si dice convergente in distribuzione alla variabile $X$ (e si scrive $X_n \xrightarrow{d} X$ se

$$\lim_{n \to \infty} F_X_n(x) = F_X(x),$$ per vettori: $$\lim_{n \to \infty} \mathbb{P}\{X_n \in A\} = \mathbb{P}\{X \in A\}, A \subseteq \mathbb{R}^M$$

dove l’uguaglianza vale in tutti gli insiemi di continuità di $F_X$.

• Il teorema cosiddetto del “continuous mapping” stabilisce che, se $g$ è una finzione continua, allora si ha:

$$X_n \xrightarrow{d} X \implies g(X_n) \xrightarrow{d} g(X)$$

• Il teorema di continuità di Levy stabilisce che, definendo la funzione generatrice dei momenti (moment generating function, mgf)

$$\Phi_n(s) = \mathbb{E}\left[e^{sX_n}\right] \quad \Phi_X(s) = \mathbb{E}\left[e^{sX}\right]

per i valori di $s$ per cui l’integrale esiste, la convergenza puntuale di $\Phi_n(s)$ a $\Phi(s)$ implica $X_n \xrightarrow{d} X$ e viceversa.

---

## Pagina 162

La funzione generatrice dei momenti

- La funzione generatrice dei momenti (moment generating function, mgf) di una variabile aleatoria gode di alcune rilevanti proprietà. Notiamo che

$$\Phi_X(s) = \int_{\mathbb{R}} e^{st} f_X(t) dt, \text{ con } f_X \text{ sommabile}$$

è funzione continua di $s$ nei punti in cui l'integrale esiste.

- Analogamente si può facilmente verificare che:

$$\Phi_X(0) = 1 \quad \Phi'(0) = \mathbb{E}[X] \quad \Phi''(0) = \mathbb{E}[X^2] \dots \Phi^{(r)}(0) = \mathbb{E}[X^r]$$

purchè i momenti di ordine $r$ esistano.

- Pertanto, nelle condizioni precedenti, la mgf ammette il seguente sviluppo in serie di Mc Laurin

$$\Phi_X(s) = \sum_{n=0}^{\infty} \frac{\mathbb{E}[X^n]}{n!} s^n$$

il che spiega il nome "mgf".

---

