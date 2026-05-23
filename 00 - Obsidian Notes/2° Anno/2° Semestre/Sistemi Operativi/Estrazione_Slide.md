# Estrazione Contenuti Slide Sistemi Operativi I

## SO1-Lezione1-AA25-26: Introduzione

### Titoli Principali
- **Lezione 1: Introduzione**
- Cos'è un Sistema Operativo?
- Componenti di un Sistema di Calcolo
- Definizione di un Sistema Operativo
- SO come Macchina Estesa
- Nucleo del Sistema Operativo
- Storia Sistemi Operativi

### Concetti Chiave
- **Sistema Operativo**: programma che gestisce le risorse di un calcolatore e fa da intermediario tra l'utente e l'hardware
- **Obiettivi SO**: gestire esecuzione programmi utente, semplificare interazione utente, rendere efficace ed efficiente l'utilizzo
- **Componenti Sistema di Calcolo**: Hardware, Sistema Operativo, Programmi applicativi, Utenti
- **SO come Allocatore di Risorse**: gestisce tutte le risorse del calcolatore e assegna risorse per richieste conflittuali
- **SO come Programma di Controllo**: controlla esecuzione programmi evitando errori e usi impropri
- **SO come Macchina Estesa**: fornisce astrazione e ambiente coerente e uniforme
- **Kernel**: nucleo SO, solo programma con accesso completo all'hardware (modalità privilegiata)
- **Modalità User/Kernel**: User mode per applicazioni, Kernel mode per SO

---

## SO1-Lezione2a-AA25-26: Gestione Risorse

### Titoli Principali
- **Gestione Risorse**
- Gestione Processi
- Gestione Memoria Principale
- Gestione Archiviazone
- Strutture di Memoria
- Gerarchia di Memorie

### Concetti Chiave
- **Processo**: programma in esecuzione (entità attiva), vs programma = entità passiva su disco
- **Processi Single-threaded**: hanno un program counter
- **Processi Multi-threaded**: hanno un program counter per thread
- **Gestione Processi - Meccanismi SO**:
  - Creazione e cancellazione di utenti e processi di sistema
  - Sospensione e resume di processi
  - Sincronizzazione di processi
  - Communicazione tra processi
  - Gestione del deadlock
  
- **System Calls Processi**: `fork()`, `waitpid()`, `execve()`, `exit()`

- **Gestione Memoria**:
  - Tenere traccia di quali parti della memoria sono utilizzate e da quale processo
  - Decidere quali processi/dati spostare dentro/fuori memoria
  - Allocazione e deallocazione dello spazio di memoria

- **Gestione Archiviazione**:
  - Rappresentazione logica e uniforme dell'archiviazione
  - **File**: unità logica di archiviazione
  - Files organizzati gerarchicamente in directory

- **Strutture di Memoria**:
  - **Memoria Principale (RAM)**: accesso diretto CPU, volatile
  - **Memoria Non Volatile**: ROM, PROM, EPROM, EEPROM
  - **Memoria Secondaria**: estensione memoria principale, non-volatile (HDD, SSD)

- **Gerarchia di Memorie**: organizzate per velocità, costo, volatilità

---

## SO1-Lezione2b-AA25-26: Servizi SO

### Titoli Principali
- **Servizi dei SO**
- Interfaccia Utente
- Esecuzione di Programmi
- Operazioni I/O
- Gestione File-system
- Comunicazione
- Rilevamento di Errori
- Panoramica dei Servizi di un SO
- Interfaccia Utente - CLI
- Tipi di Chiamate di Sistema
- Programmi di Sistema

### Concetti Chiave
- **Servizi SO per Utenti e Programmi**:
  - Interfaccia Utente (CLI, GUI, Batch)
  - Esecuzione di Programmi
  - Operazioni I/O
  - Gestione File-system
  - Comunicazione
  - Rilevamento di Errori

- **Servizi SO per Efficienza Sistema**:
  - **Allocazione Risorse**: CPU, memoria principale, file, dispositivi I/O
  - **Contabilità**: tenere traccia utilizzo risorse per utente
  - **Protezione e Sicurezza**: controllare accesso processi/utenti a risorse

- **Interfaccia Utente CLI**: interprete dei comandi consente immissione diretta
- **System Calls**: istruzioni che invocano servizi gestiti dal Kernel
- **Programmi di Sistema**: forniscono ambiente conveniente per sviluppo e esecuzione

