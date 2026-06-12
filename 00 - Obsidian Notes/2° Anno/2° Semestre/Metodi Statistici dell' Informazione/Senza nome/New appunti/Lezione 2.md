# SBOBINA - Probabilità e Statistica | Lezione su Combinatoria, Probabilità Condizionata e Variabili Aleatorie

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Nome/Codice non specificato nella trascrizione]
- **Docente**: [Nome non specificato nella trascrizione]
- **Orari e Aule**: Prossima lezione prevista per **giovedì alle 09:45**.
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione frontale con analisi teorica e risoluzione di esercizi numerici.
- **Ricevimento e Supporto**: Informazione non menzionata nella lezione.
- **Avvisi, Calendario e Assenze**:
    - La lezione di oggi è dedicata alla revisione dei concetti fondamentali e all'introduzione della formalizzazione matematica della probabilità.
- **Consigli pratici del docente**: 
    - Il docente sottolinea esplicitamente la necessità di privilegiare la **logica** rispetto alla memorizzazione mnemonica.
- **Accesso ai Materiali**: Informazione non menzionata nella lezione.

---

## 🎯 SOMMARIO RAPIDO
1. Fondamenti di analisi combinatoria (permutazioni, combinazioni e coefficienti binomiali).
2. Definizione frequentista di probabilità e proprietà derivate dalla teoria degli insiemi.
3. Probabilità condizionata, Legge della Probabilità Totale e Teorema di Bayes.
4. Formalizzazione matematica: $\sigma$-algebra, Assiomi di Kolmogorov e Variabili Aleatorie.
5. Analisi dell'indipendenza statistica e calcolo delle probabilità in sistemi multi-evento.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Spazio Campionario | $\Omega$ | L'insieme di tutti i possibili esiti di un esperimento. |
| Evento | $A, B \subseteq \Omega$ | Sottinsiemi dello spazio campionario. |
| Cardinalità | $|\cdot|$ | Il numero di elementi contenuti in un insieme. |
| Probabilità Frequentistica | $P(A)$ | Il limite della frequenza di successo di un evento quando il numero di prove $n \to \infty$. |
| Complementare | $\bar{A}$ o $A^c$ | L'insieme degli elementi in $\Omega$ non presenti in $A$. |
| Incompatibilità | Disgiunzione | Due eventi sono incompatibili se la loro intersezione è vuota ($A \cap B = \emptyset$). |
| Probabilità Condizionata | $P(A|B)$ | La probabilità che si verifichi $A$ dato che si è verificato $B$ (con $P(B) \neq 0$). |
| Algebra di $\sigma$ | $\sigma$-algebra | Una collezione di sottoinsiemi di $\Omega$ chiusa rispetto all'unione e alla complementazione. |
| Variabile Aleatoria | $X$ | Una funzione (applicazione) che associa a ogni esito $\omega \in \Omega$ un valore numerico in un alfabeto. |
| Funzione di Densità di Probabilità (PMF) | $P(X=x)$ | La sequenza di probabilità associate ai valori assunti da una variabile aleatoria discreta. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Fondamenti di Analisi Combinatoria
La probabilità può essere calcolata come il rapporto tra casi favorevoli e casi possibili, a patto che gli eventi elementari siano **equiprobabili** (equivalenti). Per calcolarli, si utilizzano le proprietà del prodotto cartesiano:

- **Permutazioni di $k$ elementi da $n$**: Numero di cappule ordinate estratte da un insieme di $n$ elementi distinti.
  $$P(n,k) = \frac{n!}{(n-k)!}$$
- **Permutazioni con ripetizione**: Se gli elementi possono essere ripetuti, il numero di combinazioni è:
  $$n^k$$
- **Combinazioni (Cappule non ordinate)**: Se l'ordine non è rilevante, si divide il numero di permutazioni per le permutazioni di $k$ elementi su $k$ posti:
  $$\frac{P(n,k)}{k!}$$
- **Coefficiente Binomiale**: Numero di $n$-duple binarie con esattamente $k$ successi (essenziale per la distribuzione binomiale).
  $$\binom{n}{k}$$

### 2. Definizione Frequentistica di Probabilità
Quando gli eventi non sono equiprobabili, si ricorre alla definizione di **frequenza di successo**.
- **Definizione**: Se facciamo $n$ prove e l'evento $A$ si verifica $n_A$ volte, la frequenza è $f_n(A) = \frac{n_A}{n}$.
- **Limite**: La probabilità di $A$ è definita come il limite della frequenza per $n$sufficientemente grande:
  $$P(A) = \lim_{n \to \infty} \frac{n_A}{n}$$
