# Metodi Statistici dell'Informazione

**Corso di Laurea in Informatica — 6 CFU**  
**Docente:** Prof. Marco Lops

---

## Indice

### Parte I — Fondamenti di Probabilità

1. **Spazi di Probabilità e Assiomi**
   - 1.1 Spazio dei Campioni ed Eventi
   - 1.2 Algebra e σ-Algebra
   - 1.3 Assiomi di Kolmogorov
   - 1.4 Proprietà Derivate dagli Assiomi

2. **Analisi Combinatoria**
   - 2.1 Principio del Prodotto Cartesiano
   - 2.2 Disposizioni e Permutazioni
   - 2.3 Combinazioni e Coefficiente Binomiale
   - 2.4 Coefficiente Multinomiale

3. **Probabilità Condizionata e Indipendenza**
   - 3.1 Definizione di Probabilità Condizionata
   - 3.2 Teorema di Bayes
   - 3.3 Legge della Probabilità Totale
   - 3.4 Indipendenza Stocastica

### Parte II — Variabili Aleatorie Discrete

4. **Variabili Aleatorie Discrete**
   - 4.1 Definizione e PMF
   - 4.2 Funzioni di Variabili Aleatorie
   - 4.3 Valore Atteso e Momenti
   - 4.4 Varianza e Deviazione Standard

5. **Distribuzioni Discrete Notevoli**
   - 5.1 Distribuzione di Bernoulli
   - 5.2 Distribuzione Binomiale
   - 5.3 Distribuzione Uniforme Discreta
   - 5.4 Distribuzione di Poisson
   - 5.5 Distribuzione Geometrica

6. **Coppie di Variabili Aleatorie**
   - 6.1 PMF Congiunta e Marginalizzazione
   - 6.2 Indipendenza Statistica
   - 6.3 PMF Condizionata
   - 6.4 Covarianza e Correlazione
   - 6.5 Matrice di Covarianza

7. **Disuguaglianze Probabilistiche**
   - 7.1 Disuguaglianza di Markov
   - 7.2 Disuguaglianza di Chebyshev
   - 7.3 Legge dei Grandi Numeri

### Parte III — Variabili Aleatorie Continue

8. **Funzioni di Distribuzione e Densità**
   - 8.1 CDF: Definizione e Proprietà
   - 8.2 PDF: Derivazione dalla CDF
   - 8.3 Valore Atteso nel Caso Continuo
   - 8.4 Trasformazione di Densità

9. **Distribuzioni Continue Notevoli**
   - 9.1 Distribuzione Uniforme Continua
   - 9.2 Distribuzione Esponenziale
   - 9.3 Distribuzione di Laplace
   - 9.4 Distribuzione Gaussiana (cenni)

10. **Variabili Continue Bivariate**
    - 10.1 PDF Congiunta e CDF Congiunta
    - 10.2 Densità Marginali
    - 10.3 Densità Condizionata
    - 10.4 Indipendenza nel Caso Continuo

### Parte IV — Teoria dell'Informazione (Cenni)

11. **Entropia e Informazione**
    - 11.1 Misura dell'Informazione
    - 11.2 Entropia di Shannon
    - 11.3 Applicazioni alla Compressione

### Parte V — Processi Aleatori (Introduzione)

12. **Processi Stocastici**
    - 12.1 Definizione e Realizzazioni
    - 12.2 Processi in Tempo Discreto e Continuo
    - 12.3 Stazionarietà
    - 12.4 Processi di Poisson e Gaussiani

### Appendici

A. **Richiami di Calcolo**
B. **Tavole di Distribuzioni**
C. **Esercizi Svolti Completi**

---

# Parte I — Fondamenti di Probabilità

## Capitolo 1: Spazi di Probabilità e Assiomi

### 1.1 Spazio dei Campioni ed Eventi

> **Perché la Probabilità per l'Informatica?**
>
> Telecomunicazioni e informatica trattano entrambe lo stesso oggetto: l'**informazione**. Le telecomunicazioni la trasferiscono *nello spazio* (da un luogo a un altro); l'informatica la trasferisce *nel tempo* (memorizzazione, compressione, correzione degli errori).
>
> Intrinseco nel concetto di informazione c'è l'**incertezza**: se non c'è incertezza su ciò che viene trasmesso, non c'è informazione da trasmettere. La **probabilità** è lo strumento formale per modellare l'incertezza.

---

#### Definizione 1.1 (Esperimento)

Un **esperimento** è un'operazione (o insieme di operazioni) che conduce a **uno tra tanti risultati possibili**.

---

#### Definizione 1.2 (Spazio dei Campioni)

Lo **spazio dei campioni** (o *sample space*), denotato con $\Omega$, è l'insieme di **tutti i possibili risultati** di un esperimento.

$$\Omega = \{\omega_1, \omega_2, \ldots\}$$

Lo spazio dei campioni può essere:

- **Finito:** $|\Omega| < \infty$
  - *Esempio:* Lancio di una moneta → $\Omega = \{T, C\}$
  
- **Numerabilmente infinito:** $|\Omega| = \aleph_0$
  - *Esempio:* Numero di pacchetti in coda → $\Omega = \mathbb{N}_0$
  
- **Non numerabile (continuo):** $|\Omega| = \mathfrak{c}$
  - *Esempio:* Tensione ai capi di una resistenza → $\Omega = \mathbb{R}$

---

#### Definizione 1.3 (Evento)

Un **evento** è un **sottoinsieme** di $\Omega$ definito da una proposizione.

Un **evento elementare** è un singolo elemento di $\Omega$.

---

**Osservazione 1.4 (Non unicità della proposizione)**

L'evento è univocamente determinato dagli elementi di $\Omega$ che lo compongono, ma la proposizione che lo descrive **non è univoca**.

> **Esempio:**
> Considerando $\Omega = \{1, 2, 3, 4, 5\}$ (euro in tasca), l'evento $\{1, 3, 5\}$ può essere descritto come:
> - "ho un numero dispari di euro"
> - "non ho un numero pari di euro"
> - "ho 1 o 3 o 5 euro"
>
> Saper **riformulare** la proposizione in modo conveniente è fondamentale per risolvere problemi.

---

#### Nomenclatura degli Eventi

| Nome | Definizione | Notazione |
|------|-------------|-----------|
| **Evento certo** | $\Omega$ stesso | $\Omega$ |
| **Evento impossibile** | Insieme vuoto | $\emptyset$ |
| **Evento complementare** | Elementi di $\Omega$ non in $A$ | $A^c$ o $\bar{A}$ |
| **Eventi incompatibili** | $A \cap B = \emptyset$ | — |
| **$A$ implica $B$** | $A \subseteq B$ | $A \subseteq B$ |

---

**Esempio 1.5 (Implicazione tra eventi)**

Consideriamo il lancio di un dado. Siano:
- $A$ = "esce 2"
- $B$ = "esce un numero pari"

Allora $A \subseteq B$: se esce 2, certamente è uscito un pari. Ma se esce un pari, non è detto che sia 2 (potrebbe essere 4 o 6).

---

### 1.2 Algebra e σ-Algebra

Per definire rigorosamente la probabilità, è necessario specificare su quale classe di sottoinsiemi di $\Omega$ la funzione di probabilità è definita.

---

#### Definizione 1.6 (Algebra di eventi)

Una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$ si chiama **algebra** se soddisfa:

1. **Chiusura rispetto all'unione finita:** Se $A_i \in \mathcal{E}$ e $A_j \in \mathcal{E}$, allora $A_i \cup A_j \in \mathcal{E}$

2. **Chiusura rispetto alla complementazione:** Se $A_i \in \mathcal{E}$, allora $A_i^c \in \mathcal{E}$

---

