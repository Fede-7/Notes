# Estrazione Appunti Completi: Indice Sezioni e Livelli di Dettaglio

**File di Origine**: `Appunti_completi.md`  
**Data Creazione**: 23 Maggio 2026  
**Organizzazione**: Gerarchia di sezioni con tre livelli di profondità

---

## PARTE I: FONDAMENTI

### 1. Introduzione e Architettura del Sistema Operativo

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 1.1 | Definizione e Obiettivi Fondamentali | Definizione SO, obiettivi (gestione risorse, astrazione, controllo conflitti, efficienza) | **Basic** |
| 1.2 | Struttura a Strati e Dual Mode | Architettura SO, dual mode (Kernel/User), modalità privilegiate, bit hardware | **Approfondito** |
| 1.3 | Evoluzione Storica dei Sistemi Operativi | Storia SO: I-V generazione, tecnologie, caratteristiche per era (Batch, Time-sharing, Personal Computer, Mobile/Cloud) | **Medio** |
| 1.4 | Meccanismo delle Interruzioni | Tipi interruzioni (Hardware, Eccezione, Trap), vettore interruzioni, sincronizzazione | **Approfondito** |
| 1.5 | La Gerarchia API → ABI → System Call | Stack API/ABI, system call POSIX, trasferimento controllo kernel, parametri registri/memoria | **Approfondito** |

**Argomento Generale**: Concetti base SO, architettura hardware/software, meccanismi di controllo

---

### 2. Processi, Thread e Comunicazione

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 2.1 | Il Processo: Definizione e Ciclo di Vita | Processo vs programma, ciclo vita stati (Creato→Pronto→In Esecuzione→In Attesa→Terminato), transizioni stato | **Basic** |
| 2.2 | Operazioni Fondamentali: fork, exec, wait | Primitive POSIX fork/exec/wait, semantica, zombie process, adoption by init | **Approfondito** |
| 2.3 | Thread: Concetti e Modelli di Mapping | Thread definition, kernel vs user threads, modelli (Many-to-One, One-to-One, Many-to-Many), LWP | **Approfondito** |
| 2.4 | Concorrenza vs Parallelismo e Legge di Amdahl | Concorrenza (interleaving single-core), parallelismo (true simultaneous multi-core), formula Amdahl, limite seriale | **Medio** |
| 2.5 | Comunicazione tra Processi (IPC) | Shared Memory vs Message Passing, Pipe anonime, FIFO, socket, synchronization | **Medio** |

**Argomento Generale**: Processi e thread, gestione esecuzione concorrente, comunicazione interprocesso

---

### 3. Scheduling della CPU

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 3.1 | Criteri e Componenti | Short-term Scheduler, Dispatcher, metriche (Throughput, Turnaround Time, Waiting Time, Response Time) | **Basic** |
| 3.2 | Algoritmi Tradizionali | FCFS, SJF, SRTF, Round Robin, stima CPU burst (media esponenziale), confronto prestazioni | **Approfondito** |
| 3.3 | Scheduling con Priorità e Code Multiple | Priorità fissa/dinamica, starvation, aging, Multi-Level Feedback Queue, aging mechanism | **Approfondito** |
| 3.4 | Scheduling Real-Time | Soft/Hard Real-Time, Rate Monotonic (RMS), Earliest Deadline First (EDF), optimalità EDF | **Approfondito** |
| 3.5 | Scheduling nei Sistemi Moderni (Linux) | CFS (Completely Fair Scheduler), virtual runtime, red-black tree, EEVDF (Linux 6.6+) | **Approfondito** |

**Argomento Generale**: Algoritmi scheduling CPU, criteri valutazione, implementazioni SO moderni

---

