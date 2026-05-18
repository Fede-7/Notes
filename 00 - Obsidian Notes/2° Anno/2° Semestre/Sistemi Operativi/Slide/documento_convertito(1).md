## Pagina 1

Lezione 8: Scheduling CPU

---

## Pagina 2

Obiettivi

- Introdurre il concetto dello scheduling CPU
- Descrivere algoritmi di scheduling di CPU
- Discutere criteri di valutazione degli algoritmi di scheduling
- Esaminare algoritmi di scheduling algorithms di vari SO

---

## Pagina 3

Concetti di Base

- Massimo utilizzo di CPU con multiprogramming
- Un programma non usa sempre la CPU continuamente. A volte calcola… a volte aspetta qualcosa (disco, input, rete)
- Cicli CPU–I/O Burst – L’esecuzione dei processi consiste di cicli di esecuzione CPU e attese I/O
- CPU burst seguiti da I/O burst
- Distribuzione di CPU burst è una problematica importante

---

## Pagina 4

Istogramma dei tempi di CPU-burst

Se misuriamo i CPU burst nei sistemi reali, otteniamo qualcosa del genere ...

I sistemi reali hanno tanti processi che fanno piccoli lavori e pochi che fanno lavori lunghi

---

## Pagina 5

CPU Scheduler

□ Short-term scheduler seleziona tra processi nella coda ready e alloca la CPU a uno di loro
□ Le code possono essere ordinate in modi diversi

□ Le decisioni di CPU scheduling occorrono quando i processi:
1. Passano dallo stato running a waiting (es. I/O req o wait)
2. Passano dallo stato running a ready (es. interrupt)
3. Passano da waiting a ready (es. I/O completo)
4. Terminano (es. terminazione)

□ In situazioni 1 e 4 processo cede il controllo (non prelazione)

□ Schemi senza prelazione (nonpreemptive) o con prelazione (preemptive)
□ Scheduling senza prelazione (processo in esecuzione fino a fine o wait)
□ Scheduling con prelazione
  □ Problema accesso a dati condivisi (race condition)
  □ Problema prelazione in modalità kernel (operazioni non interrompibili)
  □ Problema interruzioni durante attività curciali (sezioni critiche)

---

## Pagina 6

Dispatcher

- Dispatcher dalla controllo della CPU ai processi selezionati dallo short-term scheduler e richiede:
  - switching del contesto
  - switching allo user mode
  - salto alla corretta locazione del programma utente per ripartire con quel programma

- Latenza di dispatch – tempo necessario al dispatcher per fermare un processo e mandarne un altro in running
  - Più breve possible

- Context switch:
  ```asm
    vmstat 1 3
    cpu ----
    24
    225
    339
  ```

in: The number of interrupts per second, including the clock.
cs: The number of context switches per second.

---

## Pagina 7

Criteri di Scheduling

□ Utilizzo CPU – percentuale di CPU utilizzata; occorre mantenere la CPU occupata (top command).

□ Throughput – numero di processi che completano l’esecuzione per unità di tempo

□ Turnaround time – tempo di completamento di processo
  □ tempo totale per eseguire un processo
  □ accesso memoria + coda ready + CPU + I/O

□ Waiting time – tempo di attesa per un processo nella coda ready

□ Response time – tempo che intercorre tra una richiesta e la prima risposta
  □ Importante per sistemi interattivi, quando l’elaborazione continua dopo un output
  □ Alternativa al tempo di tournaround che prevede l’esecuzione completa

---

## Pagina 8

Scheduling: Criteri di Ottimizzazione

- Massimo utilizzo CPU
- Massimo throughput
- Minimo tempo di turnaround
- Minimo tempo di waiting
- Minimo tempo di risposta

- In molti sistemi (desktop, laptop) è più importante minimizzare la varianzia dei tempi di risposta che il tempo medio

---

## Pagina 9

First- Come, First-Served (FCFS) Scheduling

| Process | Burst Time |
| :--- | :--- |
| $P_1$ | 24 |
| $P_2$ | 3 |
| $P_3$ | 3 |

Assumendo che i processi nell’ordine: $P_1, P_2, P_3$
Il Gantt Chart dello schedule è:

| $P_1$ | $P_2$ | $P_3$ |
| :--- | :--- | :--- |

Tempi di attesa per $P_1 = 0; P_2 = 24; P_3 = 27$
Media del tempo di attesa: $(0 + 24 + 27)/3 = 17$

---

## Pagina 10

FCFS Scheduling

Assumendo i processi nell’ordine:

$$P_2, P_3, P_1$$

□ Il Gantt diventa:

$$\begin{array}{c|c|c}
P_2 & P_3 & P_1 \\
\hline
0 & 3 & 6 \\
\end{array}$$

□ Tempi di attesa $P_1 = 6; P_2 = 0; P_3 = 3$
□ Tempo di attesa medio: $(6 + 0 + 3)/3 = 3$
□ Molto meglio di prima
□ Effetto Convoy - processi brevi dietro i processi lunghi
  □ Considera un processo CPU-bound e tanti I/O-bound
□ Sbrigare i processi brevi per migliorare i tempi di risposta

---

## Pagina 11

Shortest-Job-First (SJF) Scheduling

- Associa ad ogni processo la lunghezza del prossimo CPU burst
  - Lunghezza usata per schedulare il processo con brust più breve

- SJF è ottimale – minima attesa media per un insieme di processi
  - Difficile conoscere la lunghezza della prossima richiesta di CPU
  - Soluzione: uso di stime basate sul comportamento passato ed esecuzione del processo con il minor tempo di esecuzione stimato

- Algoritmo particolarmente indicato per l'esecuzione batch dei job per i quali i tempi di esecuzione sono conosciuti a priori

- Lo scheduler dovrebbe utilizzare questo algoritmo quando nella coda di input risiedono job di uguale importanza

---

## Pagina 12

Esempio di SJF

| Process | Burst Time |
| :--- | :--- |
| $P_1$ | 6 |
| $P_2$ | 8 |
| $P_3$ | 7 |
| $P_4$ | 3 |

□ SJF scheduling chart

| $P_4$ | $P_1$ | $P_3$ | $P_2$ |
| :--- | :--- | :--- | :--- |
| 0 | 3 | 9 | 16 | 24 |

□ Tempo di attesa medio = $(3 + 16 + 9 + 0) / 4 = 7$

---

## Pagina 13

Lunghezza del prossimo CPU Burst

- Si può solo stimare – simile alla precedente
  - Prendi il processo con il CPU burst stimato come il più breve

- Utilizzare la lunghezza del CPU burst precedente, usando la media esponenziale delle lunghezze precedenti

1. $t_n =$ actual length of $n^{th}$ CPU burst
2. $\tau_{n+1} =$ predicted value for the next CPU burst
3. $\alpha, 0 \leq \alpha \leq 1$
4. Define: $\tau_{n+1} = \alpha t_n + (1 - \alpha)\tau_n$.

- Solitamente $\alpha$ settato a $\frac{1}{2}$
- Versione preemptive chiamata shortest-remaining-time-first

---

## Pagina 14

Lunghezza del prossimo CPU Burst

CPU burst ($t_i$) 6 4 6 4 13 13 13 …

"guess" ($\tau_i$) 10 8 6 6 5 9 11 12 …

---

## Pagina 15

Esempi di Exponential Averaging

- $\alpha = 0$
  - $\tau_{n+1} = \tau_n$
  - Storia recente non conta
- $\alpha = 1$
  - $\tau_{n+1} = \alpha t_n$
  - Conta solo l’ultimo CPU burst
- Espandendo la formula si ottiene:
  $$\tau_{n+1} = \alpha t_n + (1 - \alpha) \alpha t_{n-1} + \ldots$$
  $$+ (1 - \alpha)^{j} \alpha t_{n-j} + \ldots$$
  $$+ (1 - \alpha)^{n+1} \tau_0$$
- Sia $\alpha$ che $(1 - \alpha)$ sono minori o uguali ad 1, ogni termine successive ha minor peso del predecessore

---

## Pagina 16

Esempio di Shortest-remaining-time-first

□ Si considerano diversi tempi di arrivo e si introduce la prelazione

| Process | Arrival Time | Burst Time |
| :--- | :--- | :--- |
| $P_1$ | 0 | 8 |
| $P_2$ | 1 | 4 |
| $P_3$ | 2 | 9 |
| $P_4$ | 3 | 5 |

□ Preemptive SJF Gantt Chart

| $P_1$ | $P_2$ | $P_4$ | $P_1$ | $P_3$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 5 | 10 | 17 | 26 |

□ Tempo attesa medio = $[(10-1)+(1-1)+(17-2)+5-3)]/4 = 26/4 = 6.5 \text{ msec}$

□ Senza prelazione 8.75 msec

---

## Pagina 17

Scheduling con Priorità

- Numero di priorità (intero) associato ad ogni processo
- CPU allocata al processo con più alta priorità (minor intero ≡ maggiore priorità)
  - Preemptive
  - Nonpreemptive
- SJF è un priority scheduling con priorità inversamente proporzionale alla predizione del prossimo CPU
- Problema ≡ Starvation – processi a bassa priorità mai eseguiti
- Soluzione ≡ Aging – al passare del tempo aumenta la priorità del processo

---

## Pagina 18

Esempio di Priority Scheduling

| Process | Burst Time | Priority |
| :--- | :--- | :--- |
| $P_1$ | 10 | 3 |
| $P_2$ | 1 | 1 |
| $P_3$ | 2 | 4 |
| $P_4$ | 1 | 5 |
| $P_5$ | 5 | 2 |

□ Priority scheduling Gantt Chart

| $P_2$ | $P_5$ | $P_1$ | $P_3$ | $P_4$ |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 6 | 16 | 18 | 19 |

□ Tempo di attesa medio = 8.2 msec

---

## Pagina 19

Round Robin (RR)

- Ogni processo riceve una piccola unità di CPU (time quantum $q$), di solito 10-100 msec. A tempo scaduto il processo viene prelazionato e messo alla fine della coda ready
- Con $n$ processi in coda ready e time quantum $q$, ogni processo riceve 1/n di CPU time in chunk di $q$ unità di tempo
- Tempi di attesa inferiori a $(n-1)q$ unità di tempo
  - Es. 5 processi con $q = 20$ millisec prende 20 millisec ogni 100
- Un timer interrompe ad ogni quanto per schedulare il processo successivo
- Prestazioni
  - $q$ largo $\Rightarrow$ FIFO
  - $q$ piccolo $\Rightarrow q$ grande rispetto al context switch altrimenti l’overhead è troppo alto

---

## Pagina 20

Esempio di RR con Quanto = 4

| Process | Burst Time |
| :--- | :--- |
| $P_1$ | 24 |
| $P_2$ | 3 |
| $P_3$ | 3 |

□ Gantt chart:

| $P_1$ | $P_2$ | $P_3$ | $P_1$ | $P_1$ | $P_1$ | $P_1$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 4 | 7 | 10 | 14 | 18 | 22 | 26 | 30 |

□ Tipicamente maggiore turnaround medio di SJF, ma migliore risposta
□ q deve essere grande rispetto al tempo di context switch
□ q di solito tra 10ms e 100ms, context switch < 10 microsec

---

## Pagina 21

Quanto di Tempo e Tempo di Context Switch

Assumendo un processo di 10 unità di tempo
Se il quanto è 12 il processo completa senza context switch
Se il quanto è 6 ne occorre uno
Se il quanto è 1 ne occorre uno 9

Se cs è 10% del quanto, per ogni quanto si perde 10% di CPU

---

## Pagina 22

Tempo di Turnaround varia con il Time Quantum

Tempo di turnaround varia con la dimensione del quanto e non incrementa sempre con la dimensione
- es. 10 unità tempo se 1 q allora 29 turn se 10 q allora 20 turn

Dipende dal tempo di completamento dei processi

| process | time |
| :--- | :--- |
| $P_1$ | 6 |
| $P_2$ | 3 |
| $P_3$ | 1 |
| $P_4$ | 7 |

Regola empirica: l’80% dei CPU burst dovrebbero essere più corti di q

---

## Pagina 23

RR con Priorità

Si segue la priorità, processi con pari priorità con RR

| Process | Burst Time | Priority |
| :--- | :--- | :--- |
| $P_1$ | 4 | 3 |
| $P_2$ | 5 | 2 |
| $P_3$ | 8 | 2 |
| $P_4$ | 7 | 1 |
| $P_5$ | 3 | 3 |

Quantum 2 millisecondi

---

## Pagina 24

Code Multiple

- Se una sola coda O(n) per cercare le priorità
- Comodo avere code separate per le differenti priorità
- Assegnazione delle code ai processi
  - di solito statico e processo rimante in quella coda
- Ogni coda ha il suo scheduling

priority = 0
$$T_0 \quad T_1 \quad T_2 \quad T_3 \quad T_4$$

priority = 1
$$T_5 \quad T_6 \quad T_7$$

priority = 2
$$T_8 \quad T_9 \quad T_{10} \quad T_{11}$$

priority = n
$$T_x \quad T_y \quad T_z$$

---

## Pagina 25

Code Multiple

□ Si può usare per partizionare processi in base al tipo
  □ Es. la Coda Ready partizionata in diverse code, e.g.:
    ► foreground (interattiva)
    ► background (batch)
□ Processi assegnati alle code in modo fisso (non passaggio tra code)
□ Ogni coda ha un suo algoritmo di scheduling:
  □ foreground – RR
  □ background – FCFS

□ Scheduling tra code:
  □ Scheduling a priorità fissata (i.e., serve tutti dal foreground e poi dal background). Possibilità di starvation.
  □ Altra possibilità time-slice tra code – ogni coda prende un certo quanto di CPU che può schedulare tra i suoi processi
    ► es., 80% ai processi foreground in RR 20% ai processi in background in FCFS

---

## Pagina 26

Code Multiple

highest priority

- system processes
- interactive processes
- interactive editing processes
- batch processes
- student processes

lowest priority

---

## Pagina 27

Code Multiple con Feedback

- Metodi più adattivi
- Un processo può spostarsi tra le code
  - Processi I/O bound con priorità più elevata
  - Aging (aumento di priorità nel tempo) per evitare starvation
- Lo scheduler di code multiple con feedback definito da:
  - Numero di code
  - Algoritmi di scheduling per ogni coda
  - Metodi per determinare quando aumentare la priorità di processo
  - Metodi per determinare quando abbassare la priorità un processo
  - Metodi per determinare quale coda assegnare ad un processo quando richiede un servizio
- È lo schedulatore più complesso e flessibile

---

## Pagina 28

Esempio di Coda Multiple con Feedback

Si considerino tre code:
- $Q_0$ – RR quanto di tempo 8 msec
- $Q_1$ – RR quanto di tempo 16 msec
- $Q_2$ – FCFS

Scheduling
- Prelazione con priorità 0, 1, 2
- Nuovo processo in Ready messo in coda $Q_0$
  - Il processo riceve 8 msecs di CPU
  - Se non finisce in 8 msec, il processo è mosso in coda $Q_1$
- Se vuota $Q_0$
  - il primo processo in $Q_1$ riceve 16 msec
  - Se non completa viene prelazionato e si sposta sulla coda $Q_2$
- Se vuote $Q_0$ e $Q_1$ vengono eseguiti i processi in coda $Q_2$ con FCFS
- Schedulatore che dà priorità a processi rapidi e mette in coda quelli più lunghi

---

## Pagina 29

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

---

## Pagina 30

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

B

---

## Pagina 31

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

B C D

---

## Pagina 32

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

B C D B E

---

## Pagina 33

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

B C D B E

---

## Pagina 34

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

B C D B E D

---

## Pagina 35

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

A B C D B E D
B C D B E D

---

## Pagina 36

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

| A | B | C | D | B | E | D |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 3 | 7 | 11 | 15 | 17 | 19 | 20 |

$$t_a(RR - 4) = \frac{(3 - 3 - 0) + (17 - 6 - 2) + (11 - 4 - 4) + (20 - 5 - 6) + (19 - 2 - 8)}{5} = 6$$

---

## Pagina 37

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e CPU-brust indicato

Si calcoli il tempo medio di attesa e turnaround RR quanto = 4

| processo | tempo di arrivo | CPU-burst (millisec.) |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

$$t_{tr}(RR - 4) = \frac{(3 - 0) + (17 - 2) + (11 - 4) + (20 - 6) + (19 - 8)}{5} = 10$$

---

## Pagina 38

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e tempo di esecuzione

| processo | tempo di arrivo | tempo di esecuzione |
| :--- | :--- | :--- |
| $P_1$ | 0 | 20 |
| $P_2$ | 8 | 5 |
| $P_3$ | 3 | 12 |
| $P_4$ | 10 | 6 |
| $P_5$ | 7 | 8 |

Calcolare tempo medio di attesa e turnaround per SJF preemptive

---

## Pagina 39

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e tempo di esecuzione

Calcolare tempo medio di attesa e turnaround per SJF preemptive

---

## Pagina 40

Esercizio Scheduling

Si considerino i processi in tabella con tempi di arrivo (in millisecondi) e tempo di esecuzione

Calcolare tempo medio di attesa e turnaround per SJF preemptive

$$t_a = \frac{31 + 0 + 11 + 3 + 19}{5} = 12.8 \text{ msec}$$

$$t_{tr} = \frac{51 + 5 + 23 + 9 + 27}{5} = 23 \text{ msec}$$

---

## Pagina 41

Scheduling di Thread

- Distinguere tra thread user-level e kernel-level
- Moderni SO schedulano thread kernel-level, non processi
- Thread user-level gestiti da libreria e kernel non ne è al corrente
- Per essere eseguiti i thread user-level devono essere mappati in kernel-level

---

## Pagina 42

Scheduling di Thread

□ Per essere eseguiti i thread user-level devono essere mappati in kernel-level

□ Modelli many-to-one e many-to-many, la libreria dei thread gestisce gli user-level threads per poi lanciare i lightweight processes (LWPs)

□ Lo schema è detto Process-Contention Scope (PCS): la competizione per lo CPU è tra thread dello stesso processo

□ Tipicamente scheduling con priorità (definita dal programmatore)

□ Per decidere il kernel thread da schedulare in CPU il kernel usa un System-Contention Scope (SCS)

□ Competizioni tra tutti i thread nel sistema

□ Sistemi che utilizzano modelli one-to-one (Linux, Windows) usano SCS

---

## Pagina 43

Pthread Scheduling

- API permettono di specificare PCS o SCS durante la creazione dei thread
- POSIX Pthread permette di specificare entrambe le modalità:
  - PTHREAD_SCOPE_PROCESS usa PCS scheduling
  - PTHREAD_SCOPE_SYSTEM usa SCS scheduling
- Limtato da OS – Linux e Mac OS permettono solo PTHREAD_SCOPE_SYSTEM

---

## Pagina 44

Pthread Scheduling API

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

---

## Pagina 45

Pthread Scheduling API

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

---

## Pagina 46

Scheduling Multi-Processore

- CPU scheduling più complesso se ci sono più CPU
- Diverse architetture disponibili:
  - Multicore CPU
  - Multithreaded cores
  - Sistemi NUMA
  - Multiprocessamento eterogeneo
- Per i primi tre casi assumiamo processori omogeneri (stesse capacità)

---

## Pagina 47

Scheduling Multi-Processore

- CPU scheduling più complesso se ci sono più processori
- Homogeneous processors – processori identici per funzionalità
- Asymmetric multiprocessing – un solo processore (master) coinvolto nelle decisioni di scheduling e accede alle strutture dati di sistema senza condivisione di dati
  - Semplifica la gestione, ma il processore server master fa da collo di bottiglia
- Symmetric multiprocessing (SMP) – approccio standard: ogni processore fa self-scheduling

---

## Pagina 48

Scheduling Multi-Processore

- CPU scheduling più complesso se ci sono più CPU
- Homogeneous processors – processori identici per funzionalità
- Asymmetric multiprocessing – un solo processore (master) prende decisioni di scheduling e accede alle strutture dati di sistema senza condivisione di dati.
  - Semplifica la gestione, ma il processore server master fa da collo di bottiglia
- Symmetric multiprocessing (SMP) – approccio standard: ogni processore fa self-scheduling, due modalità
  - tutti i processi in una sola coda ready
  - ognuno ha una sua coda privata di processi ready

![Diagram](image_link)

---

## Pagina 49

Scheduling Multi-Processore

- CPU scheduling più complesso se ci sono più CPU
- Homogeneous processors – processori identici per funzionalità
- Asymmetric multiprocessing – un solo processore (master) prende decisioni di scheduling e accede alle strutture dati di sistema senza condivisione di dati. Semplifica la gestione, ma il processore server master fa da collo di bottiglia
- Symmetric multiprocessing (SMP) – approccio standard: ogni processore fa self-scheduling
  - tutti i processi in una coda ready oppure ogniuno ha una sua coda privata di processi ready
  - Attualmente la soluzione più commune/standard in SMP sono le code private
  - Tutti i sistemi supportano SMP (Linux, Windows, MacOS, Android, etc.)

---

## Pagina 50

Scheduling Multi-Processore

- CPU scheduling più complesso se ci sono più CPU
- Homogeneous processors – processori identici per funzionalità
- Asymmetric multiprocessing – un solo processore (master) prende decisioni di scheduling e accede alle strutture dati di sistema senza condivisione di dati. Semplifica la gestione, ma il processore server master fa da collo di bottiglia
- Symmetric multiprocessing (SMP) – approccio standard: ogni processore fa self-scheduling
  - tutti i processi in una coda ready oppure ogniuno ha una sua coda privata di processi ready
  - Attualmente la soluzione più commune/standard in SMP sono le code private
  - Tutti i sistemi supportano SMP (Linux, Windows, macOS, Android, etc.)

---

## Pagina 51

Scheduling Multi-Processore

- Sistemi multicore
- Ogni core è per il SO una CPU separata
- Core veloci, ma problemi di memory stall attesa di dati pronti in memoria

- Più thread pronti per core: chip multithreading (CMT)

---

## Pagina 52

Scheduling Multi-Processore

- Sistemi multicore
- Ogni core appare al SO come una CPU separata
- Core veloci, ma problemi di memory stall attesa di dati pronti in memoria
- Più thread pronti per core: chip multithreading (CMT)
- Per SO è come avere più CPU intel chiama hyperthreading
- Es. Oracle Spark M7 8 thread per core su 8 core, come 64 CPU

---

## Pagina 53

Scheduling Multi-Processore

- Sistemi multicore
- Ogni core appare al SO come una CPU separata
- Core veloci, ma problemi di memory stall attesa di dati pronti in memoria
- Più thread pronti per core: chip multithreading (CMT)
- Per OS è come avere più CPU intel chiama hyperthreading
- Es. Oracle Spark M7 8 thread per core su 8 core, come 64 CPU
- Due livelli di scheduling:
  - Software threads (SO)
  - Hardware threads

---

## Pagina 54

Multiple-Processor Scheduling – Load Balancing

