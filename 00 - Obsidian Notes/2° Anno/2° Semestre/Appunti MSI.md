# Appunti MSI — Metodi Statistici per l'Informazione

> [!info] **Info corso**
> **Docente:** Prof. Marco Lops · **CFU:** 6 · **Esame:** Scritto + colloquio rapido
> **Testi:** Conte *Fenomeni Aleatori* (teoria); Ross *Probability and Statistics for Engineers and Scientists* (statistica)

---

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

---

## 3.2 Sample Space and Relationships Between Events

> [!info] **Definizione: Esperimento**
> Un **esperimento** è un'operazione, o un insieme di operazioni, che conduce a uno tra tanti risultati possibili.

> [!info] **Definizione: Spazio dei campioni**
> Lo **spazio dei campioni** (*sample space*), indicato con $\Omega$, è l'insieme — non necessariamente numerico — di tutti i possibili risultati di un esperimento.

Lo spazio dei campioni può avere diverse nature:

| Tipo | Esempio |
|------|---------|
| **Finito** | Lancio di una moneta: $\Omega = \{T, C\}$ |
| **Infinito numerabile** | Numero di pacchetti in coda a un router: $\Omega = \mathbb{N}_0$ |
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
> Un **evento** è un sottoinsieme di $\Omega$ definito da una proposizione. Un **evento elementare** è un singolo elemento di $\Omega$.

Un evento è **univocamente determinato** dagli elementi di $\Omega$ che lo compongono, ma la **proposizione** che lo descrive non è univoca — la ridondanza del linguaggio naturale permette formulazioni diverse dello stesso evento.

> [!example] **Esempio: ambiguità della proposizione**
> Con $\Omega = \{1,2,3,4,5\}$ (euro in tasca), l'evento $A = \{1,3,5\}$ può essere descritto come: "Ho un numero dispari di euro", oppure "Non ho un numero pari di euro", oppure "Ho 1, 3 o 5 euro". L'evento è lo stesso, le proposizioni sono diverse.

> [!tip] **Parole del Professore**
> Risolvere un esercizio di probabilità su spazi discreti richiede spesso un unico vero sforzo: **riformulare la proposizione** che definisce l'evento in modo che la soluzione appaia chiara. Esempio classico: "Qual è la probabilità che due persone in una classe di 30 abbiano lo stesso compleanno?" — la chiave è lavorare sull'evento complementare.

### Nomenclatura degli eventi

| Nome | Simbolo | Significato |
|------|---------|-------------|
| Evento certo | $\Omega$ | Si verifica sempre |
| Evento impossibile | $\emptyset$ | Non si verifica mai |
| Evento complementare | $A^c$ o $\bar{A}$ | Tutti gli $\omega \notin A$ |
| Evento implicato | $A \subseteq B$ | $A$ accade $\Rightarrow$ $B$ accade |
| Eventi incompatibili | $A \cap B = \emptyset$ | Non si verificano insieme |

### Algebra degli eventi

Le operazioni fondamentali sugli insiemi sono: **unione** $A \cup B$ (almeno uno), **intersezione** $A \cap B$ (entrambi), **complemento** $A^c$ (negazione), **differenza** $A \setminus B = A \cap B^c$.

Proprietà fondamentali:

$$\Omega^c = \emptyset, \qquad (A^c)^c = A, \qquad A \cup A^c = \Omega$$

**Leggi di De Morgan:**

$$( A \cup B)^c = A^c \cap B^c, \qquad (A \cap B)^c = A^c \cup B^c$$

Dal punto di vista formale, una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$ si chiama **algebra** se è chiusa rispetto all'unione e alla complementazione. Da queste due proprietà deriva automaticamente la chiusura rispetto all'intersezione (via De Morgan) e alla differenza. Quando $\Omega$ è infinito numerabile si richiede una proprietà più forte: una **$\sigma$-algebra**, chiusa rispetto a unioni *numerabili*. Questo è necessario per poter assegnare probabilità a eventi come "il numero di pacchetti è dispari" = $\{1,3,5,7,\ldots\}$, che è un'unione infinita di eventi elementari.

---

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

---

## 3.4 Sample Spaces Having Equally Likely Outcomes

Quando $\Omega$ è finito e tutti gli eventi elementari sono **equiprobabili**, la probabilità di un evento si calcola come:

$$\boxed{P(A) = \frac{|A|}{|\Omega|}}$$

Questo riduce il problema a un conteggio combinatorio.

> [!warning]
> Questa formula è valida **solo** se gli eventi elementari sono equiprobabili. Se il dado è truccato, contare i casi favorevoli su quelli possibili non funziona.

### Analisi Combinatoria

Il principio fondamentale è la **cardinalità del prodotto cartesiano**: dati $k$ insiemi con cardinalità $n_1, n_2, \ldots, n_k$:

$$|A_1 \times A_2 \times \cdots \times A_k| = \prod_{i=1}^{k} n_i$$

Da questa regola si derivano tutti i risultati dell'analisi combinatoria.

| Tipo di selezione | Formula | Nome |
|-------------------|---------|------|
| $k$-uple ordinate **con** ripetizione da $n$ | $n^k$ | — |
| $k$-uple ordinate **senza** ripetizione da $n$ | $\dfrac{n!}{(n-k)!}$ | Disposizioni semplici |
| $n$-uple ordinate senza ripetizione da $n$ | $n!$ | Permutazioni |
| $k$-uple **non ordinate** senza ripetizione da $n$ | $\dbinom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$ | Combinazioni |

**Sequenze binarie di lunghezza $n$ con esattamente $k$ uni:** se i bit fossero tutti distinti, le permutazioni sarebbero $n!$; ma i $k$ uni sono indistinguibili tra loro (danno $k!$ permutazioni identiche) e così gli $n-k$ zeri (danno $(n-k)!$ permutazioni identiche). Quindi il numero di sequenze distinte è:

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

---

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

---

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

---

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

---

## 3.8 Law of Total Probability

Sia $\{E_1, E_2, \ldots, E_m\}$ una **partizione** di $\Omega$ (eventi a due a due disgiunti la cui unione è $\Omega$). Per qualunque evento $A$:

$$\boxed{P(A) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)}$$

*Dimostrazione:* $A = A \cap \Omega = A \cap \bigl(\bigcup_i E_i\bigr) = \bigcup_i (A \cap E_i)$. Gli insiemi $A \cap E_i$ sono disgiunti, quindi per additività:

$$P(A) = \sum_{i=1}^m P(A \cap E_i) = \sum_{i=1}^m P(A \mid E_i) \cdot P(E_i)$$

Questa legge è fondamentale: permette di scomporre il calcolo di una probabilità difficile condizionando rispetto a una partizione che semplifica il problema.

