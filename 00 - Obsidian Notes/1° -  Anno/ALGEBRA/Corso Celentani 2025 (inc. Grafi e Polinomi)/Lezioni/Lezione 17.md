# Lezione 17: Relazioni d'Ordine

**Data:** 20/05/2025 (come da note)
**Argomenti:** Relazione d'Ordine (Largo e Stretto), Corrispondenza tra Ordini, Ordine Totale/Parziale, Copertura, Diagrammi di Hasse, Elementi Minimo/Massimo, Elementi Minimali/Massimali, Insiemi Ben Ordinati, Minoranti/Maggioranti, Inf/Sup.

#tag/relations #tag/order-theory #tag/posets #tag/hasse-diagrams #tag/min-max-elements #tag/well-ordering #tag/algebra-avanzata

---

## 1. Definizione di Relazione d'Ordine

Sia $S$ un insieme non vuoto e $\mathcal{R}$ una relazione binaria su $S$.

*   **Relazione d'Ordine (Largo) (Pag 1):**
    La coppia $(S, \mathcal{R})$ è un **insieme ordinato** e $\mathcal{R}$ è una **relazione d'ordine** (o ordine parziale, ordine largo) se $\mathcal{R}$ soddisfa le seguenti tre proprietà:
    1.  **Riflessiva:** $\forall x \in S, x \mathcal{R} x$.
    2.  **Antisimmetrica:** $\forall x, y \in S, (x \mathcal{R} y \land y \mathcal{R} x) \implies x = y$.
    3.  **Transitiva:** $\forall x, y, z \in S, (x \mathcal{R} y \land y \mathcal{R} z) \implies x \mathcal{R} z$.
    *   *Notazione comune:* Spesso si usa il simbolo $\le$ (o $\preceq$) per denotare una generica relazione d'ordine largo.

