## Pagina 1

Memoria Virtuale

---

## Pagina 2

Obiettivi

- Descrivere i benefici di un sistema a memoria virtuale
- Spiegare i concetti di demand paging, sostituzione di pagina e l’allocazione di page frames
- Discutere il principio del modello working-set
- Esaminare come è gestita la memoria kernel

---

## Pagina 3

Background

□ Il codice deve essere in memoria per essere eseguito, ma non tutto è sempre necessario
□ Codice di errore, routine non usate, strutture dati grandi
□ Non necessario tutto il codice del programma nello stesso tempo

□ Se possibile eseguire programmi parzialmente caricati …
□ Programmi non più vincolati dalla memoria fisica
□ Ogni programma occupa meno memoria a run-time -> più programmi eseguiti allo stesso tempo
  ► Miglior utilizzo di CPU e maggior throughput senza incremento in tempi di risposta o tempo di turnaround
□ Meno I/O necessari per caricare o swappare programmi in memoria -> ogni programma utente più veloce

---

## Pagina 4

Background

□ Memoria Virtuale – separazione della memoria logica dalla memoria fisica

□ Solo una parte del programma in memoria per l’esecuzione
□ Spazio di indirizzi logici può essere più grande dello spazio di indirizzi fisici
□ Spazio indirizzi condiviso da molti processi
□ Creazione di processi più efficiente
□ Più programmi eseguiti in concorrenza
□ Meno I/O necessario per caricare o swappare processi

---

## Pagina 5

Background

□ Spazio degli indirizzi virtuali – vista logica su come il processo è contenuto in memoria
  □ Spazio inizia da un indirizzo (es. indirizzo 0)
  □ Indirizzi contigui fino alla fine dello spazio
  □ Memoria fisica organizzata in page frame
  □ MMU deve mappare indirizzo logico su fisico

□ Memoria Virtuale implementata con:
  □ Demand paging
  □ Demand segmentation

---

## Pagina 6

Memoria Virtuale più grande della memoria fisica

Schema che mostra memoria virtuale più grande di quella fisica

- page 0
- page 1
- page 2
- page v
- virtual memory
- memory map
- physical memory

---

## Pagina 7

Spazio degli indirizzi virtuali

Di solito spazio di indirizzi logici con:
- Stack inizia da indirizzo logico massimo e cresce “in giù”
- Heap cresce “in su”
- Massimizza l’uso dello spazio di indirizzi
- Spazio di indirizzi non usato è un buco
  - memoria fisica non necessaria finchè lo heap o stack non cresce fino a nuova pagina

Spazio di indirizzi sparso con buchi lasciati per crescita, dynamically linked libraries, etc

Librerie di sistema condivise nello spazio di indirizzi virtuali

Memoria condivisa mappando pagine read-write nello spazio degli indirizzi virtuali

Le pagine possono essere condivise durante il fork() per accelerare la creazione del processo

---

## Pagina 8

Shared Library usando Memoria Virtuale

- Librerie di sistema condivise nello spazio di indirizzi virtuali
- Shared memory mappando pagine read-write nel virtual address space
- Pagine possono essere condivise durante il fork() per accelerare la creazione del processo

---

## Pagina 9

Demand Paging

- Si può portare l’intero processo in memoria a tempo di caricamento
- Oppure portare una pagina in memoria solo quando è necessario:
  - Meno I/O, elimina il non necessario
  - Minor memoria richiesta
  - Risposta più rapida
  - Più utenti contemporanemente

- Simile al paging con swapping
- Pagina richiesta ⇒ riferimento ad essa
  - Riferimento non valido ⇒ abort
  - Non-in-memoria ⇒ portala in memoria

- Lazy swapper – non swappa una pagina in memoria se non richiesta
  - Swapper che carica singole pagine è un pager

---

## Pagina 10

Concetti di Base

- Non tutto il processo caricato per l’esecuzione, il pager porta in memoria solo le pagine richieste
- Come determinare questo insieme di pagine?
  - Occorre una nuova funzionalità MMU per implementare il demand paging
- Se la pagina richiesta è già *residenti in memoria*
  - Non c’è differenza con normale esecuzione
- Se le pagina richiesta non è residente in memoria
  - Si genera un trap di page fault
  - Si deve trovare e caricare la pagina in memoria dallo storage
    - senza cambiare il comportamento del programma
    - senza che il programmatore debba cambiare il codice

---

## Pagina 11

Valid-Invalid Bit

- Ogni entry della page table ha associato un bit valid–invalid ($v \Rightarrow$ in-memory – memory resident, $i \Rightarrow$ not-in-memory)
- Inizialmente il valid–invalid bit è settato a $i$ su tutte le entry
- Es. di uno stato di page table:

  ```markdown
    Frame #    valid-invalid bit
    v
    v
    v
    i
    ...
    i
    i
  ```

- Se invalid o il frame non è in memoria o accesso vietato
- Durante la traduzione della MMU se il valid–invalid bit nella page table entry è $i \Rightarrow$ page fault

---

## Pagina 12

Page Table quando alcune pagine non sono in Memoria

Es. 0 è valido, 1 non è valido, etc.

logical memory

valid–invalid frame

page table

physical memory

---

## Pagina 13

Page Fault

Il primo riferimento ad una pagina non in memoria genera un trap all’SO:
- Trap di page fault

Page fault gestito come segue:
1. SO cerca su altra tabella (in PCB) per verificare se:
   - Riferimento non valido ⇒ abort
   - Semplicemente non in memoria
2. Se non valido termina, altrimenti procedi con l’inserimento della pagina
3. Trova un frame libero (cercando su lista dei frame liberi)
4. Schedula operazione su disco per lettura della pagina e scrittura nel frame libero
5. A lettura completata resetta le tabelle per indicare che la pagina è in memoria; setta il validation bit = v
6. Riavvia l’instruzione che ha causato il page fault perché a questo punto il processo può accedere alla pagina in memoria

---

## Pagina 14

Passi per Gestire il Page Fault

1. load M
2. trap
3. page is on backing store
4. bring in missing page
5. reset page table
6. restart instruction
7. page table
8. free frame
9. physical memory

---

## Pagina 15

Aspetti del Demand Paging

- Caso estremo – il processo inizia senza pagine in memoria
  - SO setta l’instruction pointer sulla prima istruzione e la memoria non è residente -> page fault
  - … lo stesso per ogni altro processo al primo accesso
    - Pure demand paging

- In realtà un’istruzione può accedere più pagine (una per l’istruzione e tante per i dati) -> multipli page fault
  - Es. fetch e decode di istruzione di somma di 2 numeri da memoria che registra il risultato in memoria
  - Problema mitigato dalla località del riferimento

- Supporto hardware per demand paging
  - Page table con valid / invalid bit
  - Memoria secondaria (dispositivo di swap con swap space)
  - Restart dell’istruzione

---

## Pagina 16

Instruction Restart

□ È necessario il restart delle istruzioni dopo il page fault
□ Fault può avvenire in qualunque momento:
  □ fetch, decode, exec
  □ Se interrotta durante il prelievo di operando, va rifatta dal fetch
  □ Si consideri operazione ADD A, B con risultato in C
    ► Prelievo e decodifica di ADD
    ► Prelievo di A
    ► Prelievo di B
    ► Addizione A e B
    ► Memorizzazione somma in C
  □ Se interrotta su C, va ripetuta l’operazione dal prelievo
  □ Istruzioni ancora più complesse:
    ► IBM System 360/370 MVC può spostare 256 byte da locazione ad un’altra anche sovrapposte
    ► se il blocco di dati è tra due pagine e page fault?
    ► Blocco origine modificato, non si può fare restart, due soluzioni:
      – Si controlla prima dell’operazione caricando tutte le pagine
      – Si mantiene in registri lo stato precedente e si ripristina

---

## Pagina 17

Instruction Restart

