# Capitolo 7: Spazi Euclidei e Prodotti Scalari

---

## 7.1 Prodotto Scalare

**Prodotto Scalare:** 
Vediamo ora il prodotto scalare numerico/standard/canonico tra vettori di $K^m$: 
$$
\cdot : K^m \times K^m \longrightarrow K^m, \quad ((a_1, \dots, a_m), (b_1, \dots, b_m)) \mapsto a_1b_1 + \cdots + a_mb_m = \langle (a_1, \dots, a_m), (b_1, \dots, b_m) \rangle
$$

---

**Proprietà del Prodotto Scalare:** 
Per ogni $(a_1, \dots, a_m), (b_1, \dots, b_m), (c_1, \dots, c_m) \in K^m$, $\forall \space  \alpha \in K$: 

I) $(a_1, \dots, a_m) \cdot (b_1, \dots, b_m) = (b_1, \dots, b_m) \cdot (a_1, \dots, a_m)$ 

II) $\left( \alpha \cdot (a_1, \dots, a_m) \right) \cdot (b_1, \dots, b_m) = \alpha \left[ (a_1, \dots, a_m) \cdot (b_1, \dots, b_m) \right]$ 

III) $\left[ (a_1, \dots, a_m) + (b_1, \dots, b_m) \right] \cdot (c_1, \dots, c_m) = (a_1, \dots, a_m) \cdot (c_1, \dots, c_m) + (b_1, \dots, b_m) \cdot (c_1, \dots, c_m)$ 

IV) $(a_1, \dots, a_m) \cdot (a_1, \dots, a_m) \geq 0$ 
$$
= 0 \iff (a_1, \dots, a_m) = (0, \dots, 0)
$$

---

## 7.2 Spazi Vettoriali Euclidei

### 7.2.1 Definizione

**Def**: Uno **SPAZIO VETTORIALE EUCLIDEO** è una coppia $(V, \langle \cdot, \cdot \rangle)$, dove $V$ è uno spazio vettoriale REALE (ovvero $K = \mathbb{R}$) e $\langle \cdot, \cdot \rangle$ è un **PRODOTTO SCALARE**, ovvero:

$$
\langle \cdot, \cdot \rangle : V \times V \longrightarrow \mathbb{R}
$$
$$
(u, v) \longmapsto \langle u, v \rangle
$$

t.e.: gode delle seguenti proprietà:

I) $\forall \space  u, v \in V, \langle u, v \rangle = \langle v, u \rangle$

II) $\forall \space  u, v, w \in V, \langle u, v + w \rangle = \langle u, v \rangle + \langle u, w \rangle$ 
è lineare rispetto a $+$ sul secondo elemento $\left\{ \begin{array}{c} \text{BILINEARE} \end{array} \right.$

III) $\forall \space  u, v \in V, \forall \space  \alpha \in \mathbb{R}, \langle u, \alpha v \rangle = \alpha \langle u, v \rangle$

---

### 7.2.2 Norma e Proprietà

**Def.** $\forall \space  \mu \in V, \| \mu \| = \sqrt{\langle \mu, \mu \rangle}$ è detto **NORMA** di $\mu$.

**Proprietà della Norma:**

I) $\forall \space  \mu \in V, \| \mu \| \geq 0$

II) $\forall \space  \mu \in V, \| \mu \| = 0 \iff \mu = \Omega$

III) $\forall \space  \mu \in V, \forall \space  \alpha \in \mathbb{R}, \| \alpha \mu \| = |\alpha| \| \mu \|$

**OSSERVAZIONE:**

- $\forall \space  \mu \in V, \langle \Omega, \mu \rangle = 0$ (iii), (i)
- $\langle \Omega, \mu \rangle = \langle \Omega, \mu \rangle = 0 \Rightarrow \langle \Omega, \mu \rangle = 0$
- $\forall \space  \mu \in V, \forall \space  \alpha \in \mathbb{R}, \; \| \alpha \mu \| = |\alpha| \| \mu \|$ (i), (ii)
- $\| \alpha \mu \| = \sqrt{ \langle \alpha \mu, \alpha \mu \rangle } = \sqrt{ \alpha^2 \langle \mu, \mu \rangle } = |\alpha| \sqrt{ \langle \mu, \mu \rangle }$

