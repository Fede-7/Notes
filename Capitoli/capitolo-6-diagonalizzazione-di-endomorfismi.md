# Capitolo 6: Diagonalizzazione di Endomorfismi

---

## 6.1 Endomorfismi e Autovalori

### 6.1.1 Definizione di Endomorfismo

Sia $T: V \longrightarrow V$ un endomorfismo.

---

### 6.1.2 Autovalori, Autospazi e Autovettori

**Def.** Uno scalare $\lambda \in K$ si dice **autovalore** di $T$ se e solo se:
$$
U_\lambda = \left\{ \mu \in V \mid T(\mu) = \lambda \mu \right\} \neq \{0\}
$$

**Osservazione:**
$$
\lambda = 0 \text{ è autovalore di } T \iff U_0 = \left\{ \mu \in V \mid T(\mu) = 0 \cdot \mu \right\} = \ker T \neq \{0\} \iff T \text{ NON è iniettiva}
$$

---

**Proposizione:**
Sia $\lambda \in K$, allora $U_\lambda$ è un **sottospazio vettoriale** di $V$.

---

#### Dimostrazione

Siano $\mu, \mu' \in U_\lambda$, $\alpha \in K$.

- $T(\mu) = \lambda \mu$, $T(\mu') = \lambda \mu'$
- $T(\mu + \mu') = T(\mu) + T(\mu') = \lambda \mu + \lambda \mu' = \lambda (\mu + \mu') \Rightarrow \mu + \mu' \in U_\lambda$

- $T(\alpha \mu) = \alpha T(\mu) = \alpha (\lambda \mu) = (\alpha \lambda) \mu = (\lambda \alpha) \mu = \lambda (\alpha \mu) \Rightarrow \alpha \mu \in U_\lambda$

---

**Def.** Se $\lambda$ è autovalore di $T$, allora $U_\lambda$ si dice **autospazio** e i suoi vettori non nulli sono detti **autovettori**.

---

### 6.1.3 Calcolo di Autovalori e Autospazi

Sia $T: V \longrightarrow V$ un endomorfismo, $\dim(V) = m$.

Sia $B = \{e_1, \dots, e_m\}$ una base di $V$.

Sia $A = M_B(T)$ la matrice di $T$ rispetto a $B$.

Allora:
$$
A \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} = \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix}\quad \text{e} \quad \Phi_B(\mu) = (x_1, \dots, x_m)\quad \text{e} \quad \Phi_B(T(\mu)) = (y_1, \dots, y_m)
$$

---

#### N.B.: Equivalentemente

$\lambda \in K$ si dice **AUTOVALORE** di $T$, se esiste $\mu \in V \setminus \{0\}$: $T\mu = \lambda \mu$

$$\Rightarrow \exists \space  (x_1, \dots, x_m) \in K^m \setminus \{0\} : A \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} = \lambda \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix}$$

$$\Rightarrow \Phi_B(\lambda \mu) = \lambda \Phi_B(\mu) = \lambda (x_1, \dots, x_m)$$

$$\Rightarrow A \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} - \lambda I_m \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} = 0 \quad \Rightarrow \Sigma_0: (A - \lambda I_m) \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} = 0$$

$$\Rightarrow |A - \lambda I_m| = 0 \quad \text{“Equazione caratteristica”} \quad \text{(grado } m\text{)}$$

“Polinomio caratteristico”

$\forall \space  \lambda$ autovalore di $T$, $\Sigma_0: (A - \lambda I_m)x = 0$ ha come insieme delle soluzioni:

$$
\ker T = \Phi_B^{-1}(U_\lambda) \quad \text{“autospazio di } A\text{”}$$

“autovettori di $A$”

$\lambda$ è autovalore di $A$

---

### 6.1.4 Esempio

1) 
$$
\begin{pmatrix} 0 & 0 \\ 0 & 2 \end{pmatrix} - \lambda \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -\lambda & 0 \\ 0 & 2 - \lambda \end{pmatrix}
$$

$$
\begin{vmatrix} -\lambda & 0 \\ 0 & 2 - \lambda \end{vmatrix} = (-\lambda)(2 - \lambda) = 2\lambda + \lambda^2 = 0 \quad \Rightarrow \lambda = 0 \vee \lambda = 2
$$

- $\lambda_0$: 
$$
U_0: \begin{pmatrix} 0 & 0 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 0 \quad \Rightarrow \begin{cases} 2x_2 = 0 \end{cases}\n\Rightarrow x_2 = 0
$$

