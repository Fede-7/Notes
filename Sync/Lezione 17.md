# Lezione 17 Web Frameworks: Express

## Dalla programmazione server-side ai framework

Le applicazioni web sviluppate con la sola programmazione server-side (CGI con Bash, PHP 8.2, Node.js "puro") condividono attività ricorrenti: gestione della **routing**, rendering dei **template**, gestione delle **sessioni** web, gestione di **autenticazione/autorizzazione**. Senza un framework, queste attività presentano alcuni punti deboli:

- Molte operazioni **tediose** da reimplementare ogni volta, come il parsing dei cookie e la lettura e l'analisi dei corpi delle richieste.
- Nessuna gestione delle sessioni out-of-the-box, salvo PHP.
- Nessun supporto out-of-the-box per i **middleware** (es. autenticazione) e nessun **templating** out-of-the-box.

L'obiettivo di un framework è non reinventare la ruota in ogni progetto.

## Framework e librerie

Framework e librerie software sono cose diverse, e si distinguono per chi è al controllo del flusso di esecuzione.

### Libreria software

> [!def] Libreria software
> **Insieme di funzioni** richiamabili per far svolgere un certo lavoro: ogni chiamata esegue il compito e poi **restituisce il controllo al chiamante**.
> Il codice utente (es. il metodo `main`) è **al controllo del flusso di esecuzione**.

### Framework

> [!def] Framework
> **Insieme predefinito di componenti software, strumenti e buone pratiche** che serve da fondamenta per lo sviluppo di software; **incarna un progetto astratto** con molto comportamento già integrato.
> Il codice scritto dall'utente può essere **collegato (plugged-in)** al framework, che è **al controllo del flusso di esecuzione** e invoca il codice utente quando appropriato.

Un **web framework** è un framework progettato specificamente per semplificare e snellire lo sviluppo di applicazioni web: fornisce un modo (strutturato) di costruirle e organizzarle, riducendo la necessità di ripartire da zero.

### Inversion of Control

> [!def] Inversion of Control
> **Principio** in base al quale il flusso di controllo è **invertito** rispetto alla programmazione imperativa tradizionale: la responsabilità di gestire il flusso di esecuzione si sposta dallo sviluppatore al framework.

L'IoC è una **caratteristica distintiva** dei framework, nota anche come *legge di Hollywood*:

> [!quote] Hollywood's Law
> "Don't call us, we'll call you."

Il confronto tra i flussi di controllo in una libreria e in un framework:

![[8ba020a4df23b4ac9b4eac109e4ec327d0b8fa313d268e56b7d81e8b7f25a602.jpg|400]]

![[4248a9b5a5e6fb3ed49c2e9b0fffab8095fda414118da9a142e6621693049ade.jpg|400]]

## Componenti dei web framework

Un web framework tipicamente include tre componenti:

- **Funzionalità core**: routing, parsing delle richieste, validazione degli input, gestione dei cookie, gestione delle sessioni.
- **Template engine**: aiuta il rendering di contenuto dinamico, separando la logica del codice dal livello di presentazione.
- **ORM** (*Object-Relational Mapping*): semplifica le interazioni col database permettendo di lavorare con oggetti invece di query SQL.

### Framework opinionati

I framework possono essere più o meno **opinionati**.

> [!def] Framework opinionato
> **Framework** dotato di un insieme rigido di convenzioni, buone pratiche e decisioni predefinite prese dai suoi autori: impone uno specifico modo di fare le cose e lascia meno libertà agli sviluppatori.
> Un framework **unopinionated** non impone alcuno specifico modo di fare le cose.

- **Pro**: garantiscono livelli più alti di **consistenza** tra progetti diversi; possono velocizzare lo sviluppo riducendo la *decision fatigue*.
- **Contro**: curva di apprendimento potenzialmente più ripida; possono non essere sufficientemente flessibili per un certo progetto.

## Express

Esistono molti web framework server-side tra cui scegliere; come esempio del corso si vede **Express**, descritto come *fast, unopinionated, minimalist web framework* per **Node.js**: di gran lunga il framework backend più popolare per Node.js.

### Prima applicazione

Il pacchetto si installa con `npm install express`; un'applicazione minima crea l'app, definisce una route e mette il server in ascolto:

```js
import express from "express";
const app = express(); // crea un'applicazione Express
app.get('/', (req, res) => { res.send('Hello World!'); });
app.listen(3000);
```

### Routing

