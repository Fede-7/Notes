# Lezione 7: Threads & Concorrenza


## Obiettivi

- Introdurre la nozione di **thread**
- **Multithreaded programming**
- Supporti per threads in **Linux**


## Motivazioni

Le applicazioni sono generalmente **multithreaded**. I task multipli in applicazioni sono spesso implementati da thread separati, come ad esempio:

- Update del display
- Fetch data
- Spell checking
- Risposta in rete

La creazione di un **processo** è un'operazione pesante, mentre il **thread** è considerato "leggero". Inoltre, il kernel è generalmente multithreaded.


## Processi Single e Multithreaded

Le unità base di utilizzo della CPU sono caratterizzate da:

- **Thread ID**
- **PC** (Program Counter)
- **Registri**
- **Stack**

Questi elementi rappresentano la minima identità di un task.

*(Immagini di riferimento: Single-threaded process vs Multithreaded process)*


## Architettura di Server Multithread

Queste architetture sono molto utilizzate nei sistemi **client-server**. Per ogni client viene generato un thread dedicato che ne gestisce le operazioni.

Ogni richiesta di un client viene gestita da un thread separato. Questo permette al server di gestire tante richieste contemporaneamente eseguendo molti task leggeri.

**Flusso di lavoro:**
(1) request
(2) create new thread to service the request
(3) resume listening for additional client requests


## Benefici

**Risposta**
- Esecuzione continua se una parte del processo è bloccata (fondamentale per le interfacce utente).

**Risorse**
- I thread condividono le risorse di un processo, rendendo la gestione più semplice rispetto alla *shared memory* o al *message passing*.

**Economia**
- Essendo più leggero di una creazione di processo, il **thread switching** presenta un overhead minore rispetto al *context switching*.

**Scalabilità**
- I processi possono avvantaggiarsi delle architetture multiprocessore.


## Multicore Programming

I sistemi multithread forniscono meccanismi utili per i sistemi **multicore**. Tuttavia, i sistemi Multicore o multiprocessori pongono diversi problemi:

**Divisione e bilanciamento delle attività:**
- Come dividere le attività sui core (computazioni parallelizzabili).
- Come bilanciare il calcolo sui core.
- Come splittare i dati.

**Gestione delle dipendenze:**
- Come gestire le dipendenze dei dati sui core (possono richiedere sincronizzazione).

**Test e Debugging:**
- Come fare test e debugging con più tracce di esecuzioni da testare.

**Definizioni chiave:**
- **Parallelismo**: Più di un task simultaneamente distribuiti su più unità di calcolo.
- **Concorrenza**: Consente il progresso contemporaneo di più di un task. Se il processore/core è singolo, la concorrenza è data dallo *scheduler* che intrallaccia le esecuzioni.


## Tipi di parallelismo

**Parallelismo di dati**
- Sottoinsiemi dei dati su core multipli con la stessa operazione per ognuno.
- Esempio: calcolo della somma dei numeri su un array (il compito può essere diviso).

**Parallelismo di task**
- Thread sui core dove ciascuno svolge un’operazione particolare.
- Esempio: calcolo della media e della varianza di un set di dati.

**Supporto architetturale**
Al crescere del numero dei thread aumenta il supporto architetturale:
- Le CPU hanno core e hardware thread.
- Esempio: i7 (13th Gen) con 16 core e 24 hardware threads.


## Concorrenza vs. Parallelismo

**Esecuzione concorrente su sistema single-core:**
$T_1$ $T_2$ $T_3$ $T_4$ $T_1$ $T_2$ $T_3$ $T_4$ $T_1$ ...

**Parallelismo su sistema multi-core:**
core 1: $T_1$ $T_3$ $T_1$ $T_3$ $T_1$ ...
core 2: $T_2$ $T_4$ $T_2$ $T_4$ $T_2$ ...


## Legge di Amdahl

Guadagno teorico in performance con l’aggiunta di un core per un’applicazione che ha sia componenti seriali che paralleli.

- **S** è la porzione seriale
- **N** sono i core per il processamento

$$\text{speedup} \leq \frac{1}{S + \frac{(1-S)}{N}}$$

**Esempio:** se l’applicazione è al 75% parallela e 25% seriale, passando da 1 a 2 core si ha uno speed-up di 1.6 volte.
Con $N$ che tende ad infinito, lo speed-up tende a $1 / S$.


## Legge di Amdahl (Latenza)

Guadagno teorico in performance (latenza) con l’aggiunta di un core per un’applicazione che ha sia componenti seriali che paralleli.

- **S** è la porzione di calcolo seriale (non parallelizzabile)
- **N** sono i core per il processamento

