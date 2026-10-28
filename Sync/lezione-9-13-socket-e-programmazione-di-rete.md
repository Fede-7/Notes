# Lezione 9-13 Socket e programmazione di rete

## Applicazioni di rete

La maggior parte delle applicazioni di rete è composta da un programma lato client e un programma lato server che comunicano attraverso la rete: la loro esecuzione crea un processo client e un processo server, che comunicano leggendo e scrivendo su socket.

> [!def] Protocollo aperto
> **Protocollo** le cui regole sono pubbliche: chiunque può scrivere uno dei due lati e i due programmi interoperano.

- **Protocollo proprietario**: protocollo "custom", non pubblicato in un RFC o altrove; un solo team scrive entrambi i lati e controlla il formato, e nessun altro può scrivere un programma che vi dialoga.
- Un protocollo aperto usa la sua **well-known port**; un protocollo proprio deve stare lontano da quelle porte.
- **TCP** (*Transmission Control Protocol*): orientato alla connessione, fornisce un canale affidabile di byte-stream attraverso cui i dati fluiscono tra i due sistemi terminali.
- **UDP** (*User Datagram Protocol*): connectionless, invia pacchetti indipendenti da un sistema all'altro senza garanzie di consegna.

## Il socket

> [!def] Socket
> **Estremità** di un canale di comunicazione bidirezionale tra due processi, identificata da un descrittore.

- Introdotto in **BSD 4.2** nel 1983, è ancora lo standard de facto: Unix, macOS e Windows (con uno spelling diverso).
- I due processi possono essere sulla stessa macchina o su due macchine ai lati opposti del mondo: le chiamate non cambiano.
- Non è legato a TCP/IP: la stessa API ha servito altre famiglie di protocolli, ed è per questo che le chiamate hanno forma generica.
- Essendo un descrittore, accetta `read()`, `write()` e `close()`, le chiamate già note per i file.
- La **Socket API** dà alle applicazioni accesso ai servizi di trasporto implementati dallo stack di rete del sistema operativo.
- Diverse librerie, framework e middleware incapsulano la Socket API semplificandone l'uso, ma l'API base resta diffusamente usata.
- In dominio Unix si usano i **Berkeley socket** (detti anche BSD o POSIX socket), API native in C, sia per TCP sia per UDP; API simili sono disponibili in quasi tutti i linguaggi e sistemi operativi.

### Procedure client-server

Le procedure di comunicazione distinguono il modello connectionless e quello connection-oriented in quattro fasi.

| Fase | Connectionless (UDP) | Connection-oriented (TCP) |
|---|---|---|
| Creazione | Create Socket (client e server) | Create Socket (client e server) |
| Connessione | assente | client: `connect()`; server: attende le connessioni |
| Messaggi | Send/Read Message, Read/Send Reply | Send/Read Message, Read/Send Reply |
| Chiusura | Close Socket | Close Socket; il server chiude il socket client-specifico |

## Creazione, chiusura e associazione

### `socket()`

I socket si creano con la funzione `socket()`, che restituisce il descrittore `sockfd` del nuovo socket.

```c
#include <sys/socket.h>
int socket(int domain, int type, int protocol);
```

- **`domain`**: specifica il dominio di rete e la famiglia di indirizzamento.
- **`type`**: specifica la semantica di comunicazione (stream o datagram).
- **`protocol`**: indica un protocollo particolare, spesso `0` per quello di default.
- I socket aderiscono alla filosofia Unix *"everything is a file"*: le sorgenti di I/O sono trattate come file e associate a un file descriptor.

I valori principali di `domain` sono i seguenti.

| Domain | Famiglia |
|---|---|
| `AF_INET` | IPv4 |
| `AF_INET6` | IPv6 |
| `AF_LOCAL` | due processi su questa macchina, attraverso il file system |

I valori principali di `type` sono i seguenti.

| Type | Canale |
|---|---|
| `SOCK_STREAM` | un byte stream: connesso, ordinato, affidabile |
| `SOCK_DGRAM` | messaggi indipendenti, senza connessione né garanzie |
| `SOCK_RAW` | il pacchetto è costruito a mano, sotto il livello di trasporto |

### `close()`

I socket si chiudono con la funzione `close()`, che restituisce `0` in caso di successo e `-1` altrimenti.

```c
#include <unistd.h>
int close(int socket_id);
```

- **`socket_id`**: è il file descriptor del socket da chiudere.

### `bind()`

La funzione `bind()` associa un socket a un indirizzo e a una porta locali, e restituisce `0` in caso di successo e `-1` altrimenti.

```c
int bind(int socket, const struct sockaddr *address,
         socklen_t address_len);
```

- **`socket`**: file descriptor del socket da associare.
- **`address`**: puntatore a una struttura `sockaddr` che specifica porta e indirizzo; `address.sin_addr` è spesso impostato a `INADDR_ANY` per ascoltare su tutti gli indirizzi (più IP).
- **`address_len`**: lunghezza della struttura `sockaddr`, ottenibile con `sizeof()`.
- La funzione è usata sui server, che devono associare il socket a una porta specifica, mentre sui client è opzionale: il sistema operativo assegna automaticamente una porta libera.

## Indirizzi IP, porte e ordine dei byte

### Strutture degli indirizzi

I socket di dominio internet in C si appoggiano ad alcune strutture che definiscono indirizzi e porte degli host mittente e destinatario. La struttura `sockaddr_in` (IPv4) e la struttura `sockaddr_in6` (IPv6) hanno forma analoga ma dimensioni diverse.

