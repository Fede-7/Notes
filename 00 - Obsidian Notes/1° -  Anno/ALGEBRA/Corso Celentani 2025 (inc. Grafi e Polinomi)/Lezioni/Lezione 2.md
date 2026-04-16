# Lezione 2: Logica Avanzata, Funzioni e Partizioni

**Data:** 14/03/2025 (come da note)
**Argomenti:** Tautologie (implicazione, bicondizionale), Analisi argomentazioni, Negazione e ordine quantificatori, Immagine e Controimmagine di funzioni, Funzioni Iniettive, Partizioni.

#tag/logica #tag/logica-predicati #tag/quantificatori #tag/settheory #tag/functions #tag/injectivity #tag/partitions #tag/algebra-avanzata

---

## 1. Ancora Qualche Tautologia e Equivalenza Logica

Riprendiamo e approfondiamo alcune importanti leggi logiche.

*   **Non-Associatività dell'Implicazione:**
    > [!WARNING] Attenzione! L'implicazione **NON** è associativa in generale.
    > $(a \implies b) \implies c$ **NON** è logicamente equivalente a $a \implies (b \implies c)$.
    > [[Non-Associatività Implicazione]]

*   **Transitività dell'Implicazione (Sillogismo Ipotetico):** (Già visto, ma fondamentale!)
    *   Formula: $((a \implies b) \land (b \implies c)) \implies (a \implies c)$
    *   Questa formula è una **tautologia**. Significa: Se $a$ implica $b$, e $b$ implica $c$, allora $a$ implica $c$.
    *   *Dimostrazione alternativa (usando equivalenza $P \implies Q \iff \neg P \lor Q$):*
        1.  Partiamo da: $((a \implies b) \land (b \implies c))$
        2.  Sostituiamo le implicazioni: $((\neg a \lor b) \land (\neg b \lor c))$
        3.  Vogliamo dimostrare che questo implica $(a \implies c)$, cioè $(\neg a \lor c)$.
        4.  L'intera espressione è: $((\neg a \lor b) \land (\neg b \lor c)) \implies (\neg a \lor c)$
        5.  Questa implicazione è una tautologia (si può verificare con tavola di verità o altri metodi come la risoluzione). L'idea intuitiva è che se valgono le premesse, o $\neg a$ è vera (e quindi $\neg a \lor c$ è vera), oppure $a$ è vera. Se $a$ è vera, dalla prima premessa $(\neg a \lor b)$ otteniamo $b$. Dalla seconda premessa $(\neg b \lor c)$ otteniamo $c$. Quindi in ogni caso otteniamo $(\neg a \lor c)$.
    *   [[Legge di Transitività (Sillogismo Ipotetico)]]

*   **Bicondizionale come Doppia Implicazione:**
    *   Formula: $(a \iff b) \iff ((a \implies b) \land (b \implies a))$
    *   Questa è una **tautologia** e spesso è la *definizione* del bicondizionale. Significa che $a \iff b$ è vero se e solo se $a$ implica $b$ E $b$ implica $a$.

**Verifica Equivalenza (Bicondizionale $\iff$ Doppia Implicazione):**

| $a$ | $b$ | $a \iff b$ | $a \implies b$ | $b \implies a$ | $(a \implies b) \land (b \implies a)$ | $(a \iff b) \iff ((a \implies b) \land (b \implies a))$ |
| :--: | :--: | :--------: | :----------: | :----------: | :-------------------------------: | :-------------------------------------------------: |
| V | V | V | V | V | V | V |
| V | F | F | F | V | F | V |
| F | V | F | V | F | F | V |
| F | F | V | V | V | V | V |

*   [[Bicondizionale]]

*   **Contrapposizione (Ripasso):**
    *   Formula: $(a \implies b) \iff (\neg b \implies \neg a)$
    *   Questa è una **tautologia** fondamentale. Un'implicazione è equivalente alla sua contrapposta.

**Verifica Equivalenza (Implicazione $\iff$ Contrapposta):** (Già vista, ma utile ripeterla)

