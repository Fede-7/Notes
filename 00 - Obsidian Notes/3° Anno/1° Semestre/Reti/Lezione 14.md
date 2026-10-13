# Lezione 14: TCP — controllo di flusso e di congestione

## Il problema della congestione e del controllo di flusso

Il controllo di congestione e di flusso sono funzionalità aggiuntive di TCP rispetto a UDP. La perdita di pacchetti è **spesso il risultato dell'overflow dei buffer**: dal buffer del ricevente, se l'**applicazione ricevente non è abbastanza veloce** a leggere i dati, o dai dispositivi di rete (es. router), se **i nodi sono congestionati**. Nell'analogia dell'acqua, **i buffer sono secchi intermedi** che traboccano se l'acqua eccede. Se i pacchetti si perdono, **gli host devono ricorrere a ritrasmissioni e timeout**, che danneggiano drasticamente le prestazioni della rete.

## Controllo di flusso

Quando la connessione TCP riceve byte corretti e in sequenza, li mette nel buffer di ricezione; l'applicazione **leggerà i dati da questo buffer, ma non necessariamente nell'istante in cui arrivano** (può essere occupata). Se l'applicazione è **lenta nel leggere**, il mittente può facilmente **far traboccare il buffer del ricevente** inviando troppi dati troppo in fretta. Il **controllo di flusso TCP è un servizio di adattamento della velocità**: cerca di far combaciare (ridurre) la velocità di invio del mittente con quella di lettura dell'applicazione ricevente, e per farlo si affida a una **finestra di ricezione** che informa il mittente di quanti segmenti possiamo ricevere senza overflow: il campo **receive window** del segmento TCP dice al mittente **quanto buffer libero** rimane.

### Meccanica

Per semplicità si assume che il ricevente **scarti i segmenti fuori ordine** (i segmenti nel buffer sono ordinati). Lato **ricevente** (host B) si considerano `RcvBuffer` (dimensione del buffer di ricezione, in byte), `LastByteRead` (ultimo byte del flusso letto dall'applicazione) e `LastByteRcvd` (ultimo byte del flusso ricevuto); la **finestra di ricezione** vale:

```
rwnd = RcvBuffer − (LastByteRcvd − LastByteRead)
```

Lato **mittente** (host A) si considerano l'ultimo byte del flusso inviato (`LastByteSent`) e l'ultimo byte confermato dal ricevente (`LastByteAcked`). Conoscendo la finestra di ricezione, **il mittente garantisce in ogni istante**:

```
LastByteSent − LastByteAcked ≤ rwnd
```

## Il problema della congestione

Il **controllo di congestione** è simile al controllo di flusso, ma riguarda l'infrastruttura di rete. Si considerino due host (A e B) con una connessione che **condivide un singolo router** e un singolo link in uscita di capacità **R** tra sorgente e destinazione; il **router ha buffer** per memorizzare i pacchetti in arrivo quando la velocità di arrivo supera la capacità del link in uscita. Si assuma che entrambe le applicazioni inviino dati a velocità media pari di $\lambda_{in}$ byte/s.

### Vista semplificata

Se $\lambda_{in} < R/2$, tutto ciò che è inviato arriva al destinatario **con un ritardo finito**; se $\lambda_{in} = R/2$, **il link raggiunge la piena capacità (R)** e i pacchetti in eccesso finiscono nel buffer. Oltre la capacità massima **i pacchetti si accumulano nel buffer del router** in attesa del proprio turno ma, poiché **il buffer è finito**, i pacchetti accumulati **prima o poi vengono scartati**, e gli host devono ritrasmetterli (generando ancora più traffico). Si noti che **un buffer infinito non risolve**: i pacchetti non si perderebbero, ma **il ritardo crescerebbe costantemente** — eccedendo per sempre la capacità, il ritardo tende all'infinito e i pacchetti sono come persi.

## Controllo di congestione

Esistono due approcci principali:

1. **Congestion control end-to-end** (approccio standard di TCP): la congestione è **dedotta dai sistemi finali** basandosi solo sul comportamento osservato della rete (perdita di pacchetti, ritardi); la perdita di segmenti (per timeout o per la ricezione di 3 ACK duplicati) è interpretata come segnale di congestione, e TCP riduce la velocità di invio.
2. **Congestion control assistito dalla rete** (approccio recente e opzionale): il trasporto lavora in sinergia col livello di rete, e **i router forniscono feedback espliciti** al mittente/ricevente sullo stato di congestione, usando i flag **CWR ed ECE**; il feedback può essere semplice come **un singolo bit che indica congestione** su un link, ma è possibile anche un feedback più sofisticato.

### Il controllo di congestione in TCP

TCP si basa sul controllo **end-to-end**: **ciascun mittente adatta la propria velocità di invio** alla **congestione percepita della rete**. I tre problemi principali sono la **regolazione della velocità** (come un mittente TCP regola la velocità con cui invia traffico nella connessione), il **rilevamento della congestione** (come un mittente TCP rileva la congestione sul cammino verso la destinazione) e l'**adeguamento della velocità** (quale algoritmo usare per cambiare la velocità in funzione della congestione end-to-end percepita).

### Regolazione della velocità

Nel controllo di flusso la velocità è regolata considerando **lo spazio libero nel buffer del ricevente** (finestra di ricezione `rwnd`), con `LastByteSent − LastByteAcked ≤ rwnd`. Nel controllo di congestione il mittente tiene traccia anche di una **finestra di congestione** (`cwnd`), e la velocità è regolata aumentando/diminuendo `cwnd`:

```
LastByteSent − LastByteAcked ≤ min{cwnd, rwnd}
```

### Rilevamento della congestione

Un mittente TCP percepisce la congestione controllando i **loss event** (eventi di perdita): un loss event avviene **quando scade un timeout o arrivano 3 ACK duplicati/errati**, e in entrambi i casi significa che un pacchetto precedente **non è arrivato a destinazione**, probabilmente per overflow dei dispositivi di rete. Se **non avvengono loss event** (gli ACK arrivano come attesi), TCP assume che la rete non sia congestionata e **la finestra di congestione può aumentare**; se **avvengono loss event**, **la finestra di congestione va diminuita**.

### Adeguamento della velocità

L'adeguamento avviene tramite **bandwidth probing**: la velocità cresce finché gli ACK arrivano correttamente (si "sonda" la rete), e rilevata la congestione (loss event) la velocità si riduce; il processo si ripete continuamente. TCP usa l'**algoritmo di congestione di Jacobson** [Jacobson 1988], con tre fasi:

1. **Slow start**: si parte da 1 MSS/RTT e la velocità cresce **esponenzialmente**.
2. **Additive Increase** (congestion avoidance): la velocità cresce **linearmente**.
3. **Fast Recovery** (opzionale): **dimezza** la velocità invece di ripartire in slow start, e prosegue con incrementi additivi.

Il comportamento tipico dell'algoritmo di Jacobson è **a "dente di sega"** (*sawtooth*).