Se Symmetric Multiprocessing (SMP) e code private:
- **Load balancing**: necessario bilanciare il carico tra i processori

Due metodi di Load balancing:
- **Push migration** – un processo verifica continuamente il carico dei processori, se trova uno sbilanciamento sposta/spinge il task dalla CPU sovraccarica alle altre
- **Pull migration** – i processori in idle prendono/tirano i task in attesa sulle code dei processori occupati
- Esempio: Linux implementa entrambe le strategie

**Processor affinity** – processo ha affinità per il processore su cui è in running
- **soft affinity** – tentativo di mantenere il processore del thread
- **hard affinity** – specifica il sottoinsieme di processori per il thread
- Esempio, Linux implementa soft, ma supporta entrambi
- Con code private per core più semplice affinity

---

## Pagina 55

NUMA e CPU Scheduling

Non-uniform Memory Access (NUMA)
- Due chip con la propria CPU e memoria
- Accessi in memoria a velocità diversa
- C’è un conflitto tra problematiche di accesso in memoria e load balancing
- Spostando i thread dai core di riferimento si rallenta l’accesso ai dati

Gli algoritmi di memory-placement possono considerare l’affinity

---

## Pagina 56

Heterogeneus Multiprocessing

- Alcuni sistemi hanno architetture multicore non omogenee
  - Diverso clock, diverso consumo di energia, etc.
  - Non asimmetrici (perché core omogenei per capacità di calcolo)
  - ma diversi consumi: Big core e Little core (processori ARM)
    - Big core veloci ma consumano
    - Little core lenti ma economici
    - Vantaggio per sistemi mobile
    - Algoritmi di scheduling finalizzati al risparmio di energia

---

## Pagina 57

Real-Time CPU Scheduling

- Sistemi Real-Time
- Soft real-time system
  - non garanzie su quando un processo verrà schedulato, solo processi critici preferiti a non critici
- Hard real-time system
  - task servito prima di una deadline
- Latenza di un evento:
  - Tempo trascorso tra evento e risposta del sistema

---

## Pagina 58

Real-Time CPU Scheduling

- Sistemi Real-Time
- Soft real-time system
  - non garanzie su quando un processo verrà schedulato, solo processi critici preferiti a non critici
- Hard real-time system
  - task servito prima di una deadline
- Due tipi di latenze incidono sulla prestazione
  1. Interrupt latency – tempo dall’arrivo dell’interrupt allo start della routine di servizio
  2. Dispatch latency – tempo di scheduling per fare lo switch di un altro processo

Durante gli update delle strutture del kernel gli interrupt sono disabilitati, in sistemi real time, va minimizzato questo tempo

---

## Pagina 59

Real-Time CPU Scheduling

- **Dispatch latency**: fase di conflitto e fase di dispatch del processo
- Fase di gestione del **conflitto** durante la dispatch latency:
  1. Prelazione di qualunque processo in kernel mode
  2. Rilascio delle risorse occupate dai processi a bassa priorità quando richieste dai processi ad alta priorità

Reattività richiede preemtive kernel

**Latenza relativa al dispatch**: periodo di tempo necessario al dispatcher per bloccare un processo e avviarne un altro

Diversi microsecondi per la gestione, i sistemi real-time devono gestire

---

## Pagina 60

Priority-based Scheduling

- Nel real-time scheduling lo scheduler deve supportare prelazione e priority-based scheduling
  - Es. Windows ha 32 livelli di priorità con i livelli da 16 a 31 per i processi real-time
  - Ma questo garantisce solo il soft real-time

- Per hard real-time deve anche garantire le deadline
  - Servono altri meccanismi ed altre politiche di schedulazione

---

## Pagina 61

Priority-based Scheduling

- Nel real-time scheduling lo scheduler deve supportare preemptive e priority-based scheduling
  - Ma questo garantisce solo il soft real-time
- Per hard real-time deve anche garantire le deadlines
- Consideriamo task periodici
  - Richiedono la CPU a intervalli costanti
  - Ottenuta la CPU ha un tempo di processo $t$, deadline $d$, e periodo $p$
  - $0 \leq t \leq d \leq p$
  - Rate di un task periodico $1/p$

---

## Pagina 62

Priority-based Scheduling

- Nel real-time scheduling lo scheduler deve supportare preemptive e priority-based scheduling
  - Ma questo garantisce solo il soft real-time
- Per hard real-time deve anche garantire le deadlines
- Consideriamo task periodici
  - Richiedono la CPU a intervalli costanti
  - Ottenuta la CPU ha un tempo di processo $t$, deadline $d$, e periodo $p$
  - $0 \leq t \leq d \leq p$
  - Rate di un task periodico $1/p$
- Admission control algorithm: il processo dichiara una deadline, lo scheduler può ammettere il processo garantendo il rispetto della deadline oppure non ammettere

---

## Pagina 63

Rate Monotonic Scheduling

- Priorità assegnata in base all’inverso del periodo
  - Periodi brevi = priorità alta;
  - Periodi lunghi = priorità bassa
  - Priorità alta a chi interviene più spesso
  - Ogni processo mantiene lo stesso CPU brust

- Esempio:
  - Periodi 50 e 100, tempo di processamento rispettivamente 20 e 35
  - Deadline: terminare prima del prossimo periodo
  - Uso CPU per $P_1$ di è 20/50 = 0.4, per $P_2$ di è 35/100 = 0.35, tot 0.75
  - Assumendo $P_2$ con priorità più alta di $P_1$ deadline persa per $P_1$

---

## Pagina 64

Rate Monotonic Scheduling

- Priorità assignata in base all’inverso del periodo
- Periodi brevi = priorità alta;
- Periodi lunghi = priorità bassa
- Esempio:
  - Periodi 50 e 100, tempo di processamento 20, 35
  - Deadline: terminare prima del prossimo period
  - Uso CPU per $P_1$ di è 20/50 = 0.4, per $P_2$ di è 35/100 = 0.35, tot 0.75
  - Assumendo RMS:
    - $P_1$ con priorità più alta di $P_2$ entrambe le deadline rispettate

---

## Pagina 65

Deadline persa con il Rate Monotonic Scheduling

- Consideriamo un caso in cui non si riesce a schedulare
  - Se $P_1$ ha periodo 50 e CPU brust 25 e $P_2$ periodo 80 e CPU brust 35
  - Utilizzo CPU 25/50 + 35/80 = 0.94
  - $P_2$ interrotta da $P_1$ quando riprende finisce a 85, ma doveva finire ad 80

- Non sfrutta completamente la CPU, l’utilizzo diminuisce con il numero di processi

$$N(2^{1/N} - 1)$$

- Con 1 processo 100%, con 2 processi 83%, con al crescere di N 69%

---

## Pagina 66

Earliest Deadline First Scheduling (EDF)

- Priorità sono assegnate secondo le deadline:
  - prima la deadline, più alta è la priorità; più lontana è la deadline, più bassa è la priorità (le priorità non sono fisse, variano nel tempo)

P1: p1 = 50, t1 = 25; P2: p2 = 80, t2= 35

Non richiede la periodicità dei processi e neppure CPU brust costante
Ogni processo deve dichiarare la deadline quando diventa runnable

Teoricamente ottimo (se utilizzo sotto 100% di CPU rispetta la deadline) però va considerate il context switch e il costo della gestione dell’interrupt

---

## Pagina 67

Earliest Deadline First Scheduling (EDF)

- Priorità sono assegnate secondo le deadline
- Esempio:
  - Tracciare il Gantt secondo EDF verificando se le scadenze sono rispettate (scheduling ammissibile)

| Processo | Tempo di arrivo | Esecuzione | Scadenza |
| :--- | :--- | :--- | :--- |
| $J_1$ | 0 | 3 | 16 |
| $J_2$ | 2 | 1 | 7 |
| $J_3$ | 0 | 6 | 8 |
| $J_4$ | 8 | 2 | 11 |
| $J_5$ | 13 | 3 | 18 |

---

## Pagina 68

Earliest Deadline First Scheduling (EDF)

- Priorità sono assegnate secondo le deadline
- Esempio:
  - Tracciare il Gantt secondo EDF verificando se le scadenze sono rispettate (ammissibile)

| Processo | Tempo di arrivo | Esecuzione | Scadenza |
| :--- | :--- | :--- | :--- |
| $J_1$ | 0 | 3 | 16 |
| $J_2$ | 2 | 1 | 7 |
| $J_3$ | 0 | 6 | 8 |
| $J_4$ | 8 | 2 | 11 |
| $J_5$ | 13 | 3 | 18 |

---

## Pagina 69

Earliest Deadline First Scheduling (EDF)

- Priorità sono assegnate secondo le deadline:
  - prima la deadline, più alta è la priorità; più lontana è la deadline, più bassa è la priorità (le priorità non sono fisse, variano nel tempo)

Non richiede la periodicità dei processi e neppure CPU brust costante

Ogni processo deve dichiarare la deadline quando diventa runnable

Teoricamente ottimo (se utilizzo sotto 100% di CPU rispetta la deadline) però va considerate il context switch e il costo della gestione dell’interrupt

Se un insieme di processi caratterizzati da: tempo di arrivo, un requisito di esecuzione, scadenza può essere schedulata (da un algoritmo) in modo da garantire tutte le scadenze, l'EDF garantirà la scadenza.

---

## Pagina 70

Earliest Deadline First Scheduling (EDF)

- Priorità sono assegnate secondo le deadline:
  - prima la deadline, più alta è la priorità; più lontana è la deadline, più bassa è la priorità (le priorità non sono fisse, variano nel tempo)

Attenzione si è assunto deadline = perido.
Se la deadline è prevista prima del periodo non garantisce.

Es. T0(5,13,20), T1(3,7,11), T2(4,6,10), T3(1,1,20)

Utilizzo 5/20+3/11+4/10+1/20 = 0.97

| TaskNo(computation time, relative deadline, period) |
|-----------------------------------------------|
| T0(5,13,20) |
| T1(3,7,11) |
| T2(4,6,10) |
| T3(1,1,20) |

EDF Scheduling

CPU unit time index 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

---

## Pagina 71

Scheduling a Quote Proprozionali

- Quote proporzionali di CPU preallocate per le applicazioni
- $T$ quote di CPU devono essere preallocate tra tutti i processi

- Un’applicazione riceve $N$ quote con $N < T$
  - L’algoritmo assicura l’applicazione riceverà $N / T$ del tempo totale del processore

- Esempio $T = 100$ da dividere su A, B, C. A che riceve 50, B riceve 15, e C riceve 20. Rimangono quote per altri processi

- Algoritmo di admission control assegna le quote rimanenti ai nuovi processi nel rispetto delle quote già assegnate

---

## Pagina 72

POSIX Real-Time Scheduling

POSIX.1b fornisce API standard per gestire real-time threads

Definisce due classi di scheduling per real-time threads:

1. SCHED_FIFO - threads sono schedulati con strategia FCFS con coda FIFO. No time-slicing per thread con priorità uguale
2. SCHED_RR - simile a SCHED_FIFO ma con time-slicing per thread di pari priorità

Definisce due funzioni per prendere e settare la politica di scheduling:

1. pthread_attr_getsched_policy(pthread_attr_t *attr, int *policy)
2. pthread_attr_setsched_policy(pthread_attr_t *attr, int policy)

---

## Pagina 73

POSIX Real-Time Scheduling API

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

---

## Pagina 74

POSIX Real-Time Scheduling API (Cont.)

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

---

## Pagina 75

Hard real-time

Il POSIX 1b supportato a partire da kernel Linux (dal 2.6) fornendo schedulazione con priorità, supporto per segnali, sincronizzazione etc.

Per avere garanzie hard-real time occorre un kernel adatto:
Real-Time Operating System (RTOS)

Es. In Linux PREEMPT_RT Kernel (patch)
Altri approcci basati su cokernel (es., RTLinux, Xenomai, RTAI)

---

## Pagina 76

Virtualizzazione e Scheduling

- Con Virtualizzazione si schedula con SO ospiti multipli sulla CPU(s)
- Ogni ospite esegue il suo scheduling
  - Ma in realtà non ha una sua CPU e sta schedulando pensando di avere l’intera CPU
  - Può portare a risposte rallentate
  - Lo stesso clock del Sistema può essere rallentato
- Si possono perdere i benefici di un buon algoritmo di scheduling implementato sul SO ospite

---

## Pagina 77

Esempi di SO

- Linux scheduling
- Windows scheduling

---

## Pagina 78

Scheduling Linux prima della versione 2.5

□ Prima della versione kernel 2.5 variazione dell’algoritmo di scheduling standard di UNIX

□ Linux v1.2
  □ Unica lista contenente tutti i processi attivati sulla macchina.
    ► Il primo elemento della lista è la task_struct di init
  □ Ogni processo ha una priorità statica (nice value o nice)
  □ La priorità varia da -20 (priorità più alta) a +19 (priorità più bassa).
  □ Il valore di default è 10.
  □ Schema classico delle priorità in UNIX.
  □ Scheduling in modalità “round robin pesato”
    ► Un processo in attesa da più tempo viene favorito rispetto ad un processo che attende da meno tempo. A parità di attesa, un processo a priorità più alta viene favorito rispetto ad un processo a priorità più bassa.
    ► Ad ogni invocazione dello schedule, la lista è scandita ed i contatori aggiornati, si sceglie il processo per cui il contatore è massimo

---

## Pagina 79

Scheduling Linux prima della versione 2.5

- Prima della versione kernel 2.5 variazione dell’algoritmo di scheduling standard di UNIX
- Linux v2.2
  - Classi priorità multipla
  - Priority-based e time-sharing
  - Prelazione con priorità
  - Funzione goodness() ritorna un peso (weight) nell’intervallo [-1000, 1000].
    - Dipende dalla priorità e dai tempi di esecuzione
  - Il peso è usato per scegliere il processo da schedulare.
    - Selezione basata su Priorità con RR (se stessa goodness)

- Si usano 140 livelli di priorità.
  - Livelli [0, 99]: usati da algoritmi di scheduling di tipo soft real time (SCHED_FIFO, SCHED_RR), che hanno sempre la precedenza sull’algoritmo standard.
  - Livelli [100, 139]: corrispondono all’intervallo [-20, 19] (SCHED_OTHER) e sono utilizzati dall’algoritmo di scheduling di default (round robin pesato).

---

## Pagina 80

Linux Real-Time Scheduling

- Real-time scheduling in POSIX.1b con SCHED_FIFO o SCHED_RR
  - Task real-time assegnati a priorità statiche tra 0 e 99
  - Real-time hanno valori più bassi di quelli dei task normali e sono mappati in uno schema di priorità globale

  - Priority
    - Higher
    - Lower

- Le priorità relative dei processi real-time sono assicurate
- Il kernel non fornisce garanzia sui tempi di attesa dei processi pronti
- Se interruzione per real-time arriva mentre il kernel serve una chiamata di sistema, il processo real-time deve attendere

---

## Pagina 81

Scheduling Linux prima della versione 2.5

- Prima della versione kernel 2.5 variazione dell’algoritmo di scheduling standard di UNIX

- Classi priorità gestite con RR pesato
  - Priority-based e time-sharing
  - Prelazione con priorità
  - Priorità assegnata sulla base di una funzione goodness() ritorna un peso (weight) nell'intervallo [-1000, 1000].
  - Il peso è usato per scegliere il processo da schedulare.
  - Uso di quanti di tempo variabili (time slice).
  - L'algoritmo di scheduling è O(n) rispetto al numero di processi

- Tempo O(n) per selezionare il processo, dipende dal numero di processi
- Metodo non flessibile (lista unica) e poco adatto a Symmetric Multiprocessing (SMP)

---

## Pagina 82

Scheduling Linux prima della versione 2.5

- Prima della versione kernel 2.5 variazione dell’algoritmo di scheduling standard di UNIX

- Lo scheduler del kernel v2.4 è una estensione del Kernel v2.2.
  - Uso di quanti di tempo variabili (time slice) dipendente dalla priorità.
  - Uso di un sistema di schedulazione a crediti.
  - Sistema a crediti: un credito 10ms di esecuzione. Un credito ogni volta che si blocca. Dopo l'esecuzione di un time slice si scala un credito. No credit no CPU.
  - Quando tutti i processi in stato RUNNING hanno esaurito i crediti, il kernel ricalcola il credito per tutti i processi (recrediting).
  - L'algoritmo di scheduling è O(n) rispetto al numero di processi (unica lista)

- Il tempo per la selezione del processo migliore dipende dal numero di processi
- Migliorato ma non ok per SMP

---

## Pagina 83

Scheduling Linux versione 2.5

Con la versione 2.5 si propone uno scheduler che lavora a tempo costante O(1) indipendente dal numero di task nel sistema:

- Preemptive e priority based
- Due intervalli di priorità: processi time-sharing (detti nice) e real-time
- Real-time da 0 a 99 e valori nice da 100 a 140
- Si mappano in priorità globali con valori bassi che indicano alta priorità
- Priorità più alte prendono time-slice q maggiori

$$base \ time \ quantum \ (in \ milliseconds) = \begin{cases} (140 - static \ priority) \times 20 & \text{if } static \ priority < 120 \\ (140 - static \ priority) \times 5 & \text{if } static \ priority \ge 120 \end{cases}$$

| Description | Static priority | Nice value | Base time quantum |
| :--- | :--- | :--- | :--- |
| Highest static priority | 100 | −20 | 800 ms |
| High static priority | 110 | −10 | 600 ms |
| Default static priority | 120 | 0 | 100 ms |
| Low static priority | 130 | +10 | 50 ms |
| Lowest static priority | 139 | +19 | 5 ms |

---

## Pagina 84

Scheduling Linux versione 2.5

Con la versione 2.5 si propone uno scheduler che lavora a tempo costante O(1) indipendente dal numero di task nel sistema:

- Preemptive e priority based
- Due intervalli di priorità: processi time-sharing (detti nice) e real-time
- Real-time da 0 a 99 e valori nice da 100 a 140
- Si mappano in priorità globali con valori bassi che indicano alta priorità
- Priorità più alte prendono time-slice q maggiori
- Non goodness

- I task sono in esecuzione finché hanno il time slice (active)
- Quando scade non vanno in esecuzione finché tutti gli altri tasks non usano lo slice
- Tutti i task eseguibili tracciati con code separate
  - Due array di priorità (active, expired)
  - Task indicizzati con la priorità
  - Finiti gli attivi, gli array sono scambiati con expired (veloce scambio)
  - Scambio tempo costante, ma anche ricerca della priorità

---

## Pagina 85

Scheduling Linux versione 2.5

Con la versione 2.5 si propone uno scheduler che lavora a tempo costante O(1) indipendente dal numero di task nel sistema:

- Preemptive e priority based
- Due intervalli di priorità: processi time-sharing (detti nice) e real-time
- Real-time da 0 a 99 e valori nice da 100 a 140
- Si mappano in priorità globali con valori bassi che indicano alta priorità
- Priorità più alte prendono time-slice q maggiori
- I task sono in esecuzione finché hanno il time slice (active)
- Quando scade non vanno in esecuzione finché tutti gli altri tasks non usano lo slice
- Tutti i task eseguibili tracciati con code separate per-CPU

► Due array di priorità (active, expired)

---

## Pagina 86

Scheduling Linux versione 2.5

Con la versione 2.5 si propone uno scheduler che lavora a tempo costante O(1) indipendente dal numero di task nel sistema:

- Preemptive e priority based
- Due intervalli di priorità: processi time-sharing (detti nice) e real-time
- Real-time da 0 a 99 e valori nice da 100 a 140
- Si mappano in priorità globali con valori bassi che indicano alta priorità
- Priorità più alte prendono time-slice q maggiori
- I task sono in esecuzione finché hanno il time slice (active)
- Quando scade non vanno in esecuzione finché tutti gli altri tasks non usano lo slice
- Tutti i task eseguibili tracciati con code separate per-CPU
  - Due array di priorità (active, expired)
  - Task indicizzati con la priorità
  - Finiti gli attivi, gli array sono scambiati con expired (veloce scambio)
  - Scambio tempo costante, ma anche ricerca della priorità

- Buon funzionamento con SMP, ma tempi di risposta non soddisfacenti per processi interattivi

---

## Pagina 87

Linux Scheduling in Versione 2.6.23 +

Completely Fair Scheduler (CFS)
- Classi di scheduling, altre possono essere aggiunte
  1. Default (CFS scheduling)
  2. Real-time (real-time scheduling)

Latenza target:
- Intervallo di tempo durante il quale un task deve andare in run almeno una volta

Fairness:
- se N processi uguali su latenza target T, ogni processo deve prendere T / N
- Assumiamo latenza target = 4 e processi con CPU burst 8, 4, 16, 4

- Con coda T1, T2, T3, T4 tutti eseguono 1 ms per 4 cicli … poi T2 e T4 finiscono
- Rimane coda T1 e T3 che si dividono 2 ms per 2 cicli … poi T1 finisce
- T3 rimane solo che fa 2 cicli da 4 ms … e conclude

---

## Pagina 88

Linux Scheduling in Versione 2.6.23 +

Completely Fair Scheduler (CFS)
- Classi di scheduling, altre possono essere aggiunte
  1. Default (CFS scheduling)
  2. Real-time (real-time scheduling)

Latenza target:
- Intervallo di tempo durante il quale un task deve andare in run almeno una volta

Fairness:
- se N processi uguali su latenza target T, ogni processo deve prendere T / N

Priorità:
- Allocazione basata su proporzione di CPU time pesata sul peso del task
- Se N task time_slice(task) = (target_latency / N) * task_weight
  - Granularità minima, es. time_slice_min = 1 ms

Vruntime:
- Il tempo scorre in modo diverso a seconda del processo in esecuzione

Criterio di schedulazione:
- Ad ogni invocazione selezionato il task con il vruntime più basso

---

## Pagina 89

Linux Scheduling in Versione 2.6.23 +

- Completely Fair Scheduler (CFS)
- CFS scheduler mantiene un tempo di esecuzione virtuale per ogni task in una variable vruntime (usata come criterio per schedulare)
  - Es. Se nice diversi (priorità diverse), per nice basso il tempo CPU scorre più lento
  - Es. Se task con stesso nice, uno I/O bound l’altro CPU bound, I/O bound non consuma il suo time_slice, CPU bound lo consuma sempre, a quel punto l’I/O bound potrà avere prelazione su CPU bound per minore vruntime
  - vruntime = tempo_effettivo x peso_riferimento (nice=0) / peso_task_relativo
    - nice = 0 peso = 1024, nice = 10 peso = 64, nice = 19 peso = 15
    - Peso relativo rispetto al peso dei task in coda di w_i / W
- Il prossimo task lo scheduler prende il virtual run time minore
  - con time_slice assegnato in base al suo peso relative
- Ad un nuovo viene assegnato un min_vruntime che permetta di essere eseguito presto (ma non subito)

---

## Pagina 90

