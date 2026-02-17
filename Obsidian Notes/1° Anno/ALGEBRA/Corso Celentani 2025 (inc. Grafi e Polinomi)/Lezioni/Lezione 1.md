# Logica Proposizionale e Teoria degli Insiemi

**Data:** 11/03/2025
**Argomenti:** Connettivi logici, Tavole di verità, Tautologie, Contraddizioni, Quantificatori, Teoria degli Insiemi di base, Prodotto Cartesiano, Relazioni, Funzioni.

#tag/logica #tag/settheory #tag/algebra-avanzata #tag/fondamenti

---

## 1. Logica Proposizionale: I Mattoncini del Ragionamento

La logica ci aiuta a capire come costruire ragionamenti validi. Iniziamo con le basi: le proposizioni e come collegarle. Una **proposizione** è un'affermazione che può essere VERA (V) o FALSA (F).

### 1.1 Connettivi Logici Fondamentali

I connettivi logici sono come la "colla" che unisce le proposizioni semplici per crearne di più complesse.

*   **Negazione (NOT):** Inverte il valore di verità.
    *   Simbolo: $\neg$ (si legge "non")
    *   Esempio: Se $P$ è "Oggi piove", $\neg P$ è "Oggi non piove".

**Tavola di Verità (Negazione):**

| $P$ | $\neg P$ |
| :--: | :----: |
| V | F |
| F | V |

*   **Congiunzione (AND):** È vera solo se *entrambe* le proposizioni sono vere.
    *   Simbolo: $\land$ (si legge "e")
    *   Esempio: Se $P$ è "Studio logica" e $Q$ è "Ascolto musica", $P \land Q$ è "Studio logica e ascolto musica".

**Tavola di Verità (Congiunzione):**

| $P$ | $Q$ | $P \land Q$ |
| :--: | :--: | :-------: |
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

*   **Disgiunzione Inclusiva (OR):** È vera se *almeno una* delle proposizioni è vera.
    *   Simbolo: $\lor$ (si legge "o")
    *   Esempio: Se $P$ è "Prendo il caffè" e $Q$ è "Prendo il tè", $P \lor Q$ è "Prendo il caffè o prendo il tè (o entrambi)".

**Tavola di Verità (Disgiunzione Inclusiva):**

| $P$ | $Q$ | $P \lor Q$ |
| :--: | :--: | :-------: |
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

> [!NOTE] Nota Bene: Questa è la "o" inclusiva, significa che va bene anche se entrambe sono vere. Nelle tue note c'era scritto "non disgiuntiva", ma in realtà $\lor$ *è* la disgiunzione standard (inclusiva). Forse intendevi la disgiunzione *esclusiva*? Ne parliamo tra poco! [[#1.5 Disgiunzione Esclusiva (XOR)]]

*   **Implicazione Materiale (SE... ALLORA):** È falsa solo se la prima proposizione (antecedente) è vera e la seconda (conseguente) è falsa.
    *   Simbolo: $\implies$ (o $\rightarrow$, si legge "implica" o "se... allora")
    *   Esempio: Se $P$ è "Studio" e $Q$ è "Passo l'esame", $P \implies Q$ è "Se studio, allora passo l'esame".

**Tavola di Verità (Implicazione):**

| $P$ | $Q$ | $P \implies Q$ |
| :--: | :--: | :----------: |
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

> [!TIP] Suggerimento: Pensa all'implicazione come a una promessa. $P \implies Q$ significa "Se P è vera, prometto che Q è vera". L'unico caso in cui la promessa è infranta è quando P è vera, ma Q è falsa. Se P è falsa, la promessa non è stata messa alla prova, quindi l'implicazione è considerata vera.

*   **Bicondizionale (SE E SOLO SE):** È vera solo se le proposizioni hanno lo *stesso* valore di verità.
    *   Simbolo: $\iff$ (o $\leftrightarrow$, si legge "se e solo se" o "è equivalente a")
    *   Esempio: Se $P$ è "Il triangolo ha 3 lati uguali" e $Q$ è "Il triangolo ha 3 angoli uguali", $P \iff Q$ è "Un triangolo ha 3 lati uguali se e solo se ha 3 angoli uguali".

