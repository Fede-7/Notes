# Operazioni sui Linguaggi regolari

Per descrivere completamente la classe dei linguaggi regolari, oltre
alla definizione di automa, è necessario introdurre alcune operazioni
che permettono di costruire nuovi linguaggi regolari a partire da altri.

In particolare vedremo come i linguaggi regolari siano chiusi rispetto
alle operazioni di unione, concatenazione e iterazione.

Per dimostrare ciò più agilmente però, ci sarà necessaria una nuova
classe di automi, equivalente ai DFA, ovvero i **DFA non-restarting**.

## DFA Non-Restarting

Una definizione analoga può essere data per gli NFA, sincerandosi che
$q_1 \nin \bigcup\limits_{Q' \in \delta(Q \times A)} Q'$.

Come anticipato, vediamo ora come questa classe di automi sia
equivalente a quella dei DFA

:::: halfframedbox
red!75!blackDFA Non-Restarting **Enunciato.** $L\subseteq A$ regolare
$\implies$ esiste un DFA **non-restarting** $\mcM'$ tale che
$L=L(\mcM')$.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Sia $\mcM=(Q,A,\delta,q_1,F)$ un DFA tale che
$L=L(\mcM)$ e sia $q_0 \nin Q$.

Definiamo $\mcM'=(Q\cup\cbrakets{q_0},A,\delta',q_0,F')$ dove $\delta'$
e $F'$ sono rispettivamente:

$$\delta'(q,a)=\begin{cases}
      \delta(q,a), & q \in Q \land a \in A\\
      \delta(q_1,a), &\text{altrimenti}
    \end{cases}$$

Che è quindi identica a $\delta$ tranne per $q_0$ che emula l'uscita da
$q_1$.

$$F'=\begin{cases}
      F, & q_1 \nin F\\
      F \cup \cbrakets{q_0}, & q_1 \in F
    \end{cases}$$

Evidentemente $\mcM'$ è un DFA **non-restarting** e $L(\mcM')=L(\mcM)$.
::::

## Chiusura dei Linguaggi Regolari

### Unione

Grazie a questa nuova classe di automi possiamo dimostrare le prime
proprietà di chiusura dei linguaggi regolari. Iniziamo vedendo come la
classe dei linguaggi regolari sia chiusa rispetto all'operazione di
**unione**.

:::: halfframedbox
red!75!blackRegolarità dell'Unione[]{#Regolarità dell'unione
label="Regolarità dell'unione"} **Enunciato.** Siano
$L,L' \subseteq A^*$ regolari. Allora $L \cup L'$ è regolare.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Siano $\mcM=(Q,A,\delta,q_1,F)$ e
$\mcM'=(Q',A,\delta',q_1',F')$ DFA **non-restarting** tali che
$L=L(\mcM)$ e $L'=L(\mcM')$ con $Q \cap Q' = \varnothing$.

Definiamo un NFA
$\widehat{\mcM}=(Q\cup Q'\setminus\cbrakets{q_1,q_1'}\cup\cbrakets{q_0},A,\widehat{\delta},q_0,\widehat{F})$
con $$\begin{split}
      \widehat{F}&=\begin{cases}
        F\cup F', & q_1 \nin F \land q_1' \nin F'\\
        F\cup F'\setminus\cbrakets{q_1,q_1'}\cup\cbrakets{q_0}, & q_1 \in F \lor q_1' \in F'\\
      \end{cases} \\
      \forall a \in A: \widehat{\delta}(q,a)&=\begin{cases}
        \cbrakets{\delta(q,a)}, & q \in Q \\
        \cbrakets{\delta'(q,a)}, & q \in Q' \\
        \cbrakets{\delta(q_1,a), \delta'(q_1',a)}, & q=q_0
      \end{cases}
    \end{split}$$

