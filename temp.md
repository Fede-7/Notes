# Fondamenti di Probabilità

## Definizioni

**Esperimento**  
Operazione o azione il cui esito produce uno tra diversi risultati possibili.

**Spazio dei campioni** ($\\Omega$)  
Insieme di tutti i risultati possibili di un esperimento. Si assume discreto (finito o numerabile).

**Evento**  
Sotto-insieme di $\\Omega$.

**Evento elementare** ($\\omega$)  
Elemento di $\\Omega$.

---

## Insiemistica

Siano ${A\_i}\_{i=1}^M$ sotto-insiemi di $\\Omega$:

1. **Unione**: $A\_1 \\cup A\_2$
2. **Complemento**: $\\overline{A\_1} = \\Omega \\setminus A\_1$
  - $\\overline{\\Omega} = \\emptyset$
  - $\\overline{\\overline{A\_1}} = A\_1$
  - $A\_1 \\cup \\overline{\\overline{A\_1}} = \\Omega$
3. **Intersezione**: $A\_1 \\cap A\_2$
4. **Sottrazione**: $A\_1 \\setminus A\_2 = A\_1 \\cap \\overline{A\_2}$
5. **De Morgan**:  
 $$\\overline{A\_1 \\cup A\_2} = \\overline{A\_1} \\cap \\overline{A\_2}$$  
 $$\\overline{\\overline{A\_1} \\cup \\overline{A\_3}} = A\_1 \\cap A\_2$$
6. **Associatività**:  
 $$(A\_1 \\cup A\_2) \\cup A\_3 = A\_1 \\cup (A\_2 \\cup A\_3)$$  
 $$(A\_1 \\cap A\_2) \\cap A\_3 = A\_1 \\cap (A\_2 \\cap A\_3)$$
7. **Distributività**:  
 $$A\_1 \\cup \\left(\\bigcap\_{i=2}^M A\_i\\right) = \\bigcap\_{i=2}^M (A\_1 \\cup A\_i)$$  
 $$A\_1 \\cap \\left(\\bigcup\_{i=2}^M A\_i\\right) = \\bigcup\_{i=2}^M (A\_1 \\cap A\_i)$$

---

## Nomenclatura Probabilistica

- **Evento certo**: $\\Omega$
- **Evento impossibile**: $\\emptyset$
- **Eventi complementari**: $A$ e $\\overline{A}$
- **Eventi incompatibili**: $A \\cap B = \\emptyset$
- **Implicazione**: $A \\subseteq B$ significa che $A$ implica $B$

---

## Spazi Finiti con Eventi Elementari Equiprobabili

Sia $\\Omega$ uno spazio dei campioni finito con eventi elementari equiprobabili.  
Per $A \\subseteq \\Omega$:  
$$\\mathbb{P}(A) = \\frac{|A|}{|\\Omega|}$$

---

## Calcolo Combinatorio

### Prodotto Cartesiano

Siano $A\_1, \\ldots, A\_k$ insiemi finiti:  
$$|A\_1 \\times \\cdots \\times A\_k| = \\prod\_{i=1}^k |A\_i|$$

### k-ple Ordinate senza Ripetizione

Sia $A = {a\_1, \\ldots, a\_n}$.  
Numero di stringhe di lunghezza $k$ senza ripetizioni:  
$$n(n-1)\\cdots(n-k+1) = \\prod\_{i=0}^{k-1} (n-i)$$

### Permutazioni

Numero di $n$-ple ordinate di $n$ elementi:  
$$n!$$

### Combinazioni

$$\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$$

### Insieme delle Parti

Sia $A$ un insieme con $n$ elementi:  
$$|\\mathcal{P}(A)| = \\sum\_{k=0}^n \\binom{n}{k} = 2^n$$

---

## Probabilità su Spazi Discreti

### Definizione

$$\\mathbb{P}(A) = \\lim\_{n \\to \\infty} \\frac{n\_A}{n}$$

### Spazi con Eventi Elementari Equiprobabili

$$\\mathbb{P}(A) = \\frac{|\\Omega\_A|}{|\\Omega|}$$

### Proprietà

1. **Eventi complementari**:  
 $$\\mathbb{P(\\overline{A})} = 1 - \\mathbb{P}(A)$$