---

## SO1-Lezione4-AA25-26: Chiamate di Sistema

### Titoli Principali
- **Tipi di Chiamate di Sistema**
- Gestione Informazione
- Comunicazione
- Protezione
- Controllo dei Processi
- Gestione dei File
- Gestione dei Dispositivi
- Gestione delle Informazioni
- Gestione Protezione
- Standard C Library
- Programmi di Sistema

### Concetti Chiave
- **Tipi di Chiamate**:
  - **Gestione Informazione**: get/set time, system data, process/file/device attributes
  - **Comunicazione**: create/delete communication, send/receive messages, shared-memory, remote devices
  - **Protezione**: controllo accesso, gestione permessi, gestione accessi utenti

- **Controllo Processi**: creazione/arresto, suspend/resume, memoria
- **Gestione File**: create/delete, read/write, open/close, seek
- **Gestione Dispositivi**: richiesta/rilascio, ioctl
- **Gestione Protezione**: chmod(), umask(), chown()

- **System Calls Unix/Linux vs Windows**:
  - **Controllo Processi**: `fork()`, `exit()`, `wait()` (Unix) vs `CreateProcess()`, `ExitProcess()`, `WaitForSingleObject()` (Windows)
  - **Gestione File**: `open()`, `read()`, `write()`, `close()` (Unix) vs `CreateFile()`, `ReadFile()`, `WriteFile()`, `CloseHandle()` (Windows)

---

## SO1-Lezione4-5-6-AA25-26: Processi

### Titoli Principali
- **Lezione 5: Processi**
- Definizione di Processo
- Processo Allocato in Memoria
- Stato di un Processo
- Descrittore di Processo
- Tabella Processi in Linux
- Commutazione tra Processi
- Processi e Thread

### Concetti Chiave
- **Definizione Processo**: programma in esecuzione
  - Entità passiva su disco vs entità attiva
  - Unità di attività computazionale coerente
  - Richiede risorse: CPU, memoria, file, dispositivi I/O

- **Layout di Memoria Processo**:
  - **Sezione Testo**: codice del programma
  - **Sezione Dati**: variabili globali
  - **Stack**: dati temporanei (parametri funzione, indirizzi ritorno, variabili locali)
  - **Heap**: memoria dinamicamente allocata a runtime
  - **BSS** (block started by symbol): dati non inizializzati

- **Stati Processo**:
  - **new**: processo creato
  - **running**: esecuzione istruzioni
  - **waiting**: in attesa evento (es. I/O)
  - **ready**: in attesa assegnazione processore
  - **terminated**: esecuzione terminata

- **Descrittore Processo (PCB - Process Control Block)**:
  - Stato processo
  - IDs processo
  - **Program Counter**: prossima istruzione
  - Registri CPU
  - Scheduling CPU
  - Memoria allocata
  - Contabilità
  - Stato I/O

- **PCB in Linux (task_struct)**:
  - `pid_t pid`: process identifier
  - `long state`: stato processo
  - `struct task_struct *parent`: processo padre
  - `struct list_head children`: processi figli
  - `struct files_struct *files`: file aperti
  - `struct mm_struct *mm`: address space

- **Commutazione Processi**: salvataggio stato in PCB e ripristino da PCB durante switch
- **Thread**: multipli flussi di controllo in stesso processo, condividono risorse ma hanno stato esecutivo diverso

---

## SO1-Lezione3-AA25-26: Servizi SO (approfondimento)

### Titoli Principali
- **Servizi dei SO** (ripezione approfondita)
- Interfaccia Utente
- Esecuzione di Programmi
- Operazioni I/O
- Gestione File-system
- Comunicazione
- Rilevamento di Errori
- Protezione e Sicurezza

### Concetti Chiave
- **Interfaccia Utente**: CLI, GUI, Batch
- **Esecuzione Programmi**: caricamento memoria e esecuzione
- **Operazioni I/O**: SO nasconde complessità dispositivo, interfaccia uniforme
- **Gestione File-system**: read/write file, directory management, permessi
- **Comunicazione**: processi scambiano informazioni
- **Rilevamento Errori**: CPU, memoria, I/O, programmi utente
- **Protezione**: accesso controllato, autenticazione utente
- **Sicurezza**: difesa accessi esterni non autorizzati

---

## SO1-Lezione6-bash-AA25-26: Shell Bash