| $a$ | $b$ | $a \implies b$ | $\neg b$ | $\neg a$ | $\neg b \implies \neg a$ | $(a \implies b) \iff (\neg b \implies \neg a)$ |
| :--: | :--: | :----------: | :------: | :------: | :------------------: | :---------------------------------------: |
| V | V | V | F | F | V | V |
| V | F | F | V | F | F | V |
| F | V | V | F | V | V | V |
| F | F | V | V | V | V | V |

*   [[Legge di Contrapposizione]]

### 1.1 Analisi di un Argomento Logico (Esempio "Multiplo di")

Consideriamo le seguenti proposizioni:
*   $p$: "essere multiplo di 2" (cioè essere pari)
*   $q$: "essere multiplo di 3"
*   $r$: "essere multiplo di 6"

Analizziamo le implicazioni numerate nelle tue note (Pag 4):

1.  **(1) $(p \land q) \implies r$**
    *   Traduzione: "Se un numero è multiplo di 2 E multiplo di 3, allora è multiplo di 6".
    *   **Valore di Verità: VERO**. Questa è una proprietà aritmetica fondamentale (poiché 2 e 3 sono coprimi).

2.  **(2) $(\neg p \land \neg q) \implies \neg r$**
    *   Traduzione: "Se un numero NON è multiplo di 2 E NON è multiplo di 3, allora NON è multiplo di 6".
    *   **Valore di Verità: VERO**. Se non è multiplo di 2, non può essere multiplo di 6. Se non è multiplo di 3, non può essere multiplo di 6. Quindi se non è né multiplo di 2 né di 3, a maggior ragione non è multiplo di 6.
    *   > [!NOTE] Attenzione: Questa **NON** è la contrapposta di (1)! La contrapposta di $(p \land q) \implies r$ è $\neg r \implies \neg (p \land q)$, che per De Morgan diventa $\neg r \implies (\neg p \lor \neg q)$.

3.  **(3) $(\neg p \lor \neg q) \implies \neg r$**
    *   Traduzione: "Se un numero NON è multiplo di 2 OPPURE NON è multiplo di 3, allora NON è multiplo di 6".
    *   **Valore di Verità: VERO**. Se non è multiplo di 2, non può essere multiplo di 6. Se non è multiplo di 3, non può essere multiplo di 6. Quindi, se vale almeno una delle due negazioni, non può essere multiplo di 6.
    *   > [!TIP] Questa è equivalente alla contrapposta di (1), cioè $\neg r \implies (\neg p \lor \neg q)$. Quindi, poiché (1) è vera, anche (3) deve essere vera.

4.  **(4) $\neg r \implies (\neg p \land \neg q)$**
    *   Traduzione: "Se un numero NON è multiplo di 6, allora NON è multiplo di 2 E NON è multiplo di 3".
    *   **Valore di Verità: FALSO**. Controesempio: il numero 4. Non è multiplo di 6, ma è multiplo di 2 (quindi $\neg p$ è falso). Controesempio: il numero 9. Non è multiplo di 6, ma è multiplo di 3 (quindi $\neg q$ è falso).

5.  **(5) $\neg r \implies (\neg p \lor \neg q)$**
    *   Traduzione: "Se un numero NON è multiplo di 6, allora NON è multiplo di 2 OPPURE NON è multiplo di 3".
    *   **Valore di Verità: VERO**. Questa è la contrapposta di (1) e anche equivalente a (3). Se un numero non è multiplo di 6, significa che gli manca almeno uno dei fattori primi 2 o 3. Quindi o non è multiplo di 2, o non è multiplo di 3 (o entrambi).

> [!SUMMARY] Analisi Argomento
> * L'implicazione (1) è vera per definizione di multiplo di 6.
> * L'implicazione (2) è vera, ma non è legata a (1) da regole semplici come la contrapposizione.
> * L'implicazione (3) è vera ed è equivalente alla contrapposta di (1).
> * L'implicazione (4) è falsa.
> * L'implicazione (5) è vera ed è la contrapposta di (1).

---

## 2. Quantificatori: Negazione e Ordine

Riprendiamo i quantificatori e vediamo come negarli e quanto sia importante il loro ordine.

