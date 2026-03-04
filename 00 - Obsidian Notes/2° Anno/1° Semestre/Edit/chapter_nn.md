# Esercizi d'esame


In questo capitolo sono riportati alcuni esercizi d'esame, con le relative soluzioni, che possono essere utili per la preparazione dell'esame di Edit tenuto dal professore A. De Luca per l'anno2024/2025.

Il capitolo sarà suddiviso in due sezioni: la prima conterrà gli esercizi d'esame relativi alla prima parte del corso, argomento di intercorso, mentre la seconda conterrà gli esercizi d'esame relativi alla seconda parte del corso, argomento di fine corso.

## Esercizi d'esame di intercorso


### 2 Luglio 2018


#### Esercizio 4


Sia $g(x)$ la somma di tutti i numeri naturali $n\leq x$ tali che $n$ è un numero primo o $n$ è un numero pari. Mostrare che $g$ è una **funzione ricorsiva primitiva**.

**Soluzione:** Possiamo definire $g(x)$ come segue:

$$
    g(x) = \sum_{n=0}^{x} n(Primo(n) \lor 2\vert n)
$$


Essendo $g$ composizione di **funzioni ricorsive primitive** con **l'operatore di sommatoria**, $g$ è **ricorsiva primitiva**.

#### Esercizio 5


Sia $B=\{(x_1, \cdots, x_m) \in \mathbb{N}^m \vert g(x_1, \cdots, x_m)\downarrow\}$, dove $g$ è una funzione **parzialmente calcolabile**.

Mostrare che $B'=\{[x_1, \cdots, x_m] \in \mathbb{N}\vert (x_1, \cdots, x_m) \in B\}$ è ricorsivamente enumerabile.

**Soluzione:** $B'$ è ricorsivamente enumerabile $\iff \exists g'$ parzialmente calcolabile $: g'(x) \downarrow \iff x \in B'$.

Consideriamo allora il seguente programma $\mathcal{P}$:

```ini
[A] IF (X=0 \lor Lt(x) > m) GOTO A
    Z1 <- (X)_1
    \vdots
    Zm <- (X)_m
    Y <- g(Z1, \(\cdots\), Zm)
```


Questo programma termina $\iff x \in B'$. Dunque con $g'=\Psi_{\mathcal{P}}^{(1)}$ abbiamo la tesi.

#### Esercizio 6


Mostrare che non esiste nessuna funzione calcolabile $f(x)$ tale che $f(x)=0 \iff x \in W_x$.

**Soluzione:** $x \in W_x \iff \Phi(x,x) \downarrow \iff *HALT*(x,x)$. Supponiamo per assurdo che esista una $f(x)$ calcolabile. Allora potremmo usarla come macro in un programma.

Ma il seguente programma calcolerebbe $*HALT*(x,x)$, che porta ad assurdo:

```ini
IF f(X)!=0 GOTO E
Y <- Y + 1
```


### 20 Giugno 2019


#### Esercizio 4


Sia:
$$
    P(x,y)=\begin{cases}
    1 & x \text{esistono almeno } y \text{ numeri naturali } n \text{ tali che } n\leq x \text{ e } n \text { è quadrato perfetto}\\
    0 & \text{altrimenti}
    \end{cases}
$$


Mostrare che $P(x,y)$ è una predicato ricorsiva primitiva.

**Soluzione:** Possiamo definire $P(x,y)$ come segue:

$$
    P(x,y) = y \geq \sum_{n=0}^{x} \exists t \leq n (t^2=n)
$$


Essendo $g$ composizione di **funzioni ricorsive primitive** con **l'operatore di sommatoria** e di **quantificazione esistenziale limitata**, $g$ è **ricorsiva primitiva**.

#### Esercizio 5


Sia $f(x)>x^2 \iff x \notin \overline{K}$. Mostrare che $f$ non è calcoalbile.

**Soluzione:** $f(x)>x^2 \iff x \notin \overline{K} \iff x \in K \iff Phi(x,x) \downarrow \iff *HALT*(x,x)$. Supponiamo ora per assurdo che $f$ sia calcolabile. Allora potremmo usarla come macro in un programma.

Ma il seguente programma calcolerebbe $*HALT*(x,x)$, che porta a assurdo:

```ini
IF f(X) \leq X^2 GOTO E
Y <- Y + 1
```


#### Esercizio 6


