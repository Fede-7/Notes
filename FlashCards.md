#flashcards/Algebra/Definizioni
# Flashcard Algebra — Elenco Definizioni

## Lezione 1 — Logica, Insiemi, Funzioni

Negazione :: ¬P è vera quando P è falsa, e viceversa.
Congiunzione :: P ∧ Q è vera solo quando **entrambe** P e Q sono vere.
Disgiunzione Inclusiva :: P ∨ Q è falsa solo quando **entrambe** P e Q sono false.
Implicazione :: P ⇒ Q è falsa solo quando P è vera e Q è falsa.
Bicondizionale :: P ⇔ Q è vera quando P e Q hanno lo **stesso valore di verità**.
Tautologia :: Proposizione composta **sempre vera**, qualunque siano i valori di verità delle componenti. Esempio: P ∨ ¬P.
Contraddizione :: Proposizione composta **sempre falsa**. Esempio: P ∧ ¬P.
XOR (Disgiunzione Esclusiva) :: a ⊕ b ⟺ (¬a ∧ b) ∨ (a ∧ ¬b)
NAND / NOR :: Sono **funzionalmente completi**: ogni connettivo logico può essere espresso usando solo NAND (o solo NOR).
Legge di De Morgan :: ¬(P ∧ Q) ⇔ ¬P ∨ ¬Q ; ¬(P ∨ Q) ⇔ ¬P ∧ ¬Q
Predicato :: Proprietà o relazione con variabili; una formula ben formata (FBF) diventa proposizione quando le variabili vengono sostituite.
<!--SR:!2026-02-25,1,210-->
Quantificatore Universale :: ∀x P(x): «per ogni x, vale P(x)».
Quantificatore Esistenziale :: ∃x P(x): «esiste almeno un x tale che P(x)».
Quantificatore Esistenziale Unico :: ∃!x P(x) ⟺ ∃x P(x) ∧ ∀x∀y(P(x) ∧ P(y) ⇒ x = y)
Variabile Vincolata :: Una variabile che compare nel raggio d'azione di un quantificatore. Altrimenti è **libera**. Una formula senza variabili libere è detta **chiusa**.
C'os è un Insieme? :: Collezione di oggetti distinti, detti **elementi**. Si scrive a ∈ A se a appartiene ad A.
Insieme Vuoto :: ∅ — l'insieme privo di elementi.
Sottoinsieme :: A ⊆ B ⟺ ∀x (x ∈ A ⇒ x ∈ B).
Prodotto Cartesiano :: A × B = {(a, b) | a ∈ A ∧ b ∈ B}
Unione :: A ∪ B = {x | x ∈ A ∨ x ∈ B}
Intersezione :: A ∩ B = {x | x ∈ A ∧ x ∈ B}
Differenza :: A \ B = {x | x ∈ A ∧ x ∉ B}
Complemento :: Aᶜ = {x ∈ U | x ∉ A}
Differenza Simmetrica :: A △ B = (A \ B) ∪ (B \ A)
Relazione (Corrispondenza) :: ρ ⊆ A × B — un sottoinsieme del prodotto cartesiano.
Funzione :: f : A → B è una relazione tale che ∀a ∈ A, ∃!b ∈ B con (a, b) ∈ Gf. A è il **dominio**, B il **codominio**.
<!--SR:!2026-02-26,2,243-->

## Lezione 2 — Quantificatori, Immagini, Iniettività, Partizioni

