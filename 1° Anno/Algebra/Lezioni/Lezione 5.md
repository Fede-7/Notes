# Lezione 5: Composizione, Invertibilità, Semigruppi e Monoidi

**Data:** 25/03/2025 (come da note)
**Argomenti:** Composizione (proprietà), Funzioni invertibili (teorema, unicità), Inversa destra/sinistra, Matrici (introduzione), Semigruppi, Elemento neutro, Monoidi, Esercizi.

#tag/functions #tag/composition #tag/inverse-function #tag/bijectivity #tag/matrices #tag/algebraic-structures #tag/semigroups #tag/monoids #tag/identity-element #tag/associativity #tag/algebra-avanzata

---

## 1. Composizione di Funzioni: Proprietà Fondamentali

Riprendiamo la composizione $g \circ f$ di $f: A \to B$ e $g: C \to D$, definita quando $\vec{f}(A) \subseteq C$.

*   **Definizione:** $(g \circ f): A \to D$ con $(g \circ f)(x) = g(f(x))$.
    *   Nota: Spesso si richiede semplicemente che il codominio di $f$ sia uguale o contenuto nel dominio di $g$, cioè $B \subseteq C$.

*   **Non Commutatività (Recap, Pag 1-2):** In generale, $g \circ f \neq f \circ g$ (anche quando entrambe le composizioni sono definite, ad esempio se $f, g: \mathbb{Z} \to \mathbb{Z}$).
    *   Esempio: $f(x) = x+1$, $g(y) = y^2$.
        *   $(g \circ f)(x) = g(f(x)) = g(x+1) = (x+1)^2 = x^2 + 2x + 1$.
        *   $(f \circ g)(x) = f(g(x)) = f(x^2) = x^2 + 1$.
        *   Chiaramente $(x+1)^2 \neq x^2 + 1$ (tranne per $x=0$).

*   **Associatività (Pag 2):** La composizione di funzioni **è associativa**.
    *   Siano $f: A \to B$, $g: B \to C$, $h: C \to D$. (Nota: ho adattato i domini/codomini per rendere le composizioni sempre possibili).
    *   Allora $(h \circ g) \circ f = h \circ (g \circ f)$.
    *   **Dimostrazione:** Dobbiamo verificare che le due funzioni $(h \circ g) \circ f$ e $h \circ (g \circ f)$ abbiano stesso dominio, stesso codominio e stessa legge.
        *   Dominio: Entrambe vanno da $A$ a $D$. OK.
        *   Codominio: Entrambe vanno da $A$ a $D$. OK.
        *   Legge: Sia $x \in A$.
            *   $((h \circ g) \circ f)(x) = (h \circ g)(f(x)) = h(g(f(x)))$.
            *   $(h \circ (g \circ f))(x) = h((g \circ f)(x)) = h(g(f(x)))$.
            *   Le leggi coincidono. OK.
    *   Quindi la composizione è associativa.
    *   [[Associatività della Composizione]]

*   **Composizione con Identità (Recap, Pag 3):**
    *   $f \circ id_A = f$
    *   $id_B \circ f = f$
    *   Se $f: A \to A$, allora $id_A \circ f = f \circ id_A = f$.

---

## 2. Funzioni Invertibili e Biettività

### 2.1 Definizione di Funzione Invertibile (Pag 4)

*   Una funzione $f: A \to B$ è **invertibile** se esiste una funzione $f^{-1}: B \to A$ (detta **funzione inversa** di $f$) tale che:
    1.  $f^{-1} \circ f = id_A$
    2.  $f \circ f^{-1} = id_B$

### 2.2 Teorema di Invertibilità (Pag 4)

*   **Proposizione:** Una funzione $f: A \to B$ è **invertibile se e solo se è biettiva**.
    *   ($\implies$) Se $f$ è invertibile, allora è biettiva (si può dimostrare).
    *   ($\impliedby$) Se $f$ è biettiva, allora per ogni $y \in B$ esiste un unico $x_y \in A$ tale che $f(x_y) = y$ (perché $|\overleftarrow{f}(\{y\})|=1$). Possiamo definire $f^{-1}: B \to A$ come $f^{-1}(y) = x_y$. Si verifica poi che questa $f^{-1}$ soddisfa le condizioni $f^{-1} \circ f = id_A$ e $f \circ f^{-1} = id_B$.

