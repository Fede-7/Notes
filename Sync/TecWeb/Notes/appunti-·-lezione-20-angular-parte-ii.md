# Lezione 20 Angular (parte II)

## Form

I form sono in molti casi il modo preferito di raccogliere input dell'utente. Angular li gestisce in due modi:

- **Template-driven**: le associazioni tra i dati del componente e il form sono definite implicitamente nel template, tramite direttive.
- **Reactive**: le associazioni sono definite esplicitamente nel componente.

### Template-driven

La direttiva `[(ngModel)]="prop"` lega il valore di un campo del form a una proprietà del componente. La notazione `[()]`, detta **"banana in a box"**, rappresenta un **two-way binding**: property binding ed event binding insieme.

Il two-way binding funziona in entrambe le direzioni: digitando nell'input si aggiorna la proprietà del componente (e con essa il template), e cambiando la proprietà si aggiorna il campo dell'input.

```html
<input id="pwd" name="pwd" type="password" [(ngModel)]="pass" />
```

### Reactive

Con l'approccio reactive il form è un oggetto creato nel componente: un **`FormGroup`** con dentro un **`FormControl`** per ogni campo, col valore iniziale come argomento.

```ts
loginForm = new FormGroup({
  user: new FormControl(''),
  pass: new FormControl('')
});
```

Nel template si collega il gruppo con `[formGroup]="loginForm"` e i singoli campi con `formControlName`, e i valori si leggono da `loginForm.value.user`.

### Submission

L'invio del form si gestisce con l'event binding `(ngSubmit)="onSubmit()"` sull'elemento `<form>`, dove `onSubmit()` è un metodo del componente che accede ai valori del form.

## Services e Dependency Injection

> [!def] Service
> **Classe** che fornisce funzionalità usabili in più parti dell'applicazione, senza template né stili: solo logica invocabile quando serve.

I service sono ideali per compiti richiesti in punti diversi dell'applicazione, come recuperare dati da una REST API, fare logging o validare dati. Le classi dei componenti restano responsabili solo dell'esperienza utente: template, stili e la logica che media tra vista e business logic.

> [!def] Dependency Injection (DI)
> **Pattern** usato da Angular per far ottenere al codice le istanze delle proprie dipendenze (es. i service), separando le preoccupazioni di costruzione e di uso delle dipendenze e migliorando il disaccoppiamento.

Nel sistema DI di Angular esistono due ruoli: il **dependency consumer** (il codice scritto) e il **dependency provider** (in genere gestito da Angular).

Un service si dichiara iniettabile col decorator `@Injectable`, dove `providedIn: 'root'` lo rende disponibile ovunque nell'app (root injector):

```ts
@Injectable({ providedIn: 'root' })
export class CalculatorService {
  sum(x: number, y: number): number { return x + y; }
}
```

La dipendenza si ottiene in due modi:

- Con la funzione `inject()` in una proprietà: `private calc = inject(CalculatorService)`.
- Dichiarandola nel costruttore della classe: `constructor(private calc: CalculatorService) {}`.

## Proteggere le rotte

Un compito comune del routing è garantire che solo utenti autorizzati accedano a certe rotte.

> [!def] Route Guard
> **Funzione** invocata da Angular per decidere se l'utente può compiere una certa operazione su una rotta; i tipi includono `canActivate`, `canMatch`, `canLoad` e `canDeactivate`.

Le guardie si specificano come proprietà degli oggetti `Route`, es. `canActivate: [authorizationGuard]`. Se ne possono impostare più di una: Angular le esegue tutte in parallelo e l'azione è permessa solo se tutte restituiscono `true`.

```ts
export const authorizationGuard: CanActivateFn = (route, state) => {
  const router = inject(Router);
  const authService = inject(AuthService);
  if (authService.isUserLoggedIn()) return true;
  router.navigateByUrl("/login");
  return false;
};
```

Una guardia può restituire tre cose:

- **`true`**: la guardia è soddisfatta e la navigazione può procedere.
- **`false`**: la guardia non è soddisfatta e l'azione non può essere compiuta.
- **Un `UrlTree`**: il Router deve redirigere a quell'URL.

> [!warning] Redirigere con `UrlTree`
> Con più guardie eseguite in parallelo, restituire sempre un `UrlTree` per la redirezione e non usare direttamente i metodi `Router.navigate()`: due guardie che redirigono possono creare race condition.

## HttpClient

