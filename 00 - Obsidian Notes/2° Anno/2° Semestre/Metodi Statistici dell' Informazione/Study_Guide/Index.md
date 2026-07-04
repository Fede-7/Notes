# 📘 LIBRO DI METODI STATISTICI (Master Edition - Corso Prof. Lops)

## PARTE I: Teoria della Probabilità, Convergenza e Fondamenti
**Capitolo 1: Logica della Probabilità e Variabili Casuali**
*   1.1 Definizione di Esperimento Casuale, Spazio Campionario ($\Omega$) e Eventi.
*   1.2 Gli Assiomi della Probabilità (Kolmogorov).
*   1.3 Probabilità Condizionata e Teorema della Probabilità Totale.
*   1.4 **Teorema di Bayes:** Definizione, Derivazione e Interpretazione.
*   1.5 Variabili Casuali (Random Variables): Discrete vs Continue.
*   1.6 Funzioni di Probabilità, Funzioni di Densità (PDF) e di Ripartizione (CDF).
*   1.7 Momenti di una Variabile Casuale: Attesa (Media) e Varianza.
*   1.8 Covarianza e Correlazione: Proprietà algebriche e Interpretazione Geometrica.
*   1.9 **Diseguaglianza di Markov:** Teoria, Derivazione e Implicazioni sulla concentrazione della probabilità.
*   1.10 **Analisi della Convergenza:** Distinzioni formali tra Convergenza in Probabilità, Quasi Certa e in Media Quadratica (L2).

**Capitolo 2: Distribuzioni di Probabilità Fondamentali**
*   2.1 Distribuzioni Discrete:
    *   2.1.1 Bernoulli e Binomiale (Parametri, Media, Varianza).
    *   2.1.2 Distribuzione di Poisson (Applicazioni e Proprietà).
    *   2.1.3 *Dimostrazione:* Derivazione della Poisson come limite della Binomiale ($n \to \infty, p \to 0$).
*   2.2 Distribuzioni Continue:
    *   2.2.1 Distribuzione Uniforme.
    *   2.2.2 Distribuzione Esponenziale (*Dimostrazione della Proprietà di "Assenza di Memoria"*).
    *   2.2.3 Distribuzione Normale (Gaussiana): Caratteristiche e Regola Empirica.
    *   2.2.4 **Distribuzioni Specifiche:** Distribuzione di Laplace e Distribuzione di Rayleigh.
*   2.3 Distribuzioni Speciali per l'Inferenza:
    *   2.3.1 Distribuzione $\chi^2$ (Chi-quadrato).
    *   2.3.2 Distribuzione $t$ di Student (Derivazione e Differenza dalla Normale).
    *   2.3.3 Distribuzione $F$ di Fisher.
    *   2.3.4 **Distribuzione di Cauchy:** Modellizzazione del rumore atmosferico e proprietà di non-convergenza.
*   2.4 Funzioni Generatrici dei Momenti (MGF) e Funzioni Caratteristiche.

**Capitolo 3: Teoremi Limite e Teoria del Campionamento**
*   3.1 Legge dei Grandi Numeri (WLLN): Teorema di convergenza della media campionaria.
*   3.2 **Teorema del Limite Centrale (CLT):**
    *   3.2.1 Definizione e Significato.
    *   3.2.2 *Dimostrazione Matematica* (tramite MGF e Funzioni Caratteristiche).
*   3.3 Tecniche di Campionamento (Semplice, Stratificato, a Conglomerati).
*   3.4 Distribuzioni Campionarie: Media Campionaria ($\bar{X}$) e Varianza Campionaria ($S^2$).
*   3.5 Errore Standard e Determinazione della Dimensione Campionaria.

---

## PARTE II: Statistica Descrittiva e Analisi dei Dati
**Capitolo 4: Analisi dei Dati Descrittiva**
*   4.1 Misure di Tendenza Centrale: Media, Mediana, Moda.
*   4.2 Misure di Dispersione: Varianza, Deviazione Standard, Range, IQR.
*   4.3 Shape dei Dati: Asimmetria (Skewness) e Curtosi.
*   4.4 Visualizzazione dei Dati: Istogrammi, Boxplot, Grafici a Dispersione, Diagrammi a Barre.

**Capitolo 5: Strategie di Gioco e Interpretazione Frequentista**
*   5.1 Interpretazione Frequentista della Probabilità.
*   5.2 **Strategie di Gioco:** Analisi delle strategie di puntata fissa.
*   5.3 **Martingala:** Concetti base e applicazioni.

---

## PARTE III: Inferenza Statistica e Teoria della Decisione
**Capitolo 6: Stima dei Parametri e Metodi Avanzati**
*   6.1 Stima Puntuale: Concetti di Unbiasedness (Non Distorsione) ed Efficienza.
*   6.2 **Metodo della Massima Verosimiglanza (MLE):**
    *   6.2.1 Teoria Generale del Massimo di Verosimiglianza.
    *   6.2.2 *Dimostrazione:* Calcolo degli stimatori MLE per distribuzioni comuni.
