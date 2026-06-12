# SBOBINA - Teoria dell'Informazione e Probabilità | Lezione del 26 Marzo

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Non specificato nella trascrizione - Probabilità / Teoria dell'Informazione]
- **Docente**: [Non specificato]
- **Orari e Aule**: [Informazione non menzionata nella lezione]
- **Organizzazione Didattica**:
    - **CFU e Ore**: [Informazione non menzionata nella lezione]
    - **Modalità di erogazione**: Lezione frontale con partecipazione attiva (domande via microfono/chat).
- **Ricevimento e Supporto**:
    - [Informazione non menzionata nella lezione]
- **Avvisi, Calendario e Assenze**:
    - **Prossima lezione**: Martedì prossimo (prevista trattazione approfondita su alcunezza e catene di Markov).
    - **Note**: Il docente ha menzionato la necessità di rifare gli esercizi assegnati prima della prossima sessione.
- **Accessi ai Materiali**:
    - **File di riferimento**: File del 26 marzo (contenente gli esercizi svolti).

---

## 🎯 SOMMARIO RAPIDO
- **Canale Binario Simmetrico (SBC)**: Modellazione stocastica dei canali di comunicazione e analisi della probabilità di errore $\epsilon$.
- **Teoria dell'Informazione**: Definizione di informazione basata sulla rarità, calcolo dell'entropia $H(X)$ e concetto di compressione.
- **Relazioni tra PMF**: Marginalizzazione come media statistica e proprietà della probabilità condizionale.
- **Catene di Markov**: Regola della catena, indipendenza condizionale e memoria del sistema (esempio del Re degli scacchi).

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Canale | $C$ | Meccanismo di associazione stocastica tra un ingresso ($x$) e un'uscita ($y$). |
| Probabilità di Errore | $\epsilon$ | Frazione di bit che viene trasferita incorrettamente nella destinazione. |
| Canale Simmetrico | - | Canale in cui la probabilità di errore per lo zero è uguale a quella per l'uno ($P(1|0) = P(0|1)$). |
| Probabilità Condizionale | $P(y|x)$ | Probabilità che l'uscita sia $y$ dato che l'ingresso sia $x$. |
| Probabilità Posteriore | $P(x|y)$ | Probabilità che l'ingresso sia $x$ dato che è stata osservata l'uscita $y$ (Legge di Bayes). |
| Informazione | $I(A)$ | Quantità di informazione derivante dalla verificarsi di un evento $A$; inversamente proporzionale alla sua probabilità. |
| Entropia | $H(X)$ | Media della quantità di informazione ottenuta da una variabile aleatoria $X$. |
| PMF Congiunta | $P(x, y)$ | Probabilità simultanea che la variabile $x$ assuma un valore e la variabile $y$ un altro. |
| Marginalizzazione | - | Operazione per ottenere la PMF di una variabile partendo dalla congiunta (somma su tutti i valori dell'altra variabile). |
| Catena di Markov | - | Processo stocastico in cui la variabile successiva dipende solo da quella immediatamente precedente (indipendenza condizionale). |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### Il Canale Binario Simmetrico (SBC)
- **Spiegazione Teorica**:
    Un canale è definito come un meccanismo di **associazione stocastica** tra un ingresso $x$ e un'uscita $y$. In un canale ideale, l'ingresso viene trasferito senza alterazioni (0 rimane 0, 1 rimane 1). Tuttavia, i canali reali presentano non idealità che generano errori.
    Il canale è definito **simmetrico** quando la probabilità di errore è identica per entrambi i simboli trasmessi.
- **Condizioni Tacite e Prerequisiti**:
    Assume che l'evento "errore" sia rappresentato dalla differenza tra ingresso e uscita ($y \neq x$).
- **Formule e Modelli Matematici**:
    Nel canale simmetrico, la probabilità che il bit venga invertito è $\epsilon$:
    $$P(y=1 | x=0) = \epsilon$$
    $$P(y=0 | x=1) = \epsilon$$
    Di conseguenza, la probabilità di trasferimento corretto è $1 - \epsilon$:
    $$P(y=0 | x=0) = 1 - \epsilon$$
    $$P(y=1 | x=1) = 1 - \epsilon$$
    
    La **Probabilità di Errore** totale è data dall'applicazione della *Legge della Probabilità Totale*:
    $$P(\text{errore}) = P(x=0) \cdot P(y=1|x=0) + P(x=1) \cdot P(y=0|x=1)$$
    $$P(\text{errore}) = P(x=0) \cdot \epsilon + P(x=1) \cdot \epsilon = \epsilon \cdot (P(x=0) + P(x=1)) = \epsilon$$
    In un SBC, la probabilità di errore è esattamente $\epsilon$. Più piccolo è $\epsilon$, più il canale è informativo.

    **Analisi della Fiducia (Legge di Bayes)**:
    Per determinare la probabilità che l'ingresso sia effettivamente 0 data l'osservazione dell'uscita 0:
    $$P(x=0|y=0) = \frac{P(y=0|x=0)P(x=0)}{P(y=0)}$$
    Utilizzando la legge della probabilità totale per il denominatore (dove $P(x=1) = p$ e $P(x=0) = 1-p$):
    $$P(y=0) = (1-\epsilon)(1-p) + \epsilon p$$
    Quindi:
    $$P(x=0|y=0) = \frac{(1-\epsilon)(1-p)}{(1-\epsilon)(1-p) + \epsilon p}$$

- **Esempi Specifici Citati**:
    - *Il caso peggiore ($\epsilon = 0.5$)*: Se $\epsilon = 0.5$, la probabilità che $x=0$ dato $y=0$ diventa uguale a $1-p$ (la probabilità a priori). In questo caso, l'osservazione dell'uscita non fornisce alcuna informazione sull'ingresso; il canale è del tutto inaffidabile e "mangia" l'informazione.

---

### Teoria dell'Informazione
- **Spiegazione Teorica**:
    L'informatica e l'ingegneria dell'informazione si basano sulla misura della quantità di informazione trasferita per ottimizzare le risorse. L'informazione è definita secondo criteri di "senso comune":
    1. Deve essere **non negativa**.
    2. Deve essere **maggiore quanto più raro è l'evento**. (Es. dire che il sole sorgerà è informazione nulla; dire che non sorgerà è informazione teoricamente infinita).
    3. Deve essere **additiva** per eventi indipendenti.
    
    La funzione matematica che soddisfa queste proprietà è il **logaritmo**.
- **Formule e Modelli Matematici**:
    L'informazione di un evento $A$ è:
    $$I(A) = \log_2\left(\frac{1}{P(A)}\right)$$
    - Se $P(A) = 1$, $I(A) = 0$.
    - Se $P(A) \to 0$, $I(A) \to \infty$.
    
    **Entropia $H(X)$**:
    La quantità di informazione media di una variabile aleatoria $X$ è definita come l'entropia:
    $$H(X) = \sum_{i} P(x_i) \log_2\left(\frac{1}{P(x_i)}\right)$$
    Per una variabile bistabile (binit), $H(X)$ vale al massimo 1 bit, e questo avviene se e solo se $p = 0.5$.
    
- **Esempi Specifici Citati**:
    - *Variabile Quaternaria*: Una variabile che assume 4 valori con probabilità uniforme ($1/4$ ciascuno) ha un'entropia di:
      $$H(X) = 4 \cdot \left(\frac{1}{4} \log_2(4)\right) = 2 \text{ bit}$$
    - *Compressione*: Se i valori di una variabile non sono equiprobabili, l'entropia sarà $< 2$ bit, indicando che è possibile comprimere l'informazione usando meno di due variabili bistabili.

---

### Relazioni sulle PMF e Regola della Catena
- **Marginalizzazione come Media**:
    La PMF marginale di $x$ può essere vista come la media della PMF condizionale rispetto a $y$:
    $$P(x) = \sum_{y} P(x|y)P(y)$$
    Questa formula indica che è possibile calcolare la probabilità di $x$ condizionando su una variabile ausiliaria $y$ e calcolandone la media statistica.
- **Indipendenza e Catene di Markov**:
    - **Indipendenza**: $P(x|y) = P(x)$. L'osservazione di $y$ non influenza la probabilità di $x$.
    - **Indipendenza Condizionale**: Una terna di variabili $(x_1, x_2, x_3)$ può essere dipendente globalmente ma condizionalmente indipendente se $x_1$ e $x_3$ non dipendono l'uno dall'altro dato $x_2$.
    - **Regola della Catena**:
      $$P(x, y, z) = P(z) \cdot P(y|z) \cdot P(x|y, z)$$
      Ogni permutazione degli argomenti è possibile.

- **Esempi Specifici Citati**:
    - *Il Re degli Scacchi*: Consideriamo le posizioni del Re in tre mosse successive ($x_1, x_2, x_3$). $x_1$ e $x_3$ sono dipendenti (la posizione finale è limitata da quella iniziale). Tuttavia, se conosciamo la posizione intermedia $x_2$, $x_1$ e $x_3$ diventano condizionalmente indipendenti, poiché la mossa successiva dipende solo dalla posizione attuale. Questa è la definizione di **Catena di Markov**.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: L'Urna e le Palline
- **Testo**: Un'urna contiene 6 palline: una marcata "1", due marcate "2", tre marcate "3". Si effettuano due estrazioni senza reinserimento.
  1. Determinare la PMF congiunta $P(x_1, x_2)$.
  2. Determinare la probabilità di ottenere {2,3} in qualsiasi ordine.
  3. Determinare la PMF condizionale $P(x_2 | x_1)$.

- **Risoluzione Passo-Passo**:
  1. **PMF Marginale $x_1$**:
     - $P(x_1=1) = 1/6$
     - $P(x_1=2) = 2/6 = 1/3$
     - $P(x_1=3) = 3/6 = 1/2$
  2. **PMF Congiunta $P(x_1, x_2)$**: Calcolata come $P(x_1) \cdot P(x_2|x_1)$.
     - $P(1,1) = P(x_1=1) \cdot P(x_2=1|x_1=1) = 1/6 \cdot 0 = 0$ (non c'è reinserimento).
     - $P(1,2) = 1/6 \cdot 2/5 = 2/30 = 1/15$.
     - $P(1,3) = 1/6 \cdot 3/5 = 3/30 = 1/10$.
     - $P(2,1) = 1/3 \cdot 1/5 = 1/15$.
     - $P(2,2) = 1/3 \cdot 1/5 = 1/15$ (rimane una pallina "2" su 5).
     - $P(2,3) = 1/3 \cdot 3/5 = 3/15 = 1/5$.
     - $P(3,1) = 1/2 \cdot 1/5 = 1/10$.
     - $P(3,2) = 1/2 \cdot 2/5 = 2/10 = 1/5$.
     - $P(3,3) = 1/2 \cdot 2/5 = 2/10 = 1/5$ (rimangono due palline "3" su 5).
  3. **PMF Condizionale $P(x_2|x_1)$**: Costruzione della tabella riga per riga:
     - Dato $x_1=1$: $P(x_2|1) = \{0, 2/5, 3/5\}$
     - Dato $x_1=2$: $P(x_2|2) = \{1/5, 1/5, 3/5\}$
     - Dato $x_1=3$: $P(x_2|3) = \{1/5, 2/5, 2/5\}$

- **Concetti Applicati**: Probabilità condizionale, non reinserimento, marginalizzazione.

### Esercizio 2: I Dadi (Onesto vs Truccato)
- **Testo**: Un dado onesto ($D_F$) e un dado truccato ($D_L$) dove $P(6)=1/2$ e $P(i \neq 6)=1/10$. 
  Regola: Se esce pari $\rightarrow$ mantieni dado; se esce dispari $\rightarrow$ cambia dado.
  Calcolare: A) $P(6,6)$, B) $P(6,5)$, C) $P(6,5) = P(5,6)$?

