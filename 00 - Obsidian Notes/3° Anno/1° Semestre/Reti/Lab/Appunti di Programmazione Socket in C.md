# Appunti di Programmazione Socket in C

## Come usare questi appunti

L'obiettivo è saper scrivere da solo ogni programma del repo `Laboratorio-di-Reti`, partendo da uno scheletro che impari a memoria e aggiungendo un concetto alla volta. Per ogni argomento trovi lo schema delle chiamate, il motivo di ogni chiamata, gli errori tipici e un esercizio da rifare senza guardare.

Metodo di studio: leggi la sezione, scrivi il programma a mano senza copiare, compila con `gcc -Wall -Wextra`, poi confronta con il file del repo.

| Cartella | Cosa fa | Porta | Concetto nuovo |
| --- | --- | --- | --- |
| `udp-server` 01-03 | richiesta/risposta, bind implicito, timeout | 8080 | `sendto`, `recvfrom`, `SO_RCVTIMEO` |
| `udp-server` 04-06 | tastiera, echo, più client | 8080 | ciclo infinito, indirizzo del mittente |
| `tcp-server` 01 | un messaggio e una risposta | 5000 | `listen`, `accept`, `connect` |
| `tcp-server` 02-03 | intero +1, somma di coppie | 5201 | `htonl`, `ntohl`, connessione persistente |
| `tcp-server` 04 | somma con trasferimenti completi | 5201 | `send_all`, `recv_all` |
| `tcp-server` 05 | server con un processo per client | 5202 | `fork` |
| `tcp-echo-two-exercises` | server a thread e a `select` | 9090 / 9091 | `pthread`, `select`, `shutdown` |
| `broadcast-multicast` | broadcast e chat multicast | 5001 / 5000 | `SO_BROADCAST`, `IP_ADD_MEMBERSHIP` |
| `dns-http` | DNS, HTTP, WHOIS | 80 / 43 | `getaddrinfo`, protocollo di testo |

## Fondamenti comuni a tutti i programmi

Ogni file del repo parte dagli stessi quattro elementi: gli header, il socket, l'indirizzo e il controllo degli errori. Impararli una volta ti dà il 60% di ogni programma.

**Header che servono quasi sempre**

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>      // close(), read(), write()
#include <arpa/inet.h>   // htons, htonl, inet_pton, inet_ntop
#include <sys/socket.h>  // socket, bind, connect, send, recv
```

**Il socket**

`socket(dominio, tipo, protocollo)` restituisce un descrittore (un intero) oppure -1.

- `AF_INET` = IPv4.
- `SOCK_DGRAM` = UDP, a datagrammi.
- `SOCK_STREAM` = TCP, flusso di byte.
- Il protocollo si lascia a `0`.

**L'indirizzo `struct sockaddr_in`**

Va sempre azzerato con `memset`, poi si riempiono tre campi:

```c
struct sockaddr_in addr;
memset(&addr, 0, sizeof(addr));
addr.sin_family = AF_INET;
addr.sin_port   = htons(8080);                 // porta
addr.sin_addr.s_addr = htonl(INADDR_ANY);      // server: tutte le interfacce
// client: inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);
```

Le funzioni di bind, connect e sendto vogliono un `struct sockaddr *`, quindi si fa il cast `(struct sockaddr *)&addr` e si passa `sizeof(addr)`.

**Byte order**

La rete usa il big endian, il tuo PC di solito no. Per questo ogni numero che passa in rete si converte:

| Funzione | Dimensione | Uso |
| --- | --- | --- |
| `htons` / `ntohs` | 16 bit | porte |
| `htonl` / `ntohl` | 32 bit | indirizzi e interi scambiati |

Regola: `h` verso la rete prima di inviare, `n` verso l'host dopo aver ricevuto.

**Controllo errori**

Ogni chiamata di sistema si controlla subito. Nel repo il modello è sempre lo stesso:

```c
if (sockfd < 0) {
    perror("socket");
    exit(EXIT_FAILURE);
}
```

**Ruoli**

- **Server**: ha una porta nota, quindi fa `bind()` e aspetta.
- **Client**: conosce l'indirizzo del server e scrive per primo. Non fa `bind()`, perché il sistema gli assegna una porta libera al primo invio (esercizio UDP 02).

## UDP: datagrammi senza connessione

UDP non stabilisce nessuna connessione: ogni `sendto()` è un messaggio indipendente che porta con sé l'indirizzo del destinatario. Non c'è garanzia di consegna, di ordine o di assenza di duplicati, e gli esempi del repo non implementano ritrasmissioni.

**Scheletro del server (esercizio 01)**

1. `socket(AF_INET, SOCK_DGRAM, 0)`
2. riempire `servaddr` con `INADDR_ANY` e porta 8080
3. `bind()` alla porta
4. `recvfrom()` con un secondo indirizzo `cliaddr`, che il sistema riempie con il mittente
5. `sendto()` verso `cliaddr`
6. `close()`

```c
len = sizeof(cliaddr);                       // va riassegnato a ogni recvfrom
n = recvfrom(sockfd, buffer, BUFFER_SIZE - 1, 0,
             (struct sockaddr *)&cliaddr, &len);
buffer[n] = '\0';                            // il buffer non è una stringa finché non lo chiudi
sendto(sockfd, reply, strlen(reply), 0,
       (struct sockaddr *)&cliaddr, len);
