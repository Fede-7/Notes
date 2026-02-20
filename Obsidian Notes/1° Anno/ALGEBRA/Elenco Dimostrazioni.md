
## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">4.9:</mark> Teorema Invertibilità di Funzioni

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

## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">6.1:</mark> Elementi simmetrizzabili: se esiste il simmetrico è unico


> [!note] Elemento Invertibile opp. Simmetrizzabile
> In un monoide $(S, *, u)$, $a \in S$ è **invertibile** se:
> $$\exists\, a' \in S:\; a * a' = a' * a = u$$
> L'inverso è **unico**. Invertibile $\Longrightarrow$ Cancellabile.

> [!tip] Dimostrazione — Unicità dell'inverso
> Siano $a'$ e $a''$ entrambi inversi di $a$. Allora:
> $$a' = a' * u = a' * (a * a'') = (a' * a) * a'' = u * a'' = a''$$
> Dunque l'inverso è unico. $\square$


## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">7.6:</mark> Divisioni dello zero: mai cancellabili


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


## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">8.1:</mark> Elementi simmetrizzabili $\implies$  elementi cancellabili


> [!note] Cancellabilità
> $a$ è **cancellabile a sinistra** se $a \cdot b = a \cdot c \Rightarrow b = c$.
> $a$ è **cancellabile a destra** se $b \cdot a = c \cdot a \Rightarrow b = c$.
> **Invertibile $\Longrightarrow$ Cancellabile** (il viceversa non vale in generale).

> [!tip] Dimostrazione — Invertibile $\Longrightarrow$ Cancellabile
> Sia $a$ invertibile con inverso $a'$. Se $a \cdot b = a \cdot c$, moltiplichiamo a sinistra per $a'$:
> $$a' \cdot (a \cdot b) = a' \cdot (a \cdot c) \;\Longrightarrow\; (a' \cdot a) \cdot b = (a' \cdot a) \cdot c \;\Longrightarrow\; u \cdot b = u \cdot c \;\Longrightarrow\; b = c$$
> Analogamente per la cancellabilità a destra. $\blacksquare$
> "$\nLeftarrow$" viceversa non vale



## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">8.7:</mark> Teorema di Wedderburn

> [!important] Teorema di Wedderburn
> Ogni **corpo finito** è anche un **campo**.
> - Spiegazione:
> Il teorema dimostra che se l'insieme degli elementi è finito, è matematicamente impossibile costruire una struttura dove valga l'invertibilità senza che valga anche la commutatività
> Quindi se
> $$
> S \text{ è finito e simmetrizzabile} \implies S \text{ è commutativo}
> $$

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">8.9:</mark> Teorema di scomposizione canonica di una permutazione

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

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">10.5:</mark> Teorema della divisione euclidea

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
## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">10.6:</mark> Teorema di Bézout

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

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">11.1:</mark> Teorema fondamentale sulle relazioni di equivalenza

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">11.2:</mark> Teorema su relazioni di equivalenza e partizioni

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">12.1:</mark>  campo  è primo

## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">12.2:</mark> Gli elementi  sono divisori dello zero o invertibili

## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">12.3:</mark> Proposizioni classi di equivalenza nilpotenti

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">12.4:</mark> Equazioni congruenziali

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">13.3:</mark> Teorema di esistenza soluzioni equazioni congruenziali

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">14.2:</mark> Teorema di Fermat-Eulero

## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">14.4:</mark> Coefficiente binomiale

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">18.3:</mark> Teorema  distributivo

## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">18.4:</mark> Proposizione

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">18.5:</mark> Definizione reticolo Booleano

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">18.7:</mark> Teorema 

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">18.9:</mark> Teorema di Stone (Anello Booleano)