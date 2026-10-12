# Lezione 10 JavaScript in a Browser Environment

## L'ambiente browser

### Host environment

- JavaScript può girare in diversi **host environment** (ambienti host): **browser web** (per cui è stato originariamente creato) e **web server** (es. tramite il runtime **Node.js**).
- Ogni host environment fornisce i propri **oggetti** e **funzioni**, in aggiunta a quelli inclusi nel **core del linguaggio**.

![[b3bd56a960dc06c510972ebcd9623350bda01e6e7a63b8351d4f84b7a922ed34.png|400]]

### window

- L'ambiente browser ha un oggetto «radice» chiamato **`window`**, che è l'**oggetto globale** del codice JavaScript.
- `window` rappresenta la finestra del browser e fornisce **metodi per controllarla**.
- Le funzioni e le variabili globali sono **proprietà di `window`**.

```js
let msg = "Hello";
function greet(name) { console.log(`${msg}, ${name}!`); }

greet("Web Technologies");     // richiamata come funzione globale
window.greet("window object"); // la stessa funzione, come proprietà di window
```

### DOM

> [!def] DOM (Document Object Model)
> Rappresenta il **contenuto del documento corrente**. L'oggetto **`document`** è il punto d'ingresso principale alla pagina web e fornisce modi per **accedere** e **manipolare** i contenuti.

### BOM

> [!def] BOM (Browser Object Model)
> Insieme di oggetti aggiuntivi forniti dal browser per lavorare **sul browser stesso**, non sui contenuti del documento.

- **`location`**: contiene informazioni sull'URL del documento corrente (`location.href`).
- **`screen`**: informazioni sul display usato dall'utente (`screen.availWidth`).
- **`navigator`**: dettagli aggiuntivi su browser e piattaforma (`navigator.userAgent`).
- **`history`**: rappresenta la cronologia di navigazione (`history.back()`, come il pulsante «back» del browser).

## Il DOM

### Struttura ad albero

- Un documento HTML può essere visto come un **albero** (con discendenti, figli, fratelli): il **DOM formalizza** questa intuizione.
- Ogni **tag HTML è un oggetto** nel DOM.
- I tag annidati sono **figli** del tag che li racchiude.
- Il contenuto testuale di un tag è un oggetto (`#text`) a sua volta **figlio del tag**.
- Gli **attributi** di un tag sono accessibili come **proprietà** dell'oggetto corrispondente.
- Il DOM reale include anche **spazi e a-capo** tra i tag come nodi `#text`; nelle rappresentazioni si omettono per brevità.

![[1a98e0c713a936e079235c32b6ec8108f789ce453c2a90aab1f8ea4e7ebcf7d6.png|300]]

- I **commenti HTML** non sono mostrati dal browser, ma vengono comunque analizzati e aggiunti al DOM come speciali **nodi commento**.

### Tipi di nodo

- La specifica DOM definisce **12 tipi di nodo**; tipicamente se ne usano quattro:
- **Document node**: è la radice e il punto d'ingresso del DOM.
- **Element node**: rappresentano gli elementi HTML.
- **Text node**: rappresentano il contenuto testuale.
- **Comment node**: rappresentano i commenti.

### Trovare elementi

- L'oggetto `document` fornisce diversi **metodi per selezionare elementi** da un documento HTML.
- **`querySelector`** e **`querySelectorAll`** sono i più versatili: ricevono in input un **selettore CSS**; il primo restituisce solo il primo elemento corrispondente, il secondo la lista completa.
- Tutti i metodi restituiscono **`null`** quando non trovano elementi.

```js
document.getElementById("a");            // elemento per attributo id
document.getElementsByClassName("foo");  // HTMLCollection
document.getElementsByName("c");        // NodeList
document.querySelector("ul > li");       // primo <li> che corrisponde
document.querySelectorAll("ul > li");    // tutti i <li> che corrispondono
```

> [!def] HTMLCollection («live collection»)
> Tutti i metodi della famiglia **`getElementsBy*`** restituiscono una **HTMLCollection**: una collezione aggiornata automaticamente, che riflette sempre lo stato corrente del documento.

```js
let links = document.getElementsByTagName("a"); // HTMLCollection (1)
// ...il documento viene esteso con altri <a>...
console.log(links); // HTMLCollection (3): la collezione si è aggiornata da sola
```

- Invocati su `document`, i metodi di ricerca cercano nell'**intero documento**; se gli elementi cercati sono discendenti di un altro elemento, è più efficiente invocare i metodi di ricerca **sull'elemento antenato**.

```js
let sidebar = document.querySelector(".sidebar");
let links = sidebar.querySelectorAll("a"); // cerca solo dentro sidebar
```

