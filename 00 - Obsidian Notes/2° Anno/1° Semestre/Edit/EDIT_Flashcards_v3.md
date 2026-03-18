#flashcards/EDIT

---
## CALCOLABILITÀ

Cos'è un problema calcolabile?
?
Un problema è **calcolabile** se è possibile risolverlo algoritmicamente. Si formalizza con una funzione matematica avente input e output in ℕ, per cui esiste un algoritmo che la calcola.
...

---

Cos'è una funzione totale?
?
Una funzione **totale** è definita per **ogni** input possibile nel suo dominio: per qualsiasi x, esiste sempre un output f(x).
Esempio: la somma x+y è definita per ogni coppia di naturali.

---

Cos'è una funzione parziale?
?
Una funzione **parziale** può non essere definita per alcuni input: esistono x per cui f(x) è indefinita (si scrive f(x)↑).
Esempio: la divisione x/y non è definita per y=0.
Le funzioni totali sono un **sottoinsieme** delle funzioni parziali.

---

Cos'è una funzione parzialmente calcolabile?
?
Una funzione è **parzialmente calcolabile** se esiste un programma S che:
- termina e restituisce f(x) se f(x) è definita
- non termina (va in loop) se f(x) è indefinita
Non è richiesto che il programma termini sempre.

---

Cos'è una funzione totalmente calcolabile?
?
Una funzione è **totalmente calcolabile** se è sia **totale** (definita per ogni input) che **calcolabile** (esiste un programma S che termina sempre e restituisce il risultato corretto).

---

Tesi di Church-Turing
?
"Qualsiasi funzione che si possa determinare tramite qualche procedura algoritmica è **parzialmente calcolabile**."
Identifica il concetto intuitivo di algoritmo con quello formale di funzione parzialmente calcolabile. Non è dimostrabile, è una tesi.

---

Cos'è un predicato?
?
Un **predicato** è una funzione **totale** il cui codominio è {0, 1}. Rappresenta una proprietà che può essere vera (1) o falsa (0).

---

Cos'è una funzione k-aria?
?
Una funzione **k-aria** è una funzione con esattamente **k argomenti**.
- k=0: costante (0-aria)
- k=1: unaria, es. f(x)
- k=2: binaria, es. f(x,y)
Nel corso tutte le funzioni hanno dominio ℕᵏ e codominio ℕ.

---

## LINGUAGGIO S

