# Lezione 5: Formato dei messaggi HTTP, cookie, caching

## Ripasso di HTTP

L'**HyperText Transfer Protocol (HTTP)** è uno dei protocolli più usati su Internet (applicazioni web-based). È un protocollo **client-server** che definisce la **struttura dei messaggi** (formato) e come **client e server li scambiano**; come implementare le applicazioni client/server non è invece deciso da HTTP. Usa messaggi di tipo **richiesta/risposta**, è **stateless** (client e server non ricordano le interazioni passate) e presuppone un trasporto **affidabile** e orientato alla connessione (per lo più TCP, di recente anche UDP), potendo usare connessioni **persistenti** e **non persistenti**.

## Formato dei messaggi HTTP

In HTTP esistono due formati diversi per richiesta e risposta: la **richiesta** specifica il comando (metodo) che il server deve eseguire (es. dammi una pagina web, compila un form), mentre la **risposta** riporta l'esito del comando (successo, fallimento, ecc.) ed eventuali dati (es. il file richiesto). Entrambi i messaggi sono scritti in semplice testo ASCII, quindi leggibili anche dall'uomo.

### Formato del messaggio di richiesta

Il messaggio di richiesta include i seguenti campi:

- Il **metodo**: il comando richiesto che il server deve eseguire.
- L'**URL**: identifica l'oggetto su cui operare.
- La **versione**: la versione di HTTP (es. HTTP/1.1).
- Le **righe di intestazione (header)**: contengono i parametri della richiesta; il loro numero e tipo non sono fissi, e ogni riga include **nome** e **valore** del parametro. Ad esempio si può specificare se si vuole una connessione persistente o non persistente, e si possono usare anche header personalizzati.
- Il **body**: specifico del metodo, contiene dati potenzialmente associati al comando (es. testo di un form).

I campi sono separati da caratteri speciali: `sp` (spazio), `cr` (*carriage return*, `\r`), `lf` (*line feed*, `\n`).

### Metodi

- **GET**: recupera oggetti (risorse) dal server. È tra i comandi più usati, poiché ogni volta che navighiamo su una nuova pagina il file associato deve essere recuperato; nel metodo GET il **body è vuoto**.
- **POST**: imposta informazioni dentro oggetti (risorse) del server, e il body contiene le informazioni da inviare. Una richiesta generata da un form non necessariamente usa POST: i form HTML usano spesso GET includendo i dati nell'URL richiesto.
- **HEAD**: simile a GET, ma il server risponde con un messaggio HTTP **senza l'oggetto**; spesso usato dagli sviluppatori per il debugging.
- **PUT**: spesso usato con strumenti di pubblicazione Web; permette di caricare un oggetto in un percorso specifico di un server Web, ed è usato anche dalle applicazioni che devono caricare oggetti su server Web.
- **DELETE**: permette a un utente o a un'applicazione di eliminare un oggetto su un server Web.

### Esempio di richiesta

Un **browser** (Mozilla/5.0) che implementa "HTTP/1.1" **richiede** l'oggetto "/somedir/page.html" al server "www.someschool.edu". Il messaggio ha cinque righe: la riga di richiesta GET (risorsa e versione), il body vuoto, e quattro header (host, connection, user-agent, accept-language):

```
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
Connection: close
User-agent: Mozilla/5.0
Accept-language: fr
```

`Host: www.someschool.edu` specifica l'host su cui risiede l'oggetto: la destinazione non è sempre il prossimo host, perché un messaggio può essere **inoltrato da un altro host** (es. proxy), quindi l'indirizzo TCP può differire dall'host di destinazione reale. `Connection: close` chiede una connessione non persistente (chiudi alla fine). `User-agent: Mozilla/5.0` specifica il tipo di browser: ciò è utile perché il **server può inviare versioni diverse** dello stesso oggetto (stesso URL) a seconda del tipo. `Accept-language: fr` indica che l'utente preferisce la versione francese dell'oggetto (se esiste).

### Formato del messaggio di risposta

