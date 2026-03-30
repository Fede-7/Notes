---
date: 2026-03-26
corso: Sistemi Operativi
docente: N/D
lezione: Signal handling, cancellazione thread e introduzione allo scheduling
tags: [SO, signal-handling, thread-cancellation, scheduling, CPU-burst, FCFS, SJF]
---

# SO — Lezione: Signal Handling, Cancellazione Thread e Introduzione allo Scheduling

**Corso:** Sistemi Operativi

---

## Argomenti trattati

- Ripresa dell'esempio di signal handling con `pthread_kill` e maschere di segnali
- Comportamento dei segnali pending e non-accodamento dei segnali ordinari
- Cancellazione dei thread: asincrona, deferred e cancellation point
- TID user-level vs. TID kernel-level: come distinguerli
- Ispezione dei thread tramite `ps`, `/proc` e `sys_gettid`
- Introduzione allo scheduling della CPU
- Criteri di scheduling
- Algoritmo FCFS (First Come First Served)
- Algoritmo SJF (Shortest Job First) e stima tramite media esponenziale

---

## 1. Ripresa: signal handling in contesto multi-thread

### Il programma di esempio (caso 1 — mask1)

Il thread principale:
1. Crea tre thread secondari (`tid1`, `tid2`, `tid3`), ciascuno esegue una funzione che stampa periodicamente di essere attivo.
2. Invia un segnale `SIGUSR1` individualmente a ciascun thread con `pthread_kill(tidN, SIGUSR1)`.
3. Imposta una maschera che blocca `SIGUSR1` **solo per se stesso** (dopo che i thread secondari sono già stati lanciati).
4. Dopo un breve sleep, invia `SIGUSR1` all'**intero processo** con `kill(getpid(), SIGUSR1)`.

**Risultato**: i primi tre `pthread_kill` vengono gestiti ciascuno dal thread destinatario (il kernel mette il segnale in pending per quel thread specifico). Il quarto `kill` al processo intero viene gestito da uno dei thread secondari — il thread principale non lo gestisce perché ha una maschera che lo blocca.

> [!warning] L'ordine della maschera è fondamentale
> La maschera impostata con `pthread_sigmask` vale **solo per il thread che la chiama**. Se la maschera fosse impostata **prima** della creazione dei thread, verrebbe **ereditata** da tutti i thread figli, bloccando il segnale per tutti.

### Caso 2 — mask2: maschera impostata prima del lancio dei thread

```c
// Prima si imposta la maschera nel thread principale
sigemptyset(&set);
sigaddset(&set, SIGUSR1);
pthread_sigmask(SIG_BLOCK, &set, NULL);

// Poi si lanciano i thread (che ereditano la maschera)
pthread_create(&tid1, NULL, start_fn, "thread1");
// ...

// Si invia il segnale all'intero processo
kill(getpid(), SIGUSR1);
```

**Risultato**: nessun thread gestisce il segnale. Tutti lo hanno in pending (il kernel lo conserva, non lo perde), ma nessuno lo sblocca. Il segnale rimane "in sospeso".

### Caso 3 — mask3: maschera ereditata, poi sblocco esplicito

```c
// Maschera impostata prima → ereditata dai thread
// Si inviano 3 SIGUSR1 al processo
kill(getpid(), SIGUSR1);
kill(getpid(), SIGUSR1);
kill(getpid(), SIGUSR1);

// Il thread principale sblocca la maschera
pthread_sigmask(SIG_UNBLOCK, &set, NULL);
// → l'handler scatta una sola volta
```

**Risultato atteso e osservato**: l'handler scatta **una sola volta**, nonostante siano stati inviati tre segnali.

