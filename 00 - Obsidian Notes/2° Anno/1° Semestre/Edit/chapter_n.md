# Esercizi e Approfondimenti


Questo capitolo raccoglie gli esercizi assegnati **durante il corso** e i **codici** che non hanno trovato spazio fra le pagine principali di questo documento.

Questi risultati potrebbero essere utilizzati nella trattazione di alcuni argomenti venendo lasciati per scontati. In tal caso verrà fatto riferimento
in una **nota** l'esercizio di riferimento per poterlo consultare.

Si consiglia caldamente in ogni caso di provare a **svolgere autonomamente** gli esercizi prima di leggere le soluzioni fornite che, si ricorda, sono solo *una* soluzione possibile al problema dato.

## Calcolabilità e Linguaggio S


#### Approfondimento.


```ini
[A] IF X != 0 GOTO B
    GOTO C
[B] X <- X - 1
    Y <- Y + 1
    Z <- Z + 1
    GOTO A
[C] IF Z != 0 GOTO D
    GOTO E
[D] X <- X + 1
    Z <- Z - 1
    GOTO C
```


Questa implementazione della funzione identica ha il vantaggio di **preservare** il valore delle variabili d'input, buona pratica generale per l'implementazione di qualsiasi funzione.

#### Approfondimento.


```ini
    Y <- X1
    Z <- X2
[A] IF Z != 0 GOTO B
    GOTO E
[B] Z <- Z - 1
    Y <- Y + 1
    GOTO A
```


Faremo riferimento a questo programma da ora in poi con la macro `V <- V1 + V2`

---


#### Esercizio.


```ini
    Z <- X1
[A] Y <- Y + X2
    Z <- Z - 1
    IF Z != 0 GOTO A
```


Faremo riferimento a questo programma da ora in poi con la macro `V <- V1 * V2`

#### Esercizio.


```ini
Z <- Z + 1
Z <- Z + 1
Z <- Z + 1
Y <- X1 * Z
```


#### Esercizio.


$$
    p(x)= \begin{cases}
    1, \;\; x\equiv_{2}0\\
    \uparrow, \;\; altrimenti
    \end{cases}
$$


```ini
    Z1 <- Z1 + 1
    Z2 <- Z2 + 1
    Z2 <- Z2 + 1
[A] IF X != 0 GOTO B
    Y <- Y + 1
    GOTO E
[B] IF X == Z1 GOTO B
    X <- X - Z2
    GOTO A
```


#### Esercizio.


Programma*(ref: Predicato Uguaglianza)* in **linguaggio S** *``puro''*.

```ini
[A] IF X1 != 0 GOTO B
    IF X2 != 0 GOTO E
    Y <- Y + 1
    IF Y != 0 GOTO E
[B] X1 <- X1 - 1
    IF X2 != 0 GOTO C
    Z <- Z + 1
    IF Z != 0 GOTO E
[C] X2 <- X2 - 1
    Z <- Z + 1
    IF Z != 0 GOTO A
```


Input: $(x_1,x_2,x_3)=(2,1,3)$;

1. **Stato Iniziale** $\sigma_1=\{x_1=2,x_2=1,x_3=3,y=0,z=0\}$;
2. **Istantanea 1** $(1,\sigma_1)$;
3. **Istantanea 2** $(5,\sigma_1)$;
4. **Istantanea 3** $(6,\sigma_2)$, con $\sigma_2=\{x_1=1,x_2=1,x_3=3,y=0,z=0\}$;
5. **Istantanea 4** $(9,\sigma_2)$;
6. **Istantanea 5** $(10,\sigma_3)$, con $\sigma_3=\{x_1=1,x_2=0,x_3=3,y=0,z=0\}$;
7. **Istantanea 6** $(11,\sigma_4)$, con $\sigma_4=\{x_1=1,x_2=0,x_3=3,y=0,z=1\}$;
8. **Istantanea 7** $(1,\sigma_4)$;
9. **Istantanea 8** $(5,\sigma_4)$;
10. **Istantanea 9** $(6,\sigma_5)$, con $\sigma_5=\{x_1=0,x_2=0,x_3=3,y=0,z=1\}$;
11. **Istantanea 10** $(7,\sigma_5)$;
12. **Istantanea 11** $(8,\sigma_6)$, con $\sigma_6=\{x_1=0,x_2=0,x_3=3,y=0,z=2\}$;
13. **Istantanea 12** $(12,\sigma_6)$, **terminale**;
14. **Stato Finale** $\sigma_6=\{x_1=0,x_2=0,x_3=3,y=0,z=2\}$.

Input: $x_1=5$;

1. **Stato Iniziale** $\sigma_1=\{x_1=5, x_2=0,y=0,z=0\}$;
2. **Istantanea 1** $(1,\sigma_1)$;
3. **Istantanea 2** $(5,\sigma_1)$;
4. **Istantanea 3** $(6,\sigma_2)$, con $\sigma_2=\{x_1=4,x_2=0,y=0,z=0\}$;
5. **Istantanea 4** $(7,\sigma_2)$;
6. **Istantanea 5** $(8,\sigma_3)$, con $\sigma_3=\{x_1=4,x_2=0,y=0,z=1\}$;
7. **Istantanea 6** $(12,\sigma_3)$, **terminale**;
8. **Stato Finale** $\sigma_3=\{x_1=4,x_2=0,y=0,z=1\}$.

