---
date: 2026-04-16
corso: Sistemi Operativi
lezione: "1 — Thread e Race Condition: Mutex e Lock"
tags:
  - SO
  - thread
  - race-condition
  - mutex
  - lock
  - sincronizzazione
  - pthread
  - sezione-critica
  - SO1
---

# SO Lezione 1 — Thread e Race Condition: Mutex e Lock

**Corso:** Sistemi Operativi

---

## Argomenti trattati

- Concetto di thread e libreria pthread
- Race condition: definizione pratica e osservazione sperimentale
- Sezione critica e necessità di protezione
- Mutex: dichiarazione, inizializzazione, lock/unlock
- Compilazione con supporto multi-threaded (flag `-pthread`)
- Esercitazione pratica: riproduzione e risoluzione di race condition
- Analisi del comportamento non deterministico

---

## 1. Thread e libreria pthread

> [!info] Definizione di thread
> Un **thread** (filo di esecuzione) è l'unità di esecuzione sequenziale all'interno di un processo. A differenza dei processi separati, i thread dello stesso processo **condividono memoria**: heap, variabili globali, file descriptor.

**Caratteristiche:**
- Ogni thread ha il proprio **stack di esecuzione**
- **Condividono:** heap, dati globali, file, risorse del processo
- Su sistemi **multicore**, i thread eseguono **veramente in parallelo**
- Lo scheduler assegna il tempo di CPU ai thread

> [!info] Libreria pthread
> Per gestire thread in C/C++, si usa la libreria POSIX **pthread** (POSIX threads).
> ```c
> #include <pthread.h>
> ```

### Compilazione con supporto multi-threaded

```bash
gcc file.c -pthread -o eseguibile
```

Il flag `-pthread` **comunica al compilatore** che il codice è multi-threaded, collega le librerie necessarie, e abilita il supporto per i thread user-level.

---

## 2. Esempio pratico: race condition su contatore

### Codice di base (con race condition)

```c
#include <pthread.h>
#include <stdio.h>

int counter = 0;  // VARIABILE GLOBALE CONDIVISA

void* thread_function(void* arg) {
    for (int i = 0; i < 100000; i++) {
        counter = counter + 1;  // ← NON ATOMICO!
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;
    
    pthread_create(&t1, NULL, thread_function, NULL);
    pthread_create(&t2, NULL, thread_function, NULL);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    printf("Counter: %d\n", counter);
    // Atteso: 200.000 | Reale: ???
    
    return 0;
}
```

### Comportamento osservato

```bash
$ gcc race.c -pthread -o race && ./race
Counter: 156996
$ ./race
Counter: 187524
$ ./race
Counter: 200000
$ ./race
Counter: 142837
```

> [!warning] Risultati non deterministici
> Ogni esecuzione produce un valore **diverso**, generalmente **inferiore** a 200.000. Il risultato dipende dallo **scheduler indeterminato**.

### Perché accade?

L'operazione `counter = counter + 1` è composta da **tre istruzioni macchina**:

```
1. LOAD   r0, counter    // Carica il valore in un registro
2. ADD    r0, 1          // Incrementa il registro
3. STORE  r0, counter    // Scrive il nuovo valore in memoria
```

> [!example] Timeline di race condition
> ```
> Thread 1: LOAD counter (legge 0)      → r1 = 0
> Thread 2: LOAD counter (legge 0)      → r2 = 0
> Thread 1: ADD r1, 1                   → r1 = 1
> Thread 2: ADD r2, 1                   → r2 = 1
> Thread 1: STORE 1 → counter           counter = 1
> Thread 2: STORE 1 → counter           counter = 1 (SOVRASCRITTO!)
> ```

Entrambi leggono 0, incrementano a 1, uno sovrascrive l'altro. **Perdita di aggiornamento.**

> [!warning] Non è un problema di velocità
> Aumentare la velocità della CPU non risolve il problema. È un problema **logico di coordinamento** dovuto all'indeterminatezza dello scheduler e alla non-atomicità.

---

## 3. Sezione critica

> [!info] Sezione critica
> Una **sezione critica** è una porzione di codice dove uno o più thread accedono a **risorse condivise**. Solo **un thread alla volta** deve eseguire una sezione critica.

Nel nostro esempio:
```c
counter = counter + 1;  // ← SEZIONE CRITICA
```

### Soluzione: Mutex (Mutual Exclusion Lock)

> [!info] Mutex
> Un **mutex** è una variabile di sincronizzazione che garantisce **mutua esclusione**: solo un thread può "possedere" il mutex in un dato momento.

**Operazioni:**
- **`pthread_mutex_lock(&mutex)`**: acquisisce il mutex (attende se occupato)
- **`pthread_mutex_unlock(&mutex)`**: rilascia il mutex (sveglia un thread in attesa)

---

## 4. Implementazione con mutex

### Dichiarazione e inizializzazione

**Statica:**
```c
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
```

**Dinamica:**
```c
pthread_mutex_t mutex;
pthread_mutex_init(&mutex, NULL);
// ... uso ...
pthread_mutex_destroy(&mutex);
```

### Codice corretto

```c
#include <pthread.h>
#include <stdio.h>

int counter = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void* thread_function(void* arg) {
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&mutex);      // INIZIO SEZIONE CRITICA
        counter = counter + 1;
        pthread_mutex_unlock(&mutex);    // FINE SEZIONE CRITICA
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;
    
    pthread_create(&t1, NULL, thread_function, NULL);
    pthread_create(&t2, NULL, thread_function, NULL);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    printf("Counter: %d\n", counter);  // SEMPRE 200.000 ✓
    
    return 0;
}
```

