# Lezione 03 — HTTP: The Hypertext Transfer Protocol

## Internet e il Web

**Internet** è una rete globale di computer interconnessi che condividono informazioni tramite i protocolli Internet; le sue origini risalgono ad **ARPANET** (1969). La **World Wide Web** (WWW, o semplicemente "il Web") non coincide con Internet: ne è un sottoinsieme. Fu inventata da Sir Tim Berners-Lee all'inizio degli anni '90 come sistema di **documenti ipertestuali** interconnessi tramite **hyperlink**, e i suoi componenti fondamentali sono **HTTP** e **HTML**.

### Ipertesti

I documenti tradizionali sono semplici sequenze di caratteri. Un **ipertesto**, invece, è un documento che contiene anche collegamenti ad altri contenuti, come altri ipertesti, documenti o media.

## Il protocollo HTTP

**HTTP** è un protocollo di livello applicativo costruito sopra **TCP/IP** ed è la fondamenta del WWW. Nasce per gli ipertesti ma oggi serve a trasferire **risorse** di ogni tipo: il **client** richiede di interagire con una risorsa e il **server** risponde. Ogni risorsa è identificata dal proprio **URL** (*Uniform Resource Locator*).

### URL: Uniform Resource Locator

Un URL come `https://www.informatica.it:4242/corsi/tecweb.html` si compone di quattro parti. Lo **schema** specifica il protocollo con cui accedere alla risorsa: i più comuni sono **http** e **https**, dove HTTPS è HTTP trasmesso su una connessione **criptata** mediante **Transport Layer Security (TLS)** — un ruolo importante anche nella mitigazione di certi attacchi alle applicazioni web. Il **nome di dominio** identifica il server che ospita la risorsa e viene risolto in un indirizzo IP tramite **DNS**. La **porta** può essere omessa quando il server usa quelle standard (80 per HTTP, 443 per HTTPS), mentre va indicata esplicitamente in caso di porta non standard. Infine, il **percorso** individua la posizione della risorsa sul server, tipicamente relativa a una directory **web root**: poiché il server serve solo i file interni a tale directory, non tutto il filesystem finisce esposto sul web. Gli URL possono contenere anche **parametri di query** e **ancore**, trattati nelle lezioni successive.

## Richieste e risposte

Lo scambio HTTP segue uno schema **request-response**. Il client invia una richiesta che specifica quale operazione eseguire, su quale risorsa, con quali condizioni o preferenze, e se vi è contenuto allegato; il server risponde indicando l'esito della richiesta, i metadati che lo descrivono ed eventuale contenuto. La risposta ha una struttura precisa: **riga di stato** (versione HTTP e status), **header** con i metadati, una riga vuota e infine il **corpo** opzionale.

### Verbi (metodi) HTTP

I metodi indicano lo scopo della richiesta rispetto alla risorsa:

| Metodo  | Descrizione                                                        |
| ------- | ------------------------------------------------------------------ |
| GET     | Recupera (una rappresentazione di) una risorsa.                    |
| POST    | Invia nuovi dati alla risorsa, con effetti collaterali sul server. |
| PUT     | Sostituisce integralmente la risorsa con il payload specificato.   |
| DELETE  | Elimina la risorsa specificata.                                    |
| HEAD    | Restituisce gli stessi metadati di GET ma senza il corpo.          |
| PATCH   | Applica una modifica parziale alla risorsa.                        |
| OPTIONS | Chiede informazioni sulle opzioni di comunicazione disponibili.    |
| QUERY   | Invia dati da elaborare senza effetti collaterali (RFC 100008).    |

#### Safety e idempotenza

Un metodo è **safe** se non modifica lo stato del server: porta cioè esclusivamente a operazioni di sola lettura, e il logging non conta come cambiamento di stato. **GET**, **HEAD** e **OPTIONS** sono safe. 

Un metodo è invece **idempotente** quando l'effetto sul server di una singola richiesta coincide con quello di più richieste identiche. Ne segue che tutti i metodi safe sono anche idempotenti e che **PUT** e **DELETE** lo sono a loro volta, mentre **POST** e **PATCH** non lo sono in generale.

