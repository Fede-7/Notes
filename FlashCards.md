#flashcards/Algebra
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
Quantificatore Universale :: ∀x P(x): «per ogni x, vale P(x)».
Quantificatore Esistenziale :: ∃x P(x): «esiste almeno un x tale che P(x)».
Quantificatore Esistenziale Unico :: ∃!x P(x) ⟺ ∃x P(x) ∧ ∀x∀y(P(x) ∧ P(y) ⇒ x = y)
Variabile Vincolata :: Una variabile che compare nel raggio d'azione di un quantificatore. Altrimenti è **libera**. Una formula senza variabili libere è detta **chiusa**.
Insieme :: Collezione di oggetti distinti, detti **elementi**. Si scrive a ∈ A se a appartiene ad A.
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

## Lezione 2 — Quantificatori, Immagini, Iniettività, Partizioni

Negazione dei Quantificatori :: ¬(∀x P(x)) ⟺ ∃x(¬P(x)) ; ¬(∃x P(x)) ⟺ ∀x(¬P(x))
Ordine dei Quantificatori :: ∃y∀x φ(x,y) ⟹ ∀x∃y φ(x,y) — il viceversa non vale in generale.
Immagine di un Sottoinsieme :: f→(X) = {f(x) | x ∈ X} ⊆ B — insieme degli elementi del codominio raggiunti da X.
Controimmagine (Preimmagine) :: f←(Y) = {x ∈ A | f(x) ∈ Y} ⊆ A — insieme degli elementi del dominio le cui immagini cadono in Y.
Iniettività :: f : A → B è iniettiva se: ∀x₁, x₂ ∈ A : f(x₁) = f(x₂) ⟹ x₁ = x₂
Caratterizzazione Iniettività tramite Controimmagine :: f è iniettiva ⟺ ∀b ∈ B, |f⁻¹({b})| ≤ 1
Partizione :: Una famiglia F ⊆ P(S) è una partizione di S se: (1) ∀X ∈ F, X ≠ ∅; (2) pezzi disgiunti; (3) ⋃F = S.

## Lezione 3 — Suriettività, Funzione Caratteristica, Restrizione, Identità

Suriettività :: f : A → B è suriettiva se: ∀b ∈ B, ∃a ∈ A : f(a) = b
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
Proprietà della Composizione :: Associativa: (h ∘ g) ∘ f = h ∘ (g ∘ f). Non commutativa: g ∘ f ≠ f ∘ g.
Corrispondenza Complementare :: Data φ ⊆ A × B: φ' = (A × B) \ φ.
Corrispondenza Inversa :: Data φ ⊆ A × B: φ⁻¹ = {(b, a) ∈ B × A : (a, b) ∈ φ}.
Funzione Invertibile :: f : A → B è invertibile ⟺ ∃f⁻¹ : B → A t.c. f⁻¹ ∘ f = id_A e f ∘ f⁻¹ = id_B.
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
Anello Booleano :: Anello con a · a = a per ogni a. Esempio: (P(S), △, ∩).
Caratteristica di un Anello Unitario :: char(A) = min{m > 0 | 1_A + ⋯ + 1_A (m volte) = 0_A}. Se non esiste, char(A) = 0.
Cancellabilità :: a è cancellabile a sinistra se a·b = a·c ⇒ b = c. A destra se b·a = c·a ⇒ b = c. Invertibile ⟹ Cancellabile.
Divisore dello Zero :: a ≠ 0_A è divisore dello zero se ∃b ≠ 0_A : a · b = 0_A. Equivalentemente: a ≠ 0 è divisore dello zero ⟺ a non è cancellabile.

## Lezione 8 — Omomorfismo, Dominio, Campo, Spazio Vettoriale, Sn

Omomorfismo :: f : (S, ∗) → (T, ·) è un omomorfismo se: f(a ∗ b) = f(a) · f(b) ∀a, b ∈ S.
Dominio d'Integrità :: Un anello (A, +, ·) è un dominio d'integrità se: è commutativo, è unitario (con 1_A ≠ 0_A), è privo di divisori dello zero. Esempi: ℤ, ℚ, ℝ, ℂ.
Corpo :: Un anello (K, +, ·) è un corpo se: è unitario (con 1_K ≠ 0_K) e (K*, ·) è un gruppo, dove K* = K \ {0_K}.
Campo :: Un campo è un **corpo commutativo**. Esempi: ℚ, ℝ, ℂ, ℤ_p (con p primo).
Teorema di Wedderburn :: Ogni corpo finito è anche un **campo**.
Spazio Vettoriale :: Sia K un campo. Un K-spazio vettoriale (V, +, ·_ext) dove (V,+) è gruppo abeliano, con moltiplicazione esterna K×V→V soddisfacente associatività mista, distributività e elemento neutro 1_K.
Gruppo Simmetrico Sₙ :: B(S) = insieme delle permutazioni di S. (B(S), ∘) è un gruppo detto Sₙ. |Sₙ| = n!. Non abeliano per n ≥ 3.

## Lezione 9 — Cayley, Nilpotenti, Divisibilità, MCD, mcm, Primi