$$\text{speedup} \leq \frac{1}{S + \frac{(1-S)}{N}}$$

La porzione seriale di un’applicazione ha un effetto molto marcato sul guadagno di performance con un core aggiuntivo.


## User Thread e Kernel Thread

**User thread**
- Gestita da librerie di thread di livello utente.
- Tre principali: POSIX Pthreads, Windows threads, Java threads.

**Kernel thread**
- Supportati dal Kernel.
- Esempi (tutti gli SO general purpose inclusi): Windows, Solaris, Linux, Tru64 UNIX, Mac OS.


## Modelli di Multithreading

Diversi modi di gestire la relazione tra User e Kernel thread:
- **Many-to-One**
- **One-to-One**
- **Many-to-Many**


## Many-to-One

- Tanti thread user mappati su un **singolo** kernel thread.
- Problema: un thread bloccante (es. durante una system call) può bloccare tutto.
- Problema di parallelismo: in sistemi multicore, uno solo alla volta è in esecuzione nel Kernel.
- Pochi sistemi utilizzano questo approccio (es. Solaris Green Threads library, GNU Portable Threads library).

**Struttura:** Lato kernel, un solo PCB per gestire i thread di un processo.


## One-to-One

- Ogni thread user-level mappato su **un kernel thread**.
- La creazione di un thread user-level crea un kernel thread.
- Maggiore concorrenza rispetto al modello many-to-one.
- Il numero di thread per processo può essere limitato per evitare overhead.
- Esempi: Windows, Linux, Solaris 9 e successivi.
- L'utente deve controllare il numero dei thread.


## Many-to-Many

- Molti thread user-level sono mappati su **molti** thread del kernel.
- Il SO può creare un numero sufficiente di thread del kernel, ma può gestirne il numero e il grado di parallelismo.
- Esempi: Solaris dalla versione 9, Windows con ThreadFiber package.
- Il numero può dipendere dalla macchina e dall’applicazione.
- L’utente può lanciare più thread, il Sistema controlla quanti thread kernel utilizzare.


## Two-level Model

- Variante del Many-to-Many che permette ad un user-thread di essere **legato (bound)** ad un kernel thread.
- Esempi: IRIX, HP-UX, Tru64 UNIX, Solaris 8 e precedenti.


## Attivazioni Scheduler

Sia i modelli Many-to-Many che Two-level richiedono di mantenere un numero appropriato di kernel thread allocati per l’applicazione.

Tipicamente viene usata una struttura dati intermedia: **lightweight process (LWP)**.
- Funziona come un processore virtuale su cui il processo può schedulare l’esecuzione di user thread.
- Ogni LWP è associato ad un kernel thread.
- Il kernel fornisce all'applicazione un insieme di LWPs; l'applicazione schedula gli user thread su questi.

**Comunicazione Kernel-Applicazione:**
- **upcalls**: quando il kernel sta per bloccarsi, viene gestito da un **upcall-handler**.
- Comunica all’applicazione il blocco imminente e crea un nuovo LWP.
- Consente all’applicazione di schedulare un nuovo processo.
- Questa comunicazione permette di mantenere il corretto numero di kernel thread.


## Librerie per Thread

Le librerie per i thread (Thread library) forniscono le API per creare e gestire i thread. Esistono due modi principali di implementarle:

**1. Libreria interamente nello user space**
- I thread sono implementati al livello utente (gestiti con chiamate di funzione utente).

**2. Libreria al livello Kernel supportata dal SO**
- I thread sono gestiti con chiamate di Sistema (gestiti con chiamata di sistema).


## Pthreads

- Estensione di POSIX standard (IEEE 1003.1c) che fornisce le API per la creazione e sincronizzazione dei thread.
- Esiste sia in versione user-level sia kernel-level.
- È una **Specifica**, non un'implementazione.
- L'API specifica il comportamento delle funzioni; l'implementazione è lasciata allo sviluppatore.
- Tipiche in UNIX (Solaris, Linux, Mac OS).


## Esempio Pthreads

Esempio di somma dei primi N numeri:
- Per N = 5, Sum = 1 + 2 + 3 + 4 + 5 = 15.
- Si può delegare il calcolo ad uno o più thread.
- Esistono thread **sincroni** (il genitore aspetta i figli) e **asincroni** (il genitore continua subito).


## Esempio Pthreads (Codice)

