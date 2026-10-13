# Lezione 10: Il livello di trasporto

## Dal livello applicazione al livello di trasporto

Un protocollo di trasporto fornisce soprattutto **comunicazione logica tra processi applicativi** su host diversi: dal punto di vista dell'applicazione, gli host che eseguono i processi **sembrano direttamente connessi**, come sulla stessa macchina, anche se sono ai lati opposti del pianeta. Il **livello di trasporto converte i messaggi applicativi** in uno o più pacchetti di trasporto, detti **segmenti** o **datagram** (quest'ultimo termine soprattutto per i pacchetti UDP): se i messaggi sono spezzati in blocchi più piccoli, ogni blocco riceve un header di trasporto, e i segmenti sono passati uno a uno al livello di rete per la trasmissione.

## Responsabilità del livello di trasporto

I protocolli di trasporto (UDP e TCP) hanno quattro responsabilità principali:

1. **Consegna processo-a-processo**: i messaggi sono consegnati indipendentemente da dove sono i processi; è diverso dalla consegna **host-a-host** (tra macchine), che è responsabilità del protocollo IP di livello inferiore.
2. **Controllo di integrità**: tramite campi di rilevamento errori negli header dei segmenti.
3. **Trasferimento affidabile dei dati**: garantire che i dati arrivino dal processo mittente a quello ricevente, corretti e in ordine.
4. **Controllo di congestione/flusso**: evita che una connessione saturi i dispositivi di rete (link o router) con troppo traffico; è utile per le prestazioni e **molto benefico per l'intera rete Internet**.

UDP (più veloce ma semplice) fornisce **solo i primi due servizi**; TCP fornisce tutti e quattro.

## Consegna processo-a-processo

A livello applicazione **più processi possono accedere alla rete contemporaneamente** (ascoltare musica, scaricare file, navigare, tutti insieme), e un singolo processo può essere collegato a più processi contemporaneamente (es. proxy server, mail server). Per risolvere questi problemi si usano i socket per la consegna processo-a-processo: invece di consegnare il messaggio direttamente a un processo, **i socket sono gli endpoint da cui i processi prendono i messaggi**. Questo approccio **disaccoppia** il numero di processi dal numero di connessioni.

Poiché nell'host ricevente ci sono più socket, servono un **identificatore univoco** per ogni socket (la **porta**) da allegare ai segmenti ricevuti, e un processo di **multiplazione/demultiplazione** (*multiplexing/demultiplexing*) su mittente e ricevente. La **demultiplazione** reindirizza un segmento al socket giusto in base all'identificatore associato, mentre la **multiplazione** crea segmenti da processi diversi, assegnando l'identificatore giusto. Multiplazione e demultiplazione sono presenti anche in altri livelli, perché il problema di reindirizzare messaggi a più sorgenti è comune nelle reti.

## Porte

Gli identificatori dei socket sono dette porte sorgente e destinazione: una **porta è un numero a 16 bit** da 0 a 65535, e le porte **da 0 a 1023 sono dette "well-known"** perché riservate ai protocolli applicativi noti. La **lista delle porte note** è aggiornata da **IANA** (*Internet Assigned Numbers Authority*); sviluppando una nuova applicazione di rete, occorre assegnare le porte ai socket (e quindi alle applicazioni) di conseguenza.

| Porta | Uso |
| --- | --- |
| 20 | File Transfer Protocol (FTP) — trasferimento dati |
| 21 | FTP — controllo comandi |
| 22 | Secure Shell (SSH) |
| 23 | Telnet — accesso remoto, messaggi in chiaro |
| 25 | Simple Mail Transfer Protocol (SMTP) — instradamento e-mail |
| 53 | Domain Name System (DNS) |
| 80 | Hypertext Transfer Protocol (HTTP), Web |
| 110 | Post Office Protocol (POP3) — recupero e-mail dal server |
| 119 | Network News Transfer Protocol (NNTP) |
| 123 | Network Time Protocol (NTP) |
| 143 | Internet Mail Access Protocol (IMAP) — gestione posta |
| 161 | Simple Network Management Protocol (SNMP) |
| 443 | HTTP Secure (HTTPS), HTTP su TLS/SSL |

### Nmap

Per **controllare l'uso delle porte** (e altro) su Linux si può usare `nmap`: il *Network Mapper* è una **utility di scansione di rete** creata per mappare (scoprire) host e servizi su una rete. Può essere usata per sondare le porte degli host **per individuare quelle aperte** (su cui un'applicazione è in ascolto) ed eventualmente i servizi associati. Uso tipico:

- Port-scan di un bersaglio: `sudo nmap [indirizzo]`
- Sondare le porte per determinare i servizi: `sudo nmap -sV [indirizzo]`
- Controllare le N porte più usate: `sudo nmap --top-port N [indirizzo]`

