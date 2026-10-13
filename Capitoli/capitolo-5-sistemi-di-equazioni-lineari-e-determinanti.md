# Capitolo 5: Sistemi di Equazioni Lineari e Determinanti

---

## 5.1 Sistemi di Equazioni Lineari

### 5.1.1 Definizione e Matrici Associate

$m, n \in \mathbb{N}$, Consideriamo un sistema lineare di equazioni in $m$ incognite $x_1, \dots, x_m$ su un campo $K$, ossia una $m$-upla di equazioni:

$$\Sigma: \begin{cases} \n a_{11}x_1 + \dots + a_{1m}x_m - b_1 = 0 & \mathcal{D}_1 \\\na_{21}x_1 + \dots + a_{2m}x_m - b_2 = 0 & \mathcal{D}_2 \\\n\vdots \\\na_{m1}x_1 + \dots + a_{mm}x_m - b_m = 0 & \mathcal{D}_m\n\end{cases}\quad \Delta = \mathcal{D}_1 \cap \dots \cap \mathcal{D}_m$$


---

#### Esempi

1) $0x_1 + 0x_2 + \dots + 0x_m - b = 0$, $b \ne 0$

**INCOMPATIBILE**

2) $\underbrace{a_{11}x_1 + a_{12}x_2 + \dots + a_{1m}x_m - b_1 = 0}_{a_{11} \ne 0}$

$$nx_1 = -\frac{a_{12}x_2 + \dots + a_{1m}x_m - b_1}{a_{11}}$$

$$\mathcal{D}_1 = \left\{ \left( -\frac{a_{12}}{a_{11}}x_2 + \dots - \frac{a_{1m}}{a_{11}}x_m, x_2, \dots, x_m \right) \mid x_2, \dots, x_m \in K \right\}$$

---

#### Definizione di Compatibilità

$\Sigma$ si dice **COMPATIBILE** se ammette **ALMENO UNA SOLUZIONE**, ossia: $\Delta \ne \emptyset$

Altrimenti si dice **INCOMPATIBILE**

---

##### Matrice Incompleta e Matrice Completa

$$A = \begin{pmatrix} a_{11} & \dots & a_{1m} \\ \vdots & \ddots & \vdots \\ a_{m1} & \dots & a_{mm} \end{pmatrix} \rightarrow \text{PRIMA MATRICE ASSOCIATA a } \Sigma \quad (\text{opp. MATRICE DEI COEFFICIENTI, opp. MATRICE INCOMPLETA})$$

$$C = \begin{pmatrix} a_{11} & \dots & a_{1m} & | & b_1 \\ \vdots & \ddots & \vdots & | & \vdots \\ a_{m1} & \dots & a_{mm} & | & b_m \end{pmatrix} \rightarrow \text{SECONDA MATRICE ASSOCIATA a } \Sigma \quad (\text{opp. MATRICE COMPLETA})$$

e si può scrivere anche come: $C = (A \mid \mathbf{b})$

---

##### Esempio

$$\Sigma: \begin{cases}\n3x_2 + (-x_3) + 2x_4 - 3 = 0 \\\nx_1 + x_2 + 2x_3 + 5 = 0\n\end{cases}\quad A = \begin{pmatrix} 0 & 3 & -1 & 2 \\ 1 & 1 & 2 & 0 \end{pmatrix}\quad C = \begin{pmatrix} 0 & 3 & -1 & 2 & | & -3 \\ 1 & 1 & 2 & 0 & | & 5 \end{pmatrix}$$

---

##### Sistema Omogeneo Associato

$$\Sigma_0: \begin{cases}\n3x_2 + (-x_3) + 2x_4 = 0 \\\nx_1 + x_2 + 2x_3 = 0\n\end{cases}\quad \Rightarrow \text{Sistema Omogeneo } (b = 0) \quad \text{Associato a } \Sigma$$

---

### 5.1.2 Operazioni Elementari su Righe

Sia
$$B = \begin{pmatrix} b_{11} & \cdots & b_{1m} \\ \vdots & \ddots & \vdots \\ b_{m1} & \cdots & b_{mm} \end{pmatrix} \in M_{m \times m}(K)$$

I) $\forall \space  h, k \in \{1, \dots, m\}^2 : b^h \leftrightarrow b^k$