2. **Sub-additività**:  
 $$\\mathbb{P}(A \\cup B) = \\mathbb{P}(A) + \\mathbb{P}(B) - \\mathbb{P}(A \\cap B)$$
3. **Sottrazione tra insiemi**:  
 $$\\mathbb{P}(A \\setminus B) = \\mathbb{P}(A) - \\mathbb{P}(A \\cap B)$$
4. **Evento certo e impossibile**:  
 $$\\mathbb{P}(\\Omega) = 1, \\quad \\mathbb{P}(\\emptyset) = 0$$

---

## Probabilità Condizionata

$$\\mathbb{P}(A \\mid B) = \\frac{\\mathbb{P}(A \\cap B)}{\\mathbb{P}(B)}$$

### Legge della Probabilità Composta

$$\\mathbb{P}(A \\cap B) = \\mathbb{P}(A \\mid B)\\mathbb{P}(B) = \\mathbb{P}(B \\mid A)\\mathbb{P}(A)$$

---

## Legge della Probabilità Totale

Sia ${B\_i}*{i=1}^k$ una partizione di $\\Omega$:*  
*$$\\mathbb{P}(A) = \\sum*{i=1}^k \\mathbb{P}(A \\cap B\_i) = \\sum\_{i=1}^k \\mathbb{P}(A \\mid B\_i)\\mathbb{P}(B\_i)$$

---

## Eventi Indipendenti

$A$ e $B$ indipendenti $\\iff \\mathbb{P}(A \\cap B) = \\mathbb{P}(A)\\mathbb{P}(B)$

---

## Approccio Assiomatico

### Algebra di Eventi

$\\mathcal{E}$ è un'algebra di sotto-insiemi di $\\Omega$ se:

1. $A\_1, A\_2 \\in \\mathcal{E} \\implies A\_1 \\cup A\_2 \\in \\mathcal{E}$
2. $A \\in \\mathcal{E} \\implies \\overline{A} \\in \\mathcal{E}$

### $\\sigma$-algebra

$\\mathcal{E}$ è una $\\sigma$-algebra se è un'algebra e:

- $\\bigcup\_{i=1}^\\infty A\_i \\in \\mathcal{E}$ per ogni collezione numerabile ${A\_i}\_{i \\in \\mathbb{N}} \\subseteq \\mathcal{E}$

### Assiomi di Kolmogorov

1. **Non negatività**: $\\mathbb{P}(A) \\geq 0 \\ \\forall A \\in \\mathcal{E}$
2. **Normalizzazione**: $\\mathbb{P}(\\Omega) = 1$
3. **$\\sigma$-additività**: Se ${B\_n}*{n \\in \\mathbb{N}}$ sono incompatibili, allora*  
 *$$\\mathbb{P}\\left(\\bigcup*{n=1}^\\infty B\_n\\right) = \\sum\_{n=1}^\\infty \\mathbb{P}(B\_n)$$

### Spazio di Probabilità

$(\\Omega, \\mathcal{E}, \\mathbb{P})$

### Proprietà delle Leggi di Probabilità

1. **Eventi complementari**:  
 $\\mathbb{P(\\overline{A})} = 1 - \\mathbb{P}(A)$
2. **Sottrazione tra insiemi**:  
 $\\mathbb{P}(A \\setminus B) = \\mathbb{P}(A) - \\mathbb{P}(A \\cap B)$
3. **Unione di eventi non incompatibili**:  
 $\\mathbb{P}(A \\cup B) = \\mathbb{P}(A) + \\mathbb{P}(B) - \\mathbb{P}(A \\cap B)$

---

## Variabile Aleatoria

$X: \\Omega \\to \\mathbb{R}$

---

## Funzioni di Distribuzione

- **pmf (Probability Mass Function)**:  
$p\_X(x) = \\mathbb{P}(X = x)$  
Proprietà: $p\_X(x) \\geq 0$, $\\sum\_{x \\in \\mathcal{X}} p\_X(x) = 1$
- **pdf (Probability Density Function)**:  
$f\_X(x)$ per variabili continue
- **DF (Funzione di Ripartizione)**:  
$F\_X(x) = \\mathbb{P}(X \\leq x)$
  - Caso discreto: $F\_X(x) = \\sum\_{x\_i \\leq x} p\_X(x\_i)$
  - Caso continuo: $F\_X(x) = \\int\_{-\\infty}^x f\_X(t) , dt$