Esempio:

```
$ nmap --top-port 10 www.google.com
PORT      STATE    SERVICE
21/tcp    filtered ftp
22/tcp    filtered ssh
23/tcp    filtered telnet
25/tcp    filtered smtp
80/tcp    open     http
110/tcp   filtered pop3
139/tcp   filtered netbios-ssn
443/tcp   open     https
445/tcp   filtered microsoft-ds
3389/tcp  filtered ms-wbt-server
```

Lo stato può essere open o closed, filtered o unfiltered (non scansionabile).

## Multiplazione e demultiplazione

Si consideri un processo sull'host A (porta 19157) che vuole inviare un messaggio a un processo (porta 46428) sull'host B. Nella **multiplazione**, il trasporto dell'host A crea un segmento/datagram che include i dati applicativi, la porta sorgente (19157) e la porta destinazione (46428), poi **passa il segmento al livello di rete**, che lo incapsula in un datagram IP e fa un tentativo best-effort di consegnarlo all'host ricevente. Nella **demultiplazione**, se il segmento arriva all'host B, **il trasporto lo riceve e lo decapsula**, quindi **passa il segmento al socket appropriato** esaminando la porta di destinazione.

### In UDP (C/C++)

Client:

```c
sockfd = socket(AF_INET, SOCK_DGRAM, 0);
// il socket tipicamente non è bound: il SO sceglie una porta libera (es. 46428),
// ma si può sempre fare bind su una porta specifica

servaddr.sin_port = htons(19157);
servaddr.sin_addr.s_addr = inet_addr(address_of_B);

sendto(sockfd, (const char *)msg, strlen(msg), 0,
       (const struct sockaddr *)&destaddr, sizeof(destaddr));
```

Server:

```c
sockfd = socket(AF_INET, SOCK_DGRAM, 0);

servaddr.sin_addr.s_addr = INADDR_ANY;
servaddr.sin_port = htons(19157);

bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr));

// porta/indirizzo di destinazione recuperati dalla struttura riempita da recvfrom
recvfrom(sockfd, (char *)msg, 1024, 0,
         (struct sockaddr *)&cliaddr, &len);

sendto(sockfd, (const char *)msg, strlen(msg), 0,
       (const struct sockaddr *)&cliaddr, sizeof(cliaddr));
```

La risposta viene rispedita **a qualunque client** sia. Un socket UDP si identifica con **due elementi**: indirizzo (IP) di destinazione e porta di destinazione. Si può quindi usare lo stesso socket per inviare messaggi di ritorno **a più porte/indirizzi sorgente diversi**: la struttura `cliaddr`, riempita da `recvfrom`, può essere usata come destinazione del `sendto`, indipendentemente da chi sia l'host.

### In TCP (C/C++)

Il server ha un **welcoming socket**, in attesa di richieste di connessione su una porta specifica (es. 19157). Il client crea un socket e **invia un segmento di richiesta di connessione** all'host indicato nella struttura `sockaddr_in`:

```c
sockfd = socket(AF_INET, SOCK_STREAM, 0);

servaddr.sin_port = htons(19157);
servaddr.sin_addr.s_addr = inet_addr(address_of_B);

connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));
```

Una **richiesta di connessione è solo un segmento TCP** con porta di destinazione (19157) e il bit speciale di instaurazione della connessione attivo nell'header TCP (SYN = 1). Ricevuta la richiesta, il server **individua il processo server in attesa** di accettare la connessione e crea un nuovo socket:

```c
new_socket = accept(sockfd, (struct sockaddr *)&cliaddr, (socklen_t *)&addrlen);
```

Il trasporto lato server riempie la struttura `cliaddr` **con porte e indirizzi del segmento in arrivo** e crea il nuovo socket; tutti i segmenti futuri con quella specifica porta sorgente, IP sorgente, porta destinazione e IP destinazione **saranno demultiplati verso `new_socket`**. Un socket TCP si identifica quindi con **quattro elementi**: IP sorgente, porta sorgente, IP destinazione, porta destinazione. Per via dell'handshake iniziale, la connessione TCP **lega ("intreccia") i processi** di entrambi i lati del socket: un solo mittente e un solo destinatario; se uno dei due lati si interrompe, il socket si chiude da entrambi i lati (cosa che non avviene in UDP).

### Esempio HTTP

Si consideri un host C che apre **due sessioni HTTP verso il server B** e un host A che ne apre una verso B: A, C e B hanno ciascuno il proprio IP, e C assegna due porte sorgente diverse (26145 e 7532) alle sue due connessioni. A può assegnare la porta sorgente 26145 alla propria connessione senza sapere di C, e non è un problema: **le due connessioni hanno IP sorgente diversi**. Il server apre un nuovo processo (o thread) per ogni connessione in arrivo, assegnandogli lo specifico socket (`new_socket`); è un approccio tipico, ma aprire troppi processi/thread può danneggiare le prestazioni del server.

