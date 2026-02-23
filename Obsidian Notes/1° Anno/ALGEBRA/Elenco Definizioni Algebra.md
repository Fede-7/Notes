---
banner: "[[Banner_n4.jpg]]"
---
## Indice
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

## *Lezione 1* — Logica, Insiemi, Funzioni

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

## *Lezione 2* — Quantificatori, Immagini, Iniettività, Partizioni

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

## *Lezione 3* — Suriettività, Funzione Caratteristica, Restrizione, Identità

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

## *Lezione 4* — Biettività, Composizione, Invertibilità, Strutture Algebriche

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

## *Lezione 5* — Matrici, Semigruppo, Monoide
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

## *Lezione 6* — Prodotto Matrici, Gruppi, Invertibili, Parte Stabile

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

## *Lezione 7* — Anelli, Caratteristica, Cancellabilità, Divisori dello Zero

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

## *Lezione 8* — Omomorfismo, Dominio, Campo, Spazio Vettoriale, Gruppo Simmetrico

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

>[!danger] Osservazione
>*Sono privi di divisori dello zero,  per i due teoremi di sopra:*
>- "Simmetrizzabile $\implies$ Cancellabile"
>MA
>- "$\exists$ Divisori dello zero $\iff \neg$ Cancellabile"
>QUINDI
>- Cancellabile $\implies \nexists$ Divisori dello zero  

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
> Sia $K$ un campo. Un **$K$-spazio vettoriale** è una struttura $(V, +, \cdot_{\text{ext}})$ dove:
>
> 1. $(V, +)$ è un **gruppo abeliano** (vettori, somma vettoriale, vettore nullo $0_V$)
> 2. $\cdot_{\text{ext}}: K \times V \to V$ è un'**operazione esterna** (prodotto per scalare)
> 3. Valgono $\forall \alpha, \beta \in K, \, \forall u, v \in V$:
>    - **i)** $\alpha \cdot_{\text{ext}} (\beta \cdot_{\text{ext}} v) = (\alpha \cdot_K \beta) \cdot_{\text{ext}} v$ (Associatività mista)
>    - **ii)** $(\alpha +_K \beta) \cdot_{\text{ext}} v = (\alpha \cdot_{\text{ext}} v) +_V (\beta \cdot_{\text{ext}} v)$ (Distributività scalari)
>    - **iii)** $\alpha \cdot_{\text{ext}} (u +_V v) = (\alpha \cdot_{\text{ext}} u) +_V (\alpha \cdot_{\text{ext}} v)$ (Distributività vettori)
>    - **iv)** $1_K \cdot_{\text{ext}} v = v$ (Elemento neutro)

### Gruppo Simmetrico

> [!note] Gruppo Simmetrico $S_n$
> Sia $S$ un insieme con $|S| = n$ (spesso $S = \{1, 2, \ldots, n\}$).
>
> **$\mathcal{B}(S)$** = insieme delle permutazioni (biiezioni) di $S$.
>
> $(\mathcal{B}(S), \circ)$ è un **gruppo**, detto **Gruppo Simmetrico**, denotato $S_n$.
> - $|S_n| = n!$
> - Non abeliano per $n \geq 3$

> [!note] Notazione Ciclica
> Un **ciclo** $(c_1c_2\cdots c_k)$: $\sigma(c_i) = c_{i+1}$, $\sigma(c_k) = c_1$, $\sigma(x) = x$ altrimenti.

> [!important] **Teorema di Scomposizione Canonica (Permutazioni)**
>
> - *Enunciato*
> Ogni permutazione $\sigma \in S_n$ diversa dall'identità si può scrivere come prodotto di cicli disgiunti. Tale scomposizione è **unica a meno dell'ordine** con cui i cicli compaiono nel prodotto.
>
> - *Formulazione Matematica*
> Sia $\sigma \in S_n$, allora esistono $r$ cicli $\gamma_1, \gamma_2, \ldots, \gamma_r$ tali che:
> $$\sigma = \gamma_1 \circ \gamma_2 \circ \cdots \circ \gamma_r$$
>
> sotto le seguenti condizioni:
>
> - **Disgiunzione:** $\text{supp}(\gamma_i) \cap \text{supp}(\gamma_j) = \varnothing$ per ogni $i \neq j$
> - **Commutatività:** Essendo disgiunti, i cicli commutano: $\gamma_i \circ \gamma_j = \gamma_j \circ \gamma_i$
> - **Unicità:** La scomposizione è determinata univocamente dall'azione di $\sigma$ sulle orbite di $\{1, \ldots, n\}$
>
> - *Esempio*
> $$\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\ 2 & 4 & 7 & 1 & 5 & 6 & 3 & 9 & 8 \end{pmatrix} = (124)(37)(89)$$

> [!note] Inversa di Cicli
> **Ciclo:** $(c_1c_2\cdots c_k)^{-1} = (c_1c_kc_{k-1}\cdots c_2)$ 
>
> **Esempio:** $(1743)^{-1} = (1347)$
>
> **Prodotto:** $(\sigma_1 \circ \sigma_2 \circ \cdots \circ \sigma_k)^{-1} = \sigma_k^{-1} \circ \cdots \circ \sigma_2^{-1} \circ \sigma_1^{-1}$
## *Lezione 9* — Tavole di Cayley, Nilpotenti, Divisibilità, MCD, Relazioni Binarie

### Tavole di Cayley

> [!note] Proprietà visibili dalle Tavole
> - **Commutatività** $\Longleftrightarrow$ tabella simmetrica rispetto alla diagonale
> - **Cancellabilità** $\Longleftrightarrow$ nessuna ripetizione nelle righe e colonne
> - **Elemento Neutro** $\Longleftrightarrow$ c'è una riga ed una colonna con elementi uguali agli indici
> - **Simmetrizzabili** $\Longleftrightarrow$ l'operazione $*$ restituisce l'elemento neutro

> [!important] Cancellabilità in Strutture Finite
> In un magma **finito** $(S, *)$, un elemento $a$ è **cancellabile** se e solo se la funzione $x \mapsto a * x$ è **iniettiva** (e quindi biettiva, essendo $S$ finito).

### Elemento Nilpotente

> [!note] Nilpotente
> $a \in A$ è **nilpotente** se $\exists\, n \geq 1:\; a^n = 0_A$.
> **Nilpotente non nullo $\Longrightarrow$ Divisore dello zero.**

### Divisibilità

> [!note] Divisibilità
> $$b \mid a \;\Longleftrightarrow\; \exists c:\; a = b \cdot c$$
> - $\mathrm{div}(a)$: insieme dei divisori di $a$. 
> - $\mathrm{mult}(b)$: insieme dei multipli di $b$.

### Elementi Associati

> [!note] Associati
> > Sia $x,y \in A$ un anello commutativo unitario.
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
### Aritmentica in $\mathbb{Z}$

> [!note]  Aritmetica in $\mathbb{Z}$
>
> $\mathbb{Z}$ è un **dominio d'integrità** speciale con proprietà aritmetiche fondamentali:
>
> ### Proprietà strutturali
> - **Dominio d'integrità:** commutativo, unitario, privo di divisori dello zero
> - **Privo di elementi nilpotenti:** l'unico elemento nilpotente è $0$ (poiché $0 \cdot 0 = 0$)
> - **Ordinamento totale:** $\mathbb{Z}$ è totalmente ordinato con $\leq$
> - **Ben ordinato:** ogni sottoinsieme non vuoto di interi positivi ha minimo
>
> ### Struttura aritmetica
> In $\mathbb{Z}$ definiamo:
> - **Divisibilità:** $a \mid b \Leftrightarrow \exists k \in \mathbb{Z} : b = a \cdot k$
> - **Elementi associati:** $a \sim b \Leftrightarrow a \mid b \text{ e } b \mid a \Leftrightarrow a = \pm b$
> - **Elementi invertibili:** $\mathcal{U}(\mathbb{Z}) = \{\pm 1\}$
> - **MCD e mcm:** definiti a meno di associazione


### Relazioni Binarie — Proprietà

> [!note] 9.12 — Relazione Binaria su $A$
> Una **relazione binaria** $R$ su $A$ è un sottoinsieme del prodotto cartesiano $A \times A$.
>
> Formalmente: $R = (A \times A, G)$ dove $G \subseteq A \times A$ è il **grafo**.
>
> Scriviamo: $aRb \Leftrightarrow (a, b) \in G$

> [!note] Relazione Banali
> - **Relazione Totale**:  
> $G = A \times A$
> $\forall a, b \in A: \, aRb$
> ---
> - **Relazione di Identità**:
> $G = \text{Diag}(A) = \{(a, a) \mid a \in A\}$
> $aRb \Leftrightarrow a = b$

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

## *Lezione 10* — Buon Ordinamento, Induzione, Divisione Euclidea, Relazione d'Equivalenza

### Insieme Ben Ordinato

> [!caution] Anticipazione: 
> ##### Insieme Parzialmente Ordinato (POSet: Partial Order Set)
> Un **insieme parzialmente ordinato**  è una coppia $(S, \leq)$ dove $\leq$ è una relazione che soddisfa $\forall a, b, c \in S$:
>
> 1. **Riflessività:** $a \leq a$
> 2. **Antisimmetria:** $(a \leq b \land b \leq a) \Rightarrow a = b$
> 3. **Transitività:** $(a \leq b \land b \leq c) \Rightarrow a \leq c$
> ##### Insieme totalmente ordinato
> Un ordine si dice **totale** (o lineare) se, oltre ai tre assiomi precedenti, soddisfa l'assioma di confrontabilità:
> $∀a,b∈S⟹a≤b∨b≤a$
> ##### Quindi:
> Ben Ordinato $\subset$ Totalmente Ordinato $\subset$ Parzialmente Ordinato (Poset)

> [!note] Ben Ordinato
> $(S, \leq)$ è **ben ordinato** se ogni sottoinsieme non vuoto ammette un **minimo**.
> Ben ordinato $\Longrightarrow$ totalmente ordinato.
> Esempio: $(\mathbb{N}, \leq)$.

### Principio di Induzione
 Si basa sul fatto che $(N, ≤)$ è ben ordinato
 
> [!note] Forma I (Standard)
> Se $P(\bar{n})$ è vera e $\forall n \geq \bar{n}:\; P(n) \Rightarrow P(n+1)$, allora $P(n)$ è vera $\forall n \geq \bar{n}$.

> [!note] Forma II (Forte)
> Se $P(\bar{n})$ è vera e $\forall n > \bar{n}:\; \bigl[\forall i\;(\bar{n} \leq i < n \Rightarrow P(i))\bigr] \Rightarrow P(n)$, allora $P(n)$ è vera $\forall n \geq \bar{n}$.

### Divisione Euclidea

> [!important] Teorema della Divisione Euclidea
> $\forall\, m, n \in \mathbb{Z},\; n \not= 0,\; \exists!\, q, r \in \mathbb{Z}:$
> $$m = n \cdot q + r, \qquad 0 \leq r < |n|$$


> [!tip] Dimostrazione — Divisione Euclidea
> **Esistenza** (per induzione forte su $m$):
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