### Titoli Principali
- **Shell Bash**
- Shell
- Ciclo Esecuzione Shell
- Abilitare WSL in Win
- Variabili di Shell
- Variabili Predefinite
- Shell Interattiva
- Sintassi dei Comandi
- Listing di Processi

### Concetti Chiave
- **Shell**: programma che interpreta linguaggio a linea di comando
  - Gestione variabili
  - Costrutti controllo flusso
  - Modalità interattiva

- **Ciclo Esecuzione Shell**:
  1. Operazioni start-up
  2. Acquisizione comando
  3. Macro espansione
  4. Esecuzione comando
  5. Operazioni terminazione

- **Shell Interattiva**:
  - **Interattiva, non login**: legge `~/.bashrc`
  - **Interattiva, login**: legge `/etc/profile`, `~/.bash_profile`, `~/.bash_login`, `~/.profile`

- **Variabili di Shell Predefinite**:
  - **HOME**: directory home default
  - **PATH**: percorso ricerca eseguibili
  - **PS1**: stringa prompt
  - **USER**: nome utente
  - **HOSTNAME**: nome computer
  - **SHELL**: shell corrente

- **Sintassi Comando**: `comando [argomento ...]`
  - Argomenti: opzioni/flag (-), parametri
  - Separati da spazio

- **Ricerca Comando**: ordinatamente nelle directory elencate in PATH
- **Listing Processi (ps)**:
  - **PID**: Process ID
  - **TTY**: identificativo terminale
  - **TIME**: tempo cumulato utilizzo CPU
  - **CMD**: comando generato processo

---

## SO1-Lezione7-8-AA25-26: Threads & Concorrenza

### Titoli Principali
- **Lezione 7: Threads & Concorrenza**
- Motivazioni
- Processi Single e Multithreaded
- Architettura di Server Multithread
- Benefici
- Multicore Programming
- Concorrenza vs. Parallelismo
- Legge di Amdahl

### Concetti Chiave
- **Motivazioni Thread**:
  - Applicazioni generalmente multithreaded
  - Task multipli: update display, fetch data, spell checking, rete response
  - Creazione processo pesante, thread leggero
  - Kernel generalmente multithreaded

- **Processi Multithreaded**:
  - Unità base utilizzo CPU
  - Caratterizzati da **Thread ID**, **PC**, **Registri**, **Stack**
  - Minima identità task

- **Architettura Server Multithread** (Client-Server):
  - Generazione nuovo thread per ogni client
  - Ogni richiesta client gestita da thread
  - Server gestisce multiple richieste concorrenti

- **Benefici Thread**:
  - **Risposta**: esecuzione continua se parte processo bloccata
  - **Risorse**: thread condividono risorse processo
  - **Economia**: leggero, overhead context switch minore
  - **Scalabilità**: vantaggi architetture multiprocessore

- **Multicore Programming**: utilizzo multipli core per parallelismo
- **Parallelismo di Dati**: sottoinsiemi dati su core multipli, stessa operazione
- **Parallelismo di Task**: thread su core, operazioni particolari diverse

- **Concorrenza vs Parallelismo**:
  - **Concorrenza**: progresso contemporaneo su single-core mediante scheduler
  - **Parallelismo**: esecuzione simultanea su multiple core

- **Legge di Amdahl**: speedup ≤ 1/(S + (1-S)/N)
  - S = porzione seriale
  - N = numero core
  - Limite: speedup → 1/S per N → ∞

---

## SO1-Lezione9-10-11-AA25-26: Scheduling CPU

### Titoli Principali
- **Lezione 8: Scheduling CPU**
- Concetti di Base
- Istogramma dei tempi di CPU-burst
- CPU Scheduler
- Dispatcher
- Criteri di Scheduling
- Scheduling: Criteri di Ottimizzazione
- First-Come, First-Served (FCFS) Scheduling
- FCFS Scheduling

### Concetti Chiave
- **Scheduling CPU**: selezionare processi per assegnazione CPU

- **Cicli CPU-I/O Burst**:
  - Esecuzione processi = CPU burst + I/O burst
  - Distribuzione CPU burst importante per scheduling

- **CPU Scheduler**:
  - **Short-term scheduler**: seleziona tra processi in coda ready
  - Decisioni quando:
    1. running → waiting (I/O)
    2. running → ready (interrupt)
    3. waiting → ready (I/O completo)
    4. Terminazione

