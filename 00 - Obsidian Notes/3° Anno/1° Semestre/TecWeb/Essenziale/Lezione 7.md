# Lezione 07: Modern, Adaptive CSS

Estensione dei concetti già visti (selettori, cascata, box model, normal flow, posizionamento, Flexbox, Grid, media query) tramite nuove funzionalità del CSS moderno.

## Pseudo-classi funzionali

> [!info] Contesto
> I selettori semplici possono combinarsi in relazioni complesse, ma le liste di selettori ripetitive allungano i fogli di stile (meno efficienti da caricare) e rendono le modifiche più soggette a errori. Strumenti come **Sass** (pre/post-processore) si sono diffusi proprio per organizzare i fogli di stile; il CSS moderno ha incorporato direttamente nel linguaggio capacità analoghe.

> [!def] Pseudo-classi funzionali
> Pseudo-classi che accettano selettori come argomenti e consentono di scrivere selettori in modo più conciso.
> - **`:is()`** raggruppa selettori alternativi.
> - **`:where()`** crea default facilmente sovrascrivibili.
> - **`:not()`** esclude gli elementi che corrispondono.
> - **`:has()`** seleziona elementi in base a elementi correlati.

### `:is()` (matches-any)

- **`:is()`** corrisponde a un elemento se uno dei suoi selettori argomento corrisponde; è utile quando in un selettore complesso cambia solo una parte.

```css
:is(header, main, footer) a em { color: red; }
button:is(:hover, :focus, :active) { color: red; }
```

### `:where()`

- **`:where()`** seleziona come `:is()`, ma contribuisce **specificità zero** alla cascata, per sé e per tutti i suoi argomenti.
- La conseguenza è che gli stili risultanti sono volutamente facili da sovrascrivere (utile per regole di default).

### `:not()`

- **`:not()`** corrisponde agli elementi che non corrispondono a nessuno dei suoi argomenti.

### `:has()`

- **`:has()`** corrisponde a elementi in base ai loro discendenti o elementi correlati, anche fratelli successivi.

```css
ol:has(.active) { background-color: lightgray; }
li:has(+ .selected) { color: red; }
```

### Specificità delle pseudo-classi funzionali

- Le pseudo-classi funzionali **non contano come pseudo-classi** nel calcolo della specificità (non entrano in B come `:focus` o `:hover`).
- **`:where()`** e il suo contenuto contribuiscono sempre **zero specificità**.
- Per **`:is()`**, **`:not()`** e **`:has()`** la specificità è quella dell'argomento più specifico.

## Custom properties (variabili CSS)

- I valori ripetuti nel CSS sono difficili da mantenere: se un valore cambia, va modificato in ogni occorrenza.