**Esempio**:
$$\begin{pmatrix} 2 & -3 & 1 & 7 \\ -1 & 0 & 5 & 4 \\ 6 & 9 & -8 & 1 \end{pmatrix}\quad h=3, \quad k=1\quad b^3 \leftarrow b^1\quad \Rightarrow\begin{pmatrix} 6 & 9 & -8 & 1 \\ -1 & 0 & 5 & 4 \\ 2 & -3 & 1 & 7 \end{pmatrix}$$

II) $\forall \space  h \in \{1, \dots, m\}^2, \forall \space  \lambda \in K \setminus \{0\} : b^h \rightarrow \lambda \cdot b^h$ (invertibile)

*N.B.: Il Sistema cambia, ma non l'Insieme delle soluzioni $\mathcal{D}$.*

III) $\forall \space  h, k \in \{1, \dots, m\}^2, \forall \space  \beta \in K : b^h \rightarrow b^h + \beta b^k$

*Il primo elemento NON Nullo da sinistra della riga $i$ si chiama PIVOT della riga $i$ 
$\Rightarrow$ Allora: $\forall \space  i \in \{1, ..., m\}, i \geq 1, a_{ij} = 0, \forall \space  j \geq l$

---

**Def.**: $A$ è COMPLETAMENTE RIDOTTA A GRADINI, se: 
I) i PIVOT sono uguali a 1 
II) Gli elementi sopra a un PIVOT (nella stessa colonna) sono NULLI.

---

**Algoritmo di Gauss e Gauss-Jordan**: 
1. (Gauss): Trasformare una matrice $C$ in una matrice ridotta a scalini: $C \rightarrow C'$ 
2. (Gauss-Jordan): Consideriamo il nuovo Sistema Lineare $\Sigma'$ che ha $C'$ come Matrice Completa e traiamo l'Insieme delle soluzioni.

---

### 5.1.3 Sistemi Lineari: Notazione Matriciale

$$\Sigma: A\mathbf{x} = \mathbf{b} \quad A \in M_{m \times n}(K) \quad (K, +, \cdot) \text{ campo } (K = \mathbb{R})$$

$$\mathbf{x} = \begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix} b_1 \\ \vdots \\ b_m \end{pmatrix}, \quad \mathcal{E} = (A \mid \mathbf{b}) \text{ Matrice Associata Completa}.$$

---

#### Operazioni o Trasformazioni Elementari (RIGHE):

I) $\forall \space  i, k \in \{1, \dots, m\}, i \ne k$, $b^i \leftrightarrow b^k$

II) $\forall \space  i, k \in \{1, \dots, m\}, \forall \space  \lambda \in K \setminus \{0\}$, $b^i \rightarrow \lambda \cdot b^k$

III) $\forall \space  i, k \in \{1, \dots, m\}, \forall \space  \beta \in K$, $b^i \rightarrow b^i + \beta b^k$

---

*Nota B*: Abbiamo visto che c'è la matrice ottenuta applicando a $\mathcal{E}$ un numero finito di TRASFORMAZIONI ELEMENTARI e $\Sigma'$ è il sistema lineare che ha come Matrice Completa Associata. Allora $\Sigma'$ è EQUIVALENTE a $\Sigma$, OSSIA ha le stesse soluzioni.

---

**TEOREMA (ALGORITMO DI GAUSS):

Ogni Matrice su un Campo $K$ può essere ridotta a completamente ridotta a scalini mediante un numero finito di operazioni elementari.

---

### 5.1.4 Teorema di Rouché-Capelli

*OSSERVAZIONE (TEOREMA di ROUCHÉ-CAPELLI):*

$\Sigma: AX = \mathbf{b} \quad \text{COMPATIBILE} \iff \text{C'è ottenuta da } \mathbf{c} \text{ e NON presente pivot nella colonna dei termini noti}$

**Il pivot si trova nella colonna dei termini noti, dunque il sistema è INCOMPATIBILE.**

---

### 5.1.5 Teorema di Struttura dell'Insieme delle Soluzioni di un Sistema Lineare Compatibile

- Sia $\Sigma: AX = b$ un sistema lineare di $m$ equazioni in $m$ incognite.
- Sia $\Sigma_0: AX = 0$ il sistema lineare omogeneo associato.
- Sia $\Delta = \left\{ (y_1, \dots, y_m) \in K^m \mid A \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix} = b \right\}$ l'insieme delle soluzioni di $\Sigma$.
- Sia $\Delta_0 = \left\{ (z_1, \dots, z_m) \in K^m \mid A \begin{pmatrix} z_1 \\ \vdots \\ z_m \end{pmatrix} = 0 \right\}$ l'insieme delle soluzioni di $\Sigma_0$.

