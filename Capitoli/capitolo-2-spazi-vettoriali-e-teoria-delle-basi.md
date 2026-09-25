# Capitolo 2: Spazi Vettoriali e Teoria delle Basi

---

## 2.1 Lo Spazio Vettoriale

### 2.1.1 Definizione di Spazio Vettoriale

**Def.** Uno SPAZIO VETTORIALE su $K$ è una QUATERNIA $(V, K, \oplus, \odot)$, dove:

→ $V$ è un Insieme, non vuoto, di Vettori 
→ $(K, +, \cdot)$ è un CAMPO (Scalari) 
→ $\oplus: V \times V \longrightarrow V$ t.c. $(V, \oplus)$ è un GRUPPO ABELIANO 
→ $\odot: K \times V \longrightarrow V$ t.c. $(\alpha, \mu) \longrightarrow \alpha \odot \mu$

I) $\forall \space  \alpha, \beta \in K, \forall \space  \mu, \nu \in V, (\alpha + \beta) \odot \mu = (\alpha \odot \mu) \oplus (\beta \odot \mu)$ 
II) $\forall \space  \alpha \in K, \forall \space  \mu, \nu \in V, \alpha \odot (\mu \oplus \nu) = (\alpha \odot \mu) \oplus (\alpha \odot \nu)$ 
III) $\forall \space  \alpha, \beta \in K, \forall \space  \mu \in V, (\alpha \cdot \beta) \odot \mu = \alpha \odot (\beta \odot \mu)$ 
IV) $\exists \space  1 \in K, \forall \space  \mu \in V, 1 \odot \mu = \mu$ (elemento neutro)

---

### 2.1.2 Esempi di Spazi Vettoriali

#### Esempio 1: Vettori Liberi

$\mathcal{V} = \left\{ \overrightarrow{PQ} \mid P, Q \text{ P.T.} \right\}$ dello spazio della geometria elementare (LIBERO) 
$\oplus: \mathcal{V} \times \mathcal{V} \longrightarrow \mathcal{V}$ 
A due vettori liberi $\mu$ e $\nu$ associamo il vettore ottenuto nel seguente modo: $\mu = \overrightarrow{PQ}$, applicazione $\nu$ in $\alpha$, ottenendo con $\nu = \overrightarrow{QR} \Rightarrow \mu + \nu = \overrightarrow{PR}$

#### Esempio 2: Prodotto per Scalare su Vettori Liberi

$\odot: \mathbb{R} \times \mathcal{V} \longrightarrow \mathcal{V}$ 
$(\alpha, \mu) \longrightarrow \alpha \odot \mu$ 
Se: $\mu = \overrightarrow{PQ}$, Allora $\alpha \odot \mu = \begin{cases} \vec{0} = \overrightarrow{PP}, \text{ se } \alpha = 0 \\ \vec{v}, \text{ con direzione uguale, verso uguale e lunghezza } \ell = |\alpha| \cdot ||\mu|| \\ \vec{v}, \text{ con direzione uguale, verso opposto e lunghezza } \ell = |\alpha| \cdot ||\mu|| \end{cases}$

#### Esempio 3: Spazio Vettoriale Numerico

$(K, +, \cdot)$ è un CAMPO 
$\mathcal{V} = K^m$, $m \in \mathbb{N}$, $m \geq 0$ 
$\oplus: K^m \times K^m \longrightarrow K^m$ 
$( (a_1, \dots, a_m), (b_1, \dots, b_m) ) \sim \longrightarrow (a_1 + b_1, \dots, a_m + b_m)$ 
$\odot: K \times K^m \longrightarrow K^m$ 
$(\alpha, (a_1, \dots, a_m)) \sim \longrightarrow (\alpha \cdot a_1, \alpha \cdot a_2, \dots, \alpha \cdot a_m)$ 
$(K^m, K, \oplus, \odot)$ è uno SPAZIO VETTORIALE su $K$, detto anche spazio vettoriale numerico/standard/convesso su $K$ (es: $\mathbb{R}^3$): $(2, -5) \oplus (3, 2) = (5, 2)$

---

### 2.1.3 Definizione Alternativa di Spazio Vettoriale

Definizione: Uno **SPAZIO VETTORIALE** su un campo $(K, +, \cdot)$ è una **QUATERNIA** $(V, K, \oplus, \odot)$, dove:

→ $K$ è il **SOSTEGNO** di un campo di scalari 
→ $V$ è un **Insieme** non vuoto di vettori 
→ $\oplus : V \times V \longrightarrow V$ t.c. $(V, \oplus)$ è un **GRUPPO ABELIANO** 
→ $\odot : K \times V \longrightarrow V$ **operazione esterna** t.c.:

I) $\forall \space  \alpha, \beta \in K, \forall \space  \mu \in V, (\alpha + \beta) \odot \mu = (\alpha \odot \mu) \oplus (\beta \odot \mu)$ 
II) $\forall \space  \alpha \in K, \forall \space  \mu, \nu \in V, \alpha \odot (\mu \oplus \nu) = (\alpha \odot \mu) \oplus (\alpha \odot \nu)$ 
III) $\forall \space  \alpha, \beta \in K, \forall \space  \mu \in V, (\alpha \cdot \beta) \odot \mu = \alpha \odot (\beta \odot \mu)$ 
IV) $\exists \space  1 \in K$, **elemento neutro** rispetto a $\cdot$, $\forall \space  \mu \in V$, $1 \odot \mu = \mu$

---

### 2.1.4 Esempi per $V = K^m$

1) $\oplus : K^m \times K^m \longrightarrow K^m$ 
$((a_1, \dots, a_m), (b_1, \dots, b_m)) \longrightarrow (a_1 + b_1, \dots, a_m + b_m)$

2) $\odot : K \times K^m \longrightarrow K^m$ 
$(\alpha, (a_1, \dots, a_m)) \longrightarrow (\alpha a_1, \dots, \alpha a_m)$

---

### 2.1.5 Verifica delle Proprietà per $K^m$

#### Proprietà Commutativa di $\oplus$
$(a_1, a_2), (b_1, b_2) \in \mathbb{R}^2$ 
$(a_1, a_2) \oplus (b_1, b_2) \overset{def}{=} (a_1 + b_1, a_2 + b_2) = (b_1 + a_1, b_2 + a_2)$ 
$\overset{def}{=} (b_1, b_2) \oplus (a_1, a_2)$

#### Proprietà Associativa di $\oplus$
$(a_1, a_2), (b_1, b_2), (c_1, c_2) \in \mathbb{R}^2$ 
$((a_1, a_2) \oplus (b_1, b_2)) \oplus (c_1, c_2) \overset{def}{=} (a_1 + b_1, a_2 + b_2) \oplus (c_1, c_2) = (a_1 + b_1 + c_1, a_2 + b_2 + c_2)$ 
$\overset{def}{=} (a_1, a_2) \oplus ((b_1, b_2) \oplus (c_1, c_2))$

#### Elemento Neutro
Teo: $\exists \space  (x_1, x_2) \in \mathbb{R}^2, \forall \space  (a_1, a_2) \in \mathbb{R}^2, (x_1, x_2) \oplus (a_1, a_2) = (a_1, a_2)$ 
$\Leftrightarrow (x_1 + a_1, x_2 + a_2) = (a_1, a_2) \Leftrightarrow \begin{cases} x_1 + a_1 = a_1 \\ x_2 + a_2 = a_2 \end{cases} \Rightarrow \begin{cases} x_1 = 0 \\ x_2 = 0 \end{cases}$

#### Elemento Inverso
Teo: $\forall \space  (a_1, a_2) \in \mathbb{R}^2, \exists \space  (\overline{a_1}, \overline{a_2}) \in \mathbb{R}^2: (a_1, a_2) \oplus (\overline{a_1}, \overline{a_2}) = (0, 0) \Leftrightarrow \begin{cases} a_1 + \overline{a_1} = 0 \\ a_2 + \overline{a_2} = 0 \end{cases} \Rightarrow \begin{cases} \overline{a_1} = -a_1 \\ \overline{a_2} = -a_2 \end{cases}$

---

### 2.1.6 Proprietà Algebriche di $(V, K, \oplus, \odot)$

#### Proprietà I
$\forall \space  \alpha \in K, \forall \space  \vec{u} \in V$:
$$\alpha \odot \vec{u} = \vec{0} \iff \alpha = 0 \quad \text{oppure} \quad \vec{u} = \vec{0}$$

---

##### Dimostrazione: "$\Leftarrow$ (i)"

**Th:** $\alpha \odot \vec{0} = \vec{0}$