```c
struct sockaddr_in {
    sa_family_t sin_family;
    in_port_t sin_port;
    struct in_addr sin_addr;   // 4 B
    unsigned char sin_zero[8]; // per uniformare la dimensione
};                            // 16 B totali

struct sockaddr_in6 {
    sa_family_t sin6_family;
    in_port_t sin6_port;
    uint32_t sin6_flowinfo;
    struct in6_addr sin6_addr; // 16 B
    uint32_t sin6_scope_id;
};                            // ~28-32 B totali
```

Un socket internet è identificato da due elementi.

- Un **indirizzo IP**: intero a 32 bit (es. `143.225.5.3`).
- Una **porta**: intero a 16 bit, da 0 a 65535.

Le porte esistono per offrire diversi servizi dallo stesso indirizzo IP e si classificano per intervallo.

- **0–1023**: porte riservate (ai processi di root).
- **5000–32768**: porte utente.
- **Altre**: porte effimere, per i client, ai quali non interessa scegliere una porta specifica.

### Ordine dei byte

Un intero in memoria occupa 4 byte e può essere codificato in due modi; i processori possono essere di entrambi i tipi.

- **Big Endian**: è memorizzato prima il byte più significativo.
- **Little Endian**: è memorizzato prima il byte meno significativo.
- I protocolli TCP/IP lavorano con il big endian, chiamato **network byte order**, quindi sono necessarie funzioni di conversione.
- Le funzioni di conversione tra interi senza segno si chiamano combinando le iniziali: `h` = Host, `n` = Network (big endian), `l` = Long (4 byte), `s` = Short (2 byte).
- Ne derivano `htonl()`, `htons()`, `ntohl()` e `ntohs()`, dichiarate in `netinet/in.h` con argomenti `uint32_t` o `uint16_t`.

### `inet_pton()`

La funzione `inet_pton()` converte la notazione dotted di un indirizzo IPv4 o IPv6 in formato binario, riempiendo la struttura `in_addr` (IPv4) o `in6_addr` (IPv6).

```c
indirizzo.sin_family = AF_INET;
if (inet_pton(AF_INET, "143.225.5.3", &indirizzo.sin_addr) != 1)
    perror("inet_pton");
```

- Restituisce `1` in caso di successo, `0` per una stringa non valida e `-1` in caso di errore (es. famiglia non supportata).
- Per l'indirizzo si può usare `INADDR_ANY` con `htonl()`, mentre per IPv6 la costante globale equivalente è `in6addr_any`.

## UDP

> [!def] UDP
> **Protocollo di trasporto** semplice, senza connessione e senza garanzie di affidabilità: mentre TCP trasmette un flusso di byte, UDP invia pacchetti discreti chiamati *datagram*.

- Non richiede handshake di stabilimento o terminazione, quindi introduce meno overhead di TCP e può essere più veloce per piccole quantità di dati.
- Quando una perdita occasionale di dati è accettabile, UDP fornisce una comunicazione molto rapida ed efficiente.

### `sendto()` e `recvfrom()`

L'invio e la ricezione di messaggi in UDP sono eseguiti dalle funzioni `sendto()` e `recvfrom()`, che restituiscono il numero di byte inviati o ricevuti, oppure `-1` in caso di errore.

```c
ssize_t sendto(int sockfd, const void *buf, size_t len, int flags,
               const struct sockaddr *dest_addr, socklen_t addrlen);
ssize_t recvfrom(int sockfd, void *buf, size_t len, int flags,
                 struct sockaddr *src_addr, socklen_t *addrlen);
```

- **`sockfd`**: descrittore del socket su cui inviare o ricevere.
- **`buf`**: puntatore al buffer dei dati da inviare o ricevere.
- **`len`**: numero di byte da inviare, o massimo numero di byte ricevibili.
- **`dest_addr`/`src_addr`**: puntatori alle strutture `sockaddr` con l'indirizzo di destinazione, o in cui viene restituito l'indirizzo del mittente.
- **`addrlen`**: dimensione della struttura di indirizzo, per valore in `sendto()` e per puntatore in `recvfrom()`.
- Con blocking di default `sendto()` può bloccare finché il datagram è accettato dal sistema operativo, senza attendere la consegna al ricevente.
- Con blocking di default `recvfrom()` blocca finché un datagram è disponibile; per non attendere indefinitamente si usano `MSG_DONTWAIT` o un timeout di ricezione (`SO_RCVTIMEO`).
- Se il datagram ricevuto è più grande del buffer, i byte in eccesso sono di norma scartati.

Entrambe le funzioni accettano un parametro `flags` che ne controlla il comportamento.

| Flag | Descrizione |
|---|---|
| `0` | comportamento di default, nessuna opzione speciale |
| `MSG_DONTWAIT` | operazione non bloccante; ritorna subito se bloccerebbe |
| `MSG_PEEK` | legge un datagram senza rimuoverlo dalla coda di ricezione |
| `MSG_TRUNC` | su Linux, recupera la lunghezza completa del datagram anche se il buffer è troppo piccolo |
| `MSG_WAITALL` | attende tutti i byte richiesti; utile soprattutto con TCP, non combina più datagram |

### Flusso di un server UDP

Il ciclo tipico di un server UDP è un loop di ricezione e risposta su un solo socket.

