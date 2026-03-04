# Operazioni sui Linguaggi regolari


Per descrivere completamente la classe dei linguaggi regolari, oltre alla definizione di automa, è necessario introdurre alcune operazioni che permettono di costruire nuovi linguaggi regolari a partire da altri.

In particolare vedremo come i linguaggi regolari siano chiusi rispetto alle operazioni di unione, concatenazione e iterazione.

Per dimostrare ciò più agilmente però, ci sarà necessaria una nuova classe di automi, equivalente ai DFA, ovvero i **DFA non-restarting**.

## DFA Non-Restarting


> [!definition] DFA Non-restarting
> Un DFA $\mathcal{M}$ è **Non-Restarting** se $\mathcal{M}=(Q,A,\delta,q_1,F)$ con $q_1 \notin \delta(QxA)$, ovvero non è possibile tornare allo stato iniziale dopo aver letto un simbolo di input.


Una definizione analoga può essere data per gli NFA, sincerandosi che $q_1 \notin \bigcup\limits_{Q' \in \delta(Q \times A)} Q'$.

Come anticipato, vediamo ora come questa classe di automi sia equivalente a quella dei DFA

> [!theorem] DFA Non-Restarting
> **Enunciato. ** $L\subseteq A$ regolare $\implies$
> esiste un DFA **non-restarting** $\mathcal{M}'$ tale che $L=L(\mathcal{M}')$.
>
>
> **Dimostrazione. ** Sia $\mathcal{M}=(Q,A,\delta,q_1,F)$ un DFA tale che $L=L(\mathcal{M})$ e sia $q_0 \notin Q$.
>
> Definiamo $\mathcal{M}'=(Q\cup\{q_0\},A,\delta',q_0,F')$ dove $\delta'$ e $F'$ sono rispettivamente:
>
> $$
>     \delta'(q,a)=\begin{cases}
>     \delta(q,a), & q \in Q \land a \in A\\
>     \delta(q_1,a), &\text{altrimenti}
>     \end{cases}
> $$

>
> Che è quindi identica a $\delta$ tranne per $q_0$ che emula l'uscita da $q_1$.
>
> $$
>     F'=\begin{cases}
>     F, & q_1 \notin F\\
>     F \cup \{q_0\}, & q_1 \in F
>     \end{cases}
> $$

>
> Evidentemente $\mathcal{M}'$ è un DFA **non-restarting** e $L(\mathcal{M}')=L(\mathcal{M})$.


## Chiusura dei Linguaggi Regolari


### Unione


Grazie a questa nuova classe di automi possiamo dimostrare le prime proprietà di chiusura dei linguaggi regolari. Iniziamo vedendo come la classe dei linguaggi regolari sia chiusa rispetto all'operazione di **unione**.

> [!theorem] Regolarità dell'Unione
> **Enunciato. ** Siano $L,L' \subseteq A^*$ regolari. Allora $L \cup L'$ è regolare.
>
>
> **Dimostrazione. ** Siano $\mathcal{M}=(Q,A,\delta,q_1,F)$ e $\mathcal{M}'=(Q',A,\delta',q_1',F')$ DFA **non-restarting** tali che $L=L(\mathcal{M})$ e $L'=L(\mathcal{M}')$ con $Q \cap Q' = \varnothing$.
>
> Definiamo un NFA $\widehat{\mathcal{M}}=(Q\cup Q'\setminus\{q_1,q_1'\}\cup\{q_0\},A,\widehat{\delta},q_0,\widehat{F})$ con
> $$
>     \widehat{F}&=\begin{cases}
>     F\cup F', & q_1 \notin F \land q_1' \notin F'\\
>     F\cup F'\setminus\{q_1,q_1'\}\cup\{q_0\}, & q_1 \in F \lor q_1' \in F'\\
>     \end{cases} \\
>     \forall a \in A: \widehat{\delta}(q,a)&=\begin{cases}
>     \{\delta(q,a)\}, & q \in Q \\
>     \{\delta'(q,a)\}, & q \in Q' \\
>     \{\delta(q_1,a), \delta'(q_1',a)\}, & q=q_0
>     \end{cases}
> $$

