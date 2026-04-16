# Lezione 12: Relazioni di Equivalenza, Partizioni e Congruenze

**Data:** 29/04/2025 (come da note)
**Argomenti:** Teorema Fondamentale (Relazioni di Equivalenza $\iff$ Partizioni), Insieme Quoziente, Relazione di Equivalenza indotta da una Funzione, Applicazione Quoziente, Congruenze, Congruenza Modulo m.

#tag/relations #tag/equivalence-relations #tag/partitions #tag/quotient-set #tag/functions #tag/congruence #tag/number-theory #tag/algebra-avanzata

---

## 1. Il Teorema Fondamentale sulle Relazioni di Equivalenza

Questo teorema stabilisce un legame profondo e fondamentale tra due concetti apparentemente distinti: le relazioni di equivalenza e le partizioni di un insieme.

*   **Ricordiamo:**
    *   Una **Relazione di Equivalenza** $\mathcal{R}$ su $S$ è Riflessiva, Simmetrica e Transitiva.
    *   Una **Partizione** $\mathcal{F}$ di $S$ è una famiglia di sottoinsiemi non vuoti, disgiunti a due a due, la cui unione è $S$.
    *   Data una relazione di equivalenza $\mathcal{R}$ su $S$, la **classe di equivalenza** di $a \in S$ è $[a]_{\mathcal{R}} = \{ x \in S \mid x \mathcal{R} a \}$.
    *   L'**insieme quoziente** $S/\mathcal{R}$ è l'insieme di tutte le classi di equivalenza: $S/\mathcal{R} = \{ [a]_{\mathcal{R}} \mid a \in S \}$.

*   **Proprietà delle Classi di Equivalenza (Pag 1):**
    1.  $\forall a \in S, [a]_{\mathcal{R}} \neq \emptyset$ (perché $a \mathcal{R} a$ per riflessività, quindi $a \in [a]_{\mathcal{R}}$).
    2.  $\forall a, b \in S$, o $[a]_{\mathcal{R}} = [b]_{\mathcal{R}}$ (se $a \mathcal{R} b$) oppure $[a]_{\mathcal{R}} \cap [b]_{\mathcal{R}} = \emptyset$ (se $\neg (a \mathcal{R} b)$). Le classi o coincidono o sono disgiunte.
    3.  $\bigcup_{a \in S} [a]_{\mathcal{R}} = S$ (ogni elemento $x \in S$ appartiene almeno alla classe $[x]_{\mathcal{R}}$).

*   **Osservazione Chiave (Pag 1):** Le proprietà 1, 2, 3 delle classi di equivalenza sono esattamente le proprietà che definiscono una **partizione**! L'insieme quoziente $S/\mathcal{R}$ è una partizione di $S$.

> [!THEOREM] Teorema Fondamentale sulle Relazioni di Equivalenza (Pag 2)
> Sia $S$ un insieme non vuoto ($S \neq \emptyset$). Esiste una **corrispondenza biunivoca** tra l'insieme di tutte le relazioni di equivalenza su $S$ e l'insieme di tutte le partizioni di $S$.
>
> i)  **Da Relazione a Partizione:** Se $\mathcal{R}$ è una relazione di equivalenza su $S$, allora l'insieme quoziente $S/\mathcal{R} = \{ [a]_{\mathcal{R}} \mid a \in S \}$ è una partizione di $S$.
> ii) **Da Partizione a Relazione:** Viceversa, se $\mathcal{F}$ è una partizione di $S$, allora la relazione $\mathcal{R}_{\mathcal{F}}$ definita da:
>     $$ x \mathcal{R}_{\mathcal{F}} y \iff \exists A \in \mathcal{F} \text{ tale che } x \in A \land y \in A $$
>     (cioè, $x$ e $y$ sono in relazione se e solo se appartengono allo stesso "pezzo" della partizione $\mathcal{F}$) è una relazione di equivalenza su $S$.
>
> Inoltre, queste due costruzioni sono una l'inversa dell'altra: partendo da $\mathcal{R}$ e costruendo la partizione $S/\mathcal{R}$, la relazione indotta da questa partizione è proprio $\mathcal{R}$. Viceversa, partendo da $\mathcal{F}$ e costruendo $\mathcal{R}_{\mathcal{F}}$, le classi di equivalenza di $\mathcal{R}_{\mathcal{F}}$ sono esattamente gli insiemi della partizione $\mathcal{F}$.

