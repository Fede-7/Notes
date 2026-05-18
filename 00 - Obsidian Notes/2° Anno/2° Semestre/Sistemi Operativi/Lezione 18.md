# Trascrizione Lezione: Algoritmi di Sostituzione di Pagina e Thrashing

**Data:** 29 aprile 2026
**Argomento:** Algoritmi di Sostituzione (FIFO, OPT, LRU, Clock), Allocazione dei Frame (Locale vs Globale) e Thrashing.

---

### 1. Introduzione alla Sostituzione di Pagina

Quando i frame liberi si esauriscono, il Sistema Operativo deve scegliere una **Pagina Vittima** da espellere dalla RAM per fare spazio a una nuova pagina richiesta (Page Fault).
*   **Costo del Dirty Bit:** Se la pagina vittima ha il *Dirty Bit* attivo (è stata modificata), deve essere scritta sul Backing Store prima di essere sovrascritta (costoso). Se è *Clean* (non modificata), può essere semplicemente sovrascritta, poiché esiste già una copia aggiornata su disco.
*   **Ottimizzazione Preventiva:** Il SO può periodicamente scrivere le pagine "sporche" su disco durante i tempi morti (idle), azzerando il Dirty Bit. Questo trasforma una futura scrittura costosa in una semplice sovrascrittura veloce al momento del fault.
*   **Obiettivo:** Minimizzare i Page Fault futuri scegliendo la pagina che ha meno probabilità di essere riutilizzata a breve.

Per analizzare gli algoritmi, si utilizza una **Stringa di Riferimenti** (sequenza di accessi alle pagine logiche).

---

### 2. Algoritmi di Sostituzione di Pagina

#### A. FIFO (First-In, First-Out)
Sostituisce la pagina caricata da più tempo in memoria.
*   **Implementazione:** Coda semplice.
*   **Problema:** Soffre dell'**Anomalia di Belady**.
    *   *Definizione:* In alcuni casi, aumentare il numero di frame disponibili porta a un *aumento* del numero di Page Fault, invece che a una diminuzione. Ciò indica un uso inefficiente della memoria aggiuntiva.
*   **Performance:** Generalmente scarsa, poiché non considera la frequenza o la recentezza d'uso.

#### B. Optimal (OPT)
Sostituisce la pagina che non verrà utilizzata per il periodo di tempo più lungo nel futuro.
*   **Vantaggio:** Garantisce il minimo numero possibile di Page Fault per una data stringa di riferimenti. È l'algoritmo teorico di riferimento.
*   **Svantaggio:** Non implementabile nella pratica, poiché richiede la conoscenza del futuro (preveggenza degli accessi).
*   **Utilizzo:** Serve come benchmark per valutare l'efficienza degli altri algoritmi.

#### C. LRU (Least Recently Used)
Sostituisce la pagina che non viene utilizzata da più tempo nel passato.
*   **Logica:** Si basa sul principio di località temporale: se una pagina è stata usata recentemente, è probabile che lo sarà ancora a breve.
*   **Proprietà:** È uno **Stack Algorithm**. Non soffre dell'anomalia di Belady: all'aumentare dei frame, il numero di fault non aumenta mai.
*   **Implementazione Pratica (Difficile):**
    1.  **Contatori/Timestamp:** Ogni entry nella Page Table ha un campo "Time of Use". La CPU aggiorna questo timestamp ad ogni accesso. Richiede hardware speciale e overhead di aggiornamento.
    2.  **Stack/Liste Doppie:** Mantenere una lista doppiamente linkata delle pagine. Ad ogni accesso, la pagina viene spostata in testa alla lista. La coda contiene la vittima. L'aggiornamento della lista ad ogni accesso è computazionalmente costoso (O(1) ma con costante alta).

> **Esercizio Pratico (Simulazione LRU con Stack):**
> Per simulare LRU manualmente, si usa uno stack verticale.
> *   **Hit:** La pagina riferita viene spostata in cima allo stack (diventa la più recente).
> *   **Fault (Piena):** La nuova pagina entra in cima, tutte le altre scivolano giù, e l'ultima in fondo (la meno recente) esce (vittima).
> *   **Fault (Spazio libero):** La nuova pagina entra in cima.

#### D. Approssimazioni di LRU: Algoritmo Clock (Second Chance)
Poiché LRU puro è costoso, si usano approssimazioni basate sul **Bit di Riferimento (Reference Bit)**.
*   **Funzionamento:**
    *   Le pagine sono disposte in una lista circolare (come i numeri di un orologio).
    *   Un puntatore ("lancetta") scorre le pagine.
    *   Quando serve una vittima, l'algoritmo controlla il bit di riferimento della pagina puntata:
        *   Se **R=1**: La pagina è stata usata recentemente. Le si dà una "seconda chance": si imposta **R=0** e si passa alla successiva.
        *   Se **R=0**: La pagina non è stata usata di recente. Viene scelta come vittima.
    *   Il bit di riferimento viene impostato a 1 dalla MMU ogni volta che la pagina viene accessibile (lettura/scrittura).