```

**Scheletro del client**

1. `socket()`
2. riempire `servaddr` con `inet_pton` verso `127.0.0.1` e porta 8080
3. `sendto()` verso `servaddr`
4. `recvfrom()` con `NULL, NULL` se non ti serve il mittente
5. `close()`

**Punti da ricordare**

- Si legge al massimo `BUFFER_SIZE - 1` byte per lasciare posto al terminatore `'\0'`, che aggiungi tu con `buffer[n] = '\0'`.
- `len` è un parametro di ingresso e di uscita: prima della chiamata contiene la dimensione dello spazio disponibile, dopo la dimensione dell'indirizzo scritto.
- Il server risponde sempre all'indirizzo letto da `recvfrom()`, mai a uno fisso: è ciò che permette di servire più client.

**Esercizio 02: bind implicito**

Il client non fa `bind()`, ma dopo il primo `sendto()` il sistema gli assegna una porta locale. La si legge con `getsockname()` e `ntohs()`. Un `bind()` fatto dopo fallisce con `Invalid argument`, perché il socket è già legato: l'errore è voluto e serve a mostrarlo.

**Esercizio 03: timeout**

Di default `recvfrom()` blocca per sempre. Con `setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout))` e una `struct timeval` da 5 secondi, scaduto il tempo la chiamata torna -1 con `errno` uguale a `EAGAIN` o `EWOULDBLOCK`. Quel caso va distinto dagli errori veri, come fa il repo:

```c
if (n < 0) {
    if (errno == EAGAIN || errno == EWOULDBLOCK)
        printf("Timeout! No reply received.\n");
    else
        perror("recvfrom");
}
```

Serve `#include <errno.h>` e `<sys/time.h>`.

**Esercizi 04, 05 e 06: dal singolo scambio al ciclo**

- **04**: il client legge una riga con `fgets()`, toglie il `\n` con `strcspn()` e la invia; il server stampa ogni messaggio e termina quando riceve `exit`. Non c'è risposta.
- **05**: il server rimanda ogni messaggio allo stesso mittente. Il client aspetta l'eco con `recvfrom(..., NULL, NULL)` e si ferma quando l'eco è `exit`; il server termina dopo averlo rimandato.
- **06**: il server è un `while (1)` che non termina mai: stampa mittente e porta con `inet_ntop()` e `ntohs()` e rispedisce il datagramma allo stesso mittente. Il client riceve il nome come argomento (`./client-echo-multi Alice`) e lo scrive nel testo (`Alice: ciao`): l'identità sta nel messaggio, mentre la risposta torna al giusto client perché il server rilegge l'indirizzo a ogni datagramma.

**Prova da rifare senza guardare**: scrivi un server UDP che risponde con il messaggio ricevuto in maiuscolo (`toupper`) e un client che lo usa, poi aggiungi il timeout da 5 secondi.

## TCP: connessione e flusso di byte

Con TCP prima si stabilisce una connessione, poi si scambiano byte affidabili e in ordine. Cambiano il tipo di socket (`SOCK_STREAM`) e soprattutto il server, che ha due socket diversi.

**I due socket del server**

| Socket | Creato da | Serve a |
| --- | --- | --- |
| `listenfd` (o `s`) | `socket()` + `bind()` + `listen()` | aspettare nuove connessioni, non trasporta dati |
| `connfd` (o `c`) | `accept()` | parlare con un singolo client |

Quando il client chiama `connect()`, il server la completa con `accept()`, che restituisce un **nuovo** descrittore. Il socket di ascolto resta libero per i client successivi.

&#91;embedded content: sequenza delle chiamate TCP · server e client\]

Il server prepara l'ascolto con `bind()` e `listen()` e si ferma in `accept()`. Il client entra con `connect()`; poi i due si scambiano `send()` e `recv()` sul socket di connessione.

**Scheletro del server (esercizio 01)**

1. `socket(AF_INET, SOCK_STREAM, 0)`
2. `setsockopt(..., SO_REUSEADDR, ...)` per riavviare subito il server senza aspettare
3. riempire `servaddr` (porta 5000, `INADDR_ANY`) e `bind()`
4. `listen(listenfd, 5)`: il secondo argomento è la coda di connessioni in attesa
5. `connfd = accept(listenfd, NULL, NULL)`
6. `read()` / `write()` su `connfd`
7. `close(connfd)` e `close(listenfd)`

**Scheletro del client**

1. `socket(AF_INET, SOCK_STREAM, 0)`
2. riempire `servaddr` con `inet_pton`
3. `connect()`: qui avviene la connessione
4. `write()` / `read()` su `sockfd`
5. `close()`

Il client non chiama né `bind()` né `listen()` né `accept()`.

**Differenze rispetto a UDP**

- Niente `sendto`/`recvfrom` con indirizzo: dopo `connect()` si usano `send`/`recv` oppure `read`/`write`, perché la connessione identifica già l'altro lato.
- `recv()` che restituisce `0` significa che l'altro lato ha chiuso: è la fine del flusso, non un errore.
- Un server che deve servire molti client in successione mette `accept()` dentro un `while (1)`.

**Esercizio 02: scambiare un intero**

Il client invia un `uint32_t` e il server risponde con `x + 1`. Il numero si converte sempre con `htonl` prima di inviare e `ntohl` dopo aver ricevuto, perché il formato in rete è fisso. Il server legge una sola volta con `recv(c, &net_x, sizeof(net_x), 0)` e controlla che siano arrivati proprio 4 byte, poi chiude la connessione e torna ad `accept()`.

```c
uint32_t net_x;
ssize_t r = recv(c, &net_x, sizeof(net_x), 0);
if (r == (ssize_t)sizeof(net_x)) {
    uint32_t next = ntohl(net_x) + 1;
    uint32_t net_next = htonl(next);
    send(c, &net_next, sizeof(net_next), 0);
}
close(c);
```