[[Funzione Inversa]] [[Teorema di Invertibilità]]

### 2.3 Esempi di Verifica Biettività e Calcolo Inversa

*   **Esempio 1 (Pag 5):** $f: \mathbb{Z} \to \mathbb{Z}$ con $f(x) = -x+5$.
    *   Iniettiva? $f(x)=f(y) \implies -x+5 = -y+5 \implies -x = -y \implies x=y$. **SÌ**.
    *   Suriettiva? Per ogni $a \in \mathbb{Z}$, cerchiamo $x \in \mathbb{Z}$ tale che $f(x)=a$.
        *   $-x+5 = a \implies -x = a-5 \implies x = -(a-5) = -a+5$.
        *   Poiché $a \in \mathbb{Z}$, anche $x=-a+5 \in \mathbb{Z}$. Trovato. **SÌ**.
    *   Biettiva? Sì.
    *   Inversa: La legge trovata per $x$ in funzione di $a$ ci dà l'inversa. $f^{-1}: \mathbb{Z} \to \mathbb{Z}$ con $f^{-1}(a) = -a+5$. (Nota: in questo caso $f^{-1}=f$!).

*   **Esempio 2 (Pag 6):** $g: \mathbb{Z} \to \mathbb{Z}$ con $g(x) = x-5$.
    *   Iniettiva? $g(x)=g(y) \implies x-5 = y-5 \implies x=y$. **SÌ**.
    *   Suriettiva? Per ogni $a \in \mathbb{Z}$, cerchiamo $x \in \mathbb{Z}$ tale che $g(x)=a$.
        *   $x-5 = a \implies x = a+5$.
        *   Poiché $a \in \mathbb{Z}$, anche $x=a+5 \in \mathbb{Z}$. Trovato. **SÌ**.
    *   Biettiva? Sì.
    *   Inversa: $g^{-1}: \mathbb{Z} \to \mathbb{Z}$ con $g^{-1}(a) = a+5$.

*   **Esempio 3 (Pag 7-8):** $f: \mathbb{N} \to \mathbb{Z}$ con $f(n) = n/2$ (se n pari) e $f(n) = -(n+1)/2$ (se n dispari). (Assumiamo $\mathbb{N}=\{0, 1, 2,...\}$).
    *   Abbiamo già visto che è **biettiva** (Lezione 4).
    *   Calcoliamo l'inversa $f^{-1}: \mathbb{Z} \to \mathbb{N}$. Dobbiamo trovare la formula per $n$ dato $a=f(n)$.
        *   Se $a \ge 0$: Sappiamo che l'input $n$ deve essere pari e $n/2 = a$, quindi $n=2a$.
        *   Se $a < 0$: Sappiamo che l'input $n$ deve essere dispari e $-(n+1)/2 = a$, quindi $n+1 = -2a$, e $n = -2a - 1$.
    *   Quindi, l'inversa è:
        $$
        f^{-1}(a) = \begin{cases} 2a & \text{se } a \ge 0 \\ -2a - 1 & \text{se } a < 0 \end{cases}
        $$
        *   Verifichiamo che l'output sia in $\mathbb{N}$: Se $a \ge 0$, $2a \ge 0$. Se $a < 0$, allora $-a > 0$, $-2a > 0$, e $-2a-1 \ge -1$? No, $-2a \ge 2$ (poiché $a \le -1$), quindi $-2a-1 \ge 1$. In entrambi i casi l'output è in $\mathbb{N}$.
    *   Verifica composizioni (Pag 8): $f \circ f^{-1} = id_{\mathbb{Z}}$ e $f^{-1} \circ f = id_{\mathbb{N}}$.

### 2.4 Unicità dell'Inversa (Pag 13)