---

## Media Campionaria

$$\\overline{X\_n} = \\frac{1}{n} \\sum\_{i=1}^n X(\\omega\_i)$$

---

## Valore Atteso / Media Statistica

$$\\mathbb{E}\[X\] = \\sum\_{x \\in \\mathcal{X}} x p\_X(x)$$

---

## Distribuzioni Specifiche

### Uniforme

$X \\sim \\mathcal{U}(\\mathcal{X})$, $|\\mathcal{X}| = M$  
$p\_X(x) = \\frac{1}{M} \\ \\forall x \\in \\mathcal{X}$  
$\\mathbb{E}\[X\] = \\frac{1}{M} \\sum\_{x \\in \\mathcal{X}} x$

### Poisson

$X \\sim \\mathcal{P}(\\lambda)$  
$p\_X(k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}$, $k \\in \\mathbb{N}\_0$  
$\\mathbb{E}\[X\] = \\lambda$

---

## PMF Condizionali

$$p\_{X \\mid A}(x) = \\mathbb{P}(X = x \\mid A) = \\frac{\\mathbb{P({X = x} \\cap A)}}{\\mathbb{P}(A)}$$

---

## Regola della Probabilità Totale per le PMF

Sia ${E\_i}*{i=1}^M$ una partizione di $\\Omega$:*  
*$$p\_X(x) = \\sum*{i=1}^M p\_{X \\mid E\_i}(x) \\mathbb{P}(E\_i)$$

---

## Medie Condizionali

$$\\mathbb{E}\[X \\mid E\_i\] = \\sum\_{x \\in \\mathcal{X}} x p\_{X \\mid E\_i}(x)$$

$$\\mathbb{E}\[X\] = \\sum\_{i=1}^M \\mathbb{P}(E\_i) \\mathbb{E}\[X \\mid E\_i\]$$

---

## Funzioni di Variabili Aleatorie

Sia $Y = g(X)$.

### PMF di $Y$

1. **Funzione biunivoca**:  
 $p\_Y(y) = p\_X(g^{-1}(y))$
2. **Funzione non biunivoca**:  
 Sia $\\mathcal{A}(y) = {x \\in \\mathcal{X} \\mid g(x) = y}$  
 $p\_Y(y) = \\sum\_{x \\in \\mathcal{A}(y)} p\_X(x)$

### Media di Funzioni di Variabili Aleatorie

$$\\mathbb{E}\[g(X)\] = \\sum\_{x \\in \\mathcal{X}} g(x) p\_X(x)$$

**Teorema Fondamentale per il Calcolo della Media**:  
$\\mathbb{E}\[g(X)\] = \\sum\_{y} g(y) p\_Y(y)$ dove $Y = g(X)$

---

## Valore Quadratico Medio e Varianza

- **Valore quadratico medio**:  
$X\_{\\text{rms}}^2 = \\mathbb{E}\[X^2\] = \\sum\_{x \\in \\mathcal{X}} x^2 p\_X(x)$
- **Valore efficace (rms)**:  
$X\_{\\text{rms}} = \\sqrt{\\mathbb{E}\[X^2\]}$
- **Varianza**:  
$\\sigma\_X^2 = \\mathbb{E}\[(X - \\mu\_X)^2\] = \\mathbb{E}\[X^2\] - \\mu\_X^2$
- **Deviazione standard**:  
$\\sigma\_X = \\sqrt{\\sigma\_X^2} = \\sqrt{\\mathbb{E}\[X^2\] - \\mu\_X^2}$

---

## Disuguaglianza di Chebyshev

$$\\mathbb{P}{|X - \\mu\_X| &gt; k\\sigma\_X} \\leq \\frac{1}{k^2}$$

---

## Proprietà di Media e Varianza

### Media ($\\mathbb{E}$)

- **Linearità**: $\\mathbb{E}\[aX + b\] = a\\mathbb{E}\[X\] + b$
- **Non-negatività**: Se $X \\geq 0$ allora $\\mathbb{E}\[X\] \\geq 0$

