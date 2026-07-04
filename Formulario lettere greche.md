### Alfabeto Greco

| Maiuscola | Minuscola | Nome | Traslitterazione |
| :---: | :---: | :--- | :--- |
| $\mathrm{A}$ | $\alpha$ | Alpha | a |
| $\mathrm{B}$ | $\beta$ | Beta | b |
| $\Gamma$ | $\gamma$ | Gamma | g |
| $\Delta$ | $\delta$ | Delta | d |
| $\mathrm{E}$ | $\epsilon$ | Epsilon | e |
| $\mathrm{Z}$ | $\zeta$ | Zeta | z |
| $\mathrm{H}$ | $\eta$ | Eta | ē |
| $\Theta$ | $\theta$ | Theta | th |
| $\mathrm{I}$ | $\iota$ | Iota | i |
| $\mathrm{K}$ | $\kappa$ | Kappa | k |
| $\Lambda$ | $\lambda$ | Lambda | l |
| $\mathrm{M}$ | $\mu$ | Mu | m |
| $\mathrm{N}$ | $\nu$ | Nu | n |
| $\Xi$ | $\xi$ | Xi | x |
| $\mathrm{O}$ | $\omicron$ | Omicron | o |
| $\Pi$ | $\pi$ | Pi | p |
| $\mathrm{P}$ | $\rho$ | Rho | r |
| $\Sigma$ | $\sigma, \varsigma$* | Sigma | s |
| $\mathrm{T}$ | $\tau$ | Tau | t |
| $\Upsilon$ | $\upsilon$ | Upsilon | y / u |
| $\Phi$ | $\phi$ | Phi | ph / f |
| $\mathrm{X}$ | $\chi$ | Chi | ch |
| $\Psi$ | $\psi$ | Psi | ps |
| $\Omega$ | $\omega$ | Omega | o |

*\*Nota: La lettera Sigma ha due forme minuscole: $\sigma$ si usa all'interno delle parole, mentre $\varsigma$ si usa solo alla fine della parola.*

---

### Tabella di riepilogo rapido (Solo lettere)
Se ti serve solo una lista veloce da copiare e incollare:

**Maiuscole:**
Α, Β, Γ, Δ, Ε, Ζ, Η, Θ, Ι, Κ, Λ, Μ, Ν, Ξ, Ο, Π, Ρ, Σ, Τ, Υ, Φ, Χ, Ψ, Ω

**Minuscole:**
α, β, γ, δ, ε, ζ, η, θ, ι, κ, λ, μ, ν, ξ, ο, π, ρ, σ, τ, υ, φ, χ, ψ, ω


## Nomenclatura probabilistica

- $\Omega$ si definisce **evento certo**;
- $\emptyset \space$ si definisce **evento impossibile**;
- $A$ e $A^c$ si definiscono **eventi complementari**;
- Due eventi $A$ e $B$ tali che $A \cap B = \emptyset \space$ si definiscono **incompatibili** o **mutuamente esclusivi**;
- Se $A \subseteq B$ si dice che $A$ **implica** $B$, cioè il verificarsi di $A$ implica che si verifichi $B$.

### 1. pmf (Probability Mass Function)

* **Quando si usa:** Solo per variabili **discrete** (numeri isolati, es. $X = 1, 2, 3$).
* **La formula:** 
$$p_X(x) = \mathbb{P}(X = x)$$

* **Cosa fa:** Ti dà la probabilità **esatta e puntuale** di un singolo valore. Se inserisci $x=2$, ti sputa fuori la probabilità esatta che esca 2. La somma di tutte le pmf fa 1 ($\sum p_X(x) = 1$).

### 2. pdf (Probability Density Function)

* **Quando si usa:** Solo per variabili **continue** (valori reali infiniti, es. tempo, altezza, peso).
* **La formula:** 
$$\mathbb{P}(a \leq X \leq b) = \int_{a}^{b} f_X(x) \, dx$$

* **Cosa fa:** Nelle variabili continue la probabilità di un punto esatto è zero ($\mathbb{P}(X=2) = 0$). Quindi la formula della pdf **non è una probabilità**, ma una funzione di densità (l'altezza di una curva). Per trovare la probabilità devi calcolare un **integrale** (l'area sotto la curva) tra due punti. L'area totale sotto la curva fa 1 ($\int_{-\infty}^{+\infty} f_X(x)dx = 1$).

### 3. DF (Distribution Function / Funzione di Ripartizione)

