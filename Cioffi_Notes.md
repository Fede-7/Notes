
## LEZIONE 1

## INSIEMI

Un insieme è una collezione di oggetti. I suoi elementi possono essere rappresentati con i diagrammi di ven, per elencazione o per caratteristica. 

Consideriamo: 

X = 1 Studente × | X sta in aula A6 4 

y = { student y | y sta in aula AG } 

Passiamo eseguire diverse operazioni: 

X n y (intersezione) = elem. che ∈ almeno in uno dei 2 insieme 

x ∪ y (unione) = elem. che ∈ sia ad x che y 

x \ y (differenza) = elem. che € ad x me non y 

## PRODOTTO CARTESIANO

$$
\text {   inoltre   se   } A \neq B \text {   allora   } A \times B \neq B \times A
$$

## RELAZIONI

Siano A≠∅ e B≠∅ una relazione di A e B e- un sottoinsieme R del prodotto cartesiano AxB 

$$
R = \{(a, x), (a, y), (c, y) \}
$$

## RELAZIONI INVERSE

Siano $A \neq  \varnothing ,B \neq  \varnothing$ e $R \subseteq  A \times  B$ . se $R\overline{e}$ una relazione fra $A \in  B$ ,dicremo RELAZIONE INVERSA di $R$ la rela-

$$
\{(b, a) \in B \times A \setminus (a, b) \in R 4
$$

$$
E s e r p i o: \text { consideriamo } R = f (a, x), (z, y), (c, y) \} \text { possiamo   dire } R ^ {- 1} = f (x, z), (y, a), (y, c) \}
$$

## RELAZIONE D'EQUIVALENZA

Una relazione di A in se e' detta RELAZIONE BINARIA. 

Sia R una relazione binaria sull'insieme A allora: 

- R si dice Riflessiva se ¥×£A, ×R× 

- R si dice SIMMETRICA se ∀x,y∈A , x Ry allora yRx 

- R si dice TRANSITIVA se ∀x,y,z ∈ A , xRy ∩ yRz =D xRz 

Una relazione binaria R sull'insieme A si dice di equivalenza se e contemporaneamente 

Riflessiva, Simmetrica, Transitiva. 

$$
A = \{a, b, c \} R = \{(a, a), (b, b), (c, c), (b, c), (c, b) \} e ^ {- u n a r e l. d ^ {\prime} e q u i v.}
$$

$$
R _ {1} = \{(a, a), (b, b), (a, b), (b, a) \} \leftarrow \text { non   e   -   riflessiva.   None   d'equiv. }
$$

## CLASSI D'EQUIVALENZA

Supponiamo di avere un insieme A≠∅ e R rel. d'equiv. su A, se a ∈ A dicemo 

classe d'equivalenza di A l'insieme; 

$$
[ a ] = \{x \in A | x R a \}
$$

ogni elemento di una classe d'equivalenza si dice RAPPRESENTANTE della sua classe 

$$
\underline {{\mathrm{Dim}}} a \in [ a ] \Leftrightarrow a R a \Leftrightarrow (a, a) \in R
$$

$$
\text {   ii)   } b \in [ a ] \Rightarrow [ b ] = [ a ]
$$

Dim ⊆ se be [a] allora bRq. 

$$
\text { sia } \times \varepsilon [ b ] \text { allora } \times B b.
$$

×Rb ∩ bRa per transitivity ×Ra quindi ×ε[a] 

$$
2 [ b ] \leq [ a ] \text { per   simmetria   si   dimostra   che } [ a ] \leq [ b ] \text { e   quindi } [ b ] = [ a ]
$$

$$
\text { iii) } [ a ] \cap [ b ] \neq \phi \Rightarrow [ a ] = [ b ]
$$

DIM Supponiamo ×ε[a]n[b] dunque ×ε[a]e ×ε[b] quindi [x]=[a] e [x]=[b] 

L'insieme C e detto INSIEME QUOZIENTE ed e una partizione di A di [a] in C 

Indichiamo con F l'insieme dei punti dello spazio della geometria elementare . Gli elementi 

di FxF si dicono vettori applicati oppure segmeni orientati , essi sono caratterizzati da intensità , 

Siano A, B ≠ ∅ diremo applicazione o funzione di Ain B è una relazione F ⊆ A×B tale che:
∀a ∈ A J! b ∈ B: a F b 

## LEZIONE 2

APPLICAZIONI SURR. INIETT. BIETT. 

$$
\text {   Sia   } f: A \rightarrow B \quad \text {   con   } A, B \neq \phi
$$

$$
F e ^ {\prime} \text {   iniettiva   } \Leftrightarrow \forall a, a ^ {\prime} \in A \text {   se   } a \neq a ^ {\prime} \text {   allora   } F (a) \neq F (a ^ {\prime})
$$

dunque a elementi distinti corrispondono immagini distinte 

$$
f \text {   e   } \text {   surriettiva   } \Longleftrightarrow \text {   Im   } F = B \quad \text {   cioe   :   } \quad \forall b \in B, \exists a \in A: F (a) = b
$$

$$
F e ^ {-} b i e t t i v a \iff \forall b \in B F! a \in A: f (a) = b
$$

inoltre possiamo dire che F: A → B e biettiva ⇔ F⁻¹ e un applicazione e a 

INSIEMI EQUIPOTENTI 

$$
\text { Siano } A \neq \phi , B \neq \phi
$$

A e B si dicono equipotenti $\Leftrightarrow$ ∃ un app. f: A→B biettiva 

$$
F (x) = \{f (x) | x \in X \} \Rightarrow (\mathrm{insieme~delle~immagini})
$$

Supponendo adesso y sottoinsieme di B diremo controimmagine di y Pinsieme: 

$$
F ^ {1} (y) = \{a \in A | F (a) \in y \}
$$

INSIEME DELLE PARTI 

Sia S un insieme $P(S) = \{ |x| \leq S \}$ e' pinsieme delle parti di S. Esso e' ≠ φ poiche Φ ∈ P(S). 

Appartiene sempre a P(s) dunque è un elemento di P(s) 

$$
P (S) \mathrm{e} ^ {-} \mathrm{un} \mathrm{singleton} \Leftrightarrow S = \varnothing
$$

P(s) se S ha n elementi, avra-2" elementi. 

FUNZIONE COMPOSTA 

Consideriamo le app F: A → B e g: B → C chiamenteo composta l'applicazione gof: A → C 

$$
\text {   definita   } \forall a \in A: (g o P) (a) = g (\tilde {F} (a))
$$

$$
a \times x \sim 2 \Rightarrow a \sim 2
$$

$$
b \sim y \sim 3 = 0 b \sim 3
$$

$$
C = \{1, 2, 3, 4 \}
$$

$$
c \sim y \sim 3 = 0 c \sim 3
$$

Si noti che se abbiamo F: A → A e g: A → A allora sia gof che Fog vanno da A in A, pero in generale 

## APPLICAZIONI INVERTIBILI

Sia un'appli. F: A → B se 3 un'applicazione F': B → A : F'o F = idA e fo F' = idB allora fe invertib 

PROP: Un'applicazione F: A→B e invertibile <=> e biettiva. In tal caso abbiamo che la relazione inversa f'è 

PROP: Se A e' finito e ha esattamente n elementi allora A e' equipotente all' insieme {1, ..., n} 

## RESTRIZIONE

Consideriamo un'applicazione f.A-8. Per ogni X sottoinsieme di A (x ≤ A) possiamo considerare la restrizione di 

## Princi Pio D'induzione

Data, ∀n, un'affermazione A(n) se succede che: 

$$
1) \exists \bar {n} \in I N: A (\bar {n}) e ^ {-} v e r a (b a s e d ^ {\prime} i n d u z i o n e)
$$

$$
\text { Se   sono   vere   base   e   passo   allora } A (n) \in v a \forall n \geq \bar {n}
$$

$$
b = 0 \quad A = \varnothing \quad | A | = 0
$$

$$
P (A) = \{0 \} \quad | P (A) | = 1 = 2 ^ {\circ}
$$

$$
A _ {n + 1} = \{a _ {1}, \dots , a _ {n}, a _ {n + 1} \} \quad | P (A _ {n + 1}) | = 2 ^ {n + 1},
$$

$$
P (A _ {n + 1}) = P (A _ {n}) \cup \{x \cup \{a _ {n + 1} \} | x \in P (A _ {n}) \}
$$

$$
A _ {n} = 3 a _ {1}, \dots , a _ {n} \} \quad | P (A _ {n}) | = 2 ^ {n}
$$

$$
| P (A _ {n + 1}) | = 2 ^ {n} + 2 ^ {n} = 2 ^ {n + 1}
$$

$$
\text { OPERAZIONE   BINARIA }
$$

Siano A,B,C ≠∅ un applicazione ⊥A×B→C si dice operazione binaria. 

$$
\mathrm{Se} A = B = C \quad \mathrm{allora} \quad \mathrm{parleremo} \mathrm{di} \quad \mathrm{operazione} \quad \mathrm{interna}
$$

$$
\text { Se   invece   B - C   allora   si   parla   di   operazione   esterna   con   operatori   in   A }
$$

## LEZIONE 3

## STRUTTURE ALGEBRICHE

e' una n-upla costituita da insiemi e operazioni su di essi 

ESEπPIO: (IN,+)(R>0,·) 

Una struttura algebrica costituita da un insieme e da un'operazione interna su tale insieme e detta 

gruppoide. Se abbiamo un gruppoide (A,⊥) ha senso considerare le seguenti proprieta' per la 

Sua operazione interna: 

(i) l'operaz. ⊥ e^{- associativa} se 

$$
\forall a, b, c \in A (a \bot b) \bot c = a \bot (b \bot c)
$$

$$
\forall a, b \in A \quad a \bot b = b \bot a
$$

(iii) un elemento y∈A si dice neutro se ∀a∈A 

(iv) se ⊥ ammette elem. neutro, possiamo chiedere: 

$\forall a \in A, \exists a' \in A: a \perp a' = a' \perp a = \mu$ elem neutro 

In tal caso a è detto invertibile e al si diae inverso o simmetrico 

## GRUPPO

Un gruppoide si dice gruppo se l'operazione e' associativa, ammette elem. neutro, ogni elem è 

invertibile. Se l'operazione e anche commutativa allora si parla di gruppo abeliano. 

## CAMPO

Sia $1k$ un insieme $e + ,\cdot$ due operazioni binarie interne su $1k$ . La struttura algebrica $(1k, + ,)$ e' detta campo se: 

(i) $(K_1+) e^{-}$ un gruppo abeliano 

(ii) se 0 e' l'elem. neutro di (K, +) e K* = K/104 allora (K*, $\cdot$ ) e' un gruppo abeliano 

(iii) il prodotto e' distributivo rispetto alla somma cioè: 

$$
\forall a, b, c \in K (a + b) \cdot c = a \cdot c + b \cdot c
$$

$$
a \cdot (b + c) = a \cdot b + a \cdot c
$$

## SPAZI VETTORIALi

$$
\text {   Sia   } V \neq \phi \text {   e   sia   } (K, +,.) \text {   campo   }
$$

Siano: ☐: V×V → un'operaz. interna su V 

$$
\square : K \times V \rightarrow V \text { un'opera   zione   esterna }
$$

Allora (V₁ + , .) si dice spazio vettoriale sul campo k se 

(i) $(V_1+)$ e'un gruppo abeliano, l'elem.neutto si indica con 

$$
(i i) \forall \alpha \in K, \forall u, v \in V \quad \alpha \cdot (u + v) = (\alpha \cdot u) + (\alpha \cdot v)
$$

$$
(i i i) \forall \alpha , \beta \in K, \forall u \in V (\alpha + \beta) \cdot u = (\alpha \cdot u) + (\beta \cdot u)
$$

$$
(i v) \forall \alpha , \beta \in K, \forall u \in V (\alpha \cdot B) \cdot u = \alpha \cdot (\beta \cdot u)
$$

$$
(v) \text {   Sia   1   rispetto   alla   moltiplicazione   di   } K \quad \forall u \in V, 1 \cdot u = u
$$

$$
(K, +, \cdot) _ {\text { campo }}
$$

$$
+: K [ x ] \times K [ x ] \rightarrow K [ x ]
$$

$$
K [ x ] = \{a _ {0} + a _ {1} x + \dots + a _ {n} x ^ {n} | a _ {0}, \dots , a _ {n} \in K \}
$$

$$
(3 + 2 x - x ^ {3}, - 2 + x ^ {2} + 2 x ^ {3} + x ^ {4}) \rightarrow 1 + 2 x + x ^ {2} + x ^ {3} + x ^ {4}
$$

$$
\operatorname{grado} (p (x)) = \left\{ \begin{array}{l l} \max f _ {i} \in N / a, \neq 0 \text {   se   } p (x) \neq 0 & : K [ x ] \times K [ x ] \to K [ x ] \\ - 1 \text {   opp   qualsiasi   grado,   se   } p (x) = 0 & (3 + 2 x, - 2 + x ^ {2}) \to - 6 - 4 x + 3 x ^ {2} + 2 x ^ {3} \end{array} \right.
$$

$$
(K, +, \cdot) \text {   campo   } n \in \mathbb {N} ^ {*} \quad K ^ {n} = k \times \dots \times k
$$

$$
\boxed {+}: k ^ {n} \times k ^ {n} \rightarrow k ^ {n}
$$

$$
((a _ {1}, \dots , a _ {n}), (b _ {1}, \dots , b _ {n})) \rightarrow (a _ {1} + b _ {1}, \dots , a _ {n} + b _ {n})
$$

$$
\text { PROP } (k ^ {n}, k, +,.) \text {   e - spazio   veitt.   su   k }
$$

$$
\mathrm{Dim} \quad \mathrm{per} n = 2
$$

$$
(1.) (K ^ {2}, +) \text { gr.   abeliano }
$$

$$
\text { comm } \forall (a _ {1}, a _ {2}), (b _ {1}, b _ {2}) \in K ^ {2}
$$

$$
(a _ {1}, a _ {2}) + (b _ {1}, b _ {2}) = (a _ {1} + b _ {1}, a _ {2} + b _ {2}) = (b _ {1} + a _ {1}, b _ {2} + a _ {3}) = (b _ {1}, b _ {2}) + (a _ {1}, a _ {2})
$$

$$
\text { ass } \forall (a _ {1}, a _ {2}), (b _ {1}, b _ {2}), (c _ {1}, c _ {2}) \in K ^ {2} \text { come   per   la   commutativita,   si   ricava   da   +. }
$$

$$
\mathrm{neuT} (0, 0): \forall (a _ {1}, a _ {2}) \in K ^ {2}, (a _ {1}, a _ {2}) + (0, 0) = (a _ {1}, a _ {2}) = (0, 0) + (a _ {1}, a _ {2})
$$

$$
\text {   simm   } \forall (a _ {1}, a _ {2}) \exists (a _ {1} ^ {\prime}, a _ {2} ^ {\prime}) \in K ^ {2} (a _ {1}, a _ {2}) + (a _ {1} ^ {\prime}, a _ {2} ^ {\prime}) = (a _ {1} + a _ {1} ^ {\prime}, a _ {2} + a _ {2} ^ {\prime}) = (a _ {1} + (- a _ {1}), a _ {2} (- a _ {2})) = (0, 0)
$$

## LEZIONE 4

PROPRIETA' ARITMETICHE di uno SPAZIO VETTORIALE 

Sia (V $_{1}$ +,.) uno spazio vettoriale su un campo (K $_{1}$ +,.) 

1) $\forall u \in V, \forall \alpha \in K$ $\alpha \cdot u = \underline{0} \Leftrightarrow \alpha = 0$ oppose u = 0 

$\Leftarrow$ se $\alpha = 0$ allora $0 \cdot u = (0 + 0) \cdot u$ per la $3^{9}$ proprieta dello spazio vettoriale 

abbiamo 0·u = (0·u) + (0·u) sommo ai 2 membri dell'uguaglianza -0·u 

$$
\text {   abbiamo   dunque   } 0 \cdot u + (- 0 \cdot u) = ((0 u) + (0 \cdot u)) + (- 0 \cdot u), \text {   si ha   cosr   sfruttando   l'associativita }
$$

$$
\underline {{0}} = 0 \cdot u + (0 \cdot u + (- 0 \cdot u)) \Rightarrow \underline {{0}} = 0 \cdot u + \underline {{0}} \Rightarrow \underline {{0}} = 0 \cdot u
$$

Ragionamento simile per $u = 0$ 

⇒ Se α≠0 allora α e invertibile rispetto alla moltiplicazione del campo. Sia α⁻¹ l'inverso di α 

Per ipotesi abbiamo $\alpha \cdot u = 0$ allora moltiplichiamo $\alpha^{-1}$ a entrambi membri dell'uguaglianza e abbiamo quindi $\alpha^{-1}$ . $(\alpha \cdot u) = \alpha^{-1} \cdot 0$ . 

Sappiamo che $\alpha^{-1}\circ e^{-}$ uguale 0 sfruttiamo pa la $4^{9}$ proprietà degli spazi vettoriali e abbiamo $=0(\alpha^{-1}\cdot\alpha)\cdot u\Rightarrow1\cdot u$ che per la $5^{9}$ proprietà $e^{-}=u\Rightarrow u=0$ 

2) $\forall \alpha \in K, \forall u \in V$ l'opposto di $\alpha \cdot u$ può essere $-( \alpha \cdot u) = (- \alpha) \cdot u = \alpha \cdot (-u)$ 

Dim $\alpha \cdot u + (-\alpha) \cdot u$ sfruttiamo la $3^{9}$ proprietà degli spazi vettoriali $\Rightarrow (\alpha + (-\alpha)) \cdot u \Rightarrow 0 \cdot u = 0$ 

se abbiamo $\alpha\cdot u + \alpha\cdot(-u)$ utilizzando la $2^{9}$ proprietà degli spazi vettoriali trouiamo $\alpha\cdot(u+(-u))$ e $\alpha\cdot0 = 0$ 

3) ∀α,βεκ, ∀υεν\λοι se α·u=β·u allora i due scalari sono uguali 

Dir abbiamo $\alpha\cdot u=\beta\cdot u$ , sommiamo a entrambi i membri - $\beta\cdot u$ abbiamo dunque 

$\alpha \cdot y + (-\beta \cdot u) = \beta \cdot u + (-\beta \cdot u)$ e ci troviamo $\alpha \cdot y + (-\beta \cdot u) = 0$ utilizzando la $3^{9}$ proprietà degli spazi vettoriali 

avremo $(\alpha+(-\beta))\cdot y=\underline{0}$ $\underline{MA}$ $y\neq0$ dunque per la $1^{9}$ proprieta deve essere $\alpha+-\beta=0$ . 

sono nel campo quindi β è l'opposto di α il che vuol dire α=β 

4) $\forall \alpha \in A \setminus \partial O, \forall u, v \in V$ se $\alpha \cdot u = \alpha \cdot v$ allora $u = v$ 

Din $\alpha \cdot y = \alpha \cdot v$ ; sommiamo a entrambi $-\alpha \cdot v = \alpha \cdot y + (\alpha \cdot (-v)) = 0$ sfruttando la $2^{9}$ proprieta. 

LINEARMENTE CHIUSO 

Sia $(V_{1},+,-)$ uno spazio vettoriale su un campok e sia x un sottoinsieme di V. X si dice linearmente chiuso 

·∀u,vεX e ∀αεK abbiamo che—αuεX 

## SOTTOSPAZIO VETTORIALE

Sig (V1+,.) uno spazio vettoriale su K e sia X un sottoinsieme di V linearmente chiuso. Sicco-

me X e lin. chiuso possiamo restringere le operazioni di Va X: 

$$
+: V \times V \rightarrow V
$$

$$
+ \mid_ {x \cdot x}: X \times X \rightarrow X
$$

dunque sia X so tfoinsieme di V si dice sottospazio di V se: 

$$
(u, v) \sim u + v \in X
$$

-X e $^{-}$ linearmente chiuso 

$$
\cdot : K \times V \rightarrow V
$$

- $(x_{1} + |x_{2}|, |x_{3})$ e uno spazio vettoriale 

$$
\cdot \vert_ {x \cdot x} ^ {:} K \times X \rightarrow X
$$

$$
(\alpha , u) \text { w o d } u
$$

x con le operazioni
ereditate da V 

$$
\mathrm{TEORENA}
$$

Sig V spazio vettoriale. 

Un sottoinsieme W di V e un sottospazio vettoriale di V <=> W e linearmente chiuso 

⇒ e' ouvia per definizione 

<= per ipotesi possiamo considerare le op. ristrette +|x e |x 

Esse creditano tutte le proprietà di + e . Rimane da dimostrare che 0εW e θυεW, -αεW
considero 0 come 0·u ma se OEK e αεW poiche W e lin. chiusa allora 0·uεW
cioe 0 εω 

abbiamo poi ΨυΕW Ξ-υΕV, si vode dimostrare che -υΕW. Sappiamo che -υ può essere visto come 

$$
(- 1) \cdot u m a - 1 \varepsilon k e u \varepsilon w q u i n d i (- 1) u = - u \varepsilon W
$$

Quindi e sufficiente l'ipotesi che W sia linearmente chiuso per essere anche sottospazio 

$$
\text { vettoriale   di   V. }
$$

$$
\bullet \quad w = \phi (0, p), (0, Q) \in w
$$

$$
\forall u, v \in W \Rightarrow \exists \alpha , \beta , \alpha^ {\prime}, \beta : u = \alpha (0, p) + \beta (0, q) +
$$

$$
v = \alpha^ {\prime} (0, P) + \beta^ {\prime} (0, Q)
$$

$$
u + v = (\alpha + \alpha^ {\prime}) (0, P) + (\beta , \beta^ {\prime}) (0, Q) \in \omega
$$

△dunque W chiusa rispetto a + 

$$
\cdot \gamma E W _ {1} u = \alpha (O, P) + \beta (O, Q) = \gamma (\alpha (O, P)) + \gamma (\beta (O, Q)) =
$$

$$
\gamma u = \gamma (\alpha (0, p) + \beta (0, q)) = \gamma (\alpha (0, p)) + \gamma (\beta (0, q)) =
$$

$$
= \gamma \alpha (0, p) + \gamma \beta (0, Q) \in W
$$

9. dunque w e' chiusa 

## COMBINAZIONI

Consideriamo (V $_{1}$ +,) un spazio vettoriale su K. Sia u $_{1}$ ,...,u $_{n}$ una n-vpla di vettori 

di V. Un vettore u si dice combinazione lineare di questa n-upla se esiste una n-upla di 

$$
\text {   scalari   } \alpha_ {1}, \ldots , \alpha_ {n} \in k ^ {n} \text {   tali   che   } y = \alpha_ {1} u _ {1} + \alpha_ {2} u _ {2} + \ldots + \alpha_ {n} u _ {n}
$$

$$
\mathbb {R} ^ {3} \quad u = (3, - 2, 4) \quad u _ {2} = (1, 0, 1) \quad (\alpha_ {1}, \alpha_ {2}) = (- 2, 1)
$$

$-2u_{1}+u_{2}$ e una comb. lineare poiche 

$$
- 2 (3, - 2, 4) + 1 (1, 0, 1) = (- 6, 4, - 3) + (1, 0, 1) = (- 5, 4, - 7)
$$

se i vettori della n-upla sono a 2a2 distinti, posso parlare di insieme piuttosto che di n-upla 

## SISTEMA DI GENERATORI

le sottospazio vettoriale L(x) si dice generato da x e x si dice sistema di generatori di L(x). Quindi un sistema 

di generatori di V e- un sottoinsieme S di V tali che L(S) = V 

Uno spazio vettoriale V si dice finitamente generato su un campo k. Se esiste un sottoinsieme 

Finito S di V tale che L(S)=V. Si noti che S può essere ∅ poiche il ∅ e sistema di genitori 

OSS ( $V_{1}K_{1}+$ , ) 

Sia $S = 3u_{1},\ldots ,u + 4$ un sistema di generatori di V, cioè $L(S) = V$ . 

Definiamo adesso T=S oful con u≠S 

T e ancora un sistema di generatori di V. 

## LEZIONE 5

## CHI USURE LINEARI

DEF 

Consideriamo (V, +, ) un spazio vettoriale su k. Dato un sottoinsieme X ≠ ∅ di V si dice chiuso-

ra lineare di X il sottoinsieme L(x) di V, costituito da tutti e sobi vettori che sono combina-

zioni lineari di vettori di X. Dunque: $L(x) = \{ \alpha, u_1 + \ldots + \alpha n u_n \ln \varepsilon N, u_1 \ldots u_n \in X, \alpha_1 \ldots \alpha_n \in K \}$ 

Sia (V, +, .) spazio vettoriale sul campo k e consideriamo X sott'insieme di V. 

i) abbiamo che la chiusura lineare di X $L(x) \geq x$ , 

ii) $L(x)$ e' linearmente chiuso 

iii) se W e un sottospazio vettoriale di V tale che X ≤ W, allora L(x) ≤ W 

(i) nel caso $x = \phi$ allora banalmente $x \subseteq L(x) = \{0\}$ 

se $x \neq \phi$ possiamo considerare $\forall u \in X$ che $u = 1 \cdot u$ e dunque $\in L(x)$ di conseguenza $x \in L(x)$ 

ii) sia $X \neq \phi$ e consideriamo $u, v \in L(x)$ abbiamo che: 

$$
- \exists t \in N, \exists \alpha_ {1} \dots \alpha_ {t} \in K, \exists y _ {1} \dots y _ {T} \in X: y = \alpha_ {1} y _ {1} + \alpha_ {2} y _ {2} + \dots + \alpha_ {t} y _ {T}
$$

$$
- \exists k \in N, \exists_ {\beta_ {1} \dots \beta_ {k}} \in K, \exists v _ {1} \dots v _ {k} \in X: v = \beta_ {1} v _ {1} + \beta_ {2} v _ {2} + \dots + \beta_ {k} v _ {k}
$$

Supponiamo $t \leq K$ , abbiamo che $u + v = \alpha_1 u_1 + \ldots + \alpha_T u_T + \beta_t v_t + \beta_{t+1} v_{t+1} + \ldots + \beta_K v_K$ banalmente abbiamo che 

u+v e una combinazione lineare di vettori di x il che implica che u+v∈L(x) dunque L(x) e chiuso rispetto q+ 

Consideriamo adesso $\gamma\in K$ , abbiamo che $\gamma u=\gamma(\alpha_{1}u_{1}+\cdots+\alpha_{t}u_{t})=\gamma(\alpha_{1}u_{1})+\cdots+\gamma(\alpha_{t}u_{t})=(\gamma\alpha_{1})u_{1}+\cdots+(\gamma\alpha_{t})u_{t}$ 

abbiamo dunque che ru è una combinazione lineare di X dunque yuεL(x) di conseguenza L(x) e linearmente chiuso 

iii) Siq $u \in L(x)$ con $u = \alpha_{1} u_{1} + \ldots + \alpha_{t} u_{t}$ dobbiamo for vedere che $u \in W$ . Per ipotesi $u_{1} \ldots u_{t} \in X$ e $X \leqslant W$ ma $W$ e sottospazio vettoriale dunque $\alpha_{1} u_{1}, \ldots, \alpha_{t} u_{t} \in W$ visto che $W$ e chiuso rispetto a . , e $\alpha_{1} u_{1} + \ldots + \alpha_{t} u_{t} \in W$ visto che $W$ e chiuso rispetto a t. Abbiamo dimostrato che $u \in W$ il che implica che comunque prendiamo un vettore in $L(x)$ esso $E$ al sottospazio $W$ se $W$ contiene $X$ . 

Sia (V, +, .) uno spazio vett. sul campo K e prendiamo 2 sottoinsiemi S,T di V. Essi genera 

no lo stesso spazio vettoriale dunque $L(S) = L(T) \Rightarrow S \subseteq L(T)$ e $T \subseteq L(S)$ 

⇒ Sappiamo che $S \subseteq L(S)$ e per ipotesi $L(S) = L(T)$ dunque $S \subseteq L(T)$ e naturalmente $T \subseteq L(T)$ 

⇐ Abbiamo che $S \subseteq L(T)$ dunque, poiché $L(T)$ e un sottospazio vettoriale, si ha che $L(S) \subseteq L(T)$ 

La stessa cosa vale per $T \leq L(S)$ sempre poiche $L(S)$ e un sottospazio vettoriale, abbiamo $L(T) \leq L(S)$ . 

$$
e \text { poiché } L (S) \subseteq L (\tau) e L (\tau) \subseteq L (S) \text { allora } L (S) = L (\tau)
$$

## ESEMPiO

$$
S = \{(1, 0, 1), (0, 1, 1) \}
$$

$$
T = \{(1, 1, 2), (2, - 1, 1), (0, 2, 2) \}
$$

$$
V _ {1} = 4 1 + 4 2
$$

$$
v _ {2} = 2 y _ {1} + (- 1) y _ {2} \Rightarrow T \subseteq L (S)
$$

$$
v _ {3} = 2 4 2
$$

$$
u _ {2} = \frac {1}{2} v _ {3} \Rightarrow S \subseteq L (T)
$$

$$
\text { Quindi }
$$

$$
v _ {1} = u _ {1} + \frac {1}{2} v _ {3} \Rightarrow u _ {1} = v _ {1} - \frac {1}{2} v _ {3}
$$

$$
L (S) = L (T) \neq V
$$

LINEARMENTE (IN) DIPENDENTE 

Sia (V $_{1}$ + , .) uno spazio vettoriale sul campo K. 

Una n-upla di vettori di V si dice linearmente dipendente se esiste un n-upla di scalari di,...,an 

non tutti nulli tale che $Q = \alpha_{1}y_{1} + \ldots + \alpha_{n}u_{n}$ cioè il valore nullo si esprime come combinazione li-

neare di vettori della n-upla. La n-upla di vettori di V si dice linearmente indipendente 

se non e $^{-}$ lin. dip. cioe $^{-}$ se: ∀α₁, ..., αn εK $^{n}$ abbiamo che α₁u₁ + ... + αn uₙ = 0. 

Allora gli scalari α₁,…,αₙ devono essere tutti nulli 

OSS Preso 10f per cui Q = α. Q ∀αEK allora 10f e Lin. Dip 

## ESEMPiO

$$
\cdot K [ x ] \{1 + x, x + x ^ {2} \} e ^ {-} L i N. I N D.
$$

$$
\alpha , \beta \in K = \mathbb {R}
$$

