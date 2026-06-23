# Memoria Principale

## Obiettivo

- Fornire una descrizione dettagliata dei modi di organizzare l'**hardware di memoria**.
- Discutere le tecniche di gestione della memoria, inclusi il **paging** e la **segmentazione**.

## Background

- Un sistema di elaborazione esegue programmi.
- Per essere eseguito un programma deve essere portato (dal disco) in **memoria principale** e inserito all'interno di un processo.
- La memoria principale ed i registri sono la **sola memoria** a cui la CPU accede direttamente interpretando le istruzioni dei programmi.
- Tanti processi devono essere caricati (almeno parzialmente) in memoria contemporaneamente.

- La CPU carica le istruzioni indicate dal PC, decodifica ed esegue.
- La memoria principale può essere vista come un **grande array di bytes** con indirizzi.
- L'unità di memoria vede solo un flusso di indirizzi + richieste di lettura o indirizzo + dati e richieste di scrittura.

## Hardware

□ La memoria principale ed i registri sono la sola memoria a cui la CPU accede direttamente interpretando le istruzioni.

□ **Supporto hardware** per velocizzare l’accesso:
  □ L'accesso ai registri generalmente in un clock della CPU (in alcuni casi più operazioni in un ciclo).
  □ La memoria principale può richiedere molti cicli (**memory bus**), causando uno stallo in attesa del dato da elaborare.
  □ Accesso frequente, troppi stalli.
  □ **Cache** tra la memoria principale e i registri della CPU per accelerare.

□ **Protezioni hardware**:
  □ Necessaria protezione hardware della memoria per garantirne il corretto funzionamento (proteggere sistema e utenti).
  □ Il Sistema non interviene tra CPU e Memoria per non rallentare.

## Protezione: Registri Base e Limite

- In primo luogo occorre separare i processi in memoria.
- Una coppia di **registri CPU base e limite** definisce lo spazio degli **indirizzi logici** per un processo.
  - **Base**: il primo indirizzo fisico.
  - **Limite**: il range.
- La CPU deve controllare ogni accesso in memoria in *user mode* per verificare che sia tra gli indirizzi base e limite per quel processo.

Soluzione CDC 6600, Intel 8088 (non limite), Intel 80286.

## Protezione: Registri Base e Limite (Ripetizione)

- In primo luogo occorre separare i processi in memoria.
- Una coppia di **registri CPU base e limite** definisce lo spazio degli indirizzi logici per un processo.
- **Base**: il primo indirizzo fisico.
- **Limite**: il range.

## Protezione hardware degli indirizzi

Il controllo di accesso è **hardware**; se violato l’accesso si genera un **trap** che il Sistema Operativo considera come *fatal error*.

I registri possono essere caricati solo dal SO in **modalità privilegiata**, quindi solo in *kernel mode*.

In *kernel mode* il SO ha accesso non ristretto sia alla memoria di SO sia a quella degli utenti.

**图示：CPU处理地址判断逻辑**
- CPU处理地址判断逻辑
  - base
    - yes
    - no
  - base + limit
    - yes
    - no
- trap to operating system monitor—addressing error

## Programmi e Processi

- **Programmi su disco**:
  - file eseguibili pronti per caricamento ed esecuzione.

- **Programma caricato in memoria**:
  - La CPU può accedere a dati ed istruzioni.
  - Il processo può risiedere in ogni parte della memoria.

- **Processo termina**:
  - lo spazio di memoria viene reso disponibile.

## Processamento Multistep di Programma Utente

Un programma utente, prima di essere eseguito, deve passare attraverso varie fasi (alcune facoltative):

```monospace
gcc –E file.c
```
preprocessa ma non compila file.i

```monospace
gcc –S file.c
```
compila ma non assembla (assembly) file.s

```monospace
gcc –c file.c
```
compila e assembla non linka (file oggetto) file.o

## Binding di Istruzioni e Dati alla Memoria

□ Il **binding** (degli indirizzi di istruzioni e dati) agli indirizzi di memoria può avvenire in diverse fasi.

□ **Tempo di Compilazione**: se al momento della compilazione è già noto dove il processo risiederà in memoria si può generare codice assoluto; il codice va quindi ricompilato se la locazione di partenza viene modificate.

□ **Tempo di Caricamento**: si genera codice rilocabile se la locazione di memoria non è nota a tempo di compilazione; il collegamento finale viene ritardata finché non c’è il caricamento (**loader**). Se la locazione iniziale per il processo cambia occorre ricaricare il codice.

□ **Tempo di Esecuzione**: se durante l’esecuzione il processo può essere spostato da un segmento di memoria all’altro allora il binding è ritardato fino al run-time.
  ► Occorre supporto hardware speciale per mappare gli indirizzi.
  ► La maggior parte dei SO usa questo metodo.

## Indirizzi logici e fisici

La separazione tra **indirizzi logici** ed **indirizzi fisici** è centrale per la gestione della memoria.

- **Indirizzo logico**:
  - generato dalla CPU; anche chiamato **indirizzo virtuale**.

- **Indirizzo fisico**:
  - indirizzo visto dall’unità di memoria.
  - caricato nel registro di indirizzi di memoria (**memory-address register**).

**Indirizzi logici e fisici:**

- **Spazio degli indirizzi logici:** insieme di tutti gli indirizzi logici generati da un programma.
- **Spazio degli indirizzi fisici:** insieme di tutti gli indirizzi fisici che corrispondono ad uno spazio di indirizzi logici.

## Memory-Management Unit (MMU)

- **MMU** è un dispositivo hardware che **mappa a run-time** gli indirizzi virtuali in indirizzi fisici.
- Diversi schemi di mapping possono essere introdotti.
  - Un esempio di schema semplice è basato su registri base e limite.
  - In questo caso il registro di base è chiamato **registro di rilocazione**.

**Unità di gestione della memoria** (memory management unit, MMU) svolge l’associazione, **nella fase d’esecuzione**, tra indirizzi virtuali e indirizzi fisici.

**Figura 9.4** Unità di gestione della memoria (MMU).

## Memory-Management Unit (MMU) (Ripetizione)

- **MMU** è un dispositivo hardware che **mappa a run-time** gli indirizzi virtuali in indirizzi fisici.
- Diversi schemi di mapping possono essere introdotti.
  - Un esempio di schema semplice è basato su registri base e limite.
  - In questo caso il registro di base è chiamato **registro di rilocazione**.

