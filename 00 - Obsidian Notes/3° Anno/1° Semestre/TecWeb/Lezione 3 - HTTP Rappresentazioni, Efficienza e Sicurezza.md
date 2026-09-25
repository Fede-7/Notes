# Lezione 3 : HTTP Rappresentazioni, Efficienza e Sicurezza

## Content Negotiation

### Principi fondamentali

La **content negotiation** consente a un client di esprimere preferenze rispetto alle rappresentazioni di una risorsa. Il client comunica queste preferenze attraverso specifici header della richiesta, permettendo al server di scegliere una rappresentazione adatta tra quelle disponibili.

### Pesi e fallback

Le preferenze possono essere assegnate con un livello di priorità tramite il parametro `q` (quality factor). 

> [!example]
> 
> ```http
> GET /sections/wisdom.txt HTTP/1.1
> Host: book-of-programming.local
> Accept: text/plain
> Accept-Language: en, it;q=0.9, fr;q=0.8
> Accept-Encoding: gzip, deflate, br
> Accept-Charset: utf-8, iso-8859-1;q=0.7, *;q=0.7
> ```
> 
> Una possibile risposta è:
> 
> ```http
> HTTP/1.1 200 OK
> Content-Type: text/plain
> Content-Language: it
> Content-Encoding: br
> Content-Charset: utf-8
> 
> Contenuto in italiano.
> ```
> 

Il server non è obbligato a disporre di tutte le rappresentazioni richieste; se nessuna rappresentazione è accettabile per il client, il server può rispondere con uno status **406 Not Acceptable**. In pratica, tuttavia, i server spesso scelgono un fallback predefinito, ad esempio servendo la versione in una lingua di default se quella richiesta non è disponibile.

### Header di negoziazione comuni

I principali header di negoziazione includono `Accept` (tipo di contenuto), `Accept-Language` (lingua), `Accept-Encoding` (compressione) e `Accept-Charset` (set di caratteri). Ogni header comunica al server quale forma della risorsa il client preferisce.

#### Content Encoding