Negazione dei Quantificatori :: ¬(∀x P(x)) ⟺ ∃x(¬P(x)) ; ¬(∃x P(x)) ⟺ ∀x(¬P(x))
Ordine dei Quantificatori :: ∃y∀x φ(x,y) ⟹ ∀x∃y φ(x,y) — il viceversa non vale in generale.
Immagine di un Sottoinsieme :: f→(X) = {f(x) | x ∈ X} ⊆ B — insieme degli elementi del codominio raggiunti da X.
Controimmagine (Preimmagine) :: f←(Y) = {x ∈ A | f(x) ∈ Y} ⊆ A — insieme degli elementi del dominio le cui immagini cadono in Y.
Iniettività :: f : A → B è iniettiva se: ∀x₁, x₂ ∈ A : f(x₁) = f(x₂) ⟹ x₁ = x₂
Caratterizzazione Iniettività tramite Controimmagine :: f è iniettiva ⟺ ∀b ∈ B, |f⁻¹({b})| ≤ 1
Partizione :: Una famiglia F ⊆ P(S) è una partizione di S se: (1) ∀X ∈ F, X ≠ ∅; (2) pezzi disgiunti; (3) ⋃F = S.
Partizioni Banali :: F₁ = {{S}} (un solo pezzo: l'insieme intero); F₂ = {{a},{b},{c},…} (ogni pezzo è un singolo elemento).
<!--SR:!2026-02-26,2,243-->

## Lezione 3 — Suriettività, Funzione Caratteristica, Restrizione, Identità

Suriettività :: f : A → B è suriettiva se: ∀b ∈ B, ∃a ∈ A : f(a) = b
<!--SR:!2026-02-26,2,243-->
Caratterizzazione Suriettività tramite Controimmagine :: f è suriettiva ⟺ ∀b ∈ B, |f⁻¹({b})| ≥ 1
Applicazioni immagine e anti-immagine banali :: f(∅) = ∅ ; f⁻¹(∅) = ∅ ; f⁻¹(B) = A ; f(A) = Im(f) ⊆ B (e f(A) = B sse f è suriettiva).
Funzione Caratteristica :: Sia A ⊆ S. χ_A : S → {0,1} con χ_A(x) = 1 se x ∈ A, 0 se x ∉ A.
Uguaglianza di Funzioni :: f = g sse hanno lo stesso dominio, lo stesso codominio e f(x) = g(x) per ogni x.
Restrizione :: Sia C ⊆ A. La restrizione di f : A → B a C è f|_C : C → B con f|_C(x) = f(x).
Prolungamento (Estensione) :: f : A → B estende g : C → B se C ⊆ A e f(x) = g(x) per ogni x ∈ C.
Identità :: id_A : A → A definita da id_A(a) = a. È sempre **biettiva**.

## Lezione 4 — Biettività, Composizione, Invertibilità, Operazioni

Biettività :: f : A → B è biettiva se è **iniettiva e suriettiva**: ∀b ∈ B, |f←({b})| = 1
Caratterizzazione Biettività :: f è biettiva ⟺ per ogni b ∈ B, la controimmagine f⁻¹({b}) è un singleton.
Equipotenza :: |A| = |B| ⟺ ∃f biettiva tra A e B.
Composizione :: Date f : A → B e g : B → C: (g ∘ f)(x) = g(f(x)), (g ∘ f) : A → C.
<!--SR:!2026-02-26,2,243-->
Proprietà della Composizione :: Associativa: (h ∘ g) ∘ f = h ∘ (g ∘ f). Non commutativa: g ∘ f ≠ f ∘ g.
Corrispondenza Complementare :: Data φ ⊆ A × B: φ' = (A × B) \ φ.
Corrispondenza Inversa :: Data φ ⊆ A × B: φ⁻¹ = {(b, a) ∈ B × A : (a, b) ∈ φ}.
Funzione Invertibile :: f : A → B è invertibile ⟺ ∃f⁻¹ : B → A t.c. f⁻¹ ∘ f = id_A e f ∘ f⁻¹ = id_B.
<!--SR:!2026-02-25,1,230-->
Teorema Fondamentale — Invertibilità :: Una funzione f è completamente invertibile ⟺ **biettiva**.
Inversa Sinistra :: g ∘ f = id_A. Esiste ⟺ f è **iniettiva**.
Inversa Destra :: f ∘ h = id_B. Esiste ⟺ f è **suriettiva**.
Operazione n-aria :: Una funzione f : Aⁿ → A. n=1 → unaria interna; n=2 → binaria interna.

## Lezione 5 — Matrici, Semigruppo, Monoide

Struttura Algebrica :: (S, O) dove S è un insieme non vuoto e O è una famiglia di operazioni su S.
Matrice m×n :: Tabella rettangolare di m righe e n colonne di elementi di un anello. Trasposta: (Aᵀ)ᵢⱼ = Aⱼᵢ.
Magma :: (S, ∗), con ∗ operazione binaria interna.
Associatività :: ∀a, b, c ∈ S : (a ∗ b) ∗ c = a ∗ (b ∗ c)
Semigruppo :: (S, ∗) dove ∗ è un'operazione binaria **associativa**.
Elemento Neutro :: u ∈ S tale che ∀a ∈ S : a ∗ u = u ∗ a = a. Se esiste, è **unico**.
Monoide :: Semigruppo con elemento neutro: (S, ∗, u). Esempi: (ℕ, +, 0), (ℕ, ·, 1), (P(S), ∩, S), (P(S), ∪, ∅).

## Lezione 6 — Prodotto Matrici, Invertibili, Parte Stabile, Gruppi

Prodotto Matriciale :: Date A ∈ M_{m×p} e B ∈ M_{p×n}: cᵢⱼ = Σₖ aᵢₖ · bₖⱼ. Non commutativo; associativo; Iₙ è elemento neutro.
Elemento Invertibile (Simmetrizzabile) :: In un monoide (S, ∗, u), a ∈ S è invertibile se: ∃a' ∈ S : a ∗ a' = a' ∗ a = u. L'inverso è **unico**.
U(S) — Gruppo degli Invertibili :: L'insieme degli elementi invertibili di un monoide forma un gruppo (U(S), ∗).
Parte Stabile (Chiusa) :: H ⊆ S è stabile per ∗ se: ∀h, k ∈ H : h ∗ k ∈ H.
Gruppo :: (G, ∗) è un gruppo se: (1) ∗ è associativa; (2) esiste elemento neutro u; (3) ogni elemento ha un inverso.
Gruppo Abeliano :: Gruppo in cui ∗ è **commutativa**: a ∗ b = b ∗ a.

## Lezione 7 — Anelli, Caratteristica, Cancellabilità, Divisori dello Zero

Inversa 2×2 :: Sia A = [[a,b],[c,d]] con det(A) = ad − bc ≠ 0: A⁻¹ = 1/(ad−bc) · [[d,−b],[−c,a]]
Anello :: (A, +, ·) è un anello se: (1) (A,+) è gruppo abeliano; (2) (A,·) è semigruppo; (3) valgono le proprietà distributive.
Anello Commutativo :: (S, ·) commutativo: a · b = b · a per ogni a, b.
Anello Unitario :: (S, ·) monoide: esiste un'unità 1_A tale che a · 1_A = 1_A · a = a.
<!--SR:!2026-02-26,2,230-->
Anello Booleano :: Anello con a · a = a per ogni a. Esempio: (P(S), △, ∩).
Caratteristica di un Anello Unitario :: char(A) = min{m > 0 | 1_A + ⋯ + 1_A (m volte) = 0_A}. Se non esiste, char(A) = 0.
Cancellabilità :: a è cancellabile a sinistra se a·b = a·c ⇒ b = c. A destra se b·a = c·a ⇒ b = c. Invertibile ⟹ Cancellabile.
Divisore dello Zero :: a ≠ 0_A è divisore dello zero se ∃b ≠ 0_A : a · b = 0_A. Equivalentemente: a ≠ 0 è divisore dello zero ⟺ a non è cancellabile.

## Lezione 8 — Omomorfismo, Dominio, Campo, Spazio Vettoriale, Sn

Omomorfismo :: f : (S, ∗) → (T, ·) è un omomorfismo se: f(a ∗ b) = f(a) · f(b) ∀a, b ∈ S.
<!--SR:!2026-02-26,2,230-->
Dominio d'Integrità :: Un anello (A, +, ·) è un dominio d'integrità se: è commutativo, è unitario (con 1_A ≠ 0_A), è privo di divisori dello zero. Esempi: ℤ, ℚ, ℝ, ℂ.
<!--SR:!2026-02-26,3,250-->
Corpo :: Un anello (K, +, ·) è un corpo se: è unitario (con 1_K ≠ 0_K) e (K*, ·) è un gruppo, dove K* = K \ {0_K}.
Campo :: Un campo è un **corpo commutativo**. Esempi: ℚ, ℝ, ℂ, ℤ_p (con p primo).
Teorema di Wedderburn :: Ogni corpo finito è anche un **campo**.
Che cos'è un K-Spazio Vettoriale?
?
Sia K un campo. (V, +, ·_ext) è un **K-spazio vettoriale** se:
1. (V,+) è **gruppo abeliano**
2. ·_ext : K × V → V soddisfa:
   - **Associatività mista:** α·(β·v) = (α·β)·v
   - **Distributività scalari:** (α+β)·v = α·v + β·v
   - **Distributività vettori:** α·(u+v) = α·u + α·v
   - **Elemento neutro:** 1_K · v = v
...
Gruppo Simmetrico Sₙ :: B(S) = insieme delle permutazioni di S. (B(S), ∘) è un gruppo detto Sₙ. |Sₙ| = n!. Non abeliano per n ≥ 3.

## Lezione 9 — Cayley, Nilpotenti, Divisibilità, MCD, mcm, Primi

Notazione Ciclica (Permutazioni) :: Un ciclo (c₁c₂⋯cₖ): σ(cᵢ) = cᵢ₊₁, σ(cₖ) = c₁, σ(x) = x altrimenti.
<!--SR:!2026-02-26,2,230-->
Teorema di Scomposizione Canonica :: Ogni permutazione σ ∈ Sₙ diversa dall'identità si scrive come prodotto di cicli disgiunti. La scomposizione è unica a meno dell'ordine.
Inversa di un Ciclo :: (c₁c₂⋯cₖ)⁻¹ = (c₁cₖcₖ₋₁⋯c₂)
Quali proprietà sono visibili dalle Tavole di Cayley?
?
- **Commutatività** ⟺ tabella simmetrica rispetto alla diagonale
- **Cancellabilità** ⟺ nessuna ripetizione nelle righe/colonne
- **Elemento Neutro** ⟺ riga/colonna con elementi uguali agli indici
- **Simmetrizzabili** ⟺ ∗ restituisce l'elemento neutro
<!--SR:!2026-02-26,3,250-->
...
Cancellabilità in Strutture Finite :: In un magma **finito** (S, ∗), a è cancellabile ⟺ la funzione x ↦ a ∗ x è **iniettiva** (e quindi biettiva, essendo S finito).
Nilpotente :: a ∈ A è nilpotente se ∃n ≥ 1 : aⁿ = 0_A. Nilpotente non nullo ⟹ Divisore dello zero.
Divisibilità :: b | a ⟺ ∃c : a = b · c. div(a): insieme dei divisori di a. mult(b): insieme dei multipli di b.
Associati :: Sia x, y ∈ A anello commutativo unitario. x ∼ y ⟺ ∃u ∈ U(A) : x = u · y. È una relazione di equivalenza.
Divisori Banali e Propri :: I **divisori banali** di a sono: gli associati a 1 (cioè gli invertibili U(A)) e gli associati ad a stesso. Un **divisore proprio** è un divisore di a che non è né invertibile né associato ad a.
Massimo Comun Divisore :: e = MCD(a, b) se: (1) e|a e e|b; (2) ∀x : (x|a ∧ x|b) ⇒ x|e.
Minimo Comune Multiplo :: m = mcm(a, b) se: (1) a|m e b|m; (2) ∀x : (a|x ∧ b|x) ⇒ m|x.
Numero Primo :: p è primo se p ∉ U(ℤ) e div(p) = {1, −1, p, −p}.
Lemma di Euclide :: Se p è primo e p|ab, allora p|a oppure p|b.

## Lezione 10 — Buon Ordinamento, Induzione, Divisione Euclidea, Equivalenza, Ordine

Proprietà Riflessiva :: ∀x ∈ A, xRx
<!--SR:!2026-02-25,2,248-->
Proprietà Antiriflessiva :: ∀x ∈ A, ¬(xRx)
Proprietà Simmetrica :: xRy ⇒ yRx
Proprietà Asimmetrica :: xRy ⇒ ¬(yRx); implica antiriflessività.
Proprietà Antisimmetrica :: (xRy ∧ yRx) ⇒ x = y
Proprietà Transitiva :: (xRy ∧ yRz) ⇒ xRz
Insieme Parzialmente Ordinato (POSet) :: (S, ≤) dove ≤ è riflessiva, antisimmetrica, transitiva.
Insieme Totalmente Ordinato :: Ordine parziale con confrontabilità: ∀a, b ∈ S ⟹ a ≤ b ∨ b ≤ a.
Ben Ordinato :: (S, ≤) è ben ordinato se ogni sottoinsieme non vuoto ammette un **minimo**. Ben ordinato ⟹ totalmente ordinato. Esempio: (ℕ, ≤).
Principio di Induzione (Forma I) :: Se P(n̄) è vera e ∀n ≥ n̄ : P(n) ⇒ P(n+1), allora P(n) è vera ∀n ≥ n̄.
Principio di Induzione (Forma II — Forte) :: Se P(n̄) è vera e ∀n > n̄ : (∀i : n̄ ≤ i < n ⇒ P(i)) ⇒ P(n), allora P(n) è vera ∀n ≥ n̄.
Teorema della Divisione Euclidea :: ∀m, n ∈ ℤ, n ≠ 0, ∃!q, r ∈ ℤ : m = n·q + r, 0 ≤ r < |n|.
Identità di Bézout :: MCD(a, b) = a·x + b·y per opportuni x, y ∈ ℤ. Corollario: a, b coprimi ⟺ ∃x,y : ax + by = 1.
Relazione d'Equivalenza :: Una relazione binaria R su A è di equivalenza se è: riflessiva, simmetrica, transitiva.
<!--SR:!2026-02-26,3,250-->
Ordine (Parziale) :: Una relazione su A è d'ordine se è: riflessiva, antisimmetrica, transitiva. È totale se ∀x,y : xRy ∨ yRx.

## Lezione 11 — Algoritmo di Euclide, FTA, Classi di Equivalenza

Algoritmo di Euclide :: Calcola MCD(a,b) tramite divisioni successive: MCD(a,b) = MCD(b,r), finché r = 0. L'ultimo resto non nullo è il MCD.
Algoritmo Esteso di Euclide :: Risalendo le divisioni si trovano i coefficienti di Bézout x, y tali che ax + by = MCD(a,b).
Teorema Fondamentale dell'Aritmetica (FTA) :: Ogni intero n ≥ 2 si scrive in modo **unico** (a meno dell'ordine) come prodotto di numeri primi.
Definizione di Grafo :: Una relazione su A è un grafo se è: antiriflessiva e simmetrica.
Classe di Equivalenza :: aR = {x ∈ S | x R a}. Proprietà: non vuota, due classi sono uguali o disgiunte, la loro unione è S.
Insieme Quoziente :: S/R = {aR | a ∈ S} — l'insieme di tutte le classi di equivalenza disgiunte.

