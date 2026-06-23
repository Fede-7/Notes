# Lezione 8: Scheduling CPU

## Obiettivi

- Introdurre il concetto dello **scheduling CPU**.
- Descrivere gli **algoritmi di scheduling** di CPU.
- Discutere i **criteri di valutazione** degli algoritmi di scheduling.
- Esaminare algoritmi di scheduling di vari SO.

## Concetti di Base

- Massimo utilizzo di CPU con **multiprogramming**.
- Un programma non usa sempre la CPU continuamente. A volte calcola… a volte aspetta qualcosa (disco, input, rete).
- **Cicli CPU–I/O Burst** – L’esecuzione dei processi consiste di cicli di esecuzione CPU e attese I/O.
- CPU burst seguiti da I/O burst.
- Distribuzione di CPU burst è una **problematica importante**.

## Istogramma dei tempi di CPU-burst

Se misuriamo i CPU burst nei sistemi reali, otteniamo qualcosa del genere ...

I sistemi reali hanno tanti processi che fanno **piccoli lavori** e pochi che fanno **lavori lunghi**.

## CPU Scheduler

- **Short-term scheduler** seleziona tra processi nella coda ready e alloca la CPU a uno di loro.
- Le code possono essere ordinate in modi diversi.

Le decisioni di CPU scheduling occorrono quando i processi:
1. Passano dallo stato **running** a **waiting** (es. I/O req o wait).
2. Passano dallo stato **running** a **ready** (es. interrupt).
3. Passano da **waiting** a **ready** (es. I/O completo).
4. **Terminano** (es. terminazione).

In situazioni 1 e 4 il processo cede il controllo (**non prelazione**).

- Schemi senza prelazione (**nonpreemptive**) o con prelazione (**preemptive**).
- **Scheduling senza prelazione**: il processo in esecuzione continua fino a fine o fino a un wait.
- **Scheduling con prelazione**:
  - Problema accesso a dati condivisi (**race condition**).
  - Problema prelazione in modalità kernel (operazioni non interrompibili).
  - Problema interruzioni durante attività cruciali (**sezioni critiche**).

## Dispatcher

Il **Dispatcher** dalla controllo della CPU ai processi selezionati dallo short-term scheduler e richiede:
- switching del contesto.
- switching allo user mode.
- salto alla corretta locazione del programma utente per ripartire con quel programma.

**Latenza di dispatch** – tempo necessario al dispatcher per fermare un processo e mandarne un altro in running.
- Deve essere il più breve possibile.

**Context switch**:
```monospace
vmstat 1 3
cpu ----
24
225
339
```

*in*: The number of interrupts per second, including the clock.
*cs*: The number of context switches per second.

## Criteri di Scheduling

- **Utilizzo CPU** – percentuale di CPU utilizzata; occorre mantenere la CPU occupata (comando `top`).
- **Throughput** – numero di processi che completano l’esecuzione per unità di tempo.
- **Turnaround time** – tempo di completamento di processo.
  - Tempo totale per eseguire un processo.
  - Accesso memoria + coda ready + CPU + I/O.
- **Waiting time** – tempo di attesa per un processo nella coda ready.
- **Response time** – tempo che intercorre tra una richiesta e la prima risposta.
  - Importante per sistemi interattivi, quando l’elaborazione continua dopo un output.
  - Alternativa al tempo di turnaround che prevede l’esecuzione completa.

## Scheduling: Criteri di Ottimizzazione

- Massimo utilizzo CPU.
- Massimo throughput.
- Minimo tempo di turnaround.
- Minimo tempo di waiting.
- Minimo tempo di risposta.

In molti sistemi (desktop, laptop) è più importante **minimizzare la varianza** dei tempi di risposta che il tempo medio.

## First-Come, First-Served (FCFS) Scheduling

| Process | Burst Time |
| :--- | :--- |
| $P_1$ | 24 |
| $P_2$ | 3 |
| $P_3$ | 3 |

Assumendo che i processi nell’ordine: $P_1, P_2, P_3$.

Il **Gantt Chart** dello schedule è:

| $P_1$ | $P_2$ | $P_3$ |
| :--- | :--- | :--- |

Tempi di attesa per $P_1 = 0; P_2 = 24; P_3 = 27$.
**Media del tempo di attesa**: $(0 + 24 + 27)/3 = 17$.

## FCFS Scheduling

Assumendo i processi nell’ordine: $P_2, P_3, P_1$.

Il Gantt diventa:

$$\begin{array}{c|c|c}
P_2 & P_3 & P_1 \\
\hline
0 & 3 & 6 \\
\end{array}$$

Tempi di attesa $P_1 = 6; P_2 = 0; P_3 = 3$.
**Tempo di attesa medio**: $(6 + 0 + 3)/3 = 3$.
- Molto meglio di prima.

**Effetto Convoy** - processi brevi dietro i processi lunghi.
- Considera un processo CPU-bound e tanti I/O-bound.
- Sbrigare i processi brevi per migliorare i tempi di risposta.

## Shortest-Job-First (SJF) Scheduling

- Associa ad ogni processo la **lunghezza del prossimo CPU burst**.
- Lunghezza usata per schedulare il processo con burst più breve.

**SJF è ottimale** – minima attesa media per un insieme di processi.
- Difficile conoscere la lunghezza della prossima richiesta di CPU.
- **Soluzione**: uso di stime basate sul comportamento passato ed esecuzione del processo con il minor tempo di esecuzione stimato.

- Algoritmo particolarmente indicato per l'esecuzione batch dei job per i quali i tempi di esecuzione sono conosciuti a priori.
- Lo scheduler dovrebbe utilizzare questo algoritmo quando nella coda di input risiedono job di **uguale importanza**.

## Esempio di SJF

| Process | Burst Time |
| :--- | :--- |
| $P_1$ | 6 |
| $P_2$ | 8 |
| $P_3$ | 7 |
| $P_4$ | 3 |

**SJF scheduling chart**:

| $P_4$ | $P_1$ | $P_3$ | $P_2$ |
| :--- | :--- | :--- | :--- |
| 0 | 3 | 9 | 16 | 24 |

**Tempo di attesa medio** = $(3 + 16 + 9 + 0) / 4 = 7$.

## Lunghezza del prossimo CPU Burst

- Si può solo stimare – simile alla precedente.
- Prendi il processo con il CPU burst stimato come il più breve.
- Utilizzare la lunghezza del CPU burst precedente, usando la **media esponenziale** delle lunghezze precedenti.

1. $t_n =$ actual length of $n^{th}$ CPU burst.
2. $\tau_{n+1} =$ predicted value for the next CPU burst.
3. $\alpha, 0 \leq \alpha \leq 1$.
4. Definisci: $\tau_{n+1} = \alpha t_n + (1 - \alpha)\tau_n$.

