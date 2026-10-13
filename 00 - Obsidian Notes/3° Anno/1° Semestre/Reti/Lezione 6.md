# Lezione 6: E-mail, P2P, BitTorrent

## Posta elettronica e SMTP

La posta elettronica è una delle applicazioni Internet più antiche e importanti, ed è tipicamente implementata in modalità client-server con due tipi di host: lo **user agent**, l'applicazione per la gestione della posta (es. Pine, K-9 Mail), e il **mail server**, il server che archivia le mail e gestisce le cassette postali (*mailbox*) degli utenti. Diversamente da HTTP, qui la comunicazione avviene anche **tra server**, quindi servono due applicazioni/protocolli: uno tra user agent e mail server, e uno tra mail server e mail server. Gli utenti non si scambiano le mail direttamente (come nella messaggistica istantanea), perché è preferibile usare mail server più affidabili e specializzati.

Il **Simple Mail Transfer Protocol** (SMTP) è il principale protocollo applicativo tra mail server: permette ai server di scambiarsi le mail, mentre **gli user agent non usano SMTP**. Arrivata sul server, una mail è archiviata nella **mailbox dell'utente**, in attesa di essere scaricata dallo user agent. In SMTP esistono un lato **client** (mittente) e un lato **server** (ricevente), entrambi su mail server, che usano l'affidabile **TCP** per trasferire la posta.

### Scenario tipico

Quando l'host A (Alice) invia un'e-mail all'host B (Bob) sono coinvolti quattro elementi: lo user agent di Alice, il mail server di Alice, lo user agent di Bob e il mail server di Bob. Il processo funziona così:

1. Alice **invoca il suo user agent**, fornisce l'indirizzo e-mail di Bob (es. bob@someschool.edu), compone il messaggio e chiede all'user agent di inviarlo.
2. Lo **user agent di Alice invia il messaggio al suo mail server**, dove viene messo in una coda di messaggi.
3. Il lato client SMTP del server di Alice vede il messaggio in coda e **apre una connessione TCP** verso un server SMTP sul mail server di Bob.
4. Dopo un handshaking SMTP iniziale, il client SMTP invia il messaggio di Alice **nella connessione TCP**.
5. Sul server di Bob, **il lato server SMTP riceve il messaggio** e lo colloca nella **mailbox di Bob**.
6. Bob **invoca il suo user agent** per leggere il messaggio quando vuole.

### Dettagli della connessione

Il client SMTP (sul server mittente) **stabilisce una connessione TCP alla porta 25** del server SMTP (sul server ricevente); se il server è giù, il client riprova più tardi. Stabilita la connessione, **server e client eseguono un handshaking a livello applicazione**, presentandosi prima di trasferire informazioni: durante l'handshaking il client SMTP indica l'indirizzo e-mail del mittente e quello del destinatario. SMTP può contare sul **servizio di trasferimento affidabile di TCP** per consegnare il messaggio al server senza errori.

## Accesso alla posta

Il deployment di server SMTP è **più affidabile** rispetto alla posta diretta utente-utente: i server sono, per definizione, sempre accesi e visibili a tutti i dispositivi della rete, sono certificati, e possono ritentare continuamente l'invio in caso di fallimento (un processo computazionalmente costoso). D'altro canto, per accedere alle mail sul server serve **un'applicazione client-server aggiuntiva** con un protocollo diverso; i più diffusi sono il **Post Office Protocol - Versione 3** (POP3), l'**Internet Mail Access Protocol** (IMAP) e **HTTP**.

### POP3

POP3 è un protocollo di accesso alla posta estremamente semplice. Lo user agent (client) apre una **connessione TCP** al mail server sulla porta 110; stabilita la connessione, POP3 procede in tre fasi:

1. **Autorizzazione**: lo user agent invia username e password per autenticare l'utente.
2. **Transazione**: lo user agent può recuperare i messaggi, marcarli per la cancellazione, rimuovere i marcatori, ottenere statistiche sulla posta.
3. **Aggiornamento**: dopo il comando *quit* che chiude la sessione, il mail server **elimina i messaggi** marcati per la cancellazione.

### IMAP

Con POP3 i messaggi possono solo essere scaricati o cancellati: azioni come cercare o organizzare la posta in cartelle non sono previste e vanno fatte in locale. L'**Internet Mail Access Protocol** (IMAP) permette invece ai server di offrire funzionalità aggiuntive:

- Gestione e **creazione di cartelle**.
- **Ricerca** nelle cartelle remote di messaggi che corrispondono a criteri specifici.
- Ottenere solo parti dei messaggi (es. solo header, solo allegati).
- Connettere **più client** allo stesso server.

### Accesso via HTTP

Sempre più utenti inviano e leggono e-mail tramite il **browser**: l'accesso Web via HTTP fu introdotto da Hotmail a metà anni '90 ed è ora l'approccio dominante (Google, Yahoo!, Virgilio, ecc.), usato da quasi tutte le università e le grandi aziende. Con questo servizio **lo user agent è un normale browser**, e l'utente comunica con la propria mailbox remota via HTTP anziché via POP3 o IMAP; per lo scambio dei messaggi, invece, **i mail server restano sullo standard SMTP**.

## Peer-to-peer

Diversamente dal client-server, l'architettura P2P fa un uso minimo (o nullo) di server: ci sono **coppie di host connessi intermittentemente** (peer) che comunicano direttamente tra loro. I peer **non sono di proprietà di un provider**, ma sono desktop e laptop controllati dagli utenti. Un'applicazione naturale del P2P è la **condivisione di file**: nel client-server il server deve condividere i file con tutti i client (un grave carico, con esigenze di banda elevate), mentre nel P2P i peer che ricevono il file possono a loro volta **condividerlo con altri peer**, essendo in un certo senso client e server allo stesso tempo. Nel file sharing l'approccio P2P tipicamente **scala meglio** di quello client-server; d'altro canto può essere piuttosto **complesso da implementare**, e possono esserci **problemi di sicurezza** nell'avere tutti questi client in comunicazione diretta.

## BitTorrent

**BitTorrent** è un protocollo P2P popolare per la condivisione e distribuzione di file, con 150-170 milioni di utenti stimati (nel 2023). Un **torrent** è l'insieme di tutti i peer che partecipano alla distribuzione di un particolare file; i peer in un torrent scaricano l'uno dall'altro **blocchi (chunk) di pari dimensione** (dimensione tipica: 256 kbyte). Quando un peer entra in un torrent (senza chunk), inizia **accumulando chunk** e, mentre li scarica, **li carica anche verso altri peer**; una volta **ottenuto l'intero file**, può egoisticamente **uscire dal torrent**, oppure altruisticamente **restare** e continuare a caricare chunk verso altri peer. I peer possono **uscire dal torrent in qualunque momento** con un sottoinsieme di chunk e rientrarvi più tardi.

### Il tracker

Ogni torrent ha un nodo di infrastruttura chiamato **tracker** che tiene traccia dei peer partecipanti (i tracker sono in pratica server). Quando un **nuovo peer** entra nel torrent, si **registra** presso il tracker e **periodicamente lo informa** del proprio stato; il tracker **fornisce gli indirizzi IP** di un sottoinsieme casuale di peer del torrent. Ottenuta la lista, il nuovo host cerca di aprire **connessioni TCP simultanee con tutti i peer della lista** (i vicini); durante l'esecuzione, alcuni peer connessi possono uscire, mentre altri (fuori dalla lista iniziale) possono cercare di aprire nuove connessioni. In ogni istante ciascun peer ha **un sottoinsieme dei chunk**, con peer diversi che hanno sottoinsiemi diversi; periodicamente un host chiede a ciascun peer connesso (via TCP) **la lista dei chunk che possiede**.

### Il client BitTorrent

Il **client in download** decide quali chunk richiedere (e a chi) seguendo il principio *rarest-first*: vengono prioritizzati i chunk con **meno copie** tra i vicini, così i **chunk più rari vengono ridistribuiti più velocemente**, in modo da grossolanamente pareggiare il numero di copie nel torrent. Il **client in upload** decide invece quali richieste servire seguendo due principi intrecciati:

- **Trading**: l'host dà priorità ai migliori 4 vicini che in quel momento forniscono dati alla velocità più alta; la verifica è periodica (10 secondi) e la lista dei 4 migliori viene aggiornata.
- **Selezione casuale**: ogni 30 secondi l'host sceglie anche **un vicino aggiuntivo a caso** e gli invia chunk. Se questo scambio casuale va bene (i due host sono buoni partner), entrano nelle rispettive liste dei migliori; questo processo permette anche a peer con velocità di upload compatibili di trovarsi.