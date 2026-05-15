# Trascrizione Lezione: Architetture di Memoria (Intel x86, ARM), Memoria Virtuale e Demand Paging

**Data:** 28 aprile 2026
**Argomento:** Segmentazione Intel x86 (32/64-bit), Architettura ARM v8, Memoria Virtuale, Demand Paging, Page Fault, Copy-on-Write e Introduzione alla Sostituzione di Pagina.

---

### 1. Segmentazione e Paging nelle Architetture Intel

Sebbene la segmentazione pura sia un modello superato, rimane come retaggio storico nelle architetture Intel, spesso combinata con il paging.

#### Intel a 32-bit (x86)
L'architettura Intel a 32-bit utilizza un meccanismo ibrido:
1.  **Segmentation Unit:** Gli indirizzi logici passano prima attraverso un'unità di segmentazione.
    *   L'indirizzo logico è composto da un **Selettore di Segmento** (16 bit) e un **Offset** (32 bit). Totale: 48 bit logici.
    *   Il selettore indica:
        *   Indice nella tabella dei descrittori.
        *   Bit TI (Table Indicator): distingue tra **LDT** (Local Descriptor Table, specifica del processo) e **GDT** (Global Descriptor Table, condivisa/kernel/librerie).
        *   Bit di protezione (R/W).
    *   L'unità di segmentazione somma la **Base del Segmento** all'Offset, producendo un **Indirizzo Lineare** a 32 bit.
    *   *Nota storica:* I processori fino all'80286 usavano solo segmentazione. Dal 386 in poi, la segmentazione è affiancata dal paging. Nei SO moderni, la segmentazione è spesso impostata in "flat mode" (base = 0), rendendola trasparente per concentrarsi sul paging.

2.  **Paging Unit:** L'indirizzo lineare a 32 bit viene poi paginato.
    *   **Pagine da 4 KB:** Paging a due livelli.
        *   10 bit per Page Directory (esterno).
        *   10 bit per Page Table (interno).
        *   12 bit per Offset ($2^{12} = 4$ KB).
    *   **Pagine da 4 MB:** Paging a un livello.
        *   10 bit per Page Directory.
        *   22 bit per Offset ($2^{22} = 4$ MB).
    *   Il registro **CR3** punta alla Page Directory Base. Durante il context switch, il SO aggiorna CR3 con la directory del nuovo processo.

#### Estensione degli Indirizzi Fisici (PAE - Physical Address Extension)
Per indirizzare più di 4 GB di RAM fisica su architetture a 32-bit, Intel ha introdotto il PAE.
*   **Il Trucco:** Si aumentano le dimensioni delle entry nelle Page Table da 32 a 64 bit.
*   Questo permette di usare **24 bit** per l'indirizzo del frame fisico (invece di 20), consentendo di indirizzare fino a $2^{36}$ byte (64 GB) di RAM fisica.
*   Ogni processo continua a vedere solo 4 GB di spazio virtuale, ma il sistema può mappare molti più processi contemporaneamente nella RAM fisica estesa.
*   Le tabelle diventano più "larghe" (entry a 64 bit), aumentando l'overhead di memoria per le strutture di controllo.

#### Intel a 64-bit (AMD64 / x86-64)
Lo standard a 64-bit (inizialmente sviluppato da AMD) supporta teoricamente $2^{64}$ byte (16 Exabyte), ma attualmente implementa **48 bit** per gli indirizzi virtuali.
*   **Struttura Gerarchica a 4 Livelli:**
    1.  PML4 (Page Map Level 4)
    2.  PDPT (Page Directory Pointer Table)
    3.  PD (Page Directory)
    4.  PT (Page Table)
    5.  Offset (12 bit per pagine da 4 KB).
*   Supporta anche **Huge Pages** (2 MB, 1 GB) che riducono i livelli di gerarchia necessari.
*   **Page Address Extension:** Anche a 64-bit, si può estendere l'indirizzamento fisico fino a 52 bit per gestire RAM fisiche molto grandi, mantenendo lo spazio virtuale a 48 bit.

---

### 2. Architettura ARM v8 (64-bit)

ARM v8 utilizza un approccio simile ma con alcune specificità:
*   **Granularità delle Pagine:** Supporta pagine da 4 KB, 16 KB e 64 KB.
*   **Regioni:** Oltre alle pagine, esiste il concetto di "Region", utile per mappare aree di memoria speciali (es. I/O memory-mapped) o riservare blocchi grandi (1 GB, 2 MB) senza passare per tutti i livelli di paging.
*   **Gerarchia di Paging:** Fino a 4 livelli per pagine piccole. Per regioni grandi (1 GB), ci si ferma al primo livello.
*   **TLB (Translation Lookaside Buffer):**
    *   Separate per Istruzioni (I-TLB) e Dati (D-TLB) nei livelli L1 (più veloci).
    *   Una TLB unificata L2 (più capiente).
    *   **Paging Structure Cache:** Alcune architetture ARM hanno cache dedicate per le strutture delle page table, riducendo il costo del "page table walk" in caso di TLB miss. La gerarchia delle cache dati (L1, L2, L3) aiuta ulteriormente a recuperare le entry delle tabelle senza accedere alla RAM principale.

> **Strumento Pratico:** Su Linux, il comando `pmap` permette di visualizzare il layout di memoria logica di un processo, mostrando permessi, dirty bits e mapping fisico/logico.

---

### 3. Memoria Virtuale e Demand Paging