### 4. Sincronizzazione e Deadlock

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 4.1 | Il Problema della Sezione Critica | Entry-CS-Exit-Remainder, criteri (mutua esclusione, progresso, bounded waiting) | **Basic** |
| 4.2 | Supporto Hardware e Primitive | Memory barriers, Test-and-Set (TAS), Compare-and-Swap (CAS), operazioni atomiche | **Approfondito** |
| 4.3 | Mutex, Semafori e Monitor | Mutex lock, semafori binari/contatori, monitor (tipo dato astratto), strutture sincronizzazione | **Approfondito** |
| 4.4 | Variabili di Condizione | pthread_cond_wait/signal, while loop pattern, false awakening, race condition | **Approfondito** |
| 4.5 | Deadlock e Priority Inversion | Condizioni Coffman (mutua esclusione, hold-and-wait, non-prelazione, ciclo), priority inheritance | **Approfondito** |

**Argomento Generale**: Sincronizzazione processi/thread, sezione critica, deadlock

---

## PARTE II: GESTIONE MEMORIA

### 5. Gestione della Memoria Principale

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 5.1 | Indirizzi Logici vs Fisici e MMU | Separazione memoria logica/fisica, MMU (Memory Management Unit), traduzione indirizzi, user mode trap | **Basic** |
| 5.2 | Paginazione (Paging) | Memoria frame/pagine, eliminazione frammentazione esterna, page table, traduzione <p,d> | **Basic** |
| 5.3 | TLB e Effective Access Time (EAT) | Translation Lookaside Buffer (cache hardware), hit/miss rate, formula EAT, importanza TLB | **Approfondito** |
| 5.4 | Memoria Virtuale e Demand Paging | Demand paging, page fault gestione, backing store, Copy-on-Write (COW), lazy swapper | **Approfondito** |
| 5.5 | Algoritmi di Sostituzione e Thrashing | FIFO, OPT, LRU (stack algorithm), Clock algorithm, anomalia Belady, thrashing | **Approfondito** |

**Argomento Generale**: Gestione memoria principale, paginazione, memoria virtuale

---

### 6. Gestione Avanzata della Memoria e TLB

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 6.1 | Translation Lookaside Buffer (TLB) | Cache associativa hardware, hit/miss, principio località, EAT formula, importanza prestazioni | **Approfondito** |
| 6.2 | Protezione e Bit di Stato nella Page Table | Valid/Invalid, Present/Absent, Read/Write/Execute, Dirty, Reference, Permission bits | **Approfondito** |
| 6.3 | Strutture delle Page Table per Spazi Grandi | Page table gerarchica (multi-level), Inverted Page Table (IPT), tradeoff memoria vs accesso | **Approfondito** |
| 6.4 | Swapping e Demand Paging | Swapping storico (processi interi), demand paging (pagine singole), dirty bit rilevanza | **Approfondito** |
| 6.5 | Esercizi Proposti | Calcoli EAT, bit page table, frammentazione, allocazione frame | **Medio** |

**Argomento Generale**: Ottimizzazione memoria, TLB, protezione, strutture gerarchiche

---

### 7. Architetture di Memoria e Demand Paging

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 7.1 | Segmentazione e Paging nelle Architetture Intel | Intel 32-bit (segmentation+paging), Intel 64-bit (4 livelli, huge pages), CR3 register | **Approfondito** |
| 7.2 | Memoria Virtuale e Demand Paging | Virtual memory concept, page fault gestione, backing store, riavvio istruzione, latenza | **Medio** |
| 7.3 | Copy-on-Write (COW) e Fork | COW meccanismo, fork ottimizzazione, shared pages read-only, write-trigger copia | **Approfondito** |
| 7.4 | Esercizi Proposti | Page fault analysis, COW benefits, bit page table calcoli, istruzioni per traduzione | **Medio** |

**Argomento Generale**: Architetture hardware memoria, implementazione demand paging, ottimizzazioni

---

