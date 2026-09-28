# Lezione 05 — HTML: Hypertext Markup Language

## HTML e il web

- Il **web** è un sistema di documenti **ipertesto** interconnessi tramite **hyperlink**; i client (tipicamente browser) usano HTTP per recuperarli.
- Un **server HTTP** è un software in ascolto di richieste su una porta, che può gestire più host (da qui l'header **Host**) e serve i file a partire dalla **document root** del proprio filesystem.
- Una **Web App** consiste di uno o più documenti (pagine web), descritti in HTML e visualizzati dal browser.

> [!def] Linguaggio di markup
> Un **linguaggio di markup** arricchisce un documento con annotazioni (i **tag**, racchiusi tra parentesi angolari) che ne controllano la **struttura**, la **formattazione** o le **relazioni tra le parti**. I tag di apertura possono contenere **attributi** chiave-valore, con valore opzionale.

- HTML esiste in diverse versioni dal 1993; il riferimento attuale è l'**HTML Living Standard**.

## Struttura di un documento HTML

- La dichiarazione **`<!DOCTYPE HTML>`** non è un tag ma comunica al client il tipo di documento atteso.
- Il tag **`<html>`** rappresenta l'intero documento e contiene un `<head>` e un `<body>`; l'attributo **`lang`** è raccomandato per l'accessibilità.
- Il **`<head>`** è un contenitore di **metadati**: dati sul documento, spesso non mostrati all'utente ma utili a browser e motori di ricerca; deve contenere un `<title>`.
- Il **`<body>`** contiene i contenuti effettivi del documento.
- I **commenti** sono ignorati dai browser e servono per note o per nascondere temporaneamente contenuto.

## Elementi principali

### Titoli e paragrafi

- **`<h1>`–`<h6>`**: rappresentano titoli e sottotitoli, dal livello più alto al più basso.
- **`<p>`**: rappresenta un paragrafo, che tipicamente inizia su una nuova riga.

### Semantica a livello di testo

- **`<em>`**: enfatizza il contenuto; **`<strong>`**: forte importanza.
- **`<br>`**: interruzione di riga (**void element**, cioè senza contenuto).
- **`<abbr>`**: definisce acronimi e abbreviazioni, con la descrizione nell'attributo `title`.
- **`<del>` e `<ins>`**: contenuti rispettivamente eliminati o inseriti nel documento.

### Ancore e URL

- Gli **hyperlink** si definiscono con il tag ancora **`<a>`**, il cui attributo **`href`** indica l'URL di destinazione.
- L'attributo **`target`** specifica dove aprire la risorsa collegata: `_self` nella stessa finestra/scheda (default), `_blank` in una nuova finestra/scheda.
- L'attributo **`id`** degli elementi può essere usato negli **anchor** di URL: il **fragment** (`#id`) è un segnaposto interno alla risorsa che dice al browser di mostrare il contenuto in quel punto.

#### URL assoluti e relativi

- Un **URL assoluto** include scheme e hostname e contiene tutto il necessario per raggiungere la risorsa.
- Un **URL relativo** specifica solo un path; scheme e hostname sono dedotti dal contesto corrente.
- Se un URL relativo inizia con `/`, l'intero path è sostituito; altrimenti è sostituito solo l'ultimo segmento del path corrente.
- I **dot segments** modificano il path: `.` indica la directory corrente, `..` la directory padre.

> [!info] Quando usare URL relativi
> Le URL relative sono da preferire per risorse **interne** alla stessa web app, perché un cambio di hostname non richiede modifiche alle pagine; per risorse **esterne** servono necessariamente URL assoluti.

#### Directory index

- Se un URL punta a una directory, il server risponde tipicamente col file **`index.html`** presente in essa.
- Il nome di default è configurabile (altri usati: `home.html`, `default.html`); in assenza di file di default, il server può generare automaticamente un indice della directory.

### Tabelle

- **`<tr>`**: una riga, contenente celle **`<td>`** (dati) e/o **`<th>`** (intestazioni).
- **`<thead>`**: raggruppa le righe di intestazione; **`<tbody>`**: le righe di dati; **`<tfoot>`**: le righe di pié di pagina (tipicamente riepiloghi).
- **`<caption>`**: descrive la tabella nel suo complesso.

### Liste

- **Lista ordinata** (`<ol>`): enumerazioni.
- **Lista non ordinata** (`<ul>`): elenchi puntati.
- **Lista di descrizione** (`<dl>`): termini e relative descrizioni, usata spesso per glossari.
- Le liste ordinate e non ordinate contengono una sequenza di **`<li>`**; le liste di descrizione contengono termini **`<dt>`** e descrizioni **`<dd>`** dei termini precedenti.

### Riferimenti a caratteri

- Alcuni caratteri sono **riservati** in HTML, perché il browser può confonderli con i tag.
- I **character references** (o **entità**), nella forma `&nome;` o `&#numero;`, permettono di visualizzarli.
- Sono definiti per i caratteri riservati, lo spazio unificatore, le virgolette e simili; l'elenco completo è nella specifica HTML.

### Immagini

- **`<img>`** incorpora un'immagine: è un **void element**.
- **`src`**: specifica l'URL dell'immagine; **`alt`**: descrizione testuale alternativa; **`width`/`height`**: dimensione in pixel.
- L'attributo **`alt`** è un sostituto testuale che deve esprimere il significato o lo scopo dell'immagine: sostituendo mentalmente l'immagine con il suo testo, la pagina deve comunicare la stessa informazione.
- Le descrizioni generiche (es. "immagine") non devono essere usate: lo scopo è far trasmettere agli **screen reader** lo stesso significato o funzione agli utenti che non vedono le immagini.

#### Testo alt in base allo scopo

- Un'immagine **informativa** richiede un testo alternativo significativo.
- Un'immagine puramente **decorativa** deve usare `alt=""` (vuoto).
- Se un'immagine è l'unico contenuto di un link, il suo `alt` deve descrivere la destinazione o lo scopo del link.

#### Dietro le quinte

- I documenti HTML erano finora **autonomi** (self-contained): tutti i dati erano dentro il documento.
- Con `<img>` il contenuto esterno è indicato solo tramite URL: l'immagine non è inclusa nel documento.
- Il browser **parsa il documento dall'alto verso il basso** e deve quindi **recuperare (fetch)** risorse aggiuntive per visualizzarlo.

### Attributi globali

Gli **attributi specifici** (es. `href`, `src`, `alt`) hanno senso solo per alcuni elementi; gli **attributi globali** sono usabili con qualsiasi elemento HTML.
- **`id`**: identificatore **unico** dell'elemento nel documento.
- **`lang`**: lingua del contenuto dell'elemento.
- **`style` e `class`**: usati per lo styling.

## Form

- L'elemento **`<form>`** raccoglie input dell'utente, tipicamente inviati a un server per l'elaborazione; contiene controlli come `<input>`, `<label>`, `<textarea>`, `<select>`.

> [!def] Controlli successful e form data set
> All'atto dell'invio, il **form data set** è costruito raccogliendo tutti i **controlli successful** del form, rappresentati come coppie nome/valore separate da `&`. Ogni nome è il valore dell'attributo **`name`** di un input; il valore è quello assunto al momento dell'invio.

#### Condizioni per un controllo successful

- Deve essere definito dentro un `<form>` e avere un attributo **`name`**.
- Un controllo **`disabled`** non può essere successful, perché è ignorato nell'invio.
- Se ci sono più pulsanti di invio, solo quello attivato è successful.
- Tutte le checkbox selezionate ("on") possono essere successful.
- Per i **radio button** con lo stesso `name`, solo quello selezionato può essere successful.
- L'algoritmo completo è nell'HTML Living Standard.

### Controlli di input

- I tipi di **`<input>`** sono selezionati con l'attributo **`type`**: `text` (testo a riga singola), `password` (input nascosto con `***`), `number`, `radio` (una scelta su molte), `checkbox` (da zero a molte scelte), `button` (pulsante cliccabile).
- Esistono tipi dedicati a **date e tempi**: `date`, `week`, `month`, `time`, `datetime-local`.
- **`<select>`** definisce menu a tendina con **`<option>`**; l'attributo **`multiple`** permette di selezionare più opzioni.
- Esistono altri tipi di input (es. selettore di colore, file picker, datalist); il riferimento completo è nella documentazione MDN.

### Label e raggruppamento

- **`<label>`** etichetta un input: l'attributo **`for`** deve valere l'`id` dell'input corrispondente; usarle è una buona pratica di usabilità e accessibilità.
- **`<fieldset>`** raggruppa logicamente i controlli, con **`<legend>`** come titolo/caption del gruppo.

### Invio del form

- L'attributo **`action`** specifica l'URL del **form-handler** a cui inviare i dati (default: la stessa pagina del form).
- L'attributo **`method`** specifica il metodo HTTP (default: `GET`); all'invio viene tipicamente eseguita una nuova richiesta HTTP.
- Con **`GET`** gli input sono **appesi all'URL** del handler come **query string**: coppie chiave/valore (`?chiave=valore&...`), i cui elementi si chiamano **query parameters**.
- I **query parameters** sono parametri extra passati al server, che può usarli prima di restituire la risorsa.
- Con **`POST`** gli input sono **inviati nel body** della richiesta.

### URL encoding

- Se l'input contiene caratteri speciali (es. `&`), questi sono sostituiti da terne della forma **`%XX`**, dove `XX` sono due cifre esadecimali che rappresentano il carattere in ASCII.
- Gli spazi possono essere sostituiti con `%20` o con il simbolo `+`.

### Validazione nativa dei form

- I browser moderni hanno capacità di **validazione integrata**: verificano che l'input rispetti certi vincoli e bloccano l'invio in caso contrario.
- L'attributo **`type`** definisce il tipo di valore atteso; **`required`** impedisce l'invio di valori vuoti.
- **`minlength`/`maxlength`**: vincolano la lunghezza del testo.
- **`min`/`max`/`step`**: vincolano numeri e date.
- **`pattern`**: il testo deve corrispondere a un'espressione regolare.

> [!warning] La validazione HTML non è sicurezza
> La validazione HTML gira **nel browser dell'utente**: l'utente potrebbe usare un browser senza validazione, modificare l'HTML con le Dev Tools o bypassare il form inviando richieste HTTP direttamente; un client malintenzionato può inviare qualunque valore. Non fidarsi **solo** della validazione HTML, che resta comunque utile per intercettare gli errori presto e migliorare l'esperienza utente.

## Organizzazione del contenuto

- Il contenuto di una pagina può essere **raggruppato** in parti usando le divisioni **`<div>`** o **tag semantici**.
- **`<div>`**: era il modo principale di raggruppare contenuto prima dell'introduzione dei tag semantici; non porta alcuna semantica specifica oltre al raggruppare contenuti tra loro correlati.
- I **tag semantici** descrivono il **significato** del contenuto a browser, sviluppatori e software.

#### Tag semantici principali

- **`<nav>`**: link di navigazione.
- **`<main>`**: contenuto principale.
- **`<article>`**: contenuto indipendente e autonomo.
- **`<aside>`**: contenuto tangenzialmente correlato.
- **`<header>`**, **`<footer>`**, **`<section>`**: rispettivamente intestazione, pié di pagina e sezione tematica.

## Il modello ad albero

- La struttura nidificata di un documento HTML lo costituisce naturalmente come un **albero**: gli elementi contengono altri elementi, fino ai **nodi di testo** foglia.

> [!info] I browser recuperano dagli errori HTML
> I browser cercano di visualizzare la pagina anche in presenza di errori (chiusura automatica di tag mai chiusi, aggiunta di markup mancante, correzione di entità e problemi strutturali), nascondendo però gli errori a chi sta imparando. Una pagina visualizzata correttamente **non** implica HTML sintatticamente o semanticamente corretto: per verificarlo servono linter dedicati e validatori online.

## Dev Tools del browser

- La scheda **Inspector** ("Analisi pagina") consente di ispezionare il contenuto HTML di un documento e modificarlo **localmente**.
- "Localmente" significa modificare la pagina caricata nel browser, **non** il contenuto dell'HTML memorizzato sul server web.