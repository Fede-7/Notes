## Pagina 1

INTRODUZIONE AI LINGUAGGI DI PROGRAMMAZIONE

1.1 COS'È UN LINGUAGGIO DI PROGRAMMAZIONE

Un linguaggio di programmazione è un insieme di regole per comunicare idee. Con i linguaggi naturali, come l’inglese o l’italiano, questa comunicazione tra esseri umani e può essere svolta sia in maniera orale che in maniera scritta. I linguaggi di programmazione differiscono da quelli naturali in quanto la comunicazione avviene tra un essere umano e un calcolatore. La seconda differenza principale è il contenuto della comunicazione: i programmi. I programmi sono un modo di esprimere la soluzione per un determinato problema. La terza differenza sta nel mezzo attraverso il quale avviene la comunicazione tra il programmatore e il calcolatore. Dato che un computer è solitamente il destinatario della comunicazione, i programmi devono essere rappresentati obbligatoriamente come stringhe di caratteri.

Linguaggio di programmazione

Un linguaggio di programmazione è un linguaggio che deve essere usato da una persona per esprimere un processo attraverso il quale un calcolatore può risolvere un problema.

I quattro termini chiave presenti in questa definizione di linguaggio di programmazione sono i seguenti:

1. **Processore:** è la macchina che eseguirà il processo descritto dal programma; non si deve intendere come un singolo oggetto, ma come una architettura di elaborazione.

2. **Programma:** è l’espressione codificata di un processo.

3. **Persona:** il programmatore che desidera comunicare col calcolatore.

4. **Problema:** il sistema o ambiente che il processo deve modellare.

È uso comune intendere come linguaggi di programmazione solo quelli **computazionalmente completi**, cioè quelli che possono programmare qualsiasi **funzione calcolabile**. Questi vengono anche detti **general purpose** in quanto sono in grado di poter simulare qualunque **macchina di Turing**. Sono linguaggi completi solo quelli che riescono ad esprimere anche programmi di cui non è decidibile la terminazione.

Osservazione

Il linguaggio SQL puro non è un linguaggio completo poiché la terminazione dei programmi è sempre decidibile. Ana-logamente, il linguaggio HTML non è un linguaggio computazionalmente completo in quanto manca della capacità di eseguire calcoli o implementare logica condizionale.

---

## Pagina 2

Macchina astratta

Dato un linguaggio di programmazione $L$, una macchina astratta per $L$ (in simboli $M_L$) è un qualsiasi insieme di strutture dati e algoritmi che permettono di memorizzare ed eseguire i programmi scritti in $L$.

Le componenti chiave di una macchina astratta sono:

1. La **memoria:** rappresenta lo spazio in cui vengono memorizzati i dati, le variabili, i programmi e altri elementi necessari per l’esecuzione del software. Questa memoria può essere suddivisa in diverse aree, come memoria volatile (RAM) e memoria non volatile (disco rigido), e può includere variabili, costanti, strutture dati e altro ancora.

2. Il **processore:** rappresenta l’elemento di calcolo che esegue le istruzioni del programma. Le istruzioni vengono lette dalla memoria e interpretate o eseguite dal processore. Il processore può includere registri, una ALU (unità aritmetica e logica), un’unità di controllo e altre componenti che gestiscono il flusso di esecuzione del programma.

Figura 1.1: Struttura di una macchina astratta

Figura 1.2: Ciclo di esecuzione all’interno di un processore di una macchina astratta

---

## Pagina 3

Una macchina astratta può essere implementata in tre modi principali: hardware, software o firmware. L’implementazione hardware coinvolge la creazione di un dispositivo fisico dedicato per eseguire programmi specifici. L’implementazione software comporta la scrittura di un programma o interprete che simula il comportamento della macchina astratta su un computer generale. L’implementazione firmware è una via intermedia, in cui il software è incorporato in un dispositivo hardware specifico e spesso controlla funzionalità hardware specifiche. La scelta tra queste opzioni dipende dalle esigenze del progetto, dalle prestazioni richieste e dalla flessibilità desiderata.

1.3 LA TRADUZIONE DEI LINGUAGGI DI PROGRAMMAZIONE

Lo scopo di ogni linguaggio è la comunicazione tra due parti, un mittente e un destinatario. Con i linguaggi naturali, la comunicazione è tra due persone le quali in maniera alternata si inviano dei messaggi scambiandosi di volta in volta i ruoli. Con i linguaggi di programmazione, la comunicazione tra il programmatore e il calcolatore viene svolta mediante un programma di traduzione del linguaggio. Lo scopo di questo programma è quello di prendere in carico un processo descritto in un determinato linguaggio di programmazione e tradurlo in una sequenza di byte comprenibili dalla macchina.