L'header `Accept-Encoding` della richiesta indica gli algoritmi di compressione lossless che il client è in grado di decodificare. La compressione ha un impatto significativo sulla quantità di dati trasmessi, soprattutto per file di testo di grandi dimensioni.
L'header **identity** indica l'assenza di compressione, invece, gli algoritmi più utilizzati sono:
- **gzip** (basato su Lempel-Ziv coding – LZ77), 
- **br** (Brotli),
- **deflate** (che impiega la struttura zlib con l'algoritmo deflate). 

##### Impatto della compressione

Il beneficio della compressione aumenta con la dimensione del file, va però ricordato che comprimere e decomprimere introduce a sua volta un overhead.

> [!example]
> Ad esempio, il file bootstrap.css, non compresso, occupa circa 280 KB; compresso con gzip scende a 44 KB, realizzando un'efficienza del 84%. 

## Caching

La cache immagazzina una risposta affinché possa essere riutilizzata per richieste successive.

### Benefici

- **Latenza ridotta**: la risposta può essere disponibile più vicina al client.
- **Meno traffico di rete**: la stessa rappresentazione non viene ritrasmessa.
- **Meno lavoro per il server**: un numero inferiore di richieste raggiunge l'origine.
- **Scalabilità**: le cache condivise possono servire molti client.
- **Resilienza**: le cache possono servire risposte memorizzate quando l'origine è temporaneamente non disponibile.

### Problematiche critiche della cache

Il caching non è banale, perché non tutte le risposte vanno memorizzate I metodi **safe** (GET, HEAD) sono sempre cacheabili, mentre PUT e DELETE non lo sono; POST e PATCH sono teoricamente cacheabili se la risposta include header specifici, ma in pratica lo sono raramente.

> [!example]
> Si pensi a una pagina che mostra i posti liberi di un parcheggio, il cui valore cambia continuamente. 
> Alcune risposte sono inoltre **private**: la risposta a `GET your-bank.com/my-account` contiene i dati del proprio conto, e nessuno vuole ricevere per errore la versione in cache di quello di un altro. 

### Livelli, cache private e condivise

Le risposte possono essere memorizzate in più punti lungo il percorso della richiesta, quindi una risposta può raggiungere il browser senza che il server di origine la elabori. Una cache **privata** serve un singolo utente, come la cache del browser; una cache **condivisa** può riusare la stessa risposta per più utenti, il che è appropriato per i contenuti pubblici ma non per i dati personali, che non devono mai finire per caso a un altro utente. Si noti che **se una risposta può essere memorizzata e chi può riusarla sono due decisioni distinte**.

![[Lezione 3 - HTTP Rappresentazioni, Efficienza e Sicurezza-1790354943429.png|384]]

### Il dilemma della consistenza

La caching introduce un **problema di consistenza**: le risposte memorizzate rappresentano lo stato della risorsa in un momento precedente. La cache deve bilanciare due obiettivi conflittuali: riutilizzare le risposte il più possibile per migliorare le prestazioni, ed evitare di servire risposte inaccettabilmente vecchie o inadatte. Questa tensione è al cuore della progettazione delle strategie di caching.

### Tre decisioni fondamentali

Per ogni risposta, la cache decide tre cose: se può **memorizzarla**, per quanto tempo può **riusarla senza validazione** e, quando il riuso diretto non è permesso, come sapere se la propria copia è ancora attuale mediante **validazione**. L'esito dipende dalla risposta specifica ed è controllato dai suoi **metadati**.

### L'header Cache-Control

L'header **Cache-Control** trasporta direttive che controllano il comportamento di caching. Le direttive sono separate da virgole; alcune ammettono un valore, altre no, e i tempi sono espressi in secondi. 

> Esempio: `Cache-Control: public, max-age=300, must-revalidate`.

| Direttiva | Significato |
| --- | --- |
| max-age=300 | La risposta è fresca per 300 secondi. |
| s-max-age=300 | Durata di freschezza per le cache condivise. |
| public | La risposta può essere memorizzata in cache pubbliche. |
| private | La risposta è destinata a una cache privata. |
| no-cache | La risposta può essere memorizzata, ma va validata prima di ogni riuso. |
| no-store | La risposta non va memorizzata in nessuna cache. |
| must-revalidate | Scaduta la freschezza, la risposta va validata prima del riuso. |
| immutable | La rappresentazione non cambierà durante la durata di freschezza. |

### Freschezza

```http
HTTP/1.1 200 OK
Date: Thu, 13 Aug 2026 08:00:00 GMT
Cache-Control: public, max-age=300 
```

Mentre una risposta è **fresca** può essere riusata direttamente senza validazione; non appena diventa **stale**, richiede in genere la validazione. La freschezza si calcola dai metadati della risposta — ad esempio `Date` più `max-age` — quindi una risposta può essere memorizzata in cache quando è già scaduta. In assenza di politiche esplicite le cache possono ricorrere a euristiche; per questo i server dovrebbero sempre fornire istruzioni di caching esplicite.

### Validatori: ETag e Last-Modified

Un server può fornire **validatori** nelle sue risposte per supportare una validazione efficiente. 
- L'**ETag** (Entity Tag) è un identificatore opaco scelto dal server che cambia quando la rappresentazione cambia. È il validatore più preciso e affidabile. 
- **Last-Modified** indica quando il server ritiene che la rappresentazione sia stata modificata per l'ultima volta; è meno preciso di ETag ma comunque utile.

```http
ETag: "article-v7"  
Last-Modified: Thu, 13 Aug 2026 08:15:00 GMT 
```

> [!info] Identificatore opaco
> Il client non ha bisogno di conoscerne il significato interno né come è stata generata

#### Validazione tramite conditional requests

La validazione avviene tramite **conditional requests**, ovvero richieste normali che includono header di validazione aggiuntivi. 
Quando una risposta è diventata *stale*, ma aveva un ETag o un Last-Modified, la cache può inviare una richiesta condizionale. Se la cache include l'header `If-None-Match: "article-v7"` e il server conferma che l'ETag è ancora valido, il server risponde con **304 Not Modified** (corpo vuoto), e la cache riusa il corpo memorizzato. Se la risposta è stata modificata, il server risponde con **200 OK** e il nuovo contenuto. 

![[Lezione 3 - HTTP Rappresentazioni, Efficienza e Sicurezza-1790356127058.png|448]]

Analogamente, `If-Modified-Since` consente di validare basandosi sulla data di modifica.

![[Lezione 3 - HTTP Rappresentazioni, Efficienza e Sicurezza-1790356148861.png|446]]

### Caching e Content Negotiation

La **content negotiation** può creare varianti della stessa risposta. Un server può fornire dati compressi e non compressi per lo stesso URL. La cache potrebbe necessitare di archiviare risposte separate per ogni variante. Lo stesso accade per altre caratteristiche negoziate come `Accept-Language` e `Accept`. 
Quando il client invia una richiesta con `Accept-Language: it` non si può servire una risposta memorizzata con `Content-Language: en`.

#### L'header Vary

Per risolvere questo problema, i server devono utilizzare l'header `Vary` per indicare quali header di richiesta influenzano la risposta. 

> [!example]
> ```http
> HTTP/1.1 200 OK
> Content-Type: text/plain
> Content-Encoding: gzip
> Vary: Accept-Encoding
> Cache-Control: public, max-age=300 
> ```
> 
> `Vary: Accept-Encoding` comunica che la risposta varia in base all'encoding richiesto. Le cache sono indicizzate sulla combinazione di URL + valore Vary. 

Ciò significa che una risposta precedente può essere riutilizzata per una richiesta successiva solo se la richiesta originale e quella attuale condividono lo stesso URL e metodo, e la richiesta attuale corrisponde all'header Vary della risposta vecchia.

#### Flusso decisionale della cache

Una cache, all'arrivo di una richiesta, deve innanzitutto verificare se una risposta corrispondente è già memorizzata. Se non esiste (cache miss), invia la richiesta al server di origine e, se appropriato, memorizza la risposta. Se esiste una risposta corrispondente (cache hit), verifica se è ancora fresca e riutilizzabile; in caso affermativo, la serve direttamente. Se la risposta è stale ma un validatore è disponibile, esegue una richiesta condizionale. Se il server risponde con 304, la cache riusa il corpo memorizzato. Se il server risponde con 200, archivia e serve la nuova risposta.
- Cache view:
	![[Lezione 3 - HTTP Rappresentazioni, Efficienza e Sicurezza-1790356390904.png|527]]
- Server view:
	![[Lezione 3 - HTTP Rappresentazioni, Efficienza e Sicurezza-1790356408018.png]]

## HTTPS e Sicurezza della Comunicazione

Con HTTP un attaccante in grado di osservare o alterare la comunicazione può **leggere** richieste e risposte, rubando credenziali o identificatori di sessione, e può **modificare** le risposte, reindirizzando l'utente o impersonando il server legittimo. 
**HTTPS** affronta queste minacce a livello di comunicazione.

### HTTPS e TLS

HTTPS ha la **stessa semantica** di HTTP ma usa tipicamente la porta 443 invece della 80: è in sostanza HTTP su un canale **criptato**, la cui sicurezza è garantita da **TLS/SSL**. Concettualmente il funzinamento è questo:

1. Il client richiede `https://squids.unina.it`.
2. Il server presenta un **certificato** contenente gli hostname validi e una chiave pubblica.
3. Il client verifica catena di fiducia, validità temporale e hostname del certificato.
4. Il server dimostra di controllare la corrispondente chiave privata.
5. Viene stabilito un canale cifrato e protetto da integrità.

Con TLS 1.3, dopo il *ServerHello* l'handshake e tutto lo scambio HTTP successivo sono cifrati: un intercettatore vede ancora indirizzi IP, direzioni, tempi e dimensioni dei pacchetti, ma non può leggere metodo, URL, header né corpi delle risposte.

### Proprietà e limiti

HTTPS garantisce tre proprietà fondamentali: 
- **riservatezza** (chi ascolta il canale non può leggere le richieste), 
- **integrità** (nessuno può alterare richieste e risposte) ,
- **autenticazione del server** (il client verifica l'identità associata all'hostname). 

Non bisogna però fidarsi troppo del "lucchetto verde": HTTPS garantisce **solo** la cifratura della comunicazione. Non assicura che il sito non sia malevolo, che le informazioni pubblicate siano corrette, che il server non sia compromesso, né che i dati siano al sicuro prima della trasmissione o dopo il loro arrivo al server.

## HTTP/2: Multiplexing e Efficienza

### Limitazioni di HTTP/1.1 con richieste parallele

Le moderne pagine web richiedono dozzine o centinaia di richieste per essere renderizzate in un browser. HTTP/1.1 può riusare una connessione TCP persistente, ma le risposte non possono essere liberamente interleaved: devono arrivare nell'ordine delle richieste. Ciò significa che una risposta lenta può ritardare tutte le risposte successive. I browser aperti tipicamente molteplici connessioni TCP verso lo stesso server per mitigare questo problema, il che comporta overhead di stabilimento e mantenimento di più connessioni, setup di trasporto e TLS ripetuti, competizione tra connessioni e un utilizzo inefficiente della capacità di rete.

### Multiplexing in HTTP/2

HTTP/2 mira a risolvere queste limitazioni. I messaggi sono rappresentati utilizzando **frame binari**. Ogni coppia richiesta-risposta è assegnata a uno **stream**. I frame provenienti da stream diversi possono essere interleaved, consentendo una serializzazione efficiente su un'unica connessione TCP.
La semantica di più richieste HTTP è preservata: le richieste concettualmente rimangono `GET /index.html`, `GET /logo.png`, `GET /style.css`. L'unica differenza è che non sono trasmesse utilizzando la sintassi testuale di HTTP/1.1.

> [!example]
> Stream A: A1 A2 A3 
> Stream B: B1 B2 
> Stream C: C1 C2 
> 
> Possible serialization over a single TCP connection 
> A1 B1 B2 C1 A2 C2 A3 
> 
> I frame A1, B1, B2, C1, A2, C2, A3 provenienti da tre stream (A, B, C) possono essere transmessi in questa sequenza mischiata. 

#### Head-of-Line Blocking e limitazione di TCP

HTTP/2 multiplessa gli stream a livello HTTP, ma TCP non può vedere questi stream indipendenti. TCP presenta un unico flusso di byte affidabile e ordinato; se un segmento TCP è perso, deve essere recuperato prima di consegnare i seguenti. 

Questo collo di bottiglia è detto **Head-of-Line (HoL) Blocking**: un singolo elemento ritardato o bloccato arresta gli elementi successivi dal progredire, anche se questi ultimi sono indipendenti.

> [!example]
> Supponiamo tre streams: $A = ( A 1 , A 2 ) : B = ( B 1 , B 2 ) : C = ( C 1 , C 2 )$ 
> <table><tr><td>TCP Segment</td><td>Conceptual HTTP/2 bytes</td><td>Result</td></tr><tr><td>Segment 1 (S1)</td><td>A1 and part of B1</td><td>Received</td></tr><tr><td>Segment 2 (S2)</td><td>Rest of B1 and C1</td><td>Lost</td></tr><tr><td>Segment 3 (S3)</td><td>B2 and A2</td><td>Received but buffered (waiting for Segment 2)</td></tr></table>
> 
> HTTP/2 non può ricevere lo stream A sebbene A1 e A2 siano stati ricevuti, poiché S2 non contiene dati di A. 

## HTTP/3 e QUIC

HTTP/3 è stato introdotto per mantenere lo stile di multiplexing di HTTP/2, evitando tuttavia il collo di bottiglia del TCP Head-of-Line blocking. HTTP/3 trasporta HTTP su **QUIC** anziché direttamente su TCP.

### Caratteristiche di QUIC

QUIC è costruito su **UDP**, fornisce **stream indipendenti multipli**, garantisce affidabilità e controllo della congestione, integra il handshake TLS 1.3 e è supportato da tutti i principali browser. È stato adottato dal 35-40% dei siti web principali.