$$
\begin{array}{l} {\alpha , \beta \in K = 1 0} \\ {\alpha (1 + x) + \beta (x + x ^ {2}) = 0 \Rightarrow \alpha + (\alpha + \beta) x + \beta x ^ {2} = 0 \Rightarrow \left\{ \begin{array}{l l} {\alpha = 0} \\ {\alpha + \beta = 0} \\ {\beta = 0} \end{array} \right.} \end{array}
$$

$$
\alpha = 0 = \beta \text {   quindi   }
$$

Considerato un sottoinsieme X dello spazio vettoriale V. X e'Lin. Dip <= J u ε X: 4εL(X|X/4) inoltre intal caso L(x) = L(X|X/4) 

Caso 1) Nel caso in cui X ha un solo elemento |X| = 1 allora
X e⁻ LiN. DiP <=> X = {0} in tal caso X\{0\} = 0 e abbiamo che
L(φ) = L(0) = {0} 

Caso 2) Consideriamo il caso in cui $|x| \geq 2$ 

⇒ Per ipotesi esiste un sottoinsieme $\{u_{1},\ldots,u_{t}\}$ finito di x linearmente dipendente dunque $J_{\alpha_{1}},\ldots,\alpha_{t}\in K$ non tutti nulli tale che $\alpha_{1}u_{1}+\ldots+\alpha_{t}u_{t}=0$ . Possiamo considerare $\alpha_{t}\neq0$ il che vuddire che $J_{\alpha_{t}^{-1}}\in K$ reciproco di at Moltiplico a destra e sinistra per $\alpha_{t}^{-1}$ ottenendo $u_{t}=-(\alpha_{t}^{-1}\alpha_{1})u_{1}+\ldots-(\alpha_{t}^{-1}\alpha_{t-1})u_{t-1}\in L(u_{1},u_{t-1})\subseteq L(x\setminus\{u_{t}\})$ Abbiamo dimostrato che $u\in X:u\in L(x\setminus\{u\})$ 

- Adesso bisagna dimostrare che $L(x) = L(x|y+1)$ . Banalmente già sappiamo che $x|y+1 \leq x$ dunque $L(x|y+1) \subseteq L(x)$ , dobbiamo dimostrare il viaversa: 

Prendiamo $u \in L(x)$ quindi 3 vettori $v_1, \ldots, v_{p} \in X$ e scalari $\beta_1, \ldots, \beta_{p} \in K: u = \beta_1 v_1 + \ldots + \beta_{p} v_p$ . Abbiamo $u \in L(X \setminus V_{u+1})$ se $u_t \neq v_i \quad \forall i \in I, \ldots, p_t$ . 

se invece $u_{t}=v_{i}$ per qualche i, supponendo i=p abbiamo che: $u=\beta_{1}v_{1}+\cdots+\beta_{p}u_{t}$ ma noi sappiamo scrivere u+ come combinazione lineare. Abbiamo dunque $u=\beta_{1}v_{1}+\cdots+\beta_{p}\left(-\left(\alpha_{t}^{-1}\alpha_{1}\right)y_{1}+\cdots-\left(\alpha_{t}^{-1}\alpha_{t-1}\right)y_{t-1}\right)$ quindi anche in questo caso $u\in L(X|h_{1}u_{t})$ quindi $L(x)\subseteq L(X|h_{1}u_{t})\Rightarrow L(x)=L(X|h_{1}u_{t+1})$ 

per ipotesi $\exists u \in X : y \in L(X \setminus \{u\})$ allora $\exists \alpha_1, \ldots, \alpha_p$ ed $\exists v_1, \ldots, v_p \in X \setminus \{u\} : y = \alpha_1 v_1 + \ldots + \alpha_p v_p$ $\Rightarrow Q = -4 + \alpha_1 v_1 + \ldots + \alpha_p v_p$ ma $-4 = (-1)u$ e poiche $-1$ non e nullo allora possiamo tranquillamente scrivere il vettore nullo o come combina.lin di un sottoinsieme finito di vettori di X con scalari non tutti nulli il che vuol dire che abbiamo in sottoinsieme di X dipendente $\Rightarrow X$ e dipendente 

## LEZIONE 6

BASE DI UNO SPAZIO VETTORIALE 

Un sistema di generatori indipe. e' detto base. 

Sia nεN* e K $^{n}$ uno spazio vettoria le numerico. Sia ora B = { (1,0,...,0), (0,1,...,0) ..., (0,0,...,1)} 

|B|=n Allora B si dice base canonica 

## BASi e SISTEMI Di GENERATORi

$K[x]$ non ha sistemi di generatori finito. Cice $\forall S \subseteq K[x]: |S| = n \in N$ $L(S) \notin K[x]$ 

$$
\mathrm{Dim} S = \{p _ {1} (x), \dots , p _ {n} (x) \}
$$

$$
\alpha_ {1} = g r (p _ {1}), \dots , \alpha_ {n} = g r (p _ {n})
$$

$$
\alpha = \max \{\alpha_ {1}, \dots , \alpha_ {n} \}
$$

$$
\forall \alpha_ {1}, \dots , \alpha_ {n} \in K g r (\alpha_ {1} p _ {1}, \dots , \alpha_ {n} p _ {n}) \leq \alpha
$$

$$
H a \text { allora   sicuramente } x ^ {\alpha + 1} \not \in L (S), m a x ^ {\alpha + 1} \in K [ x ]
$$

$$
\text { Quindi } L (S) \notin K [ x ], \text { cioè } e ^ {-} \text { incluso   propriamente }
$$

## TEOREMA D'ESTRAZIONE DI UNA BASE

Sia (V1+,.) uno spazio uettoriale finitamente generato, e sia S un sistema di generatori. Finito di V allora esiste una base B di V tale che B e' contenuta in S e B si può estrarre. DiM 

i) Se $V = \{0\}$ allora $S = \emptyset$ quindi è una base di 10 $^{3}$ oppure $S = \{0\}$ cioè è LN.Dip quindi possiamo levare il vettore nullo. Abbiamo quindi che $\{0\} = L(\emptyset) = L(S|10\}$ dunque ciè una base contenuta in $S$ . 

ii) Se V≠ργ e S e⁻ LiN. iND. allora la base B=S. 

se s'è Lin. Dip. allora 3uεS, ad esempio 4t, tale che L(S|1u+1)=L(S). Considero dunque S'=S|1u+1 e ripeto se S'e-Lin. ind. Allora B=S' altri menti ripeto fino ad attenere un sottoinsieme Lin. ind. 

## ESEMPiO

in $\mathbb{R}^2$ prendiamo $S = \{(1,1), (-3,3), (0,1), (2,7)\}$ e-LiN. DiP poiche $(-3,3) = -3(1,1) + O(0,1) + O(2,7)$ quindi $S' = S\backslash \{(-3,3)\} = \{(1,1), (0,1), (2,7)\}$ 

$$
\begin{array}{l} \text { Consideriamo } \alpha (1, 1) + \beta (0, 1) + \gamma (2, 7) = (0, 0) \\ (- 2, - 2) + (0, - 9) + (2, 7) = (0, 0) \end{array} \Rightarrow \left\{ \begin{array}{l l} \alpha + 2 \gamma = 0 & \Rightarrow (\alpha = - 2 \gamma \\ - 2 \gamma + \beta + 7 \gamma = 0 & \Rightarrow \beta = - 5 \gamma \end{array} \right.
$$

$$
\text { otteniamo } S ^ {\prime \prime} = S ^ {\prime} \backslash \{2, 7 \} = f (1, 1), (0, 1) \}
$$

Sia (V $_{1}$ +,.) uno spazio vettoriale, so un campo K finitamente generato e sia S={v $_{1}$ ,...,v $_{m}$ }, un sistema di generatori di V finito con n elementi. Un sottoinsieme finito X={v $_{1}$ ,...,v $_{m}$ }, di V e $^{-}$ Lin.
DiP. se m>n. 

Se X e $^{-}$ LiN ind. invece m e $^{-}$ ≤ n, dunque un sottoinsieme indipendente non può avere più elementi di un sistema di generatori. 

Si suppone che Q & X, se nobanale. Per ipotesi L(S)=V in particolare si ha 

$$
\exists r _ {1}, \dots , r _ {n} \in K | v _ {1} = r _ {1} u _ {1} + \dots + r _ {n} u _ {n}.
$$

Poiche $v_{1} \neq 0$ supponiamo sia $r_{1}$ non nullo, allora 3rit e moltiplicchiamo a destra e sinistra per $r_{1}$ ottenendo: $\alpha_{1}^{-}v_{1}=u_{1}+\alpha_{1}^{-}\alpha_{2}u_{2}+\cdots+\alpha_{1}^{-}\alpha_{n}u_{n}$ porto $u_{1}$ a dx così ho a sx una 

combinazione lineare dei vettori $L = (v_{1}, u_{2}, \ldots, u_{n}) \in i$ vettori $u_{1}, u_{2}, \ldots, u_{n}$ . Si ha quindi 

$$
L (u _ {1}, u _ {2}, \dots , u _ {n}) \subseteq L (u _ {1}, \dots , u _ {n}) m a L (u _ {1}, \dots , u _ {n}) = L (S) = V d u n q u e
$$

$$
L (v _ {1}, u _ {2}, \dots , u _ {n}) \subseteq V.
$$

Ma a sua volta $V \subseteq L(v_{1}, u_{2}, \ldots, u_{n})$ dunque abbiamo $V = L(v_{1}, u_{2}, \ldots, u_{n})$ . Quindi sostituendo un vettore di X a un vettore di S si può avere ancora un sistema di generatori. 

Sapendo che $V = L(v_{1}, u_{2}, \ldots, u_{n})$ e $v_{2} \in V$ allora: $\exists \beta_{1}, \beta_{2}, \ldots, \beta_{n} \in K$ tale che 

In questo caso si hanno 2 possibilità: 

1) Se accade che $\beta_{2},\ldots,\beta_{n}$ sono tutti nulli allora resta che $v_{2}=\beta_{1}v_{1}$ . Ho che $v_{2}\in X$ si scrive come combinazione lineare di $v_{1}\in X$ il che vuol dire che $\{v_{1},v_{2}\}$ è LIN. Dip e poiché esso è un sottoinsieme di $X$ allora $X$ è linearmente dip. 

2) Altrimenti $\exists B_1 \neq 0$ con $i \geq 2$ , tipo $B_2 \neq 0$ , allora $\exists B_2^- \in K$ quindi: 

$$
\begin{array}{r l} {\beta_ {2} ^ {- 1} v _ {2}} & {= (\beta_ {2} ^ {- 1} \beta_ {1}) v _ {1} + (\beta_ {2} ^ {- 1} \beta_ {2}) u _ {2} + \dots + (\beta_ {2} ^ {- 1} \beta n) u _ {n} = >} \\ & {u _ {2} = \beta_ {2} ^ {- 1} v _ {2} - (\beta_ {2} ^ {- 1} \beta_ {1}) v _ {1} - (\beta_ {2} ^ {- 1} \beta_ {3}) u _ {3} - \dots (\beta_ {2} ^ {- 1} \beta n) u _ {n} \in L (v _ {1}, v _ {2}, u _ {3}, \dots , u _ {n})} \end{array}
$$

$$
\Rightarrow V = L (S ^ {\prime}) \subseteq L (v _ {1}, v _ {2}, u _ {3}, \dots , u _ {n}) \subseteq V, m a a l l o r a S ^ {\prime \prime} = \{v _ {1}, v _ {2}, u _ {3}, \dots , u _ {n} \} \Rightarrow L (S ^ {\prime \prime}) = V
$$

Reiterando il ragionamento, troviamo la dipendenza come nel caso (1) oppure $L(v_1, \ldots, v_n) = V = v_{n+1}, \ldots, v_m$ dato che m>n per ipotesi 

$(V, K, +, \cdot) \text{ sp. vett. f.g. } S_{\text{ia}} S \subseteq V: L(S) = V. \text{ Allora } T \subseteq V: T_{\text{Lin. ind}} \Rightarrow |T| \leq |S|$ 

$|T|>|S|\Rightarrow Te^{-} \text{LIN.Dip.}, \text{dal lemma di Steinitz}$ 

Ma allora ricordando una tautologia $[(p=20)(\Rightarrow)(-p<70)]$ 

abbiamo che $|T| \leq |S| \leq T$ e $^{-}$ LiN. iND. 

N.B Non si tratta di una doppia implicazione. 

## TEOREMA D'EQUIPOTENZA DI BASI

Sia (V1+,·) uno spazio vettoriale sul campo K, finitamente generato. Tutte le basi di V sono finite e hanno la stessa cardinalità 

Per ipotesi esiste un sistema di generatori S di V finito. Sià B ≤ S una base estratta da se sia la cardinalità di B = n. Consideriamo poi B' un'altra base di V. Per il corollario al lemmo di Steinitz, tutti i sottoinsiemi finiti di B' non hanno più vettori di B essendo B' LiN. ind. si ha dunque che |B'| ≤ |B|. Scambiando il rudo di Be B' si ha naturalmente 

$|B| \leq |B'|$ dunque troviamo alla fine che $|B| = |B'|$ 

## DIMENSIONE DI UNO SPAZIO VETTORIALE.

PROP 

Sia V uno spazio vettoriale. Consideriamo un insieme x ≤ V di t elementi LIN. IND 

$\Rightarrow x = \{ u_1, \ldots, u_+ \}$ . Se JueV1u & L(x) allora: x u4u4 e ancora LIN. IND. 

Dim 

4 Non e' comb.
lineare dei
vettori di x 

Dimostriamo per assurdo: supponiamo che $x \cup \cup = \{u_{1}, \ldots, u_{r}, u_{l}\} e^{-\operatorname{LiN}.DiP.}$ dunque $J_{\alpha1}, \ldots, \alpha t, \alpha \in K$ non tutti nulli: $Q = \alpha_{1} u_{1} + \ldots + \alpha_{t} u_{t} + \alpha u.$ Possiamo avere 2 casi: 

1) Siα α=0 abbiamo Ω=α₁u₁+...+αₜuₜ con α₁,...,αₜ NON tutti nulli ma cioè è assurdo poichē i vettori u₁,...,uₜ sono LiN.IND 

2) Sia $\alpha \neq 0$ abbiamo che $\exists \alpha^{-1} \in K$ che è il reciproco di $\alpha$ . Moltiplicchiamo a dx e sx di 0 

$u = -\alpha^{-1}\alpha_{1}u_{1} + \cdots - \alpha^{-1}\alpha_{t}u_{t}$ ma cio e assurdo poiche sappiamo che $u \notin L(u_{1}, \ldots, u_{t}) = L(x)$ 

## Dimensione

$(V, K, +, \cdot) f.g.$ la dimensione di V e il numero di vettori di una sua base 

PROP 

Sia (V, +, ) uno spazio F.g. sul campok avente dimensione finita = n. Sia S = {u₁, ..., uₙ} un insieme di cardinalità = n, abbiamo che Se Lin.IND. <=> Se un sistema di generatori di V 

⇒ Per assurò di ciamo S non è un sistema di generatori dunque L(S) ∈ V. Allora
∃u∈V: 4&L(S). Noi sappiamo che S u tuf è LiN. ind. ma S u tuf ha cardinalità
n+1 che e maggiore della dimensione di V e ciò è assurò per il lemma di
Steinitz 

$\Leftarrow$ Per assurdo S e LIN. DIR. allora: 34ES, supponiamo un, tale che L(S)=L(S\{un\}) e un εL(S\{un\}) quindi L(S\{un\}) e'un sistema di generatori di V con n-1 vettori allora esistera' una base di V contenuta in S\{un\} che quinoli aura' meno di n vettori e cioè assurdo. 

DEF di DIMENSIONE: 

Sia (V, +, i) f. g su K, il numero di vettori di una qualsiasi base di V si dice dimensione di V. 

## LEZIONE 7

TEOREMA DI COMPLETAMENTO DI UNA BASE 

Sia V uno spazio vettoriale F.g. su K avente dimensione finita n e sia X un sottoinsieme LIN. IND. di V avente cardinalità t<n. Allora 3 un sottoinsieme y di V avente cardinalità n-t tale che x u y e una base di V. 

Si come la cardinalità di x, cioè t < n allora x non e base di V, e poiche e Lin.IND. allora L(x) ∈ V. Dunque Jut+1 ∈ V: ut+1 & L(x) e sapendo che x e Lin.IND. allora x' = x u {ut+1} ∈ Lin.IND. Abbiamo dunque che x' ha cardinalità t+1 e abbiamo che se t+1 = n allora x' e BASE di V altrimenti x' NON e base ma x' e Lin.IND quindi x' non e sistema DI GENERATORi di V quindi L(x') ∈ V. 

Posso allora ricominciare e continuare fino a quando non ha aggiunto abbastanza elementi da trovare un sottoinsieme che contiene X è LiN. IND. e ha potenza n. 

## PROP

Sia W un sottospazio vettoriale di V. 

i) dim W = 0 <= W = {0}; 

$$
\text {   ii)   } \dim W \leq \dim V = n
$$

$$
\text { iii) } \dim W = \dim V \Leftrightarrow W = V
$$

$$
i) \Rightarrow \text { Per   ipotesi, } \emptyset e ^ {-} \text { una   base   diW } = \angle (\phi) = \{\underline {{0}} \}
$$

$$
<   = W = \{0 \} S = \{0 \} e ^ {-} L i N. D i P \Rightarrow Q \in L (S) = L (S, 1 0 4) = L (\emptyset) \Rightarrow \phi e ^ {-} u n a b a s e \Rightarrow
$$

$$
\dim \{0, 1 \} = 0
$$

ii) Sià Bw unabase di W, dunque Bw e'un sottoinsieme di V linearmente indipendente e L(Bw)=W. Poiche Bw e'un sottoinsieme di V lin. ind a allora per il corollario al lemme di Steinitz abbiamo che |Bw|≤ dim(v) ma |Bw|=dim(w) quindi dim w≤ dim V 

⇒ Bu base di W. La cardinalità di Bu e⁻ ≤ n poiche⁻ n = dim V. Se |Bw| = n allora Bu sarebbe un insieme LIN. IND contenuto in V con la cardinalità = dim V ⇒ Bu e⁻ un sistema di generatori di V. Allora Bu e⁻ una base di V quindi L(Bw) = V a sua volta L(Bw) = W e possiamo dire W = V 

BASI ORDINATE 

PROP (V, K, +, .) dim V = n 

Sia $B = (e_1, \ldots, e_n)$ una base ordinata di V. Allora: 

$$
\forall u \in V, \exists ! (x _ {1}, \dots , x _ {n}) \in k ^ {n}: u = x _ {1} e _ {1} + \dots + x _ {n} e _ {n}
$$

DEF Si dice che gli scalari $x_{1},\ldots,x_{n}$ sono le componenti di un vettore in B e che $(x_{1},\ldots,x_{n})$ e la n-pla delle componenti di u in B. 

Dim Per ipotesi i vettori e, ..., en formano una base di V, quindi in particolare formano un sistema di generatori: 

$$
(x _ {1}, \dots , x _ {n}) \in K ^ {n}
$$

Sia $(y_{1},\ldots,y_{n})\in K^{n}$ : $y=y_{1}e_{1}+\ldots+y_{n}e_{n}$ , procedo a soffrarre. Ottengo 

$$
0 = 4 - 4 = x _ {1} e _ {1} + \dots + x _ {n} e _ {n} - y _ {1} e _ {1} - \dots - y _ {n} e _ {n} = \underbrace {(x _ {1} - y _ {1})} _ {\text {   }} e _ {1} + \dots + \underbrace {(x _ {n} - y _ {n})} _ {\text {   }} e _ {n}
$$

$$
e _ {1}, \dots , e n \neq 0 \Rightarrow \left\{ \begin{array}{l l} x _ {1} - y _ {1} = 0 \\ \vdots \\ x _ {n} - y _ {n} = 0 \end{array} \right. \Rightarrow \left\{ \begin{array}{l l} x _ {1} = y _ {1} \\ \vdots \\ x _ {n} = y _ {n} \end{array} \right.
$$

'come volevasi dimostrare 

## ESEMPio :

$R^{2}$ B((1,1),(1,-1)) e una base ordinata di $R^{2}$ 

$$
\text { Determinare   le   componenti   di } u = (5, - 3) \text { in } B
$$

$$
(5, - 3) = x _ {1} (1, 1) + x _ {2} (1, - 1) = (x _ {1} + x _ {2}, x _ {1} - x _ {2})
$$

$$
\left\{ \begin{array}{l} 5 = x _ {1} + x _ {2} \\ - 3 = x _ {1} - x _ {2} \end{array} \right. \Rightarrow \left\{ \begin{array}{l} x _ {1} = 1 \\ x _ {2} = 4 \end{array} \right.
$$

$$
(x _ {1}, x _ {2}) = (1, 4)
$$

PROP Si considere un'applicazione 

$$
\Phi_ {B}: V \rightarrow k ^ {n}
$$

n-vpla delle componenti
di u in B 

$$
u \approx (a _ {1}, a _ {2} \dots , a _ {n})
$$

$$
\Phi_ {B} \text {   si   die   isomorfismo   di   V   associato   a   B   }
$$

## Riferimento

PROP $\Phi_{B}$ e-biettiva 

$$
\text { inielt:   Siano } u, v \in V e u \neq v \text { Tesi: } (x _ {1}, \dots , x _ {n}) = \Phi_ {B} (u) \neq \Phi_ {B} (v) = (y _ {1}, \dots , y _ {n})
$$

$$
\text { Per   assurdo: } \Phi_ {B} (u) = \Phi_ {B} (v) \Rightarrow (x _ {1}, \dots , x _ {n}) = (y _ {1}, \dots y _ {n})
$$

$$
y = x _ {1} e _ {1} + \dots + x _ {n} e _ {n} = y _ {1} e _ {1} + \dots + y _ {n} e _ {n} = v \quad \text {   4assurdo   }
$$

$$
\text {   surri:   } \quad \text {   Sia   } (x _ {1}, \ldots , x _ {n}) \in K ^ {n} \text {   Basta   asservare   che   se   } u = x _ {1} e _ {1} + \ldots + x _ {n} e _ {n} \in V \text {   allora   } \Phi_ {8} (u) = (x _ {1}, \ldots , x _ {n})
$$

## LEZIONE 8

Sotto SPAZIO VETTORIALE : unione ed intersezione 

Sia (V1+.) uno spazio vettoriale sul campo k e ω₁,...,wp sottospazi vettoriali di V 

i) $w_{1} \cap w_{2}, \ldots \cap w_{p}$ e' un sottospazio vettoriale di U 

ii) $w_{1} \cup w_{2}, \ldots \cup w_{p}$ non e'un sottospazio vettoriale di V 

sappiamo sicuramente che 0€ win... n wp ≠ φ. La prima casa da dimostrare e' che ∀y, v € win... n wp 

allora $u + v \in \omega_1 n \ldots n \omega_p$ . Abbiamo che $u, v \in \omega_1, u, v \in \omega_2, \ldots, u, v \in \omega_p$ 

ma poiche' w1, w2, ..., wp sono tutti sottospazi di V dunque tutti chiusi rispetto alla somma allora 

$u + v \in \omega_{1}, u + v \in \omega_{2}, \ldots, u + v \in \omega_{p}$ di conseguenza $u + v \in \omega_{1} \cap \omega_{2} \cap \cdots \cap \omega_{p}$ . 

dobbiamo dimostrare la chiusura rispetto al prodotto. 

$\forall u \in w_{1} \ldots w_{p}, \quad u$ naturalmente $\varepsilon a w_{1}, w_{2}, \ldots, w_{p}$ che sono tutti sottospazi dunque tutti 

chiusi rispetto alla moltiplicazione ⇒ ∀αεκ abbiamo che αυεω₁, αυεω₂, ..., αυεωₚ e di conse-

guenza α4εω₁n...n ωp 

$\underline{PROP} (V_{1}K_{1+1}) \text{ pEIN}^{*}$ 

Sia $w_{1}, w_{2}, \ldots, w_{p}$ sottospazi vettoriali di V 

w1 u w2 ... u wp non è generalmente un sott. vettoriale, ma la chiusura lineare della loro unione, in particolare, 

equivale al sottospazio somma così definito: 

$$
W _ {1} + W _ {2} + \dots + W p = \{w _ {1} + w _ {2} + \dots + w p | w _ {1} \in W _ {1} \cap \dots \cap w p \in W _ {p} \}
$$

DIM Notiamo innanzitutto che $w_{1} + \ldots + w_{p}$ e diverso dal vuoto e stabile rispetto alle operazioni per come e stato definito. Dato che e linearmente chiuso, e anche un sottospazio vettoriale. Non resta che esplicitare che $L(\omega_{1}, 0 \ldots 0, \omega_{p}) = \omega_{1} + \ldots + \omega_{p}$ . 

$$
\subseteq \text { ricardiamo   che } w _ {1} \cup \dots \cup w _ {p} \subseteq w _ {1} + \dots + w _ {p} \Rightarrow L (w _ {1} \cup \dots \cup w _ {p}) \subseteq W _ {1} + \dots + W _ {p}.
$$

$$
w _ {1} \varepsilon w _ {1} \Rightarrow w _ {1} = w _ {1} + 0 + \dots + 0; w _ {2} \varepsilon w _ {2} \Rightarrow w _ {2} = 0 + \dots + 0 e t c
$$

$$
2 u \in W _ {1} + \dots + W _ {p} \Rightarrow \exists w _ {1} \in W _ {1}, \dots , w _ {p} \in W _ {p}: u = w _ {1} + \dots + w _ {p} \in L (W _ {1} \cup \dots \cup W _ {p})
$$

cioe u e comb lineare di vettori che appartengono a w, o... o wp 

Se la somma di $W_1$ e $W_2$ sono sottospazi finitamente generati di V abbiamo 

$$
\dim (\omega_ {1} + \omega_ {2}) = \dim (\omega_ {1}) + \dim (\omega_ {2}) - \dim (\omega_ {1} \cap \omega_ {2})
$$

## SOMMA DIRETTA

Siano $w_{1}, w_{2}, \ldots, w_{p}$ sottospazi di U 

$w_{1}+w_{2}+\cdots+w_{p}$ si dice somma diretta se Hiει,...,pf abbiamo che 

$$
w _ {i} \cap (w _ {1} + \dots + w _ {i - 1} + w _ {i + 1} + \dots + w _ {p}) = \{0 \}
$$

PROP $w_{1}, \ldots, w_{p} \subseteq V$ sott. vett. 

$$
\dim W _ {1} = n _ {1} \quad B _ {1} = \{e _ {1 1}, \dots , e _ {1 n _ {1}} \}, \dots , \dim W _ {p} = n _ {p} \quad B _ {p} = \{e _ {p 1}, \dots , e _ {p n p} \}
$$

Se $W_1 + \ldots + W_p = W_1 \oplus \ldots \oplus W_p$ allora $(e_{i_1}, \ldots, e_{in_1}, \ldots, e_{pi}, \ldots, e_{pnp}) e^-$ LiN. IND 

ed e~ una base di ω₁⊕...⊕ωρ 

DIM si procede per induzione per p=1, la proposizione e banalmente vera. Supponiamo valga per (p-1) e verfichiamo per p. 

$$
\alpha_ {1 _ {1}} e _ {1 _ {1}} + \dots + \alpha_ {1 n _ {1}} e _ {1 n _ {1}} + \alpha_ {2 _ {1}} e _ {2 _ {1}} + \dots + \alpha_ {2 n _ {2}} + \dots + \alpha_ {p _ {1}} e _ {p _ {1}} + \dots + \alpha_ {p n} e _ {p n} = 0 \quad \Leftrightarrow >
$$

$$
\alpha_ {1} e _ {1} + \dots + \alpha_ {n 1} e _ {n 1} = - \alpha_ {2 1} e _ {2 1} - \dots - \alpha_ {2 n 2} - \dots - \alpha_ {p 1} e _ {p 1} - \dots - \alpha_ {p n} e _ {p n} = \underline {{0}} \Rightarrow \alpha_ {1} = \dots = \alpha_ {n 1} = 0
$$

Per induzione la proposizione è vera per p-1 sp. vett, ossia( $e_{2_1}, \ldots, e_{2_{n_2}}, \ldots, e_{p_1}, e_{p_{n_p}}$ ) 

$$
\alpha_ {2 _ {1}} = \dots = \alpha_ {2 n _ {2}} = \dots = \alpha_ {p _ {1}} = \dots = \alpha_ {p n _ {p}} = 0
$$

## LEZIONE 9

Siano w1, w2, ..., wp sottospazi vettoriali di V. La somma di tali sottospazi e 

$$
w _ {1} + w _ {2} + \dots + w p = \{u _ {1} + u _ {2} + \dots + u p | u _ {1} \in w _ {1}, \dots , u p \in w p 4
$$

PROP: Se $w_{1}=L(S_{1}),\ldots,w_{p}=L(sp)$ allora: 

i) $w_{1}+\ldots+w_{p}\in$ un sottospazio vettoriale 

ii) $w_{1}+\ldots+w_{p}=L(s_{1},v\ldots,v_{p})-la somma e'il più piccolo$ sottospazio che contiene  
l'unione di $s_{1},\ldots,s_{p}$ 

1) Bisagna verificare che $\omega_{1}+\ldots+\omega_{p}$ e' soft. vett. e partiamo ce verificare la chiusora della somma sicuramente $\underline{0}\in\omega_{1}+\ldots+\omega_{p}$ dunque $\omega_{1}+\ldots+\omega_{p}\neq\phi$ . Consideriamo $u,v\in\omega_{1}+\ldots+\omega_{p}$ allora si ha: 

2 Se considero $S_1 \cup \ldots \cup \mathfrak{sp}$ essa è $\subseteq W_1 + W_2 + \ldots + W_p$ piache se prendo $u \in S_1 \cup S_2 \ldots \cup \mathfrak{sp}$ allora $J_i \in \{1, \ldots, p\} : u \in S_i$ ma $S_i \subseteq W_i$ quindi posso scrivere $u = 0 + \ldots + 0 \in W_1 + W_2 + \ldots + W_p$ 

$\subseteq$ Sia $u \in W_{1} + \ldots + W_{p}$ allora $\exists u_{i} \in W_{i} \quad \forall i \in \{1, \ldots, p\} : y = u_{1} + \ldots + u_{i} + \ldots + u_{p}$ ma se $u_{i} \in W_{i}$ allora $u_{i} \in L(S_{i})$ il che vuol dire che $\exists t_{i} \in N, \exists V_{1}^{i}, \ldots, V_{t_{i}}^{i} \in S_{i}, \exists \alpha_{1}^{i}, \ldots, \alpha_{t}^{i} \in K : u_{i} = \alpha_{1}^{i} v_{1}^{i} + \ldots + \alpha_{t_{i}}^{i} v_{t_{i}}^{i}.$ 