- Solitamente $\alpha$ settato a $\frac{1}{2}$.
- Versione preemptiva chiamata **shortest-remaining-time-first**.

## Lunghezza del prossimo CPU Burst (Esempio)

CPU burst ($t_i$): 6 4 6 4 13 13 13 …
"guess" ($\tau_i$): 10 8 6 6 5 9 11 12 …

## Esempi di Exponential Averaging

- $\alpha = 0$
  - $\tau_{n+1} = \tau_n$
  - Storia recente non conta.
- $\alpha = 1$
  - $\tau_{n+1} = \alpha t_n$
  - Conta solo l’ultimo CPU burst.

Espandendo la formula si ottiene:
$$\tau_{n+1} = \alpha t_n + (1 - \alpha) \alpha t_{n-1} + \ldots$$
$$+ (1 - \alpha)^{j} \alpha t_{n-j} + \ldots$$
$$+ (1 - \alpha)^{n+1} \tau_0$$

Sia $\alpha$ che $(1 - \alpha)$ sono minori o uguali ad 1, ogni termine successivo ha minor peso del predecessore.

## Esempio di Shortest-remaining-time-first

Si considerano diversi tempi di arrivo e si introduce la **prelazione**.

| Process | Arrival Time | Burst Time |
| :--- | :--- | :--- |
| $P_1$ | 0 | 8 |
| $P_2$ | 1 | 4 |
| $P_3$ | 2 | 9 |
| $P_4$ | 3 | 5 |

**Preemptive SJF Gantt Chart**:

| $P_1$ | $P_2$ | $P_4$ | $P_1$ | $P_3$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 5 | 10 | 17 | 26 |

**Tempo attesa medio** = $[(10-1)+(1-1)+(17-2)+5-3)]/4 = 26/4 = 6.5 \text{ msec}$.
- Senza prelazione: 8.75 msec.

## Scheduling con Priorità

- Numero di **priorità** (intero) associato ad ogni processo.
- CPU allocata al processo con più alta priorità (**minor intero ≡ maggiore priorità**).
  - Preemptive.
  - Nonpreemptive.
- SJF è un priority scheduling con priorità inversamente proporzionale alla predizione del prossimo CPU.
- **Problema ≡ Starvation** – processi a bassa priorità mai eseguiti.
- **Soluzione ≡ Aging** – al passare del tempo aumenta la priorità del processo.

## Esempio di Priority Scheduling

| Process | Burst Time | Priority |
| :--- | :--- | :--- |
| $P_1$ | 10 | 3 |
| $P_2$ | 1 | 1 |
| $P_3$ | 2 | 4 |
| $P_4$ | 1 | 5 |
| $P_5$ | 5 | 2 |

**Priority scheduling Gantt Chart**:

| $P_2$ | $P_5$ | $P_1$ | $P_3$ | $P_4$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 6 | 16 | 18 | 19 |

**Tempo di attesa medio** = 8.2 msec.

## Round Robin (RR)

- Ogni processo riceve una piccola unità di CPU (**time quantum $q$**), di solito 10-100 msec.
- A tempo scaduto il processo viene prelazionato e messo alla fine della coda ready.
- Con $n$ processi in coda ready e time quantum $q$, ogni processo riceve $1/n$ di CPU time in chunk di $q$ unità di tempo.
- Tempi di attesa inferiori a $(n-1)q$ unità di tempo.
  - Es. 5 processi con $q = 20$ millisec prende 20 millisec ogni 100.
- Un timer interrompe ad ogni quanto per schedulare il processo successivo.

**Prestazioni**:
- $q$ largo $\Rightarrow$ FIFO.
- $q$ piccolo $\Rightarrow$ $q$ grande rispetto al context switch altrimenti l’overhead è troppo alto.

## Esempio di RR con Quanto = 4

| Process | Burst Time |
| :--- | :--- |
| $P_1$ | 24 |
| $P_2$ | 3 |
| $P_3$ | 3 |

**Gantt chart**:

| $P_1$ | $P_2$ | $P_3$ | $P_1$ | $P_1$ | $P_1$ | $P_1$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 4 | 7 | 10 | 14 | 18 | 22 | 26 | 30 |

- Tipicamente maggiore turnaround medio di SJF, ma migliore risposta.
- $q$ deve essere grande rispetto al tempo di context switch.
- $q$ di solito tra 10ms e 100ms, context switch < 10 microsec.

## Quanto di Tempo e Tempo di Context Switch

Assumendo un processo di 10 unità di tempo:
- Se il quanto è 12 il processo completa senza context switch.
- Se il quanto è 6 ne occorre uno.
- Se il quanto è 1 ne occorre uno 9.

Se **cs** è 10% del quanto, per ogni quanto si perde 10% di CPU.

## Tempo di Turnaround varia con il Time Quantum

Tempo di turnaround varia con la dimensione del quanto e non incrementa sempre con la dimensione.
- es. 10 unità tempo se 1 q allora 29 turn se 10 q allora 20 turn.
- Dipende dal tempo di completamento dei processi.

| process | time |
| :--- | :--- |
| $P_1$ | 6 |
| $P_2$ | 3 |
| $P_3$ | 1 |
| $P_4$ | 7 |

**Regola empirica**: l’80% dei CPU burst dovrebbero essere più corti di $q$.

## RR con Priorità

Si segue la priorità, processi con pari priorità con RR.

| Process | Burst Time | Priority |
| :--- | :--- | :--- |
| $P_1$ | 4 | 3 |
| $P_2$ | 5 | 2 |
| $P_3$ | 8 | 2 |
| $P_4$ | 7 | 1 |
| $P_5$ | 3 | 3 |

Quantum 2 millisecondi.

## Code Multiple

- Se una sola coda **O(n)** per cercare le priorità.
- Comodo avere code separate per le differenti priorità.
- Assegnazione delle code ai processi:
  - di solito statico e processo rimante in quella coda.
- Ogni coda ha il suo scheduling.

priority = 0
$$T_0 \quad T_1 \quad T_2 \quad T_3 \quad T_4$$

priority = 1
$$T_5 \quad T_6 \quad T_7$$

priority = 2
$$T_8 \quad T_9 \quad T_{10} \quad T_{11}$$

priority = n
$$T_x \quad T_y \quad T_z$$

## Code Multiple

- Si può usare per partizionare processi in base al tipo.
- Es. la Coda Ready partizionata in diverse code, e.g.:
  - foreground (interattiva)
  - background (batch)
- Processi assegnati alle code in modo fisso (non passaggio tra code).
- Ogni coda ha un suo algoritmo di scheduling:
  - foreground – RR
  - background – FCFS

**Scheduling tra code**:
- Scheduling a priorità fissata (i.e., serve tutti dal foreground e poi dal background). Possibilità di starvation.
- Altra possibilità **time-slice tra code** – ogni coda prende un certo quanto di CPU che può schedulare tra i suoi processi.
  - es., 80% ai processi foreground in RR, 20% ai processi in background in FCFS.