$$
\Rightarrow S_0 = \mathcal{L}((1, 0)) = \Phi_B^{-1}(U_0) \Rightarrow U_0 = \mathcal{L}((1, -1)) \quad \text{ker}T
$$

- $\lambda_2$:
$$
U_2: \begin{pmatrix} -2 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 0 \quad \Rightarrow \begin{cases} x_1 = 0 \end{cases}
$$

$$
\Rightarrow S_2 = \mathcal{L}((0, 1)) = \Phi_B^{-1}(U_2) \Rightarrow U_2 = \mathcal{L}((1, 1))$$

$$
\dim(U_2) = m - \text{rango}(A - 2I)$$

---

### 6.1.5 Proposizione: Autovalori e Matrici Simili

Siano $A, \bar{A} \in \mathcal{M}_m(K)$, con $A$ invertibile. Allora: 
$$
A = P^{-1} \bar{A} P
$$ 
per qualche matrice invertibile $P \in \mathcal{M}_m(K)$.

Allora: 
$$
|A - \lambda I_m| = |\bar{A} - \lambda I_m|
$$

---

#### Dimostrazione

$$
|A - \lambda I_m| = |P^{-1} \bar{A} P - \lambda P^{-1} I_m P| = |P^{-1} \bar{A} P - P^{-1} (\lambda I_m) P| = |P^{-1} (\bar{A} - \lambda I_m) P| = |P^{-1}| \cdot |\bar{A} - \lambda I_m| \cdot |P|
$$

Poiché $|P^{-1}| = \frac{1}{|P|}$, si ha:

$$
|A - \lambda I_m| = \frac{1}{|P|} \cdot |\bar{A} - \lambda I_m| \cdot |P| = |\bar{A} - \lambda I_m|$$

---

### 6.1.6 Proposizione: Indipendenza Lineare di Autovettori

Siano $\lambda_1, \dots, \lambda_h$ autovalori di $T$, a due a due distinti. 
Per ogni autovalore $\lambda_i$, consideriamo $\mu_i \in U_{\lambda_i} \setminus \{0\}$.

Allora: $\{\mu_1, \dots, \mu_h\}$ è linearmente indipendente.

---

#### Dimostrazione

$$
U_{\lambda_i} \cap U_{\lambda_j} = \{0\}, \quad \text{per } i \ne j
$$

Infatti: se $\mu \in U_{\lambda_i} \cap U_{\lambda_j}$, allora $T(\mu) = \lambda_i \mu = \lambda_j \mu$, 
quindi $\lambda_i \mu = \lambda_j \mu \Rightarrow (\lambda_i - \lambda_j) \mu = 0$. 
Poiché $\lambda_i \ne \lambda_j$, allora $\mu = 0$.

Per induzione su $h$:

- **Base ($h = 1$)**: $\{\mu_1\}$ è linearmente indipendente se $\mu_1 \ne 0$, che è vero per costruzione.

- **Passo induttivo ($h > 1$)**: 
 Siano $\alpha_1, \dots, \alpha_h \in K$ tali che: 
 $$\alpha_1 \mu_1 + \dots + \alpha_{h-1} \mu_{h-1} + \alpha_h \mu_h = 0
 $$
 Dobbiamo dimostrare che $\alpha_1 = \dots = \alpha_h = 0$.

 Applichiamo $T$: 
 $$
 \lambda_1 \alpha_1 \mu_1 + \dots + \lambda_{h-1} \alpha_{h-1} \mu_{h-1} + \lambda_h \alpha_h \mu_h = 0
 $$

 Sottraiamo la prima equazione moltiplicata per $\lambda_h$: 
 $$
 \lambda_h \alpha_1 \mu_1 + \dots + \lambda_h \alpha_{h-1} \mu_{h-1} + \lambda_h^2 \alpha_h \mu_h - \lambda_h (\alpha_1 \mu_1 + \dots + \alpha_h \mu_h) = 0
 $$

 In realtà, la sottrazione porta a: 
 $$
 \alpha_1 (\lambda_1 - \lambda_h) \mu_1 + \dots + \alpha_{h-1} (\lambda_{h-1} - \lambda_h) \mu_{h-1} = 0
 $$

 Per ipotesi induttiva, $\{\mu_1, \dots, \mu_{h-1}\}$ è linearmente indipendente, quindi: 
 $$
 \alpha_1 (\lambda_1 - \lambda_h) = 0, \quad \dots, \quad \alpha_{h-1} (\lambda_{h-1} - \lambda_h) = 0
 $$

 Poiché $\lambda_i \ne \lambda_h$ per $i < h$, allora $\alpha_1 = \dots = \alpha_{h-1} = 0$.

 Sostituendo nella prima equazione: $\alpha_h \mu_h = 0$, e poiché $\mu_h \ne 0$, allora $\alpha_h = 0$.

 Quindi, per induzione, $\{\mu_1, \dots, \mu_h\}$ è linearmente indipendente.

