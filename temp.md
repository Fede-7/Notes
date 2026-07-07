## pdf condizionate

In modo del tutto analogo a quanto fatto per le variabili discrete, potremo scrivere: 
$$
\mathbb {P} \left[ X \in \left(x - \frac {\Delta x}{2}, x - \frac {\Delta x}{2}\right) \mid A \right] = P _ {X} (x, \Delta x | A) 
$$
$$
\Rightarrow f _ {X | A} (x) = \lim _ {\Delta x \rightarrow 0} \frac {P _ {X} (x , \Delta x | A)}{\Delta x}
$$
o, anche: 
$$
F _ {X \mid A} (x) = \mathbb {P} (X \leq x \mid A) = \frac {\mathbb {P} (\{X \leq x \} \mid \cap A)}{\mathbb {P} (A)}
$$
$$
 \Rightarrow f _ {X \mid A} (x) = \frac {d F _ {X \mid A} (x)}{d x}
$$


> [!example] Esempio 1
> Per esempio, sia $X \sim L(\lambda)$ $X \sim { \mathcal { L } } ( \lambda ) \ { \textrm { e } } A = \{ - 1 \leq X \leq 2 \} \quad$. Avremo:
>
> $$
> F _ {X | \{- 1 \leq X \leq 2 \}} (x) = \frac {\mathbb {P} (\{X \leq x \} \cap \{- 1 \leq X \leq 2 \})}{F _ {X} (- 1 \leq X \leq 2)} = \left\{ \begin{array}{l l} 0 & x <   - 1 \\ \frac {F _ {X} (x) - F _ {X} (- 1)}{F _ {X} (2) - F _ {X} (- 1)} & - 1 \leq x \leq 2 \\ 1 & x \geq 2 \end{array} \right.
> $$
>
> $$
> f _ {X | \{- 1 \leq X \leq 2 \}} (x) = \left\{ \begin{array}{c l} \frac {f _ {X} (x)}{F _ {X} (2) - F _ {X} (- 1)} = \frac {\frac {\lambda}{2} e ^ {- \lambda | x |}}{1 - \frac {1}{2} e ^ {- 2 \lambda} + \frac {1}{2} e ^ {- \lambda}} & x \in (- 1, 2) \\ 0 & x \notin (- 1, 2) \end{array} \right.
> $$