## Code Multiple

**Highest priority**:
- system processes
- interactive processes
- interactive editing processes
- batch processes
- student processes

**Lowest priority**

## Code Multiple con Feedback

- Metodi più adattivi.
- Un processo può spostarsi tra le code.
  - Processi I/O bound con priorità più elevata.
  - **Aging** (aumento di priorità nel tempo) per evitare starvation.
- Lo scheduler di code multiple con feedback definito da:
  - Numero di code.
  - Algoritmi di scheduling per ogni coda.
  - Metodi per determinare quando aumentare la priorità di processo.
  - Metodi per determinare quando abbassare la priorità un processo.
  - Metodi per determinare quale coda assegnare ad un processo quando richiede un servizio.
- È lo schedulatore più complesso e flessibile.

## Esempio di Coda Multiple con Feedback

Si considerino tre code:
- $Q_0$ – RR quanto di tempo 8 msec.
- $Q_1$ – RR quanto di tempo 16 msec.
- $Q_2$ – FCFS.

**Scheduling**:
- Prelazione con priorità 0, 1, 2.
- Nuovo processo in Ready messo in coda $Q_0$.
  - Il processo riceve 8 msecs di CPU.
  - Se non finisce in 8 msec, il processo è mosso in coda $Q_1$.
- Se vuota $Q_0$:
  - il primo processo in $Q_1$ riceve 16 msec.
  - Se non completa viene prelazionato e si sposta sulla coda $Q_2$.
- Se vuote $Q_0$ e $Q_1$ vengono eseguiti i processi in coda $Q_2$ con FCFS.
- Schedulatore che dà priorità a processi rapidi e mette in coda quelli più lunghi.

## Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-burst indicato.
Si calcoli il tempo medio di attesa e turnaround **RR quanto = 4**.

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

## Esercizio Scheduling (Passaggio 1)

B

## Esercizio Scheduling (Passaggio 2)

B C D

## Esercizio Scheduling (Passaggio 3)

B C D B E

## Esercizio Scheduling (Passaggio 4)

B C D B E

## Esercizio Scheduling (Passaggio 5)

B C D B E D

## Esercizio Scheduling (Passaggio 6)

A B C D B E D
B C D B E D

## Esercizio Scheduling (Risultati)

| A | B | C | D | B | E | D |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 3 | 7 | 11 | 15 | 17 | 19 | 20 |

$$t_a(RR - 4) = \frac{(3 - 3 - 0) + (17 - 6 - 2) + (11 - 4 - 4) + (20 - 5 - 6) + (19 - 2 - 8)}{5} = 6$$

## Esercizio Scheduling (Turnaround)

$$t_{tr}(RR - 4) = \frac{(3 - 0) + (17 - 2) + (11 - 4) + (20 - 6) + (19 - 8)}{5} = 10$$

## Esercizio Scheduling SJF Preemptive

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e tempo di esecuzione.
Calcolare tempo medio di attesa e turnaround per **SJF preemptive**.

| processo | tempo di arrivo | tempo di esecuzione |
| :--- | :--- | :--- |
| $P_1$ | 0 | 20 |
| $P_2$ | 8 | 5 |
| $P_3$ | 3 | 12 |
| $P_4$ | 10 | 6 |
| $P_5$ | 7 | 8 |

## Esercizio Scheduling SJF Preemptive (Risultati)

$$t_a = \frac{31 + 0 + 11 + 3 + 19}{5} = 12.8 \text{ msec}$$

$$t_{tr} = \frac{51 + 5 + 23 + 9 + 27}{5} = 23 \text{ msec}$$

## Scheduling di Thread

- Distinguere tra thread **user-level** e **kernel-level**.
- Moderni SO schedulano thread kernel-level, non processi.
- Thread user-level gestiti da libreria e kernel non ne è al corrente.
- Per essere eseguiti i thread user-level devono essere mappati in kernel-level.

## Scheduling di Thread (Modelli)

- Per essere eseguiti i thread user-level devono essere mappati in kernel-level.
- Modelli **many-to-one** e **many-to-many**, la libreria dei thread gestisce gli user-level threads per poi lanciare i lightweight processes (LWPs).
- Lo schema è detto **Process-Contention Scope (PCS)**: la competizione per lo CPU è tra thread dello stesso processo.
- Tipicamente scheduling con priorità (definita dal programmatore).
- Per decidere il kernel thread da schedulare in CPU il kernel usa un **System-Contention Scope (SCS)**.
- Competizioni tra tutti i thread nel sistema.
- Sistemi che utilizzano modelli **one-to-one** (Linux, Windows) usano SCS.

## Pthread Scheduling

- API permettono di specificare PCS o SCS durante la creazione dei thread.
- POSIX Pthread permette di specificare entrambe le modalità:
  - `PTHREAD_SCOPE_PROCESS` usa PCS scheduling.
  - `PTHREAD_SCOPE_SYSTEM` usa SCS scheduling.
- Limitato da OS – Linux e Mac OS permettono solo `PTHREAD_SCOPE_SYSTEM`.

## Pthread Scheduling API

```c
#include <pthread.h>
#include <stdio.h>
#define NUM_THREADS 5

int main(int argc, char *argv[]) {
    int i, scope;
    pthread_t tid[NUM_THREADS];
    pthread_attr_t attr;
    /* get the default attributes */
    pthread_attr_init(&attr);
    /* first inquire on the current scope */
    if (pthread_attr_getscope(&attr, &scope) != 0)
        fprintf(stderr, "Unable to get scheduling scope\n");
    else {
        if (scope == PTHREAD_SCOPE_PROCESS)
            printf("PTHREAD_SCOPE_PROCESS");
        else if (scope == PTHREAD_SCOPE_SYSTEM)
            printf("PTHREAD_SCOPE_SYSTEM");
        else
            fprintf(stderr, "Illegal scope value.\n");
    }
}
```

## Pthread Scheduling API (Cont.)

```c
/* set the scheduling algorithm to PCS or SCS */
pthread_attr_setscope(&attr, PTHREAD_SCOPE_SYSTEM);
/* create the threads */
for (i = 0; i < NUM_THREADS; i++)
    pthread_create(&tid[i], &attr, runner, NULL);
/* now join on each thread */
for (i = 0; i < NUM_THREADS; i++)
    pthread_join(tid[i], NULL);
}

/* Each thread will begin control in this function */
void *runner(void *param)
{
    /* do some work ... */
    pthread_exit(0);
}
```

## Scheduling Multi-Processore

- CPU scheduling più complesso se ci sono più CPU.
- Diverse architetture disponibili:
  - Multicore CPU.
  - Multithreaded cores.
  - Sistemi **NUMA**.
  - Multiprocessamento eterogeneo.