| Metodo | Cerca per... | Chiamabile sugli elementi? | Restituisce live collection? |
| --- | --- | --- | --- |
| `querySelector` | selettore CSS | ✓ | – |
| `querySelectorAll` | selettore CSS | ✓ | – |
| `getElementById` | attributo `id` | – | – |
| `getElementsByName` | attributo `name` | – | ✓ |
| `getElementsByTagName` | nome del tag o `*` | ✓ | ✓ |
| `getElementsByClassName` | attributo `class` | ✓ | ✓ |

### Navigare nel DOM

- Gli elementi più in alto (`html`, `head`, `body`) sono disponibili anche come **proprietà di `document`**.
- I nodi del DOM contengono riferimenti a **padre, fratelli e figli**: `parentNode`, `previousSibling` / `nextSibling`, `firstChild` / `lastChild`, `childNodes`.
- Questi riferimenti sono **di sola lettura**.

![[6078ffb9e70ced9fdf91bbb23154ad61b67f3ff89efd2032852659242aeeb09b.png|400]]

### Navigazione solo elementi

- Per ignorare i nodi di testo e commento si usano le proprietà che considerano **solo i DOM element**: `parentElement`, `children`, `firstElementChild` / `lastElementChild`, `previousElementSibling` / `nextElementSibling`.

![[6592253cfd7810b3705f9a83a732b605c8a5b50eb1db7052a3588af0b6acd109.png|400]]

```html
<main><h1>Hello DOM!</h1><!-- comment --><p>DOM is <em>FUN</em>!</p></main>
<script>
  document.querySelector("main").childNodes; // [#text, h1, #text, #comment, #text, p, #text]
  document.querySelector("main").children;   // HTMLCollection { h1, p }
</script>
```

### Gerarchia delle classi dei nodi

- I nodi del DOM appartengono a una **gerarchia di classi**: da `EventTarget` deriva `Node`, da cui derivano `Document`, `Element` e `CharacterData` (con `Text` e `Comment`); da `HTMLElement` derivano le classi specifiche di ogni tag (`HTMLInputElement`, `HTMLAnchorElement`, …).

![[96f290c4a658794738d6fedf742e054c67fb10fc9214c17312c4c6eaf51e105a.png|400]]

### Proprietà dei nodi

#### `nodeName` / `tagName`

- **`nodeName`** e **`tagName`** danno informazioni sul **tipo di nodo** e sono di **sola lettura**: valgono `#text` e `#comment` per nodi di testo e commento, il nome del tag per gli elementi (`tagName` è `undefined` sui non-elementi).

```js
let body = document.body;
body.firstChild.nodeName;         // "#text"
body.firstChild.tagName;          // undefined (non è un elemento)
body.childNodes[3].nodeName;      // "#comment"
body.firstElementChild.tagName;   // "H1"
```

#### Attributi come proprietà

- Gli attributi **standard** vengono analizzati e resi disponibili come **proprietà** dell'elemento corrispondente; gli attributi non standard non lo sono (per quelli si usa `getAttribute`).

```js
// <input id="x" class="inp ok" name="field" custom="y">
let i = document.body.firstElementChild;
i.id;                     // "x" — attributo standard
i.classList;               // DOMTokenList ["inp", "ok"]
i.custom;                  // undefined — non è un attributo standard
i.getAttribute("custom");  // "y"
```

- Queste proprietà sono anche **scrivibili**:

```js
i.id = "w";
i.classList.remove("ok"); i.classList.add("err");
i.setAttribute("custom", "k");
i.removeAttribute("name");
// → <input id="w" class="inp err" custom="k">
```

#### `innerHTML` / `outerHTML`

- **`innerHTML`** restituisce il codice HTML **contenuto** in un elemento; **`outerHTML`** il codice HTML dell'**intero elemento**.
- Sono entrambi **scrivibili**: assegnare loro un valore cambia la pagina — `innerHTML` cambia il contenuto, `outerHTML` sostituisce l'elemento.

```js
let h1 = document.querySelector("h1"); // <h1 id="h">Hello <em>DOM!</em></h1>
h1.innerHTML; // "Hello <em>DOM!</em>"
h1.outerHTML; // "<h1 id=\"h\">Hello <em>DOM!</em></h1>"

h1.innerHTML = "DOM: <em>Wow!</em>";      // nuovo contenuto dell'elemento
h1.outerHTML = `<p>${h1.innerHTML}</p>`;  // l'<h1> diventa un <p>, stesso contenuto
```

## Manipolare il DOM

- Non ci si limita a modificare gli elementi esistenti (es. cambiandone gli attributi): si possono **creare** nuovi elementi e **rimuovere** quelli esistenti, cambiando la **struttura del DOM**.
- L'aggiornamento dinamico del DOM è la chiave per pagine web reattive, «vive».

