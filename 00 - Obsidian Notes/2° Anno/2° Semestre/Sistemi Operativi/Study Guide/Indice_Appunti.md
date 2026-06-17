# Indice - Sistemi Operativi I (AA 2025-2026)

**Basato su: 13 Lezioni Frontali + Slide Ufficiali**  
**Ordine Didattico: da Generale a Specifico**

---

## Parte I - Introduzione ai Sistemi Operativi

### Capitolo 1 - Fondamenti (Lezione 1)
1.1 Cos'è un Sistema Operativo?  
1.2 Componenti di un Sistema di Calcolo  
1.3 Obiettivi e Funzioni del Sistema Operativo  
1.4 Il Sistema Operativo come Allocatore di Risorse  
1.5 Il Sistema Operativo come Programma di Controllo  
1.6 Il Sistema Operativo come Macchina Estesa  
1.7 Il Kernel: Nucleo del Sistema Operativo  
1.8 Modalità Utente e Modalità Kernel  
1.9 Cenni di Storia dei Sistemi Operativi

---

## Parte II - Servizi e Interfacce del SO

### Capitolo 2 - Servizi del Sistema Operativo (Lezioni 2b, 3)
2.1 Panoramica dei Servizi  
2.2 Servizi Orientati all'Utente  
    2.2.1 Interfaccia Utente (CLI, GUI, Batch)  
    2.2.2 Esecuzione di Programmi  
    2.2.3 Operazioni di Input/Output  
    2.2.4 Gestione del File System  
    2.2.5 Comunicazione tra Processi  
    2.2.6 Rilevamento degli Errori  
2.3 Servizi Orientati all'Efficienza del Sistema  
    2.3.1 Allocazione delle Risorse  
    2.3.2 Contabilità delle Risorse  
    2.3.3 Protezione e Sicurezza

### Capitolo 3 - Chiamate di Sistema (Lezione 4)
3.1 Introduzione alle System Calls  
3.2 Tipi di Chiamate di Sistema  
3.3 Controllo dei Processi  
3.4 Gestione dei File  
3.5 Gestione dei Dispositivi  
3.6 Gestione delle Informazioni  
3.7 Comunicazione  
3.8 Gestione della Protezione  
3.9 Standard C Library  
3.10 Confronto: Unix/Linux vs Windows  
3.11 Programmi di Sistema

### Capitolo 4 - La Shell Bash (Lezione 6-bash)
4.1 Introduzione alla Shell  
4.2 Il Ciclo di Esecuzione della Shell  
4.3 Modalità Interattiva  
4.4 Variabili di Shell  
4.5 Variabili Predefinite (HOME, PATH, PS1, USER, HOSTNAME, SHELL)  
4.6 Sintassi dei Comandi  
4.7 Ricerca ed Esecuzione dei Comandi  
4.8 Listing dei Processi (comando ps)  
4.9 Abilitazione WSL in Windows

---

## Parte III - Processi e Gestione di Base

### Capitolo 5 - Gestione dei Processi (Lezioni 4-5-6)
5.1 Definizione di Processo  
5.2 Processi Single-threaded e Multi-threaded  
5.3 Layout di Memoria di un Processo  
    5.3.1 Sezione Testo  
    5.3.2 Sezione Dati  
    5.3.3 Stack  
    5.3.4 Heap  
    5.3.5 BSS (Block Started by Symbol)  
5.4 Stati di un Processo  
5.5 Il Descrittore di Processo (PCB)  
5.6 La Struttura task_struct in Linux  
5.7 Commutazione tra Processi (Context Switch)  
5.8 System Calls per la Gestione dei Processi  
    5.8.1 fork()  
    5.8.2 waitpid()  
    5.8.3 execve()  
    5.8.4 exit()

### Capitolo 6 - Gerarchia di Memoria e Archiviazione (Lezione 2a)
6.1 Memoria Principale (RAM)  
6.2 Memoria Non Volatile (ROM, PROM, EPROM, EEPROM)  
6.3 Memoria Secondaria  
6.4 Gerarchia delle Memorie  
6.5 Allocazione e Deallocazione della Memoria  
6.6 Decisioni di Spostamento Processi/Dati  
6.7 Rappresentazione Logica dell'Archiviazione  
6.8 Il Concetto di File  
6.9 Organizzazione Gerarchica in Directory  
6.10 Gestione dello Spazio di Archiviazione

