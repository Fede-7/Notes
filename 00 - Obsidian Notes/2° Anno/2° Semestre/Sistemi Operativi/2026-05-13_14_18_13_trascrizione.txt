# Trascrizione Lezione: Metodi di Allocazione dei File, FAT, Inode e Cache Unificata

**Data:** 13 Maggio 2026
**Argomento:** Allocazione Contigua, Concatenata (Linked), Indicizzata (Indexed); FAT; Unix Inode (Direct/Indirect Pointers); NTFS MFT; Gestione Spazio Libero (Bitmap, Linked List); Double Caching e Page Cache.

---

### 1. Metodi di Allocazione dei File

Il metodo di allocazione determina come i blocchi di un file sono distribuiti sul disco e come il SO li recupera. Esistono tre approcci principali.

#### A. Allocazione Contigua (Contiguous Allocation)
Ogni file occupa un insieme di blocchi contigui sul disco.
*   **Metadati:** Indirizzo del blocco iniziale + Lunghezza (numero di blocchi).
*   **Vantaggi:**
    *   **Accesso Sequenziale Ottimale:** Minimizza il *Seek Time* della testina (HDD).
    *   **Accesso Diretto (Random) Semplice:** Per accedere al byte $B$, si calcola:
        $$ \text{Blocco} = \lfloor B / \text{BlockSize} \rfloor $$
        $$ \text{Offset} = B \mod \text{BlockSize} $$
        Il SO salta direttamente al blocco calcolato.
*   **Svantaggi:**
    *   **Frammentazione Esterna:** Richiede algoritmi di allocazione (First-Fit, Best-Fit) e compattazione periodica (costosa su disco).
    *   **Dimensione Predefinita:** Difficile espandere un file se i blocchi adiacenti sono occupati. Soluzioni: *Extents* (liste di regioni contigue) o spostamento del file.
*   **Utilizzo:** Usato raramente per file generali nei moderni FS, ma concettualmente simile agli *Extents* in ext4 o XFS.

#### B. Allocazione Concatenata (Linked Allocation)
Ogni file è una lista concatenata di blocchi sparsi sul disco. Ogni blocco contiene un puntatore al successivo.
*   **Metadati:** Puntatore al primo blocco e all'ultimo blocco.
*   **Vantaggi:**
    *   **Nessuna Frammentazione Esterna:** I blocchi possono essere ovunque.
    *   **Espansione Facile:** Basta aggiungere un blocco libero alla fine della lista.
*   **Svantaggi:**
    *   **Accesso Diretto Lento:** Per accedere al blocco $N$, bisogna scorrere i primi $N-1$ blocchi (accesso sequenziale obbligatorio attraverso i puntatori).
    *   **Overhead di Spazio:** Parte di ogni blocco è dedicata al puntatore (non ai dati).
    *   **Affidabilità:** Se un puntatore si corrompe, la catena si interrompe e il resto del file è perso.
*   **Variante: File Allocation Table (FAT):**
    *   Risolve il problema dell'accesso diretto e dell'affidabilità spostando i puntatori fuori dai blocchi dati.
    *   Una tabella centrale (FAT) in memoria (cacheata) mappa ogni blocco al successivo.
    *   **Pro:** Accesso diretto più veloce (scansione della tabella in RAM), affidabilità maggiore.
    *   **Contro:** La FAT deve essere tenuta in RAM per performance; limita la dimensione massima del disco in base alla grandezza delle entry (12-bit, 16-bit, 32-bit).
    *   **Utilizzo:** USB drive, schede SD, partizioni EFI/Boot (compatibilità universale).

#### C. Allocazione Indicizzata (Indexed Allocation)
Ogni file ha un **blocco indice** (o struttura simile) che contiene un array di puntatori ai blocchi dati.
*   **Metadati:** Puntatore al blocco indice.
*   **Vantaggi:**
    *   **Accesso Diretto Efficiente:** Si legge il blocco indice (in RAM se cacheato) e si salta direttamente al blocco dati desiderato.
    *   **Nessuna Frammentazione Esterna.**
*   **Svantaggi:**
    *   **Overhead Indice:** Ogni file richiede almeno un blocco per l'indice (spreco per file piccoli).
    *   **Limite Dimensione File:** Dipende dalla dimensione del blocco indice e dei puntatori.

---

### 2. Implementazioni Moderne: Unix Inode vs NTFS MFT

#### A. Unix/Linux: Inode e Puntatori Multi-Livello
Per bilanciare efficienza per file piccoli e grandi, gli inode usano una struttura ibrida:
1.  **Puntatori Diretti (Direct Pointers):** Puntano direttamente ai blocchi dati. Veloci per file piccoli.
2.  **Puntatore Indiretto Singolo (Single Indirect):** Punta a un blocco che contiene solo puntatori ad altri blocchi dati.
3.  **Puntatore Indiretto Doppio (Double Indirect):** Punta a un blocco di indici, che puntano a blocchi di indici, che puntano ai dati.
4.  **Puntatore Indiretto Triplo (Triple Indirect):** Tre livelli di indicizzazione per file enormi.