```c
s = socket(AF_INET, SOCK_DGRAM, 0);
bind(s, (struct sockaddr *)&addr, sizeof(addr));
while (1) {
    n = recvfrom(s, buf, sizeof(buf), 0,
                 (struct sockaddr *)&from, &flen);
    sendto(s, buf, n, 0, (struct sockaddr *)&from, flen);
}
```

### Binding implicito

Quando un socket UDP è creato con `socket()` non è ancora associato a una porta locale; il client può lasciare che sia il sistema operativo a farlo.

- Se il client chiama `sendto()` senza prima chiamare `bind()`, il sistema operativo assegna automaticamente una porta locale disponibile (**binding implicito**).
- L'indirizzo IP sorgente è scelto in base all'interfaccia di rete e alla configurazione di routing.
- La porta assegnata resta associata al socket finché non viene chiuso.
- Una successiva chiamata a `bind()` sullo stesso socket fallisce, perché il socket è già associato.

> [!warning] Binding implicito
> Il binding implicito **non stabilisce una connessione** tra client e server.

### Ordine di avvio di client e server

L'esito della comunicazione dipende da quale dei due programmi parte prima.

- **Client prima del server**: se un datagram raggiunge l'host di destinazione ma nessun socket è associato alla porta di destinazione, lo strato UDP lo scarta e può essere generato un messaggio ICMP *Port Unreachable*.
- Il server, quando parte, non può recuperare il datagram perso; il client può restare bloccato su `recvfrom()` o ricevere un errore (es. `ECONNREFUSED`).
- **Server prima del client**: il server chiama `bind()` e attende su `recvfrom()`, poi riceve il datagram e invia la risposta, che il client riceve.

> [!info] Nessun buffering per chi non ascolta
> UDP non mette in coda i datagram per applicazioni che non sono in ascolto, e i datagram persi non sono ritrasmessi automaticamente.

### Timeout di ricezione

Poiché `recvfrom()` è bloccante, è possibile configurare un timeout di ricezione con `setsockopt()` e l'opzione `SO_RCVTIMEO`.

```c
struct timeval timeout = {5, 0};
setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO,
          &timeout, sizeof(timeout));
```

- Se un datagram arriva prima dello scadere del timeout, `recvfrom()` restituisce i dati ricevuti.
- Se nessun datagram arriva entro 5 secondi, `recvfrom()` restituisce `-1` con `errno` pari a `EAGAIN` o `EWOULDBLOCK`.
- Il timeout non ritrasmette i datagram persi.

### Più client su un solo socket

UDP non richiede che una connessione sia stabilita tra client e server, il che semplifica la gestione di più client.

- Un server UDP usa un **solo socket** associato a una porta nota.
- Più client possono inviare datagram allo stesso socket del server.
- Ogni `recvfrom()` riceve un datagram e fornisce indirizzo IP e porta del mittente.
- Il server usa `sendto()` per inviare la risposta al client corrispondente.
- Non sono richiesti `listen()`, `accept()` né un socket separato per ogni client.

### Buffer dei socket UDP

Un socket UDP ha due buffer gestiti dal kernel: un buffer di invio per i datagram in uscita e un buffer di ricezione per quelli in arrivo.

- La dimensione dei due buffer è configurabile con le opzioni `SO_SNDBUF` e `SO_RCVBUF`.
- Ogni `sendto()` invia un datagram UDP completo: socket bloccante, attende finché il datagram può essere accettato; socket non bloccante, restituisce `-1` con `EAGAIN`/`EWOULDBLOCK` se il datagram non può essere accettato.
- UDP non supporta invii parziali: il datagram completo è accettato oppure l'operazione fallisce.
- Ogni `recvfrom()` recupera al più un datagram; se il buffer dell'applicazione è più piccolo del datagram ricevuto, questo è troncato e i byte in eccesso sono scartati, irrecuperabili con ricezioni successive.

## TCP

### Dal socket UDP al modello TCP

A differenza di UDP, in TCP client e server devono completare un handshake prima di trasmettere messaggi; sul lato server servono due socket distinti.

- **Welcoming socket**: sempre attivo, permette ai client di eseguire l'handshake con il server.
- **Socket client-specific**: creato dopo l'handshake, usato da client e server per comunicare.
- Il **three-way handshake** avviene nello strato di trasporto ed è completamente invisibile ai due programmi.
- Una volta che il server accetta la connessione (handshake riuscito), la comunicazione passa al socket appena creato.

### `connect()`

La connessione TCP lato client è eseguita dalla funzione `connect()`, che restituisce `0` in caso di successo e `-1` altrimenti.

```c
int connect(int socket, const struct sockaddr *address,
            socklen_t address_len);
```

- **`socket`**: file descriptor del socket con cui connettersi.
- **`address`**: puntatore a una struttura `sockaddr` con l'indirizzo del server.
- **`address_len`**: lunghezza della struttura, ottenibile con `sizeof()`.

> [!info] `connect()` con UDP
> `connect()` può essere usata anche con UDP: a differenza di TCP **non stabilisce una connessione**, imposta solo un indirizzo di destinazione di default e filtra i datagram in entrata.

### `listen()` e `accept()`

L'attesa di connessioni lato server è eseguita dalle funzioni `listen()` e `accept()`, che operano in combinazione con la `connect()` del client.

```c
int listen(int sockfd, int backlog);
int accept(int sockfd, struct sockaddr *addr,
           socklen_t *addrlen);
```

