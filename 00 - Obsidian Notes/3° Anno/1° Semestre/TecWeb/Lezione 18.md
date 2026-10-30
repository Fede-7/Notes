# Lezione 18 Web app con Express

## Object-Relational Mapping

Quando si sviluppa software object-oriented che persiste dati in un RDBMS si gestiscono due rappresentazioni degli stessi dati: **oggetti nello heap** e **righe in tabelle relazionali**.

Le due rappresentazioni sono molto diverse e vanno tenute allineate: le modifiche ai domain object devono essere mappate sullo schema del RDBMS, e le modifiche allo schema possono impattare il codice esistente. Servono una buona quantità di lavoro e di codice boilerplate ripetitivo.

> [!def] Libreria ORM
> **Soluzione pronta all'uso** che supporta gli sviluppatori nel tenere allineate la rappresentazione a oggetti e quella relazionale, consentendo di lavorare con astrazioni ad alto livello invece che con query e statement SQL.

In genere una libreria ORM permette di:

- **Definire dichiarativamente** come le tabelle del database vengono mappate su oggetti.
- **Creare e aggiornare automaticamente** lo schema del RDBMS quando serve.
- **Eseguire facilmente le operazioni CRUD** (Create, Read, Update, Delete).
- **Comporre ed eseguire query complesse** in modo dichiarativo.
- **Gestire transazioni** e **supportare strategie di caching**.

