# Trascrizione Lezione: Thrashing, Working Set, Allocazione Memoria Kernel e Ottimizzazioni

**Data:** 30 aprile 2026
**Argomento:** Thrashing, Modello del Working Set, Buddy System e Slab Allocator, Architetture di Memoria (32/64-bit), Pre-paging e Considerazioni Finali.

---

### 1. Thrashing (Satellamento)

Il **Thrashing** si verifica quando il sistema spende più tempo a scambiare pagine (Page In/Page Out) che a eseguire istruzioni utili. È una forma di *livelock*: i processi non sono bloccati permanentemente (deadlock), ma fanno progressi infinitesimali a causa del continuo swapping.

*   **Meccanismo:**
    *   Se un processo non ha frame sufficienti per il suo *working set* (insieme di pagine attive), genera continui Page Fault.
    *   Per soddisfare il fault, il SO deve espellere una pagina. Se l'allocazione è **globale**, il processo "ruba" frame ad altri processi.
    *   Gli altri processi, a loro volta, vanno in sofferenza e generano fault, rubando frame a loro volta.
    *   Si crea un ciclo vizioso di sostituzioni reciproche.
*   **Impatto sulle Performance:**
    *   Sovraccarico del disco (I/O bottleneck): tutte le richieste di paging si accodano sul disco.
    *   I processi entrano in stato di *Waiting* (in attesa di I/O).
    *   La coda dei processi *Ready* sulla CPU si svuota.
    *   **Paradosso:** All'aumentare del grado di multiprogrammazione oltre una certa soglia, l'utilizzo della CPU crolla drasticamente invece di aumentare.
*   **Prevenzione:**
    *   Monitorare la località dei processi.
    *   Ridurre il grado di multiprogrammazione (sospendere o terminare processi) quando la somma dei working set supera la RAM disponibile.
    *   Utilizzare algoritmi di sostituzione efficienti (es. Clock/Second Chance) per minimizzare i fault inutili.

---

### 2. Il Modello del Working Set

Il **Working Set** è un modello utilizzato dal SO per stimare la località di un processo e allocare dinamicamente i frame necessari.

*   **Definizione:** Dato una finestra temporale $\Delta$ (o un numero fisso di riferimenti $N$), il working set $W(t, \Delta)$ è l'insieme delle pagine diverse a cui il processo ha fatto riferimento negli ultimi $\Delta$ istanti.
*   **Funzionamento:**
    *   Il SO monitora gli accessi alla memoria.
    *   Se la somma delle dimensioni dei working set di tutti i processi attivi ($\sum |W_i|$) supera la memoria fisica disponibile, il sistema è in sofferenza (rischio thrashing).
    *   Il SO può quindi sospendere processi o ridurre la multiprogrammazione.
*   **Implementazione Pratica (Approssimazione):**
    *   Monitorare ogni singolo accesso è troppo costoso.
    *   Si usano interrupt periodici (es. ogni 5.000 o 10.000 cicli/istruzioni).
    *   Ad ogni interrupt, il SO controlla i **Bit di Riferimento** nelle Page Table.
    *   Si mantengono bit di "storia" (history bits) per ricordare se una pagina è stata usata nell'intervallo corrente o in quelli precedenti, permettendo una stima a grana più grossa della località senza overhead eccessivo.
*   **Relazione con Page Fault:**
    *   Un cambio di località (cambio di working set) causa tipicamente un picco di Page Fault, poiché le nuove pagine devono essere caricate dal disco.
    *   Monitorando la frequenza dei Page Fault, il SO può regolare dinamicamente l'allocazione dei frame: se i fault sono troppi, assegna più frame; se sono pochi, ne recupera alcuni.

---

### 3. Ottimizzazioni: Compressione della Memoria

Nei sistemi moderni (specialmente mobile, macOS, Windows 10/11), si preferisce spesso la **compressione in RAM** allo swapping su disco.

*   **Problema:** Scrivere pagine "sporche" (Dirty) su disco è lento e usura le memorie Flash (SSD/eMMC).
*   **Soluzione:**
    *   Quando la memoria scarseggia, invece di scrivere su disco, il SO comprime le pagine inattive e le salva in una zona riservata della RAM (*Compressed Memory*).
    *   **Vantaggio:** La compressione/decompressione in CPU è spesso più veloce dell'I/O su disco.
    *   **Trade-off:** Si sacrifica spazio RAM (per contenere i dati compressi) e cicli CPU, ma si guadagna in latenza e durata dell'hardware.
    *   Algoritmi di compressione veloci (basso ratio, alta velocità) sono preferiti.

---

### 4. Gestione della Memoria del Kernel

La memoria del Kernel ha requisiti diversi da quella utente:
1.  **Strutture Dati Prevedibili:** Il SO conosce a priori le strutture che dovrà allocare (PCB, Inode, ecc.).
2.  **Piccole Dimensioni:** Spesso le strutture sono più piccole di una pagina (4KB).
3.  **Contiguità Fisica:** Alcune operazioni (DMA, tabelle hardware) richiedono indirizzi fisici contigui.

Per gestire questo, Linux (e altri Unix-like) usano due allocatori complementari:

#### A. Buddy System (Allocatore a Bassa Granularità)
Gestisce la memoria fisica libera a livello di pagine/frame.
*   **Obiettivo:** Fornire blocchi di memoria fisicamente contigui di dimensione potenza di 2 ($2^n$ pagine).
*   **Allocazione:**
    *   Se si richiedono $K$ byte, il sistema trova il blocco libero più piccolo di dimensione $2^n \ge K$.
    *   Se il blocco disponibile è più grande, viene suddiviso ("splittato") in due "buddy" (gemelli) fino alla dimensione richiesta.
