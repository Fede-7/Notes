# Trascrizione Lezione: Gestione della Memoria e Paging

**Data:** 22 aprile 2026
**Argomento:** Memoria Principale, Binding degli Indirizzi, Frammentazione e Paging.

---

### 1. Introduzione alla Gestione della Memoria

Abbiamo bisogno di gestire la memoria, quindi dobbiamo analizzare cosa succede in memoria quando vengono eseguiti i programmi. Questo aspetto è complementare all'esecuzione dei programmi stessi. Dobbiamo capire come viene gestita soprattutto la **memoria principale**, poiché è lì che le istruzioni devono essere eseguite e dove vengono stoccate le strutture dati.

Finora ne abbiamo parlato poco; ora vedremo una descrizione più dettagliata di come funziona la memoria, distinguendo tra:
*   **Memoria fisica** (reale).
*   **Memoria logica** (virtuale/logica vista dal processo).

Analizzeremo le tecniche di gestione, inclusi i modelli di **paging** (paginazione) e **segmentazione**.

#### Background: Accesso alla Memoria
Un sistema di elaborazione deve eseguire i programmi. Per essere eseguito, un programma deve essere portato in memoria principale. La memoria principale e i registri sono le uniche locazioni a cui la CPU ha accesso diretto.
*   La CPU lavora sui suoi registri o sulla memoria principale.
*   Ogni processo, per essere eseguito, deve essere almeno parzialmente caricato in memoria principale.
*   Più processi eseguiti contemporaneamente devono coesistere (parzialmente) in questa memoria.

**Ciclo di esecuzione ad alto livello:**
1.  La CPU carica le istruzioni indicate dal *Program Counter*.
2.  Le decodifica ed esegue.
3.  Eventualmente scrive qualcosa in memoria principale.
4.  Effettua chiamate per scrivere su memoria secondaria (se necessario).

A prima vista, possiamo vedere la memoria principale come un grande array di byte. Ogni byte ha un indirizzo unico che la CPU può indirizzare. Dall'altra parte, l'unità di memoria vede un flusso di indirizzi e richieste di lettura/scrittura.

#### Protezione e Accelerazione
La memoria deve essere **protetta**: ogni processo deve avere l'uso esclusivo delle proprie zone. Questa protezione è assicurata dal Sistema Operativo (SO) tramite supporti hardware che definiscono aree riservate.
Inoltre, l'accesso alla memoria deve essere **accelerato**. Poiché l'accesso alla RAM richiede molti cicli di CPU, esistono strutture di memoria più veloci (cache) intermedie per ottimizzare le procedure.

> **Domanda dagli studenti:** *Se ci sono programmi lato user che, con autorizzazione del superuser, agiscono lato kernel, possono intervenire nelle zone di memoria protette?*
>
> **Risposta:** Il kernel può fare tutto. Se sei un programmatore che modifica il kernel Linux (open source), puoi teoricamente accedere a tutto. Tuttavia, un processo utente standard non può violare le protezioni strutturali. Esiste la *Shared Memory* (memoria condivisa), ma è concessa esplicitamente dal kernel. Le violazioni non sono ammesse structuralmente. Queste protezioni si basano su bit fisici (hardware) che switching tra modalità kernel/user e registri speciali per definire i limiti.

---

### 2. Il Problema del Binding degli Indirizzi

Per introdurre la differenza tra indirizzi logici e fisici, consideriamo un approccio semplificato (e ormai obsoleto) basato su indirizzi assoluti e rilocazione.

Immaginiamo due codici assembly con istruzioni di salto (`jump`). Se carichiamo questi codici a indirizzi base differenti, gli indirizzi interni (assoluti) nei salti potrebbero puntare fuori dalla zona assegnata al processo, invadendo la memoria di altri processi.
Questo evidenzia il problema del **Binding**: l'associazione degli indirizzi simbolici/logici agli indirizzi fisici reali.