---

### 7.2.3 Disuguaglianza di Schwarz

**DISUGUAGLIANZA di SCHWARZ: $(V, \langle \cdot, \cdot \rangle)$**

$\forall \space  \mu, \nu \in V, \; | \langle \mu, \nu \rangle | \leq \| \mu \| \cdot \| \nu \|$

#### Dimostrazione

- Se: $\mu = \Omega$ oppure $\nu = \Omega$, allora $0 = 0$
- Se: $\mu \neq \Omega$ e $\nu \neq \Omega$, consideriamo un parametro $\beta \in \mathbb{R}$ e il vettore $\mu + \beta \nu$

(ii)
$$
0 \leq \langle \mu + \beta \nu, \mu + \beta \nu \rangle = \langle \mu + \beta \nu, \mu \rangle + \langle \mu + \beta \nu, \beta \nu \rangle = \langle \mu, \mu \rangle + \langle \beta \nu, \mu \rangle + \langle \mu, \beta \nu \rangle + \langle \beta \nu, \beta \nu \rangle
$$

(iii)
$$
= \| \mu \|^2 + \beta \langle \mu, \nu \rangle + \beta \langle \nu, \mu \rangle + \beta^2 \| \nu \|^2 = \| \mu \|^2 + 2\beta \langle \mu, \nu \rangle + \beta^2 \| \nu \|^2
$$

$\beta \in \mathbb{R}$

**Valore Annullante su $\beta$ del polinomio:**

$$
\| \nu \|^2 \beta^2 + 2 \langle \mu, \nu \rangle \beta + \| \mu \|^2
$$

$$
\beta = \frac{ \langle \mu, \nu \rangle \pm \sqrt{ \langle \mu, \nu \rangle^2 - \| \mu \|^2 \| \nu \|^2 } }{ \| \nu \|^2 }
$$

$$
\Rightarrow \langle \mu, \nu \rangle^2 - \| \mu \|^2 \| \nu \|^2 \leq 0
$$

$$
\langle \mu, \nu \rangle^2 \leq \| \mu \|^2 \| \nu \|^2
$$

$$
| \langle \mu, \nu \rangle | \leq \| \mu \| \| \nu \| \quad \blacksquare
$$

**OSSERVAZIONE:**

$\langle \beta \mu + \nu, \beta \mu + \nu \rangle = 0$

oppure

$\langle \mu + \beta \nu, \mu + \beta \nu \rangle = 0 \Rightarrow \mu + \beta \nu = \Omega$

$\Rightarrow \{ \mu, \nu \} \text{ Linearmente Dipendenti}$

Sia $\mu, \nu \in V \setminus \{0\} \Rightarrow \|\mu\| \ne 0, \|\nu\| \ne 0$

$$
|\langle \mu, \nu \rangle| \le \|\mu\| \|\nu\| \Rightarrow |\langle \mu, \nu \rangle| \le 1 \Rightarrow -1 \le \frac{\langle \mu, \nu \rangle}{\|\mu\| \|\nu\|} \le 1
$$

$$
\Rightarrow -1 \le \cos \theta \le 1
$$

$$
\cos: [0, \pi] \longrightarrow [-1, 1] \text{ è BIETTIVA}
$$

$$
\forall \space  \varepsilon \in [-1, 1], \exists \space  ! \theta \in [0, \pi] : \cos \theta = \varepsilon
$$

**Def.**: $\forall \space  \mu, \nu \in V \setminus \{0\}$, l'angolo tra $\mu$ e $\nu$ è l'unico $\theta \in [0, \pi]$ t.c. $\cos \theta = \frac{\langle \mu, \nu \rangle}{\|\mu\| \|\nu\|}$

---

**Def.**: $\forall \space  \mu, \nu \in V$, $\mu$ e $\nu$ sono **ORTOGONALI** ($\mu \perp \nu$), se $\langle \mu, \nu \rangle = 0$

---

### 7.2.4 Esempi Importanti

