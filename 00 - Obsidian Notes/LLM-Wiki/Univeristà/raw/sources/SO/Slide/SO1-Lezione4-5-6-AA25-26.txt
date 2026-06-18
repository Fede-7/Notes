## Pagina 1

Lezione 5: Processi

---

## Pagina 2

Obiettivi

- Nozione di processo
- Caratteristiche dei processi (schedulazione, creazione, terminazione, comunicazione, etc.)
- Comunicazione interprocesso
- Comunicazione nei sistemi client-server

---

## Pagina 3

Definizione di Processo

Un SO esegue programmi di varia natura:
- Sistemi batch – job
- Sistemi time-shared – programmi utente o task
- Job è più astratto: lavoro computazionale (che può generare processi)
- I libri di testo usano job e processo in modo quasi intercambiabile

Processo – è un programma in esecuzione
- Un programma è un’entità passiva archiviata su disco (file eseguibile), un processo è attivo (in esecuzione)
- Unità di attività computazionale coerente di un moderno SO
- Esecuzione sequenziale
- Un processo richiede risorse (CPU, memoria, file, dispositivi I/O) per l’esecuzione di un compito (task)
- Un programma può chiamare molti processi
- I sistemi sono il risultato dell’esecuzione di più processi concorreti
  - processi di sistema e processi utente

---

## Pagina 4

Definizione di Processo

□ **Processo** – è un programma in esecuzione:
  □ Stato corrente **program counter** e **registri del processore**
  □ Layout di memoria

□ Layout di memoria:
  □ Il codice del programma, chiamata **sezione testo**
  □ **Sezione Dati** contenente le variabili globali
  □ **Stack** contenente i dati temporanei
    ► Parameteri di funzione, indirizzi di ritorno, variabili locali
  □ **Heap** contenente memoria dinamicamente allocata a run time durante l’esecuzione di un task

---

## Pagina 5

Processo Allocato in Memoria

□ Processo – è un programma in esecuzione:

□ Layout di memoria:
  □ Text e Data dimensione fissata
  □ Stack e Heap variabili a run time

Non initialized data anche indicate come block started by symbol (bss)

---

## Pagina 6

Stato di un Processo

Durante l’esecuzione un processo può cambiare il suo stato

- **new**: il processo è stato creato
- **running**: esecuzione delle istruzioni del processo
- **waiting**: il processo è in attesa di un evento per proseguire (es. I/O)
- **ready**: il processo è in attesa di essere assegnato a processore
- **terminated**: il processo ha finite l’esecuzione

---

## Pagina 7

Descrittore di Processo

- Il Sistema Operativo mantiene una tabella dei processi

- Per ogni processo una entry (Task Control Block)
  - Stato del processo - running, waiting, etc
  - IDs del processo - identificativi di processo
  - Program counter - locazione prossima istruzione
  - Registri CPU - contenuto registri CPU
  - Scheduling di CPU - priorità, parametri di scheduling
  - Memoria - memoria allocata per il processo (es. base and limit registers, tabella delle pagine, etc.)
  - Contabilità - CPU usata, tempo clock dallo start, numero di processo, etc.
  - Stato I/O - dispositivi I/O allocati, lista di file aperti, etc.

---

## Pagina 8

Tabella Processi in Linux

In Linux la PCB è rappresentata in C da una task_struct specificata nel codice sorgente del kernel (in /linux/sched.h)

Alcuni campi seguono:

```c
pid t_pid; /* process identifier */
long state; /* state of the process */
unsigned int time_slice /* scheduling information */
struct task_struct *parent; /* this process’s parent */
struct list_head children; /* this process’s children */
struct files_struct *files; /* list of open files */
struct mm_struct *mm; /* address space of this process */
```

Nel kernel Linux i processi attivi sono representati da una lista doppiamente linkata

current (currently executing process)

---

## Pagina 9

Commutazione tra Processi

- La tabella dei processi supporta la commutazione tra processi
- Lo stato dei processi salvato e ripristinato durante gli switch

Diagram showing the process flow with interrupt or system call branches. Process $P_0$, operating system, and process $P_1$ are represented. Executing processes save state into PCB$_0$, reload state from PCB$_1$, and execute processes save state into PCB$_1$, reload state from PCB$_0$.

---

## Pagina 10

Processi e Thread

- I moderni Sistemi Operativi consentono ai processi di gestire l’esecuzione di più flussi di controllo (thread)

- I processi possono diramarsi in più sottounità di esecuzione
  - Più program counter per un processo
  - Multipli flussi di controllo -> threads
    - Condividono identità e risorse di processo ma hanno diverso stato esecutivo
  - Archiviazioni di ulteriori informazione per thread in PCB

---

## Pagina 11

Schedulazione di Processi

