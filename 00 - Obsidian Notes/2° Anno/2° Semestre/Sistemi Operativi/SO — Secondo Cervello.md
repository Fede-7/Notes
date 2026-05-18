---
tags: [SO, MemoVia, secondo-cervello]
---

# 🧠 SO — Secondo Cervello

> [!abstract] Come leggere questo file
> Ogni sezione è una **parcella autonoma**. Leggi dall'alto. I link `[[ ]]` ti portano al concetto collegato. I callout colorano il tipo di informazione: **Ciano = essenza**, **Verde = formula/dato esatto**, **Viola = metafora/esempio**, **Rosso = trappola da evitare**.

---

# 🏛️ PILASTRO 1 — CHE COS'È UN SISTEMA OPERATIVO
*Lezioni 0 → 2*

---

## L1 — Il SO è un intermediario

> [!abstract] Nodo Nucleare
> Il SO è il **primo strato software** tra hardware e applicazioni. Fa due cose: **gestisce le risorse** (CPU, RAM, disco) e **nasconde la complessità** dell'hardware all'utente.

> [!example] Metafora: il SO è il direttore d'orchestra
> L'hardware sono i musicisti: ognuno fa la sua cosa. Il SO è il direttore: decide chi suona quando, evita che si pestino i piedi, e dà un'interfaccia semplice al pubblico (le applicazioni).

**Struttura a cipolla:**
- Hardware → Kernel → System Programs → Applicazioni Utente

**Modalità operative (Dual-Mode):**
- `User Mode` (bit=1) — programmi normali, istruzioni privilegiate vietate
- `Kernel Mode` (bit=0) — pieno controllo hardware, tutto permesso

> [!quote] Regola fondamentale
> Il passaggio da User a Kernel Mode avviene **solo** tramite: Interrupt hardware | Trap (errore) | System Call

> [!danger] Trappola R.I.P.
> Non confondere "kernel" con "SO". Il SO include anche shell, librerie, utility. Il kernel è solo il nucleo sempre in RAM.

---

## L1 — System Call: il portone del kernel

> [!abstract] Nodo
> La **System Call** è l'unico modo legale per un programma utente di chiedere servizi al kernel. È una trap controllata: il programma dice "voglio leggere un file" e il kernel lo fa per lui.

> [!example] Metafora: sportello bancario
> Tu (user mode) non entri nel caveau (kernel). Passi la richiesta allo sportellista (syscall), lui va nel caveau e ti riporta il risultato. Non sai *come* lo fa, e va bene così.

**Flusso di una syscall:**
1. Programma carica il numero della syscall in un registro (es. `rax`)
2. Esegue `syscall` / `int 0x80` → la CPU entra in kernel mode
3. Il kernel legge il numero, esegue la funzione
4. Ritorna in user mode con il risultato

