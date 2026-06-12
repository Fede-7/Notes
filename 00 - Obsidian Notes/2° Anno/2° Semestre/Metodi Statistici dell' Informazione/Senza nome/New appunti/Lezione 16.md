# SBOBINA - ELEMENTI DI STATISTICA INFERENZIALE

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Elementi di Statistica Inferenziale
- **Docente**: Non menzionato
- **Orari e Aule**: Informazione non menzionata nella lezione
- **Organizzazione Didattica**:
    - **CFU e Ore**: Informazione non menzionata nella lezione
    - **Modalità di erogazione**: Informazione non menzionata nella lezione
- **Ricevimento e Supporto**: Informazione non menzionata nella lezione
- **Avvisi, Calendario e Assenze**: Informazione non menzionata nella lezione
- **Consigli pratici del docente**: 
    - Il docente sottolinea l'importanza di comprendere le idee fondamentali (es. il discreto) prima di passare alle formule complesse (es. il continuo).
    - Si accenna alla necessità di una "cultura matematica" per cogliere i concetti di Machine Learning (es. il gradiente discendente e la concavità).
- **Accesso ai Materiali**: Informazione non menzionata nella lezione

---

## 🎯 SOMMARIO RAPIDO
- Distinzione tra Statistica Descrittiva (analisi di un blocco dati) e Statistica Inferenziale (inferenza di popolazione da campione).
- Tipologie di convergenza per le variabili aleatorie e legami con la Legge dei Grandi Numeri (LGN).
- Formalizzazione della Teoria della Decisione Bayesiana attraverso matrici di costo e rischio medio.
- Regole di decisione ottime: Maximum A Posteriori (MAP) e Maximum Likelihood (ML).
- Applicazione pratica alla classificazione di stringhe binarie tramite calcolo della soglia sul peso di Hamming.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| **Statistica Descrittiva** | - | Analisi delle proprietà globali di un blocco dati osservato (es. media, deviazione standard). |
| **Statistica Inferenziale** | - | Processo "bottom-up": uso dei dati per inferire le caratteristiche statistiche di una popolazione sottostante. |
| **Successione di Variabili Aleatorie** | $y_n$ | Una sequenza di funzioni di probabilità $y_n(\omega)$. |
| **Convergenza in Distribuzione** | $\xrightarrow{d}$ | La legge di probabilità della successione tende a una distribuzione limite (es. Gaussiana). |
| **Legge dei Grandi Numeri (Debole)** | - | Convergenza della media campionaria in probabilità verso la media statistica. |
| **Legge dei Grandi Numeri (Forte)** | - | Convergenza della media campionaria con probabilità 1. |
| **Convergenza in Media Quadratica** | - | Convergenza in cui la varianza dell'errore tende a zero (fondamentale per il gradiente discendente). |
| **Ipotesi della Natura** | $H_i$ | Stati possibili della natura, tipicamente incompatibili (es. $H_1, \dots, H_m$). |
| **Probabilità a Priori** | $P(H_i)$ | Probabilità pre-osservazione che la natura si trovi nello stato $H_i$. |
| **PMF/PDF Condizionale** | $P(X^{(n)} | H_i)$ | Legge di probabilità dei dati dati che la natura sia nello stato $H_i$. |
| **Regola di Decisione** | $d(x^{(n)})$ | Funzione che associa una realizzazione dei dati a un indice di decisione $i \in \{1, \dots, m\}$. |
| **Matrice dei Costi** | $C_{i,j}$ | Costo associato quando si decide $i$ ma lo stato reale è $j$.
| **Rischio Medio Bayesiano** | $R_B$ | Valore atteso del costo basato sulla probabilità congiunta di decisione e stato della natura. |
| **Peso di Hamming** | $W_H(x^{(n)})$ | Numero di successi (valori 1) in una sequenza binaria di lunghezza $n$. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Statistica Descrittiva vs Inferenziale
- **Spiegazione Teorica**: 
    - La **Statistica Descrittiva** (definita dal docente come "Statistica Excel") si occupa di descrivere le proprietà globali di un singolo blocco di dati. Non assume alcuna conoscenza su una popolazione più ampia.
    - La **Statistica Inferenziale** adotta un approccio *bottom-up*: partendo da un blocco di dati (campione), si tenta di inferire le caratteristiche statistiche della popolazione da cui il campione è stato estratto.