### 2.1 Variabili Libere e Vincolate (Ripasso con Esempi)

Ricorda: una variabile è **vincolata** se è sotto l'azione di un quantificatore ($\forall$ o $\exists$). Altrimenti è **libera**.

*   Esempio 1 (Pag 6): $(\forall x (x^2 < x)) \lor (|x| > 1)$
    *   Nel primo pezzo `∀x(x² < x)`, la `x` è **vincolata** dal $\forall$.
    *   Nel secondo pezzo `|x| > 1`, la `x` è **libera**.
    *   Poiché c'è una variabile libera, l'intera formula è **aperta**. Il suo valore di verità dipende da cosa sostituiamo alla `x` libera.
    *   Se l'universo è $\mathbb{R}$:
        *   Se $x=5$, la formula diventa $(\forall y (y^2 < y)) \lor (|5| > 1)$. Il primo pezzo è Falso (non tutti i reali $y$ soddisfano $y^2<y$), il secondo è Vero ($5>1$). Falso $\lor$ Vero = **Vero**.
        *   Se $x=0.5$, la formula diventa $(\forall y (y^2 < y)) \lor (|0.5| > 1)$. Il primo pezzo è Falso, il secondo è Falso ($0.5 \ngtr 1$). Falso $\lor$ Falso = **Falso**.

*   Esempio 2 (Pag 7): $\forall x (xy = y)$
    *   La `x` è **vincolata** dal $\forall$.
    *   La `y` è **libera**.
    *   Formula **aperta**. Dipende dal valore di `y`.
    *   Se l'universo è $\mathbb{R}$:
        *   Se $y=0$, diventa $\forall x (x \cdot 0 = 0)$, che è **Vero**.
        *   Se $y=1$, diventa $\forall x (x \cdot 1 = 1)$, che è **Falso** (vero solo per $x=1$).

*   Esempio 3 (Pag 7): $\forall x (\exists y (xy = y))$
    *   La `x` è **vincolata** dal $\forall$.
    *   La `y` è **vincolata** dal $\exists$.
    *   Non ci sono variabili libere. Formula **chiusa**. Ha un valore di verità definito.
    *   Significato: "Per ogni x, esiste almeno un y tale che xy = y".
    *   Se l'universo è $\mathbb{R}$: **Vero**. Per qualsiasi $x$, possiamo scegliere $y=0$. Allora $x \cdot 0 = 0$, quindi l'uguaglianza è soddisfatta.

### 2.2 Negazione dei Quantificatori (Leggi di De Morgan per Quantificatori)

Come si nega un'affermazione con $\forall$ o $\exists$?

*   **Negazione dell'Universale:** Negare che "tutti hanno una proprietà" significa dire che "esiste almeno uno che NON ha quella proprietà".
    *   Formula: $\neg (\forall x P(x)) \iff \exists x (\neg P(x))$
    *   Esempio: Negare "Tutti gli studenti hanno passato l'esame" ($\forall x S(x)$) significa "Esiste almeno uno studente che NON ha passato l'esame" ($\exists x (\neg S(x))$).

*   **Negazione dell'Esistenziale:** Negare che "esiste almeno uno con una proprietà" significa dire che "tutti NON hanno quella proprietà".
    *   Formula: $\neg (\exists x P(x)) \iff \forall x (\neg P(x))$
    *   Esempio: Negare "Esiste un numero reale il cui quadrato è negativo" ($\exists x (x^2 < 0)$) significa "Per tutti i numeri reali, il loro quadrato NON è negativo" ($\forall x \neg (x^2 < 0)$, cioè $\forall x (x^2 \ge 0)$).

> [!IMPORTANT] Queste regole sono fondamentali per fare dimostrazioni per assurdo o per capire cosa significa falsificare un'affermazione universale o esistenziale.
> [[Negazione dei Quantificatori]]

### 2.3 Ordine dei Quantificatori

L'ordine in cui appaiono quantificatori diversi è **cruciale** e cambia il significato della frase!

Consideriamo un predicato $\varphi(x, y)$ con due variabili.