*   **Dimostrazione:**
    *   **i) $\mathcal{R} \implies S/\mathcal{R}$ è partizione:** Già verificato osservando le proprietà delle classi di equivalenza (non vuote, disgiunte o coincidenti, unione fa S).
    *   **ii) $\mathcal{F} \implies \mathcal{R}_{\mathcal{F}}$ è rel. equivalenza (Pag 3):**
        *   **Riflessiva:** $\forall x \in S$. Poiché $\mathcal{F}$ è una partizione, $\bigcup_{A \in \mathcal{F}} A = S$. Quindi $x$ deve appartenere a qualche $A \in \mathcal{F}$. Per definizione, $x \mathcal{R}_{\mathcal{F}} x$. **SÌ**.
        *   **Simmetrica:** Supponiamo $x \mathcal{R}_{\mathcal{F}} y$. Allora $\exists A \in \mathcal{F}$ tale che $x \in A \land y \in A$. Ma allora $y \in A \land x \in A$, il che significa $y \mathcal{R}_{\mathcal{F}} x$. **SÌ**.
        *   **Transitiva:** Supponiamo $x \mathcal{R}_{\mathcal{F}} y$ e $y \mathcal{R}_{\mathcal{F}} z$. Allora $\exists A \in \mathcal{F}$ tale che $x, y \in A$. E $\exists B \in \mathcal{F}$ tale che $y, z \in B$. Poiché $y \in A$ e $y \in B$, l'intersezione $A \cap B$ non è vuota (contiene almeno $y$). Ma i pezzi di una partizione sono disgiunti o coincidenti. Quindi, deve essere $A = B$. Ma allora $x \in A$ e $z \in A(=B)$. Per definizione, $x \mathcal{R}_{\mathcal{F}} z$. **SÌ**.
    *   **Corrispondenza Inversa (Pag 4):** Dobbiamo verificare che $S/\mathcal{R}_{\mathcal{F}} = \mathcal{F}$.
        *   Consideriamo una classe di equivalenza $[a]_{\mathcal{R}_{\mathcal{F}}} = \{ x \in S \mid x \mathcal{R}_{\mathcal{F}} a \}$.
        *   Per definizione di $\mathcal{R}_{\mathcal{F}}$, questo significa $\{ x \in S \mid \exists A \in \mathcal{F} : x \in A \land a \in A \}$.
        *   Poiché $\mathcal{F}$ è una partizione, esiste un unico $A_a \in \mathcal{F}$ tale che $a \in A_a$.
        *   Quindi la condizione diventa $\{ x \in S \mid x \in A_a \}$.
        *   Questo è esattamente l'insieme $A_a$.
        *   Quindi le classi di equivalenza $[a]_{\mathcal{R}_{\mathcal{F}}}$ sono proprio gli insiemi $A_a$ della partizione originale $\mathcal{F}$.

[[Relazione di equivalenza]] [[Partizione di un insieme]] [[Insieme Quoziente]] [[Teorema Fondamentale Relazioni Equivalenza]]

*   **Esempio 1 (Pag 5):** $S = \{0, 1, ..., 20\}$. $\mathcal{F} = \{ \{0\}, \{1, 10\}, \{2, 11, 20\}, \{3, 12\}, \{4, 13\}, \{5, 14\}, \{6, 15\}, \{7, 16\}, \{8, 17\}, \{9, 18\}, \{19\} \}$. (Sembra una partizione basata sulla somma delle cifre modulo qualcosa? O forse solo sulla somma delle cifre?).
    *   La relazione $\mathcal{R}_{\mathcal{F}}$ associata è: $x \mathcal{R}_{\mathcal{F}} y \iff x, y$ appartengono allo stesso blocco di $\mathcal{F}$.
    *   Esempio: $1 \mathcal{R}_{\mathcal{F}} 10$, $2 \mathcal{R}_{\mathcal{F}} 11$, $2 \mathcal{R}_{\mathcal{F}} 20$, $11 \mathcal{R}_{\mathcal{F}} 20$.
    *   Le classi di equivalenza sono i blocchi stessi: $[0]=\{0\}$, $[1]=\{1, 10\}$, $[2]=\{2, 11, 20\}$, etc.
    *   Se la relazione fosse $x \mathcal{R} y \iff \text{somma cifre}(x) = \text{somma cifre}(y)$:
        *   Somma(0)=0 -> {0}
        *   Somma(1)=1, Somma(10)=1 -> {1, 10}
        *   Somma(2)=2, Somma(11)=2, Somma(20)=2 -> {2, 11, 20}
        *   ... corrisponde alla partizione data.
        *   $[7] = \{7, 16\}$. $[1]=[10]$. $[2]=[11]=[20]$.

*   **Esempio 2 (Pag 6):** $S=\{a, b, c, d, e\}$. $\mathcal{F} = \{ \{a\}, \{b, d\}, \{c, e\} \}$.
    *   Questa è una partizione.
    *   La relazione $\mathcal{R}_{\mathcal{F}}$ associata ha le seguenti coppie (oltre a quelle riflessive): $(b,d), (d,b), (c,e), (e,c)$.
    *   Le classi di equivalenza sono: $[a]_{\mathcal{R}_{\mathcal{F}}} = \{a\}$, $[b]_{\mathcal{R}_{\mathcal{F}}} = \{b, d\} = [d]_{\mathcal{R}_{\mathcal{F}}}$, $[c]_{\mathcal{R}_{\mathcal{F}}} = \{c, e\} = [e]_{\mathcal{R}_{\mathcal{F}}}$.
    *   L'insieme quoziente è $S/\mathcal{R}_{\mathcal{F}} = \{ \{a\}, \{b, d\}, \{c, e\} \} = \mathcal{F}$.

