# Lezione 14 Transport Layer controllo di flusso e congestione

## Il problema

Rispetto a UDP, TCP aggiunge il **controllo di flusso** e il **controllo di congestione**. La perdita di pacchetti è spesso il risultato di **overflow dei buffer**:

- Dal **buffer del ricevente**, se l'applicazione non abbastanza veloce nel leggere i dati.
- Dai **dispositivi di rete** (router), se i nodi sono congestionati.

Con l'analogia del flusso d'acqua, i buffer sono secchi intermedi che **traboccano** quando l'acqua eccede. Se i pacchetti si perdono, gli host devono ricorrere a ritrasmissioni e timeout, che **peggiorano drasticamente** le prestazioni della rete.

## Controllo di flusso

Quando la connessione TCP riceve byte corretti e in sequenza, li mette nel **receive buffer**; l'applicazione legge dal buffer, ma non necessariamente appena i dati arrivano (può essere occupata).

- Se l'applicazione è lenta nel leggere, il mittente può facilmente **far traboccare il buffer del ricevente** inviando troppi dati troppo in fretta.
- Il controllo di flusso TCP è un servizio di **speed-matching**: cerca di adeguare (ridurre) il ritmo del mittente al ritmo di lettura dell'applicazione ricevente.
- Il mezzo è la **receive window**, comunicata al mittente tramite l'omonimo campo del segmento TCP: quantifica lo **spazio libero nel buffer** del ricevente.

Assumendo che il ricevente scarti i segmenti out-of-order (buffer ordinato), sul lato **ricevente** (host B) si definiscono:

- **`RcvBuffer`**: dimensione del buffer di ricezione (byte).
- **`LastByteRead`**: ultimo byte del flusso letto dall'applicazione.
- **`LastByteRcvd`**: ultimo byte del flusso ricevuto.

La finestra di ricezione vale:

$$\text{rwnd} = \text{RcvBuffer} - (\text{LastByteRcvd} - \text{LastByteRead})$$

Sul lato **mittente** (host A) si tengono `LastByteSent` (ultimo byte inviato) e `LastByteAckd` (ultimo byte confermato); noto `rwnd`, il mittente garantisce in ogni istante:

$$\text{LastByteSent} - \text{LastByteAckd} \leq \text{rwnd}$$

## Il problema della congestione

Il controllo di congestione è simile a quello di flusso, ma riguarda l'**infrastruttura di rete**.

Caso modello: due host A e B con connessioni che attraversano lo stesso router e un unico link in uscita di capacità $R$ verso la destinazione; entrambe le applicazioni inviano dati a un ritmo medio $\lambda_{in}$ byte/s:

- Se $\lambda_{in} < R/2$, tutto ciò che è inviato arriva a destinazione con ritardo finito.
- Se $\lambda_{in} = R/2$, il link raggiunge la capacità piena $R$ e i pacchetti in eccesso si accumulano nel buffer del router.
- Superata la capacità massima, i pacchetti si **accumulano** nel buffer in attesa del proprio turno; il buffer è finito, quindi i pacchetti accumulati vengono prima o poi **scartati**, e gli host devono ritrasmetterli (ancora più traffico).
- Un **buffer infinito** non risolve: i pacchetti non si perdono ma il **ritardo cresce costantemente**, fino all'infinito, quindi i pacchetti sono persi comunque (per arrivo tardivo).

## Approcci al controllo di congestione

1. **End-to-end** (approccio standard di TCP): la congestione è dedotta **dai soli sistemi finali** a partire dal comportamento osservato della rete (perdita di pacchetti e ritardi); la perdita di segmenti (timeout o 3 ACK duplicati) è interpretata come **indicazione di congestione**, e TCP riduce il ritmo di invio di conseguenza.
2. **Network-assisted** (approccio recente e opzionale): il livello trasporto lavora in sinergia col livello rete; i **router** forniscono feedback esplicito al mittente e/o ricevente sullo stato di congestione, anche solo un bit di congestione per link; a questo scopo si usano i flag **CWR** ed **ECE**.

## Controllo di congestione TCP

TCP si affida per lo più al controllo end-to-end: ogni mittente adatta il proprio ritmo di invio alla congestione percepita. Tre problemi da considerare:

- **Regolazione del ritmo**: come regola un mittente TCP il ritmo con cui invia traffico nella connessione?
- **Rilevamento della congestione**: come rileva la congestione sul percorso verso la destinazione?
- **Aggiustamento del ritmo**: quale algoritmo usare per cambiare il ritmo in funzione della congestione percepita?

### Regolazione del ritmo

Nel controllo di flusso il ritmo è regolato dalla finestra del ricevente (`LastByteSend - LastByteAcked <= rwnd`). Nel controllo di congestione il mittente tiene anche una **congestion window** (`cwnd`):

$$\text{LastByteSent} - \text{LastByteAckd} \leq \min\{\text{cwnd}, \text{rwnd}\}$$

Il ritmo si regola quindi **aumentando/riducendo `cwnd`**.

### Rilevamento della congestione

Il mittente percepisce la congestione controllando i **loss event**, che si verificano quando:

- Scade un **timeout**, oppure
- arrivano **3 ACK duplicati**.

Entrambi indicano che un pacchetto precedente non è arrivato a destinazione, probabilmente per overflow di un dispositivo di rete. Se i loss event **non** si verificano (gli ACK arrivano come atteso), TCP assume che la rete non sia congestionata e la finestra di congestione **si aumenta**; se si verificano, `cwnd` **si diminuisce**.

### Aggiustamento del ritmo

L'aggiustamento avviene tramite **bandwidth probing**: il ritmo cresce finché gli ACK arrivano correttamente (la rete è "saggiata"), e si riduce quando si rileva congestione; il ciclo si ripete continuamente.

TCP usa l'algoritmo di congestione di **Jacobson** [Jacobson 1988], con tre fasi:

1. **Slow start**: si parte da 1 MSS/RTT e il ritmo cresce **esponenzialmente**.
2. **Additive increase** (o *congestion avoidance*): il ritmo cresce **linearmente**.
3. **Fast recovery** (opzionale): al loss event, invece di tornare allo slow start, il ritmo si **dimezza** e si prosegue con incrementi additivi.

Il comportamento tipico dell'algoritmo di Jacobson ha un andamento "a **dente di sega**": crescita del ritmo fino al loss event, dimezzamento e nuova crescita.