> [!tip] Dimostrazione: Teorema di Bézout (Identità di Bézout)
> 
> Sia $S = \{as + bt \mid s, t \in \mathbb{Z}, \, as + bt > 0\}$.
>
> **1) $S \neq \varnothing$:**
> - Se $a \neq 0$, scegliendo $s = \pm 1$ si ha $|a| = a \cdot (\pm 1) + b \cdot 0 \in S$
> - Analogamente se $b \neq 0$
>
> **2) Esistenza del minimo:**
> Per il **principio del buon ordinamento**, $S$ ammette un minimo $d$. Per definizione di $S$, esistono $x, y \in \mathbb{Z}$ tali che:
> $$d = ax + by$$
>
> **3) $d \mid a$:**
> Dividiamo $a = dq + r$ con $0 \leq r < d$. Allora:
> $$r = a - dq = a - (ax + by)q = a(1 - xq) + b(-yq)$$
> 
> Poiché $1 - xq$ e $-yq$ sono interi, $r$ è una combinazione lineare di $a$ e $b$.
> 
> Se $r > 0$, allora $r \in S$ con $r < d$, contro la minimalità di $d$. Dunque $r = 0$, quindi $d \mid a$.
>
> **4) $d \mid b$:** Analogamente.
>
> **5) $d = \gcd(a, b)$:**
> Se $c \mid a$ e $c \mid b$, allora $c \mid (ax + by) = d$, dunque $d$ è il massimo comune divisore di $a$ e $b$. $\blacksquare$

### Relazione d'Equivalenza

> [!note] Equivalenza
> Una relazione binaria $R$ su $A$ è di **equivalenza** se è:
> 1. **Riflessiva**
> 2. **Simmetrica**
> 3. **Transitiva**

### Relazione d'Ordine
come accennato...
> [!note] Ordine (Parziale)
> Una relazione su $A$ è d'**ordine** se è :
> - riflessiva, 
> - **antisimmetrica**
> - transitiva.
> È **totale** se $\forall x, y:\; xRy \vee yRx$.

### Grafo

>[!note]  Definizione di garfo
>Una relazione su A è un **grafo** se è: 
>- Antiriflessivo
>- Simmetrico

---

## *Lezione 11* — Algoritmo di Euclide, Bézout, FTA, Classi di Equivalenza

### Algoritmo di Euclide

> [!note] Algoritmo di Euclide
> Calcola $\mathrm{MCD}(a, b)$ tramite divisioni successive: si divide ripetutamente il dividendo per il resto, finché il resto è $r = 0$. L'ultimo resto non nullo è il MCD.
> $$MCD(a,b) = MCD(b,r)$$

### Algoritmo Esteso di Euclide

> [!note] Algoritmo Esteso
> Risalendo le divisioni dell'Algoritmo di Euclide, si trovano i **coefficienti di Bézout** $x, y$ tali che $ax + by = \mathrm{MCD}(a, b)$.

### Lemma D'Euclide

> [!important] Lemma di Euclide
> Se $p$ è un numero primo e $p \mid ab$, allora $p \mid a$ oppure $p \mid b$.
> 
> **Dimostrazione (Idea):** Se $p \nmid a$, allora MCD$(p, a) = 1$. Per Bézout,
> $$\exists\, x, y \in \mathbb{Z} : px + ay = 1.$$
> Moltiplichiamo per $b$: $pxb + ayb = b$. Poiché $p \mid pxb$ e $p \mid ayb$ (dato che $p \mid ab$), allora $p$ divide la loro somma, cioè $p \mid b$.
### Teorema Fondamentale dell'Aritmetica

