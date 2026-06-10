# Studio Guide: Metodi Statistici dell'Informazione

## Introduzione ai Metodi Statistici dell'Informazione

### 1. Il Concetto di Informazione e Incertezza
L'informazione è un concetto intrinsecamente legato all'**incertezza**. 
- Se non c'è incertezza su un risultato (ad esempio, una sorgente che trasmette solo zeri), non c'è informazione.
- Il processo di trasferimento di informazione (sia in telecomunicazioni che in informatica) consiste nel trasformare un'**incertezza a priori** in una **certezza posteriore**.
- L'informatica e le telecomunicazioni convergono verso il trattamento e il trasferimento dell'informazione attraverso strumenti probabilistici e statistici.

### 2. Approccio Frequentistico alla Probabilità
In questo corso, la probabilità viene approcciata in modo **frequentistico**:
- **Definizione Intuitiva:** La probabilità di un evento $A$ è il limite della sua frequenza di successo quando il numero di prove $n$ tende all'infinito.
- **Frequenza di Successo ($F_n(A)$):** Il rapporto tra il numero di volte in cui l'evento $A$ si verifica ($n_A$) e il numero totale di prove ($n$).
  $$F_n(A) = \frac{n_A}{n}$$
- **Probabilità ($P(A)$):**
  $$P(A) = \lim_{n \to \infty} F_n(A)$$
- **Proprietà Fondamentali:**
  - **Evento Impossibile:** Un evento che non può verificarsi (es. lanciare una moneta e che non esca né testa né croce).
  - **Evento Certo:** L'evento che contiene tutti i risultati possibili (lo spazio dei campioni $\Omega$).
  - **Complementare:** La probabilità di un evento complementare $\bar{A}$ è $P(\bar{A}) = 1 - P(A)$.
  - **Subadditività:** La probabilità dell'unione di due eventi è data dalla somma delle loro probabilità meno la probabilità della loro intersezione:
    $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
    *Nota: Se gli eventi sono incompatibili (intersezione vuota), allora $P(A \cup B) = P(A) + P(B)$.*

---

## Fondamenti di Analisi Combinatoria
Per calcolare le probabilità in spazi finiti, è necessario saper contare correttamente le diverse configurazioni possibili.

### 3. Spazio dei Campioni e Eventi
- **Spazio dei Campioni ($\Omega$):** L'insieme di tutti i risultati possibili di un esperimento. Può essere finito (discreto) o infinito (continuo).
- **Evento:** Un sottoinsieme dello spazio dei campioni.
- **Cardinalità ($|A|$):** Il numero di elementi contenuti in un insieme $A$.

### 4. Regole di Conteggio
#### A. Prodotto Cartesiano e Permutazioni
Se abbiamo $k$ scelte da fare e per ogni scelta ci sono $n_i$ opzioni possibili, il numero totale di sequenze ordinate è il prodotto delle cardinalità:
$$N = n_1 \times n_2 \times \dots \times n_k$$

#### B. Permutazioni (Ordine Importante)
- **Con ripetizione:** Se abbiamo $n$ elementi e ne scegliamo $k$ permettendo ripetizioni:
  $$N = n^k$$
- **Senza ripetizione:** Se abbiamo $n$ elementi e ne scegliamo $k$ senza ripetizioni:
  $$P(n, k) = \frac{n!}{(n-k)!} = n(n-1)(n-2)\dots(n-k+1)$$
  *Esempio: Quante sequenze di 3 cifre diverse si possono formare con 10 cifre? $10 \times 9 \times 8 = 720$.*

#### C. Combinazioni (Ordine NON Importante)
- **Senza ripetizione:** Se abbiamo $n$ elementi e ne scegliamo $k$ senza che l'ordine conti (es. una mano di carte):
  $$C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$
  *Esempio: Quante combinazioni di 5 carte si possono fare da un mazzo di 32? $\binom{32}{5} = 201.376$.*

#### D. Coefficienti Multinomiali
Si usano quando si vogliono contare le sequenze di lunghezza $n$ con elementi ripetuti. Se abbiamo simboli di un alfabeto di dimensione $m$ e vogliamo contare quante sequenze hanno esattamente $n_1$ volte il simbolo 1, $n_2$ volte il simbolo 2, ..., $n_m$ volte il simbolo $m$ (dove $\sum n_i = n$):
$$\frac{n!}{n_1! \times n_2! \times \dots \times n_m!}$$

---

## Probabilità Condizionata e Indipendenza