### 8. Algoritmi di Sostituzione di Pagina e Thrashing

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 8.1 | FIFO | First-In First-Out pagine, anomalia Belady, vittimizzazione | **Basic** |
| 8.1.1 | Optimal (OPT) | Teorico optimal, mai implementabile, benchmark reference | **Basic** |
| 8.1.2 | LRU (Least Recently Used) | Stack algorithm, nessuna anomalia Belady, implementazione costosa | **Approfondito** |
| 8.1.3 | Algoritmo Clock (Second Chance) | Reference bit, lancetta circolare, enhanced clock (dirty bit consideration) | **Approfondito** |
| 8.2 | Allocazione dei Frame | Locale vs globale, isolation vs efficiency, multiprogramming degree | **Medio** |
| 8.2.1 | Locale vs Globale | Local allocation (isolation, underutilization), global (efficiency, interference) | **Medio** |
| 8.2.2 | Thrashing (Satellamento) | Excessive page faults, cause (multiprogrammazione elevata), sintomi (CPU idle), soluzione | **Approfondito** |
| 8.3 | Esercizi Proposti | Simulazione algoritmi, confronto FIFO/LRU, anomalia Belady, thrashing prevention | **Medio** |

**Argomento Generale**: Sostituzione pagine, strategie allocazione frame, thrashing

---

### 9. Thrashing, Working Set e Memoria del Kernel

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 9.1 | Il Modello del Working Set | Working set W(t,Δ), pagine attive intervallo, monitoraggio accessi, locality estimation | **Approfondito** |
| 9.2 | Gestione della Memoria del Kernel | Kernel memory specifici requisiti, piccole dimensioni, contiguità fisica (DMA) | **Medio** |
| 9.2.1 | Buddy System | Potenza di 2 allocazioni, splitting/merging, frammentazione interna | **Approfondito** |
| 9.2.2 | Slab Allocator | Cache/Slab/Oggetti, pre-inizializzazione, elimina frammentazione piccoli oggetti | **Approfondito** |
| 9.3 | Ottimizzazioni: Compressione e Pre-paging | Compressione RAM vs swap (mobile), pre-paging (locality spaziale) | **Medio** |
| 9.4 | Esercizi Proposti | Buddy vs Slab, compressione tradeoff, calcoli inode allocazione | **Medio** |

**Argomento Generale**: Modello working set, allocatori kernel, ottimizzazioni memoria

---

## PARTE III: STORAGE E I/O

### 10. Sistemi di I/O e Storage

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 10.1 | Architettura a Strati e Classificazione | Strati SO I/O (System Call → Device Independent → Driver → Hardware), Block/Character/Network devices | **Basic** |
| 10.2 | Dischi Magnetici (HDD) vs SSD | Accesso meccanico vs elettronico, seek time, latency, wear leveling, scheduling | **Medio** |
| 10.3 | Affidabilità e RAID | RAID 0-6 tecniche, striping, mirroring, parità distribuita, tolleranza guasti | **Approfondito** |

**Argomento Generale**: Sottosistema I/O, dispositivi storage, architetture RAID

---

### 11. Implementazioni SO e Storage Secondario

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 11.1 | Implementazione della Sostituzione nei SO Moderni | Linux (Active/Inactive lists), Windows (Working Set Trimmer), Solaris (Two-Hand Clock) | **Approfondito** |
| 11.2 | Memoria Secondaria: HDD vs SSD | Confronto caratteristiche, HDD seek latency problema, SSD P/E cycles limite | **Medio** |
| 11.3 | Algoritmi di Disk Scheduling (Per HDD) | FCFS, SSTF, SCAN, C-SCAN, LOOK/C-LOOK, seek time minimizzazione | **Approfondito** |
| 11.4 | Rilevamento e Correzione Errori (ECC) | Parity bit, Hamming code, SEC-DED, formule calcolo bit ridondanza | **Approfondito** |
| 11.5 | Esercizi Proposti | Disk scheduling calcoli, FTL ruolo, ECC bit calcoli | **Medio** |

**Argomento Generale**: Implementazioni SO replacement policies, storage devices, disk scheduling, error correction

---

