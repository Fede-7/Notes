# Lezione 8: Semigruppi, Monoidi, Anelli (Divisori Zero), Strutture Varie, Omomorfismi, Permutazioni

**Data:** 04/04/2025 (come da note originali)
**Argomenti:** Semigruppo, Elemento Cancellabile, Esempi ($\mathbb{R}^2$, $\mathbb{Z}$ con $|y|$), Monoide, Elemento Invertibile (Simmetrico), Cancellabile vs Invertibile, Anello (Definizione, Notazioni), Divisori dello Zero (Definizione, Esempi $\mathbb{Z}^2$, Matrici, Teorema vs Cancellabilità), Esercizi Associatività, Anello Funzioni $\mathbb{Z}^\mathbb{Z}$, Esercizio Struttura ($\mathbb{Z}$, $*$), Esempi Strutture ($\mathbb{Q}^2$, $\mathbb{Q}^3$), Omomorfismi (Definizione, Esempi), Dominio Integrità, Corpo, Campo, Spazio Vettoriale (Definizioni), Gruppo Simmetrico $S_n$, Notazione Ciclica, Decomposizione Cicli Disgiunti, Inversa Permutazione.

#tag/semigruppi #tag/monoidi #tag/anelli #tag/divisori-dello-zero #tag/cancellabile-element #tag/invertibile-element #tag/omomorfismi #tag/permutazioni #tag/gruppo-simmetrico #tag/esercizi #tag/algebra-avanzata

---

## 1. Semigruppi e Cancellabilità

*   **Definizione: Semigruppo**
    *   Una coppia $(S, *)$ è un **semigruppo** se $S$ è un insieme non vuoto e $*$ è un'operazione binaria **associativa** su $S$.
    *   Associatività: $(a * b) * c = a * (b * c)$ per ogni $a, b, c \in S$.

*   **Definizione: Elemento Cancellabile**
    *   Sia $(S, *)$ un semigruppo. Un elemento $a \in S$ è:
        *   **Cancellabile a destra** se: $\forall b, c \in S, \quad b * a = c * a \implies b = c$.
        *   **Cancellabile a sinistra** se: $\forall b, c \in S, \quad a * b = a * c \implies b = c$.

*   **Esempio: $(\mathbb{R}^2, *)$ con $(x_1, x_2) * (y_1, y_2) = (x_1 y_1, x_2 y_2)$**
    *   Questa struttura è un semigruppo (associativa).
    *   L'elemento $a = (1, 0)$ **non è cancellabile** (né a destra né a sinistra).
    *   Verifica (destra): Siano $b = (2, 1)$ e $c = (2, 2)$.
        *   $b * a = (2, 1) * (1, 0) = (2 \cdot 1, 1 \cdot 0) = (2, 0)$.
        *   $c * a = (2, 2) * (1, 0) = (2 \cdot 1, 2 \cdot 0) = (2, 0)$.
        *   Abbiamo $b * a = c * a$, ma $b \neq c$. Quindi $(1, 0)$ non è cancellabile a destra.

*   **Esempio: $(\mathbb{Z}, *)$ con $x * y = x |y|$** (Assumendo associatività come da note, anche se dubbia - vedi appunti precedenti)
    *   **Non commutativa:** $1 * (-1) = 1 \neq (-1) * 1 = -1$.
    *   **Elementi neutri a destra:** $u=1$ e $u=-1$ (perché $a|u|=a \implies |u|=1$).
    *   **Nessun elemento neutro a sinistra:** $w|a|=a$ dovrebbe valere per ogni $a$. Se $a=1 \implies w=1$. Ma $1|a|=|a|$, che non è sempre uguale ad $a$.
    *   **Elementi cancellabili a destra:** Tutti gli $a \in \mathbb{Z}$ con $a \neq 0$. (Se $a \neq 0$, $b|a|=c|a| \implies b=c$).
    *   **Nessun elemento cancellabile a sinistra:** $a|b|=a|c| \implies |b|=|c|$, che non implica $b=c$.

[[Semigruppo]] [[Elemento Cancellabile]]

---

## 2. Monoidi e Elementi Invertibili

*   **Definizione: Monoide**
    *   Un **monoide** è un semigruppo $(S, *)$ che possiede un **elemento neutro** $u$ (bilatero: $a*u=u*a=a$).

