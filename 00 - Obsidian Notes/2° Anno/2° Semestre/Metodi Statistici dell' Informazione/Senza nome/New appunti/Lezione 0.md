# SBOBINA - Metodi Statistici per l'Informazione | Lezione 1

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Metodi Statistici per l'Informazione
- **Docente**: Marco Lops
- **Orari e Aule**: 
    - **Martedì**: 14:00 - 16:00
    - **Giovedì**: 08:45 - 10:45
    - *Nota*: L'aula rimane costante per tutto il corso.
- **Organizzazione Didattica**:
    - **CFU e Ore**: 6 CFU (corrispondenti a 48 ore di lezione totali).
    - **Modalità di erogazione**: Lezioni frontali. La ripartizione è di circa i 2/3 teorici e 1/3 applicativi (sebbene la teoria e l'applicazione si intreccino costantemente).
    - **Recuperi**: Eventuali recuperi a distanza (specialmente nella prima settimana di maggio, per impegni di ricerca del docente in Spagna).
- **Ricevimento e Supporto**:
    - **Canali**: Disponibilità via Teams per chiarificazioni e appuntamenti.
    - **Preferenze**: Il docente preferisce incontri di gruppo piuttosto che individuali.
    - **Supporto immediato**: Sono previste spiegazioni "vive" a ridosso della fine delle lezioni (c'è un buffer di 30 minuti tra le sessioni).
- **Avvisi, Calendario e Assenze**:
    - **Iscrizioni**: Le iscrizioni sono attualmente aperte e gestite automaticamente tramite il sito web.
    - **Consigli pratici del docente**: 
        - "Non voglio sentire memoria, ma logica": Il docente insiste sulla comprensione dei passaggi logici piuttosto che sulla memorizzazione meccanica delle formule.
        - Il docente sottolinea che la comprensione della teoria della probabilità permette di trasformare quasi ogni problema in un semplice esercizio.
- **Accesso ai Materiali**:
    - **Piattaforma**: Microsoft Teams (richiede accettazione tramite codice).
    - **Materiali**: Slide disponibili nei file condivisi; PDF delle lavagne elettroniche caricati a fine ogni lezione in una sezione dedicata denominata "Lavagna".

---

## 🎯 SOMMARIO RAPIDO
- **Relazione tra discipline**: Integrazione tra Telecomunicazioni, Informatica e Statistica attraverso il concetto di incertezza.
- **Fondamenti della Probabilità**: Definizione di spazio campionario ($\Omega$), eventi e operazioni di insieme in contesti discreti.
- **Approccio Frequentistico**: Interpretazione della probabilità come limite della frequenza di successo.
- **Analisi Combinatoria**: Strumenti di conteggio (prodotti cartesiani, permutazioni, combinazioni) come base per il calcolo delle probabilità su spazi finiti.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine                  | Simbolo              | Definizione e Contesto                                                                                        |                      |                                                                    |
| ------------------------ | -------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------ |
| Spazio Campionario       | $\Omega$             | L'insieme di tutti i possibili risultati di un esperimento. Può essere finito, numerabile o continuo.         |                      |                                                                    |
| Evento                   | $A \subseteq \Omega$ | Un sottoinsieme dello spazio campionario definito da una proposizione.                                        |                      |                                                                    |
| Evento Elementare        | -                    | Uno dei singoli risultati possibili contenuti in $\Omega$ (valido per spazi finiti/discreti).                 |                      |                                                                    |
| Cardinalità              | $A$ o $\text{card}(A)$ | Il numero di elementi contenuti in un insieme finito o numerabile. |
| Eventi Incompatibili     | -                    | Eventi la cui intersezione è l'insieme vuoto ($A \cap B = \emptyset$).                                        |                      |                                                                    |
| Implicazione             | $A \implies B$       | Se il verificarsi di $A$ implica necessariamente il verificarsi di $B$ (ovvero $A \subseteq B$).              |                      |                                                                    |
| Frequenza di Successo    | $\frac{n_A}{n}$      | Il rapporto tra il numero di volte in cui si verifica l'evento $A$ ($n_A$) e il numero totale di prove ($n$). |                      |                                                                    |
| Approccio Frequentistico | -                    | Interpretazione della probabilità come limite della frequenza di successo quando $n \to \infty$.              |                      |                                                                    |
| Combinazione             | $\binom{n}{k}$       | Il numero di sottosiemi di $k$ elementi estraibili da un insieme di $n$ elementi, dove l'ordine non conta.    |                      |                                                                    |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Il Ruolo della Statistica nelle Scienze dell'Informazione
- **Spiegazione Teorica**: Il docente giustifica la presenza del corso spiegando che **Informazione** è un concetto misterioso ma centrale sia nelle Telecomunicazioni che nell'Informatica. 
    - Le **Telecomunicazioni** si occupano del trasferimento dell'informazione nello spazio (vettori elettromagnetici).
    - L'**Informatica** si occupa del trasferimento dell'informazione nel tempo (memorizzazione, compressione dati, correzione degli errori).
    - **Concetto Chiave**: L'informazione è intrinsecamente legata all'**incertezza**. Il processo di trasferimento di informazione consiste nel trasformare un'incertezza *a priori* in una certezza *posteriore*.
    - **Statistica e Probabilità**: La statistica è la base costruita sulla probabilità. Molti termini moderni (Machine Learning, Deep Learning, AI) convergono verso il trattamento probabilistico dell'informazione.
- **Condizioni Tacite e Prerequisiti**: Si assume la conoscenza di base della logica matematica; il docente specifica che per gli spazi discreti serve logica, mentre per i continui servirà l'analisi.

### 2. Spazio Campionario ed Eventi (Spazi Discreti)
- **Spiegazione Teorica**: 
    - **Esperimento**: Operazione che conduce a uno tra tanti risultati possibili.
    - **Spazio Campionario ($\Omega$)**: L'insieme di tutti i possibili risultati. 
    - **Esempi di $\Omega$**:
        - *Discreto/Finito*: Lancio di una moneta (Testa, Croce).
        - *Continuo*: Misura della tensione ai capi di una resistenza (influenzata dal rumore termico, non produce mai lo stesso valore reale), o il tempo (la sua cardinalità dipende dalla precisione dello strumento).
    - **Evento**: Sottoinsieme di $\Omega$ definito da una proposizione. 
    - **Ambiguità del Linguaggio**: Una proposizione può non essere univoca (es. "ho un numero dispari di euro" può descrivere gli eventi {1, 3, 5} o {1, 3, 5, 7...}), ma l'evento è univocamente determinato dagli elementi di $\Omega$ che lo compongono.
- **Operazioni su Insiemi**:
    - **Unione ($A \cup B$)**: Elementi appartenenti ad $A$, a $B$, o a entrambi.
    - **Complemento ($A^c$ o $\bar{A}$)**: Elementi di $\Omega$ che non appartengono ad $A$.
    - **Intersezione ($A \cap B$)**: Solo gli elementi comuni a entrambi.
    - **Sottrazione ($A \setminus B$)**: Elementi di $A$ che non appartengono a $B$. Identità: $A \setminus B = A \cap B^c$.
    - **Proprietà**: $\text{card}(\Omega)$ è l'evento certo; $\emptyset$ è l'evento impossibile. $A \cup A^c = \Omega$ e $A \cap A^c = \emptyset$.

### 3. Approccio Frequentistico e "Dato Onesto"
- **Spiegazione Teorica**: Un dato è considerato "onesto" se non vi è un evento elementare favorito. 
- **Condizioni Necessarie**: Se $n_i$ è il numero di volte in cui esce la faccia $i$ su $n$ lanci, il dato è onesto se:
  $$\frac{n_i}{n} \approx \frac{\text{card}(A_i)}{|\Omega|}$$
- **Limite Frequentistico**: Nell'ipotesi di prove indipendenti, per eventi equivalenti, il rapporto tende al valore teorico:
  $$\lim_{n \to \infty} \frac{n_A}{n} = \frac{|A|}{|\Omega|}$$
- **Criticità**: Il docente avverte che questa è una condizione *necessaria* ma non *sufficiente* (es. un dado truccato potrebbe comunque dare una distribuzione equilibrata su eventi composti come "pari" o "dispari").

### 4. Analisi Combinatoria (Strumenti di Conteggio)
- **Spiegazione Teorica**: Per calcolare le probabilità in spazi finiti, occorre saper contare i casi favorevoli e i casi possibili.
- **Prodotto Cartesiano**: Per insiemi $A, B, C$ con cardinalità $\text{card}(A_i)$, il numero di $k$-uple ordinate è il prodotto delle cardinalità:
  $$|A_1 \times A_2 \times \dots \times A_k| = \prod_{i=1}^k \text{card}(A_i)$$
- **$k$-uple Ordinate**:
    1. **Con ripetizioni**: $n^k$ (es. stringhe binarie di lunghezza $n$: $2^n$).
    2. **Senza ripetizioni**: $\frac{n!}{(n-k)!}$ (ogni estrazione riduce le possibilità del set disponibile).
- **Permutazioni**: $k$-uple ordinate di elementi distinti estraibili da un insieme di $k$ elementi.
  $$\text{Permutazioni} = k!$$
- **Combinazioni (k-uple non ordinate)**: Se l'ordine non conta, il numero di $k$-uple ordinate deve essere diviso per il numero di modi in cui si possono ordinare gli stessi $k$ elementi ($k!$).
  $$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$
- **Insieme delle Parti ($\mathcal{P}(A)$)**: Se un insieme $A$ ha $m$ elementi, il numero totale di sottosinsiemi possibili è $2^m$.
- **Binomio di Newton**: La cardinalità dell'insieme delle parti è data dalla somma dei coefficienti binomiali:
  $$\sum_{k=0}^m \binom{m}{k} = 2^m$$

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Lancio di una moneta (Spazio Campionario)
- **Testo**: Identificare lo spazio campionario e gli eventi del lancio di una moneta.
- **Risoluzione Passo-Passo**:
  1. Lo spazio campionario $\Omega$ è composto da due elementi: {Testa, Croce}.
  2. L'evento "esce una testa" è il sottoinsieme {Testa}.
  3. L'evento "esce testa o croce" è l'unione dei due, ovvero $\Omega$ (evento certo).
- **Concetti Applicati**: Definizione di $\Omega$, eventi, unione.

### Esercizio 2: Lancio di due monete
- **Testo**: Determinare lo spazio campionario e l'evento "numero di croci dispari".
- **Risoluzione Passo-Passo**:
  1. Lo spazio campionario $\Omega$ ha 4 elementi: {(T,T), (T,C), (C,T), (C,C)}.
  2. L'evento "numero di croci dispari" corrisponde ai casi con una sola croce: {(T,C), (C,T)}.
- **Concetti Applicati**: Cardinalità di $\Omega$, identificazione sottosinsiemi.

### Esercizio 3: Lancio di un dado (Eventi complessi)
- **Testo**: Determinare la cardinalità dell'evento "risultato dispari e minore o uguale a 4".
- **Risoluzione Passo-Passo**:
  1. Spazio campionario $\Omega = \{1, 2, 3, 4, 5, 6\}$, quindi $|\Omega| = 6$.
  2. Identificazione elementi dispari: $\{1, 3, 5\}$.
  3. Vincolo "minore o uguale a 4": l'insieme risultante è $\{1, 3\}$.
  4. Cardinalità dell'evento: 2.
- **Concetti Applicati**: Operazioni di intersezione, cardinalità.

### Esercizio 4: Calcolo delle combinazioni (Insieme delle parti)
- **Testo**: Calcolare il numero di sottosinsiemi di un insieme con 4 elementi.
- **Risoluzione Passo-Passo**:
  1. Identificare la cardinalità $m = 4$.
  2. Applicare la formula $2^m$.
  3. Risultato: $2^4 = 16$.
  4. Verifica logica tramite sommatoria dei coefficienti binomiali: $\binom{4}{0} + \binom{4}{1} + \binom{4}{2} + \binom{4}{3} + \binom{4}{4} = 1 + 4 + 6 + 4 + 1 = 16$.
- **Concetti Applicati**: Insieme delle parti, Binomio di Newton.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
  - **Proposizione vs Evento**: Una proposizione (linguaggio naturale) può essere ambigua o non univoca; l'evento deve essere rigorosamente definito come un sottoinsieme univoco di $\Omega$.
  - **Ordine nelle Combinazioni**: È fondamentale distinguere quando l'ordine degli elementi conta (permutazioni/prodotti cartesiani) e quando non conta (combinazioni/sottosinsiemi).
- **Chiarimenti Metodologici**:
  - Il docente sottolinea che **il discreto riempie la testa di idee, il continuo riempie la lavagna di formule**. La comprensione logica degli spazi discreti è il prerequisito fondamentale per affrontare correttamente le formule dei spazi continui.
- **Punti Critici per l'Esame**:
  - Il docente insiste sulla capacità di **formulare correttamente la proposizione** che definisce l'evento. Molti errori derivano da una formulazione ambigua che porta a un calcolo errato della cardinalità.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Prova scritta seguita da un colloquio rapido.
- **Propedeuticità e Prerequisiti**:
  - **Analisi**: Richiesta per la gestione degli spazi continui.
  - **Logica**: Fondamentale per la comprensione degli spazi discreti e delle strutture di insieme.
- **Consigli di Studio Espliciti**:
  - "Nessuna memoria, solo logica": Riflettere sui passaggi logici di ogni derivazione invece di memorizzare il risultato finale.
  - Studiare i meccanismi di conteggio combinatorio come base per ogni futuro calcolo probabilistico.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Ernesto Conte**, *Fenomeni Aleatori*. Nota: Testo molto didattico e ben strutturato, consigliato per lo studio della teoria della probabilità.
- **Sheldon Ross**, *Introduction to Probability and Statistics for Engineers and Scientists*. Nota: Testo orientato all'approccio applicativo per ingegneri e scienziati.
- **Kaila (1969-1971)**: Citato per il risultato storico che mette in relazione la teoria della stima inferenziale con la teoria dell'informazione.