$$\alpha \odot \vec{0} = \alpha \odot (\vec{0} \oplus \vec{0}) = (\alpha \odot \vec{0}) \oplus (\alpha \odot \vec{0})$$

- Da cui: $\alpha \odot \vec{0} = (\alpha \odot \vec{0}) \oplus (\alpha \odot \vec{0})$

$$\Rightarrow \alpha \odot \vec{0} \oplus (-(\alpha \odot \vec{0})) = \vec{0} \oplus \vec{0} = \vec{0}$$

$$\Rightarrow \alpha \odot \vec{0} = \vec{0}$$

---

##### Dimostrazione: "$\Leftarrow$ (ii)"

**Th:** $\vec{0} \odot \vec{u} = \vec{0}$

$$\vec{0} \odot \vec{u} = (0 + 0) \odot \vec{u} = (0 \odot \vec{u}) \oplus (0 \odot \vec{u})$$

$$(0 \odot \vec{u}) \oplus (- (0 \odot \vec{u})) = (0 \odot \vec{u}) \oplus (0 \odot \vec{u}) \oplus (- (0 \odot \vec{u})) = 0$$

$$\Rightarrow \vec{0} = 0 \odot \vec{u}$$

---

##### Dimostrazione: "$\Rightarrow$"

**Ip:** $\alpha \odot \vec{u} = \vec{0}$

Se $\alpha \neq 0$, allora $\exists \space  \alpha^{-1} \in K$ tale che:

$$\alpha^{-1} \odot (\alpha \odot \vec{u}) = \alpha^{-1} \odot \vec{0} = \vec{0}$$

$$\Rightarrow \alpha^{-1} \odot \vec{0} = \vec{0} \quad \text{per concludere}$$

---

**Nota:** Bisogna dimostrazione più in generale che $\alpha \odot \vec{0} = \vec{0}, \forall \space  \alpha \in \mathbb{R}$

---

### 2.1.7 Proprietà di un'operazione binaria su uno spazio vettoriale

$$\text{I)} \ \forall \space  \alpha, \beta \in K, \ \forall \space  \mu \in V \setminus \{0\} \quad \alpha \odot \mu = \beta \odot \mu \ \Rightarrow \ \alpha = \beta$$

$$\text{II)} \ \forall \space  \alpha \in K \setminus \{0\}, \ \forall \space  \mu, \nu \in V \quad \alpha \odot \mu = \alpha \odot \nu \ \Rightarrow \ \mu = \nu$$

$$\text{III)} \ \forall \space  \alpha \in K, \ \forall \space  \mu \in V \quad -(\alpha \odot \mu) = (-\alpha) \odot \mu = \alpha \odot (-\mu)$$

---

#### Dimostrazione

##### (i)

**Th**: $(-\alpha) \odot \mu$ è l'**opposto** di $\alpha \odot \mu$

$$\begin{align*}
[(-\alpha) \odot \mu] \oplus [\alpha \odot \mu] &\overset{\text{(I)}}{=} [(-\alpha) + \alpha] \odot \mu = 0 \odot \mu = \Omega \\
[\alpha \odot (-\mu)] \oplus [\alpha \odot \mu] &\overset{\text{(II)}}{=} \alpha \odot [(-\mu) \oplus \mu] = \alpha \odot \Omega = \Omega
\end{align*}$$

##### (ii)

$$\begin{align*}
(\alpha \odot \mu) \oplus [-(\beta \odot \mu)] &= \Omega \\
(\alpha \odot \mu) \oplus [(-\beta) \odot \mu] &\overset{\text{(I)}}{=} (\alpha + (-\beta)) \odot \mu \\
&\Downarrow \quad \mu \neq \Omega \\
\alpha + (-\beta) &= 0 \\
\alpha &= \beta
\end{align*}$$

##### (iii)

$$\begin{align*}
(\alpha \odot \mu) \oplus [-(\alpha \odot \nu)] &= \Omega \\
(\alpha \odot \mu) \oplus [\alpha \odot (-\nu)] &\overset{\text{(I)}}{=} \alpha \odot [\mu \oplus (-\nu)] \Rightarrow \mu \oplus (-\nu) = \Omega \\
&\Downarrow \\
\mu &= \nu \quad \square
\end{align*}$$

---

## 2.2 Sottospazi Vettoriali

### 2.2.1 Definizione di Sottospazio Vettoriale

