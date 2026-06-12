# SBOBINA - PROCESSI ALEATORI | LEZIONE SUI PROCESSI STAZIONARI E CATENE DI MARKOV

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Teoria della Probabilità / Statistica (Processi Aleatori)
- **Docente**: [Non specificato nella trascrizione]
- **Orari e Aule**: [Dettagli non forniti]
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione frontale/didattica concettuale.
    - **Prossime lezioni**:
        - **Lunedì**: Recupero e risoluzione esercizi sulle Catene di Markov.
        - **Martedì e Giovedì**: Inizio modulo "Statistica Inferenziale" (Teoria della Decisione, Teoria della Stima).
- **Ricevimento e Supporto**: Il docente invita a scrivere per chiarire i dubbi relativi alle ultime due lezioni.
- **Avvisi, Calendario e Assenze**:
    - Il docente informerà sui nuovi materiali da caricare lunedì.
- **Accesso ai Materiali**:
    - Il docente pubblicherà un nuovo blocco di appunti intitolato **"Elements of Inferential Statistics"**.
- **Consigli pratici del docente**:
    - **Fondamenti necessari**: È indispensabile saper eseguire correttamente le operazioni sulle matrici (moltiplicazione, riduzione per righe e colonne) provenienti dal corso di Geometria.
    - **Focus**: Nonostante la complessità teorica, molti passaggi saranno risolti tramite operazioni matriciali standard.

---

## 🎯 SOMMARIO RAPIDO
- Definizione di **Processo Aleatorio** e analisi delle dipendenze temporali e spaziali.
- Studio della **Stazionarietà** (ordine $M$ e in senso lato) e della non-stazionarietà della natura.
- Caratterizzazione statistica tramite **Matrici di Covarianza** e proprietà delle matrici (Teplitz, definite positive).
- Teoria delle **Catene di Markov**: transizioni, matrici stocastiche e distribuzioni stazionarie tramite autovettori.
- Applicazione pratica: Codifica di sequenze con vincoli attraverso modelli Markoviani.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Processo Aleatorio | $\{X_n\}$ | Una sequenza di variabili aleatorie associate a un indice temporale $n$. |
| Spazio Campionario | $\Omega$ | L'insieme di tutti i risultati possibili del processo. |
| Stazionarietà di ordine $M$ | - | Un processo è stazionario di ordine $M$ se la PMF congiunta di $M$ simboli è invariante per traslazioni rigide. |
| Stazionarietà in senso lato | - | Processo in cui la media $\mathbb{E}[X_n]$ non dipende da $n$ e la covarianza dipende solo dalla differenza $|n_1 - n_2|$. |
| Matrice di Covarianza | $\mathbf{C}$ | Matrice dove gli elementi diagonali sono le varianze $\sigma^2$ e gli elementi fuori diagonale sono le covarianze tra $X_i$ e $X_j$. |
| Matrice Teplitz | - | Matrice in cui ogni diagonale è costante (comune nelle matrici di covarianza dei processi stazionari). |
| Catena di Markov | - | Processo aleatorio in cui la probabilità dello stato futuro dipende solo dallo stato attuale e non dalla storia passata. |
| Matrice di Transizione | $\mathbf{P}$ | Matrice che descrive le probabilità di transizione tra gli stati di una catena di Markov. |
| Matrice Stocastica | - | Matrice in cui la somma degli elementi di ogni riga è uguale a 1. |
| Matrice Doppiamente Stocastica | - | Matrice in cui la somma degli elementi di ogni riga e di ogni colonna è uguale a 1. |
| Distribuzione Stazionaria | $\mathbf{q}$ | Distribuzione di probabilità che rimane invariante dopo una transizione ($\mathbf{q} = \mathbf{P}^T \mathbf{q}$). |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Definizione di Processo Aleatorio
Il docente chiarisce che un processo aleatorio associa a ogni elemento $\omega$ dello spazio campionario $\Omega$ non un singolo numero, ma una **sequenza di numeri**.
- **Variabili di riferimento**: Il processo dipende da due variabili: l'**indice temporale** ($n$) e l'elemento dello **spazio campione** ($\omega$).
    - Se si fissa $\omega$ e si varia $n$, si ottiene una specifica realizzazione (sequenza).
    - Se si fissa $n$ e si varia $\omega$, si ottiene una **variabile aleatoria**.
