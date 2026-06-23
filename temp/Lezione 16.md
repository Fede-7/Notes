Ecco il contenuto delle slide convertito in un documento Markdown professionale, ottimizzato per la lettura su tablet.

# Deadlocks

## Introduzione e Obiettivi

Il presente documento analizza il fenomeno dei **Deadlocks**, esplorando la loro caratterizzazione, il modello di sistema, e i diversi metodi di gestione, inclusi la prevenzione, l'evitamento, il rilevamento e il ripristino.

**Obiettivi del corso:**
- Descrivere i **deadlock**, che impediscono ad un insieme di thread di eseguire il loro compito.
- Presentare metodi per **prevenire**, **identificare**, **evitare** e **recuperare** i deadlock.

---

## Esempi Pratici in Ambiente Posix

### Esempio di due thread in deadlock con mutex Posix

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

## Livelock

Il **Livelock** rappresenta un'altra forma di fallimento di **Liveness**. 

In questa situazione, un gruppo di thread non è bloccato, ma non procede nell'esecuzione. Questo accade a causa di un continuo tentativo di eseguire un'azione che fallisce, impedendo di avanzare.

**Esempio analogico:** Due persone in un corridoio che non riescono ad evitarsi, muovendosi continuamente di lato.

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

*Nota: In alcuni casi, questo fenomeno si può risolvere con la **randomizzazione** (ad esempio, tramite un periodo di backoff in protocolli di rete).*

---

## Caratterizzazione del Deadlock

Un deadlock avviene se le seguenti proprietà sono verificate contemporaneamente (**condizioni di Coffman**):

- **Mutual exclusion**: almeno una risorsa deve essere tenuta in modalità esclusiva: solo un processo alla volta può usare la risorsa.
- **Hold and wait**: almeno un thread deve mantenere almeno una risorsa ed essere in attesa di avere una risorsa aggiuntiva tenuta da altri processi.
- **No preemption**: le risorse non possono essere prelazionate - una risorsa può essere rilasciata solo dal processo che la detiene dopo che tale processo ha completato il suo task.
- **Circular wait**: esiste un insieme $\{P_0, P_1, \ldots, P_n\}$ di processi in attesa mutua, tali che $P_0$ è in attesa di una risorsa che è tenuta da $P_1$, $P_1$ attende la risorsa di $P_2$, …, $P_{n-1}$ attende la risorsa di $P_n$, e $P_n$ attenda la risorsa di $P_0$.

