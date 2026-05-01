# Appunti MSI — Metodi Statistici per l'Informazione

> [!info] **Info corso**
> **Docente:** Prof. Marco Lops · **CFU:** 6 · **Esame:** Scritto + colloquio rapido
> **Testi:** Conte *Fenomeni Aleatori* (teoria); Ross *Probability and Statistics for Engineers and Scientists* (statistica)



# Capitolo 3 — Elements of Probability

## 3.1 Introduction

### Perché la probabilità per informatici e ingegneri dell'informazione?

Il filo conduttore del corso è la parola **informazione**. Sia le telecomunicazioni che l'informatica trattano questo oggetto: le telecomunicazioni si occupano di trasferirla da un luogo a un altro (usando onde elettromagnetiche), mentre l'informatica si occupa di trasferirla nel tempo (memorizzazione, compressione dati, correzione degli errori).

**Osservazione fondamentale:** se non c'è incertezza su ciò che viene trasmesso, non c'è informazione.

> **Esempio:** Una sorgente binaria che trasmette sempre zero o sempre uno non trasporta alcuna informazione — non c'è incertezza a priori su cosa la sorgente trasmetterà, quindi non ha senso né trasmetterla né memorizzarla.

Intrinseco nel concetto di informazione c'è il concetto di **incertezza**. L'incertezza è intrinsecamente probabilistica: l'intero processo di trasferimento si traduce nel trasformare un'**incertezza a priori** in una **certezza a posteriori**. Da questo deriva che tutto ciò che oggi si chiama *machine learning*, *statistical learning*, *deep learning* e reti neurali è costruito su questa base probabilistica.

> [!tip] **Parole del Professore**
> "Se vi parlano di statistica dicendo che è un'altra cosa rispetto alla probabilità, vuol dire che non conoscono la probabilità. La probabilità è la base con cui si costruisce tutto il mondo della statistica."

### Struttura e programma del corso

Il corso è organizzato in sei grandi blocchi tematici:

1. **Analisi combinatoria** — imparare a contare in modo efficace (§3.4)
2. **Teoria della probabilità su spazi finiti** — definizione assiomatica di Kolmogorov, variabili aleatorie discrete (§3.2–3.8, §4)
3. **Estensione al continuo** — PDF, CDF, integrali al posto di somme (§5)
4. **Processi aleatori** — cenni necessari per le applicazioni
5. **Informazione e sua misura** — entropia di Shannon, mutua informazione, il bit come unità di misura
6. **Statistica** — descrittiva e **inferenziale**; teoria della decisione; test di ipotesi; stima bayesiana e non bayesiana (§6–9)

> [!important] **Distinzione fondamentale nella statistica:**
> - **Descrittiva:** ho una popolazione e ne calcolo statistiche globali. Interessante, ma limitata.
> - **Inferenziale:** elaborando un campione, inferisco le caratteristiche di qualunque altro campione statisticamente omogeneo con esso. È la base di tutti gli algoritmi di *learning*: un buon algoritmo funziona su qualunque campione con certi parametri, non solo su quello di addestramento.
>
> La statistica inferenziale si divide in **bayesiana** (i parametri da stimare hanno una distribuzione a priori nota) e **non bayesiana** (questa informazione a priori non è disponibile).

> [!note] **Nota:** Esiste un'integrazione profonda tra teoria dell'informazione e statistica inferenziale, formalizzata dal risultato di Kaila (anni '69–'71, riscoperto negli anni 2000).



## 3.2 Sample Space and Relationships Between Events

> [!info] **Definizione: Esperimento**
> Un **esperimento** è un'operazione, o un insieme di operazioni, che conduce a uno tra tanti risultati possibili.

> [!info] **Definizione: Spazio dei campioni**
> Lo **spazio dei campioni** (*sample space*), indicato con $\Omega$, è l'insieme — non necessariamente numerico — di tutti i possibili risultati di un esperimento.

Lo spazio dei campioni può avere diverse nature:

| Tipo                          | Esempio                                                                    |
| ----------------------------- | -------------------------------------------------------------------------- |
| **Finito**                    | Lancio di una moneta: $\Omega = \{T, C\}$                                  |
| **Infinito numerabile**       | Numero di pacchetti in coda a un router: $\Omega = \mathbb{N}_0$           |
| **Continuo (non numerabile)** | Tensione ai capi di una resistenza (rumore termico): $\Omega = \mathbb{R}$ |

> [!note] **Sul continuo**
> Qualunque misura fisica è razionale (gli strumenti hanno un numero finito di cifre significative). Tuttavia, quando i valori possibili sono così numerosi, conviene modellarli come continui e poi applicare una troncatura numerica. Il tempo si schematizza quasi sempre come continuo.
>
> **Citazione del prof.:** *"Il discreto riempie la testa di idee, il continuo riempie la lavagna di formule. Ma se uno capisce bene le idee, le formule sono una conseguenza."*

**Esempi:**