È evidente che il linguaggio accettato da questo NFA è
$L(\widehat{\mcM})=L(\mcM)\cup L(\mcM')=L\cup L'$.
::::

È possibile ora facilmente vedere come i linguaggi regolari siano chiusi
anche rispetto all'intersezione.

:::: halfframedbox
red!75!blackCorollario: Regolarità
dell'Intersezione[]{#Regolarità dell'intersezione
label="Regolarità dell'intersezione"} **Enunciato.** Siano
$L,L' \subseteq A^*$ regolari. Allora $L \cap L'$ è regolare.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Si ha
$L\cap L'=\overline{\rbrakets{\overline{L}\cup\overline{L'}}}$. Dai
teoremi [\[Regolarità del Complemento\]](#Regolarità del Complemento){reference-type="ref"
reference="Regolarità del Complemento"}
e [\[Regolarità dell\'unione\]](#Regolarità dell'unione){reference-type="ref"
reference="Regolarità dell'unione"} abbiamo la tesi.
::::

Vediamo ora un applicazione pratica di questi due teoremi.

Si consideri
$L_1=\cbrakets{w \in \cbrakets{a,b}* \vert w \text{ contiene almeno 2 a}}$
e
$L_1=\cbrakets{w \in \cbrakets{a,b}* \vert w \text{ contiene almeno 2 b}}$.
Si consideri gli automi ottenuti
nell'esercizio [\[Esercizio NFA 2a2b\]](#Esercizio NFA 2a2b){reference-type="ref"
reference="Esercizio NFA 2a2b"}.

Avremo che $\overline{L_1}=L(\mcM_1)$ e $\overline{L_2}=L(\mcM_2)$ dove
$\mcM_1$ e $\mcM_2$ sono rispettivamente:

<figure>

</figure>

Avremo che $\overline{L_1}\cup\overline{L_2}=L(\widehat{\mcM})$ dove
$\widehat{\mcM}$ sarà:

<figure>

</figure>

A questo punto usando la tecnica usata nel
teorema [\[Corrispondenza tra DFA e NFA\]](#Corrispondenza tra DFA e NFA){reference-type="ref"
reference="Corrispondenza tra DFA e NFA"} possiamo ottenere un DFA da
complementare.

Andiamo ora a elencare alcuni risultati derivanti dalla chiusura dei
linguaggi regolari rispetto alle operazioni appena viste.

:::: halfframedbox
red!75!blackProposizione: Regolarità dell'insieme vuoto **Enunciato.**
$\varnothing \subseteq A^*$ è regolare.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Accettato da qualsiasi DFA con $F=\varnothing$.
::::

:::: halfframedbox
red!75!blackProposizione: Regolarità dei singleton **Enunciato.**
$\forall w \in A^*, \cbrakets{w}$ è regolare.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Se $w=w_1\cdots w_n$, con $w_1 \in A$ e $n \in \mbN$,
$L=\cbrakets{w}$ sarà accettato dall'NFA con diagramma:
::::

:::: halfframedbox
red!75!blackCorollario: Regolarità dei linguaggi
finiti[]{#Regolarità dei linguaggi finiti
label="Regolarità dei linguaggi finiti"} **Enunciato.** $L$ finito
$\implies L$ regolare.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Tutti i linguaggi finiti sono unione finita di
singleton. Dalla proposizione appena vista e dalla chiusura per unione
abbiamo la tesi.
::::

### Prodotto per Concatenazione

È importante notare che questo linguaggio conterrà parole di uno dei due
linguaggi originali *se e solo se* l'altro contiene $\varepsilon$.

:::: halfframedbox
red!75!blackChiusura dei Linguaggi regolari per Prodotto **Enunciato.**
Siano $L,L' \subseteq A^*$ regolari. Allora $LL'$ è regolare.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Siano $\mcM=(Q,A,\delta,q_1,F)$ e
$\mcM'=(Q',A,\delta',q_1',F')$ DFA **non-restarting** tali che
$L=L(\mcM)$ e $L'=L(\mcM')$ con $Q \cap Q' = \varnothing$.