---

## 2. Relazione di Equivalenza Indotta da una Funzione

Ogni funzione definisce naturalmente una relazione di equivalenza sul suo dominio.

> [!THEOREM] Teorema (Pag 8): Relazione di Equivalenza Indotta da una Funzione
> Siano $S, T$ insiemi non vuoti e $f: S \to T$ una funzione.
> La relazione $\mathcal{R}_f$ su $S$ definita da:
> $$ x \mathcal{R}_f y \iff f(x) = f(y) $$
> è una **relazione di equivalenza** su $S$.
>
> **Dimostrazione (Pag 11):**
> 1.  **Riflessiva:** $\forall x \in S$. Poiché $f(x)=f(x)$, vale $x \mathcal{R}_f x$. **SÌ**.
> 2.  **Simmetrica:** Supponiamo $x \mathcal{R}_f y$. Allora $f(x)=f(y)$. Ma allora $f(y)=f(x)$, il che significa $y \mathcal{R}_f x$. **SÌ**.
> 3.  **Transitiva:** Supponiamo $x \mathcal{R}_f y$ e $y \mathcal{R}_f z$. Allora $f(x)=f(y)$ e $f(y)=f(z)$. Per transitività dell'uguaglianza in $T$, segue $f(x)=f(z)$. Quindi $x \mathcal{R}_f z$. **SÌ**.

*   **Classi di Equivalenza per $\mathcal{R}_f$:**
    *   $[a]_{\mathcal{R}_f} = \{ x \in S \mid x \mathcal{R}_f a \} = \{ x \in S \mid f(x) = f(a) \}$.
    *   Questa classe è esattamente la **controimmagine** dell'elemento $f(a)$ (visto come singleton $\{f(a)\} \subseteq T$):
        $$ [a]_{\mathcal{R}_f} = \overleftarrow{f}(\{f(a)\}) $$

*   **Esempio 1 (Pag 9):** $f: \mathbb{Z} \to \mathbb{Z}$ con $f(x)=|x|$.
    *   $x \mathcal{R}_f y \iff |x|=|y|$.
    *   $[a]_{\mathcal{R}_f} = \{ x \in \mathbb{Z} \mid |x|=|a| \} = \{a, -a\}$ (se $a \neq 0$).
    *   $[0]_{\mathcal{R}_f} = \{0\}$.
    *   L'insieme quoziente $\mathbb{Z}/\mathcal{R}_f = \{ \{0\}, \{1, -1\}, \{2, -2\}, ... \}$.

*   **Esempio 2 (Pag 10):** $f: \{0, ..., 20\} \to \mathbb{N}$ con $f(x) = \text{somma delle cifre di } x$.
    *   $x \mathcal{R}_f y \iff \text{somma cifre}(x) = \text{somma cifre}(y)$.
    *   Le classi di equivalenza sono i blocchi della partizione vista prima: $[0]=\{0\}$, $[1]=\{1, 10\}$, $[2]=\{2, 11, 20\}$, etc.

[[Relazione di equivalenza indotta da funzione]]

### 2.1 Applicazione Quoziente (Teorema di Fattorizzazione)

C'è un legame tra la funzione originale $f$ e l'insieme quoziente $S/\mathcal{R}_f$.

*   **Teorema (Pag 8, 12-13):** Sia $f: S \to T$ una funzione e $\mathcal{R}_f$ la relazione di equivalenza indotta ($x \mathcal{R}_f y \iff f(x)=f(y)$). Allora esiste un'unica funzione **iniettiva** $\bar{f}$ (detta **applicazione quoziente** o mappa indotta):
    $$ \bar{f}: S/\mathcal{R}_f \to T $$
    definita da:
    $$ \bar{f}([a]_{\mathcal{R}_f}) = f(a) $$
    tale che $f = \bar{f} \circ \pi$, dove $\pi: S \to S/\mathcal{R}_f$ è la **proiezione canonica** $\pi(a) = [a]_{\mathcal{R}_f}$.