- **Risoluzione Passo-Passo**:
  1. **Caratterizzazione Dadi**:
     - $D_F$: $P(i) = 1/6$ per ogni $i \in \{1..6\}$.
     - $D_L$: $P(6) = 1/2$; $P(i \neq 6) = 1/10$.
  2. **Calcolo $P(6,6)$**:
     - Caso $D_F$: $P(x_1=6|D_F) \cdot P(x_2=6|x_1=6, D_F) = 1/6 \cdot 1/6 = 1/36$.
     - Caso $D_L$: $P(x_1=6|D_L) \cdot P(x_2=6|x_1=6, D_L) = 1/2 \cdot 1/2 = 1/4$.
     - Totale: $\frac{1}{2}(\frac{1}{36}) + \frac{1}{2}(\frac{1}{4}) = \frac{1}{72} + \frac{1}{8} = \frac{10}{72} = \frac{5}{36}$.
  3. **Calcolo $P(6,5)$**:
     - Caso $D_F$: $P(x_1=6|D_F) \cdot P(x_2=5|x_1=6, D_F) = 1/6 \cdot 1/6 = 1/36$ (6 è pari, mantieni $D_F$).
     - Caso $D_L$: $P(x_1=6|D_L) \cdot P(x_2=5|x_1=6, D_L) = 1/2 \cdot 1/10 = 1/20$ (6 è pari, mantieni $D_L$).
     - Totale: $\frac{1}{2}(\frac{1}{36}) + \frac{1}{2}(\frac{1}{20}) = \frac{5}{360} + \frac{9}{360} = \frac{14}{360} = \frac{7}{180}$.
  4. **Calcolo $P(5,6)$**:
     - Caso $D_F$: $P(x_1=5|D_F) \cdot P(x_2=6|x_1=5, \text{switch to } D_L) = 1/6 \cdot 1/2 = 1/12$.
     - Caso $D_L$: $P(x_1=5|D_L) \cdot P(x_2=6|x_1=5, \text{switch to } D_F) = 1/10 \cdot 1/6 = 1/60$.
     - Totale: $\frac{1}{2}(\frac{1}{12}) + \frac{1}{2}(\frac{1}{60}) = \frac{1}{24} + \frac{1}{120} = \frac{5+1}{120} = \frac{6}{120} = \frac{1}{20}$.
