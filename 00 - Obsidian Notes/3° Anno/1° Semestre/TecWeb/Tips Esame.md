# TIPS d'esame
## JavaScript
### Ereditarietà prototipale

> *"A volte ci sono delle domande che chiedono 'descrivi il funzionamento dell'ereditarietà'... secondo voi la risposta che io voglio quando dico 'scrivetemi...' è che ci stanno le classi e la parola chiave extends?"*

#### Cosa NON vuole (l'errore classico da evitare)

Il professore spiega che **non le basta** sentirsi dire semplicemente che in JavaScript esistono le classi e che si usa la sintassi `class ... extends ...`. Chi scrive solo questo dimostra di non aver capito come funziona davvero il linguaggio sotto il cofano.

#### La risposta che si ASPETTA (e che premia all'esame)

L'ereditarietà in JavaScript **non è basata sulle classi, ma sui prototipi**: ogni oggetto possiede una proprietà speciale interna (`[[Prototype]]` / `__proto__`) che punta al suo oggetto "antenato" (o a `null`).

- **Risalita della catena in lettura**: quando si accede a una proprietà o a un metodo di un oggetto, se questo non viene trovato sull'oggetto stesso, l'interprete risale la catena dei prototipi fino a trovarlo o fino a raggiungere `null`.
- L'ereditarietà si può implementare interamente "a mano" senza usare la parola chiave `class`, sfruttando le **funzioni costruttore** e la proprietà `.prototype`.
- `class` ed `extends` (introdotte in ES6) sono solo **zucchero sintattico**: sotto il cofano si limitano a creare la medesima struttura di prototipi e funzioni costruttore.

Per far sì che le istanze di una funzione costruttore `A` ereditino da un oggetto `b`, si assegna `b` alla proprietà `prototype` di `A` prima di creare l'istanza con `new`:

```js
function A() {}
let b = { b: 'B' };
A.prototype = b;
let a = new A();
```

### Scope, Temporal Dead Zone e "use strict"

> [!error] Accesso prima della dichiarazione  
> L'accesso a una variabile dichiarata con `let` o `const` prima della riga di dichiarazione genera un `ReferenceError` (**Temporal Dead Zone**), non `undefined`.

La direttiva `"use strict"` attiva la **strict mode**, che irrigidisce la semantica del linguaggio.

> [!error] Assegnazione a variabile non dichiarata  
> Con `"use strict"` attiva, l'assegnazione a una variabile non dichiarata causa un errore di esecuzione.

### Asincronismo e Promise

I comportamenti caratteristici dell'asincronismo in JavaScript sono due.

- **Executor sincrono**: l'executor passato a `new Promise((resolve, reject) => ...)` viene eseguito immediatamente e in modo sincrono al momento della creazione della Promise.
- **Funzioni `async`**: una funzione `async` restituisce sempre una Promise; se restituisce un valore semplice, questo viene automaticamente racchiuso in una Promise già risolta.

## CSS

### Specificità

La specificità di un selettore si esprime come terna `(A, B, C)`, confrontata da sinistra a destra.

| Composto del selettore          | Specificità |
| ------------------------------- | ----------- |
| ID                              | `(1,0,0)`   |
| Classi, pseudoclassi, attributi | `(0,1,0)`   |
| Elementi                        | `(0,0,1)`   |

Le pseudoclassi funzionali seguono regole particolari.

- `:is()`, `:not()` e `:has()` assumono la specificità dell'argomento **più specifico** presente tra le parentesi.
- `:where()` ha sempre specificità **zero**, `(0,0,0)`.

## HTML

### Caricamento degli script

Il comportamento di un tag `<script>` rispetto al parsing dell'HTML dipende dagli attributi `async` e `defer`.

- **Script standard**: il parsing dell'HTML si interrompe immediatamente per scaricare lo script dalla rete ed eseguirlo, poi riprende.
- **`defer`**: lo script viene scaricato in parallelo durante il parsing, ma l'esecuzione è posticipata al completamento del parsing dell'intero documento; l'ordine di esecuzione tra script è garantito.
- **`async`**: lo script viene scaricato in parallelo durante il parsing; appena il download termina, il parsing viene interrotto per eseguire immediatamente lo script; l'ordine tra più script `async` non è garantito.

### Form HTTP

> [!def] Controllo successful  
> **Controllo** di un form che partecipa all'invio dei dati al server.

**Condizioni**: il controllo possiede l'attributo `name` e non possiede l'attributo `disabled`.

## HTTP

### Metodi

Le proprietà dei metodi HTTP riguardano l'effetto delle richieste sullo stato del server.

