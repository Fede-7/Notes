# Lezione 11: Trasporto affidabile dei dati

## Il problema del trasferimento affidabile

Si pensi all'annuncio di una stazione: "Il treno 6 arriverà al binario 9". Se la comunicazione non è affidabile, le parole possono essere **perse** ("Il treno %&! arriverà al binario 9"), **alterate** ("Il treno 7 arriverà al binario 9"), **scambiate** ("Il treno 9 arriverà al binario 6") o **duplicate** ("Il treno 66 arriverà al binario 9"). Potreste accorgervi che il messaggio è sbagliato, ma potreste anche prendere il treno sbagliato o perdere quello giusto.

Il controllo degli errori (es. via checksum) permette al ricevente almeno di capire **se il messaggio è corrotto**, ma non basta: il trasferimento affidabile **resta uno dei problemi principali del networking**, affrontato non solo al livello di trasporto, ma anche al livello di collegamento e (spesso) applicazione. In un canale affidabile si devono garantire tre cose:

1. Nessun bit trasmesso **è corrotto** (invertito da 0 a 1 o vice versa).
2. Nessun bit trasmesso **è perso o ripetuto**.
3. Tutti i bit sono consegnati **nell'ordine esatto** di invio.

In generale si deve assumere che il livello di rete sottostante **non è affidabile**: un'assunzione realistica, dato che ad esempio TCP è un protocollo affidabile **implementato sopra un livello di rete (IP) end-to-end non affidabile**.

## Corruzione dei pacchetti e Stop-and-wait

Si assuma un **canale in cui i bit possono solo corrompersi** (non perdersi): la corruzione è un problema tipico, dovuto principalmente ai componenti fisici della rete, poiché un pacchetto viene trasmesso, propagato e bufferizzato più volte durante la comunicazione. Un primo approccio è lo **stop-and-wait**, che richiede che ogni messaggio sia confermato prima di inviarne uno nuovo, tramite **acknowledgment positivo (ACK)** — il messaggio è arrivato intatto — o **acknowledgment negativo (NCK)** — c'è stato un errore, il messaggio va ripetuto. I protocolli basati su ritrasmissione sono detti anche **ARQ** (*Automatic Repeat reQuest*).

### Problemi di stop-and-wait

Restano due domande: cosa succede se **il messaggio ACK/NCK stesso è corrotto**, e come può l'host B essere sicuro che **un messaggio è una ripetizione** anziché uno nuovo? La soluzione è il **numero di sequenza**: aggiungere agli header un campo che specifica l'ordine di ricezione dei pacchetti. Nello stop-and-wait c'è sempre **un solo messaggio** in linea, quindi basta **distinguere il pacchetto attuale dal precedente**: basta un solo bit ($s = 0/1$).

## Perdita di pacchetti e timeout

Si assuma ora un **canale in cui i pacchetti possono anche perdersi** — un'assunzione ragionevole, dato che i dispositivi di rete possono andare in **buffer overflow** con traffico intenso. Il problema è evidente: **se un messaggio si perde, gli host non invieranno mai quello nuovo**, creando un loop. Vale sia perdendo il messaggio che l'acknowledgment: in entrambi i casi l'host A non viene "svegliato" per inviare.

La soluzione è semplice ed efficace: **aggiungere un timeout lato mittente** che, scaduto, gli permette di riprovare. Un approccio simile è usato nel DNS basato su UDP; il timeout **funziona sia per perdita del pacchetto che dell'acknowledgment**, e in caso di duplicato il ricevente si limita a scartare il pacchetto. La sfida è **come stimare un timeout adeguato** (dipende dall'RTT): troppo lungo la comunicazione rallenta, troppo corto i pacchetti si sovrappongono; un timeout ragionevole dev'essere in qualche modo più lungo dell'RTT. Il timeout salva lo stop-and-wait dal loop, ma **le prestazioni restano piuttosto scarse**.

### Analogia con l'acqua

Il trasferimento dati si può vedere come un flusso d'acqua: c'è un tempo $t$ per versare l'acqua dal serbatoio al tubo, dopo il quale tutta l'acqua è nel tubo (serbatoio di partenza e destinazione vuoti). L'acqua impiega un tempo (RTT/2) a scorrere nel tubo, infine arriva al serbatoio di destinazione e — con tempi di upload/download uguali — impiega lo stesso tempo $t$ per uscire (RTT/2 + $t$ per ricevere l'ultima goccia).

## Prestazioni dello stop-and-wait

Si consideri il caso idealizzato di **due host sulle coste opposte degli USA**: RTT alla velocità della luce di circa 30 ms (0,03 s), canale a velocità $R$ = 1 Gbps ($10^9$ bit/s), pacchetto di $L$ = 1000 byte (8000 bit). Il tempo $t$ per trasmettere il pacchetto è $t = L/R = 8000/10^9 = 8$ **microsecondi**.

In **stop-and-wait**: il mittente **inizia a inviare** al tempo $t_0$; l'**ultimo bit entra nel canale** a $t_0 + 0{,}000008$ s; il pacchetto impiega **0,015 s per arrivare** al ricevente; l'**ultimo bit è ricevuto** a $t = \text{RTT}/2 + L/R = 0{,}015008$ s; assumendo gli ACK molto piccoli (tempo di trasmissione trascurabile), l'ACK torna al mittente a $t = \text{RTT} + L/R = 0{,}030008$ s. Su 0,030008 s totali, il mittente ha atteso quasi tutto il tempo (**99,973%**).