Esistono due approcci fondamentali per tradurre un linguaggio:

1. Compilazione
2. Interpretazione

I programmi di traduzione che seguono il primo approccio vengono chiamati **compilatori**, mentre i secondi **interpreti**. Mentre un interprete traduce ed esegue un costrutto alla volta (vedi lo schema in Figura 1.3), un compilatore prima traduce l’intero programma e poi esegue la sua versione tradotta.

Figura 1.3: Processo di interpretazione

1.3.1 Il processo di compilazione

Lo scopo di un compilatore è quello di tradurre un programma scritto in un linguaggio di programmazione in un programma equivalente espresso in un linguaggio eseguibile direttamente dalla macchina. Questi due programmi sono chiamati rispettivamente **programma sorgente** e **programma oggetto**.

Il linguaggio del programma oggetto viene detto **linguaggio macchina**, **linguaggio oggetto o linguaggio target**. La Figura 1.5a mostra uno schema del processo di compilazione nel caso semplice, dove il programma oggetto è direttamente eseguibile. Il tempo durante il quale il compilatore è in esecuzione è noto come **tempo di compilazione**. Il tempo durante il quale viene invece eseguito il programma oggetto viene chiamato **tempo di esecuzione o run time**.

Il processo di compilazione può essere suddiviso in varie fasi. Seguendo lo schema mostrato nella Figura 1.4, il programma passa attraverso tre fasi intermedie: la **stringa di token**, il **parse tree** e il **programma astratto**.

---

## Pagina 4

Figura 1.5: Tipologie di compilazione

---

## Pagina 5

Lo scopo principale di un linguaggio di programmazione è quello di aiutare il programmatore all’interno del processo di sviluppo. Questo deve includere l’assistenza durante la fase di progettazione, implementazione, testing, verifica e mantenimento del software. Ci sono numerose proprietà di un linguaggio di programmazione che possono contribuire a questo scopo.

1.4.1 Semplicità

Un linguaggio di programmazione dovrebbe sforzarsi di essere semplice da usare sia sotto il punto di vista della semantica che quello della sintassi.

- **Semplicità semantica:** numero minimo di concetti e strutture;
- **Semplicità semantica:** unica rappresentabilità di ogni concetto.

Un linguaggio troppo coinciso, però, non è detto possa essere facile da leggere e quindi da capire. Un buon linguaggio di programmazione deve quindi cercare di trovare un compromesso tra questi due poli.

1.4.2 Astrazione

Un’astrazione è una rappresentazione di un oggetto che include solo gli attributi rilevanti dell’oggetto originale, ignorando tutti gli attributi irrilevanti. L’abilità di un linguaggio di programmazione di esprimere e usare l’astrazione è importante sia a livello della rappresentatività dei dati che a livello procedurale. Per quanto riguarda i dati, l’astrazione permette al programmatore di poter lavorare in maniera più semplice usando astrazioni più semplici che non includono dettagli irrilevanti del modello. A livello procedurale invece, l’astrazione facilita la progettazione e la modularità del codice.

1.4.3 Espressività

L’espressività si riferisce alla facilitità con cui un oggetto può essere rappresentato. In relazione ai linguaggi di programmazione, ciò significa che il linguaggio deve consentire la rappresentazione naturale sia degli oggetti dati che delle procedure. Strutture di dati e strutture di controllo adeguate ne sono un esempio adeguato. L’espressività può andare in conflitto però con la semplicità poiché maggiore il linguaggio è espressivo e maggiore sarà la complessità del linguaggio.

1.4.4 Ortogonalità

La semplicità richiede che un linguaggio incorpori il minor numero possibile di concetti. L’espressività richiede che i concetti corrispondano strettamente agli oggetti che rappresentano, mentre l’astrazione elimina i dettagli irrilevanti. L’ortogonalità si riferisce all’interazione tra i concetti, vale a dire al grado in cui concetti diversi possono essere combinati tra loro in modo coerente. Le violazioni dell’ortogonalità si verificano quando due concetti non possono interagire tra di loro o quando interagiscono in modo non coerente con le loro.

1.4.5 Portabilità

La possibilità di manutenere dei programmi è influenzata da tutte le quattro proprietà precedenti, nel senso che tutte favoriscono la facilitità di comprensione e di modifica dei programmi. Un problema di manutenzione importante che queste caratteristiche non affrontano è lo spostamento di un programma da un computer ad un altro. La portabilità di un linguaggio è molto maggiore quando esiste uno standard indipendente dalla macchina per quel linguaggio.

1.5 I PARADIGMI COMPUTAZIONALI

Un paradigma di programmazione è un modello che permette di descrivere astrattamente l’algoritmo (cioè il metodo di soluzione di un problema).

I principali paradigmi di programmazione sono:

- **Imperativo:** basato sul punto di vista del calcolatore. Ciò si riflette nell’esecuzione sequenziale dei comandi e nell’uso di una memoria modificabile, concetti che si basano sul modo in cui i computer eseguono i programmi a livello di linguaggio macchina. Il paradigma imperativo è stato il paradigma predominante per i linguaggi, in quanto tali linguaggi sono più facili da trasporre in una forma adatta all’esecuzione meccanica. Il programma di questo modello consiste in una sequenza di modifiche alla memoria del computer.

---

## Pagina 6

• **Funzionale:** il modello funzionale si concentra sul processo di risoluzione del problema. Il punto di vista funzionale si traduce in programmi che descrivono le operazioni che devono essere eseguite per risolvere il problema.

• **Logico:** Il modello orientato alla logica è più strettamente legato alla prospettiva della persona. Il programma è una descrizione logica del problema espressa in modo formale, simile al modo in cui un cervello umano ragionerebbe sul problema.

• **Orientato agli oggetti:** Il modello orientato agli oggetti riflette più fedelmente il problema reale. Un programma in questo modello consiste in oggetti che si inviano messaggi l’un l’altro. Gli oggetti del programma corrispondono direttamente a oggetti reali, come persone, macchine, reparti, documenti e così via.

• **Parallelo:** programmi che descrivono entità distribuite che sono eseguite contemporaneamente ed in modo asincrono.

Gli ultimi due paradigmi sono *ortogonali* rispetto ai primi tre.

**Esempio**

Il listato 1.1 mostra un esempio di definizione di funzione che calcola il fattoriale di un intero $n$. Sfruttando la possibilità di poter accedere direttamente alla memoria, modificandone il valore, i programmi imperativi sono caratterizzati dal forte uso delle **assegnazioni** e dell’approccio iterativo. Al contrario, un programma scritto secondo il paradigma funzionale non può eseguire assegnazioni in memoria. Il programma nel Listato 1.2 definisce la stessa funzione per il calcolo del fattoriale senza eseguire assegnazioni.

```c
int factI(int n)
{
    int result = 1;
    for(int i=1, i≤n, i++)
        result = result*i;
    return result;
}
```

**Codice 1.1: Paradigma imperativo**

```c
int factR(int n)
{
    if(n==1)
        return 1;
    else
        return n*factR(n-1);
}
```

**Codice 1.2: Paradigma funzionale**

---

## Pagina 7

IL PARADIGMA IMPERATIVO

2.1 PERCHÉ IMPERATIVO?

Il modello imperativo fu creato per imitare, il più fedelmente possibile, le azioni che vengono eseguite dal calcolatore a livello del linguaggio macchina. A quel livello, i calcolatori operano con due unità principalemente:

• La CPU, dove vengono eseguiti tutti i calcoli;

• La memoria, dove i dati vengono conservati. Questa consiste in un insieme di “contentitori di dati” come le parole della memoria centrale. Queste sono tipicamente rappresentate dal loro indirizzo. A ciascun indirizzo viene associato successivamente un valore. Concettualmente la memoria è una funzione da uno spazio di locazioni ad uno spazio di valori:

$$\text{mem} : \text{Locazioni} \rightarrow \text{Valori}$$

(2.1)

La tipica unità di esecuzione nel linguaggio macchina consiste nei seguenti quattro passi:

1. Recupero dell’indirizzo della locazione per il risultato e dei vari operandi
2. Recupero dei valori dalle locazioni degli operandi;
3. Calcolo dell’espressione;
4. Memorizzazione del risultato nella sua locazione.

Al centro di questi passi sta il concetto di assegnazione. Il modello imperativo usa dei nomi, le variabili, come astrazione degli indirizzo di locazioni di memoria. La forma BNF¹ di questo tipo istruzione è la seguente:

$$\text{assegnazione} ::= \text{name} <\text{assignment-operator}><\text{expression}$$

dove <name> rappresenta il nome della variabile, ovvero un segnaposto per la locazione dove viene memorizzato il risultato dell’assegnazione mentre in <expression> sopo specificati una computazione e i riferimenti ai valori necessari a tale computo.

Esempio

Si consideri il seguente listato:

1 a := b+c;

Codice 2.1: Esempio di assegnazione in Pascal

In questo caso l’assegnazione prevede la somma dei valori presenti nelle variabili b e c e infine il salvataggio di tale espressione nella cella di memoria indicata dalla variabile a.

¹La BNF (Backus-Naur Form o Backus Normal Form) è una metasintassi, ovvero un formalismo attraverso cui è possibile descrivere la sintassi di linguaggi formali (il prefisso meta ha proprio a che vedere con la natura circolare di questa definizione). Si tratta di uno strumento molto usato per descrivere in modo preciso e non ambiguo la sintassi dei linguaggi di programmazione, dei protocolli di rete e così via, benché non manchino in letteratura esempi di sue applicazioni a contesti anche non informatici e addirittura non tecnologici. La BNF viene usata nella maggior parte dei testi sulla teoria dei linguaggi di programmazione e in molti testi introduttivi su specifici linguaggi.