- Per i primi tre casi assumiamo processori omogeneri (stesse capacità).

## Scheduling Multi-Processore (Architetture)

- CPU scheduling più complesso se ci sono più processori.
- **Homogeneous processors** – processori identici per funzionalità.
- **Asymmetric multiprocessing** – un solo processore (master) coinvolto nelle decisioni di scheduling e accede alle strutture dati di sistema senza condivisione di dati.
  - Semplifica la gestione, ma il processore server master fa da collo di bottiglia.
- **Symmetric multiprocessing (SMP)** – approccio standard: ogni processore fa self-scheduling.

## Scheduling Multi-Processore (SMP)

- CPU scheduling più complesso se ci sono più CPU.
- **Homogeneous processors** – processori identici per funzionalità.
- **Asymmetric multiprocessing** – un solo processore (master) prende decisioni di scheduling e accede alle strutture dati di sistema senza condivisione di dati. Semplifica la gestione, ma il processore server master fa da collo di bottiglia.
- **Symmetric multiprocessing (SMP)** – approccio standard: ogni processore fa self-scheduling.
  - Tutti i processi in una sola coda ready.
  - Ognuno ha una sua coda privata di processi ready.

![Diagram](image_link)

## Scheduling Multi-Processore (SMP Avanzato)

- CPU scheduling più complesso se ci sono più CPU.
- **Homogeneous processors** – processori identici per funzionalità.
- **Asymmetric multiprocessing** – un solo processore (master) prende decisioni di scheduling e accede alle strutture dati di sistema senza condivisione di dati. Semplifica la gestione, ma il processore server master fa da collo di bottiglia.
- **Symmetric multiprocessing (SMP)** – approccio standard: ogni processore fa self-scheduling.
  - Tutti i processi in una coda ready oppure ogniuno ha una sua coda privata di processi ready.
  - Attualmente la soluzione più commune/standard in SMP sono le **code private**.
  - Tutti i sistemi supportano SMP (Linux, Windows, MacOS, Android, etc.).

## Scheduling Multi-Processore (Multicore)

- Sistemi multicore.
- Ogni core è per il SO una CPU separata.
- Core veloci, ma problemi di **memory stall** (attesa di dati pronti in memoria).
- Più thread pronti per core: **chip multithreading (CMT)**.

## Scheduling Multi-Processore (Hyperthreading)

- Sistemi multicore.
- Ogni core appare al SO come una CPU separata.
- Core veloci, ma problemi di **memory stall** (attesa di dati pronti in memoria).
- Più thread pronti per core: chip multithreading (CMT).
- Per OS è come avere più CPU (Intel chiama **hyperthreading**).
- Es. Oracle Spark M7: 8 thread per core su 8 core, come 64 CPU.
- Due livelli di scheduling:
  - Software threads (SO).
  - Hardware threads.

## Multiple-Processor Scheduling – Load Balancing

Se Symmetric Multiprocessing (SMP) e code private:
- **Load balancing**: necessario bilanciare il carico tra i processori.

Due metodi di Load balancing:
- **Push migration** – un processo verifica continuamente il carico dei processori, se trova uno sbilanciamento sposta/spinge il task dalla CPU sovraccarica alle altre.
- **Pull migration** – i processori in idle prendono/tirano i task in attesa sulle code dei processori occupati.
- Esempio: Linux implementa entrambe le strategie.

**Processor affinity** – processo ha affinità per il processore su cui è in running.
- **soft affinity** – tentativo di mantenere il processore del thread.
- **hard affinity** – specifica il sottoinsieme di processori per il thread.
- Esempio: Linux implementa soft, ma supporta entrambi.
- Con code private per core più semplice affinity.

## NUMA e CPU Scheduling

**Non-uniform Memory Access (NUMA)**
- Due chip con la propria CPU e memoria.
- Accessi in memoria a velocità diversa.
- C’è un conflitto tra problematiche di accesso in memoria e load balancing.
- Spostando i thread dai core di riferimento si rallenta l’accesso ai dati.

Gli algoritmi di **memory-placement** possono considerare l’affinity.

## Heterogeneous Multiprocessing

- Alcuni sistemi hanno architetture multicore non omogenee.
  - Diverso clock, diverso consumo di energia, etc.
  - Non asimmetrici (perché core omogenei per capacità di calcolo).
  - Ma diversi consumi: **Big core** e **Little core** (processori ARM).
    - Big core veloci ma consumano.
    - Little core lenti ma economici.
    - Vantaggio per sistemi mobile.
    - Algoritmi di scheduling finalizzati al risparmio di energia.

## Real-Time CPU Scheduling

- **Sistemi Real-Time**.
- **Soft real-time system**:
  - non garanzie su quando un processo verrà schedulato, solo processi critici preferiti a non critici.
- **Hard real-time system**:
  - task servito prima di una deadline.
- **Latenza di un evento**:
  - Tempo trascorso tra evento e risposta del sistema.

## Real-Time CPU Scheduling (Latenze)

- **Sistemi Real-Time**.
- **Soft real-time system**:
  - non garanzie su quando un processo verrà schedulato, solo processi critici preferiti a non critici.
- **Hard real-time system**:
  - task servito prima di una deadline.

Due tipi di latenze incidono sulla prestazione:
1. **Interrupt latency** – tempo dall’arrivo dell’interrupt allo start della routine di servizio.
2. **Dispatch latency** – tempo di scheduling per fare lo switch di un altro processo.

Durante gli update delle strutture del kernel gli interrupt sono disabilitati; in sistemi real time, va minimizzato questo tempo.

## Real-Time CPU Scheduling (Dispatch Latency)

- **Dispatch latency**: fase di conflitto e fase di dispatch del processo.
- Fase di gestione del **conflitto** durante la dispatch latency:
  1. Prelazione di qualunque processo in kernel mode.
  2. Rilascio delle risorse occupate dai processi a bassa priorità quando richieste dai processi ad alta priorità.

Reattività richiede **preemptive kernel**.

**Latenza relativa al dispatch**: periodo di tempo necessario al dispatcher per bloccare un processo e avviarne un altro.
- Diversi microsecondi per la gestione, i sistemi real-time devono gestire.

## Priority-based Scheduling

- Nel real-time scheduling lo scheduler deve supportare prelazione e priority-based scheduling.
  - Es. Windows ha 32 livelli di priorità con i livelli da 16 a 31 per i processi real-time.
  - Ma questo garantisce solo il soft real-time.
- Per hard real-time deve anche garantire le **deadline**.
  - Servono altri meccanismi ed altre politiche di schedulazione.

## Priority-based Scheduling (Task Periodici)

- Nel real-time scheduling lo scheduler deve supportare preemptive e priority-based scheduling.
  - Ma questo garantisce solo il soft real-time.