#### Esercizio


```ini
    Y <- Y + 1
[A] IF X2 != 0 GOTO B
    GOTO E
[B] X2 <- X2 - 1
    Y <- Y * X1
    GOTO A
```


#### Esercizio.


```ini
    Y <- X1
[A] IF X2 == 0 GOTO E
    Y <- Y + 1
    Y <- Y + 1
    X2 <- X2 - 1
    GOTO A
```


- $\Psi_{\mathcal{P}}^{(1)}(r_1)=r_1$;
- $\Psi_{\mathcal{P}}^{(2)}(r_1,r_2)=r_1+2r_2$;
- $\Psi_{\mathcal{P}}^{(3)}(r_1,r_2,r_3)=r_1+2r_2$.

---

#### Esercizio.


1. *$\forall k\geq0$, sia $f_k(x)=k$. Dimostrare che $f_k$ è calcolabile[^1].*

2. *Un programma è **straightline** se non contiene istruzioni di salto. Mostrare per induzione su $k$ che se $\mathcal{P}$ è **straightline** e ha lunghezza $k$ allora $\Psi_{\mathcal{P}}^{(1)}(x)\leq k, \forall x \in \mathbb{N}$.*

3. *Mostrare che se $\mathcal{P}$ è straightline e calcola $f_k$, allora $\mathcal{P}$ ha lunghezza $\geq k$.*

4. *Mostrare che nessun programma straightline calcola la funzione $f(x)=x+1$, e quindi dedurne che la classe delle funzioni calcolate dai programmi straightline è **propriamente** contenuta nella classe delle funzioni calcolabili.*

**$1$.** Dimostriamo per induzione.


**Base induttiva** $k=0$. Vero poiché $f_0(x)=0$ è calcolata dal **programma vuoto**.
**Passo induttivo** $k\to k+1$. Vero poiché $f_{k+1}(x)=k+1$ è calcolata aggiungendo al programma che calcola $f_k$, esistente per ipotesi d'induzione, l'istruzione `Y <- Y + 1`.

**$2$.** Dimostriamo per induzione.


**Base induttiva** $k=0$. Vero avremo il **programma vuoto**, dunque con output $0\leq k$

**Passo induttivo** $k\to k+1$. Vero poiché avendo per ipotesi di induzione che $\Psi_{\mathcal{P}}^{(1)}(x)\leq k$, il programma di lunghezza $k+1$, dovendo essere **straightline** dovrà avere come istruzione in più necessariamente una di queste $3$ istruzioni:
- **Pigra.** Porta a un output uguale al programma precedente, dunque $y_{k+1}=y_k\leq k \leq k+1$;
- **Decremento.** Porta a un output minore di quello precedente di $1$, dunque $y_{k+1}=y_k-1\leq y_k \leq k \leq k+1$;
- **Incremento.** Porta a un output maggiore di quello precedente di $1$, ma essendo $y_k\leq k$ allora $y_{k+1}=y_k+1\leq k+1$.

**$3$.** Dimostriamo per costruzione.


Essendo il programma **straightline** potrà avere solo istruzioni **pigre**, di **incremento** o di **decremento**.
Essendo la variabile di output `Y` inizializzata a $0$, per calcolare $f_k$ sono necessario come minimo $k$ istruzioni di incremento, dunque la lunghezza del programma sarà almeno $k$.
In caso ci siano istruzioni non di incremento la lunghezza sarà maggiore di $k$ avendo bisogno di al meno $k$ istruzioni di incremento.

**$4$.** Dimostriamo per costruzione.


Preso un programma $\mathcal{P}$ di $k$ istruzioni, se questo è **straightline** avrà come output $y\leq k$, come visto nel punto $2$. Ma la funzione $f(x)=x+1$ ha $y>k, \forall x \geq k$.
Dunque nessun programma **straightline** può calcolare la funzione $f(x)=x+1$.

#### Esercizio.


```ini
    IF X1 != X2 GOTO A
    Y <- Y + 1
    GOTO E
[A] IF X1 != 0 GOTO B
    Y <- Y + 1
    GOTO E
[B] IF X2 != 0 GOTO C
    GOTO E
[C] X1 <- X1 - 1
    X2 <- X2 - 1
    GOTO A
```


Implementazione alternativa:

```ini
[C] IF X2 != 0 GOTO A
    IF X1 != 0 GOTO B
    Y <- Y + 1
[B] GOTO E
[A] X2 <- X2 - 1
    X1 <- X1 - 1
    GOTO C
```


## Operazioni sulle funzioni e paradigma funzionale


#### Esercizio.


È possibile dimostrare che la funzione $|x-y|$ è ricorsiva primitiva mostrando che essa è composizione di funzioni iniziali. Si ha infatti che le funzioni **somma** e **differenza modificata** sono già state dimostrate essere ricorsive primitive.
Per quanto riguarda la funzione **differenza modificata** con operandi invertiti è sufficiente comporla con le funzioni proiezioni in modo da ottenere il risultato voluto, ovvero:
$$
    y\dot{-} x = d_m(y,x) = d_m(u_2^{(2)}(x,y),u_1^{(2)}(x,y)) = u_2^{(2)}(x,y) \dot{-} u_1^{(2)}(x,y)
$$