*Nota: Le condizioni non sono tutte indipendenti (l'ultima implica hold and wait), ma è utile considerarle tutte.*

---

## Modello del Sistema

I sistemi forniscono risorse di vari tipi $R_1, R_2, \ldots, R_m$ (come cicli CPU, spazio di memoria, dispositivi I/O).

Ogni tipo di risorsa $R_i$ ha $W_i$ istanze. Ogni processo utilizza una risorsa seguendo questo ciclo:
1. **request**
2. **use**
3. **release**

---

## Grafo di Allocazione delle Risorse

Il sistema può essere modellato come un insieme di nodi $V$ e un insieme di archi $E$.

Il set $V$ è partizionato in due tipi:
- $P = \{P_1, P_2, \ldots, P_n\}$, insieme di tutti i processi nel sistema.
- $R = \{R_1, R_2, \ldots, R_m\}$, insieme di tutti i tipi di risorse del sistema.

**Tipi di archi:**
- **request edge**: archi diretti $P_i \rightarrow R_j$
- **assignment edge**: archi diretti $R_j \rightarrow P_i$

### Rappresentazione Grafica
- **Processo**: rappresentato come nodo.
- **Tipo di risorsa**: rappresentato con il numero di istanze disponibili.
- **$P_i$ richiede istanza di $R_j$**: indicato con un arco verso la risorsa.
- **$P_i$ detiene un’istanza di $R_j$**: indicato con un arco dalla risorsa al processo.

---

## Analisi dei Cicli e Deadlock

**Regola fondamentale:** Senza cicli non c’è deadlock.

Consideriamo i seguenti esempi:
$T = \{T_1, T_2, T_3\}$
$R = \{R_1, R_2, R_3, R_4\}$
$E = \{T_1 \rightarrow R_1, T_2 \rightarrow R_3, R_1 \rightarrow T_2, R_2 \rightarrow T_2, R_2 \rightarrow T_1, R_3 \rightarrow T_3\}$

**Considerazioni importanti:**
- Il ciclo è una **condizione necessaria ma non sufficiente**.
- Se le risorse sono **uniche**, la presenza di un ciclo implica necessariamente un deadlock.

### Esempio di Deadlock
Si introduca un ciclo di Deadlock:
$$T_1 \rightarrow R_1 \rightarrow T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_1$$
$$T_2 \rightarrow R_3 \rightarrow T_3 \rightarrow R_2 \rightarrow T_2$$

In questo scenario, i tre thread sono in deadlock.

### Ciclo senza Deadlock
È possibile avere un ciclo senza che si verifichi un deadlock. Ad esempio, se $P_4$ può rilasciare $R_2$ rompendo il ciclo per consentire a $P_3$ l’esecuzione, il sistema non è in deadlock.

**Fatti di Base:**
- Se il grafo non ha cicli $\Rightarrow$ **non ha deadlock**.
- Se il grafo contiene un ciclo $\Rightarrow$
  - Se esiste una **sola istanza** per tipo di risorsa $\Rightarrow$ **deadlock**.
  - Se esistono **molte istanze** per tipo di risorsa $\Rightarrow$ c’è la possibilità di un deadlock, ma non si ha necessariamente il deadlock.

---

## Metodi di Gestione Deadlocks

Esistono tre approcci principali per gestire il problema del deadlock:

1. **Ignorare il problema**: assumere che i deadlocks non si presentino mai. Questo approccio è usato dalla maggior parte dei sistemi operativi, incluso **UNIX**.
2. **Assicurare che il sistema non entri mai in uno stato di deadlock**:
   - **Prevenzione di deadlock (deadlock prevention)**: limitare i modi in cui si fanno le richieste per evitare i deadlock.
   - **Evitamento del deadlock (deadlock avoidance)**: valutare le richieste dinamicamente per evitare situazioni pericolose.
3. **Permettere al sistema di entrare in uno stato di deadlock per poi recuperare (deadlock recovery)**.

---

## Prevenzione Deadlock

L'obiettivo è limitare i modi in cui può essere fatta la richiesta tenendo presente le condizioni di deadlock:

- **Mutual Exclusion**: non richiesta per risorse condivisibili (es. file in read-only). Tuttavia, non è possibile limitare le richieste solo a risorse non condivisibili.
- **Hold and Wait**: deve essere garantito che quando un processo richiede una risorsa, non detiene altre risorse.
  - *Soluzione A:* Imporre al processo di richiedere e allocare tutte le sue risorse prima che inizi l'esecuzione.
  - *Soluzione B:* Consentire al processo di richiedere risorse solo quando non ne è stata allocata alcuna (le usa e le rilascia).
  - *Limite:* Non pratico a causa del basso utilizzo delle risorse e della possibile **starvation**.

- **No Preemption**: se un processo che detiene risorse richiede un’altra risorsa che non può essere immediatamente data, allora tutte le risorse devono essere rilasciate.
  - Le risorse prelazionate vengono aggiunte alla lista delle risorse in attesa.
  - Il processo verrà riavviato solo quando può ottenere le vecchie più le nuove risorse.
  - *Limite:* Funziona solo per risorse facilmente recuperabili (CPU, registry, DB, etc.), non per mutex o semafori.

- **Attesa Circolare**: imposizione di un ordine totale a tutti i tipi di risorse. Ogni processo deve richiedere le risorse in un ordine di enumerazione crescente.
  - Data la serie $R = \{R_1, R_2, \dots, R_m\}$, si assegna un numero di ordine $F(R)$.
  - Un processo può richiedere risorse solo rispettando l'ordine: se la nuova risorsa è $R_j$ e la risorsa attuale è $R_i$, deve valere $F(R_j) > F(R_i)$.

**Dimostrazione della prevenzione:**
Dato un ordine totale $F$ sulle risorse, se ogni processo richiede risorse in ordine crescente rispetto a $F$, un ciclo $P_1 \rightarrow P_2 \rightarrow \cdots \rightarrow P_n \rightarrow P_1$ implicherebbe:
$$F(R_1) < F(R_2) < \cdots < F(R_n) < F(R_1)$$
Ciò contraddice la transitività e l’anti-riflessività di $F$.

---

## Esempi di Lock Ordering

### Esempio di Deadlock con Mutex
In questo scenario, due thread cercano di acquisire due mutex in ordine opposto:
- Thread 1: `first_mutex` $\rightarrow$ `second_mutex`
- Thread 2: `second_mutex` $\rightarrow$ `first_mutex`

### Soluzione tramite Lock Ordering
Assegnando un valore di ordine:
- $F(\text{first\_mutex}) = 1$
- $F(\text{second\_mutex}) = 5$

Occorre un **lock-ordering** globale:
```cpp
if (from.id < to.id) {
    acquire(lock(from));
    acquire(lock(to));
} else {
    acquire(lock(to));
    acquire(lock(from));
}
```
Questo garantisce che i processi accedano sempre alle risorse nello stesso ordine, eliminando la possibilità di un ciclo di attesa.

---

## Evitamento del Deadlock (Deadlock Avoidance)

L'evitamento richiede che il sistema possieda **informazioni a priori addizionali**:
- I processi devono dichiarare il **massimo numero di risorse necessarie**.
- L’algoritmo esamina **dinamicamente** lo stato di allocazione per assicurare che non si entri mai in una situazione di **circular-wait**.
- Lo **stato di allocazione delle risorse** è definito dal numero di risorse disponibili, allocate e dalle massime richieste per processo.

### Stato Sicuro
Quando un processo richiede una risorsa, il sistema decide se l’allocazione immediata lascia il sistema in uno **stato sicuro**.

Un sistema è in uno **stato sicuro** se esiste una sequenza $\langle P_1, P_2, \ldots, P_n \rangle$ di TUTTI i processi tale che per ogni $P_i$, le risorse che $P_i$ può ancora richiedere possono essere soddisfatte dalle risorse correntemente disponibili + le risorse tenute da tutti i $P_j$ (con $j < i$).

**In sintesi:**
- Se le risorse richieste da $P_i$ non sono disponibili, $P_i$ attende finché tutti i $P_j$ hanno finito.
- Quando $P_j$ finisce, $P_i$ ottiene le risorse, termina e rilascia le proprie.
- Il processo successivo $P_{i+1}$ può poi procedere, e così via.

**Fatti di Base sull'Evitamento:**
- Stato sicuro $\Rightarrow$ non deadlock.
- Stato non sicuro $\Rightarrow$ possibilità di deadlock.
- **Evitamento** $\Rightarrow$ assicurare che il sistema non entri mai in uno stato non sicuro.

---

## Algoritmi di Evitamento

- **Singola istanza di un tipo di risorsa**: si usa un **Resource-Allocation Graph**.
- **Multiple istanze di tipo di risorsa**: si usa l’**Algoritmo del Banchiere**.

### Grafo di Allocazione e Claim Edge
Si introduce la **claim edge** $P_i \rightarrow R_j$ (linea tratteggiata) che indica che il processo $P_j$ *potrebbe* richiedere la risorsa $R_j$.
- La **claim edge** diventa **request edge** quando la richiesta viene effettuata.
- La **request edge** diventa **assignment edge** quando la risorsa viene allocata.
- Quando la risorsa viene rilasciata, l'**assignment edge** torna a essere **claim edge**.

**Regola:** La richiesta può essere garantita solo se la trasformazione dell'arco di richiesta in un assegnamento non porta alla formazione di un ciclo. Altrimenti, la richiesta viene messa in attesa.

---

## Algoritmo del Banchiere (Banker's Algorithm)

Applicabile per **multiple istanze** di risorse. Ogni processo deve dichiarare a priori il massimo utilizzo di risorse. Il sistema controlla se l'assegnazione lascia lo stato sicuro; se non è sicuro, la richiesta viene messa in attesa finché qualche processo libera risorse.

### Strutture Dati
Sia $n$ = numero di processi ed $m$ = numero di tipi di risorse:

- **Available**: Vettore di lunghezza $m$. $Available[j] = k$ significa che ci sono $k$ istanze della risorsa $R_j$ disponibili.
- **Max**: Matrice $n \times m$. $Max[i,j] = k$ significa che il processo $P_i$ potrebbe richiedere al massimo $k$ istanze di $R_j$.
- **Allocation**: Matrice $n \times m$. $Allocation[i,j] = k$ significa che $P_i$ ha correntemente allocate $k$ istanze di $R_j$.
- **Need**: Matrice $n \times m$. $Need[i,j] = Max[i,j] - Allocation[i,j]$.

### Algoritmo di Safety
1. Inizializza $Work = Available$ e $Finish[i] = \text{false}$ per tutti i processi.
2. Trova un indice $i$ tale che $Finish[i] = \text{false}$ e $Need_i \leq Work$.
3. Se esiste, $Work = Work + Allocation_i$, $Finish[i] = \text{true}$ e torna al passo 2.
4. Se tutti gli $i$ hanno $Finish[i] = \text{true}$, il sistema è in uno **stato sicuro**.

---

## Esempio Algoritmo del Banchiere

**Dati iniziali:** 5 processi ($P_0 \dots P_4$), 3 tipi di risorse (A, B, C).

| | Allocation | Max | Available |
| :--- | :--- | :--- | :--- |
| | A B C | A B C | A B C |
| $P_0$ | 0 1 0 | 7 5 3 | 3 3 2 |
| $P_1$ | 2 0 0 | 3 2 2 | |
| $P_2$ | 3 0 2 | 9 0 2 | |
| $P_3$ | 2 1 1 | 2 2 2 | |
| $P_4$ | 0 0 2 | 4 3 3 | |

**Matrice Need (Max - Allocation):**
$P_0: [7,4,3], P_1: [1,2,2], P_2: [6,0,0], P_3: [0,1,1], P_4: [4,3,1]$

**Verifica Sicurezza:**
La sequenza $\langle P_1, P_3, P_4, P_2, P_0 \rangle$ soddisfa i criteri:
1. $P_1$ ne prende 2 e restituisce 4 $\Rightarrow$ Work = [4, 5, 2]
2. $P_3$ ne prende 2 e restituisce 4 $\Rightarrow$ Work = [4, 6, 3]
... e così via fino al completamento.

---

## Rilevazione Deadlock (Deadlock Detection)

Si permette al sistema di entrare nello stato di deadlock. Servono quindi algoritmi di rilevamento e metodi di recupero.

**Costi:**
- Monitoraggio (strutture dati e algoritmi).
- Potenziale perdita di dati durante il recovery.

### Casi di Rilevamento
1. **Istanza Singola**: Si usa il **grafo wait-for** (grafo delle attese). Si rimuovono i nodi delle risorse e si tengono solo i processi. $P_i \rightarrow P_j$ se $P_i$ sta aspettando $P_j$.
   - Periodicamente si cerca un ciclo. Se c'è un ciclo, c'è un deadlock.
   - Esempio: Il toolkit **BCC su Linux** traccia l'uso dei mutex e costruisce il grafo delle attese.

2. **Multiple Istanze**: Si usano le strutture dati dell'algoritmo del banchiere (Available, Allocation, Request).
   - **Algoritmo di Rilevamento**: Simile all'algoritmo di safety, ma utilizza la matrice **Request** invece di Need.

**Complessità:** Entrambi gli algoritmi richiedono un ordine di $O(m \times n^2)$ operazioni.

---

## Ripristino dal Deadlock (Deadlock Recovery)

Quando viene trovato un deadlock, si può intervenire manualmente o automaticamente tramite due modalità:

### 1. Terminazione di Processo
- **Abort di tutti i processi**: Molto dispendioso per la computazione persa.
- **Abort uno alla volta**: Si terminano i processi finché il ciclo viene eliminato (richiede check continui).

**Criteri di scelta della "vittima":**
- Priorità del processo.
- Tempo di lavoro e prossimità al completamento.
- Risorse già usate vs risorse necessarie.
- Numero di processi che necessiterebbero di essere terminati.
- Natura del processo (interattivo o batch).

### 2. Prelazione di Risorse (Resource Preemption)
Si selezionano risorse da prelazionare finché il deadlock non è risolto.

- **Selezionare una vittima**: quale risorsa e quale processo prelazionare per minimizzare i costi.
- **Rollback**: il processo deve tornare in uno stato sicuro (metodo più semplice: ripartire da capo).
- **Starvation**: per evitarlo, se si usa una funzione di costo, si può includere il numero di rollback precedenti nei fattori di costo.

---

## Riassunto

Il percorso di analisi dei Deadlocks include:
- **Definizione** e **Condizioni** (Coffman).
- **Modellazione** tramite grafi di allocazione e cicli.
- **Prevenzione** basata sulle quattro condizioni.
- **Evitamento** tramite stato sicuro e Algoritmo del Banchiere.
- **Rilevamento** per risorse singole e multiple.
- **Recupero** tramite terminazione o prelazione.