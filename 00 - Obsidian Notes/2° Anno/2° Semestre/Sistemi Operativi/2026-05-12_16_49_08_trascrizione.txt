# Trascrizione Esercitazione: I/O di Basso Livello (System Call POSIX)

**Data:** 12 Maggio 2026
**Argomento:** System Call `open`, `read`, `write`, `close`, `lseek`; Condivisione di File Descriptor tra processi (Fork); Hard Link vs Soft Link; Sparse Files (Holes).

---

### 1. Le System Call Fondamentali per l'I/O

Le system call POSIX forniscono un'interfaccia uniforme per l'accesso ai file, indipendentemente dal dispositivo sottostante.

#### A. `open()`
Crea o apre un file, restituendo un **File Descriptor (FD)**, un intero non negativo che funge da indice nella tabella dei file aperti del processo.

*   **Sintassi:** `int open(const char *pathname, int flags, mode_t mode);`
*   **Parametri:**
    *   `pathname`: Percorso del file.
    *   `flags`: Bitmask che definisce la modalità di accesso.
        *   `O_RDONLY`, `O_WRONLY`, `O_RDWR` (Lettura/Scrittura).
        *   `O_CREAT`: Crea il file se non esiste (richiede il terzo argomento `mode`).
        *   `O_TRUNC`: Se il file esiste e viene aperto in scrittura, lo tronca a lunghezza zero.
        *   `O_APPEND`: Sposta l'offset alla fine del file prima di ogni scrittura.
    *   `mode`: Permessi del file (es. `S_IRUSR | S_IWUSR` per read/write owner), usati solo se `O_CREAT` è specificato.
*   **Return:** FD in caso di successo, `-1` in caso di errore (controllare `errno`).
*   **Offset Iniziale:** Di solito 0 (inizio file), a meno che `O_APPEND` sia settato.

#### B. `write()` e `read()`
Operano su blocchi di byte utilizzando il FD.

*   **`ssize_t write(int fd, const void *buf, size_t count);`**
    *   Scrive `count` byte dal buffer `buf` sul file associato a `fd`.
    *   Restituisce il numero di byte effettivamente scritti (può essere < `count` in caso di errore o disco pieno).
    *   Aggiorna l'offset corrente nel kernel.
*   **`ssize_t read(int fd, void *buf, size_t count);`**
    *   Legge fino a `count` byte dal file in `buf`.
    *   Restituisce il numero di byte letti. `0` indica End-of-File (EOF).
    *   **Nota:** L'EOF non è un carattere fisico nel file, ma una condizione gestita dal kernel quando l'offset raggiunge la dimensione del file.

#### C. `close()`
*   `int close(int fd);`
*   Chiude il FD, liberando le risorse nel kernel.
*   Garantisce che i dati nei buffer del kernel siano flushed (scritti) sul disco (anche se la sincronizzazione completa richiede `fsync`).

#### D. `lseek()`
Modifica l'offset di lettura/scrittura del file senza effettuare I/O.

*   **Sintassi:** `off_t lseek(int fd, off_t offset, int whence);`
*   **Whence:**
    *   `SEEK_SET`: Offset assoluto dall'inizio del file.
    *   `SEEK_CUR`: Offset relativo alla posizione corrente.
    *   `SEEK_END`: Offset relativo alla fine del file.
*   **Utilizzo:** Permette accessi randomici al file.

---

### 2. Esercizio 1: Comunicazione Padre-Figlio tramite File Condiviso

**Obiettivo:** Capire come i File Descriptor e gli offset vengono condivisi dopo una `fork()`.

**Scenario:**
1.  Il processo padre apre un file in `O_RDWR | O_CREAT`.
2.  Esegue `fork()`.
3.  **Figlio:** Scrive una stringa nel file.
4.  **Padre:** Attende la terminazione del figlio (`wait()`), poi legge il contenuto del file e lo stampa a stdout.

**Concetto Chiave: Condivisione dell'Offset**
Poiché l'`open()` avviene *prima* della `fork()`, padre e figlio condividono la stessa entry nella **System-wide Open File Table**.
*   Questo significa che condividono lo stesso **offset** del file.
*   Quando il figlio scrive, l'offset comune si sposta alla fine dei dati scritti.
*   Se il padre vuole leggere dall'inizio, deve resettare l'offset usando `lseek(fd, 0, SEEK_SET)` prima della `read()`.
*   Se il padre volesse scrivere immediatamente dopo il figlio, non avrebbe bisogno di `lseek`, poiché l'offset è già posizionato correttamente.

