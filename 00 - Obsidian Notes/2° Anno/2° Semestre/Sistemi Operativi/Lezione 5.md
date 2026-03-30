---
date: 2026-03-24
corso: Sistemi Operativi
docente: N/D
lezione: Thread (concetti, modelli di mapping e librerie POSIX)
tags: [SO, thread, user-thread, kernel-thread, POSIX, pthread, parallelismo]
---

# SO — Lezione: Thread — Concetti, Modelli di Mapping e Librerie POSIX

**Corso:** Sistemi Operativi

---

## Argomenti trattati

- Benefici dei thread rispetto ai processi
- Concorrenza vs. parallelismo (architetture single-core e multicore)
- Legge di Amdahl: stima teorica dello speedup
- User thread vs. kernel thread
- Modelli di mapping: many-to-one, one-to-one, many-to-many
- Lightweight process e upcall
- Librerie POSIX (`pthreads`): API principali
- Esempi di codice con `pthread_create`, `pthread_join`, `pthread_exit`
- Problematiche: `fork` dentro un thread, `exec` dentro un thread

---

## 1. Benefici dei thread

Un **thread** è un flusso esecutivo che condivide lo spazio di indirizzamento del processo che lo ha creato. Rispetto alla creazione di un nuovo processo (tramite `fork`), i thread offrono:

| Beneficio | Spiegazione |
|---|---|
| **Esecuzione continua** | Se un thread si blocca su I/O, gli altri continuano a lavorare |
| **Condivisione risorse** | I thread comunicano direttamente tramite variabili condivise, senza pipe o memoria condivisa esplicita |
| **Economia** | Creare e distruggere un thread è più veloce di un processo; il context switch è più leggero (lo stack è più piccolo) |
| **Scalabilità** | Su architetture multicore, thread diversi possono girare su core diversi contemporaneamente |

> [!important] Thread e architetture multicore
> Con l'aumentare del numero di core nelle CPU moderne (es. 16 core fisici, 24 hardware thread), la capacità di parallelizzare tramite thread diventa un principio architetturale fondamentale, non solo un'ottimizzazione.

---

## 2. Concorrenza vs. parallelismo

> [!abstract] Definizione: Concorrenza
> Due o più task sono **concorrenti** se il sistema porta avanti la loro computazione nell'arco dello stesso periodo di tempo, anche su un singolo core (tramite time-sharing).

> [!abstract] Definizione: Parallelismo
> Due o più task sono **paralleli** se vengono eseguiti **fisicamente allo stesso istante** su core o CPU distinti.

La concorrenza è possibile anche con un solo core. Il parallelismo richiede più core.

### Hardware thread (thread fisici)

Alcuni core moderni supportano più **hardware thread** contemporaneamente: eseguono fisicamente due thread su un singolo core fisico nei cicli in cui uno dei due è in attesa (es. di accesso a memoria). Il sistema operativo vede questi hardware thread come "core logici".

> [!example] Esempio
> Una CPU con 16 core fisici e 24 hardware thread: lo scheduler vede 24 slot disponibili. Alcuni core fisici "valgono doppio" perché gestiscono 2 thread contemporaneamente a livello hardware, senza che il SO ne sia consapevole.

### Tipi di parallelismo

- **Parallelismo sui dati**: stessa operazione eseguita su sottoinsiemi diversi degli stessi dati (es. SIMD, parallelismo di array).
- **Parallelismo sui task**: thread diversi eseguono funzioni diverse contemporaneamente.

---

## 3. Legge di Amdahl

Stima teorica del guadagno in velocità (speedup) ottenibile aumentando il numero di core, in funzione della percentuale di codice non parallelizzabile.

> [!abstract] Definizione: Legge di Amdahl
> Sia $S$ la frazione seriale del programma (non parallelizzabile, $0 \leq S \leq 1$). Lo speedup su $n$ core è:
> $$\text{Speedup}(n) = \frac{1}{S + \frac{1-S}{n}}$$

Casi limite:

- $n = 1$: Speedup = 1 (nessun guadagno, un solo core).
- $S = 1$: Speedup = 1 per qualsiasi $n$ (tutto seriale, nessun guadagno possibile).
- $n \to \infty$: Speedup $\to 1/S$ (limite superiore dello speedup).

> [!example] Applicazione al 75% parallela, 25% seriale ($S = 0.25$)
> - $n = 2$: Speedup $= 1/(0.25 + 0.375) = 1.6$
> - $n \to \infty$: Speedup $\leq 4$
>
> Raddoppiare i core non raddoppia le prestazioni: la componente seriale è il collo di bottiglia.

> [!tip] Implicazione pratica
> La legge di Amdahl suggerisce di analizzare la componente seriale del proprio codice prima di investire in più core. Se la parte non parallelizzabile è dominante, aggiungere core porta a ritorni decrescenti rapidamente.

