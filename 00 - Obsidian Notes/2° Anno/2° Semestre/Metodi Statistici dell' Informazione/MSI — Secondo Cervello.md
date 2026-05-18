---
tags: [MSI, secondo-cervello, master-guide, paranoia-tecnica]
corso: Metodi Statistici dell'Informazione
docente: Marco Lops
status: in-progress
---

# 🧠 MSI — Secondo Cervello (Paranoia Tecnica)

> [!ABSTRACT] Mappa Mentale del Corso e Metodo
> Questo file è progettato con il protocollo **MemoVia 2.0 (Paranoia Tecnica)**. L'obiettivo non è riassumere, ma *scolpire* l'informazione per renderla inattaccabile.
> I callout colorano il tipo di informazione:
> - **Ciano (ABSTRACT)** = L'essenza matematica pura.
> - **Verde (QUOTE)** = Definizioni formali, Formule LaTeX e Dimostrazioni.
> - **Giallo (EXAMPLE)** = Fenomenologia, metafore e applicazioni fisiche.
> - **Rosso (DANGER)** = I tranelli d'esame e le "trappole logiche" da evitare.
> - **Nodi** = Punti di ancoraggio per il richiamo rapido.

---

# 🔵 PILASTRO I — Fondamenti e Architettura dell'Incertezza

## L'Informazione e lo Spazio degli Eventi
> [!ABSTRACT] 
> L'informazione nasce esclusivamente dall'incertezza. Se non c'è incertezza a priori, non c'è informazione da trasferire. La probabilità è il framework matematico che modella l'incertezza.
> [!QUOTE] 
> Spazio dei Campioni ($\Omega$): L'insieme di tutti i possibili esiti di un esperimento. Può essere finito (moneta: $\{T,C\}$), numerabile (pacchetti in coda: $\mathbb{N}_0$) o continuo (rumore termico: $\mathbb{R}$). 
> Evento: Un sottoinsieme di $\Omega$.
> [!EXAMPLE] 
> Telecomunicazioni vs Informatica: Entrambe trattano l'informazione. Le telecomunicazioni la trasferiscono *nello spazio* (canale rumoroso), l'informatica la trasferisce *nel tempo* (hard disk, compressione).
> [!DANGER] 
> Confondere probabilità zero con impossibilità fisica. In uno spazio continuo o infinito numerabile, un evento con probabilità 0 (es. estrarre esattamente $\pi$ da un generatore continuo) può comunque verificarsi "quasi certamente".

