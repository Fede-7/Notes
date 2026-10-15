# Application Layer posta e-mail e P2P

## Posta elettronica e SMTP

La posta elettronica è una delle applicazioni Internet più antiche e importanti; è tipicamente implementata in stile client-server con due tipi di host:

- **User agent**: applicazione per la gestione della posta da parte dell'utente (es. Pine, K-9 Mail).
- **Mail server**: server che **immagazzina le e-mail** e mantiene le **mailbox** specifiche degli utenti.

Diversamente da HTTP, qui la comunicazione avviene **anche tra server**: servono due protocolli, uno tra user agent e mail server e uno tra mail server e mail server.

> [!def] SMTP
> **Simple Mail Transfer Protocol**: principale protocollo di livello applicativo che lavora **tra mail server**; permette ai server di scambiarsi le e-mail, mentre gli user agent **non** usano SMTP.

- Gli utenti non si scambiano posta direttamente (come nella messaggistica istantanea): si preferiscono mail server, più affidabili e specializzati.
- Una volta arrivata sul server, la mail è memorizzata nella mailbox dell'utente, in attesa che l'user agent la scarichi localmente.
- In SMTP esistono un lato client (mittente) e un lato server (ricevente), entrambi sui mail server, che usano il protocollo affidabile **TCP**.

> [!example]
> Invio di una mail (Alice → Bob): il processo coinvolge l'agente di Alice, il mail server di Alice, l'agente di Bob e il mail server di Bob.
> 
> 1. Alice invoca il suo user agent, fornisce l'indirizzo di Bob, compone il messaggio e ordina l'invio.
> 2. L'agente invia il messaggio al mail server di Alice, dove viene posto in una **coda dei messaggi**.
> 3. Il lato client SMTP del server di Alice vede il messaggio in coda e apre una connessione TCP verso il server SMTP sul mail server di Bob.
> 4. Dopo un handshaking iniziale, il client SMTP invia il messaggio nella connessione TCP.
> 5. Il lato server SMTP del server di Bob riceve il messaggio e lo colloca nella mailbox di Bob.
> 6. Bob invoca il suo user agent e legge il messaggio quando vuole.

Dettagli del protocollo:

- Il client SMTP stabilisce una connessione TCP alla **porta 25** del server SMTP; se il server è giù, il client **riprova più tardi**.
- Stabilita la connessione, client e server eseguono un handshaking di livello applicativo: **si presentano** prima di trasferire informazioni.
- Durante l'handshaking il client SMTP indica l'indirizzo e-mail del mittente e quello del ricevente.
- SMTP conta sul servizio di trasferimento affidabile di TCP per consegnare il messaggio al server senza errori.

## Accesso alla posta

Il deployment di server SMTP è più affidabile dello scambio utente-utente diretto: i server sono sempre accesi e visibili in rete, certificati, e possono ritentare l'invio in continuazione (processo computazionalmente costoso).

Per accedere alle mail sul server serve però un'applicazione client-server aggiuntiva con un protocollo diverso. I più diffusi:

- **POP3** (*Post Office Protocol* version 3).
- **IMAP** (*Internet Mail Access Protocol*).
- **HTTP**.

### POP3

> [!def] POP3
> **Protocollo di accesso alla posta estremamente semplice**: l'user agent (client) apre una connessione TCP al mail server sulla **porta 110**.

Con la connessione stabilita, POP3 procede in tre fasi:

1. **Authorization**: l'user agent invia username e password per autenticare l'utente.
2. **Transaction**: l'user agent può recuperare i messaggi, marcarli per la cancellazione, rimuovere i segni di cancellazione e ottenere statistiche sulla posta.
3. **Update**: dopo il comando `quit` che chiude la sessione, il server **elimina i messaggi marcati** per la cancellazione.

### IMAP

Con POP3 i messaggi possono solo essere scaricati o cancellati: azioni come cercare o organizzare le mail in cartelle non sono previste e vanno fatte sulla macchina locale.

> [!def] IMAP
> **Internet Mail Access Protocol**: protocollo di accesso che permette al server di fornire funzionalità aggiuntive rispetto a POP3.

