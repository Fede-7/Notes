## Pagina 1

Sistemi Operativi I

Corso di Laurea in Informatica

A.A. 2025-2026

Alberto Finzi

---

## Pagina 2

Informazioni Generali

• Crediti: 9 CFU
• Orario:
  – Martedì: 16:30-18:30 aula B6
  – Mercoledì: 14:00-16:00 aula B6
  – Giovedì: 14:00-16:00 aula B6

• Dal 3/3/26 al 12/06/26

• Gruppo 1:
  – Studenti aventi il cognome con iniziali tra A e G
  – Non ammessi cambi di gruppo

---

## Pagina 3

Informazioni Generali

• Propedeuticità ingresso:
  – Architettura degli Elaboratori

• Propedeuticità uscita:
  – Laboratorio di Sistemi Operativi, Reti di calcolatori I, Operating Systems for Mobile, Cloud and IoT

---

## Pagina 4

Docente

• Docente: Alberto Finzi
• Studio: via Claudio 21, 80125 Napoli
• Ricevimento:
  – Venerdì 15:00-17:00 (Finzi), Teams

• Email: alberto.finzi@unina.it
  – Specificare SEMPRE nel subject “SO1”

• Codice Team: y0o2yh0

---

## Pagina 5

Obiettivi del Corso

Struttura e funzioni dei moderni Sistemi Operativi:

- Principi, componenti fondamentali, metodologie di progettazione e di sviluppo, algoritmi e strumenti di base

- Abilità di base nell’uso di una piattaforma a livello utente ed amministratore, principi di scripting e programmazione di sistema

- Particolare riferimento ai sistemi Unix e Linux

---

## Pagina 6

Modalità di Esame

• Prova scritta
  – Domande risposta multiple, aperte ed esercizi

• Discussione orale
  – Esercizi
  – Discussione della prova scritta
  – Domande aperte

---

## Pagina 7

Libri di Testo

Il testo di riferimento è:
- Silberschatz, Galvin, Gagne: Sistemi operativi. Concetti ed esempi, decima edizione, Pearson Education Italia

Documenti segnalati a lezione e sul sito web.

Altro testo di consultazione:

- Tanenbaum, Bos: I moderni sistemi operativi, quarta edizione, Pearson Education Italie

---

## Pagina 8

Programma di Massima

• Introduzione ai Sistemi Operativi
  • Evoluzione, strutture, architetture, componenti
• Processi
  • Il concetto di processo, stati dei processi, funzioni del kernel, algoritmi di schedulazione, sincronizzazione dei processi e deadlock
• Memoria
  • Gestione memoria principale, swapping, partizione, segmentazione e paginazione, memoria virtuale
• Sistemi I/O
  • Architetture e dispositivi di I/O, interfacce, sottosistema per I'I/O del nucleo, etc.
• Dati permanenti
  • File, metodi di allocazione, directory e metodi di accesso, file system, etc.

---

## Pagina 9

Esercitazioni in Linux

Occorre ambiente POSIX con bash

• Studenti Windows
  – WSL (Windows Subsystem for Linux)
    • Fornisce bash e strumenti POSIX
  – Macchina virtuale su Windows:
    • VMware (www.vmware.com)
  – Dual boot Linux
    • Qualunque distribuzione

• Studenti macOS
  – Sistema Operativo UNIX-based (Darwin / kernel XNU)
    • Fornisce bash e strumenti POSIX

---

## Pagina 10

Lezione 1: Introduzione

---

## Pagina 11

Obiettivi

- Introduzione al concetto di Sistema Operativo
- Storia dei Sistemi Operativi e nozioni principali
- Descrivere l’organizzazione base di un Calcolatore
- Introdurre le principali componenti di un Sistema Operativo

---

## Pagina 12

Cos’è un Sistema Operativo?

- Un programma che gestisce le risorse di un calcolatore e fa da intermediario tra l’utente di un calcolatore e l’hardware del calcolatore

- Obiettivi di un Sistema Operativo:
  - Gestire l’esecuzione dei programmi utente
  - Semplificare l’interazione dell’utente con il calcolatore
  - Rendere efficace ed efficiente l’utilizzo del calcolatore
  - Utilizzare l’hardware in modo efficente

---

## Pagina 13

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

## Pagina 14

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

## Pagina 15

Definizione di un Sistema Operativo

□ L’SO è un allocatore di risorse
  □ Gestisce tutte le risorse del calcolatore
  □ Decide tra richieste conflittuali per l’assegnazione corrette ed efficiente delle risorse

□ L’SO è un programma di controllo
  □ Controlla l’esecuzione dei programmi evitando errori e usi impropri del calcolatore

□ L’SO come macchina estesa
  □ Fornisce un’astrazione fornendo un ambiente coerente ed uniforme per l’esecuzione dei programmi

---

## Pagina 16

SO come Macchina Estesa

- Sistema Operativo trasforma il “brutto” hardware in “belle” astrazioni (Tanenbaum et al. 2013)

Tanenbaum & Bo, Modern Operating Systems:4th ed., (c) 2013 Prentice-Hall, Inc. All rights reserved.

---

## Pagina 17

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

## Pagina 18

Nucleo del Sistema Operativo

- Il nucleo del sistema (kernel) gestisce le risorse essenziali: la CPU, la memoria, le periferiche, etc. per l’esecuzione dei programmi
- Tutto il resto, anche l’interazione con l’utente, è ottenuto tramite programmi eseguiti dal kernel, che accedono alle risorse hardware tramite delle richieste a quest’ultimo.

Nei moderni SO il kernel è il solo programma ad avere il completo accesso all’hardware (modalità privilegiata), gli altri programmi vengono eseguiti dal kernel (modalità protetta).

---

## Pagina 19

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

## Pagina 20

Storia Sistemi Operativi

- Prima generazione (1945–55) valvole
- Seconda generazione (1955–65) transistor e sistemi batch
- Terza generazione (1965–1980) Circuiti integrati e multiprogramming
- Quarta generazione (1980–presente) personal computer
- Quinta generazione (1990–presente) mobile computer

---

## Pagina 21

Storia Sistemi Operativi

Prima generazione (1945–55) valvole

- Non esiste Sistema Operativo, gestione manuale
- Operatore e programmatore coincidenti
- Prenotazione della macchina e uso esclusivo
- Esecuzione programma da console
  - Programma caricato in memoria un’istruzione alla volta
  - Controllo errori su spie della console

---

## Pagina 22

Storia Sistemi Operativi

□ Prima generazione (1945–55) valvole
□ Prima evoluzione
  ▶ Diffusione di periferiche (lettore/perforatore di schede, nastri, stampanti)
  ▶ Programmi di interazione con periferiche (device driver)
  ▶ Sviluppo di primo “software” di supporto
    – Librerie, compilatori (es. A-0 system 1951), linker, loader
    – … primo compilatore completo Fortran (Backus 1957)

---

## Pagina 23

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

## Pagina 24

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

## Pagina 25

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

## Pagina 26

Storia Sistemi Operativi

- Seconda generazione (1955–65) transistor e sistemi batch
  - Operazioni I/O lente rispetto a CPU
  - Gestione off-line di operazione I/O

(a) I programmatori portano le schede al 1401. (b) 1401 legge I lotti (batch) di lavori (jobs) in un nastro
(c) L’operatore porta nastri di input e al 7094. (d) 7094 elabora I lotti e stampa su nastro l’output
(e) l’operatore porta i nastri di output al 1401. (f) 1401 stampa l’output.

Tanenbaum & Bo, Modern Operating Systems:4th ed., (c) 2013 Prentice-Hall, Inc. All rights reserved.

---

## Pagina 27

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

## Pagina 28

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

## Pagina 29

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

## Pagina 30

Storia Sistemi Operativi

Terza generazione (1965–1980) ICs e multiprogramming

MULTICS (MULTiplexed Information and Computing Service)

- MIT, Bell Labs and General Electric 1964
- Prodotto commerciale di GE nel 1967 poi Honywell
- Bell Labs esce dal progetto nel 1969, ma parte l’iniziativa Unix

- Multiutente, Multiprogrammazione, File System Multilivello
- Molto complesso, limitata diffusione commerciale

---

## Pagina 31

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

## Pagina 32

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

## Pagina 33

Storia Sistemi Operativi

Quinta generazione (1990–presente) mobile computer

- PDA (Personal Digital Assistant), tablet, smartphone, smartwatch, etc.
- Diversi SO
  - MS Windows
  - Android
  - Apple iOS
  - PureOS, Ubuntu Touch

---

## Pagina 34

Organizzazione Calcolatore

Il Sistema Operativo è strettamente legato all’architettura del calcolatore:

- Una o più CPU ed i controllori di dispositivo (driver) sono connessi da un canale (bus) che permette l’accesso alla memoria condivisa
- La CPU e i controllori possono eseguire operazioni in parallelo competendo per l’accesso alla memoria

---

## Pagina 35

Organizzazione Calcolatore

Il Sistema Operativo è strettamente legato all’architettura del calcolatore

- Una o più CPU ed i controllori di dispositivo (driver) sono connessi da un canale (bus) che permette l’accesso alla memoria condivisa
- La CPU e i controllori possono eseguire operazioni in parallelo competendo per l’accesso alla memoria

---

## Pagina 36

Organizzazione Calcolatore

Il Sistema Operativo è strettamente legato all’architettura del calcolatore

- Una o più CPU ed i controllori di dispositivo (driver) sono connessi da un canale (bus) che permette l’accesso alla memoria condivisa
- La CPU e i controllori possono eseguire operazioni in parallelo competendo per l’accesso alla memoria

In realtà più bus (PCIe, PCI, DMI, etc.) interconnessi, il principale è PCIe (Peripheral Component Interconnect Express)

---

## Pagina 37

CPU

Central Processing Unit

Esegue le istruzioni dalla memoria:

- Ogni CPU ha un set di istruzioni che può eseguire
- Ciclo: fetch, decode, execute

---

## Pagina 38

CPU

Central Processing Unit

Esegue le istruzioni dalla memoria:

- Ogni CPU ha un set di istruzioni che può eseguire
- Ciclo: fetch, decode, execute
- Registri:
  - Program Counter, Stack Pointer, Instruction Register, Status Register
  - Memory Add. Reg., Memory Data Reg.

---

## Pagina 39

CPU

- CPU: componente hardware che esegue le istruzioni
- Processore: un chip fisico che contiene una o più CPU
- Unità di calcolo (core): unità di elaborazione di base della CPU
- Multicore: che include più unità di calcolo sulla stessa CPU
- Multiprocessore: che include più processori

Multiprocessori simmetrici

Figura 1.9 Architettura dual-core, con due unità sullo stesso chip.

---

## Pagina 40

Sistemi con Interrupt

- I dispositivi I/O e la CPU sono in esecuzione concorrente
- Ogni controllore di dispositivo è responsabile di un tipo di dispositivo
- Ogni controllore ha un buffer locale
- CPU porta dati dalla/alla memoria ai/dai buffers locali
- I/O dal dispositivo ai buffer locali del controller
- Ogni controllore informa la CPU che ha finito le sue operazioni attraverso il meccanismo delle interruzioni (interrupt)

---

## Pagina 41

Interrupt vs Polling

- **Interrupt e polling** sono due modalità con cui gli eventi generati dai dispositivi I/O possono essere gestiti dalla CPU
  - Con il **polling**, la CPU tiene traccia delle comunicazioni dei dispositivi di I/O interrogandoli ad intervalli regolari
  - Con **interrupt**, il dispositivo di I/O interrompe la CPU comunicando ad essa che ha bisogno di andare in esecuzione

---

## Pagina 42

Interruzioni

- Le interruzioni permettono di gestire le operazioni concorrenti
  - Sovrapporre CPU e operazioni I/O
  - Evitare busy waiting

- Un Sistema Operativo moderno è guidato dalle interruzioni
  - Le interruzioni trasferiscono il controllo ad una procedura di servizio dell’interruzione
  - Una volta eseguita la routine di servizio il controllo ritorna all’operazione interrotta

---

## Pagina 43

Interrupt Timeline

- Per avviare I/O la CPU carica opportuni registri del controllore I/O
- La CPU continua il processamento ...
- intanto il controllore I/O avvia le operazioni sul proprio buffer ...
- … quando ha terminato invia l’interrupt

Figura 1.3 Diagramma temporale delle interruzioni per un singolo programma che invia dati in output.

---

## Pagina 44

Interrupt Timeline

- … la CPU controlla l’interruzione periodicamente
- Determina il tipo di interruzione e gestisce l’interruzione
  - Gestore interruzione invoca la routine di servizio
- Gestita l’interruzione la CPU riprende l’elaborazione interrotta

Figura 1.3 Diagramma temporale delle interruzioni per un singolo programma che invia dati in output.

---

## Pagina 45

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

## Pagina 46

Gestione delle Interruzioni

- Il dispositivo I/O invia un segnale su Interrupt Request Line (IRQ)
- La CPU controlla la IRQ per ogni istruzione ...
- Due tipi di interruzione (nonmaksable/maskable)
  - Non mascherabile (errori irreversibili) – int. disable
  - Macherabile (utilizzata dai controllori di dispositivo) – int. enable

---

## Pagina 47

Gestione delle Interruzioni

Gestione interruzioni:

- Il dispositivo genera il segnale (IRQ)
- Il processore riceve il segnale e interrompe il programma in esecuzione
- Il processore informa il dispositivo che l’interrupt è stato ricevuto (ACK)
- Viene eseguita la procedura di servizio (ISR)
- Si ripristina il processo interrotto

---

## Pagina 48

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

## Pagina 49

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

## Pagina 50

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

## Pagina 51

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

## Pagina 52

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

## Pagina 53

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

## Pagina 54

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

## Pagina 55

Sistemi Operativi e Interruzioni

- Importante gestione attenta degli interrupt
- Anche un PC quasi idle gestisce continuamente interrupt
- In figura commando latency macOS su desktop
  - … in 10 secondi 23000 interrupts

---

## Pagina 56

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

## Pagina 57

Attività del Sistema Operativo

1. Programma di avviamento (*bootstrap program*).
2. Il kernel inizia a offrire servizi al sistema e agli utenti.
3. Interruzioni ed eccezioni (*traps o exceptions*).
4. Chiamata di sistema o system call.
5. Multiprogrammazione → multitasking.

---

## Pagina 58

Memoria per Sistema a Multiprogrammazione

0
operating system
job 1
job 2
job 3
job 4
512M

---

## Pagina 59

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

## Pagina 60

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

## Pagina 61

Protezione Memoria

- Occorre anche proteggere la modalità di esecuzione privilegiata
- Sovrascrivendo il vettore delle interruzioni e le operazioni di servizio si potrebbe trasferire la modalità privilegiata all’utente
- Occorrono meccanismi di protezione hardwere della memoria

- Per stabilire gli indirizzi di memoria a cui un programma può accedere si possono ad esempio utilizzare due registri:
  - Registro base: più piccolo indirizzo accessibile
  - Registro limite: dimensione del range di indirizzi

---

## Pagina 62

Chiamate di Sistema

- Le interfacce con cui i programmi possono accedere all’hardware vanno sotto il nome di chiamate al sistema (system call):
  - insieme di funzioni che un programma può chiamare (viene generata un’interruzione del processo passando il controllo dal programma al kernel)

Esempio Linux

---

## Pagina 63

Gestione Risorse

Gestione dei processi
Gestione della memoria
Gestione dei file
Gestione della memoria di massa
Gestione della cache
Gestione dell’I/O

---

## Pagina 64

Gestione Processi

- Un processo è un programma in esecuzione. Il programma è una entità passiva, il processo è una entità attiva.

- Un processo ha bisogno di risorse per svolgere un task
  - CPU, memoria, I/O, files
  - Dati di inizializzazione

- Alla terminazione di un processo occorre il rilascio e recupero delle risorse

- Processi single-threaded hanno un program counter (locazione prossima istruzione da eseguire)
  - Istruzioni sequenziali, una alla volta, fino a completamento

- Processi multi-threaded hanno un program counter per thread

- Tipicamente i sistemi hanno in esecuzione molti processi, per più utenti, in esecuzione concorrente su una o più CPU

---

## Pagina 65

Gestione Processi

Il Sistema Operativo fornisce diversi meccanismi per la gestione dei processi, in particolare per:

- Creazione e cancellazione di utenti e processi di sistema
- Sospensione e resume di processi
- Sincronizzazione di processi
- Communicazione tra processi
- Gestione del deadlock

Process tree. Process A crea due processi figli, B e C. Il processo B crea 3 processi figli, D, E e F.

---

## Pagina 66

Gestione Processi

Il Sistema Operativo fornisce diversi meccanismi per la gestione dei processi, in particolare per:

- Creazione e cancellazione di utenti e processi di sistema
- Sospensione e resume di processi
- Sincronizzazione di processi
- Communicazione tra processi
- Gestione del deadlock

Process management

| Call | Description |
| :--- | :--- |
| pid = fork() | Create a child process identical to the parent |
| pid = waitpid(pid, &statloc, options) | Wait for a child to terminate |
| s = execve(name, argv, environp) | Replace a process’ core image |
| exit(status) | Terminate process execution and return status |

---

## Pagina 67

Gestione Memoria Principale

- Per eseguire un programma, istruzioni e dati devono essere caricati in memoria principale

- Attività di gestione della memoria:
  - Tenere traccia di quali parti della memoria sono attualmente utilizzate e da quale processo
  - Decidere quali processi (o parti di essi) e dati spostare dentro e fuori alla/dalla memoria
  - Allocazione e deallocazione dello spazio di memoria secondo necessità

---

## Pagina 68

Gestione Archiviazone

- Il sistema operativo fornisce una rappresentazione logica e uniforme dell'archiviazione delle informazioni
  - Astrazione di proprietà fisiche
  - Unità logica di archiviazione è il file

- Gestione del File-System
  - Files tipicamente organizzati gerarchicamente in directory (multilivello)

---

## Pagina 69

Gestione Archiviazone

- Il sistema operativo fornisce una rappresentazione logica e uniforme dell'archiviazione delle informazioni
  - Astrazione di proprietà fisiche
  - Unità logica di archiviazione è il file

- Gestione del File-System
  - File tipicamente organizzati gerarchicamente in directory
  - Controllo dell'accesso per determinare chi può accedere a cosa
  - Il SO gestisce
    - Creazione e cancellazione file e directory
    - Primitive per modifica di file e directorie
    - Mapping di file nella memoria secondaria
    - Backup di file su memoria non-volatile

---

## Pagina 70

Strutture di Memoria

- Memoria Principale che la CPU può accedere direttamente
  - Random access memory (RAM)
  - Tipicamente volatile

- Memoria non volatile
  - Es. ROM, PROM, EPROM, EEPROM (Eletronicamente canc. e progr.)

- Memoria Secondaria
  - Estensione della memoria principale che fornisce capacità di memorizzazione non-volatile
  - Hard-disk drive (hdd)
    - Disco logicamente diviso in tracce suddivise in settori
  - Disco a stato solido (ssd)
    - più veloce, accesso casuale uniforme, tempi di accesso brevi

---

## Pagina 71

Gerarchia di Memorie

Memorie organizzate in gerarchie

- Velocità
- Costo
- Volatilità

Figura 1.6 Scala gerarchica dei sistemi di memorizzazione.

---

## Pagina 72

Varie Forme di Archiviazione dei Dati

| Livello | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Nome | registri | cache | memoria centrale | disco a stato solido | disco magnetico |
| Dimensione tipica | < 1 KB | < 16 MB | < 64 GB | < 1 TB | < 10 TB |
| Tecnologia | memoria dedicata con porte multiple (CMOS) | CMOS SRAM (on-chip o off-chip) | CMOS DRAM | memoria flash | disco magnetico |
| Tempo d’accesso (ns) | 0,25 – 0,5 | 0,5 – 25 | 80 – 250 | 25.000-50.000 | 5.000,000 |
| Ampiezza di banda (MB/s) | 20.000 – 100.000 | 5000 – 10.000 | 1000 – 5000 | 500 | 20 – 150 |
| Gestito da compilatore | hardware | sistema operativo | sistema operativo | sistema operativo |
| Supportato da cache | memoria centrale | disco | disco | disco o nastro |

Figura 1.14 Caratteristiche di varie forme di archiviazione dei dati.

---

## Pagina 73

Caching

- Principio valido a diversi livelli (hardware, SO, software)
- Informazione temporaneamente copiata da memoria più lenta a più veloce

Figura 1.15 Migrazione di un intero A da un disco a un registro.

- Memoria più veloce (cache) considerate per prima cercando un dato
  - Se il dato c’è, viene immediatamente utilizzato (veloce)
  - Se non c’è, viene copiato in cache ed usato

- Problematiche della memoria cached
  - Gestione della cache
  - Dimensione della cache e politica di replicazione

---

## Pagina 74

Sistemi I/O

- Il Sistema Operativo deve nascondere all’utente le specificità hardware dei dispositivi fornendo un’interfaccia uniforme

- Sottosistemi I/O responsabili di
  - Gestione della memoria di I/O incluso buffering (memorizzazione temporanea dei dati durante il trasferimento), memorizzazione nella cache, spooling (sovrapposizione dell’accesso a periferica di più job)
  - Interfaccia generica per i dispositivi
  - Driver per dispositivi hardware specifici

---

## Pagina 75

Servizi degli SO

I sistemi operativi forniscono un ambiente per l'esecuzione di programmi e servizi a programmi e utenti

Interfaccia con l’utente
Esecuzione di un programma
Operazioni di I/O
Gestione del file system
Comunicazioni
Rilevamento di errori

---

## Pagina 76

Servizi di Sistemi Operativi

