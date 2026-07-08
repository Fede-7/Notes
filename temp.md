# Conversione A/D di variabili aleatorie

Quando $X$ è una variabile continua e $Y$ è una variabile discreta, si ha una **conversione** $\mathsf { A } / \mathsf { D }$ di una quantità aleatoria (confronta anche l’ultima sezione della parte ”Conversione $\mathsf { A } / \mathsf { D } ^ { \prime \prime } )$").

Supponiamo di voler rappresentare $X$ con $R$ bit, ovvero con $M = 2 ^ { R }$ livelli. 

Definiamo una variabile aleatoria $\boldsymbol { Y } = \boldsymbol { g } ( \boldsymbol { X } )$ con $\mathcal { Y } = \{ y _ { 1 } , \dots , y _ { M } \}$. 

Definiamo una partizione di $X$ in $M$ intervalli, definiti dai punti $\{ x _ { i } \} _ { i = 1 } ^ { M + 1 }$. 

Si definisce rappresentazione a $R$ bit di $X$ la variabile aleatoria discreta: 

$$
Y = y _ {i} \quad \text { se } x _ {i} \leq X \leq x _ {i + 1} \quad i = 1, \dots , M
$$

La **pmf** (Probability Mass Function) di $Y$ quindi si scrive facilmente nella forma: 

$$
p _ {Y} (y _ {i}) = P _ {X} \left(\frac {x _ {i + 1} + x _ {i}}{2}; \frac {x _ {i + 1} - x _ {i}}{2}\right) = F _ {X} (x _ {i + 1}) - F _ {X} (x _ {i}), \quad i = 1, \ldots , M
$$

> [!quote] Osservazione
> Ovviamente tanto la partizione quanto i livelli di rappresentazione sono gradi di libertà a disposizione del progettista. 

## Media di funzioni di variabili aleatorie continue

Sia $X$ una variabile aleatoria continua con pdf $f_X(x)$ e sia $g(x)$ una funzione tale che $\mathcal { V } = g ( \mathcal { X } )$. Vogliamo estendere alle variabili continue il Teorema Fondamentale per il calcolo della media (vedi slide 60 e seguenti). Il risultato principale - diretta derivazione del caso discreto - è che, qualunque sia $g(x)$, vale:

$$
\mathbb {E} \left[ Y \right] = \mathbb {E} \left[ g (X) \right] = \int_ {\mathbb {R}} g (x) f _ {X} (x) d x
$$

Definiamo una versione quantizzata di $X$ a $M$ livelli, $x ^ { \Delta }$, in modo del tutto analogo a quanto fatto per ricavare la media di variabili continue (vedi slide 100). 

A questa applichiamo la trasformazione $g ( \cdot )$, ottenendo la variabile discreta ${ \cal Y } ^ { \Delta } = g ( X ^ { \Delta } )$: 

$$
X ^ {\Delta} = x _ {i} \in [ i \Delta , (i + 1) \Delta [ \quad i \Delta \leq X <   (i + 1) \Delta \Rightarrow g (X ^ {\Delta}) = g (x _ {i})
$$

Il teorema quindi segue - se $g ( x ) f _ { X } ( x )$ è Riemann-integrabile - dall’essere:

$$
\mathbb {E} \left[ Y \right] = \lim _ {\Delta \rightarrow 0} \mathbb {E} \left[ Y ^ {\Delta} \right] = \lim _ {\Delta \rightarrow 0} \sum_ {i = 1} ^ {M} g (x _ {i}) \underbrace {f _ {X} (x _ {i}) \Delta} _ {\simeq \mathbb {P} (i \Delta \leq X <   (i + 1) \Delta)} = \int_ {\mathbb {R}} g (x) f _ {X} (x)   d x
$$

## Valore quadratico medio e varianza di variabili continue

A questo punto è immediata la generalizzazione dei concetti introdotti per variabili discrete a variabili continue. 

Data una variabile aleatoria $X$ con media $\mu _ { X } = \operatorname { \mathbb { E } } [ X ]$, definiamo: 

Il **valore quadratico medio** (Mean Square) di $X$: 

$$
X _ {\mathrm{rms}} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] = \int_ {\mathbb {R}} x ^ {2} f _ {X} (x) d x
$$

Il **valore efficace** (root mean square, rms) di $X$: 

$$
X _ {\mathrm{rms}} = \sqrt {\mathbb {E} \left[ X ^ {2} \right]} = \sqrt {\int_ {\mathbb {R}} x ^ {2} f _ {X} (x) d x}
$$

La **varianza** di $X$: 

$$
\sigma_ {X} ^ {2} = \mathbb {E} \left[ (X - \mu_ {X}) ^ {2} \right] = \int_ {\mathbb {R}} (x ^ {2} + \mu_ {X} ^ {2} - 2 x \mu_ {X}) f _ {X} (x) d x = X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}
$$

La **deviazione standard** di $X$: 

$$
\sigma_ {X} = \sqrt {\sigma_ {X} ^ {2}} = \sqrt {\mathbb {E} [ X ^ {2} ] - \mu_ {X} ^ {2}} = \sqrt {X _ {\mathrm{rms}} ^ {2} - \mu_ {X} ^ {2}}
$$

> [!tip] Nota
> Tutte le proprietà della slide 68 valgono ovviamente anche per variabili continue. 

## Qualche esempio

> [!example] Esempio 1 (*Calcolo Media*)
> Sia $X$ una variabile aleatoria con pdf $f_X(x) = \frac{1}{2}$ per $x \in [-1, 1]$. Si ottiene facilmente: 
>
> $$
> \mu_ {X} = \frac {a + b}{2} \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {a ^ {2} + b ^ {2} + a b}{3} \qquad \sigma_ {X} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] - \mu_ {X} ^ {2} = \frac {(b - a) ^ {2}}{1 2}
> $$

> [!example] Esempio 2 (*Calcolo Varianza*)
> Sia $f_X(x) = x$ per $x \in [0, 1]$. Avremo: 
>
> $$
> \mu_ {X} = \frac {1}{\lambda} \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {2}{\lambda^ {2}} \qquad \sigma_ {X} ^ {2} = \mathbb {E} \left[ X ^ {2} \right] - \mu_ {X} ^ {2} = \frac {1}{\lambda^ {2}}
> $$

> [!example] Esempio 3 (*Calcolo RMS*)
> Sia $f_X(x) = \frac{1}{2}$ per $x \in [0, 2]$. Avremo: 
>
> $$
> \mu_ {X} = 0 \qquad \mathbb {E} \left[ X ^ {2} \right] = \frac {2}{\lambda^ {2}} \qquad \sigma_ {X} ^ {2} = \mathbb {E} [ X ^ {2} ] = \frac {2}{\lambda^ {2}}
> $$

> [!example] Esempio 4 (*Caso non integrabile*)
> Sia $f_X(x) = \frac{1}{x^2}$ per $x \in [1, \infty)$. Non esistono in questo caso né la media, né la varianza, né, quindi, il valore rms o la deviazione standard. 

## Variabili continue multiple 

In perfetta analogia con quanto fatto per variabili discrete (vedi slide 69), una coppia di variabili continue (o variabile doppia) è definita nella forma: 

$$
X, Y: \omega \in \Omega \longrightarrow (X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y} \subseteq \mathbb {R} ^ {2}
$$

dove $\mathcal { X } \in \mathcal { V }$ sono gli alfabeti di $X$ e di $Y$ rispettivamente. 

Analogamente, date tre variabili aleatorie - a questo punto non importa più se tutte continue o meno $\begin{array} { r } { - X ( \omega ) \in \mathcal { X } , y ( \omega ) \in \mathcal { Y } , Z ( \omega ) \in \mathcal { Z } ; } \end{array}$ 

$$
X, Y, Z: \omega \in \Omega \longrightarrow (X (\omega), Y (\omega), Z (\omega)) \in \mathcal {X} \times \mathcal {Y} \times \mathcal {Z} \subseteq \mathbb {R} ^ {3}
$$