- Massimizza l’uso della CPU, fa velocemente lo switch di processi nella CPU per il time sharing
- Schedulatore dei processi seleziona tra processi disponibili per la prossima esecuzione su CPU
- Mantiene la coda di scheduling dei processi
  - Job queue – insieme di tutti i processi nel sistema
  - Ready queue – insieme di tutti i processi in memoria principale, pronti (ready)
  - Wait queue – insieme dei processi in attesa (waiting)
  - Device queues – insieme di processi in attesa (waiting) di un dispositivo di I/O
  - I processi migrano tra le diverse code

---

## Pagina 12

Code Processi Ready e Waiting

Mantiene la coda di scheduling dei processi

- **Job queue** – insieme di tutti i processi nel sistema
- **Ready queue** – insieme di tutti i processi in memoria principale, pronti (ready) per l’esecuzione
- **Wait queue** – insieme dei processi in attesa (waiting)
- **Device queues** – insieme di processi in attesa (waiting) di un dispositivo di I/O
- I processi migrano tra le diverse code

---

## Pagina 13

Rappresentazione Scheduling dei Processi

Diagramma di accodamento
- Un nuovo processo in coda ready attende la CPU
- Una volta allocata diversi eventi possono avvenire (I/O, fine tempo, fork, wait)

---

## Pagina 14

Scheduler

□ **Short-term scheduler** (o **CPU scheduler**) – seleziona quale processo deve essere eseguito dalla CPU
  □ A volte l’unico scheduler nel sistema
  □ Lo short-term scheduler è invocato frequentemente (millisecondi) ⇒ (deve essere veloce)

□ **Long-term scheduler** (o **job scheduler**) – seleziona quale processo deve essere portato nella coda ready
  □ Long-term scheduler non frequente (secondi, minuti) ⇒ (può essere lento)
  □ Il long-term scheduler controlla il **grado di multiprogrammazione**
  □ I processi possono essere descritti come:
    ► **I/O-bound process** – spende più tempo in operazioni I/O che in computazione, piccoli e brevi accessi in CPU
    ► **CPU-bound process** – spende più tempo in computazione; pochi e lunghi accessi in CPU
    ► Long-term scheduler cerca di trovare una buona combinazione di processi

---

## Pagina 15

Scheduling di Medio Termine

- Medium-term scheduler può essere aggiunto se il grado di multiprogrammazione deve decrescere (minor contesa per CPU)
- Toglie processi dalla memoria, archivia su disco, riporta in memoria da disco per continuare l’esecuzione: swapping

---

## Pagina 16

Context Switch

- Al passaggio della CPU ad un altro processo il sistema deve salvare lo stato del vecchio processo e caricare lo stato salvato del nuovo processo attraverso un context switch
- Context (contesto) di processo representato in PCB

- Il tempo di context-switch è un overhead
  - il sistema non fa lavoro “utile” durante lo switching
  - Più è complesso il sistema e la PCB più è lungo il context switch

- Il tempo depende dal supporto hardware
  - Alcuni hardware forniscono registri multipli per CPU consentendo caricamenti di più context in una volta

---

## Pagina 17

Operazioni su Processi

Il Sistema deve fornire meccanismi per:
- Creazione di processi,
- Terminazione di processi,
- Comunicazione tra processi
- Sincronizzazione tra processi
- Altri meccanismi di gestione di processi (dettagliato dopo)

---

## Pagina 18

Creazione di Processi

- Processo padre crea un processo figlio, che a sua volta crea crea altri processi formando un albero di processi
- Processi identificati e gestiti con identificatori di processo (pid)

- Condivisione di risorse (opzioni)
  - Padre e figlio condividono tutte le risorse
  - Figlio condivide un sottoinsieme delle risorse del padre
  - Padre e figlio non condividono alcuna risorsa

- Opzioni di esecuzione
  - Padre e figlio vengono eseguiti in concorrenza
  - Padre aspetta che il figlio finisca

---

## Pagina 19

Albero di Processi in Linux

System deamon fa l’init
Logind gestisce il log nel Sistema
L’utente lancia una shell bash, fa ps e vim

In UNIX il primo processo è init

Per vedere l’albero dei processi da bash: pstree

---

## Pagina 20

Creazione di Processi

Diverse gestioni
- Spazio memoria
  - Figlio duplica quello del padre
  - Figlio ha un programma caricato
- Esecuzione:
  - Padre e figlio concorrenti o padre attende figlio

Esempi UNIX
- fork() system call crea nuovo processo
- exec() system call usata dopo la fork() per sostituire lo spazio di memoria con un nuovo programma

---

## Pagina 21

Programma C con fork ed exec

```c
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
pid_t pid;

    /* fork a child process */
    pid = fork();

    if (pid < 0) { /* error occurred */
        fprintf(stderr, "Fork Failed");
        return 1;
    }
    else if (pid == 0) { /* child process */
        execlp("/bin/ls","ls",NULL);
    }
    else { /* parent process */
        /* parent will wait for the child to complete */
        wait(NULL);
        printf("Child Complete");
    }

    return 0;
}
```

---

## Pagina 22

Programma C con fork ed exec

**exec**

- **DATI**
- **CODICE**

**Programma**

- **Environment***
  - User stack & heap
  - bss
  - initialized data
  - User text
