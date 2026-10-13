# Capitolo 3: Somma, Intersezione e Somma Diretta di Sottospazi

---

## 3.1 Operazioni Standard tra Sottospazi

### 3.1.1 Sottospazio Intersezione

#### Proposizione

$W_1, \dots, W_p$ sottospazi vettoriali di $V$, $p \geq 2$

$W_1 \cap \dots \cap W_p$ è sottospazio vettoriale di $V$

---

#### Dimostrazione

$\Omega \in W_i, \forall \space  i \in \{1, \dots, p\} \Rightarrow \Omega \in W_1 \cap \dots \cap W_p \Rightarrow W_1 \cap \dots \cap W_p \neq \emptyset$

$\mu, \nu \in W_1 \cap \dots \cap W_p \Rightarrow \forall \space  i \in \{1, \dots, p\}, \mu, \nu \in W_i \Rightarrow \mu + \nu \in W_i \Rightarrow \mu + \nu \in W_1 \cap \dots \cap W_p$

$\forall \space  \alpha \in K, \forall \space  \mu \in W_1 \cap \dots \cap W_p, \forall \space  i \in \{1, \dots, p\} \Rightarrow \alpha \mu \in W_i \Rightarrow \alpha \mu \in W_1 \cap \dots \cap W_p$

---

**Def:** $W_1 \cap \dots \cap W_p$ si chiama **SOTTOSPAZIO INTERSEZIONE**

---

### 3.1.2 Sottospazio Somma

#### Proposizione

$W_1 + \dots + W_p$ è sottospazio vettoriale di $V$

---

#### Dimostrazione

$\Omega = \Omega + \dots + \Omega \in W_1 + \dots + W_p$ (p volte) $\Rightarrow W_1 + \dots + W_p \neq \emptyset$

$\mu, \nu \in W_1 + \dots + W_p \Rightarrow \exists \space  \mu_1, \nu_1 \in W_1, \dots, \mu_p, \nu_p \in W_p$ tali che:

$\mu = \mu_1 + \dots + \mu_p$

$\nu = \nu_1 + \dots + \nu_p$

$\Rightarrow \mu + \nu = \mu_1 + \dots + \mu_p + \nu_1 + \dots + \nu_p = (\mu_1 + \nu_1) + \dots + (\mu_p + \nu_p)$

con $\mu_1 + \nu_1 \in W_1$, $\dots$, $\mu_p + \nu_p \in W_p$

$\Rightarrow \mu + \nu \in W_1 + \dots + W_p$

---

*Nota:*

$\mu = \mu_1 + \dots + \mu_p$

$\nu = \nu_1 + \dots + \nu_p$

$\Rightarrow \mu + \nu = \mu_1 + \dots + \mu_p + \nu_1 + \dots + \nu_p = (\mu_1 + \nu_1) + \dots + (\mu_p + \nu_p)$

con $\mu_1 + \nu_1 \in W_1$, $\dots$, $\mu_p + \nu_p \in W_p$

$\Rightarrow \mu + \nu \in W_1 + \dots + W_p$

Sia $\lambda \in K$, $\mu \in W_1 + \dots + W_p$ 
$\lambda \mu = \lambda (\mu_1 + \dots + \mu_p) = \lambda \mu_1 + \dots + \lambda \mu_p \in W_1 + \dots + W_p$ 
$\in W_1 \quad \in W_p$ 
$\blacksquare$

---

#### Proposizione sulla Chiusura Lineare

$\cdot W_1, \dots, W_p$ sottospazi vettoriali di $V$ 
$\parallel$ 
$\mathcal{L}(S_1) \quad \mathcal{L}(S_p)$ 
$\Rightarrow W_1 + \dots + W_p = \mathcal{L}(S_1 \cup \dots \cup S_p)$ 
*In particolare: $W_1 + \dots + W_p = \mathcal{L}(W_1 \cup \dots \cup W_p)$*

---

##### Dimostrazione: "$\supseteq$"