$\Rightarrow$ Allora: Se $(\overline{y}_1, \dots, \overline{y}_m) \in \Delta$,
$\Delta = \left\{ (\overline{y}_1, \dots, \overline{y}_m) + (z_1, \dots, z_m) \mid (z_1, \dots, z_m) \in \Delta_0 \right\}$

---

#### Dimostrazione

- $\Delta \subseteq X$ e $X \subseteq \Delta$

**"⊆":**

$(y_1, \dots, y_m) \in \Delta$, considero: $(y_1, \dots, y_m) - (\overline{y}_1, \dots, \overline{y}_m) = (z_1, \dots, z_m)$

- Th. $(z_1, \dots, z_m) \in \Delta_0$

$A \left[ \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix} - \begin{pmatrix} \overline{y}_1 \\ \vdots \\ \overline{y}_m \end{pmatrix} \right] = A \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix} - A \begin{pmatrix} \overline{y}_1 \\ \vdots \\ \overline{y}_m \end{pmatrix} = b - b = 0$

$\Rightarrow$ Je p.r.e. e' distributivo 
$\cdot \lambda (AB) = (\lambda A)B = A(\lambda B)$ 
$\cdot -u = (-1)u$

$\Rightarrow$ Quindi: $(y_1, \dots, y_m) = (\overline{y}_1, \dots, \overline{y}_m) + (z_1, \dots, z_m) \in \Delta_0$

**"⊇":**

$A \left[ \begin{pmatrix} \overline{y}_1 \\ \vdots \\ \overline{y}_m \end{pmatrix} + \begin{pmatrix} z_1 \\ \vdots \\ z_m \end{pmatrix} \right] = \underbrace{A \begin{pmatrix} \overline{y}_1 \\ \vdots \\ \overline{y}_m \end{pmatrix}}_{b} + \underbrace{A \begin{pmatrix} z_1 \\ \vdots \\ z_m \end{pmatrix}}_{0} = b + 0 = b$

---

### 5.1.6 Proposizione: Insieme delle Soluzioni del Sistema Omogeneo

$\Sigma: A\mathbf{x} = \mathbf{0}, \quad \mathcal{D}_0 \subseteq K^m$

$\Rightarrow$ Allora:

(i) $\mathbf{0} \in \mathcal{D}_0$

(ii) $\forall \space  (\mathbf{z}_1, \dots, \mathbf{z}_m), \; (\mathbf{z}_1', \dots, \mathbf{z}_m') \in \mathcal{D}_0, \; (\mathbf{z}_1 + \mathbf{z}_1', \dots, \mathbf{z}_m + \mathbf{z}_m') \in \mathcal{D}_0$

(iii) $\forall \space  \alpha \in K, \; \forall \space  (\mathbf{z}_1, \dots, \mathbf{z}_m) \in \mathcal{D}_0, \; \alpha(\mathbf{z}_1, \dots, \mathbf{z}_m) \in \mathcal{D}_0$

---

#### Dimostrazione

$A\begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} = \mathbf{0} \quad \text{e} \quad \text{OSS: } \mathcal{D}_0 \neq \emptyset$

$A\left[ \begin{pmatrix} \mathbf{z}_1 \\ \vdots \\ \mathbf{z}_m \end{pmatrix} + \begin{pmatrix} \mathbf{z}_1' \\ \vdots \\ \mathbf{z}_m' \end{pmatrix} \right] = A\begin{pmatrix} \mathbf{z}_1 \\ \vdots \\ \mathbf{z}_m \end{pmatrix} + A\begin{pmatrix} \mathbf{z}_1' \\ \vdots \\ \mathbf{z}_m' \end{pmatrix} = \mathbf{0} + \mathbf{0} = \mathbf{0}$

$A\left[ \alpha \begin{pmatrix} \mathbf{z}_1 \\ \vdots \\ \mathbf{z}_m \end{pmatrix} \right] = \alpha \cdot A\begin{pmatrix} \mathbf{z}_1 \\ \vdots \\ \mathbf{z}_m \end{pmatrix} = \alpha \cdot \mathbf{0} = \mathbf{0} \quad \blacksquare$

---

**OSSERVAZIONE:**

$\Rightarrow \Sigma_0: A\mathbf{x} = \mathbf{0}, \; \mathcal{D}_0 \subseteq K^m$ è linearmente chiuso