*   **Spiegazione:**
    *   La mappa $\bar{f}$ prende un'intera classe di equivalenza $[a]$ e la manda nell'**unico** valore che la funzione $f$ assume su tutti gli elementi di quella classe (cioè $f(a)$).
    *   **Ben definita (Pag 12):** Dobbiamo assicurarci che la definizione di $\bar{f}$ non dipenda dal rappresentante scelto per la classe. Se $[a]_{\mathcal{R}_f} = [b]_{\mathcal{R}_f}$, dobbiamo verificare che $\bar{f}([a]_{\mathcal{R}_f}) = \bar{f}([b]_{\mathcal{R}_f})$.
        *   $[a]_{\mathcal{R}_f} = [b]_{\mathcal{R}_f} \implies a \mathcal{R}_f b \implies f(a) = f(b)$.
        *   Ma $\bar{f}([a]_{\mathcal{R}_f}) = f(a)$ e $\bar{f}([b]_{\mathcal{R}_f}) = f(b)$.
        *   Poiché $f(a)=f(b)$, la definizione è coerente. $\bar{f}$ è ben definita.
    *   **Iniettività di $\bar{f}$ (Pag 13):** Dobbiamo verificare che $\bar{f}([a]_{\mathcal{R}_f}) = \bar{f}([b]_{\mathcal{R}_f}) \implies [a]_{\mathcal{R}_f} = [b]_{\mathcal{R}_f}$.
        *   $\bar{f}([a]_{\mathcal{R}_f}) = \bar{f}([b]_{\mathcal{R}_f}) \implies f(a) = f(b)$.
        *   Per definizione di $\mathcal{R}_f$, $f(a) = f(b) \implies a \mathcal{R}_f b$.
        *   Ma $a \mathcal{R}_f b \implies [a]_{\mathcal{R}_f} = [b]_{\mathcal{R}_f}$.
        *   Quindi $\bar{f}$ è iniettiva.
    *   **Fattorizzazione:** Il diagramma $S \xrightarrow{f} T$ può essere "fattorizzato" come $S \xrightarrow{\pi} S/\mathcal{R}_f \xrightarrow{\bar{f}} T$. Cioè, per andare da $S$ a $T$ con $f$, puoi prima "collassare" $S$ nell'insieme quoziente $S/\mathcal{R}_f$ tramite $\pi$ (mandando ogni elemento nella sua classe), e poi applicare la mappa iniettiva $\bar{f}$ per ottenere il valore in $T$.

*   **Esempio $f(x)=|x|$ (Pag 9):**
    *   $S=\mathbb{Z}$, $T=\mathbb{N}=\{0, 1, ...\}$. $\mathcal{R}_f$ è $x \mathcal{R}_f y \iff |x|=|y|$.
    *   $S/\mathcal{R}_f = \{ [0], [1], [2], ... \}$ dove $[0]=\{0\}$, $[a]=\{a, -a\}$ per $a>0$.
    *   $\bar{f}: S/\mathcal{R}_f \to \mathbb{N}$ è definita da $\bar{f}([a]) = f(a) = |a|$.
    *   $\bar{f}([0]) = |0| = 0$.
    *   $\bar{f}([1]) = |1| = 1$.
    *   $\bar{f}([2]) = |2| = 2$. ...
    *   Questa $\bar{f}$ è chiaramente iniettiva (e anche suriettiva su $\mathbb{N}$, quindi biettiva).

*   **Esercizio (Pag 14):** $S=\{a, b, c\}$. $f: P(S) \to P(S)$ con $f(X) = X \cap \{a, b\}$.
    *   Troviamo le classi di equivalenza $\mathcal{R}_f$. Due sottoinsiemi $X, Y$ sono in relazione se $X \cap \{a, b\} = Y \cap \{a, b\}$.
    *   $P(S) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, S\}$.
    *   $f(\emptyset) = \emptyset \cap \{a, b\} = \emptyset$.
    *   $f(\{c\}) = \{c\} \cap \{a, b\} = \emptyset$.
        *   $[\emptyset]_{\mathcal{R}_f} = \{\emptyset, \{c\}\}$.
    *   $f(\{a\}) = \{a\} \cap \{a, b\} = \{a\}$.
    *   $f(\{a, c\}) = \{a, c\} \cap \{a, b\} = \{a\}$.
        *   $[\{a\}]_{\mathcal{R}_f} = \{\{a\}, \{a, c\}\}$.
    *   $f(\{b\}) = \{b\} \cap \{a, b\} = \{b\}$.
    *   $f(\{b, c\}) = \{b, c\} \cap \{a, b\} = \{b\}$.
        *   $[\{b\}]_{\mathcal{R}_f} = \{\{b\}, \{b, c\}\}$.
    *   $f(\{a, b\}) = \{a, b\} \cap \{a, b\} = \{a, b\}$.
    *   $f(S) = \{a, b, c\} \cap \{a, b\} = \{a, b\}$.
        *   $[\{a, b\}]_{\mathcal{R}_f} = \{\{a, b\}, S\}$.
    *   L'insieme quoziente $P(S)/\mathcal{R}_f$ ha 4 classi:
        *   $C_1 = \{\emptyset, \{c\}\}$
        *   $C_2 = \{\{a\}, \{a, c\}\}$
        *   $C_3 = \{\{b\}, \{b, c\}\}$
        *   $C_4 = \{\{a, b\}, S\}$
    *   La mappa indotta $\bar{f}: P(S)/\mathcal{R}_f \to P(S)$ è:
        *   $\bar{f}(C_1) = f(\emptyset) = \emptyset$.
        *   $\bar{f}(C_2) = f(\{a\}) = \{a\}$.
        *   $\bar{f}(C_3) = f(\{b\}) = \{b\}$.
        *   $\bar{f}(C_4) = f(\{a, b\}) = \{a, b\}$.
        *   Come previsto, $\bar{f}$ è iniettiva.

