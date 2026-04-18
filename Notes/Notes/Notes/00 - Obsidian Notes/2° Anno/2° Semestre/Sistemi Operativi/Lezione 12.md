---
date: 2026-04-15
corso: Sistemi Operativi
lezione: 2 — Variabili di condizione, Monitor e Deadlock
tags:
  - SO
  - condition-variables
  - monitor
  - 5-filosofi
  - deadlock
  - sincronizzazione
  - signal
  - broadcast
  - SO1
---

# SO Lezione 2 — Variabili di Condizione, Monitor e Deadlock

**Corso:** Sistemi Operativi

---

## Argomenti trattati

- Variabili di condizione: definizione e operazioni (wait, signal, broadcast)
- Accoppiamento mutex + condition variable
- Pattern del monitor per sincronizzazione avanzata
- Problema dei 5 filosofi: formulazione e soluzione con condition variable
- Differenza tra `signal()` e `broadcast()`
- Deadlock: definizione e cause
- Esempi di deadlock: inversione di mutex, cicli di attesa

---

## 1. Variabili di condizione (Condition Variable)

> [!info] Definizione: Condition Variable
> Una **variabile di condizione** è una primitiva di sincronizzazione che consente ai thread di **aspettare il verificarsi di una condizione** e essere svegliati quando la condizione diventa vera.

A differenza di un mutex (mutua esclusione), una condition variable fornisce **comunicazione tra thread**.

### Operazioni principali

| Operazione | Descrizione |
|---|---|
| `pthread_cond_wait(&cond, &mutex)` | Thread si addormenta; rilascia temporaneamente il mutex |
| `pthread_cond_signal(&cond)` | Sveglia **uno** dei thread in attesa (arbitrariamente) |
| `pthread_cond_broadcast(&cond)` | Sveglia **tutti** i thread in attesa |

### Invariante fondamentale

> [!warning] Una condition variable deve essere associata a un mutex
> ```c
> pthread_mutex_lock(&mutex);
> while (!condition) {
>     pthread_cond_wait(&cond, &mutex);
> }
> // Ora la condizione è vera e il mutex è acquisito
> // ... sezione critica ...
> pthread_mutex_unlock(&mutex);
> ```

**Nota:** si usa un **while loop**, non un if, perché il thread potrebbe svegliarsi spuriamente.

---

## 2. Dichiarazione e inizializzazione

**Statica:**
```c
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
```

**Dinamica:**
```c
pthread_cond_t cond;
pthread_cond_init(&cond, NULL);
// ... uso ...
pthread_cond_destroy(&cond);
```

---

## 3. Pattern del monitor

> [!info] Monitor: struttura di sincronizzazione completa
> Un **monitor** combina:
> - Un **mutex** (mutua esclusione)
> - Una o più **condition variable** (comunicazione)
> - **Dati condivisi** (protetti dal mutex)

> [!example] Implementazione di un monitor
> ```c
> typedef struct {
>     pthread_mutex_t mutex;
>     pthread_cond_t cond;
>     int data;  // Risorsa condivisa
> } Monitor;
>
> void monitor_operation(Monitor* m) {
>     pthread_mutex_lock(&m->mutex);
>     
>     // Aspettare finché la condizione non è vera
>     while (m->data < 10) {
>         pthread_cond_wait(&m->cond, &m->mutex);
>     }
>     
>     // Sezione critica
>     m->data = 0;
>     
>     // Svegliare eventuali thread
>     pthread_cond_signal(&m->cond);
>     
>     pthread_mutex_unlock(&m->mutex);
> }
> ```

---

## 4. Problema dei 5 filosofi (Dining Philosophers)

> [!info] Formulazione classica
> **5 filosofi** seduti attorno a un tavolo:
> - Alternano tra **pensare** e **mangiare**
> - Per mangiare, hanno bisogno di **2 bacchette**: una a destra, una a sinistra
> - Ci sono **5 bacchette**, una tra ogni coppia di filosofi
> - La bacchetta è **condivisa** tra due filosofi
> 
> **Obiettivo:** trovare un protocollo **senza deadlock** e **senza starvation**.

### Approccio naïve (SBAGLIATO)

> [!warning] Questo approccio causa deadlock
> ```c
> while (1) {
>     think();
>     take_fork(i);              // Prende bacchetta sinistra
>     take_fork((i+1) % 5);      // Prende bacchetta destra
>     eat();
>     put_fork(i);
>     put_fork((i+1) % 5);
> }
> ```