- Lancio singolo di moneta: $\Omega = \{T, C\}$
- Lancio doppio di moneta: $\Omega = \{TT, TC, CT, CC\}$ — 4 elementi (l'ordine conta, è una sequenza temporale)
- Lancio di dado: $\Omega = \{1,2,3,4,5,6\}$, $|\Omega| = 6$
- Macchine su un'autostrada in un giorno (o pacchetti in coda a un router): $\Omega = \mathbb{N}_0 = \{0,1,2,\ldots\}$

### Definizione di Evento

> [!info] **Definizione: Evento**
> Un **evento** è un sottoinsieme di $\Omega$ definito da una proposizione.

> [!info] **Definizione: Evento elementare**
> Un **evento elementare** è un singolo elemento di $\Omega$.

**Proprietà cruciale:** Un evento è **univocamente determinato** dagli elementi di $\Omega$ che lo compongono, ma la **proposizione** che lo descrive **non è univoca** — la ridondanza del linguaggio naturale permette formulazioni diverse.

> [!example] **Esempio: ambiguità della proposizione**
> Con $\Omega = \{1,2,3,4,5\}$ (euro in tasca), l'evento $A = \{1,3,5\}$ può essere descritto come: "Ho un numero dispari di euro", oppure "Non ho un numero pari di euro", oppure "Ho 1, 3 o 5 euro". L'evento è lo stesso, le proposizioni sono diverse.

> [!tip] **Parole del Professore**
> Risolvere un esercizio di probabilità su spazi discreti richiede spesso un unico vero sforzo: **riformulare la proposizione** che definisce l'evento in modo che la soluzione appaia chiara. Esempio classico: "Qual è la probabilità che due persone in una classe di 30 abbiano lo stesso compleanno?" — la chiave è lavorare sull'evento complementare.

### Nomenclatura degli eventi

| Nome                     | Simbolo                | Significato                                         |
| ------------------------ | ---------------------- | --------------------------------------------------- |
| **Evento certo**         | $\Omega$               | Si verifica sempre ad ogni esito                    |---
| **Evento impossibile**   | $\emptyset$            | Non si verifica mai                                 |
| **Evento complementare** | $A^c$ o $\bar{A}$      | Tutti gli $\omega \in \Omega$ con $\omega \notin A$ |
| **Evento implicato**     | $A \subseteq B$        | Il verificarsi di $A$ implica $B$, non viceversa    |
| **Eventi incompatibili** | $A \cap B = \emptyset$ | Non possono verificarsi contemporaneamente          |

**Esempi su lancio di dado:**
- "Esce 2" $= \{2\}$ implica "esce un numero pari" $= \{2,4,6\}$, ma non viceversa.

**Esempi su lancio doppio di moneta ($\Omega = \{TT, TC, CT, CC\}$):**
- "Esce almeno una croce" $D = \{TC, CT, CC\}$
- $D$ è **incompatibile** con $\{TT\}$ (esce testa-testa → nessuna croce)

**Esempi con $\Omega = \mathbb{N}_0$ (pacchetti):**
- "Meno di 6 pacchetti": $\{0,1,2,3,4,5\}$
- "Numero dispari di pacchetti": $\{1,3,5,7,\ldots\} = \{2k+1 \mid k \in \mathbb{N}_0\}$ — unione **numerabile** di eventi elementari
- "Numero pari **o** minore di 4": $\{0,1,2,3,4,6,8,\ldots\}$ — include 1 e 3 (dispari ma $< 4$) e 4 (pari e $\leq 4$)

### Algebra degli eventi — Richiami di teoria degli insiemi

Dati $m$ sottoinsiemi $A_1, A_2, \ldots, A_m$ di $\Omega$:

**Unione:** $A_1 \cup A_2$ — tutti gli elementi che appartengono ad almeno uno dei due insiemi (comuni contati una sola volta).

**Intersezione:** $A_1 \cap A_2$ — tutti e soli gli elementi comuni ad entrambi.

**Complemento:** $A_1^c$ — tutti gli elementi di $\Omega$ non in $A_1$.

**Sottrazione:** $A_1 \setminus A_2 = A_1 \cap A_2^c$ — gli elementi di $A_1$ che non appartengono ad $A_2$.

| Proprietà                | Formula                       |
| ------------------------ | ----------------------------- |
| Doppio complemento       | $(A^c)^c = A$                 |
| Complemento di $\Omega$  | $\Omega^c = \emptyset$        |
| Unione con complementare | $A \cup A^c = \Omega$         |
| De Morgan (unione)       | $(A \cup B)^c = A^c \cap B^c$ |
| De Morgan (intersezione) | $(A \cap B)^c = A^c \cup B^c$ |

> [!note] **$\sigma$-algebra**
> Quando $\Omega$ è infinito numerabile, la famiglia degli eventi deve essere una **$\sigma$-algebra**: chiusa non solo rispetto a unioni **finite**, ma rispetto a unioni **numerabili**. Questo è necessario per modellare eventi come $\{k \mid k \text{ dispari}\}$, che sono unioni infinite di eventi elementari.



## 3.3 Probability

> [!info] **Definizione: Legge di probabilità (Assiomi di Kolmogorov)**
> Dato uno spazio dei campioni $\Omega$ e una $\sigma$-algebra $\mathcal{E}$, si definisce **legge di probabilità** una funzione $P : \mathcal{E} \to [0,1]$ che soddisfi i tre assiomi di Kolmogorov:
> 1. **Non negatività:** $P(A) \geq 0$ per ogni $A \in \mathcal{E}$
> 2. **Normalizzazione:** $P(\Omega) = 1$
> 3. **Additività:** se $A \cap B = \emptyset$, allora $P(A \cup B) = P(A) + P(B)$
>
> Il quarto assioma estende l'additività a unioni **numerabili** di eventi disgiunti (necessario per la $\sigma$-algebra).

La terna $(\Omega, \mathcal{E}, P)$ si chiama **spazio di probabilità**. La struttura della $\sigma$-algebra garantisce che si rimanga sempre nel dominio di definizione di $P$.

### Proprietà derivate dagli assiomi

Tutte le proprietà seguenti si *dimostrano* dagli assiomi, non si assumono:

**Probabilità del vuoto:** $P(\emptyset) = 0$. Dimostrazione: $\Omega = \Omega \cup \emptyset$ con $\Omega \cap \emptyset = \emptyset$, quindi $P(\Omega) = P(\Omega) + P(\emptyset)$, da cui $P(\emptyset) = 0$.

**Probabilità del complementare:**
$$P(A^c) = 1 - P(A)$$

**Probabilità della differenza:**
$$P(A \setminus B) = P(A) - P(A \cap B)$$

Dimostrazione: $A = (A \cap B) \cup (A \cap B^c)$ con i due insiemi disgiunti, quindi $P(A) = P(A \cap B) + P(A \cap B^c)$.

**Formula generale dell'unione (subadditività):**
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

La probabilità è una **misura** nel senso matematico: la misura di un'unione non è la somma semplice se i due insiemi si intersecano. Questo vale per qualunque misura (geometrica, di probabilità, ecc.).

> [!tip] **Parole del Professore**
> L'approccio frequentistico — definire $P(A) = \lim_{n\to\infty} N_A/n$ — è intuitivo ma circolare: per garantire la convergenza si deve già assumere l'indipendenza delle prove, che è anch'essa un concetto probabilistico. Si usa quindi la definizione assiomatica di Kolmogorov, che è rigorosa e non circolare. Tuttavia, l'intuizione frequentistica rimane preziosa per capire *perché* le proprietà della probabilità valgono: ogni proprietà corrisponde a una proprietà delle operazioni tra insiemi.



## 3.4 Sample Spaces Having Equally Likely Outcomes

Quando $\Omega$ è finito e tutti gli eventi elementari sono **equiprobabili**, la probabilità di un evento si calcola come:

$$\boxed{P(A) = \frac{|A|}{|\Omega|}}$$

Questo riduce\ il problema a un conteggio combinatorio.

> [!warning]
> Questa formula è valida **solo** se gli eventi elementari sono equiprobabili. Se il dado è truccato, contare i casi favorevoli su quelli possibili non funziona.

### Analisi Combinatoria

#### Principio del prodotto cartesiano (regola fondamentale)

> [!abstract] **Teorema: Cardinalità del prodotto cartesiano**
> Dati $k$ insiemi finiti $A_1, A_2, \ldots, A_k$ con cardinalità $|A_i| = n_i$, la cardinalità del prodotto cartesiano è:
> $$|A_1 \times A_2 \times \cdots \times A_k| = \prod_{i=1}^{k} n_i$$

**Giustificazione:** Il primo elemento si sceglie in $n_1$ modi, il secondo in $n_2$ modi **indipendentemente**, …, il $k$-esimo in $n_k$ modi.

> **Attenzione:** Le $k$-uple sono **ordinate** — $(0,1) \neq (1,0)$.

**Esempio:** $\{0,1\} \times \{0,1\} = \{(0,0),(0,1),(1,0),(1,1)\}$ — $2 \times 2 = 4$ elementi.

#### Tabella riassuntiva

| Tipo di selezione                                  | Formula                                  | Nome                            |
| -------------------------------------------------- | ---------------------------------------- | ------------------------------- |
| $k$-uple ordinate **con** ripetizione da $n$       | $n^k$                                    | —                               |
| $k$-uple ordinate **senza** ripetizione da $n$     | $\dfrac{n!}{(n-k)!}$                     | Disposizioni semplici           |
| $n$-uple ordinate **senza** ripetizione da $n$     | $n!$                                     | Permutazioni                    |
| $k$-uple **non ordinate** senza ripetizione da $n$ | $\dbinom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$ | Combinazioni (coeff. binomiale) |

#### Derivazione delle formule

**$k$-uple ordinate con ripetizione:** Ogni posizione si riempie in $n$ modi indipendentemente:
$$\underbrace{\enspace n \times n \times \cdots \times n}_{k} = n^k$$
*Esempio:* le sequenze binarie di lunghezza $k$ sono $2^k$.

**$k$-uple ordinate senza ripetizione:** Ogni volta che si pesca un elemento lo si rimuove:
$$n \times (n-1) \times (n-2) \times \cdots \times (n-k+1) = \frac{n!}{(n-k)!}$$

**Permutazioni** (caso $k = n$):
$$P(n) = n! = n(n-1)(n-2)\cdots 1$$

**Combinazioni:** Le $k$-uple **non ordinate** (dove $\{1,2,3\} = \{3,2,1\}$). Tra tutte le $\frac{n!}{(n-k)!}$ disposizioni semplici, ogni gruppo di $k!$ (tutte le permutazioni degli stessi $k$ elementi) corrisponde alla **stessa** combinazione:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

Questo risultato è fondamentale in teoria dell'informazione.

**Coefficiente multinomiale:** una sequenza di lunghezza $n$ su un alfabeto $m$-ario con $n_i$ occorrenze del simbolo $i$ (e $\sum n_i = n$) può essere formata in:

$$\binom{n}{n_1, n_2, \ldots, n_m} = \frac{n!}{n_1!\, n_2! \cdots n_m!}$$

modi distinti.

> [!info] **Teorema: Cardinalità dell'insieme delle parti**
> Dato un insieme $A$ con $m$ elementi, l'insieme delle parti $\mathcal{P}(A)$ ha cardinalità:
> $$|\mathcal{P}(A)| = 2^m$$

*Dimostrazione:* I sottoinsiemi di $A$ con esattamente $k$ elementi sono $\binom{m}{k}$. Sommando su $k = 0, 1, \ldots, m$ e applicando il binomio di Newton con $a=b=1$:

$$|\mathcal{P}(A)| = \sum_{k=0}^{m} \binom{m}{k} = (1+1)^m = 2^m \qquad \square$$

> [!example] **Esercizio: probabilità nel poker (mazzo francese da 52)**
> **Colore** (5 carte dello stesso seme):
> $$P(\text{colore}) = \frac{4\binom{13}{5}}{\binom{52}{5}}$$
> 
> **Colore nel mazzo napoletano da 32:** $|\Omega| = \binom{32}{5} = 201{.}376$. Con 8 carte per seme:
> $$P(\text{colore di picche}) = \frac{\binom{8}{5}}{\binom{32}{5}} = \frac{56}{201{.}376} \approx 0{,}00028$$
> $$P(\text{colore qualsiasi}) = \frac{4 \cdot \binom{8}{5}}{\binom{32}{5}} \approx 0{,}00111$$

> [!example] **Esercizio: sequenze binarie**
> Qual è la probabilità che due persone in una classe di 30 abbiano lo stesso compleanno?
>
> Si lavora sull'evento complementare: "tutti i 30 compleanni sono distinti".
> $$P(\text{tutti distinti}) = \frac{365 \cdot 364 \cdot 363 \cdots 336}{365^{30}} = \frac{\prod_{k=0}^{29}(365-k)}{365^{30}}$$
> $$P(\text{almeno una coincidenza}) = 1 - P(\text{tutti distinti}) \approx 0{,}706$$
>
> Più del 70%! La chiave è ragionare sul complementare.

> [!tip] **Parole del Professore**
> Regola fissa: quando vi chiedono "almeno uno", ragionate sempre sull'evento complementare ("nessuno"), perché è quasi sempre più semplice da calcolare.



## 3.5 Conditional Probability

L'intuizione della probabilità condizionata si comprende con il **database**: se ho un database di tutti i residenti in Italia con altezza e peso, la probabilità che una persona pesi almeno 70 kg si calcola su tutto il database. La probabilità *condizionata* che pesi almeno 70 kg **dato che è alta almeno 170 cm** si calcola eliminando dal database tutte le persone sotto 170 cm e ricalcolando la probabilità sul database ridotto.

> [!info] **Definizione: Probabilità condizionata**
> Dati due eventi $A, B$ con $P(B) > 0$, la **probabilità condizionata** di $A$ dato $B$ è:
> $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Il condizionamento cambia lo spazio di riferimento: da $\Omega$ si passa a $B$ come nuovo universo. Si verifica facilmente che $P(\cdot \mid B)$, con $B$ fisso, soddisfa tutti e tre gli assiomi di Kolmogorov, quindi è essa stessa una legge di probabilità valida.

Dalla definizione si ricava la **legge della probabilità composta**:

$$P(A \cap B) = P(B) \cdot P(A \mid B) = P(A) \cdot P(B \mid A)$$

**PMF condizionale:** data una condizione $C$ con $P(C) > 0$, la PMF condizionale di una variabile aleatoria $X$ è:

$$p_{X \mid C}(k) = \frac{P(X = k,\, C)}{P(C)}$$

Per $k$ incompatibili con $C$ questa probabilità è zero; per i $k$ compatibili, la PMF viene rinormalizzata dividendo per $P(C)$.



## 3.6 Bayes' Formula

Dalla simmetria della probabilità composta ($P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$) si ricava la **legge di Bayes**:

$$\boxed{P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}}$$

