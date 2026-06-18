## Pagina 1

Deadlocks

---

## Pagina 2

Deadlocks

- Modello di Sistema
- Caratterizzazione dei deadlock
- Metodi di gestione dei deadlock
- Prevenzione deadlock
- Evitamento deadlock
- Rilevamento deadlock
- Ripristino dai deadlock

---

## Pagina 3

Obiettivi

- Descrivere i deadlock, che impediscono ad un insieme di thread di eseguire il loro compito
- Presentare metodi per prevenire, identificare, evitare, recuperare i deadlock

---

## Pagina 4

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

## Pagina 5

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

## Pagina 6

Caratterizzazione Deadlock

Un deadlock avviene se le seguenti proprietà sono verificate contemporaneamente (condizioni di Coffman)

- **Mutual exclusion**: almeno una risorsa deve essere tenuta in modalità esclusiva: solo un processo alla volta può usare la risorsa
- **Hold and wait**: almeno un thread deve mantenere almeno una risorsa ed essere in attesa di avere una risorsa aggiuntiva tenuta da altri processi
- **No preemption**: le risorse non possono essere prelazionate - una risorsa può essere rilasciata solo dal processo che la detiene dopo che tale processo ha completato il suo task
- **Circular wait**: esiste un insieme $\{P_0, P_1, \ldots, P_n\}$ di processi in attesa mutua, tali che $P_0$ è in attesa di una risorsa che è tenuta da $P_1$, $P_1$ attende la risorsa di $P_2$, …, $P_{n-1}$ attende la risorsa di $P_n$, e $P_n$ attenda la risorsa di $P_0$.

Le condizioni non sono tutte indipenenti (ultima implica hold and wait), ma è utile considerarle tutte

---

## Pagina 7

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

## Pagina 8

Grafo di Allocazione delle Risorse

Insieme di nodi $V$ e insieme di archi $E$.

- $V$ partizionata in due tipi:
  - $P = \{P_1, P_2, \ldots, P_n\}$, insieme di tutti i processi nel sistema
  - $R = \{R_1, R_2, \ldots, R_m\}$, insieme di tutti i tipi di risorse del sistema

- request edge – archi diretti $P_i \rightarrow R_j$
- assignment edge – archi diretti $R_j \rightarrow P_i$

---

## Pagina 9

Grafo di Allocazione delle Risorse

□ Processo

□ Tipo di risorsa con 4 istanze

□ $P_i$ richiede istanza di $R_j$

□ $P_i$ detiene un’istanza di $R_j$

---

## Pagina 10

Esempio di un Grafo di Allocazione di Risorse

Senza cicli non c’è deadlock

Deadlock?

$T = \{T_1, T_2, T_3\}$
$R = \{R_1, R_2, R_3, R_4\}$
$E = \{T_1 \rightarrow R_1, T_2 \rightarrow R_3, R_1 \rightarrow T_2, R_2 \rightarrow T_2, R_2 \rightarrow T_1, R_3 \rightarrow T_3\}$

---

## Pagina 11

Esempio di un Grafo di Allocazione di Risorse

Senza cicli non c’è deadlock

Ciclo è condizione necessaria ma non sufficiente

Se risorse uniche?

- $T = \{T_1, T_2, T_3\}$
- $R = \{R_1, R_2, R_3, R_4\}$
- $E = \{T_1 \rightarrow R_1, T_2 \rightarrow R_3, R_1 \rightarrow T_2, R_2 \rightarrow T_2, R_2 \rightarrow T_1, R_3 \rightarrow T_3\}$

---

## Pagina 12

Grafo di Allocazione di Risorse con un Deadlock

Si introduca un ciclo Deadlock?

$$T_1 \rightarrow R_1 \rightarrow T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_1$$
$$T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_2$$

---

## Pagina 13

Grafo di Allocazione di Risorse con un Deadlock

Si introduca un ciclo

I tre thread sono in deadlock

$$T_1 \rightarrow R_1 \rightarrow T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_1$$
$$T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_2$$

---

## Pagina 14

Grafo con un ciclo ma senza deadlock

... anche in questo caso ciclo

Deadlock?

---

## Pagina 15

Grafo con un ciclo ma senza deadlock

… anche in questo caso ciclo

Deadlock?

P₄ può rilasciare R₂ rompendo il ciclo per consentire a P₃ l’esecuzione

---

## Pagina 16

Fatti di Base

□ Se il grafo non ha cicli ⇒ non ha deadlock
□ Se il grafo contiene un ciclo ⇒
  □ Se esiste una sola istanza per tipo di risorsa, allora deadlock
  □ Se molte istanze per tipo di risorsa, c’è possibilità di un deadlock, ma non si ha necessariamente il deadlock

