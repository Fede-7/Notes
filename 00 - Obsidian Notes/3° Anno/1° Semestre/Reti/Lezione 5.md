# HTTP messaggi cookie e web caching

## HTTP riepilogo

**HyperText Transfer Protocol (HTTP)**: uno dei protocolli più usati su Internet (applicazioni web-based), con le seguenti proprietà:

- È **client-server** e definisce la struttura dei messaggi e come client e server li scambiano.
- **Non** decide come implementare le applicazioni client e server.
- Usa messaggi di tipo **richiesta/risposta**, scritti in **ASCII** leggibile.
- È **stateless**: client e server non ricordano le interazioni passate.
- Assume un trasporto affidabile e connection-oriented (TCP, recentemente anche UDP).
- Usa connessioni persistenti e non persistenti.

## Formato dei messaggi

HTTP ha due formati distinti:

- **Richiesta**: specifica il comando (**metodo**) che il server deve eseguire (es. dammi una pagina, elabora un form).
- **Risposta**: riporta l'esito del comando (successo, fallimento, ecc.) e i possibili dati (es. il file richiesto).

### Messaggio di richiesta

La richiesta include i seguenti campi:

- **Method**: comando richiesto al server.
- **URL**: identifica l'oggetto su cui operare.
- **Version**: versione HTTP (es. `HTTP/1.1`).
- **Header lines**: parametri della richiesta, in numero e tipo non fissi; ogni riga contiene nome e valore del parametro (es. persistenza della connessione; sono possibili header personalizzati).
- **Body**: dipende dal metodo, contiene dati potenzialmente associati al comando (es. testo di un form).

![[Lezione 5-1792082402962.webp|300]]

I campi sono separati da caratteri speciali: **sp** (spazio), **cr** (carriage return, `\r`), **lf** (line feed, `\n`).

Metodi principali:

- **`GET`**: recupera oggetti (risorse) dal server; è il comando più usato, poiché ogni pagina richiesta va recuperata; il body è vuoto.
- **`POST`**: imposta informazioni dentro oggetti (risorse) del server; il body contiene le informazioni da inviare. Le richieste generate da un form non usano necessariamente `POST`: i form HTML usano spesso `GET`, includendo i dati nell'URL richiesto.
- **`HEAD`**: come `GET`, ma il server risponde senza restituire l'oggetto; usato spesso per il debugging.
- **`PUT`**: carica un oggetto su un percorso (directory) specifico di un server Web; usato con strumenti di Web publishing e da applicazioni che caricano oggetti.
- **`DELETE`**: elimina un oggetto su un server Web.

Esempio di richiesta (browser Mozilla/5.0 che chiede `/somedir/page.html` a `www.someschool.edu`):

```http
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
Connection: close
User-agent: Mozilla/5.0
Accept-language: fr
```

Significato delle righe di header:

- **`Host`**: host su cui risiede l'oggetto; la destinazione non è sempre l'host successivo (il messaggio può passare da un proxy), quindi l'indirizzo nel TCP può differire dall'host reale di destinazione.
- **`Connection: close`**: il browser chiede una connessione **non persistente** (chiusura al termine).
- **`User-agent`**: tipo di browser; utile perché il server può inviare versioni diverse dello stesso oggetto (stesso URL) in base al tipo.
- **`Accept-language`**: preferenza linguistica dell'utente (es. versione francese dell'oggetto, se esiste).

### Messaggio di risposta

Il formato è simile alla richiesta, ma al posto della request line c'è una **status line** con:

- **Version**: versione HTTP della risposta del server.
- **Status code**: codice (numero) che specifica l'esito del comando.
- **Phrase**: frase con il risultato della richiesta.

![[Lezione 5-1792082528768.webp|300]]

Classi di status code:

- **100–199** informational: informazioni sulla richiesta.
- **200–299** successful: richiesta eseguita con successo.
- **300–399** redirection: servono azioni aggiuntive del client.
- **400–499** client-error: la richiesta non può essere eseguita per un problema del client.
- **500–599** server-error: la richiesta non può essere eseguita per un problema del server.

> [!example] 
>Codici tipici:
> - **200 OK**: richiesta riuscita, l'informazione è nella risposta.
> - **301 Moved Permanently**: l'oggetto è stato spostato permanentemente; la nuova URL è indicata nell'header `Location` della risposta.
> - **400 Bad Request**: errore generico, il server non ha capito la richiesta.
> - **404 Not Found**: il documento richiesto non esiste sul server.
> - **505 HTTP Version Not Supported**: versione del protocollo non supportata dal server.

> [!example] Esempio di risposta:
> 
> ```http
> HTTP/1.1 200 OK
> Connection: close
> Date: Tue, 18 Aug 2015 15:44:04 GMT
> Server: Apache/2.2.3 (CentOS)
> Last-Modified: Tue, 18 Aug 2015 15:11:03 GMT
> Content-Length: 6821
> Content-Type: text/html
> ```
> 

Significato degli header:

- **`Connection: close`**: la connessione verrà chiusa dopo questo messaggio (non persistente).
- **`Date`**: data e ora di creazione/invio della risposta da parte del server.
- **`Server`**: software che ha generato il messaggio (es. Apache; analogo a `User-agent`).
- **`Last-Modified`**: data di creazione o ultima modifica dell'oggetto; utile per il caching, poiché le copie in cache possono essere datate.
- **`Content-Length`**: numero di byte dell'oggetto.
- **`Content-Type`**: tipo dell'oggetto (es. `text/html`): il tipo è dichiarato ufficialmente da questo header e **non** dall'estensione del file.

## Cookie

Un server HTTP è tipicamente **stateless**: questo semplifica la progettazione, riduce l'uso di risorse e permette migliaia di connessioni TCP simultanee; ma la pura statelessness è un limite, perché diverse funzioni Web sono **client-specific** (es. carrello, suggerimenti basati sulle preferenze).

> [!def] Cookie
> **Token digitale** (ID alfanumerico) creato dal server e consegnato al client, usato dal server per **identificare un client specifico**; i cookie possono avere attributi (es. data di scadenza) e permettono ai siti di tenere traccia degli utenti.

La tecnologia dei cookie ha quattro componenti:

1. Una riga di header **`Set-cookie`** nel messaggio di risposta HTTP.
2. Una riga di header **`Cookie`** nel messaggio di richiesta HTTP.
3. Un **file sul sistema client**, gestito dal browser, che associa hostname del server e numero ID del cookie.
4. Un **database sul lato server**, con una voce per ogni cookie.

> [!aside]
> Funzionamento: alla prima richiesta di un client verso un sito, il server crea un cookie (numero ID) e la relativa voce nel proprio database; la risposta contiene l'header `Set-cookie: 1678`. Il browser aggiunge al file dei cookie hostname e ID; da quel momento ogni richiesta verso quel sito include l'header `Cookie: 1678`, così il server può tracciare l'attività dell'utente nel database (pagine visitate, ordine, tempi).
> 
> ---
> 
> ![[Lezione 5-1792082711902.webp|300]]

Usi principali e criticità:

- **Carrello**: il server mantiene la lista degli acquisti durante la navigazione.
- **Registrazione utente**: associando le informazioni dell'utente al cookie nel database (carta di credito, nome, e-mail, indirizzo) per non reinserirle ogni volta.
- **Consigli sui prodotti** basati sulle pagine visitate.

I cookie sono **controversi**: sono considerati un'invasione della privacy, poiché combinando cookie e informazioni fornite dall'utente un sito può sapere molto di lui e potenzialmente vendere tali informazioni a terzi.

## Web caching

> [!def] Web cache
> **Entità di rete** che soddisfa le richieste HTTP **per conto** di un server Web di origine (*origin server*); le entità intermedie che lavorano per conto di altri sono dette **proxy server**.

- La cache ha un proprio disco dove conserva copie degli oggetti richiesti di recente.
- Il browser può essere configurato per indirizzare **tutte** le richieste HTTP alla cache, che verifica la disponibilità di una copia dell'oggetto.
- Una cache è **sia server** (quando fornisce oggetti) **sia client** (quando li richiede) allo stesso tempo.

Procedura di accesso a un oggetto tramite cache (es. `http://www.someschool.edu/campus.gif`):

1. Il browser apre una connessione TCP con la cache e le invia la richiesta HTTP dell'oggetto.
2. La cache verifica di avere una copia locale: in caso affermativo la restituisce al browser in un messaggio di risposta.
3. Se non la possiede, la cache apre una connessione TCP con il server di origine e gli invia la richiesta.
4. Ricevuto l'oggetto, la cache ne memorizza una copia e ne invia una al browser in un messaggio di risposta.

Motivazioni del deployment:

1. **Ridurre il tempo di risposta** per il client, specialmente se tra client e cache c'è una connessione ad alta velocità.
2. **Ridurre il traffico** dell'azienda/istituzione verso Internet, riducendo i costi di banda.

Misure e problemi:

- **Hit**: la cache fornisce l'oggetto senza contattare il server di origine; l'**hit rate** (frazione di richieste soddisfatte dalla cache) è tipicamente tra **0.2 e 0.7**, e cresce all'aumentare dei clienti che usano la cache: fino al 70% delle richieste può essere servito localmente.
- **Problema di obsolescence**: la copia in cache può essere datata; per verificarla esiste il **conditional GET**: richiesta HTTP con metodo `GET` e header `If-Modified-Since:`, con cui la cache controlla se l'oggetto è aggiornato e, in tal caso, restituisce la versione memorizzata senza ulteriore comunicazione.
- Anche i **browser** fanno caching locale: memorizzano gli oggetti per non recuperarli dal server; la tecnica migliora molto le prestazioni, ma la versione locale può non essere aggiornata, generando errori piuttosto frequenti.

![[Lezione 5-1792083357474.webp|200]]

## Oltre il caching

- I proxy servono anche ad **accedere a servizi istituzionali**: le reti aziendali/universitarie forniscono un web proxy istituzionale (es. `proxy.unina.it`).
- Poiché le richieste sono inoltrate dal proxy istituzionale, dal punto di vista del server di origine **tutte le richieste arrivano dall'istituzione**.
- Su Internet esistono diversi proxy commerciali e gratuiti.