e, date $m$ variabili aleatorie $X _ { i } \in \mathcal { X } _ { i } \subseteq \mathbb { R }$, avremo la $m$-pla aleatoria: 

$$
X _ {1}, \dots , X _ {m}: \omega \in \Omega \longrightarrow (X _ {1} (\omega), \dots , X _ {m} (\omega)) \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {m} \subseteq \mathbb {R} ^ {m}
$$

## pdf congiunta di due variabili aleatorie

Si consideri una coppia di variabili continue, $X \in \mathcal { X } \mathrm { ~ e ~ } Y \in \mathcal { Y }$, la loro **pdf congiunta** $f_{X,Y}(x,y)$ si definisce in perfetta analogia con la pdf di variabili continue singole (vedi slide 94): 

$$
\begin{array}{l} f _ {X, Y} (x, y) = \lim _ {\Delta x \to 0} \lim _ {\Delta y \to 0} \frac {\mathbb {P} \left(\left\{x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \right\} \cap \left\{y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2} \right\}\right)}{\Delta x \Delta_ {y}} \\ = \lim _ {\Delta x \to 0} \lim _ {\Delta y \to 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{\Delta x \Delta y} \quad (x, y) \in \mathcal {X} \times \mathcal {Y} \end{array}
$$

Per il teorema fondamentale del calcolo integrale abbiamo quindi che, se $C \subseteq \mathcal { X } \times \mathcal { y }$ 

$$
\mathbb {P} ((X, Y) \in C) = \int_ {C} f _ {X, Y} (x, y) d x d y
$$

Le densità di probabilità congiunte devono soddisfare dei vincoli costitutivi - simili a quelli delle densità marginali: 

$$
a f _ {X, Y} (x, y) \geq 0 \forall \space (x, y) \in \mathbb {R} ^ {2};
$$

$b$ $f _ { X , Y } ( x , y )$ è sommabile su $\mathbb { R } ^ { 2 }$ e a integrale unitario. Infatti: 

$$
\int_ {\mathbb {R} ^ {2}} f _ {X, Y} (x, y) d x d y = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} f _ {X, Y} (x, y) d x d y = \mathbb {P} ((X, Y) \in \mathbb {R} ^ {2}) = 1
$$

## Proprietà della pdf congiunta

La **pdf congiunta** $f _ { X , Y } ( x , y )$ condivide con la pmf congiunta $p x , \gamma ( x , y ) \textrm { - e }$, per alcune, con tutte le densità, le seguenti proprietà: 

### Proprietà di marginalizzazione

$$
\int_ {\mathbb {R}} f _ {X, Y} (x, y) d y = f _ {X} (x) \qquad \int_ {\mathbb {R}} f _ {X, Y} (x, y) d x = f _ {Y} (y)
$$

Per cui caratterizzare congiuntamente $( X , Y )$ significa anche caratterizzarle marginalmente, mentre il viceversa non è necessariamente vero. 

### Indipendenza statistica

Due variabili aleatorie sono **indipendenti** se e solo se 

$$
f _ {X, Y} (x, y) = f _ {X} (x) f _ {Y} (y) \Longleftrightarrow F _ {X, Y} (x, y) = \mathbb {P} (X \leq x, Y \leq y) = F _ {X} (x) F _ {Y} (y)
$$

Più in generale, se $X _ { i } \sim f _ { X _ { i } } ( x ) , x \in \mathcal { X } _ { i }$, allora esse sono indipendenti se e solo se: 

$$
f _ {X _ {1}, \dots , X _ {m}} (x _ {1}, \dots , x _ {m}) = \prod_ {i = 1} ^ {m} f _ {X _ {i}} (x _ {i}), \qquad (x _ {1}, \dots , x _ {m}) \in \mathbb {R} ^ {m}
$$

## Le pdf condizionate

Si considerino variabili aleatorie $X \in \mathcal { X } \mathrm { ~ e ~ } Y \in \mathcal { Y }$ con assegnata pdf congiunta $f _ { X , Y } ( x , y )$. 

La **pdf condizionata** di $X$ dato $Y$ si può definire a partire dalla seguente quantità (vedi slide 110): 

$$
\mathbb {P} \left(x - \frac {\Delta x}{2} \leq X \leq x + \frac {\Delta x}{2} \mid y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2}\right) = \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{P _ {Y} (y ; \Delta y)}
$$

Pertanto la densità di $X$ condizionata all’evento $\begin{array} { r } { \left\{ y - \frac { \Delta y } { 2 } \leq Y \leq y + \frac { \Delta y } { 2 } \right\} } \end{array}$ è: 

$$
\lim _ {\Delta x \rightarrow 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{\Delta x P _ {Y} (y ; \Delta y)} = f _ {X | \{y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2} \}} (x | y - \frac {\Delta y}{2} \leq Y \leq y + \frac {\Delta y}{2})
$$

Facendo dunque tendere $\Delta y$ a zero, otteniamo: 

$$
f _ {X \mid Y} (x \mid y) = \lim _ {\Delta x \rightarrow 0} \lim _ {\Delta y \rightarrow 0} \frac {P _ {X , Y} (x , y ; \Delta x , \Delta y)}{P _ {Y} (y ; \Delta y)} = \frac {f _ {X , Y} (x , y)}{f _ {Y} (y)}
$$

che, come c’era da attendersi, riproduce l’analoga definizione per la pmf condizionale che, d’altronde, è essa stessa una densità. 

Di conseguenza tutte le proprietà delle pmf condizionali si estendono alle pdf condizionali. 

## Proprietà delle pdf condizionate

Data l’analogia con le variabili discrete, ci limitiamo qui a riscrivere le proprietà della slide 74. 

$f _ { X \mid Y } ( x | y )$ se $y$ resta fisso e $x$ varia in $X$ è una densità di probabilità, cioè: 

$$
f _ {X | Y} (x | y) \geq 0 \int_ {\mathbb {R}} f _ {X | Y} (x | y) d x = 1
$$

### Legge della probabilità totale per le pdf

$$
f _ {X} (x) = \int_ {\mathbb {R}} f _ {X, Y} (x, y) d y = \int_ {\mathbb {R}} f _ {X | Y} (x | y) f _ {Y} (y) d y
$$

$$
f _ {Y} (y) = \int_ {\mathbb {R}} f _ {X, Y} (x, y) d x = \int_ {\mathbb {R}} f _ {Y | X} (y | x) f _ {X} (x) d x
$$

### Leggi della probabilità composta e di Bayes per le densità

$$
f _ {X, Y} (x, y) = f _ {Y} (y) f _ {X | Y} (x | y) = f _ {X} (x) f _ {Y | X} (y | x) \Rightarrow f _ {Y | X} (y | x) = \frac {f _ {Y} (y) f _ {X | Y} (x | y)}{f _ {X} (x)}
$$

## Altre estensioni...

Come nel caso discreto, avremo: 

Se $Z = \boldsymbol { \mathrm { g } } ( \boldsymbol { X } , \boldsymbol { Y } )$ allora 

$$
\mathbb {E} [ Z ] = \int_ {\mathbb {R} ^ {2}} g (x, y) f _ {X}, \gamma (x, y) d x d y
$$

### Linearità della media

$$
\mathbb {E} \left[ \sum_ {i = 1} ^ {m} a _ {i} X _ {i} \right] = \sum_ {i = 1} ^ {m} a _ {i} \mathbb {E} \left[ X _ {i} \right]
$$

### Teorema della media condizionata