La **Memoria Virtuale** disaccoppia lo spazio di indirizzamento logico (visto dal processo) dalla memoria fisica (RAM).
*   Permette di eseguire processi con spazi di indirizzamento più grandi della RAM disponibile.
*   Aumenta il grado di multiprogrammazione caricando in RAM solo le parti attive dei processi.

#### Demand Paging (Paginazione su Richiesta)
Invece di caricare l'intero processo in RAM all'avvio, le pagine vengono caricate solo quando necessarie.
*   **Pure Demand Paging:** All'avvio, nessuna pagina è in RAM. La Page Table ha tutti i bit di validità impostati su "Invalid".
*   **Page Fault:** Quando la CPU accede a una pagina non presente in RAM:
    1.  La MMU rileva il bit "Invalid" nella Page Table.
    2.  Genera un trap (interruzione) al Sistema Operativo.
    3.  Il SO verifica se l'accesso è legale (controllo protezione nel PCB). Se illegale -> Abort.
    4.  Se legale, il SO cerca la pagina nel **Backing Store** (memoria secondaria/disc swap).
    5.  Trova un **Frame Libero** in RAM.
    6.  Schedula un'operazione di I/O per leggere la pagina dal disco al frame.
    7.  Aggiorna la Page Table (imposta bit "Valid", scrive numero del frame).
    8.  **Restart dell'Istruzione:** Riavvia l'istruzione che ha causato il fault.

#### Gestione del Restart delle Istruzioni
Il restart deve essere atomico e coerente.
*   Per istruzioni semplici (load/store), basta ripetere l'operazione.
*   Per istruzioni complesse (es. spostamento blocchi di memoria), il SO deve garantire che lo stato sia ripristinabile (undo delle operazioni parziali) o pre-caricare tutte le pagine necessarie prima di iniziare l'istruzione complessa.

#### Performance del Demand Paging
Il Page Fault è estremamente costoso rispetto all'accesso in RAM.
*   **Tempo Accesso RAM:** ~200 ns.
*   **Tempo Servizio Page Fault:** ~8 ms (incluso seek time disco, trasferimento, interrupt).
*   **Calcolo EAT (Effective Access Time):**
    $$ EAT = (1 - p) \cdot T_{mem} + p \cdot T_{fault} $$
    Dove $p$ è la probabilità di page fault.
*   **Impatto:** Se $p = 1/1000$, l'EAT sale da 200 ns a ~8.2 $\mu$s (rallentamento di ~40x).
*   Per mantenere una degradazione delle performance < 10%, la probabilità di page fault deve essere inferiore a **1 ogni 400.000 accessi**.
*   **Ottimizzazioni:**
    *   Swap space dedicato (non file system generico) per accessi più rapidi.
    *   Nei sistemi mobile (Flash), si evita lo swap su disco per le pagine "anonime" (dati modificabili) per preservare la vita della memoria; si usa invece la compressione in RAM.

---

### 4. Copy-on-Write (COW) e Fork

La chiamata di sistema `fork()` crea un processo figlio duplicando il padre.
*   **Problema:** Duplicare fisicamente tutte le pagine è costoso e lento.
*   **Soluzione (Copy-on-Write):**
    *   Padre e figlio condividono inizialmente le stesse pagine fisiche in modalità **Read-Only**.
    *   Le strutture logiche (PCB, Page Table) sono duplicate, ma puntano agli stessi frame.
    *   Solo quando uno dei due processi tenta di **scrivere** su una pagina condivisa, scatta un fault di protezione.
    *   Il SO alloca un nuovo frame, copia la pagina, e aggiorna la Page Table del processo scrivente.
    *   Questo ottimizza drasticamente le prestazioni se il figlio esegue subito `exec()` (che sostituisce lo spazio di indirizzamento), poiché molte pagine non vengono mai copiate.

*   **vfork (Virtual Fork):** Variante obsoleta/rara dove il figlio condivide *completamente* lo spazio di indirizzamento del padre (inclusa la scrittura) fino all'`exec()`. È pericolosa perché il figlio può corrompere lo stato del padre.

---

### 5. Gestione dei Frame Liberi e Sostituzione di Pagina

Il SO deve mantenere una **Lista di Frame Liberi**.
*   I frame liberi vengono spesso **azzerati** al momento dell'allocazione (per sicurezza), non quando vengono liberati, per permettere un eventuale recupero tardivo se il riferimento era errato.
*   Il SO mantiene un **Pool di Frame Liberi** sopra una certa soglia. Se il pool scende sotto la soglia minima, un demone di sistema inizia a liberare pagine ("sfoltimento") fino a raggiungere la soglia massima, evitando oscillazioni continue.

#### Algoritmi di Sostituzione di Pagina (Page Replacement)
Se non ci sono frame liberi durante un Page Fault, il SO deve scegliere una **Pagina Vittima** da espellere.
1.  Scegliere la vittima.
2.  Se il **Dirty Bit** della vittima è settato (pagina modificata), scriverla sul Backing Store (costoso). Se non è settato (Clean), sovrascrivere direttamente (veloce, esiste già copia su disco).
3.  Liberare il frame.
4.  Caricare la nuova pagina richiesta nel frame libero.
5.  Aggiornare le Page Table (Vittima -> Invalid, Nuova -> Valid).

*Nota:* Nei sistemi reali, la sostituzione avviene preventivamente tramite il demone di sfoltimento, non durante il fault critico, per nascondere la latenza di I/O. Gli algoritmi specifici di scelta della vittima (LRU, FIFO, ecc.) saranno trattati nella prossima lezione.