Abbiamo quindi che $u = \alpha_{1}^{i} v_{1}^{i} + \alpha_{t_{1}}^{i} v_{t_{1}}^{i} + \cdots + \alpha_{1}^{i} v_{1}^{i} + \cdots + \alpha_{t_{i}}^{i} v_{t_{i}}^{i} + \cdots + \alpha_{t_{p}}^{p} v_{t_{p}}^{p}$ , possiamo dire che $u = u_{1} + \cdots + u_{i} + \cdots + u_{p} \in L(S_{1}u \ldots uS_{i}u \ldots uSp)$ . Abbiamo cost dimostrato che $w_{1} + w_{2} + \cdots + w_{p} =$ 

$$
L (S _ {1} \cup \dots \cup S _ {p})
$$

TRASFORMAZIONI LINEARI 

$$
\Phi_ {B}: u \in V \rightarrow (x _ {1}, \dots , x _ {n}) \in K ^ {n}
$$

Abbiamo gia visto che tale applicazione e biettiva 

OSS $\Phi_{B}$ gode delle seguenti proprietà: 

$$
1) \forall u, v \in V \quad \Phi_ {B} (u + v) = \phi_ {B} (u) + \Phi_ {B} (v);
$$

$$
2) \forall u \in V, \forall \lambda \in K \quad \phi_ {B} (\lambda u) = \lambda \phi_ {B} (u)
$$

DEF Siano V, W spazi vett. su un campo K. Un'applicazione T: V → W si dice appli-
cazione lineare se Yu, VE U e Haek si ha: 

i) $T(u+v)=T(u)+T(v)$ - l'immagine della somma di 2 vettori sia = alla somma delle im. 

$$
\text {   i   i   } \quad T (\alpha \cdot u) = \alpha T (u)
$$

Inoltre sia T: V→ω un'app. lineare auremo che se : 

- Te iniettiva si dice monomorfismo 

- Te' SURIETTIVA si dice epimorfismo 

- Te Biettiva si dice isomorfismo 

• V = ω, T si dice endomorfismo 

• V = W e T e biettiva, T si dice automorfismo 

PROPRIETA' APP. LINEARI 

Sia T: V→W app lineare 

i) $T(\underline{0}v) = \underline{0}\omega$ [immagine del vettore nullo del dominio $e^{-} = al$ vettore nullo del codominio]
DiM → $T(\underline{0}v) = T(0 \cdot \underline{0}v) = O \cdot T(\underline{0}v) = \underline{0}\omega$ 

ii) $\forall u_{1},\ldots,u_{t}\in V,\forall\alpha_{1},\ldots,\alpha_{t}\in K$ possiamo considerare $\alpha_{1}u_{1}+\cdots+\alpha_{t}u_{t}$ e abbiamo $T(\alpha_{1}u_{1}+\cdots+\alpha_{t}u_{t})=\alpha_{1},T(u_{1})+\cdots+\alpha_{t}T(u_{t})$ [imm. della comb. lineare = alla comb. lineare con gli scalari moltiplicata per l'immag. dei vettori] DiM 

Per induzione: con t=1 abbiamo $T(\alpha_{1},u_{1})=\alpha_{1}T(u_{1})$ as we already know. 

Passo d'induzione → t>1 ⇒ T(α₁u₁+...+αₜ₋₁uₜ₋₁+αₜuₜ) sfruttando l'associativita' della som-

ma ottengo: $T((\alpha_1 u_{1} + \ldots + \alpha_{t-1} u_{t-1}) \alpha_t u_t)$ 

Possiamo sfruttare la 1º proprietà delle app linearsi e avere 

$$
T (\alpha_ {1} u _ {1} + \dots + \alpha_ {t - 1} u _ {t - 1}) + \alpha_ {t} u _ {t}) = T (\alpha_ {1} u _ {1} + \dots + \alpha_ {t - 1} u _ {t - 1}) + T (\alpha_ {t} u _ {t}).
$$

A questo punto sfrutto l'ipotesi d'induzione che l'enunciato e vero con t-1 

$$
T (\alpha_ {1} u _ {1 +} \dots + \alpha_ {t - 1} u _ {t - 1} + \alpha_ {t} u _ {t}) = \alpha_ {1} T (u _ {1}) + \dots + \alpha_ {t - 1} T (u _ {t - 1}) + \alpha_ {t} T (u _ {t})
$$

PROP T: V → W app·lineare 

Se $(u_{1},\ldots,u_{n})$ è una n-pla di vettori di V LiN. Dip., allora anche $(T(u_{1}),\ldots,T(u_{n})) \in W$ e' LiN. Dip., non posso dire nulla se la n-pla di V e' IND. 

Dim Per ipotesi $\exists \alpha_{1},\ldots,\alpha_{n} \in K$ non tutti nulli: $\alpha_{1}u_{1}+\ldots+\alpha_{n}u_{n}=\underline{0}v$ . $T(\alpha_{1}u_{1}+\ldots+\alpha_{n}u_{n})=T(\underline{0}v)=\underline{0}w$ . $\alpha_{1}T(u_{1})+\ldots+\alpha_{n}T(u_{n})$ dove gli scalari Non sono tutti nulli. Allora anche la n-pla $(T(u_{1}),\ldots,T(u_{n}))$ e- LIN. Dip. 

$$
A P P L i C A Z I O N i L i N E A R i
$$

$$
T: V \rightarrow W \text { app   lineare }
$$

PROP Sià U ≤ V un sott. vett. Allora T(u) è un sott. vett. di W 

$$
\underline {{0}} w = T (\underline {{0}} v) \varepsilon T (u) \Rightarrow T (u) \neq \emptyset
$$

$$
u ^ {\prime}, v ^ {\prime} \in T (u) = \{T (u) | u \in U \} \Rightarrow \exists u, v \in U: T (u) = u ^ {\prime}
$$

$$
u ^ {\prime} + v ^ {\prime} = T (u) + T (v) \stackrel {(1)} {=} T (u + v) \varepsilon T (0)
$$

$$
\text { Fissiamo   ora } \lambda \in K.
$$

$$
\lambda u ^ {\prime} = \lambda T (u) \stackrel {(2)} {=} T (\lambda u) \varepsilon T (v)
$$

Per quanto appena detto, ImT = {T(u) | u ∈ V} = T(v) sottospa vett. di w 

$$
\mathrm{Prop} S \subseteq V: U = L (S) \quad \mathrm{allara} T (U) = L (T (S))
$$

$$
\text { per   la   prop.   preced. }
$$

$$
\supseteq S \in U \Rightarrow T (s) \subseteq T (U) \Rightarrow L (T (s)) \subseteq T (U)
$$

$$
\subseteq u \in T (U) \Rightarrow \exists u \in U = L (s): T (u) = u ^ {\prime}
$$

$$
u \varepsilon L (S) \Rightarrow \exists n \varepsilon N ^ {*}, \exists u _ {1}, \dots , u _ {n} \varepsilon S, \exists \alpha_ {1}, \dots , \alpha_ {n} \varepsilon K: u = \alpha_ {1} u _ {1} + \dots + \alpha_ {n} u _ {n} = 2
$$

$$
T (u) = T (\alpha_ {1} u _ {1} + \dots + \alpha_ {n} u _ {n}) \stackrel {(i i)} {=} \alpha_ {1} T (u _ {1}) + \dots + \alpha_ {n} T (u _ {n}) \in L (T (S))
$$

$$
\text {Indichiamo con ker} (\tau) \text {il nucleo o kernel di} \tau
$$

$\ker(T)=\{u\varepsilon V|T(u)=0\omega\}$ [e'l'insieme degli elementi di V che hanno come immagine il vettore 

$$
\mathrm{Prop:} T e ^ {-} \text {   societtiva   } \Leftrightarrow I m T = W
$$

$$
T e ^ {\prime} \text {   iniettiva   } \iff \ker T = \{Q v \}
$$

$$
\text { Dim   Te   surietti   Uq } \Leftrightarrow \text { ImT = W   gia'   noto }
$$

$$
\text { Dimostriamo   l'altra }
$$

⇒ sia uεV con u≠∅ sapendo che Tε iniettiva, abbiamo che T(u)≠T(Ωv) ma noi sappiamo che 

$$
\ker (T) = 1 \underline {{0}} v _ {1}
$$

$$
\Leftarrow \text { Siano } u, v \in V _ {e} T (u) = T (v) \text { possiamo   dire   che } T (u) - T (w) \Leftrightarrow T (u) - T (v) = 0 w
$$

$$
\Rightarrow T (u - v) = 0 w \quad \text { quindi } \quad \text { abbiamo   che } \quad u - v \in \ker (\tau) \quad \text { ma   } \ker (\tau) = 1 0 v 4 \text {   quindi }
$$

$$
u - v = \underline {{0}} v \quad \text {   il   che   vuol   dire   } u = v.
$$

Sia T: V → W un' applicazione lineare 

Se la n-pla di vettori e LiN.IND e T e' iniettiva allora la n-pla di immagini e LiN.IND. 

$$
\text { Siano } B _ {1 1}, \dots , B n E K: B _ {1} T (u _ {1}) + \dots + B n T (u _ {n}) = 0 w
$$

possiamo quindi scrivere $T(B_1u_1 + \ldots + Bnun) = 0w$ il che significa che $B_1u_1 + \ldots + Bnun \in Ker(T)$ ma poiche $T$ e' iniettiuq sappiamo che $Ker(T) = \{Qv\}$ di conseguenza $B_1u_1 + \ldots + Bnun = 0w$ e sapendo che i vettori $u_1, \ldots, u_n$ sono linear. Indo. allora $B_1, \ldots, B_n$ sono tutti nulli. 

## LEZIONE 10

TEOREMA DELL' EQUAZIONE DIMENSIONALE 

Siano V, W spazi vettoriali su campo K, con V fin. gen. e dim (V)=n. 

SiaT: V→W un' app lineare si ha che n= dim (ker)(τ)+ dim Im(τ) 

dimV    nudeo 

TEOREMA FONDAMENTALE DELLE APP.LINEARI 

Siano V, W spazi vett. su un campo k con V f.g. e a uente dim=n. Sia B=(e1,...,en) una base ordinata di V definiamo l'app. F:B→W NON LINEARE. 

$$
I 1 \text {   teorema   dice   che:   } J! T: V \rightarrow W: T (e _ {1}) = p (e _ {1}), \dots , T (e n) = p (e n)
$$

Dim (leggila giusto per) 

Dimostriamo l'esistenza. Sia uEV e consideriamo le sue componenti (x₁, ..., xₙ) in B. Allora de-

finisco $T(u) = x_1 \varphi(e_1) + \ldots + x_n \varphi(e_n)$ abbiamo dunque che l'app. $T: V \to W$ associa a $u \in V$ 

Verifichiamo che Te' lineare. Consideriamo atre al vettore u anche w e le sue componenti y1,...,yn 

in B. Abbiamo che le componenti di $u + v$ in B sono $x_{1} + y_{1}, \ldots, x_{n} + yn$ 

$$
\Rightarrow T (u + v) = (x _ {1} + y _ {1}) \varphi (e _ {1}) + \dots + (x _ {n} + y _ {n}) \varphi (e _ {n}) = x _ {1} \varphi (e _ {1}) + \dots + x _ {n} \varphi (e _ {n}) + y _ {1} \varphi (e _ {1}) + \dots + y _ {n} \varphi (e _ {n}) = T (u) + T (v)
$$

Facciamo lo stesso col x ed esce che e' LINEARE. 

Dimostriamo l'unicità: consideriamo un'atra applicazione T':V→W LINEARE |T'(e1)=φ(e1),... 

... $T'(en) = \varphi(en)$ . Dunque abbiamo che: $T'(y) = T'(x_1 e_1 + \ldots + x_n en)$ ma poiché $T'$ e' éineare 

quindi conserva le comb. Lineari dunque $T'(u) = x_1 T'(e_1) + \ldots + x_n T'(e_n) = x_1 \varphi(e_1) + \ldots +$ 

APPLICAZIONI LINEARI 

PROP T: V→W isomorfismc S≤V 

$S e^{-} \text{ LiN. iND} \Leftrightarrow T(S) e^{-} \text{ LiN. iND. }$ 

⇒ Te' iniettiva per cui conserva la lineare indipendenza 

$\Leftarrow T^{-1} : W \rightarrow V e^{-} \text{ uno isomorfismo. Allora. } S = T^{-1} (T(S)) e^{-} \text{ Lin. ind. Siq } S = \{ v_1, \ldots, w\}$ 

$$
T ^ {- 1} (T (s)) = T ^ {- 1} (\{T (v _ {1}), \dots , T (v _ {t}) \}) = \{T ^ {- 1} (T (v _ {1})), \dots , T ^ {- 1} (T (v _ {t})) \} = \{v _ {1}, \dots , v t \}
$$

Sia data la matrice $A=\begin{pmatrix}a_{1}^{1},a_{2}^{1}\cdots a_{m}^{1}\\ \vdots\quad\vdots\quad\vdots\\ a_{1}^{m},a_{2}^{m}\cdots a_{n}^{m}\end{pmatrix}$ Il rango di una m e = al rango
di una sua trasposta. 

abbiamo che dim(L(a₁,...,an) e 

detta rango della matrice ed e il max 

numero di colonne di A LIN. IND. 

$$
A = \left( \begin{array}{l l} 2 & 0 \\ 1 & 0 \end{array} \right) \quad \dim L ((2, 0, 1), (0, 1, 0), (0, 0, 1)) = 3 = \operatorname{range} (A) = \dim L ((2, 0, 0) (0, 1, 0) (1, 0, 1))
$$

DEF: $A \in M_{m \times 0}$ (K) 

A si dice ridotta a scalini (o a gradini): <=> 

i) a' e' una rigga nulla di A => Tutte le righe succes. sono nulle 

ii) il primo elemento da sinistra non nullo si dice pivot e deve stare più a sinistra dei pivot delle righe successive. Inoltre A si dice completamente ridotta a gradini se è vero anche che: 

iii) i pivot sono tutti uguali ad 1 

iv) gli elementi sopra a tutti i pivot sono nulli 

Prop $A \in M_{mxn}(k)$ , $A \in \text{ridotta a gradini} \Rightarrow \text{rango}(A) = k$ dove $k \in \text{il numero di pivot}$ . 

## OPERAZIONI o TRASFORMAZIONI ELEMENTARI

Si definiscono trasformazioni elementari di riga le seguenti modifiche sulle righe (Non colonne) di una matrice $A \in H_{mxn}(k)$ : 

i) scambiare 2 righe differenti ${a}^{i} \rightarrow  {a}^{j}$ 

ii) Preso αεκλ10f, moltiplicare per tale elemento α NON Nullo di K a'←α·a' 

iii) Preso uno scalare α'εκ, sommare a una riga. Una differente riga moltiplicare per α: α'i←α'+α'Tutte queste operazioni sono invertibili e conservano il rango. 

$$
A = \left( \begin{array}{l l l l} 0 & 2 & 0 & 1 \\ 1 & 1 & - 1 & 0 \\ 2 & 0 & 1 & - 1 \\ 1 & - 1 & 2 & 1 \\ - 2 \end{array} \right) \quad a ^ {1} \leftrightarrow a ^ {2} \quad B = \left( \begin{array}{l l l l} 1 & 1 & - 1 & 0 \\ 0 & 2 & 0 & 1 \\ 2 & 0 & 1 & - 1 \\ 1 & - 1 & 2 & 1 \\ - 2 \end{array} \right)
$$

Per tomano industro, bastenebbe fane $b^{2}\leftrightarrow b^{1}$ . Alesso $b^{2}\rightarrow\lambda b^{2}$ , doce $\lambda=\frac{1}{2}$ 

$$
C = \left(\begin{array}{c c c c}1&1&- 1&0\\0&1&0&4\\2&0&1&1\\1&- 1&2&1\\- 2\end{array}\right) c ^ {3} \rightarrow c ^ {3} + (- 2) c ^ {1} D = \left(\begin{array}{c c c c}1&1&- 1&0\\0&1&0&4\\0&- 2&3&1\\1&- 1&2&1\\- 2\end{array}\right)
$$

Andre queste operazioni sono reversibili clinavate. Adesso $d^{4} \rightarrow d^{4} + (-1)d^{1}$ 

$$
E = \left(\begin{array}{c c c c c}1&1&- 1&0&1\\0&1&0&\frac {4}{2}&1\\0&- 2&3&1&- 3\\0&- 2&3&1&- 3\end{array}\right) e ^ {4} \rightarrow x ^ {5} + (- 1) x ^ {3} F = \left(\begin{array}{c c c c c}1&1&- 1&0&1\\0&1&0&\frac {4}{2}&1\\0&- 2&3&1&- 3\\0&0&0&0&0\end{array}\right) g ^ {3} \rightarrow g ^ {3} + 2 g ^ {2}
$$

Questo algoritmo, piuttosto intuitivo, è andledatto. Metodo di riduzione di Gauss, utile per risolvono sistemi di equazioni velocemente.
Vediamole, a titolo informativo, un po' più nel dettaglio. 

$$
a ^ {i} \leftrightarrow a ^ {k} \quad \forall i \in \{2, \dots , m \} \quad a ^ {i} \rightarrow a ^ {i} + (\frac {- a _ {J} ^ {i}}{a _ {J} ^ {i}}) a ^ {i} \quad a _ {J} ^ {i} + a _ {j} a _ {J} ^ {i - 1 0} = a _ {j} = \frac {- a _ {J} ^ {i}}{a _ {J} ^ {i}} \quad \rightarrow \text { Creo   Chemie   di   latti   zemi   sello   pival } e \text { provado   identiavamente   nelles   setto   motive }
$$

$$
A = \left(\begin{array}{l l l l}0&0&1&2\\0&0&2&1\\0&- 7&3&- 1\\0&1&4&0\end{array}\right) \quad\begin{array}{l}a ^ {\prime} <   \rightarrow a ^ {k} = a ^ {3}\\J = 2 \quad K = 3\end{array}\quad A ^ {\prime} = \left(\begin{array}{l l l l}0&- 7&3&- 1\\0&0&2&1\\0&0&1&2\\0&1&4&0\end{array}\right) \quad\begin{array}{l}e ^ {4} \rightarrow e ^ {4} + \left(- \frac {a ^ {4}}{e ^ {1} z}\right) a ^ {4}\\- (- \frac {1}{z}) ^ {2}\end{array}
$$

## LEZIONE 11

## Sistema di EQUAZIONI

Un sistema di n equazioni lineari in n incognite su un campo k e' un n-upla 

di equazioni lineari in n incognite a coefficienti in k. 

