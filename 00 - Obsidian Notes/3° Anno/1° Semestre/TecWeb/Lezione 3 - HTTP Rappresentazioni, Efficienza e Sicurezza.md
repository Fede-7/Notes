# Lezione 3 :HTTP Rappresentazioni, Efficienza e Sicurezza

## Content Negotiation

### Principi fondamentali

La **content negotiation** consente a un client di esprimere preferenze rispetto alle rappresentazioni di una risorsa. Il client comunica queste preferenze attraverso specifici header della richiesta, permettendo al server di scegliere una rappresentazione adatta tra quelle disponibili.

### Preferenze con pesi

Le preferenze possono essere assegnate con un livello di priorità tramite il parametro `q` (quality factor). 

>[!example] Example Request
> Ad esempio, l'header `Accept-Language: en, it;q=0.9, fr;q=0.8` indica che l'inglese è la lingua preferita, seguita dall'italiano con una preferenza leggermente inferiore, e infine dal francese. 

Il server non è obbligato a disporre di tutte le rappresentazioni richieste; se nessuna rappresentazione è accettabile per il client, il server può rispondere con uno status 406 Not Acceptable. In pratica, tuttavia, i server spesso scelgono un fallback predefinito, ad esempio servendo la versione in una lingua di default se quella richiesta non è disponibile.

### Header di negoziazione comuni

I principali header di negoziazione includono `Accept` (tipo di contenuto), `Accept-Language` (lingua), `Accept-Encoding` (compressione) e `Accept-Charset` (set di caratteri). Ogni header comunica al server quale forma della risorsa il client preferisce.

---

## Content Encoding

### Compressione lossless

L'header `Accept-Encoding` della richiesta indica gli algoritmi di compressione lossless che il client è in grado di decodificare. La compressione ha un impatto significativo sulla quantità di dati trasmessi, soprattutto per file di testo di grandi dimensioni. 
Gli algoritmi più utilizzati sono 
- **gzip** (basato su Lempel-Ziv coding – LZ77), 
- **br** (Brotli),
- **deflate** (che impiega la struttura zlib con l'algoritmo deflate). 

L'header `identity` indica l'assenza di compressione.

### Impatto della compressione

Il beneficio della compressione aumenta con la dimensione del file. 
> [!example]
> Ad esempio, il file bootstrap.css, non compresso, occupa circa 280 KB; compresso con gzip scende a 44 KB, realizzando un'efficienza del 84%. 

È importante notare che la compressione introduce un overhead di elaborazione, sia per la compressione che per la decompressione, quindi va valutata in relazione alla dimensione del file e al contesto di utilizzo.

---

## Caching

### Ruolo e benefici

La cache immagazzina una risposta affinché possa essere riutilizzata per richieste successive. Ciò apporta molteplici vantaggi: 
- **la latenza diminuisce** perché la risposta è disponibile più "vicino" al client, 
- **il traffico di rete si riduce** poiché la stessa rappresentazione non viene trasferita più volte, 
- **il carico sul server diminuisce** grazie a un minor numero di richieste che lo raggiungono, 
- **la scalabilità migliora** perché le cache condivise possono servire più client contemporaneamente, 
- **la resilienza aumenta** poiché le cache possono fornire risposte memorizzate quando il server di origine è temporaneamente inaccessibile.

### Problematiche critiche della cache

Non tutte le risposte devono essere memorizzate in cache. Consideriamo:
> Una pagina che mostra il numero di posti liberi in un parcheggio: memorizzarla in cache comporterebbe il rischio di servire dati obsoleti. 

> Ancora più delicato è il caso di risposte contenenti dati privati: una richiesta a `your-bank.com/my-account` restituisce i dettagli del tuo conto, e sarebbe una violazione grave se la cache servisse accidentalmente il conto di un altro utente. 

Per questo motivo, i metodi HTTP sicuri (GET e HEAD) sono sempre memorizzabili, mentre i metodi non sicuri come PUT e DELETE non lo sono. POST e PATCH, teoricamente, potrebbero essere memorizzati se la risposta include header specifici, ma in pratica ciò accade raramente.

### Livelli di cache e architettura

Le risposte possono essere memorizzate in più livelli: nella **cache del browser**, che serve un singolo utente; nella **cache condivisa** (come una CDN), che serve più utenti contemporaneamente; e infine raggiungono il **server di origine**, che è la fonte autorevole. È possibile che una risposta raggiunga il client senza che il server di origine la elabori, ricevendola interamente da una cache intermedia.

### Cache private e shared

Una **cache privata** serve un singolo utente, ad esempio la cache integrata in un browser web. Una **cache condivisa** può riutilizzare una risposta per più utenti, il che è appropriato per contenuti pubblici. Tuttavia, è cruciale che una risposta contenente dati di un utente non venga accidentalmente servita a un altro. La decisione di archiviare una risposta in cache e quella di permettere il riuso tra utenti sono due decisioni distinte, entrambe controllate tramite header specifici.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-25/75fa9453-fd1d-4836-b833-d5a3728180c2/e76d1cf453ca557c9679fe6b31e10e35d93e43faa467b8bbefe6f5b313b73c2c.jpg)