---

## 6.2 Molteplicità Algebrica e Geometrica

### 6.2.1 Definizioni

**Def.** autovettore di $T$ 
$$
m_g(\lambda) \stackrel{\text{def.}}{=} \dim(U_\lambda) \quad \text{"Multiplicità Geometrica"}$$

Sia 
$$
T: V \longrightarrow V \quad \text{Endomorfismo, } K
$$

- **Def.**: $\lambda \in K$ si dice **AUTOVALORE** di $T$, se: 
 $$
 U_\lambda = \left\{ u \in V \mid T(u) = \lambda u \right\} \neq \{0\}, \quad \text{ovvero:} \exists \space  u \in V \setminus \{0\} : T(u) = \lambda u
 $$ 
 Se $\dim(V) = m$, allora $A = M_\mathcal{B}(T)$, e: 
 $$
 \lambda \in K \text{ è AUTOVALORE } \iff \det(A - \lambda I) = 0
 $$

- $\Phi_\mathcal{B}(U_\lambda) = \ker(A - \lambda I)$ 
 $\Rightarrow (A - \lambda I)x = 0$ 
 $\Rightarrow p(\lambda) \in K[\lambda]$

- **Def.**: $a \in K$, $a$ si dice **radice/soluzione** di $p(\lambda)$ 
 $\iff p(a) = 0$

+ **TEOREMA di RUFFINI**: 
 $a \in K$, $a$ è radice di $p(\lambda) \iff \exists \space  q(\lambda) \in K[\lambda]$ tale che: 
 $$
 p(\lambda) = q(\lambda)(\lambda - a), \quad \text{cioè } q(\lambda) \text{ divide } p(\lambda)
 $$

- **Def.**: Sia $a$ una radice di $p(\lambda)$. 
 La **MOLTEPLICITA' ALGEBRICA** di $a$ come radice di $p(\lambda)$ è: 
 $$
 m_a(a) \overset{\text{def}}{=} \max \left\{ k \in \mathbb{N} \mid (\lambda - a)^k \text{ divide } p(\lambda) \right\}
 $$

- **Def.**: Sia $\lambda$ autovalore di $T$, la **MOLTEPLICITA' GEOMETRICA** è: 
 $$
 m_g(\lambda) \overset{\text{def}}{=} \dim(U_\lambda)
 $$

+ **PROPOSIZIONE**: 
 $T: V \longrightarrow V$ Endomorfismo, $\dim(V) = m$ 
 $\mathcal{B}$ 
 $A = M_\mathcal{B}(T)$ 
 Sia $\lambda$ autovalore di $T$ 
 $\Rightarrow$ Allora: 
 $$
 m_g(\lambda) \leq m_a(\lambda)
 $$

---

## 6.3 Diagonalizzabilità

### 6.3.1 Definizione di Diagonalizzabilità

Sia $T: V \longrightarrow V$, con $\dim(V) = m$.

$T$ si dice **DIAGONALIZZABILE**, se:

(i) Ogni matrice associata a $T$ è simile a una matrice diagonale.

(ii) Equivalentemente: Una matrice associata a $T$ è simile a una matrice diagonale.

(iii) Equivalentemente: Esiste una base $\overline{B}$ di $V$ t.c.:

- $\overline{A} = M_{\overline{B}}(T)$ è diagonale.

- $A = P \overline{A} P^{-1}$, $Q = P^{-1}$, $\overline{A} = Q^{-1} A Q$

- $P = M_{\overline{B}\overline{B}}(\text{id}_V)$, $Q = M_{\overline{B}\overline{B}}(\text{id}_V)$

---

### 6.3.2 Definizione Alternativa per Matrici

Sia $A \in M_m(K)$, $A$ è **DIAGONALIZZABILE**, se è simile a una matrice diagonale:

$$
\overline{A} = Q^{-1} A Q,
$$