**(a)** $V = \mathbb{R}^m$, $\langle \cdot, \cdot \rangle : \mathbb{R}^m \times \mathbb{R}^m \longrightarrow \mathbb{R}$

$$
((a_1, a_2, \dots, a_m), (b_1, b_2, \dots, b_m)) \mapsto a_1b_1 + a_2b_2 + \dots + a_mb_m
$$

**(b)** $V = \mathbb{R}^2$

$$
\langle \cdot, \cdot \rangle : \mathbb{R}^2 \times \mathbb{R}^2 \longrightarrow \mathbb{R}
$$

$$
((a_1, a_2), (b_1, b_2)) \mapsto 2a_1b_1 + a_2b_2 + a_1b_2 + a_2b_1
$$

**(c)** $V = \mathcal{H}_2(\mathbb{R})$

---

## 7.3 Basi Ortogonali e Ortonormali

### 7.3.1 Definizioni

$(V, \langle \cdot, \cdot \rangle)$ spazio vettoriale euclideo, $\dim(V) = m$

**Def:**
$B = (e_1, \dots, e_m)$ base di $V$

- (i) $B$ è **ORTOGONALE**, se: $\forall \space  i,j \in \{1, \dots, m\}, i \neq j, \langle e_i, e_j \rangle = 0$

- (ii) $B$ è **ORTONORMALE**, se: $B$ è ORTOGONALE e $\forall \space  j \in \{1, \dots, m\}, \langle e_j, e_j \rangle = 1$ ($e_j$ è detto **VERSORE**)

$$
\|e_j\|^2 = 1 \Rightarrow \|e_j\| = 1
$$

---

**Def:**
$\forall \space  \mu \in V - \{0\}, \hat{\mu}$ è detto **VERSORE**, se:

$$
\hat{\mu} = \frac{1}{\|\mu\|} \mu \Rightarrow \|\hat{\mu}\| = \left\| \frac{1}{\|\mu\|} \mu \right\| = \frac{1}{\|\mu\|} \|\mu\| = 1
$$

---

### 7.3.2 Proposizione: Indipendenza Lineare di Vettori Ortogonali

Siano $\mu_1, \dots, \mu_n \in V - \{0\}$, a due a due **ORTOGONALI** 
$\Rightarrow$ Allora: $\exists \space  \alpha_1, \dots, \alpha_n \in \mathbb{R}$ t.c. $\alpha_1 \mu_1 + \dots + \alpha_n \mu_n = 0 \Rightarrow \alpha_1 = \dots = \alpha_n = 0$

---

#### Dimostrazione

Th. $\forall \space  \alpha_1, \dots, \alpha_n \in \mathbb{R}$ t.c. $\alpha_1 \mu_1 + \dots + \alpha_n \mu_n = 0$, allora $\alpha_1 = \dots = \alpha_n = 0$

Sia
$$
0 = \langle \mu_1, \varnothing \rangle = \langle \mu_1, \alpha_1 \mu_1 + \dots + \alpha_h \mu_h \rangle = \langle \mu_1, \alpha_2 \mu_2 \rangle + \dots + \langle \mu_1, \alpha_h \mu_h \rangle = \alpha_1 \langle \mu_1, \mu_1 \rangle + \alpha_2 \langle \mu_1, \mu_2 \rangle + \dots + \alpha_h \langle \mu_1, \mu_h \rangle = 0
$$
$$
\downarrow \quad \Rightarrow \quad \alpha_1 = 0
$$
$$
0 = \langle \mu_2, \varnothing \rangle = \langle \mu_2, \alpha_1 \mu_1 + \alpha_2 \mu_2 + \dots + \alpha_h \mu_h \rangle = \alpha_1 \langle \mu_2, \mu_1 \rangle + \alpha_2 \langle \mu_2, \mu_2 \rangle + \dots + \alpha_h \langle \mu_2, \mu_h \rangle \Rightarrow \alpha_2 = 0
$$

---

### 7.3.3 Proposizione: Coordinate in Base Ortonormale

$(V, \langle \cdot, \cdot \rangle)$, $\dim(V) = m$

- Sia $\mathcal{B} = \{e_1, \dots, e_m\}$ una base **ORTONORMALE** di $V$