I sistemi operativi forniscono un ambiente per l'esecuzione di programmi e servizi a programmi e utenti

□ Interfaccia Utente – quasi tutti i sistemi le forniscono (UI).
► Diversi tipi Command-Line (CLI), Graphics User Interface (GUI), Batch

□ Esecuzione di Programmi - Il sistema deve essere in grado di caricare un programma in memoria ed eseguire quel programma, terminare l'esecuzione, normalmente o in modo anomalo

□ Operazioni I/O - Un programma in esecuzione può richiedere I/O, che può coinvolgere un file o un dispositivo I/O.
► Il SO deve nascondere la complessità del dispositivo offrendo agli utenti un interfaccimento semplice ed uniforme

---

## Pagina 77

Servizi degli SO

Un insieme di servizi del sistema operativo:

□ Gestione File-system - I programmi devono leggere e scrivere file e directory, crearli ed eliminarli, ricercarli, elencare le informazioni sui file, gestire i permessi. Accesso frequenti richiede gestione oculata.

□ Comunicazione – I processi possono scambiare informazioni, sullo stesso computer o tra computer in una rete

□ Rilevamento di Errori – Il sistema operativo deve essere costantemente consapevole di possibili errori

► Può verificarsi nella CPU e nell'hardware di memoria, nei dispositivi I/O, nel programma utente
► Per ogni tipo di errore, il sistema operativo dovrebbe intraprendere l'azione appropriata per garantire un'elaborazione corretta e coerente
► Le funzionalità di debug possono migliorare notevolmente le capacità dell'utente e del programmatore di utilizzare in modo efficiente il sistema

---

## Pagina 78

Servizi degli SO

Insieme di funzioni del sistema operativo per garantire il funzionamento efficiente del sistema stesso tramite la condivisione delle risorse

- Allocazione delle risorse - quando più utenti o più lavori vengono eseguiti contemporaneamente, le risorse devono essere allocate a ciascuno di essi
  - Molti tipi di risorse - cicli CPU, memoria principale, file, dispositivi I/O.

- Contabilità - tenere traccia di quali utenti utilizzano quanto e quali tipi di risorse del computer

- Protezione e sicurezza - I proprietari delle informazioni archiviate in un sistema informatico multiutente o in rete devono poter controllare l'uso di tali informazioni, processi simultanei non devono interferire tra loro
  - La protezione deve garantire che l'accesso da parte di processi ed utenti (interni) alle risorse di sistema sia controllato
  - La sicurezza rispetto ad accessi esterni richiede l'autenticazione dell'utente e prevede la difesa dei dispositivi I/O esterni da accessi non consentiti

---

## Pagina 79

Panoramica dei Servizi di un SO

I processi utente accedono ai servizi del Sistema Operativo mediante chiamate di sistema:

- Istruzioni che invocano servizi gestiti dal Kernel

user and other system programs
GUI
batch
command line
user interfaces

system calls
program execution
I/O operations
file systems
communication
resource allocation
accounting
error detection
services
protection and security

operating system
hardware

---

## Pagina 80

Interfaccia Utente - CLI

L'interprete dei comandi consente l'immissione diretta dei comandi

- A volte implementato nel kernel, a volte dal programma di sistema
- A volte più interfacce – shells
- Principalmente recupera un comando dall'utente e lo esegue

---

## Pagina 81

Interfaccia Utente - GUI

Interfaccia grafica (Graphic User Interface)
- Interfaccia che usa la metafora del desktop
- Mouse, tastiera, schermo
- Le icone rappresentano file, programmi, azioni, ecc
- Inventata a Xerox PARC

---

## Pagina 82

Altre Interfacce Utente

- Interfacce touch-screen
  - Senza mouse
  - Gesti per attivare azioni
- Comandi vocali
- Etc.

---

## Pagina 83

Panoramica dei Servizi di un SO

I processi utente accedono ai servizi del Sistema Operativo mediante chiamate di sistema:
- Istruzioni che invocano servizi gestiti dal Kernel
- ABI (Application Binary Interface) tra
- Chiamate mediante API che le incapsulano

user and other system programs
GUI batch command line
user interfaces

system calls
program execution
I/O operations
file systems
communication
resource allocation
accounting
error detection
services
protection and security

operating system
hardware

---

## Pagina 84

Chiamate di Sistema

□ Le **chiamate di sistema** (*system call*) costituiscono un’interfaccia per i servizi resi disponibili dal sistema operativo

□ Chiamate dai programmi mediante **Application Programming Interface** (API)

□ Tra le API più comuni citiamo:
  □ **Win API**: API C per Windows (kernal32.dll, User32.dll, etc.)
  □ **POSIX API**: API C per POSIX-based systems (incluse tutte le versioni UNIX, Linux e MacOS) - **Portable Operating System Interface**
  □ **Java API**: API per la Java virtual machine (JVM)

---

## Pagina 85

Esempio di Chiamata di Sistema

- Chiamata di sistema per copiare il contenuto di un file in un altro file

cp in.txt out.txt

Esempio di sequenza di chiamate di sistema
Acquisisce il nome del file in ingresso
Scrive messaggio di richiesta sullo schermo
Accetta i dati in ingresso
Acquisisce il nome del file in uscita
Scrive messaggio di richiesta sullo schermo
Accetta i dati in ingresso
Apre il file in ingresso
Se il file non esiste, termina con errore
Crea il file in uscita
Se il file esiste, termina con errore
Ripete
Legge dal file in ingresso
Scrive sul file in uscita
Finché c’è ancora da leggere
Chiude il file in uscita
Scrive messaggio sullo schermo per informare del completamento
Termina senza errori

programma (cp)
API POSIX / libc
system call
kernel

Figura 2.5 Esempio d’uso delle chiamate di sistema.

---

## Pagina 86

Esempio di API standard

API: Specifica un insieme di funzioni a disposizione del programmatore e dettaglia i parametri necessari per l’invocazione di queste funzioni insieme ai valori restituiti

Come esempio di API standard consideriamo la funzione `read()` disponibile in Unix e Linux. L’API per questa funzione si può ottenere digitando

```c
man read
da riga di comando. Una descrizione di questa API è la seguente:

#include <unistd.h>

ssize_t read(int fd, void *buf, size_t count)
{
valore nome parametri
restituito della funzione
```

Un programma che utilizza la `read()` deve includere il file `unistd.h` che, tra le altre cose, definisce i tipi di dato `ssize_t` e `size_t`. Il parametri passati alla `read()` sono i seguenti:

• `int fd` — il descrittore del file da leggere
• `void *buf` — un buffer nel quale vengono messi i dati letti
• `size_t count` — il massimo numero di byte da leggere e inserire nel buffer

Quando una `read()` è completata con successo viene restituito il numero di byte letti. La `read()` restituisce 0 in caso di fine del file e –1 quando si è verificato un errore.

---

## Pagina 87

Relazione tra API e Chiamata

- Tipicamente un numero è associato per ogni chiamata (la system-call interface mantiene una tabella indicizzata)
- L’interfaccia invoca la chiamata nel kernel e restituisce lo status e valore di ritorno (dettagli nascosti gestiti da librerie di supporto)

Figura 2.6 Gestione della chiamata di sistema open() invocata da un’applicazione utente.

---

## Pagina 88

Passaggio dei parametri

- Tre metodi generali utilizzati per passare i parametri al sistema operativo
  - Passa direttamente i parametri nei registri (a volte troppi parametri)
  - Parametri in un blocco, o tabella, in memoria e indirizzo del blocco passato come parametro in un registro (Linux e Solaris)
  - Parametri inseriti nello stack dal programma e estratti dallo stack dal SO

---

## Pagina 89

Passaggio dei parametri

□ Tre metodi generali utilizzati per passare i parametri al sistema operativo

□ Passa direttamente i parametri nei registri (a volte troppi parametri)

► In GNU/Linux, una chiamata di sistema accetta al più sei parametri

► Es. nell'architettura Intel il registro eax (32 bit) o rax (64 bit) contiene sempre un identificatore numerico univoco della chiamata di sistema

► Altri registri (x64)

  * rax system call number/val ritorno
  * rdi arg0
  * rsi arg1
  • rdx arg2
  • r10 arg3
  • r8 arg4
  • r9 arg5

Es. write(fd, msg, 12)

mov rax, 1 ; numero syscall write
mov rdi, 1 ; fd (stdout)
mov rsi, msg ; buffer
mov rdx, 12 ; lunghezza
syscall

---

## Pagina 90

Passaggio dei parametri

- Tre metodi generali utilizzati per passare i parametri al sistema operativo
  - Passa direttamente i parametri nei registri (a volte troppi parametri)
  - Parametri in un blocco, o tabella, in memoria e indirizzo del blocco passato come parametro in un registro (Linux e Solaris)
    - es. con rdi = x si può puntare al blocco

Figura 2.7 Passaggio di parametri in forma di tabella.

---

## Pagina 91

Chiamata di Sistema

- Parametri inseriti nello stack dal programma e estratti dallo stack dal SO
- Programma in C invoca una chiamata di sistema:
  - Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`
  - Restituisce numero byte o -1 nel var globale errno

Il programma chiamante predispone la chiamata mettendo prima i parametri in uno stack (passi 1–3) – il buffer passato per riferimento

La procedura chiama il read (passo 4) mettendo il codice della chiamata a sistema di read in un registro atteso dal Kernel

Quindi manda una istruzione *Trap* al kernel e passa il controllo al kernel in kernel mode (passi 5-6)

Il kernel trova il codice della chiamata e mediante una tabella trova l’handler della call (passi 7 e 8) finita l’esecuzione passa il risultato al chiamante (passo 9)

Il chiamante riprende il controllo in user mode (passo 10) e pulisce lo stack (passo 11) incrementando lo Stack Pointer (SP)

---

## Pagina 92

Chiamata di Sistema

- Parametri inseriti nello stack dal programma e estratti dallo stack dal SO
- Programma in C invoca una chiamata di sistema:
  - Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`
  - Restituisce numero byte o -1 nel var globale errno

Nei sistemi Linux moderni (x86-64) i parametri delle system call sono passati **nei registri**, non nello stack.

Lo stack è usato solo per la chiamata alla funzione della libreria (read, write, ecc.). La sequenza è quindi

```text
programma C
call read() ← stack
libc wrapper (sposta i parametri nei registri)
registri syscall
syscall
kernel
```

---

## Pagina 93

Chiamata di Sistema

- Parametri inseriti nello stack dal programma e estratti dallo stack dal SO
- Programma in C invoca una chiamata di sistema:
  - Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`
  - Restituisce numero byte o -1 nel var globale errno (registo rax)

Le procedure POSIX non si mappano sempre uno a uno con le system call offerte dal SO

Nella maggior parte dei casi chiamano effettivamente le sys call. Alcune eseguono operazioni senza fare il TRAP del kernel

---

## Pagina 94

Tipi di Chiamate di Sistema

- Controllo di processi
  - Creare e terminare processi
  - Caricare, eseguire processi
  - Ottenere e settare attributi di processo
  - Attese di tempo
  - Attese di eventi/segnali
  - Allocare memoria
  - Debugger per determinare bug
  - Meccanismi di regolazione per gestire l’accesso a dati condivisi

---

## Pagina 95

Funzioni per System Call

- Controllo di processi
  - Funzioni di libreria C per l’invocazione di syscall
  - Interfaccia POSIX delle system call

```c
#include <sys/types.h>
# include <unistd.h>

pid_t getpid(void);  identificativo del processo
pid_t getppid(void);  identificativo del genitore

pid_t fork(void);        pid_t wait(int *status);
pid_t vfork(void);

pid_t pid;

if ( (pid=fork()) < 0 )
    perror("fork"), exit(1);
else if (pid != 0) {
    // codice del padre
} else {
    // codice del figlio
}
```

---

## Pagina 96

Tipi di Chiamate di Sistema

- Gestione di File
  - create file, delete file
  - open, close file
  - read, write, reposition
  - get and set file attributes

- Gestione di dispositivi
  - request device, release device
  - read, write
  - get device attributes, set device attributes
  - logically attach or detach devices

---

## Pagina 97

Servizi degli SO

I sistemi operativi forniscono un ambiente per l'esecuzione di programmi e servizi a programmi e utenti

Interfaccia con l’utente
Esecuzione di un programma
Operazioni di I/O
Gestione del file system
Comunicazioni
Rilevamento di errori

---

## Pagina 98

Servizi di Sistemi Operativi

I sistemi operativi forniscono un ambiente per l'esecuzione di programmi e servizi a programmi e utenti

□ Interfaccia Utente – quasi tutti i sistemi le forniscono (UI).
► Diversi tipi Command-Line (CLI), Graphics User Interface (GUI), Batch

□ Esecuzione di Programmi - Il sistema deve essere in grado di caricare un programma in memoria ed eseguire quel programma, terminare l'esecuzione, normalmente o in modo anomalo

□ Operazioni I/O - Un programma in esecuzione può richiedere I/O, che può coinvolgere un file o un dispositivo I/O.
► Il SO deve nascondere la complessità del dispositivo offrendo agli utenti un interfaccimento semplice ed uniforme

---

## Pagina 99

Servizi degli SO

Un insieme di servizi del sistema operativo:

□ Gestione File-system - I programmi devono leggere e scrivere file e directory, crearli ed eliminarli, ricercarli, elencare le informazioni sui file, gestire i permessi. Accesso frequenti richiede gestione oculata.

□ Comunicazione – I processi possono scambiare informazioni, sullo stesso computer o tra computer in una rete

□ Rilevamento di Errori – Il sistema operativo deve essere costantemente consapevole di possibili errori

► Può verificarsi nella CPU e nell'hardware di memoria, nei dispositivi I/O, nel programma utente
► Per ogni tipo di errore, il sistema operativo dovrebbe intraprendere l'azione appropriata per garantire un'elaborazione corretta e coerente
► Le funzionalità di debug possono migliorare notevolmente le capacità dell'utente e del programmatore di utilizzare in modo efficiente il sistema

---

## Pagina 100

Servizi degli SO

Insieme di funzioni del sistema operativo per garantire il funzionamento efficiente del sistema stesso tramite la condivisione delle risorse

- Allocazione delle risorse - quando più utenti o più lavori vengono eseguiti contemporaneamente, le risorse devono essere allocate a ciascuno di essi
  - Molti tipi di risorse - cicli CPU, memoria principale, file, dispositivi I/O.

- Contabilità - tenere traccia di quali utenti utilizzano quanto e quali tipi di risorse del computer

- Protezione e sicurezza - I proprietari delle informazioni archiviate in un sistema informatico multiutente o in rete devono poter controllare l'uso di tali informazioni, processi simultanei non devono interferire tra loro
  - La protezione deve garantire che l'accesso da parte di processi ed utenti (interni) alle risorse di sistema sia controllato
  - La sicurezza rispetto ad accessi esterni richiede l'autenticazione dell'utente e prevede la difesa dei dispositivi I/O esterni da accessi non consentiti

---

## Pagina 101

Panoramica dei Servizi di un SO

I processi utente accedono ai servizi del Sistema Operativo mediante chiamate di sistema:

- Istruzioni che invocano servizi gestiti dal Kernel

user and other system programs
GUI
batch
command line
user interfaces

system calls
program execution
I/O operations
file systems
communication
resource allocation
accounting
error detection
services
protection and security

operating system
hardware

---

## Pagina 102

Interfaccia Utente - CLI

L'interprete dei comandi consente l'immissione diretta dei comandi

- A volte implementato nel kernel, a volte dal programma di sistema
- A volte più interfacce – shells
- Principalmente recupera un comando dall'utente e lo esegue

---

## Pagina 103

Interfaccia Utente - GUI

Interfaccia grafica (Graphic User Interface)
- Interfaccia che usa la metafora del desktop
- Mouse, tastiera, schermo
- Le icone rappresentano file, programmi, azioni, ecc
- Inventata a Xerox PARC

---

## Pagina 104

Altre Interfacce Utente

- Interfacce touch-screen
  - Senza mouse
  - Gesti per attivare azioni
- Comandi vocali
- Etc.

---

## Pagina 105

Panoramica dei Servizi di un SO

I processi utente accedono ai servizi del Sistema Operativo mediante chiamate di sistema:
- Istruzioni che invocano servizi gestiti dal Kernel
- ABI (Application Binary Interface) tra
- Chiamate mediante API che le incapsulano

user and other system programs
GUI batch command line
user interfaces

system calls
program execution
I/O operations
file systems
communication
resource allocation
accounting
error detection
services
protection and security

operating system
hardware

---

## Pagina 106

Chiamate di Sistema

□ Le **chiamate di sistema** (*system call*) costituiscono un’interfaccia per i servizi resi disponibili dal sistema operativo

□ Chiamate dai programmi mediante **Application Programming Interface** (API)

□ Tra le API più comuni citiamo:
  □ **Win API**: API C per Windows (kernal32.dll, User32.dll, etc.)
  □ **POSIX API**: API C per POSIX-based systems (incluse tutte le versioni UNIX, Linux e MacOS) - **Portable Operating System Interface**
  □ **Java API**: API per la Java virtual machine (JVM)

---

## Pagina 107

Esempio di Chiamata di Sistema

- Chiamata di sistema per copiare il contenuto di un file in un altro file

cp in.txt out.txt

Esempio di sequenza di chiamate di sistema
Acquisisce il nome del file in ingresso
Scrive messaggio di richiesta sullo schermo
Accetta i dati in ingresso
Acquisisce il nome del file in uscita
Scrive messaggio di richiesta sullo schermo
Accetta i dati in ingresso
Apre il file in ingresso
Se il file non esiste, termina con errore
Crea il file in uscita
Se il file esiste, termina con errore
Ripete
Legge dal file in ingresso
Scrive sul file in uscita
Finché c’è ancora da leggere
Chiude il file in uscita
Scrive messaggio sullo schermo per informare del completamento
Termina senza errori

programma (cp)
API POSIX / libc
system call
kernel

Figura 2.5 Esempio d’uso delle chiamate di sistema.

---

## Pagina 108

Esempio di API standard

API: Specifica un insieme di funzioni a disposizione del programmatore e dettaglia i parametri necessari per l’invocazione di queste funzioni insieme ai valori restituiti

Come esempio di API standard consideriamo la funzione `read()` disponibile in Unix e Linux. L’API per questa funzione si può ottenere digitando

```c
man read
da riga di comando. Una descrizione di questa API è la seguente:

#include <unistd.h>

