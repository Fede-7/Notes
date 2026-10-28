# Lezione 8 Programmazione di rete

## Dal livello di applicazione alle socket

La maggior parte delle applicazioni di rete include un programma **lato client** e uno **lato server**: all'esecuzione si creano un processo client e un processo server che comunicano leggendo e scrivendo su **socket**.

- **Protocolli aperti**: protocolli le cui regole sono pubbliche (RFC); chiunque può sviluppare un'applicazione che li parla, e di solito si usano porte specifiche.
- **Protocolli proprietari**: protocolli "custom" di una singola applicazione, non pubblicati; due parti possono comunque comunicare a livello applicativo con un loro linguaggio concordato.

> [!info] Socket
> **Elemento centrale** della creazione di applicazioni di rete: implementano come scatola nera le funzionalità dei livelli **trasporto** (UDP/TCP) e **rete** (IP); esistono middleware che le incapsulano semplificandone l'uso, ma le API di base restano diffusissime.

I protocolli e i servizi si collocano nel sistema operativo secondo la divisione tra user space e kernel space.

- I protocolli di **livello applicazione** (web, DNS) sono pubblici ma sono implementati da **applicazioni in user space** (per esempio il browser), anche se i loro pacchetti attraversano tutto lo stack.
- Dal livello di **trasporto** in giù tutto è gestito nel **kernel space**, almeno su Unix/Linux e in generale sulle architetture monolitiche.
- Lo schema di interfacciamento è: applicazione (user space) → **API socket** → chiamate di sistema e servizi del kernel → trasporto → rete → accesso; nel kernel il livello di accesso si appoggia ai **driver** delle schede di rete, che realizzano la parte fisica.
- Ogni host implementa gli strati secondo il proprio ruolo: i terminali implementano tutto lo stack, i nodi interni solo i livelli necessari al loro compito (per esempio fino al livello rete per instradare i pacchetti).

