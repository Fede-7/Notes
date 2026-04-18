# Lezione 4: Biettività, Cardinalità, Composizione, Operazioni

**Data:** 21/03/2025 (come da note)
**Argomenti:** Insieme delle Parti (chiarimenti), Partizioni (recap, esempi), Funzioni Biettive, Equipotenza e Cardinalità, Composizione di Funzioni, Funzioni Invertibili, Operazioni (n-arie, binarie, unarie), Strutture Algebriche, Associatività, Esercizi.

#tag/settheory #tag/partitions #tag/functions #tag/bijectivity #tag/cardinality #tag/composition #tag/inverse-function #tag/operations #tag/algebraic-structures #tag/associativity #tag/algebra-avanzata

---

## 1. Chiarimenti su Insieme delle Parti e Partizioni

### 1.1 Elementi vs Sottoinsiemi in P(S) (Pag 1)

È cruciale distinguere tra appartenenza ($\in$) e inclusione ($\subseteq$) quando si lavora con l'insieme delle parti $P(S)$.

*   Sia $S = \{a, \{a\}, b, \{b\}, c, \{c\}\}$.
*   $P(S) = \{ X \mid X \subseteq S \}$ è l'insieme di **tutti i sottoinsiemi** di S.
*   **Esempi:**
    *   $a \in S$ (a è un elemento di S)
    *   $a \notin P(S)$ (a *non* è un sottoinsieme di S, è un elemento!)
    *   $a \not\subseteq P(S)$ (un elemento non può essere sottoinsieme di un insieme di insiemi in questo modo)
    *   $\{a\} \in P(S)$ (l'insieme contenente solo 'a' è un sottoinsieme di S, quindi è un elemento di P(S))
    *   $\{a\} \subseteq S$ (questo è vero solo se $a$ è anche un elemento di S, cosa che è vera nel nostro esempio)
    *   $\{a\} \not\subseteq P(S)$ (l'insieme {a} non è un sottoinsieme di P(S), perché gli elementi di {a} non sono elementi di P(S))
    *   $\{\{a\}\} \in P(S)$ (l'insieme contenente l'elemento {a} è un sottoinsieme di S, quindi è un elemento di P(S))
    *   $\{\{a\}\} \subseteq P(S)$ (questo è vero perché l'unico elemento di $\{\{a\}\}$, cioè $\{a\}$, è anche un elemento di $P(S)$).

> [!WARNING] Fai molta attenzione alla differenza tra $x$ e $\{x\}$ e tra $\in$ e $\subseteq$, specialmente con $P(S)$!

[[Insieme delle Parti]]

### 1.2 Partizioni (Recap ed Esempi) (Pag 2-4)

Ricordiamo la definizione: Una **partizione** di $S \neq \emptyset$ è una famiglia $\mathcal{F} \subseteq P(S)$ tale che:
1.  $\forall X \in \mathcal{F}, X \neq \emptyset$ (Nessun pezzo vuoto)
2.  $\forall X, Y \in \mathcal{F}, X \neq Y \implies X \cap Y = \emptyset$ (Pezzi disgiunti)
3.  $\bigcup_{X \in \mathcal{F}} X = S$ (I pezzi ricoprono tutto)

*   **Partizioni Banali:** $\mathcal{F}_1 = \{S\}$ e $\mathcal{F}_2 = \{ \{a\} \mid a \in S \}$ (se S è finito).

*   **Esempi con $S = \{a, b, c, d\}$ (Pag 3):**
    *   $\mathcal{F}_1 = \{ \{a\}, \{b, c\}, \{a, d\} \}$: **NON è partizione**. $\{a\} \cap \{a, d\} = \{a\} \neq \emptyset$. (Viola la condizione 2).
    *   $\mathcal{F}_2 = \{ \{a, b\}, \{d\} \}$: **NON è partizione**. $\{a, b\} \cup \{d\} = \{a, b, d\} \neq S$. (Manca $c$, viola la condizione 3).
    *   $\mathcal{F}_3 = \{ \{a, b\}, \{c\}, \{d\} \}$: **SÌ, è partizione**. (Pezzi non vuoti, disgiunti, unione fa S).
    *   $\mathcal{F}_4 = \{ \{a, b, d\}, \{c\} \}$: **SÌ, è partizione**.

*   **Esempio con $S = \mathbb{Z}$ (Pag 4):**
    *   Consideriamo $A = \{ a \in \mathbb{Z} \mid a^2 > 1 \}$ e $B = \{ a \in \mathbb{Z} \mid a^2 < 1 \}$.
    *   $A = \{ ..., -3, -2 \} \cup \{ 2, 3, ... \}$. $A \neq \emptyset$.
    *   $B = \{ 0 \}$. $B \neq \emptyset$.
    *   $A \cap B = \emptyset$.
    *   $A \cup B = \mathbb{Z} \setminus \{1, -1\}$. **NON ricopre tutto $\mathbb{Z}$**.
    *   Quindi $\mathcal{F} = \{A, B\}$ **NON è una partizione** di $\mathbb{Z}$.
    *   Consideriamo invece $D = \{ a \in \mathbb{Z} \mid a^2 \ge 1 \}$ e $C = \{ a \in \mathbb{Z} \mid a^2 \le 1 \}$.
    *   $D = \mathbb{Z} \setminus \{0\}$. $D \neq \emptyset$.
    *   $C = \{-1, 0, 1\}$. $C \neq \emptyset$.
    *   $D \cap C = \{-1, 1\} \neq \emptyset$.
    *   Quindi $\mathcal{G} = \{D, C\}$ **NON è una partizione** di $\mathbb{Z}$.
    *   Consideriamo $A = \{ a \in \mathbb{Z} \mid a^2 > 1 \}$, $C = \{ a \in \mathbb{Z} \mid a^2 \le 1 \} = \{-1, 0, 1\}$.
    *   $A \cap C = \emptyset$? No, $A \cap C = \{-1, 1\}$ non è vuoto.
    *   Consideriamo $A = \{ a \in \mathbb{Z} \mid a^2 > 1 \}$, $E = \{1\}$, $F = \{-1\}$, $G = \{0\}$.
    *   $\mathcal{H} = \{A, E, F, G\}$ **NON è una partizione** perché $A \cap E = \emptyset$, $A \cap F = \emptyset$, $A \cap G = \emptyset$, $E \cap F = \emptyset$, ecc. MA $A \cup E \cup F \cup G = \mathbb{Z}$. Tutti gli elementi sono non vuoti. Tutti disgiunti? No, $A$ contiene $2, -2$, ecc. $E=\{1\}$, $F=\{-1\}$, $G=\{0\}$. Sembra che $A = \mathbb{Z} \setminus \{-1, 0, 1\}$. In questo caso, $A, E, F, G$ sono disgiunti, non vuoti e la loro unione è $\mathbb{Z}$. **SÌ, $\mathcal{H}$ è una partizione.**
    *   La nota originale $\{A, C\}$ con $A=\{a | a^2>1\}$ e $C=\{a | a^2 \le 1\}$ **è una partizione** se interpretiamo $A = \mathbb{Z} \setminus \{-1, 0, 1\}$ e $C = \{-1, 0, 1\}$. I pezzi sono non vuoti, disgiunti e la loro unione è $\mathbb{Z}$.

> [!CAUTION] L'insieme vuoto $\emptyset$ e l'insieme totale $S$ **non** sono MAI partizioni di $S$ (se $|S|>1$). $\emptyset$ non è una famiglia di sottoinsiemi non vuoti. $\{S\}$ è una partizione (banale), ma $S$ da solo non è una famiglia di sottoinsiemi.

[[Partizione di un insieme]]

---

## 2. Funzioni Biettive ed Equipotenza

### 2.1 Funzione Biettiva

*   Una funzione $f: A \to B$ si dice **biettiva** (o biunivoca, o una corrispondenza biunivoca) se è **sia iniettiva sia suriettiva**.
*   **Caratterizzazione tramite Controimmagine (Pag 9):** $f$ è biettiva $\iff$ per ogni $b \in B$, la controimmagine $\overleftarrow{f}(\{b\})$ è un **singleton** (contiene esattamente un elemento).
    *   Iniettività $\implies |\overleftarrow{f}(\{b\})| \le 1$.
    *   Suriettività $\implies |\overleftarrow{f}(\{b\})| \ge 1$.
    *   Mettendole insieme: $|\overleftarrow{f}(\{b\})| = 1$.

*   **Esempio (Pag 8):** $f: \mathbb{N} \to \mathbb{Z}$ con $f(n) = n/2$ (se n pari) e $f(n) = -(n+1)/2$ (se n dispari). (Assumiamo $\mathbb{N}=\{0, 1, 2,...\}$).
    *   Abbiamo già visto che è **iniettiva** (Lezione 3).
    *   È **suriettiva?** Dobbiamo dimostrare che per ogni $b \in \mathbb{Z}$, esiste $n \in \mathbb{N}$ tale che $f(n)=b$.
        *   Se $b \ge 0$: Cerchiamo $n$ pari tale che $n/2 = b$. Basta prendere $n=2b$. Poiché $b \ge 0$, $n=2b \ge 0$ ed è pari. $n \in \mathbb{N}$. Trovato!
        *   Se $b < 0$: Cerchiamo $n$ dispari tale che $-(n+1)/2 = b$. Moltiplichiamo per -1: $(n+1)/2 = -b$. Poiché $b<0$, $-b>0$. Moltiplichiamo per 2: $n+1 = -2b$. Quindi $n = -2b - 1$. Poiché $-b > 0$, $-2b > 0$, quindi $n = -2b - 1 \ge -1$? No, $n \ge 1$. Essendo $-2b$ pari, $n=-2b-1$ è dispari. $n \in \mathbb{N}$. Trovato!
    *   Poiché per ogni $b \in \mathbb{Z}$ abbiamo trovato un $n \in \mathbb{N}$ tale che $f(n)=b$, la funzione è **suriettiva**.
    *   Essendo sia iniettiva che suriettiva, $f$ è **biettiva**.

[[Funzione Biettiva]]

### 2.2 Equipotenza e Cardinalità (Pag 9-10)

*   Due insiemi $A$ e $B$ si dicono **equipotenti** (o che hanno la stessa cardinalità) se esiste una funzione **biettiva** $f: A \to B$.
*   Notazione: $|A| = |B|$ o $A \approx B$.
*   L'equipotenza definisce una relazione di equivalenza sull'insieme di tutti gli insiemi.

*   **Cardinalità:** Concetto che generalizza il "numero di elementi".
    *   $|\emptyset| = 0$.
    *   Se $A = \{1, 2, ..., n\}$, allora $|A|=n$.
    *   Se $A \subseteq B \implies |A| \le |B|$. (Teorema di Cantor-Schröder-Bernstein per il caso generale, ovvio per insiemi finiti).

*   **Proprietà Fondamentale (Insiemi Finiti vs Infiniti):**
    *   Se $A$ e $B$ sono **finiti**: $A \subseteq B$ e $|A|=|B| \implies A=B$. (Se un sottoinsieme ha lo stesso numero di elementi dell'insieme, deve coincidere con esso).
    *   Questa proprietà **NON VALE** per insiemi **infiniti**!
        *   Esempio: $\mathbb{N} = \{0, 1, 2, ...\}$, $\mathbb{Z} = \{..., -1, 0, 1, ...\}$. Chiaramente $\mathbb{N} \subset \mathbb{Z}$ (sottoinsieme proprio). Ma abbiamo trovato una funzione biettiva $f: \mathbb{N} \to \mathbb{Z}$, quindi $|\mathbb{N}| = |\mathbb{Z}|$.
        *   Questo è un tratto distintivo degli insiemi infiniti: possono essere messi in corrispondenza biunivoca con un loro sottoinsieme proprio.

[[Equipotenza]] [[Cardinalità]] [[Insieme Finito]] [[Insieme Infinito]]

---

## 3. Composizione di Funzioni

Come combinare due funzioni in sequenza.

*   **Definizione (Pag 13):** Siano $f: A \to B$ e $g: C \to D$ due funzioni. Se l'immagine di $f$ è contenuta nel dominio di $g$ (cioè $\vec{f}(A) \subseteq C$), allora possiamo definire la **funzione composta** $g \circ f$ (si legge "g composto f"):
    $$ (g \circ f): A \to D $$
    $$ (g \circ f)(x) = g(f(x)) \quad \text{per ogni } x \in A $$
    *   **Spiegazione:** Per calcolare $(g \circ f)(x)$:
        1.  Applica $f$ a $x$, ottenendo $f(x) \in B$.
        2.  Poiché $f(x)$ appartiene anche a $C$ (per l'ipotesi $\vec{f}(A) \subseteq C$), puoi applicare $g$ a $f(x)$.
        3.  Il risultato è $g(f(x)) \in D$.

> [!WARNING] L'ordine è importante! $g \circ f$ significa: prima applichi $f$, poi applichi $g$. Il dominio della composizione è il dominio della *prima* funzione applicata ($f$). Il codominio della composizione è il codominio della *seconda* funzione applicata ($g$). La condizione $\vec{f}(A) \subseteq C$ è essenziale perché l'output di $f$ deve essere un input valido per $g$.

*   **Esempio 1 (Pag 14):**
    *   $S = \{x \subseteq{Z} \mid x ≠ \emptyset \text{ e finito}\}$? Sembra una definizione strana. Forse $S = P_{fin}(\mathbb{Z}) \setminus \{\emptyset\}$ (sottoinsiemi finiti non vuoti di $\mathbb{Z}$).
    *   $f: P(S) \to \mathbb{Z}$ con $f(X)=|X|$? Se $S$ è l'insieme dei sottoinsiemi finiti, $P(S)$ è l'insieme delle famiglie di sottoinsiemi finiti... Forse $S$ era un insieme finito? Rivediamo l'esempio.
    *   Assumiamo $S$ un insieme finito. $f: P(S) \to \mathbb{Z}$ con $f(X)=|X|$.
    *   $g: \mathbb{Q} \to \mathbb{Q}$ con $g(n) = \frac{3}{2}n$.
    *   Il codominio di $f$ è $\mathbb{Z}$. Il dominio di $g$ è $\mathbb{Q}$. Poiché $\mathbb{Z} \subseteq \mathbb{Q}$, la composizione $g \circ f$ è definita.
    *   $(g \circ f): P(S) \to \mathbb{Q}$
    *   $(g \circ f)(X) = g(f(X)) = g(|X|) = \frac{3}{2}|X|$.
    *   Esempio: Se $S=\{ -1, 0, 1, 13 \}$, $X = \{-1, 0, 1, 13\}$. $|X|=4$. $(g \circ f)(X) = \frac{3}{2} \cdot 4 = 6$.
    *   Esempio: Se $X = \{-1, 5, 7\}$. $|X|=3$. $(g \circ f)(X) = \frac{3}{2} \cdot 3 = \frac{9}{2}$.

*   **Esempio 2 (Pag 15):**
    *   $S=\{a, b, c\}$.
    *   $f: P(S) \times P(S) \to P(S)$ con $f(X, Y) = X \cap Y$.
    *   $g: P(S) \to P(S) \times P(S)$ con $g(A) = (A, S \setminus A)$.
    *   Composizione $g \circ f$: Il codominio di $f$ è $P(S)$, il dominio di $g$ è $P(S)$. Sono uguali, quindi $g \circ f$ è definita.
        *   $(g \circ f): P(S) \times P(S) \to P(S) \times P(S)$
        *   $(g \circ f)(X, Y) = g(f(X, Y)) = g(X \cap Y) = (X \cap Y, S \setminus (X \cap Y))$.
        *   Esempio: $(g \circ f)(\{a, b\}, \{b, c\}) = g(\{b\}) = (\{b\}, S \setminus \{b\}) = (\{b\}, \{a, c\})$.
    *   Composizione $f \circ g$: Il codominio di $g$ è $P(S) \times P(S)$, il dominio di $f$ è $P(S) \times P(S)$. Sono uguali, quindi $f \circ g$ è definita.
        *   $(f \circ g): P(S) \to P(S)$
        *   $(f \circ g)(A) = f(g(A)) = f((A, S \setminus A)) = A \cap (S \setminus A) = \emptyset$.
        *   Quindi $f \circ g$ è la funzione costante che manda ogni sottoinsieme $A$ nell'insieme vuoto.

*   **Esempio 3 (Pag 16):**
    *   $f: \mathbb{Z} \to \mathbb{Z}$ con $f(x) = 3x - 1$.
    *   $g: \mathbb{Z} \to \mathbb{Z}$ con $g(y) = (y+1)^2$.
    *   Composizione $g \circ f$: Codominio $f$ = Dominio $g = \mathbb{Z}$. Definita.
        *   $(g \circ f): \mathbb{Z} \to \mathbb{Z}$
        *   $(g \circ f)(x) = g(f(x)) = g(3x - 1) = ((3x - 1) + 1)^2 = (3x)^2 = 9x^2$.
    *   Composizione $f \circ g$: Codominio $g$ = Dominio $f = \mathbb{Z}$. Definita.
        *   $(f \circ g): \mathbb{Z} \to \mathbb{Z}$
        *   $(f \circ g)(x) = f(g(x)) = f((x+1)^2) = 3(x+1)^2 - 1$.
    *   **Non Commutatività (Pag 17):** Come si vede dagli esempi, in generale $g \circ f \neq f \circ g$. La composizione di funzioni **non è commutativa**.

*   **Composizione con Identità (Pag 18):**
    *   Sia $f: A \to B$. Siano $id_A: A \to A$ e $id_B: B \to B$ le funzioni identità.
    *   $f \circ id_A = f$.
        *   $(f \circ id_A)(x) = f(id_A(x)) = f(x)$. Dominio A, codominio B.
    *   $id_B \circ f = f$.
        *   $(id_B \circ f)(x) = id_B(f(x)) = f(x)$. Dominio A, codominio B.

[[Composizione di funzioni]] [[Non commutatività della composizione]]

---

## 4. Funzioni Invertibili

Quando una funzione può essere "annullata" da un'altra.

*   **Definizione (Pag 19):** Una funzione $f: A \to B$ si dice **invertibile** se esiste una funzione $f^{-1}: B \to A$ (chiamata **funzione inversa** di $f$) tale che:
    1.  $f^{-1} \circ f = id_A$ (Comporre $f$ e poi $f^{-1}$ riporta all'identità sul dominio originale A).
    2.  $f \circ f^{-1} = id_B$ (Comporre $f^{-1}$ e poi $f$ riporta all'identità sul codominio originale B).

> [!theorem] Teorema Fondamentale: Invertibilità e Biettività (Pag 19)
> Una funzione $f: A \to B$ è **completamente invertibile se e solo se è biettiva**.
>
> *   **Costruzione dell'Inversa:** Se $f$ è biettiva, la sua inversa $f^{-1}: B \to A$ è definita associando a ogni $b \in B$ l'**unico** elemento $a \in A$ tale che $f(a)=b$. L'esistenza e unicità di tale $a$ è garantita dalla biettività di $f$ (poiché $|\overleftarrow{f}(\{b\})|=1$ per ogni $b \in B$).

*   **Esempio 1 (Pag 20):** $f: \mathbb{Z} \to \mathbb{Z}$ con $f(x) = x+5$.
    *   È iniettiva? $f(x)=f(y) \implies x+5=y+5 \implies x=y$. Sì.
    *   È suriettiva? Per ogni $b \in \mathbb{Z}$, cerchiamo $x$ tale che $f(x)=b$, cioè $x+5=b$. Basta prendere $x=b-5$. Poiché $b \in \mathbb{Z}$, anche $x=b-5 \in \mathbb{Z}$. Sì.
    *   Essendo biettiva, è invertibile. L'inversa è $f^{-1}: \mathbb{Z} \to \mathbb{Z}$ con $f^{-1}(b) = b-5$.
    *   Verifica:
        *   $(f^{-1} \circ f)(x) = f^{-1}(f(x)) = f^{-1}(x+5) = (x+5)-5 = x = id_{\mathbb{Z}}(x)$.
        *   $(f \circ f^{-1})(b) = f(f^{-1}(b)) = f(b-5) = (b-5)+5 = b = id_{\mathbb{Z}}(b)$.

*   **Esempio 2 (Pag 21):** Controesempio per inversa "parziale".
    *   $f: \mathbb{Z} \to \mathbb{N}$ con $f(a)=|a|$. (Assumiamo $\mathbb{N}=\{0, 1, 2, ...\}$).
    *   $g: \mathbb{N} \to \mathbb{Z}$ con $g(x)=-x$.
    *   Calcoliamo $f \circ g$: $\mathbb{N} \to \mathbb{N}$.
        *   $(f \circ g)(x) = f(g(x)) = f(-x) = |-x| = |x|$. Poiché $x \in \mathbb{N}$ (dominio di $g$), $|x|=x$.
        *   Quindi $(f \circ g)(x) = x = id_{\mathbb{N}}(x)$. Sembra che $g$ sia un'inversa destra di $f$.
    *   Calcoliamo $g \circ f$: $\mathbb{Z} \to \mathbb{Z}$.
        *   $(g \circ f)(a) = g(f(a)) = g(|a|) = -|a|$.
        *   Questo **NON** è $id_{\mathbb{Z}}(a)=a$. Ad esempio, $(g \circ f)(1) = -|1| = -1 \neq 1$.
    *   Conclusione: $f$ non è invertibile (infatti non è iniettiva, $f(1)=f(-1)=1$). $g$ non è l'inversa di $f$.

[[Funzione Inversa]] [[Teorema di Invertibilità]]

---

## 5. Operazioni e Strutture Algebriche

Introduciamo i concetti base dell'algebra.

### 5.1 Operazioni n-arie, Binarie, Unarie (Pag 22-24)

*   Un'**operazione interna n-aria** su un insieme non vuoto $A$ è una funzione $f: A^n \to A$, dove $A^n = A \times A \times \dots \times A$ (n volte).
*   **Operazione Binaria Interna (n=2):** Una funzione $f: A \times A \to A$. Prende due elementi di A e restituisce un elemento di A. Notazione spesso infissa: $a \circ b$ invece di $f(a, b)$.
    *   Esempi:
        *   $+ : \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$, $(a, b) \mapsto a+b$.
        *   $- : \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$, $(a, b) \mapsto a-b$.
        *   $\cdot : \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q}$, $(a, b) \mapsto a \cdot b$.
        *   $/ : \mathbb{Q}^* \times \mathbb{Q}^* \to \mathbb{Q}^*$, $(a, b) \mapsto a/b$. (Qui $\mathbb{Q}^* = \mathbb{Q} \setminus \{0\}$).
        *   $\cap : P(S) \times P(S) \to P(S)$, $(A, B) \mapsto A \cap B$.
        *   $\cup : P(S) \times P(S) \to P(S)$, $(A, B) \mapsto A \cup B$.
        *   $\Delta : P(S) \times P(S) \to P(S)$, $(A, B) \mapsto A \Delta B$.
        *   $\setminus : P(S) \times P(S) \to P(S)$, $(A, B) \mapsto A \setminus B$.
*   **Operazione Unaria Interna (n=1):** Una funzione $f: A \to A$. Prende un elemento di A e restituisce un elemento di A.
    *   Esempi:
        *   Opposto: $- : \mathbb{Z} \to \mathbb{Z}$, $a \mapsto -a$.
        *   Reciproco: $^{-1} : \mathbb{Q}^* \to \mathbb{Q}^*$, $a \mapsto 1/a = a^{-1}$.
        *   Complemento: $^c : P(S) \to P(S)$, $X \mapsto S \setminus X$.

*   **Operazione Esterna (Pag 25):** Una funzione $f: S \times T \to T$ (o $S \times T \to S$). Coinvolge due insiemi diversi.
    *   Esempio: Prodotto per scalare in $\mathbb{R}^2$. $\cdot : \mathbb{R} \times \mathbb{R}^2 \to \mathbb{R}^2$, $(a, (v_1, v_2)) \mapsto (a v_1, a v_2)$.

[[Operazione Binaria]] [[Operazione Unaria]]

### 5.2 Strutture Algebriche (Pag 25)

*   Una **struttura algebrica** è una coppia $(S, \mathcal{O})$ dove $S$ è un insieme non vuoto (chiamato **sostegno** o supporto) e $\mathcal{O}$ è un insieme di una o più operazioni (interne o esterne) definite su $S$.
*   Notazione: $(S, \circ_1, \circ_2, ...)$
*   Esempi: $(\mathbb{N}, +)$, $(\mathbb{Z}, +, \cdot)$, $(\mathbb{R}, +, \cdot)$, $(P(S), \cap, \cup, ^c)$, $(\mathbb{R}^2, +, \cdot_{\text{scalare}})$.

[[Struttura Algebrica]]

### 5.3 Proprietà Associativa (Pag 27)

*   Un'operazione binaria interna $\circ: S \times S \to S$ si dice **associativa** se:
    $$ \forall a, b, c \in S, \quad (a \circ b) \circ c = a \circ (b \circ c) $$
    *   **Spiegazione:** Non importa come metti le parentesi quando componi tre elementi con un'operazione associativa.

*   **Operazioni Associative:** $+$, $\cdot$ (sui numeri), $\cap$, $\cup$, $\Delta$ (sugli insiemi), composizione di funzioni ($h \circ (g \circ f) = (h \circ g) \circ f$).
*   **Operazioni NON Associative:** $-$, $/$ (divisione).
    *   Controesempio per $-$: $(3 - 2) - 1 = 1 - 1 = 0$. Ma $3 - (2 - 1) = 3 - 1 = 2$. Poiché $0 \neq 2$, la sottrazione non è associativa.

[[Proprietà Associativa]]

---

## 6. Esercizi Proposti (Pag 28-29)

**Studiare iniettività, suriettività e determinare eventuale biettività e calcolare immagini/controimmagini per le seguenti funzioni:**

1.  Definizione della funzione:
    $$
    f: a \in \mathbb{Z} \longrightarrow (a+3, a-3) \in \mathbb{Z} \times \mathbb{Z}
    $$
    Calcolare:
    *   $\vec{f}(\emptyset)$
    *   $\overleftarrow{f}(\emptyset)$
    *   $\vec{f}(\mathbb{Z})$
    *   $\overleftarrow{f}(\mathbb{Z} \times \mathbb{Z})$
    *   $\vec{f}(\{3, 5, 7\})$
    *   $\overleftarrow{f}(\{(4, -2)\})$
    *   $\overleftarrow{f}(\{(4, 0)\})$

2.  Definizione della funzione:
    $$
    f: (a, b) \in \mathbb{Z} \times \mathbb{Z} \longrightarrow (a+b, a-b) \in \mathbb{Z} \times \mathbb{Z}
    $$
    Calcolare:
    *   $\vec{f}(\{(3, 1), (-5, 7)\})$
    *   $\overleftarrow{f}(\{(1, 1), (3, 1)\})$


3.  Ripetere esercizio 2 con dominio e codominio $\mathbb{Q} \times \mathbb{Q}$.
    *(Studiare $f: (a, b) \in \mathbb{Q} \times \mathbb{Q} \longrightarrow (a+b, a-b) \in \mathbb{Q} \times \mathbb{Q}$ per iniettività, suriettività, biettività)*

4.  Sia $S = \{a, b, c\}$. Si consideri la funzione:
    $$
    f: (A, B) \in \mathcal{P}(S) \times \mathcal{P}(S) \longrightarrow (A, A \cap B) \in \mathcal{P}(S) \times \mathcal{P}(S)
    $$
    Determinare (det):
    *   $\vec{f}(\{(\{a\}, \{b\}), (\{a\}, \{c\}), (\{a, b\}, S)\})$
    *   $\overleftarrow{f}(\{(\{a\}, \{b\})\})$
    *   $\overleftarrow{f}(\{(\{a\}, \{a\})\})$
    *   $\vec{f}(\emptyset)$
    *   $\vec{f}(\mathcal{P}(S) \times \mathcal{P}(S))$
    *   $\overleftarrow{f}(\emptyset)$
    *   $\overleftarrow{f}(\mathcal{P}(S) \times \mathcal{P}(S))$
---

> [!SUMMARY] Riepilogo Veloce Lezione 4
> *   Abbiamo chiarito la distinzione tra $\in$ e $\subseteq$ in relazione a $P(S)$.
> *   Abbiamo rivisto la definizione di **partizione** con esempi.
> *   Abbiamo definito la **funzione biettiva** (iniettiva + suriettiva) e la sua caratterizzazione tramite controimmagine di singleton.
> *   Abbiamo introdotto l'**equipotenza** ($|A|=|B|$) tramite funzioni biettive e discusso la differenza tra insiemi finiti e infiniti riguardo ai sottoinsiemi propri.
> *   Abbiamo definito la **composizione di funzioni** ($g \circ f$) e visto che non è commutativa.
> *   Abbiamo definito la **funzione invertibile** e il teorema che la lega alla biettività.
> *   Abbiamo introdotto le **operazioni n-arie, binarie, unarie** (interne ed esterne).
> *   Abbiamo definito le **strutture algebriche**.
> *   Abbiamo definito la **proprietà associativa**.

> [!TIP] Prossimi Passi
> *   Prova a svolgere gli esercizi proposti. Sono ottimi per consolidare i concetti di iniettività, suriettività, immagine e controimmagine.
> *   Rifletti sulle diverse strutture algebriche menzionate. Quali proprietà (oltre all'associatività) potrebbero avere le loro operazioni (es. commutatività, elemento neutro, inverso)? Questo ci porterà ai gruppi!