- **Process Control Block**
  - PCB*
  - kernel stack
  - kernel code (shared)
- **Layout processo**

- **Environment***
  - User stack & heap
  - bss
  - initialized data
  - User text
- **Process Control Block**
  - PCB*
  - kernel stack
  - kernel code (shared)
- **Layout processo**

---

## Pagina 23

Programma C con fork

```c
int main(void) {
    int i;

    for (i=0; i<2; i++)
        if (fork()>0) {
            printf("Padre! %d\n", i);
        } else {
            printf("Figlio! %d\n", i);
        }

    sleep(10);
    return 0;
}
```

• Qual è l'output di questo programma?
• Quanti processi vengono creati?
• Di chi è figlio ciascun processo creato?

---

## Pagina 24

Programma C con fork

$$\begin{array}{l}
\$ ./a.out
padre 0
padre 1
figlio! 0
padre 1
figlio! 1
figlio! 1
\end{array}$$

Proc principale

padre 0
figlio! 0

padre1  figlio! 1
padre1  figlio! 1

---

## Pagina 25

Terminazione Processo

- I processi eseguono le ultime istruzioni e poi chiedono all’SO di uscire con la call di sistema `exit()`
  - Ritorna i dati di status data dal figlio al padre (via `wait()`)
  - Le risorse sono deallocate dall’SO

- Padri possono terminare le esecuzioni dei processi figli con la call `abort()` ad esempio perché:
  - Il figlio ha allocato risorse in eccesso
  - Il task del figlio non è più richiesto
  - Il genitore esce e non consente a un figlio di continuare

---

## Pagina 26

Terminazione Processo

- Alcuni SO non permettono ai figli di esistere se i padri hanno terminato
  - Se un processo termina tutti i figli terminano
  - **cascading termination** (tutta la gerarchia di figli terminata)
  - la terminazione è gestita dal SO

- Il padre può aspettare la terminazione di un figlio con la call `wait()`
  - riceve informazioni di stato e il pid del processo terminato, es. Unix
    ```bash
    pid = wait(&status);
    ```

- In Unix/Linux se non c’è padre in waiting il figlio diventa **zombie**

- Se padre termina prima del figlio senza invocare `wait` il figlio è **orphan**
  - In Unix adottato da init che chiama continuamente wait per accogliere lo status (in linux init è oggi systemd – System Daemon)

---

## Pagina 27

Terminazione Processo

In UNIX/Linux

inesistente
fork()
runnable
scelto dallo scheduler
fermato dallo scheduler (preempted)
running
exit()
main: return
terminato (zombie)
evento o segnale
stopped
aspetta qualcosa (pause, read, sleep)

invia SIGCHLD al padre

---

## Pagina 28

Terminazione Processo

In UNIX/Linux

/* status.c: Fornisce un esempio dei diversi stati di uscita di un processo figlio */

```c
#include<sys/types.h> /* per il tipo pid_t */
#include <unistd.h> /* per la funzione fork */
#include<sys/wait.h> /* per la funzione waitpid */
#include <stdio.h> /* per le funz. printf, fgets e perror */
#include <stdlib.h> /* per la funzione exit */
#include <string.h> /* per la funzione strlen */
#include <errno.h> /* per la messaggistica di errore */

int main(void)
{
    pid_t pid;
    int status;

    if ( (pid = fork()) < 0)
        perror("fork"), exit(1);
    else if (pid == 0) /* primo figlio... */
        exit(7); /* che termina in modo normale */

    if (wait(&status) != pid) /* il genitore aspetta il figlio... */
        perror("wait"), exit(1);
    print_exit(status); /* e ne mostra lo stato di terminazione */

    if ( (pid = fork()) < 0)
        perror("fork"), exit(1);
    else if (pid == 0) /* secondo figlio... */
        abort(); /* che genera SIGABRT */

    if (wait(&status) != pid) /* il genitore aspetta il 2ndo figlio... */
        perror("fork"), exit(1);
    print_exit(status); /* e ne mostra lo stato di terminazione */

    if ( (pid = fork()) < 0)
        perror("fork"), exit(1);
    else if (pid == 0) /* terzo figlio... */
        status /= 0; /* che divide per 0 e genera SIGFPE */

    if (wait(&status) != pid) /* il genitore aspetta il terzo figlio... */
        perror("wait"), exit(1);
    print_exit(status); /* e ne mostra lo stato di terminazione */

    exit(0);
}
```

---

## Pagina 29

Terminazione Processo

In UNIX/Linux
- Stato di uscita
  15 8 7 0
  | exit code | signal |
  +----------------+----------------+
  int status;

  wait(&status);
  if ( WIFEXITED(status) )
    printf("valore di uscita: %d\n", WEXITSTATUS(status));
  else
    printf("terminazione anomala\n");

  #define WIFEXITED(status) (((status) & 0x7F) == 0) -> 7 bit meno significativi

  E.g., status = 10000000 with 0x7F = 01111111 (7 bit a 1)

---

## Pagina 30

