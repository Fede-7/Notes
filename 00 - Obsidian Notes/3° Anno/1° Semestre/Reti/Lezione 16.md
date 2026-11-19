# Lezione 16 TCP

## Il segmento TCP

**Il segmento TCP** è composto da un campo header e da un campo dati, quest'ultimo contiene dati applicativi di dimensione al massimo pari a MSS (Maximum Segment Size).

L'header è variabile a causa del campo opzioni e contiene i seguenti campi:

- **Sequence number** (32 bit): per il reliable data transfer.
- **Acknowledgment number** (32 bit): per il reliable data transfer.
- **Receive window** (16 bit): indica quanti byte il ricevitore è disposto ad accettare; è usato per il controllo di flusso.
- **Header length** (4 bit): specifica il numero di parole da 32 bit contenute nell'header.
- **Options field** (variabile): usato per processi opzionali come la negoziazione dell'MSS o il time-stamping.
- **Flags** (6/12 bit): le singole bande sono descritte nell'elenco seguente.
- **Checksum** (16 bit): per il controllo di integrità.
- **Urgent data pointer** (16 bit): indica la posizione dell'ultimo byte della parte urgente dei dati.

I flag del segmento TCP sono:

- **ACK**: indica che il segmento è un ACK, quindi il campo acknowledgment number è in uso.
- **RST**, **SYN**, **FIN**: usati per l'apertura e la chiusura della connessione.
- **CWR** ed **ECE**: usati nella notifica esplicita di congestione (opzionale).
- **PSH**: dice al ricevitore di passare subito i dati all'applicazione.
- **URG**: indica che il segmento contiene dati "urgenti".

### I tre bit di gestione della connessione

- **SYN**: apre una connessione; è impostato nei primi due segmenti di una connessione e mai più.
- **FIN**: il mittente non ha più dati da inviare; chiude una sola direzione ed è inviato una volta per direzione.
- **RST**: qui non esiste alcuna connessione; il segmento va scartato e mai ritrasmesso.

I campi sequence number e acknowledgment number trasportano l'accordo sui numeri; i tre bit SYN, FIN e RST dicono di che tipo di accordo si tratta.

## Problemi nella gestione delle connessioni

> [!def] Three-way handshake
> **Procedura** con cui TCP apre o chiude una connessione: le richieste di apertura/chiusura devono essere confermate da entrambi gli host prima che la connessione sia stabilita o rilasciata.

Poiché TCP è orientato alla connessione, i due host devono concordare apertura e chiusura; però i messaggi possono essere perduti o danneggiati sulla rete, e in tal caso un'estremità può risultare aperta o chiusa mentre l'altra non lo è. Il three-way handshake mitiga, ma non elimina, questo problema.

### Il two-army problem

> [!info] Two-army problem
> Due armate alleate, separate dal nemico da un valle attraversabile da messaggeri inaffidabili, devono sincronizzare un attacco simultaneo ricambiando conferme su conferme: nessuna conferma è certa perché quella successiva può perdersi.

Il nodo del problema: il comandante che invia la risposta non sa se la sua conferma è arrivata; aggiungendo una terza conferma (handshake a tre vie) il dubbio si sposta sul mittente dell'ultimo messaggio, e un'eventuale quarta conferma non risolve nulla. Può essere dimostrato che **nessun protocollo esiste** che garantisca l'accordo su una rete inaffidabile.

Ciò che è impossibile: in una rete inaffidabile nessuno scambio finito di messaggi può garantire che entrambi gli endpoint sappiano con certezza che l'altro ha completato lo scambio.

Ciò che TCP richiede è più debole: ogni estremità ha appreso il numero iniziale dell'altra e sa che il proprio è stato ricevuto. Tre segmenti consegneranno esattamente questo: ogni segmento è confermato dal successivo. Il dubbio residuo riguarda l'ultimo ACK; successivi scambi di dati possono confermarlo implicitamente, e durante la chiusura il timer TIME-WAIT lo gestisce.

## Instaurazione della connessione

