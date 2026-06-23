# Servizi degli SO

I sistemi operativi forniscono un ambiente per l'esecuzione di programmi e servizi a programmi e utenti.

*   Interfaccia con l’utente
*   Esecuzione di un programma
*   Operazioni di I/O
*   Gestione del file system
*   Comunicazioni
*   Rilevamento di errori


## Servizi di Sistemi Operativi

I sistemi operativi forniscono un ambiente per l'esecuzione di programmi e servizi a programmi e utenti.

**Interfaccia Utente** – quasi tutti i sistemi le forniscono (UI).
► Diversi tipi: **Command-Line (CLI)**, **Graphics User Interface (GUI)**, **Batch**.

**Esecuzione di Programmi** - Il sistema deve essere in grado di caricare un programma in memoria ed eseguire quel programma, terminare l'esecuzione, normalmente o in modo anomalo.

**Operazioni I/O** - Un programma in esecuzione può richiedere I/O, che può coinvolgere un file o un dispositivo I/O.
► Il SO deve nascondere la complessità del dispositivo offrendo agli utenti un **interfaccimento semplice ed uniforme**.


## Servizi degli SO: Gestione File, Comunicazioni ed Errori

Un insieme di servizi del sistema operativo:

**Gestione File-system** - I programmi devono leggere e scrivere file e directory, crearli ed eliminarli, ricercarli, elencare le informazioni sui file, gestire i permessi.
► L'accesso frequente richiede una **gestione oculata**.

**Comunicazione** – I processi possono scambiare informazioni, sullo stesso computer o tra computer in una rete.

**Rilevamento di Errori** – Il sistema operativo deve essere costantemente consapevole di possibili errori.
► Può verificarsi nella **CPU** e nell'**hardware di memoria**, nei **dispositivi I/O**, nel **programma utente**.
► Per ogni tipo di errore, il sistema operativo dovrebbe intraprendere l'azione appropriata per garantire un'elaborazione corretta e coerente.
► Le funzionalità di **debug** possono migliorare notevolmente le capacità dell'utente e del programmatore di utilizzare in modo efficiente il sistema.


## Servizi degli SO: Condivisione delle Risorse

Insieme di funzioni del sistema operativo per garantire il funzionamento efficiente del sistema stesso tramite la **condivisione delle risorse**.

**Allocazione delle risorse** - quando più utenti o più lavori vengono eseguiti contemporaneamente, le risorse devono essere allocate a ciascuno di essi.
*   Molti tipi di risorse: cicli CPU, memoria principale, file, dispositivi I/O.

**Contabilità** - tenere traccia di quali utenti utilizzano quanto e quali tipi di risorse del computer.

**Protezione e sicurezza** - i proprietari delle informazioni archiviate in un sistema informatico multiutente o in rete devono poter controllare l'uso di tali informazioni; i processi simultanei non devono interferire tra loro.
*   La **protezione** deve garantire che l'accesso da parte di processi ed utenti (interni) alle risorse di sistema sia controllato.
*   La **sicurezza** rispetto ad accessi esterni richiede l'autenticazione dell'utente e prevede la difesa dei dispositivi I/O esterni da accessi non consentiti.


## Panoramica dei Servizi di un SO

I processi utente accedono ai servizi del Sistema Operativo mediante **chiamate di sistema**:

*   **Istruzioni che invocano servizi gestiti dal Kernel**

**Struttura a livelli:**
1. user and other system programs
2. GUI / batch / command line / user interfaces
3. **system calls**
4. program execution / I/O operations / file systems / communication / resource allocation / accounting / error detection / services / protection and security
5. **operating system**
6. **hardware**


## Interfaccia Utente - CLI

L'**interprete dei comandi** consente l'immissione diretta dei comandi.

*   A volte implementato nel kernel, a volte dal programma di sistema.
*   A volte più interfacce – **shells**.
*   Principalmente recupera un comando dall'utente e lo esegue.


## Interfaccia Utente - GUI

**Interfaccia grafica (Graphic User Interface)**
*   Interfaccia che usa la metafora del desktop.
*   Mouse, tastiera, schermo.
*   Le icone rappresentano file, programmi, azioni, ecc.
*   Inventata a **Xerox PARC**.


## Altre Interfacce Utente

*   **Interfacce touch-screen**
    *   Senza mouse.
    *   Gesti per attivare azioni.
*   **Comandi vocali**
*   Etc.


## Panoramica dei Servizi di un SO (Approfondimento)

I processi utente accedono ai servizi del Sistema Operativo mediante chiamate di sistema:

*   Istruzioni che invocano servizi gestiti dal Kernel.
*   **ABI (Application Binary Interface)** tra processi utente e sistema.
*   Chiamate mediante **API** che le incapsulano.

**Struttura a livelli:**
1. user and other system programs
2. GUI / batch / command line / user interfaces
3. **system calls**
4. program execution / I/O operations / file systems / communication / resource allocation / accounting / error detection / services / protection and security
5. **operating system**
6. **hardware**


## Chiamate di Sistema

□ Le **chiamate di sistema** (*system call*) costituiscono un’interfaccia per i servizi resi disponibili dal sistema operativo.

□ Chiamate dai programmi mediante **Application Programming Interface** (API).

□ Tra le API più comuni citiamo:
*   **Win API**: API C per Windows (kernal32.dll, User32.dll, etc.)
*   **POSIX API**: API C per POSIX-based systems (incluse tutte le versioni UNIX, Linux e MacOS) - **Portable Operating System Interface**
*   **Java API**: API per la Java virtual machine (JVM)


## Esempio di Chiamata di Sistema

*   Chiamata di sistema per copiare il contenuto di un file in un altro file:
    `cp in.txt out.txt`

**Esempio di sequenza di chiamate di sistema:**
1. Acquisisce il nome del file in ingresso
2. Scrive messaggio di richiesta sullo schermo
3. Accetta i dati in ingresso
4. Acquisisce il nome del file in uscita
5. Scrive messaggio di richiesta sullo schermo
6. Accetta i dati in ingresso
7. Apre il file in ingresso
8. Se il file non esiste, termina con errore
9. Crea il file in uscita
10. Se il file esiste, termina con errore
11. **Ripete**
12. Legge dal file in ingresso
13. Scrive sul file in uscita
14. Finché c’è ancora da leggere
15. Chiude il file in uscita
16. Scrive messaggio sullo schermo per informare del completamento
17. Termina senza errori

**Livelli di astrazione:**
programma (cp) $\rightarrow$ API POSIX / libc $\rightarrow$ system call $\rightarrow$ kernel

*Figura 2.5 Esempio d’uso delle chiamate di sistema.*


## Esempio di API standard

**API**: Specifica un insieme di funzioni a disposizione del programmatore e dettaglia i parametri necessari per l’invocazione di queste funzioni insieme ai valori restituiti.

Come esempio di API standard consideriamo la funzione `read()` disponibile in Unix e Linux. L’API per questa funzione si può ottenere digitando:

```c
man read
```

da riga di comando. Una descrizione di questa API è la seguente:

```c
#include <unistd.h>

ssize_t read(int fd, void *buf, size_t count)
{
    valore nome parametri
    restituito della funzione
}
```

Un programma che utilizza la `read()` deve includere il file `unistd.h` che, tra le altre cose, definisce i tipi di dato `ssize_t` e `size_t`. I parametri passati alla `read()` sono i seguenti:

*   `int fd` — il descrittore del file da leggere
*   `void *buf` — un buffer nel quale vengono messi i dati letti
*   `size_t count` — il massimo numero di byte da leggere e inserire nel buffer

Quando una `read()` è completata con successo viene restituito il numero di byte letti. La `read()` restituisce **0** in caso di fine del file e **–1** quando si è verificato un errore.


## Relazione tra API e Chiamata

*   Tipicamente un numero è associato per ogni chiamata (la **system-call interface** mantiene una tabella indicizzata).
*   L’interfaccia invoca la chiamata nel kernel e restituisce lo status e valore di ritorno (dettagli nascosti gestiti da **librerie di supporto**).

*Figura 2.6 Gestione della chiamata di sistema open() invocata da un’applicazione utente.*


## Passaggio dei parametri

Tre metodi generali utilizzati per passare i parametri al sistema operativo:

*   Passa direttamente i parametri nei **registri** (a volte troppi parametri).
*   Parametri in un **blocco, o tabella, in memoria** e indirizzo del blocco passato come parametro in un registro (Linux e Solaris).
*   Parametri inseriti nello **stack** dal programma e estratti dallo stack dal SO.


## Passaggio dei parametri (Dettaglio Registri)

□ Tre metodi generali utilizzati per passare i parametri al sistema operativo.

□ Passa direttamente i parametri nei registri (a volte troppi parametri).
► In GNU/Linux, una chiamata di sistema accetta al più **sei parametri**.

► Es. nell'architettura Intel il registro **eax** (32 bit) o **rax** (64 bit) contiene sempre un identificatore numerico univoco della chiamata di sistema.