Architetture Multiprocesso – Chrome Browser

- Molti web browser giravano come un singlo processo (alcuni ancora)
  - Se un website causa problemi il browser può crashare o stallare

- Google Chrome Browser è multiprocesso con differenti tipi di processo:
  - Browser che gestisce l’interfaccia utente, il disco e la rete
  - Renderer che rende graficamente le web pages, gestisce HTML, Javascript. Per ogni sito web aperto è lanciato un nuovo renderer
  - Plug-in per ogni tipo di plug-in

---

## Pagina 31

Communicazione Interprocesso

□ Processi possono essere *independenti o cooperati*
□ Processi cooperanti si influenzano scambiandosi dati
□ Diverse sono le ragioni per la cooperazione tra processi:
  ▶ Condivisione di dati (accesso a dati condivisi)
  ▶ Velocità computazionale (sottoprocessi lavorano in parallelo)
  ▶ Modularità (divisione funzionale dei compiti)

□ Processi cooperanti hanno bisogno di *interprocess communication (IPC)*
□ Due modelli principali di IPC
  ▶ Shared memory
  ▶ Message passing

---

## Pagina 32

Modelli di Communicazione

(a) Message passing. (b) shared memory.

Scambio di poca informazione, tutti gli scambi passano per il Kernel

Più veloce (kernel alloca la zona condivisa), più semplice accesso, problema coordinazione tra processi

---

## Pagina 33

Memoria Condivisa

□ Comunicazione su regione di shared memory

□ Tipicamente creata nello spazio di indirizzamento del processo che la crea (segmento di shared memory)

□ Gli altri processi devono accedere a questo spazio che generalmente è proibito (va rilassata la restrizione)

□ I processi leggono e scrivono su questo spazio che è gestito dai processi (modalità utente)

□ La coordinazione di lettura e scrittura è sotto la responsabilità dei processi coinvolti, il SO lascia fare

---

## Pagina 34

Interprocess Communication – Shared Memory

Area di memoria condivisa tra i processi che desiderano comunicare

- Comunicazione è sotto il controllo dei processi degli utenti non del SO
- Occcorrono meccanismi che consentano ai processi utente di sincronizzarsi quando accedono alla memoria condivisa
- La sincronizzazione è discussa in dettaglio in seguito

---

## Pagina 35

Problema Produttore-Consumatore

□ Si introduce il problema del Produttore-Consumatore
□ Paradigma tipico per processi cooperanti
  □ processo producer produce informazione che è consumata dal processo consumer (es., web server produce html, web browser consuma)

□ Uso di buffer per produrre e consumare
  ▶ Buffer in shared memory
  ▶ Il produttore riempie il buffer
  ▶ Il consumatore svuota il buffer
  ▶ Produttore e consumatore devono sincronizzare le operazioni (mentre il produttore riempie il buffer, il consumatore lo svuota)

□ Due tipi di buffer
  ▶ unbounded-buffer non c’è limite sulla dimensione del buffer (consumatore attende se vuoto)
  ▶ bounded-buffer dimensione fissa del buffer (consumatore attende se vuoto, produttore attende se pieno)

---

## Pagina 36

Bounded-Buffer – Shared-Memory

Un buffer limitato è condiviso tra processi in memoria condivisa

```c
#define BUFFER_SIZE 10
typedef struct {
    .....
} item;

item buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
```

Array circolare con indici in (prossima free) e out (prima posizione full)

Soluzione corretta, ma può allocare fino a BUFFER_SIZE-1 items

- Buffer pieno
- Buffer vuoto
  - ((in + 1) % BUFFER_SIZE) == out
  - in == out

---

## Pagina 37

Bounded-Buffer – Productore

```c
item next_produced;

while (true) {
    /* produce an item in next produced */
    while (((in + 1) % BUFFER_SIZE) == out)
        ; /* do nothing */
    buffer[in] = next_produced;
    in = (in + 1) % BUFFER_SIZE;
}
```

in + 1 = Size, Size % Size = 0 = out

| 1 | 2 | 3 | ... | Size-1 | ? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| in = out =0 | in = 1 | in = 2 | in = 3 | in = Size -2 | in = Size -1 |

---

## Pagina 38

Bounded Buffer – Consumatore

```c
item next_consumed;

while (true) {
    while (in == out)
        ; /* do nothing */
    next_consumed = buffer[out];
    out = (out + 1) % BUFFER_SIZE;

    /* consume the item in next consumed */
}

1 2 3 ... Size-1 ?
out = 0
in = Size - 1
```

---

## Pagina 39

Bounded Buffer – Consumatore

```c
item next_consumed;

while (true) {
    while (in == out)
        ; /* do nothing */
    next_consumed = buffer[out];
    out = (out + 1) % BUFFER_SIZE;

    /* consume the item in next consumed */
}

2 3 ... Size-1 ?
out = 1
in = Size - 1
```

---

## Pagina 40

Bounded-Buffer – Produuttore

item next_produced;