- **Scheduling Preemptive vs Non-preemptive**:
  - **Non-preemptive**: processo in esecuzione fino fine o wait
  - **Preemptive**: problema race condition, sezioni critiche

- **Dispatcher**:
  - Trasferisce controllo CPU a processo selezionato
  - **Context switch**, switching user mode, salto istruzione
  - **Latenza dispatch**: tempo necessario

- **Criteri Scheduling**:
  - **Utilizzo CPU**: percentuale CPU utilizzata
  - **Throughput**: processi completati per unità tempo
  - **Turnaround Time**: tempo completamento processo
  - **Waiting Time**: tempo attesa in coda ready
  - **Response Time**: tempo tra richiesta e prima risposta

- **Ottimizzazione**: massimo utilizzo CPU, massimo throughput, minimo turnaround/waiting/response time

- **FCFS (First-Come, First-Served)**:
  - Processi serviti nell'ordine arrivo
  - Non preemptive
  - Semplice ma può avere attese lunghe

---

## SO1-Lezione12-13-AA25-26: Sincronizzazione

### Titoli Principali
- **Lezione: Sincronizzazione**
- Background
- Bounded-Buffer – Produttore-Consumatore
- Bounded-Buffer – Produttore
- Bounded Buffer – Consumatore
- Produttore-Consumatore
- Corsa Critica
- Problema della Sezione Critica

### Concetti Chiave
- **Sincronizzazione Processi**: meccanismi per assicurare esecuzione ordinata di processi cooperanti

- **Accessi Concorrenti Dati Condivisi**: possono causare inconsistenze
  - Richiedono meccanismi sincronizzazione e coordinazione

- **Bounded-Buffer Produttore-Consumatore**:
  - Buffer circolare tra processi in memoria condivisa
  - Indici `in` (prossima free) e `out` (prima full)
  - Buffer pieno: `((in + 1) % BUFFER_SIZE) == out`
  - Buffer vuoto: `in == out`

- **Race Condition (Corsa Critica)**:
  - Operazioni **non atomiche** su variabili condivise
  - Esempio: `counter++` interferisce con `counter--`
  - Problema pervasivo, specialmente su multicore

- **Problema Sezione Critica**:
  - **Sezione critica**: segmento codice dove processo accede variabili comuni
  - Quando un processo in sezione critica, altri non dovrebbero entrare
  - Occorrono meccanismi sincronizzazione

---

## SO1-Lezioni-mem-principale-AA25-26: Memoria Principale

### Titoli Principali
- **Memoria Principale**
- Background
- Hardware
- Protezione: Registri Base e Limite
- Protezione Hardware degli Indirizzi
- Programmi e Processi
- Processamento Multistep di Programma Utente
- Binding di Istruzioni e Dati alla Memoria
- Indirizzi Logici e Fisici

### Concetti Chiave
- **Background Memoria**:
  - Memoria principale e registri = sola memoria accesso diretto CPU
  - Tanti processi devono essere caricati in memoria contemporaneamente
  - Memoria vista come grande array di bytes con indirizzi

- **Hardware Protezione**:
  - Accesso registri: generalmente 1 clock CPU
  - Accesso memoria principale: multipli cicli (memory bus)
  - **Cache**: tra memoria principale e registri CPU

- **Protezione Hardware Memoria**:
  - Necessaria per garantire corretto funzionamento
  - SO non interviene tra CPU e Memoria per non rallentare

- **Registri Base e Limite**:
  - Coppia registri CPU definisce spazio indirizzi logici per processo
  - **Base**: primo indirizzo fisico
  - **Limite**: range
  - CPU verifica ogni accesso in user mode

- **Protezione Hardware Indirizzi**:
  - Controllo access è hardware
  - Se violato: **trap** → fatal error
  - Registri caricabili solo SO in modalità privilegiata

- **Programmi vs Processi**:
  - Programmi su disco: file eseguibili
  - Programma in memoria: CPU accede dati e istruzioni
  - Processo: programma in esecuzione
  - Terminazione: memoria resa disponibile

- **Processamento Multistep**:
  - **Compilazione**: genera codice assoluto/rilocabile
  - **Caricamento**: collegamento finale al caricamento
  - **Esecuzione**: runtime se processo può essere spostato

- **Binding Indirizzi**:
  - **Compile Time**: codice assoluto se locazione nota
  - **Load Time**: codice rilocabile se locazione non nota
  - **Execution Time**: binding ritardato se processo spostabile runtime

