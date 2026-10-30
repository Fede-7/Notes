# Lezione 27 Web Testing

## Verifica del software

> [!def] Verifica del software
> **Insieme di pratiche** volte ad assicurare che un software soddisfi una specifica, per catturare difetti o bug prima del rilascio del prodotto.

Si divide in due famiglie:

- **Dynamic verification**: coinvolge l'esecuzione del programma; la principale è il **software testing**.
- **Static verification**: non esegue il programma; include code review, static analysis (es. taint analysis) e automated verification (model checking).

> [!def] Software test
> **Sequenza di azioni** progettata per valutare un particolare aspetto o funzionalità di un software; il software sotto test è detto **SUT**.

Un test in genere consiste di tre fasi:

- **Arrange**: garantire che le precondizioni richieste siano soddisfatte.
- **Act**: eseguire una o più azioni.
- **Assert**: controllare che il SUT si sia comportato come inteso.

### Livelli di testing

Il testing si pratica a livelli diversi, che formano la **testing pyramid** (i test più numerosi e rapidi alla base, quelli più lenti e costosi in cima):

- **Unit testing**: testa una singola unità (es. una classe o un metodo).
- **Integration testing**: verifica che unità diverse lavorino insieme come inteso.
- **System testing**: prende di mira il sistema intero contro la sua specifica.
- **End-to-End (E2E) testing**: prende di mira il SUT dal punto di vista degli utenti finali.

Nel testing di web app emergono sfide peculiari:

- A livello **unit**: si deve fare i conti con **codice asincrono** e **dipendenze da servizi esterni**.
- A livello **E2E**: si deve fare i conti con **fragilità** e **flakiness**.

## Unit testing con Angular

Angular include tutto il necessario per testare le app con **Jasmine**; il codice di test vive in **file spec** (specification), generati come stub dalla CLI insieme ai component/service, tipicamente nella stessa directory del codice testato con la convenzione dei nomi `<nome>.spec.ts`.

La struttura tipica di uno spec è:

```ts
describe('CalculatorService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CalculatorService);
  });
  it('should sum two positive numbers correctly', () => {
    expect(service.sum(42, 58)).toBe(100);
  });
});
```

- `describe` raggruppa i test; `beforeEach` esegue codice prima di ciascun test (qui: configurare il `TestBed` e iniettare il servizio).
- `it` definisce un singolo test; `expect(...)` con un matcher esprime l'asserzione.

Il comando `ng test` compila l'app e lancia il **Karma Test Runner**, che raccoglie i file spec, li esegue e produce un report di esecuzione.

### Test double e Spy

> [!def] Test Double
> **Sostituto** di un oggetto di produzione usato nei test al posto dell'originale, per testare un'unità in isolamento, senza che l'esito dipenda da unità esterne.

Il problema: le unità testate dipendono da altre (es. un componente dipende da un service, che dipende da `HttpClient`); un fallimento potrebbe dipendere da una qualunque delle dipendenze, rendendo difficile la fault localization, e alcune condizioni reali (es. temperatura sotto zero) sono impraticabili da attendere in un servizio reale.

La **Dependency Injection** è un supporto prezioso: nei test si configura l'injector perché risolva le dipendenze con i Test Double al posto degli originali.

Scriverli da zero resta laborioso, quindi i framework di testing aiutano: **Jasmine** supporta gli **Spy**, test double che possono *mockare* qualsiasi funzione:

```js
restBackendSpy = jasmine.createSpyObj('RestBackendService', ['getTodos']);
restBackendSpy.getTodos.and.returnValue(of(todos));
```

Lo spy mocka il metodo `getTodos()` e lo configura per restituire sempre l'Observable di una lista data: il test non dipende né dal service reale né dalla REST API esterna.

Nei test dei componenti si assegnano gli spy alle dipendenze del componente, si invocano i metodi, si forza l'aggiornamento della vista con `fixture.detectChanges()` e si eseguono le asserzioni sia sullo stato (es. lunghezza dell'array) sia sul DOM via `DebugElement` (es. `element.query(By.css('ul'))` e il contenuto testuale della lista).

