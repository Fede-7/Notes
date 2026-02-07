# Lezione 9: Tavole di Cayley, Divisibilità in Anelli, Relazioni Binarie

**Data:** 10/04/2025 (come da note)
**Argomenti:** Tavole di Cayley, Cancellabilità (recap), Elementi Nilpotenti, Divisibilità in Anelli, Elementi Associati, MCD/MCM, Numeri Primi in Z, Relazioni Binarie (definizione, proprietà).

#tag/algebraic-structures #tag/cayley-tables #tag/cancellable-element #tag/zero-divisor #tag/nilpotent #tag/divisibility #tag/rings #tag/relations #tag/algebra-avanzata

---

## 1. Tavole di Cayley (Tabelle Moltiplicative)

*   **Definizione (Pag 2):** Per una struttura $(S, *)$ con un insieme finito $S=\{s_1, s_2, ..., s_n\}$, la **Tavola di Cayley** è una tabella quadrata dove l'elemento alla riga $i$ e colonna $j$ è il risultato dell'operazione $s_i * s_j$.
* |       | $s_1$ | $s_2$ | ... | $s_j$ | ... | $s_n$ |
|-------|-------|-------|-----|-------|-----|-------|
| $s_1$ | ...   | ...   | ... | ...   | ... | ...   |
| $s_2$ | ...   | ...   | ... | ...   | ... | ...   |
| ...   | ...   | ...   | ... | ...   | ... | ...   |
| $s_i$ | ...   | ...   | ... | $s_i*s_j$ | ... | ...   |
| ...   | ...   | ...   | ... | ...   | ... | ...   |
| $s_n$ | ...   | ...   | ... | ...   | ... | ...   |
*   **Utilità:**
    *   Visualizza l'intera struttura dell'operazione.
    *   **Commutatività:** L'operazione è commutativa se e solo se la tavola è **simmetrica** rispetto alla diagonale principale (cioè $s_i * s_j = s_j * s_i$).
    *   **Elemento Neutro:** Se esiste, ci sarà una riga e una colonna identiche agli indici della tabella.
    *   **Inversi:** Si possono cercare gli inversi trovando l'elemento neutro nella tabella.
    *   **Cancellabilità:** Un elemento $a$ è cancellabile a sinistra se nella riga corrispondente ad $a$ non ci sono ripetizioni. È cancellabile a destra se nella colonna corrispondente ad $a$ non ci sono ripetizioni.

*   **Esempio $(P(S), \cap)$ con $S=\{a, b\}$ (Pag 3):**
    *   $P(S) = \{\emptyset, A=\{a\}, B=\{b\}, S=\{a, b\}\}$.
    *   **Tavola di Cayley per $\cap$:**

        | $\cap$    | $\emptyset$ | A           | B           | S           |
        | :-------- | :---------- | :---------- | :---------- | :---------- |
        | $\emptyset$ | $\emptyset$ | $\emptyset$ | $\emptyset$ | $\emptyset$ |
        | A         | $\emptyset$ | A           | $\emptyset$ | A           |
        | B         | $\emptyset$ | $\emptyset$ | B           | B           |
        | S         | $\emptyset$ | A           | B           | S           |
    *   **Osservazioni:**
        *   Commutativa (tabella simmetrica).
        *   Elemento Neutro: $S$ (riga/colonna di S sono uguali agli indici).
        *   Cancellabilità:
            *   Riga $\emptyset$: tutti $\emptyset$ (non cancellabile a sx).
            *   Riga A: $\emptyset$, A, $\emptyset$, A (ripetizioni, non cancellabile a sx).
            *   Riga B: $\emptyset$, $\emptyset$, B, B (ripetizioni, non cancellabile a sx).
            *   Riga S: $\emptyset$, A, B, S (nessuna ripetizione, S è cancellabile a sx).
            *   Per simmetria, solo S è cancellabile (anche a dx).
        *   Divisori dello zero: $A \cap B = \emptyset$. $A, B$ sono divisori dello zero.

