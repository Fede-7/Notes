# Lezione 13: TCP — gestione della connessione

## Richiamo: responsabilità del livello di trasporto

I protocolli di trasporto (UDP e TCP) hanno quattro responsabilità principali: **consegna processo-a-processo** (i messaggi sono consegnati indipendentemente da dove sono i processi, diversamente dalla consegna host-a-host, responsabilità del protocollo IP di livello inferiore), **controllo di integrità** (campi di rilevamento errori negli header dei segmenti), **trasferimento affidabile** (dati consegnati correttamente e in ordine) e **controllo di congestione/flusso** (evita di saturare i dispositivi di rete; migliora le prestazioni ed è molto benefico per l'intera rete Internet). UDP fornisce solo i primi due servizi, TCP tutti e quattro.

## Richiamo: il segmento TCP

Il segmento TCP consiste di **campi di header** e un **campo dati** (al più MSS byte). L'**header** contiene:

- **Numero di sequenza** (32 bit) e **numero di acknowledgment** (32 bit), per il trasferimento affidabile.
- **Finestra di ricezione** (16 bit): byte che il ricevente è disposto ad accettare (controllo di flusso).
- **Lunghezza dell'header** (4 bit): numero di parole da 32 bit; l'header è variabile a causa delle opzioni.
- **Campo opzioni** (K bit): negoziazione dell'MSS, timestamping, ecc.
- **Flag** (6/12 bit): **ACK** (il segmento è un ACK), **RST, SYN, FIN** (instaurazione e chiusura della connessione), **CWR, ECE** (notifica esplicita di congestione, opzionale), **PSH** (passare subito i dati all'applicazione), **URG** (dati "urgenti").
- **Checksum** (16 bit): integrità.
- **Puntatore ai dati urgenti** (16 bit).

## Problemi di gestione della connessione TCP

Essendo orientato alla connessione, **due host devono accordarsi** sia nell'apertura sia nella chiusura. Poiché i messaggi possono **perdersi o danneggiarsi**, trovare questo accordo è piuttosto difficile: se i messaggi si perdono, **un capo della comunicazione può essere aperto/chiuso mentre l'altro no**. Per mitigare il problema TCP implementa il **three-way handshake**: le richieste di apertura/chiusura **devono essere confermate** prima che la connessione sia stabilita o rilasciata.

### Il problema dei due eserciti (two-army problem)

Si immagini un **esercito bianco accampato in una valle** e, sulle due colline, **due eserciti blu nemici**. L'esercito bianco è più grande di ciascun esercito blu, ma insieme i blu sono più forti: **vinceranno solo attaccando contemporaneamente**. Per sincronizzarsi, i blu devono **inviare messaggeri attraverso la valle**, dove possono essere catturati (comunicazione non affidabile).

Esiste un protocollo che permetta ai blu di vincere? Il comandante dell'esercito blu #1 manda: "Propongo di attaccare oggi, va bene?". Il messaggio arriva, il comandante #2 è d'accordo e la **risposta torna sana** al #1. L'attacco avverrà? Probabilmente no, perché **il comandante #2 non sa se la sua risposta è arrivata**: se non è arrivata, il #1 non attaccherà. Con un **three-way handshake** il primo comandante deve **confermare** la risposta, ma allora sarà il #1 a esitare (non sa se la conferma è arrivata); un four-way handshake non aiuterebbe. Si può dimostrare che **non esiste un protocollo che funzioni**: il **three-way handshake non è perfetto, ma di solito è adeguato**.

## Instaurazione della connessione TCP

In TCP si esegue il **three-way handshake** per stabilire la connessione: il client invia una **richiesta di connessione** (segmento SYN) al server, che risponde con uno **speciale acknowledgment** (segmento SYN-ACK); infine il client rimanda un **acknowledgment finale** (segmento ACK). L'instaurazione è una **procedura delicata** che può aggiungere ritardi significativi: c'è tipicamente un **timeout** (30-60 s) per completare l'handshake, dopo il quale la procedura è abortita, ed è proprio qui che avvengono alcuni **attacchi** (es. SYN flood).

### Dettagli del three-way handshake

1. Il client invia un **segmento SYN** con nessun dato applicativo (payload), bit SYN = 1 e un numero di sequenza iniziale casuale (`client_isn`).
2. Arrivato il SYN, il **server alloca buffer e variabili TCP** e invia un **segmento SYNACK** con nessun dato applicativo, bit SYN = 1 e ACK = 1, acknowledgment number = `client_isn + 1` e numero di sequenza iniziale casuale (`server_isn`).
3. Arrivato il SYNACK, anche **il client alloca buffer e variabili** e invia il **segmento ACK** finale, con eventuali dati applicativi, SYN = 0 (connessione stabilita) e ACK = 1, acknowledgment number = `server_isn + 1`.

## Rilascio della connessione TCP

Il rilascio (detto **teardown**) può essere avviato da ciascuno dei due host. Se chiude il client, l'handshake è:

1. Il client invia un **segmento speciale di chiusura** (segmento FIN) con bit FIN = 1.
2. Il server risponde con un segmento di **acknowledgment/chiusura**, con ACK = 1 e FIN = 1; ACK e FIN possono essere inviati nello stesso segmento o in due separati.
3. Infine il client **conferma** il segmento di chiusura del server.

### Gestione delle perdite nel rilascio

Poiché il three-way handshake non è perfetto, TCP si affida ai **timer** per chiudere prima o poi le connessioni o reinviare le richieste (ad esempio nella fase di rilascio della connessione).