- **Indirizzi Logici vs Fisici**:
  - **Separazione centrale** per gestione memoria

---

## SO1-Lezioni-mem-virtuale-AA25-26: Memoria Virtuale

### Titoli Principali
- **Memoria Virtuale**
- Background
- Memoria Virtuale più Grande della Memoria Fisica
- Spazio degli Indirizzi Virtuali
- Shared Library usando Memoria Virtuale
- Demand Paging
- Concetti di Base

### Concetti Chiave
- **Memoria Virtuale**: separazione memoria logica dalla memoria fisica
  - Non tutto programma caricato per esecuzione
  - Solo parte necessaria in memoria
  - Spazio indirizzi logici > spazio indirizzi fisici

- **Vantaggi**:
  - Programmi non vincolati da memoria fisica
  - Meno memoria a runtime → più programmi concorrenti
  - Miglior utilizzo CPU e throughput
  - Meno I/O necessario
  - Programmi utente più veloci

- **Implementazione**:
  - **Demand Paging**
  - **Demand Segmentation**

- **Spazio Indirizzi Virtuali**:
  - Vista logica su come processo contenuto in memoria
  - Spazio inizia da indirizzo (es. 0)
  - Indirizzi contigui
  - Memoria fisica organizzata in **page frame**
  - **MMU** (Memory Management Unit) mappa indirizzo logico su fisico

- **Organizzazione Spazio Indirizzi**:
  - **Stack**: inizia da indirizzo logico massimo, cresce "in giù"
  - **Heap**: cresce "in su"
  - Spazio indirizzi **sparso** con buchi
  - Librerie sistema condivise
  - Memoria condivisa mediante page read-write mapping

- **Shared Library**:
  - Librerie sistema condivise nello spazio indirizzi virtuali
  - Shared memory mediante page read-write mapping
  - Pagine condivise durante `fork()` per accelerare creazione processo

- **Demand Paging**:
  - Portare pagina in memoria **solo quando necessaria**
  - Vs caricamento intero processo a loadtime
  - Minore I/O, elimina non necessario
  - Minor memoria richiesta
  - Risposta più rapida
  - Più utenti contemporaneamente

- **Lazy Swapper**:
  - Non swappa pagina se non richiesta
  - **Pager**: swapper che carica singole pagine

- **Page Fault**:
  - Se pagina richiesta non residente in memoria → **trap**
  - SO deve trovare e caricare pagina da storage

---

## SO1-Lezioni-file-system1-AA25-26: File System

### Titoli Principali
- **File System**
- File System e Memoria di Massa
- Concetto di File
- Attributi del File
- Operazioni File
- Open File
- Strutture del File System
- Tipo di File, Nomi, Estensioni

### Concetti Chiave
- **File System**:
  - Fornisce metodi efficienti accesso file
  - Organizza informazione in termini di file
  - Risiede permanentemente in memoria di massa
  - Accesso sequenziale e diretto ai blocchi fisici
  - Dimensioni blocchi: 512 - 4096 Byte (tipicamente 4096 per NVM)

- **Concetto di File**:
  - **Unità logica** di immagazzinamento in memoria secondaria
  - Vista uniforme informazione memorizzata
  - Spazio contiguo indirizzi logici
  - Diversi tipi dati: numerico, caratteri, binari, programmi

- **Attributi File**:
  - **Name**: denominazione per utente
  - **Identifier**: tag unico nel file system
  - **Type**: per sistemi supportano tipi diversi
  - **Location**: pointer locazione su device
  - **Size**: dimensione corrente
  - **Protection**: chi può read/write/execute
  - **Time, date, user ID**: protection, security, monitoring
  - **inode** (Unix/Linux): indice file con metadata su disco

- **Operazioni File**:
  - **Create**: creazione file
  - **Open**: cerca file, controlla permessi, ritorna riferimento
  - **Close**: chiude file
  - **Write**: mantiene write pointer
  - **Read**: mantiene read pointer
  - **Reposition/Seek**: posizionamento
  - **Delete**: cancellazione file
  - **Truncate**: cancella contenuto, mantiene attributi

- **Open File**:
  - Per evitare ricerca ogni volta file system
  - Mantiene info file aperto in memoria principale
  - **Open-File Table**: SO traccia tutti file aperti

- **Tabelle File Aperti**:
  - **Per-processo**: File descriptor (indice nella tabella system)
  - **Di Sistema**: descrive apertura file, posizione read/write
  - **File Control Block (FCB)**: metadata file, locazione su disco

