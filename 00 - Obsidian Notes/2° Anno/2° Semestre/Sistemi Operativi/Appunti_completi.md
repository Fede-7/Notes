# Sistemi Operativi — Appunti Strutturati
*(Basato sulle lezioni del Prof. Alberto Finzi, Corso di Sistemi Operativi)*

> **Introduzione**:
> I **Sistemi Operativi** rappresentano il fondamento software di qualsiasi calcolatore moderno, fungendo da intermediari tra l'hardware e le applicazioni utente. Questo documento sintetizza i concetti fondamentali del corso, organizzandoli in moduli coerenti che spaziano dall'architettura di base e dalla gestione dei processi, fino alla memoria virtuale, allo scheduling, alla sincronizzazione e ai file system. L'approccio è rigorosamente accademico, con enfasi sulla **correttezza formale**, sull'**analisi delle prestazioni** e sull'**implementazione pratica** nei sistemi Unix-like.

---

## 1. Introduzione e Architettura del Sistema Operativo

### 1.1 Definizione e Obiettivi Fondamentali
**Sistema Operativo (SO)**:
Programma di controllo che gestisce le risorse hardware di un calcolatore, agendo da intermediario tra utente e macchina. È il primo strato software caricato all'avvio.

**Obiettivi principali**:
- **Gestione delle risorse**: Allocazione efficiente di CPU, memoria e periferiche.
- **Astrazione**: Fornire un modello semplificato dell'hardware (es. file system gerarchico, memoria contigua).
- **Controllo dei conflitti**: Risolvere le contese tra processi/utenti concorrenti.
- **Efficienza**: Massimizzare il throughput e minimizzare i tempi di risposta.

### 1.2 Struttura a Strati e Dual Mode
Il SO opera secondo un'architettura a strati che separa nettamente i privilegi di esecuzione.

```mermaid
graph TB
    U[Applicazioni Utente] -->|System Call| K[Kernel Mode]
    K -->|Driver/Interrupt| H[Hardware: CPU, RAM, I/O]
    U -.->|User Mode| K
    style U fill:#e1f5fe,stroke:#01579b
    style K fill:#ffebee,stroke:#b71c1c
    style H fill:#f3e5f5,stroke:#4a148c
```

**Dual Mode (Modalità Duale)**:
La CPU opera sempre in una di due modalità, distinte da un **bit hardware**:
- **Kernel Mode**: Accesso completo all'hardware e alle istruzioni privilegiate.
- **User Mode**: Operazioni limitate; per accedere all'hardware è necessario invocare il kernel tramite *system call*.

> ⚠️ **Attenzione**:
> La transizione tra le modalità è **sempre controllata dal kernel**. Sistemi storici come MS-DOS non implementavano questo bit, rendendo l'intero sistema vulnerabile a programmi utente maliziosi.

### 1.3 Evoluzione Storica dei Sistemi Operativi
| Generazione | Periodo | Tecnologia | Caratteristiche SO |
|---|---|---|---|
| **I** | 1940-1950 | Valvole | Nessun SO; operatore = programmatore; nasce FORTRAN |
| **II** | 1950-1960 | Transistor | Batch processing, spooling, primo monitor residente |
| **III** | 1960-1970 | Circuiti Integrati | Multiprogrammazione, time-sharing, dual mode, UNIX |
| **IV** | 1980 | Personal Computer | MS-DOS, GUI (Xerox PARC → Apple → Windows) |
| **V** | 2000-Oggi | Mobile/Cloud | iOS, Android, virtualizzazione massiva, cloud OS |

### 1.4 Meccanismo delle Interruzioni
Le **interruzioni** permettono alla CPU di sospendere temporaneamente l'esecuzione corrente per gestire eventi asincroni, evitando il costoso *polling*.

**Tipologie di interrupt**:
| Tipo | Origine | Sincronia | Esempio |
|---|---|---|---|
| **Hardware Interrupt** | Periferica esterna | Asincrono | Fine trasferimento dati, pressione tasto |
| **Eccezione** | CPU (errore esecuzione) | Sincrono | Division by zero, Segmentation Fault |
| **Trap** | Programma (richiesta esplicita) | Sincrono | System Call, breakpoint debugger |

> **Osservazione**:
> Il **vettore di interruzioni** è una tabella protetta dal kernel che mappa ogni numero di interrupt all'indirizzo della relativa routine di servizio. La sua protezione è critica per la sicurezza del sistema.

### 1.5 La Gerarchia API → ABI → System Call
La comunicazione tra spazio utente e kernel avviene attraverso livelli di astrazione sovrapposti:

```
[Programma C]       → printf("Hello\n")
     ↓
[Standard C Lib]    → write(fd, buf, n)
     ↓
[API POSIX]         → write(fd, buf, n)  ← interfaccia standardizzata
     ↓
[ABI (Machine)]     → syscall(1, ...)    ← istruzione trap
     ↓
[Kernel]            → sys_write()        ← routine di servizio
```

**System Call**:
Istruzione macchina speciale che trasferisce il controllo dal processo utente al kernel. I parametri vengono passati tramite **registri CPU** (approccio moderno) o tramite puntatore a blocco in memoria.

---

## 2. Processi, Thread e Comunicazione

### 2.1 Il Processo: Definizione e Ciclo di Vita
**Processo**:
Programma in esecuzione. Possiede uno spazio di indirizzamento dedicato, un Program Counter (PC), registri e risorse associate.

**Ciclo di vita (Grafo degli Stati)**:
```mermaid
stateDiagram-v2
    [*] --> Creato
    Creato --> Pronto : Scheduler
    Pronto --> In_Esecuzione : Dispatch
    In_Esecuzione --> Pronto : Time-slice scaduto / Prelazione
    In_Esecuzione --> In_Attesa : Richiesta I/O
    In_Attesa --> Pronto : I/O completato (Interrupt)
    In_Esecuzione --> Terminato
    Terminato --> [*]
```

