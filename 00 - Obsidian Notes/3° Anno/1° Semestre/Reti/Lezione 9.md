# Lezione 9: Programmazione di rete e DNS

## Ripasso: socket

I **socket** sono un elemento centrale della creazione di applicazioni di rete e gestiscono (in modo "black-box") le funzionalità dei livelli di trasporto (UDP/TCP) e di rete (IP). Esistono applicazioni (middleware) che **incapsulano i socket**, semplificandone la creazione e fornendo funzionalità più complesse; tuttavia **le API di base restano molto usate**.

### Comandi socket UDP

Per una connessione UDP client e server devono entrambi aprire un socket; il server deve fare il bind del socket su una porta specifica. Poi si scambiano messaggi con le funzioni `sendto` e `recvfrom`: IP e porta del client si ottengono tramite `recvfrom`, e si può ciclare su `sendto`/`recvfrom` per mantenere viva la comunicazione. A comunicazione finita, entrambi gli host chiudono il socket; se solo il client chiude il socket, il server può accettare altri client.

### Comandi socket TCP

Per una connessione TCP client e server devono entrambi aprire un socket. Il server deve fare il bind su una porta specifica, `listen` e infine `accept` le nuove connessioni; il client deve fare `connect`. Poi si scambiano messaggi con `send` e `read`: IP e porta del client si ricavano dal nuovo socket creato, e si può ciclare su `send`/`read` per mantenere viva la comunicazione. A comunicazione finita, entrambi gli host chiudono il socket. Il server dovrebbe fare una `read` aggiuntiva prima di chiudere il socket specifico del client (rilascio della connessione), altrimenti bisogna aspettare circa 4 minuti per riusare la porta; il server può anche tornare alla funzione `accept` e accogliere un altro client.

## Traduzione DNS in C/C++

Possiamo creare socket tra due host, ma **serve conoscere l'indirizzo (IP) e la porta del server**. Su Internet gli host sono tipicamente identificati per **hostname** anziché per IP, e i Berkeley socket (C/C++) funzionano solo con indirizzi IP: non sorprende, poiché **i socket lavorano al livello di trasporto** mentre **gli hostname al livello applicazione**. Per connettersi a un host via hostname serve quindi la **traduzione DNS** per ottenere l'IP da passare al socket.

C/C++ offre funzioni e strutture che fanno questa traduzione, usate per contattare i server DNS e recuperare gli indirizzi: in particolare si usa `gethostbyname()`. La funzione **non restituisce solo l'IP**, ma una struttura `hostent` con informazioni sull'host: il nome canonico, gli eventuali alias e uno o più indirizzi.

### La struttura hostent

```c
#include <netdb.h>

struct hostent {
    char  *h_name;        // nome originale dell'host (canonico)
    char **h_aliases;     // lista di alias (terminata da NULL)
    int    h_addrtype;    // famiglia dell'indirizzo (tipicamente AF_INET)
    int    h_length;      // lunghezza dell'indirizzo (tipicamente 4 byte)
    char **h_addr_list;   // lista di indirizzi (terminata da NULL)
};

// per ragioni di compatibilità
#define h_addr h_addr_list[0]
```

Un DNS può fornire una lista di indirizzi (che può essere in ordine casuale se la query va a server round-robin DNS): si può prendere il primo elemento dell'array (`h_addr_list[0]` o `h_addr`). Gli indirizzi restituiti si possono castare alla struttura `in_addr` usata dai socket.

### gethostbyname()

```c
#include <netdb.h>

struct hostent *host_info = gethostbyname(const char *name);
```

`name` è la stringa con l'hostname da tradurre, mentre `host_info` è un puntatore alla struttura `hostent` con le informazioni sull'host (NULL in caso di errore). Esiste anche `gethostbyaddr()`, che restituisce una struttura `hostent` per un dato indirizzo IP.

### Esempio completo

```cpp
#include <iostream>
#include <cstring>
#include <string>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <unistd.h>
#include <netdb.h>
#include <stdio.h>

int main(int argc, char **argv) {
    struct hostent *server_info;
    char *server_name;

    if (argc < 2) {
        std::cout << "No hostname specified" << std::endl;
        return 0;
    } else {
        server_name = argv[1];
    }

    // invoca il DNS e controlla la risposta
    server_info = gethostbyname(server_name);
    if (server_info == NULL) {
        std::cout << "Could not resolve hostname " << server_name << " :(" << std::endl;
        return 0;
    }

    // nome canonico
    std::cout << "Canonical name:" << std::endl;
    std::cout << "\t" << server_info->h_name << std::endl;

    // lista di alias
    std::cout << "Aliases:" << std::endl;
    int i = 0;
    while (server_info->h_aliases[i] != NULL) {
        std::cout << "\t" << server_info->h_aliases[i] << std::endl;
        i++;
    }

    // lista di IP
    std::cout << "IPs:" << std::endl;
    i = 0;
    while (server_info->h_addr_list[i] != NULL) {
        std::cout << "\t"
                  << inet_ntoa(*((struct in_addr *)server_info->h_addr_list[i]))
                  << std::endl;
        i++;
    }

    return 0;
}
```

## Esempio: richiesta HTTP via socket

Creiamo un codice C++ che implementa da zero una richiesta HTTP (HEAD) verso una pagina web: la pagina "cenni storici" del sito UNINA, `http://www.unina.it/chi-siamo/cenni-storici`. Per una richiesta HTTP si specificano tre elementi: l'hostname del server, il numero di porta e la risorsa da recuperare (percorso dell'oggetto).

### Creazione del socket TCP

```cpp
int main() {
    int socket_desc;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char buffer[4096];

    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_desc < 0) {
        std::cout << "failed to create socket" << std::endl;
        return 0;
    }
    ...
```

### Connessione al server web

```cpp
    server = gethostbyname("www.unina.it");
    if (server == NULL) {
        std::cout << "could not resolve hostname :(" << std::endl;
        close(socket_desc);
        return 0;
    }

    bzero((char *)&serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(80);
    bcopy((char *)server->h_addr,
          (char *)&serv_addr.sin_addr.s_addr, server->h_length);

    if (connect(socket_desc, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        std::cout << "connection failed :(" << std::endl;
        close(socket_desc);
        return 0;
    }
```

Qui `gethostbyname()` invoca il DNS e ricava l'IP del server dall'hostname (dentro la struttura `hostent`); l'IP della struttura restituita è copiato nella struttura `serv_addr` per la successiva `connect`.

### Richiesta e risposta

```cpp
    const char *request =
        "HEAD /chi-siamo/cenni-storici HTTP/1.1\r\n"
        "Host: www.unina.it\r\n"
        "Connection: close\r\n\r\n";

    if (send(socket_desc, request, strlen(request), 0) < 0) {
        std::cout << "failed to send request..." << std::endl;
        close(socket_desc);
        return 0;
    }
    std::cout << "message sent:" << std::endl;
    std::cout << request << std::endl;

    int n = recv(socket_desc, buffer, sizeof(buffer), 0);
    std::cout << "received " << n << " bytes:" << std::endl;
    std::cout << buffer;

    close(socket_desc);
    return 0;
}
```

La richiesta HTTP è definita nella stringa `request`. Creiamo una **connessione non persistente**, dato che vogliamo controllare una sola pagina; infine si chiude il socket e si stampa la risposta ricevuta.