*   **Definizione: Elemento Invertibile (o Simmetrizzabile)**
    *   Sia $(S, *)$ un monoide con elemento neutro $u$.
    *   Un elemento $a \in S$ è **invertibile** se esiste $\bar{a} \in S$ (detto **inverso** o **simmetrico**) tale che:
        $$ a * \bar{a} = \bar{a} * a = u $$
    *   L'insieme degli elementi invertibili si indica con $\mathcal{U}(S)$.

*   **Teorema: Invertibile $\implies$ Cancellabile**
    *   In un monoide, se un elemento $a$ è invertibile, allora è cancellabile (sia a destra che a sinistra).
    *   *Dimostrazione (sx):* Se $a*b = a*c$, moltiplica a sinistra per $\bar{a}$: $\bar{a}*(a*b) = \bar{a}*(a*c) \implies (\bar{a}*a)*b = (\bar{a}*a)*c \implies u*b = u*c \implies b=c$.

*   **Attenzione: Cancellabile $\not\implies$ Invertibile**
    *   Il viceversa non è vero in generale.
    *   Esempio: $(\mathbb{Z}, \cdot)$ è un monoide con $u=1$.
        *   Gli elementi cancellabili sono tutti gli $a \neq 0$.
        *   Gli elementi invertibili $\mathcal{U}(\mathbb{Z})$ sono solo $\{1, -1\}$.
        *   L'elemento $2$ è cancellabile ma non invertibile in $\mathbb{Z}$.

[[Monoide]] [[Elemento Invertibile]]

---

## 3. Anelli e Divisori dello Zero

*   **Definizione: Anello** (Recap da Lez. 7)
    *   Una struttura $(A, +, \cdot)$ è un **Anello** se:
        1.  $(A, +)$ è un **Gruppo Abeliano** (elemento neutro $0_A$, opposto $-a$).
        2.  $(A, \cdot)$ è un **Semigruppo**.
        3.  **Proprietà Distributive** del prodotto $\cdot$ rispetto alla somma $+$.