> [!def] Connection establishment in TCP
> **Scambio** di tre segmenti (SYN, SYNACK, ACK) con cui client e server allocano buffer e variabili e concordano i numeri di sequenza iniziali, prima di qualsiasi dato applicativo.

Il procedimento è quindi il seguente:

1. Il client invia un segmento **SYN**: senza payload, con SYN bit a 1 e un numero di sequenza iniziale casuale (`client_isn`).
2. Il server, appena che il SYN è arrivato, alloca buffer e variabili TCP, quindi risponde con un **SYNACK** (SYN e ACK a 1, acknowledgment = `client_isn+1`, numero di sequenza iniziale casuale `server_isn`).
3. Il client, appena che il SYNACK è arrivato, alloca a sua volta buffer e variabili e invia un **ACK** finale (ACK a 1, SYN a 0, acknowledgment = `server_isn+1`), che può già trasportare dati applicativi.

L'instaurazione è una procedura delicata che può aggiungere ritardi significativi; esiste tipicamente un timeout di 30-60 secondi, superato il quale la procedura è abortita. Alcuni attacchi, come il SYN flood, colpiscono proprio questa fase.

### Numeri di sequenza iniziali casuali

Niente costringe una connessione a partire da zero, e partire da zero sarebbe una cattiva scelta:

- Un segmento di una connessione precedente tra i medesimi quattro identificativi può ancora vagare nella rete; con un nuovo punto di partenza cade fuori dalla finestra della nuova connessione ed è scartato invece di essere accettato come dati.
- Un attaccante che può indovinare i numeri può iniettare segmenti in una connessione che non vede; renderli casuali è una difesa.
- L'`+1` di ritorno è una piccola prova: solo chi ha ricevuto il SYN poteva scriverlo.

### Interfaccia di sistema: listen, connect, accept

- **listen**: è la transizione nello stato LISTEN; da quell'istante il kernel risponde ai SYN da solo, senza coinvolgere alcun processo.
- **connect**: invia il SYN e resta bloccato; ritorna quando il SYNACK è arrivato e il terzo segmento è stato inviato.
- **accept**: non prende parte all'handshake; consegna una connessione già stabilita.

Il server può quindi chiamare `accept` in ritardo senza che alcun client se ne accorga: la connessione è già aperta e i dati aspettano in un buffer. L'handshake è fatto dai due kernel; il programma legge solo il risultato, che gli arriva come descrittore o come errore.

### Le due code di un socket in ascolto

> [!def] SYN queue e accept queue
> **Code** di ogni socket in ascolto: la prima contiene connessioni half-open (SYN ricevuto, terzo segmento mancano), la seconda connessioni completate in attesa di essere accettate.

- Un SYN in arrivo crea un elemento nella prima coda; l'ACK finale sposta quell'elemento nella seconda.
- `accept` rimuove un elemento dalla seconda coda: il **backlog** passato a `listen` è la lunghezza di quella coda.
- Se la seconda coda si riempie, nuove connessioni sono scartate o rifiutate, e per il client appare solo un ritardo senza spiegazione.
- La SYN queue è un bersaglio per gli attacchi SYN flood, mitigabili con i SYN cookie.

### Fallimenti durante `connect`

- **Nessuna risposta al SYN**: TCP ritrasmette il SYN alcune volte con intervallo crescente, poi abbandona; `connect` fallisce con `errno = ETIMEDOUT` dopo decine di secondi.
- **Rifiuto immediato**: se l'host è attivo ma nessuno è associato a quella porta, risponde con un segmento con RST a 1 e `connect` fallisce con `ECONNREFUSED`.

Il programma vede i due casi come errori diversi: un timeout, o il rifiuto tipico di un client avviato prima del server. Per UDP tale segnalazione arrivava dal livello di rete; qui è un segmento di trasporto, dal TCP del peer.

### SYN flood e SYN cookie

> [!warning] SYN flood
> **Attacco** di tipo denial-of-service: SYN falsi riempiono la coda delle connessioni half-open, esaurendo una coda, non la banda, con pochissimo traffico.

