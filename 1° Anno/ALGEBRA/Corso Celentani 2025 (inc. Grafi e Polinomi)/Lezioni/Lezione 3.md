# Lezione 3: Logica, Funzioni (Iniettività, Suriettività, Immagine/Controimmagine), Restrizioni

**Data:** 18/03/2025 (come da note)
**Argomenti:** Negazione formule logiche, Verifica tautologie, Proprietà immagine/controimmagine, Funzioni iniettive (recap), Funzioni suriettive, Funzione caratteristica, Uguaglianza funzioni, Restrizione e Prolungamento.

#tag/logica #tag/logica-predicati #tag/functions #tag/injectivity #tag/surjectivity #tag/settheory #tag/algebra-avanzata

---

## 1. Esercizi e Approfondimenti di Logica

Vediamo come negare formule più complesse e analizziamo qualche altra tautologia.

*   **Negazione dell'Implicazione:** Ricordiamo che $p \implies q \iff \neg p \lor q$.
    *   Quindi, $\neg (p \implies q) \iff \neg (\neg p \lor q)$.
    *   Applicando De Morgan: $\neg (\neg p \lor q) \iff (\neg (\neg p) \land \neg q)$.
    *   Applicando la doppia negazione: $(\neg (\neg p) \land \neg q) \iff (p \land \neg q)$.
    > [!IMPORTANT] Regola di Negazione dell'Implicazione:
    > $$ \neg (p \implies q) \iff p \land \neg q $$
    > **Spiegazione:** Negare "Se piove allora prendo l'ombrello" significa affermare che "Piove E non prendo l'ombrello". È l'unico caso che rende falsa l'implicazione originale.
    *   [[Negazione Implicazione]]

*   **Esercizio 2 (Pag 1):** L'equivalenza $p \implies (q \lor r) \iff ((p \implies q) \lor (p \implies r))$ è una tautologia?
    *   Proviamo a usare le equivalenze:
        *   Lato sinistro: $p \implies (q \lor r) \iff \neg p \lor (q \lor r)$
        *   Lato destro: $(p \implies q) \lor (p \implies r) \iff (\neg p \lor q) \lor (\neg p \lor r)$
        *   Usando associatività e idempotenza della $\lor$: $(\neg p \lor q) \lor (\neg p \lor r) \iff \neg p \lor q \lor \neg p \lor r \iff \neg p \lor q \lor r$
    *   Confrontiamo i risultati: $\neg p \lor (q \lor r)$ è effettivamente equivalente a $\neg p \lor q \lor r$.
    *   **Risposta: SÌ, è una tautologia.** Significa che "Se P implica (Q o R)" è la stessa cosa di "(Se P implica Q) o (Se P implica R)".
    *   [[Distributività Implicazione su Disgiunzione]]

*   **Esercizio 3 (Pag 1):** Negare $p \implies (q \lor r)$.
    *   Usando la regola $\neg(A \implies B) \iff A \land \neg B$:
    *   $\neg (p \implies (q \lor r)) \iff p \land \neg (q \lor r)$
    *   Applicando De Morgan a $\neg(q \lor r)$:
    *   $p \land (\neg q \land \neg r)$

*   **Esercizio 4 (Pag 1):** Negare $p \implies (q \land r)$.
    *   $\neg (p \implies (q \land r)) \iff p \land \neg (q \land r)$
    *   Applicando De Morgan:
    *   $p \land (\neg q \lor \neg r)$

*   **Esercizio 5 (Pag 1):** Negare $(p \lor q) \implies r$.
    *   $\neg ((p \lor q) \implies r) \iff (p \lor q) \land \neg r$

*   **Esercizio 6 (Pag 1):** Negare $(p \land q) \implies r$.
    *   $\neg ((p \land q) \implies r) \iff (p \land q) \land \neg r$