► Altri registri (x64):
*   **rax**: system call number / val ritorno
*   **rdi**: arg0
*   **rsi**: arg1
*   **rdx**: arg2
*   **r10**: arg3
*   **r8**: arg4
*   **r9**: arg5

**Es. write(fd, msg, 12)**
```assembly
mov rax, 1    ; numero syscall write
mov rdi, 1    ; fd (stdout)
mov rsi, msg  ; buffer
mov rdx, 12   ; lunghezza
syscall
```


## Passaggio dei parametri (Dettaglio Tabella)

*   Tre metodi generali utilizzati per passare i parametri al sistema operativo.
*   Passa direttamente i parametri nei registri (a volte troppi parametri).
*   Parametri in un **blocco, o tabella, in memoria** e indirizzo del blocco passato come parametro in un registro (Linux e Solaris).
    *   es. con **rdi = x** si può puntare al blocco.

*Figura 2.7 Passaggio di parametri in forma di tabella.*


## Chiamata di Sistema (Stack)

*   Parametri inseriti nello **stack** dal programma e estratti dallo stack dal SO.
*   Programma in C invoca una chiamata di sistema:
    *   Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`.
    *   Restituisce numero byte o -1 nel var globale `errno`.

Il programma chiamante predispone la chiamata mettendo prima i parametri in uno stack (passi 1–3) – il buffer passato per riferimento.

La procedura chiama il `read` (passo 4) mettendo il codice della chiamata a sistema di `read` in un registro atteso dal Kernel.

Quindi manda un'istruzione **Trap** al kernel e passa il controllo al kernel in **kernel mode** (passi 5-6).

Il kernel trova il codice della chiamata e mediante una tabella trova l’handler della call (passi 7 e 8). Finita l’esecuzione passa il risultato al chiamante (passo 9).

Il chiamante riprende il controllo in **user mode** (passo 10) e pulisce lo stack (passo 11) incrementando lo Stack Pointer (SP).


## Chiamata di Sistema (Architetture Moderne)

*   Parametri inseriti nello stack dal programma e estratti dallo stack dal SO.
*   Programma in C invoca una chiamata di sistema:
    *   Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`.
    *   Restituisce numero byte o -1 nel var globale `errno` (registro **rax**).

Nei sistemi Linux moderni (x86-64) i parametri delle system call sono passati **nei registri**, non nello stack.

Lo stack è usato solo per la chiamata alla funzione della libreria (read, write, ecc.). La sequenza è quindi:

```text
programma C
call read() ← stack
libc wrapper (sposta i parametri nei registri)
registri syscall
syscall
kernel
```


## Chiamata di Sistema (Mappature POSIX)

*   Parametri inseriti nello stack dal programma e estratti dallo stack dal SO.
*   Programma in C invoca una chiamata di sistema:
    *   Invocata da una procedura con il nome della sys call `read(fd, buffer, nbytes)`.
    *   Restituisce numero byte o -1 nel var globale `errno` (registro **rax**).

Le procedure **POSIX** non si mappano sempre uno a uno con le system call offerte dal SO.

Nella maggior parte dei casi chiamano effettivamente le sys call. Alcune eseguono operazioni senza fare il **TRAP** del kernel.


## Tipi di Chiamate di Sistema: Controllo Processi

*   **Controllo di processi**
    *   Creare e terminare processi.
    *   Caricare, eseguire processi.
    *   Ottenere e settare attributi di processo.
    *   Attese di tempo.
    *   Attese di eventi/segnali.
    *   Allocare memoria.
    *   Debugger per determinare bug.
    *   Meccanismi di regolazione per gestire l’accesso a dati condivisi.


## Funzioni per System Call

*   **Controllo di processi**
    *   Funzioni di libreria C per l’invocazione di syscall.
    *   Interfaccia POSIX delle system call.

```c
#include <sys/types.h>
#include <unistd.h>

pid_t getpid(void);  // identificativo del processo
pid_t getppid(void); // identificativo del genitore

pid_t fork(void);        // pid_t wait(int *status);
pid_t vfork(void);

pid_t pid;

if ( (pid=fork()) < 0 )
    perror("fork"), exit(1);
else if (pid != 0) {
    // codice del padre
} else {
    // codice del figlio
}
```


## Tipi di Chiamate di Sistema: File e Dispositivi

**Gestione di File**
*   create file, delete file.
*   open, close file.
*   read, write, reposition.
*   get and set file attributes.

**Gestione di dispositivi**
*   request device, release device.
*   read, write.
*   get device attributes, set device attributes.
*   logicamente attach or detach devices.