**Unità di gestione della memoria** (memory management unit, MMU) svolge l’associazione, **nella fase d’esecuzione**, tra indirizzi virtuali e indirizzi fisici.

## Memory-Management Unit (MMU) (Dettagli Tecnici)

□ MMU è dispositivo hardware che mappa a run time gli indirizzi virtuali in indirizzi fisici.
□ Diversi metodi sono possibili per fare il mapping.
□ Un esempio di schema semplice è basato su registri base e limite:
  ► il valore nel registro di rilocazione è addizionato all’indirizzo generato dal processo utente.
  ► Registro base chiamato ora **relocation register**.

► Es. CPU considera 346 (logico) che viene mappato su 14346.
► MS-DOS su Intel 80x86 usava 4 relocation registers.

## Memory-Management Unit (MMU) (Concetti Chiave)

- **MMU** è dispositivo hardware che mappa a run-time gli indirizzi virtuali in indirizzi fisici.

- Il processo utente vede solo gli indirizzi logici, **non vede mai gli indirizzi fisici reali**.

  - Es. Può gestire un puntatore, manipolarlo etc. rimanendo nello spazio logico.
  - Il binding a tempo di esecuzione occorre solo quando si accede ad una locazione di memoria fisica. In questo caso l’hardware per il mapping in memoria converte l’indirizzo virtuale in indirizzo fisico.
  - Il processo utente lavora nello spazio di indirizzi logici (es. intervallo [0, max]) che in memoria saranno mappati in indirizzi fisici (es. [R, R + max]).

## Allocazione Contigua di Memoria

- La memoria principale deve supportare sia i processi di sistema che di utente.
- Memoria principale di solito divisa in due parti:
  - **Sistema Operativo residente** tenuto in memoria alta o bassa.
    - Linux e Win in memoria alta.
  - **Processi utente** in memoria bassa o alta.
    - Assumiamo bassa.

- Più processi devono essere portati in memoria contemporaneamente.
- **Allocazione contigua** è tra i primi metodi impiegati.
  - Processi successivi caricati in sezioni contigue di memoria.
    - Ogni processo contenuto in una singola e contigua sezione della memoria.
    - Necessari meccanismi di protezione della memoria dei processi.

## Protezione

- **Registro di rilocazione** usato per proteggere i processi utente l’uno dall’altro e per impedire il cambiamento di codice e dati di SO.
  - Registro base contiene il valore dell’indirizzo fisico più basso.
  - Registro limite contiene il range di indirizzi logici – ogni indirizzo logico deve essere minore del limite.
  - MMU mappa dinamicamente gli indirizzi logici.
  - Dispatcher carica processo insieme ai registri limite e relocation (**contex switch**).
  - Anche la dimensione del SO può variare dinamicamente.

## Allocazione con Partizioni Multiple

### Partizioni multiple di dimensione variabile

- Partizioni di **dimensione variabile** dove ciascuna partizione può contenere esattamente un processo.
- Tra i metodi più semplici per l’allocazione della memoria.

## Allocazione con Partizioni Multiple (Dettagli)

### Partizioni multiple di dimensione variabile

- Ciascuna partizione può contenere esattamente un processo.

Il SO mantiene traccia delle partizioni occupate.
- **Hole** – blocco di memoria disponibile.
- Inizialmente tutta la memoria è disponibile (unico hole).
- Quando un processo arriva, è allocato in un hole largo abbastanza per gestirlo.
- I processi uscenti liberano le partizioni e le partizioni libere adiacenti sono combinate in una sola.

Il SO mantiene informazione su:
  a) partizioni allocate.
  b) partizioni libere (hole).

**Grado di multiprogrammazione** limitato dal numero di partizioni disponibili.

## Allocazione con Partizioni Multiple (Strategie)

### Partizioni multiple di dimensione variabile

- Allocati gli hole dimensionati sui bisogni del processo.

- Se non c’è spazio sufficiente il processo può essere respinto o messo in attesa.
- Se il buco è grande viene diviso allocandone una parte e rilasciandone una parte libera.
- Ma come scegliere gli hole da allocare?

## Problema di Allocazione con Storage Dinamico

Come soddisfare una richiesta di dimensione $n$ da una lista di hole liberi?

☐ **First-fit**: Alloca il primo hole libero che è grande abbastanza.
  ☐ Non deve scandire tutta la lista.
  ☐ Può scandire dall’inizio o dall’ultima ricerca.

☐ **Best-fit**: Alloca il più piccolo hole che è grande abbastanza.
  ☐ Deve cercare l’intera lista se non ordinata con la dimensione.
  ☐ Produce il più piccolo residuo di hole.

☐ **Worst-fit**: Alloca il più largo hole.
  ☐ Deve cercare l’intera lista, se non ordinata.
  ☐ Produce il più largo residuo di hole.

Dalle simulazioni si vede che first-fit e best-fit superiori a worst-fit in termini di velocità e utilizzo dello storage.

**First-fit più veloce**, non chiaro invece per quanto riguarda lo storage.

## Frammentazione

□ **Problemi di frammentazione esterna.**

□ **Frammentazione esterna** – esiste memoria totale per soddisfare una richiesta, ma non è contigua.
  □ Tanti buchi piccoli non contigui.
  □ Con first-fit dati $N$ blocchi allocati, 0.5 $N$ blocchi sono persi per frammentazione.
    ► 1/3 può essere non usabile -> **50-percent rule**.

□ **Frammentazione interna** – la memoria allocata può essere più grande di quella richiesta.
  □ La differenza di dimensione è interna ad una partizione, ma non è usata.
  □ Esempio:
    ► Processo richiede 18462 byte ma buco di 18464, troppo piccolo il residuo per tenerne traccia.
    ► Per evitare il problema si divide la memoria in blocchi di dimensione fissa, ma allora si alloca più memoria ogni volta (frammentazione interna).

## Frammentazione (Soluzioni)

La frammentazione esterna si riduce con la **compattazione**.
- Riassegna i contenuti della memoria per mettere insieme tutta la memoria libera in un blocco di grandi dimensioni.
- La compattazione è possibile se la rilocazione è dinamica ed è fatta a tempo di esecuzione.