- **Proprietà derivate dalla teoria degli insiemi**:
    - **Complementare**: $P(\bar{A}) = 1 - P(A)$ (poiché $n_{\bar{A}} = n - n_A$).
    - **Unione**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ (si sottrae l'intersezione per evitare il doppio conteggio).
    - **Differenza**: $P(A \setminus B) = P(A) - P(A \cap B)$.
- **Interpretazione della Misura**: La probabilità è vista come una "misura" della dimensione di un insieme. Più grande è la probabilità, più grande è la misura del sottoinsieme di $\Omega$.

### 3. Probabilità Condizionata e Legge di Bayes
- **Frequenza Condizionale**: Se limitiamo l'analisi solo agli elementi che soddisfano la condizione $B$, la frequenza è $f(A|B) = \frac{n_{A \cap B}}{n_B}$.
- **Formula**: 
  $$P(A|B) = \frac{P(A \cap B)}{P(B)} \quad \text{con } P(B) \neq 0$$
- **Relazioni fondamentali**:
    - $P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$
    - **Legge di Bayes**: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
- **Legge della Probabilità Totale**: Permette di scomporre la probabilità di un evento difficile in calcoli più semplici attraverso una partizione di $\Omega$ (es. se $\Omega = \bigcup E_i$, allora $P(A) = \sum P(A|E_i)P(E_i)$).

### 4. Formalismo Rigoroso ($\sigma$-algebra e Assiomi di Kolmogorov)
Il docente introduce il passaggio dalla definizione "arrangiata" (frequentistica) a quella rigorosa.
- **Algebra di $\sigma$**: Una collezione $\mathcal{E}$ di sottoinsiemi di $\Omega$ è un'algebra di $\sigma$ se è chiusa rispetto a:
    1. **Unione**: $A, B \in \mathcal{E} \implies A \cup B \in \mathcal{E}$.
    2. **Complementazione**: $A \in \mathcal{E} \implies \bar{A} \in \mathcal{E}$.
    *Nota: Da queste due proprietà si deduce la chiusura rispetto all'intersezione tramite le leggi di De Morgan.*
- **Assiomi di Kolmogorov**: Una funzione $\mathcal{P}: \mathcal{E} \to [0,1]$ è una legge di probabilità se soddisfa:
    1. **Non-negatività**: $P(A) \geq 0$.
    2. **Normalizzazione**: $P(\Omega) = 1$.
    3. **Subadditività (Additività countable)**: Per eventi disgiunti, $P(\cup A_i) = \sum P(A_i)$.

### 5. Variabili Aleatorie e PMF
- **Definizione**: Una variabile aleatoria $X$ è un'applicazione (funzione) da $\Omega$ a un insieme numerico (alfabeto).
- **Utilità**: Permette di trattare esperimenti diversi (lancio moneta, bit binari, lancio dado) in modo uniforme tramite lo spazio dei valori numerici.
- **Misurabilità**: Per essere rigorosa, l'anti-immagine di ogni valore di $X$ deve essere un elemento della $\sigma$-algebra.
- **Probability Mass Function (PMF)**: Per una variabile discreta, è la sequenza di probabilità $P(X=x)$ tale che $\sum P(X=x) = 1$.
- **Media Statistica**: Definita come la somma dei prodotti dei valori assunti per la loro probabilità: $E[X] = \sum x \cdot P(X=x)$.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Il Dado Truccato (Indipendenza Condizionale)
**Testo**: Un busto contiene due dadi indistinguibili. Uno è onesto, l'altro è truccato in modo che il 6 esca con probabilità $1/2$ e tutti gli altri risultati siano equiprobabili. Estrarre un dado e lanciarlo due volte ottenendo la coppia $(5,5)$. Qual è la probabilità che il dado sia il truccato?

**Risoluzione Passo-Passo**:
1. **Analisi Dado Onesto ($D_O$)**: $P(x=i) = 1/6$ per ogni $i \in \{1..6\}$.
2. **Analisi Dado Truccato ($D_T$)**: 
   - $P(x=6) = 1/2$.
   - Per gli altri 5 numeri, la probabilità deve sommare a $1/2$. Essendo equiprobabili: $P(x=i) = (1/2) / 5 = 1/10$ per $i \in \{1..5\}$.
3. **Probabilità della coppia (5,5)**:
   - Dato $D_O$: $P(5,5|D_O) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$.
   - Dato $D_T$: $P(5,5|D_T) = \frac{1}{10} \times \frac{1}{10} = \frac{1}{100}$.
4. **Probabilità a priori**: $P(D_O) = 1/2$, $P(D_T) = 1/2$.
5. **Probabilità Totale della coppia (5,5)**:
   $$P(5,5) = P(5,5|D_O)P(D_O) + P(5,5|D_T)P(D_T) = \left(\frac{1}{36} \cdot \frac{1}{2}\right) + \left(\frac{1}{100} \cdot \frac{1}{2}\right)$$
6. **Applicazione di Bayes**:
   $$P(D_T|5,5) = \frac{P(5,5|D_T)P(D_T)}{P(5,5)} = \frac{\frac{1}{200}}{\frac{1}{72} + \frac{1}{200}}$$

*Concetti Applicati: Legge della Probabilità Totale, Teorema di Bayes, Indipendenza Condizionale.*

### Esercizio 2: Indipendenza di $n$ eventi
**Testo**: Dati $n$ eventi indipendenti $A_1, A_2, \dots, A_n$ con probabilità $p_i$. Calcolare:
1. Probabilità che non se ne verifichi nessuno.
2. Probabilità che se ne verifichi almeno uno.
3. Probabilità che se ne verifichi esattamente uno.

**Risoluzione Passo-Passo**:
1. **Nessuno**: Poiché gli eventi sono indipendenti, i loro complementari $\bar{A_i}$ sono indipendenti. La probabilità che nessuno avvenga è il prodotto delle probabilità dei complementari:
   $$P(\text{nessuno}) = \prod_{i=1}^{n} (1 - p_i)$$
2. **Almeno uno**: È il complementare dell'evento "nessuno".
   $$P(\text{almeno uno}) = 1 - \prod_{i=1}^{n} (1 - p_i)$$
3. **Exactly uno**: Si verificano gli eventi disgiunti: (avviene $A_1$ e non gli altri) OPPURE (avviene $A_2$ e non gli altri)...
   $$P(\text{esattamente uno}) = \sum_{i=1}^{n} \left( p_i \cdot \prod_{j \neq i} (1 - p_j) \right)$$

*Semplificazioni/Trucchi: L'uso del complementare per "almeno uno" semplifica drasticamente il calcolo rispetto alla somma delle combinazioni possibili.*

### Esercizio 3: Bit di Parità e Indipendenza
**Testo**: Una sorgente invia una coppia di bit $(x_1, x_2)$. Viene aggiunto un terzo bit $x_3$ tale che il numero di 1 nella terna sia pari. $x_3 = (x_1 + x_2) \pmod 2$. Dimostrare l'indipendenza.

**Risoluzione Passo-Passo**:
1. **Indipendenza a coppie**: $x_1$ e $x_2$ sono indipendenti (generati dalla sorgente). $x_1$ e $x_3$ sono indipendenti (conoscendo $x_1$ non possiamo predire $x_3$ senza $x_2$).
2. **Mancanza di indipendenza tripla**: La terna $(x_1, x_2, x_3)$ **non** è indipendente. Se conosco $x_1$ e $x_2$, il valore di $x_3$ è determinato univocamente ($P(x_3 | x_1, x_2) = 1$ per un valore specifico).

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    - **Equivalenza Matematica vs. Statistica**: Il docente avverte che una legge di probabilità può essere matematicamente legittima (soddisfa gli assiomi) ma non adeguata a descrivere la realtà (es. una moneta con due teste). L'abilità sta nello scegliere la legge che "aderisce alla realtà".
    - **Indipendenza**: Attenzione a non confondere l'indipendenza a coppie con l'indipendenza di un'intera n-upla.
- **Chiarimenti Metodologici**:
    - La variabile aleatoria è un concetto fondamentale per "unificare" esperimenti diversi (monete, dadi, bit) in un unico linguaggio numerico.
    - La $\sigma$-algebra garantisce che le operazioni che facciamo (unioni, intersezioni) restino "misurabili", ovvero che la probabilità sia definita anche per gli eventi complessi.
- **Punti Critici per l'Esame**:
    - Dimostrazione di proprietà (es. $P(A \cup B)$) partendo solo dagli assiomi di Kolmogorov.
    - Applicazione corretta della Legge di Bayes in contesti di campionamento (con e senza ripetizione).

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    - **Consigliati**: Cultura matematica di base, teoria degli insiemi.
- **Consigli di Studio Espliciti**:
    - Non imparare a memoria le formule; comprendere la logica sottostante (es. perché una formula deriva da una proprietà degli insiemi).

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Relazione con la ricerca**: Il docente accenna a una tesi di laurea triennale di un collega che approfondisce gli aspetti formali della misurabilità e delle $\sigma$-algebrae.
- **Note aggiuntive**: Il docente promette di approfondire i concetti di indipendenza e variabili aleatorie nella lezione di giovedì.