> [!important] FTA
> Ogni intero $n \geq 2$ si scrive in modo **unico** (a meno dell'ordine) come prodotto di numeri primi:
> $$n = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_k^{\alpha_k}$$
>- **Unicità della Fattorizzazione :**
Se abbiamo due scomposizioni in primi positivi:
$$a = p_1 \cdot p_2 \cdots p_m = q_1 \cdot q_2 \cdots q_n$$
allora: $(m = n)$ (stesso numero di fattori), e  $(p_i = q_i)\,\space \forall i$
>$\enspace$
> - **Ruolo del Lemma di Euclide :**
Il Lemma di Euclide è cruciale per dimostrare l'unicità della fattorizzazione: se un primo $p \mid (a\cdot b), \implies p\mid a \lor p\mid b$

> [!important] Dimostrazione Th. Fondamenta della aritmetica
> - Parte 1: Esistenza della fattorizzazione
>
> **Per induzione su $n$:**
>
> **Base:** $n = 2$ è primo. ✓
>
> **Ipotesi induttiva:** Per ogni $m < n$, la fattorizzazione esiste.
>
> **Tesi:** La fattorizzazione esiste per $n$.
>
> **Dimostrazione:**
> - Se $n$ è primo, banale.
> - Altrimenti, per il **Lemma di Euclide**, esiste un primo $p \mid n$ con $n = p \cdot m$ dove $m < n$.
> - Per ipotesi induttiva, $m$ ha una fattorizzazione.
> - Dunque $n = p \cdot m$ ha una fattorizzazione. $\checkmark$
>
> ---
>
> - Parte 2: Unicità della fattorizzazione
>
> Supponiamo $n$ abbia due rappresentazioni:
> $$n = p_1^{a_1} \cdots p_k^{a_k} = q_1^{b_1} \cdots q_r^{b_r}$$
>
> dove i $p_i$ e i $q_j$ sono primi distinti.
>
> **Caso 1:** Un primo $p_i$ compare nella prima rappresentazione ma non nella seconda.
>
> Allora $p_i \mid n = q_1^{b_1} \cdots q_r^{b_r}$.
>
> Per il **Lemma di Euclide**, $p_i$ divide uno dei $q_j$. Ma i $q_j$ sono primi, quindi $p_i = q_j$, contraddizione. $\times$
>
> **Caso 2:** Le rappresentazioni hanno gli stessi primi, ma esponenti diversi.
>
> Supponiamo $a_1 > b_1$ (senza perdita di generalità). Dividendo per $p_1^{b_1}$:
> $$p_1^{a_1 - b_1} \cdot p_2^{a_2} \cdots p_k^{a_k} = q_2^{b_2} \cdots q_r^{b_r}$$
>
> Allora $p_1 \mid q_2^{b_2} \cdots q_r^{b_r}$.
>
> Per il **Lemma di Euclide**, $p_1$ divide uno dei $q_j$ (con $j \geq 2$). Ma i $q_j$ sono primi distinti dai $p_i$, contraddizione. $\times$
>
> Quindi gli esponenti devono essere uguali: $a_i = b_i$ per ogni $i$. $\checkmark$

### Classi di Equivalenza

> [!note] Classe di Equivalenza
> $$[a]_R = \{x \in S \mid x \mathrel{R} a\}$$
> Proprietà:
> - Ogni classe è **non vuota** ($a \in [a]$)
> - Due classi sono **uguali o disgiunte**
> - L'unione di tutte le classi di equivalenza **distinte** restituisce l'insieme originale $S$.

### Insieme Quoziente

> [!note] Insieme Quoziente
> $$S / R = \{[a]_R \mid a \in S\}$$
> L'insieme di tutte le classi di equivalenza disgiunte.


---

## *Lezione 12* — Equivalenza ↔ Partizioni, Congruenza, Anello $\mathbb{Z}_m$

### Th. Fondamentale sulle relazioni di equivalenza
> [!important] Teorema Fondamentale sulle Relazioni di Equivalenza
>
> Sia $S \neq \varnothing$. Esiste una corrispondenza biunivoca tra:
> - L'insieme di tutte le **relazioni di equivalenza** su $S$
> - L'insieme di tutte le **partizioni** di $S$
>
> In particolare:
> - Se $R$ è relazione di equivalenza, allora $S/R = \{[a]_R \mid a \in S\}$ è una partizione
> - Se $\mathcal{F}$ è una partizione, allora $x R_{\mathcal{F}} y \Leftrightarrow \exists A \in \mathcal{F}: x, y \in A$ è una relazione di equivalenza
> - Queste costruzioni sono una l'inversa dell'altra

> [!important] Dimostrazione: Teorema Fondamentale sulle Relazioni di Equivalenza
>
> ### Parte i) Relazione $\Rightarrow$ Partizione
>
> Se $R$ è una relazione di equivalenza su $S$, allora $S/R = \{[a]_R \mid a \in S\}$ è una partizione di $S$.
>
> **Dimostrazione:** Le classi di equivalenza sono:
> - Non vuote
> - Disgiunte o coincidenti
> - Unione uguale a $S$
>
> Quindi $S/R$ è una partizione. ✓
>
> ---
>
> ### Parte ii) Partizione $\Rightarrow$ Relazione
>
> Se $\mathcal{F}$ è una partizione di $S$, definiamo:
> $$x R_{\mathcal{F}} y \Leftrightarrow \exists A \in \mathcal{F}: \, x \in A \land y \in A$$
>
> Allora $R_{\mathcal{F}}$ è una relazione di equivalenza.
>
> **Dimostrazione:**
>
> **Riflessiva:** $\forall x \in S$. Poiché $\mathcal{F}$ è partizione: $\bigcup_{A \in \mathcal{F}} A = S$.
> Quindi $x \in A$ per qualche $A \in \mathcal{F}$. Per definizione: $x R_{\mathcal{F}} x$. ✓
>
> **Simmetrica:** Se $x R_{\mathcal{F}} y$, allora $\exists A \in \mathcal{F}: x \in A \land y \in A$.
> Ma allora $y \in A \land x \in A$, quindi $y R_{\mathcal{F}} x$. ✓
>
> **Transitiva:** Se $x R_{\mathcal{F}} y$ e $y R_{\mathcal{F}} z$, allora:
> - $\exists A \in \mathcal{F}: x, y \in A$
> - $\exists B \in \mathcal{F}: y, z \in B$
>
> Poiché $y \in A \cap B$ e i pezzi di una partizione sono **disgiunti o coincidenti**, deve essere $A = B$.
>
> Quindi $x, z \in A$, cioè $x R_{\mathcal{F}} z$. ✓
>
> ---
>
> ### Parte iii) Corrispondenza Inversa
>
> Verifichiamo che $S/R_{\mathcal{F}} = \mathcal{F}$.
>
> Consideriamo una classe di equivalenza:
> $$[a]_{R_{\mathcal{F}}} = \{x \in S \mid x R_{\mathcal{F}} a\}$$
>
> Per definizione di $R_{\mathcal{F}}$:
> $$[a]_{R_{\mathcal{F}}} = \{x \in S \mid \exists A \in \mathcal{F}: x \in A \land a \in A\}$$
>
> Poiché $\mathcal{F}$ è una partizione, $\exists! A_a \in \mathcal{F}$ tale che $a \in A_a$.
>
> Quindi:
> $$[a]_{R_{\mathcal{F}}} = \{x \in S \mid x \in A_a\} = A_a$$
>
> Le classi di equivalenza di $R_{\mathcal{F}}$ sono esattamente gli insiemi della partizione originale $\mathcal{F}$. ✓
>
> ---
>
> **Conclusione:** Esiste una biiezione tra relazioni di equivalenza e partizioni su $S$. $\square$

### Relazione di Equivalenza Indotta da Funzione

> [!note] Relazione di Equivalenza indotta da una Funzione
>
> Siano $S, T$ insiemi non vuoti e $f : S \to T$ una funzione.
>
> La relazione $R_f$ su $S$ definita da:
> $$x R_f y \Leftrightarrow f(x) = f(y)$$
>
> è una **relazione di equivalenza** su $S$.
>
> Le classi di equivalenza sono le **fibre** di $f$: $[a]_{R_f} = f^{-1}(\{f(a)\})$

> [!tip] Dimostrazione — $R_f$ è di equivalenza
> - *Riflessiva:* $f(x) = f(x)$.
> - *Simmetrica:* $f(x) = f(y) \Rightarrow f(y) = f(x)$.
> - *Transitiva:* $f(x) = f(y)$ e $f(y) = f(z) \Rightarrow f(x) = f(z)$. $\square$

### Applicazione Quoziente (Fattorizzazione)

> [!note] Fattorizzazione
> Data $f: S \to T$ e la relazione $R_f$, l'**applicazione quoziente** è:
> $$\bar{f}: S/R_f \to T, \qquad \bar{f}([a]) = f(a)$$
> È **ben definita** e **iniettiva**. Vale $f = \bar{f} \circ \pi$ (dove $\pi$ è la proiezione canonica).

> [!tip] Dimostrazione — Fattorizzazione (forse non necessaria)
> **Ben definita:** Se $[a] = [b]$, allora $a \mathrel{R_f} b$, cioè $f(a) = f(b)$, dunque $\bar{f}([a]) = \bar{f}([b])$.
>
> **Iniettiva:** Se $\bar{f}([a]) = \bar{f}([b])$, allora $f(a) = f(b)$, dunque $a \mathrel{R_f} b$, cioè $[a] = [b]$. $\square$

### Congruenza (Compatibilità)

> [!note] Congruenza (Relazione di Equivalenza Compatibile)
>
> Sia $(S, \bot)$ una struttura con un'operazione binaria $\bot$. Una relazione di equivalenza $R$ su $S$ si dice **congruenza** (o **compatibile**) rispetto a $\bot$ se:
>
> $$\forall a, b, c, d \in S: \quad (a R c \land b R d) \Rightarrow (a \bot b) R (c \bot d)$$
>
> - Interpretazione
> Se $a \sim c$ e $b \sim d$, allora $a \bot b \sim c \bot d$. L'equivalenza **rispetta l'operazione**.
>
> ---
>
>  **Operazione Quoziente**
>
> Se $R$ è una congruenza su $(S, \bot)$, allora è possibile definire un'operazione $\bot_R$ sull'insieme quoziente $S/R$ in modo **ben definito**:
>
> $$[a]_R \bot_R [b]_R = [a \bot b]_R$$
>
> La struttura quoziente $(S/R, \bot_R)$ eredita le proprietà algebriche di $(S, \bot)$.

> [!attention] Operazione "Ben definita"
>
> Se scegliamo altri rappresentanti $[a]_R = [c]_R$ (cioè $aRc$) e $[b]_R = [d]_R$ (cioè $bRd$), il risultato non deve cambiare:
> $$[a \bot b]_R \text{ deve essere uguale a } [c \bot d]_R$$
>
> Questo è **garantito dalla definizione di congruenza**:
> $$aRc \land bRd \Rightarrow (a \bot b)R(c \bot d)$$
>
> che significa proprio:
> $$[a \bot b]_R = [c \bot d]_R$$
>
> Quindi l'operazione $\bot_R$ su $S/R$ è **ben definita**.
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
> >[!tip] Dimostrazione — Compatibilità
> >Sia $a - c = mh$ e $b - d = mk$.
>>
>> **Somma:** $(a + b) - (c + d) = (a - c) + (b - d) = mh + mk = m(h + k)$, dunque $m \mid (a + b) - (c + d)$.
>>
>> **Prodotto:** $ab = (c + mh)(d + mk) = cd + m(ck + hd + mhk)$, dunque $ab - cd = m(ck + hd + mhk)$ e $m \mid (ab - cd)$. $\square$

> [!note] Anello $\mathbb{Z}_m$
> L'insieme quoziente $\mathbb{Z}_m = \{[0]_m, [1]_m, \ldots, [m-1]_m\}$ con:
> $$[a] + [b] = [a + b], \qquad [a] \cdot [b] = [a \cdot b]$$
> è un **anello commutativo unitario**.

---

## *Lezione 13* — Classi di Resto, $\mathbb{Z}_m$ Campo, Invertibili, Nilpotenti, Equazioni Congruenziali

### $\mathbb{Z}_m$ è un Campo

> [!important] Teorema
> $(\mathbb{Z}_m, +, \cdot)$ è un **campo** se e solo se $m$ è un numero **primo**.

> [!tip] Dimostrazione — $\mathbb{Z}_m$ campo: $\Longleftrightarrow$ $m$ primo
> $\mathbb{Z}_m$ è un campo 
> $\iff$ ogni $[a] \neq [0]$ è invertibile
> $\iff$ $\forall a \in \{1, \ldots, m-1\}:\; \mathrm{MCD}(a, m) = 1$
> $\iff$ $m$ non ha divisori propri 
> $\iff$ $m$ è primo. $\square$

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
> # **Invertibile** 
>  - "$\Longleftarrow$ $d = 1$":
>  Per Bézout, $\exists\, h, k \in \mathbb{Z}$ con $ah + mk = 1$.
> In $\mathbb{Z}_m$: $\bar{a} \cdot \bar{h} = \overline{ah} = \overline{1 - mk} = \bar{1}$.
>
> - "$\Longrightarrow$ $d = 1$":
>  Se $\bar{a} \cdot \bar{b} = \bar{1}$, allora $ab - mk = 1$ per qualche $k$.
> Questa è un'identità di Bézout, dunque $\mathrm{MCD}(a, m) = 1$.
>
> # **Div. zero** 
> - "$\Longleftarrow$ $d > 1$": 
> Poniamo $a = da_1$ e $m = dm_1$.
> Allora $\bar{a} \cdot \overline{m_1} = \overline{a_1 m} = \bar{0}$ con $\overline{m_1} \neq \bar{0}$ (poiché $m_1 < m$).
>
> - "$\Longrightarrow$ $d > 1$":
> Se $\bar{a} \cdot \bar{b} = \bar{0}$ con $\bar{b} \neq \bar{0}$, allora $m \mid ab$.
> Se fosse $d = 1$, per il Lemma di Euclide $m \mid b$, cioè $\bar{b} = \bar{0}$: contraddizione. $\square$

### Elementi Nilpotenti in $\mathbb{Z}_m$

> [!note] Nilpotenti in $\mathbb{Z}_m$
> Sia $m = p_1^{\alpha_1} \cdots p_t^{\alpha_t}$. Allora $[a]_m$ è nilpotente $\iff$ ogni divisore primo di $m$ divide anche $a$.

### Equazioni Congruenziali

> [!important] Teorema di Risolubilità
> L'equazione $ax \equiv b \pmod{m}$ ha soluzione $\;\Longleftrightarrow\;$ $d \mid b$, dove $d = \mathrm{MCD}(a, m)$.
> Se ha soluzione, ci sono esattamente **$d$ soluzioni distinte** modulo $m$.
> Se $d = 1$, la soluzione unica è $x \equiv a^{-1} b \pmod{m}$.

---

## *Lezione 14* — Idempotenti, Criteri di Divisibilità

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

## *Lezione 15* — Dominio, Anello Prodotto, Caratteristica del Prodotto

### Corollario: $\mathbb{Z}_n$ Dominio d'Integrità
$\mathbb{Z}_n$ equivale a $\mathbb{Z}_m$ ma con $n \not= m$
> [!note] Dominio
> $\mathbb{Z}_n$ è un **dominio d'integrità** $\;\Longleftrightarrow\;$ $n$ è primo $\;\Longleftrightarrow\;$ $\mathbb{Z}_n$ è un campo.

### Anello Prodotto

> [!note] **Definizione**
> L'anello prodotto $R \times S = \{(r,s) \mid r \in R, s \in S\}$ con operazioni componente per componente:
> - $(r_1,s_1) + (r_2,s_2) = (r_1+r_2, s_1+s_2)$
> - $(r_1,s_1) \cdot (r_2,s_2) = (r_1 \cdot r_2, s_1 \cdot s_2)$
> - Zero: $\mathbf{0} = (0_R, 0_S)$
> - Unità: $\mathbf{1} = (1_R, 1_S)$ (se $R,S$ unitari)

> [!note] **Proprietà Fondamentali**
> 
> | Proprietà | Risultato |
> |---|---|
> | **Commutatività** | $R \times S$ comm. ⟺ $R$ e $S$ comm. |
> | **Invertibili** | $(r,s) \in U(R \times S)$ ⟺ $r \in U(R)$ e $s \in U(S)$ |
> | **Cardinalità invertibili** | $\|U(\mathbb{Z}_m \times \mathbb{Z}_n)\| = \varphi(m) \cdot \varphi(n)$ |
> | **Divisori dello zero** | **Sempre presenti** (anche se $R,S$ domini): $(1_R,0_S) \cdot (0_R,1_S) = \mathbf{0}$ |
> | **Caratteristica** | $\mathrm{char}(R \times S) = \mathrm{mcm}(\mathrm{char}(R), \mathrm{char}(S))$ |
> | **Campo** | Se $F,K$ campi ⟹ $F \times K$ **NON è campo** (ha divisori dello zero) |

> [!note] **Teorema Cinese dei Resti (TCR)**
> $$\mathbb{Z}_{mn} \cong \mathbb{Z}_m \times \mathbb{Z}_n \quad \Longleftrightarrow \quad \mathrm{MCD}(m,n) = 1$$
> 
> **Isomorfismo:** $\phi([a]_{mn}) = ([a]_m, [a]_n)$
> 
> **Utilità:** Spezzare calcoli modulo $mn$ (grande) in calcoli modulo $m$ e $n$ (piccoli).
> 
> **Esempio:** $\mathbb{Z}_{15} \cong \mathbb{Z}_3 \times \mathbb{Z}_5$ (poiché $\gcd(3,5)=1$)

> [!note] **Riassunto Critico**
> - ✓ Operazioni componente per componente funzionano perfettamente
> - ✗ Divisori dello zero sempre presenti (perdita proprietà integralità)
> - ✗ Non è mai un campo anche se fattori sono campi
> - ✓ TCR consente di fattorizzare calcoli complessi quando fattori sono coprimi
> - ✓ Invertibili sono il prodotto cartesiano di invertibili

> [!note] Caratteristica dell'Anello Prodotto
> $$\mathrm{char}(\mathbb{Z}_m \times \mathbb{Z}_n) = \mathrm{mcm}(\mathrm{char}(\mathbb{Z}_m),\, \mathrm{char}(\mathbb{Z}_n)) = \mathrm{mcm}(m, n)$$
---

## *Lezione 16* — Equazioni Diofantee, Totiente di Eulero, Fermat-Eulero, Calcolo Combinatorio

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
>> [!important] Piccolo Teorema di Fermat
>> Se $p$ è primo e $p \nmid a$:
>> $$a^{p-1} \equiv 1 \pmod{p}$$
### Coefficiente Binomiale
Rappresenta il numero di modi in cui si possono scegliere elementi da un insieme di oggetti, senza considerare l'ordine e senza ripetizioni.
> [!note] **Fattoriale e Coefficiente Binomiale**
> 
> >[!info] **Fattoriale:** $n! = n \cdot (n-1) \cdot \ldots \cdot 2 \cdot 1$ per $n \geq 1$; $0! = 1$
> 
> **Coefficiente Binomiale:** $\binom{n}{k} = \frac{n!}{k!(n-k)!} = \frac{n(n-1)\cdots(n-k+1)}{k!}$ per $0 \leq k \leq n$
> 
> **Proprietà:**
> - $\binom{n}{0} = 1$, $\binom{n}{n} = 1$
> - $\binom{n}{1} = n$, $\binom{n}{n-1} = n$
> - $\binom{n}{k} = \binom{n}{n-k}$ (Simmetria)
> - $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ (Pascal)
> - $\sum_{k=0}^{n} \binom{n}{k} = 2^n$
> 
> **Esempi:** $\binom{5}{2} = 10$, $\binom{6}{3} = 20$, $\binom{4}{2} = 6$

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
>> [!tip] Dimostrazione — Conteggio applicazioni iniettive (per induzione su $n$)
>> *Base:* $n = 1$: $f$ sceglie l'immagine di $a_1$ tra $m$ elementi: $m = \frac{m!}{(m-1)!}$.
>>
>> *Passo:* Per l'elemento $a_{n+1}$, l'immagine può essere uno qualsiasi degli $m$ elementi di $T$, ma per iniettività deve essere diverso dalle immagini di $a_1, \ldots, a_n$.
>> Scelta l'immagine $b_i$ di $a_{n+1}$ ($m$ scelte), le restanti $n$ variabili definiscono un'applicazione iniettiva da $S$ a $T \setminus \{b_i\}$ ($m-1$ elementi). Per ipotesi induttiva, queste sono $\frac{(m-1)!}{(m-1-n)!}$.
>> Totale: $m \cdot \frac{(m-1)!}{(m-1-n)!} = \frac{m!}{(m-n-1)!} = \frac{m!}{(m-(n+1))!}$. $\square$

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
> $$= \sum_{k=0}^{n+1} \binom{n+1}{k} a^{n+1-k} b^k \quad \square$$


---



## *Lezione 17* — Relazioni d'Ordine, Hasse, Estremi

### Insieme Parzialmente Ordinato (POSet)

> [!note] Insieme Parzialmente Ordinato
> Un **insieme parzialmente ordinato** (POSet) è una coppia $(S, \leq)$ dove $\leq$ è una relazione d'ordine su $S$.
> Se l'ordine è totale, si parla di **insieme totalmente ordinato**.

### Ordine Largo

> [!note] Relazione d'Ordine (Largo, Parziale)
> Una relazione $\leq$ su $S$ è d'**ordine** se è:
> 1. **Riflessiva:** $\forall x \in S,\; x \leq x$
> 2. **Antisimmetrica:** $\forall x, y \in S,\; (x \leq y \wedge y \leq x) \Rightarrow x = y$
> 3. **Transitiva:** $\forall x, y, z \in S,\; (x \leq y \wedge y \leq z) \Rightarrow x \leq z$

### Ordine Stretto

> [!note] Ordine Stretto
> Una relazione $<$ su $S$ è d'**ordine stretto** se è:
> 1. **Antiriflessiva:** $\forall x \in S,\; x \not< x$
> 2. **Transitiva:** $\forall x, y, z \in S,\; (x < y \wedge y < z) \Rightarrow x < z$
>
> **Conseguenza:** Implica automaticamente l'**asimmetria**: se $x < y$, allora $y \not< x$ (altrimenti per transitività $x < x$, contraddendo l'antiriflessività).