- **Esempio della Camera Numerica**: Il docente usa l'analogia della ripresa video. I frame adiacenti sono fortemente correlati (es. un pixel nero rimane nero nei frame successivi). Se ci focalizziamo su un singolo pixel nel tempo, osserviamo un processo aleatorio la cui dipendenza tra istanti vicini è molto forte.

### 2. Stazionarietà e non-stazionarietà
Il concetto di stazionarietà è fondamentale per la possibilità di applicare leggi di compressione.
- **Stazionarietà di ordine $M$**: Un processo è stazionario di ordine $M$ se la PMF congiunta di un blocco di $M$ simboli non cambia indipendentemente dalla sua posizione sull'asse temporale (invarianza per traslazione rigida).
    - *Nota*: La stazionarietà di ordine $M$ implica la stazionarietà degli ordini inferiori, ma non necessariamente di quelli superiori.
- **Stazionarietà in senso lato**: Un processo è stazionario in senso lato se:
    1. La media $\mathbb{E}[X_n]$ non dipende da $n$.
    2. La covarianza $\text{Cov}(X_{n_1}, X_{n_2})$ dipende solo dalla differenza $|n_1 - n_2|$.
- **Non-stazionarietà della Natura**: Il docente sottolinea che il mondo reale raramente è stazionario su scale temporali ampie. 
    - *Esempio del traffico*: Il traffico a mezzogiorno è diverso da quello a mezzanotte; il traffico del 2000 è diverso da quello del 900. Per modellare tali fenomeni servono algoritmi adattativi che "riapprendano" le caratteristiche della natura su scale temporali lunghe.
    - *Esempio delle scale temporali*: Su una rete a 3 Gb/s, l'infinito "arriva subito" (3 miliardi di bit in un secondo).

### 3. Processi Base e Caratterizzazione
- **Processo di Bernoulli**: Esempio con alfabeto $\{1, -1\}$ o $\{0, 1\}$.
- **Processo Indipendente**: Non vi è dipendenza statistica tra gli elementi. In questo caso, la stazionarietà di primo ordine implica la stazionarietà di ogni ordine.
- **Processo Quaternario Uniforme**: Alfabeto di 4 valori assunti con uguale probabilità.

### 4. Matrici di Covarianza e Proprietà
Per un vettore aleatorio di ordine $n$, la caratterizzazione sintetica è data dal vettore delle medie e dalla **matrice di covarianza**.
- **Struttura**: La diagonale contiene le varianze $\sigma_i^2$. L'elemento $ij$ contiene la covarianza tra $X_i$ e $X_j$ (simmetrica: $a_{ij} = a_{ji}$).
- **Matrice Teplitz**: Nei processi stazionari, la matrice di covarianza assume spesso la forma di matrice Teplitz (diagonali costanti).
- **Matrice Definita Positiva**: Il docente ricorda che una matrice $\mathbf{C}$ è definita non negativa se $\mathbf{x}^T \mathbf{C} \mathbf{x} \geq 0$ per ogni vettore $\mathbf{x} \neq 0$. Questa è una proprietà fondamentale delle matrici di covarianza.

### 5. Catene di Markov
Un processo è di Markov se la probabilità di uno stato futuro dipende solo dallo stato attuale, indipendentemente dalla storia passata.
- **Proprietà di Memoria Corta**: $P(Y_n | Y_{n-1}, Y_{n-2}, \dots, Y_0) = P(Y_n | Y_{n-1})$.
- **Esempi Citati**:
    - *Posizione del Re*: Sulla scacchiera, la posizione del re al tempo $t=4$ dipende dalla posizione al tempo $t=3$. Se conosco la posizione al tempo $t=3$, la storia precedente è irrilevante.
    - *Passeggiata Aleatoria su Grafo*: Una passeggiata casuale su un grafo non orientato è una catena di Markov dove la probabilità di transizione è data dal peso dei rami entranti normalizzati.
- **Matrici di Transizione ($\mathbf{P}$)**: 
    - Somma delle righe = 1 $\rightarrow$ **Matrice Stocastica**.
    - Somma delle righe e delle colonne = 1 $\rightarrow$ **Matrice Doppiamente Stocastica**.
- **Distribuzione Stazionaria e Teorema di Perron-Frobenius**:
    - La distribuzione stazionaria $\mathbf{q}$ è l'autovettore corrispondente all'autovalore unitario ($\lambda = 1$) della matrice di transizione $\mathbf{P}$.
    - Equazione: $\mathbf{q} = \mathbf{P}^T \mathbf{q}$.
    - Il Teorema di Perron-Frobenius garantisce che, sotto opportune condizioni, la distribuzione di probabilità evolva verso una distribuzione limite che coincide con quella stazionaria, indipendentemente dalla condizione iniziale.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Processo Cosinusoidale e Stazionarietà