- **Condizioni Tacite**: Si assume che i blocchi di dati siano campioni $n$-dimensionali di una popolazione che possiede caratteristiche statistiche preassegnate.
- **Esempi Specifici Citati**:
    - *Esempio Excel*: Calcolo di media e deviazione standard su un vettore di dati senza alcuna inferenza esterna.

### 2. Convergenza di Variabili Aleatorie
- **Spiegazione Teorica**: Il docente distingue la convergenza di numeri dalla convergenza di variabili aleatorie (che sono funzioni).
    - **Convergenza in Distribuzione**: $\frac{1}{\sqrt{n}} \sum_{i=1}^n X_i \xrightarrow{d} \mathcal{N}(0, \sigma^2)$. Significa che le probabilità di superare certi livelli seguono la normale.
    - **Legge dei Grandi Numeri**:
        - *Debole*: Convergenza in probabilità.
        - *Forte*: Convergenza con probabilità 1 (richiede la sommabilità dei termini, citando l'Lemma di Borel-Cantelli).
    - **Convergenza in Media Quadratica**: La varianza dell'errore tende a zero. Il docente sottolinea che questa è la base per l'**algoritmo del gradiente** nel Machine Learning: si spera che l'errore quadratico medio tenda a zero all'aumentare della taglia dei dati.
- **Condizioni Tacite**: La LGN vale anche per variabili asintoticamente indipendenti (teoremi ergodici), ovvero quando la dipendenza ha "memoria finita".
- **Punti Critici**: La non-convessità è il problema principale del gradiente discendente; se la funzione non è strettamente convessa, possono esistere minimi locali.

### 3. Teoria della Decisione Bayesiana
- **Spiegazione Teorica**: Si assume che la natura si trovi in uno stato $H_i \in \{H_1, \dots, H_m\}$. Ogni stato $H_i$ determina una legge di probabilità $P(X^{(n)}|H_i)$ per i dati osservati.
- **Regola di Decisione**: Una funzione $d: X^{(n)} \rightarrow \{1, \dots, m\}$ che mappa i dati a una decisione.
- **Approccio Bayesiano**:
    - Si utilizza una **Matrice dei Costi** $C_{i,j}$, dove $C_{i,j}$ è il costo della decisione $i$ dato lo stato reale $j$.
    - **Rischio Medio Bayesiano ($R_B$)**: 
      $$R_B = \sum_{i=1}^m \sum_{j=1}^m C_{i,j} P(d(x^{(n)}) = i, H_j)$$
    - **Regola Ottima**: La regola che minimizza $R_B$.
- **Regole Specifiche**:
    - **MAP (Maximum A Posteriori)**: Sceglie l'ipotesi che massimizza $P(H_i | X^{(n)})$.
    - **ML (Maximum Likelihood)**: Sceglie l'ipotesi che massimizza $P(X^{(n)} | H_i)$. Se le probabilità a priori sono uguali, MAP coincide con ML.
- **Condizioni Tacite**: Si assume una partizione dell'insieme degli osservabili (le regioni di decisione $\Omega_i$ sono disgiunte, escludendo la *fuzzy logic*).

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio: Classificazione Binaria di Sorgenti con Probabilità Diverse
- **Testo**: Due sorgenti senza memoria emettono stringhe binarie di lunghezza $n$. La sorgente 1 emette '1' con probabilità $P_1$, la sorgente 2 con probabilità $P_2$ ($P_1 > P_2$). Si assume che le probabilità a priori siano uguali ($P(H_1) = P(H_2) = 0.5$). Determinare la regola di decisione ottima e la soglia di decisione.
- **Risoluzione Passo-Passo**:
  1. **Definizione PMF**: Poiché le sorgenti sono senza memoria, la PMF congiunta è il prodotto delle marginali. Per un vettore con peso di Hamming $W_H$ (numero di '1'):
     $$P(x^{(n)}|H_1) = P_1^{W_H} (1-P_1)^{n-W_H}$$
     $$P(x^{(n)}|H_2) = P_2^{W_H} (1-P_2)^{n-W_H}$$
  2. **Regola MAP/ML**: Dato $P(H_1) = P(H_2)$, la regola ottima sceglie $H_1$ se:
     $$P(x^{(n)}|H_1) > P(x^{(n)}|H_2)$$
  3. **Semplificazione Logaritmica**: Si applica il logaritmo (funzione monotona crescente) per linearizzare l'esponente:
     $$W_H \ln(P_1) + (n - W_H) \ln(1 - P_1) > W_H \ln(P_2) + (n - W_H) \ln(1 - P_2)$$
  4. **Isolamento del Peso di Hamming**:
     $$W_H [\ln(P_1) - \ln(P_2) + \ln(1 - P_1) - \ln(1 - P_2)] > n [\ln(P_2) - \ln(1 - P_2)]$$
     *(Nota: Il docente semplifica la forma finale riportando la soglia $\eta$)*:
     $$W_H > \frac{n \ln\left(\frac{1-P_2}{1-P_1}\right)}{\ln\left(\frac{P_1}{P_2}\right) + \ln\left(\frac{1-P_2}{1-P_1}\right)}$$
  5. **Risultato Finale**: La regola di decisione ottima consiste nel contare gli '1' nella sequenza e decidere $H_1$ se il peso di Hamming supera la soglia $\eta$.
- **Concetti Applicati**: PMF congiunte, Regola MAP, Peso di Hamming, Semplificazione tramite logaritmi.
- **Semplificazioni/Trucchi**: Il docente osserva che se la funzione è monotona crescente, il confronto tra le quantità non cambia il risultato del test (es. uso del logaritmo).

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    *   **Inferenza vs Deduzione**: L'inferenza è un processo *bottom-up* (dai dati alla popolazione), non una semplice deduzione top-down.
    *   **Convergenza**: Una variabile aleatoria non è un numero, ma una funzione; la sua convergenza deve essere trattata con attenzione rispetto alla convergenza di una successione numerica.
- **Chiarimenti Metodologici**:
    *   La distinzione tra statistica descrittiva e inferenziale sfuma alla luce dei **teoremi ergodici**, che tuttavia non verranno approfonditi in questo corso.
    *   **Fuzzy Logic**: Il docente specifica che, nel contesto della teoria della decisione presentata, le regioni di decisione sono disgiunte (l'intersezione è vuota).
- **Punti Critici per l'Esame**:
    *   Comprensione del perché la minimizzazione del rischio bayesiano equivale alla minimizzazione della probabilità d'errore quando i costi diagonali della matrice $C$ sono nulli.
    *   Distinzione tra convergenza in probabilità (LGN debole) e convergenza con probabilità 1 (LGN forte).

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione
- **Propedeuticità e Prerequisiti**:
    *   **Analisi Matematica**: Successioni, convergenza.
    *   **Probabilità**: Variabili aleatorie, PMF, variabili di Bernoulli, binomiali.
- **Consigli di Studio Espliciti**:
    *   "Non voglio sentire memoria ma logica": Il docente invita a comprendere il meccanismo logico dietro le formule.
    *   Studiare la convergenza in media quadratica per capire le basi del Machine Learning (Gradient Descent).

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Lemma di Borel-Cantelli**: Citato come condizione sufficiente per la convergenza con probabilità 1.
- **Esempio della Moneta**: Utilizzato per illustrare il passaggio da probabilità a priori a probabilità a posteriori in base all'osservazione di dati (es. 100 lanci con 70 teste).