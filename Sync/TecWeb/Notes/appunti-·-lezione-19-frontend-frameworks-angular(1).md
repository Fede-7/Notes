# Lezione 19 Frontend Frameworks Angular

## Frontend framework

> [!def] Frontend framework
> **Insieme predefinito** di componenti software, strumenti e best practice che fa da fondamento per sviluppare Single Page Application.

Le SPA portano con sé una complessità nota: client-side routing, view rendering, componenti e riuso del codice. I framework frontend affrontano esattamente queste sfide.

## Angular

> [!def] Angular
> **Framework frontend** tra i più usati al mondo, sviluppato da Google, particolarmente diffuso in Italia e per le applicazioni enterprise; la versione 2.0 è del 2016.

Le sue caratteristiche distintive sono:

- **Focus sul tooling e sulla produttività** dello sviluppatore.
- **Batteries included**: è un framework opinionato e completo (include meccanismi di dependency injection, routing, …), che riduce la *decision fatigue* e garantisce consistenza tra progetti.
- **Supporto alla migrazione**: tooling dedicato per migrare a versioni più recenti.
- **Best practice da subito**: impone TypeScript.

### CLI

L'interfaccia a riga di comando è il punto d'ingresso tipico del lavoro con Angular:

- `npm install -g @angular/cli` installa la CLI, che espone il comando `ng`.
- `ng new nome-app` crea un nuovo progetto.
- `ng serve` avvia il dev server (di default su `http://localhost:4200/`).
- `ng generate component nome` genera il boilerplate di un componente.

Per l'ambiente di sviluppo si usa Visual Studio Code, con l'estensione raccomandata (ma facoltativa) **Angular Language Service**.

## Componenti

I componenti sono i **mattoni** delle app Angular: ciascuno è responsabile di funzione e aspetto di un elemento di pagina — codice (stato, business logic, eventi), layout HTML e stile CSS. Un componente può contenerne altri: un'app Angular è un **albero di componenti**.

Anatomicamente, un componente è una **classe TypeScript** annotata col decorator `@Component`, cui si passa un oggetto di metadati:

- **`selector`**: dice ad Angular dove renderizzare il componente; per ogni elemento HTML che combacia col selettore viene creata un'istanza del componente (es. il componente con `selector: 'app-root'` renderizza dentro `<app-root>`).
- **`template`** / **`templateUrl`**: il layout HTML, inline o in file separato.
- **`styles`** / **`styleUrl`**: gli stili CSS (o Sass), inline o in file separato.
- **`standalone: true`** e **`imports`**: dichiarano il componente come standalone e importano ciò che usa.

```ts
@Component({
  selector: 'app-root',
  standalone: true,
  template: "<h1>Hello {{name.toUpperCase()}}!</h1>",
  styles: "h1 { color: darkblue; }",
})
export class AppComponent { name = 'Web Technologies'; }
```

Le espressioni in `{{ }}` nel template vengono valutate e il risultato, convertito in stringa, è renderizzato nella pagina.

### Standalone components

> [!def] Standalone component
> **Componente** con `standalone: true` nei metadati, che importa direttamente gli altri componenti, direttive e pipe usati nei suoi template.

Le versioni di Angular precedenti alla 14 usavano un meccanismo diverso, gli **NgModule**; nel corso si usano solo standalone component.

### Stato ed eventi

- Lo **stato** del componente sono le proprietà della classe, referenziabili nel template con l'interpolazione; se una proprietà cambia, la vista si aggiorna.
- Gli **eventi** si collegano a handler con la sintesi delle parentesi, es. `(click)="increment()"`, dove `increment()` è un metodo della classe del componente.

## Control flow nei template

I template Angular supportano gli scenari comuni con la nuova sintassi `@if` / `@for` (prima di Angular 17 si usavano le direttive `ngIf` e `ngFor`):

```html
<button (click)="increment()">Click me</button>
<ul>
  @for (ts of clickTimestamps; track ts) {
    <li>{{ts}}</li>
  } @empty {
    <li>Button has never been clicked!</li>
  }
</ul>
```

- **`@if` / `@else`**: renderizza una porzione di template in modo condizionale, es. `@if (counter === 1) {time} @else {times}`.
- **`@for`**: itera su una collezione rendendo la stessa porzione di template per ogni elemento; richiede `track` per identificare gli elementi; il blocco `@empty` è renderizzato quando la collezione è vuota.