> [!example] Timeline di deadlock
> ```
> Filosofo 0: prende fork 0 ✓
> Filosofo 1: prende fork 1 ✓
> Filosofo 2: prende fork 2 ✓
> Filosofo 3: prende fork 3 ✓
> Filosofo 4: prende fork 4 ✓
> 
> Filosofo 0: aspetta fork 1 (Filosofo 1 ce l'ha)
> Filosofo 1: aspetta fork 2 (Filosofo 2 ce l'ha)
> ... DEADLOCK! Ciclo circolare.
> ```

### Soluzione con condition variable

**Idea:**
- Ogni filosofo ha uno **stato**: THINKING, HUNGRY, EATING
- Ogni filosofo ha una **condition variable** su cui aspettare
- Un filosofo mangia solo se **entrambi i vicini NON stanno mangiando**

> [!example] Implementazione corretta
> ```c
> typedef enum { THINKING, HUNGRY, EATING } State;
>
> State state[5];
> pthread_cond_t cond[5];
> pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
>
> void test(int i) {
>     // Se ho fame E i vicini non mangiano → mangio
>     if (state[i] == HUNGRY && 
>         state[(i-1) % 5] != EATING && 
>         state[(i+1) % 5] != EATING) {
>         state[i] = EATING;
>         pthread_cond_signal(&cond[i]);
>     }
> }
>
> void take_forks(int i) {
>     pthread_mutex_lock(&mutex);
>     
>     state[i] = HUNGRY;
>     test(i);  // Verifico se posso mangiare
>     
>     // Se non posso, aspetto
>     while (state[i] != EATING) {
>         pthread_cond_wait(&cond[i], &mutex);
>     }
>     
>     pthread_mutex_unlock(&mutex);
> }
>
> void put_forks(int i) {
>     pthread_mutex_lock(&mutex);
>     
>     state[i] = THINKING;
>     
>     // Sveglio i vicini se sono affamati
>     test((i-1) % 5);
>     test((i+1) % 5);
>     
>     pthread_mutex_unlock(&mutex);
> }
> ```

### Proprietà garantite

> [!info] Correttezza della soluzione
> 1. **Mutua esclusione:** al massimo uno mangia per volta (protetto da mutex)
> 2. **Deadlock-free:** nessun ciclo di attese
> 3. **Starvation-free:** ogni filosofo affamato finisce per mangiare

---

## 5. Signal vs Broadcast

### `signal()`: sveglia un thread

> [!info] Signal sveglia uno
> ```c
> pthread_cond_signal(&cond);  // Sveglia UNO dei thread in attesa
> ```

**Uso:** quando sappiamo che esattamente **un thread** è in attesa, o quando non importa quale si svegli.

**Nel problema dei 5 filosofi:** ogni filosofo ha la **sua condition variable** `cond[i]`. Quando il filosofo $i$ finisce di mangiare, chiama `test(i-1)` e `test(i+1)`, che chiamano `signal(&cond[vicino])`, svegliando il filosofo specifico.

### `broadcast()`: sveglia tutti

> [!info] Broadcast sveglia tutti
> ```c
> pthread_cond_broadcast(&cond);  // Sveglia TUTTI i thread in attesa
> ```

**Uso:** quando la condizione riguarda **più thread** e non sappiamo quanti.

### Differenza nel contesto dei 5 filosofi

Se usassimo **una sola** condition variable per tutti:

```c
pthread_cond_t cond;  // Una per tutti

void put_forks(int i) {
    // ...
    pthread_cond_broadcast(&cond);  // Sveglia TUTTI
}
```

Con `broadcast`, tutti i filosofi si svegliano e verificano se possono mangiare. È inefficiente (false awakenings), ma corretto.

Con `signal()` e una sola variable, potremmo svegliare il filosofo sbagliato.

> [!tip] Regola pratica
> Con la soluzione originale (una variable per filosofo), `signal` e `broadcast` sono **equivalenti**. Con una sola variable, meglio usare `broadcast`.

---

## 6. Deadlock: definizione e cause

> [!info] Definizione: Deadlock (stallo)
> Una situazione in cui **due o più thread si aspettano mutuamente** in modo circolare, e **nessuno può procedere**. Il sistema è bloccato **permanentemente**.

### Condizioni necessarie (Coffman, 1971)

Tutte e quattro devono essere vere:

1. **Mutua esclusione:** la risorsa non può essere condivisa (mutex)
2. **Hold and wait:** un thread tiene una risorsa e aspetta un'altra
3. **Non-preemption:** non si può strappare una risorsa a un thread
4. **Circular wait:** c'è un ciclo di attese

> [!tip] Prevenzione: eliminare una sola condizione
> Basta eliminare **UNA** di queste quattro per prevenire il deadlock.

---

## 7. Esempio 1: Inversione di mutex