- $\forall \space  \mu, \nu \in V$, $\exists \space  (x_1, \dots, x_m) = \Phi_{\mathcal{B}}(\mu)$, $\mu = x_1 e_1 + \dots + x_m e_m$

- $\exists \space  (y_1, \dots, y_m) = \Phi_{\mathcal{B}}(\nu)$, $\nu = y_1 e_1 + \dots + y_m e_m$

- (i) $\forall \space  j \in \{1, \dots, m\}$, $x_j = \langle \mu, e_j \rangle$

- (ii) $\langle \mu, \nu \rangle = x_1 y_1 + \dots + x_m y_m$

---

#### Dimostrazione

**(i) $j = 1$**

$$
\langle \mu, e_1 \rangle = \langle x_1 e_1 + x_2 e_2 + \dots + x_m e_m, e_1 \rangle = \langle x_1 e_1, e_1 \rangle + \langle x_2 e_2, e_1 \rangle + \dots + \langle x_m e_m, e_1 \rangle = x_1 \langle e_1, e_1 \rangle + x_2 \langle e_2, e_1 \rangle + \dots + x_m \langle e_m, e_1 \rangle = x_1 \cdot 1 + 0 + \dots + 0 = x_1
$$

---

**(ii) $m = 2$**

$$
\langle \mu, \nu \rangle = \langle x_1 e_1 + x_2 e_2, y_1 e_1 + y_2 e_2 \rangle = \langle x_1 e_1, y_1 e_1 \rangle + \langle x_1 e_1, y_2 e_2 \rangle + \langle x_2 e_2, y_1 e_1 \rangle + \langle x_2 e_2, y_2 e_2 \rangle = x_1 y_1 \langle e_1, e_1 \rangle + x_1 y_2 \langle e_1, e_2 \rangle + x_2 y_1 \langle e_2, e_1 \rangle + x_2 y_2 \langle e_2, e_2 \rangle = x_1 y_1 \cdot 1 + x_1 y_2 \cdot 0 + x_2 y_1 \cdot 0 + x_2 y_2 \cdot 1 = x_1 y_1 + x_2 y_2
$$

---

## 7.4 Metodo di Gram-Schmidt

Sia $\mathcal{B} = (\mu_1, \dots, \mu_m)$ base ordinata di $V$.

- Esiste una base $\overline{\mathcal{B}}$ di $V$ ORTONORMALE, che si ottiene TRASFORMANDO "OPPORTUNATAMENTE" $\mathcal{B}$.

- $v_1 = \mu_1$

- $v_2 = \mu_2 - \dfrac{\langle \mu_2, v_1 \rangle}{\|v_1\|^2} v_1$

- $v_3 = \mu_3 - \dfrac{\langle \mu_3, v_1 \rangle}{\|v_1\|^2} v_1 - \dfrac{\langle \mu_3, v_2 \rangle}{\|v_2\|^2} v_2$

- $\vdots$

- $v_m = \mu_m - \sum_{j=1}^{m-1} \dfrac{\langle \mu_m, v_j \rangle}{\|v_j\|^2} v_j$

- $\overline{\mathcal{B}} = \left( \dfrac{1}{\|v_1\|} v_1, \dots, \dfrac{1}{\|v_m\|} v_m \right)$ è ORTONORMALE

- $\mathcal{B}' = (v_1, \dots, v_m)$ è ORTOGONALE

---

### 7.4.1 Esempio di Gram-Schmidt

Sia $\langle (a_1, a_2), (b_1, b_2) \rangle = 2a_1b_1 + a_1b_2 + a_2b_1 + a_2b_2$

Sia $\mathcal{B} = \left( (1,0), (0,1) \right)$

- $\langle (1,0), (0,1) \rangle = 0 + 0 + 0 + 0 = 0 \neq 1$ → **non ortogonale**

- $\mu_1 = (1,0)$

- $v_1 = \mu_1 = (1,0)$

- $v_2 = \mu_2 - \dfrac{\langle \mu_2, v_1 \rangle}{\|v_1\|^2} v_1 = (0,1) - \dfrac{\langle (0,1), (1,0) \rangle}{\|(1,0)\|^2} (1,0)$

