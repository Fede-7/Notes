# Lezione 10: Principio di Induzione, Divisione Euclidea, Relazioni di Equivalenza

**Data:** 14/04/2025 (come da note)
**Argomenti:** Principio del Buon Ordinamento, Principio di Induzione (Forma I e II), Esempi di Induzione, Teorema della Divisione Euclidea, Identità di Bézout, Relazioni di Equivalenza, Relazioni d'Ordine, Esercizi.

#tag/induction #tag/well-ordering #tag/number-theory #tag/division-algorithm #tag/bezout-identity #tag/relations #tag/equivalence-relations #tag/order-relations #tag/algebra-avanzata

---

## 1. Principio del Buon Ordinamento e Principio di Induzione

### 1.1 Insiemi Ben Ordinati

*   **Definizione (Pag 1):** Un insieme parzialmente ordinato $(S, \le)$ si dice **ben ordinato** se ogni suo sottoinsieme **non vuoto** $X \subseteq S$ ammette un **elemento minimo**.
    *   $\min X = a \iff (a \in X) \land (\forall x \in X, a \le x)$.

*   **Esempi:**
    *   $(\mathbb{N}, \le)$ **è ben ordinato**. Questo è il **Principio del Buon Ordinamento** per i naturali. È una proprietà fondamentale.
    *   $(\mathbb{Z}, \le)$ **non è ben ordinato**. Il sottoinsieme $\mathbb{Z}$ stesso non ha minimo. Il sottoinsieme degli interi negativi non ha minimo.
    *   $(\mathbb{Q}^+, \le)$ dove $\mathbb{Q}^+ = \{ x \in \mathbb{Q} \mid x \ge 0 \}$ **non è ben ordinato**.
        *   Consideriamo $X = \{ 1/n \mid n \in \mathbb{N}^* = \{1, 2, 3, ...\} \} = \{1, 1/2, 1/3, ...\}$. Questo insieme non ha minimo (si avvicina a 0, ma 0 non appartiene a X e nessun elemento di X è il minimo).
        *   Anche $\mathbb{Q}^+$ stesso ha minimo (0), ma non tutti i suoi sottoinsiemi non vuoti ce l'hanno.
    *   Un insieme ben ordinato deve essere **totalmente ordinato** (Pag 3). Se $(S, \le)$ è ben ordinato, allora per ogni $a, b \in S$, il sottoinsieme $\{a, b\}$ deve avere un minimo. Se $\min\{a, b\} = a$, allora $a \le b$. Se $\min\{a, b\} = b$, allora $b \le a$. Quindi $a, b$ sono sempre confrontabili.
    *   Tuttavia, essere totalmente ordinato non basta per essere ben ordinato (es. $\mathbb{Z}, \mathbb{Q}^+$).

[[Insieme ben ordinato]] [[Principio del Buon Ordinamento]]

### 1.2 Principio di Induzione (Derivato dal Buon Ordinamento)

Il Principio di Induzione è uno strumento potente per dimostrare proprietà $P(n)$ che valgono per tutti i numeri naturali $n$ a partire da un certo punto. Si basa sul fatto che $(\mathbb{N}, \le)$ è ben ordinato.

*   Sia $P(n)$ una proprietà definita per $n \in \mathbb{N}$. Sia $X = \{ n \in \mathbb{N} \mid P(n) \text{ è vera} \}$. Vogliamo dimostrare che $X$ contiene tutti i naturali a partire da un certo $\bar{n}$ (spesso $\bar{n}=0$ o $\bar{n}=1$).

