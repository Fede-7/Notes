# Lezione 8: Cancellabilità, Anelli, Domini, Campi, Spazi Vettoriali, Permutazioni

**Data:** 04/04/2025 (come da note)
**Argomenti:** Elementi cancellabili (recap, esempi), Anelli (recap, notazione multipli/potenze, proprietà dello zero), Divisori dello zero (recap, esempi), Domini di Integrità, Campi (Corpi), Spazi Vettoriali, Omomorfismi (introduzione), Gruppi di Permutazioni ($S_n$), Esercizi.

#tag/algebraic-structures #tag/rings #tag/integral-domains #tag/fields #tag/vector-spaces #tag/homomorphisms #tag/permutations #tag/symmetric-group #tag/cancellable-element #tag/zero-divisor #tag/algebra-avanzata

---

## 1. Elementi Cancellabili (Recap e Approfondimenti)

Ricordiamo le definizioni da Lezione 7:
Sia $(S, *)$ una struttura con operazione binaria. Un elemento $a \in S$ è:
*   **Cancellabile a sinistra** se: $\forall b, c \in S, \quad a * b = a * c \implies b = c$.
*   **Cancellabile a destra** se: $\forall b, c \in S, \quad b * a = c * a \implies b = c$.
*   **Cancellabile** (bilatero) se è cancellabile sia a sinistra sia a destra.

*   **Esempio $(\mathbb{R}^2, \cdot)$ con $(x_1, x_2) \cdot (y_1, y_2) = (x_1y_1, x_2y_2)$ (Pag 1):**
    *   L'elemento $(1, 0)$ è cancellabile?
    *   Proviamo a destra: $(x_1, x_2) * (1, 0) = (x_1 \cdot 1, x_2 \cdot 0) = (x_1, 0)$.
    *   Consideriamo $(2, 1) * (1, 0) = (2, 0)$.
    *   Consideriamo $(2, 2) * (1, 0) = (2, 0)$.
    *   Abbiamo $(2, 1) * (1, 0) = (2, 2) * (1, 0)$, ma $(2, 1) \neq (2, 2)$.
    *   Quindi $(1, 0)$ **non è cancellabile a destra**. (E analogamente, $(0, 1)$ non è cancellabile a sinistra).