[[Teorema di Fattorizzazione (Insiemi)]] [[Proiezione Canonica]]

---

## 3. Congruenze

Relazioni di equivalenza "compatibili" con le operazioni algebriche.

*   **Definizione (Pag 18):** Sia $(S, \perp)$ una struttura con un'operazione binaria $\perp$. Una relazione di equivalenza $\mathcal{R}$ su $S$ si dice **congruenza** (o compatibile) rispetto a $\perp$ se:
    $$ \forall a, b, c, d \in S, \quad (a \mathcal{R} c \land b \mathcal{R} d) \implies (a \perp b) \mathcal{R} (c \perp d) $$
    *   **Spiegazione:** Se $a$ è equivalente a $c$, e $b$ è equivalente a $d$, allora il risultato dell'operazione tra $a$ e $b$ deve essere equivalente al risultato dell'operazione tra $c$ e $d$. L'equivalenza "rispetta" l'operazione.

*   **Operazione Quoziente (Pag 20):** Se $\mathcal{R}$ è una congruenza su $(S, \perp)$, allora è possibile definire un'operazione $\perp_{\mathcal{R}}$ sull'insieme quoziente $S/\mathcal{R}$ in modo **ben definito**:
    $$ [a]_{\mathcal{R}} \perp_{\mathcal{R}} [b]_{\mathcal{R}} = [a \perp b]_{\mathcal{R}} $$
    *   **Ben definita (Pag 21):** Se scegliamo altri rappresentanti $[a]_{\mathcal{R}} = [c]_{\mathcal{R}}$ (cioè $a \mathcal{R} c$) e $[b]_{\mathcal{R}} = [d]_{\mathcal{R}}$ (cioè $b \mathcal{R} d$), il risultato non deve cambiare: $[a \perp b]_{\mathcal{R}}$ deve essere uguale a $[c \perp d]_{\mathcal{R}}$. Questo è garantito dalla definizione di congruenza: $a \mathcal{R} c \land b \mathcal{R} d \implies (a \perp b) \mathcal{R} (c \perp d)$, che significa proprio $[a \perp b]_{\mathcal{R}} = [c \perp d]_{\mathcal{R}}$.

*   **Esempi (Pag 19, 22):** Sia $(\mathbb{Z}, +)$.
    *   $\mathcal{R}_1$: $a \mathcal{R}_1 b \iff a, b$ entrambi positivi o entrambi negativi (o zero?). $a, b$ hanno lo stesso segno (considerando 0 a parte?).
        *   È una congruenza rispetto a $+$?
        *   $-1 \mathcal{R}_1 -5$. $3 \mathcal{R}_1 2$.
        *   Dovrebbe valere $(-1+3) \mathcal{R}_1 (-5+2)$, cioè $2 \mathcal{R}_1 -3$.
        *   Ma 2 è positivo e -3 è negativo. Non sono in relazione $\mathcal{R}_1$.
        *   Quindi $\mathcal{R}_1$ **non è una congruenza** rispetto a $+$.
    *   $\mathcal{R}_2$: $a \mathcal{R}_2 b \iff a, b$ entrambi pari o entrambi dispari (stessa parità).
        *   È una congruenza rispetto a $+$?
        *   Supponiamo $a \mathcal{R}_2 c$ (stessa parità) e $b \mathcal{R}_2 d$ (stessa parità).
        *   Dobbiamo verificare $(a+b) \mathcal{R}_2 (c+d)$ (cioè $a+b$ e $c+d$ hanno la stessa parità).
            *   Se a,c pari e b,d pari: a+b pari, c+d pari. OK.
            *   Se a,c pari e b,d dispari: a+b dispari, c+d dispari. OK.
            *   Se a,c dispari e b,d pari: a+b dispari, c+d dispari. OK.
            *   Se a,c dispari e b,d dispari: a+b pari, c+d pari. OK.
        *   **SÌ, $\mathcal{R}_2$ è una congruenza** rispetto a $+$.
    *   È una congruenza rispetto a $\cdot$?
        *   Supponiamo $a \mathcal{R}_2 c$ e $b \mathcal{R}_2 d$. Dobbiamo verificare $(a \cdot b) \mathcal{R}_2 (c \cdot d)$.
            *   Se a,c pari: $ab$ pari, $cd$ pari. OK.
            *   Se a,c dispari e b,d pari: $ab$ pari, $cd$ pari. OK.
            *   Se a,c dispari e b,d dispari: $ab$ dispari, $cd$ dispari. OK.
        *   **SÌ, $\mathcal{R}_2$ è una congruenza** rispetto a $\cdot$.

[[Relazione di congruenza]] [[Operazione quoziente]]

### 3.1 Congruenza Modulo m in $\mathbb{Z}$ (Pag 23-26)

