# Fondamenti Probabilità
## Definizioni

Esperimento: Operazione/azione - o insieme di operazioni/azioni - il cui esito dà uno tra tanti risultati possibili; 

Spazio dei campioni - o spazio campione - comunemente denotato con Ω: insieme - non necessariamente numerico - di tutti i risultati possibili di un esperimento; 

Ω può essere continuo o discreto: per il momento assumeremo che sia discreto, cioè finito o numerabile. 

Evento: un qualunque sotto-insieme di Ω definito matematicamente da un insieme di suoi elementi e lessicalmente da una proposizione; 

Evento elementare: uno dei possibili |Ω| elementi di Ω. Si indica anche con $\omega \in \Omega$ 

Un evento è univocamente individuato dagli elementi che lo compongono; 

Al contrario, la proposizione che lo definisce non è unica. 

## Esempio #1 : lancio di una moneta

Lancio singolo: 

Spazio campione: $\Omega = \{ \mathsf { T e s t a } , { \mathsf { C r o c e } } \} = \{ T , C \} , | \Omega | = 2 ;$ 

Esempi di eventi: 

$$
A = \text {   Testa   } = \{T \} \quad B = \text {   Croce   } = \{C \} \quad \text {   Testa   o   Croce   } = A \cup B
$$

Lancio doppio 

Spazio campione: 

$$
\Omega = \{T T, T C, C T, C C \} = \{T, C \} \times \{T, C \} = \{T, C \} ^ {2}.
$$

Esempi di eventi: 

