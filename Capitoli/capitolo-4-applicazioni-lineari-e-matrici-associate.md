# Capitolo 4: Applicazioni Lineari e Matrici Associate

---

## 4.1 Definizioni e Proprietà Generali

### 4.1.1 Definizione di Applicazione Lineare

$T: V \longrightarrow W$ Applicazione Lineare

I) $\forall \space  v \in V, \, \forall \space  \omega \in W, \, T(\omega v) = \omega T(v)$ 

-DIM: 
$T(\omega v) = T(0 \cdot \omega v) = 0 \cdot T(\omega v) = \omega T(v) \quad \square$

II) Le Applicazioni Lineari conservano le combinazioni lineari, ossia: 
$\forall \space  u_1, \dots, u_m \in V \quad \forall \space  \alpha_1, \dots, \alpha_m \in K$: 
$T(\alpha_1 u_1 + \dots + \alpha_m u_m) = \alpha_1 T(u_1) + \dots + \alpha_m T(u_m)$

---

### 4.1.2 Dimostrazione per Induzione

$h > 1 \quad h - 1 \Rightarrow h$, Per Induzione:

$$T(\alpha_1 \mu_1 + \ldots + \alpha_m \mu_m) = \alpha_1 T(\mu_1) + \ldots + \alpha_{h-1} T(\mu_{h-1}) + T(\alpha_h \mu_h) \stackrel{?}{=} T(\alpha_1 \mu_1 + \ldots + \alpha_{h-1} \mu_{h-1}) + T(\alpha_h \mu_h) = \alpha_1 T(\mu_1) + \ldots + \alpha_{h-1} T(\mu_{h-1}) + \alpha_h T(\mu_h) \quad \square$$

---

### 4.1.3 Proprietà: Conservazione della Dipendenza Lineare

#### Proposizione

$T: V \longrightarrow W$ Applicazione lineare, $K$

- Se: $(\mu_1, \ldots, \mu_m)$ è una $m$-upla di vettori di $V$ linearmente dipendente 
 $\Rightarrow (\,T(\mu_1), \ldots, T(\mu_m)\,)$ è una $m$-upla di $W$ linearmente dipendente

---

##### Dimostrazione

- Th. $\exists \space  (\beta_1, \ldots, \beta_m) \in K^m \setminus \{0\} : \beta_1 T(\mu_1) + \ldots + \beta_m T(\mu_m) = 0_W$

- hp. $\exists \space  (\alpha_1, \ldots, \alpha_m) \in K^m \setminus \{0\} : \alpha_1 \mu_1 + \ldots + \alpha_m \mu_m = 0_V$

- $T(\alpha_1 \mu_1 + \ldots + \alpha_m \mu_m) = T(0_V) = 0_W$

- $\iff \alpha_1 T(\mu_1) + \ldots + \alpha_m T(\mu_m)$

- Se: prendo $(\beta_1, \ldots, \beta_m) = (\alpha_1, \ldots, \alpha_m) \Rightarrow \checkmark \quad \square$

---

### 4.1.4 Proprietà: Conservazione della Linearità Dipendente

Le Applicazioni Lineari conservano la Linearità Dipendente

---

### 4.1.5 Tipi di Applicazioni Lineari

#### Definizione di Nucleo (Kernel)

$T: V \longrightarrow W$ Applicazione lineare 
Si chiama Nucleo o Kernel di $T$ l'insieme:

$$\ker(T) = \{ \mu \in V \mid T(\mu) = 0_W \}$$

---

#### Proposizione Fondamentale

$T: V \longrightarrow W$ Applicazione lineare

- (I) $T$ è SURIETTIVA $\iff \operatorname{Im}(T) = W$

 $$T(V) = \{ T(\mu) \mid \mu \in V \}$$

- (II) $T$ è INIETTIVA $\iff \ker(T) = \{0_V\}$

- (III) $S \subseteq V$, $L(S) \subseteq V$, $T(L(S)) = L(T(S))$

