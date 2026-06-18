## Pagina 1

Lezione: Sincronizzazione

---

## Pagina 2

Obiettivi

- Presentare il concetto di sincronizzazione di processi
- Introdurre il problema della sezione critica
- Soluzioni software e hardware al problema della sezione critica
- Problemi classici di sincronizzazione
- Strumenti per risolvere il problema della sincronizzazione

---

## Pagina 3

Background

- Processi possono essere eseguiti concorrentemente
  - Interrotti in ogni momento con esecuzione incomplete

- Accessi concorrenti a dati condivisi possono portare ad inconsistenze

- La consistenza richiede meccanismi per assicurare l’esecuzione ordinata di processi cooperanti

---

## Pagina 4

Background

- Illustrazione del problema:
  - produttore consumatore con memoria limitata
  - Soluzione vista permetteva occupazione BUFFER_SIZE - 1

---

## Pagina 5

Bounded-Buffer – Produttore-Consumatore

- Buffer condiviso tra processi in memoria condivisa

```c
#define BUFFER_SIZE 10
typedef struct {
    .....
} item;

item buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
```

- Buffer circolare con indici in (prossima free) e out (prima posizione full)
- Soluzione corretta, ma limite su BUFFER_SIZE-1

- Buffer pieno
- Buffer vuoto
  - ((in + 1) % BUFFER_SIZE) == out
  - in == out

---

## Pagina 6

Bounded-Buffer – Produuttore

```cpp
item next_produced;
while (true) {
    /* produce an item in next produced */
    while (((in + 1) % BUFFER_SIZE) == out)
        ; /* do nothing */
    buffer[in] = next_produced;
    in = (in + 1) % BUFFER_SIZE;
}
```

---

## Pagina 7

Bounded Buffer – Consumatore

```cpp
item next_consumed;
while (true) {
    while (in == out)
    ; /* do nothing */
    next_consumed = buffer[out];
    out = (out + 1) % BUFFER_SIZE;

    /* consume the item in next consumed */
}
```

---

## Pagina 8

Produttore-Consumatore

Illustrazione del problema:

□ produttore consumatore con memoria limitata

□ Soluzione vista permetteva occupazione BUFFER_SIZE - 1

□ Si può introdurre un intero counter che conta i buffer pieni

□ Inizialmente counter = 0.

□ Poi incrementato dal produttore dopo che produce un elemento nel buffer e decrementato del consumatore dopo che consuma un elemento dal buffer

---

## Pagina 9

Produttore

```cpp
while (true) {
    /* produce an item in next produced */

    while (counter == BUFFER_SIZE) ;
    /* do nothing */

    buffer[in] = next_produced;
    in = (in + 1) % BUFFER_SIZE;
    counter++;
}
```

---

## Pagina 10

Consumatore

```c
while (true) {
    while (counter == 0)
        ; /* do nothing */
    next_consumed = buffer[out];
    out = (out + 1) % BUFFER_SIZE;
    counter--;
    /* consume the item in next consumed */
}
```

---

## Pagina 11

Corsa Critica

□ Operazioni non atomiche
□ Se i due processi eseguono counter++ e counter-- insieme
□ counter++ può essere implementato come
  `register1 = counter`
  `register1 = register1 + 1`
  `counter = register1`

□ counter-- può essere implementato come
  `register2 = counter`
  `register2 = register2 - 1`
  `counter = register2`

□ Interfogliate le due esecuzioni, inizialmente “count = 5”:
  S0: producer `register1 = counter` {register1 = 5}
  S1: producer `register1 = register1 + 1` {register1 = 6}
  S2: consumer `register2 = counter` {register2 = 5}
  S3: consumer `register2 = register2 - 1` {register2 = 4}
  S4: producer `counter = register1` {counter = 6}
  S5: consumer `counter = register2` {counter = 4}

---

## Pagina 12

Corsa Critica

- Il problema della corsa critica è pervasivo
- In particolare in sistemi multicore dove multithreading è molto enfatizzato
- Occcorrono meccanismi di sincronizzazione e coordinazione dei processi

---

## Pagina 13

Problema della Sezione Critica

- Considera un sistema di $n$ processi $\{p_0, p_1, \ldots, p_{n-1}\}$
- Ogni processo ha un segmento di sezione critica nel codice
  - Processi potrebbero cambiare variabili comuni, aggiornare tabelle condivise, scrivere file, etc.
  - Quando un processo entra in sezione critica gli altri processi non dovrebbero andare nella loro sezione critica

- Problema della sezione critica richiede un protocollo di interazione per risolverlo
  - Ogni processo deve chiedere il permesso per entrare nella sezione critica.
  - Il codice che implemente la richiesta è la entry section
  - Dopo la sezione ci sarà una exit section
  - Il codice rimanente che segue è la remainder section

---

## Pagina 14

Critical Section

Struttura generale di un processo con sezione critica $P_i$

```do {
  entry section
  critical section
  exit section
  remainder section
} while (true);
```

---

## Pagina 15

Problema della Sezione Critica

1. **Mutua Esclusione** - se il processo $P_i$ esegue la sua sezione critica nessun altro processo può eseguire la sua sezione critica