*   **Notazioni Comuni:**
    *   $n \cdot a = a + \dots + a$ (n volte)
    *   $a^n = a \cdot \dots \cdot a$ (n volte)
    *   $a^0 = 1_A$ (se l'anello è unitario)
    *   $a \cdot 0_A = 0_A \cdot a = 0_A$

*   **Definizione: Divisore dello Zero**
    *   Sia $(A, +, \cdot)$ un anello.
    *   Un elemento $a \in A$, $a \neq 0_A$, è **divisore dello zero** se esiste $b \in A$, $b \neq 0_A$, tale che:
        $$ a \cdot b = 0_A \quad \text{oppure} \quad b \cdot a = 0_A $$

*   **Esempi di Divisori dello Zero:**
    *   **Anello $(\mathbb{Z}^2, +, \cdot)$** (operazioni componente per componente):
        *   $0_{\mathbb{Z}^2} = (0, 0)$.
        *   $a = (0, 1) \neq (0,0)$, $b = (1, 0) \neq (0,0)$.
        *   $a \cdot b = (0, 1) \cdot (1, 0) = (0 \cdot 1, 1 \cdot 0) = (0, 0)$.
        *   Quindi $(0, 1)$ e $(1, 0)$ sono divisori dello zero.
    *   **Anello $(M_2(\mathbb{R}), +, \cdot)$** (matrici 2x2 reali):
        *   $0_{M_2} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
        *   $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \neq 0_{M_2}$, $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \neq 0_{M_2}$.
        *   $A \cdot B = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
        *   Quindi $A$ e $B$ sono divisori dello zero.

*   **Teorema: Divisore dello Zero $\iff$ Non Cancellabile**
    *   In un anello $(A, +, \cdot)$, un elemento $a \neq 0_A$ è un **divisore dello zero** se e solo se $a$ **non è cancellabile** rispetto al prodotto $\cdot$.
    *   *Dimostrazione ($\implies$):* Se $a$ è divisore, $\exists b \neq 0_A$ t.c. $a \cdot b = 0_A$. Poiché $a \cdot 0_A = 0_A$, abbiamo $a \cdot b = a \cdot 0_A$. Se $a$ fosse cancellabile (sx), allora $b=0_A$, contraddizione.
    *   *Dimostrazione ($\impliedby$):* Se $a$ non è cancellabile (sx), $\exists b \neq c$ t.c. $a \cdot b = a \cdot c$. Allora $a \cdot (b-c) = 0_A$. Posto $d = b-c$, si ha $d \neq 0_A$ e $a \cdot d = 0_A$. Quindi $a$ è divisore dello zero.

[[Anello (matematica)]] [[Divisore dello zero]]

---

## 4. Esercizi e Strutture Algebriche Varie

> [!EXERCISE] Esercizi per Casa (Associatività)
> Verificare se l'operazione binaria $\star$ è associativa nei seguenti casi (controllare se $(a \star b) \star c = a \star (b \star c)$ per ogni $a, b, c$):
>
> 1.  $(\mathbb{Z}, *)$ con $a * b = a + |b|$
> 2.  $(\mathbb{Z}, \perp)$ con $a \perp b = |a| + |b|$
> 3.  $(\mathbb{Z}, \circ)$ con $a \circ b = |a + b|$
> 4.  $(\mathbb{Z}, \star)$ con $a \star b = -|a \cdot b|$

*   **Esempio: Anello delle Funzioni $(\mathbb{Z}^\mathbb{Z}, +, \cdot)$**
    *   $\mathbb{Z}^\mathbb{Z} = \{ f: \mathbb{Z} \to \mathbb{Z} \}$.
    *   Operazioni puntuali: $(f+g)(x) = f(x)+g(x)$, $(f \cdot g)(x) = f(x)g(x)$.
    *   È un **anello commutativo unitario**.
        *   $0_A$ è la funzione $O(x)=0$.
        *   $1_A$ è la funzione $I(x)=1$.
    *   **Ha divisori dello zero:**
        *   Sia $f(x) = 1$ se $x$ pari, $0$ se $x$ dispari.
        *   Sia $g(x) = 0$ se $x$ pari, $1$ se $x$ dispari.
        *   $f \neq O$, $g \neq O$, ma $(f \cdot g)(x) = f(x)g(x) = 0$ per ogni $x$. Quindi $f \cdot g = O$.

*   **Sottostruttura Stabile:** $T = \{ f \in \mathbb{Z}^\mathbb{Z} \mid f \text{ è costante} \}$.
    *   $T$ è **chiuso** rispetto a $+$ e $\cdot$ (somma/prodotto di costanti è costante).
    *   $(T, +, \cdot)$ è un sottoanello, isomorfo a $(\mathbb{Z}, +, \cdot)$.

> [!EXERCISE] Esercizio per Casa (Struttura Algebrica)
> Studia la struttura $(\mathbb{Z}, *)$ dove:
> $$ a * b = a + b + 4ab $$
> Verifica:
> 1.  Associatività
> 2.  Commutatività
> 3.  Esistenza dell'elemento neutro $u$ (risolvi $a*u=a$)
> 4.  Esistenza degli inversi $\bar{a}$ (risolvi $a*\bar{a}=u$) per gli elementi che li possiedono.

*   **Esempio: $(\mathbb{Q}^2, *)$ con $(x_1, x_2) * (y_1, y_2) = (x_1 y_1 + x_2 y_2, 3 x_2 y_2)$**
    *   Associativa (dato).
    *   **Commutativa:** $(x_1 y_1 + x_2 y_2, 3 x_2 y_2) = (y_1 x_1 + y_2 x_2, 3 y_2 x_2)$. **SÌ.**
    *   **Elemento Neutro?** Cerchiamo $u=(u_1, u_2)$ t.c. $(x_1, x_2)*(u_1, u_2)=(x_1, x_2)$.
        *   $(x_1 u_1 + x_2 u_2, 3 x_2 u_2) = (x_1, x_2)$.
        *   Sistema:
            1.  $x_1 u_1 + x_2 u_2 = x_1$
            2.  $3 x_2 u_2 = x_2 \implies u_2 = 1/3$ (per $x_2 \neq 0$)
        *   Sostituendo $u_2=1/3$ in (1): $x_1 u_1 + x_2/3 = x_1 \implies x_1(u_1-1) + x_2/3 = 0$.
        *   Questa deve valere per ogni $x_1, x_2$. Impossibile perché il coefficiente di $x_2$ è $1/3 \neq 0$.
        *   **NON esiste elemento neutro.** (È un semigruppo commutativo).
    *   **Sottostruttura Stabile:** $T = \mathbb{Q} \times \{0\}$.
        *   $(x_1, 0) * (y_1, 0) = (x_1 y_1 + 0, 3 \cdot 0 \cdot 0) = (x_1 y_1, 0) \in T$. **SÌ, è stabile.**

*   **Esempio: $(\mathbb{Q}^3, *)$ con $(x_1, x_2, x_3) * (y_1, y_2, y_3) = (x_1 y_1, x_2 y_1 + x_3 y_2, x_3 y_3)$**
    *   Associativa (dato).
    *   **Non Commutativa:** $(1, 2, 3)*(4, 5, 6) = (4, 23, 18)$ mentre $(4, 5, 6)*(1, 2, 3) = (4, 17, 18)$.
    *   **Elemento Neutro?** Cerchiamo $u=(u_1, u_2, u_3)$ t.c. $(x_1, x_2, x_3)*(u_1, u_2, u_3)=(x_1, x_2, x_3)$.
        *   $(x_1 u_1, x_2 u_1 + x_3 u_2, x_3 u_3) = (x_1, x_2, x_3)$.
        *   Sistema:
            1.  $x_1 u_1 = x_1 \implies u_1 = 1$.
            2.  $x_2 u_1 + x_3 u_2 = x_2$.
            3.  $x_3 u_3 = x_3 \implies u_3 = 1$.
        *   Sostituendo in (2): $x_2(1) + x_3 u_2 = x_2 \implies x_3 u_2 = 0$. Deve valere per ogni $x_3$, quindi $u_2=0$.
        *   Candidato $u = (1, 0, 1)$.
        *   Verifica a sinistra: $(1, 0, 1)*(x_1, x_2, x_3) = (1x_1, 0x_1+1x_2, 1x_3) = (x_1, x_2, x_3)$. OK.
        *   **SÌ, $u=(1, 0, 1)$ è l'elemento neutro.** (È un monoide non commutativo).

---

## 5. Omomorfismi

*   **Definizione: Omomorfismo**
    *   Siano $(S, *)$ e $(T, \perp)$ due strutture algebriche.
    *   Una funzione $f: S \to T$ è un **omomorfismo** se "preserva l'operazione":
        $$ f(a * b) = f(a) \perp f(b) \quad \forall a, b \in S $$

*   **Esempi:**
    1.  $f: (\mathbb{N}, +) \to (\mathbb{N}, \cdot)$, $f(a) = 2^a$.
        *   $f(a+b) = 2^{a+b}$.
        *   $f(a) \cdot f(b) = 2^a \cdot 2^b = 2^{a+b}$. **SÌ, è omomorfismo.**
    2.  $f: (\mathbb{N}, +) \to (\mathbb{N}, +)$, $f(a) = 2^a$.
        *   $f(a+b) = 2^{a+b}$.
        *   $f(a) + f(b) = 2^a + 2^b$. **NO, non è omomorfismo.**
    3.  $f: (\mathbb{Q}^2, \cdot_{comp}) \to (M_{2}(\mathbb{Q}), \cdot_{matr})$, $f(x_1, x_2) = \begin{pmatrix} x_1 & 0 \\ 0 & x_2 \end{pmatrix}$.
        *   $f((x_1, x_2) \cdot (y_1, y_2)) = f(x_1 y_1, x_2 y_2) = \begin{pmatrix} x_1 y_1 & 0 \\ 0 & x_2 y_2 \end{pmatrix}$.
        *   $f(x_1, x_2) \cdot f(y_1, y_2) = \begin{pmatrix} x_1 & 0 \\ 0 & x_2 \end{pmatrix} \cdot \begin{pmatrix} y_1 & 0 \\ 0 & y_2 \end{pmatrix} = \begin{pmatrix} x_1 y_1 & 0 \\ 0 & x_2 y_2 \end{pmatrix}$. **SÌ, è omomorfismo.**
    4.  $g: (\mathbb{Q}^2, \cdot_{comp}) \to (M_{2}(\mathbb{Q}), \cdot_{matr})$, $g(x_1, x_2) = \begin{pmatrix} x_1 & x_2 \\ 0 & 0 \end{pmatrix}$.
        *   $g(x_1 y_1, x_2 y_2) = \begin{pmatrix} x_1 y_1 & x_2 y_2 \\ 0 & 0 \end{pmatrix}$.
        *   $g(x_1, x_2) \cdot g(y_1, y_2) = \begin{pmatrix} x_1 & x_2 \\ 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} y_1 & y_2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} x_1 y_1 & x_1 y_2 \\ 0 & 0 \end{pmatrix}$. **NO, non è omomorfismo.**
    5.  $g: (\mathbb{Q}^2, +) \to (M_{2}(\mathbb{Q}), +)$, $g(x_1, x_2) = \begin{pmatrix} x_1 & x_2 \\ 0 & 0 \end{pmatrix}$.
        *   $g((x_1, x_2) + (y_1, y_2)) = g(x_1+y_1, x_2+y_2) = \begin{pmatrix} x_1+y_1 & x_2+y_2 \\ 0 & 0 \end{pmatrix}$.
        *   $g(x_1, x_2) + g(y_1, y_2) = \begin{pmatrix} x_1 & x_2 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} y_1 & y_2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} x_1+y_1 & x_2+y_2 \\ 0 & 0 \end{pmatrix}$. **SÌ, è omomorfismo.**