ssize_t read(int fd, void *buf, size_t count)
{
valore nome parametri
restituito della funzione
```

Un programma che utilizza la `read()` deve includere il file `unistd.h` che, tra le altre cose, definisce i tipi di dato `ssize_t` e `size_t`. Il parametri passati alla `read()` sono i seguenti:

• `int fd` — il descrittore del file da leggere
• `void *buf` — un buffer nel quale vengono messi i dati letti
• `size_t count` — il massimo numero di byte da leggere e inserire nel buffer

Quando una `read()` è completata con successo viene restituito il numero di byte letti. La `read()` restituisce 0 in caso di fine del file e –1 quando si è verificato un errore.

---

## Pagina 109

Relazione tra API e Chiamata

- Tipicamente un numero è associato per ogni chiamata (la system-call interface mantiene una tabella indicizzata)
- L’interfaccia invoca la chiamata nel kernel e restituisce lo status e valore di ritorno (dettagli nascosti gestiti da librerie di supporto)

Figura 2.6 Gestione della chiamata di sistema open() invocata da un’applicazione utente.

---

## Pagina 110

Passaggio dei parametri

- Tre metodi generali utilizzati per passare i parametri al sistema operativo
  - Passa direttamente i parametri nei registri (a volte troppi parametri)
  - Parametri in un blocco, o tabella, in memoria e indirizzo del blocco passato come parametro in un registro (Linux e Solaris)
  - Parametri inseriti nello stack dal programma e estratti dallo stack dal SO

---

## Pagina 111

Passaggio dei parametri

□ Tre metodi generali utilizzati per passare i parametri al sistema operativo

□ Passa direttamente i parametri nei registri (a volte troppi parametri)

► In GNU/Linux, una chiamata di sistema accetta al più sei parametri

► Es. nell'architettura Intel il registro eax (32 bit) o rax (64 bit) contiene sempre un identificatore numerico univoco della chiamata di sistema

► Altri registri (x64)

  * rax system call number/val ritorno
  * rdi arg0
  * rsi arg1
  • rdx arg2
  • r10 arg3
  • r8 arg4
  • r9 arg5

Es. write(fd, msg, 12)

mov rax, 1 ; numero syscall write
mov rdi, 1 ; fd (stdout)
mov rsi, msg ; buffer
mov rdx, 12 ; lunghezza
syscall

---

## Pagina 112

Passaggio dei parametri

- Tre metodi generali utilizzati per passare i parametri al sistema operativo
  - Passa direttamente i parametri nei registri (a volte troppi parametri)
  - Parametri in un blocco, o tabella, in memoria e indirizzo del blocco passato come parametro in un registro (Linux e Solaris)
    - es. con rdi = x si può puntare al blocco

Figura 2.7 Passaggio di parametri in forma di tabella.

---

## Pagina 113

Chiamata di Sistema

- Parametri inseriti nello stack dal programma e estratti dallo stack dal SO
- Programma in C invoca una chiamata di sistema:
  - Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`
  - Restituisce numero byte o -1 nel var globale errno

Il programma chiamante predispone la chiamata mettendo prima i parametri in uno stack (passi 1–3) – il buffer passato per riferimento

La procedura chiama il read (passo 4) mettendo il codice della chiamata a sistema di read in un registro atteso dal Kernel

Quindi manda una istruzione *Trap* al kernel e passa il controllo al kernel in kernel mode (passi 5-6)

Il kernel trova il codice della chiamata e mediante una tabella trova l’handler della call (passi 7 e 8) finita l’esecuzione passa il risultato al chiamante (passo 9)

Il chiamante riprende il controllo in user mode (passo 10) e pulisce lo stack (passo 11) incrementando lo Stack Pointer (SP)

---

## Pagina 114

Chiamata di Sistema

- Parametri inseriti nello stack dal programma e estratti dallo stack dal SO
- Programma in C invoca una chiamata di sistema:
  - Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`
  - Restituisce numero byte o -1 nel var globale errno

Nei sistemi Linux moderni (x86-64) i parametri delle system call sono passati **nei registri**, non nello stack.

Lo stack è usato solo per la chiamata alla funzione della libreria (read, write, ecc.). La sequenza è quindi

```text
programma C
call read() ← stack
libc wrapper (sposta i parametri nei registri)
registri syscall
syscall
kernel
```

---

## Pagina 115

Chiamata di Sistema

- Parametri inseriti nello stack dal programma e estratti dallo stack dal SO
- Programma in C invoca una chiamata di sistema:
  - Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`
  - Restituisce numero byte o -1 nel var globale errno (registo rax)

Le procedure POSIX non si mappano sempre uno a uno con le system call offerte dal SO

Nella maggior parte dei casi chiamano effettivamente le sys call. Alcune eseguono operazioni senza fare il TRAP del kernel

---

## Pagina 116

Tipi di Chiamate di Sistema

- Controllo di processi
  - Creare e terminare processi
  - Caricare, eseguire processi
  - Ottenere e settare attributi di processo
  - Attese di tempo
  - Attese di eventi/segnali
  - Allocare memoria
  - Debugger per determinare bug
  - Meccanismi di regolazione per gestire l’accesso a dati condivisi

---

## Pagina 117

Funzioni per System Call

- Controllo di processi
  - Funzioni di libreria C per l’invocazione di syscall
  - Interfaccia POSIX delle system call

```c
#include <sys/types.h>
# include <unistd.h>

pid_t getpid(void);  identificativo del processo
pid_t getppid(void);  identificativo del genitore

pid_t fork(void);        pid_t wait(int *status);
pid_t vfork(void);

pid_t pid;

if ( (pid=fork()) < 0 )
    perror("fork"), exit(1);
else if (pid != 0) {
    // codice del padre
} else {
    // codice del figlio
}
```

---

## Pagina 118

Tipi di Chiamate di Sistema

- Gestione di File
  - create file, delete file
  - open, close file
  - read, write, reposition
  - get and set file attributes

- Gestione di dispositivi
  - request device, release device
  - read, write
  - get device attributes, set device attributes
  - logically attach or detach devices

---

## Pagina 119

Tipi di Chiamate di Sistema

Gestione informazione
- get time or date, set time or date
- get system data, set system data
- get and set process, file, or device attributes

Comunicazione
- create, delete communication connection
- send, receive messages if message passing model to host name or process name
  - da client a server
- Shared-memory creazione ed accesso a regioni di memoria condivisa
- trasferire informazione di stato
- Installare/disinstallare dispositivo remoti

---

## Pagina 120

Tipi di Chiamate di Sistema

Protezione
- Controllo accesso a risorse
- Gestione dei permessi
- Gestione accesso utenti

---

## Pagina 121

Tipi di Chiamate di Sistema

• Controllo dei processi
  • creazione e arresto di un processo
  • caricamento, esecuzione
  • terminazione normale e anormale
  • esame e impostazione degli attributi di un processo
  • attesa per il tempo indicato
  • attesa e segnalazione di un evento
  • assegnazione e rilascio di memoria

• Gestione dei file
  • creazione e cancellazione di file
  • apertura, chiusura
  • lettura, scrittura, posizionamento
  • esame e impostazione degli attributi di un file

• Gestione dei dispositivi
  • richiesta e rilascio di un dispositivo
  • lettura, scrittura, posizionamento
  • esame e impostazione degli attributi di un dispositivo
  • inserimento logico ed esclusione logica di un dispositivo

• Gestione delle informazioni
  • esame e impostazione dell’ora e della data
  • esame e impostazione dei dati del sistema
  • esame e impostazione degli attributi dei processi, file e dispositivi

• Comunicazione
  • creazione e chiusura di una connessione
  • invio e ricezione di messaggi
  • informazioni sullo stato di un trasferimento
  • inserimento ed esclusione di dispositivi remoti

• Protezione
  • visualizzazione dei permessi di un file
  • impostazione dei permessi di un file

Figura 2.8 Tipi di chiamate di sistema.

---

## Pagina 122

Esempi chiamate di sistema in Windows e Unix

| Windows | UNIX |
| :--- | :--- |
| Controllo dei processi | fork() |
| CreateProcess() | exit() |
| ExitProcess() | wait() |
| WaitForSingleObject() | wait() |
| Gestione dei file | open() |
| CreateFile() | read() |
| ReadFile() | write() |
| WriteFile() | close() |
| CloseHandle() | close() |
| Gestione dei dispositivi | ioctl() |
| SetConsoleMode() | read() |
| ReadConsole() | write() |
| WriteConsole() | write() |
| Gestione delle informazioni | getpid() |
| GetCurrentProcessID() | alarm() |
| SetTimer() | sleep() |
| Sleep() | sleep() |
| Comunicazione | pipe() |
| CreatePipe() | shm_open() |
| CreateFileMapping() | mmap() |
| MapViewOfFile() | mmap() |
| Protezione | chmod() |
| SetFileSecurity() | umask() |
| InitializeSecurityDescriptor() | chown() |
| SetSecurityDescriptorGroup() | chown() |

---

## Pagina 123

Standard C Library

Programma in C invoca una chiamata di libreria standard printf() che chiama la chiamata di sistema write()

```c
#include <stdio.h>
int main ()
{
    printf ("Greetings");
    return 0;
}
```

user mode
kernel mode
standard C library
write ()
write ()
system call

---

## Pagina 124

Programmi di Sistema

I programmi di sistema forniscono un ambiente conveniente per lo sviluppo e l'esecuzione del programma

Programmi applicativi
Sistema base
Kernel

Driver dei dispositivi
Gestore I/O
Gestore dei Processi
Gestore del file system
Gestore della memoria
IPC

Kernel

Librerie di sistema
Caricatore dinamico
Sistema di init
Comandi di sistema
Shell
Terminale

2.30

---

## Pagina 125

Programmi di Sistema

- I programmi di sistema forniscono un ambiente conveniente per lo sviluppo e l'esecuzione di programmi

- Possono essere suddivisi in:
  - Manipolazione di file
  - Informazioni sullo stato
  - Supporto del linguaggio di programmazione
  - Caricamento ed esecuzione del programma
  - Comunicazioni
  - Servizi in background
  - Programmi applicativi

- La maggior parte degli utenti di un SO usa soprattutto i programmi di sistema, meno le effettive chiamate di sistema

---

## Pagina 126

Programmi di Sistema

□ Forniscono un ambiente conveniente per lo sviluppo e l'esecuzione di programmi
  □ Alcuni di essi sono semplicemente interface utente per le chiamate di sistema; altri sono notevolmente più complessi

□ Gestione dei file: crea, elimina, copia, rinomina, stampa, scarica, elenca e generalmente manipola file e directory

□ Informazioni sullo stato
  □ Informazioni al sistema: data, ora, quantità di memoria disponibile, spazio su disco, numero di utenti
  □ Informazioni dettagliate su prestazioni, registrazione e debug
  □ In genere, questi programmi formattano e stampano l'output sul terminale o su altri dispositivi di output

---

## Pagina 127

Programmi di Sistema

□ Modifica file
  □ Editor di testo per creare e modificare file
  □ Comandi speciali per cercare contenuti di file o eseguire trasformazioni del testo

□ Supporto del linguaggio di programmazione - compilatori, assemblatori, debugger ed interpreti

□ Caricamento ed esecuzione del programma - una volta assemblato o compilato un programma, deve essere caricato in memoria per essere eseguito. Il sistema fornisce strumenti come dynamic loader, linker, sistemi di debug, etc.

□ Comunicazioni - meccanismi per creare connessioni virtuali tra processi, utenti e sistemi informatici

---

## Pagina 128

Programmi di Sistema

Servizi di Background

- Lanciati a tempo di boot
  - Alcuni per lo startup, poi terminate
  - Altri continuano a girare

- I programmi di sistema in constante esecuzioni si dicono servizi, sottosistemi, demoni

- Esempi sono monitoraggio di errori, servizi di stampa, etc.

- Eseguiti in contesto user, non kernel

---

## Pagina 129

Progettazione ed Implementazione di un SO

- La struttura di un SO può variare molto da sistema a sistema
- La progettazione parte da obiettivi e specifiche
- Dipende da hardware e tipo di sistema
- Distinguiamo obiettivi utente e obiettivi di sistema
  - Utente
    - comodo da usare, facile da imparare, affidabile, sicuro e veloce
  - Sistema
    - facile da progettare, implementare e mantenere, nonché flessibile, affidabile, privo di errori ed efficiente

Es. Windows Server vs VxWorks

---

## Pagina 130

Progettazione ed Implementazione di un SO

Distinguere:
- Politica: cosa fare?
- Meccanismo: come fare?
- Es., il timer serve per la protezione della CPU, il timer è un meccanismo, ma la lunghezza del timer è una politica

La separazione della politica dal meccanismo consente flessibilità se le decisioni politiche devono essere modificate in un secondo momento
- Il meccanismo deve supportare più politiche
- La politica si può definire settando parametri dei meccanismi
- Es., approcci a microkernel favoriscono la separazione

Specificare e progettare un sistema operativo è un compito altamente creativo per l’ingegneria del software

---

## Pagina 131

Implementazione

□ Diverse modalità
  □ Primi SO in assembly
  □ Poi linguaggi di programmazione di sistema come Algol, PL/1
  □ Ora linguaggi come C, C++

□ Di solito un mix di languaggi
  □ Parti più basse in assembly
  □ Corpo principale in C
  □ Programmi di sistema in C, C++, linguaggi di scripting come PERL, Python, shell scripts

□ Più è alto il livello del linguaggio più facile è il **porting** su altro hardware, ma meno performante

□ L’**emulazione** permette ad un OS di girare su hardware non-native

□ La **virtualizzazione** permette l’esecuzione di più sistemi operativi contemporaneamente

---

## Pagina 132

Emulazione vs Virtualizzazione

Emulazione

• Riproduco un’architettura hardware diversa da quella reale.
  Così posso eseguire programmi compilati per un’altra CPU.
  → Lenta perché il codice viene interpretato/convertito.
  Esempio: QEMU (Quick EMUulator) che emula ARM su x86
• grande flessibilità, bassa efficienza.

Virtualizzazione

• Faccio girare più sistemi operativi della stessa architettura sull’hardware reale.
  Non simula la CPU → i guest girano nativamente.
  → Molto più veloce dell’emulazione.

---

## Pagina 133

Virtualizzazione

Virtualizzazione completa (full)
• Il guest non sa di essere virtualizzato.
  Pensa di parlare con hardware reale → massima compatibilità.
  → Overhead maggiore a causa della gestione trasparente dell’hardware.
• Esempio: VMware

Paravirtualizzazione
• Il guest sa di essere virtualizzato e collabora con l’VMM tramite API speciali. Meno overhead, ma richiede OS modificati.
  Esempio storico: Xen paravirtualizzato.
• Oggi la parav viene usata come ottimizzazione (es. virtio), non come modello puro.

Virtualizzazione assistita da hardware
• Le CPU (Intel VT-x, AMD-V, ARM Virt. Ext.) forniscono istruzioni speciali che rendono la virtualizzazione più efficiente.
• → È la base della virtualizzazione moderna.
  → Riduce costi di gestione del guest.
• Oggi **quasi tutte** le VM usano questo modello.

---

## Pagina 134

Virtualizzazione

- Permette di eseguire più sistemi operativi sulla stessa macchina fisica. Ogni SO esegue le proprie applicazioni come se avesse hardware dedicato.

- Virtualizzazione – sistema operativo compilato in modo nativo per la CPU, che esegue anche sistemi operativi guest compilati in modo nativo
  - VMM (Virtual Machine Manager/Monitor) fornisce servizi di virtualizzazione
  - Tipo 1:
    - VMM come Sistema operative host, comunica direttamente con hardware (es. VMware ESXi, Xen, Hyper-V, KVM)
  - Tipo 2:
    - VMM installato sopra un SO host (es. VMWare, Oracle VirtualBox)

- In Tipo 1 support hardware, accesso privilegiato dedicato:
  - Ring -1 Hyp
  - Ring 0-2 Kernel (si usa solo 0)
  - Ring 3 User

---

## Pagina 135

Virtualizzazione

Virtualizzazione – VMM/Hypervisor fornisce servizi di virtualizzazione per eseguire guest compilati nativamente.

VMM (Virtual Machine Manager/Monitor) fornisce servizi di virtualizzazione

Tipo 1:
► VMM come Sistema operative host, comunica direttamente con hardware (es. VMware ESXi, Xen, Hyper-V, KVM)

Tipo 2:
► VMM installato sopra un SO host (es. VMWare, Oracle VirtualBox)

Figura 1.16 Un computer che ha in esecuzione (a) un singolo sistema operativo e (b) tre macchine virtuali.

---

## Pagina 136

Virtualizzazione

• Caso Linux
  • Hypervisor: KVM (Kernel-based Virtual Machine)
  • È integrato direttamente nel kernel Linux (hyp tipo 1)
  • Si attiva solo quando una VM lo usa
  • Le VM sono processi user-space che accedono a KVM

• Caso Windows 11
  • Hyper-V è un hypervisor di tipo 1
  • Windows è una VM privilegiata chiamata root partition, le altre VM (es. WSL2) sono guest partitions:

Attivazione:
In windows PowShell:
  wsl --install
Per verificare WSL:
  wsl --status

Hardware
Hyper-V Hypervisor (TYPE 1)
Windows (Root VM / Parent Partition)
Linux WSL2 VM (Guest)

---

## Pagina 137

Virtualizzazione

- Caso macOS (Apple Silicon)
  - Non ha un hypervisor nel kernel
  - Le VM sono gestite da applicazioni user-space che usano Hypervisor.framework, API user-space

---

## Pagina 138

Strutture di un Sistema Operativo

- Un Sistema Operativo è un software molto complesso

- Vari modi di strutturarlo
  - Sistemi monolitici
    - Struttura semplice -- MS-DOS
    - Più complessa -- UNIX
  - Sistemi Stratificati
  - Sistemi a micro-kernel
  - Sistemi ibridi

---

## Pagina 139

Sistemi Monolitici

- Sistema Operativo è costituito da una collezione di procedure ognuna delle quali può chiamare qualsiasi altra
- Un sistema monolitico viene anche chiamato sistema strettamente accoppiato (tightly coupled)
  - Collezione di procedure linkate in un unico eseguibile
  - Ogni procedura può chiamare l’altra (efficace ed efficente)
  - Poca modularità (difficili da sviluppare ed estendere)
  - Struttura basata su chiamate di sistema

Tanenbaum & Bo, Modern Operating Systems:4th ed., (c) 2013 Prentice-Hall, Inc. All rights reserved.

---

## Pagina 140

Struttura Semplice - MS-DOS

MS-DOS – funzionalità nel minimo spazio

- Monoutente e monotask (Windows 3.1 multitask cooperativo)
- Non suddiviso in moduli
- Sebbene MS-DOS abbia una struttura, interfacce e livelli di funzionalità non sono ben separati
- Programmi utente accedono a tutti i livelli (controllo completo della macchina)

BIOS (Basic Input Output System)
avvio, interfaccia HW, interrupt

---

## Pagina 141

Struttura non Semplice - UNIX

- UNIX: limitato dalla funzionalità hardware, il sistema operativo UNIX originale aveva una strutturazione limitata
- Il sistema operativo UNIX è costituito da due parti separabili
  - Programmi di sistema
  - Kernel
    - Tutto ciò che si trova al di sotto dell'interfaccia di chiamata di sistema e al di sopra dell'hardware fisico
    - Fornisce il file system, schedulazione della CPU, gestione della memoria e altre funzioni del sistema operativo (alto numero di funzioni in un livello)
    - Interfaccia standard per chiamate di sistema (POSIX)

---

## Pagina 142

Struttura di un Sistema UNIX

Non semplice

Kernel

(the users)

shells and commands
compilers and interpreters
system libraries

system-call interface to the kernel

signals terminal handling
character I/O system terminal drivers

file system swapping block I/O system disk and tape drivers

CPU scheduling page replacement demand paging virtual memory

kernel interface to the hardware

terminal controllers terminals

device controllers disks and tapes

memory controllers physical memory

---

## Pagina 143

Struttura di un Sistema Linux

Non semplice

GNU C Library: core lib del GNU system per interagire con il kernel linux

Figure 2.13 Linux system structure.

---

## Pagina 144

Approccio Stratificato

- Il sistema operativo è suddiviso in un numero di livelli (levels), ciascuno costruito sopra i livelli inferiori (THE, MULTICS).
- Lo strato inferiore (layer 0), è l'hardware; il più alto (layer N) è l'interfaccia utente.
- Con la modularità ciascuno layer utilizza funzioni (operazioni) e servizi dei layer inferiori

| Layer | Function |
| :--- | :--- |
| 5 | The operator |
| 4 | User programs |
| 3 | Input/output management |
| 2 | Operator-process communication |
| 1 | Memory and drum management |
| 0 | Processor allocation and multiprogramming |

THE realizzato alla Technische Hogelschool Eindhoven in Olanda da Dijkstra nel 1968 per il computer Electrologica X8

---

## Pagina 145

Struttura a Microkernel

□ Verso metà anni ’80 realizzato Mach con kernel strutturato in moduli secondo il cosiddetto orientamento a microkernel
□ macOS kernel (Darwin) parzialmente basato su Mach
□ Spostare più possible servizi dal kernel allo spazio utente
□ Funzioni di comunicazione tra i programmi client e i vari servizi in esecuzione nello spazio utente – comunicazione message-passer tramite kernel

2.51

---

## Pagina 146

Struttura a Microkernel

□ Verso metà anni ’80 realizzato Mach con kernel strutturato in moduli secondo il cosiddetto orientamento a microkernel
□ macOS kernel (Darwin) parzialmente basato su Mach

□ Spostare più possible dal kernel allo spazio utente
□ Funzioni di comunicazione tra i programmi client e i vari servizi in esecuzione nello spazio utente
□ Kernel minimale:
  ► meccanismo di comunicazione tra processi (message-passer)
  ► gestione della memoria e dei processi
  ► gestione dell’hardware di basso livello
  ► tutto il resto gestito da processi in spazio utente (e.g., politiche di gestione file system, scheduling, memoria sono implementate da processi utente) che comunicano passando per il kernel

---

## Pagina 147

Struttura a Microkernel

□ Verso metà anni ’80 realizzato Mach con kernel strutturato in moduli secondo il cosiddetto orientamento a microkernel
□ macOS kernel parzialmente basato su Mach (e su BSD)

□ Spostrare più possibile dal kernel allo spazio utente
□ Funzioni di comunicazione tra i programmi client e i vari servizi in esecuzione nello spazio utente
□ Kernel minimale:

Monolithic Kernel based Operating System

Microkernel based Operating System

Application
System Call
VFS
IPC, File System
Scheduler, Virtual Memory
Device Drivers, Dispatcher, ...
Hardware

user mode
kernel mode

Application IPC
UNIX Server
Device Driver
File Server

Basic IPC, Virtual Memory, Scheduling

Hardware

---

## Pagina 148

Struttura a Microkernel

- Spostrare più possibile dal kernel allo spazio utente
- Comunicazione tra moduli utente mediante message passing
- Vantaggi:
  - Facilità di estensione microkernel
  - Facilità di trasferimento dell’SO su nuove architetture
  - Meno codice eseguito in modalità kernel
  - Sicuro
- Svantaggi:
  - Sovraccarico delle prestazioni della comunicazione tra lo spazio utente e lo spazio del kernel (context switch)

---

## Pagina 149

Struttura a Microkernel

Caso di Windows NT
- Prima release a microkernel
- Prestazioni povere rispetto a Windows 95
- Si passa a Windows NT 4.0 muovendo servizi da utente a kernel
- Windows XP torna più monolitico che microkernel

---

## Pagina 150

Moduli

- Molti sistemi operativi moderni implementano moduli del kernel caricabili
  - **Loadable kernel modules (LKMs)** - Linux, Solaris, macOS, Win, etc
  - Ogni componente principale è separato
  - Servizi linkati dinamicamente mentre il kernel è in esecuzione o caricamento
  - Ciascuno parla con gli altri tramite interfacce conosciute,
  - Ciascuno è caricabile secondo necessità all'interno del kernel

- Simile al sistema a livelli (core ha interfacce con altri moduli) ma con più flessibilità
- Simile a microkernel, ma meno message passing

---

## Pagina 151

Sistemi Ibridi

La maggior parte dei sistemi operativi moderni non sono in realtà un modello puro

- Il sistema ibrido combina più approcci per soddisfare le esigenze di prestazioni, sicurezza e usabilità
- Kernel Linux e Solaris in un singolo spazio di indirizzi, quindi monolitico, ma modulari per il caricamento dinamico di funzionalità
- Windows per lo più monolitico, microkernel per diverse parti del sottosistema
- Apple macOS ibrido (microkernel, monolitico)

---

## Pagina 152

Struttura a lbrida

Il sistema operativo macOS di Apple si basa su Kernel XNU

XNU kernel
- Mach
  - scheduling
  - IPC
  - virtual memory

- BSD
  - POSIX layer
  - networking
  - file systems
  - process model

- IOKit
  - alcuni driver

User space
- applicazioni
- framework di sistema
- Driver Kit dirvers
- servizi di sistema

Kernel XNU (X is Not Unix)

Combina Mach e BSD (microkernel e monolitico)

- memoria, IPC, I/O (variante march)
- protezioni, virtual file system, rete, POSIX (BSD)

---

## Pagina 153

Android

- SO basato su Linux kernel (modificato) quindi monolitico
- Sopra il kernel (user space) è presente un ambiente software composto:
  - framework Android e runtime ART per eseguire le applicazioni
  - strato HAL (hardware abstraction layer) astrae l’hardware dei diversi dispositivi.

Applicazioni
↓
Application Framework
↓
Android Runtime (ART) + Native Libraries
↓
HAL (hardware abstraction layer)
↓
Linux Kernel
↓
Hardware

---

## Pagina 154

Lezione 5: Processi

---

## Pagina 155

Obiettivi

- Nozione di processo
- Caratteristiche dei processi (schedulazione, creazione, terminazione, comunicazione, etc.)
- Comunicazione interprocesso
- Comunicazione nei sistemi client-server

---

## Pagina 156

Definizione di Processo

Un SO esegue programmi di varia natura:
- Sistemi batch – job
- Sistemi time-shared – programmi utente o task
- Job è più astratto: lavoro computazionale (che può generare processi)
- I libri di testo usano job e processo in modo quasi intercambiabile

Processo – è un programma in esecuzione
- Un programma è un’entità passiva archiviata su disco (file eseguibile), un processo è attivo (in esecuzione)
- Unità di attività computazionale coerente di un moderno SO
- Esecuzione sequenziale
- Un processo richiede risorse (CPU, memoria, file, dispositivi I/O) per l’esecuzione di un compito (task)
- Un programma può chiamare molti processi
- I sistemi sono il risultato dell’esecuzione di più processi concorreti
  - processi di sistema e processi utente

---

## Pagina 157

Definizione di Processo

□ **Processo** – è un programma in esecuzione:
  □ Stato corrente **program counter** e **registri del processore**
  □ Layout di memoria

□ Layout di memoria:
  □ Il codice del programma, chiamata **sezione testo**
  □ **Sezione Dati** contenente le variabili globali
  □ **Stack** contenente i dati temporanei
    ► Parameteri di funzione, indirizzi di ritorno, variabili locali
  □ **Heap** contenente memoria dinamicamente allocata a run time durante l’esecuzione di un task

---

## Pagina 158

Processo Allocato in Memoria

□ Processo – è un programma in esecuzione:

□ Layout di memoria:
  □ Text e Data dimensione fissata
  □ Stack e Heap variabili a run time

Non initialized data anche indicate come block started by symbol (bss)

---

## Pagina 159

Stato di un Processo

Durante l’esecuzione un processo può cambiare il suo stato

- **new**: il processo è stato creato
- **running**: esecuzione delle istruzioni del processo
- **waiting**: il processo è in attesa di un evento per proseguire (es. I/O)
- **ready**: il processo è in attesa di essere assegnato a processore
- **terminated**: il processo ha finite l’esecuzione

---

## Pagina 160

Descrittore di Processo

- Il Sistema Operativo mantiene una tabella dei processi

- Per ogni processo una entry (Task Control Block)
  - Stato del processo - running, waiting, etc
  - IDs del processo - identificativi di processo
  - Program counter - locazione prossima istruzione
  - Registri CPU - contenuto registri CPU
  - Scheduling di CPU - priorità, parametri di scheduling
  - Memoria - memoria allocata per il processo (es. base and limit registers, tabella delle pagine, etc.)
  - Contabilità - CPU usata, tempo clock dallo start, numero di processo, etc.
  - Stato I/O - dispositivi I/O allocati, lista di file aperti, etc.

---

## Pagina 161

Tabella Processi in Linux

In Linux la PCB è rappresentata in C da una task_struct specificata nel codice sorgente del kernel (in /linux/sched.h)

Alcuni campi seguono:

```c
pid t_pid; /* process identifier */
long state; /* state of the process */
unsigned int time_slice /* scheduling information */
struct task_struct *parent; /* this process’s parent */
struct list_head children; /* this process’s children */
struct files_struct *files; /* list of open files */
struct mm_struct *mm; /* address space of this process */
```

Nel kernel Linux i processi attivi sono representati da una lista doppiamente linkata

current (currently executing process)

---

## Pagina 162

Commutazione tra Processi

- La tabella dei processi supporta la commutazione tra processi
- Lo stato dei processi salvato e ripristinato durante gli switch

Diagram showing the process flow with interrupt or system call branches. Process $P_0$, operating system, and process $P_1$ are represented. Executing processes save state into PCB$_0$, reload state from PCB$_1$, and execute processes save state into PCB$_1$, reload state from PCB$_0$.

---

## Pagina 163

Processi e Thread

- I moderni Sistemi Operativi consentono ai processi di gestire l’esecuzione di più flussi di controllo (thread)

- I processi possono diramarsi in più sottounità di esecuzione
  - Più program counter per un processo
  - Multipli flussi di controllo -> threads
    - Condividono identità e risorse di processo ma hanno diverso stato esecutivo
  - Archiviazioni di ulteriori informazione per thread in PCB

---

## Pagina 164

Schedulazione di Processi

- Massimizza l’uso della CPU, fa velocemente lo switch di processi nella CPU per il time sharing
- Schedulatore dei processi seleziona tra processi disponibili per la prossima esecuzione su CPU
- Mantiene la coda di scheduling dei processi
  - Job queue – insieme di tutti i processi nel sistema
  - Ready queue – insieme di tutti i processi in memoria principale, pronti (ready)
  - Wait queue – insieme dei processi in attesa (waiting)
  - Device queues – insieme di processi in attesa (waiting) di un dispositivo di I/O
  - I processi migrano tra le diverse code

---

## Pagina 165

Code Processi Ready e Waiting

Mantiene la coda di scheduling dei processi

- **Job queue** – insieme di tutti i processi nel sistema
- **Ready queue** – insieme di tutti i processi in memoria principale, pronti (ready) per l’esecuzione
- **Wait queue** – insieme dei processi in attesa (waiting)
- **Device queues** – insieme di processi in attesa (waiting) di un dispositivo di I/O
- I processi migrano tra le diverse code

---

## Pagina 166

Rappresentazione Scheduling dei Processi

Diagramma di accodamento
- Un nuovo processo in coda ready attende la CPU
- Una volta allocata diversi eventi possono avvenire (I/O, fine tempo, fork, wait)

---

## Pagina 167

Scheduler

□ **Short-term scheduler** (o **CPU scheduler**) – seleziona quale processo deve essere eseguito dalla CPU
  □ A volte l’unico scheduler nel sistema
  □ Lo short-term scheduler è invocato frequentemente (millisecondi) ⇒ (deve essere veloce)

□ **Long-term scheduler** (o **job scheduler**) – seleziona quale processo deve essere portato nella coda ready
  □ Long-term scheduler non frequente (secondi, minuti) ⇒ (può essere lento)
  □ Il long-term scheduler controlla il **grado di multiprogrammazione**
  □ I processi possono essere descritti come:
    ► **I/O-bound process** – spende più tempo in operazioni I/O che in computazione, piccoli e brevi accessi in CPU
    ► **CPU-bound process** – spende più tempo in computazione; pochi e lunghi accessi in CPU
    ► Long-term scheduler cerca di trovare una buona combinazione di processi

---

## Pagina 168

Scheduling di Medio Termine

- Medium-term scheduler può essere aggiunto se il grado di multiprogrammazione deve decrescere (minor contesa per CPU)
- Toglie processi dalla memoria, archivia su disco, riporta in memoria da disco per continuare l’esecuzione: swapping

---

## Pagina 169

Context Switch

- Al passaggio della CPU ad un altro processo il sistema deve salvare lo stato del vecchio processo e caricare lo stato salvato del nuovo processo attraverso un context switch
- Context (contesto) di processo representato in PCB

- Il tempo di context-switch è un overhead
  - il sistema non fa lavoro “utile” durante lo switching
  - Più è complesso il sistema e la PCB più è lungo il context switch

- Il tempo depende dal supporto hardware
  - Alcuni hardware forniscono registri multipli per CPU consentendo caricamenti di più context in una volta

---

## Pagina 170

Operazioni su Processi

Il Sistema deve fornire meccanismi per:
- Creazione di processi,
- Terminazione di processi,
- Comunicazione tra processi
- Sincronizzazione tra processi
- Altri meccanismi di gestione di processi (dettagliato dopo)

---

## Pagina 171

Creazione di Processi

- Processo padre crea un processo figlio, che a sua volta crea crea altri processi formando un albero di processi
- Processi identificati e gestiti con identificatori di processo (pid)

- Condivisione di risorse (opzioni)
  - Padre e figlio condividono tutte le risorse
  - Figlio condivide un sottoinsieme delle risorse del padre
  - Padre e figlio non condividono alcuna risorsa

- Opzioni di esecuzione
  - Padre e figlio vengono eseguiti in concorrenza
  - Padre aspetta che il figlio finisca

---

## Pagina 172

Albero di Processi in Linux

System deamon fa l’init
Logind gestisce il log nel Sistema
L’utente lancia una shell bash, fa ps e vim

In UNIX il primo processo è init

Per vedere l’albero dei processi da bash: pstree

---

## Pagina 173

Creazione di Processi

Diverse gestioni
- Spazio memoria
  - Figlio duplica quello del padre
  - Figlio ha un programma caricato
- Esecuzione:
  - Padre e figlio concorrenti o padre attende figlio

Esempi UNIX
- fork() system call crea nuovo processo
- exec() system call usata dopo la fork() per sostituire lo spazio di memoria con un nuovo programma

---

## Pagina 174

Programma C con fork ed exec

```c
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
pid_t pid;

    /* fork a child process */
    pid = fork();

    if (pid < 0) { /* error occurred */
        fprintf(stderr, "Fork Failed");
        return 1;
    }
    else if (pid == 0) { /* child process */
        execlp("/bin/ls","ls",NULL);
    }
    else { /* parent process */
        /* parent will wait for the child to complete */
        wait(NULL);
        printf("Child Complete");
    }

    return 0;
}
```

---

## Pagina 175

Programma C con fork ed exec

**exec**

- **DATI**
- **CODICE**

**Programma**

- **Environment***
  - User stack & heap
  - bss
  - initialized data
  - User text
- **Process Control Block**
  - PCB*
  - kernel stack
  - kernel code (shared)
- **Layout processo**

- **Environment***
  - User stack & heap
  - bss
  - initialized data
  - User text
- **Process Control Block**
  - PCB*
  - kernel stack
  - kernel code (shared)
- **Layout processo**

---

## Pagina 176

Programma C con fork

```c
int main(void) {
    int i;

    for (i=0; i<2; i++)
        if (fork()>0) {
            printf("Padre! %d\n", i);
        } else {
            printf("Figlio! %d\n", i);
        }

    sleep(10);
    return 0;
}
```

• Qual è l'output di questo programma?
• Quanti processi vengono creati?
• Di chi è figlio ciascun processo creato?

---

## Pagina 177

Programma C con fork

$$\begin{array}{l}
\$ ./a.out
padre 0
padre 1
figlio! 0
padre 1
figlio! 1
figlio! 1
\end{array}$$

Proc principale

padre 0
figlio! 0

padre1  figlio! 1
padre1  figlio! 1

---

## Pagina 178

Terminazione Processo

- I processi eseguono le ultime istruzioni e poi chiedono all’SO di uscire con la call di sistema `exit()`
  - Ritorna i dati di status data dal figlio al padre (via `wait()`)
  - Le risorse sono deallocate dall’SO

- Padri possono terminare le esecuzioni dei processi figli con la call `abort()` ad esempio perché:
  - Il figlio ha allocato risorse in eccesso
  - Il task del figlio non è più richiesto
  - Il genitore esce e non consente a un figlio di continuare

---

## Pagina 179

Terminazione Processo

- Alcuni SO non permettono ai figli di esistere se i padri hanno terminato
  - Se un processo termina tutti i figli terminano
  - **cascading termination** (tutta la gerarchia di figli terminata)
  - la terminazione è gestita dal SO

- Il padre può aspettare la terminazione di un figlio con la call `wait()`
  - riceve informazioni di stato e il pid del processo terminato, es. Unix
    ```bash
    pid = wait(&status);
    ```

- In Unix/Linux se non c’è padre in waiting il figlio diventa **zombie**

- Se padre termina prima del figlio senza invocare `wait` il figlio è **orphan**
  - In Unix adottato da init che chiama continuamente wait per accogliere lo status (in linux init è oggi systemd – System Daemon)

---

## Pagina 180

Terminazione Processo

In UNIX/Linux

inesistente
fork()
runnable
scelto dallo scheduler
fermato dallo scheduler (preempted)
running
exit()
main: return
terminato (zombie)
evento o segnale
stopped
aspetta qualcosa (pause, read, sleep)

invia SIGCHLD al padre

---

## Pagina 181

Terminazione Processo

In UNIX/Linux

/* status.c: Fornisce un esempio dei diversi stati di uscita di un processo figlio */

```c
#include<sys/types.h> /* per il tipo pid_t */
#include <unistd.h> /* per la funzione fork */
#include<sys/wait.h> /* per la funzione waitpid */
#include <stdio.h> /* per le funz. printf, fgets e perror */
#include <stdlib.h> /* per la funzione exit */
#include <string.h> /* per la funzione strlen */
#include <errno.h> /* per la messaggistica di errore */

int main(void)
{
    pid_t pid;
    int status;

    if ( (pid = fork()) < 0)
        perror("fork"), exit(1);
    else if (pid == 0) /* primo figlio... */
        exit(7); /* che termina in modo normale */

    if (wait(&status) != pid) /* il genitore aspetta il figlio... */
        perror("wait"), exit(1);
    print_exit(status); /* e ne mostra lo stato di terminazione */

    if ( (pid = fork()) < 0)
        perror("fork"), exit(1);
    else if (pid == 0) /* secondo figlio... */
        abort(); /* che genera SIGABRT */

    if (wait(&status) != pid) /* il genitore aspetta il 2ndo figlio... */
        perror("fork"), exit(1);
    print_exit(status); /* e ne mostra lo stato di terminazione */

    if ( (pid = fork()) < 0)
        perror("fork"), exit(1);
    else if (pid == 0) /* terzo figlio... */
        status /= 0; /* che divide per 0 e genera SIGFPE */

    if (wait(&status) != pid) /* il genitore aspetta il terzo figlio... */
        perror("wait"), exit(1);
    print_exit(status); /* e ne mostra lo stato di terminazione */

    exit(0);
}
```

---

## Pagina 182

Terminazione Processo

In UNIX/Linux
- Stato di uscita
  15 8 7 0
  | exit code | signal |
  +----------------+----------------+
  int status;

  wait(&status);
  if ( WIFEXITED(status) )
    printf("valore di uscita: %d\n", WEXITSTATUS(status));
  else
    printf("terminazione anomala\n");

  #define WIFEXITED(status) (((status) & 0x7F) == 0) -> 7 bit meno significativi

  E.g., status = 10000000 with 0x7F = 01111111 (7 bit a 1)

---

## Pagina 183

Architetture Multiprocesso – Chrome Browser

- Molti web browser giravano come un singlo processo (alcuni ancora)
  - Se un website causa problemi il browser può crashare o stallare

- Google Chrome Browser è multiprocesso con differenti tipi di processo:
  - Browser che gestisce l’interfaccia utente, il disco e la rete
  - Renderer che rende graficamente le web pages, gestisce HTML, Javascript. Per ogni sito web aperto è lanciato un nuovo renderer
  - Plug-in per ogni tipo di plug-in

---

## Pagina 184

Communicazione Interprocesso

□ Processi possono essere *independenti o cooperati*
□ Processi cooperanti si influenzano scambiandosi dati
□ Diverse sono le ragioni per la cooperazione tra processi:
  ▶ Condivisione di dati (accesso a dati condivisi)
  ▶ Velocità computazionale (sottoprocessi lavorano in parallelo)
  ▶ Modularità (divisione funzionale dei compiti)

□ Processi cooperanti hanno bisogno di *interprocess communication (IPC)*
□ Due modelli principali di IPC
  ▶ Shared memory
  ▶ Message passing

---

## Pagina 185

Modelli di Communicazione

(a) Message passing. (b) shared memory.

Scambio di poca informazione, tutti gli scambi passano per il Kernel

Più veloce (kernel alloca la zona condivisa), più semplice accesso, problema coordinazione tra processi

---

## Pagina 186

Memoria Condivisa

□ Comunicazione su regione di shared memory

□ Tipicamente creata nello spazio di indirizzamento del processo che la crea (segmento di shared memory)

□ Gli altri processi devono accedere a questo spazio che generalmente è proibito (va rilassata la restrizione)

□ I processi leggono e scrivono su questo spazio che è gestito dai processi (modalità utente)

□ La coordinazione di lettura e scrittura è sotto la responsabilità dei processi coinvolti, il SO lascia fare

---

## Pagina 187

Interprocess Communication – Shared Memory

Area di memoria condivisa tra i processi che desiderano comunicare

- Comunicazione è sotto il controllo dei processi degli utenti non del SO
- Occcorrono meccanismi che consentano ai processi utente di sincronizzarsi quando accedono alla memoria condivisa
- La sincronizzazione è discussa in dettaglio in seguito

---

## Pagina 188

Problema Produttore-Consumatore

□ Si introduce il problema del Produttore-Consumatore
□ Paradigma tipico per processi cooperanti
  □ processo producer produce informazione che è consumata dal processo consumer (es., web server produce html, web browser consuma)

□ Uso di buffer per produrre e consumare
  ▶ Buffer in shared memory
  ▶ Il produttore riempie il buffer
  ▶ Il consumatore svuota il buffer
  ▶ Produttore e consumatore devono sincronizzare le operazioni (mentre il produttore riempie il buffer, il consumatore lo svuota)

□ Due tipi di buffer
  ▶ unbounded-buffer non c’è limite sulla dimensione del buffer (consumatore attende se vuoto)
  ▶ bounded-buffer dimensione fissa del buffer (consumatore attende se vuoto, produttore attende se pieno)

---

## Pagina 189

Bounded-Buffer – Shared-Memory

Un buffer limitato è condiviso tra processi in memoria condivisa

```c
#define BUFFER_SIZE 10
typedef struct {
    .....
} item;

item buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
```

Array circolare con indici in (prossima free) e out (prima posizione full)

Soluzione corretta, ma può allocare fino a BUFFER_SIZE-1 items

- Buffer pieno
- Buffer vuoto
  - ((in + 1) % BUFFER_SIZE) == out
  - in == out

---

## Pagina 190

Bounded-Buffer – Productore

```c
item next_produced;

while (true) {
    /* produce an item in next produced */
    while (((in + 1) % BUFFER_SIZE) == out)
        ; /* do nothing */
    buffer[in] = next_produced;
    in = (in + 1) % BUFFER_SIZE;
}
```

in + 1 = Size, Size % Size = 0 = out

| 1 | 2 | 3 | ... | Size-1 | ? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| in = out =0 | in = 1 | in = 2 | in = 3 | in = Size -2 | in = Size -1 |

---

## Pagina 191

Bounded Buffer – Consumatore

```c
item next_consumed;

while (true) {
    while (in == out)
        ; /* do nothing */
    next_consumed = buffer[out];
    out = (out + 1) % BUFFER_SIZE;

    /* consume the item in next consumed */
}

1 2 3 ... Size-1 ?
out = 0
in = Size - 1
```

---

## Pagina 192

Bounded Buffer – Consumatore

```c
item next_consumed;

while (true) {
    while (in == out)
        ; /* do nothing */
    next_consumed = buffer[out];
    out = (out + 1) % BUFFER_SIZE;

    /* consume the item in next consumed */
}

2 3 ... Size-1 ?
out = 1
in = Size - 1
```

---

## Pagina 193

Bounded-Buffer – Produuttore

item next_produced;

while (true) {
    /* produce an item in next produced */
    while (isBufferFull)
        ; /* do nothing */
    in = (in + 1) % BUFFER_SIZE;
    buffer[in] = next_produced;
    size++;
}

---

## Pagina 194

Bounded Buffer – Consumatore

```cpp
item next_consumed;

while (true) {
    while (isBufferEmpty)
        ; /* do nothing */
    next_consumed = buffer[out];
    out = (out + 1) % BUFFER_SIZE;
    size--;

    /* consume the item in next consumed */
}
```

---

## Pagina 195

Interprocess Communication – Message Passing

- Meccanismi che i processi usano per comunicare e per sincronizzarsi
- Messaggi – processi comunicano senza ricorrere a variabli condivise, ma si scambiano nessaggi
  - La dimensione del message può essere fissa o variabile
- IPC fornisce solitamente due operazioni:
  - send(message)
  - receive(message)

---

## Pagina 196

Message Passing

Se i processi $P$ e $Q$ vogliono comunicare devono:
- Stabilire un canale (communication link) tra loro
- Scambiare messaggi via send/receive

Implementazione:
- Come stabilire il canale?
- Può il canale coinvolgere più di due processi?
- Quanti canali di comunicazione tra coppie di processi comunicanti?
- Capacità di un canale?
- La dimensione del messaggio scambiato sul canale è fisso o variable?
- Il canale è unidirezionale o bi-direzionale?

---

## Pagina 197

Message Passing

□ Implementazione di un canale di comunicazione:

□ Non consideriamo tanto il canale fisico …
  ▶ Memoria condivisa
  ▶ Bus hardware
  ▶ Rete

□ … quanto il canale logico:
  ▶ Comunicazione diretta o indiretta
  ▶ Comunicazione sincrona o asincrona
  ▶ Buffering dei messaggi automatico o esplicito

---

## Pagina 198

Comunicazione Diretta

Processi devono nominarsi esplicitamente (naming):
- **send** ($P, message$) – invia message al processo P
- **receive** ($Q, message$) – riceve message dal processo Q

Propertà del canale di comunicazione:
- Il canale è stabilito automaticamente tra coppie di processi comunicanti (che conoscono l’identità reciproca)
- Il canale è stabilito tra esattamente due processi
- Per ogni coppia c’è esattamente un canale
- Il canale può essere unidirezionale o bi-direzionale

Variante - comunicazione **asimmetrica**:
- **send** ($P, message$) – invia message al processo P
- **receive** ($id, message$) – riceve message da qualunque processo (id ricevuto in ingresso)

Problema: modularità, modificando l’identità di un processo richiede revisione delle comunicazione

---

## Pagina 199

Comunicazione Indiretta

□ Messaggi mandati/ricevuti su mailboxes (o porte):
  □ Ogni mailbox ha un unico id
  □ Processi possono comunicare solo se condividono una mailbox

□ Propertà del canale:
  □ Canale stabilito solo se i processi condividono un mailbox
  □ Canale può essere associato a più processi
  □ Coppie di processi possono condividere più canali
  □ Canali sia unidirezionali che bi-direzionali

---

## Pagina 200

Comunicazione Indiretta

Operazioni
- Creare una nuova mailbox (porta)
- Inviare/ricevere messaggi (send/receive) via mailbox
- distruggere una mailbox

Primitive:
- send(A, message) – invia message alla mailbox A
- receive(A, message) – ricevi message dalla mailbox A

Propertà del canale:
- Canale stabilito solo se i processi condividono un mailbox
- Canale può essere associato a più processi
- Coppie di processi possono condividere più canali
- Canali sia unidirezionali che bi-direzionali

---

## Pagina 201

Comunicazione Indiretta

Condivisione del mailbox
- Si supponga che $P_1$, $P_2$, e $P_3$ condividano la mailbox A
- Se $P_1$, invia M ad A e $P_2$ e $P_3$ ricevono da A
- Chi prende il messaggio M?

Soluzione dipendono dal metodo scelto:
- Permettere una connessione tra solo due processi alla volta
- Permettere ad un processo alla volta di eseguire receive()
- Lasciare al sistema decidere il ricevente (al mittente verrà notificata la decisione)

La mailbox può essere proprietà del SO o di un processo (nello spazio di indirizzamento del processo).
- Per mailbox di proprietà di un processo utente, questo può solo ricevere (indirizzo), altri possono solo inviare (dismissa alla terminazione del processo)
- Se la mailbox è del SO questa non viene dismissa

---

## Pagina 202

Sincronizzazione

La comunicazione tra processi avviene con chiamate send-receive
Il message passing può essere bloccante o non bloccante
Bloccante considerato sincrono
- Blocking send -- mittente è bloccato finché il messaggio non viene ricevuto
- Blocking receive -- destinatario bloccato finché il messaggio non è disponibile

Non bloccante considerato asincrono
- Non-blocking send -- mittente invia il messaggio e continua ad eseguire
- Non-blocking receive -- destinatario riceve:
  - messaggio valido, oppure
  - messaggio nullo

Diverse combinazioni di politiche
- Se bloccati sia il mittente che il destinario abbiamo un rendezvous

---

## Pagina 203

Sincronizzazione

Con sincronizzazione bloccante il problema del produttore consumatore diventa triviale:

- Il produttore invia e attende il consume
- Il consumatore attende e consuma

```c
message next_produced;
while (true) {
    /* produce an item in next produced */
    send(next_produced);
}

message next_consumed;
while (true) {
    receive(next_consumed);

    /* consume the item in next consumed */
}
```

---

## Pagina 204

Buffering

- Lo scambio di messaggi utilizza un canale di comunicazione basato su code temporanee

- Le code sono implementate in tre modi:
  - Capacità zero – zero messaggi in coda, il mittente aspetta che il destinatario riceva (rendezvous)
  - Capacità limitata – capacità di $n$ messaggi in coda, il mittente aspetta se il canale è pieno
  - Capacità illimitata – la coda non ha lunghezza predefinita, il mittente non aspetta mai

- Capacità zero è detto senza buffering
- Capacità non zero è detto con buffering automatico

---

## Pagina 205

Esempio di IPC Systems - POSIX

POSIX Shared Memory

Un processo crea un segmento di shared memory con la call
shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);
- nome, modalità di apertura/creazione, permessi (read e write)
- restituisce un intero (descrittore di file)
- anche usata per aprire un segmento esistente per condividerlo

