## Pagina 1

Lezione 1: Introduzione

---

## Pagina 2

Obiettivi

- Introduzione al concetto di Sistema Operativo
- Storia dei Sistemi Operativi e nozioni principali
- Descrivere l’organizzazione base di un Calcolatore
- Introdurre le principali componenti di un Sistema Operativo

---

## Pagina 3

Cos’è un Sistema Operativo?

- Un programma che gestisce le risorse di un calcolatore e fa da intermediario tra l’utente di un calcolatore e l’hardware del calcolatore

- Obiettivi di un Sistema Operativo:
  - Gestire l’esecuzione dei programmi utente
  - Semplificare l’interazione dell’utente con il calcolatore
  - Rendere efficace ed efficiente l’utilizzo del calcolatore
  - Utilizzare l’hardware in modo efficente

---

## Pagina 4

Componenti di un Sistema di Calcolo

Si possono identificare quattro componenti:

□ Hardware – fornisce le risorse computazionali di base
  ▶ CPU, memoria, dispositivi I/O

□ Sistema Operativo
  ▶ Primo strato software
  ▶ Controlla e coordina l’uso dell’hardware tra diverse applicazioni e diversi utenti

□ Programmi applicativi – usano le risorse di sistema per fornire le elaborazioni richieste dagli utenti
  ▶ Word processors, compilers, web browsers, database systems, video games

□ Utenti
  ▶ Persone, altri processi, altri calcolatori, etc.

---

## Pagina 5

Componenti di un Sistema di Calcolo

- user 1
- user 2
- user 3
- ...
- user n

- compiler
- assembler
- text editor
- database system

- system and application programs

- operating system

- computer hardware

---

## Pagina 6

Definizione di un Sistema Operativo

□ L’SO è un allocatore di risorse
  □ Gestisce tutte le risorse del calcolatore
  □ Decide tra richieste conflittuali per l’assegnazione corrette ed efficiente delle risorse

□ L’SO è un programma di controllo
  □ Controlla l’esecuzione dei programmi evitando errori e usi impropri del calcolatore

□ L’SO come macchina estesa
  □ Fornisce un’astrazione fornendo un ambiente coerente ed uniforme per l’esecuzione dei programmi

---

## Pagina 7

SO come Macchina Estesa

- Sistema Operativo trasforma il “brutto” hardware in “belle” astrazioni (Tanenbaum et al. 2013)

Tanenbaum & Bo, Modern Operating Systems:4th ed., (c) 2013 Prentice-Hall, Inc. All rights reserved.

---

## Pagina 8

Definizione di Sistema Operativo

- Non c’è una definizione universalmente accettata
- “Everything a vendor ships when you order an operating system” (Silberschatz et al.) è una buona approssimazione
- A rigore il Sistema Operativo è il programma continuamente in esecuzione che gestisce le risorse del calcolatore e orchestra l’esecuzione di programmi:
  - Chiamato il nucleo (kernel)
  - Tutto il resto:
    - se non è programma di sistema (utilità fornite con il SO) ...
    - … è un programma applicativo
- Gli argomenti del corso vertono soprattutto su kernel di SO general-purpose

---

## Pagina 9

Nucleo del Sistema Operativo

- Il nucleo del sistema (kernel) gestisce le risorse essenziali: la CPU, la memoria, le periferiche, etc. per l’esecuzione dei programmi
- Tutto il resto, anche l’interazione con l’utente, è ottenuto tramite programmi eseguiti dal kernel, che accedono alle risorse hardware tramite delle richieste a quest’ultimo.

Nei moderni SO il kernel è il solo programma ad avere il completo accesso all’hardware (modalità privilegiata), gli altri programmi vengono eseguiti dal kernel (modalità protetta).

---

## Pagina 10

Nucleo del Sistema Operativo

User mode
Web browser
E-mail reader
Music player

User interface program
Kernel mode
Operating system

Software
Hardware

Tanenbaum & Bo, Modern Operating Systems:4th ed., (c) 2013 Prentice-Hall, Inc. All rights reserved.

---

## Pagina 11

Storia Sistemi Operativi

- Prima generazione (1945–55) valvole
- Seconda generazione (1955–65) transistor e sistemi batch
- Terza generazione (1965–1980) Circuiti integrati e multiprogramming
- Quarta generazione (1980–presente) personal computer
- Quinta generazione (1990–presente) mobile computer

---

## Pagina 12

Storia Sistemi Operativi