□ È necessario il restart delle istruzioni dopo il page fault
□ Fault può avvenire in qualunque momento:
  □ fetch, decode, exec
  □ Se interrotta durante il prelievo di operando, va rifatta dal fetch
  □ Si consideri operazione ADD A, B con risultato in C
  □ Se interrotta su C, va ripetuta l’operazione dal prelievo
  □ Istruzioni ancora più complesse:
    ► IBM System 360/370 MVC può spostare 256 byte da locazione ad un’altra anche sovrapposte
    ► se il blocco di dati è tra due pagine e page fault?
    ► Blocco origine modificato, non si può fare restart, due soluzioni:
      – Si controlla prima dell’operazione caricando tutte le pagine
      – Si mantiene in registri lo stato precedente e si ripristina
□ Autoincremento/ autodecremento
  ► Registri autoincrementati/decrementati prima/dopo utilizzo…
  ► … anche in questo caso, se interrotta l’operazione occorre il ripristino
□ Il paging con demand page richiede un’architettura adatta

---

## Pagina 18

Lista dei frame liberi

□ Fame Free List
□ Quando c’è un page fault occorre caricare la pagina da memoria secondaria in un frame libero
□ Il Sistema mantiene una lista di frame liberi

head → 7 → 97 → 15 → 126 … → 75

□ I frame sono azzerati prima dell’allocazione (zero-fill-on-demand)

---

## Pagina 19

Performance del Demand Paging

Passi del Demand Paging (caso peggiore)

1. Trap al sistema operativo
2. Salva gli user register e il process state
3. Determina se l’interrupt era un page fault
4. Verifica che il riferimento alla pagina era legale e determina la locazione della pagina su disco
5. Schedula una lettura dal disco ad un frame libero:
   1. Attendi in una coda per il dispositivo finché la richiesta di read è servita
   2. Attendi la ricerca e/o il tempo di latenza
   3. Inizia il transferimento della pagina al frame libero
6. Mentre attendi alloca la CPU a qualche altro user
7. Ricevi un interrupt dal I/O (I/O completato)
8. Salva i registeri e lo stato del processo dell’altro user
9. Determina che l’interrupt era dal disco
10. Correggi la page table e le altre tabelle per mostrare la pagina in memoria
11. Attendi che la CPU venga di nuovo allocata a questo processo
12. Ripristina gli user register, il process state e la nuova page table, quindi riprendi l’istruzione interrotta

---

## Pagina 20

Performance del Demand Paging

- Non sempre tutte le operazioni precedent sono richieste
- In ogni caso sono richieste tre principali attività:
  - Servi l’interrupt – ben codificato, necessarie centinaia di istruzioni
  - Leggi la pagina – molto tempo
  - Restart del processo – poco tempo

- Page Fault Rate $0 \leq p \leq 1$
  - se $p = 0$ non page fault
  - se $p = 1$, ogni riferimento è un fault

- Effective Access Time (EAT)
  $$EAT = (1 - p) \times \text{memory access}$$
  $$+ p \times (\text{page fault time})$$

---

## Pagina 21

Esempio Demand Paging

- Tempo accesso memoria = 200 nanosecondi
- Tempo medio di servizio del page-fault = 8 millisecondi
- EAT = $(1 - p) \times 200 + p$ (8 millisecondi)
  $$= (1 - p) \times 200 + p \times 8,000,000$$
  $$= 200 + p \times 7,999,800$$

- Se un accesso su 1000 causa un page fault allora
  EAT = 8.2 microsecondi
  È un slowdown di un fattore di 40!

- Se si vuole una performance degradation < 10 percent
  - $220 > 200 + 7,999,800 \times p$
  - $20 > 7,999,800 \times p$
  - $p < .0000025$
  - < una page fault per ogni 400,000 accessi in memoria

---

## Pagina 22

Demand Paging - Ottimizzazione

I/O su disco per spazio di swap più veloce che quello per accedere al file system anche se su stesso dispositivo
- Swap allocato in blocchi più grandi minor costo di gestione del file system
- Il SO può copiare l’intera immagine del processo su swap space a tempo di caricamento, ma costoso
- Altra opzione (Linux, Windows): demand paging da file system all’inizio poi le pagine vanno nello swap space

Per limitare lo swap space
- File binari eseguibili caricati da file system su frame, ma solo letti, non salvati
  - Sovrascritti in memoria quando si fa swap out, poi si ricaricano direttamente da disco
- Usato in Solaris e nei correnti BSD UNIX
- Occorre comunque scrivere nello swap space
  - Pagine non associate a codice (come stack e heap) – anonymous memory
  - Pagine modificate in memoria principale ma non ancora riscritte sul file system

Sistemi Mobile
- Tipicamente non supportano swap space
- Invece recuperano pagine read-only (come il codice) all’occorrenza (mai anon)

---

## Pagina 23

Copy-on-Write

□ La call fork() crea duplicato del padre (se il figlio fa subito exec() non è necessario il duplicato di memoria)

□ Copy-on-Write (COW) permette ai processi padre e figlio di condividere inizialmente le stesse pagine in memoria

□ Le pagine condivise sono marcate come pagine copy-on-write
□ Se uno dei processi modifica una pagina condivisa allora questa viene copiata
□ COW permette una creazione di processo più efficiente dal momento che solo le pagine modificate sono copiate
□ Tecnica usata su Linux, Windows e macOS

---

## Pagina 24

Copy-on-Write

□ La call fork() crea duplicato del padre, se il figlio fa subito exec() non necessario duplicato di memoria

□ Copy-on-Write (COW) permette ai processi padre e figlio di condividere inizialmente le stesse pagine in memoria
  □ Le pagine sono marcate come pagine copy-on-write
  □ Se uno dei processi modifica una pagina condivisa allora questa è copiata
  □ COW permette una creazione di processo più efficiente dal momento che solo le pagine modificate sono copiate
  □ Tecnica usata su Linux, Windows e macOS

□ vfork() (virtual memory fork) è variante di fork()
  □ Sospende il padre e usa l’address space del padre
  □ Non usa copy-on-write quindi può scrivere sulla memoria del padre
  □ Progettato per avere subito la call exec() per il figlio
  □ Molto efficiente

---

## Pagina 25

Sostituzione delle Pagine

- Se un processo di 10 pagine e ne usa la metà allora risparmiati 5 accessi
- Si può aumentare il grado di multiprogrammazione del doppio
- Si sta sovrallocando memoria
- … ma se non c’è un frame libero dopo il page-fault?

---

## Pagina 26

Sostituzione delle Pagine

- Se un processo di 10 pagine e ne usa la metà allora risparmiati 5 accessi
- Si può aumentare il grado di multiprogrammazione del doppio
- Si sta sovrallocando memoria

- Se non c’è un frame libero dopo il page-fault?
  - SO può terminare il processo (non è la scelta migliore, utente non dovrebbe accorgersi della gestione)
  - SO può fare uno swapping di un intero processo riducendo il livello di multiprogrammazione (ma non si usa perché troppo costoso)
  - SO può fare page replacement combinando swapping e paging

---

## Pagina 27

Sostituzione di Pagine

frame valid–invalid bit

change to invalid

page table

reset page table for new page

victim

swap out victim page

swap desired page in

physical memory

---

## Pagina 28

Bisogno della sostituzione di pagine

logical memory for process 1

frame valid-invalid bit

page table for process 1

logical memory for process 2

frame valid-invalid bit

page table for process 2

kernel

physical memory

backing store

---

## Pagina 29

Sostituzione delle Pagine

- La sostituzione di pagine è fondamentale per il demand paging
  - completa la separazione tra la memoria logica e fisica – una larga memoria virtuale può essere ottenuta da una memoria fisica più piccola

- Previene la sovrallocazione di memoria modificando il servizio di page-fault per includere la sostituzione di pagine

- Usa bit di modifica (dirty bit) per ridurre l’overhead del transferimento di pagine – solo le pagine modificate sono scritte su disco

---

## Pagina 30

Sostituzione di Pagine

1. Trova la locazione della pagina desiderata su disco

2. Trova un frame libero:
   - se c’è un frame libero usalo
   - se non c’è usa algoritmo di page replacement per selezionare un frame vittima
   - scrivi il frame vittima su disco se il dirty bit è impostato

3. Porta la pagina desiderata nel nuovo frame libero; aggiorna la tabella di pagina e dei frame