$$
(a _ {1} ^ {\prime} x _ {1} + \dots + a _ {n} ^ {\prime} x _ {n} = b ^ {\prime}
$$

$$
a ^ {2} _ {1} x _ {1} + \dots + a ^ {2} n \times n = b ^ {2}
$$

$$
9 _ {1} ^ {m} \times 1 + \dots + 9 _ {n} ^ {m} \times n = b ^ {m}
$$

A un sistema di equazioni lineari possiamo associare 2 matrici: 

- Prima matrice \ matrice incompleta : e' costituita solo dai coeff. delle in cognite 

- Seconda matrice\matrice completa: costituita sia dai coeff. delle incognite sia dai termini noti 

$$
n = 3 \quad k = \mathbb {R} \quad \left\{ \begin{array}{l l} - x _ {2} + 2 x _ {3} = 4 \\ x _ {1} + x _ {2} - 4 x _ {3} = 0 \end{array} \right.
$$

$$
A = \left( \begin{array}{l l l} 0 & - 1 & 2 \\ 1 & 1 & - 4 \end{array} \right) \quad A = \left( \begin{array}{l l l l} 0 & - 1 & 2 & 4 \\ 1 & 1 & - 4 & 0 \end{array} \right)
$$

DEF·Il sistema Σe compatibile se ammette almeno 1 soluzione cioè se 

$$
S = \{(y _ {1}, \dots , y _ {n}) \in k ^ {n} \setminus A \binom{y _ {1}}{\vdots} = b \} \neq \emptyset
$$

$$
\text { altimenti } \sum e ^ {-}
$$

$$
\begin{array}{c} \text { proclorro   tra   a } \\ \text { e   la   trasposta   della   n - pla } \\ \text { di   scalari } \end{array}
$$

- $\sum e \sum'$ sono equivalenti se hanno le stesse soluzioni: $S = S'$ 

## TRASFORMARE i SISTEMI DI EQUAZIONE

Sia Σ un sistema lineare di m equazioni in n incognite so k e sia C la sua matrice 

completa. Se effettuiamo su C un numero finito di operazioni elementari, otteniamo una 

$$
\mathrm{Dim} \quad \sum : \left\{ \begin{array}{l l} a _ {1} ^ {1} x + \dots + a _ {n} ^ {n} x n = b _ {1} \\ a _ {m} ^ {m} x + \dots + a _ {n} ^ {m} x n = b m \end{array} \right. \quad \left( \begin{array}{l l l l} a _ {1} & \dots & a _ {n} ^ {1} & b _ {1} \\ & \vdots & & \vdots \\ a _ {m} ^ {m} & \dots & a _ {n} ^ {m} & b _ {m} \end{array} \right)
$$

$$
i) i, k \in \{1, \dots , m \} a ^ {i} \leftrightarrow a ^ {k}
$$

$$
\sum : \left\{ \begin{array}{l} a _ {1} ^ {i} x _ {1} + \dots + a _ {n} ^ {i} x _ {n} - b _ {i} = 0 \\ a _ {k} ^ {k} x _ {1} + \dots + q _ {n} ^ {k} x _ {n} - b _ {k} = 0 \end{array} \right.
$$

$$
\sum : \left\{ \begin{array}{l l} a ^ {k _ {1}} x _ {1} + \dots + a ^ {k _ {n}} x _ {n} - b _ {k} = 0 \\ a ^ {i _ {1}} x _ {1} + \dots + a ^ {i _ {n}} x _ {n} - b _ {i} = 0 \end{array} \right.
$$

$$
\text {   ii)   } i \in \{1, \dots , m \} \quad \lambda \in k - \{0 \}, a ^ {i} \rightarrow \lambda a ^ {i}
$$

$$
\sum : \left\{ \begin{array}{l l} \lambda a _ {1} ^ {i} x _ {1} + \dots + \lambda a _ {n} ^ {i} x _ {n} - \lambda b _ {i} = 0 \\ \vdots \\ k \end{array} \right. \quad y = (y _ {1}, \dots , y _ {n}) \in S \Rightarrow e _ {i} (y) = 0, \dots , e _ {i} (y) = 0 \Rightarrow
$$

$$
\Rightarrow e _ {1} (y) = 0, \dots , \lambda e _ {i} (y) = \lambda \cdot 0 = 0, \dots , e n (y) = 0 \quad \Leftrightarrow \quad (y _ {1}, \dots , y _ {n}) \in S ^ {\prime}
$$

$$
\text { iii) } i, k \in \{1, \dots m \}, \alpha \in K, a ^ {i} \rightarrow a ^ {i} + \alpha a ^ {k}
$$

$$
\sum : \left( \begin{array}{l} (a _ {i} + \alpha a _ {k} ^ {k}) x _ {1} + \dots + (a _ {n} ^ {k} + \alpha a _ {n} ^ {k}) x _ {n} - (b _ {i} + \alpha b _ {k}) = 0 \\ a _ {k} ^ {k} x _ {1} + \dots + a _ {n} ^ {k} x _ {n} - b _ {k} = 0 \end{array} \right)
$$

$$
y = (y _ {1}, \dots , y _ {n}) \in S \Rightarrow
$$

$$
e _ {1} (y) = 0, \dots , e _ {i} (y) = 0, \dots , e n (y) = 0 \Rightarrow e _ {1} (y) = 0, \dots , e _ {i} (y) + \alpha e _ {k} (y) = 0, \dots , e n (y) = 0 \Leftrightarrow
$$

$$
(y _ {1}, \dots , y _ {n}) \in S ^ {\prime}
$$

$$
\sum : \left\{\begin{array}{l}x _ {1} + x _ {2} - 2 x _ {3} = 1\\- x _ {1} - x _ {2} + x _ {3} = 0\end{array}\right. \quad \left(\begin{array}{r r r r}1&1&- 2&1\\- 1&- 1&1&0\end{array}\right) \quad a ^ {2} \rightarrow a ^ {2} + a ^ {2} \left(\begin{array}{r r r r}x _ {1}&x _ {2}&x _ {3}\\1&1&- 2&1\\0&0&- 1&1\end{array}\right) \quad \sum : \left\{\begin{array}{l}x _ {1} = - x _ {2} - 2 + 1 = - x _ {3} - 1\\x _ {3} = - 1\end{array}\right.
$$

$$
S = S ^ {\prime} = \{(- x _ {2} - 1, x _ {2}, - 1) | x _ {2} \in \mathbb {R} \} \quad S \text {   dice   che   il   sistema   he   col   soluzioni,   dose   l'exp   dipende   dal   numero   di   var.   libero.   }
$$

$$
a ^ {2} \rightarrow - a ^ {2} \left(\begin{array}{c c c c}1&1&- 2&1\\0&0&1&- 1\end{array}\right) e ^ {\prime} \rightarrow a ^ {4} + 2 a ^ {2} \left(\begin{array}{c c c c}1&1&0&- 1\\0&0&1&- 1\end{array}\right) \sum^ {\prime \prime}: \left\{\begin{array}{l l}x _ {1} + x _ {2} = - 1&= x _ {1} = - x _ {2} - 1\\x _ {3} = - 1\end{array}\right.
$$

$$
\text { Notiamo   de } \underline {{\underline {{o}}}} \notin S = \{(- x _ {2} - 1, x _ {1}, - 1) | x _ {2} \in \mathbb {R} ^ {3} \} \subseteq \mathbb {R} ^ {3} \quad \text { quindu } S \text { NON } \text { e   un   settosp.   vall.   du } \mathbb {R} ^ {3}.
$$

$$
\text {   M   E   T   O   D   O   G   A   U   S   S   -   J   O   R   D   A   N   }
$$

Il metodo GAUSS-JORDAN per risolvere un sistema di equazioni consistue di 2 step: 

1) riduzione a gradini della materia completa 

2) i) sostituzione A ritroso delle variabili che corrispondono ai pivot (NON eibere) 

(ii) Riduzione completa a GRADINI della matrice completa. 

Infine si scrive l'insieme S. 

$$
\begin{array}{l} {\mathrm{Esempio:}} \\ {\sum : \left\{ \begin{array}{l l} {- 2 x _ {2} + 2 x _ {3} + x _ {4} - x _ {5} = 1} \\ {- x _ {1} + x _ {2} - 2 x _ {3} - x _ {4} + x _ {5} = 0} \\ {x _ {1} - x _ {2} + 2 x _ {3} - 2 x _ {4} + 2 x _ {5} = - 3} \\ {- x _ {1} - 2 x _ {2} + x _ {3} + x _ {4} - x _ {5} = 2} \end{array} \right.} \end{array}
$$

$$
C = \left( \begin{array}{l l l l l l} 0 & - 2 & 2 & 1 & - 1 & 1 \\ - 1 & 1 & - 2 & - 1 & 1 & 0 \\ 1 & - 1 & 2 & - 2 & 2 & - 3 \\ - 1 & - 2 & 1 & 1 & - 1 & 2 \end{array} \right) c ^ {1} <   - > c ^ {2} \quad \left( \begin{array}{l l l l l l} - 1 & 1 & - 2 & - 1 & 1 & 0 \\ 0 & - 2 & 2 & 1 & - 1 & 1 \\ 1 & - 1 & 2 & - 2 & 2 & - 3 \\ - 1 & - 2 & 1 & 1 & - 1 & 2 \end{array} \right) c ^ {3} <   > c ^ {3} + c ^ {4} \quad \left( \begin{array}{l l l l l l} - 1 & 1 & - 2 & - 1 & 1 & 0 \\ 0 & - 2 & 2 & 1 & - 1 & 1 \\ 0 & 0 & 0 & - 3 & 3 & - 3 \\ 0 & - 3 & 3 & 2 & - 2 & 2 \end{array} \right) =
$$

$$
\left(\begin{array}{c c c c c c}- 1&1&- 2&- 1&1&0\\0&- 2&2&1&- 1&1\\0&0&0&- 3&3&- 3\\0&0&0&\frac {1}{2}&- \frac {1}{2}&\frac {1}{2}\end{array}\right) c ^ {4} \rightarrow c ^ {4} + \frac {1}{6} c ^ {3} \left(\begin{array}{c c c c c c}- 1&1&- 2&- 1&1&0\\0&- 2&2&1&- 1&1\\0&0&0&- 3&3&- 3\\0&0&0&0&0&0\end{array}\right) \quad \text {   rudoitte   a   scolini.   Procediamo   con   (ii)   }
$$

$$
\left(\begin{array}{c c c c c c c c}{{C ^ {1} \rightarrow - C ^ {1}}}&{{\left(\begin{array}{c c c c c c c}{{1}}&{{- 1}}&{{2}}&{{- 1}}&{{- 1}}&{{0}}\\{{0}}&{{1}}&{{- 1}}&{{- \frac {1}{2}}}&{{\frac {1}{2}}}&{{\frac {1}{2}}}\\{{0}}&{{0}}&{{0}}&{{1}}&{{- 1}}&{{1}}\\{{0}}&{{0}}&{{0}}&{{0}}&{{0}}&{{0}}\end{array}\right)}}&{{C ^ {1} \rightarrow C ^ {2} + \frac {1}{3} C ^ {3}}}&{{\left(\begin{array}{c c c c c c}{{1}}&{{- 1}}&{{2}}&{{0}}&{{0}}&{{- 1}}\\{{0}}&{{1}}&{{- 1}}&{{0}}&{{0}}&{{0}}\\{{0}}&{{0}}&{{0}}&{{1}}&{{- 1}}&{{1}}\\{{0}}&{{0}}&{{0}}&{{0}}&{{0}}&{{0}}\end{array}\right)}}&{{C ^ {4} \rightarrow C ^ {4} + C ^ {5}}}\\{{C ^ {2} \rightarrow - \frac {1}{2} C ^ {3}}}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&{}&{}\\{}&{}&{}&{}&\end{array}\right) = C ^ {1}
$$

$$
\sum : \left\{ \begin{array}{l} x _ {1} + x _ {3} = - 1 \\ x _ {2} - x _ {3} = 0 \\ x _ {4} - x _ {5} = 1 \end{array} \right. \Rightarrow \left\{ \begin{array}{l} x _ {1} = - x _ {3} - 1 \\ x _ {2} = x _ {3} \\ x _ {4} = x _ {5} + 1 \end{array} \right.
$$

$$
S = S ^ {\prime} = \left\{(- x _ {3} - 1, x _ {3}, x _ {3}, x _ {5} + 1, x _ {5}) \mid x _ {3}, x _ {5} \in \mathbb {R} \right\} \subseteq \mathbb {R} ^ {5}
$$

Data una coppia di matrici (A,B) conforma bile (se n=p ossia il numero di cdome della prima matrice e = al numero di righe della 2º matrice B) definisco il prodotto 

righe per colonne facendo il prodotto scalare numerico tra le righe di A e tutte le colonne di B. 

## ESEMPio:

$$
A = \left( \begin{array}{l l l} 2 & - 3 & 4 \\ 0 & 1 & 7 \end{array} \right)
$$

$$
B = \left( \begin{array}{l l} - 1 & 1 \\ 0 & 1 \\ 2 & - 2 \end{array} \right)
$$

$$
A B = \left( \begin{array}{l l} a ^ {\prime} b _ {1} & a ^ {\prime} b _ {2} \\ a ^ {2} b _ {1} & a ^ {2} b _ {2} \end{array} \right) \in H _ {2 \times 2} (\mathbb {R})
$$

$$
a ^ {\prime} b _ {1} = ((2 \cdot - 1) + (- 3 \cdot 0) + (4 \cdot 2)) = - 2 + 0 + 8 = 6
$$

$$
a ^ {2} b _ {1} = ((0 \cdot 1) + (1 \cdot 0) + (7 \cdot 2)) = 0 + 0 + 1 4 = 1 4
$$

$$
\begin{array}{r l} {a ^ {\prime} b _ {2}} & {= ((2 \cdot 1) + (- 3 \cdot 1) + (4 \cdot - 2)) = - 9} \\ {a ^ {2} b _ {2}} & {= ((0 \cdot 1) + (1 \cdot 1) + (7 \cdot - 2)) = - 1 3} \end{array}
$$

$$
A B = \left( \begin{array}{l l} 6 & - 9 \\ 1 4 & - 1 3 \end{array} \right)
$$

tale operazione non è commutativa, associativa, distributiva, e il suo elemento neutro e la matrice identica fatta da tutti 1 sulla diagonale principale e tutti 0 altre. 

## GRUPPO LINEARE GENERALE

Prende il nome di gruppo generale lineare l'insieme di tutte le matrici quadrate invertibili, dello stesso ordine e a coefficienti in uno stesso campo, dotato dell'operazione di prodotto tra matrici. Più nello specifico, fissiamo un numero naturale n≥1 e consideriamo un campo k, quale potrebbe essere campo R o G. Consideriamo poi l'insieme di tutte le matrici quadrate di ordine n a coefficienti nel campo k e invertibili. Se dotiamo tale insieme dell'operazione di prodotto tra matrici si viene a formare un gruppo detto gruppo generale lineare. 

$$
\{G L (n, k) = A \in M _ {n} (k): A e ^ {- i n v e r t.} \}
$$

PROP $\sum_{0}: Ax=0$ So insieme delle scuizioni $\leq k^{n}$ . Allora So e'un sott.spa. vett. di $k^{n}$ Dim Proviamo che So e' LiN. CHIUSO: 

$$
\cdot O _ {\varepsilon} S o b a n a l e \Rightarrow S o \neq \phi
$$

$$
\begin{array}{l} {\cdot y = (y _ {1}, \ldots , y _ {n}), z = (z _ {1}, \ldots , z _ {n}) \in S _ {0}} \\ {\Rightarrow A \left( \begin{array}{l} y _ {1} \\ y _ {n} \end{array} \right) = 0 \quad \cap A \left( \begin{array}{l} z _ {1} \\ z _ {n} \end{array} \right) = 0 \quad \Rightarrow A \left[ \left( \begin{array}{l} y _ {1} \\ y _ {n} \end{array} \right) + \left( \begin{array}{l} z _ {1} \\ z _ {n} \end{array} \right) \right] = 0 + 0 = 0} \end{array}
$$

$$
\begin{array}{l} {\cdot \alpha \in K \quad T h: \alpha y \in S _ {0}} \\ {A [ \alpha (y _ {n}) ] = \alpha [ A (y _ {n}) ] = \alpha \cdot 0 = 0} \end{array}
$$

## LEZIONE 12

TEOREMA DI ROUCHE - CAPELLI 

Sia Σ un sistema di equazioni lineari tali che Ax=b allora consideriamo la matrice completa C di tale sistema, abbiamo che: 

Σ e $^{-}$ compatible ⇔ rango (A) = rango (C) incomplete 

Posso scrivere Σ in forma vettoriale cioe 

$$
\sum : \left\{x _ {1} \left( \begin{array}{c} a _ {1} ^ {\prime} \\ a _ {2} ^ {\prime} \\ \vdots \\ a _ {m} ^ {n} \end{array} \right) + x _ {2} \left( \begin{array}{c} a _ {2} ^ {\prime} \\ a _ {1} ^ {\prime} \\ \vdots \\ a _ {2} ^ {m} \end{array} \right) + \dots + x n \left( \begin{array}{c} a _ {n} ^ {\prime} \\ a _ {n} ^ {\prime} \\ \vdots \\ a _ {n} ^ {m} \end{array} \right) = \left( \begin{array}{c} b _ {1} \\ \vdots \\ b _ {n} \end{array} \right) \right\}
$$

dire che $y_{1},\ldots,y_{n}\in k^{n}$ è soluzione di tale sistema wol dire che sostituendo ordinatamente $y_{1},\ldots,y_{n}$ nelle variabili del sistema ottengo l'uguaglianza con $\begin{pmatrix}b_{1}\\ b_{1}\end{pmatrix}$ ma dunque $\begin{pmatrix}b_{1}\\ b_{1}\end{pmatrix}$ è combinazione lineare delle colonne dei coefficienti. Quindi possiamo dire che $\Sigma$ è comporibile $\Leftrightarrow b\in L(a_{1},\ldots,a_{n})$ . 

Adesso dobbiamo dimostrare che $b \in L(a_1, \ldots, a_n) \Leftrightarrow \text{rango}(A) = \text{rango}(C)$ $\Rightarrow$ Abbiamo che $b \in L(a_1, \ldots, a_n)$ manoi sappiamo che $a_1, \ldots, a_n \in L(a_1, \ldots, a_n)$ dunque per il teorema sulla chiusura lineare abbiamo che $L(b, a_1, \ldots, a_n) \subseteq L(a_1, \ldots, a_n)$ ma poiché il viceversa e' ouvio abbiamo che $L(b, a_1, \ldots, a_n) = L(a_1, \ldots, a_n)$ quindi

dim $L(b, a_1, \ldots, a_n) = \text{dim } L(a_1, \ldots, a_n)$ il che ci permette di dire che $\text{rango}(C) = \text{rango}(A)$ $\Leftarrow$ Per ipotesi sappiamo che $\text{rango}(C) = \text{rango}(A)$ , inoltre sappiamo che $L(a_1, \ldots, a_n, b) \subseteq L(a_1, \ldots, a_n)$ e poiché essi hanno la stessa dimensione allora abbiamo che $L(a_1, \ldots, a_n, b)$ e' = $L(a_1, \ldots, a_n)$ ma si può notare banalmente che $b \in L(a_1, \ldots, a_n, b)$ dunque l'implicazione e' dimostrata. 

PROP Consideriamo un sistema omogeneo $\Sigma_{0}: A_{X}=0$ . Sappiamo che prendendo una matrice $A$ di tipo $m \times n$ possiamo considerare l'applicazione lineare $\tilde{T}_{A}: (x_{1}, \ldots, x_{n}) \in K^{n} \sim A\left( \begin{array}{c} x_{1} \\ \vdots \\ x_{n} \end{array} \right) \in K^{m}$ . Il nucleo di $\tilde{T}_{A}$ cise: $\ker (\tilde{T}_{A}) = \{(x_{1}, \ldots, x_{n}) \in K^{n} | A\left( \begin{array}{c} x_{1} \\ \vdots \\ x_{n} \end{array} \right) = 0\} = SO$ trasposta di $(x_{1}, \ldots, x_{n})$ dunque e' un sottospazio vettoriale. 

$$
A = \left( \begin{array}{l l l} - 2 & 3 & 5 \\ 1 & 0 & - 1 \end{array} \right) \in M _ {2 \times 3} (\mathbb {R})
$$

$$
\tilde {T} _ {A}: \mathbb {R} ^ {3} \rightarrow \mathbb {R} ^ {2} \quad (x _ {1}, x _ {2}, x _ {3}) \rightarrow^ {t} (A (\begin{array}{c}x _ {1}\\x _ {2}\\x _ {3}\end{array})) = ^ {t} \left(\begin{array}{c c}- 2 x _ {1} + 3 x _ {2} + 5 x _ {3}\\x _ {1}&- x _ {3}\end{array}\right)
$$

$$
\tilde {T} _ {A} ((x _ {1}, x _ {2}, x _ {3})) = (- 2 x _ {1} + 3 x _ {2} + 5 x _ {3}, x _ {1} - x _ {3}).
$$

$$
B = \{(1, 0, 0), (0, 1, 0), (0, 0, 1) \}
$$

$$
\tilde {T} _ {A} ((1, 0, 0)) = (- 2, 1) \quad \tilde {T} _ {A} ((0, 1, 0)) = (3, 0) \quad \tilde {T} _ {A} ((0, 0, 1)) = (5, - 1)
$$

$$
\operatorname{Im} \widetilde {T A} = L (a _ {1}, a _ {2}, a _ {3}) \Rightarrow \dim \operatorname{Im} \widetilde {T A} = \operatorname{range} (A) \quad \dim R ^ {3} = \dim \operatorname{Im} \widetilde {T A} + \dim \ker \widetilde {T A}
$$

SCRIVERE SOTTOSPAZI VETT. COME SISTETTI OMOGENEI 

OSS: $\Sigma_{0}: Ax=0$ $So=ker\tilde{f}A\Rightarrow dimSo=n-rango(A)$ , dove n e il num di incognit 

$$
\begin{array}{r l}{\mathrm{Sempio:}}&{= \left\{\begin{array}{l l}{x _ {1} + x _ {2} - x _ {3} + 2 x _ {4} + x _ {5} = 0}\\{2 x _ {1} + x _ {2} + x _ {3} + x _ {4} - x _ {5} = 0}\\{+ 2 y _ {1} - x _ {4} - 2 z _ {5} = 0}\end{array}\right. \quad \left(\begin{array}{l l l l l}{1}&{1}&{- 1}&{2}&{1: 0}\\{2}&{1}&{1}&{1}&{- 1: 0}\\{1}&{0}&{2}&{- 1}&{- 2: 0}\end{array}\right) \quad a ^ {2} \rightarrow a ^ {1} - 2 a ^ {1}}\\&{= \left(\begin{array}{l l l l l}{1}&{1}&{- 1}&{2}&{1: 0}\\{0}&{- 1}&{3}&{- 3}&{- 3: 0}\\{0}&{- 1}&{3}&{- 3}&{- 3: 0}\end{array}\right) \quad a ^ {3} \rightarrow a ^ {3} - a ^ {3}}\end{array}
$$

$$
\left(\begin{array}{c c c c c}1&1&- 1&2&1\\0&1&- 3&3&3\\0&0&0&0&0\end{array}\right) a ^ {1} \rightarrow a ^ {1} - a ^ {2} \left(\begin{array}{c c c c c}1&0&z&- 1&- 2\\0&1&- 3&3&3\\0&0&0&0&0\end{array}\right) \quad \left\{\begin{array}{l l}x _ {1} = - 2 \overline {{x}} _ {3} + \overline {{y}} _ {3} + 2 \overline {{x}} _ {3} <   i n d i a t e l o l a b h a m p a r e m a l i s e r\\x _ {2} = 3 \overline {{x}} _ {3} - 2 \overline {{x}} _ {4} - 2 \overline {{y}} _ {3} \quad S _ {0} = \left\{\left(- 2 \overline {{y}} _ {3} + \overline {{y}} _ {4} + 2 \overline {{x}} _ {3}, 3 \overline {{x}} _ {3} - 2 \overline {{x}} _ {4} - 2 \overline {{x}} _ {3}, \overline {{x}} _ {3}, \overline {{x}} _ {4}, \overline {{x}} _ {5}\right) | \overline {{x}} _ {3}, \overline {{x}} _ {4}, \overline {{x}} _ {5} \in \mathbb {R} \right.\end{array}\right.
$$

$$
\text { Metto   in   evidenza: } \quad \overline {{x}} _ {3} (- 2, 2, 1, 0, 0) + \overline {{x}} _ {4} (1, - 3, 0, 1, 0) + \overline {{x}} _ {5} (2, - 3, 0, 0, 1) \Rightarrow S _ {0} = \mathcal {L} ((- 2, 2, 1, 0, 0), (1, - 3, 0, 1, 0), (2, - 3, 0, 0, 1))
$$

$$
\dim S _ {0} = n - \operatorname{range} (A) = 5 - 2 = 3 = \text { num   di   variabile   libere. }
$$

$$
\begin{array}{l} {i \mathrm{3~yellow}} \\ {\mathrm{sono~len~indip.}} \end{array} \quad \left( \begin{array}{c c c c c} {- 2} & {3} & {1} & {0} & {0} \\ {1} & {- 3} & {0} & {1} & {0} \\ {2} & {- 3} & {0} & {0} & {1} \end{array} \right)
$$

$$
\left(\begin{array}{c c c c c}0&1&- 1&2&1: 0\\1&2&1&- 1&2: 0\\1&3&0&1&3: 0\\2&3&3&1&- 1: 0\end{array}\right) a ^ {1} \leftrightarrow a ^ {2} \quad \left(\begin{array}{c c c c c}1&2&1&- 1&2&0\\0&1&- 1&2&1&0\\1&3&0&1&3&0\\2&3&3&1&- 1&0\end{array}\right) a ^ {3} \leftrightarrow a ^ {2} - a ^ {4} \left(\begin{array}{c c c c c}1&2&1&- 1&2&0\\0&1&- 1&2&1&0\\0&1&- 1&3&- 3&0\\0&- 1&3&- 3&0\end{array}\right) a ^ {3} \leftrightarrow a ^ {3} - a ^ {2} \quad \left(\begin{array}{c c c c c}1&2&1&- 1&2\\0&1&- 1&2&1\\0&0&0&- 5&- 4\\0&0&0&0&0\end{array}\right) a ^ {3} \rightarrow \frac {1}{5} a ^ {3}
$$

$$
\left( \begin{array}{c c c c c} 1 & 2 & 1 & - 1 & 2 \\ 0 & 1 & - 1 & 2 & 1 \\ 0 & 0 & 0 & 1 & - v _ {3} \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right) \begin{array}{l} a ^ {2} - y a ^ {2} - z a ^ {3} \\ a ^ {4} - y a ^ {4} + a ^ {3} \end{array} \left( \begin{array}{c c c c c} 1 & 2 & 1 & 0 & v _ {5} \\ 0 & 1 & - 1 & 0 & v _ {5} \\ 0 & 0 & 0 & 1 & - v _ {5} \\ 0 & 0 & 0 & 0 & v _ {5} \end{array} \right) \begin{array}{l} a ^ {\prime} - y a ^ {\prime} - z a ^ {2} \\ a ^ {3} - y a ^ {3} - z a ^ {2} \end{array} \left( \begin{array}{c c c c c} 1 & 0 & 1 & 0 & - y \\ 0 & 1 & - 1 & 0 & v _ {5} \\ 0 & 0 & 0 & 1 & - v _ {5} \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right) \quad \left\{ \begin{array}{l l l l l} x _ {1} = - \frac {3}{5} \overline {{x}} _ {3} + \frac {4}{5} \overline {{x}} _ {5} \\ x _ {2} = \overline {{x}} _ {3} - \frac {1}{5} \overline {{x}} _ {5} \\ x _ {4} = \frac {9}{5} \overline {{x}} _ {5} \end{array} \right.
$$

$$
S _ {0} = \left\{\left(- 2 \overline {{x}} _ {3} + 4 \overline {{x}} _ {5}, \overline {{x}} _ {3} - n _ {5} \overline {{x}} _ {5}, \overline {{x}} _ {3}, \frac {4}{3} \overline {{x}} _ {5}, \overline {{x}} _ {5}\right) | \overline {{x}} _ {3}, \overline {{x}} _ {5} \in \mathbb {R} \right\}
$$

$$
\dim S _ {0} = n - \operatorname{rayo} (A) = 5 - 3 = 2
$$

$$
\begin{array}{l l l} {\overline {{{x}}} _ {3}} & {\overline {{{x}}} _ {2}} & {(- 3, 1, 1, 0, 0)} \\ {1} & {0} & {(4, - \frac {1 3}{2}, 0, \frac {4}{2}, 1)} \\ {0} & {1} & \end{array} \Rightarrow S _ {0} = \mathcal {L} ((- 3, 1, 1, 0, 0), (4, - \frac {1 3}{2}, 0, \frac {4}{2}, 1)).
$$

$$
\text { TEOREMA }
$$

Sia W un soltospazic vettoriale numerico in $K^n$ avente dimensione h. Il teorema ci dice che 

$$
\exists \sum_ {0}: A x = 0 \text {   tale   one   } S _ {0} = \omega
$$

Dim 

Sia B = (ω₁, ..., ωₕ) una base di ω. I vettori della base sono costituiti 

$$
w _ {1} = (a _ {1} ^ {1}, a _ {1} ^ {2}, \dots , a _ {n} ^ {m})
$$

$$
e \text {   naturalmente   sappiamo   che   } W = L (B).
$$

$$
w h = (a _ {h} ^ {1}, a _ {h} ^ {2}, \dots , a _ {h} ^ {m})
$$

$$
\text { Considero   un   vettore } u = (x _ {1}, \ldots , x _ {n}) \in k ^ {n}, \text { sappiamo   che }
$$

$$
u \varepsilon W = L (B) \iff r a n g o
$$

$$
\left(\begin{array}{c c c c}a _ {1}&\dots&a _ {h} ^ {\prime}&x _ {1}\\a _ {2} ^ {\prime}&\dots&a _ {2 h} ^ {\prime}&x _ {2}\\\vdots&\ddots&\vdots&\vdots\\a _ {n} ^ {h}&\dots&a _ {h} ^ {n}&x _ {n}\end{array}\right) = h ^ {\prime} \rightarrow
$$

e la dimensione di W 

poiche l'ultima colonna
deve essere comb. linea.
delle preadenti 

matrice costituita
dai vettori di B
avente rango h 

$$
\begin{array}{l} \text {Colonna costituita} \\ \text {dal vettore u} \end{array}
$$

che usiamo. 

$$
W \subseteq \mathbb {R} ^ {4} W = \mathcal {L} ((1, 0, 1, 1), (2, 1, 2, 3)) d i m W = 2
$$

$$
\text {   rango   } \left(\begin{array}{c c c}1&2&x _ {1}\\0&1&x _ {1}\\1&2&x _ {1}\\1&3&x _ {1}\end{array}\right) = 2 \quad\begin{array}{l}a ^ {3} \rightarrow a ^ {2} - a ^ {2}\\a ^ {2} \rightarrow a ^ {3} - a ^ {3}\end{array}\quad \left(\begin{array}{c c c}1&2&x _ {1}\\0&1&x _ {1}\\0&0&x _ {1} - x _ {1}\\0&1&x _ {1} - x _ {1}\end{array}\right) \quad a ^ {4} \rightarrow a ^ {4} - a ^ {4} \left(\begin{array}{c c c}1&2&x _ {1}\\0&1&x _ {1}\\0&0&\{x _ {1}, - x _ {1} \} = 0\\0&0&\{x _ {1}, - x _ {1} - x _ {2} = 0 \}\end{array}\right)
$$

$$
W = \mathcal {L} ((2, 1, 0, 3, 1), (2, - 1, 1, 4, 0)) \leq R ^ {5} \quad d i m W = 2
$$

$$
\left(\begin{array}{c c}2&x _ {1}\\1&- 1\\0&1\\3&4\\1&0\\0&x _ {1}\end{array}\right) \quad \text {per   constant} \left(\begin{array}{c c}1&- 1\\2&x _ {1}\\0&1\\3&4\\1&0\\0&x _ {1}\end{array}\right) \quad\begin{array}{l}a ^ {k} \rightarrow a ^ {k} - 2 a ^ {k}\\a ^ {k} \rightarrow a ^ {k} - 2 a ^ {k}\\a ^ {k} \rightarrow a ^ {k} - 2 a ^ {k}\\a ^ {k} \rightarrow a ^ {k} - 2 a ^ {k}\end{array}\quad \left(\begin{array}{c c}1&- 1\\0&y _ {1} - 2 x _ {1}\\0&x _ {1}\\0&x _ {1}\\0&x _ {1} - 3 x _ {1}\\0&x _ {1} - x _ {1}\end{array}\right) \quad \text {per   constant} \left(\begin{array}{c c}1&- 1\\0&x _ {1}\\0&y _ {1} - 2 x _ {1}\\0&x _ {1} - 3 x _ {1}\\0&x _ {1} - x _ {1}\end{array}\right) \quad\begin{array}{l}a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}\\a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}\\a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}\\a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}\\a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}.\\a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}.\\a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}.\\a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}.\\a ^ {k} \rightarrow a ^ {k} - 4 a ^ {k}.\\a ^ {k} \rightarrow a ^ {k} - 2 x _ {1}, - x _ {2}, = 0\\a ^ {k} \rightarrow a ^ {k} - 2 x _ {1}, - x _ {2}, = 0\\a ^ {k} \rightarrow a ^ {k} - 2 x _ {1}, - x _ {2}, = 0\\a ^ {k} \rightarrow a ^ {k} - x _ {1}, - x _ {2}, = 0\\a ^ {k} \rightarrow a ^ {k} - x _ {1}, - x _ {2}, = 0\\a ^ {k} \rightarrow a ^ {k} - x _ {1}, - x _ {2}, = 0\\a ^ {k} \rightarrow a ^ {k} - x _ {1}, - x _ {2}, = 0\\b (x _ {1}) = b (x _ {2}) = b (x _ {3}) = b (x _ {4}) = b (x _ {5}) = b (x _ {6}) = b (x _ {7}) = b (x _ {8}) = b (x _ {9}) = b (x _ {1 0}) = b (x _ {1 1}) = b (x _ {1 2}) = b (x _ {1 3}) = b (x _ {1 4}) = b (x _ {1 5}) = b (x _ {1 6}) = b (x _ {1 7}) = b (x _ {1 8}) = b (x _ {1 9}) = b (x _ {2 0}) = b (x _ {2 1}) = b (x _ {2 2}) = b (x _ {2 3}) = b (x _ {2 4}) = b (x _ {2 5}) = b (x _ {2 6}) = b (x _ {2 7}) = b (x _ {2 8}) = b (x _ {2 9}) = b (x _ {3 0}) = b (x _ {3 1}) = b (x _ {3 2}) = b (x _ {3 3}) = b (x _ {3 4}) = b (x _ {3 5}) = b (x _ {3 6}) = b (x _ {3 7}) = b (x _ {3 8}) = b (x _ {3 9}) = b (x _ {4 0}) = b (x _ {4 1}) = b (x _ {4 2}) = b (x _ {4 3}) = b (x _ {4 4}) = b (x _ {4 5}) = b (x _ {4 6}) = b (x _ {4 7}) = b (x _ {4 8}) = b (x _ {4 9}) = b (x _ {5 0}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{min}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{min}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}) = b (x _ {\mathrm{max}}, y) = b (x, y) + b (y, z) + c (z, y) + d (z, z) + e (z, z) + f (z, z) + g (z, z) + h (z, z) + i (z, z) + j (z, z) + k (z, z) + l (z, z) + m (z, z) + n (z, z) + o (z, z) + p (z, z) + q (z, z) + r (z, z) + s (z, z) + t (z, z) + u (z, z) + v (z, z) + w (z, z) + x (z, z) + y (z, z) + z (z, z) + w (z, z) + x (z, z) + y (z, z) + z (z, z) + w (z, z) + y (z, z) + z (z, z) + y (z, z) + w (z, z) + y (z, z) + z (z, z) + y (z, z) + w (z, z) + w (z, z) + y (z, z) + y (z, z).\end{array}
$$

## RAPPRESENTAZIONE CARTESIANA

Sia V uno spazio finitamente generato su k, avente dim=n. Consideriamo B=(e1..en) 

una base ordinata di V. Consideniamo l'isomorfismo associato a B $\Phi_{8}:V\to K^{0}$ 

abbiamo che ∀WSV sappiamo che $\phi_{8}(w)$ e un sottospazio vettoriale di $K^{n}$ . 

$W = S_{0} \sum_{0}: A X = 0 \text{ e}^{-\text{ rappresentazione cartesiana di U nella base B.}}$ 

## RAPPRESENTAZIONE PARAMETRICA

Sia B = (ω₁, ..., ωₙ) una base di ω. E naturalmente sappiamo che ω = L(B), considero 

on vettore $u = (x_1, \ldots, x_n) \in K^n$ , sappiamo che $u \in W = L(B) \Leftrightarrow \exists t_1, \ldots, t_{\text{th}} \in K$ : 

$$
(x _ {1}, \dots , x _ {n}) = t _ {1} (a _ {1} ^ {\prime}, a _ {1} ^ {2}, \dots , a _ {1} ^ {n}) + t _ {2} (a _ {2} ^ {\prime}, a _ {2} ^ {2}, \dots , a _ {2} ^ {n}) + \dots + t _ {n} (a _ {n} ^ {\prime}, \dots , a _ {n} ^ {m})
$$

la quale può essere scritta come: 

tale rappresentazione 

e' detta parametrica 

$$
x _ {m} = t _ {1} a _ {1} ^ {m} + \dots + t _ {n} a _ {n} ^ {m}
$$

## TEOREMA Di KRAMER

Sia Σ un sistema di equazioni lineari tali che Ax=b con A che è una mattica quadrata.
Se $JA^{-1}$ , allora l'insieme delle soluzioni e fatta da un solo elemento cice: $S=\{A^{-1}b\}$ 

$$
\text { Per   ipotesi   A   e- invertibile,   ossia:   } \mathcal {I} _ {A ^ {- 1}} \in M n (K) \setminus A A ^ {- 1} = A ^ {- 1} A = I n ^ {\prime}
$$

Allora consideriamo Ax=b e moltiplicchiamo entrambi i membri per A $^{-1}$ Abbiamo 

cos: $A^{-1}(AX) = A^{-1}b$ , poiche il prodotto righe x colonne e' associativa, posso scrivere 

$$
(A ^ {- 1} A) x = A ^ {- 1} b
$$

biamo un'unica soluzione cioe: $X = A^{-1} \underline{b}$ 

Lezione 13: ${1}^{9}$ Prova intercorso ! 

## LEZIONE 14

DETERMINANTE DI UNA MATRICE 

$$
\text {   Una   matrice   } A \in M n (K) \text {   si   dice   S Michigana   se   } \forall i, j \in \{1, \dots , n \} a _ {j} ^ {i} = a _ {i} ^ {j} \rightarrow \left(\begin{array}{l l l}1&2&- 7\\2&0&1\\- 7&1&3\end{array}\right)
$$

$$
\text {   A   si   dice   ANTISINMETRICA   se   } \forall i, j \in \{1, \dots , n \} a _ {j} ^ {\prime} = - a _ {j} ^ {\prime} \Leftrightarrow \left( \begin{array}{l l l l} 0 & - 1 & 2 & - 5 \\ 1 & 0 & 7 & 1 0 \\ - 2 & - 1 & 0 & 0 \\ 5 & - 1 0 & 0 & 0 \end{array} \right)
$$

$$
\text {   A   si   dia   DIAGONALE   se   } \forall i, j \in \{1, \dots , n \}: i \neq j \text {   allora   } a _ {j} ^ {i} = 0 \rightarrow \left(\begin{array}{r r r}1&- 2&3\\2&0&- 1\\- 3&1&1\end{array}\right)
$$

DEF Sia la permutazione Fe Pn ,diciamo che f presenta un' inversione se: 

$$
\exists i, j \in \{1, \dots , n \} \mid i <   j e F (i) > F (j)
$$

oss: Se S e un' insieme finito, una permutazione di S e un' applicazione biettiva di S 

in se. In particolare si indica con Ph l'insieme delle permutazioni di 11,...,nf ouvero le 

appli cazioni F: {1,...,n} → {1,...,n} | Fe-biettiva 

Modi PER RICAVARE IL DETERMINANTE 

Ricordiamo la definizione: Il determinante di una matrice e un numero associa-

to a ciascuna materia quadrata e ne esprime alcune proprietat' algebriche e geometriche. 

Per matrici 3x3 e possibile applicare la regola di Sarius : 

$$
\left( \begin{array}{c c c} a _ {1} ^ {\prime} & a _ {2} ^ {\prime} & a _ {3} ^ {\prime} \\ a _ {1} ^ {2} & a _ {2} ^ {2} & a _ {3} ^ {2} \\ a _ {1} ^ {3} & a _ {2} ^ {3} & a _ {3} ^ {3} \end{array} \right) \left( \begin{array}{c c c} a _ {1} ^ {\prime} & a _ {2} ^ {\prime} \\ a _ {1} ^ {2} & a _ {2} ^ {2} \\ a _ {1} ^ {3} & a _ {2} ^ {3} \end{array} \right) \quad \begin{array}{l l l} - s o t t r a g g o \\ - a d d i z i o n o \end{array}
$$

$$
A = \left( \begin{array}{r r r} 2 & - 1 & 2 \\ 0 & 1 & - 1 \\ 3 & - 2 & 1 \end{array} \right) \begin{array}{r r r} 2 & - 1 \\ 0 & 1 \\ 3 & - 2 \end{array}
$$

$$
\vert A \vert = \{(2 \cdot 1. 1) + (- 1. - 1. 3) + (2 \cdot 0. - 2) - (- 1 \cdot 0. 1) - (2 \cdot - 1. - 2) - (2 \cdot 1. 3) \}
$$

$$
\begin{array}{c c c c c c c c c} 1 & & & & & \\ 2 & + & + 3 & + & 0 & - & 0 & - & (+ 4) & - & 6 \end{array}
$$

$$
5 - 1 0 = - 5
$$

Si può dimostrare che esiste un'unica applicazione da Mn(k) in k che 

ad ogni matrice A → det(A) 

Tale applicazione ha le seguenti proprietà: 

- il determinante della motrice identica e 1 

Se B e la matrice attenuta da A: 

- Scambiando 2 righe, allora |B| = -|A| 

- moltiplicando una riga per uno scalare $\alpha \varepsilon k$ allora |B| = $\alpha$ |A| 

- applicando la $3^{9}$ operazione elementare di rigga allora |B| = |A| 

- il determinante della matrice $e^{-} =$ al det. della trasposta. 

OSS: Dalle proprietà del determinante si deduce che se B è la matrice ottenuta da A applicando un numero finito di operazioni elementari allora $|B| \neq 0 \rightarrow |A| \neq 0$ 

DEF Suppongo che A sia una matrice NON necessariamente quadrata. Suppongo m,n∈N, consi-

dero k ≤ H in {m, n} 

$$
A = \left( \begin{array}{c c} a _ {1} ^ {\prime} & a _ {n} ^ {\prime} \\ a _ {1} ^ {m} & a _ {n} ^ {m} \end{array} \right)
$$

Fisso K indici di riga
e K indici di colonna 

Definisco il minore di A , individuato da tali indici di riga e calonna fissati, la sottomatrice quadrata di A formata dagli elementi di A in cui si incrociano le rispettive righe e colonne. 

Se A è quadrata possiamo individuare alcuni minori molto particolari di
A: comunque fisso i, jε {1,...,n} cancello la riga iesima e colonna j-esima, il minore 

rimanente si dice minore complementare di $a_{j}^{i}$ e si indica com $M_{j}^{i}$ . 

Il complemento algebrico di $a_{j}^{i}$ , indicato con $A_{j}^{i}$ e' $(-1)^{i+j}$ . $|M_{j}^{i}|$ 

determinante del
minore complem. 

ESEMPiO: 

$$
A = \left( \begin{array}{c c c} - 2 & 3 & 5 \\ 0 & 1 & - 1 \\ 7 & - 6 & 3 \end{array} \right)
$$

$$
a _ {2} ^ {3} = - 6
$$

$$
M _ {2} ^ {3} = \left( \begin{array}{l l} - 2 & 5 \\ 0 & - 1 \end{array} \right)
$$

$$
\vert M _ {2} ^ {3} \vert = 2
$$

$$
A _ {2} ^ {3} = (- 1) ^ {3 + 2} \cdot 2 = - 2
$$

Considero una matrice $A \in M_{n}(K)$ , dunque quadrata, il teorema dice che: 

$$
\cdot \forall k \in \{1, \dots , n \} | A | = a _ {1} ^ {k} A _ {1} ^ {k} + \dots + a _ {n} ^ {k} A _ {n} ^ {k}
$$

$$
\cdot \forall j \in \{1, \dots , n \} | A | = a _ {j} ^ {\prime} A _ {j} ^ {\prime} + \dots + a _ {j} ^ {n} A _ {j} ^ {n}
$$

$$
A _ {3} ^ {2} (- 1) ^ {2 + 3} \cdot \left( \begin{array}{l l l} 3 & 2 & 0 \\ 1 & 1 & - 1 \\ 0 & - 1 & 1 \end{array} \right) \quad | A | = 1 \cdot A _ {1} ^ {2} + 1 A _ {2} ^ {2} + 2 A _ {3} ^ {2} + 1 A _ {4} ^ {2}
$$

$$
A _ {4} ^ {2} (- 1) ^ {2 + 4} \cdot \left( \begin{array}{l l l} 3 & 2 & 1 \\ 1 & 1 & - 1 \\ 0 & - 1 & 0 \end{array} \right)
$$

Prop: Sià la matrice A ∈ Mn(k) triangolare superiore allora: 

$$
| A | = a _ {1} ^ {\prime} \cdot a _ {2} ^ {2} \cdot \dots \cdot a _ {n} ^ {n} - \text { prodotto   degli   elem.   sulla   diagonale   princ. }
$$

$$
(r i s p e t t i v a m e n t e \text { anche   per   le   matrici   triangolari   inferiori. }
$$

$$
\text {   Per   induzione:   } n = 1 \quad B = (b _ {1} ^ {\prime}) \quad | B | = b _ {1} ^ {\prime} \quad \checkmark
$$

$$
B = \left( \begin{array}{c c c} b _ {1} ^ {\prime} & & \\ b _ {1} ^ {\prime} & b _ {1} ^ {\prime} & \\ 0 & 0 & b _ {n} ^ {n} \\ 0 & \dots & 0 \end{array} \right) \quad \begin{array}{l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l} n = 1 & B = (b _ {1} ^ {\prime}) & | B | = b _ {1} ^ {\prime}, & \checkmark \\ n > 1 & & & \\ n - 1 = > n & | B ^ {\prime} | = b _ {2} ^ {2} b _ {3} ^ {3} \dots b _ {n} ^ {n} & p e a i p o t e s w. \end{array}
$$

$$
\text { Applicchiano   el   Teorema   di   Laplace   svoluppando   1B1   rispetto   alla   prima   colonna: } J = 1
$$

$$
\vert B \vert = b _ {1} ^ {\prime}, B _ {1} ^ {\prime} + o + \dots + o = b _ {1} ^ {\prime} \vert B ^ {\prime} \vert (- 1) ^ {n + 1} = b _ {1} ^ {\prime} b _ {2} ^ {2} \dots b _ {n} ^ {n}. \quad \text {   Ⅲ   }
$$

$$
B = \left( \begin{array}{l l l} 2 & 1 & 7 \\ 0 & 3 & - 1 \\ 0 & 0 & 5 \end{array} \right) \quad | B | = 2. 3. 5 = 3 0
$$

$$
\text { COROLLARIO }
$$

Sia B una matrice a gradini ottenuta da A. 

$$
\vert A \vert \neq 0 \Leftrightarrow \vert B \vert \neq 0 \Leftrightarrow n. \# p i v o t B \Leftrightarrow r a n g o (B) = n = r a n g o (A).
$$

$$
\text { Inoltre   possiamo   osservare   che } | A | = 0 \Leftrightarrow \operatorname{ranop} (A) <   n
$$

$$
\text { Siano   le   matrici } A, B \in M _ {n} (K) \text { allora } | A \cdot B | = | A | \cdot | B |
$$

## 2° TEORETIA DI LAPLACE

Considero una matrice Aε Mn(K), dunque quadrata, il teorema dice che: 

$$
\cdot \forall i, h \in \{1, \dots , n \}, i \neq h a _ {i} ^ {n} A _ {i} ^ {i} + \dots + a _ {n} ^ {n} A _ {n} ^ {i} = 0
$$

$$
\cdot \forall k, j \in \{1, \dots , n \}, k \neq j a _ {k} ^ {1} A _ {j} ^ {1} + \dots + a _ {k} ^ {n} A _ {j} ^ {n} = 0
$$

## Ricapitolando:

Il 1º teorema di Laplace afferma che il determinante di una matrice quadrata M di ordine n è pari alla somma dei prodotti degli elementi di una riga qualsiasi (o una calonna qualsiasi) per i rispettivi complementi algebrici. 

Il 2º teorema afferma che è sempre nulla la somma dei prodotti degli elementi di una riga (o colonna) per i complementi algebrici di un'attra riga (o colonna) della matrice stessa. 

Con lo sviluppo di Laplace si può verificare, che il determinante di una matrice diagonale è il prodotto dei valori sulla diagonale, che il determinante di una matrice triangolare è ancora il prodotto dei valori sulla diagonale o che gli autovalori di una matrice triangolare sono gli elementi sulla diagonale. 

TEOREMA GENERALIZZATO DI LAPLACE 

$$
\forall k, n \in \{1, \dots , n \}, a _ {1} ^ {k} A _ {1} ^ {n} + \dots + a _ {n} ^ {k} A _ {n} ^ {n} = \delta_ {n} ^ {k} | A |
$$

$$
S _ {k} ^ {h} = \left\{ \begin{array}{l l} 1 & \text { se } h = k \\ 0 & \text { se } h \neq k \end{array} \right.
$$

$$
\forall j, e \in \{1, \dots , n \}, a _ {j} ^ {\prime} A _ {e} ^ {\prime} + \dots + a _ {j} ^ {n} A _ {e} ^ {n} S e ^ {j} | A |
$$

Prima di procedere ricordiamo Aε Mn(K) e invertibile <=> 

$$
\exists B = A ^ {- 1} \in M n (k): A B = I n = B A
$$

TEOREMA Considero la matrice quadrata A E Mn (K) abbiamo che A è invertibile 

$$
\text {   aice:   } \exists A ^ {- 1} \in \mathbb {N} _ {n} (K) \Longleftrightarrow | A | \neq 0
$$

⇒ Per ipotesi sappiamo che A e invertibile dunque $\ln = A^{-1}A$ ma noi sappiamo che $\left|\ln\right| = 1$ dunque $\left|\ln\right| = \left|A^{-1}A\right|$ il che implica che $\left|A^{-1}A\right|$ che per il teorema di Binet e $\left|A^{-1}\right| \cdot \left|A\right| = 1$ allora possiamo dire che $\left|A\right| \neq 0$ 

<= Considero $A=\begin{pmatrix}a_{1} & a_{2}^{\prime} & \cdots & a_{n}^{\prime}\\ : & & & \\ a_{1}^{m} & \cdots & a_{n}^{m}\end{pmatrix}$ e la matrice $A^{\#}$ che al posto di ogni elem. di A ha il rispettivo complemento algebrico 

Abbiamo bisogno del 1º e 2º teorema di Laplace; quindi prendiamo 

$$
2 \text {   india   di   riga   } \forall h, i \in \{1, \ldots , n \} a _ {1} ^ {h} A _ {1} ^ {i} + \ldots + a _ {n} ^ {h} A _ {n} ^ {i} = \delta_ {i} ^ {h} | A |
$$

$$
e 2 \text {   indici   di   colonna:   } \forall k, j \in \{1, \dots , n \} a _ {k} ^ {\prime} A _ {j} ^ {\prime} + \dots + a _ {k} ^ {n} A _ {j} ^ {n} = \int_ {j} ^ {k} | A |
$$

con $\int_{j}^{i}$ che e 1 se i = j altrimenti vale 0. 

$$
A ^ {t} (A ^ {*}) = \left( \begin{array}{l l} a _ {1} ^ {i} & a _ {n} ^ {i} \\ a _ {1} ^ {h} & a _ {n} ^ {h} \\ \vdots & \vdots \\ a _ {1} ^ {n} & a _ {n} ^ {n} \end{array} \right) \cdot \left( \begin{array}{l l l l l} A _ {1} ^ {i} & \dots & A _ {1} ^ {i} & \dots & A _ {1} ^ {n} \\ \vdots & & & & \\ A _ {n} ^ {i} & \dots & A _ {n} ^ {i} & \dots & A _ {n} ^ {n} \end{array} \right)
$$

$$
h, i \quad \text { esso } e ^ {-}: a _ {1} ^ {h} A _ {1} ^ {i} + \dots + a _ {n} ^ {h} A _ {n} ^ {i}
$$

abbiamo quindi che $A \cdot (A^{*}) = \begin{pmatrix} |A| & 0 & 0 \\ 0 & |A| & 0 \\ 0 & 0 & |A| \end{pmatrix}$ - matrice che sulla diagonale principale, i determinanti di A e tutti O nelle attre posizioni 

analogamente se consideriamo $^{t}(A^{\#})$ : A e prendiamo l'elemento di posto (j,k)e 

$$
A _ {J} ^ {\prime} a _ {K} ^ {\prime} + \dots + A _ {J} ^ {n} a _ {K} ^ {n} = \int_ {J} ^ {K} | A |
$$

$$
\text {   mo   } \cos \alpha \text {   la   nostra   TESI   ciao:   } A ^ {- 1} = \frac {1}{| A |} t (A ^ {\#})
$$

$$
t (A ^ {\#}) \cdot A = \left( \begin{array}{c c c c} | A | & 0 & \dots & 0 \\ 0 & | A | & \dots & 0 \\ \vdots & & | A | & 0 \\ 0 & \dots & \dots & | A | \end{array} \right)
$$

$$
A = \left( \begin{array}{l l l} 2 & - 1 & 2 \\ 0 & 1 & - 1 \\ 3 & - 2 & 1 \end{array} \right) \quad | A | = 2 + 3 + 0 - 6 - 4 - 0 = - 5 \neq 0.
$$

$$
A _ {1} ^ {1} = (- 1) ^ {2} \left| _ {- 2} ^ {1} - _ {1} ^ {1} \right| = - 1 \quad A _ {2} ^ {1} = (- 1) ^ {3} \left| _ {3} ^ {0} - _ {1} ^ {1} \right| = - 3 \quad A _ {3} ^ {1} = (- 1) ^ {4} \left| _ {3} ^ {0} - _ {2} ^ {1} \right| = - 3
$$

$$
A _ {1} ^ {2} = (- 1) ^ {3} \left| \begin{array}{l l} - 1 & 2 \\ - 2 & 1 \end{array} \right| = - 3 \quad A _ {2} ^ {2} = (- 1) ^ {4} \left| \begin{array}{l l} 2 & 2 \\ 3 & 1 \end{array} \right| = - 4 \quad A _ {3} ^ {2} = (- 1) ^ {5} \left| \begin{array}{l l} 2 & - 1 \\ 3 & - 2 \end{array} \right| = 1
$$

$$
A _ {1} ^ {3} = (- 1) ^ {4} \left| \begin{array}{l l} - 1 & 2 \\ 1 & - 1 \end{array} \right| = - 1 \quad A _ {2} ^ {3} = (- 1) ^ {5} \left| \begin{array}{l l} 2 & 1 \\ 0 & - 1 \end{array} \right| = 2 \quad A _ {3} ^ {3} = (- 1) ^ {6} \left| \begin{array}{l l} 2 & - 1 \\ 0 & 1 \end{array} \right| = 2
$$

$$
A ^ {- 1} = \frac {1}{- 5} \left( \begin{array}{l l l} - 1 & - 3 & - 1 \\ - 3 & - 4 & 2 \\ - 3 & 1 & 2 \end{array} \right) = \left( \begin{array}{l l l} 1 / 5 & 3 / 5 & 1 / 5 \\ 3 / 5 & 4 / 5 & - 2 / 5 \\ 3 / 5 & - 1 / 5 & - 2 / 5 \end{array} \right) = B
$$

$$
E ^ {\prime} \text { possibile   controllano   sei   calcoli   sono   giusti.   Ad   esempio, } (a _ {1} ^ {\prime}, a _ {2} ^ {\prime}, a _ {3} ^ {\prime}) (b _ {1} ^ {\prime}, b _ {1} ^ {2}, b _ {1} ^ {3}) = (2, - 1, 2) (\frac {1}{5}, \frac {3}{5}, \frac {3}{5}) = \frac {2}{5} \cdot \frac {3}{5} + \frac {6}{5} = \frac {5}{5} = 1
$$

## LEZIONE 15

## ORLATI DI UNA MATRICE

Sia A una matrice con m righe e n calonne : 

- una sottomatrice di A e'una qualsiasi matrice estratta da A eliminando un numero arbitrario di righe e/o colonne 

- Detta A' una sottomatrice di A, prende il nome di sottomatrice orlata ogni ma-
trace ottenuta da A' aggiungendo una riga e una colonna di A 

- Un minore di A di ordine p e definito come il determinante di una qualsiasi 

- Un minore orlato e' invece il determinante di una sottomatrice di ordine p+1 ottenuta
orlando una sottomatrice di A di ordine p
ESEmpio 

$$
A = \left( \begin{array}{c c c} 7 & 8 & - 1 \\ \hline 2 & - 1 & 0 \\ \hline - 3 & 6 & - 5 \\ \end{array} \right)
$$

$M = \begin{pmatrix} 8 & 1 \\ 6 & 4 \end{pmatrix} \leftarrow$ devo necessariamente prendere le colonne $(2^{9} e 4^{9})$ e le righe $(1^{9} e 3^{9})$ su cui vi sono 

ha ordine 2
2 < min {3,4} = 3

gli elementi di M. Per M', posso scegliere 1 $^{9}$ o 3 $^{9}$ donna, e 2 $^{9}$ riga. Ad esempio M' = (78)
(2 - 3)
(364) 

TEOREMA DEGU ORLATI (ODI KRONOCKER) 

Sia una matrice A di tipo mxn, il teorema dice che 

rango (A) = r $\Leftrightarrow$ 3 un minore M di A di ordine r tale che |M| ≠ 0 e: 

• tutti gli orlati di M hanno determinante nullo 

MATRICI ASSOCIATE 

TEOREMA Di CARATTERIZZAZIONE 

Consideriamo V, W 2 spazi vettoriali finitamente generati su K con dimV=n e dimW=m
Considero un applicazione lineare T: V → W e 2 basi B = (u₁, ..., uₙ) base ordinata di V e B' = (u₁', ..., uₘ') base ordinata di W. 

Il teorema dia: 3 un'unica matrice A∈Hn,n(k) tale che: 

$\forall y \in V$ prendiamo $u \equiv_{B}(x_1, \ldots, x_n)$ e $T(u) \equiv_{B'}(y_1, \ldots, y_m)$ si ha che: $A = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix}$ A si dice matrice associata a T nelle basi Be B! Si indica con $M_{BB'}$ 

$$
A = \left( \begin{array}{c c} a _ {1} ^ {\prime} & a _ {n} ^ {\prime} \\ a _ {1} ^ {m} & a _ {n} ^ {m} \end{array} \right) \quad \begin{array}{l} u = x _ {1} e _ {1} + \dots + x _ {n} e _ {n} \\ T (u) = T (x _ {1} e _ {1} + \dots + x _ {n} e _ {n}) = x _ {1} T (e _ {1}) + \dots + x _ {n} T (e _ {n}) = x _ {1} (a _ {1} ^ {\prime} e _ {1} ^ {\prime} + \dots + a _ {1} ^ {m} e _ {m} ^ {\prime}) + \dots \end{array}
$$

$$
\ldots + x n (q _ {n} ^ {1} e _ {1} ^ {\prime} + \ldots + q _ {n} ^ {m} e _ {m} ^ {\prime}) = q _ {1} ^ {\prime} x _ {1} e _ {1} ^ {\prime} + \ldots + q _ {1} ^ {m} x _ {1} e _ {m} ^ {\prime} + \ldots + q _ {n} ^ {1} x _ {n} e _ {1} ^ {\prime} + \ldots + q _ {n} ^ {m} x _ {n} e _ {m} ^ {\prime} = (q _ {1} ^ {\prime} x _ {1} + \ldots + q _ {n} ^ {\prime} x _ {n}) e _ {1} ^ {\prime} + \ldots
$$

$$
\ldots + (a _ {1} ^ {m} x _ {1} + \ldots + a _ {n} ^ {m} x _ {n}) e ^ {i m} \Rightarrow \left( \begin{array}{c} y _ {1} \\ \vdots \\ y _ {m} \end{array} \right) = \left( \begin{array}{c c} a _ {1} ^ {2} x _ {1} + \ldots + a _ {n} ^ {2} x _ {n} \\ \vdots & \vdots \\ a _ {1} ^ {m} x _ {1} + \ldots + a _ {n} ^ {m} x _ {n} \end{array} \right) = A \left( \begin{array}{c} x _ {1} \\ \vdots \\ x _ {0} \end{array} \right) \leftarrow \text {   abbiamo   dimostrato   che   A   esiste,   manca   da   dimostrare   l'unicitat.   }
$$

Considero $B \in M_{m \times n}(K)$ tale che $B\begin{pmatrix} x_{1} \\ x_{n} \\ x_{m} \end{pmatrix} = \begin{pmatrix} y_{1} \\ y_{m} \end{pmatrix}$ devo dimostrare che B = A, prendo $y = y_{1} \equiv_{B}(1,0,\ldots,0)$ allora 

$$
B \cdot \left( \begin{array}{c} 1 \\ 0 \\ \vdots \\ 0 \end{array} \right) = \left( \begin{array}{c} a _ {1} ^ {\prime} \\ a _ {1} ^ {\prime} \\ \vdots \\ a _ {1} ^ {m} \end{array} \right) = \underline {{a _ {1}}} \quad \text {   1   } ^ {9} \text {   colonna   oli   A   }
$$

Ma anche se considero $u=4n=(0,0\ldots,1)$ allora $bn=B\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}a^{n}\\a^{m}\end{pmatrix}=an$ dunque bn=an di conseguenza poiché 

tutte le colonne di B e A sono uguali allora B=A 

$$
T: \mathbb {R} ^ {2} \rightarrow \mathbb {R} [ x ] \leq 2
$$

$$
\text { Costruiamo } M _ {B B ^ {\prime}} (T):
$$

$$
(a, b) \rightarrow a + b + (a - b) x + (2 a + b) x ^ {2}
$$

$$
T (1, 1), (1, - 1) \equiv_ {B} (2, 0, 3)
$$

$$
B = ((1, 1), (1, - 1)) \text {   base   ordinata   di   } \mathbb {R}
$$

$$
T (1, - 1) = 2 x + x ^ {2} \equiv_ {B} (0, 2, 1)
$$

$$
B ^ {\prime} = (1, x, x ^ {2}) \quad \text { base   canonica } \quad \text { di } \quad \mathbb {R} [ x ] \leq 2
$$

$$
M _ {B B ^ {\prime}} (T) = \left( \begin{array}{l l} 2 & 0 \\ 0 & 2 \\ 3 & 1 \end{array} \right) \leftarrow \text { rappresenta } T
$$

$$
V \xrightarrow {T} W
$$

$$
(x _ {1}, \dots , x _ {n}) \in k ^ {n}
$$

$$
\phi_ {B} ^ {- 1} (x _ {1}, \dots , x _ {n}) = u
$$

$$
y \equiv_ {B} (x _ {1}, \dots , x _ {n})
$$

$$
k ^ {n} \underset {\tilde {r}} {- - } > k ^ {m}
$$

$$
T (\phi_ {B} ^ {- 1} (x _ {1}, \dots , x _ {n})) = T (u)
$$

$$
\phi_ {B _ {1}} (T (\phi_ {B} (x _ {1}, \dots , x _ {n})) = \phi_ {B ^ {\prime}} (T (u)) = (y _ {1}, \dots , y _ {m}) = A \left( \begin{array}{c} x _ {1} \\ \vdots \\ x _ {n} \end{array} \right)
$$

## LEZIONE 16

## MATRICI Di PASSAGGIO

Sia V uno spazio vettoriale di dimensione n consideriamo l'applicazione identica idv: V→V e 

Un'applicazione lineare. Se Fissiamo 2 basi $B = (u_1, \ldots, u_n)$ . $\vec{B} : (\vec{u}_1, \ldots, \vec{u}_n)$ con B base del domi-

nio e B base del codominio. La matrice Ilgè si dice matrice di passaggio da B a B oppure matri-

ce di cambiamento di base. 

$$
i d v: M _ {2} R \rightarrow M _ {2} (\mathbb {R})
$$

$$
B = \left( \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right), \left( \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right), \left( \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right), \left( \begin{array}{l l} 0 & 0 \\ 0 & 1 \end{array} \right)
$$

$$
\left( \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right) = \overline {{B}} (0, 1, - 1, 1)
$$

$$
\overline {{B}} = \left( \begin{array}{l l} 0 & 1 \\ 0 & 1 \end{array} \right), \left( \begin{array}{l l} 1 & 0 \\ 1 & 0 \end{array} \right), \left( \begin{array}{l l} 0 & 0 \\ 1 & 1 \end{array} \right), \left( \begin{array}{l l} 0 & 0 \\ 0 & 1 \end{array} \right)
$$

$$
\left( \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right) = \overline {{B}} (1, 0, 0, - 1)
$$

$$
\left( \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right) = \overline {{B}} (0, 0, 1, - 1)
$$

$$
\phi_ {B}: M _ {2} (\mathbb {R}) \rightarrow \mathbb {R} ^ {4}
$$

$$
\left( \begin{array}{l l} 0 & 0 \\ 0 & 1 \end{array} \right) = \bar {B} (0, 0, 0, 1)
$$

$$
\left( \begin{array}{l l} a & b \\ c & d \end{array} \right) \sim (b, a, c - a, a - b - c + a)
$$

$$
A = \left( \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ - 1 & 0 & 1 & 0 \\ 1 & - 1 & - 1 & 1 \end{array} \right)
$$

$$
\operatorname{range} (A) = 4 = \dim (\mathrm{id} V)
$$

OSS: La matrice di passaggio hanno range massimo poiche sono invertibili 

OSS: Consideriamo l'applicazione identica id: V → V con B base di V(dominio) e B base di V (codominio). Consideriamo la matrice A = πgē (idV) 

Per il teorema di caratterizzazione: 

consideriamo $u \in V$ abbiamo che $u \equiv_{B}(x_1, \ldots, x_n)$ e naturalmente $u \equiv_{B}(\overline{x_1}, \ldots, \overline{x_n})$ 

abbiamo che $A\begin{pmatrix}x_{1}\\ \vdots\\ x_{n}\end{pmatrix}=\begin{pmatrix}\overline{x_{1}}\\ \vdots\\\overline{x_{n}}\end{pmatrix}$ . 

Dunque per il teorema di caratterizzazione le matricia di passaggio trasformano le componenti di un vettore in una base ordinata, nelle componenti dello stesso vettore in un'altra base ordinata. 

## MATRICi Simili

Siano E, E 2 matrici quadrate dunque E, E ∈ Mn(K), E si dice simile a E se: 

$\exists P \in \text{Gen}(k), P \text{ invertibile}: E = P^{-1} \cdot \bar{E} \cdot P$ 

gruppo lineare
generato su
campo k 

La Similitudine tra matricia quadrate dello stesso ordine e una relazione d'equivalenza infatti: 

-e riflessiva poiche $E = I_n^{-1} \cdot E \cdot I_n$ 

-e Simmetrica se $E = P^{-1} \cdot \bar{E} \cdot P$ . Poniamo $Q = P^{-1}$ moltipliciamo a dx e sx per P dunque 

$PE = P(P^{-1}\overline{E}P) = (P \cdot P^{-1})\overline{E}P = I_{n}\overline{E} \cdot P = \overline{E}P$ moltiplico poi entrambi i membri per $P^{-1}$ 

$$
P E P ^ {- 1} = (\overline {{E}} P) \cdot P ^ {- 1} = \overline {{E}} \cdot \ln = \overline {{E}}.
$$

considerando $Q = P^{-1}$ , $Q^{-1} \cdot E \cdot Q = \overline{E}$ quindi ho dimo-

$$
\text { strato   che } E \text { e } \text { simile } a E
$$

AUTOVALORI, AUTOVETTORI e AUTOSAZI 

Consideriamo V spazio vettoriale so campo K con dim V = n e definiamo un endomorfismo T: V → V 

$\forall \lambda \in K$ possiamo definire il sottoinsieme di U $U_{1}: \{u \in V | T(u) = \lambda U\}$ 

λ sara detto autovalore di T se Uλ ≠ {0} ossia se ∃uεV{0}: T(0)=λU. 

Tutti i vettori non nulli di Uλ si dicono autovettori. 

Uλ e un sottospazio vettoriale di V, e questa cosa e da verificare: 

- sicuramente $U_{\lambda} \neq \emptyset$ poiché $\underline{0} \in U_{\lambda}$ . 

- si considerano $U, U' \in U_{\lambda}$ con $T(U) = \lambda U$ e $T(U') = \lambda U'$ . Andando a considerare $T(U + U')$ 

Sapendo che $T$ è un'applicazione lineare abbiamo che $T(U + U') = T(U) + T(U') = \lambda U + \lambda U' = \lambda (U + U') \Rightarrow$ 

$U+U' \in U\lambda$ il che vuol dire che è chiuso rispetto alla somma. lo stesso uole per il prodotto, infatti preso 

Uno scalare $d \in K$ e il vettore $u \in U\lambda$ si ha che: 

$T(\alpha u)=\alpha T(u)=\lambda(\alpha u)$ il che vua dire che e' chiuso anche rispetto al prodotto. 

Quindi Uλ e' sottospazio vettoniae di V ed e' detto autospazio relativo a λ se λ e' autovalue 

CARATTERIZZAZIONE DEGLI AUTOVALORI 

Consideriamo l'endomorfismo T: V → V con dim V = n. 

Consideriamo poi una base $B = (e_1, \dots, e_n)$ ordinata di V. 

i) uno scalare $\lambda \in K$ e autovalore di $T \Longleftarrow$ |A - X In| = 0 

ii) se $\lambda$ e autovalore di $T$ , allora $\phi_{B}(U\lambda)$ e lo spazio delle soluzioni di $(A-\lambda In)\begin{pmatrix}x_{1}\\x_{n}\end{pmatrix}=0$ 

(i) Per quanto asservato prima, abbiamo visto che $\lambda \in K$ e autovaleore di $T \Leftrightarrow 3(x_1, \ldots, x_n) \in K^n \backslash \Omega t$ : A $\left( \begin{array}{c}x_1 \\ x_n \end{array} \right) = \lambda \left( \begin{array}{c}x_1 \\ x_n \end{array} \right)$ 

Ma esso può esser visto come $A\left(\begin{matrix}x_{1}\\ x_{0}\end{matrix}\right)=\lambda\cdot I_{n}\left(\begin{matrix}x_{1}\\ \vdots\\ x_{0}\end{matrix}\right)\Rightarrow(A-\lambda I_{n})\left(\begin{matrix}x_{1}\\ x_{0}\end{matrix}\right)=0$ per il teorema di Kramer abbiamo 

$$
\vert A - \lambda I _ {n} \vert = 0
$$

ii) No Dim. 

MOLTEPLICITA e RADICI 

Consideriamo un polinomio con variabile $X$ a coefficienti in $K$ , dunque $P(x) \in K[x]$ . Un elemento 

C £K si dice radice o soluzione di P(x) se P(c) = 0 

Consideriamo uno scalare c ∈ k e un polinomio P(x) ∈ k [x]. La molteplicità algebrica di c, come 

Radice di P(x) e' il numero seguente: 

$m_{q}(c)=MAX\{k\in N\cup\{0\}\mid(x-c)^{k} \text{ divide } P(x)\}$ 

Allora se consideriamo il polinario caratteristico $P_{T}(\lambda)=|A-\lambda I|$ possiamo parlare di molteplicità 

algebrica degli autovalori in quanto soluzioni del polinomio caratteristico . Supponiamo di avere 

un autovalore $\lambda \in K$ questo implica che $U\overline{\lambda} \neq 10\}$ di conseguenza dim $U\overline{\lambda} \geq 1$ , possiamo 

allora definire la molteplicità' geometrica mg(λ) come dimensione dell'autospazio. 

PROP ∀λ autovalore di un endomorfismo T 

si ha che mg(λ) ≤ ma(λ) 

Ri capitolando 

consideriamo una matrice A ∈ Mn(K). Se J un endomorfismo T: V → V e una base 

B di V tale che $A = M_{B}(\tau)$ . Allora gli autovalori di T si dicono autovalori di A e le componenti 

in B degli autovettori di T si dicano autovettori di A se Uλ e- autospazio di T allora φB (Uλ) si 

Prop Consideriamo l'endomorfismo T: V → V. Siano λ₁, ..., λₜ autovalori a due a due distinti di T. 

Se prendiamo $v_1 \in U_{\lambda_1} \setminus \{0\}, v_2 \in U_{\lambda_2} \setminus \{0\}, \ldots, vt \in U_{\lambda_t} \setminus \{0\}$ 

Allora l'insieme $\{v_1, \ldots, v_t\}$ e-Lin. ind. 

## Dim Base d'induzione

con t=1 abbiamo un unico autovettore $v_{1}$ che per ipotesi e diverso da zero che ovviamente forma un unsieme linearmente indipendente Passo d'induzione 

consideriamo t>1 e supponiamo che l'enunciato sia vero per t-1. La tesi è che presi gli scalari $\alpha_{1},\ldots,\alpha_{t-1},\alpha_{t}\in K$ se $\alpha_{1}v_{1}+\cdots+\alpha_{t-1}v_{t-1}+\alpha_{t}v_{t}=0$ allora $\alpha_{1}=\alpha_{2}=\cdots=\alpha_{t-1}=\alpha_{t}=0$ la $1^{9}$ cosa da fare è moltiplicare tutto per $\lambda$ ottenendo $[\lambda t\alpha_{1}v_{1}+\cdots+\lambda t\alpha_{t-1}v_{t-1}+\lambda t a t v_{t}=0]$ $1^{9}$ identità la $2^{9}$ cosa da fare è calcolare l'immagine $T(\alpha_{1}v_{1}+\cdots+\alpha_{t-1}v_{t-1}+\alpha_{t}v_{t})=0$ essa diventa pero 

$\alpha_{1}T(v_{1})+\ldots+\alpha_{t-1}T(v_{t-1})+\alpha_{t}T(v_{t})=0$ che a sua volta diventa $[x_{1}\alpha_{1}v_{1}+\ldots+x_{t-1}\alpha_{t-1}v_{t-1}+x_{t}\alpha_{t}v_{t}]$ $2^{9}$ identità
Possiamo dunque sottrarre la $2^{9}$ identità alla $1^{9}$ ottenendo $(\lambda t\alpha_{1}-\alpha_{1}\lambda_{1})v_{1}+\ldots+(\lambda t\alpha_{t-1}-\alpha_{t-1}\lambda_{t})v_{t-1}=0$ Sfruttando l'ipotesi d'induzione sappiamo che $v_{1},\ldots,v_{t-1}$ sono LIN. IND. dunque gli scalari $\alpha_{1},\ldots,\alpha_{t}$ sono NULLi 

TEO Siano $\lambda_{1},\ldots,\lambda t$ autovalori di Ta due a due distinti allora la somma di $U\lambda_{1},\ldots,U\lambda t$ è una somma diretta. 

Sappiamo che somma diretta significa che $\forall h \in \{1, \ldots, t\}$ $U_{\lambda h} \cap (U_{\lambda_1} + \ldots + U_{\lambda_{h-1}} + U_{\lambda_{h+1}} + \ldots + U_{\lambda_t}) = 0$ . Dimostriamo per $h=1$ , poiché il ragionamento e analogo in tutti i casi. Si ha dunque: $U_{\lambda_1} \cap (U_{\lambda_2} + \ldots + U_{\lambda t}) = 0$ . Consideriamo dunque $U \in U_{\lambda_1} \cap (U_{\lambda_2} + \ldots + U_{\lambda_t}) = 0$ 

Il che waldire che $u \in U\lambda_1$ e $u \in (U\lambda_2 + \ldots + U\lambda t)$ ma quindi si ha che: $3u_1 \in U\lambda_1, \ldots, 3u_t \in U\lambda_t$ tali che $u = u_1 = u_2 = \ldots = u_t$ si ha dunque $u_1 - u_2 + \ldots - u_t = 0$ se in questa scrittura ci fossero dei vettori NON nulli avremmo degli autovettori relativi ad autovalori a 2 a 2 distinti e LiN. Dip e cioè è ASSUR. 

## DiAGONALIZABILE

Consideriamo l'endomorfismo T: V→V su campo K con dim V=n. T si dice diagonalizzabile se esiste una base ordinata B di V in cui la matrice associata M $_{B}$ (T) e diagonale. Una matrice quadrata su campo K, A ∈ Mn(K) si dice diagonalizzabile se e simile a una matrice diagonale. 

OSS Le matrici associate a un endomorfismo diagonizzabile sono diagonolizzabili se consideriamo $A = M_B(T)$ sappiamo che esiste una matrice P invertibile, $P \in \text{Gen}(K): A = P^{-1} \overline{A}P$ . Ponendo 

$Q = P^{-1}$ si ottiene che $Q^{-1}AQ = \tilde{A}$ dunque Q e la matrice che diagonali 320 A. 

Quindi T e diagonalizzabile (=> T ha una matrice associata diagonale(=> ogni sua matrice associata e diagonalizzabile. 

## TEOREMA SPETRALE

Consideriamo l'endomorfismo T: V→V con dimV=n. Siano λ₁, ..., λₙ gli autovalori di T, sono equivalenti i seguenti fatti: 

a) T e diagonalizzabile 

b) 3 una base di V costituità da autovettori. Tale base è detta spettrale 

$$
c) \sum_ {i = 1} ^ {n} m g (\lambda i) = n
$$

$$
d) U \lambda_ {1} \oplus \dots \oplus U \lambda n = V
$$

Dim a => b 

$$
\exists \vec {B} = (\vec {e} _ {1}, \dots , \vec {e} _ {n}): \vec {A} = M \vec {B} (T) = \left( \begin{array}{l l l l} a _ {1} & 0 & \dots & 0 \\ 0 & \ddots & & \\ 0 & & & a _ {n} \end{array} \right)
$$

$$
\phi_ {B} (T (\overline {{e}} _ {1})) = (\alpha_ {1}, \dots , 0) = T (\overline {{e}} _ {1}) = \alpha_ {1} \overline {{e}} _ {1}
$$

$$
\Phi_ {B} (T (\overline {{e _ {2}}})) = (0, \alpha_ {2}, 0, - 1, 0) = T (\overline {{e _ {2}}}) = \alpha_ {2} \overline {{e _ {2}}}
$$

$$
\phi_ {B} (T (\overline {{e n}})) = (0, \dots , 0, \alpha_ {n}) = T (\overline {{e n}}) = \alpha_ {n} \overline {{e n}} \quad d u n q u e \quad \overline {{e _ {1}}}, \dots , \overline {{e n}} \quad s o n o \quad a u t o v e t t o r i.
$$

Per ipotesi esiste una base spettrale $\vec{B} = (\vec{e}_1, \dots, \vec{e}_n)$ sappiamo quindi che: 

$$
T (\overline {{e _ {1}}}) = \lambda_ {i _ {1}} \overline {{e _ {1}}} \rightarrow \phi_ {B} (T (\overline {{e _ {1}}})) = (\lambda_ {i _ {1}}, 0, \dots , 0)
$$

$$
T (\overline {{e _ {2}}}) = \lambda_ {i _ {2}} \overline {{e _ {2}}} \rightarrow \phi_ {B} (T (\overline {{e _ {2}}})) = (0, \lambda_ {i _ {2}, \dots , 0})
$$

$$
T (e \overline {{n}}) = \lambda_ {i n} e \overline {{n}} \rightarrow \Phi_ {B} (T (e \overline {{n}})) = (0, \dots , \lambda_ {i n})
$$

Mettendo le componenti in colonna otteniamo la matrice $\overline{M}\overline{g}(\tau)$ dunque T e diagonalizzabile e la matrice diagonale associata ha 

tutti autovalori sulla diagonabile principale. 

## $b \Rightarrow  c$

Per ipotesì 3 una base spettrale $\overline{B} = (\overline{e}_1, \ldots, \overline{e_n})$ e dobbiamo dimostrare che $\sum_{i=1}^{n} mg(\lambda_i) = n$ . Supponiamo di ordinare la base spettrale in modo da avere vicini gli autovettori con lo stesso autovalore avendo praticamente $r_1$ autovettori con autovalore $\lambda_1$ ; $r_2$ autoveff. con autovalore $\lambda_2$ e cost via fino a in $\lambda_n$ . 

Naturalmente si ha che $r_{1} \leq mg(\lambda_{1}), r_{2} \leq mg(\lambda_{2}), \ldots, r_{n} \leq mg(\lambda_{n})$ si ha dunque che $n = r_{1} + r_{2} + \ldots + r_{n} \leq \sum_{i=1}^{h} mg(\lambda_{i})$ ; poiché $\sum_{i=1}^{h} mg(\lambda_{i}) = dim U_{\lambda_{1}} + U_{\lambda_{2}} + \ldots + U_{\lambda_{n}}$ e non puo essere superiore a n, il che vuol dire avere per forza $\sum_{i=1}^{n} mg(\lambda_{i}) = n$ 

Per ipotesi abbiamo $n=\sum_{i=1}^{n}\mathrm{mg}\left(\lambda_{i}\right)=\mathrm{dim}\left(U\lambda_{i}\oplus\ldots\oplus U\lambda_{n}\right)=\mathrm{dim}V$ 

Ma un sottospazio ha la stessa dimensione dello spazio ambiente se è uguale allo spazio ambiente quindi $U\lambda_1 \oplus \ldots \oplus U\lambda_h = V$ . 

Per ipotesi sappiamo che $U\lambda_{1} \oplus \ldots \oplus U\lambda_{h} = V$ . Prendendo una base $B_{1}$ in $U\lambda_{1}, B_{2}$ in $U\lambda_{2}, \ldots, B_{h}$ in $U\lambda_{n}$ si ha che l'unione di $B_{1} \cup B_{2} \cup B_{3} \ldots \cup B_{h}$ e base di $V$ . E poiche tutte le varie basi sono costituite da autovettori, la loro unione forma una base spettrale. 

oss: Ai 4 punti del teorema spettrale se ne aggiunge un altro caratterizzato da 2 condizioni
e) $\sum_{i=1}^{k} ma(\lambda_{i}) = n$ 

$$
\forall i \in \{1, \dots , h \} \text {   si   ha   ma(  \lambda   i) =   mg(  \lambda   i) }
$$

e si può notare che tale punto equivale al punto 3 

Teorema Spettrale : tipici esercizi 

$$
T: V \rightarrow V, \quad \text {   can   } \quad R, \quad d _ {m} V = 3, \quad B = (e _ {1}, e _ {2}, e _ {3})
$$

$$
A = M _ {B} (T) = \left( \begin{array}{l l l} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right), \quad A \text {   is   diagonolizzabile?   }
$$

$$
\left| A - \lambda I _ {2} \right| = \left| \left( \begin{array}{c c c} 1 - \lambda & 0 & 1 \\ 0 & 1 - \lambda & 1 \\ 0 & 0 & - \lambda \end{array} \right) \right| = (1 - \lambda) ^ {2} (- \lambda) ^ {\frac {1}{2}} = 0 <   > \lambda + 1 m a (t) = 2 \quad \forall \lambda + 0 m a (0) = t
$$

$$
U _ {0} A X = 0 \quad \left\{ \right.\begin{array}{l}x _ {1} + x _ {2} = 0\\x _ {2} + x _ {3} = 0\end{array}\Rightarrow \left\{\begin{array}{l}x _ {1} - x _ {3}\\x _ {2} - x _ {3}\end{array}\right. S = \left\{\left(- x _ {3}, - x _ {3}, x _ {3}\right) \mid x _ {3} \in \mathbb {R} \right\} = \mathcal {L} \left(- (- 1, - 1, 1)\right) = \Phi_ {B} (U _ {0}) \Rightarrow U _ {0} = \Phi_ {B} ^ {- 1} (S) = \mathcal {L} \left(- x _ {1} - x _ {3} + x _ {2}\right)
$$

$$
\text { Quindi: } \dim V _ {0} = 1. \quad N B. \text { In   neelta,   i   esattamente   il   risultato   deci   aspettavamo,in   quanto   vole   SEMPRE: } m a (\lambda) \geq m g (\lambda) \geq 1.
$$

$$
U _ {t}: \left( \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & - 1 \end{array} \right) \binom{x _ {1}}{x _ {2}} = 0 \quad \Rightarrow \{x _ {3} = 0 \quad S = \{(x _ {1}, x _ {2}, 0) | x _ {1}, x _ {2} \in I R \} = L ((1, 0, 0), (0, 1, 0)) = \Phi_ {0} (U _ {t}) \quad \Rightarrow U _ {t} = L (\texttt {e f f} _ {1}, x _ {2}).
$$

$$
\text { Come   ci   aspettiamo: } U _ {0} + U _ {1} = U _ {0} \oplus U _ {1} = \mathcal {L} (e _ {1}, e _ {2}, - e _ {1} - e _ {2} + e _ {3}) \quad B _ {0} \cup B _ {1} \text {   i   base   d   } U _ {0} \oplus U _ {1}
$$

$$
d _ {i m} (U _ {0} \oplus U _ {1}) = 3 \Rightarrow U _ {0} \oplus U _ {1} = V.
$$

$$
\text { Allora } \quad \overline {{B}} = (e _ {1}, e _ {2}, - e _ {1} - e _ {2} + e _ {3}) \quad \text { i   una   base   speltrole } \quad e \quad \text { o }
$$

$$
\begin{array}{l} Q = M _ {B B} (d _ {V}) = \left( \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 0 & 1 \end{array} \right) \quad \text {   e   la   mative   de   diagonolizza   } \\ \widetilde {B} = (- s _ {1}, e _ {2} + s _ {2}, e _ {1}, e _ {2}) \quad , \quad \widetilde {Q} = M _ {B B} (d _ {V}) = \left( \begin{array}{c c c} - 1 & 0 & 1 \\ 1 & 0 & 0 \end{array} \right) \quad \overline {{\overline {{Q}}}} = A \overline {{\overline {{Q}}}} = \left( \begin{array}{c c c} 9 & 9 & 9 \\ 9 & 9 & 9 \end{array} \right) = A, \quad T _ {\text {   d   diagonolizza   }} = \text {   bile   }. \end{array}
$$

T: V→V $d_{im}$ V→3 R B = (e₁, e₂, e₃) A = (φ φ φ) 

$$
\left| A - \lambda I _ {3} \right| = \left| \begin{array}{l l l} 1 - \lambda & 0 & 0 \\ 0 & - \lambda & 1 \\ 1 & 0 & - \lambda \end{array} \right| = \lambda^ {2} (1 - \lambda) = 0 <   > \lambda = 0 v \lambda = 1 m _ {n} (0) = 2 > d u (1 + 1)
$$

$$
U _ {0}: A X = 0 \quad \left\{ \begin{array}{l} x _ {1} = 0 \\ x _ {2} = 0 \end{array} \right.
$$

$$
S = \{(0, x _ {2}, 0) | x _ {2} \in \mathbb {R} ^ {3} \} = \mathcal {L} (0, 1, 0) = \Phi_ {B} (U _ {0}) \Rightarrow U _ {0} = \Phi_ {B} ^ {\prime} (S) = \mathcal {L} (x _ {2}) \Rightarrow d i n U _ {0} > 1 <   x _ {2}, e l l r e T _ {n m d i g o n a l i z u b l e}.
$$

$$
\text { In } f o l t i, \text { and } s e n z a c a l c o l o n e U _ {1}, \text { so } d e \dim U _ {0} \oplus \dim U _ {1} = 2 \times 3 = \dim V \Rightarrow U _ {0} \oplus U _ {1} \subsetneq V.
$$

$$
T: \mathbb {R} [ x ] \leq 2 \rightarrow \mathbb {R} [ x ] \leq 2 B = (1, x, x ^ {2}) A - M _ {\theta} (T) = \left(\begin{array}{l l l}1&0&1\\2&1&1\end{array}\right)
$$

$$
\left| A - \lambda I _ {3} \right| = \left| \left( \begin{array}{c c c} t, & \lambda & - 1 \\ \tau & t, & \lambda \\ \tau & - 1 & + \lambda \end{array} \right) \right| = (t - \lambda) (- 1) ^ {2} \left| \left( \begin{array}{c c c} t, & \lambda & - 1 \\ - 1 & + \lambda \end{array} \right) \right| + (- 1) (- 1) ^ {2} \left| \left( \begin{array}{c c c} 0 & + \lambda \\ z & - 1 \end{array} \right) \right| = (t - \lambda) [ (t - \lambda) (- t, \lambda) - t ] + _ {2} (t - \lambda) = (t - \lambda) [ \lambda^ {2} - t - t + 2 ] = (t - \lambda) \lambda^ {2}.
$$

$$
U _ {0} = K _ {\alpha} T: A X = 0 \left\{ \begin{array}{l} x _ {1}, x _ {2}, x _ {3} \\ x _ {4}, x _ {5}, x _ {6} \end{array} \right. \Rightarrow \left\{ \begin{array}{l} x _ {1}, x _ {2}, x _ {3} \\ x _ {4}, x _ {5}, x _ {6} \\ 0 = 0 \end{array} \right. S = \{(x _ {3}, x _ {2}, x _ {3}) | x _ {3} \in \mathbb {R} \} = \mathcal {L} ((1, 1, 1)) = \Phi_ {\theta} (U _ {0}) \Rightarrow U _ {0} = \Phi_ {\mathrm{B}} ^ {- 1} (s) = \mathcal {L} (1 + x + x ^ {*}).
$$

$$
U _ {1}: \left( \begin{array}{l l l} 0 & 0 & - 1 \\ 0 & 0 & - 1 \\ 2 & - 1 & - 2 \end{array} \right) x = 0 \quad \Rightarrow \left\{ \begin{array}{l} x _ {3} = 0 \\ x _ {4} - x _ {5} = 0 \end{array} \right. \Rightarrow \left\{ \begin{array}{l} x _ {1} = 0 \\ x _ {2} = 2 x _ {1} \end{array} \right. S \cdot \{(x _ {1}, 2 x _ {1}, 0) | x _ {1} \in \mathbb {R} \} = \mathcal {L} ((1, 2, 0)) = \Phi_ {B} (u _ {1}) \Rightarrow U _ {1} = \Phi_ {B} ^ {\prime} (S) = \mathcal {L} (1 + 2 x).
$$

$$
\dim U _ {0} \oplus U _ {1} = 2 + 3 = \dim R [ x ] \leq 2 \Rightarrow \text { Non   esiste   una   base   speltrole }
$$

## RUFFINI

Considerando uno scalare c ∈ K e un polinomio P(x) ∈ K[x]. c e radice di P(x) <=> 

$$
\exists q (x) \in K [ x ]; p (x) = q (x) (x - c)
$$

## Esempio :

$$
T: \mathbb {R} ^ {3} \rightarrow \mathbb {R} ^ {3} B = ((1, 0, 0), (0, 1, 0), (0, 0, 1)) A = M _ {B} (T) = \left(\begin{array}{l l l}4&2&2\\2&4&2\\2&2&4\end{array}\right)
$$

$$
\left| A - \lambda I _ {3} \right| = \left( \begin{array}{l l l} 4 - \lambda & & \\ \frac {1}{2} & 4 - \lambda & \frac {1}{2} \\ 2 & 2 & 0 - \lambda \end{array} \right) = (4 - \lambda) ^ {3} + 8 + 8 - 4 (4 - \lambda) - 4 (4 - \lambda) - 4 (4 - \lambda) = - \lambda^ {3} + 1 2 \lambda^ {2} - 3 6 \lambda + 3 2 = 0 <   = >?
$$

$$
\text { Applico   Ruggini:   e   noto   che   se } \lambda = 2, \text { allone } - 2 ^ {3} + 1 2. 2 ^ {2} - 3 6. 2 + 1 2 = 0, \text { ciel } 2 \text { è   radice   del   mio   polinomio. }
$$

$$
\frac {\left| \begin{array}{r r r} - 1 & 1 2 & - 3 6 \\ 2 & - 2 & 3 0 \\ - 1 & 1 0 & - 1 6 \end{array} \right| - 3 2}{- 1} \Rightarrow - \lambda^ {3} + (2) ^ {2} - 3 6 \lambda + 3 2 = (- \lambda^ {2} + (0) \lambda - 1 6) (\lambda - 2) = (\lambda - 8) (\lambda - 2) ^ {2} = 0 <   = \lambda = 8 v \lambda = 2.
$$

$$
U _ {2}: \left( \begin{array}{l l l} 2 & 2 & 2 \\ 2 & 2 & 2 \\ 2 & 2 & 2 \end{array} \right) x = 0 \quad \Rightarrow \quad \left\{x _ {1} + x _ {2} + x _ {3} = 0 \quad \Rightarrow \quad \left\{x _ {3} = - x _ {1} - x _ {2} \right. \right.
$$

$$
S = \{(x _ {1}, x _ {2}, - x _ {1} - x _ {2}) | x _ {1}, x _ {2} \in \mathbb {R} \} = \mathcal {L} ((1, 0, - 1), (0, 1, - 1)) = \Phi_ {B} (U _ {2}) \Rightarrow U _ {2} = \Phi_ {B} ^ {- 1} (S) = \mathcal {L} ((1, 0, - 1), (0, 1, - 1)).
$$

$$
S _ {\mathrm{appiamo~giè}} \mathrm{che} \dim U _ {2} + \dim U _ {8} = \dim U _ {2} Ⓑ \dim U _ {8} = 3 = \dim R ^ {3}, \mathrm{quindr} T \mathrm{diagonolizzabile,me~per~scuppolo~calcoliamo} U _ {8}.
$$

$$
\bigcup_ {8}: \left( \begin{array}{c c c} - 4 & 2 & 1 \\ 3 & - 4 & 2 \\ 1 & 1 & - 4 \end{array} \right) \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {\prime} \leftarrow - x ^ {2} \binom{- 4 + 2}{- 4 + 2} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2} \leftarrow x ^ {2} + e ^ {2} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {3} \leftarrow x ^ {2} + e ^ {3} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {4} \leftarrow x ^ {2} + e ^ {4} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {5} \leftarrow x ^ {2} + e ^ {5} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {6} \leftarrow x ^ {2} + e ^ {6} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {7} \leftarrow x ^ {2} + e ^ {7} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {8} \leftarrow x ^ {2} + e ^ {8} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {9} \leftarrow x ^ {2} + e ^ {9} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 0} \leftarrow x ^ {2} + e ^ {1 0} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 1} \leftarrow x ^ {2} + e ^ {1 1} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 2} \leftarrow x ^ {2} + e ^ {1 2} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 3} \leftarrow x ^ {2} + e ^ {1 3} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 4} \leftarrow x ^ {2} + e ^ {1 4} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 5} \leftarrow x ^ {2} + e ^ {1 5} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 6} \leftarrow x ^ {2} + e ^ {1 6} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 7} \leftarrow x ^ {2} + e ^ {1 7} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 8} \leftarrow x ^ {2} + e ^ {1 8} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {1 9} \leftarrow x ^ {2} + e ^ {1 9} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 0} \leftarrow x ^ {2} + e ^ {2 0} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 1} \leftarrow x ^ {2} + e ^ {2 1} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 2} \leftarrow x ^ {2} + e ^ {2 2} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 3} \leftarrow x ^ {2} + e ^ {2 3} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 4} \leftarrow x ^ {2} + e ^ {2 4} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 5} \leftarrow x ^ {2} + e ^ {2 5} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 6} \leftarrow x ^ {2} + e ^ {2 6} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 7} \leftarrow x ^ {2} + e ^ {2 7} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 8} \leftarrow x ^ {2} + e ^ {2 8} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {2 9} \leftarrow x ^ {2} + e ^ {2 9} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {3 0} \leftarrow x ^ {2} + e ^ {3 0} \binom{x _ {1}}{x _ {2}} = 0 \quad e ^ {- x _ {1}} + x _ \texttt \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf (\textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\:}}} X}}} + X}}} - X Y Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z Y Z YZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZYZ< fcel>U, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H-I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\O,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\o,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\o,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\o,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\o,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\o,P,Q,R,S,X,A,B,C,D,E,F,G,H,I,K,L,M,N,\to O ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,M ,X ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,M ,N ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X ,X< nl>
$$

