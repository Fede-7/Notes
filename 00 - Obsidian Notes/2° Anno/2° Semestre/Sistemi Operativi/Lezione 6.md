---
Date: 2026-03-25
Professore:
tags:
  - SO
  - NoAudio
---
- [ ] Signal Handling.
- [ ] Segnali e handler.
- [ ] Cancellazione threads.
- [ ] Thread-Specific data.
- [ ] Linux si riferisce a tasks piuttosto che a threads.
- [ ] Windows threads.

## CPU Scheduler e Dispatcher
La gestione di questi scambi è affidata a due componenti fondamentali:

### Lo Short-term Scheduler (CPU Scheduler)
È il decisore. Seleziona quale tra i processi attualmente presenti nella **Coda Ready** (pronti per l'esecuzione) debba ottenere l'uso della CPU.
Le decisioni di scheduling avvengono in 4 situazioni:
1. Un processo passa da *Running* a *Waiting* (es. richiede I/O).
2. Un processo passa da *Running* a *Ready* (es. scade il suo tempo o c'è un interrupt).
3. Un processo passa da *Waiting* a *Ready* (es. l'I/O è completato).
4. Un processo termina.

Le decisioni nei casi 1 e 4 sono **Senza Prelazione (Non-preemptive)**: il processo cede volontariamente la CPU. Le decisioni nei casi 2 e 3 sono **Con Prelazione (Preemptive)**: il SO strappa la CPU al processo in esecuzione.

### Il Dispatcher
È l'esecutore materiale. Dà fisicamente il controllo della CPU al processo selezionato dallo Scheduler. Il suo lavoro richiede:
* Effettuare il **Context Switch** (salvataggio stato vecchio, caricamento stato nuovo).
* Passare alla modalità utente (*User Mode*).
* Saltare alla corretta riga di codice (Program Counter) per riavviare il programma.
Essendo un'operazione che si ripete costantemente, la **Latenza di Dispatch** (il tempo necessario per fermare un processo e farne partire un altro) deve essere il più breve possibile, altrimenti si crea troppo *overhead*.

## Criteri di Scheduling
Per valutare la bontà di un algoritmo di scheduling, si utilizzano diversi parametri:
* **Utilizzo CPU:** Percentuale di tempo in cui la CPU è occupata (da massimizzare).
* **Throughput:** Numero di processi completati nell'unità di tempo (da massimizzare).
* **Turnaround time (Tempo di completamento):** Quanto tempo ci mette un processo dalla sua creazione alla sua terminazione (include attese, esecuzione e I/O). (da minimizzare).
* **Waiting time (Tempo di attesa):** È la somma dei tempi che il processo passa **fermamente bloccato nella Coda Ready** aspettando il suo turno (da minimizzare).
* **Response time (Tempo di risposta):** Tempo che intercorre tra l'invio di una richiesta e la primissima risposta prodotta (fondamentale minimizzarne non solo la media, ma soprattutto la **varianza** nei sistemi interattivi/desktop, per evitare scatti o lag visivi all'utente).

## Algoritmi di Scheduling Tradizionali
Gli algoritmi di scheduling tradizionali si occupano di ottimizzare metriche il tempo medio di attesa o la reattività. Ne esistono di vari tipi, tra cui:
### 1. First-Come, First-Served (FCFS)
Il processo che richiede la CPU per primo la ottiene. È gestito con una semplice coda FIFO.
* **Pro:** Facilissimo da implementare.
* **Contro (Effetto Convoglio):** Se un processo lunghissimo (CPU-bound) arriva per primo, tutti i processi brevi (I/O-bound) dietro di lui dovranno aspettare tantissimo. Il tempo di attesa medio varia enormemente in base all'ordine di arrivo. È un algoritmo *Non-preemptive*.

### 2. Shortest-Job-First (SJF)
Associa a ogni processo la lunghezza del suo **prossimo CPU Burst**. La CPU viene assegnata al processo col burst più breve.
* **Pro:** È **matematicamente ottimale**. Garantisce il tempo di attesa medio più basso in assoluto per un dato set di processi.
* **Il Problema:** Il SO non può sapere a priori quanto durerà la prossima elaborazione di un processo prima che questo chieda un I/O. Deve quindi fare delle stime (che hanno un costo e possono anche essere sbagliate).

Esiste anche la variante *Preemptive* di questo algoritmo, chiamata **Shortest-Remaining-Time-First (SRTF)**: se arriva un nuovo processo nella coda ready con un tempo stimato inferiore al tempo *rimanente* del processo attualmente in esecuzione, quest'ultimo viene prelazionato (interrotto istantaneamente).

#### Stima del CPU Burst: Exponential Averaging
Poiché con l'algoritmo SJF non possiamo conoscere il futuro, possiamo solo fare una **stima** basandoci sul comportamento passato del processo (l'assunto è che i prossimi burst saranno simili a quelli recenti).

Si utilizza una tecnica chiamata **Media Esponenziale (Exponential Averaging)**, la cui formula è:
$\tau_{n+1} = \alpha $t_n$ + (1 - \alpha)\tau_n$.

Dove:
* $\tau_{n+1}$ = È la nostra predizione per il *prossimo* CPU burst.
* $\alpha$ = È un "peso" compreso tra 0 e 1 (di solito impostato a $\frac{1}{2}$). Determina quanto conta la storia recente rispetto a quella passata.
* $t_n$ = È la lunghezza *reale* dell'ultimissimo CPU burst appena concluso.
* $\tau_n$ = Era la nostra vecchia predizione.
$$
**Perché "Esponenziale"?**
$$
Espandendo la formula matematicamente, si nota che **il peso della storia passata decade in modo esponenziale**: al SO interessa molto di più cosa ha fatto il processo 2 millisecondi fa, rispetto a cosa ha fatto un'ora fa.

### 3. Shortest-Remaining-Time-First (SRTF)
È la **versione con prelazione (preemptive)** dell'algoritmo SJF. 
Se nella Coda Ready arriva un nuovo processo il cui tempo stimato di completamento è *inferiore* al tempo rimanente del processo attualmente in esecuzione, il SO esegue un Context Switch immediato (prelazione), mettendo in pausa il processo corrente per far partire quello nuovo più breve.

### 4. Scheduling con Priorità
A ogni processo viene associato un numero intero che rappresenta la sua **priorità** (generalmente, un numero più basso indica una priorità più alta, es. 0 = massima priorità). La CPU viene allocata al processo con la priorità più alta.
L'algoritmo SJF non è altro che un caso particolare di scheduling con priorità, dove la priorità è l'inverso della lunghezza stimata del prossimo CPU burst.
Può essere implementato con o senza prelazione.

*   **Il Problema: Starvation**
    I processi a bassissima priorità potrebbero non essere mai eseguiti se il sistema continua a ricevere un flusso costante di processi ad alta priorità.

*   **La Soluzione: Aging**
    Tecnica che consiste nell'aumentare gradualmente (col passare del tempo) la priorità dei processi che rimangono per troppo tempo in attesa nella Coda Ready, garantendo che prima o poi vengano eseguiti.

### 5. Round Robin (RR)
È l'algoritmo progettato specificamente per i sistemi in *time-sharing*. 
A ogni processo viene assegnata una piccola quantità fissa di tempo di CPU, chiamata **Time Quantum (q)** (di solito tra 10 e 100 millisecondi).

*   **Come funziona:**
	La Coda Ready è trattata come una coda circolare (FIFO). Il SO assegna la CPU al primo processo; se questo non termina entro il suo quanto di tempo $q$, scatta un timer, il processo viene **prelazionato** (interrotto forzatamente) e rimesso in fondo alla coda ready.

*   **Prestazioni:** Dipendono totalmente dalla dimensione di $q$:
    *   Se $q$ è *enorme*, il Round Robin degenera diventando un banale FCFS.
    *   Se $q$ è *minuscolo*, l'overhead del Context Switch "mangia" tutta la potenza della CPU.

### 6. Code Multiple (Multilevel Queue)
Invece di avere una singola Coda Ready $O(n)$, i processi vengono partizionati (spesso in modo statico e permanente) in **diverse code separate**, in base al loro tipo (es. una coda per i processi in attesa di poter usare standard input, detti **foreground**, e una per quelli *background*).

Bisogna quindi decidere quale coda servire. Può essere a *priorità fissa* (si svuota prima tutto il foreground, ma c'è rischio starvation per il background) oppure tramite *Time-slice* (es. l'80% del tempo della CPU è dedicato alla coda foreground, il 20% a quella background).

Ogni coda può avere il suo algoritmo di scheduling. Ad esempio, la coda foreground potrebbe usare il Round Robin per garantire reattività, mentre la coda background un semplice FCFS.

### 7. Code Multiple con Feedback
È l'algoritmo più flessibile e complesso. Simile alle Code Multiple, ma qui **i processi possono spostarsi da una coda all'altra** dinamicamente. I processi vengono separati in base alle loro caratteristiche (es. i processi I/O-bound, che restano poco in CPU, vengono tenuti nelle code ad altissima priorità).

Se un processo usa troppa CPU (CPU-bound), viene "declassato" spingendolo nelle code a priorità inferiore, mentre un processo relegato nelle code basse da troppo tempo viene promosso a una coda superiore per evitare la starvation (aging).

## Algoritmi di Real-Time CPU Scheduling
I sistemi Real-Time gestiscono task con vincoli temporali. Nella maggior parte dei casi con vincoli temporali intendiamo **scadenze (deadline)**.

A differenza dello scheduling tradizionale, si occupano quindi di rispettare questi vincoli temporali piuttosto che ottimizzare metriche di performance.

Gli algoritmi di Real-Time CPU Scheduling si dividono in:
1.  **Soft Real-Time:** I processi critici ottengono sempre priorità massima rispetto a quelli non critici, ma il SO non offre una garanzia assoluta matematica sul rispetto delle scadenze.
2.  **Hard Real-Time:** Un task *deve assolutamente* essere completato prima della sua deadline.
Fanno spesso uso di ulteriori algoritmi di *Admission Control*, ovvero algoritmi che rifiutano l'esecuzione di un task se questo chiede risorse che farebbero saltare le deadline.

Per supportare il real-time, i SO devono avere Kernel con *prelazione* e ridurre al minimo le **Latenze di Evento**:
*   *Interrupt Latency:* Tempo tra l'arrivo dell'interrupt e l'inizio della routine di servizio.
*   *Dispatch Latency:* Tempo per fermare il processo corrente e far partire quello nuovo.

Esistono diversi tipi di algoritmi di Real-Time CPU Scheduling, tra cui:
### Rate Monotonic Scheduling (RMS)
Algoritmo a priorità statica. La priorità viene assegnata **in base all'inverso del periodo**:
*   Periodo breve (il task si ripete molto spesso) = Priorità altissima.
*   Periodo lungo = Priorità bassa.

Si usa per task periodici, ovvero task che richiedono la CPU a intervalli costanti (hanno un tempo di processo $t$, una deadline $d$, e un periodo $p$).

*Problema (Deadline Persa):* RMS assegna quindi priorità ai task più frequenti, ma garantisce il rispetto delle deadline solo fino a circa il 69% di utilizzo della CPU; oltre questa soglia, i task potrebbero mancare la deadline (e quindi fallire).

### Earliest Deadline First (EDF)
Algoritmo a priorità dinamica. La priorità viene calcolata istante per istante: **più la scadenza (deadline) è imminente, più la priorità si alza**.
Se la somma dell'utilizzo della CPU richiesto dai task è $\le 100\%$, l'EDF garantisce che nessuna deadline verrà mai mancata.

Si può applicare sia a tasks periodici che a non periodici.

### Scheduling a Quote Proporzionali
Viene assegnato un numero totale $T$ di "quote" (es. 100) di CPU. Se un'applicazione riceve $N$ quote (es. 20), lo scheduler le garantisce matematicamente l'uso di $N/T$ (ovvero il 20%) del tempo totale del processore. L'ammissione di nuovi processi dipende dalle quote rimaste libere (se ne sono già state assegnate 99 e un processo ne richiede 2, o si accontenta di 1 o viene rifiutato).

In realtà questo algoritmo non è specifico per il real-time; si basa infatti su una suddivisione equa della quantità di CPU, indipendentemente da periodi o deadline. Esso viene catalogato come Real-Time perché è l'unico modo per garantire matematicamente a un processo una fetta costante di CPU, permettendogli di rispettare indirettamente i suoi vincoli di tempo.

---



## Thread Scheduling e Multiprocessori

### Scheduling dei Thread (PCS vs SCS)
Nei moderni Sistemi Operativi, ciò che viene schedulato fisicamente dal Kernel **non sono i processi, ma i Kernel-level Threads**.
Esistono due domini di competizione per l'allocazione della CPU:
1.  **Process-Contention Scope (PCS):** Tipico dei modelli *Many-to-One* e *Many-to-Many*. La competizione per l'accesso ai thread del kernel (LWP) avviene solo tra i thread utente appartenenti allo **stesso processo**. È gestito dalla libreria dei thread.
2.  **System-Contention Scope (SCS):** La competizione avviene tra **tutti i thread del sistema**, indipendentemente dal processo a cui appartengono. Sistemi *One-to-One* come Windows e Linux usano esclusivamente SCS.

### Scheduling Multi-Processore
Con più CPU (o core), lo scheduling diventa enormemente più complesso e può essere gestito attraverso le seguenti strategie:

1. **Asymmetric Multiprocessing:** Un solo processore (il Master) prende tutte le decisioni di scheduling e accede alle strutture dati. Semplifica la gestione (nessuna condivisione di dati) ma il Master diventa un collo di bottiglia.

2. **Symmetric Multiprocessing (SMP):** È l'approccio standard odierno. **Ogni processore si auto-schedula**. Può esserci una Coda Ready comune a tutti (causa problemi di concorrenza/lock), oppure **ogni core ha la sua Coda Ready privata** (soluzione standard attuale).

Inoltre possiamo trovare il meccanismo di **Chip Multithreading (CMT / Hyperthreading)**. Questo prevede che ogni core fisico appaia al SO come se fossero due (o più) CPU logiche separate, permettendo di nascondere i tempi morti dovuti all'attesa della memoria (*memory stall*).

#### Load Balancing e Processor Affinity
Nei sistemi SMP con code private, è fondamentale che i core abbiano carichi di lavoro equilibrati.
Si usano quindi due tecniche di **Load Balancing (Bilanciamento del carico)**:

* **Push migration**, ovvero un processo di sistema controlla i carichi e "spinge" i task dai core sovraccarichi a quelli scarichi;

* **Pull migration**, ovvero un core in *idle*, cioè senza far nulla, che "ruba" task dalla coda di un core occupato.

A causa della memoria Cache, spostare un thread da un core all'altro è costoso (la cache del nuovo core va riempita da zero). Il SO cerca quindi di mantenere un thread sempre sullo stesso processore (**Processor Affinity**). Può essere **Soft** (il SO ci prova, ma senza garanzie) o **Hard** (il programmatore vincola il thread a un set specifico di processori).

##### NUMA
La Processor Affinity serve specialmente per l'architettura **NUMA (Non-Uniform Memory Access)**, in cui il processore accede alla sua memoria locale molto più velocemente rispetto alla memoria collegata a un altro processore.

##### Heterogeneous Multiprocessing (HMP)
Architettura tipica del mondo mobile. I core fisici non sono tutti identici: alcuni sono grandi e potenti (ma consumano molta batteria), altri sono lenti ma estremamente efficienti dal punto di vista energetico. Lo scheduler qui non punta solo al bilanciamento delle performance, ma è progettato per **risparmiare energia**.

## Virtualizzazione e Scheduling
Nei sistemi virtualizzati, l'Hypervisor deve schedulare l'utilizzo della CPU fisica tra le varie Macchine Virtuali (SO ospiti). A sua volta, il SO ospite sta facendo girare i *suoi* algoritmi di scheduling per i suoi thread interni.

Il SO ospite crede (erroneamente) di possedere l'intera CPU in esclusiva. Questo strato doppio di scheduling può quindi annullare i benefici di un buon algoritmo del SO ospite e causare ritardi imprevisti nei tempi di risposta.

## Scheduling in Linux e Windows

### Lo Scheduling in Linux
Linux ha cambiato radicalmente il suo scheduler nel corso degli anni:

* **Versioni storiche (pre-2.5):** Usava una singola lista per tutti i processi ($O(n)$) e una variante del Round Robin pesato in base a un valore di *nice* (gentilezza, ovvero quanto i task tendevano a cedere il posto ad altri).

* **Kernel v2.5:** Usava due array separati per ogni CPU ($O(1)$): un array *active* (task con tempo ancora a disposizione) e uno *expired* (task che hanno esaurito il quantum). Finiti i task active, si scambiavano semplicemente i puntatori dei due array. Rapido ma pessimo per la reattività.

* **Kernel 2.6.23+:** Non usa i tradizionali "quanti di tempo" fissi. Cerca di distribuire il tempo della CPU in modo perfettamente "equo" proporzionalmente al "peso" (priorità/nice) del task. Invece della priorità pura, calcola quanto **tempo virtuale** un processo ha effettivamente girato. Il tempo scorre più o meno velocemente in base alla priorità (il vruntime di un processo a bassa priorità scorre molto in fretta).

* **Kernel 6.6+:** la versione precedente favoriva l'equità globale ma a volte generava *lag* nelle interfacce grafiche. Questa nuova versione nasce quindi per unire Equità e Reattività. Si basa sul concetto di *Lag* (da non confondere con il lag di sopra), ovvero la differenza tra quanto tempo di CPU un task *avrebbe dovuto* ricevere e quanto ne ha *effettivamente* ricevuto (con *Lag Positivo* il task è "elegibile", altrimenti ha consumato troppo e viene stoppato). L'algoritmo sceglie infine il task elegibile con la *Virtual Deadline* più vicina.

### Lo Scheduling in Windows
Windows utilizza un sistema **Priority-based Preemptive** (basato su priorità, con prelazione). Usa uno schema a **32 livelli di priorità**:
* `0`: il thread di gestione della memoria;
* `1 - 15`: Classe a priorità variabile (assegna dei boost e penalità per garantire l'interattività);
* `16 - 31`: Classe Real-Time (priorità fissa, per task critici).
Ogni livello di priorità ha una propria coda; lo scheduler sceglie sempre il thread con priorità più alta disponibile. Se non trova nessun thread pronto, esegue il *thread idle* che non svolge lavoro utile ma mantiene la CPU occupata (dato che non può restare senza far nulla);

Il componente del kernel che gestisce lo switch si chiama **Dispatcher**.