Definiamo un NFA
$\widehat{\mcM}=(Q\cup Q', A, \widehat{\delta}, q_1, \widehat{F})$ con

$$\begin{split}
      \widehat{F}&=\begin{cases}
        F\cup F', & q_1' \in F'\\
        F', & q_1' \nin F'\\
      \end{cases} \\
      \forall a \in A: \widehat{\delta}(q,a)&=\begin{cases}
        \cbrakets{\delta(q,a)}, & q \in Q \setminus F\\
        \cbrakets{\delta'(q,a)}, & q \in Q' \\
        \cbrakets{\delta(q,a), \delta'(q_1',a)}, & q\in F
      \end{cases}
    \end{split}$$

È evidente che il linguaggio accettato da questo NFA è
$L(\widehat{\mcM})=L(\mcM)L(\mcM')=LL'$.
::::

::::: generalbox
Esempio: Concatenazione di Linguaggi Regolari

Consideriamo ad esempio il linguaggio $L_1L_1$ con $L_1$ definito come
in precedenza. Consideriamo due automi $\mcM$ e $\mcM'$ che accettano
$L_1$, i quali avranno entrambi la forma:

::: center
:::

Si avrà che il prodotto per concatenazione $L_1L_1$ sarà accettato
dall'automa $\widehat{\mcM}$:

::: center
:::
:::::

In particolare questo prodotto è un esempio di prodotto per
concatenazione di un linguaggio per se stesso. Possiamo in generale
definire dal prodotto l'operazione potenza di un linguaggio come:

$$\begin{cases}
    L^0=\cbrakets{\varepsilon}\\
    L^{n+1}=LL^n
  \end{cases}$$

### Iterazione

Essendo l'operazione Star definita tramite uso di un unione infinita di
linguaggi regolari, non possiamo ricavarla direttamente come
applicazione finita di operazioni di unione e prodotto. Per questo è
necessario definire separatamente questa operazione.

:::: halfframedbox
red!75!blackChiusura dei Linguaggi regolari per
Iterazione[]{#Regolarità dell'iterazione
label="Regolarità dell'iterazione"} **Enunciato.** Sia $L \subseteq A^*$
regolare. Allora $L^*$ è regolare.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Sia $\mcM=(Q,A,\delta,q_1,F)$ un DFA
**non-restarting** tale che $L=L(\mcM)$.

Definiamo un NFA
$\widehat{\mcM}=(Q, A, \widehat{\delta}, q_1, \cbrakets{q_1})$ con:

$$\forall a \in A: \widehat{\delta}(q,a)=\begin{cases}
        \cbrakets{\delta(q,a)}, & \delta(q,a) \nin F\\
        \cbrakets{\delta(q,a), q_1}, \text{ altrimenti}
      \end{cases}$$

Per vedere come $L^*=L(\mcM)$ verifichiamo la doppia inclusione.

-   Verifichiamo per induzione che $L^*\subseteq L(\widehat{\mcM})$.
    Come base induttiva possiamo facilmente notare che
    $\varepsilon \in L(\widehat{\mcM})$. Per quanto riguarda il passo
    induttivo invece supponiamo $L^{n-1}\subseteq L(\widehat{\mcM})$ e
    mostriamo che $L^n \subseteq L(\widehat{\mcM})$.

    Siano $u \in L^{n-1}, v \in L$ tali che $w=uv$. Si ha
    $q_1 \in \widehat{\delta}^*(q_1,u)$ per ipotesi induttiva. Ma allora
    essendo $v \in L$ partendo da $q_1$ si tornerà in $q_1$ per
    costruzione di $\widehat{\mcM}$. Si avrà dunque che
    $q_1 \in \widehat{\delta}^*(q_1,uv) \implies L^n \subseteq L(\widehat{\mcM})$

-   Si ha che $L(\widehat{\mcM}) \subseteq L^*$ poiché, per costruzione
    di $\widehat{\mcM}, w \in L(\mcM)$ è composizione di parole di $L$,
    dovendo per terminare raggiungere $q_1$, ovvero l'unico stato
    terminale di $\mcM$. Essendo che $L$ era **non-restarting** l'unico
    modo per raggiungere $q_1$ in $\widehat{\mcM}$ è raggiungere uno
    stato terminale di $L$.
::::

:::::: generalbox
Esempio: Iterazione di Linguaggi Regolari Consideriamo ad esempio il
linguaggio $L=\cbrakets{ab,ba}$, accettato dall'automa $\mcM$:

::: center
:::

Si avrà che l'iterazione $L^*$ sarà accettata dall'automa
$\widehat{\mcM}$:

::: center
:::

È evidente però che questo automa non sia il più semplice possibile che
accetti $L^*$. Infatti, $\widehat{\mcM}$ può essere semplificato in:

::: center
:::
::::::

:::: halfframedbox
red!75!blackTeorema di Kleene[]{#Teorema di Kleene
label="Teorema di Kleene"}

**Enunciato.** Un linguaggio $L \subseteq A^*$ è regolare *se e solo se*
è finito oppure è ottenuto da linguaggi finiti mediante un numero finito
di operazioni di unione, concatenazione e iterazione.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Dimostriamo la doppia implicazione.

-   Ovvio dai
    teoremi [\[Regolarità dei linguaggi finiti\]](#Regolarità dei linguaggi finiti){reference-type="ref"
    reference="Regolarità dei linguaggi finiti"} [\[Regolarità dell\'unione\]](#Regolarità dell'unione){reference-type="ref"
    reference="Regolarità dell'unione"}, [\[Regolarità dell\'intersezione\]](#Regolarità dell'intersezione){reference-type="ref"
    reference="Regolarità dell'intersezione"}
    e [\[Regolarità dell\'iterazione\]](#Regolarità dell'iterazione){reference-type="ref"
    reference="Regolarità dell'iterazione"}.

-   Sia $\mcM=(Q,A,\delta,q_1,F)$ un DFA con
    $Q=\cbrakets{q_1,\cdots,q_n}$. Definiamo dunque una famiglia di
    linguaggi della forma $R^{(k)}_{i,j}$, dove: $$\begin{split}
            \forall 1 \leq i&, j \leq n \land 0 \leq k \leq n:\\
            &R^{(k)}_{i,j}=\cbrakets{w \in A^* \vert \delta^*(q_i,w)=q_j \land \delta^*(q_i,w') \in \cbrakets{q_1,\cdots,q_k} \forall w'\neq \varepsilon \text{ prefisso proprio di } w }
          \end{split}$$

    Ovvero fissati $i$, $j$ e $k$, il linguaggio $R^{(k)}_{i,j}$
    conterrà le parole che mi permettono di raggiungere lo stato $q_j$
    da $q_i$ passando solo per stati $q \in \cbrakets{q_1,\cdots,q_k}$.

    Nella definizione formale data, la seconda condizione richiede
    sostanzialmente che ogni sotto stringa di $w$ ci porti
    **esclusivamente** in stati da $q_1$ a $q_k$.

    È per questo fondamentale specificare che $w'$ debba essere un
    prefisso **proprio** di $w$, ovvero diverso da $w$ stesso, poiché
    altrimenti ogni insieme con $k<j$ sarebbe vuoto, poiché le parole al
    suo intero dovrebbero raggiungere lo stato $q_j$ dovendo passare
    esse stesse, non solo le loro sotto stringhe, solo per stati da
    $q_1$ a $q_k$, ovvero impossibilitando l'arrivo in $q_j$.

    Analogamente è fondamentale specificare che $w'$ non sia la parola
    vuota, per evitare una contraddizione simile a quella appena vista
    ma nel caso $i>k$. Si avrà in fatti in questo caso che per ogni
    parola, si dovrà avere che:

    $$\cbrakets{q_1, \cdots, q_k} \ni \delta^*(q_i,\varepsilon) = q_i \notin \cbrakets{q_1, \cdots, q_k}$$

    Definiti dunque questi insiemi possiamo osservare che:

    $$\begin{split}
            R^{(0)}_{i,i}&=\cbrakets{\varepsilon} \cup \cbrakets{a \in A^* \vert \delta(q_i, a) = q_i} \text{ è un insieme finito}\\
            \text{Con } i \neq j: R^{(0)}_{i,j}&=\cbrakets{a \in A \vert \delta(q_i, a) = q_j}, \text{ è un insieme finito} \\
            R^{(k+1)}_{i,j}&=R^{(k)}_{i,j} \cup R^{(k)}_{i,k+1}\cdot {(R^{(k)}_{k+1,k+1})}^* \cdot R^{(k)}_{k+1,j}
          \end{split}$$

    In particolare l'ultima osservazione ci dice che tutte le parole che
    ci portano da $q_i$ a $q_j$ attraversando esclusivamente stati da
    $q_1$ a $q_{k+1}$ possono essere di due tipi, ovvero quelle che
    raggiungono $q_j$ passando soltanto per stati da $q_1$ a $q_k$,
    ovvero ignorando lo stato $q_{k+1}$, e quelle che attraversano
    almeno una volta $q_{k+1}$.

    In particolare queste raggiungeranno $q_{k+1}$ una prima volta,
    passando dunque solo per stati da $q_1$ a $q_k$, torneranno in
    $q_{k+1}$ un numero arbitrario di volte, ancora passando solo per
    stati da $q_1$ a $q_k$, e infine lasceranno un'ultima volta
    $q_{k+1}$ per raggiungere $q_j$ passando ancora solo da stati tra
    $q_1$ e $q_k$. Questa divisione si può evincere più chiaramente dal
    diagramma seguente:

    ::: center
    :::

    Con queste tre osservazioni possiamo dimostriamo dunque per
    induzione su $k$ che **ogni linguaggio** $R^{(k)}_{i,j}$ può essere
    ottenuto da linguaggi finiti mediante un numero finito di operazioni
    di unione, concatenazione e iterazione.

    Possiamo ora facilmente vedere però che per ogni automa a stati
    finiti $\mcM$ di $n$ stati, in particolare quello considerato
    all'inizio della dimostrazione, vale che
    $L(\mcM)= \bigcup\limits_{q_j \in F}R^{(n)}_{1,j}$.

    Ovvero il linguaggio accettato dall'automa è l'unione dei linguaggi
    che portano da $1$ a un qualsiasi stato terminale fissato passando
    potenzialmente per tutti e $n$ gli stati, cioè dunque un qualsiasi
    linguaggio regolare è sempre della forma $R^{(k)}_{i,j}$ per qualche
    $i,j,k$ definiti come sopra, la quale è sempre come da tesi.
::::

## Espressioni Regolari

Avendo analizzato le operazioni che permettono di ottenere linguaggi
regolari, possiamo ora definire un modo per descrivere questi linguaggi
in modo più compatto e semplice, ovvero delle stringhe che seguano
specifiche regole sintattiche e che, abbinate a una semantica ben
definita, permettano di descrivere tutti i linguaggi regolari.

### Semantica delle Espressioni Regolari

Oltre ad aver definito la sintassi delle espressioni regolari, per far
si che queste possano essere utilizzate per descrivere linguaggi
regolari è necessario definire una semantica per queste espressioni,
ovvero un modo per interpretare le espressioni regolari come linguaggi
regolari.

Se $\gamma$ è un'espressione regolare su $A$, il linguaggio associato a
$\gamma$: $\abrakets{\gamma} \subseteq A^*$ è definito dalle regole
semantiche:

1.  $\forall a \in A: \abrakets{\underline{a}}=\cbrakets{a}$, inoltre
    $\abrakets{\underline{\varepsilon}}=\cbrakets{\varepsilon}$ e
    $\abrakets{\underline{\varnothing}}=\varnothing$.

2.  Se $\gamma = \underline{(}\alpha\underline{\cup}\beta\underline{)}$,
    allora $\abrakets{\gamma}=\abrakets{\alpha}\cup\abrakets{\beta}$.

3.  Se
    $\gamma = \underline{(}\alpha\underline{\cdot}\beta\underline{)}$,
    allora $\abrakets{\gamma}=\abrakets{\alpha}\cdot\abrakets{\beta}$.

4.  Se $\gamma = \underline{(}\alpha\underline{)}^{\underline{*}}$,
    allora $\abrakets{\gamma}={(\abrakets{\alpha})}^*$.

Il teorema di
Kleene [\[Teorema di Kleene\]](#Teorema di Kleene){reference-type="ref"
reference="Teorema di Kleene"} può essere dunque reinterpretato come:

$$L \subseteq A^* \text{ regolare } \iff \exists \alpha \text{ espressione regolare su } A \text{ tale che } L=\abrakets{\alpha}$$

::: generalbox
Esempio: Espressione Regolare Consideriamo il linguaggio
dell'esercizio [\[Automa L_a\]](#Automa L_a){reference-type="ref"
reference="Automa L_a"} sull'alfabeto $\cbrakets{a,b}$.

Si avrà che l'espressione regolare che lo definisce è:

$$\alpha = \rbrakets{\rbrakets{a \cup b } \cdot \rbrakets{\rbrakets{a \cup b} \cup  \rbrakets{a \cdot \rbrakets{\rbrakets{a \cup b}^* \cdot a}} \cup \rbrakets{b \cdot \rbrakets{\rbrakets{a\cup b}^* \cdot b}}}}$$
:::

Per comodità di scrittura, possiamo definire delle regole di precedenza
tra gli operatori in modo da evitare di dover usare le parentesi e per
sottintendere il simbolo $\cdot$. In particolare, definiamo:

$$* > \cdot > \cup$$

Avremo quindi che l'espressione regolare dell'ultimo esempio può essere
scritta come:

$$\alpha = (a \cup b ) (a \cup b \cup a{(a\cup b)}^*a \cup b{(a\cup b)}^*b)$$

## Pumping Lemma per Linguaggi Regolari

Fino ad ora abbiamo analizzato e descritto esclusivamente linguaggi
regolari e come operare su di essi.

Vogliamo ora analizzare il problema opposto, ovvero come dimostrare che
un linguaggio non è regolare.

Per fare ciò, introduciamo un risultato teorico che dimostra una
condizione necessaria per la regolarità di un linguaggio, che se quindi
negata ci permette di dimostrare che un linguaggio non è regolare.

Questo risultato è il **Pumping Lemma per Linguaggi Regolari**, e
sfrutta un principio combinatorio detto **principio della piccionaia**.

Il **principio della piccionaia** afferma che se $n$ piccioni vengono
messi in $m$ piccionaie, con $n>m$, allora almeno una piccionaia
conterrà almeno due piccioni.

Generalizzando questo concetto, potremmo dire che se ho $n$ oggetti da
distribuire su $m$ insiemi, con $n>m$, non potrò fare a meno di
associare a più oggetti lo stesso insieme.

::::: halfframedbox
red!75!blackPumping lemma per linguaggi regolari (lemma uwu)
**Enunciato.** Sia $\mcM$ un DFA con $n$ stati, e $x\in L(\mcM)$ tale
che $\abs{x} \geq n$. Allora esistono $u,v,w \in A^*$ tali che:

1.  $x=uvw$

2.  $v \neq \varepsilon$

3.  $\forall i \in \mbN: uv^{i}w \in L(\mcM)$, ovvero
    $\cbrakets{u}\cbrakets{v}^*\cbrakets{w} \subseteq L(\mcM)$

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Per il principio della piccionaia, nel percorso di
accettazione di $x$ (da $q_1$ a $q_k \in F$), che passa necessariamente
per almeno $n+1$ stati dovendo includere anche lo stato iniziale, deve
esistere un ciclo, ovvero si passerà per un certo stato $q_l$ almeno due
volte.

Si ha allora $x=uvw$, dove $\delta^*(q_1,u)=q_l$, ovvero $u$ è la parola
che porta da $q_1$ a $q_l$, $\delta^*(q_l,v)=q_l$, ovvero $v$ è la
parola descitta dal ciclo partente da $q_l$, e $\delta^*(q_l,w)=q_k$,
ovvero $w$ è la parola che porta dalla fine del ciclo fino allo stato
terminale $q_k$.

Avremo dunque chiaramente che $v \neq \varepsilon$, dovendo passare per
$q_l$ almeno due volte distinte, ma anche che
$\forall i \in \mbN: \delta^*(q_1,uv^{i}w)=q_k$, potendo percorrere il
ciclo un numero arbitrario di volte, da cui la tesi.

La suddivisione di $x$ in $u,v,w$ come da dimostrazione è più facilmente
intuibile dal seguente diagramma:

::: center
:::
:::::

Visto questo importante risultato, possiamo dunque dimostrare che un
linguaggio non è regolare dimostrando che non rispetta il **Pumping
Lemma**.

Oltre a fare ciò però è possibile derivare dal **Pumping Lemma** altri
risultati teorici minori utili.

:::: halfframedbox
red!75!blackCorollario 1 **Enunciato.** Sia $\mcM$ un DFA con $n$ stati,
allora
$L(\mcM) \neq \varnothing \implies \exists x \in L(\mcM): \abs{x} < n$.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Per assurdo, supponiamo che $x \in L(\mcM)$ sia la
parola di lunghezza minima con $\abs{x} \geq n$.

Per il pumping lemma, esistono $u,v,w \in A^*$ tali che $x=uvw$, con
$v \neq \varepsilon$ e $\forall i \in \mbN: uv^{i}w \in L(\mcM)$. Ma
allora $uv^0w=uw \in L(\mcM)$, contraddicendo la minimalità di $x$.
::::

Questo corollario risulta particolarmente utile per determinare se, dati
due DFA $\mcM_1, \mcM_2$, si ha che $L(\mcM_1) \subseteq L{(\mcM)}_2$.

Si ha infatti che, poiché
$L(\mcM_1) \setminus L(\mcM_2) = L(\mcM_1) \cap \overline{L(\mcM_2)}$ è
regolare, possiamo disegnare un DFA $\mcM$ che accetti
$L(\mcM_1) \setminus L(\mcM_2)$, e verificare se $L(\mcM)=\varnothing$.

Dal corollario appena dimostrato però, per dimostrare che la differenza
sia vuota è sufficiente che
$$\forall x \in A^* \abs{x} < n \implies x \nin L(\mcM)$$

Ovvero che non ci siano parole di lunghezza minore del numero di stati
dell'automa accettate dal linguaggio.

:::: halfframedbox
red!75!blackCorollario 2 **Enunciato.** Sia $\mcM$ un DFA con $n$ stati,
allora $L(\mcM)$ è infinito
$\iff \exists x \in L(\mcM): n \leq \abs{x} < 2n$.

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Dimostriamo la doppia implicazione.

-   Dal **Pumping Lemma**, $x=uvw$ con $v \neq \varepsilon$ e
    $\forall i \in \mbN: uv^{i}w \in L(\mcM)$. Avremo dunque che $L$
    accetta un numero infinito di parole, al variare di $i$ in $\mbN$.

-   Essendo $L(\mcM)$ infinito, la lunghezza delle parole non può essere
    superiormente limitata, altrimenti sarebbe possibile contare il
    numero massimo di parole accettabili.

    Sia $x$ dunque la più corta parola in $L(\mcM)$ tale che
    $\abs{x} \geq 2n$. Possiamo dunque scrivere $x=yz$ con $\abs{y}=n$ e
    $\abs{z}\geq n$. Per il principio della piccionaia, avremo $y=uvw$
    con $v \neq \varepsilon$ e
    $\forall i \in \mbN: \delta^*(q_1,uv^{i}w)=\delta^*(q_1,y)$, ovvero
    al variare di $i$ raggiungerò lo stesso stato raggiunto con $y$, da
    cui $\forall i \in \mbN: uv^{i}wz \in L(\mcM)$.

    Allora anche $uwz \in L(\mcM)$ ma $\abs{uwz} < \abs{yx}=\abs{x}$, da
    cui $\abs{uwz} < 2n$ dalla minimalità di $x$. Ma essendo
    $\abs{z} \geq n$ per costruzione, si ha che $\abs{uwz} \geq n$, da
    cui la tesi.
::::

Vediamo ora finalmente degli esempi di **Linguaggi non Regolari**, e di
come dimostrare ciò utilizzando il **Pumping Lemma**.

::: generalbox
Esempi: Linguaggi non regolari

1.  Il linguaggio $L = \cbrakets{a^{n}b^n \vert n \in \mbN}$, ovvero un
    linguaggio che accetti solo parole con un numero di $a$ consecutive
    seguito da un ugual numero di $b$ consecutive, **non** è regolare.

    Infatti sia per assurdo $\mcM$ un DFA con $p$ stati, tale che
    $L(\mcM)=L$.

    Presa $x=a^{p}b^p$, se $x=uvw$ con $v\neq \varepsilon$ sono
    possibili tre casi:

    1.  $v=a^j, j>0 \implies uw=a^{p-j}b^p \nin L$

    2.  $v=b^j, j>0 \implies uw=a^{p}b^{p-j} \nin L$

    3.  $v=a^{j}b^k, j,k>0 \implies uv^2w = a^{p-j}{(a^{j}b^k)}^2b^{p-k}=a^{p}b^{k}a^{j}b^p \nin L$

    In questo esempio specifico è possibile dimostrare la tesi anche con
    altri valori di $i$, come ad esempio $i=0$ nell'ultimo caso, ma in
    generale questo non è possibile.

    Abbiamo quindi che per qualsisi scelta di $v$ il **Pumping Lemma**
    non è rispettato, dimostrando la tesi.

2.  Il linguaggio $L' = \cbrakets{a^{m}b^n \vert m \geq n > 0}$, non è
    regolare.

    Infatti sia per assurdo $\mcM$ un DFA con $p$ stati, tale che
    $L(\mcM)=L'$.

    Scelgo $x=a^{p}b^{p} \in L, \abs{x}=2p\geq p$. Possiamo dividere i
    casi possibili in maniera analoga all'esempio precedente, con
    l'unica differenza che nel primo caso non potremo scegliere
    un'arbitraria $i$ per la dimostrazione, poichè $\forall i\geq 1$ la
    parola sarebbe ancora accettata dall'automa, dunque siamo costretti
    a scegliere $i=0 \implies uv^{i}w = uw$ per dimostrare la tesi.

3.  Considerando invece il linguaggio
    $L'' = \cbrakets{a^{m}b^n \vert m > n > 0}$, avremo che per la
    dimostrazione non potremo più usare la parola $a^{p}b^{p} \nin L''$.
    Possiamo però considerare la parola
    $x=a^{p}b^{p-1} \in L'', \abs{x}=2p-1\geq p$, che si suddivide nei
    medesimi tre casi degli esempi precedenti e si dimostra con la
    stessa scelta di $i$ del secondo esempio.

4.  **Esercizio d'esame.** Mostrare che
    $L = \cbrakets{a^{n}b^{n} \vert n \geq 0} \cup \abrakets{b^*\cdot a^*}$
    non è regolare.

    **Soluzione.** Per quanto il **Pumping Lemma** sia uno strumento
    utile per dimostrare la non regolarità di un linguaggio, non è
    sempre l'approccio corretto da seguire. In questo caso andremo ad
    utilizzare le proprietà di chiusura dei linguaggi regolari.

    Per assurdo, sia $L$ regolare. Allora dovrebbe esserlo anche
    $L \cap \abrakets{a^*b^*}$, ma
    $L \cap \abrakets{a^*b^*} = \cbrakets{a^{n}b^{n} \vert n \geq 0}$,
    che per quanto visto in precedenza non è regolare, da cui l'assurdo.
:::

Come già intuito dall'ultimo esempio, e come è evincibile dall'enunciato
stesso, il **Pumping Lemma** non fornisce una condizione sufficiente per
la regolarità di un linguaggio, bensì una condizione necessaria.

Possono esistere dunque linguaggi non regolari che rispettano il
**Pumping Lemma**, e per questo motivo non è possibile dimostrare la
regolarità di un linguaggio utilizzando il **Pumping Lemma**.

Utilizzando però l'enunciato di **Pumping Lemma** dato possiamo trovare
dei linguaggi non regolari, per i quali anche la non regolarità non è
dimostrabile utilizzandolo.

Vediamo dunque una versione più forte del **Pumping Lemma**, derivabile
in maniera diretta dalla dimostrazione precedente, per poi vedere un
esempio di linguaggio non regolare per il quale non è possibile
dimostrare la non regolarità utilizzando il **Pumping Lemma**
precedente.

:::: halfframedbox
red!75!blackPumping Lemma per linguaggi regolari rafforzato
**Enunciato.** Sia $\mcM$ un DFA con $n$ stati, e $x\in L(\mcM)$ tale
che $\abs{x} \geq n$. Allora esistono $u,v,w \in A^*$ tali che:

1.  $x=uvw$

2.  $v \neq \varepsilon$

3.  $\forall i \in \mbN: uv^{i}w \in L$

4.  $\abs{uv} \leq n$

::: center
[]{style="color: red!75!black"}
:::

**Dimostrazione.** Per dimostrare questa versione del **Pumping Lemma**
consideriamo la parola $x_n \subseteq x$ formata dalle prime $n$
lettere.

Per il principio della piccionaia sappiamo che già in questa parola deve
essere presente almeno uno stato ripetuto.

Potrò allora scegliere come $u$ la sottoparola di $x$ fino a questo
primo stato ripetuto, con dunque $u \subseteq x_n$, come $v$ la parola
del ciclo contenuto in $x_n$, e come $w$ la parola formata dalle
restanti lettere di $x$.

Avendo scelto $u,v \subseteq x_n$ si ha che $\abs{uv} \leq n$, da cui la
tesi.
::::

::: generalbox
Esempio: Non regolarità del linguaggio dei palindromi

Vediamo dunque un esempio di linguaggio non regolare, che però non può
essere dimostrato con il precedente **Pumping Lemma**.

Sia $L = \cbrakets{w \in \cbrakets{a,b}^* \vert w=\widetilde{w} }$, dove
se $w=w_1w_2\cdots w_n, w_1w_2\cdots w_n \in \cbrakets{a,b}^*$ allora
$\widetilde{w} = w_{n}w_{n-1}\cdots w_1$. Questo linguaggio non è
regolare.

Proviamo inizialmente a dimostrare col **Pumping Lemma** originario che
$L$ non è regolare.

Sia $p$ il numero di stati di un DFA che accetta $L$. Avremo che, per
ogni parola di $L$, si potrà sempre scegliere $v$ come la sotto parola
centrale e ottenere una parola in $L$. Infatti, se $x=uvw=\widetilde{x}$
con $v=\widetilde{v}$, allora $w=\widetilde{u}$ e dunque
$\forall i \in \mbN: uv^{i}w \in L$.

Utilizzando il **Pumping Lemma** rafforzato però, sappiamo che
$\abs{uv} \leq p$, ovvero $v$ dev'essere contenuta nelle prime $p$
lettere di $x$. Ma allora $v$ non può essere la sotto parola centrale di
$x$.

Consideriamo la parola $x=a^{p}ba^{p} = uvw$, con $v \neq \varepsilon$ e
$\abs{uv} \leq p$. Allora avremo necessariamente che:
$$v=a^k, p\geq k>0 \implies uw=a^{p-k}ba^{p} \nin L$$

da cui la tesi.
:::