### Il dilemma della consistenza

La caching introduce un **problema di consistenza**: le risposte memorizzate rappresentano lo stato della risorsa in un momento precedente. La cache deve bilanciare due obiettivi conflittuali: riutilizzare le risposte il più possibile per migliorare le prestazioni, ed evitare di servire risposte inaccettabilmente vecchie o inadatte. Questa tensione è al cuore della progettazione delle strategie di caching.

### Tre decisioni fondamentali

Per ogni risposta, una cache deve prendere tre decisioni. La prima riguarda l'**archiviazione**: può conservare questa risposta? La seconda concerne il **riuso senza validazione**: per quanto tempo può riutilizzare questa risposta senza contattare l'origine? La terza riguarda la **validazione**: quando il riuso diretto non è consentito, come può verificare che la sua copia sia ancora corrente? L'esito di queste decisioni dipende dalla risposta specifica ed è controllato tramite metadati della risposta.

### Cache-Control: la guida definitiva

L'header `Cache-Control` contiene direttive che controllano il comportamento della cache per una determinata risposta. La sintassi generale è `Cache-Control: directive, directive=value, ...`, dove le direttive sono separate da virgole. Alcune direttive contengono valori (come `max-age=300`), altre no (come `public`). I valori temporali sono espressi in secondi.

#### Direttive principali

<table>
<tr><td>Direttiva </td><td>Significato </td></tr>
<tr><td>max-age=300</td><td>Response is fresh for 300 seconds</td></tr>
<tr><td>s-max-age=300</td><td>Freshness lifetime for shared caches</td></tr>
<tr><td>public</td><td>Response may be stored in public caches</td></tr>
<tr><td>private</td><td>Response is intended for a private cache online</td></tr>
<tr><td>no-cache</td><td>Response may be stored, byt must be validated before reuse</td></tr>
<tr><td>no-store</td><td>Response must not be stored in any cache</td></tr>
<tr><td>must-revalidate</td><td>Once stale, the response must be validated before reuse</td></tr>
<tr><td>immutable</td><td>Representation will not change during freshness lifetime</td></tr>
</table>

**max-age=300** specifica che la risposta è fresca per 300 secondi. 
**s-max-age=300** definisce la durata della freschezza specificamente per le cache condivise. 
**public** indica che la risposta può essere memorizzata in cache pubbliche. 
**private** stabilisce che la risposta è destinata a una sola cache privata online. 
**no-cache** consente l'archiviazione, ma richiede la validazione prima del riuso. 
**no-store** proibisce completamente l'archiviazione della risposta in qualsiasi cache. 
**must-revalidate** impone la validazione una volta che la risposta diviene stale. 
**immutable** assicura che la rappresentazione non cambierà durante il periodo di freschezza.