>
> È evidente che il linguaggio accettato da questo NFA è $L(\widehat{\mathcal{M}})=L(\mathcal{M})\cup L(\mathcal{M}')=L\cup L'$.


È possibile ora facilmente vedere come i linguaggi regolari siano chiusi anche rispetto all'intersezione.

> [!theorem] Corollario: Regolarità dell'Intersezione
> **Enunciato. ** Siano $L,L' \subseteq A^*$ regolari. Allora $L \cap L'$ è regolare.
>
>
> **Dimostrazione. ** Si ha $L\cap L'=\overline{[\overline{L}\cup\overline{L'}]}$. Dai teoremi*(ref: Regolarità del Complemento)* e*(ref: Regolarità dell'unione)* abbiamo la tesi.
>


Vediamo ora un applicazione pratica di questi due teoremi.

Si consideri $L_1=\{w \in \{a,b\}* \vert w \text{ contiene almeno 2 a}\}$ e $L_1=\{w \in \{a,b\}* \vert w \text{ contiene almeno 2 b}\}$. Si consideri gli automi ottenuti nell'esercizio*(ref: Esercizio NFA 2a2b)*.

Avremo che $\overline{L_1}=L(\mathcal{M}_1)$ e $\overline{L_2}=L(\mathcal{M}_2)$ dove $\mathcal{M}_1$ e $\mathcal{M}_2$ sono rispettivamente:

}
\subfloat[Diagramma di $\mathcal{M}_2$]{
}
\end{figure}

Avremo che $\overline{L_1}\cup\overline{L_2}=L(\widehat{\mathcal{M}})$ dove $\widehat{\mathcal{M}}$ sarà:

}
\subfloat[Diagramma di $\widehat{\mathcal{M}}$ semplificato]{
}
\end{figure}

A questo punto usando la tecnica usata nel teorema*(ref: Corrispondenza tra DFA e NFA)* possiamo ottenere un DFA da complementare.

---


Andiamo ora a elencare alcuni risultati derivanti dalla chiusura dei linguaggi regolari rispetto alle operazioni appena viste.

> [!theorem] Proposizione: Regolarità dell'insieme vuoto
> **Enunciato. ** $\varnothing \subseteq A^*$ è regolare.
>
>
> **Dimostrazione. ** Accettato da qualsiasi DFA con $F=\varnothing$.


> [!theorem] Proposizione: Regolarità dei singleton
> **Enunciato. ** $\forall w \in A^*, \{w\}$ è regolare.
>
>
> **Dimostrazione. ** Se $w=w_1\cdots w_n$, con $w_1 \in A$ e $n \in \mathbb{N}$, $L=\{w\}$ sarà accettato dall'NFA con diagramma:
>
>


> [!theorem] Corollario: Regolarità dei linguaggi finiti
> **Enunciato. ** $L$ finito $\implies L$ regolare.
>
>
> **Dimostrazione. ** Tutti i linguaggi finiti sono unione finita di singleton. Dalla proposizione appena vista e dalla chiusura per unione abbiamo la tesi.


### Prodotto per Concatenazione


> [!definition] Prodotto per Concatenazione
> Se $L,L'\subseteq A^*$, definiamo:
> $$
>     LL'=\{ww' \in A^* \vert w \in L \land w' \in L'\}
> $$


È importante notare che questo linguaggio conterrà parole di uno dei due linguaggi originali *se e solo se* l'altro contiene $\varepsilon$.