### Code coverage

Il comando `ng test --no-watch --code-coverage` calcola anche le **metriche di code coverage**, un possibile indicatore di quanto "bene" è stata testata l'app: percentuali di **Statements**, **Branches**, **Functions** e **Lines** coperte. Nella directory `/coverage` viene generato un report HTML ispezionabile file per file, riga per riga.

## End-to-End testing

> [!def] End-to-End (E2E) test
> **Test** che prende di mira il sistema intero dal punto di vista dei suoi utenti finali: ogni test replica un flusso d'uso realistico, interagendo con le interfacce esterne del sistema come farebbero gli utenti.

L'interfaccia esterna dipende dal tipo di web app:

- **REST API**: gli endpoint REST sono l'interfaccia esterna e gli "utenti" sono altri programmi; i test E2E inviano richieste HTTP e controllano che le risposte siano corrette secondo la specifica (es. scenario di login: `POST /auth` con credenziali → aspettarsi `200 OK` con `{token}` JWT valido; scenario di inserimento: autenticarsi, salvare il token, `POST /todos` con header `Bearer <TOKEN>` → aspettarsi `200 OK` col corpo atteso).
- **Web app tradizionale o SPA**: le pagine web sono l'interfaccia esterna e gli utenti sono umani con un browser; i test E2E — detti **E2E web test** — interagiscono con le pagine e controllano che cambino correttamente (es. visitare la pagina di login, riempire i campi, cliccare Login, aspettarsi la redirezione alla homepage e il saluto nella navbar).

Gli step chiave di un E2E web test sono due, ripetuti per ogni passo dello scenario:

1. **Selezionare** l'elemento con cui interagire (bottone, campo di testo, …).
2. **Interagire** con esso (click, fill, verifica di proprietà, …).

### Manuale vs automatizzato

L'E2E testing può essere manuale o automatizzato:

- **Manuale**: tester umani seguono uno script dettagliato di passi, replicando gli scenari utente e riportando i problemi.
- **Automatizzato**: si sviluppa software di test (test suite) che simula gli scenari utente, e che può essere rieseguito più volte.

| | Manuale | Automatizzato |
|---|---|---|
| Competenze | Nessuna conoscenza di programmazione | Programmazione e testing |
| Costi | Lento, tedioso, error-prone | Costo iniziale alto, ma rieseguibile con poco sforzo |
| Scala | Non scala: ripetere a ogni release, su tutti i browser e dispositivi | Serve manutenzione del codice di test al variare dell'app |
| Rischi | — | I test possono essere flaky e/o fragili |

### Locator strategies

> [!def] Locator
> **Strategia** con cui si seleziona l'elemento di una pagina con cui interagire; è una parte cruciale degli E2E web test.

Le tre strategie principali sono:

- **Coordinate assolute**: si identifica l'elemento dalle coordinate sullo schermo, es. `click(200, 300)`; è la strategia più fragile.
- **Visual-based locators**: si identifica l'elemento dall'aspetto, con algoritmi di image-matching (es. SikuliX); robusti ai cambi di layout, fragili ai cambi d'aspetto degli elementi.
- **Layout-based locators**: si identifica l'elemento da proprietà di layout, es. selettori CSS: `click(".item button.buy")`; robusti ai cambi puramente visivi, più fragili ai cambi di layout; sono i più usati nella pratica.