---

## Pagina 8

Ambiente di esecuzione

Si definisce ambiente l’insieme di nomi di variabili (non gli indirizzi, piuttosto i loro identificatori) e parametri associati a qualcosa dal quale si più risalire al valore (all’interno del programma) della variabile o del parametro.

Concettualmente l’ambiente è una funzione il cui dominio è dato dall’insieme di identificatori (i nomi) mentre il codominio dipende dal paradigma computazione del linguaggio. Nel paradigma imperativo, la funzione env associa gli identificatori a locazioni di memoria, le quali, a loro volta, sono associate mediante la funzione mem al contenuto di memoria:

$$env : Identificatori \rightarrow Locazioni$$

(2.2)

Di conseguenza il valore di una variabile x sarà data da:

$$mem(env(x))$$

Ovvero, data una variabile x, ne recuperiamo la locazione ad essa associata e di questa locazione ne leggiamo il contenuto in memoria.

Esempio

Si consideri la seguente assegnazione:

$$1 \ x := x+1;$$

La variabile che compare a sinistra dell’assegnazione indica la locazione dove salvare il risultato, ovvero l’ambiente del nome x:

$$env(x)$$

A destra dell’espressione, invece, il nome della variabile x indica il valore da utilizzare all’interno dell’espressione che verrà poi memorizzata:

$$mem(env(x)) + 1$$

Nel paradigma funzionale non esiste la funzione mem e la funzione env ha come codominio direttamente l’insieme dei valori. Qualsiasi sia il paradigma computazione, però, il valore env(x) è immutabile finché esiste l’identificatore x.

Paradigma imperativo

Nel paradigma imperativo l’ambiente mappa gli identificatori sulla loro locazione di memoria. Sarà poi attraverso la funzione memory che si potrà accedere al valore in essa conservato.

Paradigma funzionale

Nel paradigma funzionale gli environment mappano gli identificatori direttamente sul loro valore invece di una locazione di memoria (il cui contenuto può cambiare).

Figura 2.1: Confronto tra paradigma imperativo e paradigma funzionale

Nel paradigma imperativo, quindi, la locazione di memoria associata ad un nome non può cambiare all’interno di un blocco di esecuzione. Anche nel paradigma funzionale puro l’associazione identificatore-valore non cambia mai.

---

## Pagina 9

Esempio

Si consideri la seguente porzione di codice:

```c
int *x,y;
x=&y;
```

In questo caso abbiamo un puntatore x e una variabile di tipo intero y. Effettuare l’assegnamento x=&y significa far puntare da x la cella della variabile y, sarà allora:

$$mem(env(x)) = env(y)$$

Non è possibile fare assegnazioni come mostrato di seguito:

```c
int x,y;
&y = x;
```

Un programma del genere infatti genererebbe un errore simile:

**error:** l'value required as left operand of assignment

A sinistra dell’assegnazione infatti abbiamo una espressione del tipo `env(env(y))` che è chiaramente malformata.

Per non incorrere in errori simili ricordiamo che a sinistra di una assegnazione si possono trovare solo i nomi di variabili oppure, nel caso di puntatori, espressioni del tipo:

*(<pointer expression>)

Ovvero il valore (l’indirizzo) salvato all’interno di un puntatore. Queste espressioni prendono il nome di l'value. Reciprocamente, le espressioni che si trovano a destra di una assegnazione prendono il nome di rvalue. Come esempio, consideriamo l’assegnazione:

$$*(x+2)=\dots$$

che avrà come traduzione una formula del tipo:

$$mem(env(x)) + 2 = \dots$$

Consideriamo il caso:

```c
int *x,y;
y=*x;
```

Si ha in questo caso: `env(y) = mem(mem(env(x)))`. Nel caso invece si avesse avuto l’assegnazione:

$$*x=y;$$

si sarebbe avuto: `mem(env(x)) = mem(env(y))`. Infatti, in C, l’operatore di dereferenziazione indica la cella di memoria il cui indirizzo è memorizzata nella variabile x. Si consideri la porzione di codice:

```c
int x,y;
x = &y;
```

In questo caso il compilatore segnala un warning del tipo:

**warning:** assignment to 'int' from 'int*' makes integer from pointer without a cast.

In quanto si sta tentando di assegnare un indirizzo (&y = env(y)) ad una variabile di tipo intero.

---

## Pagina 10