> [!abstract] Definizione: Accodamento dei segnali
> I segnali ordinari (come `SIGUSR1`, `SIGINT`) **non si accumulano**: se un segnale è già pending per un thread/processo, invii successivi dello stesso segnale vengono collassati in uno solo. Quando la maschera viene rimossa, l'handler scatta una volta sola.
>
> I **segnali real-time** (numerati da `SIGRTMIN` a `SIGRTMAX`) si comportano diversamente: vengono **accodati** e consegnati tutti in sequenza.

> [!tip] Compilazione con supporto thread
> Ricordarsi sempre di aggiungere `-lpthread` (o `-pthread`) alla riga di compilazione:
> ```bash
> gcc -o programma sorgente.c -lpthread
> ```

---

## 2. Cancellazione dei thread

Un thread può essere cancellato da un altro thread tramite `pthread_cancel(tid)`. Il comportamento dipende dallo **stato di cancellazione** del thread destinatario.

| Stato | Come si imposta | Comportamento |
|---|---|---|
| **Enabled + Deferred** (default) | — | Il thread viene cancellato solo in un cancellation point |
| **Enabled + Asynchronous** | `pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL)` | Il thread può essere cancellato in qualsiasi momento |
| **Disabled** | `pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, NULL)` | La richiesta di cancellazione rimane pending; verrà gestita quando verrà riabilitata |

### Cancellation point

Un **cancellation point** è un momento in cui il thread accetta una richiesta di cancellazione pending. Esempi di cancellation point naturali:

- `sleep()`: il thread è in attesa e può essere cancellato.
- Chiamate di I/O (lettura/scrittura su file, rete, ecc.): il thread sta attendendo una risposta dal kernel.
- Punti di sincronizzazione (`pthread_cond_wait`, ecc.).
- `pthread_testcancel()`: cancellation point **artificiale** inserito manualmente dal programmatore per thread CPU-bound che non hanno pause naturali.

> [!example] Cancellazione con stato disabled (esempio mask_cancel2)
> ```c
> void *start_fn(void *arg) {
>     pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, NULL); // disabilita cancellazione
>     for (int i = 1; i <= 5; i++) {
>         printf("%d\n", i);
>         sleep(1);
>     }
>     pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, NULL);  // riabilita
>     // Il prossimo cancellation point (es. sleep) eseguirà la cancellazione pending
>     while(1) sleep(1);  // cancellation point
> }
> ```
> Il thread principale chiama `pthread_cancel(tid)` subito dopo aver creato il thread, ma la richiesta rimane in pending finché la cancellazione non viene riabilitata. Il thread termina solo dopo aver completato il ciclo da 1 a 5.

---

## 3. TID user-level vs. TID kernel-level

In Linux, il modello è **one-to-one**: ogni user thread corrisponde a un kernel thread. Tuttavia, i due livelli usano identificativi diversi.

| Identificativo | Come si ottiene | Chi lo usa |
|---|---|---|
| TID user-level | `pthread_self()` | La libreria `pthreads` (un numero grande, gestito dalla libreria) |
| TID kernel-level | `syscall(SYS_gettid)` | Il kernel (un intero progressivo, visibile con `ps`) |
| PID del processo | `getpid()` | Entrambi i livelli |

> [!example] Codice per stampare entrambi i TID
> ```c
> #include <sys/syscall.h>
> #include <unistd.h>
>
> void *worker(void *arg) {
>     pthread_t user_tid = pthread_self();
>     pid_t kernel_tid = syscall(SYS_gettid);
>     printf("User TID: %lu, Kernel TID: %d\n", user_tid, kernel_tid);
>     // ...
> }
> ```
> **Attenzione**: `SYS_gettid` non è standard POSIX; funziona su Linux ma non è portabile.

### Ispezione dei thread da shell

```bash
# Thread di un processo specifico
ps -T -p <PID>        # SPID = kernel TID

# Tutti i processi/thread del sistema (mostra lightweight processes)
ps -eLf               # LWP = kernel TID

# Tramite /proc (filesystem virtuale)
ls /proc/<PID>/task/  # una cartella per ogni thread (TID kernel)
```