---

#### Dimostrazione di (II)

**(ii) "$\Rightarrow$":** $T(\Omega_v) = \Omega_w$ e $T$ è **iniettiva**

$\forall \space  \mu \in V \setminus \{\Omega_v\}, \text{ ossia: } \mu \neq \Omega_v \Rightarrow T(\mu) \neq T(\Omega_v) = \Omega_w$

$\Rightarrow \forall \space  \mu \in V \setminus \{\Omega_v\}, \mu \notin \text{Ker}(T)$

Quindi: $\text{Ker}(T) = \{\Omega_v\}$

"$\Leftarrow$": Th. $\forall \space  \mu, \nu \in V, T(\mu) = T(\nu) \Rightarrow \mu = \nu$

$T(\mu) = T(\nu) \Rightarrow T(\mu) - T(\nu) = \Omega_w \Rightarrow \mu - \nu \in \text{Ker}(T) = \{\Omega_v\}$

$\Rightarrow \mu - \nu = \Omega_v \Rightarrow \mu = \nu$

---

**(iii) "$\Leftarrow$":** $\forall \space  \omega \in T(\mathcal{L}(S)) \Rightarrow \exists \space  \mu \in \mathcal{L}(S): T(\mu) = \omega$

$\Downarrow$

$\exists \space  \mu_1, \dots, \mu_k \in S: \mu = \alpha_1 \mu_1 + \dots + \alpha_k \mu_k$

$\exists \space  \alpha_1, \dots, \alpha_k \in K$

$\cdot \alpha_1 T(\mu_1) + \dots + \alpha_k T(\mu_k) \in T(\mathcal{L}(S))$

---

#### Proposizione: Conservazione dell'Indipendenza Lineare

$T: V \longrightarrow W$ Applicazione lineare

- Se: $T$ è INIETTIVA
- Se: $(\mu_1, \dots, \mu_m)$ è una $m$-upla di vettori di $V$ linearmente indipendente

$\Rightarrow (T(\mu_1), \dots, T(\mu_m))$ è una $m$-upla di vettori di $W$ linearmente indipendente

---

##### Dimostrazione

Th.

- Se: $(\alpha_1, \dots, \alpha_m) \in K^m : \alpha_1 T(\mu_1) + \dots + \alpha_m T(\mu_m) = \mathbf{0}_W$

Allora: $\alpha_1 = \dots = \alpha_m = 0$

$\alpha_1 T(\mu_1) + \dots + \alpha_m T(\mu_m) = \mathbf{0}_W$

$\Downarrow$

$T(\alpha_1 \mu_1 + \dots + \alpha_m \mu_m) = \mathbf{0}_W \Rightarrow \alpha_1 \mu_1 + \dots + \alpha_m \mu_m \in \text{Ker}(T)$

$\Rightarrow \alpha_1 \mu_1 + \dots + \alpha_m \mu_m = \mathbf{0}_V \Rightarrow \alpha_1 = \dots = \alpha_m = 0$ $\square$

---

### 4.1.6 Isomorfismo

**OSSERVAZIONE:**

$T: V \longrightarrow W$ ISOMORFISMO

Se $V$ linearmente indipendente $\Rightarrow T(S)$ lin. ind.

---

**Definizione**:
$T: V \to W$ ISOMORFISMO
$S \subseteq V$

+ **PROPOSIZIONE**: 
$S$ linearmente indipendente $\iff T(S)$ linearmente indipendente
---

## 4.2 Nucleo, Immagine ed Equazione Dimensionale

### 4.2.1 Definizione di Nucleo e Immagine

$T: V \longrightarrow W$ Applicazione lineare

Si chiama **Nucleo** o **Kernel** di $T$ l'insieme:
$$\ker(T) = \{ \mu \in V \mid T(\mu) = 0_W \}$$

Si chiama **Immagine** di $T$ l'insieme:
$$\operatorname{Im}(T) = T(V) = \{ T(\mu) \mid \mu \in V \}$$