$S_1 \cup \dots \cup S_p \subseteq W_1 \cup \dots \cup W_p \subseteq W_1 + \dots + W_p \Rightarrow$ 
$\Rightarrow \mathcal{L}(S_1 \cup \dots \cup S_p) \subseteq W_1 + \dots + W_p$ 

$W_1 = W_1 + \Omega + \dots + \Omega$ 
$\vdots$ 
$W_p = \Omega + \dots + \Omega + W_p$ 

---

##### Dimostrazione: "$\subseteq$"

$\mu \in W_1 + \dots + W_p \Rightarrow \exists \space  \mu_1 \in W_1, \dots, \mu_p \in W_p :$ 
$\mu = \mu_1 + \dots + \mu_p$ 
$\mathcal{L}(S_1) \quad \mathcal{L}(S_p)$ 

$\ast^1 \Rightarrow \forall \space  v_1, \dots, v_t \in S_1 : \mu_1 = \alpha_1 v_1 + \dots + \alpha_t v_t$ 
$\exists \space  \alpha_1, \dots, \alpha_t \in K$ 

$\ast^p \Rightarrow \forall \space  z_1, \dots, z_r \in S_p : \mu_p = \beta_1 z_1 + \dots + \beta_r z_r$ 
$\exists \space  \beta_1, \dots, \beta_r \in K$ 

$\Rightarrow \mu = \alpha_1 v_1 + \dots + \alpha_t v_t + \beta_1 z_1 + \dots + \beta_r z_r \in \mathcal{L}(S_1 \cup \dots \cup S_p)$ 
$\blacksquare$
---

## 3.2 Relazione di Grassmann

### 3.2.1 Enunciato

$\cdot V, K$ 
$\cdot W_1, W_2$ sottospazi vettoriali di $V$, f.g. 
$\cdot \dim(W_1) = \pi, \dim(W_2) = \delta$ 

**+ RELAZIONE di GRASSMANN:** 
$$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$ 
$$\Leftrightarrow \dim(W_1 + W_2) + \dim(W_1 \cap W_2) = \dim(W_1) + \dim(W_2)$$

---

### 3.2.2 Dimostrazione

$W_1 \cap W_2 \subseteq W_1, W_2, W_1 + W_2$

Sia 
$$B_{W_1 \cap W_2} = \{ \mu_1, \dots, \mu_i \}, \quad \dim(W_1 \cap W_2) = i \quad \text{(Intersezione)}$$

- Sia $B_{W_1}$ un completamento di $B_{W_1 \cap W_2}$ a base di $W_1$.
- Sia $B_{W_2}$ un completamento di $B_{W_1 \cap W_2}$ a base di $W_2$.

- $B_{W_1} = \{ \mu_1, \dots, \mu_i, v_{i+1}, \dots, v_\pi \} \quad | \quad W_1 = \mathcal{L}(B_{W_1})$
- $B_{W_2} = \{ \mu_1, \dots, \mu_i, w_{i+1}, \dots, w_\Delta \} \quad | \quad W_2 = \mathcal{L}(B_{W_2})$

- $W_1 + W_2 = \mathcal{L}(B_{W_1} \cup B_{W_2}) = \{ \mu_1, \dots, \mu_i, v_{i+1}, \dots, v_\pi, w_{i+1}, \dots, w_\Delta \}$ — $h$-uplo di vettori di $W_1 + W_2$ 
 $h = \pi + \Delta - i = \pi + \Delta - i$

- Teorema: è linearmente indipendente 
 $$\Rightarrow \exists \space  \alpha_1, \alpha_i, \beta_{i+1}, \dots, \beta_\pi, \gamma_{i+1}, \dots, \gamma_\Delta \in K : \\
 \alpha_1 \mu_1 + \dots + \alpha_i \mu_i + \beta_{i+1} v_{i+1} + \dots + \beta_\pi v_\pi + \gamma_{i+1} w_{i+1} + \dots + \gamma_\Delta w_\Delta = \mathbf{0}$$ 