### 2.2 Operazioni Fondamentali: `fork`, `exec`, `wait`
La creazione e gestione dei processi in Unix si basa su tre primitive POSIX:
- **`fork()`**: Duplica il processo chiamante. Restituisce `0` al figlio, `PID > 0` al padre.
- **`exec()`**: Sostituisce l'immagine del processo corrente con un nuovo programma.
- **`wait()`**: Sospende il padre fino alla terminazione del figlio, recuperando lo status di uscita.

> ⚠️ **Attenzione**:
> Un processo terminato ma non ancora `wait()`-ato dal padre diventa uno **Zombie**. Occupa spazio nel PCB ma non risorse CPU/RAM. Se il padre termina prima del figlio, il figlio viene adottato da `init` (PID 1).

### 2.3 Thread: Concetti e Modelli di Mapping
**Thread**:
Unità di esecuzione sequenziale all'interno di un processo. Condividono heap, dati globali e file descriptor, ma possiedono stack e registri dedicati.

**Modelli di Mapping User/Kernel Thread**:
| Modello | Descrizione | Vantaggi | Svantaggi |
|---|---|---|---|
| **Many-to-One** | Molti user thread → 1 kernel thread | Leggero, gestione in user space | Blocco totale se un thread fa I/O; nessun parallelismo |
| **One-to-One** | 1 user thread → 1 kernel thread | Vero parallelismo; isolamento blocchi | Overhead kernel; proliferazione risorse |
| **Many-to-Many** | M user thread → K kernel thread | Flessibilità; pool controllato | Complessità implementativa (richiede LWP/upcall) |

Linux e Windows adottano il modello **one-to-one**.

### 2.4 Concorrenza vs Parallelismo e Legge di Amdahl
**Concorrenza**: Esecuzione alternata di task nello stesso intervallo temporale (possibile su single-core).
**Parallelismo**: Esecuzione simultanea fisica su core distinti.

**Legge di Amdahl**:
Stima lo speedup teorico ottenibile parallelizzando un programma. Sia $S$ la frazione seriale ($0 \leq S \leq 1$):
$$\text{Speedup}(n) = \frac{1}{S + \frac{1-S}{n}}$$
> **Osservazione**:
> Anche con $n \to \infty$, lo speedup è limitato a $1/S$. La componente seriale è il collo di bottiglia architetturale.

### 2.5 Comunicazione tra Processi (IPC)
I processi possono scambiare dati tramite:
1. **Memoria Condivisa**: Regione di RAM accessibile da più processi. Richiede sincronizzazione esplicita.
2. **Message Passing**: Scambio di messaggi tramite canali (pipe, socket).

**Pipe Anonime vs FIFO**:
- **Pipe**: Unidirezionali, solo per processi imparentati, esistono solo in memoria kernel.
- **FIFO (Named Pipe)**: Persistono nel filesystem, permettono comunicazione tra processi non correlati.

---

## 3. Scheduling della CPU

### 3.1 Criteri e Componenti
Lo **Short-term Scheduler** decide quale processo dalla coda *Ready* mandare in CPU. Il **Dispatcher** materializza la decisione (context switch).

**Metriche di valutazione**:
- **Throughput**: Job completati per unità di tempo.
- **Turnaround Time**: Tempo totale da submit a completion.
- **Waiting Time**: Tempo totale in coda Ready.
- **Response Time**: Tempo alla prima risposta (critico per sistemi interattivi).

### 3.2 Algoritmi Tradizionali
| Algoritmo | Meccanismo | Ottimalità | Problemi |
|---|---|---|---|
| **FCFS** | Primo arrivato, primo servito | No | Effetto convoglio (CPU-bound bloccano I/O-bound) |
| **SJF** | Minimo CPU burst stimato | Sì (minimizza waiting time) | Richiede oracolo; starvation processi lunghi |
| **SRTF** | SJF preemptive | Sì | Overhead context switch elevato |
| **Round Robin** | Quanto di tempo $q$ per processo | Equo | Calibrazione $q$ critica (troppo piccolo → overhead) |

**Stima del CPU Burst (Media Esponenziale)**:
$$\tau_{n+1} = \alpha \cdot t_n + (1-\alpha) \cdot \tau_n$$
Dove $t_n$ è il burst effettivo, $\tau_n$ la stima precedente, e $\alpha \in [0,1]$ il fattore di smorzamento.

### 3.3 Scheduling con Priorità e Code Multiple
- **Priorità Fissa**: Numero basso = alta priorità. Rischio di **starvation**. Soluzione: **Aging** (aumentare priorità col tempo di attesa).
- **Multi-Level Feedback Queue**: Code multiple con algoritmi diversi (es. RR per interattivi, FCFS per batch). I processi migrano tra le code in base al comportamento osservato (CPU-bound affondano, I/O-bound salgono).

### 3.4 Scheduling Real-Time
- **Soft Real-Time**: Massima urgenza senza garanzie assolute.
- **Hard Real-Time**: Scadenze garantite (richiede RTOS).

**Rate Monotonic (RMS)**: Priorità statica inversamente proporzionale al periodo $T$. Garantisce le deadline se $\sum \frac{t_i}{T_i} \leq n(2^{1/n}-1)$.
**Earliest Deadline First (EDF)**: Priorità dinamica alla deadline più ravvicinata. Ottimale: se esiste uno scheduling fattibile, EDF lo trova.

### 3.5 Scheduling nei Sistemi Moderni (Linux)
- **CFS (Completely Fair Scheduler)**: Usa un **virtual runtime** ($v_r$) che scorre più lentamente per processi ad alta priorità. Albero rosso-nero per selezione $O(1)$.
- **EEVDF (Linux 6.6+)**: Combina *eligibilità* (fairness passata) con *virtual deadline* (reattività futura). Più reattivo di CFS per workload interattivi.

---

## 4. Sincronizzazione e Deadlock