- **Def**: $(V, +, \cdot)$ spazio vettoriale su un campo $K$, un sottoinsieme $W \subseteq V$ si dice **SOTTOSPAZIO VETTORIALE** di $V$, se:

I) $W$ è linearmente chiuso (quindi: $+|W \times W : W \times W \to W$ e $\cdot|K \times W : K \times W \to W$)

II) $(W, +|W \times W, \cdot|K \times W)$ è uno **SPAZIO VETTORIALE** su $K$

---

### 2.2.2 Operazioni Ristrette

$g: A \longrightarrow B$ APPLICAZIONE

- $x \in A : g|_x : X \longrightarrow B$ "Applicazione $g$ ristretta a $X \subseteq A$"

- $Y \subseteq A : \exists \space  m g \in Y, g: A \longrightarrow Y$ Restringo $\{g(a) | a \in A\}$ il codominio

$\Rightarrow$ Se: $X \subseteq A$ e $g(x) \in Y \subseteq B$, posso prendere: $g|_x : X \longrightarrow Y$

---

### 2.2.3 Proposizione Fondamentale sui Sottospazi

- Ogni sottinsieme $W \subseteq V$ LINEARMENTE CHIUSO è uno SOTTOSPAZIO VETTORIALE ($\Leftrightarrow$ è chiuso)

---

#### Dimostrazione:

- $1_W \times W : W \times W \longrightarrow W$
 $(u, v) \sim u + v$

- $1_{K \times W} : K \times W \longrightarrow W$
 $(\alpha, u) \sim \alpha u$

 $$
 \begin{cases}
 \text{* Operazioni di } V \\
 \text{* Operazioni di } V
 \end{cases}
 $$

- $\exists \space  0 \in V, W \neq \emptyset \Rightarrow \exists \space  \mu \in W \Rightarrow 0 \cdot \mu = 0 \in W$

- $\forall \space  u \in W, \exists \space  -\mu \in W$
 $-\mu = (-1) \mu \in W$

$\Rightarrow$ Per le proprietà: *Autometiche*

*Tutte le altre proprietà dello spazio vettoriale vengono ereditate immediatamente con le operazioni*

---

### 2.2.4 Esempio di Sottospazio Vettoriale

$(V, +, \cdot)$ Spazio vettoriale su $K$

$\{0\}$ è un SOTTOSPAZIO VETTORIALE

---

## 2.3 Generatori e Dipendenza Lineare

### 2.3.1 Combinazione Lineare

Dati dei vettori $\mu_1, \dots, \mu_t \in V$ e degli scalari $\alpha_1, \dots, \alpha_t \in K$, la **COMBINAZIONE LINEARE** dei vettori dati mediante gli scalari è il seguente vettore:

$\alpha_1 \mu_1 + \dots + \alpha_t \mu_t$

---

*N.B.* Se vogliamo permettere che ci siano ripetizioni tra i vettori e gli scalari, allora considereremo $t$-uple $(\mu_1, \dots, \mu_t) \in V^t$, $(\alpha_1, \dots, \alpha_t) \in K^t$
$\alpha_1 \mu_1 + \dots + \alpha_t \mu_t$

---

### 2.3.2 Chiusura Lineare

Sia $X \subseteq V$, dove $V$ è uno spazio vettoriale su $K$.

La **chiusura lineare** di $X$, denotata $\mathcal{L}(X)$, oppure $\langle X \rangle$, è l'insieme:

$$\mathcal{L}(X) = \left\{ \alpha_1 \mu_1 + \dots + \alpha_t \mu_t \ \Big| \ \mu_1, \dots, \mu_t \in X, \ \alpha_1, \dots, \alpha_t \in K \right\}$$

---

### 2.3.3 Sistema di Generatori

Sia $S \subseteq V$. Si dice che $S$ è un **sistema di generatori** di $V$ se ogni vettore di $V$ è una combinazione lineare dei vettori di $S$, cioè:

$$V = \mathcal{L}(S)$$

---

### 2.3.4 Spazio Vettoriale Finitamente Generato

Uno spazio vettoriale $V$ si dice **finitamente generato** se ammette un sistema di generatori finito.

---

### 2.3.5 Proposizione sulla Chiusura Lineare

Sia $X \subseteq V$.

I) $X \subseteq \mathcal{L}(X)$

II) $\mathcal{L}(X)$ è un **sottospazio vettoriale** di $V$

III) Se $W \subseteq V$ è un sottospazio vettoriale di $V$, e $X \subseteq W$, allora $\mathcal{L}(X) \subseteq W$