- Per hard real-time deve anche garantire le deadlines.
- Consideriamo task periodici.
  - Richiedono la CPU a intervalli costanti.
  - Ottenuta la CPU ha un tempo di processo $t$, deadline $d$, e periodo $p$.
  - $0 \leq t \leq d \leq p$.
  - Rate di un task periodico $1/p$.

## Priority-based Scheduling (Admission Control)

- Nel real-time scheduling lo scheduler deve supportare preemptive e priority-based scheduling.
  - Ma questo garantisce solo il soft real-time.
- Per hard real-time deve anche garantire le deadlines.
- Consideriamo task periodici.
  - Richiedono la CPU a intervalli costanti.
  - Ottenuta la CPU ha un tempo di processo $t$, deadline $d$, e periodo $p$.
  - $0 \leq t \leq d \leq p$.
  - Rate di un task periodico $1/p$.
- **Admission control algorithm**: il processo dichiara una deadline, lo scheduler può ammettere il processo garantendo il rispetto della deadline oppure non ammettere.

## Rate Monotonic Scheduling

- Priorità assegnata in base all’**inverso del periodo**.
  - Periodi brevi = priorità alta.
  - Periodi lunghi = priorità bassa.
  - Priorità alta a chi interviene più spesso.
- Ogni processo mantiene lo stesso CPU burst.

**Esempio**:
- Periodi 50 e 100, tempo di processamento rispettivamente 20 e 35.
- Deadline: terminare prima del prossimo periodo.
- Uso CPU per $P_1$ è 20/50 = 0.4, per $P_2$ è 35/100 = 0.35, tot 0.75.
- Assumendo $P_2$ con priorità più alta di $P_1$ deadline persa per $P_1$.

## Rate Monotonic Scheduling (Esempio Corretto)

- Priorità assegnata in base all’inverso del periodo.
- Periodi brevi = priorità alta.
- Periodi lunghi = priorità bassa.
- Esempio:
  - Periodi 50 e 100, tempo di processamento 20, 35.
  - Deadline: terminare prima del prossimo periodo.
  - Uso CPU per $P_1$ è 20/50 = 0.4, per $P_2$ è 35/100 = 0.35, tot 0.75.
- Assumendo **RMS**:
  - $P_1$ con priorità più alta di $P_2$ entrambe le deadline rispettate.

## Deadline persa con il Rate Monotonic Scheduling

- Consideriamo un caso in cui non si riesce a schedulare.
  - Se $P_1$ ha periodo 50 e CPU burst 25 e $P_2$ periodo 80 e CPU burst 35.
  - Utilizzo CPU 25/50 + 35/80 = 0.94.
  - $P_2$ interrotta da $P_1$ quando riprende finisce a 85, ma doveva finire ad 80.

- Non sfrutta completamente la CPU, l’utilizzo diminuisce con il numero di processi.
$$N(2^{1/N} - 1)$$
- Con 1 processo 100%, con 2 processi 83%, con al crescere di N 69%.

## Earliest Deadline First Scheduling (EDF)

- Priorità sono assegnate secondo le **deadline**:
  - prima la deadline, più alta è la priorità.
  - più lontana è la deadline, più bassa è la priorità.
  - Le priorità non sono fisse, variano nel tempo.

P1: p1 = 50, t1 = 25; P2: p2 = 80, t2= 35.

- Non richiede la periodicità dei processi e neppure CPU burst costante.
- Ogni processo deve dichiarare la deadline quando diventa runnable.
- Teoricamente ottimo (se utilizzo sotto 100% di CPU rispetta la deadline) però va considerate il context switch e il costo della gestione dell’interrupt.

## Earliest Deadline First Scheduling (EDF) (Esempio)

- Priorità sono assegnate secondo le deadline.
- Esempio:
  - Tracciare il Gantt secondo EDF verificando se le scadenze sono rispettate (scheduling ammissibile).

| Processo | Tempo di arrivo | Esecuzione | Scadenza |
| :--- | :--- | :--- | :--- |
| $J_1$ | 0 | 3 | 16 |
| $J_2$ | 2 | 1 | 7 |
| $J_3$ | 0 | 6 | 8 |
| $J_4$ | 8 | 2 | 11 |
| $J_5$ | 13 | 3 | 18 |

## Earliest Deadline First Scheduling (EDF) (Ripetizione)

- Priorità sono assegnate secondo le deadline.
- Esempio:
  - Tracciare il Gantt secondo EDF verificando se le scadenze sono rispettate (scheduling ammissibile).

| Processo | Tempo di arrivo | Esecuzione | Scadenza |
| :--- | :--- | :--- | :--- |
| $J_1$ | 0 | 3 | 16 |
| $J_2$ | 2 | 1 | 7 |
| $J_3$ | 0 | 6 | 8 |
| $J_4$ | 8 | 2 | 11 |
| $J_5$ | 13 | 3 | 18 |

## Earliest Deadline First Scheduling (EDF) (Dettagli)

- Priorità sono assegnate secondo le deadline:
  - prima la deadline, più alta è la priorità.
  - più lontana è la deadline, più bassa è la priorità (le priorità non sono fisse, variano nel tempo).

Non richiede la periodicità dei processi e neppure CPU burst costante.
Ogni processo deve dichiarare la deadline quando diventa runnable.

Teoricamente ottimo (se utilizzo sotto 100% di CPU rispetta la deadline) però va considerate il context switch e il costo della gestione dell’interrupt.

Se un insieme di processi caratterizzati da: tempo di arrivo, un requisito di esecuzione, scadenza può essere schedulata (da un algoritmo) in modo da garantire tutte le scadenze, l'EDF garantirà la scadenza.

## Earliest Deadline First Scheduling (EDF) (Attenzione)

- Priorità sono assegnate secondo le deadline:
  - prima la deadline, più alta è la priorità.
  - più lontana è la deadline, più bassa è la priorità (le priorità non sono fisse, variano nel tempo).

**Attenzione**: si è assunto deadline = periodo.
Se la deadline è prevista prima del periodo non garantisce.

Es. T0(5,13,20), T1(3,7,11), T2(4,6,10), T3(1,1,20).
Utilizzo 5/20+3/11+4/10+1/20 = 0.97.

| TaskNo(computation time, relative deadline, period) |
|-----------------------------------------------|
| T0(5,13,20) |
| T1(3,7,11) |
| T2(4,6,10) |
| T3(1,1,20) |

**EDF Scheduling**
CPU unit time index 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

## Scheduling a Quote Proporzionali

- Quote proporzionali di CPU preallocate per le applicazioni.
- $T$ quote di CPU devono essere preallocate tra tutti i processi.
- Un’applicazione riceve $N$ quote con $N < T$.
  - L’algoritmo assicura l’applicazione riceverà $N / T$ del tempo totale del processore.