$$
\Rightarrow S = \{(x _ {3}, x _ {3}, x _ {3}) | x _ {3} \in \mathbb {R} \} = \mathcal {L} ((1, 1, 1)) = \Phi_ {\theta} (U _ {\theta}) = U _ {\theta} \quad \text {   penelis   } \Phi_ {\theta} \text {   bielliva.   }
$$

$$
Q = \left( \begin{array}{l l l} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & - 1 & - 1 \end{array} \right) \quad Q ^ {- 1} A Q = \left( \begin{array}{l l l} 8 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{array} \right), \text { provare per medere! }
$$

## LEZIONE 18

## SPAZI VETTORIALI EUCLIDEI

Sig V uno spazio vettoriale sul campo K=R Un prodotto scalare su V e un applicazione <,>,> :V×V→R 

$$
i) \text { simmetria: } \forall u, v \in V \quad <   u, v > = <   v, u > \Rightarrow \begin{array}{l} \text { prodotto   scalare   tra } \\ \text { uvevale   al } \\ \text { u.ev } \end{array}
$$

$$
\forall u, v, w \in V <   u, v + w > = <   u, v > + <   u, w > \left\{ \begin{array}{l} \text {   formano   } \\ 1 0 \end{array} \right.
$$

iii) linearità del 2º argomento rispetto una moltiplicazione: ∀u,v∈V, ∀α∈R: <u,αv> = α <u,v> bilinearità 

