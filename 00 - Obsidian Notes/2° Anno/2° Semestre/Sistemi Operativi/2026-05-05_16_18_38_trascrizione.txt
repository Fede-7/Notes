# Trascrizione Lezione: Implementazioni SO (Linux, Windows, Solaris), Dischi Magnetici vs SSD, Scheduling del Disco e Error Correction

**Data:** 5 Maggio 2026
**Argomento:** Algoritmi di Sostituzione nei SO moderni, Struttura Fisica dei Dischi (HDD/SSD), Disk Scheduling Algorithms, Error Detection & Correction (Parity, Hamming).

---

### 1. Implementazione della Sostituzione di Pagina nei Sistemi Operativi Moderni

Gli algoritmi LRU puri sono troppo costosi. I SO moderni usano approssimazioni basate sul bit di riferimento (*Reference Bit*) e liste di pagine.

#### A. Linux: Active/Inactive Lists (Approximated LRU)
Linux utilizza un meccanismo di **Global Page Replacement** con due liste principali:
1.  **Active List:** Pagine recentemente utilizzate (Reference Bit = 1).
2.  **Inactive List:** Pagine non utilizzate di recente (Reference Bit = 0).

*   **Funzionamento:**
    *   Quando una pagina viene accessibile, il suo Reference Bit viene settato a 1 e la pagina viene spostata in testa alla *Active List*.
    *   Periodicamente, il SO scandisce la *Active List*: se il Reference Bit è ancora 1, viene resettato a 0 e la pagina rimane attiva; se è già 0, la pagina viene spostata nella *Inactive List*.
    *   Un demone (*kswapd*) monitora il numero di frame liberi. Se scende sotto una soglia minima, il demone scandisce la *Inactive List* e libera le pagine (scrivendole su swap se sporche) fino a raggiungere una soglia massima.
    *   **Recupero:** Una pagina nella *Inactive List* o persino nel pool libero può essere "resuscitata" se riferita prima di essere sovrascritta fisicamente.

#### B. Windows: Working Set Trimmer
Windows supporta Demand Paging, Copy-on-Write, Compressione e **Clustering** (caricamento preemptivo di pagine adiacenti: cluster di 3 pagine per dati, 7 per codice).
*   **Gestione Working Set:** Ogni processo ha un *Minimum* e un *Maximum Working Set*. Questi sono limiti euristici, non vincoli stretti (a meno di configurazioni specifiche).
*   **Automatic Working Set Trimmer:**
    *   Monitora la memoria libera globale.
    *   Se la memoria libera scende sotto soglia, il trimmer rimuove pagine dai processi che eccedono il loro *Minimum Working Set*.
    *   **Priorità:** Vengono sacrificate prima le pagine di processi grandi e inattivi, rispetto a quelli piccoli e attivi.
    *   Se necessario, può scavare sotto il minimo working set per garantire la stabilità del sistema globale.

#### C. Solaris: Two-Hand Clock Algorithm
Solaris utilizza un algoritmo **Clock a due lancette** (Front Hand e Back Hand) per approssimare LRU con sostituzione globale/locale.
*   **Struttura:** Una lista circolare di pagine.
*   **Front Hand (Scout):** Scorre velocemente, azzerando il Reference Bit delle pagine incontrate ("rendendole vulnerabili").
*   **Back Hand (Reaper):** Segue la Front Hand a una distanza chiamata **Hand Spread**. Se trova una pagina con Reference Bit = 0 (non rireferenziata nel frattempo), la seleziona come vittima e la mette nella Free List.
*   **Adattività:**
    *   **Scan Rate:** La velocità di scansione aumenta quando la memoria libera scende sotto soglie critiche (`lotsfree` -> `desfree` -> `minfree`).
    *   **Hand Spread:** La distanza tra le lancette si riduce sotto alta pressione, diminuendo la "seconda chance" data alle pagine.
    *   Questo permette al sistema di adattarsi dinamicamente al carico di lavoro.

---

### 2. Memoria Secondaria: HDD vs SSD

Il Sistema Operativo vede la memoria secondaria come un array lineare di **Blocchi Logici** (Logical Block Addressing - LBA). Il mapping fisico è gestito dal controller del dispositivo.

#### A. Hard Disk Drive (HDD) - Memoria Magnetica
Dispositivo meccanico con piatti rotanti e testine mobili.
*   **Struttura Fisica:**
    *   **Piatti (Platters):** Dischi magnetici.
    *   **Tracce (Tracks):** Cerchi concentrici sui piatti.
    *   **Settori (Sectors):** Suddivisioni delle tracce (unità minima fisica, es. 512B o 4KB).
    *   **Cilindri (Cylinders):** Insieme di tracce alla stessa posizione radiale su tutti i piatti.
*   **Componenti del Tempo di Accesso:**
    1.  **Seek Time:** Tempo per spostare la testina sul cilindro corretto (dominante, 3-12 ms).
    2.  **Rotational Latency:** Tempo per aspettare che il settore ruoti sotto la testina (media = metà del tempo di rotazione).
        *   Es. 7200 RPM -> ~4.17 ms latenza media.
    3.  **Transfer Time:** Tempo per leggere/scrivere i dati (dipende dalla densità e velocità di rotazione).
*   **Organizzazione Dati:**
    *   **ZBR (Zone Bit Recording):** Le tracce esterne hanno più settori di quelle interne per mantenere una densità di registrazione costante. Di conseguenza, la velocità di trasferimento è maggiore sulle tracce esterne.
    *   I SO tendono a posizionare i dati frequenti sull'esterno del disco per sfruttare questa maggiore velocità.