### 12. Bootstrap, Swap Space e Architetture RAID

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 12.1 | Il Processo di Bootstrap | BIOS+MBR legacy (512 byte, <2.2 TB), UEFI+GPT moderno (64-bit, backup) | **Approfondito** |
| 12.1.1 | Architettura Legacy: BIOS + MBR | BIOS POST, MBR boot code, partition table, limiti | **Medio** |
| 12.1.2 | Architettura Moderna: UEFI + GPT | UEFI graphics/networking, GPT 64-bit, ESP partition, FAT32 bootloader | **Approfondito** |
| 12.2 | Gestione dello Swap Space | Backing store disco, raw partition vs file, anonymous memory, prefetch eseguibile | **Medio** |
| 12.3 | Architetture RAID | Comparazione RAID 0-6, tolleranza, performance, capacità, min dischi | **Approfondito** |
| 12.4 | Esercizi Proposti | Boot process comparison, swap space management, RAID level selection | **Medio** |

**Argomento Generale**: Bootstrap processo, swap space, RAID architectures

---

## PARTE IV: FILE SYSTEM

### 13. Strutture del File System e Directory

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 13.1 | Architettura Logica del File System | FCB/Inode, metadati file, tipo/permessi/timestamp, puntatori blocchi | **Basic** |
| 13.2 | Gestione dei File Aperti: Le Tre Tabelle | Per-Process FD table, System-wide Open File Table, Inode Table (in-memory) | **Approfondito** |
| 13.3 | Directory e Link | Hard link (stesso inode), Symbolic link (file percorso), cicli possibili, cross-filesystem | **Approfondito** |
| 13.4 | Affidabilità: Journaling | Write-intent log, commit, checkpoint, recovery (replay/undo), crash consistency | **Approfondito** |
| 13.5 | Esercizi Proposti | Open() flow, file locking (flock vs fcntl), hard vs soft link analisi | **Medio** |

**Argomento Generale**: Architettura file system, metadati, link, journaling

---

### 14. I/O di Basso Livello e System Call POSIX

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 14.1 | System Call Fondamentali | open() flags (O_CREAT, O_TRUNC, O_APPEND), read/write, lseek, close | **Basic** |
| 14.2 | Condivisione di File Descriptor (Fork) | open() prima/dopo fork(), offset condiviso, dipendenze, lseek necessità | **Approfondito** |
| 14.3 | Sparse Files (Creazione di "Buchi") | lseek oltre fine file, non allocazione blocchi zeri, dimensione logica vs fisica | **Approfondito** |
| 14.4 | Esercizi Proposti | File I/O snippets C, offset behavior, sparse file creation e verification | **Medio** |

**Argomento Generale**: System call POSIX I/O, file descriptor, sparse files

---

### 15. Allocazione dei File e Caching Unificato

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 15.1 | Metodi di Allocazione dei File | Contigua, concatenata, indicizzata, tradeoff spazio/prestazioni | **Approfondito** |
| 15.2 | Implementazioni Moderne: Unix Inode vs NTFS MFT | Unix inode (diretti/indiretti), NTFS MFT (estents), bilanciamento | **Approfondito** |
| 15.3 | Caching e Performance: Unified Page Cache | Double caching problema storico, unified page cache soluzione, coerenza dati | **Approfondito** |
| 15.3.1 | Read-Ahead e Pre-paging | Rilevamento accessi sequenziali, precaricamento blocchi successivi, nascondere latenza | **Medio** |
| 15.4 | Esercizi Proposti | FAT allocazione, Ext4 extents, double caching issue | **Medio** |

**Argomento Generale**: Allocazione file, cache unificata, ottimizzazioni I/O

---