```c
#include <pthread.h>
#include <stdio.h>

int sum; /* this data is shared by the thread(s) */
void *runner(void *param); /* threads call this function */

int main(int argc, char *argv[])
{
    pthread_t tid; /* the thread identifier */
    pthread_attr_t attr; /* set of thread attributes */

    if (argc != 2) {
        fprintf(stderr,"usage: a.out <integer value>\n");
        return -1;
    }
    if (atoi(argv[1]) < 0) {
        fprintf(stderr,"%d must be >= 0\n",atoi(argv[1]));
        return -1;
    }
}
```


## Esempio Pthreads (Codice continuo)

```c
/* get the default attributes */
pthread_attr_init(&attr);

/* create the thread */
pthread_create(&tid, &attr, runner, argv[1]);

/* wait for the thread to exit */
pthread_join(tid, NULL);

printf("sum = %d\n", sum);
}

/* The thread will begin control in this function */
void *runner(void *param)
{
    int i, upper = atoi(param);
    sum = 0;

    for (i = 1; i <= upper; i++)
        sum += i;

    pthread_exit(0);
}
```


## Codice Pthreads per il join di 10 Thread

```c
#define NUM_THREADS 10

/* an array of threads to be joined upon */
pthread_t workers[NUM_THREADS];

for (int i = 0; i < NUM_THREADS; i++)
    pthread_join(workers[i], NULL);
```


## Pthreads (Funzione pthread_create)

Per creare thread addizionali relativi ad uno stesso processo, Posix prevede la funzione:

```c
#include <pthread.h>

int pthread_create ( pthread_t *tid, const pthread_attr_t *attr,
                    void * ( *start_func) (void *), void *arg );
```

- Se la chiamata ha successo, *tid* punta al thread ID.
- *attr* permette di specificare gli attributi del thread (se *attr* = NULL, gli attributi sono quelli di default).
- *start_func* è l'indirizzo della funzione di avvio.
- *arg* è l'indirizzo dell'argomento accettato dalla funzione di avvio.
- Restituisce 0 in caso di successo, un intero positivo (secondo `<sys/errno.h>`) in caso di errore.


## Pthreads (Sintassi)

```c
typedef void (*thread_start)(void *);

int pthread_create(pthread_t *tid,
                  const pthread_attr_t *attributes,
                  thread_start start,
                  void *argument);
```

- Restituisce 0 se OK, un codice d'errore altrimenti.
- **tid**: argomento di ritorno, conterrà il tid del nuovo thread.
- **attributes**: attributi del thread (vedere dopo).
- **start**: indirizzo della funzione da cui partire.
- **argument**: l'argomento passato alla funzione start.


## Pthreads (pthread_exit)

`void pthread_exit(void *status);`

- Termina il thread corrente, con valore di uscita *status*.
- Altri thread possono raccogliere il valore di uscita usando `pthread_join`.
- **Attenzione**: i dati puntati da *status* devono sopravvivere alla terminazione del thread!
    - *status* non deve puntare allo stack (no variabili locali).
    - È consentito l'uso di variabili globali o allocate dinamicamente.


## Pthreads (pthread_join)

Un thread può attendere per la terminazione di un altro thread relativo allo stesso processo:

```c
#include <pthread.h>

int pthread_join (pthread_t *tid, void **status);
```

- **tid**: è l'ID del thread del quale si vuole attendere la terminazione.
- **status**: punta al valore restituito dal thread per cui si è atteso (se *status* = NULL, tale stato non viene restituito).
- Restituisce 0 in caso di successo, un intero positivo (secondo `<sys/errno.h>`) in caso di errore.


## Pthreads (Esempio TID)

```c
#include <pthread.h>
#include <stdio.h>
#include <errno.h>

void *start_func(void *arg) /* funzione di avvio */
{
    printf("%s", (char *)arg);
    printf(" and my TID is: %d\n", (int)pthread_self());
}

int main(void)
{
    int en;
    pthread_t tid1, tid2;
    char *msg1 = "Hello world, I am thread #1";
    char *msg2 = "Hello world, I am thread #2";

    printf("The launching process has PID:%d\n", (int)getpid());

    printf("The main thread has TID:%d\n", (int)pthread_self());
}
```


## Pthreads (Esempio TID - Continuazione)

*(Stessa struttura del codice precedente)*

```c
/* crea il 1mo thread */
if ((en = pthread_create(&tid1, NULL, start_func, msg1)!=0))
    errno=en, perror("pthread_create"), exit(1);

/* crea il 2ndo thread */
if ((en = pthread_create(&tid2, NULL, start_func, msg2)!=0))
    errno=en, perror("pthread_create"), exit(2);

/* attende per il 1mo */
if ((en = pthread_join(tid1, NULL)!=0))
    errno=en, perror("pthread_join"), exit(1);

/* attende per il 2ndo */
if ((en = pthread_join(tid2, NULL)!=0))
    errno=en, perror("pthread_join"), exit(2);

return 0;
}
```