Il server installa anche un gestore di `SIGINT` che fa `shutdown()` del socket di ascolto: così `Ctrl+C` fa uscire `accept()` con errore e il programma chiude in modo pulito.

**Esercizio 03: somma su connessione persistente**

Il client manda **due** interi per volta, in un array `uint32_t net_nums[2]` da 8 byte, e il server risponde con 4 byte. A differenza dell'esercizio 02, la connessione resta aperta: il client ripete un ciclo con `scanf("%u %u", ...)` finché l'utente preme `Ctrl+D`, e il server legge in un ciclo interno finché il client non chiude.

**Prova da rifare senza guardare**: scrivi un server TCP che riceve un intero e restituisce il suo quadrato, accetta più connessioni una dopo l'altra e termina con `Ctrl+C`.

## Il problema dei trasferimenti parziali: send\_all e recv\_all

TCP non conserva i confini dei messaggi. Se invii 8 byte, una sola `recv()` può restituirne 3 e un'altra i restanti 5; due `send()` consecutive possono arrivare in un'unica `recv()`. Gli esercizi 02 e 03 usano una sola chiamata per semplicità e funzionano in locale, ma non sono corretti in generale. L'esercizio 04 li rende robusti.

**Regola**: se ti aspetti N byte, leggi in un ciclo finché non li hai tutti. Lo stesso vale per l'invio, dove `send()` può accettarne meno di quelli richiesti.

**`recv_all`: leggere esattamente n byte**

```c
ssize_t recv_all(int fd, void *buf, size_t n) {
    size_t received = 0;
    char *p = buf;
    while (received < n) {
        ssize_t r = recv(fd, p + received, n - received, 0);
        if (r < 0) {
            if (errno == EINTR) continue;   // interrotta da un segnale: riprova
            return -1;                      // errore vero
        }
        if (r == 0) return (ssize_t)received; // l'altro lato ha chiuso
        received += (size_t)r;
    }
    return (ssize_t)received;
}
```

**`send_all`: inviare esattamente n byte**

```c
ssize_t send_all(int fd, const void *buf, size_t n) {
    size_t sent = 0;
    const char *p = buf;
    while (sent < n) {
        ssize_t w = send(fd, p + sent, n - sent, 0);
        if (w < 0) {
            if (errno == EINTR) continue;
            return -1;
        }
        if (w == 0) return (ssize_t)sent;
        sent += (size_t)w;
    }
    return (ssize_t)sent;
}
```

**Come leggere i valori di ritorno nel server**

| `recv_all` restituisce | Significato | Azione |
| --- | --- | --- |
| `sizeof(msg)` | messaggio completo | elaborare |
| `0` | il client ha chiuso senza inviare nulla | uscire dal ciclo |
| tra `1` e `sizeof(msg) - 1` | il client ha chiuso a metà messaggio | scartare e uscire |
| `-1` | errore | `perror` e uscire |

**Dettagli da non dimenticare**

- `errno == EINTR` richiede `#include <errno.h>`. Un segnale come `SIGINT` può interrompere la chiamata senza che ci sia un vero errore.
- `signal(SIGPIPE, SIG_IGN)` evita che il programma muoia se scrivi su una connessione già chiusa dall'altro lato: `send()` restituisce invece -1.
- Il formato dei messaggi è a lunghezza fissa (due `uint32_t` = 8 byte in andata, uno = 4 byte in ritorno), quindi il ricevente sa quanti byte aspettarsi. Con messaggi a lunghezza variabile servirebbe un prefisso con la lunghezza o un terminatore.
- La somma usa `uint32_t`, quindi il risultato può andare in overflow senza avvisi.

**Prova da rifare senza guardare**: scrivi `recv_all` e `send_all` a memoria, poi riscrivi il client della somma usandole al posto di `send` e `recv`.

## Server concorrenti: fork, thread e select

Un server come `04-sum-safe` serve un client alla volta: finché la connessione resta aperta, nessun altro viene accettato. Per servirne molti insieme il repo mostra tre tecniche. Lo schema `socket`, `bind`, `listen`, `accept` resta identico: cambia solo cosa si fa dopo `accept()`.

| Tecnica | File | Come funziona | Costo e limite |
| --- | --- | --- | --- |
| `fork()` | `05-fork/server-fork.c` | un processo figlio per connessione | processi pesanti, memoria separata |
| `pthread` | `server_thread.c` | un thread per connessione, detached | memoria condivisa, attenzione ai dati passati |
| `select()` | `server_select.c` | un solo thread controlla tutti i socket | limite `FD_SETSIZE`, niente operazioni lunghe |

**1. Un processo per client: `fork()`**

Dopo `accept()` il server chiama `fork()`. Il valore restituito dice chi sei:

- `pid == 0`: sei il **figlio**. Chiudi `listenfd` (non ti serve), gestisci il client con `connfd`, poi `close(connfd)` e `_exit(0)`.
- `pid > 0`: sei il **padre**. Chiudi `connfd` (lo usa il figlio) e torni ad `accept()`.
- `pid < 0`: errore, chiudi `connfd` e continua.

Ogni processo chiude il descrittore che non usa: è una regola da ricordare, perché dopo `fork()` entrambi ereditano entrambi i socket. Il repo aggiunge `signal(SIGCHLD, SIG_IGN)`, che su Linux evita i processi zombie senza dover chiamare `wait()`.

L'esercizio `EXERCISE.txt` chiede di scrivere `client-fork.c`: collegarsi a `127.0.0.1:5202`, leggere due `unsigned` da tastiera, inviarli con `htonl` in 8 byte, ricevere 4 byte e convertirli con `ntohl`, usando `send_all` e `recv_all`. Con due client aperti il server stampa PIDs diversi.