while (true) {
    /* produce an item in next produced */
    while (isBufferFull)
        ; /* do nothing */
    in = (in + 1) % BUFFER_SIZE;
    buffer[in] = next_produced;
    size++;
}

---

## Pagina 41

Bounded Buffer – Consumatore

```cpp
item next_consumed;

while (true) {
    while (isBufferEmpty)
        ; /* do nothing */
    next_consumed = buffer[out];
    out = (out + 1) % BUFFER_SIZE;
    size--;

    /* consume the item in next consumed */
}
```

---

## Pagina 42

Interprocess Communication – Message Passing

- Meccanismi che i processi usano per comunicare e per sincronizzarsi
- Messaggi – processi comunicano senza ricorrere a variabli condivise, ma si scambiano nessaggi
  - La dimensione del message può essere fissa o variabile
- IPC fornisce solitamente due operazioni:
  - send(message)
  - receive(message)

---

## Pagina 43

Message Passing

Se i processi $P$ e $Q$ vogliono comunicare devono:
- Stabilire un canale (communication link) tra loro
- Scambiare messaggi via send/receive

Implementazione:
- Come stabilire il canale?
- Può il canale coinvolgere più di due processi?
- Quanti canali di comunicazione tra coppie di processi comunicanti?
- Capacità di un canale?
- La dimensione del messaggio scambiato sul canale è fisso o variable?
- Il canale è unidirezionale o bi-direzionale?

---

## Pagina 44

Message Passing

□ Implementazione di un canale di comunicazione:

□ Non consideriamo tanto il canale fisico …
  ▶ Memoria condivisa
  ▶ Bus hardware
  ▶ Rete

□ … quanto il canale logico:
  ▶ Comunicazione diretta o indiretta
  ▶ Comunicazione sincrona o asincrona
  ▶ Buffering dei messaggi automatico o esplicito

---

## Pagina 45

Comunicazione Diretta

Processi devono nominarsi esplicitamente (naming):
- **send** ($P, message$) – invia message al processo P
- **receive** ($Q, message$) – riceve message dal processo Q

Propertà del canale di comunicazione:
- Il canale è stabilito automaticamente tra coppie di processi comunicanti (che conoscono l’identità reciproca)
- Il canale è stabilito tra esattamente due processi
- Per ogni coppia c’è esattamente un canale
- Il canale può essere unidirezionale o bi-direzionale

Variante - comunicazione **asimmetrica**:
- **send** ($P, message$) – invia message al processo P
- **receive** ($id, message$) – riceve message da qualunque processo (id ricevuto in ingresso)

Problema: modularità, modificando l’identità di un processo richiede revisione delle comunicazione

---

## Pagina 46

Comunicazione Indiretta

□ Messaggi mandati/ricevuti su mailboxes (o porte):
  □ Ogni mailbox ha un unico id
  □ Processi possono comunicare solo se condividono una mailbox

□ Propertà del canale:
  □ Canale stabilito solo se i processi condividono un mailbox
  □ Canale può essere associato a più processi
  □ Coppie di processi possono condividere più canali
  □ Canali sia unidirezionali che bi-direzionali

---

## Pagina 47

Comunicazione Indiretta

Operazioni
- Creare una nuova mailbox (porta)
- Inviare/ricevere messaggi (send/receive) via mailbox
- distruggere una mailbox

Primitive:
- send(A, message) – invia message alla mailbox A
- receive(A, message) – ricevi message dalla mailbox A

Propertà del canale:
- Canale stabilito solo se i processi condividono un mailbox
- Canale può essere associato a più processi
- Coppie di processi possono condividere più canali
- Canali sia unidirezionali che bi-direzionali

---

## Pagina 48

Comunicazione Indiretta

Condivisione del mailbox
- Si supponga che $P_1$, $P_2$, e $P_3$ condividano la mailbox A
- Se $P_1$, invia M ad A e $P_2$ e $P_3$ ricevono da A
- Chi prende il messaggio M?

Soluzione dipendono dal metodo scelto:
- Permettere una connessione tra solo due processi alla volta
- Permettere ad un processo alla volta di eseguire receive()
- Lasciare al sistema decidere il ricevente (al mittente verrà notificata la decisione)

La mailbox può essere proprietà del SO o di un processo (nello spazio di indirizzamento del processo).
- Per mailbox di proprietà di un processo utente, questo può solo ricevere (indirizzo), altri possono solo inviare (dismissa alla terminazione del processo)
- Se la mailbox è del SO questa non viene dismissa

---

## Pagina 49

Sincronizzazione

La comunicazione tra processi avviene con chiamate send-receive
Il message passing può essere bloccante o non bloccante
Bloccante considerato sincrono
- Blocking send -- mittente è bloccato finché il messaggio non viene ricevuto
- Blocking receive -- destinatario bloccato finché il messaggio non è disponibile

Non bloccante considerato asincrono
- Non-blocking send -- mittente invia il messaggio e continua ad eseguire
- Non-blocking receive -- destinatario riceve:
  - messaggio valido, oppure
  - messaggio nullo