> [!example]
> #### Esempi di configurazione
> 
> `Cache-Control: no-cache` significa che la risposta può essere memorizzata, ma la cache deve validarla prima di riusarla. 
> `Cache-Control: no-store` vieta completamente l'archiviazione. 
> `Cache-Control: private, no-cache` permette a una cache privata di conservare la risposta ma richiede la validazione prima del riuso; le cache condivise non devono memorizzarla. 
> `Cache-Control: private, max-age=60` consente a una cache privata di riusare la risposta per 60 secondi senza contattare l'origine; le cache condivise non devono memorizzarla.

### Freschezza e validazione

```http
HTTP/1.1 200 OK
Date: Thu, 13 Aug 2026 08:00:00 GMT
Cache-Control: public, max-age=300 
```

La **freschezza** permette il riuso senza validazione. Una risposta è fresca per un periodo definito (ad esempio 5 minuti con `max-age=300`). Durante questo periodo la cache può servire la risposta direttamente. Una volta che la risposta diviene **stale** (oltre il periodo di freschezza), generalmente necessita di validazione prima del riuso. La freschezza è calcolata in base ai metadati della risposta, in particolare l'header `Date`. Questo significa che una risposta può essere memorizzata in uno stato già scaduto. Quando non è presente una politica di caching esplicita, le cache possono applicare euristiche per calcolare la freschezza, ma è responsabilità del server fornire istruzioni di caching esplicite.

### Validatori: ETag e Last-Modified

```http
ETag: "article-v7"  
Last-Modified: Thu, 13 Aug 2026 08:15:00 GMT 
```

Un server può fornire **validatori** nelle sue risposte per supportare una validazione efficiente. 
- L'**ETag** è un identificatore opaco scelto dal server che cambia quando la rappresentazione cambia. È il validatore più preciso e affidabile. 

- **Last-Modified** indica quando il server ritiene che la rappresentazione sia stata modificata per l'ultima volta; è meno preciso di ETag ma comunque utile.

#### Validazione tramite conditional requests

La validazione avviene tramite **conditional requests**, ovvero richieste normali che includono header di validazione aggiuntivi. Quando una risposta è diventata stale ma aveva un ETag o un Last-Modified, la cache può inviare una richiesta condizionale. Se la cache include l'header `If-None-Match: "article-v7"` e il server conferma che l'ETag è ancora valido, il server risponde con **304 Not Modified** (corpo vuoto), e la cache riusa il corpo memorizzato. Se la risposta è stata modificata, il server risponde con **200 OK** e il nuovo contenuto. Analogamente, `If-Modified-Since` consente di validare basandosi sulla data di modifica.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-25/75fa9453-fd1d-4836-b833-d5a3728180c2/1772f7a968fb50bc7983a7311be8f10bbc9f5c36845a3f39da5860336e614c2b.jpg)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-25/75fa9453-fd1d-4836-b833-d5a3728180c2/ac400579dbad5a90f4d4b25e086e6fc00f22713ede2d55fa0c17ef191f9f86d8.jpg)

### Caching e Content Negotiation

La **content negotiation** può creare varianti della stessa risposta. Un server può fornire dati compressi e non compressi per lo stesso URL. La cache potrebbe necessitare di archiviare risposte separate per ogni variante. Lo stesso accade per altre caratteristiche negoziate come `Accept-Language` e `Accept`. Quando il client invia una richiesta con `Accept-Language: it` non si può servire una risposta memorizzata con `Content-Language: en`.

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
	![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-25/75fa9453-fd1d-4836-b833-d5a3728180c2/a3d7b0f72b3e3536647f335d4b8b769ffc8ff00f3ec7463e77dabbc5598db84e.jpg)
- Server view:
	![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-25/75fa9453-fd1d-4836-b833-d5a3728180c2/f8a3cd3e9960882bd333d8717be6174772934e392beefce8884274a09917a658.jpg)