**2. Un thread per client: `pthread`**

```c
struct worker_args *arg = malloc(sizeof(*arg));   // NON l'indirizzo di una variabile locale
arg->fd = connfd;
pthread_t tid;
pthread_create(&tid, NULL, handle_client, arg);
pthread_detach(tid);                              // le risorse tornano da sole alla fine
```

Punti chiave:

- Il thread riceve un puntatore. Se passassi l'indirizzo di `connfd`, il ciclo successivo lo sovrascriverebbe prima che il thread lo legga. Per questo si alloca sull'heap e il thread fa `free(arg)` appena copiato il contenuto.
- `pthread_create` restituisce un **numero d'errore**, non -1: si descrive con `strerror(err)`.
- Il thread termina con `close(fd)` e `return NULL`.
- Si compila con `-pthread`.

**3. Un solo thread con `select()`**

`select()` aspetta che almeno uno tra molti descrittori sia pronto, poi lo sai interrogare con `FD_ISSET()`. Il server tiene due insiemi:

- `allset`: tutti i descrittori che vuoi controllare (ascolto + client).
- `rset`: la copia che passi a `select()`, che la modifica. Per questo a ogni giro del ciclo si ricopia `rset = allset`.

Il ciclo ha sempre tre passi:

1. `select(maxfd + 1, &rset, NULL, NULL, NULL)`: attesa.
2. Se `FD_ISSET(listenfd, &rset)` c'è una connessione in coda: `accept()`, salva il nuovo socket in `client[]`, aggiungilo con `FD_SET(connfd, &allset)` e aggiorna `maxfd`.
3. Per ogni client pronto: `recv()`. Se restituisce `n > 0` fai echo con `send_all`. Se restituisce `0` o un errore: `close(fd)`, `FD_CLR(fd, &allset)`, `client[i] = -1`.

&#91;embedded content: ciclo del server con select · 4 passi che si ripetono\]

I passi 3 e 4 sono due controlli separati: nello stesso giro possono servire sia una nuova connessione sia dati da uno o più client.

L'array `client[]` con `-1` per gli slot liberi ricorda quali socket sono attivi. Ricorda anche che `FD_ISSET` controlla solo se un descrittore è nell'insieme, non lo toglie: la rimozione è `FD_CLR`.

**Come scegliere**

- `fork` e thread sono più semplici da pensare: il codice di un client sembra un programma sequenziale.
- `select` evita processi e thread, ma ogni operazione lunga bloccherebbe tutti i client insieme: per questo il ritardo opzionale dell'echo esiste solo nel server a thread.
- Il modello del server è indipendente da quello del client: `client_basic` funziona con tutti e tre.

**Prova da rifare senza guardare**: partendo da `04-sum-safe`, aggiungi `fork()` per gestire due client contemporanei, poi riscrivi lo stesso server con un thread per client.

## Client concorrenti: select e due thread

`client_basic.c` fa un ciclo rigido: legge una riga con `fgets()`, la invia, poi aspetta esattamente quella risposta con `recv_exact()`. Mentre aspetta l'echo non può leggere la tastiera, e mentre aspetta la tastiera non può leggere il socket. Gli esercizi A e B del repo chiedono di rendere indipendenti i due flussi, con due tecniche.

**Esercizio A: un thread con `select()`**

La struttura è la stessa del `multicast_chat`: si controllano insieme tastiera (`STDIN_FILENO`) e socket.

```c
int open_input = 1;
for (;;) {
    fd_set rfds;
    FD_ZERO(&rfds);                       // l'insieme va ricostruito a ogni giro
    if (open_input) FD_SET(STDIN_FILENO, &rfds);
    FD_SET(fd, &rfds);
    int nfds = (fd > STDIN_FILENO ? fd : STDIN_FILENO) + 1;

    if (select(nfds, &rfds, NULL, NULL, NULL) < 0) {
        if (errno == EINTR) continue;
        perror("select"); break;
    }
    if (FD_ISSET(STDIN_FILENO, &rfds)) {   // tastiera pronta
        ssize_t n = read(STDIN_FILENO, buf, sizeof(buf));
        if (n > 0)       send_all(fd, buf, (size_t)n);
        else if (n == 0) { shutdown(fd, SHUT_WR); open_input = 0; }  // Ctrl+D
    }
    if (FD_ISSET(fd, &rfds)) {             // socket pronto
        ssize_t n = recv(fd, buf, sizeof(buf), 0);
        if (n > 0)       fwrite(buf, 1, (size_t)n, stdout);
        else if (n == 0) break;            // il server ha chiuso: fine
        else if (errno != EINTR) { perror("recv"); break; }
    }
}
```

Regole da ricordare:

- I due controlli sono **due `if` indipendenti**, non un `else if`: entrambi i descrittori possono essere pronti insieme.
- Si usa `read()` sulla tastiera, non `fgets()`: `stdio` può leggere in anticipo in un buffer interno che `select()` non vede, e così si perderebbero righe.
- Dopo Ctrl+D non si esce subito: `shutdown(fd, SHUT_WR)` chiude solo l'invio (half-close), e si continua a ricevere finché `recv()` restituisce `0`. Così le risposte ancora in viaggio non vanno perse.
- Non chiamare più `recv_exact()` dopo `send()`: reintrodurrebbe il blocco del client base.

**Esercizio B: due thread sullo stesso socket**