> [!theorem] Teorema (*Media Condizionata*)
> Enunciato: 
> $$
> \mathbb {E} \left[ g (X, Y) \right] = \mathbb {E} \left[ \mathbb {E} \left[ g (X, Y) | Y \right] \right]
> $$
>
> dove: 
> $$
> \mathbb {E} \left[ g (X, Y) | Y = y \right] = \int_ {\mathbb {R}} g (x, y) f _ {X | Y} (x | y) d x = \mathbb {E} \left[ h (Y (\omega)) \right] \Longleftrightarrow
> $$
>
> $$
> h \left[ Y (\omega) \right] = \int_ {\mathbb {R}} g (x, Y) f _ {X | Y} (x | Y) d x
> $$

## Covarianza tra due variabili continue

Siano $( X , Y ) \sim f _ { X , Y } ( x , y )$. Denotiamo con $( \mu _ { X } , \mu _ { Y } )$ le rispettive medie e $( \sigma _ { X } ^ { 2 } , \sigma _ { Y } ^ { 2 } )$ le rispettive varianze. Avremo, in analogia al caso discreto: 

### Covarianza tra $X \in Y ;$

$$
\operatorname{COV} [ X, Y ] = \mathbb {E} \left[ (X - \mu_ {X}) (Y - \mu_ {Y}) \right] = \mathbb {E} [ X Y ] - \mu_ {X} \mu_ {Y}
$$

### Coefficiente di correlazione tra $X \textsf { e Y }$

$$
\rho_ {X, Y} = \frac {\operatorname{COV} [ X , Y ]}{\sigma_ {X} \sigma_ {Y}}, \quad \left| \rho_ {X, Y} \right| \leq 1
$$

### Incorrelazione tra $X \textsf { e } Y \colon { \mathsf { C O V } } [ X , Y ] = 0$

> [!quote] Osservazione
> Indipendenza implica incorrelazione, ma incorrelazione non implica indipendenza. 

## Variabili Gaussiane: Caratterizzazione marginale

Una variabile aleatoria $X _ { 0 } \in \mathcal { X } = \mathbb { R }$ si dice **Gaussiana** (o Normale) standard - $X _ { 0 } \sim \mathcal { N } ( 0 , 1 )$ se: 

$$
f _ {X _ {0}} (x _ {0}) = \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {x _ {0} ^ {2}}{2}}, \quad x \in \mathbb {R} \quad \Longrightarrow \quad \mathbb {E} [ X _ {0} ] = 0 \quad \sigma_ {X _ {0}} ^ {2} = \mathbb {E} [ X _ {0} ^ {2} ] = 1
$$

Consideriamo ora la variabile aleatoria $X = \sigma _ { X } X _ { 0 } + \mu _ { X } , \sigma _ { X } > 0 \mathrm { ~ e ~ } \mu _ { X } \in \mathbb { R }$. Applicando i risultati delle slide 114 e seguenti alla funzione lineare $g ( x ) = \sigma { x } { x } + \mu { x }$ otteniamo: 

$$
f _ {X} (x) = \frac {1}{\sqrt {2 \pi \sigma_ {X} ^ {2}}} e ^ {- \frac {(x - \mu_ {X}) ^ {2}}{2 \sigma_ {X} ^ {2}}}, \quad x \in \mathbb {R} \quad \Longrightarrow X \sim \mathcal {N} (\mu_ {X}, \sigma_ {X} ^ {2})
$$

dove ovviamente: 

$$
\mathbb {E} [ X ] = \mathbb {E} \left[ \sigma_ {X} X _ {0} + \mu_ {X} \right] = 0
$$

$$
\mathbb {E} \left[ (X - \mu_ {X}) ^ {2} \right] = \operatorname{VAR} \left[ \sigma_ {X} X _ {0} + \mu_ {X} \right] = \sigma_ {X} ^ {2}
$$

## Andamenti di pdf Gaussiane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/14bd5c980e8521e5eb02a7517ff1fac46626c196028264217617a09b4afc4823.jpg)
Figura 1: Andamenti di pdf Gaussiane.

## La funzione Q(x)

Sia $X _ { 0 } \sim \mathcal { N } ( 0 , 1 )$: nè la sua CDF né la sua CCDF sono note in forma esplicita, poiché $e ^ { - \gamma x ^ { 2 } }$ non ammette primitive elementari. 

Definiamo: 

$$
Q (x) \stackrel {\mathrm{def}} {=} \mathbb {P} (X \geq x) = 1 - F _ {X _ {0}} (x) = \frac {1}{\sqrt {2 \pi}} \int_ {x} ^ {\infty} e ^ {- \frac {t ^ {2}}{2}} d t
$$

per cui: 

$$
F _ {X _ {0}} (x) = 1 - Q (x) \quad P _ {X _ {0}} (x; \Delta x) = Q \left(x - \frac {\Delta x}{2}\right) - Q \left(x + \frac {\Delta x}{2}\right)
$$

Ovviamente, se $X \sim \mathcal { X } ( \mu _ { X } , \sigma _ { X } ^ { 2 } )$, avremo $X = X _ { 0 } \sigma _ { X } + \mu _ { X }$, per cui: 

$$
1 - F _ {X} (x) = \frac {1}{\sqrt {2 \pi \sigma_ {X} ^ {2}}} \int_ {x} ^ {\infty} e ^ {- \frac {(t - \mu_ {X}) ^ {2}}{2 \sigma_ {X} ^ {2}}} d t = Q \left(\frac {x - \mu_ {X}}{\sigma_ {X}}\right)
$$

Dato il suo uso frequente, nella prossima slide è presentato un diagramma della funzione $Q ( x ) , x \geq 0$. 

## Andamento di Q(x)

$$
Q (x) \sim \frac {1}{x \sqrt {2 \pi}} e ^ {- \frac {x ^ {2}}{2}} <   e ^ {- \frac {x ^ {2}}{2}}, \qquad x \to \infty
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9e014a72e6bb4cff5f6045f5e3af68f8479b85e9889bcb10a79b45de356eb16a.jpg)
Figura 2: Andamento di Q(x).

## Alcune utili proprietà della funzione Q(x)

Si noti preliminarmente che 

$$
Q (- \infty) = \frac {1}{\sqrt {2 \pi}} \int_ {\mathbb {R}} e ^ {- \frac {t ^ {2}}{2}} d x = 1 \qquad Q (\infty) = 0
$$

Inoltre: 

$$
\frac {d Q (x)}{d x} = - \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {x ^ {2}}{2}} <   0 \forall \space x \rightarrow Q (x) \text {   è   decrescente   in   } x
$$

### Simmetria

$$
Q (- x) = \frac {1}{\sqrt {2 \pi}} \int_ {- x} ^ {\infty} e ^ {- \frac {t ^ {2}}{2}} d t = 1 - \underbrace {\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {- x} e ^ {- \frac {t ^ {2}}{2}} d t} _ {= Q (x)} = 1 - Q (x)
$$

Se $X \sim \mathcal N ( \mu _ { X } , \sigma _ { X } ^ { 2 } )$ allora: 

$$
\mathbb {P} (X \geq \eta) = \mathbb {P} (X _ {0} \sigma_ {X} + \mu_ {X} \geq \eta) = \mathbb {P} (X _ {0} \geq \frac {\eta - \mu_ {X}}{\sigma_ {X}}) = Q (\frac {\eta - \mu_ {X}}{\sigma_ {X}})
$$

## Caratterizzazione congiunta di variabili Gaussiane

Siano $X _ { 1 } \sim \mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) \in X _ { 2 } \sim \mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$. Noi sappiamo che: 

$$
\sigma_ {1} ^ {2} = \mathbb {E} \left[ (X _ {1} - \mu_ {1}) ^ {2} \right] \quad \sigma_ {2} ^ {2} = \mathbb {E} \left[ (X _ {2} - \mu_ {2}) ^ {2} \right] \quad \rho_ {1, 2} = \overbrace {\frac {\mathbb {E} \left[ (X _ {1} - \mu_ {1}) (X _ {2} - \mu_ {2}) \right]}{\sigma_ {1} \sigma_ {2}}} ^ {\mathrm{COV} (X _ {1}, X _ {2})}
$$