$$
\text {   iv)   definito   positivo:   } \forall u \in V \quad \angle u, v > 0 \quad \text {   oppure   } = 0 \Leftrightarrow u = \underline {{0}}
$$

OSS $\forall u \in V$ il prodotto scalare tra u e 0 e 0. 

se il vettore $v \in V$ e tale che: $\forall u \in V < u, v > = 0$ aroma $v = 0$ . Possiamo definire la coppia ( $V, <, >$ ) spazio vettoriale euclidean. 

DEF Siq (V, <,>) uno spazio vettoriale euclidean. ∀y ∈ V definiamo ||u|| = √<u,u> 

$$
\cdot \mathbb {R} ^ {2} u = (3, - 5) \| u \| = \sqrt {9 + 2 5} = \sqrt {3 4}
$$

$$
\cdot \mathbb {R} ^ {2} \quad u = (3, - 5) \quad \| u \| = \sqrt {(3 , - 5) , (3 , - 5)} = \sqrt {9 + 1 6} = 5
$$

valore assoluto di a
per lunghezza di u. 

OSS: $\forall u\in V,\ \forall \alpha \in R$ ||αu|| = |α||u|| 

$$
\text {   Basta   considerare   } \| \alpha u \| = \sqrt {\langle \alpha u , \alpha u \rangle} \quad \text {   che   per   linearita   e   simmeTria   } \dot {e} = \sqrt {\alpha^ {2} \langle u , u \rangle} = | \alpha | \| u \|
$$

Consideriamo lo spazio vettoriale euclidean (V, <., >). ∀u,v ∈ V si ha che |<u,v>| ≤ ||u||·||v|| 

DiM Naturalmente se u=0 appure v=0 il risultato e banale dunque assumiamo u,v≠0. Prendiamo un parametro reale B e consideriamo <u+βv, u+βv> che sappiamo essere ≥0 per l'ultima proprietà del prodotto scalare. 

$$
= \| u \| ^ {2} + \beta <   v, u > + \beta <   u, v > + \beta^ {2} <   v, v > = \| u \| ^ {2} + 2 \beta <   w, v > + \beta^ {2} \| v \| ^ {2}
$$

questi sono uguali dunque si possono sommare e' ||v|| $^{2}$ 

atteniamo dunque $\|u\|^{2} + 2\beta < u, v > + \beta^{2}\|v\|^{2}$ che e'un polinomio in B di grado 2 dunque possiamo con-

$$
\frac {\Delta}{4} = \angle u, v > ^ {2} - \| u \| ^ {2} \| v \| ^ {2} \leq 0 \quad \text {   abbiamo   quindi   } \angle u + \beta v, u + \beta v > \geq 0 \Leftrightarrow \angle u, v > ^ {2} - \| u \| ^ {2} \| v \| ^ {2} \leq 0
$$

<table><tr><td>PROP Consideriamo 2 vettori <eq>u, v \in V \setminus \{e\}</eq>. Sappiamo che <eq>|\langle u, v \rangle| \leq ||u||||v||</eq> daua quale otteniamo <eq>\frac{&lt;u, v&gt;|}{||u|| ||v||} \leq 1 \Rightarrow -1 \leq \frac{\langle u, v \rangle}{||u|| ||v||} \leq 1</eq>Da qui possiamo dire che <eq>\exists !F \in [0, r]</eq>: cosf = <eq>\frac{\langle u, v \rangle}{||u|| ||v||}</eq> ed F è detto angolo tra u e vDEFSia (V, &lt;-, &gt;) uno spazio vettoriale euclideo. <eq>\forall u, v \in V</eq> i vettori <eq>u, v</eq> si dicano ortogonali <eq>\Leftrightarrow \langle u, v \rangle = 0</eq>TEOREMA Di PITAGORA<eq>\forall u, v \in V</eq> <eq>\|u+v\|^2 = \|u\|^2 + \|v\|^2 \Leftrightarrow \langle u, v \rangle = 0</eq> <eq>\text{Ve v sono ortogonali}</eq>infatti noi sappiamo che <eq>\|u+v\|^2 = \|u\|^2 + 2 \langle u, v \rangle + \|v\|^2</eq> e Solamente con <eq>\langle u, v \rangle = 0</eq> possiamo trovare che <eq>\|u+v\|^2 = \|u\|^2 + \|v\|^2</eq>BASI ORTONORMALIPROP Siano <eq>u_1, u_2, \ldots, u_t</eq> t vettori non nulli di V a due a due ortogonali: allora l&#x27;insieme di vettori <eq>\{u_1, u_2, \ldots, u_t\}</eq> e LIN. DiP.Dirt Consideriamo t scalari <eq>\alpha_1, \alpha_2, \ldots, \alpha_t \in \mathbb{R}</eq>: <eq>\alpha_1 u_1 + \alpha_2 u_2 + \ldots + \alpha_t u_t = 0</eq>. Partiamo con il considerare <eq>\langle u_1, 0 \rangle = 0</eq> ma noi sappiamo quanto &quot;vale&quot; 0, dunque riscrivo <eq>\langle u_1, 0 \rangle</eq> come<eq>\times</eq> la linearità addizione<eq>\times</eq> la linearità del prodottopoiche` i vettori sono a2 a 2 ortogonali allora tutto questo si annulia<eq>\langle u_1, \alpha_1 u_1 + \alpha_2 u_2 + \ldots + \alpha_t u_t \rangle = \langle u_1, \alpha_1 u_1 \rangle + \langle \ldots \rangle + \langle u_1, \alpha_t u_t \rangle = \alpha_1 \langle u_1, u_1 \rangle + \alpha_2 \langle u_1, u_2 \rangle + \alpha_t \langle u_1, u_t \rangle = \alpha_1 \langle u_1, u_t \rangle</eq>dunque ci resta <eq>\alpha_1 \langle u_1, u_1 \rangle = 0</eq> e poiche <eq>\langle u_1, u_1 \rangle \neq 0</eq> allora di deve essere per forza o facendo la stessa cosa con <eq>\langle u_2, 0 \rangle</eq> traveremo <eq>\alpha_2 = 0</eq> e così via per tutti gli altri vet.DEF Sia (V, &lt;-, &gt;) uno spazio euclideo e sia B = (u1, ..., un) una base di V con dimV = n.B si dice ortogonale se i suoi vettori sono a 2 a 2 ortogonaliB si dice ortonormale se è ortogonale e tutti i suoi vettori hanno lunghezza 1.ESEMPIO<eq>\mathbb{R}^2 \ll &gt;</eq> prodotto scalare numericoB = (c1,1), (-1,1)) (1,1) · (-1,1) = -1+1=0← base ortogonale<eq>\| (1,1)\| = \sqrt{2} = \| (-1,1)\|</eq> B&#x27; = ((<eq>\frac{1}{\sqrt{2}}</eq>, <eq>\frac{1}{\sqrt{2}}</eq>), (-<eq>\frac{1}{\sqrt{2}}</eq>, -<eq>\frac{1}{\sqrt{2}}</eq>))← base ortonormale → <eq>\vec{B} = ((1,0), (0,1))</eq></td></tr></table>

