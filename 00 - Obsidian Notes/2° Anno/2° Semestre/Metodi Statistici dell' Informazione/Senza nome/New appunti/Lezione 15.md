# SBOBINA - Statistica e Teoria dell'Informazione | Lezione su Variabili Continue e Teorema Centrale del Limite

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Nome/Corso non specificato]
- **Docente**: [Nome non specificato]
- **Orari e Aule**: Informazione non menzionata nella lezione.
- **Organizzazione Didattica**:
    - **CFU e Ore**: Informazione non menzionata nella lezione.
    - **Modalità di erogazione**: Lezione frontale (con uso di lavagna e webcam).
- **Ricevimento e Supporto**: Informazione non menzionata nella lezione.
- **Avvisi, Calendario e Assenze**:
    - **Nuovi materiali**: Il docente informerà stasera l'invio di un nuovo blocco di appunti sulla **statistica inferenziale**.
    - **Prossima lezione**: Introduzione ai teoremi di decisione statistica ottimale.
- **Accesso ai Materiali**: Informazione non menzionata nella lezione.

---

## 🎯 SOMMARIO RAPIDO
- **Revisione Covarianza**: Generalizzazione della matrice di covarianza a vettori $n$-dimensionali.
- **Quantizzazione e Probabilità Discrete**: Conversione da variabili continue a discrete e calcolo di PDF/CDF.
- **Combinazioni Lineari Gaussiane**: Proprietà della varianza e delle medie per variabili congiuntamente Gaussiane.
- **Distribuzioni Miste e Medie Condizionali**: Calcolo di medie e varianze per variabili dipendenti e indipendenti tramite la legge della probabilità totale.
- **Rate Distortion Theory**: Ottimizzazione della quantizzazione a 1 bit per minimizzare l'errore quadratico medio.
- **Teorema Centrale del Limite (CLT)**: Dimostrazione formale tramite Funzioni Generatrici dei Momenti (MGF).
- **Introduzione alla Teoria dell'Informazione**: Trasmissione parallela su canali binari simmetrici e regole di fusione dei dati (Bayes).

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| **CDF** | $F_X(x)$ | Funzione di Distribuzione Cumulativa: $P(X \le x)$. |
| **PDF** | $f_x(x)$ | Funzione di Densità di Probabilità per variabili continue. |
| **PMF** | $P(Y=y)$ | Funzione di Probabilità di Massa per variabili discrete. |
| **Covarianza** | $\text{Cov}(x,y)$ | Misura del grado di variazione congiunta tra due variabili. |
| **Correlazione** | $\rho_{1,2}$ | Rapporto tra covarianza e prodotto delle deviazioni standard: $\rho_{1,2} = \frac{\text{Cov}(x_1, x_2)}{\sigma_1 \sigma_2}$. Valore $\in [-1, 1]$. |
| **MGF** | $M_X(s)$ | Funzione Generatrice dei Momenti: $E[e^{sX}]$. |
| **Quantizzazione** | - | Processo di conversione da segnale continuo a discreto tramite partizionamento. |
| **Regioni di Voronoi** | - | Sottoinsiemi del dominio di una variabile discreta che definiscono i livelli di quantizzazione. |
| **Rate Distortion Theory** | - | Teoria che studia il compromesso tra tasso di bit (quantizzazione) e distorsione (errore). |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Revisione Matrice di Covarianza
Il docente ha ricordato la struttura del passaggio da variabili singole a vettoriali:
- Per una coppia di variabili $(x_1, x_2)$, il vettore delle medie è $2 \times 1$ e la **matrice di covarianza** è $2 \times 2$.
- Il coefficiente di correlazione $\rho_{1,2}$ è definito come $\frac{\text{Cov}(x_1, x_2)}{\sigma_1 \sigma_2}$.
- **Generalizzazione**: Per un vettore $n$-dimensionale, la matrice di covarianza è una matrice $n \times n$.
- *Nota*: Questo argomento è fondamentale per la statistica inferenziale.

### 2. Quantizzazione e Variabili Discrete
Il docente ha introdotto il concetto di **quantizzazione** come conversione da variabile continua a discreta (es. conversione analogico-digitale).
- **Gradi di libertà nella quantizzazione**:
    1.  **Suddivisione dell'alfabeto**: Partizionare l'alfabeto continuo in $2^r$ sottoinsiemi disgiunti (dove $r$ è il numero di bit).
    2.  **Valore di rappresentazione**: Scegliere quale valore $\hat{x}_i$ rappresenta la $i$-esima regione.
- **Regioni di Voronoi**: Sono i sottoinsiemi di dominio che definiscono i livelli di quantizzazione del convertitore A/D.

### 3. Rate Distortion Theory
Introduzione alla branca della teoria dell'informazione che mette in relazione:
- **Tasso di quantizzazione**: Numero di bit spesi per campione.
- **Distorsione**: Errore tollerato (differenza tra valore reale $x$ e rappresentato $\hat{x}$).
- *Principio*: Maggiore è il numero di bit, minore è la minima distorsione ottenibile. La trasformazione è **irreversibile** (codifica con perdita).