Prima generazione (1945–55) valvole

- Non esiste Sistema Operativo, gestione manuale
- Operatore e programmatore coincidenti
- Prenotazione della macchina e uso esclusivo
- Esecuzione programma da console
  - Programma caricato in memoria un’istruzione alla volta
  - Controllo errori su spie della console

---

## Pagina 13

Storia Sistemi Operativi

□ Prima generazione (1945–55) valvole
□ Prima evoluzione
  ▶ Diffusione di periferiche (lettore/perforatore di schede, nastri, stampanti)
  ▶ Programmi di interazione con periferiche (device driver)
  ▶ Sviluppo di primo “software” di supporto
    – Librerie, compilatori (es. A-0 system 1951), linker, loader
    – … primo compilatore completo Fortran (Backus 1957)

---

## Pagina 14

Storia Sistemi Operativi

Seconda generazione (1955–65) transistor e sistemi batch

□ Separazione di operatore e programmatore

□ Eliminazione dello schema a prenotazione

► Operatore elimina parte dei tempi morti
► Batching dei lavori: batch = lotto
► Raggruppamento di programmi (job) simili nell’esecuzione

□ Monitor residente (primi esempi di Sistemi Operativi)

IBM 7094 (1962)

---

## Pagina 15

Storia Sistemi Operativi

Seconda generazione (1955–65) transistor e sistemi batch

- Raggruppamento in lotti dei lavori
- Gestione automatica dei job
- Job scritti su schede perforate
- Job Control Language
- Monitor residente (in memoria)

- Primi esempi di Sistema Operativo per sequenziamo
- Es. Fortran Monitoring System (FMS), IBSYS, etc.

Struttura di un FMS job

Esempio di scheda

---

## Pagina 16

Storia Sistemi Operativi

Seconda generazione (1955–65) transistor e sistemi batch

- Raggruppamento in lotti dei job
- Gestione automatica dei job
- Monitor residente in memoria

- Primi esempi di Sistema Operativo
- Es. Fortran Monitoring System (FMS), IBSYS, etc.
- Sequenziatore, interprete schede, caricatore
- Programmi descritti da istruzione su schede perforate
- Job descrivono come eseguire i programmi

Struttura di un FMS job

Esempio di scheda

---

## Pagina 17

Storia Sistemi Operativi

- Seconda generazione (1955–65) transistor e sistemi batch
  - Operazioni I/O lente rispetto a CPU
  - Gestione off-line di operazione I/O

(a) I programmatori portano le schede al 1401. (b) 1401 legge I lotti (batch) di lavori (jobs) in un nastro
(c) L’operatore porta nastri di input e al 7094. (d) 7094 elabora I lotti e stampa su nastro l’output
(e) l’operatore porta i nastri di output al 1401. (f) 1401 stampa l’output.

Tanenbaum & Bo, Modern Operating Systems:4th ed., (c) 2013 Prentice-Hall, Inc. All rights reserved.

---

## Pagina 18

Storia Sistemi Operativi

Evoluzione dei sistemi batch

- CPU ed I/O con una sola macchina ma disaccoppiate
- Architettura più complessa per gestione delle periferiche
- Buffering
  - Buffer per ogni dispositivo periferico per disaccoppiare letture/scritture
- Spooling (Simultaneous Peripheral Operation On Line)
  - Consente a più job di accedere ad una periferica non condivisibile
  - Ogni job scrive output in coda su disco
  - Lo spooler legge dal disco i dati e li invia uno alla volta alla periferica
- Job scheduling
  - Il disco consente l’accesso casuale ai pool di job e consente il job scheduling

---

## Pagina 19

Storia Sistemi Operativi

Terza generazione (1965–1980) Int. Circuits (ICs) e multiprogramming

Buffering e Spooling
- Buffering per parallelizzare e disaccoppiare I/O
- Spooling consente a più job accesso I/O a periferica non condivisibile

Multiprogrammazione (processamento multiplo)
- Più job contemporaneamente in competizione (pool di job)
- CPU continuamente impegnata e passa da job a job
- Job scheduling (cosa deve essere caricato per l’esecuzione)
- CPU scheduling (cosa deve essere processato)

Timesharing (CTSS at M.I.T by Corbató et al. 1962)
- Gestione esecuzione per utenti multipli (multiutenti)

Memory partitions

CPU I/O
J1 J1 J2 J2
Sequenziale

CPU I/O
J1 J2 J1 J2
Multiprogrammato