---

### 4.2.2 Proposizione sul Nucleo

$\cdot$ Supponiamo $\text{Ker}(T) = \{ \mu \in V \mid T(\mu) = \Omega_w \}$

$T(\Omega_v) = \Omega_w \Rightarrow \Omega_v \in \text{Ker}(T) \Rightarrow \text{Ker}(T) \neq \emptyset$

$\mu, \nu \in \text{Ker}(T) \Rightarrow T(\mu) = \Omega_w = T(\nu)$

$\cdot$ Th. $\mu + \nu \in \text{Ker}(T)$

$T(\mu + \nu) = T(\mu) + T(\nu) = \Omega_w + \Omega_w = \Omega_w \Rightarrow \mu + \nu \in \text{Ker}(T)$

Sia $\alpha \in K$, $\mu \in \text{Ker}(T)$.

$\Downarrow$

$T(\mu) = \mathbf{0}_W$

$\text{Th. } \forall \space  \alpha \in K, \mu \in \text{Ker}(T) \Rightarrow T(\alpha \mu) = \alpha T(\mu) = \alpha \mathbf{0}_W = \mathbf{0}_W \Rightarrow \alpha \mu \in \text{Ker}(T)$ $\square$

---

### 4.2.3 Teorema Dimensionale

**TEOREMA DELLA EQUAZIONE DIMENSIONALE:**

$T: V \longrightarrow W$ Applicazione lineare, $\dim(V) = m$

$$\dim(V) = \dim(\text{Ker}T) + \dim(\text{Im}T)$$

---

**OSSERVAZIONE:**

(a) $\dim(V) > \dim(W) \Rightarrow T$ NON INIETTIVA

(b) $\dim(V) < \dim(W) \Rightarrow T$ NON SURIETTIVA

$V = \mathcal{L}(\mu_1, \dots, \mu_m) \quad T(V) = \mathcal{L}(T(\mu_1), \dots, T(\mu_m))$

- Se: $\dim(V) = \dim(W)$, osservate che:

$T$ INIETTIVA $\iff$ $T$ SURIETTIVA

---

## 4.3 Matrici Associate ad Applicazioni Lineari

### 4.3.1 Definizione di Matrice Associata

Sia $V, W$ spazi vettoriali su $K$, con $\dim(V) = m$, $\dim(W) = n$.

Sia $T: V \longrightarrow W$ un'applicazione lineare.

Siano $B_V = (e_1, \dots, e_m)$ e $B_W = (e'_1, \dots, e'_n)$ basi di $V$ e $W$, rispettivamente.

Allora:
$$T(e_1) = a_{11} e'_1 + \dots + a_{n1} e'_n \quad \text{e} \quad \Phi_{B_W}(T(e_1)) = \begin{pmatrix} a_{11} \\ \vdots \\ a_{n1} \end{pmatrix}$$
$$
T(e_m) = a_{1m} e'_1 + \dots + a_{nm} e'_n \quad \text{e} \quad \Phi_{B_W}(T(e_m)) = \begin{pmatrix} a_{1m} \\ \vdots \\ a_{nm} \end{pmatrix}$$

Definiamo la matrice $A = \begin{pmatrix} a_{11} & \dots & a_{1m} \\ \vdots & \ddots & \vdots \\ a_{n1} & \dots & a_{nm} \end{pmatrix} =: M_{B_V, B_W}(T) \in M_{n \times m}(K)$.

Sia $u \in V$, allora $u = x_1 e_1 + \dots + x_m e_m$, e $T(u) \in W$, quindi $T(u) = y_1 e'_1 + \dots + y_n e'_n$.

Allora:
$$\begin{bmatrix} A \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} \end{bmatrix} = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}$$

e si dice che $A$ è la **"rappresentazione di $T$ in $B_V$ e $B_W$"**.

---

**Schematizziamo la situazione:**

