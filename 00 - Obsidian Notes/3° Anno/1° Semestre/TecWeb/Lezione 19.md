# Lezione 19 REST API

## Dal server-centric all'architettura a due componenti

Nelle web app «tradizionali» il server si occupa di tutto: dati (con l'ORM), business logic (rotte, controller, middleware, sessioni) e presentazione (rendering dei template); il browser riceve pagine HTML generate dinamicamente, che una volta arrivate sono statiche.

Questo approccio non è abbastanza flessibile negli scenari moderni, in cui i dati devono essere accessibili anche ad altro software (es. app mobile):

- L'altro software deve scaricare le pagine HTML e **parserle** per estrarre i dati rilevanti.
- Il trasferimento è **inefficiente**: si spostano molti dati non necessari.
- Non è **robusto**: qualsiasi modifica all'HTML può rompere l'estrazione dei dati.

Il trend attuale è dividere la web app in due componenti che comunicano via Internet:

- **Backend** (lato server): responsabile di dati e business logic.
- **Frontend** (lato client): responsabile della UI; può essere un'app nativa mobile o desktop, oppure una pagina HTML "più smart" che rende un'interfaccia interattiva tramite JavaScript (Single Page Application).

## API e REST

> [!def] Application Programming Interface (API)
> **Insieme di modalità** con cui i programmi comunicano tra loro.

Per la comunicazione via Internet si potrebbe definire manualmente un protocollo su TCP/UDP con socket e simili, ma è poco conveniente e poco interoperabile: integrare n API richiederebbe di imparare n protocolli diversi. Protocolli e architetture dedicate come CORBA, Java RMI o SOAP reinventano un'alternativa al web. La scelta del corso è usare direttamente i protocolli del web, cioè HTTP.

> [!def] REST
> **Stile architettonale** — non uno standard né un protocollo — cioè un insieme di principi e linee guida che definisce come usare gli standard del web nelle API, basato su HTTP e URI.

REST fornisce un'interfaccia comune e consistente basata sull'uso «corretto» di HTTP ed è lo stile architettonale prevalente per le web API.

### Fondamenti

Una REST API permette di interagire con **risorse** tramite HTTP:

- Ogni risorsa è associata a una **URI unica**: una risorsa è «qualsiasi cosa sia abbastanza importante da essere referenziata come cosa a sé» e corrisponde tipicamente, ma non necessariamente, a oggetti di dominio persistenti.
- I **verbi HTTP** vanno usati per recuperare o manipolare le risorse.
- L'API deve essere **stateless**: niente sessioni lato server, il che ne migliora la scalabilità.

Il nome Representational State Transfer richiama il **transferimento di stato**: lo stato dell'applicazione vive sul client, lo stato della risorsa vive sul server, e vengono trasferiti tramite rappresentazioni appropriate (es. JSON, XML):

```json
{ "todos": [
  { "todo": "Learn REST", "done": false },
  { "todo": "Learn JavaScript", "done": true }
] }
```

L'uso tipico dei verbi HTTP su una collezione di to-do è il seguente:

| Verbo HTTP e URI | Significato |
|---|---|
| `GET /todos` | Recupera la lista di tutti i to-do salvati |
| `GET /todos/<ID>` | Recupera solo il to-do con quell'`<ID>` |
| `POST /todos` | Salva un nuovo to-do (dati nel body della richiesta) |
| `PUT /todos/<ID>` | Sostituisce (o crea) il to-do con quell'ID, usando i dati nel body |
| `DELETE /todos/<ID>` | Elimina il to-do con quell'ID |

### Risorse nidificate

A volte esiste una gerarchia tra risorse (es. una company ha dipartimenti, che hanno impiegati); si possono allora definire **nested resources**, es. `GET /sellers/{id}/reviews` elenca le recensioni di un dato venditore. Ogni risorsa però deve avere **una sola URI**.

### Archetipi di risorse

Quando si disegna una API si possono considerare quattro archetipi fondamentali di risorsa:

- **Document**: concetto singolare, corrisponde a un'istanza di un oggetto o a un record del database; es. `/leagues/serie-a/teams/napoli`. Regola: i nomi (non numerici) di un document sono singolari.
- **Collection**: directory di risorse gestita dalla web app; il client può proporre l'aggiunta di nuove risorse, ma è la risorsa a decidere se accettarla; es. `/leagues`, `/leagues/serie-a/teams`. Regola: i nomi sono plurali.
- **Store**: directory di risorse gestita dal client, che può creare, recuperare, aggiornare e cancellare le risorse; es. `/users/1234/favourites`. Regola: i nomi sono plurali.
- **Controller**: modella un concetto procedurale, una sorta di funzione eseguibile invocabile con parametri che produce un output o un effetto collaterale; es. `/alerts/1234/resend`, `/login`. Regola: i nomi sono verbi o frasi verbali.

### Query string: filtering e paginazione

La componente query della URI serve a **filtrare** collection e store:

- `GET /users` recupera tutti gli utenti; `GET /users?role=admin` solo quelli col ruolo specificato.
- Sono ammessi parametri strutturati: `GET /users?age.gt=18&age.lte=40`.

La stessa componente serve a **paginare** i risultati: `GET /todos?size=10&page=2` restituisce i risultati dall'11° al 20° (cioè la pagina 2).

Quando la complessità dei criteri supera le capacità espressive della query string, si può introdurre un **controller dedicato** nella collection o nello store, es. `POST /users/search`, che riceve i criteri di filtro complessi come oggetto nel body della richiesta.

## Implementazione di una REST API

Una REST API è concettualmente semplice: restare in ascolto di richieste HTTP e gestirle, esattamente come nelle app tradizionali. Le differenze sono:

- Si risponde con una rappresentazione più machine-friendly (es. JSON) invece dell'HTML da renderizzare.
- Si ricevono gli input in rappresentazione machine-friendly invece che tramite form.
- Non ci si può basare sulle sessioni: servono altri schemi di autenticazione.

## Sicurezza della API: token e JWT

Una REST API permette di manipolare risorse e in genere non tutti devono poterlo fare:

- **Autenticazione**: solo utenti legittimi possono accedere alle risorse.
- **Autorizzazione**: alcuni utenti possono accedere solo ad alcune risorse.

Uno schema di autenticazione ampiamente usato è **token-based**, con questo flusso:

1. Il client invia una richiesta con username e password alla API.
2. La API valida le credenziali e genera un token.
3. Il token (una stringa) viene restituito al client.
4. Il client rimanda il token alla API in ogni richiesta successiva che richiede autenticazione, nell'header `Authorization`.
5. La API verifica il token prima di rispondere.

> [!def] JSON Web Token (JWT)
> **Standard aperto (RFC 7519)** ampiamente adottato che permette di condividere in modo sicuro claim tra due parti; il token è una stringa di tre parti separate da `.`, nella forma `Header.Payload.Signature`.

- **Header**: JSON con il tipo di token e la funzione di hashing usata per firmarlo (es. `{"alg": "HS256", "typ": "JWT"}`), codificato con Base64Url.
- **Payload**: JSON contenente i **claim**, personalizzabili; alcuni claim registrati sono raccomandati, es. `exp` che indica la scadenza del token; anche questo è Base64Url.
- **Signature**: funzione di hash crittografica applicata alla concatenzione di header, payload e una **secret key** nota solo al server emittente; garantisce che il token non sia manomesso o contraffatto.

> [!warning] Base64Url è codifica, non cifratura
> Header e payload di un JWT sono semplicemente codificati e possono essere invertiti con facilità: chiunque può leggerne il contenuto. La sicurezza sta nella firma, non nella segretezza del contenuto.

> [!def] Funzione di hash crittografica
> **Funzione** che mappa una stringa binaria arbitraria (input) a una stringa binaria di dimensione fissa (digest o hash).

Le funzioni di hash crittografiche sicure hanno due proprietà chiave:

- Sono **praticamente senza collisioni**: è impossibile trovare due input diversi con lo stesso digest.
- Sono **facili da calcolare, impossibili da invertire**: dato un input è facile calcolare il digest, ma dato un digest è infeasibile risalire all'input che l'ha generato.

La firma JWT è in realtà un po' più complessa di una semplice hash (es. algoritmi HS256 e RS256).

### Con Express

La configurazione tipica registra questi middleware:

- `morgan('dev')` per il logging.
- `cors()`, che rende l'API accessibile da qualsiasi origine.
- `express.json()`, che parsa le richieste con payload JSON.

L'**error handler** risponde in JSON con status e descrizione dell'errore, usando `err.status || 500`.

L'emissione e verifica dei token usa la libreria `jsonwebtoken`:

```js
static issueToken(username) {
  return Jwt.sign({ user: username }, process.env.TOKEN_SECRET,
    { expiresIn: `${24*60*60}s` });
}
static isTokenValid(token, callback) {
  Jwt.verify(token, process.env.TOKEN_SECRET, callback);
}
```

Il middleware di autenticazione legge l'header `authorization`, estrae il token e lo verifica:

- Token assente o non valido → `next({ status: 401, message: "Unauthorized" })`.
- Token valido → salva lo username decodificato in `req.username` e chiama `next()`.

**Autorizzazione**: oltre all'autenticazione, occorre verificare che l'utente possa interagire con quella specifica risorsa (es. modificare solo i propri to-do). Un middleware dedicato, es. `ensureUsersModifyOnlyOwnTodos`, controlla con il controller di autenticazione se l'utente ha il permesso su quella risorsa; in caso negativo passa a `next({ status: 403, ... })`: **403 Forbidden**, non 401.

## OpenAPI

> [!def] OpenAPI
> **Standard formale e aperto** per descrivere API HTTP, noto un tempo come Swagger; le descrizioni sono documenti strutturati in JSON o YAML che rappresentano un oggetto JSON.

Le ragioni dell'esistenza dello standard:

- **Standardizzazione**: pratiche documentative consistenti.
- **Documentazione**: generazione automatica di documentazione completa.
- **Code generation**: generazione automatica di librerie client e server stub.
- **Leggibilità umana e machine-readable**: abilita la discovery automatizzata e altro.

È lo standard industriale più adottato. Una specifica minima contiene:

- `openapi`: la versione della specifica.
- `info`: informazioni sull'API (es. `title`, `version`).
- `paths`: gli endpoint dell'API, chiamati paths; per ciascun endpoint i metodi supportati e, per metodo, parametri attesi (path, header, …), request body e risposte possibili.

```yaml
openapi: 3.1.0
info:
  title: A minimal specification
  version: 0.0.1
paths: {} # No endpoints defined
```

Gli strumenti open source principali sono **Swagger Editor** (scrivere la specifica e vedere la documentazione), **Swagger Codegen** (stub server in molti linguaggi/framework: ASP.NET, Go, Java, Node.js, Python, Spring, …; client SDK in C#, Dart, Go, Java, Kotlin, PHP, Python, TypeScript, …) e **Swagger UI** (documentazione interattiva).

> [!info] OpenAPI-driven development
> Approccio in cui si definisce la specifica dell'API **prima** di scrivere il codice, sfruttando al massimo la generazione di codice; la definizione dell'API tiene allineati i team coinvolti (front-end, back-end, QA).

In Express si usano due pacchetti: **swagger-jsdoc**, che genera la specifica OpenAPI a partire da annotazioni nei commenti al codice sorgente, e **swagger-ui-express**, che serve la documentazione Swagger UI su un path scelto (es. `/api-docs`):

```js
/**
 * @swagger
 * /auth:
 *   post:
 *     description: Authenticate user
 */
authenticationRouter.post("/auth", async (req, res) => { /* ... */ });
```

## Regole di design REST

Un buon insieme di regole di base per il design di API RESTful è riportato di seguito; strumenti come RESTRuler rilevano automaticamente le violazioni di queste regole (REST antipatterns) nelle web API.

| Regola | Identificatore | Categoria |
|---|---|---|
| `401` per problemi con le credenziali del client | RC401 | Codici di stato HTTP |
| Nome plurale per collection e store | PluralNoun | URI Design |
| Nome singolare per document | SingularNoun | URI Design |
| Nessuna slash finale nelle URI | NoTrailingSlash | URI Design |
| Verbo o frase verbale per i controller | VerbController | URI Design |
| Niente nomi CRUD nelle URI | NoCRUDNames | URI Design |
| `Content-Type` sempre usato | ContentType | Metadata Design |
| Descrizione della richiesta coerente col tipo di richiesta | DescriptionType | Metadata Design |
| Slash iniziale `/` per la gerarchia | ForwardSlash | URI Design |
| `GET` e `POST` non devono "tunnelare" altri metodi | NoTunnel | Request Methods |
| `GET` solo per recuperare una rappresentazione di una risorsa | GETRetrieve | Request Methods |
| Trattini `-` per migliorare la leggibilità delle URI | Hyphens | URI Design |
| Lettere minuscole preferite nei path delle URI | Lowercase | URI Design |
| Niente underscore `_` nelle URI | NoUnderscores | URI Design |