4. Continua il processo riavviando l’istruzione che ha causato il trap

Nota: potenzialmente 2 transferimenti di pagina per page fault
- Incrementato Effective Access Time (EAT)
- Utilizzando il bit di modifica si può ridurre ad un accesso (2 solo se modifica)

---

## Pagina 31

Algoritmi di sostituzione di pagina e di frame

Per implementare il demand paging occorre:

□ Algoritmo di allocazione frame
  ► Se più processi, quanti frame assegnare ad ogni processo?

□ Algoritmo di sostituzione pagina
  ► Se sostuzione pagina quali frame sostituire?
  ► Si vuole mantenere un basso tasso di page-fault sia per il primo accesso che per il riaccesso (accesso I/O costoso anche il minimo miglioramento è importante)

---

## Pagina 32

Algoritmi di sostituzione di pagina e di frame

Per implementare il demand paging occorre:
- Algoritmo di allocazione frame
- Algoritmo di sostituzione pagina

Algoritmo valutato su una particolare stringa dei riferimenti in memoria (reference string) calcolando il numero di page fault generati
- Riferimenti generati sinteticamente o registrando accessi
- Stringa indica solo numeri di pagina, non indirizzo completo
  - Accessi ripetuti su stessa pagina non causa un page fault
  - Esempio, per la sequenza che segue, assumendo 100 bytes per pagina
    0100, 0432, 0101, 0612, 0102, 0103, 0104, 0101, 0611, 0102, 0103,
    0104, 0101, 0610, 0102, 0103, 0104, 0101, 0609, 0102, 0105
  - Si ottiene
    1, 4, 1, 6, 1, 6, 1, 6, 1
  - Risultati dipendono dal numero di frame disponibili (se un solo frame allora tutti fault)

---

## Pagina 33

Grafo dei Page Fault vs Numero di Frame

Grafo di page fault per numero di frame
- all’aumentare dei frame diminuiscono i page-fault

In tutti gli esempi che seguono la stringa dei riferimenti sarà
7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1

---

## Pagina 34

Algoritmo First-In-First-Out (FIFO)

- Sostituzione della pagina più vecchia
- Reference string: 7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1
- 3 frame (3 pagine in memoria nello stesso momento per processo)

15 page faults

- Le pagine più recenti entrano in coda le più vecchie escono
  - criterio arbitrario (es. vecchie pagine possono contenere dichiarazioni)
- Facile da implementare, ma performance varia con la reference string:
  - Si consideri 1,2,3,4,1,2,5,1,2,3,4,5
  - … Aggiungendo più frames può causare più page fault

► Anomalia di Belady

---

## Pagina 35

FIFO e anomalia di Belady

Si consideri 1,2,3,4,1,2,5,1,2,3,4,5
... aggiungere più frames può causare più page fault
Anomalia di Belady (non desiderata)

---

## Pagina 36

Algoritmo Ottimale

- Sostituisci la pagina che non verrà utilizzata per il periodo più lungo
  - Nell’esempio produce 9 page-fault
- Come si può sapere?
  - Non si può leggere nel futuro
- Usato per valutare le performance degli algoritmi

![reference string](image_url)

---

## Pagina 37

Algoritmo Least Recently Used (LRU)

- Usa la conoscenza del passato invece che quella del futuro
- Sostituisci le pagine che per più tempo non sono state usate
- Associa ad ogni pagina il tempo dell’ultimo uso

![reference string](image)

| reference string | page frames |
| :--- | :--- |
| 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1 |
| 7 0 7 0 2 0 1 2 0 3 4 0 3 4 0 3 2 1 3 2 1 0 2 1 0 7 |

- 12 fault – meglio di FIFO ma peggio di OPT
  - Con riferimento a 4 sostituisce 2 anche se subito dopo si usa
- Solitamente un buon algoritmo, frequentemente usato
  - Ottimale per l’inverso della stringa dei riferimenti
- Il problema è come implementarlo in modo efficiente ...
  - assistenza hardware può essere richiesta

---

## Pagina 38

Algoritmo Least Recently Used (LRU)

- Esercizio
- Sequenza 2 3 2 1 5 2 4 5 3 2
- Frame 3
- LRU, FIFO, OPT

---

## Pagina 39

Algoritmo Least Recently Used (LRU)

- Esercizio
- Sequenza 2 3 2 1 5 2 4 5 3 2
- Frame 3, LRU

| Rif. | Stack dopo il riferimento | Esito |
| :--- | :--- | :--- |
| 2 | 2 | F |
| 3 | 3, 2 | F |
| 2 | 2, 3 | H |
| 1 | 1, 2, 3 | F |
| 5 | 5, 1, 2 | F |
| 2 | 2, 5, 1 | H |
| 4 | 4, 2, 5 | F |
| 5 | 5, 4, 2 | H |
| 3 | 3, 5, 4 | F |
| 2 | 2, 3, 5 | F |

---

## Pagina 40

Algoritmo Least Recently Used (LRU)

- Esercizio
- Sequenza 2 3 2 1 5 2 4 5 3 2
- Frame 3
- FIFO

---

## Pagina 41

Algoritmo Least Recently Used (LRU)

- Esercizio
- Sequenza 2 3 2 1 5 2 4 5 3 2
- Frame 3, FIFO

| Rif. | Frame (ordine FIFO) | Esito |
| :--- | :--- | :--- |
| 2 | 2 - - | F |
| 3 | 2 3 - | F |
| 2 | 2 3 - | H |
| 1 | 2 3 1 | F |
| 5 | 5 3 1 | F (esce 2) |
| 2 | 5 2 1 | F (esce 3) |
| 4 | 5 2 4 | F (esce 1) |
| 5 | 5 2 4 | H |
| 3 | 3 2 4 | F (esce 5) |
| 2 | 3 2 4 | H |

---

## Pagina 42

Algoritmo Least Recently Used (LRU)

- Esercizio
- Sequenza 2 3 2 1 5 2 4 5 3 2
- Frame 3
- OPT

---

## Pagina 43

Algoritmo Least Recently Used (LRU)

□ Esercizio
□ Sequenza 2 3 2 1 5 2 4 5 3 2
□ Frame 3, OPT

Rif. Frame dopo il riferimento Esito
2 2 - - F
3 2 3 - F
2 2 3 - H
1 2 3 1 F
5 2 3 5 F, esce 1
2 2 3 5 H
4 4 3 5 F, esce 2
5 4 3 5 H
3 4 3 5 H
2 2 3 5 F, esce 4

---

## Pagina 44

Algoritmo LRU

Due possibili implementazioni

Implementazione con Counter
- Ogni elemento della tabella delle pagine ha un registro counter (time-of-use)
  - CPU ha un clock logico/contatore incrementato per riferimenti a memoria
  - Per ogni riferimento ad una pagina il clock copiato nel counter
  - Quando una pagina deve essere cambiata, cerca il valore minore del counter
  - Richiesta: ricerca attraverso la tabella e scrittura del counter per ogni accesso

Implementazione con Stack
- Mantiene uno stack di numeri di pagina
- Al riferimento di pagina si mette in cima allo stack
  - La più recente è in cima, la meno recente sul fondo
  - Con lista doppiamente linkata facile accedere al fondo e al top
  - … non viene fatta alcuna ricerca per la sostituzione
  - Approccio appropriato per realizzazione (o microcodice) software

LRU e OPT sono casi di stack algorithm senza l’anomalia di Belady
- Insieme pagine in memoria per n frame sottoinsieme di n+1
  - Per LRU le n più recenti rimangono tali anche con n+1 frame

---

## Pagina 45

Uso dello stack per registrare il più recente riferimento di pagina

Implementazione con Stack
- Mantiene uno stack di numeri di pagina
- Al riferimento di pagina si mette in cima allo stack

reference string
4 7 0 7 1 0 1 2 1 2 7 1 2
stack before a
stack after b

---

## Pagina 46

Algoritmi di Approssimazione a LRU