$\begin{array}{c}
V \xrightarrow{T} W \\
\downarrow \Phi_{B_V} \quad \downarrow \Phi_{B_W} \\
K^m \xrightarrow{T_A} K^n
\end{array}\quad \text{dove } T_A = \Phi_{B_W} \circ T \circ \Phi_{B_V}^{-1} : K^m \longrightarrow K^n$

Inoltre, l'immagine di $T$ è:
$\operatorname{Im}(T) = \mathcal{L}(T(e_1), \dots, T(e_m)) = \Phi_{B_W}(\operatorname{Im}(T))$

Il **rango** di $A$ è:
$\operatorname{Rango}(A) = \dim(\operatorname{Im}(T))$

---

### 4.3.2 TEOREMA (Caratterizzazione delle Matrici Associate alle Applicazioni Lineari)

$$T: V \longrightarrow W \quad \text{Applicazione Lineare}$$

- $\mathcal{B}_V = (e_1, \dots, e_m) \subset V$
- $\mathcal{B}_W = (e'_1, \dots, e'_m) \subset W$
- $\Phi_{\mathcal{B}_V}(u) = (x_1, \dots, x_m)$, $\Phi_{\mathcal{B}_W}(T(u)) = (y_1, \dots, y_m)$

$$\Rightarrow \exists \space ! A \in M_{m \times m}(K) \text{ t.c. } \quad A \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} = \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix}$$

---

#### Osservazione

$$\widetilde{T}_A = \Phi_{\mathcal{B}_W} \circ T \circ \Phi_{\mathcal{B}_V}^{-1}$$

$$\widetilde{T}_A((1,0,\dots,0)) = \Phi_{\mathcal{B}_W}(T(\Phi_{\mathcal{B}_V}^{-1}((1,0,\dots,0)))) = \Phi_{\mathcal{B}_W}(T(e_1))$$

$$\widetilde{T}_A((0,\dots,1)) = \Phi_{\mathcal{B}_W}(T(\Phi_{\mathcal{B}_V}^{-1}((0,\dots,0,1)))) = \Phi_{\mathcal{B}_W}(T(e_m))$$

> *Le colonne sono fatte dalle componenti, nello spazio del codominio, delle immagini dei vettori della base del dominio (nell'ordine finito)*

---

#### Dimostrazione

**(i)** La matrice associata a $T$ soddisfa la condizione 
**(ii)** L'unicità.

---

##### I) $T(u) = T(x_1 e_1 + \dots + x_m e_m) = x_1 T(e_1) + \dots + x_m T(e_m)$

$$= x_1 (a_{11} e'_1 + \dots + a_{m1} e'_m) + \dots + x_m (a_{1m} e'_1 + \dots + a_{mm} e'_m)$$

$$= (a_{11} x_1 + \dots + a_{1m} x_m) e'_1 + \dots + (a_{m1} x_1 + \dots + a_{mm} x_m) e'_m$$

$$\Rightarrow \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix} = \begin{pmatrix} a_{11} x_1 + \dots + a_{1m} x_m \\ \vdots \\ a_{m1} x_1 + \dots + a_{mm} x_m \end{pmatrix} = A \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix}$$

---

##### II) Sia $B \in M_{m \times m}(K)$:

$$B \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} = \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix} \quad \text{. Prendendo: } u = e_1$$

$$\Phi_{\mathcal{B}_V}(e_1) = (1,0,\dots,0)$$

$$\Phi_{\mathcal{B}_W}(T(e_1)) = (a_{11}, a_{21}, \dots, a_{m1})$$

$$B\left(\begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}\right) = \begin{pmatrix} a_{11} \\ \vdots \\ a_{m1} \end{pmatrix} = \vec{a}_1$$

$\begin{pmatrix}
b_{11} & b_{12} & \cdots & b_{1m} \\
b_{21} & b_{22} & \cdots & b_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
b_{m1} & b_{m2} & \cdots & b_{mm}
\end{pmatrix}
\begin{pmatrix}
1 \\
0 \\
\vdots \\
0
\end{pmatrix}
=
\begin{pmatrix}
b_{11} \\
b_{21} \\
\vdots \\
b_{m1}
\end{pmatrix}
= \vec{b}_1$