- Esempio $T = 100$ da dividere su A, B, C. A che riceve 50, B riceve 15, e C riceve 20. Rimangono quote per altri processi.
- Algoritmo di admission control assegna le quote rimanenti ai nuovi processi nel rispetto delle quote già assegnate.

## POSIX Real-Time Scheduling

POSIX.1b fornisce API standard per gestire real-time threads.
Definisce due classi di scheduling per real-time threads:

1. **SCHED_FIFO** - threads sono schedulati con strategia FCFS con coda FIFO. No time-slicing per thread con priorità uguale.
2. **SCHED_RR** - simile a SCHED_FIFO ma con time-slicing per thread di pari priorità.

Definisce due funzioni per prendere e settare la politica di scheduling:
1. `pthread_attr_getsched_policy(pthread_attr_t *attr, int *policy)`
2. `pthread_attr_setsched_policy(pthread_attr_t *attr, int policy)`

## POSIX Real-Time Scheduling API

```c
#include <pthread.h>
#include <stdio.h>
#define NUM_THREADS 5
int main(int argc, char *argv[])
{
    int i, policy;
    pthread_t tid[NUM_THREADS];
    pthread_attr_t attr;
    /* get the default attributes */
    pthread_attr_init(&attr);
    /* get the current scheduling policy */
    if (pthread_attr_getschedpolicy(&attr, &policy) != 0)
        fprintf(stderr, "Unable to get policy.\n");
    else {
        if (policy == SCHED_OTHER) printf("SCHED_OTHER\n");
        else if (policy == SCHED_RR) printf("SCHED_RR\n");
        else if (policy == SCHED_FIFO) printf("SCHED_FIFO\n");
    }
}
```

## POSIX Real-Time Scheduling API (Cont.)

```c
/* set the scheduling policy - FIFO, RR, or OTHER */
if (pthread_attr_setschedpolicy(&attr, SCHED_FIFO) != 0)
    fprintf(stderr, "Unable to set policy.\n");

/* create the threads */
for (i = 0; i < NUM_THREADS; i++)
    pthread_create(&tid[i], &attr, runner, NULL);

/* now join on each thread */
for (i = 0; i < NUM_THREADS; i++)
    pthread_join(tid[i], NULL);
}

/* Each thread will begin control in this function */
void *runner(void *param)
{
    /* do some work ... */
    pthread_exit(0);
}
```

## Hard real-time

Il POSIX 1b supportato a partire da kernel Linux (dal 2.6) fornendo schedulazione con priorità, supporto per segnali, sincronizzazione etc.

Per avere garanzie hard-real time occorre un kernel adatto:
**Real-Time Operating System (RTOS)**.

Es. In Linux **PREEMPT_RT Kernel** (patch).
Altri approcci basati su cokernel (es., RTLinux, Xenomai, RTAI).

## Virtualizzazione e Scheduling

- Con Virtualizzazione si schedula con SO ospiti multipli sulla CPU(s).
- Ogni ospite esegue il suo scheduling.
  - Ma in realtà non ha una sua CPU e sta schedulando pensando di avere l’intera CPU.
  - Può portare a risposte rallentate.
  - Lo stesso clock del Sistema può essere rallentato.
- Si possono perdere i benefici di un buon algoritmo di scheduling implementato sul SO ospite.

## Esempi di SO

- Linux scheduling.
- Windows scheduling.

## Scheduling Linux prima della versione 2.5

□ Prima della versione kernel 2.5 variazione dell’algoritmo di scheduling standard di UNIX.

□ Linux v1.2
  - Unica lista contenente tutti i processi attivati sulla macchina.
    ► Il primo elemento della lista è la task_struct di init.
  - Ogni processo ha una priorità statica (**nice value** o **nice**).
  - La priorità varia da -20 (priorità più alta) a +19 (priorità più bassa).
  - Il valore di default è 10.
  - Schema classico delle priorità in UNIX.
  - Scheduling in modalità “**round robin pesato**”.
    ► Un processo in attesa da più tempo viene favorito rispetto ad un processo che attende da meno tempo.
    ► A parità di attesa, un processo a priorità più alta viene favorito rispetto ad un processo a priorità più bassa.
    ► Ad ogni invocazione dello schedule, la lista è scandita ed i contatori aggiornati, si sceglie il processo per cui il contatore è massimo.

## Scheduling Linux prima della versione 2.5 (v2.2)

- Prima della versione kernel 2.5 variazione dell’algoritmo di scheduling standard di UNIX.
- Linux v2.2
  - Classi priorità multipla.
  - Priority-based e time-sharing.
  - Prelazione con priorità.
  - Funzione `goodness()` ritorna un peso (**weight**) nell’intervallo [-1000, 1000].
    - Dipende dalla priorità e dai tempi di esecuzione.
  - Il peso è usato per scegliere il processo da schedulare.
    - Selezione basata su Priorità con RR (se stessa goodness).
  - Si usano 140 livelli di priorità.
    - Livelli [0, 99]: usati da algoritmi di scheduling di tipo soft real time (SCHED_FIFO, SCHED_RR), che hanno sempre la precedenza sull’algoritmo standard.
    - Livelli [100, 139]: corrispondono all’intervallo [-20, 19] (SCHED_OTHER) e sono utilizzati dall’algoritmo di scheduling di default (round robin pesato).

## Linux Real-Time Scheduling

- Real-time scheduling in POSIX.1b con SCHED_FIFO o SCHED_RR.
- Task real-time assegnati a priorità statiche tra 0 e 99.
- Real-time hanno valori più bassi di quelli dei task normali e sono mappati in uno schema di priorità globale.

- Priority:
  - Higher
  - Lower

- Le priorità relative dei processi real-time sono assicurate.
- Il kernel non fornisce garanzia sui tempi di attesa dei processi pronti.
- Se interruzione per real-time arriva mentre il kernel serve una chiamata di sistema, il processo real-time deve attendere.

## Scheduling Linux prima della versione 2.5 (v2.2 - O(n))

- Prima della versione kernel 2.5 variazione dell’algoritmo di scheduling standard di UNIX.
- Classi priorità gestite con RR pesato.
  - Priority-based e time-sharing.
  - Prelazione con priorità.
  - Priorità assegnata sulla base di una funzione `goodness()` ritorna un peso (weight) nell'intervallo [-1000, 1000].
  - Il peso è usato per scegliere il processo da schedulare.
  - Uso di quanti di tempo variabili (**time slice**).
  - L'algoritmo di scheduling è **O(n)** rispetto al numero di processi.
- Tempo O(n) per selezionare il processo, dipende dal numero di processi.
- Metodo non flessibile (lista unica) e poco adatto a Symmetric Multiprocessing (SMP).

## Scheduling Linux prima della versione 2.5 (v2.4)