- `listen()` marca il socket come **listening socket**, pronto ad accettare connessioni; si usa con i tipi orientati alla connessione come `SOCK_STREAM` e `SOCK_SEQPACKET`.
- **`backlog`**: lunghezza massima della coda di connessioni pendenti, cioè quante connessioni completate possono attendere prima che il kernel inizi a rifiutarle o ignorarle.
- `accept()` restituisce un **nuovo descrittore**, oppure `-1`: crea un nuovo socket dedicato a quella connessione, mentre il vecchio socket resta in ascolto.
- Il secondo e terzo argomento di `accept()` identificano il client e possono essere `NULL`.
- `accept()` blocca il processo se non vi sono connessioni in attesa; il socket può essere marcato non bloccante.

> [!info] Due generi di socket sul server
> Il socket di ascolto è creato una volta, associato alla porta nota e **non trasporta mai dati**; ogni `accept()` restituisce un socket di connessione dedicato a un solo client. Un server che serve tre client detiene quattro descrittori.

### Lettura e scrittura

L'invio e la ricezione in TCP sono eseguiti da `read()`, `write()`, `send()` e `recv()`, più semplici delle controparti UDP, e usano la stessa interfaccia della lettura/scrittura su file.

- I socket descriptor si possono passare a processi figli, che non devono distinguere tra socket descriptor e file descriptor.
- Le stesse funzioni si possono usare anche con processi che lavorano su file locali.
- `write(fd, buf, count)`: invia il contenuto del buffer al socket, si usa esclusivamente con `SOCK_STREAM`, e restituisce il numero di byte inviati oppure `-1`; è la stessa funzione della scrittura su file.
- `read(fd, buf, count)`: solo per socket connessi (`SOCK_STREAM`), legge al massimo `count` byte; se non c'è alcun messaggio il programma rimane sospeso (chiamata bloccante); restituisce il numero di byte letti, `-1` in caso di errore, `0` se il peer ha chiuso; è la stessa funzione della lettura da file.

Esistono inoltre funzioni specifiche con modalità aggiuntive: tre varianti di send e tre di receive.

- **`send()`**: come `write()` (richiede connessione stabilita), ma accetta flag per specificare la modalità di scrittura.
- **`sendto()`**: permette la scrittura su socket connectionless, perché richiede l'indirizzo di destinazione.
- **`sendmsg()`**: per specificare buffer multipli.
- **`recv()`**: come `read()` ma con flag.
- **`recvfrom()`**: permette anche di ottenere l'indirizzo della sorgente.
- **`recvmsg()`**: per ricevere da buffer multipli.
- `send()` può essere usata solo se il socket è connesso; `sendto()` sempre; `recv()` e `recvfrom()` ricevono in `buf` al più `len` byte e se `from` non è `NULL` riempiono la struttura `sockaddr` con l'indirizzo del mittente; i flag si possono lasciare a `0`.

I flag abilitano funzionalità extra rispetto a `write()`/`read()`; senza flag il comportamento è lo stesso.

| Flag | Effetto |
|---|---|
| `MSG_DONTWAIT` | non bloccante |
| `MSG_PEEK` | legge senza modificare la coda di ricezione |
| `MSG_WAITALL` | attende finché non si raggiungono `len` byte |
| `MSG_NOSIGNAL` | su `send()`, evita `SIGPIPE` |

- `MSG_DONTWAIT` su `recv()`: non attende i dati (es. polling); su `send()`: non attende se il buffer è pieno.
- `MSG_PEEK` su `recv()`: esamina i dati prima di rimuoverli dalla coda.
- `MSG_WAITALL` su `recv()`: attende finché sono letti `len` byte.

### Opzioni del socket

Le opzioni si leggono e si configurano con `getsockopt()` e `setsockopt()`, che restituiscono `0` in caso di successo e `-1` in caso di errore (con `errno` impostato).

```c
int getsockopt(int sockfd, int level, int optname,
               void *optval, socklen_t *optlen);
int setsockopt(int sockfd, int level, int optname,
               const void *optval, socklen_t optlen);
```

- **`level`**: livello di protocollo in cui l'opzione è definita: `SOL_SOCKET` (opzioni a livello socket), `IPPROTO_TCP` (opzioni TCP), `IPPROTO_IP` (opzioni IPv4).
- **`optname`**: identifica l'opzione.
- **`optval`**: puntatore al valore dell'opzione; in `getsockopt()` `optlen` è un puntatore a una lunghezza di input/output.

#### `SO_REUSEADDR`

> [!def] `SO_REUSEADDR`
> **Opzione a livello socket** (`SOL_SOCKET`) che permette di riutilizzare un indirizzo e una porta locali in certe condizioni, in particolare quando connessioni TCP precedenti sono in `TIME_WAIT`.

- `optval` è un puntatore a un intero: valore non nullo abilita l'opzione, valore zero la disabilita; `optlen` è `sizeof(int)`.
- L'opzione va impostata **prima** di chiamare `bind()`.

```c
int opt = 1;
setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
```

- Alla chiusura di una connessione TCP, l'endpoint che esegue la chiusura attiva entra nello stato **`TIME_WAIT`** per un periodo limitato.
- `TIME_WAIT` serve a due scopi: consentire la ritrasmissione dell'ACK finale se il peer ritrasmette il suo FIN, e far scadere i segmenti ritardati della vecchia connessione prima che gli stessi identificatori di connessione siano riusati.
- Le connessioni in `TIME_WAIT` possono impedire a un nuovo socket di fare `bind()` sullo stesso indirizzo e porta: riavviare un server TCP poco dopo lo stop può fallire con *Address already in use*.
- `SO_REUSEADDR` consente il riuso, secondo le regole del sistema operativo; non consente normalmente a due server TCP di ascoltare sullo stesso IP e porta contemporaneamente.