Prop Sia (V, <.,>) uno spazio vettoriale euclidean e sia B = (e1,...,en) una base 

di V ortonormale con dimV=n allora: 

$$
\text { iesima   componente }
$$

$$
1) \forall u \in V \text {   sia   } (x _ {1}, \ldots , x _ {n}) = \Phi_ {B} (u) \text {   aulla   } \forall i \in \{1, \ldots , n \} \quad x _ {i} = <   u, e _ {i} >
$$

$$
2) \forall u, v \in V \text { siano } (x _ {1}, \dots , x _ {n}) = \Phi_ {B} (u) e (y _ {1}, \dots , y _ {n}) = \Phi_ {B} (v) a l l o r a <   u, v > = x _ {1} y _ {1} + \dots + x _ {n} y _ {n}
$$

vettore delle 

1. Per ipotesi possiamo scrivere u tramite le sue componenti cice' $u = x_{1}e_{1} + x_{2}e_{2} + \ldots + x_{n}e_{n}$ e andiamo 

$$
\text {   a   calcolare   } \langle u, e _ {1} \rangle \text {   che   } \bar {e} = \langle x _ {1} e _ {1} + \ldots + x _ {n} e _ {n}, e _ {1} \rangle = \langle x _ {1} e _ {1}, e _ {1} \rangle + \langle x _ {2} e _ {2}, e _ {1} \rangle + \ldots + \langle x _ {n} e _ {n}, e _ {1} \rangle =
$$

$$
\underbrace {x _ {1} \left<   e _ {1} , e _ {1} \right > } _ {\frac {1}{2}} + \underbrace {x _ {2} \left<   e _ {2} , e _ {1} \right> + \ldots + x _ {n} (e _ {n} , e _ {1})} _ {\text { essendo   la   base   ortonormale }} = x _ {1}
$$

2. Consideriamo il caso n=2. Possiamo scrivere u,v con le loro componenti e in questo caso 

$$
\text {   abbiamo   } u = x _ {1} e _ {1} + x _ {2} e _ {2} \text {   e   } y = y _ {1} e _ {1} + y _ {2} e _ {2} \text {   dunque   }
$$

$$
\angle u, v > = \angle x _ {1} e _ {1} + x _ {2} e _ {2}, y _ {1} e _ {1} + y _ {2} e _ {2} > = \angle x _ {1} e _ {1} + x _ {2} e _ {2}, y _ {1} e _ {1} > + \angle x _ {1} e _ {1} + x _ {2} e _ {2}, y _ {2} e _ {2} > =
$$

$$
\langle x _ {1} e _ {1}, y _ {1} e _ {1} \rangle + \langle x _ {2} e _ {2}, y _ {1} e _ {1} \rangle + \langle x _ {1} e _ {1}, y _ {2} e _ {2} \rangle + \langle x _ {2} e _ {2}, y _ {2} e _ {2} \rangle = x _ {1} y _ {1} \langle e _ {1}, e _ {1} \rangle + x _ {2} y _ {1} \langle e _ {2}, e _ {1} \rangle + x _ {1} y _ {2} \langle e _ {1}, e _ {2} \rangle + x _ {2} y _ {2} \langle e _ {2}, e _ {2} \rangle =
$$

$$
= x _ {1} y _ {1} + x _ {2} y _ {2}
$$

$$
E S E M P i o (d a q u e l l o p r e c e d e n t e)
$$

$$
B ^ {\prime} = \left(\left(\frac {1}{\sqrt {2}}, \frac {1}{\sqrt {2}}\right), \left(- \frac {1}{\sqrt {2}}, \frac {1}{\sqrt {2}}\right)\right)
$$

$$
\text {   siano   } u \equiv_ {8 1} (3, - 5) \quad \text {   cioe   } u = 3 (\frac {1}{\sqrt {2}}, \frac {1}{\sqrt {2}}) - 5 (\frac {- 1}{\sqrt {2}}, \frac {1}{\sqrt {2}}) e
$$

$$
V \equiv_ {B ^ {1}} (1, 2) \quad a i c e ^ {-} V = (\frac {1}{\sqrt {2}}, \frac {1}{\sqrt {2}}) + 2 (- \frac {1}{\sqrt {2}}, \frac {1}{\sqrt {2}})
$$

$$
\text { Allora } <   u, v > = 3 - 1 0 = - 7
$$

## GRAM-SCHMIDT

$$
(V, <   \dots >) \dim V = n \quad B = (u _ {1}, \dots , u _ {n}) \text {   base   di   } V
$$

Il metodo di Gram-Schmidt e un'algoritmo che trasforma B in una base ortogonale. 

Vediamo il caso n=2 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-06/89f1c5bc-505e-44c7-83f0-c8d891089f89/abfcb45420b8f23c0e2f9f9aa6bd7b0108ee53620cb14d987266a63bd94d73ff.jpg)


$$
V + (- \alpha u) \mathrm{e} ^ {-} \mathrm{artogonaleau.}
$$

$$
\text { Impongo } <   v - \alpha u, u > = 0
$$

du proiezione ortogonale di v su u 

$$
0 = <   v - \alpha u, u > = <   v, u > - \alpha <   u, u > \Rightarrow <   v, u > = \alpha <   u, u > \Rightarrow \alpha = \underline {{<   v , u >}}
$$

Allora il vettore che sto cercando è: $v - \alpha u = v - \frac{\langle v, u \rangle}{\|u\|^{2}} u$ . 

$$
<   \cdot >: ((a _ {1}, a _ {2}), (b _ {1}, b _ {2})) \in \mathbb {R} ^ {2} \times \mathbb {R} ^ {2} \mapsto 2 a _ {1} b _ {1} + a _ {1} b _ {2} + a _ {2} b _ {1} + a _ {2} b _ {2} \in \mathbb {R}
$$

$$
B = ((1, 0), (0, 1)) <   (1, 0), (0, 1) > = 2 \cdot 0 + 1 + 0 + 0 = 1 \neq 0
$$

$$
V ^ {\prime} = V - \frac {<   v , u >}{\| u \| ^ {2}} u = (0, 1) - \frac {1}{2} (1, 0) = (- \frac {1}{2}, 1) \quad \text { Allora }, B ^ {\prime} = ((1, 0), (- \frac {1}{2}, 1)) e ^ {- b a s e o r t o g o n a l e}
$$

$$
\| u \| ^ {2} = \langle u, u \rangle = 2 + 0 + 0 + 0 = 2 \quad \| v \| = \sqrt {\frac {1}{2} - \frac {1}{2} \sqrt {\frac {1}{2}}} = \sqrt {\frac {1}{2}} \quad \text { Quindi } \quad B ^ {\prime \prime} = (\frac {1}{\sqrt {2}} (1, 0), \sqrt {2} (- \frac {1}{2}, 1)) \quad e ^ {-} \text { ortonormale }
$$

L'algoritmo è il seguente: $B=(u_{1},\ldots,u_{n})$ base di $(V_{1},<\ldots,>)$ 

$$
\cdot V _ {2} = u _ {2} - \frac {\langle u _ {2} , v _ {1} \rangle}{\| v _ {1} \| ^ {2}} v _ {1}
$$

$$
v _ {3} = u _ {3} - \frac {\langle u _ {3} , v _ {1} \rangle}{\| v _ {1} \| ^ {2}} v _ {1} - \frac {\langle u _ {3} , v _ {2} \rangle}{\| v _ {2} \| ^ {2}} v _ {2}
$$

$$
\cdot v _ {n} = u _ {n} \sum_ {i = 1} ^ {n - 1} \frac {\angle u _ {n} , v _ {i} >}{\| v _ {i} \| ^ {2}} v _ {i}
$$

$$
B ^ {\prime} = (v _ {1}, \dots , v _ {n}) \text {   ortogonale   }
$$

$$
B ^ {\prime \prime} = (\frac {1}{\| v _ {1} \|}, v _ {1}, \dots , \frac {1}{\| v _ {n} \|}, v _ {n}) ^ {0} \text {   or   tonormale.   }
$$

## LEZIONE 19

## PRODOTTO VETTORIALE

DEF Sia (V, <. . .>) uno spazio vettoriale euclideo con dimensione finita n e supponiamo 

Be B basi ortonormali del nostro spazio euclideo si può dimostrare che la matrice 

di passaggio da Ba B gode delle seguenti proprietà: 

$A = M_{B}\overline{B}$ allora $A^{-1} = ^t A$ e tale proprieta: si esprime dicando che $A$ è ortogonale 

inoltre tali matrici ortogonali hanno determinante uguale a ±1 ma NON vale il vicuera 

DEF $(V,<\cdots>)$ dimV=3 B base div 

(V,B) spazio eucaideo orientato 

B' base di V sidie concorde con B se |MBB'(idV)| > 0 

Siano poi 

Il prodotto vettoriale uxv uquale a 0 se fu,v4e LiN.DiP,altimenti 

e' l'unico rettore tale che: (u,v,u×v) e concordo con B. 

$|u \times v| = ||u|| ||v|| \sin \hat{u}v$ $u \times v \in \text{orthogonale a u e a v}$ $\sin \hat{u}v = \sqrt{1 - \cos^2 \hat{u}v}$ 

PROP u,vεV,spazio euclidoo di dimensione 3. 

$$
\begin{array}{l} \{u, v \} \text {   LiN.   IND.,   } \overline {{B}} \text {   ortonormone   e   } u \equiv_ {B} (x _ {1}, x _ {2}, x _ {3}), v \equiv_ {B} (y _ {1}, y _ {2}, y _ {3}) \\ \text { Allora   } u \times v \equiv_ {\overline {{B}}} \left(| x _ {2} x _ {3} |, - | x _ {1} x _ {3} |, | x _ {1} x _ {2} |, y _ {1} y _ {2} |\right). \end{array}
$$

Il prodotto vettoriale e' anti-commutativo: u × v = -v × u 

DEF Sia W un sottospazio vettoriale di E e sia dimE=n si definisce 

complemento ortogonale di ω in ε: 

$^{+}W = \{ u \in \vec{\varepsilon} : <u,v> = 0, \forall v \in W \}$ si può dimostrare che è un sottospazio vettoriale detto com-

plemento ortogonale di w. 

## ESEMPio:

Sia U la chiusura lineare di 2 vettori Lin. ind. 

Allora sono ortogonali ad U tutti i vettori 

proporzionali a ω, cioe: $^{+}U_{π}=L(\omega)$ 

Prop $(V, \angle\therefore)$ dim $V=n$ $U=L(u_{1}, \ldots, u_{t}) \subseteq V$ 

$$
ⓛ U = \{v \in V: <   v, u > = 0, \forall u \in \{u _ {1}, \dots , u _ {t} \} \};
$$

$$
② ^ {\perp} U e ^ {-} \text {   un   sottospazio   vettoriale;   }
$$

$$
③ a) U, \omega \leq V \text { sottos.   vett }: U \subseteq \omega \Rightarrow^ {\perp} U \stackrel {\perp} {=} \omega
$$

$$
④ U + ^ {\perp} U = U \oplus^ {\perp} U = V \quad \text {   quindi   } \dim^ {\perp} U = n - \dim U.
$$

## Dim

$$
1) \text {   "c"   banale   }
$$

$$
\text { “ } \geqslant \text { ” } w \in \{v \in V: <   v, u > = 0, \forall u \in \{u _ {1}, \dots , u + 1 \} \quad T h: <   w, u > = 0 \forall u \in U
$$

$$
u \in U \Rightarrow \exists \alpha_ {1}, \dots , \alpha_ {t} \in R: u = \alpha_ {1} u _ {1} + \dots + \alpha_ {t} u _ {T} \Rightarrow <   w, u > = <   w, \alpha_ {1} u _ {1} + \dots + \alpha_ {t} u _ {t} > = \alpha_ {1} <   w, u _ {1} > + \dots + \alpha_ {t} <   w, u _ {t} > = 0
$$

2) $w, w' \in^{-1} U$ . Proviamo che e^ stabile rispetto + e : 

$$
<   \omega + \omega^ {\prime}, u _ {i} > = <   \omega , u _ {i} > + <   \omega^ {\prime}, u _ {i} > = 0 + 0. \quad i \in \{1, \dots , t \}
$$

$$
\lambda \in \mathbb {R} <   \lambda w, u _ {i} > = \lambda <   w, u _ {i} > = \lambda \cdot 0 = 0 \checkmark
$$

$$
3) a. w ^ {\prime} \in^ {1} W \Rightarrow \forall w \in W <   w ^ {\prime}, w > = 0 \Rightarrow \forall u \in U, <   w ^ {\prime}, u > = 0 c i o e U \subseteq W \Rightarrow \forall w ^ {\prime} \in^ {1} W, w ^ {\prime} \in^ {1} U
$$

$$
\text { quindi } ^ {\perp} W \leq^ {\perp} U.
$$

b. Sappiamo che, per definizione $\forall u \in U \Rightarrow \forall w \in^{\perp} U < u, w > = 0, \forall u \in^{\perp} (^{\perp} U) \Rightarrow$ 

$\Rightarrow \forall w \in ^{+} U < u, w > = 0. \text{ Inoltre da 2) sappiamo che } + (+U) \text{ e' sottasp. vett. di V, men-}$ 

tre U lo e per ipotesi. Ma allora +(-U)=U NECESSARIAMENTE 

4) Th: $U \cap U = \{0\}$ basta osservare che $\forall u \in V, <u, u> = 0 \Rightarrow u = 0$ 

Sia Bu una base ortonormale di U. Completiamo Bu ad una base B di V. 

$$
B U = \{v _ {1}, \dots , v _ {t} \} \quad B = \{v _ {1}, \dots , v _ {t}, v _ {t + 1}, \dots , v _ {n} \}
$$

Rendiamo B una base ortogonale mediante il metodo di Gram-Schmidt: 

$$
\begin{array}{r l} {\vec {B}} & {= \left\{v _ {1}, \dots , v t, w _ {t + 1}, \dots , w _ {n} \right\} ^ {\perp} \quad w _ {t + 1}, \dots , w _ {n} \in^ {\perp} U \wedge \left\{w _ {t + 1}, \dots , w _ {n} \right\} e ^ {- L i N. I N D}.} \\ & {\Rightarrow L (w _ {t + 1}, \dots , w _ {n}) = ^ {\perp} U} \end{array}
$$

## SPAZIO AFFINE EUCLIDEO

Uno spazio euclideo e' uno spazio affine in cui lo spazio vettoriale e'uno spazio vettoriale euclideo ed e' indicato con ( $\vec{\varepsilon}$ , $\varepsilon$ , $\pi$ ) con $\pi: \varepsilon \times \varepsilon \rightarrow \vec{\varepsilon}$ 

Un riferimento cartesiano in uno spazio euclidean e pensato essere dotato di una base ortonormale $R = (0, B)$ 

PROP Uno spazio affine euclidean ( $\varepsilon$ , $\varepsilon$ , $\pi$ ) gode delle seguenti proprietà: 

$$
\cdot P \overrightarrow {Q} = \underline {{O}} \Longleftrightarrow P = Q
$$

$$
\cdot - \overrightarrow {P Q} = \overrightarrow {Q P}
$$

Dim 

$\overrightarrow{PQ} = \overrightarrow{PP} \cdot \overrightarrow{QP}$ per hp. 

$$
\overrightarrow {P Q} + \overrightarrow {Q P} = \overrightarrow {P P} \Rightarrow \overrightarrow {P P} + \overrightarrow {P P} = \overrightarrow {P P} \Rightarrow \overrightarrow {P P} = 0
$$

⇒ Per hp $\overrightarrow{PQ} = \underline{0}$ e per quanto appena dimostrato $\overrightarrow{PP} = \underline{0}$ . 

$$
\text { Dalla   proprietà } ① \text { ottengo   che } Q = X = P \Rightarrow P = Q.
$$

$$
\cdot \mathrm{Th}: - \overrightarrow {P Q} = \overrightarrow {Q P}
$$

$$
\underline {{O}} = \overrightarrow {P P} \stackrel {(2)} {=} \overrightarrow {P Q} + \overrightarrow {Q P} \Rightarrow \underline {{O}} = \overrightarrow {P Q} + \overrightarrow {Q P} \Rightarrow - \overrightarrow {P Q} = \overrightarrow {Q P}
$$

$$
\vec {E} ^ {\rightarrow} \text { sottos.   vett. }
$$

$$
\varepsilon = \vec {\varepsilon}
$$

$$
\Pi_ {\vec {\varepsilon}}: (V, \omega) \in \vec {\varepsilon} \times \vec {\varepsilon} \rightarrow \omega - V \in \vec {\varepsilon} 4 - e ^ {- c i o ^ {-}} \text { che   auviene   tipicamente } \text { quando   di   segnano   su } R ^ {2}
$$

$(\vec{\varepsilon}, \vec{\varepsilon}, \pi_{\vec{\varepsilon}})$ spazio affine euclidean. 

## Riferimento CARTESIANO

Sia dim A = dimV = n ∈ N ∪ 104 allora possiamo prendere: una coppia (0, B) dove O e un punto 

di A e B=(u $_{1}$ , ..., u $_{n}$ ) base ordinata di V. La coppia e' detta riferimento cartesiano. 

Considerando lo spazio affine (V, A, π) e fissiamo un riferimento cartesiano R = (O, B), 

definiamo ∀P∈A le coordinate di P in R. Sono le componenti del vettore $\overrightarrow{OP}$ in B 

$$
4 P \equiv_ {R} \Phi_ {B} (\overrightarrow {O P})
$$

PROP Consideriamo lo spazio affine A dim=n e fissiamo un riferimento cartesiano 

$$
R = (0, B) \text {   si   ha   che   } \forall P, Q \in A \text {   e   poniamo   } P \equiv_ {R} (x _ {1}, \ldots , x _ {n}) \text {   e   } Q \equiv_ {R} (y _ {1}, \ldots , y _ {n}).
$$

$$
\text { Allora   le   componenti   del   vettore } \overrightarrow {P Q}, \text { dunque } \Phi_ {B} (\overrightarrow {P Q}) = (y _ {1}, \dots , y _ {n}) - (x _ {1}, \dots , x _ {n})
$$

## LEZIONE 20

Sottospazio AFFINE EUCLIDEO 

Considero lo spazio affine (v,A,r) la dimension n. Considero un sottoinsieme x:A esso si dia sottospazio affine di A se: 

considero $P(x)(x)=\left\{\vec{PQ}|P,Q\in X\right\}=\vec{H}$ esso è sottospazio vettoriale di V. per quanto riguarda la proprietà 1 abbiamo che $\forall p\in X$ e $\forall u\in\vec{H}$ l'unico punto $x\in A$ , tale che $\vec{P_{x}}=u$ , deve $\in X$ 

OSS: Se considero $(\vec{H}, X, r_{1xxx})$ e uno spazio affine. (si dice giacitura di) oppure spazio direttore di X. 

Se un sottospazio X ha dimensione n-1, X si dice iperpiano. 

## VARIETA'LINEARE

DEF ( $\vec{\varepsilon}, \varepsilon, \pi$ ) Po $\in$ $\varepsilon$ , U sott. di $\vec{\varepsilon}$ 

La varietà lineare per Po e parallela a U, e l'insieme dei punti: 

$$
P _ {0} + U = (P _ {0}, U) = \{Q \in \varepsilon | P _ {0} Q \in U \}
$$

Prop Considero lo spazio affine (V,A,π) e X sottospazio affine. 

$\forall P \in X$ si ha che $X = \{ Q \in A : \overrightarrow{PQ} \in \overrightarrow{X} \}$ e tale insieme si diae varietal lineare passante per $P$ e parallela a $X$ 

considero un punto T ∈ X (e per ipotesi P ∈ X ma dunque la coppia (P,T) ∈ X) (x), si ha che l'immagine di (P,T) dunque π ((P,T)) ∈ π (X×X) ma π(P,T) = π e π() (x)() = π quindi T ∈ (P, H). 

2 consideriamo $Q \in (P, \vec{H})$ per definizione $\overrightarrow{PQ} \in \vec{H}$ per la proprietà 1 degli spazi affini applicata ad $X, J! X \in X : \overrightarrow{PQ} = \overrightarrow{PX}$ per cui $Q = X$ e visto che $X \in X$ (allora $Q \in X$ ) 