> [!example] Esempio
> Un processo con PID 1812 che ha lanciato 5 thread avrà kernel TID 1812 (thread principale), 1813, 1814, 1815, 1816, 1817. Si vedono tutti con `ps -T -p 1812`.

---

## 4. Introduzione allo scheduling della CPU

### Motivazione

In un sistema multiprogrammato, quando un processo va in attesa (I/O, sincronizzazione) la CPU rimane libera. Lo **scheduler** decide quale tra i processi pronti mandare in esecuzione, per massimizzare l'utilizzo della CPU e rispettare criteri di equità e performance.

I cicli di esecuzione dei processi si alternano tra:

- **CPU burst**: il processo usa intensamente la CPU.
- **I/O burst**: il processo attende un'operazione di I/O.

Osservazione empirica: la maggior parte dei processi nei sistemi consumer ha burst di CPU molto brevi (pochi millisecondi). Pochi processi hanno burst lunghi.

### Quando interviene lo scheduler

| Transizione di stato | Tipo |
|---|---|
| Running → Waiting (richiesta I/O) | Senza prelazione — il processo cede volontariamente |
| Running → Ready (time slice scaduto o interrupt) | **Con prelazione** — il processo viene interrotto forzatamente |
| Waiting → Ready (I/O completato) | Può richiedere prelazione |
| Terminazione | Senza prelazione — il processo cede definitivamente |

> [!abstract] Definizione: Prelazione (Preemption)
> Si dice che lo scheduling è **con prelazione** se il sistema può interrompere un processo in esecuzione per mandarne in esecuzione un altro. Senza prelazione, i processi girano fino a terminazione o blocco volontario.

### Il dispatcher

Lo **dispatcher** è il componente che materialmente trasferisce il controllo della CPU al processo scelto dallo scheduler. Il suo costo è detto **dispatch latency**: tempo necessario per salvare il contesto del vecchio processo e caricare quello del nuovo.

---

## 5. Criteri di scheduling

| Criterio | Obiettivo | Rilevante per |
|---|---|---|
| **Utilizzo CPU** | Massimizzare % di utilizzo | Tutti i sistemi |
| **Throughput** | Massimizzare job completati per unità di tempo | Sistemi batch |
| **Turnaround time** | Minimizzare il tempo medio di completamento (da arrivo a fine) | Processi lunghi, batch |
| **Waiting time** | Minimizzare il tempo medio in coda Ready | Tutti |
| **Response time** | Minimizzare il tempo alla prima risposta | Processi interattivi |

> [!important] Minimizzare la varianza è spesso più importante della media
> Un sistema con tempi di risposta imprevedibili (alta varianza) è percepito come inaffidabile anche se la media è bassa. Ridurre la varianza aumenta la predicibilità e la fiducia dell'utente.

---

## 6. Algoritmo FCFS (First Come First Served)

Il processo che arriva per primo viene servito per primo. Nessuna prelazione.

> [!example] Esempio FCFS
> Tre processi arrivano al tempo 0 in ordine P1, P2, P3 con burst time rispettivamente 24, 3, 3 ms.
>
> ```
> | P1 (24ms) | P2 (3ms) | P3 (3ms) |
> 0          24         27         30
> ```
>
> Tempi di attesa: P1=0, P2=24, P3=27. **Media: 17 ms.**

**Problema — effetto convoglio**: un processo lungo (CPU-bound) blocca tutti i processi brevi (I/O-bound) che lo seguono, degradando il tempo di risposta dell'intero sistema.

---

## 7. Algoritmo SJF (Shortest Job First)

Ad ogni ciclo di scheduling, si manda in esecuzione il processo con il **burst time più breve**. Questo minimizza il tempo medio di attesa.