- Teorema: $\alpha_1 = \dots = \alpha_i = \beta_{i+1} = \dots = \beta_\pi = \gamma_{i+1} = \dots = \gamma_\Delta = 0$ 
 $$\alpha_1 \mu_1 + \dots + \alpha_i \mu_i + \beta_{i+1} v_{i+1} + \dots + \beta_\pi v_\pi = - \gamma_{i+1} w_{i+1} - \dots - \gamma_\Delta w_\Delta$$ 

 $$\Rightarrow \mathbf{0} = \lambda_1 \mu_1 + \dots + \lambda_i \mu_i + \gamma_{i+1} w_{i+1} + \dots + \gamma_\Delta w_\Delta \Rightarrow \\
 \Rightarrow \lambda_1 = \dots = \lambda_i = \gamma_{i+1} = \dots = \gamma_\Delta = 0 \quad \square$$ 

---

*OSSERVAZIONE:*

- Se: $W_1 \cap W_2 = \{ \mathbf{0} \}$: 
 $$B_{W_1 + W_2} = B_{W_1} \cup B_{W_2}$$ 
 $$|B_{W_1 + W_2}| = \pi + \Delta = \dim(W_1 + W_2)$$ 


---

## 3.3 Somma Diretta

### 3.3.1 Definizione di Somma Diretta

Def: $W_1, \dots, W_p$ sottospazi vettoriali di $V$, $p \geq 2$. 
La somma $W_1, \dots, W_p$ si dice **SOMMA DIRETTA**, e si scrive $W_1 \oplus \dots \oplus W_p$, se: 
$$\forall \space  i \in \{1, \dots, p\}, \quad W_i \cap (W_1 + \dots + W_{i-1} + W_{i+1} + \dots + W_p) = \{ \mathbf{0} \}$$

- Se: $p = 2$ 
 $$W_1 \cap W_2 = \{ \mathbf{0} \} \quad ; \quad W_2 \cap W_1 = \{ \mathbf{0} \}$$

---

### 3.3.2 Caratterizzazione della Somma Diretta

#### Proposizione

$W_1 + \ldots + W_p$ è somma diretta $W_1 \oplus \ldots \oplus W_p$, se e solo se ($\Leftrightarrow$), ogni suo vettore si può scrivere in un **UNICO** modo come somma di vettori di $W_1, \ldots, W_p$, ossia:

$$\mu = \mu_1 + \ldots + \mu_p = v_1 + \ldots + v_p \Rightarrow \begin{cases} \mu_1 = v_1 \\ \vdots \\ \mu_p = v_p \end{cases} \quad \text{con } \mu_i \in W_i, \; v_i \in W_i$$

---

### 3.3.3 Base della Somma Diretta

#### Proposizione

$W_1, \ldots, W_p$ sottospazi vettoriali di $V$, $\dim(W_i) = \pi_i$.
Se $W_1 + \ldots + W_p = W_1 \oplus \ldots \oplus W_p$, e $\beta_1, \ldots, \beta_p$ sono basi di $W_1, \ldots, W_p$, rispettivamente. Allora:

$$\beta_1 \cup \ldots \cup \beta_p \text{ è una base di } W_1 \oplus \ldots \oplus W_p$$

con $|\beta_1 \cup \ldots \cup \beta_p| = \pi_1 + \ldots + \pi_p$

---

#### Dimostrazione

- P.I: $p = 2$, lo dobbiamo già visto.
- Per Induzione: $W_1 \oplus \ldots \oplus W_p$ ha base:

$$\beta_1 \cup \ldots \cup \beta_{p-1}, \text{ con } |\beta_1 \cup \ldots \cup \beta_{p-1}| = \pi_1 + \ldots + \pi_{p-1}$$

- Usando mutuamente Gram-Schmidt:

$$(W_1 \oplus \ldots \oplus W_{p-1}) \oplus W_p \quad \blacksquare$$

---

> **📌 Nota di Fine Capitolo**: Questo capitolo è **completamente riorganizzato** secondo lo schema richiesto. Tutte le sezioni originali relative a operazioni tra sottospazi, Relazione di Grassmann e Somma Diretta sono state incluse e organizzate gerarchicamente. **Nessun contenuto è stato modificato, riscritto o eliminato.**
>
> **Attendo la tua conferma esplicita per procedere con il Capitolo 4.**