TEO considero lo spazio affine (V,A,π) con dimensione n e consideriamo il riferimento carte siano R=(0,B). Sia ) ( un sottospazio affine con dim ) (= dimH = h. Allora esiste un sistema lineare Σ: Ax=b in n incognite con rango (A)=n-h tale che Se' costituito dalle coordinate in R di tutti e solo i punti di ). 

Dim Consideriamo $H(-|Q\in A|\vec{P_{0}Q}\in\vec{H}|)$ ed un punto $Q\in A$ di coordinate in $R(x_{1},\ldots,x_{n})$ e un punto $P_{0}\in X$ di coordinate $(a_{1},\ldots,a_{n})$ . Noi sappiamo che $Q\in X\Leftrightarrow\vec{P_{0}Q}\in\vec{H}\Leftrightarrow$ $\Leftrightarrow\phi_{B}(\vec{P_{0}Q})\in\phi_{B}(\vec{H})\leq k^{0}$ ma poiche $\Phi_{B}(\vec{H})$ e un sottospazio di $k^{0}$ amora 

$$
\exists \Sigma_ {0}: A x = 0: S _ {0} = \phi_ {B} (\vec {H}).
$$

$$
\text { Ma   noi   sappiamo   che } \Phi_ {B} (\vec {p _ {0} Q}) = (x _ {1} - a _ {1}, \dots , x _ {n - a _ {n}}) \quad \text { dunque } \Phi_ {B} (\vec {p _ {0} Q}) \in \Phi_ {B} (\vec {H}) \Rightarrow A \binom{x _ {1} - a _ {1}}{x _ {n - a _ {n}}} = 0
$$

$$
\text { Cioe } \text { se } (x _ {1} - a _ {1},..., x _ {n} - a _ {n}) \text { e } ^ {\prime} \text { soluzione   di } E o, \text { esso   può   essere   scritto   come } A \binom{x _ {1}}{x _ {n}} = A \binom{a _ {1}}{a _ {0}}
$$

ponendo dunque $\underline{b}=A\begin{pmatrix}a_{1}\\a_{2}\end{pmatrix}$ allora troviamo il sistema $\Sigma:AX=\underline{b}$ 

TEO: Considero il sistema Σ: Ax=b compatibile in n variabili e range(A)=n-h, allora esiste un 

sottospazio affine H di A rappresentato da S. 

## SPAZI PARALLELI, RETTE SGHEMBE

DEF Un sott.spaz.euclidean di dim n-1 si dice iperpiano 

Siano H, H' due sottospazi affini, si dice che H e H' sono paralleli <=> H ⊆ H' opp. H' ⊆ → 

He H' si dicono sghembi $\Leftrightarrow$ He H' non sono paralleli e H(n) H' = $\phi$ 

$$
\text { Si   dicono   totalmente   sghembi } \iff \vec {H} _ {n} \vec {H} ^ {\prime} = \{\underline {{0}} \} \text { e } H _ {n} H ^ {\prime} = \varnothing
$$

$$
\cdot \dim E = 3 R (0, B) P _ {0} \equiv_ {R} (1, 0, 3) U = \mathcal {L} (u (1, 2, 3)) r = (P _ {0}, U) U = \overrightarrow {r}
$$

$$
Q \equiv_ {R} (x _ {1}, x _ {2}, x _ {3}) \in r \iff \overrightarrow {P _ {0} Q} \in \mathcal {L} (u (1, 2, 3)) \iff (x _ {1} - 1, x _ {2}, x _ {3} - 3) \in \mathcal {L} (\phi_ {B} (u)) = \mathcal {L} ((1, 2, 3)) <   =
$$

$$
<   = > \quad \text { range } \left( \begin{array}{c c} \frac {1}{2} & x _ {1} - 1 \\ 3 & x _ {2} \\ 3 & x _ {3} - 3 \end{array} \right) = 1 <   = > \left| \begin{array}{c c} 1 & x _ {1} - 1 \\ 2 & x _ {2} \end{array} \right| = 0 \quad \wedge \quad \left| \begin{array}{c c} 1 & x _ {1} - 1 \\ 3 & x _ {3} - 3 \end{array} \right| = 0
$$

$$
\left\{ \begin{array}{l} X _ {1} - 2 X _ {1} + 2 = 0 \\ X _ {3} - 3 - 3 x _ {1} + 5 = 0 \end{array} \right. \Rightarrow \quad \overrightarrow {n}: \left\{ \begin{array}{l} - 2 x _ {1} + x _ {2} = 0 \\ - 3 x _ {1} + x _ {3} = 0 \end{array} \right.
$$

$$
\text { In   alternative: } \exists t \in K: (x _ {1}, 1, x _ {2}, x _ {3}, 3) = t (1, 2, 3) \iff \left\{ \begin{array}{l l} x _ {2} = 2 t \\ x _ {3} = 3 + 3 t \end{array} \right. \text {   napp   parametric   dir }
$$

$$
\sim \text {   Come   funzione   la   rapp.   parametrica?   }
$$

$$
\mathrm{Sia} \quad \pi : \left\{ \begin{array}{l l} x _ {1} & = - 2 + 7 t \\ x _ {1} & = 2 - 4 t \\ x _ {3} & = 1 + t \end{array} \right. \quad d i m E = 3.
$$

$$
\begin{array}{l} {\mathrm{condiade}} \\ {\mathrm{d.8}} \end{array} \quad \begin{array}{l} {\mathrm{compensil.del}} \\ {\mathrm{velroabgewa.}} \end{array} \quad Q _ {\mathrm{windi:}} P _ {0} \equiv_ {k} (- 2, 2, 1) \quad e \quad \overline {{r}} ^ {2} = \mathcal {L} (u (7, - 5, 1)). \quad S _ {e a v e s s i} \mathcal {L} (\circ u), \mathrm{allota:} r: \left\{ \begin{array}{l l} x _ {1} & = - 2 + t \\ x _ {2} & = 2 + t \\ x _ {3} & = 1 - t \end{array} \right.
$$

$$
\cdot \quad d _ {\mathrm{im}} E = 2 \quad R = (0, B) \quad P _ {0} \equiv_ {R} (- 7, 3) \quad r ^ {2} = \mathcal {L} (u (- 1, 4)) \quad r = (P _ {0}, \bar {n} ^ {2})
$$

$$
Q \equiv_ {R} (x _ {1}, x _ {2}) \in r \quad <   = > \overrightarrow {P _ {0} Q} \in \overrightarrow {\pi^ {\prime}} <   = > (x _ {1} + 7, x _ {2} - 3) \in \mathcal {L} ((- 1, 4)) <   = >
$$

$$
\begin{array}{r l} {<   = > \mathrm{range} \left( \begin{array}{l l} {- 1} & {x _ {1} + 7} \\ {\boxed {4}} & {x _ {2} - 3} \end{array} \right) = L} & {<   = > \left| \begin{array}{l l} {- 1} & {x _ {1} + 7} \\ {4} & {x _ {2} - 3} \end{array} \right| = 0 \quad \Rightarrow \quad - x _ {2} + 3 - 4 x _ {1} - 2 8 = 0 <   = > 4 x _ {1} + x _ {2} + 2 5 = 0} \end{array}
$$

$$
\left\{ \begin{array}{l} {x _ {1} = - 9 - t ^ {0}} \\ {x _ {2} = 3 + 4 t} \end{array} \right. \quad \pi : 4 x _ {1} + x _ {2} + 2 5 = 0 \quad \overrightarrow {\pi}: 4 x _ {1} + x _ {2} = 0
$$

$$
\text {   netta   } S: S / / n \quad e R (2, 4) \in S \quad S: 4 x _ {1} + x _ {2} + k = 0 \Rightarrow k = - 1 2 \quad S: 4 x _ {1} + x _ {2} - 1 2 = 0
$$

$$
\cdot \dim E = 3 \quad R = (0, B) \quad \tau : \left\{ \begin{array}{l l} x _ {1} - x _ {1} + x _ {2} = 1 \\ x _ {2} - 2 x _ {3} = 2 \end{array} \right. \quad \left( \begin{array}{l l l} 1 & - 1 & 1 \\ 0 & 1 & - 2 & 2 \end{array} \right) \quad \text { Trovare   un   piano } \quad H: n / / H ^ {2}, R (1, 0, - 1) \in H
$$

$$
\pi : \left\{ \begin{array}{l} x _ {1} - x _ {1} + x _ {3} = 0 \\ x _ {2} - 2 x _ {3} = 0 \end{array} \right. \Rightarrow \left\{ \begin{array}{l} x _ {1} = x _ {3} \\ x _ {2} = 2 x _ {3} \end{array} \right. \quad \tilde {\pi} = \mathcal {L} (u (1, 2, 1))
$$

$$
S _ {i a} \text {   allora   } \vec {H} = \mathcal {L} (u (1, 2, 1), v (1, 0, 0))
$$

$$
Q (x _ {1}, x _ {2}, x _ {3}) \in E \quad Q \in H \Longleftrightarrow \overrightarrow {R Q} \in \overrightarrow {H} \Longleftrightarrow \exists \alpha , \beta \in R: (x _ {1} - 1, x _ {2}, x _ {3} + 1) = \alpha (1, 2, 1) + \beta (1, 0, 0).
$$

$$
<   = > \left\{ \begin{array}{l} x _ {t} = 1 + \alpha + \beta \\ x _ {t} = 2 \alpha \\ x _ {3} = - 1 + \alpha \end{array} \right.
$$

$$
\text { range } \left( \begin{array}{c c c} x _ {1} - 1 & x _ {2} & x _ {3} + 1 \\ 1 & 2 & 1 \\ 1 & 0 & 0 \end{array} \right) = 2 \quad \Longleftrightarrow \quad \left| \begin{array}{c c c} x _ {1} - 1 & x _ {2} & x _ {3} + 1 \\ 1 & 2 & 1 \\ 1 & 0 & 0 \end{array} \right| = 0 \quad \Longleftrightarrow \quad \left| \begin{array}{c c c} x _ {2} & x _ {3} + 1 \\ 2 & 1 \end{array} \right| = x _ {2} - 2 x _ {3} - 2 = 0
$$

$$
\text { Queste   e   la   rappresentazione   parametrica   di   H }
$$

Consideriamo 2 iperpiani $H: a_1 x_1 + \ldots + a_n x_n = b$ e $H': a'_1 x_1 + \ldots + a'_n x_n = b'$ si ha che. 

$$
H (n) H ^ {\prime} = \left\{ \begin{array}{l l} a _ {1} x _ {1} + \dots + a _ {n} x _ {n} = b \\ a _ {1} ^ {\prime} x _ {1} + \dots + a _ {n} ^ {\prime} x _ {n} = b ^ {\prime} \end{array} \right.
$$

se si considera solo la matrice A dei coefficienti. 

$$
C = \left( \begin{array}{c c c} a _ {1} & \dots & a n b \\ \vdots & \ddots & \vdots \\ a _ {1} ^ {\prime} & \dots & a _ {n} ^ {\prime} b ^ {\prime} \end{array} \right)
$$

Si ha che 1≤ranop(A)≤rango(C)≤2 si auranno (vari casi) 

$$
1) \operatorname{rango} (A) = \operatorname{rango} (C) = 2
$$

In tal caso, $\phi \neq r \cap r' = P(x,y), r \nmid r' (r \neq r')$ . Le rette sono incidenti in un punto 

$$
2) 1 = \text { rango } (A) <   \text { rango } (C) = 2
$$

$\overrightarrow{r}=\overrightarrow{r_{1}}$ quindi r//r' e r∩r'=∅. Le rette sono parallele 

$$
3) \quad 1 = \operatorname{rango} (A) = \operatorname{rango} (C)
$$

Allora r=r'. Si tratta dunque della stessa retta. 

PROP dim E = 0 ↕ rimane valido anche per spazi di 3,4s... dim. 

r e r' sghembe <=> r e r' NON sono complanari. 

DiM ⇒ Gia noto per quanto appena verificato nei 3 possibili casi. 

⇐ Per assurdo siano r e r' non sghembe 

re r' sghembe ⇔ r n r' = φ ∧ r ∥ r' da cui re r' non sghembe ⇔ r n r' ≠ φ v r // r' 

$$
H = (P, L (u, u))
$$

$$
(2) \frac {p ^ {\prime} \cdot \overrightarrow {u ^ {\prime}}}{p} \quad \{u, u ^ {\prime} \} \text {   LiN.DiP.   } H = (P, L (u, \overrightarrow {P P ^ {\prime}}))
$$

In entrambi i soli possibili casi, r e r' giacciano sullo stesso piano quindi sono complanari 

## - RETTE IN UNO SPAZIO

in dimensione n / posso rappresentare una retta r come: 

e poi si ha l'iperpiano H: $a_{1}x_{1}+\ldots+a_{n}\times n=b$ , di conseguenza r_nH 

$a_{1}^{n-1}x_{1}+\cdots+a_{n}^{n-1}x_{n}=b_{n-1}$ Sara l'unione di tutte le equazioni di r con quella di 

$\left( {x + 1}\right)  = \left( {x - 2}\right)$ 

Se consideriamo la matrice dei coefficienti si ha n-1≤rango(A)≤rango(c)≤n ci sono vari casi: 

$$
1) 2 = \operatorname{range} (A) = \operatorname{range} (c) \Rightarrow r = r ^ {\prime}
$$

$$
2) 2 = \operatorname{rango} (A) <   \operatorname{rango} (c) = 3 \Rightarrow r \cap r ^ {\prime} = \phi , r / / r ^ {\prime}
$$

$$
3) 3 = \operatorname{rango} (A) = \operatorname{rango} (c) \quad \Rightarrow \phi \neq r \cap r ^ {\prime} = P
$$

$$
4) 3 = \text { rango } (A) <   \text { rango } (c) = 4 \Rightarrow \text { re   r'   sghembe }
$$

$$
\cdot \text {   Piani   e   RETTE   in   UNO   SPAZIO   }
$$

$$
\dim E = 3 R = (0, B)
$$

$$
r: \left\{ \begin{array}{l} a x + b y + c z = d \\ a ^ {\prime} x + b ^ {\prime} y + c ^ {\prime} z = d ^ {\prime} \end{array} \right.
$$

$$
H: \alpha x + \beta y + \gamma z = \delta r \cap H: 1
$$

$$
C = \left( \begin{array}{l l l l} a & b & c & d \\ a ^ {\prime} & b ^ {\prime} & c ^ {\prime} & d ^ {\prime} \\ \alpha & \beta & r & \partial \end{array} \right)
$$

$$
[ 2 \leq \operatorname{range} (A) \leq \operatorname{range} (C) \leq 3 ]
$$

$$
\text {Sono nuovamente 3 i possibili casi :}
$$

$$
1) 2 = \operatorname{rango} (A) = \operatorname{rango} (c) \Rightarrow r \leq H, r \text {   giace   sul   piano   }
$$

$$
2) 2 = \operatorname{rango} (A) <   \operatorname{rango} (c) = 3 \Rightarrow r \cap H = \phi , \vec {r} ^ {2} \leq \vec {H} (\text {   quindi   } r / / H)
$$

$$
3) 3 = \operatorname{range} (A) = \operatorname{range} (c)
$$

$$
\Rightarrow \varnothing \neq r \cap H = P
$$

$$
\cdot \text {   PIANI   in   UNO   SPAZIO   }
$$

$$
\dim \varepsilon = 3 R = (0, B)
$$

$$
H: \alpha x + \beta y + \gamma z = d
$$

$$
H ^ {\prime}: \alpha x + \beta^ {\prime} y + \gamma^ {\prime} z = \delta^ {\prime}
$$

$$
H \cap H ^ {\prime}: \} = -
$$

$$
C = \left( \begin{array}{l l l} \alpha & B & r ^ {\prime}: \delta \\ \alpha^ {\prime} & B ^ {\prime} & r ^ {\prime}: \delta^ {\prime} \end{array} \right)
$$

$$
[ 1 \leq \operatorname{rango} (A) \leq \operatorname{rango} (c) \leq 2 ]
$$

$$
\text {Ancora una volta,3 possibili casi:}
$$

$$
1) l = \text { rango } (A) = \text { rango } (c) \rightarrow H = H ^ {\prime}
$$

$$
2) 1 = \text {   rango   } (A) <   \text {   rango   } (c) = 2 \Rightarrow H \cap H ^ {\prime} = \phi , H \parallel H ^ {\prime}
$$

$$
3) 2 = \operatorname{rango} (A) = \operatorname{rango} (c) \Rightarrow H \cap H ^ {\prime} = \operatorname{retta}
$$

$$
\text { ORTO   GONALITA' } \quad \text { TRA   RETTE   e   PIANI }
$$

$$
S i a (\vec {\varepsilon}, \varepsilon , \pi) \text { uno   spazio   euclideo   avente   dimensionen   e   siq } R = (0, B) \text { una   base   ortonormale. }
$$

$$
\text { se } \vec {r} \in^ {\perp} \vec {r ^ {\prime}} \text { e   si   indica   con } r \perp r ^ {\prime}
$$

$$
\text { Sia } H \text {   un   iperpiano   di   E.   Sapendo   dim)   } H = n - 1 \text {   allora   } H: a _ {1} x _ {1} + \dots + a _ {n} x _ {n} = 0 \text {   e   } H: a _ {1} x _ {1} + \dots + a _ {n} x _ {n} = 0 \text {   si }
$$

$$
\text {   ha   dunque   } \dim \vec {H} = n - 1 \text {   e   } \dim \bot \vec {H} = n - (n - 1)
$$

$$
\text { Si   puo } \quad \text { dimostrare   che } \quad + \vec {H} = L (u (a _ {1}, \ldots , a _ {n})) - \frac {\text { e } ^ {- \text { generato }} d o u v i t o r d o u n a c o m p a n t i i c o l f i c u e n d i l l ^ {\prime} q u a z i o n e}{\text { componenti }}
$$

Basta dimostrare che $\forall v \in H$ si ha $U(a_{1}, \ldots, a_{n}) \perp V$ . Partiamo coldire che 

$$
V (\overline {{x}} _ {1}, \dots , x \overline {{n}}) \in \overrightarrow {H} \iff a _ {1} \overline {{x}} _ {1} + \dots + \overline {{a}} _ {n} x _ {n} = 0 - m a c i o e i l p r o d o t t o s c a l a r e (a _ {1}, \dots , a _ {n}) (\overline {{x}} _ {1}, \dots , \overline {{x}} _ {n}), n o i
$$

sappiamo che in una base ortonormale il prodotto scalare delle componenti di due vettori e 

il prodotto scalare dei vettari stessi e poiche $U(a_{1},\ldots ,a_{n})$ e $V(\overline{x}_{1},\ldots ,\overline{x}_{n})$ allora abbia-

mo <u,v>=0 dunque e stato dimostrato che $U(a_{1},\ldots,a_{n})\perp V$ 

$$
\dim \varepsilon = 2
$$

$$
r: - 3 x + 7 y = c
$$

$$
\vec {r}: - 3 x + 7 y = 0
$$

$$
w (- 3, 7) \perp r
$$

$$
w (7, 3) \in \vec {r}
$$

DEF siano H e H' due iperpiani con 

$$
H: a _ {1 \times 1 + \dots +} a _ {n \times n} = b
$$

$$
) (1 a _ {1} x _ {1} + \dots + a _ {n} x _ {n} = b
$$

$$
\text { diciamo   che   H   e) } \left(\text { sono   ortogonali   se   } w (a _ {1}, \ldots , a _ {n}) \perp w ^ {\prime} (a _ {1}, \ldots , a _ {n}) \right.
$$

DEF Sia ( $\vec{\varepsilon}$ , $\varepsilon$ , $\pi$ ) uno spazio euclidean avente dimensione n e consideriamo il riferi-

mento cartesiano R=(0,8) con B ortonarnale. Presa una retta r e un iperpia-

$$
\text {   no   } H \text {   allora   } r \bot H \Leftrightarrow \vec {r} = ^ {\perp} \vec {H} \text {   ossia   se   } H: a _ {1} x _ {1} + \dots + a _ {n} x _ {n} = b \text {   allora   si   avra!   }
$$

$$
\vec {r} = L (\omega (a _ {1}, \dots , a _ {n}))
$$

## ORTOGONALITA' e FASCI DI PIANI

DEF in dimε=3 considerata una retta r, si definisce fascio di pioni di asse r l'insieme di piani che contengono r. Si può dimostrare che un piano appartiene al fa-

scio di asse r <= e rappresentato da un'equazione del tipo: 

$$
\lambda (a x + b y + c z - d) + \omega (a ^ {\prime} x + b ^ {\prime} y + c ^ {\prime} z - d ^ {\prime}) = 0 \quad \text {   con   } (\lambda , \omega) \in k ^ {n} \setminus \lambda_ {0}
$$

Si definisce fascio improprio di piani paralleli ad H l'insieme di tutti e sdo i piani paralleli ad H. Ogni piano passante per questo fascio si rappresenta con una 

equazione del tipo: ax+by+cz=k con k∈K. 

## LEZIONE 22

## DISTANZA

DEF La distanza tra i punti $P,Q \in \varepsilon$ e' d(P,Q) = || $\overrightarrow{PQ}$ ||. 

Se considero invece 2 sotto insiemi di punti $x, y \subseteq \varepsilon$ . 

La distanza $d(x,y) = \inf \{d(P,Q) | P \in X, Q \in V\}$ 

Sia H un iperpiano. H: $a_{1}x_{1}+\ldots+a_{n}x_{n}=b$ . Sia P ∈ E. Allora: 

$$
P \in H \Rightarrow d (P, H) = 0. \quad \text { per   il   terene   di   Patagore }
$$

$$
P \in H \Rightarrow d (P, H) = d (P, \overline {{P}}), d o v e
$$

$$
\overline {{P}} = H \cap n \quad \wedge n \text {   ortogomale   ad   } H \in P \in r.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-06/89f1c5bc-505e-44c7-83f0-c8d891089f89/6e79a8243dab460a62bf3493d6d9489a3fabef6fea8b1a3b4bd4498e6022c011.jpg)


$$
\text { Notiamo   che } \overrightarrow {P P} \text { risulta   essere   un   "calèto", }
$$

$$
\text { proiezione   ortogonale } d i P _ {i n} H
$$

$$
\text { mentre   gli   altri:   veltrui:   sono"ipotenuse". }
$$

$$
\dim E = 3 \quad H: x _ {1} - 3 x _ {2} - x _ {3} = 1 \quad P (1, 0, 1) \in H \quad d (P, H) = ?
$$

$$
P _ {n} (1 + t, - 2 t, 1 - t) \in n \quad \forall l \in \mathbb {R}
$$

$$
P _ {n} \in H \iff (1 + t) - 3 (- 3 t) - (1 - t) = 1 \iff \frac {4 t}{4 n} = \frac {1}{1 1}
$$

$$
\overline {{P}} (1 + \frac {1}{4 1}, - \frac {3}{4 1}, 1 - \frac {1}{4 1}), \mathrm{coe} \overline {{P}} (^ {1 2} _ {1 1}, - \frac {3}{4 1}, ^ {1 0} _ {1 1}) \quad \mathrm{de} \mathrm{cu:} \overline {{P P}} ^ {>} (\frac {1}{4 1}, - \frac {3}{4 1}, \frac {1}{4 1})
$$

$d(P,H)=d(P,\overrightarrow{P})=||\overrightarrow{P}\overrightarrow{P}||=\sqrt{\frac{1}{121}+\frac{9}{121}+\frac{1}{121}}=\frac{1}{\sqrt{11}}$ 

$$
d (P, H) = \frac {\vert 1 - 3 \cdot 0 - 1 1 - 1 \vert}{\sqrt {(1) ^ {2} + (- 3) ^ {2} + (1) ^ {2}}} = \frac {1}{\sqrt {1 1}}
$$

$$
\text { Generalizziamo   l' esempio: }
$$

$$
H: a _ {1} x _ {1} + \dots + a _ {n} x _ {n} = b \quad P (\overline {{x}} _ {1}, \dots , \overline {{x}} _ {n}) \quad \pi : \left\{ \begin{array}{l l} x _ {1} = \overline {{x}} _ {1} + a _ {1} t \\ x _ {n} = \overline {{x}} _ {n} + a _ {n} t \end{array} \right. \quad \vec {r} = \mathcal {L} (w ^ {*} (a _ {1}, \dots , a _ {n})) = ^ {\perp} \vec {H}
$$

$$
n H: a _ {1} (\overline {{x}} _ {1} + a _ {1} t) + \dots + a _ {n} (\overline {{x}} _ {n} + a _ {n} t) = b \quad <   = > (a _ {1} ^ {2} + \dots + a _ {n} ^ {2}) t = b - a _ {1} \overline {{x}} _ {1} - \dots - a _ {n} \overline {{x}} _ {n} \quad <   = > t = \underline {{b - a _ {1} \overline {{x}} _ {1} - \dots - a _ {n} \overline {{x}} _ {n}}}
$$

$$
\overline {{P}} (\overline {{x}} _ {1} + a _ {1} t, \dots , \overline {{x}} _ {n} + a _ {n} t) \quad \overrightarrow {P P} (a _ {1} t, \dots , a _ {n} t)
$$

$$
d (P, H) = d (P, \overline {{P}}) = \| \overrightarrow {P P} \| = \sqrt {a _ {1} ^ {2} t ^ {2} + \ldots + a _ {n} ^ {2} t ^ {2}} = | t | \sqrt {a _ {1} ^ {2} + \ldots + a _ {n} ^ {2}} = | b - a _ {1} \overline {{x}} _ {1} - \ldots - a _ {n} \overline {{x}} _ {n} | \sqrt {a _ {1} ^ {2} + \ldots + a _ {n} ^ {2}} = | a _ {1} \overline {{x}} _ {1} + \ldots + a _ {n} \overline {{x}} _ {n} - b |
$$

## DISTANZA PT.2

$$
H: a _ {1} x _ {1} + \dots + a _ {n} x _ {n} - b = 0, H ^ {\prime}: a _ {1} ^ {\prime} x _ {1} + \dots + a _ {n} ^ {\prime} x _ {n} - b ^ {\prime} = 0,
$$

$$
H \cap H ^ {\prime}: \left\{ \begin{array}{l} a _ {1} x _ {1} + \dots + a _ {n} x _ {n} - b = 0 \\ a _ {1} x _ {1} + \dots + a _ {n} x _ {n} - b = 0 \end{array} \right.
$$

$$
H \cap H ^ {\prime} \neq \emptyset \Rightarrow d (H, H ^ {\prime}) = 0 \quad c i d a l v e n o u n p u n t o i n c u s i t o c c a n o
$$

$$
H \cap H ^ {\prime} = \emptyset \Rightarrow d (H, H ^ {\prime}) = \inf \left\{d (P, P ^ {\prime}) | P \in H, P ^ {\prime} \in H ^ {\prime} \right\} = \inf \left\{d (P, \overline {{P}}) | P \in H, \overline {{P}} _ {\text { proizione   ortg.   dx }} P _ {\text { in }} H \right\}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-06/89f1c5bc-505e-44c7-83f0-c8d891089f89/a54f0a3e7a59dff1168599fdd3792ca2753af985b2830172b79f70ae73208696.jpg)


$$
\text { PROP } \quad \forall P \in H, d (P, \widetilde {P}) = d (P, H ^ {\prime}) \text {   è   costante.   }
$$

$$
\dim E = 3 \quad R = (0, B)
$$

$$
\mathrm{DIM} H / / H ^ {\prime} \Rightarrow \vec {H} ^ {\prime} = \vec {H} ^ {\prime}: a _ {1} x _ {1} + \dots + a _ {n} x _ {n} = 0.
$$

$$
H: 2 x _ {1} + x _ {2} - x _ {3} + 1 = 0 \quad W (2, 1, - 1)
$$

$$
\text { Allora: } H ^ {\prime}: a _ {1} x _ {1} + \dots + a _ {n} x _ {n} - \overline {{b}} = 0.
$$

$$
H ^ {\prime}: 4 x _ {1} + 2 x _ {2} - 2 x _ {3} - 7 = 0 \quad W ^ {\prime} (4, 2, - 2)
$$

$$
\forall P \in H, P (\bar {x} _ {1}, \dots , \bar {x} _ {n}), a _ {1} \bar {x} _ {1} + \dots + a _ {n} \bar {x} _ {n} - b = 0 \Rightarrow b = a _ {1} \bar {x} _ {1} + \dots + a _ {n} \bar {x} _ {n}.
$$

$$
w / / w ^ {\prime} \Rightarrow \overrightarrow {H} = \overrightarrow {H ^ {\prime}} H ^ {\prime}: 2 x _ {1} + x _ {2} - x _ {3} - 2 / 2 = 0 \quad \overrightarrow {b} = 2 / 2
$$

$$
d (P, H ^ {\prime}) = \frac {| a _ {1} \bar {x} _ {1} + \ldots + a _ {n} \bar {x} _ {n} - \bar {b} |}{\sqrt {a _ {1} ^ {2} + \ldots + a _ {n} ^ {2}}} = \frac {| b - \bar {b} |}{\sqrt {a _ {1} ^ {2} + \ldots + a _ {n} ^ {2}}} \quad \forall P \in H
$$

$$
d (H, H ^ {\prime}) = \frac {| - 1 - 7 / 2 |}{\sqrt {4 + 1 + 1}} = \frac {9 / 2}{\sqrt {6}}
$$

$$
(\vec {\varepsilon}, \varepsilon , \pi) \quad d i m \varepsilon = 2
$$

$$
\text {   I   sottosp.   euclidei   sono   i   punti,   le   rette   ed   E   stesso.   }
$$

$$
\text { Qui,   dunque,   sappiamo   calcolare   la   distanza   tre   i   possibili:   sottospezi. }
$$

$$
(\vec {\varepsilon}, \varepsilon , \pi) \quad d i m \varepsilon = 3
$$

$$
\text { I   sottosp.   euclidei   sono   i   punti,   le   rette,   i   piani:ed   E   stesso. }
$$

$$
\cdot \text {   distanza   di   una   retta   de   un   iperpiano   (=piano   in   questo   caso)   }
$$

$$
n \text { netta: } \left\{ \begin{array}{l} a _ {1} x _ {1} + a _ {2} x _ {2} + a _ {3} x _ {3} = b \\ a _ {1} ^ {\prime} x _ {1} + a _ {2} ^ {\prime} x _ {2} + a _ {3} ^ {\prime} x _ {3} = b ^ {\prime} \end{array} \right.
$$

$$
n \cap H = \left\{ \begin{array}{l l} P \Rightarrow d (n, H) = 0 \\ \varnothing \Rightarrow d (n, H) = ? \end{array} \right.
$$

$$
H _ {\mathrm{piano}}: \alpha_ {1} x _ {1} + \alpha_ {2} x _ {2} + \alpha_ {3} x _ {3} = \beta
$$

$$
\text { Sie   } H ^ {\prime} \text {   ipenpiano:   } H / / H ^ {\prime} \wedge n \in H ^ {\prime}. \text {   Questo   ipenpiano   esiste,   ingatti:   } n / / H \Rightarrow \overrightarrow {n ^ {\prime}} \in \overrightarrow {H ^ {\prime}} = \overrightarrow {H ^ {\prime}} \quad \text { Pen,   } H ^ {\prime} = (P, \overrightarrow {H ^ {\prime}})
$$

$$
\forall P \in H ^ {\prime}, d (P, H) \text {   è   costante.   Allora,   } \forall P \in n \subseteq H ^ {\prime}, d (P, H) \text {   è   costante:   } d (P, H ^ {\prime}) = d (n, H ^ {\prime})
$$

$$
\ln \text {   conclusione:   } d (\pi , H) = d (P, H) \quad \forall P \in \pi .
$$

$$
(\vec {\varepsilon}, \varepsilon , \pi) \quad d i m \varepsilon = 3
$$

$$
\text {   distanza   tra   nette   } \pi_ {e n t}
$$

$$
(1) n \cap n ^ {\prime} \neq \emptyset \Rightarrow d (n, n ^ {\prime}) = 0
$$

$$
(2) n / / n ^ {\prime} \wedge n \neq n ^ {\prime} \Rightarrow n _ {2} n ^ {\prime} \text { complanari }
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-06/89f1c5bc-505e-44c7-83f0-c8d891089f89/4bd90f235e64b7c3bc944107b4df0716098499bf98c197a3bfeff8fee8123c6f.jpg)


$$
\forall P \in \pi , d (P, n ^ {\prime}) \text {   è   costante.   } d (n, n ^ {\prime}) = d (P, n ^ {\prime}) \forall P \in \pi . F _ {i s s o} P.
$$

$$
\text { Allora   considero   H   ipenpiano:   H   \pm   n'   e   P   \in   H. }
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-06/89f1c5bc-505e-44c7-83f0-c8d891089f89/9712340bdfe311fb888b555aca13cc748f3dc2e28fbc25566db6d0086b711656.jpg)


$$
n ^ {\prime} \cap H = \overline {{P}} \text { proiezione   ortog.   di } P \text { su } n ^ {\prime}. d (n, n ^ {\prime}) = d (P, n ^ {\prime}) = d (P, \overline {{P}})
$$

$$
n: \left\{ \begin{array}{l} x _ {1} = 4 + t \\ x _ {2} = - 4 + t \\ x _ {3} = 3 - t \end{array} \right. \quad n ^ {\prime}: \left\{ \begin{array}{l} x _ {1} = 2 t ^ {\prime} \\ x _ {2} = 4 + t ^ {\prime} \\ x _ {3} = 1 - 2 t ^ {\prime} \end{array} \right. \quad n / / n ^ {\prime}, \text {   in   get   } t: \vec {n} = \mathcal {L} (u (1, 2, - 1), \vec {n} ^ {\prime} = \mathcal {L} (v (2, 4, - 2)) \quad v = 2 u
$$

$$
P ^ {\prime} (0, 0, 1) \in \pi^ {\prime} d (n, n ^ {\prime}) = d (n, P ^ {\prime})
$$

$$
H _ {\perp \pi} = > H: x _ {t + 2} x _ {t - x _ {3} - k = 0}
$$

$$
\overline {{{P}}} = n \cap H: P _ {n} \in \pi , P _ {n} (1 + t, - 1 + 2 t, 3 - t) \in H \Leftrightarrow (1 + t) + 2 (- 1 + 2 t) - 1 (3 + t) + 1 = 0 \Leftrightarrow 6 t - 3 = 0 \Leftrightarrow t = 1 / 2.
$$

$$
\overline {{P ^ {\prime}}} \left(1 + v _ {2}, - 1 + 2, v _ {2}, 3 - v _ {2}\right) \quad \overline {{P ^ {\prime}}} \left(3 / 2, 0, 5 / 2\right) \quad d (r, r ^ {\prime}) = d (\overline {{P}}, P ^ {\prime}) = \| \overline {{P}} P ^ {\prime} \| = \sqrt {\frac {3}{4} + \frac {3}{4}} = \sqrt {\frac {1 8}{4}} = \frac {3}{\sqrt {2}}
$$

$$
(3) n \in n ^ {\prime} s q l e m b o
$$

TEOREMA DELLA COMUNE PERPENDICOLARE\ DIST. TRA RETTE SGHEMBE. 

Siano r e r' due rette sghembe allora esiste un'unica retta s tale che $\pm r$ e $\pm r'$ e i punti $P = snr$ e $P' = snr'$ per il teo di pitagora allora la distanza $d(r,r') = d(p,p')$ 

$$
\left( \begin{array}{l} x = x _ {0} + l t \\ y = y _ {0} + m t \\ z = z _ {0} + n t \end{array} \right)
$$

$$
r ^ {\prime}: \left( \begin{array}{l} x = x ^ {\prime} 0 + e ^ {\prime} t ^ {\prime} \\ y = y ^ {\prime} 0 + m ^ {\prime} t ^ {\prime} \\ z = z ^ {\prime} 0 + n ^ {\prime} t ^ {\prime} \end{array} \right)
$$

$$
e \text {   si   ha   che   } \vec {r} = L (U (L, m, n)) e \vec {r} = L (U ^ {\prime} (L ^ {\prime}, m ^ {\prime}, n ^ {\prime}))
$$

$$
P (x _ {0} + e t, y _ {0} + m t, z _ {0} + n t) \in P ^ {\prime} (x ^ {\prime} o + e ^ {\prime} t ^ {\prime}, y ^ {\prime} o + m ^ {\prime} t ^ {\prime}, z ^ {\prime} o + n ^ {\prime} t ^ {\prime}) \text { poiche }
$$

la retta cercata passa per Pe per P' il suo vettore direzionale sara 

$\overrightarrow{PP'}(x'0+e'l'-x0-lt,y'0+m'i'-y0-mt,z'0+n'i'-z0-nt)$ e tale vettore deve essere ortogonale a u e u' e si ha 

$$
\Leftrightarrow \angle \overrightarrow {P P ^ {\prime}}, u > = 0 e \angle \overrightarrow {P P ^ {\prime}}, u ^ {\prime} > = 0 \Leftrightarrow \left\{ \begin{array}{l l} (x ^ {\prime} 0 + e ^ {\prime} t ^ {\prime} - x _ {0} - e t) e + (y ^ {\prime} 0 + m ^ {\prime} t ^ {\prime} - y _ {0} - m t) m + (z ^ {\prime} 0 + n ^ {\prime} t ^ {\prime} - z _ {0} - n t) n = 0 \\ (x ^ {\prime} 0 + e ^ {\prime} t ^ {\prime} - x _ {0} - e t) e ^ {\prime} + (y ^ {\prime} 0 + m ^ {\prime} t ^ {\prime} - y _ {0} - m t) m ^ {\prime} + (z ^ {\prime} 0 + n ^ {\prime} t ^ {\prime} - z _ {0} - n t) n ^ {\prime} = 0 \end{array} \right.
$$

$$
\Rightarrow \left\{ \begin{array}{l} (e ^ {1} e + m ^ {\prime} m + n ^ {\prime} n) t + (- e ^ {2} - m ^ {2} - n ^ {2}) t + \dots + = 0 \\ (e ^ {1 ^ {2}} + m ^ {2} + n ^ {2}) t ^ {\prime} + (- e e ^ {1} - m m ^ {\prime} - n n ^ {\prime}) t + \dots + \dots = 0 \end{array} \right.
$$

$$
: A = \left( \begin{array}{l l} <   u, v ^ {\prime} > & - \| u \| ^ {2} \\ \| u ^ {\prime} \| ^ {2} & - <   v, u ^ {\prime} > \end{array} \right)
$$

$$
\text {   il   determinante   di   A,   cioè   } | A |, e ^ {-} = 0 \Leftrightarrow - <   (0, u ^ {\prime}) ^ {2} + \| u \| ^ {2} \| u ^ {\prime} \| ^ {2} = 0
$$

ma dalla disuguaglianze di Schwartz sappiamo che questo vale solo se 10,000 sono LiN. Dip., ma re r' sono sghembe quindi 10,000 sono LiN. IND. dunque possiamo dire che 1Al±0 e dunque possiamo applicare il teorema di cramer che ci garantisce che 3! (t,t') soluzione del sistema 