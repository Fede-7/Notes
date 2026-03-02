# Calcolabilità e Linguaggio S {#chapter 1}

## Concetto di calcolabilità

Un problema è detto **calcolabile** se è possibile risolverlo
algoritmicamente. Questa misura può essere effettuata in maniera
rigorosa formalizzando il problema in esame usando una funzione
matematica. L'insieme degli input possibili per tale problema ne
costituirà il dominio, mentre quello degli output il codominio. Nel
nostro caso ci limiteremo a prendere in considerazione i problemi, e
dunque le funzioni, che abbiano come input e output numeri naturali.

Importante distinzione che va effettuata dunque è tra **funzioni
totali** e **funzioni parziali**:

-   Una funzione associata a un problema è detta **totale** se ha un
    valore di output definito $\forall a_k \in \mbN^k$, ovvero è
    definibile come: $$\begin{split}
        f: \mbN^k\rightarrow\mbN,\; k\in\mbN\\
        (x_1,x_2,\cdots,x_k)\mapsto y
        \end{split}
        \label{Funzione totale Eq}$$

-   Una funzione associata a un problema è detta **parziale** se ha un
    valore di output definito $\forall a_k \in D\subseteq \mbN^k$,
    ovvero è definibile come: $$\begin{split}
        f: D\subseteq\mbN^k\rightarrow\mbN,\; k\in\mbN\\
        (x_1,x_2,\cdots,x_k)\mapsto y
        \end{split}
        \label{Funzione parziale Eq}$$

Le **funzioni totali** rappresentano dunque un *sottoinsieme*[^1] di
quelle **parziali**. Il ricorso a quest'ultime è fondamentale poiché, al
prezzo della perdita di *generalità* del problema, possiamo alle volte
garantirne la **calcolabilità** altrimenti dimostrabile come falsa.

Per definire dunque il concetto di calcolabilità di una funzione, è
necessario enunciare la **tesi di Church-Turing**[^2].

Questo enunciato è appunto una **tesi** poiché non è dimostrabile,
essendo definito in modo non preciso, ma è comunque accettato come vero
poiché rappresenta l'idea intuitiva che ogni funzione valutabile in una
sequenza finita di passi sia esprimibile tramite un programma. Diremo
dunque che:

-   Una **funzione** $f: D\subseteq\mbN^k\rightarrow\mbN,\; k\in\mbN$ è
    ***parzialmente* calcolabile** se esiste un algoritmo che la
    rappresenta.

-   Una **funzione** è **calcolabile** se essa è **totale *e*
    parzialmente calcolabile**

Definiamo infine come **predicato** una particolare funzione totale il
cui codominio è l'insieme $\cbrakets{0,1}\in\mbN$. Codificando il valore
di $0$ come `FALSO`{.ini} e di $1$ come `VERO`{.ini}, è possibile
valutare la calcolabilità di predicati logici a valori booleani.
$$\begin{split}
    p: \mbN^k\rightarrow\cbrakets{0,1}\subset\mbN,\; k\in\mbN\\
    (x_1,x_2,\cdots,x_k)\mapsto y\in\cbrakets{0,1}
    \end{split}
    \label{Predicato Eq}$$

## Linguaggio S

Il **linguaggio S** è un linguaggio formale per la scrittura di
algoritmi utilizzabile per la verifica della **calcolabilità** di un
problema.

Questo linguaggio infatti è *minimale* nelle istruzioni, possedendo solo
quelle eseguibili da qualsiasi compilatore e con le quali è possibile,
per quanto in molte più linee, ricostruire un qualsiasi algoritmo.

### Sintassi

##### Variabili. {#variabili. .unnumbered}

Nel **linguaggio S** le variabili si dividono in tre gruppi:

1.  Variabili d'*Input* `(X1,X2,...)`{.ini}, di numero potenzialmente
    infinito[^3] inizializzate con i valori dell'input di una data
    istanza;

2.  Variabile di *Output* `(Y)`{.ini}, unica e inizializzata al valore
    `0`{.ini};

3.  Variabili *Temporanee* `(Z1,Z2,...)`{.ini}, di numero potenzialmente
    infinito inizializzate col valore `0`{.ini}.

##### Etichette. {#etichette. .unnumbered}

Il **linguaggio S** permette di utilizzare delle etichette alfabetiche,
*label*, per demarcare specifiche linee su cui poter effettuare dei
salti, *jump*.

Vengono utilizzate le lettere dell'alfabeto dalla `A`{.ini} alla
`D`{.ini} numerate, con il caso speciale dell'etichetta `E`{.ini}, usata
per la terminazione del programma, che spiegheremo meglio in seguito.