---

## 4. User thread vs. Kernel thread

> [!abstract] Definizione: User thread
> Thread gestiti interamente nello **spazio utente** da una libreria. Il kernel non ne è a conoscenza direttamente. Il thread control block (TCB) è allocato e gestito dalla libreria.

> [!abstract] Definizione: Kernel thread
> Thread la cui esistenza è nota al kernel. Il kernel mantiene il proprio TCB (analogamente al PCB per i processi) e può schedularli direttamente.

---

## 5. Modelli di mapping

### Many-to-one

```
User threads:   T1  T2  T3  T4
                 ↘  ↓  ↙  ↙
Kernel thread:      KT1
```

Tutti gli user thread di un processo si mappano su **un unico kernel thread**. La gestione è interamente in user space (libreria).

**Vantaggio**: semplicità lato kernel; nessun overhead di chiamate di sistema per creare thread.

**Svantaggi**:
- Se un thread si blocca (es. su I/O), si bloccano tutti (il kernel vede un unico thread bloccato).
- Nessun vero parallelismo su multicore.

> [!quote]
> "Questo poteva avere un senso quando avevamo architetture single core. Adesso che sono architetture multicore non si utilizza questo tipo di mapping."

### One-to-one

```
User threads:   T1   T2   T3
                 ↓    ↓    ↓
Kernel threads: KT1  KT2  KT3
```

Per ogni user thread creato, viene creato un corrispondente kernel thread. È il modello standard di Linux, Windows, macOS, Solaris, Android.

**Vantaggi**:
- Vero parallelismo su multicore.
- Se un thread si blocca, gli altri continuano.

**Svantaggio**: la proliferazione incontrollata di thread crea altrettanti kernel thread, potenzialmente saturando le risorse del kernel. La responsabilità di non esagerare è dello sviluppatore.

### Many-to-many

```
User threads:   T1  T2  T3  T4  T5
                 ↘↙    ↓    ↘↙
Kernel threads:  KT1  KT2  KT3
```

$m$ user thread si mappano su $k \leq m$ kernel thread. La libreria utente gestisce uno **scheduler interno** che assegna user thread ai kernel thread disponibili.

**Vantaggi**: il numero di kernel thread è controllato; flessibilità nel mapping.

**Svantaggio**: implementazione più complessa; richiede un meccanismo di schedulazione aggiuntivo in user space.

### Modello ibrido (two-level)

Alcune librerie combinano many-to-many e one-to-one: la maggior parte dei thread usa il pool shared, ma alcuni thread critici possono essere mappati one-to-one su un kernel thread dedicato.

---

## 6. Lightweight Process e Upcall

Nel modello many-to-many, i kernel thread vengono "esposti" alla libreria utente attraverso strutture intermedie dette **Lightweight Process (LWP)**. Attenzione: in Linux questo termine indica i kernel thread nel modello one-to-one; il significato varia tra i sistemi.

Il meccanismo di **upcall** permette al kernel di comunicare "dal basso verso l'alto" verso la libreria utente: ad esempio, avvisare la libreria che un kernel thread sta per bloccarsi, permettendo alla libreria di sganciare l'user thread e agganciarlo a un altro LWP disponibile.

---

## 7. Librerie POSIX (`pthreads`)

