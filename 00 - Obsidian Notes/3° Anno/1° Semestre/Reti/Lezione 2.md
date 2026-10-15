# Internet protocolli e livelli

## Vista "nuts and bolts" di Internet

Dalla prospettiva dell'implementazione, Internet è composta da:

- **Host** (o *end systems*): miliardi di dispositivi connessi che eseguono le applicazioni di rete al "bordo" di Internet.
- **Packet switch**: dispositivi che inoltrano pacchetti (blocchi di dati), principalmente router e switch.
- **Link di comunicazione**: fibra, rame, radio, satellite; il tasso di trasmissione è la **banda**.
- **Reti**: insiemi di dispositivi, router e link gestiti da un'organizzazione.

> [!info] Internet
> Internet è una **rete di reti** di ISP interconnessi, in cui i protocolli sono ovunque: governano l'invio e la ricezione dei messaggi (es. HTTP, streaming video, TCP, IP, WiFi, 4G, Ethernet).

Dalla prospettiva dei servizi, Internet è un'**infrastruttura** che offre servizi alle applicazioni (Web, e-mail, e-commerce, social, ...) e fornisce una **interfaccia di programmazione** alle applicazioni distribuite: "agganci" per connettersi al servizio di trasporto, con opzioni di servizio analoghe al servizio postale.

## Protocolli e standard

> [!def] Protocollo di rete
> **Insieme di regole** che definisce il *formato*, l'*ordine* dei messaggi scambiati tra le entità di rete e le *azioni* intraprese alla trasmissione e alla ricezione dei messaggi.

I protocolli umani (domande, presentazioni) e i protocolli di rete condividono la stessa struttura: messaggi specifici inviati e azioni specifiche compiute alla ricezione di un messaggio o di un altro evento; nei protocolli di rete, però, le entità sono computer.

Gli standard di Internet sono definiti da una comunità di esperti:

- **IETF** (*Internet Engineering Task Force*): organizzata in **working group** aperti, ciascuno focalizzato su un aspetto specifico di Internet.
- **RFC** (*Request For Comments*): documenti numerati prodotti dai working group, con descrizione e definizione di protocolli, concetti e metodi alla base di uno standard (es. IPv4 è definito nell'RFC 791, 1981).

## Il modello a livelli

> [!def] Layering
> **Approccio architetturale** alla comunicazione: il sistema è diviso in livelli (*divide et impera*), ciascuno un livello di astrazione che **usa i servizi del livello inferiore e offre servizi al livello superiore** attraverso interfacce.

Il modello a livelli serve a domare la complessità della rete (host, router, link eterogenei, applicazioni, protocolli, hardware e software):

- La struttura esplicita permette di **identificare** e mettere in relazione i pezzi del sistema complesso.
- La **modularizzazione** facilita manutenzione e aggiornamento: cambiare l'implementazione del servizio di un livello è trasparente al resto del sistema.
- **Contro**: il layering ha un costo in efficienza ("*layering considered harmful*").

Quando due dispositivi comunicano, **ogni livello del mittente comunica con lo stesso livello del destinatario** mediante un protocollo specifico.

## Servizi di connessione e affidabilità

> [!def] Servizio connection-oriented
> **Servizio orientato alla connessione** modellato sul sistema telefonico: l'utente prima **stabilisce** la connessione, la usa, poi la rilascia; può negoziare i parametri da usare.

> [!def] Servizio connectionless
> **Servizio senza connessione** modellato sul sistema postale: i pacchetti vengono inviati indipendentemente, senza setup.

Alcune nozioni collegate:

- **Pacchetto** (*packet*): un messaggio al livello di rete.
- **Store-and-forward switching**: i nodi intermedi ricevono il messaggio per intero prima di inoltrarlo al nodo successivo.
- **Cut-through switching**: la trasmissione presso un nodo inizia prima che il messaggio sia ricevuto completamente.
- **Servizio datagram**: servizio connectionless non affidabile (senza conferme).
- L'**affidabilità** caratterizza sia i servizi orientati sia quelli non orientati alla connessione.

I sei servizi tipici orientati e non orientati alla connessione sono i seguenti.

| Tipo | Servizio | Esempio |
|---|---|---|
| Connection-oriented | Reliable message stream | Sequenza di pagine |
| Connection-oriented | Reliable byte stream | Download di un film |
| Connection-oriented | Unreliable connection | Voice over IP |
| Connectionless | Unreliable datagram | Posta elettronica di massa |
| Connectionless | Acknowledged datagram | Messaggistica testuale |
| Connectionless | Request-reply | Interrogazione di database |

## Il modello ISO/OSI

![[Lezione 2-1790359871813.png|300]]

Negli anni '80 l'**ISO** (*International Standards Organization*) ha definito il modello a livelli **OSI** (*Open System Interconnection*), con 7 livelli:

### 1. Livello fisico

Il **livello fisico** è responsabile del movimento dei singoli bit da un hop (nodo) al successivo. Regola le caratteristiche fisiche di interfacce e mezzi (connettori, cavi, segnali elettrici), la configurazione della linea (punto-punto o multipunto), la topologia fisica (mesh, star, ring o bus), la modalità di trasmissione (simplex, half-duplex o duplex), la rappresentazione dei bit, la velocità di trasmissione (*data rate*) e la sincronizzazione dei bit.

![[Lezione 2-1790458351461.png|300]]

### 2. Livello data link

Il **livello data link** è responsabile del movimento dei frame da un hop al successivo (segmento). Lavora su frame, porzioni di dati tipicamente di poche centinaia di byte, e si occupa di controllo di flusso ed errori (tramite sequenze di controllo del frame) e di controllo di accesso.

![[Lezione 2-1790359763877.png|300]]

### 3. Livello di rete

Il **livello di rete** è responsabile della consegna dei singoli pacchetti dall'host sorgente all'host destinazione (cammino). Lavora su pacchetti, tipicamente più grandi e complessi dei frame, e gestisce la consegna da sorgente a destinazione, l'indirizzamento logico e il routing tramite tabelle di routing.

![[Lezione 2-1790359770150.png|300]]

### 4. Livello di trasporto

Il **livello di trasporto** è responsabile della consegna di un messaggio da un estremo all'altro, così che il messaggio arrivi al programma giusto. Si occupa di consegna end-to-end, controllo della connessione (orientato o senza connessione), segmentazione/riassemblaggio da e verso i pacchetti del livello 3, indirizzamento delle porte e controllo di flusso ed errori.

![[Lezione 2-1790359803876.png|300]]

### 5. Livello di sessione

Il **livello di sessione** è responsabile del controllo del dialogo e della sincronizzazione richiesta/risposta: stabilisce, mantiene e sincronizza l'interazione tra i sistemi che comunicano (sessione di comunicazione), gestisce il dialogo e prevede punti di controllo (*checkpoint*) per la sincronizzazione.

![[Lezione 2-1790359808584.png|300]]

### 6. Livello di presentazione

Il **livello di presentazione** è responsabile della rappresentazione dei dati: si occupa di traduzione (ad esempio da codifica EBCDIC o ASCII a testo), cifratura e decifratura, e compressione.

![[Lezione 2-1790359825642.png|300]]

### 7. Livello applicazione

Il **livello applicazione** è responsabile di fornire servizi all'utente: terminale virtuale di rete (accesso remoto), trasferimento e accesso a file, servizi di posta e accesso al World Wide Web.

![[Lezione 2-1790359815636.png|300]]


Non sempre tutti i livelli sono implementati: nei nodi intermedi (switch, router) sono implementati solo 2–3 livelli (livelli "media"), mentre solo i sistemi finali implementano l'intero stack fino all'applicazione.

## Incapsulamento

> [!def] Incapsulamento
> **Processo top-down** in cui ogni livello del mittente aggiunge al messaggio (payload) un campo proprio del livello, come **header** (`H`) o **trailer** (`T`); la **decapsulazione** (bottom-up) rimuole e interpreta quei campi negli stessi livelli del ricevente.

## Critiche e confronto TCP/IP vs OSI

> [!info] Critiche al modello OSI
> **Bad timing** (i protocolli TCP/IP concorrenti erano già in uso), **bad design** (modello e protocolli difettosi), **bad implementations** (implementazioni iniziali enormi e lente), **bad politics** (visto come creatura dei ministeri telecom europei).

Critiche al modello TCP/IP:

- Non distingue chiaramente i concetti di **servizi, interfacce e protocolli**.
- Non è generale: poco adatto a descrivere altri stack di protocolli.
- Il **link layer** non è un vero livello; non distingue il livello fisico dal data link.
- Le altre implementazioni di protocolli erano distribuite gratuitamente.

Confronto:

- **ISO/OSI** è *de iure* lo stack standard per le reti di calcolatori, ma è complesso e dettagliato.
- **TCP/IP e UDP/IP** (*Internet Protocol Suite*) sono *de facto* lo stack realmente usato su Internet e nelle reti locali: **TCP** (*Transmission Control Protocol*), **UDP** (*User Datagram Protocol*), **IP** (*Internet Protocol*).

Esistono altri modelli di rete per la comunicazione tra dispositivi, dipendenti dalla situazione, che però restano basati sul modello a livelli.