The Linux CFS scheduler provides an efficient algorithm for selecting which task to run next. Each runnable task is placed in a red-black tree—a balanced binary search tree whose key is based on the value of `vruntime`. This tree is shown below:

![Diagram of the Linux CFS scheduler tree](image)

When a task becomes runnable, it is added to the tree. If a task on the tree is not runnable (for example, if it is blocked while waiting for I/O), it is removed. Generally speaking, tasks that have been given less processing time (smaller values of `vruntime`) are toward the left side of the tree, and tasks that have been given more processing time are on the right side. According to the properties of a binary search tree, the leftmost node has the smallest key value, which for the sake of the CFS scheduler means that it is the task with the highest priority. Because the red-black tree is balanced, navigating it to discover the leftmost node will require $O(\lg N)$ operations (where $N$ is the number of nodes in the tree). However, for efficiency reasons, the Linux scheduler caches this value in the variable `rb_leftmost`, and thus determining which task to run next requires only retrieving the cached value.

---

## Pagina 91

Linux Scheduling

- Scheduler CSF supporta bilanciamento del carico, riduce al minimo migrazione dei thread
- Il carico del thread è dato da una combinazione di priorità e tasso medio di utilizzo della CPU
  - Carico basso, ma alta priorità simile a carico alto e bassa priorità
  - Dalla somma dei load si ha il carico della coda che si può ribilanciare
  - Domini di scheduling per ridurre il costo del bilanciamento
    - Bilanciamento prima nel dominio più prossimo

---

## Pagina 92

Linux Scheduling in Versione 6.6

- Earliest Eligible Virtual Deadline First (EEVDF) scheduler (November 2023)
- Fair + deadline virtuali
- EEVDF come CFS cerca anche di ottenere un corretto uso della CPU time tra i task
- EEVDF scheduler cerca un “eligible task” con la virtual deadline più vicina

- EEVDF introduce due nozioni: eligibility e lag di un task.
  - EEVDF gestisce il CPU time per un task sulla base di una priorità statica (nice).
  - Ogni task ha un virtual run time
  - Il lag di un task è il gap tra il CPU time ideale e quello effettivo CPU per il task.
    - Lag positivo = poco CPU time allocato.
    - Lag negativo = troppo CPU time allocato (violazione dell’uso corretto di CPU time)
  - Tasks with con lag positive sono eligible (mantiene correttezza)

- EEVDF seleziona i tasks con lag positivo e calcola una virtual deadline (VD) per ognuno selezionando il task con la VD più vicina per la prossima esecuzione

- Se CFS è orientato alla fairness pesata su priorità, EEVDF è orientato alla reattività pesata considerando piorità e deadline

---

## Pagina 93

Linux Scheduling in Versione 6.6

- Earliest Eligible Virtual Deadline First (EEVDF) scheduler (November 2023)
- Fair + deadline virtuali
- EEVDF come CFS cerca anche di ottenere un corretto uso della CPU time tra i task
- EEVDF scheduler cerca un “eligible task” con la virtual deadline più vicina

EEVDF introduce due nozioni: eligibility e lag di un task.

- Esempio:
  - Assumiamo T1, T2, T3 con uguali priorità e lag iniziale 0
  - Se T1 viene schedulato per primo con 30 ms
  - Su 30 ms, l’allocazione equa sarebbe stata 10, 10, 10 (T1 quindi ha debito, T2 e T3 sono in credito) … dunque lag T1 = -20, lag T2 = 10, lag T3 = 10
  - Ora T1 non è più eligible, se lo scheduler assegna poi a T2 30 ms, dopo l’esecuzione i lag diventano T1 = -10, T2 = -10, T3 = 20
  - Rimane quindi solo T3 eligible

---

## Pagina 94

Linux Scheduling in Versione 6.6

□ Earliest Eligible Virtual Deadline First (EEVDF) scheduler (November 2023)
□ Fair + deadline virtuali
□ EEVDF come CFS cerca anche di ottenere un corretto uso della CPU time tra i task
□ EEVDF scheduler cerca un “eligible task” con la virtual deadline più vicina

□ Per ogni processo il virtual_run_time scorre più o meno lento a seconda del peso del processo che è in esecuzione (veloce bassa priorità, lento alta)
  □ V(t)=V(t_prec)+Δt / w_i
  (dove w_i è il peso del task i-esimo rispetto al peso totale dei processi in coda)

□ Ogni volta che lo scheduler è invocato la virtual deadline è aggiornata per tutti i processi in coda:
  □ anche questa è calcolata pesando il tempo richiest C_i per la computazione dal task i-esimo
  □ VD = V(t) + C_i / w_i
  □ Se esiste un task con VD minore della corrente questo prelazione il precedente

---

## Pagina 95

Windows Scheduling

- Windows usa uno schema priority-based preemptive scheduling
  - Il thread a più alta priorità deve essere eseguito

- La parte del Kernel che si occupa di scheduling è chiamata Dispatcher

- Thread eseguono fino al (1) blocco, (2) fine del time slice, (3) prelazionato da un thread a priorità più alta

- I thread real-time possono prelazionare i non-real-time

- 32-livelli di schema di priorità

- Variable class 1-15, real-time class 16-31
  - Priorità 0 è il thread di gestione della memoria

- Code di thread per ogni priorità
  - Lo scheduler cerca i thread in ogni coda
  - Se non trova un runnable thread, allora lancia il thread idle

---

## Pagina 96

Windows Priority Classes

- Relazione tra le priorità nel Kernel e le priorità nelle API
- Win32 API identifica molte classi di priorità per i processi
  - REALTIME_PRIORITY_CLASS, HIGH_PRIORITY_CLASS, ABOVE_NORMAL_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, IDLE_PRIORITY_CLASS
  - Tutte modificabile eccetto REALTIME
  - SetPriorityClass()
- Un thread in una priority class ha una priorità relativa
  - TIME_CRITICAL, HIGHEST, ABOVE_NORMAL, NORMAL, BELOW_NORMAL, LOWEST, IDLE
- Priority class e relative priority si combinano per formare una priorità numerica
- La priorità di base è NORMAL per la classe di appartenenza
  - REALTIME_PRIORITY_CLASS—24
  - HIGH_PRIORITY_CLASS—13
  - ABOVE_NORMAL_PRIORITY_CLASS—10
  - NORMAL_PRIORITY_CLASS—8
- Se il quantum si esaurisce la priorità si abbassa, ma mai sotto la base

---

## Pagina 97

Windows Priorities

| | real-time | high | above normal | normal | below normal | idle priority |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| time-critical | 31 | 15 | 15 | 15 | 15 | 15 |
| highest | 26 | 15 | 12 | 10 | 8 | 6 |
| above normal | 25 | 14 | 11 | 9 | 7 | 5 |
| normal | 24 | 13 | 10 | 8 | 6 | 4 |
| below normal | 23 | 12 | 9 | 7 | 5 | 3 |
| lowest | 22 | 11 | 8 | 6 | 4 | 2 |
| idle | 16 | 1 | 1 | 1 | 1 | 1 |

---

## Pagina 98

Windows Priority Classes

- Se il thread esce dal wait la priorità viene aggiornata a seconda di cosa si attendeva:
  - Es. I/O favorito, memoria meno
- Nel NORMAL_PRIORITY CLASS favoriti processi interattivi
  - Processi in foreground hanno un 3x boost di priorità rispetto a quelli in background
- Gestione dello scheduling su multiprocessori utilizzando processori logici organizzati in insiemi (SMT-set)
  - Il SO cerca di mantenere un processore ideale per un task

---

## Pagina 99

Valutazione Algoritmi

- Come selezionare algoritmi di CPU-scheduling per un SO?
- Determinare un criterio, poi valutare gli algoritmi

- Esempio 1: massimizzare l’utilizzo della CPU, con tempo massimo di risposta inferiore a 300 millisecondi
- Esempio 2: massimizzare la produttività, con tempo di completamento proporzionale (in media) al tempo di esecuzione effettivo

---

## Pagina 100

Lezione: Sincronizzazione

---

## Pagina 101

Obiettivi

- Presentare il concetto di sincronizzazione di processi
- Introdurre il problema della sezione critica
- Soluzioni software e hardware al problema della sezione critica
- Problemi classici di sincronizzazione
- Strumenti per risolvere il problema della sincronizzazione

---

## Pagina 102

Background

- Processi possono essere eseguiti concorrentemente
  - Interrotti in ogni momento con esecuzione incomplete

- Accessi concorrenti a dati condivisi possono portare ad inconsistenze

- La consistenza richiede meccanismi per assicurare l’esecuzione ordinata di processi cooperanti

---

## Pagina 103

Background

- Illustrazione del problema:
  - produttore consumatore con memoria limitata
  - Soluzione vista permetteva occupazione BUFFER_SIZE - 1

---

## Pagina 104

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

## Pagina 105

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

## Pagina 106

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

## Pagina 107

Produttore-Consumatore

Illustrazione del problema:

□ produttore consumatore con memoria limitata

□ Soluzione vista permetteva occupazione BUFFER_SIZE - 1

□ Si può introdurre un intero counter che conta i buffer pieni

□ Inizialmente counter = 0.

□ Poi incrementato dal produttore dopo che produce un elemento nel buffer e decrementato del consumatore dopo che consuma un elemento dal buffer

---

## Pagina 108

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

## Pagina 109

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

## Pagina 110

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

## Pagina 111

Corsa Critica

- Il problema della corsa critica è pervasivo
- In particolare in sistemi multicore dove multithreading è molto enfatizzato
- Occcorrono meccanismi di sincronizzazione e coordinazione dei processi

---

## Pagina 112

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

## Pagina 113

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

## Pagina 114

Problema della Sezione Critica

1. **Mutua Esclusione** - se il processo $P_i$ esegue la sua sezione critica nessun altro processo può eseguire la sua sezione critica

2. **Progresso** - Se nessun processo è in esecuzione nella sua sezione critica ed esistono alcuni processi che desiderano entrare nella loro sezione critica, solo i processi non in remainder section decideranno la selezione dei processi che entreranno successivamente nella sezione critica, che non può essere posticipata indefinitamente

3. **Bounded Waiting** - Deve esistere un limite al numero di volte in cui altri processi possono entrare nelle loro sezioni critiche dopo che un processo ha fatto una richiesta di entrare nella sua sezione critica prima che tale richiesta sia concessa
   - Assunto che ogni processo esegue a velocità nonzero
   - Senza assunzioni sulla velocità relativa degli $n$ processi

---

## Pagina 115

Corse Critiche nel Kernel

- I processi P0 e P1 creano processi figlio utilizzando fork()
- Corse critiche su tabella di file aperti nel sistema
- Corse critiche sulla variabile kernel che rappresenta il prossimo identificatore di processo disponibile (pid), next_available_pid
- Senza mutua esclusione, lo stesso pid potrebbe essere assegnato a due processi diversi

Diagram showing the fork process flow with P0 and P1 processes. P0 child = fork(); P1 child = fork(); request pid next_available_pid = 2615 return 2615 child = 2615

---

## Pagina 116

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

## Pagina 117

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

## Pagina 118

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

## Pagina 119

Soluzione di Peterson

Si può provare che i requisiti sono soddisfatti:

1. Mutua esclusione
   $P_i$ entra in sezione critica solo se:
   $$flag[j] = false \text{ oppure } turn = i$$
2. Requisito di progresso è soddisfatto
3. Requisito bounded-waiting è soddisfatto

---

## Pagina 120

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

## Pagina 121

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

## Pagina 122

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

## Pagina 123

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

## Pagina 124

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

## Pagina 125

Soluzioni basate su Locks

do {
    acquire lock
    critical section
    release lock
    remainder section
} while (TRUE);

---

## Pagina 126

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

## Pagina 127

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

## Pagina 128

Istruzioni atomiche

- Macchine moderne forniscono hardware per istruzioni atomiche
  - Atomiche = non-interrompibili
  - Eseguiibili sequenzialmente

- Consideriamo due tipi di istruzioni
  - Test memory (word) and set (value)
  - Swap contents of two memory words

---

## Pagina 129

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

## Pagina 130

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

## Pagina 131

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

## Pagina 132

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

## Pagina 133

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

## Pagina 134

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

## Pagina 135

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

## Pagina 136

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

## Pagina 137

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

## Pagina 138

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

## Pagina 139

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

## Pagina 140

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

## Pagina 141

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

## Pagina 142

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

## Pagina 143

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

## Pagina 144

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

## Pagina 145

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

## Pagina 146

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

## Pagina 147

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

## Pagina 148

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

## Pagina 149

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

## Pagina 150

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

## Pagina 151

Problemi con i Semafori

- Semantica dei semafori non intuitiva
- Costrutti complessi molto dipendenti dal contest e dalle inizializzazione
- Facilmente portano ad errori

---

## Pagina 152

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

## Pagina 153

Rappresentazione di un Monitor

Schema di un Monitor:
- Coda di accesso
- Dati condivisi
- Operazioni
- Codice di inizializzazione

---

## Pagina 154

Variabili di Condizione

- **condition x, y;**
- Due operazioni sono permesse su una variabile di condizione:
  - `x.wait()` – il processo è sospeso finché non avviene x.signal()
  - `x.signal()` – riprende uno dei processi (se c’è) che ha invocato x.wait()
  - Se non c’è `x.wait()` sulla variabile, non c’è alcun effetto

---

## Pagina 155

Monitor con Variabili di Condizione

shared data

queues associated with x, y conditions

entry queue

operations

initialization code

---

## Pagina 156

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

## Pagina 157

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

## Pagina 158

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

## Pagina 159

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

## Pagina 160

Ripresa dei Processi nel Monitor

- Se molti processi accodati sulla condizione x e avviene un x.signal() quali riprendere?
- FCFS spesso non adeguato
- conditional-wait come x.wait(c)
  - Dove c’è il priority number
  - Processo con numero più basso (highest priority) è il prossimo schedulato (es., tempo di esecuzione più basso)

---

## Pagina 161

Single Resource allocation

- Allocata una singola risorsa tra processi in competizione usando i numeri di prorità che specificano il tempo massimo di utilizzo della risorsa

  R.acquire(t);

  ...

  access the resurce;

  ...

  R.release;

- Con R instanza di tipo ResourceAllocator

---

## Pagina 162

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

## Pagina 163

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

## Pagina 164

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

## Pagina 165

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

## Pagina 166

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

## Pagina 167

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

## Pagina 168

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

## Pagina 169

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

## Pagina 170

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

## Pagina 171

Inversione di Priorità

Il caso del Mars Pathfinder
- Dopo i primi test il software di Sojourner fa continui “reset”
- Inizializzato hw, sw, comunicazione

Stazione meteo riceve dati da bc_sched, blocca il bus
Low task prelaziona

https://www.slideshare.net/gabrielladodero/quando-i-computer-non-funzionano-su-marte

---

## Pagina 172

Inversione di Priorità

Il caso del Mars Pathfinder
- Dopo i primi test il software di Pathfinder fa continui “reset”
- Inizializzato hw, sw, comunicazione

- SO su Pathfinder era VxWorks (real-time)
- Variabile globale per priority inheritance su tutti i semafori
- La variabile settata su Pathfinder e il problema è stato risolto

https://www.slideshare.net/gabrielladodero/quando-i-computer-non-funzionano-su-marte

---

## Pagina 173

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

## Pagina 174

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

## Pagina 175

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

## Pagina 176

Valutazione

La scelta del meccanismo di sincronizzazione influenza le performance.

- Interi atomici più leggeri dei lock e appropriati per update singoli di variabili (es. contatori)
- SpinLock appropriati per multiprocessori se il lock è di breve durata
- Mutex lock solitamente più leggeri dei semafori contatori e binari
- Per il controllo di accesso a risorse multiple più appropriati i semafori contatori
- Solitamente strutture di più alto livello come i monitor hanno maggiore overhead

---

## Pagina 177

Deadlocks

---

## Pagina 178

Deadlocks

- Modello di Sistema
- Caratterizzazione dei deadlock
- Metodi di gestione dei deadlock
- Prevenzione deadlock
- Evitamento deadlock
- Rilevamento deadlock
- Ripristino dai deadlock

---

## Pagina 179

Obiettivi

- Descrivere i deadlock, che impediscono ad un insieme di thread di eseguire il loro compito
- Presentare metodi per prevenire, identificare, evitare, recuperare i deadlock

---

## Pagina 180

Esempio in Posix

□ Esempio di due thread in deadlock con mutex Posix

```c
pthread_mutex_t first_mutex;
pthread_mutex_t second_mutex;

pthread_mutex_init(&first_mutex, NULL);
pthread_mutex_init(&second_mutex, NULL);
```

```c
/* thread_one runs in this function */
void *do_work_one(void *param)
{
    pthread_mutex_lock(&first_mutex);
    pthread_mutex_lock(&second_mutex);
    /**
     * Do some work
     */
    pthread_mutex_unlock(&second_mutex);
    pthread_mutex_unlock(&first_mutex);

    pthread_exit(0);
}

/* thread_two runs in this function */
void *do_work_two(void *param)
{
    pthread_mutex_lock(&second_mutex);
    pthread_mutex_lock(&first_mutex);
    /**
     * Do some work
     */
    pthread_mutex_unlock(&first_mutex);
    pthread_mutex_unlock(&second_mutex);

    pthread_exit(0);
}
```

---

## Pagina 181

Livelock

- Altra forma di fallimento di Liveness
- Un gruppo di thread non bloccato ma non procede
  - Continuo tentativo di eseguire un’azione che fallisce ed impedisce di avanzare
  - Es. Due persone in un corridoio che non riescono ad evitarsi

```c
/* thread_one runs in this function */
void *do_work_one(void *param)
{
    int done = 0;

    while (!done) {
        pthread_mutex_lock(&first_mutex);
        if (pthread_mutex_trylock(&second_mutex)) {
            /**
             * Do some work
             */
            pthread_mutex_unlock(&second_mutex);
            pthread_mutex_unlock(&first_mutex);
            done = 1;
        }
        else
            pthread_mutex_unlock(&first_mutex);
    }

    pthread_exit(0);
}

/* thread_two runs in this function */
void *do_work_two(void *param)
{
    int done = 0;

    while (!done) {
        pthread_mutex_lock(&second_mutex);
        if (pthread_mutex_trylock(&first_mutex)) {
            /**
             * Do some work
             */
            pthread_mutex_unlock(&first_mutex);
            pthread_mutex_unlock(&second_mutex);
            done = 1;
        }
        else
            pthread_mutex_unlock(&second_mutex);
    }

    pthread_exit(0);
}
```

In alcuni casi si può risolvere con randomizzazione (es. periodo backoff in protocolli di rete)

---

## Pagina 182

Caratterizzazione Deadlock

Un deadlock avviene se le seguenti proprietà sono verificate contemporaneamente (condizioni di Coffman)

- **Mutual exclusion**: almeno una risorsa deve essere tenuta in modalità esclusiva: solo un processo alla volta può usare la risorsa
- **Hold and wait**: almeno un thread deve mantenere almeno una risorsa ed essere in attesa di avere una risorsa aggiuntiva tenuta da altri processi
- **No preemption**: le risorse non possono essere prelazionate - una risorsa può essere rilasciata solo dal processo che la detiene dopo che tale processo ha completato il suo task
- **Circular wait**: esiste un insieme $\{P_0, P_1, \ldots, P_n\}$ di processi in attesa mutua, tali che $P_0$ è in attesa di una risorsa che è tenuta da $P_1$, $P_1$ attende la risorsa di $P_2$, …, $P_{n-1}$ attende la risorsa di $P_n$, e $P_n$ attenda la risorsa di $P_0$.

Le condizioni non sono tutte indipenenti (ultima implica hold and wait), ma è utile considerarle tutte

---

## Pagina 183

Modello del Sistema

- I sistemi forniscono risorse
- Tipi di risorse $R_1, R_2, \ldots, R_m$
  - Cicli CPU, spazio di memoria, dispositivi I/O
- Ogni tipo di risorsa $R_i$ ha $W_i$ istanze.
- Ogni processo utilizza una risorsa come segue:
  - request
  - use
  - release

---

## Pagina 184

Grafo di Allocazione delle Risorse

Insieme di nodi $V$ e insieme di archi $E$.

- $V$ partizionata in due tipi:
  - $P = \{P_1, P_2, \ldots, P_n\}$, insieme di tutti i processi nel sistema
  - $R = \{R_1, R_2, \ldots, R_m\}$, insieme di tutti i tipi di risorse del sistema

- request edge – archi diretti $P_i \rightarrow R_j$
- assignment edge – archi diretti $R_j \rightarrow P_i$

---

## Pagina 185

Grafo di Allocazione delle Risorse

□ Processo

□ Tipo di risorsa con 4 istanze

□ $P_i$ richiede istanza di $R_j$

□ $P_i$ detiene un’istanza di $R_j$

---

## Pagina 186

Esempio di un Grafo di Allocazione di Risorse

Senza cicli non c’è deadlock

Deadlock?

$T = \{T_1, T_2, T_3\}$
$R = \{R_1, R_2, R_3, R_4\}$
$E = \{T_1 \rightarrow R_1, T_2 \rightarrow R_3, R_1 \rightarrow T_2, R_2 \rightarrow T_2, R_2 \rightarrow T_1, R_3 \rightarrow T_3\}$

---

## Pagina 187

Esempio di un Grafo di Allocazione di Risorse

Senza cicli non c’è deadlock

Ciclo è condizione necessaria ma non sufficiente

Se risorse uniche?

- $T = \{T_1, T_2, T_3\}$
- $R = \{R_1, R_2, R_3, R_4\}$
- $E = \{T_1 \rightarrow R_1, T_2 \rightarrow R_3, R_1 \rightarrow T_2, R_2 \rightarrow T_2, R_2 \rightarrow T_1, R_3 \rightarrow T_3\}$

---

## Pagina 188

Grafo di Allocazione di Risorse con un Deadlock

Si introduca un ciclo Deadlock?

$$T_1 \rightarrow R_1 \rightarrow T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_1$$
$$T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_2$$

---

## Pagina 189

Grafo di Allocazione di Risorse con un Deadlock

Si introduca un ciclo

I tre thread sono in deadlock

$$T_1 \rightarrow R_1 \rightarrow T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_1$$
$$T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_2$$

---

## Pagina 190

Grafo con un ciclo ma senza deadlock

... anche in questo caso ciclo

Deadlock?

---

## Pagina 191

Grafo con un ciclo ma senza deadlock

… anche in questo caso ciclo

Deadlock?

P₄ può rilasciare R₂ rompendo il ciclo per consentire a P₃ l’esecuzione

---

## Pagina 192

Fatti di Base

□ Se il grafo non ha cicli ⇒ non ha deadlock
□ Se il grafo contiene un ciclo ⇒
  □ Se esiste una sola istanza per tipo di risorsa, allora deadlock
  □ Se molte istanze per tipo di risorsa, c’è possibilità di un deadlock, ma non si ha necessariamente il deadlock