Un’altra strategia è la **paginazione** che permette l’allocazione in locazioni non contigue:
- Il paging è la strategia più usata dai moderni SO.

## Paging

- Lo spazio dell’indirizzi fisici di un processo può essere **non contiguo**.
  - Ad un processo è allocata memoria fisica quando è disponibile.
  - Si evita la frammentazione esterna.
  - Si evita il problema di frammenti di memoria con dimensioni variabili.

- Si divide la memoria fisica in blocchi di dimensione fissa detti **frame**.
  - Dimensione potenza di 2, tra 4 KB e 2 GB.

- Si divide la memoria logica in blocchi della stessa dimensione detti **pagine**.

- Si tiene traccia di tutti i frame liberi.

- Per lanciare un programma di dimensione $N$ pagine, si devono trovare $N$ frame liberi e caricare il programma.

- Occorre una **page table** per tradare gli indirizzi logici in fisici.

- Non risolve problemi di frammentazione interna.

## Schema di Traduzione degli Indirizzi

□ L’indirizzo logico generato dalla CPU è diviso in due parti:

□ **Page number (p)** – usato come indice nella **page table** che contiene l’indirizzo base di ogni pagina nella memoria fisica.

□ **Page offset (d)** – combinato con l’indirizzo base definisce l’indirizzo di memoria fisica.

| page number | page offset |
| :--- | :--- |
| p | d |
| m -n | n |

□ Con spazio degli indirizzi logici di dim $2^m$ e pagine di dim $2^n$.

□ Spazio degli indirizzi logici sparato da quello degli indirizzi fisici.

## Hardware per il Paging

La **MMU** esegue i seguenti passi:
- Estrae in numero $p$ di pagina usandolo come indice.
- Estrae il frame number $f$ dalla tabella.
- Compone l’indirizzo sostituendo $f$ a $p$.

Le pagine con potenza di 2 semplificano l’operazione:
- Se $2^m$ indirizzi logici ed frame di dim $2^n$ allora
- $m - n$ bit per il page number $n$ per l’offset.

## Modello di Paging di Memoria Logica e Fisica

*(Schema Concettuale)*
- **Logical Memory** $\rightarrow$ **Page Table** $\rightarrow$ **Physical Memory**
- Le pagine sono mappate sui frame corrispondenti.

## Esempio Paging

Indirizzo logico 0 = pagina 0, offset 0.
La pagina 0 è nel frame 5, quindi 0 logico si mappa in 20 [= (5 × 4) + 0] fisico.

Indirizzo logico 3 (pagina 0, offset 3) mappa nell’indirizzo fisico 23 [= (5 × 4) + 3].

Indirizzo logico 4 è in page 1, offset 0; page 1 si mappa nel frame 6.
Quindi 4 logico si mappa nel fisico 24 [= (6 × 4) + 0].

- $n=2$ e $m=4$
- Memoria 32-byte e pagine 4-byte (8 pagine)

## Paging (Analisi Frammentazione)

□ Con paging si ha solo frammentazione interna.
□ Calcolo della frammentazione interna.

□ Esempio:
  ▶ Page size = 2,048 bytes
  ▶ Process size = 72,766 bytes
  ▶ 35 pages + 1,086 bytes
  ▶ Frammentazione interna di 2,048 - 1,086 = 962 bytes

□ Frammentazione worst case = 1 frame – 1 byte.

□ In media frammentazione = 1 / 2 frame size.

□ Quindi piccoli frame desiderabili?
  ▶ … ma ogni entry della page table impegna memoria per tracciarla.

□ Le dimensioni delle pagine crescono nel tempo.
  ▶ Solaris supporta due dimensioni – 8 KB e 4 MB.
  ▶ Win 11 supporta 4 KB, 2 MB, 1 GB.
  ▶ Linux supporta default (4 KB) e huge pages.

## Paging (Statistiche Linux)

Con paging si ha solo frammentazione interna.
Le dimensioni delle pagine crescono nel tempo.
Linux supporta default (4 KB) e huge pages (def 2 MB).

```monospace
$getconf PAGESIZE
4096
```

Statistiche di mem in kb:
```monospace
$grep Huge /proc/meminfo
```
AnonHugePages: 0 kB
ShmemHugePages: 0 kB
FileHugePages: 0 kB
HugePages_Total: 0
HugePages_Free: 0
HugePages_Rsvd: 0
HugePages_Surp: 0
Hugepagesize: 2048 kB
Hugetlb: 0 kB

## Esercizio 1

Dato un sistema con uno spazio di indirizzi logici a 14 bit e pagine da 2KB, quante entry avrà la tabella delle pagine?

## Esercizio 1 (Risoluzione)

□ Dato un sistema con uno spazio di indirizzi logici a 14 bit e pagine da 2KB, quante entry avrà la tabella delle pagine?

□ Con pagine di 2KB avremo $2^{11}$ B, quindi $n = 11$.

□ Cioè 11 bit per offset, dunque rimangono 3 bit per indicare la pagina.

□ La tabella delle pagine avrà $2^3$ entry.

## Esercizio 2

- Si assuma di avere un sistema con uno spazio degli indirizzi logici di 15 bit e 8 pagine. Quanto sono grandi le pagine del sistema?

## Esercizio 2 (Risoluzione)

□ Si assuma di avere un sistema con uno spazio degli indirizzi logici di 15 bit e 8 pagine. Quanto sono grandi le pagine del sistema?

□ Pagine 8 = $2^3$, cioè 3 bit per rappresentarle.
□ Bit di offset 15 – 3 = 12.
□ $2^{12}$ byte da indirizzare, cioè pagine da 4 KB ($2^2 \times 2^{10}$).

## Esercizio 3

- Sia dato un sottosistema di memoria con paginazione, caratterizzato dalle seguenti dimensioni:
  - Frame di 4 MB e memoria fisica indirizzabile di 128 GB.
- Si calcoli il numero di bit minimo per indicizzare tutte le pagine associate.

## Esercizio 3 (Risoluzione)

- Sia dato un sottosistema di memoria con paginazione, caratterizzato dalle seguenti dimensioni:
  - Frame di 4 MB e memoria fisica indirizzabile di 128 GB.
- Si calcoli il numero di bit minimo per indicizzare tutte le pagine associate.

