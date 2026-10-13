# Lezione 8 JavaScript

## Il linguaggio

> [!def] JavaScript
> **Linguaggio di programmazione** scripting di alto livello, debolmente tipato (loosely-typed). Introdotto dal browser Netscape per rendere dinamici i documenti HTML: i programmi (script) sono interpretati come puro testo dal **JS Engine**. Implementa la specifica **ECMAScript**.

- Oggi è usato anche fuori dalle pagine web: backend, applicazioni desktop e mobile, scripting generico.
- Supporta i paradigmi **imperativo**, **funzionale** e **orientato agli oggetti**, con feature dedicate alla programmazione **asincrona**.
- Le pagine HTML+CSS sono intrinsecamente **statiche**: JavaScript permette al contenuto di cambiare durante la navigazione.

### Includere JavaScript in una pagina

- **JavaScript interno**: codice dentro un elemento `<script>` in `<head>` o `<body>`.
- **JavaScript esterno**: file con estensione `.js` referenziato tramite `<script src="...">`.

```html
<script> console.log("Hello World!"); </script>
<script src="script.js"></script>
```

### Strict mode

- Fino al 2009 (ECMAScript 5) il linguaggio è evoluto senza **breaking changes**; ES5 ne ha introdotti alcuni, disattivati di default per retro-compatibilità.
- Si abilitano con la direttiva `"use strict"` alla prima riga dello script. Nel corso si usa sempre la versione moderna «strict».

```javascript
"use strict";
/* JavaScript code here */
```

## Sintassi di base

- Un programma è una **sequenza di statement**, composti da valori, operatori, espressioni, keyword e commenti.
- La sintassi è simile a Java e C ma più permissiva; gli statement sono delimitati da newline e/o **punto e virgola** (uso preferito come buona pratica).
- Con `typeof` si ispeziona il tipo di un valore: `undefined`, `number`, `string`, `boolean`.

### Operatori

| Operatore | Descrizione |
|---|---|
| `=` | Assegnamento |
| `+` `-` `*` `/` | Somma, sottrazione, moltiplicazione, divisione |
| `**` | Elevamento a potenza (da ECMAScript 2016) |
| `%` | Modulo (resto della divisione) |
| `++` `--` | Incremento, decremento |

| Operatore         | Descrizione                                       |
| ----------------- | ------------------------------------------------- |
| `==`              | uguaglianza debole (con conversione di tipo)      |
| `===`             | uguaglianza stretta (stesso valore e stesso tipo) |
| `!=`              | diverso (debole)                                  |
| `!==`             | diverso valore o diverso tipo                     |
| `>` `<` `>=` `<=` | confronti                                         |
| `?`               | operatore ternario                                |

> [!info] Uguaglianza debole vs stretta
> - **`==`** converte gli operandi di tipo diverso prima di confrontarli: `"1" == 1` e `true == "1"` sono `true`.
> - **`===`** non converte: se i tipi differiscono restituisce subito `false` (`"1" === 1` è `false`).

### Controllo di flusso

`if`, `if-else`, `for`, `while`, `do-while` e `switch` hanno stessa sintassi e semantica di Java; anche `continue` e `break` funzionano allo stesso modo.

## Variabili e scope

### Ciclo di vita

- **Dichiarazione**: il nome della variabile è legato allo scope corrente.
- **Inizializzazione**: alla variabile viene assegnato un valore (di default `undefined`).
- **Uso**: la variabile può essere referenziata.

> [!def] Temporal Dead Zone (TDZ)
> Intervallo tra la dichiarazione e l'inizializzazione in cui la variabile è **inaccessibile**: referenziarla solleva un `ReferenceError`.

### Dichiarazione

- **`let`**: variabili «standard», con **scope a livello di blocco** (il blocco `{} più vicino`).
- **`const`**: costanti con scope di blocco; non possono essere riassegnate ( tentativo → `TypeError`).
- Le variabili sono accessibili solo dopo l'esecuzione della riga in cui sono dichiarate; nello stesso blocco non si può ridichiarare lo stesso nome.