> [!quote] Gerarchia delle interfacce
> `API` (alta astrazione, portabile) → `ABI` (livello binario, dipende dall'architettura) → `System Call` (livello hardware)
> Esempio: `printf()` [API C] → `write()` [ABI POSIX] → `sys_write` [syscall Linux]

---

## L2 — Struttura interna del kernel

> [!abstract] Nodo
> Esistono 3 filosofie per organizzare il kernel. La scelta influenza velocità, stabilità e manutenibilità.

| Tipo | Logica | Pro | Contro |
|---|---|---|---|
| **Monolitico** (Linux) | Tutto in kernel mode | Velocissimo | Un bug in un driver → crash totale |
| **Microkernel** (Mach) | Solo IPC + mem in kernel | Stabile, modulare | Lento (troppe syscall) |
| **Modulare** (Linux moderno) | Monolitico + LKM caricabili | Flessibile | Compromesso |

> [!example] Metafora: monolitico = palazzo, microkernel = modulare IKEA
> Il palazzo è solido ma se crolla un muro, crolla tutto. IKEA: monti, smonti, sostituisci un modulo senza buttare tutto.

> [!danger] Trappola
> Linux è **monolitico modulare**: non è un microkernel anche se ha i moduli. I moduli girano ancora in kernel mode.

---

# 🔄 PILASTRO 2 — PROCESSI E THREAD
*Lezioni 2 → 7*

---

## L2 — Il Processo: programma in esecuzione

> [!abstract] Nodo
> Un **processo** è un programma caricato in RAM più tutto il suo stato. Due esecuzioni dello stesso programma = due processi diversi.

**Layout di memoria di un processo (dal basso verso l'alto):**
```
[ Stack ]   ← cresce verso il basso (variabili locali, return address)
    ↕
  [vuoto]
    ↕  
[ Heap  ]   ← cresce verso l'alto (malloc, new)
[ BSS   ]   ← variabili globali non inizializzate
[ Data  ]   ← variabili globali inizializzate
[ Text  ]   ← codice eseguibile (read-only)
```

> [!quote] PCB — Process Control Block
> Il kernel tiene traccia di ogni processo con una struttura C chiamata PCB (in Linux: `task_struct`). Contiene: PID, stato, PC, registri, info scheduling, tabella file aperti, mappa memoria.

**Ciclo di vita di un processo:**
`New` → `Ready` → `Running` → `Waiting` → `Terminated`

> [!example] Metafora: Context Switch = cambio turno in cucina
> Due cuochi (processi) usano lo stesso forno (CPU). Quando il cuoco A smette, il caposala (scheduler) salva il suo stato (cosa stava cucinando, a che punto era) nel suo quaderno (PCB), poi lo riprende il cuoco B.

---

## L2 — fork, exec, wait: la trinità POSIX

> [!abstract] Nodo
> Questi tre comandi sono la base per creare qualsiasi processo su Unix/Linux.

> [!quote] Come funzionano
> - `fork()` → duplica il processo corrente. Ritorna **0 al figlio**, **PID_figlio al padre**
> - `exec()` → sostituisce lo spazio di memoria con un nuovo programma (non crea un nuovo processo)
> - `wait()` → il padre si blocca finché il figlio non termina, raccoglie l'exit status

> [!example] Metafora: fork = fotocopiatrice, exec = sovrascrittura
> `fork()` fotocopiamo il processo (stessa memoria, stesso codice). Il figlio poi chiama `exec()` e "sovrascrive" se stesso con un nuovo programma. La shell funziona esattamente così: fork → exec → wait.

> [!danger] Trappola critica: Zombie e Orfani
> - **Zombie**: il figlio è morto ma il padre non ha fatto `wait()`. Il PCB resta in RAM (spreco). Fix: chiama `wait()`.
> - **Orfano**: il padre muore prima del figlio. Il figlio viene adottato da `init`/`systemd` (PID=1) che farà la `wait()` per lui.

**Copy-on-Write (COW):** dopo `fork()`, padre e figlio condividono le stesse pagine fisiche in sola lettura. Solo alla prima **scrittura** il kernel duplica quella pagina. → fork() è quasi gratuita.

---

## L3 — IPC: come parlano i processi

> [!abstract] Nodo
> I processi sono **isolati per design** (memoria separata). Per comunicare, usano l'IPC (Inter-Process Communication). Due famiglie: **Shared Memory** (veloce, manuale) e **Message Passing** (sicuro, automatico).

### Shared Memory

> [!quote] API POSIX
> `shm_open(name, flags, mode)` → crea/apre oggetto
> `ftruncate(fd, size)` → imposta dimensione
> `mmap(addr, len, prot, MAP_SHARED, fd, 0)` → mappa nello spazio virtuale
> `munmap()` + `shm_unlink()` → pulizia

> [!example] Metafora: lavagna condivisa
> Due processi scrivono sulla stessa lavagna (memoria fisica). Velocissimo. Ma se scrivono insieme, si sovrascrivono → serve un semaforo (vedi [[#L11 — Semafori]])

### Pipe Anonime

> [!quote] Regole d'oro
> - `pipe(fd[2])` → `fd[0]` = lettura, `fd[1]` = scrittura
> - Solo tra processi **imparentati** (padre-figlio)
> - Chiudere sempre il lato non usato → altrimenti `read()` non vede mai EOF

> [!example] Metafora: tubo dell'acqua in un palazzo
> Uno scrive dall'alto (fd[1]), l'altro legge dal basso (fd[0]). Il tubo è nel kernel. Se non chiudi il rubinetto (il lato di scrittura non usato), il lettore aspetta acqua che non arriverà mai → deadlock.

### Named Pipe (FIFO) e Socket

> [!quote] Differenza chiave
> - **FIFO**: `mkfifo("nome", 0666)` → appare nel filesystem, funziona tra processi non imparentati
> - **Socket**: comunicazione di rete o locale. `SOCK_STREAM` (TCP, affidabile) vs `SOCK_DGRAM` (UDP, pacchetti)

---

## L4 — Shell e Compilazione C

> [!abstract] Nodo
> La shell è un processo come gli altri. Ogni comando che lanci è un `fork() + exec()`. La compilazione C è una pipeline a 4 stadi.

**Pipeline di compilazione:**
```
sorgente.c  →[cpp]→  sorgente.i  →[cc1]→  sorgente.s  →[as]→  sorgente.o  →[ld]→  eseguibile
            Preprocessing    Compilazione      Assembly          Linking
```

> [!quote] Formato ELF (Executable and Linkable Format)
> Il file `.o` e l'eseguibile finale sono in formato ELF. Contiene:
> - **Header**: tipo file, architettura, entry point
> - **.text**: codice macchina
> - **.data**: variabili globali inizializzate
> - **.bss**: variabili globali non inizializzate (spazio riservato, non scritto su disco)
> - **Symbol Table**: nomi di funzioni/variabili per il linker

> [!example] Metafora: linking = assemblare un mobile IKEA
> Hai più sacchetti di viti (file .o). Il linker (ld) li unisce seguendo le istruzioni (symbol table) e produce il mobile finito. Le librerie dinamiche (.so) sono pezzi condivisi che monti solo quando usi il mobile.

> [!danger] Statico vs Dinamico
> - Linking **statico**: tutto il codice della libreria finisce nell'eseguibile → grosso, ma funziona ovunque
> - Linking **dinamico**: l'eseguibile dice "usa libX.so" → piccolo, ma la libreria deve esistere a runtime

---

## L5 — Thread: processi leggeri

> [!abstract] Nodo
> Un thread è un flusso di esecuzione **dentro** un processo. Più thread = stesso codice/heap/dati, ma **stack e registri separati**.

**Cosa condividono i thread dello stesso processo:**
- ✅ Codice (Text segment)
- ✅ Heap e variabili globali
- ✅ File descriptor
- ❌ Stack (ogni thread ha il suo)
- ❌ Registri / Program Counter

> [!quote] Legge di Amdahl — il limite del parallelismo
> $$S \leq \frac{1}{S_{seq} + \frac{1-S_{seq}}{N}}$$
> - $S_{seq}$ = frazione di codice **non parallelizzabile**
> - $N$ = numero di core
> - Se $S_{seq} = 0.1$ (10% seriale), con ∞ core → max speedup = 10x. Mai.

> [!example] Metafora: Amdahl = autostrada con pedaggi
> Puoi aggiungere quante corsie vuoi, ma il pedaggio (parte seriale) è un collo di bottiglia a 1 corsia. Il guadagno totale è limitato dalla parte che non puoi parallelizzare.

**Modelli di mapping thread user ↔ kernel:**
- **1:1** (Linux) → ogni user thread = 1 kernel thread. Vero parallelismo su multicore.
- **M:N** → N user thread su M kernel thread (complesso, raro oggi)

---

## L5/L7 — Pthreads: API POSIX per i thread

> [!quote] Funzioni fondamentali
> ```c
> pthread_create(&tid, NULL, funzione, argomento); // crea thread
> pthread_join(tid, NULL);    // aspetta terminazione
> pthread_self();             // ritorna TID user-level
> syscall(SYS_gettid);        // ritorna TID kernel-level (Linux-only)
> pthread_cancel(tid);        // invia richiesta cancellazione
> pthread_testcancel();       // punto di cancellazione manuale (CPU-bound)
> ```

> [!abstract] Cancellazione Thread: 3 modalità
> - **Disabled**: la richiesta resta pending, il thread ignora tutto
> - **Deferred** (default): il thread termina solo al prossimo *cancellation point* (sleep, I/O, pthread_cond_wait…)
> - **Asynchronous**: il thread muore immediatamente → pericoloso se tiene lock

---

## L7 — Signal Handling nei Thread

> [!abstract] Nodo
> I segnali in ambiente multi-thread seguono regole precise sulla *maschera*.

> [!quote] Regole d'oro sui segnali
> 1. `pthread_kill(tid, SIG)` → manda segnale a un thread specifico
> 2. `kill(pid, SIG)` → manda a tutto il processo → il kernel lo consegna a un thread che non lo maschera
> 3. La maschera impostata **prima** del `pthread_create` → **ereditata** dal figlio
> 4. La maschera impostata **dopo** → vale solo per il thread corrente
> 5. Segnali ordinari (SIGUSR1, SIGINT): **non si accumulano** → N invii = 1 handler invocato

> [!example] Metafora: eredità della maschera
> Se papà mette i tappi alle orecchie (maschera) PRIMA di fare figli → i figli nascono già con i tappi. Se li mette dopo → i figli sentono tutto.

---

# ⚡ PILASTRO 3 — CPU SCHEDULING
*Lezioni 6 → 9*

---

## L6 — Lo Scheduler: chi va in CPU?

> [!abstract] Nodo
> Lo scheduler decide quale processo nella coda **Ready** prende la CPU. L'obiettivo è massimizzare l'utilizzo della CPU eliminando i momenti in cui è idle.

**CPU burst vs I/O burst:** i processi alternano burst di CPU intenso con attese di I/O. La maggior parte dei processi ha burst di CPU **brevi** (distribuzione iperbolica).

> [!quote] Criteri di valutazione (da massimizzare o minimizzare)
> - **Throughput** ↑ = più job finiti per unità di tempo
> - **Turnaround Time** ↓ = fine - arrivo
> - **Waiting Time** ↓ = tempo in coda Ready
> - **Response Time** ↓ = tempo alla prima risposta (critico per sistemi interattivi)

**Scheduling con o senza prelazione:**
- **Non-preemptive**: il processo gira fino a terminazione o blocco volontario
- **Preemptive**: il kernel può interromperlo forzatamente (timeout, priorità più alta)

---

## L6/L7 — Algoritmi Classici

### FCFS — First Come First Served

> [!abstract] Logica
> Coda FIFO. Chi arriva prima, serve prima. Non-preemptive.

> [!danger] Effetto Convoglio
> Un processo lungo (es. burst 24ms) blocca N processi brevi (3ms) in coda. Il waiting time medio esplode.
> Con P1=24, P2=3, P3=3: media attesa = **17ms**. Con ordine inverso → **3ms**. FCFS non considera la lunghezza.

### SJF — Shortest Job First

> [!abstract] Logica
> Serve il processo con il burst più breve. **Ottimale** per minimizzare il waiting time medio. Non-preemptive.

> [!quote] Stima del burst: Media Esponenziale
> $$\tau_{n+1} = \alpha \cdot t_n + (1-\alpha) \cdot \tau_n$$
> - $t_n$ = burst reale osservato
> - $\tau_n$ = stima precedente
> - $\alpha$ = peso del recente (tipicamente 0.5)
> I burst lontani nel tempo **sfumano esponenzialmente** → si "dimenticano" da soli.

> [!danger] SJF è teorico
> Non si può sapere a priori quanto durerà il prossimo burst. In pratica lo si stima, ma non è implementabile in modo puro.

### SRTF — Shortest Remaining Time First

> [!abstract] Logica
> Versione **preemptive** di SJF. Ogni volta che arriva un nuovo processo, il kernel confronta il suo burst con il **tempo rimanente** del processo in esecuzione. Se il nuovo è più corto → prelazione.

> [!quote] Formula del waiting time
> $\text{attesa}_i = \text{fine}_i - \text{arrivo}_i - \text{burst}_i$

### Round-Robin (RR)

> [!abstract] Logica
> Ogni processo riceve un **quanto di tempo** (quantum, tipicamente 10-100ms). Se non finisce → torna in fondo alla coda. Equo, nessuna starvation.

> [!quote] Taratura del quanto
> - Quanto **troppo grande** → degenera in FCFS
> - Quanto **troppo piccolo** → overhead di context switch enorme
> - Regola empirica: 80% dei CPU burst < quanto → buona calibrazione

### Priorità + Aging

> [!abstract] Logica
> Ogni processo ha una priorità numerica. Chi ha priorità più alta prende la CPU. Rischio: **starvation** per le priorità basse.

> [!quote] Soluzione: Aging
> La priorità di un processo aumenta col tempo di attesa. Dopo abbastanza tempo, anche il processo "scarso" diventa prioritario e viene servito.

### MLFQ — Multi-Level Feedback Queue

> [!abstract] Logica
> Code multiple (es. Q0, Q1, Q2) con algoritmi diversi. I processi si muovono tra le code in base al comportamento:
> - Usa tutto il quanto → declassamento (CPU-bound affonda nelle code basse)
> - Aspetta troppo → promozione (aging)

> [!example] Schema tipico a 3 livelli
> - Q0: RR quantum=8ms (processi nuovi entrano qui)
> - Q1: RR quantum=16ms
> - Q2: FCFS (processi CPU-bound lunghi finiscono qui)
> Un processo I/O-bound finisce spesso nel suo quanto → rimane in Q0 → risposta rapida.

---

## L8 — Scheduling Real-Time

> [!abstract] Nodo
> I sistemi real-time hanno processi con **scadenze (deadline)**. L'obiettivo non è massimizzare il throughput, ma **rispettare le deadline**.

> [!quote] Soft vs Hard Real-Time
> - **Soft**: il SO dà massima priorità, ma senza garanzie formali (Linux standard)
> - **Hard**: le deadline sono garantite matematicamente (serve RTOS: VxWorks, RT-Linux)

**Task periodici:** ogni task ha periodo $T$, burst $t$, deadline $d \leq T$. Utilizzo CPU: $u_i = t_i/T_i$.

### Rate Monotonic Scheduling (RMS)

> [!quote] Regola e limite
> - Priorità **statica**: più alta frequenza ($1/T$) → più alta priorità
> - Garantisce deadline se: $\sum \frac{t_i}{T_i} \leq n(2^{1/n}-1)$
> - Per $n \to \infty$: limite = $\ln 2 \approx$ **69%** di utilizzo CPU

> [!danger] Limite di RMS
> Con utilizzo > 69% (per n∞), RMS buca alcune deadline. Usa solo la frequenza, ignora le deadline reali.

### Earliest Deadline First (EDF)

> [!quote] Regola e proprietà
> - Priorità **dinamica**: la deadline più vicina → priorità più alta
> - **Ottimale**: se esiste uno scheduling fattibile, EDF lo trova
> - Garantisce deadline finché utilizzo totale ≤ 100%

> [!example] RMS vs EDF: quando RMS fallisce
> P1(T=50,t=25) + P2(T=80,t=35) → utilizzo = 50%+43.75% = 93.75% < 100%.
> EDF: rispetta tutte le deadline. RMS: P2 buca la deadline perché ha solo priorità statica sulla frequenza.

---

## L8 — Linux Scheduling: CFS e EEVDF

### CFS — Completely Fair Scheduler (Linux 2.6.23)

> [!abstract] Nodo
> CFS mira alla **fairness**: ogni processo riceve $1/n$ del tempo CPU. Lo realizza con un "orologio truccato" (virtual runtime).

> [!quote] Meccanismo Virtual Runtime
> - Ogni processo accumula **virtual runtime** ($v_r$) man mano che usa CPU
> - Alta priorità (nice basso) → orologio scorre **lento** → $v_r$ cresce poco → viene scelto spesso
> - Bassa priorità → orologio scorre **veloce** → viene scelto meno
> - Lo scheduler sceglie sempre il processo con **$v_r$ minore** (ha "avuto meno soddisfazione")
> - Struttura dati: **albero Rosso-Nero** → il processo con $v_r$ minore è sempre il nodo più a sinistra → accesso O(1)

### EEVDF — Earliest Eligible Virtual Deadline First (Linux 6.6+)

> [!abstract] Nodo
> Aggiunge la dimensione **futuro** (deadline virtuale) e **equità attiva** (eligibilità/lag).

> [!quote] Due criteri combinati
> - **Eligibilità**: un processo è eligibile se non ha consumato *troppo* più di quanto spettava (lag non troppo negativo). Chi ha "rubato" CPU va in quarantena.
> - **Virtual Deadline**: tra gli eligibili, vince chi ha la deadline virtuale più ravvicinata → più reattività
> - Risultato: meglio di CFS per i processi interattivi.

---

## L9 — Scheduling Multicore

> [!abstract] Nodo
> Con più core, lo scheduler deve decidere **chi** va in CPU **e su quale core**.

> [!quote] Architetture di coda
> - **Coda comune**: tutti i core pescano dalla stessa Ready Queue. Semplice, ma contention sulla struttura dati.
> - **Code private per core** (comune): ogni core ha la sua coda. Migliore cache affinity, ma serve bilanciamento.

**Load Balancing:**
- **Push**: un processo monitora il carico e spinge task ai core scarichi
- **Pull**: un core idle va a "rubare" task dalla coda di un core occupato

**CPU Affinity:**
- **Soft**: preferenza a restare sullo stesso core (cache calda), ma migrazione permessa
- **Hard**: il thread è fissato a un sottoinsieme di core (`taskset` su Linux)

> [!example] Metafora: core idle che ruba task = cassiere senza clienti che prende dalla fila del collega
> Il core idle non aspetta: va attivamente a prendere lavoro dagli altri core sovraccarichi.

**NUMA (Non-Uniform Memory Access):** su sistemi multi-socket, ogni socket ha RAM "più vicina". Migrare un thread tra socket = cache invalida + dati lontani → costo alto.

---

# 🔒 PILASTRO 4 — SINCRONIZZAZIONE E CONCORRENZA
*Lezioni 10 → 13*

---

## L10 — Il Problema: Race Condition

> [!abstract] Nodo
> Quando due thread accedono alla stessa variabile condivisa e almeno uno scrive, il risultato dipende dall'ordine di esecuzione → **non deterministico**. Si chiama Race Condition.

> [!example] Metafora: due persone che modificano lo stesso documento senza Google Docs
> Thread1 legge "counter=5", Thread2 legge "counter=5", entrambi aggiungono 1, entrambi scrivono "6". Il risultato è 6 invece di 7. Un aggiornamento è perso.

> [!quote] Perché counter++ non è atomica
> A livello macchina è 3 istruzioni: `LOAD r, counter` → `ADD r, 1` → `STORE counter, r`. Lo scheduler può interrompere tra una e l'altra.

---

## L10 — Sezione Critica: le 3 proprietà

> [!abstract] Nodo
> Una **sezione critica** è il blocco di codice che accede a dati condivisi. Un meccanismo di protezione è corretto se e solo se garantisce tutte e 3 queste proprietà:

> [!quote] Le 3 proprietà (da sapere a memoria)
> 1. **Mutua Esclusione**: al più 1 processo alla volta dentro la sezione critica
> 2. **Progresso**: se nessuno è dentro e qualcuno vuole entrare, la scelta avviene in tempo finito (non aspettano all'infinito)
> 3. **Bounded Waiting**: esiste un limite al numero di volte in cui altri processi entrano prima di te (no starvation)

> [!danger] Mutua Esclusione da sola NON basta
> Puoi avere mutua esclusione e violare progresso (tutti si bloccano senza che nessuno entri). Servono tutte e 3.

---

## L10 — Soluzione di Peterson (teorica)

> [!abstract] Nodo
> Soluzione software per 2 processi. Usa 2 variabili condivise: `flag[2]` (voglio entrare) e `turn` (a chi tocca). Soddisfa tutte e 3 le proprietà.

> [!quote] Codice per processo i (j = 1-i)
> ```c
> flag[i] = true;   // dichiaro di voler entrare
> turn = j;         // cedo gentilmente il turno all'altro
> while (flag[j] && turn == j);  // aspetto se l'altro vuole E ha il turno
> // --- SEZIONE CRITICA ---
> flag[i] = false;  // esco, non voglio più entrare
> ```

> [!example] La logica della "gentilezza"
> Ogni processo dice: "voglio entrare, ma ti do la precedenza." L'ultimo a cedere il turno è quello che aspetta. Se entrambi cedono quasi contemporaneamente, vince chi ha ceduto per primo (turn = j dell'ultimo assegnamento).

> [!danger] Peterson non funziona su hardware moderno
> Il compilatore può **riordinare** le istruzioni (`flag[i]=true` e `turn=j` potrebbero invertirsi). Servono **memory barriers** per forzare l'ordine.

---

## L10 — Supporto Hardware: Test-and-Set e CAS

> [!abstract] Nodo
> Il kernel usa istruzioni hardware **atomiche** (indivisibili): eseguono due operazioni come se fossero una sola, senza possibilità di interruzione.

### Test-and-Set

> [!quote] Pseudo-codice atomico
> ```c
> bool test_and_set(bool *target) {
>     bool rv = *target;
>     *target = true;   // setta sempre a true
>     return rv;        // ritorna il vecchio valore
> }
> // Uso:
> while (test_and_set(&lock));  // aspetta finché lock era false
> // SEZIONE CRITICA
> lock = false;
> ```

> [!danger] TAS garantisce mutua esclusione ma NON bounded waiting
> Chi vince il TAS è casuale. Un processo può aspettare per sempre se altri continuano a "rubargli" il lock.

### Compare-and-Swap (CAS)

> [!quote] Pseudo-codice atomico
> ```c
> int compare_and_swap(int *value, int expected, int new_val) {
>     int rv = *value;
>     if (*value == expected) *value = new_val;
>     return rv;  // ritorna il vecchio valore
> }
> ```

> [!abstract] Uso lock-free: incremento atomico
> ```c
> void increment(int *v) {
>     int temp;
>     do { temp = *v; }
>     while (compare_and_swap(v, temp, temp+1) != temp);
> }
> ```
> "Tenta l'aggiornamento. Se nel frattempo qualcun altro ha cambiato v, riprova." Nessun lock, ma con alta contesa = starvation possibile.

---

## L11 — Spin Lock vs Mutex Lock

> [!quote] Tabella comparativa
> | | Spin Lock | Mutex Lock |
> |---|---|---|
> | Processo in attesa | Rimane in Running (busy wait) | Viene sospeso (sleeping) |
> | Context switch | Nessuno | Uno per sospendere, uno per svegliare |
> | Usa se... | Attesa **breve**, multicore | Attesa **lunga**, qualsiasi sistema |
> | Analogia | Macchina ferma col motore acceso | Macchina spenta che si riavvia |

> [!danger] Spin lock su single-core = deadlock di fatto
> Il processo che aspetta occupa il 100% della CPU → il processo che tiene il lock non può mai girare per liberarlo.

---

## L11 — Semafori

> [!abstract] Nodo
> Il semaforo è una variabile intera $S$ con due operazioni **atomiche**. Permette sincronizzazione più ricca del semplice mutex.

> [!quote] Operazioni wait(P) e signal(V)
> - `wait(S)`: $S \leftarrow S-1$. Se $S < 0$ → il processo si blocca in coda
> - `signal(S)`: $S \leftarrow S+1$. Se $S \leq 0$ → sveglia un processo dalla coda

**Semaforo Binario** (inizializzato a 1): equivale a un mutex.
**Semaforo Contatore** (inizializzato a N): permette N accessi contemporanei.

> [!example] Produttore-Consumatore con 3 semafori
> ```c
> semaphore mutex = 1;   // accesso esclusivo al buffer
> semaphore empty = N;   // slot vuoti (inizia con N)
> semaphore full  = 0;   // slot pieni (inizia con 0)
>
> // PRODUTTORE:
> wait(empty); wait(mutex);
> // metti item nel buffer
> signal(mutex); signal(full);
>
> // CONSUMATORE:
> wait(full); wait(mutex);
> // prendi item dal buffer
> signal(mutex); signal(empty);
> ```
> `empty` e `full` si complementano perfettamente.

> [!danger] Ordine dei wait conta!
> Invertire `wait(mutex)` e `wait(empty)` nel produttore → deadlock: il produttore tiene mutex, aspetta empty; il consumatore aspetta mutex → ciclo.

---

## L12 — Monitor e Variabili di Condizione

> [!abstract] Nodo
> Il monitor è un ADT (tipo di dato astratto) che **incapsula** dati condivisi + operazioni che li accedono, garantendo mutua esclusione **automaticamente**. Il programmatore non dichiara lock esplicitamente.

> [!quote] API POSIX per condition variables
> ```c
> pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
> pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
>
> // Aspettare una condizione:
> pthread_mutex_lock(&m);
> while (!condizione) pthread_cond_wait(&cond, &m);
> // ... sezione critica ...
> pthread_mutex_unlock(&m);
>
> // Segnalare:
> pthread_cond_signal(&cond);    // sveglia 1 thread
> pthread_cond_broadcast(&cond); // sveglia tutti i thread
> ```

> [!danger] SEMPRE while, mai if
> `pthread_cond_wait` può svegliarsi **spuriamente** (senza che nessuno abbia fatto signal). Con `if` entreresti nella sezione critica senza che la condizione sia vera. Con `while` ri-controlli sempre.

---

## L12 — I 5 Filosofi: deadlock classico

> [!abstract] Nodo
> 5 filosofi, 5 bacchette, 1 tra ogni coppia. Per mangiare servono 2 bacchette (sinistra + destra). Problema: tutti prendono la sinistra → nessuno ha la destra → deadlock circolare.

> [!quote] Soluzione corretta con condition variable per filosofo
> ```c
> // Ogni filosofo ha: stato (THINKING/HUNGRY/EATING) + sua cond var
> void take_forks(int i) {
>     lock(); state[i] = HUNGRY; test(i);
>     while (state[i] != EATING) cond_wait(&cond[i], &mutex);
>     unlock();
> }
> void put_forks(int i) {
>     lock(); state[i] = THINKING;
>     test((i-1)%5); test((i+1)%5); // controlla i vicini
>     unlock();
> }
> void test(int i) { // mangio solo se entrambi i vicini non mangiano
>     if (state[i]==HUNGRY && state[(i-1)%5]!=EATING && state[(i+1)%5]!=EATING)
>         { state[i]=EATING; cond_signal(&cond[i]); }
> }
> ```

> [!example] signal vs broadcast
> - Con 1 cond var per filosofo → `signal`: sveglio esattamente il filosofo giusto
> - Con 1 cond var globale → `broadcast`: sveglio tutti, ognuno ri-controlla la sua condizione

---

## L12 — Deadlock: condizioni di Coffman

> [!abstract] Nodo
> Il deadlock richiede tutte e 4 queste condizioni **simultaneamente**. Basta eliminarne una per prevenirlo.

> [!quote] Le 4 condizioni di Coffman (1971)
> 1. **Mutua Esclusione**: la risorsa è esclusiva (un processo alla volta)
> 2. **Hold and Wait**: un processo tiene una risorsa mentre aspetta un'altra
> 3. **No Preemption**: non si può strappare una risorsa a forza
> 4. **Circular Wait**: P1 aspetta P2, P2 aspetta P3, … Pn aspetta P1

> [!quote] Prevenzione pratica: ordinamento totale dei lock
> Se tutti i processi acquisiscono i lock **sempre nello stesso ordine** (es. sempre mutex1 prima di mutex2), il circular wait è impossibile per costruzione.

---

## L11 — Priority Inversion (caso Pathfinder 1997)

> [!abstract] Nodo
> Problema subdolo: un processo ad **alta priorità** H viene bloccato indirettamente da uno a **media priorità** M, attraverso un lock tenuto da uno a **bassa priorità** L.

> [!quote] Scenario
> 1. L entra in sezione critica (prende lock)
> 2. H arriva, vuole il lock → si blocca
> 3. M arriva, prelaziona L (M ha priorità > L)
> 4. M gira quanto vuole. L non gira. Il lock resta a L. H aspetta M.
> → H è bloccato da M, anche se H > M. Inversione di priorità.

> [!quote] Soluzione: Priority Inheritance
> Quando H si blocca aspettando un lock di L → L eredita **temporaneamente** la priorità di H. M non può più prelazionare L. L finisce in fretta, libera il lock, H riparte.
> Su Pathfinder: bastò abilitare un flag nel RTOS via radio da Terra.

---

# 🧩 PILASTRO 5 — GESTIONE DELLA MEMORIA
*Lezioni 14 → 19*

---

## L14 — Indirizzo Logico vs Fisico

> [!abstract] Nodo
> Un processo non vede mai gli indirizzi fisici della RAM. Vede solo indirizzi **logici (virtuali)** che partono da 0. La traduzione è trasparente e avviene in hardware.

> [!quote] I 3 momenti del Binding
> - **Compile time**: indirizzo fisso nel codice (obsoleto, rigido)
> - **Load time**: il loader aggiunge un offset base all'avvio (flessibile ma non rilocabile a runtime)
> - **Runtime** (moderno): la traduzione avviene a ogni accesso tramite MMU → il processo può essere spostato in RAM

**MMU (Memory Management Unit)**: chip hardware (integrato nella CPU moderna) che intercetta ogni indirizzo logico generato dalla CPU e lo traduce in fisico.

---

## L14 — Frammentazione e Paging

> [!abstract] Nodo
> Il paging risolve la frammentazione esterna dell'allocazione contigua dividendo la memoria in blocchi fissi uguali.

**Frammentazione esterna**: spazio libero frammentato in tanti piccoli buchi inutilizzabili.
**Soluzione — Paging:**
- Memoria fisica: divisa in **Frame** (blocchi fissi, es. 4KB)
- Memoria logica del processo: divisa in **Pagine** (stessa dimensione dei frame)
- Una pagina logica può finire in qualsiasi frame fisico libero → niente frammentazione esterna

> [!quote] Traduzione dell'indirizzo logico
> Indirizzo logico = `(p, d)` dove p = numero pagina, d = offset
> La **Page Table** mappa `p → f` (numero frame).
> Indirizzo fisico = `(f, d)` = `f * DimFrame + d`

> [!example] Calcolo veloce dei bit
> Spazio logico $2^m$ byte, pagine da $2^n$ byte:
> - Bit per l'offset: $n$
> - Bit per il numero di pagina: $m - n$
> - Numero di pagine: $2^{m-n}$

> [!danger] Frammentazione interna (residua)
> L'ultima pagina di un file/processo raramente è piena → spreco medio = metà pagina per processo. Con pagine da 4KB = al max 2KB sprecati.

---

## L15 — TLB: cache delle traduzioni

> [!abstract] Nodo
> Senza TLB: ogni accesso logico → 2 accessi fisici (1 per leggere la page table, 1 per il dato). Lentissimo. La TLB è una cache hardware che memorizza le traduzioni più recenti.

> [!quote] Meccanismo TLB Hit/Miss
> - **Hit**: la traduzione è in TLB → 1 solo accesso (alla velocità della cache)
> - **Miss**: la TLB non ha la traduzione → leggi la page table in RAM (accesso lento) → aggiorna TLB → poi accedi al dato
> Hit rate moderno: >99%

> [!quote] EAT — Effective Access Time
> $$EAT = \alpha(\epsilon + T_M) + (1-\alpha)(\epsilon + 2T_M)$$
> - $\alpha$ = hit rate TLB
> - $\epsilon$ = tempo accesso TLB
> - $T_M$ = tempo accesso RAM
> Esempio: $\alpha=0.99$, $\epsilon=20ns$, $T_M=100ns$ → EAT ≈ 121ns (vs 200ns senza TLB)

**ASID (Address Space Identifiers):** estensione delle TLB moderne. Ogni entry include il PID → non serve svuotare la TLB a ogni context switch.

---

## L15 — Strutture delle Page Table per spazi grandi

> [!abstract] Nodo
> Con 64-bit, una page table lineare sarebbe enorme (terabyte). Si usano strutture più efficienti.

> [!quote] 3 approcci
> 1. **Gerarchica (Multi-Level)**: l'indirizzo logico è suddiviso in più indici di tabella. Linux x86-64 usa 4 livelli (PML4 → PDPT → PD → PT → offset). Si alloca solo la parte usata.
> 2. **Hashed**: funzione hash sul numero di pagina → tabella hash di dimensione fissa. Usata per spazi sparsi enormi.
> 3. **Inverted Page Table**: 1 entry per ogni frame fisico (non per ogni pagina logica). Dimensione dipende dalla RAM, non dallo spazio virtuale. Contro: ricerca lenta (hash aiuta), condivisione difficile.

---

## L16 — Memoria Virtuale e Demand Paging

> [!abstract] Nodo
> La memoria virtuale disaccoppia lo spazio di indirizzamento del processo dalla RAM disponibile. Un processo può essere più grande della RAM → alcune pagine sono su disco.

> [!quote] Demand Paging: carica solo quello che serve
> - All'avvio: tutte le pagine marcate **Invalid** nella page table
> - Al primo accesso: **Page Fault** → il SO carica la pagina dal disco al RAM → aggiorna la page table → riavvia l'istruzione

> [!quote] Flusso del Page Fault (7 passi)
> 1. MMU vede bit Invalid → genera Trap
> 2. SO salva il contesto del processo
> 3. SO controlla se l'accesso è legale (via PCB)
> 4. SO trova un frame libero
> 5. SO legge la pagina dal disco (operazione I/O lenta)
> 6. SO aggiorna la page table (Valid, numero frame)
> 7. SO riavvia l'istruzione interrotta

> [!quote] EAT con Page Fault
> $$EAT = (1-p) \cdot T_{RAM} + p \cdot T_{fault}$$
> Con $T_{RAM}=200ns$ e $T_{fault}=8ms$: per degradazione < 10% serve $p < 1/400000$.

**Copy-on-Write (COW):** dopo `fork()`, le pagine sono condivise in sola lettura. Solo alla prima scrittura una pagina viene duplicata. → `exec()` dopo `fork()` non copia quasi nulla.

---

## L17 — Algoritmi di Sostituzione Pagina

> [!abstract] Nodo
> Quando la RAM è piena e serve un frame, il SO sceglie una **pagina vittima** da espellere. Se il **Dirty Bit** è 1 (modificata), va scritta su disco (costoso). Se è 0 (clean), si sovrascrive (la copia su disco è ancora valida).

### FIFO

> [!quote] Logica e problema
> Sostituisce la pagina più vecchia. Semplice. Soffre dell'**Anomalia di Belady**: più frame → più page fault (possibile per FIFO).

### OPT (Ottimale)

> [!quote] Logica
> Sostituisce la pagina che non sarà usata per più tempo in futuro. **Impossibile** da implementare (richiede preveggenza). Serve come **benchmark**.

### LRU — Least Recently Used

> [!quote] Logica e proprietà
> Sostituisce la pagina non usata da più tempo nel **passato**. Non soffre anomalia di Belady (è uno Stack Algorithm). Il problema: implementazione costosa.
> - Timestamp: ogni accesso aggiorna un campo → hardware dedicato
> - Lista doppiamente collegata: ad ogni accesso si sposta la pagina in testa → O(1) ma costante alta

### Clock (Second Chance) — approssimazione LRU

> [!abstract] Nodo
> La TLB/MMU setta il **Reference Bit** a 1 ad ogni accesso. L'algoritmo usa una lancetta circolare.

> [!quote] Funzionamento
> - Lancetta punta a una pagina: controlla il Reference Bit
> - **R=1**: dai seconda chance → azzera R, avanza la lancetta
> - **R=0**: questa è la vittima → sostituiscila

**Enhanced Clock (con Dirty Bit):** 4 classi di priorità:
1. R=0, M=0 → vittima ideale (non usata, non sporca)
2. R=0, M=1 → non usata ma sporca (richiede I/O)
3. R=1, M=0 → usata ma clean
4. R=1, M=1 → ultima scelta (usata e sporca)

---

## L18 — Thrashing

> [!abstract] Nodo
> Il thrashing è il collasso del sistema: i processi generano così tanti page fault che il SO passa più tempo a fare I/O su disco che a eseguire codice utile.

> [!example] Metafora: un ristorante che cucina velocissimamente ma aspetta sempre il forno
> Troppi cuochi (processi), un solo forno (RAM). Tutti aspettano di cuocere. Nessuno serve clienti. Il ristorante collassa.

> [!quote] Causa e sintomi
> - **Causa**: somma dei Working Set dei processi > RAM fisica disponibile
> - **Sintomi**: CPU idle (tutti i processi in Waiting I/O), coda disco lunghissima, page fault rate altissimo
> - **Soluzione**: ridurre la multiprogrammazione (sospendere processi)

**Working Set $W(t, \Delta)$**: l'insieme delle pagine distinte a cui un processo ha fatto accesso negli ultimi $\Delta$ istanti. Se $\sum |W_i| >$ RAM → pericolo thrashing.

---

## L18 — Allocazione Memoria Kernel: Buddy + Slab

### Buddy System

> [!abstract] Nodo
> Gestisce la memoria fisica in blocchi di dimensione **potenza di 2**. Serve per allocare pagine contigue richieste da operazioni hardware (DMA) o grandi strutture kernel.

> [!quote] Allocazione e merge
> - Richiesta K byte → trova il blocco libero più piccolo $\geq$ K (potenza di 2)
> - Se troppo grande → lo divide in 2 "buddy" uguali → ripete
> - Liberazione → controlla se il buddy è libero → fonde i due in un blocco doppio

### Slab Allocator

> [!abstract] Nodo
> Gestisce oggetti specifici del kernel (PCB, inode, socket…) eliminando l'overhead di inizializzazione e la frammentazione.

> [!quote] Struttura a 3 livelli
> - **Cache**: contiene oggetti dello stesso tipo (es. cache degli inode)
> - **Slab**: gruppo di pagine fisicamente contigue (dal Buddy) → contiene N istanze dell'oggetto
> - **Oggetto**: istanza pre-inizializzata, pronta all'uso

> [!example] Vantaggio pratico
> Creare un nuovo PCB = prendere un oggetto già inizializzato dallo slab (O(1)) invece di allocare e azzerare memoria da zero ogni volta.

---

## L19 — LRU nei SO reali: approssimazioni pratiche

> [!abstract] Nodo
> LRU puro è troppo costoso. Ogni SO lo approssima con varianti basate sul Reference Bit.

### Linux — Active/Inactive Lists

> [!quote] Meccanismo
> - **Active List**: pagine con Reference Bit = 1 (usate di recente)
> - **Inactive List**: pagine con Reference Bit = 0 (candidate all'espulsione)
> - `kswapd` (demone kernel): controlla la memoria libera; se scende sotto soglia → scandisce Inactive List e libera pagine (le sporca → swap; le clean → sovrascrive)
> - Una pagina nella Inactive List può essere "resuscitata" se vi si accede prima di essere sovrascritta

### Windows — Working Set Trimmer

> [!quote] Meccanismo
> - Ogni processo ha un Working Set Min e Max (limiti euristici)
> - Se RAM scende sotto soglia → il Trimmer rimuove pagine dai processi che eccedono il loro minimo
> - Prima vengono sacrificati i processi **grandi e inattivi**

### Solaris — Two-Hand Clock

> [!quote] Meccanismo
> - **Front Hand (Scout)**: scorre veloce, azzera il Reference Bit (rende le pagine vulnerabili)
> - **Back Hand (Reaper)**: segue a distanza (Hand Spread); se trova R=0 → vittima
> - Sotto pressione: velocità di scansione aumenta, Hand Spread si riduce → meno seconda chance data

---

# 💾 PILASTRO 6 — STORAGE, FILE SYSTEM E I/O
*Lezioni 19 → 25*

---

## L19 — HDD vs SSD

> [!abstract] Nodo
> Il SO vede entrambi come array lineare di blocchi logici (LBA). La differenza fisica è enorme.

> [!quote] HDD — Anatomia e tempi
> - **Struttura**: piatti magnetici, tracce, settori, cilindri
> - **Tempo di accesso** = Seek Time (testina si sposta) + Rotational Latency (aspetta il settore) + Transfer Time
> - Seek Time è il dominante: 3–12ms
> - 7200 RPM → latenza rotazionale media ≈ **4.17ms**
> - ZBR: tracce esterne hanno più settori → maggiore velocità di trasferimento

> [!quote] SSD — Caratteristiche chiave
> - Nessun Seek Time (accesso random quasi istantaneo)
> - NAND Flash: si **cancella a blocchi** (lento), si **scrive a pagine** (veloce)
> - Numero limitato di cicli P/E → usura
> - **FTL (Flash Translation Layer)**: gestisce Wear Leveling (distribuisce le scritture), Garbage Collection (compatta dati validi, libera blocchi invalidi), Bad Block Management

> [!danger] Disk Scheduling sugli SSD è inutile
> Per HDD ha senso ridurre il movimento della testina. Per SSD l'ordine fisico non conta → si usa NOOP (FIFO semplice) o deadline.

---

## L19 — Disk Scheduling (per HDD)

> [!abstract] Nodo
> Minimizza il movimento totale della testina (Seek Time) ottimizzando l'ordine di servizio delle richieste in coda.

> [!quote] Confronto algoritmi
> | Algoritmo | Logica | Problema |
> |---|---|---|
> | **FCFS** | Ordine d'arrivo | Movimento erratico, seek time alto |
> | **SSTF** | Più vicina alla testina | Starvation per le richieste lontane |
> | **SCAN** (Ascensore) | Va da un estremo all'altro, poi inverte | Attesa doppia per le richieste agli estremi |
> | **C-SCAN** | Solo in una direzione, poi torna veloce all'inizio | Più equo di SCAN |
> | **LOOK** | Come SCAN ma si ferma all'ultima richiesta | Evita movimenti inutili verso estremi vuoti |
> | **C-LOOK** | Come C-SCAN ma con l'ottimizzazione LOOK | Ottimale nella pratica |

> [!example] Metafora SCAN = ascensore
> L'ascensore non torna indietro per ogni piano richiesto: va su fino all'ultimo piano richiesto, poi scende raccogliendo chi aspetta nel verso contrario.

---

## L20 — Bootstrap: BIOS+MBR vs UEFI+GPT

> [!abstract] Nodo
> Il bootstrap è la sequenza di eventi che porta il kernel in RAM da zero. Due standard: legacy (BIOS) e moderno (UEFI).

### BIOS + MBR (Legacy)

> [!quote] Flusso
> 1. BIOS esegue POST (Power-On Self Test)
> 2. Legge **MBR** (Master Boot Record) = primi 512 byte del disco:
>    - 446 byte: Boot Code
>    - 64 byte: Partition Table (max 4 partizioni primarie)
>    - 2 byte: Firma magica `0x55AA`
> 3. Boot Code carica il Bootloader di 2° livello (GRUB stage2)
> 4. GRUB carica il kernel in RAM

> [!danger] Limiti BIOS+MBR
> - Max disco: ~2.2TB (indirizzamento 32-bit)
> - Max 4 partizioni primarie

### UEFI + GPT (Moderno)

> [!quote] Flusso
> 1. UEFI fa POST + legge **GPT** (GUID Partition Table, 64-bit → dischi enormi, >128 partizioni)
> 2. UEFI trova l'**ESP** (EFI System Partition) → partizione FAT32 speciale
> 3. Carica il Boot Manager dall'ESP (es. `grubx64.efi`, `bootx64.efi`)
> 4. Boot Manager presenta menu, carica kernel specifico

> [!example] Dual Boot
> Ogni SO installa il suo bootloader nell'ESP. Il Boot Manager sceglie quale caricare. Windows Update può resettare il boot order → Linux sparisce dal menu. Fix: `efibootmgr`.

---

## L20 — Swap Space

> [!abstract] Nodo
> Lo swap è l'area su disco che estende la memoria virtuale oltre la RAM fisica (Backing Store per le pagine espulse).

> [!quote] Raw Partition vs Swap File
> - **Raw Partition** (es. `/dev/sda3` come swap): accesso diretto, più veloce, nessun overhead FS
> - **Swap File** (`/swapfile` in Linux, `pagefile.sys` in Windows): più flessibile (ridimensionabile), overhead trascurabile su SSD

> [!quote] Cosa finisce nello swap
> - **Memoria anonima**: stack, heap, dati modificabili → va sullo swap
> - **Codice (Text segment)**: NON va sullo swap → viene ricaricato direttamente dall'eseguibile su disco (è già lì, read-only)

> [!danger] SSD e swap
> Le scritture continue sullo swap consumano il ciclo P/E degli SSD. iOS/Android preferiscono **compressione in RAM** (zswap) invece di swap su flash.

---

## L20 — RAID: Affidabilità e Performance

> [!abstract] Nodo
> RAID combina più dischi fisici in uno logico per ottenere affidabilità (ridondanza) o performance (striping) o entrambe.

> [!quote] Concetti chiave
> - **Striping**: dati divisi a blocchi su più dischi → parallelismo I/O → velocità
> - **Mirroring**: stessa copia su 2+ dischi → ridondanza → sicurezza
> - **Parità**: bit XOR extra permette di ricostruire un disco guasto → compromesso

> [!quote] Livelli RAID principali
> | RAID | Tecnica | Tollera guasti | Capacità utile | Uso tipico |
> |---|---|---|---|---|
> | **0** | Striping puro | **0** | 100% | Performance pura (video editing) |
> | **1** | Mirroring | 1 | 50% | SO, dati critici |
> | **5** | Stripe + parità distribuita | 1 | N-1 | Server generici |
> | **6** | Stripe + doppia parità | **2** | N-2 | Ambienti ad alta criticità |
> | **10 (1+0)** | Mirror poi Stripe | 1 per specchio | 50% | Database ad alte prestazioni |

> [!example] Metafora RAID 5 = libretto di risparmio + fotocopia
> Ogni blocco ha una "fotocopia" (parità) distribuita sugli altri dischi. Se un disco muore, la fotocopia ricostruisce i dati mancanti. Ma durante la ricostruzione sei vulnerabile → RAID 6 (doppia fotocopia) è più sicuro.

> [!danger] RAID 0: zero tolleranza
> Con N dischi in RAID 0, la probabilità che almeno uno si rompa è N volte quella del singolo disco. RAID 0 **amplifica** il rischio di perdita dati.

---

## L21/L22 — Struttura del File System: le 3 tabelle

> [!abstract] Nodo
> Quando apri un file, il kernel crea una catena di 3 strutture dati in RAM per tracciare ogni accesso. Capire queste 3 tabelle risolve il 90% dei dubbi sul comportamento dei file.

> [!quote] Le 3 tabelle (da più vicina al processo a più vicina al disco)
> 1. **Per-Process File Descriptor Table** (nel PCB): array indicizzato dai FD (0=stdin, 1=stdout, 2=stderr, 3…n). Ogni entry punta alla tabella globale.
> 2. **System-wide Open File Table** (kernel): 1 entry per ogni `open()` attiva. Contiene: flag di accesso (r/w/append), **offset corrente** (File Pointer), puntatore all'inode.
> 3. **In-Memory Inode Table**: copie degli inode caricati dal disco. Contiene i metadati reali (dimensione, permessi, blocchi disco).

> [!example] Perché l'offset si sposta dopo fork()
> `open()` prima di `fork()` → padre e figlio **condividono la stessa entry** nella Open File Table → condividono lo stesso offset. Se il figlio scrive, l'offset avanza anche per il padre. Per leggere dall'inizio, il padre deve fare `lseek(fd, 0, SEEK_SET)`.
>
> `open()` separati dopo `fork()` → entry indipendenti → offset indipendenti.

---

## L21 — Inode: il cuore del file

> [!abstract] Nodo
> L'**Inode** (Index Node) è la struttura dati che rappresenta un file nel filesystem. Contiene tutto **tranne il nome**.

> [!quote] Contenuto dell'Inode
> - Inode Number (identificatore univoco nel FS)
> - Tipo (file regolare, directory, link, dispositivo…)
> - Dimensione in byte
> - UID/GID (proprietario)
> - Permessi rwx per owner/group/others
> - Timestamps (creazione, modifica dati, modifica metadati)
> - **Puntatori ai blocchi dati** (la parte cruciale)
> - Contatore hard link

> [!danger] Il nome NON è nell'inode
> Il nome del file sta nella **directory** che mappa `nome → numero inode`. Un inode può avere più nomi (hard link).

### Struttura dei puntatori (Unix/ext4)

> [!quote] Puntatori ibridi per coprire file piccoli e grandi
> - **12 Direct Pointers**: puntano direttamente ai blocchi dati → velocissimi per file piccoli
> - **1 Single Indirect**: punta a un blocco pieno di puntatori → 2 accessi disco
> - **1 Double Indirect**: blocco → blocco di puntatori → dato → 3 accessi
> - **1 Triple Indirect**: 4 accessi → file enormi

> [!example] Calcolo dimensione massima
> Con blocchi da 4KB e puntatori da 8 byte: 512 puntatori per blocco indiretto.
> - Direct: 12 × 4KB = 48KB
> - Single indirect: 512 × 4KB = 2MB
> - Double: 512² × 4KB = 1GB
> - Triple: 512³ × 4KB = 512GB

---

## L21 — Hard Link vs Symbolic Link

> [!quote] Tabella comparativa
> | | Hard Link | Symbolic Link |
> |---|---|---|
> | Cos'è | Altro nome per lo stesso Inode | File speciale che contiene un path |
> | Inode | Condiviso | Proprio (diverso dal target) |
> | Cross-filesystem | ❌ No | ✅ Sì |
> | Se cancelli il target | Il link funziona ancora | Link rotto (dangling) |
> | Cicli | Impossibile | Possibili (loop) |
> | Comando | `ln src dest` | `ln -s src dest` |

> [!abstract] Contatore link nell'Inode
> Il file viene fisicamente eliminato **solo quando**: contatore hard link = 0 **E** nessun processo lo tiene aperto. Questo è perché `rm` non è "delete" ma "unlink": decrementa il contatore.

---

## L22 — I/O di Basso Livello: le Syscall fondamentali

> [!quote] API POSIX per I/O su file
> ```c
> // Apri/crea un file → ritorna FD
> int fd = open("file.txt", O_RDWR | O_CREAT | O_TRUNC, 0644);
>
> // Scrivi N byte dal buffer → ritorna byte scritti
> ssize_t n = write(fd, buffer, count);
>
> // Leggi fino a N byte nel buffer → ritorna byte letti, 0=EOF
> ssize_t n = read(fd, buffer, count);
>
> // Sposta l'offset di lettura/scrittura
> off_t pos = lseek(fd, offset, SEEK_SET | SEEK_CUR | SEEK_END);
>
> // Chiudi il FD
> close(fd);
> ```

> [!quote] Flag di open()
> - `O_RDONLY` / `O_WRONLY` / `O_RDWR`: modalità accesso
> - `O_CREAT`: crea il file se non esiste (richiede il terzo argomento `mode`)
> - `O_TRUNC`: tronca il file a 0 byte se esiste
> - `O_APPEND`: ogni `write()` va automaticamente in fondo al file

> [!example] Sparse File — buchi nel file
> ```c
> fd = open("sparse.bin", O_WRONLY | O_CREAT, 0644);
> write(fd, "INIZIO", 6);
> lseek(fd, 100000, SEEK_CUR);  // salta 100KB senza scrivere
> write(fd, "FINE", 4);
> close(fd);
> ```
> `ls -l`: dimensione logica ≈ 100KB. `du`: spazio fisico ≈ pochi KB.
> Il FS non alloca blocchi per il "buco" → legge come zero automaticamente.

> [!danger] read() su file vs Pipe: comportamento diverso
> - `read()` su **file**: ritorna 0 (EOF) se hai raggiunto la fine. Non blocca.
> - `read()` su **pipe**: si **blocca** se non ci sono dati, finché qualcuno non scrive o chiude il write-end.

---

## L23 — Metodi di Allocazione dei File

> [!abstract] Nodo
> Come il FS mappa un file ai suoi blocchi fisici su disco. 3 approcci, ognuno con trade-off diversi.

### Allocazione Contigua

> [!quote] Logica
> Il file occupa blocchi fisicamente consecutivi. Metadati: blocco iniziale + numero blocchi.
> - ✅ Accesso sequenziale ottimale (minimo seek)
> - ✅ Accesso diretto banale: blocco = $\lfloor B / \text{BlockSize} \rfloor$
> - ❌ Frammentazione esterna (buchi sparsi nel disco)
> - ❌ Difficile espandere il file

### Allocazione Concatenata (FAT)

> [!quote] Logica
> Ogni blocco contiene un puntatore al blocco successivo (lista concatenata). FAT sposta i puntatori in una tabella centrale in RAM.
> - ✅ Nessuna frammentazione esterna
> - ✅ Espansione facile
> - ❌ Accesso random lento (bisogna scorrere la catena)
> - FAT12/16/32 usata ancora oggi per chiavette USB, schede SD, ESP

### Allocazione Indicizzata (Unix Inode)

> [!quote] Logica
> Un blocco indice contiene l'array di puntatori ai blocchi dati (o usa la struttura ibrida dell'inode con indiretti multipli).
> - ✅ Accesso random efficiente (leggi il blocco indice, salta direttamente al dato)
> - ✅ Nessuna frammentazione esterna
> - ❌ Overhead per file piccoli (1 blocco indice sprecato)

---

## L23 — Gestione Spazio Libero e Evoluzione ext

> [!quote] Metodi per tracciare i blocchi liberi
> 1. **Bitmap**: 1 bit per blocco (0=occupato, 1=libero). Facile trovare blocchi contigui. Serve RAM (32MB per 1TB con blocchi 4KB).
> 2. **Lista concatenata**: i blocchi liberi si collegano tra loro. Zero overhead RAM, lenta per trovare blocchi contigui.
> 3. **Raggruppamento (Grouping)**: il primo blocco libero contiene N indirizzi di altri blocchi liberi. Compromise.

> [!quote] Evoluzione Linux ext
> - **ext2**: introduce i **Block Groups** (metadati vicini ai dati → meno seek HDD)
> - **ext3**: aggiunge il **Journaling** per il recovery rapido
> - **ext4**: aggiunge gli **Extents** (una entry descrive una sequenza contigua invece di un singolo blocco), Delayed Allocation, supporto file grandi

---

## L24/L25 — Journaling: protezione da crash

> [!abstract] Nodo
> Un crash durante la scrittura di metadati (directory, inode, bitmap) lascia il FS inconsistente. Il journaling previene questo con una **transazione atomica**.

> [!quote] 4 fasi del journaling
> 1. **Write to Journal**: scrivi le modifiche nel log circolare (area dedicata e veloce del disco)
> 2. **Commit**: marca la transazione come "committed" nel journal
> 3. **Checkpoint**: applica le modifiche ai metadati reali sul disco
> 4. **Cleanup**: rimuovi la voce dal journal

> [!quote] Recovery dopo crash
> - Crash prima del Commit → transazione ignorata (Undo implicito)
> - Crash dopo Commit ma prima del Checkpoint → il SO rilegge il journal e completa (Redo)
> - Vantaggio: recovery in secondi (legge solo il piccolo journal) vs `fsck` che scandisce tutto il disco (minuti/ore)

> [!danger] Il journaling protegge i METADATI, non i dati
> Di default, ext3/4 garantisce la consistenza strutturale del FS (inode, directory). I dati del file potrebbero comunque essere persi o corrotti in caso di crash durante la scrittura. Modalità `data=journal` protegge anche i dati ma è più lenta.

---

## L24/L25 — VFS: l'astrazione universale

> [!abstract] Nodo
> Il VFS (Virtual File System) è lo strato del kernel che permette di usare ext4, FAT32, NTFS, tmpfs, proc… con la stessa identica API (`open`, `read`, `write`). L'applicazione non sa su quale FS sta lavorando.

> [!quote] Architettura a 4 strati
> 1. **Logical File System**: API utente (open/close/read/write), gestisce metadati e permessi
> 2. **File Organization Module**: traduce indirizzi logici blocco → fisici, gestisce spazio libero
> 3. **Basic File System**: I/O generico sui settori, gestisce il buffer cache
> 4. **I/O Control (Device Drivers)**: codice specifico per ogni hardware

> [!quote] Strutture dati VFS su disco vs in RAM
> | Su Disco (persistente) | In RAM (volatile/cache) |
> |---|---|
> | Superblock | Mount Table |
> | Directory Structure | Directory Cache (dentry cache) |
> | FCB/Inode | System-wide Open File Table |
> | Data Blocks | Per-Process FD Table |
> | | In-Memory Inode Table |

---

## L24/L25 — Sottosistema I/O: dispositivi e driver

> [!abstract] Nodo
> Il kernel gestisce periferiche eterogenee (disco, tastiera, scheda di rete) tramite un'architettura uniforme. Il segreto: i **Device Driver** come strato di traduzione.

> [!quote] 3 categorie di dispositivi
> - **Block Devices**: accesso random a blocchi fissi (HDD, SSD, USB storage) → supportano `seek`
> - **Character Devices**: flusso sequenziale di byte (tastiera, mouse, stampante, porte seriali) → no seek
> - **Network Devices**: comunicazione tramite socket (TCP/UDP) → API speciale: `send`, `recv`, `bind`, `listen`

> [!quote] Device Driver
> - Gira in **Kernel Mode (Ring 0)**: un bug in un driver → kernel panic potenziale
> - Implementa una tabella di function pointer standard (`open`, `read`, `write`, `ioctl`) che il kernel invoca
> - `ioctl()`: syscall "pass-partout" per comandi non standardizzati (es. espellere CD, configurare interfaccia di rete)

> [!quote] Gestione Interrupt (I/O asincrono)
> 1. Driver invia comando al dispositivo
> 2. Processo si sospende (Waiting)
> 3. Dispositivo finisce → genera **Hardware Interrupt**
> 4. **Interrupt Handler** si sveglia → notifica il driver → il driver sveglia il processo → torna Ready

> [!example] TTY e Line Discipline: perché il backspace funziona
> Il terminale è un character device speciale. La **Line Discipline** è uno strato software sopra il driver grezzo che:
> - Interpreta Backspace → cancella l'ultimo carattere nel buffer
> - Converte `\r` in `\n`
> - `Ctrl+C` → invia SIGINT al processo in foreground
> - `Ctrl+Z` → invia SIGTSTP (stop)
> Senza Line Discipline, ogni programma dovrebbe gestire questi caratteri da solo.

---

# 🗺️ MAPPA DELLE CONNESSIONI

| Concetto           | Si collega a                                       |
| ------------------ | -------------------------------------------------- |
| System Call        | → Dual Mode, Kernel vs User                        |
| fork() + COW       | → Demand Paging, Page Fault                        |
| Page Fault         | → Algoritmi Sostituzione, Dirty Bit, Swap          |
| Semafori           | → Sezione Critica, Produttore-Consumatore          |
| Deadlock           | → Condizioni Coffman, 5 Filosofi, Ordinamento Lock |
| Priority Inversion | → Scheduling a Priorità, Semafori                  |
| TLB                | → Page Table, EAT, Context Switch                  |
| Thrashing          | → Working Set, Multiprogrammazione                 |
| Inode              | → Directory, Hard Link, Allocazione Blocchi        |
| Journaling         | → Crash Recovery, Metadati, ext3/ext4              |
| Device Driver      | → Interrupt, Kernel Mode, VFS                      |
| RAID               | → Affidabilità, Striping, Parità                   |

