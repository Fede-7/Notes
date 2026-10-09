# Lezione 9 JavaScript

## Prototipi ed ereditarietà

### Il prototype

> [!def] Ereditarietà prototipale
> Ogni oggetto possiede una proprietà nascosta **`[[Prototype]]`**, che è `null` oppure riferimento a un altro oggetto. Quando si accede a una proprietà mancante, JavaScript la cerca risalendo la **catena dei prototipi**.

- **`__proto__`** è un getter/setter per la proprietà `[[Prototype]]`; in JavaScript moderno si preferiscono `Object.getPrototypeOf()` e `Object.setPrototypeOf()`.
- I prototipi sono usati **solo in lettura**: le operazioni di **scrittura e cancellazione** agiscono direttamente sull'oggetto, non sul prototipo.

```js
let pet = { legs: 4 };
let cat = { name: "Garfield" };
Object.setPrototypeOf(cat, pet);
cat.legs;      // 4 (dalla catena)
snake.legs = 0; // snake ora ha una proprietà propria legs
```

![[63e6435241b609648e2d8921fb37a65a1df6c2c1c50a3380f88a9efc2bef20d7.png|100]]

### Costruttori e prototype

- Con una **funzione costruttore** invocata con `new`, l'operatore usa `Constructor.prototype` per impostare il `[[Prototype]]` del nuovo oggetto.
- Se il costruttore non ha una proprietà `prototype`, viene usato un **prototipo di default**: un oggetto con la proprietà `constructor` che punta alla funzione costruttore stessa (`Pet.prototype = { constructor: Pet }`).
- Questo meccanismo consente di risalire al costruttore tramite `obj.constructor`.

```js
function Duck(name) { this.name = name; }
Duck.prototype = { eats: true };
let chuck = new Duck("Chuck");
chuck.eats; // true, via prototype
```

![[6231d67170fe703e4a425ba5746519e2153bd1e667d4a4c681a9f72200cd5407.png|400]]

### Metodi: due alternative

Esistono due modi per dotare di metodi gli oggetti creati da un costruttore:

- Assegnare il metodo a `this` dentro il costruttore: ogni oggetto ha una **copia propria** del metodo.
- Assegnarlo a `Constructor.prototype`: il metodo è **condiviso** da tutti gli oggetti tramite la catena dei prototipi.

```js
Pet.prototype.describe = describe; // metodo condiviso sul prototype
```

## Strutture dati

### Array

- Un **array** memorizza una sequenza ordinata di valori, dichiarabile con la sintassi letterale `[...]` o con il costruttore `new Array(...)`.
- Gli array sono **indicizzati da 0**; l'accesso in lettura/scrittura usa la notazione a parentesi quadre.
- La proprietà **`length`** non è il conteggio dei valori: contiene l'indice massimo + 1, ed è **scrivibile** (assegnare un indice alto la aumenta, ridurla tronca l'array).
- Un array può contenere **tipi eterogenei** (stringhe, oggetti, numeri, funzioni).
- Gli array possono contenere altri array, formando **array multidimensionali** (es. matrici, accessibili con `matrix[i][j]`).

```js
let a = [1, 2, 3];
a[999] = 998;   // a.length diventa 1000
a.length = 3;   // tronca l'array
```

#### Metodi di aggiunta/rimozione

- **`push()`**: aggiunge in coda; **`unshift()`**: aggiunge in testa.
- **`pop()`**: estrae dalla coda; **`shift()`**: estrae dalla testa.

#### Iterazione

- **`for` classico** sugli indici e **`for..of`** percorrono tutti gli elementi (inclusi eventuali *buchi* come `undefined`).
- **`forEach()`** riceve una callback `(value, index, array)`.
- **`for..in`** è sconsigliato sugli array: è 10–100 volte più lento e può includere altre proprietà enumerabili.

### Destructuring

> [!def] Destructuring assignment
> Sintassi che permette di **spacchettare** un array in variabili: `let [x, y] = ...`. Gli elementi rimanenti sono scartati, oppure raccolti con l'operatore **rest** `...`.

```js
let [a, b, ...rest] = [1, 2, 3, 4, 5]; // rest = [3, 4, 5]
```

- Una sintassi simile vale per i **parametri di funzione**: `function greet(msg, ...names)` raccoglie gli argomenti extra nell'array `names`.

### Iterabili e Symbol.iterator

- Il **`for..of`** funziona con oggetti **iterabili**: array e stringhe lo sono.
- Per rendere iterabile un oggetto custom occorre implementare il metodo speciale **`Symbol.iterator`**.

> [!info] Protocollo di iterazione
> - All'avvio del ciclo, `for..of` chiama `Symbol.iterator` una volta (in sua assenza lancia un `TypeError`).
> - Da quel momento lavora solo con l'**iterator** restituito.
> - Per ogni valore chiama `next()`, che restituisce `{ done: boolean, value: any }`: `done: true` termina il ciclo, altrimenti `value` è il prossimo valore.

```js
range[Symbol.iterator] = function() {
    return { current: this.min, max: this.max, step: this.step,
        next() {
            let n = { done: false, value: this.current };
            if (n.value > this.max) n.done = true;
            this.current += this.step;
            return n;
        } };
};
```

- È possibile usare l'iteratore **esplicitamente**: chiamare `next()` in un ciclo `while` fino a `done` replica il comportamento di `for..of`.

### Map

> [!def] Map
> Collezione di **coppie chiave-valore** a differenza degli oggetti, ammette **chiavi di qualsiasi tipo** (non solo stringhe).

| Metodo / proprietà | Descrizione |
|---|---|
| `new Map()` | crea la map |
| `map.set(key, value)` | memorizza il valore associato alla chiave |
| `map.get(key)` | restituisce il valore, o `undefined` se assente |
| `map.has(key)` | `true` se la chiave esiste |
| `map.delete(key)` | rimuove la coppia |
| `map.clear()` | svuota la map |
| `map.size` | numero di elementi |