rappresenta una caratterizzazione ”globale” (cioè incompleta) della coppia $( X _ { 1 } , X _ { 2 } )$. Organizziamo tale coppia in un vettore colonna $\pmb { X } = ( X _ { 1 } \pmb { X } _ { 2 } ) ^ { T }$. Ovviamente, $\pmb { x } \in \mathbb { R } ^ { 2 \times 1 }$ è un **vettore bidimensionale aleatorio**, la cui media è essa stessa un vettore, $\mu _ { X } = ( \mu _ { 1 } \mu _ { 2 } ) ^ { T }$.

Definiamo **Matrice di covarianza** del vettore $X$ la matrice $\kappa _ { X } \in \mathbb R ^ { 2 \times 2 }$:

$$
\boldsymbol {K} _ {\boldsymbol {X}} \stackrel {{\text { def }}} {{=}} \mathbb {E} \left[ (\boldsymbol {X} - \boldsymbol {\mu} _ {\boldsymbol {X}}) (\boldsymbol {X} - \boldsymbol {\mu} _ {\boldsymbol {X}}) ^ {T} \right] = \mathbb {E} \left[ \binom{X _ {1} - \mu_ {1}}{X _ {2} - \mu_ {2}} (X _ {1} - \mu_ {1} X _ {2} - \mu_ {2}) \right] =
$$

$$
\Sigma = E[(X - \mu)(X - \mu)^T] \tag{1}
$$

$$
= \mathbb {E} \left[ \begin{array}{c c} (X _ {1} - \mu_ {1}) ^ {2} & (X _ {1} - \mu_ {1}) (X _ {2} - \mu_ {2}) \\ (X _ {2} - \mu_ {2}) (X _ {1} - \mu_ {1}) & (X _ {2} - \mu_ {2}) ^ {2} \end{array} \right] = \left( \begin{array}{c c} \sigma_ {1} ^ {2} & \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ \sigma_ {1} \sigma_ {2} \rho_ {1, 2} & \sigma_ {2} ^ {2} \end{array} \right)
$$

## Alcune proprietà della matrice di covarianza

Poiché $| \boldsymbol { K } \boldsymbol { x } | = \sigma _ { 1 } ^ { 2 } \sigma _ { 2 } ^ { 2 } \bigl ( 1 - \rho _ { 1 , 2 } ^ { 2 } \bigr ) \geq 0 , \boldsymbol { K } \boldsymbol { x }$ è definita non negativa; 

Se $\rho _ { 1 , 2 } \neq \pm 1 \kappa _ { x }$ è invertibile e ha inversa definita positiva: 

$$
\boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} = \frac {1}{\sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})} \left( \begin{array}{c c} \sigma_ {2} ^ {2} & - \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ - \sigma_ {1} \sigma_ {2} \rho_ {1, 2} & \sigma_ {1} ^ {2} \end{array} \right)
$$

$\kappa _ { x }$ è simmetrica; 

Ovviamente, se $\pmb { z } = [ z _ { 1 } z _ { 2 } ] ^ { T } \in \mathbb { R } ^ { 2 \times 1 }$ 

$$
\boldsymbol {z} ^ {T} \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} \boldsymbol {z} \geq 0 \quad \forall \space \boldsymbol {z} \in \mathbb {R} ^ {2 \times 1}
$$

Se $X _ { 1 } \texttt { e } X _ { 2 }$ sono incorrelate allora $\rho _ { 1 , 2 } = 0$, per cui $\kappa _ { x }$ diventa la matrice diagonale: 

$$
\boldsymbol {K} _ {\boldsymbol {X}} = \left( \begin{array}{c c} \sigma_ {1} ^ {2} & 0 \\ 0 & \sigma_ {2} ^ {2} \end{array} \right) \Longrightarrow \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} = \left( \begin{array}{c c} \frac {1}{\sigma_ {1} ^ {2}} & 0 \\ 0 & \frac {1}{\sigma_ {2} ^ {2}} \end{array} \right)
$$

## Variabili congiuntamente Gaussiane

Le due variabili $X _ { 1 } \sim \mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) \in X _ { 2 } \sim \mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$ si dicono **congiuntamente Gaussiane** se la loro pdf congiunta - cioè la pdf del vettore $\pmb { X } = ( X _ { 1 } X _ { 2 } ) ^ { T }$ - si scrive: 

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \frac {1}{2 \pi | \boldsymbol {K} _ {\boldsymbol {X}} | ^ {1 / 2}} \exp \left[ - \frac {1}{2} (\boldsymbol {x} - \boldsymbol {\mu} _ {\boldsymbol {X}}) ^ {T} \boldsymbol {K} _ {\boldsymbol {X}} ^ {- 1} (\boldsymbol {x} - \boldsymbol {\mu} _ {\boldsymbol {X}}) \right] = f _ {X _ {1}, X _ {2}} (x _ {1}, x _ {2}) =
$$

$$
f(x_1, x_2) = \frac{1}{2\pi \sqrt{|\Sigma|}} \exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)\right) \tag{2}
$$

$$
\frac {1}{2 \pi \sqrt {\sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})}} \exp \left[ - \frac {\sigma_ {2} ^ {2} (x _ {1} - \mu_ {1}) ^ {2} + \sigma_ {1} ^ {2} (x _ {2} - \mu_ {2}) ^ {2} - 2 \rho_ {1 , 2} (x _ {1} - \mu_ {1}) (x _ {2} - \mu_ {2})}{2 \sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})} \right]
$$

In questo caso si può usare la notazione abbreviata $\pmb { X } \sim \mathcal { N } ( \pmb { \mu } \pmb { x } , \pmb { K } \pmb { x } )$:

> [!example] Notazione abbreviata
> $X \sim \mathcal{N}(\mu, \Sigma)$

Nel caso speciale $\rho _ { 1 , 2 } = 0$, la precedente dà: 

$$
f _ {\pmb {X}} (\pmb {x}) = f _ {X _ {1}, X _ {2}} (x _ {1}, x _ {2}) = \frac {1}{2 \pi \sqrt {\sigma_ {1} ^ {2} \sigma_ {2} ^ {2}}} e ^ {- \frac {(x _ {1} - \mu_ {1}) ^ {2}}{2 \sigma_ {1} ^ {2}} - \frac {(x _ {2} - \mu_ {2}) ^ {2}}{2 \sigma_ {2} ^ {2}}} = f _ {X _ {1}} (x _ {1}) f _ {X _ {2}} (x _ {2})
$$

cioè se due variabili sono congiuntamente Gaussiane (e solo in questo caso) l’incorrelazione implica l’indipendenza statistica! 

## Proprietà di chiusura rispetto a trasformazioni lineari

Se $\pmb { x } \sim \mathcal { N } ( \pmb { \mu } \pmb { x } , \pmb { K } \pmb { x } )$ allora ogni trasformazione lineare di $X$ dà luogo a un nuovo vettore Gaussiano. 

Focalizziamoci prima su una semplice combinazione lineare di $X _ { 1 } \texttt { e } X _ { 2 }$. Avremo che: 

$$
\begin{array}{c} Z = a _ {1} X _ {1} + a _ {2} X _ {2} \Rightarrow \mu_ {Z} = a _ {1} \mu_ {1} + a _ {2} \mu_ {2} \quad \sigma_ {Z} ^ {2} = a _ {1} ^ {2} \sigma_ {1} ^ {2} + a _ {2} ^ {2} \sigma_ {2} ^ {2} + 2 a _ {1} a _ {2} \sigma_ {1} \sigma_ {2} \rho_ {1, 2} \\ \boxed {Z \sim \mathcal {N} (\mu_ {Z}, \sigma_ {Z} ^ {2})} \end{array}
$$