> [!def] Custom properties
> Entità definite dagli autori CSS che rappresentano valori specifici riutilizzabili; si definiscono con la sintassi delle proprietà personalizzate (o con l'at-rule `@property`) e si recuperano con `var()`.

```css
:root {
  --primary-color: #663399;
}
h1 { color: var(--primary-color); }
```

### Ereditarietà

- Le custom properties **partecipano alla cascata**, sono **normalmente ereditate** e possono essere **sovrascritte**.
- La pseudo-classe **`:root`** corrisponde alla radice dell'albero del documento e permette di definire custom property «globali»; un elemento antenato può poi ridefinire la stessa proprietà, e i discendenti ereditano il nuovo valore.

```css
:root { --accent: #cfa2fb; }
button { background: var(--accent); }
.warning { --accent: orangered; }
```

### Fallback

- **Fallback**: `var()` accetta un valore di riserva come secondo argomento, usato se la custom property non è definita.

```css
.notice { color: var(--notice-color, darkred); }
```

- I fallback sono utili quando un componente ammette **personalizzazione opzionale**.

### At-rule `@property`

- **`@property`** permette di personalizzare il comportamento di ereditarietà di una custom property, dichiarandone sintassi, ereditarietà e valore iniziale.

```css
@property --accent {
  syntax: "<color>";
  inherits: false;
  initial-value: teal;
}
```

## Valori calcolati

### `calc()`

- **`calc()`** combina valori e unità compatibili con gli operatori aritmetici `+`, `-`, `*`, `/`.

```css
.item { width: calc(100% - 20px); margin: auto; }
```

### `min()` e `max()`

- **`min()`** e **`max()`** selezionano rispettivamente il più piccolo e il più grande dei loro argomenti.
- Con `width: min(100px, calc(100% - 2rem))` l'elemento non supera mai 100px, si restringe quando lo spazio disponibile è minore e conserva almeno 1rem per lato.
- Con `font-size: max(1rem, 10vw)` la dimensione del font non scende mai sotto 1rem e può crescere su viewport più larghi.

### `clamp()`

- **`clamp()`** vincola un valore tra un minimo e un massimo: il valore cresce fluidamente ma non supera mai i limiti.

## Unità viewport su dispositivi mobili

- **`100vh`** rappresenta l'altezza del viewport; su desktop si basa sulla dimensione corrente della finestra, ma su mobile i controlli del browser (es. barra degli indirizzi) possono apparire e scomparire, complicando il calcolo.

> [!info] Unità viewport moderne
> - **`svh`** (small viewport height): altezza del viewport calcolata con la barra di navigazione visibile.
> - **`lvh`** (large viewport height): calcolata sull'altezza massima possibile del viewport (come `vh`).
> - **`dvh`** (dynamic viewport height): rappresenta dinamicamente l'altezza corrente del viewport; con i controlli visualizzati corrisponde a `lvh` meno l'altezza dei controlli (`svh`), senza controlli coincide con `lvh`.

## Pattern di layout moderni

### `gap`

- La proprietà **`gap`** si usa sui container **flex** e **grid** per aggiungere spazio tra i figli.
- A differenza dei margini sui singoli figli, `gap` aggiunge spazio **solo tra gli elementi** (non ai bordi del container).

### Shorthand `flex`

- Lo shorthand **`flex`** controlla quanto un item cresce (**`flex-grow`**), quanto si restringe (**`flex-shrink`**) e la sua dimensione base iniziale (**`flex-basis`**).

```css
.item { flex: 1 1 100px; }  /* equivale a flex-grow:1; flex-shrink:1; flex-basis:100px */
```

## Container queries

- Le **media query** osservano il viewport, ma lo stesso componente può trovarsi in container di dimensioni diverse (area principale oppure sidebar/colonna di griglia più piccola): in un container piccolo il componente dovrebbe comportarsi come in un viewport piccolo, anche se il viewport è grande.

> [!def] Container queries
> Regole che permettono di stilare un componente in base alla dimensione di un antenato; richiedono la dichiarazione della proprietà `container-type` sull'antenato e l'uso dell'at-rule `@container` per la query.

```css
aside { container-type: inline-size; }
@container (max-width: 300px) {
  .card { background-color: lightgreen; }
  .card :is(h2, p) { font-size: 1em; }
}
```

## Candidati immagine responsive

- Il CSS determina quanto grande viene mostrata un'immagine, ma scaricare un'immagine ad alta risoluzione e scalarla su schermi piccoli è inefficiente.
- L'**HTML** può fornire più file per la stessa immagine: il browser seleziona il migliore candidato in base al dispositivo, scaricando solo la versione necessaria, tramite l'attributo **`srcset`** o l'elemento **`<picture>`**.

### `srcset`

- L'attributo **`src`** funge da fallback (quando `srcset` non è supportato); `srcset` specifica una lista di nomi di file con **descrittori**:
  - **descrittori di larghezza** (numero seguito da `w`): dimensione intrinseca dell'immagine;
  - **descrittori di densità di pixel** (numero seguito da `x`): densità di pixel del dispositivo rispetto alla densità standard.

```html
<img src="fu-tzu-400.jpg"
     srcset="fu-tzu-400.jpg 400w, fu-tzu-800.jpg 800w, fu-tzu-1200.jpg 1200w"
     alt="Portrait of the great master Fu-Tzu">
```

### `<picture>` e art direction

> [!def] Art direction
> Processo di selezione del media migliore per condizioni specifiche: non solo diverse risoluzioni della stessa immagine, ma anche contenuti diversi (es. un grafico con meno dettagli su mobile e completo su desktop).

```html
<picture>
  <source media="(max-width: 200px)" srcset="fu-tzu-400.png">
  <source media="(max-width: 400px)" srcset="fu-tzu-800.png">
  <img src="fu-tzu-1200.png" alt="Portrait of the great master Fu-Tzu">
</picture>
```

## Media query e preferenze utente

- Le media query possono testare più delle dimensioni del viewport: riflettono anche le **preferenze dell'utente**, normalmente originate dalle impostazioni del browser o del sistema operativo:
  - **schema di colori preferito**: `@media (prefers-color-scheme: dark)`;
  - **movimento ridotto**: `@media (prefers-reduced-motion: reduced)`;
  - **contrasto aumentato o ridotto**: `@media (prefers-contrast: more)`;
  - **trasparenza ridotta**: `@media (prefers-reduced-transparency: reduced)`.

```css
:root { --bg-color: white; --text-color: indigo; }
@media (prefers-color-scheme: dark) {
  :root { --bg-color: indigo; --text-color: white; }
}
```

## Query `@supports`

- **`@supports`** applica gli stili solo quando certe coppie proprietà/valore sono supportate; la regola base funge da **fallback** e il layout avanzato (es. griglia) è applicato solo se il browser lo supporta.

```css
.cards { display: block; }
@supports (display: grid) {
  .cards { display: grid; grid-template-columns: 1fr 1fr; }
}
```

## Nesting nativo del CSS

- Nel CSS moderno i selettori correlati possono essere **nidificati** all'interno di altre regole, evitando di ripetere il selettore padre.

```css
.card {
  background-color: lightblue;
  :is(h2, p) { font-size: 1.25em; }
}
```

### Selettore di nesting: `&`

- Il selettore **`&`** in un selettore nidificato si riferisce esplicitamente al selettore della regola padre.

```css
.card {
  background: white;
  &:hover { background: lavender; }
  & > h2 { color: rebeccapurple; }
}
```

> [!warning] Prudenza con il nesting
> Mantenere il nesting poco profondo: un eccesso di nidificazione rende i selettori e il comportamento della cascata più difficili da capire.

# Lezione 08 — Modern, Adaptive CSS

Estensione dei concetti già visti (selettori, cascata, box model, normal flow, posizionamento, Flexbox, Grid, media query) tramite nuove funzionalità del CSS moderno.

## Pseudo-classi funzionali

> [!info] Contesto
> I selettori semplici possono combinarsi in relazioni complesse, ma le liste di selettori ripetitive allungano i fogli di stile (meno efficienti da caricare) e rendono le modifiche più soggette a errori. Strumenti come **Sass** (pre/post-processore) si sono diffusi proprio per organizzare i fogli di stile; il CSS moderno ha incorporato direttamente nel linguaggio capacità analoghe.

> [!def] Pseudo-classi funzionali
> Pseudo-classi che accettano selettori come argomenti e consentono di scrivere selettori in modo più conciso.
> - **`:is()`** raggruppa selettori alternativi.
> - **`:where()`** crea default facilmente sovrascrivibili.
> - **`:not()`** esclude gli elementi che corrispondono.
> - **`:has()`** seleziona elementi in base a elementi correlati.

### `:is()` (matches-any)

- **`:is()`** corrisponde a un elemento se uno dei suoi selettori argomento corrisponde; è utile quando in un selettore complesso cambia solo una parte.

```css
:is(header, main, footer) a em { color: red; }
button:is(:hover, :focus, :active) { color: red; }
```

### `:where()`

- **`:where()`** seleziona come `:is()`, ma contribuisce **specificità zero** alla cascata, per sé e per tutti i suoi argomenti.
- La conseguenza è che gli stili risultanti sono volutamente facili da sovrascrivere (utile per regole di default).

### `:not()`

- **`:not()`** corrisponde agli elementi che non corrispondono a nessuno dei suoi argomenti.

### `:has()`

- **`:has()`** corrisponde a elementi in base ai loro discendenti o elementi correlati, anche fratelli successivi.

```css
ol:has(.active) { background-color: lightgray; }
li:has(+ .selected) { color: red; }
```

### Specificità delle pseudo-classi funzionali

- Le pseudo-classi funzionali **non contano come pseudo-classi** nel calcolo della specificità (non entrano in B come `:focus` o `:hover`).
- **`:where()`** e il suo contenuto contribuiscono sempre **zero specificità**.
- Per **`:is()`**, **`:not()`** e **`:has()`** la specificità è quella dell'argomento più specifico.

## Custom properties (variabili CSS)

- I valori ripetuti nel CSS sono difficili da mantenere: se un valore cambia, va modificato in ogni occorrenza.

> [!def] Custom properties
> Entità definite dagli autori CSS che rappresentano valori specifici riutilizzabili; si definiscono con la sintassi delle proprietà personalizzate (o con l'at-rule `@property`) e si recuperano con `var()`.

```css
:root {
  --primary-color: #663399;
}
h1 { color: var(--primary-color); }
```

### Ereditarietà

- Le custom properties **partecipano alla cascata**, sono **normalmente ereditate** e possono essere **sovrascritte**.
- La pseudo-classe **`:root`** corrisponde alla radice dell'albero del documento e permette di definire custom property «globali»; un elemento antenato può poi ridefinire la stessa proprietà, e i discendenti ereditano il nuovo valore.

```css
:root { --accent: #cfa2fb; }
button { background: var(--accent); }
.warning { --accent: orangered; }
```

### Fallback

- **Fallback**: `var()` accetta un valore di riserva come secondo argomento, usato se la custom property non è definita.

```css
.notice { color: var(--notice-color, darkred); }
```

- I fallback sono utili quando un componente ammette **personalizzazione opzionale**.

### At-rule `@property`

- **`@property`** permette di personalizzare il comportamento di ereditarietà di una custom property, dichiarandone sintassi, ereditarietà e valore iniziale.

```css
@property --accent {
  syntax: "<color>";
  inherits: false;
  initial-value: teal;
}
```

## Valori calcolati

### `calc()`

- **`calc()`** combina valori e unità compatibili con gli operatori aritmetici `+`, `-`, `*`, `/`.

```css
.item { width: calc(100% - 20px); margin: auto; }
```

### `min()` e `max()`

- **`min()`** e **`max()`** selezionano rispettivamente il più piccolo e il più grande dei loro argomenti.
- Con `width: min(100px, calc(100% - 2rem))` l'elemento non supera mai 100px, si restringe quando lo spazio disponibile è minore e conserva almeno 1rem per lato.
- Con `font-size: max(1rem, 10vw)` la dimensione del font non scende mai sotto 1rem e può crescere su viewport più larghi.

### `clamp()`

- **`clamp()`** vincola un valore tra un minimo e un massimo: il valore cresce fluidamente ma non supera mai i limiti.

## Unità viewport su dispositivi mobili

- **`100vh`** rappresenta l'altezza del viewport; su desktop si basa sulla dimensione corrente della finestra, ma su mobile i controlli del browser (es. barra degli indirizzi) possono apparire e scomparire, complicando il calcolo.

> [!info] Unità viewport moderne
> - **`svh`** (small viewport height): altezza del viewport calcolata con la barra di navigazione visibile.
> - **`lvh`** (large viewport height): calcolata sull'altezza massima possibile del viewport (come `vh`).
> - **`dvh`** (dynamic viewport height): rappresenta dinamicamente l'altezza corrente del viewport; con i controlli visualizzati corrisponde a `lvh` meno l'altezza dei controlli (`svh`), senza controlli coincide con `lvh`.

## Pattern di layout moderni

### `gap`

- La proprietà **`gap`** si usa sui container **flex** e **grid** per aggiungere spazio tra i figli.
- A differenza dei margini sui singoli figli, `gap` aggiunge spazio **solo tra gli elementi** (non ai bordi del container).

### Shorthand `flex`

- Lo shorthand **`flex`** controlla quanto un item cresce (**`flex-grow`**), quanto si restringe (**`flex-shrink`**) e la sua dimensione base iniziale (**`flex-basis`**).

```css
.item { flex: 1 1 100px; }  /* equivale a flex-grow:1; flex-shrink:1; flex-basis:100px */
```

## Container queries

- Le **media query** osservano il viewport, ma lo stesso componente può trovarsi in container di dimensioni diverse (area principale oppure sidebar/colonna di griglia più piccola): in un container piccolo il componente dovrebbe comportarsi come in un viewport piccolo, anche se il viewport è grande.

> [!def] Container queries
> Regole che permettono di stilare un componente in base alla dimensione di un antenato; richiedono la dichiarazione della proprietà `container-type` sull'antenato e l'uso dell'at-rule `@container` per la query.

```css
aside { container-type: inline-size; }
@container (max-width: 300px) {
  .card { background-color: lightgreen; }
  .card :is(h2, p) { font-size: 1em; }
}
```

## Candidati immagine responsive

- Il CSS determina quanto grande viene mostrata un'immagine, ma scaricare un'immagine ad alta risoluzione e scalarla su schermi piccoli è inefficiente.
- L'**HTML** può fornire più file per la stessa immagine: il browser seleziona il migliore candidato in base al dispositivo, scaricando solo la versione necessaria, tramite l'attributo **`srcset`** o l'elemento **`<picture>`**.

### `srcset`

- L'attributo **`src`** funge da fallback (quando `srcset` non è supportato); `srcset` specifica una lista di nomi di file con **descrittori**:
  - **descrittori di larghezza** (numero seguito da `w`): dimensione intrinseca dell'immagine;
  - **descrittori di densità di pixel** (numero seguito da `x`): densità di pixel del dispositivo rispetto alla densità standard.

```html
<img src="fu-tzu-400.jpg"
     srcset="fu-tzu-400.jpg 400w, fu-tzu-800.jpg 800w, fu-tzu-1200.jpg 1200w"
     alt="Portrait of the great master Fu-Tzu">
```

### `<picture>` e art direction

> [!def] Art direction
> Processo di selezione del media migliore per condizioni specifiche: non solo diverse risoluzioni della stessa immagine, ma anche contenuti diversi (es. un grafico con meno dettagli su mobile e completo su desktop).

```html
<picture>
  <source media="(max-width: 200px)" srcset="fu-tzu-400.png">
  <source media="(max-width: 400px)" srcset="fu-tzu-800.png">
  <img src="fu-tzu-1200.png" alt="Portrait of the great master Fu-Tzu">
</picture>
```

## Media query e preferenze utente

- Le media query possono testare più delle dimensioni del viewport: riflettono anche le **preferenze dell'utente**, normalmente originate dalle impostazioni del browser o del sistema operativo:
  - **schema di colori preferito**: `@media (prefers-color-scheme: dark)`;
  - **movimento ridotto**: `@media (prefers-reduced-motion: reduced)`;
  - **contrasto aumentato o ridotto**: `@media (prefers-contrast: more)`;
  - **trasparenza ridotta**: `@media (prefers-reduced-transparency: reduced)`.

```css
:root { --bg-color: white; --text-color: indigo; }
@media (prefers-color-scheme: dark) {
  :root { --bg-color: indigo; --text-color: white; }
}
```

## Query `@supports`

- **`@supports`** applica gli stili solo quando certe coppie proprietà/valore sono supportate; la regola base funge da **fallback** e il layout avanzato (es. griglia) è applicato solo se il browser lo supporta.

```css
.cards { display: block; }
@supports (display: grid) {
  .cards { display: grid; grid-template-columns: 1fr 1fr; }
}
```

## Nesting nativo del CSS

- Nel CSS moderno i selettori correlati possono essere **nidificati** all'interno di altre regole, evitando di ripetere il selettore padre.

```css
.card {
  background-color: lightblue;
  :is(h2, p) { font-size: 1.25em; }
}
```

### Selettore di nesting: `&`

- Il selettore **`&`** in un selettore nidificato si riferisce esplicitamente al selettore della regola padre.

```css
.card {
  background: white;
  &:hover { background: lavender; }
  & > h2 { color: rebeccapurple; }
}
```

> [!warning] Prudenza con il nesting
> Mantenere il nesting poco profondo: un eccesso di nidificazione rende i selettori e il comportamento della cascata più difficili da capire.