## Lezione 12 — Equivalenza ↔ Partizioni, Congruenza, Zₘ

Teorema Fondamentale sulle Relazioni di Equivalenza :: Esiste una biiezione tra: (1) relazioni di equivalenza su S; (2) partizioni di S. Se R è equivalenza → S/R è partizione. Se F è partizione → xRy ⟺ ∃A ∈ F : x,y ∈ A è equivalenza.
Relazione di Equivalenza Indotta da Funzione :: xRf y ⟺ f(x) = f(y). Le classi sono le **fibre** di f: aRf = f⁻¹({f(a)}).
Fattorizzazione (Applicazione Quoziente) :: Data f : S → T e Rf, l'applicazione quoziente f̄ : S/Rf → T è ben definita e iniettiva.
Congruenza (Compatibilità) :: R è una congruenza rispetto a ∗ se: ∀a,b,c,d ∈ S : (aRc ∧ bRd) ⇒ (a∗b)R(c∗d).
Operazione Quoziente :: Se R è congruenza su (S,∗), si definisce aR ∗R bR = (a∗b)R. La struttura quoziente eredita le proprietà algebriche.
Congruenza Modulo m :: a ≡ b (mod m) ⟺ m | (a − b). Equivalentemente: a e b hanno lo stesso resto nella divisione per m.
Anello Zₘ :: L'insieme quoziente Zₘ = {0̄, 1̄, …, m−1̄} con ā + b̄ = (a+b)̄ e ā·b̄ = (ab)̄ è un anello commutativo unitario.