* **Quando si usa:** Per **qualsiasi** tipo di variabile (sia discrete che continue).
* **La formula:** 
$$F_X(x) = \mathbb{P}(X \leq x)$$

* **Cosa fa:** È una formula **cumulativa**. Non ti dice la probabilità di un punto fisso, ma la probabilità che la variabile sia *minore o uguale* a quel punto (accumula la probabilità da $-\infty$ fino a $x$).
* Se la variabile è *discreta*, la DF si calcola con una **somma**: $F_X(x) = \sum_{x_i \leq x} p_X($x_i$)$
* Se la variabile è *continua*, la DF si calcola con un **integrale**: $F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt$


## 2. Funzioni di Distribuzione

### 1. pmf (Probability Mass Function)

> [!important] Probability Mass Function (pmf)
> La **funzione di massa di probabilità** $p_X(x)$ è definita per le variabili aleatorie discrete come:
> $$p_X(x) = \mathbb{P}(X = x)$$

La pmf viene utilizzata quando i possibili risultati di una variabile aleatoria sono isolati e numerabili (es. il numero di figli, il risultato di un lancio di dadi). Serve a fornire la probabilità esatta associata a ogni singolo valore possibile del dominio. 

> [!important] Sintesi Matematica
> $$p_X(x) = \mathbb{P}(X = x)$$
> $$\sum_{x} p_X(x) = 1$$

Richiede: **Variabile Aleatoria**. Usato in: **Distribuzione di Poisson**, **Distribuzione Binomiale**.

> [!warning] Attenzione
> La pmf è definita solo per variabili **discrete**. Per una variabile continua, la probabilità puntuale $\mathbb{P}(X=x)$ è sempre zero, rendendo la pmf non utile.

### 2. pdf (Probability Density Function)

> [!important] Probability Density Function (pdf)
> La **funzione di densità di probabilità** $f_X(x)$ è definita per le variabili aleatorie continue e descrive la distribuzione della probabilità tramite l'area sottesa alla curva:
> $$\mathbb{P}(a \leq X \leq b) = \int_{a}^{b} f_X(x) \, dx$$

Nelle variabili continue (come il tempo di attesa o l'altezza), la probabilità che una variabile assuma un valore esatto è nulla ($\mathbb{P}(X=x)=0$). La pdf risolve questo problema non fornendo probabilità puntuali, ma "densità": la probabilità viene calcolata come l'area sotto la curva in un intervallo.

> [!important] Sintesi Matematica
> $$\mathbb{P}(a \leq X \leq b) = \int_{a}^{b} f_X(x) \, dx$$
> $$\int_{-\infty}^{+\infty} f_X(x)dx = 1$$

Richiede: **Variabile Aleatoria**. Usato in: **Distribuzione Normale**, **Distribuzione Esponenziale**.

> [!warning] Attenzione
> Un errore comune è confondere il valore di $f_X(x)$ con la probabilità. Il valore della funzione può essere maggiore di 1 (poiché è una densità, non una probabilità), mentre la probabilità deve sempre essere $\leq 1$.

### 3. DF (Distribution Function / Funzione di Ripartizione)

> [!important] Funzione di Ripartizione (DF)
> La **funzione di ripartizione** $F_X(x)$ è una funzione cumulativa che indica la probabilità che la variabile aleatoria $X$ assuma un valore minore o uguale a $x$:
> $$F_X(x) = \mathbb{P}(X \leq x)$$

La DF è lo strumento universale per descrivere la distribuzione di una variabile, indipendentemente dal fatto che sia discreta o continua. Permette di calcolare facilmente probabilità su intervalli e fornisce un ponte matematico tra pmf e pdf.

La DF può essere ricavata dalle altre funzioni di distribuzione in base alla natura della variabile:
1. **Caso Discreto:** La DF è la somma cumulativa delle masse di probabilità:
   $$F_X(x) = \sum_{x_i \leq x} p_X(x_i)$$
2. **Caso Continuo:** La DF è l'integrale della densità fino al punto $x$:
   $$F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt$$

> [!important] Sintesi Matematica
> $$F_X(x) = \mathbb{P}(X \leq x)$$
> Discreta: $F_X(x) = \sum_{x_i \leq x} p_X($x_i$)$
> Continua: $F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt$

Richiede: **Variabile Aleatoria**. Usato in: **Calcolo di probabilità su intervalli**, **Teorema di Distribuzione Cumulativa**.