### 16. Consistenza del File System e Sottosistema I/O

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 16.1 | Architettura a Strati del File System | Logical FS, File Organization, Basic FS, Device Drivers, VFS astrazione | **Approfondito** |
| 16.2 | Sottosistema di Input/Output (I/O) | Block/Character/Network devices, driver, interrupt asincrono | **Medio** |
| 16.2.1 | Classificazione dei Dispositivi | Block (randomico), Character (sequenziale), Network | **Basic** |
| 16.2.2 | Device Drivers e Interrupt | Ring 0 kernel mode, driver vulnerabilità, asincrono I/O, hardware interrupt | **Approfondito** |
| 16.2.3 | Terminali e Line Discipline | TTY, editing riga, caratteri controllo, segnali (SIGINT) | **Medio** |
| 16.3 | Esercizi Proposti | VFS ruolo, Block vs Character device syscall, TTY line discipline | **Medio** |

**Argomento Generale**: Consistenza file system, VFS, sottosistema I/O, device drivers

---

## PARTE V: TÓPICI AVANZATI

### 17. Gestione della Memoria del Kernel

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 17.1 | Principio di Separazione: Policy vs Meccanismo | Meccanismo (strumento tecnico), policy (decisione), separazione importanza | **Approfondito** |
| 17.2 | Paradigmi di Progettazione del Kernel | Monolitico (velocità, bug risk), Microkernel (modularità, overhead), Modulare (flessibilità), Ibrido | **Approfondito** |
| 17.3 | Virtualizzazione | Tipo 1 (bare metal), Tipo 2 (hosted), isolamento SO guest, ipervisor overhead | **Approfondito** |

**Argomento Generale**: Architettura kernel, paradigmi progettazione, virtualizzazione

---

### 18. Gestione dei Segnali e Cancellazione dei Thread

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 18.1 | Segnali in Contesto Multi-thread | Segnali ordinari vs real-time, accodamento, blocco maschere, ereditarietà | **Approfondito** |
| 18.2 | Cancellazione dei Thread | Deferred (safe, cancellation point), asynchronous (rischioso, race condition) | **Approfondito** |

**Argomento Generale**: Segnali multi-thread, cancellazione thread, ereditarietà maschere

---

### 19. Gestione Avanzata della Memoria del Kernel

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 19.1 | Buddy System | Allocazione potenza 2, split/merge, frammentazione interna | **Approfondito** |
| 19.2 | Slab Allocator | Cache/Slab/Objects, pre-inizializzazione, elimina frammentazione piccoli | **Approfondito** |
| 19.3 | Compressione della Memoria | Trade-off CPU vs latenza I/O, compressione in RAM preferita swap per mobile | **Medio** |

**Argomento Generale**: Allocatori kernel avanzati, compressione memoria

---

### 20. Architetture di Memoria Hardware (Intel e ARM)

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 20.1 | Intel x86: Segmentazione e Paging | Segmentazione GDT/LDT, paging 32-bit (PAE), paging 64-bit (huge pages) | **Approfondito** |
| 20.2 | Architettura ARM v8 | Pagine 4/16/64 KB, TLB separate L1 (I/D), cache strutture page table | **Approfondito** |

**Argomento Generale**: Architetture hardware memoria, x86 vs ARM, implementazioni pratiche

---

### 21. Caching e Ottimizzazione delle Prestazioni I/O

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 21.1 | Il Problema del Double Caching | Buffer cache vs page cache storico, duplicazione dati, incoerenza | **Approfondito** |
| 21.2 | Unified Page Cache | Fusione cache, mmap e read/write coerenza, singola page cache | **Approfondito** |
| 21.3 | Read-Ahead e Pre-paging | Rilevamento sequenziale, precaricamento anticipato, nascondere latenza disco | **Medio** |

**Argomento Generale**: Cache unificata, ottimizzazioni I/O, read-ahead

---

### 22. Laboratorio di Sistemi: Programmazione POSIX

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 22.1 | Ambiente di Sviluppo e Compilazione | GCC, preprocessore, compilatore, linker, flag ottimizzazione | **Medio** |
| 22.2 | Gestione dei Processi e I/O di Basso Livello | open flags, lseek, sparse files, FD condivisione | **Medio** |
| 22.3 | Programmazione Concorrente (Thread e Sincronizzazione) | pthread_create, pthread_join, mutex, condition variables, while loop pattern | **Approfondito** |
| 22.4 | Comunicazione tra Processi (IPC) | Pipe, shm_open, mmap, sincronizzazione esterna | **Medio** |