- `main()` legge la tastiera e invia.
- Un secondo thread, creato con `pthread_create()`, esegue un ciclo di `recv()` e stampa.
- Al Ctrl+D: `shutdown(fd, SHUT_WR)`, poi `pthread_join()` sul thread ricevente, infine `close(fd)`.

```c
static void *receiver(void *arg) {
    int fd = *(int *)arg;                 // fd vive in main fino al join: indirizzo valido
    char buf[BUFSIZE];
    for (;;) {
        ssize_t n = recv(fd, buf, sizeof(buf), 0);
        if (n > 0)       fwrite(buf, 1, (size_t)n, stdout);
        else if (n == 0) break;
        else if (errno != EINTR) { perror("recv"); break; }
    }
    return NULL;
}
/* main: pthread_create(&t, NULL, receiver, &fd); ...ciclo read/send...
         shutdown(fd, SHUT_WR); pthread_join(t, NULL); close(fd); */
```

Ordine che conta: si fa il `join` **prima** del `close(fd)`, altrimenti il thread ricevente userebbe un descrittore già chiuso.

**Come vederne la differenza**

Avvia il server a thread con ritardo: `./bin/server_thread 9090 2000`. Scrivi più righe di seguito. Il client base le invia una alla volta aspettando 2 secondi ciascuna. I client con `select` o thread le inviano subito e mostrano gli echo man mano che arrivano.

**Prova da rifare senza guardare**: scrivi `client_select.c` partendo da `client_basic.c`, poi `client_thread.c`, e verifica entrambi contro `server_select` e `server_thread`.

## Broadcast e multicast

Sono ancora socket UDP: lo scheletro è quello della sezione UDP. Cambia l'indirizzo di destinazione e serve una `setsockopt()` che chieda al sistema un comportamento di livello rete. Qui IGMP e il routing multicast non vengono trattati: le opzioni dicono solo allo stack locale cosa fare.

|  | Broadcast | Multicast |
| --- | --- | --- |
| A chi arriva | a tutti gli host della sottorete | solo a chi si è iscritto al gruppo |
| Indirizzo di destinazione | `255.255.255.255` o l'indirizzo broadcast della subnet (es. `192.168.1.255`) | gruppo `224.0.0.0` - `239.255.255.255` (nel repo `239.255.0.1`) |
| Opzione chiave | `SO_BROADCAST` (`SOL_SOCKET`) | `IP_ADD_MEMBERSHIP` (`IPPROTO_IP`) |
| Attraversa i router | di norma no | no con `TTL = 1` |

**Broadcast: mittente (`broadcast_sender.c`)**

```c
int sock = socket(AF_INET, SOCK_DGRAM, 0);
int enabled = 1;
setsockopt(sock, SOL_SOCKET, SO_BROADCAST, &enabled, sizeof(enabled));

struct sockaddr_in destination = {0};
destination.sin_family = AF_INET;
destination.sin_port   = htons(5001);
inet_pton(AF_INET, "255.255.255.255", &destination.sin_addr);
sendto(sock, message, strlen(message), 0,
       (struct sockaddr *)&destination, sizeof(destination));
```

Senza `SO_BROADCAST` il `sendto()` verso un indirizzo di broadcast fallisce. Non serve `bind()`: il mittente non deve ricevere.

**Broadcast: ricevitore (`broadcast_receiver.c`)**

È un normale server UDP: `socket`, `bind` a `INADDR_ANY` sulla porta 5001, poi `recvfrom()` in ciclo e stampa del mittente. Ricorda che `192.168.1.255` è un indirizzo di broadcast solo se la maschera lo rende tale (per esempio una `/24`): va usato quello reale della tua rete.

**Multicast: la chat (`multicast_chat.c`)**

Ogni istanza è insieme mittente e ricevente, con **un solo socket** e nessun server centrale. Gli ingredienti, in ordine:

1. `socket(AF_INET, SOCK_DGRAM, 0)`.
2. `SO_REUSEADDR` (e `SO_REUSEPORT` se disponibile), per far convivere più istanze sulla stessa porta.
3. `bind()` a `INADDR_ANY` sulla porta 5000. Non è l'indirizzo del gruppo: serve a ricevere i datagrammi su quella porta.
4. Iscrizione al gruppo con `struct ip_mreq`:

```c
struct ip_mreq membership = {0};
inet_pton(AF_INET, "239.255.0.1", &membership.imr_multiaddr);   // il gruppo
membership.imr_interface.s_addr = htonl(INADDR_ANY);           // interfaccia scelta dal sistema
setsockopt(sock, IPPROTO_IP, IP_ADD_MEMBERSHIP,
           &membership, sizeof(membership));
```

5. `IP_MULTICAST_TTL = 1`: i pacchetti non escono dalla sottorete.
6. `IP_MULTICAST_LOOP = 1`: ricevi anche i tuoi stessi messaggi.
7. Destinazione dei messaggi = il gruppo e la porta.
8. Ciclo con `select()` su tastiera e socket, come nel client dell'esercizio A.

Le opzioni `TTL` e `LOOP` nel repo si passano come `unsigned char`, invece di `int`.

**Dettagli utili**

- Alla ricezione l'indirizzo restituito da `recvfrom()` è quello del **mittente**, non del gruppo.
- Con `/quit` o `Ctrl+D` si esce, e la `close()` rilascia anche l'iscrizione al gruppo.
- Il codice verifica che il gruppo sia davvero multicast con `IN_MULTICAST(ntohl(addr))`.
- In VM, WSL, VPN e reti campus broadcast e multicast possono non funzionare: prova prima su un solo host.

**Prova da rifare senza guardare**: scrivi un ricevitore broadcast che stampa mittente e testo, poi una chat multicast che usa un gruppo e una porta passati come argomenti.

