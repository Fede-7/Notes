# Lezione 25 Angular To-do List SPA

Questa lezione applica i concetti di Angular a un'app To-do List completa: frontend Angular 19 e backend REST (l'API Express delle lezioni precedenti). Gli schemi architetturali nuovi o degni di nota sono riportati di seguito.

## Rotte e protezione

Le rotte dell'app dichiarano, oltre a `path` e `component`, anche `title` (titolo della pagina per la vista) e, per le rotte riservate, la guardia `canActivate`:

```ts
{ path: "todos", component: TodoPageComponent,
  title: "To-do List | To-do List Angular App",
  canActivate: [authGuard] },
{ path: "todos/:id", component: TodoDetailComponent,
  canActivate: [authGuard] }
```

La rotta `todos/:id` mostra il **path param** `:id`, che il componente dettaglio usa per identificare la risorsa.

La guardia segue lo schema raccomandato: verifica l'autenticazione e, in caso negativo, **non** naviga direttamente ma restituisce un `UrlTree`, che il Router usa per redirigere:

```ts
export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);
  if (authService.isUserAuthenticated()) {
    return true;
  } else {
    return router.parseUrl("/login"); // restituisce un UrlTree
  }
};
```

## Login con reactive form

Il componente di login usa un `FormGroup` con `FormControl` e **validators** sincroni: `Validators.required`, `Validators.minLength(4)`, `Validators.maxLength(16)`.

Il metodo di submit segue il pattern consolidato:

- Se il form è **invalido**, si mostra un messaggio d'errore e non si procede.
- Altrimenti si inviano le credenziali al `RestBackendService`, sottoscrivendo l'`Observable` con le tre callback `next`, `error` e `complete`:
  - `next`: si salva il token restituito dal backend.
  - `error`: credenziali non valide, messaggio d'errore.
  - `complete`: si naviga verso la pagina dei to-do.

Nel template gli errori dei controlli si mostrano solo quando serve, col nuovo control flow `@if`, verificando la proprietà `submitted` e gli `errors` del controllo:

```html
@if (submitted && loginForm.controls.pass.errors) {
  @if (loginForm.controls.pass.errors['required']) {
    <p class="form-error">Password is required.</p>
  }
}
```

## `AuthService` con signal

Il servizio di autenticazione incapsula lo stato in un **signal** di tipo `WritableSignal<AuthState>`, dove lo stato contiene `user`, `token` e `isAuthenticated`. Il token e lo user sono inizializzati da `localStorage`, verificando alla partenza se il token non è scaduto.

Dal signal si espongono tre **computed**: `user`, `token` e `isAuthenticated`.

```ts
user = computed(() => this.authState().user);
token = computed(() => this.authState().token);
isAuthenticated = computed(() => this.authState().isAuthenticated);
```

La sincronizzazione con `localStorage` si affida a un **effect** nel costruttore: ogni volta che `token` o `user` cambiano nello stato, l'effect li riscrive in `localStorage` — o li rimuove se valgono `null`.

## Servizio REST e intercettore

Il servizio verso il backend incapsula `HttpClient` con le opzioni HTTP condivise (header `Content-Type: application/json`) e un metodo per endpoint:

```ts
login(loginRequest: AuthRequest) {
  return this.http.post<string>(`${this.url}/auth`, loginRequest, this.httpOptions);
}
```

> [!def] Auth interceptor
> **Interceptor** di HttpClient che clona ogni richiesta in uscita aggiungendo l'header `Authorization: Bearer <token>` quando il token è presente, così che ogni chiamata autenticata non debba occuparsene manualmente.

```ts
function authInterceptor(request: HttpRequest<unknown>, next: HttpHandlerFn) {
  const authService = inject(AuthService);
  const token = authService.getToken();
  if (token) {
    request = request.clone({ setHeaders: { Authorization: 'Bearer ' + token } });
  }
  return next(request);
}
```

## Pagina dei to-do e componente figlio

La pagina dei to-do dichiara un array `todos: TodoItem[]`, un form reattivo per il nuovo elemento, e delega a `RestBackendService` e ai toast le notifiche; in `ngOnInit()` chiama `fetchTodos()`.

Il singolo elemento della lista è un **componente separato**, incaricato di visualizzare un to-do; il collegamento col genitore segue i pattern `@Input()` / `@Output()`:

```ts
export class TodoItemComponent {
  @Input({ required: true }) todoItem: TodoItem;
  @Output() delete: EventEmitter<number | undefined> = new EventEmitter();
}
```

- `@Input({ required: true })`: il genitore **deve** passare la proprietà, non è più opzionale.
- `@Output() delete`: il figlio emette l'evento (es. l'id dell'elemento) e il genitore lo gestisce con `(delete)="handleDelete($event)"`.

Il template del genitore itera la lista col control flow `@for`, con `track item.id` e blocco `@empty` per la lista vuota:

```html
<ul>
  @for (item of todos; track item.id) {
    <app-todo-item [todoItem]="item" (delete)="handleDelete($event)" />
  } @empty {
    <li>No to-do items to show.</li>
  }
</ul>
```