Si avrà in questo modo che la **differenza modificata** riceverà gli operandi nell'ordine per cui è stata dimostrata essere ricorsiva primitiva.
Alternativamente possiamo dividere la funzione nei casi della definizione di funzione ottenuta per ricorsione primitiva:
$$
    \begin{cases}
    |x-0|=x \dot{-} 0 + 0 \dot{-} x = x + 0 = x = u_1^{(1)}(x)\\
    |x-(t+1)|= p(|x-t|)=g(x,t,|x-t|), \forall t \in \mathbb{N}^*
    \end{cases}
    
$$

Dove $g(x,y,z)=p(u_3^{(3)}(x,y,z))$ è composizione di funzioni iniziali.

#### Esercizio.

Consideriamo il predicato dato come:
$$
    p(x,y)=\begin{cases}
    1, \;\; x\leq y\\
    0, \;\; \text{altrimenti}
    \end{cases} = \begin{cases}
    1, \;\; x\dot{-} y = 0\\
    0, \;\; \text{altrimenti}
    \end{cases} = \alpha(x\dot{-} y)
    
$$

Dunque il predicato $p$ è ricorsivo primitivo in quanto composizione di funzioni ricorsive primitive.

#### Approfondimento.


> [!theorem] Corollario al Teorema di Definizione per Casi
> **Dimostrazione. ** Dal teorema*(ref: Chiusure per congiunzione, disgiunzione e negazione Teorema)* sappiamo che tutti i *predicati composti* a partire da $p_1,\cdots,p_n$ usando i connettivi $\land,\lor,\neg$ appartengono a $\mathcal{C}$.
> Per ogni caso $i\in \{1,\cdots,k\}$ della definizione di $f$ possiamo dunque definire un predicato $p_i'$ come:
> $$
>     p_i'(x_1,\cdots,x_n)=\neg p_1 \land \cdots \land \neg p_{i-1} \land p_i
> $$

> In oltre possiamo definire il caso $(k+1)\text{-esimo}$ come:
> $$
>     p_{k+1}'(x_1,\cdots,x_n)=\neg p_1 \land \cdots \land \neg p_{n-1} \land \neg p_n
> $$

> Possiamo dunque definire la funzione $f$ come:
> $$
>     f(x_1,\cdots,x_n)=g_1(x_1,\cdots,x_n)p_1'(x_1,\cdots,x_n)+\cdots+g_k(x_1,\cdots,x_n)p_k'(x_1,\cdots,x_n)+h(x_1,\cdots,x_n)p_{k+1}'(x_1,\cdots,x_n)
> $$

> Essendo dunque $f$ composizione di **funzioni ricorsive primitive** e **funzioni appartenenti** a $\mathcal{C}$ è **ricorsiva primitiva**.


#### Esercizio

$$
    f^{(0)}(x)=x, f^{(1)}(x)=f(x),\cdots, f^{(n+1)}(x)=f(f^{(n)}(x)), \forall n \in \mathbb{N}
    
$$

*Definiamo allora la funzione $t_f$ binaria come:*
$$
    t_f(x,n)=f^{(n)}(x)
    
$$

*Mostrare che se $f \in \mathcal{C}$ **classe PRC**, allora anche $t_f\in\mathcal{C}$*

**Dimostriamo per Ricorsione Primitiva**

$$
    \begin{cases}
    t_f(x,0)=x=u_1^{(2)}(x)\\
    t_f(x,n+1)=f(t_f(x,n))=g(x,n,t_f(x,n)), \forall n \in \mathbb{N}
    \end{cases}
    
$$


Dove $g(x,y,z)=f(u_3^{(3)}(x,y,z))$ è composizione di funzioni iniziali e appartenenti a $\mathcal{C}$ e dunque ricorsiva primitiva.

#### Esercizio:


Consideriamo la funzione data come:
$$
    \pi(x)=\sum_{i=0}^x Primo(i)
    
$$


Essendo dunque la funzione $\pi(x)$ ottenuta tramite **l'operatore sommatoria** applicato a un predicato ricorsivo primitivo, essa è ricorsiva primitiva.

#### Esercizio:


Essendo $\sqrt{2}$ un numero *irrazionale* non è compreso nel dominio delle funzioni che stiamo contemplando. Dobbiamo dunque limitarlo superiormente.
$$
    n\leq\sqrt{2}x<n+1 \iff n^2\leq 2x^2<{(n+1)}^2
$$


Possiamo dunque considerare la funzione data come:
$$
    h(x)=\min_{t<2x}({(t+1)}^2> 2x^2)
    
$$


La funzione è dunque ricorsiva primitiva poiché ottenuta per **minimizzazione limitata** del predicato ricorsivo primitivo ${(t+1)}^2> 2x^2$ composizione di funzioni ricorsive primitive.

#### Esercizio:


**Dimostrazione per Ricorsione Primitiva**

Possiamo definire la funzione data per ricorsione primitiva come:

$$
    \begin{cases}
    \max_{t\leq 0}R(x,t)=g(x,0)=0\\
    \max_{t\leq y+1}R(x,t)=\max_{t\leq y}R(x,t)\cdot(\neg R(x,y+1)) + (y+1)\cdot(R(x,y+1)) = g(x,y,\max_{t\leq y}R(x,y)), \forall y \in \mathbb{N}
    \end{cases}
    
$$


Dove $g(x,y,\max_{t\leq y}R(x,y))$ è una funzione ricorsiva primitiva poiché composta di funzioni e predicati ricorsivi primitivi.

