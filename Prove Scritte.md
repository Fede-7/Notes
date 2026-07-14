Ecco il ranking completo che include tutti gli esercizi presenti nel file PDF e i due compiti scritti che hai caricato, organizzato per livello di difficoltà:

#### Ranking di Difficoltà:

Difficoltà **Bassa**
* Esercizio 7 del PDF - Calze 
* Esercizio 2 del PDF - PMF congiunta 
Difficoltà **Media**
* Esercizio 9 del PDF - Poisson/Ufficio Postale 
* Esercizio 2 del compito (15 giugno 2025) - Candidati/Misture
* Esercizio 8 del PDF - Trasformazione $Y=\ln X$ 
* Esercizio 6 del PDF - Roulette 
Difficoltà **Medio-Alta**
* Esercizio 10 del PDF - Verifica CDF 
* Esercizio 1 del PDF - Variabile Esponenziale 
* Esercizio 1 del compito (15 giugno 2025) - Dadi/Inferenza
* Esercizio 1 del compito (4 giugno 2026) - Dadi/Inferenza
* Esercizio 2 del compito (4 giugno 2026) - Gaussiane e Quantizzazione
Difficoltà **Alta**
* Esercizio 3 del compito (4 giugno 2026) - Test di Ipotesi
* Esercizio 3 del compito (15 giugno 2025) - Stimatore Poissoniano
* Esercizio 5 del PDF - Stimatore Poissoniano 
* Esercizio 3 del PDF - Gaussiane e Quantizzazione 
Difficoltà **Molto Alta**
* Esercizio 4 del PDF - Test di Neyman-Pearson 

