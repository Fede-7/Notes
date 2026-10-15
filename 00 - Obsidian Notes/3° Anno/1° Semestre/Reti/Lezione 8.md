# Application Layer programmazione di rete

## Creare applicazioni di rete

La maggior parte delle applicazioni di rete include un programma **lato client** e uno **lato server** che comunicano tramite la rete: all'esecuzione si creano un **processo client** e un **processo server**, che comunicano leggendo e scrivendo su **socket**.

Scelte di progettazione:

- **Protocolli aperti**: protocolli le cui regole sono pubbliche.
- **Protocolli proprietari**: protocolli "custom", non pubblicati in un RFC o altrove.
- **Trasporto**: due protocolli disponibili:
  - **TCP**: orientato alla connessione, fornisce un canale affidabile di byte-stream tra i due sistemi finali.
  - **UDP**: connectionless, invia pacchetti indipendenti senza garanzie di consegna.

> [!info] Socket
> **Elemento centrale** della creazione di applicazioni di rete: implementano (come scatola nera) le funzionalità dei livelli **trasporto** (UDP/TCP) e **rete** (IP); esistono middleware che le incapsulano semplificandone l'uso, ma le API di base restano diffusissime.

Le API di base per socket UDP e TCP sono disponibili in quasi tutti i linguaggi e sistemi operativi (C, C++, C#, Java, Perl, Python, Matlab, ecc.); l'implementazione e l'uso dipendono dalla configurazione delle macchine. Nel dominio Unix si usano le **Berkeley socket** (dette BSD o POSIX socket), API native C, sia per TCP sia per UDP.

## Connessione connectionless vs connection-oriented

**Connectionless (UDP)** — procedura del client e del server:

1. Client: crea la socket.
2. Server: crea la socket e la **lega** (`bind`) a porta e indirizzo.
3. Client: invia il messaggio (`sendto`) senza contattare prima il server.
4. Server: legge il messaggio (`recvfrom`), ricavandone IP e porta del client.
5. Server: invia la risposta (`sendto`).
6. Client: legge la risposta (`recvfrom`) e chiude la socket; il server chiude la socket.

**Connection-oriented (TCP)** — procedura del client e del server:

1. Client: crea la socket e **si connette** (`connect`) al server.
2. Server: crea la socket, la lega a porta/indirizzo, si mette in **ascolto** (`listen`) e **accetta** (`accept`) le connessioni.
3. Client: invia il messaggio (`send`); server: legge il messaggio (`read`) e risponde (`send`).
4. Client: legge la risposta (`read`); il server chiude la socket **specifica del client** e può tornare ad `accept` per altri client; il client chiude la propria socket.

Le fasi comuni sono **creazione**, **connessione**, **messaggistica** e **distruzione**: UDP va diretta alla messaggistica, TCP prevede la fase di connessione.

## Strutture e funzioni delle socket in C

La struttura che definisce indirizzi e porte degli host:

```c
struct sockaddr_in {
    short   sin_family; // famiglia dell'indirizzo, tipicamente AF_INET (IPv4)
    unsigned short sin_port;   // numero di porta, es. htons(3490)
    struct in_addr sin_addr;  // indirizzo IP (vedi sotto)
    char    sin_zero[8]; // zeri: la struttura ha la dimensione di sockaddr
};
struct in_addr {
    unsigned long s_addr; // IP, caricato con inet_addr() o INADDR_ANY
};
```

Le funzioni principali dell'API (in `<sys/socket.h>`):

- **`socket(domain, type, protocol)`**: crea la socket e restituisce il **file descriptor** `sockfd`.
  - `domain`: famiglia (`AF_INET`).
  - `type`: `SOCK_STREAM` per TCP, `SOCK_DGRAM` per UDP.
  - `protocol`: spesso `0` (nessun protocollo specifico).
- **`bind(socket, address, address_len)`**: associa la socket a indirizzo e porta locali; restituisce 0 in caso di successo, `-1` altrimenti.
  - `address.sin_addr` spesso impostato a `INADDR_ANY` per ascoltare connessioni da **tutti** gli indirizzi (IP multipli).
  - Usata **sui server** (che devono legare una porta nota); sul client è opzionale, perché il SO assegna automaticamente una porta libera.
- **`sendto(osock, obuf, olen, oflags, oaddr, oaddr_len)`** / **`recvfrom(isock, ibuf, ilen, iflags, iaddr, iaddr_len)`**: invio e ricezione UDP; restituiscono il numero di byte effettivamente inviati/ricevuti.
  - `obuf`/`ibuf`: buffer del messaggio; `olen`/`ilen`: lunghezze in byte.
  - `flags`: tipicamente `0` o `MSG_WAITALL` (attende tutti i byte).
  - `oaddr`/`iaddr`: strutture `sockaddr` con l'indirizzo del ricevente/del mittente; `recvfrom` riempie `iaddr` con IP e porta del client.
- **`close(socket)`**: chiude la socket (0 successo, `-1` errore), secondo la filosofia Unix "everything is a file".

## Dal UDP al TCP

A differenza di UDP, in TCP client e server devono fare **handshake** prima di trasmettere; sul server si usano **due socket**:

- **Welcoming socket**: sempre attiva, permette ai client di fare handshake col server.
- **Socket client-specifica**: creata **dopo** il handshake, usata da client e server per comunicare.

Il three-way handshake avviene **dentro il livello trasporto** ed è completamente **invisibile** ai programmi client e server; accettata la connessione, la comunicazione passa alla socket appena creata.

Funzioni aggiuntive TCP:

- **`connect(socket, address, address_len)`** (client): apre la connessione verso l'indirizzo del server contenuto nella `sockaddr`; 0 successo, `-1` errore.
- **`listen(socket, backlog)`** (server): apre la **coda** delle connessioni in arrivo; `backlog` è la lunghezza massima della coda di connessioni pendenti.
- **`accept(socket, address, address_len)`** (server): apre la **socket client-specifica**, restituita come nuovo descrittore `new_sockfd`; l'indirizzo del client connesso è riportato nella struttura `sockaddr` puntata.
- **`send(osock, obuf, olen, flags)`** / **`read(isock, ibuf, ilen)`**: invio e ricezione TCP, più semplici delle controparti UDP: gli indirizzi di client e server sono già stati specificati in fase di connessione, quindi non servono qui.

## Esempio minimo UDP

Schema essenziale del client (il server specula):

```c
sockfd = socket(AF_INET, SOCK_DGRAM, 0);
memset(&servaddr, 0, sizeof(servaddr));
servaddr.sin_family = AF_INET;
servaddr.sin_port = htons(8080);
servaddr.sin_addr.s_addr = INADDR_ANY;
sendto(sockfd, hello, strlen(hello), 0,
       (struct sockaddr *) &servaddr, sizeof(servaddr));
n = recvfrom(sockfd, buffer, 1024, MSG_WAITALL,
             (struct sockaddr *) &servaddr, &len);
close(sockfd);
```

Osservazioni sul client e sul server UDP:

- Il client **non fa `bind`**: è il SO a scegliere una porta libera; il server invece crea la socket, la imposta con `INADDR_ANY` e la lega alla porta scelta prima di ricevere.
- Per parlare con un altro computer si usa `inet_addr()` al posto di `INADDR_ANY` (es. `inet_addr("192.168.1.10")`).
- Il server riceve con `recvfrom` (che riempie `cliaddr` con IP e porta del client) e risponde con `sendto` verso `cliaddr`.

Osservazioni sul server TCP:

- Il server crea la socket, fa `bind` alla porta, `listen` e `accept`; poi legge e scrive sulla socket **client-specifica** (`read`/`send`).
- A comunicazione finita chiude la socket client-specifica e la socket di benvenuto, oppure torna ad `accept` per accogliere un altro client.