La **routing** è il modo in cui il framework determina come gestire una richiesta a un dato **endpoint**; una route si definisce con metodi appropriati sull'oggetto `app`, nella forma `app.<METHOD>(<PATH>, callback)`, dove `<METHOD>` e `<PATH>` identificano un endpoint e `callback` è la funzione eseguita per gestire le richieste a quell'endpoint.

```js
app.get("/hello", (req, res) => { res.send("Hello"); });
app.post("/hello", (req, res) => { res.send("Hello Post"); });
```

#### Route path

I path delle route possono essere stringhe, pattern di stringhe o espressioni regolari complete; in caso di corrispondenze multiple si applica la prima route che fa match.

```js
app.get("/webtech", (req, res) => { res.send("Web Technologies!"); });
// corrisponde a /webtech, /wirelesstech, /whatever-tech, ...
app.get(/^\w.*tech$/, (req, res) => { res.send("Regex!"); });
```

#### Parametri di route

Le route possono catturare segmenti URL con nome, detti **parametri**, dichiarati nel `<PATH>` con `:paramName`; i valori catturati sono resi disponibili nell'oggetto `req.params`.

```js
// GET /student/42/exams/TecWeb
app.get("/student/:student_id/exams/:exam_name",
    (req, res) => { res.send(req.params); }
); // {"student_id":"42","exam_name":"TecWeb"}
```

#### Più handler per route

Una route può avere più funzioni **handler**, che si comportano come middleware; `next` è il callback che invoca la funzione handler successiva da eseguire.

```js
let f1 = function (req, res, next) { console.log("f1"); next(); };
app.get("/handlers", [f1, f2, f3], (req, res) => {
    res.send("Done with all handlers");
});
```

#### Route concatenabili

Con `app.route()` il path è specificato in un'unica posizione (meno ridondanza) e gli handler specifici per metodo vengono concatenati:

```js
app.route('/book')
    .get((req, res) => { res.send('Get a random book'); })
    .post((req, res) => { res.send('Add a book'); })
    .delete((req, res) => { res.send('Delete a book'); });
```

#### Router modulari

`express.Router()` crea un **router modulare**, caricabile all'occorrenza; si monta con `app.use(<path>, router)`, e le richieste al path indicato (es. `/custom/echo/:value`) vengono gestite dal router.

```js
// router.js
export const router = express.Router();
router.get("/echo/:value", (req, res) => { res.send(req.params.value); });
// index.js
app.use("/custom", echoRouter);
```

### Metodi della risposta

Per inviare una risposta al client vanno chiamati metodi appropriati sull'oggetto `res`, altrimenti la richiesta resta appesa:

| Metodo | Descrizione |
|---|---|
| `res.download()` | Richiede il download di un file. |
| `res.end()` | Termina il processo di risposta. |
| `res.json()` | Invia una risposta JSON. |
| `res.jsonp()` | Invia una risposta JSON con supporto JSONP. |
| `res.redirect()` | Redirige una richiesta. |
| `res.render()` | Fa il rendering di un template. |
| `res.send()` | Invia una risposta di vario tipo. |
| `res.sendFile()` | Invia un file come octet stream. |
| `res.sendStatus()` | Imposta il codice di stato e ne invia la rappresentazione testuale come corpo. |

### Rendering dei template

Il rendering di un template (es. **Pug**) è un processo diretto: si imposta il template engine con `app.set()` e si renderizza una vista con `res.render()`; inoltre, i dati impostati in `res.locals` sono disponibili a tutte le viste che renderizzano `res`.

```js
app.set("view engine", "pug");
app.get("/example", (req, res) => {
    res.locals.items = [{name: "Web tech.", grade: "A+"}];
    res.render("example"); // items è disponibile nella vista
});
```

### Ciclo richiesta-risposta

Il ciclo richiesta-risposta è il cuore del framework Express:

1. Creazione degli oggetti richiesta e risposta.
2. Esecuzione di una sequenza di uno o più passi di calcolo per processare la richiesta, come il parsing del corpo, il parsing dei cookie e l'istituzione di una sessione.
3. Preparazione e invio della risposta.

![[54c6cae737bf1985f450daf0f5efc4d6ffad69c7c295bc54ef349b0e726e5d90.jpg|400]]

## Middleware

> [!def] Middleware
> **Funzione** che può manipolare gli oggetti richiesta e risposta correnti o eseguire codice arbitrario; è così chiamata perché eseguita tra la ricezione di una richiesta e l'invio della relativa risposta.
> I middleware sono eseguiti **nell'ordine di dichiarazione** e ricevono in input `req` (la richiesta HTTP), `res` (la risposta HTTP) e `next`, un callback che invoca il middleware successivo nello stack.