$$
A = \{\# \text { croci   dispari } \} = \{T C, C T \}
$$

$$
B = \{\text { N   e   s   s   u   n   a   c   r   o   c   e } \} = \{T T \}
$$
## Qualche richiamo di insiemistica -1

Siano $\{ A _ { i } \} _ { i = 1 } ^ { M }$ M sotto-insiemi di un insieme $\Omega .$ . Definiamo: 

Unione tra due sotto-insiemi, $A _ { 1 } \cup A _ { 2 }$ , un sotto-insieme di $\Omega$ che contenga tutti gli elementi di $A _ { 1 }$ e quelli di $A _ { 2 }$ , ovviamente contando una sola volta quelli comuni; 

Complemento in $\Omega$ di un sotto-insieme $A _ { 1 }$ l’insieme $\overline { { A _ { 1 } } }$ che contiene tutti gli elementi di $\Omega$ che non appartengono a $A _ { 1 }$ ; ovviamente $\overline { { \Omega } } = \emptyset , \overline { { \overline { { A _ { 1 } } } } } = A _ { 1 } \mathrm { ~ e ~ } A _ { 1 } \cup \overline { { \overline { { A _ { 1 } } } } } = \Omega$ 

Intersezione tra due sotto-insiemi, $A _ { 1 } \cap A _ { 2 }$ , l’insieme che contiene tutti e soli gli elementi comuni a $A _ { 1 }$ e $A _ { 2 }$ 

Sottrazione tra due insiemi, $A _ { 1 } \setminus A _ { 2 }$ , l’insieme che contiene gli elementi di $A _ { 1 }$ che non appartengono a $A _ { 2 }$ . Ovviamente avremo: 

$$
A _ {1} \setminus A _ {2} = A _ {1} \cap \overline {{A _ {2}}}
$$

## Alcune proprietà delle pmf condizionate

$p _ { Y \mid X } ( y | x )$ se x resta fisso e y varia in Y è una legge di probabilità. Infatti: 

$$
p _ {Y | X} (y | x) \geq 0 \quad \sum_ {y \in \mathcal {Y}} p _ {Y | X} (y | x) = \mathbb {P} \left(\cup_ {y \in \mathcal {Y}} \{Y = y \} | \{X = x \}\right) = \mathbb {P} (\Omega | \{X = x \}) = 1
$$

La proprietà di marginalizzazione della pmf congiunta (vedi slide 71) si scrive in termini di pmf condizionali nella forma: 

$$
p _ {X} (x) = \sum_ {y \in \mathcal {Y}} p _ {X, Y} (x, y) = \sum_ {y \in \mathcal {Y}} p _ {X | Y} (x | y) p _ {Y} (y)
$$

$$
p _ {Y} (y) = \sum_ {x \in \mathcal {X}} p _ {X, Y} (x, y) = \sum_ {x \in \mathcal {X}} p _ {Y | X} (y | x) p _ {X} (x)
$$

Si noti che questa non è altro che la legge della probabilità totale (vedi slide 37) scritta, per la prima equazione, per l’evento $\{ X = x \}$ rispetto alla partizione $\Omega = \cup _ { y \in \mathcal { y } } \{ Y = y \}$ e, per la seconda equazione, per l’evento $\{ Y = y \}$ rispetto alla partizione $\Omega = \cup _ { x \in { \mathcal { X } } } \{ X = x \}$ 

Si noti, infine, che se $X \textsf { e Y }$ sono indipendenti: 

$$
p _ {Y | X} (y | x) = p _ {Y} (y)
$$

$$
p _ {X \mid Y} (x \mid y) = p _ {X} (x)
$$

## Generalizzando...

Si consideri una terna di variabili aleatorie (X , Y , Z ), distribuite secondo $p x , Y , Z ( x , y , z ) , ( x , y , z ) \in \mathcal { X } \times \mathcal { Y } \times \mathcal { Z } .$ 

Usando consecutivamente la legge della probabilità composta, otteniamo: 

$$
\mathbb {P} (X = x, Y = y, Z = z) = \mathbb {P} (X = x, Y = y | Z = z) \mathbb {P} (Z = z) =
$$

$$
\mathbb {P} (X = x \mid Z = z, Y = y) \mathbb {P} (Y = y \mid Z = z) \mathbb {P} (Z = z)
$$

che ci introduce alla ”regola della catena” (ogni permutazione dei pedici e degli argomenti è ovviamente possibile): 

$$
p _ {X \mid Y, Z} (x \mid y, z) = \frac {p _ {X , Y \mid Z} (x , y \mid z)}{p _ {Y \mid Z} (y \mid z)} \rightarrow p _ {X, Y, Z} (x, y, z) = p _ {Z} (z) p _ {Y \mid Z} (y \mid z) p _ {X \mid Y, Z} (x \mid y, z)
$$

La terna è dunque indipendente se e solo se $p _ { X | Y , Z } ( x | y , z ) = p _ { X } ( x )$ 

$$
p _ {Y | X, Z} (y | x, z) = p _ {Y} (y) \in p _ {Z | X, Y} (z | x, y) = p _ {Z} (z).
$$

## Esempio: Emissione di 3 bit da una sorgente binaria

Si consideri una sorgente binaria che emetta tre bit, siano ess $\left( B _ { 1 } , B _ { 2 } , B _ { 3 } \right)$ $B _ { i } \in \{ 0 , 1 \}$ ; 

Si assegnano le due leggi congiunte $p _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } ) \in q _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ della tabella $( 0 < \alpha < 1 )$ 

Dire se $( B _ { 1 } , B _ { 2 } ) , ( B _ { 1 } , B _ { 3 } ) , ( B _ { 2 } , B _ { 3 } ) , ( B _ { 1 } , B _ { 2 } , B _ { 3 } )$ sono o meno indipendent secondo $p _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } ) / q _ { B _ { 1 } , B _ { 2 } , B _ { 3 } } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$ 

<table><tr><td><eq>(b_1, b_2, b_3)</eq></td><td><eq>p_{B_1, B_2, B_3}(b_1, b_2, b_3)</eq></td><td><eq>q_{B_1, B_2, B_3}(b_1, b_2, b_3)</eq></td></tr><tr><td>000</td><td><eq>$(1 - \alpha)^3$</eq></td><td><eq>(1 - \alpha)^2</eq></td></tr><tr><td>001</td><td><eq>\alpha(1 - \alpha)^2</eq></td><td>0</td></tr><tr><td>010</td><td><eq>\alpha(1 - \alpha)^2</eq></td><td>0</td></tr><tr><td>011</td><td><eq>\alpha^2(1 - \alpha)</eq></td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>100</td><td><eq>\alpha(1 - \alpha)^2</eq></td><td>0</td></tr><tr><td>101</td><td><eq>\alpha^2(1 - \alpha)</eq></td><td><eq>\alpha(1 - \alpha)</eq></td></tr><tr><td>110</td><td><eq>\alpha^2(1 - \alpha)</eq></td><td><eq>\alpha^2</eq></td></tr><tr><td>111</td><td><eq>\alpha^3</eq></td><td>0</td></tr></table>