Il binding può avvenire in tre momenti:
1.  **Tempo di Compilazione:** Se la posizione in memoria è nota a priori, si genera codice assoluto. (Raro e rigido).
2.  **Tempo di Caricamento:** Si genera codice rilocabile. Il *Loader* somma l'indirizzo base all'indirizzo relativo. (Usato in sistemi older).
3.  **Tempo di Esecuzione (Runtime):** È il metodo usato nei sistemi moderni. Gli indirizzi rimangono logici/virtuali fino al momento dell'accesso effettivo. Richiede supporto hardware speciale.

---

### 3. Indirizzi Logici vs Fisici e la MMU

Nei sistemi moderni c'è una netta separazione:
*   **Indirizzi Logici (Virtuali):** Generati dalla CPU. Quando usate i puntatori in C, state lavorando su indirizzi logici. Il processo ha l'illusione di avere uno spazio di indirizzamento contiguo che parte da 0.
*   **Indirizzi Fisici:** Gli indirizzi reali della RAM dove risiedono effettivamente dati e istruzioni.

La traduzione da logico a fisico avviene tramite la **MMU (Memory Management Unit)**, un modulo hardware (spesso integrato nella CPU).
*   La CPU genera un indirizzo logico.
*   La MMU lo traduce in un indirizzo fisico.
*   Il processo utente vede solo indirizzi logici; la traduzione è trasparente e veloce.

> **Nota sulla contiguità:** Gli array sono contigui negli indirizzi logici. Fisicamente, grazie al paging, potrebbero non esserlo (se sparsi su frame diversi), ma si cerca di mantenere la località per performance.

---

### 4. Allocazione Contigua e Frammentazione

Prima del paging, si usava l'allocazione contigua. La memoria era vista come un unico blocco suddiviso tra processi.
*   Il SO doveva tenere traccia dei "buchi" liberi.
*   Strategie di allocazione: *First Fit* (primo buco sufficiente), *Best Fit* (buco più aderente), *Worst Fit* (buco più grande).

**Problema: Frammentazione Esterna**
Dopo molte allocazioni e deallocazioni, la memoria si frammenta. Si creano piccoli buchi sparsi troppo piccoli per essere utilizzati, anche se la somma totale della memoria libera è sufficiente.
*   Empiricamente, con *First Fit*, circa il **50%** della memoria allocata può andare persa per frammentazione esterna a regime.
*   Soluzione teorica: **Compattazione** (spostare i processi in memoria per unire i buchi liberi). Tuttavia, la compattazione a runtime è proibitiva perché richiede di stoppare i processi e aggiornare tutti gli indirizzi (rilocazione dinamica costosa).