## Livello applicativo: DNS, HTTP e WHOIS

Qui i protocolli sono semplici scambi di **testo** sopra un socket TCP. Il lavoro nuovo è risolvere il nome di un host e costruire a mano la richiesta nel formato giusto.

**DNS con `gethostbyname()` (`dns_lookup.c`)**

È l'API storica, solo IPv4, che restituisce un puntatore a `struct hostent` (non va liberato). I campi da conoscere:

| Campo | Contenuto |
| --- | --- |
| `h_name` | nome canonico |
| `h_aliases` | array di alias, terminato da `NULL` |
| `h_addrtype` | `AF_INET` per IPv4 |
| `h_length` | lunghezza dell'indirizzo in byte (4) |
| `h_addr_list` | array di indirizzi, terminato da `NULL` |

Si scorrono gli array con un ciclo fino a `NULL` e ogni indirizzo si stampa con `inet_ntop(AF_INET, h_addr_list[i], ip, sizeof(ip))`, con `ip` di tipo `char[INET_ADDRSTRLEN]`. Header necessari: `<netdb.h>` e `<arpa/inet.h>`. Se la risoluzione fallisce il puntatore è `NULL`.

**DNS moderno con `getaddrinfo()`**

È la funzione da preferire nel codice nuovo, perché gestisce IPv4 e IPv6 e fa anche la conversione della porta. `http_unina.c` e `whois_client.c` usano lo stesso helper `connect_tcp()`:

```c
struct addrinfo hints, *results, *p;
memset(&hints, 0, sizeof(hints));
hints.ai_family   = AF_UNSPEC;      // IPv4 o IPv6
hints.ai_socktype = SOCK_STREAM;    // TCP

int err = getaddrinfo(hostname, port, &hints, &results);
if (err != 0) { fprintf(stderr, "%s\n", gai_strerror(err)); return -1; }

for (p = results; p != NULL; p = p->ai_next) {   // prova ogni risultato
    sock = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
    if (sock < 0) continue;
    if (connect(sock, p->ai_addr, p->ai_addrlen) == 0) break;
    close(sock); sock = -1;
}
freeaddrinfo(results);                            // sempre, a lista finita
```

Nota: gli errori di `getaddrinfo` si descrivono con `gai_strerror()`, non con `perror()`. La porta si passa come stringa (`"80"`).

**HTTP a mano (`http_unina.c`)**

Dopo la connessione si invia una richiesta di testo con righe separate da `\r\n` e terminata da una riga vuota:

```c
snprintf(request, sizeof(request),
         "%s %s HTTP/1.1\r\n"
         "Host: %s\r\n"
         "Connection: close\r\n"
         "User-Agent: SocketCourseExample/1.0\r\n"
         "\r\n",                 // riga vuota = fine delle intestazioni
         method, path, hostname);
```

- `HEAD` chiede solo le intestazioni, `GET` anche il corpo.
- `Host:` è obbligatorio in HTTP/1.1; con porta diversa da 80 va indicata nell'intestazione.
- `Connection: close` fa chiudere la connessione al server a fine risposta, così il client sa quando fermarsi.
- La risposta si legge in un ciclo di `recv()` fino a `0` e si stampa con `fwrite(buffer, 1, bytes, stdout)`, che non richiede il terminatore `'\0'`.
- Il programma non segue i redirect e non supporta HTTPS: un `301` o `302` viene stampato così com'è.

**WHOIS (`whois_client.c`)**

È ancora più semplice: connessione TCP alla porta 43, invio del dominio seguito da `\r\n`, lettura della risposta fino alla chiusura.

```c
snprintf(query, sizeof(query), "%s\r\n", domain);
send_all(sock, query, length);
while ((n = recv(sock, buffer, sizeof(buffer), 0)) != 0) { /* fwrite... */ }
```

Il server predefinito è `whois.iana.org`, che dà soprattutto informazioni sui TLD. Per `.com` si usa `whois.verisign-grs.com`. Il codice rifiuta domini con `\r` o `\n` dentro, per evitare di iniettare righe in più nella richiesta.

**Cosa hanno in comune HTTP e WHOIS**

1. `getaddrinfo()` e `connect()`.
2. Costruzione della richiesta con `snprintf` e controllo che non sia stata troncata (`n >= sizeof(request)`).
3. `send_all()`.
4. Ciclo di `recv()` fino a `0`, gestendo `EINTR`.

**Prova da rifare senza guardare**: scrivi un client che, dato un host e un percorso, invia un `GET` e stampa solo la prima riga della risposta (lo status), leggendo fino al primo `\n`.

## Errori comuni, checklist ed esercizi di autonomia

**Gli errori che si ripetono più spesso**

| Sintomo | Causa probabile | Rimedio |
| --- | --- | --- |
| `bind: Address already in use` | server riavviato subito, oppure un altro server sulla stessa porta | `SO_REUSEADDR` prima di `bind()`, un solo server per porta |
| `connect: Connection refused` | il server non è avviato o la porta è sbagliata | avviare prima il server, controllare la porta |
| output con caratteri strani | buffer non terminato | `buffer[n] = '\0'` e leggere al massimo `size - 1` byte |
| numeri sbagliati tra client e server | manca la conversione di byte order | `htonl` prima di inviare, `ntohl` dopo la ricezione |
| messaggio troncato o letto a metà | una sola `recv()` su TCP | `recv_all()` con ciclo |
| il programma muore scrivendo | `SIGPIPE` su connessione chiusa | `signal(SIGPIPE, SIG_IGN)` |
| `recvfrom` blocca per sempre | datagramma perso o server spento | `SO_RCVTIMEO` e controllo di `EAGAIN` |
| server a thread legge un `fd` sbagliato | passato l'indirizzo di una variabile locale | `malloc` di una struttura per thread |
| `select()` ignora un client | `rset` non ricopiato da `allset` | `rset = allset` a ogni giro |
| `bind: Invalid argument` nel client UDP | `bind()` dopo il primo `sendto()` | non fare `bind()` nel client, oppure farlo prima |