---

## Codifica di Programmi in Numeri


#### Esercizio:

Consiglio, usare funzione pairing.

Consideriamo la funzione $g$ definita come:
$$
    \begin{cases}
    g(0)=\langle  0,1  \rangle\\
    g(n+1)=\langle  r(g(n)),l(g(n))+r(g(n))  \rangle
    \end{cases}
    
$$


La funzione $g$ è ricorsiva primitiva in quanto composizione di funzioni ricorsive primitive.

Possiamo ora facilmente notare che $F(x) = l(g(x))$ è ricorsiva primitiva in quanto composizione di funzioni ricorsive primitive.

#### Esercizio

```ini
    IF X != 0 GOTO A
[A] X <- X + 1
    IF X != 0 GOTO A
    Y <- Y + 1
```


Iniziamo dalla codifica delle singole istruzioni. Avremo:
1. $\langle  0,\langle  3,1 \rangle \rangle= \langle  0,2^3(2\cdot 1 +1)-1 \rangle = \langle  0,23 \rangle = 2^0(2\cdot 23 + 1) - 1 = 46$;
2. $\langle  1,\langle  1,1 \rangle \rangle= \langle  1,2^1(2\cdot 1 +1)-1 \rangle = \langle  1,5 \rangle = 2^1(2\cdot 5 + 1) - 1 = 21$;
3. $\langle  0,\langle  3,1 \rangle \rangle= 46$;
4. $\langle  0,\langle  1,0 \rangle \rangle= \langle  0,2^1(2\cdot 0 +1)-1 \rangle = \langle  0,1 \rangle = 2^0(2\cdot 1 + 1) - 1 = 2$;
Utilizziamo ora i Numeri di Gödel per trovare $\# (\mathcal{P})$. Essendo il programma composto da $4$ istruzioni avremo:
$$
    \# (\mathcal{P}) = P_1^{\# (I_1)} + P_2^{\# (I_2)} + P_3^{\# (I_3)} + P_4^{\# (I_4)}-1= 2^{46} \cdot 3^{21} \cdot 5^{46} \cdot 7^2 - 1\approx 5.125573068 \times  10^{57}
$$


```ini
[B] IF X != 0 GOTO A
    Z <- Z + 1
    IF Z != 0 GOTO B
[A] X <- X
```


Iniziamo dalla codifica delle singole istruzioni. Avremo:
1. $\langle  2,\langle  3,1 \rangle \rangle= \langle  2,2^3(2\cdot 1 +1)-1 \rangle = \langle  2,23 \rangle = 2^2(2\cdot 23 + 1) - 1 = 187$;
2. $\langle  0,\langle  1,2 \rangle \rangle= \langle  0,2^1(2\cdot 2 +1)-1 \rangle = \langle  0,9 \rangle = 2^0(2\cdot 9 + 1) - 1 = 18$;
3. $\langle  0,\langle  4,2 \rangle \rangle= \langle  0,2^4(2\cdot 2 + 1)-1 \rangle = \langle  0,79 \rangle = 2^0(2\cdot 79 + 1)-1= 158$;
4. $\langle  1,\langle  0,1 \rangle \rangle= \langle  1,2^0(2\cdot 1 +1)-1 \rangle = \langle  1,2 \rangle = 2^1(2\cdot 2 + 1) - 1 = 9$;
Utilizziamo ora i Numeri di Gödel per trovare $\# (\mathcal{P})$. Essendo il programma composto da $4$ istruzioni avremo:
$$
    \# (\mathcal{P}) = P_1^{\# (I_1)} + P_2^{\# (I_2)} + P_3^{\# (I_3)} + P_4^{\# (I_4)} - 1= 2^{187} \cdot 3^{18} \cdot 5^{158} \cdot 7^9 -1\approx 8.393340064428623004696575 \times  10^{182}
$$


#### Esercizio:


Iniziamo scomponendo in fattori primi il numero dato $+1$:
$$
    576 = 5^2 \cdot 23= 2^6 \cdot 3^2
$$

Abbiamo dunque che $Lt(576)=2$. Decodifichiamo adesso gli esponenti nelle singole istruzioni:
1.
$$
    &6 = \langle  a_1,\langle  b_1,c_1 \rangle \rangle \implies 2^{a_1}(2\langle  b_1,c_1 \rangle+1)-1=6 \implies 2^{a_1}(2\langle  b_1,c_1 \rangle+1)=7 \implies a_1=0 \land \langle  b_1,c_1 \rangle =3 \\
    &a_1 =0, 2^{b_1}(2c_1+1)=4 \implies a_1=0, b_1=2, c_1=0
$$


Abbiamo dunque l'istruzione (0,2,0) ovvero l'istruzione `Y <- Y - 1`;
2. $2 = \langle  a_1,\langle  b_1,c_1 \rangle \rangle \implies 2^{a_1}(2\langle  b_1,c_1 \rangle+1)-1=2 \implies 2^{a_1}(2\langle  b_1,c_1 \rangle+1)=3 \implies a_1=0 \land \langle  b_1,c_1 \rangle =1 \implies a_1=0, 2^{b_1}(2c_1+1)=2 \implies a_1=0, b_1=1, c_1=0$. Abbiamo dunque l'istruzione (0,1,0) ovvero l'istruzione `Y <- Y + 1`;

