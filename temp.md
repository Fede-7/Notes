
Compatta questa introduzione alle variabili continue, lo fa troppo logo le slide.

## Qualche considerazione iniziale

Si rimuove ora l'ipotesi che lo spazio dei campioni $\Omega$ sia discreto.

In particolare, si supponga d'ora in poi che $\Omega \subseteq \mathbb { R }$ sia un sottoinsieme continuo dell'insieme reale; $\Omega$ potrebbe essere quindi esso stesso lo spazio delle misure osservabili oppure potrebbe rappresentare il dominio di una applicazione:
$$
X: \omega \in \Omega \to X (\omega) \in \mathcal {X}
$$
Naturalmente, su $X$ non varrà più la limitazione di essere un insieme finito; spesso accade che $X ( \omega ) = \omega \in \mathcal { X } = \Omega .$

## Esempio

La tensione misurata a vuoto ai capi di un carico resistivo è sempre non nulla per effetto dell'agitazione termica degli elettroni.

1. Si assuma di misurare $n$ volte tale tensione: avremmo ovviamente che $X ( \omega ) = \omega = x \in \mathbb { R }$ e i risultati delle misure saranno $\{ x _ { i } \} _ { i = 1 } ^ { n }$.
2. Si supponga di misurare la potenza trasferita al carico resistivo $R$. In questo caso lo spazio campione sarà ancora $\Omega$, ma la corrispondente variabile aleatoria sarà $X ( \omega ) = \omega ^ { 2 } / R = x \in \mathbb { R }$.

## Qualche considerazione iniziale

Continuando con l’esempio precedente, è chiaro che gli eventi elementari saranno in entrambi i casi $\{ X ( \omega _ { i } ) = x _ { i } \}$ ; 

Si potrebbe quindi essere tentati di definire: 
$$
\mathbb {P} \left(X = x _ {i}\right) = \lim _ {n \rightarrow \infty} \frac {n _ {X = x _ {i}}}{n}
$$
dove, come nel caso discreto, ${ \boldsymbol { n } } _ { X = x _ { i } }$ rappresenta il numero di occorrenze dell’evento al pedice; 

> [!warning] Problematica della misurazione esatta
> Il problema di questa definizione - peraltro corretta - è che, se $X ( \omega _ { i } ) \in X ( \omega _ { j } )$ sono due realizzazioni distinte di una variabile aleatoria reale non saremo mai in grado di misurarle con esattezza: dovremmo infatti disporre di uno strumento a precisione infinita e - anche in questo caso - l’evento $\{ X ( \omega _ { i } ) = X ( \omega _ { j } ) \}$ } sarebbe impossibile; 

Quello che possiamo dire è se la misura $X ( \omega _ { j } )$ cada o meno in un intorno della misura $X ( \omega _ { i } )$ 

Quindi, se $X ( \omega )$ è una **variabile aleatoria continua**, gli eventi elementari $\{ X ( \omega ) = x \}$ hanno - a meno di casi degeneri - probabilità nulla. 

## Esperimenti e variabili continue

Supponiamo di compiere $n$ esperimenti, così da disporre di una collezione $\{ X ( \omega _ { i } ) \}$ di osservazioni di una variabile aleatoria continua $X ( \omega )$ 

Sia $x \in \mathcal { X }$ : ci chiediamo quale sia la frequenza di coccorrenza dell’evento $\{X \text{ cade in un intorno di dimensione } $\Delta x { \mathrm { \sf ~ d i ~ } } x \}$ \}$. In conformità a quanto fatto in precedenza, avremo: 
$$
f _ {n} (x; \Delta x) = \frac {n _ {\{x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \}}}{n}
$$
dove ora $\begin{array} { r } { \begin{array} { r } { n _ { \{ x - $\frac { \Delta x } { 2 }$ \leq X \leq x + $\frac { \Delta x } { 2 }$ \} } } \end{array} } \end{array}$ è il numero di volte (su $n$ esperimenti) in cui osserviamo $\begin{array} { r } { x - $\frac { \Delta x } { 2 }$ \leq X ( \omega ) \leq x + $\frac { \Delta x } { 2 }$ } \end{array}$ 

Possiamo allora definire la probabilità dell’evento $\begin{array} { r } { \left\{ x - $\frac { \Delta x } { 2 }$ \leq X \leq x + $\frac { \Delta x } { 2 }$ \right\} } \end{array}$ nella forma usuale (si riguardi l’avvertenza sulle notazioni della slide 45): 
$$
\mathbb {P} \left(\omega \in \Omega : \left\{x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \right\}\right) = \mathbb {P} \left(X \in \left[ x - \frac {\Delta x}{2}, x + \frac {\Delta x}{2} \right]\right) =
$$
$$
P _ {X} (x; \Delta x) = \lim _ {n \to \infty} f _ {n} (x; \Delta x)
$$