Più in generale, se $\pmb { Z } = \pmb { A } \pmb { X } + \pmb { b }$, con $\pmb { A } \in \mathbb { R } ^ { 2 \times 2 } \mathrm { ~ e ~ } \pmb { b } \in \mathbb { R } ^ { 2 \times 1 }$ allora: 

$$
\mu_ {Z} = A \mu_ {X} + b
$$

$$
\mu_{Y} = A \mu_{X} \tag{3}
$$

$$
\mathbb {E} \left[ (Z - \mu_ {Z}) (Z - \mu_ {Z}) ^ {T} \right] = A K _ {X} A ^ {T} = K _ {Z}
$$

$$
\Sigma_{Y} = A \Sigma_{X} A^T \tag{4}
$$

$$
\mathbf {Z} \sim \mathcal {N} (\boldsymbol {\mu_ {Z}}, \mathbf {K _ {Z}})
$$

## Richiami sulle variabili aleatorie

- Si consideri uno spazio di probabilità arbitrario, $\Omega , \tau , \mathbb { P }$, dove $\Omega \ { \dot { \mathbf { e } } }$ lo spazio dei campioni, $\mathcal{T}$ una $\sigma$-algebra di eventi di $\Omega \textsf { e l P } \colon { \mathcal { T } }  [ 0 , 1 ]$ una legge di probabilità. 

- Ricordiamo che una **variabile aleatoria** reale $X$ è una funzione (misurabile) definita come: 

$$
X: \omega \in \Omega \Longrightarrow X (\omega) \in \mathcal {X} \subseteq \mathbb {R}
$$

- La variabile aleatoria è discreta se tale è $X$, continua se tale è $X$. 

- Una coppia di variabili aleatorie è un’applicazione 

$$
X, Y: \omega \in \Omega \Longrightarrow (X (\omega), Y (\omega)) \in \mathcal {X} \times \mathcal {Y} \subseteq \mathbb {R} ^ {2}
$$

- La variabile aleatoria $X$ si dice completamente caratterizzata se ne $\grave { \mathbf { e } }$ nota la **CDF** $F _ { X } ( x ) \circ$ - equivalentemente - la **DF** $p _ { X } ( x )$ o la **pdf** $f _ { X } ( x )$ nel caso discreto e continuo, rispettivamente: 

$$
F _ {X} (x) = \mathbb {P} \left\{X \leq x \right\} \forall \space x \in \mathbb {R} p _ {X} (x) = \mathbb {P} \left\{X = x \right\} \forall \space x \in \mathcal {X} f _ {X} (x) = \frac {d f _ {X} (x)}{d x}
$$

- Parallelamente, per la coppia $( X , Y )$ si ha: 

$$
F _ {X, Y} (x, y) = \mathbb {P} \left\{X \leq x, Y \leq y \right\} \forall \space (x, y) \in \mathbb {R} ^ {2} f _ {X, Y} (x, y) = \frac {\partial^ {2} F _ {X , Y} (x , y)}{\partial x \partial y}
$$

$$
p _ {X, Y} (x, y) = \mathbb {P} \{X = x, Y = y \} \forall \space x \in \mathcal {X} \times \mathcal {Y}
$$

## Vettori aleatori

- Una **n-pla aleatoria** è una ovvia generalizzazione del concetto di coppia di variabili aleatorie, cioè: 

$$
\left(X _ {1}, \dots , X _ {n}\right): \omega \in \Omega \Longrightarrow \boldsymbol {X} (\omega) = \left(X _ {1} (\omega), \dots , X _ {n} (\omega)\right) \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {n} \subseteq \mathbb {R} ^ {n}
$$

- Un vettore aleatorio si ottiene quindi facilmente come 

$$
\boldsymbol {X} (\omega) = \left[ X _ {1} (\omega), \dots , X _ {n} (\omega) \right] ^ {T} \in \mathcal {X} _ {1} \times \dots \times \mathcal {X} _ {n} \subseteq \mathbb {R} ^ {n}
$$

- Se gli alfabeti $\mathcal { X } _ { 1 } , \ldots \mathcal { X } _ { n }$ sono discreti, il vettore è discreto e si caratterizza mediante la DF congiunta; 

$$
p _ {\mathcal {X}} (\boldsymbol {x}) = p _ {\mathcal {X}} \left(x _ {1}, \dots , x _ {n}\right) = \mathbb {P} \left\{X _ {1} = x _ {1}, \dots , X _ {n} = x _ {n} \right\} \forall \space \boldsymbol {x} \in \mathcal {X} _ {1} \times \dots \mathcal {X} _ {n}
$$

dove $\pmb { x } = [ x _ { 1 } , \dots , x _ { n } ] ^ { T } \in \mathcal { X } _ { 1 } \times \dots \mathcal { X } _ { n }$ 

- Per alfabeti continui, avremo 

$$
F _ {\boldsymbol {X}} (\boldsymbol {x}) = \mathbb {P} \left\{X _ {1} \leq x _ {1}, \dots , X _ {n} \leq x _ {n} \right\} \forall \space \boldsymbol {x} \in \mathbb {R} ^ {n} \quad f _ {\boldsymbol {X}} (\boldsymbol {x}) = \frac {\partial^ {n} F _ {\boldsymbol {X}} (\boldsymbol {x})}{\partial x _ {1} \dots \partial x _ {n}}
$$

dove $\pmb { x } = [ x _ { 1 } , \dots , x _ { n } ] ^ { T } \in \mathbb { R } ^ { n }$ 

## Legge di Bayes per vettori aleatori

- Consideriamo un vettore aleatorio discreto con pmf $p _ { X } ( { \pmb x } )$. Sappiamo che la **Legge di Bayes** assicura che 

$$
\mathbb {P} (A \cap B) = \mathbb {P} (A | B) \mathbb {P} (B)
$$

- Posto $A = \{ X _ { n } = x _ { n } , \ldots , X _ { 2 } = x _ { 2 } \} \textsf { e } B = \{ X _ { 1 } = x _ { 1 } \}$ avremo 

$$
p _ {\boldsymbol {X}} (\boldsymbol {x}) = \mathbb {P} \left\{X _ {n} = x _ {n}, \dots , X _ {2} = x _ {2} | X _ {1} = x _ {1} \right\} \mathbb {P} \left\{X _ {1} = x _ {1} \right\}
$$

- Iterando il ragionamento avremo la regola della catena: 

$$
\begin{array}{c} p _ {X} (x) = \mathbb {P} \{X _ {1} = x _ {1} \} \mathbb {P} \left\{X _ {2} = x _ {2} | X _ {1} = x _ {1} \right\} \dots \mathbb {P} \left\{X _ {n} = x _ {n} | X _ {n - 1} = x _ {n - 1}, \ldots , X _ {1} = x _ {1} \right\} \\ = \prod_ {i = 1} ^ {n} p _ {X _ {i} | X _ {i - 1}, \ldots , X _ {1}} (x _ {i} | x _ {i - 1}, \ldots , x _ {1}), \qquad p _ {X _ {1} | X _ {0}} (x _ {1} | x _ {0}) = p _ {X _ {1}} (x _ {1}) \end{array}
$$

- Analogamente, per vettori continui avremo 

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \prod_ {i = 1} ^ {n} f _ {X _ {i} | X _ {i - 1}, \dots , X _ {1}} (x _ {i} | x _ {i - 1}, \dots , x _ {1})
$$

## Processi aleatori tempo-discreti

Si definisce **processo aleatorio tempo-discreto** un’applicazione che ad ogni elemento dello spazio campione fa corrispondere una successione:

$$
X: \omega \in \Omega \longrightarrow \{X (n, \omega) \} _ {n \in \mathbb {Z}}
$$

dove $\mathbb{Z}$ indica l’insieme degli interi.