**Proposizione 1.7 (Chiusura rispetto all'intersezione)**

Un'algebra è chiusa anche rispetto all'intersezione.

*Dimostrazione:*

Per le leggi di De Morgan:
$$(A \cup B)^c = A^c \cap B^c$$

Complementando entrambi i membri:
$$A \cap B = (A^c \cup B^c)^c$$

Se $A, B \in \mathcal{E}$:
1. $A^c, B^c \in \mathcal{E}$ (chiusura per complementazione)
2. $A^c \cup B^c \in \mathcal{E}$ (chiusura per unione)
3. $(A^c \cup B^c)^c \in \mathcal{E}$ (chiusura per complementazione)

Quindi $A \cap B \in \mathcal{E}$. □

---

**Proposizione 1.8 (Chiusura rispetto alla differenza)**

Un'algebra è chiusa rispetto alla differenza insiemistica.

*Dimostrazione:*

$$A \setminus B = A \cap B^c$$

Poiché $B^c \in \mathcal{E}$ (chiusura per complementazione) e l'intersezione è chiusa (Proposizione 1.7), segue che $A \setminus B \in \mathcal{E}$. □

---

**Esempio 1.9 (Algebra minimale)**

Sia $\Omega = \{1,2,3,4,5,6\}$ (dado) e $A = \{2,4,6\}$ (risultato pari). La più piccola algebra che contiene $A$ è:

$$\mathcal{E}_{\min} = \{\emptyset, \Omega, A, A^c\}$$

Verifica:
- Contiene $A$ per costruzione
- Contiene $A^c = \{1,3,5\}$ (chiusura per complementazione)
- Contiene $A \cup A^c = \Omega$ (chiusura per unione)
- Contiene $\Omega^c = \emptyset$ (chiusura per complementazione)

Questa è la struttura minimale che rispetta gli assiomi di un'algebra.

---

#### Definizione 1.10 (σ-Algebra)

Un'algebra $\mathcal{E}$ si chiama **σ-algebra** se un'**unione numerabile** di suoi elementi è ancora un elemento dell'algebra:

$$A_1, A_2, A_3, \ldots \in \mathcal{E} \quad \Longrightarrow \quad \bigcup_{i=1}^{\infty} A_i \in \mathcal{E}$$

---

**Osservazione 1.11**

Un'algebra garantisce la chiusura per unioni **finite**. Una σ-algebra estende questa garanzia a unioni **numerabili** (infinite ma contabili). La distinzione è rilevante quando $\Omega$ è numerabile.

Se $\Omega$ è finito, ogni algebra è automaticamente una σ-algebra.

---

**Esempio 1.12 (Necessità della σ-algebra)**

Consideriamo il conteggio delle macchine su un'autostrada. Gli eventi elementari sono "nessuna macchina", "una macchina", "due macchine", ..., fino potenzialmente a infinito. Per ogni insieme numerabile di questi eventi dobbiamo poter fare l'unione. Se $\Omega$ è finito, le unioni finite sono sufficienti; la σ-algebra diventa necessaria quando $\Omega$ è numerabile.

---

### 1.3 Assiomi di Kolmogorov

---

#### Definizione 1.13 (Spazio di Probabilità)

Dato uno spazio dei campioni $\Omega$ e una σ-algebra $\mathcal{E}$, si definisce **legge di probabilità** una funzione

$$P : \mathcal{E} \to [0,1]$$

che soddisfa i seguenti **assiomi di Kolmogorov**:

1. **Assioma 1 (Non negatività):**
   $$P(A) \geq 0 \quad \forall A \in \mathcal{E}$$

2. **Assioma 2 (Normalizzazione):**
   $$P(\Omega) = 1$$

3. **Assioma 3 (Additività):**
   Se $A$ e $B$ sono eventi disgiunti ($A \cap B = \emptyset$):
   $$P(A \cup B) = P(A) + P(B)$$

4. **Assioma 3½ (σ-additività):**
   Se $\{A_i\}_{i=1}^{\infty}$ è una successione di eventi a due a due disgiunti:
   $$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

La terna $(\Omega, \mathcal{E}, P)$ prende il nome di **spazio di probabilità**.

---

**Osservazione 1.14**

La σ-algebra garantisce che tutte le operazioni insiemistiche (unione, intersezione, complementazione, differenza) restino nel dominio di definizione della funzione $P$. Senza questa struttura, non si potrebbe essere certi di poter calcolare $P$ su combinazioni arbitrarie di eventi.

---

### 1.4 Proprietà Derivate dagli Assiomi

Tutte le proprietà che seguono sono **teoremi** derivati esclusivamente dagli assiomi di Kolmogorov, senza alcun ricorso alla definizione frequentistica.

---

**Teorema 1.15 (Probabilità dell'evento impossibile)**

$$P(\emptyset) = 0$$

*Dimostrazione:*

L'insieme vuoto $\emptyset$ è il complemento di $\Omega$:

$$P(\emptyset) = P(\Omega^c) = 1 - P(\Omega) = 1 - 1 = 0$$

utilizzando la proprietà del complementare (Teorema 1.16). □

---

**Teorema 1.16 (Probabilità del complementare)**

$$P(A^c) = 1 - P(A)$$

*Dimostrazione:*

Gli eventi $A$ e $A^c$ sono disgiunti e la loro unione è $\Omega$:

$$A \cup A^c = \Omega, \quad A \cap A^c = \emptyset$$

Per l'Assioma 3 (additività) e l'Assioma 2 (normalizzazione):

$$P(A) + P(A^c) = P(A \cup A^c) = P(\Omega) = 1$$

Da cui $P(A^c) = 1 - P(A)$. □

---

**Teorema 1.17 (Probabilità della differenza)**

$$P(A \setminus B) = P(A) - P(A \cap B)$$

*Dimostrazione:*

Scriviamo $A$ come unione disgiunta utilizzando la proprietà distributiva:

$$A = A \cap \Omega = A \cap (B \cup B^c) = (A \cap B) \cup (A \cap B^c)$$

Gli insiemi $(A \cap B)$ e $(A \cap B^c)$ sono disgiunti:
- $(A \cap B)$ contiene elementi che appartengono sia ad $A$ che a $B$
- $(A \cap B^c) = A \setminus B$ contiene elementi che appartengono ad $A$ ma non a $B$

Per l'Assioma 3:

$$P(A) = P(A \cap B) + P(A \cap B^c)$$

Quindi:

$$P(A \setminus B) = P(A \cap B^c) = P(A) - P(A \cap B)$$

□

---

**Teorema 1.18 (Probabilità dell'unione)**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

*Dimostrazione:*

Possiamo scrivere:

$$A \cup B = A \cup (B \cap A^c)$$

dove $A$ e $B \cap A^c$ (gli elementi di $B$ che non appartengono ad $A$) sono disgiunti. Per l'Assioma 3:

$$P(A \cup B) = P(A) + P(B \cap A^c)$$

Dal Teorema 1.17 applicato a $B$:

$$P(B \cap A^c) = P(B \setminus A) = P(B) - P(A \cap B)$$

Sostituendo:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

□

---

**Corollario 1.19 (Subadditività)**

Per eventi qualsiasi (non necessariamente disgiunti):

$$P(A \cup B) \leq P(A) + P(B)$$

con uguaglianza se e solo se $A \cap B = \emptyset$.

---

## Capitolo 2: Analisi Combinatoria

Quando lo spazio dei campioni è **finito** e gli eventi sono **equiprobabili**, calcolare la probabilità si riduce al **conteggio**:

$$P(A) = \frac{|A|}{|\Omega|}$$

L'analisi combinatoria fornisce gli strumenti per determinare efficientemente $|A|$ e $|\Omega|$.

---

### 2.1 Principio del Prodotto Cartesiano

---

**Teorema 2.1 (Cardinalità del prodotto cartesiano)**

Dati $k$ insiemi $A_1, A_2, \ldots, A_k$ con $|A_i| = n_i$:

$$|A_1 \times A_2 \times \cdots \times A_k| = \prod_{i=1}^{k} n_i$$

Questa è la **formula base** da cui derivano tutti i risultati di analisi combinatoria.

---

### 2.2 Disposizioni e Permutazioni

---

#### Definizione 2.2 ($k$-uple ordinate con ripetizione)

Il numero di **sequenze ordinate di lunghezza $k$** scelte da un alfabeto di $n$ simboli, **con la possibilità di ripetere** lo stesso simbolo, è:

$$\boxed{D_{n,k}^{\text{rep}} = n^k}$$

**Ragionamento:** Per ogni delle $k$ posizioni si sceglie uno dei $n$ simboli indipendentemente. Totale: $\underbrace{n \times n \times \cdots \times n}_{k \text{ volte}} = n^k$.

---

**Esempio 2.3**

Stringhe binarie di lunghezza 5: $D_{2,5}^{\text{rep}} = 2^5 = 32$.

---

#### Definizione 2.4 ($k$-uple ordinate senza ripetizione — Disposizioni semplici)

Il numero di **sequenze ordinate di lunghezza $k$** scelte da un insieme di $n$ elementi **senza ripetizione** (elementi distinti), è:

$$\boxed{D_{n,k} = \frac{n!}{(n-k)!} = n(n-1)(n-2)\cdots(n-k+1)}$$

**Ragionamento:** Per la prima posizione si sceglie uno dei $n$ elementi; per la seconda, uno dei $n-1$ rimanenti; ...; per la $k$-esima posizione restano $n-k+1$ scelte.

---

**Esempio 2.5**

Codice PIN di 3 cifre distinte da 0-9: $D_{10,3} = \frac{10!}{7!} = 10 \times 9 \times 8 = 720$.

---

#### Definizione 2.6 (Permutazioni)

Le **permutazioni** di $n$ elementi sono tutte le $n$-uple ordinate senza ripetizione degli $n$ elementi stessi:

$$\boxed{P_n = n!}$$

Le permutazioni corrispondono al caso particolare $k = n$ delle disposizioni semplici.

---

### 2.3 Combinazioni e Coefficiente Binomiale

---

#### Definizione 2.7 ($k$-uple non ordinate — Combinazioni semplici)

Il numero di **sottoinsiemi non ordinati di dimensione $k$** scelti da un insieme di $n$ elementi è:

$$\boxed{\binom{n}{k} = \frac{n!}{k!(n-k)!}}$$

**Ragionamento:** Le disposizioni semplici $D_{n,k}$ contano le sequenze ordinate. Se l'ordine non importa (sono sottoinsiemi), ogni sottoinsieme di $k$ elementi corrisponde a $k!$ sequenze ordinate diverse (permutazioni degli elementi del sottoinsieme). Quindi:

$$\binom{n}{k} = \frac{D_{n,k}}{k!} = \frac{n!}{k!(n-k)!}$$

Questo coefficiente è detto **coefficiente binomiale**.

---

**Esempio 2.8 (Mani di poker)**

Mazzo da 52 carte, mano di 5 carte:

$$\binom{52}{5} = \frac{52!}{5! \cdot 47!} = 2.598.960$$

---

**Proposizione 2.9 (Interpretazione combinatoria del coefficiente binomiale)**

Il numero di sequenze binarie di lunghezza $n$ con esattamente $k$ uni (e $n-k$ zeri) è:

$$\binom{n}{k}$$

*Dimostrazione:*

Se tutti i bit fossero distinti, ci sarebbero $n!$ permutazioni. Ma nella sequenza ci sono $k$ uni (indistinguibili tra loro) e $n-k$ zeri (indistinguibili tra loro). Le $k!$ permutazioni degli uni tra di loro danno la stessa sequenza, e lo stesso vale per le $(n-k)!$ permutazioni degli zeri. Quindi:

$$\left|\{x \in \{0,1\}^n : |x|_1 = k\}\right| = \frac{n!}{k! \cdot (n-k)!} = \binom{n}{k}$$

□

---

**Teorema 2.10 (Binomio di Newton)**

$$\boxed{(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}}$$

---

**Applicazione 2.11 (Cardinalità dell'insieme delle parti)**

Dato un insieme $A$ con $m$ elementi, l'**insieme delle parti** $\mathcal{P}(A)$ (l'insieme di tutti i sottoinsiemi di $A$, inclusi $\emptyset$ e $A$ stesso) ha cardinalità:

$$|\mathcal{P}(A)| = 2^m$$

*Dimostrazione:*

I sottoinsiemi di $A$ di cardinalità $k$ sono esattamente $\binom{m}{k}$. Sommando su tutti i possibili $k$:

$$|\mathcal{P}(A)| = \sum_{k=0}^{m} \binom{m}{k} = \sum_{k=0}^{m} \binom{m}{k} 1^k \cdot 1^{m-k} = (1+1)^m = 2^m$$

utilizzando il Binomio di Newton con $a = b = 1$. □

---

### 2.4 Coefficiente Multinomiale

---

**Teorema 2.12 (Coefficiente multinomiale)**

Data una sequenza di lunghezza $n$ su un alfabeto di $m$ simboli, con $n_i$ occorrenze del simbolo $i$ (con $\sum_{i=1}^m n_i = n$), il numero di sequenze distinte è:

$$\boxed{\binom{n}{n_1, n_2, \ldots, n_m} = \frac{n!}{n_1! \cdot n_2! \cdots n_m!}}$$

Questo è il **coefficiente multinomiale**, generalizzazione del binomiale al caso di più di due simboli.

---

### Riepilogo delle Formule Fondamentali

| Tipo | Formula | Nome |
|------|---------|------|
| $k$-uple ordinate **con** ripetizione | $n^k$ | — |
| $k$-uple ordinate **senza** ripetizione | $\dfrac{n!}{(n-k)!}$ | Disposizioni semplici |
| Permutazioni ($k=n$, senza ripetizione) | $n!$ | Permutazioni |
| $k$-uple **non** ordinate senza ripetizione | $\dbinom{n}{k} = \dfrac{n!}{k!(n-k)!}$ | Combinazioni / Coeff. binomiale |
| Sequenze di $n$ elementi con $n_i$ ripetizioni del tipo $i$ | $\dfrac{n!}{n_1! \cdots n_m!}$ | Coefficiente multinomiale |

---

**Esempio 2.13 (Probabilità di "colore" al poker)**

Mazzo francese da 52 carte, si estraggono 5 carte.

$$|\Omega| = \binom{52}{5}$$

**Colore (flush):** tutte e 5 le carte dello stesso seme. Ci sono 4 semi e 13 carte per seme:

$$|A_{\text{colore}}| = 4 \cdot \binom{13}{5}$$

$$P(\text{colore}) = \frac{4 \cdot \binom{13}{5}}{\binom{52}{5}} \approx 0.00198$$

---

## Capitolo 3: Probabilità Condizionata e Indipendenza

### 3.1 Definizione di Probabilità Condizionata

---

**Intuizione 3.1 (Il database)**

Immaginiamo un database con tutti i residenti in Italia, con colonne altezza, peso, colore occhi.

- $P(\text{peso} \geq 70 \text{ kg})$: conto quanti pesano almeno 70 kg, divido per il totale.

- $P(\text{peso} \geq 70 \text{ kg} \mid \text{altezza} \geq 170 \text{ cm})$: **restringo il database** alle sole persone alte almeno 170 cm (elimino tutti gli altri), poi conto quanti di questi pesano almeno 70 kg, divido per la dimensione del database ristretto.

Il condizionamento cambia lo spazio dei campioni: da $\Omega$ si passa ad $A$ come nuovo universo di riferimento.

---

#### Definizione 3.2 (Probabilità condizionata)

Dato un evento $B$ con $P(B) > 0$, la **probabilità condizionata** di $A$ dato $B$ è:

$$\boxed{P(A \mid B) = \frac{P(A \cap B)}{P(B)}}$$

---

**Teorema 3.3 (Legge della probabilità composta)**

$$\boxed{P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)}$$

*Dimostrazione:*

Diretta dalla definizione di probabilità condizionata, moltiplicando entrambi i membri per $P(B)$ (risp. $P(A)$). □

---

**Proposizione 3.4 (La probabilità condizionata è una legge di probabilità)**

Fissato $B$ con $P(B) > 0$, la funzione $P(\cdot \mid B)$ soddisfa gli assiomi di Kolmogorov ed è quindi una legge di probabilità a tutti gli effetti.

*Dimostrazione:*

**Assioma 1 (Non negatività):**

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \geq 0$$

poiché rapporto di due quantità non negative.

**Assioma 2 (Normalizzazione):**

$$P(\Omega \mid B) = \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1$$

**Assioma 3 (σ-additività):**

Siano $A$ e $C$ eventi disgiunti ($A \cap C = \emptyset$):

$$P(A \cup C \mid B) = \frac{P\big((A \cup C) \cap B\big)}{P(B)} = \frac{P\big((A \cap B) \cup (C \cap B)\big)}{P(B)}$$

Poiché $A \cap C = \emptyset$ implica che $(A \cap B)$ e $(C \cap B)$ sono disgiunti:

$$= \frac{P(A \cap B) + P(C \cap B)}{P(B)} = \frac{P(A \cap B)}{P(B)} + \frac{P(C \cap B)}{P(B)} = P(A \mid B) + P(C \mid B)$$

□

---

### 3.2 Teorema di Bayes

---

**Teorema 3.5 (Legge di Bayes)**

$$\boxed{P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}}$$

*Dimostrazione:*

Dalla legge della probabilità composta (Teorema 3.3):

$$P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$$

Dividendo per $P(A)$ (assumendo $P(A) > 0$):

$$P(B \mid A) = \frac{P(B) \cdot P(A \mid B)}{P(A)}$$

□

---

**Interpretazione 3.6**

La legge di Bayes permette di **invertire** la direzione del condizionamento, aggiornando la conoscenza *a priori* di un fenomeno ($P(B)$) alla luce di nuove evidenze sperimentali ($A$), determinando la probabilità *a posteriori* ($P(B \mid A)$).

---

### 3.3 Legge della Probabilità Totale

---

#### Definizione 3.7 (Partizione)

Una collezione di $m$ sottoinsiemi $\{E_1, E_2, \ldots, E_m\}$ è una **partizione** di $\Omega$ se:

1. Sono a due a due disgiunti: $E_i \cap E_j = \emptyset$ per $i \neq j$
2. La loro unione è l'intero spazio: $\bigcup_{i=1}^{m} E_i = \Omega$

---

**Teorema 3.8 (Legge della probabilità totale)**

Data una partizione $\{E_1, E_2, \ldots, E_m\}$ di $\Omega$:

$$\boxed{P(A) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)}$$