##### Statement. {#statement. .unnumbered}

Il **linguaggio S** contempla solo $4$ tipi di **statement**, o
*asserzioni*, che possono essere combinate o meno a **etichette** per
formare **istruzioni**. Nello specifico questi statement sono:

-   **Pigra**: `V<-V`{.ini}, asserzione nulla;

-   **Incremento**: `V<-V+1`{.ini}, incrementa una variabile qualsiasi
    `V`{.ini} di `1`{.ini};

-   **Decremento**: `V<-V-1`{.ini}, decrementa una variabile qualsiasi
    `V`{.ini} di `1`{.ini}, se essa contiene il valore `0`{.ini}
    l'istruzione viene ignorata;

-   **Salto**: `IF V!=0 GOTO L`{.ini}, passa alla prima linea
    etichettata dall'etichetta generica `L`{.ini} se la variabile
    generica `V`{.ini} è diversa da `0`{.ini}, altrimenti l'istruzione
    viene ignorata. Nel caso l'etichetta `L` non esista, il programma
    termina.\
    Solitamente questo meccanismo è effettuato con l'etichetta
    `E`{.ini}, che viene riservata allo scopo di terminazione.

::: generalbox
Esempio: S-Programma Un primo esempio di **S-Programma** può dunque
essere il seguente:

``` {#Primo Esempio S-Programma .ini language="ini" label="Primo Esempio S-Programma" caption="Esempio di S-Programma"}
[A] X <- X - 1
        Y <- Y + 1
        IF X!=0 GOTO A
```

Nello specifico, questo **S-Programma** rappresenta la funzione:
$$f(x)=\begin{cases}
        1, & x=0\\
        x, & x\neq0
      \end{cases}
      \label{Funzione quasi Identica Eq}$$

Poiché il programma ripete l'operazione d'incremento della variabile
`Y`{.ini} un numero `X`{.ini} di volte, per $x\neq0$, mentre una volta
sola per $x=0$. Il programma termina infine, dopo l'esecuzione
dell'ultima linea.
:::

### Esempi di S-Programmi e Macro

Consideriamo invece adesso un **S-Programma** che implementi proprio la
*funzione identica*[^4] $f(x) = x$:

``` {#Funzione Identica .ini language="ini" label="Funzione Identica" caption="Funzione identica"}
[A] IF X!=0 GOTO B
    Z <- Z + 1
    IF Z != 0 GOTO E
[B] X <- X - 1
    Y <- Y + 1
    Z <- Z + 1
    IF Z != 0 GOTO A
```

Possiamo notare come le righe `6--7`{.ini} effettuano un *salto
incondizionato*. È possibile isolarle sfruttando il concetto di
**macro**.

Nello specifico definiamo la **macro di salto incondizionato**
`GOTO L`{.ini} come[^5]:

``` {#Salto Incondizionato .ini language="ini" label="Salto Incondizionato" caption="Macro di salto incondizionato"}
[L]...
   ...
    V <- V + 1
    IF V != 0 GOTO L
```

::: generalbox
Esempi

-   Definiamo innanzitutto la **macro di azzeramento** `V<-0`{.ini}:

    -   ``` {#Aggiornamento .ini language="ini" label="Aggiornamento" caption="Macro di azzeramento"}
        [A] V <- V - 1
              IF V != 0 GOTO A
        ```

    -   Questa **macro** corrisponde alla **funzione costante**
        $f(x)=0$, ed è di fondamentale importanza per il corretto
        funzionamento di altre macro.

    -   Ogni **macro** che d'ora in avanti andremo a definire, conterrà
        implicitamente la **macro di azzeramento** per garantire lo
        stato iniziale delle variabili.

-   Definiamo infine un'altra importante **macro**, ovvero la **macro di
    assegnazione** `V<-V1`{.ini}:

    -   ``` {#Assegnazione .ini language="ini" label="Assegnazione" caption="Macro di assegnazione"}
        [C] IF V1 != 0 GOTO A
              GOTO E
          [A] V <- V + 1
              V1 <- V1 - 1
              GOTO C
        ```
:::

#### Predicati

La codifica di **predicati** invece può essere utilizzata per la
definizione di **macro** di *salto* con condizione diversa da
`!=0`{.ini}.

Potendo infatti conservare in una variabile generica `V`{.ini} l'output
di una qualsiasi **funzione k-aria (parzialmente) calcolabile** grazie
alla macro di assegnazione, è possibile definire la **macro** di **salto
generalizzato**:

``` {#Salto generalizzato .ini language="ini" label="Salto generalizzato" caption="Macro di salto generalizzato"}
V <- P(x1,x2, ... , xk)
IF V != 0 GOTO L
```