---

## Pagina 193

Metodi di Gestione Deadlocks

Approcci al problema della gestione del deadlock

- Ignorare il problema assumendo che i deadlocks non si presentino mai nel sistema;
  - usato dalla maggior parte dei sistemi operativi, incluso UNIX

- Assicurare che il sistema non entri mai in un deadlock state:
  - Prevenzione di deadlock (deadlock prevention)
    - Limitare i modi in cui si fanno le richieste per evitare i deadlock
  - Evitamento del deadlock (deadlock avoidance)
    - Valutare le richieste per evitare situazioni pericolose

- Permettere al sistema di entrare in una stato di deadlock per poi recuperare (deadlock recovery)

---

## Pagina 194

Prevenzione Deadlock

Limitare i modi in cui può essere fatta la richiesta tenendo presente le condizioni di deadlock

□ Mutual Exclusion – non richiesta per risorse condivisibili (e.g., read-only files)
  □ .. però non si possono limitare le richieste solo a risorse non condivisibili

□ Hold and Wait – deve garantire che quando un processo richiede una risorsa, non detiene altre risorse
  □ Imporre al processo di richiedere e allocare tutte le sue risorse prima che inizi l'esecuzione
  □ Consentire al processo di richiedere risorse solo quando al processo non ne è stata allocata alcuna, le usa e le rilascia
  □ Non pratico: basso utilizzo delle risorse; possibile starvation

---

## Pagina 195

Prevenzione Deadlock

Non cosentire prelazione di risorse –

Se un processo che detiene risorse richiede un’altra risorsa che non può essere immediatamente data allora tutte le risorse devono essere rilasciate
► Le risorse prelazionate sono aggiunte alla lista delle risorse per le quali il processo è in attesa
► Il processo verrà riavviato solo quando può ottenere le vecchie più le nuove risorse

Oppure si cercano le risorse tra quelle di processi in attesa (che si possono prelazionare)

Può funzionare solo per risorse facilmente recuperabili (CPU, registry, DB, etc.), non per mutex o semafori

Attesa circolare –

imponi un ordine totale a tutti i tipi di risorse e richiedi che ogni processo richieda le risorse in un ordine di enumerazione crescente

Date le risorse $R = \{R_1, R_2, ..., R_m\}$ si assegna un numero di ordine $F(R)$

Un processo può richiedere risorse solo rispettando l’ordine delle risorse
► Se nuova risorsa $F(R_j) > F(R_i)$

---

## Pagina 196

Prevenzione Deadlock

Attesa circolare –

□ imponi un ordine totale a tutti i tipi di risorse e richiedi che ogni processo richieda le risorse in un ordine di enumerazione crescente

□ Date le risorse si assegna un numero di ordine F(R)

□ Un processo può richiedere risorse solo rispettando l’ordine delle risorse

► Se nuova risorsa

$$R = \{R_1, R_2, \ldots, R_m\}$$

$$F(R_j) > F(R_i)$$

Dato un ordine totale $F$ sulle risorse, si assuma che ogni processo richieda risorse in ordine crescente rispetto a $F$.

Se esistesse un ciclo $P_1 \rightarrow P_2 \rightarrow \cdots \rightarrow P_n \rightarrow P_1$, allora

$$F(R_1) < F(R_2) < \cdots < F(R_n) < F(R_1),$$

che contraddice la transitività e l’anti-riflessività di $F$.

---

## Pagina 197

Esempio Deadlock

```c
/* thread one runs in this function */
void *do_work_one(void *param)
{
    pthread_mutex_lock(&first_mutex);
    pthread_mutex_lock(&second_mutex);
    /** * Do some work */
    pthread_mutex_unlock(&second_mutex);
    pthread_mutex_unlock(&first_mutex);
    pthread_exit(0);
}

/* thread two runs in this function */
void *do_work_two(void *param)
{
    pthread_mutex_lock(&second_mutex);
    pthread_mutex_lock(&first_mutex);
    /** * Do some work */
    pthread_mutex_unlock(&first_mutex);
    pthread_mutex_unlock(&second_mutex);
    pthread_exit(0);
}
```

---

## Pagina 198

Esempio Deadlock

```c
/* thread one runs in this function */
void *do_work_one(void *param)
{
    pthread_mutex_lock(&first_mutex);
    pthread_mutex_lock(&second_mutex);
    /** * Do some work */
    pthread_mutex_unlock(&second_mutex);
    pthread_mutex_unlock(&first_mutex);
    pthread_exit(0);
}

/* thread two runs in this function */
void *do_work_two(void *param)
{
    pthread_mutex_lock(&second_mutex);
    pthread_mutex_lock(&first_mutex);
    /** * Do some work */
    pthread_mutex_unlock(&first_mutex);
    pthread_mutex_unlock(&second_mutex);
    pthread_exit(0);
}
```

$$F(\text{first\_mutex}) = 1$$
$$F(\text{second\_mutex}) = 5$$

Occorre un lock-ordering