2. **Progresso** - Se nessun processo è in esecuzione nella sua sezione critica ed esistono alcuni processi che desiderano entrare nella loro sezione critica, solo i processi non in remainder section decideranno la selezione dei processi che entreranno successivamente nella sezione critica, che non può essere posticipata indefinitamente

3. **Bounded Waiting** - Deve esistere un limite al numero di volte in cui altri processi possono entrare nelle loro sezioni critiche dopo che un processo ha fatto una richiesta di entrare nella sua sezione critica prima che tale richiesta sia concessa
   - Assunto che ogni processo esegue a velocità nonzero
   - Senza assunzioni sulla velocità relativa degli $n$ processi

---

## Pagina 16

Corse Critiche nel Kernel

- I processi P0 e P1 creano processi figlio utilizzando fork()
- Corse critiche su tabella di file aperti nel sistema
- Corse critiche sulla variabile kernel che rappresenta il prossimo identificatore di processo disponibile (pid), next_available_pid
- Senza mutua esclusione, lo stesso pid potrebbe essere assegnato a due processi diversi

Diagram showing the fork process flow with P0 and P1 processes. P0 child = fork(); P1 child = fork(); request pid next_available_pid = 2615 return 2615 child = 2615

---

## Pagina 17

Corse Critiche nel Kernel

Problema di race conditions in kernel mode:

- Disabilitàzione degli interrupt in kernel mode
  - in single-core, ma per multicore non plausibile
- Altrimenti kernel preemptive o non-preemptive
- Preemptive – permette la prelazione del processo quando è in kernel mode. Più complesso da gestire con SMP ma più reattivo (standard nei kernel moderni: Linux, Win, XNU)
- Non-preemptive – esegue finché in kernel mode, si blocca, o volontariamente rilasciano la CPU
  - Non si consente l’interruzione forzata di processi attivi in modalità di sistema
  - WindowsXP/2000
  - Essenzialmente evitate le race condition in kernel mode

---

## Pagina 18

Soluzione di Peterson

- Buona descrizione algoritmica del problema
- Fornisce soluzione sezione critica per due processi concorrenti
- Si assume che **load e store** siano istruzioni atomiche in linguaggio macchina (non interrompibili)
- Due processi condividono due variabili:
  - `int turn;`
  - `Boolean flag[2]`

- La variable **turn** indica il processo di turno per entrare nella sezione critica
- Il **flag** array è usato per indicare se un processo è pronto per entrare in critical section.
  - `flag[i] = true` significa che il processo $P_i$ è pronto

---

## Pagina 19

Algoritmo per il Processo $P_i$

do {
  flag[i] = true;
  turn = j;
  while (flag[j] && turn == j);
  critical section
  flag[i] = false;
  remainder section
} while (true);

$P_0$: flag[0]=true
$P_1$: flag[1]=true
$P_1$: turn=0
$P_1$: while(flag[0] && turn=0);
$P_0$: turn=1
$P_0$: while(flag[1] && turn=1);

Soluzione — Mutua esclusione garantita dal valore di turn; $P_i$ entra nella sezione critica (progresso) al massimo dopo un ingresso da parte di $P_j$ (attesa limitata): alternanza stretta

---

## Pagina 20

Soluzione di Peterson

Si può provare che i requisiti sono soddisfatti:

1. Mutua esclusione
   $P_i$ entra in sezione critica solo se:
   $$flag[j] = false \text{ oppure } turn = i$$
2. Requisito di progresso è soddisfatto
3. Requisito bounded-waiting è soddisfatto

---

## Pagina 21

Soluzione di Peterson

Per n processi competizione su n-1 livelli

- level[i] : livello della competizione (0 non interessanto, fino ad n-1)
- victim[L]: chi cede al livello L

```cpp
// shared
int level[n] = {0};
int victim[n] = {0};

// processo Pi
do {
    for (int L = 1; L < n; L++) {
        level[i] = L;
        victim[L] = i;

        while (exists k != i such that level[k] >= L && victim[L] == i);
    }

    // critical section
    level[i] = 0;

    // remainder section

} while (true);
```

---

## Pagina 22

Soluzione di Peterson

Per n processi competizione su n-1 livelli
□ level[i] : livello della competizione (0 non interessanto, fino ad n-1)
□ victim[L]: chi cede al livello L

Esempio con P0, P1, P2, n = 3

1. P0 entra: level[0]=1, victim[1] = 0
2. P1 entra: level[1]=1, victim[1] = 1
3. P2 entra: level[2]=1, victim[1] = 2

P2 è victim e passano P0 e P1 al livello 2
Si aggiornano P0 e P1

1. level[0]=2, victim[2]=0
2. level[1]=2, victim[2]=1

Ora P1 aspetta e P0 entra in sezione critica

Uscito P0 level[0]=0, P1 entra in sezione critica

Uscito P1, level[1]=0, rimane solo P2

---

## Pagina 23

Soluzione di Peterson

□ In sistemi multithreaded ci sono problemi
□ Esempio, due thread condividono le variabili:

```c
boolean flag = false;
int x = 0;
```

□ Il primo thread esegue

```c
while (!flag)
    ;
print x;
```

1. Compilatore può riordinare le assegnazioni
2. CPU può eseguire out-of-order

