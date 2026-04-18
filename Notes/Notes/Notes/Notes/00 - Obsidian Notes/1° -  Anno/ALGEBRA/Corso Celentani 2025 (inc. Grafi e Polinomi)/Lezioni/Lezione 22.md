# Lezione 22 di Algebra Avanzata - 03 Giugno 2025

**Docente:** Maria Rosaria Celentani
**Argomenti Principali:** Sottoanelli, Reticoli (Dualità, Complementati, Distributivi, Booleani), Algebre di Boole, Anelli Booleani.

> [!TIP] Ricorda!
> *   Usa il tuo **dizionario visuale** per i simboli che incontriamo. Se un simbolo è nuovo o ostico, disegnalo e associalo a un'immagine o a una parola chiave che ti aiuti a ricordarlo!
> *   Non esitare a **fare pause** quando ne senti il bisogno. Il cervello impara meglio quando è riposato.
> *   Se un concetto sembra un mostro, spezzettiamolo in parti più piccole. Insieme, possiamo domarlo!

---

## 1. Sottoanelli: Piccoli Mondi negli Anelli

Ricordi cosa sia un **anello** $(A, +, \cdot)$? È una struttura algebrica con due operazioni, un po' come i numeri interi che puoi sommare e moltiplicare.

Ora, immaginiamo di trovare un "piccolo mondo" all'interno di un anello più grande, che si comporta esso stesso come un anello. Quello è un **sottoanello**!

> [!NOTE] Definizione: Sottoanello
> Sia $(A, +, \cdot)$ un anello e sia $B$ un sottoinsieme **non vuoto** di $A$ ($B \subseteq A$, $B \neq \emptyset$).
> Diciamo che $(B, +, \cdot)$ è un **sottoanello** di $A$ se soddisfa queste condizioni:
> 1.  **$B$ è stabile (o chiuso) rispetto a entrambe le operazioni $+$ e $\cdot$**:
>     *   Per ogni $b_1, b_2 \in B$, anche $b_1 + b_2 \in B$ (in realtà questa si deduce dal punto 2, ma spesso si verifica la chiusura rispetto alla sottrazione).
>     *   Per ogni $b_1, b_2 \in B$, anche $b_1 \cdot b_2 \in B$.
>     *   Più sinteticamente (e comunemente): per ogni $b_1, b_2 \in B$, $b_1 - b_2 \in B$ e $b_1 \cdot b_2 \in B$.
> 2.  **$(B, +)$ è un gruppo abeliano.** (Deve contenere lo zero dell'anello $A$, e l'opposto di ogni suo elemento).
> 3.  **$(B, \cdot)$ è un semigruppo.** (L'operazione $\cdot$ è associativa in $B$, ma questo è ereditato da $A$).
>
> In pratica, se $B$ è chiuso per sottrazione e per moltiplicazione, e non è vuoto, allora è un sottoanello!

**Esempio Visto a Lezione (Pagina 1 degli appunti):**

Consideriamo l'anello $A = M_{2,2}(\mathbb{R})$ delle matrici $2 \times 2$ con coefficienti reali, con le usuali operazioni di somma ($+$) e prodotto ($\cdot$) tra matrici.
Sia $B$ il seguente sottoinsieme di $A$:
$$
B = \left\{ \begin{pmatrix} a & 0 \\ 0 & 0 \end{pmatrix} \mid a \in \mathbb{R} \right\}
$$
Questo insieme $B$ è un sottoanello di $A$? Vediamo!

*   **$B$ non è vuoto?** Certo, se $a=0$, la matrice nulla $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ appartiene a $B$.
*   **Chiusura rispetto alla sottrazione:**
    Prendiamo due matrici generiche in $B$:
    $X = \begin{pmatrix} a & 0 \\ 0 & 0 \end{pmatrix}$ e $Y = \begin{pmatrix} b & 0 \\ 0 & 0 \end{pmatrix}$, con $a, b \in \mathbb{R}$.
    La loro differenza è:
    $$
    X - Y = \begin{pmatrix} a & 0 \\ 0 & 0 \end{pmatrix} - \begin{pmatrix} b & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} a-b & 0 \\ 0 & 0 \end{pmatrix}
    $$
    Poiché $a-b$ è ancora un numero reale, la matrice $X-Y$ ha la forma richiesta per appartenere a $B$. Quindi, $B$ è chiuso rispetto alla sottrazione.
*   **Chiusura rispetto alla moltiplicazione:**
    Il loro prodotto è:
    $$
    X \cdot Y = \begin{pmatrix} a & 0 \\ 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} b & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} a \cdot b + 0 \cdot 0 & a \cdot 0 + 0 \cdot 0 \\ 0 \cdot b + 0 \cdot 0 & 0 \cdot 0 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} ab & 0 \\ 0 & 0 \end{pmatrix}
    $$
    Poiché $ab$ è ancora un numero reale, la matrice $X \cdot Y$ appartiene a $B$. Quindi, $B$ è chiuso rispetto alla moltiplicazione.

**Conclusione:** Sì, $B$ è un sottoanello di $M_{2,2}(\mathbb{R})$!

> [!NOTE] Un dettaglio menzionato negli appunti (pag. 1):
> $I_A \neq I_B$ in generale. $I_A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
> L'elemento $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ agisce come identità moltiplicativa *all'interno* di $B$ (se $B$ fosse un anello unitario a sé stante), ma non è l'identità di $A$.
> In questo specifico esempio $B$, l'elemento $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ è l'unità di $B$.
> Chiamiamolo $1_B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Se moltiplichi qualsiasi matrice $X \in B$ per $1_B$, ottieni $X$.

---

## 2. Reticoli: L'Arte dell'Ordine

Passiamo ora ai **reticoli**. Immagina una struttura dove gli elementi sono "ordinati" in qualche modo, e per ogni coppia di elementi possiamo trovare un "punto d'incontro superiore" e un "punto d'incontro inferiore".