Il problema: il terzo segmento dello handshake non arriva mai, ma il server ha già allocato buffer e variabili e tiene la connessione half-open per un minuto o più. Bastano abbastanza SYN (con indirizzi sorgente falsificati, così i SYNACK vanno a host che non hanno mai richiesto nulla) per riempire la coda di connessioni half-open con voci che non completeranno mai, rifiutando i client legittimi. Fu tra i primi attacchi denial-of-service documentati ed è ancora tra i più comuni.

> [!def] SYN cookie
> **Tecnica** di difesa dal SYN flood: il server risponde ai SYN senza allocare memoria per connessioni incomplete, codificando lo stato della connessione nel numero di sequenza del SYN-ACK.

Normalmente il server salva ogni connessione half-open nella SYN queue; quando questa si riempie, il server può attivare i SYN cookie e rispondere senza salvare stato: calcola un cookie come `hash` di indirizzi IP, porte, una chiave segreta e informazioni sul tempo, lo codifica nel numero di sequenza iniziale (ISN) del SYN-ACK, e alloca risorse per la connessione stabilita solo quando l'ACK finale arriva e il cookie è validato. Così un SYN flood non può esaurire la coda per le connessioni gestite con cookie.

Le tre risposte possibili a un SYN e il loro significato:

| Risposta al SYN | Significato | Stato |
|---|---|---|
| SYNACK | qualcosa è in ascolto su quella porta | open |
| RST | l'host è attivo, ma quella porta non è servita | closed |
| nessuna risposta | non è mai arrivato: qualcosa lo ha scartato | filtered |

Con un SYN per porta le tre risposte mappano una macchina dall'esterno senza completare mai una connessione; lo strumento abituale è `nmap`, usato per diagnosticare una rete.

## Rilascio della connessione

**Il rilascio (teardown)** può essere avviato da ciascuno dei due host. Assumendo che sia il client a chiudere, il procedimento con handshake a tre vie è:

1. Il client invia un segmento **FIN** (FIN bit a 1) per informare il server che ha finito di inviare.
2. Il server risponde con un segmento di acknowledgment/chiusura (ACK a 1, FIN a 1). Nota: ACK e FIN possono viaggiare nello stesso segmento o in due separati.
3. Il client conferma il segmento di chiusura del server con un ultimo ACK.

### Half-close

- Un **FIN** dice "non ho più dati da inviare", non "questa connessione è finita": chiude una sola direzione.
- Dopo aver inviato il proprio FIN il client può ancora ricevere; dopo averlo confermato il server può continuare a inviare quanto vuole.
- I due FIN sono quindi indipendenti e il rilascio normale usa quattro segmenti: FIN, ACK, poi FIN e ACK nell'altra direzione.
- Collassano in tre soltanto quando il peer non ha più nulla da inviare e chiude subito: allora il suo ACK e il suo FIN viaggiano insieme.
- `close` invia il FIN e rinuncia al descrittore; `shutdown(fd, SHUT_WR)` lo invia e continua a leggere, ed è il modo in cui un client dichiara che la richiesta è finita.

### TIME-WAIT

L'estremità che chiude per prima non va direttamente in CLOSED: aspetta, tipicamente da trenta secondi a due minuti.

- **Prima ragione**: se il suo ultimo acknowledgment è perso, il peer ritrasmetterà il suo FIN, e qualcuno deve esserci per rispondere.
- **Seconda ragione**: segmenti della connessione possono ancora essere nella rete, e i suoi quattro numeri potrebbero essere assegnati a una nuova connessione.
- L'attesa è pari a circa due volte il tempo massimo di vita di un segmento, così tutto ciò che appartiene alla vecchia connessione muore prima.
- È il prezzo di chi chiude per prima, non necessariamente il client.

> [!error] bind che fallisce dopo un riavvio del server
> **Causa**: interrompendo il server lo si è reso l'estremità che ha chiuso per prima; le sue connessioni sono in TIME-WAIT, tengono ancora occupata la porta locale, e `bind` non accetta una porta usata da una connessione viva.

La soluzione è `SO_REUSEADDR`, che dice a `bind` di procedere comunque: è sicuro, perché la vecchia connessione conserva i propri quattro numeri e nessun suo segmento può essere consegnato alla nuova socket. Quando il client chiude per primo, caso abituale, il server non entra mai in TIME-WAIT e il problema non si presenta.