Sia $R=\{<r_1,r_2> \vert r_1 \in W_{(r_1+r_2)}\}$. Mostrare che $R$ è ricorsivamente enumerabile.

**Soluzione:** Dalla definizione di $W_n$ abbiamo che

$$
    R=\{<r_1,r_2> \vert r_1 \in W_{(r_1+r_2)} \iff \Phi(r_1,r_1+r_2) \downarrow\}={n \in \mathbb{N} \vert \Phi(l(n), l(n) + r(n)) \downarrow}
$$


Essendo composizione di parizalmente calcolabili, $R$ è ricorsivmane enumerabile

### 17 Luglio 2019


#### Esercizio 4


Sia $A = \{(x_1, x_2) \vert f(x_1, x_2) \downarrow\}$ con $f$ funzione parzialmente calcolabile. Mostrare che $B=\{<x_1, x_2> \vert (x_1, x_2) \in A\}$ è ricorsivamente enumerabile.

**Soluzione:** $B$ è ricorsivamente enumerabile $\iff \exists g$ parzialmente calcolabile $: g(x) \downarrow \iff x \in B$.

Consideriamo allora il seguente programma $\mathcal{P}$:

```ini
Z1 <- l(X)
Z2 <- r(X)
Y <- f(Z1, Z2)
```


Questo programma termina $\iff x \in B$. Dunque con $g=\Psi_{\mathcal{P}}^{(1)}$ abbiamo la tesi.

#### Esercizio 5


Sia $c$ una costante e sia $f(x)$ il più grande numero naturale $y \leq x$ che è multiplo di $c$. Mostrare che $f$ è ricorsiva primitiva.

**Soluzione:** Possiamo definire $f(x)$ come segue:

$$
    f(x) =\begin{cases}
    x \dot{-} \min_{t \leq x} (c \vert (x\dot{-} t)), & \exists t \leq x: c\vert (x\cdot t)\\
    0, \text{altrimenti}
    \end{cases}
$$


Essendo che $0$ è multiplo di ogni numero, in caso non venga trovato alcun multiplo di $c$ è corretto che la minimalizzazione restituisca $0$.

#### Esercizio 6


Sia $f(x)$ una funzione che soddisfa la condizione:
$$
    f(x) \downarrow \iff l(x) \notin W_{r(x)}
$$


$f$ è parzialmente calcolabile? Dimostrare o confutare.

**Soluzione: ** Sia $f(x)$ parizlamente calcoalbile, allora $\exists p \in \mathbb{N}: \forall x \in \mathbb{N} :\Psi_{\mathcal{P}_p}^{(1)}(x)=f(x)$.

Sapendo che anche la funzione $\Phi(l(x), r(x))$ è parzialmente calcolabile sia $q$ il numero del programma che la calcola.

Vediamo ora che il seguente programma calcola $*HALT*(x,q)$:

```ini
[B] IF STP(X,p,Z) GOTO E
    IF STP(X,q,Z) GOTO A
    Z <- Z + 1
    GOTO B
[A] Y <- Y + 1
```


Il programma termina necessariamente poichè, $\forall x \in \mathbb{N}, l(x) \in W_{r(x)} \lor l(x) \notin W_{r(x)}$.

### 20 Gennaio 2020


#### Esercizio 4


Sia $\omega(n)$ il numero di fattori primi distinti di un numero naturale $n$ con $\omega(1)=0$ e $\omega(0)=0$. Mostrare che $\omega$ è ricorsiva primitiva.

**Soluzione:** Possiamo definire $\omega(n)$ come segue:

$$
    \omega(n) = \sum_{i=0}^{n} Primo(i) \land i\vert n
$$


Essendo $g$ composizione di **funzioni ricorsive primitive** con **l'operatore di sommatoria** $g$ è ricorsivamente enumerabile.

#### Esercizio 5


Sia $f$ una funzione ricorsiva primitiva, e

$$
    B=\{1+\sum_{i=0}^{x} f(i) \vert x \in \mathbb{N}\}
$$


Dimostrare che $B$ è ricorsivamente enumerabile.

**Soluzione: ** $B$ è ricorsivamente enumerabile $\iff \exists f'$ ricorsiva primitiva $: B=\{f'(x) \vert x \in \mathbb{N}\}$.

