# Lezione 2: Internet, protocolli e livelli

## Le due visioni di Internet

Internet può essere descritta in due modi complementari. Nella visione "concreta" (*nuts and bolts*) essa è costituita da miliardi di **dispositivi di calcolo connessi**: gli **host** (o sistemi finali, *end system*) eseguono applicazioni di rete al bordo (*edge*) di Internet, mentre i **commutatori di pacchetti** (*packet switch*), come router e switch, inoltrano blocchi di dati chiamati pacchetti. I dispositivi sono collegati da **collegamenti di comunicazione** di vario mezzo (fibra, rame, radio, satellite), ciascuno caratterizzato dalla propria **banda** (velocità di trasmissione). Un'ultima componente è l'insieme delle **reti**: insiemi di dispositivi, router e link gestiti da un'organizzazione. Tra i dispositivi oggi connessi si va ben oltre i PC: assistenti vocali, elettrodomestici, telecamere, pacemaker, dispositivi indossabili e tostapane connessi.

Nella visione "dei servizi", invece, Internet è un'**infrastruttura che fornisce servizi alle applicazioni**: Web, video in streaming, teleconferenze, e-mail, giochi, e-commerce e social media. Fornisce inoltre un'*interfaccia di programmazione* alle applicazioni distribuite, ossia degli "agganci" (*hook*) che permettono alle applicazioni che inviano e ricevono di connettersi a Internet e usare il servizio di trasporto, con opzioni di servizio analoghe a quelle del servizio postale.

## Protocolli

### Dai protocolli umani ai protocolli di rete

I protocolli umani — come chiedere l'ora o presentarsi — consistono nell'inviare messaggi specifici e nel compiere azioni specifiche alla ricezione di un messaggio o in risposta ad altri eventi. I **protocolli di rete** seguono lo stesso schema, ma coinvolgono calcolatori anziché esseri umani: tutta l'attività di comunicazione in Internet è governata da protocolli. Un protocollo definisce il **formato e l'ordine dei messaggi** scambiati tra le entità di rete, e le **azioni compiute** alla trasmissione e alla ricezione dei messaggi.

### Chi definisce gli standard

Gli standard e i protocolli di Internet sono definiti da una comunità di esperti, la **Internet Engineering Task Force** (IETF), organizzata in gruppi di lavoro aperti, ciascuno dedicato ad aspetti specifici di Internet. Ogni gruppo produce documenti numerati chiamati **Request For Comments** (RFC), che descrivono e definiscono protocolli, concetti e metodi alla base di uno standard: ad esempio il protocollo IPv4 è stato definito nell'RFC 791 (1981).

## Il modello a livelli

