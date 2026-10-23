# Lezione 15 Web app con Node.js

## Il caso di studio

Come caso di studio per lo **scripting server-side** si implementa una **To-do list web app** in Node.js puro (v. 20.9.0), usando solo moduli standard di Node.js e il template engine Pug; l'app include un meccanismo di **session tracking** implementato da zero.

> [!warning] App didattica
> L'app è intesa come primo esempio basilare per mostrare lo scripting server-side: non è rappresentativa delle pratiche moderne di sviluppo web.

## Il server HTTP in Node.js puro

Node.js permette di implementare in modo semplice ed efficiente un **server HTTP** sfruttando i moduli built-in e il **single-threaded event loop**. Il server si crea a partire dal modulo `http`:

```js
import http from 'http';
const PORT = 3000;
let server = http.createServer();
server.listen(PORT);
server.on('request', handleRequest);
```

Node.js effettua anche del **pre-processing sulle richieste** (es. il parsing degli header) e fornisce un'astrazione per richieste (`http.IncomingMessage`) e risposte (`http.ServerResponse`). Al di là di questo, si è da soli nell'implementare l'app: i tre problemi da affrontare sono il **routing**, il **templating** e il **parsing del body delle richieste**.

## Routing

> [!def] Routing
> **Processo** che, data una richiesta HTTP, decide quale codice eseguire per servirla. Il componente che svolge questo compito è il **router**.

![[Lezione 15-1792748112696.png|200]]

### Percorsi

Le richieste a percorsi diversi dell'app (homepage, pagina della lista, pagina di reset, …) possono essere gestite da funzioni diverse, selezionate sull'URL della richiesta:

```js
function handleRequest(request, response) {
  switch (request.url) {
    case "/":
      renderHomepage(request, response);
      break;
    case "/todo":
      handleTodoListRequest(request, response);
      break;
    default:
      handleError(request, response, 404, "Web page not found");
  }
}
```

Quando nessuna delle rotte note si applica, si restituisce un errore **404** (pagina non trovata).

### Metodi HTTP

Le richieste allo stesso percorso possono essere gestite diversamente a seconda del **metodo HTTP** usato: un `GET` a `/todos` restituisce la lista degli elementi, un `POST` a `/todos` prova a salvarne uno nuovo.

```js
switch (request.method) {
  case "GET":
    handleTodoListRequestGet(request, response);
    break;
  case "POST":
    handleTodoListRequestPost(request, response);
    break;
  default:
    handleError(request, response, 405, "Unsupported method");
}
```

Un metodo non supportato viene segnalato con un errore **405**.

### File statici

Se l'output HTML include file statici (immagini, CSS, JS), il router va configurato per servirli leggendoli dal filesystem con `fs.readFile` e impostando il `Content-Type` appropriato:

```js
case "/css/bootstrap.css":
  fs.readFile('./static/css/bootstrap.css', function (err, data) {
    response.writeHead(200, {'Content-Type': 'text/css'});
    response.end(data, 'utf-8');
  });
  break;
```

> `function (err, data){...}` è una call-back

### Oltre il caso semplice

Il routing sembra semplice, ma può crescere in complessità insieme all'app.

> [!info] Complessità del routing
> - Alcune rotte possono essere accessibili solo ad alcuni utenti (es. amministratori).
> - Alcune rotte dipendono da pattern o parametri nella richiesta (es. `GET /users/42/friends`, dove `42` è un qualunque id utente).
> - Una richiesta può richiedere l'esecuzione di due o più pezzi di codice (es. una funzione che registra i dati e una diversa che prepara la risposta).

## Template engine

L'app deve produrre codice HTML da inviare nel body della risposta, così che il browser possa renderizzarlo. Nell'esempio più semplice l'HTML si scrive manualmente concatenando stringhe, ma parti di HTML si ripetono su più pagine (navbar, footer) e, al crescere della complessità, costruire risposte manipolando e concatenando stringhe diventa rapidamente invasibile.

> [!def] Template engine
> **Software** che genera HTML a partire da **template**, affrontando il problema del riuso delle parti comuni e della crescita della complessità delle pagine.

### Pug

> [!aside]
> 
> > [!def] Pug
> > **Template engine** ad alte prestazioni implementato in JavaScript (port disponibili in molti altri linguaggi), con sintassi **whitespace-sensitive** (simile a Python) per scrivere template HTML, facilmente compilabili in codice HTML.
> 
> ---
> 
> ![[Lezione 15-1792748045067.png|50]]

L'installazione avviene con `npm install pug`; l'uso più semplice richiede il modulo e chiama `pug.renderFile()` sul file del template, che restituisce l'HTML generato:

```js
import pug from "pug";
let html = pug.renderFile("./templates/basic_example.pug");
```

Nella sintassi di Pug l'indentazione esprime l'annidamento degli elementi HTML:

```text
doctype html
html(lang="en")
  head
    title Hello Pug!
  body
    h1(class="foo") First Pug template
    p This is our first Pug template!
```

### Include

Un template può includere altri template con la keyword `include`: è un grande aiuto per il riuso dei template.