if (F(first_mutex) < F(second_mutex))
{
    lock(first_mutex);
    lock(second_mutex);
} else {
    lock(second_mutex);
    lock(first_mutex);
}
```

---

## Pagina 199

Esempio di Deadlock con Lock Ordering

```cpp
void transaction(Account from, Account to, double amount)
{
    mutex lock1, lock2;
    lock1 = get_lock(from);
    lock2 = get_lock(to);
    acquire(lock1);
    acquire(lock2);
    withdraw(from, amount);
    deposit(to, amount);
    release(lock2);
    release(lock1);
}
```

Transaction 1 e 2 eseguite concurrentemente. Transaction 1 transferisce $25 da A a B mentre Transaction 2 transferisce $50 da B ad A

```cpp
transaction(checking_account, savings_account, 25.0)
transaction(savings_account, checking_account, 50.0)
```

---

## Pagina 200

Esempio di Deadlock con Lock Ordering

```cpp
void transaction(Account from, Account to, double amount)
{
    mutex lock1, lock2;
    lock1 = get_lock(from);
    lock2 = get_lock(to);
    acquire(lock1);
    acquire(lock2);
    withdraw(from, amount);
    deposit(to, amount);
    release(lock2);
    release(lock1);
}
```

Occorre un lock-ordering globale

```cpp
if (from.id < to.id) {
    acquire(lock(from));
    acquire(lock(to));
} else {
    acquire(lock(to));
    acquire(lock(from));
}
```

Transaction 1 e 2 eseguite concorrentemente. Transaction 1 transferisce $25 da A a B mentre Transaction 2 transferisce $50 da B ad A

```cpp
transaction(checking_account, savings_account, 25.0)
transaction(savings_account, checking_account, 50.0)
```

---

## Pagina 201

Deadlock Avoidance

Il Sistema deve avere informazione a priori addizionale:

- Il modello più semplice ed utile richiede ai processi di dichiarare il massimo numero di risorse necessarie per tipo di processo
- L’algoritmo di deadlock-avoidance esamina dinamicamente lo stato di allocazione delle risorse per assicurare che non si entri mai in una situazione di circular-wait
- Lo stato di allocazione delle risorse (resource-allocation state) è dato dal numero di risorse disponibile e allocate, e dale massime richieste per processo

---

## Pagina 202

Stato Sicuro

- Quando un processo richiede una risorsa disponibile, il sistema deve decidere se l’allocazione immediata lascia il sistema in uno stato sicuro

- Un sistema è in uno **stato sicuro** se esiste una sequenza $<P_1, P_2, \ldots, P_n>$ di TUTTI i processi nel sistema tali che per ogni $P_i$, le risorse che $P_i$ può ancora richiedere possono essere soddisfatte dalle risorse correntemente disponibili + le risorse tenute da tutti i $P_j$, con $j < i$

- Cioè:
  - Se le risorse richieste da $P_i$ non sono immediatamente disponibili, allora $P_i$ può apettare finché tutti i $P_j$ hanno finito
  - Quando $P_j$ ha finito, $P_i$ può ottenere le risorse richieste, eseguirle, rilasciando le risorse allocate e terminare
  - Quando $P_i$ termina, $P_{i+1}$ può ottenere le risorse necessarie, e così via ...

---

## Pagina 203

Stato Sicuro

□ Esempio: 12 risorse e 3 thread

| | Maximum Needs | Current Needs |
| :--- | :--- | :--- |
| $T_0$ | 10 | 5 |
| $T_1$ | 4 | 2 |
| $T_2$ | 9 | 2 |

□ Il Sistema è in stato sicuro
□ Allocate 9 ne rimangono 3
□ La sequenza $<T_1, T_0, T_2>$ soddisfa il requisite
  ▶ T1 ne prende 2 e restituisce 4
  ▶ T0 ne prende 5 e restituisce 10
  ▶ T2 ne prende 7 e finisce

□ Se invece si alloca a T2 un’ulteriore risorsa al tempo t1 lo stato non è più safe

---

## Pagina 204

Fatti di Base

- Se un sistema è in stato sicuro ⇒ non deadlock
- Se un sistema è in stato non sicuro ⇒ possibilità di deadlock
- Evitamento ⇒ assicurare che un sistema non entri mai in uno stato non sicuro

---

## Pagina 205

Safe, Unsafe, Deadlock State

deadlock

unsafe

safe

---

## Pagina 206

Algoritmo di Avoidance

- Singola istanza di un tipo di risorsa
  - Usa un resource-allocation graph

- Multiple istanze di tipo di risorsa
  - Usa l’algoritmo del banchiere

---

## Pagina 207

Schema con grafo di allocazione

- Si introduce la claim edge $P_i \rightarrow R_j$ che indica che il processo $P_j$ potrebbe richiedere la risorsa $R_j$; (linea tratteggiata)
- La claim edge si converte in request edge quando un processo richiede la risorsa
- La request edge si converte in assignment edge quando la risorsa è allocata al processo
- Quando la resource è rilasciata dal processo, l’assignment edge si riconverte in claim edge
- Le risorse devono essere richieste a priori nel sistema

---

## Pagina 208

Resource-Allocation Graph

assignment edge
request edge
claim edge
claim edge

---

## Pagina 209

Stato unsafe in Resource-Allocation Graph

- assignment edge
- request edge
- claim edge
- assignment edge

---

## Pagina 210

Algoritmo di Resource-Allocation Graph

- Supponi che il processo $P_i$ richieda una risorsa $R_j$
- La richiesta può essere garantita solo se trasformando l’arco di richiesta in un assegnamento non porta alla formazione di un ciclo nel grafo di allocazione delle risorse
- Altrimenti la richiesta viene messa in attesa
- Complessità di rilevare un ciclo è n^2 con n numero di thread del sistema

---

## Pagina 211

Algoritmo del Banchiere

- Allocazione delle risorse della banca per soddisfare tutti i clienti
- Applicabile per multiple istanze
- Ogni processo deve dichiarare a priori il massimo utilizzo di risorse
- Quando un processo richiede una risorsa potrebbe dover aspettare
- Quando un processo ottiene tutte le sue risorse deve restituirle in un tempo finito

---

## Pagina 212

Algoritmo del Banchiere

- Quando un processo richiede un insieme di risorse, il Sistema deve controllare se l’assegnazione lascia il Sistema in uno stato sicuro

- Se lo stato è sicuro le risorse sono allocate altrimenti la richiesta viene messa in attesa finché qualche processo libera delle risorse aggiuntive

- Si introducono diverse strutture dati per rappresentare lo stato del sistema

---

## Pagina 213

Strutture Dati per l’Algoritmo del Banchiere

Sia $n$ = numero di processi ed $m$ = numero di tipi di risorse.

□ **Available**: Vettore di lunghezza $m$. Se available $[j] = k$, ci sono $k$ istanze della risorsa di tipo $R_j$ disponibili

□ **Max**: matrice $n \times m$. Se $Max[i,j] = k$, allora il processo $P_i$ potrebbe richiedere al massimo $k$ istanze della risorsa di tipo $R_j$

□ **Allocation**: matrice $n \times m$. Se Allocation[i,j] = $k$ allora $P_i$ ha correntemente allocate $k$ istanze di $R_j$

□ **Need**: matrice $n \times m$. Se Need[i,j] = $k$, allora $P_i$ potrebbe aver bisogno di $k$ più istanze di $R_j$ per complare il suo task

$$Need[i,j] = Max[i,j] - Allocation[i,j]$$

---

## Pagina 214

Esempio Stato Sicuro

□ Esempio precedente: 12 risorse (tutte di un tipo) e 3 thread
□ Matrici Max e Allocation

| | Maximum Needs | Current Needs |
| :--- | :--- | :--- |
| $T_0$ | 10 | 5 |
| $T_1$ | 4 | 2 |
| $T_2$ | 9 | 2 |

□ Il Sistema era in stato sicuro
□ Allocate 9 rimangono 3
□ La sequenza $<T_1, T_0, T_2>$ soddisfa il requisite

---

## Pagina 215

Esempio Algoritmo Banchiere

□ 5 processi da $P_0$ a $P_4$;
3 tipi di risorse:
A (10 istanze), B (5 istanze) e C (7 istanze)

□ Stato al tempo $T_0$:

| | Allocation | Max | Available |
| :--- | :--- | :--- | :--- |
| | A B C | A B C | A B C |
| $P_0$ | 0 1 0 | 7 5 3 | 3 3 2 |
| $P_1$ | 2 0 0 | 3 2 2 | |
| $P_2$ | 3 0 2 | 9 0 2 | |
| $P_3$ | 2 1 1 | 2 2 2 | |
| $P_4$ | 0 0 2 | 4 3 3 | |

---

## Pagina 216

Algoritmo di Safety

1. Siano Work e Finish vettori di lunghezza $m$ (risorse) ed $n$ (processi), rispettivamente. Inizializza:
   Work = Available
   Finish $[i] = \text{false}$ for $i = 0, 1, \dots, n-1$

2. Trova un indice $i$ tale che entrambi:
   (a) Finish $[i] = \text{false}$
   (b) Need$_i \leq \text{Work}$
   Se non esiste $i$, vai al passo 4

3. Work = Work + Allocation$_i$
   Finish$[i] = \text{true}$
   vai al passo 2

   Trova un processo per cui le assegnazioni non siano state soddisfatte

4. Se Finish $[i] == \text{true}$ per tutti gli $i$, allora il sistema è in uno stato sicuro (safe state)

L’algoritmo verifica se lo stato è sicuro e può richiedere un ordine di $m \times n^2$ operazioni

---

## Pagina 217

Algoritmo di Richiesta di Risorsa per il Processo $P_i$

Algoritmo per deteriminare se una richiesta può essere accordata in sicurezza

$Request_i =$ vettore richieste per il processo $P_i$.

Se $Request_i[j] = k$ allora il processo $P_i$ vuole $k$ istanze delle risorse di tipo $R_j$

1. Se $Request_i \leq Need_i$ vai al passo 2. Altrimenti, segnala la condizione di errore dal momento che il processo ha superato il suo massimo dichiarato
2. Se $Request_i \leq Available$ vai al passo 3. Altrimenti $P_i$ deve aspettare perché le risorse non sono disponibili
3. Prova ad allocare le risorse richieste per $P_i$ modificando lo stato come segue:

$$Available = Available - Request_i;$$
$$Allocation_i = Allocation_i + Request_i;$$
$$Need_i = Need_i - Request_i;$$

- Verifica se safe
- Se safe $\Rightarrow$ le risorse sono allocate a $P_i$
- Se unsafe $\Rightarrow P_i$ deve aspettare e il vecchio stato di allocazione delle risorse viene recuperato

---

## Pagina 218

Esempio Algoritmo Banchiere

□ 5 processi da $P_0$ a $P_4$;
3 tipi di risorse:
A (10 istanze), B (5 istanze) e C (7 istanze)

□ Stato al tempo $T_0$:

| | Allocation | Max | Available |
| :--- | :--- | :--- | :--- |
| | A B C | A B C | A B C |
| $P_0$ | 0 1 0 | 7 5 3 | 3 3 2 |
| $P_1$ | 2 0 0 | 3 2 2 | |
| $P_2$ | 3 0 2 | 9 0 2 | |
| $P_3$ | 2 1 1 | 2 2 2 | |
| $P_4$ | 0 0 2 | 4 3 3 | |

---

## Pagina 219

Esempio

□ Il contenuto della matrice *Need* è definite come *Max – Allocation*

$$\begin{array}{c}
\text{Need} \\
\text{A B C} \\
P_0 & 7 4 3 \\
P_1 & 1 2 2 \\
P_2 & 6 0 0 \\
P_3 & 0 1 1 \\
P_4 & 4 3 1
\end{array}$$

□ Il Sistema è in un stato sicuro (safe state) perché la sequenza $< P_1, P_3, P_4, P_2, P_0>$ soddisfa i criteri di safety

---

## Pagina 220

Esempio

Il contenuto della matrice *Need* è definite come *Max – Allocation*

| Need | Available |
| :--- | :--- |
| $P_0$ | 7 4 3 |
| $P_1$ | 1 2 2 |
| $P_2$ | 6 0 0 |
| $P_3$ | 0 1 1 |
| $P_4$ | 4 3 1 |

- Per $P_1$ la Need $\leq$ Work e Finish[1] = F
- Work = Work + Allocation[1] = 4 5 2, Finish[1] = T
- Per $P_3$ la Need $\leq$ Work e Finish[3] = F
- Work = Work + Allocation[3] = 4 6 3, Finish[1] = T
- ...

---

## Pagina 221

Esempio: $P_1$ Richiede (1,0,2)

- Controlla che Request ≤ Available (cioè, $(1,0,2) \leq (3,3,2) \Rightarrow$ true

| Allocation | Need | Available |
| :--- | :--- | :--- |
| A B C | A B C | A B C |
| $P_0$ | 0 1 0 | 7 4 3 | 2 3 0 |
| $P_1$ | 3 0 2 | 0 2 0 | |
| $P_2$ | 3 0 2 | 6 0 0 | |
| $P_3$ | 2 1 1 | 0 1 1 | |
| $P_4$ | 0 0 2 | 4 3 1 | |

- Eseguendo l’algoritmo di safety si vede che la sequenza $< P_1, P_3, P_4, P_0, P_2>$ soddisfa i criteri

- Può la richiesta per (3,3,0) di $P_4$ essere garantita?

- Può la richiesta per (0,2,0) di $P_0$ essere garantita?

---

## Pagina 222

Rilevazione Deadlock

- Permetti al sistema di entrare nello stato di deadlock
- Servono quindi:
  - Algoritmi di deadock detection
  - Metodi di deadlock recovery
- Costi:
  - Costo del monitoraggio (strutture dati ed algoritmi)
  - Potenziale perdita di dati durante il recovery
- Cosideriamo due casi:
  - Istanza singola di risorsa
  - Istanze multiple di risorsa

---

## Pagina 223

Istanza Singola di Ogni Tipo di Risorsa

- Si usa una variante del grafo di allocazione delle risorse chiamato grafo wait-for (grafo delle attese)
  - Si rimuovono i nodi delle risorse che si bypassano con archi tra processi
  - Nodi sono solo per i processi
  - $P_i \rightarrow P_j$ se $P_i$ sta aspettando $P_j$

---

## Pagina 224

Grafo di Allocazione delle e Grafo delle Attese

Grafo di allocazione delle risorse

Grafo delle Attese corrispondente

---

## Pagina 225

Istanza Singola di Ogni Tipo di Risorsa

□ Si usa una variante del grafo di allocazione chiamato grafo wait-for (grafo delle attese)
  □ Si rimuovono i nodi delle risorse che si bypassano con archi tra processi
  □ Nodi sono solo processi
  □ $P_i \rightarrow P_j$ se $P_i$ sta aspettando $P_j$

□ Periodicamente invoca un algoritmo che cerca i cicli nel grafo. Se c’è ciclo allora c’è un deadlock

□ Un algoritmo per rilevare un ciclo in un grafo richiede un ordine di $n^2$ operazioni, dove $n$ è il numero di vertici nel grafo

□ Esempio
  □ BCC toolkit su Linux mette a disposizione un deadlock_detector che traccia l’uso dei pthread_mutex_lock e pthread_mutex_unlock costruendo un grafo delle attese e segnalando i deadlock

---

## Pagina 226

Molte Istanze di un Tipo di Risorsa

Nel caso di più istanze occorrono più strutture dati come per l’algoritmo del banchiere

□ Available: un vettore di lunghezza $m$ che indica il numero di risorse disponibili per ogni tipo di risorsa

□ Allocation: una matrice $n \times m$ definisce il numero di risorse per tipo correntemente allocato ad ogni processo

□ Request: una matrice $n \times m$ indica la richiesta corrente di ogni processo. Se $Request[i][j] = k$, allora il processo $P_i$ sta richiedendo $k$ più istanze di risorsa di tipe $R_j$.

---

## Pagina 227

Algoritmo di Rilevamento

1. Siano Work e Finish vettori di lunghezza $m$ ed $n$
Inizializza:
(a) Work = Available
(b) For $i = 1,2, \ldots, n$, if Allocation$_i \neq 0$, then Finish[i] = false; otherwise, Finish[i] = true

2. Trova un indice $i$ tale che entrambi:
(a) Finish[i] == false
(b) Request$_i \leq Work$

Se non esiste tale $i$, vai al passo 4

---

## Pagina 228

Algoritmo di Rilevamento

3. Work = Work + Allocationᵢ
Finish[i] = true
vai al passo 2

Rilasciate le risorse dopo il completamento, si assume che non siano necessarie altre risorse da allocare per finire il processamento

4. Se Finish[i] == false, per qualche $i$, $1 \leq i \leq n$, allora il sistema è in uno stato di deadlock. Inoltre, se Finish[i] == false, allora $P_i$ è in deadlocked

Algoritmo richiede un ordine di $O(m \times n^2)$ operazioni per rilevare se il sistema è in stato di deadlock

---

## Pagina 229

Esempio di Algoritmo di Rilevamento

□ Cinque processi da $P_0$ a $P_4$; tre tipi di risorsa
A (7 istanze), B (2 istanze), and C (6 istanze)

□ Stato al tempo $T_0$:

| | Allocation | Request | Available |
| :--- | :---: | :---: | :---: |
| $P_0$ | 0 1 0 | 0 0 0 | 0 0 0 |
| $P_1$ | 2 0 0 | 2 0 2 | |
| $P_2$ | 3 0 3 | 0 0 0 | |
| $P_3$ | 2 1 1 | 1 0 0 | |
| $P_4$ | 0 0 2 | 0 0 2 | |

□ La sequenza $<P_0, P_2, P_3, P_1, P_4>$ porterà a *Finish[i] = true* per tutti le $i$

---

## Pagina 230

Esempio

- $P_2$ richiede un’istanza addizionale di tipo $C$
  - Request
    - A B C
    - $P_0$ 0 0 0
    - $P_1$ 2 0 2
    - $P_2$ 0 0 1
    - $P_3$ 1 0 0
    - $P_4$ 0 0 2

- Stato del sistema?
  - Può rilasciare le risorse tenute dal processo $P_0$, ma le risorse sono insufficienti per soddisfare le richieste degli altri processi
  - Esiste un deadlock per i processi $P_1$, $P_2$, $P_3$, e $P_4$

---

## Pagina 231

Uso dell’Algoritmo di Rilevamento

□ Quanto spesso invocare il rilevamento?
□ Dipende da:
  □ Quanto spesso un deadlock è probabile che avvenga?
    ► Se frequente va invocato frequentemente
  □ Può coinvolgere più processi?
    ► Nel caso estremo può essere invocato ogni volta che una richiesta non può essere soddisfatta
    ► In questo caso si può identificare anche chi ha causato il deadlock
    ► Però dispendioso, quindi check ad intervalli fissi
  □ Quanti processi sarà necessario recuperare?
    ► uno per ogni ciclo disgiunto

□ Se l’algoritmo di detection invocato ad intervalli definiti (o quando l’uso della CPU va sotto una soglia definita)
  □ possibili molti cicli nel grafo delle risorse
    ► complicato risalire a quali dei tanti processi abbia “causato” il deadlock.

---

## Pagina 232

Ripristino dal Deadlock

- Quando viene trovato un deadlock va gestito:
  - Avvertire operatore che gestisce a mano
  - Gestione automatica

- Due modalità principali di gestione:
  - Terminare uno o più processi coinvolti
  - Prelazionare risorse dai processi coinvolti nel deadlock

---

## Pagina 233

Ripristino dal Deadlock: Terminazione di Processo

Terminazione

- Abort di tutti i processi in deadlock
  - Molto dispendioso tutta la computazione persa
- Abort dei processi, uno alla volta finché il ciclo di deadlock cycle è eliminato
  - Invocato il deadlock check ad ogni passo (overhead)

In quale ordine dovremmo sceglili per fare l’abort?
- Si dovrebbe scegliere il costo minimo, ma diversi criteri:
  1. Priorità del processo
  2. Per quanto tempo ha lavorato e quanto manca al completamento
  3. Quante e quali risorse il processo ha già usato (si possono prelazionare?)
  4. Quante risorse il processo necessita per completare
  5. Quanti processi necessiteranno di essere terminati
  6. È un processo interattivo o batch

---

## Pagina 234

Ripristino dal Deadlock: Prelazione di Risorse

□ Si selezionano risorse da prelazionare finché il deadlock non è risolto

□ Per la selezione della risorsa occorre:

□ **Selezionare una vittima** – quale risorsa e quale processo prelazionare?
  ► Minimizza il costo: il numero di risorse trattenute, il tempo di computazione impiegato, etc.

□ **Rollback** – se prelazionata risorsa da un processo che farne del processo?
  ► Deve ritornare in qualche safe state e ripartire da quello stato. Metodo più semplice ripartire da capo. Altrimenti da stato intermedio di computazione, però va mantenuto.

□ **Starvation** – come evitare lo starvation?
  ► Se c’è una cost function per la scelta, sempre lo stesso processo può essere scelto come vittima. Per evitarlo si può includere il numero dei rollback nei fattori di costo

---

## Pagina 235

Riassunto

- Definizione di deadlock
- Condizioni per avere un deadlock
- Grafi di allocazione delle risorse e cicli
- Prevenzione dei deadlock in base alle condizioni di deadlock
- Metodi di evitamento del deadlock per risorse singole (grafo delle allocazioni) e multiple (algoritmo del banchiere)
- Metodi di deadlock detection per risorse singole e multiple
- Metodi di deadlock recovery

---

## Pagina 236

Memoria Principale

---

## Pagina 237

Obiettivo

- Fornire una descrizione dettagliata dei modi di organizzare l'hardware di memoria
- Discutere le tecniche di gestione della memoria, inclusi il paging e la segmentazione

---

## Pagina 238

Background

- Un sistema di elaborazione esegue programmi
- Per essere eseguito un programma deve essere portato (dal disco) in memoria principale e inserito all'interno di un processo
- La memoria principale ed i registri sono la sola memoria a cui la CPU accede direttamente interpretando le istruzioni dei programmi
- Tanti processi devono essere caricati (almeno parzialmente) in memoria contemporaneamente

- La CPU carica le istruzioni indicate dal PC, decodifica ed esegue
- La memoria principale può essere vista come un grande array di bytes con indirizzi
- L'unità di memoria vede solo un flusso di indirizzi + richieste di lettura o indirizzo + dati e richieste di scrittura

---

## Pagina 239

Hardware

□ La memoria principale ed i registri sono la sola memoria a cui la CPU accede direttamente interpretando le istruzioni

□ Supporto hardware per velocizzare l’accesso:
  □ L'accesso ai registri generalmente in un clock della CPU (in alcuni casi più operazioni in un ciclo)
  □ La memoria principale può richiedere molti cicli (memory bus), causando uno stallo in attesa del dato da elaborare
  □ Accesso frequente, troppi stalli
  □ Cache tra la memoria principale e i registri della CPU per accelerare

□ Protezioni hardware:
  □ Necessaria protezione hardware della memoria per garantirne il corretto funzionamento (proteggere sistema e utenti)
  □ Il Sistema non interviene tra CPU e Memoria per non rallentare

---

## Pagina 240

Protezione: Registri Base e Limite

- In primo luogo occorre separare i processi in memoria
- Una coppia di registi CPU base e limite definisce lo spazio degli indirizzi logici per un processo
  - Base il primo indirizzo fisico, limite il range
- La CPU deve controllare ogni accesso in memoria in user mode per verificare che sia tra gli indirizzi base e limite per quel processo

Soluzione CDC 6600
Intel 8088 (non limite),
Intel 80286

---

## Pagina 241

Protezione: Registri Base e Limite

- In primo luogo occorre separare i processi in memoria
- Una coppia di registi CPU base e limite definisce lo spazio degli indirizzi logici per un processo
- Base il primo indirizzo fisico, limite il range

---

## Pagina 242

Protezione hardware degli indirizzi

Il controllo di accesso è hardware, se violato l’accesso si genera un trap che il Sistema Operativo considera come fatal error

I registri possono essere caricati solo dal SO in modalità privilegiata, quindi solo in kernel mode

In kernel mode il SO ha accesso non ristretto sia alla memoria di SO sia a quella degli utenti

图示：CPU处理地址判断逻辑
- CPU处理地址判断逻辑
  - base
    - yes
    - no
  - base + limit
    - yes
    - no
- trap to operating system monitor—addressing error

---

## Pagina 243

Programmi e Processi

- Programmi su disco
  - file eseguibili pronti per caricamento ed esecuzione

- Programma caricato in memoria
  - La CPU può accedere a dati ed istruzioni
  - Il processo può risiedere in ogni parte della memoria

- Processo termina
  - lo spazio di memoria viene reso disponibile

---

## Pagina 244

Processamento Multistep di Programma Utente

Un programma utente, prima di essere eseguito, deve passare attraverso varie fasi (alcune facoltative)

gcc –E file.c
preprocessa ma non compila file.i

gcc –S file.c
compila ma non assembla (assembly) file.s

gcc –c file.c
compila e assembla non linka (file oggetto) file.o

---

## Pagina 245

Binding di Istruzioni e Dati alla Memoria

□ Il binding (degli indirizzi di istruzioni e dati) agli indirizzi di memoria può avvenire in diverse fasi

□ Tempo di Compilazione: se al momento della compilazione è già noto dove il processo risiederà in memoria si può generare codice assoluto, il codice va quindi ricompilato se la locazione di partenza viene modificate

□ Tempo di Caricamento: si genera codice rilocabile se la locazione di memoria non è nota a tempo di compilazione; il collegamento finale viene ritardata finché non c’è il caricamento (loader). Se la locazione iniziale per il processo cambia occorre ricaricare il codice.

□ Tempo di Esecuzione: se durante l’esecuzione il processo può essere spostato da un segmento di memoria all’altro allora il binding è ritardato fino al run-time
  ► Occorre supporto hardware speciale per mappare gli indirizzi
  ► La maggior parte dei SO usa questo metodo

---

## Pagina 246

Indirizzi logici e fisici

La separazione tra **indirizzi logici** ed **indirizzi fisici** è centrale per la gestione della memoria

- **Indirizzo logico**
  - generato dalla CPU; anche chiamato **indirizzo virtuale**

- **Indirizzo fisico**
  - indirizzo visto dall’unità di memoria
  - caricato registro di indirizzi di memoria (memory-address register)

Indirizzi logici e fisici:

- **Spazio degli indirizzi logici:** insieme di tutti gli indirizzi logici generati da un programma
- **Spazio degli indirizzi fisici:** insieme di tutti gli indirizzi fisici che corrispondono ad uno spazio di indirizzi logici

---

## Pagina 247

Memory-Management Unit (MMU)

- MMU è un dispositivo hardware che **mappa a run-time** gli indirizzi virtuali in indirizzi fisici
- Diversi schemi di mapping possono essere introdotti
  - Un esempio di schema semplice è basato su registri base e limite
  - In questo caso il registro di base è chiamato **registro di rilocazione**

**Unità di gestione della memoria** (memory management unit, MMU) svolge l’associazione, **nella fase d’esecuzione**, tra indirizzi virtuali e indirizzi fisici

**Figura 9.4** Unità di gestione della memoria (MMU).

---

## Pagina 248

Memory-Management Unit (MMU)

- MMU è un dispositivo hardware che **mappa a run-time** gli indirizzi virtuali in indirizzi fisici
- Diversi schemi di mapping possono essere introdotti
  - Un esempio di schema semplice è basato su registri base e limite
  - In questo caso il registro di base è chiamato **registro di rilocazione**

**Unità di gestione della memoria** (memory management unit, MMU) svolge l’associazione, **nella fase d’esecuzione**, tra indirizzi virtuali e indirizzi fisici

---

## Pagina 249

Memory-Management Unit (MMU)

□ MMU è dispositivo hardware che mappa a run time gli indirizzi virtuali in indirizzi fisici
□ Diversi metodi sono possibili per fare il mapping
□ Un esempio di schema semplice è basato su registri base e limite:
  ► il valore nel registro di relocazione è addizionato all’indirizzo generato dal processo utente
  ► Registro base chiamato ora relocation register

► Es. CPU considera 346 (logico) che viene mappato su 14346
► MS-DOS su Intel 80x86 usava 4 relocation registers

---

## Pagina 250

Memory-Management Unit (MMU)

- MMU è dispositivo hardware che mappa a run-time gli indirizzi virtuali in indirizzi fisici

- Il processo utente vede solo gli indirizzi logici, non vede mai gli indirizzi fisici reali

  - Es. Può gestire un puntatore, manipolarlo etc. rimanendo nello spazio logico
  - Il binding a tempo di esecuzione occorre solo quando si accede ad una locazione di memoria fisica. In questo caso l’hadware per il mapping in memoria converte l’indirizzo virtuale in indirizzo fisico
  - Il processo utente lavora nello spazio di indirizzi logici (es. intervallo [0, max]) che in memoria saranno mappati in indirizzi fisici (es. [R, R + max])

---

## Pagina 251

Allocazione Contigua di Memoria

- La memoria principale deve supportare sia i processi di sistema che di utente
- Memoria principale di solito divisa in due parti:
  - Sistema Operativo residente tenuto in memoria alta o bassa
    - Linux e Win in memoria alta
  - Processi utente in memoria bassa o alta
    - Assumiamo bassa

- Più processi devono essere portati in memoria contemporaneamente
- Allocazione contigua è tra i primi metodi impiegati
  - Processi successivi caricati in sezioni contigue di memoria
    - Ogni processo contenuto in una singola e contigua sezione della memoria
    - Necessari meccanismi di protezione della memoria dei processi

---

## Pagina 252

Protezione

- Registro di rilocazione usato per proteggere i processi utente l’uno dall’altro e per impedire il cambiamento di codice e dati di SO
  - Registro base contiene il valore dell’indirizzo fisico più basso
  - Registro limite contiene il range di indirizzi logici – ogni indirizzo logico deve essere minore del limite
  - MMU mappa dinamicamente gli idirizzi logici
  - Dispatcher carica processo insieme ai registri limite e relocation (contex switch)
  - Anche la dimensione del SO può variare dinamicamente

---

## Pagina 253

Allocazione con Partizioni Multiple

Partizioni multiple di dimensione variabile

- Partizioni di **dimensione variabile** dove ciascuna partizione può contenere esattamente un processo
- Tra i metodi più semplici per l’allocazione della memoria

---

## Pagina 254

Allocazione con Partizioni Multiple

Partizioni multiple di dimensione variabile
- Ciascuna partizione può contenere esattamente un processo

Il SO mantiene traccia delle partizioni occupate
  - Hole – blocco di memoria disponibile
  - Inizialmente tutta la memoria è disponibile (unico hole)
  - Quando un processo arriva, è allocato in un hole largo abbastanza per gestirlo
  - I processi uscenti liberano le partizioni e le partizioni libere adiacenti sono combinate in una sola

Il SO mantiene informazione su:
  a) partizioni allocate
  b) partizioni libere (hole)

Grado di multiprogrammazione limitato dal numero di partizioni disponibili

---

## Pagina 255

Allocazione con Partizioni Multiple

Partizioni multiple di dimensione variabile
- Allocati gli hole dimensionati sui bisogni del processo

- Se non c’è spazio sufficiente il processo può essere respinto o messo in attesa
- Se il buco è grande viene diviso allocandone una parte e rilasciandone una parte libera
- Ma come scegliere gli hole da allocare?

---

## Pagina 256

Problema di Allocazione con Storage Dinamico

Come soddisfare una richiesta di dimensione $n$ da una lista di hole liberi?

☐ First-fit: Alloca il primo hole libero che è grande abbastanza
  ☐ Non deve scandire tutta la lista
  ☐ Può scandire dall’inizio o dall’ultima ricerca

☐ Best-fit: Alloca il più piccolo hole che è grande abbastanza
  ☐ Deve cercare l’intera lista se non ordinata con la dimensione
  ☐ Produce il più piccolo residuo di hole

☐ Worst-fit: Alloca il più largo hole
  ☐ Deve cercare l’intera lista, se non ordinata
  ☐ Produce il più largo residuo di hole

Dalle simulazione si vede che first-fit e best-fit superiori a worst-fit in termini di velocità e utilizzo dello storage

First-fit più veloce, non chiaro invece per quanto riguarda lo storage

---

## Pagina 257

Frammentazione

□ Problemi di frammentazione esterna

□ Frammentazione esterna – esiste memoria totale per soddisfare una richiesta, ma non è contigua
  □ Tanti buchi piccolo non contigui
  □ Con first-fit dati $N$ blocchi allocati, 0.5 $N$ blocchi sono persi per frammentazione
    ► 1/3 può essere non usabile -> 50-percent rule

□ Frammentazione interna – la memoria allocata può essere più grande di quella richiesta
  □ La differenza di dimensione è interna ad una partizione, ma non è usata
  □ Esempio:
    ► Processo richiede 18462 byte ma buco di 18464, troppo piccolo il residuo per tenerne traccia
    ► Per evitare il problema si divide la memoria in blocchi di dimensione fissa, ma allora si alloca più memoria ogni volta (frammentazione interna)

---

## Pagina 258

Frammentazione

La frammentazione esterna si riduce con la compattazione
- Riassegna i contenuti della memoria per mettere insieme tutta la memoria libera in un blocco di grandi dimensioni
- La compattazione è possible se la rilocazione è dinamica ed è fatta a tempo di esecuzione

Un’altra strategia è la paginazione che permettere l’allocazione in locazioni non contigue:
- Il paging è la strategia più usata dai moderni SO

---

## Pagina 259

Paging

- Lo spazio dell’indirizzi fisici di un processo può essere non contiguo
  - Ad un processo è allocata memoria fisica quando è disponibile
  - Si evita la frammentazione esterna
  - Si evita il problema di frammenti di memoria con dimensioni variabili

- Si divide la memoria fisica in blocchi di dimensione fissa detti frame
  - Dimensione potenza di 2, tra 4 KB e 2 GB

- Si divide la memoria logica in blocchi della stessa dimensione detti pagine

- Si tiene traccia di tutti i frame liberi

- Per lanciare un programma di dimensione $N$ pagine, si devono trovare $N$ frame liberi e caricare il programma

- Occorre una page table per tradurre gli indirizzi logici in fisici

- Non risolve problemi di frammentazione interna

---

## Pagina 260

Schema di Traduzione degli Indirizzi

□ L’indirizzo logico generato dalla CPU è diviso in due parti:

□ **Page number (p)** – usato come indice nella **page table** che contiene l’indirizzo base di ogni pagina nella memoria fisica

□ **Page offset (d)** – combinato con l’indirizzo base definisce l’indirizzo di memoria fisica

| page number | page offset |
| :--- | :--- |
| p | d |
| m -n | n |

□ Con spazio degli indirizzi logici di dim 2ᵐ e pagine di dim 2ᵙ

□ Spazio degli indirizzi logici sparato da quello degli indirizzi fisici

---

## Pagina 261

Hardware per il Paging

La MMU esegue i seguenti passi:
- Estrae in numero p di pagina usandolo come indice
- Estrae il frame number f dalla tabella
- Compone l’indirizzo sostituendo f a p

Le pagine con potenza di 2 semplificano l’operazione:
- Se $2^m$ indirizzi logici ed frame di dim $2^n$ allora
- $m - n$ bit per il page number $n$ per l’offset

---

## Pagina 262

Modello di Paging di Memoria Logica e Fisica

logical memory

frame number

0
1
2
3
4
5
6
7

page table

physical memory

---

## Pagina 263

Esempio Paging

Indirizzo logico 0 = pagina 0, offset 0
La pagina 0 è nel frame 5,
quindi 0 logico si mappa in 20 [= (5 × 4) + 0] fisico

Indirizzo logico 3 (pagina 0, offset 3) mappa
nell’indirizzo fisico 23 [= (5 × 4) + 3]

Indirizzo logico 4 è in page 1, offset 0;
page 1 si mappa nel frame 6.
Quindi 4 logico si mappa nel fisico 24 [= (6 × 4) + 0]

n=2 e m=4
memoria 32-byte e pagine 4-byte (8 pagine)

---

## Pagina 264

Paging

□ Con paging si ha solo frammentazione interna
□ Calcolo della frammentazione interna

□ Esempio:
  ▶ Page size = 2,048 bytes
  ▶ Process size = 72,766 bytes
  ▶ 35 pages + 1,086 bytes
  ▶ Frammentazione interna di 2,048 - 1,086 = 962 bytes

□ Frammentazione worst case = 1 frame – 1 byte

□ In media frammentazione = 1 / 2 frame size

□ Quindi piccoli frame desiderabili?
  ▶ … ma ogni entry della page table impegna memoria per tracciarla

□ Le dimensioni delle pagine crescono nel tempo
  ▶ Solaris supporta due dimensioni – 8 KB e 4 MB
  ▶ Win 11 supporta 4 KB, 2 MB, 1 GB
  ▶ Linux supporta default (4 KB) e huge pages

---

## Pagina 265

Paging

Con paging si ha solo frammentazione interna
Le dimensioni delle pagine crescono nel tempo
Linux supporta default (4 KB) e huge pages (def 2 MB)

scrive il valore della conf variable
$getconf PAGESIZE
4096

Statistiche di mem in kb
$grep Huge /proc/meminfo

AnonHugePages: 0 kB
ShmemHugePages: 0 kB
FileHugePages: 0 kB
HugePages_Total: 0
HugePages_Free: 0
HugePages_Rsvd: 0
HugePages_Surp: 0
Hugepagesize: 2048 kB
Hugetlb: 0 kB

---

## Pagina 266

Esercizio

Dato un sistema con uno spazio di indirizzi logici a 14 bit e pagine da 2KB quante entry avrà la tabella delle pagine?

---

## Pagina 267

Esercizio

□ Dato un sistema con uno spazio di indirizzi logici a 14 bit e pagine da 2KB quante entry avrà la tabella delle pagine?

□ Con pagine di 2KB avremo 2^11 B quindi n = 11

□ Cioè 11 bit per offset, dunque rimangono 3 bit per indicare la pagina

□ La tabella delle pagine avrà 2^3 entry

---

## Pagina 268

Esercizio

- Si assuma di avere un sistema con uno spazio degli indirizzi logici di 15 bit e 8 pagine. Quanto sono grandi le pagine del sistema?

---

## Pagina 269

Esercizio

□ Si assuma di avere un sistema con uno spazio degli indirizzi logici di 15 bit e 8 pagine. Quanto sono grandi le pagine del sistema?

□ Pagine 8 = 2^3, cioè 3 bit per rappresentarle
□ Bit di offset 15 – 3 = 12
□ 2^12 byte da indirizzare, cioè pagine da 4 KB (2^2 x 2^10)

---

## Pagina 270

Esercizio

- Sia dato un sottosistema di memoria con paginazione, caratterizzato dalle seguenti dimensioni:
  - Frame di 4 MB e memoria fisica indirizzabile di 128 GB
- Si calcoli il numero di bit minimo per indicizzare tutte le pagine associate

---

## Pagina 271

Esercizio

- Sia dato un sottosistema di memoria con paginazione, caratterizzato dalle seguenti dimensioni:
  - Frame di 4 MB e memoria fisica indirizzabile di 128 GB
- Si calcoli il numero di bit minimo per indicizzare tutte le pagine associate

- Frame 4 MB, quindi 2^2 x 2^20 = 2^22 byte
- Memoria fisica 128 GB = 2^7 x 2^30 = 2^37 byte
- Numero frame = 2^37 / 2^22 = 2^15
- Quindi 15 bit è il numero minimo per indicizzare le pagine

---

## Pagina 272

Frame Liberi

Un processo da eseguire viene valutato in pagine e se richiede $n$ pagine occorrono $n$ frame liberi in memoria. Le pagine sono via via allocate e associate ai frame liberi

Before allocation

After allocation

---

## Pagina 273

Frame Liberi

Un processo da eseguire viene valutato in pagine e se richiede $n$ pagine occorrono $n$ frame liberi in memoria. Le pagine sono via via allocate e associate ai frame liberi

Il Sistema Operativo mantiene una Tabella dei Blocchi per tracciare l’uso della memoria (libera, occupata, assegnazione)

Quando un processo chiede memoria viene consultata la tabella dei blocchi per l’assegnazione

Before allocation

After allocation

---

## Pagina 274

Implementazione della Page Table

- Struttura per-processo con puntatore nel PCB
- Quando un processo va in esecuzione devono essere ricaricati i registi e ricaricati i valori per la gestione della page table
- La page table può essere implementata in vari modi
  - Registri dedicati caricati dal dispatcher della CPU, accesso del SO in modalità privilegiata, richiede gestione context switch, piccola tabella (es. 256 entry)
  - Se più grande (es. $2^{20}$ entry) la page table è mantenuta in memoria principale
    - Page-table base register (PTBR) punta alla page table
    - Page-table length register (PTLR) indica la dim della page table

Diagram showing the CPU, page table, and memory hierarchy. The page table is shown as a stack of horizontal layers with labels for "Tabelle delle pagine" and "Processo in esecuzione". The CPU is at the bottom, with the page table above it. The memory hierarchy is indicated by horizontal layers with labels for "per prelevare un dato dalla memoria sono necessari 2 accessi!!".

---

## Pagina 275

Implementazione della Page Table

- Struttura per-processo con puntatore nel PCB
- Quando un processo va in esecuzione devono essere ricaricati i registi e ricaricati i valori per la gestione della page table
- La page table può essere implementata in vari modi
  - Registri dedicati caricati dal dispatcher della CPU, accesso del SO in modalità privilegiata, richiede gestione context switch, piccola tabella (es. 256 entry)
  - Se più grande (es. $2^{20}$ entry) la page table è mantenuta in memoria principale
    - Page-table base register (PTBR) punta alla page table
    - Page-table length register (PTLR) indica la dim della page table
    - Veloce context switch (cambia il puntatore)
    - Lento accesso a memoria. Ogni accesso a dati/instruzioni richiede due accessi in memoria: uno per la page table ed uno per i dati/instruzioni
    - I due accessi in memoria possono essere risolti utilizzando una cache speciale detta registri associativi o translation look-aside buffers (TLBs)

---

## Pagina 276

Memoria Associativa (TLB)

- Per la traduzione di un indirizzo si cerca prima in memoria associative e poi in memoria principale
- Memoria associativa – ricerca parallela

| Page # | Frame # |
| :--- | :--- |
| | |
| | |
| | |

- Traduzione di un indirizzo (p, d)
  - Se p è in un registro associativo, genera il frame # in output
  - Altrimenti (TLB miss) prendi il frame # dalla page table in memoria
    - La nuova coppia trovata può essere aggiunta nei registri

---

## Pagina 277

Hardware per Paging con TLB

Hardware necessario per implementare il paging con Translation Look-aside Buffers (TLBs)

- CPU
- logical address
- page number
- frame number
- TLB
- TLB hit
- physical address
- physical memory
- TLB miss
- page table

---

## Pagina 278

Implementazione della Page Table

- Ogni volta che non si trova il valore in TLB (TLB miss), il valore è caricato sulla TLB per un accesso veloce la volta successiva
  - Se piena occorrono politiche di rimpiazzo
    - Least recently used (LRU), round robin, random
- Alcune entry possono essere cablate per consentire l’accesso permanente
  - Es. Codice del kernel rilevante

- Alcune TLB hanno address-space identifiers (ASIDs) per ogni entry
  - Identifica univocamente il processo
  - Permette di mantenere info su diversi processi contemporaneamente
    - Altrimenti dovrebbe fare il flush per ogni context switch per evitare di far accedere il processo alle associazioni della page table di un processo precedente
  - Fornisce una protezione del suo spazio di indirizzi
    - Quando risolve l’indirizzo verifica se il processo corrente corrisponde a quello indicato, se non corrisponde si considera una TLB miss

---

## Pagina 279

Tempo di Accesso Effettivo

- Assumiamo $\varepsilon$ unità di tempo la ricerca in TLB
  - Può essere < 10% del tempo di accesso in memoria
- Assumiamo la hit ratio = $\alpha$
  - Hit ratio – percentuale di volte che si trova la pagina in TLB (dipende dal numero di registri)
    - Es. 80% significa 80% delle volte si trova la pagina
- Considiamo $\alpha = 80\%$, $\varepsilon = 20$ns per una ricerca in TLB e $T_a = 100$ns per un accesso in memoria
- Effective Access Time (EAT)
  $$EAT = (T_a + \varepsilon) \alpha + (2 T_a + \varepsilon)(1 - \alpha)$$
  $$= 2 T_a + \varepsilon - T_a \alpha$$
  - Se $\alpha = 80\%$, $\varepsilon = 20$ns per la ricerca in TLB search, $T_a = 100$ns per accesso in memoria … EAT = 0.80 x 100 + 0.20 x 200 + 20 = 140ns
  - Con un più realistico hit ratio -> $\alpha = 99\%$, $\varepsilon = 20$ns per la ricerca in TLB, 100ns per accesso in memoria … EAT = 0.99 x 100 + 0.01 x 200 + 20 = 121ns

---

## Pagina 280

Tempo di Accesso Effettivo

Nei sistemi moderni più complicato il calcolo perché più livelli di TLB
- Es. La CPU Intel Core i7 ha una TLB L1 da 128-entry per le istruzioni ed una TLB L1 dati da 64-entry
- Se c’è il miss ad L1 occorrono 6 cicli di CPU per verificare la entry nella L2 512-entry TLB.
- Se miss in L2 allora la CPU o cerca le entry in memoria, con costo di centinaia di cicli, oppure può interrompere per delegare al SO il compito …

TLB sono elementi hardware a supporto del paging, gli SO devono essere progettati tenendo presente le caratteristiche di questi elementi che possono variare a seconda della piattaforma

---

## Pagina 281

Esercizio

- Sia dato un sistema di paginazione con una tabella delle pagine che risieda in memoria con un TLB con un hit ratio del 90%
- Se per un accesso in memoria occorrono 200 nanosecondi, quanto tempo occorrerà per ottenere il dato relativo a un indirizzo logico?
  - Si supponga trascurabile il tempo di ricerca della entry nella tabella delle pagine

---

## Pagina 282

Esercizio

□ Sia dato un sistema di paginazione con una tabella delle pagine che risieda in memoria con un TLB con un hit ratio del 90%
□ Se per un accesso in memoria occorrono 200 nanosecondi, quanto tempo occorrerà per ottenere il dato relativo a un indirizzo logico?
  □ Si supponga trascurabile il tempo di ricerca della entry nella tabella delle pagine

□ Caso hit: tempo di accesso 200 ns
□ Caso miss: tempo di accesso 400 ns
□ Tempo accesso effettivo: 0.9 x 200 + 0.1 x 400 ns = 220 ns

---

## Pagina 283

Protezione di Memoria

- La protezione della memoria è implementata associando dei bit di protezione per ogni frame per indicare i permessi (read-only, read-write)
  - Si possono aggiungere più bit per indicare execute-only, etc.
  - Mentre si cerca il frame si può controllare l’accesso
  - Una violazione dei permessi provoca un trap hardware

- Alle entry della page table sono associate anche bit valid-invalid:
  - “valid” indicata che la pagina nello spazio logico del processo è valida, quindi legale
  - “invalid” indica che la pagina non è nello spazio logico del processo
  - Ogni violazione provoca un trap al kernel
  - Il SO usa questi bit per permettere o vietare l’accesso alle pagine

---

## Pagina 284

Valid (v) o Invalid (i) Bit in Page Table

Es. 14-bit address space [0,16383], processo solo in [0, 10468]
Pagine di 2KB, quindi le pagine 6, 7 non sono valide

Però pagina 5 accessibile (frammentazione interna) fino a 12287

Accesso disabilitato

Si può usare il page-table length register (PTLR) per indicare la dimensione della tabella delle pagine e verificare se l’accesso è consentito oppure no

Operating System Concepts – 10th Edition

---

## Pagina 285

Present/Not Present Bit in Page Table

Es. 16 bit e pagine di 4 KB (2^12), entry tabella delle pagine?

Indirizzo virtuale 8196 tradotto nell’indirizzo fisico 24580

---

## Pagina 286

Entry di una Page Table

Diverse informazioni aggiuntive nella Page Table

Presente/Assente page fault
Valido/invalid
Protezione read/write o only read
Modificato drity bit
Riferito
Caching (se disabilitato accessi diretti alla pag. in mem)

---

## Pagina 287

Pagine Condivise

□ Vantaggio del paging è la possibilità di condividere pagine fra processi
□ Particolarmente vantaggioso in architetture multiutente

□ Codice condiviso
□ Una copia di codice read-only (rientrante) condivisa tra processi (i.e., text editor, compilatori, librerie) evitando duplicazioni
  ► Due o più processi possono condividere lo stesso codice
  ► Es. Standard C library condivisa tra processi (se 2Mb per 40 utenti, 2Mb vs 80 Mb)
□ Simile a thread multipli che condividono lo stesso spazio di processo
□ Utile anche per interprocess communication se possibile condividere pagine read-write

□ Codice e dati privati
□ Ogni processo mantiene copia separata del codice e dei dati
□ Le pagine per codice privato e dati può apparire ovunque nello spazio degli indirizzi logici

---

## Pagina 288

Esempio Pagine Condivise

□ Esempio codice editor condiviso da tre processi

- process $P_1$
- page table for $P_1$
- ed 1
- ed 2
- ed 3
- data 1
- process $P_2$
- page table for $P_2$
- ed 1
- ed 2
- ed 3
- data 2
- process $P_3$
- page table for $P_3$

---

## Pagina 289

Struttura della Tabella delle Pagine

- Modeni elaboratori supportano spazi di indirizzi logici molto estesi (da $2^{32}$ a $2^{64}$)
- Struttura per la paginazione può diventare enorme
  - Se indirizzi logici di 32-bit e dimensione delle pagine di 4 KB ($2^{12}$)
  - La page table avrebbe più di un millione di entry ($2^{32} / 2^{12}$)
  - Se ogni entry è di 4 byte -> 4 MB di spazio di indirizzi fisici solo per la tabella delle pagine
    - Alto costo di memorizzazione
    - Non si vuole allocare in modo contiguo in memoria principale

- Metodi
  - Hierarchical Paging
  - Hashed Page Tables
  - Inverted Page Tables

---

## Pagina 290

Tabella delle Pagine Gerarchiche

- Suddividere lo spazio degli indirizzi logici su più tabelle delle pagine
- Una tecnica semplice è la tabella delle pagine su più livelli
  - Si pagina la tabella delle pagine
  - Il page number è a sua volta diviso in page number e offset
  - Es. con spazio degli indirizzi logici a $2^{32}$ e pagine di 4KB

| page number | page offset |
| :--- | :--- |
| $p_1$ | $p_2$ |
| 10 | 10 | 12 |

---

## Pagina 291

Tabella delle Pagine a Due Livelli

outer page table
page of page table
page table
memory

---

## Pagina 292

Esempio Paginazione a due Livelli

- Un indirizzo logico (su macchina a 32-bit con pagine da 1KB) diviso in:
  - page number di 22 bit
  - page offset di 10 bit

- La tabella delle pagine è paginata e il page number è ancora suddiviso in:
  - 12-bit page number
  - 10-bit page offset

- L’indirizzo logico è quindi:

| page number | page offset |
| :--- | :--- |
| $p_1$ | $p_2$ | $d$ |
| 12 | 10 | 10 |

- dove $p_1$ è indice della tabella esterna, $p_2$ è l’offset nella pagina della tabella delle pagine esterna

- Metodo chiamato forward-mapped page table

---

## Pagina 293

Schema di Address-Translation

- Metodo chiamato forward-mapped page table

---

## Pagina 294

64-bit Logical Address Space

- Ma anche lo schema di paging a due livelli non è sufficiente (indirizzi 64 bit)
- Se la dimensione delle pagine fosse 4 KB ($2^{12}$)
  - La page table avrebbe $2^{52}$ entry
  - Con lo schema a due livelli e pagine interne di $2^{10}$ con entry di 4-byte
  - L’indirizzo sarebbe

| outer page | inner page | page offset |
| :--- | :--- | :--- |
| $p_1$ | $p_2$ | $d$ |
| 42 | 10 | 12 |

- La tabella esterna avrebbe $2^{42}$ entry
- Una soluzione prevede l’aggiunta di una seconda tabella esterna
- Ad esempio una seconda tabella esterna di $2^{34}$ byte

- Può portare fino a 4 accessi in memoria per un singolo accesso

---

## Pagina 295

Schema di Paging a Tre Livelli

| outer page | inner page | offset |
| :--- | :--- | :--- |
| $p_1$ | $p_2$ | $d$ |
| 42 | 10 | 12 |

| 2nd outer page | outer page | inner page | offset |
| :--- | :--- | :--- | :--- |
| $p_1$ | $p_2$ | $p_3$ | $d$ |
| 32 | 10 | 10 | 12 |

Sempre pagina esterna di 2^32 entry (se 4 byte per entry allora 2^34 byte, i.e., 16 GB)

Allora altri livelli?

---

## Pagina 296

Hashed Page Table

- Tipico con spazio di indirizzi > 32 bits
- Il numero di pagina virtuale viene messo in una hash page table

Hash Table:
- Struttura dati per implementare array associativi
  - Mappa chiave su valore
  - Utilizza una funzione di hash h che traduce una chiave in un indice di una tabella
    $$h : U \rightarrow \{0, 1, \ldots, m-1\}$$
  Dove U è l’universo delle chiavi, mappate da h su indici sono indici di una tabella
    $$T[0 \ldots m-1]$$
  Dal momento che Hash table utile con m << | U | sono possibili collisioni
    $$h(k_1) = h(k_2)$$
  Finché il numero di elementi in tabella n < m sono rare
  Con n > m inevitabili

---

## Pagina 297

Hashed Page Table

- Tipico con spazio di indirizzi > 32 bits
- Il numero di pagina virtuale viene messo in una hash page table
  - La page table contiene una catena di elementi in hash sulla stessa locazione
  - Ogni elemento contiene (1) il numero di pagina virtuale (2) il valore del page frame mappato (3) un puntatore all’elemento successivo
  - I numeri di pagina virtuale sono confrontati nella catena in cerca di un match
  - Se un match è trovato viene estratto il frame fisico corrispondente

---

## Pagina 298

Hashed Page Table

- Tipico con spazio di indirizzi > 32 bits
- Il numero di pagina virtuale viene messo in una hash page table
  - La page table contiene una catena di elementi in hash sulla stessa locazione
  - Ogni elemento contiene (1) il numero di pagina virtuale (2) il valore del page frame mappato (3) un puntatore all’elemento successivo
  - I numeri di pagina virtuale sono confrontati nella catena in cerca di un match
  - Se un match è trovato viene estratto il frame fisico corrispondente

- Una variazione per indirizzi a 64-bit sono le clustered page tables
  - Simili alle hashed ma ogni entry nella hash si riferisce a molte pagine (16) invece di una sola
  - Molto utile per spazi di indirizzi sparsi (dove i riferimenti in memoria sono non contigui e sparpagliati)

---

## Pagina 299

Tabella delle Pagine Invertite

□ Invece di avere ogni processo con una page table e tener traccia di tutte le pagine logiche si tracciano le pagine fisiche (es. IBM RT)

□ Una entry per ogni pagina reale di memoria
□ Le entry consistono dell’indirizzo virtuale della pagina contenuta in memoria reale con informazione sul processo che possiede quella pagina

<process-id, page-number, offset>

□ Minore memoria per le tabelle delle pagine, ma aumenta il tempo necessario per cercare la tabella quando c’è un riferimento ad una pagina
□ Usata da 64-bit UltraSPARC e PowerPC

---

## Pagina 300

Architettura delle Tabella delle Pagine invertite

p non è più indice, ricerca del pid

---

## Pagina 301

Tabella delle Pagine Invertite

- Minore memoria per le tabelle delle pagine, ma aumenta il tempo necessario per cercare la tabella quando c’è un riferimento ad una pagina

  `<process-id, page-number, offset>`

- Hash table per limitare la ricerca ad una - o poche - entry della tabella
  - Due accessi in memoria (uno per accedere ad hash table)
  - TLB può accelerare l’accesso (prima di accedere ad hash table)

- Più complesso implementare la memoria condivisa (shared memory)
  - Un mapping solo di un indirizzo virtuale all’indirizzo fisico condiviso
  - Un riferimento da parte di altro processo genera il fallimento ed eventuale rimpiazzo del processo che insiste sul segmento

---

## Pagina 302

Oracle SPARC Solaris

- Esempio di SO a 64-bit con HW strettamente integrato
  - Obiettivi: efficienza e basso overhead

- Basato su hashing, ma più complesso
- Utilizza due hash table
  - Una per il kernel ed una per i processi utente
  - Ognuna mappa indirizzi da memoria virtuale su memoria fisica
  - Ogni entry rappresenta un’area contigua di memoria virtuale mappata
    - Non una entry di hash-table separata per ogni pagina
    - Ogni entry ha un indirizzo base e uno span (che indica il numero di pagine che la entry rappresenta)

---

## Pagina 303

Oracle SPARC Solaris

- La ricerca di una traduzione direttamente su hash-table inefficiente
  - Si usa Translation Lookaside Buffer (TLB)

- TLB mantiene le Translation Table Entries (TTEs) per una ricerca rapida:
  - Un insieme di TTEs è anche mantenuto in un Translation Storage Buffer (TSB)
    - Include entry per le pagine con accesso recente

- Un riferimento ad un indirizzo virtuale porta alla ricerca in TLB
  - Se c’è il miss, si scandisce via hardware la TSB cercando la TTE corrispondente a quell’indirizzo (TSB walk)
    - Se si trova il match la CPU copia la TSB entry nella TLB e si completa la traduzione
    - Se non si trova il match il kernel interrompe per cercare nella hash table
      - Il kernel poi crea una TTE dalla hash table e la mette in TSB, l’interrupt handler ritorna il controlla alla MMU che completa la traduzione dell’indirizzo

---

## Pagina 304

Swapping

- Un processo può essere scambiato (swapped) temporanemente con memoria ausiliaria (backing store) e poi portato ancora nella memoria principale per continuare l’esecuzione
  - La memoria fisica totale occupata dai processi può eccedere la memoria fisica disponibile

- Backing store – memoria secondaria veloce grande abbastanza per accommodare i processi che devono essere stoccati e repristinati
  - Deve fornire un accesso diretto a queste immagini in memoria

- Swap out, swap in – swapping di processi
  - Processi inattivi possono essere selezionati per swapping
  - La maggior parte del tempo di swap è di tempo di transferimento; il tempo di trasferimento è direttamente proporzionale alla quantità di memoria trasferita (swapped)

---

## Pagina 305

Schema dello Swapping

1. swap out
2. swap in

user space
main memory
process $P_1$
process $P_2$
backing store

---

## Pagina 306

Tempo di Context Switch incluso lo Swapping

- Se il prossimo processo da mandare alla CPU non è in memoria si deve fare lo swap-out di un processo e lo swap-in del processo target

- Il tempo di context switch può essere molto alto
  - Un processo di 100MB che fa swapping su hard disk con un transfer rate di 50MB/sec
  - tempo di swap out di 2000 ms
  - … più swap in di un processo della stessa dimensione
  - tempo totale di context switch swapping è 4000ms (4 secondi)

- Si può ridurre se si riduce la dimensione della memoria swapped
  - Sapendo quanta memoria viene usata esattamente da un processo si può ridurre

---

## Pagina 307

Tempo di Context Switch incluso lo Swapping

- Lo standard swapping non è più usato nei moderni SO (si usava in UNIX)
  - Una versione modificata tipica
    - Swap solo quando la memoria libera è estremamente bassa
  - Viene fatto swapping con paging
    - Sottoinsieme di pagine: page-in page-out

![Diagram showing page-out and page-in processes in main memory.](image)

---

## Pagina 308

Swapping su Sistemi Mobile

Tipicamente non supportata

□ Basta su flash memory
  ► poco spazio
  ► limitato numero of di cicli di scrittura
  ► dialogo carente tra la flash memory e la CPU su piattaforma mobile

□ Si usano altri metodi per liberare memoria

□ iOS chiede alle app di lasciare volontariamente memoria
  ► Dati read-only rilasciati e ricaricati dalla flash se necessario
  ► Fallimento nel rilascio può portare alla terminazione

□ Android termina le app se poca memoria, prima salva lo stato sulla flash per un restart veloce
□ Entrambi i sistemi supportano il paging

---

## Pagina 309

Segmentazione

- La pagina separa memoria logica e memoria fisica
- Segmentazione è uno schema di gestione della memoria che supporta la prospettiva utente sulla memoria
- Un programma è visto come una collezioni di segmenti
  - Un segmento è un’unità logica come:
    - main program
    - procedure
    - function
    - method
    - object
    - local variables, global variables
    - common block
    - stack
    - symbol table
    - arrays

---

## Pagina 310

Visione utente di un Programma

logical address

---

## Pagina 311

Visione Logica della Segmentazione

I segmenti sono numerati

user space

physical memory space

---

## Pagina 312

Architettura di Segmentazione

- Indirizzi logici sono definiti dalla tuple bidimensionale:
  `<segment-number, offset>`,

- Serve una struttura che mappa le tuple in indirizzi fisici

- Tabella dei Segmenti – mappa indirizzi bidimensionali in fisici; ogni table entry ha:
  - base – contiene l’indirizzo fisico di partenza del segmento
  - limite – specifica la lunghezza del segmento

---

## Pagina 313

Hardware per Segmentazione

CPU
s
d
limit base
segment table
yes
no
trap: addressing error
physical memory

---

## Pagina 314

Architettura di Segmentazione

□ Indirizzi logici sono definiti dalla tuple bidimensionale:
  <segment-number, offset>,

□ Serve una struttura che mappa le tuple in indirizzi fisici

□ Tabella dei Segmenti – mappa indirizzi bidimensionali in fisici; ogni table entry ha:
  □ base – contiene l’indirizzo fisico di partenza del segmento
  □ limite – specifica la lunghezza del segmento

□ La tabella dei segmenti non può essere tenuta in registri, quindi in memoria

□ Segment-table base register (STBR) indica la locazione di memoria della tabella dei segmenti

□ Segment-table length register (STLR) indica il numero dei segmenti usati da un program:
  ► Dato indirizzo logico (s,d), il numero s è legale se s < STLR

□ Registri associativi per limitare i due accessi in memoria

---

## Pagina 315

Architettura di Segmentazione

Esempio

---

## Pagina 316

Architettura per Segmentazione

Protezione (stesso segmento, stessa protezione)
- Ogni entry nella tabella dei segmenti è associata a:
  - validation bit = 0 ⇒ segmento illegale
  - privilegi read/write/execute
- Bit di protezione associati ai segmenti

Possono essere condivisi i segmenti tra processi
- La condivisione del codice avviene al livello di segmento
- Come per il paging una copia di un programma condiviso (es. editor di testo)
- Più programmi possono dover fare riferimento allo stesso numero di frammento
  - Porzioni di codice con riferimento diretto a sé stesse

Problema del doppio accesso come per paginaione

I segmenti di un processo, come per pagine, non necessariamente contigui
- segmenti di dimensione diversa quindi problemi di frammentazione
- si possono fondere i metodi di paginaione e segmentazione

---

## Pagina 317

Segmentazione Paginata

- Segmentazione paginate in GE 645 (MULTICS)
  - Tabella dei segmenti:
    - lunghezza segmento e base della tabella
  - Tabella delle pagine per il segment s
    - base tab + p = base pagina

---

## Pagina 318

Esempi: Architetture Intel 32 e 64-bit

Intel ha dominato l’industria per decadi
- Negli anni 70, 8086 a 16-bit seguita da 8088 (usato nel PC IBM)
- Poi passata ad architetture a 32-bit (Architetture IA-32 – Intel Architecture)
- Le CPU Pentium sono esempi di 32-bit
- Ora le CPU Intel sono a 64-bit e sono chiamata architetture IA-64
- Molte varianti nei chip, si consideriamo solo i concetti principali

---

## Pagina 319

Esempio: l’Architetture Intel IA-32

- Supporta sia segmentazione che segmentazione con paging
- La CPU genera indirizzi logici passati all’unità di segmentazione che produce **indirizzi lineari** poi passati all’unità di paging che produce l’indirizzo fisico (segmentation unit + page unit = MMU)

- Ogni segmento grande fino a 4 GB
- Numero di segmenti per processo divisi in due partizioni
  - Prima partizione segmenti privati per il processo (descritti in una **local descriptor table** (LDT))
  - Seconda partizione segmenti condivisi tra tutti i processi (descritti in una **global descriptor table** (GDT))

---

## Pagina 320

Esempio: Architettura Intel IA-32

- La CPU genera indirizzi logici per l’unità di segmentazione
  - logical address
  - selector
  - offset
  - offset a 32 bit
  - enty da 8 byte (base e limite e attributi di protezione)
  - se offset supera limite generato un fault
  - 8086-80286 solo segmentazione
  - 80386 segmentation+paging (1985)
  - Negli SO moderni segmentazione in flat mode (base=0) e paging dominante

- Il selettore è a 16-bit

  - s per il numero di segmento, g il tipo (global/local), p la protezione

---

## Pagina 321

Esempio: Architettura Intel IA-32

- Traduzione da indirizzo logico a fisico in IA-32

  Intel 80386 e successivi in modalità 32 bit

- Unità di paging di IA-32

- Dimensioni delle pagine 4 KB o 4 MB

  - Per 4 KB schema di paging a due livelli
  - Per 4 MB schema ad un livello
  - Indirizzo lineare 32 bit per paging a 2 livelli

---

## Pagina 322

Esempio: Architettura Intel IA-32

- Unità di paging di IA-32
- Dimensioni delle pagine 4 KB o 4 MB
  - Per 4 KB schema di paging a due livelli
  - Per 4 MB schema ad un livello

Indica una entry nella page directory (tabella esterna)

Registro che indica la page directory del processo corrente

---

## Pagina 323

Intel IA-32 Estensioni Indirizzo Pagina

- Limiti di accesso di indirizzi 32-bit hanno portato Intel a creare page address extension (PAE) permettendo ad app di 32-bit l’accesso a memorie più grandi di 4GB
  - Paging con schema a 3-livelli (per pagine a 4 KB)
  - Primi 2 bit si riferiscono ad una page directory pointer table
  - Le entry delle strutture di paging aumentate da 32 a 64-bit
    - Base address da 20 a 24 bit + 12 bit per offset
    - Indirizzi fisici di 36 bit – fino a 64GB di memoria fisica

Diagram showing the page directory pointer table and page table offsets. In IA-32 Linux e MacOS supportano, Windows no

---

## Pagina 324

AMD64/Intel x86-64

- Generazione corrente è architettura x86-64
- x86-64 proposto da AMD e adottato da Intel (AMD64 e Intel64)

- 64 bit consentirebbero dimensioni enormi ( $2^{64} > 16$ exabyte)
- In pratica è implementato un indirizzamento a 48 bit
  - Dimensione di pagina 4 KB, 2 MB, 1 GB
  - Quattro livelli di gerarchia di paging

Anche se 48-bit virtuali con page address extension fino a 52-bit indirizzi fisici

---

## Pagina 325

Esempio: Architettura ARM

- Dominante per i chip su piattaforma mobile (es. Apple iOS e Google Android, ma anche sistemi embedded real-time)
- CPU moderna ed efficiente energeticamente
- ARMv8 è a 64-bit

---

## Pagina 326

Esempio: Architettura ARMv8

□ ARMv8 è a 64-bit
□ Tre granularità di traduzione 4 KB, 16 KB, 64 KB associate a dimensione di pagina e sezioni di memoria contigua (regions)

| Translation Granule Size | Page Size | Region Size |
| :--- | :--- | :--- |
| 4 KB | 4 KB | 2 MB, 1 GB |
| 16 KB | 16 KB | 32 MB |
| 64 KB | 64 KB | 512 MB |

□ Usati fino a 48 bit

□ Per 4 KB e 16 KB fino a 4 livelli di paging, fino a 3 per 64 KB

---

## Pagina 327

Esempio: Architettura ARMv8

□ ARMv8 è a 64-bit
□ Tre granularità di traduzione 4 KB, 16 KB, 64 KB associate a dimensione di pagina e sezioni di memoria contigua (regions)

| Translation Granule Size | Page Size | Region Size |
| :--- | :--- | :--- |
| 4 KB | 4 KB | 2 MB, 1 GB |
| 16 KB | 16 KB | 32 MB |
| 64 KB | 64 KB | 512 MB |

□ Usati fino a 48 bit

□ Per 4 KB e 16 KB fino a 4 livelli di paging, fino a 3 per 64 KB
□ I livelli 1 e 2 possono essere anche usati per indirizzare regioni da 1-GB (livello 1) e 2-MB (livello 2)

□ Se livello 1, 0–30 bit di offset, se livello 2, 0–20 bit di offset
□ Due livelli di TLBs
  ▶ Livelli interni hanno due micro TLBs (una dati, una instruzioni)
  ▶ La più esterna è una singola TLB

---

## Pagina 328

TLB Miss e Cache

- In caso di TLB miss si attiva il page table walk
- Il page table walk richiede più accessi alle strutture di paging
- Le page table sono dati in memoria
- Gli accessi alle page table:
  - passano attraverso la gerarchia di cache (L1 D-cache, L2, L3)
  - non vanno direttamente in memoria principale

- Spesso le entry delle page table sono già in cache
- Gli accessi alle page table sono serviti dalla cache dati, riducendo significativamente il costo di una TLB miss
- Alcune architetture hanno paging-structure cache (cache dedicate per PTE/PDE)

---

## Pagina 329

Comandi

- Layout di memoria di un processo (print memory map)
  - Indirizzi virtuali, Resident Set Size (mem RAM), dirty bit, mode, map
  - pmap [options] [pid]
    - -x extended info (address, permissions)
    - -d content of heap regions
    - -p show the page size
  - pmap –d [pid]
  - pmap –x [pid]
  - ps

| Address | Kbytes | RSS | Dirty | Mode | Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0000563511c54000 | 2048 | 1024 | 0 | r-x-- | /path/to/executable |
| 0000563511e54000 | 4 | 4 | 4 | rw--- | /path/to/executable |
| 00007f5c0ec75000 | 16384 | 8192 | 0 | rw--- | [ anon ] |

---

## Pagina 330

Memoria di Massa

---

## Pagina 331

Memoria di Massa

- Overview della struttura di un Sistema di Memoria di Massa
- Struttura del Disco
- Schedulazione del Disco
- Gestione del disco
- Swap-Space Gestione
- Struttura RAID
- Implementazione Stable-Storage

---

## Pagina 332

Obiettivi

- Descrivere la struttura fisica di un dispositivo di memoria secondario e i suoi effetti sull’uso del dispositivo
- Spiegare le performance dei dispositivi di memoria di massa
- Valutare gli algoritmi di disk scheduling
- Discutere i servizi del SO per la memorizzazione di massa, inclusi i RAID

---

## Pagina 333

Overview della Struttura di Memoria di Massa

Consideriamo due tipi di memorie secondarie

- Hard Disk Drives (HDDs) e NonVolatile Memory (NVM)
- Coprono la maggior parte dei dispositivi per la memoria secondaria dei moderni computer
- Si descrivono le caratteristiche di questi dispositivi

---

## Pagina 334

Hard Disk

- Strutturati su dischi
- Dischi piatti come CD hanno dimensioni da .85” a 14” (storicamente)
  - Comunemente 3.5, 2.5 e 1.8 pollici
  - Superfici coperte da materiale magnetico
- Una testina read-write si move suoi piatti
- Braccio muove le testine
- Piatti divisi in tracce
- Tracce divise in settori
- Testine si muovono su cilindri (insieme di tracce)
- Migliaia di cilindri, per ogni traccia centinaia di settori
- Prima settori 512 bytes ora fino a 4 KB

---

## Pagina 335

Hard Disk

- Capacità da GB a TB
- Motore disco
  - da 60 a 250 rotazioni per secondo,
  - rotation per minute (RPM) da 5400 a 15000
- Performance
  - Transfer Rate
    - da disco a computer
    - teorico – 6 Gb/sec
    - Effective Transfer Rate – real – 1Gb/sec
- Tempo di posizionamento
  - Seek time e rotational latecy
  - Seek time da 3ms a 12ms – 9ms comune per desktop drives
  - Latenza dipende da spindle speed
  - 1 / (RPM / 60) = 60 / RPM
  - Average latency = ½ latency

---

## Pagina 336

Hard Disk Performance

□ Access Latency = Average access time = average seek time + average latency
  □ Per dischi più veloci 3ms + 2ms = 5ms
  □ Per dischi lenti 9ms + 5.56ms = 14.56ms

□ Average I/O time = average access time + (quantità da transferire / velocità di transferimento) + overhead del controllore

□ Per esempio per trasferire un blocco di 4KB su un disco da 7200 RPM con un average seek time di 5ms, 1Gb/sec di transfer rate con un .1ms overhead del controllore =
  □ 5ms + 4.17ms + 0.1ms + transfer time =
  □ Transfer time = 4KB / 1Gb/s = 0.031 ms
  □ Average I/O time for 4KB block = 9.27ms + .031ms = 9.301ms

---

## Pagina 337

1956
IBM RAMDAC computer included the IBM Model 350 disk storage system

5M (7 bit) characters
50 x 24” platters
Access time = < 1 second

---

## Pagina 338

Dispositivi NVM

I dispositivi NVM sempre più rilevanti e diffusi. Sono eletrici e non meccanici. Tipicamente composti basati su memoria flash (chip NAND flash) vengono spesso inseriti in contenitori simili a unità disco, e per questa ragione sono chiamati dischi a stato solido, o SSD

Un dispositivo NVM può anche assumere la forma di un’unità USB

In tutte le sue forme possiamo trattarlo in modo uniforme

Figura 11.3 Scheda di un SSD da 3,5 pollici.

---

## Pagina 339

Solid-State Disks (SSDs)

- Memoria nonvolatile usata come un hard drive
  - Non meccanica
  - Implementata con diverse tecnologie

- Può essere più affidabile di HDDs
- Più costosa per MB
- Forse life span più breve
- In generale ha meno capacità di HDD ma più veloce
- Capacità cresce rapidamante ed il prezzo cala, quindi si stanno affermando

- I bus di connessione possono essere troppo lenti
  - connessi direttamente al bus di sistema

- Non parti mobili, non parti meccaniche
  - non seek time e rotational latency

---

## Pagina 340

Algoritmi del controllore delle NAND Flash

Implementate con semiconduttori NAND (transistor MOSFET) che portano nuove sfide a capacità di memorizzazione e affidabilità

I semiconduttori NAND non possono essere sovrascritti direttamente, devono prima essere cancellati. Organizzati in pagine e presentano pagine che contengono dati non validi.

La cancellazione avviene in blocco e prende tempo (> del tempo di scrittura > tempo lettura). Le operazioni possono avvenire in parallelo. Deterioramento dopo ogni cancellazione. Durata misurata in Drive Writes per Day: quanto volte può essere scritta per giorno prima del fallimento (es. 1 TB può avere 5 DWPD nel periodo garantito)

Algoritmi gestiti dal controller, non dal sistema Operativo

Figura 11.4 Blocco NAND con pagine valide e non valide.

---

## Pagina 341

Controllore delle NAND Flash

I semiconductori NAND non possono essere sovrascritti direttamente, devono prima essere cancellati. Sono di solito presenti pagine che contengono dati non validi.

Il controller contiene una tabella: Flash Translation Layer (FTL) indica quali pagine contengono dati validi

Per gestire i dati occorrono: algoritmi di garbage collection per liberare blocchi da pagine valide, pagine (circa 20%) sempre disponibili per fare il write (overprovisioning), meccanismi per distribuire le cancellazioni, meccanismi di correzione del dato (se errori continui su una pagina, questa è marcata come bad)

Figura 11.4 Blocco NAND con pagine valide e non valide.

---

## Pagina 342

Memoria Volatile

- Memoria volatile (DRAM) può essere usata per fare storage
- Si parla di RAM drivers o RAM disk

- Creati dai device driver che presentano porzioni della DRAM come se fosse memoria di massa (temporaneo)
- Accessibile ad utenti e programmatori
- In Linux /dev/ram e /tmp
- Memorizzazione temporanea, ma accesso molto rapido

---

## Pagina 343

Dischi Magnetici

- Era il primo mezzo di memorizzazione secondaria
  - Evoluto da bobina a cartucce

- Relativamente permanente, contiene larghe quantità di dati
- Tempo di accesso molto lento
- Random access ~1000 volte più lento del disco, 100000 più lento di SSD
- Usate soprattutto per backup, stoccaggio di dati non usati frequentemente, trasferimento tra sistemi
- Mantenuto in bobina e avvolto o riavvolto per la testina di lettura-scrittura
- Una volta che i dati sotto testina, velocità di trasferimento simile al disco
  - 140MB/sec e maggiore
- TB di storage

---

## Pagina 344

Metodi di Connessione Memoria Secondaria

- Drive connesso al computer via I/O bus o il bus di sistema
  - Bus variano, es. EIDE, ATA, SATA, USB, Fibre Channel, SCSI, SAS, Firewire
    - Per HDDs più comune è il SATA
    - Per NVM interface veloci NVM express che collega direttamente al Peripheral Component Interconnect (PCI) bus

- Trasferimento dati sul bus gestiti da controller
- Host controller gestisce il trasferimento dati lato computer che usa il bus per parlare con il disk controller

---

## Pagina 345

Mapping degli Indirizzi

- Le unità disco sono indirizzati come grandi array 1-dimensionali di blocchi logici dove il logical block è la più piccola unità di trasferimento
  - Formattazione di basso livello creano blocchi logici su mezzi fisici
  - Ogni blocco logico mappato sui settori fisici o su pagine di un dispositivo NVM

- Su Disco i blocchi logici sono mappati sequenzialmente in settori
  - Settore 0 è il primo settore della prima traccia sul cilindro più esterno
  - Il mapping procede in ordine, dalla prima al resto delle tracce su quel cilindro e poi attraverso il resto dei cilindri (dal più esterno al più interno)

- Per NVM mapping da tuple (chip, blocco, pagina) a blocchi logici

- Indirizzamento basato su Logical Block Address (LBA) più semplice di settore, cilindro, testina o chip, blocco, pagine

---

## Pagina 346

Mapping degli Indirizzi

- Le unità disco sono indirizzati come grandi array 1-dimensionali di blocchi logici dove il logical block è la più piccola unità di trasferimento
  - Formattazione di basso livello creano blocchi logici su mezzi fisici
  - Ogni blocco logico mappato su un settore fisico o su pagina di un dispositivo NVM

- Su Disco blocchi logici mappati sequenzialmente in settori
  - Unità minima di lettura/scrittura (si scrive in blocchi)
  - Settore di solito 512 bytes individuato mediante un numero a partire da 1
  - Settori per traccia 63
  - Settore individuato da numero della testina, il numero di cilindro e quello del settore CHS (Cylinder Head Sector)
  - LBA (Linear Block Addressing) i settori vengono numerati utilizzando la successione 0,1,2... Es. primi 63 (C=0,H=0), poi 64 (C=1, H=0, S=1)

---

## Pagina 347

Mapping degli Indirizzi

- Le unità disco sono indirizzati come grandi array 1-dimensionali di blocchi logici dove il logical block è la più piccola unità di trasferimento
  - Formattazione di basso livello creano blocchi logici su mezzi fisici
  - Ogni blocco logico mappato su un settore fisico o su pagina di un dispositivo NVM

- Su Disco blocchi logici mappati sequenzialmente in settori
- Per NVM mapping da una tupla (chip, blocco, pagina) ad un blocco logico

- Il passaggio da indirizzi logici a fisici dovrebbe essere facile ma …

  - Settori possono essere danneggiati danneggiati
  - Non-constante numero di settori per traccia
  - Gestione interna del mapping tra LBA e settori fisici
  - Si tende a mantenere comunque allineati indirizzi logici e fisici (salgono insieme)

---

## Pagina 348

Struttura Disco

- L’array 1-dimensionale di blocchi logici è mappato in settori del disco sequenzialmente
- Due tipi di organizzazione del disco:

  - Stesso numero di settori per traccia
    - Ampiezza variabile del settore e densità scrittura variabile
    - Velocità lettura costante per traccia
    - Tracce esterne poco utilizzate

  - Numero di settori differente per traccia (zone bit recording)
    - Densità scrittura costante
    - Velocità lettura settori variabile
    - Ottimizzazione (più dati nei settori esterni)

---

## Pagina 349

Struttura Disco

□ L’array 1-dimensionale di blocchi logici è mappato in settori del disco sequenzialmente

□ Nei CD velocità aumenta verso l’interno per mantenere la lettura dei settori costante
  ► Constant Linear Velocity (CLV)

□ Nei dischi
  ► Constant Angular Velocity (CAV)
  ► Se stesso numero di settori per traccia densità dei bit varia per mantenere costante il flusso dei dati
  ► In zone bit recording il flusso varia per traccia (velocità di lettura diversa per zona)

□ Dimensioni tipiche:
  ► Diverse centinaia di settori per traccia,
  ► Decine di migliaia di cilindri

---

## Pagina 350

Scheduling del Disco

- Il SO è responsabile dell’uso efficiente dell’hardware
  - Per le unità disco significa veloce accesso e alto trasferimento dati

- Per le unità a disco
  - minimizzare il seek time e il latency time
  - Seek time ≈ seek distance
  - Latency time tempo per arrivare al settore con rotazione

- La disk bandwidth è il numero totale di bytes transferiti diviso per il tempo totale tra la prima richiesta di servizio ed il completamento dell’ultimo transferimento

- Si può aumentare sia l’accesso che il trasferimento gestendo l’ordine con cui vengono servite le diverse richieste di I/O

---

## Pagina 351

Scheduling del Disco

- Ci sono tipi di richieste di I/O da disco
  - Processi di sistema
  - Processi utente
  - Le richieste riguardano input o output, file da aprire, pagine da trasferire, etc.

- SO mantiene una coda di richieste, per disco o dispositivo

- Un disco disponibile in idle può subito servire la richiesta di I/O, il disco occupato gestisce una coda di richieste
  - Gli algoritmi di ottimizzazione hanno un ruolo nel caso di code
  - Nel passato molto sforzo per definire interfacce ai dischi per ottimizzare
  - Oggi molto è gestito direttamente dai controllori del disco
    - Non è accessibile la locazione esatta della testina di lettura dei dischi
    - Però si può assumere prossimità tra indirizzi fisici e logici

---

## Pagina 352

Scheduling del Disco

- Nota che il controllori di unità hanno piccoli buffer e possono gestire code di richieste di I/O
- Molti algoritmi proposti per schedulare il modo in cui sono servite le richieste di I/O (basati su riduzione del seek time)
- L’analisi è valida per uno o più piatti
- Illustriamo gli algoritmi di scheduling con una coda di richieste a blocchi su cilindri (0-199)

98, 183, 37, 122, 14, 124, 65, 67

Testina che punta a 53

---

## Pagina 353

FCFS

Algoritmo più semplice
La figura mostra un movimento di testina attraverso 640 cilindri
Si potrebbe migliorare con 37 e 14 serviti vicini, come 122 e 124

queue = 98, 183, 37, 122, 14, 124, 65, 67
head starts at 53

---

## Pagina 354

SSTF

- Shortest Seek Time First, seleziona la richiesta con il minimo seek time dalla corrente posizione della testina
- SSTF scheduling è una forma di SJF scheduling; può causare starvation di qualcuna delle richieste
- La figura mostra un numero totale di movimenti di testa di 236 cilindri

---

## Pagina 355

SCAN

- La testina inizia ad un estremo del disco e move verso l’altro estremo servendo le richieste finché non arriva all’altro estremo dove inverte il percorso
- SCAN algorithm chiamato anche elevator algorithm
- Nota che se le richieste non sono uniformemente dense con densità accumulate all’altro estremo del disco, queste possono aspettare molto

---

## Pagina 356

SCAN

- La figura mostra un movimento totale di 236 cilindri
- Nota che se le richieste non sono uniformemente dense con densità accumulate all’altro estremo del disco, queste aspettano molto

$$\text{queue} = 98, 183, 37, 122, 14, 124, 65, 67$$

head starts at 53

---

## Pagina 357

C-SCAN

- Tempi di attesa più uniformi rispetto a SCAN
- La testina si muove da un estremo del disco all’altro servendo le richieste nel mentre
  - Quando raggiunge l’altro estremo, comunque, immediatamente torna all’inizio del disco, senza servire le richieste nel viaggio di ritorno
  - Costo del ritorno ...
  - … ma le richieste sono più frequenti nei cilindri esterni

- Mette i cilindri in una lista circulare dove l’ultimo cilindro porta al primo

---

## Pagina 358

C-SCAN

Si assume il movimento sempre verso destra

queue = 98, 183, 37, 122, 14, 124, 65, 67
head starts at 53

---

## Pagina 359

C-LOOK

- LOOK è un tipo di SCAN, C-LOOK è una versione di C-SCAN
- Il braccio avanza fino all’ultima richiesta in ogni direzione, poi cambia direzione

$$\text{queue} = 98, 183, 37, 122, 14, 124, 65, 67$$
head starts at 53

---

## Pagina 360

Selezionare un Algoritmo di Disk-Scheduling

- SSTF (Shortest Seek Time First) è tipico e naturale
- SCAN e C-SCAN funzionano meglio per sistemi con grosso carico su disco
  - Meno starvation

- Performance dipende dal numero e dai tipi di richiesta
- Le richieste di servizio possono essere influenzate dai metodi di file-allocation
  - File allocato in modo contiguo meno movimenti di testina
  - File likato sparso più movimenti di testina
  - Allocazione delle directory (file aperti richiedono ricerca nella struttura)

- Algoritmi di disk-scheduling implementati come moduli separati del SO per consentire un aggiornamento se necessario
- SSTF che LOOK sono una ragionevole algoritmo di default

---

## Pagina 361

Selezionare un Algoritmo di Disk-Scheduling

- In alcuni sistemi più code con priorità per evitare starvation
- Linux – deadline scheduler con code di read e write con priorità e ordine LBA (Logical Block Addressing) implementate in modo simile a C-SCAN
  - read maggiore priorità perché bloccante
- Quattro code per gestire le deadline
  - 2 per read e 2 per write, una gestita con LBA l’altra con FCFS
  - Le richieste gestite in batch, dopo ogni batch si controlla se ci sono richieste in FCFS vecchie (più di 500 ms per read e 5 sec per write) e si sceglie quello come prossimo batch LBA
  - Quando scade il timer di deadline, Deadline comincia a servire le richieste dalla coda FIFO. Si serve per ordine di arrivo. Si contrasta la starvation delle richieste (con preferenza alle richieste in lettura)

---

## Pagina 362

Selezionare un Algoritmo di Disk-Scheduling

- Lo scheduler NOOP (NO OPERATION) è il più semplice fornito da Linux.
- echo noop > /sys/block/sda/queue/scheduler
- Funzionamento. Una coda di richieste, gestita in modalità FIFO con merging delle richieste contigue

- Vantaggi. Scheduler semplicissimo e molto efficiente in termini di esecuzione. Non ha nessuna logica di riduzione dei seek (a parte il merging) ideale per dispositivi non rotazionali → (SSD).

- Svantaggi. Non ha nessuna logica di riduzione dei seek (a parte il merging) disastroso sui dispositivi rotazionali. → Starvation delle richieste. Incapacità di differenziare in base all’importanza del processo.

---

## Pagina 363

NVM scheduling

- Lo scheduling HDD deve minimizzare i movimenti meccanici
- Nel caso di NVM non ci sono movimenti meccanici e si usa FCFS
  - Es. In Linux NOOP usa FCFS modificato per servire richieste adiacenti
- Le richieste read sono servite in modo uniforme, ma write in modo non uniforme
  - Alcuni SO servono le read con FCFS, e accorpando solo richieste di write
- I/O possono avvenire in modo random o sequenziale
  - Per HDD meglio sequenziale
  - Per NVM random è ok
  - input/output operations per second (IOPS) diversi per HDD e NVM
    - Nel caso di accesso random centinaia vs centinaia diiglia
    - Nel caso di accesso sequenziale più simile
    - Le performance di NVM degradano nel tempo e la scrittura è più lenta della lettura

---

## Pagina 364

Gestione del Disco

□ Il Sistema Operativo è responsabile di diverse operazioni
  □ Inizializzazione, bootstrap, bad-block recovery

□ Il dispositivo deve essere strutturato
  □ HDD in tracce e settori, NMV con pagine e FTL (Flash Transaltion Layer)
  □ Formattazione di basso livello o fisca, disco in settori che il disk controller può leggere e scrivere (produttore fornisce e fa testing)
    ► Utility di formattazione effettuano solo una rinizializzazione
  □ Ogni settore è un blocco di dati definita da un header, dati, più un trailer
    ► L’header permette l’identificazione del settore
    ► Il trailer contiene il checksum e un error correction code (ECC)

□ Il SO deve anche avere una strutturazione del disco
  □ Partizione del disco in uno o più gruppi di cilindri, ognuno trattato come un disco logico separato

---

## Pagina 365

Error Detection and Correction

- Occorrono tecniche per trovare e correggere errori
- Parity Bit
  - Esempio di metodo checksums che utilizza metodi aritmetici per controllare dati di lunghezza fissata:
    - Ogni byte ha associato un bit che controlla se il numero di 1 è pari (parity = 0) oppure è dispari (parity = 1)
    - Se uno dei bit è danneggiato allora il parity non coincide più con quello precalcolato (incluso il danno dello stesso parity)
    - Tutti gli errori di un un bit su un byte sono trovati (due bit non visti)
    - Il parity si calcola rapidamente con lo XOR (1 xor 1 = 0)
- Error Correction Code (ECC) fa anche la correzione
  - Disk drive usano un ECC per settore, NVM per pagina
  - Quando si scrive un settore/pagina ECC è scritto
  - Quando si legge ECC è controllato, se non coincide allora il settore/pagina è bad
  - Se soft error può essere corretto (pochi bit) altrimenti hard error

---

## Pagina 366

Error Detection and Correction

- Occorrono tecniche per trovare e correggere error

- Error Correction Code (ECC) fa anche la correzione
  - Disk drive usano un ECC per settore, NVM per pagina
  - Quando si scrive un settore/pagina ECC è scritto
  - Quando si legge ECC è controllato, se non coincide allora il settore/pagina è bad
  - Se soft error può essere corretto (pochi bit) altrimenti hard error

- Esempio ECC (Hamming)
  - k bit + r di parità ($r \geq \log_2(m + 1)$ con m bit totale in codice)
  - Es. Dati D1,D2,D3,D4 e parity P1, P2, P3
  - P1=Parity(1,2,4), P2 = Parity(1,3,4), P3 = Parity(2,3,4)
  - Se non parity errore 1,0,1,1,P1,P2,P4 sarà 0 1 0
  - Se non torna la parità errore e possibilità di individuarlo

---

## Pagina 367

Gestione dei Bad Block

□ Blocchi del disco possono essere corrotti
□ Nei vecchi sistemi la ricerca dei bad blocchi richiedeva una scansione lanciata dall’utente
□ Una gestione più sofisticata è fornita dai controllori del disco più recenti

□ Il controllore del disco mantiene una lista dei bad block del disco e ha a disposizione dei settori di ricambio non visti dal SO
  □ Quando prova ad accedere ad un settore e lo trova corrotto (ECC)
  □ Riporta l’errore all’SO e marca il settore come bad e lo sostituisce con un settore di richiambio
  □ Quando è richiesta il medesimo blocco logico, questo viene tradotto nel nuovo settore di ricambio
  □ Sostituzione può interferire con lo scheduling del disco se le riparazioni sono “lontane”, per questo i settori di ricambio si cercano nello stesso cilindro
    ► Altro metodo è il sector slipping che fa slittare i settori
    ► Nota: in NVM la gestione è più semplice, non c’è seek time da gestire

---

## Pagina 368

Gestione del Disco

Il SO deve anche avere una strutturazione del disco

suddivide il dispositivo in uno o più gruppi di blocchi o pagine, dette partizioni

crea e gestisce il volume

formattazione logica, cioè crea un file system

---

## Pagina 369

Gestione del Disco

Il SO deve avere una strutturazione logica del disco
- Partizione del disco in uno o più gruppi di cilindri, ognuno trattato come un disco logico separato (info su partizioni è su locazione del disco)
- In Linux fdisk per avere info sul dispositivo di storage
- Il Sistema Operativo riconosce un dispositivo e legge la sua info su partizione
- Il Sistema crea una entry per quella partizione (in Linux /dev)
- Per rendere un file system disponibile l’SO deve montare la partizione

Il secondo step è la creazione e gestione di un volume (drive logico)
- Creazione del volume può essere implicita o esplicita
- Linux volume manager lvm2

Il terzo step è la formattazione logica o la creazione di un file system
- Per incrementare l’efficenza i file system raggrupano i blocchi in clusters
  - Disk I/O fatto in blocchi
  - File I/O fatto in clusters (insiemi di blocchi)
- Partizione indica anche se la partizione consente il bootstrap

---

## Pagina 370

Gestione del Disco

- Esempio del tool di disk management di Windows 7
- Illustrati tre volumi C: E: F:, E: F: in partizioni del disco 1, c’è spazio non allocato per più partizioni

Figura 11.9 Lo strumento gestione dischi di Windows 7 mostra i dispositivi, le partizioni, i volumi e i file system.

---

## Pagina 371

Gestione del Disco

- Esempio del tool di disk management di Windows 10
- Illustrati due volumi C: D:, C: in partizione del disco 0 D: in partizione disco 1, c’è spazio non allocato per più partizioni

---

## Pagina 372

Gestione del Disco

Dal Boot block si inizializza il sistema
- I primi passi del bootstrap sono in firmware (test e avvio del boot)
- Avvio del processo di boot gestito con MBR (Master Boot Record) o GPT (GUID Partition Table)
- Con MBR
  - 512 byte: boot code (es. 446 byte), tabella partizioni (es. 64 byte), check (2 byte)
  - Portato in memoria boot code dal Master Boot Record
  - Può leggere partizioni e cercare i boot blocks
  - Boot Code carica un bootloader per fare il bootstrap
  - Il bootloader program è nel “boot block”
    - Un dispositivo che ha il boot block è un boot disk o system disk
  - Con il caricamento del boot block si può lanciare il bootloader program che poi caricherà il Kernel (bootstrap)

---

## Pagina 373

Gestione del Disco

□ Dal Boot block si inizializza il sistema
□ Esempio Windows (con BIOS - Basic Input/Output System)
  ► Boot inizia lanciando il programma nel firmwere (test e avvio)
  ► Test POST (Power-On Self Test)
  ► Programma avvio nel primo blocco logico di HDD o prima pagina di NVM - Master Boot Record (MBR)
  ► MBR ha codice di avvio (boot code) e tabella delle partizioni, da queste si risale alle partizioni di boot dove trova il bootloader NTLDR
  ► NTLDR carica il kernel

---

## Pagina 374

Booting da disco in Windows

Esempio Windows (BIOS - Basic Input/Output System)
- Firmware all’avvio test e lancio del boot
- boot code nel Master Boot Record (MBR)
- Il firmware carica il boot code dal MBR (lancia il sistema)
- MBR ha boot code e tabella delle partizioni, da queste si risale alle partizioni di boot dove trova il bootloader

MBR - settore 512-byte con settori di 512
2^32 indirizzi
Indirizzabili 2.2TB

---

## Pagina 375

Partizioni

- Il boot block può puntare a un volume di boot
  - Il codice nel boot block consente di caricare il Sistema
  - Il superblock contiene parametri del file system

A possible file system layout.

---

## Pagina 376

Booting da disco in Linux

Esempio Linux (con BIOS - Basic Input/Output System)
- Firmware all’avvio test e lancio del boot code (MBR bootloader)
- Bootloader di secondo livello (Grub2, systemd-boot)
- Il bootloader presenta un menu di possibili sistemi
- Una volta selezionato il sistema viene caricato il kernel in memoria
- Chiamato lo start_kernel() che lancia idle_process, scheduler, init

Booting Process

---

## Pagina 377

Booting da disco GPT

Boot con UEFI e disco GPT (GUID Partition Table)
- Usa identificatori univoci globali (GUID) per le partizioni
- Supporta dischi con capacità superiore a 2 TB e fino a 128 partizioni
- UEFI (Unified Extensible Firmware Interface) sostituisce BIOS
- Non usa MBR ma partizione ESP (EFI System Partition) nel disco GPT

- La GPT occupa i primi settori del disco:
  - LBA 0: Settore compatibilità (MBR protettivo) per indicare disco GPT
  - LBA 1: Intestazione GPT primaria, descrive la struttura delle partizioni
  - LBA 2 e succ.: Tabella partizioni GPT (entry per ogni partizione, inclusa ESP)

MBR:
•tabella = 64 byte
•max 4 partizioni
•indirizzi limitati (32 bit)

GPT:
•tabella = espandibile
•molte entry (es. 128)
•ogni entry contiene:
  •GUID
  •indirizzi a 64 bit
  •attributi

---

## Pagina 378

Booting da disco GPT

Boot con UEFI e disco GPT (GUID Partition Table)
- Usa identificatori univoci globali (GUID) per le partizioni
- Supporta dischi con capacità superiore a 2 TB e fino a 128 partizioni
- UEFI (Unified Extensible Firmware Interface) sostituisce BIOS
- Non usa MBR ma partizione ESP (EFI System Partition) nel disco GPT

- La GPT occupa i primi settori del disco:
  - LBA 0: Settore compatibilità (MBR protettivo) per indicare disco GPT
  - LBA 1: Intestazione GPT primaria, descrive la struttura delle partizioni
  - LBA 2 e succ.: Tabella partizioni GPT (entry per ogni partizione, inclusa ESP)

- Firmware UEFI all’avvio test - POST (Power-On Self Test)
- Il firmware consulta GPT e cerca file di avvio in ESP
- Il firmware carica il Boot Manager UEFI da ESP
- Il Boot Manager UEFI legge configurazioni di avvio e gestisce caricamento del kernel

- Può gestire diversi SO:
  - Ogni SO installato crea una directory nella ESP con i suoi file di avvio
  - Win /EFI/Microsoft/Boot/bootmgfw.efi
  - Linux /EFI/Ubuntu/grubx64.efi
  - macOS /EFI/APPLE/BOOT/BOOTX64.EFI

---

## Pagina 379

Partizioni e Montaggio

- Partizione può essere un volume che contiene un file system (“cotta”) or raw (cruda)– una sequenza di blocchi senza un file system
- Il meccanismo di boot individua un volume di avvio e carica un bootloader, che a sua volta carica il kernel dal file system
  - … o un programma boot management per boot con multipli SO
  - Il boot loader deve intepretare il formato del FS per poter caricare i blocchi
- Partizione root contiene il SO, altre partizioni possono contenere altri sistemi, altri file system, o possono essere raw
  - Montata a tempo di boot
  - Altre partizioni si possono montare automaticamente o manualmente
  - Su win montato su volume differenti name-space (lettere F:, E:, etc.)
- A tempo di mount, viene controllata la consistenza del file system
  - I metadata sono corretti?
    - se non lo sono, aggiusta e riprova
    - se lo sono, aggiungi la tabella del montaggio, permetti l’accesso

---

## Pagina 380

Gestione dello Swap-Space

- Swap-space — la memoria virtuale usa spazio su disco come estensione della memoria principale

- Lo swap space può variare da pochi megabytes a gigabytes a seconda della dimensione della memoria fisica, di quella virtuale e da uso
  - Solitamente meglio sovrastimare che sottostimare perché se finisce i processi possono essere abortiti o arrivare al crash di Sistema
  - Es. Solaris suggerisce tanto quanto SS = VM – FM, Linux prima SS = FM ora meno
  - In Linux multipli swap space su file system o su diverse partizioni

- Swap-space può essere ottenuto dal normale file system, ma più comunemente da una partizione del disco separata (raw)
  - Le partizioni raw permettono accesso più veloce ma è meno efficiente lo stoccaggio (frammentazione interna), cmq dati in swap a breve termine
  - Linux permette swap sia su file system che su partizione raw

---

## Pagina 381

Gestione dello Swap-Space

Gestione dello Swap-space – Esempio nei Sistemi UNIX

- Nei primi sistemi il Kernel faceva swapping dell’intero processo in locazioni contigue del disco, poi si è passata alla gestione con paging
- In Solaris 1 si rileggono le pagine di text direttamente dal file system, memoria anonima su swap space (stack, heap, memoria non inizializzata)
- Solaris 2 alloca swap space solo quando una dirty page viene mandata fuori dalla memoria fisica (non quando è creata la pagina della virtual memory)
- In Linux, come in Solaris, swap space solo per memoria anonima
  - Mantiene più aree swap (sia file system sia raw) – area composta di pagine di 4 KB
  - Il Kernel usa mappe di swap per tracciare l’uso dello swap-space – array di contatori interi che contano quanti processi si riferiscono a quella pagina (es. 0 pagina libera, 3 indica tre processi che condividono la stessa pagina)

In ubuntu le aree di swap attive si vedono con
  - swapon --show
RAM e swap
  - free -h
Swap file
  - ls -lh /swap.img

---

## Pagina 382

Strutture Dati Kernel per lo Swapping in Linux

swap area

page slot

swap partition or swap file

swap map

1 0 3 0 1

Occorre una struttura che fornisce informazioni sulla memoria di swap (swap_info_struct in linux): dispositivo, blocchi usati, liberi, etc.

Occorre anche la mappatura tra (pagine,pid) e blocchi in memoria di swap

---

## Pagina 383

Struttura RAID

- RAID – Redundant Array of Inexpensive Disks
  - Multiple unità disco forniscono affidabilità e performance con la ridondanza
  - Prima Inexpensive ora Independent

- La probabilità di fallimento di N dischi è più bassa

- Consideriamo il mean time between failure (MTBF)
  - Se 100.000 ore per un disco, in un array di 100 dischi il MTBF di almeno un disco è 1000 ore, cioè 41,66 giorni …
  - Senza replicazione dei dati è un problema

- Modo più semplice di replicare è il mirroring duplicazione dei dischi
  - Ogni disco logico corrisponde a più dischi fisici (es. scrittura doppia)
  - Perdita di dato solo se anche il secondo disco fallisce (prima della riparazione del primo)

---

## Pagina 384

Mirrored Disk

- Mirrored Disk
  - Oltre al mean time between failures
  - Mean time to repair – tempo di esposizione quando un altro fallimento potrebbe causare perdita di dati
  - Mean time to data loss tempo medio di perdita dei dati dovuti a fallimento
  - Se i mirrored disks fallissero independentemente, preso un disco con 100000 ore di mean time between failures e 10 ore di mean time to repair
  - Il mean time to data loss è 57000 anni!

- Però i fallimenti non sono indipendenti
  - Problemi di alimentazioni particolarmente problematici durante la scrittura
  - Scrivere in momenti diversi le repliche, oppure usare NVM come cache

---

## Pagina 385

Disk Striping

- Nel mirroring duplicate le scritture, però le richieste di lettura solo ad una delle unità e questo non migliora il trasferimento

- Disk striping usa un gruppo di dischi come un’unica unità di storage
  - Dati distibuiti (strisciati) su più dischi
  - Bit-level striping, ogni i-esimo bit sul drive i-esimo
  - Block-level striping, blocco i-esimo su (i mod n) + 1 drive
    - Tipicamente questo è il metodo

- Due obiettivi principali
  - Incrementare il throughput di piccoli accessi bilanciando il carico
  - Ridurre il tempo di risposta di un accesso grande

---

## Pagina 386

Redundant Array of Inexpensive Disks

- Mirroring porta ridondanza, ma è costoso
- Striping amenta il trasferimento di dati, ma non l’affidabilità
- Alcuni schemi combinano striping con parity bit
- Organizzazioni a livelli RAID

Es. 4 dischi per i dati, gli altri per ridondanza

- Livello 0 non ridondanza, molto fragile
  - No fault tolerance: se un disco fallisce dati persi
  - Veloce, parallelismo, no parity control
  - Minimo numero di dischi 2

- Livello 1 mirrored (C copia)
  - Dati duplicati, non overhead in velocità di scrittura
  - Velocizza la lettura (dati da più dischi)
  - Metà della capacità del disco
  - Minimo numero di dischi 2

(a) RAID 0: non-redundant striping.
(b) RAID 1: mirrored disks.
(c) RAID 2: memory-style error-correcting codes.
(d) RAID 3: bit-interleaved parity.
(e) RAID 4: block-interleaved parity.
(f) RAID 5: block-interleaved distributed parity.
(g) RAID 6: P + Q redundancy.

---

## Pagina 387

RAID 2 (poco utilizzato)
- Utilizza striping al livello di bit
- Utilizza hamming code per error detection/correction
- Minimo numero di dischi 3

RAID 3 (poco utilizzato)
- Utilizza byte level striping
- Disco con un parity disk
- Minimo numero dischi 3

RAID 4
- Utilizza block level striping
- Disco con parity disk
- Scrittura lenta, scrittura del parity su unico disco
- Minimo numero dischi 3

(a) RAID 0: non-redundant striping.
(b) RAID 1: mirrored disks.
(c) RAID 2: memory-style error-correcting codes.
(d) RAID 3: bit-interleaved parity.
(e) RAID 4: block-interleaved parity.
(f) RAID 5: block-interleaved distributed parity.
(g) RAID 6: P + Q redundancy.

---

## Pagina 388

RAID 5, 6

- RAID 5 distribuisce i parity su tutti i dischi, evita di usare troppo il disco parity
  - Minimo numero di dischi 3
  - Block level striping + ECC distribuito
  - ECC usato con stripping
    - Il primo blocco in drive 1, scondo in drive 2, N in drive N, error in N + 1
  - Permette anche la correzione dei dati
  - Più veloce del livello 1 nell’accesso
  - Scrittura migliore di livello 4

- RAID 6 simile
  - Minimo numero di dischi 4
  - aggiunge ridondanza per permettere recorvery da fallimenti multipli
  - 2 blocchi di parity distributi nei dischi
  - Tollera due fallimenti di dischi
  - Penalizzazione in scrittura

---

## Pagina 389

RAID (0 + 1) e (1 + 0)

Nested RAID o Hybrid RAID combinano i livelli standard

Striped mirrors (RAID 1+0) o mirrored stripes (RAID 0+1) forniscono alta performance e alta affidabilità: RAID 0 performance, RAID 1 affidabilità

RAID 01 (0 + 1)
Dati striped e duplicate

a) RAID 0 + 1 with a single disk failure.

RAID 10 (1 + 0)
Prima dati duplicati poi stripled sui dischi (almeno 4)
Vicino a RAID 0 per performance (usato per sistemi I/O intense) più ridondanza

b) RAID 1 + 0 with a single disk failure.

---

## Pagina 390

RAID

- Mirroring porta ridondanza, ma costoso
- Striping migliora il trasferimento di dati, ma non l’affidabilità
- Alcuni schemi combinano striping con parity bit

- RAID è organizzato in sei livelli differenti
- Gli schemi RAID aumentano le performance e l’affidabilità dello storage memorizzando dati ridondanti

  - Mirroring o shadowing (RAID 1) mantiene un duplicato di ogni disco
  - Striped mirrors (RAID 1+0) o mirrored stripes (RAID 0+1) fornisce alta performance e alta affidabilità
  - Block interleaved parity (RAID 4, 5, 6) usa molta meno ridondanza

---

## Pagina 391

Altre Caratteristiche

- Indipendente da come il RAID è implementato si possono aggiungere altri strumenti

- Snapshot
  - vista del file system prima che occorra un insieme di cambiamente (i.e., ad un certo istante di tempo)

- Duplicazione automatica delle scritture tra siti separati
  - Per ridondanza e disaster recovery
  - Può essere sincrona o asincrona

- Dischi di hot spare (di ricambio)
  - non usati per dati, ma solo in caso di fallimento per replicare il disco fallito e ricostruire il RAID set se possibile
  - Diminuisce il mean time to repair

---

## Pagina 392

Estensioni

- RAID da solo non previene o trova tutti gli errori, solo errori di disk failures
- Solaris ZFS ha approccio innovativo
  - Aggiunge un checksum ad ogni dato e metadato
    - Checksum del blocco mantenuto in blocco separato: nel puntatore al blocco
  - Se checksum non corrisponde può trovare e correggere errori

---

## Pagina 393

Estensioni

- Solaris ZFS gestisce in modo flessibile anche il file system su volumi e partizioni
  - Dischi allocate in pool
  - Filesystem allocati su un pool condivide quel pool dove lo spazio si usa e rilascia come con le chiamate `malloc()` e `free()`
  - Non c’è bisogno di fare resize o riallocazione del file system sui volumi

(a) Traditional volumes and file systems.

(b) ZFS and pooled storage.

---