Le reti sono sistemi complessi: host, router, link di vario mezzo, applicazioni, protocolli, hardware e software. Per dominare questa complessità si ricorre a un approccio architetturale chiamato **modello a livelli**, una strategia *divide et impera* in cui ogni livello costituisce un livello di astrazione: ogni livello si appoggia sui servizi del livello inferiore e fornisce servizi al livello superiore, attraverso interfacce ben definite, dal livello alto (le applicazioni) verso quello basso (l'hardware).

Il layering è la chiave per gestire sistemi complessi. Una struttura esplicita permette di identificare le componenti del sistema e le loro relazioni, fornendo così un modello di riferimento per la discussione; la **modularizzazione**, inoltre, facilita manutenzione e aggiornamento, poiché un cambiamento nell'*implementazione* del servizio di un livello è trasparente al resto del sistema. Va notato che il layering può avere un costo in termini di efficienza, e che strutture a livelli esistono anche in molti altri sistemi complessi. Le entità usano i protocolli per implementare le proprie definizioni di servizio; quando due dispositivi comunicano, ogni livello del mittente comunica con lo stesso livello del destinatario tramite un protocollo specifico.

## Connessioni e affidabilità

### Servizio orientato alla connessione

Il servizio orientato alla connessione è modellato sul sistema telefonico: l'utente stabilisce prima una connessione, la usa, poi la rilascia, e durante l'instaurazione può condurre una negoziazione sui parametri da usare.

### Servizio senza connessione

Il servizio senza connessione è modellato sul sistema postale, dove il pacchetto è un messaggio al livello di rete. Lo scambio può avvenire in due modi: con **store-and-forward switching** i nodi intermedi ricevono il messaggio per intero prima di inoltrarlo al nodo successivo, mentre con **cut-through switching** la trasmissione da un nodo inizia prima che il nodo abbia ricevuto completamente il messaggio. Il **servizio datagram** è un servizio senza connessione non affidabile, cioè privo di *acknowledgement*. L'affidabilità, in generale, caratterizza sia i servizi orientati alla connessione sia quelli senza connessione.

#### Sei servizi comuni

| Tipo | Servizio | Esempio |
| --- | --- | --- |
| Orientato alla connessione | Flusso di messaggi affidabile | Sequenza di pagine |
| Orientato alla connessione | Flusso di byte affidabile | Download di un film |
| Orientato alla connessione | Connessione non affidabile | Voice over IP |
| Senza connessione | Datagram non affidabile | Posta elettronica spazzatura |
| Senza connessione | Datagram confermato | Messaggistica testuale |
| Senza connessione | Richiesta-risposta | Query su database |

## Il modello OSI

Negli anni '80 la ISO (*International Standards Organization*) definì un modello a livelli per le reti di calcolatori: il modello **OSI** (*Open System Interconnection*), composto da 7 livelli, che vanno dalla trasmissione fisica dei bit "grezzi" (livello 1) fino all'uso dei dati e all'interazione uomo-macchina (livello 7). I livelli intermedi si occupano, nell'ordine, del formato dei dati (frame), dell'instradamento dei messaggi, dei protocolli di trasmissione, della gestione delle porte e delle sessioni, e della traduzione dei messaggi (codifica, compressione, decifratura).

Non sempre tutti i livelli sono implementati: tipicamente nei nodi intermedi (switch, router) sono implementati solo 2 o 3 livelli (i livelli dei mezzi), mentre solo gli endpoint implementano l'intero stack fino ai livelli applicativi. La comunicazione tra livelli segue due meccanismi speculari: con l'**incapsulamento** (*top-down*) ogni livello del mittente aggiunge al messaggio (payload) un campo proprio, sotto forma di header (H) o trailer (T); con il **decapsulamento** (*bottom-up*) quei campi sono rimossi e interpretati dallo stesso livello nel destinatario.

### 1. Livello fisico

Il **livello fisico** è responsabile del movimento dei singoli bit da un hop (nodo) al successivo. Regola le caratteristiche fisiche di interfacce e mezzi (connettori, cavi, segnali elettrici), la configurazione della linea (punto-punto o multipunto), la topologia fisica (mesh, star, ring o bus), la modalità di trasmissione (simplex, half-duplex o duplex), la rappresentazione dei bit, la velocità di trasmissione (*data rate*) e la sincronizzazione dei bit.

### 2. Livello data link

Il **livello data link** è responsabile del movimento dei frame da un hop al successivo (segmento). Lavora su frame, porzioni di dati tipicamente di poche centinaia di byte, e si occupa di controllo di flusso ed errori (tramite sequenze di controllo del frame) e di controllo di accesso.

### 3. Livello di rete

Il **livello di rete** è responsabile della consegna dei singoli pacchetti dall'host sorgente all'host destinazione (cammino). Lavora su pacchetti, tipicamente più grandi e complessi dei frame, e gestisce la consegna da sorgente a destinazione, l'indirizzamento logico e il routing tramite tabelle di routing.

### 4. Livello di trasporto

Il **livello di trasporto** è responsabile della consegna di un messaggio da un estremo all'altro, così che il messaggio arrivi al programma giusto. Si occupa di consegna end-to-end, controllo della connessione (orientato o senza connessione), segmentazione/riassemblaggio da e verso i pacchetti del livello 3, indirizzamento delle porte e controllo di flusso ed errori.

### 5. Livello di sessione

Il **livello di sessione** è responsabile del controllo del dialogo e della sincronizzazione richiesta/risposta: stabilisce, mantiene e sincronizza l'interazione tra i sistemi che comunicano (sessione di comunicazione), gestisce il dialogo e prevede punti di controllo (*checkpoint*) per la sincronizzazione.

### 6. Livello di presentazione

Il **livello di presentazione** è responsabile della rappresentazione dei dati: si occupa di traduzione (ad esempio da codifica EBCDIC o ASCII a testo), cifratura e decifratura, e compressione.

### 7. Livello applicazione

Il **livello applicazione** è responsabile di fornire servizi all'utente: terminale virtuale di rete (accesso remoto), trasferimento e accesso a file, servizi di posta e accesso al World Wide Web.

## Critiche ai modelli

### Critiche al modello OSI

Il modello OSI fu criticato su più fronti: il **tempismo** era sbagliato, poiché i protocolli concorrenti TCP/IP erano già in uso diffuso; il **progetto** era scadente, con difetti sia nel modello sia nei protocolli; le prime **implementazioni** erano enormi, ingombranti e lente; e la **politica** lo vedeva diffusamente come creatura dei ministeri europei delle telecomunicazioni e dei governi. Per evitare il "tempismo sbagliato", è essenziale che gli standard vengano scritti nell'incavo tra le creste delle due "onde degli elefanti".

### Critiche al modello TCP/IP

Anche il modello TCP/IP ha difetti: non distingue chiaramente i concetti di **servizi, interfacce e protocolli**; non è affatto generale, quindi è poco adatto a descrivere qualunque altro stack di protocolli; il **livello link** non è davvero un livello nel senso normale del termine; e il modello non distingue tra livello fisico e data link. A ciò si aggiunge il fatto che altre implementazioni di protocolli erano distribuite gratuitamente.

### TCP/IP vs OSI

Il modello ISO/OSI è lo stack standard *de iure* per le reti di calcolatori, ma è piuttosto complesso e dettagliato. TCP/IP e UDP/IP (detti *Internet Protocol Suite*) sono invece l'insieme di protocolli di comunicazione effettivamente usati su Internet e nelle reti locali — TCP (*Transmission Control Protocol*), UDP (*User Datagram Protocol*) e IP (*Internet Protocol*) — e costituiscono quindi lo stack standard *de facto* per la comunicazione su Internet. Esistono infine diversi altri protocolli per la comunicazione tra dispositivi, usabili a seconda della situazione, che si basano comunque sul modello a livelli.