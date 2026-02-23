# Lezione 7: Gruppi (Recap), Anelli, Caratteristica, Cancellabilità e Divisori dello Zero

**Data:** 01/04/2025 (come da note)
**Argomenti:** Definizione di Gruppo (recap), Esempi (Abeliani/Non Abeliani), Matrici (notazione, inversa 2x2), Verifica proprietà strutture algebriche, Definizione di Anello, Esempi di Anelli (P(S), Matrici), Anello Commutativo, Anello Unitario, Caratteristica di un Anello, Elementi Cancellabili, Divisori dello Zero.

#tag/algebraic-structures #tag/groups #tag/abelian-groups #tag/rings #tag/matrices #tag/cancellable-element #tag/zero-divisor #tag/characteristic #tag/algebra-avanzata

---

## 1. Gruppi: Definizione ed Esempi (Recap)

*   **Definizione (Pag 1):** Una struttura $(G, *)$ è un **Gruppo** se:
    1.  $*$ è **associativa** (Semigruppo)
    2.  Esiste l'**elemento neutro** $u \in G$ (Monoide)
    3.  **Ogni elemento** $a \in G$ è **invertibile** (o simmetrizzabile) in $G$ (cioè $U(G)=G$).

*   **Esempi (Pag 1, 5):**
    *   **Gruppi Abeliani (Commutativi):**
        *   $(\mathbb{Z}, +)$, $(\mathbb{Q}, +)$, $(\mathbb{R}, +)$, $(\mathbb{C}, +)$
        *   $(\mathbb{Q}^*, \cdot)$, $(\mathbb{R}^*, \cdot)$, $(\mathbb{C}^*, \cdot)$ (dove $X^* = X \setminus \{0\}$)
        *   $(\{1, -1\}, \cdot)$
        *   $(\mathbb{R}^n, +)$ (somma vettoriale)
        *   $(M_{m,n}(\mathbb{R}), +)$ (somma matriciale)
        *   $(P(S), \Delta)$ (differenza simmetrica)
    *   **Gruppi NON Abeliani (Non Commutativi):**
        *   $(B(A) = \{f: A \to A \mid f \text{ biettiva}\}, \circ)$ (Gruppo Simmetrico $S_A$, se $|A| \ge 3$)
        *   $(GL_n(\mathbb{R}) = \{A \in M_n(\mathbb{R}) \mid \det(A) \neq 0\}, \cdot)$ (Gruppo Lineare Generale, se $n \ge 2$)

[[Gruppo (matematica)]] [[Gruppo Abeliano]]

---

## 2. Matrici: Notazione e Inversa 2x2

*   **Notazione (Pag 2):** Una matrice $A = (a_{ij})_{\substack{i=1..m \\ j=1..n}}$ può essere vista come:
    *   Un insieme di vettori colonna: $A = (C^1 | C^2 | \dots | C^n)$ dove $C^j \in \mathbb{R}^m$.
    *   Un insieme di vettori riga: $A = \begin{pmatrix} R_1 \\ \vdots \\ R_m \end{pmatrix}$ dove $R_i \in \mathbb{R}^n$.
*   **Matrice Diagonale:** Una matrice quadrata $D$ è diagonale se $d_{ij}=0$ per ogni $i \neq j$.
*   **Matrice Identità $I_n$:** Matrice diagonale con $a_{ii}=1$ per ogni $i$.
*   **Matrice Nulla $O$:** Matrice con tutti gli elementi uguali a 0.

*   **Inversa di una Matrice 2x2 (Pag 3):**
    Sia $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ una matrice $2 \times 2$.
    *   Il **determinante** di A è $\det(A) = |A| = ad - bc$.
    *   Se $\det(A) \neq 0$, allora $A$ è invertibile e la sua inversa è:
        $$ A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} $$
    *   **Spiegazione:** Si scambiano gli elementi sulla diagonale principale ($a, d$), si cambiano i segni degli elementi sull'altra diagonale ($-b, -c$), e si divide tutto per il determinante.