## Comunicazione tra componenti

I componenti devono a volte condividere dati: il genitore configura il figlio o gli passa dati da visualizzare, il figlio comunica al genitore che un evento è avvenuto. I due pattern si implementano con `@Input()` e `@Output()`.

### Da genitore a figlio: `@Input()`

Nel componente figlio, le proprietà che il genitore può passare si dichiarano col decorator `@Input()`, con un valore di default usato quando il genitore non ne passa uno:

```ts
export class CounterComponent {
  @Input() buttonText = "Click me";
  counter: number = 0;
}
```

Il genitore passa il valore impostando una proprietà sull'elemento HTML: `<app-counter buttonText="CLICK HERE" />`.

> [!info] `@Input()` e `input()`
> In molti framework lo stesso meccanismo si chiama *Props* (es. React, Vue). Da Angular 19 l'input/output si gestisce anche con le funzioni `input()` e `output()`, in un approccio basato su signal.

### Property binding

> [!def] Property binding
> **Associazione dinamica** tra un attributo di un elemento HTML o di un componente nel template e una proprietà del componente corrente: il nome dell'attributo va tra parentesi quadre `[...]` e il valore è la proprietà collegata, es. `<app-counter [buttonText]="btnMsg" />`.

Il binding e l'interpolazione non sono sempre equivalenti:

- L'**interpolazione** valuta l'espressione e converte il risultato in stringa.
- Il **property binding** passa il valore così com'è: per passare un oggetto o un array come proprietà di un elemento serve il binding, non l'interpolazione.

### Da figlio a genitore: `@Output()`

> [!def] `@Output()`
> **Canale di comunicazione** da figlio a genitore: una proprietà del figlio decorata con `@Output()` e di tipo `EventEmitter`; il figlio emette un evento invocando `emit()` sulla proprietà.

```ts
export class CounterComponent {
  @Output() counterClickedTenTimes = new EventEmitter<number>();
  increment() {
    this.counter++;
    if (this.counter % 10 === 0)
      this.counterClickedTenTimes.emit(this.counter);
  }
}
```

Il genitore reagisce agli eventi del canale definendo un handler, come per un evento ordinario: `<app-counter (counterClickedTenTimes)="addClicks($event)" />`.

## Routing

Una SPA deve gestire il client-side routing: il **Router** di Angular abilita la navigazione tra viste interpretando l'URL come istruzione per cambiare vista. I progetti creati con `ng new` hanno già il routing configurato.

### Setup

Il setup del Router tocca tre file:

- **`main.ts`**: carica il componente radice con `bootstrapApplication(AppComponent, appConfig)`.
- **`app.config.ts`**: esporta l'`appConfig` con `provideRouter(routes)`, che prepara i provider necessari al modulo Router.
- **`app.routes.ts`**: definisce l'oggetto `routes` di tipo `Routes` (un array di `Route`); ciascuna `Route` ha, tra le altre, le proprietà `path` (URL associato), `title` (titolo della pagina HTML) e `component` (componente associato al path).

```ts
export const routes: Routes = [
  { path: "", component: HomePageComponent, title: "Home Page" },
  { path: "counter", component: CounterPageComponent, title: "Counter" },
];
```

Col setup in atto, il componente **`RouterOutlet`** analizza l'URL corrente e renderizza il componente della rotta combaciante al posto del tag `<router-outlet></router-outlet>` nel template radice.

### Navigazione senza full-reload

Usare link tradizionali con `href` fa eseguire al browser una nuova richiesta HTTP e ricarica tutta l'app: sconfigge lo scopo stesso di una SPA.

> [!def] `RouterLink`
> **Direttiva** da applicare agli elementi che innescano la navigazione, es. `<a routerLink="/counter">Counter</a>`, per usare il Router e cambiare vista senza ricaricare la pagina: è così che una SPA gestisce il routing.

Se l'utente digita manualmente l'URL, avviene un page load e il Router renderizza comunque il componente giusto.

### Link attivi

> [!def] `RouterLinkActive`
> **Direttiva** che applica una lista di classi CSS ai link corrispondenti alla rotta su cui l'app si trova correntemente, per ricordare all'utente in quale pagina è.

Si usa come `routerLinkActive="active"`, abbinata a un po' di CSS (es. `nav .active { font-weight: bold; }`); con `routerLinkActiveOptions` si può richiedere la combaciatura esatta del path.