Un esempio fondamentale di congruenza.
*   Sia $m \in \mathbb{Z}$ un intero fissato. Definiamo la relazione $a \equiv b \pmod{m}$ (si legge "a congruo b modulo m") come:
    $$ a \equiv b \pmod{m} \iff m \mid (a-b) $$
    (cioè, $m$ divide la differenza tra $a$ e $b$; equivalente a $a-b = m \cdot h$ per qualche $h \in \mathbb{Z}$).

*   **Teorema:** La congruenza modulo $m$ è una **relazione di equivalenza** su $\mathbb{Z}$.
    *   **Dimostrazione (Pag 23-24):**
        1.  **Riflessiva:** $\forall a \in \mathbb{Z}$. $a-a = 0$. Poiché $m \mid 0$ (perché $0 = m \cdot 0$), vale $a \equiv a \pmod{m}$. **SÌ**.
        2.  **Simmetrica:** Supponiamo $a \equiv b \pmod{m}$. Allora $m \mid (a-b)$. Questo significa $a-b = mh$. Allora $b-a = -(a-b) = m(-h)$. Poiché $-h \in \mathbb{Z}$, $m \mid (b-a)$. Quindi $b \equiv a \pmod{m}$. **SÌ**.
        3.  **Transitiva:** Supponiamo $a \equiv b \pmod{m}$ e $b \equiv c \pmod{m}$. Allora $m \mid (a-b)$ e $m \mid (b-c)$. Cioè $a-b = mh$ e $b-c = mk$ per $h, k \in \mathbb{Z}$. Sommiamo le due equazioni: $(a-b) + (b-c) = mh + mk$. $a-c = m(h+k)$. Poiché $h+k \in \mathbb{Z}$, $m \mid (a-c)$. Quindi $a \equiv c \pmod{m}$. **SÌ**.

*   **Casi Speciali (Pag 25):**
    *   Se $m=0$: $a \equiv b \pmod{0} \iff 0 \mid (a-b)$. L'unico multiplo di 0 è 0 stesso. Quindi $a-b=0 \iff a=b$. La congruenza modulo 0 è la **relazione di uguaglianza**.
    *   Se $m=1$: $a \equiv b \pmod{1} \iff 1 \mid (a-b)$. Poiché 1 divide qualsiasi intero, questo è sempre vero. La congruenza modulo 1 è la **relazione totale**.
    *   $a \equiv b \pmod{m} \iff a \equiv b \pmod{-m}$. (Perché $m \mid (a-b) \iff -m \mid (a-b)$). Possiamo quindi considerare solo $m \ge 0$.

---

### Legame con il Resto della Divisione Euclidea (per $m \ge 2$) (Pagine 26-27)

Prima di enunciare il teorema, ricordiamo brevemente la **Divisione Euclidea**:
Per ogni intero $a$ (dividendo) e ogni intero $m \ge 1$ (divisore), esistono **unici** interi $q$ (quoziente) e $r$ (resto) tali che:
$$ a = m \cdot q + r $$
e
$$ 0 \le r < m $$
Il valore $r$ è denotato come $\text{rest}(a,m)$.

> [!THEOREM] Equivalenza tra Congruenza Modulo m e Uguaglianza dei Resti (Pag 26)
> Siano $a, b \in \mathbb{Z}$ e $m \in \mathbb{Z}$ con $m \ge 2$. Allora:
> $$ a \equiv b \pmod{m} \iff \text{rest}(a, m) = \text{rest}(b, m) $$
> In altre parole, due interi sono congrui modulo $m$ se e solo se hanno lo stesso resto nella divisione euclidea per $m$.

**Dimostrazione:**