*   **Esempio (Pag 4):** $$ A = \begin{pmatrix} 2 & 2 \\ 5 & 3 \end{pmatrix} $$
    *   $\det(A) = (2)(3) - (2)(5) = 6 - 10 = -4$. Poiché $\det(A) \neq 0$, A è invertibile.
    *   $A^{-1} = \frac{1}{-4} \begin{pmatrix} 3 & -2 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} -3/4 & 1/2 \\ 5/4 & -1/2 \end{pmatrix}$.
    *   **Verifica:**
        *   $A^{-1} \cdot A = \begin{pmatrix} -3/4 & 1/2 \\ 5/4 & -1/2 \end{pmatrix} \begin{pmatrix} 2 & 2 \\ 5 & 3 \end{pmatrix} = \begin{pmatrix} (-6/4+5/2) & (-6/4+3/2) \\ (10/4-5/2) & (10/4-3/2) \end{pmatrix} = \begin{pmatrix} (-3/2+5/2) & (-3/2+3/2) \\ (5/2-5/2) & (5/2-3/2) \end{pmatrix} = \begin{pmatrix} 2/2 & 0 \\ 0 & 2/2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2$.
        *   $A \cdot A^{-1} = \begin{pmatrix} 2 & 2 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} -3/4 & 1/2 \\ 5/4 & -1/2 \end{pmatrix} = \begin{pmatrix} (-6/4+10/4) & (2/2-2/2) \\ (-15/4+15/4) & (5/2-3/2) \end{pmatrix} = \begin{pmatrix} 4/4 & 0 \\ 0 & 2/2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2$. OK.

[[Determinante]] [[Matrice Invertibile]]

---

## 3. Esempi di Strutture Algebriche: Verifica Proprietà

*   **Esempio 1: $(\mathbb{Q}, *)$ con $a * b = a + b - 3ab$ (Pag 6-9):**
    1.  **Associatività?**
        *   $a * (b * c) = a * (b+c-3bc) = a + (b+c-3bc) - 3a(b+c-3bc) = a+b+c-3bc-3ab-3ac+9abc$.
        *   $(a * b) * c = (a+b-3ab) * c = (a+b-3ab) + c - 3(a+b-3ab)c = a+b-3ab+c-3ac-3bc+9abc$.
        *   I risultati coincidono. **SÌ, è associativa.**
    2.  **Commutatività?**
        *   $a * b = a + b - 3ab$.
        *   $b * a = b + a - 3ba$.
        *   Poiché $+$ e $\cdot$ sono commutative in $\mathbb{Q}$. **SÌ, è commutativa.**
    3.  **Elemento Neutro?** Cerchiamo $u \in \mathbb{Q}$ tale che $a * u = a$.
        *   $a + u - 3au = a \implies u - 3au = 0 \implies u(1 - 3a) = 0$.
        *   Questa deve valere per *ogni* $a \in \mathbb{Q}$. L'unico modo è che $u=0$.
        *   Verifica: $a * 0 = a+0-3a(0) = a$. **SÌ, $u=0$ è l'elemento neutro.**
        *   Quindi $(\mathbb{Q}, *, 0)$ è un **monoide commutativo**.
    4.  **Elementi Invertibili $U(\mathbb{Q}, *)$?** Cerchiamo $a'$ tale che $a * a' = 0$.
        *   $a + a' - 3aa' = 0 \implies a'(1 - 3a) = -a$.
        *   $a' = \frac{-a}{1 - 3a}$.
        *   Questo $a'$ esiste ed è in $\mathbb{Q}$ se e solo se il denominatore $1 - 3a \neq 0$.
        *   $1 - 3a \neq 0 \iff 3a \neq 1 \iff a \neq 1/3$.
        *   Quindi, tutti gli elementi $a \in \mathbb{Q}$ tranne $a=1/3$ sono invertibili.
        *   $U(\mathbb{Q}, *) = \mathbb{Q} \setminus \{1/3\}$.
        *   Esempio: L'inverso di $a=5$ è $a' = \frac{-5}{1 - 3(5)} = \frac{-5}{1 - 15} = \frac{-5}{-14} = 5/14$.
    5.  **È un gruppo? NO**, perché l'elemento $1/3$ non ha inverso.