**Argomento Generale**: Programmazione POSIX pratica, thread, IPC

---

### 23. Analisi degli Algoritmi Critici

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 23.1 | Soluzione di Peterson (Mutua Esclusione Software) | Algoritmo teorico due processi, flag/turn, memory barriers | **Approfondito** |
| 23.2 | Problema dei 5 Filosofi | Stati (THINKING/HUNGRY/EATING), prevenzione deadlock, condition variables | **Approfondito** |
| 23.3 | Algoritmo Clock (Sostituzione Pagine) | Bit R, lancetta, second chance, enhanced clock (R+M) | **Approfondito** |

**Argomento Generale**: Algoritmi sincronizzazione, sostituzione pagine, problemi classici

---

### 24. Sottosistema I/O e Dispositivi

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 24.1 | Classificazione dei Dispositivi | Block devices, character devices, network devices, operazioni specifiche | **Basic** |
| 24.2 | Line Discipline | Terminali TTY, editing riga, caratteri controllo, signal mapping | **Medio** |

**Argomento Generale**: Dispositivi I/O, classificazione, line discipline

---

### 25. Manuale di Calcolo per l'Esame

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 25.1 | Metriche di Scheduling | Turnaround time, waiting time, response time, calcoli | **Basic** |
| 25.2 | Gestione della Memoria | Bit page table, indirizzo logico/fisico, EAT formula | **Medio** |
| 25.3 | Affidabilità e Errori | MTTF array, codice Hamming, bit ridondanza calcoli | **Medio** |

**Argomento Generale**: Formule e calcoli per esame, metriche, examples

---

### 26. Glossario Rapido dei Termini Tecnici

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 26 | Glossario | Context Switch, Deadlock, Page Fault, Thrashing, VFS, Working Set, Copy-on-Write | **Basic** |

**Argomento Generale**: Definizioni rapide concetti tecnici

---

## PARTE VI: CAPITOLI AGGIUNTIVI STRUTTURATI

### 27. Gestione della Memoria e Paging

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 27.1 | Background: Accesso alla Memoria e Protezione | Ciclo esecuzione CPU, memoria array bytes, protezione accesso, hardware support | **Basic** |
| 27.2 | Il Problema del Binding degli Indirizzi | Compile time, load time, runtime binding, MMU traduzione trasparente | **Approfondito** |
| 27.2.1 | Momenti del Binding | Compile/Load/Runtime, code generation (assoluto/rilocabile), loader | **Approfondito** |
| 27.2.2 | Indirizzi Logici vs Fisici e la MMU | Indirizzi virtuali/fisici, traduzione real-time, trasparenza processo | **Approfondito** |
| 27.3 | Allocazione Contigua e Frammentazione | Strategie (First/Best/Worst Fit), frammentazione esterna/interna, limite | **Approfondito** |
| 27.3.1 | Strategie di Allocazione | First/Best/Worst fit algoritmi | **Medio** |
| 27.3.2 | Tipi di Frammentazione | Esterna vs interna, conseguenze, perdita memoria | **Medio** |
| 27.4 | La Paginazione (Paging) | Frame/pagine, page table, traduzione <p,d>, eliminazione fragmentazione esterna | **Approfondito** |
| 27.4.1 | Definizione | Memoria divisa frame/pagine, vantaggi | **Basic** |
| 27.4.2 | Traduzione degli Indirizzi | Numero pagina, offset, page table lookup, indirizzo fisico | **Approfondito** |
| 27.5 | Esercizi Proposti | Calcoli page table, bits, frammentazione, allocazione | **Medio** |

**Argomento Generale**: Memoria principale, binding indirizzi, paginazione

---