*   **Esempio $(P(S), \Delta)$ con $S=\{a, b\}$ (Pag 4):**
    *   **Tavola di Cayley per $\Delta$:** (Ricorda $X \Delta Y = (X \cup Y) \setminus (X \cap Y)$)

        | $\Delta$  | $\emptyset$ | A           | B           | S           |
        | :-------- | :---------- | :---------- | :---------- | :---------- |
        | $\emptyset$ | $\emptyset$ | A           | B           | S           |
        | A         | A           | $\emptyset$ | S           | B           |
        | B         | B           | S           | $\emptyset$ | A           |
        | S         | S           | B           | A           | $\emptyset$ |
    *   **Osservazioni:**
        *   Commutativa (tabella simmetrica).
        *   Elemento Neutro: $\emptyset$.
        *   Inversi: Ogni elemento è inverso di se stesso ($X \Delta X = \emptyset$).
        *   Cancellabilità: Ogni riga/colonna è una permutazione degli elementi $\{\emptyset, A, B, S\}$. Non ci sono ripetizioni. **Tutti gli elementi sono cancellabili**.
        *   È un **Gruppo Abeliano**.

[[Tavola di Cayley]]

---

## 2. Cancellabilità e Strutture Finite

*   **Proprietà (Pag 5):** In una struttura finita $(S, *)$, un elemento $a \in S$ è **cancellabile a destra** se e solo se la funzione "moltiplicazione a destra per a", $f_a: S \to S$ definita da $f_a(x) = x * a$, è **iniettiva**.
    *   **Dimostrazione:** $a$ è cancellabile a destra $\iff (\forall x, y \in S, x*a = y*a \implies x=y) \iff (\forall x, y \in S, f_a(x) = f_a(y) \implies x=y) \iff f_a$ è iniettiva.
*   **Corollario (Pag 5):** In una struttura finita $(S, *)$, se $a$ è cancellabile (a dx o sx), allora la funzione $f_a(x)=x*a$ (o $g_a(x)=a*x$) è **biettiva**.
    *   **Dimostrazione:** Una funzione $f: S \to S$ da un insieme finito a se stesso è iniettiva se e solo se è suriettiva, se e solo se è biettiva. Poiché $f_a$ è iniettiva (se $a$ è cancellabile), allora è anche biettiva.

---

## 3. Elementi Nilpotenti e Divisori

Sia $(A, +, \cdot)$ un anello.

*   **Elemento Nilpotente (Pag 7):** Un elemento $a \in A$ si dice **nilpotente** se esiste un intero $n \ge 1$ tale che $a^n = 0_A$ (dove $a^n = a \cdot a \cdot \dots \cdot a$, n volte).
    *   L'elemento $0_A$ è sempre nilpotente ($0_A^1 = 0_A$).
    *   **Esempio $(M_2(\mathbb{Q}), +, \cdot)$ (Pag 8):** La matrice $N = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ è nilpotente?
        *   $N^1 = N \neq O$.
        *   $N^2 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O$.
        *   Sì, $N$ è nilpotente (con $n=2$).
    *   **Osservazione (Pag 8):** Se $a \neq 0_A$ è nilpotente (cioè $a^n = 0_A$ per $n \ge 1$), allora $a$ è un **divisore dello zero**.
        *   **Dimostrazione:** Sia $n$ il più piccolo intero $\ge 1$ tale che $a^n = 0_A$. Se $n=1$, $a=0_A$, caso escluso. Se $n>1$, allora $a^{n-1} \neq 0_A$. Ma $a \cdot a^{n-1} = a^n = 0_A$. Abbiamo trovato $b = a^{n-1} \neq 0_A$ tale che $a \cdot b = 0_A$. Quindi $a$ è divisore dello zero.
    *   **Controesempio $(P(S), \Delta, \cap)$ (Pag 8):** L'elemento neutro additivo è $\emptyset$. $A^n = A \cap \dots \cap A = A$. Se $A \neq \emptyset$, $A^n = A \neq \emptyset$. Gli unici elementi nilpotenti sono $\emptyset$. Ma abbiamo visto che ci sono divisori dello zero (sottoinsiemi propri non vuoti).

[[Elemento Nilpotente]]

