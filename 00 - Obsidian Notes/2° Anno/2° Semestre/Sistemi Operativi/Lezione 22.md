# Trascrizione Lezione: Strutture del File System, Directory, Link e Inode

**Data:** 7 Maggio 2026
**Argomento:** Architettura del File System (FCB, Tabella File Aperti), Operazioni sui File, Directory come File, Hard Link vs Symbolic Link, Journaling e Struttura degli Inode (Indirizzamento Diretto/Indiretto).

---

### 1. Architettura Logica del File System

Il File System risiede permanentemente sulla memoria secondaria (disco), ma il Kernel mantiene strutture dati dinamiche in RAM per gestirlo efficientemente.
*   **Vista Utente:** I file sono sequenze contigue di byte (astrazione logica).
*   **Vista Fisica:** I dati sono frammentati in **blocchi** sul disco (es. 512B o 4KB).
*   **Granularità:** La CPU lavora a livello di byte in RAM, ma il trasferimento da/verso il disco avviene a livello di blocchi. Questo causa **frammentazione interna** (spreco di spazio nell'ultimo blocco allocato).

#### Metadati e File Control Block (FCB)
Ogni file è associato a un insieme di metadati, noto come **File Control Block (FCB)**. In Unix/Linux, questa struttura è chiamata **Inode** (Index Node).
*   **Contenuto dell'Inode:**
    *   Identificatore univoco (Inode Number).
    *   Tipo di file (regolare, directory, dispositivo, link).
    *   Dimensione del file (in byte).
    *   Proprietario (UID) e Gruppo (GID).
    *   Permessi (Read/Write/Execute per Owner, Group, Others).
    *   Timestamps (Creazione, Modifica, Accesso).
    *   Puntatori ai blocchi di dati sul disco.
*   **Nota Importante:** L'Inode **NON** contiene il nome del file. Il nome è gestito separatamente nelle Directory.

---

### 2. Gestione dei File Aperti: Le Tre Tabelle

Quando un processo apre un file (`open()`), il Sistema Operativo crea una serie di strutture dati in RAM per tracciare l'accesso. Esiste una separazione chiara tra stato del processo, stato dell'apertura e stato del file.

1.  **Tabella dei File Descriptor (Per-Process):**
    *   Situata nel **PCB** (Process Control Block).
    *   È un array indicizzato dai **File Descriptor (FD)** (interi: 0=stdin, 1=stdout, 2=stderr, 3...n).
    *   Ogni entry punta a una entry nella *System-wide Open File Table*.

2.  **System-wide Open File Table (Globale al Kernel):**
    *   Contiene una entry per ogni apertura attiva di un file da parte di qualsiasi processo.
    *   **Contenuto:**
        *   Flag di stato (Read-only, Write-only, Append, etc.).
        *   **Current Offset (File Pointer):** Posizione corrente di lettura/scrittura. *Nota: Ogni apertura ha il suo offset indipendente.*
        *   Puntatore all'Inode in memoria (V-node/iNode cache).
    *   Permette a due processi (o lo stesso processo due volte) di aprire lo stesso file con offset e modalità diversi.

3.  **Inode Table (In-Memory Inodes):**
    *   Contiene le copie degli Inode caricati dal disco in RAM per i file attualmente utilizzati.
    *   **Contenuto:** Metadati statici (dimensione, permessi, puntatori ai blocchi disco).
    *   Aggiornata quando la dimensione del file cambia o i metadati vengono modificati.
    *   Sincronizzata periodicamente con il disco (write-back).

> **Flusso di `open()`:**
> 1. Cerca il nome nella Directory -> Ottiene Inode Number.
> 2. Carica Inode dal disco alla *Inode Table* (se non già presente).
> 3. Crea entry nella *Open File Table* (inizializza offset a 0 o fine se APPEND).
> 4. Alloca FD nella tabella del processo e punta alla entry della Open File Table.

---

### 3. Operazioni sui File e Locking

*   **Read/Write:** Operano sulla RAM (cache/buffer). L'offset nella *Open File Table* viene aggiornato automaticamente dopo ogni operazione sequenziale.
*   **Seek (lseek):** Sposta l'offset nella *Open File Table* senza effettuare I/O immediato.
*   **Truncate:** Azzera il contenuto del file (libera blocchi), ma mantiene l'Inode e i metadati.
*   **Delete (unlink):** Rimuove l'entry dalla Directory e decrementa il contatore dei link nell'Inode. Se il contatore arriva a 0 e nessun processo ha il file aperto, l'Inode e i blocchi dati vengono liberati.

#### File Locking
Meccanismo per coordinare l'accesso concorrente ai file (simile ai Mutex, ma a livello di FS).
*   **`flock()` (BSD):** Lock su intero file. Semplice ma meno flessibile.
*   **`fcntl()` (POSIX):** Lock su regioni specifiche del file (byte range locking). Più complesso, permette lock condivisi (lettura) ed esclusivi (scrittura).
*   **Costo:** Il file locking è più costoso dei Mutex in memoria perché richiede chiamate di sistema e accesso alle strutture del Kernel/FS. È essenziale per la coordinazione tra **processi distinti** (che non condividono memoria), mentre i thread dovrebbero preferire i Mutex.

---

### 4. Directory e Naming

Le Directory sono file speciali che contengono una mappa di associazione: **Nome File <-> Inode Number**.
*   **Struttura:** Lista di entry a lunghezza fissa (o variabile nei FS moderni).
*   **Entry Speciali:**
    *   `.` (Dot): Punta all'Inode della directory corrente.
    *   `..` (Dot-Dot): Punta all'Inode della directory padre.
*   **Gerarchia:** La struttura ad albero (o grafo) permette il naming gerarchico (Pathnames).
    *   **Absolute Path:** Dalla root (`/`).
    *   **Relative Path:** Dalla Working Directory del processo (memorizzata nel PCB).

#### Link: Hard Link vs Symbolic Link

| Caratteristica | Hard Link | Symbolic Link (Soft Link) |
| :--- | :--- | :--- |
| **Cos'è** | Un altro nome per lo stesso Inode. | Un file speciale contenente il percorso del target. |
| **Inode** | Condivide lo stesso Inode del target. | Ha un Inode proprio e distinto. |
| **Dimensione** | Occupa spazio solo nella directory (entry). | Occupa un blocco disco (per contenere il path). |
| **Target** | Può puntare solo a file (non directory, solitamente). | Può puntare a file o directory. |
| **Cross-FS** | No (stesso file system). | Sì (può puntare ovunque). |
| **Cicli** | Impossibile creare cicli (grafo aciclico). | Possibile creare cicli (loop infiniti). |
| **Validità** | Se cancelli il target originale, il link funziona ancora (finché ci sono link). | Se cancelli il target, il link diventa "rotto" (dangling). |
| **Comando** | `ln source dest` | `ln -s source dest` |

*   **Contatore Link:** L'Inode mantiene un conteggio di quanti hard link puntano ad esso. Il file viene fisicamente eliminato solo quando questo conteggio è 0 e nessun processo lo tiene aperto.

---

### 5. Affidabilità: Journaling

Per prevenire la corruzione del File System in caso di crash improvviso (blackout), i FS moderni (ext3/4, NTFS, XFS) usano il **Journaling**.
*   **Problema:** Le operazioni su FS richiedono aggiornamenti multipli (dati + metadati). Se il sistema crasha a metà, il FS diventa inconsistente.
*   **Soluzione:** Prima di scrivere i dati/metadati reali, il FS scrive l'intento dell'operazione in un'area dedicata chiamata **Journal** (log circolare).
*   **Recovery:** Al riavvio, il FS controlla il Journal.
    *   Se l'operazione era completata nel Journal ma non sul FS principale, viene "replayata" (completata).
    *   Se l'operazione era incompleta nel Journal, viene annullata (undo).
    *   Questo garantisce la consistenza strutturale del FS molto più rapidamente di un full check (fsck).

---

### 6. Allocazione dei Blocchi: La Struttura degli Inode

Come fa l'Inode a puntare ai blocchi dati sul disco? Unix/Linux usa una struttura ibrida per bilanciare velocità (file piccoli) e capacità (file grandi).

L'Inode contiene un array di puntatori ai blocchi:
1.  **Direct Pointers (Indirizzamento Diretto):**
    *   Puntano direttamente ai blocchi dati.
    *   Velocissimi per file piccoli (accesso O(1)).
    *   Esempio: Primi 12 puntatori diretti.

2.  **Single Indirect Pointer (Indiretto Singolo):**
    *   Punta a un **blocco indice** (un blocco pieno di puntatori ad altri blocchi dati).
    *   Permette di gestire file di media dimensione.
    *   Richiede 2 accessi al disco per leggere un dato (uno per l'indice, uno per il dato).

3.  **Double Indirect Pointer (Indiretto Doppio):**
    *   Punta a un blocco indice di primo livello, che punta a blocchi indice di secondo livello, che puntano ai dati.
    *   Per file grandi.
    *   Richiede 3 accessi al disco.

4.  **Triple Indirect Pointer (Indiretto Triplo):**
    *   Tre livelli di indicizzazione.
    *   Per file enormi.
    *   Richiede 4 accessi al disco.

> **Efficienza:** La maggior parte dei file è piccola e rientra nei puntatori diretti, garantendo prestazioni elevate. I file grandi pagano il costo aggiuntivo degli accessi indiretti, ma possono crescere fino a dimensioni teoriche enormi (limitate solo dallo spazio disco e dai bit di indirizzamento).

---

*Fine della lezione.*