### 4. Teorema Centrale del Limite (CLT)
Il docente ha fornito una dimostrazione formale del CLT tramite le Funzioni Generatrici dei Momenti (MGF).
- **MGF della Gaussiana**: Per una variabile $X \sim N(\mu, \sigma^2)$, la MGF è $M_X(s) = e^{\mu s + \frac{\sigma^2 s^2}{2}}$.
- **Dimostrazione CLT**:
    - Si considera la somma $Z_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n X_i$ con $X_i$ indipendenti, identicamente distribuiti (i.i.d.) con media 0 e varianza $\sigma^2$.
    - La MGF di $Z_n$ è $M_{Z_n}(s) = [M_X(s/\sqrt{n})]^n$.
    - Sviluppo di Taylor (serie di Maclaurin) per $M_X(s/\sqrt{n})$: $1 + \frac{\sigma^2 s^2}{2n} + o(\frac{1}{n})$.
    - Al limite $n \to \infty$, $M_{Z_n}(s) \to e^{\frac{\sigma^2 s^2}{2}}$, che è la MGF di una Gaussiana $N(0, \sigma^2)$.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Quantizzazione di una Variabile Continua
- **Testo**: Variabile $x$ con PDF $f_x(x) = \frac{1}{\pi(1+x^2)}, x \in \mathbb{R}$. Sottoposta a quantizzazione a 2 bit in 4 valori: $y \in \{-3, -1, 1, 3\}$.
- **Risoluzione Passo-Passo**:
    1.  **Calcolo della CDF $F_X(x)$**:
        $$F_X(x) = \int_{-\infty}^x \frac{1}{\pi(1+t^2)} dt = \frac{1}{\pi} \arctan(x) + \frac{1}{2}$$
        *(Verifica: $F_X(\infty) = 1$, $F_X(-\infty) = 0$)*.
    2.  **Definizione di $y$**:
        - $y = -3$ se $x \le -2$
        - $y = -1$ se $-2 < x \le 0$
        - $y = 1$ se $0 < x \le 2$
        - $y = 3$ se $x > 2$
    3.  **Calcolo della PMF di $y$**:
        - $P(Y = -3) = F_X(-2) = \frac{1}{2} - \frac{\arctan(2)}{\pi}$
        - $P(Y = -1) = F_X(0) - F_X(-2) = \frac{1}{2} - (\frac{1}{2} - \frac{\arctan(2)}{\pi}) = \frac{\arctan(2)}{\pi}$
        - Per simmetria (funzione pari): $P(Y=1) = P(Y=-1)$ e $P(Y=3) = P(Y=-3)$.
    4.  **Trasformazione $z = y^2$**:
        - $y^2$ assume solo i valori $\{1, 9\}$.
        - $P(Z = 1) = P(Y = 1) + P(Y = -1) = 2 \cdot \frac{\arctan(2)}{\pi}$
        - $P(Z = 9) = 1 - P(Z = 1)$
- **Concetti Applicati**: Calcolo integrali, trasformazione di variabili casuali, variabili discrete/continue.

### Esercizio 2: Combinazioni Lineari di Gaussiane
- **Testo**: $x, y$ congiuntamente Gaussiane, $\mu=0, \sigma^2=1, \rho=0.25$. Sia $z = 2x + 3y + 2$. Calcolare distribuzione di $z$, $P(|z - \mu_z| > 10)$ e $P(z > 7)$.
- **Risoluzione Passo-Passo**:
    1.  **Calcolo Media $\mu_z$**:
        $$\mu_z = 2\mu_x + 3\mu_y + 2 = 2(0) + 3(0) + 2 = 2$$
    2.  **Calcolo Varianza $\sigma_z^2$**:
        $$\sigma_z^2 = 4\sigma_x^2 + 9\sigma_y^2 + 2(2)(3)\text{Cov}(x,y)$$
        $$\text{Cov}(x,y) = \rho \sigma_x \sigma_y = 0.25 \cdot 1 \cdot 1 = 0.25$$
        $$\sigma_z^2 = 4(1) + 9(1) + 12(0.25) = 4 + 9 + 3 = 16 \implies \sigma_z = 4$$
    3.  **Probabilità $|z - \mu_z| > 10$**:
        - Corrisponde a $z - \mu_z > 10$ oppure $z - \mu_z < -10$.
        - Per simmetria: $P(|z - \mu_z| > 10) = 2 \cdot P(z - \mu_z > 10) = 2 \cdot Q\left(\frac{10}{\sigma_z}\right) = 2 \cdot Q(2.5)$.
    4.  **Probabilità $z > 7$**:
        - $P(z > 7) = Q\left(\frac{7 - 2}{4}\right) = Q(1.25)$.
- **Semplificazioni/Trucchi**: Il docente ricorda che sommando un fattore deterministico ($+2$) la varianza non cambia.