## Lezione 13 — Zₘ Campo, Invertibili, Divisori Zero, Nilpotenti, Eq. Congruenziali

Compatibilità della Congruenza con + e · :: Se a ≡ c e b ≡ d (mod m), allora a+b ≡ c+d (mod m) e a·b ≡ c·d (mod m).
Zₘ è un Campo :: (Zₘ, +, ·) è un **campo** se e solo se m è un numero **primo**.
Caratteristica di Zₘ :: char(Zₘ) = m.
Invertibili in Zₘ :: āₘ è invertibile in Zₘ ⟺ MCD(a, m) = 1.
<!--SR:!2026-02-26,3,250-->
Divisori dello Zero in Zₘ :: āₘ ≠ 0̄ₘ è divisore dello zero in Zₘ ⟺ MCD(a, m) > 1.
Dicotomia in Zₘ :: In Zₘ, ogni a ≠ 0 è **o invertibile o divisore dello zero**.
Nilpotenti in Zₘ :: Sia $m = p₁^α₁⋯pₜ^αₜ$.  Allora āₘ è nilpotente ⟺ ogni divisore primo di m divide anche a. Equivalentemente: rad(m) | a.
<!--SR:!2026-02-25,1,230-->
Radicale di m :: rad(m) = prodotto dei fattori primi distinti di m. Es: rad(12) = rad(2²·3) = 2·3 = 6.
Numero di Nilpotenti in Zₘ :: |{ā ∈ Zₘ | ā nilpotente}| = m / rad(m) (incluso 0̄).
Teorema di Risolubilità (Eq. Congruenziali) :: ax ≡ b (mod m) ha soluzione ⟺ d | b, dove d = MCD(a,m). Se ha soluzione, ci sono esattamente **d soluzioni distinte** mod m. Se d = 1, la soluzione unica è x ≡ a⁻¹·b (mod m).

## Lezione 14 — Idempotenti, Criteri di Divisibilità

Idempotente in Zₘ :: āₘ è idempotente se a² ≡ a (mod m), cioè m | a(a−1). Sempre idempotenti: 0 e 1.
Numero di Idempotenti in Zₘ :: Se m = p₁^α₁⋯pₖ^αₖ, il numero di idempotenti è 2ᵏ, dove k è il numero di fattori primi distinti di m.
Formula Generale Criteri di Divisibilità :: Sia n = cₖ·10ᵏ + ⋯ + c₁·10 + c₀. Allora n ≡ Σ cᵢ·(10ⁱ mod m) (mod m).
Criterio per 2, 5, 10 :: Dipende dall'ultima cifra (10 ≡ 0).
Criterio per 4, 25, 100 :: Dipende dalle ultime due cifre (100 ≡ 0).
<!--SR:!2026-02-26,2,243-->
Criterio per 3 e 9 :: Dipende dalla somma delle cifre (10 ≡ 1).
Criterio per 11 :: Dipende dalla somma a segni alterni (10 ≡ −1).