*Nota: La difficoltà è determinata dal livello di astrazione matematica, dalla complessità delle operazioni (calcoli integrali, derivate di verosimiglianza) e dalla necessità di dimostrazioni teoriche.
##### Esercizi di allenamento
###### 1°
La variabile aleatoria X ha pdf $\begin{array} { r } { f _ { X } ( x ) = \frac { 1 } { 6 } \exp { \left( - \frac { | x | } { 3 } \right) } , x \in \mathbb { R } . } \end{array}$ 
a. Determinare CDF, media e varianza di $X { \mathrm { : } }$ ; 
b. Si supponga ora di voler quantizzare X a due bit mediante la trasformazione 
$$
V = \left\{ \begin{array}{l l} - 2 & X <   - x _ {1} \quad \text {"00"} \\ - 1 & - x _ {1} \leq X <   0 \quad \text {"01"} \\ 1 & X \leq x _ {1} \quad \text {"10"} \\ 2 & X > x _ {1} \quad \text {"11"} \end{array} \right.
$$
con $x _ { 1 } > 0$ . Si determinino pmf, media e varianza di V in funzione di $x _ { 1 }$ 
c. Si determini il valore di $x _ { 1 }$ che rende V uniforme. 
###### 2°
Le variabili aleatorie X ed Y hanno la seguente pmf congiunta 
<table><tr><td>x\y</td><td>2</td><td>4</td><td>6</td></tr><tr><td>1</td><td><eq>1/10</eq></td><td><eq>1/10</eq></td><td><eq>1/10</eq></td></tr><tr><td>3</td><td>0</td><td><eq>3/20</eq></td><td><eq>1/4</eq></td></tr><tr><td>5</td><td><eq>3/20</eq></td><td><eq>1/10</eq></td><td><eq>1/20</eq></td></tr></table>
a. Calcolare la probabilità che X sia maggiore di 2 dato che Y è minore o uguale a 4. 
b. Determinare la densità marginale, la media e la varianza di X e di $Y$ . 
c. Calcolare l’indice di correlazione tra $X \mathrm { ~ e ~ } Y$ . Sono indipendenti? 
###### 3°
Siano $X \sim \mathcal { N } ( 1 , 4 ) \textrm { e } Y \sim \mathcal { N } ( - 1 , 9 )$ due variabili aleatorie congiuntamente Gaussiane con coeficiente di correlazione $\rho \textup { e }$ si formi la variabile aleatoria $Z = 3 X - 2 Y$ . Si determini: 
a La pdf di Z in funzione di $\rho ;$ 
b Volendo quantizzare Z a 1 bit, si esegue la conversione analogico-digitale: 
$$
U = \left\{ \begin{array}{r l} 1 & Z > \eta \\ - 1 & Z <   \eta \end{array} \right.
$$
Determinare media e varianza di $U ;$ 
c Determinare η in modo che U sia uniforma. 
###### 4°
Si supponga di avere una collezione di dati $r ^ { n } = [ r _ { 1 } , \ldots , r _ { n } ] \in \mathbb { R } ^ { n }$ . Si supponge di voler discriminare tra le due ipotesi $H _ { 1 } \mathrm { ~ e ~ } H _ { 0 }$ : 
$$
R _ {i} = \left\{ \begin{array}{l l} A + W _ {i} & H _ {1} \\ - A + W _ {i} & H _ {0} \end{array} \right.
$$
dove $W _ { i }$ sono variabili Gaussiane standard indipendenti e identicamente distribuite, mentre A è una costante deterministica. 
a Si determini la forma più semplice del test di Neyman-Pearson atto a decidere se sia vera l’ipotes $H _ { 1 }$ o l’ipotesi nulla $H _ { 0 } { \mathrm { : } }$ ; 
b Si determinino potenza e livello di significatività del test in funzione della soglia di rivelazione e di $A ;$ c Dimostrare che, quando $n  \infty ,$ , la ROC tende al caso ideale. 
###### 5°
Siano $X _ { 1 } , \ldots , X _ { n }$ n variabili aleatorie condizionalmente indipendenti e Poissoniane, cioè: 
$$
p _ {X _ {i} | \Lambda} (x _ {i} | \lambda) = \operatorname * {P r} \left\{X _ {i} = x _ {i} | \Lambda = \lambda \right\} = \frac {\lambda^ {x _ {i}}}{x _ {i} !} e ^ {- \lambda}, \quad x _ {i} \in \{0, 1, \ldots \} \qquad p _ {\boldsymbol {X} ^ {n} | \Lambda} (\boldsymbol {x} ^ {n} | \lambda) = \prod_ {i = 1} ^ {n} p _ {X _ {i} | \Lambda} (x _ {i} | \lambda)
$$
dove Λ è una variabile aleatoria con pdf esponenziale di parametro noto $\mu ,$ cioè $f _ { \Lambda } ( \lambda ) = \mu e ^ { - \lambda \mu } \mathrm { u } ( \lambda )$ ). A partire da $\pmb { x } ^ { n } = ( x _ { 1 } , \ldots , x _ { n } )$ si vuole ottenere una stima del parametro λ. 
a. Si determini ${ \widehat { \Lambda } } _ { \mathrm { M A P } } ( X ^ { n } )$ , lo stimatore MAP del parametro aleatorio $\Lambda ;$ ; 
b. Si dica se lo stimatore è polarizzato e se è consistente; 
c. opzionale: Si ripetano i punti precedenti nel caso che λ sia un parametro deterministico non noto. 
###### 6°
Un giocatore ha x euro e si siede ad un tavolo di roulette. Il giocatore punta ad ogni giocata 1 euro e si alza dal tavolo solo quando o ha finito il danaro o realizza una vincita. Ricordando che i numeri della roulette sono 37: 
a Detta N la variabile aleatoria che modella il numero delle giocate efettuate, dimostrare che risulta : 
$$
\operatorname * {P r} \{N = \ell \} = \left\{ \begin{array}{l l} \frac {1}{3 7} \left(\frac {3 6}{3 7}\right) ^ {\ell - 1} & \ell <   x \\ \left(\frac {3 6}{3 7}\right) ^ {x} + \frac {1}{3 7} \left(\frac {3 6}{3 7}\right) ^ {x - 1} & \ell = x \\ 0 & \ell > x \end{array} \right.
$$
b Determinare la probabilità che il giocatore si alzi dal tavolo avendo in tasca almeno un euro; 
c Determinare la pmf di N nel caso che il giocatore si limiti a puntare alternativamente sul rosso o sul nero (ricordando che lo zero non è nè nero nè rosso). 
###### 7°
Una cesta contiene 100 calze, di cui 30 rosse, 50 blu $\textrm { e } 2 0$ bianche, tutte mischiate tra loro. 
a Determinare la probabilit´a di estrarre due calze bianche nelle prime due estrazioni; 
b Determinare la probabilit´a di estrarre due calze dello stesso colore nelle prime due estrazioni; 
c Determinare la probabilit´a di estrarre due paia di calze blu nelle prime quattro estrazioni. 
###### 8°
Sia X una variabile aleatoria esponenziale a media 1 e si consideri la variabile aleatoria: 
$$
Y = \ln X
$$
a Si determini l’alfabeto, la pdf e la CDF di $Y ;$ 
b Con riferimento alla variabile 
$$
Z = \operatorname{sgn} (Y) = \left\{ \begin{array}{l l} 1 & \text {se Y > 0} \\ - 1 & \text {se Y <   0} \end{array} \right.
$$
si determini la media di $Z ;$ 
c Si determini la varianza di $Z .$ 
###### 9°
 Il numero di clienti presenti in un uficio postale tra le 10 e le 11 del mattino di un giorno feriale ´e una variabile aleatoria di Poisson di varianza 100. Sapendo che di queste il 60% ´e donna, determinare: 
a La probabilit´a che non entrino donne tra le 10 e le 11 del mattino; 
b La media e la varianza del numero di donne presenti nell’uficio tra le 10 e le 11; 
c Il numero medio di uomini presenti nell’uficio nell’arco di tempo considerato. 
###### 10°
Si consideri la funzione:
$$
g (x) = \left\{ \begin{array}{l l} \frac {1}{2} e ^ {x + 1} & x \leq - 1 \\ \frac {1}{2} & - 1 \leq x \leq 2 \\ \left[ 1 - \frac {1}{2} e ^ {- (x - 2) ^ {2}} \right] & x \geq 2 \end{array} \right.\tag{1}
$$
a Schizzare l’andamento della funzione e verificare che essa è una possibile CDF di una variabile aleatoria continua $X$ , determinandone l’alfabeto; 
b Determinare la pdf e calcolare $\operatorname* { P r } \{ X > 0 \}$ ; 
c Determinare Pr $\{ X > 3 | X > - 2 \}$ 
##### Esercizi Prove Scritte
> [!info] Info:
> La prova conterrà solo **3 esercizi**.
> Considera quindi che i 10 di prima sono le possibili tipologie

###### 15 giugno 2025 - Tempo massimo: 3 ore 
1. Un bussolotto contiene tre dadi, indistinguibili per colore e peso, di cui due onesti, e uno truccato in modo che il 6 esca con probabilità pari a 5 volte quella di un qualunque altre risultato (gli altri risultati sono tra loro equiprobabili). L'esperimento consiste nell'estrarre un dado e nel lanciarlo: se il risultato - sia esso R - è 6 si estrae un altro dado e lo si lancia fino a quando si ottiene un 6, mentre se il risultato del primo lancio non è 6 si continua a lanciare lo stesso dado fino a quando non si ottiene 6. Sia X la variabile aleatoria che modella il numero dei lanci effettuati (successivi al primo). 
a. Determinare alfabeto e pmf di X; 
b. Determinare la media statistica di X; 
c. Sapendo che X = 2, calcolare la probabilità che il dado sia truccato. 
2. Un'azienda sottopone i candidati all'assunzione ad un test a risposta multipla. Il tempo dopo il quale il generico candidato finisce il test viene modellato come una variabile aleatoria esponenziale di media 30 minuti, se il candidato appartiene alla categoria A, di media 50 minuti se appartiene alla categoria B e di media 60 minuti se appartiene alla categoria C. Si supponga inoltre che i candidati della categoria A siano in numero pari alla metà di quelli delle altre due categorie, che hanno entrambe lo stesso numero di candidati e che il numero totale di candidati sia 100. 
a. Detta X la variabile aleatoria che indica il tempo dopo il quale un candidato scelto a caso finisce il test, determinarne la pdf; 
b. Sapendo che un candidato ha consegnato la prova prima che trascorrano 40 minuti (cioè, X < 40), calcolare la probabilità che appartenga alla categoria B; 
c. Si determinino E[X] e var(X). 
3. Siano $X_{1},\ldots,X_{n}$ n variabili aleatorie condizionalmente indipendenti e Poissoniane, cioè: 
$$
p _ {X _ {i} | \Lambda} (x _ {i} | \lambda) = \operatorname * {P r} \left\{X _ {i} = x _ {i} | \Lambda = \lambda \right\} = \frac {\lambda^ {x _ {i}}}{x _ {i} !} e ^ {- \lambda}, \quad x _ {i} \in \{0, 1, \dots \} \quad p _ {X ^ {n} | \Lambda} (x ^ {n} | \lambda) = \prod_ {i = 1} ^ {n} p _ {X _ {i} | \Lambda} (x _ {i} | \lambda)
$$
dove $\Lambda$ è una variabile aleatoria con pdf esponenziale di parametro noto $\mu$ , cioè $f_{\Lambda}(\lambda) = \mu e^{-\lambda \mu} u(\lambda)$ . A partire da $x^n = (x_1, \ldots, x_n)$ si vuole ottenere una stima del parametro $\lambda$ . 
1. Si determini $\widehat{\Lambda}_{\mathrm{MAP}}(X^{n})$ , lo stimatore MAP del parametro aleatorio $\Lambda$ ; 
2. Si dica se lo stimatore è polarizzato e se è consistente; 
3. opzionale: Si ripetano i punti precedenti nel caso che λ sia un parametro deterministico non noto. 

###### 3 luglio 2026 - Tempo massimo: 2,5 ore 
1. Un bussolotto contiene due dadi, indistinguibili per colore e peso, di cui uno onesto, e uno truccato in modo che il 6 esca con probabilità pari a 7 volte quella di un qualunque altre risultato (gli altri risultati sono tra loro equiprobabili). L'esperimento consiste nell'ESTRARRE un dado e nel lanciarlo fino a quando non si ottiene un 5. Detto X il numero di lanci effettuati: 
a. Determinare alfabeto e pmf di X; 
b. Determinare la media statistica di X; 
c. Sapendo che X = 2, calcolare la probabilità che il dado estratto sia truccato. 
2. Siano $X \sim \mathcal{N}(0,1)$ e $Y \sim \mathcal{N}(2,4)$ due variabili aleatorie congiuntamente gaussiane con coefficiente di correlazione $\rho = \frac{1}{2}$ e si formi la variabile Z = 2X - Y. 
a. Determinare la pdf della variabile aleatoria Z; 
b. Volendo quantizzare a un bit Z secondo la legge 
$$
U = \left\{ \begin{array}{l l} - 1 & Z <   \eta \\ 1 & Z \geq \eta \end{array} \right.
$$
si determini pmf, media e varianza di U in funzione di η. 
c. Si determini per quale valore di η Z è uniforme. 
3. Una moneta viene lanciata n volte per stabilire se essa sia onesta o truccata in modo che la testa esca nel 70% dei casi. Si sa che a priori la moneta è onesta con probabilità del 30%. 
1. Si determini la regola di decisione a minima probabilità d'errore per stabilire se la moneta è onesta o truccata; 
2. Si calcoli la probabilità d'errore di tale regola, 
