# Insiemi Ricorsivi e Ricorsivamente Enumerabili

## Da funzioni a insiemi

Conclusa l'analisi relativa alla calcolabilità delle funzioni possiamo
ora spostarci a quella relativa agli insiemi.\
Chiaramente, avendo considerato esclusivamente funzioni con dominio in
$\mbN^n$, ci occuperemo solo di sottoinsiemi di tale dominio. Per
collegare le due analisi, consideriamo la funzione caratteristica di un
insieme $S\subseteq \mbN^n$:

È facile intuire[^1] che esiste una corrispondenza biunivoca tra
l'insieme delle funzioni caratteristiche e l'insieme delle parti di
$\mbN^n$, ovvero che esista esattamente una funzione per ogni
sottoinsieme $S$ considerato.\
Diremo dunque, con un leggero abuso di nomenclatura, che S *appartiene*
a una certa **classe PRC** $\mcC$ se vi appartiene $f_s$. Diremo dunque
che $S$ è *ricorsivo* $\iff f_s$ è *ricorsivo* ovvero *calcolabile*,
mentre $S$ è *ricorsivo primitivo* $\iff f_s$ è *ricorsivo primitivo*.

### Analisi degli Insiemi Ricorsivi

Iniziamo l'analisi della *ricorsività* degli insiemi semplificandone la
trattazione. Possiamo vedere infatti che, partendo da un sottoinsieme di
$\mbN^n$ con $n$ arbitrario, è sempre possibile ricondurci allo studio
di un sottoinsieme di $\mbN$ analogo.

:::: halfframedbox
red!75!blackRiduzione a sottoinsiemi di $\mbN$ **Enunciato.**
$S \subseteq \mbN^n$ appartiene alla classe PRC $\mcC$ *se e solo se* a
$\mcC$ appartiene anche:
$$S'=\cbrakets{[x_1,\cdots, x_n] \vert (x_1,\cdots, x_n) \in S}\subseteq \mbN$$

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Verifichiamo la doppia implicazione:

-   Sia $f_S \in \mcC$. Allora:
    $$f_{S'}(x) \iff Lt(x)\leq n \land x\neq 0 \land f_S({(x)}_1, \cdots, {(x)}_n)$$
    Dunque $f_{S'} \in \mcC$ poiché composto di predicati ricorsivi
    primitivi o appartenenti a $\mcC$.

-   Sia $f_{S'} \in \mcC$. Allora:
    $$f_S(x_1, \cdots, x_n) \iff f_{S'}([x_1, \cdots, x_n,])$$ Dunque
    $f_S \in \mcC$ poiché composto di predicati ricorsivi primitivi o
    appartenenti a $\mcC$.
::::

Andiamo adesso, analogamente a quanto fatto per le funzioni, ad
analizzare una **proprietà di chiusura** degli **insiemi ricorsivi**.

:::: halfframedbox
red!75!blackChiusura per operazioni insiemistiche su insiemi
ricorsivi[]{#Chiusura per operazioni insiemistiche su insiemi ricorsivi
label="Chiusura per operazioni insiemistiche su insiemi ricorsivi"}
**Enunciato.** Siano $S,T \subseteq \mbN^n$ appartenenti a $\mcC$.
Allora anche $S\cup T$, $S\cap T$ e
$\overline{S}=\mbN^n\smallsetminus S$ appartengono a $\mcC$.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Basta osservare che: $$\begin{split}
      f_{S\cup T}(x_1, \cdots, x_n) &= f_S(x_1, \cdots, x_n) \lor f_T(x_1, \cdots, x_n)\\
      f_{S\cap T}(x_1, \cdots, x_n) &= f_S(x_1, \cdots, x_n) \land f_T(x_1, \cdots, x_n)\\
      f_{\overline{S}}(x_1, \cdots, x_n) &= \lnot f_S(x_1, \cdots, x_n)\\
    \end{split}$$ Abbiamo dunque che questi predicati sono composti di
predicati ricorsivi primitivi o appartenenti a $\mcC$.
::::

È possibile notare come da questa dimostrazione, è possibile ricavare
tale proprietà di chiusura anche per altre operazioni insiemistiche
come: $$\begin{split}
    S \smallsetminus T &= S \cap \overline{T}\\
    S \triangle  T &= (S \smallsetminus T) \cup (T \smallsetminus S)
  \end{split}$$

::: generalbox
Esempi

1.  Qualsiasi $S\subseteq \mbN$ finito è ricorsivo primitivo. Infatti se
    $S=\cbrakets{s_1, \cdots, s_k}$, allora
    $f_S(x) \iff x=s_1 \lor \cdots \lor x=s_k$

2.  L'insieme $\mathbf{P}$ dei numeri primi è ricorsivo primitivo poiché
    $f_{\mathbf{P}}=Primo$.

3.  L'insieme
    $H=\cbrakets{(x_1, x_2) \in \mbN^2 \vert \textit{HALT}(x_1, x_2)}$
    **non è ricorsivo**, dato che $f_H=\textit{HALT}$. Abbiamo inoltre
    che
    $H'=\cbrakets{[x_1,x_2] \in \mbN \vert (x_1, x_2) \in H \iff \textit{HALT}(x_1, x_2)}$
    **non è ricorsivo**, dal teorema precedente.
:::

### Insiemi Ricorsivamente Enumerabili

Abbiamo visto come partendo dai predicati, sottoinsieme delle funzioni
totali, è possibile definire il concetto di insieme ricorsivo.\
Vediamo ora come sia possibile definire un concetto analogo per le
funzioni parziali.

Possiamo dunque dire che un insieme è **ricorsivamente enumerabile** se
esiste per esso una **Procedure di Semi-Decisione**, ovvero una
**procedura** che termina *se e solo se* l'elemento appartiene
all'insieme. Nel nostro caso specifico, se esiste un **S-Programma** che
termina solo per gli input appartenenti a tale insieme.

Un insieme è invece **ricorsivo** *se e solo se* esiste per esso una
**Procedura di Decisione**, cioè un programma che termina **sempre** e
dà output diversi, come $1$ o $0$, a seconda che l'input appartenga
all'insieme o meno. Un esempio di **Procedura di Decisione** per
l'insieme $S$ è il programma che calcola $f_S$.

È fondamentale sottolineare le differenze tra questi due tipi di
**procedure**. Le **Procedura di Decisione** sono per definizione
**funzioni totali**, poiché per ogni input dato devono valutare
l'appartenenza o meno all'insieme. A differenza di quest'ultime le
**Procedure di Semi-Decisione**, essendo **funzioni parziali**, mi
garantiscono esclusivamente l'*appartenenza* di un input a un dato
insieme, ma non la *non appartenenza*, poiché la procedura non
terminerebbe.

Sottolineata questa analogia tra **funzioni totali e parziali** e
**insiemi ricorsivi e ricorsivamente enumerabili** è facile intuire che
gli **insiemi ricorsivi** siano un sottoinsieme di quelli
**ricorsivamente enumerabili**.

:::: halfframedbox
red!75!blackInsiemi ricorsivi contenuti nei ricorsivamente
enumerabili[]{#Ricorsivi Contenuti in Enumerabili
label="Ricorsivi Contenuti in Enumerabili"} **Enunciato.** Se
$S \subseteq \mbN$ è ricorsivo, allora è anche ricorsivamente
enumerabile.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** È sufficiente considerare il programma:

``` {.ini language="ini" caption=""}
[A] IF (*\(\neg f_S(X)\)*) GOTO A
```

Questo programma termina *se e solo se* $X \in S$.
::::

Il legame tra insiemi ricorsivi e ricorsivamente enumerabili è però
molto più stretto di quanto appena visto.

:::: halfframedbox
red!75!blackRelazione tra ricorsività e ricorsivo
enumerabilità[]{#Relazione tra ricorsività e ricorsivo enumerabilità
label="Relazione tra ricorsività e ricorsivo enumerabilità"}
**Enunciato.** $S \subseteq \mbN$ è ricorsivo *se e solo se* $S$ e
$\overline{S}$ sono ricorsivamente enumerabili.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Verifichiamo la doppia implicazione:

-   Ovvia dai
    teoremi [\[Chiusura per operazioni insiemistiche su insiemi ricorsivi\]](#Chiusura per operazioni insiemistiche su insiemi ricorsivi){reference-type="ref"
    reference="Chiusura per operazioni insiemistiche su insiemi ricorsivi"}
    e [\[Ricorsivi Contenuti in Enumerabili\]](#Ricorsivi Contenuti in Enumerabili){reference-type="ref"
    reference="Ricorsivi Contenuti in Enumerabili"}.

-   Siano $g,h$ funzioni parzialmente calcolabili tali che
    $S=\cbrakets{x \in \mbN \vert g(x) \downarrow}$ e
    $\overline{S}=\cbrakets{x \in \mbN \vert h(x) \downarrow}$. Siano
    inoltre $p,q\in\mbN$ tali che $g=\Psi_{\mcP_p}^{(1)}$ e
    $h=\Psi_{\mcP_q}^{(1)}$. Allora $f_s$ è calcolata dal programma:

    ``` {.ini language="ini" caption=""}
    [A] IF (*\(STP(X,p,Z)\)*) GOTO B
              IF (*\(STP(X,q,Z)\)*) GOTO E
              Z <- Z + 1
              GOTO A
          [B] Y <- Y + 1
    ```

È importante notare che non sarebbe stato sufficiente utilizzare $h$ e
$g$ come macro in un programma, poiché essendo funzioni parziali, la
prima delle due incontrata su input che non la soddisfa avrebbe impedito
la terminazione.

È necessario dunque procedere col predicato $STP$ aumentando
gradualmente il numero di *step* concessi. In questo modo il programma
non andrà mai in loop poiché $S \cup \overline{S}=\mbN$, ovvero prima o
poi il programma dovrà terminare.
::::

Caratterizzati a modo questa classe di insiemi, possiamo valutare la
**proprietà di chiusura** per operazioni insiemistiche anche su di loro.

:::: halfframedbox
red!75!blackTeorema **Enunciato.** Siano $S$ e $S'$ insiemi
ricorsivamente enumerabili. Allora lo sono anche $S\cap S'$ e
$S\cup S'$.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.**

-   Siano $g,h$ funzioni unarie parzialmente calcolabili tali che
    $S=\cbrakets{x \in \mbN \vert g(x) \downarrow}$ e
    $S'=\cbrakets{x \in \mbN \vert h(x) \downarrow}$. Consideriamo
    allora il programma:

    ``` {.ini language="ini" caption="" nolol=""}
    Z <- (*\(g(X)\)*)
        Z <- (*\(h(X)\)*)
    ```

    Questo programma termina *se e solo se*
    $g(x)\downarrow\land \; h(x)\downarrow$, ovvero *se e solo se*
    $x\in S\cap S'$.

-   Siano $g,h$ funzioni unarie 1parzialmente calcolabili tali che
    $S=\cbrakets{x \in \mbN \vert g(x) \downarrow}$ e
    $S'=\cbrakets{x \in \mbN \vert h(x) \downarrow}$. Siano inoltre
    $p,q\in\mbN$ tali che $g=\Psi_{\mcP_p}^{(1)}$ e
    $h=\Psi_{\mcP_q}^{(1)}$. Consideriamo allora il programma:

    ``` {.ini language="ini" caption="" nolol=""}
    [A] IF (*\(STP(X,p,Z)\)*) GOTO E
              IF (*\(STP(X,q,Z)\)*) GOTO E
              Z <- Z + 1
              GOTO A
    ```

    Analogamente al
    teorema [\[Relazione tra ricorsività e ricorsivo enumerabilità\]](#Relazione tra ricorsività e ricorsivo enumerabilità){reference-type="ref"
    reference="Relazione tra ricorsività e ricorsivo enumerabilità"} è
    fondamentale l'utilizzo progressivo del predicato $STP$ per valutare
    entrambe le funzioni. Avremo dunque che questo programma termina *se
    e solo se* $g(x)\downarrow \lor \; h(x)\downarrow$, ovvero *se e
    solo se* $x\in S\cup S'$.
::::

Per quanto riguarda l'**operatore di complemento** non è possibile
dimostrare la proprietà di chiusura, e infatti in seguito vedremo un
controesempio[^2].

Possiamo quindi definire un nuovo tipo di insieme:
$$W_n=\cbrakets{x \in \mbN \vert \Phi(x, n) \downarrow}$$

Grazie a questa nuova definizione possiamo osservare che:
$$S \subseteq \mbN \text{ ricorsivamente enumerabile} \iff \exists n \in \mbN : S=W_n$$

Infatti avremo che
$S \text{ ricorsivamente enumerabile} \iff \exists g \text{ parzialmente calcolabile}: S=\cbrakets{x\vert g(x)\downarrow} \iff S=\cbrakets{x\vert \Psi_{\mcP_n}^{(1)}(x)\downarrow}$
per qualche $n \in \mbN$

Con la definizione di $W_n$ abbiamo un nuovo modo per indicare che un
programma termina su un dato input, infatti avremo che:
$$\textit{HALT}(x,y) \iff \Psi_{\mcP_y}^{(1)}(x)\downarrow \iff \Phi(x,y)\downarrow \iff \exists t \in \mbN : STP(x,y,t) \iff x \in W_y$$

Questo insieme ha questo nome poiché, nella matrice vista nel
teorema [\[Esistenza funzioni non calcolabili\]](#Esistenza funzioni non calcolabili){reference-type="ref"
reference="Esistenza funzioni non calcolabili"}, considera esattamente
gli elementi sulla sua diagonale.

Questo insieme è particolarmente rilevante, poiché è esempio di insieme
**ricorsivamente enumerabile** il cui complemento non è **ricorsivamente
enumerabile**.

:::: halfframedbox
red!75!blackTeorema di Enumerazione **Enunciato.** $K$ è ricorsivamente
enumerabile ma non ricorsivo.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Dalla sua definizione sappiamo che, $K$ è
ricorsivamente enumerabile.

Vediamo ora due dimostrazioni per la sua non ricorsività:

1.  Dal
    teorema [\[Relazione tra ricorsività e ricorsivo enumerabilità\]](#Relazione tra ricorsività e ricorsivo enumerabilità){reference-type="ref"
    reference="Relazione tra ricorsività e ricorsivo enumerabilità"}
    sappiamo che $K$ ricorsivamente enumerabile è **ricorsivo** *se e
    solo se* anche $\overline{K}$ è **ricorsivamente
    enumerabile**. **Per assurdo**, supponiamo $\overline{K}$
    ricorsivamente enumerabile.

    Abbiamo allora da quanto visto prima che
    $\exists i \in \mbN: \overline{K}=W_i=\cbrakets{ x \in \mbN \vert \Phi(x,i)\downarrow}$.

    Si ha dunque che
    $\forall x \in \mbN: x \in \overline{K} \iff x \in W_i \iff \Phi(x,i)\downarrow$.

    In particolare per $x = i$ abbiamo che
    $i \in \overline{K} \iff i \in W_i \iff i \in K$. Questo porta
    chiaramente ad **assurdo** poiché un numero non può appartenere sia
    a un insieme che al suo complemento.

    Questa dimostrazione oltre a mostrare che $K$ non è **ricorsivo** ci
    mostra anche che $\overline{K}$ non è **ricorsivamente
    enumerabile**.

2.  K è ricorsivo *se e solo se* $f_k$ è calcolabile. Ma abbiamo che
    $f_k(n) \iff n \in K \iff n \in W_n \iff \textit{HALT}(n,n)$

    E come visto dalla dimostrazione di non calcolabilità di
    $\textit{HALT}$ abbiamo che $\textit{HALT}(x,x)$ non è calcolabile.
::::

Gli insiemi ricorsivamente enumerabili possono essere caratterizzati
anche in un altro modo, ovvero come **codominio** di funzioni piuttosto
che **dominio**.

Prima di vedere ciò però, è necessario dimostrare prima un risultato
intermedio che ci aiuterà nella dimostrazione, ovvero che per ogni
insieme ricorsivamente enumerabile esiste un predicato binario
ricorsivamente enumerabile che lo caratterizza.

:::: halfframedbox
red!75!blackInsiemi ricorsivamente enumerabili e predicati binari
ricorsivi primitivi **Enunciato.** Se $S \subseteq \mbN$ è
ricorsivamente enumerabile allora esiste $R$ predicato binario ricorsivo
primitivo tale che $x \in S \iff \exists t \in \mbN : R(x,t)$, ovvero
$S=\cbrakets{x \in \mbN \vert \exists t \in \mbN : R(x,t)}$.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Sia $n$ tale che $S=W_n$. Allora
$S=\cbrakets{x \in \mbN \vert \Phi(x,n)\downarrow} = \cbrakets{x \in \mbN \vert \exists t \in \mbN: STP_n(x,t)\downarrow}$,
dove $STP_n(x,t)$ è un predicato binario definito come
$STP_n(x,t) \iff STP(x,n,t)$. Questo è chiaramente ricorsivo primitivo
poiché definibile per casi partendo da $STP$. Abbiamo dunque che
l'enunciato del teorema è vero per $R(x,t)=STP_n(x,t)$.
::::

Ottenuto questo risultato possiamo dunque procedere con la dimostrazione
di una prima versione del teorema accennato in precedenza, relativo alle
funzioni **ricorsive primitive**.

:::: halfframedbox
red!75!blackInsiemi ricorsivamente enumerabili e funzioni ricorsive
primitive **Enunciato.** Sia $S \subseteq \mbN$ non vuoto ricorsivamente
enumerabile. Allora esiste $h$ funzione ricorsiva primitiva tale che
$S=\cbrakets{h(x) | x \in \mbN}$.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Sia $R$ predicato binario ricorsivo primitivo tale
che $S=\cbrakets{ x \in \mbN \vert \exists t \in \mbN: R(x,t)}$. Essendo
$S \neq \varnothing$ è possibile fissare un $x_0 \in S$. Definiamo
dunque $h$ come: $$h(x) = \begin{cases}
      l(x), & R(l(x),r(x))\\
      x_0, & \text{altrimenti}
    \end{cases}$$

Essendo definita per casi da funzioni e predicati ricorsivi primitivi
$h$ è chiaramente ricorsiva primitiva. Verifichiamo ora che
$S= H \coloneq\cbrakets{h(x) | x \in \mbN}$. Per vedere che $S=H$
verifichiamo la doppia inclusione:

-   $y \in H \implies y=x_0 \in S \lor \exists x \in \mbN: \left(y=l(x) \land R(l(x),r(x))\right)$.
    Abbiamo dunque in questo secondo caso $R(y,r(x))$. Abbiamo dunque
    che $y\in S$ dal teorema precedente poiché
    $\exists t \in \mbN: R(y,t)$, ovvero $t=r(x)$.

-   Viceversa $x \in S \implies \exists t : R(x,t)$. Allora
    $x=h(\abrakets{ x,t })$ poiché
    $R(l(\abrakets{ x,t }),r(\abrakets{ x,t }))$ e dunque $x \in H$.
::::

Vediamo ora un teorema più generale, che ci permette di caratterizzare
gli insiemi ricorsivamente enumerabili come **codominio** di funzioni
parzialmente calcolabili.

:::: halfframedbox
red!75!blackTeorema **Enunciato.** Sia
$S = \cbrakets{f(n) \vert f(n) \downarrow}$, con $f$ parzialmente
calcolabile. Allora $S$ è ricorsivamente enumerabile.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Sia $p$ il numero di programma che calcola $f$.
Consideriamo dunque il programma:

``` {.ini language="ini" caption="" nolol=""}
[A] IF (*\(\neg STP(Z_1,p,Z_2)\)*) GOTO B
    Z3 <- (*\(f(Z_1)\)*)
    IF X = Z3 GOTO E
[B] Z1 <- Z1 + 1
    IF Z1 <= Z2 GOTO A
    Z1 <- 0
    Z2 <- Z2 + 1
    GOTO A
```

Questo programma termina solo su input $x$ tali che
$\exists n \in \mbN: f(n)=x$. Abbiamo dunque che $S$ è ricorsivamente
enumerabile.

Nel programma viene eseguito un doppio controllo su i potenziali $n$ e
il numero di passi concessi per la computazione. Questo è necessario per
assicurarsi che tutti i numeri vengano controllati, infatti per ogni
valore del contapassi $Z_2$ vengono controllati tutti i valori di $Z_1$
compresi tra $0$ e $Z_2$.

Senza questa accortezza il programma proverebbe a calcolare $f$ sullo
stesso numero all'infinito se questo non facesse terminare $f$.

Inoltre il programma può terminare solo effettuando il salto sulla terza
istruzione, cioè se $X=Z_3$, ovvero se $f(Z_1)=X$.
::::

Sfruttando quest'ultimi risultati possiamo dunque dimostrare un teorema
di carattere generale che caratterizza gli insiemi ricorsivamente
enumerabili a pieno[^3].

:::: halfframedbox
red!75!blackTeorema di caratterizzazione degli insiemi ricorsivamente
enumerabili **Enunciato.** Sia $S \subseteq \mbN$ non vuoto. Allora sono
equivalenti:

1.  $S$ è ricorsivamente enumerabile, cioè $\exists f$ parzialmente
    calcolabile tale che $S=\cbrakets{n \vert f(n) \downarrow}$.

2.  Esiste $f$ ricorsiva primitiva tale che
    $S=\cbrakets{f(n) \vert n \in \mbN}$.

3.  Esiste $f$ calcolabile tale che
    $S=\cbrakets{f(n) \vert n \in \mbN}$.

4.  Esiste $f$ parzialmente calcolabile tale che
    $S=\cbrakets{f(n) \vert f(n) \downarrow}$.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Dimostriamo le varie implicazioni.

Come abbiamo visto nei teoremi precedenti $1 \implies 2$ e
$4 \implies 1$. Inoltre $2 \implies 3 \implies 4$ sono ovvie.
::::

::: generalbox
Esercizio d'esame Dato un insieme $S \subseteq \mbN$, sia
$2S=\cbrakets{2x \vert x \in S}$. Mostrare che se $S$ è ricorsivamente
enumerabile, lo è anche $2S$.

**Soluzione.** Se $S= \varnothing, 2S$ è banalmente ricorsivamente
enumerabile. Altrimenti essendo $S$ ricorsivamente enumerabile, esiste
$f$ ricorsiva primitiva tale che $S=\cbrakets{f(n) \vert n \in \mbN}$.
Allora $2S=\cbrakets{2f(n) \vert n \in \mbN}$ è ricorsivamente
enumerabile poiché $2f$ è ricorsiva primitiva.
:::

[^1]: Questa dimostrazione non rientra nelle finalità di questo corso,
    quindi verrà tralasciata. È però trattata nel dettaglio nel corso di
    Algebra.

[^2]: Esercizi
    consigliati: [\[Riduzione a N per ricorsivamente enumerabili\]](#Riduzione a N per ricorsivamente enumerabili){reference-type="ref"
    reference="Riduzione a N per ricorsivamente enumerabili"}

[^3]: Con questo teorema è conclusa la prima metà del corso, che sarà
    argomento della prova intercorso del 7/11/2023