## Lezione 15 — Dominio, Anello Prodotto, Caratteristica Prodotto

Zₙ Dominio d'Integrità :: Zₙ è un dominio d'integrità ⟺ n è primo ⟺ Zₙ è un campo.
Anello Prodotto — Definizione :: R × S = {(r,s) | r ∈ R, s ∈ S} con operazioni componente per componente. Zero: (0_R, 0_S). Unità: (1_R, 1_S).
Invertibili nell'Anello Prodotto :: (r,s) ∈ U(R×S) ⟺ r ∈ U(R) e s ∈ U(S).
Divisori dello Zero nell'Anello Prodotto :: Sempre presenti anche se R, S sono domini: (1_R, 0_S)·(0_R, 1_S) = (0_R, 0_S).
Caratteristica dell'Anello Prodotto :: char(R × S) = mcm(char(R), char(S)).
Teorema Cinese dei Resti (TCR) :: Zₘₙ ≅ Zₘ × Zₙ ⟺ MCD(m,n) = 1. Isomorfismo: φ(aₘₙ) = (aₘ, aₙ).

## Lezione 16 — Equazioni Diofantee, φ(n), Fermat-Eulero, Combinatoria

Equazione Diofantea Lineare :: ax + by = c con a,b,c ∈ ℤ, soluzioni x,y ∈ ℤ. Ha soluzione ⟺ MCD(a,b)|c.
Funzione Totiente di Eulero :: φ(n) = |U(Zₙ)| = |{k ∈ {0,…,n−1} | MCD(k,n) = 1}|.
<!--SR:!2026-02-26,3,250-->
Proprietà di φ (n)
?
 φ(p) = p−1 (p primo); 
φ(pᵏ) = pᵏ⁻¹(p−1); 
φ(ab) = φ(a)φ(b) se MCD(a,b) = 1.

...
<!--SR:!2026-02-25,1,210-->
Teorema di Fermat-Eulero :: Se MCD(a,n) = 1, allora: a^φ(n) ≡ 1 (mod n).
Piccolo Teorema di Fermat :: Se p è primo e p∤a: aᵖ⁻¹ ≡ 1 (mod p).
Fattoriale :: n! = n·(n−1)·…·2·1 per n ≥ 1; 0! = 1.
Coefficiente Binomiale :: C(n,k) = n! / (k!(n−k)!) per 0 ≤ k ≤ n. Rappresenta il numero di modi di scegliere k elementi da n senza ordine e senza ripetizioni.
Identità di Pascal :: C(n,k) + C(n,k−1) = C(n+1,k).
<!--SR:!2026-02-26,2,230-->
Somma dei Coefficienti Binomiali :: Σₖ₌₀ⁿ C(n,k) = 2ⁿ.
Binomio di Newton :: (a+b)ⁿ = Σₖ₌₀ⁿ C(n,k) aⁿ⁻ᵏ bᵏ.
Numero di Applicazioni Iniettive :: Il numero di f iniettive da S a T con |S|=n, |T|=m, n≤m: m!/(m−n)!.

## Lezione 17 — Relazioni d'Ordine, Hasse, Estremi

Relazione d'Ordine Largo (Parziale) :: ≤ è d'ordine se: riflessiva, antisimmetrica, transitiva.
Ordine Stretto :: < è d'ordine stretto se: antiriflessiva, transitiva. Implica automaticamente l'asimmetria.
Relazione tra Ordine Largo e Stretto :: x < y ⟺ (x ≤ y ∧ x ≠ y) ; x ≤ y ⟺ (x < y ∨ x = y).
<!--SR:!2026-02-26,3,250-->
Ordine Totale (o Lineare) :: Ordine ≤ su S è **totale** se ogni coppia è confrontabile: ∀x,y ∈ S : x ≤ y ∨ y ≤ x.
Minimo :: a è minimo se a ≤ x per ogni x ∈ S. Se esiste, è **unico**.
Massimo :: a è massimo se x ≤ a per ogni x ∈ S. Se esiste, è **unico**.
Minimale :: a è minimale se non esiste x ∈ S con x < a. Equivalentemente: ∀x ∈ S, (x ≤ a ⇒ x = a).
<!--SR:!2026-02-27,3,250-->
Massimale :: a è massimale se non esiste x ∈ S con a < x. Equivalentemente: ∀x ∈ S, (a ≤ x ⇒ x = a).
Relazione Minimo–Minimale :: Minimo ⟹ unico elemento minimale. In un ordine totale: minimale ⟺ minimo.
Teorema — Poset Finiti :: Ogni insieme finito non vuoto parzialmente ordinato possiede almeno un minimale e almeno un massimale.
Copertura (Successore Immediato) :: b **copre** a se: a < b ∧ ¬∃c ∈ S : a < c < b.
Che cos'è il Diagramma di Hasse?
?
Rappresentazione grafica di un poset finito (S, ≤):
- **Vertici:** elementi di S
- **Archi:** solo relazioni di **copertura** (successore immediato)
- **Disposizione:** elementi maggiori più in alto
- No loop, no archi transitivi, no frecce
<!--SR:!2026-02-26,2,243-->
...
Minorante :: a ∈ S è un minorante di X se a ≤ x per ogni x ∈ X.
Maggiorante :: a ∈ S è un maggiorante di X se x ≤ a per ogni x ∈ X.
Infimo :: inf(X) = max(minoranti di X) — il più grande tra i minoranti di X (se esiste).
Supremo (Sup(X)) :: sup(X) = min(maggioranti di X) — il più piccolo tra i maggioranti di X (se esiste).
<!--SR:!2026-02-26,3,250-->
Infimo e MCD :: In (ℕ*, |): inf{a,b} = MCD(a,b).
Supremo e mcm :: In (ℕ*, |): sup{a,b} = mcm(a,b).
<!--SR:!2026-02-26,2,243-->