- LRU ha bisogno hardware speciale che non tutti i sistemi forniscono
- In alcuni casi il supporto è un bit di riferimento (reference bit)
  - Ogni pagina associata al bit di riferimento, inizialmente = 0
  - Quando si fa riferimento alla pagina (lettura o scrittura) bit settato ad 1
  - Si può sostiture qualunque pagina con bit = 0 (se esiste)
    - Non si conosce l’ordine di utilizzo …

- Algoritmo second-chance
  - È un FIFO con un reference bit
    - Dopo la selezione della pagina si controlla il bit, se 1 seconda chance
  - Aggiorna il clock
  - Se la pagina da sostituire ha
    - Reference bit = 0 -> sostituisci
    - reference bit = 1 allora:
      - setta reference bit 0, lascia la pagina in memoria
      - passa alla prossima pagina con stesse regole
  - Implementato con coda circolare

---

## Pagina 47

Second-Chance (clock) Page-Replacement Algorithm

Algoritmo second-chance
- Implementato con coda circolare
- Puntatore indica la pagina da sostituire
- Quando serve un frame avanza finché non trova uno zero
- Pagina sostituita in quella posizione
- Se tutti i bit sono 1 diventa FIFO

(a) circular queue of pages

(b) circular queue of pages

---

## Pagina 48

Second-Chance (clock) Page-Replacement Algorithm

Algoritmo second-chance
- Esempio:
- 3 frame
- Sequenza: 1 2 3 2 4 1 2 5

t1: 1 → fault
[1, -, -] (1,-,-) → 1

t2: 2 → fault
[1, 2, -] (1,1,-) → 2

t3: 3 → fault
[1, 2, 3] (1,1,1) → 0

Ora i frame sono pieni.

---

## Pagina 49

Second-Chance (clock) Page-Replacement Algorithm

Algoritmo second-chance
- Esempio:
- 3 frame
- Sequenza: 1 2 3 2 4 1 2 5

t4: 2 → hit
[1, 2, 3] (1,1,1) → 0

t5: 4 → fault

scan:
0:1→0
1:1→0
2:1→0
0:0 → sostituisco

[4, 2, 3] (1,0,0) → 1

---

## Pagina 50

Second-Chance (clock) Page-Replacement Algorithm

Algoritmo second-chance
- Esempio:
- 3 frame
- Sequenza: 1 2 3 2 4 1 2 5

t6: 1 → fault

1:0 → sostituisco

[4, 1, 3] (1,1,0) → 2

t7: 2 → fault

2:0 → sostituisco

[4, 1, 2] (1,1,1) → 0

---

## Pagina 51

Second-Chance (clock) Page-Replacement Algorithm

Algoritmo second-chance
- Esempio:
- 3 frame
- Sequenza: 1 2 3 2 4 1 2 5

t8: 5 → fault

scan:
0:1→0
1:1→0
2:1→0
0:0 → sostituisco

[5, 1, 2] (1,0,0) → 1

Quindi 7 page fault

---

## Pagina 52

Algoritmo Enhanced Second-Chance

- Migliora l’algoritmo usando insieme il reference bit ed il bit di modifica (se disponibile)

- Prendi coppie ordinate (reference, modify)
  1. (0, 0) né usata e né modificata – miglior pagina da sostituire
  2. (0, 1) non usata ma modificata – non così buona, bisogna scrivere prima della sostituzione
  3. (1, 0) usata ma non scritta – potrebbe presto essere usata di nuovo
  4. (1, 1) usata e modificata – può essere riusata e deve essere salvata prima della sostituzione

- Quando occorre una sostituzione di pagina usa lo schema clock (second chance) ma cerca una pagina della classe più bassa non vuota
  - Si potrebbe dover scorrere la lista più volte
  - Preferenza per le pagine che consentono minor I/O

---

## Pagina 53

Algoritmi Contatori

- Altri algoritmi per approssimare LRU
- Mantieni un contatore del numero di riferimenti per ogni pagina
  - Non molto usati … costosi e non approssimano bene l’ottimo

- Lease Frequently Used (LFU) Algorithm: sostituisci pagine con il contatore più basso
  - Pagine intensamente usate hanno contatori alti
  - Però alcune pagine intensamente usate solo inizialmente
    - Si può decrementare progressivamente il contatore

- Most Frequently Used (MFU) Algorithm: sostituisci pagine con contatore più alto
  - assumendo che le pagine con il contatore più basso siano le più recenti e debbano essere ancora usate

---

## Pagina 54

Algoritmi Page-Buffering

- Altri metodi possono essere utilizzati insieme a quelli page-replacement

- I sistemi mantengono un pool di frame liberi
  - Il frame è a disposizione quando occorre, non tovato a tempo di page-fault
  - Leggi la pagina in un frame libero e seleziona una vittima da aggiungere al pool
  - Quando è opportuno porta fuori la vittima

- Variazione: si mantiene lista di pagine modificate
  - Quando il sistema di paging è idle copia pagine modificate in backing store e setta il bit di modifica a non-dirty, si evitano gli accessi in memoria per copiare le pagine modificate

- Si può mantenere intatto il contenuto del frame libero
  - Se è referenziato prima del riuso non occorre ricaricare il contenuto dal disco
  - Alcune versioni di UNIX lo utilizzano con il second chance
    - Utile per ridurre la penaltà se viene selezionata una vittima sbagliata

---

## Pagina 55

Applicazioni e Sostituzione di Pagina

□ In tutti gli algoritmi presentati il SO cerca di anticipare il futuro accesso in memoria

□ Alcune applicazioni gestiscono meglio – i.e., databases

□ Applicazioni che usano intensamente la memoria possono fare buffering, quindi si può avere un doppio buffering
  □ SO mantiene copia di pagine in memoria come un I/O buffer
  □ L’applicazione mantiene la pagina in memoria per il suo funzionamento

□ SO può dare diretto accesso a queste applicazioni
  □ Raw disk mode e raw I/O
  □ Con questa modalità vengono bypassati diversi servizi, es. buffering, file locking, file name, directory, etc.

---

## Pagina 56

Allocazione di Frame

□ Come si allocano i frame per processo?

□ Caso di un sistema con 128 frame
  □ SO ne prende 35 e 93 per i processi utente
  □ Se pure demand, tutti i 93 nella lista dei frame liberi
  □ Il processo in esecuzione richiede i frame
    ► fino a 93 page fault prende pagine libere, poi sostituzione
    ► alla fine rilascio (tutti i 93 nella free frame list)

□ Molte varianti di questo approccio
  ► Si possono sempre lasciare liberi frame sulla frame list e postporre la scrittura nello swap space della vittima per sostituire
  ► Però il metodo alloca tutti i frame per un processo

---

## Pagina 57

Allocazione di Frame

- La strategia di allocazione deve tenere conto di un **minimo numero** di frame richiesti da un processo
  - Prestazioni (più frame, meno page fault)
  - Alcune istruzioni richiedono più frame, se page fault restarted
    - Dipende da architettura

- Esempio: IBM 370 – 6 pagine per l’istruzione SS MOVE:
  - istruzione di 6 byte, può richiedere fino a 2 pagine
  - 2 pagine per gestire *from*
  - 2 pagine per gestire *to*

- Il **massimo** numero dipende dai frame disponibili nel sistema

---

## Pagina 58

Allocazione di Frame

- Due principali schemi di allocazione
  - Fixed allocation
  - Priority allocation

- Molte varianti

---

## Pagina 59

Fixed Allocation

Equal allocation

- Se m frame per n processi allora alloca ad ognuno m/n
- Per esempio, se 110 frame (tolti quelli per SO) e 5 processi, per ogni processo 20 frame
- I rimanenti mantenuti come free frame buffer pool

Proportional allocation

- Però processi diversi (processo studente vs database)
- Alloca proporzionalmente alla dimensione del processo

$$\begin{array}{l}
- s_i = \text{size of process } p_i \\
- S = \sum s_i \\
- m = \text{total number of frames} \\
- a_i = \text{allocation for } p_i = \frac{s_i}{S} \times m
\end{array}$$

- Esempio: 64 frame, 2 processi ...