---

## Pagina 20

Storia Sistemi Operativi

Terza generazione (1965–1980) ICs e multiprogramming

Multiprogrammazione e Multiutente
- Più processi e più utenti contemporaneamente
- Condivisione delle risorse della macchina

Meccanismi di protezione
- Protezione I/O, Memoria, CPU
- SO deve sempre mantenere il controllo
- Modalità Operativa Duale (Dual Mode)
  - Superuser e User
  - Richieste al Sistema
- Protezione hardware
- Gestione memoria dedicate ai processi
- Gestione slot di tempo dedicato ad ogni processo
- Gestione dei permessi degli utenti
- Etc.

---

## Pagina 21

Storia Sistemi Operativi

Terza generazione (1965–1980) ICs e multiprogramming

MULTICS (MULTiplexed Information and Computing Service)

- MIT, Bell Labs and General Electric 1964
- Prodotto commerciale di GE nel 1967 poi Honywell
- Bell Labs esce dal progetto nel 1969, ma parte l’iniziativa Unix

- Multiutente, Multiprogrammazione, File System Multilivello
- Molto complesso, limitata diffusione commerciale

---

## Pagina 22

Storia Sistemi Operativi

Terza generazione (1965–1980) ICs e multiprogramming

Sistema Unix

- Bell Labs esce nel 1969 ma parte l’iniziativa Unix
- Progetto ripreso da Ken Thompson e Dennis Ritchie
- Semplificazione dei concetti: Unix vs Multics
- Sviluppato in linguaggio C

- Multiutente, Multiprogrammazione, File System Multilivello, Shell come processo separato
- Diversi sviluppi:
  - System V di AT&T, BSD (Berkeley Software Distribution)
  - Minix, Linux

---

## Pagina 23

Storia Sistemi Operativi

Quarta generazione (1980–presente) personal computer

- Circuiti LSI (Large Scale Integration)
- Processore 8080 Intel
  - 1974 SO CP/M (Control Program for Microcomputers)
- 1980 IBM Personal Computer
  - DOS (Disk Operating System) - QDOS
  - MS-DOS (MicroSoft Disk Operating System)
- GUI
  - Xerox PARC
  - Project Lisa and Apple Macintosh

---

## Pagina 24

Storia Sistemi Operativi

Quinta generazione (1990–presente) mobile computer

- PDA (Personal Digital Assistant), tablet, smartphone, smartwatch, etc.
- Diversi SO
  - MS Windows
  - Android
  - Apple iOS
  - PureOS, Ubuntu Touch

---

## Pagina 25

Organizzazione Calcolatore

Il Sistema Operativo è strettamente legato all’architettura del calcolatore:

- Una o più CPU ed i controllori di dispositivo (driver) sono connessi da un canale (bus) che permette l’accesso alla memoria condivisa
- La CPU e i controllori possono eseguire operazioni in parallelo competendo per l’accesso alla memoria

---

## Pagina 26

Organizzazione Calcolatore

Il Sistema Operativo è strettamente legato all’architettura del calcolatore

- Una o più CPU ed i controllori di dispositivo (driver) sono connessi da un canale (bus) che permette l’accesso alla memoria condivisa
- La CPU e i controllori possono eseguire operazioni in parallelo competendo per l’accesso alla memoria

---

## Pagina 27

Organizzazione Calcolatore

Il Sistema Operativo è strettamente legato all’architettura del calcolatore

- Una o più CPU ed i controllori di dispositivo (driver) sono connessi da un canale (bus) che permette l’accesso alla memoria condivisa
- La CPU e i controllori possono eseguire operazioni in parallelo competendo per l’accesso alla memoria

In realtà più bus (PCIe, PCI, DMI, etc.) interconnessi, il principale è PCIe (Peripheral Component Interconnect Express)

---

## Pagina 28

CPU

Central Processing Unit

Esegue le istruzioni dalla memoria:

- Ogni CPU ha un set di istruzioni che può eseguire
- Ciclo: fetch, decode, execute

---

## Pagina 29

CPU

Central Processing Unit

Esegue le istruzioni dalla memoria:

- Ogni CPU ha un set di istruzioni che può eseguire
- Ciclo: fetch, decode, execute
- Registri:
  - Program Counter, Stack Pointer, Instruction Register, Status Register
  - Memory Add. Reg., Memory Data Reg.

---

## Pagina 30

CPU