> [!example] Esempio SJF
> Stessi tre processi, ma ordinati per burst time crescente: P2 (3), P3 (3), P1 (24).
>
> ```
> | P2 (3ms) | P3 (3ms) | P1 (24ms) |
> 0          3          6           30
> ```
>
> Tempi di attesa: P2=0, P3=3, P1=6. **Media: 3 ms** (vs. 17 ms di FCFS).

> [!abstract] Proprietà: ottimalità di SJF
> SJF è **ottimale** rispetto alla minimizzazione del tempo medio di attesa. Non esiste algoritmo non-preemptive che faccia meglio.

> [!warning] Il problema pratico: non si conosce il burst time futuro
> Il sistema operativo non può sapere a priori quanto durerà il prossimo CPU burst di un processo. SJF è quindi un **algoritmo teorico di riferimento**; in pratica si usa solo in contesti dove i tempi sono noti (es. job batch schedulati manualmente).

> [!example] Esempio SJF con 4 processi e oracolo
> P1 burst=6, P2 burst=8, P3 burst=7, P4 burst=3. Ordine: P4, P1, P3, P2.
>
> Tempi di attesa: P4=0, P1=3, P3=9, P2=16. **Media: 7 ms.**

---

## 8. Stima del burst time: media esponenziale

Per stimare la durata del prossimo CPU burst, il sistema operativo usa la storia delle esecuzioni passate tramite una **media esponenziale**:

$$\tau_{n+1} = \alpha \cdot t_n + (1 - \alpha) \cdot \tau_n$$

dove:
- $t_n$ = durata effettiva dell'$n$-esimo CPU burst (valore osservato)
- $\tau_n$ = stima che era stata fatta per l'$n$-esimo burst
- $\tau_{n+1}$ = nuova stima per il prossimo burst
- $\alpha \in [0, 1]$ = peso relativo tra osservazione recente e storia passata

Espandendo la formula ricorsivamente si ottiene:

$$\tau_{n+1} = \alpha t_n + (1-\alpha)\alpha t_{n-1} + (1-\alpha)^2 \alpha t_{n-2} + \ldots$$

I burst più recenti pesano di più; i burst più vecchi **sfumano esponenzialmente** (da cui il nome). L'ipotesi iniziale $\tau_0$ contribuisce sempre meno con il passare delle iterazioni.

> [!example] Esempio con $\alpha = 0.5$, $\tau_0 = 10$
> - Burst reale $t_1 = 6$ → $\tau_2 = 0.5 \cdot 6 + 0.5 \cdot 10 = 8$
> - Burst reale $t_2 = 4$ → $\tau_3 = 0.5 \cdot 4 + 0.5 \cdot 8 = 6$
> - E così via: la stima insegue il valore reale smorzando le fluttuazioni.

---

> [!summary] Punti chiave della lezione
> - I segnali ordinari pending non si accumulano: N invii → 1 sola consegna. I segnali real-time invece si accodano.
> - Una maschera impostata prima del lancio dei thread viene ereditata da tutti i figli; impostata dopo, vale solo per il thread corrente.
> - La cancellazione deferred (default) aspetta un cancellation point; si possono aggiungere cancellation point artificiali con `pthread_testcancel()`.
> - TID user-level (`pthread_self`) e TID kernel-level (`SYS_gettid`) sono diversi ma in Linux corrispondono one-to-one.
> - Lo scheduler minimizza idle time della CPU scegliendo quale processo mandare in esecuzione dalla coda Ready.
> - FCFS: semplice, soffre dell'effetto convoglio. SJF: ottimale per tempo medio di attesa, ma richiede di conoscere i burst time futuri.

## Prossimi argomenti

- [ ] Esercitazione pratica su thread, segnali e cancellazione (martedì)
- [ ] Scheduling con prelazione: Round Robin
- [ ] Scheduling a priorità e problemi di starvation
- [ ] Scheduling su sistemi multicore

#SO #signal-handling #thread-cancellation #scheduling #FCFS #SJF #CPU-burst
