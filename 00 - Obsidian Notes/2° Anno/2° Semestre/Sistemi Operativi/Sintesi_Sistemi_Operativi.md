---
title: Sintesi Sistemi Operativi
corso: Sistemi Operativi
---

# Sintesi Sistemi Operativi

Questa sintesi raccoglie i concetti fondamentali del corso di Sistemi Operativi, strutturati per moduli, con un focus su definizioni, algoritmi e meccanismi architetturali.

---

## Modulo 1: Introduzione e Architettura del Sistema Operativo

### 1.1 Definizioni e Concetti Base
Il **Sistema Operativo (SO)** è un software che agisce da intermediario tra l'utente e l'hardware, fungendo da:
- **Resource Allocator:** Gestisce equamente le risorse (CPU, memoria, I/O).
- **Control Program:** Controlla l'esecuzione dei programmi utente per prevenire errori e usi impropri.

> [!abstract] Definizione di Kernel
> Il **kernel** è il programma principale del sistema operativo, costantemente in esecuzione in memoria. Gestisce i processi, la memoria e l'hardware.

### 1.2 Architettura Hardware e Dual-Mode
Per garantire la protezione, l'hardware offre il supporto al **Dual-Mode Operation** tramite un *mode bit*:
1.  **User Mode (Mode bit = 1):** Esecuzione normale dei programmi utente. Istruzioni privilegiate disabilitate.
2.  **Kernel Mode (Mode bit = 0):** Pieno controllo dell'hardware. Accesso a istruzioni privilegiate (es. gestione I/O, modifica registri di base/limite).

Il passaggio da User a Kernel Mode avviene tramite **Interrupts** o **Traps/Exceptions** (es. divisione per zero, system call).

### 1.3 System Call, API e ABI
Le **System Call** (chiamate di sistema) sono l'interfaccia tra un processo utente e i servizi del kernel.
- Generano un'interruzione software (Trap) che cambia il contesto in Kernel Mode.
- I parametri vengono passati tramite registri, blocchi di memoria o stack.

> [!info] API vs ABI
> - **API (Application Programming Interface):** Interfaccia a livello sorgente (es. `printf` in C). Più portabile.
> - **ABI (Application Binary Interface):** Interfaccia a livello binario tra l'eseguibile e l'architettura hardware/SO (es. registri usati per i parametri delle syscall).

