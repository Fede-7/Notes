## Pagina 1

Gestione Risorse

Gestione dei processi
Gestione della memoria
Gestione dei file
Gestione della memoria di massa
Gestione della cache
Gestione dell’I/O

---

## Pagina 2

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

## Pagina 3

Gestione Processi

Il Sistema Operativo fornisce diversi meccanismi per la gestione dei processi, in particolare per:

- Creazione e cancellazione di utenti e processi di sistema
- Sospensione e resume di processi
- Sincronizzazione di processi
- Communicazione tra processi
- Gestione del deadlock

Process tree. Process A crea due processi figli, B e C. Il processo B crea 3 processi figli, D, E e F.

---

## Pagina 4

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

## Pagina 5

Gestione Memoria Principale

- Per eseguire un programma, istruzioni e dati devono essere caricati in memoria principale

- Attività di gestione della memoria:
  - Tenere traccia di quali parti della memoria sono attualmente utilizzate e da quale processo
  - Decidere quali processi (o parti di essi) e dati spostare dentro e fuori alla/dalla memoria
  - Allocazione e deallocazione dello spazio di memoria secondo necessità

---

## Pagina 6

Gestione Archiviazone

- Il sistema operativo fornisce una rappresentazione logica e uniforme dell'archiviazione delle informazioni
  - Astrazione di proprietà fisiche
  - Unità logica di archiviazione è il file

- Gestione del File-System
  - Files tipicamente organizzati gerarchicamente in directory (multilivello)

---

## Pagina 7

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

## Pagina 8

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

## Pagina 9

Gerarchia di Memorie

Memorie organizzate in gerarchie

- Velocità
- Costo
- Volatilità

Figura 1.6 Scala gerarchica dei sistemi di memorizzazione.

---

## Pagina 10

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

## Pagina 11

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

## Pagina 12

Sistemi I/O

- Il Sistema Operativo deve nascondere all’utente le specificità hardware dei dispositivi fornendo un’interfaccia uniforme

- Sottosistemi I/O responsabili di
  - Gestione della memoria di I/O incluso buffering (memorizzazione temporanea dei dati durante il trasferimento), memorizzazione nella cache, spooling (sovrapposizione dell’accesso a periferica di più job)
  - Interfaccia generica per i dispositivi
  - Driver per dispositivi hardware specifici

---

