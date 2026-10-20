# Lezione 13 Node.js

## JavaScript in ambiente server

Col *server-side scripting* le pagine web possono essere generate al volo da programmi in esecuzione sul server; JavaScript, finora usato solo in un ambiente browser, può essere eseguito anche in un ambiente server.

Per eseguire JavaScript lato server sono disponibili diversi **runtime**, tra cui **Node.js**, **Deno** e **Bun**.

> [!def] Node.js
> **Runtime Environment** per JavaScript *open-source* e *cross-platform*, che esegue il motore **V8** di Google proveniente dal progetto Chromium. Si basa su un modello *event-based*, asincrono per default e a I/O *non-blocking*, ed è di gran lunga l'ambiente di esecuzione JavaScript più popolare.

## Gestione multi-threaded delle richieste

Negli altri ambienti di esecuzione e linguaggi, ogni richiesta è gestita da un thread o processo dedicato, prelevato da un pool interno all'*application server*.

![[lezione-13-1792513773927.png|300]]

Nel servire le richieste, le web application devono spesso eseguire operazioni I/O **bloccanti** e time-consuming: **accedere a un database**, **accedere a un'API esterna** (es. con `fetch()`), **leggere un file** dal file system locale, **leggere il body della richiesta**. Di conseguenza, i thread o processi che gestiscono una richiesta passano molto tempo in attesa del completamento di queste operazioni.

Il modello multi-threaded ha due limiti:

- **Inefficienza**: gran parte del tempo dei thread è speso in attesa delle operazioni bloccanti.
- **Scalabilità limitata**: il thread pool è pre-allocato a una dimensione predefinita, quindi non si possono gestire più richieste concorrenti di quante il pool ne permetta.

## La filosofia di Node.js

Node.js adotta una filosofia alternativa al modello multi-threaded, orientata all'efficienza.

- Un programma Node.js viene eseguito in **un singolo processo**: non serve creare un nuovo thread per ogni richiesta.
- Il runtime fornisce nella standard library un insieme di **primitive di I/O asincrone** che impediscono al codice JavaScript di bloccarsi.
- La maggior parte delle librerie sfrutta il paradigma *non-blocking* ogni volta che è possibile.
- Vasta adozione del **callback pattern**: la funzione da eseguire al termine dell'operazione viene registrata al momento della chiamata.
- Le operazioni sincrone sono generalmente un'eccezione più che la norma.

### Il single-threaded event loop

> [!def] Event loop
> **Ciclo a thread singolo** al centro del runtime Node.js: preleva gli eventi in coda, esegue i callback e delega le operazioni I/O bloccanti ai *worker thread*.

 - **Event queue**: le richieste dei client arrivano come eventi in coda, in attesa di essere processati.
 - **Worker thread**: eseguono le operazioni I/O bloccanti (file system, rete, database) al posto del thread dell'event loop.
- **Callback**: al termine dell'operazione la callback torna all'event loop, che può completare la risposta al client.

![[lezione-13-1792513816820.png|300]]

## Installazione

> [!lab]
> Node.js si può installare in tre modi:
> 
> - **Installer ufficiali** disponibili sul sito web del progetto.
> - **Package manager** di sistema.
> - **Version manager** come `nvm`, `nvs` o `nvm4w`, comodi per sperimentare versioni diverse e passare frequentemente dall'una all'altra.
> 
> La corretta installazione si verifica con `node --version`, che stampa la versione di Node.js in uso.

## Node.js vs browser

L'ambiente di esecuzione determina gli oggetti e le API disponibili:

- **Ambiente browser**: JavaScript manipola principalmente il DOM, con oggetti e API della piattaforma web come `window`, `document`, Cookies, LocalStorage.
- **Ambiente Node.js**: questi oggetti e API non sono disponibili, ma si possono sfruttare i moduli della standard library per l'accesso al file system e alla rete.
- In Node.js è possibile **leggere e scrivere file** sul filesystem e **ascoltare su una socket** le richieste in arrivo.

## npm

> [!def] npm
> **Node Package Manager**, gestore di pacchetti che fornisce i modi per scaricare e gestire le dipendenze dei progetti Node.js. È uno dei principali motivi del successo di Node.js: a settembre 2022 contava oltre 2,1 milioni di pacchetti, il più grande repository monolinguaggio al mondo, con un pacchetto per quasi tutto.