*   **Proposizione:** Se una funzione $f: A \to B$ è invertibile, la sua funzione inversa $f^{-1}$ è **unica**.
*   **Dimostrazione:** Supponiamo per assurdo che esistano due funzioni inverse, $g: B \to A$ e $h: B \to A$. Allora devono valere:
    *   $g \circ f = id_A$ e $f \circ g = id_B$
    *   $h \circ f = id_A$ e $f \circ h = id_B$
    *   Consideriamo $h$. Possiamo scrivere $h = h \circ id_B$.
    *   Sostituiamo $id_B$ con $f \circ g$: $h = h \circ (f \circ g)$.
    *   Usiamo l'associatività: $h = (h \circ f) \circ g$.
    *   Sappiamo che $h \circ f = id_A$: $h = id_A \circ g$.
    *   Sappiamo che $id_A \circ g = g$.
    *   Quindi, abbiamo ottenuto $h = g$. Le due inverse devono coincidere.

[[Unicità della Funzione Inversa]]

### 2.5 Inversa Destra e Sinistra (Cenno, Pag 10-12)

Esistono concetti più deboli di invertibilità:

*   $g: B \to A$ è **inversa sinistra** di $f: A \to B$ se $g \circ f = id_A$. Si può dimostrare che $f$ ammette inversa sinistra $\iff$ $f$ è **iniettiva**. L'inversa sinistra, se esiste, non è necessariamente unica.
*   $h: B \to A$ è **inversa destra** di $f: A \to B$ se $f \circ h = id_B$. Si può dimostrare che $f$ ammette inversa destra $\iff$ $f$ è **suriettiva**. L'inversa destra, se esiste, non è necessariamente unica.

> [!IMPORTANT] Una funzione è invertibile (cioè ha un'inversa "bilatera") se e solo se è **biettiva**, e in tal caso l'inversa è unica. L'esistenza di solo una delle due (sinistra o destra) è legata solo all'iniettività o solo alla suriettività.

*   Esempio (Pag 11): $f: \mathbb{Z} \to \mathbb{Z}$ con $f(x)=2x+1$.
    *   Iniettiva? $2x+1=2y+1 \implies 2x=2y \implies x=y$. **SÌ**.
    *   Suriettiva? Cerchiamo $x$ tale che $2x+1=a$. $2x=a-1$. $x=(a-1)/2$. Questo è intero solo se $a-1$ è pari, cioè se $a$ è dispari. Se $a$ è pari (es. $a=2$), non esiste $x \in \mathbb{Z}$ tale che $f(x)=a$. **NO**.
    *   Essendo iniettiva ma non suriettiva, ammette inversa sinistra ma non destra.
    *   Candidata inversa sinistra $g: \mathbb{Z} \to \mathbb{Z}$ con $g(a) = (a-1)/2$ se $a$ dispari, e $g(a)=0$ (o qualsiasi altra cosa) se $a$ pari. Verifichiamo $g \circ f$:
        *   $(g \circ f)(x) = g(f(x)) = g(2x+1)$. Poiché $2x+1$ è sempre dispari, usiamo la prima regola per $g$: $g(2x+1) = ((2x+1)-1)/2 = (2x)/2 = x$.
        *   Quindi $g \circ f = id_{\mathbb{Z}}$. $g$ è un'inversa sinistra.

[[Inversa Sinistra e Destra]]

---

## 3. Strutture Algebriche: Semigruppi e Monoidi

### 3.1 Matrici (Cenno, Pag 14-16)

*   Una **matrice** $A$ di dimensione $m \times n$ a coefficienti in un insieme $K$ (es. $\mathbb{R}$) è una tabella rettangolare di elementi di $K$ con $m$ righe e $n$ colonne.
*   Notazione: $A = (a_{ij})$ dove $i$ è l'indice di riga ($1 \le i \le m$) e $j$ è l'indice di colonna ($1 \le j \le n$). $a_{ij}$ è l'elemento nella riga $i$ e colonna $j$.
*   L'insieme di tutte le matrici $m \times n$ a coefficienti in $K$ si denota $M_{m,n}(K)$.
*   **Matrice Trasposta** $A^T$: si ottiene scambiando le righe con le colonne. Se $A$ è $m \times n$, $A^T$ è $n \times m$, e $(A^T)_{ij} = a_{ji}$.
*   **Matrice Quadrata:** Se $m=n$.
*   **Operazioni:**
    *   **Somma di Matrici** (solo tra matrici della stessa dimensione $m \times n$): $(A+B)_{ij} = a_{ij} + b_{ij}$. L'insieme $(M_{m,n}(\mathbb{R}), +)$ è una struttura algebrica.
    *   **Prodotto per Scalare:** $\cdot : \mathbb{R} \times M_{m,n}(\mathbb{R}) \to M_{m,n}(\mathbb{R})$. $(c, A) \mapsto cA$, dove $(cA)_{ij} = c \cdot a_{ij}$. (Operazione esterna).
    *   (Vedremo più avanti il prodotto tra matrici).

[[Matrice (matematica)]] [[Matrice Trasposta]]

### 3.2 Semigruppi (Pag 18)

*   Una struttura algebrica $(S, *)$ dove $*$ è un'operazione binaria interna ($*: S \times S \to S$) si dice **semigruppo** se l'operazione $*$ è **associativa**.
    $$ \forall a, b, c \in S, \quad (a * b) * c = a * (b * c) $$

*   **Esempi di Semigruppi (Pag 19):**
    1.  $(\mathbb{N}, +)$, $(\mathbb{Z}, +)$, $(\mathbb{Q}, +)$, $(\mathbb{R}, +)$
    2.  $(\mathbb{N}, \cdot)$, $(\mathbb{Z}, \cdot)$, $(\mathbb{Q}, \cdot)$, $(\mathbb{R}, \cdot)$
    3.  $(P(S), \cap)$, $(P(S), \cup)$, $(P(S), \Delta)$
    4.  $(\mathbb{R}^n, +)$ (somma vettoriale componente per componente)
    5.  $(M_{m,n}(\mathbb{R}), +)$ (somma di matrici)
    6.  $(A^A, \circ)$, dove $A^A = \{ f \mid f: A \to A \}$ è l'insieme di tutte le funzioni da $A$ in $A$, e $\circ$ è la composizione di funzioni. (L'associatività della composizione garantisce che sia un semigruppo).