### Varianza ($\\sigma^2$)

- **Non-negatività**: $\\sigma\_X^2 \\geq 0$
- **Trasformazione lineare**: Se $Y = aX + b$ allora $\\sigma\_Y^2 = a^2 \\sigma\_X^2$
- **Relazione**: $\\sigma\_X^2 = X\_{\\text{rms}}^2 - \\mu\_X^2$

---

## Variabili Multiple

### Definizione

$(X, Y): \\Omega \\to \\mathcal{X} \\times \\mathcal{Y} \\subseteq \\mathbb{R}^2$

### pmf Congiunta

$$p\_{X,Y}(x,y) = \\mathbb{P}(X = x, Y = y)$$

**Proprietà**:

- $p\_{X,Y}(x,y) \\geq 0$
- $\\sum\_{x \\in \\mathcal{X}} \\sum\_{y \\in \\mathcal{Y}} p\_{X,Y}(x,y) = 1$

### Marginalizzazione

$$p\_X(x) = \\sum\_{y \\in \\mathcal{Y}} p\_{X,Y}(x,y), \\quad p\_Y(y) = \\sum\_{x \\in \\mathcal{X}} p\_{X,Y}(x,y)$$

### Indipendenza

$X$ e $Y$ indipendenti $\\iff p\_{X,Y}(x,y) = p\_X(x) p\_Y(y)$

### pmf Condizionata

$$p\_{Y\\mid X}(y\\mid x) = \\frac{p\_{X,Y}(x,y)}{p\_X(x)}, \\quad p\_{X\\mid Y}(x\\mid y) = \\frac{p\_{X,Y}(x,y)}{p\_Y(y)}$$

### Legge di Bayes

$$p\_{X\\mid Y}(x\\mid y) = \\frac{p\_{Y\\mid X}(y\\mid x) p\_X(x)}{p\_Y(y)}$$

### Regola della Catena

$$p\_{X,Y,Z}(x,y,z) = p\_{Z\\mid X,Y}(z\\mid x,y) p\_{Y\\mid X}(y\\mid x) p\_X(x)$$

### Generalizzazione a $m$ Variabili

$p\_{X\_1, \\ldots, X\_m}(x\_1, \\ldots, x\_m) = \\prod\_{i=1}^m p\_{X\_i}(x\_i)$ se indipendenti

---

## Funzioni di Variabili Doppie

$Z = g(X, Y)$

### PMF di $Z$

1. **Trasformazione biunivoca**:  
 $p\_Z(z) = p\_{X,Y}(x(z), y(z))$
2. **Trasformazione non biunivoca**:  
 Sia $\\mathcal{A}(z) = {(x,y) \\in \\mathcal{X} \\times \\mathcal{Y} \\mid g(x,y) = z}$  
 $p\_Z(z) = \\sum\_{(x,y) \\in \\mathcal{A}(z)} p\_{X,Y}(x,y)$

### Media di Funzioni di Variabili Doppie

$$\\mathbb{E}\[g(X,Y)\] = \\sum\_{x \\in \\mathcal{X}} \\sum\_{y \\in \\mathcal{Y}} g(x,y) p\_{X,Y}(x,y)$$

**Linearità del Valore Atteso**:  
$$\\mathbb{E}\[aX + bY\] = a\\mathbb{E}\[X\] + b\\mathbb{E}\[Y\]$$

**Generalizzazione a $m$ variabili**:  
$$\\mathbb{E}\\left\[\\sum\_{i=1}^m a\_i X\_i\\right\] = \\sum\_{i=1}^m a\_i \\mathbb{E}\[X\_i\]$$

### Teorema della Media Condizionata

$$\\mathbb{E}\[g(X,Y)\] = \\sum\_{y \\in \\mathcal{Y}} p\_Y(y) \\mathbb{E}\[g(X,Y) \\mid Y = y\]$$

Dove:  
$$\\mathbb{E}\[g(X,Y) \\mid Y = y\] = \\sum\_{x \\in \\mathcal{X}} g(x,y) p\_{X\\mid Y}(x\\mid y)$$