> [!example] Esempio 1 (Realizzazioni di un processo tempo-discreto)
> Di seguito sono riportate tre realizzazioni di un processo tempo-discreto.
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/7e76ee276ef5ef4aa0a28d11f4fc129e3b4bfc5e7363b6e3ebb01def91168f7a.jpg)
> Figura 1: Realizzazione 1
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/eef731154ce7b72b160d3d277cbe6b34a0a3867f94f145234edd9dd15d98f5db.jpg)
> Figura 2: Realizzazione 2
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/057411ab0f31edbb00e115bfa3816d1d5e5f1c3faed5ab464cbf318ca0bb423a.jpg)
> Figura 3: Realizzazione 3

## Commenti e osservazioni

- Per ogni valore di $\omega \in \Omega$ il processo si realizza in una sequenza che assume valori nell’intervallo $[-1, 1]$;
- Fissando l’istante di tempo $n = n _ { 0 }$ e facendo variare $\omega \in \Omega$ otteniamo $X ( n _ { 0 } , \omega )$ che è una variabile aleatoria (visto che ”campionando verticalmente” il processo otteniamo che al variare di $\omega X ( n _ { 0 } , \omega )$ assume diverse determinazioni);
- La variabile aleatoria $X ( n _ { 0 } , \omega )$ ha una sua pdf, che in genere dipende da $\omega ;$;
- Se la pdf non dipende dall’istante di campionamento $\boldsymbol { n _ { 0 } }$, il processo si dice **stazionario al primo ordine**.
- Nel caso mostrato in figura, il processo è stato generato assumendolo stazionario e marginalmente uniforme in $[ - 0 . 5 , 0 . 5 ]$, cioè:

$$
f _ {X (n)} (x; n) = f _ {X (n)} (x) = \Pi (x - 0. 5)
$$

> [!quote] Osservazione
> Si noti che siccome
> 
> $$
> \mathbb {E} [ X (n) ] = \int_ {- \infty} ^ {\infty} x f _ {X (n)} (x; n) d x = \int_ {- 0, 5} ^ {0, 5} x \Pi (x - 0. 5) d x = 0
> $$
> 
> il processo è a media identicamente nulla.

## Un altro esempio: processo Gaussiano tempo-discreto

Come secondo esempio, consideriamo un processo tempo-discreto stazionario al primo ordine con pdf:

$$
f _ {X (n)} (x) = \frac {1}{\sqrt {2 \pi}} \exp \left[ - \frac {(x + 0 . 5) ^ {2}}{2} \right]
$$

quindi con densità marginale Gaussiana a media $-0.5$ e varianza unitaria. Otteniamo realizzazioni del tipo rappresentate in figura:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/48a5eafdb76a91cfaeec049306e38b42c43e3516620a31cd0a3e5059967ed7ab.jpg)
Figura 4: Realizzazione Gaussiana 1

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/51684a9d1e2c1908853f9b305d6cbfc31882599c788d4ca54497b82c5cfb42be.jpg)
Figura 5: Realizzazione Gaussiana 2

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/2c12f75b390651df009e373f8c5f9758ea1925d2f1a52f06939bfdc2260a96eb.jpg)
Figura 6: Realizzazione Gaussiana 3

## Caratterizzazione del secondo ordine del processo

- Un processo aleatorio si dice **caratterizzato al primo ordine** se ne è nota la pdf $f _ { X ( n ) } ( x ; n )$ per ogni $n$. Se il processo è stazionario al primo ordine, questo equivale ad assegnare un’unica pdf.
- Un processo aleatorio si dice **caratterizzato al secondo ordine** se ne è assegnata la pdf congiunta:

$$
f _ {X (n _ {1}), X (n _ {2})} \big (x _ {1}, x _ {2}; n _ {1}, n _ {2} \big), \quad \forall \space n _ {1}, n _ {2}
$$

- Un processo aleatorio si dice **stazionario al secondo ordine** se, per qualsiasi intero $h$, abbiamo:

$$
f _ {X (n _ {1}), X (n _ {2})} (x _ {1}, x _ {2}; n _ {1}, n _ {2}) = f _ {X (n _ {1} + h), X (n _ {2} + h)} (x _ {1}, x _ {2}; n _ {1}, n _ {2} + h)
$$

- In altre parole, un processo stazionario al secondo ordine è tale che la caratterizzazione congiunta di due suoi campioni dipende unicamente dalla loro ”distanza” temporale, ma non dalla loro posizione: in altre parole, la pdf congiunta è invariante ad atti di moto rigido dei due punti in anticipo o in ritardo.
- Ovviamente un processo stazionario al secondo ordine lo è anche al primo, ma non è vero il viceversa. Perchè?

## Caratterizzazione completa di un processo

Un processo aleatorio $X ( n )$ si dice **completamente caratterizzato** se, detto $M$ un intero arbitrario e detti $n _ { 1 } , \ldots , n _ { M }$ $M$ istanti arbitrari, il vettore aleatorio:

$$
\boldsymbol {X} = [ X (n _ {1}), \dots , X (n _ {M}) ] ^ {T}
$$

ha densità di probabilità $f _ { \pmb { X } } ( x _ { 1 } , \ldots , x _ { M } )$ nota.

Un processo aleatorio si dice **stazionario in senso stretto di ordine $M$** se la sua densità di probabilità di ordine $M$ è invariante per traslazione, cioè:

$$
\begin{array}{c} f _ {X (n _ {1}), \ldots , X (n _ {M})} (x _ {1}, \ldots , x _ {M}; n _ {1}, \ldots , n _ {M}) = \\ f _ {X (n _ {1} + h), \ldots , X (n _ {M} + h)} (x _ {1}, \ldots , x _ {M}; n _ {1} + h, \ldots , n _ {M} + h) \end{array}
$$

- Un processo stazionario di ordine $M$ lo è di qualunque ordine $i \leq M$;
- Un processo si dice **indipendente** (o a campioni indipendenti) se, comunque si scelga un intero $M$, il vettore $\pmb { X } = [ X ( n _ { 1 } ) , \dots , X ( n _ { M } ) ] ^ { T }$ è costituito da variabili aleatorie indipendenti, cioè:

$$
f _ {X (n _ {1}), \dots , X (n _ {M})} (x _ {1}, \dots , x _ {M}) = f _ {X (n _ {1})} (x _ {1}) f _ {X (n _ {2})} (x _ {2}) \dots f _ {X (n _ {M})} (x _ {M}) = \prod_ {i = 1} ^ {M} f _ {X (n _ {i})} (x _ {i})
$$

## Processi discreti

Si definisce **processo ampiezza discreto** (o - per brevità - **processo discreto**) un processo aleatorio in cui le cui realizzazioni siano sequenze di numeri che possano assumere valore in un alfabeto discreto.

Un caso di importanza notevole è quello di un **processo indipendente binario**, $X ( n ) \in \{ - 1 , 1 \}$, con $\mathbb { P } \left\{ X ( n ) = 1 \right\} = \mathbb { P } \left\{ X ( n ) = 1 \right\} = { \frac { 1 } { 2 } }$, di cui le realizzazioni sono riportate in figura, anche detto **Processo di Bernoulli**.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/62faba250dc710ba5cb9fbd4a331bfdc4d2dc4cd5d3bd696b38454e5f14bc19a.jpg)
Figura 7: Realizzazioni del processo di Bernoulli

## Un altro esempio: Un processo quaternario

Un ulteriore esempio si ha considerando un **alfabeto quaternario**, per esempio $X ( n ) \in \{ - 2 , - 1 , 1 , 2 \}$, con livelli equiprobabili (per cui ${ \mathbb { P } } \left\{ X ( n ) = i \right\} = { \textstyle { \frac { 1 } { 4 } } } \ \forall \space i )$).

Le realizzazioni del processo saranno quindi del tipo rappresentato in figura:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9f7957aa1d5176320b74eb7c6ea5945937ed809d0cfc9354252211d9f644fc02.jpg)
Figura 1: Realizzazioni di un processo quaternario.

## Caratterizzazione di processi discreti