### 4.1 Il Problema della Sezione Critica
Ogni processo ha una struttura: `Entry → Critical Section → Exit → Remainder`.
Un meccanismo corretto deve garantire:
1. **Mutua Esclusione**: Al più un processo in CS.
2. **Progresso**: La decisione di ingresso non dipende da processi in remainder.
3. **Bounded Waiting**: Limite massimo di ingressi altrui prima del servizio.

### 4.2 Supporto Hardware e Primitive
Le soluzioni software pure (es. Peterson) richiedono **memory barriers** per prevenire il riordino delle istruzioni da parte del compilatore/CPU.
**Istruzioni Atomiche**:
- **Test-and-Set (TAS)**: Legge e setta a `True` atomicamente.
- **Compare-and-Swap (CAS)**: Sostituisce un valore solo se uguale a quello atteso. Fondamentale per strutture *lock-free*.

### 4.3 Mutex, Semafori e Monitor
| Meccanismo | Livello | Descrizione |
|---|---|---|
| **Mutex Lock** | Basso | Acquisizione/release binaria. Leggero, ideale per CS brevi. |
| **Semaforo** | Medio | Variabile intera con `wait()`/`signal()`. Binario (mutex) o contatore ($k$ slot). |
| **Monitor** | Alto | Tipo di dato astratto. Garantisce mutua esclusione strutturalmente sui metodi. |

### 4.4 Variabili di Condizione
Permettono ai thread di sospendersi in attesa di una condizione logica.
```c
pthread_mutex_lock(&mutex);
while (!condizione) {
    pthread_cond_wait(&cond, &mutex); // Rilascia mutex e dorme
}
// Sezione critica
pthread_mutex_unlock(&mutex);
```
> ⚠️ **Attenzione**:
> Usare sempre un `while` loop, non `if`, per proteggersi dai **false awakenings** e dalle race condition sulla valutazione della condizione.

### 4.5 Deadlock e Priority Inversion
**Deadlock**: Attesa circolare permanente. Richiede 4 condizioni (Coffman): mutua esclusione, hold-and-wait, non-prelazione, attesa circolare.
**Priority Inversion**: Processo ad alta priorità bloccato da uno a bassa priorità, mentre uno a media priorità prelaziona il basso. Soluzione: **Priority Inheritance** (il processo che tiene il lock eredita temporaneamente la priorità del bloccato).

---

## 5. Gestione della Memoria

### 5.1 Indirizzi Logici vs Fisici e MMU
La **MMU (Memory Management Unit)** traduce indirizzi logici (generati dalla CPU) in indirizzi fisici (RAM). Questo disaccoppiamento permette la **memoria virtuale** e la protezione dello spazio di indirizzamento.

### 5.2 Paginazione (Paging)
La memoria fisica è divisa in **frame**, quella logica in **pagine** (stessa dimensione, es. 4KB).
- **Vantaggio**: Elimina la frammentazione esterna.
- **Page Table**: Tabella che mappa `pagina[i] → frame[j]`.
- **Frammentazione Interna**: Max `frame_size - 1` byte per processo.

### 5.3 TLB e Effective Access Time (EAT)
La **TLB (Translation Lookaside Buffer)** è una cache hardware associativa per le traduzioni recenti.
$$EAT = \alpha(\epsilon + T_M) + (1-\alpha)(\epsilon + 2T_M)$$
Dove $\alpha$ è l'hit rate, $\epsilon$ il tempo TLB, $T_M$ il tempo memoria. Un hit rate >99% è cruciale per le prestazioni.

### 5.4 Memoria Virtuale e Demand Paging
Le pagine vengono caricate in RAM solo al primo accesso (**Demand Paging**). Un accesso a pagina non residente genera un **Page Fault**, gestito dal kernel che alloca un frame, schedula l'I/O e riavvia l'istruzione.

**Copy-on-Write (COW)**:
Ottimizzazione per `fork()`. Padre e figlio condividono le pagine in read-only. La copia fisica avviene solo quando uno dei due tenta di scrivere.

### 5.5 Algoritmi di Sostituzione e Thrashing
| Algoritmo | Criterio | Note |
|---|---|---|
| **FIFO** | Primo entrato, primo uscito | Soffre dell'anomalia di Belady |
| **OPT** | Mai usato nel futuro | Teorico, benchmark ottimale |
| **LRU** | Meno usato nel passato | Stack algorithm; costoso da implementare puro |
| **Clock** | Approssimazione LRU (Reference Bit) | Standard nei SO moderni |

**Thrashing**: Fenomeno in cui il sistema spende più tempo a swap pagine che a eseguire istruzioni, causato da un grado di multiprogrammazione eccessivo rispetto alla RAM disponibile. Si previene regolando dinamicamente i **Working Set**.

---

## 6. Sistemi di I/O e Storage

### 6.1 Architettura a Strati e Classificazione
Il sottosistema I/O è strutturato in: `System Call API → Device Independent OS → Drivers → Interrupt Handlers → Hardware`.
- **Block Devices**: Accesso randomico a blocchi fissi (HDD, SSD).
- **Character Devices**: Flusso sequenziale di byte (TTY, tastiera).

### 6.2 Dischi Magnetici (HDD) vs SSD
| Caratteristica | HDD | SSD (NAND Flash) |
|---|---|---|
| **Accesso** | Meccanico (Seek + Rotational Latency) | Elettronico (accesso random veloce) |
| **Scrittura** | Sovrascrittura diretta | Cancellazione a blocco → riscrittura a pagina |
| **Usura** | Bassa | Limitata (P/E cycles); richiede Wear Leveling |
| **Scheduling** | Critico (SSTF, SCAN, C-LOOK) | Inutile (NOOP/Deadline sufficiente) |

### 6.3 Affidabilità e RAID
**RAID (Redundant Array of Independent Disks)** combina dischi per performance o ridondanza:
- **RAID 0**: Striping (massima velocità, zero tolleranza).
- **RAID 1**: Mirroring (massima affidabilità, 50% spazio utile).
- **RAID 5/6**: Striping + parità distribuita (tolleranza 1/2 guasti).

---

## 7. File System