## UDP

**UDP è utile per connessioni semplici e rapide** e svolge principalmente due compiti: consegna processo-a-processo (porte, multiplazione/demultiplazione) e controllo degli errori. UDP è senza connessione: **nessun handshake** tra le entità di trasporto prima di inviare un segmento, **nessuna garanzia di consegna** (nessun trasferimento affidabile) e **nessun controllo di congestione/flusso**. Grossolanamente, UDP è un protocollo **minimalista**: aggiunge solo "l'essenziale" rispetto al protocollo IP sottostante.

### Perché usare UDP invece di TCP?

- **Controllo a livello applicazione**: UDP è più diretto, l'applicazione ha più controllo sulla trasmissione; utile nelle applicazioni real-time, dove velocità di invio e ritardi sono cruciali e la perdita di dati è tollerabile.
- **Stabilimento rapido della connessione**: niente handshake, meno ritardo; bene per il DNS, per non aggiungere ritardi.
- **Nessuno stato di connessione**: niente parametri di controllo di congestione, niente numeri di sequenza o acknowledgment; un server può sostenere molti più client attivi su UDP che su TCP.
- **Overhead di pacchetto minimo**: l'header TCP aggiunge 20 byte per segmento, UDP solo 8.

### Esempio: DNS su UDP

Il client DNS funziona così: a **livello applicazione** l'host costruisce il messaggio di query DNS e lo passa a UDP; a **livello di trasporto**, senza handshake, UDP aggiunge gli header e passa il segmento al livello di rete; a **livello di rete** il segmento UDP è incapsulato in un datagram IP e inviato al server DNS (attraverso il livello di accesso). Il client attende la risposta e, se **non arriva** (la rete ha perso query o risposta), può reinviare la query, inviarla a un altro name server, o informare l'applicazione che la risposta non è arrivata.

### Uso di UDP

Le applicazioni che necessitano **trasferimento affidabile** (e-mail, terminale remoto, Web) girano su TCP (o su protocolli affidabili basati su UDP come QUIC), perché non ci si può permettere perdite: le mail, ad esempio, vanno consegnate per intero. **SNMP** usa UDP per la gestione dei dispositivi, poiché le applicazioni di network management **devono spesso girare quando la rete è sotto stress**, proprio quando il trasferimento affidabile è difficile. Le **applicazioni multimediali** (telefonia Internet, videoconferenza, streaming) usano spesso sia UDP che TCP, perché si può tollerare una piccola perdita di pacchetti; in generale le applicazioni real-time reagiscono male al controllo di congestione di TCP.

| Servizio | Protocollo applicativo | Protocollo di trasporto |
| --- | --- | --- |
| E-mail | SMTP | TCP |
| Terminale remoto | Telnet | TCP |
| Web | HTTP | TCP o UDP |
| Trasferimento file | FTP | TCP |
| Traduzione nomi | DNS | UDP |
| Gestione dispositivi | SNMP | UDP |
| Streaming multimediale | Proprietari | UDP o TCP |
| Telefonia Internet | Proprietari | UDP o TCP |

### Controversia

Far girare applicazioni multimediali su UDP è **controverso**, perché non c'è controllo di congestione. Se tutti (egoisticamente) iniziassero a trasmettere video ad alto bit-rate senza controllo di congestione, **i dispositivi di rete andrebbero in overflow** con più pacchetti UDP persi; gli alti tassi di perdita indotti dai sender UDP fuori controllo farebbero anche **calare drasticamente le velocità dei sender TCP**.

## Formato del segmento UDP

Il **segmento UDP** (più precisamente, datagram) è composto da due parti: un **header UDP** (64 bit), con **4 campi da 16 bit**, e i **dati** (N bit), cioè il messaggio applicativo. I campi dell'header sono:

- **Porta sorgente**: numero di porta del processo mittente.
- **Porta destinazione**: numero di porta del processo ricevente.
- **Lunghezza**: lunghezza dell'intero datagram (header+dati, cioè N + 64 bit).
- **Checksum**: usato dal ricevente per verificare l'integrità del messaggio.

### Checksum UDP

Il controllo di integrità usa il **checksum**, campo a 16 bit per il rilevamento degli errori. Il lato mittente calcola il **complemento a 1 della somma di tutte le parole a 16 bit** del datagram, con eventuali bit di overflow sommati a loro volta, e il **risultato è messo nel campo checksum**. Quando **il ricevente somma tutti i bit del messaggio (checksum incluso)**, la somma deve dare 1111111111111111 (16 uni); se anche un solo bit è 0, si sa che **sono stati introdotti errori** nel pacchetto.