□ Il secondo esegue

```c
x = 100;
flag = true;
```

□ Ci si aspetta che il primo thread stampi 100, ma non sono garantite le dipendenze tra le variabili x e flag,

□ Il thread 2 potrebbe aver cambiato l’ordine delle assegnazioni e il primo thread potrebbe stampare 0

---

## Pagina 24

Soluzione di Peterson

In sistemi multithreaded si potrebbe avere accesso concorrente alla sezione

```c
while(1) {
    turn = j;
    flag[i] = true;
    while (flag[j] && turn == j);
        sezione critica
        flag[i] = false;
        sezione non critica
}
```

Effetto dello scambio di istruzioni nella soluzione di Peterson

```c
process_0 → turn = 1 → flag[0] = true → cs
process_1 → turn = 0, flag[1] = true → cs
while (flag[0] && turn == 0)
    time
```

---

## Pagina 25

Hardware per Sincronizzazione

- Molti sistemi forniscono supporto hardware per implementare il codice della sezione critica
- Tutte le soluzioni che seguono si basano sul locking
  - Proteggere le sezioni critiche con i lock
- Uniprocessori – possono disabilitare gli interrupt
  - Il codice corrente eseguirebbe senza prelazione
  - Troppo inefficente su sistemi multiprocessori
    - SO che lo implementano non scalabile
- Macchine moderne forniscono hardware per gestire
  - Barriere di memoria
  - Istruzioni hardware
  - Variabili atomiche
- Usati direttamente o utilizzati per costrure meccanismi di sincronizzazione

---

## Pagina 26

Soluzioni basate su Locks

do {
    acquire lock
    critical section
    release lock
    remainder section
} while (TRUE);

---

## Pagina 27

Barriere di Memoria

- Un modello di memoria stabilisce quello che la memoria garantisce
- Modelli di due tipi:
  - Fortemente ordinate
    - modifica di un processore immediatamente visible per gli altri
  - Debolmente ordinate
    - modifica non vista da tutti gli altri
- Si possono forzare cambiamenti in memoria propagati ad altri processori (barriera di memoria o recinzione di memoria)
  - Meccanismi di basso livello utilizzati da sviluppatori del kernel
  - Esempio
    - Thread 1
      while (!flag)
        memory_barrier();
      print x;
    - Thread 2
      x = 100;
      memory_barrier();
      flag = true;

---

## Pagina 28

Barriere di Memoria

```c
#include <stdio.h>
#include <pthread.h>
#include <stdatomic.h>

int x = 0;
_Atomic int flag = 0;

void *thread_writer(void *arg) {
    x = 100;
    atomic_store_explicit(&flag, 1, memory_order_release);
    return NULL;
}

void *thread_reader(void *arg) {
    while (atomic_load_explicit(&flag, memory_order_acquire) == 0);

    printf("x = %d\n", x);
    return NULL;
}

int main(void) {
    pthread_t t1, t2;

    pthread_create(&t1, NULL, thread_reader, NULL);
    pthread_create(&t2, NULL, thread_writer, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    return 0;
}
```

---

## Pagina 29

Istruzioni atomiche

- Macchine moderne forniscono hardware per istruzioni atomiche
  - Atomiche = non-interrompibili
  - Eseguiibili sequenzialmente

- Consideriamo due tipi di istruzioni
  - Test memory (word) and set (value)
  - Swap contents of two memory words

---

## Pagina 30

test_and_set

Definizione:

```cpp
boolean test_and_set (boolean *target)
{
    boolean rv = *target;
    *target = TRUE;
    return rv;
}
```

1. Eseguite atomicamente
2. Restituisce il valore originale (parametro)
3. Setta il nuovo valore del parametro passato a “TRUE”.

---

## Pagina 31

Soluzione usando test_and_set()

□ Variabile condivisa boolean lock inizializzata a FALSE
□ Soluzione:

```c
do {
    while (test_and_set(&lock))
    ; /* do nothing */
    /* critical section */
    lock = false;
    /* remainder section */
} while (true);

Se lock = false, setta il lock a true ed esce dal while
Se lock = true, setta il lock a true ma non esce dal while

Per sbloccare un thread deve settare il lock = flase
```

---

## Pagina 32

compare_and_swap

Definizione:

```c
int compare _and_swap(int *value, int expected, int new_value) {
    int temp = *value;

    if (*value == expected)
        *value = new_value;
    return temp;
}
```

1. Eseguite atomicamente
2. Restituisce il valore originale del parametro in “value”
3. Settta la variabile “value” al valore di “new_value” ma solo se “value” ==“expected”. Cioè lo swap avviene solo con questa condizione.

Su architetture Intel x86 istruzione per CAS con lock del bus

```text
lock cmpxchg <destination operand>, <source operand>
```

Dest indica intero in memoria, source è un registro, in un registo EAX altro valore (src: new_val, dest: value, EAX: expected).
Se EAX == dest, allora dest = src, altrimenti EAX = dest

---

## Pagina 33

compare_and_swap

Definizione:

```c
int compare _and_swap(int *value, int expected, int new_value) {
    int temp = *value;

    if (*value == expected)
        *value = new_value;
    return temp;
}
```

