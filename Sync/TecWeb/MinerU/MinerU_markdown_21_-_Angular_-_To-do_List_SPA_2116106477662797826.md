## ANGULAR: TO-DO LIST APP

Luigi Libero Lucio Starace, PhD 

luigiliberolucio.starace@unina.it 

https://luistar.github.io 

https://www.docenti.unina.it/luigiliberolucio.starace 

## TO-DO LIST WEB APP: SPA EDITION

• Today, we’ll implement the good ol’ To-do List App as a modern SPA 

• We will use the REST backend developed back in Lecture 15 

• And add a nice Angular 19 frontend on top of it 

## To-do List App: Angular Edition

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/d69ba06c-529b-44e6-9ed1-eac2f68e29ed/770c20ff6f12c77c60bd233e9c43c04d915ce76e85fb663c914390498a733e94.jpg)


Welcome to the To-do List App, now implemented as a sleek Single Page Application using Angular 17 and Tailwind CSS. The backend is the REST API we implemented using Express in Lecture 16. 

Web Technolgies Course, University of Naples Federico II 

Made with  by Luigi Libero Lucio Starace 

## TO-DO LIST WEB APP: SPA EDITION

• During today’s lecture, we’ll check out the Angular To-do List SPA the teacher implemented 

• The source code is available in the course materials on Teams 

• In the remainder of these slides, we’ll go over some of the interesting parts for reference 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/d69ba06c-529b-44e6-9ed1-eac2f68e29ed/ec85fbb91fc3f72408ee6e58f16011d39f2c7e64d5c847f617f568409ff5f59a.jpg)


Web Technolgies Course, University of Naples Federico II 

## TO-DO LIST SPA: LIVE DEMO TIME

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/d69ba06c-529b-44e6-9ed1-eac2f68e29ed/826c5880865fc8ea64325f32b6bb29e39491f8be8604f6cd8b436fd514f93abe.jpg)


## TO-DO LIST SPA: ROUTES

```typescript
/* Nothing much is going on here */
export const routes: Routes = [
    {
    path: "home", component: HomepageComponent,
    title: "To-do List Angular App"
    },
    {
    path: "login", component: LoginComponent,
    title: "Login | To-do List Angular App"
    },
    { /*some routes were omitted for the sake of brevity*/
    path: "todos", component: TodoPageComponent,
    title: "To-do List | To-do List Angular App",
    canActivate: [authGuard]
    },
    {
    path: "todos/:id", component: TodoDetailComponent,
    title: "To-do Detail | To-do List Angular App",
    canActivate: [authGuard]
    }
]; 
```

## TO-DO LIST SPA: AUTHGUARD

```javascript
export const authGuard: CanActivateFn = (route, state) => {
    const authService = inject(AuthService);
    const toaster = inject(ToastrService);
    const router = inject(Router);
    if (authService.isUserAuthenticated()) {
    return true;
    } else {
    toaster.warning("Please, login to access this feature", "Unauthorized!");
    return router.parseUrl("/login"); //return a UrlTree
    }
}; 
```

## TO-DO LIST SPA: LOGIN COMPONENT

```javascript
export class LoginComponent {
    toaster = inject(ToastrService);
    router = inject(Router);
    revService = inject(RestBackendService);
    authService = inject(AuthService);
    submitted = false;
    loginForm = new FormGroup({
    user: new FormControl('', [Validators.required]),
    pass: new FormControl('', [
    Validators.required,
    Validators.minLength(4),
    Validators.maxLength(16)])
    });
    handleLogin() {/* handles login submit */}
} 
```

## TO-DO LIST SPA: LOGIN COMPONENT