**Checklist prima di compilare**

- [ ] Ho incluso gli header giusti (`errno.h` se uso `errno`, `netdb.h` per `getaddrinfo`, `pthread.h` per i thread)?
- [ ] Ho azzerato ogni `struct sockaddr_in` con `memset` o `= {0}`?
- [ ] Ho controllato il valore di ritorno di ogni chiamata e usato `perror`?
- [ ] Porte e interi passano per `htons`/`htonl` all'invio e `ntohs`/`ntohl` alla ricezione?
- [ ] Ho terminato i buffer con `'\0'` prima di stamparli come stringhe?
- [ ] Su TCP leggo e invio in un ciclo quando conosco la lunghezza?
- [ ] Ogni descrittore aperto viene chiuso, in ogni ramo (anche dopo `fork`)?
- [ ] Compilo con `gcc -Wall -Wextra` (e `-pthread` se uso thread)?

**Percorso di studio consigliato**

1. Basi, poi UDP 01, 03, 06.
2. TCP 01, 02, 03.
3. `send_all` e `recv_all`, poi TCP 04.
4. `fork`, poi il client dell'esercizio 05.
5. `server_thread`, poi `server_select`.
6. `client_select` e `client_thread`.
7. Broadcast, multicast, DNS, HTTP e WHOIS.

**Esercizi finali per verificare l'autonomia**

Ognuno va scritto da zero, senza aprire il repo, poi confrontato.

1. **Eco UDP in maiuscolo** con timeout da 3 secondi sul client.
2. **Calcolatrice TCP**: il client invia due interi e un carattere operatore (`+`, `-`, `*`), il server risponde con il risultato. Decidi tu il formato dei messaggi a lunghezza fissa.
3. **Server concorrente con `fork`** per la calcolatrice, provato con due client.
4. **Stesso server con `select`**, senza processi né thread.
5. **Chat TCP a due**: ogni lato legge da tastiera e dal socket insieme, con `select`.
6. **Rilevatore di host** con broadcast: un client invia un messaggio a tutta la rete, chi lo riceve risponde con il proprio nome.
7. **Client HTTP** che stampa solo la riga di stato e il valore di `Content-Type`.

Se ne riesci a scrivere quattro o cinque senza guardare, padroneggi gli schemi usati in tutto il repo.

## Soluzioni dei tre client lasciati da scrivere

Prova prima a scriverli da solo. Ognuno è stato compilato con `gcc -Wall -Wextra -Wpedantic` e provato contro i server del repo: `client-fork` con due client in parallelo su `server-fork` (somme corrette, due PID diversi), `client_select` su `server_select` e `client_thread` su `server_thread` con ritardo di 500 ms (echo corretto, uscita pulita dopo Ctrl+D). I file `.c` ti sono stati consegnati anche in chat.

**`client-fork.c` (esercizio 05)**

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <errno.h>
#include <signal.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 5202

static ssize_t recv_all(int fd, void *buf, size_t n)
{
    size_t got = 0;
    char *p = buf;
    while (got < n) {
        ssize_t r = recv(fd, p + got, n - got, 0);
        if (r < 0) { if (errno == EINTR) continue; return -1; }
        if (r == 0) return (ssize_t)got;
        got += (size_t)r;
    }
    return (ssize_t)got;
}

static ssize_t send_all(int fd, const void *buf, size_t n)
{
    size_t sent = 0;
    const char *p = buf;
    while (sent < n) {
        ssize_t w = send(fd, p + sent, n - sent, 0);
        if (w < 0) { if (errno == EINTR) continue; return -1; }
        if (w == 0) return (ssize_t)sent;
        sent += (size_t)w;
    }
    return (ssize_t)sent;
}