1. Eseguite atomicamente
2. Restituisce il valore originale del parametro in “value”
3. Settà la variabile “value” al valore di “new_value” ma solo se “value” ==“expected”. Cioè lo swap avviene solo con questa condizione.

Su architetture Intel x86 istruzione per CAS con lock del bus

```text
lock cmpxchg <destination operand>, <source operand>
```

Esempio uso:
```text
mov eax, expected ;
mov ebx, new_val ;
lock cmxchg [mem], ebx ;
```

---

## Pagina 34

Soluzione con compare_and_swap

□ Intero condiviso “lock” initializzato a 0;
□ Soluzione:

```c
do {
    while (compare_and_swap(&lock, 0, 1) != 0)
    ; /* do nothing */
    /* critical section */
    lock = 0;
    /* remainder section */
} while (true);

Non soddisfa attesa limitata
(bounded-waiting)

Se lock = 0, restituisce 0 e setta 1, esce dal loop
Se lock = 1, restituisce 1 e rimane 1, rimane nel loop
```

---

## Pagina 35

Bounded-waiting Mutual Exclusion con CAS

```c
while (true) {
    waiting[i] = true;
    key = 1;
    while (waiting[i] && key == 1)
        key = compare_and_swap(&lock, 0, 1);
    waiting[i] = false;

    /* critical section */

    j = (i + 1) % n;
    while ((j != i) && !waiting[j])
        j = (j + 1) % n;

    if (j == i)
        lock = 0;
    else
        waiting[j] = false;

    /* remainder section */
}
```

waiting inizializzato a false
lock inizializzato a 0

Il primo trova lock = 0 e setta key a 0 e lock a 1

Salta chi non attende

Se non ci sono attese sblocca lock

Se ci sono attese sblocca un processo j lasciando il lock = 1

---

## Pagina 36

Bounded-waiting Mutual Exclusion con test_and_set

do {
  waiting[i] = true;
  key = true;
  while (waiting[i] && key)
    key = test_and_set(&lock);
  waiting[i] = false;
  /* critical section */
  j = (i + 1) % n;
  while ((j != i) && !waiting[j])
    j = (j + 1) % n;
  if (j == i)
    lock = false;
  else
    waiting[j] = false;
  /* remainder section */
} while (true);

---

## Pagina 37

Variabili atomiche

- CAS possono essere utilizzate per implementare altri costrutti
- Esempio incrementare una variabile
  ```csharp
  increment(&sequence);
  ```

- Implementata con CAS
  ```csharp
  void increment(atomic_int *v)
  {
    int temp;

    do {
      temp = *v;
    }
    while (temp != compare_and_swap(v, temp, temp+1));
  }
  ```

- Non risolvono il problema per casi più complessi

---

## Pagina 38

Variabili atomiche

- CAS possono essere utilizzate per implementare altri costrutti
- Esempio incrementare una variabile
  ```csharp
  increment(&sequence);
  ```

- Implementata con CAS
  ```csharp
  void increment(atomic_int *v)
  {
    int temp;

    do {
      temp = *v;
    }
    while (temp != compare_and_swap(v, temp, temp+1));
  }
  ```

- Non risolvono il problema per casi più complessi

---

## Pagina 39

Variabili atomiche

- CAS possono essere utilizzate per implementare altri costrutti
- Esempio incrementare una variabile lock-free

```csharp
increment(&sequence);
```

- Implementata con CAS

```csharp
void increment(atomic_int *v)
{
    int temp;

    do {
        temp = *v;
    }
    while (temp != compare_and_swap(v, temp, temp+1));
}
```

- Non risolvono il problema per casi più complessi

---

## Pagina 40

Mutex Locks

Le soluzioni precedenti sono complicate e generalmente inaccessibili ai programmatori di applicazioni
I progettisti di SO forniscono strumenti software per risolvere i problemi della sezione critica
Il più semplice è il mutex lock (mutual exclusion)
Protegge una sezione critica prendendo acquire() un lock e poi rilasciandolo release()
Variabile booleana indica se il lock è disponibile o no
Chiamate acquire() e release() atomiche
Solitamente implementate con istruzioni hardware atomiche
… ma richiede busy waiting
Il lock bloccante è chiamato spinlock perché il processo in attesa gira
Vantaggio: non fa context-switch, quindi per brevi attese è ok
Vantaggio: su multicore durante uno spin l’esecuzione continua
Uso conveniente se attesa minore di due context-switch

---

## Pagina 41

acquire() e release()

```c
acquire() {
    while (!available)
        ; /* busy wait */
    available = false;
}

release() {
    available = true;
}

do {
    acquire lock
    critical section
    release lock
    remainder section
} while (true);
```

Es. Implementazione di spinlock con CAS

```c
void lock(int *lock) {
    while (compare_and_swap(lock, 0, 1) != 0)
        // spin
}

void unlock(int *lock) {
    *lock = 0;
}
```

---

## Pagina 42

Semafori

- Strumenti di sincronizzazione più sofisticati (dei mutex locks) per sincronizzare processi.
- Semaforo S – variable intera
- Modificata con due operazioni indivisibili (atomiche)
  - wait() e signal()
    - Originariamente detti P() e V() da Dijkstra (Proberen: to test, Verhogen: to increment)