Abbiamo dunque che il programma $\mathcal{P}$ di numero \#$\mathcal{P}=575$ è:
```ini
    Y <- Y - 1
    Y <- Y + 1
```


#### Esercizio:


**Dimostrazione per Assurdo**

Supponiamo che $\overline{*HALT*}(x,y)$ sia calcolabile. Allora è calcolabile anche il predicato $\neg \overline{*HALT*}(x,y)$ dal teorema*(ref: Chiusure per congiunzione, disgiunzione e negazione Teorema)*. Ma si ha che:
$$
    \neg \overline{\mathit{HALT}}(x,y) \iff \mathit{HALT}(x,y)
$$


Ma dal teorema*(ref: Problema della Fermata)* sappiamo che $*HALT*(x,y)$ non è calcolabile. Assurdo.


#### Esercizio:

*Dimostrare o Confutare: ``Se $f$ è una funzione $n\text{-aria}$ totale per la quale esiste $k\in\mathbb{N}$ tale che $f(x_1,\cdots,x_n)\leq k$ per ogni $n$-upla $(x_1,\cdots,x_n)$, allora $f$ è calcolabil''.*

**Confutazione per controesempio.**

È sufficiente notare che il **predicato** $*HALT*^{(n-1)}$ rispetta i requisiti della traccia ma non è calcolabile.

Infatti da definizione di **predicato**, $*HALT*^{(n-1)}$ è una **funzione totale** con codominio $\{0,1\}$. Dunque:
$$
    \forall (x_1,x_2,\cdots, x_{n-1}, y) \in \mathbb{N}^n, \mathit{HALT}^{(n-1)}(x_1,x_2,\cdots, x_{n-1}, y)\leq k=1
$$


**Esercizio. ** *Mostrare come calcolabile la funzione:*
$$
    H_1(x) = \begin{cases}
    1, & \Phi(x,x)\downarrow\\
    \uparrow, & \text{altrimenti}
    \end{cases}
$$


Per dimostrare la calcolabilità di questa funzione è sufficiente considerare il seguente programma:
```ini
    Z <- \Phi(X,X)
    Y <- Y + 1
```


Essendo $\Phi(x,x)$ calcolabile può essere infatti usata come macro in altri programmi.  Nel caso $\Phi(x,x)$ termini, il programma terminerà con output $1$, altrimenti terminerà in loop.

Alternativamente è possibile considerare la funzione data come:
$$
    H_1(x)=\alpha(\Phi(x,x)) + \alpha(\alpha(\Phi(x,x)))
$$


Si avrà infatti che:
$$
    \Phi(x,x)\downarrow \land \Phi(x,x)=0 &\implies \alpha(\Phi(x,x))=1 \land \alpha(\alpha(\Phi(x,x)))=0 \implies H_1(x)=1\\
    \Phi(x,x)\downarrow \land \Phi(x,x)\neq0 &\implies \alpha(\Phi(x,x))=0 \land \alpha(\alpha(\Phi(x,x)))=1 \implies H_1(x)=1\\
    \Phi(x,x)\uparrow & \implies H_1(x)\uparrow
$$

**Esercizio. ** *Trovare un programma $\mathcal{P}$ tale che il seguente predicato sia non calcolabile:*
$$
    H_{\mathcal{P}}(x_1,x_2) \iff \text{il programma \(\mathcal{P}\) termina su input \(x_1,x_2\)}
$$


Basta considerare il programma universale $\mcU^{(1)}$ che calcola $\Phi^{(1)}(x_1,x_2)$, allora:
$$
    H_{\mcU^{(1)}}(x_1,x_2) \iff \Phi^{(1)}(x_1,x_2)\downarrow \iff HALT(x_1,x_2)
$$


## Insiemi Ricorsivi e Ricorsivamente Enumerabili


**Esercizio. ** *Sia $B \subseteq \mathbb{N}^m, m > 1$. Diciamo che $B$ è **ricorsivamente enumerabile** se $B=\{(x_1,\cdots, x_m) \in \mathbb{N}^m \vert g(x_1, \cdots, x_m)\downarrow\}$ per qualche funzione $g$ parzialmente calcolabile. Mostrare che:*
$$
    
    B \text{ è ricorsivamente enumerabile} \iff B'=\{[x_1, \cdots, x_m] \vert (x_1, \cdots, x_m) \in B \} \text{ è ricorsivamente enumerabile}
$$


Dimostriamo la doppia implicazione.
- **$\Longleftarrow$** Supponiamo che $B'$ sia ricorsivamente enumerabile. Allora esiste una funzione $g'$ parzialmente calcolabile tale che \\
$B'=\{y \in \mathbb{N} \vert g'(y)\downarrow\}$. Sappiamo poi dalla definizione data in precedenza di $B'$ che:
$$
    \forall y \in B': y=[x_1, \cdots, x_m], (x_1, \cdots, x_m) \in B
$$

Consideriamo dunque il seguente programma di $m$ variabili:
```ini
        Z <- [X1, X2, \cdots, Xm]
        Z2 <- g'(Z)
```

Questo programma termina se e solo se $y=[x_1, \cdots, x_m] \in B'$, ovvero se e solo se $(x_1, \cdots, x_m) \in B$. Dunque $B$ è ricorsivamente enumerabile.
- **$\Longrightarrow$** Sia $B \in \mathbb{N}^m$ ricorsivamente enumerabile. Allora fissato tale $m$ possiamo considerare il seguente programma unario:
```ini
    [A] IF X=0\lor Lt(x)>m GOTO A
        Z1 <- (X)_1
        Z2 <- (X)_2
        \vdots
        Zm <- (X)_m
        Zm+1 <- g(Z1, Z2, \cdots, Zm)
```