Nel caso infatti che il predicato $p$ sia `VERO`{.ini}, avremo che la
variabile `V`{.ini} sarà pari a `1`{.ini}, la condizione dello statement
di salto sarà verificata, e avverrà il salto. In caso contrario, si avrà
che la variabile `V`{.ini} sarà pari a `0`{.ini}, la condizione dello
statement di salto non sarà verificata, e il programma procederà
all'istruzione successiva.

::: generalbox
Esempo: Funzione totale predicato

Prendiamo ad esempio il predicato d'uguaglianza fra due numeri
$p(x_1,x_2)\iff x_1=x_2$. Possiamo esprimere questo **predicato** usando
la **funzione totale**:

$$f(x_1,x_2)= \begin{cases}
                1, \;\; x_1=x_2\\
                0, \;\; x_1\neq x_2
              \end{cases}
  \label{Predicato Uguaglianza Eq}$$

Un **programma** che implementa questo predicato è:

``` {#Predicato Uguaglianza .ini language="ini" label="Predicato Uguaglianza" caption="Predicato logico (uguaglianza)"}
Z1 <- X1
    Z2 <- X2
[A] IF Z1 != 0 GOTO B
    IF Z2 != 0 GOTO E
    Y <- Y + 1
    GOTO E
[B] Z1 <- Z1 - 1
    IF Z2 != 0 GOTO C
    GOTO E
[C] Z2 <- Z2 - 1
    GOTO A
```
:::

#### Funzioni parzialmente calcolabili

Possiamo anche scrivere programmi per le **funzioni parzialmente
calcolabili**, come per esempio:

``` {#Funzione Sottrazione .ini language="ini" label="Funzione Sottrazione" caption="Funzione parzialmente calcolabile (sottrazione)"}
Y <- X1
    Z <- X2
[C] IF Z != 0 GOTO A
    GOTO E
[A] IF Y != 0 GOTO B
    GOTO A
[B] Y <- Y - 1
    Z <- Z - 1
    GOTO C
```

Nello specifico, questo **S-programma** rappresenta:
$$f(x_1, x_2)=\begin{cases}
    x_1-x_2, \;\; \text{se}\; x_1\geqslant x_2\\
    \uparrow, \;\;\text{altrimenti}
  \end{cases}
  \label{Funzione Sottrazione Eq}$$

Dove il simbolo $\uparrow$ indica *l'inesistenza di output*, normalmente
chiamata **divergenza** della funzione.\
Questa funzione è quindi parzialmente calcolabile dato che può eseguire
la sottrazione *se e solo se* il primo numero è maggiore o uguale del
secondo[^6].

In **linguaggio S** l'inesistenza di output è codificata con
l'impossibilità di terminazione del programma. Nel caso specifico
possiamo infatti notare che, se verificato il caso $x_1 < x_2$,
l'esecuzione rimane bloccata tra le righe `5--6`{.ini} non giungendo mai
alla fine del programma.

## Caratterizzazione di un S-programma

Una volta afferrate così le basi del **linguaggio S** e visti alcuni
esempi notevoli, andiamo a formalizzare il concetto di **S-Programma**.
Chiamiamo **S-Programma** una qualsiasi *lista finita*[^7]
d'**istruzioni**.

Una volta definito formalmente il concetto di **S-Programma** possiamo,
usando le proprietà che derivano da questa definizione, andarlo a
caratterizzare fino a cogliere il parallelismo suddetto tra
**S-Programmi** e **funzioni calcolabili**.

Innanzitutto, per descrivere un **S-Programma** è importante tenere
traccia dell'aggiornamento delle sue variabili. Per fare ciò ci
avvaliamo del concetto di **Stato di un Programma**.

Lo **stato** però non è sufficiente a descrivere un **programma**, in
quanto non tiene traccia dell'ordine di esecuzione delle istruzioni. Per
avere una descrizione puntuale di un **programma** di *'l'
istruzioni*[^8], è però necessario contestualizzare il suo **stato** in
un determinato momento dell'esecuzione. Per fare questo ci avvaliamo del
concetto d'**istantanea**, o *snapshot*.

Dove con $l+1$ codifichiamo la terminazione del programma, essendo
un'istruzione con tale indice non esistente. Chiamiamo l'**istantanea**
con questo indice **terminale**.

Le **istantanee** permettono in oltre di descrivere consequenzialmente
le **istantanee successive** di un **programma** se abbinate alla
istruzione indicizzata da $i$, a patto che essa non sia un'**istantanea
terminale**.