- Frame 4 MB, quindi $2^2 \times 2^{20} = 2^{22}$ byte.
- Memoria fisica 128 GB = $2^7 \times 2^{30} = 2^{37}$ byte.
- Numero frame = $2^{37} / 2^{22} = 2^{15}$.
- Quindi **15 bit** è il numero minimo per indicizzare le pagine.

## Frame Liberi

Un processo da eseguire viene valutato in pagine e se richiede $n$ pagine occorrono $n$ frame liberi in memoria. Le pagine sono via via allocate e associate ai frame liberi.

*Before allocation* $\rightarrow$ *After allocation*

## Frame Liberi (Gestione SO)

Un processo da eseguire viene valutato in pagine e se richiede $n$ pagine occorrono $n$ frame liberi in memoria. Le pagine sono via via allocate e associate ai frame liberi.

Il Sistema Operativo mantiene una **Tabella dei Blocchi** per tracciare l’uso della memoria (libera, occupata, assegnazione).

Quando un processo chiede memoria viene consultata la tabella dei blocchi per l’assegnazione.

*Before allocation* $\rightarrow$ *After allocation*

## Implementazione della Page Table

- Struttura **per-processo** con puntatore nel PCB.
- Quando un processo va in esecuzione devono essere ricaricati i registri e ricaricati i valori per la gestione della page table.
- La page table può essere implementata in vari modi:
  - **Registri dedicati**: caricati dal dispatcher della CPU, accesso del SO in modalità privilegiata, richiede gestione context switch, piccola tabella (es. 256 entry).
  - **In memoria principale**: Se più grande (es. $2^{20}$ entry) la page table è mantenuta in memoria principale.
    - **Page-table base register (PTBR)** punta alla page table.
    - **Page-table length register (PTLR)** indica la dim della page table.

*Diagram showing the CPU, page table, and memory hierarchy. The page table is shown as a stack of horizontal layers with labels for "Tabelle delle pagine" and "Processo in esecuzione". The CPU is at the bottom, with the page table above it. The memory hierarchy is indicated by horizontal layers with labels for "per prelevare un dato dalla memoria sono necessari 2 accessi!!".*

## Implementazione della Page Table (Dettagli)

- Struttura per-processo con puntatore nel PCB.
- Quando un processo va in esecuzione devono essere ricaricati i registri e ricaricati i valori per la gestione della page table.
- La page table può essere implementata in vari modi:
  - Registri dedicati caricati dal dispatcher della CPU, accesso del SO in modalità privilegiata, richiede gestione context switch, piccola tabella (es. 256 entry).
  - Se più grande (es. $2^{20}$ entry) la page table è mantenuta in memoria principale.
    - Page-table base register (PTBR) punta alla page table.
    - Page-table length register (PTLR) indica la dim della page table.
    - **Veloce context switch** (cambia il puntatore).
    - **Lento accesso a memoria**: Ogni accesso a dati/istruzioni richiede due accessi in memoria: uno per la page table ed uno per i dati/istruzioni.
    - I due accessi in memoria possono essere risolti utilizzando una cache speciale detta **registri associativi** o **translation look-aside buffers (TLBs)**.

## Memoria Associativa (TLB)

- Per la traduzione di un indirizzo si cerca prima in memoria associative e poi in memoria principale.
- **Memoria associativa** – ricerca parallela.

| Page # | Frame # |
| :--- | :--- |
| | |
| | |
| | |

- **Traduzione di un indirizzo (p, d)**:
  - Se $p$ è in un registro associativo, genera il frame # in output.
  - Altrimenti (**TLB miss**) prendi il frame # dalla page table in memoria.
    - La nuova coppia trovata può essere aggiunta nei registri.

## Hardware per Paging con TLB

Hardware necessario per implementare il paging con Translation Look-aside Buffers (TLBs):

- CPU
- logical address
- page number
- frame number
- TLB
- TLB hit
- physical address
- physical memory
- TLB miss
- page table

## Implementazione della Page Table (TLB Policies)

- Ogni volta che non si trova il valore in TLB (**TLB miss**), il valore è caricato sulla TLB per un accesso veloce la volta successiva.
  - Se piena occorrono politiche di rimpiazzo: **Least recently used (LRU)**, **round robin**, **random**.
- Alcune entry possono essere cablate per consentire l’accesso permanente.
  - Es. Codice del kernel rilevante.

- Alcune TLB hanno **address-space identifiers (ASIDs)** per ogni entry:
  - Identifica univocamente il processo.
  - Permette di mantenere info su diversi processi contemporaneamente.
    - Altrimenti dovrebbe fare il flush per ogni context switch per evitare di far accedere il processo alle associazioni della page table di un processo precedente.
  - Fornisce una protezione del suo spazio di indirizzi.
    - Quando risolve l’indirizzo verifica se il processo corrente corrisponde a quello indicato, se non corrisponde si considera una TLB miss.

## Tempo di Accesso Effettivo (EAT)

- Assumiamo $\varepsilon$ unità di tempo la ricerca in TLB.
  - Può essere < 10% del tempo di accesso in memoria.
- Assumiamo la **hit ratio** = $\alpha$.
  - Hit ratio – percentuale di volte che si trova la pagina in TLB (dipende dal numero di registri).
    - Es. 80% significa 80% delle volte si trova la pagina.
- Considiamo $\alpha = 80\%$, $\varepsilon = 20$ns per una ricerca in TLB e $T_a = 100$ns per un accesso in memoria.
- **Effective Access Time (EAT)**:
  $$EAT = (T_a + \varepsilon) \alpha + (2 T_a + \varepsilon)(1 - \alpha)$$
  $$= 2 T_a + \varepsilon - T_a \alpha$$
  - Se $\alpha = 80\%$, $\varepsilon = 20$ns per la ricerca in TLB search, $T_a = 100$ns per accesso in memoria … **EAT = 140ns**.
  - Con un più realistico hit ratio -> $\alpha = 99\%$, $\varepsilon = 20$ns per la ricerca in TLB, 100ns per accesso in memoria … **EAT = 121ns**.

## Tempo di Accesso Effettivo (Sistemi Moderni)