- **Testo**: Considerare il processo $X_n = \cos(2\pi \cdot 0 \cdot n + \phi)$, dove $\phi$ è una variabile aleatoria uniforme su $[-\pi, \pi]$.
- **Risoluzione Passo-Passo**:
    1. **Calcolo della Media**: $\mathbb{E}[X_n] = \int_{-\pi}^{\pi} \cos(2\pi \cdot 0 \cdot n + \phi) \cdot f(\phi) d\phi$. Poiché l'integrale del coseno su un periodo intero è zero, $\mathbb{E}[X_n] = 0$. La media non dipende da $n$.
    2. **Calcolo della Covarianza**: $\text{Cov}(X_{n_1}, X_{n_2}) = \mathbb{E}[X_{n_1}X_{n_2}] - \mathbb{E}[X_{n_1}]\mathbb{E}[X_{n_2}]$.
    3. **Semplificazione**: Poiché la media è zero, la covarianza è $\mathbb{E}[\cos(2\pi \cdot 0 \cdot n_1 + \phi)\cos(2\pi \cdot 0 \cdot n_2 + \phi)]$. Utilizzando l'identità trigonometrica $\cos(A)\cos(B) = \frac{1}{2}(\cos(A-B) + \cos(A+B))$, si nota che il termine dipende dalla differenza $(n_2 - n_1)$.
    4. **Conclusione**: Il processo è **stazionario in senso lato** perché la media è costante e la covarianza dipende solo dalla distanza temporale.

### Esercizio 2: Codifica con Vincoli (Evitare zeri consecutivi)
- **Testo**: Codificare una sorgente binaria tale da non ammettere due zeri consecutivi.
- **Risoluzione Passo-Passo**:
    1. **Identificazione degli Stati**: Per evitare due zeri consecutivi, lo stato deve essere definito dagli ultimi due bit emessi.
    2. **Analisi delle Transizioni**:
        - Stato $(0,1)$: Se arriva un $0 \rightarrow$ nuovo stato $(1,0)$. Se arriva un $1 \rightarrow$ nuovo stato $(1,1)$.
        - Stato $(1,0)$: Se arriva un $0 \rightarrow$ **impossibile** (vincolo). Se arriva un $1 \rightarrow$ nuovo stato $(0,1)$.
        - Stato $(1,1)$: Se arriva un $0 \rightarrow$ nuovo stato $(1,0)$. Se arriva un $1 \rightarrow$ nuovo stato $(1,1)$.
    3. **Modellazione**: Questo può essere schematizzato come una catena di Markov dove alcuni stati di transizione hanno probabilità zero.
    4. **Conclusione**: Il vincolo di codifica può essere modellato matematicamente come un processo di Markov, permettendo una caratterizzazione completa tramite matrici di transizione.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    - Confondere la stazionarietà di ordine $M$ con la stazionarietà generale: un processo può essere stazionario al primo ordine ma non al secondo.
    - Confondere l'indipendenza con la stazionarietà: l'indipendenza è una condizione molto più forte e specifica.
- **Chiarimenti Metodologici**:
    - La natura non è stazionaria su scale macroscopiche; la stazionarietà è un'approssimazione valida solo su scale temporali brevi o specifiche.
    - L'uso delle matrici di transizione è un potente strumento di sintesi: permette di passare da una descrizione complessa di dipendenze a una semplice analisi di autovettori.
- **Punti Critici per l'Esame**:
    - Sapere dimostrare perché $\lambda = 1$ è un autovalore di una matrice di transizione (matrice singolare perché le righe sono linearmente dipendenti).
    - Comprendere la differenza tra processo indipendente e catena di Markov.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: [Non specificata]
- **Propedeuticità e Prerequisiti**:
    - **Geometria**: Fondamentale la padronanza delle operazioni matriciali (riduzioni, prodotti, determinanti).
- **Consigli di Studio Espliciti**:
    - "Non voglio sentire memoria ma logica".
    - Ripassare attentamente le ultime due lezioni prima di passare alla statistica inferenziale.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Elements of Inferential Statistics** (Nuovo blocco di appunti da consultare).
- **Geometria** (Per il recupero delle operazioni matriciali).