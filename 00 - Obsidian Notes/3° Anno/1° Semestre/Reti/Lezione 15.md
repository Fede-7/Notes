# Lezione 15 Transport Layer TCP

## TCP rispetto a UDP

> [!def] TCP
> **Transmission Control Protocol**: protocollo di trasporto **orientato alla connessione**, **affidabile** e **consapevole di congestione e flusso**.

- **Orientato alla connessione**: prima della trasmissione c'è una fase di **handshake** che assicura che i processi mittente e ricevente siano "connessi".
- **Affidabile**: implementa rilevamento errori, ritrasmissioni, acknowledgment, timer e numeri di sequenza.
- **Consapevole di congestione e flusso**: regola il ritmo di trasmissione in base alle prestazioni del ricevente (flusso) e della rete (congestione).

L'orientamento alla connessione rende TCP **full-duplex** e **point-to-point**:

- **Full-duplex**: se A è connesso con B, allora B è connesso con A.
- **Point-to-point**: un solo mittente e un solo destinatario; non è possibile trasmettere da un mittente a più destinatari (UDP invece permette il multicasting).

TCP è orientato allo scambio di **flussi di dati** (*data stream*): più segmenti TCP possono essere parti di un flusso più grande (sequenza ordinata di dati), mentre i singoli datagram UDP sono per lo più scollegati.

## Buffer e Maximum Segment Size

Le operazioni di invio e ricezione in TCP si basano fortemente su **buffer**, che disaccoppiano parzialmente i tempi di trasmissione da:
>[!aside]
> - Ritardi dell'applicazione.
> - Ritardi del SO nel multiplexing/demultiplexing dei pacchetti.
> - Ritardi di rete (oscillazioni delle prestazioni).
> 
> Esiste anche il limite del ritmo di trasmissione: messaggi lunghi possono essere spezzati in segmenti più piccoli, raccolti nei buffer prima di essere **disassemblati** (lato mittente) e **riassemblati** (lato ricevente).
> 
> ---
> ![[Lezione 15-1793789021613.webp | 150]]
> 

> [!def] MSS
> **Maximum Segment Size**: quantità massima di dati dentro un segmento, legata all'**MTU** (*Maximum Transmission Unit*, lunghezza massima del frame accettabile dal livello link, es. 1500 byte in Ethernet) dalla relazione $\mathrm{MSS} + 40 = \mathrm{MTU}$, dove 40 byte sono le dimensioni combinate delle header TCP e IP (tipicamente 20+20).

- All'invio i segmenti sono creati dai dati applicativi e passati al livello rete, dove sono incapsulati separatamente in datagram IP.
- Alla ricezione i dati sono messi nel **receive buffer**, da cui l'applicazione legge quando è pronta.

## Il segmento TCP

Il segmento TCP consiste di campi di header e di un campo dati (al massimo di MSS byte). Campi principali:

> [!aside]
> - **Sequence number** (32 bit): per il trasferimento affidabile.
> - **Acknowledgment number** (32 bit): per il trasferimento affidabile.
> - **Receive window** (16 bit): numero di byte che il ricevente è disposto ad accettare (controllo di flusso).
> - **Header length** (4 bit): numero di parole da 32 bit nella header; la header TCP è **variabile** per via del campo opzioni.
> - **Options** (K bit): processi opzionali, come la negoziazione dell'MSS o i timestamp.
> - **Flags** (6/12 bit):
>   - **ACK**: il segmento è un ACK (il campo acknowledgment number è in uso).
>   - **RST**, **SYN**, **FIN**: apertura e chiusura della connessione.
>   - **CWR**, **ECE**: notifica esplicita di congestione (opzionale).
>   - **PSH**: dice al ricevente di passare subito i dati all'applicazione (raro).
>   - **URG**: il segmento contiene dati "urgenti" (raro), con l'**Urgent data pointer** (16 bit) che indica la posizione dell'ultimo byte urgente.
> - **Checksum** (16 bit): controllo di integrità.
> 
> ---
> ![[Lezione 15-1793788979675.webp|200]]


## Numeri di sequenza e acknowledgment

I numeri di sequenza servono anche a gestire la **segmentazione**: un grande flusso di dati va spezzato in "pezzi" di dimensione dipendente dall'MSS, e ogni pezzo entra in un segmento.

- Il **numero di sequenza** di un segmento è convenzionalmente la **posizione che il primo byte del suo dato occupa nel flusso**.
- Il **numero di acknowledgment** è convenzionalmente il **prossimo pezzo del flusso atteso** (calcolato dal numero di sequenza del segmento precedente).
- TCP non sa nulla dei dati trasmessi: dal suo punto di vista i dati sono solo un **flusso ordinato di byte** (è un protocollo di trasporto general-purpose).

![[Lezione 15-1793789101717.webp|300]]

> [!example] 
> Per un flusso da 500.000 byte (~500 KB) con MSS di 1000 byte, TCP costruisce 500 segmenti: il primo ha numero di sequenza 0, il secondo 1000, il terzo 2000, e così via.
> 

Trasferimento A $\to$ B (partendo dal numero di sequenza 0):

- Il ricevente riceve il primo segmento da 1000 byte (byte 0–999) e conferma con **acknowledgment number 1000** (prossimo byte atteso nel flusso).
- Poi riceve il segmento 1000–1999, e così via.

**Full-duplex**: se A e B comunicano, esistono **due flussi** da considerare per l'affidabilità (A$\to$B e B$\to$A), e i numeri si usano in coppia:

- I segmenti di A hanno numeri di sequenza relativi al flusso A$\to$B e acknowledgment relativi al flusso B$\to$A.
- I segmenti di B hanno numeri di sequenza relativi al flusso B$\to$A e acknowledgment relativi al flusso A$\to$B.

> [!aside]
> 
> > [!example] Echo di un byte: 
> > **A** trasmette il carattere `c` (byte 42 del proprio flusso) con acknowledgment 79 (prossimo atteso dal flusso B$\to$A); 
> > **B** risponde echoando `c` con numero di sequenza 79 e acknowledgment 43 (42 + 1); 
> > **A** invia infine un **pure ACK** con sequenza 43 e acknowledgment 80. 
> > 
> > I segmenti che portano dati e ACK insieme hanno il flag `ACK = 1`.
> 
> ---
> 
> ![[Lezione 15-1793789569416.webp|150]]
> 

## Stima dell'RTT e timeout di ritrasmissione

Il meccanismo di affidabilità di TCP fa largo uso di **timeout**: nell'approccio a pipelining si ritrasmette un segmento solo se l'ACK relativo non arriva prima della scadenza.

- La stima del timeout è **critica**: un timeout troppo lungo rallenta la comunicazione, uno troppo corto fa sovrapporre i pacchetti (e ritrasmette pacchetti inutili, generando traffico inutile).
- Il timeout deve essere **maggiore dell'RTT**, altrimenti si generano ritrasmissioni non necessarie.

TCP stima l'RTT **campionando** i segmenti confermati con successo e **non ritrasmessi** (one-shot). Il tempo campionato (*SampleRTT*) oscilla (congestione, carico del ricevente), quindi la stima è una **media mobile esponenziale** (EWMA):

$$\text{EstimatedRTT} = (1-\alpha)\,\text{EstimatedRTT} + \alpha\,\text{SampleRTT}$$

con $\alpha = 0.125$ (cioè 1/8). 

> [!aside]
> Anche la **variabilità** dell'RTT entra nel calcolo:
> 
> $$\text{DevRTT} = (1-\beta)\,\text{DevRTT} + \beta\,|\text{SampleRTT} - \text{EstimatedRTT}|$$
> con $\beta = 0.25$ (cioè 1/4). 
> 
> ---
> 
> ![[Lezione 15-1793790241001.webp|200]]


 L'**intervallo di timeout** è:

$$\text{TimeoutInterval} = \text{EstimatedRTT} + 4 \cdot \text{DevRTT}$$

La deviazione fornisce un margine **ragionevole e adattivo** rispetto all'RTT stimato, esso cresce quando l'RTT oscilla, quindi la finestra di timeout è più larga quando si è incerti.
Il valore iniziale di default dell'RTT a $t = 0$: **1 secondo**.

## Fast retransmit

La ritrasmissione a timeout è efficace, ma ha un limite fondamentale che ha motivato l'introduzione di un meccanismo di segnalazione più rapido.

- Il periodo di timeout è **relativamente lungo**: in attesa della scadenza, la connessione resta **stallata**.
- **Fast retransmit**: è il **ricevente** a segnalare al mittente una probabile perdita, senza aspettare il timeout, tramite **ACK duplicati**.

### Come funziona

Il meccanismo si svolge in tre passi.

1. Il ricevente TCP riceve un segmento con numero di sequenza **maggiore di quello atteso** → un segmento intermedio è presumibilmente andato perso.
2. Il ricevente **reinvia lo stesso ACK di prima** (duplicato), che riporta il numero del **prossimo byte atteso**.
3. Quando il mittente riceve **N ACK duplicati** (tipicamente **3**, soglia definita in RFC 5681), assume che il segmento successivo all'ultimo ACK non duplicato sia perso e lo **ritrasmette subito**, ben prima della scadenza del timeout.

> [!aside]
> 
> > [!warning] Perché aspettare 3 duplicati
> > Gli ACK duplicati possono nascere anche **senza perdite**: se due segmenti arrivano **scambiati di ordine** (riordino nella rete), il ricevente emette 1 ACK duplicato prima di accorgersi dello scambio. Reagire al **primo** duplicato causerebbe ritrasmissioni inutili o sbagliate. La soglia di 3 fa da **filtro** contro il riordino occasionale.
> 
> ---
> 
> ![[Lezione 15-1793791268998.webp|150]]

### Dopo la ritrasmissione

Completata la ritrasmissione, la ripresa della trasmissione dipende dalla politica di ritrasmissione adottata.

- All'arrivo del segmento ritrasmesso, il ricevente invia l'ACK del **prossimo segmento atteso**, secondo la propria politica (go-back-N o selective repeat).

### TCP: Go-Back-N o selective repeat?

A prima vista TCP assomiglia a entrambi, ma il confronto va fatto punto per punto.

- **Come Go-Back-N**: ACK **cumulativi**, nessuna risposta individuale per ciò che arriva in anticipo, **un solo timer** e due variabili.
- **A differenza di Go-Back-N**: al timeout si ritrasmette **un solo segmento**, non tutto ciò che è in attesa — e nemmeno quello, se l'ACK successivo lo copre già.
- **Come selective repeat**: il ricevente **buffera** ciò che arriva in anticipo invece di scartarlo.
- **Conclusione**: TCP non è né l'uno né l'altro — ACK cumulativi su un ricevente che **conserva** i dati, cioè **la metà utile di ciascuno**.

> [!tip] Selective Acknowledgement (SACK)
> Un'opzione, il **selective acknowledgement**, permette al ricevente di **nominare i blocchi** che sta trattenendo — e porta TCP **fino in fondo** verso il selective repeat.