Ma essendo $f'(x)=1+\sum_{i=0}^{x} f(i)$ composizione di funzioni ricorsive primitive con l'operatore di sommatoria è anch'essa ricorsiva primitiva.

#### Esercizio 6


Sia $H=\{<x,y> \vert x \in W_{2y}\}$. L'insieme H è ricorsivamente enumerabile? Dimostrare o Confutare.

**Soluzione: ** $H=\{z \in \mathbb{N} \vert l(z) \in W_{2r(z)} \iff \Phi(l(z), 2r(z)) \downarrow\}$. Essendo composizione di parzialmente calcolabili, $H$ è ricorsivamente enumerabile.

---


### 18 Febbraio 2020


#### Esercizio 2


Sia $A$ un insieme ricorsivo primitivo e sia $B=\{<z_1,z_2> \vert z_1 \in A \land z_2 \notin A\}$. Mostrare che $B$ è un insieme ricorsivo.

**Soluzione 1: ** Scriviamo $B$ come segue:

$$
    B=\{x \in \mathbb{N} \vert f_A(l(x)) \land \neq f_A(r(x))\}
$$


Essendo $A$ ricorsivo primitivo, $f_A$ è ricorsiva primitiva. Ma allora $B$ è ricorsivo primitivo, poichè composizione di funzioni ricorsive primitive con l'operatore di congiunzione.

**Soluzione 2: ** $B$ è ricorsivo $\iff B \land \overline{B}$ sono ricorsivamente enumerabili.

- **$B$:** Possiamo riscrivere $B$ come:
$$
    B=\{x \in \mathbb{N} \vert l(x) \in A \land r(x) \in \overline{A}\}
$$