Creato l’oggetto si setta la dimensione
ftruncate(shm_fd, 4096);
- Settta la dimensione 4096 byte

Crea un memory-mapped file
mmap(0,SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);
- MAP_SHARED specifica che i cambiamenti sono condivisi

È quindi possibile scrivere su shared memory (puntatore) come su file
sprintf(shared memory, "Writing to shared memory");

---

## Pagina 206

IPC POSIX Producer

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>

int main()
{
/* the size (in bytes) of shared memory object */
const int SIZE = 4096;
/* name of the shared memory object */
const char *name = "OS";
/* strings written to shared memory */
const char *message_0 = "Hello";
const char *message_1 = "World!";

/* shared memory file descriptor */
int shm_fd;
/* pointer to shared memory object */
void *ptr;

/* create the shared memory object */
shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);

/* configure the size of the shared memory object */
ftruncate(shm_fd, SIZE);

/* memory map the shared memory object */
ptr = mmap(0, SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);

/* write to the shared memory object */
sprintf(ptr,"%s",message_0);
ptr += strlen(message_0);
sprintf(ptr,"%s",message_1);
ptr += strlen(message_1);

return 0;
}
```

Aperta con nome “OS” in modalità R/W - se non esiste creata con permessi R/W -

Dimensione SIZE

Mappata in memoria in modalità MAP_SHARED - cambiamenti visibili a chi condivide la memoria

PROT_WRITE permette la scrittura

Puntatore ptr incrementato in modalità non automatica

---

## Pagina 207

IPC POSIX Consumer

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>

int main()
{
/* the size (in bytes) of shared memory object */
const int SIZE = 4096;
/* name of the shared memory object */
const char *name = "OS";
/* shared memory file descriptor */
int shm_fd;
/* pointer to shared memory object */
void *ptr;

/* open the shared memory object */
shm_fd = shm_open(name, O_RDONLY, 0666);

/* memory map the shared memory object */
ptr = mmap(0, SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);

/* read from the shared memory object */
printf("%s", (char *)ptr);

/* remove the shared memory object */
shm_unlink(name);

return 0;
}
```