## Pthreads (Scope Variabili)

```c
typedef struct foo{
    int a;
    int b;
} myfoo;

myfoo test; // Variabile GLOBALE

void stampa(char *st, struct foo *test){
    printf("%s: tid=%d a=%d b=%d\n", st, pthread_self(),test->a, test->b);
}

void *fun1(void *arg){
    myfoo test2 = {1,2}; // Variabile LOCALE
    printf("%s %d\n", arg, pthread_self());
    stampa(arg, &test2);
    pthread_exit((void *)&test2);
}
```


## Pthreads (Scope Variabili - Varianti)

```cpp
void *fun2(void *arg){
    test.a = 3;
    test.b = 4; // Variabile GLOBALE
    printf("%s %d\n", arg, pthread_self());
    stampa(arg, &test);
    pthread_exit((void *)&test);
}

void *fun3(void *arg){
    myfoo *test3;
    test3=malloc(sizeof(struct foo)); // Variabile allocata dinamicamente
    test3->a = 5;
    test3->b = 6;
    printf("%s %d\n", arg, pthread_self());
    stampa(arg, test3);
    pthread_exit((void *)test3); //c
}
```


## Pthreads (Esecuzione e Risultati)

```c
int main(void){
    char st[100];
    pthread_t tid1;
    pthread_t tid2;
    pthread_t tid3;

    myfoo *b; // PUNTATORE alla struttura (non allocata)

    pthread_create(&tid1, NULL, fun1, "Thread 1"); // Locale
    pthread_join(tid1, (void *)&b);
    stampa("Master ", b);

    pthread_create(&tid2, NULL, fun2, "Thread 2"); // Globale
    pthread_join(tid2, (void *)&b);
    stampa("Master ", b);

    pthread_create(&tid3, NULL, fun3, "Thread 3"); // Dinamica
    pthread_join(tid3, (void *)&b);
    stampa("Master ", b);
}
```


## Pthreads (Output Risultati)

**Thread 1: 1077283760**
// Locale
Thread 1: a=1 b=2
Master : a=1075156600 b=1077281896

**Thread 2: 1077283760**
// Globale
Thread 2: a=3 b=4
Master : a=3 b=4

**Thread 3: 1077283760**
// Dinamica
Thread 3: a=5 b=6
Master : a=5 b=6


## Windows Multithreaded in C

```c
#include <windows.h>
#include <stdio.h>
DWORD Sum; /* data is shared by the thread(s) */

/* the thread runs in this separate function */
DWORD WINAPI Summation(LPVOID Param)
{
    DWORD Upper = *(DWORD*)Param;
    for (DWORD i = 0; i <= Upper; i++)
        Sum += i;
    return 0;
}

int main(int argc, char *argv[])
{
    DWORD ThreadId;
    HANDLE ThreadHandle;
    int Param;

    if (argc != 2) {
        fprintf(stderr,"An integer parameter is required\n");
        return -1;
    }
    Param = atoi(argv[1]);
    if (Param < 0) {
        fprintf(stderr,"An integer >= 0 is required\n");
        return -1;
    }
}
```

**Windows API Note:**
- **DWORD**: 32-bit unsigned int
- **LPVOID**: puntatore void
- **Funzione di avvio**: Simile a Pthread


## Windows Multithreaded in C (Codice)

```c
/* create the thread */
ThreadHandle = CreateThread(
    NULL, /* default security attributes */
    0, /* default stack size */
    Summation, /* thread function */
    &Param, /* parameter to thread function */
    0, /* default creation flags */
    &ThreadId); /* returns the thread identifier */

if (ThreadHandle != NULL) {
    /* now wait for the thread to finish */
    WaitForSingleObject(ThreadHandle, INFINITE);

    /* close the thread handle */
    CloseHandle(ThreadHandle);

    printf("sum = %d\n", Sum);
}
}
```

**Note:** Creazione e attesa del thread sono simili alla logica di Pthread.


## Threading implicito

È una tecnica sempre più popolare al crescere della complessità dei sistemi multithread. La creazione e gestione dei thread è affidata a **compilatori** e **librerie run-time** invece che ai programmatori.

In questo caso, il programmatore identifica dei **task** e non dei thread.

**Tre metodi considerati:**
- Thread Pools
- OpenMP
- Grand Central Dispatch


## Pool di Thread

- Si crea un numero di thread in attesa in un pool.
- Se richiesto un thread per un servizio e non c'è attesa, viene assegnato.