---

## Parte IV - Thread e Concorrenza

### Capitolo 7 - Thread (Lezione 7-8)
7.1 Motivazioni per l'Utilizzo dei Thread  
7.2 Processi Single-threaded vs Multithreaded  
7.3 Caratteristiche dei Thread  
7.4 Architettura Client-Server Multithread  
7.5 Benefici dei Thread  
    7.5.1 Risposta  
    7.5.2 Condivisione delle Risorse  
    7.5.3 Economia  
    7.5.4 Scalabilità

### Capitolo 8 - Programmazione Multicore (Lezione 7-8)
8.1 Introduzione al Multicore Programming  
8.2 Parallelismo di Dati  
8.3 Parallelismo di Task  
8.4 Concorrenza vs Parallelismo  
8.5 La Legge di Amdahl

---

## Parte V - Sincronizzazione dei Processi

### Capitolo 9 - Sincronizzazione dei Processi (Lezione 12-13)
9.1 Background e Motivazioni  
9.2 Accessi Concorrenti a Dati Condivisi  
9.3 Race Condition (Corsa Critica)  
9.4 Operazioni Non Atomiche  
9.5 Il Problema della Sezione Critica  
    9.5.1 Criteri di Soluzione (Mutua Esclusione, Progresso, Bounded Waiting)  
    9.5.2 Soluzione Software: Peterson Algorithm  
9.6 Memory Barriers e Istruzioni Atomiche  
    9.6.1 Test-and-Set (TAS)  
    9.6.2 Compare-and-Swap (CAS)  
9.7 Mutex Lock  
9.8 Semafori  
    9.8.1 Semafori Binari  
    9.8.2 Semafori Contatori  
    9.8.3 Wait/Signal Operations  
9.9 Monitor  
    9.9.1 Definizione e Struttura  
    9.9.2 Variabili di Condizione  
    9.9.3 Wait/Signal/Broadcast  
9.10 Deadlock  
    9.10.1 Condizioni di Coffman  
    9.10.2 Prevenzione e Rilevamento  
9.11 Priority Inversion e Priority Inheritance  
9.12 Problemi Classici  
    9.12.1 Produttore-Consumatore (Bounded-Buffer)  
    9.12.2 Lettori-Scrittori (Readers-Writers)  
    9.12.3 Problema dei 5 Filosofi

---

## Parte VI - Scheduling della CPU

### Capitolo 10 - Concetti di Base dello Scheduling (Lezione 9-10-11)
10.1 Cicli CPU-burst e I/O-burst  
10.2 Istogramma dei Tempi di CPU-burst  
10.3 Il CPU Scheduler (Short-term Scheduler)  
10.4 Scheduling Preemptive vs Non-preemptive  
10.5 Il Dispatcher  
10.6 Latenza di Dispatch

### Capitolo 11 - Criteri e Algoritmi di Scheduling (Lezione 9-10-11)
11.1 Criteri di Scheduling  
    11.1.1 Utilizzo della CPU  
    11.1.2 Throughput  
    11.1.3 Turnaround Time  
    11.1.4 Waiting Time  
    11.1.5 Response Time  
11.2 Criteri di Ottimizzazione  
11.3 Algoritmo FCFS (First-Come, First-Served)

---

## Parte VII - Gestione della Memoria

### Capitolo 12 - Memoria Principale (Lezione mem-principale)
12.1 Background  
12.2 Hardware di Memoria  
12.3 Cache e Gerarchia di Memoria  
12.4 Protezione Hardware della Memoria  
    12.4.1 Registri Base e Limite  
    12.4.2 Controllo degli Accessi Hardware  
12.5 Binding di Istruzioni e Dati alla Memoria  
    12.5.1 Compile Time Binding  
    12.5.2 Load Time Binding  
    12.5.3 Execution Time Binding  
12.6 Indirizzi Logici vs Indirizzi Fisici  
    12.6.1 Separazione Logica/Fisica  
    12.6.2 Memory Management Unit (MMU)  