## Lezione 19 — Divisibilità come Ordine, Ordine Indotto

Divisibilità su ℕ* come Ordine :: La relazione "|" su ℕ* è un ordine parziale largo (riflessiva, antisimmetrica, transitiva). Non è totale.
Divisibilità su ℤ — Non è Ordine :: La relazione "|" su ℤ non è d'ordine perché non è antisimmetrica. Controesempio: 2|(−2) e (−2)|2 ma 2 ≠ −2.
Ordine Indotto da Funzione :: Sia f : S → T e (T, ≤_T) ordinato. Su S: a ≤_f b ⟺ (a = b) ∨ (f(a) <_T f(b)). Questa è una relazione d'ordine su S.

## Lezione 20 — Reticoli

Reticolo (Definizione tramite Ordine) :: Un poset (L, ≤) è un **reticolo** se per ogni coppia a,b ∈ L esistono: inf{a,b} = a ∧ b (meet) e sup{a,b} = a ∨ b (join).
<!--SR:!2026-02-26,3,250-->
Reticolo (Definizione Algebrica) :: Una struttura (L, ∧, ∨) è un reticolo se ∧ e ∨ soddisfano: associatività, commutatività, assorbimento (a ∧ (a ∨ b) = a; a ∨ (a ∧ b) = a).
<!--SR:!2026-02-25,1,223-->
Idempotenza nel Reticolo :: Dalle leggi di assorbimento: a ∧ a = a e a ∨ a = a.
<!--SR:!2026-02-25,1,223-->
Equivalenza Ordine ↔ Algebrica :: Le due definizioni di reticolo sono equivalenti. La relazione d'ordine si recupera da: a ≤ b ⟺ a ∧ b = a ⟺ a ∨ b = b.
L'Insieme delle Parti è un Reticolo :: (P(S), ⊆) è un reticolo con A ∧ B = A ∩ B e A ∨ B = A ∪ B.
Catena :: Un sottoinsieme C ⊆ S di un insieme ordinato (S, ≤) è una catena se è totalmente ordinato: ∀x,y ∈ C : x ≤ y ∨ y ≤ x.
Catena Massimale :: Una catena C in (S, ≤) è massimale se non può essere estesa: non esiste s ∈ S \ C tale che C ∪ {s} sia ancora una catena.

## Lezione 21 — Reticoli Limitati, Sottoreticoli, Isomorfismi, Complementati, Prodotto

Reticolo Limitato :: Un reticolo (L, ≤) è **limitato** se possiede un elemento minimo 0_L e un elemento massimo 1_L.
Teorema — Reticoli Finiti Sono Limitati :: Ogni reticolo **finito** è limitato.
Corollario — Totalmente Ordinato è Reticolo :: Se (S, ≤) è totalmente ordinato, è un reticolo con a ∧ b = min{a,b} e a ∨ b = max{a,b}.
Sottoreticolo :: A ⊆ L è un sottoreticolo se è chiuso per ∧ e ∨: ∀x,y ∈ A : x ∧ y ∈ A ∧ x ∨ y ∈ A.
Isomorfismo di Reticoli :: f : L → M biettiva è un isomorfismo se preserva l'ordine: a ≤_L b ⟺ f(a) ≤_M f(b). Equivalentemente: f(a∧b) = f(a)∧f(b) e f(a∨b) = f(a)∨f(b).
Complemento in un Reticolo Limitato :: a ∈ L ha un **complemento** ā se: a ∧ ā = 0_L e a ∨ ā = 1_L.
Reticolo Complementato :: Un reticolo limitato è complementato se ogni elemento possiede almeno un complemento.
Reticolo Prodotto :: Dati (L₁, ≤₁) e (L₂, ≤₂): L₁ × L₂ è un reticolo con ordine e operazioni componente per componente. Se limitati, con (0₁,0₂) e (1₁,1₂).
Reticolo dei Divisori (Dₙ, |) :: Infimo: a ∧ b = MCD(a,b); Supremo: a ∨ b = mcm(a,b); Minimo: 1; Massimo: n.

## Lezione 22 — Dualità, Distributivi, Booleani, Algebre di Boole, Anelli Booleani