*Dimostrazione:*

Per la proprietà distributiva:

$$A = A \cap \Omega = A \cap \left(\bigcup_{i=1}^{m} E_i\right) = \bigcup_{i=1}^{m} (A \cap E_i)$$

Gli insiemi $A \cap E_i$ e $A \cap E_j$ (con $i \neq j$) sono disgiunti perché $E_i \cap E_j = \emptyset$. Quindi:

$$P(A) = \sum_{i=1}^{m} P(A \cap E_i) = \sum_{i=1}^{m} P(A \mid E_i) \cdot P(E_i)$$

utilizzando la legge della probabilità composta. □

---

**Osservazione 3.9**

La legge della probabilità totale permette di scomporre il calcolo di $P(A)$ condizionando rispetto a una partizione dello spazio campionario, riducendo un problema complesso a calcoli più semplici.

---

### 3.4 Indipendenza Stocastica

---

#### Definizione 3.10 (Indipendenza statistica)

Due eventi $A, B \in \mathcal{E}$ si dicono **statisticamente indipendenti** se:

$$\boxed{P(A \cap B) = P(A) \cdot P(B)}$$

---

**Proposizione 3.11 (Caratterizzazione alternativa)**

Se $P(B) > 0$, allora $A$ e $B$ sono indipendenti se e solo se:

$$P(A \mid B) = P(A)$$

*Dimostrazione:*

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A) \cdot P(B)}{P(B)} = P(A)$$

□

Il verificarsi di $B$ **non fornisce alcuna informazione** sul verificarsi di $A$: la probabilità condizionata coincide con quella incondizionata.

---

**Teorema 3.12 (Indipendenza dei complementari)**

Se $A$ e $B$ sono statisticamente indipendenti, allora anche $A^c$ e $B^c$ sono statisticamente indipendenti.

*Dimostrazione:*

Per le leggi di De Morgan:

$$A^c \cap B^c = (A \cup B)^c$$

Quindi:

$$P(A^c \cap B^c) = P\big((A \cup B)^c\big) = 1 - P(A \cup B)$$

Sostituendo la formula dell'unione (Teorema 1.18):

$$= 1 - P(A) - P(B) + P(A \cap B)$$

Poiché $A$ e $B$ sono indipendenti, $P(A \cap B) = P(A) \cdot P(B)$:

$$= 1 - P(A) - P(B) + P(A) \cdot P(B)$$

Raccogliendo:

$$= 1 - P(A) - P(B)(1 - P(A)) = \big(1 - P(A)\big)\big(1 - P(B)\big) = P(A^c) \cdot P(B^c)$$

□

---

#### Definizione 3.13 (Indipendenza di $n$ eventi)

Gli eventi $A_1, A_2, \ldots, A_n$ sono **mutuamente indipendenti** se per ogni sottoinsieme $\{i_1, i_2, \ldots, i_k\} \subseteq \{1, \ldots, n\}$:

$$P(A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}) = P(A_{i_1}) \cdot P(A_{i_2}) \cdots P(A_{i_k})$$

---

**Osservazione 3.14 (Indipendenza a coppie vs congiunta)**

L'indipendenza a coppie (pairwise) **non implica** l'indipendenza congiunta.

---

**Esempio 3.15 (Bit di parità — Controesempio)**

Siano $X_1$ e $X_2$ due bit equiprobabili e indipendenti, ciascuno con valore $0$ o $1$ con probabilità $1/2$. Si definisce il **bit di parità**:

$$X_3 = X_1 \oplus X_2$$

dove $\oplus$ denota la somma modulo 2 (XOR): $X_3 = 0$ se $X_1$ e $X_2$ sono uguali, $X_3 = 1$ se sono diversi.

**Verifica dell'indipendenza a coppie:**

- $X_1$ e $X_2$ sono indipendenti per ipotesi
- $P(X_1 = 0, X_3 = 0) = P(X_1 = 0, X_2 = 0) = 1/4 = P(X_1 = 0) \cdot P(X_3 = 0)$ ✓
- Analogamente per le altre coppie

**La terna non è indipendente:**