> [!tip] Dimostrazione — Asimmetria derivata da ordine stretto
> Supponiamo $x < y$ e $y < x$. Per transitività, $x < x$, contraddicendo l'antiriflessività. Dunque non può valere contemporaneamente $x < y$ e $y < x$. $\square$

### Corrispondenza Largo ↔ Stretto

> [!note] Relazione tra Ordine Largo e Stretto
> Esiste una corrispondenza biunivoca tra ordine largo e stretto sullo stesso insieme:
> $$x < y \;\Longleftrightarrow\; (x \leq y \;\wedge\; x \neq y)$$
> $$x \leq y \;\Longleftrightarrow\; (x < y \;\vee\; x = y)$$
### Ordine Totale

> [!note] Ordine Totale (o Lineare)
> Un ordine $\leq$ su $S$ è **totale** se ogni coppia di elementi è **confrontabile**:
> $$\forall x, y \in S:\; x \leq y \;\vee\; y \leq x$$
> Se un ordine non è totale, è detto **parziale**.
>
> **Esempi di ordini totali:** $(\mathbb{N}, \leq)$, $(\mathbb{Z}, \leq)$, $(\mathbb{R}, \leq)$.
>
> **Esempio di ordine parziale:** $(\mathcal{P}(S), \subseteq)$ con $|S| \geq 2$.

### Elemento Minimo e Massimo

> [!note] Minimo e Massimo
> Sia $(S, \leq)$ un insieme ordinato:
> - $a$ è **minimo** se $a \leq x$ per ogni $x \in S$. Se esiste, è **unico**.
> - $a$ è **massimo** se $x \leq a$ per ogni $x \in S$. Se esiste, è **unico**.

> [!tip] Dimostrazione — Unicità del Minimo
> Se $m_1, m_2$ sono entrambi minimi, allora:
> - $m_1$ è minimo: $m_1 \leq m_2$
> - $m_2$ è minimo: $m_2 \leq m_1$
> 
> Per antisimmetria, $m_1 = m_2$. $\square$

### Elemento Minimale e Massimale

> [!note] Minimale e Massimale
> Sia $(S, \leq)$ un insieme ordinato:
> - $a$ è **minimale** se non esiste $x \in S$ con $x < a$. Equivalentemente: $\forall x \in S,\; (x \leq a \Rightarrow x = a)$.
> - $a$ è **massimale** se non esiste $x \in S$ con $a < x$. Equivalentemente: $\forall x \in S,\; (a \leq x \Rightarrow x = a)$.

> [!note] Relazione tra Minimo e Minimale
> - Minimo $\Rightarrow$ unico elemento minimale
> - Un minimale unico **non è necessariamente** il minimo
> - In un ordine **totale**, minimale $\Longleftrightarrow$ minimo

> [!important] Teorema — Poset Finiti
> Ogni insieme **finito non vuoto** parzialmente ordinato possiede almeno un elemento **minimale** e almeno un elemento **massimale**.
>
> **Controesempio per insiemi infiniti:** $(\mathbb{Z}, \leq)$ non ha né minimali né massimali.

### Copertura (Successore Immediato)

> [!note] Copertura
> Sia $(S, \leq)$ un poset. L'elemento $b$ **copre** $a$ se:
> $$a < b \;\wedge\; \nexists\, c \in S:\; a < c < b$$
> Cioè $b$ è "immediatamente sopra" $a$ nell'ordine (è il successore immediato).

### Diagramma di Hasse

> [!note] Diagramma di Hasse
> Rappresentazione grafica di un poset finito $(S, \leq)$:
> - Vertici: elementi di $S$
> - Archi: solo le relazioni di **copertura**
> - Disposizione: elementi maggiori più in alto
> - Non si disegnano loop, archi transitivi, né frecce (è un grafo non orientato)

### Insieme Ben Ordinato

> [!note] Ben Ordinato
> $(S, \leq)$ è **ben ordinato** se ogni sottoinsieme non vuoto $X \subseteq S$ ammette un **minimo**.
> - Ben ordinato $\Rightarrow$ totalmente ordinato
> - **Esempio:** $(\mathbb{N}, \leq)$
> - **Controesempi:** $(\mathbb{Z}, \leq)$, $(\mathbb{R}_{\geq 0}, \leq)$ (es. $(0, 1)$ non ha minimo)

### Minoranti e Maggioranti

> [!note] Minorante e Maggiorante
> Sia $(S, \leq)$ un poset e $X \subseteq S$:
> - $a \in S$ è un **minorante** di $X$ se $a \leq x$ per ogni $x \in X$
> - $a \in S$ è un **maggiorante** di $X$ se $x \leq a$ per ogni $x \in X$
>
> **Osservazione:** Se un minorante $a$ di $X$ appartiene anche a $X$, allora $a = \min(X)$.

### Infimo e Supremo

> [!note] Infimo
> $$\inf(X) = \max(\text{minoranti di } X)$$
> Il **più grande** tra i minoranti di $X$ (se esiste).

> [!note] Supremo
> $$\sup(X) = \min(\text{maggioranti di } X)$$
> Il **più piccolo** tra i maggioranti di $X$ (se esiste).

> [!note] Relazione con Minimo e Massimo
> - Se $\min(X)$ esiste, allora $\inf(X) = \min(X)$
> - Se $\max(X)$ esiste, allora $\sup(X) = \max(X)$

> [!note] Esempio Fondamentale: $(\mathbb{N}^*, \mid)$
> Per $X = \{60, 54\}$:
> - **Minoranti** = divisori comuni = $\{1, 2, 3, 6\}$
> - **Infimo** = massimo dei minoranti = $6 = \mathrm{MCD}(60, 54)$
> - **Maggioranti** = multipli comuni
> - **Supremo** = minimo dei maggioranti = $540 = \mathrm{mcm}(60, 54)$

---

## *Lezione 19* — Divisibilità come Ordine, Ordine Indotto

### Divisibilità come Relazione d'Ordine

> [!note] Divisibilità su $\mathbb{N}^*$
> La relazione di divisibilità "$\mid$" su $\mathbb{N}^*$ è una **relazione d'ordine parziale**:
> 1. **Riflessiva:** $a \mid a$ per ogni $a \in \mathbb{N}^*$
> 2. **Antisimmetrica:** Se $a \mid b$ e $b \mid a$ con $a, b > 0$, allora $a = b$
> 3. **Transitiva:** Se $a \mid b$ e $b \mid c$, allora $a \mid c$
>
> **Non è totale:** Controesempio: $2 \nmid 3$ e $3 \nmid 2$.
>
> **Elementi estremi:**
> - Minimo: $\min(\mathbb{N}^*, \mid) = 1$
> - Massimo: non esiste

> [!note] Divisibilità su $\mathbb{Z}$ — Non è un Ordine
> La relazione "$\mid$" su $\mathbb{Z}$ **non** è una relazione d'ordine perché **non è antisimmetrica**.
> 
> **Controesempio:** $2 \mid (-2)$ e $(-2) \mid 2$, ma $2 \neq -2$.

### Ordine Indotto da una Funzione

> [!note] Ordine Indotto
> Sia $f: S \to T$ una funzione e $(T, \leq_T)$ un insieme ordinato. Su $S$ definiamo la relazione:
> $$a \leq_f b \;\Longleftrightarrow\; (a = b) \;\vee\; (f(a) <_T f(b))$$
> Questa è una **relazione d'ordine** su $S$.

> [!tip] Dimostrazione — $\leq_f$ è un ordine
> **Riflessiva:** $a \leq_f a$ poiché $a = a$.
>
> **Antisimmetrica:** Se $a \leq_f b$ e $b \leq_f a$:
> - Se $a \neq b$: allora $f(a) <_T f(b)$ (da $a \leq_f b$) e $f(b) <_T f(a)$ (da $b \leq_f a$), il che è assurdo per l'asimmetria di $<_T$.
> - Quindi deve valere $a = b$.
>
> **Transitiva:** Se $a \leq_f b$ e $b \leq_f c$:
> - Se $a = b$: allora $a \leq_f c$.
> - Se $b = c$: allora $a \leq_f c$.
> - Se $a \neq b$ e $b \neq c$: allora $f(a) <_T f(b) <_T f(c)$, da cui $f(a) <_T f(c)$ e $a \leq_f c$.
> $\square$

---

## *Lezione 20* — Reticoli

### Reticolo (Definizione tramite Ordine)

> [!note] Reticolo
> Un poset $(L, \leq)$ è un **reticolo** se per ogni coppia $a, b \in L$ esistono:
> - $\inf\{a, b\} = a \wedge b$ (**meet**, infimo di due elementi)
> - $\sup\{a, b\} = a \vee b$ (**join**, supremo di due elementi)