Aperta con nome “OS” in modalità lettura con permessi R/W

Dimensione SIZE

Mappata in memoria in modalità MAP_SHARED - cambiamenti visibili a chi condivide la memoria

PROT_READ permette la lettura

Rimuove l’oggetto shared mem

---

## Pagina 208

POSIX mmap

- La funzione `mmap`: mappa in process address space un file o un device
- Una volta mappato accessibile in modo diretto

`void * mmap (void *address, size_t length, int protect, int flags, int filedes, off_t offset)`

- **address**: indirizzo di partenza
- **length**: bytes richiesti
- **protect**: PROT_READ | PROT_WRITE | PROT_EXEC | PROT_NONE
- **flags**: MAP_SHARED, MAP_PRIVATE, MAP_ANON, MAP_FIXED
- **fildes**: descrittore di file
- **offset**: offset del file

---

## Pagina 209

Pipe

- Flusso di dati che permette a due processi di comunicare
- Uno dei primi meccanismi di comunicazione in UNIX
- Problematiche:
  - Comunicazione unidirezionale o bidirezionale?
  - Se two-way communication, è half o full-duplex?
  - Ci deve essere una relazione (i.e., parent-child) tra i processi comunicanti?
  - Si possono usare le pipes in una rete?

- Pipe ordinarie
  - Non può essere usata da processi che non hanno creato
  - Processo padre crea la pipe a la usa per comunicare con un processo figlio

- Named pipes
  - Possono essere usate senza una relazione parentale tra processi

---

## Pagina 210

Pipe Ordinarie

Pipe ordinarie comunicano in modalità produttore-consumatore
Produttore scrive su un’estremità (write-end della pipe)
Consumatore legge dall’altra estremità (read-end della pipe)
Le pipe ordinarie sono unidirezionali
Richiedono una relazione parentale tra i processi che comunicano

Windows le chiama anonymous pipes

---

## Pagina 211

Pipe Ordinarie

La funzione pipe in Unix

```c
#include <unistd.h>
int pipe ( int filedes[2] );
```

- l'argomento `filedes` è costituito da due descrittori di file:
  - `filedes[0]` è aperto in lettura e rappresenta il lato in lettura della pipe;
  - `filedes[1]` è aperto in scrittura e rappresenta il lato in scrittura della pipe;
  - l'output di `filedes[1]` è l'input per `filedes[0]`;

- restituisce 0 in caso di successo, -1 altrimenti.

---

## Pagina 212

Pipe Ordinarie

La funzione pipe in Unix

Generata da un singolo processo ha poca utilità ...

---

## Pagina 213

Pipe Ordinarie

La funzione pipe in Unix

• Tipicamente, un processo crea una pipe e poi chiama fork

---

## Pagina 214

Pipe Ordinarie

La funzione pipe in Unix

• Come utilizzare i pipe?
  • Cosa succede dopo la fork dipende dalla direzione dei dati
  • I canali non utilizzati vanno chiusi

• Esempio: parent → child
  • Il parent chiude l'estremo di read (close(fd[0]);)
  • Il child chiude l'estremo di write (close(fd[1]);)

parent
fd[0] fd[1]
child
fd[0] fd[1]
pipe
kernel

---

## Pagina 215

Pipe Ordinarie

La funzione pipe in Unix

```c
int fd[2];

if (pipe(fd) < 0)
    perror("pipe"), exit(1);
if ( (pid=fork()) < 0 )
    perror("fork"), exit(1);
else if (pid>0) { // padre
    close(fd[0]);
    write(fd[1], "ciao!", 5);
} else { // figlio
    close(fd[1]);
    n = read(fd[0], buf, sizeof(buf));
    write(STDOUT_FILENO, buf, n);
}
```

---

## Pagina 216

Pipe Ordinarie

La funzione pipe in Unix

```c
/* pipe1: invio di dati da un genitore ad un figlio */

#include <stdio.h>
#include <unistd.h>
#define MAXLINE 64

int main(void)
{
    int n, fd[2];
    pid_t pid;
    char line[MAXLINE];

    if (pipe(fd) < 0) perror("pipe"), exit(1);

    if ( (pid = fork()) < 0) perror("fork"), exit(1);

    else if (pid > 0) { /* genitore */
        close(fd[0]);
        write(fd[1], "hello world\n", 12);
    }
    else { /* figlio */
        close(fd[1]);
        n = read(fd[0], line, MAXLINE);
        write(STDOUT_FILENO, line, n);
    }
    exit(0);
}
```

---

## Pagina 217

Pipe Ordinarie

La funzione pipe in Unix

• All'inizio una pipe è vuota
• write aggiunge dati alla pipe
• read legge e rimuove dati dalla pipe
  – non si possono leggere piu' volte gli stessi dati da una pipe
  – non si puo' chiamare lseek su una pipe
  – i dati si ottengono in ordine First In First Out
• una pipe con una estremita' chiusa si dice rotta (broken)

---

## Pagina 218

Pipe Ordinarie

La funzione pipe in Unix

• Scrivere: write aggiunge i suoi dati alla pipe
  – se la pipe e' rotta, viene generato il segnale SIGPIPE e write restituisce un errore

• Leggere: read(fd[0], buf, 100)
  – meno di 100 bytes nella pipe: read legge l'intero contenuto della pipe
  – piu' di 100 bytes nella pipe: read legge i primi 100 bytes
  – pipe vuota: read si blocca in attesa di dati
  – pipe vuota e rotta: read restituisce 0

---

## Pagina 219

Pipe con Nome

- Named Pipes sono più potenti delle pipe ordinarie
- La comunicazione è bidirezionale
- Non è necessaria una relazione parentale tra processi comunicanti
- Molti processi possono usare le named pipe per comunicare
- Sia su UNIX che su Windows

---

## Pagina 220

Pipe con Nome in Unix

I file speciali FIFO (pipe con nome) consentono di superare alcune delle limitazione delle pipe. Essi difatti, rispetto a queste ultime, offrono i seguenti vantaggi:

• una volta creati, esistono nel file sistem fintanto che non vengono esplicitamente cancellati;
• possono essere usati da processi che non hanno un comune antenato.

I file FIFO possono essere creati in due modi:
• attraverso la shell, con il comando mkfifo;
• all'interno di un programma, con la chiamata alla funzione mkfifo.

Una volta creato un file FIFO, su di esso si possono effettuare le operazioni usuali di IO su file (open, read, write, close, ...)

---

## Pagina 221

Pipe con Nome in Unix

```c
#include <stdio.h>
#include <errno.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#define MAX_BUF_SIZE 1000

int main(int argc, char *argv[]){

int fd, ret_val, count, numread;
char buf[MAX_BUF_SIZE];

/* Create the named - pipe */
ret_val = mkfifo("miafifo", 0666);
if ((ret_val == -1) && (errno != EEXIST)) {
    perror("Error creating the named pipe");
    exit (1);
}

/* Open the pipe for reading */
fd = open("miafifo", O_RDONLY);

/* Read from the pipe */
numread = read(fd, buf, MAX_BUF_SIZE);
buf[numread] = '0';
printf("Server: Read From the pipe: %s\n", buf);
```

Codice Server

---

## Pagina 222

Pipe con Nome in Unix

```c
#include <stdio.h>
#include <errno.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

Codice Client

int main(int argc, char *argv[])
{
    int fd;

    /* Check if an argument was specified. */

    if (argc != 2) {
        printf("Usage : %s <string to be sent to the server>n", argv[0]);
        exit (1);
    }

    /* Open the pipe for writing */
    fd = open("miafifo", O_WRONLY);

    /* Write to the pipe */
    write(fd, argv[1], strlen(argv[1]));
```

Esempio esecuzione:

• $./servFifo &
• $./clientFifo prova
• Server : Read From the pipe : prova
• Server : Converted String : PROVA

---

## Pagina 223

Comunicazione in Sistemi Client-Server

- Per la comunicazione client-server vediamo due metodi
  - Sockets
  - Remote Procedure Call

---

## Pagina 224

Sistemi Client-Server

- Sistemi Client-Server
- Tipica archiettura di rete dove Sistemi Server rispondono alle richieste dei Sistemi client

---

## Pagina 225

Sistemi Distribuiti

- Sistemi distribuiti
  - Insiemi di calcolatori fisicamente separati con caratteristiche etereogenee connessi in una rete per consentire agli utenti l’accesso alle risorse distribuite
  - La rete fornisce un canale di comunicazione (es., tcp/ip)
  - Differenti tipi di reti
    - Local Area Network (LAN)
    - Wide Area Network (WAN)
    - Metropolitan Area Network (MAN)
    - Personal Area Network (PAN)

---

## Pagina 226

Socket

□ Una socket è un punto finale (endpoint) di comunicazione
□ Introdotti nel 1983 in Berkeley Software Distribution (BSD)
  □ Berkeley socket API
□ La comunicazione avviene tra coppie di socket
  □ Su stessa macchina (IPC locali) o diverse (IPC di rete)
□ Una socket internet è identificata da un indirizzo e una porta: 161.25.19.8:1625 indica la porta 1625 sull’host 161.25.19.8
□ La porta è un numero che differenzia diversi servizi su un host
□ Tutte le porte sotto 1024 sono usate per servizi standard
  □ Es. FTP 21, SSH 22, 25 smtp, 80 HTTP, etc. (vedi www.iana.org)
□ Un IP address speciale 127.0.0.1 (loopback) si riferisce al sistema in cui il processo gira

---

## Pagina 227

Comunicazione Socket

- Comunicazione Client-Server
  - Server in ascolto su una porta e Client richiede servizio
  - Processo Client stabilisce una comunicazione tramite una porta
    - Connessione unica per processo (altro Client altra porta)
  - Si possono definire diversi tipi di comunicazione
    - Connection oriented (TCP) o connectionless (UDP)

  ```
    host X
    (146.86.5.20)

    socket
    (146.86.5.20:1625)

    web server
    (161.25.19.8)

    socket
    (161.25.19.8:80)
  ```

---

## Pagina 228

Comunicazione Socket Unix

Comunicazione Client-Server Unix

Server in ascolto

```c
int fd1, fd2;
struct sockaddr_in mio_indirizzo;

mio_indirizzo.sin_family = AF_INET;
mio_indirizzo.sin_port = htons(5200);
mio_indirizzo.sin_addr.s_addr = htonl(INADDR_ANY);

fd1 = socket(PF_PF_INET, SOCK_STREAM, 0);
bind(fd1, (struct sockaddr *) &mio_indirizzo, sizeof(mio_indirizzo));

listen(fd1, 5);
fd2 = accept(fd1, NULL, NULL);
...
close(fd2);
close(fd1);
```

---

## Pagina 229

Comunicazione Socket Unix

Comunicazione Client-Server Unix
- Client connesso

```c
int fd;
struct sockaddr_in mio_indirizzo;

mio_indirizzo.sin_family = AF_INET;
mio_indirizzo.sin_port = htons(5200);
inet_aton("143.225.5.3", &indirizzo.sin_addr);

fd = socket(PF_INET, SOCK_STREAM, 0);
connect(fd, (struct sockaddr *) &mio_indirizzo,
sizeof(mio_indirizzo));
...
close(fd);
```

---

## Pagina 230

Comunicazione Socket Unix

- Comunicazione Client-Server Unix
- Schema di connessione

---

## Pagina 231

Shell Bash

---

## Pagina 232

Shell

• Programma che interpreta il linguaggio a linea di comando attraverso il quale l'utente utilizza le risorse del sistema.
• Permette la gestione di variabili e dispone di costrutti per il controllo del flusso delle operazioni.
• https://tldp.org/LDP/Bash-Beginners-Guide/html

• Viene generalmente eseguito in modalità interattiva, all'atto del login, restando attivo per tutta la durata della sessione di lavoro ed effettuando le seguenti operazioni:
  – Gestione del “main command loop”;
  – Analisi sintattica;
  – Esecuzione di comandi (“built-in”, file eseguibili) e programmi in linguaggio di shell (script);
  – Gestione dello standard I/O e dello standard error;
  – Gestione dei processi da terminale.

---

## Pagina 233

Ciclo Esecuzione Shell

operazioni di start-up
acquisizione di un comando
EOF?
Si
No
"macro espansione" del comando
operazioni di terminazione
esecuzione del comando

---

## Pagina 234

Shell

• Shell interattiva
  – **interattiva, non login** → legge ~/.bashrc
  – **interattiva, login** → legge uno tra
    • /etc/profile
    • ~/.bash_profile
    • ~/.bash_login
    • ~/.profile
  • Es., bash –login (exit per tornare interattivi)

---

## Pagina 235

Abilitare WSL in Win

• Menu Start
• Cerca PowerShell
• Clic destro su “Windows PowerShell”
• Selezionare Esegui come amministratore

• wsl --install
  abilita WSL e installa WSL2

• Riavviare il computer
• Creare utente linux

• Verificare istallazione con: wsl -l –v

• In win installare anche Visual Studio Code

---

## Pagina 236

Variabili di Shell

• Esistono delle variabili di shell predefinite (variabili di ambiente), che permettono di caratterizzare il comportamento della shell.

• Per convenzione, il nome di tali variabili è in caratteri tutti maiuscoli:
  – **HOME**: argomento di default per il comando `cd`, inizializzato da login con il path della home directory, letto dal file `/etc/passwd`;
  – **PATH**: il path di ricerca degli eseguibili;
  – **PS1**: stringa del prompt, di default $ per l'utente normale e # per il super-user;
  – **HOSTNAME**: nome del computer
  – **SHELL**: la shell corrente

---

## Pagina 237

Variabili predefinite

• PATH percorso di ricerca eseguibili
• USER nome utente
• HOME directory home dell'utente
• PS1 il prompt
• HOSTNAME nome computer
• SHELL la shell corrente
• ...

---

## Pagina 238

Shell Interattiva

• Comunicazione tra utente e shell avviene tramite comandi o script:
• Nome comando built-in oppure
• Nome di un file eseguibile oppure
• Nome di Script, cioè file ASCII presente nel sistema dotato del premesso di esecuzione.

---

## Pagina 239

Sintassi dei comandi

comando [argomento ...]

Gli argomenti possono essere:

• opzioni o flag (-)
• parametri

separati da almeno un separatore

Nota: Il separatore di default è il carattere spazio; per alcune shell può essere modificato grazie alla ridefinizione di una variabile d'ambiente opportuna (cfr. seg.).

Una volta interpretata la prima parola sulla linea di comando, la shell ricerca nel file system un file con il nome uguale a tale prima parola.

La ricerca avviene ordinatamente all'interno delle directory elencate nella variabile d'ambiente PATH

---

## Pagina 240

Listing di Processi

ps = process status → mostra i processi attivi.

Senza opzioni, elenca solo i processi collegati al terminale corrente e all’utente attivo (effective user).

Permette di osservare:
- PID (Process ID) → identificativo univoco del processo
- TTY → identificativo del terminale
- TIME → indica il tempo (hh:mm:ss) cumulato di utilizzo CPU
- CMD → comando che ha generato il processo