$\Rightarrow \Sigma: A\mathbf{x} = \mathbf{b}, \; \mathcal{D} \text{ NON è linearmente chiuso} \quad \text{se } \mathbf{b} \neq \mathbf{0}$

---

## 5.2 Determinanti

### 5.2.1 Definizione e Proprietà Fondamentali

**Def.** Il **DETERMINANTE** è una funzione: 
$\det : \mathcal{M}_m(K) \longrightarrow K$
con 
$A \longmapsto |A| \quad \text{opp.} \quad \det(A)$

---

**T.C.** (Teorema Caratterizzante)

1. Se: B è la matrice ottenuta da A, scambiando due righe (opp. due colonne). 
 Allora: $|B| = -|A|$

2. Se: B è la matrice ottenuta da A, moltiplicando una riga (opp. una colonna) per uno scalare $\lambda \in K$. 
 Allora: $|B| = \lambda |A|$

3. Se: B è la matrice ottenuta da A mediante un'operazione elementare del III tipo su righe (opp. colonne). 
 Allora: $|B| = |A|$

4. $\det(I_m) = 1$

---

**N.B.** Se B è ottenuta da A mediante op. elementari, Allora: $|B| \ne 0 \iff |A| \ne 0$

---

### 5.2.2 Permutazioni e Segno

Sia $X \neq \emptyset$, $|X| = m$.

Sia $g: X \longrightarrow X$ biettiva, 
"permutazione su $X$".

$X = \{1, \dots, m\}$, 
$P_m = \{ g: \{1, \dots, m\} \longrightarrow \{1, \dots, m\} \mid g \text{ biettiva} \}$.

$|P_m| = m(m-1)\dots 3 \cdot 2 \cdot 1 = m!$

**Def.** Diciamo che una permutazione $g \in P_m$ presenta una **INVERSIONE**, se: 
$\exists \space  i, j \in \{1, \dots, m\} \text{ t.c. } i < j \text{ e } g(i) > g(j)$.

**Def.** Il segno di $g \in P_m$ è: 
$
\text{sign}(g) = 
\begin{cases}
1, & \text{se } g \text{ ha un numero pari di inversioni} \\
-1, & \text{altrimenti}
\end{cases}
$

---

### 5.2.3 Regole di Calcolo

**Regola di Sarrus**: 
**N.B.** Si può applicare solo su matrici di ordine 3.

$
\begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{vmatrix}
= a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{12}a_{21}a_{33} - a_{11}a_{23}a_{32}
$

---

**Regole per il Determinante**:

I) $|A| = |A^T|$

II) Se $A$ è triangolare (sup. opp. inf.), 
Allora: $|A| = a_{11}a_{22}\dots a_{mm}$

---

### 5.2.4 Minori, Minori Complementari e Complementi Algebrici

**Def.** Sia $A \in M_{m,m}(K)$ una matrice, si dice **MINORE** di $A$ una sua **SOTTO-MATRICE QUADRATA**.

**Def.** Sia $A \in M_{m,m}(K)$ una matrice quadrata e sia $a_{ij}$ un elemento di $A$, allora il **MINORE COMPLEMENTARE** di $a_{ij}$ è la **SOTTO-MATRICE QUADRATA** di $A$ di ordine $m-1$ che si ottiene cancellando l'$i$-esima riga e la $j$-esima colonna.

**Def.** Sia $A \in M_{m,m}(K)$ una matrice quadrata e sia $a_{ij}$ un elemento di $A$, si dice **COMPLEMENTO ALGEBRICO** di $a_{ij}$: 
$A_{ij} = (-1)^{i+j} M_{ij}$

---

### 5.2.5 Teorema di Laplace

- Sia $A \in M_m(K)$
- $\forall \space  h \in \{1, \dots, m\}, \, |A| = a_{h1}A_{h1} + a_{h2}A_{h2} + \dots + a_{hm}A_{hm}$
- $\forall \space  k \in \{1, \dots, m\}, \, |A| = a_{1k}A_{1k} + a_{2k}A_{2k} + \dots + a_{mk}A_{mk}$

*Senza Dimostrazione*

---

#### Esempio di Laplace:
$A = \begin{pmatrix} 2 & 3 & 1 \\ 0 & 4 & 2 \\ 1 & 0 & 1 \end{pmatrix}$
- $h = 2$: $\det(A) = a_{21}A_{21} + a_{22}A_{22} + a_{23}A_{23} = 4A_{22} + 2A_{23} = 4(1) + 2(-3) = -2$

