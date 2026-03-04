# Macchine di Turing e Automi a Stati Finiti


Per la valutazione della calcolabilità fino a ora ci siamo limitati a un unico modello di calcolo, ovvero il linguaggio S. Questo modello è stato scelto per la sua semplicità e per la sua capacità di calcolare tutte le funzioni calcolabili.

Nonostante ciò esistono altri modelli di calcolo che sono equivalenti a S, ovvero che calcolano le stesse funzioni calcolabili essendo però ancora più minimali.

Il linguaggio S infatti, nonostante possa sembrare già minimale, mette in realtà a disposizione operazioni non esattamente banali. Infatti una macchina che fa un incremento deve sapere ad esempio che al numero $99$ segue $100$, cosa che rappresentando i numeri come stringhe di caratteri da $0$ a $9$ non è banale.

Ciò nonostante quanto detto in precedenza rimane vero, ovvero che ogni funzione calcolabile è calcolabile da S e il linguaggio S è minimale nelle istruzioni.

La banalità delle istruzioni è raggiunta considerando i numeri in base $1$, ovvero non più come stringhe di cifre da $0$ a $9$ ma come stringhe di $1$.
$(x \mapsto \underbrace{1, \cdots , 1}_x )$

Interpretando in questo modo i numeri, le operazioni diventano banali, ad esempio l'incremento diventa aggiungere un $1$ alla fine della stringa e il decremento rimuoverne uno.

La base $1$ però ha molte limitazioni, ad esempio per quanto riguarda la rappresentazione, ogni numero avrebbe infatti bisogno di spazio $n$ per essere rappresentato.

Per ovviare a questo problema è possibile definire linguaggi $S_n$ **equivalenti a S** adatti a lavorare in base $n$ arbitraria.

Questi linguaggi però condividono con il linguaggio S il difetto di non essere pienamente generali, poiché presuppongono di avere come input e output numeri naturali che, per quanto possano codificare ogni insieme con cardinalità minore di $\mbR$, limitano la generalità del modello.

## Macchine di Turing


Uno dei primi modelli di calcolo fu stato proposto da Alan Turing nel 1936. Questo modello, equivalente anch'esso al linguaggio S, è detto **Macchina di Turing**.

Una macchina di Turing può essere immaginata come una macchina con un nastro infinito, su cui sono scritti dei simboli. La macchina può a ogni istante in base alle istruzioni fornite cambiare cosa c'è scritto sul nastro e spostarsi a destra o a sinistra o cambiare stato, altra cosa che caratterizza queste macchine.

\caption{Rappresentazione grafica del nastro di una macchina di Turing}
\end{figure}

---


> [!definition] Macchina di Turing
> Una macchina di Turing è una quadrupla $(Q, A, I, q_1 \in Q)$ dove:
> - $Q$ è un insieme finito (di stati);
> - $A$ è un insieme finito (Alfabeto), che non contenga i simboli $\{\text{\Large{**\textvisiblespace**}}, L , R\}$;
> - $I \subseteq Q \times (A \cup \{\text{\Large{**\textvisiblespace**}}\}) \times (A \cup \{\text{\Large{**\textvisiblespace**}}, L, R\}) \times Q$, è l'insieme delle istruzioni. Queste sono quadruple in cui i primi due valori ci danno stato e valore scritto da verificare e i secondi due ci danno il valore da scrivere e il nuovo stato;
> - $q_1$ è lo stato iniziale.


Come è già chiaro dalla definizione delle macchine di Turing queste sono più generali del linguaggio S, non presupponendo un dominio specifico per l'input e l'output, e definendo inoltre operazioni banali a prescindere dalla rappresentazione dei dati.

Per ottenere l'output di una macchina di Turing $\mathcal{M}$ rispetto a un input esprimibile come stringa su $A$, facciamo sì che la macchina parta dallo stato $q_1$ su un ``nastro'' vuoto tranne che nelle posizioni immediatamente a destra di quella di $\mathcal{M}$, occupate dai caratteri della stringa di input.

L'esecuzione continuerà finché in $I$ saranno presenti istruzioni con stato e carattere di controllo corrispondenti alla situazione attuale (stato e simbolo correnti).
L'output esiste se l'esecuzione termina (e in tal caso consisterà in ciò che è rimasto scritto sul nastro).

