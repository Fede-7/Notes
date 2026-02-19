# Definizioni e Teoremi — Corso Celentani 2025

> [!abstract] Indice
> Raccolta completa di tutte le definizioni testuali e algebriche, ordinate per lezione (1–22, esclusa la 18).
>
> | Sezione | Argomenti Principali |
> |:--------|:---------------------|
> | **Lez. 1** | Logica, Insiemi, Relazioni, Funzioni |
> | **Lez. 2** | Quantificatori, Immagine, Controimmagine, Iniettività, Partizioni |
> | **Lez. 3** | Suriettività, Funzione Caratteristica, Restrizione, Identità |
> | **Lez. 4** | Biettività, Equipotenza, Composizione, Invertibilità, Operazioni |
> | **Lez. 5** | Inversa sx/dx, Matrici, Semigruppo, Monoide |
> | **Lez. 6** | Prodotto Matrici, Invertibili $U(S)$, Parte Stabile, Gruppi |
> | **Lez. 7** | Anelli, Caratteristica, Cancellabilità, Divisori dello Zero |
> | **Lez. 8** | Omomorfismo, Dominio d'Integrità, Corpo, Campo, $V_K$, $S_n$ |
> | **Lez. 9** | Cayley, Nilpotenti, Divisibilità, MCD, mcm, Primi, Relazioni Binarie |
> | **Lez. 10** | Buon Ordinamento, Induzione, Divisione Euclidea, Bézout, Equivalenza, Ordine |
> | **Lez. 11** | Algoritmo di Euclide, FTA, Classi di Equivalenza, Insieme Quoziente |
> | **Lez. 12** | Equivalenza $\leftrightarrow$ Partizioni, Congruenza, $\mathbb{Z}_m$ |
> | **Lez. 13** | $\mathbb{Z}_m$ Campo, Invertibili, Divisori Zero, Nilpotenti, Eq. Congruenziali |
> | **Lez. 14** | Idempotenti, Criteri di Divisibilità |
> | **Lez. 15** | Dominio, Anello Prodotto, Caratteristica Prodotto |
> | **Lez. 16** | Eq. Diofantee, $\varphi(n)$, Fermat-Eulero, Calcolo Combinatorio |
> | **Lez. 17** | Ordine Largo/Stretto, Hasse, Min/Max, Minimali/Massimali, Inf/Sup |
> | **Lez. 19** | Divisibilità come Ordine, Ordine Indotto da Funzione |
> | **Lez. 20** | Reticoli (Ordine e Algebrici), Catene |
> | **Lez. 21** | Reticoli Limitati, Sottoreticoli, Isomorfismi, Complementati, Prodotto |
> | **Lez. 22** | Sottoanelli, Dualità, Distributivi, Booleani, Algebre di Boole, Anelli Booleani |

---

## Lezione 1 — Logica, Insiemi, Funzioni

### Connettivi Logici

> [!note] Negazione
> $\neg P$ è vera quando $P$ è falsa, e viceversa.

> [!note] Congiunzione
> $P \wedge Q$ è vera solo quando **entrambe** $P$ e $Q$ sono vere.

> [!note] Disgiunzione Inclusiva
> $P \vee Q$ è falsa solo quando **entrambe** $P$ e $Q$ sono false.

> [!note] Implicazione
> $P \Rightarrow Q$ è falsa solo quando $P$ è vera e $Q$ è falsa.

> [!note] Bicondizionale
> $P \Leftrightarrow Q$ è vera quando $P$ e $Q$ hanno lo **stesso valore di verità**.

### Tautologia e Contraddizione

> [!note] Tautologia
> Proposizione composta **sempre vera**, qualunque siano i valori di verità delle componenti.
> Esempio: $P \vee \neg P$.

> [!note] Contraddizione
> Proposizione composta **sempre falsa**.
> Esempio: $P \wedge \neg P$.

### Leggi Logiche Fondamentali

| Legge | Forma |
|:------|:------|
| Idempotenza | $P \vee P \Leftrightarrow P$, $\;P \wedge P \Leftrightarrow P$ |
| Commutatività | $P \vee Q \Leftrightarrow Q \vee P$, $\;P \wedge Q \Leftrightarrow Q \wedge P$ |
| Associatività | $(P \vee Q) \vee R \Leftrightarrow P \vee (Q \vee R)$ |
| Distributività | $P \wedge (Q \vee R) \Leftrightarrow (P \wedge Q) \vee (P \wedge R)$ |
| De Morgan | $\neg(P \wedge Q) \Leftrightarrow \neg P \vee \neg Q$, $\;\neg(P \vee Q) \Leftrightarrow \neg P \wedge \neg Q$ |

### XOR, NAND, NOR

> [!note] XOR (Disgiunzione Esclusiva)
> $$a \oplus b \;\Longleftrightarrow\; (\neg a \wedge b) \vee (a \wedge \neg b)$$
> [!note] NAND / NOR
> Sono **funzionalmente completi**: ogni connettivo logico può essere espresso usando solo NAND (o solo NOR).

### Predicati e Quantificatori

> [!note] Predicato
> Proprietà o relazione con variabili; una **formula ben formata** (FBF) diventa proposizione quando le variabili vengono sostituite.

> [!note] Quantificatore Universale
> $\forall x\, P(x)$: «per ogni $x$, vale $P(x)$».

> [!note] Quantificatore Esistenziale
> $\exists x\, P(x)$: «esiste almeno un $x$ tale che $P(x)$».

> [!note] Quantificatore Esistenziale Unico
> $$\exists!\, x\, P(x) \;\Longleftrightarrow\; \exists x\, P(x) \;\wedge\; \forall x\,\forall y\,\bigl(P(x) \wedge P(y) \Rightarrow x = y\bigr)$$
### Variabili Libere e Vincolate

> [!note] Variabile Vincolata
> Una variabile che compare nel raggio d'azione di un quantificatore. Altrimenti è **libera**. Una formula senza variabili libere è detta **chiusa** (è una proposizione).

### Insiemi

> [!note] Insieme
> Collezione di oggetti distinti, detti **elementi**. Si scrive $a \in A$ se $a$ appartiene ad $A$.

> [!note] Insieme Vuoto
> $\emptyset$ — l'insieme privo di elementi.

> [!note] Sottoinsieme
> $A \subseteq B \;\Longleftrightarrow\; \forall x\,(x \in A \Rightarrow x \in B)$.

> [!note] Prodotto Cartesiano
> $$A \times B = \{(a, b) \mid a \in A \wedge b \in B\}$$
### Operazioni su Insiemi

| Operazione | Definizione |
|:-----------|:-----------|
| Unione | $A \cup B = \{x \mid x \in A \vee x \in B\}$ |
| Intersezione | $A \cap B = \{x \mid x \in A \wedge x \in B\}$ |
| Differenza | $A \setminus B = \{x \mid x \in A \wedge x \notin B\}$ |
| Complemento | $A^c = \{x \in U \mid x \notin A\}$ |
| Differenza Simmetrica | $A \mathbin{\triangle} B = (A \setminus B) \cup (B \setminus A)$ |

### Relazione e Funzione

> [!note] Relazione opp. Corrispondenza
> $\rho \subseteq A \times B$ — un sottoinsieme del prodotto cartesiano.

> [!note] Funzione
> $f: A \to B$ è una relazione tale che $\forall a \in A,\; \exists!\, b \in B$ con $(a, b) \in G_f$.
> $A$ è il **dominio**, $B$ il **codominio**.

---

## Lezione 2 — Quantificatori, Immagini, Iniettività, Partizioni

### Proprietà dei Quantificatori

> [!note] Negazione dei Quantificatori (De Morgan Generalizzato)
> $$\neg(\forall x\, P(x)) \;\Longleftrightarrow\; \exists x\,(\neg P(x))$$
> $$\neg(\exists x\, P(x)) \;\Longleftrightarrow\; \forall x\,(\neg P(x))$$

> [!note] Ordine dei Quantificatori
> $$\exists y\,\forall x\, \varphi(x,y) \;\Longrightarrow\; \forall x\,\exists y\, \varphi(x,y)$$
> Il viceversa **non** vale in generale.

### Immagine e Controimmagine

> [!note] Immagine di un Sottoinsieme
> Dato un sottoinsieme X ⊆ A, l'immagine di X tramite f è l'insieme di tutti gli elementi del codominio B che sono "raggiunti" da almeno un elemento di X.
> $$\vec{f}(X) = \{f(x) \mid x \in X\} \subseteq B$$

> [!note] Controimmagine
> Dato un sottoinsieme Y ⊆ B, la controimmagine (o preimmagine) di Y tramite f è l'insieme di tutti gli elementi del dominio A le cui immagini cadono dentro Y .
> $$\overleftarrow{f}(Y) = \{x \in A \mid f(x) \in Y\} \subseteq A$$
### Funzione Iniettiva

> [!note] Iniettività
> $f: A \to B$ è **iniettiva** se:
> $$\forall x_1, x_2 \in A:\; f(x_1) = f(x_2) \;\Longrightarrow\; x_1 = x_2$$

