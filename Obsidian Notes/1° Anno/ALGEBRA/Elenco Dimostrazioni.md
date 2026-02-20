
## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">4.9:</mark> Teorema Invertibilità di Funzioni

## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">6.1:</mark> Elementi simmetrizzabili: se esiste il simmetrico è unico

## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">7.6:</mark> Divisioni dello zero: mai cancellabili

## <mark style="background:#C0C0C0; color:black; padding:0 6px; border-radius:6px;">8.1:</mark> Elementi simmetrizzabili  elementi cancellabili

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">8.7:</mark> Teorema di Wedderburn

## <mark style="background:#D4AF37; color:white; padding:0 6px; border-radius:6px;">8.9:</mark> Teorema di scomposizione canonica di una permutazione

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

> [!tip] Dimostrazione — Identità di Bézout
> 1. Sia $S = \{as + bt \mid s, t \in \mathbb{Z},\; as + bt > 0\}$.
> 2. $S \neq \emptyset$: se $a \neq 0$, $|a| = a \cdot (\pm 1) + b \cdot 0 \in S$; analogamente per $b$.
> 3. Per il **principio del buon ordinamento**, $S$ ammette un minimo $d = ax + by$.
> 4. **$d \mid a$:** Dividiamo $a = dq + r$ con $0 \le r < d$. Allora:
>    $$r = a - dq = a - (ax + by)q = a(1 - xq) + b(-yq)$$
>    Se $r > 0$, allora $r \in S$ con $r < d$, contraddicendo la minimalità di $d$. Dunque $r = 0$.
> 5. **$d \mid b$:** Analogamente.
> 6. **$d = \mathrm{MCD}(a,b)$:** Se $c \mid a$ e $c \mid b$, allora $c \mid (ax + by) = d$, dunque $d$ è il massimo. $\square$

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