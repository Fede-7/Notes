# Trascrizione Lezione: Gestione Avanzata della Memoria (Paging, TLB, Strutture delle Page Table)

**Data:** 23 aprile 2026
**Argomento:** Allocazione dei Frame, TLB, Calcolo dell'Effective Access Time, Protezione, Memoria Virtuale, Strutture Gerarchiche e Hashed Page Tables, Swapping.

---

### 1. Allocazione dei Frame e Page Table

Quando un processo viene lanciato, inizia ad allocare le sue pagine. Poiché non tutte le pagine possono risiedere contemporaneamente in RAM (o non sono tutte utilizzate immediatamente), il sistema deve gestire l'allocazione dinamica sui **frame** della memoria fisica.

*   **Lista dei Frame Liberi:** Il Sistema Operativo mantiene una lista dei frame liberi in RAM. Quando un processo richiede memoria, le sue pagine vengono mappate su questi frame disponibili.
*   **Esempio di Allocazione:**
    *   Un processo ha bisogno delle pagine 0, 1, 2, 3.
    *   La Page Table del processo viene popolata mappando:
        *   Pagina 0 → Frame 14
        *   Pagina 1 → Frame 13
        *   Pagina 2 → Frame 18
        *   Pagina 3 → Frame 20
    *   I frame occupati vengono segnati come tali nella tabella globale dei frame del sistema.

Ogni processo possiede la propria **Page Table**. Nel **Process Control Block (PCB)** esiste un registro (Page Table Base Register) che punta all'inizio della tabella delle pagine del processo, insieme a un registro di lunghezza (*length register*) che ne definisce la dimensione. Questi registri vengono caricati dal dispatcher ogni volta che si effettua un context switch.

> **Nota sulle Performance:** Se la Page Table risiede in memoria principale (come accade generalmente, dato che può essere molto grande), ogni accesso a un dato richiede due accessi in memoria:
> 1.  Accesso alla Page Table per risolvere l'indirizzo logico in fisico.
> 2.  Accesso effettivo al dato in memoria fisica.
> Questo raddoppia il tempo di accesso, rendendo cruciali i meccanismi di caching.

---

### 2. Translation Lookaside Buffer (TLB)

Per accelerare la traduzione degli indirizzi, si utilizza la **TLB**, una cache hardware associativa ad alta velocità integrata nella MMU.

#### Funzionamento
1.  La CPU genera un indirizzo logico (Numero di Pagina + Offset).
2.  La MMU cerca prima nella **TLB**:
    *   **TLB Hit:** La traduzione (Numero di Frame) è trovata nella cache. L'indirizzo fisico viene costruito immediatamente aggiungendo l'offset. Tempo di accesso: molto breve ($\epsilon$).
    *   **TLB Miss:** La traduzione non è presente. La MMU deve accedere alla Page Table in memoria principale per recuperare il numero di frame. Una volta trovato, aggiorna la TLB con questa nuova entry per accessi futuri.

#### Principio di Località
L'efficacia della TLB si basa sul **principio di località**: se un processo accede a una pagina, è probabile che vi acceda nuovamente a breve (località temporale) o che acceda a pagine vicine (località spaziale). Pertanto, mantenere le traduzioni recenti in cache riduce drasticamente gli accessi lentissimi alla RAM.

#### Politiche di Rimpiazzo
La TLB ha dimensioni finite. Quando è piena e si verifica un miss, bisogna sostituire una entry esistente. Strategie comuni:
*   **LRU (Least Recently Used):** Si sostituisce l'entry non utilizzata da più tempo.
*   **Random:** Sostituzione casuale (più veloce da implementare hardware-wise).
*   **Round-Robin:** Scorrimento circolare delle entry.

Alcune entry possono essere "cablate" (fisse), ad esempio per il codice del kernel, per garantire accessi sempre rapidi alle risorse critiche. Inoltre, moderne TLB supportano gli **ASID (Address Space Identifiers)**, permettendo di distinguere le traduzioni di processi diversi senza svuotare la TLB ad ogni context switch.

---

### 3. Calcolo dell'Effective Access Time (EAT)

L'EAT è il tempo medio necessario per accedere a un dato in memoria, considerando hit e miss della TLB.

**Formula Generale:**
$$ EAT = \alpha \cdot (\epsilon + T_M) + (1 - \alpha) \cdot (\epsilon + 2T_M) $$