- Definizione di wait()
  ```c
  wait(S) {
    while (S <= 0)
      ; // busy wait
    S--;
  }
  ```

- Definizione di signal()
  ```c
  signal(S) {
    S++;
  }
  ```

Operazioni Atomiche:
- Nessun altro processo può modificare il valore mentre sono in esecuzione
- Nel caso di wait sia test che decremento senza interruzioni

---

## Pagina 43

Semafori Uso

□ Distinzione tra due tipi di semafori:
□ **Semaforo contatore** – valore intero varia su un domino non ristretto
□ **Semaforo binario** – valore intero varia tra 0 e 1
□ Come il **mutex lock**
□ Controllo accesso a numero di risorse pari al valore inizializzato
□ Può risolvere diversi problemi di sincronizzazione
□ Esempio – vincoli di scheduling
□ Considera $P_1$ e $P_2$ con $P_1$ che richiede $S_1$ prima di $S_2$
Crea un semaforo “synch” inizializzato a 0

**P1:**
$$S_1;$$
signal(synch);
Thread join
Synch = 0

**P2:**
wait(synch);
wait(S)
signal(S)
$S_2;$

□ Può implementare un semaforo contatore $S$ con un semaforo binario

---

## Pagina 44

Produttori Consumatori

```c
int n;
semaphore mutex = 1;
semaphore empty = n;
semaphore full = 0

while (true) {
    /* produce an item in next_produced */
    wait(empty);
    wait(mutex);
    /* add next_produced to the buffer */
    signal(mutex);
    signal(full);
}
```

Due semafori per vincoli di scheduling tra produttore e consumatore + un lock

```c
while (true) {
    wait(full);
    wait(mutex);
    /* remove an item from buffer to next_consumed */
    signal(mutex);
    signal(empty);
    /* consume the item in next_consumed */
}
```

---

## Pagina 45

Implementazione Semaforo

- Garantire che due processi non eseguano `wait()` e `signal()` sullo stesso semaforo nello stesso tempo
- Problema della sezione critica dove il codice di `wait()` e `signal` sono in sezione critica
- Definizioni precedenti con busy waiting
  ```c
  wait(S) {
    while (S <= 0)
      ; // busy wait
    S--;
  }
  ```

- Come evitare il busy waiting?

---

## Pagina 46

Implementazione senza Busy waiting

□ Il controllo in attesa si mette in waiting per essere svegliato da un signal (poi decide lo scheduler)

□ Per implementare ogni semaforo ha una coda di attesa
  □ Struttura dati semaforo:
    ► valore (di tipo intero)
    ► puntatore al prossimo record in lista

□ typedef struct{
  int value;
  struct process *list;
} semaphore;

□ Due operazioni:
  □ block – mette il processo che chiede l’operazione nell’appropriata coda di attesa
  □ wakeup – toglie uno dei processi in coda di attesa lo mette nella coda ready

---

## Pagina 47

Implementazione senza Busy waiting

```c
wait(semaphore *S) {
    S->value--;
    if (S->value < 0) {
        add this process to S->list;
        block();
    }
}                sleep e wakeup chiamate base di Sistema
                Lista di PCB

signal(semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        remove a process P from S->list;
        wakeup(P);
    }
}
```

---

## Pagina 48

Implementazione Semaforo

□ In questo caso il valore del semaforo diverge dalla definizione classica perché può essere negativo
  □ Invertito ordine di decremento e attesa (definizione classica inverso)
  □ Se negativo indica il numero di processi in attesa da risvegliare

□ La lista dei processi in attesa si può ottenere con puntatori ai Process Contol Block (PCB)

□ Rimane il problema della sezione critica per il codice di wait e signal
  □ Per singoli processori si può inibire l’interrupt
  □ Per multicore molto inefficiente, meglio usare compare_and_swap o spinlocks
  □ … ma non eliminato il busy waiting spostato (codice wait e signal)
    ► Dove il codice è breve quindi poco busy waiting se la sezione critica è raramente occupata
    ► Le applicazioni potrebbero spendere molto tempo in sezioni critiche

---

## Pagina 49

Implementazione Semaforo

□ In questo caso il valore del semaforo diverge dalla definizione classica perché può essere negativo
  □ Invertito ordine di decremento e attesa (definizione classica inverso)
  □ Se negativo indica il numero di processi in attesa da risvegliare

□ La lista dei processi in attesa si può ottenere con puntatori ai Process Contol Block (PCB)

□ Rimane il problema della sezione critica per il codice di wait e signal
  □ Per singoli processori si può inibire l’interrupt
  □ Per multicore molto inefficiente, meglio usare compare_and_swap o spinlocks
  □ … ma non eliminato il busy waiting spostato (codice wait e signal)
    ► Dove il codice è breve quindi poco busy waiting se la sezione critica è raramente occupata
    ► Le applicazioni potrebbero spendere molto tempo in sezioni critiche

---

## Pagina 50

Deadlock e Starvation

- Deadlock – due o più processi sono in attesa per un evento che può essere causato solo da uno dei processi in attesa
- Siano $S$ e $Q$ due semafori initializati ad 1