```javascript
let bool;
bool = true;
if (bool) {
    let msg = "Hello"; // visibile solo dentro il blocco
    console.log(msg);
}
```

- Una variabile dichiarata in un blocco interno **oscura** (shadowing) l'omonima dello scope esterno.

### Hoisting

> [!def] Hoisting
> Comportamento predefinito per cui le dichiarazioni di variabili (e funzioni) sono implicitamente spostate all'inizio del loro scope. Con `let`/`const` è sollevata solo la **dichiarazione**, non l'inizializzazione, che avviene alla riga originaria: l'uso precedente cade nella TDZ.

```javascript
{
    console.log(x); // ReferenceError: can't access 'x' before initialization
    let x = 1;
}
```

### `var` e dichiarazione implicita (pre-ECMAScript 6)

> [!warning] `var` è deprecato
> - **`var`** ha scope di funzione/globale (nessuno scope di blocco) ed è hoistato **con inizializzazione a `undefined`**: usare la variabile prima della riga di dichiarazione stampa `undefined` invece di un errore, e la variabile resta visibile fuori dal blocco.
> - **Dichiarazione implicita** (assegnamento senza keyword): crea una **variabile globale**, pratica error-prone, vietata in strict mode (`ReferenceError`).

```javascript
if (true) {
    console.log(n); // undefined (non errore!)
    var n = 1;
}
console.log(n); // 1
```

## Scope

- **Scope globale**, **scope di funzione**, **scope di modulo**; le variabili `let`/`const` aggiungono lo **scope di blocco**.

## Funzioni

```javascript
function greet(name, message = "Hello") {
    console.log(`${message} ${name}`);
}
```

- La **dichiarazione di funzione** vale nello scope in cui avviene; le dichiarazioni di funzione sono **hoistate** e quindi richiamabili prima della riga che le definisce.
- Se un argomento non è passato, il parametro è `undefined`; i parametri possono avere **valori di default**.
- I **template literals** (backtick) permettono l'interpolazione `${...}`.

### Scope interno e visibilità

- Una funzione crea il proprio scope: le variabili e funzioni dichiarate al suo interno non sono visibili all'esterno.
- Una funzione può accedere alle variabili degli scope esterni (**closure**), purché non mascherate nel proprio scope.

### Function expressions

- Le funzioni sono **valori**: possono essere assegnate a variabili (**function expression**), anche con sintassi **arrow function**.
- Si applicano le regole di hoisting delle variabili: la funzione non è usabile prima della riga di assegnazione (TDZ), a differenza delle dichiarazioni.

```javascript
let greet = function(name) { console.log(`Hello ${name}!`); };
let salute = (name) => { console.log(`Howdy ${name}!`); };
```

### Funzioni annidate e closure

> [!def] Funzione annidata
> Funzione creata dentro un'altra funzione. Può essere **restituita** e usata fuori dalla funzione originaria e, ovunque venga usata, conserva l'accesso al contesto esterno (**closure**) della funzione che l'ha creata.

```javascript
function getGreeter(message) {
    let sep = ",";
    return function(name) {
        console.log(`${message}${sep} ${name}!`);
    }
}
let helloGreeter = getGreeter("Hello"); // "cattura" message e sep
```

## Oggetti

> [!def] Oggetto
> Contenitore di dati **chiave: valore**. Si crea con la sintassi **object constructor** (`new Object()`) o, più comunemente, **object literal** (`{}`). Una **proprietà** ha una chiave (nome) prima di `:` e un valore a destra; le proprietà sono separate da virgole.

### Proprietà

- **Accesso con dot notation**: `pet.name`; proprietà inesistente → `undefined`.
- **Aggiunta/cancellazione**: `pet.nickname = "..."` aggiunge, `delete pet.age` rimuove.
- **Square brackets notation**: necessaria per chiavi con spazi o espressioni: `dog["is a good boy"]`, `dog["is the " + "best boy"] = true`.

### Riferimenti

