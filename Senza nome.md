# HTML — Hypertext Markup Language

## HTML e il web

- Il **web** è un sistema di documenti **ipertesto** interconnessi tramite **hyperlink**, recuperati dai client (browser) tramite HTTP.
- Un **server HTTP** è un software in ascolto su una porta che può servire più host (da qui l'header **Host**) e distribuisce i file a partire dalla **document root** del proprio filesystem.
- Una **Web App** consiste di una o più pagine web, descritte in HTML e visualizzate dal browser.

> [!def] Linguaggio di markup
> Un **linguaggio di markup** arricchisce un documento con annotazioni (**tag**, tra parentesi angolari) che ne controllano struttura, formattazione o relazioni tra le parti; i tag di apertura possono contenere **attributi** chiave-valore con valore opzionale.

- HTML esiste dal 1993 in diverse versioni; il riferimento attuale è l'**HTML Living Standard**.

## Struttura di un documento HTML

- La dichiarazione **`<!DOCTYPE HTML>`** non è un tag: comunica al client il tipo di documento atteso.
- Il tag **`<html>`** rappresenta l'intero documento e contiene `<head>` e `<body>`; l'attributo **`lang`** è raccomandato per l'accessibilità.
- Il **`<head>`** contiene **metadati** (dati sul documento, utili a browser e motori di ricerca) e deve contenere un `<title>`.
- Il **`<body>`** contiene i contenuti effettivi del documento.
- I **commenti** sono ignorati dai browser e servono per note o per nascondere temporaneamente contenuto.

## Elementi principali

### Titoli, paragrafi e testo

- **`<h1>`–`<h6>`**: titoli e sottotitoli, dal livello più alto al più basso.
- **`<p>`**: paragrafo, che tipicamente inizia su una nuova riga.
- **`<em>`**: enfasi; **`<strong>`**: forte importanza.
- **`<br>`**: interruzione di riga (**void element**, senza contenuto).
- **`<abbr>`**: acronimi e abbreviazioni, con la descrizione nell'attributo `title`.
- **`<del>`** e **`<ins>`**: contenuti rispettivamente eliminati o inseriti.

### Ancore e URL

- Gli hyperlink si definiscono con il tag ancora **`<a>`**; l'attributo **`href`** indica l'URL di destinazione.
- Un URL è **assoluto** se include scheme e hostname (contiene tutto il necessario per la risorsa), **relativo** se specifica solo un path (scheme e hostname dedotti dal contesto).
- Un URL relativo che inizia con `/` sostituisce l'intero path; altrimenti solo l'ultimo segmento del path corrente.
- I **dot segments** modificano il path: `.` è la directory corrente, `..` la directory padre.
- Per risorse **interne** alla web app si preferiscono URL relativi (un cambio di hostname non richiede modifiche); per risorse **esterne** servono URL assoluti.
- L'attributo **`target`** specifica dove aprire la risorsa: `_self` (stessa finestra/scheda, default) o `_blank` (nuova finestra/scheda).
- Se un URL punta a una directory, il server risponde tipicamente col file `index.html` (altri default configurabili: `home.html`, `default.html`); in assenza, può generare un indice della directory.
- L'attributo **`id`** negli **anchor** di URL (fragment `#id`) è un segnaposto interno che dice al browser di mostrare il contenuto in quel punto.

### Tabelle

- **`<tr>`**: una riga, con celle **`<td>`** (dati) e/o **`<th>`** (intestazioni).
- **`<thead>`**/**`<tbody>`**/**`<tfoot>`**: raggruppano rispettivamente righe di intestazione, di dati e di piè di pagina (riepiloghi).
- **`<caption>`**: descrive la tabella nel suo complesso.

### Liste

- Tre tipi di liste: **ordinate** (`<ol>`, enumerazioni), **non ordinate** (`<ul>`, elenchi puntati) e **di descrizione** (`<dl>`, termini e descrizioni, es. glossari).
- `<ol>` e `<ul>` contengono una sequenza di **`<li>`**; `<dl>` contiene termini **`<dt>`** e descrizioni **`<dd>`** dei termini precedenti.

### Riferimenti a caratteri

- I caratteri **riservati** (confondibili con i tag) si visualizzano tramite **character references** (o **entità**), nella forma `&nome;` o `&#numero;`.
- Sono definiti per caratteri riservati, spazio unificatore, virgolette e simili; l'elenco completo è nella specifica HTML.

### Immagini

- **`<img>`** incorpora un'immagine: è un void element; **`src`** è l'URL dell'immagine, **`alt`** la descrizione testuale alternativa, **`width`/`height`** la dimensione in pixel.
- **`alt`** è un sostituto testuale che deve esprimere significato o scopo dell'immagine: sostituendo mentalmente l'immagine col suo testo, la pagina deve comunicare la stessa informazione.
- Non usare descrizioni generiche: lo scopo è far trasmettere dagli screen reader lo stesso significato o funzione a chi non vede le immagini.

> [!info] Testo alt in base allo scopo
> - Immagine **informativa** → testo alternativo significativo.
> - Immagine **decorativa** → `alt=""` (vuoto).
> - Immagine che è l'unico contenuto di un link → `alt` che descrive la destinazione o lo scopo del link.

> [!info] Dietro le quinte
> I documenti HTML erano finora **autonomi** (self-contained). Con `<img>` il contenuto esterno è indicato solo tramite URL: l'immagine non è inclusa nel documento, quindi il browser, che **parsa dall'alto verso il basso**, deve **recuperare (fetch)** risorse aggiuntive per visualizzarlo.

### Attributi globali

- Gli attributi specifici (es. `href`, `src`, `alt`) valgono solo per alcuni elementi; gli **attributi globali** sono usabili con qualsiasi elemento.
- **`id`**: identificatore **unico** dell'elemento nel documento; **`lang`**: lingua del contenuto; **`style`** e **`class`**: usati per lo styling.

## Form

- L'elemento **`<form>`** raccoglie input dell'utente, tipicamente inviati a un server; contiene controlli come `<input>`, `<label>`, `<textarea>`, `<select>`.

> [!def] Controlli successful e form data set
> All'invio, il **form data set** è costruito raccogliendo tutti i **controlli successful** del form: coppie nome/valore separate da `&`, dove il nome è l'attributo `name` di un input e il valore è quello assunto al momento dell'invio.

**Condizioni per un controllo successful:**
- Deve essere definito dentro un `<form>` e avere un attributo **`name`**.
- Un controllo **`disabled`** non è successful (ignorato nell'invio).
- Con più pulsanti di invio, solo quello attivato è successful.
- Tutte le checkbox selezionate possono essere successful.
- Per i radio button con lo stesso `name`, solo quello selezionato è successful.
- L'algoritmo completo è nell'HTML Living Standard.

### Controlli di input

- Il tipo di `<input>` è selezionato con **`type`**: `text`, `password` (input nascosto con `***`), `number`, `radio` (una scelta su molte), `checkbox` (da zero a molte scelte), `button`.
- Tipi dedicati a **date e tempi**: `date`, `week`, `month`, `time`, `datetime-local`.
- **`<select>`** definisce menu a tendina con `<option>`; l'attributo `multiple` permette selezioni multiple.
- Esistono altri tipi (es. selettore di colore, file picker, datalist); riferimento completo nella documentazione MDN.

### Label e raggruppamento

- **`<label>`** etichetta un input: l'attributo **`for`** deve valere l'`id` dell'input corrispondente; usarle è una buona pratica di usabilità e accessibilità.
- **`<fieldset>`** raggruppa logicamente i controlli, con **`<legend>`** come titolo/caption del gruppo.

### Invio del form

- L'attributo **`action`** specifica l'URL del **form-handler** a cui inviare i dati (default: la stessa pagina del form).
- L'attributo **`method`** specifica il metodo HTTP (default: `GET`); all'invio si esegue tipicamente una nuova richiesta HTTP.
- Con **`GET`** gli input sono **appesi all'URL** del handler come **query string** (`?chiave=valore&...`), i cui elementi sono i **query parameters**: parametri extra che il server può usare prima di restituire la risorsa.
- Con **`POST`** gli input sono **inviati nel body** della richiesta.

### URL encoding

- I caratteri speciali nell'input (es. `&`) sono sostituiti da terne `%XX`, dove `XX` sono due cifre esadecimali che rappresentano il carattere in ASCII.
- Gli spazi possono essere sostituiti con `%20` o con il simbolo `+`.

### Validazione nativa dei form

- I browser moderni hanno **validazione integrata**: verificano vincoli sull'input e bloccano l'invio in caso di errore.
- **`type`** definisce il tipo di valore atteso; **`required`** impedisce l'invio di valori vuoti.
- Vincoli comuni: **`minlength`/`maxlength`** (lunghezza del testo), **`min`/`max`/`step`** (numeri e date), **`pattern`** (espressione regolare).

> [!warning] La validazione HTML non è sicurezza
> La validazione gira **nel browser dell'utente**: si può usare un browser senza validazione, modificare l'HTML con le Dev Tools o bypassare il form inviando richieste HTTP direttamente; un client malintenzionato può inviare qualunque valore. Non fidarsi **solo** della validazione HTML — utile comunque per intercettare errori presto e migliorare l'esperienza utente.

## Organizzazione del contenuto

- Il contenuto può essere **raggruppato** con le divisioni **`<div>`** o con **tag semantici**.
- **`<div>`**: modo principale di raggruppare prima dei tag semantici; non porta semantica specifica oltre al raggruppare contenuti correlati.
- I **tag semantici** descrivono il **significato** del contenuto a browser, sviluppatori e software: `<nav>` (link di navigazione), `<main>` (contenuto principale), `<article>` (contenuto indipendente e autonomo), `<aside>` (contenuto tangenzialmente correlato), oltre a `<header>`, `<footer>`, `<section>`.

## Il modello ad albero

- La struttura nidificata di un documento HTML lo costituisce naturalmente come un **albero**: gli elementi contengono altri elementi, fino ai nodi di testo foglia.

> [!info] I browser recuperano dagli errori HTML
> I browser cercano di visualizzare la pagina anche in presenza di errori (chiusura automatica di tag, aggiunta di markup mancante, correzione di entità e problemi strutturali), nascondendo però gli errori a chi impara. Una pagina visualizzata correttamente **non** implica HTML corretto: per verificarlo servono linter dedicati e validatori online.

## Dev Tools del browser

- La scheda **Inspector** ("Analisi pagina") consente di ispezionare l'HTML di un documento e modificarlo **localmente**.
- "Localmente" significa modificare la pagina caricata nel browser, **non** l'HTML memorizzato sul server web.