Tabella 2.1: "In un vettore possiamo usare sia la notazione indicizzata sia l’aritmetica dei puntatori. Si consideri un vettore di interi dichiarato come `int a[10]`. Nonostante si possano usare entrambe le notazioni bisogna ricordare che il nome di un vettore non è un puntatore. Il nome di un vettore identifica infatti l’indirizzo (l’ambiente) della prima cella dell’array."

| Descrizione | Notazione indicizzata | Notazione puntatori | Espressione lvalue | Espressione rvalue |
| :--- | :--- | :--- | :--- | :--- |
| Valore del primo elemento dell’array | `a[0]` | *a | `env(a)` | `mem(env(a))` |
| Indirizzo del primo elemento dell’array | `&a[0]` | a | Not an lvalue | `env(a)` |
| Valore dell’i-esimo elemento dell’array | `a[i]` | *(a+i)` | `env(a) + mem(env(i))` | `mem(env(a) + mem(env(i)))` |
| Indirizzo dell’i-esimo elemento dell’array | `&a[i]` | a+i | Not an lvalue | `env(a) + mem(env(i))` |

---

## Pagina 11

Esempio (Array e puntatori)

Supponiamo di avere un array di interi:

```python
int v[3];
```

In questo caso l’espressione `env(v)` indica la prima cella del vettore `v`:

```python
env(v)
v[0] v[1] v[2] — Celle
```

Si consideri la seguente porzione di codice:

```python
v = v+1;
```

In casi come questi il compilatore restituisce un errore del tipo:

**error:** assignment to expression with array type

Questo perché si sta provando a modificare il valore dell’ambiente della variabile `V`. Consideriamo l’assegnamento:

```python
y=v[1];
```

In questo caso avremo a sinistra `env(y)` mentre a destra sarà necessario accedere alla seconda cella di memoria sommando un offset di una posizione all’indirizzo salvato in `v` e successivamente leggere il contenuto di tale cella: `mem(env(v)+1)`.

Sia ora:

```python
v[1]=y;
```

In questo caso si ha a sinistra l’espressione `env(v)+1`, che esprime l’indirizzo della seconda cella di memoria, mentre a destra si avrà `mem(env(y))`.

Sia `x` un puntatore e consideriamo l’assegnamento:

```python
y=x[1]+v[1];
```

In questo caso si vuole salvare all’interno della variabile `y` il valore ottenuto dalla somma tra il secondo elemento dell’array puntato da `x` e il secondo elemento dell’array `v`. Si avrà quindi in questo caso:

$$env(y) = mem(mem(env(x)) + 1) + mem(env(v) + 1)$$

Da notare qui il differente uso delle funzioni `mem` ed `env` nel caso in cui queste vengano applicate ad un puntatore o direttamente ad un vettore. Infatti, nel caso di un puntatore sarà necessario prima leggere la cella di memoria del puntatore per risalire all’indirizzo della prima cella del vettore puntato, sommare l’offset e infine leggere il valore della cella così ottenuto. Nel caso del vettore, invece, è sufficiente sommare l’offset direttamente alla quantità `env(v)`, che contiene già l’indirizzo della prima cella del vettore, e infine applicare la funzione `mem`.

Consideriamo il caso in cui si voglia usare un puntatore a sinistra di un assegnamento:

```python
x[1]=y;
```

Si ha in questo caso si vuole assegnare il valore della variabile `y all’interno della seconda cella dell’array puntato da `x`. Si ha quindi:

$$mem(env(x)) + 1 = mem(env(y))$$

Consideriamo ora il caso dell’assegnamento:

```python
y=*x+*y;
```

In questo caso si vuole salvare in `y` il valore della cella puntata da `x` e del primo elemento del vettore `v`. Infatti, in un vettore, sono simili le scritture `v[0]` e *v* in quanto entrambe fanno riferimento al valore della prima cella (si osservi la Tabella 2.1). Si ha quindi:

$$env(y) = mem(mem(env(x))) + mem(env(y))$$

Mentre, avessimo avuto:

---

## Pagina 12

Ogni variabile, parametro od oggetto può essere rappresentato mediante un **data object**.

**Data Object**

Un **data object** è una quadrupla $(L, N, V, T)$, dove:
- L: locazione;
- N: nome;
- V: valore;
- T: tipo.

**Binding**

Un **legame** $(\text{binding})$ è la determinazione di una delle componenti di un data object. Si distinguono quindi in legami di locazione, di nome, di valore e di tipo.

**Osservazione**

Nel paradigma imperativo il legame di locazione corrisponde alla funzione *env* mentre risalire al legame di valore di una variabile di nome $x$ corrisponde al calcolo della funzione *mem(env(x))*.

