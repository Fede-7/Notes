# Lezione 17 Frontend Tooling

## Perché serve del tooling

I siti costruiti con le tecnologie fondamentali (HTML, CSS, JS) avevano un solo foglio di stile, poco client-side JavaScript e nessuna libreria esterna. I frontend moderni sono molto più complessi:

- Il codice client-side JavaScript cresce ed è sempre più complesso.
- Si usano molti moduli e librerie esterne.
- Serve transpilare e fare downleveling del codice.
- Si vogliono ottimizzare i file serviti.
- Si usano pre/post-processori per i fogli di stile, es. SASS.

Per sviluppare frontend complessi serve quindi del **tooling** che automatizzi questi passi: pre/post-processori CSS, framework CSS, bundling e minification, server di sviluppo e build.

## CSS pre e post processori

> [!def] CSS pre-processore
> **Compilatore speciale** che genera codice CSS a partire da file scritti in una sintassi propria, che estende il CSS base con nuove feature (es. variabili) per scrivere fogli di stile mantenibili in modo più efficiente.

I pre-processori più diffusi sono **Sass**, LESS e Stylus.

> [!def] CSS post-processore
> **Strumento** che processa e trasforma automaticamente fogli di stile CSS esistenti.

I post-processori si usano tipicamente per:

- **Downleveling**: riscrivere feature CSS recenti in sintassi compatibile con i browser vecchi (es. `oklch()` convertito in `rgb()`).
- **Autoprefixing**: aggiungere i prefissi vendor (es. `-webkit-`, `-o-`) alle proprietà che li richiedono.
- **Ottimizzazioni**: minificazione o eliminazione delle parti non usate.
- **Applicare convenzioni e rilevare errori**.

Il post-processore più popolare è **PostCSS**.

## SASS

> [!def] Sass
> **Pre-processore CSS** che si autodefinisce «CSS with superpowers», il più popolare in circolazione, attivo dal 2006.

Si installa facilmente via npm con `npm install -g sass`, che rende disponibile il binario `sass`; la compilazione è `sass input.scss output.css`.

Sass supporta **due sintassi**:

- **SCSS** (estensione `.scss`): superset del CSS, la più popolare.
- **Indented syntax** (estensione `.sass`): basata sull'indentazione come Python, era la sintassi originale.

### Variabili e nesting

- **Variabili**: dichiarate con `$nome`, permettono di riusare valori nel foglio di stile; alla compilazione vengono sostituite col loro valore.
- **Nesting**: le regole possono essere annidate seguendo la gerarchia degli elementi HTML, es. `a` dentro `span` dentro `.elem`; il CSS generato espande i selettori combinati (`.elem span a`).

```scss
$primary-color: #333;
nav {
  ul { margin: 0; padding: 0; list-style: none; }
  li { display: inline-block; }
  a { display: block; padding: 6px 12px; text-decoration: none; }
}
```

> [!warning] Nesting eccessivo
> Troppo nesting è una cattiva pratica: porta a CSS eccessivamente specifico.

### Mixin

> [!def] Mixin
> **Gruppo riutilizzabile** di dichiarazioni CSS/Sass, dichiarato con l'at-rule `@mixin` seguita da un identificatore e incluso con `@include`; può accettare uno o più parametri opzionali, anche con valori di default.

```scss
@mixin theme($color: DarkBlue) {
  background: $color;
  color: #fff;
}
.info   { @include theme; }
.danger { @include theme($color: DarkRed); }
```

### Moduli e partial

- **Moduli**: un file può usare le definizioni di un altro con `@use 'base'` e accedervi col namespace, es. `base.$primary-color`.
- **Partial**: i file Sass il cui nome inizia con underscore (es. `_variables.scss`) sono pensati per essere inclusi da altri file; Sass **non genera** un CSS standalone per essi — utile, ad esempio, per un file di sole variabili.

### Liste, mappe e control flow

- **Lista**: sequenza di valori separati da virgole, spazi o slash, purché coerente nella lista.
- **Map**: sequenza di coppie `<chiave>: <valore>` con chiavi uniche, es. `("xs": 480px, "md": 768px)`.

Sass fornisce **regole di controllo del flusso** per decidere se e quante volte emettere gli stili, come un template engine per generare CSS:

- `@if` / `@else`: emette stili in modo condizionale.
- `@each`: itera su tutti gli elementi di una lista o mappa, es. per generare media query per ogni breakpoint.
- `@for` e `@while`: le consuete semantiche di iterazione.

## Framework CSS

I framework CSS non sono framework software veri e propri: sono un insieme di **stili general-purpose** pronti all'uso. Risolvono problemi ricorrenti:

- Creare un sistema di layout.
- Creare una tipografia consistente.
- Stilizzare tabelle, liste e componenti UI.
- Azzerare gli stili user agent per un aspetto consistente su ogni browser.

I framework più diffusi sono **Bootstrap** (il più popolare, originario di Twitter), **Tailwind** (noto per l'approccio *utility-first*), Materialize, Foundation, Bulma e PureCSS.

### Uso e personalizzazione

Il framework è un insieme di file CSS da importare nelle pagine, usando le classi documentate: si possono servire dal proprio server o tramite **CDN** — comodo per il prototipazione, ma solleva qualche problema di privacy.

Due approcci per non avere un sito identico a mille altri:

- **Personalizzare la build**: la maggior parte dei framework è costruita con Sass o simili; si possono cambiare le variabili di build (colori, font, dimensioni…) e ricompilare il framework, es. importare `bootstrap.scss` dopo aver ridefinito `$primary` e `$secondary`.
- **Override CSS**: definire stili custom che sovrascrivono alcuni stili del framework.

## Bundling e minification

> [!def] Bundling
> **Tecnica** che combina più file CSS o JS in un unico file, così il browser esegue meno richieste HTTP per caricare la pagina.

Il bundling è un'ottimizzazione delle prestazioni ampiamente adottata perché ogni richiesta HTTP aggiuntiva introduce latenza: le strategie di caching aiutano i caricamenti successivi, ma il primo caricamento resta penalizzato da molti stylesheet e script.

> [!warning] L'ordine conta
> L'ordine con cui i file vengono concatenati nel bundle è significativo: può cambiare il comportamento della pagina.

Nota storica: prima che i moduli ES fossero disponibili nei browser, non c'era modo di scrivere codice JS modulare per il client; i bundler (Webpack, Rollup, Parcel) si occupavano di concatenare i moduli sorgente in un modo comprensibile ai browser.

> [!def] Tree shaking
> **Eliminazione del codice morto** (dead code elimination) eseguita dai bundler: analizzando import ed export, pota dal bundle finale tutto il codice non usato dei moduli importati, con un impatto significativo sulle dimensioni del bundle.

### Minification

> [!def] Minification
> **Processo di ottimizzazione** del trasferimento dei file che rimuove gli spazi "non necessari" e accorcia il codice sorgente senza impattarne la funzionalità; i file risultanti sono detti *minified*.

Gli umani hanno bisogno di indentazione e nomi di variabile significativi per leggibilità, manutenibilità e capibilità; i browser non necessitano di codice leggibile. L'effetto cresce con la dimensione dei file:

- React 18.2.0 pesa ~85 kB, la versione minificata ~25 kB: ~70% di compressione.
- Moment.js 2.29.4 pesa ~151 kB, la versione minificata ~75 kB: ~50% di compressione.

## Vite

> [!def] Vite
> **Strumento di supporto** allo sviluppo e al deploy di progetti web, con due componenti chiave: un **development server** con funzionalità avanzate per lo sviluppo, e un **build tool** che produce asset statici altamente ottimizzati, pronti per la produzione.

Un progetto Vite si crea con `npm create vite@latest`, scegliendo framework e variante (es. TypeScript). Lo scaffolding generato prevede tre script:

- `npm run dev`: avvia il dev server, che osserva i cambiamenti ai sorgenti e ricarica automaticamente l'app quando serve (**live reload**).
- `npm run build`: genera un bundle ottimizzato, pronto per la produzione.
- `npm run preview`: un semplice server statico che serve i file generati in fase di build.

Per usare un foglio di stile Sass nel progetto si installa `npm install -D sass`, si crea il file `.scss` e lo si importa nel `main.ts`: Vite lo rileva, lo compila con `sass` e lo aggiunge al bundle dopo il CSS originale.

### La fase di build

Durante la build Vite svolge parecchio lavoro automaticamente:

- Analizza le risorse statiche effettivamente usate nell'app.
- Compila i file Sass (risp. TypeScript) in CSS (risp. JavaScript).
- Raggruppa in un singolo bundle i file CSS e i file JavaScript.
- Minifica i bundle.
- Applica il **filename fingerprinting** ai bundle finali.
- Sposta tutte le risorse in `/dist` e aggiorna l'`index.html` con i riferimenti corretti.

> [!def] Filename fingerprinting
> **Tecnica** che nomina i bundle finali con un hash del loro contenuto (es. `index-DiAK_ebR.js`): quando il contenuto cambia, cambia anche il nome del file, il che evita i problemi di **cache staleness** — il browser non continua a usare la vecchia versione in cache come farebbe con un nome fisso come `index.js`.