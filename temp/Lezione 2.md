Ecco il contenuto delle slide convertito in un documento Markdown professionale, ottimizzato per la lettura su dispositivi tablet.

***

# Gestione Risorse

*   Gestione dei processi
*   Gestione della memoria
*   Gestione dei file
*   Gestione della memoria di massa
*   Gestione della cache
*   Gestione dell’I/O

***

# Gestione Processi

**Definizione di Processo**

Un **processo** è un programma in esecuzione. 
Il programma è un'entità passiva, mentre il processo è un'entità attiva.

**Risorse Necessarie**

Un processo ha bisogno di risorse per svolgere un task:
*   CPU, memoria, I/O, files
*   Dati di inizializzazione

**Terminazione**

Alla terminazione di un processo occorre il rilascio e il recupero delle risorse.

**Threading**

*   I processi **single-threaded** hanno un **program counter** (locazione prossima istruzione da eseguire).
*   Le istruzioni sono sequenziali, una alla volta, fino a completamento.
*   I processi **multi-threaded** hanno un program counter per ogni singolo thread.

**Concorrenza**

Tipicamente i sistemi hanno in esecuzione molti processi, per più utenti, in esecuzione concorrente su una o più CPU.

***

# Meccanismi di Gestione dei Processi

Il Sistema Operativo fornisce diversi meccanismi per la gestione dei processi, in particolare per:

*   Creazione e cancellazione di utenti e processi di sistema
*   Sospensione e resume di processi
*   Sincronizzazione di processi
*   Comunicazione tra processi
*   Gestione del **deadlock**

**Process Tree**

Esempio di struttura ad albero:
Il processo A crea due processi figli, B e C. 
Il processo B crea 3 processi figli, D, E e F.

***

# Process Management (Chiamate di Sistema)

Il Sistema Operativo fornisce diversi meccanismi per la gestione dei processi, in particolare per:

*   Creazione e cancellazione di utenti e processi di sistema
*   Sospensione e resume di processi
*   Sincronizzazione di processi
*   Comunicazione tra processi
*   Gestione del deadlock

**Comandi di gestione processi:**

```monospace
pid = fork() 
# Create a child process identical to the parent

pid = waitpid(pid, &statloc, options) 
# Wait for a child to terminate

s = execve(name, argv, environp) 
# Replace a process’ core image

exit(status) 
# Terminate process execution and return status
```

***

# Gestione Memoria Principale

Per eseguire un programma, le **istruzioni** e i **dati** devono essere caricati in memoria principale.

**Attività di gestione della memoria:**

*   Tenere traccia di quali parti della memoria sono attualmente utilizzate e da quale processo.
*   Decidere quali processi (o parti di essi) e dati spostare dentro e fuori alla/dalla memoria.
*   Allocazione e deallocazione dello spazio di memoria secondo necessità.

***

# Gestione dell'Archiviazione

Il sistema operativo fornisce una **rappresentazione logica e uniforme** dell'archiviazione delle informazioni.

*   Astrazione di proprietà fisiche.
*   L'unità logica di archiviazione è il **file**.

**Gestione del File-System**

*   Files tipicamente organizzati gerarchicamente in directory (multilivello).

***

# Dettagli sulla Gestione del File-System

Il sistema operativo fornisce una rappresentazione logica e uniforme dell'archiviazione delle informazioni.

*   Astrazione di proprietà fisiche.
*   L'unità logica di archiviazione è il file.

**Gestione del File-System (Approfondimento)**

*   File tipicamente organizzati gerarchicamente in directory.
*   Controllo dell'accesso per determinare chi può accedere a cosa.

**Il Sistema Operativo gestisce:**

*   Creazione e cancellazione file e directory.
*   Primitive per modifica di file e directory.
*   Mapping di file nella memoria secondaria.
*   Backup di file su memoria non-volatile.

***

# Strutture di Memoria

**Memoria Principale**