**Vantaggi:**
- Solitamente più veloce nel servire una richiesta quando il thread esiste già.
- Il numero dei thread per l'applicazione è limitato dalla dimensione del pool.
- Separa il task da eseguire dal meccanismo per creare il task e permette differenti strategie di esecuzione (es. scheduling periodico).

**Windows API per thread pool:**
- Thread function da eseguire con un thread del pool.

```cpp
DWORD WINAPI PoolFunction( PVOID Param) {
    /*
     * this function runs as a separate thread.
     */
}
```


## Pool di Thread (QueueUserWorkItem)

Un puntatore a `PoolFunction()` è passato ad una delle funzioni delle API del thread pool e un thread dal pool la esegue.

Una di queste funzioni è `QueueUserWorkItem` che ha 3 parametri:
- **LPTHREAD_START_ROUTINE Function**: il puntatore alla funzione da eseguire.
- **PVOID Param**: i parametri passati alla funzione.
- **ULONG Flags**: flag che indicano come il thread pool deve gestire l'esecuzione.

**Esempio di chiamata:**
`QueueUserWorkItem(&PoolFunction, NULL, 0);`
(Porta uno dei thread del pool ad invocare la `PoolFunction()`).


## OpenMP

- Direttive di compilazione ed API per C, C++, FORTRAN.
- Supporto per programmazione parallela in ambienti in **shared-memory**.
- Identifica regioni parallele (blocchi di codice parallelizzabili).

`#pragma omp parallel`
- Crea tanti thread quanti sono i core.
- Esegui il loop in parallelo.

`#pragma omp parallel for`

```c
for(i=0;i<N;i++) {
    c[i] = a[i] + b[i];
}
```

**Compilazione:** `gcc -fopenmp prog.c`

**Esempio Open Multi-Processing:**

```c
#include <omp.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    /* sequential code */

    #pragma omp parallel
    printf("I am a parallel region.");
}

/* sequential code */

return 0;
}
```


## Problematiche Threading

- Semantica delle chiamate `fork()` ed `exec()`.
- **Signal handling** (Sincrono e asincrono).
- Cancellazione thread (Asincrono o deferred).
- Thread-local storage.
- Attivazione Scheduler.


## Semantica di fork() ed exec()

- **fork()**: Duplica solo il thread chiamante o tutti i thread del processo?
    - Per alcune versioni di UNIX esistono due versioni di fork.
    - Spesso duplica solo il thread chiamante.
- **exec()**: Funziona normalmente – sovrascrive il processo in esecuzione inclusi i thread.


## Signal Handling

- Un **“segnale”** è un interrupt “software”.
    - Terminologia corretta: “exception”.
    - “Interrupt” è usato solo per gli interrupt “hardware”.
- Consente la comunicazione asincrona tra processi e/o tra device e processo.
- Ogni segnale ha un proprio nome:
    - Cominciano per **“SIG”**.
    - Definiti in `<signal.h>`.
    - Associati ad interi positivi.


## Signal Handling (Processo)

I segnali in UNIX notificano eventi ai processi. Un **signal handler** è usato per processare i segnali.

**Flusso:**
1. Generato da evento.
2. Mandato ad un processo.
3. Signal handler:
    1. Default.
    2. User-defined.

Ogni segnale ha un default handler che il kernel esegue. Il *user-defined signal handler* sovrascrive il default.
Per i sistemi *single-threaded*, i segnali sono mandati al processo.


## Segnali (Unix)

**Caratteristiche dei segnali:**
- Ogni segnale ha un identificatore (inizia con **SIG**, es. `SIGABRT`).
- Numero segnali: 15-40, a seconda della versione di UNIX (POSIX: 18, Linux: 38).
- I nomi simbolici corrispondono ad un intero positivo.

**Costanti:**
- Definite internamente in header specifici (es. `bits/signum.h`).
- L'interfaccia standard POSIX è `<signal.h>`.


## Segnali (Unix) - Trigger

- **Pressione di tasti speciali:** Es: `ctrl-c` genera `SIGINT`.
- **Eccezioni hardware:**
    - Divisione per 0 (`SIGFPE`).
    - Riferimento non valido a memoria (`SIGSEGV`).
    - L'interrupt viene generato dall'hardware, catturato dal kernel, che invia il segnale al processo.
- **System call kill:**
    - Permette di spedire un segnale ad un altro processo.
    - Limitazione: l'uid del processo che esegue `kill` deve essere lo stesso del destinatario, oppure 0 (root).


## Tabella Segnali (Unix)