### Creare nuovi elementi

- `document.createElement(tag)` crea un nuovo elemento; `document.createTextNode(value)` crea un nuovo nodo `#text`.
- I nodi appena creati **non sono ancora nel DOM**: vanno inseriti con i metodi di inserimento.

```js
let heading = document.createElement("h1");  // nuovo <h1>, non ancora nel DOM
let title = document.createTextNode("Wow!"); // nuovo #text, non ancora nel DOM
heading.append(title);          // #text come figlio dell'<h1>
document.body.prepend(heading); // <h1> (con il suo figlio) in cima al <body>
```

![[bdcdcb9aa018132a5b4f21536075ca04221c0f358e0cc2ec90186676b5b36bb7.png|300]]

### Metodi di inserimento

![[e084e9cb13fb1a243cf8ce78c2639137e9f48629f62f2a9526894ef2ab786aab.png|300]]

| Metodo | Descrizione |
| --- | --- |
| `document.createElement(tag)` | crea un elemento con il tag indicato |
| `document.createTextNode(value)` | crea un nodo di testo (raramente usato) |
| `elem.cloneNode(deep)` | clona l'elemento; se `deep == true` con tutti i discendenti |
| `node.append(...nodi o stringhe)` | inserisce dentro il nodo, alla fine |
| `node.prepend(...nodi o stringhe)` | inserisce dentro il nodo, all'inizio |
| `node.before(...nodi o stringhe)` | inserisce subito prima del nodo |
| `node.after(...nodi o stringhe)` | inserisce subito dopo il nodo |
| `node.replaceWith(...nodi o stringhe)` | sostituisce il nodo |
| `node.remove()` | rimuove il nodo |

### Interagire con l'utente

- **`alert`**, **`prompt`** e **`confirm`** sono modi utili per interagire con l'utente in un browser.
- `alert(message)` mostra un messaggio; `confirm(question)` restituisce `true`/`false`; `prompt(question)` restituisce la stringa inserita dall'utente.

```js
alert("This page will ask for your input");
if (confirm("Do you want to continue?") === true) {
  let name = prompt("State your name:");
} else {
  console.log("user cancelled");
}
```

## Eventi

### Definizione e classificazione

> [!def] Evento
> Un **evento** è un segnale che indica che è successo qualcosa.

- **Comportamento dell'utente**: click, pressioni di tasti sulla tastiera, movimenti del mouse.
- **Form**: invio (submission), focus (o perdita di focus) su un campo di input.
- **Eventi del documento**: documento o elementi caricati, richieste di rete completate.

| Categoria | Evento | Significato |
| --- | --- | --- |
| Mouse | `click` | l'utente clicca (tap su dispositivi touchscreen) su un elemento |
| | `contextMenu` | clic destro del mouse su un elemento |
| | `mouseover` / `mouseout` | il cursore entra in / esce da un elemento |
| | `mousedown` / `mouseup` | il pulsante principale del mouse è premuto / rilasciato su un elemento |
| | `mousemove` | il cursore del mouse si muove |
| Keyboard | `keydown` / `keyup` | un tasto della tastiera è premuto / rilasciato |
| Forms | `submit` | l'utente invia un form |
| | `focus` | l'utente dà focus a un elemento (es. `<input>`) |
| Document | `DOMContentLoaded` | l'HTML è stato analizzato, il DOM è completamente costruito |
| Window | `load` | la pagina è stata completamente caricata e renderizzata |

### Handler

- Per reagire agli eventi si definiscono **handler**: funzioni eseguite quando un evento scatta.
- Il modo più semplice per definirli sono gli **attributi HTML `on<evento>`**, il cui valore è il codice JavaScript da eseguire.

```html
<input type="button" value="Click me" onclick="handleClick();">
```

- Gli handler si possono anche definire **dinamicamente** via JavaScript: assegnando la **proprietà `on<evento>`** dell'elemento, oppure con il metodo **`addEventListener`**.
- Assegnare la proprietà `on<evento>` **sovrascrive** l'handler definito tramite attributo HTML; `addEventListener` invece **aggiunge** un nuovo handler.

```js
input.onclick = () => console.log("Tap");     // sovrascrive l'handler da attributo
input.addEventListener("click", handleClick); // aggiunge una nuova funzione handler
```

### `this` negli handler

- Dentro un event handler, **`this`** vale l'elemento a cui l'handler invocato è **assegnato**.

```js
function handleClick(){ console.log(this.outerHTML); }
// assegnato all'<input>: stampa l'<input>; assegnato al <p>: stampa il <p>
```

### L'oggetto event

