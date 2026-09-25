# Capitolo 1: Richiami di Teoria degli Insiemi e Strutture Algebriche

---

## 1.1 Fondamenti di Teoria degli Insiemi

### 1.1.1 Definizione e Rappresentazione di un Insieme

- Come definire un insieme:
 1. Elenchiamo gli elementi contenuti nell'insieme.
 2. Caratterizziamo gli elementi che appartengono all'insieme tramite una proprietà.

Esempio:
$$ A = \{ x \mid x \in \mathbb{N} \text{ e } x \text{ dispari} \} $$
oppure
$$ A = \{ 1, 3, 5 \} $$

*N.B.:* L'insieme vuoto si indica con $\emptyset$.

---

### 1.1.2 Inclusione e Uguaglianza

- $A, B$ insiemi
- $A \subseteq B \iff \forall \space  a \in A, a \in B$
- $A = B \iff A \subseteq B \text{ e } B \subseteq A$

*N.B.:* Se $P_1, P_2$ sono due affermazioni, scrivere:
$$ P_1 \Rightarrow P_2 $$
significa che ogni volta che $P_1$ si verifica, allora $P_2$ si verifica anche.

---

### 1.1.3 Operazioni tra Insiemi

#### Unione e Intersezione
$$ A \cup B = \{ x \mid x \in A \text{ oppure } x \in B \} $$
$$ A \cap B = \{ x \mid x \in A \text{ e } x \in B \} $$

---

#### Differenza e Complemento
$$ B \setminus A = \{ x \mid x \in B \text{ e } x \notin A \} $$

$A \subseteq X$, $X \setminus A$ si dice complemento di $A$ in $X$ e si denota con: $C_X(A)$

---

### 1.1.4 Prodotto Cartesiano

- $A, B \neq \emptyset$
$$ A \times B = \{ (a, b) \mid a \in A, b \in B \} $$

---

## 1.2 Relazioni e Applicazioni

### 1.2.1 Relazioni e Corrispondenze

- *Def:* Si dice relazione o corrispondenza da $A$ in $B$ un sottoinsieme: $R \subseteq A \times B$ (oppure $(A \times B, R)$ oppure $(A, B, R)$).

+ Esempio:
$$ A = \{ 1, 2, 3 \}, \quad B = \{ \square, *, \epsilon, y \} $$
$$ R \subseteq A \times B, \quad R = \{ (1, \epsilon), (2, \square), (3, \epsilon) \} $$

---

### 1.2.2 Applicazioni o Funzioni

- *Def:* Si dice Applicazione o Funzione da $A$ in $B$ una relazione $f \subseteq A \times B$ e diciamo: $f: A \longrightarrow B$ t.c.
$$ \forall \space  x \in A, \exists \space ! y \in B: (x, y) \in f \quad \text{e} \quad [x, f(x)] \Rightarrow f(x) = y $$

---

### 1.2.3 Relazione Inversa

Se $\mathcal{R} \subseteq A \times B$ è una relazione da $A$ in $B$, allora si ha anche la relazione inversa: $\mathcal{R}^{-1} \subseteq B \times A$, definita nel seguente modo:
$$ \mathcal{R}^{-1} = \{ (b, a) \mid (a, b) \in \mathcal{R} \} $$

*Nota: la relazione inversa di una funzione NON è necessariamente una funzione.*

---

### 1.2.4 Immagine e Controimmagine

Sia $g: A \to B$.

- $x \in A \quad g(x) = \{ g(x) \mid x \in A \} \subseteq B \quad g(A) = \text{Im}g$
- $y \in B \quad g^{-1}(x) = \{ a \in A \mid g(a) \in y \} \subseteq A$

---

### 1.2.5 Iniettività