dove $Q$ è la matrice che diagonalizza $A$.

---

### 6.3.3 Teorema Spettrale

Sia $T: V \longrightarrow V$ un endomorfismo, con $\dim(V) = m$.

Siano $\lambda_1, \dots, \lambda_h$ gli autovalori di $T$.

Allora sono equivalenti i seguenti fatti:

(a) $T$ è diagonalizzabile.

(b) Esiste una base $\overline{B}$ (base spettrale) di $V$ costituita da autovettori di $T$.

(c) $\sum_{i=1}^h m_g(\lambda_i) = m$

(d) $U_{\lambda_1} \oplus \dots \oplus U_{\lambda_h} = V$

(e) (i) $\sum_{i=1}^h m_a(\lambda_i) = m$ e (ii) $\forall \space  \lambda_i$ autovalore di $T$, $m_a(\lambda_i) = m_g(\lambda_i)$

---

### 6.3.4 Dimostrazione del Teorema Spettrale

(a) $\Longleftrightarrow$ (b) $\Longleftrightarrow$ (c) $\Longleftrightarrow$ (d) $\Longleftrightarrow$ (b)

**(a) $\Rightarrow$ (b)**: P.D. $\exists \space $ una base $\overline{B}$ di $V$, t.c.:

- $\overline{A} = M_{\overline{B}}(T)$ è diagonale.

- Th. $\overline{B}$ è una base spettrale.

Sia 
$$
\overline{A} = (\overline{a}_1, \overline{a}_2, \dots, \overline{a}_m) \quad \text{con} \quad \overline{a}_1, \overline{a}_2, \dots, \overline{a}_m \text{ AUTOVALORI}
$$ 
$$
\overline{B} = (\overline{e}_1, \overline{e}_2, \dots, \overline{e}_m)
$$ 
$$
T(\overline{e}_1) = \overline{a}_1 \overline{e}_1 + 0 \cdot \overline{e}_2 + \dots + 0 \cdot \overline{e}_m = \overline{a}_1 \overline{e}_1 \Rightarrow \overline{e}_1 \text{ AUTOVETTORE}
$$ 
$$
T(\overline{e}_2) = 0 \cdot \overline{e}_1 + \overline{a}_2 \overline{e}_2 + \dots + 0 \cdot \overline{e}_m = \overline{a}_2 \overline{e}_2 \Rightarrow \overline{e}_2 \text{ AUTOVETTORE}
$$ 
$$
\vdots
$$ 
$$
T(\overline{e}_m) = 0 \cdot \overline{e}_1 + 0 \cdot \overline{e}_2 + \dots + \overline{a}_m \overline{e}_m = \overline{a}_m \overline{e}_m \Rightarrow \overline{e}_m \text{ AUTOVETTORE}
$$

**"(b) ⇒ (a)":** P.I. ∃ $\overline{B} = (\overline{e}_1, \dots, \overline{e}_m)$ base di $V$, costituita da Autovettori di $T$ 
$$
\overline{B} = (\underbrace{\overline{e}_1^1, \dots, \overline{e}_{r_1}^1}_{\in U_{\lambda_1}}, \underbrace{\overline{e}_1^2, \dots, \overline{e}_{r_2}^2}_{\in U_{\lambda_2}}, \dots, \underbrace{\overline{e}_1^h, \dots, \overline{e}_{r_h}^h}_{\in U_{\lambda_h}})
$$ 
$$
T(\overline{e}_{11}^1) = \lambda_1 \overline{e}_{11}^1
$$ 
*(disegno di una matrice diagonale con elementi $\lambda_1, \lambda_2, \dots, \lambda_h$)*

**"(b) ⇒ (c) ⇒ (d)":** 
$$
m = r_1 + r_2 + \dots + r_h \leq mg(\lambda_1) + mg(\lambda_2) + \dots + mg(\lambda_h) = \dim(U_{\lambda_1} \oplus \dots \oplus U_{\lambda_h}) \leq m
$$ 
$$
\overline{e}_1^1, \dots, \overline{e}_{r_1}^1 \in U_{\lambda_1} \Rightarrow r_1 \leq \dim(U_{\lambda_1}) = mg(\lambda_1)
$$ 
*linearmente indipendenti* 
$$
\overline{e}_1^2, \dots, \overline{e}_{r_2}^2 \in U_{\lambda_2} \Rightarrow r_2 \leq \dim(U_{\lambda_2}) = mg(\lambda_2)
$$ 
*linearmente indipendenti* 
$$
\overline{e}_1^h, \dots, \overline{e}_{r_h}^h \in U_{\lambda_h} \Rightarrow r_h \leq \dim(U_{\lambda_h}) = mg(\lambda_h)
$$ 
*linearmente indipendenti*