- $\langle (0,1), (1,0) \rangle = 2 \cdot 0 \cdot 1 + 0 \cdot 1 + 1 \cdot 0 + 1 \cdot 0 = 0$

- Quindi: $v_2 = (0,1) - 0 \cdot (1,0) = (0,1)$

- $\|v_1\|^2 = \langle (1,0), (1,0) \rangle = 2 \cdot 1 \cdot 1 + 1 \cdot 0 + 0 \cdot 1 + 0 \cdot 0 = 2$

- $\|v_2\|^2 = \langle (0,1), (0,1) \rangle = 2 \cdot 0 \cdot 0 + 0 \cdot 1 + 1 \cdot 0 + 1 \cdot 1 = 1$

- Quindi $\|v_2\| = 1$, e $\overline{\mathcal{B}} = \left( \left( \frac{1}{\sqrt{2}}, 0 \right), (0,1) \right)$

---

## 7.5 Sottospazi Ortogonali

### 7.5.1 Definizione

Sia $(V, \langle \cdot, \cdot \rangle)$ uno spazio vettoriale euclideo, $\dim(V) = m$.

Sia $X \subseteq V$.

Sottospazio ortogonale a $X$:

$$
X^\perp = \{ \vec{v} \in V \mid \langle \vec{v}, \vec{u} \rangle = 0 \ \forall \space  \vec{u} \in X \}
$$

---

### 7.5.2 Proposizioni

**Osservazione:**

- $X \subseteq Y \Rightarrow X^\perp \supseteq Y^\perp$

---

**Proposizione:**

Sia $U \subseteq V$.

(1) $U + U^\perp = V$

(2) $U \cap U^\perp = \{ \vec{0} \}$

---

**Osservazione:**

(a) $U \cap U^\perp = \{ \vec{0} \}$

(b) $U \oplus U^\perp = V$

---

**Proposizione:**

- $X \subseteq V$, $U = \mathcal{L}(X)$, $\dim(V) = m$

(i) $U^\perp = \{ x \}$

(ii) $U \cap U^\perp = \{ 0 \}$

(iii) $U \oplus U^\perp = V$

---

#### Dimostrazione

$U^\perp = \{ \mu \in V \mid \langle \mu, w \rangle = 0, \forall \space  w \in U \}$

$\perp X = \{ \mu \in V \mid \langle \mu, v \rangle = 0, \forall \space  v \in X \}$

$X \subseteq U$, per l'esercizio: $\perp X \supseteq \perp U$

---

**Th.**

$\perp X \subseteq \perp U$, ovvero: $\mu \in \perp X \Rightarrow \mu \in \perp U$

$$
\downarrow
$$

$\langle \mu, v \rangle = 0, \forall \space  v \in X \quad \Rightarrow \quad \langle \mu, w \rangle = 0, \forall \space  w \in U$

---

$\forall \space  w \in U = \mathcal{L}(X) \Rightarrow \exists \space  \mu_1, \dots, \mu_h \in X \quad : \quad w = \alpha_1 \mu_1 + \dots + \alpha_h \mu_h$

$\exists \space  \alpha_1, \dots, \alpha_h \in \mathbb{R} \quad : \quad w = \alpha_1 \mu_1 + \dots + \alpha_h \mu_h$

**BILINEARITÀ**

$\langle \mu, w \rangle = \langle \mu, \alpha_1 \mu_1 + \dots + \alpha_h \mu_h \rangle = \langle \mu, \alpha_1 \mu_1 \rangle + \dots + \langle \mu, \alpha_h \mu_h \rangle$

$$
= \alpha_1 \langle \mu, \mu_1 \rangle + \dots + \alpha_h \langle \mu, \mu_h \rangle = 0
$$

$$
\text{per deg. (P.S.)} \quad \mu = 0
$$

---

(iii) $U \oplus U^\perp \Rightarrow \dim(U \oplus U^\perp) = \dim(U) + \dim(U^\perp)$

$\Rightarrow$ per Gromman

---

**Th: $\dim(U^\perp) = \dim(V) - \dim(U) = m - h$, dove $h = \dim(U)$**