- CPU: componente hardware che esegue le istruzioni
- Processore: un chip fisico che contiene una o più CPU
- Unità di calcolo (core): unità di elaborazione di base della CPU
- Multicore: che include più unità di calcolo sulla stessa CPU
- Multiprocessore: che include più processori

Multiprocessori simmetrici

Figura 1.9 Architettura dual-core, con due unità sullo stesso chip.

---

## Pagina 31

Sistemi con Interrupt

- I dispositivi I/O e la CPU sono in esecuzione concorrente
- Ogni controllore di dispositivo è responsabile di un tipo di dispositivo
- Ogni controllore ha un buffer locale
- CPU porta dati dalla/alla memoria ai/dai buffers locali
- I/O dal dispositivo ai buffer locali del controller
- Ogni controllore informa la CPU che ha finito le sue operazioni attraverso il meccanismo delle interruzioni (interrupt)

---

## Pagina 32

Interrupt vs Polling

- **Interrupt e polling** sono due modalità con cui gli eventi generati dai dispositivi I/O possono essere gestiti dalla CPU
  - Con il **polling**, la CPU tiene traccia delle comunicazioni dei dispositivi di I/O interrogandoli ad intervalli regolari
  - Con **interrupt**, il dispositivo di I/O interrompe la CPU comunicando ad essa che ha bisogno di andare in esecuzione

---

## Pagina 33

Interruzioni

- Le interruzioni permettono di gestire le operazioni concorrenti
  - Sovrapporre CPU e operazioni I/O
  - Evitare busy waiting

- Un Sistema Operativo moderno è guidato dalle interruzioni
  - Le interruzioni trasferiscono il controllo ad una procedura di servizio dell’interruzione
  - Una volta eseguita la routine di servizio il controllo ritorna all’operazione interrotta

---

## Pagina 34

Interrupt Timeline

- Per avviare I/O la CPU carica opportuni registri del controllore I/O
- La CPU continua il processamento ...
- intanto il controllore I/O avvia le operazioni sul proprio buffer ...
- … quando ha terminato invia l’interrupt

Figura 1.3 Diagramma temporale delle interruzioni per un singolo programma che invia dati in output.

---

## Pagina 35

Interrupt Timeline

- … la CPU controlla l’interruzione periodicamente
- Determina il tipo di interruzione e gestisce l’interruzione
  - Gestore interruzione invoca la routine di servizio
- Gestita l’interruzione la CPU riprende l’elaborazione interrotta

Figura 1.3 Diagramma temporale delle interruzioni per un singolo programma che invia dati in output.

---

## Pagina 36

Gestione delle Interruzioni

CPU
1
il driver di periferica avvia l’I/O
la CPU controlla eventuali interruzioni tra un’istruzione e l’altra
la CPU riceve un’interruzione e trasferisce il controllo al gestore delle interruzioni
5
il gestore delle interruzioni elabora i dati e ritorna dall’interruzione
6
la CPU riprende l’esecuzione dell’attività interrotta

controllore di I/O
avvio dell’I/O
l’input pronto, l’output completato o un errore generano un segnale di interruzione

Figura 1.4 Ciclo di I/O guidato dalle interruzioni.

---

## Pagina 37

Gestione delle Interruzioni

- Il dispositivo I/O invia un segnale su Interrupt Request Line (IRQ)
- La CPU controlla la IRQ per ogni istruzione ...
- Due tipi di interruzione (nonmaksable/maskable)
  - Non mascherabile (errori irreversibili) – int. disable
  - Macherabile (utilizzata dai controllori di dispositivo) – int. enable

---

## Pagina 38

Gestione delle Interruzioni

Gestione interruzioni:

- Il dispositivo genera il segnale (IRQ)
- Il processore riceve il segnale e interrompe il programma in esecuzione
- Il processore informa il dispositivo che l’interrupt è stato ricevuto (ACK)
- Viene eseguita la procedura di servizio (ISR)
- Si ripristina il processo interrotto

---

## Pagina 39

Gestione delle Interruzioni

□ Il dispositivo I/O invia un segnale su Interrupt Request Line (IRQ)
□ La CPU controlla la IRQ per ogni istruzione … Fetch();
Decode();
Execute();
CheckForInterrupt();

□ Per servire la richiesta la CPU:
□ **Salva lo stato** dell’operazione interrotta
  ► minimo contesto: registri e program counter
