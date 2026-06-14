# SBOBINA - STATISTICA E PROBABILITÀ | LEZIONE SU VARIabili Aleatorie e PMF Congiunte

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Informazione non menzionata
- **Docente**: Informazione non menzionata
- **Orari e Aule**: Informazione non menzionata
- **Organizzazione Didattica**:
    - **CFU e Ore**: Informazione non menzionata
    - **Modalità di erogazione**: Informazione non menzionata
- **Ricevimento e Supporto**: Informazione non menzionata
- **Avvisi, Calendario e Assenze**: Informazione non menzionata
- **Consigli pratici del docente**: Il docente sottolinea l'importanza di comprendere la logica sottostante piuttosto che limitarsi alla memorizzazione dei risultati.
- **Accesso ai Materiali**: Informazione non menzionata

---

## 🎯 SOMMARIO RAPIDO
- Caratterizzazione delle variabili aleatorie tramite PMF e calcolo dei momenti (Media, Varianza, RMS).
- Trasformazioni di variabili aleatorie e Teorema Generale per il calcolo della media.
- Caratterizzazione globale (Chebyshev) e condizionale delle variabili aleatorie.
- Variabili aleatorie multiple: PMF congiunta, marginalizzazione e indipendenza statistica.
- Struttura gerarchica delle variabili a $n$ componenti e applicazioni alla compressione dati.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Funzione di Massa di Probabilità | PMF | Insieme di numeri compresi tra 0 e 1 che si sommano a 1, corrispondenti alle probabilità di ogni valore dell'alfabeto di una variabile aleatoria discreta. |
| Media Statistica | $E[X]$ o $\mu$ | Introdotta come definizione formale e interpretata come limite di una media campionaria. |
| Momento Emesso | $E[X^m]$ | Media statistica della funzione $g(X) = X^m$. |
| Momento Centrale | $E[(X - \mu)^m]$ | Media statistica della funzione $g(X) = (X - \mu)^m$. |
| ValoreআরM (RMS) | $\sqrt{E[X^2]}$ | Valore quadratico medio, corrispondente alla radice quadrata del secondo momento emesso. |
| Varianza | $\sigma^2$ | Momento centrale di ordine 2, calcolabile come differenza tra il quadrato del valore quadratico medio e il quadrato del valore medio. |
| Deviazione Standard | $\sigma$ | Radice quadrata della varianza. |
| Disuguaglianza di Chebyshev | - | Relazione che limita la probabilità di deviazioni dalla media: $P(|X - \mu| > k\sigma) \le \frac{1}{k^2}$. |
| PMF Congiunta | $P(X, Y)$ | Tabella di probabilità per ogni coppia ordinata $(x, y)$ appartenente al prodotto cartesiano degli alfabeti di $X$ e $Y$. |
| Marginalizzazione | - | Processo di ottenimento della PMF di una variabile singola sommando la PMF congiunta su tutti i possibili valori dell'altra variabile. |
| Indipendenza Statistica | - | Condizione in cui la PMF congiunta si fattorizza nel prodotto delle PMF marginali: $P(X,Y) = P(X)P(Y)$. |
| Variabile Aleatoria n-dupla | $(X_1, \dots, X_n)$ | Applicazione dallo spazio dei campioni a una terna o n-terna ordinata appartenente a un prodotto cartesiano di $n$ alfabeti. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### Caratterizzazione della Variabile Aleatoria Singola
- **Spiegazione Teorica**: Una variabile aleatoria singola è completamente caratterizzata dalla sua **PMF**, che rappresenta l'insieme delle probabilità associate a ogni elemento dell'alfabeto della variabile.
- **Media Statistica**: Il docente introduce la media sia come definizione formale, sia come limite di una media campionaria.
- **Trasformazioni di Variabili Aleatorie**: Data una funzione $y = g(x)$, dove $x$ è una variabile aleatoria, anche $y$ è una variabile aleatoria poiché rappresenta una funzione composta $g(x(\omega))$ applicata allo spazio dei campioni $\Omega$.
- **Regole di Trasformazione**:
    1. **Trasformazione Biunivoca**: Se la corrispondenza è biunivoca, si tratta di un semplice cambio di alfabeto; le probabilità non cambiano e si spostano semplicemente dal valore $x$ al valore $g(x)$.
    2. **Trasformazione Non Univoca (Collasso)**: Se più punti dell'alfabeto di $x$ collassano in un unico punto dell'alfabeto di $y$, la probabilità del punto $y$ è data dalla **somma delle probabilità** dei punti di $x$ che vi convergono.