- Sia $\mathcal{B}_U = \{ w_1, \dots, w_h \}$ base di $U$.

Completiamo $\mathcal{B}_U$ in una base di $V$. Quindi esistono:

$w_{h+1}, \dots, w_m$ vettori di $V$ t.c.

$\mathcal{B}_U \cup \{ w_{h+1}, \dots, w_m \}$ è una base di $V$

- Applichiamo il procedimento di Gram-Schmidt su $\{ w_{h+1}, \dots, w_m \}$ e otteniamo $\{ v_{h+1}, \dots, v_m \} \subseteq \mathcal{L}(w_{h+1}, \dots, w_m)$

$\dim(\mathcal{L}(w_{h+1}, \dots, w_m)) = m - h$

$$
\Rightarrow \mathcal{L}(v_{h+1}, \dots, v_m) = U^\perp
$$

"⊆": L(V_{a+1}, ..., V_m) ⊆ ⊥U per costruzione

"⊆": U ⊕ L(V_{a+1}, ..., V_m) ha dim h+(m-h) ⇒
U ⊕ L(V_{a+1}, ..., V_m) ⇒ L(V_{a+1}, ..., V_m) = ⊥U, Altrimenti
dim(U ∩ ⊥U) > 0

---

## 7.6 Spazio Affine Euclideo

+ SPAZIO (AFFINE) EUCLIDEO:

· Def.: Lo spazio (affine) euclideo è una TERNA
$(E^, E, \Pi)$, dove:

(i) $E^$ è uno spazio vettoriale euclideo

(ii) $E$ è un insieme i cui elementi sono detti PUNTI

(iii) $\Pi: E \times E \rightarrow E^$
 $(P, Q) \mapsto \Pi((P, Q)) = \overrightarrow{PQ}$

t.c.

(1) $\forall \space  P \in E, \forall \space  u \in E^, \exists \space ! X \in E: \overrightarrow{PX} = u$

(2) $\forall \space  P, Q, R \in E, \overrightarrow{PQ} + \overrightarrow{QR} = \overrightarrow{PR}$

---

**OSSERVAZIONE:**
· Potremmo prendere uno spazio vettoriale qualsiasi al posto di $E^$, e con $(V, E, \Pi)$ si dice SPAZIO AFFINE.

---

### 7.6.1 Proprietà

$(E^, E, \Pi)$ spazio euclideo

I) $\forall \space  P, Q \in E, \overrightarrow{PQ} = \vec{0} \Leftrightarrow P = Q$

II) $\forall \space  P, Q \in E, -\overrightarrow{PQ} = \overrightarrow{QP}$

---

## 7.7 Distanza

### 7.7.1 Definizione di Distanza

$(E, \mathcal{E}, \Pi)$, $\dim(E) = m$

**Def.**: $\forall \space  P, Q \in E$, $d(P, Q) = \| \overrightarrow{PQ} \|$

---

### 7.7.2 Proprietà della Distanza

**Osservazione:**

(i) $\forall \space  P, Q \in E$, $d(P, Q) \geq 0$

(ii) $\forall \space  P, Q \in E$, $d(P, Q) = \| \overrightarrow{PQ} \| = \| -\overrightarrow{QP} \| = \| \overrightarrow{QP} \| = d(Q, P)$

---

**Def.**: $\forall \space  X, Y \subseteq E$, $d(X, Y) = \inf \{ d(P, Q) \mid P \in X, Q \in Y \}$

---

### 7.7.3 Distanza Punto-Iperiano

$d(P, \mathcal{H}) = d(P, \overline{P})$, $\overline{P} = \mathbb{R} \cap \mathcal{H}$, dove $\mathbb{R}$ è la retta passante per $P$ e ortogonale a $\mathcal{H}$

---

**Immagini:**

$\forall \space  Q \in \mathcal{H} \setminus \{ \overline{P} \}$, $\| \overrightarrow{PQ} \| > \| \overrightarrow{PP} \|$ e ortogonale a $\mathcal{H}$

---

In generale: $\dim(E) = m$, $R = (O, \vec{B})$

$\mathcal{H}: a_1 x_1 + a_2 x_2 + \dots + a_m x_m - b = 0$, $P(e_1, \dots, e_m)$