Questa formula permette di **invertire il condizionamento**: se conosco $P(A \mid B)$ e $P(B)$, posso calcolare $P(B \mid A)$. È lo strumento fondamentale dell'inferenza statistica bayesiana: aggiorna la conoscenza a priori $P(B)$ alla luce dell'evidenza osservata (evento $A$), ottenendo la probabilità a posteriori $P(B \mid A)$.

Quando si lavora con una **partizione** $\{E_1, E_2, \ldots, E_m\}$ di $\Omega$, la legge di Bayes combinata con la probabilità totale diventa:

$$P(E_i \mid A) = \frac{P(A \mid E_i) \cdot P(E_i)}{\sum_{j=1}^{m} P(A \mid E_j) \cdot P(E_j)}$$

> [!example] **Esercizio: dado onesto e dado truccato**
> Un bussolotto contiene un dado onesto $O$ e un dado truccato $T$ (il 6 esce con $P=1/2$, gli altri con $P=1/10$ ciascuno). Si estrae un dado a caso e si lanciano due volte, ottenendo la coppia $(5,5)$. Qual è la probabilità che il dado sia truccato?
>
> - $P(T) = P(O) = 1/2$ (estrazione equiprobabile)
> - $P(5,5 \mid T) = (1/10)^2 = 1/100$
> - $P(5,5 \mid O) = (1/6)^2 = 1/36$
> - $P(5,5) = \frac{1}{2} \cdot \frac{1}{100} + \frac{1}{2} \cdot \frac{1}{36} = \frac{1}{200} + \frac{1}{72} = \frac{36+100}{7200} = \frac{136}{7200} = \frac{17}{900}$
> - $P(T \mid 5,5) = \dfrac{\frac{1}{200}}{\frac{17}{900}} = \frac{900}{200 \cdot 17} = \frac{9}{34} \approx 0{,}265$
>
> La probabilità che il dado sia truccato è scesa dal 50% al 26,5%. Il 5 esce più facilmente con il dado onesto (1/6) che con il truccato (1/10), quindi osservare due 5 è evidenza a favore del dado onesto.



## 3.7 Independent Events

> [!info] **Definizione: Indipendenza statistica**
> Due eventi $A$ e $B$ si dicono **statisticamente indipendenti** se e solo se:
> $$P(A \cap B) = P(A) \cdot P(B)$$
> Equivalentemente (se $P(B) > 0$): $P(A \mid B) = P(A)$ — il verificarsi di $B$ non fornisce alcuna informazione su $A$.

L'indipendenza è un concetto fondamentale: tutta la statistica inferenziale si fonda su ipotesi di indipendenza (o almeno di ergodicità). Se i campioni non sono indipendenti, le stime non sono generalizzabili.

Se $A$ e $B$ sono indipendenti, anche $A^c$ e $B^c$ lo sono. Dimostrazione via De Morgan:

$$P(A^c \cap B^c) = P((A \cup B)^c) = 1 - P(A) - P(B) + P(A)P(B) = (1-P(A))(1-P(B)) = P(A^c)P(B^c)$$

Per **tre eventi** $A, B, C$, l'indipendenza richiede sia l'indipendenza a coppie sia quella congiunta:

$$P(A \cap B) = P(A)P(B), \quad P(A \cap C) = P(A)P(C), \quad P(B \cap C) = P(B)P(C)$$
$$P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$$

> [!warning]
> L'indipendenza a coppie **non implica** l'indipendenza congiunta. Controesempio classico: il **bit di parità**. Siano $X_1, X_2$ bit equiprobabili e indipendenti, e $X_3 = X_1 \oplus X_2$ (XOR). Ogni coppia tra $X_1, X_2, X_3$ è indipendente, ma la terna non lo è: conoscere $X_1$ e $X_2$ determina completamente $X_3$.

Per $n$ eventi indipendenti $A_1, \ldots, A_n$ con $P(A_i) = p_i$:

$$P\!\left(\bigcap_{i=1}^n A_i^c\right) = \prod_{i=1}^n (1 - p_i) \qquad \text{(nessuno si verifica)}$$

$$P\!\left(\bigcup_{i=1}^n A_i\right) = 1 - \prod_{i=1}^n (1 - p_i) \qquad \text{(almeno uno si verifica)}$$

> [!example] **Esercizio: almeno un 6 in 5 lanci**
> $$P(\text{almeno un 6}) = 1 - P(\text{nessun 6}) = 1 - \left(\frac{5}{6}\right)^5 \approx 0{,}598$$



## 3.8 Law of Total Probability

Sia $\{E_1, E_2, \ldots, E_m\}$ una **partizione** di $\Omega$ (eventi a due a due disgiunti la cui unione è $\Omega$). Per qualunque evento $A$:

$$\boxed{P(A) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)}$$

*Dimostrazione:* $A = A \cap \Omega = A \cap \bigl(\bigcup_i E_i\bigr) = \bigcup_i (A \cap E_i)$. Gli insiemi $A \cap E_i$ sono disgiunti, quindi per additività:

$$P(A) = \sum_{i=1}^m P(A \cap E_i) = \sum_{i=1}^m P(A \mid E_i) \cdot P(E_i)$$

Questa legge è fondamentale: permette di scomporre il calcolo di una probabilità difficile condizionando rispetto a una partizione che semplifica il problema.


# Capitolo 4 — Random Variables and Expectation

## 4.1 Random Variables

Molti esperimenti fisicamente diversi hanno la stessa struttura probabilistica. Il lancio di una moneta, la lettura di un bit da una sorgente binaria e la parità del lancio di un dado producono tutti un esito binario. Il concetto di **variabile aleatoria** permette di trattare tutti questi esperimenti in modo unificato, lavorando su un alfabeto numerico anziché su spazi campionari eterogenei.

> [!info] **Definizione: Variabile Aleatoria**
> Dato uno spazio di probabilità $(\Omega, \mathcal{E}, P)$, una **variabile aleatoria** $X$ è un'applicazione misurabile:
> $$X : \Omega \to \mathcal{X}$$
> dove $\mathcal{X}$ è l'**alfabeto** della variabile. La misurabilità garantisce che per ogni $x \in \mathcal{X}$, l'insieme $\{\omega : X(\omega) = x\}$ appartenga a $\mathcal{E}$, e quindi si possa calcolare la sua probabilità.

La variabile aleatoria *trasporta* la legge di probabilità da $\Omega$ all'alfabeto:
$$P(X = x) = P\bigl(\{\omega \in \Omega : X(\omega) = x\}\bigr)$$

> [!tip] **Parole del Professore**
> Perché sono utili le variabili aleatorie? Perché io posso trattare in un unico modo esperimenti completamente diversi. Il lancio di una moneta, la lettura di un bit, la parità di un dado — tutti esperimenti binari — diventano la stessa variabile aleatoria. In informatica, qualunque insieme discreto (stringhe, pacchetti, simboli di un alfabeto) si può indicizzare con numeri interi: la variabile aleatoria è il puntatore alla locazione di memoria che memorizza il valore corrispondente. Quindi si può sempre farlo.


## 4.2 Discrete Random Variables

Una variabile aleatoria si dice **discreta** se il suo alfabeto $\mathcal{X}$ è finito o infinito numerabile.

> [!info] **Definizione: PMF (Probability Mass Function)**
> La **funzione di massa di probabilità** di $X$ con alfabeto $\mathcal{X} = \{x_1, x_2, \ldots, x_m\}$ è la sequenza:
> $$p_X(x_i) = P(X = x_i), \quad i = 1, \ldots, m$$
> Una sequenza è una PMF valida se e solo se:
> $$p_X(x_i) \geq 0 \;\;\forall i \qquad \text{e} \qquad \sum_{i=1}^{m} p_X(x_i) = 1$$