| Metodo | Safe | Idempotente |
| --- | --- | --- |
| GET | Sì | Sì |
| HEAD | Sì | Sì |
| OPTIONS | Sì | Sì |
| PUT | No | Sì |
| DELETE | No | Sì |
| POST | No | Non garantito (di solito no). |
| PATCH | No | Non garantito (di solito no). |
| QUERY | Sì | Sì |

### Header HTTP

Gli header trasportano informazioni aggiuntive in richieste e risposte. Ogni header è composto da un **nome** (case-insensitive), due punti e un **valore**: `HEADER_NAME: value`. La **IANA** mantiene l'elenco degli header permanenti e provvisori, ed è possibile definire anche header personalizzati.

### Codici di stato

I codici di stato indicano se una richiesta è stata completata con successo e si raggruppano in cinque classi, ciascuna con una semantica precisa: i **1xx** segnalano che lo scambio sta continuando; i **2xx** che la richiesta è stata gestita con successo (es. **200 OK**); i **3xx** che il client deve compiere un passo ulteriore, tipicamente un redirect (es. **301 Moved**); i **4xx** che la richiesta non può essere gestita così com'è, perché contiene un errore (es. **400 Bad Request**, **403 Forbidden**, **404 Not Found**); i **5xx** che è il server o un intermediario, come il database, a essere fallito (es. **500**, **503 Unavailable**).

### L'header Host

Le richieste HTTP includono un header **Host** che potrebbe sembrare ridondante: quando la richiesta arriva a destinazione, il DNS ha già risolto il nome in un indirizzo IP. In realtà **più nomi di host possono risolvere allo stesso IP** — ad esempio `www`, `informatica`, `biblioteca` ed `erasmus.dieti.unina.it` puntano tutti a 143.225.97.81. Poiché un server HTTP può essere configurato per gestire più **virtual host**, ciascuno con la propria document root, è proprio l'header **Host** a permettergli di selezionare il virtual host corretto.

## Le caratteristiche del protocollo

### Statelessness

HTTP è un protocollo **stateless**: ogni richiesta è indipendente dalle precedenti e il server non conserva informazioni sulle richieste già ricevute da un client. Di conseguenza, per ottenere una comunicazione con stato occorrono meccanismi dedicati, come i **cookie**.

### I server HTTP

Un server HTTP è un **software** in esecuzione sulla macchina server che ascolta su una porta (80 per HTTP, 443 per HTTPS), riceve le richieste, ne interpreta metodo, destinazione ed header, e produce una risposta. Il termine "server" è ambiguo e può indicare il **ruolo** (il partecipante che risponde), il **software**, il **processo** in esecuzione o la **macchina** fisica. 
Per costruire la risposta, il server può **leggere un file** dal proprio filesystem (file statici) oppure **eseguire codice** che la genera al volo, eventualmente interrogando database e altri sistemi. Esempi noti di server statici sono **nginx** e **Apache httpd**.

#### Server statici e document root

I server statici mappano le risorse richieste a file nel filesystem, secondo una configurazione decisa dal server. Tipicamente si servono i file a partire da una directory specifica, la **document root**: se questa è `/var/www/`, la richiesta `GET /webtech/hello.txt` restituisce `/var/www/webtech/hello.txt`. La root e molte altre impostazioni si definiscono nei file di configurazione dedicati del server.

#### Esempio: nginx in Docker

```nginx
services:
  nginx:
    image: nginx:1.31.3
    ports:
      - "80:80"
    volumes:
      - ./website-book-of-programming:/usr/share/nginx/html/book-of-programming
      - ./website-web-technologies:/usr/share/nginx/html/web-technologies
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
```

Il file `nginx.conf` definisce due blocchi `server`, cioè due virtual host (`book-of-programming.local` e `web-technologies.local`), ciascuno con una document root diversa:

```nginx
events {}
http {
    server {
        listen 80;
        server_name book-of-programming.local;
        root /usr/share/nginx/html/book-of-programming;
    }
    server {
        listen 80;
        server_name web-technologies.local;
        root /usr/share/nginx/html/web-technologies;
    }
}
```