La Figura 2.2 mostra una visualizzazione di un data object e dei suoi legami. Le quattro linee si dipartono dal data object fino ai relativi spazi di arrivo. Lo **spazio di memoria** dal quale sono selezionati i legami di locazione è l’insieme delle locazioni di memoria virtuali disponibili nel momento in cui il programma è in esecuzione.

Il momento in cui questi legami possono avvenire rappresenta un’informazione importante nel momento in cui si parla di linguaggi di programmazione:

1. **Tempo di compilazione**: quando il programma viene tradotto in linguaggio macchina;
2. **Tempo di caricamento**: quando il programma in linguaggio macchina viene assegnato a specifiche locazioni di memoria all’interno della memoria;
3. **Tempo di esecuzione**: quando il programma viene eseguito.

Il **location binding** avviene durante il caricamento in memoria, oppure a run time. Il **name binding** avviene durante la compilazione, nell’istante in cui il compilatore incontra una dichiarazione. Il **type binding** avviene di solito durante la compilazione, nell’istante in cui il compilatore incontra una dichiarazione di tipo. Un tipo è definito dal sottospazio di valori (e dai relativi operatori) che un data object può assumere. Quando i legami avvengono a tempo di compilazione (immutabili) si è soliti segnalarlo **evidenziando in grassetto la linea** mentre i legami che possono essere modificati a tempo di esecuzione sono descritti da linee sottili.

**Figura 2.2**: Visualizzazione concettuale di un data object

---

## Pagina 13

Esempio

Si consideri la seguente assegnazione:

1. A: integer;

il data object A avrà una raffigurazione come mostrato nella Figura 2.3. Inizializzando la variabile si avrà un’assegnazione di tipo a tempo di compilazione mentre il legame di valore avviene a tempo di load time:

1. B: integer := 1;

il data object B avrà una rappresentazione come mostrato in Figura 2.4. Solo dichiarando una costante si può avere un legame di tipo e valore a tempo di compilazione (si veda la Figura 2.5):

1. C: constant integer := 1;

2.3.1 I puntatori

Il data object dei puntatori si differenzia da quelli per gli altri tipo di dato (che hanno un nome, un valore e una singola locazione) per il fatto di coinvolgere ben due data object. Infatti, il valore di un data object di tipo puntatore èesso stesso la locazione di un altro data object il quale può non avere un legame di nome o di valore (come nel caso di allocazione dinamica mediante malloc in C). La definizione di una variabile puntatore è mostrata nella Figura 2.6.

I due data object coinvolti sono quindi:

1. Il data object del puntatore (Data Object 1);
2. Il data object della variabile puntata o dello spazio di memoria puntato (Data Object 2).

---

## Pagina 14

Nel caso del puntatore, il data object è legato a un nome e ad una locazione come per gli altri tipi. Il valore legato ad un data object di tipo puntatore, tuttavia, è un elemento dello spazio di memoria. Come per gli altri tipi, i legami di tipo e di nome si verificano al momento della compilazione, il legame di locazione si verifica al momento del caricamento mentre il legame di valore in tempo di esecuzione.

L’oggetto puntato (Data Object 2) è molto diverso da quelli che abbiamo visto in precedenza. Innanzitutto, notiamo che non ha alcun legame con lo spazio dei nomi. Infatti, non ci si riferisce ad esso mediante un suo identificatore bensi dal nome del puntatore legato adesso. In secondo luogo, i legami di posizione e di tipo di questo oggetto devono avvenire a tempo di esecuzione, dal momento che il data object stesso non esiste fino a quando non viene assegnato al puntatore come valore. In questo caso è necessaria la deallocazione della memoria in quanto la modifica del legame di valore genera di solito dati non più accessibili per nome o riferimento. Alcuni linguaggi possiedono meccanismi di recupero automatico di memoria come il garbage collector.

2.3.2 Il legame di tipo

Sebbene i tipi siano legati ai data object in fase di compilazione nella maggior parte dei linguaggi, spesso è possibile che questo legame avvenga anche a tempo di esecuzione. I linguaggi APL e Smalltalk, ad esempio, implementano questo tipo di legame dinamico. Il tipo di un data object è determinato quindi dal tipo del suo valore. Pertanto, ogni volta che un data object viene legato a un valore diverso, assume il tipo del nuovo valore adesso associato. Considerando che le dichiarazioni sono usate per legare i data objects ai tipi in fase di compilazione, i linguaggi a tipizzazione dinamica non hanno bisogno di dichiarazioni.

Un linguaggio è detto dinamicamente tipizzato se il legame (e le variazioni di legame) e di conseguenza anche il controllo di consistenza (se avviene) avvengono durante il tempo di esecuzione. Un linguaggio invece è detto staticamente tipizzato se il legame avviene durante la compilazione. In questo caso il controllo di consistenza (se avviene) può avvenire in entrambe le fasi.

---