> [!example] Due mutex in ordine invertito
> ```c
> pthread_mutex_t mutex1, mutex2;
>
> void* thread1(void* arg) {
>     pthread_mutex_lock(&mutex1);
>     sleep(1);
>     pthread_mutex_lock(&mutex2);  // Aspetta mutex2
>     // ...
>     pthread_mutex_unlock(&mutex2);
>     pthread_mutex_unlock(&mutex1);
> }
>
> void* thread2(void* arg) {
>     pthread_mutex_lock(&mutex2);  // Prende PRIMA mutex2
>     sleep(1);
>     pthread_mutex_lock(&mutex1);  // Aspetta mutex1 (Thread1 ce l'ha!)
>     // ...
>     pthread_mutex_unlock(&mutex1);
>     pthread_mutex_unlock(&mutex2);
> }
> ```

> [!warning] Timeline di deadlock
> ```
> Thread 1: lock(mutex1) ✓
> Thread 2: lock(mutex2) ✓
> Thread 1: lock(mutex2) → ATTESA (Thread 2 ce l'ha)
> Thread 2: lock(mutex1) → ATTESA (Thread 1 ce l'ha)
> DEADLOCK! ↔ Attesa circolare.
> ```

---

## 8. Esempio 2: Ciclo di attese (3+ thread)

> [!example] Ciclo di tre thread
> ```c
> void* thread1(void* arg) {
>     pthread_mutex_lock(&mutex1);
>     pthread_mutex_lock(&mutex2);
> }
>
> void* thread2(void* arg) {
>     pthread_mutex_lock(&mutex2);
>     pthread_mutex_lock(&mutex3);
> }
>
> void* thread3(void* arg) {
>     pthread_mutex_lock(&mutex3);
>     pthread_mutex_lock(&mutex1);  // Aspetta mutex1
> }
> ```

> [!warning] Ciclo di attesa
> ```
> Thread 1 aspetta mutex2 ← Thread 2 aspetta mutex3 ← Thread 3 aspetta mutex1 ← Thread 1
> DEADLOCK! Ciclo di tre.
> ```

---

## 9. Prevenzione del deadlock

### Strategia 1: Ordinamento totale dei mutex

Acquisire **sempre** i mutex nello **stesso ordine**:

> [!tip] Soluzione semplice e pratica
> ```c
> void* thread1(void* arg) {
>     pthread_mutex_lock(&mutex1);
>     pthread_mutex_lock(&mutex2);
>     // ...
> }
>
> void* thread2(void* arg) {
>     pthread_mutex_lock(&mutex1);  // Stesso ordine!
>     pthread_mutex_lock(&mutex2);
>     // ...
> }
> ```

Questo **elimina l'inversione** e il ciclo.

### Strategia 2: Acquisizione atomica

Prendi **tutte** le risorse necessarie in una sola operazione atomica, invece di una per volta.

Nel problema dei 5 filosofi: prendere **entrambe le bacchette** senza interleaving (già implementato nella soluzione).

### Strategia 3: Timeout

Se un mutex non viene acquisito entro un tempo limite, rilascia tutti e riprova:

```c
if (pthread_mutex_timedlock(&mutex, &timeout) == ETIMEDOUT) {
    // Timeout: rilascia altre risorse e riprova
}
```

Evita attese infinite, ma non garantisce correttezza.

---

> [!abstract] Riepilogo: Punti Chiave
> 1. **Condition variable:** permette ai thread di aspettare un evento e essere svegliati
> 2. **Pattern monitor:** mutex + condition variable per sincronizzazione complessa
> 3. **Problema dei 5 filosofi:** classico problema; soluzione: una variable per thread, test su vicini
> 4. **Signal vs broadcast:** signal sveglia uno, broadcast tutti; equivalenti con una variable per thread
> 5. **Deadlock:** attesa circolare. Cause: mutua esclusione, hold-and-wait, non-preemption, circular wait
> 6. **Prevenzione:** ordinamento totale dei mutex, acquisizione atomica, timeout

---

> [!question] Domande d'esame frequenti
> - Perché il problema naïve dei 5 filosofi causa deadlock?
> - Quale è la differenza tra signal e broadcast?
> - Quali sono le 4 condizioni di Coffman?
> - Come si previene il deadlock con ordinamento totale?

> [!todo] Esercizi suggeriti
> - [ ] Implementare i 5 filosofi da zero
> - [ ] Modificare la soluzione per eliminare starvation
> - [ ] Simulare il deadlock con inversione di mutex
> - [ ] Misurare le performance: signal vs broadcast

---

#SO #condition-variables #monitor #deadlock #sincronizzazione #5-filosofi #signal-broadcast