In particolare, partendo da una qualsiasi **istantanea** $(i,\sigma)$
esistono $4$ diverse configurazioni di possibili **istantanee
successive** $(j,\tau)$ in base all'istruzione in questione.

1.  $j=i+1$ e $\tau = \sigma$, se l'i-esima istruzione è:

    -   [pigra]{.underline} (`V<-V`{.ini});

    -   [decremento]{.underline} (`V<-V-1`{.ini}) con $V=0$;

    -   [salto]{.underline} (`IF V!=0 GOTO L`{.ini}) con $V=0$.

2.  $j=i+1$ e $\tau$ ottenuta da $\sigma$ sostituendo l'equazione $V=n$
    con $V=n+1$, se l'i-esima istruzione è:

    -   [incremento]{.underline} (`V<-V+1`{.ini});

3.  $j=i+1$ e $\tau$ ottenuta da $\sigma$ sostituendo l'equazione $V=n$
    con $V=n-1$, se l'i-esima istruzione è:

    -   [decremento]{.underline} (`V<-V-1`{.ini}) e $V>0$;

4.  1.  $j=l+1$ e $\tau = \sigma$, se l'i-esima istruzione è:

        -   [salto]{.underline} (`IF V!=0 GOTO L`{.ini}), con $\mcP$ non
            contenente istruzioni etichettate con `L`{.ini} e $V>0$;

    2.  $j=k$ e $\tau = \sigma$, se l'i-esima istruzione è:

        -   [salto]{.underline} (`IF V!=0 GOTO L`{.ini}), con $k$ indice
            della prima istruzione di $\mcP$ etichettata con `L`{.ini} e
            $V>0$;

In ultimo chiamiamo **istantanea iniziale** una qualunque coppia
$(i,\sigma)$ con $i=1$ e $\sigma$ contenente equazione $V=0$ per ogni
$V$ locale o di output.

Avvalendoci di queste definizioni e caratterizzazioni, possiamo in
definitiva definire[^9] formalmente cosa si intende per **calcolo
terminante di $\mcP$**.

Date queste definizioni formali, è possibile trarre dei parallelismi tra
la vista del programma come funzione e la vista del programma come
sequenza d'istruzioni.

Infatti, dato $(r_1,\cdots,r_k)\in\mbN$ come n-upla d'input di una
funzione $f$, lo **Stato Iniziale** dell'**S-Programma** $\mcP$
corrispondente sarà
$\sigma_1 = \cbrakets{x_1=r_1,\cdots,x_k=r_k,y=0,z_1=0,\cdots,z_n=0}$,
con $n$ numero di variabili temporanee, mentre l'**istantanea iniziale**
sarà rappresentata dalla coppia $(1,\sigma_1)$.

::: generalbox
Esempo: Calcolo Terminante di $\mcP$

-   Prendiamo come esempio il
    programma [\[Primo Esempio S-Programma\]](#Primo Esempio S-Programma){reference-type="ref"
    reference="Primo Esempio S-Programma"} e andiamo ad analizzare
    l'andamento del programma per input pari a **$2$**:

-   1.  **Stato Iniziale**: $\sigma_1 = \cbrakets{X=2,Y=0}$

    2.  **Istantanea 1**: $(1,\sigma_1)$;

    3.  **Istantanea 2**: $(2,\sigma_2)$ con
        $\sigma_2 = \cbrakets{X=1,Y=0}$;

    4.  **Istantanea 3**: $(3,\sigma_3)$ con
        $\sigma_3 = \cbrakets{X=1,Y=1}$;

    5.  **Istantanea 4**: $(1,\sigma_3)$;

    6.  **Istantanea 5**: $(2,\sigma_4)$ con
        $\sigma_4 = \cbrakets{X=0,Y=1}$;

    7.  **Istantanea 6**: $(3,\sigma_5)$ con
        $\sigma_5 = \cbrakets{X=0,Y=2}$;

    8.  **Istantanea 7**: $(4,\sigma_5)$ **terminale**;

    9.  **Stato Finale**: $\sigma_4 = \cbrakets{X=0,Y=2}$;

-   È possibile notare che se venissero forniti più input di quelli
    necessari, la successione d'istantanee rimarrebbe invariata,
    ignorando gli input in eccesso.

-   Se ad esempio prendiamo come input la n-upla $(2,3,4)$, lo **stato
    iniziale** sarà $\sigma_1 \cup \cbrakets{X_1=3,X_2=4}$, ma si
    comporterà come se fosse stato fornito solo $2$ come input.

-   Inoltre è possibile generalizzare il calcolo ulteriormente,
    contemplando anche la possibilità d'input sottodimensionati rispetto
    al numero di variabili richieste.