*   **Principio di Induzione (Forma I - Standard) (Pag 5, 11):**
    Sia $P(n)$ una proprietà per $n \in \mathbb{N}$. Se valgono entrambe le seguenti condizioni:
    1.  **Base dell'Induzione:** $P(\bar{n})$ è vera per un certo $\bar{n} \in \mathbb{N}$ (spesso $\bar{n}=0$ o $1$).
    2.  **Passo Induttivo:** Per ogni $n \ge \bar{n}$, **se** $P(n)$ è vera (**ipotesi induttiva**), **allora** anche $P(n+1)$ è vera. ($\forall n \ge \bar{n}, P(n) \implies P(n+1)$).
    **Allora:** $P(n)$ è vera per ogni $n \ge \bar{n}$. (Cioè $X = \{ n \in \mathbb{N} \mid n \ge \bar{n} \}$).

*   **Principio di Induzione (Forma II - Forte) (Pag 11):**
    Sia $P(n)$ una proprietà per $n \in \mathbb{N}$. Se valgono entrambe le seguenti condizioni:
    1.  **Base dell'Induzione:** $P(\bar{n})$ è vera per un certo $\bar{n} \in \mathbb{N}$.
    2.  **Passo Induttivo Forte:** Per ogni $n > \bar{n}$, **se** $P(i)$ è vera per **tutti** gli $i$ tali che $\bar{n} \le i < n$ (**ipotesi induttiva forte**), **allora** anche $P(n)$ è vera. ($\forall n > \bar{n}, (\forall i, \bar{n} \le i < n \implies P(i)) \implies P(n)$).
    **Allora:** $P(n)$ è vera per ogni $n \ge \bar{n}$.

> [!NOTE] Le due forme sono logicamente equivalenti. La Forma II sembra richiedere un'ipotesi più forte, ma permette di dimostrare il passo induttivo in casi in cui $P(n+1)$ dipende non solo da $P(n)$ ma anche da $P(k)$ per $k < n$.

[[Principio di Induzione]]

Ecco una tabella che confronta le due forme, aiuti a visualizzare meglio la differenza:

| Caratteristica             | Principio di Induzione (Forma I - Standard)                                  | Principio di Induzione (Forma II - Forte)                                         |
| :------------------------- | :--------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| **Obiettivo**              | Dimostrare che una proprietà $P(n)$ è vera per tutti gli $n \ge \bar{n}$.      | Dimostrare che una proprietà $P(n)$ è vera per tutti gli $n \ge \bar{n}$.         |
| **1. Base dell'Induzione** | Dimostrare che $P(\bar{n})$ è vera.                                          | Dimostrare che $P(\bar{n})$ è vera (a volte servono più casi base, es. $P(\bar{n}+1)$). |
| **2. Passo Induttivo**     | Dimostrare l'implicazione: $\forall n \ge \bar{n}, \quad P(n) \implies P(n+1)$ | Dimostrare l'implicazione: $\forall n > \bar{n}, \quad (\forall i, \bar{n} \le i < n \implies P(i)) \implies P(n)$ |
|    *Ipotesi Induttiva*     | Si assume che $P(n)$ sia vera per **un singolo** valore $n$.                 | Si assume che $P(i)$ sia vera per **TUTTI** i valori $i$ da $\bar{n}$ fino a $n-1$. |
|    *Tesi da Dimostrare*    | Si dimostra che $P(n+1)$ è vera.                                             | Si dimostra che $P(n)$ è vera.                                                    |
| **Analogia Domino**        | Se la tessera $n$ cade, allora fa cadere la tessera $n+1$.                    | Se **tutte** le tessere da $\bar{n}$ a $n-1$ sono cadute, allora fanno cadere la tessera $n$. |

**Punti Chiave della Tabella:**