#### B. Solid State Drive (SSD) - Memoria Non Volatile (NAND Flash)
Dispositivo a stato solido, elettronico, senza parti meccaniche.
*   **Caratteristiche:**
    *   Molto più veloce degli HDD (nessun Seek Time o Rotational Latency).
    *   **Limiti di Scrittura:** Le celle NAND devono essere cancellate (operazione lenta a livello di *Blocco*) prima di essere riscritte (operazione a livello di *Pagina*).
    *   **Usura (Endurance):** Ogni cella ha un numero limitato di cicli di cancellazione/scrittura (P/E cycles). Misurato in DWPD (Drive Writes Per Day).
    *   **Flash Translation Layer (FTL):** Il controller mappa i Blocchi Logici ai Blocchi Fisici. Gestisce:
        *   **Wear Leveling:** Distribuisce le scritture uniformemente per evitare l'usura prematura di alcune celle.
        *   **Garbage Collection:** Ricompatta i dati validi e cancella i blocchi contenenti dati invalidi per liberare spazio scrivibile.
        *   **Bad Block Management:** Marca le celle deteriorate come inutilizzabili.

> **Nota:** Per gli SSD, lo scheduling del disco tradizionale (basato sul seek time) è inutile. Si usa spesso **NOOP** (FIFO semplice) o deadline-based, poiché l'ordine fisico non influisce significativamente sulle prestazioni di accesso random.

---

### 3. Algoritmi di Disk Scheduling (Per HDD)

L'obiettivo è minimizzare il **Seek Time** totale (movimento della testina). Il SO mantiene una coda di richieste I/O.

#### A. FCFS (First-Come, First-Served)
*   Serve le richieste nell'ordine di arrivo.
*   **Svantaggio:** Movimento erratico della testina, seek time medio elevato. Prestazioni scadenti sotto carico.

#### B. SSTF (Shortest Seek Time First)
*   Serve sempre la richiesta più vicina alla posizione attuale della testina.
*   **Vantaggio:** Minimizza il seek time totale.
*   **Svantaggio:** Rischio di **Starvation**. Le richieste lontane potrebbero non essere mai servite se arrivano continuamente richieste vicine alla testina.

#### C. SCAN (Algoritmo dell'Ascensore)
*   La testina si muove in una direzione (es. verso l'interno), servendo tutte le richieste incontrate.
*   Raggiunto l'estremo, inverte la direzione e serve le richieste nel ritorno.
*   **Vantaggio:** Più equo di SSTF, nessuna starvation.
*   **Svantaggio:** Le richieste agli estremi possono avere tempi di attesa doppi rispetto a quelle centrali.

#### D. C-SCAN (Circular SCAN)
*   La testina si muove solo in una direzione (es. verso l'interno), servendo le richieste.
*   Raggiunto l'estremo, torna rapidamente all'inizio (esterno) **senza servire richieste** nel viaggio di ritorno.
*   **Vantaggio:** Tratta i cilindri come un anello circolare. Fornisce un tempo di attesa più uniforme. Sfrutta il fatto che le tracce esterne sono più veloci/dense.

#### E. LOOK e C-LOOK
*   Varianti ottimizzate di SCAN e C-SCAN.
*   La testina non arriva fino all'estremo fisico del disco, ma si ferma all'**ultima richiesta presente** in quella direzione, poi inverte (LOOK) o torna all'inizio (C-LOOK).
*   Evita movimenti inutili verso cilindri vuoti.

> **Esempio Pratico (Esame):** Date una sequenza di richieste (es. 98, 183, 37, 122, 14, 124, 65, 67) e la posizione iniziale (53), calcolare il movimento totale della testina per ogni algoritmo.
> *   SSTF: ~236 cilindri.
> *   FCFS: ~640 cilindri.
> *   SCAN/C-SCAN: Valori intermedi, dipendenti dalla direzione iniziale.

#### F. Scheduling in Linux (CFQ/Deadline)
Linux usa code multiple con priorità:
*   Code separate per Lettura (più urgenti) e Scrittura.
*   All'interno delle code, usa un mix di priorità e ordinamento sector-based (simile a C-LOOK).
*   **Deadline:** Se una richiesta aspetta troppo (es. 500ms per read, 5s per write), viene promossa in una coda FIFO per evitare starvation.

---

### 4. Rilevamento e Correzione degli Errori

I dispositivi di storage sono soggetti a degradazione. Il SO e i controller usano codici per garantire l'integrità dei dati.

#### A. Parity Bit (Rilevamento)
*   Aggiunge un bit extra a un byte (o parola) per rendere il numero totale di bit '1' pari (o dispari).
*   **Limite:** Rileva solo errori a **singolo bit**. Se due bit flippano, la parità resta corretta e l'errore non viene rilevato.
*   Utile per rilevare danni, ma non per correggerli.

#### B. Error Correction Code (ECC) - Es. Codice di Hamming
*   Aggiunge più bit di controllo (ridondanza) ai dati.
*   Permette non solo di **rilevare** errori, ma anche di **correggerli** (fino a un certo numero di bit errati, tipicamente 1 bit per parola nel caso base).
*   **Formula di Hamming:** Per $k$ bit di dati, servono $r$ bit di ridondanza tali che $2^r \ge k + r + 1$.
*   **SEC-DED (Single Error Correction, Double Error Detection):** Codici più avanzati che correggono 1 bit e rilevano 2 bit.
*   **Gestione Bad Blocks:** Se l'ECC non riesce a correggere un errore, il blocco viene marcato come "Bad". Il controller remappa logicamente quel blocco su uno spare sector (Sector Slipping/Remapping), mantenendo la continuità logica degli indirizzi LBA.

---

*Fine della lezione.*