Questo programma innanzitutto verifica che l'input sia un numero di Gödel, ovvero sia maggiore di $0$, e che la lunghezza della sua fattorizzazione sia $m$, ovvero sia numero di Gödel di una n-upla di $\mathbb{N}^m$, altrimenti non terminerà. Negli altri casi il programma termina se e solo se $({(x)}_1, \cdots, {(x)}_m) \in B$. Essendo che $\forall (y_1, \cdots, y_m) \in B \exists x \in B' : x=[y_1, \cdots, y_m]$ questo programma termina se e solo se $x \in B'$. Dunque $B'$ è ricorsivamente enumerabile.
È importante notare che questo singolo programma è sufficiente a dimostrare l'enunciato per un singolo $m$ fissato. Per dimostrare l'enunciato per ogni $m$ è necessario considerare un numero infinito di programmi, uno per ogni $m$.

**Esercizio. ** *Dimostrare che $Z=\{ \langle  x,y  \rangle \vert x \in W_y\}$ è ricorsivamente enumerabile*

Possiamo sfruttare la definizione dell'insieme $W$ per dimostrare che $\{ \langle  x,y  \rangle \vert x \in W_y\}$ è ricorsivamente enumerabile.
Sappiamo infatti che $W_y=\{x \in \mathbb{N} \vert \Phi(x, y)\downarrow\}$. Abbiamo dunque che $Z=\{z \vert \Phi(l(z),r(z))\downarrow\}$. Essendo $\Phi(l(z),r(z))$ composta di funzioni parzialmente calcolabili è anch'essa parzialmente calcolabile. Dunque $Z$ è ricorsivamente enumerabile.

**Esercizio. ** \begin{enumerate}
- Sia $B\subseteq \mathbb{N}$ ricorsivamente enumerabile, e $C \subseteq B$. È sempre vero che $C$ è ricorsivamente enumerabile?\\
**NO.** Si consideri $B=N$, chiaramente ricorsivamente enumerabile. Sia ora per assurdo vero che $\forall C \subseteq \mathbb{N}, C$ è ricorsivamente enumerabile. Ma allora anche l'insieme $\overline{K}$ o l'insieme $H=\{x \in \mathbb{N} \vert *HALT*(x,x)\}$ dovrebbero essere ricorsivamente enumerabile. Avendo già dimostrato che questo è falso abbiamo l'assurdo.
- Siano $B,C \in \mathbb{N}$ tali che $B\cup C$ è ricorsivamente enumerabile. È sempre vero che $B$ e $C$ sono ricorsivamente enumerabili?\\
**NO.** Si consideri $B=K$ e $C=\overline{K}$. Avremo che $B\cup C = \mathbb{N}$ è ricorsivamente enumerabile. Ma $C$ non è ricorsivamente enumerabile come già dimostrato.
Si pensi alternativamente agli insiemi $B=\{x \vert *HALT*(x,x)\}$ e $C=\{x \vert \neg *HALT*(x,x)\}=\overline{B}$. Avremo che $B\cup C = \mathbb{N}$ è ricorsivamente enumerabile. Ma $B$ e $C$ non sono ricorsivamente enumerabile come già dimostrato.

**Esercizio. ** *Dimostrare che non esiste una funzione calcolabile $f$ tale che $f(x)=\Phi(x,x)+1$ se $\Phi(x,x)\downarrow$*

Fissando un $x_0 \in \mathbb{N}$ qualsiasi possiamo esprimere una tale funzione $f$ qualsiasi come:
$$
    f(x)=\begin{cases}
    \Phi(x,x)+1, & \Phi(x,x)\downarrow\\
    x_0, & \text{altrimenti}
    \end{cases} = \begin{cases}
    \Psi_{\mathcal{P}_x}^{(1)}(x)+1, & \Psi_{\mathcal{P}_x}^{(1)}(x)\downarrow\\
    x_0, & \text{altrimenti}
    \end{cases}
$$

Questo funzione è dunque analoga alla funzione definita nel teorema*(ref: Esistenza funzioni non calcolabili)* e dunque non è calcolabile.

---


## Macchine di Turing e Automi


**Esercizio. ** *Consideriamo l'alfabeto $A=\{a,b\}$ dimostrare che sono regolari i linguaggi:*

1. Stringhe che terminano con $bbab$

Per dimostrare che questo linguaggio è regolare possiamo costruire un automa a stati finiti che lo riconosca.

\end{figure}
2. Parole $w=s_1 \cdots s_n$ tali che $s_{n-2}=b$

Per dimostrare che questo linguaggio è regolare possiamo costruire un automa a stati finiti che lo riconosca.

\end{figure}

3. Parole che **non** contengono $aaa$

Per dimostrare che questo linguaggio è regolare possiamo costruire un automa a stati finiti che lo riconosca.

\end{figure}

**Esercizio. ** *Considerando l'esempio*(ref: NFA Esempio)*, ricavare la tabella di transizione dell'automa non deterministica e disegnare il diagramma usando un DFA*