*   **Esempio 2: $(\mathbb{R}^2, *)$ con $(a_1, a_2) * (b_1, b_2) = (3a_1b_1, a_2+b_2-3a_2b_2)$ (Pag 10-13):**
    1.  **Associatività?**
        *   $[(a_1, a_2)*(b_1, b_2)]*(c_1, c_2) = (3a_1b_1, a_2+b_2-3a_2b_2)*(c_1, c_2) = (3(3a_1b_1)c_1, (a_2+b_2-3a_2b_2)+c_2-3(a_2+b_2-3a_2b_2)c_2) = (9a_1b_1c_1, a_2+b_2+c_2-3a_2b_2-3a_2c_2-3b_2c_2+9a_2b_2c_2)$.
        *   $(a_1, a_2)*[(b_1, b_2)*(c_1, c_2)] = (a_1, a_2)*(3b_1c_1, b_2+c_2-3b_2c_2) = (3a_1(3b_1c_1), a_2+(b_2+c_2-3b_2c_2)-3a_2(b_2+c_2-3b_2c_2)) = (9a_1b_1c_1, a_2+b_2+c_2-3b_2c_2-3a_2b_2-3a_2c_2+9a_2b_2c_2)$.
        *   I risultati coincidono. **SÌ, è associativa.**
    2.  **Commutatività?**
        *   $(a_1, a_2)*(b_1, b_2) = (3a_1b_1, a_2+b_2-3a_2b_2)$.
        *   $(b_1, b_2)*(a_1, a_2) = (3b_1a_1, b_2+a_2-3b_2a_2)$.
        *   Poiché $\cdot$ e $+$ sono commutative in $\mathbb{R}$. **SÌ, è commutativa.**
    3.  **Elemento Neutro?** Cerchiamo $u=(u_1, u_2)$ tale che $(a_1, a_2) * (u_1, u_2) = (a_1, a_2)$.
        *   $(3a_1u_1, a_2+u_2-3a_2u_2) = (a_1, a_2)$.
        *   Deve valere per ogni $(a_1, a_2)$:
            *   $3a_1u_1 = a_1 \implies 3u_1 = 1 \implies u_1 = 1/3$.
            *   $a_2+u_2-3a_2u_2 = a_2 \implies u_2 - 3a_2u_2 = 0 \implies u_2(1 - 3a_2) = 0$. Questo deve valere per ogni $a_2$, quindi $u_2=0$.
        *   L'elemento neutro è $u = (1/3, 0)$. **SÌ, esiste.**
        *   Quindi $(\mathbb{R}^2, *, (1/3, 0))$ è un **monoide commutativo**.
    4.  **Elementi Invertibili $U(\mathbb{R}^2, *)$?** Cerchiamo $(\bar{a}_1, \bar{a}_2)$ tale che $(a_1, a_2) * (\bar{a}_1, \bar{a}_2) = (1/3, 0)$.
        *   $(3a_1\bar{a}_1, a_2+\bar{a}_2-3a_2\bar{a}_2) = (1/3, 0)$.
        *   $3a_1\bar{a}_1 = 1/3 \implies \bar{a}_1 = \frac{1}{9a_1}$. Esiste se $a_1 \neq 0$.
        *   $a_2+\bar{a}_2-3a_2\bar{a}_2 = 0 \implies \bar{a}_2(1 - 3a_2) = -a_2 \implies \bar{a}_2 = \frac{-a_2}{1 - 3a_2}$. Esiste se $a_2 \neq 1/3$.
        *   Quindi, $(a_1, a_2)$ è invertibile se e solo se $a_1 \neq 0$ e $a_2 \neq 1/3$.
        *   $U(\mathbb{R}^2, *) = \{ (a_1, a_2) \in \mathbb{R}^2 \mid a_1 \neq 0 \land a_2 \neq 1/3 \}$.
        *   Esempio: L'inverso di $(5, 7)$ è $(\bar{a}_1, \bar{a}_2)$ con $\bar{a}_1 = 1/(9 \cdot 5) = 1/45$ e $\bar{a}_2 = -7 / (1 - 3 \cdot 7) = -7 / (1 - 21) = -7 / (-20) = 7/20$. Inverso: $(1/45, 7/20)$.

---

## 4. Anelli: La Struttura con Due Operazioni

Passiamo ora a strutture algebriche un po' più ricche, che hanno due operazioni che interagiscono tra loro. Pensa a come i numeri interi $\mathbb{Z}$ hanno sia la somma che il prodotto, e queste operazioni non vivono per conto loro, ma sono legate dalla proprietà distributiva.