#### `SO_REUSEPORT`

> [!def] `SO_REUSEPORT`
> **Opzione a livello socket** (non parte dello standard POSIX) che permette a più socket di fare `bind()` sullo stesso indirizzo IP e sulla stessa porta.

- Con TCP, più socket possono chiamare indipendentemente `listen()` sullo stesso endpoint: il kernel distribuisce le connessioni in arrivo tra i socket in ascolto, fornendo un bilanciamento di carico integrato.
- Il kernel organizza i socket compatibili in una **reuseport group** e su Linux distribuisce le connessioni con selezione basata su hash; ogni socket in ascolto ha la propria coda di `accept()`.
- L'opzione va abilitata su ogni socket prima di chiamare `bind()`.
- È utile per il bilanciamento di carico tra processi o thread, per server ad alte prestazioni multicore e per ridurre la contesa su un singolo socket in ascolto.
- Su Linux i processi che condividono lo stesso indirizzo e porta devono avere lo stesso effective user ID.

### Buffer dei socket TCP

Anche i socket TCP hanno due buffer: un buffer di ricezione per i dati in entrata e un buffer di invio per i dati in uscita, entrambi in spazio kernel.

- Le dimensioni si configurano con `SO_SNDBUF` (invio) e `SO_RCVBUF` (ricezione).
- Un buffer di invio più ampio può accodare più dati in uscita riducendo il blocking in `send()`; un buffer di ricezione più ampio riduce il rischio di stalli del controllo di flusso TCP.
- `write()` può restituire **meno byte di quelli richiesti**: il valore di ritorno indica i byte accettati per la trasmissione, non necessariamente consegnati al ricevente.
- Socket bloccante: `write()` attende che tutti i byte richiesti siano accettati nel buffer, salvo interruzioni o timeout di invio; socket non bloccante: restituisce subito un conteggio parziale oppure `EAGAIN`/`EWOULDBLOCK`.
- `read()` con `n` byte copia dal buffer di ricezione fino a `n` byte: socket bloccante, restituisce subito i byte disponibili senza attendere il riempimento del buffer, e blocca solo se non c'è alcun dato; socket non bloccante, restituisce i byte disponibili oppure `-1` con `EAGAIN`/`EWOULDBLOCK`.
- Un valore di ritorno `0` indica che il peer ha chiuso il lato di invio e tutti i dati pendenti sono stati letti.

Un esempio con `write(sockfd, buffer, 1000)` mostra le differenze tra le due modalità.

| Spazio libero nel buffer di invio | `write()` bloccante | `write()` non bloccante |
|---|---|---|
| 0 byte | attende spazio libero | `-1` (`EAGAIN`/`EWOULDBLOCK`) |
| 300 byte | normalmente attende di trasferire tutti i 1000 byte | può restituire 300 |
| 1000 byte | normalmente restituisce 1000 | normalmente restituisce 1000 |

Un esempio con `read(sockfd, buffer, 1000)` è speculare.

| Dati disponibili | `read()` bloccante | `read()` non bloccante |
|---|---|---|
| 0 byte | attende i dati | `-1` (`EAGAIN`/`EWOULDBLOCK`) |
| 300 byte | normalmente restituisce 300 | normalmente restituisce 300 |
| 1000 byte | può restituire 1000 | può restituire 1000 |

### Modalità non bloccante

Il metodo POSIX per rendere non bloccante un descrittore è impostare il flag `O_NONBLOCK` con `fcntl()`.

```c
int flags = fcntl(fd, F_GETFL, 0);
fcntl(fd, F_SETFL, flags | O_NONBLOCK);
```

- `recv()`/`read()`: restituiscono `-1` con `EAGAIN` o `EWOULDBLOCK` se non ci sono dati disponibili.
- `send()`/`write()`: restituiscono `-1` con `EAGAIN` o `EWOULDBLOCK` se i dati non possono essere accettati immediatamente.
- `connect()`: può restituire `-1` con `EINPROGRESS` mentre la connessione viene stabilita.
- Il meccanismo vale per TCP, UDP, pipe e altri file descriptor supportati.
- `MSG_DONTWAIT` abilita il comportamento non bloccante **per una singola chiamata** a `send()` o `recv()`, senza cambiare la modalità del socket.

### Lettura e scrittura complete

Poiché `read()` e `write()` possono trasferire meno byte di quelli richiesti, per leggere o scrivere `n` byte in sicurezza servono cicli che ripetono l'operazione finché tutti i byte sono trasferiti.

- Su **`EINTR`** la chiamata è stata interrotta da un segnale: si riprova.
- Su ritorno `0` la connessione è stata chiusa: ci si ferma restituendo i byte trasferiti fino a quel momento.

```c
while (sent < n) {
    w = send(fd, p + sent, n - sent, 0);
    if (w < 0) { if (errno == EINTR) continue; return -1; }
    sent += w;
}
```

## Server concorrenti

Un generico server attende le richieste di connessione su una porta determinata, ma le richieste possono arrivare in modo concorrente da molteplici client.