Nei sistemi moderni più complicato il calcolo perché più livelli di TLB.
- Es. La CPU Intel Core i7 ha una TLB L1 da 128-entry per le istruzioni ed una TLB L1 dati da 64-entry.
- Se c’è il miss ad L1 occorrono 6 cicli di CPU per verificare la entry nella L2 512-entry TLB.
- Se miss in L2 allora la CPU o cerca le entry in memoria, con costo di centinaia di cicli, oppure può interrompere per delegare al SO il compito …

**TLB** sono elementi hardware a supporto del paging, gli SO devono essere progettati tenendo presente le caratteristiche di questi elementi che possono variare a seconda della piattaforma.

## Esercizio

- Sia dato un sistema di paginazione con una tabella delle pagine che risieda in memoria con un TLB con un hit ratio del 90%.
- Se per un accesso in memoria occorrono 200 nanosecondi, quanto tempo occorrerà per ottenere il dato relativo a un indirizzo logico?
  - Si supponga trascurabile il tempo di ricerca della entry nella tabella delle pagine.

## Esercizio (Risoluzione)

□ Sia dato un sistema di paginazione con una tabella delle pagine che risieda in memoria con un TLB con un hit ratio del 90%.
□ Se per un accesso in memoria occorrono 200 nanosecondi, quanto tempo occorrerà per ottenere il dato relativo a un indirizzo logico?
□ Si supponga trascurabile il tempo di ricerca della entry nella tabella delle pagine.

- **Caso hit**: tempo di accesso 200 ns.
- **Caso miss**: tempo di accesso 400 ns.
- **Tempo accesso effettivo**: $0.9 \times 200 + 0.1 \times 400 = 220$ ns.

## Protezione di Memoria

- La protezione della memoria è implementata associando dei **bit di protezione** per ogni frame per indicare i permessi (read-only, read-write).
  - Si possono aggiungere più bit per indicare execute-only, etc.
  - Mentre si cerca il frame si può controllare l’accesso.
  - Una violazione dei permessi provoca un **trap hardware**.

- Alle entry della page table sono associate anche bit **valid-invalid**:
  - “valid” indica che la pagina nello spazio logico del processo è valida, quindi legale.
  - “invalid” indica che la pagina non è nello spazio logico del processo.
  - Ogni violazione provoca un trap al kernel.
  - Il SO usa questi bit per permettere o vietare l’accesso alle pagine.

## Valid (v) o Invalid (i) Bit in Page Table

Es. 14-bit address space [0,16383], processo solo in [0, 10468].
Pagine di 2KB, quindi le pagine 6, 7 non sono valide.

Però pagina 5 accessibile (frammentazione interna) fino a 12287.

Accesso disabilitato.

Si può usare il **page-table length register (PTLR)** per indicare la dimensione della tabella delle pagine e verificare se l’accesso è consentito oppure no.

*Operating System Concepts – 10th Edition*

## Present/Not Present Bit in Page Table

Es. 16 bit e pagine di 4 KB ($2^{12}$), entry tabella delle pagine?

Indirizzo virtuale 8196 tradotto nell’indirizzo fisico 24580.

## Entry di una Page Table

Diverse informazioni aggiuntive nella Page Table:
- Presente/Assente (page fault)
- Valido/invalid
- Protezione read/write o only read
- Modificato (**dirty bit**)
- Riferito
- Caching (se disabilitato accessi diretti alla pag. in mem)

## Pagine Condivise

□ Vantaggio del paging è la possibilità di **condividere pagine** fra processi.
□ Particolarmente vantaggioso in architetture multiutente.

□ **Codice condiviso**:
  □ Una copia di codice read-only (rientrante) condivisa tra processi (i.e., text editor, compilatori, librerie) evitando duplicazioni.
  ► Due o più processi possono condividere lo stesso codice.
  ► Es. Standard C library condivisa tra processi (se 2Mb per 40 utenti, 2Mb vs 80 Mb).
  ► Simile a thread multipli che condividono lo stesso spazio di processo.
  ► Utile anche per *interprocess communication* se possibile condividere pagine read-write.

□ **Codice e dati privati**:
  □ Ogni processo mantiene copia separata del codice e dei dati.
  □ Le pagine per codice privato e dati può apparire ovunque nello spazio degli indirizzi logici.

## Esempio Pagine Condivise

□ Esempio codice editor condiviso da tre processi:

- process $P_1$
  - page table for $P_1$
  - ed 1, ed 2, ed 3
  - data 1
- process $P_2$
  - page table for $P_2$
  - ed 1, ed 2, ed 3
  - data 2
- process $P_3$
  - page table for $P_3$

## Struttura della Tabella delle Pagine

- Modeni elaboratori supportano spazi di indirizzi logici molto estesi (da $2^{32}$ a $2^{64}$).
- Struttura per la paginazione può diventare enorme.
  - Se indirizzi logici di 32-bit e dimensione delle pagine di 4 KB ($2^{12}$)
  - La page table avrebbe più di un milione di entry ($2^{32} / 2^{12}$).
  - Se ogni entry è di 4 byte -> 4 MB di spazio di indirizzi fisici solo per la tabella delle pagine.
    - Alto costo di memorizzazione.
    - Non si vuole allocare in modo contiguo in memoria principale.

**Metodi:**
- Hierarchical Paging
- Hashed Page Tables
- Inverted Page Tables

## Tabella delle Pagine Gerarchiche

- Suddividere lo spazio degli indirizzi logici su più tabelle delle pagine.
- Una tecnica semplice è la tabella delle pagine su più livelli.
  - Si pagina la tabella delle pagine.
  - Il page number è a sua volta diviso in page number e offset.
  - Es. con spazio degli indirizzi logici a $2^{32}$ e pagine di 4KB.

| page number | page offset |
| :--- | :--- |
| $p_1$ | $p_2$ |
| 10 | 10 | 12 |

## Tabella delle Pagine a Due Livelli

*Schema Concettuale:*
- outer page table
- page of page table
- page table
- memory

## Esempio Paginazione a due Livelli

- Un indirizzo logico (su macchina a 32-bit con pagine da 1KB) diviso in:
  - page number di 22 bit
  - page offset di 10 bit

- La tabella delle pagine è paginata e il page number è ancora suddiviso in:
  - 12-bit page number
  - 10-bit page offset

- L’indirizzo logico è quindi:

| page number | page offset |
| :--- | :--- |
| $p_1$ | $p_2$ |
| 12 | 10 | 10 |