I benefici sono minore boilerplate, più produttività e cambio più facile di RDBMS. Esempi noti: **Hibernate** (Java), **Entity Framework** (C#), **SQLAlchemy** (Python), **Propel** (PHP), **Active Record** (Ruby on Rails), **Sequelize**, **Prisma** e **TypeORM** (Node.js). I framework opinionati a volte includono un proprio ORM.

## Sequelize

> [!def] Sequelize
> **ORM per Node.js** che supporta Postgres, MySQL, MariaDB, SQLite, SQL Server e altri DB, con un'elegante API basata su Promise.

Si installa con `npm install sequelize` più il driver del RDBMS scelto (per il corso si usa SQLite, con il driver `sqlite3`). La connessione si crea istanziando `Sequelize` con la stringa di connessione:

```js
import { Sequelize } from "sequelize";
const database = new Sequelize("sqlite:mydb.sqlite");
await database.authenticate();
```

### Modelli

> [!def] Modello
> **Classe che estende `Model`** e definisce come una tabella del database viene mappata su oggetti; è l'essenza di ogni ORM.

Esistono due modi equivalenti di definire un modello:

- Chiamare il metodo `define` sulla connessione al database.
- Creare una classe che estende `Model` e chiamare poi il suo metodo `init`.

```js
const User = database.define('User', {
  firstName: { type: DataTypes.STRING, allowNull: false },
  age: { type: DataTypes.INTEGER }, // allowNull default: true
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true }
});
```

### Sincronizzazione dei modelli

All'avvio il database è vuoto: **model synchronization** è il meccanismo con cui Sequelize allinea lo schema del database ai modelli definiti, tramite il metodo asincrono `model.sync()`, che ritorna una Promise.

Alcuni aspetti del processo:

- Sequelize nomina le tabelle col **plurale** del nome del modello, salvo override esplicito.
- Prima verifica che la tabella esista (`SELECT` di controllo, poi `CREATE TABLE IF NOT EXISTS`); se esiste già, non fa nulla.
- Chiamando `sync()` sulla connessione si sincronizzano tutti i modelli insieme.

Le modalità di sincronizzazione sono tre:

- `User.sync()`: crea la tabella solo se non esiste.
- `User.sync({ force: true })`: ricrea la tabella, droppandola se esiste — è distruttivo.
- `User.sync({ alter: true })`: controlla lo stato della tabella (colonne, tipi…) e la altera per farla combaciare col modello.

### Creazione, lettura, modifica, cancellazione

Un'entità si può creare in due modi: istanziare il modello con `new` e chiamare `save()`, oppure usare il metodo statico `Model.create()`:

```js
let riff = await User.create({ name: "Riff Raff", age: 26 });
```

La lettura dei dati usa metodi dedicati sui modelli:

- `findAll()` recupera tutte le istanze; accetta un oggetto `where` con operatori della costante `Op` (es. `Op.gte`, `Op.like`) per filtrare.
- `include: [User]` carica anche le associazioni, che per default non vengono recuperate.
- `findByPk(pk)` recupera un'entità a partire dalla sua chiave primaria.

Per aggiornare un'entità si usa `setDataValue()` seguito da `save()`, che riscrive la riga sul database; per cancellarla si chiama `destroy()`, che elimina la riga.

### Associazioni

Sequelize supporta associazioni **uno-a-uno**, **uno-a-molti** e **molti-a-molti**:

- `A.hasOne(B)`: A ha una B.
- `A.belongsTo(B)`: A appartiene a B.
- `A.hasMany(B)`: A ha molte B.
- `A.belongsToMany(B, { through: 'C' })`: A è collegata a molte B tramite la tabella di giunzione C.

Definendo un'associazione, Sequelize crea automaticamente una colonna foreign key sul modello target, per default chiamata `NomeModello` + `NomePK` (es. `UserId` su `Todo`). Un'istanza può essere creata insieme alle sue associazioni annidate in un solo passo, purché tutti gli elementi siano nuovi, passando le entità figlie e l'opzione `include: [Modello]`.

### Pro e contro dell'ORM

I vantaggi principali dell'approccio ORM sono:

- **Astrazione**: si lavora con oggetti e modelli invece che con SQL.
- **Produttività**: meno boilerplate, schema generato automaticamente.
- **Portabilità**: è facile passare tra RDBMS supportati.
- **Leggibilità e consistenza**: codice più leggibile del SQL grezzo, con pattern e convenzioni uniformi.

Gli svantaggi da tenere presenti:

- **Learning curve** più ripida e alcune operazioni più complesse che con SQL puro.
- **Vendor lock-in**: può essere difficile migrare a un ORM diverso.
- **Performance**: possibile overhead, soprattutto con uso improprio.

## Organizzazione di un'app Express

Express è unopinionated: non esiste un unico modo giusto di organizzare un'app. Un'organizzazione possibile prevede queste cartelle:

- **`views`**: contiene i template.
- **`routes`**: definizione dei Router, che dirigono le richieste al controller appropriato.
- **`controllers`**: business logic per la gestione delle richieste.
- **`models`**: definizione dei modelli dati e della connessione al database.
- **`middleware`**: middleware custom.
- **`public`**: file statici organizzati in sottodirectory.

## Configurazione dell'applicazione

Le web app dipendono da informazioni **sensibili** (API key, password del database, credenziali AWS) e da impostazioni **specifiche dell'ambiente** (URL del database di produzione/sviluppo/staging, livello di logging, …).

Hardcodare questi valori nel codice è una cattiva pratica per tre motivi:

- Non è sicuro quando il codice viene versionato in un repository pubblico.
- Cambiare un'impostazione può richiedere modifiche a più file.
- Produce "versioni" diverse dell'app (sviluppo, produzione…) da aggiornare e mantenere separatamente.

Il file di configurazione deve essere il punto unico dove cambiare queste impostazioni:

- Il file reale (es. `.env`) **non va versionato**: va inserito nel `.gitignore`.
- Si può versionare un file **dummy** (es. `.env.dummy`) che ciascuno rinomina e adatta ai propri valori.
- Pacchetti come **dotenv** leggono il file `.env` e ne rendono disponibile il contenuto, es. nell'oggetto globale `process.env`.

## To-do List con Express

> [!lab]
> 
> ### Configurazione dei middleware
> 
> La configurazione tipica dell'app registra, in ordine, template engine, logging, file statici, parsing del body, sessioni e gestione dei messaggi flash:
> 
> ```js
> app.set("view engine", "pug");
> app.use(morgan('dev'));
> app.use(express.static("public"));
> app.use(express.urlencoded({ extended: false }));
> app.use(session({ secret: 'fu-tzu the great master', resave: false,
>   saveUninitialized: false, cookie: { maxAge: 10*60*1000 } }));
> ```
> 
> - **Sessione**: `maxAge` del cookie espresso in millisecondi (nell'esempio, 10 minuti).
> - Completano la configurazione `flash()` e middleware custom che esportano i messaggi flash e lo stato di autenticazione verso le viste.
> 
> ### Rotte e gestione degli errori
> 
> La configurazione delle rotte monta i vari Router con `app.use(router)` e in coda:
> 
> - Una rotta **catch-all** (`app.get('/*splat')`) che, se raggiunta, risponde `404` renderizzando la pagina d'errore.
> - Un **error handler** con firma `(err, req, res, next)`: logga lo stack e risponde con status `err.status || 500` renderizzando la pagina d'errore con codice e descrizione.
> 
> Ogni router può registrare un middleware comune a tutte le sue rotte con `todoRouter.use(enforceAuthentication)`, e le rotte delegano al controller, che restituisce Promise; gli errori vengono inoltrati con `next(err)`.
> 
> ### Autenticazione con sessioni
> 
> Il controller di autenticazione verifica le credenziali cercando un utente con `findOne` su username e password della richiesta; se le credenziali sono valide crea la sessione impostando `req.session.isAuthenticated = true` e salvandovi lo username, altrimenti fallisce l'autenticazione.
> 
> Il middleware che impone l'autenticazione è il seguente:
> 
> ```js
> export function enforceAuthentication(req, res, next) {
>   if (!req?.session?.isAuthenticated) {
>     req.flash("error", "You must be logged in to access this feature.");
>     res.redirect("/auth");
>   } else { next(); }
> }
> ```
> 
> Il middleware redirige gli utenti non autenticati alla pagina di login con un messaggio flash d'errore; altrimenti passa il controllo al successivo. I controller usano lo username in sessione per filtrare i dati dell'utente corrente, es. con `Todo.findAll({ where: { ... } })` sulla chiave esterna dell'utente.