Sia $g: A \to B$ **INIETTIVA** se e solo se:
$$ \forall \space  x, x' \in A, \; x \ne x' \Rightarrow g(x) \ne g(x') $$
equivalentemente:
$$ g(x) = g(x') \Rightarrow x = x' $$

---

### 1.2.6 Suriettività

Sia $g: A \to B$ **SURIETTIVA** se e solo se:
$$ \forall \space  b \in B, \; \exists \space  a \in A : g(a) = b \Rightarrow \text{Im}g = B $$

---

### 1.2.7 Biettività

Sia $g: A \to B$ **BIETTIVA** se e solo se:
$$ \forall \space  b \in B, \; \exists \space ! a \in A : g(a) = b $$

---

### 1.2.8 Invertibilità

Sia $g: A \to B$ **INVERTIBILE** se esiste $g: B \to A$ tale che:
$$ g \circ g = \text{id}_B \quad \text{e} \quad g \circ g = \text{id}_A $$

**ALLORA**: $g$ si dice **APPLICAZIONE INVERSA** di $g$.

---

### 1.2.9 Proposizione Fondamentale

$g$ **INVERTIBILE** $\iff g$ **BIETTIVA**

e si ha: $g = g^{-1}$

---

## 1.3 Strutture Algebriche

### 1.3.1 Operazioni Binarie

Siano $A, B, C \ne \emptyset$. Un'**operazione binaria** è una applicazione:
$ \perp: A \times B \to C $

---

### 1.3.2 Operazioni Interne ed Esterne

*N.B.:*

I) Se $A = B = C$, $\perp$ si dice **INTERNA**.

II) Se $B = C$, $\perp$ si dice **ESTERNA** con operatore in $A$.

---

### 1.3.3 Leggi di Composizione Interna

Sia $A \neq \emptyset$, e sia $\perp : A \times A \longrightarrow A$ una legge di composizione interna su $A$. Allora $\perp$ ha le seguenti proprietà:

1. $\perp$ è **associativa**, ossia:
$ \forall \space  x, x', x'' \in A, \quad (x \perp x') \perp x'' = x \perp (x' \perp x'') $

2. $\perp$ è **commutativa**, ossia:
$ \forall \space  x, x' \in A, \quad x \perp x' = x' \perp x $

3. $\perp$ ammette **elemento neutro** $\mu \in A$, ossia:
$ \forall \space  x \in A, \quad x \perp \mu = \mu \perp x = x $

4. Se $\perp$ ammette elemento neutro, allora:
$ \forall \space  x \in A, \exists \space  \overline{x} \in A : x \perp \overline{x} = \overline{x} \perp x = \mu \quad \text{(ovvero esiste l'inverso per ogni elemento)} $

---

### 1.3.4 Proposizioni sulle Operazioni Binarie

**PROPOSIZIONE:**

Sia $\perp : A \times A \longrightarrow A$.

(1) Se $\perp$ ha elemento neutro $\mu \in A \Rightarrow \mu$ **unico**.

(2) Se $\perp$ ha elemento neutro $\mu$ ed è associativa:

(a) Se $x \in A$ ammette inverso $\overline{x} \in A \Rightarrow \overline{x}$ **unico**.

(b) Se $x, x' \in A$ ammettono inverso $\overline{x}, \overline{x'} \in A \Rightarrow x \perp x'$ **invertibile** e il suo inverso è: $\overline{x'} \perp \overline{x}$.

---

### 1.3.5 Dimostrazioni

#### Dimostrazione di (1): Unicità dell'elemento neutro

Siano $\mu$ e $\nu$ elementi neutri di $\perp \Rightarrow$
$ \forall \space  x \in A, \quad x \perp \mu = \mu \perp x = x \quad \text{e} \quad x \perp \nu = \nu \perp x = x $

Sostituiamo $x$ con $\nu$ nella prima uguaglianza:
$ \nu \perp \mu = \mu \perp \nu = \nu $

Sostituiamo $x$ con $\mu$ nella seconda uguaglianza:
$ \mu \perp \nu = \nu \perp \mu = \mu $

Quindi: $\nu = \mu$.

---

#### Dimostrazione di (2a): Unicità dell'inverso

Siano $\overline{x}$ e $\overline{\overline{x}}$ inversi di $x$:

- $\overline{x} \perp x = x \perp \overline{x} = \mu \Rightarrow \overline{x} = \overline{x} \perp \mu = \overline{x} \perp (x \perp \overline{x}) = (\overline{x} \perp x) \perp \overline{x} = \mu \perp \overline{x} = \overline{x} \Rightarrow \overline{x} = \overline{\overline{x}}$

---

#### Dimostrazione di (2b): Invertibilità del prodotto

- $x \perp \overline{x} = \overline{x} \perp x = \mu$
- $x' \perp \overline{x'} = \overline{x'} \perp x' = \mu$

**Teorema**: $(\overline{x} \perp \overline{x'}) = \overline{x'} \perp \overline{x}$

$\begin{align*}
(\overline{x} \perp \overline{x'}) \perp (\overline{x'} \perp \overline{x}) &= \overline{x} \perp (\overline{x'} \perp \overline{x}) \perp \overline{x'} \\
&= \overline{x} \perp (\overline{x'} \perp \overline{x}) \perp \overline{x'} \\
&= \overline{x} \perp \mu = \mu
\end{align*}$

$\begin{align*}
(\overline{x'} \perp \overline{x}) \perp (\overline{x} \perp \overline{x'}) &= \overline{x'} \perp (\overline{x} \perp \overline{x'}) \perp \overline{x} \\
&= \overline{x'} \perp (\overline{x} \perp \overline{x'}) \perp \overline{x} \\
&= \overline{x'} \perp \mu = \mu
\end{align*}$

Quindi: $\overline{x'} \perp \overline{x} = \mu \Rightarrow \overline{x'} \perp \overline{x} = \mu$

---

### 1.3.6 Strutture Algebriche Fondamentali

**Def**: Una Struttura algebrica è una coppia ordinata formata da un insieme $A$, detto sostegno, e una operazione $\perp : (A, \perp)$.

**Def**: Una struttura algebrica è detta **GRUPPO** se l'operazione $\perp$ gode delle proprietà **associativa** e inoltre ammette sia elemento **NEUTRO** sia elemento **INVERTIBILE**.

**Def**: Un gruppo è detto **ABELIANO** se l'operazione $\perp$ gode anche della proprietà **commutativa**.

**Esempi**:
1) $(\mathbb{N}, +)$: Ass., ma non è un gruppo.
2) $(\mathbb{N}, \cdot)$: Ass., Comm., elemento neutro 1, ma non è un gruppo.
3) $(\mathbb{Z}, +)$: Gruppo Abeliano.