*   L'**obiettivo** è lo stesso per entrambe le forme.
*   La **Base** è simile (dimostrare il primo/i primi casi).
*   La grande differenza è nel **Passo Induttivo**:
    *   **Forma I:** Assumi vero per $n \implies$ Dimostri vero per $n+1$. (Guardi solo l'ultimo passo).
    *   **Forma II:** Assumi vero per *tutti* da $\bar{n}$ a $n-1 \implies$ Dimostri vero per $n$. (Guardi tutta la storia precedente).

### 1.3 Esempi di Dimostrazioni per Induzione

*   **Esempio 1: Somma dei primi n interi (Pag 4, 6):**
    *   $P(n): 1 + 2 + \dots + n = \frac{n(n+1)}{2}$. Vogliamo dimostrare per $n \ge 1$.
    *   **Base ($\bar{n}=1$):** $P(1): 1 = \frac{1(1+1)}{2} = \frac{1 \cdot 2}{2} = 1$. Vera.
    *   **Passo Induttivo (Forma I):** Assumiamo $P(n)$ vera per un $n \ge 1$ (Ipotesi Induttiva: $1 + \dots + n = \frac{n(n+1)}{2}$). Dobbiamo dimostrare $P(n+1)$, cioè $1 + \dots + n + (n+1) = \frac{(n+1)((n+1)+1)}{2} = \frac{(n+1)(n+2)}{2}$.
        *   Partiamo dal lato sinistro di $P(n+1)$:
            $$ (1 + 2 + \dots + n) + (n+1) $$
        *   Usiamo l'ipotesi induttiva sul pezzo tra parentesi:
            $$ = \frac{n(n+1)}{2} + (n+1) $$
        *   Mettiamo a denominatore comune:
            $$ = \frac{n(n+1) + 2(n+1)}{2} $$
        *   Raccogliamo $(n+1)$:
            $$ = \frac{(n+1)(n+2)}{2} $$
        *   Questo è esattamente il lato destro di $P(n+1)$. Abbiamo dimostrato $P(n) \implies P(n+1)$.
    *   **Conclusione:** Per il Principio di Induzione, $P(n)$ è vera per ogni $n \ge 1$.

*   **Esempio 2: Cardinalità dell'Insieme delle Parti (Pag 7-10):**
    *   $P(n):$ Se $|S|=n$, allora $|P(S)|=2^n$. Vogliamo dimostrare per $n \ge 0$.
    *   **Base ($\bar{n}=0$):** $P(0):$ Se $|S|=0$, allora $S=\emptyset$. $P(S) = \{\emptyset\}$, quindi $|P(S)|=1$. Vogliamo verificare se $1 = 2^0$. Sì. $P(0)$ è vera.
    *   **Passo Induttivo (Forma I):** Assumiamo $P(n)$ vera per un $n \ge 0$ (Ipotesi Induttiva: per ogni insieme $T$ con $|T|=n$, vale $|P(T)|=2^n$). Dobbiamo dimostrare $P(n+1)$: per ogni insieme $S$ con $|S|=n+1$, vale $|P(S)|=2^{n+1}$.
        *   Sia $S$ un insieme con $|S|=n+1$. Scriviamo $S = \{a_1, ..., a_n, a_{n+1}\}$.
        *   Consideriamo l'insieme $T = S \setminus \{a_{n+1}\} = \{a_1, ..., a_n\}$. Allora $|T|=n$.
        *   Per ipotesi induttiva, $|P(T)|=2^n$.
        *   Consideriamo i sottoinsiemi di $S$. Possiamo dividerli in due categorie:
            1.  $\mathcal{B} = \{ X \in P(S) \mid a_{n+1} \notin X \}$: Questi sono esattamente i sottoinsiemi di $T$. Quindi $\mathcal{B} = P(T)$, e $|\mathcal{B}| = |P(T)| = 2^n$.
            2.  $\mathcal{A} = \{ X \in P(S) \mid a_{n+1} \in X \}$: Ogni insieme $X$ in $\mathcal{A}$ può essere scritto come $X = Y \cup \{a_{n+1}\}$ dove $Y = X \setminus \{a_{n+1}\}$. Notiamo che $Y \subseteq T$ (perché $Y$ non contiene $a_{n+1}$). Quindi $Y \in P(T) = \mathcal{B}$.
        *   Consideriamo la funzione $f: \mathcal{A} \to \mathcal{B}$ definita da $f(X) = X \setminus \{a_{n+1}\}$.
            *   È ben definita: se $X \in \mathcal{A}$, $f(X)$ non contiene $a_{n+1}$ ed è un sottoinsieme di $T$, quindi $f(X) \in \mathcal{B}$.
            *   È iniettiva? Se $f(X)=f(Y)$, allora $X \setminus \{a_{n+1}\} = Y \setminus \{a_{n+1}\}$. Poiché sia $X$ che $Y$ contengono $a_{n+1}$ (perché appartengono ad $\mathcal{A}$), aggiungere $a_{n+1}$ ad entrambi i lati mantiene l'uguaglianza: $(X \setminus \{a_{n+1}\}) \cup \{a_{n+1}\} = (Y \setminus \{a_{n+1}\}) \cup \{a_{n+1}\}$, cioè $X=Y$. Sì.
            *   È suriettiva? Per ogni $Y \in \mathcal{B}$ (cioè $Y \subseteq T$), consideriamo $X = Y \cup \{a_{n+1}\}$. Chiaramente $a_{n+1} \in X$, quindi $X \in \mathcal{A}$. Inoltre, $f(X) = (Y \cup \{a_{n+1}\}) \setminus \{a_{n+1}\} = Y$. Sì.
            *   Quindi $f$ è biettiva.
        *   Poiché $f: \mathcal{A} \to \mathcal{B}$ è biettiva, $|\mathcal{A}| = |\mathcal{B}| = 2^n$.
        *   L'insieme delle parti $P(S)$ è l'unione disgiunta di $\mathcal{A}$ e $\mathcal{B}$: $P(S) = \mathcal{A} \cup \mathcal{B}$ e $\mathcal{A} \cap \mathcal{B} = \emptyset$.
        *   Quindi $|P(S)| = |\mathcal{A}| + |\mathcal{B}| = 2^n + 2^n = 2 \cdot 2^n = 2^{n+1}$.
        *   Abbiamo dimostrato $P(n+1)$.
    *   **Conclusione:** Per il Principio di Induzione, $P(n)$ è vera per ogni $n \ge 0$.

---

## 2. Teorema della Divisione Euclidea e Identità di Bézout

Torniamo all'aritmetica in $\mathbb{Z}$.

### 2.1 Teorema della Divisione Euclidea (Pag 14)

*   **Enunciato:** Per ogni $m, n \in \mathbb{Z}$ con $n \neq 0$, esistono **unici** interi $q$ (quoziente) e $r$ (resto) tali che:
    $$ m = n \cdot q + r \quad \text{e} \quad 0 \le r < |n| $$

*   **Esempi (Pag 14-15):**
    *   $m=17, n=5$: $17 = 5 \cdot 3 + 2$. ($q=3, r=2$). $0 \le 2 < |5|=5$.
    *   $m=17, n=-5$: $17 = (-5) \cdot (-3) + 2$. ($q=-3, r=2$). $0 \le 2 < |-5|=5$.
    *   $m=-17, n=5$: $-17 = 5 \cdot (-4) + 3$. ($q=-4, r=3$). $0 \le 3 < |5|=5$. (Attenzione: non $-17 = 5 \cdot (-3) - 2$, perché il resto $-2$ non soddisfa $0 \le r < 5$).
    *   $m=-17, n=-5$: $-17 = (-5) \cdot 4 + 3$. ($q=4, r=3$). $0 \le 3 < |-5|=5$.
    *   $m=5, n=17$: $5 = 17 \cdot 0 + 5$. ($q=0, r=5$). $0 \le 5 < |17|=17$.

*   **Dimostrazione (Cenno per Esistenza, $m, n > 0$, Pag 16-18):**
    *   Si usa l'induzione (forte) su $m$.
    *   **Base:** Se $0 \le m < n$. Allora $m = n \cdot 0 + m$. Scegliamo $q=0, r=m$. Vale $0 \le r < n$. OK.
    *   **Passo Induttivo Forte:** Supponiamo che la tesi valga per tutti gli $\bar{m}$ con $0 \le \bar{m} < m$ (per un $n$ fissato). Dobbiamo dimostrare che vale per $m$ (assumendo $m \ge n$).
        *   Consideriamo $\bar{m} = m - n$. Poiché $m \ge n$, $\bar{m} \ge 0$. Poiché $n>0$, $\bar{m} < m$.
        *   Per ipotesi induttiva forte, esistono $\bar{q}, \bar{r}$ tali che $\bar{m} = n \cdot \bar{q} + \bar{r}$ con $0 \le \bar{r} < n$.
        *   Sostituiamo $\bar{m}$: $m - n = n \cdot \bar{q} + \bar{r}$.
        *   Portiamo $n$ a destra: $m = n \cdot \bar{q} + n + \bar{r} = n \cdot (\bar{q} + 1) + \bar{r}$.
        *   Abbiamo trovato $q = \bar{q} + 1$ e $r = \bar{r}$. Poiché $0 \le \bar{r} < n$, abbiamo $0 \le r < n$.
        *   La tesi vale anche per $m$.
    *   Per il principio di induzione, l'esistenza è dimostrata per $m, n \ge 0$. (Si estende poi ai casi negativi).

*   **Dimostrazione (Unicità, Pag 19-20):**
    *   Supponiamo che esistano due coppie $(q_1, r_1)$ e $(q_2, r_2)$ tali che:
        *   $m = n \cdot q_1 + r_1$ con $0 \le r_1 < |n|$
        *   $m = n \cdot q_2 + r_2$ con $0 \le r_2 < |n|$
    *   Sottraendo le due equazioni: $0 = n(q_1 - q_2) + (r_1 - r_2)$.
    *   Quindi $n(q_1 - q_2) = r_2 - r_1$.
    *   Poiché $0 \le r_1 < |n|$ e $0 \le r_2 < |n|$, la loro differenza $r_2 - r_1$ soddisfa $-|n| < r_2 - r_1 < |n|$.
    *   Ma $n(q_1 - q_2)$ è un multiplo di $n$. L'unico multiplo di $n$ strettamente compreso tra $-|n|$ e $|n|$ è $0$.
    *   Quindi deve essere $r_2 - r_1 = 0$, cioè $r_1 = r_2$.
    *   Sostituendo nell'equazione $n(q_1 - q_2) = r_2 - r_1$, otteniamo $n(q_1 - q_2) = 0$.
    *   Poiché $n \neq 0$, deve essere $q_1 - q_2 = 0$, cioè $q_1 = q_2$.
    *   La coppia $(q, r)$ è unica.

[[Divisione Euclidea]]

### 2.2 Identità di Bézout (Pag 21)

*   **Enunciato (Corollario del Teorema della Divisione / Algoritmo Euclideo):** Per ogni $a, b \in \mathbb{Z}$, se $d = \text{MCD}(a, b)$ (il MCD positivo), allora esistono interi $h, k \in \mathbb{Z}$ tali che:
    $$ d = a \cdot h + b \cdot k $$
    *   **Spiegazione:** Il Massimo Comun Divisore di due interi può sempre essere espresso come una **combinazione lineare** intera degli stessi due interi.
    *   Gli interi $h, k$ non sono unici, ma possono essere trovati usando l'**Algoritmo Euclideo** delle divisioni successive (non visto in dettaglio qui).
*   Anche l'associato $-d$ si può esprimere: $-d = a(-h) + b(-k)$.

[[Identità di Bézout]] [[Algoritmo di Euclide]]

---

## 3. Relazioni di Equivalenza e Ordine

Riprendiamo le proprietà delle relazioni binarie su un insieme $S$.

*   **Proprietà (Pag 23, 27):**
    1.  Riflessiva: $\forall x, x \mathcal{R} x$
    2.  Antiriflessiva: $\forall x, \neg (x \mathcal{R} x)$
    3.  Simmetrica: $x \mathcal{R} y \implies y \mathcal{R} x$
    4.  Antisimmetrica: $(x \mathcal{R} y \land y \mathcal{R} x) \implies x = y$
    5.  Transitiva: $(x \mathcal{R} y \land y \mathcal{R} z) \implies x \mathcal{R} z$

*   **Relazione di Equivalenza (Pag 24):** Una relazione $\mathcal{R}$ su $S$ è di equivalenza se è:
    *   **Riflessiva (1)**
    *   **Simmetrica (3)**
    *   **Transitiva (5)**
    *   Obiettivo: Partizionare l'insieme in classi di elementi "equivalenti".

*   **Relazione d'Ordine (Pag 24):** Una relazione $\mathcal{R}$ su $S$ è d'ordine (parziale) se è:
    *   **Riflessiva (1)**
    *   **Antisimmetrica (4)**
    *   **Transitiva (5)**
    *   Se è anche **totalmente definita** ($\forall x, y$, $x \mathcal{R} y$ o $y \mathcal{R} x$), si parla di **ordine totale**.
    *   Obiettivo: Stabilire un ordinamento (parziale o totale) tra gli elementi.

*   **Esempi di Relazioni di Equivalenza (Pag 25-28):**
    1.  **Relazione Totale ($G=S \times S$):** Riflessiva, Simmetrica, Transitiva. **SÌ**. (Tutti gli elementi sono equivalenti tra loro, un'unica classe di equivalenza S).
    2.  **Relazione di Identità ($G=Diag(A)$):** Riflessiva, Simmetrica, Transitiva. **SÌ**. (Ogni elemento è equivalente solo a se stesso, classi di equivalenza sono i singleton $\{a\}$).
    3.  **$(\mathbb{Z}, \mathcal{R}_{||})$ con $a \mathcal{R}_{||} b \iff |a|=|b|$:** Riflessiva, Simmetrica, Transitiva. **SÌ**. (Classi di equivalenza: $\{0\}, \{1, -1\}, \{2, -2\}, ...$).
    4.  **Costruzione di $\mathbb{Q}$ (Pag 26-28):** Sia $S = \mathbb{Z} \times \mathbb{Z}^* = \{ (a, b) \mid a, b \in \mathbb{Z}, b \neq 0 \}$. Definiamo $\mathcal{R}$ su $S$ come:
        $$ (a, b) \mathcal{R} (c, d) \iff a \cdot d = b \cdot c $$
        (Questa rappresenta l'uguaglianza delle frazioni $a/b = c/d$).
        *   **Riflessiva?** $(a, b) \mathcal{R} (a, b) \iff a \cdot b = b \cdot a$. Vero per commutatività in $\mathbb{Z}$. **SÌ**.
        *   **Simmetrica?** $(a, b) \mathcal{R} (c, d) \implies a \cdot d = b \cdot c$. Vogliamo $(c, d) \mathcal{R} (a, b)$, cioè $c \cdot b = d \cdot a$. Per commutatività, $b \cdot c = c \cdot b$ e $a \cdot d = d \cdot a$. Quindi $a \cdot d = b \cdot c \implies d \cdot a = c \cdot b$. **SÌ**.
        *   **Transitiva?** $(a, b) \mathcal{R} (c, d) \land (c, d) \mathcal{R} (e, f)$. Significa $ad=bc$ e $cf=de$. Vogliamo $(a, b) \mathcal{R} (e, f)$, cioè $af=be$.
            *   Da $ad=bc$, moltiplichiamo per $f$: $adf = bcf$.
            *   Da $cf=de$, sostituiamo $cf$: $adf = b(de)$.
            *   $adf = bde$. Poiché $d \in \mathbb{Z}^*$, $d \neq 0$. Possiamo cancellare $d$ (perché $\mathbb{Z}$ è dominio): $af = be$. **SÌ**.
        *   **Conclusione:** $\mathcal{R}$ è una relazione di equivalenza su $\mathbb{Z} \times \mathbb{Z}^*$. Le classi di equivalenza $[(a, b)]$ rappresentano i numeri razionali.

[[Relazione di equivalenza]] [[Relazione d'ordine]] [[Costruzione dei numeri razionali]]

---

## 4. Esercizi Proposti (Pag 29)

Verificare se le seguenti sono relazioni di equivalenza sui rispettivi insiemi. Ricorda che per essere di equivalenza, una relazione deve essere **Riflessiva**, **Simmetrica** e **Transitiva**.

> [!EXERCISE] Esercizio 1: Relazione su P(S)
> Sia $S = \{a, b, c, d\}$ e sia $K = \{b, c\}$.
> Si consideri la relazione $\mathcal{R}_1$ su $P(S)$ definita da:
> $$ X \mathcal{R}_1 Y \iff X \cap K = Y \cap K $$
> Verificare se $\mathcal{R}_1$ è una relazione di equivalenza.

> [!EXERCISE] Esercizio 2: Relazione su P(S)
> Sia $S = \{a, b, c, d\}$ e sia $K = \{b, c\}$.
> Si consideri la relazione $\mathcal{R}_2$ su $P(S)$ definita da:
> $$ X \mathcal{R}_2 Y \iff X \cup K = Y \cup K $$
> Verificare se $\mathcal{R}_2$ è una relazione di equivalenza.

> [!EXERCISE] Esercizio 3: Relazione su P(S)
> Sia $S = \{a, b, c, d\}$ e sia $K = \{b, c\}$.
> Si consideri la relazione $\mathcal{R}_3$ su $P(S)$ definita da:
> $$ X \mathcal{R}_3 Y \iff X \setminus K = Y \setminus K $$
> Verificare se $\mathcal{R}_3$ è una relazione di equivalenza.

> [!EXERCISE] Esercizio 4: Relazione su $\mathbb{Z} \times \mathbb{Z}$
> Si consideri la relazione $\mathcal{R}_4$ su $\mathbb{Z} \times \mathbb{Z}$ definita da:
> $$ (a, b) \mathcal{R}_4 (c, d) \iff a + c = b + d $$
> Verificare se $\mathcal{R}_4$ è una relazione di equivalenza.

---

> [!SUMMARY] Riepilogo Veloce Lezione 10
> *   Il **Principio del Buon Ordinamento** di $\mathbb{N}$ garantisce che ogni sottoinsieme non vuoto ha minimo.
> *   Il **Principio di Induzione** (Forma I e II) è una tecnica di dimostrazione basata sul buon ordinamento.
> *   Il **Teorema della Divisione Euclidea** garantisce esistenza e unicità di quoziente e resto $r$ con $0 \le r < |n|$.
> *   L'**Identità di Bézout** afferma che $\text{MCD}(a, b)$ è combinazione lineare intera di $a$ e $b$.
> *   Una **Relazione di Equivalenza** è Riflessiva, Simmetrica, Transitiva.
> *   Una **Relazione d'Ordine** è Riflessiva, Antisimmetrica, Transitiva.
> *   La relazione $ad=bc$ su $\mathbb{Z} \times \mathbb{Z}^*$ è di equivalenza e definisce i razionali.

> [!TIP] Prossimi Passi
> *   Prova a svolgere gli esercizi sulle relazioni di equivalenza.
> *   Il passo successivo naturale è studiare le **classi di equivalenza** e l'**insieme quoziente** associati a una relazione di equivalenza, e vedere come le partizioni sono collegate.
> *   Approfondire le **relazioni d'ordine** (parziale, totale, massimi, minimi, maggioranti, minoranti).