> [!info] **Definizione: PMF Condizionale**
> Data una condizione $C$ con $P(C) > 0$, la **PMF condizionale** di $X$ dato $C$ è:
> $$p_{X \mid C}(k) = P(X = k \mid C) = \frac{P(X = k,\; C)}{P(C)}$$
> Per i valori $k$ incompatibili con $C$ questa è zero; per i valori compatibili, la PMF originale viene rinormalizzata dividendo per $P(C)$. Si verifica che $p_{X|C}$ è essa stessa una PMF valida (la probabilità condizionale soddisfa gli assiomi di Kolmogorov).

> [!example] **Esempio: PMF condizionale di una Binomiale**
> Sia $X \sim \text{Bin}(16, 1/3)$. La PMF condizionale "dato $X > 4$" è:
> $$p_{X \mid X>4}(k) = \begin{cases} \dfrac{p_X(k)}{P(X > 4)} & k = 5, 6, \ldots, 16 \\ 0 & k \leq 4 \end{cases}$$
> Questo corrisponde a potare i dati, tenendo solo gli esperimenti con almeno 5 successi — la PMF si ridistribuisce su un alfabeto ristretto. Questo è il fondamento della *outlier removal* in analisi dei dati.


## 4.3 Expected Value

L'intuizione è immediata: se misuri $n$ volte una quantità e ne fai la media aritmetica, ottieni la *media campionaria*. Man mano che $n$ cresce, questa converge a un numero fisso — la media statistica, o valore atteso.

Formalmente: $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X(\omega_i) = \sum_{k} x_k \cdot \frac{n_k}{n}$, dove $n_k$ è il numero di volte in cui compare $x_k$. Per la legge dei grandi numeri, $n_k/n \to p_X(x_k)$.

> [!info] **Definizione: Valore Atteso (Expected Value)**
> $$E[X] = \mu_X = \sum_{x \in \mathcal{X}} x \cdot p_X(x)$$
> Il valore atteso è il **baricentro probabilistico** della distribuzione: la media ponderata dei valori assunti, pesata con le rispettive probabilità.

> [!abstract] **Proprietà: Linearità del valore atteso**
> Per qualunque costanti $a, b \in \mathbb{R}$:
> $$E[aX + b] = a\,E[X] + b$$
> Questa proprietà vale per *qualunque* legge di probabilità, discreta o continua.

**Media condizionale:** analogamente alla PMF condizionale, si definisce:
$$E[X \mid C] = \sum_{x \in \mathcal{X}} x \cdot p_{X \mid C}(x)$$

> [!abstract] **Teorema: Media per partizione**
> Data una partizione $\{E_1, E_2, \ldots, E_m\}$ di $\Omega$:
> $$E[X] = \sum_{i=1}^{m} P(E_i) \cdot E[X \mid E_i]$$
> È la versione "pesata" della legge di probabilità totale, applicata ai valori attesi.

> [!abstract] **Teorema della Media Condizionale (per coppie di variabili)**
> Il concetto si estende al calcolo del valore atteso di una qualunque funzione $g(X,Y)$. Invece di usare direttamente la PMF congiunta, si può calcolare prima l'aspettativa condizionale dato $Y=y$, e poi mediare il risultato rispetto a $Y$:
> $$E[g(X,Y)] = E_Y[\, E_{X|Y}[\,g(X,Y) \mid Y\,] \,]$$

> [!example] **Esercizio (Reductio ad unum): Pacchetti errati in un Router (Poisson Thinning)**
> Siano i pacchetti in coda a un router modellati da una variabile Poissoniana $N \sim \text{Poi}(\lambda)$. Supponiamo che ogni pacchetto sia "in errore" con probabilità $p$, in modo indipendente. Vogliamo calcolare la distribuzione del numero di pacchetti in errore $M$.
> 
> *Soluzione:* Conoscere direttamente $P(M=m)$ è difficile. Usiamo il condizionamento! Se *fissiamo* il numero totale di pacchetti $N=n$, il numero di pacchetti in errore $M$ diventa un semplice conteggio di successi (errori) su $n$ prove indipendenti. Dunque la distribuzione condizionale è Binomiale:
> $$P(M=m \mid N=n) = \binom{n}{m} p^m (1-p)^{n-m} \quad \text{per } m \leq n$$
> Ora applichiamo la probabilità totale (media rispetto a $N$):
> $$P(M=m) = \sum_{n=m}^{\infty} P(M=m \mid N=n) P(N=n) = \sum_{n=m}^{\infty} \binom{n}{m} p^m (1-p)^{n-m} \frac{\lambda^n}{n!} e^{-\lambda}$$
> Sviluppando i fattoriali e isolando i termini, si può porre $l = n-m$. Il risultato magico della serie di Taylor farà emergere che:
> $$P(M=m) = \frac{(\lambda p)^m}{m!} e^{-\lambda p}$$
> **Conclusione:** Il numero di pacchetti errati $M$ segue ancora una distribuzione Poissoniana, ma con parametro scalato $\lambda p$. Questa è una proprietà formidabile dei processi di Poisson, applicabile a innumerevoli scenari (es. auto italiane in un semaforo)!


## 4.4 Expectation of a Function of a Random Variable

Data $X$ e una funzione $g$, la variabile $Y = g(X)$ è anch'essa una variabile aleatoria (è una composizione di applicazioni). Per calcolarne la media, non serve prima ricavare la PMF di $Y$:

> [!info] **Teorema: LOTUS (Law Of The Unconscious Statistician)**
> Sia $Y = g(X)$. Allora:
> $$E[g(X)] = \sum_{x \in \mathcal{X}} g(x) \cdot p_X(x)$$

*Dimostrazione (caso non biiettivo):* Se più valori $\{x_{i_1}, \ldots, x_{i_\ell}\}$ collassano sullo stesso $y_j = g(x_{i_s})$ per ogni $s$, allora $p_Y(y_j) = \sum_s p_X(x_{i_s})$. Nella somma $\sum_x g(x) p_X(x)$, tutti questi termini hanno lo stesso valore $g(x_{i_s}) = y_j$, e le loro probabilità si sommano automaticamente a $p_Y(y_j)$. Il risultato finale è $\sum_j y_j p_Y(y_j) = E[Y]$. $\square$

> [!warning] **Disuguaglianza di Jensen**
> Se $g$ è convessa ($g'' \geq 0$): $E[g(X)] \geq g(E[X])$.
> Se $g$ è concava ($g'' \leq 0$): $E[g(X)] \leq g(E[X])$.
> Importante: in generale $E[g(X)] \neq g(E[X])$.

> [!example] **Esempio applicativo**
> $X$ ha alfabeto $\{-2,-1,1,2\}$ con PMF $\{1/8, 1/4, 1/4, 3/8\}$.
>
> *Caso $Y = 4X$:* $E[Y] = 4\,E[X]$ per linearità. L'alfabeto di $Y$ è $\{-8,-4,4,8\}$ con le stesse probabilità.
>
> *Caso $Y = |X|$:* L'alfabeto di $Y$ è $\{1,2\}$. In $Y=1$ collassano $X=-1$ e $X=1$: $p_Y(1) = 1/4 + 1/4 = 1/2$. In $Y=2$ collassano $X=-2$ e $X=2$: $p_Y(2) = 1/8 + 3/8 = 1/2$. Quindi $E[Y] = 1 \cdot 1/2 + 2 \cdot 1/2 = 3/2$.


## 4.5 Variance

La media da sola non basta a caratterizzare una variabile aleatoria. Se il professore ha mediamente 100€ in tasca con varianza di 1 centesimo, la media è informativa. Se la varianza è 30€, la situazione può essere molto diversa da giorno a giorno. La coppia $(\mu_X, \sigma_X)$ è molto più informativa del solo $\mu_X$.

> [!info] **Definizione: Varianza e Deviazione Standard**
> La **varianza** di $X$ è il valore quadratico medio dello scarto dalla media:
> $$\text{Var}(X) = \sigma_X^2 = E\!\left[(X - \mu_X)^2\right] = \sum_{x \in \mathcal{X}} (x - \mu_X)^2\, p_X(x)$$
> La **deviazione standard** è $\sigma_X = \sqrt{\text{Var}(X)}$.