Diverse combinazioni di politiche
- Se bloccati sia il mittente che il destinario abbiamo un rendezvous

---

## Pagina 50

Sincronizzazione

Con sincronizzazione bloccante il problema del produttore consumatore diventa triviale:

- Il produttore invia e attende il consume
- Il consumatore attende e consuma

```c
message next_produced;
while (true) {
    /* produce an item in next produced */
    send(next_produced);
}

message next_consumed;
while (true) {
    receive(next_consumed);

    /* consume the item in next consumed */
}
```

---

## Pagina 51

Buffering

- Lo scambio di messaggi utilizza un canale di comunicazione basato su code temporanee

- Le code sono implementate in tre modi:
  - Capacità zero – zero messaggi in coda, il mittente aspetta che il destinatario riceva (rendezvous)
  - Capacità limitata – capacità di $n$ messaggi in coda, il mittente aspetta se il canale è pieno
  - Capacità illimitata – la coda non ha lunghezza predefinita, il mittente non aspetta mai

- Capacità zero è detto senza buffering
- Capacità non zero è detto con buffering automatico

---

## Pagina 52

Esempio di IPC Systems - POSIX

POSIX Shared Memory

Un processo crea un segmento di shared memory con la call
shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);
- nome, modalità di apertura/creazione, permessi (read e write)
- restituisce un intero (descrittore di file)
- anche usata per aprire un segmento esistente per condividerlo

Creato l’oggetto si setta la dimensione
ftruncate(shm_fd, 4096);
- Settta la dimensione 4096 byte

Crea un memory-mapped file
mmap(0,SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);
- MAP_SHARED specifica che i cambiamenti sono condivisi

È quindi possibile scrivere su shared memory (puntatore) come su file
sprintf(shared memory, "Writing to shared memory");

---

## Pagina 53

IPC POSIX Producer

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>

int main()
{
/* the size (in bytes) of shared memory object */
const int SIZE = 4096;
/* name of the shared memory object */
const char *name = "OS";
/* strings written to shared memory */
const char *message_0 = "Hello";
const char *message_1 = "World!";

/* shared memory file descriptor */
int shm_fd;
/* pointer to shared memory object */
void *ptr;

/* create the shared memory object */
shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);

/* configure the size of the shared memory object */
ftruncate(shm_fd, SIZE);

/* memory map the shared memory object */
ptr = mmap(0, SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);

/* write to the shared memory object */
sprintf(ptr,"%s",message_0);
ptr += strlen(message_0);
sprintf(ptr,"%s",message_1);
ptr += strlen(message_1);

return 0;
}
```

Aperta con nome “OS” in modalità R/W - se non esiste creata con permessi R/W -

Dimensione SIZE

Mappata in memoria in modalità MAP_SHARED - cambiamenti visibili a chi condivide la memoria

PROT_WRITE permette la scrittura

Puntatore ptr incrementato in modalità non automatica

---

## Pagina 54

IPC POSIX Consumer

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>

int main()
{
/* the size (in bytes) of shared memory object */
const int SIZE = 4096;
/* name of the shared memory object */
const char *name = "OS";
/* shared memory file descriptor */
int shm_fd;
/* pointer to shared memory object */
void *ptr;

/* open the shared memory object */
shm_fd = shm_open(name, O_RDONLY, 0666);

/* memory map the shared memory object */
ptr = mmap(0, SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);

/* read from the shared memory object */
printf("%s", (char *)ptr);

/* remove the shared memory object */
shm_unlink(name);

return 0;
}
```

Aperta con nome “OS” in modalità lettura con permessi R/W

Dimensione SIZE

Mappata in memoria in modalità MAP_SHARED - cambiamenti visibili a chi condivide la memoria

PROT_READ permette la lettura

Rimuove l’oggetto shared mem

---

## Pagina 55

POSIX mmap

- La funzione `mmap`: mappa in process address space un file o un device
- Una volta mappato accessibile in modo diretto

`void * mmap (void *address, size_t length, int protect, int flags, int filedes, off_t offset)`

- **address**: indirizzo di partenza
- **length**: bytes richiesti
- **protect**: PROT_READ | PROT_WRITE | PROT_EXEC | PROT_NONE
- **flags**: MAP_SHARED, MAP_PRIVATE, MAP_ANON, MAP_FIXED
- **fildes**: descrittore di file
- **offset**: offset del file

---

## Pagina 56

Pipe

- Flusso di dati che permette a due processi di comunicare
- Uno dei primi meccanismi di comunicazione in UNIX
- Problematiche:
  - Comunicazione unidirezionale o bidirezionale?
  - Se two-way communication, è half o full-duplex?
  - Ci deve essere una relazione (i.e., parent-child) tra i processi comunicanti?
  - Si possono usare le pipes in una rete?

- Pipe ordinarie
  - Non può essere usata da processi che non hanno creato
  - Processo padre crea la pipe a la usa per comunicare con un processo figlio

- Named pipes
  - Possono essere usate senza una relazione parentale tra processi

---