---

## HTTPS e Sicurezza della Comunicazione

### Limitazioni di HTTP

In HTTP puro, un attaccante in grado di osservare e alterare la comunicazione può leggere richieste e risposte, rubare credenziali o identificatori di sessione, modificare le risposte, reindirizzare l'utente, o impersonare il server inteso. HTTPS affronta direttamente queste **minacce a livello di comunicazione**.

### HTTPS: HTTP Secure

HTTPS ha la stessa semantica di HTTP ma utilizza tipicamente la porta 443 anziché la porta 80. In sostanza, è HTTP trasportato su un canale di comunicazione crittografato garantito da **Transport Layer Security (TLS)** o, nella terminologia più risalita nel tempo, **Secure Sockets Layer (SSL)**.

#### Funzionamento di TLS

Concettualmente, TLS funziona come segue: il client richiede `https://squids.unina.it`. Il server presenta un certificato contenente nomi host validi e una chiave pubblica. Il client verifica la catena di fiducia del certificato, la sua validità e l'allineamento con il nome host. Il server prova il controllo della chiave privata corrispondente. Un canale criptato e protetto dall'integrità è stabilito. Il certificato contiene informazioni identificative del soggetto (paese, organizzazione, nome comune), dell'emittente, della validità temporale (data di inizio e fine) e della chiave pubblica (algoritmo, dimensione della chiave, esponente e modulo nel caso di RSA).

### Proprietà garantite da HTTPS

HTTPS fornisce tre proprietà fondamentali. **Confidentiality**: gli outsider e gli eavesdropper sul canale di comunicazione non possono leggere le richieste HTTP. **Integrity**: gli outsider non possono alterare le richieste o le risposte HTTP. **Server authentication**: il client verifica l'identità associata al nome host. Durante la comunicazione, gli eavesdropper possono osservare indirizzi IP, direzioni del traffico, tempi e dimensioni dei pacchetti, ma non possono leggere il metodo HTTP, l'URL, gli header o i corpi delle risposte.

### Cosa HTTPS non garantisce

È cruciale non fare affidamento eccessivo sul "lucchetto verde" del browser. HTTPS assicura che la comunicazione sia criptata e nient'altro. HTTPS **non** garantisce che il sito web non sia malevolo, che le informazioni contenute siano corrette, che il server non sia stato compromesso, o che i dati siano al sicuro prima della trasmissione o dopo il raggiungimento del server.

---

## HTTP/2: Multiplexing e Efficienza

### Limitazioni di HTTP/1.1 con richieste parallele

Le moderne pagine web richiedono dozzine o centinaia di richieste per essere renderizzate in un browser. HTTP/1.1 può riusare una connessione TCP persistente, ma le risposte non possono essere liberamente interleaved: devono arrivare nell'ordine delle richieste. Ciò significa che una risposta lenta può ritardare tutte le risposte successive. I browser aperti tipicamente molteplici connessioni TCP verso lo stesso server per mitigare questo problema, il che comporta overhead di stabilimento e mantenimento di più connessioni, setup di trasporto e TLS ripetuti, competizione tra connessioni e un utilizzo inefficiente della capacità di rete.

### Multiplexing in HTTP/2

HTTP/2 mira a risolvere queste limitazioni. I messaggi sono rappresentati utilizzando **frame binari**. Ogni coppia richiesta-risposta è assegnata a uno **stream**. I frame provenienti da stream diversi possono essere interleaved, consentendo una serializzazione efficiente su un'unica connessione TCP. 

> [!example]
> Stream A: A1 A2 A3 
> Stream B: B1 B2 
> Stream C: C1 C2 
> 
> Possible serialization over a single TCP connection 
> A1 B1 B2 C1 A2 C2 A3 
> 
> I frame A1, B1, B2, C1, A2, C2, A3 provenienti da tre stream (A, B, C) possono essere transmessi in questa sequenza mischiata. 