## Pagina 15

Type checking Il type checking è processo mediante il quale si determina il tipo di un data object controllando la consistenza della coppia valore-tipo. L’esecuzione di questo tipo di controllo da parte del calcolatore può essere di grande aiuto nel rilevamento e nella prevenzione degli errori.

Il type checking può avvenire a tempo di compilazione, di esecuzione, o non avvenire per nulla. I linguaggi che eseguono il controllo del tipo a tempo di compilazione vengono chiamati fortemente tipati. Il linguaggio Java è un esempio di linguaggio fortemente tipizzato. Il linguaggio Pascal è quasi fortemente tipizzato (una sola eccezione dei record di assenza di controllo: record con varianti).

Un linguaggio è detto debolmente tipizzato se il controllo di consistenza non avviene sempre. Il linguaggio C ne è un esempio. Infatti in esso esiste la possibilità di eseguire operazioni di casting, che consentono di forzare, in esecuzione, l’interpretazione di un qualunque valore secondo un qualunque tipo (anche un tipo diverso da quello a cui il valore è stato precedentemente associato).

Type equivalence All’inizio dell’informatica esistevano solo i tipi elementari. Successivamente sono stati introdotti i tipi definiti dall’utente i quali erano semplici ridenominazioni di tipi elementari oppure nomi di record.

A stabilire se un assegnamento del tipo x=y fosse valido stava alla base il concetto di type equivalence adottata dal linguaggio. Esistono due forme di equivalenza:

1. **Name equivalence:** i tipi di x e y devono avere lo stesso nome, ovvero lo stesso tipo;
2. **Structural equivalence:** i tipi di x e y devono avere la stessa rappresentazione interna. Apparentemente più snello e flessibile ma aumenta la possibilità di errori.

Esempio

Il linguaggio Pascal adotta il name equivalence mentre il linguaggio C/C++ entrambi i tipi (quasi sempre structural tranne che per le struct):

```c
typedef int money;
typedef int apples;

typedef struct{int a;} S1;
typedef struct{int a;} S2;

int main(){
    money x = 0;
    apples y = 0;
    int z = x+y; // Non fa una piega
    S1 a;
    S2 b;
    a = b; // Questo non lo compila
}
```

questo perché verificare se due struct sono strutturalmente equivalenti richiede di verificare una proprietà chiamata bisimulazione.

Con l’avvento dei linguaggi a oggetti il concetto di equivalenza viene rimpiazzato dal concetto di compatibilità. Nei linguaggi object oriented più comuni la compatibilità è basata sul nome piuttosto che la struttura. Di conseguenza due classi con nomi diversi sono diverse anche se hanno gli stessi attributi e gli stessi metodi. Inoltre, una classe per essere sottotipo di un’altra deve essere esplicitamente dichiarata tale mediante il costrutto extends.

2.4 BLOCCHI DI ISTRUZIONE

Le unità di esecuzione sono gruppi di istruzioni che sono raggruppate insieme per uno scopo preciso. L’unità più grande è il programma stesso, questo è poi suddiviso in blocchi di istruzioni. Ci sono vari motivi per avere diversi blocchi d’istruzione all’interno di un programma. Questi servono infatti a definire meglio:

1. L’ambito delle strutture di controllo;
2. L’ambito di una procedura;
3. Unità di compilazione separate;
4. L’ambito dei legami di nome.

---

## Pagina 16

2.4.1 Ambito del name binding

I blocchi che definiscono l’ambito di validità di un nome contengono due parti: una sezione di dichiarazione del nome e una sezione che comprende gli enunciati sui quali ha validità il legame. Dal punto di vista sintattico, questo richiede di solito un marcatore per l’inizio della sezione di dichiarazione, un marcatore che separa la sezione di dichiarazione dalle dichiarazioni e un marcatore che indica la fine del blocco. Svilupperemo un piccolo pseudolinguaggio simile al Pascal per esprimere gli esempi in questa sezione. Questo pseudolinguaggio userà BLOCK per iniziare il blocco, BEGIN per separare le dichiarazioni dagli enunciati e END per indicare la fine del blocco. La struttura generale di un un blocco nel nostro pseudolinguaggio sarà quindi come mostrato nel Listato 2.2. L’istruzione DECLARE in questo esempio viene utilizzata per legare il nome I a un data object all’ingresso del blocco A. In questo caso, il riferimento a I è al legame fatto nel blocco A.

All’interno di ogni blocco, esistono due tipi di visibilità:

• locale: per le variabili specificate all’interno del blocco;
• non locale: per le variabili specificate all’esterno del blocco.

Anche se alcuni linguaggi richiedono una dichiarazione separata dei legami che sono ereditati dal blocco corrente, è consuetudine che un blocco erediti direttamente i legami dall’ambiente che lo contiene. Questo è particolarmente utile quando si ha a che fare con blocchi annidati.