- $A_{22} = (-1)^{2+2} \begin{vmatrix} 2 & 1 \\ 1 & 1 \end{vmatrix} = 1$
- $A_{23} = (-1)^{2+3} \begin{vmatrix} 2 & 3 \\ 1 & 0 \end{vmatrix} = -3$

---

### 5.2.6 Teorema di Binet

- Siano $A, B \in M_m(K)$
- $\det(AB) = \det(A) \det(B)$

---

### 5.2.7 Secondo Teorema di Laplace

- Sia $A \in M_m(K)$
- $\forall \space  h, \overline{h} \in \{1, \dots, m\}, \, h \ne \overline{h}, \, 0 = a_{h1}A_{\overline{h}1} + \dots + a_{hm}A_{\overline{h}m}$
- $\forall \space  k, \overline{k} \in \{1, \dots, m\}, \, k \ne \overline{k}, \, 0 = a_{1k}A_{1\overline{k}} + \dots + a_{mk}A_{m\overline{k}}$

---

### 5.2.8 Teorema di Laplace Generalizzato

- Sia $A \in M_m(K)$
- $\forall \space  h, \overline{h} \in \{1, \dots, m\}$
 $a_{h1}A_{\overline{h}1} + \dots + a_{hm}A_{\overline{h}m} = \delta_{h\overline{h}} |A|$
- $\forall \space  k, \overline{k} \in \{1, \dots, m\}$
 $a_{1k}A_{1\overline{k}} + \dots + a_{mk}A_{m\overline{k}} = \delta_{k\overline{k}} |A|$

- $\delta_{h\overline{h}} = \begin{cases} 1, & \text{se } h = \overline{h} \\ 0, & \text{se } h \ne \overline{h} \end{cases}$

---

### 5.2.9 Osservazione su Operazioni Elementari e Determinante

Sia $A \in M_m(K)$

1. Sia $B$ una matrice ottenuta da $A$ mediante un numero finito di operazioni elementari:
 $|A| \ne 0 \iff |B| \ne 0$

---

### 5.2.10 Teorema di Invertibilità di una Matrice

Sia $A \in M_m(K)$.

$A$ è INVERTIBILE $\iff |A| \neq 0$

**Dimostrazione:**

**"⇒":** P.I.: $\exists \space  A^{-1} : A A^{-1} = A^{-1} A = I_m$

Allora: $|A A^{-1}| = |I_m| = 1 \Rightarrow |A| \neq 0$

Inoltre: $|A^{-1}| = |A|^{-1}$

**"⇐":** Consideriamo la matrice "aggiunta" di $A$:

$A^* = \begin{pmatrix} A_{11} & A_{12} & \cdots & A_{1n} \\ A_{21} & A_{22} & \cdots & A_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{n1} & A_{n2} & \cdots & A_{nn} \end{pmatrix} \quad \text{e} \quad (A^*) = \begin{pmatrix} A_{11} & A_{21} & \cdots & A_{n1} \\ A_{12} & A_{22} & \cdots & A_{n2} \\ \vdots & \vdots & \ddots & \vdots \\ A_{1n} & A_{2n} & \cdots & A_{nn} \end{pmatrix}$

Allora: $A^{-1} = \frac{1}{|A|} A^*$

Quindi:

$
\frac{1}{|A|} A^* A = \begin{pmatrix} |A| & 0 & \cdots & 0 \\ 0 & |A| & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & |A| \end{pmatrix} = I_m
$

e

$
(A^*) A = \begin{pmatrix} |A| & 0 & \cdots & 0 \\ 0 & |A| & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & |A| \end{pmatrix} = I_m
$

$\square$

---

## 5.3 Teorema di Kronecker (o degli Orlati)

Sia $A \in M_{m,n}(K)$

Se il Rango di $A = \text{rank}(A) = \min\{m, n\} \iff \exists \space  H \subset A$, $\det(H) \neq 0$

(i) $\text{rank}(A) = \min\{m, n\}$

oppure

(ii) $\text{rank}(A) < \min\{m, n\}$ e tutti gli ORLATI di $A$ hanno $\det = 0$

---

**Definizione:** Sia $A \in M_{m,n}(K)$

Sia $H$ un minore di $A$ di ordine $h \leq \min\{m, n\}$

Un ORLATO di $H$ è un minore $H'$ di $A$ di ordine $h+1$ di cui $H$ è una SOTTO-MATRICE.

---

> **Fine Capitolo 5**