- Soluzione senza programmazione concorrente: i client sono serviti **uno alla volta**; finché una connessione non è terminata non vengono serviti gli altri client interessati al servizio.
- Il tempo di attesa di ogni client dipende dalla durata delle altre connessioni e può risultare eccessivo.
- Se le connessioni durano molto, il server ben presto diverrebbe indisponibile anche solo ad accodare le nuove richieste; nei server reali le richieste dei vari client vanno gestite concorrentemente.
- Anche in un server sequenziale è comunque il sistema operativo a gestire le richieste concorrenti, che di fatto serializza.

### Server a processi con `fork()`

Un server concorrente genera un processo ad hoc per ogni client, così che più client siano serviti in modalità concorrente; l'attesa in coda si limita alla gestione della richiesta e all'avvio del nuovo processo.

```c
while (1) {
    fd2 = accept(fd1, NULL, NULL);
    if ((pid = fork()) == 0) {  // processo figlio
        close(fd1);             // al figlio non serve fd1
        /* gestisce la connessione con fd2 */
        exit(0);
    }
    close(fd2);                 // il padre ripete il ciclo
}
```

- Il figlio chiude il socket di ascolto `fd1` e gestisce la connessione con `fd2`; il padre chiude `fd2` e ripete il ciclo.

Per evitare processi **zombie** si installa un gestore di `SIGCHLD` che raccoglie tutti i figli terminati.

- Il gestore chiama `waitpid(-1, NULL, WNOHANG)` in un ciclo, senza bloccarsi se non ci sono figli.
- La registrazione avviene con `sigaction()`, impostando `SA_RESTART` perché le system call interrotte (`accept()`, `recv()`) vengano riavviate automaticamente.

### Server multithreaded

In alternativa ai processi si può servire ogni connessione con un thread.

```c
connect_sd = accept(listen_sd, NULL, NULL);
int *thread_sd = malloc(sizeof(int));
*thread_sd = connect_sd;
pthread_create(&tid, NULL, gestisci, thread_sd);
pthread_detach(tid);
```

- `malloc()` fornisce un contenitore separato per il descrittore di ogni thread, evitando race condition nel passaggio degli argomenti.
- `pthread_detach()` fa sì che le risorse del thread siano rilasciate automaticamente alla sua terminazione, senza chiamare `pthread_join()`.

### Più connessioni sulla stessa porta

Un server TCP può gestire più connessioni simultanee su una sola porta in ascolto.

- Il server crea il socket in ascolto con `socket()`, `bind()` e `listen()`.
- Ogni `accept()` restituisce un nuovo socket connesso, mentre il socket in ascolto resta disponibile per le nuove connessioni.
- Tutti i socket connessi condividono la stessa porta locale del server.
- Ogni connessione TCP è identificata univocamente da una **4-tupla**: (Source IP, Source Port, Destination IP, Destination Port).
- Il numero di connessioni è limitato dalle risorse di sistema, non dalla sola porta in ascolto.

Le principali limitazioni al numero di connessioni simultanee sono le seguenti.

- **File descriptor**: ogni socket connesso richiede un file descriptor; il sistema operativo impone limiti per processo e di sistema.
- **Memoria del kernel**: ogni connessione TCP richiede strutture di controllo e buffer di invio/ricezione.
- **Risorse CPU**: gestire molte connessioni attive aumenta l'overhead di elaborazione.
- **Porte sorgente dei client**: le connessioni dallo stesso IP client verso lo stesso endpoint server richiedono porte sorgente distinte (numeri a 16 bit).
- **Architettura del server**: un modello a processo o thread per client consuma più risorse di un I/O multiplexing event-driven.

> [!info] Esaurimento delle porte sorgente
> L'esaurimento delle porte sorgente limita le connessioni **da un particolare IP client** verso uno specifico endpoint server, non il numero totale di connessioni che un server può accettare.

## Multiplexing I/O con `select()`

> [!def] `select()`
> **Funzione di I/O multiplexing** che attende eventi di I/O su più socket simultaneamente e permette all'applicazione di identificare quali socket sono pronti per la lettura o la scrittura.

- Evita di bloccarsi su un socket mentre altri hanno dati disponibili.
- Elimina la necessità di un thread o processo separato per ogni client.
- È utile per gestire più client in un server **single-threaded**.

```c
#include <sys/select.h>
int select(int nfds, fd_set *readfds, fd_set *writefds,
           fd_set *exceptfds, struct timeval *timeout);
```

- `select()` blocca finché uno di questi eventi si verifica: un descrittore diventa pronto in lettura o scrittura; occorre una condizione eccezionale su un descrittore monitorato; scade il timeout; una signal interrompe la chiamata.
- Valore di ritorno: `-1` in caso di errore (`errno` impostato), `0` se il timeout è scaduto, valore positivo pari al numero totale di descrittori pronti negli insiemi restituiti.

### Insiemi di descrittori

I tre insiemi di descrittori da monitorare sono puntatori a variabili `fd_set`, tipicamente implementate come bitmask.

- **`readfds`**: descrittori da monitorare in lettura; ad esempio un listening socket è pronto quando si può accettare una connessione con `accept()`.
- **`writefds`**: descrittori da monitorare in scrittura.
- **`exceptfds`**: descrittori da monitorare per condizioni eccezionali (spesso `NULL`).
- **`nfds`**: specifica l'intervallo di descrittori esaminati; se `maxfd` è il descrittore più alto monitorato, allora `nfds = maxfd + 1`.
- `FD_SETSIZE` definisce la capacità di un `fd_set` (tipicamente 1024 su Linux).

Gli insiemi `fd_set` si manipolano con quattro macro.