### Comportamento garantito

```bash
$ ./race_fixed
Counter: 200000
$ ./race_fixed
Counter: 200000
$ ./race_fixed
Counter: 200000
```

**Il risultato è DETERMINISTICO** — sempre 200.000.

---

## 5. Semantica del mutex

### Acquisizione (lock)

```c
pthread_mutex_lock(&mutex);
```

- Se il mutex è **libero**: lo acquisisci subito e continui
- Se è **occupato**: **attendi** in una coda finché non si libera
- Una volta acquisito, nessun altro thread può acquisirlo fino al `unlock`

### Rilascio (unlock)

```c
pthread_mutex_unlock(&mutex);
```

- Libera il mutex (transizione da acquisito a libero)
- Se ci sono thread in attesa, uno di loro viene **svegliato** e può acquisire il mutex

### Pattern atomico

> [!tip] Protezione standard di sezione critica
> ```c
> pthread_mutex_lock(&mutex);
> // SEZIONE CRITICA: solo questo thread esegue qui
> // ...operazioni sulla risorsa condivisa...
> pthread_mutex_unlock(&mutex);
> ```

---

## 6. Esercitazione pratica

> [!question] Compito 1: Riprodurre la race condition
> 1. Copia il codice di base in `race_condition.c`
> 2. Compila: `gcc race_condition.c -pthread -o race_condition`
> 3. Esegui più volte: `./race_condition`
> 4. **Osserva** i risultati non deterministici

> [!question] Compito 2: Proteggere con mutex
> 1. Modifica il codice aggiungendo un mutex
> 2. Aggiungi `pthread_mutex_lock()` **prima** di `counter = counter + 1`
> 3. Aggiungi `pthread_mutex_unlock()` **dopo**
> 4. Compila e esegui
> 5. **Verifica** che il risultato sia sempre 200.000

---

## 7. Implementazione naive (SBAGLIATO!)

> [!warning] Tentativo naïve: spin lock senza atomicità
> ```c
> int my_lock = 0;
>
> void acquire_lock() {
>     while (my_lock == 1) {
>         // Busy waiting
>     }
>     my_lock = 1;  // ← NON ATOMICO! Ancora race condition!
> }
> ```

Il problema persiste: tra il test e l'assegnamento, un altro thread può acquisire il lock. **Non è una soluzione.**

### Soluzione hardware: primitiva atomica

Gli hardware moderni forniscono istruzioni **atomiche** come `test_and_set` o `compare_and_swap` (CAS):

```
test_and_set(address):
    temp ← memory[address]
    memory[address] ← 1
    return temp
```

Legge il vecchio valore e scrive 1 **in un'unica operazione indivisibile**.

Pthread usa internamente queste primitive, quindi `pthread_mutex_lock()` è implementata correttamente.

---

## 8. Prestazioni e contesa

> [!info] Overhead del mutex
> Ogni volta che acquisiamo un mutex, c'è un **costo**:
> - Se è libero: overhead minimale (poche istruzioni)
> - Se è occupato: il thread si blocca (context switch costoso)

> [!info] Contesa (contention)
> La **contesa** è il grado in cui più thread cercano simultaneamente di acquisire lo stesso mutex.
> - **Bassa contesa**: pochi thread in attesa → buone prestazioni
> - **Alta contesa**: molti thread in attesa → prestazioni scarse

### Miglioramento: accumulo locale

Nel nostro esempio con 2 thread che incrementano 100.000 volte, c'è **alta contesa**: ogni iterazione richiede lock/unlock.

> [!example] Soluzione ottimizzata
> ```c
> void* thread_function(void* arg) {
>     int local_counter = 0;
>     
>     // Incrementa LOCALMENTE (senza lock)
>     for (int i = 0; i < 100000; i++) {
>         local_counter++;
>     }
>     
>     // Aggiorna il contatore globale UNA SOLA VOLTA
>     pthread_mutex_lock(&mutex);
>     counter += local_counter;
>     pthread_mutex_unlock(&mutex);
>     
>     return NULL;
> }
> ```

**Un solo lock/unlock per thread** invece di 100.000. Prestazioni drasticamente migliori.

---

> [!abstract] Riepilogo: Punti Chiave
> 1. I thread **condividono memoria** — senza sincronizzazione, c'è **race condition**
> 2. Una race condition genera **risultati non deterministici** — dipendono dallo scheduler
> 3. La soluzione è proteggere le **sezioni critiche** con un **mutex**
> 4. **Mutex:** `lock()` acquisisce, `unlock()` rilascia; solo un thread alla volta
> 5. Pthread garantisce **atomicità** del mutex (usa primitive hardware come test-and-set)
> 6. **Contesa:** molti lock/unlock = context switch = prestazioni scarse. Minimizzare!

---

> [!todo] Letture consigliate
> - [ ] POSIX Threads Programming: https://computing.llnl.gov/tutorials/pthreads/
> - [ ] Intel Threading Building Blocks (TBB) documentation
> - [ ] Capitolo su sincronizzazione in un testo di Sistemi Operativi

---

#SO #thread #race-condition #mutex #lock #sincronizzazione #sezione-critica #pthread