-   Considerando infatti le variabili d'input senza inizializzazione
    esplicita come poste a `0`{.ini}, l'avanzamento delle istantanee
    procederà normalmente fino alla terminazione in maniera analoga a
    quelle appena viste.
:::

Formalizziamo dunque la **funzione k-aria** calcolata da $\mcP$ come:

$$\Psi_{\mcP}^{(k)}(x_1,x_2,\cdots,x_k)=\begin{cases}
    y \text{ nello stato terminale}, \;\; \text{se esiste un calcolo terminante di } \mcP \text{ con input } x_1,x_2,\cdots,x_k\\
    \uparrow, \text{ altrimenti}
  \end{cases}
  \label{Funzione k-aria di P Eq}$$

Possiamo finalmente dare una definizione formale del concetto di
**funzione parzialmente calcolabile** accennato all'inizio di questo
capitolo:

È necessario, logicamente, che la funzione $f$ sia definita per *tutte e
sole* le n-uple per cui $\Psi_{\mcP}^{(k)}$ termina.

Formalizziamo dunque anche il processo di *sostituzione di macro* vista
in precedenza. Sia $f$ funzione n-aria calcolata da
$\mcP=\mcP(y,x_1,x_2,\cdots,x_n,z_1,z_2,\cdots,z_k,E,A_1,\cdots,A_l)$.
Allora la macro $V'\leftarrow f(V_1,V_2,\cdots,V_n)$ all'interno di un
altro programma $\mcP_2$ va sostituita con:

``` {#Macro Formalizzata .ini language="ini" label="Macro Formalizzata" caption="Macro"}
Zm <- 0
     Zm+1 <- V1
     (*\(\vdots\)*)
     Zm+n <- Vn
     Zm+n+1 <- 0
     Zm+n+2 <- 0
     (*\(\vdots\)*)
     Zm+n+k <- 0
     (*\(\mcQ=\mcP(Z_m,Z_{m+1},Z_{m+2},...,Z_{m+n+k},E_m,A_{m+1},A_{m+l})\)*)
[Em] V'<- Zm
```

Dove per la linea `9`{.ini} si intende aver sostituito in $\mcP_2$ le
istruzioni del programma $\mcP$, e $m$ è sufficientemente grande da non
creare conflitti con le variabili di $\mcP_2$. È importante inoltre
notare la presenza della **label** `[Em]`{.ini} che permette la corretta
assegnazione del valore di output nella variabile `V'`{.ini} anche in
caso la macro termini per *salto* a etichetta `[E]`{.ini}[^10].

[^1]: Essendo il dominio di una funzione parziale $D\subseteq\mbN^k$, ne
    fanno parte anche i casi particolari di $D=\mbN^k$, ovvero le
    funzioni totali.

[^2]: La versione enunciata è quella relativa al **Modello S**, che
    utilizzeremo per la valutazione della calcolabilità di una funzione.
    Ogni modello di calcolo però è dimostrabile come equivalente.

[^3]: Il numero è potenzialmente infinito per non inserire limitazione
    di numero, ma chiaramente ogni programma ne utilizzerà un numero
    finito.

[^4]: Implementazione alternativa [\[Funzione Identica AltVer\]](#Funzione Identica AltVer){reference-type="ref"
    reference="Funzione Identica AltVer"}.

[^5]: Approfondimento [\[Funzione Somma\]](#Funzione Somma){reference-type="ref"
    reference="Funzione Somma"}.
    Esercizi [\[Funzione Prodotto\]](#Funzione Prodotto){reference-type="ref"
    reference="Funzione Prodotto"} [\[Funzione Prodotto con Costante\]](#Funzione Prodotto con Costante){reference-type="ref"
    reference="Funzione Prodotto con Costante"}

[^6]: Esercizio [\[Predicato Pari Dispari\]](#Predicato Pari Dispari){reference-type="ref"
    reference="Predicato Pari Dispari"}

[^7]: Importante sottolineare che anche la *lista vuota* è contemplata,
    rappresentata infatti dal *programma vuoto*.

[^8]: Dove *l* è detta di norma *lunghezza del programma*.

[^9]: A chiunque turbi l'accoppiata delle parole "definitiva" e
    "definire" si ricorda la figura retorica di suono della
    [consonanza](https://en.wikipedia.org/wiki/Literary_consonance),
    ampiamente utilizzata e apprezzata nella poesia da secoli.

[^10]: Esercizi da [\[Programma P\]](#Programma P){reference-type="ref"
    reference="Programma P"}
    a [\[Predicato Minore Uguale\]](#Predicato Minore Uguale){reference-type="ref"
    reference="Predicato Minore Uguale"}