Notazione Ciclica (Permutazioni) :: Un ciclo (c₁c₂⋯cₖ): σ(cᵢ) = cᵢ₊₁, σ(cₖ) = c₁, σ(x) = x altrimenti.
Teorema di Scomposizione Canonica :: Ogni permutazione σ ∈ Sₙ diversa dall'identità si scrive come prodotto di cicli disgiunti. La scomposizione è unica a meno dell'ordine.
Inversa di un Ciclo :: (c₁c₂⋯cₖ)⁻¹ = (c₁cₖcₖ₋₁⋯c₂)
Proprietà visibili dalle Tavole di Cayley :: Commutatività ⟺ tabella simmetrica; Cancellabilità ⟺ no ripetizioni in righe/colonne; Elemento Neutro ⟺ riga/colonna uguale agli indici; Simmetrizzabili ⟺ ∗ restituisce l'elemento neutro.
Nilpotente :: a ∈ A è nilpotente se ∃n ≥ 1 : aⁿ = 0_A. Nilpotente non nullo ⟹ Divisore dello zero.
Divisibilità :: b | a ⟺ ∃c : a = b · c. div(a): insieme dei divisori di a. mult(b): insieme dei multipli di b.
Associati :: Sia x, y ∈ A anello commutativo unitario. x ∼ y ⟺ ∃u ∈ U(A) : x = u · y. È una relazione di equivalenza.
Divisori Banali e Propri :: I divisori banali di a sono gli invertibili U(A) e gli associati ad a stesso. Un divisore proprio non è né banale né invertibile.
Massimo Comun Divisore :: e = MCD(a, b) se: (1) e|a e e|b; (2) ∀x : (x|a ∧ x|b) ⇒ x|e.
Minimo Comune Multiplo :: m = mcm(a, b) se: (1) a|m e b|m; (2) ∀x : (a|x ∧ b|x) ⇒ m|x.
Numero Primo :: p è primo se p ∉ U(ℤ) e div(p) = {1, −1, p, −p}.
Lemma di Euclide :: Se p è primo e p|ab, allora p|a oppure p|b.

## Lezione 10 — Buon Ordinamento, Induzione, Divisione Euclidea, Equivalenza, Ordine

Proprietà Riflessiva :: ∀x ∈ A, xRx
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
Divisori dello Zero in Zₘ :: āₘ ≠ 0̄ₘ è divisore dello zero in Zₘ ⟺ MCD(a, m) > 1.
Dicotomia in Zₘ :: In Zₘ, ogni a ≠ 0 è **o invertibile o divisore dello zero**.
Nilpotenti in Zₘ :: Sia m = p₁^α₁⋯pₜ^αₜ. Allora āₘ è nilpotente ⟺ ogni divisore primo di m divide anche a.
Teorema di Risolubilità (Eq. Congruenziali) :: ax ≡ b (mod m) ha soluzione ⟺ d|b, dove d = MCD(a,m). Se ha soluzione, ci sono esattamente d soluzioni distinte mod m.

## Lezione 14 — Idempotenti, Criteri di Divisibilità

Idempotente in Zₘ :: āₘ è idempotente se a² ≡ a (mod m), cioè m | a(a−1). Sempre idempotenti: 0 e 1.
Formula Generale Criteri di Divisibilità :: Sia n = cₖ·10ᵏ + ⋯ + c₁·10 + c₀. Allora n ≡ Σ cᵢ·(10ⁱ mod m) (mod m).
Criterio per 2, 5, 10 :: Dipende dall'ultima cifra (10 ≡ 0).
Criterio per 4, 25, 100 :: Dipende dalle ultime due cifre (100 ≡ 0).
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
Proprietà di φ :: φ(p) = p−1 (p primo); φ(pᵏ) = pᵏ⁻¹(p−1); φ(ab) = φ(a)φ(b) se MCD(a,b) = 1.
Teorema di Fermat-Eulero :: Se MCD(a,n) = 1, allora: a^φ(n) ≡ 1 (mod n).
Piccolo Teorema di Fermat :: Se p è primo e p∤a: aᵖ⁻¹ ≡ 1 (mod p).
Fattoriale :: n! = n·(n−1)·…·2·1 per n ≥ 1; 0! = 1.
Coefficiente Binomiale :: C(n,k) = n! / (k!(n−k)!) per 0 ≤ k ≤ n. Rappresenta il numero di modi di scegliere k elementi da n senza ordine e senza ripetizioni.
Identità di Pascal :: C(n,k) + C(n,k−1) = C(n+1,k).
Somma dei Coefficienti Binomiali :: Σₖ₌₀ⁿ C(n,k) = 2ⁿ.
Binomio di Newton :: (a+b)ⁿ = Σₖ₌₀ⁿ C(n,k) aⁿ⁻ᵏ bᵏ.
Numero di Applicazioni Iniettive :: Il numero di f iniettive da S a T con |S|=n, |T|=m, n≤m: m!/(m−n)!.

## Lezione 17 — Relazioni d'Ordine, Hasse, Estremi