```text
//- index.pug
doctype html
html
  include partials/head.pug
  body
    h1 Hello Pug!
    include partials/footer.pug
```

I partial inclusi (es. `partials/head.pug` con `head`, `title`, `script` e `link`; `partials/footer.pug` con il `footer`) vengono inseriti nel punto dell'include nell'HTML finale.

### Ereditarietà dei template

> [!aside]
> Nella progettazione di web application è comune un **layout comune** condiviso da tutte le pagine, che ciascuna pagina può eventualmente ridefinire in alcune parti; Pug supporta questi scenari con l'**ereditarietà dei template**, basata su due keyword:
> 
> - **`block`**: blocco di template che i template figli possono sostituire; può contenere un contenuto di default.
> - **`extends`**: permette a un template di estenderne un altro e sovrascrivere alcuni dei blocchi definiti nel genitore; i blocchi non sovrascritti mostrano il contenuto di default.
> 
> ---
> 
> ![[Lezione 15-1792747711309.png|200]]

```text
//- base-layout.pug
body
  block heading
    h1 Pug Inheritance
  block content
  block footer
    footer This is the default footer.
```

```text
extends ./base-layout.pug
block content
  p The actual content of the homepage.
block footer
  footer This is a specialized footer.
```

Nel secondo template i blocchi `content` e `footer` vengono sovrascritti, mentre `heading` non viene sovrascritto e mostra il valore di default.

### Locali

> [!def] Locali (locals)
> **Oggetto di dati** passato alle funzioni `render()` o `renderFile()` su cui il template può basare il contenuto da renderizzare.

```js
let html = pug.renderFile("./locals.pug", {
  "product": { "name": "Samsung S24", "description": "Smartphone" }
});
```

Il codice contenuto tra `#{` e `}` viene valutato, escapato e inserito nel buffer di output:

```text
h1 #{product.name.toUpperCase()}
p Description: #{product.description}
```

### Condizionali

Spesso i template vengono renderizzati diversamente a seconda di certe condizioni; a questo scopo Pug supporta il familiare costrutto `if`/`else`:

```text
if !user
  a(href="/login") Please, authenticate yourself.
else if user.isAdmin
  p At your command, #{user.name}
else
  p Welcome back, #{user.name}
```

### Iterazioni

Un task comune nell'uso dei template è iterare su sequenze di dati, con `each ... in` e un ramo `else` per la sequenza vuota:

```text
ul
  each item in items
    li #{item.name} - € #{item.price.toFixed(2)}
  else
    li No pizza is available at the moment!
```

### Altri template engine

Pug è solo uno dei tanti template engine disponibili; altri ben noti sono elencati di seguito.

> [!info] Altri template engine
> - **EJS** (ex Jake): sintassi in qualche modo simile a JSP/PHP.
> - **SquirellyJS**, **Nunjucks**, **LiquidJS**, **Eta**.
> - **Haml** (nato per Ruby).

## Parsing del body delle richieste

Gli utenti salvano nuovi elementi riempiendo il form sulla pagina della To-do list, inviato con il metodo `POST` allo stesso URL della pagina:

```text
form(action="/todo" method="POST")
  label(for="todo") To-do Item
  input(type="text" id="todo" name="todo" required)
  button(type="submit") Save To-do
```

Per salvare l'elemento serve leggere il body della richiesta ed estrarne i nomi dei parametri e i loro valori: il body è una stringa nella forma `p1=v1&p2=v2&...` — non banale come potrebbe sembrare.

### Lettura del body

> [!aside]
> Il body potrebbe non essere ancora disponibile quando si processa la richiesta (l'utente ha una connessione lenta o sta caricando file grandi) e diventa disponibile più tardi. L'oggetto richiesta (`http.IncomingMessage`) estende `stream.Readable`: genera un evento **`data`** quando un nuovo chunk di dati diventa disponibile nel body e un evento **`end`** quando non c'è più dati da consumare dallo stream.
> 
> ---
> 
> ![[Lezione 15-1792750126646.png|150]]
> 

La lettura del body va quindi operata in modo asincrono, sfruttando questi due eventi:

```js
function parseRequestBody(request) {
  return new Promise((resolve, reject) => {
    let body = [];
    request
      .on('data', chunk => { body.push(chunk); })
      .on('end', () => {
        body = Buffer.concat(body).toString();
        resolve(parseRequestBodyString(body));
      });
  });
}
```

### Parsing della stringa

Una volta letto il body come stringa, si tratta di dividerla per ricavare i nomi e i valori dei parametri, sostituendo i `+` con spazi e decodificando i valori con `decodeURIComponent`:

```js
function parseRequestBodyString(body) {
  let data = {};
  for (let slice of body.split("&")) {
    let [paramName, paramValue] = slice.split("=");
    paramName = decodeURIComponent(paramName.replace(/\+/g, " "));
    paramValue = decodeURIComponent(paramValue.replace(/\+/g, " "));
    data[paramName] = paramValue;
  }
  return data;
}
```

## Anatomia di una web application tipica

Lo schema riassume l'organizzazione dei componenti di una web application tipica.

![[Lezione 15-1792750068993.png|300]]