- Nodo Radice: L'incertezza è la valuta dell'informazione.
- Nodo Evento: Un evento è univoco, ma la proposizione linguistica che lo descrive no (riformulare l'evento è il 90% del lavoro).

## Analisi Combinatoria: L'Arte di Contare
> [!ABSTRACT] 
> Se uno spazio è finito e gli eventi elementari sono equiprobabili, la probabilità diventa una pura operazione di conteggio: $P(A) = \frac{|A|}{|\Omega|}$.
> [!QUOTE] 
> Disposizioni con Ripetizione (Ordinate): $n^k$
> Disposizioni Semplici (Ordinate): $D_{n,k} = \frac{n!}{(n-k)!}$
> Permutazioni (Ordinate, $k=n$): $n!$
> Combinazioni (Non Ordinate): $\binom{n}{k} = \frac{n!}{k!(n-k)!}$
> Binomio di Newton: $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ (Numero di sottoinsiemi, ovvero cardinalità dell'Insieme delle Parti $\mathcal{P}(\Omega)$).
> Coefficiente Multinomiale: $\binom{n}{n_1, n_2, \ldots, n_m} = \frac{n!}{n_1! \cdot n_2! \cdots n_m!}$
> [!EXAMPLE] 
> Mani a Poker (Non ordinate): 5 carte da 52 sono $\binom{52}{5} = 2.598.960$. 
> Sequenze Binarie con $k$ uni: Per contare le stringhe lunghe $n$ con esattamente $k$ uni e $n-k$ zeri, si usano le combinazioni (i $k$ uni sono indistinguibili tra loro): $\binom{n}{k}$.
> [!DANGER] 
> Usare le combinazioni quando l'ordine conta. Esempio: Il codice di un bancomat (1234 è diverso da 4321) richiede Disposizioni Semplici. Una mano a scala quaranta richiede le Combinazioni.

- Nodo Alfabeto: Il coefficiente binomiale cuenta le permutazioni degli elementi distinguibili dividendo per le permutazioni di quelli indistinguibili.
- Nodo Newton: L'insieme delle parti esplode esponenzialmente come $2^n$.

## Approccio Frequentistico vs Assiomatico
> [!ABSTRACT] 
> L'approccio frequentistico definisce $P(A) = \lim_{n \to \infty} \frac{N_A}{n}$. È intuitivo ma circolarmente difettoso (il limite richiede indipendenza, che è un concetto probabilistico). L'approccio assiomatico di Kolmogorov fonde la probabilità con la teoria della Misura.
> [!QUOTE] 
> Assiomi di Kolmogorov per lo Spazio di Probabilità $(\Omega, \mathcal{E}, P)$:
> 1. Non negatività: $P(A) \geq 0$
> 2. Normalizzazione: $P(\Omega) = 1$
> 3. Additività (Disgiunti): $A \cap B = \emptyset \implies P(A \cup B) = P(A) + P(B)$
> 3.5. $\sigma$-Additività: Valida per successioni numerabili di eventi disgiunti.
> [!EXAMPLE] 
> Misurare con l'Ape: La probabilità è una misura geometrica anomala. In una stanza di 50mq, ogni mq vale geometricamente $1/50$. Ma se metti un fiore in un angolo, la "probabilità" di trovarvi un'ape in quel mq balza a $0.99$. L'area è la stessa, la misura probabilistica no.
> [!DANGER] 
> Usare l'approccio frequentistico (rapporto di casi) se gli eventi NON sono equiprobabili. Un dado truccato rende invalido $P(E) = \frac{|E|}{|\Omega|}$.

- Nodo Limite: La frequenza empirica converge asintoticamente alla probabilità reale.
- Nodo Misura: La probabilità è una funzione che mappa insiemi su $[0,1]$.

## Algebra e $\sigma$-Algebra
> [!ABSTRACT] 
> Per poter calcolare matematicamente la probabilità senza uscire dai confini, l'insieme degli eventi deve formare una struttura algebrica chiusa.
> [!QUOTE] 
> Algebra di Eventi ($\mathcal{E}$): Chiusa per Unione ($A \cup B \in \mathcal{E}$) e Complementazione ($A^c \in \mathcal{E}$). Via De Morgan, risulta chiusa per intersezione e differenza.
> $\sigma$-Algebra: Un'algebra che garantisce la chiusura anche per unioni infinite numerabili. Necessaria quando $\Omega$ è continuo o infinito discreto ($\mathbb{N}_0$).
> [!EXAMPLE] 
> Algebra Minimale: Se $A$ è "esce pari", la più piccola algebra è $\{\emptyset, \Omega, A, A^c\}$.

- Nodo Dominio: L'algebra definisce il recinto entro cui la funzione Misura può operare legalmente.
- Nodo Chiusura: Tutte le combinazioni insiemistiche ricadono sempre nell'algebra.

## Teoremi Derivati dagli Assiomi
> [!ABSTRACT] 
> Grazie ai 3 Assiomi di Kolmogorov, le proprietà insiemistiche si trasformano in equazioni algebriche blindate.
> [!QUOTE] 
> - $P(A^c) = 1 - P(A)$ (da $A \cup A^c = \Omega$)
> - $P(\emptyset) = 0$
> - Subadditività: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
> - Differenza: $P(A \setminus B) = P(A) - P(A \cap B)$
> [!EXAMPLE] 
> Dimostrazione Subadditività: Scomponiamo $A \cup B$ negli insiemi disgiunti $A$ e $(B \setminus A)$. Per l'Assioma 3: $P(A \cup B) = P(A) + P(B \setminus A)$. Sostituendo la differenza, si ottiene la formula.

- Nodo Geometria: La probabilità di un'unione sottrae sempre l'intersezione per non contarla due volte.

## Probabilità Condizionata e Legge Composta
> [!ABSTRACT] 
> Condizionare un evento significa distruggere l'universo originario ($\Omega$) e crearne uno nuovo, ristretto all'evento condizionante ($B$).
> [!QUOTE] 
> Definizione: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ (con $P(B)>0$).
> Legge Composta: $P(A \cap B) = P(A)P(B \mid A) = P(B)P(A \mid B)$
> [!EXAMPLE] 
> Il Database: Vuoi $P(\text{peso}>70 \mid \text{altezza}>170)$. Prendi il database di 60 milioni di italiani, applichi il filtro `altezza > 170`, e dividi il numero di persone $>70kg$ rimaste per la *nuova* dimensione del database ristretto.
> [!DANGER] 
> Credere che $P(A \mid B)$ sia uguale a $P(B \mid A)$. "Probabilità di avere l'ombrello dato che piove" è diversa da "Probabilità che piova dato che hai l'ombrello".

- Nodo Filtro: Il condizionamento è una query SQL col costrutto `WHERE`.
- Nodo Asimmetria: Il condizionamento inverte drasticamente il dominio di riferimento.

## Indipendenza Stocastica
> [!ABSTRACT] 
> L'indipendenza si ha quando l'universo ristretto fornisce esattamente le stesse informazioni dell'universo originario. Il condizionamento diviene ininfluente.
> [!QUOTE] 
> Definizione: $A \perp B \iff P(A \cap B) = P(A)P(B) \iff P(A \mid B) = P(A)$.
> Teorema: Se $A \perp B$, allora $A^c \perp B^c$.
> [!EXAMPLE] 
> Piove a Napoli e piove a Kathmandu: Saperlo in un posto non cambia la stima per l'altro. Piove a Napoli e piove a Caserta: Eventi dipendenti (correlati dal meteo regionale).
> [!DANGER] 
> Indipendenza a coppie $\neq$ Indipendenza Congiunta! 
> **Controesempio del Bit di Parità**: $X_3 = X_1 \oplus X_2$. $X_1$ e $X_2$ sono indipendenti. Anche le altre coppie lo sono. Ma se conosci $X_1$ e $X_2$, $X_3$ è *determinato* (probabilità 1). La terna NON è indipendente.

- Nodo Moltiplicazione: L'intersezione di eventi indipendenti è il semplice prodotto delle marginali.
- Nodo Inganno: L'indipendenza su scala inferiore non garantisce l'indipendenza strutturale globale.

## Il Trucco dell' "Almeno Uno"
> [!ABSTRACT] 
> Calcolare l'unione di $n$ eventi è un incubo matematico. Il passaggio al complementare trasforma l'unione (somma logica) in intersezione (prodotto logico).
> [!QUOTE] 
> Se $A_1, \ldots, A_n$ sono indipendenti con $P(A_i) = p_i$:
> $P(\text{nessuno}) = \prod_{i=1}^n (1 - p_i)$
> $P(\text{almeno uno}) = 1 - P(\text{nessuno}) = 1 - \prod_{i=1}^n (1 - p_i)$
> $P(\text{esattamente uno}) = \sum_{i=1}^n p_i \prod_{j \neq i} (1 - p_j)$
> [!EXAMPLE] 
> Paradosso del Compleanno: Invece di calcolare la probabilità complessa che due, tre o dieci persone condividano il compleanno, si calcola la probabilità che *tutti* siano diversi: $1 - (\frac{365}{365} \cdot \frac{364}{365} \cdots \frac{365-N+1}{365})$.

- Nodo Specchio: La negazione inverte il problema trasformandolo da impossibile a banale.

## Probabilità Totale e Teorema di Bayes
> [!ABSTRACT] 
> Se un problema è troppo complesso, lo si divide in scompartimenti stagni (partizione). Bayes usa questi scompartimenti per invertire la causa e l'effetto.
> [!QUOTE] 
> Probabilità Totale (Partizione $E_1, \ldots, E_m$): 
> $P(A) = \sum_{i=1}^m P(A \mid E_i)P(E_i)$
> Teorema di Bayes: 
> $P(B \mid A) = \frac{P(A \mid B)P(B)}{P(A)} = \frac{P(A \mid B)P(B)}{\sum_i P(A \mid E_i)P(E_i)}$
> [!EXAMPLE] 
> Il Dado Truccato: Ho 2 dadi onesti e 1 truccato (esce 6 al 50%). Pesco a caso e lancio: esce 6. Qual è la probabilità di aver pescato il truccato?
> A Priori: $P(T) = 1/3 \approx 33\%$.
> A Posteriori: $P(T \mid \text{esce 6}) = \frac{P(\text{6} \mid T)P(T)}{P(\text{6})} = \frac{(1/2)(1/3)}{(1/6)(2/3) + (1/2)(1/3)} = 60\%$. L'evidenza empirica ha aggiornato la credenza dal 33% al 60%.
> [!DANGER] 
> Omettere il denominatore della Probabilità Totale. Il Teorema di Bayes è inutile se non si pesa l'effetto contro tutte le altre cause possibili della partizione.

- Nodo Frantumazione: La probabilità totale seziona la realtà in compartimenti incompatibili.
- Nodo Aggiornamento: Bayes ricalibra le credenze matematiche alla luce della nuova evidenza empirica.

---

# 🔵 PILASTRO II — Variabili Aleatorie Discrete

## Astrazione: Dallo Spazio agli Interi
> [!ABSTRACT] 
> Le Variabili Aleatorie (VA) unificano esperimenti eterogenei. Lancio della moneta (T,C), dado (Pari,Dispari), segnale elettrico (Alto,Basso) diventano la stessa astrazione matematica $\{0,1\}$.
> [!QUOTE] 
> Variabile Aleatoria ($X$): Un'applicazione $X: \Omega \to \mathcal{X}$ che associa ad ogni esito dello spazio dei campioni un valore numerico in un Alfabeto $\mathcal{X}$.
> PMF (Probability Mass Function): Nel caso discreto, $p_X(x) = P(X=x)$. Deve soddisfare $p_X(x) \geq 0$ e $\sum p_X(x) = 1$.
> [!EXAMPLE] 
> Se ho $2^k$ stringhe binarie in memoria, l'esperimento astratto diventa semplicemente l'estrazione di un puntatore di memoria (intero da $0$ a $2^k-1$).

- Nodo Mappatura: La VA maschera l'universo fisico dietro numeri calcolabili.

## Valore Atteso (Media Statistica)
> [!ABSTRACT] 
> La media statistica è il baricentro gravitazionale della distribuzione di probabilità. Per la Legge dei Grandi Numeri, è il limite a cui tende la media campionaria all'infinito.
> [!QUOTE] 
> $E[X] = \mu_X = \sum_{x \in \mathcal{X}} x \cdot p_X(x)$
> [!EXAMPLE] 
> Media degli stipendi: Se 9 operai guadagnano 30k e 1 CEO guadagna 300k, la media è 57k. Ma 57k non rappresenta nessuno!
> [!DANGER] 
> Confondere la media statistica (pesata) con la media aritmetica. Coincidono **esclusivamente** nella distribuzione Uniforme. Inoltre, la media è drasticamente sensibile ai valori anomali (Outlier); per questo nella vita reale si usa la Mediana.

- Nodo Baricentro: Il valore atteso subisce un tiraggio inerziale dalle masse di probabilità estreme.

## Distribuzioni Discrete Notevoli e Dimostrazioni

### Bernoulli e Binomiale
> [!ABSTRACT] 
> La Bernoulli è il quanto atomico di probabilità. La Binomiale è la somma algebrica di $n$ quanti i.i.d. (Indipendenti e Identicamente Distribuiti).
> [!QUOTE] 
> Bernoulli: $\text{Ber}(p)$. Alfabeto $\{0,1\}$. $p_X(x) = p^x (1-p)^{1-x}$. 
> Media: $E[X] = 1 \cdot p + 0 \cdot (1-p) = p$.
> Binomiale: $\text{Bin}(n,p)$. Alfabeto $\{0, 1, \dots, n\}$. $p_X(k) = \binom{n}{k}p^k(1-p)^{n-k}$.
> Media: $E[S_n] = E[\sum X_i] = \sum E[X_i] = np$.
> [!EXAMPLE] 
> Vaccino: Efficacia 95%. Somministrato a 1000 persone. Numero atteso di immuni: $1000 \cdot 0.95 = 950$.

- Nodo Atomo: La singola prova vincola il successo a $p$.
- Nodo Aggregazione: La somma binomiale accumula le varianze e stabilizza la media lineare.

### Uniforme Discreta
> [!ABSTRACT] 
> L'anomalia statistica dove la geometria piatta fa coincidere la media statistica con quella aritmetica.
> [!QUOTE] 
> Uniforme: Alfabeto $\{1, \ldots, M\}$. $p_X(k) = 1/M$.
> Media: $E[X] = \sum_{k=1}^M k \cdot \frac{1}{M} = \frac{1}{M} \frac{M(M+1)}{2} = \frac{M+1}{2}$.
> [!EXAMPLE] 
> Dado a 6 facce. $E[X] = \frac{6+1}{2} = 3.5$. (Nota che la media non appartiene all'alfabeto!)

- Nodo Piattezza: La massa è spalmata uniformemente abbattendo la pesatura asimmetrica.

### Poisson (Distribuzione degli Eventi Rari)
> [!ABSTRACT] 
> Limite asintotico della Binomiale per $n \to \infty$ e $p \to 0$. Modella l'arrivo asincrono di eventi indipendenti su uno spettro temporale continuo.
> [!QUOTE] 
> Poisson: $\text{Poi}(\lambda)$. Alfabeto $\mathbb{N}_0 = \{0, 1, 2, \dots\}$. 
> PMF: $p_X(k) = \frac{\lambda^k}{k!}e^{-\lambda}$. (Normalizzazione garantita dallo sviluppo di Taylor di $e^\lambda$).
> Media: $E[X] = \sum_{k=1}^\infty k \frac{\lambda^k}{k!} e^{-\lambda} = \lambda e^{-\lambda} \sum_{j=0}^\infty \frac{\lambda^j}{j!} = \lambda$.
> [!EXAMPLE] 
> Pacchetti al Router: Un nodo di rete riceve in media 100 pacchetti al ms. Modello: $\text{Poi}(100)$. Fondamentale per dimensionare le code ed evitare Buffer Overflow.
> [!DANGER] 
> Usare la Poisson per eventi con forte memoria (come scosse di assestamento di un terremoto). La Poisson richiede che gli eventi nel tempo siano indipendenti.

- Nodo Deriva: Il parametro $\lambda$ è simultaneamente il rate fisico, la media e la varianza del processo.

### Geometrica (Tempo di Attesa e Assenza di Memoria)
> [!ABSTRACT] 
> Numero di fallimenti consecutivi necessari prima di ottenere il primo successo. Gode dell'inquietante proprietà Memoryless.
> [!QUOTE] 
> Geometrica: $\text{Geo}(p)$. Alfabeto $\{1, 2, 3, \dots\}$.
> PMF: $p_X(k) = (1-p)^{k-1}p$.
> Media: Derivata della serie geometrica $\to E[X] = 1/p$.
> [!EXAMPLE] 
> Roulette: Scommessa sul rosso ($p=18/37$). Tempo medio per vincere: $1/p = 37/18 \approx 2.06$ giocate.
> [!DANGER] 
> Il Fallacy del Giocatore (Assenza di Memoria): $P(X > n+m \mid X > n) = P(X > m)$. Se lanci una moneta 10 volte ed esce croce, la probabilità di successo all'undicesimo è SEMPRE $1/2$. Il passato non ricarica la probabilità.

- Nodo Amnesia: Il processo rinasce vergine ad ogni istante temporale. 
- Nodo Attesa: L'inverso della probabilità genera il raggio medio di attesa del successo.

## Trasformazioni e Teorema Fondamentale della Media
> [!ABSTRACT] 
> Calcolare il valore atteso di una trasformazione $Y = g(X)$ non richiede di conoscere la PMF di $Y$. Si può operare direttamente nello spazio originario di $X$.
> [!QUOTE] 
> Teorema Fondamentale: $E[g(X)] = \sum_{x \in \mathcal{X}} g(x) p_X(x)$
> [!EXAMPLE] 
> Se $Y = X^2$, non serve mappare $X \to Y$ (caso molti-a-uno, dove le probabilità collassano). Sommi semplicemente $x^2 \cdot p_X(x)$.

- Nodo Biiettivo vs Molti-a-uno: Una trasformazione biiettiva fa un semplice *reflagging* delle etichette (le probabilità restano intatte). Una molti-a-uno somma le probabilità degli eventi che collassano.

## Varianza, Dispersione e Disuguaglianze
> [!ABSTRACT] 
> Se la Media è il baricentro, la Varianza è il momento d'inerzia. Misura l'entità dell'aleatorietà: quanto le realizzazioni fisiche sfuggono all'attrazione del baricentro.
> [!QUOTE] 
> Varianza: $\sigma_X^2 = E[(X-\mu_X)^2] = E[X^2] - \mu_X^2$
> Deviazione Standard: $\sigma_X = \sqrt{\sigma_X^2}$
> Linearità Media: $E[aX+b] = aE[X]+b$
> Invarianza/Covarianza Varianza: $\sigma_{aX+b}^2 = a^2\sigma_X^2$
> Disuguaglianza di Markov ($Y \geq 0$): $P(Y \geq \delta) \leq \frac{E[Y]}{\delta}$
> Disuguaglianza di Chebyshev: $P(|X-\mu_X| \geq k\sigma_X) \leq \frac{1}{k^2}$
> [!EXAMPLE] 
> RMS e Corrente Efficace: La corrente alternata ha media zero, ma la potenza dissipata dipende dall'RMS ($E[X^2]$). Una presa con $\mu = 0$ ti folgora lo stesso.
> La Potenza di Chebyshev: Metti $k=10$. Qualsiasi sia la distribuzione al mondo, la probabilità di trovare un valore oltre 10 deviazioni standard dalla media è inferiore all'1%.
> [!DANGER] 
> Il paradosso della Martingala (Raddoppio della posta). Il limite del guadagno per $S \to \infty$ diverge, ma fare il limite di $S$ e puntare all'infinito non sono la stessa cosa (convergenza in probabilità vs convergenza della media). Al casinò la rovina è certa a causa del limite di puntata.

- Nodo Inerzia: Se $\sigma^2 = 0$, la variabile è deterministica (collassa sulla media).
- Nodo Universalità: Chebyshev non richiede di conoscere la distribuzione. Ti dà un bound assoluto usando solo media e varianza.

---

# 🔵 PILASTRO III — Variabili Aleatorie Multiple ed Entropia

## La Matrice dell'Incertezza: PMF Congiunta e Marginali
> [!ABSTRACT] 
> Osservare due fenomeni simultaneamente richiede un salto dimensionale. La PMF congiunta è la matrice madre; le marginali sono solo le ombre (proiezioni) di questa matrice sugli assi.
> [!QUOTE] 
> PMF Congiunta: $p_{XY}(x,y) = P(X=x, Y=y)$.
> Marginalizzazione: $p_X(x) = \sum_y p_{XY}(x,y)$. (La marginalizzazione è a tutti gli effetti la media statistica della PMF condizionale: $E_Y[p_{X|Y}(x|Y)]$)
> Indipendenza Statistica: $X \perp Y \iff p_{XY}(x,y) = p_X(x)p_Y(y)$
> Regola della Catena: $p_{XYZ}(x,y,z) = p_Z(z) p_{Y|Z}(y|z) p_{X|YZ}(x|y,z)$
> [!EXAMPLE] 
> Terne di Bit e l'Illusione delle Marginali: Prendi 3 bit i.i.d e 3 bit in cui il terzo è il Bit di Parità ($X_1 \oplus X_2$). Entrambi i sistemi hanno marginali identiche ($P(X_i=1) = p$). Ma le leggi congiunte sono drasticamente diverse! Le marginali nascondono la correlazione fisica.
> [!DANGER] 
> Congiunta $\implies$ Marginali. Ma Marginali $\cancel{\implies}$ Congiunta (salvo indipendenza). Dalle ombre non puoi ricostruire l'oggetto 3D originale.

- Nodo Ombra: La marginalizzazione schiaccia un asse (sommando le probabilità) per far sopravvivere solo l'altro.

## PMF Condizionale e Proprietà di Markov
> [!ABSTRACT] 
> Sezioni trasversali della matrice congiunta. Condizionare significa affettare la matrice e rinormalizzare la fetta affinché la sua somma torni a 1.
> [!QUOTE] 
> PMF Condizionale: $p_{X|Y}(x|y) = \frac{p_{XY}(x,y)}{p_Y(y)}$
> Proprietà di Markov: $P(X_{n+1} | X_n, X_{n-1}, \ldots, X_1) = P(X_{n+1} | X_n)$
> Indipendenza Condizionale: $X_1 \perp X_3 \mid X_2 \iff p_{X_1 X_3 | X_2} = p_{X_1|X_2} p_{X_3|X_2}$
> [!EXAMPLE] 
> Coda in Banca (Markov): Il numero di clienti al tempo $n+1$ dipende matematicamente SOLO dal numero di clienti al tempo $n$. La storia pregressa di come si è formata la coda è condizionalmente irrilevante (Assenza di memoria del passato remoto).

- Nodo Affettatrice: Nella tabella $p_{X|Y}(x|y)$, la somma su $x$ fa 1, ma la somma su $y$ no.
- Nodo Amnesia Storica: Markov taglia il cordone ombelicale col passato remoto. Il presente contiene tutta l'informazione necessaria per predire il futuro.

## Canale Binario Simmetrico (BSC) ed Entropia
> [!ABSTRACT] 
> Shannon definisce l'Informazione non come significato, ma come risoluzione dell'incertezza. Più un evento è raro, più il suo verificarsi è esplosivo informativamente.
> [!QUOTE] 
> Entropia di Shannon (Variabile Discreta): $H(X) = - \sum_{x} p_X(x) \log_2 p_X(x)$ [bit]
> Canale Binario Simmetrico (BSC): Probabilità di errore $\varepsilon$ fissa (inversione del bit). 
> Caso Peggiore: $\varepsilon = 1/2$ (rumore puro, $P(X \mid Y) = P(X)$).
> [!EXAMPLE] 
> Compressione File: Un file ZIP ideale ha 0 e 1 equiprobabili e indipendenti. Trasporta esattamente 1 bit di entropia per bit fisico. È incompressibile. Se $p \neq 0.5$, l'entropia crolla e Huffman può comprimere.
> [!DANGER] 
> Se $\varepsilon = 1$ in un BSC, il canale è perfetto! Basta invertire il bit ricevuto. L'abisso dell'informazione è $\varepsilon = 0.5$, dove l'entropia del rumore è massima e distrugge ogni traccia del segnale.

- Nodo Sorpresa: $I(A) = -\log_2 P(A)$. Evento certo = 0 bit (ovvietà).
- Nodo Rumore Massimo: La distruzione dell'informazione si ottiene quando l'entropia del disturbo satura a 1 bit ($\varepsilon=1/2$).

---

---

# 🔵 PILASTRO IV — Variabili Aleatorie Continue

## L'Abisso del Continuo: CDF e PDF
> [!ABSTRACT] 
> Nel dominio continuo, la probabilità di un singolo punto è rigorosamente zero. La probabilità diventa una massa distribuita su un intervallo, calcolabile solo tramite l'area sottesa a una curva di densità.
> [!QUOTE] 
> Funzione di Distribuzione Cumulativa (CDF): $F_X(x) = P(X \leq x)$. È universale, monotona crescente, vale 0 a $-\infty$ e 1 a $+\infty$.
> Densità di Probabilità (PDF): $f_X(x) = \frac{d}{dx} F_X(x)$.
> Probabilità di un intervallo: $P(a \leq X \leq b) = \int_a^b f_X(x) \, dx = F_X(b) - F_X(a)$.
> Valore Atteso (tramite somme di Riemann): $E[X] = \int_{-\infty}^{+\infty} x f_X(x) \, dx$.
> [!EXAMPLE] 
> Quantizzazione: Shannon dimostrò che digitalizzare dati analogici richiede di raggrupparli. Una variabile continua viene approssimata dividendo il supporto in intervalli di ampiezza $\delta$. Al limite per $\delta \to 0$, la sommatoria discreta diventa l'integrale di Riemann.
> [!DANGER] 
> L'errore letale all'esame: dire che $f_X(x)$ è una probabilità. **LA PDF NON È UNA PROBABILITÀ!** È una densità. Può tranquillamente assumere valori maggiori di 1 (es. un'Uniforme su $[0, 0.1]$ ha densità costante pari a 10).

- Nodo Zero: Un evento con probabilità 0 non è fisicamente impossibile nel continuo; è semplicemente un punto senza larghezza, ergo senza area.

## Distribuzioni Continue Fondamentali

### Uniforme Continua $U(a,b)$
> [!ABSTRACT] 
> Spande la probabilità in modo perfettamente omogeneo su un intervallo chiuso. È il modello dell'ignoranza massima e dell'errore di quantizzazione.
> [!QUOTE] 
> PDF: $f_X(x) = \frac{1}{b-a}$ per $x \in [a,b]$.
> CDF: Rampa lineare da 0 a 1 ($F_X(x) = \frac{x-a}{b-a}$).
> Media: $E[X] = \frac{a+b}{2}$ (Punto medio).
> Varianza: $\text{Var}(X) = \frac{(b-a)^2}{12}$.
> [!EXAMPLE] 
> Rumore di Quantizzazione: In un convertitore analogico-digitale (ADC), l'errore commesso per arrotondamento è modellato come Uniforme tra $-\Delta/2$ e $+\Delta/2$. La potenza del rumore di quantizzazione è la varianza: $\Delta^2/12$.

- Nodo Piattezza: La varianza dell'Uniforme è la base della teoria della codifica analogico-digitale.

### Esponenziale $\text{Exp}(\lambda)$
> [!ABSTRACT] 
> L'estensione continua della distribuzione Geometrica. È l'unica variabile continua che gode della proprietà di assenza di memoria (Markov).
> [!QUOTE] 
> PDF: $f_X(x) = \lambda e^{-\lambda x}$ (per $x \geq 0$).
> CDF: $F_X(x) = 1 - e^{-\lambda x}$.
> Media: $E[X] = \frac{1}{\lambda}$.
> [!EXAMPLE] 
> Tempi di attesa: Modella il tempo prima del decadimento di una particella radioattiva o il tempo tra due arrivi consecutivi in un server (coda di Poisson).
> [!DANGER] 
> Attenzione all'inganno di $\lambda$: Se $\lambda$ (tasso di guasto/arrivo) è molto alto, il tempo medio di attesa $E[X] = 1/\lambda$ è bassissimo. La curva decade istantaneamente.

- Nodo Amnesia Continua: Il fatto che l'autobus non sia passato negli ultimi 10 minuti non cambia la distribuzione del tempo rimanente prima che passi.

### Laplace e l'Abisso di Cauchy
> [!ABSTRACT] 
> Laplace modella rumori asimmetrici con code più "pesanti" dell'esponenziale; Cauchy distrugge la matematica stessa avendo momento d'inerzia infinito.
> [!QUOTE] 
> Laplace (Doppia Esponenziale): $f_X(x) = \frac{\lambda}{2} e^{-\lambda|x|}$. Ha media 0 e varianza $\frac{2}{\lambda^2}$. Modella il rumore impulsivo (es. fulmini, scariche atmosferiche).
> Distribuzione di Cauchy: $f_X(x) = \frac{1}{\pi(1+x^2)}$.
> [!EXAMPLE] 
> L'Anomalia di Cauchy: Modella la risonanza fisica. Le code decadono talmente lentamente che l'integrale della varianza diverge: $E[X^2] = \infty$. La deviazione standard non esiste. La media campionaria non convergerà MAI (legge dei grandi numeri infranta).

- Nodo Code Pesanti: Più le code decadono lentamente, più i valori estremi (outlier) dominano il fenomeno fisico.

## PDF Condizionata nel Continuo
> [!ABSTRACT] 
> Condizionare nel continuo significa ritagliare la PDF originale sull'intervallo dell'evento noto e amplificarla affinché l'area ritorni a valere 1.
> [!QUOTE] 
> Data $P(A) > 0$:
> $f_{X|A}(x) = \begin{cases} \frac{f_X(x)}{P(A)} & x \in A \\ 0 & x \notin A \end{cases}$
> [!EXAMPLE] 
> Triangolo Mozzato: Se ho una densità che va da -3 a 3 e condiziono all'evento $A = \{X \leq 0\}$ (la cui probabilità è 0.5), la densità per $x > 0$ si polverizza, mentre la densità nella parte negativa si raddoppia (diviso per 0.5 = moltiplicato per 2) per conservare l'area totale.

- Nodo Lente di Ingrandimento: Il condizionamento zooma sull'intervallo dell'evento e ne dilata verticalmente la densità.

---

# 🔵 PILASTRO V — Vettori, Trasformazioni e Teoremi Limite

## Estensione Bivariata e Vettori Aleatori
> [!ABSTRACT] 
> Due variabili continue sono accoppiate dalla loro PDF congiunta. La matrice di covarianza fotografa la correlazione tra le componenti, ma l'indipendenza è una condizione molto più forte dell'incorrelazione (tranne nel caso Gaussiano).
> [!QUOTE] 
> Densità Congiunta: $f_{X,Y}(x,y) \geq 0$, il volume sotteso fa 1.
> Marginalizzazione: $f_X(x) = \int f_{X,Y}(x,y) dy$.
> Vettore delle Medie: $\boldsymbol{\mu} = E[\mathbf{X}]$.
> Matrice di Covarianza ($K$): Simmetrica e semidefinita positiva. Sulla diagonale ha le varianze $\sigma_i^2$, fuori le covarianze.
> Correlazione Normalizzata: $\rho_{12} = \frac{\text{Cov}(X_1, X_2)}{\sigma_1 \sigma_2}$ (compresa in $[-1, 1]$).
> [!EXAMPLE] 
> Sfera vs Ellissoide: Se due variabili gaussiane sono indipendenti (e hanno stessa varianza), la loro densità congiunta nel piano forma circonferenze perfette. Se sono correlate, diventano ellissi inclinate a seconda del segno della covarianza.

- Nodo Incorrelazione vs Indipendenza: Se $\rho=0$, non c'è legame *lineare*. Ma potrebbero essere perfettamente legate da una legge quadratica ($Y = X^2$). Solo per le Gaussiane $\rho=0 \implies$ Indipendenza totale.

## Convoluzione e Somma di Variabili
> [!ABSTRACT] 
> Quando sommi due variabili aleatorie indipendenti ($Z = X + Y$), le loro densità di probabilità si fondono tramite l'operatore di convoluzione.
> [!QUOTE] 
> Convoluzione: $f_Z(z) = (f_X * f_Y)(z) = \int f_X(x) f_Y(z-x) dx$.
> [!EXAMPLE] 
> Se lanci due dadi (discrete uniformi), la probabilità della somma ha una forma triangolare (convoluzione di due rettangoli). Se sommi tre rettangoli diventa quasi una campana di Gauss.

- Nodo Passaggio nel dominio Trasformato: Usando la Trasformata di Laplace, la convoluzione diventa un semplice prodotto algebrico: $\mathcal{L}\{f * g\} = \mathcal{L}\{f\} \cdot \mathcal{L}\{g\}$.

## Processi Stocastici e Processi di Poisson
> [!ABSTRACT] 
> Un processo stocastico $X(t)$ è un insieme infinito di variabili aleatorie indicizzate dal tempo. Aggiunge una dimensione all'aleatorietà.
> [!QUOTE] 
> Realizzazione: Fissando l'aleatorietà $\omega$, si ottiene un normale segnale $x(t)$.
> Stazionarietà: Le proprietà statistiche (media, varianza) sono costanti e indipendenti dalla traslazione temporale.
> Processo di Poisson: Conta gli eventi nel tempo. Ha incrementi indipendenti e stazionari, e tempi d'attesa distribuiti esponenzialmente.

- Nodo Amnesia Totale: Il processo di Poisson non ha memoria, ed è la pietra angolare della teoria delle code e dell'affidabilità.

## Il Miracolo Matematico: Teorema Centrale del Limite (TCL)
> [!ABSTRACT] 
> Il TCL spiega perché l'Universo è gaussiano. Quando un fenomeno macroscopico è il risultato della somma di innumerevoli fenomeni microscopici microscopici indipendenti, la distribuzione complessiva tende inesorabilmente a una curva a campana, indipendentemente dalla natura dei microscopici.
> [!QUOTE] 
> Siano $X_i$ variabili i.i.d. con media $\mu$ e varianza $\sigma^2$. La somma normalizzata converge in distribuzione a $\mathcal{N}(0,1)$:
> $$Z_n = \frac{\sum X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$
> [!DANGER] 
> La convergenza dipende dalla varianza, ma richiede che questa sia FINITA. Se sommiamo infinite variabili di Cauchy (varianza infinita), il teorema crolla miseramente e la curva non diventerà mai gaussiana.

- Nodo Attrazione: La Gaussiana è il buco nero delle distribuzioni. Tutte le distribuzioni convolute infinite volte collassano dentro di essa.

---

# 🔴 PILASTRO VI — Statistica Inferenziale e Teoria delle Decisioni

## Convergenza e Legge dei Grandi Numeri
> [!ABSTRACT] 
> L'Inferenza fa il percorso inverso: dai campioni cerca di ricostruire il modello generativo nascosto. La garanzia matematica che questo funzioni è data dai teoremi asintotici.
> [!QUOTE] 
> Tipi di Convergenza: In Distribuzione (es. TCL), In Probabilità (Legge Debole), In Media Quadratica (implica la convergenza in probabilità), Quasi-Certamente (Legge Forte).
> Legge Debole dei Grandi Numeri: La media campionaria converge in probabilità alla media statistica: $\bar{X}_n \xrightarrow{P} E[X]$.

- Nodo Ergodicità: La frequenza empirica diventerà inevitabilmente la probabilità teorica se campioni abbastanza a lungo.

## Classificazione Bayesiana, ML e MAP
> [!ABSTRACT] 
> Il Rischio Medio Bayesiano definisce la penalità degli errori decisionali. Minimizzare il costo di un errore equivale a ottimizzare le soglie.
> [!QUOTE] 
> MAP (Maximum A Posteriori): Decido per l'ipotesi con la probabilità a posteriori più alta date le osservazioni.
> ML (Maximum Likelihood): Se le probabilità a priori $\pi_i$ sono equiprobabili (la natura non ha preferenze), MAP collassa nella Massima Verosimiglianza.
> [!EXAMPLE] 
> Classificazione di Sorgenti Binarie: Per distinguere due monete con $p_1 > p_2$, il Likelihood Ratio Test (LRT) si riduce a contare il numero di '1' (peso di Hamming $w_H$) e confrontarlo con una soglia dipendente dal numero di lanci.

- Nodo Rasoio di Occam: La regola MAP sposta le soglie di decisione a favore dell'evento che è a priori più probabile.

## Test di Ipotesi Continui (Media e Varianza) e Neyman-Pearson
> [!ABSTRACT] 
> Nel mondo reale spesso non conosciamo i costi né le probabilità a priori delle minacce (es. attacco missilistico, radar). Neyman-Pearson offre un framework basato sul controllo rigido dei Falsi Allarmi.
> [!QUOTE] 
> Errore di I Specie (Falso Allarme - $P_{FA} = \alpha$): Dire che c'è segnale quando c'è solo rumore.
> Errore di II Specie (Mancata Rivelazione - $P_M = \beta$): Dire che c'è rumore quando in realtà c'è un segnale (fatale).
> Potenza del Test (Detection - $P_D = 1-\beta$).
> Lemma di Neyman-Pearson: Il LRT $L(\mathbf{x}) \geq \eta$ è il test più potente (massimizza $P_D$) per un dato livello tollerabile di $P_{FA} \leq \alpha_0$.
> [!EXAMPLE] 
> Test di Ipotesi su media Gaussiana (LRT): Per decidere se le osservazioni provengono da una media $\mu_1$ o $\mu_2$, è inutile testare tutti gli $n$ campioni. Il test collassa nella sola *Media Campionaria* (Statistica Sufficiente). Tutto il resto è rumore ignorabile.

- Nodo Trade-off fatale: Aumentare la potenza (ridurre le mancate rivelazioni) aumenta sempre inevitabilmente i falsi allarmi. Non esiste il pranzo gratis.
- Nodo Rumore Laplaciano e Soglie: Se la soglia del rapporto di verosimiglianza eccede il limite strutturale del segnale, il decisore andrà in cecità totale (rifiuterà sempre di dichiarare il segnale, assumendo tutto rumore).

## Stima Parametrica Bayesiana: MMSE vs MAP
> [!ABSTRACT] 
> Quando il parametro $\theta$ da indovinare è continuo, la probabilità di indovinarlo esattamente è zero. Cambiamo obiettivo: minimizziamo l'errore quadratico medio (MSE) o troviamo il punto più probabile.
> [!QUOTE] 
> Stimatore MAP (Maximum A Posteriori): Il picco (moda) della densità a posteriori. Risponde a "qual è il valore più probabile della natura?".
> Stimatore MMSE (Minimum Mean Square Error): La media condizionata a posteriori $E[\theta | \mathbf{x}^n]$. Risponde a "quale stima riduce al minimo l'errore quadratico complessivo?".
> Bias (Polarizzazione): $B(\theta) = E[\hat{\theta} | \theta] - \theta$.
> Consistenza: Un buon stimatore deve avere la varianza che decade a zero asintoticamente.
> [!EXAMPLE] 
> Moneta Truccata (Beta-Binomiale): Usando la MAP, la stima della probabilità $p$ è pari esattamente alla frequenza empirica $w_H/n$ (Unbiased). Usando la MMSE, viene $(w_H+1)/(n+2)$ (Biased ma a minor varianza, *Regola di Laplace*). Entrambi sono asintoticamente consistenti.

- Nodo Baricentro vs Cima: Il MAP si posiziona sulla vetta del monte (più facile da calcolare tramite derivata). L'MMSE cerca il baricentro del monte (richiede l'integrale). L'MMSE garantirà sempre (per definizione) l'errore quadratico medio inferiore.
---
