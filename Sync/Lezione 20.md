# Lezione 21 API REST: documentazione, evoluzione e hardening

Un backend non è finito appena gli endpoint funzionano: diventa maturo quando può evolvere, sopravvivere ai clienti, resistere agli abusi ed essere gestito in sicurezza. Gli strumenti per riuscirci sono documentazione formale, strategie di evoluzione, sicurezza e osservabilità.

## OpenAPI

### Cos'è OpenAPI

> [!def] OpenAPI
> **Standard aperto e formale** per descrivere API HTTP, noto in precedenza come *Swagger*. È lo standard più adottato a livello industriale.

Le ragioni dell'introduzione dello standard:

- **Standardizzazione**: garantisce pratiche di documentazione consistenti.
- **Documentazione**: consente di generare automaticamente documentazione completa.
- **Code generation**: permette la generazione automatica di librerie client e di stub server.
- **Leggibilità**: è leggibile sia da macchine (discovery automatizzata) sia da esseri umani.

### Struttura di una specifica

Una descrizione OpenAPI è un documento testuale strutturato che rappresenta un oggetto JSON, in formato JSON o YAML. I campi principali della specifica sono:

- `openapi`: la versione della specifica OpenAPI usata.
- `info`: i metadati dell'API (titolo, versione).
- `paths`: gli endpoint dell'API.

```yaml
openapi: 3.1.0
info:
  title: A minimal specification
  version: 0.0.1
paths: {} # nessun endpoint definito
```

### Paths

Gli endpoint dell'API sono chiamati **path** nella specifica. Un oggetto `paths` definisce una sequenza di endpoint; per ogni endpoint i metodi HTTP supportati; per ogni metodo i parametri di input attesi (path parameter, header, ecc.), l'eventuale request body e le possibili risposte.

Un endpoint `/auth` con metodo `POST` attende una request body JSON di tipo `{usr, pwd}` e risponde `200` in caso di successo, `401` con credenziali non valide:

```yaml
/auth:
  post:
    requestBody:
      content:
        application/json:
          schema: { type: object, properties: { usr: {type: string}, pwd: {type: string} } }
    responses:
      "200": { description: User authenticated }
      "401": { description: Invalid credentials }
```

### Strumenti e code generation

OpenAPI è supportato da strumenti open source maturi, tra cui:

- **Swagger Editor**: editor della specifica con anteprima della documentazione (Swagger UI) generata in tempo reale.
- **Swagger Codegen**: generazione di codice a partire dalla specifica.
- **Swagger UI**: rendering della documentazione interattiva.
- Un'alternativa gratuita è `openapi-generator.tech`.

La generazione di codice agisce su due lati:

- **Server**: produce soltanto stub; i linguaggi e framework supportati includono ASP.NET, Go, Java, JaxRS, Micronaut, Kotlin, Node.js, Python (Flask), Scala, Spring.
- **Client**: genera SDK dell'API in decine di linguaggi, tra cui C#, Dart, Go, Java, JavaScript, Kotlin, PHP, Python, R, Ruby, Scala, Swift, TypeScript.

### OpenAPI-driven development

Nell'approccio **OpenAPI-driven development** la specifica dell'API viene definita prima di scrivere il codice. In questo modo si sfruttano al massimo le capacità di code generation e si promuove l'indipendenza tra i team coinvolti (front-end, back-end, QA): la definizione dell'API tiene tutti gli stakeholder allineati.

## Il contratto API

> [!def] Contratto API
> **Impegno** che si crea verso i clienti nel momento in cui si espone un'API. Anche se non viene scritto formalmente, i client ci dipendono.

Il contratto include:

- **Percorsi URL e metodi HTTP**.
- **Formato della request body** e della **response body**.
- **Status code**.
- **Requisiti di autenticazione e regole di autorizzazione**.
- **Formato degli errori**.
- **Aspettative di performance**.

## Evoluzione dell'API

### Perché le API evolvono

Le API, come ogni software di rilievo, evolvono nel tempo. Cause tipiche di cambiamento:

- **Regole di business** che cambiano.
- **Requisiti del frontend** che cambiano.
- **App mobile** che hanno bisogno di nuovi campi.
- **Modello dati** diventato insufficiente.
- **Problemi di performance** che emergono.
- **Requisiti di sicurezza** che cambiano.
- **Integrazioni con terze parti** che evolvono.

### Cambiamenti sicuri e breaking

Un cambiamento è **sicuro** se non influisce sui clienti esistenti; è **potenzialmente breaking** se può far smettere di funzionare i clienti esistenti con la nuova API.

| Di solito sicuri | Potenzialmente breaking |
|---|---|
| Aggiungere un nuovo endpoint | Rinominare un campo |
| Aggiungere un campo opzionale in request | Rimuovere un campo |
| Aggiungere un campo opzionale in response | Cambiare il tipo di un campo |
| Aggiungere un parametro di filtro con default | Cambiare gli status code |
| Rifattorizzare l'interno senza alterare il comportamento | Cambiare il formato degli errori |
|  | Cambiare la semantica di un endpoint esistente |
|  | Cambiare i requisiti di autenticazione/autorizzazione |

Aggiungere un campo a una response è tipicamente sicuro: i client dovrebbero ignorare i campi sconosciuti. Al contrario, sostituire un campo `completed` booleano con un campo `status` a valori `TODO`, `IN-PROGRESS`, `DONE` (per tracciare lo stato con granularità più fine) è breaking, perché i client esistenti si aspettano il campo originale con il tipo originale.

### Versionamento

Non è possibile limitarsi ai soli cambiamenti sicuri: prima o poi un cambiamento breaking diventa necessario. Quando la retro-compatibilità si rompe serve una **strategia evolutiva**: mantenere online entrambe le versioni, almeno per un periodo, e permettere ai client di usare versioni diverse dell'API.

Le strategie comuni di **API versioning** sono:

- **URI versioning**: la versione compare nell'URI, es. `/api/v1/tasks` e `/api/v2/tasks`.
- **Header**: il client dichiara la versione in un header di richiesta, es. `X-API-Version: 2` oppure `Accept: application/vnd.academy.tasks.v2+json`.

L'URI versioning è facile da capire e testare, facile da documentare e facile da instradare nella maggior parte dei framework; può però creare duplicazioni nei controller e nei router.

> [!info] Regole di versionamento
> - Non creare una nuova versione per ogni piccolo cambiamento: il versionamento si usa solo in presenza di un cambiamento breaking.
> - Mantenere più versioni contemporaneamente è un grosso sforzo.
> - Regola pratica: aggiungere senza versionare, rimuovere o ridefinire con versionamento.

### Deprecation e sunset

Il versionamento non basta: serve anche comunicare il ciclo di vita, perché in genere non si vuole supportare una vecchia API per sempre. Il ciclo tipico di una versione è:

1. **Active**: la versione raccomandata.
2. **Deprecated**: funziona ancora, ma i client dovrebbero migrare alla versione attiva.
3. **Sunset**: funziona ancora, ma la data di rimozione è stata annunciata.
4. **Removed**: la versione non è più disponibile.

L'idea importante è non rompere i client in silenzio, dando loro un preavviso equo prima del cambiamento breaking. Un endpoint deprecato può continuare a funzionare ma restituire header di avvertimento aggiuntivi:

```http
HTTP/1.1 200 OK
Deprecation: true
Sunset: Wed, 31 Dec 2026 23:59:59 GMT
Link: </docs/migrate-v1-to-v2>; rel="deprecation"
```

Questi header si aggiungono con Spring Boot impostandoli sulla `ResponseEntity` (es. `.header("Deprecation", "true")`) e con Django Ninja assegnandoli direttamente sulla risposta.

## Sicurezza e hardening

### OWASP API Security Top 10

L'elenco dei principali rischi di sicurezza per le API:

1. **Broken Object Level Authorization** (BOLA)
2. **Broken Authentication**
3. **Broken Object Property Level Authorization**
4. **Unrestricted Resource Consumption**
5. **Broken Function Level Authorization**
6. **Unrestricted Access to Sensitive Business Flows**
7. **Server Side Request Forgery** (SSRF)
8. **Security Misconfiguration**
9. **Improper Inventory Management**
10. **Unsafe Consumption of APIs**

### Broken Object Level Authorization

Il rischio: un client autenticato richiede un oggetto che non gli appartiene, es. `GET /api/tasks/42` dove il task 42 è di un altro utente. Gli sviluppatori spesso dimenticano l'autorizzazione a livello di oggetto e si affidano troppo alla sola autenticazione.

> [!warning] Autenticazione e autorizzazione
> L'autenticazione accerta **chi** è il client, non **che cosa** può fare: ogni accesso a un oggetto deve verificare anche la **proprietà** dell'oggetto, es. filtrando per proprietario (`owner`) nella query.

### Broken Authentication

Impatto: un attaccante può prendere il controllo di account di altri utenti, accedendo a dati personali ed eseguendo operazioni sensibili. Un'API è vulnerabile se:

- La chiave segreta dei JWT è esposta o prevedibile.
- Permette password deboli.
- Permette di cambiare email o password, o di fare operazioni sensibili, senza conferma della password.
- Non valida correttamente i token, es. ignora la data di scadenza.
- Permette attacchi brute force senza meccanismi di lockout.

### Broken Object Property Level Authorization

Impatto: l'accesso non autorizzato a proprietà private o sensibili di un oggetto può causare divulgazione indesiderata di dati. Un'API è vulnerabile se espone proprietà sensibili di un oggetto, o se permette di cambiarne, aggiungerne o eliminarne il valore. Il difetto è tipicamente associato alla restituzione dei modelli direttamente, senza l'uso di DTO o schema.

### Unrestricted Resource Consumption

Le API spesso non limitano le interazioni dei client né il consumo di risorse, il che può essere sfruttato per attacchi DoS o per aumentare i costi operativi. Un'API è vulnerabile se almeno uno di questi limiti è impostato in modo inappropriato:

- **Execution timeout**.
- **Rate limit**: quante richieste per client per unità di tempo.
- **Memoria allocabile massima**.
- **Numero massimo di processi**.
- **Dimensione massima dei file in upload**.
- **Numero di record restituiti per pagina** in una singola request-response.
- **Limiti di spesa** verso servizi di terze parti.

### Rate limiting

> [!def] Rate limiting
> **Meccanismo** che controlla quante richieste un client può effettuare, imponendo un numero massimo di richieste per utente, per funzionalità, per unità di tempo.

Il rate limiting aiuta con: prevenzione degli abusi, riduzione dei brute-force, controllo dei costi, fair usage, protezione degli endpoint costosi e riduzione dei sovraccarichi accidentali.

Lo si implementa ad esempio con il middleware `express-rate-limit` in Express:

```js
const limiter = rateLimit({
  windowMs: 60 * 1000,
  limit: 10, // max richieste per finestra temporale
})
app.use(limiter)
```

Con Django Ninja esiste il throttling globale, a livello di router e di metodo (es. `AnonRateThrottle("1/s")`, `AuthRateThrottle("10/s")`); in Spring Boot si può usare la libreria Bucket4j. Quando il limite è superato, la risposta tipica è `429 Too Many Requests`.

### Broken Function Level Authorization

Difetti di autorizzazione che permettono di accedere a funzionalità non autorizzate: un'operazione riservata agli staff, come `DELETE /api/tags/{id}`, viene implementata con un controllo errato oppure non implementata affatto.

### Unrestricted Access to Sensitive Business Flows

Le API possono esporre flussi di business sensibili. Esempi tipici:

- **Acquisto di un prodotto**: l'attaccante compra tutte le scorte di un articolo molto richiesto e rivende a prezzo maggiorato (scalping).
- **Creazione di commenti o post**: l'attaccante riempie il sistema di spam.
- **Prenotazione**: l'attaccante occupa tutti gli slot disponibili impedendone l'uso agli altri utenti.