> [!NOTE] Definizione: Reticolo (con relazione d'ordine $\le$)
> Un insieme parzialmente ordinato $(L, \le)$ (cioè $\le$ è riflessiva, antisimmetrica, transitiva) si dice un **reticolo** se, per ogni coppia di elementi $a, b \in L$, esistono:
> 1.  L'**estremo inferiore** (o *meet* o *infimum*), indicato con $a \land b$ (leggi "a meet b" o "a inf b"). È il più grande elemento che è $\le a$ e $\le b$.
> 2.  L'**estremo superiore** (o *join* o *supremum*), indicato con $a \lor b$ (leggi "a join b" o "a sup b"). È il più piccolo elemento che è $\ge a$ e $\ge b$.
>
> Possiamo anche definire un reticolo algebricamente con le operazioni $\land$ (meet) e $\lor$ (join) che soddisfano certe proprietà (associatività, commutatività, assorbimento).

### 2.1. Principio di Dualità (Pagina 2)

Questo è un concetto super potente e elegante! È come guardare un'immagine allo specchio.

> [!IMPORTANT] Principio di Dualità per Reticoli
> Se un enunciato (una proprietà, un teorema) è valido per **tutti** i reticoli, allora anche l'enunciato **duale** è valido per tutti i reticoli.
>
> Come si ottiene l'enunciato duale?
> *   Si scambia $\le$ con $\ge$.
> *   Si scambia $\land$ con $\lor$.
> *   Se presenti, si scambiano gli eventuali elementi $0_L$ (minimo) e $1_L$ (massimo).
>
> Se hai un reticolo $(L, \le)$, il suo **reticolo duale** è $(L^*, \ge^*)$, dove $L^* = L$ e la relazione $a \le^* b$ in $L^*$ è definita come $b \le a$ in $L$ (o, come scritto negli appunti, $a \le^* b \iff a \ge b$). Le operazioni diventano:
> *   $\land^*$ (meet nel duale) corrisponde a $\lor$ (join nell'originale).
> *   $\lor^*$ (join nel duale) corrisponde a $\land$ (meet nell'originale).

**Esempi di Enunciati Duali (dalla Pagina 3):**

Sia $(L, \le)$ un reticolo.
*   **Enunciato $a$**: $\forall a \in L, \exists b \in L \mid b \le a$. (Per ogni elemento, ne esiste uno più piccolo o uguale).
    *   **Enunciato duale $a^*$**: $\forall a \in L, \exists b \in L \mid b \ge a$. (Per ogni elemento, ne esiste uno più grande o uguale).
*   **Enunciato $a$**: $\forall a, b \in L, \exists c \in L \mid c \le a \land b$.
    *   **Enunciato duale $a^*$**: $\forall a, b \in L, \exists c \in L \mid c \ge a \lor b$.
*   **Enunciato $a$**: Se esiste $0_L$ (elemento minimo), allora $0_L \le a, \forall a \in L$.
    *   **Enunciato duale $a^*$**: Se esiste $1_L$ (elemento massimo), allora $1_L \ge a, \forall a \in L$.

> [!TIP] Pensa alla musica! Se hai una melodia che sale, la sua "duale" potrebbe essere una melodia che scende in modo speculare. Il principio di dualità ci dice che se certe armonie funzionano con la melodia originale, armonie "speculari" funzioneranno con la melodia duale.

### 2.2. Esempio Pratico: Una Relazione d'Ordine su $\mathbb{N} \times \mathbb{N}$ (Pagine 4-6)

Consideriamo l'insieme $\mathbb{N} \times \mathbb{N}$ (coppie di numeri naturali, assumendo $\mathbb{N}=\{0, 1, 2, ...\}$ o $\{1, 2, 3, ...\}$ a seconda della convenzione usata a lezione – qui l'uso di $3^0 \cdot 7^0$ implica $0 \in \mathbb{N}$ per gli esponenti).
Definiamo una relazione $\rho$ (che indicheremo con $\le_\rho$ per chiarezza) su $\mathbb{N} \times \mathbb{N}$ così:
Per $(a,b), (c,d) \in \mathbb{N} \times \mathbb{N}$:
$$
(a,b) \le_\rho (c,d) \iff 3^a \cdot 7^b \le 3^c \cdot 7^d
$$
dove $\le$ è la solita relazione d'ordine sui numeri naturali.

**Dimostriamo che $(\mathbb{N} \times \mathbb{N}, \le_\rho)$ è un insieme parzialmente ordinato (POSET):**

1.  **Riflessività**: $(a,b) \le_\rho (a,b)$?
    Questo significa $3^a \cdot 7^b \le 3^a \cdot 7^b$. Vero, per la riflessività di $\le$ su $\mathbb{N}$.
2.  **Antisimmetria**: Se $(a,b) \le_\rho (c,d)$ e $(c,d) \le_\rho (a,b)$, allora $(a,b)=(c,d)$?
    *   $(a,b) \le_\rho (c,d) \implies 3^a \cdot 7^b \le 3^c \cdot 7^d$.
    *   $(c,d) \le_\rho (a,b) \implies 3^c \cdot 7^d \le 3^a \cdot 7^b$.
    Se entrambi sono veri, allora $3^a \cdot 7^b = 3^c \cdot 7^d$. Per il **Teorema Fondamentale dell'Aritmetica** (unicità della scomposizione in fattori primi), questo implica che $a=c$ e $b=d$. Quindi $(a,b)=(c,d)$. Vera.
3.  **Transitività**: Se $(a,b) \le_\rho (c,d)$ e $(c,d) \le_\rho (e,f)$, allora $(a,b) \le_\rho (e,f)$?
    *   $(a,b) \le_\rho (c,d) \implies 3^a \cdot 7^b \le 3^c \cdot 7^d$.
    *   $(c,d) \le_\rho (e,f) \implies 3^c \cdot 7^d \le 3^e \cdot 7^f$.
    Per la transitività di $\le$ su $\mathbb{N}$, segue che $3^a \cdot 7^b \le 3^e \cdot 7^f$.
    Quindi $(a,b) \le_\rho (e,f)$. Vera.

Quindi, $(\mathbb{N} \times \mathbb{N}, \le_\rho)$ è un POSET.

**È un ordine totale? (Pagina 5)**
Sì. Dati due elementi qualsiasi $(a,b)$ e $(c,d)$, i numeri $N_1 = 3^a \cdot 7^b$ e $N_2 = 3^c \cdot 7^d$ sono numeri naturali. Tra $N_1$ e $N_2$ vale sempre $N_1 \le N_2$ oppure $N_2 \le N_1$. Quindi, o $(a,b) \le_\rho (c,d)$ o $(c,d) \le_\rho (a,b)$.
L'insieme è **totalmente ordinato**.

**È un reticolo? (Pagina 6)**
Sì, ogni insieme totalmente ordinato è un reticolo!
Dati $(a,b)$ e $(c,d)$:
*   $(a,b) \land (c,d) = \min((a,b), (c,d))$ secondo $\le_\rho$.
*   $(a,b) \lor (c,d) = \max((a,b), (c,d))$ secondo $\le_\rho$.
Ad esempio, se $3^a \cdot 7^b \le 3^c \cdot 7^d$, allora $(a,b) \land (c,d) = (a,b)$ e $(a,b) \lor (c,d) = (c,d)$.

**Funzione $f$ (Pagina 6):**
La funzione $f: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ definita come $f((a,b)) = 3^a \cdot 7^b$ è un **isomorfismo d'ordine** tra $(\mathbb{N} \times \mathbb{N}, \le_\rho)$ e l'immagine $Im(f) = \{3^a \cdot 7^b \mid a,b \in \mathbb{N}\}$ con la solita relazione $\le$.
L'immagine $Im(f)$ è un sottoinsieme di $\mathbb{N}$.
Il minimo di $(\mathbb{N} \times \mathbb{N}, \le_\rho)$ è $(0,0)$, poiché $f((0,0)) = 3^0 \cdot 7^0 = 1$ (se $0 \in \mathbb{N}$ per gli esponenti). Se invece $\mathbb{N}=\{1,2,...\}$, il minimo sarebbe $(1,1)$ e $f((1,1)) = 3^1 \cdot 7^1 = 21$. L'appunto dice `min(N x N) = 1` e poi `f( (1) ) = { (0,0) }` (sembra una notazione un po' confusa, ma probabilmente si riferisce al fatto che $1$ è il minimo dell'immagine e corrisponde a $(0,0)$).

**Esercizio Proposto (Pagina 7):**
Ripetere l'esercizio con la relazione $\sigma$ (che indicheremo con $\le_\sigma$):
$$
(a,b) \le_\sigma (c,d) \iff (3^a \cdot 7^b) \text{ divide } (3^c \cdot 7^d)
$$
Questa è la relazione di **divisibilità**.
Questo definisce un altro POSET. Sarà un reticolo? Sarà totalmente ordinato? (Spoiler: è un reticolo, ma non totalmente ordinato. Ad esempio $(1,0)$ e $(0,1)$ non sono confrontabili, cioè $3^1 \cdot 7^0 = 3$ non divide $3^0 \cdot 7^1=7$, e viceversa).
Prova a verificarlo! È un ottimo esercizio.

---

## 3. Tipi Speciali di Reticoli

Non tutti i reticoli sono uguali! Alcuni hanno proprietà speciali.

### 3.1. Reticoli Limitati (Pagina 8, 10)

> [!NOTE] Definizione: Reticolo Limitato
> Un reticolo $(L, \le)$ (o $(L, \land, \lor)$) si dice **limitato** se possiede:
> *   Un elemento minimo, chiamato **zero** ($0_L$ o $0$), tale che $0_L \le x$ per ogni $x \in L$.
> *   Un elemento massimo, chiamato **uno** ($1_L$ o $1$), tale che $x \le 1_L$ per ogni $x \in L$.
>
> Nelle notazioni algebriche:
> *   $x \lor 0_L = x$ e $x \land 0_L = 0_L$
> *   $x \land 1_L = x$ e $x \lor 1_L = 1_L$
> (L'appunto a pag. 10 dice che $0_L$ è l'elemento neutro per $\lor$, e $1_L$ è l'elemento neutro per $\land$).

### 3.2. Reticoli Complementati (Pagine 8-9)

Questa è come trovare l' "opposto" o il "contrario" di un elemento, ma in senso reticolare.

> [!NOTE] Definizione: Reticolo Complementato
> Un reticolo **limitato** $(L, \le, 0_L, 1_L)$ si dice **complementato** se per ogni elemento $a \in L$ esiste almeno un **complemento** $\bar{a} \in L$ tale che:
> $$
> a \land \bar{a} = 0_L \quad \text{e} \quad a \lor \bar{a} = 1_L
> $$

**Esempi Visivi (dai disegni nelle pagine 8-9):**

*   **Diagramma a diamante (Pagina 8):**
    ```mermaid
    graph TD
        Uno["1 (Massimo)"] --> a
        Uno --> b
        Uno --> c
        a --> Zero["0 (Minimo)"]
        b --> Zero
        c --> Zero
    ```
    In questo diagramma (che assomiglia al reticolo dei sottospazi di uno spazio vettoriale di dimensione 2, o a un reticolo $M_3$ se $a,b,c$ sono atomi non confrontabili), se prendiamo l'elemento $a$:
    *   Un suo complemento potrebbe essere $b$ se $a \land b = 0$ e $a \lor b = 1$.
    *   Un suo complemento potrebbe essere $c$ se $a \land c = 0$ e $a \lor c = 1$.
    L'appunto dice: "$a$ ha come complementi $b$ e $c$". Questo implica che i complementi non sono necessariamente unici.

*   **Diagramma a pentagono (Pagina 9, sinistra):**
    ```mermaid
    graph TD
        Uno["1"] --> b
        b --> a
        a --> Zero["0"]
        Uno --> c
        c --> Zero
    ```
    In un reticolo a forma di pentagono (chiamato $N_5$), l'elemento $a$ potrebbe avere $c$ come complemento, ma l'elemento $b$ potrebbe non averne.
    L'appunto dice: "$c$ ha come complementi sia $a$ che $b$". Questo è un po' strano, bisogna verificare le relazioni esatte nel diagramma fornito (che è stilizzato). Un tipico $N_5$ è $0 < a < b < 1$ e $0 < c < 1$ con $a,b$ non confrontabili con $c$. In tal caso, per $a$, $c$ è un complemento se $a \land c = 0$ e $a \lor c = 1$. Per $b$, $c$ è complemento se $b \land c = 0$ e $b \lor c = 1$. L'elemento $a$ nel pentagono standard non ha complemento.

*   **Non tutti i reticoli limitati sono complementati (Pagina 9, destra):**
    Una catena $0 < a < 1$.
    ```mermaid
    graph TD
        Uno["1"] --> a
        a --> Zero["0"]
    ```
    L'elemento $a$ non ha complemento. Infatti:
    *   $a \land x = 0 \implies x=0$. Ma $a \lor 0 = a \neq 1$.
    *   $a \lor x = 1 \implies x=1$. Ma $a \land 1 = a \neq 0$.
    L'appunto dice: "$a$ non ha complemento". Corretto!

**Importante (Pagina 10):**
In un reticolo limitato, $0_L$ ha come unico complemento $1_L$, e viceversa.
$0_L \land 1_L = 0_L$ e $0_L \lor 1_L = 1_L$.

### 3.3. Reticoli Distributivi (Pagine 11-14)

La distributività è una proprietà che conosciamo bene dall'aritmetica (la moltiplicazione distribuisce sulla somma). Nei reticoli è simile.

> [!NOTE] Definizione: Reticolo Distributivo
> Un reticolo $(L, \land, \lor)$ si dice **distributivo** se valgono le seguenti leggi distributive (basta che ne valga una, l'altra segue per dualità):
> 1.  $a \land (b \lor c) = (a \land b) \lor (a \land c)$  per ogni $a,b,c \in L$. (meet distribuisce su join)
> 2.  $a \lor (b \land c) = (a \lor b) \land (a \lor c)$  per ogni $a,b,c \in L$. (join distribuisce su meet)

**Non tutti i reticoli sono distributivi (Pagine 11-12):**
I "cattivi ragazzi" che impediscono la distributività sono due reticoli specifici:
*   **$M_3$ (il "diamante"):** Un reticolo con 5 elementi: $0, 1$ e tre elementi $a,b,c$ tra loro non confrontabili, ma tutti compresi tra $0$ e $1$. (Quello dell'esempio di pag. 8).
    Nell'esempio di pag. 11, si mostra che per $M_3$:
    $a \land (b \lor c) = a \land 1 = a$.
    $(a \land b) \lor (a \land c) = 0 \lor 0 = 0$.
    Poiché $a \neq 0$, $M_3$ non è distributivo.
*   **$N_5$ (il "pentagono"):** Un reticolo con 5 elementi: $0 < x < y < 1$ e un altro elemento $z$ tale che $0 < z < 1$, con $z$ non confrontabile con $x$ e $y$. (Quello dell'esempio di pag. 9, sinistra, se interpretato correttamente).
    Nell'esempio di pag. 12 (che è un $N_5$ con $a, b, c, 0, 1$ dove $0<a<b<1$ e $0<c<1$, $c$ non confrontabile con $a,b$; $b$ al posto di $y$, $a$ al posto di $x$ e $c$ al posto di $z$):
    Si verifica la seconda legge distributiva con gli elementi $a,b,c$ come nell'immagine.
    $a \lor (b \land c) = a \lor 0 = a$.
    $(a \lor b) \land (a \lor c) = b \land 1 = b$. (Assumendo $a \lor b = b$ perché $a<b$, e $a \lor c = 1$ e $b \land c = 0$).
    Poiché $a \neq b$, $N_5$ non è distributivo.

> [!IMPORTANT] Teorema Fondamentale per i Reticoli Distributivi (Pagina 13)
> Un reticolo $L$ è **distributivo** se e solo se **non contiene** alcun sottoreticolo isomorfo a $M_3$ o $N_5$.
> (I disegni a pag. 13 mostrano $N_5$ e $M_3$).
> Questo è un risultato molto potente per "diagnosticare" la distributività guardando la struttura del reticolo!

**Esempio di Test di Distributività (Pagina 14):**
Sia $L = \{1, 2, 3, 4, 6, 9, 12, 18, 36\}$ l'insieme dei divisori di 36, con la relazione di divisibilità. Questo forma un reticolo. ($a \land b = \text{MCD}(a,b)$, $a \lor b = \text{mcm}(a,b)$).
L'appunto prende $M = \{1,2,4,9,36\}$ e verifica:
$2 \lor (4 \land 9) = 2 \lor (\text{MCD}(4,9)) = 2 \lor 1 = \text{mcm}(2,1) = 2$.
$(2 \lor 4) \land (2 \lor 9) = (\text{mcm}(2,4)) \land (\text{mcm}(2,9)) = 4 \land 18 = \text{MCD}(4,18) = 2$.
Qui sembra funzionare. (L'appunto dice $2 \lor (4 \land 9) = 2$ (X), e $(2 \lor 4) \land (2 \lor 9) = 4 \land 36 = 4$. Questo non è corretto, $\text{mcm}(2,9)=18$, $\text{MCD}(4,18)=2$. Sembra ci sia un errore di calcolo o trascrizione negli appunti manoscritti. Il reticolo dei divisori di 36 è distributivo).
Rifacciamo il calcolo come nell'appunto, ma con i simboli corretti:
$a=2, b=4, c=9$.
$a \lor (b \land c) = 2 \lor \text{MCD}(4,9) = 2 \lor 1 = 2$.
$(a \lor b) \land (a \lor c) = \text{mcm}(2,4) \land \text{mcm}(2,9) = 4 \land 18 = \text{MCD}(4,18) = 2$.
Quindi per questa terna $a,b,c$ la proprietà è verificata.

**Controesempio (Pagina 15): "No reticolo"**
Il diagramma a pagina 15 mostra una struttura che non è un reticolo. Probabilmente perché per alcuni elementi (es. $a$ e $d$) non esiste un unico estremo superiore o inferiore. Ad esempio, $b$ e $c$ sono entrambi "sopra" $a$ e $d$. Se non c'è un *minimo* tra questi "limiti superiori comuni", non è un reticolo.

**Unicità del Complemento (Pagina 16):**

> [!IMPORTANT] Proposizione
> Sia $(L, \land, \lor)$ un reticolo **distributivo** e **limitato**. Se un elemento $a \in L$ possiede un complemento, allora tale complemento è **unico**.
>
> **Dimostrazione (idea):**
> Supponiamo che $\bar{a}$ e $\hat{a}$ siano due complementi di $a$.
> Cioè:
> 1.  $a \land \bar{a} = 0_L$, $a \lor \bar{a} = 1_L$
> 2.  $a \land \hat{a} = 0_L$, $a \lor \hat{a} = 1_L$
>
> Vogliamo dimostrare che $\bar{a} = \hat{a}$.
> Consideriamo $\bar{a}$:
> $\bar{a} = \bar{a} \land 1_L \quad$ (perché $1_L$ è massimo)
> $\bar{a} = \bar{a} \land (a \lor \hat{a}) \quad$ (sostituisco $1_L$ usando la proprietà di $\hat{a}$)
> $\bar{a} = (\bar{a} \land a) \lor (\bar{a} \land \hat{a}) \quad$ (**uso la distributività!**)
> $\bar{a} = 0_L \lor (\bar{a} \land \hat{a}) \quad$ (sostituisco $\bar{a} \land a = 0_L$)
> $\bar{a} = \bar{a} \land \hat{a} \quad (*)$
>
> In modo simmetrico (scambiando i ruoli di $\bar{a}$ e $\hat{a}$), si ottiene:
> $\hat{a} = \hat{a} \land \bar{a} \quad (**)$
>
> Poiché $\land$ è commutativa, $\bar{a} \land \hat{a} = \hat{a} \land \bar{a}$.
> Quindi, da $(*)$ e $(**)$, segue che $\bar{a} = \hat{a}$.
> Il complemento è unico! Fantastico, vero? La distributività è la chiave qui.

**Esempi di Reticoli Distributivi (Pagina 17):**
1.  $(\mathcal{P}(S), \subseteq)$ (l'insieme delle parti di un insieme $S$, ordinato per inclusione). Le operazioni di meet e join sono $\cap$ (intersezione) e $\cup$ (unione).
    $$ A \cap (B \cup C) = (A \cap B) \cup (A \cap C) $$
    $$ A \cup (B \cap C) = (A \cup B) \cap (A \cup C) $$
    Queste sono le note proprietà distributive dell'intersezione e dell'unione. Quindi $(\mathcal{P}(S), \cap, \cup)$ è distributivo.
2.  Un **insieme totalmente ordinato** è sempre distributivo.
    Se $a \le b \le c$ (o qualsiasi altra permutazione d'ordine), le leggi distributive si riducono a identità semplici. Ad esempio, se $a \le b \le c$:
    $a \land (b \lor c) = a \land c = a$.
    $(a \land b) \lor (a \land c) = a \lor a = a$. Funziona!

**Esempio di Reticolo NON Distributivo (Pagina 18):**
Il reticolo $(\mathbb{N}_+, |)$ dei numeri naturali positivi con la relazione di divisibilità **non è** in generale distributivo.
Prendiamo i divisori di $30$: $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$.
Scegliamo $a=2, b=3, c=5$. Questi sono gli "atomi" sopra l'1.
$a \land (b \lor c) = 2 \land \text{mcm}(3,5) = 2 \land 15 = \text{MCD}(2,15) = 1$.
$(a \land b) \lor (a \land c) = \text{MCD}(2,3) \lor \text{MCD}(2,5) = 1 \lor 1 = 1$.
Questo funziona. Ma dobbiamo trovare un controesempio.
Gli elementi $a=6, b=10, c=15$ formano un $M_3$ (con $0_L = \text{MCD}(6,10,15)$ e $1_L = \text{mcm}(6,10,15)$)? No.
Il diagramma disegnato a pagina 18 per $(\mathbb{N}, |)$ è quello dei divisori di 30, che è isomorfo a $\mathcal{P}(\{p_1, p_2, p_3\})$, quindi *dovrebbe* essere distributivo.
Ah, l'appunto dice "NO" riferendosi a $(\mathbb{N}, |)$ in generale. L'esempio sotto con $D_{30}$ (elementi $1,2,3,5,30$ e altri impliciti) è fatto per mostrare un $N_5$.
Se $a=2$, $b=3 \cdot 5 = 15$, $c=5 \cdot k$ (no, questo non forma N5).
Il tipico esempio di non distributività in $(\mathbb{N}_+, |)$ si ha considerando i divisori di un numero che abbia almeno due fattori primi con esponente $\ge 1$ e un altro fattore primo. Esempio: $D_{12}=\{1,2,3,4,6,12\}$. Scegli $a=2, b=3, c=2$.
$a \lor (b \land c)$ vs $(a \lor b) \land (a \lor c)$.
In $D_{12}$, $M_3$ è dato da $\{2,3, \text{mcm}(2,3)=6, \text{MCD}(2,3)=1 \}$. No, $M_3$ è $\{d, dp_1, dp_2, dp_3, dp_1p_2p_3\}$.
Un $N_5$ in $(\mathbb{N}_+, |)$ può essere formato da $\{1, p, q, p^2, p^2q\}$ (dove $p,q$ sono primi distinti). E.g. $\{1, 2, 3, 4, 12\}$.
$0=1, x=2, y=4, 1=12, z=3$.
$x \lor (z \land y) = 2 \lor (3 \land 4) = 2 \lor \text{MCD}(3,4) = 2 \lor 1 = 2$.
$(x \lor z) \land (x \lor y) = (\text{mcm}(2,3)) \land (\text{mcm}(2,4)) = 6 \land 4 = \text{MCD}(6,4) = 2$.
Questo esempio non mostra la non-distributività.

> [!CAUTION] L'esempio della non distributività di $(\mathbb{N}, |)$ va chiarito meglio. Il reticolo dei divisori di un numero $n = p_1^{a_1} \cdots p_k^{a_k}$ è distributivo se e solo se tutti gli $a_i \le 1$ oppure $k \le 2$. Quindi $D_{30}$ (divisori di $2 \cdot 3 \cdot 5$) è distributivo. $D_{12}$ (divisori di $2^2 \cdot 3$) è distributivo. $D_{p^2 q r}$ non lo è. Ad esempio $D_{60}$ (divisori di $2^2 \cdot 3 \cdot 5$) contiene un $M_3$ (ad es. $\{2, 6, 10\}$ non è un $M_3$, i tre elementi "intermedi" sono $2\cdot3=6$, $2\cdot5=10$, $2\cdot2=4$). Gli elementi $2, 6, 10$ non sono in $M_3$.
> Il reticolo $D_{pqr}$ (come $D_{30}$) è isomorfo a $\mathcal{P}(\{p,q,r\})$ ed è distributivo.
> Il reticolo $D_{p^2q}$ (come $D_{12}$) è distributivo.
> Un reticolo $L$ è non distributivo se contiene $M_3$ o $N_5$.
> Il disegno a pagina 18 con $1,2,3,5$ e un $30$ in alto sembra l'ossatura di $D_{30}$, che è distributivo. Forse si intende che l'intero $(\mathbb{N},|)$ non è distributivo.

### 3.4. Reticoli Booleani (Pagine 18-20)

Questi sono i reticoli "perfetti": distributivi E complementati.

> [!NOTE] Definizione: Reticolo Booleano
> Un reticolo $(L, \le)$ si dice **booleano** se:
> 1.  È **distributivo**.
> 2.  È **complementato**.
> (Essendo complementato, deve essere anche limitato, quindi avere $0_L$ e $1_L$).

**L'Esempio per Eccellenza (Pagina 19):**
$(\mathcal{P}(S), \subseteq)$ è un reticolo booleano!
*   Abbiamo visto che è distributivo.
*   È limitato: $0_L = \emptyset$ (insieme vuoto), $1_L = S$ (insieme universo).
*   È complementato: per ogni $A \subseteq S$, il suo complemento è $A^c = S \setminus A$ (il complemento insiemistico).
    *   $A \cap A^c = \emptyset = 0_L$.
    *   $A \cup A^c = S = 1_L$.
L'appunto dice: "non è 'un' esempio, è L'ESEMPIO". Questo sottolinea la sua importanza!

> [!IMPORTANT] Teorema di Rappresentazione per Reticoli Booleani Finiti (Pagina 19)
> Sia $(L, \le)$ un reticolo booleano.
> *   $(L, \le)$ è isomorfo a un sottoreticolo di $(\mathcal{P}(S), \subseteq)$ per qualche insieme $S$. (Questo $S$ è l'insieme degli atomi di $L$ o degli ideali primi/massimali).
> *   Se $L$ è **finito**, allora esiste un insieme finito $S$ tale che $(L, \le)$ è isomorfo a $(\mathcal{P}(S), \subseteq)$.
> *   Inoltre, se $L$ è finito, allora la sua cardinalità (numero di elementi) è una potenza di 2: $|L|=2^n$ per qualche intero $n \ge 0$ (dove $n = |S|$).

**Esempi Grafici (Pagina 20):**
*   Una catena $0-a-b-1$ (4 elementi) **non è booleana** (a meno che non sia $0-1$, o $0-a-1$ con $a$ auto-complementare, il che non succede). Ad esempio, in $0<a<b<1$, $a$ non ha complemento. L'appunto a pag. 20 mostra una catena $0-a-b-1$ e dice "non è booleano".
*   Un reticolo booleano con $|L|=2^n$ ha la forma di un ipercubo $n$-dimensionale.
    *   $n=0 \implies |L|=1$ (un punto, $0=1$).
    *   $n=1 \implies |L|=2$ (la catena $0-1$). Booleano.
    *   $n=2 \implies |L|=4$ (il "quadrato" $0, a, b, 1$ con $a,b$ complementi l'uno dell'altro). Booleano.
    *   $n=3 \implies |L|=8$ (il "cubo", come $D_{30}$). Booleano.
L'appunto mostra un disegno che potrebbe essere la struttura di $D_{30}$ (un cubo) e un altro che è una lunga catena lineare (non booleana se ha più di 2 elementi).
La nota $|L|=2^n$ con un X sopra ($|L|=2^n \mathbb{X}$) forse significa che *non tutti* i reticoli hanno cardinalità $2^n$, solo quelli booleani finiti.

---

## 4. Algebre di Boole (Pagine 21-23)

Strettamente collegate ai reticoli booleani, le algebre di Boole formalizzano le operazioni.

> [!NOTE] Definizione: Algebra di Boole
> Un'**algebra di Boole** è una struttura $(A, \land, \lor, ', 0, 1)$ dove:
> *   $A$ è un insieme non vuoto.
> *   $\land$ (meet) e $\lor$ (join) sono operazioni binarie su $A$.
> *   $'$ (complemento o negazione) è un'operazione unaria su $A$.
> *   $0$ e $1$ sono elementi distinti di $A$ (costanti, o elementi nullari).
>
> Queste operazioni devono soddisfare le seguenti proprietà per ogni $a, b, c \in A$:
> 1.  **Associatività:**
>     *   $a \land (b \land c) = (a \land b) \land c$
>     *   $a \lor (b \lor c) = (a \lor b) \lor c$
> 2.  **Commutatività:**
>     *   $a \land b = b \land a$
>     *   $a \lor b = b \lor a$
> 3.  **Leggi di Assorbimento:** (Collegano $\land$ e $\lor$)
>     *   $a \land (a \lor b) = a$
>     *   $a \lor (a \land b) = a$
> 4.  **Distributività:** (Ognuna implica l'altra)
>     *   $a \land (b \lor c) = (a \land b) \lor (a \land c)$
>     *   $a \lor (b \land c) = (a \lor b) \land (a \lor c)$
> 5.  **Esistenza di Elementi Neutri ($0$ e $1$):**
>     *   $a \land 1 = a$
>     *   $a \lor 0 = a$
> 6.  **Leggi del Complemento:** (Con l'operazione unaria $'$ )
>     *   $a \land a' = 0$
>     *   $a \lor a' = 1$

**Connessione tra Reticoli Booleani e Algebre di Boole (Pagina 22):**
Un reticolo booleano $(L, \le)$ definisce un'algebra di Boole $(L, \land, \lor, ', 0_L, 1_L)$ dove $0_L$ è il minimo, $1_L$ il massimo, e $a'$ è l'**unico** complemento di $a$ (sappiamo che è unico perché i reticoli booleani sono distributivi).
Viceversa, un'algebra di Boole $(A, \land, \lor, ', 0, 1)$ definisce un reticolo booleano $(A, \le)$ ponendo $a \le b \iff a \land b = a$ (o equivalentemente $a \le b \iff a \lor b = b$).

**Esempio Primario (Pagina 23):**
$(\mathcal{P}(S), \cap, \cup, (\cdot)^c, \emptyset, S)$ è l'algebra di Boole per eccellenza.
*   Operazione unaria $'$: $A' = S \setminus A$ (complemento insiemistico).

> [!IMPORTANT] Teorema di Rappresentazione di Stone per Algebre di Boole Finite (Pagina 23)
> Ogni algebra di Boole **finita** $(A, \land, \lor, ', 0, 1)$ è isomorfa all'algebra di Boole $(\mathcal{P}(S), \cap, \cup, (\cdot)^c, \emptyset, S)$ per qualche insieme finito $S$.
> (Questo è essenzialmente lo stesso teorema visto per i reticoli booleani finiti, ma formulato per le algebre).

---

## 5. Anelli Booleani (Pagine 24-26)

Ora colleghiamo questi concetti con gli anelli!

> [!NOTE] Definizione: Anello Booleano
> Un **anello** $(A, +, \cdot)$ (solitamente unitario, cioè con un'identità moltiplicativa $1_A$) si dice **booleano** se ogni suo elemento è **idempotente**, cioè:
> $$
> a^2 = a \cdot a = a \quad \text{per ogni } a \in A
> $$

**Proprietà Fondamentali degli Anelli Booleani (Pagina 24):**
Se $(A,+, \cdot)$ è un anello booleano:
1.  **$a+a = 0$ (elemento nullo dell'addizione) per ogni $a \in A$**.
    Questo significa che ogni elemento è il suo opposto additivo ($a = -a$).
    L'anello ha **caratteristica 2**.
    *Dimostrazione (come negli appunti):*
    $(a+b)^2 = a+b$. Ma $(a+b)^2 = a^2 + ab + ba + b^2 = a + ab + ba + b$.
    Quindi $a+b = a + ab + ba + b$. Semplificando $a$ e $b$, otteniamo $ab+ba = 0$.
    Questo vale per ogni $a,b$. Se $b=a$, allora $a \cdot a + a \cdot a = 0$, cioè $a^2+a^2=0$, quindi $a+a=0$.
    (Un'altra derivazione più diretta: $(2a)^2 = 2a$. D'altra parte $(2a)^2 = (a+a)^2 = a+a = 2a$. Ma anche $(2a)^2 = (2a)(2a) = 4a^2 = 4a$. Quindi $2a=4a \implies 2a=0$.)
    L'appunto (pag. 24) parte da $(2a)=(a+a)=0 \implies a=-a$. Poi $2a=(2a)^2 = 4a^2=4a \implies 2a=0 \quad \forall a \in A$. (corretto: $2a=0$).
2.  L'anello booleano è **commutativo** (cioè $ab=ba$ per ogni $a,b \in A$).
    *Dimostrazione (come negli appunti):*
    Abbiamo visto sopra che $ab+ba=0$. Poiché $ba = -ba$ (dalla proprietà $x+x=0 \implies x=-x$), allora $ab - ba = 0$, quindi $ab=ba$.

**Esempio Principale (Pagina 25):**
Sia $S$ un insieme. L'insieme delle parti $\mathcal{P}(S)$ con le operazioni:
*   $+$ : Differenza Simmetrica $\Delta$. ($X \Delta Y = (X \setminus Y) \cup (Y \setminus X)$)
*   $\cdot$ : Intersezione $\cap$. ($X \cap Y$)
forma un anello booleano $(\mathcal{P}(S), \Delta, \cap)$.
*   L'elemento $0$ dell'anello è $\emptyset$. ($X \Delta \emptyset = X$).
*   L'elemento $1$ dell'anello è $S$. ($X \cap S = X$).
*   Verifichiamo l'idempotenza: $A^2 = A \cap A = A$. Sì!
L'appunto dice: "CNO se considero $(\mathcal{P}(S), \Delta, \cup)$ non vale la distributività". Qui si riferisce alla distributività di $\cup$ rispetto a $\Delta$, che non è una delle leggi degli anelli. L'anello è $(\mathcal{P}(S), \Delta, \cap)$. La distributività richiesta è $\cap$ su $\Delta$: $A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$. Questa è vera.

> [!IMPORTANT] Teorema di Rappresentazione per Anelli Booleani Finiti (Pagina 26)
> Ogni anello booleano **finito** $(A, +, \cdot)$ è isomorfo a un anello $(\mathcal{P}(S), \Delta, \cap)$ per qualche insieme finito $S$.
> (Se $A$ non è finito, è isomorfo a un sottoanello di $(\mathcal{P}(S), \Delta, \cap)$).

---

## 6. Collegamenti Strutturali: Da Reticoli ad Anelli (Pagine 27-29)

Possiamo costruire un anello booleano a partire da un reticolo booleano!

Sia $(L, \land, \lor, ', 0, 1)$ un reticolo booleano. Definiamo le operazioni di anello $(L, +, \cdot)$:
*   **Prodotto ($\cdot$):** $a \cdot b = a \land b$
    *   Questa operazione è associativa e commutativa (ereditato da $\land$).
    *   L'elemento $1_L$ (massimo del reticolo) è l'unità per il prodotto: $a \cdot 1_L = a \land 1_L = a$.
    *   $(L, \cdot)$ è un monoide commutativo con unità $1_L$.
*   **Somma ($+$):** $a+b = (a \land b') \lor (b \land a')$
    *   Questa è la **differenza simmetrica** espressa con le operazioni del reticolo.
    *   $a \land b'$ significa "$a$ ma non $b$". $b \land a'$ significa "$b$ ma non $a$".
    *   L'unione $(\lor)$ di queste due parti dà $a+b$.

**Verifichiamo alcune proprietà dell'anello (Pagine 28):**
1.  **Elemento nullo per la somma:** È $0_L$ (minimo del reticolo).
    $a + 0_L = (a \land 0_L') \lor (0_L \land a')$
    Sappiamo che $0_L' = 1_L$.
    $a + 0_L = (a \land 1_L) \lor (0_L \land a') = a \lor 0_L = a$. Sì!
2.  **$a+a = 0_L$ (ogni elemento è opposto di sé stesso):**
    $a+a = (a \land a') \lor (a \land a') = 0_L \lor 0_L = 0_L$. Sì!
3.  **Idempotenza per il prodotto:** $a \cdot a = a \land a = a$. (Questo era già una proprietà di $\land$).
    Quindi, $(L, +, \cdot)$ è un anello booleano.

L'appunto a pagina 28 verifica $a \cdot (b+c) = a \cdot b + a \cdot c$ (distributività del prodotto sulla somma):
$a \land ((b \land c') \lor (c \land b')) \neq (a \land b) + (a \land c)$.
Attenzione! La riga sopra sembra indicare che NON è uguale, il che sarebbe un problema. Deve essere uguale.
$a \cdot (b+c) = a \land ((b \land c') \lor (c \land b'))$.
Per la distributività di $\land$ su $\lor$ nel reticolo:
$= (a \land (b \land c')) \lor (a \land (c \land b'))$
$= ((a \land b) \land c') \lor ((a \land c) \land b')$.
D'altra parte:
$a \cdot b + a \cdot c = (a \land b) + (a \land c)$.
Sia $X = a \land b$ e $Y = a \land c$.
$X+Y = (X \land Y') \lor (Y \land X')$.
$X \land Y' = (a \land b) \land (a \land c)' = (a \land b) \land (a' \lor c')$.
$Y \land X' = (a \land c) \land (a \land b)' = (a \land c) \land (a' \lor b')$.
Questa uguaglianza è una proprietà nota e si può dimostrare (anche se è un po' laboriosa).

**Relazione d'Ordine nell'Anello Booleano (Pagina 29):**
Se partiamo da un anello booleano $(A, +, \cdot)$, come possiamo recuperare la relazione d'ordine del reticolo booleano associato?
$$
a \le b \iff a \cdot b = a
$$
Ricorda che $a \cdot b = a \land b$. Quindi $a \le b \iff a \land b = a$, che è una delle definizioni standard di $\le$ in un reticolo.

*   Se $a \le b$ e $b \le a$, allora $a \cdot b = a$ e $b \cdot a = b$. Poiché $\cdot$ è commutativa, $a=b$. (Antisimmetria)
*   Se $a \le b$ e $b \le c$, allora $a \cdot b = a$ e $b \cdot c = b$.
    $a \cdot c = (a \cdot b) \cdot c = a \cdot (b \cdot c) = a \cdot b = a$. Quindi $a \le c$. (Transitività)

---

## Riepilogo della Lezione: Punti Chiave

> [!SUMMARY] Cosa abbiamo imparato oggi:
> *   Un **sottoanello** è un sottoinsieme di un anello che è esso stesso un anello con le stesse operazioni.
> *   Un **reticolo** è un insieme parzialmente ordinato dove ogni coppia di elementi ha un estremo superiore (join $\lor$) e un estremo inferiore (meet $\land$).
> *   Il **Principio di Dualità** ci permette di ottenere nuovi teoremi validi scambiando $\le/\ge$ e $\land/\lor$.
> *   I reticoli possono essere **limitati** (con $0$ e $1$), **complementati** (ogni elemento ha un complemento), e **distributivi** (le operazioni $\land, \lor$ si distribuiscono l'una sull'altra).
> *   Un reticolo è distributivo se e solo se non contiene sottoreticoli $M_3$ (diamante) o $N_5$ (pentagono).
> *   Nei reticoli distributivi e limitati, il complemento (se esiste) è **unico**.
> *   Un **reticolo booleano** è distributivo e complementato. $(\mathcal{P}(S), \subseteq)$ è l'esempio fondamentale. I reticoli booleani finiti sono isomorfi a $\mathcal{P}(S)$ con $|L|=2^{|S|}$.
> *   Un'**algebra di Boole** è la struttura algebrica $(A, \land, \lor, ', 0, 1)$ che cattura le proprietà dei reticoli booleani.
> *   Un **anello booleano** è un anello $(A,+, \cdot)$ dove $a^2=a$ per ogni $a$. Questo implica che $a+a=0$ (caratteristica 2) e l'anello è commutativo. $(\mathcal{P}(S), \Delta, \cap)$ è l'esempio chiave.
> *   Esiste una stretta **corrispondenza** tra reticoli booleani, algebre di Boole e anelli booleani. Possiamo definire le operazioni dell'uno a partire dall'altro.

---

## Domande per Te! (Spunti di Riflessione)

1.  Prova a pensare a un altro esempio di sottoanello, magari usando i numeri interi o i polinomi. Quali condizioni devi verificare?
2.  Riguarda l'esercizio sulla relazione $(a,b) \le_\sigma (c,d) \iff (3^a \cdot 7^b) \text{ divide } (3^c \cdot 7^d)$.
    *   È un ordine parziale?
    *   È un ordine totale? (Suggerimento: pensa a $(2,0)$ e $(0,1)$ cioè $3^2=9$ e $7^1=7$. $9$ divide $7$? $7$ divide $9$?)
    *   Se è un reticolo, come sono definiti $meet$ e $join$?
3.  Disegna il diagramma di Hasse del reticolo dei divisori di 12 ($D_{12}$). È distributivo? È booleano?
4.  Nell'anello booleano $(\mathcal{P}(S), \Delta, \cap)$, se $S=\{1,2,3\}$, prendi $A=\{1,2\}$ e $B=\{2,3\}$. Calcola $A+B$ e $A \cdot B$.
5.  Qual è la cosa più sorprendente o interessante che hai imparato oggi sui reticoli o sulle strutture booleane? C'è qualcosa che ti ricorda un concetto musicale o di un'altra tua passione?

#tag/algebra #tag/algebraavanzata #tag/lezione #tag/anelli #tag/sottoanelli #tag/reticoli #tag/dualità #tag/reticolibimitati #tag/reticolicomplementati #tag/reticolidistributivi #tag/M3N5 #tag/reticolibooleani #tag/algebreBoole #tag/anelliBooleani #tag/teoremiRappresentazione