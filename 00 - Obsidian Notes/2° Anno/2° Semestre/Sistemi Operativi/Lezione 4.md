# Trascrizione Lezione: Comunicazione Inter-Processo (IPC) e Introduzione alla Shell Linux

**Data:** 11 Marzo 2026
**Argomento:** Shared Memory (mmap), Anonymous Pipes, Named Pipes (FIFO), Socket, Permessi Unix, Gestione Processi (ps, kill) e Comandi Base Shell.

---

### 1. Shared Memory con `mmap`

La memoria condivisa permette a processi distinti di accedere alla stessa regione fisica di RAM. In POSIX, si utilizza spesso `shm_open` combinato con `mmap`.

#### Creazione e Mappatura (Produttore)
1.  **`shm_open(name, flags, mode)`:** Crea o apre un oggetto di memoria condivisa identificato da un `name` (stringa).
    *   `flags`: `O_CREAT | O_RDWR` (crea se non esiste, lettura/scrittura).
    *   `mode`: Permessi del file (es. `0666` -> RW per User, Group, Others).
2.  **`ftruncate(fd, size)`:** Imposta la dimensione dell'oggetto in byte.
3.  **`mmap(addr, length, prot, flags, fd, offset)`:** Mappa l'oggetto nello spazio di indirizzamento virtuale del processo.
    *   Restituisce un puntatore (`void*`) all'inizio della regione.
    *   `prot`: `PROT_READ | PROT_WRITE`.
    *   `flags`: `MAP_SHARED` (le modifiche sono visibili agli altri processi e persistono sull'oggetto).

#### Accesso (Consumatore)
1.  **`shm_open(name, O_RDWR, 0)`:** Apre lo stesso oggetto tramite il nome condiviso.
2.  **`mmap(...)`:** Mappa la regione. Il consumatore vede gli stessi dati scritti dal produttore.
3.  **Sincronizzazione:** `mmap` da sola non offre sincronizzazione. Spesso si usano semafori o mutex (in shared memory) per coordinare lettura/scrittura.

#### Pulizia
*   **`munmap(ptr, length)`:** Rimuove la mappatura dallo spazio del processo.
*   **`shm_unlink(name)`:** Rimuove il nome dell'oggetto dal filesystem (simile a `unlink` per i file). L'oggetto viene distrutto quando tutti i processi hanno fatto `munmap`.

> **Nota sui Permessi (0666):** I permessi Unix sono ottali.
> *   `6` = `110` in binario = Read (4) + Write (2).
> *   `7` = `111` in binario = Read + Write + Execute.
> *   `0666` significa: RW per Owner, RW per Group, RW per Others.

---

### 2. Anonymous Pipes (Pipe Ordinarie)

Le pipe anonime sono canali di comunicazione unidirezionali (half-duplex) tra processi imparentati (padre-figlio).

#### Creazione
*   **`int pipefd[2];`**
*   **`pipe(pipefd)`:** Crea una pipe nel kernel.
    *   `pipefd[0]`: File Descriptor per la **Lettura** (Read End).
    *   `pipefd[1]`: File Descriptor per la **Scrittura** (Write End).

#### Flusso di Comunicazione
1.  Il processo padre chiama `pipe()`.
2.  Il padre chiama `fork()`. Ora padre e figlio condividono i FD della pipe.
3.  **Chiusura dei lati inutilizzati (Cruciale):**
    *   Se il Padre scrive e il Figlio legge:
        *   Padre: `close(pipefd[0])` (chiude lato lettura).
        *   Figlio: `close(pipefd[1])` (chiude lato scrittura).
4.  **Scambio Dati:**
    *   Scrittore: `write(pipefd[1], buffer, nbytes)`.
    *   Lettore: `read(pipefd[0], buffer, maxbytes)`.

#### Comportamento Bloccante e EOF
*   **`read()` bloccante:** Se la pipe è vuota, `read()` blocca il processo finché non arrivano dati o tutti gli scrittori chiudono la pipe.
*   **EOF (End-of-File):** Se tutti gli scrittori chiudono il lato write (`close(pipefd[1])`), una successiva `read()` restituisce **0**. Questo segnala al lettore che la comunicazione è finita.
*   **SIGPIPE:** Se un processo scrive su una pipe dove tutti i lettori hanno chiuso il lato read, il kernel invia il segnale **`SIGPIPE`** allo scrittore. Di default, questo termina il processo. È necessario gestire questo segnale o controllare gli errori di `write()`.

---

### 3. Named Pipes (FIFO)

Le FIFO risolvono il limite delle pipe anonime (solo processi imparentati) permettendo la comunicazione tra processi qualsiasi tramite un nome nel filesystem.

#### Creazione
*   **Comando Shell:** `mkfifo mypipe`
*   **System Call:** `mkfifo("mypipe", 0666)`
*   La FIFO appare come un file speciale nel filesystem (`prw-r--r--`).

#### Utilizzo
1.  **Server/Lettore:**
    *   `fd = open("mypipe", O_RDONLY);`
    *   `read(fd, ...)` -> Si blocca in attesa di uno scrittore.
2.  **Client/Scrittore:**
    *   `fd = open("mypipe", O_WRONLY);`
    *   `write(fd, ...)`
3.  **Chiusura:** `close(fd)` e infine `unlink("mypipe")` per rimuovere il file dal filesystem.

> **Differenza chiave:** A differenza delle pipe anonime (create in memoria kernel), le FIFO persistono nel filesystem fino a quando non vengono esplicitamente cancellate con `unlink`.

---

### 4. Socket (Cenno)

Le socket estendono il concetto di file descriptor alla comunicazione di rete.
*   **API BSD Socket:** `socket()`, `bind()`, `listen()`, `accept()` (lato server); `connect()` (lato client).
*   **Uniformità:** Una volta stabilita la connessione, si usa `read()` e `write()` sui socket FD esattamente come su file o pipe.
*   **Tipi:**
    *   `SOCK_STREAM` (TCP): Affidabile, orientato alla connessione.
    *   `SOCK_DGRAM` (UDP): Senza connessione, messaggi discreti.

---

### 5. Laboratorio: Shell Linux e Gestione Processi

#### Comandi Base
*   **Navigazione:** `pwd` (print working directory), `cd` (change directory), `ls` (list files).
    *   `ls -l`: Mostra dettagli (permessi, owner, size, date).
    *   Permessi: `rwx` (read/write/execute) per User, Group, Others.
*   **Visualizzazione Processi:**
    *   `ps`: Snapshot dei processi.
    *   `ps -ef` o `ps aux`: Elenco completo con PID, PPID (Parent PID), UID, CMD.
    *   `vmstat`: Statistiche di memoria virtuale e CPU.
*   **Gestione Processi:**
    *   **Background:** `command &` (es. `gedit &`). La shell non attende la terminazione.
    *   **Kill:** `kill -9 <PID>` (SIGKILL, terminazione forzata immediata). `kill -15 <PID>` (SIGTERM, terminazione gentile).
    *   **Segnali:** I processi possono gestire segnali (tranne SIGKILL e SIGSTOP) tramite handler.

#### Esecuzione Programmi C
1.  **Compilazione:** `gcc source.c -o executable`
2.  **Esecuzione:** `./executable arg1 arg2`
3.  **Argomenti Main:**
    *   `int main(int argc, char *argv[])`
    *   `argc`: Numero di argomenti (incluso il nome del programma).
    *   `argv[]`: Array di stringhe. `argv[0]` è il nome del programma.
    *   Conversione: `atoi(argv[1])` converte stringa in intero.

#### Esempio Fork e PID
```c
pid_t pid = fork();
if (pid == 0) {
    // Figlio
    printf("Figlio: PID=%d, PPID=%d\n", getpid(), getppid());
} else {
    // Padre
    printf("Padre: PID=%d, Figlio PID=%d\n", getpid(), pid);
    wait(NULL); // Attende il figlio
}
```
*   `getpid()`: Restituisce il PID del processo corrente.
*   `getppid()`: Restituisce il PID del processo padre.
*   Dopo la `fork()`, padre e figlio hanno spazi di memoria separati. Le modifiche alle variabili in uno non sono visibili all'altro.

---

*Fine della lezione.*