- **Risultato**: $P(6,5) \neq P(5,6)$ poiché $7/180 \neq 1/20$.
- **Semplificazioni/Trucchi**: Il docente sottolinea l'importanza di identificare correttamente quale dado viene usato al secondo lancio in base alla parità del primo esito.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    - Confusione nella costruzione delle tabelle di probabilità condizionate (errore comune del docente durante la lezione, poi corretto sottolineando che la somma deve essere unitaria lungo le righe per le probabilità condizionate).
    - Difficoltà nel distinguere tra probabilità congiunta e condizionale negli esercizi complessi (es. il cambio di dado).
- **Chiarimenti Metodologici**:
    - La legge della probabilità totale è uno strumento fondamentale per scomporre problemi complessi in casi mutuamente esclusivi.
    - La relazione tra entropia e informazione è basata sul concetto di "incertezza rimossa".
- **Punti Critici per l'Esame**:
    - Importanza di leggere attentamente il testo (es. "senza reinserimento", "cambia dado").
    - Interpretazione del caso limite $\epsilon = 0.5$ come punto di indipendenza totale.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: [Informazione non menzionata nella lezione]
- **Propedeuticità e Prerequisiti**:
    *   Buone basi di probabilità (Legge di Bayes, Probabilità Totale).
    *   Competenze matematiche di base (Logaritmi, Sommatorie).
- **Consigli di Studio Espliciti**:
    *   Rifare gli esercizi assegnati autonomamente.
    *   Focalizzarsi sulla comprensione dei passaggi logici piuttosto che sulla memoria dei risultati.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- File del 26 marzo (esercizi pratici).
- [Informazione non menzionata nella lezione]