ps -f full information (comando Unix style)
UID, PID, PPID, C, STIME, TTY, TIME, CMD
(C sta per percentuale di utilizzo CPU)

ps -e (oppure -A) info su tutti i processi indipendentemente dal terminale
info su tutti processi con dettagli

ps -ef info su tutti processi con terminale, non demoni (BSD style)
STAT indica lo stato (Running, Sleeping, Zombi, etc.)

ps aux x senza terminale, u in formato utente

---

## Pagina 241

Listing di Processi

Albero dei processi (Process Tree)

• pstree → mostra padre/figli
• ps --forest → albero con ps

---

## Pagina 242

Listing di Processi

top – visualizza in tempo reale i processi e l’uso delle risorse (CPU, RAM, tempo). Versione dinamica di ps, con possibilità di interazione.

• PR → priority: priorità del processo (gestita dal kernel).
• NI → nice value: valore “nice” impostato dall’utente (influenza PR).
• VIRT → virtual memory: memoria virtuale totale usata dal processo (RAM + swap + lib).
• RES → resident memory: memoria realmente occupata in RAM.
• SHR → shared memory: memoria condivisa con altri processi (es. librerie).
• S → state: stato del processo (R=running, S=sleeping, T=stopped, Z=zombie).
• %CPU → percentuale di CPU usata.
• %MEM → percentuale di RAM usata.
• TIME+ → tempo totale di CPU consumato.
• COMMAND → nome/programma eseguito.

htop modalità interattiva

us = processi utente
sy = kernel
ni = processi “nice”
id = inattiva
wa = attesa I/O
hi/si = interrupt HW/SW
st = tempo rubato (VM)

---

## Pagina 243

Esempio

• Comando vmstat …
  • Proc: r (processi attivi), b (processi bloccati)
  • Mem: free, swap, buff
  • System: in (interrupt), cs (context switch), us (%user mode), sy (%kernel mode)
  • CPU: id (%idle time), wa (%I/O waiting time), st (%stolen time da hypervision)
  • Comando:
    – ls /proc/
    – cat /proc/interrupts
    – watch –n 1 cat /proc/interrupts

• timer: interrupt del timer di sistema
• i8042: tastiera o il touchpad.
• eth0: interfaccia di rete.
• ahci: Il controller del disco
• LOC local timer interrupt (per CPU)

IO-APIC: gestione avanzata degli interrupt nei sistemi x86

---

## Pagina 244

Variabili

• Scrittura/definizione: a=3 (senza spazi)
• Lettura: ${a} o semplicemente $a

Esempi:
> a=3
> echo $a
3
> echo $aa
> echo ${a}a
3a
> a=ciao pippo
bash: pippo: command not found
> echo “ecco: $a”
ecco: 3
> echo 'ecco: $a'
ecco: $a

---

## Pagina 245

Comando echo

echo [argomenti]

Visualizza gli argomenti in ordine, separati da singoli blank

Esempio:

```bash
echo $SHELL
echo $PATH
% echo uno due tre
uno due tre
%
```

---

## Pagina 246

(Ri)definizione di variabili di shell

La shell offre all'utente sia la possibilità di ridefinire alcune variabili d'ambiente, sia di definire delle nuove variabili a proprio piacimento.

Esempio 1

$$\text{frutto}=mela$$
$$\text{verbo}=mangia$$
$$\text{nome}=\text{Stefania}$$
$$\text{echo } \text{$nome} \text{ verbo una } \text{frutto}$$

Stefania mangia una mela

$$\$

---

## Pagina 247

(Ri)definizione di variabili di shell

Esempio 2

$ echo $PATH
$ /usr/bin:/home/gio:.
$ ps
sh: ps: No such file or directory
$ PATH=$PATH:/bin
$ ps
PID TTY TIME CMD
2487 ttyp1 00:00:00 sh
2488 ttyp1 00:00:00 ps
$

---

## Pagina 248

(Ri)definizione di variabili di shell

Esempio 3

$ frutto=mela
$ frutto=${frutto}banana
$ echo $frutto
melabanana
$ tipo="mela banana"
$ echo $tipo
mela banana
$

---

## Pagina 249

# File Standard

Normalmente, un programma (comando) opera su più file

In Unix esiste il concetto di **file standard**:

| File standard | Che cos'è |
| :--- | :--- |
| standard input | il file da cui normalmente il programma acquisisce i suoi input |
| standard output | il file su cui normalmete un programma produce i suoi output |
| standard error | il file su cui normalmente un programma invia i messaggi di errore |

---

## Pagina 250

Redirezione std I/O

• I programmi dispongono di 3 canali di comunicazione:
  – Standard input (codice 0), per input
  – Standard output (1), per output
  – Standard error (2), per errore

Normalmente:

Standard input = tastiera

Standard output= schermo

---

## Pagina 251

Redirezione File Standard

La shell può variare queste associazioni di default **redirigendo** i files standard su qualsiasi file nel sistema

---

## Pagina 252

Ridirezione Stn Output

comando argomenti > file

Redirige lo standard output del comando sul file:
• se file non esiste, viene creato
• se file non esiste, viene riscritto (>) oppure il nuovo output viene accodato (>>)

~>ls -a > listaFile.txt
~>echo $PATH >> listaFile.txt

---

## Pagina 253

Ridirezione Stn Input

command arg1 ... argn < file

Il file file viene redirettto sullo standard input del comando

---

## Pagina 254

Ridirezione Stn Error

comando argomenti 2> file
2>>

(Analogo a > e >>)

Esempio:

> echho “ciao!”
bash: echho: command not found
> echho “ciao!” 2> /dev/null

---

## Pagina 255

Ridirezione

comando (codiceA)>&(codiceB)  redirige il canale A sul canale B

– esempio: comando > file 2>&1

---

## Pagina 256

Ridirezione

Per redigere correttamente, è necessario conoscere, di ogni comando:

• come usa lo standard input
• come usa lo standard output
• come usa l'error output
• come usa eventuali altri files

---

## Pagina 257

Esempio

1. Lista oppure msg di errore per directory non trovata
2. Msg di errore per operazioni illegali (usage: ...)

Non ha standard input

Inoltre accede ai files di sistema:

/etc/passwd per trovare lo user name

---

## Pagina 258

Pipe (tubo)

comando1 | comando2

Pipeline di due o più comandi:
Lo standard output di com1 funge da input a com2...

• com1 [arg ..] | com2 [arg ..]..|...

Esempi di comandi concatenabili: cat, sort, wc

~> cat file | sort
~> ls | less

---

## Pagina 259

Esercizi

• Creare un file che si chiami come l'utente corrente
• Creare un file che si chiami come l'host corrente, e che contenga il nome dell'host corrente

---

## Pagina 260

Command substitution

• Il pattern $(comando) viene sostituito con l'output del comando

• Esempi:
  - $(ls) equivale a *
  - $(echo ciao) equivale a ciao
  - $(cat nomefile) equivale all'intero contenuto del file
  - a=$$(ls) assegna ad a l'elenco dei file nella dir corrente
  - touch “$(date)” crea un file chiamato come la data attuale

---

## Pagina 261

Metacaratteri

• La shell riconosce alcuni caratteri speciali, chiamati **metacaratteri**, che possono comparire nei comandi.
• Quando l’utente invia un commando, la shell lo scandisce alla ricerca di metacratteri che processa in modo speciale
• Esempio:

```java
user> ls *.java
Albero.java div.java ProvaAlbero.java
AreaTriangolo.java EasyIn.java ProvaAlbero1.java
AreaTriangolo1.java IntQueue.java

Il metacarattere * nel pathname è un’abbreviazione per un nome di file. Il pathname *.java viene espando dalla shell con tutti I nome di file che terminano con .java. Il commando ls fronisce la lista di tutti i file con tale estensione
```

---

## Pagina 262

Abbreviazione pathname

• I seguenti metacaratteri, detti wildcard sono usati per abbreviare il nome di un file in un path name:

| Metacarattere | Significato |
| :--- | :--- |
| * | stringa di 0 o più caratteri |
| ? | singolo carattere |
| [ ] | singolo carattere tra quelli elencati |
| { } | stringa tra quelle elencate |

Esempi:

```bash
user> cp /JAVA/Area*.java /JAVA_backup
copia tutti i files il cui nome inizia con la stringa Area e termina con l'estensione
.java nella directory JAVA_backup.

user> ls /dev/tty?
/dev/ttya /dev/ttyb
```

---

## Pagina 263

Abbreviazione pathname

• I seguenti metacaratteri, detti wildcard sono usati per abbreviare il nome di un file in un path name:

```bash
user> ls /dev/tty?[234]
/dev/ttyp2 /dev/ttyp4 /dev/ttyq3 /dev/ttyr2 /dev/ttyr4
/dev/ttyp3 /dev/ttyq2 /dev/ttyq4 /dev/ttyr3

user> ls /dev/tty?[2-4]
/dev/ttyp2 /dev/ttyp4 /dev/ttyq3 /dev/ttyr2 /dev/ttyr4
/dev/ttyp3 /dev/ttyq2 /dev/ttyq4 /dev/ttyr3

user> mkdir /user/studenti/rossi/{bin,doc,lib}
crea le directory bin, doc, lib .
```

---

## Pagina 264

Quoting

Il meccanismo del **quoting** è utilizzato per inibire l’effetto dei metacaratteri. I metacaratteri a cui è applicato il quoting perdono il loro significato speciale e la shell li tratta come caratteri ordinari.

Ci sono tre meccanismi di quoting:

• il metacarattere di **escape** \ inibisce l’effetto speciale del metacarattere che lo segue:
  user> cp file file\?
  user> ls file*
  file    file?

• tutti i metacaratteri presenti in una stringa racchiusa tra **singoli apici** perdono l’effetto speciale:
  user> cat ’file*?’
  …

• i metacaratteri per l’abbreviazione del pathname presenti in una stringa racchiusa tra **doppi apici** perdono l’effetto speciale (ma non tutti i metacaratteri della shell):
  user> cat "file*?"

---

## Pagina 265

<table><thead><tr><th>Simbolo</th><th>Significato</th><th>Esempio d’uso</th></tr></thead><tbody><tr><td>&gt;</td><td>Ridirezione dell’output</td><td>ls &gt;temp</td></tr><tr><td>&gt;&gt;</td><td>Ridirezione dell’output (append)</td><td>ls &gt;&gt;temp</td></tr><tr><td>&lt;</td><td>Ridirezione dell’input</td><td>wc -l &lt;text</td></tr><tr><td>&lt;&lt;delim</td><td>ridirezione dell’input da linea di comando (here document)</td><td>wc -l &lt;&lt;delim</td></tr><tr><td>*</td><td>Wildcard: stringa di 0 o più caratteri, ad eccezione del punto (.)</td><td>ls *.c</td></tr><tr><td>?</td><td>Wildcard: un singolo carattere, ad eccezione del punto (.)</td><td>ls ?.c</td></tr><tr><td>[...]</td><td>Wildcard: un singolo carattere tra quelli elencati</td><td>ls [a-zA-Z].bak</td></tr><tr><td>{...}</td><td>Wildcard: le stringhe specificate all’interno delle parentesi</td><td>ls {prog,doc}*.txt</td></tr></tbody></table>

---

## Pagina 266

<table><thead><tr><th>Simbolo</th><th>Significato</th><th>Esempio d’uso</th></tr></thead><tbody><tr><td>|</td><td>Pipe</td><td>ls | more</td></tr><tr><td>;</td><td>Sequenza di comandi</td><td>pwd;ls;cd</td></tr><tr><td>||</td><td>Esecuzione condizionale. Esegue un comando se il precedente fallisce.</td><td>cc prog.c || echo errore</td></tr><tr><td>&amp;&amp;</td><td>Esecuzione condizionale. Esegue un comando se il precedente termina con successo.</td><td>cc prog.c && a.out</td></tr><tr><td>(...)</td><td>Raggruppamento di comandi</td><td>(date;ls;pwd)>out.txt</td></tr><tr><td>#</td><td>Introduce un commento</td><td>ls # lista di file</td></tr><tr><td>\</td><td>Fa in modo che la shell non interpreti in modo speciale il carattere che segue.</td><td>ls file.\*</td></tr><tr><td>!</td><td>Ripetizione di comandi memorizzati nell’history list</td><td>!ls</td></tr></tbody></table>

---

## Pagina 267

Shell expansions and substitutions

disabled by:

- Tilde expansion
- Variable substitution $a$
- Arithmetic substitution $((...))$
- Command substitution $((...))$
- Filename expansion (wildcards)
- Word splitting
- Execute command

Warning: Quoting works differently with assignments

---

## Pagina 268

Word splitting

L’ultima fase prima di eseguire un comando consiste nella suddivisione in parole

La variabile IFS (internal field separator) definisce i separatori
Di default, IFS=”<space><tab><newline>”

Come effetto collaterale, il word splitting sostituisce i newline con spazi
In una directory con molti file, confrontare l'output di “Is” con quello di “echo $(ls)”

---

## Pagina 269

Altri Comandi

---

## Pagina 270

pwd (print working directory)

pwd "printworking directory"
stampa il path della directory corrente

Esempio:

```bash
% pwd
/usr/mariog
%
```

---

## Pagina 271

cd (change directory)

cd [directory]
Cambia la directory corrente a quella indicata.
Se non viene passato nessun argomento, la directory corrente diventa la home directory.

Esempio:
1so:~>cd
1so:~>pwd
/home/1so
1so:~>cd esempio/esempiocd
1so:~>pwd
/home/1so/esempio/esempiocd

---

## Pagina 272

ls (list)

ls [options] [directory]
Elenca i file contenuti nella directory specificata.
Se la directory non e' indicata, viene elencato il contenuto della directory corrente.
Alcune opzioni:
-a Elenca anche i file nascosti
-l Formato esteso con informazioni su modo, proprietario, dimensione, etc dei file
-s fornisce la dimensione in blocchi dei file
-t lista i file nell'ordine di modifica (prima il file modificato per ultimo)
-1 elenca i file in una singola colonna
-F aggiunge / al nome delle directory e * al nome dei file eseguibili
-R si chiama ricorsivamente su ogni subdirectory

---

## Pagina 273

Is – campi del formato esteso

Totale dimensione occupata (in blocchi)

Riferimenti al file

Dimensione (byte)

Nome

sol1:~>ls -l
total 12
-rw-rw-r-- 1 lso lso 10 Mar 4 13:29 a
-rw-rw-r-- 1 lso lso 10 Mar 4 14:12 b
drwxrwxr-x 2 lso lso 4096 Mar 4 14:29 c

Proprietario

Gruppo primario

Data ultima modifica

Tipo

Permessi

(r)ead, (w)rite, e(x)ecute, (s)et uid bit

(d)directory, (l)ink, (c)haracter special file, (b)lock special file, (-) ordinary file

---

## Pagina 274

cp (copy)

cp [options] source... target

copia un file in un altro file oppure uno o più file in una directory

Se vengono specificati solo i nomi di due file, il primo viene copiato sul secondo

Se vengono specificati solo due nomi, e se il secondo nome indicato è una directory, source viene copiato con lo stesso nome nella directory target. Se source è una directory, la copia avviene solo con opzioni particolari.

Se vengono indicati più di due nomi, il file target deve essere una directory e vengono generate le copie dei source in target. In mancanza di opzioni particolari, le directory non vengono copiate.

Alcune opzioni

-r se source e target sono directory, copia ricorsivamente source, i suoi file e le sue subdirectory in target

-i opera in modo interattivo, chiedendo una conferma se la copia comporta la cancellazione di un target preesistente

---

## Pagina 275

Esempi

• Copia il file pippo nella directory corrente nel file /tmp/pippo.back
  cp pippo /tmp/pippo.back

• Copia il file /tmp/pippo.back e la directory dir nella directory nuovadir
  cp -r /tmp/pippo.back dir nuovadir

• Copia il file pippo nel file pippo2
  cp pippo pippo2

---

## Pagina 276

mv (move)

mv [options] source... destination
rinomina (sposta) file o directory.

Se vengono specificati solo i nomi di due elementi, source viene rinominato in destination, oppure in destination/source, a seconda che destination indichi un file o una directory. Qualora destination denoti un file preesistente, questo non sarà più accessibile come tale, e non sarà più accessibile in alcun modo se destination era il suo unico nome.

Se vengono indicati più di due elementi, destination deve essere una directory, e source_1...source_n vengono rinominati come destination/source_1...destination/source_n.

Nel caso che source e destination appartengono a due diversi file system, il comando effettua un vero e proprio spostamento dati tra i due file system. In tal caso vengono spostati solo i file ordinari, quindi: né collegamenti, né directory.

Alcune opzioni:

-i il comando chiede conferma all'utente qualora destination è un file preesistente

---

## Pagina 277

rm (remove)

rm [options] file...
elimina i file o le directory indicati come argomento.

Alcune opzioni:
-i chiede conferma prima di rimuovere ogni file
-R rimuove ricorsivamente i file e le sottodirectory

Esempi d'uso
Elimina i file pippo nella directory corrente e /tmp/pippo.back
rm pippo /tmp/pippo.back
Elimina la directory nuovadir e tutto il suo contenuto
rm -R nuovadiru
Elimina tutti i file nella directory corrente
rm *

---

## Pagina 278

wc (word count)

wc [options] [file...]

fornisce il numero dei codici di interruzione di riga (in pratica il numero delle righe), delle parole o dei caratteri contenuti in file. Senza opzioni fornisce, nell'ordine suddetto, ciascuna delle precedenti informazioni.

Alcune opzioni:
-c emette solo il numero complessivo di caratteri di file.
-w emette solo il numero complessivo di parole in file.
-1 emette solo il numero di righe in file.

Esempi di esecuzione

gio$ wc which_manpage
132 239 2083 which_manpage

gio$ wc -c which_manpage
2083 which_manpage
gio$

---

## Pagina 279

cat (concatenate)

cat [options] [file...]

concatena i file indicati come argomento, visualizzandoli attraverso lo standard output

Alcune opzioni:

-n fa precedere ogni linea di ouput dal numero progressivo che identifica la posizione della linea nel file concatenato

-b come l'opzione precedente, ma omette la numerazione delle linee bianche

-v mostra anche i caratteri non stampabili, ad eccezione dei caratteri di tabulazione, nuova linea e ritorno a capo

---

## Pagina 280

Comando cat

cat file...

"concatenate"

Concatena i file e li scrive sullo standard output...

% cat file1 file2 file1 ei fu
ei fu file2 siccome immobile
siccome immobile

% cat file1 file2 > file3

%

... a meno che manchino gli argomenti, nel qual caso scrive lo standard input sullo standard output

---

## Pagina 281

cut

cut [options] [file...]

estrae delle colonne specifiche dalle linee di testo che compongono file.

Alcune opzioni:
-c char_list
-f field_list
  definisce gli intervalli da estrarre espressi in caratteri.
  definisce gli intervalli da estrarre espressi in campi.
  I campi sono distinti in base a un certo carattere usato

  come delimitatore. Quello predefinito è il carattere di tabulazione.
  definisce un delimitatore alternativo al carattere di tabulazione.

Esempi d'uso
Estrae la prima e la quinta colonna del file /etc/passwd
cut -d: -f1,5 /etc/passwd

Estrae i primi dieci caratteri da ogni riga del file /etc/passwd
cut -c1-10 /etc/passwd

---

## Pagina 282

Sort

sort [options] [file…]

permette di (ri)ordinare o fondere insieme il contenuto dei file passati come parametri, oppure di (ri)ordinare le linee passategli in input.

In assenza di opzioni che definiscano diversi criteri di ordinamento, quest'ultimo avviene in base al primo campo ed è alfabetico.

Alcune opzioni:
-f ignora le differenze tra lettere minuscole e maiuscole
-n considera numerica anzichè testuale la chiave di ordinamento
-r ordina in senso decrescente anzichè crescente
-o fileout invia l'output a fileout anzichè sull'output standard
-t s usa s come separatore di campo
-k s1,s2 usa i campi da s1 a s2-1 come chiavi di ordinamento

---

## Pagina 283

sort – Esempi d'uso

Ordina le linee del file /etc/passwd in base al valore del terzo campo (UID)

sort -t: -k3,4 /etc/passwd

Come prima, solo che ora l'ordinamento è numerico anzichè alfabetico

sort -t: -n -k3,4 /etc/passwd

Come prima, ma seguendo l'ordinamento inverso (prima l'UID maggiore)

sort -t: -n -k3,4 -r /etc/passwd

Come prima, ma ora l'output è memorizzato in passwd_reordered

sort -t: -n -k3,4 -r /etc/passwd -o passwd_reordered

---

## Pagina 284

# Esempio

## # sort senza < (argomento file)
sort dati.txt
# a
# b
# c

## # sort con < (stdin da file)
sort < dati.txt
# a
# b
# c

## #word counter
wc 0< dati.txt
# 3 3 6

---

## Pagina 285

head & tail

| Comando/Sintassi | Descrizione |
| :--- | :--- |
| head [-numero] file | visualizza le prime 10 (o -numero) linee di un file |
| tail [-numero] file | visualizza le ultime 10 (o -numero) linee di un file |

Esempio d’uso head:
head -40 filename
oppure
head -n 40 filename

Esempio d’uso tail:
tail -30 filename

---

## Pagina 286

find

find [pathname...] [expression]

discende ricorsivamente le directory specificate (pathname...), cercando tutti i file che rendono vera expression.

Molto flessibile:

• ricerca file di specificati attributi (nome, tipo, permessi, proprietario, gruppo, numero di link, dimensione, data di ultima modifica/accesso …)
• and, or, not di attributi
• può eseguire automaticamente, o previa conferma, uno o più comandi sui file individuati
• le espressioni si ottengono combinando flag, parametri e gli operatori booleani;
• le espressioni costituite solo da un flag e da un parametro (opzionale) si dicono espressioni elementari;

---

## Pagina 287

Esempi

Ricerca in /home/lso di file la cui dimensione è maggiore di 100 blocchi

find /home/lso -size +100

Ricerca dalla working dir (ricorsivamente) dei file con nome “pattern”

find . -type f -name “pattern”

Es.

find . -type f -name "*.txt"
find . -maxdepth 1 -type f -name "*.txt"

---

## Pagina 288

Lezione 7: Threads & Concorrenza

---

## Pagina 289

Obiettivi

- Introdurre la nozione di thread
- Multithreaded programming
- Supporti per threads in Linux

---

## Pagina 290

Motivazioni

- Le applicazioni sono generalmente multithreaded
- Task multipli in applicazioni implementati da thread separati
  - Update del display
  - Fetch data
  - Spell checking
  - Risposta in rete
- La creazione di processo è pesante, il thread è leggero
- Il kernel è generalmente multithreaded

---

## Pagina 291

Processi Single e Multithreaded

- Unità base di utilizzo di CPU
  - Caratterizzati da Thread ID, PC, Registri e Stack
  - Minima identità di task

![Single-threaded process](image1)

![Multithreaded process](image2)

---

## Pagina 292

Architettura di Server Multithread

- Molto utilizzate nelle architetture client-server
  - Per ogni client si genera un thread che gestisce il client
  - Ogni richiesta di un client gestita da un thread
  - Server può gestire tante richieste eseguendo molti task leggeri

  (1) request
  (2) create new thread to service the request
  (3) resume listening for additional client requests

---

## Pagina 293

Benefici

□ Risposta
  □ Esecuzione continua se una parte del processo è bloccata (importante per le interfacce utente)

□ Risorse
  □ Thread condividono le risorse di un processo, più semplice di shared memory o message passing

□ Economia
  □ Più leggero di una creazione di processo, il thread switching ha minore overhead del context switching

□ Scalabilità
  □ I processi possono avvantaggiarsi delle architetture multiprocessore

---

## Pagina 294

Multicore Programming

- Sistemi mutitread forniscono meccanismi utili per sistemi multicore
- Sistemi Multicore o multiprocessori pongono diversi problemi:
  - Come dividere le attività sui core
    - Computazioni parallelizzabili su più core
  - Come bilanciare i calcolo sui core
  - Come splittare i dati
  - Come gestire le dipendenze dei dati sui core
    - Dipendenze possono richiedere sincronizzazione
  - Come fare test e debugging
    - Più tracce di esecuzioni da testare

- Parallelismo
  - Più di un task simultaneamente distribuiti su più unità di calcolo

- Concorrenza
  - Consente il progresso contemporaneo di più di un task
  - Se processore/core singolo, concorrenza data dallo scheduler che intrallaccia le esecuzioni

---

## Pagina 295

Multicore Programming

Tipi di parallelismo

- Parallelismo di dati – sottoinsiemi dei dati su core multipli con stessa operazione per ognuno
  - Ad esempio calcolo della somma dei numeri su array, si può dividere il compito

- Parallelismo di task – thread sui core dove ciascuno svolge un’operazione particolare
  - Esempio media e varianza di un set di dati

Al crescere del numero dei thread aumenta il supporto architetturale

- CPU hanno core e hardware thread
- Esempio, i7 (13th Gen) con 16 core e 24 hardware threads

---

## Pagina 296

Concorrenza vs. Parallelismo

□ Esecuzione concorrente su sistema single-core:

single core
$T_1$ $T_2$ $T_3$ $T_4$ $T_1$ $T_2$ $T_3$ $T_4$ $T_1$ …

□ Parallelismo su sistema multi-core:

core 1
$T_1$ $T_3$ $T_1$ $T_3$ $T_1$ …

core 2
$T_2$ $T_4$ $T_2$ $T_4$ $T_2$ …

---

## Pagina 297

Legge di Amdahl

- Guadagno teorico in performance con l’aggiunta di un core per un’applicazione che ha sia componenti seriali che paralleli
  - S è la porzione seriale
  - N sono i core per il processamento

$$\text{speedup} \leq \frac{1}{S + \frac{(1-S)}{N}}$$

- Esempio: se l’applicazione è al 75% parallela e 25% seriale, passando da 1 a 2 core si ha uno speed-up di 1.6 volte
- Con $N$ che tende ad infinito lo speed-up tende a 1 / S

---

## Pagina 298

Legge di Amdahl

- Guadagno teorico in performance (latenza) con l’aggiunta di un core per un’applicazione che ha sia componenti seriali che paralleli
  - S è la porzione di calcolo seriale (non parallelizzabile)
  - N sono i core per il processamento

$$\text{speedup} \leq \frac{1}{S + \frac{(1-S)}{N}}$$

- La porzione seriale di un’applicazione ha effetto molto marcato sul guadagno di performance con un core aggiuntivo

---

## Pagina 299

User Thread e Kernel Thread

□ User thread – gestita da librerie di thread di livello utente

□ Tre principali:
  □ POSIX Pthreads
  □ Windows threads
  □ Java threads

□ Kernel thread - supportati dal Kernel

□ Esempi – tutti gli SO general purpose inclusi:
  □ Windows
  □ Solaris
  □ Linux
  □ Tru64 UNIX
  □ Mac OS

---

## Pagina 300

Modelli di Multithreading

- Diversi modi di gestire la relazione tra User e Kernel thread
  - Many-to-One
  - One-to-One
  - Many-to-Many

---

## Pagina 301

Many-to-One

- Tanti thread user mappati su un singolo kernel thread
- Però un thread bloccante (es. durante una system call) può bloccare tutto
- Problemi di parallelismo con sistemi multicore perché uno solo alla volta è in esecuzione nel Kernel
- Pochi sistemi utilizzano questo approccio:
  - Solaris Green Threads library
  - GNU Portable Threads library

---

## Pagina 302

Many-to-One

- Tanti thread user mappati su un singolo kernel thread
- Lato kernel un solo PCB per gestire i thread di un processo

Fig. tratta dal corso SO di UniMore

---

## Pagina 303

One-to-One

- Ogni thread user-level mappato su kernel thread
  - La creazione di thread user-level crea un kernel thread
  - Maggiore concorrenza di many-to-one
  - Il numero di thread per processo può essere limitato per evitare overhead
- Esempi:
  - Windows
  - Linux
  - Solaris 9 e successivi
- Utente deve controllare il numero dei thread

---

## Pagina 304

One-to-One

- Ogni thread user-level mappato su kernel thread
- La creazione di thread user-level crea un kernel thread

Fig. tratta dal corso SO di UniMore

---

## Pagina 305

Many-to-Many

- Molti thread user-level sono mappati su molti thread del kernel
- Il SO può creare un numero sufficiente di thread del kernel
  - Però può gestirne il numero e il grado di parallelismo

- Esempi:
  - Solaris dalla versione 9
  - Windows con ThreadFiber package

- Il numero può dipendere dalla macchina e dall’applicazione

- L’utente può lanciare più thread, poi controlla il Sistema quanti thread kernel

---

## Pagina 306

Many-to-Many

- Molti thread user-level sono mappati su molti thread del kernel
- Il SO può creare un numero sufficiente di thread del kernel
- Però può gestirne il numero e il grado di parallelismo

Fig. tratta dal corso SO di UniMore

---

## Pagina 307

Two-level Model

- Variante del Many-to-Many che permette ad un user-thread di essere legato (bound) ad un kernel thread

- Esempi:
  - IRIX
  - HP-UX
  - Tru64 UNIX
  - Solaris 8 e precedenti

---

## Pagina 308

Attivazioni Scheduler

- Sia modelli Many-to-Many che Two-level richiedono di mantenere un numero appropriato di kernel thread allocati per l’applicazione
- Tipicamente usata una struttura dati intermedia tra user e kernel thread – lightweight process (LWP)
  - Come un processore virtuale su cui il processo può schedulare l’esecuzione di user thread
  - Ogni LWP è associato ad un kernel thread
- Il kernel fornisce ad un’applicazione un insieme di LWPs e l’applicazione può schedulare gli user thread su questi
- Il kernel deve comunicare con l’applicazione
  - **upcalls** – quando si sta per bloccare il kernel è gestito da **upcall-handler**
    - comunica all’applicazione che sta per bloccarsi, crea un nuovo LWP
    - consente all’applicazione di schedulare un nuovo processo
- Questa comunicazione consente ad un’applicazione di mantenere il corretto numero di kernel thread

---

## Pagina 309

Librerie per Thread

- Librerie per i thread (Thread library)
  - API per creare e gestire i thread

- Due modi principali di implementarle
  - Libreria interamente nello user space
    - I thread sono implementati al livello utente (gestiti con chiamate di funzione utente)

- Libreria al livello Kernel supportata dal SO
  - I thread sono gestiti con chiamate di Sistema (gestiti con chiamata di sistema)

---

## Pagina 310

Librerie per Thread

- Librerie per i thread (Thread library)
  - API per creare e gestire i thread

- Due modi principali di implementarle
  - Libreria interamente nello user space
  - Libreria al livello Kernel supportata dall’SO

---

## Pagina 311

Pthreads

- Estensione di POSIX standard (IEEE 1003.1c) fornisce le API per la creazione e sincronizzazione dei thread

- Esiste sia in versione user-level sia kernel-level

- **Specifica**, non implementazione

- API specifica il comportamento delle funzioni di libreria, implementazione lasciata allo sviluppatore

- Tipiche in UNIX (Solaris, Linux, Mac OS)

---

## Pagina 312

Esempio Pthreads

- Esempio somma dei primi N numeri
  - Per esempio per N = 5, Sum = 1 + 2 + 3 + 4 + 5 = 15
  - Si può delegare il calcolo ad uno o più thread
  - Abbiamo thread `sincroni` e `asincroni`
    - Nel caso sincrono il genitore aspetta i figli
    - Nel caso asincrono il genitore continua subito

---

## Pagina 313

Esempio Pthreads

```c
#include <pthread.h>
#include <stdio.h>

int sum; /* this data is shared by the thread(s) */
void *runner(void *param); /* threads call this function */

int main(int argc, char *argv[])
{
    pthread_t tid; /* the thread identifier */
    pthread_attr_t attr; /* set of thread attributes */

    if (argc != 2) {
        fprintf(stderr,"usage: a.out <integer value>\n");
        return -1;
    }
    if (atoi(argv[1]) < 0) {
        fprintf(stderr,"%d must be >= 0\n",atoi(argv[1]));
        return -1;
    }
}
```

---

## Pagina 314

Esempio Pthreads

```c
/* get the default attributes */
pthread_attr_init(&attr);
/* create the thread */
pthread_create(&tid, &attr, runner, argv[1]);
/* wait for the thread to exit */
pthread_join(tid, NULL);

printf("sum = %d\n", sum);
}

/* The thread will begin control in this function */
void *runner(void *param)
{
    int i, upper = atoi(param);
    sum = 0;

    for (i = 1; i <= upper; i++)
        sum += i;

    pthread_exit(0);
}
```

---

## Pagina 315

Codice Pthreads per il join di 10 Thread

```c
#define NUM_THREADS 10

/* an array of threads to be joined upon */
pthread_t workers[NUM_THREADS];

for (int i = 0; i < NUM_THREADS; i++)
    pthread_join(workers[i], NULL);
```

---

## Pagina 316

Pthreads

Per creare thread addizionali relativi ad uno stesso processo, Posix prevede la funzione:

```c
#include <pthread.h>

int pthread_create ( pthread_t *tid, const pthread_attr_t *attr,
                    void * ( *start_func) (void *), void *arg );
```

• se la chiamata ha successo, *tid* punta al thread ID;
• *attr* permette di specificare gli attributi del thread (se *attr* = NULL, gli attributi sono quelli di default);
• *start_func* è l'indirizzo della funzione di avvio;
• *arg* è l'indirizzo dell'argomento accettato dalla funzione di avvio;
• restituisce 0 in caso di successo, un intero positivo – secondo le convenzioni di `<sys/errno.h>` – in caso di errore.

---

## Pagina 317

Pthreads

```c
typedef void (*thread_start)(void *);

int pthread_create(pthread_t *tid,
                  const pthread_attr_t *attributes
                  thread_start start,
                  void *argument);
```

• Restituisce 0 se OK, un codice d'errore altrimenti
• tid = argomento di ritorno, conterrà il tid del nuovo thread
• attributes = attributi del thread (vedere dopo)
• start = indirizzo della funzione da cui partire
• argument = l'argomento passato alla funzione start

---

## Pagina 318

Pthreads

void pthread_exit(void *status);

• termina il thread corrente, con valore di uscita status
• altri thread possono raccogliere il valore di uscita usando pthread_join (vedere slide successiva)
• fare attenzione che i dati puntati da ret sopravvivano alla terminazione del thread!

– status non deve puntare allo stack (no variabili locali)
– Ok uso di variabili globali o allocate dinamicamente

---

## Pagina 319

Pthreads

Un thread può attendere per la terminazione di un altro thread relativo allo stesso processo:

```c
#include <pthread.h>

int pthread_join (pthread_t *tid, void **status);
```

• tid è l'ID del thread del quale si vuole attendere la terminazione;
• status punta al valore restituito dal thread per cui si è atteso, indicante il suo stato di terminazione (se status = NULL, tale stato non viene restituito);
• restituisce 0 in caso di successo, un intero positivo – secondo le convenzioni di <sys/errno.h> – in caso di errore.

---

## Pagina 320

Pthreads

/* thread_create: stampa i TID del main thread e di due altri thread */

#include <pthread.h>
#include <stdio.h>
#include <errno.h>

void *start_func(void *arg) /* funzione di avvio */
{
    printf("%s", (char *)arg);
    printf(" and my TID is: %d\n", (int)pthread_self());
}

int main(void)
{
    int en;
    pthread_t tid1, tid2;
    char *msg1 = "Hello world, I am thread #1";
    char *msg2 = "Hello world, I am thread #2";

    printf("The launching process has PID:%d\n", (int)getpid());

    printf("The main thread has TID:%d\n", (int)pthread_self());
}

---

## Pagina 321

Pthreads

/* thread_create: stampa i TID del main thread e di due altri thread */

#include <pthread.h>
#include <stdio.h>
#include <errno.h>

void *start_func(void *arg) /* funzione di avvio */
{
    printf("%s", (char *)arg);
    printf(" and my TID is: %d\n", (int)pthread_self());
}

int main(void)
{
    int en;
    pthread_t tid1, tid2;
    char *msg1 = "Hello world, I am thread #1";
    char *msg2 = "Hello world, I am thread #2";

    printf("The launching process has PID:%d\n", (int)getpid());

    printf("The main thread has TID:%d\n", (int)pthread_self());
}

---

## Pagina 322

Pthreads

```c
/* crea il 1mo thread */
if ((en = pthread_create(&tid1, NULL, start_func, msg1)!=0))
    errno=en, perror("pthread_create"), exit(1);

/* crea il 2ndo thread */
if ((en = pthread_create(&tid2, NULL, start_func, msg2)!=0))
    errno=en, perror("pthread_create"), exit(2);

/* attende per il 1mo */
if ((en = pthread_join(tid1, NULL)!=0))
    errno=en, perror("pthread_join"), exit(1);

/* attende per il 2ndo */
if ((en = pthread_join(tid2, NULL)!=0))
    errno=en, perror("pthread_join"), exit(2);

return 0;
}
```

---

## Pagina 323

Pthreads

typedef struct foo{
    int a;
    int b;
} myfoo;

myfoo test; // Variabile GLOBALE

void stampa(char *st, struct foo *test){
    printf("%s: tid=%d a=%d b=%d\n", st, pthread_self(),test->a, test->b);
}

void *fun1(void *arg){
    myfoo test2 = {1,2}; // Variabile LOCALE
    printf("%s %d\n", arg, pthread_self());
    stampa(arg, &test2);
    pthread_exit((void *)&test2);
}

---

## Pagina 324

Pthreads

```cpp
void *fun2(void *arg){
    test.a = 3;
    test.b = 4; // Variabile GLOBALE
    printf("%s %d\n", arg, pthread_self());
    stampa(arg, &test);
    pthread_exit((void *)&test);
}

void *fun3(void *arg){
    myfoo *test3;
    test3=malloc(sizeof(struct foo)); // Variabile allocata dinamicamente
    test3->a = 5;
    test3->b = 6;
    printf("%s %d\n", arg, pthread_self());
    stampa(arg, test3);
    pthread_exit((void *)test3); //c
}
```

---

## Pagina 325

Pthreads

```c
int main(void){
    char st[100];
    pthread_t tid1;
    pthread_t tid2;
    pthread_t tid3;

    myfoo *b; // PUNTATORE alla struttura (non allocata)

    pthread_create(&tid1, NULL, fun1, "Thread 1"); // Locale
    pthread_join(tid1, (void *)&b);
    stampa("Master ", b);

    pthread_create(&tid2, NULL, fun2, "Thread 2"); // Globale
    pthread_join(tid2, (void *)&b);
    stampa("Master ", b);

    pthread_create(&tid3, NULL, fun3, "Thread 3"); // Dinamica
    pthread_join(tid3, (void *)&b);
    stampa("Master ", b);
}
```

---

## Pagina 326

Pthreads

Thread 1: 1077283760
// Locale
Thread 1: a=1 b=2
Master : a=1075156600 b=1077281896

Thread 2: 1077283760
// Globale
Thread 2: a=3 b=4
Master : a=3 b=4

Thread 3: 1077283760
// Dinamica
Thread 3: a=5 b=6
Master : a=5 b=6

---

## Pagina 327

# Windows Multithreaded in C

```c
#include <windows.h>
#include <stdio.h>
DWORD Sum; /* data is shared by the thread(s) */

/* the thread runs in this separate function */
DWORD WINAPI Summation(LPVOID Param)
{
    DWORD Upper = *(DWORD*)Param;
    for (DWORD i = 0; i <= Upper; i++)
        Sum += i;
    return 0;
}

int main(int argc, char *argv[])
{
    DWORD ThreadId;
    HANDLE ThreadHandle;
    int Param;

    if (argc != 2) {
        fprintf(stderr,"An integer parameter is required\n");
        return -1;
    }
    Param = atoi(argv[1]);
    if (Param < 0) {
        fprintf(stderr,"An integer >= 0 is required\n");
        return -1;
    }
}
```

Windows API

DWORD 32-bit unsigned int

LPVOID puntatore void

Funzione di avvio del thread come in Pthread

---

## Pagina 328

Windows Multithreaded in C

```c
/* create the thread */
ThreadHandle = CreateThread(
    NULL, /* default security attributes */
    0, /* default stack size */
    Summation, /* thread function */
    &Param, /* parameter to thread function */
    0, /* default creation flags */
    &ThreadId); /* returns the thread identifier */

if (ThreadHandle != NULL) {
    /* now wait for the thread to finish */
    WaitForSingleObject(ThreadHandle, INFINITE);

    /* close the thread handle */
    CloseHandle(ThreadHandle);

    printf("sum = %d\n", Sum);
}
}
```

Creazione del thread come in Pthread

Attesa del thread come in Pthread

---

## Pagina 329

Threading implicito

- Tecnica sempre più popolare al crescere della complessità dei sistemi multithread
- Creazione e gestione dei thread fatta da compilatori e librerie run-time invece che dai programmatori
- Il programmatore identifica dei task non dei thread

- Tre metodi considerati
  - Thread Pools
  - OpenMP
  - Grand Central Dispatch

---

## Pagina 330

Pool di Thread

□ Si crea un numero di thread in attesa in un pool
□ Richiesto un thread per servizio, se non c’è attesa.

□ Vantaggio:
□ Solitamente più veloce nel servire una richiesta quando il thread esiste già
□ Il numero dei thread per l’applicazione applicazione è limitato dalla dimensione del pool
□ Separa il task da eseguire dal meccanismo per creare il task e permette differenti strategie di esecuzione del task
► i.e. I task possono essere schedulati per avviarsi periodicamente

□ Windows API per supportare i thread pool:
□ Thread function da eseguire con un thread del pool

```cpp
DWORD WINAPI PoolFunction( PVOID Param) {
    /*
     * this function runs as a separate thread.
     */
}
```

---

## Pagina 331

Pool di Thread

DWORD WINAPI PoolFunction(AVOID Param) {
    /* This function runs as a separate thread */
}

□ Un puntatore a PoolFunction() è passato ad una delle funzioni delle API del thread pool e un thread dal pool la esegue.

□ Una di queste funzioni è QueueUserWorkItem che ha 3 parametri
    □ LPTHREAD_START_ROUTINE Function – il puntatore alla funzione da eseguire come thread
    □ PVOID Param – i parametri passati alla funzione
    □ ULONG Flags – flag che indicano come il thread pool deve creare e gestire l’esecuzione del thread.

Esempio di chiamata:
    QueueUserWorkItem(&PoolFunction, NULL, 0);
    che porta uno dei thread del pool ad invocare la PoolFunction()

---

## Pagina 332

OpenMP

- Direttive di compilazione ed API per C, C++, FORTRAN
- Supporto per programmazione parallela in ambienti in shared-memory
- Identifica regioni parallele – blocchi di codice parallelizzabili

#pragma omp parallel

Crea tanti thread quanti sono i core

Esegui il loop in parallelo

#pragma omp parallel for

```c
for(i=0;i<N;i++) {
    c[i] = a[i] + b[i];
}
```

gcc -fopenmp prog.c

Open Multi-Processing