$$\begin{array}{l}
m = 64 \\
s_1 = 10 \\
s_2 = 127 \\
a_1 = \frac{10}{137} \times 62 \approx 4 \\
a_2 = \frac{127}{137} \times 62 \approx 57
\end{array}$$

---

## Pagina 60

Fixed Allocation

Equal e Proportional allocation
- Se aumenta il numero dei processi diminusce la memoria allocata per processo
- Problema: stessa allocazione per priorità differenti
  - Si può includere la priorità nel computo dei frame allocate

Priority allocation
- Usa uno schema di proportional allocation usando le priorità invece della dimensione

---

## Pagina 61

Rimpiazzamento Locale vs Globale

Se il processo $P_i$ genera un page fault,

- selezione per rimpiazzare uno dei suoi frame (locale)
- selezione per rimpiazzare un frame di un processo con priorità più bassa (globale)

---

## Pagina 62

Rimpiazzamento Locale vs Globale

- **Global replacement** – un processo seleziona un frame da rimpiazzare dall’insieme di tutti i frame
  - un processo può prendere un frame di un altro processo
  - … ma tempi di esecuzione di un processo possono variare molto (dipendono dalle strategie degli altri)
  - … ma più alto il throughput (quindi scelta più comune)

- **Local replacement** – ogni processo selezione solo dal suo insieme di frame allocati
  - Prestazioni più stabili e consistenti
  - … ma memoria sottoutilizzata

---

## Pagina 63

Allocazione Globale

- **Global replacement** – un processo seleziona un frame da rimpiazzare dall’insieme di tutti i frame
- Strategia per global page-replacement
  - Non si attende che la free-list si esaurisca
  - Page replacement quando sotto una soglia (tipicamente LRU approx)
  - Sotto soglia minima il kernel inizia a recuperare frame …
  - finché non va sopra la soglia massima
  - Strategie chiamate reapers

---

## Pagina 64

Allocazione Globale

□ Global replacement – un processo seleziona un frame da rimpiazzare dall’insieme di tutti i frame

□ Strategia per global page-replacement può diventare più aggressiva
  □ Se non riesce a mantenere i frame liberi può passare a strategie più aggressive
  □ In Linux se livelli troppo bassi out-of-memory (OOM) killer termina un processo
    ► Ogni processo ha un OOM score, più è alto più rischia
    ► OOM dipende dalla memoria usata, più percentuale più alto il numero
    ► Si può vedere in /proc, es., con PID 2500 /proc/2500/oom_score

□ Anche le soglie per attivare le reaper routine si possono configurare

---

## Pagina 65

Non-Uniform Memory Access

- Fino ad ora si è assunto un accesso uniforme alla memoria virtuale
- Non uniforme con **NUMA** – velocità di accesso a memoria varia
  - Considera schede con più CPU e memorie connesse con bus
  - Ogni CPU con sua memoria locale ad accesso più veloce
  - Accesso in memoria meno veloce ma maggiore parallelismo
  - Se trattato come uniforme l’accesso può essere molto rallentato
  - I frame di memoria allocati più vicino possibile alla CPU di riferimento

---

## Pagina 66

Non-Uniform Memory Access

- Fino ad ora si è assunto un accesso uniforme alla memoria virtuale
- Non uniforme con **NUMA** – velocità di accesso a memoria varia
  - allocare memoria “vicina” alla CPU su cui il thread è schedulato
  - se page-fault una memoria virtuale NUMA-aware alloca il nuovo frame vicino
  - Scheduler deve tracciare la CPU su cui gira il processo
    - allocare stessa CPU e frame vicini, con thread ancora più complicato
- Linux utilizza gerarchia di domini di scheduling
  - Scheduler limita la migrazione tra domini
  - Frame-list separate per ogni nodo NUMA
- Solaris utilizza degli **Igroups** (gruppi di località)
  - Ogni CPU nel gruppo può accedere a memoria nel gruppo con una latenza
  - Gerarchia di gruppi
  - Cerca di schedulare i thread di un processo e la memoria per quel processo all’interno del Igroup, altrimenti passa ai gruppi vicini

---

## Pagina 67

Thrashing

Se un processo non ha “abbastanza” frame, il page-fault rate è molto alto
- Page fault per avere una pagina
- Rimpiazza un frame esistente
- … ma rapidamente il frame deve essere ripreso
- Rimpiazzamento continuo di pagine …
- Questo porta a:
  - Basso utilizzo di CPU
  - SO può voler incrementare il grado di multiprogrammazione
  - Altro processo aggiunto, etc.

Thrashing ≡ un processo è occupato nello swapping di pagine in e out (più tempo in paging che in esecuzione)

---

## Pagina 68

Thrashing

- SO monitora utilizzo di CPU, se basso tende a favorire un aumento del livello di multiprogrammazione
- Algoritmo globale di page-replacement, i processi iniziano a sottrarre frame ad altri processi, a loro volta vanno in page-fault, serve il paging device per swap in e out, si accodano i processi e si svuota la coda ready … aumenta la multiprogrammazione
- L’utilizzo della CPU aumenta con la multiprogrammazione, poi va in trashing

---

## Pagina 69

Demand Paging e Thrashing

- Limitare l’effetto del thrashing usando un algoritmo di local replacement
  - Frame rimpiazzati solo localmente, non possono essere “rubati”
  - … un processo in thrashing non trascina gli altri ma …
  - … non risolto il problema, un processo in thrashing occupa il dispositivo di paging e rallenta il page fault di tutti i processi

- Per prevenire un thrashing bisogna allocare per un processo tanti frame quanti ne necessita, come si fa a sapere?
  - Guardando a quanti ne sta attualmente usando …
  - Si definisce un modello di località (locality model) del processo

- Locality Model:
  - Un processo passa da locality a locality durante l’esecuzione
  - Le località sono insiemi di pagine che sono usate insieme
  - Le località possono sovrapporsi e nuove funzioni corrispondono a nuove località
  - Località di una funzione: istruzioni, variabili locali, sottoinsieme delle globali

---

## Pagina 70

Località in una sequenza di riferimenti in memoria

Località al tempo (a)
{18-24, 29-33}

Località al tempo (b)
{18-20,24-29, 31-33}

18, 19, 20 si sovrappongono

---

## Pagina 71

Località

- Le località sono definite dalla struttura del programma e dalle sue struttura dati
- Notare che il modello di località è anche il principio che giustifica l’utilizzo delle cache
- Se si riesce ad allocare i frame per le località di un processo non genererà page fault finché non cambia la località
- Se invece non si allocano frame sufficienti per la località corrente andrà verso il thrashing

---

## Pagina 72

Modello Working Set

□ Il modello del Working Set è basato sull’assunzione di località
□ Utilizza parametro $\Delta$ per definire una working-set window
  □ I più recenti $\Delta$ riferimenti in memoria
    ► Es. 10000 instruzioni

□ L’insieme delle $\Delta$ pagine più recenti è il Working Set
  □ Se una pagina è in uso attivo è nel WS, se non è più utilizzata esce dal WS dopo $\Delta$ unità di tempo dall’ultimo suo riferimento

□ II WS approssima la località di un programma
□ Esempio con $\Delta = 10$ (dimensione di WS varia)

page reference table

$$WS(t_1) = \{1,2,5,6,7\}$$

$$WS(t_2) = \{3,4\}$$

---

## Pagina 73

Modello Working-Set

□ L’accuratezza del WS dipende da $\Delta$
□ Dim del Working Set $WSS_i$ (working set size del processo $P_i$)
  □ numero totale di pagine riferite nel più recente $\Delta$ (variabile nel tempo)
  □ se $\Delta$ troppo piccolo non contiene l’intera località
  □ se $\Delta$ troppo grande può sovrapporre più località
  □ se $\Delta = \infty \Rightarrow$ contiene tutto il programma

□ $WSS_i$ è la caratteristica curciale da monitorare
  □ $D = \Sigma WSS_i$ è la richiesta totale di frame
  □ Approssima la località
□ Se $D > m \Rightarrow$ si verifica il thrashing