Relazione d'Ordine Largo (Parziale) :: ≤ è d'ordine se: riflessiva, antisimmetrica, transitiva.
Ordine Stretto :: < è d'ordine stretto se: antiriflessiva, transitiva. Implica automaticamente l'asimmetria.
Relazione tra Ordine Largo e Stretto :: x < y ⟺ (x ≤ y ∧ x ≠ y) ; x ≤ y ⟺ (x < y ∨ x = y).
Ordine Totale (o Lineare) :: Ordine ≤ su S è **totale** se ogni coppia è confrontabile: ∀x,y ∈ S : x ≤ y ∨ y ≤ x.
Minimo :: a è minimo se a ≤ x per ogni x ∈ S. Se esiste, è **unico**.
Massimo :: a è massimo se x ≤ a per ogni x ∈ S. Se esiste, è **unico**.
Minimale :: a è minimale se non esiste x ∈ S con x < a. Equivalentemente: ∀x ∈ S, (x ≤ a ⇒ x = a).
Massimale :: a è massimale se non esiste x ∈ S con a < x. Equivalentemente: ∀x ∈ S, (a ≤ x ⇒ x = a).
Relazione Minimo–Minimale :: Minimo ⟹ unico elemento minimale. In un ordine totale: minimale ⟺ minimo.
Teorema — Poset Finiti :: Ogni insieme finito non vuoto parzialmente ordinato possiede almeno un minimale e almeno un massimale.
Copertura (Successore Immediato) :: b **copre** a se: a < b ∧ ¬∃c ∈ S : a < c < b.
Diagramma di Hasse :: Rappresentazione grafica di un poset finito. Vertici: elementi; Archi: solo relazioni di copertura; elementi maggiori più in alto. No loop, no archi transitivi, no frecce.
Minorante :: a ∈ S è un minorante di X se a ≤ x per ogni x ∈ X.
Maggiorante :: a ∈ S è un maggiorante di X se x ≤ a per ogni x ∈ X.
Infimo :: inf(X) = max(minoranti di X) — il più grande tra i minoranti di X (se esiste).
Supremo :: sup(X) = min(maggioranti di X) — il più piccolo tra i maggioranti di X (se esiste).
Infimo e MCD :: In (ℕ*, |): inf{a,b} = MCD(a,b).
Supremo e mcm :: In (ℕ*, |): sup{a,b} = mcm(a,b).

## Lezione 19 — Divisibilità come Ordine, Ordine Indotto

Divisibilità su ℕ* come Ordine :: La relazione "|" su ℕ* è un ordine parziale largo (riflessiva, antisimmetrica, transitiva). Non è totale.
Divisibilità su ℤ — Non è Ordine :: La relazione "|" su ℤ non è d'ordine perché non è antisimmetrica. Controesempio: 2|(−2) e (−2)|2 ma 2 ≠ −2.
Ordine Indotto da Funzione :: Sia f : S → T e (T, ≤_T) ordinato. Su S: a ≤_f b ⟺ (a = b) ∨ (f(a) <_T f(b)). Questa è una relazione d'ordine su S.

## Lezione 20 — Reticoli

Reticolo (Definizione tramite Ordine) :: Un poset (L, ≤) è un **reticolo** se per ogni coppia a,b ∈ L esistono: inf{a,b} = a ∧ b (meet) e sup{a,b} = a ∨ b (join).
Reticolo (Definizione Algebrica) :: Una struttura (L, ∧, ∨) è un reticolo se ∧ e ∨ soddisfano: associatività, commutatività, assorbimento (a ∧ (a ∨ b) = a; a ∨ (a ∧ b) = a).
Idempotenza nel Reticolo :: Dalle leggi di assorbimento: a ∧ a = a e a ∨ a = a.
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
Unicità del Complemento in Reticoli Distributivi :: In un reticolo **distributivo e limitato**, se un elemento ha un complemento, questo è **unico**.
Reticolo Booleano :: Un reticolo è **booleano** se è distributivo e complementato. Esempio: (P(S), ⊆) con complemento Aᶜ = S \ A.
Teorema di Rappresentazione dei Reticoli Booleani :: Ogni reticolo booleano **finito** è isomorfo a (P(S), ⊆) per un opportuno insieme finito S. Se |L| = 2ⁿ, L ha n "atomi".
Algebra di Boole :: (A, ∧, ∨, ', 0, 1) è un'algebra di Boole se soddisfa: associatività, commutatività, assorbimento, distributività, elementi neutri (a∧1=a, a∨0=a), complemento (a∧a'=0, a∨a'=1).
Teorema di Stone :: Ogni algebra di Boole finita è isomorfa a (P(S), ∩, ∪, ᶜ, ∅, S) per un opportuno S.
Anello Booleano :: Un anello (A, +, ·) è **booleano** se a² = a per ogni a ∈ A. Proprietà: char(A) = 2, (A,·) è commutativo. Esempio: (P(S), △, ∩).
Da Reticolo Booleano ad Anello Booleano :: Dato un reticolo booleano (L, ∧, ∨, ', 0, 1), si costruisce l'anello booleano con: a·b = a∧b (meet); a+b = (a∧b') ∨ (b∧a') (differenza simmetrica). Relazione d'ordine recuperata: a ≤ b ⟺ a·b = a.