```javascript
handleLogin() {
    this.submitted = true;
    if(this.loginForm.invalid){
    this.toast.error("Invalid data!", "Oops! Invalid data!");
    } else {
    this.restService.login({
    usr: this.loginForm.value.user as string,
    pwd: this.loginForm.value.pass as string,
    }).subscribe({
    next: (token) => { this.authService.updateToken(token as string); },
    error: (err) => { this.toast.error("Invalid", "Oops! Invalid credentials");},
    complete: () => {
    this.toast.success(`Welcome`, `Welcome ${this.loginForm.value.user}!\);
    this.router.navigateByUrl("/todos");
    }
    })
    }
} 
```

Luigi Libero Lucio Starace, Ph.D. - University of Naples Federico II - Web Technologies Course - Lecture 22 - Implementing a SPA with Angular 

## TO-DO LIST SPA: LOGIN TEMPLATE

• Interesting bit from the LoginComponent template 

• We conditionally show input errors only when needed 

• We use the new Angular 17 control flow syntax @if! 

```txt
<label for="pass" class="classes-omitted">Password</label>
<input type="password" formControlName="pass" id="pass" class="omitted" required="">
@if(submitted && loginForm.controls.pass.errors){
    @if(loginForm.controls.pass.errors['requiredehler]
    <p class="form-error">Password is required.</p>
    }
    @if(loginForm.controls.pass.errors['minlengthehler]
    <p class="form-error">Password should contain at least 4 characters</p>
    }
} 
```

## TO-DO LIST SPA: AUTH SERVICE

```typescript
type AuthState = {
    user: string | null,
    token: string | null,
    isAuthenticated: boolean
}

@Injectable({
    providedIn: 'root'
})
export class AuthService {

    authState: WritableSignal<AuthState> = signal<AuthState>({
    user: this.getUser(),
    token: this.getToken(), //get token from localStorage, if there isAuthenticated: this.verifyToken(this.getToken()) //verify it's not expired
    }) 
```

## TO-DO LIST SPA: AUTH SERVICE

```typescript
@Injectable({
    providedIn: 'root'
})
export class AuthService {

//continues from the previous slide
user = computed(() => this.authState().user);
token = computed(() => this.authState().token);
isAuthenticated = computed(() => this.authState().isAuthenticated); 
```

## TO-DO LIST SPA: AUTH SERVICE

```javascript
@Injectable({ providedIn: 'root'})
export class AuthService {
    // continues from the previous slide
    constructor(){
    effect( () => { //we use an effect to keep data aligned with localStorage
    const token = this.authState().token;
    const user = this.authState().user;
    if(token !== null)
    localStorage.setItem("token", token);
    else
    localStorage.removeItem("token");
    if(user !== null)
    localStorage.setItem("user", user);
    else
    localStorage.removeItem("user");
    });
} 
```

## TO-DO LIST SPA: REST BACKEND SERVICE

```typescript
@Injectable( { providedIn: 'root' }) export class RestBackendService {
    url = "http://localhost:3000"
    constructor(private http: HttpClient) {}
    httpOptions = {
    headers: new HttpHeaders({
    'Content-Type': 'application/json'
    })
};
login(loginRequest: AuthRequest){
    const url = `${this.url}/auth`
    return this.http.post<string>(url, loginRequest, this.httpOptions);
}
//rest of the service omitted for the sake of brevity
} 
```

## TO-DO LIST SPA: AUTH INTERCEPTOR

```typescript
function authInterceptor(request: HttpRequest, next: HttpHandlerFn) {
    const authService = inject(AuthService);
    const token = authService.getToken();

    if (token) {
    // Clone the request and add the Authorization header with the token
    request = request.clone({
    setHeaders: {
    Authorization: 'Bearer' + token
    }
    });
    }

    return next(request); // Continue with subsequent interceptors, if any
} 
```

## TO-DO LIST SPA: TO-DO PAGE COMPONENT

```typescript
export class TodoPageComponent {
    createTodoSubmitted = false;
    revService = inject(RestBackendService);
    toaster = inject(ToastrService);
    router = inject(Router);
    todos: TodoItem[] = []; //array of TodoItems

    newTodoForm = new FormGroup({
    todo: new FormControl('', [Validators.required])
});

ngOnInit() { this.fetchTodos(); }
fetchTodos() { /*...*/ }
handleTodoSubmit() { /*...*/ }
handleDelete(id: number | undefined) { /*...*/ }
} 
```

## TO-DO LIST SPA: TO-DO TEMPLATE

• Interesting bit shown below 

• Note that <app-todo-item> is a separate component, taking care of displaying a single To-do Item in the list 

• The TodoItem to show is passed as a property 

• Note that the component can also emit delete events 

```txt
<ul class="classes-omitted">
    @for(item of todos; track item.id){
    <app-todo-item [todoItem]=item (delete)="handleDelete($event)"/>
    } @empty {
    <li class="classes-omitted">No to-do items to show.</li>
    }
</ul> 
```

## THE TO-DO ITEM COMPONENT

```typescript
export class TodoItemComponent {
    @Input({ required: true}) todoItem: TodoItem;
    @Output() delete: EventEmitter<number | undefined> = new EventEmitter();
    editLink = "";
    restBackend = inject(RestBackendService);
    toaster = inject(ToastrService);

    ngOnInit(){ this.editLink = "/todos/" + this.todoItem?.id; }

    handleToggleDoneStatus(){ /*...*/ }
    handleDelete(){ /*...*/ }
} 
```