## pdf e CDF condizionali di variabili Laplaciane

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c9bb9b6105893847da5816e4162cf664c0a5d6c418d723bc46ff1a263cd47a27.jpg)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/c151e31d1c7e39157c315436b8b74f28bd1d6631fb7d6d648dfe224e47f288e4.jpg)

## Legge della probabilità totale per pdf e medie

In modo del tutto analogo al caso discreto (vedi slide 56) si può mostrare che, se $\{ E _ { m } \} _ { m = 1 } ^ { M }$ è una qualunque partizione di $\Omega ,$ , allora: 

$$
f _ {X} (x) = \sum_ {m = 1} ^ {M} f _ {X | E _ {m}} (x) \mathbb {P} (E _ {m}) \Longleftrightarrow F _ {X} (x) = \sum_ {m = 1} ^ {M} F _ {X | E _ {m}} (x) \mathbb {P} (E _ {m})
$$

Naturalmente, questo implica che per le medie valga un’analoga relazione (vedi slide 57): 

$$
\mathbb {E} \left[ X \right] = \sum_ {m = 1} ^ {M} \mathbb {E} \left[ X | E _ {m} \right] \mathbb {P} (E _ {m}) = \sum_ {m = 1} ^ {M} \mathbb {P} (E _ {m}) \int_ {\mathbb {R}} x f _ {X | E _ {m}} (x) d x
$$

Quindi, con riferimento all’esempio precedente con $\begin{array} { r } { X \sim \mathcal { L } ( \lambda ) } \end{array}$ 

$$
\mathbb {E} [ X ] = \mathbb {E} \left[ X | \{- 1 \leq X \leq 2 \} \right] \mathbb {P} (- 1 \leq X \leq 2) + \mathbb {E} \left[ X | \{X \notin [ - 1, 2 ] \} \right] \underbrace {\mathbb {P} (X \notin [ - 1 , 2 ])} _ {1 - \mathbb {P} (- 1 \leq X \leq 2)} = 0
$$

## Legge di Bayes per vettori aleatori
• Consideriamo un vettore aleatorio discreto con pmf $p _ { X } ( { \pmb x } )$ . Sappiamo che la Legge di Bayes assicura che 

$$
\mathbb {P} (A \cap B) = \mathbb {P} (A | B) \mathbb {P} (B)
$$

• Posto $A = \{ X _ { n } = x _ { n } , \ldots , X _ { 2 } = x _ { 2 } \} \textsf { e } B = \{ X _ { 1 } = x _ { 1 } \}$ avremo 

$$
p _ {\boldsymbol {X}} (\boldsymbol {x}) = \mathbb {P} \left\{X _ {n} = x _ {n}, \dots , X _ {2} = x _ {2} | X _ {1} = x _ {1} \right\} \mathbb {P} \left\{X _ {1} = x _ {1} \right\}
$$

• Iterando il ragionamento avremo la regola della catena: 

$$
\begin{array}{c} p _ {X} (x) = \mathbb {P} \{X _ {1} = x _ {1} \} \mathbb {P} \left\{X _ {2} = x _ {2} | X _ {1} = x _ {1} \right\} \dots \mathbb {P} \left\{X _ {n} = x _ {n} | X _ {n - 1} = x _ {n - 1}, \ldots , X _ {1} = x _ {1} \right\} \\ = \prod_ {i = 1} ^ {n} p _ {X _ {i} | X _ {i - 1}, \ldots , X _ {1}} (x _ {i} | x _ {i - 1}, \ldots , x _ {1}), \qquad p _ {X _ {1} | X _ {0}} (x _ {1} | x _ {0}) = p _ {X _ {1}} (x _ {1}) \end{array}
$$

• Analogamente, per vettori continui avremo 

$$
f _ {\boldsymbol {X}} (\boldsymbol {x}) = \prod_ {i = 1} ^ {n} f _ {X _ {i} | X _ {i - 1}, \dots , X _ {1}} (x _ {i} | x _ {i - 1}, \dots , x _ {1})
$$