Dove:
*   $\alpha$ (alfa): Probabilità di Hit nella TLB (es. 0.90 o 90%).
*   $\epsilon$ (epsilon): Tempo di accesso alla TLB.
*   $T_M$: Tempo di accesso alla memoria principale.
*   $(1 - \alpha)$: Probabilità di Miss.

**Spiegazione dei termini:**
*   **Caso Hit:** Tempo TLB ($\epsilon$) + Accesso dato ($T_M$).
*   **Caso Miss:** Tempo TLB ($\epsilon$) + Accesso Page Table ($T_M$) + Accesso dato ($T_M$). Totale: $\epsilon + 2T_M$.

#### Esempio Pratico 1
*   Hit Rate ($\alpha$): 80% (0.8)
*   Tempo TLB ($\epsilon$): 20 ns
*   Tempo Memoria ($T_M$): 100 ns

$$ EAT = 0.8 \cdot (20 + 100) + 0.2 \cdot (20 + 200) $$
$$ EAT = 0.8 \cdot 120 + 0.2 \cdot 220 $$
$$ EAT = 96 + 44 = 140 \text{ ns} $$

*Senza TLB, il tempo sarebbe stato $2 \cdot 100 = 200$ ns. Il guadagno è significativo.*

#### Esempio Pratico 2 (Hit Rate Realistico)
Nei sistemi moderni, l'hit rate è spesso >99%.
*   Hit Rate ($\alpha$): 99% (0.99)
*   Tempo TLB ($\epsilon$): 20 ns
*   Tempo Memoria ($T_M$): 100 ns

$$ EAT = 0.99 \cdot (120) + 0.01 \cdot (220) = 118.8 + 2.2 = 121 \text{ ns} $$

Si nota che con un hit rate elevato, l'EAT si avvicina molto al tempo di accesso ideale ($\epsilon + T_M$).

#### Esercizio Proposto
*   Hit Rate: 90%
*   Tempo Memoria: 200 ns
*   Tempo TLB: Trascurabile ($\approx 0$)

$$ EAT = 0.9 \cdot (0 + 200) + 0.1 \cdot (0 + 400) $$
$$ EAT = 180 + 40 = 220 \text{ ns} $$

---

### 4. Protezione e Bit di Stato nella Page Table

Oltre al mapping Pagina-Frame, ogni entry della Page Table contiene bit di controllo per la protezione e la gestione della memoria virtuale.

1.  **Valid/Invalid Bit:** Indica se l'accesso a quella pagina logica è legale.
    *   Spesso la **Pagina 0** è marcata come *Invalid* per catturare errori di dereferenziazione di puntatori NULL.
2.  **Present/Absent Bit:** Indica se la pagina è attualmente caricata in un frame fisico (RAM) o se risiede nel backing store (memoria secondaria).
    *   Se *Absent*, l'accesso genera un **Page Fault**, interrompendo la CPU per permettere al SO di caricare la pagina dalla disk alla RAM.
3.  **Read/Write/Execute Permissions:** Definiscono i permessi di accesso (es. sola esecuzione per il codice, sola lettura per dati costanti).
4.  **Dirty Bit (Modified Bit):** Segnala se la pagina è stata modificata dopo essere stata caricata in RAM.
    *   Se *Dirty=0*: La pagina in RAM è identica a quella su disco. Può essere sovrascritta senza scrivere su disco (risparmio di I/O).
    *   Se *Dirty=1*: La pagina deve essere scritta su disco (*page out*) prima di essere sostituita.
5.  **Reference Bit (Accessed Bit):** Segnala se la pagina è stata letta o scritta recentemente. Utile per algoritmi di rimpiazzo (es. LRU) per identificare le pagine "vive" vs quelle "morte".
6.  **Cache Disable Bit:** Impedisce che la pagina venga cachata (utile per memory-mapped I/O dove i dati cambiano esternamente e la cache fornirebbe valori obsoleti).

---

### 5. Condivisione della Memoria (Shared Memory)

Il paging permette la condivisione efficiente di codice e dati tra processi.
*   **Codice Condiviso (Read-Only):** Più processi possono mappare le stesse pagine fisiche (frame) contenenti librerie o eseguibili comuni (es. un editor di testo). Nelle rispettive Page Table, le entry puntano agli stessi frame fisici.
*   **Dati Privati:** Ogni processo ha i propri frame per i dati modificabili (stack, heap).

Questo riduce drasticamente l'uso di memoria rispetto alla duplicazione del codice per ogni processo.

---

### 6. Strutture delle Page Table per Spazi di Indirizzamento Grandi