| Segnale | Origine | Default | Note |
| :--- | :--- | :--- | :--- |
| SIGINT | Ctrl+C | terminate | interrupt |
| SIGQUIT | Ctrl+\ | terminate + core dump | debug |
| SIGTERM | kill | terminate | terminazione “gentile” |
| SIGKILL* | kill | terminate | NON intercettabile |
| SIGSTOP* | kernel | stop | NON intercettabile |
| SIGTSTP | Ctrl+Z | stop | sospensione |
| SIGCHLD | sistema | ignore | figlio terminato |
| SIGALRM | timer | terminate | alarm |
| SIGSEGV | errore | terminate + core dump | invalid memory |
| SIGUSR1 | user | terminate | custom |


## Segnali (Unix) - Trasmissione

- I segnali vengono inviati in modo **asincrono**. Non è possibile sapere quando il processo li riceverà.
- È possibile indicare al kernel l'azione da intraprendere:
    - **Ignora**: Valida per quasi tutti tranne SIGKILL e SIGSTOP.
    - **“Catch”**: Indica una procedura da eseguire (signal handler). Es: `SIGCHLD` (operazioni figlio), `SIGINT` (cancella file).
    - **Default**: Esegui l'azione predefinita.


## Segnali (Unix) - Handler

Un handler è una funzione del tipo:

```c
void funzione(int num_segnale) {
    printf("%d", num_segnale);
}
```

Una volta che l'handler termina, si torna al punto in cui il programma era stato interrotto.


## Segnali (Unix) - Gestione POSIX

```c
typedef void (*sighandler_t)(int);
sighandler_t signal(int signum, sighandler_t handler);
```

- `signal(SIGINT, foo)`: imposta la funzione *foo* come handler per `SIGINT`.
- `signal(SIGINT, SIG_IGN)`: richiede di ignorare il segnale.
- `signal(SIGINT, SIG_DFL)`: ritorna alla reazione di default.


## Segnali (Unix) - kill

```c
int kill(pid_t pid, int sig);
```

- `kill(127, SIGINT)`: invia il segnale `SIGINT` al processo con pid 127.
- Restituisce 0 in caso di successo e -1 in caso di errore.


## Segnali (Unix) - Esempio con alarm

```c
void foo(int num_segnale);
int main(void){
    int n=0;    int buf[100];
    alarm(5);
    signal(SIGALRM,foo);

    while (n<=0){
        printf("Digitare qualcosa:\n");
        alarm(1);
        if ((n=read(STDIN_FILENO,buf,10))<0)
            perror("Read error");
        alarm(0);
    }
}

void foo(int num_segnale) {
    alarm(1);
    printf("Vuoi muoverti a digitare qualcosa ???\n");
}
```


## Signal Handling - Multi-threading

Se il sistema è multi-threaded, il segnale può essere inviato:
- Al thread a cui si applica.
- A tutti i thread del processo.
- A specifici thread del processo.
- Assegnando ad un thread specifico il compito di ricevere tutti i segnali del processo.


## Signal Handling - pthread_kill

```c
int pthread_kill(pthread_t tid, int signo);
```

- Manda il segnale *signo* al thread specificato da *tid*.
- Se è impostato un handler, viene eseguito nel thread *tid*.
- Se non è impostato un handler e il comportamento di default è la terminazione, vengono terminati tutti i thread.
- Restituisce 0 se OK, un codice d'errore altrimenti.


## Signal Handling - Maschere e Blocchi

*(Codice esemplificativo sulla gestione delle maschere dei segnali)*

Le maschere dei segnali sono sia al livello di processi che di thread:
- `int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);`
- `int pthread_sigmask(int how, const sigset_t *set, sigset_t *oldset);`


## Signal Handling - Segnali Pending

**Comportamento dei segnali pending**
Quando un segnale è bloccato, diventa *pending*. La gestione dipende dal tipo:

**Segnali standard** (es. SIGINT, SIGUSR1)
- **NON accodati**.
- Per ogni segnale può esserci al massimo una istanza pending.
- Segnali multipli dello stesso tipo vengono collassati in uno.
- *Esempio:* arrivano 5 SIGUSR1 mentre è bloccato → 1 solo pending → allo sblocco il handler viene eseguito 1 volta.

**Segnali real-time** (SIGRTMIN ... SIGRTMAX)
- **Accodati (FIFO)**.
- Ogni invio genera una nuova istanza pending.
- I segnali vengono consegnati tutti e in ordine.
- *Esempio:* arrivano 5 SIGRTMIN → 5 pending → allo sblocco il handler viene eseguito 5 volte.


## Cancellazione Thread

- Terminare un thread prima che sia finito.
- Il thread da cancellare è il *target thread*.

**Due approcci:**
1. **Asynchronous cancellation**: termina il target thread subito.
2. **Deferred cancellation**: permette al target thread di controllare periodicamente se deve essere cancellato.