*   **Calcolo Accessi Disco:**
    *   Direct: 1 accesso (dato).
    *   Single Indirect: 2 accessi (1 indice + 1 dato).
    *   Double Indirect: 3 accessi (2 indici + 1 dato).
    *   *Nota:* Gli inode sono cacheati in RAM dopo l'`open()`, quindi gli accessi agli indici sono spesso evitati grazie alla cache.

#### B. Windows: NTFS e Master File Table (MFT)
NTFS usa un approccio centralizzato.
*   **MFT:** Un database relazionale contenente un record per ogni file e directory.
*   **Record MFT:** Contiene attributi (nome, sicurezza, timestamp) e la mappa dei blocchi (spesso usando *Extents* per efficienza).
*   **Journaling:** NTFS include journaling nativo per garantire la consistenza dei metadati in caso di crash.

---

### 3. Gestione dello Spazio Libero

Il SO deve tenere traccia dei blocchi non allocati.

1.  **Bitmap (Vettore di Bit):**
    *   Un bit per ogni blocco sul disco (1 = libero, 0 = occupato).
    *   **Pro:** Trovare blocchi contigui è facile (ricerca di sequenze di 1). Efficiente per dischi pieni/vuoti.
    *   **Contro:** Occupa memoria RAM significativa (es. 32 MB per un disco da 1 TB con blocchi da 4KB).
2.  **Lista Concatenata di Blocchi Liberi:**
    *   Il primo blocco libero punta al secondo, ecc.
    *   **Pro:** Nessun overhead in RAM (solo un puntatore iniziale).
    *   **Contro:** Lenta per trovare blocchi contigui; richiede lettura disco per traversare la lista.
3.  **Raggruppamento (Grouping):**
    *   Il primo blocco libero contiene indirizzi di $N$ blocchi liberi successivi. Combina vantaggi di bitmap e liste.

---

### 4. Evoluzione dei File System Linux (Ext2/3/4)

*   **Ext2 (Extended File System):** Basato su UFS/BSD FFS. Introduce i **Block Groups**.
    *   Ogni Block Group contiene: Superblock, Bitmap Inode, Bitmap Blocco, Tabella Inode, Blocchi Dati.
    *   **Obiettivo:** Località dei dati. Metadati e dati dello stesso file sono vicini fisicamente, riducendo il seek time su HDD.
*   **Ext3:** Aggiunge **Journaling**.
    *   Registra le modifiche ai metadati in un "journal" prima di applicarle al FS principale.
    *   Permette un recovery rapido dopo un crash senza dover scandire tutto il disco (fsck).
*   **Ext4:** Miglioramenti prestazioni e capacità.
    *   Supporta *Extents* (invece di puntatori singoli block-mapping) per ridurre la frammentazione e migliorare le prestazioni su file grandi.
    *   Allocazione ritardata (*Delayed Allocation*) per ottimizzare il posizionamento dei blocchi.

---

### 5. Caching e Performance: Il Problema del Double Caching

L'accesso ai file coinvolge due livelli di cache nel kernel Linux, potenzialmente ridondanti:

1.  **Buffer Cache (Page Cache):** Cache della memoria virtuale. I blocchi del file vengono caricati in pagine di RAM gestite dal subsistema di paging.
2.  **File System Cache:** Cache specifica per metadati e operazioni I/O del FS.

**Problema (Double Caching):**
Se un file viene accessibile sia tramite I/O standard (`read/write`) che tramite *Memory Mapped I/O* (`mmap`), i dati potrebbero risiedere in due cache separate o richiedere copie multiple, sprechando RAM e cicli CPU per mantenere la coerenza.

**Soluzione: Unified Page Cache**
I moderni kernel Linux usano una **Page Cache unificata**.
*   I blocchi del disco sono cacheati direttamente nelle pagine della memoria virtuale.
*   Sia le system call `read/write` che `mmap` accedono alle stesse pagine in RAM.
*   Elimina la duplicazione dei dati e semplifica la coerenza.

**Algoritmi di Sostituzione per File:**
*   L'algoritmo LRU standard non è ottimale per l'accesso sequenziale ai file (una pagina letta sequenzialmente probabilmente non sarà riletta a breve).
*   Il kernel marca le pagine lette sequenzialmente come "freddas" o le rimuove rapidamente dalla cache attiva per fare spazio a dati più probabili da riutilizzare.
*   **Read-Ahead (Pre-fetching):** Il kernel legge blocchi successivi anticipatamente durante accessi sequenziali per nascondere la latenza del disco.

---

*Fine della lezione.*