### 5. Probabilità Condizionata
La probabilità di un evento $B$ dato che si è verificato un evento $A$ (probabilità *a posteriori*) è il rapporto tra la probabilità che si verifichino entrambi e la probabilità dell'evento di condizionamento:
$$P(B|A) = \frac{P(A \cap B)}{P(A)}$$
*Condizione: $P(A) > 0$.*

### 6. Indipendenza
Due eventi $A$ e $B$ sono **indipendenti** se il verificarsi di uno non influenza la probabilità dell'altro. Matematicamente:
$$P(B|A) = P(B)$$
Ciò equivale a:
$$P(A \cap B) = P(A) \times P(B)$$
- *Esempio:* Il lancio di due dadi indipendenti. La probabilità di ottenere 5 sul primo e 2 sul secondo è $P(5) \times P(2) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$.

---

## Variabili Aleatorie e Caratterizzazione

### 7. Definizione di Variabile Aleatoria
Una variabile aleatoria $X$ è un'applicazione dallo spazio dei campioni di uno spazio di probabilità a un insieme numerico.
- **Variabile Discreta:** Assume valori in un insieme numerabile (es. conteggio di successi).
- **PMF (Probability Mass Function):** Caratterizza la probabilità che $X$ assuma ogni valore del suo alfabeto. La somma di tutte le probabilità deve essere uguale a 1.
- **Media Statistica ($E[X]$):** La media dei valori assunti pesata per le loro probabilità.
- **Varianza ($\sigma^2_X$):** Misura la dispersione della variabile rispetto alla sua media. La varianza è un operatore quadratico (invariante per traslazione $b$, covariante per scalatura $a$): $\sigma^2_{aX+b} = a^2 \sigma^2_X$.

### 8. Caratterizzazione Condizionale
Data una variabile aleatoria $X$ e un evento $A$, possiamo definire la **PMF condizionale** di $X$ dato $A$.
- Se la condizione $A$ è fissa, essa può definire una nuova legge di probabilità che permette di studiare la distribuzione di $X$ su un sottoinsieme del dominio.
- **Filtro/Potatura (Data Analysis):** Permette di escludere "outliers" o dati non rilevanti per focalizzare l'analisi su una regione di interesse (es. altezze tra 1.50 e 1.70 m).

### 9. Teoremi Fondamentali e Convergenza
- **Legge dei Grandi Numeri (LLN):** La media campionaria $\bar{X}$ converge alla media statistica $\mu$ quando il numero di prove $n \to \infty$.
- **Convergenza in Media Quadratica:** La differenza tra la media campionaria e la media statistica tende a zero in modo quadratico.
- **Devianza di Chebyshev:** Fornisce un limite sulla probabilità che una variabile aleatoria si discosti dalla sua media:
  $$P(|X - \mu| \ge k\sigma_X) \le \frac{1}{k^2}$$
  Questo garantisce che la variabile sia "concentrata" vicino alla sua media se $\sigma_X$ è piccola.

---

## Teorie Avanzate e Applicazioni

### 10. Binomiale e Poissoniana
- **Distribuzione Binomiale ($\text{Bin}(n, p)$):** Modella il numero di successi in $n$ prove indipendenti con probabilità di successo $p$.
- **Distribuzione di Poisson:** Modella il numero di eventi che avvengono in un intervallo continuo (es. numero di macchine in coda, numero di pacchetti in un router). Parametrizzata dalla media $\lambda$.

### 11. Informazione e Compressione
- **Redondanza:** Molte sequenze (testi, immagini) contengono pattern ripetitivi che rendono la loro rappresentazione non ottimale.
- **Compressione (ZIP, Lempel-Ziv):** Algoritmi che sfruttano la caratterizzazione statistica delle stringhe per ridurre la loro lunghezza, avvicinandosi al limite della compressibilità informazionale.
- **Indipendenza di Ordine:** In una sequenza di $n$ bit indipendenti, la congiunta è il prodotto delle marginali. In una sequenza dipendente (es. codice con bit di parità), le marginali non bastano a descrivere la congiunta.

### 12. Esempi Pratici Analizzati
- **Lancio di dadi:** Calcolo della probabilità di ottenere almeno un 6 in 5 lanci ($1 - (\frac{5}{6})^5$).
- **Poker:** Calcolo della probabilità di avere una coppia d'assi, un tris di 7, o un colore di picche, escludendo punteggi più alti.
- **Database di Altezza/Peso:** Esempio di condizionamento sulla popolazione residente in Italia.
- **Modello Martingala:** Studio del raddoppio della puntata e dei suoi limiti statistici nel lungo termine.
