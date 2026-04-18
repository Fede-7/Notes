# Lezione 6: Monoidi Commutativi, Elementi Invertibili e Gruppi

**Data:** 28/03/2025 (come da note)
**Argomenti:** Operazioni (non associative, neutro dx/sx), Prodotto tra matrici (definizione, esempio, non commutatività, associatività, elemento neutro), Monoidi commutativi, Elementi invertibili (simmetrici) in un monoide, Unicità dell'inverso, Gruppo degli elementi invertibili U(S), Inversa della composizione, Definizione di Gruppo, Gruppi Abeliani, Esempi.

#tag/algebraic-structures #tag/monoids #tag/matrices #tag/identity-element #tag/inverse-element #tag/groups #tag/abelian-groups #tag/algebra-avanzata

---

## 1. Strutture Algebriche: Esempi e Proprietà

### 1.1 Operazione di Esponenziazione (Pag 1)

*   Consideriamo $(\mathbb{N}^*, *)$ dove $\mathbb{N}^* = \{1, 2, 3, ...\}$ e l'operazione è $a * b = a^b$.
*   **Associatività?**
    *   $a * (b * c) = a * (b^c) = a^{(b^c)}$
    *   $(a * b) * c = (a^b) * c = (a^b)^c = a^{bc}$
    *   In generale, $a^{(b^c)} \neq a^{bc}$. Esempio: $2 * (3 * 2) = 2 * (3^2) = 2^9 = 512$. $(2 * 3) * 2 = (2^3) * 2 = 8 * 2 = 8^2 = 64$.
    *   Quindi, l'operazione **non è associativa**. $(\mathbb{N}^*, *)$ non è un semigruppo.
*   **Elemento Neutro?**
    *   Cerchiamo $u$ tale che $a * u = a$ e $u * a = a$ per ogni $a \in \mathbb{N}^*$.
    *   $a * u = a \implies a^u = a$. Questo vale per $u=1$. Quindi $1$ è **neutro a destra**.
    *   $u * a = a \implies u^a = a$. Questo non vale per un $u$ fisso per tutti gli $a$. Se $u=1$, $1^a = 1 \neq a$ (se $a \neq 1$). Quindi $1$ **non è neutro a sinistra**.
    *   Non esiste un elemento neutro bilatero.

### 1.2 Prodotto tra Matrici (Pag 2-6)

*   **Prodotto Righe per Colonne:** Il prodotto tra una matrice $A$ di dimensione $m \times n$ e una matrice $B$ di dimensione $n \times p$ è definito. (Il numero di colonne di A deve essere uguale al numero di righe di B).
*   Il risultato è una matrice $C = A \cdot B$ di dimensione $m \times p$.
*   L'elemento $c_{ij}$ della matrice prodotto $C$ (che si trova nella riga $i$ e colonna $j$) si calcola facendo il prodotto scalare tra la riga $i$ di $A$ e la colonna $j$ di $B$:
    $$ c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{in}b_{nj} $$