### 7.1 Architettura Logica e Metadati
Il File System astrae i blocchi disco in file e directory. I metadati sono gestiti tramite **Inode** (Unix) o **MFT** (NTFS).
L'Inode contiene: permessi, timestamp, puntatori ai blocchi dati, ma **non il nome del file**.

**Tabelle dei File Aperti**:
1. **Per-Process FD Table**: Mappa interi (0,1,2...) a entry globali.
2. **System-wide Open File Table**: Contiene offset corrente, flags, puntatore all'Inode.
3. **In-Memory Inode Cache**: Copia RAM dei metadati persistenti.

### 7.2 Allocazione dei Blocchi e Inode
L'Inode Unix usa indirizzamento ibrido:
- **Diretto**: 12 puntatori immediati (accesso $O(1)$).
- **Indiretto Singolo/Doppio/Triplo**: Blocchi indice a cascata per file enormi.

### 7.3 Consistenza e Journaling
In caso di crash, le modifiche ai metadati possono rimanere a metà. Il **Journaling** registra le intenzioni di modifica in un log circolare prima di applicarle al disco principale. Al riavvio, il SO *replaya* le transazioni commitate o *unda* quelle incomplete, garantendo consistenza strutturale in pochi secondi.

---

## 8. Ambiente di Sviluppo e Shell Unix

### 8.1 La Shell e Redirezione
La shell (es. Bash) è un interprete comandi in user space. Supporta:
- **Redirezione**: `>` (overwrite), `>>` (append), `<` (input).
- **Pipe**: `|` connette lo stdout di un comando allo stdin del successivo.
- **Background**: `&` esegue il comando asincronamente.

### 8.2 Processo di Compilazione
1. **Preprocessore**: Espande macro (`#define`), include header.
2. **Compilatore**: Traduce C in assembly.
3. **Assemblatore**: Genera codice macchina (file oggetto `.o`).
4. **Linker**: Unisce oggetti e librerie in eseguibile (`ELF` su Linux).

**Linking Statico vs Dinamico**:
- **Statico** (`.a`): Codice libreria incorporato nell'eseguibile.
- **Dinamico** (`.so`): Riferimenti risolti a runtime dal *dynamic linker*. Risparmia memoria e permette aggiornamenti trasparenti.

---

## 📝 Esercizi Proposti per lo Studio

1. **Scheduling**: Dati i processi $P_1(arr.0, burst=8), P_2(arr.1, burst=4), P_3(arr.2, burst=9)$, calcolare il tempo medio di attesa usando **SRTF** e confrontarlo con **Round Robin** (quanto=4). Disegnare il diagramma di Gantt.
2. **Sincronizzazione**: Implementare in C la soluzione al problema del **Produttore-Consumatore** usando 3 semafori POSIX (`mutex`, `empty`, `full`) e una buffer circolare di dimensione $N$.
3. **Memoria Virtuale**: Spiegare come funziona il meccanismo **Copy-on-Write** durante una `fork()` seguita da `exec()`. Perché è più efficiente della duplicazione fisica immediata?
4. **File System**: Analizzare la struttura di un **Inode Unix** con 10 puntatori diretti, 1 singolo, 1 doppio e 1 triplo indiretto. Calcolare la dimensione massima teorica di un file assumendo blocchi da 4KB e indirizzi a 32 bit.
5. **System Call**: Scrivere un programma C che usa `open()`, `fork()`, `write()` e `read()` per far comunicare padre e figlio tramite un file condiviso. Discutere il comportamento dell'offset del file in entrambi i casi: `open()` prima e dopo la `fork()`.

> **Riferimenti Incrociati**:
> - Per dettagli sulla gestione dei segnali in contesto multi-thread, Vedi Sezione 2.5.
> - Per l'analisi delle prestazioni della TLB e formule EAT, Vedi Sezione 5.3.
> - Per la prevenzione del deadlock tramite ordinamento delle risorse, Vedi Sezione 4.5.

## 9. Avvio del Sistema e Gestione dello Swap

### 9.1 Il Processo di Bootstrap
Il **Bootstrap** è la sequenza di operazioni che porta il Sistema Operativo dalla memoria secondaria (disco) alla RAM, permettendone l'esecuzione.

#### Architettura Legacy: BIOS + MBR
- **BIOS (Basic Input/Output System)**: Firmware che esegue il POST (*Power-On Self-Test*) e cerca il dispositivo di boot.
- **MBR (Master Boot Record)**: I primi 512 byte del disco.
  - Contiene il *Boot Code* (446 byte) e la *Partition Table* (max 4 partizioni primarie).
  - **Limiti**: Supporta dischi fino a ~2.2 TB; indirizzamento a 32 bit.

#### Architettura Moderna: UEFI + GPT
- **UEFI (Unified Extensible Firmware Interface)**: Sostituisce il BIOS. Supporta mouse, rete pre-boot e interfaccia grafica.
- **GPT (GUID Partition Table)**:
  - Supporta partizioni a 64 bit (dischi enormi, >128 partizioni).
  - Include una copia di backup della tabella per la ridondanza.
  - **ESP (EFI System Partition)**: Partizione speciale (FAT32) contenente i bootloader (`.efi`).

### 9.2 Gestione dello Swap Space
Lo **Swap Space** è l'area su disco utilizzata come estensione della memoria fisica (*Backing Store*).
- **Raw Partition**: Area dedicata non formattata. Accesso diretto, minor overhead.
- **Swap File**: File regolare all'interno del file system. Più flessibile (ridimensionabile dinamicamente).
- **Swap Map**: Tabella mantenuta in RAM dal kernel per tracciare quali blocchi dello swap sono liberi o occupati, permettendo un rapido recupero durante un *Page Fault*.

---

## 10. Affidabilità e Storage Avanzato

### 10.1 Architetture RAID
**RAID (Redundant Array of Independent Disks)** combina più dischi fisici per migliorare le prestazioni, l'affidabilità o entrambi.