*   **Relazione di Divisibilità (Pag 9, 13):** In un anello $(A, +, \cdot)$, diciamo che $b$ **divide** $a$ (o $a$ è **multiplo** di $b$), e scriviamo $b \mid a$, se esiste un elemento $c \in A$ tale che $a = b \cdot c$.
    *   L'insieme dei **divisori** di $a$ è $div(a) = \{ b \in A \mid b \mid a \}$.
    *   L'insieme dei **multipli** di $b$ è $mult(b) = \{ a \in A \mid b \mid a \} = \{ b \cdot c \mid c \in A \}$.
    *   **Esempio $(\mathbb{Z}, +, \cdot)$ (Pag 9):** $div(4) = \{1, -1, 2, -2, 4, -4\}$.
    *   **Esempio $(P(S), \Delta, \cap)$ (Pag 9):** $A \mid B \iff B = A \cap C$ per qualche $C$. Questo significa $B \subseteq A$. Quindi $div(A) = \{ X \in P(S) \mid A \subseteq X \}$.
        *   $div(A) = \{S, A\}$? No, $div(A)=\{X | A \subseteq X\}$. Se $S=\{a,b\}$, $A=\{a\}$, $div(A)=\{ \{a\}, \{a,b\}=S \}$.
        *   $div(B) = \{B, S\}$. $div(S) = \{S\}$.

*   **Divisori dell'Unità (Pag 10):** In un anello unitario $(A, +, \cdot, 1_A)$:
    *   $div(1_A) = \{ b \in A \mid \exists c: 1_A = b \cdot c \}$.
    *   Questi sono esattamente gli elementi che hanno un inverso destro. Se l'anello è commutativo, sono gli elementi invertibili.
    *   $div(1_A) = U(A)$ (il gruppo degli elementi invertibili).
    *   **Esempio $(\mathbb{Z}, +, \cdot)$:** $div(1) = \{1, -1\} = U(\mathbb{Z})$.

*   **Elementi Associati (Pag 11):** In un anello unitario commutativo $A$, due elementi $x, y \in A$ si dicono **associati** (notazione $x \sim y$) se esiste un elemento invertibile $u \in U(A)$ tale che $x = u \cdot y$.
    *   Questa è una relazione di equivalenza.
    *   Se $x = u \cdot y$, allora $y = u^{-1} \cdot x$, quindi anche $y \sim x$.
    *   Se $x \sim y$, allora $div(x) = div(y)$.
    *   **Esempio $(\mathbb{Z}, +, \cdot)$:** $U(\mathbb{Z}) = \{1, -1\}$. $x \sim y \iff x = 1 \cdot y$ o $x = -1 \cdot y$. Cioè $x = \pm y$. Gli elementi associati a $a$ sono $\{a, -a\}$.
    *   **Divisori Banali (Pag 12):** I divisori banali di $a$ sono gli elementi associati ad $a$ e gli elementi associati a $1_A$ (cioè gli invertibili $U(A)$).
    *   **Divisori Propri (Pag 13):** Un divisore $b$ di $a$ è **proprio** se $b$ non è associato ad $a$ e $b$ non è invertibile (non è associato a $1_A$).
    *   **Esempio $(\mathbb{Z}, +, \cdot)$:** $div(4) = \{1, -1, 2, -2, 4, -4\}$.
        *   Associati a 4: $\{4, -4\}$.
        *   Associati a 1 (invertibili): $\{1, -1\}$.
        *   Divisori banali di 4: $\{1, -1, 4, -4\}$.
        *   Divisori propri di 4: $\{2, -2\}$.

[[Divisibilità]] [[Elementi Associati]]

*   **Proprietà Divisibilità (Pag 14):** Se $a \mid x$ e $a \mid y$, allora $\forall h, k \in A$, $a \mid (h \cdot x + k \cdot y)$.
    *   **Dimostrazione:** $x = x_1 a$, $y = y_1 a$. $h x + k y = h(x_1 a) + k(y_1 a) = (h x_1 + k y_1) a$. Poiché $(h x_1 + k y_1) \in A$, abbiamo $a \mid (hx+ky)$.

---

## 4. Aritmetica in $\mathbb{Z}$ (Pag 15-19)

L'anello $(\mathbb{Z}, +, \cdot)$ è un **Dominio di Integrità** (commutativo, unitario, privo di divisori dello zero). $U(\mathbb{Z}) = \{1, -1\}$.