Tutte le definizioni introdotte per i processi continui si estendono ai **processi discreti**, con la sola differenza che le densità di probabilità sono ora sostituite dalle **funzioni di massa di probabilità** (DF).

> [!theorem] Definizione: Funzione di Massa di Probabilità (DF)
> Intuitivamente, la DF indica la probabilità che una variabile aleatoria discreta assuma un valore specifico. Ad esempio, in un lancio di un dado, la DF assegna $1/6$ a ogni numero da 1 a 6.
>
> Formalmente, per una variabile aleatoria discreta $X$, la funzione di massa $p(x)$ è definita come:
> $$p(x) = P(X = x)$$

Un processo discreto si dice **stazionario in senso stretto** se, comunque si scelga un intero $M$, il vettore aleatorio $\pmb { X } = [ X ( n _ { 1 } ) , \dots , X ( n _ { M } )$ gode, per un $h$ arbitrario, della proprietà:

$$
\begin{array}{c} \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2}, \ldots X (n _ {M}) = x _ {M} \right\} \qquad = \\ \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2}, \ldots X (n _ {M} + h) = x _ {M} \right\} \end{array}
$$

Ovviamente, la stazionarietà di ordine $M$ implica quella di ogni ordine $\leq M$. In particolare, un processo stazionario ha una DF marginale indipendente dal tempo.

Un processo discreto che sia stazionario e indipendente gode ovviamente della proprietà:

$$
\mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2}, \dots X (n _ {M}) = x _ {M} \right\} = \prod_ {i = 1} ^ {M} \mathbb {P} \left\{X (n _ {i}) = x _ {i} \right\} = \prod_ {i = 1} ^ {M} p _ {X} (x _ {i})
$$

dove $p _ { X } ( \cdot )$ è la DF marginale (ovviamente indipendente dal tempo).

## Caratterizzazione sintetica dei vettori aleatori

Come per le variabili aleatorie, anche per i processi aleatori è possibile — a fronte di un’impossibilità di fornirne una caratterizzazione completa — definire una **caratterizzazione sintetica**, cioè assegnarne statistiche che siano significative.

In modo del tutto analogo al caso scalare, dove abbiamo visto che la coppia media-varianza $( \mu x , \sigma _ { X } ^ { 2 } )$ offre spesso importanti informazioni sul comportamento della variabile $X$, e al caso delle coppie, in cui la cinquina $( m u _ { X } , \sigma _ { X } , \mu _ { Y } , \sigma _ { Y } , \mathrm { C O V } ( X , Y )$ offre analoghe informazioni sulla coppia $(X, Y)$, per un vettore aleatorio $\pmb { X } = [ X _ { 1 } , \ldots , X _ { n } ] ^ { T }$ abbiamo:

###1 La media statistica
$$
\boldsymbol {\mu} _ {\boldsymbol {X}} = \left(\mathbb {E} \left[ X _ {1} \right], \dots , \mathbb {E} \left[ X _ {n} \right]\right) ^ {T}
$$

###2 La matrice di covarianza
La **matrice di covarianza**, $C _ { X } = \mathbb { E } \left[ \left( X - \mu _ { X } \right) \left( X - \mu _ { X } \right) ^ { T } \right]$, è definita come:

$$
\left( \begin{array}{c c c c} \sigma_ {X _ {1}} ^ {2} & \operatorname{COV} (X _ {1}, X _ {2}) & \dots & \operatorname{COV} (X _ {1}, X _ {n}) \\ \operatorname{COV} (X _ {2}, X _ {1}) & \sigma_ {X _ {1}} ^ {2} & \dots & \operatorname{COV} (X _ {2}, X _ {n}) \\ \dots & \dots & \dots & \dots \\ \operatorname{COV} (X _ {n}, X _ {1}) & \operatorname{COV} (X _ {n}, X _ {2}) & \dots & \sigma_ {X _ {n}} ^ {2} \end{array} \right)
$$

## Processi Stazionari in Senso Lato (SSL)

Focalizziamoci sui processi tempo discreti, ma quanto verrà detto vale anche per i processi tempo-continui. Abbiamo visto che un processo $X ( n ) \in { \mathcal { X } }$ è stazionario di ordine 2 se:

$$
\mathbb {P} \left\{X (n) = x \right\} = p _ {X} (x) \quad \forall \space x \text {e} \quad \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2} \right\} = \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2} \right\}
$$

Ovviamente la media $\begin{array} { r } { \mu _ { X } = \operatorname { \mathbb { E } } \left[ X ( n ) \right] = \sum _ { x \in \mathcal { X } } x p _ { X } ( x ) } \end{array}$ non dipende da $n ;$. Inoltre si noti che:

$$
\mathbb {E} \left[ X (n _ {1}) X (n _ {2}) \right] = \sum_ {x _ {1} \in \mathcal {X}} \sum_ {x _ {2} \in \mathcal {X}} x _ {1} x _ {2} \mathbb {P} \left\{X (n _ {1}) = x _ {1}, X (n _ {2}) = x _ {2} \right\} =
$$
$$
\mathbb {E} \left[ X (n _ {1} + h) X (n _ {2} + h) \right] = \sum_ {x _ {1} \in \mathcal {X}} \sum_ {x _ {2} \in \mathcal {X}} x _ {1} x _ {2} \mathbb {P} \left\{X (n _ {1} + h) = x _ {1}, X (n _ {2} + h) = x _ {2} \right\}
$$

Ciò significa che $\mathbb { E } \left[ X ( n _ { 1 } ) X ( n _ { 2 } ) \right]$ è funzione di $n _ { 2 } - n _ { 1 }$, ma non separatamente di $\boldsymbol { n } _ { 1 } \in \boldsymbol { n } _ { 2 }$.

Un processo $X ( n / t )$, continuo o discreto, non necessariamente stazionario al secondo ordine, si dice **stazionario in senso lato** se:

- La sua media non dipende dal tempo;
- La sua autocorrelazione soddisfa la condizione:

$$
R _ {X} \left(t _ {1} / n _ {1}, t _ {2} / n _ {2}\right) = \mathbb {E} \left[ X \left(t _ {1} / n _ {1}\right) X \left(t _ {2} / n _ {2}\right) \right] = R _ {X} \left(t _ {2} - t _ {1} / n _ {2} - n _ {1}\right)
$$

## Matrice di covarianza per processi SSL

Sia $X ( t / n )$ un processo SSL, continuo o discreto, e sia $\pmb { x } = [ X _ { 1 } , \ldots , X _ { M } ] ^ { T }$ un vettore aleatorio $M$-dimensionale di campioni di $X ( t / n )$, presi negli istanti $( t _ { 1 } , \dots , t _ { M } ) / ( n _ { 1 } , \dots , n _ { M } )$.

Ovviamente avremo che $\pmb { \mu } = \mathbb { E } \left[ \pmb { X } \right] = \mu \mathbf { 1 }$, con $\mu$ scalare e $1$ un vettore $M$-dimensionale di tutti $" \bf { 1 } ^ { \prime \prime }$.

Inoltre, avremo, per la condizione SSL:

$$
\mathbb {E} \left[ X _ {i} X _ {j} \right] = f (| i - j |) \quad \mathbb {E} \left[ X _ {i} ^ {2} \right] = \overline {{X ^ {2}}}, \operatorname{Var} (X _ {i}) = \overline {{X ^ {2}}} - \mu^ {2} = \sigma_ {X} ^ {2}
$$

Per cui, definendo $\begin{array} { r } { \rho _ { i , j } = \frac { \mathrm { C O V } ( X _ { i } , X _ { j } ) } { \sigma _ { X } ^ { 2 } } } \end{array}$ la matrice di covarianza assume la forma:

$$
\boldsymbol {C} _ {\boldsymbol {X}} = \sigma_ {\chi} ^ {2} \left( \begin{array}{c c c c c} 1 & \rho_ {1, 2} & \rho_ {1, 3} & \dots & \rho_ {1, M} \\ \rho_ {1, 2} & 1 & \rho_ {2, 3} & \dots & \rho_ {2, M} \\ \dots & \dots & \dots & \dots & \dots \\ \rho_ {1, M} & \rho_ {2, M} & \rho_ {3, M} & \dots & 1 \end{array} \right)
$$

Pertanto, la matrice di covarianza di un vettore tratto da un processo SSL è simmetrica.

> [!quote] Osservazione
> Se il passo di campionamento del processo è costante (cioè, $( t _ { i + 1 } - t _ { i } ) / ( n _ { i + 1 } - n _ { i } )$ costante $\forall \space i ,$), allora la matrice assume una forma di **Toeplitz**.

## Esercizio: La matrice di covarianza è sempre definita non-negativa

> [!example] Esercizio 1
> Si dimostri che la **matrice di covarianza** è una matrice definita non negativa.
>
> *Suggerimento: Considerare il prodotto scalare tra un vettore e la matrice applicato a un vettore arbitrario.*

Si ricorda che una matrice $A \in \mathbb{R}^{M \times M}$ è definita non negativa se, detto $x \in \mathbb{R}^M$ un qualunque vettore $M$-dimensionale risulta $x^T A x \geq 0$.

Consideriamo un vettore aleatorio $M$-dimensionale $X$ di media $\mu$ e matrice di covarianza $\Sigma$. La quantità $X^T \Sigma X$ è ovviamente una variabile aleatoria scalare con $\mathbb{E}[X^T \Sigma X] = \text{tr}(\Sigma \Sigma^T)$. Inoltre,

$$
\mathbb{E}[(X-\mu)^T \Sigma (X-\mu)] = \mathbb{E}[\sum_{i=1}^M \sum_{j=1}^M (X_i - \mu_i) \Sigma_{ij} (X_j - \mu_j)]
$$

Avremo allora la catena di disuguaglianze:

$$
\mathbb{E}[(X-\mu)^T \Sigma (X-\mu)] = \sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij} \mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)]
$$

$$
= \sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij} \Sigma_{ij} = \sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij}^2 \geq 0
$$

dove si è sfruttato il fatto che $\mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)] = \Sigma_{ij}$.

## Estensione ai processi continui: definizioni

Quanto detto sui processi ampiezza-discreti si estende ai processi ampiezza continui. Detto $X(t)$ tratto da un processo stazionario, la sua caratterizzazione implica l’assegnazione di una delle due funzioni:

$$
\mu(t) = \mathbb{E}[X(t)]
$$

$$
R(t_1, t_2) = \mathbb{E}[X(t_1)X(t_2)]
$$

dove $\mu(t)$ è la media e $R(t_1, t_2)$ è la funzione di autocorrelazione.

Ovviamente le definizioni di stazionarietà in senso lato e in senso stretto si estendono tal quali ai processi ampiezza continui.

## Un esempio: Processi Gaussiani

Un processo $X(t)$ si dice **Gaussiano** se un qualunque suo campione di dimensione $M$ definisce un vettore aleatorio $X$ Gaussiano.

Dato un vettore aleatorio $X$ con media e matrice di covarianza assegnati:

$$
\begin{cases} \mathbb{E}[X] = \mu \\ \text{Cov}(X) = \Sigma \end{cases}
$$

questo si dice Gaussiano se la sua pdf si scrive nella forma

$$
f(x) = \frac{1}{\sqrt{(2\pi)^M |\Sigma|}} \exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)\right)
$$

dove $|\Sigma|$ denota il determinante della matrice di covarianza.

## Proprietà dei processi Gaussiani

- La stazionarietà in senso lato implica quella in senso stretto. Si verifichi questo asserto ricordando che nel caso di stazionarietà in senso lato la matrice di covarianza ha struttura **Toeplitz**.
- Chiusura rispetto a trasformazioni lineari. Se $X$ è un vettore Gaussiano, $X \sim \mathcal{N}(\mu, \Sigma)$, allora, avremo

$$
AX + b \sim \mathcal{N}(A\mu + b, A\Sigma A^T)
$$

- Per un processo Gaussiano, incorrelazione implica indipendenza. Infatti, un processo incorrelato ha matrice di covarianza $\Sigma = \text{diag}(\sigma_1^2, \dots, \sigma_M^2)$. Sostituendo nella espressione di una pdf Gaussiana abbiamo

$$
f(x) = \prod_{i=1}^M \frac{1}{\sqrt{2\pi\sigma_i^2}} \exp\left(-\frac{(x_i-\mu_i)^2}{2\sigma_i^2}\right)
$$

## Tipi di convergenza

Sia $X_n$ una successione di variabili aleatorie con densità $f_n(x)$. Ci chiediamo come definire la convergenza di tale successione a un dato limite, sia esso $X$.

Ovviamente la forma più forte di convergenza è quella puntuale, vale a dire - ricordando che le variabili aleatorie sono in realtà funzioni - $P(\lim_{n \to \infty} X_n = X) = 1$, dove $\Omega$ lo spazio dei campioni dello spazio di probabilità sottostante.

Altre forme di convergenza più ”deboli” (con diversa gradazione) sono:
- La convergenza in distribuzione;
- La convergenza in probabilità;
- La convergenza in media quadratica;
- La convergenza quasi certa (o con probabilità 1).

## Convergenza in distribuzione

La successione $X_n$ si dice convergente in distribuzione alla variabile $X$ (e si scrive $X_n \xrightarrow{d} X$) se

$$
\lim_{n \to \infty} F_n(x) = F(x)
$$

dove l’uguaglianza vale in tutti gli insiemi di continuità di $F(x)$.

> [!theorem] Teorema (*Continuous Mapping*)
> Se $g$ è una funzione continua, allora si ha:
>
> $$
> X_n \xrightarrow{d} X \implies g(X_n) \xrightarrow{d} g(X)
> $$

> [!theorem] Teorema (*Continuità di Levy*)
> Definendo la funzione generatrice dei momenti (moment generating function, mgf)
>
> $$
> M_X(s) = \mathbb{E}[e^{sX}]
> $$
>
> per i valori di $s$ per cui l’integrale esiste, la convergenza puntuale di $M_{X_n}(s)$ a $M_X(s)$ implica $X_n \xrightarrow{d} X$ e viceversa.

## La funzione generatrice dei momenti

La **funzione generatrice dei momenti** (moment generating function, mgf) di una variabile aleatoria gode di alcune rilevanti proprietà. 

> [!quote] Proprietà di continuità
> Si nota che 
>
> $$
> \Phi_ {X} (s) = \int_ {\mathbb {R}} e ^ {s t} f _ {X} (t) d t, \text {   con   } f _ {X} \text {   sommabile }
> $$
>
> è funzione continua di $s$ nei punti in cui l’integrale esiste. 

Analogamente, si può facilmente verificare che: 

> [!theorem] Derivabilità della mgf
> Purché i momenti di ordine $r$ esistano, vale:
>
> $$
> \Phi_ {X} (0) = 1 \quad \Phi^ {\prime} (0) = \mathbb {E} [ X ] \quad \Phi_ {X} ^ {\prime \prime} (0) = \mathbb {E} [ X ^ {2} ] \dots \Phi_ {X} ^ {(r)} (0) = \mathbb {E} [ X ^ {r} ]
> $$

Pertanto, nelle condizioni precedenti, la mgf ammette il seguente sviluppo in serie di **MacLaurin**:

> [!example] Sviluppo in serie della mgf
> $$
> \Phi_ {X} (s) = \sum_ {n = 0} ^ {\infty} \frac {\mathbb {E} [ X ^ {n} ]}{n !} s ^ {n}
> $$
>
> Questo sviluppo spiega la denominazione di "mgf" (moment generating function), poiché i coefficienti della serie sono direttamente correlati ai momenti della variabile aleatoria.

---