> [!EXERCISE] Esercizi per Casa (Operazioni e Omomorfismi)
> Definisci le seguenti operazioni su $\mathbb{Z}$:
> *   $a \perp b = 2ab - a - b$
> *   $a \circ b = a + b + 2ab$
>
> Considera due strutture $(S, *)$ e $(T, \perp)$ e la definizione di omomorfismo $f: S \to T$:
> $$ f(a * b) = f(a) \perp f(b) \quad \forall a, b \in S $$
> (Questo è più un promemoria della definizione che un esercizio specifico da svolgere dalle note).

[[Omomorfismo]]

---

## 6. Domini di Integrità, Campi, Spazi Vettoriali (Cenni)

*   **Definizione: Dominio d'Integrità**
    *   Un anello $(A, +, \cdot)$ è un **dominio d'integrità** se è:
        1.  **Commutativo**
        2.  **Unitario** ($1_A \neq 0_A$)
        3.  **Privo di divisori dello zero**.
    *   Esempi: $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$.
    *   Non Esempi: $\mathbb{Z}^2$, $M_2(\mathbb{R})$, $\mathbb{Z}^\mathbb{Z}$, $(P(S), \Delta, \cap)$ (se $|S| \ge 2$).

*   **Definizione: Corpo e Campo**
    *   Un **corpo** è un anello unitario ($1_K \neq 0_K$) in cui **ogni elemento non nullo è invertibile** rispetto al prodotto ($\mathcal{U}(K) = K \setminus \{0_K\}$).
    *   Un **campo** è un **corpo commutativo**.
    *   Proprietà: Un campo è sempre un dominio d'integrità.
    *   Esempi: $\mathbb{Q}, \mathbb{R}, \mathbb{C}$ sono campi. $\mathbb{Z}$ non è un campo.
    *   **Teorema di Wedderburn (Piccolo):** Ogni corpo finito è un campo (commutativo).