- Una variabile assegnata a un oggetto memorizza un **riferimento**, non l'oggetto: due variabili che puntano allo stesso oggetto sono uguali sia con `==` che con `===` (condividono lo stesso valore di riferimento).

### Cloning

- **Copia per riferimento**: assegnare un oggetto a un'altra variabile non copia nulla; le modifiche sono visibili da entrambe le variabili.
- **Shallow clone**: copia proprietà per proprietà (es. con un ciclo `for...in`); gli oggetti annidati restano **condivisi** (modificare `copy.owner.name` modifica anche l'originale).
- **Deep clone**: richiede **ricorsione** — se il valore di una proprietà è un oggetto, si clona ricorsivamente.
- Alternative built-in: `Object.assign()` (shallow), `structuredClone()` (deep).

```javascript
function clone(object) {
    let copy = {};
    for (let key in object) {
        copy[key] = (typeof object[key] === "object") ? clone(object[key]) : object[key];
    }
    return copy;
}
```

### Metodi

- Una proprietà il cui valore è una funzione è un **metodo**; definibili in assegnamento, con sintassi classica `greet: function() {...}` o **shorthand** `greet() {...}`.

### `this`

> [!def] `this`
> Riferimento valutato **a run-time** in base al contesto: dentro un metodo, punta all'oggetto che contiene il metodo, permettendogli di accedere alle altre proprietà dello stesso oggetto.

```javascript
let john = { name: "John", greet() { console.log(`Hi, I'm ${this.name}!`); } };
```

- La stessa funzione assegnata come metodo a oggetti diversi vede ogni volta l'oggetto chiamante tramite `this`.
- **Le arrow function non hanno `this`**: il `this` al loro interno è preso dal contesto esterno, quindi non riflette l'oggetto chiamante.

### Costruttori

> [!def] Funzione costruttore
> Funzione regolare invocata con la keyword **`new`** per creare molti oggetti simili. Convenzioni: nome con iniziale maiuscola e invocazione solo con `new`.

Quando una funzione è eseguita con `new`: 1) si crea un nuovo oggetto vuoto assegnato a `this`; 2) viene eseguito il corpo, che tipicamente modifica `this`; 3) `this` è restituito.

```javascript
function Pet(name, species) {
    this.name = name;
    this.species = species;
}
let rick = new Pet("Richard", "Lizard");
```

### Optional chaining

- Accedere una proprietà di una proprietà `undefined` solleva un errore; l'operatore **`?.`** «cortocircuita»: se la parte sinistra è `undefined` restituisce subito `undefined` invece di un errore.
- Sostituisce il controllo esplicito `pet.owner ? pet.owner.name : undefined`.
- Varianti: **`?.()`** per chiamare una funzione che potrebbe non esistere (`mike.greet?.()` → `undefined`), **`?.[chiave]`** con la notazione a parentesi.

### Configurazione delle proprietà

- Ogni proprietà ha tre **flag**: **Writable** (il valore può cambiare), **Enumerable** (la proprietà compare nei cicli), **Configurable** (la proprietà può essere cancellata e i flag modificati).
- Con la creazione «tradizionale» tutti i flag sono `true`; con `Object.defineProperty(obj, key, { value, writable, enumerable, configurable })` si configurano esplicitamente (es. proprietà read-only → `TypeError` alla riassegnazione o alla cancellazione se non configurabile).

### Getter e setter

> [!info] Proprietà dati vs accessorie
> - **Proprietà dati**: memorizzano un valore.
> - **Proprietà accessorie**: funzioni eseguite quando la proprietà è letta (**getter**, keyword `get`) o assegnata (**setter**, keyword `set`).

```javascript
let p = {
    first: "John", last: "Smith",
    get fullName() { return `${this.first} ${this.last}`; },
    set fullName(name) { [this.first, this.last] = name.split(" "); }
};
p.fullName; // si accede come proprietà, senza ()
```

- Getter e setter si usano **come proprietà** (senza `()`): dall'esterno non c'è differenza tra proprietà dati e accessorie.