- **Gestione e creazione di cartelle**.
- **Ricerca** nelle cartelle remote di messaggi che rispettano criteri specifici.
- Ottenimento di **solo parti** dei messaggi (es. solo header, solo allegati).
- **Client multipli** connessi contemporaneamente allo stesso server.

### Accesso via HTTP

- Sempre più utenti inviano e leggono posta tramite **browser Web**: l'accesso web-based è stato introdotto da Hotmail a metà anni '90 ed è oggi l'approccio dominante (Google, Yahoo!, Virgilio, ecc.), usato da quasi tutte le università e aziende.
- L'user agent è un comune browser che comunica con la mailbox remota via **HTTP** anziché POP3 o IMAP.
- Vale per gli user agent: **i mail server continuano a usare SMTP** per scambiarsi i messaggi.

## Peer-to-Peer

> [!def] Architettura P2P
> **Architettura** che fa uso minimo (o nullo) di server: coppie di host connessi intermittentemente (**peer**) comunicano **direttamente** tra loro; i peer non sono di proprietà di un fornitore di servizi, ma desktop e laptop controllati dagli utenti.

Il file sharing è l'applicazione naturale:

- Nel client-server il server deve distribuire i file a tutti i client: grave onere per il server, che richiede grande banda.
- Nel P2P i peer che ricevono il file possono **condividerlo a loro volta** con altri peer: in qualche modo i peer sono client e server allo stesso tempo.
- Il P2P scala tipicamente **meglio** del client-server nel file sharing, ma è più complesso da implementare e ha problemi di **sicurezza**, con tutti questi client in comunicazione diretta.

## BitTorrent

> [!def] BitTorrent
> **Protocollo P2P** popolare per la condivisione/distribuzione di file (utenti stimati 150–170 milioni nel 2023); definisce il comportamento di un **torrent**.

- Un **torrent** è l'insieme dei peer che partecipano alla distribuzione di un file; i peer si scaricano l'un l'altro **chunk** di uguali dimensioni del file (tipicamente 256 kB).
- Un peer che entra nel torrent senza chunk inizia ad accumularne; mentre scarica chunk, **carica** chunk verso gli altri peer.
- Ottenuto il file completo, il peer può lasciare il torrent (egoisticamente) o restare e continuare a caricare (altruisticamente); i peer possono uscire in qualsiasi momento con un sottoinsieme di chunk e rientrare più tardi.

### Il tracker

- Ogni torrent ha un nodo di infrastruttura chiamato **tracker**, che tiene traccia dei peer partecipanti (i tracker sono di fatto server).
- Un nuovo peer si **registra** col tracker e lo informa periodicamente del proprio stato; il tracker gli fornisce gli **indirizzi IP** di un sottoinsieme casuale di peer del torrent.
- Il nuovo host tenta connessioni TCP **concorrenti** con tutti i peer della lista (**vicini**); durante l'esecuzione alcuni vicini possono uscire, mentre altri peer (fuori dalla lista iniziale) possono tentare nuove connessioni.
- In ogni istante ogni peer possiede un sottoinsieme di chunk, diverso da peer a peer; **periodicamente** ogni host chiede a ciascun vicino connesso (sulle connessioni TCP) la **lista dei chunk** che possiede.

### Strategie del client

Il client in download decide quali chunk richiedere (e a chi) secondo il principio **rarest-first**: hanno priorità i chunk con **meno copie ripetute** tra i vicini; così i chunk più rari vengono ridistribuiti più rapidamente e il numero di copie nel torrent si equalizza.

Il client in upload decide quali richieste servire secondo due principi intrecciati:

- **Trading**: il host da priorità ai **4 migliori vicini** che stanno fornendo dati alla massima velocità; il controllo avviene periodicamente (ogni 10 secondi) e la lista dei 4 migliori si aggiorna di conseguenza.
- **Random selection (optimistic unchoking)**: ogni 30 secondi ogni host sceglie anche **un vicino a caso** e gli invia chunk; se lo scambio casuale risulta buono (i due host sono buoni partner), entrano nelle rispettive liste dei migliori; il processo permette ai peer con velocità di upload compatibili di **trovarsi**.