# Lezione 12: Il livello di trasporto — TCP

## TCP rispetto a UDP

Rispetto a UDP, TCP è **orientato alla connessione** (c'è una fase di "handshake" prima della trasmissione, che garantisce che i due processi siano "connessi"), **affidabile** (implementa rilevamento degli errori, ritrasmissioni, acknowledgment, timer e numeri di sequenza) e **sensibile a congestione e flusso** (c'è una regolazione della velocità di trasmissione in base alle prestazioni del ricevente — flusso — e della rete — congestione).

L'orientamento alla connessione rende TCP **full-duplex** (se A è connesso con B, allora B è connesso con A) e **punto-a-punto**: un solo mittente e un solo ricevente, quindi il trasferimento da un mittente a più riceventi non è possibile (UDP invece permette il multicasting). TCP è inoltre orientato all'invio/ricezione di **flussi di dati** (*data stream*): più segmenti TCP possono far parte di un flusso più grande (sequenza ordinata di dati), mentre i singoli datagram UDP sono considerati per lo più disaccoppiati.

## Buffer TCP

Nella connessione TCP, invio e ricezione si basano fortemente sui **buffer**. I buffer permettono di **disaccoppiare parzialmente** i tempi di trasmissione dai **ritardi applicativi**, dai **ritardi del SO** nella multiplazione/demultiplazione dei pacchetti e dai **ritardi di rete** (oscillazioni delle prestazioni). C'è anche il limite della velocità di trasmissione: messaggi lunghi possono **essere spezzati in segmenti più piccoli**, raccolti nei buffer prima di essere disassemblati (lato mittente) o riassemblati (lato ricevente).

## Maximum Segment Size (MSS)

La quantità di **dati dentro un segmento** è limitata dalla **Maximum Segment Size (MSS)**:

$$MSS + 40 = MTU$$

dove la **Maximum Transmission Unit (MTU)** è la lunghezza massima di un frame accettabile dal livello di collegamento (es. in Ethernet 1500 byte) e **40 byte** è la dimensione combinata degli header TCP e IP (tipicamente 20+20 byte). **In invio**, i segmenti sono creati dai dati applicativi e passati al livello di rete, dove sono incapsulati separatamente in datagram IP; **in ricezione**, i dati sono messi nel buffer di ricezione e l'applicazione preleva i dati quando è pronta.

## Il segmento TCP

Il segmento TCP consiste di **campi di header** e un **campo dati** (al più MSS byte). L'**header** contiene:

- **Numero di sequenza** (32 bit): per il trasferimento affidabile.
- **Numero di acknowledgment** (32 bit): per il trasferimento affidabile.
- **Finestra di ricezione** (16 bit): indica quanti byte il ricevente è disposto ad accettare (per il controllo di flusso).
- **Lunghezza dell'header** (4 bit): numero di parole da 32 bit nell'header; l'header TCP **è variabile a causa del campo opzioni**.
- **Campo opzioni** (K bit): processi opzionali come la negoziazione dell'MSS, il timestamping, ecc.
- **Flag** (6/12 bit):
  - **ACK**: il segmento è un pacchetto ACK (il campo acknowledgment è in uso).
  - **RST, SYN, FIN**: usati per instaurazione e chiusura della connessione.
  - **CWR, ECE**: usati nella notifica esplicita di congestione (opzionale).
  - **PSH**: dice al ricevente di passare subito i dati all'applicazione (raro).
  - **URG**: il segmento contiene dati "urgenti" (raro).
- **Checksum** (16 bit): controllo di integrità.
- **Puntatore ai dati urgenti** (16 bit): posizione dell'ultimo byte della parte urgente dei dati (raro).

## Numeri di sequenza e acknowledgment

I numeri di sequenza servono non solo per il trasferimento affidabile, **ma anche per gestire la segmentazione**: un flusso grande va **spezzato in "pezzi"** in base all'MSS, e ogni pezzo va in un segmento TCP. Sequenza e acknowledgment sono **strettamente collegati**: il **numero di sequenza** di un segmento è convenzionalmente **la posizione che il primo byte dei dati del segmento occupa nel flusso**, mentre il **numero di acknowledgment** è convenzionalmente **il prossimo pezzo del flusso atteso** (calcolato dal numero di sequenza del segmento precedente).

TCP è un protocollo general-purpose e non sa nulla dei dati trasmessi: dal punto di vista di TCP i dati sono **solo un flusso ordinato di byte**, quindi il numero di sequenza è il **numero, nel flusso di byte, del primo byte dei dati** del segmento.

### Esempio

Si consideri un flusso di dati di **500.000 byte** (~500 KB) con **MSS di 1.000 byte**: TCP costruisce **500 segmenti** — il primo con numero di sequenza 0, il secondo 1000, il terzo 2000, e così via. Quando il flusso è passato **dall'host A all'host B** (partendo dalla sequenza 0), il ricevente riceve il primo segmento di 1.000 byte, cioè **dalla sequenza 0 alla 999**, e conferma impostando **acknowledgment = 1.000** (prossimo byte atteso nel flusso); riceve poi il segmento successivo (sequenze 1.000–1.999), e così via.