*   **Esempio $(\mathbb{Z}, *)$ con $x * y = x |y|$ (Pag 2-5):**
    *   **Associatività:**
        *   $a * (b * c) = a * (b|c|) = a |b|c|| = a \cdot |b| \cdot |c|$ (poiché $|b| \ge 0$, $|b|c|| = |b||c|$).
        *   $(a * b) * c = (a|b|) * c = (a|b|) |c| = a \cdot |b| \cdot |c|$.
        *   **SÌ, è associativa.** Quindi $(\mathbb{Z}, *)$ è un semigruppo.
    *   **Commutatività?**
        *   $1 * (-1) = 1 |-1| = 1 \cdot 1 = 1$.
        *   $(-1) * 1 = (-1) |1| = (-1) \cdot 1 = -1$.
        *   Poiché $1 \neq -1$. **NO, non è commutativa.**
    *   **Elemento Neutro?**
        *   Neutro a destra $u$: $a * u = a \implies a|u| = a$. Questo vale per ogni $a$ se $|u|=1$, cioè $u=1$ o $u=-1$.
        *   Neutro a sinistra $w$: $w * a = a \implies w|a| = a$. Se $a=1$, $w|1|=1 \implies w=1$. Se $a=-1$, $w|-1|= -1 \implies w=-1$. Non esiste un $w$ unico che funzioni per tutti gli $a$.
        *   **Conclusione:** Esistono elementi neutri a destra ($1$ e $-1$), ma non esiste un elemento neutro (né a sinistra né bilatero). Non è un monoide.
    *   **Elementi Cancellabili?**
        *   A destra: $b * a = c * a \implies b|a| = c|a|$. Se $a \neq 0$, allora $|a| \neq 0$, possiamo dividere per $|a|$ (in $\mathbb{Q}$, ma dato che $b,c$ sono interi, l'uguaglianza vale anche in $\mathbb{Z}$) ottenendo $b=c$. Quindi **ogni $a \neq 0$ è cancellabile a destra**.
        *   A sinistra: $a * b = a * c \implies a|b| = a|c|$. Se $a \neq 0$, possiamo dividere per $a$, ottenendo $|b|=|c|$. Questo **non** implica $b=c$. Esempio: $a=1$, $b=1$, $c=-1$. $1*1 = 1|1|=1$. $1*(-1) = 1|-1|=1$. Quindi $1*1 = 1*(-1)$ ma $1 \neq -1$. **Solo $a=0$ non è cancellabile a sinistra, ma gli $a \neq 0$ non garantiscono la cancellabilità.** Nessun elemento è cancellabile a sinistra (tranne forse casi banali da verificare).

*   **Relazione Invertibile $\implies$ Cancellabile (Recap, Pag 5-6):**
    *   In un monoide $(S, *, u)$, se $a$ è invertibile (simmetrizzabile), allora $a$ è cancellabile.
    *   **Dimostrazione (Pag 6):** Se $a*b = a*c$, moltiplichiamo a sinistra per l'inverso $a'$: $a'*(a*b) = a'*(a*c) \implies (a'*a)*b = (a'*a)*c \implies u*b = u*c \implies b=c$. (Analogo per destra).
    *   **Viceversa NON vale (Pag 7):** In $(\mathbb{Z}, \cdot)$, ogni $a \neq 0$ è cancellabile, ma gli unici invertibili sono $1, -1$.

---

## 2. Anelli: Proprietà e Divisori dello Zero

*   **Definizione Anello (Recap, Pag 7):** $(A, +, \cdot)$ è un anello se:
    1.  $(A, +)$ è Gruppo Abeliano (associativa, commutativa, neutro $0_A$, opposto $-a$).
    2.  $(A, \cdot)$ è Semigruppo (associativa).
    3.  Proprietà Distributive (sx e dx).

*   **Notazione Multipli e Potenze (Pag 8):** In un anello A:
    *   $n \cdot a = a + \dots + a$ (n volte) per $n \in \mathbb{N}, n>0$.
    *   $0 \cdot a = 0_A$.
    *   $(-n) \cdot a = -(n \cdot a)$.
    *   Se l'anello è unitario (con unità $1_A$):
        *   $a^n = a \cdot \dots \cdot a$ (n volte) per $n \in \mathbb{N}, n>0$.
        *   $a^0 = 1_A$ (per $a \neq 0_A$, a volte anche per $a=0_A$ a seconda delle convenzioni).

*   **Proprietà dello Zero (Pag 11):** In ogni anello $A$:
    $$ \forall a \in A, \quad a \cdot 0_A = 0_A \cdot a = 0_A $$
    *   **Dimostrazione:** $a \cdot 0_A = a \cdot (0_A + 0_A) = a \cdot 0_A + a \cdot 0_A$ (distributività). Poiché $(A, +)$ è un gruppo, ogni elemento è cancellabile rispetto a $+$. Cancellando $a \cdot 0_A$ da entrambi i lati, otteniamo $0_A = a \cdot 0_A$. (Dimostrazione analoga per $0_A \cdot a$).

*   **Divisori dello Zero (Recap, Pag 9-10):**
    *   $a \in A, a \neq 0_A$ è **divisore dello zero** se $\exists b \in A, b \neq 0_A$ tale che $a \cdot b = 0_A$ o $b \cdot a = 0_A$.
    *   Equivalenza: $a \neq 0_A$ è divisore dello zero $\iff$ $a$ non è cancellabile rispetto a $\cdot$.
    *   **Esempio $(\mathbb{Z}^2, +, \cdot)$ con prodotto componente per componente (Pag 9):**
        *   $0_{\mathbb{Z}^2} = (0, 0)$.
        *   Sia $a = (0, 1) \neq (0, 0)$. Sia $b = (1, 0) \neq (0, 0)$.
        *   $a \cdot b = (0, 1) \cdot (1, 0) = (0 \cdot 1, 1 \cdot 0) = (0, 0) = 0_{\mathbb{Z}^2}$.
        *   Quindi $(0, 1)$ e $(1, 0)$ sono divisori dello zero.
    *   **Esempio Matrici (Pag 12):** In $(M_2(\mathbb{R}), +, \cdot)$:
        *   $$ A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \neq O $$, $$ B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \neq O $$.
        *   $$ A \cdot B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O $$.
        *   Quindi $A$ e $B$ sono divisori dello zero. (In generale, le matrici quadrate con determinante nullo sono divisori dello zero, tranne la matrice nulla stessa).

[[Anello (matematica)]] [[Divisore dello zero]]

---

## 3. Esercizi Proposti (come da note e suggerimento)

> [!EXERCISE] Esercizio 1 (Pag 13 - Verifica Associatività)
> Verificare se vale o meno l'associatività per le seguenti operazioni su $\mathbb{Z}$:
> 1.  $a * b = a + |b|$
> 2.  $a \perp b = |a| + |b|$
> 3.  $a \circ b = |a + b|$
> 4.  $a \star b = -|a \cdot b|$

> [!EXERCISE] Esercizio 2 (Pag 14 - Divisori Zero in $\mathbb{Z}^{\mathbb{Z}}$)
> Determinare gli eventuali divisori dello zero nell'anello $(\mathbb{Z}^{\mathbb{Z}}, +, \cdot)$, dove $+$ e $\cdot$ sono definiti puntualmente: $(f+g)(x) = f(x)+g(x)$ e $(f \cdot g)(x) = f(x)g(x)$. L'elemento neutro additivo è la funzione costante $cost_0(x)=0$.
> *Suggerimento: Una funzione $f \neq cost_0$ è divisore dello zero se esiste $g \neq cost_0$ tale che $f \cdot g = cost_0$. Cosa significa $f(x)g(x)=0$ per ogni $x$?*

> [!EXERCISE] Esercizio 3 (Pag 15 - Stabilità Funzioni Costanti)
> Sia $T = \{ f \in \mathbb{Z}^{\mathbb{Z}} \mid f \text{ è costante} \}$. Verificare che $T$ è stabile (chiuso) rispetto a $+$ e $\cdot$ in $\mathbb{Z}^{\mathbb{Z}}$. È un sottoanello?

> [!EXERCISE] Esercizio 4 (Pag 15 - Studio Struttura $\mathbb{Z}$)
> Studiare la struttura $(\mathbb{Z}, *)$ dove $a * b = a + b + 4ab$.
> *   Verificare associatività e commutatività.
> *   Cercare l'eventuale elemento neutro.
> *   Determinare gli eventuali elementi invertibili (simmetrici).
> *   È un monoide? È un gruppo?

> [!EXERCISE] Esercizio 5 (Pag 16-18 - Studio Struttura $\mathbb{Q}^2$)
> Studiare la struttura $(\mathbb{Q}^2, *)$ dove $(x_1, x_2) * (y_1, y_2) = (x_1y_1 + x_2y_2, 3x_2y_2)$.
> *   Verificare se vale la proprietà associativa.
> *   Verificare se è commutativa.
> *   Cercare l'eventuale elemento neutro.
> *   (Se è un monoide) Determinare gli eventuali elementi invertibili.
> *   È un semigruppo? Monoide? Gruppo?
> *   Considerare la stabilità del sottoinsieme $T = \mathbb{Q} \times \{0\}$.

> [!EXERCISE] Esercizio 6 (Pag 19-20 - Studio Struttura $\mathbb{Q}^3$ e Anello)
> Studiare la struttura $(\mathbb{Q}^3, *)$ dove $(x_1, x_2, x_3) * (y_1, y_2, y_3) = (x_1y_1, x_2y_1 + x_3y_2, x_3y_3)$.
> *   Verificare se è associativa.
> *   Verificare se è commutativa.
> *   Cercare l'eventuale elemento neutro.
> *   (Se è un monoide) Determinare gli eventuali elementi invertibili.
> *   È un semigruppo? Monoide? Gruppo?
>
> **Verifica Anello (Suggerimento Leonardo):** Sia $+$ la somma componente per componente in $\mathbb{Q}^3$. Verificare se $(\mathbb{Q}^3, +, *)$ è un anello.
> *   Verificare che $(\mathbb{Q}^3, +)$ sia gruppo abeliano (è standard).
> *   Verificare che $(\mathbb{Q}^3, *)$ sia semigruppo (associatività verificata sopra).
> *   Verificare le **proprietà distributive**:
>     *   $X * (Y + Z) = (X * Y) + (X * Z)$ ?
>     *   $(Y + Z) * X = (Y * X) + (Z * X)$ ?
>     (dove $X=(x_1,x_2,x_3)$, $Y=(y_1,y_2,y_3)$, $Z=(z_1,z_2,z_3)$).

> [!EXERCISE] Esercizio 7 (Pag 21 - Stabilità Sottoinsiemi $\mathbb{Z}$)
> Nella struttura $(\mathbb{Z}, *)$ con $a * b = a|b|$, verificare quali dei seguenti sottoinsiemi sono stabili:
> *   $P = \{ 2n \mid n \in \mathbb{Z} \}$ (Pari)
> *   $D = \{ 2n+1 \mid n \in \mathbb{Z} \}$ (Dispari)
> *   $S = \{ n \in \mathbb{Z} \mid n < 0 \}$ (Negativi)
> *   $L = \{ n \in \mathbb{Z} \mid n > 0 \}$ (Positivi)

> [!EXERCISE] Esercizio 8 (Pag 22 - Studio Strutture $\mathbb{Z}$)
> Studiare le strutture $(\mathbb{Z}, \perp)$ con $a \perp b = 2ab - a - b$ e $(\mathbb{Z}, \circ)$ con $a \circ b = a + b + 2ab$.
> *   Verificare associatività, commutatività.
> *   Cercare elemento neutro.
> *   Determinare elementi invertibili.

---

## 4. Omomorfismi tra Strutture Algebriche

Una funzione che "preserva la struttura".

*   **Definizione (Pag 22):** Siano $(S, *)$ e $(T, \perp)$ due strutture algebriche con operazioni binarie. Una funzione $f: S \to T$ si dice **omomorfismo** di $(S, *)$ in $(T, \perp)$ se:
    $$ \forall a, b \in S, \quad f(a * b) = f(a) \perp f(b) $$
    *   **Spiegazione:** Applicare l'operazione in $S$ e poi mappare il risultato in $T$ tramite $f$ dà lo stesso risultato che mappare prima $a$ e $b$ in $T$ tramite $f$ e poi applicare l'operazione di $T$.

*   **Esempi (Pag 23-26):**
    *   $f: (\mathbb{N}, +) \to (\mathbb{N}, \cdot)$ con $f(a) = 2^a$.
        *   Verifichiamo $f(a+b) = f(a) \cdot f(b)$.
        *   $f(a+b) = 2^{a+b}$.
        *   $f(a) \cdot f(b) = 2^a \cdot 2^b = 2^{a+b}$.
        *   **SÌ, è un omomorfismo.**
    *   $f: (\mathbb{N}, +) \to (\mathbb{N}, +)$ con $f(a) = 2^a$.
        *   Verifichiamo $f(a+b) = f(a) + f(b)$.
        *   $f(a+b) = 2^{a+b}$.
        *   $f(a) + f(b) = 2^a + 2^b$.
        *   $2^{a+b} \neq 2^a + 2^b$ in generale (es. $a=1, b=1 \implies 2^2 = 4 \neq 2^1+2^1=4$. Funziona solo in questo caso? No. $a=1, b=2 \implies 2^3=8 \neq 2^1+2^2=2+4=6$).
        *   **NO, non è un omomorfismo.**
    *   $f: (\mathbb{Q}^2, \cdot) \to (M_{2,2}(\mathbb{Q}), \cdot)$ con $f(x_1, x_2) = \begin{pmatrix} x_1 & 0 \\ 0 & x_2 \end{pmatrix}$.
        *   Operazione in $\mathbb{Q}^2$: $(x_1, x_2) \cdot (y_1, y_2) = (x_1y_1, x_2y_2)$.
        *   Operazione in $M_{2,2}(\mathbb{Q})$: Prodotto righe per colonne.
        *   Verifichiamo $f((x_1, x_2) \cdot (y_1, y_2)) = f(x_1, x_2) \cdot f(y_1, y_2)$.
        *   $f((x_1y_1, x_2y_2)) = \begin{pmatrix} x_1y_1 & 0 \\ 0 & x_2y_2 \end{pmatrix}$.
        *   $f(x_1, x_2) \cdot f(y_1, y_2) = \begin{pmatrix} x_1 & 0 \\ 0 & x_2 \end{pmatrix} \cdot \begin{pmatrix} y_1 & 0 \\ 0 & y_2 \end{pmatrix} = \begin{pmatrix} (x_1y_1+0) & (0+0) \\ (0+0) & (0+x_2y_2) \end{pmatrix} = \begin{pmatrix} x_1y_1 & 0 \\ 0 & x_2y_2 \end{pmatrix}$.
        *   **SÌ, è un omomorfismo.**
    *   $g: (\mathbb{Q}^2, \cdot) \to (M_{2,2}(\mathbb{Q}), \cdot)$ con $g(x_1, x_2) = \begin{pmatrix} x_1 & x_2 \\ 0 & 0 \end{pmatrix}$.
        *   Verifichiamo $g((x_1, x_2) \cdot (y_1, y_2)) = g(x_1, x_2) \cdot g(y_1, y_2)$.
        *   $g((x_1y_1, x_2y_2)) = \begin{pmatrix} x_1y_1 & x_2y_2 \\ 0 & 0 \end{pmatrix}$.
        *   $g(x_1, x_2) \cdot g(y_1, y_2) = \begin{pmatrix} x_1 & x_2 \\ 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} y_1 & y_2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} (x_1y_1+0) & (x_1y_2+0) \\ (0+0) & (0+0) \end{pmatrix} = \begin{pmatrix} x_1y_1 & x_1y_2 \\ 0 & 0 \end{pmatrix}$.
        *   Le matrici risultato non sono uguali in generale (se $x_2y_2 \neq x_1y_2$).
        *   **NO, non è un omomorfismo.**
    *   $g: (\mathbb{Q}^2, +) \to (M_{2,2}(\mathbb{Q}), +)$ con $g(x_1, x_2) = \begin{pmatrix} x_1 & x_2 \\ 0 & 0 \end{pmatrix}$.
        *   Verifichiamo $g((x_1, x_2) + (y_1, y_2)) = g(x_1, x_2) + g(y_1, y_2)$.
        *   $g((x_1+y_1, x_2+y_2)) = \begin{pmatrix} x_1+y_1 & x_2+y_2 \\ 0 & 0 \end{pmatrix}$.
        *   $g(x_1, x_2) + g(y_1, y_2) = \begin{pmatrix} x_1 & x_2 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} y_1 & y_2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} x_1+y_1 & x_2+y_2 \\ 0 & 0 \end{pmatrix}$.
        *   **SÌ, è un omomorfismo** (tra strutture additive).