**Tavola di Verità (Bicondizionale):**

| $P$ | $Q$ | $P \iff Q$ |
| :--: | :--: | :--------: |
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

### 1.2 Equivalenze Logiche Importanti

Alcune formule complesse sono equivalenti, cioè hanno sempre lo stesso valore di verità.

*   **Implicazione e Disgiunzione:** L'implicazione $P \implies Q$ è equivalente a $\neg P \lor Q$.
    *   Formula: $(P \implies Q) \iff (\neg P \lor Q)$

**Verifica Equivalenza (Implicazione $\iff$ Disgiunzione Negata):**

| $P$ | $Q$ | $P \implies Q$ | $\neg P$ | $\neg P \lor Q$ | $(P \implies Q) \iff (\neg P \lor Q)$ |
| :--: | :--: | :----------: | :------: | :-----------: | :---------------------------------: |
| V | V | V | F | V | V |
| V | F | F | F | F | V |
| F | V | V | V | V | V |
| F | F | V | V | V | V |

> [!IMPORTANT] Questa equivalenza è super utile per trasformare le implicazioni! [[Equivalenza Implicazione-Disgiunzione]]

*   **Doppia Negazione:** Negare due volte riporta alla proposizione originale.
    *   Formula: $\neg (\neg P) \iff P$
    *   [[Legge della Doppia Negazione]]

*   **Contrapposizione:** L'implicazione $P \implies Q$ è equivalente alla sua contrapposta $\neg Q \implies \neg P$.
    *   Formula: $(P \implies Q) \iff (\neg Q \implies \neg P)$

**Verifica Equivalenza (Implicazione $\iff$ Contrapposta):**

| $P$ | $Q$ | $P \implies Q$ | $\neg Q$ | $\neg P$ | $\neg Q \implies \neg P$ | $(P \implies Q) \iff (\neg Q \implies \neg P)$ |
| :--: | :--: | :----------: | :------: | :------: | :------------------: | :---------------------------------------: |
| V | V | V | F | F | V | V |
| V | F | F | V | F | F | V |
| F | V | V | F | V | V | V |
| F | F | V | V | V | V | V |

*   [[Legge di Contrapposizione]]

### 1.3 Tautologie e Contraddizioni

*   **Tautologia:** Una proposizione composta che è **sempre VERA**, indipendentemente dal valore di verità delle proposizioni semplici che la compongono.
    *   Esempi (dalle tue note!):
        *   $P \lor \neg P$ (Principio del terzo escluso)
        *   $P \implies P$ (Identità)
        *   $((P \implies Q) \land P) \implies Q$ (Modus Ponens)
    > [!NOTE] Le tautologie rappresentano le leggi fondamentali del pensiero logico.
    *   #tag/tautologia [[Tautologia]]

*   **Contraddizione:** Una proposizione composta che è **sempre FALSA**. È la negazione di una tautologia.
    *   Esempio (dalle tue note!): $P \land \neg P$ (Principio di non contraddizione)
    *   Formula: $P \land \neg P \iff \neg (P \lor \neg P)$
    *   #tag/contraddizione [[Contraddizione]]

### 1.4 Leggi Logiche (Proprietà Tautologiche)

Queste sono equivalenze logiche fondamentali che valgono sempre (sono tautologie). Usiamo $a, b, c$ come proposizioni generiche. [[Leggi Logiche]]

1.  **Idempotenza:** Ripetere una proposizione con $\land$ o $\lor$ non cambia nulla.
    *   $a \land a \iff a$
    *   $a \lor a \iff a$
    *   [[Legge di Idempotenza]]