- dove $p_1$ è indice della tabella esterna, $p_2$ è l’offset nella pagina della tabella delle pagine esterna.

- Metodo chiamato **forward-mapped page table**.

## Schema di Address-Translation

- Metodo chiamato forward-mapped page table.

## 64-bit Logical Address Space

- Ma anche lo schema di paging a due livelli non è sufficiente (indirizzi 64 bit).
- Se la dimensione delle pagine fosse 4 KB ($2^{12}$)
  - La page table avrebbe $2^{52}$ entry.
  - Con lo schema a due livelli e pagine interne di $2^{10}$ con entry di 4-byte
  - L’indirizzo sarebbe:

| outer page | inner page | page offset |
| :--- | :--- | :--- |
| $p_1$ | $p_2$ | $d$ |
| 42 | 10 | 12 |

- La tabella esterna avrebbe $2^{42}$ entry.
- Una soluzione prevede l’aggiunta di una seconda tabella esterna.
- Ad esempio una seconda tabella esterna di $2^{34}$ byte.

- Può portare fino a 4 accessi in memoria per un singolo accesso.

## Schema di Paging a Tre Livelli

| outer page | inner page | offset |
| :--- | :--- | :--- |
| $p_1$ | $p_2$ | $d$ |
| 42 | 10 | 12 |

| 2nd outer page | outer page | inner page | offset |
| :--- | :--- | :--- | :--- |
| $p_1$ | $p_2$ | $p_3$ | $d$ |
| 32 | 10 | 10 | 12 |

Sempre pagina esterna di $2^{32}$ entry (se 4 byte per entry allora $2^{34}$ byte, i.e., 16 GB).

Allora altri livelli?

## Hashed Page Table

- Tipico con spazio di indirizzi > 32 bits.
- Il numero di pagina virtuale viene messo in una hash page table.

**Hash Table:**
- Struttura dati per implementare array associativi.
  - Mappa chiave su valore.
  - Utilizza una funzione di hash $h$ che traduce una chiave in un indice di una tabella.
    $$h : U \rightarrow \{0, 1, \ldots, m-1\}$$
  Dove $U$ è l’universo delle chiavi, mappate da $h$ su indici sono indici di una tabella.
    $$T[0 \ldots m-1]$$
  Dal momento che Hash table utile con $m \ll | U |$ sono possibili collisioni.
    $$h(k_1) = h(k_2)$$
  Finché il numero di elementi in tabella $n < m$ sono rare.
  Con $n > m$ inevitabili.

## Hashed Page Table (Dettagli)

- Tipico con spazio di indirizzi > 32 bits.
- Il numero di pagina virtuale viene messo in una hash page table.
  - La page table contiene una catena di elementi in hash sulla stessa locazione.
  - Ogni elemento contiene: (1) il numero di pagina virtuale, (2) il valore del page frame mappato, (3) un puntatore all’elemento successivo.
  - I numeri di pagina virtuale sono confrontati nella catena in cerca di un match.
  - Se un match è trovato viene estratto il frame fisico corrispondente.

- Una variazione per indirizzi a 64-bit sono le **clustered page tables**.
  - Simili alle hashed ma ogni entry nella hash si riferisce a molte pagine (16) invece di una sola.
  - Molto utile per spazi di indirizzi sparsi (dove i riferimenti in memoria sono non contigui e sparpagliati).

## Tabella delle Pagine Invertite

□ Invece di avere ogni processo con una page table e tener traccia di tutte le pagine logiche si tracciano le pagine fisiche (es. IBM RT).

□ Una entry per ogni pagina reale di memoria.
□ Le entry consistono dell’indirizzo virtuale della pagina contenuta in memoria reale con informazione sul processo che possiede quella pagina.

`<process-id, page-number, offset>`

□ Minore memoria per le tabelle delle pagine, ma aumenta il tempo necessario per cercare la tabella quando c’è un riferimento ad una pagina.
□ Usata da 64-bit UltraSPARC e PowerPC.

## Architettura delle Tabella delle Pagine invertite

$p$ non è più indice, ricerca del pid.

## Tabella delle Pagine Invertite (Dettagli)

- Minore memoria per le tabelle delle pagine, ma aumenta il tempo necessario per cercare la tabella quando c’è un riferimento ad una pagina.

`<process-id, page-number, offset>`

- Hash table per limitare la ricerca ad una - o poche - entry della tabella.
  - Due accessi in memoria (uno per accedere ad hash table).
  - TLB può accelerare l’accesso (prima di accedere ad hash table).

- Più complesso implementare la memoria condivisa (**shared memory**).
  - Un mapping solo di un indirizzo virtuale all’indirizzo fisico condiviso.
  - Un riferimento da parte di altro processo genera il fallimento ed eventuale rimpiazzo del processo che insiste sul segmento.

## Oracle SPARC Solaris

- Esempio di SO a 64-bit con HW strettamente integrato.
  - Obiettivi: efficienza e basso overhead.

- Basato su hashing, ma più complesso.
- Utilizza due hash table.
  - Una per il kernel ed una per i processi utente.
  - Ognuna mappa indirizzi da memoria virtuale su memoria fisica.
  - Ogni entry rappresenta un’area contigua di memoria virtuale mappata.
    - Non una entry di hash-table separata per ogni pagina.
    - Ogni entry ha un indirizzo base e uno span (che indica il numero di pagine che la entry rappresenta).

## Oracle SPARC Solaris (Dettagli)

- La ricerca di una traduzione direttamente su hash-table inefficiente.
  - Si usa **Translation Lookaside Buffer (TLB)**.

- TLB mantiene le **Translation Table Entries (TTEs)** per una ricerca rapida:
  - Un insieme di TTEs è anche mantenuto in un **Translation Storage Buffer (TSB)**.
    - Include entry per le pagine con accesso recente.

- Un riferimento ad un indirizzo virtuale porta alla ricerca in TLB.
  - Se c’è il miss, si scandisce via hardware la TSB cercando la TTE corrispondente a quell’indirizzo (**TSB walk**).
    - Se si trova il match la CPU copia la TSB entry nella TLB e si completa la traduzione.
    - Se non si trova il match il kernel interrompe per cercare nella hash table.
      - Il kernel poi crea una TTE dalla hash table e la mette in TSB, l’interrupt handler ritorna il controlla alla MMU che completa la traduzione dell’indirizzo.