## Pagina 57

Pipe Ordinarie

Pipe ordinarie comunicano in modalità produttore-consumatore
Produttore scrive su un’estremità (write-end della pipe)
Consumatore legge dall’altra estremità (read-end della pipe)
Le pipe ordinarie sono unidirezionali
Richiedono una relazione parentale tra i processi che comunicano

Windows le chiama anonymous pipes

---

## Pagina 58

Pipe Ordinarie

La funzione pipe in Unix

```c
#include <unistd.h>
int pipe ( int filedes[2] );
```

- l'argomento `filedes` è costituito da due descrittori di file:
  - `filedes[0]` è aperto in lettura e rappresenta il lato in lettura della pipe;
  - `filedes[1]` è aperto in scrittura e rappresenta il lato in scrittura della pipe;
  - l'output di `filedes[1]` è l'input per `filedes[0]`;

- restituisce 0 in caso di successo, -1 altrimenti.

---

## Pagina 59

Pipe Ordinarie

La funzione pipe in Unix

Generata da un singolo processo ha poca utilità ...

---

## Pagina 60

Pipe Ordinarie

La funzione pipe in Unix

• Tipicamente, un processo crea una pipe e poi chiama fork

---

## Pagina 61

Pipe Ordinarie

La funzione pipe in Unix

• Come utilizzare i pipe?
  • Cosa succede dopo la fork dipende dalla direzione dei dati
  • I canali non utilizzati vanno chiusi

• Esempio: parent → child
  • Il parent chiude l'estremo di read (close(fd[0]);)
  • Il child chiude l'estremo di write (close(fd[1]);)

parent
fd[0] fd[1]
child
fd[0] fd[1]
pipe
kernel

---

## Pagina 62

Pipe Ordinarie

La funzione pipe in Unix

```c
int fd[2];

if (pipe(fd) < 0)
    perror("pipe"), exit(1);
if ( (pid=fork()) < 0 )
    perror("fork"), exit(1);
else if (pid>0) { // padre
    close(fd[0]);
    write(fd[1], "ciao!", 5);
} else { // figlio
    close(fd[1]);
    n = read(fd[0], buf, sizeof(buf));
    write(STDOUT_FILENO, buf, n);
}
```

---

## Pagina 63

Pipe Ordinarie

La funzione pipe in Unix

```c
/* pipe1: invio di dati da un genitore ad un figlio */

#include <stdio.h>
#include <unistd.h>
#define MAXLINE 64

int main(void)
{
    int n, fd[2];
    pid_t pid;
    char line[MAXLINE];

    if (pipe(fd) < 0) perror("pipe"), exit(1);

    if ( (pid = fork()) < 0) perror("fork"), exit(1);

    else if (pid > 0) { /* genitore */
        close(fd[0]);
        write(fd[1], "hello world\n", 12);
    }
    else { /* figlio */
        close(fd[1]);
        n = read(fd[0], line, MAXLINE);
        write(STDOUT_FILENO, line, n);
    }
    exit(0);
}
```

---

## Pagina 64

Pipe Ordinarie

La funzione pipe in Unix

• All'inizio una pipe è vuota
• write aggiunge dati alla pipe
• read legge e rimuove dati dalla pipe
  – non si possono leggere piu' volte gli stessi dati da una pipe
  – non si puo' chiamare lseek su una pipe
  – i dati si ottengono in ordine First In First Out
• una pipe con una estremita' chiusa si dice rotta (broken)

---

## Pagina 65

Pipe Ordinarie

La funzione pipe in Unix

• Scrivere: write aggiunge i suoi dati alla pipe
  – se la pipe e' rotta, viene generato il segnale SIGPIPE e write restituisce un errore

• Leggere: read(fd[0], buf, 100)
  – meno di 100 bytes nella pipe: read legge l'intero contenuto della pipe
  – piu' di 100 bytes nella pipe: read legge i primi 100 bytes
  – pipe vuota: read si blocca in attesa di dati
  – pipe vuota e rotta: read restituisce 0

---

## Pagina 66

Pipe con Nome

- Named Pipes sono più potenti delle pipe ordinarie
- La comunicazione è bidirezionale
- Non è necessaria una relazione parentale tra processi comunicanti
- Molti processi possono usare le named pipe per comunicare
- Sia su UNIX che su Windows

---

## Pagina 67

Pipe con Nome in Unix

I file speciali FIFO (pipe con nome) consentono di superare alcune delle limitazione delle pipe. Essi difatti, rispetto a queste ultime, offrono i seguenti vantaggi:

• una volta creati, esistono nel file sistem fintanto che non vengono esplicitamente cancellati;
• possono essere usati da processi che non hanno un comune antenato.

I file FIFO possono essere creati in due modi:
• attraverso la shell, con il comando mkfifo;
• all'interno di un programma, con la chiamata alla funzione mkfifo.

Una volta creato un file FIFO, su di esso si possono effettuare le operazioni usuali di IO su file (open, read, write, close, ...)

---

## Pagina 68