*   **$\forall x \exists y \, \varphi(x, y)$**: "Per ogni $x$, esiste (almeno) un $y$ (che può dipendere da $x$) tale che $\varphi(x, y)$ è vera."
    *   Esempio (Universo $\mathbb{R}$): $\forall x \exists y (y > x)$. ("Per ogni numero reale x, esiste un numero reale y più grande di x"). **VERO** (basta prendere $y = x+1$). La scelta di $y$ dipende da $x$.

*   **$\exists y \forall x \, \varphi(x, y)$**: "Esiste (almeno) un $y$ (fisso, lo stesso per tutti) tale che per ogni $x$, $\varphi(x, y)$ è vera."
    *   Esempio (Universo $\mathbb{R}$): $\exists y \forall x (y > x)$. ("Esiste un numero reale y che è più grande di tutti i numeri reali x"). **FALSO**. Non esiste un numero reale massimo.

> [!WARNING] In generale: $\exists y \forall x \, \varphi(x, y) \implies \forall x \exists y \, \varphi(x, y)$
> L'implicazione inversa **NON** vale! Se per ogni x trovo un y *diverso*, non è detto che esista un y *unico* che vada bene per tutti gli x.

*   Esempio dalle note (Pag 8): $\varphi(x,y)$ è $x \cdot y = x$. Universo $\mathbb{N} = \{1, 2, 3, ...\}$.
    *   **(1) $\forall x \in \mathbb{N}, \exists y \in \mathbb{N} (x \cdot y = x)$?**
        *   Significato: "Per ogni numero naturale x, esiste un naturale y tale che xy=x".
        *   **VERO**. Basta scegliere $y=1$. $x \cdot 1 = x$ è vero per ogni $x \in \mathbb{N}$.
    *   **(2) $\exists y \in \mathbb{N}, \forall x \in \mathbb{N} (x \cdot y = x)$?**
        *   Significato: "Esiste un numero naturale y (fisso) tale che per tutti i naturali x, si ha xy=x".
        *   **VERO**. Possiamo scegliere $y=1$. Per questo $y$ fisso, vale $x \cdot 1 = x$ per tutti gli $x \in \mathbb{N}$.
    *   In questo caso specifico, entrambe le affermazioni sono vere e quindi equivalenti. Ma non è sempre così!

---

## 3. Funzioni: Immagine e Controimmagine di Insiemi

Data una funzione $f: A \to B$.

### 3.1 Immagine di un Sottoinsieme del Dominio

*   Dato un sottoinsieme $X \subseteq A$, l'**immagine di X tramite f** è l'insieme di tutti gli elementi del codominio $B$ che sono "raggiunti" da almeno un elemento di $X$.
*   Notazione (dalle note): $\vec{f}(X)$ o $f(X)$
*   Definizione Formale: $\vec{f}(X) = \{ f(x) \mid x \in X \}$
*   Proprietà: $\vec{f}(X) \subseteq B$

> [!NOTE] L'immagine $\vec{f}(X)$ contiene i *risultati* della funzione applicata agli elementi di $X$.

*   Esempio (Pag 13): $f: \mathbb{Z} \to \mathbb{Z}$ definita da $f(x) = |x|$. Sia $X = \{-2, 5, -5\}$.
    *   $\vec{f}(X) = \{ f(-2), f(5), f(-5) \} = \{ |-2|, |5|, |-5| \} = \{ 2, 5, 5 \} = \{2, 5\}$. (Ricorda: gli insiemi non hanno ripetizioni).