> [!abstract] **Formula computazionale della varianza**
> $$\text{Var}(X) = E[X^2] - \bigl(E[X]\bigr)^2$$
> *Dimostrazione:* $E[(X-\mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu^2 + \mu^2 = E[X^2] - \mu^2$. $\square$

> [!info] **Definizione: Valore efficace (RMS)**
> Il **valore quadratico medio** è $E[X^2]$, indicato anche come $x^2_\text{rms}$.
> Il **valore efficace** è $x_\text{rms} = \sqrt{E[X^2]}$ (dalla sigla inglese *Root Mean Square*).

> [!tip] **Parole del Professore**
> Se il valore efficace di una presa elettrica è zero, puoi toccarla senza rischi — la presa è spenta. Ma se è zero solo il *valor medio* (come per la corrente alternata sinusoidale, il cui valor medio è sempre zero), ti folgoreresti. Il valore efficace della rete elettrica italiana è 230 V RMS. La varianza cattura l'**energia** del segnale, non la media. Ecco perché nel machine learning si minimizza il *quadrato* dell'errore: è una misura di energia, è convessa, e ammette un unico minimo globale.

> [!abstract] **Proprietà della varianza**
> $$\text{Var}(aX + b) = a^2\,\text{Var}(X)$$
> La traslazione $b$ non influenza la varianza (sposta la distribuzione senza allargarla); la scala $a$ la moltiplica per $a^2$.

Il rapporto $\mu_X / \sigma_X$ misura quanto $X$ è "poco aleatoria": se è grande, la distribuzione è concentrata intorno alla media e $\mu_X$ è un buon predittore. Se è piccolo, la distribuzione è molto dispersa.

### Covarianza e Correlazione (per coppie di variabili)

Per caratterizzare *parzialmente* come due variabili aleatorie variano insieme senza dover ricorrere all'intera PMF congiunta, si usano la covarianza e la correlazione.

> [!info] **Definizione: Covarianza**
> Date due variabili aleatorie $X$ e $Y$ con medie $\mu_X$ e $\mu_Y$, la covarianza è definita come:
> $$\text{Cov}(X,Y) = E[\,(X - \mu_X)(Y - \mu_Y)\,] = E[XY] - \mu_X\mu_Y$$
> - Se $\text{Cov}(X,Y) > 0$: deviazioni positive di $X$ si accompagnano spesso a deviazioni positive di $Y$.
> - Se $\text{Cov}(X,Y) < 0$: deviazioni positive di $X$ si accompagnano spesso a deviazioni negative di $Y$.

Se due variabili sono **indipendenti**, la media del prodotto fattorizza ($E[XY] = E[X]E[Y]$), quindi la loro covarianza è *zero* (sono scorrelate). **Attenzione:** Il viceversa in generale non vale! Variabili con covarianza nulla possono essere fortemente dipendenti (l'unico caso in cui l'assenza di correlazione implica indipendenza è nel mondo delle distribuzioni normali/gaussiane).

> [!info] **Definizione: Coefficiente di Correlazione**
> Per avere un indice adimensionale, la covarianza viene normalizzata rispetto alle deviazioni standard, definendo il coefficiente di correlazione:
> $$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$$

> [!abstract] **Proprietà di Cauchy-Schwarz e Correlazione**
> L'insieme delle variabili aleatorie con media quadratica finita forma uno spazio vettoriale in cui la covarianza funge da *prodotto scalare* e la deviazione standard da *norma*. Per la disuguaglianza di Cauchy-Schwarz:
> $$-1 \leq \rho_{X,Y} \leq 1$$
> L'uguaglianza $\rho_{X,Y} = \pm 1$ si ha se e solo se $X$ e $Y$ sono linearmente dipendenti (perfettamente proporzionali). Il coefficiente $\rho$ misura quindi la *prevedibilità lineare* di una variabile a partire dall'altra.

### Matrice di Covarianza

Se raccogliamo $n$ variabili aleatorie in un vettore colonna $\mathbf{X} = [X_1, X_2, \ldots, X_n]^T$, possiamo definire la **Matrice di Covarianza**:
$$\mathbf{C_X} = E[\,(\mathbf{X} - \boldsymbol{\mu_X})(\mathbf{X} - \boldsymbol{\mu_X})^T\,]$$
È una matrice quadrata $n \times n$ che ha:
- Sulla **diagonale principale**: le varianze delle singole variabili ($\sigma_i^2$).
- Sulla **diagonale secondaria (antidiagonale)**: le covarianze tra le coppie ($\text{Cov}(X_i, X_j)$).

La matrice di covarianza è sempre **definita non negativa**. Questa matrice è il punto di partenza per tecniche avanzate di machine learning, filtraggio predittivo e data analysis (es. l'analisi delle componenti principali (PCA) si basa proprio sugli autovalori/autovettori di questa matrice).


## 4.6 The Bernoulli and Binomial Random Variables

### Variabile di Bernoulli

La variabile di Bernoulli modella il risultato di un singolo esperimento binario (successo/insuccesso, 1/0, testa/croce).

> [!info] **Definizione: Variabile di Bernoulli**
> $X \sim \text{Ber}(p)$ se $\mathcal{X} = \{0, 1\}$ con:
> $$p_X(1) = p, \quad p_X(0) = 1 - p, \quad 0 \leq p \leq 1$$
> $$E[X] = p, \qquad \text{Var}(X) = p(1-p)$$

### Variabile Binomiale (Conteggio Bernulliano)

Conta il numero di successi in $n$ prove **indipendenti**, ognuna con probabilità di successo $p$. Il nome "binomiale" deriva dal binomio di Newton, che compare nella verifica della normalizzazione.

> [!info] **Definizione: Variabile Binomiale**
> $X \sim \text{Bin}(n, p)$ se $\mathcal{X} = \{0, 1, \ldots, n\}$ con:
> $$p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

> [!abstract] **Media e Varianza della Binomiale**
> $$E[X] = np, \qquad \text{Var}(X) = np(1-p)$$
> *Calcolo della media:* $E[X] = \sum_{k=1}^n k\binom{n}{k}p^k q^{n-k}$. Usando $k\binom{n}{k} = n\binom{n-1}{k-1}$ e la sostituzione $\ell = k-1$:
> $$E[X] = np \sum_{\ell=0}^{n-1}\binom{n-1}{\ell}p^\ell q^{n-1-\ell} = np(p+q)^{n-1} = np \qquad \square$$

*Verifica normalizzazione:* $\sum_{k=0}^n \binom{n}{k}p^k(1-p)^{n-k} = \bigl(p+(1-p)\bigr)^n = 1$ per il binomio di Newton. ✓

> [!tip] **Parole del Professore**
> L'intuizione non deve essere abbandonata: data una sorgente che emette 1 con probabilità $p$, in una stringa di $n$ bit mi aspetto mediamente $np$ uni. Non mi serve il calcolo formale. L'indipendenza è però cruciale: senza di essa non posso scrivere la probabilità di una stringa come prodotto delle probabilità dei singoli bit.

> [!example] **Esempi applicativi**
> - **Vaccini:** 10 bambini, efficacia 90%. $E[\text{immunizzati}] = 10 \cdot 0{,}9 = 9$. Probabilità che tutti e 10 siano immunizzati: $0{,}9^{10} \approx 0{,}349$.
> - **Compressione:** In 1000 bit con $p = 0{,}3$, mediamente $300$ uni. L'analisi combinatoria di quante sequenze hanno esattamente $k$ uni è la base dell'algoritmo di Huffman.
> - **Roulette:** 100 puntate al numero 7 ($p = 1/37$). Probabilità di esattamente 5 successi: $\binom{100}{5}(1/37)^5(36/37)^{95}$.


## 4.7 The Poisson Random Variable

La Poissoniana è la distribuzione più importante per modellare il **numero di arrivi** in un intervallo di tempo quando gli arrivi sono rari, casuali e indipendenti. È il modello fondamentale per la teoria delle code: code di pacchetti in un router, code di automobili a un semaforo, code agli sportelli.

> [!info] **Definizione: Variabile Poissoniana**
> $X \sim \text{Poisson}(\lambda)$ se $\mathcal{X} = \mathbb{N}_0 = \{0, 1, 2, \ldots\}$ con:
> $$p_X(k) = e^{-\lambda}\frac{\lambda^k}{k!}, \quad k = 0, 1, 2, \ldots, \quad \lambda > 0$$

> [!abstract] **Media e Varianza della Poissoniana**
> $$E[X] = \lambda, \qquad \text{Var}(X) = \lambda$$
> Il parametro $\lambda$ è sia la media sia la varianza.
>
> *Verifica normalizzazione:* $\sum_{k=0}^\infty e^{-\lambda}\frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^\lambda = 1$ (serie di Maclaurin di $e^\lambda$). ✓
>
> *Calcolo della media:* $E[X] = e^{-\lambda}\sum_{k=1}^\infty k\frac{\lambda^k}{k!} = e^{-\lambda}\lambda\sum_{\ell=0}^\infty\frac{\lambda^\ell}{\ell!} = \lambda e^{-\lambda}e^\lambda = \lambda$. $\square$

> [!abstract] **Poisson come limite della Binomiale**
> $\text{Bin}(n, p) \xrightarrow{n \to \infty,\; p \to 0,\; np = \lambda} \text{Poisson}(\lambda)$
>
> La Binomiale con $n$ grande e $p$ piccolo (eventi rari) converge alla Poissoniana. Questa è la giustificazione teorica del modello di Poisson per eventi rari in grandi popolazioni.

> [!tip] **Parole del Professore**
> "La Poissoniana non invecchia" — il numero di arrivi in un intervallo futuro è indipendente da quanti ne sono arrivati nel passato. Questa proprietà di *assenza di memoria* la rende il modello più semplice per le code, ma anche il più limitato: in un'ora di punta, $\lambda$ cambia (più macchine a mezzogiorno che a mezzanotte). Si modella allora con una Poisson non-stazionaria o con processi più complessi.

> [!example] **Esempio: semaforo urbano**
> Il numero di automobili in coda a un semaforo a mezzogiorno è modellato come $\text{Poisson}(\lambda = 40)$. Si vuole regolare il tempo del verde in modo che la coda non ecceda $K$ macchine con probabilità almeno $0{,}95$:
> $$P(X \leq K) = \sum_{k=0}^K e^{-40}\frac{40^k}{k!} \geq 0{,}95$$
> Si trova $K$ per via numerica e si dimensiona di conseguenza il ciclo semaforico.


## 4.8 Moment Generating Functions

**Non ancora trattato** nelle lezioni disponibili.


## 4.9 The Weak Law of Large Numbers

La legge dei grandi numeri formalizza l'intuizione fondamentale: su molti esperimenti, la media osservata converge alla media statistica.

> [!info] **Teorema: Legge Debole dei Grandi Numeri (WLLN)**
> Siano $X_1, X_2, \ldots, X_n$ variabili aleatorie **i.i.d.** (*independent and identically distributed*) con media $\mu$ e varianza $\sigma^2 < \infty$. Allora la media campionaria converge **in probabilità** a $\mu$:
> $$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{\;\;P\;\;} \mu$$
> ovvero: $\lim_{n \to \infty} P\!\left(|\bar{X}_n - \mu| > \varepsilon\right) = 0$ per ogni $\varepsilon > 0$.

> [!abstract] **Dimostrazione tramite Disuguaglianza di Chebyshev**
> Per qualunque variabile aleatoria $X$ con media $\mu$ e varianza $\sigma^2$:
> $$P(|X - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2}$$
> *Dimostrazione:* $\sigma^2 = E[(X-\mu)^2] \geq \varepsilon^2 \cdot P(|X-\mu| \geq \varepsilon)$ (spezzando la somma sulle regioni $|x-\mu| \geq \varepsilon$ e $|x-\mu| < \varepsilon$). $\square$
>
> Poiché $\bar{X}_n$ ha varianza $\sigma^2/n$:
> $$P(|\bar{X}_n - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{n\varepsilon^2} \xrightarrow{n \to \infty} 0 \qquad \square$$
>
> **Nota sulle Variabili Continue:** Le disuguaglianze di Markov ($P(X \geq \delta) \leq \frac{E[X^m]}{\delta^m}$) e Chebyshev valgono in modo assolutamente identico anche per le variabili continue. La dimostrazione sfrutta la stessa tecnica di maggiorazione applicata all'integrale (es. l'integrale su $[\delta, \infty)$ di $f_X(x)$ è maggiorato da quello di $\frac{x^m}{\delta^m} f_X(x)$).

> [!tip] **Parole del Professore**
> La WLLN è la base teorica di ZIP, gzip e tutti gli algoritmi di compressione universale. L'algoritmo di Lempel-Ziv (LZ77/LZ78), che è alla base di tutti i formati compressi che usate ogni giorno, è ottimale nel senso che raggiunge asintoticamente l'entropia della sorgente. La dimostrazione dell'ottimalità usa la legge *forte* dei grandi numeri (convergenza con probabilità 1, non solo in probabilità).



# Capitolo 5 — Special Random Variables

## 5.0 Introduzione alle Variabili Aleatorie Continue

Fino ad ora abbiamo studiato variabili discrete, in cui l'evento $X=x$ ha una probabilità ben definita e finita. Se consideriamo la misura della tensione ai capi di una resistenza (in presenza di rumore termico), lo spazio dei valori possibili è l'intero asse reale $\mathbb{R}$. 

Se la variabile è intrinsecamente continua, la probabilità di un *singolo punto esatto* (es. $X = 1.50000000\dots$) è rigorosamente **zero**. 
Analogamente alla massa in fisica: un singolo punto in una sbarra ha lunghezza nulla e quindi massa nulla, ma un segmento di lunghezza $\Delta x$ possiede una massa.

> [!tip] **Parola del Professore: La probabilità come misura**
> La lunghezza o il volume sono modi di misurare lo spazio (e una sbarra ha lunghezza ovunque). La massa è un altro modo di "pesare" lo spazio. **La probabilità è esattamente come la massa**: è un modo di "misurare" l'asse reale, pesando di più gli intervalli dove l'esito è più verosimile. 

> [!info] **Densità di Probabilità (PDF)**
> Si definisce la densità di probabilità (Probability Density Function) come la "concentrazione" di probabilità per unità di lunghezza:
> $$f_X(x) = \lim_{\Delta x \to 0} \frac{P\left(x - \frac{\Delta x}{2} < X \leq x + \frac{\Delta x}{2}\right)}{\Delta x}$$
> Ne consegue che la probabilità che $X$ cada in un intervallo $[a,b]$ è l'integrale della densità:
> $$P(a \leq X \leq b) = \int_a^b f_X(x) dx$$

> [!warning] **Attenzione: la PDF non è una probabilità!**
> Il valore della PDF $f_X(x)$ in un punto *non è* una probabilità! Può tranquillamente essere maggiore di 1. Non chiamatelo "il valore più probabile" se vi riferite al picco della campana, perché la probabilità di estrarre *esattamente* quel valore è zero! È corretto dire che la PDF ha il suo massimo in quel punto, indicando la zona di massima densità.

> [!info] **Funzione di Ripartizione (CDF - Cumulative Distribution Function)**
> La CDF è definita come $F_X(x) = P(X \leq x)$ ed è un concetto universale, valido sia per variabili discrete che continue. Le sue proprietà fondamentali sono:
> 1. $\lim_{x \to -\infty} F_X(x) = 0$ e $\lim_{x \to +\infty} F_X(x) = 1$
> 2. È una funzione **monotona non decrescente**.
> 3. Per variabili continue, è legata alla PDF dalla relazione integrale: $F_X(x) = \int_{-\infty}^x f_X(t)dt$, da cui deriva $f_X(x) = \frac{d}{dx}F_X(x)$.
> 4. Per variabili discrete, è una funzione a scalini con salti pari alle probabilità (PMF) dei singoli punti.

> [!tip] **Digitalizzazione e Quantizzazione**
> I calcolatori digitali richiedono di discretizzare le grandezze continue (es. conversione A/D). Il processo di **quantizzazione** mappa intervalli continui in un numero finito di valori discreti. Shannon (1948) ha dimostrato che è possibile rappresentare questo mondo continuo digitalmente. Matematicamente, il valore atteso di una variabile continua $E[X] = \int_{-\infty}^{+\infty} x f_X(x) dx$ può essere rigorosamente derivato come limite della media di una variabile quantizzata quando l'ampiezza dell'intervallo di quantizzazione $\Delta x \to 0$.

> [!abstract] **Densità Condizionata (PDF Condizionale)**
> Così come si condizionano gli eventi, si può restringere l'analisi di una PDF a un sotto-intervallo $A$. La PDF condizionata all'evento $A$ è definita ricalibrando l'area sul nuovo dominio:
> $$f_{X \mid A}(x) = \frac{d}{dx} P(X \leq x \mid X \in A) = \begin{cases} \frac{f_X(x)}{P(X \in A)} & \text{se } x \in A \\ 0 & \text{altrimenti} \end{cases}$$
> *Esempio:* Se analizzo i dati radar scartando l'eco inferiore a una soglia $x_0$, sto calcolando le probabilità rispetto a una nuova PDF troncata e rinormalizzata.

---

## 5.0-bis La Funzione Generatrice dei Momenti (MGF)

La **Moment Generating Function (MGF)** è un potente strumento analitico che permette di caratterizzare le variabili aleatorie aggirando complessi calcoli integrali, unificando di fatto il trattamento di variabili continue e discrete tramite l'operatore valore atteso.

> [!info] **Definizione: Funzione Generatrice dei Momenti**
> Sia $X$ una variabile aleatoria. La sua MGF, se esiste, è definita come il valore atteso dell'esponenziale:
> $$M_X(s) = E[e^{sX}] = \int_{-\infty}^{+\infty} e^{sx} f_X(x) dx \quad \text{(nel caso continuo)}$$
> $$M_X(s) = \sum_{x \in \mathcal{X}} e^{sx} p_X(x) \quad \text{(nel caso discreto)}$$
> *Proprietà di base:* Indipendentemente dalla distribuzione, $M_X(0) = E[e^0] = 1$.

> [!abstract] **Proprietà Generatrice**
> Espandendo in serie di Maclaurin $M_X(s)$ nell'intorno di $s=0$, si dimostra che la derivata $n$-esima della MGF calcolata in $s=0$ fornisce esattamente il **momento di ordine $n$** della variabile aleatoria:
> $$\left. \frac{d^n M_X(s)}{ds^n} \right|_{s=0} = E[X^n]$$
> Ad esempio, $M_X'(0) = E[X]$ (la media) e $M_X''(0) = E[X^2]$ (il valore quadratico medio).

> [!tip] **Somma di Variabili Indipendenti e Teorema Centrale del Limite (CLT)**
> Se $X$ e $Y$ sono variabili aleatorie **indipendenti**, la MGF della loro somma $Z = X+Y$ è il **prodotto** delle loro MGF:
> $$M_{X+Y}(s) = E[e^{s(X+Y)}] = E[e^{sX} e^{sY}] = M_X(s) M_Y(s)$$
> *Nota del professore:* Questa proprietà è fondamentale. Nel **Teorema Centrale del Limite**, la MGF di una somma normalizzata di un gran numero di variabili aleatorie identicamente distribuite e indipendenti tende asintoticamente sempre alla stessa MGF, indipendentemente dalla distribuzione originale. Questa MGF limite è proprio quella della distribuzione Gaussiana (Normale). Questo spiega il ruolo universale della Normale nella teoria degli errori.

---

## 5.1 The Normal Random Variable (Variabile Gaussiana)

La distribuzione **Normale** (o Gaussiana) modella fenomeni naturali che sono la somma di un grandissimo numero di piccole perturbazioni indipendenti.

> [!info] **Definizione: Gaussiana Standard**
> $X_0 \sim \mathcal{N}(0, 1)$ è una normale standard se ha media $\mu = 0$ e varianza $\sigma^2 = 1$. La sua PDF, simmetrica a campana, è:
> $$f_{X_0}(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}, \quad x \in \mathbb{R}$$
> L'integrale su tutto $\mathbb{R}$ fa $1$, e poiché la funzione è pari ($x \cdot f_{X_0}(x)$ è dispari), l'integrale della media fa 0.

> [!abstract] **Gaussiana Generale e Scalamento**
> Una normale generica $X \sim \mathcal{N}(\mu, \sigma^2)$ si ottiene riscalando e traslando la normale standard: $X = \sigma X_0 + \mu$. La sua PDF diventa una campana "spiazzata e riscalata":
> $$f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad x \in \mathbb{R}$$

> [!tip] **La Funzione Speciale Q(x) e la CDF**
> La CDF della normale, $F_X(x) = \int_{-\infty}^x f_X(t)dt$, non è calcolabile in forma chiusa (non ammette primitive elementari). Si ricorre pertanto alla **funzione Q(x)** (o Complementary CDF), definita per la normale standard come la probabilità di eccedere un valore $x$:
> $$Q(x) = P(X_0 > x) = \frac{1}{\sqrt{2\pi}} \int_x^{+\infty} e^{-\frac{t^2}{2}} dt$$
> *Proprietà:* $Q(-\infty)=1$, $Q(+\infty)=0$. La CDF della normale standard è $F_{X_0}(x) = 1 - Q(x)$.
> Per una normale generica $\mathcal{N}(\mu, \sigma^2)$, la CDF si valuta standardizzando la variabile:
> $$F_X(x) = P(X \leq x) = P\left( \frac{X-\mu}{\sigma} \leq \frac{x-\mu}{\sigma} \right) = 1 - Q\left(\frac{x - \mu}{\sigma}\right)$$

## 5.2 The Exponential Random Variable

La variabile esponenziale descrive il **tempo di attesa** tra eventi in un processo di Poisson. È la versione continua della variabile geometrica, e condivide con essa la fondamentale proprietà di **assenza di memoria**.

> [!info] **Definizione: Variabile Esponenziale**
> $X \sim \text{Exp}(\lambda)$ con $\lambda > 0$ se ha **densità di probabilità (PDF)**:
> $$f_X(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$
> e **funzione di ripartizione (CDF)**:
> $$F_X(x) = P(X \leq x) = 1 - e^{-\lambda x}, \quad x \geq 0$$

> [!abstract] **Media e Varianza dell'Esponenziale**
> $$E[X] = \frac{1}{\lambda}, \qquad \text{Var}(X) = \frac{1}{\lambda^2}$$
> Il parametro $\lambda$ è il *tasso* (numero medio di eventi per unità di tempo); il tempo medio tra eventi è $1/\lambda$.
> 
> *Calcolo della media:* $E[X] = \int_0^\infty x \lambda e^{-\lambda x} dx$. Sfruttando l'integrale notevole basato sulla funzione Gamma di Eulero, $\int_0^\infty x^n e^{-ax} dx = \frac{n!}{a^{n+1}}$, con $n=1$ e $a=\lambda$, si ottiene immediatamente $E[X] = \lambda \frac{1!}{\lambda^2} = \frac{1}{\lambda}$.

> [!abstract] **Proprietà di assenza di memoria**
> $$P(X > s + t \mid X > s) = P(X > t) \quad \forall s, t \geq 0$$
> Il tempo residuo ha la stessa distribuzione del tempo originale, indipendentemente da quanto si è già aspettato. L'esponenziale è l'**unica** distribuzione continua con questa proprietà.
>
> *Dimostrazione:*
> $$P(X > s+t \mid X > s) = \frac{P(X > s+t)}{P(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t) \qquad \square$$


## 5.3 The Hypergeometric Random Variable

**Non ancora trattato** nelle lezioni disponibili.


## 5.4 The Discrete Uniform Random Variable

> [!info] **Definizione: Variabile Uniforme Discreta**
> $X$ è **uniforme** su $\mathcal{X} = \{x_1, x_2, \ldots, x_m\}$ se:
> $$p_X(x_i) = \frac{1}{m} \quad \forall i = 1, \ldots, m$$
> Tutti i valori dell'alfabeto sono equiprobabili.

> [!abstract] **Media della Variabile Uniforme Discreta**
> $$E[X] = \frac{1}{m}\sum_{i=1}^m x_i \quad \text{(media aritmetica dei valori)}$$
> Per $\mathcal{X} = \{1, 2, \ldots, m\}$: $E[X] = \dfrac{m+1}{2}$ (usando $\sum_{i=1}^m i = m(m+1)/2$, formula di Gauss).


## 5.5 The Poisson Process

**Non ancora trattato** nelle lezioni disponibili.


## 5.6 The Uniform Random Variable

> [!info] **Definizione: Variabile Uniforme Continua**
> $X \sim \text{Unif}(a, b)$ se ha PDF:
> $$f_X(x) = \frac{1}{b - a}, \quad a \leq x \leq b$$
> e CDF: $F_X(x) = \dfrac{x-a}{b-a}$ per $a \leq x \leq b$.
> *Graficamente:* La PDF è un rettangolo di area 1. La CDF è una rampa lineare che parte da 0 in $a$ e arriva a 1 in $b$.

> [!abstract] **Media e Varianza dell'Uniforme Continua**
> $$E[X] = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{(b-a)^2}{12}$$

## 5.6-bis La Variabile di Laplace *(aggiunta del professore)*

> [!info] **Definizione: Variabile Laplaciana**
> $X \sim \text{Laplace}(\lambda)$ ha il supporto su tutto $\mathbb{R}$ e PDF simmetrica (a forma di "vela"):
> $$f_X(x) = \frac{\lambda}{2} e^{-\lambda |x|}, \quad x \in \mathbb{R}$$

> [!abstract] **CDF della Laplace**
> Poiché il modulo ha comportamento diverso per $x<0$ e $x>0$, l'integrale si spezza:
> $$F_X(x) = \begin{cases} \frac{1}{2} e^{\lambda x} & \text{se } x \leq 0 \\ 1 - \frac{1}{2} e^{-\lambda x} & \text{se } x > 0 \end{cases}$$
> *Graficamente:* La CDF ha un andamento *sigmoidale*, tipico delle variabili che spaziano su tutto l'asse reale (curva a "S", concava per $x>0$ e convessa per $x<0$).
>
> *Calcolo della media:* Essendo $x f_X(x)$ il prodotto tra una funzione dispari ($x$) e una pari (PDF del modulo), il risultato è una funzione dispari. Integrata su un intervallo simmetrico $(-\infty, +\infty)$, l'integrale è nullo: $E[X] = 0$.


## 5.7 Trasformazioni di Variabili Continue ($Y = g(X)$)

Data una variabile aleatoria continua $X$ con PDF $f_X(x)$ e una funzione $Y = g(X)$ continua e derivabile, vogliamo trovare la PDF di $Y$, $f_Y(y)$.

> [!tip] **Regola d'oro: Passare dalla CDF**
> Il metodo più robusto per trovare la PDF di una trasformazione è ricavare prima la CDF $F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$, risolvere la disequazione rispetto a $X$, e poi derivare il risultato per ottenere la PDF.

> [!abstract] **Teorema Fondamentale delle Trasformazioni**
> Se la funzione $g(x)$ è **strettamente monotona** (crescente o decrescente) ed è derivabile, allora ammette un'inversa $g^{-1}(y)$. La PDF della variabile trasformata $Y$ è:
> $$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right| = \frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}$$
> Il valore assoluto gestisce correttamente il caso in cui la funzione sia decrescente (preservando la positività della densità).

> [!abstract] **Generalizzazione (Funzioni non monotone)**
> Se l'equazione $y = g(x)$ ammette $m$ soluzioni $x_1, x_2, \ldots, x_m$, allora i contributi di probabilità si sommano:
> $$f_Y(y) = \sum_{i=1}^{m} \frac{f_X(x_i)}{|g'(x_i)|}$$

> [!example] **Esercizio: Valore Quadratico Medio**
> Nel caso di trasformazioni continue, la media di una funzione $g(X)$ si generalizza tramite l'integrale:
> $$E[g(X)] = \int_{-\infty}^{+\infty} g(x) f_X(x) dx$$
> Questo permette di calcolare rapidamente il **Valore Quadratico Medio** $E[X^2] = x_{rms}^2$. Per un'Esponenziale, l'integrale $\int_0^\infty x^2 \lambda e^{-\lambda x} dx$ (sfruttando le proprietà della Gamma) vale $\frac{2}{\lambda^2}$. Di conseguenza la varianza è $\frac{2}{\lambda^2} - (\frac{1}{\lambda})^2 = \frac{1}{\lambda^2}$.

## 5.8 Generazione di Variabili Aleatorie (Inverse Transform Sampling)

Come si simula al calcolatore una variabile con una distribuzione arbitraria? I calcolatori (es. `rand()` in C o MATLAB) generano variabili *uniformi* in $[0,1]$.

> [!info] **Il Metodo dell'Inversa della CDF**
> Sia $U \sim \text{Unif}(0,1)$ la variabile generata dal computer. Vogliamo generare una variabile $X$ avente una specifica CDF $F_X(x)$.
> Se definiamo la trasformazione $X = F_X^{-1}(U)$, allora $X$ avrà esattamente la distribuzione $F_X(x)$ desiderata.
> 
> *Dimostrazione:* $P(X \leq x) = P(F_X^{-1}(U) \leq x)$. Siccome $F_X$ è monotona crescente, applicandola a entrambi i membri otteniamo $P(U \leq F_X(x))$. Ma la CDF di un'uniforme in $(0,1)$ è l'argomento stesso! Quindi $P(U \leq F_X(x)) = F_X(x)$. $\square$

## 5.8-bis Legge della Probabilità Totale per le Densità

Così come per le probabilità discrete, se abbiamo una partizione dello spazio campionario $\{E_1, E_2, \ldots, E_m\}$, possiamo condizionare la densità di $X$:

> [!abstract] **PDF e Media per Partizione**
> $$f_X(x) = \sum_{m=1}^{M} f_{X \mid E_m}(x \mid E_m) P(E_m)$$
> $$E[X] = \sum_{m=1}^{M} E[X \mid E_m] P(E_m)$$
> *Esempio:* Se $Y = B \cdot X$ dove $X \sim \text{Exp}(\lambda)$ e $B$ lancia una moneta assegnando segni $\{-1, 1\}$ con probabilità $\frac{1}{2}$, condizionando sul segno $B$ si ricostruisce esattamente la PDF della variabile di Laplace!


## 5.9 Estensione al Multidimensionale: Variabili Aleatorie Doppie

Nel caso continuo, due variabili aleatorie $X$ e $Y$ sono descritte congiuntamente da una **PDF congiunta** $f_{X,Y}(x,y)$, funzione di due variabili. Il concetto si estende in modo analogo alla densità di massa di una lamina piana in fisica.

> [!info] **Densità di Probabilità Congiunta**
> $$f_{X,Y}(x,y) = \lim_{\Delta x, \Delta y \to 0} \frac{P\left(x-\frac{\Delta x}{2} < X \leq x+\frac{\Delta x}{2}, \, y-\frac{\Delta y}{2} < Y \leq y+\frac{\Delta y}{2}\right)}{\Delta x \Delta y}$$
> L'integrale doppio su tutto $\mathbb{R}^2$ fa 1. La probabilità che la coppia $(X,Y)$ appartenga a una regione bidimensionale $A$ è l'integrale doppio della densità su $A$.

> [!abstract] **Densità Marginali e Indipendenza**
> Saturando (integrando) rispetto a una variabile si ottiene la densità (marginale) dell'altra:
> $$f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y) dy$$
> Due variabili continue sono **indipendenti** se e solo se la PDF congiunta fattorizza nel prodotto delle marginali:
> $$f_{X,Y}(x,y) = f_X(x) f_Y(y)$$

## 5.10 Somma di Variabili Indipendenti (Convoluzione)

Spesso si è interessati alla PDF della somma $Z = X + Y$, dove $X$ e $Y$ sono variabili aleatorie **indipendenti**.

> [!info] **Teorema della Convoluzione**
> La PDF della somma di due variabili aleatorie indipendenti è il **prodotto di convoluzione** delle rispettive PDF:
> $$f_Z(z) = (f_X * f_Y)(z) = \int_{-\infty}^{+\infty} f_X(z - y) f_Y(y) dy = \int_{-\infty}^{+\infty} f_X(x) f_Y(z - x) dx$$
> L'operazione di convoluzione gode delle proprietà commutativa, associativa e distributiva.

> [!tip] **Parole del Professore**
> L'importanza del prodotto di convoluzione è immensa. Esso regola la relazione ingresso-uscita di tutti i sistemi LTI (Lineari Tempo Invarianti). Dal punto di vista della probabilità, la convoluzione ripetuta è il cuore del **Teorema Centrale del Limite**: sovrapponendo un gran numero di variabili aleatorie elementari indipendenti si ottiene una distribuzione Gaussiana (Normale).


### Variabile Geometrica *(non nel libro ma trattata a lezione)*

La variabile geometrica modella il **numero di tentativi** fino al primo successo, in una sequenza di prove indipendenti. È la versione discreta dell'esponenziale.

> [!info] **Definizione: Variabile Geometrica**
> $X \sim \text{Geom}(p)$ se $\mathcal{X} = \{1, 2, 3, \ldots\}$ con:
> $$p_X(n) = (1-p)^{n-1} \cdot p, \quad n = 1, 2, 3, \ldots$$
> $X = n$ significa: i primi $n-1$ tentativi sono falliti e il $n$-esimo è un successo.

> [!abstract] **Media e Varianza della Geometrica**
> $$E[X] = \frac{1}{p}, \qquad \text{Var}(X) = \frac{1-p}{p^2}$$
> *Calcolo della media:* $E[X] = p\sum_{n=1}^\infty n(1-p)^{n-1} = p \cdot \frac{d}{dq}\left(\sum_{n=0}^\infty q^n\right) = p \cdot \frac{d}{dq}\frac{1}{1-q} = p \cdot \frac{1}{(1-q)^2} = \frac{1}{p}$.

> [!example] **Esempio: roulette**
> La roulette ha 37 numeri. La probabilità di indovinare il numero puntato è $p = 1/37$. Il tempo atteso al primo successo è $E[X] = 37$ puntate. Tuttavia il banco paga 36 volte la posta (non 37), garantendo un valore atteso negativo per il giocatore.

> [!abstract] **Assenza di memoria della Geometrica**
> $$P(X > m + n \mid X > m) = P(X > n) \quad \forall m, n \geq 0$$
> La geometrica è l'**unica** distribuzione discreta con questa proprietà.




# Capitolo 6 — Distributions of Sampling Statistics

## 6.1 Introduction

**Non ancora trattato.**



## 6.2 The Sample Mean

**Parzialmente trattato** (la convergenza della frequenza alla probabilità è stata accennata nell'approccio frequentistico — §3.4). La distribuzione della media campionaria non è stata sviluppata formalmente.



## 6.3 The Central Limit Theorem

**Non ancora trattato.**



## 6.4 Sample Variance

**Non ancora trattato.**



## 6.5 Sampling Distributions from a Normal Population

**Non ancora trattato.**



## 6.6 Sampling from a Finite Population

**Non ancora trattato.**



# Capitolo 7 — Parameter Estimation

## 7.1 Introduction

**Non ancora trattato.**



## 7.2 Maximum Likelihood Estimators

**Non ancora trattato.**



## 7.3 Interval Estimates

**Non ancora trattato.**



## 7.4 Estimating the Difference in Means of Two Normal Populations

**Non ancora trattato.**



## 7.5 Interval Estimates of Population Variances

**Non ancora trattato.**



## 7.6 Estimating the Unknown Bernoulli Parameter

**Non ancora trattato.**



## 7.7 Interval Estimates of the Mean of a Poisson Distribution

**Non ancora trattato.**



## 7.8 Bayes Estimators

**Non ancora trattato.**



# Capitolo 8 — Hypothesis Testing

## 8.1 Introduction

**Non ancora trattato.**



## 8.2 Significance Levels

**Non ancora trattato.**



## 8.3 Tests Concerning the Mean of a Normal Population

**Non ancora trattato.**



## 8.4 Testing the Equality of Means of Two Normal Populations

**Non ancora trattato.**



## 8.5 Tests Concerning the Variance of a Normal Population

**Non ancora trattato.**



## 8.6 Tests Concerning Bernoulli Parameters

**Non ancora trattato.**



## 8.7 Tests Concerning Poisson Parameters

**Non ancora trattato.**



# Capitolo 9 — Regression

## 9.1 Introduction

**Non ancora trattato.**



## 9.2 Least Squares Estimators of the Regression Parameters

**Non ancora trattato.**



## 9.3 Distribution of the Estimators

**Non ancora trattato.**



## 9.4 Statistical Inferences about the Regression Parameters

**Non ancora trattato.**



## 9.5 The Coefficient of Determination and the Sample Correlation Coefficient

**Non ancora trattato.**



## 9.6 Analysis of Residuals: Assessing the Model

**Non ancora trattato.**



## 9.7 Transforming to Linearity

**Non ancora trattato.**



## 9.8 Weighted Least Squares

**Non ancora trattato.**



## 9.9 Polynomial Regression

**Non ancora trattato.**



## 9.10 Multiple Linear Regression

**Non ancora trattato.**



## 9.11 Logistic Regression Models for Binary Output Data

**Non ancora trattato.**