**Codice Pthread:**
```c
pthread_t tid;
pthread_create(&tid, 0, worker, NULL);
// ...
pthread_cancel(tid);
```


## Cancellazione Thread - Stati

La cancellazione effettiva dipende dallo stato del thread:

| Mode | State | Type |
| :--- | :--- | :--- |
| Off | Disabled | – |
| Deferred | Enabled | Deferred |
| Asynchronous | Enabled | Asynchronous |

- Se la cancellazione è disabilitata, rimane pending finché il thread non la consente.
- Il default è **deferred**: la cancellazione avviene solo quando il thread raggiunge un **cancellation point** (allora viene invocato il *cleanup handler*).
- Su Linux la cancellazione dei thread è gestita con segnali.


## Cancellazione Thread - Esempi di Cancellation Points

| Tipo | Esempi |
| :--- | :--- |
| Sleep | sleep, nanosleep |
| I/O | read, write |
| Sync | pthread_cond_wait |
| Rete | recv, accept |
| Manuale | pthread_testcancel |

Se il thread esegue puro calcolo (CPU bound), va inserito manualmente:
```cpp
while (1) {
    // lavoro CPU-bound
    pthread_testcancel(); // punto inserito a mano
}
```


## Cancellazione Thread (Posix)

In ogni istante, un thread può essere cancellabile o non cancellabile.
- Quando partono tutti i thread sono cancellabili.
- Quando un altro thread chiama `pthread_cancel`:
    - Se il thread è cancellabile, viene cancellato.
    - Se non è cancellabile, la richiesta viene memorizzata in attesa che il thread diventi cancellabile.


## Comandi per Thread

| Comando | Cosa mostra | Nome ID thread | Note |
| :--- | :--- | :--- | :--- |
| `ps -T -p <PID>` | thread di un processo | SPID / TID | ogni riga = thread |
| `ps -eLf` | tutti i thread del sistema | LWP | vista completa |
| `ps -L -p <PID>` | thread di un processo | LWP | alternativa a -T |
| `top -H -p <PID>` | thread di un processo live | SPID | molto usato |
| `htop -H` | thread con UI | TID | più leggibile |
| `ls /proc/<PID>/task` | thread (livello kernel) | directory = TID | ogni cartella = thread |


## Thread-Specific Data (TSD)

**Thread-local storage (TLS)** o **Thread-specific Data (TSD)**
- Nei thread vari, le variabili globali sono condivise, quelle locali no.
- Ogni thread può mantenere una sua copia dei dati.
- Utile quando non si controlla direttamente la creazione dei thread (es. thread pool).

**Differenza rispetto alle variabili locali:**
- Variabili locali: visibili solo per una singola invocazione di funzione.
- TSD: visibile per più invocazioni di funzione.

**Similitudine con dati statici:**
- TSD è unico per ogni thread ma senza *race condition*.


## Thread-Specific Data (Posix)

- Ogni thread possiede un’area di memoria privata, la **TSD area**, indicizzata da chiavi.
- L'area contiene associazioni tra le chiavi e un valore di tipo `void*`.
    - Diversi thread possono usare le stesse chiavi, ma i valori associati variano da thread a thread.
    - Inizialmente tutte le chiavi sono associate a NULL.


## Thread-Specific Data (Posix) - Esempio di Associazione

Processo principale:
1. `pthread_key_t chiave;` (variabile globale)
2. Inizializza la chiave.
3. Crea i thread.

Thread 1:
`pthread_setspecific(chiave, malloc(...));`
...
`void *p = pthread_getspecific(chiave)`

Thread 2:
`pthread_setspecific(chiave, malloc(...));`
...
`void *p = pthread_getspecific(chiave)`


## Thread-Specific Data (Posix) - Funzioni

- `int pthread_key_create(…)`: per creare una chiave TSD.
- `int pthread_key_delete(…)`: per deallocare una chiave TSD.
- `int pthread_setspecific(…)`: per associare un valore ad una chiave TSD.
- `void *pthread_getspecific(…)`: per ottenere il valore associato a una chiave TSD.


## Thread-Specific Data (Posix) - Destruttori

```c
int pthread_key_create(pthread_key_t *key,
void (*destructor)(void *));
```

- Crea una chiave per dati privati.
- **destructor**: puntatore alla funzione distruttore che deve essere chiamata alla terminazione di un thread (`pthread_exit()`).
- Restituisce 0 se OK, un codice d'errore altrimenti.


## Thread-Specific Data (Posix) - Associazione e Recupero