**Frammentazione Interna**
Si verifica quando la memoria allocata a un processo è leggermente superiore a quella richiesta (es. l'ultimo blocco non è pieno). Lo spazio inutilizzato *all'interno* del blocco allocato è frammentazione interna.

---

### 5. La Paginazione (Paging)

Per risolvere la frammentazione esterna, si introduce il **Paging**.
*   La memoria fisica è divisa in blocchi fissi di dimensione uguale, chiamati **Frame** (potenze di 2: 4KB, 2MB, etc.).
*   La memoria logica è divisa in blocchi della stessa dimensione, chiamati **Pagine**.

**Vantaggi:**
*   Non serve più contiguità fisica. Una pagina logica può essere messa in qualsiasi frame fisico libero.
*   **Elimina la frammentazione esterna.** Tutti i frame sono utilizzabili.
*   Rimane solo la **frammentazione interna** (massimo un frame meno 1 byte per processo). In media, si spreca mezzo frame per processo.

**Trade-off sulla dimensione delle pagine:**
*   **Pagine piccole:** Minore frammentazione interna, ma Page Table molto grande (più overhead di memoria e gestione).
*   **Pagine grandi (Huge Pages):** Page Table più piccola e traduzione più veloce (meno accessi alla tabella), ma maggiore frammentazione interna.
    *   *Linux* supporta Huge Pages (es. 2MB o 1GB) per applicazioni dedicate ad alte prestazioni, riducendo il carico sulla TLB (Translation Lookaside Buffer).

---

### 6. Traduzione degli Indirizzi nel Paging

L'indirizzo logico è suddiviso in due parti:
1.  **Numero di Pagina (p):** Indice nella Page Table.
2.  **Offset (d):** Spostamento all'interno della pagina/frame.

**Meccanismo:**
1.  La CPU genera l'indirizzo logico `<p, d>`.
2.  La MMU usa `p` come indice nella **Page Table** del processo.
3.  La Page Table restituisce il numero del **Frame (f)** corrispondente.
4.  L'indirizzo fisico diventa `<f, d>`. L'offset rimane invariato perché la dimensione della pagina e del frame è identica.

> **Esempio di calcolo bit:**
> Se lo spazio di indirizzamento logico è $2^m$ byte e la pagina è $2^n$ byte:
> *   Bit per l'offset = $n$.
> *   Bit per il numero di pagina = $m - n$.
>
> *Caso pratico:* Spazio logico 1 GB ($2^{30}$ byte), Pagine 4 KB ($2^{12}$ byte).
> *   Offset: 12 bit.
> *   Numero di pagina: $30 - 12 = 18$ bit.
> *   Numero di pagine totali: $2^{18}$.

La Page Table è una struttura dati in memoria (spesso cacheata nella TLB per velocità). L'accesso alla Page Table è ad accesso random (costante O(1)) se si usa una tabella diretta. Esistono anche *Inverse Page Tables* (scansione lineare, più lente ma risparmiano memoria per spazi di indirizzamento enormi).

---

### 7. Esercizi Pratici

#### Esercizio 1
**Dati:** Spazio di indirizzi logici a 14 bit. Pagine di 2 KB.
**Domanda:** Quante entry avrà la tabella delle pagine?

**Soluzione:**
*   Spazio logico totale: $2^{14}$ byte.
*   Dimensione pagina: 2 KB = $2^{11}$ byte.
*   Numero di pagine = $\frac{2^{14}}{2^{11}} = 2^{14-11} = 2^3 = 8$.
*   **Risposta:** La tabella delle pagine avrà **8 entry**.

#### Esercizio 2
**Dati:** Spazio di indirizzi logici a 15 bit. Il sistema ha 8 pagine.
**Domanda:** Quanto sono grandi le pagine?

**Soluzione:**
*   Spazio logico totale: $2^{15}$ byte.
*   Numero di pagine: $8 = 2^3$.
*   Dimensione pagina = $\frac{\text{Spazio Totale}}{\text{Num Pagine}} = \frac{2^{15}}{2^3} = 2^{15-3} = 2^{12}$ byte.
*   $2^{12}$ byte = 4096 byte = **4 KB**.
*   **Risposta:** Le pagine sono grandi **4 KB**.

#### Esercizio 3
**Dati:** Frame di 4 MB. Memoria fisica indirizzabile di 128 GB.
**Domanda:** Calcolare il numero minimo di bit per indicizzare tutte le pagine (frame) associate.

**Soluzione:**
Dobbiamo trovare quanti frame ci sono nella memoria fisica.
1.  Convertiamo tutto in potenze di 2.
    *   Dimensione Frame: 4 MB = $2^2 \times 2^{20} = 2^{22}$ byte.
    *   Memoria Fisica: 128 GB = $2^7 \times 2^{30} = 2^{37}$ byte.
2.  Calcoliamo il numero di frame:
    *   $\text{Num Frame} = \frac{2^{37}}{2^{22}} = 2^{37-22} = 2^{15}$.
3.  Per indicizzare $2^{15}$ elementi, servono **15 bit**.

**Risposta:** Servono **15 bit**.

---

*Fine della lezione.*