- **Strutture File System in Memoria (Linux)**:
  - Process table
  - Open file table
  - Active i-node
  - File status flag
  - Current offset
  - File Control Block

---

## SO1-Lezioni-mem-massa-AA25-26: Memoria di Massa

### Titoli Principali
- **Memoria di Massa**
- Obiettivi
- Overview della Struttura di Memoria di Massa
- Hard Disk
- Hard Disk Performance
- Dispositivi NVM
- Solid-State Disks (SSDs)
- Algoritmi del Controllore delle NAND Flash

### Concetti Chiave
- **Memoria di Massa**:
  - Struttura fisica dispositivo memoria secondaria
  - Performance dispositivi memoria di massa
  - Algoritmi disk scheduling
  - RAID structures
  - Stable-storage implementation

- **Tipi Dispositivi**:
  - **Hard Disk Drives (HDDs)**: meccanici
  - **NonVolatile Memory (NVM)**: elettrici

- **Struttura Hard Disk**:
  - Dischi piatti (0.85" - 14", comunemente 3.5", 2.5", 1.8")
  - Superfici coperte materiale magnetico
  - Testina read-write
  - Braccio muove testine
  - Piatti divisi in **tracce**
  - Tracce divise in **settori** (512 - 4096 bytes)
  - Testine si muovono su **cilindri** (insieme tracce)

- **Performance Hard Disk**:
  - **Capacità**: GB - TB
  - **Motore**: 60-250 rotazioni/secondo (5400-15000 RPM)
  - **Transfer Rate**: 6 Gb/sec teorico, ~1 Gb/sec effective
  - **Seek Time**: 3-12 ms (9 ms comune)
  - **Rotational Latency**: dipende spindle speed
  - **Average Latency** = ½ latency

- **Access Latency (Average Access Time)**:
  - average seek time + average latency
  - Fast disk: 3ms + 2ms = 5ms
  - Slow disk: 9ms + 5.56ms = 14.56ms

- **Average I/O Time**:
  - average access time + (quantità transferire / velocità transfer) + overhead controller
  - Esempio 4KB su disco 7200 RPM: 9.301ms

- **Dispositivi NVM (Solid-State Disks)**:
  - Memoria nonvolatile come hard drive
  - **Non meccanici** (nessun seek time/rotational latency)
  - Basati su memoria flash (NAND flash)
  - Più affidabili di HDD
  - Più costosi per MB
  - Vita più breve
  - Minore capacità HDD ma più veloce
  - Capacità cresce rapidamente, prezzo cala

- **Caratteristiche SSD**:
  - Nessuna parte mobile
  - Accesso casuale uniforme
  - Tempi accesso brevi
  - Bus connessione a volte lento
  - Si stanno affermando per sostituire HDD

---

## Riepilogo Concetti Chiave Trasversali

### Processi e Sincronizzazione
- **Processo**: programma in esecuzione con risorse dedicate
- **Processo vs Thread**: thread più leggero, condivide risorse processo
- **Stato Processo**: new, running, waiting, ready, terminated
- **Sincronizzazione**: meccanismi per esecuzione ordinata processi cooperanti
- **Race Condition**: accessi concorrenti a dati condivisi causano inconsistenze
- **Sezione Critica**: codice accede variabili comuni, mutua esclusione necessaria

### Memoria
- **Memoria Principale**: accesso diretto CPU, volatile
- **Memoria Secondaria**: non-volatile (HDD, SSD)
- **Memoria Virtuale**: separazione memoria logica da fisica
- **Indirizzo Logico vs Fisico**: MMU mappa indirizzi logici su fisici
- **Demand Paging**: carica pagina solo quando necessaria
- **Protezione**: registri base/limite, controllo access hardware

### I/O e File System
- **File System**: organizza informazione in file in memoria secondaria
- **File**: unità logica archiviazione con attributi
- **inode** (Unix/Linux): metadata file su disco
- **Open-File Table**: SO traccia file aperti
- **Hard Disk vs SSD**: meccanico vs elettronico

### Shell e Comandi
- **Shell**: interprete linguaggio a linea di comando
- **System Calls**: interfaccia tra programmi e kernel
- **Variabili Ambiente**: HOME, PATH, PS1, USER, HOSTNAME, SHELL
- **Process Status (ps)**: PID, TTY, TIME, CMD