Le API di base per socket UDP e TCP sono disponibili in quasi tutti i linguaggi (C, C++, C#, Java, Python, Matlab), con sintassi diverse ma semantica identica.

- Le **Berkeley socket** (dette BSD o POSIX socket) sono state introdotte con la Berkeley Software Distribution (1983), su sistemi già orientati alla comunicazione in rete.
- Sono state poi **standardizzate POSIX** e sono lo standard su Unix, macOS, Windows e altri sistemi; non sono legate all'architettura TCP/IP e gestiscono diversi tipi di canali di comunicazione.
- Sono **native in C**: le implementazioni di altri linguaggi (per esempio Python) si appoggiano a loro volta a un'interfaccia C sottostante, secondo lo schema API di alto livello sopra implementazione a basso livello.

## Socket come interfaccia tra processi e trasporto

Il processo si appoggia ai servizi delle socket (API in user space); le API si interfacciano ai servizi del kernel, che si appoggiano allo strato di trasporto configurato sulla socket (TCP o UDP); la comunicazione tra i due host avviene sul trasporto e sopra viaggia il livello di applicazione.

- Il **dominio** di una socket è più generale della rete: oltre alle socket di rete esistono socket locali (`AF_LOCAL`) usabili come comunicazione tra processi sullo stesso host.
- Le socket sono pensate per connessioni **client/server**, ma lo schema non lo impone: entrambe le parti possono mandare messaggi.
- Client e server devono creare socket **dello stesso tipo**: stessa famiglia di indirizzi (non può parlare una in IPv4 e l'altra in IPv6) e stesso tipo di canale di comunicazione.
- Le fasi comuni sono **creazione**, **connessione**, **messaggistica** e **distruzione**: UDP passa direttamente alla messaggistica, TCP prevede la fase di connessione.

### Connectionless e connection-oriented

Nel modello **connectionless (UDP)** client e server svolgono questa procedura.

1. Client: crea la socket.
2. Server: crea la socket e la **lega** (`bind`) a porta e indirizzo.
3. Client: invia il messaggio (`sendto`) senza contattare prima il server.
4. Server: legge il messaggio (`recvfrom`), ricavandone IP e porta del client.
5. Server: invia la risposta (`sendto`).
6. Client: legge la risposta (`recvfrom`) e chiude la socket; il server chiude la socket.

Nel modello **connection-oriented (TCP)** la procedura prevede una connessione prima della messaggistica.

1. Client: crea la socket e **si connette** (`connect`) al server.
2. Server: crea la socket, la lega a porta/indirizzo, si mette in **ascolto** (`listen`) e **accetta** (`accept`) le connessioni.
3. Client: invia il messaggio (`send`); server: legge il messaggio (`read`) e risponde (`send`).
4. Client: legge la risposta (`read`); il server chiude la socket **specifica del client** e può tornare ad `accept` per altri client; il client chiude la propria socket.

## La funzione socket

`socket(domain, type, protocol)` crea la socket e restituisce un **socket descriptor**, un intero trattato dal sistema come un file descriptor.

- **domain**: tipo di network e famiglia di indirizzi; `AF_INET` (IPv4, il default di internet), `AF_INET6` (IPv6), `AF_LOCAL` (socket locali).
- **type**: semantica del canale di comunicazione; `SOCK_STREAM` (TCP, connection-oriented), `SOCK_DGRAM` (UDP, connectionless), `SOCK_RAW` (gestione manuale del pacchetto, a un livello più basso).
- **protocol**: di solito `0`, cioè il protocollo default per quella combinazione domain/type; si sottospecifica un protocollo particolare solo quando serve.

> [!info] Everything is a file
> **Descrittori uniformi**: il socket descriptor entra nella tabella dei file aperti del processo, accanto a standard input, output ed error (0, 1, 2); il canale è trattato in modo uniforme rispetto a file, pipe e FIFO, come l'apertura di un canale di comunicazione.
> `close()` chiude la socket e rimuove il descrittore dalla tabella dei file aperti.

## Strutture degli indirizzi

### `sockaddr_in`

La struttura che definisce famiglia, porta e indirizzo di un end point IPv4 è la seguente.

```c
struct sockaddr_in {
    short          sin_family;  // famiglia, tipicamente AF_INET
    unsigned short sin_port;    // porta, in network order (htons)
    struct in_addr sin_addr;    // indirizzo IP
    char           sin_zero[8]; // padding alla dimensione di sockaddr
};
```

- L'indirizzo IPv4 è un intero a **32 bit**, la porta un intero a **16 bit**; le porte permettono di offrire diversi servizi dallo stesso indirizzo IP.
- Le fasce di porte: da 0 a 1023 **riservate** (ai processi di root), da 5000 a 32768 **porte utente**, le altre **effimere** (per i client, ai quali non interessa scegliere una porta specifica).
- `sin_zero` è padding di allineamento alla dimensione della struttura generica `sockaddr`.
- La struttura dipende dalla famiglia: `sockaddr_in` occupa **16 byte** totali, mentre `sockaddr_in6` aggiunge i campi `sin6_flowinfo` e `sin6_scope_id` attorno all'indirizzo a 128 bit, per un totale di circa 28–32 byte; serve congruenza tra famiglia dichiarata, struttura usata e argomenti delle funzioni.
- L'equivalente IPv6 di `INADDR_ANY` è la costante `in6addr_any`, che fa ascoltare la socket su tutti gli indirizzi locali IPv6.
- `sin_addr` spesso si imposta a `INADDR_ANY`: la socket si aggancia a **qualunque indirizzo** esposto dalle interfacce di rete dell'host; per ascoltare solo da una macchina specifica si indica il suo IP (per esempio `inet_addr("192.168.1.10")`).
- `inet_pton()` converte direttamente un indirizzo in notazione dotted nel formato binario della struttura (funziona per IPv4 e IPv6, purché coerenti con la famiglia): ritorna `1` in caso di successo, `0` per una stringa non valida, `-1` in caso di errore (per esempio famiglia non supportata); `inet_ntop()` fa l'inverso.

### Rappresentazione dei numeri e byte order

> [!def] Big endian e little endian
> **Rappresentazioni degli interi in memoria**: big endian pone prima il byte più significativo, little endian prima il meno significativo; host diversi possono usare rappresentazioni diverse, quindi un numero letto con l'ordine sbagliato risulta completamente diverso.

- **Network byte order**: per convenzione i protocolli TCP/IP lavorano in **big endian**; tutti i dati numerici devono viaggiare in rete in questo formato.
- Il programmatore non deve conoscere l'endianess della propria macchina: le funzioni di conversione `htons`/`htonl` (host → network) e `ntohs`/`ntohl` (network → host) fanno la traduzione localmente e rendono il codice portabile; `short` per le porte, `long` per gli indirizzi e gli interi a 32 bit.
- Regola pratica: prima di mandare un numero si converte con `htonl`/`htons`, dopo averlo ricevuto con `ntohl`/`ntohs`; per i byte non serve conversione.

## `bind` e assegnazione dell'indirizzo

`bind(socket, address, address_len)` associa la socket a un indirizzo e a una porta locali; restituisce `0` in caso di successo, `-1` altrimenti, e l'ultimo campo serve a verificare la lunghezza attesa della struttura.

- Il bind è **fondamentale per il server**, che deve essere raggiungibile su una porta nota; il client può anche non esporre un indirizzo, perché nel TCP apre lui la connessione e il server risponde sul canale, mentre nell'UDP entrambe le parti devono poter mandare e ricevere.
- Il bind **non crea una connessione**: crea solo l'associazione a un indirizzo; la connessione TCP richiede `listen` e `accept` sul server e `connect` sul client.
- Nessuno garantisce l'assenza di **conflitti di porta**: una porta già occupata rende il bind fallimentare, e quando un canale viene chiuso la porta resta per un periodo non riutilizzabile.

### Binding implicito

> [!def] Implicit binding
> **Assegnazione automatica** dell'indirizzo e della porta: su una socket non bindata, la prima `sendto` (UDP) o `connect` (TCP) delega al sistema operativo la scelta di un'interfaccia e di una porta libera (solitamente una porta alta), e l'associazione dura fino alla chiusura della socket.

`getsockname()` interroga la socket per conoscere indirizzo, porta e interfaccia effettivamente assegnati dal sistema.

> [!error] Bind esplicito dopo quello implicito
> **Operazione fallimentare a runtime** (per esempio `EINVAL`): dopo l'associazione implicita non si può rifare il bind; per associare di nuovo l'indirizzo bisogna chiudere la socket e aprirne un'altra.

## UDP

### Schema di comunicazione

Nell'UDP ogni invio deve specificare il destinatario e ogni ricezione può restituire il mittente.

- `sendto(osock, obuf, olen, oflags, oaddr, oaddr_len)` invia il datagram; `recvfrom(isock, ibuf, ilen, iflags, iaddr, iaddr_len)` lo riceve e riempie `iaddr` con IP e porta del mittente; entrambe restituiscono i byte effettivamente inviati/ricevuti.
- La trasmissione è **non affidabile**: se un datagram si perde non arriva nessuna notifica; la perdita si può rilevare solo a livello applicativo.
- Entrambe le parti devono essere pronte a ricevere: per ogni `sendto` deve esserci dall'altro lato un processo su una `recvfrom`.
- La configurazione più tipica è **simmetrica**: entrambe le parti fanno il bind, così ciascuna può mandare e ricevere; il client può comunque ometterlo grazie al binding implicito.

Schema essenziale del client (il server è speculare):

```c
sockfd = socket(AF_INET, SOCK_DGRAM, 0);
memset(&servaddr, 0, sizeof(servaddr));
servaddr.sin_family = AF_INET;
servaddr.sin_port = htons(8080);
servaddr.sin_addr.s_addr = inet_addr("192.168.1.10");
sendto(sockfd, hello, strlen(hello), 0,
       (struct sockaddr *) &servaddr, sizeof(servaddr));
n = recvfrom(sockfd, buffer, 1024, 0, NULL, NULL);
close(sockfd);
```

- Il buffer di ricezione raccoglie byte: per trattarli come stringa si aggiunge il terminatore alla posizione `n`.
- Il server riceve con `recvfrom` (che riempie `cliaddr` con IP e porta del client) e risponde con `sendto` verso `cliaddr`: può così rispondere anche a un client che non ha fatto bind.

### `connect` su socket UDP

> [!info] Pseudo-canale UDP
> La `connect` su una socket datagram **non crea un canale affidabile**: imposta l'indirizzo di destinazione di default e definisce un filtro, scartando i datagram in ingresso non provenienti dal peer con cui ci si è connessi; la comunicazione resta UDP, con perdite comprese.

### Flag di `recvfrom` e `sendto`

I flag modificano il comportamento di default (flag a `0`) delle primitive di invio e ricezione.

- **MSG_PEEK**: legge il datagram **senza rimuoverlo** dalla coda di ricezione; consente un'ispezione condizionale (prima guardare cosa c'è, poi estrarre o eventualmente inoltrare a livello applicativo).
- **MSG_TRUNC** (su Linux): permette di recuperare la lunghezza completa del datagramma anche quando il buffer di ricezione è più piccolo; i byte eccedenti restano scartati.
- **MSG_WAITALL**: attende l'intero numero di byte richiesto prima di restituire; usato tipicamente con il TCP.
- **MSG_DONTWAIT**: ricezione non bloccante; considera solo ciò che è arrivato in quel momento, senza aspettare l'intero messaggio.

### Datagram non attesi

> [!warning] Datagram senza ricevitore
> Un datagram che raggiunge la destinazione ma non trova una socket associata alla porta di destinazione è **scartato dal livello di trasporto**, che può inoltre emettere un messaggio di porta non raggiungibile.

- UDP **non bufferizza i datagram che nessuno attende**: il pacchetto arriva dove deve arrivare, ma a livello di trasporto non c'è nessun processo pronto a prenderlo e viene smaltito.
- Il client lanciato prima del server manda il datagram con `sendto` (che parte comunque) e poi rimane **bloccato sulla ricezione**, oppure riceve l'errore: occorre lanciare prima il server.
- Dev'esserci sempre un **processo in ascolto nel momento giusto**: le sincronizzazioni si ottengono con le primitive bloccanti.

### Timeout di ricezione

Per evitare l'attesa indefinita si può impostare un timeout sulla ricezione tramite opzione della socket.

- Si prepara una `struct timeval` (secondi e microsecondi) e la si passa con `setsockopt()` per impostare **SO_RCVTIMEO** sulla ricezione.
- Se il datagram arriva prima della scadenza non succede nulla; alla scadenza la ricezione ritorna `-1` con errore `EAGAIN` o `EWOULDBLOCK` (non equivalenti: si controllano entrambi per compatibilità).
- Il timeout **non ritrasmette**: il datagram che non è arrivato è perso.

### Comunicazione su localhost

Nella comunicazione su `localhost` lo stack di rete viene attraversato fino al livello di trasporto, che lo rimanda indietro (**loopback**) con una risalita diretta: nessun pacchetto reale viaggia sulla rete; questi esempi servono solo a prendere confidenza sulla stessa macchina.

### Server UDP multi-client

L'UDP permette di servire più client con una sola socket e un solo processo.

- Il server risponde ai datagram con una **singola socket**: riceve, discrimina il mittente (IP e porta) e risponde; non deve stabilire connessioni particolari.
- È più semplice del TCP quando i messaggi sono brevi in entrambe le direzioni e i client sono molti: a ogni pacchetto in arrivo risponde in modo appropriato.
- Non c'è garanzia se due datagram arrivano insieme e il server non è ancora tornato in `recvfrom`: il canale non è affidabile e qualcosa può andare perso.

### Broadcast e multicast

Oltre alla comunicazione uno-a-uno, i protocolli IP offrono due meccanismi di invio diffuso, usati tipicamente con le **socket UDP** (TCP non li supporta).

> [!def] Broadcast
> **Invio a tutti gli host di una rete locale**, senza richiedere adesione a gruppi: supportato da IPv4, mentre IPv6 non lo prevede e usa il multicast al suo posto.

- Gli **indirizzi di broadcast IPv4** sono due: directed broadcast (per esempio `192.168.1.255`, dipende dalla subnet mask) e limited broadcast (`255.255.255.255`, non inoltrato dai router).
- Il **mittente** crea la socket UDP, abilita il broadcast con `setsockopt()` e opzione **SO_BROADCAST**, poi invia con `sendto()` verso l'indirizzo di broadcast e la porta di destinazione.
- Il **ricevente** crea la socket UDP, fa il bind su `INADDR_ANY` e sulla porta di destinazione, poi riceve con `recvfrom()`.

> [!def] Multicast
> **Invio agli host che hanno aderito a un gruppo multicast**, identificato da un indirizzo IP multicast (per esempio `239.255.0.1`): supportato sia da IPv4 sia da IPv6.

- Il ricevente deve **aderire al gruppo** con l'opzione `IP_ADD_MEMBERSHIP` (livello `IPPROTO_IP`), tramite una `struct ip_mreq` che indica indirizzo del gruppo e interfaccia locale da usare.
- Il mittente imposta il TTL dei pacchetti multicast con `IP_MULTICAST_TTL` (per esempio `1` per restare nella LAN locale) e invia i datagram all'indirizzo del gruppo, **senza conoscere i singoli riceventi**.
- Più riceventi fanno bind sulla stessa coppia indirizzo/porta grazie a `SO_REUSEADDR` e `SO_REUSEPORT`.
- All'adesione cooperano **sistema operativo e rete**: l'OS gestisce la richiesta di adesione e la comunica alla rete locale, i router multicast-aware inoltrano i pacchetti verso le reti con ricevitori interessati; le socket option permettono di richiedere comportamenti a livello di rete, mentre la consegna resta affidata alla rete sottostante.

## Buffer delle socket

Ogni socket ha a livello kernel un **send buffer** e un **receive buffer**, gestiti dalle chiamate di sistema; non vanno confusi con il buffer applicativo definito dal programmatore.

- I buffer possono essere **liberi, vuoti o parzialmente occupati**: ciò che si vuole leggere o scrivere può non coincidere con l'intero contenuto.
- Le dimensioni sono configurabili con le opzioni **SO_SNDBUF** e **SO_RCVBUF**, anche in modo asimmetrico tra invio e ricezione: un send buffer più grande accoda più dati in uscita riducendo i blocchi su `send`, un receive buffer più grande riduce il rischio di stalli del controllo di flusso TCP.

### Invio UDP

Il comportamento dell'invio dipende dalla modalità della socket e dallo stato del send buffer.

- **Comportamento blocking (default)**: `sendto` si blocca finché il datagram non viene accettato; il blocco può essere interrotto (per esempio da un segnale), quindi anche in modalità bloccante non ci si può fidare e i dati vanno controllati.
- **Comportamento non blocking**: `sendto` ritorna immediatamente; se il datagram non può essere accettato viene **scartato**, con `-1` e `EAGAIN`/`EWOULDBLOCK`.
- L'invio è atomico: il datagram va **tutto intero o niente** (niente mezzi pacchetti), anche se il suo payload può essere un frammento del dato di livello applicativo.

### Ricezione UDP

Anche la ricezione cambia comportamento tra modalità bloccante e non bloccante, e consuma un datagram per chiamata.

- **Blocking (default)**: `recvfrom` si blocca se non c'è nulla; quando trova qualcosa prende **un intero datagram** per chiamata.
- **Non blocking**: ritorna immediatamente; se la coda è vuota ritorna `-1` (con la relativa giustificazione) e si può gestire con polling (busy waiting).
- **Troncamento**: se il buffer applicativo è più piccolo del datagram, il datagram viene troncato e i byte eccedenti sono persi.

## TCP

### Connessione e handshake

> [!def] Connection-oriented
> **Canale affidabile di byte-stream** tra i due sistemi finali: prima di trasmettere, client e server fanno handshake; sul lato server coesistono una socket in ascolto (welcoming socket) e una socket client-specifica creata dopo l'handshake, su cui avviene lo scambio.

- Il client chiama `connect(socket, address, address_len)`, **bloccante**, verso l'indirizzo del server; restituisce `0` in caso di successo, `-1` in caso di fallimento.
- Il server chiama `listen(socket, backlog)` per mettersi in ascolto, **non bloccante**: dopo la `listen` il codice procede; è l'`accept` il punto di blocco. La `listen` si usa con i tipi connection-oriented come `SOCK_STREAM` e `SOCK_SEQPACKET`.
- `accept(socket, address, address_len)` è **bloccante**: il processo si ferma lì ad aspettare la connessione e riporta l'indirizzo del client; i due argomenti dell'indirizzo possono essere `NULL` se non serve identificarlo.
- Il **three-way handshake** avviene dentro il livello di trasporto ed è completamente **invisibile** ai programmi: `connect` e `accept` sono il punto di sincronizzazione, da cui la comunicazione prosegue nelle due direzioni.
- `accept` restituisce un **nuovo socket descriptor**: la socket client-specifica insiste sullo stesso indirizzo e porta del bind, mentre la socket di ascolto resta disponibile per le altre connessioni; un server che serve tre client tiene quindi **quattro descrittori** (la socket in ascolto più tre dedicate).
- `backlog` è la lunghezza massima della **coda delle richieste pendenti**, unica per tutti i client che si collegano; se la coda è piena, le nuove richieste possono essere rifiutate, ignorate o messe in attesa: decide il kernel, in una zona non garantita dallo standard (di solito sono rifiutate).
- Stabilita la connessione, i due processi comunicano come su un **interprocess communication**: lo stream di byte è utilizzabile con `read`/`write` (come file, pipe e FIFO), oppure con `send`/`recv`, versioni più specializzate per la rete dotate di flag; `sendto`/`recvfrom` restano utilizzabili con il destinatario implicito nella connessione, e `recv` con flag `0` è identica a `read`.
- Chi parla e chi ascolta va definito a livello applicativo: se entrambi si mettono su `send` (o entrambi su `recv`) non comunicano.
- `sendmsg()`/`recvmsg()` generalizzano `sendto()`/`recvfrom()` permettendo di inviare e ricevere da **buffer multipli**.

### Identificazione delle connessioni

> [!def] Quadrupla
> **Identificatore di una connessione TCP**: l'insieme (source IP, source port, destination IP, destination port); connessioni con quadruple diverse non sono in conflitto.

- Il server può tenere **più connessioni simultanee sulla stessa coppia IP e porta**: ogni `accept` crea una nuova socket, tutte sullo stesso bind, distinte dalla quadrupla.
- Il binding implicito assegna ai client porte diverse, distinguendo anche client con lo stesso IP.
- I limiti pratici al numero di connessioni sono: i **file descriptor** per processo (limiti del kernel), la **memoria kernel**, le **risorse di CPU**, le **porte disponibili lato client** e altri limiti architetturali.

### Chiusura della connessione

La terminazione TCP avviene a **quattro segmenti** (four-way closure), due per ciascuna direzione di chiusura.

- Il client chiama `close`: parte un segmento **FIN**, confermato dall'**ACK** del server; dopo la `close` il client entra nello stato **FIN_WAIT_1** e, ricevuto l'ACK, passa a **FIN_WAIT_2**: la sua socket è chiusa ma il canale resta aperto, in attesa della chiusura del server.
- Quando anche il server chiude la propria socket client-specifica, manda il suo **FIN** (stato **LAST_ACK**); il client risponde con l'ultimo **ACK** e passa allo stato **TIME_WAIT**: non è sicuro che il suo ultimo ACK sia arrivato.
- Il server, ricevuto l'ultimo ACK, può chiudere senza dubbi: l'incertezza sull'arrivo dell'ultimo messaggio resta solo al client, che per questo mantiene la finestra di attesa.

> [!def] TIME_WAIT
> **Periodo refrattario** dopo la chiusura, con due ragioni: consentire la ritrasmissione dell'ACK finale nel caso in cui il peer, non ricevendolo, ritrasmetta il FIN; lasciar scadere i segmenti ritardati della vecchia connessione, perché non finiscano in una nuova connessione sulla stessa porta.

- Durante il TIME_WAIT la coppia indirizzo/porta non è immediatamente riutilizzabile: chi riapre subito la stessa porta deve attendere la latenza, salvo usare le opzioni sottostanti.
- **SO_REUSEADDR** (opzione di livello socket, POSIX): permette di riutilizzare subito la coppia indirizzo/porta appena chiusa, trascurando il TIME_WAIT; si imposta **prima del bind** e vale sia lato client sia lato server, ma non permette normalmente a due server TCP di ascoltare sulla stessa coppia IP e porta.
- **SO_REUSEPORT** (non standard POSIX, usata per esempio su Linux): permette a **più socket** di fare bind sulla stessa coppia IP e porta e di chiamare `listen` sullo stesso end point (su Linux i processi che la condividono devono avere lo stesso effective user ID); il kernel distribuisce le connessioni in modo bilanciato tra le socket in ascolto, utile per distribuire il carico su sistemi multicore.
- `shutdown(socket, how)` chiude selettivamente una direzione del canale: `SHUT_RD` per la lettura, `SHUT_WR` per la scrittura, `SHUT_RDWR` per entrambe; su Linux interrompe anche una `accept` bloccata, quindi è il modo ordinato di sbloccare il server alla ricezione di un segnale.

### Opzioni dei socket

`getsockopt()`/`setsockopt()` leggono e impostano le opzioni di una socket già creata; restituiscono `0` in caso di successo, `-1` altrimenti.

- Parametri: socket descriptor, **livello** dell'opzione (`SOL_SOCKET` per il comportamento della socket, ma anche livelli inferiori come il trasporto TCP o le opzioni IPv4), **nome** dell'opzione, **valore** (impostato o letto) e sua **lunghezza**.
- Le opzioni quindi non riguardano solo il livello della socket: si può scendere fino ai livelli più bassi dello stack di rete.
- Le opzioni vanno impostate **prima del bind**: `SO_REUSEADDR`, `SO_REUSEPORT`, il timeout `SO_RCVTIMEO` e le dimensioni dei buffer `SO_SNDBUF`/`SO_RCVBUF` sono i casi visti.

### Flag di `send` e `recv`

I flag specializzano il comportamento di default delle primitive di rete per la singola chiamata.

- **MSG_DONTWAIT**: `send`/`recv` non bloccanti sulla singola chiamata; il controllo diventa attivo (polling).
- **MSG_PEEK**: legge i dati **senza estrarli** dalla coda di ricezione.
- **MSG_WAITALL**: sulla ricezione attende che l'intera lunghezza richiesta sia raggiunta; interrompibile comunque da segnali ed errori, quindi il valore di ritorno va comunque controllato.
- **MSG_NOSIGNAL**: evita che la `send` su canale rotto generi `SIGPIPE`; la schermatura del segnale andrebbe comunque predisposta prima.

> [!warning] SIGPIPE
> Scrivere su un **canale rotto** (l'estremo di lettura ha chiuso) genera il segnale **SIGPIPE**: se non è catturato o ignorato, il comportamento di default è la **terminazione del processo** che lo riceve.

### Modalità non bloccante del descrittore

Oltre ai flag per singola chiamata esiste un modo per rendere non bloccante l'intera socket.

- Per la modalità non bloccante dell'intero descrittore non esiste un'opzione standard tra quelle viste: si usa la funzione POSIX `fcntl()`.
- Si leggono i flag con `fcntl(fd, F_GETFL)` e si reimpostano con `fcntl(fd, F_SETFL, flags | O_NONBLOCK)`: i flag sono **maschere di bit**, quindi al valore letto si aggiunge la modalità non bloccante.
- Da quel momento **tutte** le operazioni sul descrittore (`read`, `write`, `send`, `recv`, `connect`) sono non bloccanti; la `connect` non bloccante può ritornare `-1` con **EINPROGRESS** mentre la connessione è in corso; la funzione vale per qualunque file descriptor (TCP, UDP, pipe e altri canali), non solo per le socket.

### Buffer e comportamenti blocking

#### Scrittura

In base allo spazio nel send buffer le due modalità si comportano così.

- **Blocking (default)**: `write`/`send` attende che **tutti** i byte richiesti siano accettati dal send buffer; normalmente ci riesce, ma un'interruzione (segnale, timeout) può ridurre i byte scritti: il valore di ritorno va sempre controllato.
- **Non blocking**: non aspetta mai lo spazio sufficiente per tutto; scrive i byte che entrano e ritorna quanti ne ha scritti, oppure `-1` con `EAGAIN`/`EWOULDBLOCK` se il buffer è pieno.

#### Lettura

La lettura ha una semantica diversa dalla scrittura.

- **Blocking (default)**: `read`/`recv` restituisce i byte disponibili in quel momento, anche **uno solo**, senza aspettare che il buffer si riempia; si blocca soltanto quando il buffer di lettura è **vuoto**.
- Per questo è facilissimo che `read` legga **meno** di quanto richiesto: chi vuole tutti i byte deve ciclare.
- **Non blocking**: ritorna subito con i dati disponibili, oppure `-1` con `EAGAIN` se non c'è nulla.
- C'è un'**asimmetria** tra le primitive: la `write` bloccante è "paziente" (aspetta di trasferire tutto), la `read` è "impaziente" (restituisce subito la parte disponibile).
- Una lettura pari a **0 byte** significa che l'altro estremo ha **chiuso la connessione**.

### Letture e scritture robuste

Poiché né `read` né `write` garantiscono di coprire tutti i byte richiesti, si definiscono funzioni **robuste** (safe read/write) che ciclicano sul canale fino al completamento.

```c
while (nleft > 0) {
  n = recv(fd, p, nleft, 0);
  if (n == -1 && errno == EINTR) continue; // interrotta: riprova
  if (n == -1) return -1;                  // errore reale
  if (n == 0) break;                       // connessione chiusa
  p += n; nleft -= n;                      // avanza nel buffer
}
```

- Il **puntatore avanza** nel buffer con l'aritmetica dei puntatori: ogni volta che si riceve o invia una quantità di byte, ci si sposta per trattare i rimanenti.
- Un errore `EINTR` (interruzione) fa riprovare; una lettura pari a `0` indica connessione chiusa e si ritorna quanto letto finora; lo schema è identico per la scrittura robusta.

## Server concorrenti

### Server sequenziale

Un server con un unico processo gestisce **una comunicazione alla volta**: dal `socket` al `bind`, `listen` e `accept`, la socket client-specifica impegna completamente il processo, che solo alla fine torna in ascolto; le altre richieste restano **in coda nel backlog**.

### Server multiprocesso

Il server concorrente multiprocesso crea un **nuovo processo per ogni connessione accettata**, così il padre torna subito in ascolto.

- Sequenza: `socket`, `bind`, `listen`, poi ciclo su `accept`; ogni `accept` crea una nuova socket e subito dopo si fa `fork()`.
- Il `fork` restituisce al padre il **PID del figlio** e al figlio **0**: dentro lo stesso codice si distingue il ramo del padre da quello del figlio.
- Padre e figlio nascono **indistinguibili** (a parte il PID) e condividono i descrittori: il figlio chiude la socket in `listen` e gestisce il canale dedicato al client; il padre chiude la socket del client e torna in `accept`.
- Le chiusure sono simmetriche: ciascun processo chiude solo ciò che non usa; la socket in ascolto resta aperta nel padre.

#### Figli zombie

> [!warning] Processi zombie
> Se il padre non raccoglie l'**exit status** dei figli, questi restano **zombie**: il descrittore resta occupato in attesa della consegna e, su un server pensato per restare in piedi a lungo, si accumula un **memory leak**.

- Rimedio 1: catturare il segnale **SIGCHLD** con un handler che recupera i figli terminati (per esempio con `wait`, o con un ciclo di `waitpid(-1, NULL, WNOHANG)` che li raccoglie tutti senza bloccare): alla morte del figlio il padre riceve il segnale e l'handler lo raccoglie.
- Rimedio 2: impostare `SIG_IGN` su `SIGCHLD`, che equivale a mettere i figli in **detach**: il destino del figlio non è più legato al monitoraggio del padre.
- `sigaction()` è il modo moderno per associare un handler a un segnale: una struttura dati (con il campo `sa_handler`) riceve l'handler come puntatore a funzione e viene agganciata al segnale; all'arrivo del segnale il flusso di controllo è interrotto, si esegue l'handler, poi si riprende. Il campo `sa_flags` permette per esempio **SA_RESTART**, che fa ripartire automaticamente le chiamate di sistema interrotte dal segnale (come `accept` e `recv`).
- `signal()` è l'alternativa storica e più semplice: associa direttamente la funzione al segnale.

### Server multithread

Il server multithread replica lo schema del fork, ma i **thread condividono lo spazio di indirizzamento**, il che crea un problema sull'`accept`.

- Due `accept` consecutive scriverebbero il nuovo descriptor **nella stessa variabile**, sovrascrivendolo.
- Si salva temporaneamente il nuovo descriptor e lo si copia in **memoria dedicata allocata dinamicamente** (`malloc`), passata come argomento a `pthread_create()`.
- `pthread_create(&tid, attr, routine_avvio, arg)` crea il thread, che lavora nello spazio di indirizzamento del processo principale e gestisce in esclusiva il client.
- La memoria allocata va **deallocata**: la gestione della distruzione può essere centralizzata o delegata al thread in uscita, che sa cosa distruggere.
- Il thread può essere creato o messo in **detach**, per non doverne attendere la terminazione.

### Server multiplexing con `select`

> [!def] Multiplexing
> **Tecnica** per gestire più client contemporaneamente con un **unico processo**, senza creare thread o processi: `select()` monitora insiemi di file descriptor e si sblocca appena uno di loro è pronto; evita la proliferazione di processi o thread al crescere dei client, al prezzo di overhead e maggiore complessità del codice.

- `select(nfds, readfds, writefds, exceptfds, timeout)` lavora su canali di I/O in generale, non solo socket: rimane bloccata finché un descrittore non è pronto in lettura o scrittura, si verifica un evento, scade il timeout o arriva un'interruzione.
- **nfds** è il range dei descrittori da controllare: si passa il numero massimo di descrittori **più uno**; la capacità di un `fd_set` è limitata da **FD_SETSIZE** (tipicamente 1024 su Linux).
- I tre insiemi: descrittori su cui aspettare dati **da leggere**, descrittori attesi **a scrivere** e monitoraggio delle **eccezioni** (se non interessa, `NULL`).
- **timeout**: `NULL` per un'attesa indefinita, una `struct timeval` (secondi e microsecondi) per un tempo di attesa definito (la `select` può comunque sbloccarsi prima se un descrittore diventa pronto), oppure timeout a zero per ritornare subito senza bloccare (polling).
- Valori di ritorno: **positivo** = numero di descrittori pronti; `0` = timeout scaduto; `-1` = errore o interruzione.
- Gli insiemi sono variabili `fd_set`, implementate tipicamente come **maschere di bit**, gestite con le macro `FD_ZERO` (azzera), `FD_SET` (aggiunge), `FD_CLR` (toglie), `FD_ISSET` (verifica l'appartenenza: dopo la `select` indica se il descrittore è pronto).
- La `select` **modifica gli insiemi**: dopo lo sblocco contengono solo i descrittori che si sono resi pronti; l'insieme di lavoro va quindi **reimpostato a ogni iterazione** partendo dall'insieme completo.

```c
FD_ZERO(&rset);
FD_SET(sockfd, &rset);
ret = select(sockfd + 1, &rset, NULL, NULL, NULL);
if (ret > 0 && FD_ISSET(sockfd, &rset))
  n = recv(sockfd, buffer, 1024, 0);
```

Le condizioni che svegliano la `select` sono le seguenti.

- **In lettura**: dati nel receive buffer oltre la soglia **SO_RCVLOWAT** (di default **un byte**), chiusura del lato di invio del peer, errore sul canale, richiesta di connessione pendente su una socket in `listen`.
- **In scrittura**: spazio disponibile nel send buffer (anche solo in parte: lo sblocco non garantisce spazio per l'intero messaggio), connessione TCP stabilita (`connect` completata), errore sul canale.
- **In eccezione**: condizioni eccezionali del livello di trasporto, come gli **out-of-band data** (dati urgenti segnalati da TCP con il flag URG, ricevibili su Linux con `recv()` e flag `MSG_OOB`), che possono richiedere una gestione rapida dell'evento.

Poiché la `select` si sblocca solo quando c'è qualcosa da fare, l'operazione successiva sul descrittore pronto **non si blocca**: si è certi che ci sia un dato da ricevere (o spazio per scrivere).

#### Schema del server echo

Lo schema classico combina socket in ascolto e socket dei client in un unico loop.

- Si mantiene un insieme **allset** con tutti i descrittori da monitorare (la socket in `listen` più le socket dei client) e una **copia di lavoro** passata alla `select`, ricostruita a ogni ciclo.
- Un array di client con slot inizializzati a `-1` registra le socket attive; un indice massimo delimita la scansione dell'array.
- Allo sblocco: se è pronta la socket in `listen` si fa subito `accept` (la connessione è già arrivata), si inserisce il nuovo descrittore nel primo slot libero e si aggiornano massimo e range.
- Per ogni client pronto si legge: se la lettura ritorna `0` il client ha chiuso, si rimuove il descrittore dall'insieme e si libera lo slot; altrimenti si scrive la risposta sulla stessa socket.
- Con un unico loop si servono tutti i client, evitando la proliferazione di processi o thread.

#### Client multiplexing

Un client può essere reso **multiplexed** in un unico processo: la `select` monitora insieme lo **standard input** e la **socket**; se arriva input da tastiera lo si scrive sulla socket, se arrivano dati dalla socket li si stampa su schermo: due canali gestiti contemporaneamente senza thread aggiuntivi.

## Risoluzione dei nomi

Le socket lavorano con **indirizzi IP**, mentre su internet gli host sono tipicamente identificati per **hostname**: la socket opera a livello di trasporto e l'hostname a livello di applicazione, quindi per connettersi tramite nome serve la **traduzione DNS**, che restituisce l'indirizzo IP da passare alla socket.

- `gethostbyname()` è la funzione **legacy** che risolve un hostname in indirizzi IPv4 tramite il resolver di sistema; non restituisce solo l'indirizzo ma una struttura `hostent` con le informazioni sull'host; `gethostbyaddr()` è la funzione analoga che parte da un indirizzo IP.

> [!info] Struttura `hostent`
> Contiene: `h_name` (nome canonico dell'host), `h_aliases` (array di alias terminato da `NULL`), `h_addrtype` (famiglia, tipicamente `AF_INET`), `h_length` (lunghezza dell'indirizzo, tipicamente 4 byte) e `h_addr_list` (array di indirizzi terminato da `NULL`; `h_addr` è il primo elemento).

- Un DNS può restituire una **lista di indirizzi**, in ordine eventualmente casuale se la query arriva a server round-robin; l'indirizzo risolto serve a inizializzare la `sockaddr_in` (per esempio copiando `h_addr_list[0]` nella struttura con `memcpy`).
- `getaddrinfo()` è la funzione **moderna** consigliata per le nuove applicazioni: risolve hostname in IPv4 e IPv6 con un'unica interfaccia e restituisce una lista di strutture `addrinfo` pronte per `socket()` e `connect()`.
- La struttura `hints` esprime i **criteri di selezione** che filtrano i risultati: `ai_family` (`AF_INET`, `AF_INET6`, `AF_UNSPEC` per entrambe), `ai_socktype` (`SOCK_STREAM`, `SOCK_DGRAM`), `ai_protocol` (protocollo specifico, `0` se non specificato) e `ai_flags` (opzioni aggiuntive della risoluzione).
- Il risultato è una **lista concatenata** di indirizzi: si può tentare la `connect` su ciascuno fino a quella che riesce, chiudendo le socket fallite; la memoria allocata da `getaddrinfo()` va liberata con `freeaddrinfo()`, e gli errori si descrivono con `gai_strerror()`.

Un'applicazione della catena risoluzione → socket è una **richiesta HTTP costruita a mano**: gli elementi da specificare sono tre — **hostname** del server, **porta** e **risorsa** da recuperare (percorso dell'oggetto). Risolto l'hostname e copiato l'indirizzo nella struttura, ci si connette alla porta (tipicamente la 80), si invia la richiesta come stringa (per esempio un metodo `HEAD` con `Connection: close`, cioè una connessione non persistente quando basta controllare una sola pagina) e si legge la risposta ricevuta dalla socket.