- **Safe**: metodo che non altera lo stato del server; lo sono `GET`, `HEAD` e `OPTIONS`.
- **Idempotente**: `N` richieste identiche producono lo stesso effetto sul server; lo sono `GET`, `HEAD`, `OPTIONS`, `PUT` e `DELETE`.
- `POST` e `PATCH` non sono garantiti né safe né idempotenti.

| Metodo    | Safe | Idempotente |
| --------- | ---- | ----------- |
| `GET`     | sì   | sì          |
| `HEAD`    | sì   | sì          |
| `OPTIONS` | sì   | sì          |
| `PUT`     | no   | sì          |
| `DELETE`  | no   | sì          |
| `POST`    | no   | no          |
| `PATCH`   | no   | no          |

### Validazione e caching

La validazione condizionale e la cache condividono un meccanismo a base di header.

- **`304 Not Modified`**: codice restituito quando le intestazioni di richiesta condizionale (`If-Modified-Since`, `If-None-Match`) coincidono con quelle del server (`Last-Modified`, `ETag`), evitando il reinvio del body.
- **Header `Vary`**: specifica quali header di richiesta (es. `Accept-Encoding`, `Accept-Language`) devono combaciare affinché una risposta in cache possa essere servita a una richiesta successiva.

## DNS

### Protocollo di trasporto

La scelta del protocollo di trasporto del DNS dipende dalla dimensione dello scambio e dall'affidabilità richiesta.

- Il DNS utilizza primariamente **UDP** (porta 53) per le normali interrogazioni e risposte client-server: richiede bassa latenza ed evita l'overhead del Three-Way Handshake TCP.
- Utilizza invece **TCP** quando la dimensione della risposta supera i 512 byte (o il limite stabilito da EDNS), oppure per le operazioni di **trasferimento di zona** (*Zone Transfer*) tra Name Server, dove la garanzia di affidabilità del canale è fondamentale.

## Backend

### Componenti di un'applicazione web

Un'applicazione web tradizionale si compone di quattro componenti fondamentali.

1. **Frontend**: responsabile del rendering dei documenti HTML/CSS/JS recepiti dal browser.
2. **Router (backend)**: riceve la richiesta HTTP, ne analizza il path e il metodo e la smista al relativo handler/controller.
3. **Controllers e logica di business**: eseguono le operazioni del sistema e gestiscono la persistenza dei dati comunicando con il database.
4. **Template engine**: componente dedicato alla generazione dinamica dell'HTML da inviare in risposta, disaccoppiando la presentazione dalla logica applicativa.

### Interfaccia CGI

> [!def] CGI  
> **Interfaccia** standard che permette a un web server di eseguire un programma esterno per generare risposte HTTP dinamiche.

#### Passaggio dell'input (server → programma)

I metadati della richiesta, la query string e gli header sono messi a disposizione come **variabili d'ambiente** (es. `REQUEST_METHOD`, `QUERY_STRING`, `CONTENT_LENGTH`); il body della richiesta passa invece attraverso lo `stdin`.

#### Generazione dell'output (programma → server)

Tutto ciò che il programma scrive sullo `stdout` viene catturato dal server per costruire la risposta HTTP, compresi gli header della risposta, la riga vuota e il body.

### Node.js ed Express

> [!info] Event loop vs multithreading  
> **Architettura** di Node.js: single-threaded, basata su event loop, con I/O non bloccante; si contrappone all'architettura multithread con I/O bloccante.

#### Comandi npm

I comandi principali del gestore di pacchetti sono `npm init`, `npm install`, `npm start`, `npm test` e `npm run <script>`.

#### Middleware ed errori

Due elementi del backend Express sono caratteristici.

- **Middleware di gestione errori**: si distingue dagli altri middleware perché accetta 4 parametri, `(err, req, res, next)`.
- **Gestione delle dipendenze**: `package.json` dichiara le dipendenze e `npm install` le reinstalla; la cartella `node_modules` non viene mai distribuita né versionata.

### Gestione delle sessioni

Nel backend, la gestione delle sessioni associa un ID di sessione, inviato tramite cookie, a una struttura dati (**session store**) salvata sul server.

#### Logout da tutti i dispositivi

Il server accede al proprio session store e cancella, o invalida, tutte le sessioni associate a quello `username` (o ID utente). Una richiesta successiva con il vecchio cookie non trova più la sessione nello store e ottiene un errore di autenticazione (es. `401 Unauthorized`) o un redirect alla pagina di login.

> [!error] Cancellare i cookie da remoto  
> Il server non può "spingere" né cancellare da remoto i cookie presenti sul browser di un client senza che questo invii prima una richiesta HTTP.