[[Omomorfismo]]

---

## 5. Domini di Integrità e Campi

Anelli con proprietà aggiuntive desiderabili.

*   **Dominio di Integrità (Pag 27):** Un anello $(A, +, \cdot)$ è un Dominio di Integrità se soddisfa:
    1.  $A$ è **commutativo**.
    2.  $A$ è **unitario** con $1_A \neq 0_A$.
    3.  $A$ è **privo di divisori dello zero** (diversi da $0_A$).
        *   Equivalente a: $\forall a, b \in A, a \cdot b = 0_A \implies (a = 0_A \lor b = 0_A)$.
        *   Equivalente a: Ogni elemento $a \neq 0_A$ è cancellabile rispetto a $\cdot$.

*   **Esempi:** $(\mathbb{Z}, +, \cdot)$, $(\mathbb{Q}, +, \cdot)$, $(\mathbb{R}, +, \cdot)$, $(\mathbb{C}, +, \cdot)$ sono domini di integrità.
*   **Controesempio $(P(S), \Delta, \cap)$ (Pag 28):**
    *   È commutativo e unitario (unità $S$).
    *   Ma se $|S| \ge 2$, ha divisori dello zero (tutti i sottoinsiemi propri non vuoti).
    *   Quindi **non** è un dominio di integrità (a meno che $|S|=1$).