2.  **Associatività:** Puoi raggruppare come vuoi con lo stesso connettivo ($\land$, $\lor$, $\iff$).
    *   $(a \land b) \land c \iff a \land (b \land c)$
    *   $(a \lor b) \lor c \iff a \lor (b \lor c)$
    *   $(a \iff b) \iff c \iff a \iff (b \iff c)$ (*Attenzione: l'associatività per $\implies$ non vale in generale!*)
    *   [[Legge Associativa]]
3.  **Commutatività:** Puoi scambiare l'ordine delle proposizioni con $\land$, $\lor$, $\iff$.
    *   $a \land b \iff b \land a$
    *   $a \lor b \iff b \lor a$
    *   $a \iff b \iff b \iff a$
    *   [[Legge Commutativa]]
4.  **Distributività:** Come la moltiplicazione si distribuisce sulla somma in aritmetica.
    *   $a \land (b \lor c) \iff (a \land b) \lor (a \land c)$ ($\land$ si distribuisce su $\lor$)
    *   $a \lor (b \land c) \iff (a \lor b) \land (a \lor c)$ ($\lor$ si distribuisce su $\land$)

**Verifica Legge Distributiva ($\land$ su $\lor$):**

| $a$ | $b$ | $c$ | $b \lor c$ | $a \land (b \lor c)$ | $a \land b$ | $a \land c$ | $(a \land b) \lor (a \land c)$ | Equivalenza |
| :--: | :--: | :--: | :-------: | :-----------------: | :-------: | :-------: | :-------------------------: | :---------: |
| V | V | V | V | V | V | V | V | V |
| V | V | F | V | V | V | F | V | V |
| V | F | V | V | V | F | V | V | V |
| V | F | F | F | F | F | F | F | V |
| F | V | V | V | F | F | F | F | V |
| F | V | F | V | F | F | F | F | V |
| F | F | V | V | F | F | F | F | V |
| F | F | F | F | F | F | F | F | V |

*   [[Legge Distributiva]]

5.  **Leggi di De Morgan:** Utili per negare $\land$ e $\lor$.
    *   $\neg (a \land b) \iff (\neg a \lor \neg b)$
    *   $\neg (a \lor b) \iff (\neg a \land \neg b)$
    *   [[Leggi di De Morgan]]
6.  **Transitività dell'Implicazione:** Se $a$ implica $b$ e $b$ implica $c$, allora $a$ implica $c$.
    *   Formula: $((a \implies b) \land (b \implies c)) \implies (a \implies c)$

**Verifica Transitività Implicazione:**

| $a$ | $b$ | $c$ | $b \implies c$ | $a \implies b$ | $(a \implies b) \land (b \implies c)$ | $a \implies c$ | Transitività |
| :--: | :--: | :--: | :----------: | :----------: | :-------------------------------: | :----------: | :------------: |
| V | V | V | V | V | V | V | V |
| V | V | F | F | V | F | F | V |
| V | F | V | V | F | F | V | V |
| V | F | F | V | F | F | F | V |
| F | V | V | V | V | V | V | V |
| F | V | F | F | V | F | V | V |
| F | F | V | V | V | V | V | V |
| F | F | F | V | V | V | V | V |

*   [[Legge di Transitività (Sillogismo Ipotetico)]]

### 1.5 Disgiunzione Esclusiva (XOR)

Questo è l'"o" che significa "uno o l'altro, ma non entrambi".

*   Simbolo: $\oplus$ (o $\veebar$, a volte indicato come $\dot{\lor}$ nelle tue note)
*   Significato: $a \oplus b$ è vera se *esattamente una* tra $a$ e $b$ è vera.
*   Equivalenza (dalle tue note!): $a \oplus b \iff (\neg a \land b) \lor (a \land \neg b)$
*   Equivalenza alternativa: $a \oplus b \iff (a \lor b) \land \neg (a \land b)$

**Tavola di Verità (XOR):**

| $P$ | $Q$ | $P \oplus Q$ |
| :--: | :--: | :----------: |
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | F |

*   #tag/xor [[Disgiunzione Esclusiva (XOR)]]

### 1.6 Operatori NAND e NOR

Questi sono interessanti perché *ciascuno* di essi può essere usato per costruire tutti gli altri connettivi logici! Sono chiamati **operatori funzionalmente completi**.

*   **NAND (NOT AND):** È la negazione di AND.
    *   Simbolo: $\uparrow$ (Freccia di Sheffer)
    *   Definizione: $P \uparrow Q \iff \neg (P \land Q)$
*   **NOR (NOT OR):** È la negazione di OR.
    *   Simbolo: $\downarrow$ (Freccia di Peirce)
    *   Definizione: $P \downarrow Q \iff \neg (P \lor Q)$
*   #tag/nand #tag/nor [[Operatore NAND]] [[Operatore NOR]] [[Completezza Funzionale]]

> [!QUESTION] Domanda Rapida: Riesci a vedere perché $(P \land \neg P)$ è una contraddizione usando la tavola di verità? E perché $(P \lor \neg P)$ è una tautologia?

---

## 2. Logica dei Predicati: Parlare di Proprietà e Quantità

A volte, le proposizioni dipendono da variabili. #tag/logica-predicati

### 2.1 Predicati e Variabili

*   **Predicato:** Una proprietà o relazione che coinvolge una o più variabili. Diventa una proposizione (V o F) quando alle variabili viene assegnato un valore specifico da un certo **universo del discorso** (dominio).
    *   Esempio (dalle tue note!): $P(x): x > 10$.
        *   Qui $P(x)$ è il predicato. $x$ è la **variabile**.
        *   Se l'universo sono i numeri interi $\mathbb{Z}$:
            *   $P(12)$ (cioè $12 > 10$) è VERA.
            *   $P(2)$ (cioè $2 > 10$) è FALSA.
    *   [[Predicato]] [[Variabile]] [[Universo del Discorso]]
*   **Formula Ben Formata (FBF):** Un'espressione costruita correttamente usando variabili, predicati, connettivi logici e quantificatori (vedi sotto). Le tue note mostrano esempi come "$3+x=10$" o "$x+3 > 10$", che sono predicati (o formule aperte). L'esempio "$3++x-=$" non è ben formato. [[Formula Ben Formata (FBF)]]

### 2.2 Quantificatori

I quantificatori ci dicono *quanti* elementi nell'universo soddisfano un predicato. [[Quantificatori]]

*   **Quantificatore Universale (PER OGNI):** Afferma che il predicato è vero per *tutti* gli elementi dell'universo.
    *   Simbolo: $\forall$ (si legge "per ogni" o "per tutti")
    *   Esempio: $\forall x \in \mathbb{R}, x^2 \ge 0$ ("Per ogni numero reale x, il suo quadrato è maggiore o uguale a zero").
    *   Nelle tue note: $\forall x (x>1)$ (Questa affermazione dipende dall'universo! Se l'universo sono i numeri reali $\mathbb{R}$, è Falsa. Se l'universo sono i numeri reali maggiori di 1, $(1, +\infty)$, è Vera).
    *   #tag/quantificatore-universale [[Quantificatore Universale]]

*   **Quantificatore Esistenziale (ESISTE ALMENO UN):** Afferma che il predicato è vero per *almeno un* elemento dell'universo.
    *   Simbolo: $\exists$ (si legge "esiste almeno un" o "per qualche")
    *   Esempio: $\exists x \in \mathbb{R}, x^2 = 4$ ("Esiste almeno un numero reale x il cui quadrato è 4" - Vero, x=2 e x=-2).
    *   #tag/quantificatore-esistenziale [[Quantificatore Esistenziale]]

*   **Quantificatore Esistenziale Unico (ESISTE UN UNICO):** Afferma che il predicato è vero per *esattamente un* elemento dell'universo.
    *   Simbolo: $\exists !$ (si legge "esiste un unico")
    *   Definizione (dalle tue note!): $\exists ! x P(x) \iff \exists x ( P(x) \land \forall y (P(y) \implies x=y) )$
        *   **Spiegazione Semplice:** "Esiste un x che ha la proprietà P, e se qualcos'altro (y) ha la proprietà P, allora quel qualcos'altro deve essere proprio x".
    *   #tag/quantificatore-unico [[Quantificatore di Unicità]]

### 2.3 Variabili Libere e Vincolate, Formule Chiuse

*   **Variabile Vincolata:** Una variabile che è "controllata" da un quantificatore ($\forall$ o $\exists$) che agisce su di essa.
*   **Variabile Libera:** Una variabile che non è vincolata da nessun quantificatore.
*   **Formula Aperta:** Una formula che contiene almeno una variabile libera. Il suo valore di verità dipende dal valore assegnato alle variabili libere (es. $x > 10$).
*   **Formula Chiusa (o Enunciato):** Una formula che non contiene variabili libere. Ha un valore di verità definito (V o F) indipendentemente da assegnazioni esterne (es. $\forall x (x > 1)$, $\exists x (x > 10)$).

> [!NOTE] Esempio dalle tue note (Pagina 17):
> *   `a: x > 1` (Formula aperta, $x$ è libera)
> *   `b: ∀x(x > 1)` (Formula chiusa, $x$ è vincolata da $\forall$)
> *   `c: ∀x(x > 1) ∧ x = 7` (Questa è un po' ambigua come scritta. Probabilmente si intende `(∀y(y > 1)) ∧ (x = 7)`. Qui, la $y$ nel primo pezzo è vincolata (ho cambiato nome per chiarezza), ma la $x$ nel secondo pezzo è libera. Quindi è una formula aperta.)
> Se sostituiamo $x=3$ in `a`, otteniamo $3 > 1$ (Vero).
> Se sostituiamo $x=3$ in `c` (nell'interpretazione sopra), otteniamo $(∀y(y > 1)) \land (3 = 7)$. Il valore di verità di $(∀y(y > 1))$ dipende dall'universo scelto per $y$. Ma poiché $(3 = 7)$ è Falso, l'intera congiunzione $\land$ sarà Falsa, indipendentemente dal primo pezzo.
*   [[Variabile Libera]] [[Variabile Vincolata]] [[Formula Aperta]] [[Formula Chiusa]]

---

## 3. Teoria degli Insiemi: Collezioni di Oggetti

Un **insieme** è una collezione di oggetti distinti (senza ordine e senza ripetizioni), chiamati **elementi**. #tag/settheory [[Teoria degli Insiemi]]

*   Notazione: $A = \{a, b, c\}$, $x \in A$ (x è un elemento di A), $y \notin A$ (y non è un elemento di A).
*   **Insieme Vuoto:** L'insieme che non contiene alcun elemento. Simbolo: $\emptyset$ (o $\{\}$). [[Insieme Vuoto]]
*   **Sottoinsieme:** $S \subseteq A$ significa che ogni elemento di $S$ è anche un elemento di $A$. [[Sottoinsieme]]

### 3.1 Prodotto Cartesiano

Dati due insiemi A e B, il loro prodotto cartesiano è l'insieme di tutte le **coppie ordinate** $(a, b)$ dove $a$ proviene da A e $b$ proviene da B.

*   Simbolo: $A \times B$
*   Definizione (dalle tue note!): $A \times B = \{ (a, b) \mid a \in A \land b \in B \}$
*   Esempio (dalle tue note!): Se $A = \{a, b, c\}$ e $B = \{1, 2, 3, 4\}$, allora $A \times B$ contiene coppie come $(a, 1), (b, 3), (c, 4)$, ecc. In totale $|A| \times |B| = 3 \times 4 = 12$ coppie.
    *   Nota: L'ordine conta! $(a, 1) \in A \times B$, ma $(1, a) \notin A \times B$ (a meno che $1 \in A$ e $a \in B$). $(1, a) \in B \times A$.
*   Proprietà (dalle tue note!): $A \times B = \emptyset \iff A = \emptyset \lor B = \emptyset$. (Il prodotto cartesiano è vuoto se e solo se almeno uno dei due insiemi è vuoto).
*   #tag/prodotto-cartesiano [[Prodotto Cartesiano]]

### 3.2 Relazioni

Una **relazione** (o corrispondenza) $\rho$ tra un insieme A (dominio o insieme di partenza) e un insieme B (codominio o insieme di arrivo) è semplicemente un **sottoinsieme** del prodotto cartesiano $A \times B$.

*   Notazione: $\rho \subseteq A \times B$. Spesso si indica una relazione con il suo **grafo**, cioè l'insieme delle coppie $G = \rho \subseteq A \times B$.
*   Si scrive $a \rho b$ o $(a, b) \in G$ per dire che $a$ è in relazione con $b$.
*   Esempio (dalle tue note!): $A = \{a, b, c\}$, $B = \{1, 2, 3, 4\}$.
    *   $S = \{(a, 1), (b, 4)\}$ è una relazione tra A e B. Qui, $a$ è in relazione con $1$, e $b$ è in relazione con $4$. $c$ non è in relazione con nessuno, e $2, 3$ non sono in relazione con nessuno tramite $S$.
    *   $T = \{(a, 1), (b, 1), (a, 4), (b, 4)\}$ è un'altra relazione. Qui $a$ è in relazione sia con $1$ che con $4$.
*   #tag/relazione [[Relazione Binaria]] [[Grafo di una Relazione]]

### 3.3 Funzioni (o Applicazioni)

Una **funzione** $f$ da A a B è un tipo *speciale* di relazione in cui **ogni** elemento di A è associato a **esattamente un** elemento di B.

*   Notazione: $f: A \to B$
*   Definizione formale (usando il grafo $G \subseteq A \times B$):
    1.  **Dominio totale (Esistenza):** Per ogni $a \in A$, esiste almeno un $b \in B$ tale che $(a, b) \in G$. ($\forall a \in A, \exists b \in B : (a,b) \in G$)
    2.  **Univalenza (Unicità):** Per ogni $a \in A$, se $(a, b_1) \in G$ e $(a, b_2) \in G$, allora $b_1 = b_2$. ($\forall a \in A, \forall b_1, b_2 \in B : ((a,b_1) \in G \land (a,b_2) \in G) \implies b_1=b_2$)
*   Combinando le due condizioni (dalle tue note!): $\forall a \in A, \exists ! b \in B \text{ tale che } (a, b) \in G$.
*   Notazione funzionale: Se $(a, b) \in G$, scriviamo $f(a) = b$. $b$ è detta **immagine** di $a$ tramite $f$. $a$ è una **controimmagine** di $b$.

> [!IMPORTANT] Differenza Chiave: In una relazione generica, un elemento di A può essere collegato a zero, uno o molti elementi di B. In una funzione, ogni elemento di A *deve* essere collegato a *esattamente un* elemento di B.

*   **Esempi (dalle tue note - Pagine 24-27):**
    *   Consideriamo relazioni $G \subseteq \mathbb{Z} \times \mathbb{Z}$. Quali sono funzioni $f: \mathbb{Z} \to \mathbb{Z}$?
        *   $G_1 = \{(a, b) \mid a = |b|\}$: **NO**. Se $a=1$, $b$ può essere $1$ o $-1$ (manca unicità). Se $a=-1$, non esiste $b$ (manca esistenza).
        *   $G_2 = \{(a, b) \mid |a| = b\}$: **SÌ**. Per ogni $a \in \mathbb{Z}$, $|a|$ è un unico intero $b \ge 0$. $f_2(a) = |a|$.
        *   $G_3 = \{(a, b) \mid |a| = |b|\}$: **NO**. Se $a=1$, $b$ può essere $1$ o $-1$ (manca unicità).
        *   $G_4 = \{(a, b) \mid a^2 = b\}$: **SÌ**. Per ogni $a \in \mathbb{Z}$, $a^2$ è un unico intero $b \ge 0$. $f_4(a) = a^2$.
        *   $G_5 = \{(a, b) \mid a = b^2\}$: **NO**. Se $a=1$, $b$ può essere $1$ o $-1$ (manca unicità). Se $a=-1$ o $a=2$, non esiste $b \in \mathbb{Z}$ (manca esistenza per alcuni $a$).
    *   Consideriamo $A=\{a,b,c\}, B=\{1,2,3\}$.
        *   $G = \{(a,1), (b,1), (c,1)\}$: **SÌ**. È una funzione costante. $f(a)=1, f(b)=1, f(c)=1$.
        *   $G = \{(a,1), (b,2), (a,3)\}$: **NO**. L'elemento $a$ è associato a due valori diversi (1 e 3, manca unicità). Inoltre, $c$ non è associato a nessun valore (manca esistenza).
    *   Consideriamo relazioni $G \subseteq \mathbb{N} \times \mathbb{N}$ (assumiamo $\mathbb{N} = \{1, 2, 3, ...\}$).
        *   $G_1 = \{(a, b) \mid a = 2^b\}$: **NO** (come funzione $f: \mathbb{N} \to \mathbb{N}$). Se $a=3$, non esiste $b \in \mathbb{N}$ tale che $3 = 2^b$. (Manca esistenza per molti $a$).
        *   $G_2 = \{(a, b) \mid b = 2^a\}$: **SÌ**. Per ogni $a \in \mathbb{N}$, $2^a$ è un unico numero naturale $b$. $f_2(a) = 2^a$.
*   #tag/funzione [[Funzione (matematica)]] [[Dominio (matematica)]] [[Codominio]] [[Immagine (matematica)]]

### 3.4 Altre Operazioni e Concetti sugli Insiemi

*   **Unione:** $A \cup B = \{ x \mid x \in A \lor x \in B \}$ (elementi in A OR in B) [[Unione di Insiemi]]
*   **Intersezione:** $A \cap B = \{ x \mid x \in A \land x \in B \}$ (elementi in A AND in B) [[Intersezione di Insiemi]]
*   **Differenza:** $A \setminus B = \{ x \mid x \in A \land x \notin B \}$ (elementi in A ma NOT in B) [[Differenza tra Insiemi]]
*   **Complemento:** $A^c = U \setminus A = \{ x \in U \mid x \notin A \}$ (elementi non in A, rispetto a un universo U) [[Insieme Complementare]]
*   **Differenza Simmetrica (XOR per insiemi):**
    *   Simbolo: $A \Delta B$
    *   Definizione 1 (dalle tue note!): $A \Delta B = (A \setminus B) \cup (B \setminus A)$ (Elementi che sono in A ma non in B, oppure in B ma non in A)
    *   Definizione 2 (equivalente, dalle tue note!): $A \Delta B = (A \cup B) \setminus (A \cap B)$ (Elementi che sono nell'unione, ma non nell'intersezione)
    *   Proprietà (dalle tue note!): La differenza simmetrica è **associativa**: $(A \Delta B) \Delta C = A \Delta (B \Delta C)$. (La dimostrazione può essere complessa, coinvolge l'analisi dei casi o l'uso delle funzioni caratteristiche). #tag/xor-insiemi [[Differenza Simmetrica]] [[Associatività Differenza Simmetrica]]

---

> [!SUMMARY] Riepilogo Veloce
> *   Abbiamo definito i **connettivi logici** ($\neg, \land, \lor, \implies, \iff$) e visto le loro **tavole di verità**.
> *   Abbiamo esplorato **equivalenze logiche** importanti come De Morgan, contrapposizione e l'equivalenza tra implicazione e disgiunzione.
> *   Abbiamo distinto **tautologie** (sempre vere) e **contraddizioni** (sempre false).
> *   Abbiamo introdotto i **predicati** (formule con variabili) e i **quantificatori** ($\forall, \exists, \exists!$) per parlare di quantità.
> *   Abbiamo definito gli **insiemi**, il **prodotto cartesiano** ($A \times B$), le **relazioni** (sottoinsiemi di $A \times B$) e le **funzioni** (relazioni speciali dove ogni input ha un unico output).
> *   Abbiamo visto le operazioni fondamentali tra insiemi ($\cup, \cap, \setminus, \Delta, ^c$).

> [!TIP] Prossimi Passi
> *   Rileggi questi appunti con calma. Ci sono parti che non sono chiare? Usa i link `[[...]]` per creare nuove note o collegarti a note esistenti per approfondire!
> *   Prova a fare qualche esempio tu stesso/a. Crea piccole tavole di verità o elenca gli elementi di un prodotto cartesiano.
> *   Pensa a come questi concetti si collegano. Ad esempio, come useresti i quantificatori per definire l'unione di due insiemi? ($x \in A \cup B \iff (x \in A) \lor (x \in B)$).