# Lezione 11 Transfer Layer trasferimento affidibile dei dati

## Il problema del trasferimento affidibile

In un canale inaffidabile i messaggi possono essere **persi**, **alterati**, **scambiati** o **duplicati**: potresti accorgerti che il messaggio è sbagliato, ma anche fare l'azione sbagliata o perdere quella giusta. Il controllo di errori (es. checksum) fa capire al ricevente se il messaggio è corrotto, ma **non basta**: il trasferimento affidibile resta uno dei problemi centrali del networking, affrontato sia a livello trasporto sia a livello link (e spesso applicativo).

In un canale affidibile si garantiscono tre proprietà:

1. Nessun bit trasmesso è **corrotto** (invertito da 0 a 1 o viceversa).
2. Nessun bit è **perso o ripetuto**.
3. Tutti i bit sono consegnati **nell'ordine esatto** di invio.

In generale si assume che il livello rete sottostante sia **inaffidabile**: assunzione realistica (TCP è un protocollo affidabile implementato sopra un livello rete IP end-to-end inaffidabile).

## Corruzione dei pacchetti e stop-and-wait

Nel canale si assuma prima che i bit possano solo essere **corrotti** (tipico problema dei componenti fisici: un pacchetto è trasmesso, propagato e bufferizzato più volte).

> [!def] Stop-and-wait
> **Approccio** in cui ogni messaggio deve essere confermato prima di inviarne uno nuovo; i protocolli basati su ritrasmissione sono detti **ARQ** (*Automatic Repeat reQuest*).

- **ACK** (acknowledgment positivo): il messaggio è arrivato integro.
- **NCK** (acknowledgment negativo): c'è stato un errore, il messaggio va ripetuto.

Problemi dell'approccio:

- Cosa succede se **ACK/NCK stesso si corrompe**? Come fa il ricevente a sapere se un messaggio è una **ripetizione** invece che uno nuovo?
- **Risoluzione: numero di sequenza** — un campo nelle header dei pacchetti che specifica l'ordine di ricezione atteso.
- Nello stop-and-wait c'è **un solo messaggio sulla linea**: basta distinguere il pacchetto corrente dal precedente, quindi **un solo bit** (`s = 0/1`) di numero di sequenza.

## Perdita di pacchetti e timeout

Assumendo che i pacchetti possano anche **perdersi** (ragionevole: i dispositivi di rete possono andare in buffer overflow con traffico intenso), lo stop-and-wait ha un problema di **stallo**: perso il messaggio o l'acknowledgment, l'host A non è mai più innescato a spedire.

- **Risoluzione: timeout** lato mittente: scaduto il timer, l'host riprova; l'idea è la stessa usata nel DNS su UDP. Funziona sia in caso di perdita del pacchetto sia dell'ack; in caso di duplicato il ricevente **scarta** il pacchetto.
- Scegliere il timeout è difficile (dipende dall'RTT): un timeout **troppo lungo** rallenta la comunicazione, uno **troppo corto** fa sovrapporre i pacchetti; un timeout ragionevole è **qualcosa più lungo dell'RTT**.
- Il timeout salva lo stop-and-wait dallo stallo, ma le prestazioni restano molto scarse.

## Prestazioni dello stop-and-wait e pipelining

Con due host su coste opposte degli USA (RTT alla velocità della luce ≈ 30 ms), canale a $R = 1$ Gbps e pacchetti di $L = 1000$ byte (8000 bit), il tempo di trasmissione è $t = L/R = 8$ μs: il mittente è in attesa **quasi tutto il tempo** (~99.97% del tempo totale di ~$RTT + L/R$), poiché invia il pacchetto e poi resta fermo fino all'ACK.

> [!def] Pipelining
> **Tecnica** in cui il mittente può inviare **più pacchetti senza attendere gli acknowledgment** (es. 3 pacchetti invece di 1): con 3 pacchetti il tempo totale cresce appena, e la frazione di attesa del mittente scende.

Con il pipelining servono accorgimenti:

- L'**intervallo dei numeri di sequenza va aumentato**: ogni pacchetto in transito (esclusi i ritrasmissioni) deve avere un numero di sequenza **univoco**, e possono esserci più pacchetti in transito non confermati.
- Servono **buffer** per memorizzare i pacchetti in arrivo, perché non si sa se sono corretti o se ci sono "buchi" nella trasmissione.
- I due protocolli base basati su pipelining sono **Go-Back-N** e **Selective Repeat**.

## Go-Back-N

> [!def] Go-Back-N
> **Protocollo** (detto anche *sliding-window*): il mittente può trasmettere più pacchetti senza attendere acknowledgment, ma non può avere **più di N pacchetti non confermati**.

Notazione:

- **`base`**: numero di sequenza del pacchetto non confermato più vecchio.
- **`nextseqnum`**: più piccolo numero di sequenza non usato (prossimo da spedire).

Partizione dello spazio dei numeri di sequenza:

- Pacchetti in $[0, \text{base}-1]$: trasmessi e **confermati**.
- Pacchetti in $[\text{base}, \text{nextseqnum}-1]$: **inviati ma non confermati**.
- Pacchetti in $[\text{nextseqnum}, \text{base}+N-1]$: **possono essere inviati**.
- Pacchetti in $[\text{base}+N, +\infty]$: **non usabili** finché non arriva un nuovo acknowledgment.

Il ricevente in GBN è molto semplice:

- **Scarta i pacchetti out-of-order** (che siano danneggiati o no) e consegna al livello superiore **solo i pacchetti in ordine**.
- I pacchetti scartati (non confermati) saranno prima o poi **ritrasmessi dal mittente**.
- Il mittente mantiene gli indici della finestra; il ricevente mantiene solo il numero di sequenza del **prossimo pacchetto in ordine** atteso.

Svantaggio: scartare un pacchetto ricevuto correttamente costringe a **reinviarlo** di nuovo; è una reazione a catena — con la rete in difficoltà, molti pacchetti corretti ma out-of-order vengono scartati, forzando ritrasmissioni che a loro volta possono perdersi o corrompersi.

## Selective Repeat

Con finestre grandi, un **singolo** errore può costringere GBN a ritrasmettere molti pacchetti inutilmente.

> [!def] Selective Repeat
> **Protocollo** in cui il mittente **ritrasmette solo i pacchetti** probabilmente ricevuti in errore (persi o corrotti).

- Come in GBN, i singoli pacchetti sono confermati individualmente e la finestra di N limita i pacchetti non confermati.
- A differenza di GBN, i pacchetti **out-of-order sono bufferizzati** (memorizzati) e confermati dal ricevente: si evita di rinviare i pacchetti già arrivati, evitando ulteriori perdite o errori.

Problema della dimensione: la finestra è legata ai numeri di sequenza, che sono **finiti**. Con 4 pacchetti, numero massimo di sequenza 3 e finestra 3: se i pacchetti 0–2 arrivano e i loro ACK partono (ma non arrivano), la finestra del ricevente scorre su $[3, 0, 1]$ **senza certezza** degli ACK:

- Se gli ACK dei primi tre pacchetti si perdono, il mittente li ritrasmette: il pacchetto 0 è **nuovo o vecchio**?
- Se gli ACK arrivano e vengono spediti 3 e 0 ma il 3 si perde: il pacchetto 0 è **nuovo o vecchio**?

> [!warning] Dimensione della finestra in SR
> Per evitare l'ambiguità, **lo spazio dei numeri di sequenza deve essere almeno il doppio della finestra**: $|\text{sequenze}| \geq 2 \cdot N$.