## Swapping

- Un processo può essere scambiato (**swapped**) temporanemente con memoria ausiliaria (**backing store**) e poi portato ancora nella memoria principale per continuare l’esecuzione.
  - La memoria fisica totale occupata dai processi può eccedere la memoria fisica disponibile.

- **Backing store** – memoria secondaria veloce grande abbastanza per accommodare i processi che devono essere stoccati e repristinati.
  - Deve fornire un accesso diretto a queste immagini in memoria.

- **Swap out, swap in** – swapping di processi.
  - Processi inattivi possono essere selezionati per swapping.
  - La maggior parte del tempo di swap è di tempo di transferimento; il tempo di trasferimento è direttamente proporzionale alla quantità di memoria trasferita (swapped).

## Schema dello Swapping

1. swap out
2. swap in

*Diagrama:*
User space $\rightarrow$ Main Memory $\rightarrow$ Backing Store

## Tempo di Context Switch incluso lo Swapping

- Se il prossimo processo da mandare alla CPU non è in memoria si deve fare lo swap-out di un processo e lo swap-in del processo target.

- Il tempo di context switch può essere molto alto.
  - Un processo di 100MB che fa swapping su hard disk con un transfer rate di 50MB/sec.
  - tempo di swap out di 2000 ms.
  - … più swap in di un processo della stessa dimensione.
  - tempo totale di context switch swapping è 4000ms (4 secondi).

- Si può ridurre se si riduce la dimensione della memoria swapped.
  - Sapendo quanta memoria viene usata esattamente da un processo si può ridurre.

## Tempo di Context Switch incluso lo Swapping (Moderne Varianti)

- Lo standard swapping non è più usato nei moderni SO (si usava in UNIX).
  - Una versione modificata tipica:
    - Swap solo quando la memoria libera è estremamente bassa.
  - Viene fatto swapping con paging.
    - Sottoinsieme di pagine: **page-in page-out**.

![Diagramma che mostra i processi di page-out e page-in nella memoria principale.](image)

## Swapping su Sistemi Mobile

Tipicamente non supportata.

□ Basta su flash memory.
  ► poco spazio.
  ► limitato numero di cicli di scrittura.
  ► dialogo carente tra la flash memory e la CPU su piattaforma mobile.

□ Si usano altri metodi per liberare memoria.

□ iOS chiede alle app di lasciare volontariamente memoria.
  ► Dati read-only rilasciati e ricaricati dalla flash se necessario.
  ► Fallimento nel rilascio può portare alla terminazione.

□ Android termina le app se poca memoria, prima salva lo stato sulla flash per un restart veloce.
□ Entrambi i sistemi supportano il paging.

## Segmentazione

- La pagina separa memoria logica e memoria fisica.
- **Segmentazione** è uno schema di gestione della memoria che supporta la prospettiva utente sulla memoria.
- Un programma è visto come una collezione di segmenti.
  - Un segmento è un’unità logica come:
    - main program
    - procedure
    - function
    - method
    - object
    - local variables, global variables
    - common block
    - stack
    - symbol table
    - arrays

## Visione utente di un Programma

*Logical Address*

## Visione Logica della Segmentazione

I segmenti sono numerati.
*(User Space $\rightarrow$ Physical Memory Space)*

## Architettura di Segmentazione

- Indirizzi logici sono definiti dalla tuple bidimensionale:
  `<segment-number, offset>`,

- Serve una struttura che mappa le tuple in indirizzi fisici.

- **Tabella dei Segmenti** – mappa indirizzi bidimensionali in fisici; ogni table entry ha:
  - **base** – contiene l’indirizzo fisico di partenza del segmento.
  - **limite** – specifica la lunghezza del segmento.

## Hardware per Segmentazione

*Diagramma:*
CPU $\rightarrow$ (s, d) $\rightarrow$ (limit, base) $\rightarrow$ Segment Table $\rightarrow$ (yes/no) $\rightarrow$ Physical Memory (Trap: addressing error).

## Architettura di Segmentazione (Dettagli Hardware)

□ Indirizzi logici sono definiti dalla tuple bidimensionale:
  <segment-number, offset>,

□ Serve una struttura che mappa le tuple in indirizzi fisici.

□ **Tabella dei Segmenti** – mappa indirizzi bidimensionali in fisici; ogni table entry ha:
  □ **base** – contiene l’indirizzo fisico di partenza del segmento.
  □ **limite** – specifica la lunghezza del segmento.

□ La tabella dei segmenti non può essere tenuta in registri, quindi in memoria.

□ **Segment-table base register (STBR)** indica la locazione di memoria della tabella dei segmenti.

□ **Segment-table length register (STLR)** indica il numero dei segmenti usati da un programma:
  ► Dato indirizzo logico (s,d), il numero s è legale se $s < STLR$.

□ Registri associativi per limitare i due accessi in memoria.

## Architettura di Segmentazione (Esempio)

*(Esempio grafico)*

## Architettura per Segmentazione (Protezione)

Protezione (stesso segmento, stessa protezione).
- Ogni entry nella tabella dei segmenti è associata a:
  - **validation bit** = 0 ⇒ segmento illegale.
  - privilegi read/write/execute.
- Bit di protezione associati ai segmenti.

Possono essere condivisi i segmenti tra processi.
- La condivisione del codice avviene al livello di segmento.
- Come per il paging una copia di un programma condiviso (es. editor di testo).
- Più programmi possono dover fare riferimento allo stesso numero di frammento.
  - Porzioni di codice con riferimento diretto a sé stesse.

Problema del doppio accesso come per paginazione.
- I segmenti di un processo, come per pagine, non necessariamente contigui.
- Segmenti di dimensione diversa quindi problemi di frammentazione.
- Si possono fondere i metodi di paginazione e segmentazione.

## Segmentazione Paginata

- Segmentazione paginate in GE 645 (MULTICS).
  - Tabella dei segmenti:
    - lunghezza segmento e base della tabella.
  - Tabella delle pagine per il segmento s:
    - base tab + p = base pagina.

## Esempi: Architetture Intel 32 e 64-bit