**Esercizio. ** *Prendendo in considerazione l'esempio*(ref: Esercizio DFA)*, ricavare il linguaggio accettato dall'automa con $F' = \{q_4\}$*

Per ottenere il linguaggio accettato dall'automa sarà sufficiente seguire tutti i percorsi che arrivano allo stato $q_4$ essendo che questo è l'unico stato d'accettazione e che ogni lettera successiva all'arrivo in $q_4$ ci farà rimanere in $q_4$.

Si avrà che, considerando $A={a,b,c}$ il linguaggio accettato dall'automa è:

$$
    L(\mathcal{M}) = &\{cw \vert w \in A^*\} \cup \{a^{n}bw \vert n > 0, w \in A^*\} \cup \{b^{n}aw \vert n > 0, w \in A^*\} \cup \\
    &\{a^{n}c^{m}xw\vert n,m > 0, w \in A^*, x \in \{a,b\}\} \cup \{b^{n}c^{m}xw\vert n,m > 0, w \in A^*, x \in \{a,b\}\}
$$


---


**Esercizio. ** *Ricavare il linguaggio accettato dal DFA rappresentato dalla seguente tabella avente $F=\{q_2\}$*


| $\pmb{\delta}$ | $\pmb{a}$ | $\pmb{b}$ | $\pmb{c}$ |
|---|---|---|---|
| $\pmb{q_1}$ | $q_2$ | $q_2$ | $q_1$ |
| $\pmb{q_2}$ | $q_3$ | $q_2$ | $q_1$ |
| $\pmb{q_3}$ | $q_1$ | $q_3$ | $q_2$ |


Innanzitutto procediamo a disegnare il diagramma dell'automa.

\end{figure}

Possiamo ora ricavare il linguaggio accettato dall'automa. Seguendo i percorsi che arrivano allo stato $q_2$ avremo che il linguaggio accettato dall'automa conterrà solo parole che iniziano con un numero positivo di $c$ e poi una $a$ o una $b$.

Avremo dunque che $L(\mathcal{M})=\{c^{n}xw \vert n \in \mathbb{N}, x \in \{a,b\}, w \in L'\} $, dove $L'$ è l'insieme delle parole che permettono nell'automa di tornare a $q_2$ partendo da $q_2$ stesso.

Quest'ultimo sarà dunque una qualsiasi combinazione delle parole che permettono di compiere un ciclo singolo da $q_2$ a $q_2$, ovvero $L'=\{u_1u_2\cdots u_n\vert n \in \mathbb{N}, \forall i \in \{1, \cdots, n\}, u_i \in L''\}$, dove $L''$ è l'insieme delle parole che permettono di compiere un ciclo semplice da $q_2$ a $q_2$.

Nello specifico avremo che $L''=\{b\} \cup \{ab^{n}c \vert n \in \mathbb{N}\} \cup \{c^{m}x \vert m > 0, x \in \{a,b\}\} \cup \{ab^{n}ac^{m}x \vert n,m \in \mathbb{N}, x \in \{a,b\}\}$.

Riassumendo si avrà che:

$$
    L(\mathcal{M}) = & \{c^{n}xw \vert n \in \mathbb{N}, x \in \{a,b\}, w \in L'\} \\
    \text {dove } L' = & \{u_1u_2\cdots u_n\vert n\in\mathbb{N}, \forall i \in \{1, \cdots, n\}, u_i \in L''\} \\
    \text {dove } L'' = & \{b\} \cup \{ab^{n}c \vert n \in \mathbb{N}\} \cup \{c^{m}x \vert m > 0, x \in \{a,b\}\} \cup \{ab^{n}ac^{m}x \vert n,m \in \mathbb{N}, x \in \{a,b\}\}
$$


**Esercizio. ** *Mostrare che esiste un linguaggio regolare non accettato da una DFA con uno stato terminale*

Si consideri il linguaggio $L=\{\varepsilon, b\}$. Questo linguaggio è regolare poichè è accettato dall'automa a stati finiti:

\end{figure}

Per questo linguaggio non esiste un DFA con uno stato terminale che lo accetti. Infatti per accettare $\varepsilon$ è necessario che lo stato iniziale sia anche terminale. D'altro canto per accettare $b$ c'è bisogno di una transizione che valuti $b$ dallo stato iniziale ad uno stato terminale. Se ci fosse un unico stato terminale questo sarebbe quello iniziale e dunque la transizione in questione un cappio, che però renderebbe accettate tutte le parole della forma $b^n$ con $n \in \mathbb{N}$.

---


## Operazioni sui Linguaggi Regolari


**Esercizio.** *Sia $A=\{a,b\}$ e siano $L_1=\{w \in A^* \vert w \text{ contiene almeno due occorrenze di } a\}$ e *

$L_2=\{w \in A^* \vert w \text{ contiene almeno due occorrenze di } b\}$.\ *Per ognuno dei seguenti $L$, esibire un NFA che accetti $L$.*

1. $L=L_1 \cup L_2$
2. $L=A^* \setminus L_1$
3. $L=A^* \setminus L_2$
4. $L=L_1 \cap L_2$

Innanzitutto andiamo a verificare che esista un NFA che accetti $L_1$ e una che accetti $L_2$.

}
\subfloat[NFA che accetta $L_2$]{
}
\end{figure}

1. $L=L_1 \cup L_2$
Per l'unione sarà sufficiente considerare l'unione dei due NFA
\end{figure}
2. $L=A^* \setminus L_1= \overline{L_1}$. Dai teoremi*(ref: Regolarità del Complemento)* e*(ref: Corrispondenza tra DFA e NFA)* sarà sufficiente prendere l'automa*(ref: NFA L1)* e invertire tra loro stati terminali e non.
3. $L=A^* \setminus L_2$
Ragionamento analogo al punto precedente.
4. $L=L_1 \cap L_2$

\end{figure}

---


**Esercizio. ** *Siano $L,L'$ regolari. Mostrare che $L \setminus L'$ è regolare.*

$L \setminus L' = L \cap \overline{L'}$. Per i teoremi*(ref: Regolarità dell'intersezione)* e*(ref: Regolarità del Complemento)* sappiamo che $L \cap \overline{L'}$ è regolare.

