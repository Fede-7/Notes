# Lezione 18 Single Page Applications

## App multi-page

Nelle web app tradizionali le pagine sono generate dinamicamente sul server e inviate al browser per la renderizzazione: una volta arrivate, sono intrinsecamente statiche.

Quando l'utente cambia pagina (es. clicca su un link) accade quanto segue:

- Una **nuova richiesta** viene inviata al server.
- La **nuova pagina** è restituita in risposta e visualizzata dal browser.

Questo è l'approccio **multi-page**: ogni navigazione provoca un **full-reload** della pagina.

> [!def] Single Page Application (SPA)
> **Applicazione web** che reagisce all'input dell'utente aggiornando dinamicamente il contenuto della pagina corrente, invece di caricare una nuova pagina dal server.

Le caratteristiche chiave di una SPA:

- L'intera applicazione è caricata nella **richiesta iniziale**; la pagina non viene mai ricaricata completamente.
- La complessità del rendering delle viste passa dal server al codice client-side (da *thin client* a *thick client*).
- Sono applicazioni ad alta densità di JavaScript.
- La navigazione a una vista diversa **non** provoca il full-reload: i dati necessari vengono recuperati da un backend (es. REST) e il JavaScript lato client crea dinamicamente la nuova pagina.

### Perché le SPA

Le SPA offrono alcuni vantaggi sulle app multi-page tradizionali:

- **Esperienza utente più dinamica**, simile alle app desktop.
- Il caricamento iniziale è più lento (serve scaricare tutta l'app), ma i successivi sono molto più veloci.
- **Carico del server ridotto**: si recuperano solo i dati necessari e solo quando servono, senza trasferire continuamente interi documenti HTML, con risparmi anche di banda.

## Client-side routing

> [!def] Client-side routing
> **Pratica** con cui, in una SPA, la navigazione e l'aggiornamento delle viste sono gestiti interamente lato client, senza ricaricare la pagina dal server.

Le diverse "pagine" di una SPA sono dette **viste**. Il client-side routing comporta:

- Aggiornare l'URL del browser.
- Caricare e renderizzare il contenuto (vista) appropriato nella pagina.
- Interagire con la **Browser History API**, così che i pulsanti indietro e avanti funzionino come in qualunque app multi-page.

I componenti chiave del client-side routing sono tre:

- **Router**: modulo che gestisce la mappatura tra URL e viste.
- **View rendering**: meccanismo per renderizzare le viste diverse.
- **History management**: meccanismo che usa la History API per manipolare la cronologia di navigazione del browser.

### Anatomia di una SPA minimale

C'è un **singolo documento HTML**, senza alcun contenuto: solo un `<div id="app">` vuoto e lo script principale caricato come modulo. Il grosso del lavoro avviene nel client-side JavaScript.

Il file principale costruisce tre elementi nel contenitore: una navbar e un footer, che non cambiano al variare della vista, e un contenitore `main` per il contenuto, che cambia.

Le rotte associano le viste ai path URL; ciascuna rotta è indicizzata per path e ha due proprietà: `title` (il titolo della pagina quando quella vista è caricata) e `render` (una funzione che ritorna la stringa HTML della vista):

```js
const routes = {
  "/":       { title: "Home", render: home },
  "/about":  { title: "About", render: about },
};
```

La funzione `router()` implementa la logica di routing:

```js
function router() {
  let view = routes[location.pathname];
  if (view) {
    document.title = view.title;
    content.innerHTML = view.render();
  } else {
    history.replaceState("", "", "/");
    router();
  }
}
```

Se una rotta combacia col path corrente, aggiorna il titolo e sostituisce il contenuto col risultato della `render` della vista; altrimenti sostituisce la voce di cronologia corrente con il path `/` e richiama se stessa.

### Gestione della navigazione

In una SPA possono esserci link che devono comportarsi normalmente (es. verso siti esterni) e link che devono solo aggiornare la vista; questi ultimi si marcano con un **attributo custom**, es. `data-link`, e si gestiscono con un listener globale:

```js
window.addEventListener("click", e => {
  if (e.target.matches("[data-link]")) {
    e.preventDefault();               // no full-reload
    history.pushState("", "", e.target.href);
    router();
  }
});
```

Il click su un link interno viene intercettato: si previene il comportamento di default, si aggiunge il nuovo stato sulla pila della cronologia con `pushState`, e si invoca `router()` per aggiornare la vista secondo l'URL corrente.

Infine, `router()` va eseguita anche in due occasioni:

- **`popstate`**: quando l'utente preme il pulsante indietro del browser.
- **`DOMContentLoaded`**: quando la pagina principale viene (ri)caricata completamente.

## Componenti

Man mano che la complessità del frontend cresce, gestire intere viste come monoliti diventa rapidamente infeasibile: la codebase diventa difficile da mantenere ed è complicato riusare pezzi di funzionalità in viste diverse.

La soluzione è **decomporre la UI in componenti modulari**; ogni componente incapsula una funzionalità specifica, è il solo responsabile del proprio HTML e del proprio stato interno, e le viste che lo usano non si preoccupano di questi dettagli.

> [!def] Componente
> **Unità modulare della UI** che racchiude una specifica funzionalità, riusabile in più parti dell'applicazione.

Le caratteristiche chiave di un componente sono:

- **Modularità**: è autonomo e incapsula un pezzo specifico di funzionalità.
- **Encapsulation**: racchiude la propria business logic, il proprio stato, layout e stili.
- **Riuso**: è progettato per essere riusato in parti diverse dell'app.

I componenti hanno un ruolo centrale in tutti i framework frontend. Con i **custom elements** se ne può creare uno da zero estendendo `HTMLElement` e registrandolo:

```js
class Counter extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = "<button>Click</button>";
    this.querySelector("button").onclick = () => { /* ... */ };
  }
}
customElements.define("click-counter", Counter);
```

Una vista usa il componente semplicemente includendo il suo tag, es. `<click-counter></click-counter>`, dopo averne importato il codice.

## Recupero dei dati: AJAX e XMLHttpRequest

Prima dell'introduzione della Fetch API in ES6, le richieste di rete si effettuavano con **AJAX**, acronimo di *Asynchronous JavaScript And XML*, implementato tramite l'interfaccia **XMLHttpRequest**.

> [!info] XMLHttpRequest oggi
> La Fetch API lo sta sostituendo, ma `XMLHttpRequest` è ancora comune e si trova in molti pacchetti esistenti.

Il workflow tipico era:

- Creare un oggetto `XMLHttpRequest`.
- Impostare una **callback** da eseguire quando la richiesta è completata.
- Inizializzare la richiesta con `open` (metodo HTTP, URL, flag asincrono).
- Inviare la richiesta con `send`.

```js
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) { /* uso della risposta */ }
};
xhttp.open("GET", "/url/to/fetch", true);
xhttp.send();
```

## Le sfide delle SPA e i framework

Implementare una SPA da zero è istruttivo, ma fa emergere alcune difficoltà:

- **State management**: tenere stato e UI sempre aggiornati, e riflettere correttamente le viste dopo ogni cambiamento di stato.
- **DOM manipulation**: l'API `document` richiede molto codice boilerplate.
- **Client-side routing**: un router fatto a mano è basilare; servirebbero rotte parametriche, redirect, …
- **Efficient rendering**: si ridisegna tutta la lista a ogni cambiamento, senza ottimizzazioni.

I **framework frontend** come Angular, React, Vue.js, Ember e Svelte forniscono soluzioni pronte per queste sfide e, in genere, anche supporto di tooling (generazione di boilerplate, automazione di build e deploy) e un modo "standardizzato" di costruire i frontend, che facilita il passaggio di uno sviluppatore tra progetti che usano lo stesso framework.