- Prima della versione kernel 2.5 variazione dell’algoritmo di scheduling standard di UNIX.
- Lo scheduler del kernel v2.4 è una estensione del Kernel v2.2.
  - Uso di quanti di tempo variabili (time slice) dipendente dalla priorità.
  - Uso di un sistema di **schedulazione a crediti**.
  - Sistema a crediti: un credito 10ms di esecuzione. Un credito ogni volta che si blocca. Dopo l'esecuzione di un time slice si scala un credito. No credit no CPU.
  - Quando tutti i processi in stato RUNNING hanno esaurito i crediti, il kernel ricalcola il credito per tutti i processi (**recrediting**).
  - L'algoritmo di scheduling è O(n) rispetto al numero di processi (unica lista).
- Il tempo per la selezione del processo migliore dipende dal numero di processi.
- Migliorato ma non ok per SMP.

## Scheduling Linux versione 2.5

Con la versione 2.5 si propone uno scheduler che lavora a tempo costante **O(1)** indipendente dal numero di task nel sistema:

- Preemptive e priority based.
- Due intervalli di priorità: processi time-sharing (detti nice) e real-time.
- Real-time da 0 a 99 e valori nice da 100 a 140.
- Si mappano in priorità globali con valori bassi che indicano alta priorità.
- Priorità più alte prendono time-slice q maggiori.

$$base \ time \ quantum \ (in \ milliseconds) = \begin{cases} (140 - static \ priority) \times 20 & \text{if } static \ priority < 120 \\ (140 - static \ priority) \times 5 & \text{if } static \ priority \ge 120 \end{cases}$$

| Description | Static priority | Nice value | Base time quantum |
| :--- | :--- | :--- | :--- |
| Highest static priority | 100 | −20 | 800 ms |
| High static priority | 110 | −10 | 600 ms |
| Default static priority | 120 | 0 | 100 ms |
| Low static priority | 130 | +10 | 50 ms |
| Lowest static priority | 139 | +19 | 5 ms |

## Scheduling Linux versione 2.5 (Dettagli)

Con la versione 2.5 si propone uno scheduler che lavora a tempo costante O(1) indipendente dal numero di task nel sistema:

- Preemptive e priority based.
- Due intervalli di priorità: processi time-sharing (detti nice) e real-time.
- Real-time da 0 a 99 e valori nice da 100 a 140.
- Si mappano in priorità globali con valori bassi che indicano alta priorità.
- Priorità più alte prendono time-slice q maggiori.
- **Non goodness**.
- I task sono in esecuzione finché hanno il time slice (**active**).
- Quando scade non vanno in esecuzione finché tutti gli altri tasks non usano lo slice.
- Tutti i task eseguibili tracciati con code separate:
  - Due array di priorità (**active**, **expired**).
  - Task indicizzati con la priorità.
  - Finiti gli attivi, gli array sono scambiati con expired (veloce scambio).
  - Scambio tempo costante, ma anche ricerca della priorità.

## Scheduling Linux versione 2.5 (Efficienza)

Con la versione 2.5 si propone uno scheduler che lavora a tempo costante O(1) indipendente dal numero di task nel sistema:

- Preemptive e priority based.
- Due intervalli di priorità: processi time-sharing (detti nice) e real-time.
- Real-time da 0 a 99 e valori nice da 100 a 140.
- Si mappano in priorità globali con valori bassi che indicano alta priorità.
- Priorità più alte prendono time-slice q maggiori.
- I task sono in esecuzione finché hanno il time slice (active).
- Quando scade non vanno in esecuzione finché tutti gli altri tasks non usano lo slice.
- Tutti i task eseguibili tracciati con code separate **per-CPU**.
  - Due array di priorità (active, expired).
  - Task indicizzati con la priorità.
  - Finiti gli attivi, gli array sono scambiati con expired (veloce scambio).
  - Scambio tempo costante, ma anche ricerca della priorità.
- Buon funzionamento con SMP, ma tempi di risposta non soddisfacenti per processi interattivi.

## Linux Scheduling in Versione 2.6.23 +

**Completely Fair Scheduler (CFS)**
- Classi di scheduling, altre possono essere aggiunte:
  1. Default (CFS scheduling).
  2. Real-time (real-time scheduling).

**Latenza target**:
- Intervallo di tempo durante il quale un task deve andare in run almeno una volta.

**Fairness**:
- se N processi uguali su latenza target T, ogni processo deve prendere T / N.
- Assumiamo latenza target = 4 e processi con CPU burst 8, 4, 16, 4.
- Con coda T1, T2, T3, T4 tutti eseguono 1 ms per 4 cicli … poi T2 e T4 finiscono.
- Rimane coda T1 e T3 che si dividono 2 ms per 2 cicli … poi T1 finisce.
- T3 rimane solo che fa 2 cicli da 4 ms … e conclude.

## Linux Scheduling in Versione 2.6.23 + (Dettagli CFS)

**Completely Fair Scheduler (CFS)**
- Classi di scheduling, altre possono essere aggiunte:
  1. Default (CFS scheduling).
  2. Real-time (real-time scheduling).

**Latenza target**:
- Intervallo di tempo durante il quale un task deve andare in run almeno una volta.

**Fairness**:
- se N processi uguali su latenza target T, ogni processo deve prendere T / N.

**Priorità**:
- Allocazione basata su proporzione di CPU time pesata sul peso del task.
- Se N task time_slice(task) = (target_latency / N) * task_weight.
  - Granularità minima, es. time_slice_min = 1 ms.

**Vruntime**:
- Il tempo scorre in modo diverso a seconda del processo in esecuzione.

**Criterio di schedulazione**:
- Ad ogni invocazione selezionato il task con il **vruntime più basso**.

## The Linux CFS scheduler (Tecnica)

The Linux CFS scheduler provides an efficient algorithm for selecting which task to run next. Each runnable task is placed in a **red-black tree**—a balanced binary search tree whose key is based on the value of `vruntime`. This tree is shown below:

![Diagram of the Linux CFS scheduler tree](image)

When a task becomes runnable, it is added to the tree. If a task on the tree is not runnable (for example, if it is blocked while waiting for I/O), it is removed. Generally speaking, tasks that have been given less processing time (**smaller values of `vruntime`**) are toward the left side of the tree, and tasks that have been given more processing time are on the right side. 

According to the properties of a binary search tree, the leftmost node has the smallest key value, which for the sake of the CFS scheduler means that it is the task with the highest priority. Because the red-black tree is balanced, navigating it to discover the leftmost node will require $O(\lg N)$ operations (where $N$ is the number of nodes in the tree). However, for efficiency reasons, the Linux scheduler caches this value in the variable `rb_leftmost`, and thus determining which task to run next requires only retrieving the cached value.

## Linux Scheduling (Bilanciamento)

- Scheduler CFS supporta bilanciamento del carico, riduce al minimo migrazione dei thread.
- Il carico del thread è dato da una combinazione di priorità e tasso medio di utilizzo della CPU.
  - Carico basso, ma alta priorità simile a carico alto e bassa priorità.
  - Dalla somma dei load si ha il carico della coda che si può ribilanciare.