*   **Esercizio 7 (Pag 1):** Negare $\forall x (\exists y (\varphi(x,y) \implies \psi(x,y)))$.
    *   Applichiamo le regole di negazione passo passo, dall'esterno verso l'interno:
    1.  $\neg [\forall x (\dots)]$ $\iff \exists x \neg [(\dots)]$
        *   $\exists x \neg (\exists y (\varphi(x,y) \implies \psi(x,y)))$
    2.  $\neg [\exists y (\dots)]$ $\iff \forall y \neg [(\dots)]$
        *   $\exists x (\forall y \neg (\varphi(x,y) \implies \psi(x,y)))$
    3.  $\neg [A \implies B]$ $\iff A \land \neg B$
        *   $\exists x (\forall y (\varphi(x,y) \land \neg \psi(x,y)))$
    *   **Risultato:** $\exists x \forall y (\varphi(x,y) \land \neg \psi(x,y))$

*   **Esercizio 8 (Pag 1):** L'equivalenza $((p \implies q) \implies (q \implies r \land s)) \iff ((\neg q) \lor (r \land s))$ è una tautologia?
    *   Analizziamo il lato sinistro: $(p \implies q) \implies (q \implies (r \land s))$
    *   Questo **NON** sembra una tautologia standard o facilmente riconducibile. Potrebbe essere un errore di trascrizione o un'affermazione da verificare con una tavola di verità (che sarebbe molto lunga!). Sembra improbabile che sia una tautologia generale senza ulteriori condizioni su p, q, r, s. La nota "è tautologia?" suggerisce che sia una domanda, non un'affermazione.
    > [!QUESTION] Verifica: Questa equivalenza è corretta o era una domanda da verificare? A prima vista non sembra una tautologia standard.

---

## 2. Funzioni: Chiarimenti e Proprietà

### 2.1 Errore Comune sull'Iniettività (Pag 2)

> [!WARNING] Attenzione a non confondere la definizione di funzione con quella di iniettività!
> *   Per **definizione di funzione**, se prendi lo stesso input $x$, otterrai sempre lo stesso output $f(x)$. Quindi, l'implicazione $x = y \implies f(x) = f(y)$ è **SEMPRE VERA** per qualsiasi funzione.
> *   La **definizione di iniettività** richiede l'implicazione inversa: $f(x) = f(y) \implies x = y$. Questo **NON** è vero per tutte le funzioni, ma solo per quelle iniettive.

### 2.2 Proprietà dell'Immagine $\vec{f}(X)$ (Pag 3)