Poiché **.local** non è un TLD acquistabile, occorre un meccanismo per far risolvere i due nomi verso 127.0.0.1. I sistemi operativi moderni mettono a disposizione il file **hosts** (`C:\Windows\System32\drivers\etc\hosts` su Windows, `/etc/hosts` su Linux/MacOS): gli stub resolver DNS lo leggono prima di interrogare il resolver ricorsivo, quindi aggiungendo `127.0.0.1 book-of-programming.local` le richieste per quel nome risolvono a localhost.

## Strumenti per fare richieste HTTP

### Dev tools del browser

I dev tools del browser sono strumenti integrati, accessibili con **F12** o con *tasto destro → Ispeziona*, ed equivalenti tra i browser moderni. La scheda **Network** mostra le richieste HTTP effettuate: header e body di richiesta e risposta, metodo e percorso, codici di stato e un'analisi dettagliata dei tempi, dalla risoluzione DNS alla connessione, dall'invio della richiesta alla ricezione della risposta.

### REST Client in VS Code

L'estensione REST Client per VS Code permette di scrivere richieste HTTP in file di testo con estensione `.http` e di inviarle al volo dall'editor: un modo pratico per richieste rapide e molto utile per imparare HTTP.

### Client HTTP dedicati

Esistono anche client HTTP dedicati, come **Postman**, **Bruno** e **Insomnia**, che offrono una GUI per definire richieste e ispezionare risposte. Tipicamente includono funzioni avanzate per gestire collezioni di richieste e per il testing, e si rivelano utili quando si sviluppano API web.

## Riferimenti

- **Introduction to Web Applications Development** — Carles Mateu (Modulo 1), liberamente su archive.org.
- **Computer Networks: A Systems Approach** — Peterson & Davie, sez. 9.1.2.
- MDN web docs: *How the web works*, *What are hyperlinks?*, *What is a URL?*, *An overview of HTTP*, *Webpage, website, web server, and search engine*.

---

# Lezione 04 — HTTP: Rappresentazioni, efficienza, sicurezza

## Content negotiation

Un client può esprimere **preferenze** sulle rappresentazioni delle risorse tramite gli header di richiesta, e il server sceglie la rappresentazione più adatta. Ad esempio:

```http
GET /sections/wisdom.txt HTTP/1.1
Host: book-of-programming.local
Accept: text/plain
Accept-Language: en, it;q=0.9, fr;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Charset: utf-8, iso-8859-1;q=0.7, *;q=0.7
```

Una possibile risposta è:

```http
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Language: it
Content-Encoding: br
Content-Charset: utf-8

Contenuto in italiano.
```

### Pesi e fallback

Le preferenze possono avere pesi: in `Accept-Language: en, it;q=0.9, fr;q=0.8` l'inglese è la lingua preferita, l'italiano è accettabile con preferenza inferiore e il francè con preferenza ancora minore. Poiché il server non è tenuto a disporre di ogni rappresentazione richiesta, se nessuna è accettabile può rispondere con **406 Not Acceptable**; in pratica, però, i server scelgono spesso un fallback, ad esempio servendo la versione nella lingua predefinita quando quella richiesta non è disponibile.

### Content encoding

L'header **Accept-Encoding** indica le codifiche del contenuto — di norma algoritmi di compressione **senza perdita** — che il client è in grado di comprendere. Poiché riducono la quantità di dati trasmessi, hanno un impatto significativo, specie sui file di testo di grandi dimensioni. Le codifiche più diffuse sono **gzip** (codifica Lempel-Ziv LZ77), **br** (Brotli), **deflate** (struttura zlib con algoritmo deflate) e **identity** (nessuna modifica); ne esistono molte altre (dcb, dcz, …) elencate dalla IANA.

#### Effetto della compressione: esempio

Richiedendo la stessa risorsa con `Accept-Encoding: gzip` il server risponde con `Content-Encoding: gzip`, mentre con `identity` restituisce il file non compresso specificandone la lunghezza (`Content-Length: 1150`). Il contenuto visibile non cambia, poiché browser e client HTTP decomprimono il body in modo trasparente: quello mostrato nei dev tools è sempre il corpo decompresso. Concretamente, `wisdom.txt` passa da ~1150 caratteri con identity a 846 con gzip, con un **risparmio del 24%**; con file più grandi il guadagno cresce — `bootstrap.css` scende da 280.308 caratteri (280 KB) a 44.644 (44 KB), cioè una compressione dell'**84%**. Va però ricordato che comprimere e decomprimere introduce a sua volta un overhead.

