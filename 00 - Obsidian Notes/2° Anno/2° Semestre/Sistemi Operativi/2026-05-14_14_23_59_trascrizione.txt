# Trascrizione Lezione: Consistenza del File System (Journaling), Architettura VFS e Sottosistema I/O

**Data:** 14 Maggio 2026
**Argomento:** Recupero da Crash, Journaling, Backup, Architettura a Strati (VFS, Logical FS, Device Drivers), Classificazione Dispositivi (Block/Char/Network), Line Discipline (TTY).

---

### 1. Consistenza del File System e Recupero da Crash

Le operazioni sul file system modificano frequentemente i **metadati** (directory, inode, bitmap spazio libero). Poiché queste scritture sono asincrone (cacheate in RAM e scritte su disco in batch), un crash improvviso può lasciare il file system in uno stato inconsistente (es. inode allocato ma non presente in nessuna directory).

#### Metodi di Protezione
1.  **Bit di "Dirty" / Flag di Modifica:**
    *   Il SO marca i metadati come "in modifica" prima di scrivere e rimuove il flag al completamento.
    *   Al riavvio, un *consistency checker* (es. `fsck`) scandisce il disco cercando flag attivi.
    *   **Svantaggio:** Richiede una scansione completa del disco (lenta per dischi grandi). È un approccio *best-effort*.

2.  **Journaling (Registrazione Anticipata):**
    *   Introdotto in ext3, ext4, NTFS, XFS.
    *   **Meccanismo:** Prima di modificare i metadati reali, il SO scrive le intenzioni di modifica in un'area dedicata e veloce del disco chiamata **Journal** (o Log).
    *   **Fasi:**
        1.  **Write to Journal:** Le modifiche vengono registrate nel log.
        2.  **Commit:** Si marca la transazione come "committed" (impegnata) nel journal.
        3.  **Checkpoint:** Le modifiche vengono applicate ai metadati reali sul disco.
        4.  **Cleanup:** La voce nel journal viene rimossa/sovrascritta.
    *   **Recovery:** Al riavvio dopo un crash:
        *   Se la transazione non era *committed*: Viene ignorata (Undo implicito).
        *   Se era *committed* ma non applicata: Il SO rilegge il journal e completa le operazioni (Redo).
    *   **Vantaggio:** Il recovery è velocissimo perché deve leggere solo il piccolo journal, non tutto il disco.

3.  **Backup:**
    *   Ultima linea di difesa contro la perdita dati irreversibile.
    *   Tipi: *Full Backup* (copia completa), *Incremental Backup* (solo modifiche dall'ultimo backup).

---

### 2. Architettura a Strati del File System

Il File System è organizzato in livelli gerarchici per favorire l'astrazione e la portabilità.

1.  **Logical File System (Livello Alto):**
    *   Gestisce l'interfaccia utente (API: `open`, `close`, `read`, `write`).
    *   Gestisce i metadati astratti (FCB/Inode) e la struttura delle directory (mapping Nome -> Inode Number).
    *   Controlla i permessi di accesso.
2.  **File Organization Module:**
    *   Traduce gli indirizzi logici dei blocchi del file in indirizzi fisici sul disco.
    *   Gestisce l'allocazione dei blocchi (contigua, indicizzata, ecc.) e lo spazio libero.
3.  **Basic File System:**
    *   Esegue comandi generici di I/O sui blocchi fisici (lettura/scrittura di settori).
    *   Gestisce il buffering e la cache dei blocchi disco.
4.  **I/O Control Layer (Device Drivers):**
    *   Contiene i driver specifici per ogni hardware (controller disco, SSD, USB).
    *   Gestisce gli interrupt hardware e la comunicazione diretta con i registri del dispositivo.

#### Virtual File System (VFS)
*   Strato di astrazione che permette al kernel di supportare molteplici file system (ext4, NTFS, FAT, ISO9660) contemporaneamente.
*   Fornisce un'interfaccia uniforme alle applicazioni, nascondendo le differenze implementative dei singoli file system sottostanti.
*   Utilizza strutture come i **Vnode** (Virtual Node) che mappano gli inode specifici del file system reale.

#### Strutture Dati in Memoria vs Disco
*   **Su Disco (Persistenti):** Superblock, Directory Structure, FCB/Inode, Data Blocks.
*   **In RAM (Volatili/Cache):**
    *   **Mount Table:** Elenco dei volumi montati.
    *   **Directory Cache:** Parte della struttura delle directory caricata per velocità.
    *   **System-wide Open File Table:** Contiene offset, modalità di accesso, puntatore all'Inode in memoria.
    *   **Per-Process File Descriptor Table:** Mappa i FD interi alle entry della tabella globale.
    *   **In-Memory Inodes:** Copie degli inode attivi per evitare accessi disco ripetuti.

---

### 3. Sottosistema di Input/Output (I/O)

Il kernel deve gestire una vasta gamma di periferiche eterogenee attraverso un'architettura standardizzata.

#### Classificazione dei Dispositivi
1.  **Block Devices (Dispositivi a Blocchi):**
    *   Accesso randomico a blocchi di dati fissi (es. Hard Disk, SSD, USB Storage).
    *   Supportano operazioni di `seek`, lettura/scrittura bufferizzata.
2.  **Character Devices (Dispositivi a Carattere/Stream):**
    *   Flusso sequenziale di byte (es. Tastiera, Mouse, Stampante, Porte Seriali).
    *   Nessun concetto di "blocco" o "seek".
3.  **Network Devices:**
    *   Comunicazione tramite socket (BSD Sockets).
    *   Supporta protocolli connection-oriented (TCP) e connectionless (UDP).
    *   Primitive specifiche: `send`, `recv`, `bind`, `listen`.

#### Device Drivers
*   Moduli software (spesso in C) che traducono le chiamate generiche del kernel in comandi specifici per il controller hardware.
*   **Sicurezza:** I driver eseguono in **Kernel Mode (Ring 0)**. Un driver maligno o buggy può compromettere l'intero sistema. L'installazione richiede privilegi di amministratore.
*   **Interfaccia Standard:** I vendor implementano una tabella di puntatori a funzioni standard (`read`, `write`, `ioctl`, `open`) che il kernel invoca.

#### Gestione degli Interrupt
*   L'I/O è prevalentemente **asincrono**.
*   Il driver invia un comando al dispositivo e si sospende o continua altre attività.
*   Quando il dispositivo ha finito, genera un **Hardware Interrupt**.
*   L'**Interrupt Handler** (routine di servizio) sveglia il driver o segnala il completamento dell'operazione al processo in attesa.

#### Terminali e Line Discipline
*   I terminali (TTY) sono dispositivi a carattere speciali.
*   Implementano una **Line Discipline**: un livello software che interpreta il flusso di byte grezzo.
    *   Gestisce l'editing della riga (backspace, cancellazione).
    *   Converte caratteri speciali (es. `CR` -> `LF`).
    *   Gestisce segnali (es. `Ctrl+C` invia SIGINT).
*   Separa l'hardware fisico (tastiera/schermo) dalla logica di elaborazione dell'input testuale.

#### IOCTL (Input/Output Control)
*   Chiamata di sistema "pass-partout" per inviare comandi specifici e non standardizzati a un dispositivo (es. espellere un CD, configurare una scheda di rete).
*   Permette di accedere a funzionalità hardware specifiche non coperte da `read/write`.

---

*Fine della lezione.*
