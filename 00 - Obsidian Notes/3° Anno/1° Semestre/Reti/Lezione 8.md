# Lezione 8: Programmazione di rete (socket)

## Creare applicazioni di rete

La maggior parte delle applicazioni di rete include un programma **lato client** e uno **lato server** che comunicano attraverso la rete. Eseguendo questi due programmi si creano **un processo client e un processo server**, che comunicano leggendo e scrivendo su **socket**.

### Scelta dei protocolli

I protocolli si dividono in **aperti**, le cui regole sono pubbliche, e **proprietari**, protocolli "custom" non pubblicati apertamente in un RFC o altrove. Per il trasporto ci sono due protocolli utilizzabili: **TCP** (*Transmission Control Protocol*), **orientato alla connessione**, che fornisce un canale affidabile a flusso di byte tra i due sistemi finali, e **UDP** (*User Datagram Protocol*), **senza connessione**, che invia pacchetti indipendenti da un sistema finale all'altro senza garanzie di consegna.

## Socket

I **socket** sono un elemento centrale della creazione di applicazioni di rete: implementano (in modo "black-box") le funzionalità dei livelli di trasporto (UDP/TCP) e di rete (IP). Esistono applicazioni (middleware) che possono **incapsulare i socket**, semplificandone la creazione e fornendo funzionalità più complesse; tuttavia **le API di base restano molto usate**. I socket UDP e TCP sono disponibili in quasi **tutti i linguaggi e sistemi operativi** (C, C++, C#, Java, Perl, Python, Matlab, ecc.), e l'implementazione sottostante e l'uso dipendono dalla configurazione delle macchine. Nel dominio Unix si usano i **Berkeley socket** (detti anche BSD o POSIX socket) per TCP e UDP: API C native.

### Definizioni (strutture in C)

```c
#include <netinet/in.h>
#include <arpa/inet.h>   // per inet_addr()
#include <sys/types.h>   // alcuni tipi custom

struct sockaddr_in {
    short sin_family;         // famiglia, tipicamente AF_INET (IPv4)
    unsigned short sin_port;  // numero di porta, es. htons(3490)
    struct in_addr sin_addr;
    char sin_zero[8];         // tipicamente zeri: la struttura ha la stessa
                              // dimensione di sockaddr e può esserle "castata"
};

struct in_addr {
    unsigned long s_addr;     // indirizzo IP: inet_addr() o INADDR_ANY per localhost
};
```

### Creazione: socket()

```c
#include <sys/socket.h>

int sockfd = socket(int domain, int type, int protocol);
```

I parametri sono: `domain`, la famiglia di indirizzi (es. `AF_INET`); `type`, il tipo di socket (`SOCK_STREAM` per TCP, `SOCK_DGRAM` per UDP); `protocol`, il protocollo specifico da usare nel socket (spesso 0, nessun protocollo particolare). Il valore restituito `sockfd` è un file descriptor che identifica il socket appena creato: i socket seguono la filosofia Unix "tutto è un file", per cui le sorgenti di I/O sono trattate come file, con file descriptor associato.

### Associazione: bind()

```c
#include <sys/socket.h>

int val = bind(int socket, const struct sockaddr *address, socklen_t address_len);
```

`socket` è il file descriptor del socket da associare; `address` è un puntatore a una struttura `sockaddr` che specifica porta e indirizzo (`address.sin_addr` è spesso impostato a `INADDR_ANY`, così da ascoltare connessioni da tutti gli indirizzi, IP multipli); `address_len` è la lunghezza della struttura `sockaddr` (si può usare `sizeof()`); `val` vale 0 in caso di successo, −1 altrimenti. Si noti che bind **si usa sui server** (il socket va legato a una porta specifica) ed è **opzionale sui client**, poiché il sistema operativo assegna automaticamente una porta libera.

### Invio e ricezione (UDP)

```c
#include <sys/socket.h>

int ob = sendto(int osock, const void *obuf, size_t olen, int oflags,
                const struct sockaddr *oaddr, socklen_t oaddr_len);
int ib = recvfrom(int isock, void *ibuf, size_t ilen, int iflags,
                  struct sockaddr *iaddr, socklen_t *iaddr_len);
```

- `osock`/`isock`: file descriptor su cui inviare/ricevere il messaggio.
- `obuf`/`ibuf`: puntatori ai buffer con il messaggio da inviare/ricevere.
- `olen`/`ilen`: lunghezze dei messaggi in byte.
- `oflags`/`iflags`: flag (tipicamente 0 o `MSG_WAITALL` per attendere tutti i byte).
- `oaddr`/`iaddr`: puntatori a `sockaddr` con l'indirizzo del ricevente/mittente.
- `oaddr_len`/`iaddr_len`: lunghezza in byte della struttura `sockaddr`.
- `ob`/`ib`: numero di byte effettivamente inviati/ricevuti.

### Chiusura: close()

```c
#include <unistd.h>

int val = close(int socket);
```

`socket` è il file descriptor del socket da chiudere; `val` vale 0 in caso di successo, −1 altrimenti.

## Esempio UDP in C/C++

### Client

```cpp
int main() {
    int sockfd;
    char buffer[1024];
    const char *hello = "Hello from client";
    struct sockaddr_in servaddr;

    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(8080);
    servaddr.sin_addr.s_addr = INADDR_ANY;

    int n;
    socklen_t len;

    sendto(sockfd, (const char *)hello, strlen(hello),
           0, (const struct sockaddr *)&servaddr, sizeof(servaddr));
    std::cout << "Hello message sent." << std::endl;

    n = recvfrom(sockfd, (char *)buffer, 1024,
                 MSG_WAITALL, (struct sockaddr *)&servaddr, &len);
    buffer[n] = '\0';
    std::cout << "Received \"" << buffer << "\"" << std::endl;

    close(sockfd);
    return 0;
}
```

> Nota: per comunicare con un altro computer usare `inet_addr()` al posto di `INADDR_ANY` (es. `inet_addr("192.168.1.10")`).

### Server

```cpp
int main() {
    int sockfd;
    char buffer[1024];
    const char *hello = "Hello from server";
    struct sockaddr_in servaddr, cliaddr;

    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(8080);

    if (bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    socklen_t len = sizeof(cliaddr);
    int n;

    n = recvfrom(sockfd, (char *)buffer, 1024,
                 MSG_WAITALL, (struct sockaddr *)&cliaddr, &len);
    buffer[n] = '\0';
    std::cout << "Received \"" << buffer << "\"" << std::endl;

    sendto(sockfd, (const char *)hello, strlen(hello),
           0, (const struct sockaddr *)&cliaddr, len);
    std::cout << "Hello message sent." << std::endl;

    close(sockfd);
    return 0;
}
```

## Da UDP a TCP

Diversamente da UDP, in TCP client e server devono fare **handshake** prima di trasmettere messaggi. Sul lato server si usano **due socket**: un **welcoming socket**, sempre attivo, con cui i client fanno l'handshake col server, e un **socket specifico del client**, creato dopo l'handshake e usato da client e server per comunicare. Il three-way handshake, che avviene nel livello di trasporto, è completamente **invisibile ai programmi client e server**; accettata la connessione (handshake riuscito), **la comunicazione passa al nuovo socket creato**.

### Connessione lato client: connect()

```c
#include <sys/socket.h>

int val = connect(int socket, const struct sockaddr *address, socklen_t address_len);
```

`socket` è il file descriptor del socket con cui connettersi; `address` è un puntatore a `sockaddr` con l'indirizzo del server; `address_len` è la lunghezza della struttura (si può usare `sizeof()`); `val` vale 0 in caso di successo, −1 altrimenti.

### Attesa di connessione lato server: listen() e accept()

Queste funzioni funzionano in combinazione con la `connect()` del client: `listen()` apre una coda dove sono messe le connessioni in arrivo, mentre `accept()` apre il socket specifico del client.

```c
#include <sys/socket.h>

int val = listen(int socket, int backlog);
int new_sockfd = accept(int socket, struct sockaddr *address, socklen_t *address_len);
```

- `socket`: file descriptor del socket su cui attendere connessioni (deve essere in bind su indirizzo/porta).
- `backlog`: lunghezza massima della coda di connessioni pendenti.
- `address`: può essere NULL, o un puntatore a `sockaddr` dove verrà restituito l'indirizzo del socket che si connette.
- `address_len`: lunghezza dell'indirizzo.
- `new_sockfd`: nuovo descrittore di socket su cui client e server comunicheranno.
- `val`: 0 in caso di successo, −1 altrimenti.

### Invio e ricezione (TCP)

```c
#include <sys/socket.h>
int ob = send(int osock, const void *obuf, size_t olen, int flags);

#include <unistd.h>
int ib = read(int isock, void *ibuf, size_t ilen);
```

`osock`/`isock` sono i file descriptor su cui inviare/ricevere, `obuf`/`ibuf` i puntatori ai buffer, `olen`/`ilen` le lunghezze in byte, `flags` il tipo di trasmissione (dipende dal protocollo, tipicamente 0), e `ob`/`ib` i byte effettivamente inviati/ricevuti. Poiché gli indirizzi di client e server sono già stati specificati in fase di connessione, non serve farlo qui come in `sendto`/`recvfrom`.

## Esempio TCP in C/C++

### Client

```cpp
int main() {
    int sockfd, status;
    char buffer[1024];
    const char *hello = "Hello from client";
    struct sockaddr_in servaddr;

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(8080);
    servaddr.sin_addr.s_addr = INADDR_ANY;

    int n;

    if ((status = connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr))) < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }

    send(sockfd, hello, strlen(hello), 0);
    std::cout << "Hello message sent." << std::endl;

    n = read(sockfd, buffer, 1024);
    std::cout << "Received \"" << buffer << "\"" << std::endl;

    close(sockfd);
    return 0;
}
```

### Server

```cpp
int main() {
    int sockfd, new_socket;
    char buffer[1024];
    const char *hello = "Hello from server";
    struct sockaddr_in servaddr, cliaddr;

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(8080);

    if (bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    if (listen(sockfd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    int addrlen = sizeof(cliaddr);
    if ((new_socket = accept(sockfd, (struct sockaddr *)&cliaddr,
                             (socklen_t *)&addrlen)) < 0) {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    int n = read(new_socket, buffer, 1024);
    std::cout << "Received \"" << buffer << "\"" << std::endl;

    send(new_socket, hello, strlen(hello), 0);
    std::cout << "Hello message sent." << std::endl;

    close(new_socket);
    close(sockfd);
    return 0;
}
```