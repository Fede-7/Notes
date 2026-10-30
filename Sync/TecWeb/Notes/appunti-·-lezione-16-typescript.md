# Lezione 16 TypeScript

## JavaScript e i tipi

JavaScript ha un type system peculiare, con due caratteristiche fondamentali:

- È **dinamicamente tipizzato**: una variabile non ha un tipo fisso, che dipende dal valore assegnato (`undefined`, poi `number`, poi `string`, …).
- È **debolmente tipizzato** ed esegue cast impliciti nelle espressioni, es. in `"100" - 1 + "42"` la sottrazione converte a numero e la somma finale converta a stringa, producendo `"9942"`.

Queste caratteristiche rendono il linguaggio pratico per manipolare piccole pagine web, senza dichiarare tipi o cast espliciti. Al crescere della complessità dei programmi però:

- È più facile introdurre bug subdoli.
- L'esperienza di sviluppo peggiora: scarso supporto IDE, pochissimi errori colti prima del runtime.
- Il codice diventa meno manutenibile e difficile da capire.

Tipici errori rilevabili solo a runtime in JavaScript puro: invocare come funzione una variabile che non lo è (`TypeError`), assegnare a una proprietà col nome sbagliato senza alcun errore, usare un metodo inesistente (es. `add` su un array).

## Transpiler

> [!def] Transpiler
> **Strumento** che traduce codice scritto in un nuovo linguaggio di programmazione, con feature aggiuntive, in codice JavaScript standard, eseguibile ovunque JavaScript sia supportato.

Con l'uso di JS per programmi sempre più complessi, gli sviluppatori hanno sentito il bisogno di superarne i limiti; un nuovo linguaggio non era fattibile perché JS era già ampiamente supportato, quindi sono nati molti linguaggi che compilano verso JS: CoffeeScript, TypeScript, Dart, Elm e centinaia d'altri.

> [!def] TypeScript
> **Superset di JavaScript** nato nel 2012, disegnato e sviluppato da Microsoft (core dev: Anders Hejlsberg), che aggiunge la tipizzazione statica e altro; compila verso JavaScript ed è di gran lunga il "sapore" di JS più popolare.

Si installa come pacchetto npm con `npm install -g typescript`, che rende disponibile il compilatore `tsc`; in alternativa si esegue `tsc` da un pacchetto locale con `npx`. I file TypeScript hanno estensione `.ts`.

## Compilazione e downleveling

Il codice JavaScript standard è anche TypeScript valido: un file `.ts` contenente solo JS può essere eseguito direttamente con Node, ma senza type checking.

Il compilatore rileva i bug prima del runtime anche su codice JS puro, es. un numero di argomenti inferiore a quello atteso da una funzione (`TS2554`). Con `tsc file.ts` il compilatore produce `file.js`, eseguibile con Node come al solito; il codice generato preserva commenti e indentazioni e sembra scritto da un essere umano.

> [!def] Downleveling
> **Riscrittura** da parte del compilatore di feature di versioni JavaScript recenti in codice per versioni più vecchie: di default TypeScript targetizza ES3 (1999), quindi i template string vengono convertiti in concatenazioni `.concat()`; è possibile scegliere il target, es. `tsc --target es6`.

Il downleveling permette di usare le feature moderne pur girando su browser vecchi.

## Dichiarare i tipi

TypeScript permette di dichiarare tipi per variabili, parametri e valori di ritorno; i tipi primitivi più comuni sono `string`, `number` e `boolean`:

```ts
let courseName: string = "Web Technologies";
let credits: number = 6;
let isGreat: boolean = true;
```

Il codice con annotazioni di tipo non è più JavaScript valido: l'esecuzione diretta con Node fallisce con un `SyntaxError`, quindi occorre compilare il file `.ts` prima di eseguire il `.js` generato. Il compilatore segnala le assegnazioni di tipo incompatibile, es. assegnare una stringa a una variabile `number` (`TS2322`).

## `any` e inferenza dei tipi

- **`any`**: tipo speciale con cui si può fare qualsiasi cosa senza che il compilatore si lamenti; il codice compila ma gli errori tornano a manifestarsi a runtime.
- **Type inference**: senza annotazione esplicita, TypeScript deduce il tipo dal contesto, es. una stringa letterale diventa `string`, un array di numeri diventa `number[]`; il tipo inferito viene comunque applicato, quindi assegnare dopo un tipo diverso è errore.
- **Implicit any**: quando il tipo non è specificato né deducibile, il compilatore defaulta a `any`; il flag `noImplicitAny` trasforma ogni `any` implicito in errore di compilazione (`TS7006`).

## Tipi strutturali

### Array e object types

- **Array**: si specificano con la sintassi `type[]`, es. `let langs: string[]`; passare un elemento di altro tipo è errore (`TS2345`).
- **Object types**: si definiscono elencando le proprietà e i loro tipi, es. `{name: string, credits: number}`; il compilatore segnala le proprietà mancanti (`TS2453`) e le proprietà extra non previste (`TS2353`).
- **Proprietà opzionali**: si dichiarano aggiungendo `?` dopo il nome, es. `credits?: number`; in tal caso il valore può essere `undefined` e va controllato prima dell'uso.

### Union types

> [!def] Union type
> **Tipo** ottenuto combinando due o più tipi con `|`, che rappresenta valori appartenenti a uno qualsiasi dei tipi combinati.

TypeScript garantisce che le operazioni su un union type siano valide per **ogni** tipo dell'unione: chiamare `toUpperCase()` su `number | string` è errore (`TS2339`).

> [!def] Narrowing
> **Restrizione** del tipo entro un ramo del codice tramite controlli specifici, es. `typeof x === "string"` o `Array.isArray(x)`; TypeScript inferisce il tipo specifico per ciascun ramo.