>[!note] Caratterizzazione tramite Controimmagine
Una funzione f : A → B è iniettiva se e solo se per ogni elemento b del codominio B, la sua controimmagine $f^{-1}(\{b\})$ contiene al massimo un elemento.
$$ f \text{ è iniettiva } \iff (\forall b \in B) \quad \bigl| f^{-1}(\{b\}) \bigr| \leq 1 $$
### Partizione

> [!note] Partizione
> Una famiglia $\mathcal{F} \subseteq \mathcal{P}(S)$ è una **partizione** di $S$ se:
> 1. $\forall X \in \mathcal{F},\; X \neq \emptyset$
> 2. $\forall X, Y \in \mathcal{F},\; X \neq Y \Rightarrow X \cap Y = \emptyset$
> 3. $\bigcup \mathcal{F} = S$

> [!note] Partizioni Banali:
$\mathcal{F}_1 = \{\{S\}\} = \{\{a, b, c\}\}$. (Un solo pezzo: l'insieme intero).
$\mathcal{F}_2 = \{\{a\}, \{b\}, \{c\}\}$. (Ogni pezzo è un singolo elemento)

---

## Lezione 3 — Suriettività, Funzione Caratteristica, Restrizione, Identità

### Funzione Suriettiva

> [!note] Suriettività
> $f: A \to B$ è **suriettiva** se:
> $$\forall b \in B,\; \exists a \in A:\; f(a) = b$$

>[!note] Caratterizzazione tramite Controimmagine
Una funzione f : A → B è suriettiva se e solo se per ogni elemento b del codominio B, la sua controimmagine $f^{-1}(\{b\})$ contiene al minimo un elemento.
$$ f \text{ è iniettiva } \iff (\forall b \in B) \quad \bigl| f^{-1}(\{b\}) \bigr| \geq 1 $$
### App. Immagine e Anti-Immagine banali e Funzione Caratteristica

> [!nota] Applicazioni immagine e anti-immagine banali
>  Per ogni $f: A \to B$: 
> - $f(\varnothing)=\varnothing$.
> - $f^{-1}(\varnothing)=\varnothing$.
> - $f^{-1}(B)=A$.
> - $f(A)=\operatorname{Im}(f)\subseteq B$ (e $f(A)=B$ sse $f$ è suriettiva).

> [!note] Funzione Caratteristica
> Sia $A \subseteq S$. La funzione $\chi_A: S \to \{0, 1\}$ è definita da:
> $$\chi_A(x) = \begin{cases} 1 & \text{se } x \in A \\ 0 & \text{se } x \notin A \end{cases}$$
### Uguaglianza di Funzioni

> [!note] Uguaglianza
> $f = g$ se e solo se hanno lo **stesso dominio**, lo **stesso codominio** e la **stessa legge**: $f(x) = g(x)$ per ogni $x$.


### Restrizione e Prolungamento

> [!note] Restrizione
> Sia $C \subseteq A$. La **restrizione** di $f: A \to B$ a $C$ è $f|_C: C \to B$ con $f|_C(x) = f(x)$.

> [!note] Prolungamento (Estensione)
> $f: A \to B$ **estende** $g: C \to B$, se 
> - $C \subseteq A$
> - $f(x) = g(x)$ per ogni $x \in C$.

### Funzione(o Applicazione) Identità

> [!note] Identità
> $\mathrm{id}_A: A \to A$ definita da $\mathrm{id}_A(a) = a$. È sempre **biettiva**.

---

## Lezione 4 — Biettività, Composizione, Invertibilità, Strutture Algebriche

### Funzione Biettiva

> [!note] Biettività
> $f: A \to B$ è **biettiva** se è **iniettiva e suriettiva**:
> $$\forall b \in B,\; |\overleftarrow{f}(\{b\})| = 1$$

>[!note] Caratterizzazione tramite Controimmagine
>
>f è biettiva ⟺ per ogni b ∈ B, la controimmagine f⁻¹({b}) è un singleton (contiene esattamente un elemento).
>
>- Iniettività ⟹ |f⁻¹({b})| ≤ 1
>- Suriettività ⟹ |f⁻¹({b})| ≥ 1
>
>Mettendole insieme: |f⁻¹({b})| = 1

> [!note] Funzione biettiva $\mathbb{N}\to\mathbb{Z}$
>$$f:\mathbb{N}\to\mathbb{Z},\qquad
> f(n)=
> \begin{cases}
> \ \ \frac{n}{2} & \text{se } n \text{ è pari}\\[4pt]
> -\frac{n+1}{2} & \text{se } n \text{ è dispari}
> \end{cases} $$
> (con $\mathbb{N}=\{0,1,2,\dots\}$).
### Equipotenza $\iff \exists f$   Biettiva

>[!note] Equipotenza $\iff \exists f$   Biettiva
>$|A| \gt |B| \to \nexists f iniettiva \atop |B| \gt |A| \to \nexists f suriettiva$ $\rbrace \to |A| = |B| \iff \exists f biettiva$

### Composizione di Funzioni e proprietà

> [!note] Composizione
> Date $f: A \to B$ e $g: B \to C$:
> $$(g \circ f)(x) = g(f(x))$$
> $$(g \circ f) : A \to C$$

>[!note] Proprietà
>- Associativa = $(h \circ g) \circ f = h\circ(g\circ f)$
>- Non commutativa = $g \circ f \not= f \circ g$
### Corrispondenza Complementare ed Inversa
>[!note] Corrispondenza Complementare
Data una relazione $\varphi \subseteq A \times B$,
 $\varphi' = (A \times B) \setminus \varphi$.

>[!note] Corrispondenza Inversa
Data una relazione $\varphi \subseteq A \times B$, 
$\varphi^{-1} = \{ (b, a) \in B \times A : (a, b) \in \varphi \}$.
### Funzione Inversa

>[!note] Funzione Invertibile
>Una funzione f : A → B $\iff \exists$ f⁻¹ : B → A  tale che:
>1. f⁻¹ ∘ f = idₐ (Comporre f e poi f⁻¹ riporta all'identità sul dominio originale A)
>2. f ∘ f⁻¹ = idᵦ (Comporre f⁻¹ e poi f riporta all'identità sul codominio originale B)

>[!important] Teorema Fondamentale: Invertibilità
>Una funzione $f$ è completamente invertibile $\iff$ biettiva.
>
>**Dimostrazione**
>
>($\implies$) Se $f$ invertibile $\implies$ è biettiva
>
>($\impliedby$) 
>Se $f$ è biettiva $\implies \forall b \in B, \exists! \space a \in A$ t.c. $f(a) = b$ (perché $|f^{-1}(\{b\})| = 1$).
>
>Possiamo definire $f^{-1}(b) = a$, che soddisfa le condizioni $f^{-1} \circ f = \text{id}_A$ e $f \circ f^{-1} = \text{id}_B$.

> [!note] Inversa Sinistra
> $g \circ f = \mathrm{id}_A$. Esiste $\Longleftrightarrow$ $f$ è **iniettiva**.

> [!note] Inversa Destra
> $f \circ h = \mathrm{id}_B$. Esiste $\Longleftrightarrow$ $f$ è **suriettiva**.

### Operazione $n$-aria

>[!note] Operazione $n$-aria
>Una operazione $n$-aria è una funzione $f : A^n \to A$, dove $A^n = A \times A \times \cdots \times A$ ($n$ volte).
>- $n=1 \to$ "Unaria interna"
>- $n=2 \to$ "Binaria interna"
>- Si dicono "**esterne**" solo quando si coinvolgono due insiemi diversi
>---

## Lezione 5 — Matrici, Semigruppo, Monoide
### Strutture Algebriche

> [!note] Struttura Algebrica
> $(S, \mathcal{O})$ dove $S$ è un insieme non vuoto e $\mathcal{O}$ è una famiglia di operazioni su $S$ (Interne opp. Esterne).

#### Matrici

> [!note] Matrice $m \times n$
> Tabella rettangolare di $m$ righe e $n$ colonne di elementi di un anello.
> **Trasposta:** $(A^T)_{ij} = A_{ji}$.


#### Magma

>[!note] Magma
>$(S,*)$, con $*$ operazione binaria interna
#### Associatività
> [!note] Associatività
> $$\forall a, b, c \in S:\; (a * b) * c = a * (b * c)$$

#### Semigruppo

> [!note] Semigruppo
> $(S, *)$ dove $*$ è un'operazione binaria **associativa**.

#### Elemento Neutro

> [!note] Elemento Neutro
> $u \in S$ tale che $\forall a \in S:\; a * u = u * a = a$.
> Se esiste, è **unico**.

>[!note] Proposizione: Unicità elemento neutro
> Se in un semigruppo $(S, ∗)$ esiste un elemento neutro "$u$", allora
> esso è unico.
> - Dimostrazione: 
> Siano $u_1$ e $u_2$ due elementi neutri.
Consideriamo $u_1$. Poiché $u_2$ è neutro (in particolare a destra), $u_1 = u_1 ∗ u_2$.
Consideriamo $u_2$. Poiché $u_1$ è neutro (in particolare a sinistra), $u_1 ∗ u_2 = u_2$.
Mettendo insieme le due uguaglianze: $u_1 = u_1 ∗ u_2 = u_2$. Quindi $u_1 = u_2$.
#### Monoide

> [!note] Monoide
> **Semigruppo con elemento neutro**: $(S, *, u)$.
>
> Esempi:
> - $(\mathbb{N}, +, 0)$, $(\mathbb{N}, \cdot, 1)$
> - $(\mathcal{P}(S), \cap, S)$, $(\mathcal{P}(S), \cup, \emptyset)$, $(\mathcal{P}(S), \triangle, \emptyset)$
> - $(A^A, \circ, \mathrm{id}_A)$

---

## Lezione 6 — Prodotto Matrici, Gruppi, Invertibili, Parte Stabile

### Prodotto di Matrici

> [!note] Prodotto Matriciale
> Date $A \in M_{m \times p}$ e $B \in M_{p \times n}$:
> $$c_{ij} = \sum_{k=1}^{p} a_{ik} \cdot b_{kj}$$
> Non commutativo; associativo; la matrice identità $I_n$ è l'elemento neutro.


### Elemento Invertibile (Simmetrico)

> [!note] Elemento Invertibile opp. Simmetrizzabile
> In un monoide $(S, *, u)$, $a \in S$ è **invertibile** se:
> $$\exists\, a' \in S:\; a * a' = a' * a = u$$
> L'inverso è **unico**. Invertibile $\Longrightarrow$ Cancellabile.

> [!tip] Dimostrazione — Unicità dell'inverso
> Siano $a'$ e $a''$ entrambi inversi di $a$. Allora:
> $$a' = a' * u = a' * (a * a'') = (a' * a) * a'' = u * a'' = a''$$
> Dunque l'inverso è unico. $\square$

### Gruppo degli Invertibili

> [!note] $U(S)$ — Gruppo degli Invertibili
> L'insieme degli elementi invertibili di un monoide $(S, *, u)$ è **chiuso** per $*$ e forma un **gruppo** $(U(S), *)$.
>
> Esempi: $U(\mathbb{N},+) = \{0\}$, $\;U(\mathbb{Z}, \cdot) = \{1,-1\}$, $\;U(\mathbb{Q}, \cdot) = \mathbb{Q}^*$, $\;U(A^A, \circ) = S_A$.

### Parte Stabile (Chiusa)

> [!note] Parte Stabile
> $H \subseteq S$ è **stabile** (o **chiusa**) per $*$ se:
> $$\forall h, k \in H:\; h * k \in H$$
> 
> ### Proprietà
> - Se $(S, *)$ è un **semigruppo** e $H \subseteq S$ è una parte stabile, allora $(H, *)$ è anch'esso un semigruppo.
> - Se $S$ è un **monoide** con elemento neutro $u$, allora $(H, *)$ è un monoide solo se $u \in H$.
> - L'elemento neutro di $H$ sarà lo stesso $u$.
### Gruppo

> [!note] Gruppo
> $(G, *)$ è un **gruppo** se:
> 1. $*$ è **associativa**
> 2. Esiste un **elemento neutro** $u$
> 3. Ogni elemento ha un **inverso**: $\forall a \in G,\; \exists\, a^{-1} \in G$

> [!note] Gruppo Abeliano
> Gruppo in cui $*$ è **commutativa**: $a * b = b * a$.

---

## Lezione 7 — Anelli, Caratteristica, Cancellabilità, Divisori dello Zero

### Inversa di una Matrice $2 \times 2$

> [!note] Inversa $2 \times 2$
> Sia $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ con $\det(A) = ad - bc \neq 0$:
> $$A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$
### Anello

> [!note] Anello
> $(A, +, \cdot)$ è un **anello** se:
> 1. $(A, +)$ è un **gruppo abeliano**
> 2. $(A, \cdot)$ è un **semigruppo**
> 3. Valgono le **proprietà distributive** (sinistra e destra):
>    $$a \cdot (b + c) = a \cdot b + a \cdot c \qquad (b + c) \cdot a = b \cdot a + c \cdot a$$

> [!note] Anello Commutativo
> $(S,\cdot)$ commutativo
> $a \cdot b = b \cdot a$ per ogni $a, b$.

> [!note] Anello Unitario
> $(S,\cdot)$ monoide
> Esiste un'unità $1_A$ tale che $a \cdot 1_A = 1_A \cdot a = a$.

> [!note] Anello Booleano
> $(S,\cdot) idempotenza prodotto$
> Anello con $a \cdot a = a$ per ogni $a$. Esempio: $(\mathcal{P}(S), \triangle, \cap)$.

### Caratteristica di un Anello Unitario

> [!note] Caratteristica
> $$\mathrm{char}(A) = \min\{m > 0 \mid \underbrace{1_A + \cdots + 1_A}_{m} = 0_A\}$$
> Se tale $m$ non esiste, $\mathrm{char}(A) = 0$.
>
> Esempi: $\mathrm{char}(\mathbb{Z}) = 0$, $\;\mathrm{char}(\mathcal{P}(S), \triangle, \cap) = 2$.

### Elemento Cancellabile

> [!note] Cancellabilità
> $a$ è **cancellabile a sinistra** se $a \cdot b = a \cdot c \Rightarrow b = c$.
> $a$ è **cancellabile a destra** se $b \cdot a = c \cdot a \Rightarrow b = c$.
> **Invertibile $\Longrightarrow$ Cancellabile** (il viceversa non vale in generale).

> [!tip] Dimostrazione — Invertibile $\Longrightarrow$ Cancellabile
> Sia $a$ invertibile con inverso $a'$. Se $a \cdot b = a \cdot c$, moltiplichiamo a sinistra per $a'$:
> $$a' \cdot (a \cdot b) = a' \cdot (a \cdot c) \;\Longrightarrow\; (a' \cdot a) \cdot b = (a' \cdot a) \cdot c \;\Longrightarrow\; u \cdot b = u \cdot c \;\Longrightarrow\; b = c$$
> Analogamente per la cancellabilità a destra. $\blacksquare$
> "$\nLeftarrow$" viceversa non vale

### Divisore dello Zero

> [!note] Divisore dello Zero
> $a \neq 0_A$ è **divisore dello zero** se $\exists\, b \neq 0_A:\; a \cdot b = 0_A$.
> $$a \neq 0 \text{ è divisore dello zero} \;\Longleftrightarrow\; a \text{ non è cancellabile}$$

> [!tip] Dimostrazione — Divisore dello zero $\Longleftrightarrow$ Non cancellabile
>Un elemento $(a \neq 0_A)$ è un divisore dello zero $\Longleftrightarrow (a)$ non è cancellabile rispetto al prodotto $(\cdot)$.
> 
> **($\Longrightarrow$)** Se $a$ è divisore dello zero, $\exists\, b \neq 0_A$ con $a \cdot b = 0_A = a \cdot 0_A$.
> Se $a$ fosse cancellabile, $b = 0_A$: contraddizione.
>
> **($\Longleftarrow$)** Se $a$ non è cancellabile, $\exists\, b \neq c$ con $a \cdot b = a \cdot c$.
> Allora $a \cdot (b - c) = 0_A$ con $b - c \neq 0_A$, dunque $a$ è divisore dello zero. $\square$

---

## Lezione 8 — Omomorfismo, Dominio, Campo, Spazio Vettoriale, Gruppo Simmetrico

### Omomorfismo

> [!note] Omomorfismo
> $f: (S, *) \to (T, \perp)$ è un **omomorfismo** se:
> $$f(a * b) = f(a) \perp f(b) \quad \forall a, b \in S$$
### Dominio d'Integrità e campi

> [!note] Dominio d'Integrità
> Un anello $(A, +, \cdot)$ è un **dominio d'integrità** se:
> - È **commutativo**
> - È **unitario** (con $1_A \neq 0_A$)
> - È **privo di divisori dello zero**
>
> **Esempi:** $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$.

> [!note] Corpo
> Un anello $(K, +, \cdot)$ è un **corpo** se:
> - È **unitario** (con $1_K \neq 0_K$)
> - $(K^*, \cdot)$ è un **gruppo** (dove $K^* = K \setminus \{0_K\}$)
>  Equivalentemente: $\mathcal{U}(K^*) = K \setminus \{0_K\}$, ossia ogni elemento non nullo è invertibile/simmetrizzabile.

> [!note] Campo
> Un **campo** è un **corpo commutativo**, ossia:
> - È un corpo
> - La moltiplicazione "$\cdot$" è **commutativa**
>
> **Esempi:** $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Z}_p$ (con $p$ primo).

>[!abstract] ciao


> [!important] Teorema di Wedderburn
> Ogni **corpo finito** è anche un **campo**.
> - Spiegazione:
> Il teorema dimostra che se l'insieme degli elementi è finito, è matematicamente impossibile costruire una struttura dove valga l'invertibilità senza che valga anche la commutatività
> Quindi se
> $$
> S \text{ è finito e simmetrizzabile} \implies S \text{ è commutativo}
> $$

### Spazio Vettoriale

> [!note] Spazio Vettoriale
> $(V, +)$ gruppo abeliano su un campo $(K, +, \cdot)$ con operazione esterna $\cdot: K \times V \to V$ che soddisfa:
> 1. $\lambda(\mu v) = (\lambda\mu)v$
> 2. $(\lambda + \mu)v = \lambda v + \mu v$
> 3. $\lambda(v + w) = \lambda v + \lambda w$
> 4. $1_K \cdot v = v$

### Gruppo Simmetrico

> [!note] Gruppo Simmetrico $S_n$
> L'insieme di tutte le permutazioni di $\{1, 2, \ldots, n\}$ con l'operazione di composizione.
> $$|S_n| = n!$$
> Non abeliano per $n \geq 3$.

> [!note] Notazione Ciclica
> Ogni permutazione si decompone in **cicli disgiunti** in modo unico (a meno dell'ordine).

---

## Lezione 9 — Tavole di Cayley, Nilpotenti, Divisibilità, MCD, Relazioni Binarie

### Tavole di Cayley

> [!note] Proprietà visibili dalle Tavole
> - **Commutatività** $\Longleftrightarrow$ tabella simmetrica rispetto alla diagonale
> - **Cancellabilità** $\Longleftrightarrow$ nessuna ripetizione nelle righe e colonne

> [!important] Cancellabilità in Strutture Finite
> In un magma **finito** $(S, *)$, un elemento $a$ è **cancellabile** se e solo se la funzione $x \mapsto a * x$ è **iniettiva** (e quindi biettiva, essendo $S$ finito).

### Elemento Nilpotente

> [!note] Nilpotente
> $a \in A$ è **nilpotente** se $\exists\, n \geq 1:\; a^n = 0_A$.
> **Nilpotente non nullo $\Longrightarrow$ Divisore dello zero.**

### Divisibilità

> [!note] Divisibilità
> $$b \mid a \;\Longleftrightarrow\; \exists c:\; a = b \cdot c$$
> $\mathrm{div}(a)$: insieme dei divisori di $a$. $\;\mathrm{mult}(b)$: insieme dei multipli di $b$.

### Elementi Associati

> [!note] Associati
> $x \sim y \;\Longleftrightarrow\; \exists\, u \in U(A):\; x = u \cdot y$.
> È una **relazione di equivalenza**.

### Divisori Banali e Propri

> [!note] Divisori Banali e Propri
> Sia $a \in A$ un anello unitario.
> - I **divisori banali** di $a$ sono gli elementi **associati** a $1$ (cioè gli invertibili $U(A)$) e gli associati ad $a$ stesso.
> - Un **divisore proprio** è un divisore di $a$ che non è né banale né invertibile.

### MCD e mcm

> [!note] Massimo Comun Divisore
> $e = \mathrm{MCD}(a, b)$ se:
> 1. $e \mid a$ e $e \mid b$
> 2. $\forall x:\; (x \mid a \;\wedge\; x \mid b) \Rightarrow x \mid e$

> [!note] Minimo Comune Multiplo
> $m = \mathrm{mcm}(a, b)$ se:
> 1. $a \mid m$ e $b \mid m$
> 2. $\forall x:\; (a \mid x \;\wedge\; b \mid x) \Rightarrow m \mid x$

### Numero Primo

> [!note] Primo
> $p$ è **primo** se $p \notin U(\mathbb{Z})$ e $\mathrm{div}(p) = \{1, -1, p, -p\}$.

> [!important] Lemma di Euclide
> Se $p$ è primo e $p \mid ab$, allora $p \mid a$ oppure $p \mid b$.

> [!tip] Dimostrazione — Lemma di Euclide
> **Caso 1:** Se $p \mid a$, la tesi è soddisfatta.
>
> **Caso 2:** Se $p \nmid a$, poiché $p$ è primo si ha $\mathrm{MCD}(p, a) = 1$.
> Per l'identità di Bézout, $\exists\, x, y \in \mathbb{Z}$ tali che $px + ay = 1$.
> Moltiplicando per $b$: $pxb + aby = b$.
> Ora $p \mid pxb$ (banalmente) e $p \mid aby$ (perché $p \mid ab$).
> Quindi $p \mid (pxb + aby) = b$. $\square$

### Relazioni Binarie — Proprietà

> [!note] Proprietà di una Relazione $R \subseteq A \times A$
> | Proprietà | Definizione |
> |:----------|:-----------|
> | **Riflessiva** | $\forall x \in A,\; xRx$ |
> | **Antiriflessiva** | $\forall x \in A,\; \neg(xRx)$ |
> | **Simmetrica** | $xRy \Rightarrow yRx$ |
> | **Asimmetrica** | $xRy \Rightarrow \neg(yRx)$; implica antiriflessività |
> | **Antisimmetrica** | $(xRy \wedge yRx) \Rightarrow x = y$ |
> | **Transitiva** | $(xRy \wedge yRz) \Rightarrow xRz$ |

---

## Lezione 10 — Buon Ordinamento, Induzione, Divisione Euclidea, Relazione d'Equivalenza

### Insieme Ben Ordinato

> [!note] Ben Ordinato
> $(S, \leq)$ è **ben ordinato** se ogni sottoinsieme non vuoto ammette un **minimo**.
> Ben ordinato $\Longrightarrow$ totalmente ordinato.
> Esempio: $(\mathbb{N}, \leq)$.

### Principio di Induzione

> [!note] Forma I (Standard)
> Se $P(\bar{n})$ è vera e $\forall n \geq \bar{n}:\; P(n) \Rightarrow P(n+1)$, allora $P(n)$ è vera $\forall n \geq \bar{n}$.

> [!note] Forma II (Forte)
> Se $P(\bar{n})$ è vera e $\forall n > \bar{n}:\; \bigl[\forall i\;(\bar{n} \leq i < n \Rightarrow P(i))\bigr] \Rightarrow P(n)$, allora $P(n)$ è vera $\forall n \geq \bar{n}$.

### Divisione Euclidea

> [!important] Teorema della Divisione Euclidea
> $\forall\, m \in \mathbb{Z},\; n \in \mathbb{Z} \setminus \{0\},\; \exists!\, q, r \in \mathbb{Z}:$
> $$m = n \cdot q + r, \qquad 0 \leq r < |n|$$
> [!tip] Dimostrazione — Divisione Euclidea
> **Esistenza** (per induzione forte su $m$, $m, n > 0$):
> - *Base:* Se $0 \le m < n$, basta prendere $q = 0$ e $r = m$.
> - *Passo:* Se $m \ge n$, poniamo $\bar{m} = m - n \ge 0$. Poiché $\bar{m} < m$, per ipotesi induttiva $\bar{m} = n\bar{q} + \bar{r}$ con $0 \le \bar{r} < n$.
>   Allora $m = \bar{m} + n = n(\bar{q} + 1) + \bar{r}$, con $q = \bar{q} + 1$ e $r = \bar{r}$.
>
> **Unicità:** Supponiamo $m = nq_1 + r_1 = nq_2 + r_2$ con $0 \le r_1, r_2 < |n|$.
> Sottraendo: $n(q_1 - q_2) = r_2 - r_1$.
> Poiché $|r_2 - r_1| < |n|$, l'unico multiplo di $n$ in quell'intervallo è $0$.
> Quindi $r_1 = r_2$ e $q_1 = q_2$. $\square$

### Identità di Bézout

> [!important] Identità di Bézout
> $$\mathrm{MCD}(a, b) = a \cdot x + b \cdot y \quad \text{per opportuni } x, y \in \mathbb{Z}$$
> Corollario: $a, b$ coprimi $\Longleftrightarrow$ $\exists\, x, y:\; ax + by = 1$.

> [!tip] Dimostrazione — Identità di Bézout
> 1. Sia $S = \{as + bt \mid s, t \in \mathbb{Z},\; as + bt > 0\}$.
> 2. $S \neq \emptyset$: se $a \neq 0$, $|a| = a \cdot (\pm 1) + b \cdot 0 \in S$; analogamente per $b$.
> 3. Per il **principio del buon ordinamento**, $S$ ammette un minimo $d = ax + by$.
> 4. **$d \mid a$:** Dividiamo $a = dq + r$ con $0 \le r < d$. Allora:
>    $$r = a - dq = a - (ax + by)q = a(1 - xq) + b(-yq)$$
>    Se $r > 0$, allora $r \in S$ con $r < d$, contraddicendo la minimalità di $d$. Dunque $r = 0$.
> 5. **$d \mid b$:** Analogamente.
> 6. **$d = \mathrm{MCD}(a,b)$:** Se $c \mid a$ e $c \mid b$, allora $c \mid (ax + by) = d$, dunque $d$ è il massimo. $\square$

### Relazione d'Equivalenza

> [!note] Equivalenza
> Una relazione $R$ su $A$ è di **equivalenza** se è:
> 1. **Riflessiva**
> 2. **Simmetrica**
> 3. **Transitiva**

### Relazione d'Ordine

> [!note] Ordine (Parziale)
> Una relazione su $A$ è d'**ordine** se è riflessiva, **antisimmetrica** e transitiva.
> È **totale** se $\forall x, y:\; xRy \vee yRx$.

---

## Lezione 11 — Algoritmo di Euclide, Bézout, FTA, Classi di Equivalenza

### Algoritmo di Euclide

> [!note] Algoritmo di Euclide
> Calcola $\mathrm{MCD}(a, b)$ tramite divisioni successive: si divide ripetutamente il dividendo per il resto, finché il resto è $0$. L'ultimo resto non nullo è il MCD.

### Algoritmo Esteso di Euclide

> [!note] Algoritmo Esteso
> Risalendo le divisioni dell'Algoritmo di Euclide, si trovano i **coefficienti di Bézout** $x, y$ tali che $ax + by = \mathrm{MCD}(a, b)$.

### Teorema Fondamentale dell'Aritmetica

> [!important] FTA
> Ogni intero $n \geq 2$ si scrive in modo **unico** (a meno dell'ordine) come prodotto di numeri primi:
> $$n = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_k^{\alpha_k}$$
### Classi di Equivalenza

> [!note] Classe di Equivalenza
> $$[a]_R = \{x \in S \mid x \mathrel{R} a\}$$
> Proprietà:
> - Ogni classe è **non vuota** ($a \in [a]$)
> - Due classi sono **uguali o disgiunte**
> - L'unione di tutte le classi è $S$ — formano una **partizione**

### Insieme Quoziente

> [!note] Insieme Quoziente
> $$S / R = \{[a]_R \mid a \in S\}$$
> L'insieme di tutte le classi di equivalenza.

> [!important] Teorema
> Esiste una corrispondenza biunivoca tra relazioni di equivalenza su $S$ e partizioni di $S$.

> [!tip] Dimostrazione — Equivalenza $\longleftrightarrow$ Partizioni
> **(i) Equivalenza $\Longrightarrow$ Partizione.**
> Le classi di equivalenza $S/\mathcal{R}$ formano una partizione:
> - Ogni classe è non vuota ($a \in [a]$).
> - Due classi sono uguali o disgiunte: se $[a] \cap [b] \neq \emptyset$, esiste $c \in [a] \cap [b]$, dunque $a \mathrel{R} c$ e $c \mathrel{R} b$, da cui $a \mathrel{R} b$ e $[a] = [b]$.
> - L'unione di tutte le classi è $S$.
>
> **(ii) Partizione $\Longrightarrow$ Equivalenza.**
> Data una partizione $\mathcal{F}$, definiamo $a \mathrel{R}_{\mathcal{F}} b \iff$ $a$ e $b$ appartengono allo stesso blocco.
> - *Riflessiva:* $a$ appartiene a qualche blocco, dunque $a \mathrel{R}_{\mathcal{F}} a$.
> - *Simmetrica:* banale.
> - *Transitiva:* se $a \mathrel{R} b$ e $b \mathrel{R} c$, allora $b$ sta nei blocchi di $a$ e di $c$; poiché i blocchi sono disgiunti, è lo stesso blocco, dunque $a \mathrel{R} c$.
>
> Le due costruzioni sono una l'inversa dell'altra: $S/\mathcal{R}_{\mathcal{F}} = \mathcal{F}$. $\square$

---

## Lezione 12 — Equivalenza ↔ Partizioni, Congruenza, Anello $\mathbb{Z}_m$

### Relazione di Equivalenza Indotta da Funzione

> [!note] Equivalenza indotta
> Data $f: S \to T$, si definisce $x \mathrel{R_f} y \;\Longleftrightarrow\; f(x) = f(y)$.
> Questa è una relazione di equivalenza su $S$.

> [!tip] Dimostrazione — $R_f$ è di equivalenza
> - *Riflessiva:* $f(x) = f(x)$.
> - *Simmetrica:* $f(x) = f(y) \Rightarrow f(y) = f(x)$.
> - *Transitiva:* $f(x) = f(y)$ e $f(y) = f(z) \Rightarrow f(x) = f(z)$. $\square$

### Applicazione Quoziente (Fattorizzazione)

> [!note] Fattorizzazione
> Data $f: S \to T$ e la relazione $R_f$, l'**applicazione quoziente** è:
> $$\bar{f}: S/R_f \to T, \qquad \bar{f}([a]) = f(a)$$
> È **ben definita** e **iniettiva**. Vale $f = \bar{f} \circ \pi$ (dove $\pi$ è la proiezione canonica).

> [!tip] Dimostrazione — Fattorizzazione
> **Ben definita:** Se $[a] = [b]$, allora $a \mathrel{R_f} b$, cioè $f(a) = f(b)$, dunque $\bar{f}([a]) = \bar{f}([b])$.
>
> **Iniettiva:** Se $\bar{f}([a]) = \bar{f}([b])$, allora $f(a) = f(b)$, dunque $a \mathrel{R_f} b$, cioè $[a] = [b]$. $\square$

### Congruenza (Compatibilità)

> [!note] Congruenza
> Una relazione di equivalenza $R$ su $(S, \perp)$ è una **congruenza** se:
> $$a \mathrel{R} c \;\wedge\; b \mathrel{R} d \;\Longrightarrow\; (a \perp b) \mathrel{R} (c \perp d)$$
> Questo rende l'operazione quoziente **ben definita**.

### Congruenza Modulo $m$

> [!note] Congruenza Modulo $m$
> $$a \equiv b \pmod{m} \;\Longleftrightarrow\; m \mid (a - b)$$
> Equivalentemente: $a$ e $b$ hanno lo **stesso resto** nella divisione per $m$.
>
> Casi particolari:
> - $m = 0$: la congruenza è l'**uguaglianza**
> - $m = 1$: la relazione è **totale** (sempre vera)

> [!note] Compatibilità con $+$ e $\cdot$
> Se $a \equiv c$ e $b \equiv d$ $\pmod{m}$, allora:
> $$a + b \equiv c + d \pmod{m} \qquad a \cdot b \equiv c \cdot d \pmod{m}$$
> [!tip] Dimostrazione — Compatibilità
> Sia $a - c = mh$ e $b - d = mk$.
>
> **Somma:** $(a + b) - (c + d) = (a - c) + (b - d) = mh + mk = m(h + k)$, dunque $m \mid (a + b) - (c + d)$.
>
> **Prodotto:** $ab = (c + mh)(d + mk) = cd + m(ck + hd + mhk)$, dunque $ab - cd = m(ck + hd + mhk)$ e $m \mid (ab - cd)$. $\square$

> [!note] Anello $\mathbb{Z}_m$
> L'insieme quoziente $\mathbb{Z}_m = \{[0]_m, [1]_m, \ldots, [m-1]_m\}$ con:
> $$[a] + [b] = [a + b], \qquad [a] \cdot [b] = [a \cdot b]$$
> è un **anello commutativo unitario**.

---

## Lezione 13 — Classi di Resto, $\mathbb{Z}_m$ Campo, Invertibili, Nilpotenti, Equazioni Congruenziali

### $\mathbb{Z}_m$ è un Campo

> [!important] Teorema
> $(\mathbb{Z}_m, +, \cdot)$ è un **campo** se e solo se $m$ è un numero **primo**.

> [!tip] Dimostrazione — $\mathbb{Z}_m$ campo $\Longleftrightarrow$ $m$ primo
> $\mathbb{Z}_m$ è un campo $\iff$ ogni $[a] \neq [0]$ è invertibile
> $\iff$ $\forall a \in \{1, \ldots, m-1\}:\; \mathrm{MCD}(a, m) = 1$
> $\iff$ $m$ non ha divisori propri $\iff$ $m$ è primo. $\square$

### Caratteristica di $\mathbb{Z}_m$

> [!note] Caratteristica
> $$\mathrm{char}(\mathbb{Z}_m) = m$$
> [!tip] Dimostrazione — $\mathrm{char}(\mathbb{Z}_m) = m$
> $\underbrace{[1] + [1] + \cdots + [1]}_{k \text{ volte}} = [k] = [0] \iff m \mid k$.
> Il più piccolo $k > 0$ tale che $m \mid k$ è $k = m$. $\square$

### Invertibili e Divisori dello Zero in $\mathbb{Z}_m$

> [!note] Invertibili
> $[a]_m$ è **invertibile** in $\mathbb{Z}_m$ $\;\Longleftrightarrow\;$ $\mathrm{MCD}(a, m) = 1$.

> [!note] Divisori dello Zero
> $[a]_m \neq [0]_m$ è **divisore dello zero** in $\mathbb{Z}_m$ $\;\Longleftrightarrow\;$ $\mathrm{MCD}(a, m) > 1$.

> [!note] Dicotomia
> In $\mathbb{Z}_m$, ogni $[a] \neq [0]$ è **o invertibile o divisore dello zero**.

> [!tip] Dimostrazione — Invertibili e Divisori dello Zero in $\mathbb{Z}_m$
> Sia $d = \mathrm{MCD}(a, m)$.
>
> **Invertibile $\Longleftarrow$ $d = 1$:** Per Bézout, $\exists\, h, k \in \mathbb{Z}$ con $ah + mk = 1$.
> In $\mathbb{Z}_m$: $\bar{a} \cdot \bar{h} = \overline{ah} = \overline{1 - mk} = \bar{1}$.
>
> **Invertibile $\Longrightarrow$ $d = 1$:** Se $\bar{a} \cdot \bar{b} = \bar{1}$, allora $ab - mk = 1$ per qualche $k$.
> Questa è un'identità di Bézout, dunque $\mathrm{MCD}(a, m) = 1$.
>
> **Div. zero $\Longleftarrow$ $d > 1$:** Poniamo $a = da_1$ e $m = dm_1$.
> Allora $\bar{a} \cdot \overline{m_1} = \overline{a_1 m} = \bar{0}$ con $\overline{m_1} \neq \bar{0}$ (poiché $m_1 < m$).
>
> **Div. zero $\Longrightarrow$ $d > 1$:** Se $\bar{a} \cdot \bar{b} = \bar{0}$ con $\bar{b} \neq \bar{0}$, allora $m \mid ab$.
> Se fosse $d = 1$, per il Lemma di Euclide $m \mid b$, cioè $\bar{b} = \bar{0}$: contraddizione. $\square$

### Elementi Nilpotenti in $\mathbb{Z}_m$

> [!note] Nilpotenti in $\mathbb{Z}_m$
> Sia $m = p_1^{\alpha_1} \cdots p_t^{\alpha_t}$. Allora $[a]_m$ è nilpotente se e solo se $a$ è multiplo di $\mathrm{rad}(m) = p_1 \cdot p_2 \cdots p_t$.

### Equazioni Congruenziali

> [!important] Teorema di Risolubilità
> L'equazione $ax \equiv b \pmod{m}$ ha soluzione $\;\Longleftrightarrow\;$ $d \mid b$, dove $d = \mathrm{MCD}(a, m)$.
> Se ha soluzione, ci sono esattamente **$d$ soluzioni distinte** modulo $m$.
> Se $d = 1$, la soluzione unica è $x \equiv a^{-1} b \pmod{m}$.

---

## Lezione 14 — Idempotenti, Criteri di Divisibilità

### Elemento Idempotente

> [!note] Idempotente in $\mathbb{Z}_m$
> $[a]_m$ è **idempotente** se $[a]^2 = [a]$, cioè $m \mid a(a-1)$.
> Sempre idempotenti: $[0]$ e $[1]$.

### Criteri di Divisibilità (via Aritmetica Modulare)

> [!note] Formula Generale
> Sia $n = c_k \cdot 10^k + \cdots + c_1 \cdot 10 + c_0$. Allora:
> $$n \equiv \sum_{i=0}^{k} c_i \cdot (10^i \bmod m) \pmod{m}$$
| Divisore | Criterio |
|:---------|:---------|
| $2, 5, 10$ | Ultima cifra ($10 \equiv 0$) |
| $4, 25, 100$ | Ultime due cifre ($100 \equiv 0$) |
| $3, 9$ | Somma delle cifre ($10 \equiv 1$) |
| $11$ | Somma a segni alterni ($10 \equiv -1$) |

---

## Lezione 15 — Dominio, Anello Prodotto, Caratteristica del Prodotto

### Corollario: $\mathbb{Z}_n$ Dominio d'Integrità

> [!note] Dominio
> $\mathbb{Z}_n$ è un **dominio d'integrità** $\;\Longleftrightarrow\;$ $n$ è primo $\;\Longleftrightarrow\;$ $\mathbb{Z}_n$ è un campo.

### Anello Prodotto

> [!note] Anello Prodotto $\mathbb{Z}_m \times \mathbb{Z}_n$
> Operazioni **componente per componente**:
> $$(\bar{a}, \tilde{b}) + (\bar{c}, \tilde{d}) = (\overline{a+c},\, \widetilde{b+d})$$
> $$(\bar{a}, \tilde{b}) \cdot (\bar{c}, \tilde{d}) = (\overline{a \cdot c},\, \widetilde{b \cdot d})$$
> - $0_R = ([0]_m, [0]_n)$, $\;1_R = ([1]_m, [1]_n)$
> - $(\bar{a}, \tilde{b}) \in U(R) \;\Longleftrightarrow\; \bar{a} \in U(\mathbb{Z}_m) \;\wedge\; \tilde{b} \in U(\mathbb{Z}_n)$

### Caratteristica del Prodotto

> [!note] Caratteristica dell'Anello Prodotto
> $$\mathrm{char}(\mathbb{Z}_m \times \mathbb{Z}_n) = \mathrm{mcm}(\mathrm{char}(\mathbb{Z}_m),\, \mathrm{char}(\mathbb{Z}_n)) = \mathrm{mcm}(m, n)$$
---

## Lezione 16 — Equazioni Diofantee, Totiente di Eulero, Fermat-Eulero, Calcolo Combinatorio

### Equazione Diofantea Lineare

> [!note] Equazione Diofantea
> $ax + by = c$ con $a, b, c \in \mathbb{Z}$, soluzioni $x, y \in \mathbb{Z}$.
> Ha soluzione $\;\Longleftrightarrow\;$ $\mathrm{MCD}(a, b) \mid c$.

### Funzione Totiente di Eulero

> [!note] Funzione $\varphi(n)$
> $$\varphi(n) = |U(\mathbb{Z}_n)| = |\{k \in \{0, \ldots, n-1\} \mid \mathrm{MCD}(k, n) = 1\}|$$
>
> Proprietà:
> - $\varphi(p) = p - 1$ se $p$ è primo
> - $\varphi(p^k) = p^{k-1}(p - 1)$
> - $\varphi(ab) = \varphi(a)\varphi(b)$ se $\mathrm{MCD}(a, b) = 1$ (moltiplicativa)

### Teorema di Fermat-Eulero

> [!important] Fermat-Eulero
> Se $\mathrm{MCD}(a, n) = 1$, allora:
> $$a^{\varphi(n)} \equiv 1 \pmod{n}$$
> [!important] Piccolo Teorema di Fermat
> Se $p$ è primo e $p \nmid a$:
> $$a^{p-1} \equiv 1 \pmod{p}$$
### Coefficiente Binomiale

> [!note] Coefficiente Binomiale
> $$\binom{n}{k} = \frac{n!}{k!\,(n-k)!} \qquad \text{per } 0 \leq k \leq n$$
> Simmetria: $\binom{n}{k} = \binom{n}{n-k}$.

### Identità di Pascal

> [!important] Identità di Pascal
> $$\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$$
> [!tip] Dimostrazione — Identità di Pascal
> $$\binom{n}{k} + \binom{n}{k-1} = \frac{n!}{k!\,(n-k)!} + \frac{n!}{(k-1)!\,(n-k+1)!}$$
> $$= \frac{n!\,(n-k+1) + n!\,k}{k!\,(n-k+1)!} = \frac{n!\,(n+1)}{k!\,(n+1-k)!} = \frac{(n+1)!}{k!\,(n+1-k)!} = \binom{n+1}{k}$$
> $\square$

### Somma dei Coefficienti Binomiali

> [!note] Somma
> $$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$
> [!tip] Dimostrazione — $|\mathcal{P}(S)| = 2^{|S|}$ (per induzione)
> *Base:* $n = 0$: $|\mathcal{P}(\emptyset)| = |\{\emptyset\}| = 1 = 2^0$.
>
> *Passo:* Sia $|S| = n$ e $T = S \cup \{a\}$ con $a \notin S$.
> I sottoinsiemi di $T$ si dividono in quelli che **non contengono** $a$ (sono i sottoinsiemi di $S$, cioè $2^n$) e quelli che **contengono** $a$ (sono $X \cup \{a\}$ al variare di $X \subseteq S$, cioè ancora $2^n$).
> Totale: $2^n + 2^n = 2^{n+1}$. $\square$

### Applicazioni Iniettive

> [!note] Conteggio
> Il numero di applicazioni iniettive $f: S \to T$ con $|S| = n$, $|T| = m$, $n \leq m$:
> $$\frac{m!}{(m-n)!}$$
> [!tip] Dimostrazione — Conteggio applicazioni iniettive (per induzione su $n$)
> *Base:* $n = 1$: $f$ sceglie l'immagine di $a_1$ tra $m$ elementi: $m = \frac{m!}{(m-1)!}$.
>
> *Passo:* Per l'elemento $a_{n+1}$, l'immagine può essere uno qualsiasi degli $m$ elementi di $T$, ma per iniettività deve essere diverso dalle immagini di $a_1, \ldots, a_n$.
> Scelta l'immagine $b_i$ di $a_{n+1}$ ($m$ scelte), le restanti $n$ variabili definiscono un'applicazione iniettiva da $S$ a $T \setminus \{b_i\}$ ($m-1$ elementi). Per ipotesi induttiva, queste sono $\frac{(m-1)!}{(m-1-n)!}$.
> Totale: $m \cdot \frac{(m-1)!}{(m-1-n)!} = \frac{m!}{(m-n-1)!} = \frac{m!}{(m-(n+1))!}$. $\square$

### Binomio di Newton

> [!important] Binomio di Newton
> $$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k}\, a^{n-k}\, b^k$$
> [!tip] Dimostrazione — Binomio di Newton (per induzione su $n$)
> *Base:* $n = 0$: $(a+b)^0 = 1 = \binom{0}{0} a^0 b^0$.
>
> *Passo:* $(a+b)^{n+1} = (a+b)^n \cdot (a+b)$. Per ipotesi induttiva:
> $$= \left(\sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k\right)(a+b)$$
> $$= \sum_{k=0}^{n} \binom{n}{k} a^{n+1-k} b^k + \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^{k+1}$$
> Ri-indicizzando la seconda somma ($j = k+1$):
> $$= a^{n+1} + \sum_{k=1}^{n} \left[\binom{n}{k} + \binom{n}{k-1}\right] a^{n+1-k} b^k + b^{n+1}$$
> Per l'identità di Pascal, $\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$, ottenendo:
> $$= \sum_{k=0}^{n+1} \binom{n+1}{k} a^{n+1-k} b^k \quad \square$

---

## Lezione 17 — Relazioni d'Ordine, Hasse, Estremi

### Relazione d'Ordine Largo

> [!note] Ordine Largo
> $\mathcal{R}$ su $S$ è d'**ordine** se è:
> 1. **Riflessiva**
> 2. **Antisimmetrica**
> 3. **Transitiva**

### Relazione d'Ordine Stretto

> [!note] Ordine Stretto
> $\mathcal{R}'$ su $S$ è d'**ordine stretto** se è:
> 1. **Antiriflessiva**
> 2. **Transitiva**
>
> Implica automaticamente l'**asimmetria**.

### Corrispondenza Largo ↔ Stretto

> [!note] Corrispondenza
> $$x <  y \;\Longleftrightarrow\; (x \leq y \;\wedge\; x \neq y)$$
> $$x \leq y \;\Longleftrightarrow\; (x < y \;\vee\; x = y)$$
### Ordine Totale

> [!note] Ordine Totale
> $\forall x, y \in S:\; x \leq y \;\vee\; y \leq x$ (ogni coppia è confrontabile).

### Copertura

> [!note] Copertura
> $b$ **copre** $a$ se $a < b$ e $\nexists\, c:\; a < c < b$.

### Diagramma di Hasse

> [!note] Diagramma di Hasse
> Rappresentazione grafica di un poset finito: si disegnano solo le relazioni di **copertura**, con l'elemento maggiore in alto.

### Elemento Minimo / Massimo

> [!note] Minimo e Massimo
> - $a$ è **minimo** se $a \leq x$ per ogni $x \in S$. Se esiste, è **unico**.
> - $a$ è **massimo** se $x \leq a$ per ogni $x \in S$. Se esiste, è **unico**.

### Elemento Minimale / Massimale

> [!note] Minimale e Massimale
> - $a$ è **minimale** se $\nexists\, x:\; x < a$.
> - $a$ è **massimale** se $\nexists\, x:\; a < x$.
> - Minimo $\Longrightarrow$ unico minimale. Ma un minimale unico **non** è necessariamente il minimo.

> [!important] Teorema (Poset Finiti)
> Ogni insieme **finito non vuoto** parzialmente ordinato possiede almeno un elemento **minimale** e almeno un elemento **massimale**.

### Minoranti, Maggioranti, Inf, Sup

> [!note] Minorante e Maggiorante
> Sia $X \subseteq S$:
> - **Minorante** di $X$: $a \leq x\;\forall x \in X$
> - **Maggiorante** di $X$: $x \leq a\;\forall x \in X$

> [!note] Infimo e Supremo
> - $\inf(X) = \max(\text{minoranti di } X)$
> - $\sup(X) = \min(\text{maggioranti di } X)$
>
> Se $\min(X)$ esiste, allora $\inf(X) = \min(X)$. Analogamente per $\max$ e $\sup$.

---

## Lezione 19 — Ordini (recap), Divisibilità come Ordine, Ordine Indotto

### Divisibilità su $\mathbb{N}^*$

> [!note] Divisibilità come Ordine
> $(\mathbb{N}^*, \mid)$ è un **ordine parziale**.
> $(\mathbb{Z}, \mid)$ **non** è un ordine (non è antisimmetrica: $2 \mid {-2}$ e ${-2} \mid 2$ ma $2 \neq -2$).

### Ordine Indotto da Funzione

> [!note] Ordine Indotto
> Data $f: S \to T$ e $(T, \leq_T)$ ordinato:
> $$a \leq_f b \;\Longleftrightarrow\; (a = b) \;\vee\; (f(a) <_T f(b))$$
> Questa è una relazione d'ordine su $S$.

---

## Lezione 20 — Reticoli

### Reticolo (Definizione tramite Ordine)

> [!note] Reticolo
> Un poset $(L, \leq)$ è un **reticolo** se per ogni $a, b \in L$ esistono:
> - $\inf\{a, b\} = a \wedge b$ (**meet**)
> - $\sup\{a, b\} = a \vee b$ (**join**)

### Reticolo (Definizione Algebrica)

> [!note] Reticolo (algebrico)
> $(L, \wedge, \vee)$ è un **reticolo** se $\wedge$ e $\vee$ soddisfano:
> 1. **Associatività**: $(a \wedge b) \wedge c = a \wedge (b \wedge c)$, $\;(a \vee b) \vee c = a \vee (b \vee c)$
> 2. **Commutatività**: $a \wedge b = b \wedge a$, $\;a \vee b = b \vee a$
> 3. **Assorbimento**: $a \wedge (a \vee b) = a$, $\;a \vee (a \wedge b) = a$

### Idempotenza (derivata)

> [!note] Idempotenza
> Dalle leggi di assorbimento:
> $$a \wedge a = a, \qquad a \vee a = a$$
### Equivalenza tra le Due Definizioni

> [!important] Teorema
> Le due definizioni sono equivalenti. La relazione d'ordine si recupera da:
> $$a \leq b \;\Longleftrightarrow\; a \wedge b = a \;\Longleftrightarrow\; a \vee b = b$$
> [!tip] Dimostrazione — Algebrico ⟹ Ordine
> Data $(L, \wedge, \vee)$ con le proprietà algebriche, definiamo $a \leq b \iff a \wedge b = a$.
> - *Riflessiva:* $a \wedge a = a$ (idempotenza).
> - *Antisimmetrica:* $a \wedge b = a$ e $b \wedge a = b$; per commutatività, $a = b$.
> - *Transitiva:* $a \wedge b = a$ e $b \wedge c = b$. Allora:
>   $a \wedge c = (a \wedge b) \wedge c = a \wedge (b \wedge c) = a \wedge b = a$.
>
> Infine $\inf\{a,b\} = a \wedge b$: infatti $(a \wedge b) \wedge a = a \wedge b$ e $(a \wedge b) \wedge b = a \wedge b$, dunque $a \wedge b \leq a$ e $a \wedge b \leq b$. Se $c \leq a$ e $c \leq b$, allora $c \wedge (a \wedge b) = (c \wedge a) \wedge b = c \wedge b = c$, cioè $c \leq a \wedge b$. $\square$

### Esempio Fondamentale

> [!note] $(\mathcal{P}(S), \subseteq)$ è un Reticolo
> Con $A \wedge B = A \cap B$ e $A \vee B = A \cup B$.
### Catena

> [!note] Catena
> Un sottoinsieme $C \subseteq S$ di un insieme parzialmente ordinato $(S, \leq)$ è una **catena** se è **totalmente ordinato**:
> $$\forall x, y \in C:\; x \leq y \;\vee\; y \leq x$$
> [!note] Catena Massimale
> Una catena $C$ in $(S, \leq)$ è **massimale** se non può essere estesa: non esiste alcun elemento $s \in S \setminus C$ tale che $C \cup \{s\}$ sia ancora una catena.
---

## Lezione 21 — Reticoli Limitati, Sottoreticoli, Isomorfismi, Reticoli Complementati, Prodotto

### Reticolo Limitato

> [!note] Reticolo Limitato
> Un reticolo $L$ è **limitato** se possiede:
> - Elemento **minimo** $0_L$: $\;0_L \leq a\;\forall a$, ossia $a \vee 0_L = a$
> - Elemento **massimo** $1_L$: $\;a \leq 1_L\;\forall a$, ossia $a \wedge 1_L = a$
>
> **Ogni reticolo finito è limitato.**

> [!important] Insieme Totalmente Ordinato ⇒ Reticolo
> Se $(S, \leq)$ è un insieme **totalmente ordinato**, allora è un **reticolo**.
> Per ogni $a, b \in S$: se $a \leq b$, allora $a \wedge b = a$ e $a \vee b = b$.

> [!important] Reticolo Finito ⇒ Limitato
> Ogni reticolo **finito** è **limitato**: possiede sempre un elemento minimo $0_L$ e un elemento massimo $1_L$.

### Sottoreticolo

> [!note] Sottoreticolo
> $A \subseteq L$ non vuoto è un **sottoreticolo** se è chiuso per $\wedge$ e $\vee$:
> $$\forall x, y \in A:\; x \wedge y \in A \;\wedge\; x \vee y \in A$$
### Isomorfismo di Reticoli

> [!note] Isomorfismo di Poset / Reticoli
> $f: L \to M$ biettiva è un **isomorfismo** se:
> $$a \leq_L b \;\Longleftrightarrow\; f(a) \leq_M f(b)$$
> Equivalentemente, preserva $\wedge$ e $\vee$:
> $$f(a \wedge b) = f(a) \wedge f(b), \qquad f(a \vee b) = f(a) \vee f(b)$$
### Reticolo Complementato

> [!note] Complementato
> Un reticolo **limitato** è **complementato** se per ogni $a \in L$ esiste almeno un $\bar{a} \in L$ tale che:
> $$a \wedge \bar{a} = 0_L \qquad \text{e} \qquad a \vee \bar{a} = 1_L$$
### Reticolo Prodotto

> [!note] Reticolo Prodotto
> Dati $(L_1, \leq_1)$ e $(L_2, \leq_2)$ reticoli, $L_1 \times L_2$ è un reticolo con:
> $$(a, b) \leq (c, d) \;\Longleftrightarrow\; a \leq_1 c \;\wedge\; b \leq_2 d$$
> $$(a, b) \wedge (c, d) = (a \wedge_1 c,\; b \wedge_2 d)$$
> $$(a, b) \vee (c, d) = (a \vee_1 c,\; b \vee_2 d)$$
### Reticolo dei Divisori

> [!note] Reticolo $(\mathbb{D}_n, \mid)$
> L’insieme dei divisori positivi di $n$, ordinato per divisibilità, forma un **reticolo limitato**:
> - $a \wedge b = \mathrm{MCD}(a, b)$
> - $a \vee b = \mathrm{mcm}(a, b)$
> - $0_L = 1$, $\;1_L = n$

---

## Lezione 22 — Sottoanelli, Dualità, Reticoli Distributivi e Booleani, Algebre di Boole, Anelli Booleani

### Sottoanello

> [!note] Sottoanello
> Sia $(A, +, \cdot)$ un anello e $B \subseteq A$, $B \neq \emptyset$.
> $(B, +, \cdot)$ è un **sottoanello** se $B$ è chiuso per **sottrazione** e **moltiplicazione**:
> $$\forall b_1, b_2 \in B:\; b_1 - b_2 \in B \;\wedge\; b_1 \cdot b_2 \in B$$
### Principio di Dualità per Reticoli

> [!important] Principio di Dualità
> Se un enunciato vale per **tutti** i reticoli, anche l'enunciato **duale** vale, ottenuto scambiando:
> $$\leq \;\longleftrightarrow\; \geq, \qquad \wedge \;\longleftrightarrow\; \vee, \qquad 0_L \;\longleftrightarrow\; 1_L$$
### Reticolo Distributivo

> [!note] Distributivo
> Un reticolo è **distributivo** se:
> $$a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$$
> $$a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$$
> (Le due leggi sono equivalenti per dualità.)

> [!important] Teorema ($M_3$, $N_5$)
> Un reticolo è distributivo $\;\Longleftrightarrow\;$ **non contiene** sottoreticoli isomorfi a $M_3$ (diamante) o $N_5$ (pentagono).

> [!note] Reticolo Pentagonale $N_5$
> Il reticolo con 5 elementi $\{0, a, b, c, 1\}$ dove $0 < a < b < 1$ e $0 < c < 1$ con $c$ non confrontabile con $a$ e $b$. **Non è distributivo** né modulare.

> [!note] Reticolo Diamante $M_3$
> Il reticolo con 5 elementi $\{0, a, b, c, 1\}$ dove $a, b, c$ sono mutuamente non confrontabili e $0 < a, b, c < 1$. **Non è distributivo** (ma è modulare).

> [!tip] Dimostrazione — $M_3$ e $N_5$ non sono distributivi
> **$M_3$:** Scegliamo $a, b, c$ i tre atomi mutuamente non confrontabili.
> $a \wedge (b \vee c) = a \wedge 1 = a$.
> $(a \wedge b) \vee (a \wedge c) = 0 \vee 0 = 0$.
> Poiché $a \neq 0$, la distributività fallisce.
>
> **$N_5$** ($0 < a < b < 1$ e $0 < c < 1$, $c$ non confrontabile con $a, b$):
> $a \vee (b \wedge c) = a \vee 0 = a$.
> $(a \vee b) \wedge (a \vee c) = b \wedge 1 = b$.
> Poiché $a \neq b$, la distributività fallisce. $\square$

### Unicità del Complemento

> [!important] Proposizione
> In un reticolo **distributivo e limitato**, se un elemento ha un complemento, questo è **unico**.

> [!tip] Dimostrazione — Unicità del Complemento
> Siano $\bar{a}$ e $\hat{a}$ due complementi di $a$. Allora:
> $$\bar{a} = \bar{a} \wedge 1 = \bar{a} \wedge (a \vee \hat{a}) = (\bar{a} \wedge a) \vee (\bar{a} \wedge \hat{a}) = 0 \vee (\bar{a} \wedge \hat{a}) = \bar{a} \wedge \hat{a}$$
> Analogamente $\hat{a} = \hat{a} \wedge \bar{a}$. Per commutatività di $\wedge$, $\bar{a} = \hat{a}$. $\square$

### Reticolo Booleano

> [!note] Reticolo Booleano
> Un reticolo è **booleano** se è **distributivo** e **complementato**.
>
> Esempio fondamentale: $(\mathcal{P}(S), \subseteq)$.

> [!important] Teorema di Rappresentazione
> Ogni reticolo booleano **finito** è isomorfo a $(\mathcal{P}(S), \subseteq)$ per qualche insieme finito $S$.
> Pertanto $|L| = 2^n$.

### Algebra di Boole

> [!note] Algebra di Boole
> $(A, \wedge, \vee, ', 0, 1)$ dove $\wedge, \vee$ sono binarie, $'$ è unaria, e valgono:
> 1. **Associatività** di $\wedge$ e $\vee$
> 2. **Commutatività** di $\wedge$ e $\vee$
> 3. **Assorbimento**: $a \wedge (a \vee b) = a$, $\;a \vee (a \wedge b) = a$
> 4. **Distributività**: $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$
> 5. **Elementi neutri**: $a \wedge 1 = a$, $\;a \vee 0 = a$
> 6. **Complemento**: $a \wedge a' = 0$, $\;a \vee a' = 1$

> [!important] Teorema di Stone
> Ogni algebra di Boole **finita** è isomorfa a $(\mathcal{P}(S), \cap, \cup, {}^c, \emptyset, S)$.

### Anello Booleano

> [!note] Anello Booleano
> Un anello $(A, +, \cdot)$ è **booleano** se $a^2 = a$ per ogni $a \in A$.
>
> Proprietà:
> - $\mathrm{char}(A) = 2$ (cioè $a + a = 0$ per ogni $a$)
> - $A$ è **commutativo**
>
> Esempio: $(\mathcal{P}(S), \triangle, \cap)$.

> [!tip] Dimostrazione — Proprietà degli Anelli Booleani
> **$a + a = 0$:** Sviluppiamo $(a + b)^2 = a + b$ (idempotenza).
> D'altra parte $(a + b)^2 = a^2 + ab + ba + b^2 = a + ab + ba + b$.
> Dunque $a + b = a + ab + ba + b$, da cui $ab + ba = 0$.
> Ponendo $b = a$: $a^2 + a^2 = 0$, cioè $a + a = 0$. Pertanto $\mathrm{char}(A) = 2$ e $a = -a$.
>
> **Commutatività:** Da $ab + ba = 0$ e $ba = -ba$ (poiché $x = -x$ per ogni $x$), si ha $ab - ba = 0$, dunque $ab = ba$. $\square$

### Da Reticolo Booleano ad Anello Booleano

> [!note] Costruzione
> Dato un reticolo booleano $(L, \wedge, \vee, ', 0, 1)$, si definisce l'anello $(L, +, \cdot)$:
> - **Prodotto:** $a \cdot b = a \wedge b$
> - **Somma:** $a + b = (a \wedge b') \vee (b \wedge a')$ (differenza simmetrica)
> - $0_{\text{anello}} = 0_L$, $\;1_{\text{anello}} = 1_L$
>
> Relazione d'ordine recuperata: $a \leq b \;\Longleftrightarrow\; a \cdot b = a$.