### 1.4 Strutture del Kernel
I SO possono essere organizzati secondo diversi paradigmi:
- **Monolitico (Linux):** Tutti i servizi (scheduler, FS, driver) sono nello stesso spazio di indirizzamento in kernel mode. Molto veloce ma difficile da estendere e meno resiliente (un bug in un driver fa crashare l'intero kernel).
- **Microkernel (Mach, QNX):** Solo le funzioni essenziali (IPC, memory management base, scheduling base) sono in kernel mode. Servizi come FS e driver sono processi utente. Più sicuro e scalabile, ma con alto overhead per il passaggio di messaggi (IPC).
- **Modulare (Linux moderno):** Il kernel è monolitico per performance, ma supporta **Loadable Kernel Modules (LKM)**, permettendo di caricare e scaricare componenti a runtime senza ricompilare o riavviare.

### 1.5 Compilazione e Toolchain C
La generazione di un eseguibile in C richiede quattro fasi:
1.  **Preprocessing (`cpp`):** Risolve le direttive `#include`, `#define`. Output: file sorgente espanso (`.i`).
2.  **Compilation (`gcc -S`):** Traduce il C in Assembly (`.s`).
3.  **Assembly (`as`):** Traduce l'Assembly in codice macchina rilocabile (Object file, `.o`), formato tipicamente **ELF**.
4.  **Linking (`ld`):** Combina più file oggetto e librerie (statiche/dinamiche) in un singolo eseguibile **ELF**.

> [!tip] Formato ELF (Executable and Linkable Format)
> Contiene intestazioni (Header), sezioni per codice (Text), dati inizializzati (Data), dati non inizializzati (BSS) e la Symbol Table per il linking.

---

## Modulo 2: Gestione di Processi e Thread

### 2.1 Il Concetto di Processo
Un processo è un programma in esecuzione. In memoria, il layout di un processo è diviso in:
- **Text:** Codice eseguibile.
- **Data & BSS:** Variabili globali e statiche (inizializzate e non).
- **Heap:** Memoria allocata dinamicamente a runtime (cresce verso l'alto).
- **Stack:** Dati temporanei come parametri di funzioni, indirizzi di ritorno e variabili locali (cresce verso il basso).

Tutte le informazioni su un processo sono contenute nel **Process Control Block (PCB)**, che include lo stato del processo, il Program Counter, i registri della CPU, le informazioni di scheduling e la tabella dei file aperti.

### 2.2 Stati di un Processo
- **New:** Il processo è in fase di creazione.
- **Ready:** Il processo è pronto e in attesa di essere assegnato alla CPU.
- **Running:** Le istruzioni sono in esecuzione sulla CPU.
- **Waiting (Blocked):** Il processo attende un evento (I/O, segnale).
- **Terminated:** L'esecuzione è terminata.

### 2.3 Creazione e Terminazione (POSIX)
- `fork()`: Crea un processo figlio duplicando il padre. Restituisce 0 al figlio e il PID del figlio al padre. Nei sistemi moderni usa **Copy-on-Write (COW)** per ritardare la copia delle pagine fisiche fino a una scrittura.
- `exec()`: Sostituisce lo spazio di memoria del processo con un nuovo programma.
- `wait()` / `waitpid()`: Il padre attende la terminazione del figlio e ne raccoglie l'exit status.

> [!warning] Processi Zombie e Orfani
> - **Zombie:** Un processo figlio è terminato, ma il padre non ha ancora chiamato `wait()`. Il PCB rimane nel sistema.
> - **Orfano:** Il padre termina prima del figlio. Il figlio viene adottato dal processo `init` (o `systemd`), che ne farà la `wait()`.

### 2.4 Inter-Process Communication (IPC)
I processi non condividono memoria di default. Per comunicare usano l'IPC:
1.  **Shared Memory (Memoria Condivisa):** Più processi mappano la stessa regione fisica nel loro spazio virtuale tramite `shm_open` e `mmap`. Molto veloce, ma richiede sincronizzazione esplicita (es. semafori).
2.  **Message Passing:** Comunicazione tramite il kernel (senza memoria condivisa diretta).
    - **Pipe Anonime:** (`pipe()`) Unidirezionali (half-duplex), solo per processi imparentati (padre-figlio).
    - **Named Pipe (FIFO):** (`mkfifo`) Bidirezionali asimmetriche, usano il filesystem, permettono comunicazione tra processi non imparentati.
    - **Socket:** Bidirezionali, per comunicazione su rete o locale.

### 2.5 Thread e Legge di Amdahl
Un **thread** (Lightweight Process) è l'unità base di utilizzo della CPU. Condivide con gli altri thread dello stesso processo codice (Text), dati (Data) e file aperti, ma ha un proprio **Program Counter, registri e Stack**.

> [!info] Concorrenza vs Parallelismo
> - **Concorrenza:** Più task avanzano nello stesso lasso di tempo (es. interleaving su singola CPU).
> - **Parallelismo:** Più task eseguono *simultaneamente* su core diversi.

**Legge di Amdahl:** Definisce il limite teorico di speedup ($S$) parallelizzando un programma:
$$ S \leq \frac{1}{S_{seq} + \frac{1 - S_{seq}}{N}} $$
dove $S_{seq}$ è la frazione strettamente seriale del programma e $N$ è il numero di core.

### 2.6 Gestione dei Thread (Pthreads)
- **TID User-level vs Kernel-level:** In Linux (modello 1:1), ogni user thread ha un corrispondente kernel thread. Il kernel usa un TID progressivo (`SYS_gettid`, visibile con `ps -T`), mentre `pthreads` gestisce un ID interno alla libreria (`pthread_self()`).
- **Cancellazione Thread:** `pthread_cancel()` invia una richiesta di cancellazione.
  - *Asynchronous:* Il thread può terminare in qualsiasi momento (pericoloso per i lock).
  - *Deferred (Default):* Il thread termina solo quando raggiunge un **Cancellation Point** (es. `sleep`, `wait`, o manuale con `pthread_testcancel()`).
- **Signal Handling nei Thread:**
  I segnali ordinari *pending* non si accumulano (più segnali identici = 1 handler invocato). Le maschere di segnale (`pthread_sigmask`) impostate prima del lancio dei thread vengono ereditate dai figli.

---

## Modulo 3: CPU Scheduling

### 3.1 Concetti di Base e Criteri
Lo scheduler decide quale processo nella coda *Ready* deve usare la CPU, alternando tra **CPU burst** e **I/O burst**.
Lo scheduling può essere:
- **Preemptive (Con prelazione):** Il processo in esecuzione può essere interrotto forzatamente (es. timeout o arrivo di processo a priorità maggiore).
- **Non-Preemptive:** Il processo cede volontariamente la CPU.

> [!info] Criteri di Valutazione
> - **Throughput:** Numero di processi completati nell'unità di tempo.
> - **Turnaround Time:** Tempo tra l'arrivo e il completamento.
> - **Waiting Time:** Tempo totale trascorso in coda Ready.
> - **Response Time:** Tempo tra la richiesta e la prima risposta.

### 3.2 Algoritmi Tradizionali
- **FCFS (First Come First Served):** Semplice coda FIFO. Soffre dell'**effetto convoglio** (un processo CPU-bound lungo blocca tutti i brevi I/O-bound).
- **SJF (Shortest Job First):** Sceglie il processo con il burst più breve. È **ottimale** per minimizzare il tempo medio di attesa. Per stimare il burst futuro usa la **media esponenziale**: $\tau_{n+1} = \alpha t_n + (1 - \alpha)\tau_n$.
- **SRTF (Shortest Remaining Time First):** Variante preemptive di SJF. Se arriva un processo con burst minore del tempo rimanente del processo attuale, prelaziona.
- **Round-Robin (RR):** Assegna a ogni processo un **quanto di tempo**. Se non finisce, viene interrotto e rimesso in coda. Equo e privo di starvation.
- **Priorità:** Sceglie il processo con priorità più alta. Rischio di **starvation** per i processi a bassa priorità, risolto tramite **aging** (aumentare la priorità col tempo di attesa).
- **Multi-Level Feedback Queue (MLFQ):** Code a priorità diverse con spostamento dei processi tra le code (es. declassamento per chi usa tutto il quanto, promozione per chi aspetta troppo).

### 3.3 Scheduling Real-Time
Nei sistemi real-time, i processi hanno una scadenza (**deadline**).
- **Soft Real-Time:** Il SO dà la massima precedenza, ma senza garanzie assolute.
- **Hard Real-Time:** Le deadline sono garantite (richiede RTOS specifici).
Algoritmi per task periodici (Periodo $T$, Burst $t$):
- **Rate Monotonic (RMS):** Priorità statica basata sulla frequenza ($1/T$). Garantito se utilizzo $\leq n(2^{1/n}-1)$, ovvero circa 69% per $n \to \infty$.
- **Earliest Deadline First (EDF):** Priorità dinamica alla deadline più vicina. Ottimale, garantisce se l'utilizzo è $\leq 100\%$.

### 3.4 Scheduling in Linux
- **CFS (Completely Fair Scheduler):** Mira all'equità assegnando CPU proporzionalmente. Usa un **virtual runtime** (l'orologio scorre più o meno velocemente in base alla priorità `nice`). Sceglie sempre il processo con il minor virtual runtime tramite un albero Rosso-Nero $O(1)$.
- **EEVDF (Earliest Eligible Virtual Deadline First - Linux 6.6+):** Sostituisce CFS. Unisce **eligibilità** (un processo non deve aver consumato più del dovuto rispetto al suo lag temporale) e **virtual deadline** per garantire maggiore reattività.

---

## Modulo 4: Sincronizzazione e Concorrenza

### 4.1 Il Problema della Sezione Critica
Una **sezione critica** è un frammento di codice in cui si manipolano dati condivisi (race condition se non protetto). Una soluzione valida deve garantire:
1.  **Mutua Esclusione:** Solo un processo alla volta può essere nella sezione critica.
2.  **Progresso:** Se nessuno è dentro e qualcuno vuole entrare, la scelta non può essere rinviata all'infinito.
3.  **Bounded Waiting:** Nessun processo deve aspettare all'infinito (no starvation).

### 4.2 Supporto Hardware e Lock
- **Istruzioni Atomiche:** L'hardware fornisce istruzioni indivisibili (che non possono essere interrotte) come **Test-and-Set** o **Compare-and-Swap (CAS)**. Il CAS confronta un valore atteso e, se uguale, lo scambia; è la base per la programmazione **lock-free** (es. incremento lock-free rubando cicli in caso di contesa).
- **Spin Lock:** Basato sul *busy waiting* (il thread cicla verificando la condizione). Spreca cicli di CPU ma evita il context switch. Ottimo in multicore per attese brevi.
- **Mutex Lock (Mutual Exclusion):** Se il lock non è disponibile, il thread si sospende (sleeping) e viene risvegliato da chi lo rilascia. Ottimo per attese lunghe.

### 4.3 Semafori e Monitor
> [!abstract] Definizione di Semaforo (Dijkstra)
> Una variabile intera $S$ con due operazioni atomiche:
> - **Wait (P):** $S \leftarrow S-1$. Se $S < 0$, il processo si blocca.
> - **Signal (V):** $S \leftarrow S+1$. Se $S \leq 0$, sveglia un processo in attesa.

- I semafori risolvono eleganti problemi classici (es. Produttore-Consumatore con 3 semafori: `mutex`, `empty`, `full`).
- **Monitor:** Struttura ad alto livello (ADT) che garantisce la mutua esclusione strutturalmente (incapsula dati e metodi). Le **Variabili di Condizione** (`cond.wait()`, `cond.signal()`, `cond.broadcast()`) permettono ai thread di sospendersi in attesa di specifici stati logici (utilizzato ad es. nel problema dei 5 Filosofi).

### 4.4 Deadlock e Inversione di Priorità
- **Deadlock:** Un insieme di processi bloccati circolarmente in attesa di risorse (es. Filosofi incrociati o lock invertiti). Requisiti (Condizioni di Coffman): Mutua esclusione, Hold and Wait, No preemption, Circular Wait. Per prevenirlo, si usa spesso l'**ordinamento totale dei lock**.
- **Priority Inversion:** Un task ad alta priorità $H$ è bloccato da un task a bassa priorità $L$ che detiene un lock. Un task a priorità media $M$ prelaziona $L$, tenendo di fatto bloccato $H$ a tempo indefinito (es. caso Mars Pathfinder).
- **Soluzione:** **Priority Inheritance** (Ereditarietà di priorità), $L$ eredita temporaneamente la priorità di $H$ per completare rapidamente la sezione critica.

---

## Modulo 5: Gestione della Memoria e Memoria Virtuale

### 5.1 Indirizzi Logici vs Fisici e MMU
- **Indirizzo Logico (Virtuale):** Generato dalla CPU, è quello visto dal processo utente.
- **Indirizzo Fisico:** Indirizzo reale della memoria RAM.
- **MMU (Memory Management Unit):** Componente hardware che traduce in tempo reale (a runtime) gli indirizzi logici in fisici. Il **Binding** a tempo di esecuzione è l'unico che permette la rilocazione dinamica del processo.

### 5.2 Frammentazione e Paginazione (Paging)
L'allocazione contigua soffre di **frammentazione esterna** (spazio libero frammentato in piccoli buchi non utilizzabili).
La **Paginazione** risolve il problema:
- Memoria fisica divisa in blocchi fissi: **Frame**.
- Memoria logica divisa in blocchi uguali: **Pagine**.
Elimina la frammentazione esterna, lasciando solo un piccolo spreco nell'ultima pagina (**frammentazione interna**).
L'indirizzo logico è diviso in `(Numero Pagina (p), Offset (d))`. La **Page Table** mappa `p` al numero di frame `f`.

### 5.3 TLB e Tempo di Accesso (EAT)
La Page Table risiede in memoria: ogni accesso logico richiederebbe due accessi fisici (uno alla tabella, uno al dato).
Si usa la **TLB (Translation Lookaside Buffer)**, una cache hardware associativa ad altissima velocità.
- **Hit:** La traduzione è nella TLB (tempo di accesso $\approx 0$).
- **Miss:** Bisogna leggere la Page Table in RAM, e poi aggiornare la TLB.
**EAT (Effective Access Time):** $EAT = \alpha (\epsilon + T_{mem}) + (1 - \alpha) (\epsilon + 2T_{mem})$, dove $\alpha$ è l'hit rate e $\epsilon$ è il tempo della TLB.

### 5.4 Memoria Virtuale e Demand Paging
Disaccoppia lo spazio virtuale dalla RAM fisica, permettendo di caricare solo le pagine necessarie.
- **Page Fault:** La CPU accede a una pagina marcata come *Invalid/Absent*. Genera una trap, il SO cerca la pagina sul disco (Backing Store), la carica in un frame libero, aggiorna la Page Table e fa ripartire l'istruzione.
- **Copy-on-Write (COW):** Ottimizza la `fork()`. Padre e figlio condividono le stesse pagine in lettura. Se uno scrive, scatta un fault e la pagina viene duplicata.

### 5.5 Algoritmi di Sostituzione Pagina
Quando la RAM è piena e serve un frame, bisogna espellere una **Pagina Vittima**. Se il *Dirty Bit* (modificata) è 1, va scritta su disco (costoso).
- **FIFO:** Sostituisce la più vecchia. Soffre dell'**Anomalia di Belady** (più frame = più fault in alcuni casi).
- **OPT (Ottimale):** Sostituisce la pagina usata più in là nel futuro. Impossibile da implementare, serve come benchmark.
- **LRU (Least Recently Used):** Sostituisce la pagina non usata da più tempo. Nessuna anomalia di Belady, ma richiede hardware costoso (timestamp/stack).
- **Clock (Second Chance):** Approssimazione di LRU. Usa il **Reference Bit**. Una lancetta scorre circolarmente: se il bit è 1, dà una "seconda chance" (lo mette a 0 e avanza); se è 0, sostituisce la pagina.

> [!warning] Thrashing (Satellamento)
> Se un processo non ha abbastanza frame per il suo *Working Set* (pagine usate attivamente), genera infiniti Page Fault. Il sistema passa il tempo a fare I/O su disco, azzerando l'utilizzo della CPU. Soluzione: diminuire la multiprogrammazione.

### 5.6 Allocazione Memoria Kernel
Il kernel usa allocatori specifici per non sprecare memoria con la frammentazione interna del paging 4KB:
- **Buddy System:** Alloca blocchi contigui fisici in potenze di 2. Unisce ("merge") blocchi liberi adiacenti (gemelli).
- **Slab Allocator:** Pre-alloca cache di oggetti frequenti (es. inode, task_struct) senza overhead di inizializzazione e annullando la frammentazione interna.

---

## Modulo 6: File System, Storage e I/O

### 6.1 Struttura del Disco (HDD vs SSD)
- **HDD (Hard Disk Drive):** Magnetico, basato su testine, tracce e cilindri. Tempi dominati dal **Seek Time** e **Rotational Latency**.
- **SSD (Solid State Drive):** Elettronico (NAND Flash). Nessun seek time. Problemi: numero limitato di scritture, necessità di cancellare a blocchi (gestito dal **Flash Translation Layer - FTL** con *Wear Leveling* e *Garbage Collection*).

### 6.2 Disk Scheduling (per HDD)
Minimizza il movimento della testina.
- **FCFS:** Ordine d'arrivo (scadente).
- **SSTF (Shortest Seek Time First):** Va alla traccia più vicina (rischio starvation).
- **SCAN (Ascensore):** Va da un estremo all'altro, servendo le richieste.
- **C-SCAN:** Va in una sola direzione, poi torna all'inizio senza servire richieste (più equo).

### 6.3 Architettura Logica del File System
- **Inode / FCB:** Contiene i metadati del file (dimensione, permessi, timestamp, puntatori ai blocchi). *Non contiene il nome.*
- **Directory:** Un file che mappa i nomi dei file ai loro Inode Number.
- **Hard Link:** Due nomi diversi per lo stesso Inode. Il file esiste finché c'è almeno un hard link.
- **Soft/Symbolic Link:** Un file speciale che contiene il path verso un altro file. Se il target è eliminato, il link si rompe.
- **Tabelle dei File Aperti:** 
  1. *Per-process FD table* (punta alla tabella globale).
  2. *System-wide open file table* (mantiene l'offset di r/w).
  3. *In-memory Inode table* (dati sul disco).

### 6.4 Metodi di Allocazione dei Blocchi
- **Contigua:** File allocati sequenzialmente. Ottimo accesso, ma soffre frammentazione esterna.
- **Concatenata (FAT):** Lista concatenata (spesso tramite la File Allocation Table in RAM). No frammentazione esterna, accesso random lento se non ottimizzato.
- **Indicizzata (Unix Inodes):** Un array di puntatori (diretti per file piccoli, indiretti, doppio indiretti e triplo indiretti per file enormi). Garantisce alta flessibilità e velocità.

### 6.5 Affidabilità e RAID
- **RAID 0:** Striping (solo performance, no affidabilità).
- **RAID 1:** Mirroring (duplicazione esatta).
- **RAID 5:** Striping + Parità distribuita (tollera 1 guasto).
- **RAID 6:** Striping + Doppia parità (tollera 2 guasti).
- **Journaling:** I FS (ext4, NTFS) registrano l'intento in un *Journal* log circolare prima di modificare i metadati sul disco. Dopo un crash, il recovery legge il journal per completare o annullare operazioni, evitando la lenta scansione del disco (`fsck`).

### 6.6 Sottosistema I/O
- I dispositivi sono visti come **Block Devices** (accesso random a blocchi, es. dischi) o **Character Devices** (stream di byte, es. tastiera, terminali TTY con Line Discipline).
- **VFS (Virtual File System):** Strato di astrazione in Linux che permette di usare ext4, FAT, NTFS offrendo un'unica API POSIX (`open`, `read`, `write`) alle applicazioni.