*   **Deallocation:**
    *   Quando un blocco viene liberato, il sistema controlla se il suo "buddy" è anche libero.
    *   Se sì, i due vengono fusi ("merged") in un blocco più grande.
*   **Svantaggio:** Frammentazione interna (se chiedo 21KB, ottengo un blocco da 32KB).

#### B. Slab Allocator (Allocatore ad Alta Granularità)
Gestisce le strutture dati specifiche del kernel sopra il Buddy System.
*   **Obiettivo:** Eliminare la frammentazione interna per oggetti piccoli e frequenti e velocizzare l'allocazione.
*   **Struttura a 3 Livelli:**
    1.  **Cache:** Contiene oggetti dello stesso tipo (es. `task_struct`, `inode`).
    2.  **Slab:** Un insieme di pagine fisicamente contigue (allocate dal Buddy System) che contiene multipli istanze dell'oggetto.
    3.  **Oggetto:** L'istanza singola della struttura dati (pre-inizializzata).
*   **Stati degli Slab:**
    *   *Full:* Tutti gli oggetti sono usati.
    *   *Partial:* Alcuni oggetti liberi, alcuni usati (prima scelta per allocazioni).
    *   *Empty:* Tutti liberi (pronti per essere distrutti o riutilizzati).
*   **Vantaggi:**
    *   Nessun overhead di inizializzazione/distruzione per ogni allocazione (gli oggetti sono "prefabbricati").
    *   Cache-friendly: gli oggetti dello stesso tipo tendono a stare vicini in memoria.
    *   Niente frammentazione interna significativa.

> **Flusso Tipico:** `kmalloc()` -> Cerca nella Slab Cache appropriata -> Se lo slab è pieno, chiede nuove pagine al Buddy System -> Restituisce puntatore all'oggetto.

---

### 5. Mapping della Memoria in Architetture Intel

#### Intel 32-bit (x86)
*   **Spazio Indirizzamento Logico:** 4 GB per processo.
*   **Divisione Tipica:**
    *   **User Space:** 0 - 3 GB (privato per ogni processo).
    *   **Kernel Space:** 3 - 4 GB (condiviso tra tutti i processi, mappato sempre allo stesso indirizzo fisico/virtuale).
*   **Problema:** Solo 1 GB per il Kernel.
    *   **Low Memory:** Memoria direttamente mappata (indirizzo virtuale = indirizzo fisico + offset costante). Usata per allocazioni contiguous (Buddy/Slab).
    *   **High Memory:** Memoria oltre il limite mappabile direttamente. Deve essere mappata dinamicamente tramite `vmalloc()` (non contigua fisicamente, ma contigua virtualmente). Complesso da gestire.

#### Intel 64-bit (x86-64)
*   **Spazio Indirizzamento:** Enorme (teoricamente 64-bit, praticamente 48-bit o 57-bit).
*   **Vantaggio:** Il Kernel ha terabyte di spazio virtuale.
*   **Mapping:**
    *   Ampia area per mapping diretto (Direct Map) della memoria fisica.
    *   Meno necessità di trucchi come l'High Memory.
    *   Separazione chiara tra aree per `kmalloc` (contigue), `vmalloc` (non contigue), e mapping dispositivi.

---

### 6. Considerazioni Finali e Ottimizzazioni

#### Pre-paging
Anticipare il caricamento di pagine non ancora richieste.
*   **Strategia:** Se viene richiesta la pagina $P$, carica anche $P+1, P+2...$ (assumendo località spaziale/seguenziale).
*   **Costo-Beneficio:**
    *   Utile se la percentuale di pagine precaricate effettivamente usate ($\alpha$) è alta.
    *   Spreco di I/O e RAM se $\alpha$ è bassa (pagine caricate inutilmente).
    *   Più efficace per codice sequenziale (text) che per dati heap casuali.

#### Dimensione delle Pagine (Page Size)
*   **Pagine Piccole (es. 4KB):**
    *   Pro: Minore frammentazione interna, migliore granularità per la località, più processi in RAM.
    *   Contro: Page Table grandi, più overhead di gestione TLB, più fault I/O (più trasferimenti piccoli).
*   **Pagine Grandi (Huge Pages, es. 2MB/1GB):**
    *   Pro: Page Table piccole, TLB Reach maggiore (copre più memoria con poche entry TLB), meno fault per grandi dataset sequenziali.
    *   Contro: Maggiore frammentazione interna, spreco di RAM se non usata tutta.
*   **TLB Reach:** Quantità di memoria indirizzabile dalla TLB senza miss. $Reach = \text{TLB Entries} \times \text{Page Size}$. Aumentare la page size aumenta il reach.

#### Tabella delle Pagine Invertita (IPT) - Problemi
1.  **Ricerca Lenta:** Non esiste accesso diretto indice->frame. Bisogna cercare `(PID, Page Number)` in tutta la tabella (hashing aiuta, ma collisioni possibili).
2.  **Gestione Page Fault:** Se la pagina non è in RAM, l'IPT non ha l'entry. Serve una struttura ausiliaria per sapere dove sta la pagina su disco.
3.  **Condivisione Memoria:** Difficile gestire pagine condivise tra processi, poiché ogni frame nell'IPT è associato a un singolo `(PID, Page)`.

#### I/O e Pagine Bloccate (Locked Pages)
*   I dispositivi I/O (DMA) scrivono direttamente in RAM.
*   Le pagine coinvolte in I/O devono essere **bloccate** (Lock Bit settato) nella RAM: non possono essere sostituite (swapped out) finché il trasferimento non è completo.
*   Previne la corruzione dei dati se il SO tentasse di spostare la pagina mentre il dispositivo sta scrivendo.

---

*Fine della lezione.*