| Livello | Tecnica | Descrizione | Pro | Contro |
|---|---|---|---|---|
| **RAID 0** | Striping | Dati divisi su più dischi. | Massima velocità, 100% spazio. | Zero tolleranza ai guasti. |
| **RAID 1** | Mirroring | Duplicazione esatta dei dati. | Alta affidabilità, lettura veloce. | 50% spazio utile. |
| **RAID 5** | Striping + Parità | Parità distribuita su tutti i dischi. | Tolleranza a 1 guasto, efficienza. | Write penalty (calcolo parità). |
| **RAID 6** | Doppia Parità | Due blocchi di parità indipendenti. | Tolleranza a **2 guasti**. | Overhead scrittura maggiore. |
| **RAID 10** | Mirror + Stripe | Strisce di mirror. | Alta perf. + Alta affidabilità. | Costo elevato (50% spazio). |

### 10.2 Rilevamento e Correzione Errori
I dispositivi di storage utilizzano codici per garantire l'integrità dei dati contro la degradazione fisica.
- **Parity Bit**: Rileva errori a singolo bit (rende pari il numero di 1). Non corregge.
- **ECC (Error Correction Code)**: Es. **Codice di Hamming**. Aggiunge ridondanza per correggere errori automaticamente.
  - **SEC-DED**: *Single Error Correction, Double Error Detection*. Corregge 1 bit, rileva 2.
  - Se l'errore è incorrreggibile, il blocco viene marcato come *Bad Block* e rimappato.

---

## 11. File System: Strutturazione e Allocazione

### 11.1 Metodi di Allocazione dei File
Il metodo di allocazione determina come i blocchi di un file sono distribuiti fisicamente sul disco.

| Metodo | Descrizione | Vantaggi | Svantaggi |
|---|---|---|---|
| **Contigua** | Blocchi adiacenti. | Accesso sequenziale/diretto ottimo. | Frammentazione esterna; difficile espansione. |
| **Concatenata** | Lista di blocchi sparsi. | Nessuna frammentazione; espansione facile. | Accesso diretto lento; overhead puntatori. |
| **Indicizzata** | Blocco indice con puntatori. | Accesso diretto efficiente; nessuna frammentazione. | Overhead del blocco indice. |

> **Osservazione**:
> Il **FAT (File Allocation Table)** è una variante dell'allocazione concatenata dove i puntatori sono spostati in una tabella centrale in RAM, migliorando l'affidabilità e la velocità di accesso.

### 11.2 Hard Link vs Symbolic Link
| Caratteristica | Hard Link | Symbolic Link (Soft) |
|---|---|---|
| **Definizione** | Un altro nome per lo stesso Inode. | File speciale contenente il percorso del target. |
| **Inode** | Condiviso. | Distinto. |
| **Target** | Solo file (solitamente). | File o directory. |
| **Cross-FS** | No. | Sì. |
| **Validità** | Indipendente dal nome originale. | Diventa "rotto" se il target viene cancellato. |

### 11.3 Affidabilità: Journaling
Il **Journaling** previene la corruzione del file system in caso di crash improvviso.
1. **Write to Journal**: Le intenzioni di modifica ai metadati vengono scritte in un log circolare.
2. **Commit**: La transazione viene marcata come impegnata.
3. **Checkpoint**: Le modifiche vengono applicate ai metadati reali.
4. **Recovery**: Al riavvio, il SO *replaya* le transazioni completate o *unda* quelle incomplete.

---

## 12. I/O di Basso Livello e Architettura VFS

### 12.1 System Call Fondamentali
Le API POSIX forniscono un'interfaccia uniforme per l'I/O:
- **`open(pathname, flags, mode)`**: Restituisce un File Descriptor (FD). Flags comuni: `O_CREAT`, `O_TRUNC`, `O_APPEND`.
- **`read(fd, buf, count)` / `write(fd, buf, count)`**: Lettura/scrittura di byte. Aggiornano l'offset corrente.
- **`lseek(fd, offset, whence)`**: Modifica l'offset senza effettuare I/O. Permette accesso randomico.
- **`close(fd)`**: Rilascia le risorse e flush dei buffer kernel.

### 12.2 Sparse Files
I **Sparse Files** permettono di avere una dimensione logica maggiore di quella fisica.
- Quando si usa `lseek()` per saltare una regione e si scrive oltre, il kernel non alloca blocchi fisici per la regione intermedia ("hole").
- I "buchi" leggono come zeri (`\0`) ma non occupano spazio su disco.

### 12.3 Architettura a Strati del File System
Il file system è organizzato per favorire l'astrazione:
1. **Logical File System**: Gestisce API utente, permessi e directory logiche.
2. **File Organization Module**: Traduce indirizzi logici in fisici (allocazione blocchi).
3. **Basic File System**: I/O generici su blocchi fisici.
4. **Device Drivers**: Interfaccia specifica con l'hardware.

**Virtual File System (VFS)**:
Livello di astrazione che permette al kernel di supportare diversi file system (ext4, NTFS, FAT) contemporaneamente, presentando un'interfaccia uniforme alle applicazioni tramite strutture virtuali (Vnode).

### 12.4 Sottosistema I/O e Line Discipline
- **Block Devices**: Accesso randomico (dischi).
- **Character Devices**: Flusso sequenziale (tastiera, terminali).
- **Line Discipline**: Livello software per i terminali (TTY) che gestisce l'editing della riga, la conversione dei caratteri (es. `CR` → `LF`) e i segnali (es. `Ctrl+C` invia `SIGINT`).

---

## 📝 Esercizi Avanzati Proposti

1. **RAID e Affidabilità**:
   In un array **RAID 5** composto da 4 dischi da 1 TB ciascuno, calcolare:
   - La capacità totale utile dell'array.
   - La capacità residua e lo stato dell'array in caso di guasto di un disco.
   - Cosa accade se falliscono contemporaneamente due dischi?

