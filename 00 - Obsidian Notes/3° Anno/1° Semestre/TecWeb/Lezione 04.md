# Lezione 4 : HTML: Hypertext Markup Language

## Contesto: server HTTP e web

- Un **server HTTP** è un software in ascolto di richieste HTTP su una certa porta (es. 80).
- Può gestire più host virtuali: per questo le richieste HTTP contengono un header **Host**.
- Serve le richieste leggendo file dal **Document root** del proprio filesystem, in modo che non tutti i file locali siano accessibili via HTTP.

## HTML: linguaggio di markup

- I browser visualizzano **documenti** descritti in HTML; una **web app** è composta da uno o più documenti (pagine web).
- Un **linguaggio di markup** arricchisce un documento con annotazioni che ne controllano struttura, formattazione o le relazioni tra le parti.
- In HTML le annotazioni sono i **tag**, delimitati da parentesi angolari; i tag di apertura possono contenere **attributi** chiave-valore (valore opzionale), nella forma `<tagName attr1="value" attr2>`.
- Ci sono più versioni dal 1993; il riferimento attuale è l'**HTML Living Standard**.

### Struttura del documento

- Il documento inizia con la dichiarazione `<!DOCTYPE HTML>`: non è un tag, indica al client il tipo di documento atteso.
- Il tag `<html>` rappresenta l'intero documento e contiene un `<head>` e un `<body>`; l'attributo **lang** è raccomandato per l'accessibilità.
- Lo `<head>` contiene i **metadati** (dati sul documento, spesso non mostrati all'utente ma utili a browser e motori di ricerca) e deve contenere un `<title>`.
- Lo `<body>` contiene il contenuto effettivo del documento.

> [!def] Attributi globali
> Alcuni attributi sono **globali**, cioè ammessi su qualunque elemento; altri hanno senso solo per alcuni elementi.
> - **id**: identificatore univoco dell'elemento nel documento.
> - **lang**: lingua del contenuto dell'elemento.
> - **style, class**: usati per lo stile.

### Commenti

- I **commenti** sono ignorati dai browser, delimitati da `<!--` e `-->`; servono per note o per nascondere temporaneamente contenuto.

## Elementi fondamentali

### Titoli e paragrafi

- `<h1>`–`<h6>` rappresentano titoli e sottotitoli di livello crescente.
- `<p>` rappresenta un paragrafo, che tipicamente inizia su una nuova riga.

### Semantica a livello di testo

- `<em>` enfatizza il contenuto; `<strong>` indica forte importanza; `<br>` è un elemento *void* che inserisce un'interruzione di riga.
- `<abbr title="...">` definisce acronimi e abbreviazioni.
- `<del>` marca contenuto eliminato dal documento; `<ins>` contenuto inserito.

### Ancore e URL

- I **link** si definiscono con l'ancora `<a>`; l'attributo **href** punta all'URL di destinazione.
- Un URL è composto da **schema** (protocollo), **nome di dominio**, **porta** e **percorso**; può includere una **query string** e un **anchor**.

#### URL assoluti e relativi

- Un **URL assoluto** include schema e hostname e contiene tutte le informazioni per raggiungere la risorsa.
- Un **URL relativo** specifica solo un percorso; schema e hostname sono dedotti dal contesto corrente.
- Un URL relativo che inizia con `/` sostituisce l'intero percorso; altrimenti sostituisce solo l'ultimo segmento del percorso.
- I segmenti **dot** indicano directory: `.` è la directory corrente, `..` la directory padre.

| href | Percorso risultante (da `/a/b/c/hello.html`) |
| --- | --- |
| `./index.html` | `/a/b/c/index.html` |
| `../foo.html` | `/a/b/foo.html` |
| `../../pic.jpg` | `/a/pic.jpg` |

- Le URL relative sono da preferire per link interni alla stessa web app (cambiare l'hostname non richiede modifiche alle pagine); per risorse esterne servono URL assoluti.
- L'attributo **target** specifica dove aprire la risorsa: `_self` (default) nella stessa scheda, `_blank` in una nuova scheda/finestra.

#### Anchor e index.html

- Un **anchor** (`#id`) è un "segnalibro" dentro la risorsa: indica al browser di mostrare il contenuto in corrispondenza dell'elemento con quell'`id`.
- Quando un URL punta a una directory, il server risponde tipicamente con il file `index.html` in essa (comportamento configurabile: anche `home.html`, `default.htm`, o generazione automatica di un indice).

### Tabelle

- `<table>` contiene righe `<tr>`; ogni riga contiene celle `<td>` o intestazioni `<th>`.
- `<thead>`, `<tbody>` e `<tfoot>` raggruppano rispettivamente intestazioni di colonna, righe di dati e righe di riepilogo; `<caption>` descrive la tabella nel suo insieme.

### Liste

- **Liste ordinate** `<ol>`: per enumerazioni.
- **Liste non ordinate** `<ul>`: per elenchi puntati; entrambe contengono elementi `<li>`.
- **Liste di descrizione** `<dl>`: coppie di termine `<dt>` e descrizione `<dd>`, spesso usate per glossari.

### Riferimenti di carattere

- Alcuni caratteri (es. `<`, `>`) sono **riservati** in HTML: per visualizzarli si usano i **riferimenti di carattere** (entità) nella forma `&nome;` o `&#numero;`.

| Risultato | Riferimento |
| --- | --- |
| Spazio non separabile | `&nbsp;` |
| `<` | `&lt;` |
| `>` | `&gt;` |
| `&` | `&amp;` |
| `"` | `&quot;` |
| `'` | `&#x27;` |
| © | `&copy;` |

### Immagini

- `<img>` è un elemento *void* che incorpora un'immagine: **src** specifica l'URL, **alt** il testo alternativo, **width**/**height** le dimensioni in pixel.
- L'attributo **alt** fornisce un sostituto testuale dell'immagine e deve trasmetterne significato o funzione: un'immagine informativa richiede un alt significativo, una decorativa usa `alt=""`, un'immagine che è l'unico contenuto di un link deve descriverne la destinazione.
- Un'immagine è contenuto esterno di cui il documento ha solo l'URL: il browser, parsando il documento dall'alto verso il basso, deve recuperare risorse aggiuntive per visualizzarlo.

## Form

- Gli elementi `<form>` raccolgono input dell'utente, tipicamente inviati a un server per l'elaborazione; contengono controlli come `<input>`, `<label>`, `<textarea>`, `<select>`.
- `<label>` etichetta un controllo: buona pratica di usabilità e accessibilità; il suo attributo **for** deve coincidere con l'`id` del controllo.

### Controlli di input

- Il tipo di `<input>` è definito dall'attributo **type**: `text`, `password`, `number`, `radio` (una scelta tra molte), `checkbox` (zero o più scelte), `submit` (pulsante), oltre a tipi dedicati a date e orari (`date`, `week`, `month`, `time`, `datetime-local`) e altri (color picker, file picker, datalist…).
- `<select>` definisce menu a tendina con `<option>`; l'attributo **multiple** permette la selezione multipla.
- `<fieldset>` raggruppa controlli correlati, con `<legend>` come etichetta del gruppo.
- L'attributo **disabled** fa sì che un controllo sia ignorato durante l'invio.

### Invio (submission)

- Alla sottomissione si genera una nuova richiesta HTTP verso il **form-handler** indicato dall'attributo **action** (default: la pagina corrente); l'attributo **method** indica il metodo HTTP (default: GET).
- I dati raccolti formano il **form data set**: coppie nome/valore `name1=value1&...&nameN=valueN`, dove il nome è l'attributo **name** di ciascun controllo e il valore il suo contenuto all'atto dell'invio.
- Con **GET** i dati sono accodati alla URL del handler come **query string** (`/handler.html?msg=Hello!&num=42`): i nomi sono detti **query parameters**, coppie chiave/valore separate da `&`, che il server può usare prima di restituire la risorsa.
- Con **POST** i dati sono inviati nel corpo della richiesta.
- La **URL encoding** sostituisce i caratteri speciali con terne `%XX`, dove XX sono due cifre esadecimali che rappresentano il carattere ASCII (gli spazi diventano `%20` o `+`).

#### Controlli "successful"

- Il form data set è costruito raccogliendo solo i controlli **successful**: definiti dentro un `<form>`, con attributo `name`, non disabilitati.
- Con più pulsanti di invio, solo quello attivato è successful; tutte le checkbox selezionate sono successful; tra radio button con lo stesso `name`, solo quella selezionata lo è.

### Validazione nativa

- I browser moderni hanno **validazione integrata**: verificano vincoli sull'input e bloccano l'invio se non soddisfatti.
- Vincoli esprimibili con attributi: **type** (tipo atteso), **required** (valore non vuoto), **minlength/maxlength** (lunghezza del testo), **min/max/step** (numeri e date), **pattern** (espressione regolare da rispettare).

> [!warning] La validazione HTML non è sicurezza
> La validazione gira nel browser dell'utente, che potrebbe usare un browser senza validazione, modificare l'HTML con le DevTools o inviare richieste HTTP direttamente: un client malintenzionato può inviare qualunque valore. Restano comunque utili per intercettare gli errori presto e migliorare l'esperienza utente.

## Organizzazione del contenuto

- Il contenuto di una pagina può essere raggruppato con **divisioni** `<div>` (nessuna semantica oltre al raggruppamento) o con **tag semantici**, che descrivono il significato del contenuto a browser, sviluppatori e software.
- `<nav>` contiene link di navigazione; `<main>` il contenuto principale; `<article>` contenuto indipendente e autonomo; `<aside>` contenuto tangenzialmente correlato; `<header>`, `<footer>`, `<section>` autoesplicativi.
- Un documento HTML è un **albero**: `html` è la radice, con figli `head` e `body`; il nesting di elementi definisce la gerarchia.

![Struttura ad albero di un documento HTML](https://cdn-mineru.openxlab.org.cn/result/2026-09-29/b3a92b72-21ce-4049-937b-de0d1d0cdf5d/6c31009ea4e2a7d20f2638d6c4bea84d6ecdda98bd6b24ad46f36e6259cb53a5.jpg)

## Errori HTML e recupero dei browser

- I browser cercano di visualizzare la pagina anche in presenza di errori (**tag soup**): chiudono automaticamente tag non chiusi, aggiungono markup mancante, correggono entità e problemi strutturali.
- Questo può mascherare errori durante l'apprendimento: una pagina visualizzata correttamente non implica HTML sintatticamente o semanticamente corretto; conviene usare linter (es. HTMLHint) o validatori online (es. validator.w3.org/nu).

## DevTools

- La scheda "Inspector"/"Analisi pagina" dei DevTools del browser permette di ispezionare l'HTML del documento e modificarlo **localmente**, cioè solo nella copia caricata nel browser, non sul server.