---

### 1.3.7 Anelli

$A \neq \emptyset$, $+ : A \times A \longrightarrow A$
$\cdot : A \times A \longrightarrow A$

- $(A, +, \cdot)$ si dice **ANELLO**, se e solo se:
 I) $(A, +)$ è un **GRUPPO ABELIANO**
 II) $(A, \cdot)$ è un **SEMIGRUPPO**, ossia: $\cdot$ **ASSOCIATIVA**

**Def**: $(A, +, \cdot)$ è un **ANELLO COMMUTATIVO**, se:
→ $(A, \cdot)$ gode della proprietà **COMMUTATIVA**

**Def**: $(A, +, \cdot)$ è un **ANELLO UNITARIO**, se:
→ $(A, \cdot)$ ammette elemento neutro.

---

### 1.3.8 Campi

$K \neq \emptyset$, $+ : K \times K \longrightarrow K$
$\cdot : K \times K \longrightarrow K$

- $(K, +, \cdot)$ si dice **CAMPO**, se è un **ANELLO COMMUTATIVO UNITARIO** e se ogni elemento diverso da 0 è **INVERTIBILE**.

→ Dunque:
- $(K, +)$ è un **GRUPPO ABELIANO**
- $(K \setminus \{0\}, \cdot)$ è un **GRUPPO ABELIANO**

e $\forall \space  a, b, c \in K$:
1. $a(b + c) = ab + ac$
2. $(a + b)c = ac + bc$

---

> **📌 Nota di Fine Capitolo**: Questo capitolo è **completamente riorganizzato** secondo lo schema richiesto. Tutte le sezioni originali relative a Teoria degli Insiemi, Relazioni, Applicazioni e Strutture Algebriche sono state incluse e organizzate gerarchicamente. **Nessun contenuto è stato modificato, riscritto o eliminato.**
>
> **Attendo la tua conferma esplicita per procedere con il Capitolo 2.**