- **Teorema Generale per il Calcolo della Media**: La media statistica di una funzione $g(X)$ si ottiene tramite la sommatoria:
  $$E[g(X)] = \sum_{x} g(x) \cdot P(X=x)$$
- **Momenti di una Variabile Aleatoria**:
    - **Momento emesso di ordine $m$**: $E[g(X)]$ dove $g(x) = x^m$.
    - **Momento centrale di ordine $m$**: $E[g(X)]$ dove $g(x) = (x - \mu)^m$.
    - **Caso $m=2$**:
        - $E[X^2]$ è il valore quadratico medio.
        - $RMS = \sqrt{E[X^2]}$.
        - $\sigma^2 = E[(X - \mu)^2]$ è la varianza.
        - $\sigma = \sqrt{\sigma^2}$ è la deviazione standard.
        - Relazione: $\sigma^2 = E[X^2] - (E[X])^2$.

### Caratterizzazione Globale e Condizionale
- **Caratterizzazione Globale**: In assenza di dati sufficienti per l'inferenza precisa, una variabile può essere caratterizzata globalmente tramite la coppia **(Media, Deviazione Standard)**.
- **Interpretazione di Chebyshev**:
    - Se $\sigma$ è piccola rispetto a $\mu$, la variabile è **molto concentrata** attorno al valore medio (frequenti valori vicini a $\mu$).
    - Se $\sigma$ è grande rispetto a $\mu$, la variabile è **molto aleatoria** (le realizzazioni sono distribuite in modo più disperso sull'alfabeto).
- **Caratterizzazione Condizionale**: La PMF condizionata $P(X|A)$ mantiene le proprietà della PMF (somma 1, valori non negativi).
    - **Relazione con la Probabilità Congiunta**: $P(X=x|A) = \frac{P(X=x \cap A)}{P(A)}$.
- **Media come Combinazione Convessa**: La media di una variabile aleatoria $X$ può essere vista come una combinazione convessa, dove i coefficienti di linearità sono le masse di probabilità delle prime condizionali, essendo non negativi e la loro somma pari a 1.

### Variabili Aleatorie Multiple e n-duple
- **Variabile Aleatoria Doppia**: Applicazione da $\Omega$ a una coppia ordinata $(x, y)$ appartenente al prodotto cartesiano degli alfabeti.
- **PMF Congiunta**: Caratterizza una coppia di variabili quando viene assegnata una tabella di numeri (pari al prodotto delle cardinalità degli alfabeti) tale che la loro somma sia 1.
- **Proprietà di Normalizzazione e Marginalizzazione**:
    - La somma della PMF congiunta su tutti i valori di $x$ dà la marginale di $y$.
    - La somma della PMF congiunta su tutti i valori di $y$ dà la marginale di $x$.
    - **Conseguenza**: Assegnare una PMF congiunta implica automaticamente assegnare le due PMF marginali. Il contrario non è vero (date due marginali esistono molte congiunte compatibili).
- **Indipendenza Statistica**: Due variabili sono indipendenti se la PMF congiunta si fattorizza nel prodotto delle marginali:
  $$P(x, y) = P(x) \cdot P(y)$$
- **Variabili a $n$ componenti**: Una variabile $n$-dupla associa a ogni $\omega$ una terna (o n-terna) ordinata.
    - **Gerarchia della Conoscenza**: Caratterizzare una variabile all'ordine $n$ implica automaticamente la conoscenza di tutte le congiunte di ordine inferiore ($n-1, n-2, \dots, 1$) tramite marginalizzazione successiva. Il contrario non è vero.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Analisi di una Variabile Aleatoria Doppia (Indipendenza)
- **Testo**: Data una tabella di probabilità per due variabili binarie $X_1, X_2 \in \{0, 1\}$ con valori:
    - $P(0,0) = 1/4$
    - $P(0,1) = 1/8$
    - $P(1,0) = 1/8$
    - $P(1,1) = 1/2$
- **Risoluzione Passo-Passo**:
    1. **Calcolo Marginali**: 
       - $P(X_1=0) = P(0,0) + P(0,1) = 1/4 + 1/8 = 3/8$.
       - $P(X_1=1) = 1 - 3/8 = 5/8$.
       - $P(X_2=0) = P(0,0) + P(1,0) = 1/4 + 1/8 = 3/8$.
       - $P(X_2=1) = 1 - 3/8 = 5/8$.
    2. **Verifica Indipendenza**: 
       - Prodotto delle marginali: $P(X_1=0) \cdot P(X_2=0) = (3/8) \cdot (3/8) = 9/64$.
       - Valore della congiunta: $P(0,0) = 1/4 = 16/64$.
    3. **Risultato finale**: Poiché $16/64 \neq 9/64$, le variabili **non sono indipendenti**.
- **Concetti Applicati**: PMF Congiunta, Marginalizzazione, Indipendenza Statistica.

### Esercizio 2: Modelli di Sorgenti di Bit (Parità vs Indipendenza)
- **Testo**: Confronto di due modelli per una terna di bit $(X_1, X_2, X_3)$ con $P(1)=p$ e $P(0)=1-p$.
- **Risoluzione Passo-Passo**:
    - **Modello 1 (Indipendenza)**: Ogni bit è indipendente. La probabilità di una terna è il prodotto delle probabilità dei singoli bit. Esempio: $P(0,0,0) = (1-p)^3$.
    - **Modello 2 (Bit di Parità)**: I primi due bit sono indipendenti, il terzo è un bit di parità (determina il valore affinché il numero di 1 sia pari).
    - **Confronto**:
        - Nel Modello 2, la terna $(0,0,0)$ è possibile perché il numero di 1 è pari (zero). La sua probabilità è uguale a quella della coppia $(0,0)$ poiché il terzo bit è determinato.
        - La marginale di $X_1$ o $X_2$ è identica in entrambi i modelli ($1-p$).
        - La PMF di ordine 3 è invece **totalmente diversa** a causa del vincolo di parità.
- **Concetti Applicati**: Variabili a $n$ componenti, Indipendenza vs Dipendenza.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    * **Somma della PMF**: Confondere la somma della PMF congiunta (che deve essere sempre 1) con la somma della PMF condizionale (che deve essere 1 solo se il condizionamento resta fisso).
    * **Marginali vs Congiunte**: Confondere la conoscenza delle marginali con la conoscenza della congiunta (le marginali non determinano univocamente la congiunta, a meno che non vi sia indipendenza).
- **Chiarimenti Metodologici**:
    * Il concetto di "caratterizzazione" dipende dall'ordine della variabile: una caratterizzazione di ordine $n$ implica tutte quelle di ordine inferiore per marginalizzazione.
- **Punti Critici per l'Esame**:
    * Distinzione tra trasformazioni biunive e non biunive.
    * Interpretazione fisica della deviazione standard (concentrazione vs dispersione).
    * Capacità di riconoscere se due variabili sono indipendenti tramite il prodotto delle marginali.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata.
- **Propedeuticità e Prerequisiti**:
    * Cultura matematica di base.
    * Conoscenza degli assiomi di Kolmogorov (normalizzazione, subadditività).
- **Consigli di Studio Espliciti**:
    * Il docente raccomanda di non focalizzarsi sulla memoria ma sulla logica della costruzione delle PMF.
    * Comprendere come la scelta di una PMF congiunta modella un fenomeno specifico (es. sorgente senza memoria vs bit di parità).

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Lempel-Ziv**: Algoritmo di compressione (Zipping) citato come esempio di come la caratterizzazione statistica delle stringhe permetta di raggiungere i limiti informazionali.
- **Iuri Polianski (MIT)**: Citato per lo studio sulla comprimibilità asintotica di stringhe di simboli (dimostrazione che l'infinito asintotico può essere raggiunto con 4-5 mila simboli).
- **Marcel Proust**: Citato (*La Recherche du Temps Perdu*) come esempio di sorgente con altissima ridondanza linguistica.

---

### 💡 ANEDDOTI E CONTESTI EXTRA (FORNITI DAL DOCENTE)
- **Sicurezza e Guerra**: Citato il ruolo storico della ricerca scientifica durante i periodi di guerra (es. Oppenheimer e la bomba atomica) come motore di progresso tecnologico accelerato dai fondi militari.
- **Falsi Allarmi**: Esempio della probabilità di falso allarme nei radar (necessità di probabilità $10^{-10}$ per evitare di bombardare ospedali), per illustrare l'importanza della precisione statistica.
- **Ridondanza Linguistica**: Esempio della scrittura "quadro" vs "quandro": la rimozione della ridondanza aumenta la fragilità del messaggio rispetto agli errori sistematici.