□ **Trova l’indirizzo** della procedura di servizio (interrupt handler) …
□ **Passa il controllo** alla procedura di servizio fornendone l’indirizzo iniziale
  ► La procedura di servizio viene eseguita (salva il resto dello stato modificato)
  ► La procedura di servizio esce (interrupt handler exit)
□ Il **controllo torna** all’operazione interrotta (recuperando lo stato esecutivo)

---

## Pagina 40

Gestione delle Interruzioni

Per servire la richiesta la CPU:

□ Riceve l’interruzione
□ Determina il tipo di interruzione
□ Trova l’indirizzo della procedura di servizio (interrupt handler) …
□ Passa il controllo alla procedura di servizio fornendone l’indirizzo iniziale

□ Interrupt vettorizzato

► Il dispositivo manda un codice di interruzione
► Il codice è un indice nel vettore delle interruzioni che contiene l’inidirizzo della proc. servizio
► Il gestore dell’interruzione salva lo stato dell’operazione interrotta (registri e program counter)
► La procedura di servizio viene eseguita:
► Il controllo torna all’operazione interrotta (recuperando lo stato esecutivo)

---

## Pagina 41

Gestione delle Interruzioni

Nei SO moderni il controllore hardware di interruzione fornisce meccanismi di interruzione sofisticati:

- Posticipare le gestione dell’interruzione durante fasi critiche
- Gestione multi-livello delle priorità (altra priorità, bassa priorità)
- Gestione efficiente delle routine di servizio

(4) interrupt vector: l’IC mette sul bus l’ID dell’interrupt; la CPU seleziona l’ISR (Routine di Servizio).

Due tipi di interruzione (nonmaksable/maskable) su due line di interrupt

- Non mascherabile (errori irreversibili)
- Mascherabile (utilizzata dai controllori di dispositivo), può essere spenta dalla CPU durante le operazioni critiche

Di solito più servizi che elementi nell’interrupt vector

- Interrupt chaining (numero di interrupt punta ad una lista di interrupt handler)

---

## Pagina 42

Gestione delle Interruzioni

Nei SO moderni il controllore hardware di interruzione fornisce meccanismi di interruzione sofisticati:

- Posticipare le gestione dell’interruzione durante fasi critiche
- Gestione multi-livello (altra priorità, bassa priorità)
- Modo efficiente per lanciare il corretto gestore per un dispositivo

ARM – (GIC Generic Interrupt Controller)
x86 – (APIC Advanced Programmable Interrupt Controller)

Su ARM, il GIC centralizza tutte le interruzioni e le distribuisce ai core, supportando priorità, masking e interrupt per-core

Su x86 l’architettura APIC separa la gestione delle periferiche da quella dei core, permettendo il routing dinamico delle interruzioni.

---

## Pagina 43

Gestione delle Interruzioni

Esempio:

Pressione di un tasto sulla tastiera

► Evento asincrono da periferica, non dipende dal programma in esecuzione
► Non efficiente gestire con polling, occorrono interrupt
► Flusso di controllo:

Tasto premuto
↓
Controller della tastiera
↓
Interrupt hardware
↓
CPU sospende il programma corrente
↓
Invocata routine di servizio (ISR)
↓
codice del tasto letto e inserito in buffer del SO
↓
Il processo sospeso viene ripristinato e può successivamente chiedere il carattere al SO

---

## Pagina 44

Sistemi Operativi e Interruzioni

I Sistemi Operativi sono **interrupt driven** (hardware e software)
- Hardware interrupt da un dispositivo (asincroni)

Software interrupt (sincroni):

- **Exception** (durante l’esecuzione delle istruzioni)
  - Errori Software (e.g., division by zero)
  - Operazione non lecita
  - Accesso illegale alla memoria
  - Altri problematiche …

- **Trap** (istruzione esplicita del programma)
  - Richiesta per un **servizio** del sistema operative
  - Chiamata di Sistema syscall
  - Nel caso di exception istruzione ripetuta, trap istruzione conclusa

---

## Pagina 45

Tabella degli Eventi

Tabella degli eventi dei processori Intel, da 0 a 31 non mascherabili, da 32 a 255 mascherabili