*   **Definizione Generale di Anello (Pag 19):** Una struttura $(A, +, \cdot)$ è un **Anello** se soddisfa queste tre condizioni fondamentali:
    1.  **La "somma" è un Gruppo Abeliano:** L'operazione $+$ rende $(A, +)$ un gruppo abeliano. Questo significa che:
        *   $+$ è **associativa**: $(a+b)+c = a+(b+c)$ per ogni $a,b,c \in A$.
        *   $+$ è **commutativa**: $a+b = b+a$ per ogni $a,b \in A$.
        *   Esiste un **elemento neutro** per $+$, che chiamiamo lo **zero** dell'anello, denotato $0_A$, tale che $a+0_A = 0_A+a = a$ per ogni $a \in A$.
        *   Ogni elemento $a \in A$ ha un **inverso additivo** (o opposto), denotato $-a$, tale che $a + (-a) = (-a) + a = 0_A$.
    2.  **Il "prodotto" è un Semigruppo:** L'operazione $\cdot$ rende $(A, \cdot)$ un semigruppo. Questo significa che:
        *   $\cdot$ è **associativa**: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ per ogni $a,b,c \in A$.
    3.  **Il Prodotto si Distribuisce sulla Somma:** Le due operazioni sono legate dalle proprietà distributive:
        *   **Distributiva sinistra:** $a \cdot (b+c) = (a \cdot b) + (a \cdot c)$ per ogni $a,b,c \in A$.
        *   **Distributiva destra:** $(b+c) \cdot a = (b \cdot a) + (c \cdot a)$ per ogni $a,b,c \in A$.