□ Il SO monitora il Working Set di ogni processo
  □ Alloca frame secondo il $WSS_i$
  □ Se ci sono frame extra alloca un nuovo processo
  □ Se $D > m$ allora sospende o fa swap out di uno dei processi

---

## Pagina 74

Tracciare il Working Set

□ La finestra del Working Set è mobile
  □ Ad ogni riferimento in memoria un elemento entra, l’altro esce

□ Si può approssimare con un timer ad intervalli fissi + un bit di riferimento + bit di storia

□ Esempio: per $\Delta = 10000$
  □ Timer interrupt dopo ogni 5000 unità di tempo
  □ Mantiene in memoria 2 bit di storia per ogni pagina + bit riferimento
  □ Quando il timer interrompe copia il riferimento nella storia e setta i reference bit a 0
  □ Se bit attuale o uno di 2 bit in memoria = 1 $\Rightarrow$ la pagina è nel working set
  □ Non accurato, non sappiamo dove è avvenuto il riferimento in 5000 unità
  □ Miglioramento: 10 bit di storia e interrupt ogni 1000 unità di tempo

---

## Pagina 75

Frequenza dei Page-Fault

- Approccio più diretto del Working Set Size
- Thrashing aumenta la frequenza di page fault
- Stabilire un tasso “accettabile” di page-fault frequency (PFF) per utilizzare una politica di rimpiazzo locale
  - Se il tasso attuale è troppo basso il processo perde frame
  - Se il tasso attuale è troppo alto il processo guadagna frame
- Può essere richiesta la sospensione di un processo
  - i frame liberati possono essere distribuiti ai processi con frequenze più alte

---

## Pagina 76

Working Sets e Page Fault Rates

Relazione diretta tra working set di un processo e la frequenza di page-fault
- Working set cambia nel tempo
- Picchi e valli di frequenze di page fault indicano i cabiamenti di località
- L’intervallo tra gli inizi dei picchi definiscono il Working Set

---

## Pagina 77

Pratica Corrente

- Thrashing e swapping hanno un importante impatto sulle prestazioni
- Il trend attuale prevede l’utilizzo di memoria fisica sufficiente per evitare sia thrashing che swapping
- Mantenere tutti i working set in memoria tranne che in casi estremi

---

## Pagina 78

Compressione di Memoria

□ Si utilizza la compressione di memoria per ridurre l’utilizzo di memoria
□ Esempio:
□ Free frame list sotto soglia e selezionati frame 15, 3, 35, 26 per liberare memoria

free-frame list
head → 7 → 2 → 9 → 21 → 27 → 16

modified frame list
head → 15 → 3 → 35 → 26

□ Invece di scrivere direttamente in swap space fa la compressione di alcuni frame e li mette nei compressed frame (es. 15, 3, 35 compressi in 7 e liberati)

free-frame list
head → 2 → 9 → 21 → 27 → 16 → 15 → 3 → 35

modified frame list
head → 26

compressed frame list
head → 7

□ Quando si fa riferimento alle pagine in 7 si decomprime e rialloca

---

## Pagina 79

Compressione di Memoria

- Si utilizza la compressione di memoria per ridurre l’utilizzo di memoria
- Usato nei sistemi mobile (Android, iOS), Windows 10 e macOS
- Velocità di compressione vs riduzione di memoria (compression ratio)
  - Maggiore è la velocità minore la compressione
  - Compressione in parallelo su architetture multicore
  - Microsoft Xpress e Apple WKdm sono veloci e garantiscono buone compressioni

---

## Pagina 80

Allocare la Memoria per il Kernel

- Trattata in modo differente dalla memoria per processi utente
- Spesso allocate memoria da un pool di free-memory differente
- Due sono le ragioni principali:
  - Kernel richiede memoria per strutture di varie dimensioni, sotto la dimensione della pagina, deve usare la memoria in modo più conservative e mirato
  - La memoria del Kernel in alcuni casi necessita di essere contigua
    - I.e., dispositivi I/O che dialogano direttamente in memoria fisica, in questi casi la memoria deve essere contigua
- Di seguito si presentano due metodi per l’allocazione di memoria kernel:
  - Buddy System
  - Allocazione slab

---

## Pagina 81

Sistema Buddy

□ Alloca memoria da segmenti di dimensioni fissate che consistono di pagine fisicamente contigue
  □ Un segmento largo e contiguo suddiviso in porzioni più piccolo; più segmenti combinati rapidamente per ottenere frammento contiguo

□ Memoria allocata usando allocatore di potenza-di-2
  □ Soddisfa richieste in unità di dimensione potenza di 2
  □ Richieste approssimate alla più alta Potenza di 2
  □ Quando occorre un’allocazione più piccolo della disponibile, il chunk corrente diviso in due buddies della prossima potenza di 2 più bassa
    ► Continua finché un chunk appropriato non è disponibile

□ Per esempio, assume chunk di 256KB disponibile, il kernel richiede 21KB
  □ Diviso in $A_L$ e $A_R$ di 128KB ognuno
    ► Uno ulteriormente diviso in $B_L$ e $B_R$ di 64KB
      – Uno ulteriormente in $C_L$ e $C_R$ di 32KB ognuno – uno usato per soddisfare la richiesta

---

## Pagina 82

Buddy System Allocator

physically contiguous pages

256 KB

128 KB $A_L$
128 KB $A_R$

64 KB $B_L$
64 KB $B_R$

32 KB $C_L$
32 KB $C_R$

---

## Pagina 83

Sistema Buddy

- Alloca memoria da segmenti di dimensioni fissate che consistono di pagine fisicamente contigue
  - Un segmento largo e contiguo suddiviso in porzioni più piccolo; più segmenti combinati rapidamente per ottenere frammento contiguo

- Memoria allocata usando allocatore di potenza-di-2
  - Soddisfa richieste in unità di dimensione potenza di 2
  - Richieste approssimate alla più alta Potenza di 2
  - Quando occorre un’allocazione più piccolo della disponibile, il chunk corrente diviso in due buddies della prossima potenza di 2 più bassa
    - Continua finché un chunk appropriato non è disponibile

- Vantaggio – velocemente compatta chunk non usati in chunk più grandi

- Svantaggio – frammentazione interna
  - Sempre potenze di due, e la memoria richiesta può essere minore

---

## Pagina 84

Slab Allocator

- Strategia che elimina frammentazione interna
  - Oggetti di un certo tipo preallocati
  - Riuso di oggetti dello stesso tipo
- Slab fatto da una o più pagine fisicamente contigue
  - È il contenitore di oggetti di un certo tipo
- Una cache consiste di uno o più slab
  - Una cache per per ogni data structure del kernel
  - Ogni cache popolata di oggetti – istanze delle strutture dati

---

## Pagina 85

Slab Allocator

Strategia che elimina frammentazione interna
- Oggetti di un certo tipo preallocati
- Riuso di oggetti dello stesso tipo

Tre livelli di annidamento: cache, slab, oggetti
- Gli oggetti sono strutture dati preallocate
- Gli slab fatti da una o più pagine fisicamente contigue
  - Sono contenitori di oggetti di un certo tipo
- Le cache contengono più slab dello stesso tipo
  - Una cache per per ogni data structure del kernel
  - Ogni cache contiene slab i cui oggetti sono istanze di una struttura dati

Quando è creata la cache riempita di oggetti marcati come free
Quando le strutture sono memorizzate oggetti marcati come used

Benefici: non frammentazione, veloce soddisfazione di richieste di memoria

---

## Pagina 86

Slab Allocator in Linux

- Esempio: per process descriptor è di tipo `struct task_struct`
- Appross. 1.7KB di memoria
- Nuovo task -> alloca new struct dalla cache
  - Userà free `struct task_struct`
- Slab può essere in tre possibili stati
  1. Full – tutto usato
  2. Empty – tutto libero
  3. Partial – mix di free e used

- Su richiesta, slab allocator
  1. Usa free struct in partial slab
  2. Se non c’è, prende uno degli empty slab
  3. Se non c’è empty slab, crea un nuovo empty slab

---

## Pagina 87

Slab Allocator in Linux

- Slab iniziato in Solaris, ora diffuso sia per Kernel mode e memoria user in molti SO, in Linux da 2.2, prima solo Buddy

