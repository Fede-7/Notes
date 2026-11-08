# Guida alla lettura

Questa dispensa segue gli argomenti e la progressione delle **lezioni di Tecnologie Web** del PDF fornito (146 pagine). Lo scopo è imparare a **definire i concetti, spiegare i meccanismi, confrontare approcci e interpretare semplici frammenti di codice**: non soltanto memorizzare parole chiave. Sono mantenute anche distinzioni facilmente oggetto di domanda d'esame. Gli esempi sono illustrativi e non sostituiscono le esercitazioni pratiche. La lezione 14 del materiale di partenza è dedicata soprattutto a esercizi di ripasso e alla traccia del progetto: per questa ragione non compare come capitolo teorico autonomo.

> [!info] Metodo di studio
> Per ciascuna sezione saper rispondere a tre domande: *che cos'è?*, *come funziona?*, *quando e perché lo si usa?*. I riquadri **Da ricordare** individuano differenze e errori ricorrenti. La terminologia tecnica inglese resta presente accanto a quella italiana.

# Parte I - DNS

## 1. Domain Name System

### Definizione, nomi e gerarchia

**DNS (Domain Name System)**: database **distribuito e gerarchico** di Internet che associa a un nome informazioni descritte tramite *resource record* (RR). Non associa necessariamente un nome a un computer: un nome può identificare servizi, alias, server di posta o nodi amministrativi. DNS non è una semplice rubrica centralizzata.

Un **nome DNS** è una sequenza di **etichette** separate da punti, lette in senso gerarchico **da destra a sinistra**. In `informatica.dieti.unina.it.` la gerarchia è: radice `.` → `it` → `unina` → `dieti` → `informatica`. La radice corrisponde all'etichetta vuota finale; i nomi sono **case-insensitive**. Un nome completo terminato dal punto è un *fully qualified domain name* (FQDN). Uno stesso host può possedere più nomi.

**Dominio**: nodo dell'albero dei nomi insieme a tutto il suo sottoalbero. **Zona**: porzione del namespace di cui uno o più name server pubblicano autoritativamente i record. **Delega**: trasferimento dell'autorità su un sottoalbero ad altri name server. Se `unina.it` delega `dieti.unina.it`, quest'ultimo resta nel **dominio** `unina.it`, ma non nella **zona** `unina.it`.

Un **name server autoritativo** contiene e distribuisce dati delle zone per cui è responsabile; può servire molte zone e una zona può avere più server autoritativi, anche per ridondanza. Un **resolver ricorsivo** interroga i server necessari fino a ricostruire una risposta, spesso riutilizzando cache.

### Resource record e attori

Un record DNS contiene: **owner name** (nome a cui si riferisce), **TTL** (*time to live*, durata in secondi della copia in cache), **class** (di norma `IN`), **type** (natura del record) e **value** (dato). Esempio: `www.example.org. 3600 IN A 192.0.2.5`.

| Record | Significato principale |
| --- | --- |
| `A` / `AAAA` | Associa un nome rispettivamente a un indirizzo IPv4 / IPv6. |
| `CNAME` | Crea un alias verso un nome canonico, **non** direttamente verso un indirizzo IP. |
| `NS` | Indica i server di nomi autoritativi di una zona/delega. |
| `SOA` | Identifica l'autorità e i metadati di una zona. |
| `MX` | Indica i server di ricezione della posta per un dominio (con priorità). |

**Attori**: l'applicazione o *client* vuole risolvere un nome; lo **stub resolver** del sistema operativo raccoglie la richiesta; il **resolver ricorsivo** (dell'ISP o di un provider) ricerca o recupera dalla propria cache i dati; i **server autoritativi** forniscono record o informazioni sulla delega. L'IP può essere ottenuto anche da meccanismi locali come il file `hosts`, senza una query DNS esterna.

### Ricorsione, iterazione e risposte

- **Query ricorsiva**: chi riceve la query deve procurarsi la risposta finale oppure un errore; è il normale rapporto stub → resolver ricorsivo.

- **Query iterativa**: chi risponde dà la migliore informazione disponibile, anche un **referral** (indicazione di server da interrogare in seguito); il resolver segue i referral verso gli autoritativi.

Una richiesta (*question*) contiene principalmente `QNAME`, `QCLASS` e `QTYPE`. Una risposta presenta **header** (identificativo, flag e stato), **question** (domanda ripetuta), **answer** (RR che rispondono), **authority** (autorità o referral) e **additional** (RR ausiliari, ad esempio indirizzi dei name server indicati).

| Stato | Interpretazione |
| --- | --- |
| `NOERROR` | Query elaborata: **non** garantisce che esista un RR del tipo richiesto. |
| `NXDOMAIN` | Il **nome** richiesto non esiste. |
| `SERVFAIL` | Impossibile completare la risoluzione. |
| `REFUSED` | Il server rifiuta la richiesta. |
| `FORMERR` | Query malformata. |

Con `NOERROR` si distinguono **risposta positiva** (RR in `Answer`), **referral** (deleghe in `Authority`) e **NODATA** (nome esistente ma assenza del tipo di record chiesto). **NODATA non equivale a NXDOMAIN**.

**Risoluzione a cache vuota** (*cold-cache*): per `squids.unina.it` il resolver interroga un server **root**, che indica quelli di `.it`; uno di `.it` indica quelli di `unina.it`; il server di `unina.it` fornisce il record `A` o un'ulteriore delega. In presenza di cache fresche alcuni passaggi sono evitati. Il TTL governa il riuso dei record: un TTL più elevato riduce le interrogazioni ma può ritardare la visibilità delle modifiche. `dig nome A`, `dig nome MX` e `dig +trace nome` consentono di esplorare il processo.

> [!warning] Da ricordare
> *Dominio ≠ zona; resolver ricorsivo ≠ autoritativo; query ricorsiva ≠ iterativa; NXDOMAIN ≠ NODATA; TTL DNS ≠ durata della cache HTTP.*

# Parte II - HTTP

## 2. Fondamenti del Web e di HTTP

**Internet** è la rete globale basata sulla suite TCP/IP; il **World Wide Web** è un sistema di risorse e ipertesti collegati, che usa Internet come infrastruttura. Un **ipertesto** contiene collegamenti (*hyperlink*) ad altri contenuti; **HTML** ne descrive la struttura e **HTTP** la comunicazione.

**HTTP (Hypertext Transfer Protocol)**: protocollo applicativo **client-server**, basato sull'interazione **richiesta-risposta**, che permette di operare su risorse identificate da URL. Nelle versioni 1.1 e 2 usa di norma TCP; HTTP/3 usa QUIC/UDP. La semantica delle richieste resta analoga tra le versioni.

**URL (Uniform Resource Locator)**: riferimento che specifica dove e come raggiungere una risorsa. Forma generale:

```text
scheme://host:porta/percorso?chiave=valore#frammento
```

Componenti: **scheme** (es. `https`), **authority/host**, **porta** (se assente quella predefinita), **path**, **query string** (`?chiave=valore`) e **fragment** (`#...`, di norma elaborato dal client e non inviato nella richiesta HTTP). I nomi si risolvono in IP, ma la risorsa è identificata anche dal percorso e dalla scelta del virtual host.

### Richieste, metodi, intestazioni e risposte

Una richiesta HTTP/1.1 contiene **request line** (`METODO target HTTP/versione`), intestazioni, riga vuota e un eventuale **body**; una risposta contiene **status line**, intestazioni, riga vuota e un eventuale body.

```http
GET /index.html HTTP/1.1
Host: www.example.org

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
```

Una **intestazione** (*header*) è una coppia nome-valore separata da `:`; i nomi sono insensibili a maiuscole/minuscole. `Content-Type` identifica il media type del corpo (`text/html`, `application/json`, ...); `Content-Length` indica i byte del corpo quando applicabile; `Host` identifica il server virtuale desiderato.

| Metodo | Semantica essenziale | Safe? | Idempotente? |
| --- | --- | --- | --- |
| `GET` | Recupera una rappresentazione. | Sì | Sì |
| `HEAD` | Come GET, ma senza corpo della risposta. | Sì | Sì |
| `POST` | Sottopone dati per un'elaborazione/creazione. | No | Non garantito |
| `PUT` | Crea o sostituisce la rappresentazione della risorsa indicata. | No | Sì |
| `PATCH` | Applica modifiche parziali. | No | Non garantito |
| `DELETE` | Elimina la risorsa indicata. | No | Sì |

**Safe**: il client non richiede un cambiamento di stato; **idempotente**: eseguire più volte la stessa operazione ha lo stesso **effetto previsto** che eseguirla una volta (non significa risposte necessariamente identiche). In una REST API questi significati sono importanti.

I codici HTTP sono divisi in cinque famiglie: **1xx** informativi; **2xx** successi (200 OK, 201 Created, 204 No Content); **3xx** redirect/gestione cache (301, 302, 304 Not Modified); **4xx** errori lato richiesta (400, 401, 403, 404, 405, 409); **5xx** errori nel trattamento da parte del server (500, 502, 503). **401** significa credenziali mancanti/non valide; **403** significa che l'identità può essere nota ma l'operazione è vietata.

Un singolo IP può ospitare più **virtual host**: dopo la risoluzione DNS il server ha bisogno dell'header **Host** per distinguere, ad esempio, `shop.example.org` e `docs.example.org` sul medesimo indirizzo IP.

### Statelessness e server HTTP

**HTTP è stateless**: ciascuna richiesta è semanticamente indipendente, e il protocollo non prescrive al server di ricordare lo stato conversazionale del client. Autenticazione persistente, carrello e preferenze richiedono meccanismi applicativi aggiuntivi (cookie, sessioni, token). Ciò **non** impedisce di usare una connessione di trasporto persistente.

**Server HTTP** può significare ruolo client-server, software (Apache/Nginx), processo oppure macchina. Il processo ascolta una porta (tipicamente **80 HTTP**, **443 HTTPS**), riceve richieste, determina la risorsa e produce risposte. Un **server statico** associa URL a file in una **document root** (es. `/var/www`); un **server dinamico** esegue logica applicativa, può accedere a database e costruisce la risposta al momento.

Per provare nomi fittizi in locale si può associare `127.0.0.1 esempio.local` nel file `hosts`. Questo è un override della risoluzione locale: non equivale ad acquistare un dominio DNS pubblico.

## 3. Rappresentazioni, cache, HTTPS e versioni HTTP

### Content negotiation e compressione

Una risorsa può avere **più rappresentazioni** (lingua, formato, codifica). La **content negotiation** permette al client di inviare preferenze mediante `Accept` (MIME type), `Accept-Language`, `Accept-Encoding` e `Accept-Charset`. Il parametro `q` (*quality factor*) esprime una preferenza da **0** a **1**; assenza di `q` implica normalmente 1.

```http
Accept-Language: it-IT,it;q=0.9,en;q=0.8
```