int main(void)
{
    signal(SIGPIPE, SIG_IGN);

    int s = socket(AF_INET, SOCK_STREAM, 0);
    if (s < 0) { perror("socket"); return EXIT_FAILURE; }

    struct sockaddr_in srv = {0};
    srv.sin_family = AF_INET;
    srv.sin_port = htons(PORT);
    inet_pton(AF_INET, "127.0.0.1", &srv.sin_addr);

    if (connect(s, (struct sockaddr *)&srv, sizeof(srv)) < 0) {
        perror("connect"); close(s); return EXIT_FAILURE;
    }
    printf("Connected to server.\n");

    for (;;) {
        unsigned int x, y;
        printf("Enter two numbers (Ctrl+D to exit): ");
        fflush(stdout);
        if (scanf("%u %u", &x, &y) != 2) break;

        uint32_t net_nums[2] = { htonl((uint32_t)x), htonl((uint32_t)y) };
        if (send_all(s, net_nums, sizeof(net_nums)) != (ssize_t)sizeof(net_nums)) {
            perror("send_all"); break;
        }

        uint32_t net_sum;
        ssize_t r = recv_all(s, &net_sum, sizeof(net_sum));
        if (r != (ssize_t)sizeof(net_sum)) {
            if (r < 0) perror("recv_all");
            else       fprintf(stderr, "Server closed the connection.\n");
            break;
        }
        printf("Server response: %u\n", (unsigned)ntohl(net_sum));
    }

    close(s);
    return EXIT_SUCCESS;
}
```

Compilazione: `gcc -Wall -Wextra client-fork.c -o client-fork`. Avvia `./server-fork` e due copie di `./client-fork` in tre terminali.

**`client_select.c` (esercizio A)**

La funzione `send_all` è la stessa del `client_basic`. Il resto del programma:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <signal.h>
#include <arpa/inet.h>
#include <sys/select.h>
#include <sys/socket.h>

#define BUFSIZE 1024

static int send_all(int fd, const char *buf, size_t len)
{
    size_t done = 0;
    while (done < len) {
        ssize_t n = send(fd, buf + done, len - done, 0);
        if (n < 0 && errno == EINTR) continue;
        if (n <= 0) return -1;
        done += (size_t)n;
    }
    return 0;
}

int main(int argc, char **argv)
{
    if (argc > 3) { fprintf(stderr, "Usage: %s [server_ip] [port]\n", argv[0]); return EXIT_FAILURE; }
    const char *ip = argc >= 2 ? argv[1] : "127.0.0.1";
    int port = argc == 3 ? atoi(argv[2]) : 9091;
    if (port < 1 || port > 65535) { fprintf(stderr, "Invalid port\n"); return EXIT_FAILURE; }
    signal(SIGPIPE, SIG_IGN);

    int fd = socket(AF_INET, SOCK_STREAM, 0);
    if (fd < 0) { perror("socket"); return EXIT_FAILURE; }

    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons((uint16_t)port);
    if (inet_pton(AF_INET, ip, &addr.sin_addr) != 1) {
        fprintf(stderr, "Invalid IPv4 address: %s\n", ip); close(fd); return EXIT_FAILURE;
    }
    if (connect(fd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        perror("connect"); close(fd); return EXIT_FAILURE;
    }

    int input_open = 1;          /* 0 dopo Ctrl+D */
    char buf[BUFSIZE];

    for (;;) {
        fd_set rfds;
        FD_ZERO(&rfds);          /* da ricostruire a ogni giro */
        if (input_open) FD_SET(STDIN_FILENO, &rfds);
        FD_SET(fd, &rfds);
        int nfds = (fd > STDIN_FILENO ? fd : STDIN_FILENO) + 1;

        if (select(nfds, &rfds, NULL, NULL, NULL) < 0) {
            if (errno == EINTR) continue;
            perror("select"); break;
        }

        if (input_open && FD_ISSET(STDIN_FILENO, &rfds)) {
            ssize_t n = read(STDIN_FILENO, buf, sizeof(buf));
            if (n > 0) {
                if (send_all(fd, buf, (size_t)n) < 0) { perror("send"); break; }
            } else if (n == 0) {
                shutdown(fd, SHUT_WR);   /* half-close */
                input_open = 0;
            } else if (errno != EINTR) {
                perror("read"); break;
            }
        }

        if (FD_ISSET(fd, &rfds)) {
            ssize_t n = recv(fd, buf, sizeof(buf), 0);
            if (n > 0) {
                fwrite(buf, 1, (size_t)n, stdout);
                fflush(stdout);
            } else if (n == 0) {
                break;                   /* il server ha chiuso */
            } else if (errno != EINTR) {
                perror("recv"); break;
            }
        }
    }

    close(fd);
    return EXIT_SUCCESS;
}
```

Compilazione: `gcc -Wall -Wextra client_select.c -o client_select`, poi `./client_select 127.0.0.1 9091`.

**`client_thread.c` (esercizio B)**

Il thread ricevente è l'unica parte nuova rispetto al client precedente; `send_all` è identica.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <pthread.h>
#include <signal.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define BUFSIZE 1024

/* send_all: identica a quella di client_select.c */

static void *receiver(void *arg)
{
    int fd = *(int *)arg;        /* valido: main fa il join prima di close */
    char buf[BUFSIZE];
    for (;;) {
        ssize_t n = recv(fd, buf, sizeof(buf), 0);
        if (n > 0) {
            fwrite(buf, 1, (size_t)n, stdout);
            fflush(stdout);
        } else if (n == 0) {
            break;
        } else if (errno != EINTR) {
            perror("recv"); break;
        }
    }
    return NULL;
}

int main(int argc, char **argv)
{
    /* argomenti, socket(), inet_pton(), connect(): come in client_select.c */

    pthread_t tid;
    int err = pthread_create(&tid, NULL, receiver, &fd);
    if (err != 0) {
        fprintf(stderr, "pthread_create: %s\n", strerror(err));
        close(fd); return EXIT_FAILURE;
    }

    char buf[BUFSIZE];
    for (;;) {
        ssize_t n = read(STDIN_FILENO, buf, sizeof(buf));
        if (n > 0) {
            if (send_all(fd, buf, (size_t)n) < 0) { perror("send"); break; }
        } else if (n == 0) {
            break;             /* Ctrl+D */
        } else if (errno != EINTR) {
            perror("read"); break;
        }
    }

    shutdown(fd, SHUT_WR);     /* il server vede EOF e chiude a sua volta */
    pthread_join(tid, NULL);   /* prima il join... */
    close(fd);                 /* ...poi la close */
    return EXIT_SUCCESS;
}
```

Compilazione: `gcc -Wall -Wextra -pthread client_thread.c -o client_thread`. Il file completo e provato è tra quelli che ti ho inviato.

Con `./server_thread 9090 2000` puoi vedere la differenza: il client base aspetta 2 secondi a ogni riga, questi due invia subito tutto e stampa gli echo man mano che arrivano.