*   Proprietà (Pag 14): $\vec{f}(\emptyset) = \emptyset$. (L'immagine dell'insieme vuoto è l'insieme vuoto).

*   Esempio (Pag 14): $g: \mathbb{Z} \to \mathbb{N}$ definita da $g(x) = |x|$. (Assumiamo $\mathbb{N} = \{0, 1, 2, ...\}$ qui).
    *   $\vec{g}(\mathbb{Z}) = \{ |x| \mid x \in \mathbb{Z} \} = \{0, 1, 2, 3, ...\} = \mathbb{N}$. (L'immagine dell'intero dominio è l'insieme dei numeri naturali, detto anche **Immagine della funzione**, $Im(g)$).

*   Esempio (Pag 14): $h: \mathbb{Z} \to \mathbb{Z}$ definita da $h(x) = 3$. (Funzione costante).
    *   $\vec{h}(\mathbb{Z}) = \{ h(x) \mid x \in \mathbb{Z} \} = \{ 3 \mid x \in \mathbb{Z} \} = \{3\}$. (L'immagine dell'intero dominio è solo l'elemento 3).

### 3.2 Controimmagine (o Preimmagine) di un Sottoinsieme del Codominio

*   Dato un sottoinsieme $Y \subseteq B$, la **controimmagine (o preimmagine) di Y tramite f** è l'insieme di tutti gli elementi del dominio $A$ le cui immagini cadono dentro $Y$.
*   Notazione (dalle note): $\overleftarrow{f}(Y)$ o $f^{-1}(Y)$ (Attenzione: $f^{-1}$ qui **non** significa funzione inversa! È solo una notazione per la controimmagine).
*   Definizione Formale: $\overleftarrow{f}(Y) = \{ x \in A \mid f(x) \in Y \}$
*   Proprietà: $\overleftarrow{f}(Y) \subseteq A$

> [!NOTE] La controimmagine $\overleftarrow{f}(Y)$ contiene gli *input* della funzione che producono risultati appartenenti a $Y$.

*   Esempio (Pag 13): $f: \mathbb{Z} \to \mathbb{Z}$ definita da $f(x) = |x|$. Sia $Y = \{2, 5\}$.
    *   $\overleftarrow{f}(Y) = \{ x \in \mathbb{Z} \mid f(x) \in \{2, 5\} \} = \{ x \in \mathbb{Z} \mid |x| = 2 \text{ oppure } |x| = 5 \}$
    *   $\overleftarrow{f}(Y) = \{ -2, 2, -5, 5 \}$.

*   Esempio (Pag 13): $f(x)=|x|$. Sia $Y = \{-2\}$.
    *   $\overleftarrow{f}(Y) = \{ x \in \mathbb{Z} \mid f(x) \in \{-2\} \} = \{ x \in \mathbb{Z} \mid |x| = -2 \}$
    *   $\overleftarrow{f}(Y) = \emptyset$. (Nessun intero ha valore assoluto -2).

*   Proprietà (Pag 15): $\overleftarrow{f}(\emptyset) = \emptyset$. (La controimmagine dell'insieme vuoto è l'insieme vuoto).
*   Proprietà (Pag 15): $\overleftarrow{f}(B) = \{ x \in A \mid f(x) \in B \} = A$. (La controimmagine dell'intero codominio è l'intero dominio).

[[Immagine di una Funzione]] [[Controimmagine]]

---

## 4. Funzioni Iniettive (One-to-One)

Una proprietà molto importante delle funzioni.

*   **Definizione Intuitiva:** Una funzione è **iniettiva** se manda elementi distinti del dominio in elementi distinti del codominio. Non "schiaccia" mai due input diversi sullo stesso output.
*   **Definizione Formale:** Una funzione $f: A \to B$ è iniettiva se:
    $$
    \forall x_1, x_2 \in A, \quad f(x_1) = f(x_2) \implies x_1 = x_2
    $$
    *   **Spiegazione:** Se prendi due elementi qualsiasi nel dominio, $x_1$ e $x_2$, e scopri che hanno la stessa immagine ($f(x_1) = f(x_2)$), allora devi concludere che stavi guardando lo stesso elemento fin dall'inizio ($x_1 = x_2$).

*   **Forma Contrapposta (Spesso utile per le dimostrazioni):**
    $$
    \forall x_1, x_2 \in A, \quad x_1 \neq x_2 \implies f(x_1) \neq f(x_2)
    $$
    *   **Spiegazione:** Se prendi due elementi *distinti* nel dominio, allora le loro immagini devono essere *distinte*.

*   **Negazione (Come dimostrare che una funzione NON è iniettiva):**
    $$
    \exists x_1, x_2 \in A : x_1 \neq x_2 \land f(x_1) = f(x_2)
    $$
    *   **Spiegazione:** Basta trovare *almeno una coppia* di elementi distinti nel dominio che vengono mandati dalla funzione nello stesso elemento del codominio.

*   **Caratterizzazione tramite Controimmagine (Molto utile! Pag 17-18):**
    Una funzione $f: A \to B$ è iniettiva se e solo se per ogni elemento $b$ del codominio $B$, la sua controimmagine $\overleftarrow{f}(\{b\})$ contiene **al massimo un elemento**.
    $$
    f \text{ è iniettiva} \iff (\forall b \in B, |\overleftarrow{f}(\{b\})| \le 1)
    $$
    *   **Spiegazione:** Se una funzione fosse non iniettiva, esisterebbero $x_1 \neq x_2$ con $f(x_1)=f(x_2)=b$. Ma allora la controimmagine di $b$, $\overleftarrow{f}(\{b\})$, conterrebbe sia $x_1$ che $x_2$, e quindi avrebbe cardinalità $\ge 2$. Viceversa, se la controimmagine di ogni $b$ ha al massimo un elemento, non possono esistere due $x$ distinti che mappano allo stesso $b$.

> [!TIP] Per dimostrare che $f$ è iniettiva, parti da $f(x_1)=f(x_2)$ e cerca di dedurre $x_1=x_2$.
> Per dimostrare che $f$ NON è iniettiva, trova due $x_1 \neq x_2$ specifici tali che $f(x_1)=f(x_2)$.

[[Funzione Iniettiva]]

### 4.1 Esempi di Iniettività

*   **Esempio 1 (Pag 19):** $f: \mathbb{N} \setminus \{0, 1\} \to \mathbb{N}$, dove $a = p_1^{n_1} \cdots p_t^{n_t}$ (fattorizzazione unica in primi) e $f(a) = n_1 + n_2 + \dots + n_t$ (somma degli esponenti).
    *   È iniettiva? **NO**.
    *   Controesempio: $a=4=2^2$, $f(4)=2$. $a=6=2^1 \cdot 3^1$, $f(6)=1+1=2$.
    *   Abbiamo $4 \neq 6$ ma $f(4) = f(6) = 2$.

*   **Esempio 2 (Pag 21):** $A=\{1, 2, 3\}$. $f: A \times A \to \mathbb{N}$ definita da $f((a, b)) = a^b$.
    *   È iniettiva? **NO**.
    *   Controesempio (dalle note): $(1, 1) \neq (1, 2)$. Ma $f((1, 1)) = 1^1 = 1$ e $f((1, 2)) = 1^2 = 1$.
    *   Quindi $f((1, 1)) = f((1, 2))$.

*   **Esempio 3 (Pag 22):** $f: \mathbb{N} \to \mathbb{N}$ (qui $\mathbb{N}=\{0, 1, 2, ...\}$ probabilmente)
    $$
    f(n) = \begin{cases} 2n & \text{se } n \text{ è dispari} \\ n & \text{se } n \text{ è pari} \end{cases}
    $$
    *   È iniettiva? **NO**.
    *   Controesempio: $n=1$ (dispari), $f(1) = 2 \cdot 1 = 2$. $n=2$ (pari), $f(2) = 2$.
    *   Abbiamo $1 \neq 2$ ma $f(1) = f(2) = 2$.

*   **Esempio 4 (Pag 23-24):** $f: \mathbb{N} \to \mathbb{Z}$ (qui $\mathbb{N}=\{0, 1, 2, ...\}$ probabilmente)
    $$
    f(n) = \begin{cases} n/2 & \text{se } n \text{ è pari} \\ -(n+1)/2 & \text{se } n \text{ è dispari} \end{cases}
    $$
    *   È iniettiva? **SÌ**. Dimostriamolo per casi, partendo da $f(n)=f(m)$.
        *   **Caso 1:** $n, m$ entrambi pari. $f(n)=n/2$, $f(m)=m/2$. Se $n/2 = m/2$, allora $n=m$. OK.
        *   **Caso 2:** $n, m$ entrambi dispari. $f(n)=-(n+1)/2$, $f(m)=-(m+1)/2$. Se $-(n+1)/2 = -(m+1)/2$, allora $(n+1)/2 = (m+1)/2$, quindi $n+1=m+1$, e $n=m$. OK.
        *   **Caso 3:** $n$ pari, $m$ dispari. $f(n)=n/2$, $f(m)=-(m+1)/2$. Se $f(n)=f(m)$, allora $n/2 = -(m+1)/2$. Poiché $n \ge 0$, $n/2 \ge 0$. Poiché $m \ge 0$ e dispari, $m+1 > 0$, quindi $-(m+1)/2 < 0$. Non è possibile che $n/2 = -(m+1)/2$. Questo caso non può verificarsi se $f(n)=f(m)$. OK.
    *   In tutti i casi possibili in cui $f(n)=f(m)$, abbiamo dedotto che $n=m$. Quindi la funzione è iniettiva.

*   **Esempio 5 (Pag 25):** Sia $S$ un insieme non vuoto. $f: P(S) \to P(S)$ definita da $f(X) = S \setminus X$ (complemento relativo a S).
    *   È iniettiva? **SÌ**.
    *   Dimostrazione: Supponiamo $f(X) = f(Y)$. Questo significa $S \setminus X = S \setminus Y$. Vogliamo dimostrare che $X=Y$.
    *   Prendiamo il complemento rispetto a $S$ di entrambi i lati: $S \setminus (S \setminus X) = S \setminus (S \setminus Y)$.
    *   Ma il complemento del complemento di un insieme è l'insieme stesso: $S \setminus (S \setminus A) = A$.
    *   Quindi otteniamo $X = Y$. Poiché $f(X)=f(Y)$ implica $X=Y$, la funzione è iniettiva.

*   **Esempio 6 (Pag 29):** $f: \mathbb{N} \to \mathbb{N}$ (assumiamo $\mathbb{N}=\{0, 1, 2, ...\}$) definita da $f(a) = \text{rest}(a, 3)$ (resto della divisione di $a$ per 3).
    *   È iniettiva? **NO**.
    *   Controesempio: $f(3) = \text{rest}(3, 3) = 0$. $f(6) = \text{rest}(6, 3) = 0$.
    *   Abbiamo $3 \neq 6$ ma $f(3) = f(6) = 0$.

---

## 5. Partizioni di un Insieme

Un modo per "dividere" un insieme in pezzi disgiunti.

*   Sia $S$ un insieme non vuoto ($S \neq \emptyset$).
*   Una **partizione** di $S$ è una **famiglia** (un insieme) $\mathcal{F}$ di sottoinsiemi di $S$ (cioè $\mathcal{F} \subseteq P(S)$) che soddisfa le seguenti tre condizioni:
    1.  **Nessun pezzo è vuoto:** Ogni sottoinsieme nella famiglia $\mathcal{F}$ deve essere non vuoto.
        $$ \forall X \in \mathcal{F}, \quad X \neq \emptyset $$
    2.  **I pezzi sono disgiunti a due a due:** L'intersezione di due sottoinsiemi *distinti* qualsiasi nella famiglia $\mathcal{F}$ deve essere vuota.
        $$ \forall X, Y \in \mathcal{F}, \quad X \neq Y \implies X \cap Y = \emptyset $$
    3.  **I pezzi ricoprono tutto l'insieme:** L'unione di tutti i sottoinsiemi nella famiglia $\mathcal{F}$ deve dare l'insieme originale $S$.
        $$ \bigcup_{X \in \mathcal{F}} X = S $$

> [!NOTE] Immagina di rompere un piatto $S$. I frammenti $X_i$ formano una partizione: nessun frammento è vuoto, due frammenti diversi non si sovrappongono (a parte i bordi, che qui ignoriamo), e rimettendo insieme tutti i frammenti ottieni il piatto originale.

*   **Esempi (Pag 27):** Sia $S = \{a, b, c\}$.
    *   **Partizioni Banali:**
        *   $\mathcal{F}_1 = \{ \{S\} \} = \{ \{a, b, c\} \}$. (Un solo pezzo: l'insieme intero).
        *   $\mathcal{F}_2 = \{ \{a\}, \{b\}, \{c\} \}$. (Ogni pezzo è un singolo elemento).
    *   **Altre Partizioni:**
        *   $\mathcal{F}_3 = \{ \{a\}, \{b, c\} \}$
        *   $\mathcal{F}_4 = \{ \{b\}, \{a, c\} \}$
        *   $\mathcal{F}_5 = \{ \{c\}, \{a, b\} \}$
    *   La famiglia $\mathcal{L} = \{\mathcal{F}_1, \mathcal{F}_2, \mathcal{F}_3, \mathcal{F}_4, \mathcal{F}_5\}$ è l'insieme di *tutte* le possibili partizioni di $S=\{a,b,c\}$.

*   **Esempio Funzione (Pag 28):** Sia $\mathcal{L}$ l'insieme di tutte le partizioni di $S=\{a,b,c\}$. Definiamo $g: \mathcal{L} \to \{1, 2, 3\}$ dove $g(\mathcal{F}) = |\mathcal{F}|$ (la cardinalità della partizione, cioè il numero di pezzi).
    *   $g(\mathcal{F}_1) = |\{\{a, b, c\}\}| = 1$.
    *   $g(\mathcal{F}_2) = |\{\{a\}, \{b\}, \{c\}\}| = 3$.
    *   $g(\mathcal{F}_3) = |\{\{a\}, \{b, c\}\}| = 2$.
    *   $g(\mathcal{F}_4) = |\{\{b\}, \{a, c\}\}| = 2$.
    *   $g(\mathcal{F}_5) = |\{\{c\}, \{a, b\}\}| = 2$.
    *   Consideriamo la controimmagine:
        *   $\overleftarrow{g}(\{1\}) = \{ \mathcal{F} \in \mathcal{L} \mid |\mathcal{F}| = 1 \} = \{ \mathcal{F}_1 \}$.
        *   $\overleftarrow{g}(\{2\}) = \{ \mathcal{F} \in \mathcal{L} \mid |\mathcal{F}| = 2 \} = \{ \mathcal{F}_3, \mathcal{F}_4, \mathcal{F}_5 \}$.
        *   $\overleftarrow{g}(\{3\}) = \{ \mathcal{F} \in \mathcal{L} \mid |\mathcal{F}| = 3 \} = \{ \mathcal{F}_2 \}$.
        *   $\overleftarrow{g}(\{0\}) = \emptyset$.

[[Partizione di un insieme]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 2
> *   Abbiamo rivisto tautologie importanti come la **transitività** e la **contrapposizione** dell'implicazione, e l'equivalenza del **bicondizionale**.
> *   Abbiamo analizzato un'argomentazione logica concreta.
> *   Abbiamo imparato a **negare i quantificatori** ($\neg \forall \iff \exists \neg$, $\neg \exists \iff \forall \neg$).
> *   Abbiamo visto l'importanza cruciale dell'**ordine dei quantificatori**.
> *   Abbiamo definito l'**immagine** $\vec{f}(X)$ e la **controimmagine** $\overleftarrow{f}(Y)$ di insiemi tramite una funzione $f$.
> *   Abbiamo definito la **funzione iniettiva** (diversi input $\implies$ diversi output) e visto diversi modi per caratterizzarla (definizione formale, contrapposta, negazione, tramite controimmagine di singleton).
> *   Abbiamo introdotto il concetto di **partizione** di un insieme (divisione in pezzi non vuoti e disgiunti che ricoprono tutto).

> [!TIP] Prossimi Passi
> *   Assicurati di aver compreso bene la differenza tra immagine e controimmagine. Prova a calcolarle per funzioni semplici.
> *   Fai pratica nel dimostrare se una funzione è iniettiva o meno. Trovare un controesempio è spesso il modo più rapido per dimostrare la non-iniettività.
> *   Rifletti sul legame tra partizioni e relazioni di equivalenza (lo vedremo presto!).