Angular fornisce un'API per le richieste HTTP nel service **`HttpClient`**, da configurare con la dependency injection in `app.config.ts` tramite la funzione dedicata `provideHttpClient()`:

```ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(withFetch(), withInterceptors([authInterceptor])),
    provideRouter(routes)
  ]
};
```

`HttpClient` si ottiene come dipendenza di service e componenti (con `inject()` o via costruttore) e offre metodi corrispondenti ai verbi HTTP; ogni metodo, es. `this.http.get<T>(url)`, restituisce un **`Observable`** dalla libreria **RxJS**.

## Observables

Angular usa gli Observable per gestire molte operazioni asincrone. A grandi linee la differenza con le Promise è questa:

- Una **Promise** può risolvere (o rigettare) una sola volta: emette asincronamente un singolo valore (o un errore).
- Un **Observable** può emettere asincronamente **più valori nel tempo**.

Per ricevere gli eventi si **fa subscribe** all'Observable, passando un oggetto con fino a tre callback:

```ts
observable.subscribe({
  next(value)  { /* un valore è stato emesso */ },
  error(err)   { /* un errore è stato emesso */ },
  complete()   { /* l'Observable ha finito di emettere */ }
});
```

L'argomento del costruttore `new Observable(subscriber => { ... })` è la funzione da eseguire al momento della sottoscrizione; al suo interno si chiamano `subscriber.next(value)`, `subscriber.error(err)` o `subscriber.complete()`.

> [!warning] Errore come completamento
> Gli errori sono considerati completamenti: dopo un `error()` l'Observable non emette più nulla e la callback `complete()` **non** viene invocata.

## Interceptor

> [!def] Interceptor
> **Forma di middleware** di HttpClient per le richieste in uscita: una funzione che riceve la `HttpRequest` corrente e una funzione `next` che rappresenta il passo successivo della catena di interceptor.

```ts
function log(req: HttpRequest<unknown>, next: HttpHandlerFn) {
  console.log(req.url);
  return next(req);
}
```

Casi d'uso tipici: aggiungere header di autenticazione alle richieste (es. token JWT), mettere in cache le risposte per un periodo, loggare le richieste in uscita. Gli interceptor da usare si dichiarano configurando `provideHttpClient(withInterceptors([...]))`.

## Change detection

Quando una proprietà di un componente (il suo stato) cambia, Angular aggiorna automaticamente il suo template: aggiornare le viste solo quando necessario e in modo efficiente (solo le parti da aggiornare) è la chiave delle prestazioni di una SPA.

Il funzionamento in sintesi:

- Quando qualcosa avviene nell'app (eventi DOM, operazioni asincrone, …) scatta il meccanismo di **change detection**.
- Angular percorre tutta la **gerarchia dei componenti**.
- Per ciascun componente controlla se lo stato è cambiato e se il cambio ha effetto sulla vista.
- In tal caso aggiorna la porzione di DOM corrispondente al template del componente.

## Signals

> [!def] Signal
> **Variabile che notifica** gli interessati quando il suo valore cambia; traccia in modo granulare come e dove lo stato è usato nell'app, permettendo ad Angular di evitare change detection non necessarie e aggiornare solo le parti di DOM cambiate.

I signal sono una via alla **programmazione reattiva**, forma di programmazione dichiarativa basata sull'elaborazione di eventi asincroni. Si dividono in **scrivibili** e **read-only**.

- Uno signal scrivibile si crea con `signal(valoreIniziale)`; la lettura avviene invocandolo come funzione, es. `{{count()}}` nel template.
- **`.set(v)`** imposta un nuovo valore; **`.update(fn)`** calcola il nuovo valore a partire dal precedente.

```ts
count = signal(0);
handleClick() { this.count.update(value => value + 1); }
handleReset() { this.count.set(0); }
```

### Computed ed effects

- **`computed(fn)`**: crea un signal **read-only** che deriva il proprio valore da altri signal; Angular lo mantiene aggiornato in modo reattivo; chiamare `.set()` o `.update()` su di esso è errore.
- **`effect(fn)`**: crea una funzione eseguita ogni volta che i signal letti al suo interno cambiano; gli effect vengono eseguiti **almeno una volta**, e durante l'esecuzione registrano i signal letti, così da rieseguirsi al loro cambiamento.

```ts
constructor() {
  effect(() => { console.log(`Count: ${this.count()}`); });
}
```