Un middleware si monta con `app.use()`, che lo registra su un dato path (default `/`):

```js
export function addTimestamp(req, res, next) {
    req.timestamp = new Date();
    next();
}
app.use(addTimestamp); // monta il middleware sul path "/"
app.get('/', (req, res) => { res.send(`Ts: ${req.timestamp}`); });
```

### Gestione degli errori

È importante assicurarsi che ogni errore occorso durante l'elaborazione di middleware o route sia gestito correttamente da Express:

- Un errore **lanciato** durante l'esecuzione di codice **sincrono** è catturato automaticamente dal default error handler di Express.
- Gli errori restituiti da **funzioni asincrone** invocate da route handler e middleware devono essere passati alla funzione `next()`.

```js
app.get('/readfile', (req, res, next) => {
    fs.readFile('/file-does-not-exist', (err, data) => {
        if (err) next(err); // passa l'errore a Express
        else res.send(data);
    });
});
```

A partire da **Express 5**, i route handler e i middleware che restituiscono una **promise** invocano automaticamente `next(value)` quando la promise si respinge o quando lanciano un errore: non è necessario farlo esplicitamente.

```js
app.get('/user/:id', async (req, res) => {
    const user = await getUserById(req.params.id);
    res.send(user);
});
```

### Error handler personalizzati

Express include un **default error handler** che stampa l'intero stack trace solo in *development mode*; è possibile definire error handler personalizzati, middleware speciali con **quattro parametri** in input:

```js
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});
```

## Middleware utili

Oltre a quelli scritti dal programmatore, esistono middleware pronti all'uso, built-in o disponibili via npm.

### express.static

Middleware built-in progettato per servire **file statici**: usa `req.url` per determinare se una richiesta corrisponde a un file o path della directory root specificata (es. `public`).

```js
app.use(express.static("public")); // montato nella root "/"
app.use("/static", express.static("public")); // path virtuale "/static"
```

### express.urlencoded

Middleware built-in che fa il parsing del corpo delle richieste con payload **urlencoded** (es. quelle inviate tramite form), rendendo i parametri disponibili nell'oggetto `req.body`; si registra con `app.use(express.urlencoded({extended: false}))`.

### express.json

Middleware built-in dal comportamento analogo a `express.urlencoded`, ma progettato per fare il parsing di corpi **JSON**: anche qui i valori finiscono in `req.body`.

### express-session

Middleware disponibile tramite **npm** che semplifica la gestione di una sessione conservata sul server: i dati di sessione sono conservati sul server, mentre l'**id di sessione** è conservato in un cookie.

> [!warning] Storage di sessione
> Lo storage server-side di default **non è production-ready**: per la produzione va configurato uno store di sessione dedicato (es. basato su *memcached* o *redis*).

```js
app.use(session({ secret: "s3cr37", resave: false, saveUninitialized: false }));
app.get("/session-counter", (req, res) => {
    if (!req.session.count) { req.session.count = 1; } // dati in req.session
    else { req.session.count = req.session.count + 1; }
});
```

### cookie-parser

Middleware disponibile tramite npm che fa il parsing dell'header `Cookie` delle richieste in arrivo e popola `req.cookies` con un oggetto le cui proprietà sono i nomi dei cookie.

### Flash message

Spesso, in un'applicazione web, l'utente viene rediretto dopo aver eseguito un'azione (es. alla homepage dopo una cancellazione): è una buona regola fornire un riscontro, così che sappia se l'operazione è riuscita o meno. La difficoltà è che dopo la redirezione inizia un **nuovo ciclo richiesta-risposta**: è una variante del solito problema di **HTTP** senza stato, e si risolve negli stessi modi visti in precedenza (cookie, sessioni).

- `connect-flash` è un semplice middleware per flash message, disponibile su npm, che si registra con `app.use(flash())`.
- `req.flash(chiave, messaggio)` salva un flash message nella sessione corrente.
- `req.flash(chiave)` consuma i flash message con la chiave data.

```js
app.get("/redirect", (req, res) => {
    req.flash("info", "You have been redirected."); // salva
    res.redirect("/showflash");
});
app.get("/showflash", (req, res) => {
    let infos = req.flash("info"); // consuma i messaggi con chiave "info"
});
```

Poiché i flash message sono **consumati alla lettura**, ricaricando la pagina (o visitandola direttamente senza essere stati rediretti) nessun flash message è presente nella sessione e non viene mostrato nulla.