Se si conoscono sia $X_1$ che $X_2$, il valore di $X_3$ è completamente determinato:

$$P(X_3 = 0 \mid X_1 = 0, X_2 = 0) = 1 \neq P(X_3 = 0) = 1/2$$

Quindi $P(X_1 = x_1, X_2 = x_2, X_3 = x_3) \neq P(X_1 = x_1) \cdot P(X_2 = x_2) \cdot P(X_3 = x_3)$.

---

# Parte II — Variabili Aleatorie Discrete

## Capitolo 4: Variabili Aleatorie Discrete

### 4.1 Definizione e PMF

---

**Motivazione 4.1**

Tre esperimenti apparentemente diversi:
1. Lancio di una moneta: testa o croce
2. Sorgente binaria: emette $0$ o $1$
3. Lancio di un dado: risultato pari o dispari

hanno tutti un esito **binario**. Codificando opportunamente (testa $\to 0$, croce $\to 1$; pari $\to 0$, dispari $\to 1$), si possono trattare in modo **unificato** attraverso un'applicazione che associa ad ogni esito dello spazio campione un valore numerico.

---

#### Definizione 4.2 (Variabile aleatoria discreta)

Dato uno spazio di probabilità $(\Omega, \mathcal{E}, P)$ discreto, una **variabile aleatoria** è un'applicazione

$$X : \Omega \to \mathcal{X}$$

dove $\mathcal{X}$ è un insieme numerico chiamato **alfabeto** della variabile aleatoria. La funzione $X$ associa ad ogni esito $\omega \in \Omega$ un valore numerico $X(\omega) \in \mathcal{X}$.

---

**Osservazione 4.3**

Per essere rigorosi, $X$ deve essere **misurabile**: l'anti-immagine di ogni evento concernente $X$ deve essere un elemento della σ-algebra. Questa condizione garantisce che si possa calcolare la probabilità che $X$ assuma certi valori.

---

#### Definizione 4.4 (PMF — Probability Mass Function)

Data una variabile aleatoria discreta $X$ con alfabeto $\mathcal{X} = \{x_1, x_2, \ldots, x_m\}$, la **PMF** è la sequenza:

$$p_X(x_i) = P(X = x_i), \quad i = 1, 2, \ldots, m$$

Una sequenza di $m$ numeri è una PMF valida se e solo se:

1. **Non negatività:** $p_X(x_i) \geq 0$ per ogni $i$ (Assioma 1 di Kolmogorov)
2. **Normalizzazione:** $\displaystyle\sum_{i=1}^{m} p_X(x_i) = 1$ (Assioma 2 di Kolmogorov)

---

**Esempio 4.5**

La sequenza $\left(\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8}\right)$ è una PMF valida:

$$\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} = \frac{4}{8} + \frac{2}{8} + \frac{1}{8} + \frac{1}{8} = \frac{8}{8} = 1 \quad \checkmark$$

Tutti i termini sono non negativi. ✓

---

### 4.2 Funzioni di Variabili Aleatorie

---

#### Definizione 4.6 (Trasformazione di variabile aleatoria)

Se $X$ è una variabile aleatoria e $g : \mathcal{X} \to \mathcal{Y}$ è una funzione, allora $Y = g(X)$ è anch'essa una variabile aleatoria.

---

**Caso 1: Corrispondenza biiettiva**

Se $g$ è una biiezione (ogni valore di $X$ mappa in un valore distinto di $Y$), allora:

$$p_Y(g(x_i)) = p_X(x_i)$$

Si tratta di un semplice **reflagging dell'alfabeto**: le probabilità sono invariate, cambiano solo le etichette.

---

**Caso 2: Corrispondenza molti-a-uno**

Più valori di $X$ collassano in uno stesso valore di $Y$. Le probabilità corrispondenti si sommano:

$$\boxed{p_Y(y_k) = \sum_{\{x : g(x) = y_k\}} p_X(x)}$$

---

**Esempio 4.7**

$Y = |X|$, con $X \in \{-2,-1,1,2\}$ e $p_X = \{1/8, 1/4, 1/4, 3/8\}$.

$Y \in \{1, 2\}$.

$$p_Y(1) = p_X(-1) + p_X(1) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$

$$p_Y(2) = p_X(-2) + p_X(2) = \frac{1}{8} + \frac{3}{8} = \frac{1}{2}$$

Media:

$$E[Y] = 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{2} = \frac{3}{2}$$

---

### 4.3 Valore Atteso e Momenti

---

**Motivazione 4.8 (Dalla frequenza alla media)**

Supponiamo di ripetere un esperimento $n$ volte e di osservare i valori $x_1, x_2, \ldots, x_n$. La **media campionaria** è:

$$\bar{x}_n = \frac{1}{n} \sum_{i=1}^{n} x_i$$

Sia $\mathcal{X} = \{a_1, a_2, \ldots, a_M\}$ l'alfabeto di $X$. Se il valore $a_k$ compare $N_k$ volte nelle $n$ prove (dove $\sum_{k=1}^{M} N_k = n$), possiamo riscrivere:

$$\bar{x}_n = \frac{1}{n} \sum_{k=1}^{M} N_k \cdot a_k = \sum_{k=1}^{M} \frac{N_k}{n} \cdot a_k = \sum_{k=1}^{M} f_n(a_k) \cdot a_k$$

dove $f_n(a_k) = N_k / n$ è la frequenza relativa. Per la legge dei grandi numeri:

$$f_n(a_k) \xrightarrow{n \to \infty} P_X(a_k)$$

Quindi:

$$\bar{x}_n \xrightarrow{n \to \infty} \sum_{k=1}^{M} a_k \cdot P_X(a_k)$$

---

#### Definizione 4.9 (Valore atteso)

Sia $X$ una variabile aleatoria discreta con alfabeto $\mathcal{X} = \{a_1, a_2, \ldots, a_M\}$ e PMF $p_X$. Il **valore atteso** (o **media statistica**, o **speranza matematica**) di $X$ è:

$$\boxed{E[X] = \mu_X = \sum_{k=1}^{M} a_k \cdot p_X(a_k)}$$

Il simbolo $E[\cdot]$ si legge "valore atteso di"; $\mu_X$ è la notazione alternativa.

---

**Teorema 4.10 (Calcolo della media per funzioni di variabili aleatorie)**

Data una variabile aleatoria $X$ con PMF $p_X$ e una funzione $g$, la media di $Y = g(X)$ è:

$$\boxed{E[g(X)] = \sum_{x \in \mathcal{X}} g(x) \cdot p_X(x)}$$

indipendentemente dal fatto che $g$ sia biiettiva o molti-a-uno.

*Dimostrazione (caso molti-a-uno):*

I valori che collassano nello stesso punto di $Y$ hanno tutti lo stesso $g(x)$; la somma su $x$ è quindi equivalente alla somma su $y$ (le probabilità si sommano automaticamente). □

---

**Proposizione 4.11 (Linearità del valore atteso)**

Per costanti reali $a$ e $b$:

$$\boxed{E[aX + b] = a \cdot E[X] + b}$$

*Dimostrazione:*

$$E[aX + b] = \sum_{x \in \mathcal{X}} (ax + b) \cdot p_X(x) = a \sum_{x \in \mathcal{X}} x \cdot p_X(x) + b \sum_{x \in \mathcal{X}} p_X(x) = a \cdot E[X] + b \cdot 1$$

□

---

#### Definizione 4.12 (Momenti)

Il **momento di ordine $m$** di $X$ è:

$$E[X^m] = \sum_{x \in \mathcal{X}} x^m \cdot p_X(x)$$

Il **momento centrale di ordine $m$** è:

$$E[(X - \mu_X)^m]$$

---

### 4.4 Varianza e Deviazione Standard

---

#### Definizione 4.13 (Varianza)

La **varianza** di $X$ è:

$$\boxed{\sigma_X^2 = \text{Var}(X) = E\left[(X - \mu_X)^2\right] = \sum_{x \in \mathcal{X}} (x - \mu_X)^2 \cdot p_X(x)}$$

La **deviazione standard** è:

$$\sigma_X = \sqrt{\sigma_X^2}$$

---

**Teorema 4.14 (Formula alternativa per la varianza)**

$$\boxed{\sigma_X^2 = E[X^2] - \mu_X^2}$$

*Dimostrazione:*

$$E[(X-\mu_X)^2] = E[X^2 - 2\mu_X X + \mu_X^2] = E[X^2] - 2\mu_X E[X] + \mu_X^2 = E[X^2] - 2\mu_X^2 + \mu_X^2 = E[X^2] - \mu_X^2$$

□

---

**Teorema 4.15 (Proprietà della varianza rispetto a trasformazioni lineari)**

$$\boxed{\text{Var}(aX + b) = a^2 \cdot \text{Var}(X)}$$

*Dimostrazione:*

$$E[aX+b] = a\mu_X + b$$

$$\text{Var}(aX+b) = E\!\left[(aX+b - (a\mu_X + b))^2\right] = E\!\left[(a(X-\mu_X))^2\right] = a^2 E\!\left[(X-\mu_X)^2\right] = a^2\sigma_X^2$$

□

**Interpretazione:**

1. **Invarianza per traslazione:** Un termine additivo $b$ sposta la distribuzione ma non la allarga né la restringe
2. **Covarianza quadratica per scala:** Un fattore moltiplicativo $a$ scala la deviazione standard di $|a|$ e la varianza di $a^2$

---

**Definizione 4.16 (Valore quadratico medio)**

Il **valore quadratico medio** (root mean square, RMS) di $X$ è:

$$x_{\text{rms}} = \sqrt{E[X^2]}$$

Dalla formula alternativa della varianza:

$$E[X^2] = \sigma_X^2 + \mu_X^2$$

---

## Capitolo 5: Distribuzioni Discrete Notevoli

### 5.1 Distribuzione di Bernoulli

---

#### Definizione 5.1 (Variabile di Bernoulli)

Una variabile aleatoria $X$ segue una **distribuzione di Bernoulli** di parametro $p \in [0,1]$, scritto $X \sim \text{Ber}(p)$, se:

- Alfabeto: $\mathcal{X} = \{0, 1\}$
- PMF:

$$p_X(x) = \begin{cases} p & \text{se } x = 1 \\ 1-p & \text{se } x = 0 \end{cases}$$

**Forma compatta:**

$$p_X(x) = p^x (1-p)^{1-x}, \quad x \in \{0,1\}$$

---

**Proposizione 5.2 (Media della Bernoulli)**

$$E[X] = p$$

*Dimostrazione:*

$$E[X] = 0 \cdot (1-p) + 1 \cdot p = p$$

□

---

### 5.2 Distribuzione Binomiale

---

#### Definizione 5.3 (Variabile Binomiale)

Siano $X_1, X_2, \ldots, X_n$ variabili i.i.d. (indipendenti e identicamente distribuite) con $X_i \sim \text{Ber}(p)$. La variabile:

$$S_n = \sum_{i=1}^{n} X_i$$

conta il numero totale di successi in $n$ prove. Si dice che $S_n \sim \text{Bin}(n, p)$ con PMF:

$$\boxed{p_{S_n}(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n}$$

---

**Proposizione 5.4 (Verifica della normalizzazione)**

$$\sum_{k=0}^{n} p_{S_n}(k) = \sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = \big(p + (1-p)\big)^n = 1$$

utilizzando il Binomio di Newton. □

---

**Teorema 5.5 (Media della Binomiale)**

$$\boxed{E[S_n] = np}$$

*Dimostrazione (Metodo 1 — linearità):*

$$E[S_n] = E\left[\sum_{i=1}^{n} X_i\right] = \sum_{i=1}^{n} E[X_i] = \sum_{i=1}^{n} p = np$$

□

*Dimostrazione (Metodo 2 — calcolo diretto):*

$$E[S_n] = \sum_{k=0}^{n} k \cdot \binom{n}{k} p^k (1-p)^{n-k} = \sum_{k=1}^{n} k \cdot \frac{n!}{k!(n-k)!} p^k (1-p)^{n-k}$$

Semplificando $k$ con $k! = k \cdot (k-1)!$:

$$= np \sum_{k=1}^{n} \frac{(n-1)!}{(k-1)!(n-k)!} p^{k-1} (1-p)^{n-k}$$

Con il cambio di indice $j = k-1$ e $m = n-1$:

$$= np \sum_{j=0}^{m} \binom{m}{j} p^j (1-p)^{m-j} = np \cdot (p + (1-p))^m = np$$

□

---

### 5.3 Distribuzione Uniforme Discreta

---

#### Definizione 5.6 (Distribuzione Uniforme Discreta)

$X$ è **uniforme** su $\mathcal{X} = \{a_1, a_2, \ldots, a_M\}$ se:

$$p_X(a_k) = \frac{1}{M}, \quad k = 1, 2, \ldots, M$$

---

**Proposizione 5.7 (Media della Uniforme)**

$$E[X] = \frac{1}{M} \sum_{k=1}^{M} a_k = \frac{a_1 + a_2 + \cdots + a_M}{M}$$

La media coincide con la media aritmetica dell'alfabeto.

---

**Teorema 5.8 (Formula di Gauss)**

$$\sum_{k=1}^{M} k = \frac{M(M+1)}{2}$$

*Dimostrazione:*

Sia $S = 1 + 2 + \cdots + M$. Scriviamo:

$$S = 1 + 2 + \cdots + (M-1) + M$$
$$S = M + (M-1) + \cdots + 2 + 1$$

Sommando termine a termine:

$$2S = \underbrace{(M+1) + (M+1) + \cdots + (M+1)}_{M \text{ volte}} = M(M+1)$$

Quindi $S = \frac{M(M+1)}{2}$. □

---

**Corollario 5.9**

Per una variabile uniforme su $\{1, 2, \ldots, M\}$:

$$E[X] = \frac{M+1}{2}$$

---

### 5.4 Distribuzione di Poisson

---

#### Definizione 5.10 (Distribuzione di Poisson)

$X \sim \text{Poi}(\lambda)$ se:

- Alfabeto: $\mathcal{X} = \mathbb{N}_0 = \{0, 1, 2, \ldots\}$
- PMF:

$$\boxed{p_X(k) = \frac{\lambda^k}{k!} e^{-\lambda}, \quad k = 0, 1, 2, \ldots}$$

Il parametro $\lambda > 0$ rappresenta il **tasso medio** di occorrenze.

---

**Proposizione 5.11 (Verifica della normalizzazione)**

$$\sum_{k=0}^{\infty} p_X(k) = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^{\lambda} = 1$$

utilizzando lo sviluppo in serie di Taylor dell'esponenziale. □

---

**Teorema 5.12 (Media della Poisson)**

$$\boxed{E[X] = \lambda}$$

*Dimostrazione:*

$$E[X] = \sum_{k=0}^{\infty} k \cdot \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \sum_{k=1}^{\infty} k \cdot \frac{\lambda^k}{k!}$$

Semplificando $k$ con $k!$:

$$= e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!} = \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}$$

Con $j = k-1$:

$$= \lambda e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^{j}}{j!} = \lambda e^{-\lambda} \cdot e^{\lambda} = \lambda$$

□

---

**Teorema 5.13 (Approssimazione di Poisson alla Binomiale)**

Quando $n \to \infty$, $p \to 0$, con $np = \lambda$ costante:

$$\binom{n}{k} p^k (1-p)^{n-k} \to \frac{\lambda^k}{k!} e^{-\lambda}$$

---

### 5.5 Distribuzione Geometrica

---

#### Definizione 5.14 (Distribuzione Geometrica)

$X \sim \text{Geo}(p)$ rappresenta il numero di prove necessarie per ottenere il primo successo:

- Alfabeto: $\mathcal{X} = \{1, 2, 3, \ldots\}$
- PMF:

$$\boxed{p_X(k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots}$$

---

**Proposizione 5.15 (Verifica della normalizzazione)**

Sia $q = 1-p$. Per la serie geometrica con $|q| < 1$:

$$\sum_{k=1}^{\infty} p_X(k) = p \sum_{k=1}^{\infty} q^{k-1} = p \sum_{j=0}^{\infty} q^j = p \cdot \frac{1}{1-q} = p \cdot \frac{1}{p} = 1$$

□

---

**Teorema 5.16 (Media della Geometrica)**

$$\boxed{E[X] = \frac{1}{p}}$$

*Dimostrazione:*

$$E[X] = p \sum_{k=1}^{\infty} k \cdot q^{k-1}$$

Ricordando che:

$$\frac{d}{dq}\sum_{k=0}^{\infty} q^k = \sum_{k=1}^{\infty} k \cdot q^{k-1}$$

e che:

$$\frac{d}{dq}\left(\frac{1}{1-q}\right) = \frac{1}{(1-q)^2}$$

Quindi:

$$E[X] = p \cdot \frac{1}{(1-q)^2} = p \cdot \frac{1}{p^2} = \frac{1}{p}$$

□

---

**Proposizione 5.17 (Proprietà di assenza di memoria)**

$$P(X > n + m \mid X > n) = P(X > m)$$

per ogni $n, m \geq 0$.

La geometrica è l'**unica** distribuzione discreta con questa proprietà.

---

## Capitolo 6: Coppie di Variabili Aleatorie

### 6.1 PMF Congiunta e Marginalizzazione

---

#### Definizione 6.1 (Coppia di variabili aleatorie)

Una **coppia di variabili aleatorie** $(X, Y)$ è un'applicazione:

$$\omega \mapsto (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y}$$

---

#### Definizione 6.2 (PMF congiunta)

La **PMF congiunta** di $(X, Y)$ è:

$$p_{XY}(x, y) = P(X = x, Y = y), \quad \forall x \in \mathcal{X}, y \in \mathcal{Y}$$

Questa è una tabella di $|\mathcal{X}| \times |\mathcal{Y}|$ numeri non negativi che sommano a 1:

$$\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p_{XY}(x, y) = 1$$

---

**Definizione 6.3 (PMF marginali)**

$$\boxed{p_X(x) = \sum_{y \in \mathcal{Y}} p_{XY}(x, y)}$$

$$\boxed{p_Y(y) = \sum_{x \in \mathcal{X}} p_{XY}(x, y)}$$

*Dimostrazione:*

L'evento $\{X = x\}$ è l'unione disgiunta degli eventi $\{X = x, Y = y\}$ al variare di $y$. Per l'assioma di additività:

$$P(X=x) = \sum_y P(X=x, Y=y)$$

□

---

**Osservazione 6.4 (Asimmetria congiunta ↔ marginali)**

- Congiunta **implica** marginali: data la PMF congiunta, le marginali sono univocamente determinate
- Marginali **non implicano** congiunta: date le due PMF marginali, esistono in generale molte congiunte compatibili

L'unica eccezione è il caso di indipendenza statistica.

---

### 6.2 Indipendenza Statistica

---

#### Definizione 6.5 (Indipendenza per variabili aleatorie)

$X$ e $Y$ sono **statisticamente indipendenti** se e solo se:

$$\boxed{p_{XY}(x, y) = p_X(x) \cdot p_Y(y), \quad \forall x \in \mathcal{X}, y \in \mathcal{Y}}$$

---

**Osservazione 6.6**

Se la PMF congiunta si fattorizza come $p_{XY}(x, y) = g(x) \cdot h(y)$ per opportune funzioni $g, h \geq 0$, allora $X$ e $Y$ sono indipendenti.

*Dimostrazione:*

Siano $c_1 = \int g(x) dx$ e $c_2 = \int h(y) dy$ con $c_1 \cdot c_2 = 1$. Allora:

$$p_X(x) = \frac{g(x)}{c_1}, \quad p_Y(y) = \frac{h(y)}{c_2}$$

□

---

### 6.3 PMF Condizionata

---

#### Definizione 6.7 (PMF condizionale)

La **PMF condizionale di $X$ dato $Y$** è:

$$\boxed{p_{X|Y}(x|y) = P(X=x \mid Y=y) = \frac{p_{XY}(x,y)}{p_Y(y)}}$$

per ogni $y$ con $p_Y(y) > 0$.

---

**Proposizione 6.8**

Per ogni $y$ fissato, $\sum_{x \in \mathcal{X}} p_{X|Y}(x|y) = 1$ (è una legge di probabilità).

---

**Proposizione 6.9 (Relazione con l'indipendenza)**

Se $X$ e $Y$ sono indipendenti:

$$p_{X|Y}(x|y) = p_X(x)$$

Conoscere $Y$ non modifica la distribuzione di $X$.

---

**Teorema 6.10 (Regola della catena)**

Per tre variabili:

$$p_{XYZ}(x, y, z) = p_Z(z) \cdot p_{Y|Z}(y|z) \cdot p_{X|YZ}(x|y,z)$$

---

**Teorema 6.11 (Marginalizzazione come media)**

$$p_X(x) = \sum_{y \in \mathcal{Y}} p_{X|Y}(x|y) \cdot p_Y(y) = E_Y[p_{X|Y}(x|Y)]$$

La PMF marginale di $X$ è la **media rispetto a $Y$** della PMF condizionale.

---

**Teorema 6.12 (Media condizionale)**

$$\boxed{E[X] = \sum_{y \in \mathcal{Y}} E[X|Y=y] \cdot p_Y(y)}$$

---

### 6.4 Covarianza e Correlazione

---

#### Definizione 6.13 (Covarianza)

$$\boxed{\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - \mu_X \mu_Y}$$

---

**Proposizione 6.14**

Se $X$ e $Y$ sono indipendenti:

$$\text{Cov}(X, Y) = 0$$

*Dimostrazione:*

$$E[XY] = \sum_x \sum_y xy \cdot p_{XY}(x,y) = \sum_x \sum_y xy \cdot p_X(x) p_Y(y) = \left(\sum_x x p_X(x)\right)\left(\sum_y y p_Y(y)\right) = E[X]E[Y]$$

Quindi $\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = 0$. □

---

**Osservazione 6.15**

Incorrelazione ($\text{Cov}(X,Y) = 0$) **non implica** indipendenza, tranne nel caso gaussiano.

---

#### Definizione 6.16 (Coefficiente di correlazione)

$$\boxed{\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}}$$

---

**Teorema 6.17 (Limiti del coefficiente di correlazione)**

$$-1 \leq \rho_{XY} \leq 1$$

*Dimostrazione (Cauchy-Schwarz):*

L'insieme delle variabili aleatorie con varianza finita forma uno spazio vettoriale con prodotto scalare $\langle X', Y' \rangle = \text{Cov}(X, Y)$ e norma $\|X'\| = \sigma_X$. Per Cauchy-Schwarz:

$$|\langle X', Y' \rangle| \leq \|X'\| \cdot \|Y'\|$$

Quindi:

$$|\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y \implies |\rho_{XY}| \leq 1$$

□

**Uguaglianza:**

- $\rho_{XY} = 1$ sse $Y - \mu_Y = k(X - \mu_X)$ con $k > 0$ (relazione lineare diretta)
- $\rho_{XY} = -1$ sse $k < 0$ (relazione lineare inversa)

---

### 6.5 Matrice di Covarianza

---

#### Definizione 6.18 (Matrice di covarianza)

Per un vettore aleatorio $\mathbf{x} = (X_1, X_2, \ldots, X_n)^T$:

$$\boxed{K = E\!\left[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^T\right]}$$

dove $\boldsymbol{\mu} = E[\mathbf{x}]$.

Per $n=2$:

$$K = \begin{pmatrix} \sigma_{X_1}^2 & \text{Cov}(X_1, X_2) \\ \text{Cov}(X_1, X_2) & \sigma_{X_2}^2 \end{pmatrix}$$

---

**Proposizione 6.19**

La matrice di covarianza è:

1. **Simmetrica:** $K = K^T$
2. **Semidefinita positiva:** $\mathbf{a}^T K \mathbf{a} \geq 0$ per ogni vettore $\mathbf{a}$

---

## Capitolo 7: Disuguaglianze Probabilistiche

### 7.1 Disuguaglianza di Markov

---

**Teorema 7.1 (Disuguaglianza di Markov)**

Sia $X$ una variabile aleatoria **non negativa** con media finita $\mu_X = E[X]$. Per ogni $\delta > 0$:

$$\boxed{P(X \geq \delta) \leq \frac{E[X]}{\delta}}$$

*Dimostrazione:*

$$E[X] = \int_0^\infty x f_X(x) dx \geq \int_\delta^\infty x f_X(x) dx \geq \delta \int_\delta^\infty f_X(x) dx = \delta \cdot P(X \geq \delta)$$

Dividendo per $\delta$:

$$P(X \geq \delta) \leq \frac{E[X]}{\delta}$$

□

---

### 7.2 Disuguaglianza di Chebyshev

---

**Teorema 7.2 (Disuguaglianza di Chebyshev)**

Sia $X$ una variabile aleatoria con media $\mu_X$ e varianza $\sigma_X^2$ finita. Per ogni $k > 0$:

$$\boxed{P(|X - \mu_X| \geq k\sigma_X) \leq \frac{1}{k^2}}$$

Equivalentemente:

$$\boxed{P(|X - \mu_X| < k\sigma_X) \geq 1 - \frac{1}{k^2}}$$

*Dimostrazione:*

Applicando Markov a $Y = (X - \mu_X)^2$ (non negativa) con $\delta = (k\sigma_X)^2$:

$$P\big((X-\mu_X)^2 \geq (k\sigma_X)^2\big) \leq \frac{E[(X-\mu_X)^2]}{(k\sigma_X)^2} = \frac{\sigma_X^2}{k^2\sigma_X^2} = \frac{1}{k^2}$$

Prendendo la radice:

$$P(|X - \mu_X| \geq k\sigma_X) \leq \frac{1}{k^2}$$

□

---

**Interpretazione 7.3**

| $k$ | Limite superiore | Interpretazione |
|-----|------------------|-----------------|
| 2 | $P(\|X-\mu\| \geq 2\sigma) \leq 1/4$ | Al massimo 25% oltre 2σ |
| 3 | $P(\|X-\mu\| \geq 3\sigma) \leq 1/9$ | Al massimo 11% oltre 3σ |
| 10 | $P(\|X-\mu\| \geq 10\sigma) \leq 1/100$ | Al massimo 1% oltre 10σ |

---

### 7.3 Legge dei Grandi Numeri

---

**Definizione 7.4 (Frequenza di successo)**

Dati $n$ esperimenti indipendenti, la **frequenza di successo** dell'evento $A$ è:

$$F_n(A) = \frac{N_A(\omega)}{n}$$

dove $N_A(\omega)$ è il numero di occorrenze di $A$ in $n$ prove.

---

**Proposizione 7.5**

$N_A \sim \text{Bin}(n, P(A))$. Quindi:

$$E[F_n(A)] = P(A), \quad \text{Var}(F_n(A)) = \frac{P(A)(1-P(A))}{n}$$

---

**Teorema 7.6 (Legge Debole dei Grandi Numeri — Convergenza in probabilità)**

Per ogni $\varepsilon > 0$:

$$\lim_{n \to \infty} P(|F_n(A) - P(A)| > \varepsilon) = 0$$

*Dimostrazione:*

Per Chebyshev:

$$P(|F_n(A) - P(A)| > \varepsilon) \leq \frac{\text{Var}(F_n(A))}{\varepsilon^2} = \frac{P(A)(1-P(A))}{n\varepsilon^2} \xrightarrow{n \to \infty} 0$$

□

---

**Teorema 7.7 (Convergenza in media quadratica)**

$$\lim_{n \to \infty} E[(F_n(A) - P(A))^2] = \lim_{n \to \infty} \text{Var}(F_n(A)) = 0$$

---

**Osservazione 7.8**

La **Legge Forte dei Grandi Numeri** (convergenza con probabilità 1) afferma:

$$P\left(\lim_{n \to \infty} F_n(A) = P(A)\right) = 1$$

La dimostrazione esula dagli obiettivi del corso.

---

# Parte III — Variabili Aleatorie Continue

## Capitolo 8: Funzioni di Distribuzione e Densità

### 8.1 CDF: Definizione e Proprietà

---

**Motivazione 8.1**

Per una variabile aleatoria continua, la probabilità che assuma un valore esatto è zero:

$$P(X = x_0) = 0 \quad \forall x_0$$

La PMF (definita per valori discreti) non si può usare. Si lavora con probabilità di **intervalli**.

---

#### Definizione 8.2 (CDF — Cumulative Distribution Function)

La **funzione di distribuzione cumulativa** di $X$ è:

$$\boxed{F_X(x) = P(X \leq x) \quad \forall x \in \mathbb{R}}$$

Definita per **qualsiasi** variabile aleatoria, discreta o continua.

---

**Teorema 8.3 (Proprietà della CDF)**

1. **Valori agli estremi:** $F_X(-\infty) = 0$, $F_X(+\infty) = 1$

2. **Monotonia crescente:** Se $x_2 > x_1$, allora $F_X(x_2) \geq F_X(x_1)$

3. **Continuità a destra:** $\lim_{h \to 0^+} F_X(x+h) = F_X(x)$

4. **Probabilità di intervalli:**

$$P(a < X \leq b) = F_X(b) - F_X(a)$$

---

### 8.2 PDF: Derivazione dalla CDF

---

#### Definizione 8.4 (PDF — Probability Density Function)

Per variabili continue, la **densità di probabilità** è:

$$\boxed{f_X(x) = \frac{d}{dx} F_X(x)}$$

**Relazione inversa:**

$$\boxed{F_X(x) = \int_{-\infty}^{x} f_X(t) dt}$$

---

**Teorema 8.5 (Proprietà della PDF)**

1. **Non negatività:** $f_X(x) \geq 0$ per ogni $x$ (la CDF è monotona)

2. **Normalizzazione:**

$$\int_{-\infty}^{+\infty} f_X(x) dx = 1$$

3. **Probabilità di intervalli:**

$$P(a \leq X \leq b) = \int_a^b f_X(x) dx$$

---

**Osservazione 8.6**

La PDF **non è** una probabilità: può valere più di 1. La probabilità è l'**area** sotto la curva su un intervallo.

---

### 8.3 Valore Atteso nel Caso Continuo

---

**Derivazione 8.7 (Via quantizzazione)**

Dividiamo il supporto di $X$ in sottointervalli di ampiezza $\delta$ e approssimiamo con la variabile discreta $X_\delta$ che assume il valore centrale $x_i$ dell'$i$-esimo intervallo.

$$E[X_\delta] = \sum_i x_i \cdot P(X_\delta = x_i) = \sum_i x_i \cdot f_X(c_i) \cdot \delta$$

dove $c_i$ è un punto del sottointervallo per il teorema del valor medio. Questa è la somma di Riemann di $\int x f_X(x) dx$. Quando $\delta \to 0$:

$$E[X] = \int_{-\infty}^{+\infty} x f_X(x) dx$$

---

#### Definizione 8.8 (Valore atteso per variabili continue)

$$\boxed{E[X] = \int_{-\infty}^{+\infty} x f_X(x) dx}$$

---

**Teorema 8.9 (Calcolo della media per funzioni)**

$$\boxed{E[g(X)] = \int_{-\infty}^{+\infty} g(x) f_X(x) dx}$$

---

**Definizione 8.10 (Varianza per variabili continue)**

$$\boxed{\text{Var}(X) = \int_{-\infty}^{+\infty} (x - \mu_X)^2 f_X(x) dx = E[X^2] - \mu_X^2}$$

---

### 8.4 Trasformazione di Densità

---

**Teorema 8.11 (Trasformazione di densità per funzioni monotone)**

Se $X$ è continua con densità $f_X(x)$ e $Y = g(X)$ dove $g$ è **strettamente monotona** e differenziabile, allora:

$$\boxed{f_Y(y) = f_X(g^{-1}(y)) \cdot \left|\frac{d}{dy} g^{-1}(y)\right| = \frac{f_X(x)}{|g'(x)|} \bigg|_{x = g^{-1}(y)}}$$

dove il termine $|g'(x)|^{-1}$ è il **fattore jacobiano**.

---

**Esempio 8.12 (Trasformazione lineare)**

Se $X \sim \mathcal{N}(\mu, \sigma^2)$ e $Y = aX + b$ con $a > 0$:

$$f_Y(y) = f_X\left(\frac{y-b}{a}\right) \cdot \frac{1}{|a|}$$

che è una gaussiana con media $a\mu + b$ e deviazione standard $|a|\sigma$.

---

## Capitolo 9: Distribuzioni Continue Notevoli

### 9.1 Distribuzione Uniforme Continua

---

#### Definizione 9.1 (Variabile Uniforme $U(a,b)$)

$X$ è **uniforme** sull'intervallo $[a, b]$ se:

$$\boxed{f_X(x) = \begin{cases} \dfrac{1}{b-a} & a \leq x \leq b \\ 0 & \text{altrove} \end{cases}}$$

---

**Proposizione 9.2 (CDF della uniforme)**

$$F_X(x) = \begin{cases} 0 & x < a \\ \dfrac{x-a}{b-a} & a \leq x \leq b \\ 1 & x > b \end{cases}$$

---

**Teorema 9.3 (Media della uniforme)**

$$\boxed{E[X] = \frac{a+b}{2}}$$

*Dimostrazione:*

$$E[X] = \int_a^b x \cdot \frac{1}{b-a} dx = \frac{1}{b-a} \cdot \left[\frac{x^2}{2}\right]_a^b = \frac{b^2 - a^2}{2(b-a)} = \frac{(b+a)(b-a)}{2(b-a)} = \frac{a+b}{2}$$

□

---

**Teorema 9.4 (Varianza della uniforme)**

$$\boxed{\text{Var}(X) = \frac{(b-a)^2}{12}}$$

---

### 9.2 Distribuzione Esponenziale

---

#### Definizione 9.5 (Variabile Esponenziale $\text{Exp}(\lambda)$)

$X$ è **esponenziale** di parametro $\lambda > 0$ se:

$$\boxed{f_X(x) = \begin{cases} \lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{cases}}$$

---

**Proposizione 9.6 (CDF della esponenziale)**

$$F_X(x) = \begin{cases} 0 & x < 0 \\ 1 - e^{-\lambda x} & x \geq 0 \end{cases}$$

*Dimostrazione:*

$$F_X(x) = \int_0^x \lambda e^{-\lambda t} dt = [-e^{-\lambda t}]_0^x = 1 - e^{-\lambda x}$$

□

---

**Teorema 9.7 (Media dell'esponenziale)**

$$\boxed{E[X] = \frac{1}{\lambda}}$$

*Dimostrazione:*

$$E[X] = \int_0^{+\infty} x \lambda e^{-\lambda x} dx$$

Integrazione per parti con $u = x$, $dv = \lambda e^{-\lambda x} dx$:

$$= [-x e^{-\lambda x}]_0^{\infty} + \int_0^{\infty} e^{-\lambda x} dx = 0 + \left[-\frac{1}{\lambda} e^{-\lambda x}\right]_0^{\infty} = \frac{1}{\lambda}$$

□

---

**Teorema 9.8 (Varianza dell'esponenziale)**

$$\boxed{\text{Var}(X) = \frac{1}{\lambda^2}}$$

---

**Proposizione 9.9 (Proprietà di assenza di memoria)**

$$P(X > s + t | X > s) = P(X > t)$$

L'esponenziale è l'**unica** distribuzione continua con questa proprietà.

---

### 9.3 Distribuzione di Laplace

---

#### Definizione 9.10 (Variabile di Laplace $\text{Laplace}(\lambda)$)

$X$ è **laplaciana** di parametro $\lambda > 0$ se:

$$\boxed{f_X(x) = \frac{\lambda}{2} e^{-\lambda|x|}, \quad x \in \mathbb{R}}$$

---

**Proposizione 9.11 (CDF della Laplace)**

$$F_X(x) = \begin{cases} \dfrac{1}{2} e^{\lambda x} & x \leq 0 \\[6pt] 1 - \dfrac{1}{2} e^{-\lambda x} & x > 0 \end{cases}$$

---

**Teorema 9.12 (Media della Laplace)**

$$E[X] = 0$$

per simmetria.

---

**Teorema 9.13 (Varianza della Laplace)**

$$\boxed{\text{Var}(X) = \frac{2}{\lambda^2}}$$

---

### 9.4 Distribuzione Gaussiana (Cenni)

La distribuzione gaussiana (o normale) $\mathcal{N}(\mu, \sigma^2)$ ha PDF:

$$f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

Trattazione completa nel corso avanzato.

---

## Capitolo 10: Variabili Continue Bivariate

### 10.1 PDF Congiunta e CDF Congiunta

---

#### Definizione 10.1 (PDF congiunta)

La **densità di probabilità congiunta** di $(X, Y)$ è una funzione $f_{X,Y} : \mathbb{R}^2 \to \mathbb{R}_{\geq 0}$ tale che:

$$\iint_{\mathbb{R}^2} f_{X,Y}(x, y) dx dy = 1$$

e

$$P((X, Y) \in C) = \iint_C f_{X,Y}(x, y) dx dy$$

per ogni regione $C \subset \mathbb{R}^2$.

---

#### Definizione 10.2 (CDF congiunta)

$$F_{X,Y}(x, y) = P(X \leq x, Y \leq y) = \int_{-\infty}^x \int_{-\infty}^y f_{X,Y}(u, v) dv du$$

---

**Proposizione 10.3**

La PDF congiunta si recupera dalla CDF mediante:

$$f_{X,Y}(x, y) = \frac{\partial^2 F_{X,Y}(x, y)}{\partial x \partial y}$$

---

### 10.2 Densità Marginali

---

**Teorema 10.4 (Marginalizzazione)**

$$\boxed{f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x, y) dy}$$

$$\boxed{f_Y(y) = \int_{-\infty}^{+\infty} f_{X,Y}(x, y) dx}$$

---

### 10.3 Densità Condizionata

---

#### Definizione 10.5 (PDF condizionata)

Dato un evento $A$ con $P(A) > 0$, la **CDF condizionata** è:

$$F_{X|A}(x) = P(X \leq x | A) = \frac{P(X \leq x, A)}{P(A)}$$

La **PDF condizionata** è:

$$\boxed{f_{X|A}(x) = \frac{d}{dx} F_{X|A}(x)}$$

---

**Esempio 10.6 (Uniforme condizionata)**

Sia $X \sim U(0, 10)$ e $A = \{X > 3\}$.

$$P(A) = 1 - F_X(3) = 1 - \frac{3}{10} = 0.7$$

Per $x \in (3, 10)$:

$$f_{X|A}(x) = \frac{1}{7}$$

La PDF condizionata è uniforme su $(3, 10)$ con altezza $1/7$ (normalizzazione sull'intervallo ridotto).

---

### 10.4 Indipendenza nel Caso Continuo

---

#### Definizione 10.7 (Indipendenza per variabili continue)

$X$ e $Y$ sono **indipendenti** se e solo se:

$$\boxed{f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y)}$$

per ogni $(x, y) \in \mathbb{R}^2$.

---

**Esempio 10.8 (Gaussiane indipendenti)**

Se $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$ e $Y \sim \mathcal{N}(\mu_Y, \sigma_Y^2)$ sono indipendenti:

$$f_{X,Y}(x, y) = \frac{1}{2\pi \sigma_X \sigma_Y} \exp\left(-\frac{(x-\mu_X)^2}{2\sigma_X^2} - \frac{(y-\mu_Y)^2}{2\sigma_Y^2}\right)$$

---

# Parte IV — Teoria dell'Informazione (Cenni)

## Capitolo 11: Entropia e Informazione

### 11.1 Misura dell'Informazione

---

**Motivazione 11.1**

L'informazione ricevuta quando si osserva un evento $A$ di probabilità $P(A)$ deve soddisfare:

1. **Non negativa:** $I(A) \geq 0$
2. **Decrescente nella probabilità:** più raro l'evento, più informazione porta
3. **Additiva per eventi indipendenti:** $I(A \cap B) = I(A) + I(B)$ se $A \perp B$

---

#### Definizione 11.2 (Contenuto informativo)

$$\boxed{I(A) = \log_2 \frac{1}{P(A)} = -\log_2 P(A)}$$

L'unità è il **bit** (binary digit).

---

**Esempi 11.3**

- Evento certo ($P(A) = 1$): $I(A) = 0$ bit
- Moneta equilibrata ($P(A) = 1/2$): $I(A) = 1$ bit
- Evento molto raro ($P(A) = 2^{-10}$): $I(A) = 10$ bit

---

### 11.2 Entropia di Shannon

---

#### Definizione 11.4 (Entropia)

L'**entropia** di una variabile aleatoria discreta $X$ con PMF $p_X(x)$ è:

$$\boxed{H(X) = -\sum_{x \in \mathcal{X}} p_X(x) \log_2 p_X(x) = E\left[-\log_2 p_X(X)\right]}$$

Si misura in **bit**.

---

**Teorema 11.5 (Proprietà dell'entropia)**

1. **Non negativa:** $H(X) \geq 0$, con $H(X) = 0$ sse $X$ è deterministica

2. **Massimizzata dall'uniforme:** Per alfabeto di cardinalità $n$:

$$H_{\max} = \log_2 n$$

raggiunto quando $p_X(x) = 1/n$ per ogni $x$

3. **Sotto-additività:** $H(X, Y) \leq H(X) + H(Y)$, con uguaglianza sse $X \perp Y$

---

**Esempio 11.6 (Entropia di una Bernoulliana)**

Per $X \in \{0, 1\}$ con $P(X=1) = p$:

$$H(X) = -p \log_2 p - (1-p) \log_2(1-p)$$

Massimo a $p = 1/2$: $H(1/2, 1/2) = 1$ bit.

---

### 11.3 Applicazioni alla Compressione

---

**Teorema 11.7 (Shannon — Primo teorema della teoria delle sorgenti)**

L'entropia $H(X)$ rappresenta il **limite inferiore** del numero medio di bit necessari per codificare $X$ senza perdita di informazione.

---

**Osservazione 11.8**

Un file compresso ideale è una sequenza binaria in cui:
- Ogni bit è equiprobabile ($P(0) = P(1) = 1/2$)
- I bit sono statisticamente indipendenti

In questo caso, l'entropia per bit è massima (1 bit), e non è possibile comprimere ulteriormente.

---

# Parte V — Processi Aleatori (Introduzione)

## Capitolo 12: Processi Stocastici

### 12.1 Definizione e Realizzazioni

---

#### Definizione 12.1 (Processo stocastico)

Un **processo stocastico** è una famiglia di variabili aleatorie indicizzate dal tempo:

$$\{X(t) : t \in \mathcal{T}\}$$

dove $\mathcal{T}$ è un insieme di indici (tipicamente $\mathbb{N}$ per tempo discreto, $\mathbb{R}$ per tempo continuo).

---

**Osservazione 12.2**

Per ogni $\omega \in \Omega$ fissato, la funzione $t \mapsto X(t, \omega)$ è una **realizzazione** (o **traiettoria**) del processo.

Per ogni $t$ fissato, $X(t, \cdot)$ è una variabile aleatoria.

---

### 12.2 Processi in Tempo Discreto e Continuo

---

**Definizione 12.3 (Tempo discreto)**

$\mathcal{T} = \mathbb{Z}$ o $\mathbb{N}$: sequenza $\{X_1, X_2, X_3, \ldots\}$.

**Esempi:** prezzi azionari giornalieri, campioni di un segnale audio.

---

**Definizione 12.4 (Tempo continuo)**

$\mathcal{T} = [0, T]$ o $\mathbb{R}_{\geq 0}$: funzione continua $t \mapsto X(t, \omega)$.

**Esempi:** voltaggio di rumore termico, posizione di una particella in moto browniano.

---

### 12.3 Stazionarietà

---

#### Definizione 12.5 (Stazionarietà stretta)

Un processo è **stazionario in senso stretto** se le proprietà statistiche sono invarianti per traslazioni temporali:

$$P(X(t_1) \leq x_1, \ldots, X(t_n) \leq x_n) = P(X(t_1 + \tau) \leq x_1, \ldots, X(t_n + \tau) \leq x_n)$$

per ogni scelta di tempi e ritardo $\tau$.

---

#### Definizione 12.6 (Stazionarietà in senso lato)

Un processo è **stazionario in senso lato** (WSS — Wide Sense Stationary) se:

1. $E[X(t)]$ è costante nel tempo
2. $\text{Var}(X(t))$ è costante nel tempo
3. $\text{Cov}(X(t_1), X(t_2))$ dipende solo da $|t_1 - t_2|$

---

### 12.4 Processi di Poisson e Gaussiani

---

**Definizione 12.7 (Processo di Poisson)**

Il **processo di Poisson** con intensità $\lambda$ conta il numero di eventi fino al tempo $t$:

$$P(N(t) = k) = \frac{(\lambda t)^k}{k!} e^{-\lambda t}$$

**Proprietà:**

- **Incrementi indipendenti:** eventi in intervalli disgiunti sono indipendenti
- **Incrementi stazionari:** la distribuzione dipende solo dalla lunghezza dell'intervallo
- **Assenza di memoria**

**Applicazioni:** code di rete, guasti di componenti, arrivi di clienti.

---

**Definizione 12.8 (Processo Gaussiano)**

Un processo è **gaussiano** se ogni marginale $X(t)$ è gaussiana e ogni densità congiunta è gaussiana multivariata.

Completamente caratterizzato da:
- Funzione media: $\mu_X(t) = E[X(t)]$
- Funzione di autocovarianza: $\gamma(t_1, t_2) = \text{Cov}(X(t_1), X(t_2))$

**Applicazioni:** filtraggio di Kalman, Gaussian Process regression.

---

# Appendici

## Appendice A: Richiami di Calcolo

**Serie Geometrica:**

$$\sum_{k=0}^{\infty} r^k = \frac{1}{1-r}, \quad |r| < 1$$

**Serie Esponenziale:**

$$e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}$$

**Integrazione per parti:**

$$\int u \, dv = uv - \int v \, du$$

**Funzione Gamma di Eulero:**

$$\Gamma(n) = (n-1)! = \int_0^{\infty} t^{n-1} e^{-t} dt$$

---

## Appendice B: Tavole di Distribuzioni

### Discrete

| Distribuzione | PMF | Media | Varianza |
|---------------|-----|-------|----------|
| Bernoulli$(p)$ | $p^x(1-p)^{1-x}$ | $p$ | $p(1-p)$ |
| Binomiale$(n,p)$ | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Poisson$(\lambda)$ | $\frac{\lambda^k}{k!}e^{-\lambda}$ | $\lambda$ | $\lambda$ |
| Geometrica$(p)$ | $(1-p)^{k-1}p$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |
| Uniforme$(m)$ | $\frac{1}{m}$ | $\frac{m+1}{2}$ | $\frac{m^2-1}{12}$ |

### Continue

| Distribuzione | PDF | Media | Varianza |
|---------------|-----|-------|----------|
| Uniforme$(a,b)$ | $\frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| Esponenziale$(\lambda)$ | $\lambda e^{-\lambda x}$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| Laplace$(\lambda)$ | $\frac{\lambda}{2}e^{-\lambda|x|}$ | $0$ | $\frac{2}{\lambda^2}$ |

---

## Appendice C: Esercizi Svolti Completi

### Esercizio C.1 (Probabilità al poker)

**Testo:** Mazzo da 52 carte, calcolare la probabilità di ottenere un "colore" (flush).

**Soluzione:**

$$|\Omega| = \binom{52}{5} = 2.598.960$$

$$|A_{\text{colore}}| = 4 \cdot \binom{13}{5} = 4 \cdot 1.287 = 5.148$$

$$P(\text{colore}) = \frac{5.148}{2.598.960} \approx 0.00198$$

---

### Esercizio C.2 (Teorema di Bayes — dado truccato)

**Testo:** Bussolotto con 2 dadi onesti e 1 truccato ($P(6|\text{truccato}) = 1/2$). Estraggo un dado, lancio due volte, ottengo $(5, 5)$. Probabilità che il dado sia truccato?

**Soluzione:**

**Distribuzione dado truccato:**

$$P(6|\text{truccato}) = \frac{1}{2}, \quad P(i|\text{truccato}) = \frac{1}{10} \quad (i \neq 6)$$

**Probabilità a priori:**

$$P(\text{truccato}) = \frac{1}{3}$$

**Calcolo di $P(5,5)$:**

Via legge della probabilità totale:

$$P(5,5) = P(5,5|\text{onesto}) \cdot P(\text{onesto}) + P(5,5|\text{truccato}) \cdot P(\text{truccato})$$

$$= \left(\frac{1}{6} \cdot \frac{1}{6}\right) \cdot \frac{2}{3} + \left(\frac{1}{10} \cdot \frac{1}{10}\right) \cdot \frac{1}{3}$$

$$= \frac{1}{36} \cdot \frac{2}{3} + \frac{1}{100} \cdot \frac{1}{3} = \frac{2}{108} + \frac{1}{300} = \frac{17}{900}$$

**Teorema di Bayes:**

$$P(\text{truccato}|5,5) = \frac{P(5,5|\text{truccato}) \cdot P(\text{truccato})}{P(5,5)} = \frac{\frac{1}{100} \cdot \frac{1}{3}}{\frac{17}{900}} = \frac{9}{34} \approx 0.265$$

---

### Esercizio C.3 (Vaccinazione — Binomiale)

**Testo:** 10 bambini vaccinati, efficacia 90%. Probabilità che almeno 8 siano immunizzati?

**Soluzione:**

$X \sim \text{Bin}(10, 0.9)$

$$P(X \geq 8) = \sum_{k=8}^{10} \binom{10}{k} (0.9)^k (0.1)^{10-k}$$

$$= \binom{10}{8}(0.9)^8(0.1)^2 + \binom{10}{9}(0.9)^9(0.1) + (0.9)^{10}$$

$$\approx 0.1937 + 0.3874 + 0.3487 = 0.9298$$

---

**Fine del Libro**