*   **Relazione d'Ordine Stretto (Pag 1):**
    Una relazione $\mathcal{R}'$ su $S$ è una **relazione d'ordine stretto** se soddisfa:
    1.  **Antiriflessiva (o Irriflessiva):** $\forall x \in S, \neg (x \mathcal{R}' x)$.
    2.  **Transitiva:** $\forall x, y, z \in S, (x \mathcal{R}' y \land y \mathcal{R}' z) \implies x \mathcal{R}' z$.
    *   *Notazione comune:* Spesso si usa il simbolo $<$ (o $\prec$) per denotare una generica relazione d'ordine stretto.
    > [!NOTE] Una relazione d'ordine stretto è automaticamente asimmetrica. Se fosse $x \mathcal{R}' y$ e $y \mathcal{R}' x$, per transitività avremmo $x \mathcal{R}' x$, il che contraddice l'antiriflessività.

[[Relazione d'ordine]] [[Relazione d'ordine stretto]]

---

## 2. Corrispondenza tra Ordine Largo e Stretto (Pag 2)

Esiste una corrispondenza biunivoca tra relazioni d'ordine largo ($\mathcal{R}$) e relazioni d'ordine stretto ($\mathcal{R}'$) sullo stesso insieme $S$.

*   **Da Ordine Largo $\mathcal{R}$ a Ordine Stretto $\mathcal{R}'$:**
    $$ x \mathcal{R}' y \iff (x \mathcal{R} y \land x \neq y) $$
    *   **Spiegazione:** $x$ è strettamente minore di $y$ se $x$ è minore o uguale a $y$, ma $x$ non è uguale a $y$.

*   **Da Ordine Stretto $\mathcal{R}'$ a Ordine Largo $\mathcal{R}$:**
    $$ x \mathcal{R} y \iff (x \mathcal{R}' y \lor x = y) $$
    *   **Spiegazione:** $x$ è minore o uguale a $y$ se $x$ è strettamente minore di $y$ oppure $x$ è uguale a $y$.

### Esempio Illustrativo
Consideriamo l'insieme $S = \{a, b, c\}$ e una relazione d'ordine largo $\mathcal{R}$ su $S$ definita come:
$$\mathcal{R} = \{(a, a), (b, b), (c, c), (a, b), (a, c), (b, c)\}$$

- **Passaggio a Ordine Stretto $\mathcal{R}'$:**
  $$\mathcal{R}' = \{(a, b), (a, c), (b, c)\}$$
  Nota che le coppie $(a, a)$, $(b, b)$, $(c, c)$ sono escluse perché $x \neq y$.

- **Ritorno a Ordine Largo $\mathcal{R}$:**
  Ricostruiamo $\mathcal{R}$ da $\mathcal{R}'$:
  $$\mathcal{R} = \{(a, a), (b, b), (c, c), (a, b), (a, c), (b, c)\}$$
  La relazione originale è recuperata.

### Verifica che la costruzione funziona (Pag 7-8):
Se $\mathcal{R}'$ è un ordine stretto (antiriflessivo, transitivo) e definiamo $\mathcal{R}$ come $x \mathcal{R} y \iff (x \mathcal{R}' y \lor x = y)$, allora $\mathcal{R}$ è un ordine largo:
1.  **Riflessiva:** $x \mathcal{R} x \iff (x \mathcal{R}' x \lor x=x)$. Poiché $x=x$ è vero, $x \mathcal{R} x$ è vero.
2.  **Antisimmetrica:** Supponiamo $x \mathcal{R} y \land y \mathcal{R} x$.
    *   $x \mathcal{R} y \implies (x \mathcal{R}' y \lor x=y)$.
    *   $y \mathcal{R} x \implies (y \mathcal{R}' x \lor y=x)$.
    *   Se $x \neq y$: allora deve essere $x \mathcal{R}' y$ e $y \mathcal{R}' x$. Ma questo contraddice l'asimmetria (e quindi l'antiriflessività) di $\mathcal{R}'$.
    *   Quindi, l'unica possibilità è $x=y$.
3.  **Transitiva:** Supponiamo $x \mathcal{R} y \land y \mathcal{R} z$. Dobbiamo mostrare $x \mathcal{R} z$.
    *   Analizziamo i 4 casi possibili dalle definizioni:
        *   (i) $x=y \land y=z \implies x=z \implies x \mathcal{R} z$.
        *   (ii) $x=y \land y \mathcal{R}' z \implies x \mathcal{R}' z \implies x \mathcal{R} z$.
        *   (iii) $x \mathcal{R}' y \land y=z \implies x \mathcal{R}' z \implies x \mathcal{R} z$.
        *   (iv) $x \mathcal{R}' y \land y \mathcal{R}' z \implies x \mathcal{R}' z$ (per transitività di $\mathcal{R}'$) $\implies x \mathcal{R} z$.
    *   In tutti i casi, $x \mathcal{R} z$.

---

## 3. Ordine Totale vs. Ordine Parziale (Pag 2)

Sia $(S, \mathcal{R})$ un insieme ordinato (con ordine largo).
*   L'ordine $\mathcal{R}$ è **totale** (o lineare) se per ogni coppia di elementi $x, y \in S$, vale sempre che $x \mathcal{R} y$ oppure $y \mathcal{R} x$.
    $$ \forall x, y \in S, \quad (x \mathcal{R} y \lor y \mathcal{R} x) $$
    *   **Spiegazione:** Ogni coppia di elementi è confrontabile.
*   Se un ordine non è totale, è detto **parziale**.

*   **Esempi:**
    *   $(\mathbb{N}, \le)$ con l'usuale "minore o uguale" è un **ordine totale**.
    *   $(\mathbb{Z}, \le)$, $(\mathbb{Q}, \le)$, $(\mathbb{R}, \le)$ sono ordini totali.
    *   $(P(S), \subseteq)$ (insieme delle parti di $S$ con l'inclusione insiemistica), se $|S| \ge 2$, è un **ordine parziale** (non totale).
        *   Esempio (Pag 3): $S=\{a, b\}$. $P(S) = \{\emptyset, \{a\}, \{b\}, S\}$.
        *   $\{a\} \not\subseteq \{b\}$ e $\{b\} \not\subseteq \{a\}$. I due elementi $\{a\}$ e $\{b\}$ non sono confrontabili.

[[Ordine totale]] [[Ordine parziale]]

---

## 4. Copertura e Diagrammi di Hasse

Per visualizzare insiemi parzialmente ordinati finiti.

*   **Copertura (Pag 3):** Sia $(S, \mathcal{R})$ un insieme ordinato. Diciamo che $b$ **copre** $a$ (o $a$ è coperto da $b$) se $a \mathcal{R}' b$ (cioè $a \mathcal{R} b$ e $a \neq b$) e non esiste nessun elemento $c \in S$ tale che $a \mathcal{R}' c$ e $c \mathcal{R}' b$.
    $$ b \text{ copre } a \iff (a \mathcal{R}' b \land \neg (\exists c \in S : a \mathcal{R}' c \land c \mathcal{R}' b)) $$
    *   **Spiegazione:** $b$ è "immediatamente sopra" ad $a$ nell'ordine, senza elementi intermedi.

*   **Diagramma di Hasse (Pag 4):** Una rappresentazione grafica di un insieme finito parzialmente ordinato $(S, \mathcal{R})$.
    1.  I vertici del diagramma sono gli elementi di $S$.
    2.  Se $b$ copre $a$, si disegna un segmento da $a$ a $b$, con $b$ posizionato più in alto di $a$.
    3.  Non si disegnano:
        *   Loop (per riflessività, implicita).
        *   Archi che possono essere dedotti per transitività (es. se $c$ copre $b$ e $b$ copre $a$, non si disegna un arco diretto da $a$ a $c$).
        *   Frecce (la direzione "verso l'alto" è implicita).

*   **Esempi di Diagrammi di Hasse:**
    *   **$(P(S), \subseteq)$ con $S=\{a, b\}$ (Pag 4):**
        *   $P(S) = \{\emptyset, \{a\}, \{b\}, S\}$.
        *   Coperture: $S$ copre $\{a\}$ e $\{b\}$. $\{a\}$ copre $\emptyset$. $\{b\}$ copre $\emptyset$.
        *   ```mermaid
            graph TD
                S["S={a,b}"] --> A["{a}"]
                S --> B["{b}"]
                A --> E["∅"]
                B --> E
            ```
    *   **$(P(S), \subseteq)$ con $S=\{a, b, c\}$ (Pag 4):**
        *   ```mermaid
            graph TD
                S["{a,b,c}"] --> AB["{a,b}"]
                S --> AC["{a,c}"]
                S --> BC["{b,c}"]
                AB --> A["{a}"]
                AB --> B["{b}"]
                AC --> A
                AC --> C["{c}"]
                BC --> B
                BC --> C
                A --> E["∅"]
                B --> E
                C --> E
            ```
    *   **$(P(S), \mathcal{R})$ con $S=\{a,b,c\}$ e $X \mathcal{R} Y \iff (X=Y) \lor (|X| < |Y|)$ (Pag 5):**
        *   Questo è un ordine per livelli basato sulla cardinalità. Un insieme $Y$ copre un insieme $X$ se $|Y| = |X| + 1$.
        *   Ecco il diagramma di Hasse che rappresenta questa relazione di copertura:
            ```mermaid
            graph BT
              E["∅"]
              A["{a}"]
              B["{b}"]
              C["{c}"]
              AB["{a, b}"]
              AC["{a, c}"]
              BC["{b, c}"]
              ABC["{a, b, c}"]

              E --> A
              E --> B
              E --> C

              A --> AB
              A --> AC
              A --> BC

              B --> AB
              B --> AC
              B --> BC

              C --> AB
              C --> AC
              C --> BC

              AB --> ABC
              AC --> ABC
              BC --> ABC
            ```
        *   **Spiegazione del Diagramma:** Gli elementi sono disposti verticalmente in base alla loro cardinalità (dal basso verso l'alto). Una freccia da $X$ a $Y$ indica che $Y$ copre $X$, il che per questa relazione significa che $|Y| = |X| + 1$. Ad esempio, da $\{a\}$ (cardinalità 1) ci sono frecce verso tutti gli insiemi di cardinalità 2 ($\{a,b\}, \{a,c\}, \{b,c\}$), perché tutti questi insiemi hanno cardinalità 2 e non esiste un insieme $Z$ con cardinalità strettamente compresa tra 1 e 2.
    *   **$(\{2,3,4,5,6,8,10\}, \mathcal{R})$ con $a \mathcal{R} b \iff (a=b) \lor (\pi(a) \subset \pi(b))$, dove $\pi(n)$ è l'insieme dei divisori primi di $n$ (Pag 6):**
        *   $\pi(2)=\{2\}$, $\pi(3)=\{3\}$, $\pi(4)=\{2\}$, $\pi(5)=\{5\}$, $\pi(6)=\{2,3\}$, $\pi(8)=\{2\}$, $\pi(10)=\{2,5\}$.
        *   La relazione d'ordine è basata sull'inclusione stretta tra gli insiemi dei divisori primi. Un elemento $b$ copre $a$ se $\pi(a) \subset \pi(b)$ e non esiste $c$ tale che $\pi(a) \subset \pi(c) \subset \pi(b)$.
        *   Ecco il diagramma di Hasse per questo insieme e questa relazione:
            ```mermaid
            graph BT
              2 & 4 & 8 --> 6
              2 & 4 & 8--> 10
              3 --> 6
              5 --> 10
            ```
        *   **Spiegazione del Diagramma:** Gli elementi minimali (quelli i cui insiemi di divisori primi non contengono strettamente altri insiemi dell'insieme) sono 2, 3, 4, 5, 8 e sono posizionati in basso. Gli elementi massimali (quelli i cui insiemi di divisori primi non sono contenuti strettamente in altri insiemi dell'insieme) sono 6 e 10 e sono posizionati in alto. Le frecce indicano le relazioni di copertura: ad esempio, 6 copre 2, 3, 4, e 8 perché i loro insiemi di divisori primi sono strettamente contenuti in $\pi(6)=\{2,3\}$ e non c'è nessun altro elemento $c$ nell'insieme con un $\pi(c)$ "intermedio".

[[Diagramma di Hasse]]

---

## 5. Elementi Speciali in Insiemi Ordinati

Sia $(S, \le)$ un insieme parzialmente ordinato.

*   **Elemento Minimo (Pag 11):** $a \in S$ è **minimo** di $S$ se $a \le x$ per ogni $x \in S$.
    *   Se esiste, l'elemento minimo è **unico**.
    *   **Dimostrazione unicità:** Se $m_1, m_2$ sono minimi, allora $m_1 \le m_2$ (perché $m_1$ è minimo) e $m_2 \le m_1$ (perché $m_2$ è minimo). Per antisimmetria, $m_1 = m_2$.
*   **Elemento Massimo (Pag 11):** $a \in S$ è **massimo** di $S$ se $x \le a$ per ogni $x \in S$.
    *   Se esiste, l'elemento massimo è **unico**.

*   **Esempi:**
    *   $(P(S), \subseteq)$: $\min(P(S)) = \emptyset$, $\max(P(S)) = S$.
    *   $(\mathbb{N}, \le)$: $\min(\mathbb{N}) = 0$. Non esiste $\max(\mathbb{N})$.
    *   $(\mathbb{N}, \mid)$ (divisibilità su $\mathbb{N}=\{1,2,...\})$: $\min(\mathbb{N}, \mid) = 1$. $\max(\mathbb{N}, \mid)$ non esiste (ma $0$ se si include in $\mathbb{N}_0$ sarebbe il massimo, $x|0$ per ogni $x$).
    *   $(\mathbb{N} \setminus \{1\}, \mid)$: Non esiste minimo (es. 2 e 3 sono incomparabili e non dividono tutti gli altri). Non esiste massimo.

*   **Elemento Minimale (Pag 14):** $a \in S$ è **minimale** se non esiste alcun $x \in S$ tale che $x < a$ (cioè $x \le a \land x \neq a$).
    *   Equivalentemente: $\forall x \in S, x \le a \implies x = a$.
*   **Elemento Massimale (Pag 16):** $a \in S$ è **massimale** se non esiste alcun $x \in S$ tale che $a < x$.
    *   Equivalentemente: $\forall x \in S, a \le x \implies x = a$.

*   **Relazioni tra Minimo/Massimo e Minimale/Massimale (Pag 16-17):**
    *   Se $a$ è minimo, allora $a$ è l'**unico** elemento minimale.
    *   Se $a$ è massimo, allora $a$ è l'**unico** elemento massimale.
    *   Un elemento minimale (o massimale) **non è necessariamente unico**.
    *   Se esiste un elemento minimale unico, **non è detto** che sia il minimo dell'insieme (a meno che l'ordine non sia totale).

*   **Esempi:**
    *   $(\mathbb{N} \setminus \{1\}, \mid)$: Gli elementi minimali sono tutti i numeri primi. Non c'è un minimo.
    *   $(P(S) \setminus \{\emptyset\}, \subseteq)$: Gli elementi minimali sono i singleton $\{s\}$ per ogni $s \in S$.

*   **Teorema (Pag 18):** Ogni insieme finito non vuoto parzialmente ordinato possiede almeno un elemento minimale e almeno un elemento massimale.
*   **Controesempio per insiemi infiniti (Pag 18):** $(\mathbb{Z}, \le)$ non ha né minimali né massimali.

[[Elemento minimale e massimale]] [[Elemento minimo e massimo]]

---

## 6. Insiemi Ben Ordinati e Operazioni su Insiemi Ordinati

*   **Insieme Ben Ordinato (Pag 21):** Un insieme parzialmente ordinato $(S, \le)$ è **ben ordinato** se ogni suo sottoinsieme non vuoto $X \subseteq S$ ammette un elemento **minimo**.
    *   Un insieme ben ordinato è **sempre totalmente ordinato**. (Se non fosse totale, esisterebbero $a,b$ non confrontabili. Allora il sottoinsieme $\{a,b\}$ non avrebbe minimo).
    *   Esempio: $(\mathbb{N}, \le)$ è ben ordinato (Principio del Buon Ordinamento).
    *   Controesempio: $(\mathbb{Z}, \le)$ non è ben ordinato (es. $\mathbb{Z}$ stesso non ha minimo). $(\mathbb{R}_{\ge 0}, \le)$ non è ben ordinato (es. $(0, 1)$ non ha minimo).

[[Buon ordinamento]]

*   **Minoranti e Maggioranti (Pag 22):** Sia $(S, \le)$ un insieme ordinato e $X \subseteq S$ un sottoinsieme.
    *   $a \in S$ è un **minorante** di $X$ se $a \le x$ per ogni $x \in X$.
    *   $a \in S$ è un **maggiorante** di $X$ se $x \le a$ per ogni $x \in X$.
    *   Se un minorante $a$ di $X$ appartiene anche a $X$, allora $a = \min(X)$.

*   **Estremo Inferiore (Infimum) e Superiore (Supremum) (Pag 23):**
    *   $\inf(X) = \max(\text{insieme dei minoranti di } X)$, se esiste. (Il più grande dei minoranti).
    *   $\sup(X) = \min(\text{insieme dei maggioranti di } X)$, se esiste. (Il più piccolo dei maggioranti).
    *   Se $\min(X)$ esiste, allora $\inf(X)=\min(X)$. Se $\max(X)$ esiste, allora $\sup(X)=\max(X)$.
    *   **Esempio $(\mathbb{N}, \mid)$:** $X=\{60, 54\}$.
        *   $60 = 2^2 \cdot 3 \cdot 5$. $54 = 2 \cdot 3^3$.
        *   Minoranti (divisori comuni): $\{1, 2, 3, 6\}$.
        *   $\inf(\{60, 54\}) = \max(\{1,2,3,6\}) = 6 = \text{MCD}(60, 54)$.
        *   Maggioranti (multipli comuni): $\{2^2 \cdot 3^3 \cdot 5 \cdot k \mid k \in \mathbb{N}^*\} = \{540, 1080, ...\}$.
        *   $\sup(\{60, 54\}) = \min(\{540, 1080, ...\}) = 540 = \text{mcm}(60, 54)$.

[[Minorante e maggiorante]] [[Estremo superiore e inferiore]]

---

## 7. Esercizi Proposti

> [!EXERCISE] Esercizio 1 (Pag 24 - Ordine tramite Funzione)
> Siano $(S, \le_S)$ e $(T, \le_T)$ insiemi ordinati, e $f: S \to T$ una funzione.
> Definiamo una relazione $\le_f$ su $S$ come:
> $$ a \le_f b \iff (a=b) \lor (f(a) <_T f(b)) $$
> (dove $<_T$ è l'ordine stretto associato a $\le_T$).
> Verificare se $\le_f$ è una relazione d'ordine su $S$.
>
> **Casi specifici da analizzare (Pag 24-28):**
> 1.  $S = \mathbb{N} \times \mathbb{N}$, $T = (\mathbb{N}, \le)$, $f(a,b) = a+b$.
>     Determinare $\vec{f}(\mathbb{N} \times \mathbb{N})$, $\min(\vec{f}(\mathbb{N} \times \mathbb{N}))$.
>     Determinare $\overleftarrow{f}(\{0\})$, $\overleftarrow{f}(\{1\})$.
> 2.  $S = \mathbb{N} \times \mathbb{N}$, $T = (\mathbb{N}, \mid)$ (divisibilità, $\mathbb{N}=\{0,1,2,...\}$), $f(a,b) = a \cdot b$.
>     Determinare $\vec{f}(\mathbb{N} \times \mathbb{N})$, $\min(\vec{f}(\mathbb{N} \times \mathbb{N}))$, $\max(\vec{f}(\mathbb{N} \times \mathbb{N}))$.
>     Determinare $\overleftarrow{f}(\{1\})$, $\overleftarrow{f}(\{0\})$ (se $0 \in T$).
> 3.  $S = \mathbb{N}^* \times \mathbb{N}^*$, $T = (\mathbb{N}, \le)$, $f(a,b) = a^b$.
>     Determinare $\vec{f}(\mathbb{N}^* \times \mathbb{N}^*)$, $\min(\vec{f}(\mathbb{N}^* \times \mathbb{N}^*))$.
>     Determinare $\overleftarrow{f}(\{1\})$.
> 4.  $S_{10}$ un insieme con $|S_{10}|=10$. $S = P(S_{10})$, $T = (\mathbb{N}, \mid)$, $f(X) = |X|$.
>     Determinare $\vec{f}(P(S_{10}))$.
>     Disegnare il diagramma di Hasse di $(P(S_{10}), \mid_f)$ (dove $\mid_f$ è l'ordine indotto da $f$ e dalla divisibilità su $\mathbb{N}$).
> 5.  $S = \mathbb{Z}$, $T = (\mathbb{Z}, \le)$, $f(a) = 2^{|a|}$.
>     Determinare $\vec{f}(\mathbb{Z})$, $\min(\vec{f}(\mathbb{Z}))$.
>     Determinare $\overleftarrow{f}(\{1\})$.

> [!EXERCISE] Esercizio 2 (Pag 30 - DA FARE)
> Sia $(P(S), \mathcal{R})$ con $S=\{a,b,c\}$ e $X \mathcal{R} Y \iff (X=Y) \lor (|X| < |Y|)$.
> Trovare gli elementi minimali e massimali di $P(S) \setminus \{\{a,b\}, \{a,c\}\}$.
> Disegnare il diagramma di Hasse di questo sottoinsieme ordinato.

---

> [!SUMMARY] Riepilogo Veloce Lezione 17
> *   Abbiamo definito le **relazioni d'ordine largo** (riflessiva, antisimmetrica, transitiva) e **stretto** (antiriflessiva, transitiva) e la loro corrispondenza.
> *   Un ordine è **totale** se tutti gli elementi sono confrontabili, altrimenti è **parziale**.
> *   I **Diagrammi di Hasse** visualizzano ordini finiti mostrando solo le relazioni di copertura.
> *   Abbiamo distinto tra elementi **minimo/massimo** (unici, se esistono) ed elementi **minimali/massimali** (possono essere multipli).
> *   Un insieme è **ben ordinato** se ogni suo sottoinsieme non vuoto ha un minimo (implica ordine totale).
> *   Abbiamo definito **minoranti, maggioranti, infimum (MCD generalizzato) e supremum (mcm generalizzato)**.

> [!TIP] Prossimi Passi
> *   Svolgi gli esercizi proposti per familiarizzare con i diversi tipi di ordine e gli elementi speciali.
> *   Le relazioni d'ordine sono fondamentali per strutture come i reticoli e le algebre di Boole.
> *   Le relazioni di equivalenza (che vedremo) sono l'altro tipo principale di relazione con proprietà strutturali importanti.}