### 28. Gestione Avanzata della Memoria e TLB

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 28.1 | Translation Lookaside Buffer (TLB) | Cache hardware associativa, hit/miss, locality, EAT formula rilevanza | **Approfondito** |
| 28.1.1 | Funzionamento e Principio di Località | TLB lookup, cache hit/miss, principle of locality utilizzo | **Approfondito** |
| 28.1.2 | Calcolo dell'Effective Access Time (EAT) | Formula EAT, variabili α/ε/T_M, example calcolo | **Approfondito** |
| 28.2 | Protezione e Bit di Stato nella Page Table | Valid/Invalid, Present/Absent, R/W/X, Dirty, Reference bits funzione | **Approfondito** |
| 28.3 | Strutture delle Page Table per Spazi Grandi | Gerarchica multi-level, Inverted Page Table, memoria vs accesso tradeoff | **Approfondito** |
| 28.4 | Swapping e Demand Paging | Storico swapping intero processo, moderno demand paging, dirty bit ruolo | **Approfondito** |
| 28.5 | Esercizi Proposti | EAT calcoli, bit page table, strutture gerarchiche | **Medio** |

**Argomento Generale**: TLB, protezione memoria, strutture gerarchiche, swapping

---

### 29. Architetture di Memoria e Demand Paging

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 29.1 | Segmentazione e Paging nelle Architetture Intel | Intel 32-bit (segmentation+paging), Intel 64-bit (4 livelli, huge pages) | **Approfondito** |
| 29.1.1 | Intel a 32-bit (x86) | Segmentation unit, linear address, paging 2 livelli, CR3 | **Approfondito** |
| 29.1.2 | Intel a 64-bit (x86-64) | 48-bit virtual address, 4 livelli, huge pages (2MB, 1GB) | **Approfondito** |
| 29.2 | Memoria Virtuale e Demand Paging | Virtual memory concept, page fault gestione, backing store, riavvio istruzione | **Approfondito** |
| 29.2.1 | Gestione del Page Fault | Trap verificazione, legalità accesso, backing store ricerca, frame allocazione | **Approfondito** |
| 29.3 | Copy-on-Write (COW) e Fork | Shared read-only initial, write-fault copy, fork() optimization exec() | **Approfondito** |
| 29.4 | Esercizi Proposti | Page fault flow, COW benefits, bit calcoli, instruction translation | **Medio** |

**Argomento Generale**: Architetture hardware Intel/ARM, demand paging, COW optimization

---

### 30. Algoritmi di Sostituzione di Pagina e Thrashing

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 30.1 | Algoritmi di Sostituzione di Pagina | Scelta vittima quando frame esauriti | **Basic** |
| 30.1.1 | FIFO | Primo caricato primo uscito, anomalia Belady | **Basic** |
| 30.1.2 | Optimal (OPT) | Mai usato futuro (preveggenza), algoritmo benchmark teorico | **Basic** |
| 30.1.3 | LRU (Least Recently Used) | Non usato da più tempo passato, stack algorithm, costoso puro | **Approfondito** |
| 30.1.4 | Algoritmo Clock (Second Chance) | Bit riferimento R, lancetta, resetta R se 1, enhanced clock M consideration | **Approfondito** |
| 30.2 | Allocazione dei Frame | Locale (isolation), globale (efficiency), multiprogramming degree | **Medio** |
| 30.2.1 | Locale vs Globale | Local vs global allocation tradeoff | **Medio** |
| 30.2.2 | Thrashing (Satellamento) | CPU swap overhead, cause (multiprogramming elevata), soluzione | **Approfondito** |
| 30.3 | Esercizi Proposti | Simulazione FIFO/LRU, anomalia Belady, thrashing analysis | **Medio** |

**Argomento Generale**: Algoritmi sostituzione pagine, allocazione frame, thrashing prevention

---