---

## Pagina 17

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

## Pagina 18

Prevenzione Deadlock

Limitare i modi in cui può essere fatta la richiesta tenendo presente le condizioni di deadlock

□ Mutual Exclusion – non richiesta per risorse condivisibili (e.g., read-only files)
  □ .. però non si possono limitare le richieste solo a risorse non condivisibili

□ Hold and Wait – deve garantire che quando un processo richiede una risorsa, non detiene altre risorse
  □ Imporre al processo di richiedere e allocare tutte le sue risorse prima che inizi l'esecuzione
  □ Consentire al processo di richiedere risorse solo quando al processo non ne è stata allocata alcuna, le usa e le rilascia
  □ Non pratico: basso utilizzo delle risorse; possibile starvation

---

## Pagina 19

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

## Pagina 20

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

## Pagina 21

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

## Pagina 22

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

## Pagina 23

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

## Pagina 24

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

## Pagina 25

Deadlock Avoidance

Il Sistema deve avere informazione a priori addizionale:

- Il modello più semplice ed utile richiede ai processi di dichiarare il massimo numero di risorse necessarie per tipo di processo
- L’algoritmo di deadlock-avoidance esamina dinamicamente lo stato di allocazione delle risorse per assicurare che non si entri mai in una situazione di circular-wait
- Lo stato di allocazione delle risorse (resource-allocation state) è dato dal numero di risorse disponibile e allocate, e dale massime richieste per processo

---

## Pagina 26

Stato Sicuro

- Quando un processo richiede una risorsa disponibile, il sistema deve decidere se l’allocazione immediata lascia il sistema in uno stato sicuro

- Un sistema è in uno **stato sicuro** se esiste una sequenza $<P_1, P_2, \ldots, P_n>$ di TUTTI i processi nel sistema tali che per ogni $P_i$, le risorse che $P_i$ può ancora richiedere possono essere soddisfatte dalle risorse correntemente disponibili + le risorse tenute da tutti i $P_j$, con $j < i$

- Cioè:
  - Se le risorse richieste da $P_i$ non sono immediatamente disponibili, allora $P_i$ può apettare finché tutti i $P_j$ hanno finito
  - Quando $P_j$ ha finito, $P_i$ può ottenere le risorse richieste, eseguirle, rilasciando le risorse allocate e terminare
  - Quando $P_i$ termina, $P_{i+1}$ può ottenere le risorse necessarie, e così via ...

---

## Pagina 27

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

## Pagina 28

Fatti di Base

- Se un sistema è in stato sicuro ⇒ non deadlock
- Se un sistema è in stato non sicuro ⇒ possibilità di deadlock
- Evitamento ⇒ assicurare che un sistema non entri mai in uno stato non sicuro

---

## Pagina 29

Safe, Unsafe, Deadlock State

deadlock

unsafe

safe

---

## Pagina 30

Algoritmo di Avoidance

- Singola istanza di un tipo di risorsa
  - Usa un resource-allocation graph

- Multiple istanze di tipo di risorsa
  - Usa l’algoritmo del banchiere

---

## Pagina 31

Schema con grafo di allocazione

- Si introduce la claim edge $P_i \rightarrow R_j$ che indica che il processo $P_j$ potrebbe richiedere la risorsa $R_j$; (linea tratteggiata)
- La claim edge si converte in request edge quando un processo richiede la risorsa
- La request edge si converte in assignment edge quando la risorsa è allocata al processo
- Quando la resource è rilasciata dal processo, l’assignment edge si riconverte in claim edge
- Le risorse devono essere richieste a priori nel sistema

---

## Pagina 32

Resource-Allocation Graph

assignment edge
request edge
claim edge
claim edge

---

## Pagina 33

Stato unsafe in Resource-Allocation Graph

- assignment edge
- request edge
- claim edge
- assignment edge

---

## Pagina 34

Algoritmo di Resource-Allocation Graph

- Supponi che il processo $P_i$ richieda una risorsa $R_j$
- La richiesta può essere garantita solo se trasformando l’arco di richiesta in un assegnamento non porta alla formazione di un ciclo nel grafo di allocazione delle risorse
- Altrimenti la richiesta viene messa in attesa
- Complessità di rilevare un ciclo è n^2 con n numero di thread del sistema

---

## Pagina 35

Algoritmo del Banchiere