12.7 Allocazione Contigua  
    12.7.1 First Fit, Best Fit, Worst Fit  
    12.7.2 Frammentazione Esterna  
    12.7.3 Frammentazione Interna  
12.8 La Paginazione (Paging)  
    12.8.1 Concetto di Frame e Pagine  
    12.8.2 Page Table  
    12.8.3 Traduzione Indirizzi <p, d>  
    12.8.4 Bit di Stato nella Page Table (Valid, Dirty, Reference, R/W/X)  
12.9 Translation Lookaside Buffer (TLB)  
    12.9.1 Cache Hardware Associativa  
    12.9.2 Hit e Miss  
    12.9.3 Effective Access Time (EAT)  
12.10 Strutture Page Table per Spazi Grandi  
    12.10.1 Page Table Gerarchica (Multi-level)  
    12.10.2 Inverted Page Table (IPT)

### Capitolo 13 - Memoria Virtuale e Demand Paging (Lezione mem-virtuale)
13.1 Introduzione alla Memoria Virtuale  
13.2 Vantaggi della Memoria Virtuale  
13.3 Spazio degli Indirizzi Virtuali  
    13.3.1 Organizzazione Stack e Heap  
    13.3.2 Spazi Sparsi con Buchi  
13.4 La Memory Management Unit (MMU)  
13.5 Demand Paging  
    13.5.1 Concetti di Base  
    13.5.2 Lazy Swapper  
    13.5.3 Page Fault e Gestione  
    13.5.4 Implementazione: Demand Paging e Demand Segmentation  
13.6 Copy-on-Write (COW)  
    13.6.1 Meccanismo e Vantaggi  
    13.6.2 Applicazione in fork()  
13.7 Shared Library e Memoria Condivisa

---

## Parte VIII - File System e Memoria di Massa

### Capitolo 14 - File System (Lezione file-system)
14.1 File System e Memoria di Massa  
14.2 Il Concetto di File  
14.3 Attributi del File  
14.4 L'inode in Unix/Linux  
    14.4.1 Struttura Inode  
    14.4.2 Puntatori Diretti e Indiretti  
    14.4.3 Calcolo Max File Size  
14.5 Operazioni sui File  
    14.5.1 Create  
    14.5.2 Open e Close  
    14.5.3 Read e Write  
    14.5.4 Reposition/Seek  
    14.5.5 Delete e Truncate  
14.6 Gestione dei File Aperti  
    14.6.1 File Descriptor (FD)  
    14.6.2 Open-File Table (3 livelli)  
    14.6.3 Per-Process FD Table  
    14.6.4 System-wide Open File Table  
    14.6.5 In-Memory Inode Table  
    14.6.6 File Control Block (FCB)  
14.7 Strutture del File System in Memoria (Linux)  
14.8 Tipi di File, Nomi ed Estensioni

### Capitolo 15 - Memoria di Massa (Lezione mem-massa)
15.1 Obiettivi e Overview  
15.2 Struttura della Memoria di Massa  
15.3 Hard Disk Drives (HDD)  
    15.3.1 Struttura Fisica (Piatti, Tracce, Settori, Cilindri)  
    15.3.2 Performance degli HDD  
    15.3.3 Seek Time, Rotational Latency, Transfer Rate  
    15.3.4 Average Access Time e Average I/O Time  
15.4 Dispositivi NonVolatile Memory (NVM)  
15.5 Solid-State Disks (SSD)  
    15.5.1 Caratteristiche degli SSD  
    15.5.2 Memoria NAND Flash  
    15.5.3 Vantaggi e Svantaggi rispetto agli HDD  
    15.5.4 Algoritmi del Controllore NAND Flash (Cenni)

---

## Appendici

### Appendice A - Riepilogo Concetti Chiave
A.1 Processi e Sincronizzazione  
A.2 Gestione della Memoria  
A.3 I/O e File System  
A.4 Shell e Comandi di Sistema

### Appendice B - Tabelle di Riferimento Rapido
B.1 System Calls Unix/Linux vs Windows  
B.2 Stati dei Processi  
B.3 Campi del PCB  
B.4 Variabili di Ambiente Shell