### Il descrittore che nessuno ha chiuso

> [!error] Forget to close the descriptor
> **Bug**: se `recv` restituisce 0 e il programma non chiude il descrittore, la connessione resta per sempre in CLOSE-WAIT: il FIN del peer è stato confermato, ma il proprio FIN non viene mai inviato.

In un primo momento apparentemente non si rompe nulla; però il peer resta anche lui in attesa, il rilascio non finisce da nessuna parte e nessun programma viene avvisato. Dopo qualche migliaio di client il server esaurisce i descrittori e smette di accettare: il guasto appare lontano dalla sua causa. Il comando `ss -tn state close-wait` elenca esattamente quelle connessioni: una colonna di CLOSE-WAIT è sempre un bug del programma, mai della rete. Il valore 0 di `recv` è il FIN in arrivo: è un'istruzione a chiudere, non un errore da ignorare.

### Gestione della perdita di pacchetti nel rilascio

Poiché il three-way handshake non è perfetto, TCP si affida a temporizzatori per chiudere comunque le connessioni o reinviare le richieste.

- Se l'ultimo ACK del client si perde, il server resta in attesa; alla scadenza del suo timer rilascia la connessione comunque: entrambe le estremità finiscono chiuse, non nello stesso istante, e nessuna se ne accorge.
- Se a perdersi è la risposta del server, il client, che non sa ancora nulla, lascia scadere il suo timer e ritrasmette il FIN, esattamente come ritrasmetterebbe un segmento di dati; il server risponde al FIN ripetuto con lo stesso segmento inviato prima, e stavolta il segmento arriva.

La ritrasmissione alla chiusura non è un meccanismo nuovo: un timer, e una copia conservata finché non è confermata.

### Connection reset: RST

> [!def] RST
> **Flag** che interrompe immediatamente una connessione TCP, a differenza del FIN che ne supporta la chiusura graduale, potendo scartare i dati già in buffer.

L'host genera un segmento RST quando riceve un segmento riferito a una connessione inesistente, ad esempio un SYN verso una porta chiusa. Un host terminato per crash non invia né FIN né RST, così il peer continua a considerare la connessione aperta; dopo il riavvio, se il peer invia dati, l'host che ha perso lo stato risponde con RST. Un RST ricevuto può generare `ECONNRESET`; le scritture successive possono fallire con `EPIPE` e generare `SIGPIPE`. TCP rileva i peer non rispondenti tramite timeout di ritrasmissione o, opzionalmente, probe di keepalive; le applicazioni che richiedono rilevamento più rapido dei guasti possono usare heartbeats periodici.

## Osservazione di una connessione

Strumenti e comandi per osservare una connessione TCP:

- `nc -l 5001` crea un endpoint TCP in ascolto sulla porta 5001; `nc localhost 5001` si connette. In TCP ciò che si digita sul client appare sul server; nell'altra direzione viaggia solo un acknowledgment, un segmento senza dati.
- Il filtro di cattura Wireshark `tcp && tcp.port==5001 && ip` combina tre clausole: il protocollo di trasporto, la porta e il protocollo di rete sottostante; la clausola centrale da sola basterebbe.
- Tutto è avvenuto su `127.0.0.1`: le due estremità sono lo stesso host e nessun pacchetto raggiunge un cavo; l'interfaccia su cui catturare è quindi la loopback, puntando il analizzatore di pacchetti su quella reale non si vedrebbe nulla.

Un trasferimento di file con `nc` (per esempio `nc -l 12338 > real2.doc` sul server e `nc 127.0.0.1 12338 < real.doc` sul client) mostra la natura di TCP: ciò che viaggia è un **byte stream** senza struttura, e nulla sul filo indica dove il file finisce. Poiché `nc` non si ferma quando l'input è esaurito, il trasferimento è chiuso a mano: è il `Ctrl-C` a inviare il FIN, che qui fa da marcatore di fine file. Un protocollo che deve inviare più file sulla stessa connessione deve dirlo da sé.