[[Dominio di integrità]]

*   **Campo (Corpo Commutativo) (Pag 29):** Un anello $(K, +, \cdot)$ è un Campo (in italiano spesso si usa "Campo" per indicare un corpo commutativo) se:
    1.  $K$ è un **anello commutativo unitario** con $1_K \neq 0_K$.
    2.  **Ogni elemento non nullo ha un inverso moltiplicativo:** $(K^*, \cdot)$ è un gruppo abeliano, dove $K^* = K \setminus \{0_K\}$.

*   **Definizione alternativa (Corpo):** Un anello $(K, +, \cdot)$ è un Corpo se $(K^*, \cdot)$ è un gruppo. Se $\cdot$ è anche commutativa, è un Campo.

*   **Relazione:** Un Campo è sempre un Dominio di Integrità. (Se $a \cdot b = 0_K$ e $a \neq 0_K$, allora $a$ ha inverso $a^{-1}$. Moltiplicando per $a^{-1}$ si ottiene $a^{-1}ab = a^{-1}0_K \implies 1_K b = 0_K \implies b = 0_K$. Quindi non ci sono divisori dello zero).

*   **Esempi di Campi:** $(\mathbb{Q}, +, \cdot)$, $(\mathbb{R}, +, \cdot)$, $(\mathbb{C}, +, \cdot)$.
*   **Controesempio:** $(\mathbb{Z}, +, \cdot)$ è un dominio di integrità ma non un campo (mancano gli inversi moltiplicativi per elementi diversi da 1, -1).