Essendo questo processo come detto generale e del tutto indipendente dalla tipologia di dominio di input e output, questo modo di procedere è perfettamente valido per le funzioni in $\mathbb{N}$.

Consideriamo una macchina di Turing $\mathcal{M}$ unaria con dominio $\mathbb{N}$ in base $1$, ovvero si comporti come il linguaggio S.
$$
    \mathcal{M} = (Q,A,I,q_n) : Q = \{q_1, q_2, q_3\}, A = \{1\}, I=\{(q_1, \text{\Large{\mathbf{\textvisiblespace}}}, R,q_2), (q_2,1,R,q_2), (q_2, \text{\Large{\mathbf{\textvisiblespace}}}, 1, q_3), (q_3,1, R, q_3), (q_3, \text{\Large{\mathbf{\textvisiblespace}}} , 1, q_1)\}
$$


}
\subfloat[Secondo Step] {
}

\subfloat[Terzo Step] {
}
\subfloat[Quarto Step] {
}

\subfloat[Quinto Step] {
}
\subfloat[Sesto Step] {
}

\subfloat[Settimo Step] {
}
\end{figure}

Questa macchina di Turing calcola la funzione $f(n) = n+2$, poiché su un input generico aggiungerà sempre due volte '$1$'.

Le macchine di Turing possono calcolare anche funzioni non unarie, separando gli input con degli spazi vuoti.

Questo modello di calcolo ci suggerisce che il dominio delle stringe renda il calcolo ancora più elementare e astratto essendo ogni numero rappresentabile come una stringa di caratteri.

In questo passaggio di astrazione andremo a chiamare:
- $A^*$ l'insieme delle stringhe su $A$, compresa $\varepsilon$ (stringa vuota);
- $L \subseteq A^*$ un linguaggio su $A$.

Diremo che un linguaggio $L$ è ricorsivamente enumerabile se esiste una macchina di Turing $\mathcal{M}$ che termina se e solo se l'input appartiene a $L$.
Essendo i linguaggi generalizzazione dei sottoinsiemi di $\mathbb{N}$, questa definizione comprende quella data per i sottoinsiemi di $\mathbb{N}$.
Diremo che un linguaggio $L$ è ricorsivo se $L$ e $\overline{L}=A^* \setminus L$ sono ricorsivamente enumerabili.

Consideriamo ora la versione più limitata possibile di macchina di Turing, ovvero che possa solo scorrere in una direzione o cambiare stato. Queste macchine sono dette **automi a stati finiti**.

## Automi a Stati Finiti


Un Automa a Stati Finiti è una macchina che legge un input e può solo cambiare stato di conseguenza.

Questo tipo di macchine non producono output, e possono dunque esclusivamente *accettare*, ovvero terminare, o meno una parola. Per questo motivo vengono dunque detti **accettori** e hanno solo due configurazioni finali, quella di **accettazione** e quella di **rifiuto**.

Andiamo dunque a definire formalmente un primo tipo di **accettore**, gli **Automi Finiti Deterministici**.

### Automi Finiti Deterministici


> [!definition] Automi Finiti Deterministici
> Un automa finito deterministico (DFA) è una quintupla $(Q, A, \delta, q_1, F)$ dove:
> - $Q$ è un insieme finito (di stati);
> - $A$ è un insieme finito (Alfabeto);
> - $\delta : Q \times A \rightarrow Q$ è una funzione detta di transizione;
> - $q_1 \in Q$ è lo stato iniziale;
> - $F \subseteq Q$ è l'insieme degli stati terminali o di accettazione.


Questi automi sono detti deterministici poiché, grazie alla funzione $\delta$, non esistono transizioni ambigue, ovvero per ogni stato e simbolo di input è definito un unico stato successivo. In oltre, dalle proprietà delle applicazioni, sappiamo che per ogni stato dev'essere associata un istruzione per simbolo di input.
Definiamo dunque per ricorrenza la funzione di transizione iterata come:
$$
    \delta^*&: Q \times A^* \rightarrow Q \\
    \delta^*(q, w) &= \begin{cases}
    \delta^*(q, \varepsilon) = q, \forall q \in Q\\
    \delta^*(q, wa) = \delta(\delta^*(q,w),a).
    \end{cases}
