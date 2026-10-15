# Application Layer HTTP

## Web e HTTP

Fino ai primi anni '90 Internet era usato principalmente da ricercatori, accademici e studenti (Telnet per il login remoto, FTP per i file, e-mail); il **World Wide Web**, nei primi anni '90, fu la prima applicazione che catturò il grande pubblico.

> [!def] World Wide Web
> **Insieme di informazione** (documenti, immagini, video, audio, ecc.) accessibile su Internet secondo il protocollo **HTTP** (*HyperText Transfer Protocol*).

La comunicazione HTTP è tipicamente **client-server**:

- Un programma client traduce le richieste dell'utente in messaggi HTTP: è il **browser** (Chrome, Firefox, Edge, Safari, ecc.).
- Un programma server esegue le richieste HTTP e restituisce le **risposte** HTTP.

HTTP definisce principalmente due cose:

- La **struttura dei messaggi**.
- **Come client e server si scambiano** tali messaggi.

Il Web e i suoi protocolli sono la piattaforma per applicazioni web-based (YouTube, web-mail, app mobili, social network). HTTP evolve continuamente per bilanciare affidabilità e prestazioni.

## URL

> [!def] URL
> **Uniform Resource Locator**: stringa che identifica una risorsa (o oggetto) sul Web, con la struttura `[protocol]://[usrinfo@][host][:port][/path][?query][#fragment]`.

I campi del URL:

- **`[protocol]`**: protocollo da usare per accedere alla risorsa (`HTTP`, `HTTPS`, `FTP`, ecc.).
- **`[usrinfo]`** (opzionale): informazioni utente come username e password seguite da `@` (es. `username:password@`); per lo più deprecato per ragioni di sicurezza.
- **`[host]`**: nome o indirizzo IP del server.
- **`[port]`** (opzionale): porta da usare, spesso dedotta dal protocollo.
- **`[path]`**: percorso della risorsa nel server (es. `/path/to/resource`).
- **`[query]`**: preceduta da `?`, specifica possibili richieste.
- **`[fragment]`**: preceduta da `#`, identifica un elemento nella risorsa (es. un punto di un formulario).

Pagine e oggetti:

- Le pagine Web consistono di un **file HTML** (*HyperText Markup Language*) di base e riferimenti a oggetti aggiuntivi (immagini, video, Java applet, ecc.).
- Una pagina con testo HTML e cinque immagini JPEG contiene **6 oggetti**: il file base più le 5 immagini.
- La URL `http://www.someSchool.edu/someDepartment/picture1.gif` si legge: `http` protocollo, `www.someSchool.edu` hostname, `/someDepartment/picture1.gif` percorso dell'oggetto.
- Una query reale come `https://en.wikipedia.org/w/index.php?title=SSC_Napoli` si legge: `https` protocollo, `en.wikipedia.org` hostname, `/w/index.php` percorso, `?title=SSC_Napoli` query; equivale alla pagina `https://en.wikipedia.org/wiki/SSC_Napoli`.

## Il protocollo HTTP

HTTP definisce come i client Web richiedono oggetti (es. pagine Web) ai server Web e come i server li trasferiscono ai client.

- Quando l'utente chiede un oggetto (es. cliccando un collegamento), il browser invia al server **messaggi di richiesta HTTP** per gli oggetti della pagina.
- Il server riceve le richieste e risponde con **messaggi di risposta** che contengono gli oggetti.

> [!info] HTTP e livello trasporto
> HTTP usa **TCP** come protocollo di trasporto sottostante; dalla versione **HTTP/3** (2022) può usare anche **UDP**, e circa il 30% del traffico HTTP complessivo viaggia su UDP.

- Il client prima **inizializza la connessione** con il server; stabilita la connessione, browser e server comunicano attraverso le rispettive interfacce **socket**: il client invia richieste nella propria socket e riceve risposte dalla propria socket; analogamente il server riceve richieste e invia risposte nella propria socket.
- Storicamente si usava TCP per i suoi servizi, prima di tutto il **trasferimento affidabile**: TCP garantisce che i messaggi arrivino integri a destinazione (se possibile).
- I servizi di TCP possono però rallentare la comunicazione, quindi HTTP/3 usa anche UDP: si stima che sia circa il **30% più veloce**; si affida a **QUIC** (*Quick UDP Internet Connection*), che implementa l'affidabilità sopra UDP.
- Qui si vede il vantaggio dell'architettura a livelli: le applicazioni HTTP **non si preoccupano** di raggiungibilità o perdita di dati, delegando il lavoro ai livelli inferiori, e risultano più semplici (logicamente e computazionalmente).

## Stateless

> [!def] Stateless
> **Proprietà** delle applicazioni HTTP: il server **non mantiene informazioni** sull'interazione (sequenza di richieste/risposte) con un client specifico.

- Se un client chiede due volte lo stesso oggetto, il server non considera la richiesta ridondante: reinvia l'oggetto, avendo "dimenticato" il passato.
- La semplicità è importante per server che gestiscono molti riferimenti al secondo (in media ~1000 richieste/s; i grandi motori di ricerca ricevono centinaia di migliaia di query al secondo).
- Non tutte le applicazioni sono stateless: diverse sono invece **stateful**.