[[Campo (matematica)]] [[Corpo (matematica)]]

*   **Teorema di Wedderburn (Pag 33):** Ogni corpo finito è un campo (cioè il prodotto è automaticamente commutativo).

---

## 6. Spazi Vettoriali (Cenno)

Struttura fondamentale dell'algebra lineare.

*   **Definizione (Pag 29-30):** Sia $K$ un campo. Un **K-spazio vettoriale** (o spazio vettoriale su K) è una struttura $(V, +, \cdot_{ext})$ dove:
    1.  $(V, +)$ è un **Gruppo Abeliano** (gli elementi di V sono chiamati vettori, $+$ è la somma vettoriale, $0_V$ è il vettore nullo).
    2.  $\cdot_{ext}: K \times V \to V$ è un'**operazione esterna** (prodotto per scalare) che associa a uno scalare $\alpha \in K$ e un vettore $v \in V$ un vettore $\alpha \cdot_{ext} v \in V$.
    3.  Valgono le seguenti **proprietà di compatibilità** ($\forall \alpha, \beta \in K, \forall u, v \in V$):
        *   i) $\alpha \cdot_{ext} (\beta \cdot_{ext} v) = (\alpha \cdot_K \beta) \cdot_{ext} v$ (Associatività mista)
        *   ii) $(\alpha +_K \beta) \cdot_{ext} v = (\alpha \cdot_{ext} v) +_V (\beta \cdot_{ext} v)$ (Distributività rispetto somma scalari)
        *   iii) $\alpha \cdot_{ext} (u +_V v) = (\alpha \cdot_{ext} u) +_V (\alpha \cdot_{ext} v)$ (Distributività rispetto somma vettori)
        *   iv) $1_K \cdot_{ext} v = v$ (Elemento neutro scalare)