| Macro | Effetto |
|---|---|
| `FD_SET(fd, set)` | aggiunge `fd` all'insieme |
| `FD_CLR(fd, set)` | rimuove `fd` dall'insieme |
| `FD_ISSET(fd, set)` | restituisce vero se `fd` è nell'insieme |
| `FD_ZERO(set)` | svuota l'insieme |

- Dopo il ritorno di `select()`, `FD_ISSET()` verifica se un descrittore è pronto (0 = non pronto, non-zero = pronto).

> [!warning] Gli insiemi sono modificati
> `select()` **modifica gli insiemi** passati: vanno ricostruiti prima di ogni chiamata.

### Condizioni di prontezza

`select()` identifica i descrittori pronti per operazioni di I/O senza bloccarsi.

Un socket è pronto in lettura (`readfds`) quando si verifica una di queste condizioni.

- Ci sono dati nel buffer di ricezione (`SO_RCVLOWAT`, default: 1 byte).
- Il peer ha chiuso il suo lato di invio (EOF).
- C'è un errore pendente sul socket.
- Un listening socket ha connessioni in attesa di `accept()`.

Un socket è pronto in scrittura (`writefds`) quando si verifica una di queste condizioni.

- C'è spazio sufficiente nel buffer di invio per un'operazione di scrittura.
- Un tentativo di connessione non bloccante è completato (con successo o con errore).
- C'è un errore pendente sul socket.

> [!warning] Prontezza in scrittura
> La prontezza in scrittura **non garantisce** che una `send()` di grandi dimensioni completi senza bloccare.

L'insieme `exceptfds` monitora condizioni eccezionali: per TCP è usato principalmente per rilevare dati **Out-of-Band (OOB)**.

- TCP segnala dati urgenti con il flag `URG`.
- Su Linux i dati urgenti si ricevono con `recv()` e il flag `MSG_OOB`.

### Timeout

Il parametro `timeout` specifica il tempo massimo per cui `select()` attende che un descrittore diventi pronto.

```c
struct timeval {
    time_t tv_sec;        // secondi
    suseconds_t tv_usec;  // microsecondi
};
```

- **`timeout == NULL`**: `select()` blocca indefinitamente finché un descrittore non diventa pronto o la chiamata è interrotta.
- **`tv_sec == 0 && tv_usec == 0`**: `select()` restituisce immediatamente senza bloccare (polling).
- **Timeout non nullo**: `select()` attende al massimo il tempo specificato, ma ritorna prima se uno o più descrittori diventano pronti.

### Server e client multiplexing

Un server multiplexing gestisce più client con un solo processo o thread, monitorando sia il socket di ascolto sia i socket dei client connessi.

- Si inizializzano le strutture `fd_set` per la lettura (e, se serve, la scrittura) e vi si aggiungono il listening socket e i socket dei client connessi.
- Quando `select()` ritorna: se il listening socket è pronto si accetta una nuova connessione e il nuovo descrittore entra nell'insieme; se un socket client è pronto si leggono o scrivono dati su di esso.
- Il contatore dei descrittori pronti va decrementato a ogni gestione e il ciclo su di essi si interrompe quando raggiunge zero.
- Alla chiusura di un client (`recv()` restituisce 0 o errore): `close()`, `FD_CLR()` e rimozione del descrittore dalla lista dei client.
- Un server single-threaded può così gestire più client senza creare thread o processi per ogni connessione.

Un client multiplexing monitora in lettura due descrittori.

- **Standard input** (`stdin`): per leggere i messaggi digitati dall'utente.
- **Socket connesso** (`sockfd`): per ricevere i messaggi dal server.
- Con `select()` il client risponde al descrittore che diventa pronto, senza bloccarsi sull'altro.

## Broadcast e multicast

Broadcast e multicast sono meccanismi a livello IP, usati comunemente con socket UDP (non standard TCP).

- **Broadcast**: supportato da IPv4.
- **Multicast**: supportato da IPv4 e IPv6.
- IPv6 non ha il broadcast: si usa il multicast al suo posto.

### Broadcast

> [!def] Broadcast
> **Invio** di dati a tutti gli host di una rete locale, senza richiedere l'adesione a un gruppo.

- A livello rete IPv4 permette l'invio di un pacchetto a tutti gli host di una rete; nella programmazione di socket si usa tipicamente con UDP, perché UDP supporta la comunicazione connectionless, mentre TCP non supporta il broadcast.
- **Directed broadcast**: `192.168.1.255`, dipende dalla subnet mask.
- **Limited broadcast**: `255.255.255.255`, non inoltrato dai router.
- Mittente: crea un socket con `socket(AF_INET, SOCK_DGRAM, 0)`, abilita il broadcast con `setsockopt()` e `SO_BROADCAST`, e invia il datagram all'indirizzo di broadcast e alla porta di destinazione con `sendto()`.
- Ricevente: crea un socket UDP, fa `bind()` su `INADDR_ANY` e sulla porta di destinazione, e riceve i datagram con `recvfrom()`.

### Multicast

> [!def] Multicast
> **Invio** di datagram UDP a un gruppo di riceventi identificati da un indirizzo IP multicast (es. `239.255.0.1`).

- Per ricevere datagram multicast un socket deve **aderire al gruppo** con l'opzione `IP_ADD_MEMBERSHIP`.
- Il mittente imposta il TTL dei pacchetti multicast in uscita con `IP_MULTICAST_TTL`; con TTL pari a 1 il pacchetto resta nella LAN locale.
- Il ricevente imposta `SO_REUSEADDR` (con `SO_REUSEPORT` per permettere a più client di fare `bind` sullo stesso indirizzo), fa `bind()` su `INADDR_ANY` e sulla porta, aderisce al gruppo e riceve in un ciclo.