**Prendendo**: $u = \vec{e}_2$

$\Phi_B(\vec{e}_2) = (0, 1, \dots, 0)$

$\vec{b}_2 = B\left(\begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}\right) = \vec{a}_2 \Rightarrow \text{Perché vale } B\left(\begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix}\right) = \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix}$

e per come è, **gotta A**.

---

### 4.3.3 Matrice di Passaggio e Cambiamento di Base

**Caso Particolare: Molto Importante**

$V = W, \quad \dim(V) = m$

$\text{id}_V : V \longrightarrow V$

$\begin{array}{c}\text{Id} \\\n\downarrow \\\nT \\\n\downarrow \\\nB \\\n\downarrow \\\n\overline{B}\end{array}$

$\mathcal{B} = (\vec{e}_1, \dots, \vec{e}_m)\quad ; \quad\overline{\mathcal{B}} = (\vec{e}_1, \dots, \vec{e}_m)$

$P = M_{\mathcal{B}\overline{\mathcal{B}}}(\text{id}_V) = \left( \begin{array}{c} \text{Componente di } T(\vec{e}_1) = \vec{e}_1 \text{ in } \mathcal{B} \\ \text{Componente di } T(\vec{e}_m) = \vec{e}_m \text{ in } \overline{\mathcal{B}} \end{array} \right)$

**"Matrice di Passaggio"**
**"Matrice di Cambiamento di Base"**

$\text{rango}(P) = m, \quad |P| \neq 0$

$P\left(\begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix}\right) = \begin{pmatrix} \overline{x}_1 \\ \vdots \\ \overline{x}_m \end{pmatrix}\quad * = \Phi_{\mathcal{B}}(\mu)\quad ** = \Phi_{\overline{\mathcal{B}}}(\mu)$

---

**OSSERVAZIONE:**

$V, K$

$T: V \longrightarrow W$ ISOMORFISMO

$\begin{array}{c}B_V \\\n\downarrow \\\nB_W\end{array}$

$A = M_{B_V B_W}(T) \Longrightarrow A^{-1} = M_{B_W B_V}(T^{-1})$

$T: V \longrightarrow W \quad T': W \longrightarrow V$

$\begin{array}{c}B_V \\\n\downarrow \\\nB_W\end{array} \quad\begin{array}{c}B_W \\\n\downarrow \\\nB_V\end{array}$

$A = M_{B_V B_W}(T)$

$C = M_{B_W B_V}(T')$

$\Rightarrow CA = M_{B_V B_W}(T' \circ T)$

---

### 4.3.4 Matrici Simili per Endomorfismi

**Definizione**: $A, \bar{A} \in M_m(K)$ si dicono **simili**, se esiste una **MATRICE INVERTIBILE** $P$ t.c.:

$A = P^{-1} \bar{A} P \quad (\bar{A} = P A P^{-1}, \quad Q = P^{-1})$

---

**TEOREMA**:

$T: V \longrightarrow V \quad \dim(V) = m$

$B \quad A \equiv M_B(T) \quad \bar{B} \quad \bar{A} \equiv M_{\bar{B}}(T)$

$\Rightarrow \text{Allora: } A \text{ e } \bar{A} \text{ sono SIMILI}$

---

**PROPOSIZIONE**:

$A, \bar{A} \in M_m(K)$

Se $A$ e $\bar{A}$ sono simili, allora esiste un endomorfismo $T: V \longrightarrow V$ su $K$, $\dim(V) = m$, t.c. $A$ è la matrice associata a $T$ in una certa base $B$ di $V$ e $\bar{A}$ è la matrice associata a $T$ in un'altra base $\bar{B}$ di $V$.

---

> **Fine Capitolo 4**