*   Memoria che la CPU può accedere direttamente.
*   **Random access memory (RAM)**.
*   Tipicamente volatile.

**Memoria non volatile**

*   Esempi: ROM, PROM, EPROM, EEPROM (Eletronicamente cancellabile e programmabile).

**Memoria Secondaria**

*   Estensione della memoria principale che fornisce capacità di memorizzazione non-volatile.
*   **Hard-disk drive (hdd)**:
    *   Disco logicamente diviso in tracce suddivise in settori.
*   **Disco a stato solido (ssd)**:
    *   Più veloce.
    *   Accesso casuale uniforme.
    *   Tempi di accesso brevi.

***

# Gerarchia di Memorie

Le memorie sono organizzate in gerarchie basate su tre criteri principali:

*   Velocità
*   Costo
*   Volatilità

*Figura 1.6 Scala gerarchica dei sistemi di memorizzazione.*

***

# Varietà di Archiviazione dei Dati

**Livello 1: Registri**
*   Dimensione tipica: < 1 KB
*   Tecnologia: Memoria dedicata con porte multiple (CMOS)
*   Tempo d’accesso (ns): 0,25 – 0,5
*   Ampiezza di banda (MB/s): 20.000 – 100.000
*   Gestito da: Hardware
*   Supportato da cache: Memoria centrale

**Livello 2: Cache**
*   Dimensione tipica: < 16 MB
*   Tecnologia: CMOS SRAM (on-chip o off-chip)
*   Tempo d’accesso (ns): 0,5 – 25
*   Ampiezza di banda (MB/s): 5000 – 10.000
*   Gestito da: Hardware
*   Supportato da cache: Disco

**Livello 3: Memoria Centrale**
*   Dimensione tipica: < 64 GB
*   Tecnologia: CMOS DRAM
*   Tempo d’accesso (ns): 80 – 250
*   Ampiezza di banda (MB/s): 1000 – 5000
*   Gestito da: Sistema operativo
*   Supportato da cache: Disco

**Livello 4: Disco a Stato Solido**
*   Dimensione tipica: < 1 TB
*   Tecnologia: Memoria flash
*   Tempo d’accesso (ns): 25.000 - 50.000
*   Ampiezza di banda (MB/s): 500
*   Gestito da: Sistema operativo
*   Supportato da cache: Disco o nastro

**Livello 5: Disco Magnetico**
*   Dimensione tipica: < 10 TB
*   Tecnologia: Disco magnetico
*   Tempo d’accesso (ns): 5.000.000
*   Ampiezza di banda (MB/s): 20 – 150
*   Gestito da: Sistema operativo
*   Supportato da cache: Disco o nastro

*Figura 1.14 Caratteristiche di varie forme di archiviazione dei dati.*

***

# Caching

**Principi Generali**

*   Principio valido a diversi livelli (hardware, SO, software).
*   Informazione temporaneamente copiata da una memoria più lenta a una più veloce.

*Figura 1.15 Migrazione di un intero A da un disco a un registro.*

**Logica di Accesso**

Le memorie più veloci (cache) sono considerate per prime cercando un dato:
*   Se il dato è presente, viene immediatamente utilizzato (veloce).
*   Se il dato non è presente, viene copiato in cache ed usato.

**Problematiche della memoria cached**

*   Gestione della cache.
*   Dimensione della cache e politica di replicazione.

***

# Sistemi I/O

Il Sistema Operativo deve **nascondere all’utente** le specificità hardware dei dispositivi fornendo un’interfaccia uniforme.

**Sottosistemi I/O responsabili di:**

*   Gestione della memoria di I/O incluso:
    *   **Buffering** (memorizzazione temporanea dei dati durante il trasferimento).
    *   Memorizzazione nella cache.
    *   **Spooling** (sovrapposizione dell’accesso a periferica di più job).
*   Interfaccia generica per i dispositivi.
*   Driver per dispositivi hardware specifici.