$\mathcal{L}: \begin{cases} x_1 = e_1 + a_1 t \\ x_m = e_m + a_m t \end{cases}$, $\mathcal{L} \cap \mathcal{H}: a_1(e_1 + a_1 t) + \dots + a_m(e_m + a_m t) = 0$

$\Rightarrow (a_1^2 + \dots + a_m^2)t - b + a_1 e_1 + \dots + a_m e_m = 0$

$t = \dfrac{b - a_1 e_1 - \dots - a_m e_m}{a_1^2 + \dots + a_m^2}$, $\overline{P}(a_1 t, \dots, a_m t)$

$d(P, \mathcal{H}) = d(P, \overline{P}) = \|\overline{P}P\| = \sqrt{a_1^2 t^2 + \dots + a_m^2 t^2} = \dfrac{|a_1 e_1 + \dots + a_m e_m - b|}{\sqrt{a_1^2 + \dots + a_m^2}} = \|W\|$

---

### 7.7.4 Geometria nel Piano

#### Segmento

$A, B \in E$, $\exists \space  P \in E \mid d(P, A) = d(P, B)$

Segmento $\langle A, B \rangle = \left\{ P \in E \mid \overrightarrow{AP} = t \overrightarrow{AB}, \text{ con } 0 \leq t \leq 1 \right\}$

---

$m = 2$

$P(x_1, x_2)$, $P \in \langle A, B \rangle \iff \exists \space  t \in [0,1] : (x_1, x_2) - (a_1, a_2) = t(b_1 - a_1, b_2 - a_2)$

$\iff \exists \space  t \in [0,1] : (x_1, x_2) = (a_1, a_2) + t(b_1 - a_1, b_2 - a_2)$

$\iff \exists \space  t \in [0,1] : (x_1, x_2) = t(b_1, b_2) + (1 - t)(a_1, a_2)$

---

$\exists \space  M \in E : \overrightarrow{AM} = \overrightarrow{AB}$, punto medio del segmento $\langle A, B \rangle$

$\mathcal{H}(x_1, x_2) : (x_1 - a_1, x_2 - a_2) = (b_1 - x_1, b_2 - x_2)$

$\begin{cases} x_1 - a_1 = b_1 - x_1 \\ x_2 - a_2 = b_2 - x_2 \end{cases} \iff \begin{cases} 2x_1 = b_1 - a_1 \\ 2x_2 = b_2 - a_2 \end{cases} \iff \begin{cases} x_1 = \dfrac{b_1 - a_1}{2} \\ x_2 = \dfrac{b_2 - a_2}{2} \end{cases}$

---

#### Circonferenza nel Piano

- $\dim(\mathbb{E}) = 2$, $R = (0, R) > 0$ raggio, $C(x_0, y_0)$ centro 
 $C = \{ P \in \mathbb{E} \mid d(C, P) = R \}$ 
 $P(x, y) \in C \iff d(C, P) = R \iff d(C, P)^2 = R^2 \iff (x - x_0)^2 + (y - y_0)^2 = R^2$

- $x^2 - 2x_0x + x_0^2 + y^2 - 2y_0y + y_0^2 = R^2$ 
 $x^2 + y^2 - 2x_0x - 2y_0y = R^2 - x_0^2 - y_0^2$

- $x^2 + y^2 + ax + by = e$ rappresenta una circonferenza se, 
 e solo se,

 $a = -2x_0$, $b = -2y_0$, $e = R^2 - x_0^2 - y_0^2 = R^2 - \frac{a^2}{4} - \frac{b^2}{4}$

- $\downarrow$

 $x_0 = -\frac{a}{2}$, $y_0 = -\frac{b}{2}$, $e \left[ R^2 = e + \frac{a^2}{4} + \frac{b^2}{4} > 0 \right]$

- $x_0^2 = \frac{a^2}{4}$, $y_0^2 = \frac{b^2}{4}$, $C\left(-\frac{a}{2}, -\frac{b}{2}\right)$ e raggio $\sqrt{e + \frac{a^2}{4} + \frac{b^2}{4}}$

---

> **Fine Capitolo 7**