La mitigazione prevede due fasi: identificare i flussi di business sensibili e applicare soluzioni ingegneristiche — device fingerprinting, human-detection, rilevamento di pattern d'uso non umani, blocco di indirizzi IP.

### Server Side Request Forgery

Se un endpoint esegue una richiesta verso un URI remoto fornito dal client, l'URI deve essere validato correttamente. In caso contrario, un attaccante può forzare l'API a fare richieste verso destinazioni inattese, con possibile esposizione di informazioni sensibili.

### Security Misconfiguration

I framework per API contengono configurazioni complesse; sviluppatori e DevOps possono non seguirle o non rispettare le best practice di sicurezza, aprendo a diversi tipi di attacco. Esempi:

- API distribuita in modalità debug o dev, con esposizione degli stack trace.
- **TLS** non configurato.
- Patch di sicurezza mancanti.

### Error responses

Gli errori fanno parte del contratto API: le API mature restituiscono errori prevedibili e consistenti.

```json
{
  "error": "VALIDATION_ERROR",
  "message": "Title must not be blank",
  "details": { "field": "title" }
}
```

> [!error] Dettagli interni negli errori
> Non far trapelare gli internals nelle risposte di errore, es. `"NullPointerException at TaskService.java:47"` espone dettagli implementativi utili a un attaccante.

### Improper Inventory Management

A volte un'organizzazione non conosce con chiarezza quali endpoint, versioni, ambienti e flussi dati sono esposti. Il problema nasce quando API vecchie o dimenticate restano raggiungibili: gli attaccanti le cercano perché possono avere autenticazione più debole, controlli di autorizzazione mancanti o vulnerabilità note.

### Unsafe Consumption of APIs

Gli sviluppatori tendono a fidarsi dei dati forniti dalle API di terze parti più che dei dati forniti dai client. È pericoloso: i servizi esterni sono fuori dal nostro controllo e vanno trattati con lo stesso sospetto. Un'API fidata può essere compromessa, reindirizzare verso servizi malevoli o inviare payload malevoli, es. SQL injection.

## Osservabilità

In produzione bisogna poter osservare automaticamente lo stato dell'API. Le domande a cui saper rispondere: l'applicazione è in esecuzione? il database è raggiungibile? quante richieste falliscono? quali endpoint sono lenti? gli utenti ricevono 401, 403, 404 o 500? i rate limit vengono superati? le vecchie versioni dell'API sono ancora usate? Senza osservabilità, i problemi di produzione diventano congetture.

### Health check e metriche

Due strumenti concreti di osservabilità:

- **Spring Boot Actuator**: aggiungendo la dipendenza al progetto ed esponendo gli endpoint con `management.endpoints.web.exposure.include=*`, `GET /actuator/health` restituisce lo stato dell'applicazione — valori possibili `UP`, `DOWN`, `OUT_OF_SERVICE`, `UNKNOWN` — mentre `GET /actuator/metrics` elenca le metriche disponibili e `/actuator/metrics/{name}` ne restituisce i valori.
- **Django Ninja**: un health check minimale è un endpoint senza autenticazione che verifica il database con una query semplice.

```python
@api.get("/health", auth=None)
def health(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    return {"status": "ok", "database": "ok"}
```

### Logging

I log utili riguardano gli eventi significativi da tenere sotto controllo:

- **Fallimenti di autenticazione** e di **autorizzazione**.
- **Violazioni dei rate limit**.
- **Errori server imprevisti**.
- **Uso di API deprecate**.
- **Azioni amministrative**.
- **Operazioni che modificano i dati**.
- **Guasti dei servizi esterni**.

Da evitare invece nei log, perché espongono dati sensibili:

- **Password**.
- **Token**.
- **Header `Authorization` completo**.
- **Dati personali sensibili**.
- **Corpi delle richieste completi**, per default.

> [!warning] I log come rischio
> I log sono strumenti operativi, ma possono diventare essi stessi un rischio per la sicurezza.