### Reticolo (Definizione Algebrica)

> [!note] Reticolo (struttura algebrica)
> Una struttura $(L, \wedge, \vee)$ è un **reticolo** se $\wedge$ e $\vee$ sono operazioni binarie che soddisfano:
> 1. **Associatività:** 
>    - $(a \wedge b) \wedge c = a \wedge (b \wedge c)$
>    - $(a \vee b) \vee c = a \vee (b \vee c)$
> 2. **Commutatività:** 
>    - $a \wedge b = b \wedge a$
>    - $a \vee b = b \vee a$
> 3. **Assorbimento:** 
>    - $a \wedge (a \vee b) = a$
>    - $a \vee (a \wedge b) = a$

### Idempotenza (Conseguenza)

> [!note] Idempotenza
> Dalle leggi di assorbimento derivano le **proprietà di idempotenza**:
> $$a \wedge a = a \qquad \qquad a \vee a = a$$
> [!tip] Dimostrazione — Idempotenza
> Applicando assorbimento con $b = a$:
> $$a \wedge (a \vee a) = a$$
> Sviluppiamo il lato sinistro usando idempotenza di $\vee$ (che assumiamo): $a \wedge a = a$. $\square$

### Equivalenza tra le Due Definizioni

> [!important] Teorema — Equivalenza Ordine ↔ Algebrica
> Le due definizioni di reticolo sono **equivalenti**. La relazione d'ordine si recupera da:
> $$a \leq b \;\Longleftrightarrow\; a \wedge b = a \;\Longleftrightarrow\; a \vee b = b$$
> [!tip] Dimostrazione — Algebrico ⟹ Ordine
> Data $(L, \wedge, \vee)$ con le proprietà algebriche, definiamo $a \leq b \iff a \wedge b = a$.
>
> **Riflessiva:** $a \wedge a = a$ (per idempotenza).
>
> **Antisimmetrica:** Se $a \wedge b = a$ e $b \wedge a = b$, per commutatività di $\wedge$ abbiamo $a = b$.
>
> **Transitiva:** Se $a \wedge b = a$ (cioè $a \leq b$) e $b \wedge c = b$ (cioè $b \leq c$), allora:
> $$a \wedge c = (a \wedge b) \wedge c = a \wedge (b \wedge c) = a \wedge b = a$$
> Dunque $a \leq c$.
>
> **Infimo:** Mostriamo che $\inf\{a, b\} = a \wedge b$.
> - Da $(a \wedge b) \wedge a = a \wedge b$ e $(a \wedge b) \wedge b = a \wedge b$, derivano $a \wedge b \leq a$ e $a \wedge b \leq b$.
> - Se $c \leq a$ e $c \leq b$, allora $c \wedge a = c$ e $c \wedge b = c$. 
>   Per assorbimento: $c \wedge (a \wedge b) = (c \wedge a) \wedge b = c \wedge b = c$, dunque $c \leq a \wedge b$.
>
> Pertanto $a \wedge b$ è il massimo dei minoranti di $\{a, b\}$. $\square$

### Esempio Fondamentale

> [!note] L'Insieme delle Parti è un Reticolo
> La struttura $(\mathcal{P}(S), \subseteq)$ è un **reticolo** con:
> - $A \wedge B = A \cap B$ (infimo = intersezione)
> - $A \vee B = A \cup B$ (supremo = unione)
>
> Le operazioni $\cap$ e $\cup$ soddisfano tutte le proprietà algebriche dei reticoli.

### Catena

> [!note] Catena
> Un sottoinsieme $C \subseteq S$ di un insieme ordinato $(S, \leq)$ è una **catena** se è **totalmente ordinato**:
> $$\forall x, y \in C:\; x \leq y \;\vee\; y \leq x$$
> [!note] Catena Massimale
> Una catena $C$ in $(S, \leq)$ è **massimale** se **non può essere estesa**: non esiste alcun elemento $s \in S \setminus C$ tale che $C \cup \{s\}$ sia ancora una catena.

### Poset che Non è un Reticolo

> [!note] Esempio — Poset Privo di Infimo o Supremo
> Consideriamo il poset $P = \{0, a, b, c, d, 1\}$ con ordine:
> $$0 < a, b \quad \text{e} \quad a, b < c, d \quad \text{e} \quad c, d < 1$$
> dove $c$ e $d$ **non sono confrontabili**.
>
> - Per la coppia $\{a, b\}$: i **maggioranti** sono $\{c, d, 1\}$. Poiché $c$ e $d$ non sono confrontabili, $\sup\{a, b\}$ **non esiste**.
> - Poiché esiste una coppia senza supremo, $P$ **non è un reticolo**.

---

## *Lezione 21* — Reticoli Limitati, Sottoreticoli, Isomorfismi, Complementati, Prodotto

### Reticolo Limitato

> [!note] Reticolo Limitato
> Un reticolo $(L, \leq)$ è **limitato** se possiede:
> - Un **elemento minimo** $0_L$: $0_L \leq a$ per ogni $a \in L$
> - Un **elemento massimo** $1_L$: $a \leq 1_L$ per ogni $a \in L$
>
> Equivalentemente (in notazione algebrica): $a \vee 0_L = a$ e $a \wedge 1_L = a$ per ogni $a$.

> [!important] Teorema — Reticoli Finiti Sono Limitati
> Ogni reticolo **finito** è **limitato**: possiede sempre un elemento minimo e un elemento massimo.

> [!important] Corollario — Insieme Totalmente Ordinato è un Reticolo
> Se $(S, \leq)$ è un insieme **totalmente ordinato**, allora è un **reticolo**. Per ogni $a, b \in S$:
> $$a \wedge b = \min\{a, b\} \qquad \quad a \vee b = \max\{a, b\}$$
### Esempi di Reticoli Limitati

> [!note] Esempi Comuni
> - $(\mathcal{P}(S), \subseteq)$: elemento minimo $0_L = \emptyset$, massimo $1_L = S$
> - $(\mathbb{D}_n, \mid)$ (divisori di $n$): elemento minimo $0_L = 1$, massimo $1_L = n$
> - $(\mathbb{N}^*, \mid)$: limitato **inferiormente** (minimo = 1), ma **non** limitato superiormente. Non è un reticolo limitato.

### Sottoreticolo

> [!note] Sottoreticolo
> Un sottoinsieme non vuoto $A \subseteq L$ di un reticolo $(L, \wedge, \vee)$ è un **sottoreticolo** se è **chiuso** per $\wedge$ e $\vee$:
> $$\forall x, y \in A:\; x \wedge y \in A \;\wedge\; x \vee y \in A$$
> In tal caso, $(A, \wedge|_A, \vee|_A)$ è esso stesso un reticolo.