*   **Definizione: Spazio Vettoriale**
    *   Una struttura $(V, +)$ (gruppo abeliano, vettori) su un campo $(K, +, \cdot)$ (scalari) con un'operazione esterna $\cdot_{ext}: K \times V \to V$ (prodotto per scalare) che soddisfa le 4 proprietà note (pseudo-associatività, distributività scalari, distributività vettori, $1_K \cdot v = v$).
    *   Esempi: $K^n$, $M_{m,n}(K)$.

[[Dominio d'integrità]] [[Campo (matematica)]] [[Corpo (matematica)]] [[Spazio Vettoriale]]

---

## 7. Gruppo Simmetrico $S_n$ (Permutazioni)

*   **Definizione: Permutazione e Gruppo Simmetrico**
    *   Sia $S = \{1, 2, \dots, n\}$. Una **permutazione** di $S$ è una funzione biettiva $\sigma: S \to S$.
    *   $S_n = B(S)$ è l'insieme di tutte le permutazioni di $S$.
    *   $(S_n, \circ)$ (con $\circ$ = composizione di funzioni) è un **gruppo**, detto **Gruppo Simmetrico** su $n$ elementi.
    *   $|S_n| = n!$.
    *   È non abeliano per $n \ge 3$.

*   **Notazione a Due Righe:**
    $$ \sigma = \begin{pmatrix} 1 & 2 & \dots & n \\ \sigma(1) & \sigma(2) & \dots & \sigma(n) \end{pmatrix} $$

*   **Notazione Ciclica:**
    *   Un **ciclo** $(a_1 a_2 \dots a_k)$ rappresenta $\sigma(a_1)=a_2, \dots, \sigma(a_{k-1})=a_k, \sigma(a_k)=a_1$, e $\sigma(x)=x$ per $x \notin \{a_1, \dots, a_k\}$.
    *   **Cicli Disgiunti:** Cicli che non hanno elementi in comune.

*   **Teorema: Decomposizione in Cicli Disgiunti**
    *   Ogni permutazione $\sigma \in S_n$ ($\sigma \neq id$) si scrive in modo **unico** (a meno dell'ordine) come **prodotto (composizione) di cicli disgiunti**.

*   **Esempio Decomposizione:** $\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\ 2 & 4 & 7 & 1 & 5 & 6 & 3 & 9 & 8 \end{pmatrix}$
    *   $1 \mapsto 2 \mapsto 4 \mapsto 1 \implies (1 2 4)$
    *   $3 \mapsto 7 \mapsto 3 \implies (3 7)$
    *   $5 \mapsto 5$ (fisso)
    *   $6 \mapsto 6$ (fisso)
    *   $8 \mapsto 9 \mapsto 8 \implies (8 9)$
    *   Quindi $\sigma = (1 2 4)(3 7)(8 9)$.

*   **Inversa di una Permutazione:**
    *   Inverso di un ciclo $(a_1 a_2 \dots a_k)$ è $(a_k \dots a_2 a_1)$.
    *   Inverso di $\sigma = c_1 c_2 \dots c_m$ è $\sigma^{-1} = c_m^{-1} \dots c_2^{-1} c_1^{-1}$.
    *   Se i cicli $c_i$ sono **disgiunti**, allora $\sigma^{-1} = c_1^{-1} c_2^{-1} \dots c_m^{-1}$.
    *   Esempio: $\sigma = (1 7 4 3)(2 5)$. $\sigma^{-1} = (2 5)^{-1} (1 7 4 3)^{-1} = (5 2) (3 4 7 1)$.

[[Gruppo Simmetrico]] [[Permutazione]] [[Notazione Ciclica]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 8
> *   Definito **Semigruppo** e **Elemento Cancellabile**, con esempi.
> *   Definito **Monoide** e **Elemento Invertibile**, visto che Invertibile $\implies$ Cancellabile (ma non viceversa).
> *   Richiamato **Anello** e definito **Divisori dello Zero**, collegandoli alla non-cancellabilità.
> *   Svolti **esercizi** su associatività e studio di strutture algebriche specifiche ($\mathbb{Z}^\mathbb{Z}$, $\mathbb{Z}$ con $a*b=a+b+4ab$, $\mathbb{Q}^2$, $\mathbb{Q}^3$).
> *   Introdotto **Omomorfismo** come funzione che preserva la struttura, con vari esempi.
> *   Definizioni rapide di **Dominio Integrità**, **Corpo**, **Campo**, **Spazio Vettoriale**.
> *   Introdotto il **Gruppo Simmetrico $S_n$** (permutazioni), la **notazione ciclica**, il teorema di **decomposizione in cicli disgiunti** e il calcolo dell'**inversa**.

> [!TIP] Prossimi Passi
> *   Assicurati di saper distinguere Semigruppo, Monoide, Gruppo, Anello, Dominio, Campo.
> *   Esercitati con la cancellabilità e i divisori dello zero.
> *   Prendi confidenza con la notazione ciclica delle permutazioni e la loro composizione/inversione.
> *   Rivedi la definizione di omomorfismo, è un concetto chiave che collega strutture diverse.