### Esercizio 3: Variabili Miste e Legge della Probabilità Totale
- **Testo**: $x \sim N(0,1), y \sim N(-3,4), \rho = -0.75, z \sim \text{Exp}(\mu=1), B \sim \text{Bern}(\alpha)$. Sia $W = 2x - 3yB + z(1-B)$. Determinare PDF, media e varianza.
- **Risoluzione Passo-Passo**:
    1.  **PDF di $W$ (Legge della Probabilità Totale)**:
        $$f_W(w) = P(B=1) f_{W|B=1}(w) + P(B=0) f_{W|B=0}(w)$$
        - Se $B=1$, $W = 2x - 3y$. Definiamo $U = 2x - 3y$.
        - Se $B=0$, $W = z$.
        $$f_W(w) = \alpha f_U(w) + (1-\alpha) f_Z(w)$$
    2.  **Analisi di $U = 2x - 3y$**:
        - $\mu_u = 2(0) - 3(-3) = 9$.
        - $\sigma_u^2 = 4\sigma_x^2 + 9\sigma_y^2 + 2(2)(-3)\text{Cov}(x,y)$.
        - $\text{Cov}(x,y) = (-0.75)(1)(2) = -1.5$.
        - $\sigma_u^2 = 4(1) + 9(4) + (-12)(-1.5) = 4 + 36 + 18 = 58$.
        - $U \sim N(9, 58)$.
    3.  **Media e Varianza di $W$**:
        - $\mu_W = \alpha \mu_u + (1-\alpha) \mu_z = 9\alpha + (1-\alpha)(1)$.
        - $E[W^2] = \alpha E[U^2] + (1-\alpha) E[Z^2]$.
        - $E[U^2] = \sigma_u^2 + \mu_u^2 = 58 + 81 = 139$.
        - $E[Z^2] = 2/\lambda = 2$ (per variabile esponenziale con $\mu=1$).
        - $\text{Var}(W) = E[W^2] - \mu_W^2$.
    4.  **Probabilità condizionata $P(|W| > 1 \mid |W| < 3)$**:
        - Calcolata tramite la definizione di probabilità condizionata: $\frac{P(|W| > 1 \cap |W| < 3)}{P(|W| < 3)}$.
        - L'intersezione $|W| > 1 \cap |W| < 3$ corrisponde a $W \in (-3, -1) \cup (1, 3)$.
        - Il denominatore è $F_W(3) - F_W(-3)$.

### Esercizio 4: Applicazione Atletica (Modellazione Gaussiana)
- **Testo**: Giulio ($G$) e Marco ($M$) corrono i 100m. Qualità di qualificazione: $T < 10.62$ s.
    - $G \sim N(10.72, 0.1^2)$ (10 centesimi).
    - $M \sim N(10.86, 0.27^2)$ (27 centesimi).
    - Variabili indipendenti.
- **Domande risolutive**:
    1.  **Chi ha più probabilità di qualificarsi?** Confrontare $P(G \le 10.62)$ e $P(M \le 10.62)$.
    2.  **Chi ha più probabilità di battere l'altro?**
        - Giulio batte Marco se $G < M \iff G - M < 0$.
        - Definiamo $D = G - M$. Poiché $G, M$ sono indipendenti e Gaussiane:
        - $D \sim N(\mu_G - \mu_M, \sigma_G^2 + \sigma_M^2)$.
        - Calcolare $P(D < 0)$.
- **Concetti Applicati**: Somma di variabili casuali indipendenti, proprietà della varianza.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    - **Somma di variabili**: Ricordare che quando si sommano variabili aleatorie e termini deterministici (es. $2x + 3y + 2$), la varianza non cambia.
    - **Indipendenza**: L'assunzione di indipendenza è cruciale per sommare le varianze ($\sigma^2_{G+M} = \sigma^2_G + \sigma^2_M$).
- **Chiarimenti Metodologici**:
    - La trasformazione da continuo a discreto tramite quantizzazione è irreversibile: si perde informazione.
    - Le medie condizionali non sono "trucchi" matematici ma concetti fondamentali per la statistica moderna.
- **Punti Critici per l'Esame**:
    - Dimostrazione del CLT tramite MGF (molto probabile come argomento teorico).
    - Calcolo di parametri di distribuzioni miste usando la legge della probabilità totale.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    - Buona cultura matematica e conoscenza delle distribuzioni base (Gaussiana, Esponenziale, Bernoulli).
- **Consigli di Studio Espliciti**:
    - "Non voglio sentire memoria ma logica".
    - Creare un formulario con le formule rilevanti per le Gaussiane e le MGF per velocizzare i calcoli.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Teoria dell'Informazione**: Citato il settore della *Rate Distortion Theory*.
- **Testi di riferimento**: Il docente suggerisce di consultare testi in lingua inglese per il termine *Central Limit Theorem (CLT)*.

---
*Sbobina prodotta automaticamente dall'assistente accademico.*