```c
int pthread_setspecific(pthread_key_t *key,
    const void* val);

/* associa l'indirizzo val alla chiave key, per il thread chiamante */
/* restituisce 0 se OK, un codice d'errore altrimenti */

void* pthread_getspecific(pthread_key_t *key);

/* restituisce l'indirizzo associato alla chiave key nel thread chiamante */
/* restituisce NULL se nessun indirizzo è stato associato a key */
```


## Thread-Specific Data (Posix) - Esempio Log File

*(Esempio di gestione di file log unici per ogni thread tramite TSD)*

```cpp
#include ...
static pthread_key_t thread_log_key; /* tsd key per thread */

void write_to_thread_log (const char* message); // Scrive log
void close_thread_log (void* thread_log); // Chiude file log
void* thread_function (void* args); // Eseguita dai thread

int main() {
    // Crea una chiave da associare al log Thread-Specific
    pthread_key_create(&thread_log_key, close_thread_log);
    // Crea 5 thread che facciano il lavoro
    for (int i = 0; i < 5; ++i)
        pthread_create(&(threads[i]), NULL, thread_function, NULL);
    // Aspetta che tutti finiscano
    for (int i = 0; i < 5; ++i)
        pthread_join(threads[i], NULL);
    return 0;
}
...
```


## Thread-Specific Data (Posix) - Implementazione Log

```cpp
void write_to_thread_log (const char* message) {
    FILE* thread_log = (FILE*)pthread_getspecific(thread_log_key);
    fprintf (thread_log, "%s\n", message);
}

void close_thread_log (void* thread_log) {
    fclose ((FILE*) thread_log);
}

void* thread_function (void* args) {
    char thread_log_filename[20];
    FILE* thread_log;
    sprintf(thread_log_filename,"thread%d.log",(int)pthread_self());

    thread_log = fopen (thread_log_filename, "w");
    /* Associa la struttura FILE TSD a thread_log_key. */
    pthread_setspecific (thread_log_key, thread_log);

    write_to_thread_log ("Thread starting.");
    /* Fai altro lavoro qui... */ 
    return NULL;
}
```


## Esempi in SO

- Linux Threads
- Windows Threads


## Thread Linux

Linux si riferisce a **tasks** piuttosto che a **threads**, unificando la gestione di processi e thread.

- La creazione di thread è gestita dalla chiamata di sistema **clone()**.
- Usata per implementare **pthread_create**.
- **clone()** permette ad un *child task* di condividere l’*address space* del *parent task* (processo).

**Flag di controllo:**

| flag | meaning |
| :--- | :--- |
| CLONE_FS | File-system information is shared. |
| CLONE_VM | The same memory space is shared. |
| CLONE_SIGHAND | Signal handlers are shared. |
| CLONE_FILES | The set of open files is shared. |

Viene comunque usata la chiamata a `fork()`: `do_fork()`.
- Se tutte le flag sono settate, `clone` si comporta come un thread.
- Se tutte non sono settate, si comporta come un `fork`.

La **struct task_struct** punta alle strutture dati del processo (condivise o uniche), permettendo una gestione uniforme.


## Thread Linux - Esempio clone()

```cpp
int thread_func(void *arg) {
    printf("Hello from the new thread! Arg: %s\n", (char *)arg);
    return 0;
}

int main() {
    char *child_stack = malloc(1024 * 1024); // Allocazione dello stack
    if (child_stack == NULL) {
        perror("malloc");
        exit(1);
    }

    // Creazione del nuovo thread con clone()
    pid_t pid = clone(thread_func, child_stack + 1024 * 1024, CLONE_VM | CLONE_FS | CLONE_FILES |
        CLONE_SIGHAND | CLONE_THREAD, "Thread Arg");

    if (pid == -1) {
        perror("clone");
        exit(1);
    }

    printf("Thread created with pid: %d\n", pid);
    sleep(1); // Aspetta che il thread finisca
    free(child_stack); // Libera lo stack

    return 0;
}
```


## Windows Threads

Strutture dati del thread includono:

- **ETHREAD** (executive thread block) – include puntatore al processo al quale il thread appartiene, puntatore alla routine da dove parte il thread, puntatore a KTHREAD nel kernel space.
- **KTHREAD** (kernel thread block) – info di scheduling e sincronizzazione, kernel-mode stack, puntatore a TEB nel user space.
- **TEB** (thread environment block) – thread id, user-mode stack, thread-local storage, nello user space.

*(Schema spaziale: Kernel space vs User space)*


## Windows Threads Data Structures

**ETHREAD**
- Thread start address
- Pointer to parent process

**KTHREAD**
- Scheduling and synchronization information
- Kernel stack

**TEB**
- Thread identifier
- User stack
- Thread-local storage