Il server sceglie una rappresentazione disponibile; se nessuna è accettabile può restituire **406 Not Acceptable** (la scelta del fallback dipende dall'applicazione). `Content-Language`, `Content-Type` e `Content-Encoding` descrivono la rappresentazione inviata. La compressione **lossless** (`gzip`, `deflate`, `br`/Brotli) risparmia banda ma richiede CPU; `identity` significa nessuna compressione. La negoziazione è distinta dall'identificazione della risorsa.

### Caching: memorizzazione, freschezza e validazione

**Caching HTTP**: conservazione di risposte per riutilizzarle, riducendo latenza, banda, carico server e migliorando la scalabilità. La cache **privata** (browser) serve un singolo utente; quella **condivisa** (proxy/CDN) può servire più client. I contenuti personali non devono essere riutilizzati tra utenti. La cache deve scegliere **se memorizzare**, **quando riusare direttamente** e **come validare** quando la copia è scaduta.

Principali direttive di **`Cache-Control`**:

| Direttiva | Significato |
| --- | --- |
| `max-age=300` | Durata nominale della freschezza: 300 secondi. |
| `s-maxage=300` | Durata nelle cache condivise (precedenza su `max-age`). |
| `public` / `private` | Consente cache condivise / limita il riuso a cache private. |
| `no-cache` | Può memorizzare, ma **deve validare prima del riuso**. |
| `no-store` | Vietata la memorizzazione. |
| `must-revalidate` | Dopo scadenza impone validazione prima del riuso. |
| `immutable` | Contenuto dichiarato immutabile durante la freschezza. |

Una risposta **fresh** è riusabile secondo le direttive; una **stale** è scaduta e di norma va validata. Le durate si calcolano dai metadati HTTP, non dal tempo di caricamento percepito. Metodi, status e intestazioni determinano la cacheabilità: **GET/HEAD sono candidati comuni, non automaticamente memorizzabili in ogni situazione**; gli altri metodi hanno vincoli diversi.

**Validatore `ETag`**: identificatore opaco di una rappresentazione; il client può mandare `If-None-Match: "v7"`. **`Last-Modified`**: timestamp di modifica, riutilizzato con `If-Modified-Since`. Se il server conferma che la rappresentazione non è cambiata risponde **304 Not Modified**, senza ritrasmetterne il corpo; se è cambiata restituisce **200 OK** con dati nuovi. L'ETag è generalmente più affidabile di una data con granularità limitata.

**`Vary`** evita il riuso errato di rappresentazioni negoziate: `Vary: Accept-Language` segnala che una copia per `it` non è intercambiabile con una per `en`. La chiave di cache dipende quindi anche dagli header elencati in `Vary`.

> [!warning] Da ricordare
> `no-cache` ≠ `no-store`; **freshness** ≠ **validation**; `304` significa «usa il corpo già in cache»; `Vary` non crea varianti, informa le cache su come distinguerle.

### HTTPS, TLS e sicurezza del canale

**HTTPS** conserva la semantica HTTP ma trasmette su un canale protetto da **TLS**. Il server presenta un **certificato digitale** che lega una chiave pubblica a determinati hostname; il client controlla la catena di fiducia, la validità e la corrispondenza del nome; mediante l'handshake si autentica il server e si concordano chiavi per proteggere la comunicazione. Le proprietà principali sono **riservatezza**, **integrità** e **autenticazione del server**.

HTTPS non garantisce che il sito sia benigno, che i contenuti siano veri o che il server sia immune da attacchi. Alcuni metadati di rete, come indirizzi IP, tempi e dimensioni, restano osservabili. Non bisogna confondere la sicurezza **del trasporto** con quella **dell'applicazione**.

### HTTP/1.1, HTTP/2 e HTTP/3

**HTTP/1.1** può mantenere connessioni TCP persistenti; senza multiplexing gli scambi sulle singole connessioni possono essere serializzati, causando attese quando una risposta è lenta. I browser hanno storicamente aperto più connessioni parallele.

**HTTP/2** mantiene la semantica HTTP ma usa **frame binari**, associando richieste e risposte a **stream** indipendenti a livello applicativo. I frame di stream differenti vengono **interleavati** sulla stessa connessione TCP (*multiplexing*). Rimane tuttavia il **TCP head-of-line blocking**: la perdita di un segmento costringe TCP a ritardare la consegna ordinata dei byte successivi, anche se appartengono ad altri stream.

**HTTP/3** usa **QUIC**, protocollo di trasporto basato su UDP che integra TLS 1.3, controllo della congestione, affidabilità e stream indipendenti. La perdita di dati in uno stream non blocca la consegna degli altri come avviene nel singolo flusso ordinato di TCP. QUIC non elimina tutti i ritardi di rete o la congestione, ma elimina questo particolare blocco tra stream.

| Aspetto | HTTP/1.1 | HTTP/2 | HTTP/3 |
| --- | --- | --- | --- |
| Trasporto usuale | TCP | TCP | QUIC/UDP |
| Codifica messaggi | Testuale | Frame binari | Frame su stream QUIC |
| Multiplexing | No, nel modello base | Sì, a livello HTTP | Sì, a livello QUIC |
| HoL tra stream per perdita di pacchetti | Non multiplessa | Possibile per TCP | Evitato tra stream QUIC |

# Parte III - HTML

## 4. HTML e documenti ipertestuali

**HTML (HyperText Markup Language)**: linguaggio di **markup**, non di programmazione, che descrive struttura e significato degli elementi di un documento Web tramite **tag** e **attributi**. Un elemento normalmente ha tag di apertura, contenuto e tag di chiusura; gli elementi **void** (es. `img`, `input`, `br`) non contengono figli. Lo standard moderno è l'**HTML Living Standard**.

### Documento, semantica e URL

```html
<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8">
    <title>Titolo della pagina</title>
  </head>
  <body>
    <!-- contenuto -->
  </body>
</html>
```

`<!doctype html>` seleziona il modo standard del browser; `<html>` contiene **`<head>`** (metadati e `<title>`) e **`<body>`** (contenuto). Attributi globali: **`id`** (identificatore unico), **`class`** (insieme di classi), **`lang`** (lingua), **`style`** (stile inline). I commenti sono `<!-- ... -->`.

**Elementi importanti**: `h1`-`h6` gerarchizzano i titoli; `p` è un paragrafo; `em` segnala enfasi, `strong` forte importanza; `br` forza un'interruzione; `abbr` con `title` espande abbreviazioni; `ins` e `del` segnalano inserzioni e rimozioni. Usare tag **semantici** aiuta accessibilità, ricerca e manutenzione; la resa grafica va gestita principalmente con CSS.

**Link**: `<a href="...">testo</a>` rende il contenuto cliccabile. L'URL è **assoluto** se contiene scheme e host; è **relativo** se la base è desunta dall'URL del documento. Da `/a/b/c/pagina.html`: `foto.jpg` → `/a/b/c/foto.jpg`; `../index.html` → `/a/b/index.html`; `/home` → `/home`. `.` indica la directory corrente e `..` quella superiore. `#id` porta a un frammento del documento; `target="_blank"` apre in un nuovo contesto di navigazione. Per URL e query string occorre rispettare la codifica dei caratteri.

### Liste, tabelle, immagini e struttura semantica

**Liste**: `ul` non ordinata, `ol` ordinata, `li` elemento; `dl`, `dt`, `dd` per coppie termine-descrizione. **Tabelle**: `table`, `tr` (riga), `th` (cella d'intestazione), `td` (cella dati); `caption`, `thead`, `tbody`, `tfoot` danno struttura. `rowspan` e `colspan` fanno occupare più celle. Le tabelle sono per **dati tabulari**, non per posizionare elementi grafici.

**Immagine**: `<img src="..." alt="descrizione" width="..." height="...">`. Il testo alternativo `alt` descrive la funzione o il significato dell'immagine in quel contesto; per un'immagine puramente decorativa si può usare `alt=""`. Dichiarare dimensioni aiuta a prevenire spostamenti di layout durante il caricamento.

**Contenitori e regioni**: `div` e `span` sono generici (rispettivamente contenitore di blocco e porzione inline senza semantica specifica); `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `figure`, `figcaption` esprimono il ruolo delle parti. L'annidamento forma un **albero** e deve rispettare le regole di contenuto degli elementi. I browser possono recuperare HTML non valido, correggendo automaticamente il DOM: la resa visibile non prova che il markup sia corretto.

**Riferimenti di carattere**: `&amp;` per `&`, `&lt;` per `<`, `&gt;` per `>`, `&quot;` per virgolette; possono essere anche numerici (`&#...;`). Sono necessari quando i caratteri hanno significato speciale nel markup.

### Form HTML e submission

Un **form** raccoglie dati da controlli associati e li invia a una destinazione secondo un metodo HTTP:

```html
<form action="/registrazione" method="post">
  <label for="email">Email</label>
  <input type="email" id="email" name="email" required>
  <button type="submit">Invia</button>
</form>
```

`action` è l'endpoint; `method` è generalmente `get` o `post`. Un controllo contribuisce al **form data set** quando è *successful*: in particolare deve essere associato al form, avere l'attributo **`name`**, non essere disabilitato, e soddisfare le regole del proprio tipo (un checkbox non selezionato, per esempio, non invia la propria coppia nome-valore). `id` serve a identificare un elemento e collegarvi una label, ma **non** sostituisce `name` nell'invio. `label` aumenta usabilità e accessibilità; `fieldset`/`legend` raggruppano controlli.

Controlli: `input` (`text`, `password`, `email`, `number`, `checkbox`, `radio`, `file`, `hidden`, `date`, ...), `textarea`, `select` e `option`, `button`. Proprietà quali `required`, `min`, `max`, `pattern` possono eseguire validazione **client-side**.

- **GET**: normalmente i campi sono codificati nella query string dell'URL; adatto a ricerche senza effetti laterali e dati non sensibili.

- **POST**: dati nel body; adatto ad azioni/creazioni e invii più complessi. Per default il form usa `application/x-www-form-urlencoded`; per file upload si usa spesso `multipart/form-data`.

- **URL encoding**: caratteri riservati sono percent-encoded; in `application/x-www-form-urlencoded` gli spazi possono apparire come `+`.

> [!warning] Da ricordare
> Un input con `id` ma senza `name` non compare normalmente nei dati inviati. `disabled` esclude il campo dalla submission; `readonly` non lo esclude. **La validazione HTML non è una misura di sicurezza:** il server deve convalidare sempre i dati ricevuti. I **DevTools** (Elements, Network, Console) permettono di esaminare DOM, richieste, risposte e comportamento.

# Parte IV - CSS

## 5. CSS: regole, selettori e cascata

**CSS (Cascading Style Sheets)**: linguaggio di dichiarazioni con cui si definisce la **presentazione** dei documenti HTML (colore, tipografia, dimensioni, layout). Il browser possiede stili di default (*user-agent stylesheet*). CSS si inserisce con fogli esterni (`<link rel="stylesheet">`, preferibili per riuso), con `<style>` oppure con attributo `style` sui singoli elementi.

Una regola comprende un **selettore** e un blocco di dichiarazioni `proprietà: valore;`:

```css
p.note {
  color: darkslategray;
  font-weight: bold;
}
```

**Selettori semplici**: tag (`p`), universale (`*`), classe (`.note`), ID (`#main`), attributo (`[disabled]`, `[type="email"]`, `[href^="https"]`, `[href$=".pdf"]`, `[class~="tag"]`). **Selettore composto**: concatenazione che riguarda lo stesso elemento (`p.warning`). **Combinatori**: spazio `A B` (discendente), `A > B` (figlio diretto), `A + B` (fratello immediatamente successivo), `A ~ B` (fratelli successivi). **Lista**: `A, B` applica la regola a entrambi.

**Pseudo-classi**: selezionano uno stato o una posizione, ad esempio `:hover`, `:focus`, `:checked`, `:disabled`, `:first-child`, `:last-child`, `:nth-child(2n+1)` (l'indicizzazione CSS parte da **1**). **Pseudo-elementi**: selezionano porzioni o elementi generati, come `::first-line`, `::before`, `::after` (con `content`).

**Cascata**: algoritmo che risolve dichiarazioni concorrenti sulla stessa proprietà di un elemento. Conta nell'ordine appropriato **origine e importanza**, **cascade layer**, **specificità**, **ordine di comparsa**; non basta il numero di classi o l'ultima regola scritta. Gli stili possono provenire dall'autore, dall'utente e dal browser. L'annotazione `!important` cambia le priorità e andrebbe usata con parsimonia.

**Specificità** (intuizione): una tripla **(ID, classi/attributi/pseudo-classi, tipi/pseudo-elementi)**, confrontata lessicograficamente. `#x` → (1,0,0), `.a:hover` → (0,2,0), `p` → (0,0,1), `*` → (0,0,0). Lo stile inline ha una precedenza propria nell'ambito della cascata. A parità di condizioni vince la regola successiva. Con **`@layer`** si definiscono strati con precedenza dichiarata, utile per separare reset, librerie e stili dell'app (le regole *unlayered* hanno una posizione specifica nel confronto).

**Ereditarietà**: alcune proprietà (es. `color`, proprietà del font) sono ereditate dagli antenati; altre (`margin`, `border`, `width`) no. `inherit` forza l'ereditarietà; `initial` torna al valore iniziale della specifica; `unset` equivale a inherit per proprietà ereditabili e initial per le altre. Ereditarietà e cascata sono processi collegati ma distinti.

> [!warning] Da ricordare
> Una dichiarazione più specifica non vince necessariamente su qualunque altra: prima occorre considerare **origine/importanza/layer**. Il selettore `A B` non è equivalente a `A > B`.

## 6. Box model, layout e responsive design

### Dimensioni e box model

**Unità assolute**: `px`, `cm`, `mm`, `in`, `pt` (nel CSS `px` è un'unità di riferimento, non sempre un pixel fisico). **Relative al font**: `em` (font size pertinente), `rem` (font size radice), `ch`, `ex`; **relative al viewport**: `vw`, `vh`, `vmin`, `vmax`; **percentuali**: dipendono dalla dimensione di riferimento definita per la proprietà (non sempre dallo stesso lato).

**Box model**: ogni elemento è costituito, dall'interno all'esterno, da **content**, **padding**, **border** e **margin**. Con `box-sizing: content-box` `width` si riferisce al contenuto; con `box-sizing: border-box` include padding e bordo. Le margin possono collassare in determinati casi del normale flusso verticale; padding e bordi no.

### Normal flow, display, float e position

**Normal flow**: ordine ordinario dei box nel documento. Gli elementi **block** iniziano generalmente una nuova riga e occupano l'ampiezza disponibile; gli **inline** partecipano al flusso di testo e non seguono le stesse regole dimensionali. **`display`** determina comportamento esterno/interno (`block`, `inline`, `inline-block`, `none`, `flex`, `grid`). `display:none` rimuove il box dal layout; `visibility:hidden` nasconde mantenendo lo spazio.

**Float** (`float:left/right`) nasce per far scorrere testo intorno a un elemento, non per griglie moderne; `clear` impedisce l'affiancamento ai float precedenti. **Positioning**: `static` (normale), `relative` (spostamento visivo rispetto alla posizione normale), `absolute` (fuori dal flusso, posizionato rispetto al containing block), `fixed` (tipicamente viewport), `sticky` (si comporta come normale fino a una soglia e poi resta vincolato nello scorrimento). `top/right/bottom/left` regolano gli offset; `z-index` interviene nei contesti di sovrapposizione.

### Flexbox e Grid

**Flexbox** è un sistema **monodimensionale**: dispone gli item sull'**asse principale** (*main axis*) e gestisce l'asse trasversale (*cross axis*). Sul **container**: `display:flex`, `flex-direction`, `flex-wrap`, `justify-content` (asse principale), `align-items` (trasversale), `gap`. Sugli **item**: `flex-grow`, `flex-shrink`, `flex-basis`, `align-self`, `order`. Lo shorthand `flex: grow shrink basis` specifica distribuzione dello spazio e dimensione di base.

**CSS Grid** è un sistema **bidimensionale**, basato su righe e colonne. `display:grid`, `grid-template-columns`, `grid-template-rows`, `gap`; sugli item `grid-column`, `grid-row` e `grid-area`. `fr` indica una frazione dello spazio disponibile nel contesto della griglia; `repeat()`, `minmax()`, `auto-fit` e `auto-fill` consentono griglie flessibili. Con **template areas** si dichiarano aree nominali.

**Confronto**: Flexbox facilita distribuzione e allineamento lungo un asse; Grid facilita il controllo simultaneo di righe e colonne. Possono convivere nello stesso layout.

### Media query e strategie responsive

**Media query**: regola condizionale che applica CSS quando caratteristiche del dispositivo/viewport rispettano una condizione; `@media (max-width: 700px)` adatta il layout agli schermi stretti. Media type come `screen`/`print` e feature come `width`, `orientation`, `prefers-color-scheme`, `prefers-reduced-motion` permettono comportamenti mirati.

**Fixed layout**: larghezza fissa, fragile sugli schermi piccoli. **Fluid layout**: dimensioni relative, ma può diventare scomodo agli estremi. **Adaptive**: layout distinti per intervalli di larghezza. **Responsive**: approccio che combina griglie fluide, immagini flessibili e media query, adattandosi a molti schermi. La separazione in un sito mobile a parte aumenta oneri di manutenzione.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Il meta viewport evita che i browser mobili trattino la pagina come un grande viewport virtuale e la ridimensionino, rendendo prevedibili i breakpoint. È raccomandato progettare *mobile first* e intervenire con media query quando il contenuto lo richiede.

## 7. CSS moderno, adattivo e accessibile

**Pseudo-classi funzionali**: `:is(A,B)` seleziona chi soddisfa almeno uno tra i selettori; `:where(A,B)` fa lo stesso ma ha **specificità zero**; `:not(A)` esclude; `:has(A)` seleziona un elemento in base a elementi correlati, per esempio un contenitore che contiene un input invalido. In generale `:is`, `:not`, `:has` prendono la specificità massima dei loro argomenti, mentre `:where` resta zero.

**Custom properties**: dichiarazioni `--nome: valore` utilizzabili tramite `var(--nome, fallback)`; partecipano alla cascata e normalmente si ereditano. Sono calcolate a runtime dal browser; differiscono dalle variabili Sass elaborate prima della distribuzione. `@property` può descriverne sintassi, valore iniziale e comportamento di ereditarietà.

**Funzioni di calcolo**: `calc()` esegue combinazioni dimensionali; `min()` sceglie il minore; `max()` il maggiore; `clamp(min,preferito,max)` limita un valore in un intervallo. Per viewport mobili sono disponibili anche unità `svh`, `lvh`, `dvh`, che trattano in modo diverso barre e aree visibili variabili.

**Container queries** (`@container`): scelgono lo stile in funzione delle dimensioni/condizioni del **contenitore** dichiarato, anziché dell'intero viewport. Sono utili per componenti riutilizzabili in regioni di ampiezza diversa.

**Immagini responsive**: `srcset` offre candidati per densità (`2x`) o larghezza (`480w`); `sizes` esprime la larghezza di visualizzazione prevista; il browser sceglie il file più opportuno. `<picture><source media="..." srcset="...">...` supporta *art direction* (cambiare ritaglio/composizione dell'immagine), non solo risoluzione.

**Preferenze e feature detection**: `@media (prefers-reduced-motion: reduce)` rispetta la riduzione delle animazioni; `@media (prefers-color-scheme: dark)` gestisce il tema. `@supports (display: grid)` applica regole solo se la funzionalità è supportata. Il **nesting CSS** consente di annidare selettori; il riferimento `&` rappresenta il selettore padre. Troppi livelli di annidamento aumentano specificità e complessità.

> [!warning] Da ricordare
> `@media` guarda principalmente il contesto di visualizzazione, `@container` il contenitore; `srcset` è selezione della risorsa adatta, `<picture>` può cambiare la direzione artistica; `:where()` è volutamente a specificità zero.

# Parte V - JavaScript

## 8. JavaScript: linguaggio, scope, funzioni e oggetti

**JavaScript** è un linguaggio di programmazione general-purpose, dinamicamente e debolmente tipizzato, specificato da **ECMAScript**. Il codice viene eseguito da un **motore JavaScript** in un *host environment* come browser o Node.js; il motore e l'ambiente host non coincidono. JavaScript consente logica applicativa, manipolazione della pagina e gestione di operazioni asincrone.

### Inclusione, sintassi e operatori

Il codice può essere incorporato con `<script>...</script>` o importato con `<script src="..."></script>`. Gli script classici senza `defer` possono bloccare il parsing della pagina; `defer` scarica in parallelo ed esegue quando il parsing è completo, rispettando l'ordine degli script defer; `async` esegue appena possibile senza garantire l'ordine relativo. Gli script `type="module"` sono moduli e hanno comportamento di caricamento differito per impostazione predefinita.

**Strict mode** (`'use strict';`) abilita vincoli che rendono errori pratiche storicamente tollerate; i moduli e il corpo delle classi sono già strict. Tipi primitivi principali: `number`, `bigint`, `string`, `boolean`, `undefined`, `symbol`, `null` (per ragioni storiche `typeof null === 'object'`). Oggetti e funzioni sono valori di riferimento. `NaN` rappresenta un risultato numerico non valido e non è uguale neppure a sé stesso.

Operatori: aritmetici `+ - * / % **`; confronti `< <= > >=`; logici `&&`, `||`, `!`; `??` (usa il valore di destra solo se sinistra è `null` o `undefined`); ternario `cond ? a : b`. **Uguaglianza debole** `==` / `!=` può eseguire conversioni implicite; **stretta** `===` / `!==` confronta senza conversioni di quel tipo e va di norma preferita. In JS `+` può concatenare stringhe. Sono presenti `if/else`, `switch`, `for`, `while`, `do/while`, `break`, `continue`, `for...of` e `for...in` (questi ultimi **non** sono intercambiabili: valori iterabili vs chiavi enumerabili).

### Variabili, hoisting e scope

- **`let`** dichiara variabile riassegnabile con **scope di blocco**.

- **`const`** dichiara binding non riassegnabile, anch'esso con scope di blocco. **Non rende immutabile l'oggetto** referenziato.

- **`var`** è la forma storica con scope di funzione, non di blocco; permette ridichiarazioni e ha comportamento di hoisting particolare: è sconsigliata nel codice moderno.

**Scope lessicale**: la visibilità di una variabile dipende da dove il codice è scritto, non da chi chiama una funzione. **Hoisting**: il linguaggio elabora le dichiarazioni prima di eseguire le istruzioni. Una funzione dichiarata con `function f(){}` può essere chiamata prima della sua dichiarazione; `var` risulta inizialmente `undefined`; `let`/`const` esistono ma non sono utilizzabili prima dell'inizializzazione per la **Temporal Dead Zone (TDZ)**, pena `ReferenceError`.

### Funzioni, espressioni e closure

**Function declaration** `function sum(a,b){return a+b;}` definisce una funzione con nome; **function expression** `const sum = function(a,b){...}` assegna una funzione a un binding; **arrow function** `const sum = (a,b) => a+b` è una forma concisa con differenze semantiche, soprattutto rispetto a `this`. Le funzioni sono **first-class values**: possono essere assegnate, passate e restituite. I parametri possono avere default; `...args` (*rest parameter*) raccoglie argomenti e `...arr` (*spread*) espande un iterabile.

**Closure**: combinazione di una funzione e del suo **ambiente lessicale**, che permette alla funzione di accedere a variabili esterne anche dopo la conclusione della funzione che l'ha creata. È utile per incapsulare stato e creare callback configurate.

### Oggetti, riferimenti, metodi, this

**Oggetto**: collezione dinamica di proprietà **chiave-valore**; le chiavi sono stringhe o simboli. Si crea con un **object literal** `{ name: 'Ada', age: 24 }` o altri costrutti. Le proprietà si leggono/scrivono con `obj.name` e `obj['name']`; il secondo accetta una chiave calcolata. `delete obj.age` rimuove una proprietà configurabile; `in` verifica la presenza lungo la catena dei prototipi, `Object.hasOwn(obj,key)` solo quella propria.

Gli oggetti sono assegnati **per riferimento**: `let b = a` non clona l'oggetto. Il confronto `a === b` verifica l'identità del riferimento. **Shallow copy** (`{...a}`, `Object.assign`) copia il livello superficiale: oggetti annidati rimangono condivisi; una **deep copy** richiede una copia ricorsiva o strumenti adeguati (es. `structuredClone` per valori supportati).

Un **metodo** è una funzione memorizzata in una proprietà. In una chiamata `obj.method()`, il valore di **`this`** dipende dal modo in cui viene invocata la funzione, non dalla posizione del codice: in generale è `obj` (nel metodo ordinario); estrarre il metodo e chiamarlo da solo può perdere il receiver. Le **arrow function** non hanno `this` proprio e lo catturano lessicalmente. `call`, `apply` e `bind` permettono di gestire il contesto di chiamata.

Le **funzioni costruttrici** sono invocate con `new`: creano un oggetto collegato al prototipo della funzione, assegnano `this` al nuovo oggetto e restituiscono normalmente tale oggetto. La sintassi `class` è oggi preferibile per descrivere costruttori e metodi. L'**optional chaining** `user?.address?.city` restituisce `undefined` se un tratto è `null`/`undefined` senza lanciare un errore di accesso; `??` fornisce un fallback senza scartare valori validi come `0`, `false` o stringa vuota.

Le **property descriptors** controllano `writable`, `enumerable` e `configurable`; **getter** `get name()` e **setter** `set name(v)` definiscono proprietà accessor anziché dati memorizzati direttamente.

## 9. Ereditarietà prototipale, strutture dati, classi, moduli

### Prototipi

**Ereditarietà prototipale**: ogni oggetto ordinario può riferirsi a un altro oggetto tramite il proprio `[[Prototype]]`. Se una proprietà non esiste nell'oggetto, la ricerca prosegue sulla **prototype chain** fino a trovarla o a incontrare `null`. L'oggetto corrente può **sovrascrivere** una proprietà ereditata senza modificarne necessariamente il valore nel prototipo. `Object.getPrototypeOf` e `Object.create` permettono di esaminare e creare legami prototipali.

**`prototype` della funzione costruttrice** e **`[[Prototype]]` di un'istanza** sono concetti diversi: quando si invoca `new F()`, il nuovo oggetto ha normalmente `F.prototype` come prototipo. Inserire metodi in `F.prototype` consente la condivisione di un'unica funzione fra le istanze anziché crearne una copia per ogni istanza.

### Array, destructuring, iterabili, Map e Set

**Array**: oggetto indicizzato e dinamico con proprietà `length`; può contenere valori eterogenei ed essere annidato. Metodi frequenti: `push`/`pop` (fine), `unshift`/`shift` (inizio), `slice` (sottosequenza senza mutare), `splice` (modifica in place), `map` (trasformazione), `filter` (selezione), `find` (primo elemento), `reduce` (accumulazione), `forEach` (effetti). **`map` restituisce un nuovo array** e `forEach` normalmente no. `for...of` itera valori; `for...in` enumera chiavi, quindi è inadatto come ciclo generale sugli array.

**Destructuring assignment**: estrae elementi da array o proprietà da oggetti usando un pattern di assegnazione, con possibili default e rest/spread.

**Iterabile**: oggetto che implementa `Symbol.iterator`, il cui iteratore fornisce valori attraverso `next()` nella forma `{value,done}`. È usabile con `for...of` e spread; array, stringhe, Map e Set sono iterabili.

**`Map`**: raccolta di coppie chiave-valore in cui le chiavi possono essere valori di qualunque tipo (anche oggetti), con ordine d'inserimento. Operazioni: `set`, `get`, `has`, `delete`, `clear`, proprietà `size`. **`Set`**: collezione di valori unici; operazioni `add`, `has`, `delete`, `clear`, `size`. A differenza di `Object`, `Map` è pensata esplicitamente per una tabella associativa dinamica; a differenza di Array, Set evita duplicati.

### Classi, gestione errori e moduli

**`class`** definisce costruttore e metodi con sintassi più leggibile, ma sotto il cofano usa ancora **prototipi**. `constructor` inizializza l'oggetto; `extends` crea una relazione d'ereditarietà; `super(...)` richiama il costruttore base; `super.method()` richiama un metodo della superclasse. Metodi definiti nella classe risiedono sul suo prototipo; i campi di istanza possono essere dichiarati esplicitamente, i campi privati usano `#nome`.

**Eccezione**: errore o condizione eccezionale propagata con `throw`, intercettabile con `try { ... } catch (err) { ... } finally { ... }`. `finally` esegue pulizia alla conclusione del blocco, anche dopo un'eccezione. Gli oggetti `Error` espongono `name` e `message`; `instanceof` verifica che un oggetto abbia un certo costruttore nella sua catena prototipale (utile per distinguere tipi di eccezione).

**Moduli ECMAScript (ESM)**: file che esportano selettivamente simboli (`export`) e importano dipendenze (`import`). Permettono modularità, incapsulamento, riuso e gestione esplicita delle dipendenze. Export **named** (`export function f(){}` e `import {f} from './m.js'`), **default** (`export default ...` e `import x from './m.js'`), alias con `as`; quanto non esportato resta interno. I moduli hanno uno scope proprio e funzionano in strict mode.

## 10. JavaScript nell'ambiente browser: DOM ed eventi

### Browser Object Model e Document Object Model

**Host environment**: ambiente che arricchisce JavaScript con API specifiche. Nel browser l'oggetto globale tradizionale è **`window`**; la pagina corrente è accessibile con **`document`**. Il **BOM (Browser Object Model)** offre funzionalità del browser non limitate alla pagina: `location` (URL/navigazione), `history` (cronologia), `navigator` (informazioni sul browser), `screen`, timer.

**DOM (Document Object Model)**: rappresentazione a **oggetti e ad albero** del documento, accessibile e modificabile via script. Un `Document` contiene nodi di tipo `Element`, `Text`, `Comment`, ecc. Il testo tra tag è spesso un nodo distinto; anche gli spazi possono generare nodi di testo. Quindi `firstChild` può essere un nodo testo mentre `firstElementChild` è un elemento HTML.

**Selezionare nodi**: `document.querySelector('selettore CSS')` restituisce **il primo** elemento corrispondente o `null`; `querySelectorAll` restituisce una **NodeList statica** di elementi corrispondenti. `getElementById`, `getElementsByTagName`, `getElementsByClassName` sono alternative; le `HTMLCollection` restituite da alcuni `getElementsBy...` sono in genere **live** (riflettono il DOM aggiornato), al contrario della NodeList di `querySelectorAll`.

**Navigare**: `parentNode`, `childNodes`, `firstChild`, `nextSibling`, `previousSibling` includono anche nodi testuali/commenti; `parentElement`, `children`, `firstElementChild`, `nextElementSibling` selezionano soltanto elementi. `nodeName` descrive qualsiasi nodo; `tagName` è significativo per gli elementi.

**Leggere e modificare**: attributi standard possono essere proprietà (`element.id`); `getAttribute`, `setAttribute`, `removeAttribute` gestiscono attributi generici; `classList.add/remove/toggle` manipola classi; `textContent` gestisce testo puro; **`innerHTML`** interpreta il valore come markup ed è pericoloso con input non affidabile; `outerHTML` rappresenta anche il tag esterno.

`createElement` crea un elemento **non ancora inserito**; `append`, `prepend`, `before`, `after`, `replaceWith`, `remove` cambiano l'albero. `cloneNode(true)` copia l'elemento e i suoi discendenti (ma non la totalità di stato e listener associati via JavaScript). API tradizionali di dialogo: `alert`, `confirm` (booleano) e `prompt` (stringa o null).

### Eventi: handler, propagazione, delega

**Evento**: segnale di un accadimento (click, pressione di un tasto, submit di un form, caricamento di un documento, ...). Un **event handler** è una funzione invocata quando l'evento si verifica; si registra con `addEventListener(type, handler, options)`, che supporta più listener per lo stesso evento, o assegnando una proprietà `onclick`, che ne supporta uno alla volta.

L'oggetto `event` contiene informazioni come `type`, `target` (origine effettiva), `currentTarget` (elemento su cui gira il listener). Per una **funzione ordinaria** usata come listener, `this` è normalmente il `currentTarget`; le arrow non hanno `this` dinamico.

**Propagazione**: un evento può attraversare la fase di **capturing** (dagli antenati al target), la fase sul **target** e la fase di **bubbling** (dal target agli antenati). `stopPropagation()` ferma la propagazione ulteriore; `stopImmediatePropagation()` ferma anche gli altri handler sul nodo corrente; `preventDefault()` annulla il comportamento predefinito **se l'evento è cancellabile** (es. invio di un form). Fermare la propagazione **non** equivale ad annullare l'azione predefinita.

**Event delegation**: si aggiunge un solo listener a un antenato e si usa `event.target.closest(...)` per individuare il discendente che ha generato l'evento. Riduce il numero di listener e funziona anche per nuovi elementi aggiunti dinamicamente, purché l'evento propaghi opportunamente.

Si possono inviare eventi programmaticamente con `dispatchEvent(new Event('change', {bubbles:true}))`. **Ordine degli script**: un codice eseguito prima che il DOM interessato sia stato costruito può non trovare elementi; si risolve con `defer`, moduli, collocazione dello script o evento `DOMContentLoaded`.

## 11. Storage, asincronismo, Promise e richieste di rete

### Persistenza nel browser

**Cookie**: coppie nome-valore e attributi gestite nel protocollo HTTP (`Set-Cookie` nella risposta, `Cookie` nelle richieste pertinenti). Il browser decide l'invio in base a dominio, percorso, scadenza, regole SameSite e altre proprietà. Un cookie può essere di **sessione** o persistente (`Expires`/`Max-Age`); `Secure` ne vincola l'invio a canali sicuri; `HttpOnly` impedisce accesso via JavaScript; `SameSite` limita alcuni invii cross-site. I cookie hanno dimensioni ridotte e spesso sono usati per un **identificatore di sessione**, non per contenere l'intero stato.

**`localStorage`**: memorizzazione chiave-valore di **stringhe** persistente per origin, accessibile via JavaScript; **`sessionStorage`**: analoga ma legata alla singola sessione/contesto di navigazione. Le Web Storage API sono **sincrone** (`setItem/getItem/removeItem/clear`). **IndexedDB** è un database client-side asincrono per dati strutturati e quantità maggiori. Nessuno di questi meccanismi sostituisce i controlli di accesso sul server; dati Web Storage sono leggibili dallo JavaScript della stessa origin, inclusi eventuali script malevoli inseriti con XSS.

### Sincronismo, callback ed event loop

**Codice sincrono**: le istruzioni si eseguono in sequenza bloccando il thread fino al termine dell'operazione. **Codice asincrono**: un'operazione viene avviata, il programma prosegue e il completamento viene segnalato in seguito; nel browser esempi sono timer e rete. **Callback**: funzione passata a un'altra funzione per essere invocata al verificarsi di un evento/risultato. Un annidamento ripetuto di callback può produrre il problema del *callback hell*, con gestione degli errori e flusso difficili da seguire.

L'**event loop** orchestra esecuzione sincrona e code di callback. Nel modello JavaScript le callback delle **Promise** diventano *microtask* e vengono elaborate al momento appropriato dopo l'attuale esecuzione sincrona; callback di timer/eventi vengono gestite con meccanismi di scheduling distinti. Questo spiega perché un `then` di Promise già risolta non esegua la callback immediatamente durante il codice che la registra.

### Promise, chaining e combinatori

**Promise**: oggetto che rappresenta il risultato futuro di un'operazione asincrona. Stati: **pending** (non terminata), **fulfilled** (successo con valore), **rejected** (fallimento con motivo). Fulfilled o rejected è uno stato **settled**. Un executor di `new Promise((resolve,reject)=>{...})` può risolvere o rifiutare la Promise; la transizione da pending è definitiva.

`then(onFulfilled, onRejected)` registra gestori e **restituisce una nuova Promise**, permettendo **chaining**; `catch(onRejected)` gestisce un errore in una catena; `finally(onFinally)` esegue pulizia sia dopo successo sia dopo fallimento. Se un `then` restituisce una Promise, la successiva attende il suo esito; se lancia un'eccezione, la nuova Promise viene rifiutata.

**Combinatori**:

| API | Quando si stabilizza e cosa produce |
| --- | --- |
| `Promise.all([...])` | Risolve con tutti i valori in ordine se tutte riescono; fallisce al primo rifiuto osservato. |
| `Promise.allSettled([...])` | Attende tutte e restituisce per ciascuna stato e valore/errore. |
| `Promise.race([...])` | Assume il primo esito concluso, successo o errore. |
| `Promise.any([...])` | Assume il primo successo; se tutti falliscono restituisce un `AggregateError`. |
| `Promise.resolve(v)` / `.reject(e)` | Crea Promise già risolte / rifiutate. |

**`async`/`await`** è sintassi per scrivere codice asincrono in forma lineare. Una funzione `async` **restituisce sempre una Promise**; `await` sospende l'esecuzione della funzione asincrona finché l'operazione non è risolta, **non** blocca l'intero thread dell'event loop. Gli errori possono essere gestiti con `try/catch`.

### XMLHttpRequest e Fetch API

**AJAX (Asynchronous JavaScript And XML)**: tecnica per aggiornare parti di un'interfaccia attraverso richieste di rete senza ricaricare tutta la pagina; i dati oggi sono spesso JSON, non XML. **`XMLHttpRequest`** è l'API storica basata su evento/callback e `readyState`; la **Fetch API** è l'alternativa moderna basata su Promise.

**`fetch(url, options)`** restituisce una Promise che si risolve con un oggetto **`Response`** appena sono disponibili le intestazioni. `response.status`, `response.ok`, `response.headers` permettono di ispezionarla. Il **corpo** viene consumato separatamente e asincronamente con `.json()`, `.text()`, `.blob()`, ecc.; tali metodi restituiscono a loro volta Promise. Per esempio:

```js
const response = await fetch('/api/todos/42');
if (!response.ok) throw new Error(`HTTP ${response.status}`);
const todo = await response.json();
```

**Fondamentale**: `fetch` **non** rigetta automaticamente la Promise per risposte HTTP `404` o `500`; ciò va verificato con `ok` o `status`. Rigetta per errori di rete, abort o altre condizioni di impossibilità della richiesta. Il parsing JSON può fallire indipendentemente dall'esito HTTP. Le regole di **same-origin/CORS** stabiliscono quali risposte cross-origin possono essere lette dagli script.

> [!warning] Da ricordare
> Callback ≠ Promise; `await` non trasforma l'I/O in operazione sincrona globale; la Promise di `fetch` ≠ la Promise di `response.json()`; cookie ≠ localStorage; catturare un errore senza rilanciarlo cambia l'esito della catena di Promise.

# Parte VI - Server-side e architetture Web

## 12. Web statico e dinamico: CGI e scripting server-side

Nel **Web statico** un server HTTP recupera file e li serve così come sono. La stessa risorsa riceve sostanzialmente lo stesso documento indipendentemente dall'utente; il JavaScript nel browser può modificarne la visualizzazione, ma non può da solo fornire dati condivisi e autorevoli o salvare un ordine nel database del servizio.

**Web dinamico**: la risposta viene **generata on the fly** da un programma server-side che elabora richiesta, dati del client e stato persistente, accedendo eventualmente a database o servizi esterni. Risolve la necessità di personalizzazione, contenuti variabili, grandi collezioni di pagine e azioni applicative. Non va confuso con l'aggiornamento del DOM lato client: una pagina statica può comunque essere interattiva.

**CGI (Common Gateway Interface)**: interfaccia storica che definisce il modo in cui un server HTTP passa una richiesta a un programma esterno e ne raccoglie l'output. In CGI classico, il server **lancia un processo** per richiesta; gli header e la query string sono esposti mediante **variabili d'ambiente**, il body arriva da **stdin**, e l'output del programma su **stdout** (header, linea vuota, corpo) diventa la risposta HTTP. È portabile ma costoso per creazione dei processi e poco ergonomico per il parsing e la costruzione dell'HTML.

**Server-side scripting**: codice sul server che produce HTML/dati tramite runtime o application server, con un livello d'astrazione più conveniente. Tecnologie storiche includono **PHP**, **ASP** e **JSP**, che possono mescolare markup e istruzioni elaborate sul server. Per esempio, un file PHP usa `<?php ... ?>` per il codice che viene interpretato e il client riceve **solo l'output HTML**, non il sorgente PHP. Nei sistemi moderni gli stessi problemi sono affrontati da runtime applicativi e web framework.

## 13. Node.js: runtime, event loop e npm

**Node.js**: **runtime** open source e cross-platform per JavaScript costruito sul motore **V8**. Consente di sviluppare applicazioni server-side con un modello **event-driven** e API **asincrone non bloccanti** per molte operazioni I/O. Il modello comune di server multi-thread assegna un thread a ogni richiesta (o ne usa uno da pool): quando il thread resta bloccato su I/O non svolge altro lavoro. Node punta a gestire molte connessioni senza un thread JavaScript dedicato a ciascuna.

### Come funziona il modello non-blocking

Il thread JavaScript principale esegue callback sull'**event loop**. Quando un'operazione I/O è avviata tramite API asincrona, il controllo torna rapidamente all'event loop; l'infrastruttura del sistema operativo e/o il thread pool sottostante gestiscono il lavoro; al completamento viene schedulata la continuazione. L'event loop può nel frattempo gestire altre richieste. **Non** significa che Node sia incapace di usare thread, né che tutte le operazioni I/O siano sempre eseguite da worker thread: la gestione dipende dal tipo di I/O e dalle API usate.

**Conseguenza**: codice JavaScript **CPU-bound** molto pesante o una funzione sincrona bloccante possono paralizzare l'event loop e peggiorare la latenza di tutte le richieste. Per lavori computazionali costosi si valutano worker thread, processi o servizi separati. Le API sincrone, ad esempio `readFileSync`, vanno usate con cautela nel percorso delle richieste.

### Node, browser e package manager

I due ambienti condividono **ECMAScript**, ma non tutte le API: Node offre moduli come `fs`, `path`, `http`, `process` e accesso al filesystem/rete; il browser offre `window` e `document` (DOM). La gestione dei moduli può usare **ESM** (`import/export`) o **CommonJS** (`require/module.exports`) a seconda della configurazione.

**npm (Node Package Manager)**: strumento per installare e gestire dipendenze e script di progetti Node. `npm init` crea un **`package.json`**, il manifesto con nome, versione, entry point, scripts, dependencies e devDependencies. `npm install pacchetto` aggiunge dipendenze; `npm install` installa le dipendenze del progetto; `npm run nome-script` esegue uno script; `npm publish` distribuisce un pacchetto al registry. `node_modules` contiene le dipendenze installate e **`package-lock.json`** registra un albero risolto di versioni per installazioni riproducibili. Il campo `"type": "module"` abilita l'interpretazione ESM dei file `.js` nel package.

**SemVer**: versione `MAJOR.MINOR.PATCH`; cambi major possono essere incompatibili, minor tipicamente nuove funzionalità compatibili, patch correzioni. L'operatore `^` consente un insieme di aggiornamenti entro limiti definiti da semver; il lockfile fissa le dipendenze effettive installate.

**Debug**: si possono porre **breakpoint**, esaminare **call stack**, variabili, watch; **Step Into** entra nella funzione, **Step Over** esegue senza entrarci, **Step Out** risale, **Continue** riprende. In VS Code, l'**Auto Attach** può connettere il debugger ai processi Node; `node --watch` può riavviare l'applicazione alle modifiche (*live reloading*).

## 15. Web application con Node.js puro, routing e template

### Server HTTP e routing

Il modulo standard **`node:http`** consente di creare il server con `http.createServer(handler)`; il **request handler** riceve `req` (richiesta, istanza di `IncomingMessage`) e `res` (risposta, `ServerResponse`). Il server ascolta con `listen(port)`.

```js
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('<h1>Ciao</h1>');
});
server.listen(3000);
```

**Routing**: funzione di instradamento che decide **quale handler** eseguire in base a **metodo HTTP**, **path** ed eventualmente parametri. Un path inesistente deve condurre a **404**; un metodo non supportato su una risorsa nota può dare **405 Method Not Allowed**. Serve anche una strategia per file statici (lettura tramite `fs` e Content-Type corretto) e per errori. In Node puro lo sviluppatore deve implementare esplicitamente gran parte di questi aspetti.

### Body, stream e form encoding

Il body di una richiesta POST può arrivare a **chunk**: `req` è uno **stream leggibile**, e gli eventi `data` ed `end` consentono di accumularlo e analizzarlo. È necessario limitare la dimensione accettata e gestire errori/connessioni interrotte. Per un form `application/x-www-form-urlencoded` le coppie sono normalmente separate da `&`, con chiave e valore separati da `=`; la codifica percentuale va decodificata. In applicazioni reali sono preferibili **parser consolidati**, evitando parsing artigianale vulnerabile o incompleto. Form JSON richiedono invece un parser JSON.

### Template engine e Pug

**Template engine**: sistema che trasforma un modello di pagina più dati in HTML, riducendo duplicazione di struttura e concatenazioni manuali. **Pug** usa una sintassi in cui **l'indentazione** definisce l'annidamento e consente **locals** (variabili passate al render), **include** (inserire frammenti), **extends** e **block** (ereditarietà di layout), `if/else` ed `each ... in` per le iterazioni.

In un'applicazione server-rendered, il controller carica i dati e passa i **locals** al template; il motore produce HTML che viene inviato via HTTP. Altri motori includono EJS, Nunjucks, Liquid. **Vantaggio**: semplicità per pagine dinamiche basate sul server; **limite**: quando l'app richiede molta interazione client-side, il modello tradizionale può produrre numerosi reload.

**Anatomia di una web app**: server HTTP → router → gestione della richiesta → validazione → logica e dati → render/template oppure serializzazione JSON → risposta HTTP. Integrazioni e responsabilità aumentano con la complessità, motivo per cui si usano i framework.

## 16. Session tracking, cookie e sessioni lato server

**Session tracking**: insieme delle tecniche con cui un'applicazione **riconosce** richieste appartenenti a una stessa interazione/utente, nonostante la natura stateless di HTTP. **Autenticazione** verifica chi è l'utente; **autorizzazione** decide cosa può fare; una **sessione** rappresenta il contesto della conversazione mantenuto attraverso richieste.

### Approcci possibili

1. **Cookie con informazioni di stato**: il server invia tramite `Set-Cookie` una rappresentazione dei dati o un token; nelle richieste successive il browser rinvia il cookie secondo le regole di applicabilità. Se i dati sono sul client, non ci si può fidare della loro integrità senza protezione crittografica.

2. **Sessione memorizzata sul server**: il server crea un record di sessione (`session-id` casuale e imprevedibile → dati utente) e comunica al browser **solo l'identificatore**, normalmente in un cookie. Alle richieste successive legge il cookie e recupera la sessione dal proprio store. Logout e scadenza devono invalidarla lato server, non limitarsi a nascondere l'interfaccia.

3. **URL rewriting** (inserire un identificatore nell'URL) e campi nascosti del form: alternative storiche, meno sicure o difficili da mantenere rispetto a un cookie protetto.

**Flusso di login con sessione server-side**:

```text
POST /login  → verifica delle credenziali
             → sessione creata nello store (session-id casuale)
             → Set-Cookie: sid=...; HttpOnly; Secure; SameSite=Lax
GET /profilo → cookie sid → sessione recuperata dallo store
```

Gli attributi **`HttpOnly`** (non accessibile via DOM), **`Secure`** (HTTPS), **`SameSite`** (mitigazione CSRF), **`Path`/`Domain`** e **`Max-Age`/`Expires`** gestiscono ambito e durata, ma non sostituiscono i controlli server-side. È buona pratica **rigenerare l'ID di sessione dopo login** per limitare la *session fixation*, usare session ID con elevata entropia, scadenze appropriate e uno store adatto alla produzione. Un cookie scaduto nel browser può comunque non cancellare immediatamente una sessione ancora valida nello store: le due durate vanno coordinate.

**Limite del semplice cookie con credenziali/dati**: il client controlla ciò che invia, quindi i valori possono essere alterati; un cookie non protetto può essere letto o rubato. **Limite della sessione in memoria locale al processo**: un riavvio la cancella; con più istanze le richieste possono raggiungere processi diversi; per produzione è preferibile uno storage condiviso o un'architettura coerente con le strategie di deployment. In Express `express-session` gestisce il cookie ID e integra gli store.

> [!warning] Da ricordare
> *Cookie* è una modalità di trasmissione e memorizzazione nel browser; *sessione* è il contesto applicativo. **Il cookie di sessione** in un design server-side porta tipicamente un **identificatore**, non l'intero oggetto utente.

## 17. Framework Web ed Express

### Libreria, framework e inversion of control

**Libreria**: codice riusabile che il programma chiama quando serve; è l'applicazione a stabilire il flusso. **Framework**: struttura di esecuzione e insieme di componenti che governano una parte significativa del ciclo di vita dell'applicazione e **invocano il codice applicativo** nei punti predisposti. Questo rapporto è chiamato **Inversion of Control (IoC)**: in una libreria *tu chiami*, in un framework *il framework chiama te* in risposta a eventi o richieste.

I web framework forniscono comunemente routing, parsing richieste, risposte, gestione errori, middleware, sessioni, supporto per template, configurazione e integrazione con database. Un framework **opinionated** propone convenzioni/strutture specifiche; **unopinionated** lascia più libertà al progettista.

**Express**: framework Web minimalista per Node.js, basato su un flusso ordinato di **middleware** e **route handler**. Espone `app.get/post/put/delete`, `app.use`, `app.listen`, `express.Router` e metodi della risposta come `res.status`, `res.send`, `res.json`, `res.render`, `res.redirect`, `res.sendFile` e `res.end`.

```js
const express = require('express');
const app = express();

app.use(express.json());
app.get('/', (req, res) => res.send('Ciao'));
app.listen(3000);
```

**Parametri di rotta** `:id` si trovano in `req.params`, **query parameters** in `req.query`, il body parsato in `req.body`, header in `req.headers`. **Express Router** raggruppa percorsi correlati e può essere montato con un prefisso, es. `app.use('/api/users', userRouter)`.

### Middleware, ciclo richiesta-risposta ed errori

**Middleware**: funzione `(req,res,next)` che può leggere/modificare la richiesta o la risposta, terminare la risposta o passare il controllo al prossimo handler con `next()`. L'**ordine di registrazione** conta; se un middleware non invia una risposta e non chiama `next()`, la richiesta può restare pendente.

**Error-handling middleware**: ha **quattro parametri** `(err,req,res,next)` e viene invocato quando si passa un errore a `next(err)` o tramite la gestione del framework. Nel codice asincrono va considerata la versione di Express: **Express 5** inoltra automaticamente i rifiuti di Promise restituiti dai route handler; nel codice legacy con callback o in Express 4 può servire passare esplicitamente l'errore a `next`. La gestione degli errori deve evitare di mostrare dettagli interni e stack trace ai client in produzione.

**Middleware notevoli**: `express.static` serve file statici; `express.urlencoded` interpreta body di form; `express.json` interpreta JSON; **`cookie-parser`** rende più comoda la lettura dei cookie; **`express-session`** gestisce sessioni server-side (configurando uno store per la produzione). Le **flash message** sono notifiche salvate temporaneamente nella sessione e tipicamente eliminate alla prima lettura, utili dopo un redirect (es. login fallito).

**Server rendering con Express**: con `app.set('view engine','pug')`, `res.render('pagina', {titolo:'...'})` elabora un template. Le rotte combinano controlli (es. middleware di autenticazione), logica applicativa e costruzione della risposta. Il metodo della risposta è indispensabile per terminare il ciclo.

## 18. Persistenza con ORM, Sequelize e organizzazione Express

### Object-Relational Mapping

**Impedance mismatch oggetto-relazionale**: un programma usa oggetti, riferimenti ed ereditarietà, mentre un RDBMS usa tabelle, tuple, chiavi e relazioni; occorre mappare i due mondi. **ORM (Object-Relational Mapping)**: tecnica/libreria che rappresenta tabelle e operazioni relazionali attraverso modelli a oggetti, riducendo il boilerplate SQL. Può gestire definizione modelli, query, CRUD, associazioni e transazioni.

**Sequelize** è un ORM JavaScript per database relazionali. Un modello descrive entità e attributi (tipi, `allowNull`, chiavi, vincoli); i metodi **`create`**, **`findAll`**, **`findOne`**, **`findByPk`**, **`update`**, **`destroy`** realizzano CRUD. Le query sono generalmente asincrone, quindi usano Promise e `await`.

**Sincronizzazione** `Model.sync()` crea tabelle non esistenti; `sync({force:true})` elimina e ricrea (possibile **perdita di dati**); `sync({alter:true})` tenta l'allineamento dello schema. In produzione una strategia di **migrazioni versionate** è preferibile alle modifiche indiscriminate del modello. **Associazioni**: `hasOne`, `belongsTo`, `hasMany`, `belongsToMany` modellano relazioni e chiavi esterne; bisogna comprendere chi possiede la FK e come vengono recuperate le righe collegate.

**Vantaggi ORM**: produttività, query dichiarative, minore duplicazione, astrazione dal database, integrazione con modelli. **Svantaggi**: curva di apprendimento, possibili query inefficienti/overhead e dipendenza dal specifico ORM; sapere SQL rimane utile, soprattutto per query complesse e prestazioni.

### Struttura e configurazione

Una possibile organizzazione Express è:

```text
progetto/
├─ routes/        # percorsi raggruppati
├─ controllers/   # coordinamento input/output
├─ models/        # modelli ORM
├─ services/      # logica applicativa
├─ middleware/    # autenticazione, gestione errori
└─ config/        # lettura di variabili d'ambiente
```

Le **route** non dovrebbero inglobare tutto: il controller coordina input/output, i modelli e i servizi gestiscono dati e logica. **Configurazione**: credenziali database, chiavi segrete, endpoint e parametri dipendenti dall'ambiente non vanno hardcodati o inviati in un repository; si leggono da **variabili d'ambiente** (`process.env`), con eventuale `.env` locale escluso dal versionamento. **Autenticazione in Express**: middleware verifica che `req.session` contenga un'identità valida; la logica di autorizzazione deve verificare anche la proprietà delle risorse e non affidarsi ai parametri inviati dal client. Le password vanno conservate mediante **hashing sicuro con salt**, non in chiaro (il caso di studio didattico delle dispense non va preso come schema pronto per la produzione).

## 19. API REST, autenticazione a token e OpenAPI

### Dal rendering server-side a frontend e backend separati

In una web app **server-centric** il backend compone HTML mediante template. In una architettura **a due componenti**, il **backend** pubblica dati e operazioni in un'API e il **frontend** presenta la UI; browser, app mobile e altri client possono utilizzare lo stesso servizio. Questo separa responsabilità e permette interfacce dinamiche; richiede però gestione di contratti, errori, versionamento e sicurezza tra componenti.

**API (Application Programming Interface)**: contratto con cui un componente espone funzionalità o dati ad altri componenti. **REST (Representational State Transfer)**: stile architetturale per sistemi distribuiti che tratta le informazioni come **risorse** identificate da URI, manipolate tramite rappresentazioni e interfaccia uniforme; tra i suoi vincoli troviamo client-server, statelessness, cacheability, interfaccia uniforme e sistema a livelli. Una REST API pratica usa spesso HTTP e **JSON**; JSON è un formato testuale per oggetti, array, numeri, stringhe, booleani e null.

**Risorsa**: entità concettuale identificata da un URI, ad esempio `/todos/42`. **Rappresentazione**: descrizione trasmessa della risorsa, ad esempio il JSON `{"id":42,"done":false}`. URI dovrebbero identificare **nomi di risorse**, non azioni verbali nel path. Le risorse **collection** (`/todos`) aggregano elementi e le **document** (`/todos/42`) ne identificano uno; le **nested resources** (`/users/7/todos`) rappresentano relazioni gerarchiche. Una collezione può supportare **filtri, ordinamento e paginazione** tramite query string, come `/todos?done=false&page=2&limit=20`.

| Metodo / endpoint | Uso atteso | Stato tipico |
| --- | --- | --- |
| `GET /todos` | Elenco, con filtri e paginazione. | `200` |
| `GET /todos/42` | Recupero di un singolo elemento. | `200` o `404` |
| `POST /todos` | Creazione in una collezione. | `201 Created` con `Location` |
| `PUT /todos/42` | Sostituzione (o creazione prevista dal contratto). | `200`, `204` o `201` |
| `PATCH /todos/42` | Aggiornamento parziale. | `200` o `204` |
| `DELETE /todos/42` | Eliminazione. | `204`, ecc. |

Un buon design usa correttamente metodi e codici HTTP, nomi coerenti, rappresentazioni JSON con Content-Type adeguato, gestione uniforme degli errori e identificatori di risorsa stabili. **REST non richiede obbligatoriamente JWT, JSON o URL plurali**: questi sono standard e convenzioni spesso usati, ma vanno distinti dai vincoli dello stile architetturale.

### Autenticazione, autorizzazione, token, JWT

**Autenticazione**: verifica dell'identità (es. credenziali). **Autorizzazione**: verifica che l'identità possa agire su una specifica risorsa. Un'API può utilizzare un **bearer token**: dopo il login il server rilascia un token; il client lo trasmette in `Authorization: Bearer <token>`; il server lo valida a ogni richiesta protetta. Chiunque possieda un bearer token valido può spesso usarlo, quindi la sua protezione è essenziale.

**JWT (JSON Web Token)**: formato standard di token che rappresenta **claim**, spesso in tre blocchi Base64url separati da punti, **`header.payload.signature`**. L'**header** identifica tipo/algoritmo; il **payload** contiene claim (soggetto, scadenza, eventuali ruoli); la **signature** permette di verificare l'integrità e l'autenticità rispetto alla chiave. **Base64url non è cifratura**: header e payload in un JWT firmato sono leggibili da chiunque lo possieda. Una firma JWT **non** indica che il contenuto sia confidenziale. Validare significa controllare firma con algoritmo e chiave attesi e claim rilevanti (`exp`, `iss`, `aud`, ecc.). Un ruolo nel payload va considerato attendibile **solo dopo** la verifica del token e delle policy applicative.

**Differenze**: una sessione stateful memorizza il contesto sul server e invia un ID; un JWT firmato può essere verificato senza lookup del singolo token, ma **revoca**, scadenza, rotazione delle chiavi e compromissione hanno implicazioni differenti. Un JWT **non è necessariamente** una sessione stateless completa e non è l'unico tipo di bearer token. **401 Unauthorized** per autenticazione assente/non valida, **403 Forbidden** per permessi insufficienti (es. tentativo di modificare il to-do di un altro utente).

### OpenAPI e strumenti Swagger

**OpenAPI**: specifica standard, **machine-readable** e leggibile dall'uomo, del contratto di una API HTTP: versione, metadati, path, metodi, parametri, request body, risposte, schemi dati e sicurezza. Il documento può essere in **YAML** o JSON. Consente documentazione interattiva, generazione di client/server stub, validazione e collaborazione tra team.

**Swagger Editor** aiuta a scrivere la specifica; **Swagger UI** la visualizza come documentazione interattiva; strumenti di **code generation** producono SDK e stub. **API-first/OpenAPI-driven development** definisce il contratto prima dell'implementazione e rende esplicite le aspettative tra frontend, backend e testing.

> [!warning] Da ricordare
> Risorsa ≠ sua rappresentazione; endpoint ≠ URI da solo (contano anche metodo e contratto); autenticazione ≠ autorizzazione; JWT firmato ≠ cifrato; **401 ≠ 403**.

# Parte VII - TypeScript e tooling frontend

## 20. TypeScript e sistema dei tipi

**TypeScript**: **superset tipizzato di JavaScript** che aggiunge un sistema di tipi principalmente **statico** e strumenti di analisi prima dell'esecuzione. Il compilatore **`tsc`** verifica il codice, segnala incompatibilità e produce JavaScript eseguibile; le annotazioni di tipo normalmente **non esistono a runtime**. Il processo di traduzione da un linguaggio di alto livello a JavaScript si chiama **transpilazione**; il **downleveling** trasforma feature moderne in una sintassi compatibile con target JavaScript precedenti quando possibile. TypeScript non elimina la necessità della validazione dei dati a runtime, soprattutto alle frontiere di rete.

### Tipi, inferenza, any, unknown

JavaScript è **dinamicamente tipizzato**: i tipi appartengono ai valori e la stessa variabile può ricevere valori di tipi diversi; è inoltre permissivo nelle conversioni implicite. TypeScript aggiunge dichiarazioni di tipi per variabili, parametri, risultati e strutture dati. I tipi primitivi usuali sono `string`, `number`, `boolean`, oltre a `bigint`, `symbol`, `null`, `undefined`.

**Inferenza**: `let course = 'Web'` porta il compilatore a dedurre `string`; non è sempre necessario annotare ogni variabile. **`any`** disabilita molti controlli: consente operazioni arbitrarie, rischiando errori a runtime. **`unknown`** può contenere qualunque valore, ma richiede controllo (*narrowing*) prima di usarlo; è generalmente preferibile ad `any` per dati non noti. **`void`** indica tipicamente assenza di valore restituito da una funzione; **`never`** rappresenta valori impossibili/rami irraggiungibili o funzioni che non terminano normalmente.

**Type narrowing**: restringimento del tipo grazie a verifiche come `typeof x === 'string'`, controlli su proprietà o discriminanti; rende sicuro accedere a membri specifici di un union type. **Type assertion** `x as T` comunica al compilatore un'ipotesi del programmatore e non esegue una validazione a runtime.

### Structural typing, union, intersezioni e interfacce

**Structural typing**: la compatibilità fra tipi dipende dalla **struttura**, cioè dalle proprietà/metodi richiesti, non dal nome della dichiarazione. Un oggetto con più proprietà può soddisfare un'interfaccia che ne richiede meno; nei literal assegnati direttamente sono previste anche verifiche aggiuntive sulle proprietà in eccesso.

**Object types** descrivono le proprietà e i relativi tipi, anche opzionali (`?`) o readonly. **Union type** `A | B` accetta valori di uno dei tipi; **intersection type** `A & B` richiede l'insieme dei requisiti di entrambi. **Type alias** (`type`) assegna un nome a un tipo, anche primitive, union o tuple; **`interface`** definisce contratti strutturali di oggetti, può essere estesa e supporta il *declaration merging*. `type` non può essere riaperto con una seconda definizione dello stesso nome. Per gli array si usano `T[]` o `Array<T>`; una **tuple** può esprimere una sequenza con posizioni tipizzate (`[string, number]`).

**Generics**: parametrizzano funzioni, tipi e classi usando variabili di tipo, preservando la relazione tra input e output. `function identity<T>(x:T):T {return x;}` mantiene il tipo di `x` nel risultato: **non** è equivalente a `any`. I vincoli `T extends ...` richiedono determinate caratteristiche strutturali.

### Strictness e compilazione

`tsconfig.json` governa compilazione, versione di ECMAScript target, moduli, output e livello di controllo. **`strict`** abilita più verifiche, incluse regole per `null`/`undefined`; **`noImplicitAny`** evita che un parametro privo di tipo deducibile diventi silenziosamente `any`; **`strictNullChecks`** richiede di trattare esplicitamente i valori potenzialmente nullish. Aumentare la severità aumenta la quantità di errori trovati prima dell'esecuzione.

> [!warning] Da ricordare
> I tipi TS non sono una misura di sicurezza contro JSON malformato o input malevolo: i dati ricevuti vanno controllati in esecuzione.

## 21. Frontend tooling: Sass, bundle, build e Vite

L'aumento di moduli JavaScript, dipendenze, CSS e target browser richiede una **toolchain** che automatizzi compilazione, ottimizzazioni e avvio del progetto.

**CSS preprocessor**: trasforma un linguaggio sorgente esteso in CSS; **Sass/SCSS** aggiunge variabili, nesting, mixin, funzioni e moduli. **CSS postprocessor**: trasforma CSS già prodotto (es. **Autoprefixer** per prefissi vendor, riscritture compatibili e minification). Le variabili **Sass** (`$color`) sono sostituite **in build**, mentre le **CSS custom properties** (`--color`) rimangono dinamiche nel browser.

**Mixin**: blocco riusabile di dichiarazioni parametrizzato; **partial/module**: frammento CSS/SCSS separato importato nel progetto; nesting e cicli possono generare CSS, ma annidamenti eccessivi aumentano il rischio di selettori difficili da mantenere. I **framework CSS** forniscono componenti, griglie o utility già pronti (es. Bootstrap o Tailwind), riducendo il lavoro ripetitivo ma introducendo convenzioni e vincoli di personalizzazione.

**Bundling**: analisi del grafo delle dipendenze e raggruppamento/trasformazione dei moduli in asset distribuibili; migliora gestione e ottimizzazione, ma può avere più bundle/loose chunks per caricamento efficiente. **Minification**: rimozione di spazi e riscritture equivalenti per ridurre byte senza cambiare il comportamento; **tree shaking**: eliminazione di codice esportato non usato, quando l'analisi lo consente. **Fingerprinting**: hash nel nome del file generato (`app.a82f.js`) per usare cache lunghe degli asset e cambiare URL quando cambia il contenuto.

**Vite**: strumento di sviluppo/build per frontend che fornisce un **dev server** rapido (con aggiornamenti HMR) e una **build** ottimizzata per produzione, gestendo moduli, asset e trasformazioni. Tipico flusso: `npm create vite@latest`, `npm install`, `npm run dev`, `npm run build`. Il server di sviluppo **non** è equivalente a un server di distribuzione pronto per produzione. **Compilazione, bundling e minification sono concetti diversi**: la build può orchestrarli, ma non coincidono.

# Parte VIII - SPA e Angular

## 22. Single Page Applications

**Multi-Page Application (MPA)**: alla navigazione il browser richiede in genere un **nuovo documento HTML**, aggiornando tutta la pagina. **Single Page Application (SPA)**: una pagina HTML iniziale carica codice JavaScript che cambia la vista, gestisce la navigazione e recupera dati attraverso API **senza richiedere un full reload per ogni passaggio**. SPA non vuol dire «una sola schermata», bensì un **documento principale** con più viste controllate lato client.

**Client-side routing**: corrispondenza tra URL e viste/componenti effettuata nel browser. `history.pushState(...)` aggiorna l'URL senza ricaricare il documento; l'evento **`popstate`** consente di reagire a indietro/avanti; un router deve processare anche il caricamento diretto di un URL. Per ottenere una SPA navigabile serve configurare il server affinché restituisca il documento di ingresso anche quando un path frontend non corrisponde a un file statico, senza confondere questo fallback con il routing dell'API.

**Componente**: unità riutilizzabile di UI che incapsula struttura, stile, comportamento e spesso stato; componenti annidati formano un albero. Si possono usare Web Components nativi, ma i framework offrono sistemi più completi di rendering, stato, eventi e routing.

**AJAX/fetch** carica i dati dalla REST API; la SPA converte i dati in interfaccia. Vantaggi: navigazione fluida, logica UI ricca, riuso di API da più client, meno reload. Sfide: maggiore complessità client, bundle iniziale, gestione stato e sincronizzazione, loading/error states, accessibilità della navigazione, sicurezza e necessità di gestire correttamente URL e dati. Framework come Angular forniscono soluzioni strutturate.

## 23. Angular: componenti, template e comunicazione

**Angular**: framework frontend, sviluppato e mantenuto da Google, basato su **TypeScript**, con strumenti per componenti, template dichiarativi, dependency injection, router, form, rete e test. La **Angular CLI** crea progetti (`ng new`), genera artefatti (`ng generate component`/`service`), serve in sviluppo e prepara build.

### Componenti e template

La UI Angular è un **albero di componenti**. Un componente è una classe TypeScript associata a un **selector**, a un **template HTML** e a stili. Un **standalone component** dichiara le proprie dipendenze (`imports`) senza dover essere dichiarato in un NgModule tradizionale; è il modello moderno presentato nel corso.

```ts
@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  standalone: true,
  imports: [CommonModule],
})
export class TodoItemComponent {}
```

**Interpolazione** `{{espressione}}` inserisce un valore testuale nel template; **property binding** `[property]="espressione"` imposta una proprietà DOM o input di componente; **event binding** `(event)="handler($event)"` collega un evento a un'azione. Non sono equivalenti: per un valore booleano o una proprietà non testuale serve spesso property binding, non interpolazione come stringa.

**Control flow** nei template: `@if (...) { ... } @else { ... }`, `@for (item of items; track item.id) { ... }` e `@switch` scelgono o ripetono contenuti. `track` aiuta Angular a riconciliare correttamente gli elementi di una lista. Le vecchie direttive `*ngIf` e `*ngFor` sono alternative storiche.

### Input e Output

**Da genitore a figlio**: un **`@Input()`** (o API moderna `input()`) passa dati nel componente figlio, spesso con `[nome]="espressione"`. **Da figlio a genitore**: un **`@Output()`** (o API `output()`) espone un evento; il figlio lo emette e il padre lo intercetta con `(nomeEvento)="handler($event)"`. Distingue **data flow verso il basso** da **comunicazione di eventi verso l'alto**.

### Router

**Angular Router** associa URL a componenti. Le rotte si configurano con `provideRouter(routes)`. Il template radice contiene **`<router-outlet>`**, in cui viene mostrata la vista scelta. Per navigare senza reload si usano `routerLink` o `Router.navigate`. **`routerLinkActive`** applica classi ai link attivi.

La configurazione **`routerLinkActiveOptions`** controlla, fra le altre cose, la corrispondenza esatta del percorso. I parametri di route e query devono essere letti come **input non affidabili**.

## 24. Angular: form, servizi, HTTP e reattività

### Form template-driven e reactive

**Template-driven form**: la definizione del form è concentrata nel template, usando direttive come `ngModel` e `ngForm`; conveniente per casi semplici. **Reactive form**: il modello del form è costruito **esplicitamente in TypeScript** con `FormControl`, `FormGroup`, `FormBuilder`; rende più semplici validazione e testing di form complessi. Con `ReactiveFormsModule` i controlli si collegano con `formGroup` e `formControlName`. **Submission**: `(ngSubmit)="onSubmit()"` processa i dati; le regole di validazione (`Validators.required`, `minLength`, ecc.) producono stato `valid/invalid`, `touched/untouched`, `dirty/pristine` e collezioni di errori.

### Servizi e dependency injection

**Service**: classe che incapsula logica condivisa, ad esempio accesso API, autenticazione o gestione dati, separandola dalla UI. **Dependency Injection (DI)**: il componente **dichiara** le dipendenze richieste invece di costruirle manualmente; l'**injector** Angular le istanzia/fornisce secondo la configurazione. `@Injectable({providedIn:'root'})` rende normalmente un service disponibile a livello dell'applicazione. Una dipendenza si ottiene tramite parametro del costruttore oppure `inject(ServiceClass)`; lo stesso service può essere condiviso da più componenti.

**Route Guard**: funzione/servizio di controllo che decide se attivare o lasciare una rotta. `canActivate`, `canMatch` e altre guardie possono restituire boolean, `UrlTree`/redirect oppure un esito asincrono. Una guardia frontend migliora la navigazione, **non è una barriera di sicurezza**: ogni API protetta deve convalidare autenticazione e autorizzazione lato server.

### HttpClient, Observable e interceptor

**`HttpClient`** è l'API Angular per richieste HTTP (da configurare, ad esempio, tramite `provideHttpClient()`). I suoi metodi (`get`, `post`, `put`, `delete`, ...) restituiscono normalmente **Observable RxJS**, non Promise. **Observable**: descrizione di una sorgente asincrona che può emettere **zero, uno o più valori** nel tempo, un errore o il completamento. Il consumatore usa `subscribe({next,error,complete})`; per richieste HTTP standard l'observable in genere emette la risposta e si completa. Operatori RxJS come `map`, `filter`, `switchMap`, `catchError` trasformano o compongono flussi; gestione della sottoscrizione e degli errori è essenziale.

Un **HTTP interceptor** esegue logica trasversale per richieste/risposte (es. aggiungere un token, logging, error handling). Si inserisce nella pipeline di `HttpClient`, per esempio tramite `withInterceptors(...)`; l'implementazione funzionale riceve richiesta e funzione `next`, e può clonare la richiesta per aggiungere header: la richiesta è concettualmente immutabile.

### Change detection e signals

**Change detection**: processo tramite cui Angular individua aggiornamenti dello stato e mantiene coerente il **DOM renderizzato** con i valori dell'app. I **signals** forniscono reattività esplicita: `signal(v)` crea uno stato leggibile invocandolo come funzione, modificabile con `.set()` e `.update()`; **`computed(() => ...)`** deriva un valore in modo reattivo dalle dipendenze; **`effect(() => ...)`** esegue effetti collaterali quando cambiano i signals letti. I computed sono derivati e **non vanno aggiornati direttamente**.

**Observable vs Signal**: il primo è adatto a **flussi di eventi asincroni** nel tempo (HTTP, input, timer, ...); il secondo rappresenta **uno stato corrente reattivo**. Possono essere integrati, ma non sono sinonimi. Gli effect servono per effetti esterni, non come sostituto indiscriminato di computed o del flusso dati.

## 25. Caso completo: Angular To-do SPA

Il caso di studio unisce i concetti precedenti in una **applicazione con login e to-do**, mostrando come cooperano router, form, servizi, interceptor, guard e componenti.

**Percorso di una richiesta autenticata**:

```text
click su «Completa» nel componente figlio
  → @Output() emette l'ID al genitore
  → TodoService.complete(id) → HttpClient: PATCH /api/todos/:id
  → interceptor: aggiunge Authorization: Bearer <token>
  → backend: verifica token e proprietà della risorsa
  → genitore aggiorna un signal → la vista si aggiorna
```

**Stato di autenticazione**: `AuthService` può conservare un signal con sessione/identità e ricavare `user`, `token` e `isAuthenticated` con `computed`. Un `effect` può sincronizzare alcune informazioni nel browser (es. localStorage), ma **memorizzare bearer token in localStorage aumenta l'esposizione ad XSS**: è un compromesso didattico/architetturale da motivare, non una pratica universalmente sicura. La vera sicurezza dipende dal backend e dalla gestione dei token.

**Login form**: controlli tipizzati e validati; errore visualizzato in caso di credenziali errate; il submit avvia una richiesta asincrona e gestisce successo/fallimento. **Guard**: per una rotta privata restituisce `true` se autenticato, altrimenti un `UrlTree` di redirezione verso il login. **Interceptor**: acquisisce token, clona la richiesta e aggiunge l'header `Authorization` solo dove opportuno. **TodoService**: raccoglie metodi `getAll`, `create`, `update`, `delete` e interagisce con la REST API. **Lista e item**: il padre passa il to-do al figlio tramite input, il figlio emette un evento `delete` con l'identificatore e il padre invoca il servizio e aggiorna lo stato. L'autorizzazione **per ogni singola risorsa** resta responsabilità del backend.

> [!warning] Da ricordare
> `@Input` e `@Output` regolano lo scambio tra componenti, non quello col backend; `HttpClient` usa Observable; una guard non sostituisce l'autorizzazione; un signal contiene uno stato, un computed deriva un altro stato.

# Parte IX - Sicurezza delle Web application

## 26. Minacce e difese fondamentali

**Web Application Security**: disciplina che protegge **riservatezza, integrità e disponibilità** dei dati e delle funzionalità in un'applicazione Web. La sicurezza è **end-to-end**: browser, JavaScript, server HTTP, framework, dipendenze, database, configurazione e sistema operativo contribuiscono alla superficie di attacco. La sicurezza del trasporto HTTPS è necessaria, ma non rende automaticamente sicuro il codice applicativo. I principi pratici sono **minimo privilegio**, validazione lato server, gestione delle dipendenze, controlli di accesso centralizzati, gestione sicura dei segreti e dei log. **OWASP** pubblica classificazioni e linee guida per vulnerabilità Web ricorrenti.

### Cross-Site Scripting (XSS)

**XSS**: vulnerabilità che permette di far eseguire a un browser **JavaScript controllato da un attaccante** nel contesto di una pagina legittima. Se un'app concatena testo non fidato dentro `innerHTML` o inserisce input utente in punti eseguibili senza protezioni, il browser può interpretarlo come markup o codice. Lo script malevolo può manipolare il DOM, inviare richieste con l'identità dell'utente e leggere dati accessibili allo script della pagina.

Forme frequenti: **stored/persistente** (payload conservato dal server, ad esempio in un commento), **reflected** (payload riflesso da una risposta), **DOM-based** (vulnerabilità nella trasformazione client-side di dati non fidati). **Difese**: output encoding/escaping contestuale (HTML, attributi, URL, JS), usare API testuali (`textContent`) invece di `innerHTML` per testo non fidato, sanitizzazione robusta quando è **necessario** accettare HTML, **CSP** come difesa aggiuntiva e limitazione dei privilegi.

**Angular e XSS**: l'interpolazione nel template esegue escaping dei contenuti e Angular sanitizza vari binding per contesti pericolosi; non bisogna aggirare queste difese con API come `bypassSecurityTrustHtml` su input non fidato. La protezione automatica non autorizza a usare acriticamente tutte le API DOM o librerie esterne.

> [!warning] Da ricordare
> *escaping* trasforma caratteri speciali in dati innocui in uno specifico contesto; *sanitizzazione* rimuove o neutralizza costrutti pericolosi da contenuti che devono mantenere un sottoinsieme di markup. Un filtro generico che elimina solo la stringa `<script>` non elimina tutti i vettori XSS.

### Cross-Site Request Forgery (CSRF)

**CSRF**: attacco in cui un sito malevolo induce il **browser di un utente autenticato** a inviare una richiesta che compie un'operazione indesiderata su un altro sito. Il bersaglio è l'autorità derivante da **credenziali inviate automaticamente dal browser**, tipicamente cookie di sessione, e non è necessario che l'attaccante legga la risposta. Esempio: un form cross-site esegue una richiesta di trasferimento; il browser può allegare cookie validi del sito bersaglio.

**Difese**: usare metodi **non safe** per azioni che cambiano stato (mai affidarsi a GET), **CSRF token** imprevedibili collegati alla sessione e validati sul server (**synchronizer token pattern**), `SameSite` sui cookie, verifica di Origin/Referer quando appropriata. L'uso di header `Authorization: Bearer ...` aggiunti esplicitamente dal JavaScript riduce alcune modalità classiche di CSRF, ma introduce altri rischi, soprattutto se il token è leggibile da uno script XSS.

**CSRF vs XSS**: in XSS viene eseguito codice dell'attaccante **nella origin della vittima**; in CSRF una origin esterna induce una richiesta **con l'identità automatica della vittima**. Hanno presupposti e difese differenti.

### SQL injection e query parametrizzate

**SQL injection**: attacco in cui input non affidabile, concatenato al testo di una query SQL, **altera la struttura della query** anziché restare un dato. Può cambiare criteri di ricerca, bypassare controlli, leggere o modificare dati. Non basta «rimuovere gli apostrofi» o usare validazione superficiale.

**Prepared statement/query parametrizzata**: separa la **struttura della query** dai **valori**; i parametri vengono inviati come dati e non interpretati come istruzioni SQL. Esempio con `pg` in Node:

```js
const result = await db.query(
  'SELECT * FROM todos WHERE user_id = $1',
  [req.user.id]
);
```

È fondamentale verificare l'autorizzazione per i record richiesti. ORM affidabili normalmente parametrizzano le query standard, ma SQL manuale o costruzione dinamica di identificatori possono reintrodurre vulnerabilità: un ORM **non** garantisce automaticamente assenza di SQL injection.

### Session hijacking e validazione

**Session hijacking**: appropriazione di un identificatore di sessione o token per impersonare l'utente. Vettori: intercettazione su HTTP, XSS, log, furto dal dispositivo o prevedibilità degli identificatori. Mitigazioni: **HTTPS**, cookie `Secure`, `HttpOnly`, `SameSite` nei casi pertinenti, elevata casualità degli ID, durata limitata, invalidazione al logout, rotazione al cambio di privilegio, protezione da XSS, gestione sicura dei token.

**Validazione degli input**: controllo di tipo, formato, intervallo, lunghezza e coerenza semantica; va effettuata **sempre sul server**, perché richieste HTTP possono essere prodotte senza utilizzare il form o l'Angular app. La validazione client-side resta utile per l'esperienza utente. **Validazione ≠ autorizzazione**: anche un ID formalmente corretto non può consentire l'accesso a dati altrui.

### Modello di sicurezza del browser, same-origin e CORS

**Origin**: combinazione di **schema, host e porta**. Due URL sono *same-origin* solo se coincidono in tutti e tre. La **Same-Origin Policy (SOP)** limita ciò che uno script può leggere o manipolare di risorse di altre origin, proteggendo l'isolamento tra siti. Alcune **richieste** cross-origin possono comunque essere inviate, ma la lettura delle **risposte** da parte di JavaScript è soggetta a restrizioni.

**CORS (Cross-Origin Resource Sharing)**: protocollo basato su header HTTP che consente al **server di destinazione** di dichiarare quali origin possono leggere certe risposte dal browser. Per esempio `Access-Control-Allow-Origin: https://frontend.example.org`; quando si usano credenziali sono richieste ulteriori condizioni (incluso `Access-Control-Allow-Credentials` e un'origine esplicita compatibile). Le richieste non semplici possono generare un **preflight** `OPTIONS` con `Access-Control-Request-Method` e `Access-Control-Request-Headers`, a cui il server risponde con i metodi/header permessi.

**Distinzioni fondamentali**: CORS è applicato dai **browser**, non è un sistema di autenticazione né un sostituto delle policy di autorizzazione server-side; un client non-browser può inviare richieste indipendentemente dalla SOP. **CORS non è una difesa generale da CSRF**: il blocco della lettura di una risposta non implica sempre il blocco dell'invio dell'azione. HTTPS protegge il canale; SOP/CORS isolano l'accesso agli oggetti/risposte; i controlli di autenticazione e autorizzazione proteggono i dati applicativi.

# Parte X - Testing

## 27. Verifica, unit test, E2E e Playwright

**Verifica del software**: insieme delle attività che mirano a stabilire che il programma soddisfi le proprietà e i requisiti previsti. Il **software testing** è una forma di **verifica dinamica**: si esegue il **System Under Test (SUT)** con input e condizioni scelti e si confrontano risultati reali con gli attesi. La verifica **statica** include analisi del codice, review e strumenti che operano senza eseguire l'applicazione.

Un test si organizza spesso in **Arrange-Act-Assert**: preparazione di dati e ambiente; esecuzione dell'operazione; verifica dell'esito. Deve essere **ripetibile**, isolato quanto possibile e avere un risultato interpretabile. Un test superato dimostra che **quel caso** ha soddisfatto le aspettative: non prova l'assenza di ogni difetto.

### Livelli di testing

**Unit test**: verificano una singola funzione/classe/componente con dipendenze controllate; sono rapidi e aiutano a isolare bug. **Integration test**: verificano la collaborazione tra più componenti o un confine (controller-servizio-database, UI-service). **End-to-End (E2E) test**: simulano flussi utente attraverso l'intero sistema in esecuzione, fino a browser, backend e persistenza quando previsti. Una **testing pyramid** suggerisce numerosi test veloci in basso e meno test lenti/fragili in alto.

**Unit testing Angular**: si possono creare componenti in un ambiente di test con **TestBed** e **ComponentFixture**, fornire dependency mock e verificare logica e DOM. Il runner e le librerie dipendono dalla configurazione del progetto. Un **test double** sostituisce una dipendenza reale: *stub* fornisce risposte predefinite, *fake* offre un'implementazione semplificata, *mock* supporta aspettative sull'interazione, *spy* registra chiamate/argomenti e può alterare i risultati. I termini possono sovrapporsi tra framework.

**Code coverage**: percentuale di unità di codice attraversate dai test, ad esempio **statement**, **branch**, **function** e **line coverage**. Un'alta coverage indica esecuzione di codice, **non** necessariamente capacità di rilevare bug: sono importanti asserzioni, casi limite e comportamenti verificati. Un test può avere coverage elevata senza verificare correttamente i requisiti.

### Test E2E e strategie di locator

**E2E testing**: interagisce con la UI e verifica scenari concreti (login, aggiunta to-do, logout). L'esecuzione **manuale** è flessibile ed esplorativa, ma costosa e poco ripetibile; quella **automatizzata** richiede manutenzione iniziale, ma facilita la regressione continua. **Flakiness**: un test fallisce o riesce in modo non deterministico senza cambiamenti rilevanti del codice; cause comuni sono race condition, attese temporali rigide, dati condivisi e dipendenze instabili.

**Locator**: criterio per individuare un elemento della pagina nel test. Strategie: selettori **CSS**, **XPath**, **ruolo/accessibility name** (`getByRole`) e identificatori di test (`data-testid`). Per interazioni utente si preferiscono spesso locator **semantici**, più resistenti a modifiche estetiche del DOM e più coerenti con l'accessibilità. Indici posizionali e selettori su classi CSS volatili sono fragili. Un locator deve individuare l'elemento giusto in modo chiaro.

### Playwright, fixture, azioni e asserzioni

**Playwright**: framework/tool di test E2E che automatizza browser moderni e offre API per navigazione, interazioni, locator, asserzioni e isolamento dei test. Supporta diversi linguaggi e browser; consente test su interfacce Web reali. **Fixture**: risorsa/ambiente fornito e preparato per un test (ad esempio l'oggetto `page`); ogni test dovrebbe usare stato **isolato** e dati controllati, pulendo o ricreando quanto occorre, evitando dipendenze dall'ordine di esecuzione.

**Fasi E2E**: **locating** (trova elemento), **actions** (`click`, `fill`, `selectOption`, ...), **asserting** (`toBeVisible`, `toHaveText`, ...). Le **auto-waiting actions** e le asserzioni con retry riducono test fragili rispetto a `sleep` arbitrari. L'**isolamento** richiede dati, cookie, storage e account test adeguati; una suite non dovrebbe modificare dati di produzione. **Capture and Replay (C&R)**: registra interazioni utente e genera una traccia/script da riprodurre; accelera la creazione di test ma può generare locator fragili e non sostituisce la revisione delle asserzioni.

# Casi ragionati: come affrontare una prova d'esame

Gli esercizi seguenti mettono insieme concetti che, nelle lezioni, sono spesso presentati separatamente. Il punto non è imparare una soluzione a memoria: è saper **motivare i passaggi** e distinguere fatti corretti da conclusioni affrettate.

## Caso A - Risoluzione DNS e referral

**Domanda.** Un browser richiede `www.dipartimento.example.it`. La cache del resolver è inizialmente vuota. Quali server vengono contattati? Che differenza c'è se la risposta è `NOERROR` con `Answer` vuoto oppure `NXDOMAIN`?

**Ragionamento.** Lo stub locale inoltra la query al resolver ricorsivo. Questo, senza informazioni in cache, segue la gerarchia: root, autoritativi del TLD `.it`, eventuali server delegati per `example.it`, poi l'autorità per `dipartimento.example.it` se esiste una delega. A ogni passo un **referral** contiene tipicamente record NS nell'`Authority`, mentre gli indirizzi dei server possono trovarsi in `Additional` o richiedere risoluzioni dedicate. Quando il resolver trova un record richiesto, restituisce il risultato al client, conservando in cache i record secondo TTL e policy applicabili.

- `NOERROR` + record A in Answer: risposta positiva.

- `NOERROR` + Answer vuoto + informazioni appropriate: il nome esiste ma può non avere record A (**NODATA**), oppure il server fornisce un referral per proseguire: servono sezione Authority e contesto.

- `NXDOMAIN`: il nome interrogato non esiste, non semplicemente «non ha record A».

**Trappola**: il client non interroga normalmente uno per uno i server root, TLD e autoritativi; questa navigazione è responsabilità del **resolver ricorsivo**. È altrettanto sbagliato sostenere che un RR `NS` da solo contenga necessariamente l'indirizzo IPv4 del name server.

## Caso B - HTTP, Vary e validazione condizionale

**Domanda.** Il browser ha memorizzato la seguente risposta e, dieci minuti dopo, effettua di nuovo la richiesta:

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: private, max-age=300
Vary: Accept-Language
ETag: "rev9"
```

**Soluzione.** La risposta aveva una durata nominale di **cinque minuti**; dopo dieci minuti non può essere riusata direttamente secondo la normale politica di freschezza. Essendo `private`, può essere memorizzata e riusata da una cache privata, ma non come copia condivisa da un proxy per utenti diversi. La richiesta successiva **in italiano**, se compatibile con la variante registrata tramite `Vary`, può inviare `If-None-Match: "rev9"`. Se il server risponde **304**, la cache riutilizza il corpo locale e aggiorna i metadati opportuni; se risponde **200**, sostituisce la copia. Una richiesta in altra lingua potrebbe richiedere una diversa rappresentazione: non è sufficiente che il path coincida.

**Domanda aggiuntiva.** Se fosse presente `no-store`, perché non dovremmo parlare di validazione? Perché la copia non doveva essere memorizzata: non c'è un corpo da recuperare dalla cache. Se ci fosse `no-cache`, invece, memorizzare sarebbe possibile, ma la validazione sarebbe necessaria prima del riuso. Sono due direttive semanticamente diverse.

## Caso C - Metodi HTTP e scelta dello status

Un client presenta questo workflow: recupera un prodotto, invia una richiesta di creazione, tenta di cancellare un prodotto altrui e legge un ID inesistente. Quali metodi e status sono coerenti?

| Operazione | Scelta ragionata |
| --- | --- |
| Recuperare prodotto 17 | `GET /products/17` → `200`, oppure `404` se inesistente. |
| Creare prodotto | `POST /products` → `201 Created`, eventualmente header `Location`. |
| Aggiornare completamente prodotto 17 | `PUT /products/17` → `200`/`204` secondo la rappresentazione restituita. |
| Cambiare solo il prezzo | `PATCH /products/17` → `200`/`204`. |
| Eliminare prodotto di un altro utente | `DELETE /products/17` → `403` **se la richiesta è autenticata ma vietata**. |
| Chiamare senza credenziali una rotta protetta | `401`, eventualmente con una sfida di autenticazione. |

**Spiegazione**: `GET` è safe e idempotente; `PUT` e `DELETE` sono idempotenti in termini dell'effetto richiesto, anche se eliminare due volte può produrre codici diversi. `POST` non è garantito idempotente: ripetere la richiesta può creare risorse multiple, a meno di introdurre un meccanismo applicativo di idempotency key. Uno status **500** non è una risposta appropriata per una normale validazione fallita del client: in molti casi è corretto `400` o altro codice 4xx.

## Caso D - HTML: quali valori arrivano al server?

```html
<form action="/profilo" method="post">
  <input type="text" id="nickname">
  <input type="text" name="city" value="Napoli" readonly>
  <input type="text" name="role" value="utente" disabled>
  <input type="checkbox" name="promo">
  <input type="radio" name="theme" value="dark">
  <input type="radio" name="theme" value="light" checked>
  <button type="submit">Salva</button>
</form>
```

**Soluzione.** Il controllo nickname non ha **`name`**, quindi non contribuisce al form data set. `city=Napoli` viene inviato perché `readonly` non disabilita la submission. `role` è escluso perché `disabled`. Il checkbox non selezionato è escluso. Per il gruppo radio si invia `theme=light`, il valore del radio selezionato. Il body form-url-encoded contiene quindi, nel caso illustrato, coppie equivalenti a `city=Napoli&theme=light` (l'ordine non è elemento su cui fondare la logica). Un client potrebbe inviare volontariamente `role=admin` con una richiesta HTTP manuale: il server non può dedurre autorizzazioni dal fatto che il campo fosse disabilitato nel form. `label` e validazione HTML sono utili, ma non sostituiscono la verifica server-side.

## Caso E - Specificità, cascata e box model

```css
#intro { color: purple; }
article p.note { color: green; }
```

Con `<article><p id="intro" class="note">Testo</p></article>` e **stesse origine, importanza e layer**, vince **purple**, poiché `#intro` ha specificità (1,0,0), maggiore di `article p.note`, che ha (0,1,2). Se una dichiarazione rivale fosse collocata in un contesto di cascata con precedenza superiore, il semplice confronto di specificità potrebbe non decidere il vincitore.

Per un elemento con `width: 200px; padding: 20px; border: 2px solid; margin: 10px`, nel modello **content-box** la larghezza esterna fino al bordo è `200+40+4 = 244px` e con i margini orizzontali arriva a **264px** (in assenza di altri vincoli). Con **border-box**, `width:200px` comprende contenuto, padding e bordo; aggiungendo margini di 10px su ciascun lato lo spazio esterno nominale arriva a **220px**. L'effetto di percentuali e dimensioni disponibili dipende dal layout e dal containing block. Questo esercizio permette di distinguere dimensione del contenuto, dimensione del box e spazio esterno.

## Caso F - Flexbox o Grid?

**Domanda.** La pagina ha intestazione in alto, barra laterale e contenuto principale; dentro il contenuto ci sono pulsanti allineati lungo una riga. Si deve usare solo una tecnologia?

**Risposta.** No. È naturale usare **Grid** per le due colonne della struttura principale e **Flexbox** per l'allineamento degli elementi della barra di strumenti. Una griglia fluida come `grid-template-columns: 16rem minmax(0,1fr)` tiene una sidebar di ampiezza nominale stabile e un contenuto che assorbe lo spazio restante; un breakpoint può passare a una sola colonna. Un contenitore `.toolbar { display:flex; flex-wrap:wrap; gap:.5rem; }` dispone i controlli sull'asse principale e può mandare a capo quando manca spazio. Per componenti ospitati in pannelli di dimensione variabile, una **container query** può essere più appropriata di un breakpoint sul viewport.

**Distinzione da spiegare**: `justify-content` non significa sempre «allineamento orizzontale»; agisce sull'**asse principale**, che con `flex-direction:column` è verticale. `align-items` agisce sull'asse trasversale. In Grid le proprietà `grid-template-*` descrivono la griglia, mentre `grid-column`/`grid-row` posizionano gli item.

## Caso G - Hoisting, closure, riferimenti e this

```js
function adder() {
  let sum = 0;
  return (n) => { sum += n; return sum; };
}
const next = adder();
console.log(next(2), next(3));   // 2 5: closure sul binding sum

const first = { points: [1, 2, 3] };
const second = { ...first };     // copia superficiale
console.log(second.points);     // [ 1, 2, 3 ]: points resta condiviso
```

**Risposta.** La prima stampa è **`2 5`**, perché la closure mantiene il binding `sum` fra invocazioni. La seconda stampa è **`[1,2,3]`**, perché spread crea una copia superficiale: l'array annidato `points` resta condiviso. `const` impedisce di riassegnare `first` o `second`, non di modificare gli oggetti referenziati.

**Domanda su `this`.** Se `obj.greet()` usa `this.name`, il metodo ordinario usa tipicamente `obj` come receiver; se si scrive `const f = obj.greet; f()` il receiver può andare perso, in strict mode `this` può essere `undefined`. Una arrow function non ricostruisce automaticamente il receiver: cattura invece `this` dalla posizione lessicale. La definizione di un metodo su un prototipo consente condivisione fra istanze.

## Caso H - DOM, bubbling e delega degli eventi

Supponiamo:

```html
<ul id="todo-list">
  <li><button data-id="1">Completa</button></li>
  <li><button data-id="2">Elimina</button></li>
</ul>
```

Un click sul pulsante può seguire il percorso di propagazione dagli antenati verso il target e poi, se bubbling è previsto, dal pulsante fino a `ul` e oltre. Se il listener è su `ul`, **`event.currentTarget`** è `ul`, mentre **`event.target`** è il nodo su cui è originato il click (tipicamente il pulsante o un suo discendente). Il listener può fare `event.target.closest('button[data-id]')` per scoprire l'elemento pertinente. Questa è **event delegation**: funziona anche dopo aver inserito un nuovo `<li>` senza registrare un nuovo listener su ciascun pulsante.

`preventDefault()` impedisce, quando applicabile, un comportamento come la navigazione di un link o il submit del form; `stopPropagation()` impedisce che il segnale attraversi altri antenati. Non si deve usare l'uno come sostituto dell'altro. `querySelectorAll` produce una collezione generalmente **statica**; una `HTMLCollection` di `getElementsByClassName` può aggiornarsi automaticamente quando si modifica il DOM.

## Caso I - Ordine d'esecuzione e Fetch

```js
console.log('A');
setTimeout(() => console.log('B'), 0);
Promise.resolve().then(() => console.log('C'));
setTimeout(() => console.log('D'), 0);
```

**Risposta attesa nel modello ordinario:** `A`, `C`, `B`, `D`. Le istruzioni sincrone completano prima, poi viene processata la callback di Promise come **microtask**, mentre i timer schedulano le proprie callback in turni successivi dell'event loop (l'ordine può essere più complesso quando si introducono eventi o runtime differenti).

Per una richiesta:

```js
const response = await fetch('/api/todos/99');  // 404: fetch NON rigetta
const data = await response.json();
```

Se il server risponde `404` con JSON valido, **`fetch` può risolvere comunque con `Response`**, e `.json()` può riuscire a fare il parsing. Per sapere se la richiesta è applicativamente riuscita si deve controllare `response.ok`. Se il server risponde HTML o body vuoto, `.json()` può fallire a prescindere dal codice HTTP. In una funzione `async`, un'eccezione non catturata produce il **rifiuto** della Promise restituita.

## Caso L - Request pipeline Express e accesso al database

**Domanda.** Perché l'ordine di questi middleware è importante?

```js
app.use(express.json());
app.use('/api', requireAuth);
app.post('/api/todos', createTodo);
app.use(errorHandler);
```

Il primo middleware analizza il body JSON e valorizza `req.body`. Il secondo, montato su `/api`, controlla l'identità/il token e può interrompere la richiesta con `401` oppure passare a `next()`. Il terzo legge dati validati, invoca la logica applicativa e crea un record nel database; il quarto gestisce errori inoltrati o lanciati secondo le regole della versione Express. Se mancasse `next()` e non venisse prodotta una risposta, il client potrebbe restare in attesa. Se la rotta fosse registrata prima del middleware di autenticazione, potrebbe essere raggiungibile senza controllo, se un handler terminale rispondesse direttamente.

Un controller dovrebbe distinguere almeno questi casi: **body malformato/valori invalidi** (`400` o altro 4xx pertinente), **utente non autenticato** (`401`), **utente non autorizzato sul record** (`403` oppure scelta coerente di non rivelare esistenza), **record inesistente** (`404`), **errore interno inatteso** (`500`). Query ORM come `Todo.findAll({where:{userId:req.user.id}})` non devono usare ciecamente l'ID utente fornito dal client: è il contesto autenticato a stabilire l'identità.

## Caso M - Sessione, JWT e attacchi: dove si decide la fiducia?

Una web app protegge `/api/users/3/orders/18`. Il browser ha un token il cui payload dichiara `role: "admin"`. **È sufficiente?** No: il server deve verificare la firma, l'algoritmo e i claim rilevanti del token, poi applicare la propria **policy di autorizzazione** all'azione e alla risorsa. Non basta decodificare il payload in Base64url. Un JWT firmato può essere **letto** dal possessore; non vi vanno memorizzati segreti in chiaro assumendo che la firma li nasconda.

**Sessione vs token**: se la sessione risiede sul server, il cookie con un ID imprevedibile identifica un record validato nello store; invalidare il record può revocare subito l'accesso. Un JWT breve e autonomamente verificabile può evitare il lookup, ma richiede considerazioni su revoca anticipata, rotazione e compromissione. In entrambi i casi è necessario HTTPS. Se il browser invia automaticamente il cookie, una rotta che modifica dati deve difendersi da **CSRF**; se JavaScript non fidato può leggere credenziali o dati, esiste rischio **XSS**.

**CORS** risponde a un'altra domanda: lo script eseguito su `https://frontend.example` può leggere una risposta dell'API ospitata su `https://api.example`? Poiché gli host sono diversi, le origin sono diverse; il browser verifica gli header CORS dell'API. **Non** decide se l'utente abbia il permesso di vedere l'ordine 18: quello compete alle regole di autorizzazione del backend.

## Caso N - Angular: il percorso completo di un evento

**Scenario.** L'utente preme «Completa» su un to-do mostrato da un componente figlio. Il figlio emette con `@Output()` l'ID al genitore; il genitore chiama `TodoService.complete(id)`; il service invia una richiesta `PATCH` tramite `HttpClient`, ottenendo un **Observable**; l'**interceptor** può aggiungere l'header di autenticazione; il backend verifica il token e la proprietà del to-do; a successo, il genitore aggiorna il proprio **signal** e il template si aggiorna tramite il meccanismo reattivo Angular.

**Spiegazione da esame.** `@Output()` serve per **comunicazione di componenti**, non equivale a una richiesta HTTP; `Observable` descrive un flusso e deve essere consumato nella forma prevista; `signal` rappresenta il **valore corrente**; `computed` deriva un valore e non si imposta manualmente. Una **route guard** può impedire la navigazione verso una pagina privata, ma un utente può invocare l'endpoint direttamente con `curl`: il backend deve ripetere tutti i controlli.

Se il form è **reactive**, le verifiche `Validators` migliorano l'input e abilitano/disabilitano l'azione, ma il server deve verificare autonomamente payload, identità e permessi. Un form *template-driven* descrive maggior parte della configurazione nel template; un form *reactive* porta il modello nel codice TypeScript.

## Caso O - Testing: che cosa prova ciascun test?

**Domanda.** Un componente Angular mostra i to-do caricati da un servizio; un test sostituisce il servizio con un mock che restituisce sempre la stessa lista e verifica il testo nel DOM. È unit test o E2E? È un **test del componente con dipendenze controllate** (unit/component test), non un test dell'intero server. Non prova che il database sia disponibile o che l'endpoint HTTP sia corretto, ma permette di attribuire eventuali fallimenti al componente con minore rumore.

Un test **E2E Playwright**, invece, avvia l'app completa, apre il browser, effettua login, aggiunge un to-do e verifica che risulti nell'elenco. Può scoprire errori di integrazione tra browser, API, autenticazione e persistenza, ma è più costoso, può soffrire di *flakiness* e richiede dati di test isolati. Se una suite ha **100% di line coverage**, non significa che ogni scelta logica sia verificata: senza asserzioni sui rami e casi limite si possono avere difetti non scoperti.

**Locator robusto**: `getByRole('button', {name:'Accedi'})` esprime la semantica dell'azione; `div:nth-child(4) > span.btn-primary` dipende molto dalla struttura e dallo stile. Le asserzioni asincrone di Playwright attendono il soddisfacimento della condizione entro un timeout; aggiungere sistematicamente `waitForTimeout(3000)` non è una strategia solida. **Capture and Replay** accelera la registrazione dei passi, ma occorre rivedere significato, qualità dei locator e controllo dei risultati attesi.

# Ripasso finale - collegamenti trasversali per l'esame

## Il viaggio completo di una richiesta Web

Un utente visita `https://app.example.org/todos`: il browser risolve il nome tramite **DNS** (stub → resolver → autoritativi o cache), stabilisce una connessione protetta tramite **TLS** su un trasporto adatto, invia una richiesta **HTTP** con URL/path e intestazioni come `Host`, e riceve una rappresentazione HTML/JS/CSS, eventualmente dalla **cache**. Il browser costruisce il **DOM**, applica la **cascata e il layout CSS**, esegue il **JavaScript**. In una **SPA** il router client sceglie la vista Angular, i componenti mostrano lo stato e `HttpClient` interroga una **REST API**. La richiesta arriva al server **Node/Express**, attraversa i **middleware**, viene autenticata e autorizzata, poi il controller/servizio usa un **ORM** per leggere dati da un RDBMS. La risposta JSON torna al browser, dove il flusso asincrono si completa, lo stato reattivo cambia e Angular aggiorna la vista. **CORS/SOP**, TLS, validazione, controlli di accesso e mitigazioni di XSS/CSRF operano in punti diversi di questo percorso. Test unitari, di integrazione ed E2E verificano parti e scenari complessivi.

## Contrasti da saper spiegare senza esitazioni

| Coppia di concetti | Differenza decisiva |
| --- | --- |
| DNS dominio / zona | Sottoalbero logico / dati soggetti a un'autorità amministrativa. |
| NXDOMAIN / NODATA | Nome inesistente / nome esistente senza RR del tipo chiesto. |
| HTTP stateless / sessione | Il protocollo non ricorda richieste / l'app ricostruisce contesto. |
| Cache fresh / stale | Può essere riusata / necessita in genere di validazione. |
| `no-cache` / `no-store` | Memorizza ma valida / non memorizza. |
| ETag / Last-Modified | Identificatore di versione / timestamp come validatore. |
| HTTP/2 / HTTP/3 | TCP con stream HTTP / QUIC con stream indipendenti. |
| HTML / CSS / JavaScript | Struttura e semantica / presentazione / comportamento. |
| Specificità / ereditarietà | Risolve regole concorrenti / trasferisce valori da antenati. |
| Flexbox / Grid | Layout monodimensionale / bidimensionale. |
| `let` / `const` / `var` | Riassegnabile a blocchi / binding costante a blocchi / scope di funzione. |
| `==` / `===` | Consente coercizioni / confronto stretto. |
| `for...of` / `for...in` | Valori iterati / nomi di proprietà enumerabili. |
| `map` / `forEach` | Trasformazione che restituisce array / iterazione per effetti. |
| `this` ordinario / arrow | Dipende dalla chiamata / cattura `this` lessicale. |
| DOM node / DOM element | Qualsiasi nodo / nodo che rappresenta un elemento. |
| `innerHTML` / `textContent` | Interpreta markup / tratta il dato come testo. |
| Promise / Observable / Signal | Risultato asincrono / flusso nel tempo / stato reattivo corrente. |
| `fetch` / `response.json()` | Risposta HTTP iniziale / parsing asincrono del corpo. |
| Cookie / sessione / JWT | Meccanismo browser / contesto logico / formato di token. |
| Framework / libreria | Governa flusso e invoca codice / è richiamata dal programma. |
| ORM / SQL | Astrazione a oggetti / linguaggio di interrogazione relazionale. |
| Authentication / authorization | Stabilisce l'identità / controlla i permessi. |
| `401` / `403` | Non autenticato / autenticato o identificato ma senza permessi. |
| JWT firmato / cifrato | Integrità/autenticità / confidenzialità. |
| SPA / MPA | Vista client senza full reload / navigazione caricando documenti. |
| Angular Input / Output | Genitore → figlio / figlio → genitore. |
| Unit / E2E testing | Unità isolata / workflow completo come utente. |
| XSS / CSRF / SQL injection | Codice nel browser / richiesta indotta / query SQL alterata. |
| Same-Origin Policy / CORS | Restrizione del browser / eccezioni dichiarate via header. |

## Autoverifica rapida: dodici domande orali

1. **Perché `Host` è necessario dopo il DNS?** Il DNS risolve un nome in un indirizzo, ma sullo stesso indirizzo può esistere più di un virtual host. L'header consente al server di scegliere quello richiesto.

2. **Chi segue i referral della risoluzione DNS?** Il resolver ricorsivo, non normalmente l'applicazione client; può ottenere informazioni intermedie già disponibili in cache.

3. **La risposta `304` contiene la nuova risorsa?** No: segnala che la rappresentazione già salvata può essere riutilizzata dopo la validazione, secondo i metadati forniti.

4. **Come si riconosce il tipo di body?** Principalmente da `Content-Type`; `Accept` riguarda invece le rappresentazioni richieste dal client e non descrive di per sé il body ricevuto.

5. **Perché un file HTML può produrre un DOM diverso dal markup scritto?** Il parser HTML applica regole di recupero degli errori e può inserire o ricollocare nodi impliciti.

6. **Quando usare una container query?** Quando lo stile di un componente deve dipendere dallo spazio che gli concede il suo contenitore, non soltanto dalla larghezza della finestra.

7. **`let x = obj` crea un clone?** No: copia il riferimento. Anche `{...obj}` è solo una copia superficiale; gli oggetti annidati possono rimanere condivisi.

8. **Un callback asincrono può bloccare Node?** Sì, se contiene calcoli sincroni intensivi: quando esegue JavaScript sul thread principale, l'event loop non può servire contemporaneamente altre callback.

9. **Che differenza c'è tra validazione e autorizzazione?** La prima controlla che l'input rispetti forma e vincoli, la seconda che il richiedente abbia diritto a compiere l'operazione su quella risorsa.

10. **In TypeScript, perché `unknown` è più sicuro di `any`?** Perché obbliga a restringere o controllare il tipo prima di accedere a proprietà e invocare metodi.

11. **Angular deve proteggere la rotta se il backend controlla già il token?** Una guard è utile per l'esperienza utente, ma la difesa autorevole è il controllo del token e dei permessi effettuato dal backend su ogni richiesta.

12. **Perché un test con coverage elevata può essere insufficiente?** La coverage misura esecuzione, non correttezza delle asserzioni; un flusso può attraversare molte righe senza verificare gli esiti importanti.

> [!info] Controllo personale prima dell'esame
> Si dovrebbe essere capaci di descrivere una risoluzione DNS completa; interpretare metodo, header, status, cache e semantica di una richiesta HTTP; comporre un form e spiegare i suoi dati; decidere un selettore CSS e giustificarne specificità/layout; interpretare callback, closure, Promise ed eventi DOM; scrivere una rotta Express protetta e spiegare `req`/`res`/`next`; associare un modello ORM a una API REST; leggere un tipo TypeScript e un template Angular; diagnosticare XSS/CSRF/SQL injection; distinguere un test unitario da un test Playwright E2E.

> [!info] Nota di fedeltà alla fonte
> La struttura tematica, le definizioni e gli esempi di tecnologie seguono le lezioni del PDF di partenza. Sono state sintetizzate le dimostrazioni operative ripetitive e accorpati alcuni passaggi; eventuali precisazioni di buona pratica, come la gestione sicura delle password, i limiti della protezione frontend e le sfumature di compatibilità dei framework, sono formulate per non scambiare un esempio didattico per codice già pronto alla produzione.