Pipe con Nome in Unix

```c
#include <stdio.h>
#include <errno.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#define MAX_BUF_SIZE 1000

int main(int argc, char *argv[]){

int fd, ret_val, count, numread;
char buf[MAX_BUF_SIZE];

/* Create the named - pipe */
ret_val = mkfifo("miafifo", 0666);
if ((ret_val == -1) && (errno != EEXIST)) {
    perror("Error creating the named pipe");
    exit (1);
}

/* Open the pipe for reading */
fd = open("miafifo", O_RDONLY);

/* Read from the pipe */
numread = read(fd, buf, MAX_BUF_SIZE);
buf[numread] = '0';
printf("Server: Read From the pipe: %s\n", buf);
```

Codice Server

---

## Pagina 69

Pipe con Nome in Unix

```c
#include <stdio.h>
#include <errno.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

Codice Client

int main(int argc, char *argv[])
{
    int fd;

    /* Check if an argument was specified. */

    if (argc != 2) {
        printf("Usage : %s <string to be sent to the server>n", argv[0]);
        exit (1);
    }

    /* Open the pipe for writing */
    fd = open("miafifo", O_WRONLY);

    /* Write to the pipe */
    write(fd, argv[1], strlen(argv[1]));
```

Esempio esecuzione:

• $./servFifo &
• $./clientFifo prova
• Server : Read From the pipe : prova
• Server : Converted String : PROVA

---

## Pagina 70

Comunicazione in Sistemi Client-Server

- Per la comunicazione client-server vediamo due metodi
  - Sockets
  - Remote Procedure Call

---

## Pagina 71

Sistemi Client-Server

- Sistemi Client-Server
- Tipica archiettura di rete dove Sistemi Server rispondono alle richieste dei Sistemi client

---

## Pagina 72

Sistemi Distribuiti

- Sistemi distribuiti
  - Insiemi di calcolatori fisicamente separati con caratteristiche etereogenee connessi in una rete per consentire agli utenti l’accesso alle risorse distribuite
  - La rete fornisce un canale di comunicazione (es., tcp/ip)
  - Differenti tipi di reti
    - Local Area Network (LAN)
    - Wide Area Network (WAN)
    - Metropolitan Area Network (MAN)
    - Personal Area Network (PAN)

---

## Pagina 73

Socket

□ Una socket è un punto finale (endpoint) di comunicazione
□ Introdotti nel 1983 in Berkeley Software Distribution (BSD)
  □ Berkeley socket API
□ La comunicazione avviene tra coppie di socket
  □ Su stessa macchina (IPC locali) o diverse (IPC di rete)
□ Una socket internet è identificata da un indirizzo e una porta: 161.25.19.8:1625 indica la porta 1625 sull’host 161.25.19.8
□ La porta è un numero che differenzia diversi servizi su un host
□ Tutte le porte sotto 1024 sono usate per servizi standard
  □ Es. FTP 21, SSH 22, 25 smtp, 80 HTTP, etc. (vedi www.iana.org)
□ Un IP address speciale 127.0.0.1 (loopback) si riferisce al sistema in cui il processo gira

---

## Pagina 74

Comunicazione Socket

- Comunicazione Client-Server
  - Server in ascolto su una porta e Client richiede servizio
  - Processo Client stabilisce una comunicazione tramite una porta
    - Connessione unica per processo (altro Client altra porta)
  - Si possono definire diversi tipi di comunicazione
    - Connection oriented (TCP) o connectionless (UDP)

  ```
    host X
    (146.86.5.20)

    socket
    (146.86.5.20:1625)

    web server
    (161.25.19.8)

    socket
    (161.25.19.8:80)
  ```

---

## Pagina 75

Comunicazione Socket Unix

Comunicazione Client-Server Unix

Server in ascolto

```c
int fd1, fd2;
struct sockaddr_in mio_indirizzo;

mio_indirizzo.sin_family = AF_INET;
mio_indirizzo.sin_port = htons(5200);
mio_indirizzo.sin_addr.s_addr = htonl(INADDR_ANY);

fd1 = socket(PF_PF_INET, SOCK_STREAM, 0);
bind(fd1, (struct sockaddr *) &mio_indirizzo, sizeof(mio_indirizzo));

listen(fd1, 5);
fd2 = accept(fd1, NULL, NULL);
...
close(fd2);
close(fd1);
```

---

## Pagina 76

Comunicazione Socket Unix

Comunicazione Client-Server Unix
- Client connesso

```c
int fd;
struct sockaddr_in mio_indirizzo;

mio_indirizzo.sin_family = AF_INET;
mio_indirizzo.sin_port = htons(5200);
inet_aton("143.225.5.3", &indirizzo.sin_addr);

fd = socket(PF_INET, SOCK_STREAM, 0);
connect(fd, (struct sockaddr *) &mio_indirizzo,
sizeof(mio_indirizzo));
...
close(fd);
```

---

## Pagina 77

Comunicazione Socket Unix

- Comunicazione Client-Server Unix
- Schema di connessione

---