Sia $f: A \to B$ una funzione e $X \subseteq A$.
*   $\vec{f}(\emptyset) = \emptyset$. (L'immagine del vuoto è vuota).
*   Se $X \neq \emptyset$, è possibile che $\vec{f}(X) \neq \emptyset$? **Sì, sempre!** Se $X$ contiene almeno un elemento $x$, allora $\vec{f}(X)$ contiene almeno $f(x)$, quindi non è vuoto.
    > [!NOTE] La nota $\vec{f}(X) \neq \emptyset$ nella pagina 3 sembra ridondante se $X \neq \emptyset$. Forse si intendeva qualcos'altro?
*   $\vec{f}(A)$ è l'**immagine dell'intera funzione**, spesso denotata $Im(f)$.
*   In generale, $\vec{f}(A) \subseteq B$.
*   $\vec{f}(A) = B$ se e solo se $f$ è **suriettiva**. (Lo vedremo meglio tra poco).

### 2.3 Proprietà della Controimmagine $\overleftarrow{f}(Y)$ (Pag 4)

Sia $f: A \to B$ una funzione e $Y \subseteq B$.
*   $\overleftarrow{f}(\emptyset) = \emptyset$. (Gli input la cui immagine è nel vuoto... non esistono!).
*   È possibile che $\overleftarrow{f}(Y) = \emptyset$ anche se $Y \neq \emptyset$? **SÌ**.
    *   Questo accade se nessun elemento di $Y$ viene "raggiunto" dalla funzione, cioè se $Y$ è disgiunto dall'immagine della funzione ($Y \cap Im(f) = \emptyset$).
    *   Esempio: $f(x)=|x|$ da $\mathbb{Z}$ a $\mathbb{Z}$. $\overleftarrow{f}(\{-1, -2\}) = \emptyset$ perché nessun intero ha valore assoluto negativo.
*   La nota "solo se è suriettiva" (Pag 4) riferita a $\overleftarrow{f}(Y) \neq \emptyset$ se $Y \neq \emptyset$ **non è corretta** in generale. È vero il contrario per la *suriettività*: $f$ è suriettiva se e solo se $\overleftarrow{f}(\{b\}) \neq \emptyset$ per ogni *singleton* $\{b\}$ con $b \in B$.

### 2.4 Iniettività e Controimmagine (Recap) (Pag 5)

Come visto nella Lezione 2, una caratterizzazione molto utile:
*   $f: A \to B$ è **iniettiva** $\iff$ per ogni $b \in B$, l'insieme $\overleftarrow{f}(\{b\})$ (la controimmagine del singolo elemento $b$) contiene **al massimo un elemento** (cioè è vuoto o è un singleton).

---

## 3. Funzioni Suriettive (Onto)

Un'altra proprietà fondamentale delle funzioni.

*   **Definizione Intuitiva:** Una funzione è **suriettiva** se ogni elemento del codominio $B$ viene "raggiunto" da almeno un elemento del dominio $A$. L'immagine della funzione coincide con l'intero codominio.
*   **Definizione Formale:** Una funzione $f: A \to B$ è suriettiva se:
    $$
    \forall b \in B, \exists a \in A \text{ tale che } f(a) = b
    $$
    *   **Spiegazione:** Per ogni possibile output $b$ nel codominio, devi essere in grado di trovare almeno un input $a$ nel dominio che produce quell'output.

*   **Caratterizzazioni Equivalenti (Pag 25-26):**
    1.  Tramite Immagine: $f$ è suriettiva $\iff \vec{f}(A) = B$. (L'immagine dell'intero dominio coincide con l'intero codominio).
    2.  Tramite Controimmagine di Singleton: $f$ è suriettiva $\iff \forall b \in B, \overleftarrow{f}(\{b\}) \neq \emptyset$. (La controimmagine di ogni singolo elemento del codominio non è mai vuota).
    3.  Tramite Controimmagine di Sottoinsiemi Non Vuoti: $f$ è suriettiva $\iff \forall C \subseteq B \text{ con } C \neq \emptyset, \text{ si ha } \overleftarrow{f}(C) \neq \emptyset$. (Se prendi un qualsiasi sottoinsieme non vuoto del codominio, ci deve essere almeno un elemento nel dominio la cui immagine cade in quel sottoinsieme).

> [!TIP] Per dimostrare che $f$ è suriettiva, prendi un generico $b \in B$ e dimostra che esiste un $a \in A$ (spesso trovando una formula per $a$ in termini di $b$) tale che $f(a)=b$.
> Per dimostrare che $f$ NON è suriettiva, trova uno specifico $b \in B$ per cui non esiste nessun $a \in A$ tale che $f(a)=b$.

[[Funzione Suriettiva]]

---

## 4. Esercizi su Iniettività e Suriettività

Analizziamo gli esempi dalle note.

*   **Esempio 1 (Pag 5-8):** $S=\{a, \{a\}, b\}$. $P(S) = \{\emptyset, \{a\}, \{\{a\}\}, \{b\}, \{a,\{a\}\}, \{a,b\}, \{\{a\},b\}, S\}$.
    $f: P(S) \times P(S) \to \{0, 1, ..., 6\}$ definita da $f(X, Y) = |X \Delta Y|$.
    *   **Iniettiva? NO.** (Come mostrato a Pag 6).
        *   Sia $X_1 = \{a\}$, $Y_1 = \{b\}$. $X_1 \Delta Y_1 = (X_1 \setminus Y_1) \cup (Y_1 \setminus X_1) = \{a\} \cup \{b\} = \{a, b\}$. $|X_1 \Delta Y_1| = 2$.
        *   Sia $X_2 = \{b\}$, $Y_2 = \{a\}$. $X_2 \Delta Y_2 = \{b\} \cup \{a\} = \{a, b\}$. $|X_2 \Delta Y_2| = 2$.
        *   Abbiamo $(X_1, Y_1) \neq (X_2, Y_2)$ ma $f(X_1, Y_1) = f(X_2, Y_2) = 2$.
        *   La nota a Pag 6 mostra $f(\{ \{a\} \}, \{b\}) = f(\{b\}, \{ \{a\} \})$. Calcoliamo:
            *   $\{ \{a\} \} \Delta \{b\} = \{ \{a\}, b \}$. Cardinalità 2.
            *   $\{b\} \Delta \{ \{a\} \} = \{ b, \{a\} \}$. Cardinalità 2.
            *   Quindi $f(\{ \{a\} \}, \{b\}) = f(\{b\}, \{ \{a\} \}) = 2$. Conferma la non iniettività.
    *   **Suriettiva? NO.** (Come mostrato a Pag 7).
        *   Il codominio è $\{0, 1, 2, 3, 4, 5, 6\}$. L'insieme $S$ ha 3 elementi. La cardinalità massima di un sottoinsieme di $S$ è 3. La cardinalità massima di $X \Delta Y = (X \cup Y) \setminus (X \cap Y)$ è $|X \cup Y|$, che è al massimo $|S|=3$.
        *   Quindi $|X \Delta Y|$ può valere al massimo 3. Non potrà mai valere 4, 5, o 6.
        *   Ad esempio, non esiste nessuna coppia $(X, Y)$ tale che $f(X, Y) = 4$.
        *   La controimmagine $\overleftarrow{f}(\{4\})$ è $\emptyset$. Poiché esiste un elemento del codominio (4) con controimmagine vuota, la funzione non è suriettiva.

*   **Esempio 2 (Pag 9-10): Funzione Caratteristica**
    Sia $S \neq \emptyset$ e $A \subseteq S$. La **funzione caratteristica** di $A$ in $S$ è:
    $$ \chi_A: S \to \{0, 1\} $$
    $$ \chi_A(x) = \begin{cases} 1 & \text{se } x \in A \\ 0 & \text{se } x \notin A \text{ (cioè } x \in S \setminus A \text{)} \end{cases} $$
    *   **Iniettiva?** Dipende. È iniettiva solo se $S$ ha al massimo un elemento. Se $S$ ha due elementi $s_1, s_2$ e $A=\{s_1\}$, allora $\chi_A(s_1)=1$, $\chi_A(s_2)=0$. Se $A=S$, $\chi_A(s_1)=\chi_A(s_2)=1$ (non iniettiva se $|S|>1$). Se $A=\emptyset$, $\chi_A(s_1)=\chi_A(s_2)=0$ (non iniettiva se $|S|>1$).
    *   **Suriettiva?** È suriettiva se e solo se esistono elementi sia dentro $A$ sia fuori $A$. Cioè, se $A \neq \emptyset$ AND $A \neq S$.
        *   Se $A=\emptyset$, l'immagine è solo $\{0\}$. Non suriettiva (su $\{0,1\}$).
        *   Se $A=S$, l'immagine è solo $\{1\}$. Non suriettiva (su $\{0,1\}$).
        *   Se $\emptyset \subset A \subset S$, allora esistono $x \in A$ (quindi $\chi_A(x)=1$) ed esistono $y \notin A$ (quindi $\chi_A(y)=0$). L'immagine è $\{0, 1\}$, quindi è suriettiva.
    *   **Controimmagini:**
        *   $\overleftarrow{\chi_A}(\{1\}) = \{ x \in S \mid \chi_A(x) = 1 \} = A$.
        *   $\overleftarrow{\chi_A}(\{0\}) = \{ x \in S \mid \chi_A(x) = 0 \} = S \setminus A$. (Complementare di A in S).
        *   $\overleftarrow{\chi_A}(\{0, 1\}) = S$.
        *   $\overleftarrow{\chi_A}(\emptyset) = \emptyset$.
    *   [[Funzione Caratteristica]]

*   **Esempio 3 (Pag 11-12):** $f: \mathbb{N}^* \times \mathbb{N}^* \to \mathbb{N}^*$ definita da $f(n, m) = n^m$. (Qui $\mathbb{N}^* = \{1, 2, 3, ...\}$).
    *   **Iniettiva? NO.**
        *   Controesempio: $f(2, 4) = 2^4 = 16$. $f(4, 2) = 4^2 = 16$.
        *   Abbiamo $(2, 4) \neq (4, 2)$ ma $f(2, 4) = f(4, 2) = 16$.
    *   **Suriettiva?** Dobbiamo chiederci: per ogni $a \in \mathbb{N}^*$, esistono $n, m \in \mathbb{N}^*$ tali che $n^m = a$?
        *   **SÌ**. Per ogni $a \in \mathbb{N}^*$, possiamo sempre scegliere $n=a$ e $m=1$. Entrambi sono in $\mathbb{N}^*$. Allora $f(a, 1) = a^1 = a$.
        *   Quindi ogni elemento $a$ del codominio ha almeno una controimmagine (la coppia $(a, 1)$). La funzione è suriettiva.

*   **Esempio 4 (Pag 13-15):** $S=\{a, b, c\}$. $f: P(S) \times P(S) \to P(S)$ definita da $f(X, Y) = X \setminus Y$.
    *   **Iniettiva? NO.**
        *   Controesempio (dalle note): $f(\{a\}, \{a\}) = \{a\} \setminus \{a\} = \emptyset$. $f(\{b\}, \{b\}) = \{b\} \setminus \{b\} = \emptyset$.
        *   Abbiamo $(\{a\}, \{a\}) \neq (\{b\}, \{b\})$ ma $f(\{a\}, \{a\}) = f(\{b\}, \{b\}) = \emptyset$.
    *   **Suriettiva? SÌ.**
        *   Dobbiamo dimostrare che per ogni $Z \in P(S)$ (cioè per ogni $Z \subseteq S$), esistono $X, Y \in P(S)$ tali che $X \setminus Y = Z$.
        *   Possiamo sempre scegliere $X=Z$ e $Y=\emptyset$. Entrambi sono sottoinsiemi di $S$ (appartengono a $P(S)$).
        *   Allora $f(Z, \emptyset) = Z \setminus \emptyset = Z$.
        *   Quindi ogni elemento $Z$ del codominio ha almeno una controimmagine (la coppia $(Z, \emptyset)$). La funzione è suriettiva.
    *   **Proprietà $X \setminus Y = \emptyset \iff X \subseteq Y$ (Pag 15):**
        *   ($\implies$) Se $X \setminus Y = \emptyset$, significa $\{x \in X \mid x \notin Y\} = \emptyset$. Questo vuol dire che non esiste nessun elemento $x$ che sta in $X$ ma non in $Y$. Quindi, ogni elemento di $X$ deve stare anche in $Y$. Cioè $X \subseteq Y$.
        *   ($\impliedby$) Se $X \subseteq Y$, allora ogni elemento $x \in X$ è anche in $Y$. Quindi non ci sono elementi $x$ tali che ($x \in X$ e $x \notin Y$). Perciò l'insieme $\{x \in X \mid x \notin Y\}$ è vuoto. Cioè $X \setminus Y = \emptyset$.

---

## 5. Uguaglianza, Restrizione, Prolungamento

### 5.1 Uguaglianza tra Funzioni (Pag 16)

Due funzioni $f$ e $g$ sono **uguali** ($f=g$) se e solo se soddisfano **tutte e tre** le seguenti condizioni:
1.  Hanno lo stesso **Dominio**.
2.  Hanno lo stesso **Codominio**.
3.  Hanno la stessa **legge (o grafo)**, cioè $f(x) = g(x)$ per ogni $x$ nel dominio comune.

*   Esempio:
    *   $f: \mathbb{N} \to \mathbb{N}$ con $f(a) = 2|a|+1$. Poiché $a \in \mathbb{N}$, $|a|=a$, quindi $f(a)=2a+1$.
    *   $g: \mathbb{Z} \to \mathbb{N}$ con $g(a) = 2|a|+1$.
    *   $h: \mathbb{Z} \to \mathbb{Z}$ con $h(a) = 2a+1$.
    *   Qui $f \neq g$ (domini diversi). $g \neq h$ (codomini diversi). $f \neq h$ (domini e codomini diversi).
    *   Anche se la "formula" sembra simile, le funzioni sono diverse perché dominio e/o codominio cambiano.

### 5.2 Restrizione di una Funzione (Pag 22)

*   Sia $f: A \to B$ una funzione e sia $C$ un sottoinsieme non vuoto del dominio ($\emptyset \neq C \subseteq A$).
*   La **restrizione di f a C**, denotata $f|_C$, è una nuova funzione definita come:
    $$ f|_C : C \to B $$
    $$ f|_C(x) = f(x) \quad \text{per ogni } x \in C $$
    *   **Spiegazione:** È la stessa funzione $f$, ma consideriamo solo gli input che provengono dal sottoinsieme $C$. Il codominio rimane $B$.

*   **Proprietà (Iniettività):**
    *   Se $f: A \to B$ è **iniettiva**, allora **qualsiasi** sua restrizione $f|_C: C \to B$ è anch'essa **iniettiva**. (Se $f$ non manda input diversi sullo stesso output in tutto $A$, a maggior ragione non lo farà nel sottoinsieme $C$).
    *   **Il viceversa NON vale:** Se una restrizione $f|_C$ è iniettiva, **non** è detto che la funzione originale $f$ sia iniettiva su tutto $A$.
        *   Esempio: $f(x)=x^2$ da $\mathbb{R}$ a $\mathbb{R}$ non è iniettiva. Ma la sua restrizione $f|_{(0, +\infty)}$ (ai reali positivi) è iniettiva.

### 5.3 Prolungamento di una Funzione (Pag 23)

*   Siano $f: A \to B$ e $g: C \to B$ due funzioni.
*   Diciamo che $f$ è un **prolungamento** di $g$ se:
    1.  Il dominio di $g$ è un sottoinsieme del dominio di $f$ ($C \subseteq A$).
    2.  $f$ coincide con $g$ su tutto il dominio di $g$ (cioè $f(x) = g(x)$ per ogni $x \in C$).
    *   In pratica, $f$ "estende" la funzione $g$ a un dominio più grande, comportandosi come $g$ sul dominio originale $C$. Questo è equivalente a dire che $g$ è la restrizione di $f$ a $C$ ($g = f|_C$).

*   **Proprietà (Iniettività):**
    *   Se $g: C \to B$ è iniettiva, **non** è detto che un suo prolungamento $f: A \to B$ (con $A \supset C$) sia anch'esso iniettivo. (Potremmo estendere la funzione in modo da creare "collisioni" al di fuori di $C$).

### 5.4 Esistenza di Restrizioni Iniettive (Pag 24)

*   Data una qualsiasi funzione $f: A \to B$ (con $A \neq \emptyset$), esiste **sempre** almeno una restrizione di $f$ che è iniettiva.
*   **Dimostrazione banale:** Basta prendere un qualsiasi elemento $a \in A$ e considerare il sottoinsieme $C = \{a\}$. La restrizione $f|_C: \{a\} \to B$ è definita da $f|_C(a) = f(a)$. Una funzione definita su un dominio con un solo elemento è sempre iniettiva (non ci sono due input distinti da confrontare!).

### 5.5 Funzione Identità (Pag 25)

*   Per ogni insieme non vuoto $A$, la **funzione identità** su $A$ è:
    $$ id_A: A \to A $$
    $$ id_A(a) = a $$
    *   Manda ogni elemento in se stesso.
*   Il suo grafo è $G = \{ (a, a) \mid a \in A \}$.
*   La funzione identità è sempre **iniettiva** e **suriettiva** (quindi **biettiva**).

[[Restrizione di una funzione]] [[Prolungamento di una funzione]] [[Funzione identità]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 3
> *   Abbiamo praticato la **negazione** di formule logiche complesse (implicazioni, quantificatori).
> *   Abbiamo chiarito un **errore comune sull'iniettività**.
> *   Abbiamo esplorato le **proprietà dell'immagine e della controimmagine**, collegandole alla suriettività.
> *   Abbiamo definito formalmente la **funzione suriettiva** e visto le sue caratterizzazioni equivalenti.
> *   Abbiamo analizzato diversi esempi per determinare **iniettività e suriettività**.
> *   Abbiamo introdotto la **funzione caratteristica** $\chi_A$.
> *   Abbiamo definito l'**uguaglianza tra funzioni**.
> *   Abbiamo definito la **restrizione** $f|_C$ e il **prolungamento** di funzioni, vedendo come si rapportano all'iniettività.
> *   Abbiamo definito la **funzione identità** $id_A$.

> [!TIP] Prossimi Passi
> *   Assicurati di saper distinguere bene tra iniettività e suriettività e di conoscere le loro definizioni e caratterizzazioni.
> *   Prova a creare tu degli esempi di funzioni e a determinarne iniettività e suriettività.
> *   Rifletti: una funzione può essere sia iniettiva che suriettiva? (Sì, si chiama biettiva!). Può non essere nessuna delle due? (Sì!).