2. **Calcolo Inode e Allocazione**:
   Dato un Inode con 10 puntatori diretti, 1 singolo, 1 doppio e 1 triplo indiretto, e una dimensione di blocco di 4 KB (32 bit per i puntatori):
   - Qual è la dimensione massima teorica di un file gestibile?
   - Quanti accessi a disco sono necessari per leggere l'ultimo byte di un file molto grande?

3. **System Call e Offset**:
   Si consideri il seguente codice C:
   ```c
   int fd = open("file.txt", O_RDWR | O_CREAT, 0644);
   if (fork() == 0) {
       write(fd, "Hello", 5);
       exit(0);
   }
   wait(NULL);
   char buf[10];
   read(fd, buf, 5); // Legge cosa?
   ```
   Spiegare perché la `read()` nel padre potrebbe non leggere "Hello" e come correggere il comportamento usando `lseek()`.

4. **Journaling e Consistenza**:
   Descrivere la sequenza di operazioni che il file system esegue quando si effettua un `mv` (spostamento) di un file tra due directory diverse su un file system journaling. Cosa viene registrato nel journal prima della modifica effettiva?

---

> **Riferimenti Incrociati**:
> - Per il confronto tra allocazione contigua e indicizzata, Vedi Sezione 11.1.
> - Per i dettagli sulla gestione della memoria virtuale e swap, Vedi Sezione 9.2.
> - Per l'architettura a strati del SO e i driver, Vedi Sezione 12.3.

## 13. Struttura del Kernel e Virtualizzazione

### 13.1 Principio di Separazione: Policy vs Meccanismo
Un principio fondamentale nella progettazione dei sistemi operativi è la distinzione tra **meccanismo** e **policy**.
- **Meccanismo**: *Come* si fa qualcosa (lo strumento tecnico).
- **Policy**: *Cosa* si fa (la decisione strategica).

> **Osservazione**:
> Separare i due permette di modificare le politiche (es. algoritmo di scheduling) senza dover riscrivere i meccanismi di base (es. il timer hardware).
> - *Esempio*: Il **meccanismo** è il timer hardware che genera interruzioni; la **policy** è la decisione di assegnare 10ms di tempo a un processo interattivo e 100ms a uno batch.

### 13.2 Paradigmi di Progettazione del Kernel
| Tipo di Kernel | Descrizione | Vantaggi | Svantaggi |
|---|---|---|---|
| **Monolitico** | Tutte le funzionalità (scheduling, memoria, driver) risiedono in kernel space. | Alta velocità (chiamate dirette); nessuna syscall overhead. | Difficile da mantenere; bug nei driver possono crashare tutto il sistema. |
| **Microkernel** | Solo il minimo vitale (IPC, scheduling base) è in kernel; servizi in user space. | Alta modularità e sicurezza; crash di un servizio non ferma il SO. | Overhead elevato (passaggio messaggi costante); complessità implementativa. |
| **Modulare** | Kernel base + moduli caricabili dinamicamente (es. driver, FS). | Flessibilità (Linux); aggiornamento senza riavvio. | Complessità di gestione delle dipendenze. |
| **Ibrido** | Compromesso tra monolitico e microkernel (es. Windows NT, macOS XNU). | Bilancia prestazioni e modularità. | Complessità architetturale. |

### 13.3 Virtualizzazione
La **virtualizzazione** permette di eseguire più sistemi operativi sullo stesso hardware fisico, isolandoli a vicenda.
- **Tipo 1 (Bare Metal)**: L'ipervisore gira direttamente sull'hardware (es. VMware ESXi, Xen).
- **Tipo 2 (Hosted)**: L'ipervisore gira come applicazione su un SO host (es. VirtualBox, VMware Workstation).

---

## 14. Gestione dei Segnali e Cancellazione dei Thread

### 14.1 Segnali in Contesto Multi-thread
I segnali sono notifiche asincrone inviate a processi o thread specifici.
- **Maschere di Segnali**: Ogni thread può bloccare segnali specifici tramite `pthread_sigmask`.
- **Segnali Pending**:
  - I segnali **ordinari** (es. `SIGUSR1`) **non si accodano**: se un segnale è già pending, nuovi invii vengono ignorati (collassati).
  - I segnali **real-time** (`SIGRTMIN`...`SIGRTMAX`) **si accodano** e vengono consegnati tutti in sequenza.

> ⚠️ **Attenzione**:
> Se si imposta una maschera di blocco *prima* di creare i thread, questa viene **ereditata** da tutti i thread figli. Se impostata *dopo*, vale solo per il thread chiamante.

### 14.2 Cancellazione dei Thread
La cancellazione (`pthread_cancel`) termina un thread forzatamente.
- **Deferred (Differita)**: La cancellazione avviene solo in un **cancellation point** (es. `sleep`, I/O, `pthread_testcancel`). È il comportamento default e più sicuro.
- **Asynchronous**: Il thread può essere cancellato in qualsiasi istruzione. Rischioso (può lasciare strutture dati inconsistenti o mutex bloccati).

---

## 15. Gestione Avanzata della Memoria del Kernel

### 15.1 Buddy System
Allocatore di memoria fisica usato dal kernel per gestire blocchi di grandi dimensioni.
- **Meccanismo**: Alloca blocchi di dimensione potenza di 2 ($2^n$ pagine).
- **Fusione**: Quando un blocco viene liberato, il sistema controlla se il suo "buddy" (blocco adiacente di stessa dimensione) è libero. Se sì, li fonde in un blocco più grande.
- **Vantaggio**: Riduce la frammentazione esterna e semplifica la deallocazione.

### 15.2 Slab Allocator
Gestisce oggetti kernel piccoli e frequenti (es. PCB, Inode, socket) sopra il Buddy System.
- **Struttura**:
  - **Cache**: Contiene oggetti dello stesso tipo.
  - **Slab**: Insieme di pagine fisiche contigue contenenti istanze pre-inizializzate.
- **Vantaggio**: Elimina l'overhead di inizializzazione per ogni allocazione e riduce la frammentazione interna.