### Dati in entrambe le direzioni

E se il ricevente a sua volta invia dati? TCP è **full-duplex**: se A e B comunicano ci sono **due flussi** da considerare, **A→B** e **B→A**, e si usano **sequenza e acknowledgment contemporaneamente**. I segmenti di A hanno numeri di **sequenza relativi al flusso A→B** e di **acknowledgment relativi al flusso B→A**; i segmenti di B hanno sequenza relativa al flusso **B→A** e acknowledgment relativo al flusso **A→B**.

### Esempio semplificato (echo)

Si considerino due messaggi da **1 solo byte** (1 carattere) da A a B e viceversa: A trasmette una 'c' che B **rimanda indietro (echo)**, e i segmenti forniscono **ACK e DATA insieme** (flag ACK = 1).

1. **Da A a B**: ack number = seq del prossimo pacchetto atteso nel flusso B→A (byte 79); seq number = posizione dell'unico byte trasmesso (byte 42).
2. **Da B ad A**: ack number = seq del prossimo pacchetto atteso nel flusso A→B (cioè seq + 1 byte del carattere 'c'); seq number = posizione del byte trasmesso (byte 79).
3. **Da A a B**: segmento di **puro ACK**, con seq 43 (come atteso da B) e ack 80 (prossimo atteso).

## Retransmission Timeout

Il meccanismo di trasferimento affidabile di TCP **fa un uso massiccio dei timeout**. Nella trasmissione TCP basata su pipelining, l'approccio di default è **ritrasmettere i segmenti solo se gli ACK associati non arrivano prima del timeout**, quindi la **stima del timeout è critica**: un timeout troppo lungo rallenta la comunicazione, uno troppo corto fa sovrapporre i pacchetti (e pacchetti inutili vengono ritrasmessi, generando traffico inutile).

### Stima dell'RTT

Per impostare i timeout serve una **stima del round-trip time (RTT)**: il timeout dev'essere **maggiore dell'RTT**, altrimenti si invierebbero ritrasmissioni inutili. TCP stima l'RTT **campionando (SampleRTT) i segmenti confermati con successo e non ritrasmessi** (one-shot). Poiché il SampleRTT **può oscillare** (congestione, carico del ricevente, ecc.), la stima (EstimatedRTT) è una **media mobile esponenziale (EWMA)**:

$$\text{EstimatedRTT} = (1-\alpha)\cdot\text{EstimatedRTT} + \alpha\cdot\text{SampleRTT}$$

con $\alpha$ solitamente 0,125 (cioè 1/8). Si può considerare anche la **variabilità dell'RTT** (DevRTT), data dalla differenza tra campione e stima:

$$\text{DevRTT} = (1-\beta)\cdot\text{DevRTT} + \beta\cdot|\text{SampleRTT} - \text{EstimatedRTT}|$$

con $\beta$ solitamente 0,25 (cioè 1/4).

### Timeout di ritrasmissione

Con queste stime si definisce un timeout né troppo basso né troppo alto rispetto all'RTT stimato:

$$\text{TimeoutInterval} = \text{EstimatedRTT} + 4\cdot\text{DevRTT}$$

La deviazione dell'RTT dà un **margine ragionevole e adattivo**: cresce quando l'RTT oscilla, quindi la finestra di timeout è più larga **quando siamo incerti** sull'RTT corrente. Di default, il **valore iniziale** dell'RTT (a t=0) è 1 secondo.

## Fast Retransmit

La ritrasmissione su timeout è efficace, ma **il periodo di timeout può essere relativamente lungo**. Il **fast retransmit** è un approccio in cui il ricevente segnala al mittente che un pacchetto potrebbe essere perso inviando **ACK duplicati**: quando il ricevente riceve un segmento con **numero di sequenza maggiore di quello atteso**, ragionevolmente un segmento è andato perso, quindi **reinvia il vecchio ACK** (duplicato), con numero di acknowledgment pari a quello del segmento atteso. Se **il mittente riceve N duplicati** (tipicamente 3), assume che il segmento precedente sia perso e lo ritrasmette (fast) **ben prima della scadenza**.

### Esempio

Si consideri un segmento perso con sequenza 100: ogni volta che B riceve un segmento fuori ordine, **rimanda un ACK duplicato** (ack=100); quando A **riceve 3 duplicati**, assume perso il segmento 100 e **lo rispedisce** (fast retransmit); quando B riceve il segmento perso, **invia l'ACK del prossimo segmento atteso**, secondo la sua politica (go-back-N o selective repeat).

Perché non ritrasmettere al primo ACK duplicato? Perché **possiamo ricevere ACK duplicati per motivi vari**, non solo perdite: ad esempio, se **2 segmenti arrivano in ordine invertito** (scambiati in trasmissione), il ricevente invia **1 ACK duplicato** (per il primo segmento) prima di accorgersi dello scambio.