*   **Parte 1: $(\implies)$ Dimostriamo che se $a \equiv b \pmod{m}$, allora $\text{rest}(a, m) = \text{rest}(b, m)$.**
    1.  **Ipotesi:** $a \equiv b \pmod{m}$.
        Per definizione, questo significa che $m \mid (a-b)$, quindi esiste un intero $h$ tale che $a-b = m \cdot h$.
    2.  **Divisione Euclidea per $a$ e $b$:**
        Sia $r_1 = \text{rest}(a,m)$ e $r_2 = \text{rest}(b,m)$.
        Allora possiamo scrivere $a = m q_1 + r_1$ e $b = m q_2 + r_2$, dove $q_1, q_2$ sono i rispettivi quozienti e $0 \le r_1 < m$, $0 \le r_2 < m$.
    3.  **Sostituzione nell'ipotesi:**
        Sostituiamo le espressioni di $a$ e $b$ nell'equazione $a-b = mh$:
        $(m q_1 + r_1) - (m q_2 + r_2) = mh$
    4.  **Riorganizzazione algebrica:**
        $m q_1 + r_1 - m q_2 - r_2 = mh$
        $m(q_1 - q_2) + (r_1 - r_2) = mh$
    5.  **Isoliamo la differenza dei resti $(r_1 - r_2)$:**
        $r_1 - r_2 = mh - m(q_1 - q_2)$
        $r_1 - r_2 = m (h - q_1 + q_2)$.
        Poiché $h, q_1, q_2$ sono interi, anche $k = (h - q_1 + q_2)$ è un intero. Quindi, $r_1 - r_2 = mk$.
        Questo mostra che $m \mid (r_1 - r_2)$ (cioè, $r_1-r_2$ è un multiplo di $m$).
    6.  **Consideriamo i limiti per la differenza $r_1 - r_2$:**
        Sappiamo che $0 \le r_1 < m$ e $0 \le r_2 < m$.
        Per trovare l'intervallo di $r_1 - r_2$:
        *   Il valore massimo di $r_1$ è $m-1$, il valore minimo di $r_2$ è $0$. Quindi $r_1 - r_2 \le (m-1) - 0 = m-1$.
        *   Il valore minimo di $r_1$ è $0$, il valore massimo di $r_2$ è $m-1$. Quindi $r_1 - r_2 \ge 0 - (m-1) = -(m-1) = 1-m$.
        Dunque, $-(m-1) \le r_1 - r_2 \le m-1$. Questo significa che $-m < r_1 - r_2 < m$.
    7.  **Conclusione per la Parte 1:**
        Abbiamo stabilito che $r_1 - r_2$ è un multiplo di $m$ e che $-m < r_1 - r_2 < m$.
        L'unico multiplo di $m$ che si trova strettamente tra $-m$ e $m$ è $0 \cdot m = 0$.
        Pertanto, deve essere $r_1 - r_2 = 0$, il che implica $r_1 = r_2$.
        Quindi, $\text{rest}(a, m) = \text{rest}(b, m)$.

*   **Parte 2: $(\impliedby)$ Dimostriamo che se $\text{rest}(a, m) = \text{rest}(b, m)$, allora $a \equiv b \pmod{m}$.**
    1.  **Ipotesi:** $\text{rest}(a, m) = \text{rest}(b, m)$. Chiamiamo $r$ questo resto comune, con $0 \le r < m$.
    2.  **Divisione Euclidea per $a$ e $b$:**
        Possiamo scrivere $a = m q_1 + r$ per qualche intero $q_1$.
        E possiamo scrivere $b = m q_2 + r$ for qualche intero $q_2$.
    3.  **Calcoliamo la differenza $a-b$:**
        $a-b = (m q_1 + r) - (m q_2 + r)$
        $a-b = m q_1 + r - m q_2 - r$
        $a-b = m q_1 - m q_2$
    4.  **Mettiamo $m$ in evidenza:**
        $a-b = m (q_1 - q_2)$.
    5.  **Conclusione per la Parte 2:**
        Poiché $q_1$ e $q_2$ sono interi, la loro differenza $k = (q_1 - q_2)$ è anch'essa un intero.
        Quindi, $a-b = mk$, il che significa che $a-b$ è un multiplo di $m$.
        Per definizione di divisibilità, $m \mid (a-b)$.
        E per definizione di congruenza, $a \equiv b \pmod{m}$.

Avendo dimostrato entrambe le direzioni $(\implies)$ e $(\impliedby)$, il teorema è provato.

**Implicazioni per le Classi di Equivalenza:**
Questo teorema implica che le classi di equivalenza modulo $m$ (per $m \ge 2$) sono determinate unicamente dal resto della divisione per $m$. Ci sono $m$ resti possibili: $0, 1, \dots, m-1$. Di conseguenza, ci sono esattamente $m$ classi di equivalenza distinte modulo $m$, spesso denotate come $[0]_m, [1]_m, \dots, [m-1]_m$. L'insieme di queste classi, $\mathbb{Z}_m = \{[0]_m, [1]_m, \dots, [m-1]_m\}$, è l'insieme quoziente.

---

### Congruenza Modulo m come Relazione di Congruenza

La relazione di congruenza modulo $m$ non è solo una relazione di equivalenza, ma è anche una **congruenza** rispetto alle operazioni di addizione e moltiplicazione definite su $\mathbb{Z}$. Questo è un risultato cruciale.

> [!THEOREM] Compatibilità della Congruenza Modulo m con Addizione e Moltiplicazione
> Siano $a, b, c, d \in \mathbb{Z}$ e $m \in \mathbb{Z}$ con $m \neq 0$. Se
> *   $a \equiv c \pmod{m}$
> *   $b \equiv d \pmod{m}$
>
> Allora valgono le seguenti proprietà:
> 1.  **Compatibilità con l'Addizione:**
>     $$ a+b \equiv c+d \pmod{m} $$
> 2.  **Compatibilità con la Moltiplicazione:**
>     $$ a \cdot b \equiv c \cdot d \pmod{m} $$

**Dimostrazione:**