- Allocazione delle risorse della banca per soddisfare tutti i clienti
- Applicabile per multiple istanze
- Ogni processo deve dichiarare a priori il massimo utilizzo di risorse
- Quando un processo richiede una risorsa potrebbe dover aspettare
- Quando un processo ottiene tutte le sue risorse deve restituirle in un tempo finito

---

## Pagina 36

Algoritmo del Banchiere

- Quando un processo richiede un insieme di risorse, il Sistema deve controllare se l’assegnazione lascia il Sistema in uno stato sicuro

- Se lo stato è sicuro le risorse sono allocate altrimenti la richiesta viene messa in attesa finché qualche processo libera delle risorse aggiuntive

- Si introducono diverse strutture dati per rappresentare lo stato del sistema

---

## Pagina 37

Strutture Dati per l’Algoritmo del Banchiere

Sia $n$ = numero di processi ed $m$ = numero di tipi di risorse.

□ **Available**: Vettore di lunghezza $m$. Se available $[j] = k$, ci sono $k$ istanze della risorsa di tipo $R_j$ disponibili

□ **Max**: matrice $n \times m$. Se $Max[i,j] = k$, allora il processo $P_i$ potrebbe richiedere al massimo $k$ istanze della risorsa di tipo $R_j$

□ **Allocation**: matrice $n \times m$. Se Allocation[i,j] = $k$ allora $P_i$ ha correntemente allocate $k$ istanze di $R_j$

□ **Need**: matrice $n \times m$. Se Need[i,j] = $k$, allora $P_i$ potrebbe aver bisogno di $k$ più istanze di $R_j$ per complare il suo task

$$Need[i,j] = Max[i,j] - Allocation[i,j]$$

---

## Pagina 38

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

## Pagina 39

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

## Pagina 40

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

## Pagina 41

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

## Pagina 42

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

## Pagina 43

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

## Pagina 44

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

## Pagina 45

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

## Pagina 46

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

## Pagina 47

Istanza Singola di Ogni Tipo di Risorsa

- Si usa una variante del grafo di allocazione delle risorse chiamato grafo wait-for (grafo delle attese)
  - Si rimuovono i nodi delle risorse che si bypassano con archi tra processi
  - Nodi sono solo per i processi
  - $P_i \rightarrow P_j$ se $P_i$ sta aspettando $P_j$

---

## Pagina 48

Grafo di Allocazione delle e Grafo delle Attese

Grafo di allocazione delle risorse

Grafo delle Attese corrispondente

---

## Pagina 49

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

## Pagina 50

Molte Istanze di un Tipo di Risorsa

Nel caso di più istanze occorrono più strutture dati come per l’algoritmo del banchiere

□ Available: un vettore di lunghezza $m$ che indica il numero di risorse disponibili per ogni tipo di risorsa

□ Allocation: una matrice $n \times m$ definisce il numero di risorse per tipo correntemente allocato ad ogni processo

□ Request: una matrice $n \times m$ indica la richiesta corrente di ogni processo. Se $Request[i][j] = k$, allora il processo $P_i$ sta richiedendo $k$ più istanze di risorsa di tipe $R_j$.

---

## Pagina 51

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

## Pagina 52

Algoritmo di Rilevamento

3. Work = Work + Allocationᵢ
Finish[i] = true
vai al passo 2

Rilasciate le risorse dopo il completamento, si assume che non siano necessarie altre risorse da allocare per finire il processamento

4. Se Finish[i] == false, per qualche $i$, $1 \leq i \leq n$, allora il sistema è in uno stato di deadlock. Inoltre, se Finish[i] == false, allora $P_i$ è in deadlocked

Algoritmo richiede un ordine di $O(m \times n^2)$ operazioni per rilevare se il sistema è in stato di deadlock

---

## Pagina 53

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

## Pagina 54

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

## Pagina 55

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

## Pagina 56

Ripristino dal Deadlock

- Quando viene trovato un deadlock va gestito:
  - Avvertire operatore che gestisce a mano
  - Gestione automatica

- Due modalità principali di gestione:
  - Terminare uno o più processi coinvolti
  - Prelazionare risorse dai processi coinvolti nel deadlock

---

## Pagina 57

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

## Pagina 58

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

## Pagina 59

Riassunto

- Definizione di deadlock
- Condizioni per avere un deadlock
- Grafi di allocazione delle risorse e cicli
- Prevenzione dei deadlock in base alle condizioni di deadlock
- Metodi di evitamento del deadlock per risorse singole (grafo delle allocazioni) e multiple (algoritmo del banchiere)
- Metodi di deadlock detection per risorse singole e multiple
- Metodi di deadlock recovery

---

