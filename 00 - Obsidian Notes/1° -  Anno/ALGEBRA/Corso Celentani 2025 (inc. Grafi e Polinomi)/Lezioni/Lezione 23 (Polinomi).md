# Lezione (Bonus) 23: Il Mondo dei Polinomi

#tag/algebra #tag/polinomi #tag/lezione23

---

### Indice della Lezione
1.  [[Lezione 23 (Polinomi)#Definizioni di Base sui Polinomi]]
2.  [[Lezione 23 (Polinomi)#Operazioni tra Polinomi]]
3.  [[Lezione 23 (Polinomi)#Grado di un Polinomio e Teorema dei Gradi]]
4.  [[Lezione 23 (Polinomi)#Elementi Speciali: Unità, Associati e Polinomi Monici]]
5.  [[Lezione 23 (Polinomi)#Divisione tra Polinomi: L'Algoritmo Euclideo]]
6.  [[Lezione 23 (Polinomi)#Radici di un Polinomio e Teorema di Ruffini]]
7.  [[Lezione 23 (Polinomi)#Polinomi e Funzioni Polinomiali]]
8.  [[Lezione 23 (Polinomi)#Divisibilità e Irriducibilità]]
9.  [[Lezione 23 (Polinomi)#Teorema di Fattorizzazione Unica]]
10. [[Lezione 23 (Polinomi)#Punti Chiave della Lezione]]
11. [[Lezione 23 (Polinomi)#Domande per la Riflessione]]

---

## Definizioni di Base sui Polinomi

> [!NOTE] Definizione: Anello dei Polinomi
> Dato un anello commutativo unitario $(A, +, \cdot)$, l'insieme dei polinomi a coefficienti in $A$ nell'indeterminata $x$, indicato con $A[x]$, è l'insieme di tutte le espressioni formali del tipo:
> $$
> f(x) = a_0 + a_1x + a_2x^2 + \dots + a_nx^n
> $$
> dove i coefficienti $a_i$ appartengono all'anello $A$ e $n$ è un numero intero non negativo.

**Spiegazione Semplice:** Pensa a un polinomio come a una "ricetta" matematica. Gli **ingredienti** sono i numeri dell'anello $A$ (i **coefficienti** $a_i$), e li combiniamo con potenze crescenti di una variabile "magica" $x$ (l'**indeterminata**).

*   **Polinomio nullo:** Il polinomio con tutti i coefficienti uguali a zero. Lo indichiamo con $0$.
*   **Polinomi costanti:** Polinomi del tipo $f(x) = a_0$. Praticamente, solo un numero.

---

## Operazioni tra Polinomi

Possiamo sommare e moltiplicare i polinomi in modo molto intuitivo.

### Somma di Polinomi

> [!TIP] Come sommare due polinomi
> Per sommare due polinomi, $f(x)$ e $g(x)$, semplicemente **sommiamo i coefficienti dei termini con lo stesso grado**.

Se $f(x) = a_0 + a_1x + \dots$ e $g(x) = b_0 + b_1x + \dots$, allora:
$$
f(x) + g(x) = (a_0 + b_0) + (a_1 + b_1)x + (a_2 + b_2)x^2 + \dots
$$

> [!EXAMPLE] Esempio di Somma
> *   $f(x) = 3 - 5x^2 + 7x^4$
> *   $g(x) = 1 + 3x + 4x^2 - 2x^3$
>
> $(f+g)(x) = (3+1) + 3x + (-5+4)x^2 - 2x^3 + 7x^4 = \mathbf{4 + 3x - x^2 - 2x^3 + 7x^4}$

### Prodotto di Polinomi

Il prodotto è un po' più elaborato, ma segue la regola "tutti per tutti".

> [!NOTE] Formula del Prodotto
> Se $f(x) \cdot g(x) = c_0 + c_1x + c_2x^2 + \dots$, il coefficiente $c_k$ si ottiene sommando tutti i prodotti $a_i \cdot b_j$ tali che $i+j=k$.
> $$
> c_k = \sum_{i+j=k} a_i b_j
> $$

**Spiegazione Semplice:** È come la normale moltiplicazione che hai sempre fatto, distribuendo ogni termine del primo polinomio per ogni termine del secondo.

Con queste operazioni, $(A[x], +, \cdot)$ diventa a sua volta un **anello commutativo unitario**. L'elemento neutro della somma è il polinomio nullo, e quello del prodotto è il polinomio costante $1$.

---

## Grado di un Polinomio e Teorema dei Gradi

#tag/definizione #tag/teorema

> [!IMPORTANT] Definizione: Grado di un Polinomio
> Il **grado** di un polinomio non nullo $f(x)$, indicato con $\text{gr}(f)$ o $\delta(f)$, è il **massimo esponente** della $x$ con un coefficiente diverso da zero.
> *   Il coefficiente di grado massimo è detto **coefficiente direttore**.
> *   Per convenzione, il grado del polinomio nullo è $-\infty$.

### Proprietà dei Gradi

1.  **Grado della Somma:** $\text{gr}(f+g) \le \max\{\text{gr}(f), \text{gr}(g)\}$
    *   **Perché "minore o uguale"?** Perché se i gradi sono uguali e i coefficienti direttori sono opposti, si annullano!
    *   **Esempio:** Se $f(x) = x$ e $g(x) = -x$, allora $\text{gr}(f)=1, \text{gr}(g)=1$. Ma $f(x)+g(x)=0$, che ha grado $-\infty$.

2.  **Grado del Prodotto:** $\text{gr}(f \cdot g) \le \text{gr}(f) + \text{gr}(g)$

Questa seconda proprietà diventa un'uguaglianza in un caso molto importante.

### Teorema: Additività dei Gradi (DIM)

> [!NOTE] Teorema dei Gradi
> Siano $f(x), g(x) \in A[x]$.
> 1.  $\text{gr}(f \cdot g) \le \text{gr}(f) + \text{gr}(g)$
> 2.  Se $A$ è un **dominio di integrità**, allora vale l'uguaglianza:
>     $$
>     \text{gr}(f \cdot g) = \text{gr}(f) + \text{gr}(g)
>     $$

#### Dimostrazione

1.  **Ipotesi:** Sia $A$ un dominio di integrità. Questo significa che se prendiamo due elementi non nulli $a, b \in A$, il loro prodotto $a \cdot b$ è anch'esso non nullo.
2.  **Polinomi:** Prendiamo due polinomi non nulli:
    *   $f(x) = a_n x^n + \dots + a_0$ con $\text{gr}(f)=n$ (quindi $a_n \neq 0$).
    *   $g(x) = b_m x^m + \dots + b_0$ con $\text{gr}(g)=m$ (quindi $b_m \neq 0$).
3.  **Prodotto:** Calcoliamo il prodotto $f(x) \cdot g(x)$. Il termine di grado più alto possibile si ottiene moltiplicando i termini di grado più alto di $f$ e $g$:
    $$
    (a_n x^n) \cdot (b_m x^m) = (a_n \cdot b_m) x^{n+m}
    $$
4.  **Coefficiente Direttore:** Il coefficiente direttore del prodotto è $c_{n+m} = a_n \cdot b_m$.
5.  **Conclusione:** Poiché siamo in un dominio di integrità e $a_n \neq 0$ e $b_m \neq 0$, allora anche il loro prodotto $a_n \cdot b_m \neq 0$.
    Dato che il coefficiente del termine di grado $n+m$ non è zero, il grado del polinomio prodotto è esattamente $n+m$.
    $$
    \text{gr}(f \cdot g) = n+m = \text{gr}(f) + \text{gr}(g)
    $$
    **Q.E.D.** (Quod Erat Demonstrandum - Come Volevasi Dimostrare)

> [!WARNING] Cosa succede se A non è un dominio di integrità?
> Prendiamo l'anello $\mathbb{Z}_6[x]$. $\mathbb{Z}_6$ non è un dominio perché $\bar{2} \cdot \bar{3} = \bar{6} = \bar{0}$.
> *   $f(x) = \bar{5} + \bar{2}x$ (grado 1)
> *   $g(x) = \bar{1} + \bar{3}x$ (grado 1)
> *   $f(x) \cdot g(x) = (\bar{5} + \bar{2}x)(\bar{1} + \bar{3}x) = \bar{5} + \overline{15}x + \bar{2}x + \bar{6}x^2 = \bar{5} + (\bar{3}+\bar{2})x + \bar{0}x^2 = \bar{5} + \bar{5}x$
> Il grado del prodotto è 1, che è **diverso** da $\text{gr}(f)+\text{gr}(g) = 1+1=2$.

**Corollario:** Se $A$ è un dominio di integrità, allora anche $A[x]$ è un dominio di integrità.

---

## Elementi Speciali: Unità, Associati e Polinomi Monici

### Unità in A[x]

> [!IMPORTANT] Teorema sulle Unità
> Se $A$ è un **dominio di integrità**, allora le unità dell'anello dei polinomi $A[x]$ sono esattamente le unità dell'anello dei coefficienti $A$.
> $$
> \mathcal{U}(A[x]) = \mathcal{U}(A)
> $$

**Spiegazione Semplice:** In un dominio (come i numeri interi $\mathbb{Z}$ o i reali $\mathbb{R}$), gli unici polinomi che hanno un "inverso moltiplicativo" sono i polinomi costanti che erano già invertibili nell'anello di partenza. Per esempio, in $\mathbb{Z}[x]$, gli unici polinomi invertibili sono $1$ e $-1$.

### Elementi Associati

> [!NOTE] Definizione: Elementi Associati
> Due polinomi $f(x)$ e $g(x)$ si dicono **associati** (e si scrive $f \sim g$) se esiste un'unità $c \in \mathcal{U}(A[x])$ tale che:
> $$
> f(x) = c \cdot g(x)
> $$

**Analogia Musicale:** Pensa a due melodie identiche, ma una è suonata a un volume "forte" e l'altra a un volume "piano". La melodia di base è la stessa, cambia solo un "fattore di scala" (l'unità). In $\mathbb{Z}[x]$, $f(x)=x+1$ è associato a $g(x)=-x-1$ perché $g(x) = (-1) \cdot f(x)$ e $-1$ è un'unità.

### Polinomi Monici

> [!TIP] Definizione: Polinomio Monico
> Un polinomio si dice **monico** se il suo coefficiente direttore è **1**.

> [!EXAMPLE] Esempi di Polinomi Monici
> *   $x^2 - 3x + 5$ è monico.
> *   $2x^3 + x - 1$ **non** è monico.

**Il Superpotere dei Polinomi Monici:** Se il coefficiente direttore di un polinomio $f(x)$ è un'unità, allora $f(x)$ è associato a un **unico** polinomio monico. Basta moltiplicare $f(x)$ per l'inverso del suo coefficiente direttore!

> [!QUESTION] Esercizio Guidato
> Verificare se in $\mathbb{Z}_{42}[x]$ il polinomio $f(x) = \overline{25}x^3 + \overline{7}x - \overline{2}$ è associato a un polinomio monico.
> 1.  **Domanda:** Il coefficiente direttore, $\overline{25}$, è un'unità in $\mathbb{Z}_{42}$?
> 2.  **Controllo:** Un elemento $\bar{a}$ è invertibile in $\mathbb{Z}_n$ se e solo se $\text{MCD}(a, n) = 1$.
> 3.  **Calcolo:** $\text{MCD}(25, 42) = \text{MCD}(5^2, 2 \cdot 3 \cdot 7) = 1$. Sì, è invertibile!
> 4.  **Trovare l'inverso:** Usiamo l'algoritmo di Euclide per trovare $x, y$ tali che $25x + 42y = 1$.
>     *   $42 = 1 \cdot 25 + 17$
>     *   $25 = 1 \cdot 17 + 8$
>     *   $17 = 2 \cdot 8 + 1$
>     Andando a ritroso:
>     *   $1 = 17 - 2 \cdot 8 = 17 - 2(25 - 1 \cdot 17) = 3 \cdot 17 - 2 \cdot 25$
>     *   $1 = 3(42 - 1 \cdot 25) - 2 \cdot 25 = 3 \cdot 42 - 3 \cdot 25 - 2 \cdot 25 = 3 \cdot 42 - 5 \cdot 25$
>     In $\mathbb{Z}_{42}$, questo significa $-5 \cdot 25 \equiv 1 \pmod{42}$.
>     L'inverso di $\overline{25}$ è $\overline{-5} = \overline{37}$.
> 5.  **Trovare il monico associato:** Moltiplichiamo $f(x)$ per $\overline{37}$.
>     *   $\overline{37} \cdot (\overline{25}x^3 + \overline{7}x - \overline{2}) = (\overline{37} \cdot \overline{25})x^3 + (\overline{37} \cdot \overline{7})x - (\overline{37} \cdot \overline{2})$
>     *   $= \overline{1}x^3 + \overline{259}x - \overline{74}$
>     *   Calcolando i resti modulo 42: $259 = 6 \cdot 42 + 7 \implies \overline{259}=\bar{7}$. $74 = 1 \cdot 42 + 32 \implies \overline{74}=\overline{32}$.
>     *   Il polinomio monico associato è $\mathbf{x^3 + \overline{7}x - \overline{32}}$.

---

## Divisione tra Polinomi: L'Algoritmo Euclideo

#tag/teorema #tag/dimostrazione

Proprio come per i numeri interi, possiamo fare la divisione con resto anche per i polinomi!

### Teorema: Divisione Euclidea tra Polinomi (DIM)

> [!NOTE] Teorema della Divisione
> Siano $f(x), g(x) \in A[x]$, con $g(x) \neq 0$. Se il **coefficiente direttore di $g(x)$ è un'unità** in $A$, allora esistono e sono **unici** due polinomi $q(x)$ (quoziente) e $r(x)$ (resto) tali che:
> $$
> f(x) = g(x) \cdot q(x) + r(x)
> $$
> con $\text{gr}(r) < \text{gr}(g)$.

#### Dimostrazione (Esistenza)

La dimostrazione si fa per **induzione sul grado di $f(x)$**.

1.  **Caso Base:** Se $\text{gr}(f) < \text{gr}(g)$, la divisione è già fatta! Basta scegliere $q(x)=0$ e $r(x)=f(x)$. La condizione $\text{gr}(r) < \text{gr}(g)$ è soddisfatta.

2.  **Passo Induttivo:** Assumiamo che il teorema sia vero per tutti i polinomi con grado minore di $n = \text{gr}(f)$. Vogliamo dimostrarlo per $f(x)$.
    *   Siano $f(x) = a_n x^n + \dots$ e $g(x) = b_m x^m + \dots$, con $n \ge m$.
    *   Sia $b_m$ il coefficiente direttore di $g(x)$. Per ipotesi, $b_m$ è invertibile e il suo inverso è $b_m^{-1}$.
    *   **Costruiamo un nuovo polinomio** $\tilde{f}(x)$ per "abbassare il grado" di $f(x)$:
        $$
        \tilde{f}(x) = f(x) - (a_n b_m^{-1} x^{n-m}) \cdot g(x)
        $$
    *   **Analizziamo il termine di grado n:** Il termine di grado $n$ di $(a_n b_m^{-1} x^{n-m}) \cdot g(x)$ è $(a_n b_m^{-1} x^{n-m}) \cdot (b_m x^m) = a_n x^n$.
    *   Quando sottraiamo questo da $f(x)$, il termine $a_n x^n$ si cancella! Quindi, $\text{gr}(\tilde{f}) < n$.
    *   **Applichiamo l'ipotesi induttiva:** Poiché $\tilde{f}(x)$ ha grado minore di $n$, esistono $\tilde{q}(x)$ e $\tilde{r}(x)$ tali che:
        $$
        \tilde{f}(x) = g(x) \cdot \tilde{q}(x) + \tilde{r}(x) \quad \text{con } \text{gr}(\tilde{r}) < \text{gr}(g)
        $$
    *   **Sostituiamo e risolviamo per f(x):**
        $$
        f(x) - (a_n b_m^{-1} x^{n-m}) \cdot g(x) = g(x) \cdot \tilde{q}(x) + \tilde{r}(x)
        $$
        $$
        f(x) = g(x) \cdot \tilde{q}(x) + (a_n b_m^{-1} x^{n-m}) \cdot g(x) + \tilde{r}(x)
        $$
        $$
        f(x) = g(x) \cdot \underbrace{[\tilde{q}(x) + a_n b_m^{-1} x^{n-m}]}_{q(x)} + \underbrace{\tilde{r}(x)}_{r(x)}
        $$
    *   Abbiamo trovato il nostro quoziente $q(x)$ e il nostro resto $r(x)$, e il resto ha il grado giusto. L'esistenza è provata.

> [!EXAMPLE] Esempio di Divisione
> Dividiamo $f(x) = 2x^3 + 7x^2 - 5x + 3$ per $g(x) = x-1$ in $\mathbb{Q}[x]$.
> ```
>        2x^2 + 9x + 4   <-- q(x)
>      _________________
> x-1 | 2x^3 + 7x^2 - 5x + 3
>     -(2x^3 - 2x^2)
>     _________________
>            9x^2 - 5x
>          -(9x^2 - 9x)
>          ___________
>                   4x + 3
>                 -(4x - 4)
>                 ________
>                        7   <-- r(x)
> ```
> Quindi, $q(x) = 2x^2+9x+4$ e $r(x) = 7$.

---

## Radici di un Polinomio e Teorema di Ruffini

#tag/teorema #tag/radici

### Funzione Polinomiale e Radici

Ad ogni polinomio formale $f(x) \in A[x]$ possiamo associare una **funzione polinomiale** $\tilde{f}: A \to A$ che calcola il valore del polinomio per ogni elemento $c \in A$.
$$
\tilde{f}(c) = a_0 + a_1c + a_2c^2 + \dots + a_nc^n
$$

> [!IMPORTANT] Definizione: Radice (o Zero)
> Un elemento $c \in A$ è una **radice** (o **zero**) del polinomio $f(x)$ se $\tilde{f}(c) = 0$.

### Lemma del Resto (DIM)

> [!NOTE] Lemma del Resto
> Il resto della divisione di un polinomio $f(x)$ per un binomio $(x-c)$ è uguale al valore che il polinomio assume in $c$, cioè $\tilde{f}(c)$.
> $$
> \text{rest}(f(x), x-c) = \tilde{f}(c)
> $$

#### Dimostrazione

1.  Dal teorema della divisione, dividendo $f(x)$ per $(x-c)$, otteniamo:
    $$
    f(x) = (x-c) \cdot q(x) + r(x)
    $$
2.  Il divisore $(x-c)$ ha grado 1. Quindi il resto $r(x)$ deve avere grado minore di 1, cioè grado 0 o $-\infty$. In ogni caso, $r(x)$ è un polinomio costante. Chiamiamolo $r_0$.
    $$
    f(x) = (x-c) \cdot q(x) + r_0
    $$
3.  Valutiamo entrambi i lati dell'equazione in $c$:
    $$
    \tilde{f}(c) = (c-c) \cdot \tilde{q}(c) + r_0
    $$
    $$
    \tilde{f}(c) = 0 \cdot \tilde{q}(c) + r_0
    $$
    $$
    \tilde{f}(c) = r_0
    $$
    Il resto è proprio $\tilde{f}(c)$. **Q.E.D.**

### Teorema di Ruffini (DIM)

> [!NOTE] Teorema di Ruffini
> Un elemento $c \in A$ è una radice di $f(x)$ se e solo se il polinomio $(x-c)$ divide $f(x)$.
> $$
> \tilde{f}(c) = 0 \iff (x-c) \mid f(x)
> $$

#### Dimostrazione

È una conseguenza diretta del Lemma del Resto.
*   ($\Rightarrow$) **Se $c$ è una radice**, allora $\tilde{f}(c) = 0$. Per il Lemma del Resto, il resto della divisione per $(x-c)$ è 0. Se il resto è zero, significa che $(x-c)$ divide $f(x)$.
*   ($\Leftarrow$) **Se $(x-c)$ divide $f(x)$**, allora il resto della divisione è 0. Per il Lemma del Resto, $\tilde{f}(c)$ è uguale al resto, quindi $\tilde{f}(c)=0$. Questo significa che $c$ è una radice. **Q.E.D.**

### Teorema di Ruffini Generalizzato

> [!NOTE] Teorema di Ruffini Generalizzato
> Se $A$ è un **dominio di integrità** e $c_1, c_2, \dots, c_k$ sono $k$ radici **distinte** di $f(x)$, allora il prodotto $(x-c_1)(x-c_2)\dots(x-c_k)$ divide $f(x)$.

---

## Polinomi e Funzioni Polinomiali

#tag/funzioni

> [!QUESTION] Se due polinomi generano la stessa funzione, sono per forza lo stesso polinomio?

La risposta, sorprendentemente, è... **dipende dall'anello A!**

### Teorema: Identità dei Polinomi (DIM)

> [!NOTE] Teorema sull'Identità dei Polinomi
> Siano $f(x), g(x) \in A[x]$ dove $(A, +, \cdot)$ è un **campo**.
> 1.  Se $A$ è un **campo infinito** (come $\mathbb{Q}, \mathbb{R}, \mathbb{C}$), allora:
>     $$
>     \tilde{f} = \tilde{g} \iff f = g
>     $$
>     (Due polinomi sono uguali se e solo se generano la stessa funzione).
> 2.  Se $A$ è un **campo finito** con $|A|=m$ elementi, allora $\tilde{f} = \tilde{g}$ se e solo se il polinomio $x^m - x$ divide la loro differenza $f(x) - g(x)$.

#### Dimostrazione (idea chiave)

*   **Caso Infinito:** Se $\tilde{f} = \tilde{g}$, allora il polinomio differenza $h(x) = f(x) - g(x)$ ha la proprietà che $\tilde{h}(c) = 0$ per ogni $c \in A$. Ma un polinomio non nullo può avere solo un numero finito di radici (al massimo il suo grado). Poiché $A$ è infinito, l'unico modo per avere infinite radici è che il polinomio $h(x)$ sia il polinomio nullo. Se $h(x)=0$, allora $f(x)=g(x)$.
*   **Caso Finito:** Se $\tilde{f} = \tilde{g}$, allora il polinomio differenza $h(x) = f(x) - g(x)$ ha come radici tutti gli $m$ elementi del campo $A$. Per il Teorema di Ruffini Generalizzato, il prodotto $(x-c_1)\dots(x-c_m)$ deve dividere $h(x)$. Si può dimostrare che questo prodotto è esattamente il "polinomio fondamentale" $x^m - x$.

> [!EXAMPLE] Esempio in un Campo Finito
> In $\mathbb{Z}_3[x]$, consideriamo $f(x) = x^3+1$ e $g(x) = x+1$.
> *   $f \neq g$ come polinomi formali.
> *   Valutiamo le funzioni $\tilde{f}$ e $\tilde{g}$:
>     *   $\tilde{f}(\bar{0}) = \bar{0}^3+\bar{1} = \bar{1}$
>     *   $\tilde{f}(\bar{1}) = \bar{1}^3+\bar{1} = \bar{2}$
>     *   $\tilde{f}(\bar{2}) = \bar{2}^3+\bar{1} = \bar{8}+\bar{1} = \bar{9} = \bar{0}$
>     *   $\tilde{g}(\bar{0}) = \bar{0}+\bar{1} = \bar{1}$
>     *   $\tilde{g}(\bar{1}) = \bar{1}+\bar{1} = \bar{2}$
>     *   $\tilde{g}(\bar{2}) = \bar{2}+\bar{1} = \bar{3} = \bar{0}$
> Le funzioni non sono uguali! C'è un errore negli appunti originali. Vediamo un esempio che funziona: $f(x) = x^3$ e $g(x)=x$ in $\mathbb{Z}_3$.
> *   $\tilde{f}(\bar{0})=\bar{0}, \tilde{f}(\bar{1})=\bar{1}, \tilde{f}(\bar{2})=\bar{8}=\bar{2}$.
> *   $\tilde{g}(\bar{0})=\bar{0}, \tilde{g}(\bar{1})=\bar{1}, \tilde{g}(\bar{2})=\bar{2}$.
> In questo caso $\tilde{f} = \tilde{g}$ ma $f \neq g$. La loro differenza è $h(x) = x^3-x$, che è esattamente il polinomio fondamentale di $\mathbb{Z}_3$.

---

## Divisibilità e Irriducibilità

Questi concetti sono l'analogo dei numeri primi per i polinomi.

> [!IMPORTANT] Definizione: Polinomio Irriducibile
> Un polinomio non costante $f(x) \in A[x]$ si dice **irriducibile** su $A$ se non può essere scritto come prodotto di due polinomi non costanti di grado inferiore.
> Formalmente, se $f(x) = g(x) \cdot h(x)$, allora o $g(x)$ o $h(x)$ deve essere un'unità (cioè un polinomio costante invertibile).

**Spiegazione Semplice:** Un polinomio è irriducibile se non puoi "spezzarlo" in polinomi più semplici. È un "atomo" polinomiale. Se è possibile spezzarlo, si dice **riducibile**.

> [!TIP] Irriducibilità e Radici
> Se un polinomio $f(x)$ di grado 2 o 3 **ha una radice** in un campo $A$, allora è **riducibile** su $A$.
> **Perché?** Se $c$ è una radice, per Ruffini $(x-c)$ divide $f(x)$. Quindi $f(x) = (x-c) \cdot q(x)$. Poiché $\text{gr}(f) > 1$, anche $q(x)$ non sarà costante. Abbiamo spezzato $f(x)$!
>
> > [!WARNING] Attenzione!
> > Il viceversa non è sempre vero! Un polinomio può essere riducibile anche senza avere radici.
> > Esempio: $f(x) = (x^2+1)^2$ in $\mathbb{R}[x]$ non ha radici reali, ma è chiaramente riducibile.

### Proposizione: Irriducibilità per gradi 2 e 3 (DIM)

> [!NOTE] Proposizione
> Sia $A$ un **campo** e $f(x) \in A[x]$ un polinomio di grado 2 o 3. Allora:
> $$
> f(x) \text{ è irriducibile} \iff f(x) \text{ non ha radici in } A
> $$

#### Dimostrazione

*   ($\Rightarrow$) **Se $f$ è irriducibile, allora non ha radici.**
    Lo dimostriamo per assurdo. Supponiamo che $f$ abbia una radice $c \in A$. Allora per il Teorema di Ruffini, $(x-c)$ divide $f(x)$. Possiamo scrivere $f(x) = (x-c) \cdot q(x)$.
    Poiché $\text{gr}(f) \ge 2$ e $\text{gr}(x-c)=1$, il quoziente $q(x)$ deve avere grado $\text{gr}(f)-1 \ge 1$.
    Quindi, abbiamo scritto $f(x)$ come prodotto di due polinomi non costanti, il che contraddice l'ipotesi che $f$ sia irriducibile. Assurdo. Dunque $f$ non può avere radici.

*   ($\Leftarrow$) **Se $f$ non ha radici, allora è irriducibile.**
    Lo dimostriamo per assurdo. Supponiamo che $f$ sia riducibile. Allora possiamo scrivere $f(x) = g(x) \cdot h(x)$, dove $g$ e $h$ non sono costanti.
    Poiché $A$ è un campo, $\text{gr}(f) = \text{gr}(g) + \text{gr}(h)$.
    Dato che $\text{gr}(f)$ è 2 o 3, e $\text{gr}(g), \text{gr}(h) \ge 1$, uno dei due fattori (diciamo $g(x)$) deve avere per forza **grado 1**.
    Un polinomio di grado 1 su un campo ha sempre una radice. Se $g(x)=ax+b$ con $a \neq 0$, la sua radice è $c = -b a^{-1}$.
    Ma se $c$ è una radice di $g(x)$, allora $\tilde{g}(c)=0$, e quindi $\tilde{f}(c) = \tilde{g}(c) \cdot \tilde{h}(c) = 0 \cdot \tilde{h}(c) = 0$.
    Questo significa che $f(x)$ ha una radice $c$, il che contraddice l'ipotesi. Assurdo. Dunque $f$ deve essere irriducibile. **Q.E.D.**

---

## Teorema di Fattorizzazione Unica

Questo è uno dei risultati più importanti, l'equivalente del Teorema Fondamentale dell'Aritmetica per i polinomi.

### Teorema Fondamentale dell'Aritmetica (per confronto)

Ogni intero $a \in \mathbb{Z} \setminus \{0, 1, -1\}$ è un numero primo oppure può essere scritto in modo **unico** (a meno dell'ordine e di fattori $\pm 1$) come prodotto di numeri primi.

### Teorema di Fattorizzazione Unica per Polinomi (DIM)

> [!NOTE] Teorema di Fattorizzazione Unica
> Sia $A$ un **campo**. Ogni polinomio non costante $f(x) \in A[x]$ è irriducibile oppure può essere scritto in modo **unico** (a meno dell'ordine e di fattori associati) come prodotto di polinomi irriducibili.

#### Dimostrazione (Cenno)

La dimostrazione è molto simile a quella per i numeri interi e si basa su due pilastri:

1.  **Esistenza:** Si dimostra per induzione sul grado del polinomio.
    *   **Caso Base:** Se $f(x)$ è irriducibile, abbiamo finito.
    *   **Passo Induttivo:** Se $f(x)$ è riducibile, lo spezziamo in $f(x)=g(x)h(x)$. I gradi di $g$ e $h$ sono minori di quello di $f$. Per ipotesi induttiva, $g$ e $h$ si possono fattorizzare in irriducibili. Mettendo insieme le loro fattorizzazioni, otteniamo quella di $f$.

2.  **Unicità:** Si basa su un risultato analogo al Lemma di Euclide: se un polinomio irriducibile $p(x)$ divide un prodotto $g(x)h(x)$, allora deve dividere o $g(x)$ o $h(x)$. Usando questa proprietà, si mostra che due fattorizzazioni diverse devono in realtà contenere gli stessi "atomi" irriducibili.

---

## Punti Chiave della Lezione

> [!TIP] Riepilogo Super-Sintetico
> *   I **polinomi** formano un anello $A[x]$ con le operazioni di somma e prodotto.
> *   Il **grado** è l'esponente più alto. Se i coefficienti sono in un **dominio di integrità**, il grado del prodotto è la somma dei gradi.
> *   La **divisione con resto** è possibile se il coefficiente direttore del divisore è un'unità.
> *   **Teorema di Ruffini:** $c$ è una **radice** di $f(x)$ se e solo se $(x-c)$ divide $f(x)$.
> *   Un polinomio è **irriducibile** se non può essere spezzato in fattori più semplici (non costanti).
> *   **Fattorizzazione Unica:** Se i coefficienti sono in un **campo**, ogni polinomio si scompone in modo unico in un prodotto di irriducibili (come i numeri si scompongono in primi).

---

## Domande per la Riflessione

> [!QUESTION] Mettiti alla Prova!
> 1.  Perché è così importante che l'anello dei coefficienti $A$ sia un dominio di integrità per il teorema dei gradi? Cosa "si rompe" se non lo è?
> 2.  Prendi il polinomio $f(x) = x^2 + 1$. È irriducibile su $\mathbb{R}[x]$? E su $\mathbb{C}[x]$? (Suggerimento: cerca le radici!)
> 3.  Sai spiegare a parole tue la differenza tra un polinomio *formale* $f(x)$ e la sua *funzione* associata $\tilde{f}$? Perché questa distinzione è importante nei campi finiti?