- npm è installato di default insieme a Node.js; la sua disponibilità si verifica con `npm --version`.
- Un pacchetto npm si crea nella directory corrente con `npm init`, che chiede le informazioni sul pacchetto: nome, versione, repository (se presente), licenza, autore, *entry point* (il primo file JavaScript eseguito) e comando di test (se presente).
- Per creare un pacchetto compatibile con i **moduli ES** si usa `npm init es6`.

### Il file package.json

> [!def] `package.json`
> **File descrittore del pacchetto** generato da `npm init` nella stessa directory: contiene tutte le informazioni sul pacchetto, incluse le dipendenze e i comandi per eseguirlo. È la controparte npm del `pom.xml` di Maven.

Le sue proprietà principali sono:

- **`main`**: file (es. `app.js`) eseguito quando il codice client importa il pacchetto; in genere esporta le variabili e le funzioni pubbliche.
- **`type`**: imposta il pacchetto a modulo ES con il valore `"module"`.
- **`scripts`**: task da riga di comando, eseguibili con `npm <taskname>`; il task `test` è definito di default, mentre un task `start` si aggiunge modificando la proprietà.

```json
{
  "name": "hello-web-technologies",
  "version": "0.0.1",
  "main": "app.js",
  "type": "module",
  "scripts": { "start": "node app.js" },
  "dependencies": { "cowsay": "^1.5.0" }
}
```

### Installare le dipendenze

Per installare una dipendenza si esegue `npm install <nomepacchetto>`, con due effetti:

- La dipendenza viene tracciata nella nuova sezione `dependencies` del `package.json`.
- I pacchetti vengono scaricati nella directory `node_modules`, comprese le loro dipendenze ricorsive.

L'importazione di una dipendenza usa la sintassi dei moduli ES:

```js
import cowsay from 'cowsay';
console.log(cowsay.think({ text: 'Hello Web Tech!' }));
```

### Distribuire un pacchetto

Per distribuire un pacchetto npm bastano il codice proprio e il descrittore `package.json`: la directory `node_modules` non va inclusa nel versioning.

Il comando `npm install`, eseguito senza argomenti, installa tutte le dipendenze elencate nel `package.json`.

## Una prima applicazione web

La standard library include il modulo `http`, con cui un server Node.js resta in ascolto su una porta e genera risposte HTML al volo:

```js
import http from 'http';
const PORT = 3000;
http.createServer(function(request, response) {
  response.writeHead(200, { 'Content-Type': 'text/html' });
  response.write('<!DOCTYPE html><html><body><h1>Hello Web Tech</h1></body></html>');
  response.end();
}).listen(PORT);
```

## Debugging in VS Code

> [!lab]
> 
> ### Auto Attach
> 
> L'Auto Attach si attiva e configura così:
> 
> - Il modo più semplice per fare debugging è abilitare la funzione **Auto Attach**, che collega automaticamente un debugger ai processi Node.js avviati da VS Code.
> - Si attiva con `CTRL+SHIFT+P` aprendo la palette dei comandi e cercando «Toggle Auto Attach».
> - La modalità **Smart** collega il debugger solo agli script eseguiti fuori da `node_modules`.
> 
> A debugging avviato si lavora così:
> 
> - I **breakpoint** si aggiungono cliccando accanto al numero di riga; quando l'esecuzione li raggiunge, il codice si mette in pausa.
> - Il pannello **Run and Debug** permette di ispezionare le variabili, osservare espressioni (*watch*), consultare lo *call stack* e altro, in modo più efficace del debugging via `console.log`.
> 
> ### Azioni di debug
> 
> Le **debugging actions** permettono un controllo fine del flusso di esecuzione:
> 
>
>
> | Azione | Descrizione |
> | --- | --- |
> | Resume | Riprende il normale flusso di esecuzione, fino al prossimo breakpoint |
> | Step Over | Esegue l'istruzione successiva come unità singola, senza ispezionarne i passaggi interni |
> | Step Into | Entra nell'istruzione successiva per seguirne l'esecuzione riga per riga |
> | Step Out | Da dentro un metodo, completa il metodo corrente come un unico comando e torna al contesto precedente |
> | Restart | Termina l'esecuzione e riavvia il debugging con la configurazione corrente (non funziona con Auto Attach) |
> | Disconnect | Termina la sessione di debug corrente |
> 
> ## Live reloading
> 
> A ogni modifica del codice l'intero server va riavviato manualmente (`npm start`, `node app.js`, ...), il che rende lo sviluppo poco agevole.
> 
> - Le utility di **live reloading** monitorano il codebase e riavviano il server di sviluppo quando serve.
> - **nodemon** è una di queste utility: si installa con `npm install nodemon` e si usa sostituendo `node app.js` con `nodemon app.js`.