$$


Diremo quindi che un linguaggio $L$ è accettato da una DFA $\mathcal{M}$ *se e solo se* $L = L(\mathcal{M}) = \{w\in A^* \vert \delta^*(q_1,w)\in F\}$, dove per $L(\mathcal{M})$ si intende l'insieme delle stringhe accettate da $\mathcal{M}$.

> [!example] Esempio: DFA
> Sia $\mathcal{M}=(Q,A,\delta,q_1,F)$ con $Q=\{q_1,q_2,q_3,q_4\}, A=\{a,b\}, F=\{q_4\} \text{ e } \delta$ definita dalla seguente tabella:
>
>
> | $\pmb{\delta}$ | $\pmb{a}$ | $\pmb{b}$ |
> |---|---|---|
> | $\pmb{q_1}$ | $q_2$ | $q_3$ |
> | $\pmb{q_2}$ | $q_2$ | $q_4$ |
> | $\pmb{q_3}$ | $q_3$ | $q_3$ |
> | $\pmb{q_4}$ | $q_3$ | $q_4$ |

>
>
> Possiamo subito notare che $q_3$ non è uno stato terminale ma una volta raggiunto non è possibile uscirne, questo tipo di stato è detto **stato pozzo**.
>
> Da questo possiamo vedere che le parole accettate **devono necessariamente iniziare** per $a$ poiché altrimenti entreremo nel pozzo immediatamente. Inoltre essendo $q_1$   **non terminale** non possiamo accettare la stringa vuota.
>
> Dovendo necessariamente avere una lettera $a$ come iniziale, arriveremo necessariamente nello stato $q_2$. Da qui, sia $a$ che $b$ saranno accettate. Infatti per $a$ rimarremo in $q_2$ e per $b$ andremo in $q_4$ che è uno stato terminale, in cui potremo rimanere finché non arriverà una $a$ che porta nel **pozzo**.
>
> Seguendo quindi le transizioni possiamo notare che le parole accettate da $\mathcal{M}$ sono quelle formate da una serie di $a$ seguite da una serie di $b$. Ovvero $L(\mathcal{M})=\{a^{n}b^m \vert n,m > 0\}$.
>


Per denotare la concatenazione successiva di parole identiche, utilizzeremo la notazione di elevamento a potenza. La notazione varia rispetto al testo di riferimento, il quale utilizza parentesi quadre aggiuntive per indicare l'esponente.

In generale se $w\in A^*$, avremo che:

$$
    \begin{cases}
    w^0=\varepsilon\\
    w^{n+1}=ww^n
    \end{cases}
$$

#### Diagramma di Transizione di stato di un DFA


Esaminiamo adesso un approccio alternativo per la rappresentazione di tali automi. Prendiamo in considerazione l'esempio precedentemente menzionato*(ref: DFA Esempio)*. Un metodo per rappresentare le transizioni di stato consiste nel disegnare un grafo orientato in cui ogni stato è un nodo e ogni transizione è un arco.
Ad esempio avremo:

\caption{Diagramma di Transizione di Stato di un DFA}
\end{figure}


In questa rappresentazione un qualsiasi $q \in Q $ avrà il doppio cerchio   *se e solo se* $q \in F$. Mentre lo stato iniziale è indicato con una freccia entrante nello stato senza stato di partenza.

Ora che sappiamo come rappresentare graficamente un DFA, possiamo caratterizzare i linguaggi sono accettati da tali DFA, chiamati **linguaggi regolari**.

### Linguaggi Regolari


> [!definition] Linguaggi Regolari
> Un linguaggio $L \subseteq A^*$ è regolare se esiste una DFA $\mathcal{M}$ su $A$ tale che $L=L(\mathcal{M})$.


Dalla definizione appena data, i **linguaggi regolari** sembrano essere strettamente legati all'alfabeto su cui sono definiti. Tuttavia, come vedremo, questo non è il caso, poiché la regolarità di un linguaggio è mantenuta in tutti gli alfabeti che contengono quello in cui è definito.

