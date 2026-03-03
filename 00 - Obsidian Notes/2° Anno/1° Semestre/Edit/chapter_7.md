# Grammatiche context-free e Linguaggi a Pila

Dopo aver esplorato a fondo il concetto di automa, analiziamo ora un
altro modello di calcolo, le grammatiche context-free.

Il concetto di **grammatica context-free** nasce in ambito linguistico
per descrivere i linguaggi naturali, e solo successivamente venne
formalizzato per essere utilizzato con i linguaggi formali.

Le **grammatiche context-free** forniscono descrizioni del linguaggio
più ad alto livello sulla struttura delle stringhe rispetto a quanto
visto coi linguaggi regolari, che, ricordando l'origine di questo
concetto, è assimilabile ad un analisi logica di un periodo.

## Grammatiche context-free

Innanzitutto per utilizzare le **grammatica context-free** con linguaggi
formali, dobbiamo darne una definzione formale.

Similmente a quanto visto per i DFA con la funzione di transizione e la
funzione di transizione iterata, per definire i linguaggi generati da
una **grammatica context-free** dobbiamo definire la relazione di
derivazione elementare e la relazione di derivazione.

Data la definizione formale di **grammatica context-free**, dobbiamo
definire il concetto di derivazione.

Possiamo finalemente definire i linguaggi generati da una **grammatica
context-free** come
$L(G) = \cbrakets{w \in \Sigma^* \vert S \xRightarrow[G]{*} w}$, ovvero
stringhe di soli **terminali** derivabili dall'**assioma**.

::: generalbox
Esempio: Grammatica context-free

Un primo esempio di **grammatica context-free** è la seguente:

$$\begin{split}
      S &\to \varepsilon\\
      S &\to aSb
    \end{split}$$

Per legibbilità, nella scrittura delle regole di una gramamtica
context-free, si utilizzano alcune convenzioni, come ad esempio scrivere
per prime le regole che sostituiscono l'assioma e raggruppare tutte le
regole che sostituiscono la stessa variabile separando le possibili
sostituzioni col simbolo $\mid$.

Possiamo quindi riscrivere la grammatica precedente come:

$$S \to \varepsilon \mid aSb$$

Per questa grammatica, possiamo dire che
$L(G) = \cbrakets{a^{n}b^n \vert n \geq 0}$. Infatti, ad ogni
derivazione da $S$ avremo o la terminazione della sequenza di
derivazioni o l'aggiunta di un $a$ e di un $b$ alla stringa, che quindi
avrà sempre la forma $a^{n}b^n$.

Si avrà quindi
$S \xRightarrow[G]{} aSb \xRightarrow[G]{} aaSbb \xRightarrow[G]{} \dots \xRightarrow[G]{} a^{n}b^n \xRightarrow[G]{}$
utilizzando la regola $S \to \varepsilon$ come ultima.
:::