$$P_0$$
wait(S);
wait(Q);
...
signal(S);
signal(Q);

$$P_1$$
wait(Q);
wait(S);
...
signal(Q);
signal(S);

- Starvation – blocco indefinito
  - Un processo potrebbe non essere più rimosso dalla coda del semaforo su cui è sospeso
- Priority Inversion
  - problema di scheduling quando un processo a bassa priorità tiene un lock necessario ad un processo a più alta priorità
  - Risolto con un protocollo di priority-inheritance

---

## Pagina 51

Problemi con i Semafori

□ Uso scorretto delle operazioni dei semafori da parte dei programmatori:

□ Inversione di signal e wait
  ▶ signal (mutex) … wait (mutex)
  ▶ Violazione della mutua esclusione

□ Scambio di signal con wait
  ▶ wait (mutex) … wait (mutex)
  ▶ Blocco permanente

□ Omissione di wait (mutex) o signal (mutex) (o entrambi)

□ Sono quindi possibili deadlock e starvation
□ Si introducono costrutti di sincronizzazione di alto livello per affronatare questi problemi

---

## Pagina 52

Problemi con i Semafori

- Semantica dei semafori non intuitiva
- Costrutti complessi molto dipendenti dal contest e dalle inizializzazione
- Facilmente portano ad errori

---

## Pagina 53

Monitor

- Astrazione di alto livello che fornisce un meccanismo di sincronizzazione (introdotti nel 1974 da Hoare)
- *Tipo di dato astratto*, variabili condivise accessibili con procedure predefinite
- Solo un processo alla volta può essere attivo nel monitor
- Dati privati
- … ma non potente abbastanza da modellare alcuni schemi di sincronizzazione
  - Introdotte le variabili di condizione

```cpp
monitor monitor-name
{
  // shared variable declarations
  procedure P1 (...) { ... }

  procedure Pn (...) { ... }

  Initialization code (...) { ... }
}
```

---

## Pagina 54

Rappresentazione di un Monitor

Schema di un Monitor:
- Coda di accesso
- Dati condivisi
- Operazioni
- Codice di inizializzazione

---

## Pagina 55

Variabili di Condizione

- **condition x, y;**
- Due operazioni sono permesse su una variabile di condizione:
  - `x.wait()` – il processo è sospeso finché non avviene x.signal()
  - `x.signal()` – riprende uno dei processi (se c’è) che ha invocato x.wait()
  - Se non c’è `x.wait()` sulla variabile, non c’è alcun effetto

---

## Pagina 56

Monitor con Variabili di Condizione

shared data

queues associated with x, y conditions

entry queue

operations

initialization code

---

## Pagina 57

Scelte su Condition Variables

Se il processo P invoca x.signal() e il processo Q è sospeso in x.wait() che succede?

- Q e P non possono eseguire in parallelo nel monitor.
  - Se Q viene ripreso, P deve attendere

Tra le opzioni abbiamo:

- **Signal and wait** – P aspetta finché Q o lascia il monitor o aspetta un’altra condizione

- **Signal and continue** – Q aspetta finché P lascia il monitor o aspetta un’altra condizione

- Entrambe hanno pros e cons – implementatore del linguaggio decide
  - La seconda lascia al processo in esecuzione, ma la variabile attesa potrebbe cambiare

---

## Pagina 58

Monitor Implementati con Semafori

□ Variabili

```c
semaphore mutex; // (initially = 1)
semaphore next; // (initially = 0)
int next_count = 0;
```

next usato dal processo segnalante per sospendersi

□ Ogni procedura $F$ sostituita da Signal and Wait

```c
wait(mutex);
...
body of F;
...
if (next_count > 0)
    signal(next)
else
    signal(mutex);
```

Accesso esclusivo

Se altri in attesa lascia, altrimenti sblocca

□ La mutua esclusione nel monitor è assicurata
□ Implementazione con signal-and-wait

---

## Pagina 59

Monitor Implementation – Condition Variables

□ Per ogni condition var $x$, abbiamo:

```c
semaphore x_sem; // (initially = 0)
int x_count = 0;
```

□ La $x.wait$ implementata come:

```c
x_count++;
if (next_count > 0)
    signal(next);
else
    signal(mutex);
wait(x_sem);
x_count--;
```

Se prossimo in attesa passa a lui, altrimenti rilascia il mutex

Aspetta su $x$
Esci abbassando il cont

---

## Pagina 60

Monitor Implementation

La x.signal implementata come:

```c
if (x_count > 0) {
    next_count++;
    signal(x_sem);
    wait(next);
    next_count--;
}
```

Se prossimo in attesa, lascia a lui e rimettiti in coda di attesa per il monitor

sblocca la var x

Attendi su next
Quando entri aggiorna next

---

## Pagina 61

Ripresa dei Processi nel Monitor

- Se molti processi accodati sulla condizione x e avviene un x.signal() quali riprendere?
- FCFS spesso non adeguato
- conditional-wait come x.wait(c)
  - Dove c’è il priority number
  - Processo con numero più basso (highest priority) è il prossimo schedulato (es., tempo di esecuzione più basso)

---

## Pagina 62

Single Resource allocation