> [!theorem] Indipendenza dei Linguaggi Regolari dall'alfabeto di supporto
> **Enunciato. ** Sia $A \subseteq A'$ e $L \subseteq A^*$. Allora
> $$
>     \exists\mathcal{M}=(Q,A,\delta,q_1,F):L=L(\mathcal{M}) \iff \exists\mathcal{M}'=(Q', A', \delta', q_1', F'):L=L(\mathcal{M}')
> $$

>
>
> **Dimostrazione. ** Dimostriamo la doppia implicazione:
> - **``$\Rightarrow$''** Se $L=L(\mathcal{M}) $, definiamo $Q'=Q\cup\{q_p\}$, dove $q_p \notin Q$ è uno stato pozzo$, q_1'=q_1, F'=F$ e $\delta'$ come:
> $$
>     \delta'(q,a)=\begin{cases}
>     \delta(q,a), & q \in Q \land a \in A\\
>     q_p, \text{altrimenti}
>     \end{cases}
> $$

>
> Avremo che $\mathcal{M}'$ si comporterà esattamente come $\mathcal{M}$ per tutte le parole di $A'^*$ che appartengono anche a $A^*$, mentre per tutte le altre non arriverà mai a terminazione.
> - **``$\Leftarrow$''** Se $L=L(\mathcal{M}')$, definiamo $Q=Q', F=F', q_1=q_1'$ e $\delta$ come la restrizione di $\delta'$ su $A$, ovvero:
> $$
>     \delta(q,a)=\delta'(q,a), \forall q \in Q, a \in A
> $$

>
> Avremo che $\mathcal{M}$ accetterà tutte le parole accettate da $\mathcal{M}'$ composte unicamente da simboli in $A$. Essendo però che $L\subseteq A^*$, avremo che $\mathcal{M}$ accetterà tutte le parole di $L$.


---


Consideriamo ora un esempio di linguaggio regolare per meglio comprendere la definizione appena data.

> [!example] Esempio: Linguaggio regolare
> Si consideri il linguaggio su $A=\{a\}$ definito da $L=\{a^{6k+1} \vert k \in \mathbb{N}\}$. Questo corrisponde a tutti i numeri che hanno resto $1$ nella divisione per $6$. Per dimostrare che questo linguaggio è regolare, possiamo dunque costruire un DFA che lo accetti come segue:
>
>
>
> Avremo che infatti una qualsiasi parola di $A^*$ sarà accettata *se e solo se* farà esattamente un numero qualsiasi di ``giri completi'' del diagramma e termini con un ``passo aggiuntivo'' per raggiungere $q_2$, in poche parole se la parola avrà lunghezza $l \equiv_6 1$.


#### Proprietà e caratterizzazione dei linguaggi regolari


Definiti bene i **linguaggi regolari** possiamo andare a descriverne alcune proprietà.

In primo luogo, possiamo vedere come ogni linguaggio $L\subseteq A^*$ regolare è anche un insieme **ricorsivamente enumerabile**[^1].

> [!theorem] Linguaggi regolari e ricorsivo enumerabilità
> **Enunciato. ** $L \subseteq A^*$ **regolare** $\implies L$ **ricorsivamente enumerabile**.
>
>
> **Dimostrazione. ** $L$ è ricorsivamente enumerabile *se e solo se* esiste una macchina di Turing $\mathcal{M}'$ che termina solo su input in $L$[^2].
>
> Sia $\mathcal{M}=(Q,A,\delta,q_1,F)$ una DFA tale che $L=L(\mathcal{M})$. Allora definiamo $Q'=Q\cup\{q_0\}$, con $q_0 \notin Q$ che funga da stato iniziale della macchina di Turing[^3] e poniamo
>
> $$
>     I=\{(q_0, \text{\Large{\mathbf{\textvisiblespace}}},R,q_1)\} \cup \{(q_1,a,R,\delta(q,a))\vert q\in Q, a \in A\} \cup \{(q,\text{\Large{\mathbf{\textvisiblespace}}},R,q_0)\vert q \in Q\setminus F\}
> $$

>
> Dove $(q_0, \text{\Large{**\textvisiblespace**}},R,q_1)$ serve a far iniziare la computazione alla macchina, $\{(q_1,a,R,\delta(q,a))\vert q\in Q, a \in A\}$ serve a farla continuare seguendo i percorsi di $\mathcal{M}$ e $\{(q,\text{\Large{**\textvisiblespace**}},R,q_0)\vert q \in Q\setminus F\}$ serve a non far terminare la computazione in caso la stringa sia terminata ma non si sia raggiunto uno stato terminale.


Possiamo però caratterizzare i linguaggi regolari in maniera più profonda. Iniziamo però prima da dimostrare una loro proprietà che ci aiuterà nella caratterizzazione.

> [!theorem] Regolarità del Complemento
> **Enunciato. ** $L \subseteq A^*$ regolare $\iff \overline{L}=A^*\setminus L$ è regolare.
>
>
> **Dimostrazione. ** Se $L=L(\mathcal{M})$ con $\mathcal{M}=(Q,A,\delta,q_1,F)$ DFA, allora $\overline{L}=L(\mathcal{M}')$ con $\mathcal{M}'=(Q,A,\delta,q_1,Q\setminus F)$. L'implicazione inversa è analoga.
>


Sfruttando questa proprietà, il teorema dimostrato subito prima e la caratterizzazione degli insiemi ricorsivi*(ref: Relazione tra ricorsività e ricorsivo enumerabilità)*, possiamo dedurre che $L$ è regolare $\implies L$ è ricorsivo.

---


> [!example] Esempio: Sintesi del Linguaggio accettato da un Automa
> Fino a ora abbiamo analizzato il caso in cui, dato un linguaggio abbiamo *sintetizzato* il diagramma di un automa che lo accetti. È però possibile anche fare il processo opposto. Vediamone un esempio.
>
> Sia $\mathcal{M}$ il DFA su $A=\{a,b,c\}$  con $Q=\{q_1,q_2,q_3,q_4,q_5\}, F=\{q_5\}$ e $\delta$ dato da:
>
>
> | $\pmb{\delta}$ | $\pmb{a}$ | $\pmb{b}$ | $\pmb{c}$ |
> |---|---|---|---|
> | $\pmb{q_1}$ | $q_2$ | $q_3$ | $q_4$ |
> | $\pmb{q_2}$ | $q_2$ | $q_4$ | $q_5$ |
> | $\pmb{q_3}$ | $q_4$ | $q_3$ | $q_5$ |
> | $\pmb{q_4}$ | $q_4$ | $q_4$ | $q_4$ |
> | $\pmb{q_5}$ | $q_4$ | $q_4$ | $q_5$ |

>
>
> Andiamo dunque a disegnare il diagramma di questo automa:
> Per determinare il linguaggio accettato da questo automa ci basterà ricostruire tutti i percorsi che portano da $q_1$ a $q_5$.
>
> In particolare avremo che se iniziamo con una $a$, per arrivare in $q_5$ possiamo avere un altro numero arbitrario di $a$ dal cappio in $q_2$, almeno una $c$ per raggiungere $q_5$ e poi un altro numero arbitrario di $c$ dal cappio in $q_5$.
>
> Alternativamente partendo con una $b$ avremo un numero arbitrario di $b$ dal cappio in $q_3$, almeno una $c$ per raggiungere $q_5$ e poi un altro numero arbitrario di $c$ dal cappio in $q_5$.
>
> Tutti gli altri percorsi non sono percorribili poiché passano per $q_4$ che è uno stato pozzo.
>
> Avremo dunque che il linguaggio accettato da $\mathcal{M}$ sarà $L(\mathcal{M})=\{a^{n}c^m\vert n,m >0\} \cup \{b^{n}c^m\vert n,m >0\} $.


### Automi Finiti Non Deterministici


> [!definition] Automi Finiti Non Deterministici
> Un automa finito non deterministico (NDFA o NFA) è una quintupla $\mathcal{M} = (Q,A,\delta,q_1,F)$ dove:
> - $Q$ e $A$ sono insiemi finiti;
> - $q_1 \in Q$
> - $F \subseteq Q$
> - $Q \times A \mapsto \mbP(Q)$ funzione di transizione (totale).


Avremo dunque che, partendo da un qualsiasi stato con la parola vuota assoceremo il singleton di quello stato, mentre con una parola generica $wa$ andremo ad associare l'unione di tutti gli stati raggiungibili con $a$ partendo da quelli raggiunti con $w$ da $q$.

Per dare un senso a questa definizione però è necessario identificare quali linguaggi vengono accettati da una NFA. Analogamente a come fatto per i DFA utilizziamo la funzione $\delta$ iterata.

$$
    \begin{cases}
    \delta^*(q,\varepsilon)=\{q\}, & \forall q \in Q\\
    \delta^*(q,wa)=\bigcup\limits_{q' \in \delta^*(q,w)} \delta(q', a)
    \end{cases}
$$


Possiamo infine definire $L\subseteq A^*$ come accettato da una NFA *se e solo se* $L=L(\mathcal{M}) = \{w \in A^* \vert \delta^*(q_1,w) \cap F \neq \emptyset\}$.

#### Diagramma di Transizione di stato di un NFA


Come con i DFA è possibile rappresentare i NFA utilizzando dei diagrammi di passaggi di stato. La differenza principale è che in un NFA è possibile avere più di una transizione per stato e simbolo di input, come non averne affatto.

Vediamo un esempio di NFA. Consideriamo il linguaggio $L=\{w \in \{a,b\}^* \vert w \text{ contiene } aa \text{ oppure } bb\}$.

\caption{Diagramma di Transizione di Stato di un NFA}
\end{figure}

### Equivalenza tra DFA e NFA


Nonostante i DFA e i NFA siano due modelli di automi molto diversi, e si potrebbe pensare che i linguaggi accettati da questi due modelli siano diversi e, in particolare, essendo le NFA meno stringenti e più facili da elaborare, che queste accettino più linguaggi delle DFA.

Questo non è il caso però, infatti, come vedremo, ogni linguaggio accettato da una NFA è accettato anche da una DFA e viceversa. Questo ci permette di affermare che i due modelli sono equivalenti, ovvero che accettano esattamente gli stessi linguaggi.

> [!theorem] Corrispondenza tra DFA e NFA
> **Enunciato. ** $L\subseteq A^*$ regolare $\iff L=L(\mathcal{M})$ per qualche NDFA $\mathcal{M}$.
>
>
> **Dimostrazione. ** Dimostriamo la doppia implicazione:
> - **``$\Rightarrow$''** Sia $L$ regolare. Allora $\exists \mathcal{M}'=(Q,A,\delta',q_1,F)$ DFA $: L=L(\mathcal{M}')$. Allora $L=L(\mathcal{M})$ dove $\mathcal{M}=(Q,A,\delta,q_1,F)$ è l'NFA definita da $\delta(q,a)=\{\delta'(q,a)\}$.
> - **``$\Leftarrow$''** Sia $L=L(\mathcal{M})$ con $\mathcal{M}(Q,A,\delta,q_1,F)$ NFA. Definiamo allora $\mathcal{M}'=(\mbP(Q), A, \delta', \{q_1\}, \mbF)$ dove
> - []
> $$
>     \mbF = &\{Q' \subseteq Q \vert Q' \cap F \neq \varnothing \}\\
>     \delta'(Q',a)=&\bigcup\limits_{q \in Q'} \delta(q,a) \forall Q'\subseteq Q, a \in A
> $$

>
> Si può dimostrare, anche se non lo vedremo allora che $\delta'^*(Q',w)=\bigcup\limits_{q \in Q'}\delta^*(q,w)$
>
> Allora $L(\mathcal{M})=\{w \in A^* \vert \delta'^*(\{q_1\},w) \in \mbF\} = \{w \in A^* \vert \delta^*(\{q_1\},w) \in \mbF\} = \{w \in A^* \vert \delta^*(q_1,w) \cap F \neq \varnothing\}=L(\mathcal{M})$.
>


Questa equivalenza è fondamentale poiché ci permette di trattare ogni NFA, più semplice da concepire e rappresentare, come un DFA, più semplice da implementare con una vera macchina non dovendo fare scelte arbitrarie, e viceversa.


---

[^1]:  Essendo $L\subseteq A^*$ non possiamo utilizzare la nozione di ricorsivo enumerabilità relativa ai sottoinsiemi di $\mathbb{N}$ che sfrutta il Linguaggio S, pensi quella più generale ma equivalente fornitaci dalle macchine di Turing
[^2]: Importante prestare attenzione al fatto che si parli di un implicazione singola, ergo non vale necessariamente l'opposta
[^3]: Si ricorda che per definizione una macchina di Turing presuppone che di iniziare da una cella vuota con l'input che inizia immediatamente alla sua destra.