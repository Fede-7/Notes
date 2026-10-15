# Lezione 9 Application Layer programmazione di rete e DNS

## Richiamo delle procedure socket

Le socket gestiscono (in scatola nera) le funzionalità dei livelli trasporto (UDP/TCP) e rete (IP).

**UDP** — client e server aprono una socket; il server lega (`bind`) la socket a una porta specifica; poi si scambiano messaggi con `sendto`/`recvfrom`. IP e porta del client sono ricavati dalla `recvfrom`; si può ciclare su `sendto`/`recvfrom` per mantenere viva la comunicazione; a fine comunicazione entrambi chiudono la socket. Se chiude solo il client, il server può comunque accettare altri client.

**TCP** — client e server aprono una socket; il server fa `bind`, `listen` e infine `accept` delle nuove connessioni, il client si connette con `connect`; poi si scambiano messaggi con `send`/`read`. IP e porta del client sono ricavati dalla nuova socket creata. A fine comunicazione entrambi chiudono; il server esegue una `read` aggiuntiva prima di chiudere la socket client-specifica (rilascio della connessione), altrimenti occorre attendere ~4 minuti per riusare la porta; poi può tornare ad `accept` per un altro client.

## Traduzione DNS in C C++

Per creare socket tra due host serve conoscere **indirizzo (IP) e porta** del server; su Internet però gli host sono tipicamente identificati per **hostname**.

- Le Berkeley socket funzionano **solo con indirizzi IP**: le socket operano a livello trasporto, gli hostname a livello applicazione.
- Per connettersi via hostname serve la **traduzione DNS** per ottenere l'IP da passare alla socket.

C/C++ offre funzioni e strutture che eseguono la traduzione, contattando i server DNS e recuperando gli indirizzi:

- **`gethostbyname(name)`**: contatta i server DNS e restituisce un puntatore a una struttura **`hostent`** con le informazioni dell'host (`NULL` in caso di errore); non restituisce solo l'IP.
- **`gethostbyaddr`**: funzione analoga che restituisce una `hostent` per un dato indirizzo IP.

```c
struct hostent {
    char  *h_name;      // nome originale dell'host (canonico)
    char **h_aliases;   // lista di alias (terminata da NULL)
    int    h_addrtype;  // famiglia dell'indirizzo (tipicamente AF_INET)
    int    h_length;    // lunghezza dell'indirizzo (tipicamente 4 byte)
    char **h_addr_list; // lista di indirizzi (terminata da NULL)
};
#define h_addr h_addr_list[0] // per compatibilità
```

- Un DNS può fornire una **lista di indirizzi**, anche in ordine casuale se la query va a un server round-robin; si prende il primo elemento (`h_addr_list[0]` o `h_addr`).
- Gli indirizzi restituiti possono essere **castiati alla struttura `in_addr`** usata dalle socket, e stampati in notazione decimale con `inet_ntoa()`.

## Esempio HTTP con le socket

Una richiesta HTTP da programma specifica tre elementi: **hostname** del server, **numero di porta** e **risorsa** da recuperare (percorso dell'oggetto).

Sequenza del programma client (convenzione: 3 elementi definiti prima, poi socket → DNS → connessione → richiesta):

1. Creare la socket TCP (`socket(AF_INET, SOCK_STREAM, 0)`).
2. Tradurre l'hostname con `server = gethostbyname("www.unina.it")`, verificando che non restituisca `NULL`.
3. Azzerare la struttura `serv_addr`, impostare `sin_family` e `sin_port = htons(80)`, copiare l'IP con `bcopy(server->h_addr, &serv_addr.sin_addr.s_addr, server->h_length)`.
4. Connettersi con `connect()` alla struttura `serv_addr`.
5. Inviare la richiesta HTTP con `send()`, ricevere la risposta con `recv()`, chiudere la socket.

La richiesta è definita in una stringa; per controllare una sola pagina si crea una **connessione non persistente** (`Connection: close`):

```http
HEAD /chi-siamo/cenni-storici HTTP/1.1
Host: www.unina.it
Connection: close
```

- Il metodo **`HEAD`** chiede al server la risposta HTTP **senza il corpo** dell'oggetto.
- Con `recv()` si ricevono gli header della risposta: `Connection`, `Date`, `Server`, `Last-Modified`, `Content-Length`, `Content-Type`.
- Il buffer ricevuto va chiuso come stringa (`buffer[n] = '\0'`) prima di stamparlo, perché `recv` non aggiunge il terminatore.