> [!note] Esempi e Non-Esempi
> - Ogni singolo elemento $\{a\}$ è un **sottoreticolo banale**.
> - $\{a, b\}$ è un sottoreticolo $\iff$ $a$ e $b$ sono **confrontabili** (uno è $\leq$ all'altro).
> - In $(\mathbb{D}_{36}, \mid)$: il sottoinsieme $L = \{1, 2, 3, 6, 36\}$ **è** un sottoreticolo.
> - In $(\mathbb{D}_{36}, \mid)$: il sottoinsieme $M = \{1, 2, 3, 36\}$ **non** è un sottoreticolo perché $\mathrm{mcm}(2, 3) = 6 \notin M$ (non chiuso per $\vee$).

### Isomorfismo di Reticoli

> [!note] Isomorfismo tra Poset e Reticoli
> Una funzione biettiva $f: L \to M$ è un **isomorfismo** se **preserva l'ordine**:
> $$a \leq_L b \;\Longleftrightarrow\; f(a) \leq_M f(b) \quad \forall a, b \in L$$
>
> Equivalentemente (per reticoli): $f$ preserva $\wedge$ e $\vee$:
> $$f(a \wedge b) = f(a) \wedge f(b) \qquad \quad f(a \vee b) = f(a) \vee f(b)$$
### Elemento Complementato

> [!note] Complemento in un Reticolo Limitato
> In un reticolo **limitato** $(L, \leq, 0_L, 1_L)$, un elemento $a \in L$ ha un **complemento** $\bar{a}$ se:
> $$a \wedge \bar{a} = 0_L \qquad \text{e} \qquad a \vee \bar{a} = 1_L$$
> [!note] Osservazione
> - Ogni elemento ha **al massimo** un complemento (l'inverso è unico).
> - Gli elementi $0_L$ e $1_L$ sono sempre complementari tra loro.

### Reticolo Complementato

> [!note] Reticolo Complementato
> Un reticolo **limitato** è **complementato** se **ogni** elemento possiede almeno un complemento.

> [!note] Esempio: $M_3$ (Diamante) è Complementato
> Il reticolo $M_3 = \{0, a, b, c, 1\}$ con $a, b, c$ mutuamente non confrontabili e $0 < a, b, c < 1$:
> - $a$ ha come complementi sia $b$ che $c$ (ad es., $a \wedge b = 0$ e $a \vee b = 1$)
> - È un reticolo complementato (ma non distributivo).

### Reticolo NON Complementato

> [!note] Esempio: Catena $0 < a < 1$ Non è Complementata
> La catena a 3 elementi $L = \{0, a, 1\}$ con $0 < a < 1$:
> 
> Se $\bar{a}$ è il complemento di $a$, deve soddisfare $a \wedge \bar{a} = 0$ e $a \vee \bar{a} = 1$.
>
> - Se $\bar{a} = 0$: $a \wedge 0 = 0$ ✓, ma $a \vee 0 = a \neq 1$ ✗
> - Se $\bar{a} = a$: $a \wedge a = a \neq 0$ ✗
> - Se $\bar{a} = 1$: $a \wedge 1 = a \neq 0$ ✗
>
> Nessun elemento funziona: $a$ **non ha complemento**, quindi la catena **non è complementata**.

### Reticolo Prodotto

> [!note] Reticolo Prodotto
> Dati due reticoli $(L_1, \leq_1)$ e $(L_2, \leq_2)$, il **prodotto cartesiano** $L_1 \times L_2$ è un reticolo con ordine e operazioni **componente per componente**:
>
> **Ordine:** $(a, b) \leq (c, d) \;\Longleftrightarrow\; a \leq_1 c \;\wedge\; b \leq_2 d$
>
> **Infimo:** $(a, b) \wedge (c, d) = (a \wedge_1 c,\; b \wedge_2 d)$
>
> **Supremo:** $(a, b) \vee (c, d) = (a \vee_1 c,\; b \vee_2 d)$
>
> Se $L_1$ e $L_2$ sono limitati, allora $L_1 \times L_2$ è limitato con $(0_1, 0_2)$ e $(1_1, 1_2)$.

### Reticolo dei Divisori

> [!note] Reticolo $(\mathbb{D}_n, \mid)$
> L'insieme dei divisori positivi di $n$, ordinato per divisibilità, forma un **reticolo limitato**:
> - **Infimo:** $a \wedge b = \mathrm{MCD}(a, b)$
> - **Supremo:** $a \vee b = \mathrm{mcm}(a, b)$
> - **Minimo:** $0_L = 1$
> - **Massimo:** $1_L = n$

---

## *Lezione 22* — Dualità, Reticoli Distributivi e Booleani, Algebre di Boole, Anelli Booleani

### Principio di Dualità per Reticoli

> [!important] Principio di Dualità
> Se un enunciato vale per **tutti** i reticoli, allora vale anche il suo **duale**, ottenuto scambiando simultaneamente:
> $$\leq \;\longleftrightarrow\; \geq \qquad \wedge \;\longleftrightarrow\; \vee \qquad 0_L \;\longleftrightarrow\; 1_L$$
>
> **Applicazione:** Ogni teorema su reticoli è valido insieme al suo duale, garantendo simmetria nelle proprietà.

### Reticolo Distributivo

> [!note] Reticolo Distributivo
> Un reticolo è **distributivo** se soddisfa la **distributività** del meet sul join:
> $$a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$$
>
> Per dualità, la distributività del join sul meet è automaticamente equivalente:
> $$a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$$
>
> (Le due leggi sono equivalenti per dualità.)

### Reticoli Non Distributivi: $M_3$ e $N_5$

> [!important] Teorema — Caratterizzazione della Distributività
> Un reticolo è distributivo se e soltanto se **non contiene** sottoreticoli isomorfi a $M_3$ (diamante) o $N_5$ (pentagono).

> [!note] Reticolo Diamante $M_3$
> Il reticolo con 5 elementi $\{0, a, b, c, 1\}$ dove:
> - $a, b, c$ sono mutuamente **non confrontabili**
> - $0 < a, b, c < 1$
> - **Non è distributivo** (ma è modulare).

> [!note] Reticolo Pentagonale $N_5$
> Il reticolo con 5 elementi $\{0, a, b, c, 1\}$ dove:
> - $0 < a < b < 1$ (una catena)
> - $0 < c < 1$ con $c$ **non confrontabile** con $a$ e $b$
> - **Non è distributivo** né modulare.

> [!tip] Dimostrazione — $M_3$ non è distributivo
> Sia $M_3 = \{0, a, b, c, 1\}$ con $a, b, c$ mutuamente non confrontabili.
>
> Consideriamo $a, b, c$:
> $$a \wedge (b \vee c) = a \wedge 1 = a$$
> $$(a \wedge b) \vee (a \wedge c) = 0 \vee 0 = 0$$
>
> Poiché $a \neq 0$, la distributività **fallisce**. $\square$

> [!tip] Dimostrazione — $N_5$ non è distributivo
> Sia $N_5 = \{0, a, b, c, 1\}$ con $0 < a < b < 1$ e $0 < c < 1$ (c non comparabile con a, b).
>
> Consideriamo $a, b, c$:
> $$a \vee (b \wedge c) = a \vee 0 = a$$
> $$(a \vee b) \wedge (a \vee c) = b \wedge 1 = b$$
>
> Poiché $a \neq b$, la distributività **fallisce**. $\square$

### Unicità del Complemento in Reticoli Distributivi

> [!important] Teorema — Unicità del Complemento
> In un reticolo **distributivo e limitato**, se un elemento ha un complemento, questo è **unico**.

> [!tip] Dimostrazione — Unicità del Complemento
> Siano $\bar{a}$ e $\hat{a}$ due complementi di $a$. Allora:
> $$\bar{a} = \bar{a} \wedge 1_L = \bar{a} \wedge (a \vee \hat{a})$$
>
> Per distributività:
> $$= (\bar{a} \wedge a) \vee (\bar{a} \wedge \hat{a}) = 0_L \vee (\bar{a} \wedge \hat{a}) = \bar{a} \wedge \hat{a}$$
>
> Analogamente, $\hat{a} = \bar{a} \wedge \hat{a}$.
>
> Per commutatività, $\bar{a} = \hat{a}$. $\square$

### Reticolo Booleano

> [!note] Reticolo Booleano
> Un reticolo è **booleano** se è **distributivo** e **complementato**.
>
> **Esempio fondamentale:** $(\mathcal{P}(S), \subseteq)$ con complemento $A^c = S \setminus A$.
>
> **Non sono booleani:**
> - Qualsiasi catena con più di 2 elementi (è ordinato ma non è complementato)
> - $M_3$ (è complementato ma non distributivo)
> - $N_5$ (non è distributivo)

> [!important] Teorema di Rappresentazione
> Ogni reticolo booleano **finito** è isomorfo a $(\mathcal{P}(S), \subseteq)$ per un opportuno insieme finito $S$.
>
> **Conseguenza:** Se $|L| = 2^n$, allora $L$ ha $n$ "atomi" (elementi minimali non zero).

### Algebra di Boole

> [!note] Algebra di Boole
> Una struttura $(A, \wedge, \vee, ', 0, 1)$ è un'**algebra di Boole** se:
> 1. **Associatività** di $\wedge$ e $\vee$
> 2. **Commutatività** di $\wedge$ e $\vee$
> 3. **Assorbimento:** $a \wedge (a \vee b) = a$ e $a \vee (a \wedge b) = a$
> 4. **Distributività:** $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$
> 5. **Elementi neutri:** $a \wedge 1 = a$ e $a \vee 0 = a$
> 6. **Complemento:** $a \wedge a' = 0$ e $a \vee a' = 1$
>
> dove $'$ è un'operazione unaria (**complementazione**).

> [!important] Teorema di Rappresentazione di Stone
> Ogni algebra di Boole **finita** è isomorfa a $(\mathcal{P}(S), \cap, \cup, {}^c, \emptyset, S)$ per un opportuno insieme $S$.

### Anello Booleano

> [!note] Anello Booleano
> Un anello $(A, +, \cdot)$ è **booleano** se $a^2 = a$ (idempotenza moltiplicativa) per ogni $a \in A$.
>
> **Proprietà caratteristiche:**
> - $\mathrm{char}(A) = 2$ (cioè $a + a = 0$ per ogni $a$)
> - $(A, \cdot)$ è **commutativo**
>
> **Esempio:** $(\mathcal{P}(S), \triangle, \cap)$ con operazioni differenza simmetrica e intersezione.

> [!tip] Dimostrazione — Proprietà degli Anelli Booleani
> **Caratteristica = 2:** Per ogni $a, b \in A$, sviluppiamo $(a + b)^2 = a + b$ (idempotenza):
> $$(a + b)^2 = a^2 + ab + ba + b^2 = a + ab + ba + b$$
> 
> Quindi $a + b = a + ab + ba + b$, da cui $ab + ba = 0$, cioè $ba = -ab$.
> 
> Ponendo $b = a$: $a^2 + a^2 = 0$, dunque $a + a = 0$. Quindi $\mathrm{char}(A) = 2$ (ogni elemento è auto-inverso).
>
> **Commutatività:** Poiché $ab + ba = 0$ e $x = -x$ per ogni $x \in A$, abbiamo $ab - ba = 0$, cioè $ab = ba$. $\square$

### Corrispondenza tra Reticoli Booleani e Anelli Booleani

> [!note] Da Reticolo Booleano ad Anello Booleano
> Dato un reticolo booleano $(L, \wedge, \vee, ', 0, 1)$, si costruisce l'anello booleano $(L, +, \cdot)$ definendo:
> - **Prodotto (meet):** $a \cdot b = a \wedge b$
> - **Somma (differenza simmetrica):** $a + b = (a \wedge b') \vee (b \wedge a')$
> - **Elementi neutri:** $0_{\text{anello}} = 0_L$ e $1_{\text{anello}} = 1_L$
>
> **Relazione d'ordine recuperata:** $a \leq b \;\Longleftrightarrow\; a \cdot b = a$

---




---

---

# Proprietà dell'Anello delle Classi di Resto $(\mathbb{Z}_m, +, \cdot)$

## Introduzione

> [!note] Struttura Fondamentale
> $(\mathbb{Z}_m, +, \cdot)$ è un **anello commutativo unitario** per ogni $m > 1$:
> - **Unità moltiplicativa:** $\bar{1}$
> - **Elemento nullo (zero additivo):** $\bar{0}$
> - **Operazione addittiva:** $[a]_m + [b]_m = [a + b]_m$
> - **Operazione moltiplicativa:** $[a]_m \cdot [b]_m = [ab]_m$

---

## 1. Divisori dello Zero in $\mathbb{Z}_m$

### Definizione

> [!note] Divisore dello Zero
> Un elemento $\bar{a} \in \mathbb{Z}_m$ con $\bar{a} \neq \bar{0}$ è un **divisore dello zero** se esiste $\bar{b} \in \mathbb{Z}_m$ con $\bar{b} \neq \bar{0}$ tale che:
> $$\bar{a} \cdot \bar{b} = \bar{0}$$
### Teorema Caratterizzante

> [!important] **TEOREMA — Caratterizzazione dei Divisori dello Zero**
> Un elemento $\bar{a} \in \mathbb{Z}_m$ (con $\bar{a} \neq \bar{0}$) è un divisore dello zero **se e solo se**:
> $$\mathrm{MCD}(a, m) \neq 1$$
> 
> Equivalentemente: $\mathrm{MCD}(a, m) > 1$

### Dimostrazione Completa

### Verso (⟹): Divisore dello Zero ⟹ MCD(a,m) ≠ 1

> [!tip] **Prova per Contrapposizione**
> 
> Supponiamo $\bar{a}$ sia divisore dello zero. Allora:
> - Esiste $\bar{b} \neq \bar{0}$ tale che $\bar{a} \cdot \bar{b} = \bar{0}$
> - Questo significa: $ab \equiv 0 \pmod{m}$, cioè $m \mid ab$
>
> **Contrapposizione:** Mostriamo che se $\mathrm{MCD}(a, m) = 1$, allora $\bar{a}$ **non** è divisore dello zero.
>
> Se $\mathrm{MCD}(a, m) = 1$ e $m \mid ab$:
> - Per il **Lemma di Euclide Generalizzato**: $m \mid b$
> - Questo implica $b \equiv 0 \pmod{m}$
> - Quindi $\bar{b} = \bar{0}$, **contraddizione**
>
> Dunque, se $\bar{a}$ è divisore dello zero, necessariamente $\mathrm{MCD}(a, m) \neq 1$. $\square$

### Verso (⟸): MCD(a,m) ≠ 1 ⟹ Divisore dello Zero

> [!tip] **Costruzione Esplicita**
> 
> Dato che $d = \mathrm{MCD}(a, m) \neq 1$, per definizione di MCD:
> $$a = d \cdot a' \quad \text{e} \quad m = d \cdot m' \quad \text{(con $d > 1$)}$$
>
> dove $a'$ e $m'$ sono interi positivi con:
> $$m' = \frac{m}{d} < m \quad \text{(divisore proprio)}$$
>
> **Definiamo** $\bar{b} = [\overline{m'}]_m$.
>
> **Affermazione 1:** $\bar{b} \neq \bar{0}$
> - Se fosse $\bar{b} = \bar{0}$, allora $m \mid m'$
> - Ma $1 \leq m' < m$, quindi $m \nmid m'$ ✗
> - Perciò $\bar{b} \neq \bar{0}$ ✓
>
> **Affermazione 2:** $\bar{a} \cdot \bar{b} = \bar{0}$
> $$\bar{a} \cdot \bar{b} = [\overline{a}]_m \cdot [\overline{m'}]_m = [\overline{a \cdot m'}]_m$$
>
> Sostituendo $a = d \cdot a'$:
> $$= [\overline{(d \cdot a') \cdot m'}]_m = [\overline{a' \cdot (d \cdot m')}]_m$$
>
> Sostituendo $d \cdot m' = m$:
> $$= [\overline{a' \cdot m}]_m = [\overline{0}]_m = \bar{0}$$ ✓
>
> Abbiamo trovato $\bar{b} \neq \bar{0}$ con $\bar{a} \cdot \bar{b} = \bar{0}$: **$\bar{a}$ è divisore dello zero**. $\square$

#### Esempio Concreto

> [!note] **Esempio: $\bar{6} \in \mathbb{Z}_{15}$**
>
> **Dati:** $a = 6$, $m = 15$, $\mathrm{MCD}(6, 15) = 3 > 1$ ✓
>
> **Fattorizzazione:**
> - $d = 3$
> - $6 = 3 \cdot 2$ ⟹ $a' = 2$
> - $15 = 3 \cdot 5$ ⟹ $m' = 5$
>
> **Elemento divisore dello zero:**
> - $\bar{b} = \bar{5} \neq \bar{0}$ ✓
> - $\bar{6} \cdot \bar{5} = [\overline{30}]_{15} = [\overline{0}]_{15} = \bar{0}$ ✓

---

## 2. Elementi Invertibili in $\mathbb{Z}_m$

### Definizione

> [!note] Elemento Invertibile
> Un elemento $\bar{a} \in \mathbb{Z}_m$ è **invertibile** (o **simmetrizzabile** rispetto al prodotto) se esiste $\bar{b} \in \mathbb{Z}_m$ tale che:
> $$\bar{a} \cdot \bar{b} = \bar{1}$$
> 
> L'elemento $\bar{b}$ si chiama **inverso moltiplicativo** di $\bar{a}$ e si denota $\bar{a}^{-1}$.

### Teorema Caratterizzante

> [!important] **TEOREMA — Caratterizzazione degli Elementi Invertibili**
> Un elemento $\bar{a} \in \mathbb{Z}_m$ è invertibile **se e solo se**:
> $$\mathrm{MCD}(a, m) = 1$$
> 
> Cioè, $a$ e $m$ sono **coprimi** (primi tra loro).

#### Dimostrazione Completa

##### Verso (⟸): MCD(a,m) = 1 ⟹ [a]_m Invertibile

> [!tip] **Teorema di Bézout**
> 
> Se $\mathrm{MCD}(a, m) = 1$, allora per il **Teorema di Bézout Esteso**, esistono interi $h, k$ tali che:
> $$a \cdot h + m \cdot k = 1$$
>
> **Riduciamo modulo $m$:**
> $$a \cdot h + m \cdot k \equiv 1 \pmod{m}$$
>
> Poiché $m \cdot k \equiv 0 \pmod{m}$:
> $$a \cdot h \equiv 1 \pmod{m}$$
>
> **In notazione di classi:**
> $$\bar{a} \cdot \bar{h} = \bar{1}$$
>
> Quindi **$\bar{h}$ è l'inverso moltiplicativo di $\bar{a}$**, e $\bar{a}$ è **invertibile**. $\square$

### Verso (⟹): [a]_m Invertibile ⟹ MCD(a,m) = 1

> [!tip] **Identità di Bézout Inversa**
> 
> Se $\bar{a}$ è invertibile, esiste $\bar{b}$ tale che:
> $$\bar{a} \cdot \bar{b} = \bar{1}$$
>
> Questo significa:
> $$ab \equiv 1 \pmod{m}$$
>
> Per definizione di congruenza, esiste intero $k$ tale che:
> $$ab = 1 + km$$
>
> Riarrangiando:
> $$ab - km = 1$$
>
> Questa è un'**identità di Bézout**. Per il **Teorema di Bézout (Contrapositivo)**, se esiste combinazione lineare di $a$ e $m$ che produce 1:
> $$\mathrm{MCD}(a, m) = 1$$ $\square$

### L'Insieme degli Invertibili: $U(\mathbb{Z}_m)$

> [!note] Gruppo Moltiplicativo degli Invertibili
> L'insieme:
> $$U(\mathbb{Z}_m) = \{\bar{a} \in \mathbb{Z}_m \mid \mathrm{MCD}(a, m) = 1\}$$
> 
> forma un **gruppo abeliano** rispetto alla moltiplicazione in $\mathbb{Z}_m$.
>
> **Proprietà:**
> - **Chiuso:** Se $\mathrm{MCD}(a, m) = 1$ e $\mathrm{MCD}(b, m) = 1$, allora $\mathrm{MCD}(ab, m) = 1$
> - **Associatività:** Ereditata dall'anello
> - **Identità:** $\bar{1} \in U(\mathbb{Z}_m)$ (poiché $\mathrm{MCD}(1, m) = 1$)
> - **Inversi:** Ogni elemento ha inverso (per definizione di $U(\mathbb{Z}_m)$)
> - **Commutatività:** $\mathbb{Z}_m$ è commutativo

#### La Funzione Toziente di Eulero

> [!note] Cardinalità di $U(\mathbb{Z}_m)$ — Funzione toziente
> Il numero di elementi invertibili in $\mathbb{Z}_m$ è dato dalla **funzione toziente di Eulero**:
> $$|U(\mathbb{Z}_m)| = \varphi(m)$$
> 
> dove $\varphi(m)$ è il numero di interi in $\{1, 2, \ldots, m-1\}$ coprimi con $m$.

#### Formula Esplicita per $\varphi(m)$

> [!note] Formula Moltiplicativa
> Se $m = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k}$, allora:
> $$\varphi(m) = m \prod_{p \mid m} \left(1 - \frac{1}{p}\right) = \prod_{i=1}^{k} p_i^{\alpha_i-1}(p_i - 1)$$
#### Esempi di $\varphi(m)$

| $m$ | Fattorizzazione | $\varphi(m)$ | Calcolo |
|---|---|---|---|
| 6 | $2 \cdot 3$ | 2 | $6(1 - 1/2)(1 - 1/3) = 6 \cdot 1/2 \cdot 2/3 = 2$ |
| 12 | $2^2 \cdot 3$ | 4 | $12(1 - 1/2)(1 - 1/3) = 12 \cdot 1/2 \cdot 2/3 = 4$ |
| 15 | $3 \cdot 5$ | 8 | $15(1 - 1/3)(1 - 1/5) = 15 \cdot 2/3 \cdot 4/5 = 8$ |
| 20 | $2^2 \cdot 5$ | 8 | $20(1 - 1/2)(1 - 1/5) = 20 \cdot 1/2 \cdot 4/5 = 8$ |

#### Esempio Concreto

> [!note] **Esempio: Elementi Invertibili in $\mathbb{Z}_{15}$**
>
> $15 = 3 \cdot 5$, quindi $\varphi(15) = 15 \cdot (1 - 1/3)(1 - 1/5) = 15 \cdot 2/3 \cdot 4/5 = 8$
>
> **Elementi coprimi con 15:**
> - $\mathrm{MCD}(1, 15) = 1$ ✓
> - $\mathrm{MCD}(2, 15) = 1$ ✓
> - $\mathrm{MCD}(4, 15) = 1$ ✓
> - $\mathrm{MCD}(7, 15) = 1$ ✓
> - $\mathrm{MCD}(8, 15) = 1$ ✓
> - $\mathrm{MCD}(11, 15) = 1$ ✓
> - $\mathrm{MCD}(13, 15) = 1$ ✓
> - $\mathrm{MCD}(14, 15) = 1$ ✓
>
> $$U(\mathbb{Z}_{15}) = \{\bar{1}, \bar{2}, \bar{4}, \bar{7}, \bar{8}, \bar{11}, \bar{13}, \bar{14}\}$$
> $$|U(\mathbb{Z}_{15})| = 8 = \varphi(15)$$ ✓

---

## 3. Corollario: $\mathbb{Z}_p$ è un Campo (quando $p$ è primo)

### Teorema

> [!important] **TEOREMA — $\mathbb{Z}_p$ è un Campo**
> Se $p$ è un numero **primo**, allora $(\mathbb{Z}_p, +, \cdot)$ è un **campo**.

#### Dimostrazione

> [!tip] **Passo 1: Ricordiamo la Definizione di Campo**
> 
> Un anello commutativo unitario $(F, +, \cdot)$ è un **campo** se:
> - Ogni elemento **non nullo** è **invertibile**

> [!tip] **Passo 2: Elementi di $\mathbb{Z}_p$**
> 
> Gli elementi non nulli di $\mathbb{Z}_p$ sono:
> $$\mathbb{Z}_p^* = \{\bar{1}, \bar{2}, \ldots, \overline{p-1}\}$$
>
> Ogni $\bar{a}$ corrisponde a un intero $a \in \{1, 2, \ldots, p-1\}$.

> [!tip] **Passo 3: Proprietà dei Primi**
> 
> Poiché $p$ è **primo**:
> - $p$ ha come unici divisori positivi: 1 e $p$ stesso
> - Per ogni $a \in \{1, 2, \ldots, p-1\}$: $a < p$
> - Quindi $a$ **non è un multiplo di $p$**
> - L'unico divisore comune di $a$ e $p$ è 1
> - Dunque: $\mathrm{MCD}(a, p) = 1$ ✓

> [!tip] **Passo 4: Invertibilità di Ogni Elemento Non Nullo**
> 
> Per il **Teorema Caratterizzante degli Elementi Invertibili**:
> $$\mathrm{MCD}(a, p) = 1 \quad \Rightarrow \quad \bar{a} \text{ è invertibile}$$
>
> Quindi **ogni $\bar{a} \in \mathbb{Z}_p^*$ è invertibile**.

> [!tip] **Passo 5: Conclusione**
> 
> Poiché $(\mathbb{Z}_p, +, \cdot)$ è:
> - **Anello commutativo unitario** (per qualsiasi $p$)
> - **Ogni elemento non nullo è invertibile** (quando $p$ è primo)
>
> Per definizione, $\boxed{\mathbb{Z}_p \text{ è un campo}}$. $\square$

#### Esempi

> [!note] **Esempi di Campi**
> 
> - $\mathbb{Z}_2 = \{\bar{0}, \bar{1}\}$ è un campo (campo finito con 2 elementi, $\mathbb{F}_2$)
> - $\mathbb{Z}_3 = \{\bar{0}, \bar{1}, \bar{2}\}$ è un campo
> - $\mathbb{Z}_5 = \{\bar{0}, \bar{1}, \bar{2}, \bar{3}, \bar{4}\}$ è un campo
> - $\mathbb{Z}_{11}, \mathbb{Z}_{13}, \mathbb{Z}_{17}, \ldots$ sono tutti campi

> [!note] **Contro-Esempi: Non-Campi**
> 
> - $\mathbb{Z}_4$: $\bar{2} \neq \bar{0}$ ma $\mathrm{MCD}(2, 4) = 2 \neq 1$, quindi $\bar{2}$ **non è invertibile**
> - $\mathbb{Z}_6$: $\bar{2}, \bar{3}, \bar{4}$ non sono invertibili (hanno MCD > 1 con 6)
> - $\mathbb{Z}_{15}$: $\bar{3}, \bar{5}, \bar{6}, \ldots$ non sono invertibili

---

## 4. Elementi Nilpotenti in $\mathbb{Z}_m$

### Definizione

> [!note] Elemento Nilpotente
> Un elemento $\bar{a} \in \mathbb{Z}_m$ è **nilpotente** se esiste un intero positivo $N$ tale che:
> $$\bar{a}^N = \bar{0}$$
> 
> In altri termini: $a^N \equiv 0 \pmod{m}$

### Teorema Caratterizzante

> [!important] **TEOREMA — Caratterizzazione degli Elementi Nilpotenti**
> Sia $m = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k}$ la fattorizzazione in primi distinti di $m$.
> 
> Un elemento $\bar{a} \in \mathbb{Z}_m$ è nilpotente **se e solo se**:
> $$p_i \mid a \quad \text{per ogni fattore primo } p_i \text{ di } m$$
> 
> Equivalentemente: $a$ è un multiplo del **radicale di $m$**:
> $$\mathrm{rad}(m) = p_1 p_2 \cdots p_k \mid a$$
### Radicale di un Numero

> [!note] Radicale
> Il **radicale** di $m$ è il prodotto di tutti i fattori primi distinti di $m$:
> $$\mathrm{rad}(m) = \prod_{p \mid m, \, p \text{ primo}} p$$
>
> **Esempi:**
> - $\mathrm{rad}(12) = \mathrm{rad}(2^2 \cdot 3) = 2 \cdot 3 = 6$
> - $\mathrm{rad}(20) = \mathrm{rad}(2^2 \cdot 5) = 2 \cdot 5 = 10$
> - $\mathrm{rad}(100) = \mathrm{rad}(2^2 \cdot 5^2) = 2 \cdot 5 = 10$

#### Dimostrazione Completa

##### Verso (⟹): Nilpotente ⟹ rad(m) | a

> [!tip] **Ipotesi: $\bar{a}$ è Nilpotente**
> 
> Allora esiste $N \geq 1$ tale che $\bar{a}^N = \bar{0}$.
>
> Per definizione di congruenza:
> $$a^N \equiv 0 \pmod{m} \quad \Rightarrow \quad m \mid a^N$$
>
> **Per ogni fattore primo $p_i$ di $m$:**
> - Poiché $m = p_1^{\alpha_1} \cdots p_k^{\alpha_k}$ e $m \mid a^N$
> - Ogni $p_i^{\alpha_i} \mid a^N$
> - Per il Lemma di Euclide: se $p_i \mid a^N$, allora $p_i \mid a$
>
> Quindi **ogni primo che divide $m$ divide anche $a$**, cioè:
> $$\mathrm{rad}(m) = p_1 \cdots p_k \mid a$$ $\square$

##### Verso (⟸): rad(m) | a ⟹ Nilpotente

> [!tip] **Ipotesi: $\mathrm{rad}(m) | a$**
> 
> Se $\mathrm{rad}(m) \mid a$, allora ogni primo $p_i$ divide $a$.
> 
> Possiamo scrivere: $a = \mathrm{rad}(m) \cdot b$ per qualche intero $b$.
>
> **Scegliamo** $N = \max(\alpha_1, \alpha_2, \ldots, \alpha_k)$ (l'esponente massimo nella fattorizzazione di $m$).
>
> Allora:
> $$a^N = (\mathrm{rad}(m) \cdot b)^N = \mathrm{rad}(m)^N \cdot b^N = (p_1 \cdots p_k)^N \cdot b^N$$
>
> Poiché ogni $p_i$ appare con esponente $\geq N$ in $a^N$:
> $$p_i^{\alpha_i} \mid a^N \quad \text{per ogni } i$$
>
> Quindi:
> $$m = p_1^{\alpha_1} \cdots p_k^{\alpha_k} \mid a^N$$
>
> Cioè $\bar{a}^N = \bar{0}$ in $\mathbb{Z}_m$: **$\bar{a}$ è nilpotente**. $\square$

#### Esempio Concreto

> [!note] **Esempio: Elementi Nilpotenti in $\mathbb{Z}_{12}$**
>
> $12 = 2^2 \cdot 3$, quindi $\mathrm{rad}(12) = 2 \cdot 3 = 6$
>
> **Elementi nilpotenti:** Multipli di 6 in $\{0, 1, \ldots, 11\}$ (escludendo 0):
> - $\bar{6}$: $6 = 6 \cdot 1$ ✓
>
> **Verifica:** $\bar{6}^2 = [\overline{36}]_{12} = [\overline{0}]_{12} = \bar{0}$ ✓
>
> È il **solo elemento nilpotente non nullo** di $\mathbb{Z}_{12}$.

### Numero di Elementi Nilpotenti

> [!note] Cardinalità dell'Insieme dei Nilpotenti
> Il numero di elementi nilpotenti in $\mathbb{Z}_m$ è:
> $$\#\{\bar{a} \in \mathbb{Z}_m \mid \bar{a} \text{ nilpotente}\} = \frac{m}{\mathrm{rad}(m)}$$
>
> (Incluso $\bar{0}$, che è sempre nilpotente.)

---

## 5. Elementi Idempotenti in $\mathbb{Z}_m$

### Definizione

> [!note] Elemento Idempotente
> Un elemento $\bar{a} \in \mathbb{Z}_m$ è **idempotente** se:
> $$\bar{a}^2 = \bar{a}$$
> 
> In termini di congruenza: $a^2 \equiv a \pmod{m}$

### Caratterizzazione Algebrica

> [!note] Equivalenza Algebrica
> $\bar{a}$ è idempotente se e solo se:
> $$a^2 \equiv a \pmod{m} \quad \Longleftrightarrow \quad m \mid (a^2 - a) \quad \Longleftrightarrow \quad m \mid a(a-1)$$
### Elementi Idempotenti Banali

> [!note] Idempotenti Banali
> **Sempre** $\bar{0}$ e $\bar{1}$ sono idempotenti:
> - $\bar{0}^2 = \bar{0} \cdot \bar{0} = \bar{0}$ ✓
> - $\bar{1}^2 = \bar{1} \cdot \bar{1} = \bar{1}$ ✓

### Caratterizzazione Completa (Teorema Cinese dei Resti)

> [!important] **TEOREMA — Elementi Idempotenti**
> Un elemento $\bar{a} \in \mathbb{Z}_m$ è idempotente se e solo se:
> $$a \equiv 0 \pmod{p^k} \quad \text{oppure} \quad a \equiv 1 \pmod{p^k}$$
> 
> **per ogni potenza primo** $p^{\alpha_p}$ nella fattorizzazione di $m$.
>
> Equivalentemente, usando il **Teorema Cinese dei Resti**, gli idempotenti di $\mathbb{Z}_m$ corrispondono a scelte indipendenti in ogni componente $\mathbb{Z}_{p_i^{\alpha_i}}$.

### Numero di Elementi Idempotenti

> [!note] Cardinalità dell'Insieme degli Idempotenti
> Se $m = p_1^{\alpha_1} \cdots p_k^{\alpha_k}$, il numero di elementi idempotenti è:
> $$\#\{\bar{a} \in \mathbb{Z}_m \mid \bar{a}^2 = \bar{a}\} = 2^k$$
> 
> dove $k$ è il numero di **fattori primi distinti** di $m$.

#### Esempi Concreti

##### Esempio 1: $\mathbb{Z}_6$

> [!note] **Elementi Idempotenti in $\mathbb{Z}_6$**
>
> $6 = 2 \cdot 3$ (2 fattori primi distinti), quindi ci sono $2^2 = 4$ idempotenti.
>
> **Verifichiamo ogni elemento:**
> - $\bar{0}^2 = \bar{0}$ ✓ (idempotente banale)
> - $\bar{1}^2 = \bar{1}$ ✓ (idempotente banale)
> - $\bar{2}^2 = \bar{4} \neq \bar{2}$ ✗
> - $\bar{3}^2 = \bar{9} = \bar{3}$ ✓ (idempotente: $9 \equiv 3 \pmod{6}$)
> - $\bar{4}^2 = \bar{16} = \bar{4}$ ✓ (idempotente: $16 \equiv 4 \pmod{6}$)
> - $\bar{5}^2 = \bar{25} = \bar{1} \neq \bar{5}$ ✗
>
> **Idempotenti:** $\{\bar{0}, \bar{1}, \bar{3}, \bar{4}\}$ — totale: 4 ✓

##### Esempio 2: $\mathbb{Z}_{12}$

> [!note] **Elementi Idempotenti in $\mathbb{Z}_{12}$**
>
> $12 = 2^2 \cdot 3$ (2 fattori primi distinti), quindi ci sono $2^2 = 4$ idempotenti.
>
> **Calcoli modulo 12:**
> - $\bar{0}^2 = \bar{0}$ ✓
> - $\bar{1}^2 = \bar{1}$ ✓
> - $\bar{3}^2 = \bar{9}$ ✗ (perché $9 \not\equiv 3 \pmod{12}$)
> - $\bar{4}^2 = \bar{16} = \bar{4}$ ✓
> - $\bar{9}^2 = \bar{81} = \bar{9}$ ✓
>
> **Idempotenti:** $\{\bar{0}, \bar{1}, \bar{4}, \bar{9}\}$ — totale: 4 ✓

### Interpretazione Geometrica: Anello Prodotto

> [!note] Teorema Cinese dei Resti e Idempotenti
> Se $m = p_1^{\alpha_1} \cdots p_k^{\alpha_k}$, allora:
> $$\mathbb{Z}_m \cong \mathbb{Z}_{p_1^{\alpha_1}} \times \cdots \times \mathbb{Z}_{p_k^{\alpha_k}}$$
>
> Gli idempotenti di $\mathbb{Z}_m$ corrispondono alle **proiezioni** $(e_1, \ldots, e_k)$ dove ogni $e_i \in \{\bar{0}, \bar{1}\}$ in $\mathbb{Z}_{p_i^{\alpha_i}}$.
>
> Con $2^k$ scelte indipendenti, otteniamo $2^k$ idempotenti totali.

---

---
## Tabella Riassuntiva: Proprietà Confrontate

| **Proprietà** | **Condizione** | **Numero** | **Esempi** |
|---|---|---|---|
| **Divisori dello Zero** | $\mathrm{MCD}(a, m) > 1$ | $m - \varphi(m) - 1$ | In $\mathbb{Z}_{12}$: $\bar{2}, \bar{3}, \bar{4}, \bar{6}, \bar{8}, \bar{9}, \bar{10}$ |
| **Invertibili** | $\mathrm{MCD}(a, m) = 1$ | $\varphi(m)$ | In $\mathbb{Z}_{12}$: $\bar{1}, \bar{5}, \bar{7}, \bar{11}$ ($\varphi(12) = 4$) |
| **Nilpotenti** | Multipli di $\mathrm{rad}(m)$ | $m / \mathrm{rad}(m)$ | In $\mathbb{Z}_{12}$: $\bar{0}, \bar{6}$ (2 elementi) |
| **Idempotenti** | $a^2 \equiv a \pmod{m}$ | $2^k$ ($k$ = fattori primi) | In $\mathbb{Z}_{12}$: $\bar{0}, \bar{1}, \bar{4}, \bar{9}$ (4 elementi) |

---

## Osservazione Finale: Relazioni tra le Proprietà

> [!important] **Implicazioni tra Proprietà**
> 
> 1. **Nilpotente ⟹ Divisore dello Zero** (eccetto lo zero)
>    - Se $\bar{a}^N = \bar{0}$, allora $\bar{a} \cdot \bar{a}^{N-1} = \bar{0}$ con $\bar{a}^{N-1} \neq \bar{0}$ (in genere)
>
> 2. **Invertibile ⟹ Non Divisore dello Zero**
>    - Se $\bar{a}$ è invertibile e $\bar{a} \cdot \bar{b} = \bar{0}$, allora $\bar{b} = \bar{a}^{-1} \cdot \bar{0} = \bar{0}$
>
> 3. **Idempotente ⟹ Non Nilpotente** (eccetto $\bar{0}$)
>    - Se $\bar{a}^2 = \bar{a}$, allora $\bar{a}^N = \bar{a}$ per ogni $N \geq 1$, quindi mai $\bar{a}^N = \bar{0}$ (a meno che $\bar{a} = \bar{0}$)