| numero di vettore | descrizione |
| :--- | :--- |
| 0 | errore di divisione |
| 1 | eccezione di debug |
| 2 | interruzione null |
| 3 | breakpoint |
| 4 | eccezione di overflow |
| 5 | eccezione di range exceeded |
| 6 | codice operativo non valido |
| 7 | dispositivo non disponibile |
| 8 | doppio errore |
| 9 | overrun del segmento coprocessore (riservato) |
| 10 | task state segment (tss) non valido |
| 11 | segmento non presente |
| 12 | errore di stack |
| 13 | protezione generale |
| 14 | errore di pagina |
| 15 | (riservato Intel, non utilizzare) |
| 16 | errore in virgola mobile |
| 17 | controllo dell’allineamento |
| 18 | controllo della macchina |
| 19–31 | (riservato Intel, non utilizzare) |
| 32–255 | interruzioni mascherabili |

Figura 1.5 Tabella degli eventi di un processore Intel.

0-31 eccezioni, 32-255 interruzioni

---

## Pagina 46

Sistemi Operativi e Interruzioni

- Importante gestione attenta degli interrupt
- Anche un PC quasi idle gestisce continuamente interrupt
- In figura commando latency macOS su desktop
  - … in 10 secondi 23000 interrupts

---

## Pagina 47

Caratteristiche Sistema Operativo

- **Multiprogrammazione** per efficienza
  - Un singolo utente non riesce ad utilizzare al meglio CPU e dispositivi I/O
  - Multiprogrammazione organizza i jobs (codice e dati) per mantenere sempre attiva la CPU
  - Un sottinsieme dei job totali del sistema è mantenuto in memoria
  - Un job viene selezionato ed eseguito dal **job scheduler**
  - Nel caso di attesa (operazioni I/O per esempio) il SO cambia il job

- **Timesharing** (**multitasking**) la CPU che cambia job molto frequentemente permettendo agli utenti di interagire (**interactive** computing)
  - **Tempo di risposta** breve
  - Ogni utente ha programmi in esecuzione ⇒ **processi**
  - Se più jobs sono pronti per essere eseguiti ⇒ **CPU scheduling**

---

## Pagina 48

Attività del Sistema Operativo

1. Programma di avviamento (*bootstrap program*).
2. Il kernel inizia a offrire servizi al sistema e agli utenti.
3. Interruzioni ed eccezioni (*traps o exceptions*).
4. Chiamata di sistema o system call.
5. Multiprogrammazione → multitasking.

---

## Pagina 49

Memoria per Sistema a Multiprogrammazione

0
operating system
job 1
job 2
job 3
job 4
512M

---

## Pagina 50

Modalità Operativa Duale

- Sistemi multiprogrammati e multiutente richiedono meccanismi di protezione
- Operazioni in dual-mode
  - User mode e kernel mode (modo utente e supervisore)
  - Permettono all’OS di proteggersi e proteggere altri componenti

Figura 1.13 Transizione da modalità utente a modalità di sistema.

- Un bit di modalità (hardware)
  - Distinguere quando il sistema esegue codice utente o kernel
  - Alcune istruzioni sono privilegiate quindi solo eseguibili in modalità kernel
  - Interrupt/trap modalità kernel, servita l’interruzione il SO ripristina la modalità user
  - MS-DOS per Intel 8088 non aveva bit di modo

---

## Pagina 51

Protezione CPU - tempo

- Programmi utenti non devono mantenere il controllo indefinito
  - Limite temporale

- Timer per dare a SO controllo periodico della CPU
  - Timer invia segnale d’interruzione alla CPU dopo una latenza fissata
    - Contatore decrementato dal clock fisico
  - SO setta il contatore (modalità privilegiata) a zero genera un interrupt
  - Permette ad SO di riprendere il controllo o terminare processi

  - Il tempo macchina della CPU è quantizzato in ticks
  - Ogni processo viene eseguito per un certo numero di ticks e poi messo in stato di attesa.

---

## Pagina 52

Protezione Memoria

- Occorre anche proteggere la modalità di esecuzione privilegiata
- Sovrascrivendo il vettore delle interruzioni e le operazioni di servizio si potrebbe trasferire la modalità privilegiata all’utente
- Occorrono meccanismi di protezione hardwere della memoria

- Per stabilire gli indirizzi di memoria a cui un programma può accedere si possono ad esempio utilizzare due registri:
  - Registro base: più piccolo indirizzo accessibile
  - Registro limite: dimensione del range di indirizzi

---

## Pagina 53

Chiamate di Sistema

- Le interfacce con cui i programmi possono accedere all’hardware vanno sotto il nome di chiamate al sistema (system call):
  - insieme di funzioni che un programma può chiamare (viene generata un’interruzione del processo passando il controllo dal programma al kernel)

Esempio Linux

---