Essendo $A$ ricorsivo, $A$ e $\overline{A}$ sono ricorsivamente enumerabili, dunque esistono due funzioni parzialmente calcolabili $f$ e $f'$ a loro associate. Possiamo dunque riscrivere $B$ come:
$$
    B=\{x \in \mathbb{N} \vert f(l(x)) \land f'(r(x))\}
$$

Questa funzione è parzialmente calcolabile, poichè calcolata dal seguente programma:
```ini
    Z1 <- l(X)
    Z2 <- r(X)
    Z3 <- f(Z1)
    Z4 <- f'(Z2)
```

- **$\overline{B}$:** Possiamo riscrivere $\overline{B}$ usando le leggi di De Morgan come:
$$
    B=\{x \in \mathbb{N} \vert l(x) \notin A \lor r(x) \notin \overline{A}\}=\{x \in \mathbb{N} \vert l(x) \in \overline{A} \lor r(x) \in A\}
$$

Essendo $A$ ricorsivo, $A$ e $\overline{A}$ sono ricorsivamente enumerabili, dunque esistono due funzioni parzialmente calcolabili $f$ e $f'$ a loro associate. Possiamo dunque riscrivere $B$ come:
$$
    B=\{x \in \mathbb{N} \vert f'(l(x)) \lor f(r(x))\}
$$

Siano $p,q$ rispettivamente i numeri dei programmi che calcolano $f,f'$. Questa funzione è parzialmente calcolabile, poichè calcolata dal seguente programma:
```ini
    Z1 <- l(X)
    Z2 <- r(X)
[B] IF STP(Z1,q,Z3) GOTO E
    IF STP(Z2,p,Z3) GOTO E
    Z3 <- Z3 + 1
    GOTO B
```


#### Esercizio 3


Sia:
$$
    f(x) = \begin{cases}
    1, & x \text{ è dispari e } x \in \overline{K}\\
    x, & x \text{ è pari e } x \in \overline{K}\\
    \uparrow, \text{altrimenti}
    \end{cases}
$$


La funzione $f$ è calcolabile? Dimostrare o confutare.

**Soluzione: ** sia $f$ calcolabile e $p$ il numero di programma che la calcola. Allora abbiamo:

$$
    \forall x &\in \mathbb{N}:\\
    &\Psi_{\mathcal{P}_p}^{(1)}(x) = f(x) \uparrow \iff x \in K \iff \Phi(x,x) \downarrow \iff \Psi_{\mathcal{P}_x}^{(1)}(x) \downarrow
$$


In particolare però per $x=p$ abbiamo che $\Psi_{\mathcal{P}_p}^{(1)}(p) \uparrow \iff \Psi_{\mathcal{P}_p}^{(1)}(p)  \downarrow$, che porta a contraddizione.

#### Esercizio 6


Sia $M_n=2^n -1$ per ogni $n \in \mathbb{N}$, e sia $g(x)$ la somma di tutti gli $M_n$ che siano numeri primi tali che $n \leq x$. Mostrare che $g$ è ricorsiva primitiva.

**Soluzione: ** Essendo che $M_n=<n,0>$ è ricorsivamente primitiva. Possiamo definire $g(x)$ come segue:

$$
    g(x) = \sum_{n=0}^{x} M_n \cdot Primo(M_n)
$$


Essendo $g$ composizione di **funzioni ricorsive primitive** con **l'operatore di sommatoria**, $g$ è **ricorsiva primitiva**.

### 23 Giugno 2020


#### Esercizio Moodle 1


Dimostrare che l'insieme $S=\{<x,y> \vert *HALT*(y,x)\}$ è ricorsivamente enumerabile.

**Soluzione: ** $S=\{<x,y> \vert *HALT*(y,x)\}=\{<x,y> \vert \Phi(y,x) \downarrow\}= \{z \in \mathbb{N} \vert \Phi(r(z), l(z)) \downarrow\}$. Essendo composizione di parzialmente calcolabili, $S$ è ricorsivamente enumerabile.

### 16 Ottobre 2020


#### Esercizio Moodle (?)


Qual è il predicato $p(x,z)$ che rende l'insieme $B=\{x \vert \exists z \in \mathbb{N}: p(x,z)\}$ ricorsivamente enumerabile ma non ricorsivo?

**Soluzione: ** $p=STP(x,x,z)$

### 22 Giugno 2021


#### Esercizio 4


Per ogni $n \in \mathbb{N}$ sia $f(n)$ il numero di coppie di numeri primi $(p,q)$ tali che $p\leq q \land n=p+q$. Ad esempio $f(3)=0$ e $f(10)=2$ poichè $10=3+7=5+5$. Mostrare che $f$ è ricorsiva primitiva.

**Soluzione: ** Possiamo definire $f(n)$ come segue:

$$
    f(n) = \sum_{q=0}^{n} Primo(q) \cdot \exists p \leq q (Primo(p) \land n=p+q)
$$


Essendo $f$ composizione di **funzioni ricorsive primitive** con **l'operatore di sommatoria** e di **quantificazione esistenziale limitata**, $f$ è **ricorsiva primitiva**.

Un modo alternativo per scrivere $f(n)$ è:

$$
    f(n) = \sum_{q=0}^{n} [Primo(q) \cdot \sum_{p=0}^q (Primo(p) \land n=p+q)]
$$


#### Esercizio 5


Sia $g$ la funzione parziale binaria definita come segue:
$$
    g(x_1, x_2) = \begin{cases}
    \langle x_1,x_2 \rangle, & \exists z \in \mathbb{N}: STP(x_1,x_2,z)\\
    \uparrow, & \text{altrimenti}
    \end{cases}
$$


La funzione $g$ è parzialmente calcolabile? Dimostrare o confutare.

**Soluzione: ** Possiamo riscrivere $\exists z \in \mathbb{N}: STP(x_1,x_2,z) \iff \Phi(x_1,x_2)\downarrow$. Quindi la funzione $f$ è calcolata dal seguente programma:

```ini
  Z <- \Phi(X_1,X_2)
  Y <- \abrakets{X_1,X_2}
```


#### Esercizio 6


Mostrare che l'insieme $K_p=\{p \in \mathbb{N} \vert Primo(p) \land *HALT*(p,p) \}$ è ricorsivamente enumerabile.

**Soluzione: ** $K_p=\{p \in \mathbb{N} \vert Primo(p) \land *HALT*(p,p) \}=\{p \in \mathbb{N} \vert Primo(p) \land \Phi(p,p) \downarrow\}$. Tale funzione è calcolata dal seguente programma:

```ini
[A] IF \neg Primo(X) GOTO A
  Z <- \Phi(X,X)
```


**Soluzione 2: ** $K_p=K \cap P$ dove $P$ è l'insieme dei numeri primi, ricorsivamente enumerabile essendo $Primo$ ricorsivamente enumerabile.

### 20 Luglio 2021


#### Esercizio 4


Sia $B\subseteq \mathbb{N}$ ricorsivo primitivo e $C=\{(x,y) \vert f(x,y) \in B\}$ dove $f$ è una funzione ricorsiva primitiva. Mostrare che $C$ è ricorsivo primitivo.

**Soluzione: ** Essendo $B$ ricorsivo primitivo, $f_B$ è ricorsiva primitiva. Allora possiamo dire che:
$$
    f_C=f_B(f(x,y))
$$


Essendo $f_C$ composizione di funzioni ricorsive primitive, $f_C$ è ricorsiva primitiva, dunque $C$ è ricorsivo primitivo.

#### Esercizio 5


Sia $D\subseteq \mathbb{N}$ un insieme non ricorsivo, e sia $g$ una funzione totale unaria tale che $x \vert g(x) \iff x \in D$. Mostrare che $g$ non è calcolabile.

**Soluzione: ** Supponiamo per assurdo che $g$ sia calcolabile. Allora $f_D=x\vert g(x)$ è calcolabile, ma $D$ non è ricorsivo, ciò porta a contraddizione.

#### Esercizio 6


Sia $h$ una funzione unaria parzialmente calcolabile. Dimostrare che è ricorsivamente enumerabile l'insieme:
$$
    H=\{x \in \mathbb{N} \vert h(x) \downarrow \land h(x) \in W_x\}
$$


**Soluzione: ** $H=\{x \in \mathbb{N} \vert h(x) \downarrow \land h(x) \in W_x\}=\{x \in \mathbb{N} \vert \Phi(h(x),x) \downarrow\}$. Essendo composizione di parzialmente calcolabili, $H$ è ricorsivamente enumerabile.

### 19 Gennaio 2021


#### Esercizio Moodle 2


Sia $f(x,y)$ il più piccolo intero $n>x$ che sia multiplo di $y+1$. Mostrare che $f$ è ricorsiva primitiva.

**Soluzione: ** Possiamo definire $f(x,y)$ come segue:

$$
    f(x,y)= \min_{n\leq x(y+1)} ( (y+1) \vert n \land n > x)
$$


### 16 Marzo 2022


#### Esercizio 4


Sia $B\subseteq \mathbb{N}$ un insieme ricorsivo primitivo, e $Q$ il predicato definito da

$$
    Q(x) \iff \text{ tutti i divisori di } x+1 \text{ appartengono a } B
$$


Mostrare che $Q$ è ricorsivo primitivo.

**Soluzione: ** Possiamo definire $Q(x)$ come segue:

$$
    Q(x) = \forall n \leq x+1 (\neg (n \vert (x+1)) \lor f_B(n))
$$


Essendo $Q$ composizione di **funzioni ricorsive primitive** con **l'operatore di quantificazione universale limitata** e di **congiunzione**, $Q$ è **ricorsiva primitiva**.

#### Esercizio 5


La funzione $f$ definita da
$$
    f(x) = \begin{cases}
    x+1, & \neg(\exists z : STP(x,x,z))\\
    \uparrow, & \text{altrimenti}
    \end{cases}
$$


è parzilmente calcolabile? Dimostrare o confutare.

**Soluzione: ** Possiamo riscrivere $\neg(\exists z : STP(x,x,z)) \iff \Phi(x,x) \uparrow$.

Sia per assurdo $f$ parzialmente calcolabile. Sia $p$ il numero del programma che la calcola. Allora abbiamo:

$$
    \forall x &\in \mathbb{N}:\\
    &\Psi_{\mathcal{P}_p}^{(1)}(x) = f(x) \uparrow \iff \Phi(x,x) \downarrow \iff \Psi_{\mathcal{P}_x}^{(1)}(x) \downarrow
$$


Per $x=p$ andiamo a contraddizione.

#### Esercizio 6


Mostrare che l'insieme $S=\{[i,j,k] \vert *HALT*(i,k) \land *HALT*(j,k)\}$ è ricorsivamente enumerabile.

**Soluzione: ** Riscriviamo l'insieme come segue:

$$
    S=\{z \in \mathbb{N} \vert HALT({(z)}_1, {(z)}_3) \land HALT({(z)}_2, {(z)}_3)\}=\{z \in \mathbb{N} \vert \Phi({(z)}_1, {(z)}_3) \downarrow \land \Phi({(z)}_2, {(z)}_3) \downarrow\}
$$


La funzione che descrive $S$ non è automaticamente parzialmente calcolabile poichè le funzioni parzialmente calcolabili non sono chiuse rispetto a $\land$.
Consideriamo dunque il programma seguente:

```ini
[A] IF (X == 0 \lor Lt(x) > 3) GOTO A
    Z1 <- \Phi((X)_1, (X)_3)
    Z2 <- \Phi((X)_2, (X)_3)
```


Questo programma termina se e solo se $x \in S$. Dunque $S$ è ricorsivamente enumerabile.

### 07 Aprile 2022


#### Esercizio 4


Per $x,y \in \mathbb{N}$, sia $f(x,y)$ il più piccolo multiplo di $y+1$ che sia maggiore di $x$. Mostrare che la funzione $f$ è ricorsiva primitiva.

**Soluzione: ** Possiamo definire $f(x,y)$ come segue:

$$
    f(x,y) = \min_{n\leq x(y+1)} ( ((y+1) \vert n) \land n > x)
$$


Essendo $f$ composizione di **funzioni ricorsive primitive** con **l'operatore di quantificazione universale limitata** e di **congiunzione**, $f$ è **ricorsiva primitiva**.

#### Esercizio 5


Dimostrare o confutare: la funzione $g$ definita da

$$
    g(x_1,x_2) = \begin{cases}
    0, \mathit{HALT}(x_1,x_2) \lor x_1 \in K\\
    \uparrow, \text{altrimenti}
    \end{cases}
$$


è parzialmente calcolabile?

**Soluzione: ** Possiamo riscrivere $g(x_1,x_2)$ come segue:

$$
    g(x_1,x_2) = \begin{cases}
    0, \Phi(x_1,x_2) \downarrow \lor \Phi(x_1,x_1) \downarrow\\
    \uparrow, \text{altrimenti}
    \end{cases}
$$


Allora $g$ è calcolata dal seguente programma:

```ini
[A] IF STP(X1,X2,Z) GOTO E
    IF STP(X1,X1,Z) GOTO E
    Z <- Z + 1
    GOTO A
```


#### Esercizio 6


Sia $B \subseteq \mathbb{N}$ un insieme ricorsivo. Mostrare che l'insieme

$$
    C = \{\langle m,n \rangle \vert \Phi(m,n) \downarrow \land \Phi(m,n) \notin B\}
$$


è ricorsivamente enumerabile?

**Soluzione: ** $C=\{\langle m,n \rangle \vert \Phi(m,n) \downarrow \land \Phi(m,n) \notin B\}=\{ z \in \mathbb{N} \vert \Phi(l(z),r(z)) \downarrow \land \Phi(l(z),r(z)) \notin B\}$.

Allora il seguente programma termina solo su input appartenti a $C$:

```ini
    Z <- \Phi(l(X),r(X))
[A] IF f_B(Z) GOTO A
```


### 20 Luglio 2022


#### Esercizio 4


Per $x,y \in \mathbb{N}$, sia $P(x,y)$ vero se e solo se $x$ è maggiore del più grande divisore primo di $y+1$. Mostrare che $P$ è ricorsivo primitivo.

**Soluzione: ** Possiamo definire $P(x,y)$ come segue:

$$
    P(x,y) = \max_{n \leq y+1} (Primo(n) \land n \vert (y+1)) < x
$$

oppure come:
$$
    P(x,y) = P_{Lt(y+1)}< x
$$


Essendo $P$ composizione di **funzioni ricorsive primitive** con **l'operatore di quantificazione universale limitata** e di **congiunzione**, $P$ è **ricorsiva primitiva**.

#### Esercizio 5


Dimostrare o confutare: la funzione $g$ definita da

$$
    g(x_1,x_2) = \begin{cases}
    0, &x_2 \in K \lor \Phi(x_1, x_2) \downarrow\\
    \uparrow, &\text{altrimenti}
    \end{cases}
$$


è parzialmente calcolabile?

**Soluzione: ** Possiamo riscrivere $g(x_1,x_2)$ come segue:

$$
    g(x_1,x_2) = \begin{cases}
    0, &\Phi(x_2,x_2) \downarrow \lor \Phi(x_1, x_2) \downarrow\\
    \uparrow, &\text{altrimenti}
    \end{cases}
$$


Allora $g$ è calcolata dal seguente programma:

```ini
[A] IF STP(X2,X2,Z) GOTO E
    IF STP(X1,X2,Z) GOTO E
    Z <- Z + 1
    GOTO A
```


---

#### Esercizio 6


Mostrare che l'insieme $C=\{\langle m,n \rangle \vert \Phi(m,n) \uparrow\}$ non è ricorsivamente enumerabile.

**Soluzione: ** Supponiamo per assurdo che $C$ sia ricorsivamente enumerabile.

Riscriviamo dunque $C$ come segue:

$$
    C=\{\langle m,n \rangle \vert \Phi(m,n) \uparrow\}=\{z \in \mathbb{N} \vert \Phi(l(z),r(z)) \uparrow\}
$$


Ma allora la funzione $f$ che termina solo su input $z \in C$ termina se e solo se $\Phi(l(z),r(z)) \uparrow$. Sia $p$ il numero del programma che calcola $f$. Allora abbiamo:

```ini
[A] IF STP(X,p,Z) GOTO E
    IF STP(l(X),r(X),Z) GOTO B
    Z <- Z + 1
    GOTO A
[B] Y <- Y + 1
```


questo programma calcola $HALT(l(x), r(x))$. Il che porta a contraddizione.

**Soluzione 2: ** Sia $C$ ricorsivamente enumerabile. Consideriamo l'isieme $B=\{z \in \mathbb{N} \vert l(z) = r(z)\}$. Questo insieme è chiaramente ricorsivo primitivo.

Ma allora $C \cap B$ è ricorsivamente enumerabile. Ma se vediamo che $C=\{z \vert l(z) \in \overline{W_{r(z)}}\}$ abbiamo che:

$$
    A = C \cap B = \{z \vert l(z) \in \overline{W_{r(z)}} \land l(z) = r(z)\} = \{z \vert l(z) \in \overline{K} \land r(z) \in \overline{K}\}
$$


Se questo fosse ricorsicamente enumerabile, potrei trovare una funzione parziale che termina solo su input $x \in K$. Questo porta ad assurdo.

### 13 Settembre 2022


#### Esercizio 4


Sia $A = \{\langle x,y \rangle \vert Primo(x) \land Primo (y) \land |x-y|=2\}$. Dimostrare che $A$ è un insieme ricorsivo primitivo.

**Soluzione: ** Se riscriviamo $A$ come segue:

$$
    A = \{\langle x,y \rangle \vert Primo(x) \land Primo (y) \land |x-y|=2\} = \{z \vert Primo(l(z)) \land Primo (r(z)) \land |l(z)-r(z)|=2\}
$$


Abbiamo che la funzione caratteristica di $A$ è composta di funzioni ricorsive primitive, dunque $A$ è ricorsivo primitivo.

#### Esercizio 5


Sia $f$ una funzione ricorsiva primitiva, e $B=\{x \vert f(x) \in K\}$. Mostrare che $B$ è ricorsivamente enumerabile.

**Soluzione: ** $B=\{x \vert f(x) \in K\}=\{x \vert \Phi(f(x),f(x)) \downarrow\}$. Essendo composizione di parzialmente calcolabili, $B$ è ricorsivamente enumerabile.

#### Esercizio 6


Sia
$$
    g(x)=\begin{cases}
    x+1, & \exists z \in \mathbb{N}: STP(x,x,z)\\
    0, &\text{altrimenti}
    \end{cases}
$$


$g$ è una funzione calcolabile? Dimostrare o confutare.

**Soluzione: ** Supponiamo per assurdo che $g$ sia calcolabile. Allora il seguente programma calcola $HALT(x,x)$:

```ini
  IF (g(x) != x + 1) GOTO E
  Y <- Y + 1
```


Alternativamente si può vedere come $HALT(x,x) = \alpha\alpha(g(x))$. Altra contraddizione.

### 20 Gennaio 2023


#### Esercizio 4


Per $n\in \mathbb{N}$, sia $f(n)$ il prodotto dei numeri primi minori o uguali a $n$ (con $f(0)=f(1)=0$). Mostrare che $f$ è ricorsiva primitiva.

**Soluzione: ** Possiamo definire $f(n)$ come segue:

$$
    f(n) = \prod_{i=0}^{n} (i \cdot Primo(i) +  (\neg Primo(i)))
$$


#### Esercizio 5


Dimostrare che se $S \subseteq \mathbb{N}$ è un insieme finito, allora $\overline{K} \cup S$ non è ricorsivamente enumerabile.

**Soluzione: ** Supponiamo per assurdo che $\overline{K} \cup S$ sia ricorsivamente enumerabile. Inoltre possiamo notare che $S \setminus K$ è un insieme finito, dunque è ricorsivo. Ma allora si ha che:

$$
    ((\overline{K} \cup S) \cap \overline{S} )\cup (S \setminus K) = \overline{K}
$$


Ciò porta a contraddizione.

#### Esercizio 6


Sia $g$ la funzione unaria tale che

$$
    g(\langle x,y \rangle) = \begin{cases}
    m+1, & \text{HALT}(x,y)\\
    \uparrow, & \text{altrimenti}
    \end{cases}
$$


per ogni $m,n \in \mathbb{N}$. Mostrare che $g$ è parzialmente calcolabile.

**Soluzione: ** Possiamo riscrivere $g$ come:

$$
    g(z)= \begin{cases}
    l(z)+1, & \Phi(l(z),r(z)) \downarrow\\
    \uparrow, & \text{altrimenti}
    \end{cases}
$$


Possiamo dunque vedere che il seguente programma calcola $g$:

```ini
  Z <- \Phi(l(X),r(X))
  Y <- l(X) + 1
```


### 03 Marzo 2023


#### Esercizio 4


Sia $f(n)$ la somma di tutti i numeri naturali con la stessa parità di $n$ fino a $n$ incluso. Mostrare che la funzione $f$ è ricorsiva primitiva.

**Soluzione: ** Possiamo definire $f(n)$ come segue:

$$
    f(n) = \sum_{i=0}^{n} (i \cdot (n \bmod 2 = i \bmod 2))
$$


#### Esercizio 5


Sia $P(x)$ un predicato calcolabile. Dimostrare che l'insieme $S_p=\{x \in \mathbb{N} \vert \exists y : y>x \land P(y)\}$ è ricorsivamente enumerabile.

**Soluzione: ** $S_p$ è ricorsivamente enumerabile $\iff \exists g$ parzialmente calcolabile $: g(x) \downarrow \iff x \in S_p$.

Tale funzione è calcolata dal seguente programma:

```ini
[A] IF (P(Z) \land  Z>X) GOTO E
    Z <- Z + 1
    GOTO A
```


#### Esercizio 6


Mostrare che non esiste una funzione calcolabile $g(x_1,x_2)$ tale che:

$$
    g(x_1,x_2) = 0 \iff \Phi(x_1,x_2) \downarrow
$$


**Soluzione: **

$$
    g(x_1,x_2) = 0 \iff \Phi(x_1,x_2) \downarrow \iff HALT(x_1,x_2)
$$


Ma allora $\alpha(g)=HALT$, dunque non calcolabile.

### 13 Giugno 2023


#### Esercizio 4


Per $n \geq 0$, sia $f(n)$ il più piccolo numero primo che non divide $n+1$. Dimostrare che $f$ è una funzione ricorsiva primitiva.

**Soluzione: ** Possiamo definire $f(n)$ come segue:

$$
    f(n) = \min_{i \leq P_{(n+1)}} (Primo(i) \land \neg (i \vert (n+1)))
$$


#### Esercizio 5


Per $m,n \in \mathbb{N}$, sia

$$
    g(m,n)=\begin{cases}
    \Phi(m,n), & m>n \land HALT(m,n)\\
    \uparrow, & \text{altrimenti}
    \end{cases}
$$


La funzione $g$ è parzialmente calcolabile? Dimostrare o confutare.

**Soluzione: ** Consideriamo il seguente programma:

```ini
    Y <- \Phi(X_1,X_2)
[A] IF (X1 <= X2) GOTO A
```


Questo programma calcola $g$.

#### Esercizio 6


Sia $C \subseteq \mathbb{N}$ un insieme ricorsivo, e sia $D=\{x \in \mathbb{N} \vert x \in W_x \setminus C\}$. Mostrare che $D$ è ricorsivamente enumerabile.

**Soluzione: ** $D=\{x \in \mathbb{N} \vert x \in W_x \cap \overline{C}\}$. In oltre $C$ ricorsivo $\iff \overline{C}$ ricorsivamente enumerabile. Allora possiamo riscrivere $D=K \cap \overline{C}$, che è ricorsivamente enumerabile.