> [!info] Il giusto compromesso
> Un buon locator non deve essere né troppo generico (può selezionare l'elemento sbagliato) né troppo specifico (anche un cambiamento minimo lo rompe): anche un piccolo cambiamento nell'app o nell'ambiente di test può rompere i locator, rendendo impossibile interagire con gli elementi giusti e richiedendo una costosa manutenzione per ripararli.

### Flakiness

> [!def] Flakiness
> **Tendenza** dei test E2E a comportarsi in modo inconsistente: lo stesso test può passare o fallire intermittentemente a condizioni identiche (nessun cambiamento nell'app né nel test).

La causa è tipicamente il **non-determinismo** dei tempi di caricamento e di fetch dei dati: una risorsa esterna può impiegare più tempo a restituire i dati da visualizzare, e il test può tentare di accedere a elementi non ancora renderizzati ("element not found"). Si mitiga con appropriate **waiting strategies**.

### Isolamento dei test E2E

I test E2E dovrebbero girare **in isolamento**, con tre benefici:

- **No failure carry-over**: un test che fallisce non influenza i successivi.
- **L'ordine di esecuzione non conta**: i test si possono eseguire in parallelo.
- Ogni test è eseguibile **indipendentemente**, il che facilita il debug.

L'isolamento si ottiene in due modi: **start from scratch**, eseguendo ogni test in un ambiente nuovo e pulito, oppure **clean-up**, ripristinando l'ambiente tra un test e l'altro.

## Playwright

> [!def] Playwright
> **Framework open source** di automazione e testing del browser, sviluppato da Microsoft (prima release: 31 gennaio 2020), cross-browser e cross-platform, event-driven e asincrono, scritto in TypeScript, con API in TypeScript, JavaScript, C#, Java e Python.

Gli altri strumenti principali del settore sono **Selenium** (dal 2009, cross-browser), **Cypress** (dal 2014, cross-browser) e **Puppeteer** (di Google, dal 2017, orientato a Chrome).

Si installa con `npm init playwright@latest`, scegliendo linguaggio, cartella dei test e browser da installare. I test si definiscono con la funzione `test()`, che riceve un titolo e una funzione async col codice del test:

```ts
import { test, expect } from '@playwright/test';
test('has title', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await expect(page).toHaveTitle(/Playwright/);
});
```

Di default i test girano su **chromium** (Blink), **firefox** (Gecko) e **webkit** (il motore di Safari), configurabili in `playwright.config.ts` insieme alle piattaforme; Playwright sa anche emulare browser di tablet e mobile.

### Isolamento e fixture

Playwright ottiene l'isolamento **partendo da zero**: ogni test gira in un ambiente pulito, cioè un nuovo **`BrowserContext`** — una sorta di profilo in incognito — con i propri `localStorage`, `sessionStorage` e cookie, non influenzato dai test precedenti.

L'ambiente di ogni test è definito da **Test Fixtures**: tipicamente Playwright crea un nuovo `BrowserContext` per test e vi fornisce una `Page` di default — un'astrazione di una tab in un browser nuovo. L'argomento `{ page }` nella firma del test chiede a Playwright di configurare la fixture `page`.

### Locating, actions, asserting

I test E2E automatizzati ruotano su tre momenti chiave.

Per **locare gli elementi** Playwright offre funzioni dedicate, oltre ai locator CSS e XPATH con `page.locator(...)`:

- `getByText()`: per contenuto testuale; `getByLabel()`: form control tramite la label associata.
- `getByPlaceholder()`: input tramite il placeholder; `getByAltText()`: elemento (es. immagine) tramite il testo alt.
- `getByTitle()`: tramite l'attributo title; `getByTestId()`: tramite l'attributo `data-testid`.

Per **interagire** con l'elemento locato basta invocare il metodo adeguato: `fill()`, `clear()`, `press()`, `check()`, `selectOption()`, `click()`, `dblclick()`.

Per **asserire** si chiama `expect()` su un valore o un locator seguito dal matcher appropriato: `toBeVisible()`, `toContainText()`, `toHaveClass()`, `toBeDisabled()`, `toBeEmpty()`, `toBeInViewport()`, `toBeDefined()`, …

### Capture and Replay

> [!def] Capture and Replay (C&R)
> **Approccio** in cui il codice di test E2E è generato automaticamente "registrando" (catturando) le interazioni dell'utente con la web app, permettendo di creare test rieseguibili semplicemente usando l'app.

Playwright supporta il C&R col **Test Generator**, accessibile anche dall'estensione VS Code: durante la registrazione il tester interagisce col browser come un utente finale e Playwright cattura le interazioni generando il codice per replicarle, con euristiche integrate per scegliere i locator migliori.

> [!warning] Codice generato
> Il codice C&R può essere subottimale rispetto a fragilità e flakiness: va trattato come punto di partenza, non come prodotto finale.