```program
PROGRAM P;
DECLARE X;
BEGIN P
... {X from P}
BLOCK A;
DECLARE Y;
BEGIN A
... {X from P, Y from A}
BLOCK B;
DECLARE Z;
BEGIN B
... {X from P, Y from A, Z from B}
END B;
... {X from P, Y from A}
END A;
... {X from P}
BLOCK C;
DECLARE Z;
BEGIN C
... {X from P, Z from C}
END C;
... {X from P}
END P;
```

Codice 2.3: Blocchi annidati

Nell’esempio mostrato nel Listato 2.3 si vede come ciascun blocco erediti i legami dall’ambiente all’interno del quale è stato definito.

Questo tipo di politica di scoping viene anche chiamata **scoping lessicale o scoping statico** e può essere sintetizzare come segue:

1. Se un nome ha una dichiarazione all’interno del blocco, quel nome è legato all’oggetto specificato nella dichiarazione;
2. Se un nome non ha una dichiarazione all’interno di un blocco, il nome è legato allo stesso oggetto a cui era legato nel blocco che lo contiene. Se il blocco non ha un blocco contenente o il nome non è vincolato nel blocco contenente, allora il nome è svincolato nel blocco attuale.

Un’alternativa allo scoping statico è lo **scope dinamico** che assume senso maggiore quando vi sono procedure chiamanti e chiamate. In questo caso la procedura chiamata vede e usa i legami visti e usati dalla procedura chiamante.

---

## Pagina 17

Il mascheramento Una situazione nota come mascheramento avviene quando un blocco ridefinisce un nome già vincolato ad un oggetto dell’ambiente circostante. In questo caso, la dichiarazione locale sovrascrive il legame non locale rendendo il data object precedentemente dichiarato irraggiungibile nel blocco corrente.

```prolog
PROGRAM P;
DECLARE X,Y;
BEGIN P
... {X from P, Y from P}
BLOCK A;
DECLARE X,Z;
BEGIN A
... {X from A, Y from P, Z from A}
END A;
... {X from P, Y from P}
END P;
```

Codice 2.4: Mascheramento

2.4.2 Ambito del location binding

I legami di locazione possono essere **statici** e **dinamici**. Gli unici linguaggi dove tutti i legami di memoria venivano fatti staticamente erano quelli arcaici come il primo Fortran che non disponevano di memoria dinamica. Esempio di variabile con legame di tipo statico possono essere le variabili globali del linguaggio C.

Si dice **allocazione statica di memoria** quando le variabili conservano il proprio valore ogni volta che si rientra in un blocco. Il legame di locazione quindi viene fissato e resta costante al tempo di caricamento. Se un linguaggio prevede un legame del genere è possibile far funzionare programmi come quello mostrato nel Listato 2.5.

Si dice **allocazione dinamica di memoria** quando il legame di locazione (e anche di nome) è creato all’inizio dell’esecuzione di un blocco e viene rilasciato a fine esecuzione. Questo meccanismo è quello adottato comunemente nei linguaggi moderni e realizzato mediante i **record di attivazione** dei blocchi posti all’interno dello **stack di attivazione**. Un record di attivazione contiene tutte le informazioni sull’esecuzione del blocco necessarie per riprendere l’esecuzione dopo che essa è stata sospesa. Può contenere informazioni complesse ma per realizzare un legame dinamico di locazione in blocchi annidati è sufficiente che contenga le locazioni dei dati locali più un **puntatore al record di attivazione del blocco immediatamente più esterno**.

Codice 2.5: Allocazione statica di memoria

2.4.3 Lo stack di attivazione

In ogni momento dell’esecuzione lo stack di attivazione contiene sempre e solo i record “attivi”:

• Il top dello stack contiene sempre il record del blocco correntemente in esecuzione;
• Ogni volta che si entra in un blocco, il record di attivazione del blocco viene posto sullo stack (push);
• Ogni volta che si esce da un blocco, viene eliminato il record al top dello stack.

---

## Pagina 18

Esempio

Si consideri ad esempio il programma mostrato nel Listato 2.6. L’evoluzione dello stack di attività è mostrato nella Figura 2.7.

```prolog
PROGRAM P;
DECLARE I,J;
BEGIN P
  BLOCK A;
  DECLARE I,K;
  BEGIN A
  BLOCK B;
    DECLARE I,L:INTEGER;
    BEGIN B
      ...
      END B;
    ...
    END A;
  BLOCK C;
  DECLARE I,N;
  BEGIN C
    ...
    END C;
  ...
END P;
```

Codice 2.6: Esempio stack di attività

Figura 2.7: Contenuto dello stack di attività per il programma 2.6

---