*   **Esempio di NON Semigruppo (Pag 18):** $(\mathbb{Z}, *)$ con $a * b = 2a + b$.
    *   $a * (b * c) = a * (2b + c) = 2a + (2b + c) = 2a + 2b + c$.
    *   $(a * b) * c = (2a + b) * c = 2(2a + b) + c = 4a + 2b + c$.
    *   Le due espressioni non sono uguali in generale (es. $a=b=c=1$). Non è associativa.

[[Semigruppo]]

### 3.3 Elemento Neutro (Pag 20)

Sia $(S, *)$ un semigruppo (o anche solo una struttura con operazione binaria).
*   Un elemento $u \in S$ si dice **elemento neutro** (o identità) se:
    $$ \forall a \in S, \quad a * u = u * a = a $$
*   $u_L \in S$ è **neutro a sinistra** se $\forall a \in S, u_L * a = a$.
*   $u_R \in S$ è **neutro a destra** se $\forall a \in S, a * u_R = a$.
*   Un elemento è neutro (bilatero) se è neutro sia a sinistra sia a destra.

*   **Esempi (Pag 21):**
    *   $(\mathbb{Z}, -)$: $0$ è neutro a destra ($a - 0 = a$), ma non a sinistra ($0 - a = -a \neq a$ se $a \neq 0$).
    *   $(P(S), \setminus)$: $\emptyset$ è neutro a destra ($A \setminus \emptyset = A$), ma non a sinistra ($\emptyset \setminus A = \emptyset \neq A$ se $A \neq \emptyset$).