### 15.3 Compressione della Memoria
Nei sistemi moderni (specialmente mobile), invece di scrivere pagine sporche su disco (swap lento e usura SSD), il kernel le **comprime** e le mantiene in RAM.
- **Trade-off**: Si scambiano cicli CPU e spazio RAM per guadagnare in latenza e durata dell'hardware.

---

## 16. Architetture di Memoria Hardware (Intel e ARM)

### 16.1 Intel x86: Segmentazione e Paging
- **Segmentazione**: L'indirizzo logico è `(Selettore, Offset)`. Il selettore punta alla **GDT** (Global Descriptor Table) o **LDT**.
- **Paging Gerarchico**:
  - **32-bit**: 2 livelli (Directory + Table). Supporta **PAE** (Physical Address Extension) per indirizzare fino a 64GB di RAM fisica.
  - **64-bit**: 4 livelli (PML4 → PDPT → PD → PT). Supporta **Huge Pages** (2MB, 1GB) per ridurre l'overhead TLB.

### 16.2 Architettura ARM v8
- Supporta pagine da 4KB, 16KB e 64KB.
- **TLB Separate**: I-TLB (istruzioni) e D-TLB (dati) a livello L1, unificate a L2.
- **Paging Structure Cache**: Cache dedicate per le strutture delle page table, riducendo il costo del *page table walk*.

---

## 17. Caching e Ottimizzazione delle Prestazioni I/O

### 17.1 Il Problema del Double Caching
Storicamente, Linux manteneva due cache separate:
1. **Buffer Cache**: Per blocchi disco grezzi.
2. **Page Cache**: Per memoria virtuale.
Questo causava duplicazione dei dati se un file veniva accesso sia via `read()` che via `mmap()`.

### 17.2 Unified Page Cache
Nei kernel moderni, le due cache sono fuse in una **Unified Page Cache**.
- I blocchi disco sono trattati come pagine di memoria virtuale.
- Sia le system call I/O che la memoria mappata accedono alle stesse pagine in RAM, garantendo coerenza e risparmio di spazio.

### 17.3 Read-Ahead e Pre-paging
- **Read-Ahead**: Il kernel rileva accessi sequenziali e precarica in cache i blocchi successivi per nascondere la latenza del disco.
- **Pre-paging**: Caricamento anticipato di pagine di memoria virtuale non ancora richieste (utile per codice sequenziale, meno per dati casuali).

---

## 📝 Esercizi Avanzati Proposti

1. **Kernel Memory Management**:
   Spiegare la differenza tra **Buddy System** e **Slab Allocator**. Perché il kernel non usa solo il Buddy System per allocare un `task_struct`?

2. **Virtualizzazione**:
   Confrontare un ipervisore di **Tipo 1** e uno di **Tipo 2** in termini di overhead di prestazioni e isolamento. Qual è l'impatto sulle system call di un guest OS?

3. **Unified Page Cache**:
   Descrivere cosa succede a livello di cache quando un processo esegue `mmap()` su un file già presente nella buffer cache. Come il kernel garantisce la coerenza dei dati?

4. **Architetture Intel**:
   Dato un indirizzo logico a 32 bit con paging a due livelli (10 bit directory, 10 bit table, 12 bit offset), calcolare quanti accessi a memoria sono necessari per risolvere l'indirizzo fisico in assenza di TLB hit.

---

> **Riferimenti Incrociati**:
> - Per i dettagli sulla gestione della memoria virtuale e swap, Vedi Sezione 9.2.
> - Per l'analisi delle prestazioni della TLB e formule EAT, Vedi Sezione 5.3.
> - Per la prevenzione del deadlock tramite ordinamento delle risorse, Vedi Sezione 4.5.
> - Per il confronto tra allocazione contigua e indicizzata, Vedi Sezione 11.1.

## 18. Laboratorio di Sistemi: Programmazione POSIX

### 18.1 Ambiente di Sviluppo e Compilazione
Il processo di compilazione in C separa le fasi di traduzione e collegamento.
- **Preprocessore**: Espande macro e include header (`#include`, `#define`).
- **Compilatore**: Traduce il codice sorgente in assembly.
- **Linker**: Unisce i file oggetto (`.o`) nelle librerie finali.

**Comandi GCC Fondamentali**:
```bash
gcc -c file.c          # Compila in file oggetto (senza linking)
gcc file.c -o app      # Compila e linka in eseguibile
gcc file.c -lpthread   # Necessario per linkare le librerie dei thread
gcc file.c -O2         # Ottimizzazione del codice (per misurare le performance reali)
```

### 18.2 Gestione dei Processi e I/O di Basso Livello
Le system call POSIX offrono un controllo fine sui file descriptor.

**Apertura File (`open`)**:
- `O_CREAT`: Crea il file se non esiste (richiede permessi es. `0644`).
- `O_TRUNC`: Tronca il file a lunghezza zero (sovrascrittura).
- `O_APPEND`: Posiziona l'offset alla fine prima di ogni scrittura (atomico).

**Spostamento Offset (`lseek`)**:
- `lseek(fd, offset, SEEK_SET)`: Assoluto dall'inizio.
- `lseek(fd, offset, SEEK_CUR)`: Relativo alla posizione corrente.
- **Sparse Files**: Usare `lseek` per saltare grandi regioni senza scrivere crea "buchi" che non occupano spazio su disco.

### 18.3 Programmazione Concorrente (Thread e Sincronizzazione)
**Creazione Thread**:
```c
pthread_t tid;
pthread_create(&tid, NULL, funzione_start, argomento);
pthread_join(tid, NULL); // Fondamentale per evitare race condition alla terminazione
```

**Protezione Sezioni Critiche**:
- **Mutex**: Per l'accesso esclusivo a variabili condivise.
  ```c
  pthread_mutex_lock(&m);
  // Sezione critica (es. counter++)
  pthread_mutex_unlock(&m);
  ```
- **Condition Variables**: Per la comunicazione tra thread (produttore-consumatore).
  - Regola d'oro: Usare sempre un ciclo `while` per verificare la condizione dopo il `wait`.