Il formato generale è simile alla richiesta, ma invece della riga di richiesta c'è una **riga di stato** (*status line*) che riporta l'esito del comando, con: la **versione** (la versione HTTP della risposta del server), il **codice di stato** (un numero che specifica l'esito del comando) e la **frase** (contiene il risultato della richiesta).

### Codici di stato

I codici di stato sono divisi in classi:

- 100-199 **informativi**: informazioni sulla richiesta.
- 200-299 **successo**: la richiesta è stata eseguita con successo.
- 300-399 **redirezione**: sono necessarie azioni aggiuntive da parte del client.
- 400-499 **errore client**: la richiesta non può essere eseguita per un problema del client.
- 500-599 **errore server**: la richiesta non può essere eseguita per un problema del server.

Esempi tipici: **200 OK** (richiesta riuscita, l'informazione è restituita nella risposta), **301 Moved Permanently** (l'oggetto richiesto è stato spostato permanentemente; il nuovo URL è nell'header "Location" della risposta), **400 Bad Request** (errore generico, la richiesta non è stata compresa dal server), **404 Not Found** (il documento richiesto non esiste su questo server), **505 HTTP Version Not Supported** (la versione di HTTP richiesta non è supportata dal server).

### Esempio di risposta

La status line indica che il server usa HTTP/1.1 e che tutto è OK (l'oggetto è stato trovato e viene inviato); il **body contiene l'oggetto richiesto**:

```
HTTP/1.1 200 OK
Connection: close
Date: Tue, 18 Aug 2015 15:44:04 GMT
Server: Apache/2.2.3 (CentOS)
Last-Modified: Tue, 18 Aug 2015 15:11:03 GMT
Content-Length: 6821
Content-Type: text/html

(data data data data data ...)
```

`Connection: close` comunica che la connessione verrà chiusa dopo questo messaggio (non persistente); `Date` riporta data e ora in cui la risposta è stata creata e inviata dal server; `Server` indica che il messaggio è stato generato da un server Apache (analogo a user-agent); `Last-Modified` riporta data e ora di creazione/ultima modifica dell'oggetto, utile per il caching perché i file in cache possono non essere aggiornati; `Content-Length` è il numero di byte dell'oggetto; `Content-Type` indica che l'oggetto è testo HTML (il tipo è indicato ufficialmente da questo header, non dall'estensione del file).

## Cookie

Un server HTTP è tipicamente **stateless**: questo semplifica la progettazione, riduce l'uso di risorse e permette a un server di gestire migliaia di connessioni TCP simultanee. La statelessness pura è però un limite forte, perché diverse funzioni web sono specifiche del client: il carrello di Amazon dipende dal client, Netflix suggerisce contenuti in base alle preferenze, e così via. Per questi scopi HTTP usa i **cookie**: un cookie è un token digitale (ID alfanumerico) usato dai server per identificare un client specifico, **creato dal server** e consegnato al client. I cookie permettono ai siti di tracciare gli utenti (la maggior parte dei grandi siti commerciali li usa) e possono avere attributi, come la data di scadenza.

La tecnologia dei cookie ha quattro componenti principali:

1. Un header **"Set-cookie"** nel messaggio di risposta HTTP.
2. Un header **"Cookie"** nel messaggio di richiesta HTTP.
3. Un **file** sul sistema client (gestito dal browser).
4. Un **database di back-end** sul server.

### Esempio

Si consideri un host client che usa regolarmente eBay e **contatta Amazon.com per la prima volta**: ha già un cookie per eBay ma non per Amazon. Quando la richiesta arriva al server Amazon, **il server crea un cookie** (numero ID) e una voce associata nel suo database di back-end, poi risponde al browser **includendo nella risposta un header "Set-cookie"** con l'ID (`Set-cookie: 1678`). Ricevuta la risposta, **il browser aggiunge una riga a un file cookie speciale** con l'hostname del server e il numero ID del cookie. Da quel momento le richieste del client ad Amazon saranno associate al nuovo cookie, includendo l'header `Cookie: 1678` nei messaggi HTTP. Il server Amazon può così **tracciare l'attività del client nel database**: sa esattamente quali pagine l'utente 1678 ha visitato, in che ordine e in quali momenti. Se il client torna sul sito una settimana dopo, il browser continuerà a inserire `Cookie: 1678` nelle richieste.

### Usi dei cookie

Amazon (e altri siti) può usare i cookie per servizi diversi: il **carrello** (il server mantiene la lista degli acquisti intenzionati durante la navigazione), la **registrazione utente** (associando le informazioni dell'utente al cookie nel database — carta di credito, nome, e-mail, indirizzo — così da non reinserirle ogni volta) e i **consigli sui prodotti**, basati sulle pagine visitate. Sebbene i cookie semplifichino l'esperienza d'acquisto, sono **controversi** perché possono essere considerati un'invasione della privacy: combinando cookie e informazioni di account fornite dall'utente, un sito può imparare molto su di lui e potenzialmente vendere queste informazioni a terzi.

## Web caching

Una **Web cache** è un'entità di rete che soddisfa richieste HTTP per conto di un server Web di origine; queste entità intermedie che lavorano per conto di altri si chiamano **proxy server**. La Web cache ha un suo spazio su disco e **conserva copie degli oggetti richiesti di recente**; un browser può essere configurato così che tutte le **richieste HTTP vadano prima alla Web cache**, per verificare se è disponibile una copia dell'oggetto.

### Funzionamento

Si assume che un browser richieda `http://www.someschool.edu/campus.gif` passando per una Web cache:

1. Il **browser apre una connessione TCP** con la Web cache e le invia la richiesta HTTP dell'oggetto.
2. La Web cache **controlla se ha una copia locale** dell'oggetto; in tal caso, la restituisce al browser in un messaggio di risposta HTTP.
3. Se la **cache non ha l'oggetto**, apre una connessione TCP al server di origine (www.someschool.edu) e gli invia la richiesta.
4. Ricevuto l'oggetto, la **cache ne memorizza una copia** in locale e ne invia una copia al browser in un messaggio di risposta.

Si noti che la cache è **sia server** (quando fornisce oggetti) **sia client** (quando li richiede). Il caching Web è stato adottato su Internet per due ragioni: una cache può **ridurre sensibilmente il tempo di risposta** per il client, soprattutto se tra client e cache c'è una connessione ad alta velocità, e può **ridurre sensibilmente il traffico** verso Internet di un'azienda o istituzione, riducendo i costi di banda.

### Hit rate

Le cache Web sono spesso installate nella rete locale di aziende e istituzioni per accelerare e ridurre il traffico. Un **hit** avviene quando una cache fornisce un oggetto senza contattare il server originale; il tasso di hit (frazione di richieste soddisfatte dalla cache) tipicamente **va da 0,2 a 0,7** e cresce al crescere dei client che usano la cache. Significa che fino al 70% delle richieste può essere servito localmente.

### Il problema dell'aggiornamento: conditional GET

Il caching introduce un problema: la copia nella cache può essere **obsoleta**. Per evitarlo, HTTP ha un meccanismo che permette alla cache di verificare l'oggetto memorizzato: il **conditional GET**, un messaggio di richiesta HTTP con metodo GET e header "If-Modified-Since:". La cache **controlla se l'oggetto è aggiornato** e, in tal caso, la versione memorizzata è rispedita all'host, senza necessità di altre comunicazioni.

### Caching nel browser

Il caching avviene anche localmente nei browser. Il principio è lo stesso: il browser memorizza gli oggetti in locale, così non devono essere riscaricati dal server; è una tecnica comune nei browser moderni perché **migliora drasticamente le prestazioni**. La versione locale però può non essere aggiornata, generando errori (piuttosto frequenti).

### Oltre il caching

Oltre alle prestazioni, i **proxy server possono dare accesso a servizi istituzionali**: ad esempio la rete UNINA fornisce un proxy web istituzionale (proxy.unina.it). Poiché le richieste passano dal proxy istituzionale, dal punto di vista del server di origine **tutte le richieste provengono dall'istituzione**. Su Internet esistono anche diversi proxy commerciali o gratuiti.