## Connessioni persistenti e non persistenti

In molte applicazioni client e server comunicano per un periodo esteso scambiando più coppie richiesta-risposta (back-to-back, periodiche o intermittenti). Con un protocollo connection-oriented (TCP o QUIC) si hanno due modalità:

- **Connessione persistente**: tutte le richieste e le relative risposte sono inviate sulla **stessa connessione**.
- **Connessione non persistente**: per ogni coppia richiesta-risposta si stabilisce una **nuova connessione**.

Per impostazione predefinita le applicazioni HTTP odierne usano connessioni persistenti, ma client e server possono essere configurati per la modalità non persistente; le prime versioni di HTTP (1.0) usavano di default la non persistenza.

### Connessione non persistente

> [!aside]
> In una connessione non persistente la connessione si chiude a ogni richiesta servita (es. a ogni oggetto inviato). La sequenza su TCP per una pagina con file HTML base e 10 immagini JPEG (11 oggetti sullo stesso server):
> 
> 1. Il processo client HTTP inizializza la connessione TCP verso il server sulla porta 80 (porta di default di HTTP): una socket al client e una al server.
> 2. Il client invia il messaggio di richiesta HTTP con il percorso `/someDepartment/home.index`.
> 3. Il server riceve la richiesta, recupera l'oggetto (da RAM o disco), lo incapsula in un messaggio di risposta e lo invia tramite la propria socket.
> 4. Il server chiede a TCP di chiudere la connessione; TCP la termina solo dopo aver certificato che il client ha ricevuto la risposta integra (affidabilità).
> 5. Il client riceve la risposta, estrae il file HTML e trova i riferimenti alle 10 immagini JPEG.
> 6. I primi quattro passi si ripetono per ciascuno degli oggetti referenziati.
> 
> ---
> 
> ![[Lezione 4-1792081943365.webp|150]]


> [!example]
> - Servono **11 connessioni TCP** (e 11 paia di socket) per trasferire l'intera pagina, quindi gli elementi possono arrivare in momenti diversi.
> - Le connessioni possono essere stabilite in **sequenza o in parallelo**: ricevuta la pagina base, si possono scaricare in parallelo tutte le immagini; i browser aprono tipicamente 5–10 connessioni TCP parallele, ciascuna per una transazione richiesta-risposta.
> - Il parallelismo **accorcia il tempo di risposta** ma **aumenta il costo computazionale**, e stabilire più connessioni TCP può introdurre comunque un overhead significativo.
> - HTTP definisce solo il protocollo di comunicazione tra programma client e programma server, **non come i contenuti sono visualizzati**: la resa dipende dal browser (due browser possono interpretare la stessa pagina in modo diverso).

### RTT e tempi di risposta

> [!def] RTT
> **Round-Trip Time**: tempo che un pacchetto piccolo impiega per andare dal client al server e tornare al client.

> [!aside]
> - Per stabilire una connessione TCP si esegue il **three-way handshake**: il client invia un segmento TCP per richiedere la connessione; il server risponde con un segmento di acknowledgement; il client conferma al server.
> - Dalla prospettiva dell'RTT servono **2 RTT** per stabilire la connessione (senza perdite); un handshake simile avviene anche alla chiusura.
> - Le prime due parti del handshake consumano 1 RTT; il client invia la richiesta HTTP **insieme alla terza parte** del handshake (l'acknowledgment); arrivata la richiesta, il server invia il file HTML, consumando un altro RTT.
> - Il **tempo totale di risposta** è circa **2 RTT più il tempo di trasmissione** del file HTML da parte del server.
> 
> ---
> 
> ![[Lezione 4-1792082066036.webp|200]]

### Connessione persistente

- Il server **lascia aperta** la connessione TCP dopo aver inviato una risposta.
- Un'intera pagina Web (file HTML e oggetti referenziati) e anche più pagine dello stesso server verso lo stesso client viaggiano su **una sola** connessione persistente.
- Il risparmio è di circa **2–4 RTT per oggetto**.

**Pipelining**: le richieste degli oggetti possono essere fatte back-to-back, senza attendere le risposte; da HTTP/2 richieste e risposte multiple possono essere **interleave** sulla stessa connessione, con meccanismi per **prioritizzare** richieste e risposte. Connessione persistente con pipelining è la modalità di default di HTTP.

![[Lezione 4-1792082164482.webp|200]]

### Confronto persistente vs non persistente

**Persistente**:

- Più **veloce**, soprattutto con pipelining.
- Richiede **meno risorse** (soprattutto memoria).
- Più **complessa** da implementare, soprattutto con pipelining.
- La connessione può restare aperta anche inutilizzata: il server la chiude dopo un **timeout** di inattività.

**Non persistente**:

- **Facile** da implementare e coerente con la *statelessness* di HTTP.
- Richiede più risorse: per ogni connessione si allocano buffer TCP e variabili TCP sia al client sia al server.
- Più **lenta**: 1–2 RTT aggiuntivi per richiesta.
- Le connessioni non possono restare aperte.