### 31. Thrashing, Working Set e Memoria del Kernel

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 31.1 | Il Modello del Working Set | W(t,Δ) pagine intervallo tempo, monitoraggio accessi, locality estimation | **Approfondito** |
| 31.2 | Gestione della Memoria del Kernel | Requisiti speciali (piccolo, contiguo per DMA), allocatori dual | **Medio** |
| 31.2.1 | Buddy System | Potenza 2, split/merge, frammentazione interna, page-level gestione | **Approfondito** |
| 31.2.2 | Slab Allocator | Cache/Slab/Objects, pre-init, kernel object specifici (PCB, inode) | **Approfondito** |
| 31.3 | Ottimizzazioni: Compressione e Pre-paging | Compressione RAM vs swap, pre-paging locality spaziale | **Medio** |
| 31.4 | Esercizi Proposti | Buddy vs Slab, compressione tradeoff, inode allocazione calcoli | **Medio** |

**Argomento Generale**: Working set model, kernel allocators, memory optimizations

---

### 32. Bootstrap, Swap Space e Architetture RAID

| # | Titolo Sezione | Argomento | Livello |
|---|---|---|---|
| 32.1 | Il Processo di Bootstrap | BIOS+MBR legacy (<2.2TB), UEFI+GPT moderno (64-bit backup) | **Approfondito** |
| 32.1.1 | Architettura Legacy: BIOS + MBR | BIOS POST, MBR 512 byte, boot code, partition table limiti | **Medio** |
| 32.1.2 | Architettura Moderna: UEFI + GPT | UEFI firmware, GPT 64-bit, ESP partition FAT32 bootloader | **Approfondito** |
| 32.2 | Gestione dello Swap Space | Backing store disco, raw partition vs file, anonymous memory storage | **Medio** |
| 32.3 | Architetture RAID | Confronto 0-6, tolleranza guasti, performance, capacità, minimum disks | **Approfondito** |
| 32.4 | Esercizi Proposti | Boot process comparison, swap space utilization, RAID selection | **Medio** |

**Argomento Generale**: Bootstrap process, swap management, RAID architectures

---

## STATISTICHE GENERALI

### Distribuzione Livello di Dettaglio
- **Basic**: 15 sezioni (~18%)
- **Medio**: 28 sezioni (~34%)
- **Approfondito**: 40 sezioni (~48%)

### Categorie Principali
1. **Processi e Scheduling**: 8 sezioni
2. **Memoria**: 12 sezioni
3. **Sincronizzazione**: 5 sezioni
4. **I/O e Storage**: 8 sezioni
5. **File System**: 6 sezioni
6. **Kernel Avanzato**: 6 sezioni
7. **Laboratorio/Esercizi**: 3 sezioni
8. **Architetture Hardware**: 4 sezioni
9. **Ottimizzazioni**: 4 sezioni
10. **Algoritmi Critici**: 3 sezioni

### Sezioni Approfondite (Approfondito)
- 1.2, 1.4, 1.5, 2.2, 2.3, 3.2, 3.3, 3.4, 3.5, 4.2, 4.3, 4.4, 4.5
- 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.3, 6.4
- 7.1, 7.3, 8.1.2, 8.1.3, 8.2.2, 9.1, 9.2.1, 9.2.2
- 10.3, 11.1, 11.3, 11.4, 12.1, 12.3
- 13.2, 13.3, 13.4, 14.2, 14.3, 15.1, 15.2, 15.3
- 16.1, 16.2.2, 17.1, 17.2, 18.1, 18.2, 19.1, 19.2
- 20.1, 20.2, 21.1, 21.2, 22.3, 23.1, 23.2, 23.3
- 27.2, 27.2.1, 27.2.2, 27.3, 27.4, 27.4.2
- 28.1, 28.1.1, 28.1.2, 28.2, 28.3, 28.4
- 29.1, 29.1.1, 29.1.2, 29.2, 29.2.1, 29.3
- 30.1.3, 30.1.4, 30.2.2, 31.1, 31.2.1, 31.2.2
- 32.1.2, 32.3