**Esercizio.** *Siano $L,L'$ tali che $L$ è regolare, $L \cup L$ è regolare e $L \cap L' = \varnothing$. Mostrare che $L'$ è regolare.*

$L\cap L' = \varnothing \implies (L \cup L') \setminus L = L'$. Dal teorema*(ref: Regolarità dell'unione)* e dall'esercizio precedente sappiamo che L' è regolare.

**Esercizio. ** *Mostrare che il linguaggio $L=\{w=a_1a_2\cdots a_n \vert n \in \mathbb{N}, a_i \in A, a_2=a_n\}$ è regolare*

Iniziamo mostrando che $\forall a \in A: L_a=\{xaw \in A^* \vert w \in A^*, x \in A\}$ è regolare.

Per questo è sufficiente considerare l'automa a stati finiti:

\caption{Automa a stati finiti per $L_a$}
\end{figure}

Si avrà per chiusura rispetto al prodotto che $\forall a \in A: L_a\{a\}$ è regolare, essendo tutti i singleton regolari in quanto finiti.

Otteniamo infine che $L= \bigcup\limits_{a \in A} L_a\{a\}$ è regolare per chiusura rispetto all'unione. Si sottolinea come questa operazione non sia una unione infinita in quanto per definizione di **macchina di Turing** la cardinalità di $A$ è finita.

**Esercizio. ** *Per ogni linguaggio $L$ descritto nell'esercizio*(ref: Esercizio NFA 2a2b)*, ricavare un'espressiore regolare $\alpha$ tale che $L = \langle \alpha \rangle$.*

1. $L=L_1 \cup L_2 =\langle \alpha \rangle$ con $\alpha = b^*ab^*ab^* \cup ab^*ab^*ab^*$
2. $L=A^* \setminus L_1 = \langle \alpha \rangle$ con $\alpha = b^*ab^*$
3. $L=A^* \setminus L_2 = \langle \alpha \rangle$ con $\alpha = a^*ba^*$
4. $L=L_1 \cap L_2 = \langle \alpha \rangle$ con $\alpha = a(a{(a \cup b)}^* \cup b(a \cup b){(a \cup b)}^*) \cup b(b{(a \cup b)}^* \cup a(a \cup b){(a \cup b)}^*)$
**Esercizio. ** *Sia $L= \{x \in \{a,b\}^* \vert x \neq \varepsilon \land x \text{ non contiene } bb\}\*
- **\text{a.}** Construire un DFA che accetti $L$;
- **\text{b.}** Scrivere un'espressione regolare $\alpha$ tale che $L = \langle \alpha \rangle$.
\end{itemize}}

  - ***a.*** DFA:
\end{figure}
  - ***b.*** $\alpha = {(a \cup ba)}^*b \cup {(a \cup ba)}^*(a \cup ba) = {(a \cup ba)}^*(b \cup a \cup ba)$

**Esercizio** *Sia $L = \{a^{n}b^{m}c^r \vert n+m \leq r \land n,m,r \in \mathbb{N}\}$. Mostrare che $L$ non è regolare.*

Sia per assurdo $\mathcal{M}$ un DFA di $p$ stati che accetti $L$. Avremo dunque che $x=a^{\frac{p}{2}}b^{\frac{p}{2}}c^{p}$ è accettata da $\mathcal{M}$ e $|x|=2p \geq p$.

Dal **Pumping Lemma rafforzato** sappiamo che $\exists u,v,w \in A^*$ tali che $x=uvw \land v \neq \varepsilon \land |uv| \leq p \land \forall i \in \mathbb{N}: uv^{i}w\in L$.

Avremo dunque che la scelta per $v$ è limitata a tre possibilità:
  1. $v=a^k, \frac{p}{2} \geq k > 0 \implies uv^{2}w = a^{\frac{p}{2}+k}b^{\frac{p}{2}}c^{p} \notin L$,  essendo che $\frac{p}{2}+k+\frac{p}{2} > p$
  2. $v=b^k, \frac{p}{2} \geq k > 0 \implies uv^{2}w = a^{\frac{p}{2}}b^{\frac{p}{2}+k}c^{p} \notin L $, essendo che $\frac{p}{2}+k+\frac{p}{2} > p$
  3. $v=a^{j}b^k, \frac{p}{2} \geq j,k > 0 \implies uv^{2}w = a^{\frac{p}{2}}b^{k}a^{j}b^{\frac{p}{2}}c^{p} \notin L $, avendo una struttura errata.

---

[^1]: Da ora in avanti le funzioni costanti saranno considerate tutte calcolabili, e dunque usate in S-Programmi