```ts
function printError(code: number | string) {
  if (typeof code === "string") {
    console.log(code.toUpperCase()); // in questo ramo code: string
  } else {
    console.log(code); // in questo ramo code: number
  }
}
```

### Type alias e interface

- **Type alias**: assegnano un nome a un tipo con la sintassi `type Nome = definizione`, per riusare lo stesso tipo più volte senza ripetersi (principio DRY).
- **Interface**: altro modo di nominare object types, con la sintassi `interface Nome { ... }`.

```ts
type Credits = number | string;
type Course = { name: string, credits: Credits };
```

> [!def] Structural typing
> **Natura di TypeScript**: la compatibilità tra tipi è determinata solo dalla struttura e dalle capacità dei tipi, non dai nomi; un oggetto con `name: string` e `age: number` è compatibile sia con `interface Person` sia con `interface Pet` che abbiano quei membri. Java, al contrario, ha un type system **nominativo**.

Le interfacce si estendono con `interface Bird extends Pet`, che eredita le proprietà; assegnare un oggetto senza la proprietà richiesta della "madre" è errore (`TS2322`).

Per estendere i type alias si usano gli **intersection types**, creati con `&`: combinano più tipi in uno, il cui risultato ha le proprietà di ciascun tipo (es. `type Bird = Pet & { flies: boolean }`).

> [!info] `type` vs `interface`
> Sono molto simili e spesso intercambiabili; la distinzione chiave è che un **type alias non può essere riaperto** per aggiungere proprietà (una seconda dichiarazione omonima è un errore `TS2300`), mentre un'**interfaccia è sempre estendibile**: più dichiarazioni omonime si fondono in una sola.

### Altri strumenti di tipizzazione

- **Type assertions**: sintassi `x as T` per dire al compilatore un tipo più specifico di quello inferibile, es. `document.getElementById("name") as HTMLInputElement`, che altrimenti sarebbe `HTMLElement`.
- **Type literals**: in posizione di tipo si possono usare stringhe e numeri specifici, es. `let alignment: "center"` accetta solo quel valore; poco utili da soli.
- **Literals + unions**: esprimono tipi che corrispondono a un insieme chiuso di valori noti: `type Alignment = "center" | "left" | "right"`; valori fuori dall'insieme sono errore di compilazione.
- **Enum**: permettono di definire un insieme di costanti nominate, es. `enum Priority { Low, Medium, High }`; i membri hanno valori numerici progressivi a partire da 0, quindi `Priority.Medium` vale `1`.
- **Function types**: espressioni che descrivono firme di funzione, es. `type stringDecoratorFunction = (x: string, mode: boolean) => string`; una funzione assegnata deve avere la firma compatibile.

> [!warning] Type assertion a compile-time
> Un'asserzione di tipo non è un'asserzione in senso di testing e **non è applicata a runtime**: è solo una promessa al compilatore, che non verifica nulla dell'effettivo contenuto del valore.

## Generics

Il problema di partenza: una funzione come l'identità, con parametri e ritorno `any`, è generica ma **perde l'informazione sul tipo** in uscita; dichiararla su un tipo fisso funziona solo con quello.

> [!def] Type variable (generics)
> **Variabile speciale** che opera sui tipi anziché sui valori, dichiarata dopo il nome della funzione tra `<` e `>`; è uno degli strumenti principali per scrivere codice che lavora con una varietà di tipi preservando l'informazione su di essi.

```ts
function identity<Type>(x: Type): Type { return x; }
let s: string = identity<string>("Hello"); // Type impostato esplicitamente
let n: number = identity(42);              // inferenza automatica
```

Usare i generics non equivale a usare `any`: il tipo di input viene **preservato** in output. Altre possibilità:

- **Più variabili di tipo**: `function merge<T1, T2>(x: T1, y: T2)`.
- **Array parametrici**: `function getFirst<T>(arr: T[]): T` ritorna il primo elemento di un array di `T`.
- **Classi generiche**: `class CustomCollection<T>` incapsula `list: T[]` con metodi tipizzati su `T`.
- **Vincoli**: `<T extends Animal>` restringe il type variable ai tipi compatibili con l'animale; per il typing strutturale, anche un oggetto letterale con le proprietà richieste soddisfa il vincolo.

## Altri tipi da conoscere

- **`void`**: il tipo di ritorno delle funzioni che non restituiscono un valore; è il tipo inferito per le funzioni senza `return` o con `return` vuoto.
- **`unknown`**: rappresenta qualsiasi possibile valore; è simile ad `any` ma più sicuro, perché **non consente alcuna operazione** senza un narrowing o un'asserzione (accedere a `a.name` è errore `TS18046`).
- **`never`**: rappresenta valori mai osservati; è il tipo di un ramo irraggiungibile (es. dopo aver escluso con `typeof` tutti i tipi di un union) o di funzioni che non ritornano mai, perché terminano sempre con un'eccezione.

## Livelli di strictness

Di default TypeScript offre un'esperienza **opt-in**: i tipi sono facoltativi e si usa `any` quando non si può dedurre un tipo preciso. Per evitare di essere troppo invasivo, alcuni controlli sono disattivati di default:

- `noImplicitAny`: segnala come errore ogni `any` implicito.
- `strictNullChecks`: di default `null` e `undefined` sono assegnabili a qualsiasi tipo; dimenticare di gestirli esplicitamente è la causa di innumerevoli bug nel mondo (il cosiddetto **billion dollar mistake**), e il flag li obbliga a una gestione esplicita (es. `TS18048`: "possibly `undefined`").

Un caso tipico: `Array.prototype.find` può restituire `undefined`, e chiamare un metodo sul risultato senza controllarlo è esattamente l'errore che `strictNullChecks` intercetta a compile-time.