*   **Proposizione (Unicità dell'Elemento Neutro, Pag 21):** Se in un semigruppo $(S, *)$ esiste un elemento neutro, allora esso è **unico**.
*   **Dimostrazione:** Siano $u_1$ e $u_2$ due elementi neutri.
    *   Consideriamo $u_1$. Poiché $u_2$ è neutro (in particolare a destra), $u_1 = u_1 * u_2$.
    *   Consideriamo $u_2$. Poiché $u_1$ è neutro (in particolare a sinistra), $u_1 * u_2 = u_2$.
    *   Mettendo insieme le due uguaglianze: $u_1 = u_1 * u_2 = u_2$. Quindi $u_1 = u_2$.

[[Elemento Neutro]] [[Unicità dell'Elemento Neutro]]

### 3.4 Monoidi (Pag 22)

*   Un semigruppo $(S, *)$ si dice **monoide** se **esiste** l'elemento neutro $u \in S$.
*   Un monoide è quindi una struttura $(S, *, u)$ con $*$ associativa e $u$ elemento neutro per $*$.

*   **Esempi di Monoidi (Pag 22):**
    *   $(\mathbb{N}, +, 0)$
    *   $(\mathbb{N}, \cdot, 1)$ (Anche $\mathbb{Z}, \mathbb{Q}, \mathbb{R}$)
    *   $(M_{m,n}(\mathbb{R}), +, 0)$ (dove $0$ è la matrice nulla)
    *   $(\mathbb{R}^n, +, \vec{0})$ (dove $\vec{0}=(0, ..., 0)$ è il vettore nullo)
    *   $(P(S), \cap, S)$ (S è neutro per $\cap$: $A \cap S = A$)
    *   $(P(S), \cup, \emptyset)$ ($\emptyset$ è neutro per $\cup$: $A \cup \emptyset = A$)
    *   $(P(S), \Delta, \emptyset)$ ($\emptyset$ è neutro per $\Delta$: $A \Delta \emptyset = A$)
    *   $(A^A, \circ, id_A)$ (L'insieme delle funzioni da A in A con la composizione e l'identità come neutro).

[[Monoide]]

---

## 4. Esercizi Proposti (Pag 23-24)

1.  Verificare che le seguenti applicazioni sono biettive e determinarne l'inversa:
    *   $f: \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q} \times \mathbb{Q}$ con $f(x, y) = (x+y, x-y)$. (Ripetizione es. 2 Lez 4, ma su $\mathbb{Q}$).
    *   $f: \mathbb{Q} \to \mathbb{Q}$ con $f(x) = 3x-7$.
    *   $S=\{a, b, c\}$, $A=\{a\}$. $f: P(S) \to P(S)$ con $f(X) = X \Delta A$.
    *   $f: \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z} \times \mathbb{Z}$ con $f(a, b) = (a+b, -b)$.

2.  Quali delle seguenti operazioni $*$ sono associative?
    *   $(\mathbb{N}, *)$ con $a * b = a \cdot |b|$. (Qui $|b|=b$ in $\mathbb{N}$, quindi $a*b=ab$. Sì).
    *   $(\mathbb{Z}, *)$ con $a * b = a \cdot |b|$.
    *   $(\mathbb{Z}, *)$ con $a * b = |a \cdot b|$.
    *   $(\mathbb{Z}, *)$ con $a * b = a + b + a \cdot b$.

---

> [!SUMMARY] Riepilogo Veloce Lezione 5
> *   La composizione di funzioni **non è commutativa** ma **è associativa**.
> *   Una funzione è **invertibile se e solo se è biettiva**, e l'inversa è **unica**.
> *   L'esistenza di inverse sinistre/destre è legata all'iniettività/suriettività.
> *   Abbiamo introdotto le **matrici** e alcune operazioni base.
> *   Un **semigruppo** è $(S, *)$ con $*$ associativa.
> *   L'**elemento neutro**, se esiste in un semigruppo, è unico.
> *   Un **monoide** è un semigruppo con elemento neutro.

> [!TIP] Prossimi Passi
> *   Prova a svolgere gli esercizi proposti sulla biettività/inversa e sull'associatività. Sono fondamentali per prendere confidenza.
> *   Il prossimo passo logico in algebra è introdurre l'ultimo ingrediente per i gruppi: l'**elemento inverso**.