Con architetture a 32 o 64 bit, una Page Table lineare (monolitica) diventerebbe enormemente grande.
*   **Esempio 32-bit:** Con pagine da 4KB ($2^{12}$), lo spazio di 4GB ($2^{32}$) richiede $2^{20}$ entry. Se ogni entry è 4 byte, la tabella occupa **4 MB** per *ogni processo*.
*   **Esempio 64-bit:** Lo spazio è astronomico ($2^{64}$ byte). Una tabella lineare è impossibile da gestire in memoria contigua.

Soluzioni adottate:

#### A. Page Table Gerarchica (Multi-Level)
La Page Table viene suddivisa in livelli. L'indirizzo logico viene partizionato in più indici (es. P1, P2) e un offset.
*   **Livello Esterno (Outer):** Punta a una tabella di secondo livello.
*   **Livello Interno:** Contiene il mapping finale Pagina-Frame.
*   **Vantaggio:** Non è necessario allocare in memoria tutta la struttura gerarchica, ma solo le parti effettivamente usate dal processo.
*   **Svantaggio:** Aumenta il numero di accessi in memoria per la traduzione (uno per livello), peggiorando le performance se non mitigato dalla TLB.

#### B. Hashed Page Table
Utilizza una funzione hash sul numero di pagina virtuale per indicizzare una tabella hash di dimensioni fisse.
*   Gestisce le collisioni tramite liste concatenate (bucket).
*   **Vantaggio:** Dimensione della tabella indipendente dalla dimensione dello spazio di indirizzamento virtuale.
*   **Svantaggio:** Overhead computazionale per la risoluzione delle collisioni e complessità di gestione.
*   Utilizzata in architetture come SPARC Solaris per spazi a 64-bit. Spesso combinata con **Clustered Page Tables** (una entry mappa un gruppo di pagine contigue).

#### C. Inverted Page Table (IPT)
Invece di una tabella per processo, esiste **una sola tabella globale** per tutta la memoria fisica.
*   La tabella ha tante entry quanti sono i **frame fisici**.
*   Ogni entry contiene: `(PID, Numero Pagina Virtuale, Dati di Protezione)`.
*   **Ricerca:** Per tradurre un indirizzo, bisogna cercare nella IPT la coppia `(PID, Pagina)`. Questa ricerca è lineare (lenta) se non ottimizzata con hash.
*   **Vantaggio:** Risparmio enorme di memoria (la tabella dipende dalla RAM fisica, non dalla memoria virtuale teorica).
*   **Svantaggio:** Difficile gestire la memoria condivisa (un frame appartiene logicamente a un solo entry nella IPT standard) e la ricerca è più lenta rispetto all'indicizzazione diretta.

---

### 7. Swapping e Paging

Storicamente, lo **Swapping** prevedeva lo spostamento intero di un processo dalla RAM al disco (backing store) e viceversa (*Swap-in/Swap-out*).
*   **Problema:** Tempi di trasferimento elevati (es. secondi per processi grandi), rendendo il context switch proibitivo.

Nei sistemi moderni si usa il **Demand Paging** (Page-in/Page-out):
*   Si spostano solo singole pagine tra RAM e disco quando necessario.
*   Il **Dirty Bit** è cruciale: se una pagina non è stata modificata (*Clean*), non viene scritta su disco durante il replacement, poiché esiste già una copia valida nel backing store. Questo risparmia operazioni di I/O lente.

> **Nota sui Sistemi Mobile (Flash Memory):**
> Nelle memorie Flash, le scritture hanno un ciclo di vita limitato (wear leveling). Per evitare di deteriorare la memoria con frequenti page-out, i sistemi mobile spesso preferiscono tecniche alternative, come la compressione delle pagine in RAM (zipping/unzipping), invece di scriverle su storage flash.

---

### 8. Segmentazione (Cenno)

La segmentazione è un modello alternativo o complementare al paging.
*   Divide la memoria in segmenti logici (Codice, Dati, Stack) di dimensione variabile.
*   L'indirizzo logico è composto da `(Numero Segmento, Offset)`.
*   La **Segment Table** contiene Base e Limite per ogni segmento.
*   **Architetture Ibride:** Alcuni sistemi (es. Multics, o Intel x86 in modalità protetta a 32-bit) combinano segmentazione e paging. L'indirizzo logico passa prima attraverso l'unità di segmentazione (producendo un indirizzo lineare), che viene poi paginato per ottenere l'indirizzo fisico.

Nelle prossime lezioni analizzeremo nel dettaglio l'implementazione concreta del binding a 64-bit su architetture moderne.