- Allocata una singola risorsa tra processi in competizione usando i numeri di prorità che specificano il tempo massimo di utilizzo della risorsa

  R.acquire(t);

  ...

  access the resurce;

  ...

  R.release;

- Con R instanza di tipo ResourceAllocator

---

## Pagina 63

Monitor per Singola Risorsa

```cpp
monitor ResourceAllocator
{
    boolean busy;
    condition x;
    void acquire(int time) {
        if (busy)
            x.wait(time);
        busy = TRUE;
    }
    void release() {
        busy = FALSE;
        x.signal();
    }
    initialization code() {
        busy = FALSE;
    }
}
```

---

## Pagina 64

Single Resource allocation

- Allocata una singola risorsa tra processi in competizione usando i numeri di prorità che specificano il tempo massimo di utilizzo della risorsa

```python
R.acquire(t);
...
access the resurce;
...
R.release;
```

- Con R instanza di tipo ResourceAllocator
- Però il monitor non garantisce la corretta esecuzione
  - Accesso a risorse senza avere i permessi, doppia richiesta, rilascio di risorse senza utilizzo, non rilascio
  - Controllo di accesso definite nel monitor
  - Ma va controllato che tutti usino correttamente l’allocatore

---

## Pagina 65

Liveness

- Un processo che prova ad entrare in sezione critica potrebbe attendere indefinitivamente
- Violato Progresso e Attesa Limitata

Liveness:
- insieme di proprietà che un sistema deve soddisfare per garantire che i processi facciano progressi durante il ciclo di vita della loro esecuzione.
- Un processo che attende indefinitamente è un esempio di “mancanza di liveness” (liveness failure).

Esempi di situazioni che possono portare a liveness failure:
- Ciclo infinito
- Attesa indefinita
- Deadlock
- Inversione di priorità

---

## Pagina 66

Inversione di Priorità

- Processo ad alta priorità che deve accedere a risorse del kernel tenute da un processo a priorità più bassa
- Più complicato se il processo è prelazionato da un altro ancora

- Tre processo L < M < H
  - H chiede il semaforo S tenuto da L
  - H deve aspettare che L liberi il semaforo
  - … M diventa runnable e prelaziona L
  - Il processo M influenza l’attesa di un processo H (a più alta priorità) sul semaforo S tenuta da L

- Priority-inheritance protocol
  - Quando processi accedono ad una risorsa richiesta da un processo ad alta priorità, ereditano la priorità del processo. Poi tornano ai valori originali
  - L avrebbe ereditato la priorità di H bloccando M (rientra con priorità L al rilascio), la competizione tra H ed M è così vinta da H

---

## Pagina 67

Inversione di Priorità

- Processo ad alta priorità che deve accedere a risorse del kernel tenute da un processo a priorità più bassa
- Più complicato se il processo è prelazionato da un altro ancora
- Priority-inheritance protocol

Priority Inheritance

- Task H is blocked trying to take lock
- Task L assumes Task H’s priority
- Task H can now freely preempt Task M
- Task L takes lock
- Task L releases lock

---

## Pagina 68

Inversione di Priorità

- L’inversion di priorità può avere effetti a catena causando un fallimento sistemico
- Il caso della missione Mars Pathfinder
  - Prima missione ad aver trasportato un rover, Sojourner, sul pianeta.
  - Lancio: 4 dicembre 1996
  - Arrivo: 4 luglio 1997 (7 mesi dopo), operatività 92 sol (95 giorni)
  - Lander operava come stazione meteorologica
  - Rover usato per analizzare il suolo e le roccce del sito di atterraggio ed effettuare esperimenti sulla superficie (100 metri di esplorazione)
  - https://space.skyrocket.de/doc_sdat/mars_pathfinder.htm

---

## Pagina 69

Inversione di Priorità

- L’inversion di priorità può avere effetti a catena causando un fallimento sistemico
- Il caso del Mars Pathfinder
  - Dopo i primi test il software di Pathfinder fa continui “reset”
  - Inizializzato hw, sw, comunicazione

- La raccolta dati dal bus era affidata a due task:
  - Il gestore delle transizioni del bus (bc_sched)
  - Il responsabile di acquisizione dati (bc_dist)
- Una sequenza di operazioni corrette richiedeva che i due task si alternassero in esecuzione, durante ogni ciclo di 8Hz
  - Quando un task iniziava, per prima cosa controllava che l’altro task avesse finito; altrimenti, generava un reset del sistema.

---

## Pagina 70

Inversione di Priorità

- L’inversion di priorità può avere effetti a catena causando un fallimento sistemico
- Il caso del Mars Pathfinder
  - Dopo i primi test il software di Pathfinder fa continui “reset”
  - Inizializzato hw, sw, comunicazione

- La raccolta dati dal bus era affidata a due task:
  - Il gestore delle transizioni del bus (bc_sched)
  - Il responsabile di acquisizione dati (bc_dist)
- Una sequenza di operazioni corrette richiedeva che i due task si alternassero in esecuzione, durante ogni ciclo di 8Hz
  - Quando un task iniziava, per prima cosa controllava che l’altro task avesse finito; altrimenti, generava un reset del sistema.