**"(d) ⇒ (b)":** 
$\overline{B}_1$ base di $U_{\lambda_1}$ 
$\overline{B}_2$ base di $U_{\lambda_2}$ 
$\dots$ 
$\overline{B}_h$ base di $U_{\lambda_h}$ 
$$
\overline{B}_1 \cup \dots \cup \overline{B}_h \text{ è base di } U_{\lambda_1} \oplus \dots \oplus U_{\lambda_h} = V
$$

---

## 6.4 Esercizi

### 6.4.1 Esercizio 1

1) $V, \mathbb{R}^3$, $\dim(V) = 3$ 
$\mathcal{B} = \{e_1, e_2, e_3\}$ 
$T: V \longrightarrow V$ 
$\mu_{\mathcal{B}}(T) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$

$$
|A - \lambda I_3| = \begin{vmatrix} 1 - \lambda & 0 & 0 \\ 0 & -\lambda & 1 \\ 1 & 0 & -\lambda \end{vmatrix} = (1 - \lambda)(-\lambda)^2 - \lambda \cdot 1 = (1 - \lambda)\lambda^2 = 0
$$

$$
\Rightarrow \lambda \in \{0, 1\} \quad \text{con} \quad \lambda_1 = 0, \quad \lambda_2 = 1
$$

1 = $\mathrm{mg}(0) < \mathrm{ma}(0) = 2$ 
$\mathrm{ma}(1) = 1$ 
" 
$\mathrm{mg}(1)$

$U_0, \dim(U_0) = 3 - \mathrm{rank}(A) = 1$ 
$U_1, \dim(U_1) = 1$ 
$\dim(U_0 \oplus U_1) = 2 \Rightarrow U_0 \oplus U_1 \neq V$

$U_0: \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = 0 \quad \begin{cases} x_1 = 0 \\ x_2 = 0 \\ x_3 = 0 \end{cases} \Rightarrow U_0 = \{(0, x_2, 0) \mid x_2 \in \mathbb{R}\} = \mathcal{L}((0,1,0)) = \overline{\Phi_{\mathcal{B}}(U_0)}$ 
$\Rightarrow U_0 = \mathcal{L}(e_2)$

---

### 6.4.2 Esercizio 2

Sia
$$
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \\ 1 & 1 & 0 \end{pmatrix} = M_B(T)
$$

$$
|A - \lambda I_3| = \begin{vmatrix} 1 - \lambda & 0 & 0 \\ 0 & 1 - \lambda & -1 \\ 1 & 1 & -\lambda \end{vmatrix} = (-1)^2 (1 - \lambda) \begin{vmatrix} 1 - \lambda & -1 \\ 1 & -\lambda \end{vmatrix} =
$$

$$
= (1 - \lambda) \left[ (1 - \lambda)(-\lambda) + 1 \right] = (1 - \lambda) \left[ -\lambda + \lambda^2 + 1 \right]
$$

$$
\lambda^2 - \lambda + 1 \quad \quad \lambda = \frac{1 \pm \sqrt{1 - 4}}{2} \in \mathbb{C}
$$

$$
\lambda = 1
$$

$$
1 \leq \mathrm{mg}(1) \leq \mathrm{ma}(1) = 1
$$

Sia
$$
U_1: \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 1 & 1 & -1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = 0 \quad \Rightarrow \quad \begin{cases} -x_3 = 0 \\ x_1 + x_2 - x_3 = 0 \end{cases} \quad \Rightarrow \quad \begin{cases} x_3 = 0 \\ x_1 = -x_2 \end{cases}
$$

Allora:
$$
\Phi_B(U_1) = \Delta = \left\{ (-x_2, x_2, 0) \, \middle| \, x_2 \in \mathbb{R} \right\} = \mathcal{L}((-1,1,0))
$$

$$
U_2 = \Phi_B^{-1}(\Delta) = \mathcal{L}(\Phi_B^{-1}(-2,1,0)) = \mathcal{L}(-e_1 + e_2)
$$

$$
-e_1 + e_2 + 0e_3
$$

---

> **Fine Capitolo 6**