Intel ha dominato l’industria per decadi.
- Negli anni 70, 8086 a 16-bit seguita da 8088 (usato nel PC IBM).
- Poi passata ad architetture a 32-bit (Architetture IA-32 – Intel Architecture).
- Le CPU Pentium sono esempi di 32-bit.
- Ora le CPU Intel sono a 64-bit e sono chiamate architetture IA-64.
- Molte varianti sui chip, si considerino solo i concetti principali.

## Esempio: l’Architetture Intel IA-32

- Supporta sia segmentazione che segmentazione con paging.
- La CPU genera indirizzi logici passati all’unità di segmentazione che produce **indirizzi lineari** poi passati all’unità di paging che produce l’indirizzo fisico (**segmentation unit + page unit = MMU**).

- Ogni segmento grande fino a 4 GB.
- Numero di segmenti per processo divisi in due partizioni:
  - Prima partizione segmenti privati per il processo (descritti in una **local descriptor table (LDT)**).
  - Seconda partizione segmenti condivisi tra tutti i processi (descritti in una **global descriptor table (GDT)**).

## Esempio: Architettura Intel IA-32 (Specifiche)

- La CPU genera indirizzi logici per l’unità di segmentazione.
  - logical address.
  - selector.
  - offset.
  - offset a 32 bit.
  - enty da 8 byte (base e limite e attributi di protezione).
  - se offset supera limite generato un fault.
  - 8086-80286 solo segmentazione.
  - 80386 segmentation+paging (1985).
  - Negli SO moderni segmentazione in *flat mode* (base=0) e paging dominante.

- Il selettore è a 16-bit.
  - s per il numero di segmento, g il tipo (global/local), p la protezione.

## Esempio: Architettura Intel IA-32 (Traduzione)

Traduzione da indirizzo logico a fisico in IA-32.

Intel 80386 e successivi in modalità 32 bit.

- Unità di paging di IA-32.
- Dimensioni delle pagine 4 KB o 4 MB.
  - Per 4 KB schema di paging a due livelli.
  - Per 4 MB schema ad un livello.

Indirizzo lineare 32 bit per paging a 2 livelli.

## Esempio: Architettura Intel IA-32 (Dettagli)

- Unità di paging di IA-32.
- Dimensioni delle pagine 4 KB o 4 MB.
  - Per 4 KB schema di paging a due livelli.
  - Per 4 MB schema ad un livello.

Indica una entry nella page directory (tabella esterna).

Registro che indica la page directory del processo corrente.

## Intel IA-32 Estensioni Indirizzo Pagina

- Limiti di accesso di indirizzi 32-bit hanno portato Intel a creare **page address extension (PAE)** permettendo ad app di 32-bit l’accesso a memorie più grandi di 4GB.
  - Paging con schema a 3-livelli (per pagine a 4 KB).
  - Primi 2 bit si riferiscono ad una page directory pointer table.
  - Le entry delle strutture di paging aumentate da 32 a 64-bit.
    - Base address da 20 a 24 bit + 12 bit per offset.
    - Indirizzi fisici di 36 bit – fino a 64GB di memoria fisica.

*Diagram showing the page directory pointer table and page table offsets. In IA-32 Linux e MacOS supportano, Windows no.*

## AMD64/Intel x86-64

- Generazione corrente è architettura x86-64.
- x86-64 proposto da AMD e adottato da Intel (AMD64 e Intel64).

- 64 bit consentirebbero dimensioni enormi ($2^{64} > 16$ exabyte).
- In pratica è implementato un indirizzamento a 48 bit.
  - Dimensione di pagina 4 KB, 2 MB, 1 GB.
  - Quattro livelli di gerarchia di paging.

Anche se 48-bit virtuali con page address extension fino a 52-bit indirizzi fisici.

## Esempio: Architettura ARM

- Dominante per i chip su piattaforma mobile (es. Apple iOS e Google Android, ma anche sistemi embedded real-time).
- CPU moderna ed efficiente energeticamente.
- ARMv8 è a 64-bit.

## Esempio: Architettura ARMv8 (Granularità)

□ ARMv8 è a 64-bit.
□ Tre granularità di traduzione 4 KB, 16 KB, 64 KB associate a dimensione di pagina e sezioni di memoria contigua (regions).

| Translation Granule Size | Page Size | Region Size |
| :--- | :--- | :--- |
| 4 KB | 4 KB | 2 MB, 1 GB |
| 16 KB | 16 KB | 32 MB |
| 64 KB | 64 KB | 512 MB |

□ Usati fino a 48 bit.

□ Per 4 KB e 16 KB fino a 4 livelli di paging, fino a 3 per 64 KB.
□ I livelli 1 e 2 possono essere anche usati per indirizzare regioni da 1-GB (livello 1) e 2-MB (livello 2).

□ Se livello 1, 0–30 bit di offset, se livello 2, 0–20 bit di offset.
□ Due livelli di TLBs.
  ▶ Livelli interni hanno due micro TLBs (una dati, una instruzioni).
  ▶ La più esterna è una singola TLB.

## TLB Miss e Cache

- In caso di TLB miss si attiva il **page table walk**.
- Il page table walk richiede più accessi alle strutture di paging.
- Le page table sono dati in memoria.
- Gli accessi alle page table:
  - passano attraverso la gerarchia di cache (L1 D-cache, L2, L3).
  - non vanno direttamente in memoria principale.

- Spesso le entry delle page table sono già in cache.
- Gli accessi alle page table sono serviti dalla cache dati, riducendo significativamente il costo di una TLB miss.
- Alcune architetture hanno **paging-structure cache** (cache dedicate per PTE/PDE).

## Comandi

- Layout di memoria di un processo (print memory map).
  - Indirizzi virtuali, Resident Set Size (mem RAM), dirty bit, mode, map.
  - `pmap [options] [pid]`
    - `-x` extended info (address, permissions)
    - `-d` content of heap regions
    - `-p` show the page size
  - `pmap –d [pid]`
  - `pmap –x [pid]`
  - `ps`

| Address | Kbytes | RSS | Dirty | Mode | Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0000563511c54000 | 2048 | 1024 | 0 | r-x-- | /path/to/executable |
| 0000563511e54000 | 4 | 4 | 4 | rw--- | /path/to/executable |
| 00007f5c0ec75000 | 16384 | 8192 | 0 | rw--- | [ anon ] |