## Caching

Se un minuto dopo una `GET` per `/sections/wisdom.txt` ricarichiamo la pagina, è molto improbabile che il contenuto sia cambiato: spesso conviene quindi **riusare le risposte precedenti**. Una **cache** memorizza una risposta proprio per poterla riutilizzare in richieste future.

### Benefici

- **Latenza ridotta**: la risposta può essere disponibile più vicina al client.
- **Meno traffico di rete**: la stessa rappresentazione non viene ritrasmessa.
- **Meno lavoro per il server**: un numero inferiore di richieste raggiunge l'origine.
- **Scalabilità**: le cache condivise possono servire molti client.
- **Resilienza**: le cache possono servire risposte memorizzate quando l'origine è temporaneamente non disponibile.

### Limiti e cacheabilità

Il caching non è banale, perché non tutte le risposte vanno memorizzate: si pensi a una pagina che mostra i posti liberi di un parcheggio, il cui valore cambia continuamente. Alcune risposte sono inoltre **private**: la risposta a `GET your-bank.com/my-account` contiene i dati del proprio conto, e nessuno vuole ricevere per errore la versione in cache di quello di un altro. I metodi **safe** (GET, HEAD) sono sempre cacheabili, mentre PUT e DELETE non lo sono; POST e PATCH sono teoricamente cacheabili se la risposta include header specifici, ma in pratica lo sono raramente.

### Livelli, cache private e condivise

Le risposte possono essere memorizzate in più punti lungo il percorso della richiesta, quindi una risposta può raggiungere il browser senza che il server di origine la elabori. Una cache **privata** serve un singolo utente, come la cache del browser; una cache **condivisa** può riusare la stessa risposta per più utenti, il che è appropriato per i contenuti pubblici ma non per i dati personali, che non devono mai finire per caso a un altro utente. Si noti che **se una risposta può essere memorizzata e chi può riusarla sono due decisioni distinte**.

### Consistenza

Il caching introduce un problema di **consistenza**: una risposta memorizzata rappresenta la risorsa in un istante passato. La cache deve quindi bilanciare due obiettivi in conflitto: riusare le risposte il più possibile per migliorare le prestazioni ed evitare al contempo di restituire risposte troppo vecchie o inappropriate.

### Le tre decisioni della cache

Per ogni risposta, la cache decide tre cose: se può **memorizzarla**, per quanto tempo può **riusarla senza validazione** e, quando il riuso diretto non è permesso, come sapere se la propria copia è ancora attuale mediante **validazione**. L'esito dipende dalla risposta specifica ed è controllato dai suoi **metadati**.

### L'header Cache-Control

L'header **Cache-Control** trasporta direttive che controllano il comportamento di caching. Le direttive sono separate da virgole; alcune ammettono un valore (`max-age=300`), altre no (`public`), e i tempi sono espressi in secondi. Esempio: `Cache-Control: public, max-age=300, must-revalidate`.

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

#### Esempi

Con `no-cache` la risposta può essere memorizzata, ma la cache deve validarla prima di ogni riuso; con `no-store` nessuna cache HTTP può memorizzarla. Con `private, no-cache` una cache privata può trattenerla ma deve validarla, mentre le cache condivise non devono memorizzarla; con `private, max-age=60` una cache privata può riusarla per 60 secondi senza contattare l'origine, sempre con divieto di memorizzazione per le cache condivise.

### Freschezza

Mentre una risposta è **fresca** può essere riusata direttamente senza validazione; non appena diventa **stale**, richiede in genere la validazione. La freschezza si calcola dai metadati della risposta — ad esempio `Date` più `max-age` — quindi una risposta può essere memorizzata in cache quando è già scaduta. In assenza di politiche esplicite le cache possono ricorrere a euristiche; per questo i server dovrebbero sempre fornire istruzioni di caching esplicite.

### Validatori

Un server può fornire **validatori** nelle proprie risposte:

```http
ETag: "article-v7"
Last-Modified: Thu, 13 Aug 2026 08:15:00 GMT
```

L'**ETag** è un identificatore opaco scelto dal server che cambia quando cambia la rappresentazione; **Last-Modified** indica quando il server ritiene che la rappresentazione sia stata modificata l'ultima volta e può essere meno preciso dell'ETag. I validatori permettono una validazione efficiente.

### Validazione con richieste condizionali

La validazione avvi tramite **richieste condizionali**: richieste HTTP normali cui si aggiungono header di validazione. Consideriamo una risposta ricevuta alle 10:05 con `Cache-Control: max-age=300`, `Last-Modified` ed `ETag` presenti: essendo memorizzabile in cache privata, resta fresca fino alle 10:10. Se alle **10:07** arriva una nuova richiesta, la copia in cache è ancora fresca e viene riusata senza contattare l'origine. Se invece la richiesta arriva alle **10:11**, la copia è stantia e va validata prima del riuso: poiché la risposta originale conteneva ETag e Last-Modified, si può effettuare una richiesta condizionale.

#### Validazione con ETag

La cache ripropone la richiesta aggiungendo `If-None-Match: "6a7b172b-47e"` (l'ETag memorizzato). Se la risorsa **non è cambiata**, il server risponde con **304 Not Modified** e body vuoto, a indicare che la copia in cache è ancora valida. Se invece la risorsa **è stata modificata**, il server risponde con **200 OK** e il nuovo contenuto, accompagnato da un ETag cambiato e da un `Last-Modified` aggiornato.

#### Validazione con Last-Modified

In alternativa si usa `If-Modified-Since: Tue, 11 Aug 2026 12:35:55 GMT`: gli esiti sono gli stessi — **304 Not Modified** se la risorsa non è cambiata, **200 OK** con contenuto aggiornato in caso contrario.

### Caching e content negotiation

La content negotiation può generare **varianti** della stessa risposta: se un server restituisce sia la versione compressa sia quella non compressa, la cache deve conservare due risposte distinte, e lo stesso vale per le altre caratteristiche negoziate, come `Accept-Language` e `Accept`. Le risposte si distinguono in base a metodo e URL — per una cache `GET /index.html`, `POST /index.html` e `GET /style.css` sono richieste diverse — ma due risposte con lo stesso URL non sono necessariamente uguali: a una richiesta con `Accept-Language: it` non si può servire una risposta in cache con `Content-Language: en`.

#### L'header Vary

Per questo motivo i server dovrebbero usare l'header **Vary** per indicare quali header di richiesta hanno influenzato la risposta:

```http
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Encoding: gzip
Vary: Accept-Encoding
Cache-Control: public, max-age=300
```

Le cache usano come chiave l'URL composto con il valore di Vary, quindi una risposta precedente è riusabile solo se la richiesta corrente condivide URL e metodo dell'originale **e** corrisponde al Vary della vecchia risposta.

## HTTPS

### Le minacce di HTTP in chiaro

Un attaccante in grado di osservare o alterare la comunicazione può **leggere** richieste e risposte, rubando credenziali o identificatori di sessione, e può **modificare** le risposte, reindirizzando l'utente o impersonando il server legittimo. **HTTPS** affronta queste minacce a livello di comunicazione.

### HTTPS e TLS

HTTPS ha la **stessa semantica** di HTTP ma usa tipicamente la porta 443 invece della 80: è in sostanza HTTP su un canale **criptato**, la cui sicurezza è garantita da **TLS/SSL**. Concettualmente il funzinamento è questo:

1. Il client richiede `https://squids.unina.it`.
2. Il server presenta un **certificato** contenente gli hostname validi e una chiave pubblica.
3. Il client verifica catena di fiducia, validità temporale e hostname del certificato.
4. Il server dimostra di controllare la corrispondente chiave privata.
5. Viene stabilito un canale cifrato e protetto da integrità.

Con TLS 1.3, dopo il *ServerHello* l'handshake e tutto lo scambio HTTP successivo sono cifrati: un intercettatore vede ancora indirizzi IP, direzioni, tempi e dimensioni dei pacchetti, ma non può leggere metodo, URL, header né corpi delle risposte.

### Proprietà e limiti

HTTPS garantisce tre proprietà fondamentali: **riservatezza** (chi ascolta il canale non può leggere le richieste), **integrità** (nessuno può alterare richieste e risposte) e **autenticazione del server** (il client verifica l'identità associata all'hostname). Non bisogna però fidarsi troppo del "lucchetto verde": HTTPS garantisce **solo** la cifratura della comunicazione. Non assicura che il sito non sia malevolo, che le informazioni pubblicate siano corrette, che il server non sia compromesso, né che i dati siano al sicuro prima della trasmissione o dopo il loro arrivo al server.

## HTTP/2 e HTTP/3

### Il problema delle richieste parallele

Una pagina web moderna può richiedere decine o **centinaia** di richieste per essere renderizzata. HTTP/1.1 può riusare una connessione TCP persistente, ma le risposte non possono essere liberamente interlacciate: devono arrivare nell'ordine delle richieste, quindi una risposta lenta ne ritarda tutte le successive. Per aggirare il problema i browser aprono più connessioni TCP verso lo stesso server, il che comporta però più connessioni da stabilire e mantenere, un overhead ripetuto di setup trasporto e TLS, competizione tra connessioni e un uso inefficiente della capacità di rete.

### HTTP/2: multiplexing

HTTP/2 risolve queste limitazioni rappresentando i messaggi come **frame binari** e assegnando ogni coppia richiesta-risposta a uno **stream**. Poiché i frame di stream diversi possono essere interlacciati su una singola connessione TCP, gli stream A=(A1,A2,A3), B=(B1,B2) e C=(C1,C2) possono essere serializzati come `A1 B1 B2 C1 A2 C2 A3`. La **semantica HTTP resta invariata** — le richieste restano concettualmente `GET /index.html`, `GET /logo.png`, `GET /style.css` — cambia solo la sintassi dei messaggi, binaria invece che testuale.

#### Head-of-Line blocking da TCP

HTTP/2 moltiplexa gli stream a livello HTTP, ma TCP non vede gli stream indipendenti e presenta un unico flusso di byte affidato e ordinato: se un segmento si perde, va recuperato prima di consegnare i successivi. Con tre stream A=(A1,A2), B=(B1,B2), C=(C1,C2):

| Segmento TCP | Byte HTTP/2 concettuali | Risultato |
| --- | --- | --- |
| S1 | A1 e parte di B1 | Ricevuto. |
| S2 | Resto di B1 e C1 | Perso. |
| S3 | B2 e A2 | Ricevuto, ma bufferizzato in attesa di S2. |

Il risultato è che HTTP/2 non può consegnare lo **stream A**, pur avendo ricevuto A1 e A2, dato che S2 (che non contiene dati di A) non è ancora disponibile. Questo collo di bottiglia è l'**Head-of-Line (HoL) Blocking**: un singolo elemento bloccato o ritardato ferma tutti quelli dietro, anche se indipendenti.

### HTTP/3: QUIC

HTTP/3 nasce per mantenere il multiplexing in stile HTTP/2 eliminando l'HoL blocking di TCP, e trasporta HTTP su **QUIC** anziché direttamente su TCP. QUIC gira su **UDP**, fornisce **stream indipendenti**, offre affidabilità e controllo della congestione e **integra l'handshake di TLS 1.3**. È supportato da tutti i principali browser e adottato dal 35–40% dei siti più visitati (riferimento: https://quicwg.org/).

## HTML

**HTML** (*Hypertext Markup Language*) è lo standard per rappresentare i documenti ipertestuali nel Web. Le pagine con cui interagiamo nei browser sono **documenti** definiti in HTML, che permette di strutturarle con titoli, paragrafi, immagini, liste, tabelle e altro.

## Riferimenti

- **Computer Networks: A Systems Approach** — Peterson & Davie, sez. 9.1.2.
- **High-Performance Browser Networking** — Ilya Grigorik (capitoli rilevanti: 4 TLS, 9 storia di HTTP, 11 HTTP/1.x, 12 HTTP/2).
- MDN web docs: *Content Negotiation*, *HTTP Caching*, *Evolution of HTTP*.
- **RFC 9111** — *HTTP Caching*, specifica completa per riferimento.