- Linux 2.2 aveva SLAB, ora ha allocatori SLOB e SLUB
  - SLOB per sistemi embedded con limitata memoria
    - Simple List Of Blocks – mantiene 3 liste di oggetti per piccoli, medi e grandi
    - First fit-policy per l’allocazione
  - SLUB è uno SLAB ottimizzato,
    - Introdotto da 2.6.24 per sostituire SLAB
    - Migliore utilizzo dei multicore

- Tutti questi allocator lavorano sopra il Buddy allocator
  - Il Buddy allocator fornisce pagine di memoria (frame contigui) allo slab allocator, e lo slab le usa per creare gli slab

---

## Pagina 88

Gestione Frame

Gestione memoria basso livello

kmalloc(): memoria contigua fisicamente e virtualmente
vmalloc(): memoria contigua solo virtualmente (fisicamente non contigua)

---

## Pagina 89

Gestione Frame Liberi

- La memoria allocata dal kernel (e dai processi) deve essere supportata dai frame fisici
- Occorre gestione efficiente della lista di frame liberi
  - Allocazione: si prendono frame dalla lista
  - Deallocazione: si rilasciano frame alla lista
  - Lista collegata di page_struct non fattibile
  - Il kernel gestisce l'area dei frame liberi mediante il Sistema Buddy
- L'allocatore buddy è buono per gestire grandi aree di memoria libera

---

## Pagina 90

Gestione Frame Occupati

- La memoria allocata dal kernel (e dai processi) deve essere supportata dai frame fisici
- L'allocatore a lastre (SLAB allocator) inizialmente implementato in Solaris 2.4 (1994) gestisce “cache” di porzioni di memoria
  - preallocate.
  - fisicamente contigue.
  - linearmente contigue.
- Quando il kernel chiede una porzione di memoria l'allocatore fornisce un'area preallocata dalla cache (quando la memoria è liberata, restituita alla cache)

- Uno SLAB è un insieme di pagine logiche associate a frame fisici contigui
- Uno o più SLAB contigui formano una cache:
  - Ciascuna cache è un contenitore di oggetti di un dato tipo
  - Un oggetto è un'area di memoria di una specifica dimensione
  - Funzioni: kmem_cache_create(), kmem_cache_alloc(), kmem_cache_free()
    - Anche kmem_cache_grow(), kmem_cache_shrink(), kmalloc(), kfree()
    - Allocatore buddy invocato per ottenere memoria contigua

---

## Pagina 91

Slab Allocator in Linux

- kmalloc(): allocazione generica nel kernel
- kmalloc(size, flags) alloca **memoria contigua** per uso kernel

- kmalloc() riceve una dimensione richiesta
  - es. kmalloc(100, GFP_KERNEL)

- Arrotonda alla cache più vicina
  - es. 100 byte → kmalloc-128

- Prende un oggetto libero da quella cache
  - Se la cache non ha spazio:
    - lo slab allocator crea un nuovo slab
    - chiedendo pagine al buddy allocator

  Buddy → fornisce pagine
  Slab → divide pagine in oggetti
  kmalloc → sceglie la cache giusta

---

## Pagina 92

Layout memoria x86

- Nell'architettura x86-32 lo spazio degli indirizzi lineari è diviso in due aree
  - 0-3GB. Assegnato ad ogni processo (sostituito con context-switch).
  - 3-4GB. Assegnato al kernel, non sostituito

- Nell’architettura x86-64 lo spazio di indirizzi diviso
  - 0-128TB. Assegnato ad ogni processo.
    - Sostituito ad ogni cambio contesto
  - 128TB-256TB. Assegnato al kernel, non sostituito.

---

## Pagina 93

Layout memoria x86

- Nell'architettura x86-32 lo spazio degli indirizzi lineari è diviso in due aree
  - 0-3GB. Assegnato ad ogni processo (sostituito con context-switch).
  - 3-4GB. Assegnato al kernel, non sostituito

I primi 8MB di memoria dedicati all'immagine del kernel.
Decompresso il codice del kernel all'inizio del boot. Contigui

I successivi 880MB sono direttamente mappati su frame fisici.
Possono essere liberi o allocati (per oggetti del kernel).
Contigui fisicamente.
- Frame liberi: gestiti dall'allocatore buddy.
- Frame occupati: gestiti dall'allocatore SLAB (kmalloc())

3GB (0xc0000000)
Immagine del kernel
Frame fisici
Gap
Area vmalloc
Gap
Area kmap
Area fixmap
Gap

3GB + 896MB (0xf8000000)
8MB ~880MB
8MB 120 MB
8KB ~1-6 MB
~1-2MB
8KB

4GB - 1 (0xffffffff)

---

## Pagina 94

Layout memoria x86

- Nell'architettura x86-32 lo spazio degli indirizzi lineari è diviso in due aree
  - 0-3GB. Assegnato ad ogni processo (sostituito con context-switch).
  - 3-4GB. Assegnato al kernel, non sostituito

L'area vmalloc è grande circa 120MB ed è dedicata alle porzioni di codice e dati dei moduli del kernel. I moduli sono attivati e disattivati più volte durante il ciclo di vita del kernel, l'area di memoria successiva non è garantita fisicamente contigua.

- vmalloc(): allocazione blocco.
- vfree(): deallocazione blocco.

---

## Pagina 95

Layout memoria x86

- Nell'architettura x86-32 lo spazio degli indirizzi lineari è diviso in due aree
  - 0-3GB. Assegnato ad ogni processo (sostituito con context-switch).
  - 3-4GB. Assegnato al kernel, non sostituito

L'area kmap, grande circa 1-6MB è dedicata alla creazione di mappature lineari verso frame fisici oltre il GB. Tali mapping sono di breve durata (es. operazioni di I/O)

L'area fixed map contiene pagine di 4KB i cui indirizzi lineari iniziali sono costanti (gestibili dal loader dinamico)
- set_fixmap(idx, phys)
- clear_fixmap(idx, phys)

---

## Pagina 96

Layout memoria x86-64

□ Nell’architettura x86-64 lo spazio di indirizzi diviso
□ 0-128TB. Assegnato ad ogni processo.
► Sostituito ad ogni cambio contesto
□ 128TB-256TB. Assegnato al kernel, non sostituito.

| Indirizzo iniziale | Indirizzo finale | Dimensione | Scopo |
| :--- | :--- | :--- | :--- |
| 0xffff80000000000 | 0xffff80ffffffff | 1TB | Gap |
| 0xffff81000000000 | 0xffff87ff0000000 | 16EB | Spazio non indirizzabile |
| 0xffff88000000000 | 0xffffc7ffffffff | 64TB | Frame fisici |
| 0xffffc8000000000 | 0xffffc8ffffffff | 1TB | Gap |
| 0xffffc9000000000 | 0xfffffe8ffffffff | 32TB | Area vmalloc (I/O) |
| 0xfffffe9000000000 | 0xfffffe9ffffffff | 1TB | Gap |
| 0xffffea000000000 | 0xffffeaffffffff | 1TB | Area fixmap |
| 0xffffeb000000000 | 0xffffffff7fffffff | 21TB | Non usato |
| 0xffffffff80000000 | 0xffffffffa0000000 | 512MB | Immagine del kernel |
| 0xffffffffa0000000 | 0xffffffff5fffff | 1525MB | Area moduli kernel |
| 0xffffffff600000 | 0xffffffffdfffff | 8MB | Area vsyscall |
| 0xfffffffffe00000 | 0xfffffffffffff | 2MB | Non usato |

---

## Pagina 97

Altre Considerazioni -- Prepaging

Prepaging
- Pure demand paging crea molti page fault allo start di un processo
- Occorre ridurre il numero di page fault allo start-up del processo
- Preallocare alcune delle pagine che un processo userà prima che siano riferite

- Se si utilizza il modello Working Set, si può usare WS per ripristinare le pagine quando il processo è richiamato in memoria