---

### 2.3.6 Dimostrazione della Proposizione

#### (i) $X \neq \emptyset \Rightarrow \mathcal{L}(\emptyset) = \emptyset$, $X \neq \emptyset$

$\forall \space  \mu \in X$, $\mu = 1 \cdot \mu \in \mathcal{L}(X) \Rightarrow X \subseteq \mathcal{L}(X)$

#### (ii) $\mathcal{L}(X) \neq \emptyset \Rightarrow \mathcal{L}(X) \neq \emptyset$

Siano $\mu, \mu' \in \mathcal{L}(X)$. Allora esistono $t, t' \in \mathbb{N}$, $\exists \space  \mu_1, \dots, \mu_t \in X$, $\exists \space  \alpha_1, \dots, \alpha_t \in K$, $\exists \space  \mu'_1, \dots, \mu'_{t'} \in X$, $\exists \space  \alpha'_1, \dots, \alpha'_{t'} \in K$ tali che:

$$\mu = \alpha_1 \mu_1 + \dots + \alpha_t \mu_t, \quad \mu' = \alpha'_1 \mu'_1 + \dots + \alpha'_{t'} \mu'_{t'}$$

Siano $\lambda, \lambda' \in K$. Allora:
$$\lambda \mu + \lambda' \mu' = \lambda (\alpha_1 \mu_1 + \dots + \alpha_t \mu_t) + \lambda' (\alpha'_1 \mu'_1 + \dots + \alpha'_{t'} \mu'_{t'})$$
$$= (\lambda \alpha_1) \mu_1 + \dots + (\lambda \alpha_t) \mu_t + (\lambda' \alpha'_1) \mu'_1 + \dots + (\lambda' \alpha'_{t'}) \mu'_{t'}$$

Poiché $\lambda \alpha_i \in K$, $\lambda' \alpha'_j \in K$, e $\mu_i, \mu'_j \in X$, allora:
$$\lambda \mu + \lambda' \mu' \in \mathcal{L}(X)$$

Inoltre, $0 = 0 \cdot \mu_1 + \dots + 0 \cdot \mu_t \in \mathcal{L}(X)$, quindi $\mathcal{L}(X)$ è un sottospazio vettoriale.

#### (iii) Ipotesi: $W \subseteq V$ sottospazio vettoriale di $V$, $X \subseteq W$

Vogliamo dimostrare: $\mathcal{L}(X) \subseteq W$

Sia $\mu \in \mathcal{L}(X)$. Allora esistono $t \in \mathbb{N}$, $\mu_1, \dots, \mu_t \in X$, $\alpha_1, \dots, \alpha_t \in K$ tali che:
$$\mu = \alpha_1 \mu_1 + \dots + \alpha_t \mu_t$$

Poiché $X \subseteq W$, allora $\mu_i \in W$ per ogni $i$. Poiché $W$ è un sottospazio vettoriale, allora $\alpha_i \mu_i \in W$ per ogni $i$, e quindi $\mu \in W$.

Quindi $\mathcal{L}(X) \subseteq W$.

---

### 2.3.7 Dipendenza e Indipendenza Lineare

Sia $V, K$ uno spazio vettoriale su un campo $K$, e sia $X \subseteq V$ un sottoinsieme di $V$.

**Definizione**: $X$ si dice **LINEARMENTE DIPENDENTE** se: 
Esistono $\mu_1, \dots, \mu_t \in X$ e $\alpha_1, \dots, \alpha_t \in K$, **NON TUTTI nulli**, t.c.: 
$$\Omega = \alpha_1 \mu_1 + \dots + \alpha_t \mu_t = 0$$

---

**Definizione**: $X$ si dice **LINEARMENTE INDIPENDENTE** se: 
NON è linearmente dipendente, ossia: 
$$\forall \space  \mu_1, \dots, \mu_t \in X, \quad \forall \space  \alpha_1, \dots, \alpha_t \in K, \quad \alpha_1 \mu_1 + \dots + \alpha_t \mu_t = 0 \quad \Rightarrow \quad \alpha_1 = \dots = \alpha_t = 0$$

---

**OSSERVAZIONE**: 
Sia $Y \subseteq X \subseteq V$. 
Allora: 
$$X \text{ linearmente indipendente } \Rightarrow Y \text{ linearmente indipendente}$$

---

### 2.3.8 Proposizione sulla Dipendenza Lineare

Siano $V, K$ uno spazio vettoriale su un campo $K$, e $X \subseteq V$. 
Allora: 
$$X \text{ linearmente dipendente } \iff \exists \space  \mu \in X \text{ t.c. } \mathcal{L}(X) = \mathcal{L}(X \setminus \{\mu\})$$

---

#### Dimostrazione:

*Nota B*: Per convenzione, $\emptyset$ è linearmente indipendente. 
E si assume $X \neq \emptyset$.

---

**"⇒"**: 
Sia $X$ linearmente dipendente. 
Allora: 
$$\exists \space  \mu_1, \dots, \mu_t \in X, \quad \exists \space  \alpha_1, \dots, \alpha_t \in K \text{ NON TUTTI nulli}, \text{ con } \alpha_t \neq 0$$ 
t.c.: 
$$\Omega = \alpha_1 \mu_1 + \dots + \alpha_t \mu_t = 0$$ 
Allora: 
$$\alpha_t \mu_t = -(\alpha_1 \mu_1 + \dots + \alpha_{t-1} \mu_{t-1}) \in \mathcal{L}(\mu_1, \dots, \mu_{t-1})$$ 
Quindi: 
$$\mu_t \in \mathcal{L}(\mu_1, \dots, \mu_{t-1}) \subseteq \mathcal{L}(X \setminus \{\mu_t\})$$ 
Quindi: 
$$\mathcal{L}(X) = \mathcal{L}(X \setminus \{\mu_t\})$$

---

**"⇐"**: 
Sia $\mathcal{L}(X) = \mathcal{L}(X \setminus \{\mu\})$ per qualche $\mu \in X$. 
Allora: 
$$\mu \in \mathcal{L}(X \setminus \{\mu\}) \Rightarrow \exists \space  \alpha_1, \dots, \alpha_{t-1} \in K \text{ t.c. } \mu = \alpha_1 \mu_1 + \dots + \alpha_{t-1} \mu_{t-1}$$ 
Quindi: 
$$0 = \mu - \mu = \alpha_1 \mu_1 + \dots + \alpha_{t-1} \mu_{t-1} - \mu$$ 
Ma $\mu \in X$, quindi: 
$$0 = \alpha_1 \mu_1 + \dots + \alpha_{t-1} \mu_{t-1} - \mu \Rightarrow \text{esiste una combinazione lineare non nulla che dà 0}$$ 
Quindi $X$ è linearmente dipendente.

---

## 2.4 Teoria delle Basi e della Dimensione

### 2.4.1 Definizione di Base

$\Rightarrow \exists \space $ una base $B$ di $V$ contenuta in $S$.

**Definizione**
Una **BASE** $B$ di $V$ è un sistema di generatori di $V$ linearmente indipendente.

---

### 2.4.2 Teorema di Estrazione di una Base

Sia $V$ uno spazio vettoriale su $K$. 
Sia $S$ un sistema di generatori di $V$, con $|S| = m \in \mathbb{N} \cup \{0\}$. 
Allora esiste una base $B$ di $V$ contenuta in $S$.

---

#### Dimostrazione:

(i) Se $S = \emptyset$, allora $B = S$, $V = \mathcal{L}(\emptyset) = \{\mathbf{0}\}$.

(ii) Se $S \neq \emptyset$, allora vediamo se $S$ è linearmente indipendente oppure no.

- a) Se $S$ è linearmente indipendente, allora $B = S$.
- b) Se $S$ è linearmente dipendente, allora: $\exists \space  u \in S : \mathcal{L}(S) = \mathcal{L}(S - \{u\})$.