La libreria **POSIX Threads** (`pthread.h`) è lo standard per la gestione dei thread su sistemi Unix/Linux/macOS. È una specifica (non un'implementazione): definisce le interfacce, la semantica è garantita dallo standard POSIX.

### Funzioni principali

| Funzione | Descrizione |
|---|---|
| `pthread_create(tid, attr, start_fn, arg)` | Crea un nuovo thread; `start_fn` è la funzione di avvio |
| `pthread_exit(status)` | Termina il thread corrente, restituisce `status` |
| `pthread_join(tid, status_ptr)` | Aspetta la terminazione del thread `tid` (equivalente di `wait`) |
| `pthread_self()` | Restituisce il TID del thread corrente |
| `pthread_attr_init(attr)` | Inizializza gli attributi del thread |

> [!important] Prototipo della funzione di avvio
> Ogni funzione passata a `pthread_create` deve avere questa firma:
> ```c
> void *start_function(void *arg);
> ```
> Sia l'argomento che il valore di ritorno sono puntatori generici (`void *`). Il cast al tipo corretto avviene nel corpo della funzione.

### Compilazione

```bash
gcc -o programma programma.c -lpthread
```

Il flag `-lpthread` è necessario per linkare la libreria pthreads.

---

## 8. Esempi di codice

### Esempio 1: somma dei primi n numeri

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int sum = 0;  // variabile globale condivisa

void *runner(void *param) {
    int upper = atoi((char *)param);
    for (int i = 1; i <= upper; i++)
        sum += i;
    pthread_exit(0);
}

int main(int argc, char *argv[]) {
    pthread_t tid;
    pthread_attr_t attr;

    pthread_attr_init(&attr);
    pthread_create(&tid, &attr, runner, argv[1]);
    pthread_join(tid, NULL);  // attende che runner finisca

    printf("Somma = %d\n", sum);
    return 0;
}
```

> [!warning] Cosa succede senza `pthread_join`
> Se si rimuove `pthread_join`, il thread principale continua immediatamente dopo la creazione. La stampa di `sum` avviene **prima** che `runner` abbia terminato: si legge un valore incompleto o 0. Questo è un esempio di **race condition**.

> [!example] Variabili globali vs. locali nei thread
> - **Variabile globale** (`sum` nell'esempio): allocata nell'heap del processo, visibile a tutti i thread. Modifiche persistono dopo la terminazione del thread.
> - **Variabile locale** del thread: allocata nello stack del thread; deallocata alla terminazione. Restituire un puntatore a una variabile locale è un errore (dangling pointer).
> - **Variabile allocata dinamicamente** (`malloc`): nell'heap del processo, visibile a tutti. Deve essere liberata (`free`) dal thread principale, altrimenti si ha un memory leak.

### Esempio 2: stesso `runner` su più thread

```c
pthread_t tid1, tid2;
char *msg1 = "Sono il thread 1";
char *msg2 = "Sono il thread 2";

pthread_create(&tid1, NULL, runner, (void *)msg1);
pthread_create(&tid2, NULL, runner, (void *)msg2);

pthread_join(tid1, NULL);
pthread_join(tid2, NULL);
```

La stessa funzione `runner` viene lanciata due volte in parallelo con argomenti diversi. Ogni thread ha il proprio stack e il proprio TID (`pthread_self()`).

---

## 9. Problematiche con `fork` ed `exec` nei thread

### `fork` dentro un thread

Quando un thread chiama `fork`, il comportamento standard POSIX è: **solo il thread chiamante viene duplicato** nel processo figlio. Il figlio nasce come processo single-threaded (gli altri thread del padre non vengono copiati).

**Problema**: il figlio si porta in memoria tutte le strutture dati del processo padre (incluse quelle degli altri thread), senza i thread corrispondenti. Questo può lasciare strutture dati in stato incoerente (mutex bloccati da thread inesistenti nel figlio, ecc.).

> [!warning] Evitare `fork` all'interno di thread
> È buona norma chiamare `fork` **prima** di creare qualsiasi thread. Se è inevitabile farlo dentro un thread, usare le funzioni `pthread_atfork` per registrare handler di pulizia eseguiti prima e dopo il `fork`.

### `exec` dentro un thread

Se un thread chiama `exec`, il nuovo programma **sostituisce l'intero processo**: tutti i thread vengono terminati bruscamente e il nuovo programma parte come processo single-threaded. `exec` è molto più "pulita" di `fork` in contesto multi-thread.

---

## 10. Threading implicito

Oltre all'uso diretto delle API POSIX (threading esplicito), esistono meccanismi di **threading implicito**:

- **Thread pool**: insieme di thread pre-allocati, pronti a ricevere task. Elimina l'overhead di creazione/distruzione ripetuta.
- **OpenMP**: direttive di preprocessore che indicano al compilatore di parallelizzare regioni del codice.

```c
#include <omp.h>

#pragma omp parallel for
for (int i = 0; i < N; i++) {
    // il compilatore parallelizza automaticamente questo ciclo
}
```

---

> [!summary] Punti chiave della lezione
> - I thread condividono lo spazio di indirizzamento del processo: comunicano direttamente ma possono andare in conflitto (race condition).
> - La legge di Amdahl mostra che la parte seriale limita lo speedup ottenibile con più core.
> - User thread e kernel thread sono distinti; i modelli di mapping (many-to-one, one-to-one, many-to-many) definiscono come vengono collegati.
> - Linux/Windows/macOS usano one-to-one: ogni user thread crea un kernel thread.
> - `pthread_join` è l'equivalente di `wait` per i thread; senza di esso si rischia una race condition.
> - `fork` dentro un thread duplica solo il thread chiamante: il figlio è single-threaded ma si porta le strutture dati di tutti.

## Prossimi argomenti

- [ ] Esercitazione pratica su thread con esempi di race condition
- [ ] Meccanismi di sincronizzazione: mutex, semafori, variabili di condizione
- [ ] Scheduling dei thread: algoritmi e politiche
- [ ] Nota: giovedì lezione **da remoto** (Career Day occupa le aule)

#SO #thread #user-thread #kernel-thread #POSIX #pthread #parallelismo #concorrenza