*   6.3 **Informazione di Fisher e Limite di Cramér-Rao:**
    *   6.3.1 Definizione dell'Informazione di Fisher.
    *   6.3.2 Dimostrazione del Limite di Cramér-Rao per l'efficienza degli stimatori.
*   6.4 **Approccio Bayesiano e Teoria della Decisione:**
    *   6.4.1 Minimizzazione del Rischio Bayesiano tramite la funzione di costo quadratica.
    *   6.4.2 Distinzione critica per parametri continui (Probabilità di errore vs Rischio).
*   6.3 **Stima degli Intervalli di Confidenza:**
    *   6.3.1 Intervalli per la Media ($\mu$) con varianza nota e ignota.
    *   6.3.2 Intervalli per la Proporzione.

**Capitolo 7: Test di Ipotesi e Ottimizzazione**
*   7.1 Logica del Test: Ipotesi Nulla ($H_0$), Ipotesi Alternativa ($H_1$).
*   7.2 Errori di Tipo I ($\alpha$) e Tipo II ($\beta$).
*   7.3 **Potenza del Test** e Relazione con la Dimensione Campionaria.
*   7.4 Valore p (p-value): Definizione, Interpretazione e Critiche.
*   7.5 **Lemma di Neyman-Pearson:** Teoria dell'ottimizzazione vincolata per la massima potenza.
*   7.6 Test Parametrici: Test Z, Test t, Test $\chi^2$ di Indipendenza e Bontà dell'Adattamento, Test F.

---

## PARTE IV: Regressione Lineare e ANOVA
**Capitolo 8: Regressione Lineare Semplice**
*   8.1 Il Modello Lineare: $Y = \beta_0 + \beta_1 X + \epsilon$.
*   8.2 **Metodo dei Minimi Quadrati Ordinari (OLS):**
    *   8.2.1 *Dimostrazione:* Minimizzazione della Somma dei Quadrati degli Errori (SSE).
    *   8.2.2 Proprietà degli stimatori $\hat{\beta}_0$ e $\hat{\beta}_1$.
*   8.3 **Teorema di Gauss-Markov:** Dimostrazione dell'efficienza degli stimatori OLS.
*   8.4 Correlazione vs Causalità: Coefficiente di Correlazione di Pearson ($r$).

**Capitolo 9: Regressione Multipla e Analisi Matrice**
*   9.1 Estensione a più variabili indipendenti.
*   9.2 Formulazione Matriziale della Regressione Lineare.
*   9.3 Coefficienti Standardizzati e Interpretazione dei Coefficienti.
*   9.4 Analisi dei Residui: Eteroschedasticità, Autocorrelazione, Outlier.

**Capitolo 10: Analisi della Varianza (ANOVA)**
*   10.1 Concetti di Varianza Totale, Varianza tra i Gruppi e Varianza entro i Gruppi.
*   10.2 Decomposizione della Varianza (Sum of Squares Decomposition).
*   10.3 Test F di Fisher e Analisi della Varianza a un fattore.
*   10.4 Introduzione all'ANOVA a due fattori e Interazioni.

---

## PARTE V: Processi Stocastici e Teoria dell'Informazione
**Capitolo 11: Processi Aleatori e Sistemi Stocastici**
*   11.1 Definizione di Processo Aleatorio.
*   11.2 **Stazionarietà:**
    *   11.2.1 Stazionarietà di Ordine M.
    *   11.2.2 Stazionarietà a Breve Lungo (SSL).
*   11.3 **Catene di Markov:** Regola della catena, Matrici di Transizione, Probabilità di Transizione e proprietà di memoria.

**Capitolo 12: Teoria dell'Informazione**
*   12.1 **Entropia di Shannon:** Definizione matematica e interpretazione come misura di incertezza.
*   12.2 **Canali di Comunicazione:** Modellazione del Canale Binario Simmetrico (BSC) e probabilità di errore $\epsilon$.
*   12.3 **Concetti di Compressione e Ridondanza:** Relazione tra entropia, capacità di canale e trasmissione dati.

---

## PARTE VI: Appendice delle Dimostrazioni Matematiche (Full Proofs)
*(Sviluppo analitico completo di ogni passaggio logico trattato a lezione)*
*   A1. Teorema di Bayes.
*   A2. Varianza della Somma di Variabili Casuali.
*   A3. Teorema del Limite Centrale (via MGF).
*   A4. Distribuzione $t$ di Student.
*   A5. Distribuzione di Poisson come limite della Binomiale.
*   A6. Unbiasedness degli stimatori OLS.
*   A7. Proprietà di "Assenza di Memoria" della Distribuzione Esponenziale.
*   A8. Lemma di Neyman-Pearson (Ottimizzazione della Potenza).
*   A9. Limite di Cramér-Rao (Informazione di Fisher).