Principio di Dualità :: Se un enunciato vale per tutti i reticoli, vale anche il suo **duale**, ottenuto scambiando: ≤ ↔ ≥, ∧ ↔ ∨, 0_L ↔ 1_L.
Reticolo Distributivo :: Un reticolo è distributivo se: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c). Per dualità, equivale anche a: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c).
Teorema — Caratterizzazione Distributività :: Un reticolo è distributivo ⟺ **non** contiene sottoreticoli isomorfi a M₃ (diamante) o N₅ (pentagono).
Reticolo Diamante M₃ :: Reticolo con 5 elementi {0,a,b,c,1} dove a,b,c sono mutuamente non confrontabili e 0 < a,b,c < 1. Non è distributivo (ma è modulare).
Reticolo Pentagonale N₅ :: Reticolo con 5 elementi {0,a,b,c,1} dove 0 < a < b < 1 e 0 < c < 1 con c non confrontabile con a e b. Non è distributivo né modulare.
<!--SR:!2026-02-26,2,243-->
Unicità del Complemento in Reticoli Distributivi :: In un reticolo **distributivo e limitato**, se un elemento ha un complemento, questo è **unico**.
Reticolo Booleano :: Un reticolo è **booleano** se è distributivo e complementato. Esempio: (P(S), ⊆) con complemento Aᶜ = S \ A.
Teorema di Rappresentazione dei Reticoli Booleani :: Ogni reticolo booleano **finito** è isomorfo a (P(S), ⊆) per un opportuno insieme finito S. Se |L| = 2ⁿ, L ha n "atomi".
Cos'è un'Algebra di Boole?
?
(A, ∧, ∨, ', 0, 1) è un'algebra di Boole se soddisfa:
1. **Associatività** di ∧ e ∨
2. **Commutatività** di ∧ e ∨
3. **Assorbimento:** a ∧ (a ∨ b) = a; a ∨ (a ∧ b) = a
4. **Distributività:** a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
5. **Elementi neutri:** a ∧ 1 = a; a ∨ 0 = a
6. **Complemento:** a ∧ a' = 0; a ∨ a' = 1
...

Teorema di Stone :: Ogni algebra di Boole finita è isomorfa a (P(S), ∩, ∪, ᶜ, ∅, S) per un opportuno S.
Anello Booleano :: Un anello (A, +, ·) è **booleano** se a² = a per ogni a ∈ A. Proprietà: char(A) = 2, (A,·) è commutativo. Esempio: (P(S), △, ∩).
Come si passa da Reticolo Booleano ad Anello Booleano?
?
Dato un reticolo booleano (L, ∧, ∨, ', 0, 1), si definisce (L, +, ·):
- **Prodotto (meet):** a · b = a ∧ b
- **Somma (diff. simmetrica):** a + b = (a ∧ b') ∨ (b ∧ a')
- **Relazione d'ordine recuperata:** a ≤ b ⟺ a · b = a
<!--SR:!2026-02-25,1,230-->
...




#flashcards/Algebra/Dimostrazioni
# Dimostrazioni da sapere

Teorema Fondamentale dell'Aritmetica (TFA)
?
> [!important] **Teorema Fondamentale dell'Aritmetica (TFA)**
>
> **Enunciato:**
> Ogni intero $n \geq 2$ si scrive in modo **unico** (a meno dell'ordine) come prodotto di numeri primi:
> $$n = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdots p_k^{\alpha_k}$$
> dove i $p_i$ sono primi distinti e gli $\alpha_i$ sono interi positivi.
>
>> [!attention] **Dimostrazione (Idea Generale)**
>> 
>> ### Parte 1: Esistenza della fattorizzazione
>>
>> **Per induzione su $n$:**
>>
>> **Base:** $n = 2$ è primo. ✓
>>
>> **Ipotesi induttiva:** Per ogni $m < n$, la fattorizzazione esiste.
>>
>> **Tesi:** La fattorizzazione esiste per $n$.
>>
>> **Dimostrazione:**
>> - Se $n$ è primo, banale.
>> - Altrimenti, per il **Lemma di Euclide**, esiste un primo $p \mid n$ con $n = p \cdot m$ dove $m < n$.
>> - Per ipotesi induttiva, $m$ ha una fattorizzazione.
>> - Dunque $n = p \cdot m$ ha una fattorizzazione. ✓
>>
>> ### Parte 2: Unicità della fattorizzazione
>>
>> Supponiamo $n$ abbia due rappresentazioni:
>> $$n = p_1^{a_1} \cdots p_k^{a_k} = q_1^{b_1} \cdots q_r^{b_r}$$
>>
>> dove i $p_i$ e i $q_j$ sono primi distinti.
>>
>> **Caso 1:** Un primo $p_i$ compare nella prima rappresentazione ma non nella seconda.
>>
>> Allora $p_i \mid n = q_1^{b_1} \cdots q_r^{b_r}$.
>>
>> Per il **Lemma di Euclide**, $p_i$ divide uno dei $q_j$. Ma i $q_j$ sono primi, quindi $p_i = q_j$, contraddizione. ✗
>>
>> **Caso 2:** Le rappresentazioni hanno gli stessi primi, ma esponenti diversi.
>>
>> Supponiamo $a_1 > b_1$ (senza perdita di generalità). Dividendo per $p_1^{b_1}$:
>> $$p_1^{a_1 - b_1} \cdot p_2^{a_2} \cdots p_k^{a_k} = q_2^{b_2} \cdots q_r^{b_r}$$
>>
>> Allora $p_1 \mid q_2^{b_2} \cdots q_r^{b_r}$.
>>
>> Per il **Lemma di Euclide**, $p_1$ divide uno dei $q_j$ (con $j \geq 2$). Ma i $q_j$ sono primi distinti dai $p_i$, contraddizione. ✗
>>
>> Quindi gli esponenti devono essere uguali: $a_i = b_i$ per ogni $i$. ✓

...

Teorema Divisione euclidea
?
> [!important] **Teorema della Divisione Euclidea**
>
> **Enunciato:**
> $\forall\, m, n \in \mathbb{Z},\; n \neq 0,\; \exists!\, q, r \in \mathbb{Z}:$
> $$m = n \cdot q + r, \qquad 0 \leq r < |n|$$
>
>> [!attention] **Dimostrazione**
>>
>> **Esistenza** (per induzione forte su $m$):
>> - *Base:* Se $0 \leq m < |n|$, basta prendere $q = 0$ e $r = m$.
>> - *Passo:* Se $m \geq |n|$, poniamo $\bar{m} = m - |n| \geq 0$. Poiché $\bar{m} < m$, per ipotesi induttiva $\bar{m} = |n| \cdot \bar{q} + \bar{r}$ con $0 \leq \bar{r} < |n|$.
>>   Allora $m = \bar{m} + |n| = |n|(\bar{q} + 1) + \bar{r}$, con $q = \bar{q} + 1$ e $r = \bar{r}$.
>>
>> **Unicità:** Supponiamo $m = nq_1 + r_1 = nq_2 + r_2$ con $0 \leq r_1, r_2 < |n|$.
>> Sottraendo: $n(q_1 - q_2) = r_2 - r_1$.
>> Poiché $|r_2 - r_1| < |n|$, l'unico multiplo di $n$ in quell'intervallo è $0$.
>> Quindi $r_1 = r_2$ e $q_1 = q_2$. ✓

...

Teorema di Bézout
?
> [!important] **Identità di Bézout**
>
> **Enunciato:**
> Per ogni coppia di interi $a, b$, esistono interi $x, y$ tali che:
> $$\mathrm{MCD}(a, b) = a \cdot x + b \cdot y$$
>
>> [!attention] **Dimostrazione**
>>
>> Sia $S = \{as + bt \mid s, t \in \mathbb{Z}, \, as + bt > 0\}$.
>>
>> **1) $S \neq \varnothing$:**
>> - Se $a \neq 0$, scegliendo $s = \pm 1$ si ha $|a| = a \cdot (\pm 1) + b \cdot 0 \in S$
>> - Analogamente se $b \neq 0$
>>
>> **2) Esistenza del minimo:**
>> Per il **principio del buon ordinamento**, $S$ ammette un minimo $d$. Per definizione di $S$, esistono $x, y \in \mathbb{Z}$ tali che:
>> $$d = ax + by$$
>>
>> **3) $d \mid a$:**
>> Dividiamo $a = dq + r$ con $0 \leq r < d$. Allora:
>> $$r = a - dq = a - (ax + by)q = a(1 - xq) + b(-yq)$$
>> 
>> Poiché $1 - xq$ e $-yq$ sono interi, $r$ è una combinazione lineare di $a$ e $b$.
>> 
>> Se $r > 0$, allora $r \in S$ con $r < d$, contro la minimalità di $d$. Dunque $r = 0$, quindi $d \mid a$.
>>
>> **4) $d \mid b$:** Analogamente.
>>
>> **5) $d = \gcd(a, b)$:**
>> Se $c \mid a$ e $c \mid b$, allora $c \mid (ax + by) = d$, dunque $d$ è il massimo comune divisore di $a$ e $b$. ✓