- In un oggetto le chiavi sono **coercite a stringhe**: `{1: "Num"}` e `{"1": ...}` collidono; in una `Map` i tipi restano distinti.

#### Iterazione sulle Map

- **`map.keys()`**, **`map.values()`** e **`map.entries()`** restituiscono iterabili su chiavi, valori e coppie.
- Iterare direttamente la map (`for (let [key, value] of map)`) equivale a usare `entries()`.

### Set

> [!def] Set
> Struttura per collezioni di **valori unici**, senza ripetizioni.

| Metodo / proprietà | Descrizione |
|---|---|
| `new Set([iterable])` | crea il Set, copiando i valori di un iterabile |
| `set.add(value)` | aggiunge il valore e restituisce il set |
| `set.delete(value)` | elimina il valore; `true` se esisteva |
| `set.has(value)` | `true` se il valore è presente |
| `set.clear()` | svuota il set |
| `set.size` | numero di elementi |

## Classi

### La sintassi class

- Una **classe** è un template per creare oggetti; `new Pet(...)` crea l'oggetto e invoca `constructor()` con gli argomenti, che imposta le proprietà sull'oggetto nuovo, poi lo restituisce.

```js
class Pet {
    constructor(name) { this.name = name; }
    greet() { /* ... */ }
}
let pet = new Pet("Chuck");
```

> [!info] Cosa fa davvero `class`
> Una classe **non è una nuova entità del linguaggio**: `typeof Pet` è `"function"`.
> 1. Crea una funzione costruttore il cui codice è preso da `constructor()`.
> 2. Memorizza gli altri metodi in `Pet.prototype`.

- Come gli oggetti, le classi supportano **proprietà** di istanza e **getter/setter** (`get`), e possono definire metodi speciali come `[Symbol.iterator]`.

```js
class Duck {
    species = "Duck";           // proprietà
    get fullDescription() { return `${this.name} the ${this.species}`; }
}
```

### Ereditarietà: extends

- Una classe può ereditare da un'altra con la keyword **`extends`**; i metodi della classe base restano accessibili, quelli ridefiniti vengono **sovrascritti** (override).

```js
class Duck extends Pet {
    greet() { console.log("Quack!"); } // override
}
```

- Internamente, `extends` è implementato tramite la proprietà **`[[Prototype]]`**: il `<prototype>` di `Duck` punta a `Pet`, che a sua volta punta a `Object`.

![[c63f11662c26cd87aa065b918e341efff06a01d7bee1471a9ee5cac9bab947f5.png|200]]

## Gestione degli errori

### Errori e try/catch/finally

- A runtime possono verificarsi **errori** (errori del programmatore, input inattesi): normalmente interrompono lo script con un messaggio in console.
- Il costrutto **`try/catch/finally`** gestisce gli errori: `try` contiene il codice a rischio, `catch` riceve l'oggetto `error` (con `name` e `message`), `finally` è eseguito sempre.

```js
try {
    x = 1; // errore
} catch (error) {
    console.log(error.name, error.message);
} finally {
    console.log("done");
}
```

- In JavaScript c'è **al massimo un blocco `catch`** (`try/finally` da solo è ammesso); i diversi tipi di errore si distinguono dentro il blocco, ad esempio con `instanceof`.
- L'oggetto `error` è gestito tipicamente verificando `error instanceof ReferenceError`.

### instanceof

> [!def] Operatore instanceof
> Verifica se la proprietà `prototype` di un costruttore **compare nella catena dei prototipi** di un oggetto.

```js
pet instanceof Pet;    // true
pet instanceof Object; // true
```

![[c7653673a2b3c7c10b0cd19f28aa5a0ee497365b22b19fc5a6c58fda57f552d1.png|200]]

### throw

- Gli errori **si propagano verso l'alto** nella call tree finché non sono catturati o si raggiunge la cima (in tal caso lo script si interrompe).
- Si possono lanciare errori con la keyword **`throw`**, tipicamente `throw new Error("...")`.
- È possibile definire **classi di errore custom** estendendo `Error` e sovrascrivendo `this.name` nel costruttore (chiamando `super(message)`).

```js
class MyError extends Error {
    constructor(message = "Whoops") { super(message); this.name = "MyError"; }
}
```

## Moduli

### Modularità

> [!def] Modulo
> Un modulo è semplicemente un **file JavaScript**; i moduli si caricano a vicenda tramite le direttive **`export`** ed **`import`**, per scambiare funzionalità.

- La modularità ** migliora la manutenibilità** e promuove la separazione delle *concerns*.
- Aiuta a prevenire **conflitti di naming**: identificatori uguali in moduli diversi non collidono.

> [!warning] Perché gli script semplici non bastano
> Includere più `<script>` nella pagina mette tutto in un unico scope globale: due `let msg` con lo stesso nome provocano un `SyntaxError: redeclaration of let msg`. Il riuso del codice richiederebbe di rinominare gli identificatori, vanificando lo scopo.

### export e import

- **`export`** etichetta le variabili e le funzioni accessibili dall'esterno del modulo; tutto il resto rimane **privato**.
- **`import`** importa funzionalità specifiche da altri moduli (solo se esportate), specificandone l'URL; si può rinominare con `import { greet as greetPet }`.
- Nell'HTML basta includere lo script principale come modulo: `<script type="module" src="./script-module.js"></script>`.

```js
// pet-module.js
export function Pet(name, age) { this.name = name; this.age = age; }
let msg = "Hello"; // privato, non esportato

// script-module.js
import { Pet, greet as greetPet } from './pet-module.js';
```