### 18.4 Comunicazione tra Processi (IPC)
- **Pipe Anonime**: `pipe(fd)` crea due file descriptor (lettura/scrittura) per processi imparentati. La `read()` blocca se la pipe è vuota; la `write()` genera `SIGPIPE` se non ci sono lettori.
- **Shared Memory (`mmap`)**:
  1. `shm_open()`: Crea/apre oggetto di memoria.
  2. `ftruncate()`: Imposta dimensione.
  3. `mmap()`: Mappa nello spazio virtuale del processo.
  - Richiede sincronizzazione esterna (es. semafori) poiché `mmap` da sola non è atomica.

---

## 19. Analisi degli Algoritmi Critici

### 19.1 Soluzione di Peterson (Mutua Esclusione Software)
Soluzione teorica per due processi $P_i$ e $P_j$ che soddisfa mutua esclusione, progresso e bounded waiting.

**Logica**:
1. Ogni processo imposta `flag[i] = TRUE` (voglio entrare).
2. Cede il turno all'altro: `turn = j`.
3. Entrano solo se l'altro non vuole entrare oppure il turno è loro.

```c
// Codice per Pi
flag[i] = TRUE;
turn = j;
while (flag[j] && turn == j) { /* busy waiting */ }
// Sezione Critica
flag[i] = FALSE;
```

### 19.2 Problema dei 5 Filosofi
Soluzione che evita il deadlock usando una variabile di condizione per ogni filosofo e uno stato esplicito.
- **Stati**: `THINKING`, `HUNGRY`, `EATING`.
- **Funzione `test(i)`**: Verifica se il filosofo $i$ può mangiare (vicini non stanno mangiando). Se sì, lo mette in `EATING` e fa `signal(&cond[i])`.
- **Prevenzione Deadlock**: L'uso di un mutex globale per modificare gli stati e le condition variable individuali impediscono l'attesa circolare indefinita.

### 19.3 Algoritmo Clock (Sostituzione Pagine)
Approssimazione efficiente di LRU usata nei SO moderni.
1. Le pagine sono in una lista circolare con un bit di riferimento (R).
2. **Hand (Lancetta)**: Scorre le pagine.
   - Se `R=1`: La pagina è stata usata di recente. Si imposta `R=0` (si dà una "seconda chance") e si passa alla successiva.
   - Se `R=0`: La pagina non è usata. Viene scelta come **vittima**.
3. **Enhanced Clock**: Considera anche il bit Dirty (M). Preferisce espellere pagine con `(R=0, M=0)` (non usate e non modificate) per evitare costose scritture su disco.

---

## 20. Sottosistema I/O e Dispositivi

### 20.1 Classificazione dei Dispositivi
| Tipo | Descrizione | Esempi | Operazioni |
|---|---|---|---|
| **Block Devices** | Accesso randomico a blocchi fissi. | HDD, SSD, USB | `read`, `write`, `seek` |
| **Character Devices** | Flusso sequenziale byte per byte. | Tastiera, Mouse, TTY | `read`, `write` |
| **Network Devices** | Comunicazione tramite socket. | Ethernet, WiFi | `send`, `recv`, `bind` |

### 20.2 Line Discipline
Livello software tra il driver del terminale e l'utente.
- Gestisce l'editing della riga (backspace, cancellazione).
- Converte caratteri di controllo (es. `Ctrl+C` → `SIGINT`).
- Permette di configurare il comportamento del terminale (echo, canonical mode).

---

## 21. Manuale di Calcolo per l'Esame

### 21.1 Metriche di Scheduling
- **Turnaround Time** = Tempo Fine - Tempo Arrivo.
- **Waiting Time** = Turnaround Time - Burst Time.
- **Response Time** = Tempo Prima Esecuzione - Tempo Arrivo.

### 21.2 Gestione della Memoria
**Calcolo Bit Page Table**:
- Numero bit Indirizzo Logico = $\log_2(\text{Spazio Virtuale})$.
- Numero bit Offset = $\log_2(\text{Dimensione Pagina})$.
- Numero bit Indice Pagina = Bit Logico - Bit Offset.
- Numero Entry Page Table = $2^{\text{Bit Indice}}$.

**Effective Access Time (EAT)**:
$$EAT = \alpha(\epsilon + T_m) + (1-\alpha)(\epsilon + 2T_m)$$
*(Dove $\alpha$ = hit rate, $\epsilon$ = tempo TLB, $T_m$ = tempo memoria)*.

### 21.3 Affidabilità e Errori
**MTTF di un Array**:
Se un disco ha MTTF $M$ e l'array ha $N$ dischi:
$$MTTF_{sistema} = \frac{M}{N}$$

**Codice di Hamming (ECC)**:
Per correggere errori a singolo bit su $k$ bit di dati, servono $r$ bit di ridondanza tali che:
$$2^r \geq k + r + 1$$

---

## 22. Glossario Rapido dei Termini Tecnici

- **Context Switch**: Cambio di processo; salva stato vecchio, carica stato nuovo.
- **Deadlock**: Attesa circolare indefinita tra processi per risorse.
- **Page Fault**: Eccezione generata quando si accede a pagina non in RAM.
- **Thrashing**: Saturazione della CPU in gestione swap per mancanza di RAM.
- **VFS (Virtual File System)**: Astrazione che unifica diversi file system.
- **Working Set**: Insieme di pagine attive di un processo in un intervallo di tempo.
- **Copy-on-Write**: Ottimizzazione che ritarda la copia della memoria alla prima scrittura.

---

> **Nota Finale per lo Studio**:
> Per l'esame scritto, concentratevi sulla capacità di **tracciare l'esecuzione** di algoritmi di scheduling (disegnare il Gantt chart) e di gestione della memoria (calcolare indirizzi fisici da logici). Per l'orale, preparate bene le differenze concettuali (es. Mutex vs Semaforo, Hard Link vs Soft Link, Process vs Thread) e le motivazioni architetturali (es. perché si usa la TLB, perché si usa il Journaling).