- **Domini di scheduling** per ridurre il costo del bilanciamento.
  - Bilanciamento prima nel dominio più prossimo.

## Linux Scheduling in Versione 6.6

**Earliest Eligible Virtual Deadline First (EEVDF)** scheduler (November 2023).
- Fair + deadline virtuali.
- EEVDF come CFS cerca anche di ottenere un corretto uso della CPU time tra i task.
- EEVDF scheduler cerca un “**eligible task**” con la virtual deadline più vicina.

EEVDF introduce due nozioni: **eligibility** e **lag** di un task.
- EEVDF gestisce il CPU time per un task sulla base di una priorità statica (nice).
- Ogni task ha un virtual run time.
- Il **lag** di un task è il gap tra il CPU time ideale e quello effettivo CPU per il task.
  - Lag positivo = poco CPU time allocato.
  - Lag negativo = troppo CPU time allocato (violazione dell’uso corretto di CPU time).
- Tasks con lag positive sono eligible (mantiene correttezza).

- EEVDF seleziona i tasks con lag positivo e calcola una virtual deadline (VD) per ognuno selezionando il task con la VD più vicina per la prossima esecuzione.

- Se CFS è orientato alla fairness pesata su priorità, EEVDF è orientato alla **reattività pesata** considerando priorità e deadline.

## Linux Scheduling in Versione 6.6 (Esempio)

□ Earliest Eligible Virtual Deadline First (EEVDF) scheduler (November 2023).
□ Fair + deadline virtuali.
□ EEVDF come CFS cerca anche di ottenere un corretto uso della CPU time tra i task.
□ EEVDF scheduler cerca un “eligible task” con la virtual deadline più vicina.

EEVDF introduce due nozioni: eligibility e lag di un task.

**Esempio**:
- Assumiamo T1, T2, T3 con uguali priorità e lag iniziale 0.
- Se T1 viene schedulato per primo con 30 ms.
- Su 30 ms, l’allocazione equa sarebbe stata 10, 10, 10 (T1 quindi ha debito, T2 e T3 sono in credito) … dunque lag T1 = -20, lag T2 = 10, lag T3 = 10.
- Ora T1 non è più eligible, se lo scheduler assegna poi a T2 30 ms, dopo l’esecuzione i lag diventano T1 = -10, T2 = -10, T3 = 20.
- Rimane quindi solo T3 eligible.

## Linux Scheduling in Versione 6.6 (Formule)

□ Earliest Eligible Virtual Deadline First (EEVDF) scheduler (November 2023).
□ Fair + deadline virtuali.
□ EEVDF come CFS cerca anche di ottenere un corretto uso della CPU time tra i task.
□ EEVDF scheduler cerca un “eligible task” con la virtual deadline più vicina.

□ Per ogni processo il **virtual_run_time** scorre più o meno lento a seconda del peso del processo che è in esecuzione (veloce bassa priorità, lento alta).
  - $V(t)=V(t_{prec})+ \frac{\Delta t}{w_i}$
  - (dove $w_i$ è il peso del task i-esimo rispetto al peso totale dei processi in coda).

□ Ogni volta che lo scheduler è invocato la virtual deadline è aggiornata per tutti i processi in coda:
  - anche questa è calcolata pesando il tempo richiesto $C_i$ per la computazione dal task i-esimo.
  - **$\text{VD} = V(t) + \frac{C_i}{w_i}$**
  - Se esiste un task con VD minore della corrente questo prelazione il precedente.

## Windows Scheduling

- Windows usa uno schema **priority-based preemptive scheduling**.
  - Il thread a più alta priorità deve essere eseguito.
- La parte del Kernel che si occupa di scheduling è chiamata **Dispatcher**.
- Thread eseguono fino al (1) blocco, (2) fine del time slice, (3) prelazionato da un thread a priorità più alta.
- I thread real-time possono prelazionare i non-real-time.
- 32-livelli di schema di priorità.
- Code di thread per ogni priorità:
  - Lo scheduler cerca i thread in ogni coda.
  - Se non trova un runnable thread, allora lancia il thread idle.

## Windows Priority Classes

- Relazione tra le priorità nel Kernel e le priorità nelle API.
- Win32 API identifica molte classi di priorità per i processi:
  - REALTIME_PRIORITY_CLASS, HIGH_PRIORITY_CLASS, ABOVE_NORMAL_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, IDLE_PRIORITY_CLASS.
  - Tutte modificabili eccetto REALTIME (funzione `SetPriorityClass()`).
- Un thread in una priority class ha una priorità relativa:
  - TIME_CRITICAL, HIGHEST, ABOVE_NORMAL, NORMAL, BELOW_NORMAL, LOWEST, IDLE.
- Priority class e relative priority si combinano per formare una priorità numerica.
- La priorità di base è NORMAL per la classe di appartenenza:
  - REALTIME_PRIORITY_CLASS — 24
  - HIGH_PRIORITY_CLASS — 13
  - ABOVE_NORMAL_PRIORITY_CLASS — 10
  - NORMAL_PRIORITY_CLASS — 8
- Se il quantum si esaurisce la priorità si abbassa, ma mai sotto la base.

## Windows Priorities

| | real-time | high | above normal | normal | below normal | idle priority |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| time-critical | 31 | 15 | 15 | 15 | 15 | 15 |
| highest | 26 | 15 | 12 | 10 | 8 | 6 |
| above normal | 25 | 14 | 11 | 9 | 7 | 5 |
| normal | 24 | 13 | 10 | 8 | 6 | 4 |
| below normal | 23 | 12 | 9 | 7 | 5 | 3 |
| lowest | 22 | 11 | 8 | 6 | 4 | 2 |
| idle | 16 | 1 | 1 | 1 | 1 | 1 |

## Windows Priority Classes (Dettagli)

- Se il thread esce dal wait la priorità viene aggiornata a seconda di cosa si attendeva:
  - Es. I/O favorito, memoria meno.
- Nel NORMAL_PRIORITY CLASS favoriti processi interattivi.
  - Processi in foreground hanno un **3x boost** di priorità rispetto a quelli in background.
- Gestione dello scheduling su multiprocessori utilizzando processori logici organizzati in insiemi (**SMT-set**).
  - Il SO cerca di mantenere un processore ideale per un task.

## Valutazione Algoritmi

- Come selezionare algoritmi di CPU-scheduling per un SO?
- Determinare un criterio, poi valutare gli algoritmi.

- **Esempio 1**: massimizzare l’utilizzo della CPU, con tempo massimo di risposta inferiore a 300 millisecondi.
- **Esempio 2**: massimizzare la produttività, con tempo di completamento proporzionale (in media) al tempo di esecuzione effettivo.