> [!theorem] Chiusura dei Linguaggi regolari per Prodotto
> **Enunciato. ** Siano $L,L' \subseteq A^*$ regolari. Allora $LL'$ è regolare.
>
>
> **Dimostrazione. ** Siano $\mathcal{M}=(Q,A,\delta,q_1,F)$ e $\mathcal{M}'=(Q',A,\delta',q_1',F')$ DFA **non-restarting** tali che $L=L(\mathcal{M})$ e $L'=L(\mathcal{M}')$ con $Q \cap Q' = \varnothing$.
>
> Definiamo un NFA $\widehat{\mathcal{M}}=(Q\cup Q', A, \widehat{\delta}, q_1, \widehat{F})$ con
>
> $$
>     \widehat{F}&=\begin{cases}
>     F\cup F', & q_1' \in F'\\
>     F', & q_1' \notin F'\\
>     \end{cases} \\
>     \forall a \in A: \widehat{\delta}(q,a)&=\begin{cases}
>     \{\delta(q,a)\}, & q \in Q \setminus F\\
>     \{\delta'(q,a)\}, & q \in Q' \\
>     \{\delta(q,a), \delta'(q_1',a)\}, & q\in F
>     \end{cases}
> $$

>
> È evidente che il linguaggio accettato da questo NFA è $L(\widehat{\mathcal{M}})=L(\mathcal{M})L(\mathcal{M}')=LL'$.
>


---


> [!example] Esempio: Concatenazione di Linguaggi Regolari
>
> Consideriamo ad esempio il linguaggio $L_1L_1$ con $L_1$ definito come in precedenza. Consideriamo due automi $\mathcal{M}$ e $\mathcal{M}'$ che accettano $L_1$, i quali avranno entrambi la forma:
>
>
> Si avrà che il prodotto per concatenazione $L_1L_1$ sarà accettato dall'automa $\widehat{\mathcal{M}}$:
>


In particolare questo prodotto è un esempio di prodotto per concatenazione di un linguaggio per se stesso. Possiamo in generale definire dal prodotto l'operazione potenza di un linguaggio come:

$$
    \begin{cases}
    L^0=\{\varepsilon\}\\
    L^{n+1}=LL^n
    \end{cases}
$$


### Iterazione


> [!definition] Iterazione (Star)
> Se $L \subseteq A^*$, definiamo:
> $$
>     L^*=\{w_1\cdots w_n \vert n \in \mathbb{N}, w_i \in L\}=\bigcup\limits_{n \in \mathbb{N}}^\infty  L^n
> $$


Essendo l'operazione Star definita tramite uso di un unione infinita di linguaggi regolari, non possiamo ricavarla direttamente come applicazione finita di operazioni di unione e prodotto. Per questo è necessario definire separatamente questa operazione.

> [!theorem] Chiusura dei Linguaggi regolari per Iterazione
> **Enunciato. ** Sia $L \subseteq A^*$ regolare. Allora $L^*$ è regolare.
>
>
> **Dimostrazione. ** Sia $\mathcal{M}=(Q,A,\delta,q_1,F)$ un DFA **non-restarting** tale che $L=L(\mathcal{M})$.
>
> Definiamo un NFA $\widehat{\mathcal{M}}=(Q, A, \widehat{\delta}, q_1, \{q_1\})$ con:
>
> $$
>     \forall a \in A: \widehat{\delta}(q,a)=\begin{cases}
>     \{\delta(q,a)\}, & \delta(q,a) \notin F\\
>     \{\delta(q,a), q_1\}, \text{ altrimenti}
>     \end{cases}
> $$

>
> Per vedere come $L^*=L(\mathcal{M})$ verifichiamo la doppia inclusione.
>
> - **``$\subseteq$''** Verifichiamo per induzione che $L^*\subseteq L(\widehat{\mathcal{M}})$. Come base induttiva possiamo facilmente notare che $\varepsilon \in L(\widehat{\mathcal{M}})$.
> Per quanto riguarda il passo induttivo invece supponiamo $L^{n-1}\subseteq L(\widehat{\mathcal{M}})$ e mostriamo che $L^n \subseteq L(\widehat{\mathcal{M}})$.
>
> Siano $u \in L^{n-1}, v \in L$ tali che $w=uv$. Si ha $q_1 \in \widehat{\delta}^*(q_1,u)$ per ipotesi induttiva. Ma allora essendo $v \in L$ partendo da $q_1$ si tornerà in $q_1$ per costruzione di $\widehat{\mathcal{M}}$. Si avrà dunque che $q_1 \in \widehat{\delta}^*(q_1,uv) \implies L^n \subseteq L(\widehat{\mathcal{M}})$
>
> - **``$\supseteq$''** Si ha che $L(\widehat{\mathcal{M}}) \subseteq L^*$ poiché, per costruzione di $\widehat{\mathcal{M}}, w \in L(\mathcal{M})$ è composizione di parole di $L$, dovendo per terminare raggiungere $q_1$, ovvero l'unico stato terminale di $\mathcal{M}$. Essendo che $L$ era **non-restarting** l'unico modo per raggiungere $q_1$ in $\widehat{\mathcal{M}}$ è raggiungere uno stato terminale di $L$.
>


---


\begin{generalbox}
[colframe=azure-gradient-3!90!black]
{Esempio: Iterazione di Linguaggi Regolari}
Consideriamo ad esempio il linguaggio $L=\{ab,ba\}$, accettato dall'automa $\mathcal{M}$:


Si avrà che l'iterazione $L^*$ sarà accettata dall'automa $\widehat{\mathcal{M}}$:


È evidente però che questo automa non sia il più semplice possibile che accetti $L^*$. Infatti, $\widehat{\mathcal{M}}$ può essere semplificato in:


---


> [!theorem] Teorema di Kleene
>
> **Enunciato.** Un linguaggio $L \subseteq A^*$ è regolare *se e solo se* è finito oppure è ottenuto da linguaggi finiti mediante un numero finito di operazioni di unione, concatenazione e iterazione.
>
>
> **Dimostrazione.** Dimostriamo la doppia implicazione.
>
> - **``$\Rightarrow$''** Ovvio dai teoremi*(ref: Regolarità dei linguaggi finiti)**(ref: Regolarità dell'unione)*,*(ref: Regolarità dell'intersezione)* e*(ref: Regolarità dell'iterazione)*.
> - **``$\Leftarrow$''** Sia $\mathcal{M}=(Q,A,\delta,q_1,F)$ un DFA con $Q=\{q_1,\cdots,q_n\}$. Definiamo dunque una famiglia di linguaggi della forma $R^{(k)}_{i,j}$, dove:
> $$
>     \forall 1 \leq i&, j \leq n \land 0 \leq k \leq n:\\
>     &R^{(k)}_{i,j}=\{w \in A^* \vert \delta^*(q_i,w)=q_j \land \delta^*(q_i,w') \in \{q_1,\cdots,q_k\} \forall w'\neq \varepsilon \text{ prefisso proprio di } w \}
> $$

>
> Ovvero fissati $i$, $j$ e $k$, il linguaggio $R^{(k)}_{i,j}$ conterrà le parole che mi permettono di raggiungere lo stato $q_j$ da $q_i$ passando solo per stati $q \in \{q_1,\cdots,q_k\}$.
>
> Nella definizione formale data, la seconda condizione richiede sostanzialmente che ogni sotto stringa di $w$ ci porti **esclusivamente** in stati da $q_1$ a $q_k$.
>
> È per questo fondamentale specificare che $w'$ debba essere un prefisso **proprio** di $w$, ovvero diverso da $w$ stesso, poiché altrimenti ogni insieme con $k<j$ sarebbe vuoto, poiché le parole al suo intero dovrebbero raggiungere lo stato $q_j$ dovendo passare esse stesse, non solo le loro sotto stringhe, solo per stati da $q_1$ a $q_k$, ovvero impossibilitando l'arrivo in $q_j$.
>
> Analogamente è fondamentale specificare che $w'$ non sia la parola vuota, per evitare una contraddizione simile a quella appena vista ma nel caso $i>k$. Si avrà in fatti in questo caso che per ogni parola, si dovrà avere che:
>
> $$
>     \{q_1, \cdots, q_k\} \ni \delta^*(q_i,\varepsilon) = q_i \notin \{q_1, \cdots, q_k\}
> $$

>
> Definiti dunque questi insiemi possiamo osservare che:
>
> $$
>     R^{(0)}_{i,i}&=\{\varepsilon\} \cup \{a \in A^* \vert \delta(q_i, a) = q_i\} \text{ è un insieme finito}\\
>     \text{Con } i \neq j: R^{(0)}_{i,j}&=\{a \in A \vert \delta(q_i, a) = q_j\}, \text{ è un insieme finito} \\
>     R^{(k+1)}_{i,j}&=R^{(k)}_{i,j} \cup R^{(k)}_{i,k+1}\cdot {(R^{(k)}_{k+1,k+1})}^* \cdot R^{(k)}_{k+1,j}
> $$

>
>
> In particolare l'ultima osservazione ci dice che tutte le parole che ci portano da $q_i$ a $q_j$ attraversando esclusivamente stati da $q_1$ a $q_{k+1}$ possono essere di due tipi, ovvero quelle che raggiungono $q_j$ passando soltanto per stati da $q_1$ a $q_k$, ovvero ignorando lo stato $q_{k+1}$, e quelle che attraversano almeno una volta $q_{k+1}$.
>
> In particolare queste raggiungeranno $q_{k+1}$ una prima volta, passando dunque solo per stati da $q_1$ a $q_k$, torneranno in $q_{k+1}$ un numero arbitrario di volte, ancora passando solo per stati da $q_1$ a $q_k$, e infine lasceranno un'ultima volta $q_{k+1}$ per raggiungere $q_j$ passando ancora solo da stati tra $q_1$ e $q_k$. Questa divisione si può evincere più chiaramente dal diagramma seguente:
>
>
>
>
> Con queste tre osservazioni possiamo dimostriamo dunque per induzione su $k$ che **ogni linguaggio ** $R^{(k)}_{i,j}$ può essere ottenuto da linguaggi finiti mediante un numero finito di operazioni di unione, concatenazione e iterazione.
>
> Possiamo ora facilmente vedere però che per ogni automa a stati finiti $\mathcal{M}$ di $n$ stati, in particolare quello considerato all'inizio della dimostrazione, vale che $L(\mathcal{M})= \bigcup\limits_{q_j \in F}R^{(n)}_{1,j}$.
>
> Ovvero il linguaggio accettato dall'automa è l'unione dei linguaggi che portano da $1$ a un qualsiasi stato terminale fissato passando potenzialmente per tutti e $n$ gli stati,
> cioè dunque un qualsiasi linguaggio regolare è sempre della forma $R^{(k)}_{i,j}$ per qualche $i,j,k$ definiti come sopra, la quale è sempre come da tesi.


---


## Espressioni Regolari


Avendo analizzato le operazioni che permettono di ottenere linguaggi regolari, possiamo ora definire un modo per descrivere questi linguaggi in modo più compatto e semplice, ovvero delle stringhe che seguano specifiche regole sintattiche e che, abbinate a una semantica ben definita, permettano di descrivere tutti i linguaggi regolari.
> [!definition] Espressioni regolari
> Dato $A$ alfabeto finito, definisco:
>
> $$
>     \widehat{A} = \{\underline{a} \vert a \in A\} \cup \{\underline{\cup}, \underline{\cdot}, \underline{*}, \underline{(}, \underline{)}, \underline{\varepsilon}, \underline{\varnothing}\} % chktex 9
> $$

>
> Chiameremo **espressione regolare** su $A$ una parola su $\widehat{A}^*$ ottenuta dalle seguenti regole:
>
> 1. $\forall a \in A: <u>a</u>$ è un'espressione regolare, così come $<u>\varepsilon</u>$ e $<u>\varnothing</u>$.
> 2. Se $\alpha$ e $\beta$ sono espressioni regolari, allora anche $<u>(</u>\alpha<u>\cup</u>\beta<u>)</u>$ lo è.
> 3. Se $\alpha$ e $\beta$ sono espressioni regolari, allora anche $<u>(</u>\alpha<u>\cdot</u>\beta<u>)</u>$ lo è.
> 4. Se $\alpha$ è un'espressione regolare, allora anche $<u>(</u>\alpha<u>)*</u>$ lo è.
> 5. Non ci sono altre regole.


### Semantica delle Espressioni Regolari


Oltre ad aver definito la sintassi delle espressioni regolari, per far si che queste possano essere utilizzate per descrivere linguaggi regolari è necessario definire una semantica per queste espressioni, ovvero un modo per interpretare le espressioni regolari come linguaggi regolari.

Se $\gamma$ è un'espressione regolare su $A$, il linguaggio associato a $\gamma$: $\langle \gamma \rangle \subseteq A^*$ è definito dalle regole semantiche:

1. $\forall a \in A: \langle <u>a</u> \rangle=\{a\}$, inoltre $\langle <u>\varepsilon</u> \rangle=\{\varepsilon\}$ e $\langle <u>\varnothing</u> \rangle=\varnothing$.
2. Se $\gamma = <u>(</u>\alpha<u>\cup</u>\beta<u>)</u>$, allora $\langle \gamma \rangle=\langle \alpha \rangle\cup\langle \beta \rangle$.
3. Se $\gamma = <u>(</u>\alpha<u>\cdot</u>\beta<u>)</u>$, allora $\langle \gamma \rangle=\langle \alpha \rangle\cdot\langle \beta \rangle$.
4. Se $\gamma = <u>(</u>\alpha<u>)</u>^{<u>*</u>}$, allora $\langle \gamma \rangle={(\langle \alpha \rangle)}^*$.

Il teorema di Kleene*(ref: Teorema di Kleene)* può essere dunque reinterpretato come:

$$
    L \subseteq A^* \text{ regolare } \iff \exists \alpha \text{ espressione regolare su } A \text{ tale che } L=\langle \alpha \rangle
$$


\begin{generalbox}
[colframe=azure-gradient-3!90!black]
{Esempio: Espressione Regolare}
Consideriamo il linguaggio dell'esercizio*(ref: Automa L_a)* sull'alfabeto $\{a,b\}$.

Si avrà che l'espressione regolare che lo definisce è:

$$
    \alpha = [[a \cup b ] \cdot [[a \cup b] \cup  [a \cdot [[a \cup b]^* \cdot a]] \cup [b \cdot [[a\cup b]^* \cdot b]]]]
$$


Per comodità di scrittura, possiamo definire delle regole di precedenza tra gli operatori in modo da evitare di dover usare le parentesi e per sottintendere il simbolo $\cdot$. In particolare, definiamo:

$$
    * > \cdot > \cup
$$


Avremo quindi che l'espressione regolare dell'ultimo esempio può essere scritta come:

$$
    \alpha = (a \cup b ) (a \cup b \cup a{(a\cup b)}^*a \cup b{(a\cup b)}^*b)
$$


---


## Pumping Lemma per Linguaggi Regolari


Fino ad ora abbiamo analizzato e descritto esclusivamente linguaggi regolari e come operare su di essi.

Vogliamo ora analizzare il problema opposto, ovvero come dimostrare che un linguaggio non è regolare.

Per fare ciò, introduciamo un risultato teorico che dimostra una condizione necessaria per la regolarità di un linguaggio, che se quindi negata ci permette di dimostrare che un linguaggio non è regolare.

Questo risultato è il **Pumping Lemma per Linguaggi Regolari**, e sfrutta un principio combinatorio detto **principio della piccionaia**.

Il **principio della piccionaia** afferma che se $n$ piccioni vengono messi in $m$ piccionaie, con $n>m$, allora almeno una piccionaia conterrà almeno due piccioni.

Generalizzando questo concetto, potremmo dire che se ho $n$ oggetti da distribuire su $m$ insiemi, con $n>m$, non potrò fare a meno di associare a più oggetti lo stesso insieme.

> [!theorem] Pumping lemma per linguaggi regolari (lemma uwu)
> **Enunciato. ** Sia $\mathcal{M}$ un DFA con $n$ stati, e $x\in L(\mathcal{M})$ tale che $|x| \geq n$. Allora esistono $u,v,w \in A^*$ tali che:
>
> 1. $x=uvw$
> 2. $v \neq \varepsilon$
> 3. $\forall i \in \mathbb{N}: uv^{i}w \in L(\mathcal{M})$, ovvero $ \{u\}\{v\}^*\{w\} \subseteq L(\mathcal{M})$
>
>
> **Dimostrazione. ** Per il principio della piccionaia, nel percorso di accettazione di $x$ (da $q_1$ a $q_k \in F$), che passa necessariamente per almeno $n+1$ stati dovendo includere anche lo stato iniziale, deve esistere un ciclo, ovvero si passerà per un certo stato $q_l$ almeno due volte.
>
> Si ha allora $x=uvw$, dove $\delta^*(q_1,u)=q_l$, ovvero $u$ è la parola che porta da $q_1$ a $q_l$, $\delta^*(q_l,v)=q_l$, ovvero $v$ è la parola descitta dal ciclo partente da $q_l$, e $\delta^*(q_l,w)=q_k$, ovvero $w$ è la parola che porta dalla fine del ciclo fino allo stato terminale $q_k$.
>
> Avremo dunque chiaramente che $v \neq \varepsilon$, dovendo passare per $q_l$ almeno due volte distinte, ma anche che $\forall i \in \mathbb{N}: \delta^*(q_1,uv^{i}w)=q_k$, potendo percorrere il ciclo un numero arbitrario di volte, da cui la tesi.
>
> La suddivisione di $x$ in $u,v,w$ come da dimostrazione è più facilmente intuibile dal seguente diagramma:
>
>
>


Visto questo importante risultato, possiamo dunque dimostrare che un linguaggio non è regolare dimostrando che non rispetta il **Pumping Lemma**.

Oltre a fare ciò però è possibile derivare dal **Pumping Lemma** altri risultati teorici minori utili.

> [!theorem] Corollario 1
> **Enunciato. ** Sia $\mathcal{M}$ un DFA con $n$ stati, allora $L(\mathcal{M}) \neq \varnothing \implies \exists x \in L(\mathcal{M}): |x| < n$.
>
>
> **Dimostrazione. ** Per assurdo, supponiamo che $x \in L(\mathcal{M})$ sia la parola di lunghezza minima con $|x| \geq n$.
>
> Per il pumping lemma, esistono $u,v,w \in A^*$ tali che $x=uvw$, con $v \neq \varepsilon$ e $\forall i \in \mathbb{N}: uv^{i}w \in L(\mathcal{M})$. Ma allora $uv^0w=uw \in L(\mathcal{M})$, contraddicendo la minimalità di $x$.
>


Questo corollario risulta particolarmente utile per determinare se, dati due DFA $\mathcal{M}_1, \mathcal{M}_2$, si ha che $L(\mathcal{M}_1) \subseteq L{(\mathcal{M})}_2$.

Si ha infatti che, poiché $L(\mathcal{M}_1) \setminus L(\mathcal{M}_2) = L(\mathcal{M}_1) \cap \overline{L(\mathcal{M}_2)}$  è regolare, possiamo disegnare un DFA $\mathcal{M}$ che accetti $L(\mathcal{M}_1) \setminus L(\mathcal{M}_2)$, e verificare se $L(\mathcal{M})=\varnothing$.

Dal corollario appena dimostrato però, per dimostrare che la differenza sia vuota è sufficiente che
$$
    \forall x \in A^* |x| < n \implies x \notin L(\mathcal{M})
$$


Ovvero che non ci siano parole di lunghezza minore del numero di stati dell'automa accettate dal linguaggio.

---


> [!theorem] Corollario 2
> **Enunciato. ** Sia $\mathcal{M}$ un DFA con $n$ stati, allora $L(\mathcal{M})$ è infinito $\iff \exists x \in L(\mathcal{M}): n \leq |x| < 2n$.
>
>
> **Dimostrazione. ** Dimostriamo la doppia implicazione.
>
> - **``$\Rightarrow$''** Dal **Pumping Lemma**, $x=uvw$ con $v \neq \varepsilon$ e $\forall i \in \mathbb{N}: uv^{i}w \in L(\mathcal{M})$. Avremo dunque che $L$ accetta un numero infinito di parole, al variare di $i$ in $\mathbb{N}$.
> - **``$\Leftarrow$''** Essendo $L(\mathcal{M})$ infinito, la lunghezza delle parole non può essere superiormente limitata, altrimenti sarebbe possibile contare il numero massimo di parole accettabili.
>
> Sia $x$ dunque la più corta parola in $L(\mathcal{M})$ tale che $|x| \geq 2n$. Possiamo dunque scrivere $x=yz$ con $|y|=n$ e $|z|\geq n$. Per il principio della piccionaia, avremo $y=uvw$ con $v \neq \varepsilon$ e $\forall i \in \mathbb{N}: \delta^*(q_1,uv^{i}w)=\delta^*(q_1,y)$, ovvero al variare di $i$ raggiungerò lo stesso stato raggiunto con $y$, da cui $\forall i \in \mathbb{N}: uv^{i}wz \in L(\mathcal{M})$.
>
> Allora anche $uwz \in L(\mathcal{M})$ ma $|uwz| < |yx|=|x|$, da cui $|uwz| < 2n$ dalla minimalità di $x$. Ma essendo $|z| \geq n$ per costruzione, si ha che $|uwz| \geq n$, da cui la tesi.


Vediamo ora finalmente degli esempi di **Linguaggi non Regolari**, e di come dimostrare ciò utilizzando il **Pumping Lemma**.

> [!example] Esempi: Linguaggi non regolari
>
> 1. Il linguaggio $L = \{a^{n}b^n \vert n \in \mathbb{N}\}$, ovvero un linguaggio che accetti solo parole con un numero di $a$ consecutive seguito da un ugual numero di $b$ consecutive, **non** è regolare.
>
>
>
> Infatti sia per assurdo $\mathcal{M}$ un DFA con $p$ stati, tale che $L(\mathcal{M})=L$.
>
>
>
> Presa $x=a^{p}b^p$, se $x=uvw$ con $v\neq \varepsilon$ sono possibili tre casi:
>   1. $v=a^j, j>0 \implies uw=a^{p-j}b^p \notin L$
>   2. $v=b^j, j>0 \implies uw=a^{p}b^{p-j} \notin L$
>   3. $v=a^{j}b^k, j,k>0 \implies uv^2w = a^{p-j}{(a^{j}b^k)}^2b^{p-k}=a^{p}b^{k}a^{j}b^p \notin L$
>
>
>
> In questo esempio specifico è possibile dimostrare la tesi anche con altri valori di $i$, come ad esempio $i=0$ nell'ultimo caso, ma in generale questo non è possibile.
>
>
>
> Abbiamo quindi che per qualsisi scelta di $v$ il **Pumping Lemma** non è rispettato, dimostrando la tesi.
>
>
>
> 2. Il linguaggio $L' = \{a^{m}b^n \vert m \geq n > 0\}$, non è regolare.
>
>
>
> Infatti sia per assurdo $\mathcal{M}$ un DFA con $p$ stati, tale che $L(\mathcal{M})=L'$.
>
>
>
> Scelgo $x=a^{p}b^{p} \in L, |x|=2p\geq p$. Possiamo dividere i casi possibili in maniera analoga all'esempio precedente, con l'unica differenza che nel primo caso non potremo scegliere un'arbitraria $i$ per la dimostrazione, poichè $ \forall i\geq 1$ la parola sarebbe ancora accettata dall'automa, dunque siamo costretti a scegliere $i=0 \implies uv^{i}w = uw$ per dimostrare la tesi.
>
>
>
> 3. Considerando invece il linguaggio $ L'' = \{a^{m}b^n \vert m > n > 0\}$, avremo che per la dimostrazione non potremo più usare la parola $a^{p}b^{p} \notin L''$. Possiamo però considerare la parola $ x=a^{p}b^{p-1} \in L'', |x|=2p-1\geq p$, che si suddivide nei medesimi tre casi degli esempi precedenti e si dimostra con la stessa scelta di $i$ del secondo esempio.
>
>
>
> 4. **Esercizio d'esame. ** Mostrare che $L = \{a^{n}b^{n} \vert n \geq 0\} \cup \langle b^*\cdot a^* \rangle$ non è regolare.
>
>
>
> **Soluzione. ** Per quanto il **Pumping Lemma** sia uno strumento utile per dimostrare la non regolarità di un linguaggio, non è sempre l'approccio corretto da seguire. In questo caso andremo ad utilizzare le proprietà di chiusura dei linguaggi regolari.
>
>
>
> Per assurdo, sia $L$ regolare. Allora dovrebbe esserlo anche $L \cap \langle a^*b^* \rangle$, ma $L \cap \langle a^*b^* \rangle = \{a^{n}b^{n} \vert n \geq 0\}$, che per quanto visto in precedenza non è regolare, da cui l'assurdo.
>


Come già intuito dall'ultimo esempio, e come è evincibile dall'enunciato stesso, il **Pumping Lemma** non fornisce una condizione sufficiente per la regolarità di un linguaggio, bensì una condizione necessaria.

Possono esistere dunque linguaggi non regolari che rispettano il **Pumping Lemma**, e per questo motivo non è possibile dimostrare la regolarità di un linguaggio utilizzando il **Pumping Lemma**.

Utilizzando però l'enunciato di **Pumping Lemma** dato possiamo trovare dei linguaggi non regolari, per i quali anche la non regolarità non è dimostrabile utilizzandolo.

Vediamo dunque una versione più forte del **Pumping Lemma**, derivabile in maniera diretta dalla dimostrazione precedente, per poi vedere un esempio di linguaggio non regolare per il quale non è possibile dimostrare la non regolarità utilizzando il **Pumping Lemma** precedente.

---


> [!theorem] Pumping Lemma per linguaggi regolari rafforzato
> **Enunciato. ** Sia $\mathcal{M}$ un DFA con $n$ stati, e $x\in L(\mathcal{M})$ tale che $|x| \geq n$. Allora esistono $u,v,w \in A^*$ tali che:
>
> 1. $x=uvw$
> 2. $v \neq \varepsilon$
> 3. $\forall i \in \mathbb{N}: uv^{i}w \in L$
> 4. $|uv| \leq n$
>
>
> **Dimostrazione. ** Per dimostrare questa versione del **Pumping Lemma** consideriamo la parola $x_n \subseteq x$ formata dalle prime $n$ lettere.
>
> Per il principio della piccionaia sappiamo che già in questa parola deve essere presente almeno uno stato ripetuto.
>
> Potrò allora scegliere come $u$ la sottoparola di $x$ fino a questo primo stato ripetuto, con dunque $u \subseteq x_n$, come $v$ la parola del ciclo contenuto in $x_n$, e come $w$ la parola formata dalle restanti lettere di $x$.
>
> Avendo scelto $u,v \subseteq x_n$ si ha che $|uv| \leq n$, da cui la tesi.


> [!example] Esempio: Non regolarità del linguaggio dei palindromi
>
> Vediamo dunque un esempio di linguaggio non regolare, che però non può essere dimostrato con il precedente **Pumping Lemma**.
>
>
>
> Sia $L = \{w \in \{a,b\}^* \vert w=\widetilde{w} \} $, dove se $ w=w_1w_2\cdots w_n, w_1w_2\cdots w_n \in \{a,b\}^* $ allora $ \widetilde{w} = w_{n}w_{n-1}\cdots w_1 $. Questo linguaggio non è regolare.
>
>
>
> Proviamo inizialmente a dimostrare col **Pumping Lemma** originario che $L$ non è regolare.
>
>
>
> Sia $p$ il numero di stati di un DFA che accetta $L$. Avremo che, per ogni parola di $L$, si potrà sempre scegliere $v$ come la sotto parola centrale e ottenere una parola in $L$. Infatti, se $x=uvw=\widetilde{x}$ con $v=\widetilde{v}$, allora $w=\widetilde{u}$ e dunque $\forall i \in \mathbb{N}: uv^{i}w \in L$.
>
>
>
> Utilizzando il **Pumping Lemma** rafforzato però, sappiamo che $|uv| \leq p$, ovvero $v$ dev'essere contenuta nelle prime $p$ lettere di $x$. Ma allora $v$ non può essere la sotto parola centrale di $x$.
>
> Consideriamo la parola $x=a^{p}ba^{p} = uvw $, con $v \neq \varepsilon $ e $|uv| \leq p$. Allora avremo necessariamente che:
> $$
>     v=a^k, p\geq k>0 \implies uw=a^{p-k}ba^{p} \notin L
> $$

>
> da cui la tesi.