*   **Divisori Banali di $a \in \mathbb{Z}$:** $\{1, -1, a, -a\}$.
*   **Elementi Associati a $a \in \mathbb{Z}$:** $\{a, -a\}$. ($a \sim b \iff a = \pm b$).
*   **Proprietà:** $a \mid b$ e $b \mid a \iff a \sim b$ (cioè $a = \pm b$).
    *   **Dimostrazione:** $b = b_1 a$, $a = a_1 b$. Sostituendo: $a = a_1 (b_1 a) = (a_1 b_1) a$. Se $a \neq 0$, per cancellatività $1 = a_1 b_1$. Poiché siamo in $\mathbb{Z}$, gli unici elementi il cui prodotto è 1 sono $1 \cdot 1 = 1$ e $(-1)(-1)=1$. Quindi $a_1, b_1 \in \{1, -1\} = U(\mathbb{Z})$. Perciò $a \sim b$. Se $a=0$, allora $b=b_1 0 = 0$, quindi $a=b=0$ e $a \sim b$.

*   **Massimo Comun Divisore (MCD) (Pag 17):** $e \in \mathbb{Z}$ è un MCD di $a, b \in \mathbb{Z}$ se:
    1.  $e \mid a$ e $e \mid b$ (è un divisore comune).
    2.  $\forall x \in \mathbb{Z}$: se $x \mid a$ e $x \mid b$, allora $x \mid e$ (è il più grande tra i divisori comuni, nel senso della divisibilità).
    *   Se $e$ è un MCD, allora anche $-e$ (l'associato) è un MCD. L'insieme degli MCD di $(a, b)$ è $\{e, -e\}$.
    *   **Convenzione:** "il" MCD, denotato $\text{MCD}(a, b)$ o $\text{gcd}(a, b)$, si intende quello **positivo**.
    *   Esempio: $\text{MCD}(4, 6) = 2$. L'insieme degli MCD è $\{2, -2\}$.

*   **Minimo Comune Multiplo (mcm) (Pag 18):** $m \in \mathbb{Z}$ è un mcm di $a, b \in \mathbb{Z}$ se:
    1.  $a \mid m$ e $b \mid m$ (è un multiplo comune).
    2.  $\forall x \in \mathbb{Z}$: se $a \mid x$ e $b \mid x$, allora $m \mid x$ (è il più piccolo tra i multipli comuni, nel senso della divisibilità).
    *   Se $m$ è un mcm, allora anche $-m$ è un mcm. L'insieme degli mcm di $(a, b)$ è $\{m, -m\}$.
    *   **Convenzione:** "il" mcm, denotato $\text{mcm}(a, b)$ o $\text{lcm}(a, b)$, si intende quello **positivo**.
    *   Esempio: $\text{mcm}(4, 6) = 12$. L'insieme degli mcm è $\{12, -12\}$.

*   **Numero Primo (Pag 19):** Un intero $p \in \mathbb{Z}$ è **primo** se:
    1.  $p \notin U(\mathbb{Z})$ non è un elemento invertibile (cioè $p \neq 1, p \neq -1$).
    2.  I suoi unici divisori sono quelli banali: $div(p) = \{1, -1, p, -p\}$.
    *   **Proprietà Fondamentale (Lemma di Euclide):** Se $p$ è primo e $p \mid (a \cdot b)$, allora $p \mid a$ oppure $p \mid b$.
    *   Esempio: $6$ non è primo. $6 \mid (3 \cdot 4) = 12$, ma $6 \nmid 3$ e $6 \nmid 4$.

[[Massimo Comun Divisore]] [[Minimo Comune Multiplo]] [[Numero Primo]] [[Lemma di Euclide]]

---

## 5. Relazioni Binarie: Proprietà Fondamentali

Torniamo alle relazioni, ma ora definite su un singolo insieme $A$.

*   **Relazione Binaria su A (Pag 20):** Una relazione $\mathcal{R}$ su $A$ è un sottoinsieme del prodotto cartesiano $A \times A$. Formalmente $\mathcal{R} = (A \times A, G)$ dove $G \subseteq A \times A$ è il grafo. Scriviamo $a \mathcal{R} b \iff (a, b) \in G$.

*   **Esempi Banali (Pag 21):**
    1.  **Relazione Totale:** $G = A \times A$. $\forall a, b \in A, a \mathcal{R} b$.
    2.  **Relazione di Identità (o Uguaglianza):** $G = Diag(A) = \{ (a, a) \mid a \in A \}$. $a \mathcal{R} b \iff a = b$.

*   **Proprietà delle Relazioni Binarie (Pag 22, 25):** Sia $\mathcal{R}$ una relazione su $A$.
    1.  **Riflessiva:** $\forall x \in A, x \mathcal{R} x$. (Ogni elemento è in relazione con se stesso).
        *   Equivalente a: $Diag(A) \subseteq G$.
    2.  **Antiriflessiva (o Irriflessiva):** $\forall x \in A, \neg (x \mathcal{R} x)$. (Nessun elemento è in relazione con se stesso).
        *   Equivalente a: $Diag(A) \cap G = \emptyset$.
    3.  **Simmetrica:** $\forall x, y \in A, x \mathcal{R} y \implies y \mathcal{R} x$. (Se x è in relazione con y, allora y è in relazione con x).
    4.  **Asimmetrica:** $\forall x, y \in A, x \mathcal{R} y \implies \neg (y \mathcal{R} x)$. (Se x è in relazione con y, allora y NON può essere in relazione con x).
        *   Nota: Asimmetrica $\implies$ Antiriflessiva.
    5.  **Antisimmetrica:** $\forall x, y \in A, (x \mathcal{R} y \land y \mathcal{R} x) \implies x = y$. (Gli unici "cicli di lunghezza 2" sono gli anelli su un elemento, cioè $x \mathcal{R} x$).
    6.  **Transitiva:** $\forall x, y, z \in A, (x \mathcal{R} y \land y \mathcal{R} z) \implies x \mathcal{R} z$. (Se x è in relazione con y, e y con z, allora x è in relazione con z).

*   **Esempi (Pag 23-28):**
    *   Relazione Totale su $S=\{a, b\}$: $G=\{(a,a),(a,b),(b,a),(b,b)\}$. È Riflessiva, Simmetrica, Transitiva. Non Antiriflessiva, Non Asimmetrica, Non Antisimmetrica.
    *   Relazione Identità su $S=\{a, b\}$: $G=\{(a,a),(b,b)\}$. È Riflessiva, Simmetrica, Antisimmetrica, Transitiva. Non Antiriflessiva, Non Asimmetrica.
    *   $(\mathbb{Z}, \mathcal{R}_{||})$ con $a \mathcal{R}_{||} b \iff |a|=|b|$.
        *   Riflessiva: $|a|=|a|$. Sì.
        *   Simmetrica: $|a|=|b| \implies |b|=|a|$. Sì.
        *   Transitiva: $|a|=|b| \land |b|=|c| \implies |a|=|c|$. Sì.
        *   (È una relazione di equivalenza). Non Antiriflessiva, Non Asimmetrica, Non Antisimmetrica (es. $2 \mathcal{R}_{||} -2$ e $-2 \mathcal{R}_{||} 2$ ma $2 \neq -2$).
    *   $(\mathbb{Z}, \mathcal{R}_{<})$ con $a \mathcal{R}_{<} b \iff |a|<|b|$.
        *   Antiriflessiva: $|a|<|a|$ è falso. Sì.
        *   Asimmetrica: $|a|<|b| \implies \neg(|b|<|a|)$. Sì.
        *   Transitiva: $|a|<|b| \land |b|<|c| \implies |a|<|c|$. Sì.
        *   (È una relazione d'ordine?). Non Riflessiva, Non Simmetrica, Non Antisimmetrica (non ci sono coppie $x \mathcal{R} y$ e $y \mathcal{R} x$).
    *   $(\mathbb{Z}, \mathcal{R}^*)$ con $a \mathcal{R}^* b \iff a=|b|$.
        *   Riflessiva? $a = |a|$ solo se $a \ge 0$. No.
        *   Antiriflessiva? $1 = |1|$. No.
        *   Simmetrica? $1 \mathcal{R}^* -1$ (perché $1=|-1|$). Ma $-1 \mathcal{R}^* 1$ è falso (perché $-1 \neq |1|$). No.
        *   Asimmetrica? No (vedi sopra).
        *   Antisimmetrica? $a \mathcal{R}^* b \land b \mathcal{R}^* a \implies a=|b| \land b=|a|$. Se $a,b \ge 0$, $a=b$. Se $a=1, b=-1$, $1=|-1|$ e $-1=|1|$ è falso. Se $a=-1, b=1$, $-1=|1|$ è falso. Sembra di sì? Verifichiamo: se $a=|b|$ e $b=|a|$, allora $|a|=||a||=|a|$, $|b|=||b||=|b|$. Se $a<0$, $b=|a|>0$. $a=|b|=b$. Contraddizione. Quindi $a,b$ devono essere $\ge 0$. In tal caso $a=b$ e $b=a$. Quindi $a=b$. **SÌ, è antisimmetrica.**
        *   Transitiva? $a \mathcal{R}^* b \land b \mathcal{R}^* c \implies a=|b| \land b=|c|$. Allora $a=||c|| = |c|$. Quindi $a \mathcal{R}^* c$? No. Esempio: $a=1, b=-1, c=1$. $1 \mathcal{R}^* -1$ ($1=|-1|$). $-1 \mathcal{R}^* 1$ (falso). Non si può applicare la transitività. Proviamo $a=1, b=1, c=-1$. $1 \mathcal{R}^* 1$ ($1=|1|$). $1 \mathcal{R}^* -1$ ($1=|-1|$). Dovrebbe seguire $1 \mathcal{R}^* -1$, che è vero. Proviamo $a=2, b=-2, c=2$. $2 \mathcal{R}^* -2$ ($2=|-2|$). $-2 \mathcal{R}^* 2$ (falso). Sembra transitiva? No. $a=2, b=2, c=-2$. $2 \mathcal{R}^* 2$ ($2=|2|$). $2 \mathcal{R}^* -2$ ($2=|-2|$). Deve seguire $2 \mathcal{R}^* -2$, vero. Forse è transitiva.
    *   $(\mathbb{Z}, \mathcal{R}_{\le})$ con $a \mathcal{R}_{\le} b \iff a \le b$.
        *   Riflessiva ($a \le a$). Sì.
        *   Antisimmetrica ($a \le b \land b \le a \implies a=b$). Sì.
        *   Transitiva ($a \le b \land b \le c \implies a \le c$). Sì.
        *   (È una relazione d'ordine). Non Antiriflessiva, Non Simmetrica (a meno che $a=b$), Non Asimmetrica.
    *   $(\mathbb{Z}, \mid)$ (divisibilità).
        *   Riflessiva ($a \mid a$, $a=a \cdot 1$). Sì.
        *   Antisimmetrica? $a \mid b \land b \mid a \implies a = \pm b$. Non è $a=b$. No.
        *   Transitiva ($a \mid b \land b \mid c \implies a \mid c$). Sì.

*   **Relazione Simmetrica e Asimmetrica (Pag 28):** Una relazione $\mathcal{R}$ è sia simmetrica sia asimmetrica se e solo se il suo grafo $G$ è vuoto. (L'asimmetria implica $G \cap G^{-1} = \emptyset$, la simmetria $G=G^{-1}$, quindi $G=\emptyset$).
*   **Relazione Simmetrica e Antisimmetrica (Pag 29):** Una relazione $\mathcal{R}$ è sia simmetrica sia antisimmetrica se e solo se il suo grafo $G$ è contenuto nella diagonale ($G \subseteq Diag(A)$).
    *   Esempio: La relazione di uguaglianza.

[[Relazione binaria]] [[Relazione riflessiva]] [[Relazione simmetrica]] [[Relazione transitiva]] [[Relazione antisimmetrica]] [[Relazione asimmetrica]] [[Relazione antiriflessiva]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 9
> *   Le **Tavole di Cayley** aiutano a visualizzare operazioni su insiemi finiti e a verificarne le proprietà (commutatività, neutro, inversi, cancellabilità).
> *   In strutture finite, **cancellabilità $\iff$ iniettività** della mappa di moltiplicazione.
> *   Un elemento **nilpotente** $a \neq 0$ ($a^n=0$) è sempre un **divisore dello zero**.
> *   Abbiamo definito la **divisibilità** in anelli, gli **elementi associati** ($x \sim y \iff x=uy, u \in U(A)$), i **divisori banali/propri**.
> *   In $\mathbb{Z}$, abbiamo definito **MCD**, **mcm** e **numeri primi**.
> *   Abbiamo introdotto le **relazioni binarie** su un insieme $A$ e le loro proprietà fondamentali: riflessiva, antiriflessiva, simmetrica, asimmetrica, antisimmetrica, transitiva.

> [!TIP] Prossimi Passi
> *   Rivedi le definizioni delle proprietà delle relazioni binarie. Prova a classificarne altre (es. "<", ">", "essere fratello di", "essere antenato di").
> *   Le combinazioni di queste proprietà daranno origine a strutture importanti: relazioni di equivalenza (riflessiva, simmetrica, transitiva) e relazioni d'ordine (riflessiva, antisimmetrica, transitiva).