*   **Esempio (Pag 4):**

    Matrice A (2×3):
    $$ A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} $$
    Matrice B (3×2):  
    $$ B = \begin{pmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{pmatrix} $$
    
    Il prodotto $A \cdot B$ è una matrice $C$ (2x2).
    $$ A \cdot B = \begin{pmatrix} c_{11} & c_{12} \\ c_{21} & c_{22} \end{pmatrix} $$
    *   $c_{11} = (\text{riga 1 di A}) \cdot (\text{colonna 1 di B}) = (1 \cdot 7) + (2 \cdot 9) + (3 \cdot 11) = 7 + 18 + 33 = 58$
    *   $c_{12} = (\text{riga 1 di A}) \cdot (\text{colonna 2 di B}) = (1 \cdot 8) + (2 \cdot 10) + (3 \cdot 12) = 8 + 20 + 36 = 64$
    *   $c_{21} = (\text{riga 2 di A}) \cdot (\text{colonna 1 di B}) = (4 \cdot 7) + (5 \cdot 9) + (6 \cdot 11) = 28 + 45 + 66 = 139$
    *   $c_{22} = (\text{riga 2 di A}) \cdot (\text{colonna 2 di B}) = (4 \cdot 8) + (5 \cdot 10) + (6 \cdot 12) = 32 + 50 + 72 = 154$
    $$ A \cdot B = \begin{pmatrix} 58 & 64 \\ 139 & 154 \end{pmatrix} $$

*   **Prodotto $B \cdot A$ (Pag 5):** Ora $B$ è (3x2) e $A$ è (2x3). Il prodotto è definito e sarà una matrice $D$ (3x3).
    $$ B \cdot A = \begin{pmatrix} d_{11} & d_{12} & d_{13} \\ d_{21} & d_{22} & d_{23} \\ d_{31} & d_{32} & d_{33} \end{pmatrix} $$
    *   $d_{11} = (\text{riga 1 di B}) \cdot (\text{colonna 1 di A}) = (7 \cdot 1) + (8 \cdot 4) = 7 + 32 = 39$
    *   $d_{12} = (\text{riga 1 di B}) \cdot (\text{colonna 2 di A}) = (7 \cdot 2) + (8 \cdot 5) = 14 + 40 = 54$
    *   ... e così via.
    > [!IMPORTANT] Si vede subito che $A \cdot B \neq B \cdot A$ (non sono nemmeno delle stesse dimensioni in questo caso!). Il prodotto tra matrici **non è commutativo**.

*   **Matrici Quadrate e Monoide (Pag 6):** Consideriamo l'insieme delle matrici quadrate $n \times n$ a coefficienti reali, $M_{n,n}(\mathbb{R})$ o $M_n(\mathbb{R})$.
    *   Il prodotto tra matrici è un'operazione binaria interna su $M_n(\mathbb{R})$.
    *   Il prodotto è **associativo**: $(A \cdot B) \cdot C = A \cdot (B \cdot C)$. (Dimostrazione non banale).
    *   Esiste l'**elemento neutro**: la **matrice identità** $I_n$, che ha 1 sulla diagonale principale e 0 altrove.
        $$ I_n = \begin{pmatrix} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{pmatrix} $$
        Vale $A \cdot I_n = I_n \cdot A = A$ per ogni $A \in M_n(\mathbb{R})$.
    *   Quindi, $(M_n(\mathbb{R}), \cdot, I_n)$ è un **monoide**.
    *   Poiché il prodotto non è commutativo (in generale), è un **monoide non commutativo**.

[[Prodotto tra Matrici]] [[Matrice Identità]] [[Monoide non Commutativo]]

---

## 2. Monoidi Commutativi

*   **Definizione (Pag 9):** Un monoide $(S, *, u)$ si dice **commutativo** (o **abeliano**) se l'operazione $*$ è commutativa:
    $$ \forall a, b \in S, \quad a * b = b * a $$

*   **Esempi di Monoidi Commutativi (Pag 9):**
    *   $(\mathbb{N}, +, 0)$, $(\mathbb{Z}, +, 0)$, $(\mathbb{Q}, +, 0)$, $(\mathbb{R}, +, 0)$
    *   $(\mathbb{N}, \cdot, 1)$, $(\mathbb{Z}, \cdot, 1)$, $(\mathbb{Q}, \cdot, 1)$, $(\mathbb{R}, \cdot, 1)$
    *   $(P(S), \cap, S)$
    *   $(P(S), \cup, \emptyset)$
    *   $(P(S), \Delta, \emptyset)$

*   **Esempi di Monoidi NON Commutativi (Pag 9):**
    *   $(A^A, \circ, id_A)$ (se $|A| \ge 3$)
    *   $(M_n(\mathbb{R}), \cdot, I_n)$ (se $n \ge 2$)

*   **Esempio: Monoide Commutativo su $\mathbb{R} \times \mathbb{R}$ (Pag 10-11):**
    *   Sia $S = \mathbb{R} \times \mathbb{R} = \mathbb{R}^2$. Definiamo l'operazione $*$ :
        $$ (a, b) * (c, d) = (a+c, b \cdot d) $$
    *   Verifichiamo le proprietà:
        1.  **Associatività:**
            *   $[(a, b) * (c, d)] * (e, f) = (a+c, b \cdot d) * (e, f) = ((a+c)+e, (b \cdot d) \cdot f) = (a+c+e, bdf)$
            *   $(a, b) * [(c, d) * (e, f)] = (a, b) * (c+e, d \cdot f) = (a+(c+e), b \cdot (d \cdot f)) = (a+c+e, bdf)$
            *   I risultati coincidono. **SÌ, è associativa.**
        2.  **Commutatività:**
            *   $(a, b) * (c, d) = (a+c, b \cdot d)$
            *   $(c, d) * (a, b) = (c+a, d \cdot b)$
            *   Poiché $+$ e $\cdot$ sono commutative in $\mathbb{R}$, $a+c=c+a$ e $b \cdot d = d \cdot b$.
            *   **SÌ, è commutativa.**
        3.  **Elemento Neutro:** Cerchiamo $(u, v) \in \mathbb{R}^2$ tale che $(a, b) * (u, v) = (a, b)$ per ogni $(a, b)$.
            *   $(a, b) * (u, v) = (a+u, b \cdot v)$
            *   Vogliamo $(a+u, b \cdot v) = (a, b)$. Questo richiede:
                *   $a+u = a \implies u = 0$ (per ogni $a$)
                *   $b \cdot v = b \implies v = 1$ (per ogni $b$, attenzione se $b=0$, ma $0 \cdot v = 0$ vale per ogni $v$. Per $b \neq 0$, $v=1$).
            *   L'elemento neutro è $(u, v) = (0, 1)$. **SÌ, esiste.**
    *   Conclusione: $(\mathbb{R}^2, *, (0, 1))$ è un **monoide commutativo**.

*   **Esempio: $(\mathbb{Z}, *)$ con $a * b = a + b + 2ab$ (Pag 12-13):**
    *   **Associatività?**
        *   $a * (b * c) = a * (b+c+2bc) = a + (b+c+2bc) + 2a(b+c+2bc) = a+b+c+2bc+2ab+2ac+4abc$.
        *   $(a * b) * c = (a+b+2ab) * c = (a+b+2ab) + c + 2(a+b+2ab)c = a+b+2ab+c+2ac+2bc+4abc$.
        *   I risultati coincidono. **SÌ, è associativa.**
    *   **Commutatività?**
        *   $a * b = a + b + 2ab$
        *   $b * a = b + a + 2ba$
        *   Poiché $+$ e $\cdot$ sono commutative in $\mathbb{Z}$. **SÌ, è commutativa.**
    *   **Elemento Neutro?** Cerchiamo $u \in \mathbb{Z}$ tale che $a * u = a$ per ogni $a$.
        *   $a * u = a + u + 2au = a$
        *   $u + 2au = 0$
        *   $u(1 + 2a) = 0$
        *   Questa equazione deve valere per *ogni* $a \in \mathbb{Z}$. Se $a=0$, $u(1)=0 \implies u=0$. Se $a=1$, $u(3)=0 \implies u=0$. Se $a=-1$, $u(-1)=0 \implies u=0$.
        *   Verifichiamo $u=0$: $a * 0 = a+0+2a(0) = a$. Funziona.
        *   Poiché è commutativa, $0 * a = a$ vale automaticamente.
        *   L'elemento neutro è $u=0$. **SÌ, esiste.**
    *   Conclusione: $(\mathbb{Z}, *, 0)$ è un **monoide commutativo**.

[[Monoide Commutativo]]

---

## 3. Elementi Invertibili (Simmetrici) in un Monoide

Sia $(S, *, u)$ un monoide.

*   **Definizione (Pag 15):** Un elemento $a \in S$ si dice **invertibile** (o **simmetrizzabile**) se esiste un elemento $a' \in S$ (chiamato **inverso** o **simmetrico** di $a$) tale che:
    $$ a * a' = a' * a = u $$
*   $a'$ è **inverso destro** se $a * a' = u$.
*   $a'$ è **inverso sinistro** se $a' * a = u$.
*   $a'$ è inverso (bilatero) se è sia inverso destro sia sinistro.

*   **Unicità dell'Inverso (Pag 16):** Se un elemento $a$ in un monoide ammette un inverso $a'$, allora questo inverso è **unico**.
*   **Dimostrazione:** Supponiamo che $a'$ e $a''$ siano entrambi inversi di $a$.
    *   $a * a' = u$ e $a' * a = u$.
    *   $a * a'' = u$ e $a'' * a = u$.
    *   Consideriamo $a'$. Possiamo scrivere $a' = a' * u$.
    *   Sostituiamo $u$ con $a * a''$: $a' = a' * (a * a'')$.
    *   Usiamo l'associatività: $a' = (a' * a) * a''$.
    *   Sappiamo che $a' * a = u$: $a' = u * a''$.
    *   Poiché $u$ è neutro: $a' = a''$.
    *   Quindi l'inverso, se esiste, è unico.

*   **Notazione:** L'inverso di $a$, se esiste, si denota spesso $a^{-1}$ (notazione moltiplicativa) o $-a$ (notazione additiva).

*   **Gruppo degli Elementi Invertibili $U(S)$ (Pag 16):**
    *   L'insieme di tutti gli elementi invertibili di un monoide $(S, *, u)$ si denota $U(S)$ (o $S^*$, o $S^\times$).
    *   $U(S) = \{ a \in S \mid \exists a' \in S : a * a' = a' * a = u \}$.
    *   L'elemento neutro $u$ è sempre invertibile ($u * u = u$), quindi $u \in U(S)$, e $U(S)$ è **sempre non vuoto**.
    *   **Teorema (Pag 24):** $(U(S), *)$ è un **gruppo**. In particolare, $U(S)$ è **chiuso** rispetto all'operazione $*$.
        *   **Dimostrazione Chiusura:** Siano $a, b \in U(S)$. Dobbiamo dimostrare che $a * b \in U(S)$. Esistono $a', b' \in S$ tali che $a*a'=a'*a=u$ e $b*b'=b'*b=u$. Cerchiamo l'inverso di $(a * b)$. Proviamo con $(b' * a')$.
            *   $(a * b) * (b' * a') = a * (b * b') * a'$ (associatività) $= a * u * a' = a * a' = u$.
            *   $(b' * a') * (a * b) = b' * (a' * a) * b$ (associatività) $= b' * u * b = b' * b = u$.
            *   Abbiamo trovato l'inverso di $a * b$, che è $b' * a'$. Quindi $a * b \in U(S)$.
        *   L'operazione è associativa perché lo è in $S$. $u \in U(S)$ è l'elemento neutro. Ogni elemento in $U(S)$ ha un inverso per definizione. Quindi $(U(S), *)$ è un gruppo.

*   **Inversa della Composizione (Pag 25):** Se $f, g$ sono funzioni invertibili (biettive) e la composizione $f \circ g$ è definita, allora anche $f \circ g$ è invertibile e vale:
    $$ (f \circ g)^{-1} = g^{-1} \circ f^{-1} $$
    *   **Spiegazione:** Per annullare "prima g poi f", devi annullare "prima f (con f⁻¹) poi g (con g⁻¹)". L'ordine si inverte. Questa regola vale in generale per gli inversi in $U(S)$: $(a * b)' = b' * a'$.

[[Elemento Invertibile (Simmetrico)]] [[Unicità dell'Inverso]] [[Gruppo degli Elementi Invertibili]] [[Inverso di una Composizione]]

### 3.5 Esempi di U(S) (Pag 17-18)

*   $(\mathbb{N}, +, 0)$: $U(\mathbb{N}, +) = \{0\}$. (Solo 0 ha un opposto in $\mathbb{N}$).
*   $(\mathbb{N}, \cdot, 1)$: $U(\mathbb{N}, \cdot) = \{1\}$. (Solo 1 ha un reciproco in $\mathbb{N}$).
*   $(\mathbb{Z}, +, 0)$: $U(\mathbb{Z}, +) = \mathbb{Z}$. (Ogni intero $a$ ha opposto $-a \in \mathbb{Z}$).
*   $(\mathbb{Z}, \cdot, 1)$: $U(\mathbb{Z}, \cdot) = \{1, -1\}$. (Solo 1 e -1 hanno reciproco intero).
*   $(\mathbb{Q}, \cdot, 1)$: $U(\mathbb{Q}, \cdot) = \mathbb{Q}^* = \mathbb{Q} \setminus \{0\}$.
*   $(\mathbb{R}, \cdot, 1)$: $U(\mathbb{R}, \cdot) = \mathbb{R}^* = \mathbb{R} \setminus \{0\}$.
*   $(\mathbb{Q}, +, 0)$: $U(\mathbb{Q}, +) = \mathbb{Q}$.
*   $(\mathbb{R}, +, 0)$: $U(\mathbb{R}, +) = \mathbb{R}$.
*   $(\mathbb{R}^2, \cdot)$ con $(a,b)\cdot(c,d)=(ac, bd)$ e $u=(1,1)$:
    $U(\mathbb{R}^2, \cdot) = \{ (a, b) \in \mathbb{R}^2 \mid a \neq 0 \land b \neq 0 \} = \mathbb{R}^* \times \mathbb{R}^*$.
*   $(S = \mathbb{R} \times \{0\}, \cdot)$ con $u=(1,0)$:
    $U(S) = \{ (a, 0) \in S \mid a \neq 0 \} = \mathbb{R}^* \times \{0\}$.
*   $(A^A, \circ, id_A)$: $U(A^A) = \{ f \in A^A \mid f \text{ è biettiva} \}$. (Chiamato Gruppo delle Permutazioni o Simmetrico $S_A$).
*   $(M_n(\mathbb{R}), \cdot, I_n)$: $U(M_n(\mathbb{R})) = GL_n(\mathbb{R}) = \{ A \in M_n(\mathbb{R}) \mid \det(A) \neq 0 \}$. (Gruppo Lineare Generale).
*   $(P(S), \cap, S)$: $U(P(S), \cap) = \{S\}$. (Solo $S$ ha inverso $S$ perché $S \cap S = S$).
*   $(P(S), \cup, \emptyset)$: $U(P(S), \cup) = \{\emptyset\}$. (Solo $\emptyset$ ha inverso $\emptyset$ perché $\emptyset \cup \emptyset = \emptyset$).
*   $(P(S), \Delta, \emptyset)$: $A \Delta A' = \emptyset \iff A = A'$. Quindi l'inverso di $A$ è $A$ stesso. $U(P(S), \Delta) = P(S)$.

*   **Esempio $(\mathbb{Z}, *)$ con $a * b = a + b + 2ab$ e $u=0$ (Pag 19-20):**
    *   Cerchiamo l'inverso $a'$ di $a$. Vogliamo $a * a' = 0$.
    *   $a + a' + 2aa' = 0$
    *   $a'(1 + 2a) = -a$
    *   $a' = \frac{-a}{1+2a}$
    *   Questo $a'$ deve essere un intero $\mathbb{Z}$. Quando succede?
        *   Se $a=0$, $a'=0/1=0$. $0$ è inverso di se stesso. $0 \in U(\mathbb{Z}, *)$.
        *   Se $a=-1$, $a' = -(-1)/(1+2(-1)) = 1/(1-2) = 1/(-1) = -1$. $-1$ è inverso di se stesso. $-1 \in U(\mathbb{Z}, *)$.
        *   Se $a=1$, $a' = -1/(1+2) = -1/3 \notin \mathbb{Z}$.
        *   Se $a=-2$, $a' = -(-2)/(1-4) = 2/(-3) \notin \mathbb{Z}$.
        *   Sembra che $a'$ sia intero solo se $1+2a$ divide $-a$. Questo accade solo per $a=0$ e $a=-1$.
    *   Quindi $U(\mathbb{Z}, *) = \{0, -1\}$.

---

## 4. Sottostrutture Stabili (Parti Chiuse)

*   **Definizione (Pag 21):** Sia $(S, *)$ una struttura con un'operazione binaria interna. Un sottoinsieme non vuoto $H \subseteq S$ si dice **stabile** (o **parte chiusa**) rispetto a $*$ se:
    $$ \forall h, k \in H, \quad h * k \in H $$
    *   **Spiegazione:** Se prendi due elementi qualsiasi dentro $H$ e applichi l'operazione $*$, il risultato deve rimanere dentro $H$.

*   **Esempi (Pag 22-23):**
    *   $S = \{0, 1, ..., 9\}$. $(P(S), \cap)$. $H = \{ X \in P(S) \mid 1 \in X \land 5 \in X \}$.
        *   $H$ è stabile per $\cap$? Siano $X, Y \in H$. Allora $1, 5 \in X$ e $1, 5 \in Y$. Ne segue che $1, 5 \in X \cap Y$. Quindi $X \cap Y \in H$. **SÌ**.
        *   $H$ è stabile per $\cup$? Siano $X, Y \in H$. Allora $1, 5 \in X$ e $1, 5 \in Y$. Ne segue che $1, 5 \in X \cup Y$. Quindi $X \cup Y \in H$. **SÌ**.
        *   $H$ è stabile per $\Delta$? $X \Delta Y = (X \cup Y) \setminus (X \cap Y)$. Se $X=\{1, 5\}$ e $Y=\{1, 5, 2\}$, entrambi in $H$. $X \Delta Y = \{1, 2, 5\} \setminus \{1, 5\} = \{2\}$. Ma $\{2\} \notin H$. **NO**.
    *   $(\mathbb{Z}, +)$. $D = \{ 2n+1 \mid n \in \mathbb{Z} \}$ (interi dispari).
        *   $D$ è stabile per $+$? Siano $a=2n+1, b=2m+1 \in D$. $a+b = (2n+1)+(2m+1) = 2n+2m+2 = 2(n+m+1)$. Questo è un numero pari. Non appartiene a $D$. **NO**.
    *   $(A^A, \circ)$. $C = \{ f \in A^A \mid f \text{ è costante} \}$.
        *   $C$ è stabile per $\circ$? Siano $f, g \in C$. $f(x)=c_1$, $g(x)=c_2$ per ogni $x$.
        *   $(f \circ g)(x) = f(g(x)) = f(c_2) = c_1$. La funzione composta è la funzione costante uguale a $c_1$. Quindi $f \circ g \in C$. **SÌ**.
    *   $(\mathbb{R}^2, \cdot)$ con $(a,b)\cdot(c,d)=(ac, bd)$. $S = \mathbb{R} \times \{0\} = \{ (a, 0) \mid a \in \mathbb{R} \}$.
        *   $S$ è stabile? Siano $(a, 0), (b, 0) \in S$. $(a, 0) \cdot (b, 0) = (a \cdot b, 0 \cdot 0) = (ab, 0)$. Poiché $ab \in \mathbb{R}$, il risultato $(ab, 0)$ è ancora in $S$. **SÌ**.
    *   $(\mathbb{R}^2, \cdot)$. $T = \{ (a, -1) \mid a \in \mathbb{R} \}$.
        *   $T$ è stabile? Siano $(a, -1), (b, -1) \in T$. $(a, -1) \cdot (b, -1) = (a \cdot b, (-1) \cdot (-1)) = (ab, 1)$. Poiché la seconda componente è 1 (e non -1), il risultato $(ab, 1)$ **non** appartiene a $T$. **NO**.

*   **Proprietà (Pag 24):** Se $(S, *)$ è un semigruppo (o monoide) e $H \subseteq S$ è una parte stabile, allora $(H, *)$ è anch'esso un semigruppo. Se $S$ è monoide con neutro $u$, $(H, *)$ è un monoide solo se $u \in H$. L'elemento neutro di $H$ sarà lo stesso $u$.

[[Parte Stabile (Sottoinsieme Chiuso)]]

---

## 5. Gruppi

La struttura algebrica fondamentale.

*   **Definizione (Pag 26):** Una struttura $(G, *)$ è un **gruppo** se:
    1.  $*$ è **associativa** (quindi $(G, *)$ è un semigruppo).
    2.  Esiste l'**elemento neutro** $u \in G$ (quindi $(G, *, u)$ è un monoide).
    3.  **Ogni elemento** $a \in G$ è **invertibile** (ammette simmetrico) in $G$.
        (Cioè, $U(G) = G$).

*   **Gruppo Abeliano (Commutativo) (Pag 27):** Un gruppo $(G, *)$ si dice **abeliano** se l'operazione $*$ è **commutativa**.

*   **Esempi di Gruppi (Pag 26-27):**
    *   $(\mathbb{Z}, +)$, $(\mathbb{Q}, +)$, $(\mathbb{R}, +)$, $(\mathbb{C}, +)$ (Abeliani)
    *   $(\mathbb{R}^n, +)$ (Abeliano)
    *   $(M_{m,n}(\mathbb{R}), +)$ (Abeliano)
    *   $(\mathbb{Q}^*, \cdot)$, $(\mathbb{R}^*, \cdot)$, $(\mathbb{C}^*, \cdot)$ (Abeliani)
    *   $(P(S), \Delta)$ (Abeliano, neutro $\emptyset$, inverso di A è A stesso).
    *   $(B(A) = \{f: A \to A \mid f \text{ biettiva}\}, \circ)$ (Gruppo Simmetrico $S_A$, non abeliano se $|A| \ge 3$).
    *   $(GL_n(\mathbb{R}) = \{A \in M_n(\mathbb{R}) \mid \det(A) \neq 0\}, \cdot)$ (Gruppo Lineare Generale, non abeliano se $n \ge 2$).

*   **Esempi di Monoidi che NON sono Gruppi:**
    *   $(\mathbb{N}, +, 0)$ (mancano inversi tranne per 0)
    *   $(\mathbb{Z}, \cdot, 1)$ (mancano inversi tranne per 1, -1)
    *   $(P(S), \cap, S)$ (mancano inversi tranne per S)
    *   $(P(S), \cup, \emptyset)$ (mancano inversi tranne per $\emptyset$)
    *   $(M_n(\mathbb{R}), \cdot, I_n)$ (le matrici non invertibili non hanno inverso)

[[Gruppo (matematica)]] [[Gruppo Abeliano]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 6
> *   Abbiamo visto che l'esponenziazione non è associativa.
> *   Abbiamo definito e praticato il **prodotto tra matrici**, notando che è associativo ma non commutativo, e che $(M_n(\mathbb{R}), \cdot, I_n)$ è un monoide.
> *   Abbiamo definito i **monoidi commutativi**.
> *   Abbiamo definito l'**elemento invertibile (simmetrico)** in un monoide e dimostrato la sua **unicità**.
> *   Abbiamo introdotto il **gruppo degli elementi invertibili** $U(S)$ di un monoide $S$, dimostrando che è chiuso e forma un gruppo.
> *   Abbiamo visto la regola per l'**inversa della composizione**: $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$.
> *   Abbiamo definito una **parte stabile (chiusa)** $H \subseteq S$.
> *   Abbiamo finalmente definito la struttura di **Gruppo** (associatività, neutro, inverso per tutti gli elementi) e di **Gruppo Abeliano** (gruppo con operazione commutativa).
> *   Abbiamo visto numerosi esempi di gruppi e monoidi.

> [!TIP] Prossimi Passi
> *   Assicurati di aver ben compreso la definizione di Gruppo e le sue proprietà costitutive.
> *   Rivedi gli esempi di gruppi e monoidi, cercando di capire perché alcuni lo sono e altri no.
> *   Il prossimo passo sarà esplorare le proprietà fondamentali dei gruppi e introdurre i sottogruppi.