```c
#include <omp.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    /* sequential code */

    #pragma omp parallel
    printf("I am a parallel region.");
}

/* sequential code */

return 0;
}
```

---

## Pagina 333

Problematiche Threading

- Semantica delle chiamate `fork()` ed `exec()`
- Signal handling
  - Sincrono e asincrono
- Cancellazione thread
  - Asincrono o deferred
- Thread-local storage
- Attivazione Scheduler

---

## Pagina 334

Semantica di fork() ed exec()

□ fork() duplica solo il thread chiamante o tutti i thread del processo?
□ Per alcune versioni di UNIX due versioni di fork
□ Spesso duplica solo il thread chiamante

□ exec() funziona nomalmente – sovrascrive il processo in esecuzione inclusi i thread

---

## Pagina 335

Signal Handling

• Un “segnale” e' un interrupt “software”
  – La terminologia corretta e' “exception” mentre “interrupt” e' usata solo per gli interrupt “hardware”

• Consente la comunicazione asincrona tra processi e/o tra device e processo

• Ogni segnale ha un proprio nome
  – Tutti i nomi cominciano per “SIG”
  – Definiti in <signal.h>
  – Associati ad interi positivi

---

## Pagina 336

Signal Handling

Segnali in UNIX notificano eventi ai processi

Un signal handler usato per processare i segnali

1. Generato da evento
2. Mandato ad un processo
3. Signal handler:
   1. default
   2. user-defined

Ogni segnale ha un default handler che il kernel esegue

User-defined signal handler sovrascrive il default
Per single-threaded, segnali mandati al processo

---

## Pagina 337

Segnali (Unix)

• Caratteristiche dei segnali

• Ogni segnale ha un identificatore
  • Identificatori di segnali iniziano con i tre caratteri SIG
  • Es. SIGABRT è il segnale di abort

• Numero segnali: 15-40, a seconda della versione di UNIX
  • POSIX: 18
  • Linux: 38

• I nomi simbolici corrispondono ad un intero positivo

Le costanti dei segnali sono definite internamente in header specifici dell’implementazione (es. bits/signum.h), ma l’interfaccia standard POSIX è <signal.h>

---

## Pagina 338

Segnali (Unix)

Pressione di tasti speciali sul terminale
• Es: Premere il tasto `ctrl-c` genera il segnale `SIGINT`

Eccezioni hardware
• Divisione per 0 (`SIGFPE`)
• Riferimento non valido a memoria (`SIGSEGV`)
• L'interrupt viene generato dall'hardware, e catturato dal kernel; questi invia il segnale al processo in esecuzione

System call kill
• Permette di spedire un segnale ad un altro processo
• Limitazione: uid del processo che esegue `kill` deve essere lo stesso del processo a cui si spedisce il segnale, oppure 0 (root)

---

## Pagina 339

# Segnali (Unix)

| Segnale | Origine | Default | Note |
| :--- | :--- | :--- | :--- |
| SIGINT | Ctrl+C | terminate | interrupt |
| SIGQUIT | Ctrl+\ | terminate + core dump | debug |
| SIGTERM | kill | terminate | terminazione “gentile” |
| SIGKILL* | kill | terminate | NON intercettabile |
| SIGSTOP* | kernel | stop | NON intercettabile |
| SIGTSTP | Ctrl+Z | stop | sospensione |
| SIGCHLD | sistema | ignore | figlio terminato |
| SIGALRM | timer | terminate | alarm |
| SIGSEGV | errore | terminate + core dump | invalid memory |
| SIGUSR1 | user | terminate | custom |

---

## Pagina 340

Segnali (Unix)

• I segnali vengono inviati in modo asincrono.
  – Non e' possibile sapere quando il processo ricevera' un segnale.

• E' possibile indicare al kernel l'azione da intraprendere quando un segnale e' generato per un processo:
  – Ignora: Valida per quasi tutti i segnali tranne SIGKILL e SIGSTOP.
  – “Catch” del segnale: Indicare una procedura da eseguire (signal handler). Ad esempio:
    • SIGCHLD: esegui le operazioni associate alla termiazione di un figlio
    • SIGINT: (CTRL-C) “cancella file temporanei”...
    • Non e' possibile intercettare SIGKILL o SIGSTOP.
  – Default: Esegui l'azione di default.

---

## Pagina 341

Segnali (Unix)

• Un handler (gestore) è una funzione del tipo:

```c
void funzione(int num_segnale) {
    printf("%d", num_segnale);
}
```

Una volta che l'handler termina, si torna al punto in cui il programma era stato interrotto.

---

## Pagina 342

Segnali (Unix)

typedef void (*sighandler_t)(int);

sighandler_t signal(int signum, sighandler_t handler);

• signal(SIGINT, foo) imposta la funzione foo come handler del segnale SIGINT
• si puo' anche richiedere di ignorare il segnale
  – signal(SIGINT, SIG_IGN)
• oppure ritornare alla reazione di default
  – signal(SIGINT, SIG_DFL)

---

## Pagina 343

Segnali (Unix)

int kill(pid_t pid, int sig);

• kill(127, SIGINT) invia il segnale SIGINT al processo il cui pid e' 127
• restituisce 0 in caso di successo e -1 in caso di errore

---

## Pagina 344

Segnali (Unix)

```c
void foo(int num_segnale);
int main(void){

    int n=0;    int buf[100];
    alarm(5);
    signal(SIGALRM,foo);

    while (n<=0){
        printf("Digitare qualcosa:\n");
        alarm(1);
        if ((n=read(STDIN_FILENO,buf,10))<0)
            perror("Read error");
        alarm(0);
    }
}

void foo(int num_segnale) {
    alarm(1);
    printf("Vuoi muoverti a digitare qualcosa ???\n");
}
```

---

## Pagina 345

Signal Handling

Se multi-threaded?

- Invia il segnale al thread a cui si applica
- Invia a tutti i thread del processo
- Invia a specifici thread del processo
- Assegna ad un thread specifico il compito di recevere tutti i segnali del processo

---

## Pagina 346

Signal Handling

int pthread_kill(pthread_t tid, int signo);

• manda il segnale signo al thread specificato da tid
  – se e' impostato un handler, viene eseguito nel thread tid
  – se non e' impostato un handler, e il comportamento di default e' di terminare il processo, vengono comunque terminati tutti i thread

• restituisce 0 se OK, un codice d'errore altrimenti

---

## Pagina 347

Signal Handling

```c
void usr1(int sig) {
  printf("Handler eseguito nel thread %lu\n", (unsigned long)pthread_self());
}

int main() {
  signal(SIGUSR1, usr1);

  pthread_create(&tid1, NULL, fun, "Thread 1");
  pthread_create(&tid2, NULL, fun, "Thread 2");
  pthread_create(&tid3, NULL, fun, "Thread 3");

  sleep(1);

  // invio direttto ai thread
  pthread_kill(tid1, SIGUSR1);
  pthread_kill(tid2, SIGUSR1);
  pthread_kill(tid3, SIGUSR1);

  // maschera SOLO nel main thread
  sigemptyset(&set);
  sigaddset(&set, SIGUSR1);
  sigprocmask(SIG_SETMASK, &set, NULL);

  sleep(1);

  while (i++ < 10) {
    sleep(1);
    kill(pid, SIGUSR1); // consegnato a un thread NON bloccato
  }
}
```

void *fun(void *arg) {
  char *name = (char *)arg;
  while (1) {
    printf("%s attivo\n", name);
    sleep(2);
  }
  return NULL;
}

---

## Pagina 348

Signal Handling

```c
signal(SIGUSR1, usr1);
pthread_create(&tid1, NULL, fun, "Thread 1");
pthread_create(&tid2, NULL, fun, "Thread 2");
pthread_create(&tid3, NULL, fun, "Thread 3");
sleep(1);
pthread_kill(tid1, SIGUSR1);
pthread_kill(tid2, SIGUSR1);
pthread_kill(tid3, SIGUSR1);

sigemptyset(&set); // Configura la maschera SOLO nel master thread
sigaddset(&set, SIGUSR1);
sigprocmask(SIG_SETMASK, &set, NULL);
sleep(1);
while (i++<10){
    sleep(1);
    kill(pid, SIGUSR1); // il segnale e' intercettato da un thread
}
```

Le maschere dei segnali sono sia al livello di processi che thread:
```c
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
int pthread_sigmask(int how, const sigset_t *set, sigset_t *oldset);
```

---

## Pagina 349

Signal Handling

```cpp
void usr1(int sig) {
    printf("Thread id=%ld ricevuto segnale\n", pthread_self());
}
```

Thread id=1077283760 ricevuto segnale
Thread id=1079385008 ricevuto segnale
Thread id=1081486256 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
Thread id=1077283760 ricevuto segnale
```

---

## Pagina 350

Signal Handling

```c
void usr1(int sig) {
  printf("Handler eseguito nel thread %lu\n", (unsigned long)pthread_self());
}

int main() {
  sigset_t set;

  signal(SIGUSR1, usr1);

  // BLOCCO PRIMA DI CREARE I THREAD
  sigemptyset(&set);
  sigaddset(&set, SIGUSR1);
  pthread_sigmask(SIG_BLOCK, &set, NULL);

  pthread_create(&tid1, NULL, fun, "Thread 1");
  pthread_create(&tid2, NULL, fun, "Thread 2");
  pthread_create(&tid3, NULL, fun, "Thread 3");

  while (1) {
    sleep(1);
    printf("Invio SIGUSR1 al processo\n");
    kill(getpid(), SIGUSR1);
  }

  return 0;
}
```

void *fun(void *arg) {
  char *name = (char *)arg;
  while (1) {
    printf("%s attivo\n", name);
    sleep(2);
  }
  return NULL;
}
```

---

## Pagina 351

Signal Handling

```c
int main() {
    sigset_t set;

    signal(SIGUSR1, usr1);

    sigemptyset(&set);
    sigaddset(&set, SIGUSR1);
    pthread_sigmask(SIG_BLOCK, &set, NULL);

    pthread_create(&tid1, NULL, fun, "Thread 1");
    pthread_create(&tid2, NULL, fun, "Thread 2");
    pthread_create(&tid3, NULL, fun, "Thread 3");

    printf("SIGUSR1 bloccato in tutti i thread\n");

    kill(getpid(), SIGUSR1);
    kill(getpid(), SIGUSR1);
    kill(getpid(), SIGUSR1);

    printf("Mandati 3 SIGUSR1: restano pending\n");
    sleep(5);

    printf("Sblocco SIGUSR1 nel main\n");
    pthread_sigmask(SIG_UNBLOCK, &set, NULL);

    while (1) { sleep(1); }

    return 0;
}

void usr1(int sig) {
    printf("Handler eseguito nel thread %lu\n", (unsigned long)pthread_self());
}
```

void *fun(void *arg) {
    char *name = (char *)arg;
    while (1) {
        printf("%s attivo\n", name);
        sleep(2);
    }
    return NULL;
}

Allo sblocco solo il thread principale gestisce, ma una sola volta perché SIGUR1 pending non si accoda

---

## Pagina 352

Signal Handling

Accodamento di segnali

Comportamento dei segnali pending
Quando un segnale è bloccato diventa pending

La gestione dei segnali pending dipende dal tipo di segnale

- **Segnali standard** (es. SIGINT, SIGUSR1)
  - NON accodati
  - Per ogni segnale può esserci al massimo una istanza pending
  - Segnali multipli dello stesso tipo vengono collassati in uno
  - **Esempio:**
    - arrivano 5 SIGUSR1 mentre è bloccato → 1 solo pending
    - allo sblocco → handler eseguito 1 volta

- **Segnali real-time** (SIGRTMIN ... SIGRTMAX)
  - Accodati (FIFO)
  - Ogni invio genera una nuova istanza pending
  - I segnali vengono consegnati tutti e in ordine
  - **Esempio:**
    - arrivano 5 SIGRTMIN → 5 pending
    - allo sblocco → handler eseguito 5 volte

---

## Pagina 353

Cancellazione Thread

- Terminare un thread prima che sia finito
- Il thread da cancellare è il target thread
- Due approcci:
  - Asynchronous cancellation termina il target thread subito
  - Deferred cancellation permette al target thread di controllare periodicamente se deve essere cancellato

- Codice Pthread per creare e cancellare un thread:

```c
pthread_t tid;

/* create the thread */
pthread_create(&tid, 0, worker, NULL);

.....

/* cancel the thread */
pthread_cancel(tid);
```

---

## Pagina 354

Cancellazione Thread

□ La cancellazione effettiva depende dallo stato del thread

| Mode | State | Type |
| :--- | :--- | :--- |
| Off | Disabled | – |
| Deferred | Enabled | Deferred |
| Asynchronous | Enabled | Asynchronous |

□ Se il thread ha la cancellazione disabilitata questa rimane pending finché il thread non la consente

□ Il default è deferred:
  □ Cancellazione avviene solo quando il thread raggiunge un *cancellation point*
    ► Allora *cleanup handler* è invocato

□ Su Linux la cancellazione dei thread gestita con segnali

---

## Pagina 355

Cancellazione Thread

□ Esempi di cancellation points

| Tipo | Esempi |
| :--- | :--- |
| Sleep | sleep, nanosleep |
| I/O | read, write |
| Sync | pthread_cond_wait |
| Rete | recv, accept |
| Manuale | pthread_testcancel |

Se puro calcolo (CPU bound) va inserito:

```cpp
while (1) {
    // lavoro CPU-bound
    pthread_testcancel(); // punto inserito a mano
}
```

---

## Pagina 356

Cancellazione Thread (Posix)

• In ogni istante, un thread può essere cancellabile o non cancellabile
• Quando partono tutti i thread sono cancellabili
• Quando un altro thread chiama pthread_cancel
  – se il thread è cancellabile, viene cancellato
  – se non è cancellabile, la richiesta di cancellazione viene memorizzata, in attesa che il thread diventi cancellabile

---

## Pagina 357

Cancellazione Thread (Posix)

```c
int pthread_setcancelstate(int state, int *oldstate);
```

• imposta la cancellabilità a state e restituisce la vecchia cancellabilità in oldstate

• state e oldstate possono assumere i valori:
  – PTHREAD_CANCEL_ENABLE
  – PTHREAD_CANCEL_DISABLE

• restituisce 0 se OK, un codice d'errore altrimenti

---

## Pagina 358

Comandi per Thread

| Comando | Cosa mostra | Nome ID thread | Note |
| :--- | :--- | :--- | :--- |
| ps -T -p <PID> | thread di un processo | SPID / TID | ogni riga = thread |
| ps -eLf | tutti i thread del sistema | LWP | vista completa |
| ps -L -p <PID> | thread di un processo | LWP | alternativa a -T |
| top -H -p <PID> | thread di un processo live | SPID | molto usato |
| htop -H | thread con UI | TID | più leggibile |
| ls /proc/<PID>/task | thread (livello kernel) | directory = TID | ogni cartella = thread |

---

## Pagina 359

Thread-Specific Data

- Thread-local storage (TLS) o Thread-specific Data (TSD)
  - Nei thread var globali condivise, var locali no
  - Ogni thread può mantenere una sua copia dei dati
  - Utile quando non si controlla direttamente la creazione dei thread (i.e., usando i thread pool)

- Differenza rispetto a variabili locali
  - Variabili locali visibili solo per una singola invocazione di funzione
  - TSD visibile per più invocazioni di funzione

- Simile ai dati static (ma senza race condition)
  - TSD unico per ogni thread

---

## Pagina 360

Thread-Specific Data (Posix)

• Ogni thread possiede un’area di memoria privata, la TSD area, indicizzata da chiavi

• La TSD area contiene associazioni tra le chiavi ed un valore di tipo void*

  – diversi thread possono usare le stesse chiavi ma i valori associati variano di thread in thread
  – inizialmente tutte le chiavi sono associate a NULL

---

## Pagina 361

Thread-Specific Data (Posix)

• associare a una stessa chiave, dati diversi per ciascun thread

processo principale
pthread_key_t chiave; // variabile globale
inizializza la chiave
crea i thread

thread 1
pthread_setspecific(chiave, malloc(...));
...
void *p = pthread_getspecific(chiave)

thread 2
pthread_setspecific(chiave, malloc(...));
...
void *p = pthread_getspecific(chiave)

---

## Pagina 362

Thread-Specific Data (Posix)

• int pthread_key_create(…)
  – per creare una chiave TSD

• int pthread_key_delete(…)
  – per deallocare una chiave TSD

• int pthread_setspecific(…)
  – per associare un certo valore ad una chiave TSD

• void * pthread_getspecific(…)
  – per ottenere il valore associato ad una chiave TSD

---

## Pagina 363

Thread-Specific Data (Posix)

```c
int pthread_key_create(pthread_key_t *key,
void (*destructor)(void *));
```

• crea una chiave per dati privati
• key è l'indirizzo della chiave da inizializzare
• destructor è un puntatore alla funzione distruttore che deve essere chiamata alla terminazione di un thread (pthread_exit())
• restituisce 0 se OK, un codice d'errore altrimenti

---

## Pagina 364

Thread-Specific Data (Posix)

```c
int pthread_setspecific(pthread_key_t *key,
    const void* val);

• associa l'indirizzo val alla chiave key, per il thread chiamante
• restituisce 0 se OK, un codice d'errore altrimenti

void* pthread_getspecific(pthread_key_t *key);

• restituisce l'indirizzo associato alla chiave key nel thread chiamante
  – restituisce NULL se nessun indirizzo è stato associato a key
```

---

## Pagina 365

Thread-Specific Data (Posix)

```c
#include ...
static pthread_key_t thread_log_key; /* tsd key per thread */

void write_to_thread_log (const char* message); //Scrive log
void close_thread_log (void* thread_log); //Chiude file log
void* thread_function (void* args); //Eseguita dai thread

int main() {
    // Crea una chiave da associare al log Thread-Specific
    // Crea 5 thread che facciano il lavoro
    // Aspetta che tutti finiscano
    return 0;
}
...
```

---

## Pagina 366

Thread-Specific Data (Posix)

```cpp
int main() {
    int i;
    pthread_t threads[5];
    // Crea una chiave da associare al puntatore TSD al log file
    pthread_key_create(&thread_log_key, close_thread_log);

    for (i = 0; i < 5; ++i) // thread che faccia il lavoro
        pthread_create(&(threads[i]), NULL, thread_function, NULL);

    for (i = 0; i < 5; ++i) // Aspetta che tutti finiscano
        pthread_join(threads[i], NULL);
    return 0;
}
```

---

## Pagina 367

Thread-Specific Data (Posix)

```cpp
void write_to_thread_log (const char* message) {
    FILE* thread_log = (FILE*)pthread_getspecific(thread_log_key);
    fprintf (thread_log, "%s\n", message);
}

void close_thread_log (void* thread_log) {
    fclose ((FILE*) thread_log);
}

void* thread_function (void* args) {
    char thread_log_filename[20];
    FILE* thread_log;
    sprintf(thread_log_filename,"thread%d.log",(int)pthread_self());

    thread_log = fopen (thread_log_filename, "w");
    /* Associa la struttura FILE TSD a thread_log_key. */
    pthread_setspecific (thread_log_key, thread_log);

    write_to_thread_log ("Thread starting.");
    /* Fai altro lavoro qui... */ return NULL;
}
```

---

## Pagina 368

Esempi in SO

- Linux Threads
- Windows Threads

---

## Pagina 369

Linux si riferisce a **tasks** piuttosto che a **threads**
- Unificando la gestione di processi e thread
- Thread creation è gestita dalla chiamata di sistema **clone()**
- Usata per implementare **pthread_create**
- **clone()** permette ad un child task di condividere l’address space del parent task (processo)
- Flag di controllo:

| flag | meaning |
| :--- | :--- |
| CLONE_FS | File-system information is shared. |
| CLONE_VM | The same memory space is shared. |
| CLONE_SIGHAND | Signal handlers are shared. |
| CLONE_FILES | The set of open files is shared.

Viene comunque usata la chiamata a fork(): do_fork()

Se tutte settate allora clone come thread, se tutte non settate come fork

**struct task_struct** punta alle strutture dati del processo (condivise o uniche) - gestione uniforme

---

## Pagina 370

Thread Linux

□ Esempio di uso del clone()

```cpp
int thread_func(void *arg) {
    printf("Hello from the new thread! Arg: %s\n", (char *)arg);
    return 0;
}

int main() {
    char *child_stack = malloc(1024 * 1024); // Allocazione dello stack
    if (child_stack == NULL) {
        perror("malloc");
        exit(1);
    }

    // Creazione del nuovo thread con clone()
    pid_t pid = clone(thread_func, child_stack + 1024 * 1024, CLONE_VM | CLONE_FS | CLONE_FILES |
        CLONE_SIGHAND | CLONE_THREAD, "Thread Arg");

    if (pid == -1) {
        perror("clone");
        exit(1);
    }

    printf("Thread created with pid: %d\n", pid);
    sleep(1); // Aspetta che il thread finisca
    free(child_stack); // Libera lo stack

    return 0;
}
```

---

## Pagina 371

Windows Threads

Strutture dati del thread includono:

- ETHREAD (executive thread block) – include punt. al processo al quale il thread appartiene, punt. alla routine da dove parte il thread, punt. a KTHREAD nel kernel space
- KTHREAD (kernel thread block) – info di scheduling e sincronizzazione, kernel-mode stack, puntatore a TEB nel user space
- TEB (thread environment block) – thread id, user-mode stack, thread-local storage, nello user space

---

## Pagina 372

Windows Threads Data Structures

ETHREAD
- thread start address
- pointer to parent process

KTHREAD
- scheduling and synchronization information
- kernel stack

TEB
- thread identifier
- user stack
- thread-local storage

kernel space
user space

---