*Allora: pongo $S' = S - \{u\}$*

$\Rightarrow$ Se $S'$ è linearmente indipendente, allora $B = S'$.

*Altrimenti: $\exists \space  v \in S' : \mathcal{L}(S') = \mathcal{L}(S' - \{v\})$ e continuo in questo modo finché non trovo un sistema di generatori di $V$ linearmente indipendente. $\blacksquare$*

---

### 2.4.3 Proposizione sulla Dipendenza Lineare e Generatori

Sia $V, K$ uno spazio vettoriale su un campo $K$. 
Sia $X = \{u_1, \dots, u_m\} \subseteq V$. 
Sia $S$ linearmente indipendente.

+ Se: 
(i) $u \in V - \mathcal{L}(S) \Rightarrow S \cup \{u\}$ linearmente indipendente 
(ii) $S \cup \{u\}$ linearmente dipendente $\Rightarrow u \in \mathcal{L}(S)$

---

#### Dimostrazione:

- P.A.: $S \cup \{u\}$ è linearmente dipendente, allora: 
$\exists \space  \alpha_1, \dots, \alpha_m, \alpha \in K$, NON tutti nulli t.c.: 
$$\alpha_1 u_1 + \dots + \alpha_m u_m + \alpha u = \mathbf{0}$$
Sia $\alpha \neq 0$:

$$\exists \space  \alpha^{-1} \in K \text{ e } \alpha ( \alpha_1 \mu_1 + \dots + \alpha_m \mu_m + \alpha \mu ) = \alpha \cdot \Omega = \Omega$$

$$\Rightarrow \alpha^{-1} \alpha_1 \mu_1 + \dots + \alpha^{-1} \alpha_m \mu_m + \alpha^{-1} \alpha \mu = \Omega$$

$$\Rightarrow \mu = - (\alpha^{-1} \alpha_1) \mu_1 - \dots - (\alpha^{-1} \alpha_m) \mu_m \in \mathcal{L}(X)$$

---

$\alpha = 0$:

$$\Rightarrow \alpha_1 \mu_1 + \dots + \alpha_m \mu_m + 0 \cdot \mu = \Omega$$

$$\Rightarrow \alpha_1 \mu_1 + \dots + \alpha_m \mu_m = \Omega$$

Comunque, **non tutti i coefficienti sono nulli** (altrimenti sarebbe impossibile, perché $X$ è linearmente indipendente).

P.I. $\blacksquare$

---

### 2.4.4 Lemma di Steinitz

**+ LEMMA (o TEOREMA) di STEINITZ:**

- Sia $V$ uno spazio vettoriale f.g. su un campo $K$.
- Sia $S = \{ \mu_1, \dots, \mu_m \}$ un sistema di generatori finito di $V$ ($\mathcal{L}(S) = V$).
- Sia $X = \{ v_1, \dots, v_n \}$ un insieme di vettori di $V$.

- Se:
 $$\begin{cases}
 n > m \\
 |X| > |S|
 \end{cases}
 \Rightarrow X \text{ linearmente dipendente.}$$

---

**+ COROLLARIO:**

Sono date le stesse ipotesi del Lemma di Steinitz:

- Se: $X$ linearmente indipendente $\Rightarrow |X| \leq |S|$

---

### 2.4.5 Definizione di Dimensione

**Def.:** Si dice **DIMENSIONE** di $V$ (dim $V$ opp. dim($V$)) la cardinalità comune delle basi di $V$.

---

### 2.4.6 Teorema di Equipotenza delle Basi

- Sia $V$ e.f.g., $\exists \space $ un sistema di generatori finito $(S)$ di $V$.
- Sia $\mathcal{B}$ una base di $V$ estratta da $S$.

$$\Rightarrow |\mathcal{B}| = m < +\infty$$
Sia $B'$ un'altra base di $V$.

I) $|B'| = m < +\infty$ è vero. Altrimenti:

$$\exists \space  X \in B' : |X| = m+1 > |B'| \leftarrow \text{S. di Gen.} \Rightarrow$$

$$\Rightarrow \text{Impossibile per il corollario di Steinitz}$$

II) $|B'| \leq |B|$

a) $B'$ è linearmente indipendente in $V$ e $B$ è sistema di generatori di $V \Rightarrow |B'| \leq |B|$

b) $B$ è linearmente indipendente in $V$ e $B'$ è sistema di generatori di $V \Rightarrow |B| \leq |B'|$

$$\Rightarrow |B'| = |B| \quad \blacksquare$$

---

*Esempio*:

Sia $V$ uno spazio vettoriale f.g. su un campo $K$, allora le basi di $V$ hanno la stessa cardinalità.

---

> **📌 Nota di Fine Capitolo**: Questo capitolo è **completamente riorganizzato** secondo lo schema richiesto. Tutte le sezioni originali relative a Spazi Vettoriali, Sottospazi, Generatori, Dipendenza Lineare e Teoria delle Basi sono state incluse e organizzate gerarchicamente. **Nessun contenuto è stato modificato, riscritto o eliminato.**
>
> **Attendo la tua conferma esplicita per procedere con il Capitolo 3.**