```c
struct ip_mreq mreq;
inet_pton(AF_INET, "239.255.0.1", &mreq.imr_multiaddr);
mreq.imr_interface.s_addr = htonl(INADDR_ANY); // interfaccia scelta dall'OS
setsockopt(sock, IPPROTO_IP, IP_ADD_MEMBERSHIP, &mreq, sizeof(mreq));
```

- La struttura `ip_mreq` specifica l'indirizzo del gruppo multicast e l'interfaccia di rete locale da usare.

Quando un'applicazione aderisce a un gruppo multicast, sistema operativo e rete cooperano alla gestione della comunicazione.

- **Group membership**: il ricevente richiede l'adesione con `IP_ADD_MEMBERSHIP`.
- **Sistema operativo**: gestisce la richiesta e comunica le informazioni necessarie alla rete locale.
- **Rete**: i router multicast-aware usano le informazioni di appartenenza per inoltrare i pacchetti verso le reti con riceventi interessati.
- **Consegna dei dati**: il mittente invia i datagram all'indirizzo IP multicast senza conoscere i singoli riceventi.

> [!info] Socket option e rete
> Le socket option permettono alle applicazioni di richiedere comportamenti a livello di rete, mentre la rete sottostante gestisce la consegna dei pacchetti.

## Risoluzione dei nomi DNS

I socket Berkeley funzionano solo con indirizzi IP, ma su Internet gli host sono tipicamente identificati da hostname.

- Gli hostname appartengono al livello applicativo, mentre i socket operano al livello di trasporto: per connettersi tramite hostname serve la traduzione DNS per ottenere l'indirizzo IP da passare al socket.
- C/C++ offre funzioni e strutture che contattano i server DNS e recuperano gli indirizzi.

### `gethostbyname()`

> [!def] `gethostbyname()`
> **Funzione legacy** che risolve un hostname in indirizzi IPv4 tramite il resolver di sistema, restituendo una struttura `hostent` (`NULL` in caso di errore).

- La struttura non contiene solo l'indirizzo IP, ma informazioni sull'host: nome canonico, eventuali alias, uno o più indirizzi.
- Un DNS può restituire una lista di indirizzi, in ordine anche casuale se la query arriva a server round-robin.
- Il primo elemento della lista si ottiene con `h_addr_list[0]` (o `h_addr`); l'indirizzo risolto può inizializzare una `sockaddr_in`.

```c
struct hostent {
    char  *h_name;      // nome originale dell'host (canonico)
    char **h_aliases;   // array di alias, terminato da NULL
    int    h_addrtype;  // famiglia dell'indirizzo (tipicamente AF_INET)
    int    h_length;    // lunghezza dell'indirizzo (tipicamente 4 byte)
    char **h_addr_list; // array di indirizzi, terminato da NULL
};
```

- Esiste anche `gethostbyaddr()`, che restituisce una struttura `hostent` per un indirizzo IP specificato.

### `getaddrinfo()`

> [!def] `getaddrinfo()`
> **Funzione moderna** che risolve un hostname in uno o più indirizzi IP (IPv4/IPv6) con un'interfaccia unificata, restituendo le informazioni necessarie per creare e connettere un socket.

- Restituisce una lista concatenata di strutture `addrinfo` contenenti le informazioni pronte per `socket()` e `connect()`.
- La struttura `hints` specifica i criteri con cui `getaddrinfo()` seleziona gli indirizzi adatti; `res` punta alla lista collegata degli indirizzi corrispondenti.

```c
struct addrinfo hints, *res;
memset(&hints, 0, sizeof(hints));
hints.ai_family = AF_UNSPEC;      // IPv4 + IPv6
hints.ai_socktype = SOCK_STREAM;   // TCP
err = getaddrinfo("www.example.com", "80", &hints, &res);
```

- **`ai_family`**: famiglia di indirizzi (`AF_INET`, `AF_INET6`, `AF_UNSPEC`).
- **`ai_socktype`**: tipo di socket (`SOCK_STREAM`, `SOCK_DGRAM`).
- **`ai_protocol`**: protocollo di trasporto specifico (`0` = non specificato).
- **`ai_flags`**: opzioni aggiuntive che controllano la risoluzione degli indirizzi.

Gli indirizzi restituiti si usano in sequenza finché uno non si connette.

```c
for (p = res; p != NULL; p = p->ai_next) {
    sock = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
    if (connect(sock, p->ai_addr, p->ai_addrlen) == 0)
        break;  // connesso
    close(sock);
}
freeaddrinfo(res);
```

- `p->ai_addr` si può usare direttamente con `connect()`; per accedere all'IP e stamparlo va fatto il cast a `sockaddr_in` (IPv4) o `sockaddr_in6` (IPv6).
- `freeaddrinfo()` libera la memoria allocata dinamicamente da `getaddrinfo()`.

### Richieste HTTP su socket TCP

Una richiesta HTTP su un socket TCP specifica tre elementi: hostname del server web, numero di porta e path della risorsa da recuperare.

- La stringa di richiesta contiene metodo, path e versione del protocollo, e si invia con `send()`; la risposta si riceve con `recv()` in un ciclo fino alla chiusura della connessione da parte del server.