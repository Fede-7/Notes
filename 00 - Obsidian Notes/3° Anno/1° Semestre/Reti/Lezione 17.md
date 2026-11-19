# Lezione 17 Controllo di Flusso e Congestion Control

## Congestion control e Flow control: la distinzione

Tra i campi dell'header TCP uno non era mai stato usato, e un limite non compare in nessun header:

> [!aside]
> 
> - **Receive window**: quanto spazio rimane nel buffer all'altra estremità; è un limite impostato dal ricevitore.
> - **Congestione**: è l'altro limite, impostato dalla rete, che il mittente deve dedurre da ciò che torna indietro.
> 
> Entrambi generano la stessa azione: inviare meno. L'affidabilità dice cosa fare dopo una perdita, nulla ancora dice come non provocarne una.
> 
> ---
> 
> ![[Lezione 17-1795125758508.png|150]]
> 

## Controllo di flusso

> [!warning] Overflow dei buffer
> **Causa** tipica delle perdite di pacchetti su Internet, non un cavo rotto: può avvenire nel buffer del ricevitore (l'applicazione che legge è lenta) o nei dispositivi di rete come i router (nodi congestionati). Le perdite obbligano poi a ritrasmissioni e timeout che degradano drasticamente le prestazioni della rete.

> [!def] Flow control
> **Servizio** di adattamento della velocità con cui il mittente invia dati rispetto alla velocità con cui l'applicazione ricevente li legge, per non mandare in overflow il buffer di ricezione del TCP.

Quando una connessione TCP riceve byte corretti e in sequenza li colloca nel receive buffer; l'applicazione ricevente li leggerà da quel buffer, ma non necessariamente nell'istante in cui arrivano. Se l'applicazione legge lentamente, un mittente troppo veloce va facilmente in overflow del buffer. Per questo ci si affida al campo **receive window**, con cui il ricevitore comunica al mittente quanto spazio libero è disponibile nel suo buffer.

### Definizione e utilizzo della receive window

> [!aside]
> Sul lato ricevitore (host B) si tengono tre grandezze in byte:
> 
> - **RcvBuffer**: dimensione totale del buffer di ricezione.
> - **LastByteRead**: l'ultimo byte dello stream letto dall'applicazione.
> - **LastByteRcvd**: l'ultimo byte dello stream ricevuto.
> 
> La dimensione della **rwnd** (receive window) si dice allora:
> 
> $$
> \mathrm{rwnd} = \mathrm{RcvBuffer} - (\mathrm{LastByteRcvd} - \mathrm{LastByteRead})
> $$
> 
> ---
> 
> ![[Lezione 17-1795126307899.png|150]]

Il ricevitore colloca la sua rwnd corrente nel campo receive window di ogni segmento che invia indietro. Il mittente tiene due numeri propri: **LastByteSent** e **LastByteAcked**; la loro differenza è la quantità di dati in volo, inviata dal mittente ma non ancora confermati. La regola che il mittente garantisce in ogni istante è:

$$
\mathrm{LastByteSent} - \mathrm{LastByteAcked} \leq \mathrm{rwnd}
$$

Se si rispetta la regola, il buffer di ricezione non può andare in overflow: il mittente non ha mai più dati in volo di quanto c'è spazio. Poiché la connessione è full duplex, ogni direzione ha la propria finestra e ciascuna estremità annuncia la propria.


### Deadlock della finestra zero

> [!warning] Finestra zero e deadlock
> **Problema**: se B annuncia rwnd = 0 e non ha nulla da inviare, quando la sua applicazione svuota il buffer (rwnd > 0) nessuno parla per primo: TCP invia un segmento solo quando ha dati o un acknowledgment da spedire, così la nuova finestra non viene mai annunciata e A, che non può inviare nulla, attende all'infinito.

La specifica spezza il deadlock dal lato mittente: A continua a inviare segmenti con un byte di dati (zero-window probe); il ricevitore li conferma e prima o poi una di quelle conferme porta con sé una finestra non nulla.

### Limiti della finestra e Window Scaling

- **Limite del campo**: il campo TCP Window Size è a 16 bit, così la finestra massima annunciabile è di 65.535 byte, circa 64 KB.
- **Problema**: una finestra è anche un limite di velocità: al massimo una finestra per round trip, quindi al massimo `window/RTT`. 64 KB con un RTT di 100 ms danno circa 5 Mbit/s, qualunque cosa valga il collegamento sottostante.
- **Product banda-ritardo**: 1 Gbit/s sullo stesso RTT richiede 12,5 MB in volo, duecento volte il campo.
- **Soluzione**: **TCP Window Scaling** consente finestre di ricezione più grandi: l'opzione window scale trasporta un fattore di shift, così il numero nel campo non è la finestra ma va shiftato.
- **Negoziazione**: ciascun endpoint annuncia il proprio fattore di scala (S) durante l'handshake TCP; il fattore resta invariato per tutta la connessione.

## Il problema della congestione

> [!warning] La congestione non avvisata
> **Problema**: il controllo di flusso è un accordo tra le due estremità, ma il cammino è condiviso: un mittente può rispettare la finestra del ricevitore e intanto immettere più di quanto il cammino trasporti. Nessun router si lamenta e nessuna estremità vede la coda che si sta riempiendo.

Il problema del controllo della congestione è simile a quello del flusso, ma riguarda l'infrastruttura di rete. Nel caso semplificato, due host condividono un solo router con un solo collegamento in uscita di capacità R byte/s e buffer per i pacchetti in arrivo quando la frequenza supera quella del collegamento; entrambe le applicazioni inviano alla stessa velocità media $\lambda_{\mathrm{in}}$ byte/s.

### Vista semplificata: il caso di buffer infinito

Se due flussi condividono un collegamento di capacità R, la ripartizione vale nel seguente modo:

- Se $\lambda_{\mathrm{in}} < R/2$, tutto ciò che i mittenti inviano arriva ai ricevitori con ritardo finito.
- Se $\lambda_{\mathrm{in}} = R/2$, il collegamento raggiunge la sua piena capacità R e i pacchetti in eccesso si accumulano nel buffer del router.
- Oltre la capacità massima i pacchetti si accumulano aspettando il loro turno; con buffer infinito non si perdono pacchetti, ma il ritardo cresce senza sosta: se la capacità è superata per sempre il ritardo tende all'infinito, cioè i pacchetti sono a tutti effetti perduti.

![[Lezione 17-1795126432743.png|230]]

In termini di prestazioni: **throughput** cresce con $\lambda_{\mathrm{in}}$ fino a R/2, la massima quota disponibile a ciascuna connessione; **ritardo** cresce man mano che $\lambda_{\mathrm{in}}$ si avvicina a R/2, poiché i pacchetti passano sempre più tempo nel buffer; se $\lambda_{\mathrm{in}}$ supera R/2 il traffico in entrata eccede la capacità disponibile e le code crescono o si perdono pacchetti.

### Il caso di buffer finiti

Con buffer finiti, un pacchetto che arriva a un buffer pieno è scartato e, essendo la connessione affidabile, viene ritrasmesso. Tre grandezze si distinguono:

- $\lambda_{\mathrm{in}}$: dati originali, ciò che l'applicazione consegna alla socket.
- $\lambda'_{\mathrm{in}}$: il carico offerto (offered load), cioè dati originali più ritrasmissioni, ciò che il collegamento vede davvero.
- $\lambda_{\mathrm{out}}$: ciò che viene consegnato all'estremità opposta.

Nel primo scenario i tre numeri coincidevano; adesso non più, e le differenze tra essi sono il costo. Tre sottocasi illustrano l'effetto delle ritrasmissioni:

- **a. Nessuna perdita**: tutti i dati inviati sono consegnati con successo, con throughput massimo di R/2 per connessione.
- **b. Ritrasmissione dei pacchetti perduti**: gli overflow del buffer causano perdite, e le ritrasmissioni consumano risorse di rete riducendo il throughput utile.
- **c. Ritrasmissioni non necessarie**: timeout prematuri causano trasmissioni duplicate di pacchetti non perduti, riducendo ulteriormente il throughput utile.

Punto chiave: le ritrasmissioni aumentano il carico di rete senza aumentare la quantità di dati utili consegnati.

### Reti multihop e celle collapse della congestione

In una rete multihop, più mittenti trasmettono lungo percorsi in cui due o più salti si sovrappongono e competono per buffer e capacità limitati dei router; gli effetti sono:

> [!aside]
> 
> - **Spreco di risorse**: un pacchetto può attraversare il primo router ed essere scartato al secondo, sprecando la banda già usata.
> - **Crescita della congestione**: al crescere del carico offerto, più pacchetti sono scartati prima di raggiungere la destinazione.
> - **Congestion collapse**: sotto congestione estrema, il throughput utile può tendere a zero anche mentre la rete resta fortemente carica.
> 
> ---
> 
> ![[Lezione 17-1795126567866.png|100]]


Punto chiave: più traffico trasmesso non significa sempre più dati consegnati. Ciò motiva il controllo di congestione. La congestion collapse è stata osservata in Internet negli anni '80, spingendo allo sviluppo dei meccanismi di congestione di TCP.

## Due approcci al controllo della congestione

- **End-to-end**: l'approccio standard di TCP; la congestione è dedotta dai sistemi finali soltanto dal comportamento osservato della rete, tipicamente perdite di segmenti (timeout o ricezione di 3 ACK duplicati), in risposta alle quali il TCP riduce la velocità di invio.
- **Network-assisted**: approccio recente e opzionale in cui il livello di trasporto collabora con quello di rete: i router forniscono feedback esplicito al mittente e/o al ricevitore sullo stato di congestione, tramite i flag CWR ed ECE. Il feedback può essere un solo bit o essere più sofisticato.

### Explicit Congestion Notification (ECN)

> [!def] ECN
> **Mecchanismo** di network-assisted congestion control che permette ai router di segnalare la congestione marcando i pacchetti invece di scartarli, agendo sul campo ECN a 2 bit dell'header IP.

Ecco come funziona:

- **Marcatura di capacità**: il mittente marca i pacchetti IP come ECN-capable usando il campo ECN a 2 bit: `00` Not-ECT, `01` ECT(1), `10` ECT(0), `11` CE.
- **Rilevamento congestione**: un router congestionato può marcare un pacchetto con CE (Congestion Experienced) invece di scartarlo.
- **Feedback del ricevitore**: il ricevitore imposta il flag **ECE** (ECN Echo) nei suoi acknowledgment per segnalare la congestione.
- **Reazione del mittente**: con il classico TCP ECN (usando ECT(0)), il mittente riduce la sua finestra di congestione al ricevimento di un ACK con ECE impostato e imposta il flag **CWR** (Congestion Window Reduced) per confermare la riduzione.

Punto chiave: ECN permette a TCP di reagire alla congestione senza richiedere perdite di pacchetti, riducendo le ritrasmissioni non necessarie. Con CWR, TCP Reno riduce la finestra del 50%.

I dettagli della negoziazione e dell'interazione TCP/IP:

1. **Negoziazione ECN**: avviene durante il three-way handshake usando i flag ECE e CWR dell'header TCP: nel segmento `SYN` si hanno ECE = 1 e CWR = 1 (richiesta ECN), nel `SYN-ACK` ECE = 1 e CWR = 0 (ECN accettata); la negoziazione stabilisce che entrambi gli endpoint supportano ECN.
2. **Marcatura ECN**: una volta negoziata, il TCP del mittente chiede al livello IP di contrassegnare i pacchetti dati in uscita come ECN-capable (ECT(0) = `10`); TCP e IP comunicano tramite interfacce interne del sistema operativo, non con messaggi di rete addizionali. Al ricevitore, il livello IP avvisa il TCP quando un pacchetto è contrassegnato CE, permettendo al TCP di generare feedback ECE.

Nota: la negoziazione ECN è standardizzata in TCP; l'interazione TCP-IP dipende dall'implementazione. Il campo ECN stesso appartiene all'header IP.

## Controllo di congestione di TCP

TCP fa affidamento principalmente sul controllo di congestione end-to-end: ciascun mittente adatta la sua velocità di invio in funzione della congestione percepita della rete. Tre problemi principali:

- **Controllo della velocità**: come il mittente TCP limita il tasso di invio del traffico sulla sua connessione.
- **Rilevamento congestione**: come il mittente TCP rileva la congestione sul cammino tra sé e la destinazione.
- **Risposta alla congestione**: quale algoritmo deve usare il mittente per variare la velocità in funzione della congestione percepita end-to-end.

Nessun mittente è coordinato con gli altri: ciascuno agisce su informazione locale, in modo asincrono.

### Regolazione della velocità: cwnd

> [!def] Congestion window (cwnd)
> **Variabile** mantenuta dal TCP mittente, a fianco della receive window, che limita la quantità di dati non confermati immessi nella connessione a tutela della rete, non del ricevitore.

Mentre nel flusso regola (ricorda) è:

$$
\mathrm{LastByteSend} - \mathrm{LastByteAcked} \leq \mathrm{rwnd}
$$

nsubseteq controllo di congestione il mittente impone anche:

$$
\mathrm{LastByteSent} - \mathrm{LastByteAcked} \leq \min\{\mathrm{cwnd}, \mathrm{rwnd}\}
$$

così la velocità è regolata aumentando o riducendo cwnd.

![[Lezione 17-1795126889602.png|300]]

### Velocità di invio e self-clocking

La velocità di invio di TCP è determinata approssimativamente da:

$$
\text{Sending rate} \approx \frac{\text{cwnd}}{\text{RTT}}
$$

- **Congestion window (cwnd)**: limita la quantità di dati non confermati in volo.
- **Trasmissione ACK-clocked**: gli acknowledgment in arrivo liberano spazio di finestra, consentendo l'invio di ulteriori dati.
- **Crescita della finestra**: TCP adegua cwnd in base agli acknowledgment e ai segnali di congestione.
- **Dipendenza dal RTT**: con il classico congestion avoidance di TCP, un RTT più lungo significa crescita della finestra più lenta nel tempo.

> [!note] **Punto chiave**
> Connessioni che condividono lo stesso collo di bottiglia possono raggiungere throughput diversi a causa dei loro RTT diversi.

La formula è approssimativa perché TCP non fissa esplicitamente una velocità: controlla la quantità di dati non confermati tramite cwnd, mentre gli arrivi degli ACK determinano quando nuovi dati possono essere inviati; la formula stima la velocità media assumendo cwnd pienamente utilizzato e RTT abbastanza stabile.

### Rilevamento della congestione: eventi di perdita

- Un **evento di perdita (loss event)** accade quando scade un timeout oppure arrivano 3 ACK duplicati o errati.
- Entrambi gli eventi significano che un pacchetto precedente non è arrivato a destinazione, probabilmente per l'overflow di un dispositivo di rete.
- Se non si verificano eventi di perdita, cioè gli ACK arrivano come previsto, TCP assume che la rete non sia congestionata e quindi **aumenta cwnd**.
- Se invece si verificano eventi di perdita, la finestra di congestione deve essere **ridotta**.

### Esplorazione della banda (bandwidth probing)

Il TCP classico adegua la finestra di congestione in base al feedback della rete:

- **ACK ricevuto**: la consegna riuscita consente a cwnd di aumentare.
- **Perdita di pacchetto**: si assume congestione, quindi cwnd viene ridotto.
- **Bandwidth probing**: TCP aumenta ripetutamente cwnd finché la congestione è rilevata, poi arretra.

I meccanismi principali sono: **Slow Start**, **Congestion Avoidance**, **Fast Retransmit** e **Fast Recovery**.

### Slow start

> [!def] Slow start
> **Fase** iniziale del controllo di congestione di TCP: cwnd parte da 1 MSS e cresce di un MSS per ogni segmento confermato, raddoppiando di fatto a ogni round trip.

Il punto di partenza è troppo lento: con un MSS di 500 byte e un cammino di 200 ms si parte da circa 20 kbit/s, e il mittente non sa di quanto accelerare. Crescendo di un MSS per ogni ACK, e tornando indietro a ogni round trip tanti acknowledgment quanti erano i segmenti inviati, la finestra raddoppia a ogni RTT: 1, 2, 4, 8. Si tratta di crescita lineare negli acknowledgment, esponenziale nel tempo: ciò che è lento è il punto di partenza, non la crescita.

Durante Slow Start cwnd raddoppia circa a ogni RTT finché non accade uno di tre eventi:

- **Timeout**: si imposta `ssthresh = cwnd/2`, cwnd torna a 1 MSS e si riparte con Slow Start.
- **cwnd raggiunge ssthresh**: si passa a Congestion Avoidance, con crescita lineare.
- **Tre ACK duplicati**: si innesca Fast Retransmit e si entra in Fast Recovery (in TCP Reno).

Lo **ssthresh** (Slow Start Threshold) determina quando TCP passa dalla crescita esponenziale a quella lineare e viene aggiornato in risposta alla congestione.

![[Lezione 17-1795127094568.png|200]]

### Congestion avoidance

Quando cwnd raggiunge ssthresh, TCP passa dalla crescita esponenziale a quella lineare:

- **Crescita della finestra**: circa 1 MSS a ogni RTT.
- **Incremento per ACK**: ogni ACK aggiunge $\mathrm{MSS}^2 / \mathrm{cwnd}$; con cwnd = 10 MSS, ogni ACK aggiunge circa 0,1 MSS, per un totale di circa 1 MSS per RTT.

Punto chiave: TCP esplora la banda disponibile più cautamente rispetto a Slow Start.

### Fast Retransmit e Fast Recovery (TCP Reno)

Scatenati da 3 ACK duplicati, che indicano una probabile perdita di pacchetto:

- **Fast Retransmit**: ritrasmissione immediata del segmento mancante.
- **Adeguamento della finestra**: si imposta `ssthresh ≈ cwnd/2` e `cwnd = ssthresh + 3 MSS`.
- **ACK duplicati ulteriori**: cwnd cresce di 1 MSS per ogni ACK duplicato.
- **Recupero completato**: quando un ACK conferma dati nuovi, si imposta `cwnd = ssthresh` e si riprende Congestion Avoidance.
- **Timeout**: si azzera cwnd a 1 MSS e si riparte da Slow Start.

Idea chiave: il recupero della perdita avviene senza ripartire da Slow Start.

### Algoritmo complessivo e risposta alla congestione

L'algoritmo di regolazione della velocità: la velocità è aumentata finché gli ACK arrivano correttamente (esplorazione della rete), e ridotta quando la congestione è rilevata (eventi di perdita); il processo si ripete continuamente. TCP usa l'algoritmo di Jacobson (1988-1990) che comprende tre fasi:

1. **Slow start**: partendo da 1 MSS, cwnd cresce esponenzialmente.
2. **Additive Increase (congestion avoidance)**: la velocità cresce linearmente.
3. **Fast recovery**: dopo 3 ACK duplicati, TCP ritrasmette il segmento mancante e riduce cwnd senza ripartire da Slow Start.

La risposta alla congestione è **AIMD (Additive Increase, Multiplicative Decrease)**: incremento additivo della finestra, decremento moltiplicativo in caso di perdita; il comportamento tipico del materiale di Reno è a dente di sega.

### Varianti degli algoritmi di controllo di congestione

TCP Reno offre il modello base, ma i sistemi moderni possono usare algoritmi differenti:

- **Tahoe**: azzera cwnd a 1 MSS dopo una perdita, riprendendo da Slow Start.
- **Reno**: introduce Fast Recovery, evitando Slow Start dopo 3 ACK duplicati.
- **CUBIC**: usa crescita cubica di cwnd durante Congestion Avoidance; è il default in Linux.
- **Vegas**: usa le variazioni di RTT per rilevare code in crescita.
- **BBR**: stima la banda del collo di bottiglia e il ritardo di propagazione per regolare la velocità di invio.

Punto chiave: i diversi algoritmi mirano a usare efficientemente la banda disponibile limitando congestione e ritardo.

## Riassunto Congestion Control

- **Flow control**: protegge il buffer del ricevitore tramite la receive window annunciata (rwnd).
- **Congestion control**: protegge la rete adeguando la finestra di congestione del mittente (cwnd) al feedback della rete.
- **Costi della congestione**: le code aumentano il ritardo; perdite e ritrasmissioni sprecano risorse di rete.
- **TCP Reno classico**: Slow Start accresce cwnd esponenzialmente, Congestion Avoidance linearmente, Fast Recovery evita di ripartire dopo 3 ACK duplicati.
- **Limite all'invio**: i dati non confermati sono limitati da `min(cwnd, rwnd)`.