*   **Esempi (Pag 31):**
    *   $K^n = \{(x_1, ..., x_n) \mid x_i \in K\}$ con somma vettoriale e prodotto per scalare componente per componente.
    *   $M_{m,n}(K)$ (matrici $m \times n$ a coefficienti in $K$) con somma matriciale e prodotto per scalare.

[[Spazio vettoriale]]

---

## 7. Gruppi di Permutazioni ($S_n$)

Un esempio importante di gruppo non abeliano.

*   Sia $S$ un insieme finito con $|S|=n$. Spesso si prende $S = \{1, 2, ..., n\}$.
*   $B(S) = \{ f: S \to S \mid f \text{ è biettiva} \}$ è l'insieme delle **permutazioni** di $S$.
*   $(B(S), \circ)$ è un gruppo, chiamato **Gruppo Simmetrico** su $n$ elementi, denotato $S_n$.
*   La cardinalità di $S_n$ è $|S_n| = n! = n \cdot (n-1) \cdot \dots \cdot 1$.

*   **Notazione Ciclica (Pag 34-36):**
    *   Una permutazione può essere rappresentata elencando come mappa gli elementi: $$ \begin{pmatrix} 1 & 2 & 3 & \dots & n \\ f(1) & f(2) & f(3) & \dots & f(n) \end{pmatrix} $$
    *   Un **ciclo** $(c_1 c_2 \dots c_k)$ rappresenta la permutazione $\sigma$ tale che $\sigma(c_1)=c_2, \sigma(c_2)=c_3, \dots, \sigma(c_{k-1})=c_k, \sigma(c_k)=c_1$, e $\sigma(x)=x$ per gli elementi $x$ non nel ciclo.
    *   **Teorema (Decomposizione in Cicli Disgiunti, Pag 35):** Ogni permutazione $\sigma \in S_n$ si può scrivere in modo unico (a meno dell'ordine dei cicli) come prodotto (composizione) di cicli disgiunti.
    *   **Esempio:** $$ \sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\ 2 & 4 & 7 & 1 & 5 & 6 & 3 & 9 & 8 \end{pmatrix} $$
        *   $1 \to 2 \to 4 \to 1$. Ciclo: $(1 2 4)$.
        *   $3 \to 7 \to 3$. Ciclo: $(3 7)$.
        *   $5 \to 5$. (Ciclo di lunghezza 1, spesso omesso).
        *   $6 \to 6$. (Ciclo di lunghezza 1, spesso omesso).
        *   $8 \to 9 \to 8$. Ciclo: $(8 9)$.
        *   Decomposizione: $\sigma = (1 2 4)(3 7)(8 9)$.
    *   **Inversa di un Ciclo (Pag 36):** L'inversa del ciclo $(c_1 c_2 \dots c_k)$ si ottiene leggendo gli elementi al contrario: $(c_1 c_k c_{k-1} \dots c_2)$.
        *   Esempio: $(1 7 4 3)^{-1} = (1 3 4 7)$.
    *   **Inversa di un Prodotto di Cicli Disgiunti:** L'inversa del prodotto è il prodotto delle inverse (nello stesso ordine, perché cicli disgiunti commutano).
        *   Esempio: $$ \sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 \\ 7 & 5 & 1 & 3 & 2 & 6 & 4 \end{pmatrix} = (1 7 4 3)(2 5) $$.
        *   $\sigma^{-1} = (1 7 4 3)^{-1} (2 5)^{-1} = (1 3 4 7)(2 5)$.

[[Gruppo simmetrico]] [[Permutazione]] [[Notazione ciclica]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 8
> *   Abbiamo rivisto la **cancellabilità** e la sua relazione (non equivalenza) con l'invertibilità.
> *   Abbiamo definito la notazione per **multipli additivi e potenze moltiplicative** in anelli.
> *   Abbiamo dimostrato che $a \cdot 0_A = 0_A$.
> *   Abbiamo rivisto i **divisori dello zero** e la loro equivalenza con la non-cancellabilità.
> *   Abbiamo introdotto i **Domini di Integrità** (anelli commutativi unitari privi di divisori dello zero).
> *   Abbiamo introdotto i **Campi** (anelli commutativi unitari dove ogni elemento non nullo è invertibile moltiplicativamente).
> *   Abbiamo definito gli **Spazi Vettoriali** su un campo K.
> *   Abbiamo definito gli **Omomorfismi** tra strutture algebriche.
> *   Abbiamo introdotto il **Gruppo Simmetrico $S_n$** (permutazioni), la notazione ciclica, la decomposizione in cicli disgiunti e il calcolo dell'inversa.
> *   Sono stati proposti numerosi **esercizi** per praticare questi concetti.

> [!TIP] Prossimi Passi
> *   Prova a svolgere gli esercizi proposti, in particolare quelli sullo studio delle strutture e sulla verifica delle proprietà (anello, associatività, commutatività, neutro, inversi, divisori dello zero).
> *   Familiarizza con la notazione ciclica delle permutazioni.
> *   Il prossimo passo potrebbe essere approfondire le proprietà dei gruppi (sottogruppi, teorema di Lagrange) o degli anelli (ideali, anelli quoziente).