## Pipelining

Con il **pipelining**, invece dello stop-and-wait, al mittente è **consentito inviare più pacchetti** senza attendere gli acknowledgment. Con 3 pacchetti invece di 1: il mittente inizia a $t_0$; l'**ultimo bit dell'ultimo pacchetto entra** a $t_0 + 0{,}000024$ s; l'**ultimo bit è ricevuto** a $t = \text{RTT}/2 + L/R = 0{,}015024$ s; l'ACK torna a $t = \text{RTT} + L/R = 0{,}030024$ s. In 0,030024 s il mittente ha atteso un po' meno (**99,920%** invece di 99,973%).

Nel pipelining **l'intervallo dei numeri di sequenza va aumentato** — ogni pacchetto in volo (escluse le ritrasmissioni) deve avere un numero di sequenza univoco e possono esserci più pacchetti in volo non confermati — e servono **buffer per memorizzare i pacchetti in arrivo**, perché non si sa se sono corretti o se ci sono "buchi" nella trasmissione. I due protocolli base con pipelining sono **Go-Back-N** e **Selective Repeat**.

## Go-Back-N (GBN)

Il protocollo **Go-Back-N** (detto anche *sliding window*) permette al mittente di trasmettere più pacchetti **senza attendere acknowledgment**, ma con il vincolo di **non più di N pacchetti non confermati**. Le variabili chiave sono **base**, il numero di sequenza del **pacchetto più vecchio non confermato**, e **nextseqnum**, il più piccolo numero di sequenza **non ancora usato** (prossimo da inviare). Allora:

- I pacchetti in $[0, \text{base}-1]$ sono stati **trasmessi e confermati**.
- I pacchetti in $[\text{base}, \text{nextseqnum}-1]$ sono **inviati ma non confermati**.
- I pacchetti in $[\text{nextseqnum}, \text{base}+N-1]$ **possono essere inviati**.
- I pacchetti in $[\text{base}+N, +\infty)$ **non possono essere usati** finché non arriva un nuovo acknowledgment.

### Il ricevente in GBN

In GBN **il ricevente è molto semplice**: deve **semplicemente scartare i pacchetti fuori ordine** (che siano corrotti o no) e consegnare al livello superiore solo i pacchetti in ordine; i pacchetti scartati (non confermati) saranno prima o poi ritrasmessi dal mittente. Con questo approccio anche pacchetti buoni vengono scartati, ma il processo resta semplice: il **mittente mantiene gli indici della finestra**, mentre il **ricevente deve mantenere solo il numero di sequenza del prossimo pacchetto in ordine**.

Lo svantaggio è che un pacchetto ricevuto correttamente va **rispedito comunque**: è una **reazione a catena** — se si perdono pacchetti per difficoltà di rete, molti pacchetti corretti ma fuori ordine vengono scartati, forzando il mittente a ritrasmetterli, e la ritrasmissione stessa può perdersi o corrompersi, richiedendo altre ritrasmissioni. Ad esempio, se si perde pkt2, anche pkt3, pkt4 e pkt5 vanno scartati e ritrasmessi, anche se corretti.

## Selective Repeat (SR)

GBN è più efficace dello stop-and-wait, ma può **soffrire di problemi di prestazioni**: con finestre grandi, **un solo errore può causare la ritrasmissione di molti pacchetti**, molti inutilmente. Nei protocolli **selective-repeat (SR)** il mittente ritrasmette **solo i pacchetti presumibilmente ricevuti con errore** (persi o corrotti): come in GBN, i singoli pacchetti sono confermati e si usa di nuovo **una finestra di N** per limitare i pacchetti non confermati; diversamente da GBN, però, **i pacchetti fuori ordine vengono bufferizzati** (memorizzati) e confermati dal ricevente.

Ad esempio, con pacchetti persi: il ricevente inizialmente bufferizza pkt3, pkt4 e pkt5 in attesa che pkt2 (perso) sia ritrasmesso, evitando così di rispedire pkt3, pkt4 e pkt5, ed evitando ulteriori perdite o errori di trasmissione.

### Limite della finestra in SR

Resta un problema: la dimensione della finestra è legata al numero di sequenza, **che è finito**. Si considerino 4 pacchetti, **numero di sequenza massimo 3**, finestra di dimensione 3; i pacchetti da 0 a 2 sono ricevuti correttamente e gli ACK inviati (ma non ancora ricevuti). La **finestra del ricevente si sposta sul 6° pacchetto** (cioè su [3, 0, 1]) anche se gli ACK non sono stati ricevuti. Nel **caso a** gli ACK dei primi tre pacchetti si perdono e il mittente li ritrasmette: il pacchetto 0 è nuovo o vecchio? Nel **caso b** gli ACK arrivano, si inviano i pacchetti 3 e 0 ma il 3 si perde: il pacchetto 0 è nuovo o vecchio? Per evitare il problema, **lo spazio dei numeri di sequenza dev'essere almeno il doppio della dimensione della finestra**.