*   **Enhanced Second Chance (Clock Algorithm con Dirty Bit):**
    Considera due bit: **R** (Riferimento) e **M** (Modifica/Dirty). Classifica le pagine in 4 classi di priorità per la sostituzione:
    1.  **(R=0, M=0):** Non usata, non modificata. **Vittima ideale** (nessun I/O necessario).
    2.  **(R=0, M=1):** Non usata recentemente, ma modificata. Buona vittima, ma richiede write-back su disco.
    3.  **(R=1, M=0):** Usata recentemente, non modificata. Probabilmente utile, ma facile da ripristinare se espulsa.
    4.  **(R=1, M=1):** Usata recentemente e modificata. **Ultima scelta** (costosa da espellere).
    *   L'algoritmo fa fino a 4 giri dell'orologio, cercando la prima classe disponibile nell'ordine sopra indicato.

#### E. Algoritmi a Contatore (Frequency-Based)
Mantengono un contatore del numero totale di accessi per ogni pagina.
*   **LFU (Least Frequently Used):** Sostituisce la pagina con il contatore più basso.
    *   *Problema:* Una pagina usata intensamente all'inizio e mai più dopo rimane "bloccata" con un conteggio alto, impedendo la sua sostituzione anche se non serve più.
*   **MFU (Most Frequently Used):** Sostituisce la pagina con il contatore più alto (assumendo che quelle usate poco siano appena state caricate e serviranno a breve).
*   **Giudizio:** Generalmente meno efficaci di LRU/Clock perché non catturano bene la località temporale recente.

---

### 3. Allocazione dei Frame

Come distribuire i frame fisici tra i vari processi?

#### A. Allocazione Locale vs Globale
*   **Allocazione Locale (Local Replacement):**
    *   Ogni processo ha un insieme fisso o proporzionale di frame dedicati.
    *   La sostituzione avviene solo all'interno dei frame assegnati a quel processo.
    *   *Vantaggio:* Isolamento. Un processo "affamato" non influisce sulle performance degli altri.
    *   *Svantaggio:* Possibile sottoutilizzo della memoria se un processo non usa tutti i suoi frame mentre un altro ne avrebbe bisogno.
*   **Allocazione Globale (Global Replacement):**
    *   Tutti i frame liberi sono condivisi. Un processo può prendere un frame da un altro processo.
    *   *Vantaggio:* Utilizzo più efficiente della memoria totale.
    *   *Svantaggio:* Interferenza. Un processo ad alta intensità di I/O può rubare frame agli altri, degradando le performance globali.

#### B. Politiche di Allocazione
*   **Fixed Allocation:** Numero di frame fisso per processo (spesso proporzionale alla dimensione del processo o alla priorità).
*   **Priority Allocation:** Processi ad alta priorità ricevono più frame.
*   **Minimo Garantito:** Ogni processo deve avere un numero minimo di frame pari al massimo numero di pagine richieste da una singola istruzione complessa (per evitare restart continui dell'istruzione).

#### C. Gestione del Pool Libero (Watermarking)
Nei sistemi moderni (Global Replacement), il SO mantiene un **Pool di Frame Liberi**.
*   **Soglia Minima:** Se i frame liberi scendono sotto questa soglia, parte un demone ("Reaper" o "Page Daemon") che esegue aggressivamente l'algoritmo di sostituzione (es. Clock) per liberare frame.
*   **Soglia Massima:** Il demone lavora fino a raggiungere la soglia massima, per evitare oscillazioni continue (hysteresis).
*   **Out of Memory (OOM) Killer:** Se la memoria è critica e non si possono liberare frame sufficienti, Linux usa un punteggio (OOM Score) per terminare (kill) i processi meno critici e liberare la loro memoria.

---

### 4. Thrashing (Satellamento)

Il **Thrashing** si verifica quando il sistema spende più tempo a scambiare pagine (Page In/Page Out) che a eseguire istruzioni utili.

*   **Cause:**
    *   Grado di multiprogrammazione troppo elevato.
    *   Somma dei working set (insiemi di pagine attive) dei processi > Memoria Fisica disponibile.
    *   Allocazione insufficiente di frame per processo (sotto il minimo richiesto dalla località).
*   **Sintomi:**
    *   Elevatissimo tasso di Page Fault.
    *   Coda di I/O sul disco molto lunga.
    *   **Crollo dell'utilizzo della CPU:** La CPU diventa idle perché tutti i processi sono in stato di *Waiting* (in attesa di I/O dal disco).
*   **Soluzione:**
    *   Ridurre il grado di multiprogrammazione (sospendere o terminare alcuni processi).
    *   Migliorare l'algoritmo di sostituzione o aumentare la RAM fisica.
    *   Utilizzare algoritmi che stimano il *Working Set* di ogni processo per allocare dinamicamente i frame necessari a mantenere la località.

---

*Fine della lezione.*