- Attivazione bus
- bc_dist: distribuisce i dati e passa il controllo a bc_sched
- bc_sched: bus scheduler prepara lo schedulere per il prossimo ciclo basandosi su priorità e dati preparati da bc_dist (meteo comunica direttamente a bc_sched)

---

## Pagina 71

Inversione di Priorità

- L’inversion di priorità può avere effetti a catena causando un fallimento sistemico
- Il caso del Mars Pathfinder
  - Dopo i primi test il software di Sojourner fa continui “reset”
  - Inizializzato hw, sw, comunicazione

Priorità:
1 bc_sched, 3 bc_dist, 4 operazioni stazione, 5 esperimenti scientifici

Il problema riguardava tre task:
- bc_dist (priorita` 3),
- Un qualsiasi task relativo alle operazioni della stazione spaziale (priorita` 4), e
- Il task della stazione meteo (priorita` 5)

Il task della stazione meteo riceveva i dati da bc_sched, per fare questo, doveva prendere in uso esclusivo (lock) una risorsa, cioe` il bus.

- La sua esecuzione veniva sospesa dal task con priorita` 4, prima che rilasciasse il lock,
- Successivamente, bc_dist non riusciva ad acquisire quella risorsa, e forzava il reset.

---

## Pagina 72

Inversione di Priorità

Il caso del Mars Pathfinder
- Dopo i primi test il software di Sojourner fa continui “reset”
- Inizializzato hw, sw, comunicazione

Stazione meteo riceve dati da bc_sched, blocca il bus
Low task prelaziona

https://www.slideshare.net/gabrielladodero/quando-i-computer-non-funzionano-su-marte

---

## Pagina 73

Inversione di Priorità

Il caso del Mars Pathfinder
- Dopo i primi test il software di Pathfinder fa continui “reset”
- Inizializzato hw, sw, comunicazione

- SO su Pathfinder era VxWorks (real-time)
- Variabile globale per priority inheritance su tutti i semafori
- La variabile settata su Pathfinder e il problema è stato risolto

https://www.slideshare.net/gabrielladodero/quando-i-computer-non-funzionano-su-marte

---

## Pagina 74

Livelli di Contesa

- Strumenti per il problema della sezione critica e per sincronizzare l’attività dei processi possono essere valutati a seconda del livello di contesa.
- Alcuni strumenti funzionano meglio con un certo livello di contesa
- Strumenti basati su istruzioni CAS per avere lock-free
  - Approccio ottimistico (prima test poi verifica collisioni)
  - Pessimistico (prima lock poi test)

```c
typedef struct node {
  value_t data;
  struct node *next;
} Node;

Node *top; // top of stack

void push(value_t item) {
  Node *old_node;
  Node *new_node;

  new_node = malloc(sizeof(Node));
  new_node->data = item;

  do {
    old_node = top;
    new_node->next = old_node;
  }
  while (compare_and_swap(top, old_node, new_node) != old_node);
}
```

Treiber 86

---

## Pagina 75

Livelli di Contesa

- Strumenti per il problema della sezione critica e per sincronizzare l’attività dei processi possono essere valutati a seconda del livello di contesa.
- Alcuni strumenti funzionano meglio con un certo livello di contesa
- Strumenti basati su istruzioni CAS per avere lock-free
  - Approccio ottimistico (prima test poi verifica collisioni)
  - Pessimistico (prima lock poi test)

```c
typedef struct node {
  value_t data;
  struct node *next;
} Node;

Node *top; // top of stack

Treiber 86

value_t pop() {
  Node *old_node;
  Node *new_node;

  do {
    old_node = top;
    if (old_node == NULL)
      return NULL;
    new_node = old_node->next;
  }
  while (compare_and_swap(top, old_node, new_node) != old_node);

  return old_node->data;
}
```

---

## Pagina 76

Livelli di Contesa

- Strumenti per il problema della sezione critica e per sincronizzare l’attività dei processi possono essere valutati a seconda del livello di contesa.
- Alcuni strumenti funzionano meglio con un certo livello di contesa
- Strumenti basati su istruzioni CAS per avere lock-free
  - Approccio ottimistico (prima testi poi verifici collisioni)
  - Pessimistico (prima lock poi test)

- Linee guida per distinguere le prestazioni della sincronizzazione al variare del livello di contesa:
  - Nessuna contesa. Sebbene entrambe le opzioni siano generalmente veloci, la protezione ottimistica sarà leggermente più veloce della sincronizzazione tradizionale.
  - Contesa moderata. La protezione ottimistica sarà più veloce e in alcuni casi molto più veloce rispetto alla sincronizzazione tradizionale.
  - Alta contesa. Con carichi molto elevati, la sincronizzazione tradizionale sarà in definitiva più veloce della sincronizzazione ottimistica.

---

## Pagina 77

Valutazione

La scelta del meccanismo di sincronizzazione influenza le performance.

- Interi atomici più leggeri dei lock e appropriati per update singoli di variabili (es. contatori)
- SpinLock appropriati per multiprocessori se il lock è di breve durata
- Mutex lock solitamente più leggeri dei semafori contatori e binari
- Per il controllo di accesso a risorse multiple più appropriati i semafori contatori
- Solitamente strutture di più alto livello come i monitor hanno maggiore overhead

---