...

Applicazione Quoziente
?
>[!important] Fattorizzazione
> Data $f: S \to T$ e la relazione $R_f$, l'**applicazione quoziente** è:
> $$\bar{f}: S/R_f \to T, \qquad \bar{f}([a]) = f(a)$$
> È **ben definita** e **iniettiva**. Vale $f = \bar{f} \circ \pi$ (dove $\pi$ è la proiezione canonica).
>
>> [!attention] Dimostrazione — Fattorizzazione (forse non necessaria)
>> **Ben definita:** Se $[a] = [b]$, allora $a \mathrel{R_f} b$, cioè $f(a) = f(b)$, dunque $\bar{f}([a]) = \bar{f}([b])$.
>>
>> **Iniettiva:** Se $\bar{f}([a]) = \bar{f}([b])$, allora $f(a) = f(b)$, dunque $a \mathrel{R_f} b$, cioè $[a] = [b]$. $\square$

...

Teorema fondamentale sulle relazioni d'equivalenza (Equivalenza $\iff$ Partizione)
?
> [!important] **Teorema Fondamentale sulle Relazioni di Equivalenza (Versione Ristretta)**
>
> **Enunciato:**
> Sia $R$ una relazione di equivalenza su un insieme non vuoto $S$. Allora l'insieme quoziente $S/R$ è una **partizione** di $S$. 
> 
> Viceversa, ogni partizione di $S$ definisce una relazione di equivalenza.
>
>> [!attention] **Dimostrazione**
>>
>> ### Verso 1: Equivalenza $\Rightarrow$ Partizione
>>
>> Sia $R$ una relazione di equivalenza. Definiamo $\mathcal{P} = S/R = \{[a]_R \mid a \in S\}$.
>>
>> **Proprietà 1: Non vuotezza**
>> Ogni classe $[a]_R$ contiene almeno $a$ (per riflessività). ✓
>>
>> **Proprietà 2: Disgiunzione o coincidenza**
>> Supponiamo $[a]_R \cap [b]_R \neq \varnothing$. Allora esiste $c$ con $c \in [a]_R$ e $c \in [b]_R$.
>> - Da $c \in [a]_R$: $c R a$
>> - Da $c \in [b]_R$: $c R b$
>> - Per simmetria: $a R c$ e $c R b$
>> - Per transitività: $a R b$
>>
>> Quindi $[a]_R = [b]_R$ (perché se $x \in [a]_R$, allora $x R a$ e $a R b$, dunque $x R b$, cioè $x \in [b]_R$).
>> ✓
>>
>> **Proprietà 3: Unione = $S$**
>> Ovvio: ogni $a \in S$ appartiene a $[a]_R$. ✓
>>
>> Quindi $\mathcal{P}$ è una partizione.
>>
>> ### Verso 2: Partizione $\Rightarrow$ Equivalenza
>>
>> Sia $\mathcal{P} = \{A_i \mid i \in I\}$ una partizione di $S$. Definiamo:
>> $$a R b \Leftrightarrow \exists i \in I : a, b \in A_i$$
>>
>> **Riflessiva:** $\forall a \in S$, esiste $i$ con $a \in A_i$ (per copertura). Quindi $a R a$. ✓
>>
>> **Simmetrica:** Se $a R b$, allora $\exists i$ con $a, b \in A_i$. Dunque $b, a \in A_i$, cioè $b R a$. ✓
>>
>> **Transitiva:** Se $a R b$ e $b R c$, allora:
>> - $\exists i$ con $a, b \in A_i$
>> - $\exists j$ con $b, c \in A_j$
>>
>> Poiché $b \in A_i \cap A_j$ e gli elementi di $\mathcal{P}$ sono disgiunti, $A_i = A_j$.
>> Quindi $a, c \in A_i$, cioè $a R c$. ✓
>>
>> Quindi $R$ è una relazione di equivalenza. ✓

...
