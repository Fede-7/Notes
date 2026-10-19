# Lezione 12 Web statico e dinamico

## Richiami su Promise e Fetch

### Promise

Un rapido richiamo sul ciclo di vita e sul consumo delle promise.

- **Creazione**: `new Promise(executor)` crea la promise; l'executor riceve le funzioni `resolve` e `reject` per stabilirne l'esito.
- **`setTimeout`**: prende in input una callback e un tempo in millisecondi.
- **Consumo**: `.then(onResult, onError)` gestisce rispettivamente successo ed errore; `.finally()` esegue una callback quando la promise si è *settled*.
- **Asincronia**: le callback della promise vengono eseguite dopo il codice sincrono: `Here` e `There` vengono stampati prima di `Promise settled` e del risultato.

```js
let promise = new Promise((resolve, reject) => {
    // l'executor chiama resolve(value) o reject(new Error(...))
});
promise.finally(() => { /* eseguita quando la promise si settle */ });
promise.then(
    (result) => { /* successo */ },
    (error) => { /* errore: error.message */ });
```

### Fetch API

`fetch()` restituisce una promise che risolve con un oggetto `Response`.

- **Header specifico**: si legge con `response.headers.get(name)`.
- **Tutti gli header**: `response.headers` è iterabile con `for(let [key, value] of response.headers)`.
- **Stato**: `response.status` contiene il codice di stato HTTP; `response.ok` è `true` quando la richiesta ha avuto successo.
- **Corpo**: quando la promise di `fetch()` si risolve, il corpo potrebbe non essere ancora disponibile; la `Response` fornisce metodi *promise-based* per accedere al corpo in vari formati.
  - **`.json()`**: elabora il corpo come JSON appena diventa disponibile.

```js
async function f(){
    let response = await fetch("./example.json");
    response.headers.get('Content-Type');   // un singolo header
    for(let [key, value] of response.headers){ /* iterazione */ }
    let status = response.status;           // codice di stato
    if(response.ok){ /* richiesta riuscita */ }
    let fact = await response.json();       // corpo come JSON
}
```

## Il web statico

Finora abbiamo imparato le tecnologie core del web — **HTML**, **CSS** e **JavaScript** — progettando pagine moderne, responsive e dinamiche: gestione di eventi, modifica del DOM al volo e richieste HTTP asincrone per recuperare dati da mostrare nelle pagine.

### App web statiche


- **Dinamicità nel browser**: il dinamismo dato da JavaScript avviene interamente dentro il browser.
- **Documento identico**: ogni richiesta a una stessa pagina riceve sempre lo stesso documento identico, servito dal **document root** del server.

![[Pasted image 20261016111438.jpg|300]]

### Limitazioni del web statico

L'approccio statico è semplice ed efficace per applicazioni con un numero limitato di pagine che cambiano raramente, ma soffre di alcuni limiti.

- **Personalizzazione**: non permette di adattare una pagina a un utente specifico.
- **Contenuti variabili**: non è adatto quando il contenuto di una pagina cambia molto frequentemente.
- **Scala**: non regge siti costituiti da milioni di pagine.
- **Azioni**: non permette di agire in base a una richiesta (es. salvare un ordine).

> [!info] Costo della duplicazione
> In un sito di ~60 milioni di pagine con la stessa struttura da ~150kB ripetuta in ogni pagina si accumulano ~9TB di dati duplicati; un elemento comune (es. la *navbar*) andrebbe modificato in tutte le pagine.

## Programmazione server-side

### Generazione on-the-fly

Un web server può fare molto più che servire file: può **generare** pagine web **on-the-fly**, tipicamente in base ai parametri ricevuti nella richiesta HTTP. È l'idea chiave dietro la **programmazione server-side**.

- **Parametri della richiesta**: richieste diverse, anche verso la stessa risorsa, producono pagine diverse.
- **Contenuti sempre aggiornati**: la pagina viene costruita al momento della richiesta, non preparata in anticipo.

![[Pasted image 20261016111727.jpg|300]]

## CGI

### Definizione

> [!def] Common Gateway Interface
> **Specifica di interfaccia** che consente a un web server di eseguire programmi esterni per processare una richiesta HTTP. Diffusa nei primi anni '90, prima ancora dell'esistenza di JavaScript, fu il primo strumento per ottenere pagine web dinamiche.