La semantica di più richieste HTTP è preservata: le richieste concettualmente rimangono `GET /index.html`, `GET /logo.png`, `GET /style.css`. L'unica differenza è che non sono trasmesse utilizzando la sintassi testuale di HTTP/1.1.

### Head-of-Line Blocking e limitazione di TCP

HTTP/2 multiplessa gli stream a livello HTTP, ma TCP non può vedere questi stream indipendenti. TCP presenta un unico flusso di byte affidabile e ordinato; se un segmento TCP è perso, deve essere recuperato prima di consegnare i seguenti. Ciò crea una limitazione critica: 

> [!example]
> Supponiamo
> Tre streams: $A = ( A 1 , A 2 ) : B = ( B 1 , B 2 ) : C = ( C 1 , C 2 )$ 
> <table><tr><td>TCP Segment</td><td>Conceptual HTTP/2 bytes</td><td>Result</td></tr><tr><td>Segment 1 (S1)</td><td>A1 and part of B1</td><td>Received</td></tr><tr><td>Segment 2 (S2)</td><td>Rest of B1 and C1</td><td>Lost</td></tr><tr><td>Segment 3 (S3)</td><td>B2 and A2</td><td>Received but buffered (waiting for Segment 2)</td></tr></table>
> 
> HTTP/2 non può ricevere lo stream A sebbene A1 e A2 siano stati ricevuti, poiché S2 non contiene dati di A. 

Questo collo di bottiglia è detto **Head-of-Line (HoL) Blocking**: un singolo elemento ritardato o bloccato arresta gli elementi successivi dal progredire, anche se questi ultimi sono indipendenti.

---

## HTTP/3 e QUIC

### Introduzione di QUIC

HTTP/3 è stato introdotto per mantenere lo stile di multiplexing di HTTP/2, evitando tuttavia il collo di bottiglia del TCP Head-of-Line blocking. HTTP/3 trasporta HTTP su **QUIC** anziché direttamente su TCP.

#### Caratteristiche di QUIC

QUIC è costruito su **UDP**, fornisce **stream indipendenti multipli**, garantisce affidabilità e controllo della congestione, integra il handshake TLS 1.3 e è supportato da tutti i principali browser. È stato adottato dal 35-40% dei siti web principali.

---

## Conclusione: Verso HTML

HTML è il standard per rappresentare documenti ipertestuali sul Web. Le pagine che interagiamo nel browser sono documenti definiti utilizzando HTML, il quale consente di definire pagine web con intestazioni, paragrafi, immagini, elenchi, tabelle e molto altro. Gli approfondimenti su HTML verranno affrontati nella lezione successiva

---

## Riferimenti

### Testi principali

**Computer Networks: A Systems Approach** di Larry Peterson e Bruce Davie è un libro di testo open-source e liberamente disponibile. La sezione 9.1.2 (World Wide Web – HTTP) è rilevante per questa lezione. Disponibile su https://book.systemsapproach.org/applications/traditional.html#world-wide-web-http

**High-performance Browser Networking** di Ilya Grigorik (Google) è un libro di testo liberamente disponibile pubblicato da O'Reilly. I capitoli rilevanti per questa lezione sono il 4 (Transport Layer Security – TLS), il 9 (Brief history of HTTP), l'11 (HTTP/1.X) e il 12 (HTTP/2). Disponibile su https://hpbn.co/

### Approfondimenti tematici

**Content Negotiation** trattato nella documentazione MDN Web Docs. Consultare https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation

**HTTP Caching** nella documentazione MDN Web Docs. Consultare https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching

**Evolution of HTTP** nella documentazione MDN Web Docs. Consultare https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Evolution_of_HTTP

### Specifiche tecniche

**HTTP Caching (full specification)** è definita nel RFC 9111. Disponibile su https://httpwg.org/specs/rfc9111.html. Si tratta di un documento di riferimento; non è richiesto imparare l'intera specifica.