1.  **Dimostrazione della Compatibilità con l'Addizione:**
    *   **Ipotesi:**
        *   $a \equiv c \pmod{m} \implies m \mid (a-c) \implies a-c = k_1 m$ per qualche $k_1 \in \mathbb{Z}$.
        *   $b \equiv d \pmod{m} \implies m \mid (b-d) \implies b-d = k_2 m$ per qualche $k_2 \in \mathbb{Z}$.
    *   **Tesi:** Dobbiamo dimostrare che $a+b \equiv c+d \pmod{m}$, cioè che $m \mid ((a+b) - (c+d))$.
    *   Consideriamo la differenza $(a+b) - (c+d)$:
        $(a+b) - (c+d) = a+b-c-d = (a-c) + (b-d)$.
    *   Sostituiamo le espressioni dalle ipotesi:
        $(a-c) + (b-d) = k_1 m + k_2 m$.
    *   Mettiamo $m$ in evidenza:
        $k_1 m + k_2 m = m(k_1 + k_2)$.
    *   Poiché $k_1, k_2 \in \mathbb{Z}$, anche $(k_1+k_2) \in \mathbb{Z}$.
    *   Quindi, $(a+b) - (c+d)$ è un multiplo di $m$.
    *   Questo significa $m \mid ((a+b) - (c+d))$, e dunque $a+b \equiv c+d \pmod{m}$.
    La compatibilità con l'addizione è dimostrata.

2.  **Dimostrazione della Compatibilità con la Moltiplicazione:**
    *   **Ipotesi:** (Come sopra)
        *   $a-c = k_1 m \implies a = c + k_1 m$.
        *   $b-d = k_2 m \implies b = d + k_2 m$.
    *   **Tesi:** Dobbiamo dimostrare che $a \cdot b \equiv c \cdot d \pmod{m}$, cioè che $m \mid (ab - cd)$.
    *   Consideriamo la differenza $ab - cd$. Usiamo un trucco: aggiungere e sottrarre $bc$ (o $ad$):
        $ab - cd = ab - bc + bc - cd$.
    *   Raccogliamo:
        $ab - bc + bc - cd = b(a-c) + c(b-d)$.
    *   Sostituiamo le espressioni dalle ipotesi:
        $b(k_1 m) + c(k_2 m)$.
    *   Mettiamo $m$ in evidenza:
        $m(bk_1 + ck_2)$.
    *   Poiché $b, k_1, c, k_2 \in \mathbb{Z}$, anche $(bk_1 + ck_2) \in \mathbb{Z}$.
    *   Quindi, $ab - cd$ è un multiplo di $m$.
    *   Questo significa $m \mid (ab - cd)$, e dunque $a \cdot b \equiv c \cdot d \pmod{m}$.
    La compatibilità con la moltiplicazione è dimostrata.

Questa proprietà di essere una congruenza è ciò che permette di definire in modo **ben definito** le operazioni di somma e prodotto sull'insieme quoziente $\mathbb{Z}_m = \mathbb{Z}/\equiv_m$ (l'insieme delle classi di resto modulo $m$). Si definisce:
*   $[a]_m + [b]_m = [a+b]_m$
*   $[a]_m \cdot [b]_m = [a \cdot b]_m$

L'insieme $\mathbb{Z}_m$ con queste operazioni forma una nuova e fondamentale struttura algebrica (un anello commutativo unitario).

[[Congruenza (teoria dei numeri)]] [[Aritmetica modulare]] [[Anello Zn]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 12
> *   Il **Teorema Fondamentale** stabilisce una corrispondenza 1:1 tra **relazioni di equivalenza** su $S$ e **partizioni** di $S$. La partizione associata a $\mathcal{R}$ è l'insieme quoziente $S/\mathcal{R}$. La relazione associata a $\mathcal{F}$ è $x \mathcal{R}_{\mathcal{F}} y \iff x, y$ appartengono allo stesso blocco di $\mathcal{F}$.
> *   Ogni **funzione** $f: S \to T$ induce una relazione di equivalenza $\mathcal{R}_f$ su $S$ ($x \mathcal{R}_f y \iff f(x)=f(y)$).
> *   Esiste una **mappa quoziente iniettiva** $\bar{f}: S/\mathcal{R}_f \to T$ tale che $\bar{f}([a]) = f(a)$.
> *   Una **congruenza** è una relazione di equivalenza compatibile con un'operazione algebrica.
> *   La **congruenza modulo m** ($a \equiv b \pmod{m} \iff m \mid (a-b)$) è una relazione di equivalenza su $\mathbb{Z}$.
> *   Per $m \ge 2$, $a \equiv b \pmod{m} \iff \text{rest}(a, m) = \text{rest}(b, m)$.

> [!TIP] Prossimi Passi
> *   Assicurati di aver compreso il legame tra relazioni di equivalenza, classi di equivalenza e partizioni.
> *   Rifletti su come la relazione indotta da una funzione "raggruppa" gli elementi del dominio che hanno la stessa immagine.
> *   La congruenza modulo m è fondamentale. Il prossimo passo sarà studiare la struttura dell'insieme quoziente $\mathbb{Z}_m$ (l'anello delle classi di resto modulo m).