### Flusso di una richiesta

Il CGI definisce come comunicano il web server e i programmi **CGI-compliant**.

- **Browser → Server**: il browser invia la richiesta HTTP al web server.
- **Server → Programma**: il server invoca il programma CGI per processarla.
- **Ritorno**: l'output del programma torna al server, che lo invia al browser come risposta HTTP.


![[Pasted image 20261016111848.jpg|300]]

### Input e output del programma

> [!aside]
> Il programma CGI accede ai suoi input e costruisce la risposta secondo regole precise.
> 
> - **Header e query string della richiesta**: disponibili tramite **variabili d'ambiente**.
> - **Corpo della richiesta**: disponibile al programma sullo stream **stdin**.
> - **Corpo della risposta**: è l'output del programma sullo stream **stdout**.
>
>---
> ![[Pasted image 20261016112005.jpg|200]]

### Primo script CGI

Il primo script CGI mostra la struttura essenziale della risposta: prima gli header (es. `Content-type`), poi una riga vuota, poi il corpo HTML; un contenuto generato al volo (la data corrente) dimostra la dinamicità della pagina.

```bash
#!/bin/bash
echo "Content-type: text/html; charset=utf-8"
echo ""
echo "<h1>Hello CGI!</h1>"
date +"%d/%m/%Y at %H:%M:%S"
```

## Server-side scripting

### Limiti dell'approccio CGI

Scrivere programmi CGI non è un'esperienza piacevole.

- **HTML su stdout**: scrivere interi documenti HTML sullo standard output è macchinoso.
- **Parsing manuale**: analizzare a mano query string e corpi delle richieste è tutt'altro che divertente.
- **Processi**: creare un nuovo processo per ogni richiesta non è molto efficace in termini di risorse.

### Linguaggi di scripting server-side

Per fortuna sono emersi linguaggi e framework specializzati per lo scripting server-side.

- **PHP**: acronimo ricorsivo di *PHP Hypertext Preprocessor*, 1995.
- **ASP**: *Active Server Pages*, linguaggio di scripting server-side di Microsoft, 1997.
- **JSP**: *Java Server Pages*, rilasciato originariamente da Sun, 1999.

L'idea era «mixare» codice server-side e HTML: un interprete speciale elabora il mix per produrre codice HTML «puro».

### PHP

#### Delimitatori

PHP usa **delimitatori** speciali per separare codice e HTML.

- **`<?php ... ?>`**: racchiudono il codice PHP.
- **Testo esterno ai delimitatori**: resta così com'è nell'output.
- **Codice interno ai delimitatori**: viene interpretato e l'output risultante è inserito nell'HTML.
- **`<?=`**: shorthand per `<?php echo`.

```php
<title><?php echo "Hello PHP" ?></title>
<?php $array = ["Hello", "PHP"] ?>
<ul>
    <?php foreach($array as $item): ?>
        <li><?= $item ?></li>
    <?php endforeach; ?>
</ul>
```

#### Gestione delle richieste

Le soluzioni di scripting server-side supportano lo sviluppatore nei compiti tediosi tipici della gestione delle richieste HTTP: le richieste vengono pre-processate automaticamente.

- **Parametri della richiesta**: disponibili negli array associativi `$_GET` e `$_POST`; ad esempio `$_POST['todo']` accede al parametro `todo`.
- **Cookie**: già elaborati nell'array associativo `$_COOKIES`.
- **Risposta**: non è necessario scrivere esplicitamente l'intera risposta su `stdout`.

#### Architettura NGINX e PHP-FPM

Un'applicazione PHP moderna può essere distribuita con **NGINX** come web server e **PHP-FPM** (*FastCGI Process Manager*) come gestore dei processi PHP.

- **NGINX**: web server che riceve le richieste HTTP in arrivo e le smista.
- **Pool di worker**: PHP-FPM gestisce un pool di processi worker che eseguono il codice PHP.
- **Comunicazione**: NGINX inoltra a PHP-FPM le richieste PHP via TCP sulla porta `9000`; i due componenti condividono un volume di dati comune.

![[Pasted image 20261016112143.jpg|300]]