Quali sono le variabili del linguaggio S?
?
- **Input**: X₁, X₂, ... (fornite dall'utente)
- **Output**: Y (unica, default 0)
- **Temporanee**: Z₁, Z₂, ... (default 0)
Pedice omesso = pedice 1 (es. X = X₁). Non può esserci più di una variabile Y.

---

Quali sono i 4 statement del linguaggio S?
?
1. **Pigra**: `V ← V` (non fa nulla)
2. **Incremento**: `V ← V + 1`
3. **Decremento**: `V ← V − 1` (se V=0, ignorata)
4. **Salto condizionale**: `IF V ≠ 0 GOTO L` (salta a L se V≠0; se L non esiste, il programma termina)

---

Come funzionano le etichette nel linguaggio S?
?
Le etichette (A₁, B₁, C₁, D₁, A₂, ...) indicano linee su cui effettuare salti. L'etichetta **E** indica la terminazione. Un salto a un'etichetta inesistente fa terminare il programma. Servono solo con l'istruzione GOTO.

---

Cos'è lo stato di un programma S?
?
Lo **stato** σ è una funzione che associa ad ogni variabile del programma il suo valore corrente. È rappresentato come un insieme di coppie (variabile, valore), es. {X=2, Y=0, Z=0}.

---

Cos'è un'istantanea (snapshot)?
?
Un'**istantanea** è una coppia **(i, σ)** dove:
- **i**: indice della prossima istruzione da eseguire
- **σ**: stato corrente
L'istantanea **(l+1, σ)** (con l = numero totale di istruzioni) è detta **terminale**: il programma ha finito.

---

Cos'è il calcolo terminale?
?
Il **calcolo terminale** è la sequenza di istantanee che porta dall'istantanea iniziale (1, σ₀) a quella terminale (l+1, σ_f). Il risultato del programma è il valore di Y nello stato finale σ_f. Se il programma non termina, il calcolo è infinito e la funzione è indefinita.

---

## OPERAZIONI SULLE FUNZIONI E PARADIGMA FUNZIONALE

Definizione di composizione di funzioni
?
Data f m-aria e g₁,...,gₘ tutte n-arie, la **composizione** h è:
**h(x₁,...,xₙ) = f(g₁(x₁,...,xₙ), ..., gₘ(x₁,...,xₙ))**
h è n-aria. Si applica prima ogni gᵢ agli input, poi f ai risultati.

---

Dimostrazione del Teorema di Composizione
?
**Enunciato**: Se f, g₁,...,gₘ ∈ C (classe PRC), allora h = f∘(g₁,...,gₘ) ∈ C.
**Dimostrazione**: Si costruisce un programma S per h:
1. Per ogni i, si calcola gᵢ(x̄) e si salva in Zᵢ (esiste il programma per gᵢ per ipotesi, ∈ C).
2. Si calcola f(Z₁,...,Zₘ) (esiste il programma per f per ipotesi, ∈ C).
3. Il risultato è in Y.
Il programma complessivo calcola h. Poiché C è chiusa per composizione per definizione, h ∈ C. □

---

## RICORSIONE PRIMITIVA

Che tipologie di funzioni si usano nella ricorsione primitiva?
?
Si usano esclusivamente **funzioni totali**. La ricorsione primitiva è definita solo per funzioni totali, e garantisce che la funzione risultante h sia anch'essa totale.

---

Definizione generalizzata di funzione ricorsiva primitiva
?
h è definita per **ricorsione primitiva** da f (n-aria) e g ((n+2)-aria) se:
- **Caso base**: h(x₁,...,xₙ, 0) = f(x₁,...,xₙ)
- **Passo induttivo**: h(x₁,...,xₙ, t+1) = g(x₁,...,xₙ, t, h(x₁,...,xₙ, t))
Due modi per dimostrare che h è r.p.:
1. Costruzione diretta (caso base + passo)
2. Dimostrarla come composizione di funzioni r.p. già note

---

Dimostrazione del Teorema di Ricorsione Primitiva
?
**Enunciato**: Se f, g ∈ C (classe PRC), allora h definita per ricorsione primitiva da f e g appartiene a C.
**Dimostrazione**: Si costruisce un programma S per h(x̄, t):
1. Si inizializza un accumulatore A = f(x̄) (caso base, programma per f ∈ C).
2. Si usa un contatore T che parte da 0.
3. Finché T < t: si calcola g(x̄, T, A) → nuovo valore di A; si incrementa T.
4. Quando T = t, A contiene h(x̄, t).
Tutti i passi usano programmi in C. Poiché C è chiusa per composizione, il programma complessivo ∈ C. □

---

## CLASSI PRC

Definizione di classe PRC
?
Una classe **PRC** è una classe C di funzioni **totali** che:
1. Contiene le **funzioni iniziali** (zero, successore, proiezione)
2. È **chiusa per composizione**
3. È **chiusa per ricorsione primitiva**

---

Quali sono le funzioni iniziali delle classi PRC?
?
1. **Zero**: z(x) = 0 (unaria, costante)
2. **Successore**: s(x) = x + 1 (unaria)
3. **Proiezione**: Uⁿᵢ(x₁,...,xₙ) = xᵢ (n-aria, restituisce l'i-esimo argomento)
Attenzione: nella proiezione **entrambi** gli indici n (arità) e i (quale argomento) sono importanti.

---

Funzioni ricorsive primitive note — pag. 15
?
- **Addizione**: add(x,y) = x+y
- **Moltiplicazione**: mult(x,y) = x·y
- **Fattoriale**: fact(x) = x!
- **Predecessore**: pred(x) = x−1 se x>0, 0 se x=0
- **Sottrazione limitata**: x ∸ y = x−y se x≥y, 0 altrimenti
- **β (uguaglianza)**: β(x,y) = 1 se x=y, 0 altrimenti
- **α (se è zero)**: α(x) = 1 se x=0, 0 altrimenti

---

Funzioni ricorsive primitive note — pag. 19
?
- **Divisione predicato**: D(x,y) = 1 se y|x, 0 altrimenti
- **Primo**: Pr(x) = 1 se x è primo, 0 altrimenti
- **Quoziente**: quo(x,y) = ⌊x/y⌋ (funzione, restituisce un numero)
- **Resto**: rem(x,y) = x mod y
- **N-esimo primo**: p(n) = l'n-esimo numero primo (p(1)=2, p(2)=3, p(3)=5, ...)

---

Teorema di chiusura PRC per congiunzione, disgiunzione, negazione
?
**Enunciato**: Se P, Q ∈ C (classe PRC, predicati), allora ¬P, P∧Q, P∨Q ∈ C.
**Dimostrazione**:
- **Negazione**: ¬P(x̄) = α(P(x̄)) = 1−P(x̄). Composizione di P (∈C) con α (∈C) → ∈C.
- **Congiunzione**: P∧Q = P(x̄)·Q(x̄). Composizione con la moltiplicazione → ∈C.
- **Disgiunzione**: P∨Q = α(α(P(x̄))·α(Q(x̄))). Composizione → ∈C. □

---

Definizione degli operatori di sommatoria e produttoria
?
Dato f(x̄, t) ∈ C:
- **Sommatoria**: Σᵤ₌₀ʸ f(x̄, u) — somma i valori di f per u da 0 a y
- **Produttoria**: Πᵤ₌₀ʸ f(x̄, u) — prodotto dei valori di f per u da 0 a y
Entrambe sono funzioni di (x̄, y) definite per ricorsione primitiva su y.

---

Teorema di chiusura PRC per sommatoria e produttoria
?
**Enunciato**: Se f ∈ C, allora Σᵤ₌₀ʸ f(x̄,u) ∈ C e Πᵤ₌₀ʸ f(x̄,u) ∈ C.
**Dimostrazione** (sommatoria; produttoria analoga):
- Caso base: Σᵤ₌₀⁰ f(x̄,u) = f(x̄,0) → composizione di f con U, ∈C.
- Passo: Σᵤ₌₀ʸ⁺¹ f(x̄,u) = (Σᵤ₌₀ʸ f(x̄,u)) + f(x̄,y+1) → composizione con addizione, ∈C.
Definizione per ricorsione primitiva → ∈C. □

---

Definizione dei quantificatori limitati
?
Dato un predicato R(x̄, t):
- **Esistenziale limitato**: (∃t ≤ y) R(x̄,t) = 1 se esiste almeno un t≤y con R(x̄,t)=1
- **Universale limitato**: (∀t ≤ y) R(x̄,t) = 1 se per ogni t≤y vale R(x̄,t)=1
Devono essere **limitati superiormente** da y per garantire la calcolabilità (la quantificazione illimitata porta fuori dalle classi PRC).

---

Dimostrazione chiusura PRC per quantificatori limitati
?
**Enunciato**: Se R ∈ C, allora (∃t≤y)R e (∀t≤y)R ∈ C.
**Dimostrazione**:
- **Esistenziale**: (∃t≤y)R(x̄,t) = α(α(Σᵤ₌₀ʸ R(x̄,u))). La somma è >0 ↔ esiste un t che soddisfa R. La sommatoria è in C, α e composizione mantengono in C → ∈C.
- **Universale**: (∀t≤y)R(x̄,t) = α(α(Πᵤ₌₀ʸ R(x̄,u))). Il prodotto è 1 ↔ tutti i fattori sono 1. Produttoria in C, composizione mantiene in C → ∈C. □

---

Definizione di minimalizzazione limitata
?
**min_{t≤y} R(x̄,t)** = il più piccolo t ≤ y per cui R(x̄,t)=1; se nessun t≤y soddisfa R, restituisce y+1.
È **totale** perché il limite y garantisce sempre la terminazione. Serve per trovare il primo elemento che soddisfa una proprietà entro un limite fissato. Le classi PRC sono chiuse per minimalizzazione limitata.

---

Definizione di massimizzazione limitata
?
**max_{t≤y} R(x̄,t)** = il più grande t ≤ y per cui R(x̄,t)=1; se nessun t≤y soddisfa R, restituisce 0.
Si dimostra r.p. sfruttando la ricorsione primitiva su y: il massimo si aggiorna ad ogni passo se R vale per il nuovo t. Le classi PRC sono chiuse per massimizzazione limitata.

---

## PROBLEMA DELLA FERMATA E FUNZIONE UNIVERSALE

Cos'è la funzione di pairing (angoletto)?
?
La funzione di **pairing** ⟨x,y⟩ = ((x+y)(x+y+1))/2 + x è una funzione da ℕ² a ℕ che codifica una coppia di numeri in un singolo numero. È **ricorsiva primitiva**.

---

Proprietà fondamentali della funzione di pairing
?
1. È **ricorsiva primitiva**
2. È **biettiva** (iniettiva + suriettiva): ogni numero naturale corrisponde a esattamente una coppia
3. Le sue **inverse parziali** l (sinistra) e r (destra) sono ricorsive primitive:
   - l(⟨x,y⟩) = x
   - r(⟨x,y⟩) = y

---

Qual è l'inversa parziale sinistra della funzione di pairing?
?
**l(z)** = x, dove z = ⟨x,y⟩. Restituisce il **primo** elemento della coppia codificata da z.
È ricorsiva primitiva: si trova per minimalizzazione limitata come il più piccolo x≤z tale che esiste y≤z con ⟨x,y⟩=z.

---

Definizione del numero di Gödel
?
**[a₁,...,aₖ] = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ** dove pᵢ è l'i-esimo numero primo.
Codifica una k-pla di numeri naturali in un unico numero. Rappresenta una **classe** di funzioni (una per ogni k∈ℕ). Ogni [a₁,...,aₖ] è ricorsiva primitiva (produttoria di funzioni r.p.).

---

Definizione delle inverse parziali del numero di Gödel: (x)ᵢ
?
**(x)ᵢ** = esponente di pᵢ nella fattorizzazione di x.
Esempio: (10)₂ = 0 perché 10 = 2¹·3⁰·5¹, l'esponente di p₂=3 è 0.
È ricorsiva primitiva (per minimalizzazione limitata: il più grande e≤x tale che pᵢ^e divide x).

---

Definizione di Lt(x)
?
**Lt(x)** = lunghezza della sequenza codificata da x = il più grande indice i tale che (x)ᵢ ≠ 0.
Se x=1 (nessun fattore primo), Lt(1)=0. È ricorsiva primitiva.
Serve per sapere quanti elementi significativi sono codificati nel numero di Gödel (escludendo gli zeri finali).

---

Come si risolve il problema della non-biettività dei numeri di Gödel?
?
Il numero di Gödel **non è biettivo**:
- **Non suriettivo**: 0 non è codificato da nessuna k-pla (ogni prodotto di primi è ≥1)
- **Non iniettivo**: aggiungere zeri a destra non cambia il valore: [a₁,...,aₖ] = [a₁,...,aₖ,0]
**Soluzione**: si usa Lt(x) per conoscere la lunghezza effettiva della sequenza, e si considera il numero 0 come caso speciale (lista vuota di lunghezza 0). Così due codifiche diverse rappresentano sequenze diverse se hanno Lt diverso.

---

Perché usiamo i numeri di Gödel?
?
Permettono di **codificare sequenze di numeri in un unico numero**, rendendo possibile trattare programmi come dati numerici. Questo è fondamentale per:
- Codificare le istruzioni di un programma S come numero
- Permettere a un programma di ricevere come input un altro programma
- Definire la funzione universale e formalizzare il problema della fermata

---

Definizione della codifica delle istruzioni del linguaggio S
?
Si assegna un numero ad ogni variabile: Y=1, X₁=2, Z₁=3, X₂=4, Z₂=5, ...
Si assegna un numero ad ogni etichetta: nessuna=0, A₁=1, B₁=2, C₁=3, D₁=4, E₁=5, A₂=6, ...
Il **tipo** di istruzione è codificato: V←V=0, V←V+1=1, V←V-1=2, IF V≠0 GOTO L=3+4·(cod_etichetta).
Un'**istruzione** è codificata come la coppia ⟨cod_variabile - 1, cod_tipo⟩.
Un **programma** di l istruzioni è codificato come [cod_istr₁, ..., cod_istrₗ] (numero di Gödel).

---

Dimostrazione che esistono funzioni non parzialmente calcolabili
?
**Dimostrazione per diagonalizzazione (Cantor)**:
1. I programmi S sono liste finite di istruzioni su un alfabeto finito → sono **numerabili**: esiste una biiezione con ℕ. Si possono elencare come φ₀, φ₁, φ₂, ...
2. Le funzioni f: ℕ→ℕ sono **non numerabili** (hanno la cardinalità del continuo, come i reali).
3. Poiché |programmi| = |ℕ| < |funzioni da ℕ a ℕ|, esistono funzioni che **non corrispondono ad alcun programma** → funzioni non parzialmente calcolabili. □

---

Cos'è il predicato HALT?
?
**HALT(x,y) = 1** se il programma con codice y termina sull'input x; 0 altrimenti.
Il suo scopo è determinare se un dato programma si ferma su un dato input. È **non calcolabile**: non esiste un algoritmo che lo calcoli in ogni caso.

---

Dimostrazione che HALT non è calcolabile
?
**Dimostrazione per diagonalizzazione**:
1. Supponi per assurdo che HALT sia calcolabile.
2. Definisci f(x) = 0 se HALT(x,x)=0 (il programma x non termina su x), ↑ se HALT(x,x)=1.
3. f è parzialmente calcolabile → ha un codice e: f = φₑ.
4. Valuto per x=e:
   - Se HALT(e,e)=1: φₑ(e) termina → f(e)↑ → contraddizione.
   - Se HALT(e,e)=0: φₑ(e)↑ → f(e)=0 termina → contraddizione.
5. In entrambi i casi contraddizione → HALT non è calcolabile. □

---

Definizione della funzione universale Φ
?
**Φ⁽ⁿ⁾(x₁,...,xₙ, y)** = risultato dell'esecuzione del programma con codice y sull'input (x₁,...,xₙ), se termina; ↑ altrimenti.
È **parzialmente calcolabile** (non totale): termina ↔ il programma y termina su quell'input. Rappresenta una classe di funzioni (una per ogni n). Dimostra che un programma può simulare qualsiasi altro.

---

Definizione di STP
?
**STP(x, y, t) = 1** se il programma con codice y termina sull'input x **entro t passi**, 0 altrimenti.
È **ricorsivo primitivo** (totalmente calcolabile): si simula il programma contando i passi, ci si ferma dopo t.

---

Classificazione di HALT, STP e funzione universale
?
- **HALT**: **non calcolabile** (indecidibile)
- **STP**: **ricorsivo primitivo** — totalmente calcolabile, termina sempre
- **Funzione universale Φ**: **parzialmente calcolabile** — termina solo se il programma simulato termina

---

Come si scrive HALT usando STP?
?
**HALT(x,y) = 1 ↔ ∃t. STP(x,y,t) = 1**
Un programma termina se e solo se esiste un t entro cui termina. La quantificazione su t è **illimitata** → HALT resta non calcolabile nonostante STP lo sia.

---

## INSIEMI RICORSIVI E RICORSIVAMENTE ENUMERABILI

Cos'è la funzione caratteristica di un insieme?
?
La **funzione caratteristica** fₛ di S ⊆ ℕ è:
- fₛ(x) = 1 se x ∈ S
- fₛ(x) = 0 se x ∉ S
È sempre **totale**. Serve per collegare insiemi e funzioni: S è ricorsivo ↔ fₛ è totalmente calcolabile; S è ricorsivo primitivo ↔ fₛ è ricorsiva primitiva.

---

Qual è la relazione tra insieme S ricorsivo/r.p. e funzione caratteristica?
?
- S è **ricorsivo primitivo** ↔ fₛ è **ricorsiva primitiva**
- S è **ricorsivo** ↔ fₛ è **totalmente calcolabile**
In entrambi i casi la funzione caratteristica deve essere **totale** (terminare sempre).

---

Definizione di insieme ricorsivo
?
Un insieme S ⊆ ℕ è **ricorsivo** se la sua funzione caratteristica fₛ è **totalmente calcolabile**: esiste un programma che termina sempre e restituisce 1 se x∈S, 0 se x∉S (**procedura di decisione**).

---

Definizione di insieme ricorsivamente enumerabile
?
Un insieme S ⊆ ℕ è **ricorsivamente enumerabile (r.e.)** se esiste una funzione parzialmente calcolabile g tale che:
- g(x)↓ (termina) ↔ x ∈ S
- g(x)↑ (non termina) ↔ x ∉ S
Equivale ad avere una **procedura di semi-decisione**: il programma termina solo per gli elementi di S.

---

Teorema: chiusura per operazioni insiemistiche su insiemi ricorsivi
?
**Enunciato**: Se S e S' sono ricorsivi, allora S∪S', S∩S', S̄ (complemento) sono ricorsivi.
**Dimostrazione**:
- **Complemento**: fₛ̄ = 1−fₛ = α(fₛ). Composizione di funzioni totali calcolabili → totale calcolabile.
- **Unione**: fₛ∪ₛ'(x) = fₛ(x) ∨ fₛ'(x). Composizione → totale calcolabile.
- **Intersezione**: fₛ∩ₛ'(x) = fₛ(x) ∧ fₛ'(x). Composizione → totale calcolabile. □

---

Gli insiemi ricorsivi sono contenuti nei ricorsivamente enumerabili?
?
**Sì**: ogni insieme ricorsivo è anche r.e.
**Dimostrazione**: Se S è ricorsivo, esiste fₛ totale calcolabile. Definisci g(x) = 0 se fₛ(x)=1, ↑ altrimenti. g è parzialmente calcolabile e il suo dominio è S → S è r.e. □
Il viceversa non vale: K è r.e. ma non ricorsivo.

---

Relazione tra ricorsività e ricorsiva enumerabilità
?
S è **ricorsivo** ↔ **sia S che il complemento S̄ sono r.e.**
**Dimostrazione (⇒)**: S ricorsivo → fₛ calcolabile → fₛ̄ calcolabile → S̄ ricorsivo → S̄ r.e.
**Dimostrazione (⇐)**: Se S e S̄ sono r.e., esistono g (dominio S) e g̃ (dominio S̄). Si eseguono **in parallelo**: per ogni input x, si alternano i passi di g e g̃. Prima o poi uno dei due termina e decide l'appartenenza → procedura di decisione → S ricorsivo. □

---

Teorema: unione e intersezione di insiemi r.e. sono r.e.
?
**Enunciato**: Se S, S' sono r.e., allora S∩S' e S∪S' sono r.e.
**Dimostrazione per S∩S'**: Siano g (dominio S) e g' (dominio S'). Definisci h(x) = g(x)+g'(x). h↓ ↔ entrambe terminano ↔ x∈S∩S'. → S∩S' r.e.
**Dimostrazione per S∪S'**: Si eseguono g e g' **in parallelo** (dovetailing, alternando i passi). h↓ ↔ almeno una termina ↔ x∈S∪S'. → S∪S' r.e. □

---

Definizione dell'operatore di complemento
?
Il **complemento** di S ⊆ ℕ è **S̄ = ℕ \ S**, cioè l'insieme di tutti i numeri naturali che non appartengono a S.
Proprietà: (S̄)̄ = S. Se S è ricorsivo → S̄ è ricorsivo. Se S è r.e. → S̄ non è necessariamente r.e.

---

Definizione di insieme diagonale K
?
**K = {x | il programma x termina sull'input x}** = {x | φₓ(x)↓} = {x | HALT(x,x)=1}
K è **ricorsivamente enumerabile** (è il dominio della funzione parzialmente calcolabile Φ(x,x)) ma **NON ricorsivo**.

---

Funzione caratteristica di K
?
La funzione caratteristica fₖ di K è:
- fₖ(x) = 1 se il programma x termina su x
- fₖ(x) = 0 altrimenti
fₖ **non è calcolabile**: se lo fosse, potremmo calcolare HALT(x,x) = fₖ(x), che è indecidibile. Quindi K non è ricorsivo.

---

Dimostrazione del teorema di enumerazione (K non è ricorsivo; K̄ non è r.e.)
?
**K è r.e.**: K = dominio di Φ(x,x), parzialmente calcolabile → K è r.e. ✓
**K non è ricorsivo**: Supponi K ricorsivo → fₖ calcolabile → costruisci f(x)=0 se x∉K, ↑ se x∈K. f è parzialmente calcolabile → ha codice e. Per x=e: se e∈K allora f(e)↑ → e∉K, contraddizione; se e∉K allora f(e)=0↓ → e∈K, contraddizione. → K non ricorsivo. □
**K̄ non è r.e.**: Se K̄ fosse r.e., allora K e K̄ entrambi r.e. → K ricorsivo → contraddizione. □

---

## AUTOMI A STATI FINITI (DFA)

Definizione formale di DFA
?
Un **DFA** è una quintupla M = (Q, A, δ, q₁, F) dove:
- **Q**: insieme finito di stati
- **A**: alfabeto di input
- **δ: Q × A → Q**: funzione di transizione (deterministica, totale)
- **q₁ ∈ Q**: stato iniziale
- **F ⊆ Q**: insieme degli stati finali

---

Definizione della funzione di transizione iterata δ* (DFA)
?
La funzione **δ*: Q × A* → Q** estende δ alle stringhe, per induzione:
- **Caso base**: δ*(q, ε) = q
- **Passo induttivo**: δ*(q, wa) = δ(δ*(q, w), a)
L'idea del passo: prima si porta q nello stato raggiunto leggendo **w** (con δ*), poi si fa un passo aggiuntivo con il simbolo **a**.

---

Quando un linguaggio L è accettato da un DFA?
?
**L(M) = {w ∈ A* | δ*(q₁, w) ∈ F}**
w è accettata se la funzione di transizione iterata, partendo da q₁ e leggendo w, arriva in uno stato finale. Il linguaggio L è accettato da M se L = L(M).

---

Definizione di linguaggio regolare
?
Un linguaggio L ⊆ A* è **regolare** se esiste un DFA M tale che **L = L(M)**.

---

Definizione di NFA
?
Un **NFA** è una quintupla M = (Q, A, δ, q₁, F) identica al DFA tranne per la funzione di transizione:
**δ: Q × A → 𝒫(Q)** — restituisce un **insieme** di stati (anche vuoto).
Una stringa è accettata se almeno un percorso possibile termina in uno stato finale.

---

Definizione della funzione di transizione iterata δ* per NFA
?
La funzione **δ*: Q × A* → 𝒫(Q)** per induzione:
- **Caso base**: δ*(q, ε) = {q}
- **Passo induttivo**: δ*(q, wa) = ⋃_{p ∈ δ*(q,w)} δ(p, a)
L'idea del passo: si calcola prima l'insieme degli stati raggiungibili con **w** (δ*(q,w)), poi si fa un passo con **a** da ognuno di essi, e si unisce tutto.

---

Quando un linguaggio L è accettato da un NFA?
?
**L(M) = {w ∈ A* | δ*(q₁, w) ∩ F ≠ ∅}**
w è accettata se almeno uno degli stati raggiungibili leggendo w da q₁ è uno stato finale.

---

## OPERAZIONI SUI LINGUAGGI REGOLARI

Definizione di DFA non-restarting
?
Un **DFA non-restarting** è un DFA in cui lo stato iniziale q₁ **non ha transizioni entranti**: nessuna transizione porta a q₁. Una volta usciti dallo stato iniziale, non vi si ritorna mai. Semplifica la costruzione di automi composti (unione, concatenazione, star).

---

Dimostrazione: l'unione di linguaggi regolari è regolare
?
**Enunciato**: Se L₁, L₂ ⊆ A* sono regolari, allora L₁∪L₂ è regolare.
**Dimostrazione**: Siano M₁=(Q₁,A,δ₁,q₁,F₁) e M₂=(Q₂,A,δ₂,q₂,F₂) DFA non-restarting (Q₁∩Q₂=∅).
Costruisci NFA M=(Q₁∪Q₂∪{q₀}, A, δ, q₀, F₁∪F₂) con q₀ nuovo stato iniziale:
- δ(q₀, a) = δ₁(q₁,a) ∪ δ₂(q₂,a) per ogni a∈A
- δ(q,a) = δᵢ(q,a) per q∈Qᵢ, i=1,2
La funzione iterata: δ*(q₀,wa) = δ*(q₀,w) ∪ (⋃_{p∈δ*(q₀,w)} δ(p,a)).
M accetta w ↔ M₁ o M₂ accetta w ↔ w∈L₁∪L₂. NFA≡DFA → L₁∪L₂ regolare. □

---

Definizione di prodotto per concatenazione di linguaggi
?
**L₁·L₂ = {uv | u∈L₁, v∈L₂}**
L'alfabeto è A₁∪A₂. Si concatenano tutte le stringhe di L₁ con tutte quelle di L₂.

---

Dimostrazione: la concatenazione di linguaggi regolari è regolare
?
**Enunciato**: Se L₁, L₂ sono regolari, allora L₁·L₂ è regolare.
**Dimostrazione**: Siano M₁, M₂ DFA non-restarting.
Costruisci NFA M: si parte da q₁ di M₁; dagli stati finali di M₁ si aggiungono le transizioni di q₁ di M₂ (gli stati finali di M₁ "si comportano anche come q₁ di M₂"); gli stati finali di M sono quelli di F₂.
M accetta w ↔ esiste u·v=w con u∈L₁, v∈L₂. NFA≡DFA → L₁·L₂ regolare. □

---

Definizione di iterazione (Star) di un linguaggio
?
**L* = ⋃_{n≥0} Lⁿ** dove L⁰={ε}, Lⁿ=L·Lⁿ⁻¹.
Contiene: ε, tutte le stringhe di L, tutte le concatenazioni di 2 stringhe di L, di 3, ecc. Non si può ricavare come unione finita → va definita separatamente.

---

Dimostrazione: L* è regolare se L è regolare
?
**Enunciato**: Se L è regolare, allora L* è regolare.
**Dimostrazione**: Sia M=(Q,A,δ,q₁,F) DFA non-restarting.
Costruisci NFA M*=(Q∪{q₀},A,δ*,q₀,F∪{q₀}):
- q₀ nuovo stato iniziale e finale (per includere ε)
- δ*(q₀,a) = δ(q₁,a) (q₀ simula q₁)
- Per ogni q∈F: δ*(q,a) include δ(q₁,a) (dagli stati finali si può ricominciare)
- Altrimenti δ*=δ
M* accetta ε (q₀∈F) e ogni concatenazione di stringhe di L. NFA≡DFA → L* regolare. □

---

Teorema di Kleene
?
**Enunciato**: L⊆A* è regolare ↔ L è denotabile da un'espressione regolare.
**Dim. (⇒) Automa → Regex**: Per induzione si eliminano gli stati dell'automa uno alla volta (state elimination), accumulando l'espressione regolare sui cammini rimanenti, fino ad ottenere la regex per L(M).
**Dim. (⇐) Regex → Automa**: Per induzione sulla struttura della regex:
- Basi: a → DFA 2 stati; ε → DFA con q₁∈F; ∅ → DFA senza stati finali.
- Passo: α∪β, α·β, α* → si usano le costruzioni di unione, concatenazione, star. □

---

Sintassi e precedenza delle espressioni regolari
?
Simboli: lettere, ε, ∅, ∪, · (concatenazione), *, ( ).
**Precedenza** (dalla più alta):
1. **Star (*)**: si lega solo all'elemento immediatamente a sinistra
2. **Concatenazione (·)**
3. **Unione (∪)**
Esempio: a∪bc* = a∪(b·(c*))

---

## PUMPING LEMMA PER LINGUAGGI REGOLARI

Enunciato del Pumping Lemma per linguaggi regolari
?
Se L è regolare, esiste **n** (numero di stati del DFA) tale che ogni z∈L con |z|≥n si scrive z=uvw con:
1. |uv| ≤ n
2. |v| ≥ 1
3. ∀i≥0: uvⁱw ∈ L
**Idea**: una stringa lunga almeno n deve passare due volte per lo stesso stato (piccionaia) → ciclo v che si può pompare.

---

Come si usa il Pumping Lemma per dimostrare che L NON è regolare?
?
Per **contraddizione**:
1. Assumo L regolare (esiste n)
2. Scelgo strategicamente z∈L con |z|≥n
3. Per **ogni** divisione z=uvw con |uv|≤n e |v|≥1, trovo i tale che uvⁱw∉L
4. Contraddizione → L non regolare

---

## GRAMMATICHE CONTEXT-FREE

Definizione formale di grammatica context-free (CFG)
?
Una **CFG** è una quadrupla G=(V,Σ,R,S) dove:
- **V**: variabili (non terminali), V∩Σ=∅
- **Σ**: terminali
- **R**: regole finite della forma A→α, con A∈V e α∈(V∪Σ)*
- **S∈V**: simbolo iniziale
L(G) = {w∈Σ* | S⇒*w}

---

Cos'è l'ambiguità in una CFG?
?
Una grammatica è **ambigua** se esiste almeno una stringa con **due o più alberi di derivazione distinti** (equivalentemente: due derivazioni leftmost diverse). Problematica nei compilatori: stessa stringa → due significati diversi.

---

Dimostrazione: chiusura per unione dei linguaggi context-free
?
**Enunciato**: Se L₁, L₂ sono CF, allora L₁∪L₂ è CF.
**Dimostrazione**: Siano G₁=(V₁,Σ,R₁,S₁) e G₂=(V₂,Σ,R₂,S₂) con V₁∩V₂=∅.
Costruisci G=(V₁∪V₂∪{S}, Σ, R₁∪R₂∪{S→S₁|S→S₂}, S).
Ogni derivazione inizia con S→S₁ (genera L₁) oppure S→S₂ (genera L₂) → L(G)=L₁∪L₂. □

---

Dimostrazione: chiusura star per linguaggi context-free
?
**Enunciato**: Se L è CF, allora L* è CF.
**Dimostrazione**: Sia G=(V,Σ,R,S) CFG per L.
Costruisci G*=(V∪{S'}, Σ, R∪{S'→ε, S'→S'S}, S') dove S' è un nuovo simbolo iniziale:
- S'→ε include la stringa vuota (L⁰)
- S'→S'S permette di concatenare ripetutamente stringhe di L
L(G*) = L*: ogni derivazione di S' produce una concatenazione di zero o più stringhe di L. □

---

Dimostrazione: tutti i linguaggi finiti sono context-free
?
**Enunciato**: Ogni linguaggio finito L={w₁,...,wₖ} è CF.
**Dimostrazione**: Si costruisce G con regole S→w₁ | w₂ | ... | wₖ. L(G)=L. □
Alternativa: ogni linguaggio finito è regolare (DFA con percorsi finiti) e ogni regolare è CF.

---

Dimostrazione: tutti i linguaggi regolari sono context-free (via grammatica regolare)
?
Dato DFA M=(Q,A,δ,q₁,F), costruisci CFG G:
- Variabili = stati Q
- Per ogni δ(qᵢ,a)=qⱼ: aggiungi regola qᵢ→a qⱼ
- Per ogni qᵢ∈F: aggiungi qᵢ→ε
- Simbolo iniziale = q₁
G è **grammatica regolare** (lineare destra) e L(G)=L(M). Quindi ogni linguaggio regolare è CF. □

---

Dimostrazione: tutti i linguaggi regolari sono context-free (via inclusione delle classi)
?
Le grammatiche regolari (regole A→aB, A→a, A→ε) sono un **caso speciale** di CFG: le regole A→aB e A→a rispettano il formato A→α con α∈(V∪Σ)*. Quindi ogni grammatica regolare è anche una CFG → ogni linguaggio regolare è CF. □

---

Cos'è una grammatica regolare?
?
Una **grammatica regolare** (lineare destra) è una CFG con regole solo della forma:
- **A → aB** (terminale + variabile)
- **A → a** (solo terminale)
- **A → ε** (stringa vuota)
Genera esattamente i linguaggi regolari.

---

Definizione formale di automa pushdown (PDA)
?
Un **PDA** è una sestupla M=(Q, A, Γ, δ, q₁, F) dove:
- **Q**: stati
- **A**: alfabeto input
- **Γ**: alfabeto della pila
- **δ: Q×(A∪{ε})×Γ → 𝒫(Q×Γ*)**: funzione di transizione (legge input o ε, toglie un simbolo dalla pila, inserisce una stringa)
- **q₁**: stato iniziale
- **F**: stati finali
Le etichette di transizione hanno forma **a, β → w**: leggi a (o ε), togli β dalla pila, inserisci w.

---

Dimostrazione: CFG ↔ PDA (equivalenza, direzione CFG→PDA)
?
**Enunciato**: Se L è CF, esiste un PDA che accetta L.
**Dimostrazione**: Data G=(V,Σ,R,S), costruisci PDA con:
- Pila iniziale: S (simbolo iniziale)
- Per ogni regola A→α: transizione ε, A→α (espande la variabile in cima alla pila con α in ordine inverso)
- Per ogni terminale a∈Σ: transizione a, a→ε (fa match tra input e cima della pila)
Il PDA accetta quando pila e input sono entrambi vuoti: ha simulato una derivazione di G. □

---

Dimostrazione: CFG ↔ PDA (equivalenza, direzione PDA→CFG)
?
**Enunciato**: Se esiste un PDA che accetta L, allora L è CF.
**Idea della dimostrazione**: Ogni transizione del PDA (q, a, β)→(p, w) corrisponde a una produzione della CFG. Si introduce una variabile per ogni coppia (stato, simbolo di pila) che codifica il "da q con β in pila si arriva a p svuotando β". La CFG risultante genera esattamente le stringhe accettate dal PDA. □

---

## FORME NORMALI DI CHOMSKY

Cos'è la Forma Normale di Chomsky (CNF)?
?
Una CFG è in **CNF** se ogni regola ha una delle forme:
- **A → BC** (esattamente due variabili)
- **A → a** (esattamente un terminale)
- Eventualmente **S → ε** (solo per S, se ε∈L)
Ogni linguaggio CF è generabile da una grammatica in CNF.

---

Come si normalizza una CFG in CNF?
?
Si applicano in sequenza:
1. **Eliminare ε-produzioni**: per ogni A→ε, propagare rimuovendo A da ogni lato destro, poi eliminare A→ε (tranne S→ε se ε∈L).
2. **Eliminare produzioni unitarie** (A→B): sostituire con le produzioni di B.
3. **Isolare i terminali nelle regole lunghe**: per ogni terminale a in regola con |α|≥2, introdurre Tₐ→a e rimpiazzare a con Tₐ.
4. **Binarizzare**: A→B₁B₂...Bₖ con k>2 diventa A→B₁C₁, C₁→B₂C₂, ..., Cₖ₋₂→Bₖ₋₁Bₖ.

---

## PUMPING LEMMA PER LINGUAGGI CONTEXT-FREE

Enunciato del Pumping Lemma per linguaggi context-free
?
Se L è CF, esiste **n** tale che ogni z∈L con |z|≥n si scrive z=uvwxy con:
1. |vwx| ≤ n
2. |vx| ≥ 1 (v e x non entrambe vuote)
3. ∀i≥0: uvⁱwxⁱy ∈ L (v e x si pompano **simultaneamente**)
**Idea**: in un albero di derivazione in CNF abbastanza alto, una variabile si ripete (piccionaia) → si può "pompare" quella parte dell'albero.

---

Come si usa il Pumping Lemma CF per dimostrare non-CF?
?
Per **contraddizione**:
1. Assumo L CF (esiste n)
2. Scelgo strategicamente z∈L con |z|≥n
3. Per **ogni** divisione z=uvwxy con |vwx|≤n e |vx|≥1, trovo i tale che uvⁱwxⁱy∉L
4. Contraddizione → L non CF