*   **Esempi Comuni di Anelli (Pag 20):**
    *   $(\mathbb{Z}, +, \cdot)$, $(\mathbb{Q}, +, \cdot)$, $(\mathbb{R}, +, \cdot)$, $(\mathbb{C}, +, \cdot)$ con le usuali somma e prodotto.
    *   $(\mathbb{R}^n, +, \cdot)$ dove $+$ è la somma vettoriale e $\cdot$ è il prodotto **componente per componente**.
    *   $(M_n(\mathbb{R}), +, \cdot)$ con la somma e il prodotto righe per colonne tra matrici $n \times n$.
    *   $(\mathbb{Z}^{\mathbb{Z}}, +, \cdot)$ (l'insieme delle funzioni da $\mathbb{Z}$ a $\mathbb{Z}$ con somma e prodotto definiti "punto per punto": $(f+g)(x) = f(x)+g(x)$ e $(f \cdot g)(x) = f(x) \cdot g(x)$).

[[Anello (matematica)]] [[Proprietà Distributiva]]

### 4.1 Anelli Booleani: Una Proprietà Speciale

Ora, esiste una classe speciale di anelli che ha un nome specifico: gli Anelli Booleani.

*   **Definizione di Anello Booleano:** Un anello $(A, +, \cdot)$ si dice **Anello Booleano** se, oltre a soddisfare le tre proprietà della definizione generale di Anello, ha anche questa proprietà aggiuntiva:
    *   **Idempotenza del Prodotto:** Per ogni elemento $a \in A$, vale $a \cdot a = a$.

Pensa all'idempotenza come a un'operazione che, se applicata due volte di seguito allo stesso elemento, non cambia il risultato rispetto ad applicarla una sola volta.

*   **Esempio Fondamentale: L'Anello Booleano dei Sottoinsiemi $(P(S), \Delta, \cap)$ (Pag 20):**
    Consideriamo l'insieme delle parti $P(S)$ di un insieme $S$, con l'operazione di "somma" data dalla differenza simmetrica $\Delta$ e l'operazione di "prodotto" data dall'intersezione $\cap$.
    *   **È un Anello?** Le tue note verificano in modo eccellente che $(P(S), \Delta, \cap)$ è un anello generale:
        *   $(P(S), \Delta)$ è un gruppo abeliano (l'elemento neutro è l'insieme vuoto $\emptyset$, e ogni insieme è l'inverso di se stesso rispetto a $\Delta$).
        *   $(P(S), \cap)$ è un semigruppo (l'intersezione è associativa).
        *   L'intersezione $\cap$ è distributiva rispetto alla differenza simmetrica $\Delta$. Le note mostrano la verifica dettagliata di questa proprietà cruciale: $A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$.
    *   **È un Anello Booleano?** Per esserlo, deve soddisfare anche la proprietà di idempotenza per il prodotto $\cap$. Dobbiamo verificare se per ogni $A \in P(S)$, vale $A \cap A = A$.
        *   Ebbene sì! Per la definizione stessa di intersezione, l'intersezione di un insieme con se stesso è sempre l'insieme stesso. $A \cap A = A$ vale per qualsiasi insieme $A$.
    *   **Conclusione:** Poiché $(P(S), \Delta, \cap)$ è un anello e soddisfa la proprietà $A \cap A = A$ per ogni suo elemento $A$, è effettivamente un **Anello Booleano**.

*   **Esempio di NON Anello (Pag 22):** $(P(S), \Delta, \cup)$.
    Come mostrano le note, questa struttura non è un anello perché l'unione $\cup$ non si distribuisce sulla differenza simmetrica $\Delta$. Abbiamo visto il controesempio con insiemi specifici $\{a\}, \{b\}, \{c\}$. Quindi, non ha senso chiedersi se sia un Anello Booleano, perché non è nemmeno un Anello!

[[Anello Booleano]] [[Idempotenza]]

### 4.2 Tipi di Anelli Aggiuntivi

Oltre agli Anelli Booleani, ci sono altre proprietà che un anello può avere:

*   **Anello Commutativo (Pag 24):** Un anello $(A, +, \cdot)$ è **commutativo** se l'operazione di prodotto $\cdot$ è commutativa, cioè $a \cdot b = b \cdot a$ per ogni $a,b \in A$.
    *   Esempi: $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$, $\mathbb{R}^n$, $(P(S), \Delta, \cap)$ (l'intersezione è commutativa!), $(\mathbb{Z}^{\mathbb{Z}}, +, \cdot)$.
    *   Non Esempio: $(M_n(\mathbb{R}), +, \cdot)$ per $n \ge 2$ (il prodotto tra matrici in generale non è commutativo).
*   **Anello Unitario (con unità) (Pag 24):** Un anello $(A, +, \cdot)$ è **unitario** se il semigruppo $(A, \cdot)$ è un **monoide**, cioè se esiste un elemento neutro per il prodotto $\cdot$, che chiamiamo l'**unità** dell'anello, denotato $1_A$, tale che $a \cdot 1_A = 1_A \cdot a = a$ per ogni $a \in A$.
    *   Esempi: $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ (unità 1), $(M_n(\mathbb{R}), +, \cdot)$ (unità $I_n$, la matrice identità), $(P(S), \Delta, \cap)$ (l'unità è l'insieme $S$, perché $A \cap S = A$ per ogni $A \in P(S)$), $(\mathbb{Z}^{\mathbb{Z}}, +, \cdot)$ (l'unità è la funzione costante $f(x)=1$).
*   **Anello Commutativo Unitario:** Un anello che è sia commutativo che unitario. (Es. $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$, $(P(S), \Delta, \cap)$).

[[Anello Commutativo]] [[Anello Unitario]]

### 4.3 Caratteristica di un Anello Unitario (Pag 25)

Questa è una proprietà interessante che si definisce solo per anelli che hanno un'unità moltiplicativa.

Sia $(A, +, \cdot)$ un anello unitario con unità $1_A$.
*   Consideriamo i multipli additivi dell'unità: $n \cdot 1_A$ è la somma di $1_A$ con se stesso $n$ volte (per $n > 0$). Ad esempio, $2 \cdot 1_A = 1_A + 1_A$. Definiamo $0 \cdot 1_A = 0_A$ e $(-n) \cdot 1_A = -(n \cdot 1_A)$.
*   La **caratteristica** dell'anello A, denotata $char(A)$, è definita come:
    *   $char(A) = 0$ se $n \cdot 1_A \neq 0_A$ per ogni intero positivo $n \ge 1$. In altre parole, non importa quante volte sommi l'unità a se stessa, non otterrai mai lo zero dell'anello (a meno che non la sommi 0 volte).
    *   $char(A) = m$ se $m$ è il **più piccolo intero positivo** tale che $m \cdot 1_A = 0_A$. Qui, sommando l'unità a se stessa $m$ volte ottieni lo zero dell'anello, e $m$ è il primo numero positivo per cui succede.

*   **Esempi di Caratteristica (Pag 26):**
    *   $char(\mathbb{Z}) = 0$, $char(\mathbb{Q}) = 0$, $char(\mathbb{R}) = 0$, $char(\mathbb{C}) = 0$. (Perché in questi anelli, $n \cdot 1 = n$, e $n$ è diverso da $0$ per ogni $n \ge 1$).
    *   $char(P(S), \Delta, \cap) = 2$. L'unità è $S$. Il neutro additivo (zero dell'anello) è $\emptyset$.
        *   $1 \cdot S = S$. Se $S$ non è vuoto, $S \neq \emptyset$.
        *   $2 \cdot S = S \Delta S$. Ricordi la differenza simmetrica di un insieme con se stesso? $S \Delta S = (S \setminus S) \cup (S \setminus S) = \emptyset \cup \emptyset = \emptyset$.
        *   Quindi, $2 \cdot S = \emptyset$. Il più piccolo intero positivo $m$ tale che $m \cdot S = \emptyset$ è $m=2$. La caratteristica è 2.


[[Caratteristica (algebra)]]

---
## 5. Elementi Cancellabili e Divisori dello Zero

Proprietà degli elementi rispetto a un'operazione.

### 5.1 Elementi Cancellabili (Pag 27-28)

Sia $(S, *)$ una struttura con operazione binaria. Un elemento $a \in S$ è:
*   **Cancellabile a sinistra** se: $\forall b, c \in S, \quad a * b = a * c \implies b = c$.
*   **Cancellabile a destra** se: $\forall b, c \in S, \quad b * a = c * a \implies b = c$.
*   **Cancellabile** (bilatero) se è cancellabile sia a sinistra sia a destra.

*   **Esempi:**
    *   $(P(S), \cap)$: $A=\{a\}, B=\{b\}, C=\{c\}$. $A \cap B = \emptyset$, $A \cap C = \emptyset$. Ma $B \neq C$. Quindi $A=\{a\}$ non è cancellabile a sinistra (e per commutatività, neanche a destra). In generale, in $(P(S), \cap)$ solo $S$ è cancellabile.
    *   $(\mathbb{Z}, \cdot)$: Gli elementi cancellabili sono tutti gli interi **diversi da 0**. Se $a \neq 0$ e $ab=ac$, allora $a(b-c)=0$, che implica $b-c=0$, cioè $b=c$. Se $a=0$, $0 \cdot b = 0 \cdot c$ (cioè $0=0$) non implica $b=c$.

*   **Relazione con Invertibilità (Pag 29):** In un monoide $(S, *, u)$:
    *   Se $a \in S$ è **invertibile**, allora $a$ è **cancellabile** (sia a sinistra che a destra).
    *   **Dimostrazione (cancellabile a sinistra):** Supponiamo $a * b = a * c$. Poiché $a$ è invertibile, esiste $a'$. Moltiplichiamo a sinistra per $a'$:
        *   $a' * (a * b) = a' * (a * c)$
        *   $(a' * a) * b = (a' * a) * c$ (Associatività)
        *   $u * b = u * c$
        *   $b = c$. OK. (Dimostrazione analoga per destra).
    *   **Il viceversa NON vale in generale:** Un elemento può essere cancellabile senza essere invertibile.
        *   Esempio: In $(\mathbb{Z}, \cdot)$, l'elemento $2$ è cancellabile ($2b=2c \implies b=c$), ma non è invertibile (il suo inverso $1/2$ non è in $\mathbb{Z}$).

[[Elemento Cancellabile]]

### 5.2 Divisori dello Zero (Pag 30-31)

Concetto specifico degli anelli $(A, +, \cdot)$.
*   **Definizione:** Un elemento $a \in A$, con $a \neq 0_A$, si dice **divisore dello zero** se esiste un elemento $b \in A$, con $b \neq 0_A$, tale che $a \cdot b = 0_A$ oppure $b \cdot a = 0_A$.
    *   Se $a \cdot b = 0_A$ con $a, b \neq 0_A$, $a$ è un divisore dello zero a sinistra, $b$ è un divisore dello zero a destra.
    *   Se l'anello è commutativo, la distinzione sx/dx non serve.

*   **Relazione con Cancellabilità (Pag 31):** In un anello $(A, +, \cdot)$:
    *   Un elemento $a \neq 0_A$ è un **divisore dello zero** $\iff$ $a$ **non è cancellabile** rispetto al prodotto $\cdot$.
    *   **Dimostrazione ($\implies$):** Se $a$ è divisore dello zero, esiste $b \neq 0_A$ tale che $a \cdot b = 0_A$. Ma sappiamo anche che $a \cdot 0_A = 0_A$. Quindi $a \cdot b = a \cdot 0_A$. Se $a$ fosse cancellabile (a sinistra), dovremmo concludere $b = 0_A$, ma avevamo $b \neq 0_A$. Assurdo. Quindi $a$ non può essere cancellabile. (Dimostrazione simile se $b \cdot a = 0_A$).
    *   **Dimostrazione ($\impliedby$):** Se $a \neq 0_A$ non è cancellabile (diciamo a sinistra), allora esistono $b, c \in A$ con $b \neq c$ tali che $a \cdot b = a \cdot c$. Questo implica $a \cdot b - a \cdot c = 0_A$, e per distributività $a \cdot (b - c) = 0_A$. Poiché $b \neq c$, l'elemento $d = b - c$ è diverso da $0_A$. Abbiamo trovato $d \neq 0_A$ tale che $a \cdot d = 0_A$. Quindi $a$ è un divisore dello zero (a sinistra).

*   **Esempio $(P(S), \Delta, \cap)$ (Pag 32):**
    *   L'elemento neutro per $\Delta$ è $\emptyset$. L'elemento neutro per $\cap$ è $S$.
    *   Cerchiamo $A \neq \emptyset$ che sia divisore dello zero. Cioè esiste $B \neq \emptyset$ tale che $A \cap B = \emptyset$.
    *   Questo è possibile se $A$ non è l'insieme $S$. Se $A \neq S$ e $A \neq \emptyset$, possiamo prendere $B = S \setminus A$. Poiché $A \neq S$, $B \neq \emptyset$. Poiché $A \neq \emptyset$, $B \neq S$. E $A \cap B = A \cap (S \setminus A) = \emptyset$.
    *   Quindi, in $(P(S), \Delta, \cap)$, i divisori dello zero sono **tutti i sottoinsiemi propri non vuoti** di $S$. Gli unici elementi non divisori dello zero sono $\emptyset$ (per definizione) e $S$ (l'unità moltiplicativa).

[[Divisore dello zero]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 7
> *   Abbiamo rivisto la definizione di **Gruppo** e classificato esempi comuni.
> *   Abbiamo visto come calcolare l'**inversa di una matrice 2x2**.
> *   Abbiamo analizzato in dettaglio due **strutture algebriche** verificando associatività, commutatività, neutro e invertibili.
> *   Abbiamo introdotto la **struttura di Anello** $(A, +, \cdot)$ (gruppo abeliano per $+$, semigruppo per $\cdot$, distributività).
> *   Abbiamo visto esempi di anelli, inclusi l'**Anello Booleano** $(P(S), \Delta, \cap)$.
> *   Abbiamo definito **Anello Commutativo** e **Anello Unitario**.
> *   Abbiamo definito la **Caratteristica** di un anello unitario.
> *   Abbiamo definito gli **elementi cancellabili** e visto che invertibile $\implies$ cancellabile.
> *   Abbiamo definito i **divisori dello zero** in un anello e visto che $a \neq 0$ è divisore dello zero $\iff$ $a$ non è cancellabile (rispetto a $\cdot$).

> [!TIP] Prossimi Passi
> *   Assicurati di aver compreso la definizione di Anello e le sue proprietà.
> *   Rifletti sulla differenza tra cancellabilità e invertibilità.
> *   Il prossimo passo potrebbe essere l'introduzione di Domini di Integrità e Campi, che sono anelli con proprietà aggiuntive legate ai divisori dello zero e agli inversi moltiplicativi.