Costo/beneficio del prepaging
- Se pagine prepaged non usate, I/O e memoria “sprecate”
- Assumi s pagine sono prepaged con percentuale $\alpha$ delle pagine usata
  - costo di $s * \alpha$ pages fault evitati > o < del costo del prepaging $s * (1 - \alpha)$ pagine non necessarie?
  - $\alpha$ vicino $a$ zero $\Rightarrow$ prepaging perde
- Più facile fare prepaging di un file che di un programma eseguibile

---

## Pagina 98

Altre Considerazioni – Page Size

- I progettisti di SO raramente possono decide la dimensione delle pagine
- Dimensione definite in fase di progetto
  - Sempre potenza di 2, di solito nel range $2^{12}$ (4,096 bytes) fino a $2^{22}$ (4,194,304 bytes)
- Selezione della dimensione delle pagine deve tenere in considerazione:
  - Frammentazione
  - Dimensione della page table
    - Per VM di 4MB ($2^{22}$) si hanno 4096 pagine di 1024 byte e 512 da 8192 byte
  - Risoluzione
    - Si accede alla porzione di memoria necessaria
    - Minore I/O overhead
    - Maggior numero di page faults
- Pagine piccolo: località, meno frammentazione, meno I/O overhead
- Pagine grandi: meno page fault, page table più piccolo

---

## Pagina 99

Altre Considerazioni – TLB Reach

- Hit ratio della TLB – quantità di indirizzi risolti in TLB
  - Per aumentare si possono introdurre TLB con più registry, ma costoso

- TLB Reach - la quantità di memoria accessibile dalla TLB
  - TLB Reach = (TLB Size) X (Page Size)

- Idealmente, il working set di ogni processo va immagazzinato nella TLB
  - altrimenti c’è alto livello di page fault …
  - Per aumentare il reach incrementa la dimensione di pagina (es. da 4 a 16 KB)
  - … ma potrebbe portare ad un incremento della frammentazione interna dal momento che non tutte le applicazioni richiedono dimensioni grandi
  - … oppure fornire dimensioni di pagina multiple
  - Permette alle applicazioni di usare pagine grandi senza incorrere in problemi di frammentazione

- Es. Linux ha pagine di 4KB, ma anche più grandi, e.g., 2M
- Es. ARMv8 più tipi di pagine,
  - TLB entry hanno contiguous bit (riferiscono blocchi di memoria contigua)
  - es. da 64KB (16x4KB), 1GB (32x32MB), 2MB (32x64KB)

---

## Pagina 100

Altre Considerazioni – Tab Pagine inverse

- Utilizza una sola pagina con coppie <process id, numero di pagina>
- Però solo info su pagine in memoria principale
- Se page fault?

Figura 9.18 Tabella delle pagine invertita.

---

## Pagina 101

Altre Considerazioni – Tab Pagine inverse

- Utilizza una sola pagina con coppie <process id, numero di pagina>

- Però solo info su pagine in memoria principale

- Se page fault?
  - Non informazione complete su indirizzo logico della pagina referenziata
  - Demand paging richiede queste informazioni

  - Occorre leggerlo in una tabella anche questa paginata …

  - Ogni processo ha una tabella delle pagine, ma serve solo sul page fault

  - … ma anche la tabella può essere paginate e può fare page fault

  - Occorre una gestione attenta da parte del kernel

---

## Pagina 102

Altre Considerazioni – I/O interlock

□ I/O Interlock – le pagine qualche volta devono essere “locked” in memoria

□ Nel caso di I/O - pagine usate per copiare un file da un dispositivo (es. USB) devono essere locked per evitare che siano selezionate da un algoritmo di page replacement

□ Es. Processo richiede I/O, altro processo schedulato, fa page fault e sottrae pagina in global replacemente

□ Pinning (fissare) pagine da tenere in memoria

□ Lock bit per impedire il trasferimento di pagina

□ Può essere usato anche durante il paging, es. per impedire che proc. ad alta priorità prenda pagine appena caricate a proc. a bassa priorità

---

## Pagina 103

Esempi di Sistemi Operativi

- Linux
- Windows
- Solaris

---

## Pagina 104

Linux

- Per memoria virtuale Linux usa demand paging con allocazione da lista di free frame
- Global page replacement con clock approx LRU
- Due liste di pagine **active_list** e **inactive_list**, le inactive sono elegibili per essere riusate

---

## Pagina 105

Linux

Due liste di pagine **active_list** e **inactive_list**, le inactive sono elegibili per essere riusate

- Un *accessed* bit per stabilire chi ha avuto un riferimento
- Nuova pagina nel retro della active list (come ogni pagina con accesso in active)
- Il bit è peridicamente resettato
- Last Recently Used emerge sul fronte che retrocede nel retro dell’inactive
- Un demone kswapd periodicamente verifica se occorre liberare memoria, se la memoria libera va sotto soglia scorre la inactive_list e libera frame

---

## Pagina 106

Windows

- Windows 10 supporta 32 o 64 bit (IA-32, IA-64, ARM)
- Windows 11 solo 64 bit
- Supporta demand paging, copy-on-write, paging, memory compression

---

## Pagina 107

Windows

- Usa demand paging con clustering.
  - Il clustering porta in memoria pagine “vicine” alla pagina che ha generato il page fault
  - Nel caso di data page il cluster è di 3 (la pagina richiesta, quella prima e dopo), altrimenti il cluster è 7

- Elemento cruciale è la gestione del working set

---

## Pagina 108

Gestione del working set

- Ai processi sono assegnati **working set minimum** e **working set maximum**
- Working set minimum è il numero minimo di pagine che il processo è garantito avere in memoria (50 pagine)
- Al processo possono essere assignate tante pagine quanto è il suo working set maximum (345 pagine)
- I valori possono essere ignorati a meno che non è settato **hard working set limit**
- Win utilizza un LRU approx. clock con global e local replacement
- Quando la memoria è sufficiente procede allocando free memory per servire il page fault
- Quando la quantità di free memory nel sistema va sotto una soglia **automatic working set trimming** è eseguito per recuperare la quantità di free memory
- Working set trimming rimuove pagine dai processi che hanno pagine in eccesso rispetto al loro working set minimum
- Preferiti processi grandi e non attivi rispetto a quelli piccolo e attivi
- Continua finché non si raggiunge la soglia (anche sottraendo sotto il min ws)
- Trimming sia su processi utente che di sistema

---

## Pagina 109

Solaris

- Mantiene una lista di free pages da assegnare ai processi richiedenti
- **Lotsfree** – parametro soglia (quantità di free memory) per iniziare il pageout (1/64 della dimensione della memoria fisica)
- **Desfree** – parametro soglia di free memory per incrementare il paging
- Scansione 4 volte al secondo per verificare la soglia,
- Se sotto soglia **Lotsfree** inizia il processo di pageout

- **Pageout** scansiona le pagine usando un algoritmo second chance modificato
  - **Front hand**: scansione delle pagine azzerando il reference bit
  - **Back hand**: assegna le pagine non referenziate alla free list e la copia in backing store
  - La distanza tra front e back è di **handspeard**
  - Una pagina non riassegnata ma con riaccesso può essere recuperate

---

## Pagina 110

Solaris

- **Scanrate** è la frequenza di scansione delle pagine.
  - Varia da **slowscan** a **fastscan**
  - … da 100 pagine per secondo a mem-fisica/2 per secondo

- **Pageout** è chiamata più frequentemente in dipendenza dall’ammontare della free memory disponibile

- Il tempo di scansione dipende da **scanrate e handspeard** …
  - Se **scanrate** è 100 pagine al secondo e **handspeard** è 1024 allora possono passare 10 secondi tra front hand e back hand …
  - Nei sistemi reali il tempo tra front e back hand è di pochi secondi

---

## Pagina 111

Solaris

- **Pageout** fa il check di memoria 4 volte al secondo, se **desfree** è sotto soglia incrementa a 100 volte al secondo
- Se il SO non riesce a tenere **desfree** (per 30 sec) allora inizia lo swapping e libera i frame dei processi swappati
- Sotto **minfree** fa **pageout** per ogni richiesta di nuova pagina

Non fa swapping di shared pages, distingu tra pagine per processo e pagine per dati

---