- Tutti i dettagli dell'evento sono forniti da un **oggetto event**, passato agli handler.
- Ogni tipo di evento ha le sue **proprietà**: es. gli eventi legati alla tastiera hanno la proprietà **`key`** con il tasto premuto.

```js
function handler(event){ console.log(`You pressed ${event.key}`); }
document.querySelector("input").addEventListener("keyup", handler);
```

### Event bubbling

> [!def] Event bubbling
> Quando un evento scatta su un elemento, prima vengono eseguiti tutti gli handler registrati **su quell'elemento**, poi quelli del **padre**, e così via risalendo tutti gli antenati fino al **nodo radice** del DOM.

- Il meccanismo si applica alla **maggior parte** degli eventi, ma non a tutti: gli eventi **`focus`** non fanno bubbling.
- Un evento in bubbling si propaga fino all'oggetto globale **`window`**.

```html
<section onclick="console.log('section');">
  <article onclick="console.log('article');">
    <p onclick="console.log('p');">Bubbling</p>
  </article>
</section>
<!-- output in console dopo un click su <p>: p, article, section, document -->
```

### Event delegation

> [!info] Event delegation
> Se molti elementi possono generare eventi simili, invece di assegnare un handler a ciascuno se ne usa **uno solo sul loro antenato comune**: gli elementi **delegano** la gestione dell'evento a un antenato.

- La proprietà **`target`** dell'oggetto event permette di determinare **su quale elemento** l'evento è stato generato.

```html
<table onclick="handler(event);"><!-- ...righe con celle <td>... --></table>
<script>
  function handler(event){
    if (event.target.nodeName === "TD") {  // gestisce solo le celle
      let oldValue = parseInt(event.target.innerHTML);
      event.target.innerHTML = ++oldValue;
    }
  }
</script>
```

### Fermare il bubbling

- Un handler può decidere che l'evento è stato **completamente processato** e non va propagato oltre: il bubbling si ferma invocando **`stopPropagation()`** sull'oggetto event.

> [!warning] Regola pratica
> Non fermare la propagazione senza un buon motivo: in futuro potrebbe servire catturare l'evento su un antenato.

```js
function handler(event){
  console.log(this.tagName);
  event.stopPropagation();
}
```

### Generare eventi (dispatching)

- Da JavaScript è possibile **generare eventi**: con il costruttore `new Event(...)` e il metodo **`dispatchEvent`**.

> [!info] `isTrusted`
> La proprietà **`isTrusted`** dell'evento vale **`false`** per gli eventi «artificiali» generati via JavaScript.

```js
let click = new Event("click");
input.dispatchEvent(click); // isTrusted === false per gli eventi generati via JS
```

### Capturing

- Esiste un'altra fase di elaborazione dell'evento, il **capturing**, che procede «verso il basso» fino all'elemento target.
- L'elaborazione di un evento ha tecnicamente **tre fasi**: 1. capturing, 2. target, 3. bubbling.
- Per registrare listener nella fase di capturing: `elem.addEventListener(..., {capture: true});`

![[12a2031a63c396958532c1c37f952fbcf42131c561da6a32a53905549822d001.png|300]]

## Ordine di esecuzione degli script

- Man mano che gli script diventano complessi, interagiscono con il DOM e generano dinamicamente handler, serve conoscere **come viene eseguito il codice JavaScript** al caricamento di una pagina.
- **Default**: gli script vengono scaricati ed eseguiti **nell'ordine in cui compaiono**, mentre il parsing della pagina è **in pausa**.
- **`defer`**: gli script esterni vengono scaricati **in parallelo** ed eseguiti **dopo** che la pagina ha finito di essere analizzata.
- **`async`**: gli script esterni vengono scaricati in parallelo ed eseguiti **appena scaricati**.
- Gli script **module** sono `defer` di default e possono essere dichiarati `async`.

![[8f8725551de9c1f10607e23a9878d514304e42171e0aec9fb95cf5657dcd5069.png|400]]

- L'ordine di esecuzione **conta**: uno script nel `<head>` senza attributi viene eseguito prima che il `<body>` esista, quindi `document.body` è `null` (TypeError).

| Script nel `<head>` che accede a un elemento del `<body>` | Esito |
| --- | --- |
| `<script src="load.js">` | eseguito subito: `document.body` è `null` → TypeError |
| `<script defer src="load.js">` | eseguito a parsing concluso: il DOM è pronto ✓ |
| `<script async src="load.js">` | non prevedibile: dipende dal tempo di scaricamento |
| handler di `DOMContentLoaded` | eseguito quando il DOM è completamente costruito ✓ |

```js
document.addEventListener("DOMContentLoaded", () => {
  let h1 = document.body.querySelector("h1"); // ora il body esiste
  console.log(h1.innerHTML);
});
```