**Codice Esempio (Logica):**
```c
int fd = open(filename, O_RDWR | O_CREAT | O_TRUNC, 0644);
if (fork() == 0) {
    // Figlio
    write(fd, message, strlen(message));
    exit(0);
} else {
    // Padre
    wait(NULL);
    lseek(fd, 0, SEEK_SET); // Reset offset per leggere dall'inizio
    char buffer[1024];
    ssize_t n = read(fd, buffer, sizeof(buffer));
    write(STDOUT_FILENO, buffer, n);
    close(fd);
}
```

**Variazione (Open Separati):**
Se padre e figlio eseguono `open()` *dopo* la `fork()`:
*   Ogni processo ha la propria entry nella Open File Table.
*   Gli offset sono **indipendenti**.
*   Il padre non ha bisogno di `lseek()` per leggere dall'inizio, poiché il suo offset è rimasto a 0 (o dove lo ha lasciato lui), indipendentemente dalle scritture del figlio.

---

### 3. Esercizio 2: Lettura Inversa di un File

**Obiettivo:** Manipolare l'offset per leggere un file al contrario (byte per byte).

**Algoritmo:**
1.  Aprire il file in lettura.
2.  Ottenere la dimensione del file (usando `lseek(fd, 0, SEEK_END)` o `stat()`).
3.  Posizionarsi sull'ultimo byte: `lseek(fd, -1, SEEK_END)`.
4.  Ciclo `while`:
    *   Leggere 1 byte.
    *   Stamparlo a stdout.
    *   Spostarsi indietro di 2 byte: `lseek(fd, -2, SEEK_CUR)` (uno per compensare la lettura automatica che avanza l'offset, uno per tornare al byte precedente).
    *   Uscire se l'offset diventa negativo (inizio file raggiunto).

**Nota:** Questa operazione è inefficiente per file grandi a causa dell'overhead delle system call ripetute, ma utile didatticamente per comprendere `lseek`.

---

### 4. Esercizio 3: Sparse Files (Creazione di "Buchi")

**Obiettivo:** Dimostrare la differenza tra dimensione logica e dimensione fisica su disco.

**Scenario:**
1.  Aprire un file in scrittura (`O_WRONLY | O_CREAT`).
2.  Scrivere la stringa "INIZIO".
3.  Spostare l'offset di N byte (es. 100.000) usando `lseek(fd, 100000, SEEK_CUR)`.
4.  Scrivere la stringa "FINE".
5.  Chiudere il file.

**Risultato:**
*   **Dimensione Logica (`ls -l`):** ~100.012 byte (la distanza tra inizio e fine).
*   **Dimensione Fisica (`ls -s` o `du`):** Pochi KB (solo i blocchi effettivamente allocati per "INIZIO" e "FINE").
*   **Contenuto (`cat`):** Visualizza "INIZIO" seguito da caratteri nulli (`\0`) e poi "FINE".

**Spiegazione Tecnica:**
I file system moderni supportano i **Sparse Files**. Quando si fa `lseek` oltre la fine del file e si scrive, il FS non alloca blocchi fisici pieni di zeri per la regione intermedia. Invece, marca quella regione come "buco" (hole) nei metadati (Inode/extents).
*   I buchi leggono come zeri.
*   Non occupano spazio su disco fino a quando non vi si scrivono dati reali.
*   Utile per database, immagini VM, e file di log pre-allocati.

---

### 5. Considerazioni Finali su Sincronizzazione e Pipe

*   **File vs Pipe:**
    *   L'uso di file per IPC (Inter-Process Communication) richiede sincronizzazione esplicita (`wait`, `sleep`, lock) perché la `read()` su file non è bloccante in attesa di nuovi dati (legge ciò che c'è, o EOF).
    *   Le **Pipe** (`pipe()`) offrono sincronizzazione implicita: la `read()` blocca il processo finché non ci sono dati disponibili o la pipe non viene chiusa dall'writer.
*   **Race Conditions:**
    *   Senza `wait()` o meccanismi di locking, l'ordine di esecuzione tra padre e figlio è nondeterministico.
    *   Scrivere nello stesso file da due processi senza coordinamento può portare a sovrascritture o dati interleaved (mescolati), a meno che non si usi `O_APPEND` (che garantisce atomicità nella scrittura alla fine) o lock sui file (`flock`/`fcntl`).

*Fine dell'esercitazione.*
