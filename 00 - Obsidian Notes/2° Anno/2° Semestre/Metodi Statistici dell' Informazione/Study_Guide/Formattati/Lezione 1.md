# SBOBINA - [PROBABILITÀ] | LEZIONE DI COMBINATORIA E DEFINIZIONI FUNDAMENTALI

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Non specificato - Probabilità/Statistica]
- **Docente**: [Non specificato]
- **Orari e Aule**: Informazione non menzionata nella lezione.
- **Organizzazione Didattica**:
    - **CFU e Ore**: Informazione non menzionata nella lezione.
- **Ricevimento e Supporto**: 
    - **Canali**: Comunicazione esclusiva tramite la piattaforma **Schimms**.
- **Avvisi, Calendario e Assenze**:
    - **Materiali**: Il docente caricherà una cartella denominata **"esercizi"** su Schimms.
- **Consigli pratici del docente**: 
    - Il docente sottolinea che la comprensione della materia deve basarsi sul **ragionamento logico** e sulla corretta **formulazione delle proposizioni** che definiscono gli eventi, piuttosto che sulla memorizzazione meccanica delle formule.

---

## 🎯 SOMMARIO RAPIDO
- Distinzione tra combinazioni ordinate e non ordinate e calcolo dei coefficienti binomiali e multinomiali.
- Definizione formale di probabilità come limite della frequenza di successo e sua interpretazione come misura.
- Analisi della probabilità in contesti non equiprobabili (es. dadi truccati, misure pesate).
- Introduzione alla probabilità condizionata attraverso la riduzione dello spazio campionario.
- Definizione di indipendenza tra eventi.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Spazio Campionario | $\Omega$ | L'insieme di tutti i possibili risultati di un esperimento. Può essere discreto (finito o numerabile). |
| Evento | $A$ | Un qualsiasi sottoinsieme dello spazio campionario $A \subseteq \Omega$. |
| Frequenza di successo | $F_n(A)$ | Il rapporto tra il numero di volte in cui si verifica l'evento $A$ su $n$ prove e il numero totale di prove: $F_n(A) = \frac{N_A}{n}$. |
| Probabilità | $P(A)$ | Il limite della frequenza di successo quando il numero di prove tende all'infinito: $P(A) = \lim_{n \to \infty} F_n(A)$. |
| Coefficiente Binomiale | $\binom{n}{k}$ | Il numero di modi per scegliere $k$ elementi da un insieme di $n$ elementi, dove l'ordine non conta. |
| Coefficiente Multinomiale | $\frac{n!}{n_1! n_2! \dots n_m!}$ | Il numero di modi per disporre $n$ elementi in un alfabeto $m$-ario con frequenze $n_1, n_2, \dots, n_m$. |
| Evento Condizionato | $P(B|A)$ | La probabilità che si verifichi l'evento $B$ dato che si è verificato l'evento $A$. |
| Eventi Indipendenti | $P(A \cap B) = P(A)P(B)$ | Due eventi sono indipendenti se la verifica di uno non influenza la probabilità dell'altro. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Combinatoria: Ordine e Coefficienti
Il docente illustra la differenza fondamentale tra combinazioni **ordinate** e **non ordinate**.
- **Combinazioni non ordinate**: Se l'ordine degli elementi non è rilevante, il numero di combinazioni si ottiene dividendo il numero di permutazioni per il fattoriale del numero di elementi scelti ($k!$).
- **Coefficiente Binomiale**: Rappresenta il numero di modi per scegliere $k$ elementi da un insieme di $n$.
- **Coefficiente Multinomiale**: Generalizzazione per sequenze di lunghezza $n$ composte da un alfabeto $m$-ario, dove ci sono $n_1$ simboli del tipo 1, $n_2$ del tipo 2, ..., $n_m$ del tipo $m$.
  $$ \frac{n!}{n_1! n_2! \dots n_m!} $$

### 2. Definizione di Probabilità come Limite di Frequenza
Il docente presenta una definizione "brutalista" (per analogia con l'architettura) ma rigorosa del concetto di probabilità:
- **Definizione**: La probabilità dell'evento $A$ è il limite della frequenza di successo $F_n(A)$ per $n$ che tende all'infinito.
- **Criticità**: 
    1. Le prove devono essere **indipendenti** e il processo deve essere **ergodico**.
    2. La convergenza della successione deve essere specificata (es. convergenza forte/quadratica).
- **Intuizione**: Se gli eventi sono **equiprobabili**, la probabilità è semplicemente il rapporto tra le cardinalità: $P(A) = \frac{|A|}{|\Omega|}$. Se non sono equiprobabili, questo metodo fallisce.

### 3. Probabilità come Misura
Il docente introduce il concetto di **misura di probabilità**: la probabilità non è solo un conteggio di elementi, ma un modo di "pesare" la realtà.
- **Esempio del Dado Truccato**: Se un dado è truccato affinché il "1" esca con probabilità $5/6$ e gli altri numeri con $1/30$, la probabilità di ottenere un numero pari non sarà $1/2$, ma dipenderà dal peso specifico di ogni esito.
- **Analogia della Pianta e dell'Ape**: Immaginiamo un'aula (spazio campionario) divisa in quadrati di $1m^2$. Se ogni quadrato è uguale, la probabilità di trovare un'ape in un punto è $1/50$. Se però mettiamo una pianta fiorita su un metro specifico, quel metro "pesa" molto di più in termini probabilistici (es. $0.99$), pur mantenendo la stessa dimensione fisica.
- **Conclusione**: La probabilità è una **misura normalizzata** a 1.

### 4. Probabilità Condizionata e Indipendenza
Il docente propone un approccio intuitivo basato sulla **riduzione dello spazio campionario**.
- **Concetto**: Se diamo un'informazione (condizione $A$), eliminiamo dal database tutti i risultati che non soddisfano $A$. Lo spazio campionario si riduce.
- **Formula**: $P(B|A) = \frac{P(A \cap B)}{P(A)}$.
- **Indipendenza**: Due eventi $A$ e $B$ sono indipendenti se la condizione $A$ non fornisce alcuna informazione su $B$. In questo caso, $P(B|A) = P(B)$, il che implica matematicamente che $P(A \cap B) = P(A)P(B)$.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Combinazioni con le carte (Quaterne e Cinquine)
- **Testo**: Calcolo di quaterne e cinquine non ordinate da un mazzo di carte.
- **Risoluzione Passo-Passo**:
  1. Per una quaterna di carte (es. fiori, picche, quadri, carte), se l'ordine non conta, il numero di combinazioni è dato dal prodotto delle cardinalità diviso per $4!$.
  2. **Esempio Cinquine con esattamente due assi**:
     - Posizioni totali: 5.
     - Scelta dei 2 assi da 4 disponibili: $\binom{4}{2} = \frac{4 \cdot 3}{2!} = 6$.
     - Scelta delle altre 3 carte dalle 48 rimanenti (non assi): $\binom{48}{3} = \frac{48 \cdot 47 \cdot 46}{3 \cdot 2 \cdot 1} = 17.296$.
     - **Risultato**: $6 \cdot 17.296 = 103.776$ (il docente cita il numero $69.184$ come esempio di calcolo intermedio).
  3. **Semplificazioni/Trucchi**: Per escludere punteggi più alti (es. full o doppie coppie), il docente suggerisce di scegliere le carte una alla volta: la terza carta tra 48 opzioni, la quarta tra 44 (diversa dalla terza), la quinta tra 40, dividendo per $3!$ per l'ordine non rilevante.

### Esercizio 2: Sequenze binarie con $K_1$ degli "1"
- **Testo**: Quante sono le sequenze di $n$ bit che hanno esattamente $K_1$ degli "1"?
- **Risoluzione Passo-Passo**:
  1. Se tutti i bit fossero distinti, avremmo $n!$ permutazioni.
  2. Poiché gli "1" sono identici, le loro $K_1!$ permutazioni tra loro non cambiano la sequenza.
  3. Poiché gli "0" sono identici, le loro $(n - K_1)!$ permutazioni non cambiano la sequenza.
  4. **Risultato**: Il numero di sequenze è $\frac{n!}{K_1! (n - K_1)!} = \binom{n}{K_1}$.
- **Generalizzazione**: Per un alfabeto $m$-ario con $n_1, n_2, \dots, n_m$ simboli, il numero di sequenze è il coefficiente multinomiale $\frac{n!}{n_1! n_2! \dots n_m!}$.

### Esercizio 3: Probabilità nel Poker (Mazzo da 32 carte)
- **Testo**: Calcolo di diverse probabilità su 5 carte estratte da un mazzo da 32.
- **Risoluzione Passo-Passo**:
  - **Spazio Campionario**: $\binom{32}{5} = \frac{32!}{5! 27!} = 201.376$ combinazioni totali.
  - **Almeno tre assi**: Somma della probabilità di avere esattamente 3 assi e esattamente 4 assi.
    - *Tre assi*: $\binom{4}{3} \cdot \binom{28}{2} = 4 \cdot 378 = 1.512$.
    - *Quattro assi*: $\binom{4}{4} \cdot \binom{28}{1} = 1 \cdot 28 = 28$.
    - **Risultato**: $(1.512 + 28) / 201.376 \approx 0,0076$.
  - **Tris di 7 (escludendo full e poker)**:
    - Scegliere tre 7: $\binom{4}{3} = 4$.
    - Scegliere la quarta carta (non 7): 28 opzioni.
    - Scegliere la quinta carta (diversa dalla quarta e non 7): 24 opzioni.
    - Dividere per $2!$ per l'ordine non rilevante delle ultime due carte.
    - **Risultato**: $(4 \cdot 28 \cdot 24 / 2) / 201.376 \approx 0,0067$.
  - **Colore di Picche**: $\binom{8}{5} / 201.376 = 56 / 201.376 \approx 0,001$.

### Esercizio 4: Il Paradosso del Compleanno (30 persone)
- **Testo**: Qual è la probabilità che in una classe di 30 persone almeno due abbiano lo stesso compleanno?
- **Risoluzione Passo-Passo**:
  1. Calcolare l'evento complementare: "Nessuno ha lo stesso compleanno".
  2. La prima persona ha 365 opzioni, la seconda 364, ..., la trentaesima $(365 - 29)$.
  3. Probabilità complementare: $\prod_{i=0}^{29} \frac{365-i}{365}$.
  4. **Risultato**: La probabilità richiesta è $1 - \text{Prodotto}$. Il docente specifica che il valore è "altissimo".

### Esercizio 5: Lancio di dado (Almeno un 6 in 5 lanci)
- **Testo**: Qual è la probabilità che esca almeno un 6 lanciando un dado onesto 5 volte?
- **Risoluzione Passo-Passo**:
  1. Calcolare la probabilità dell'evento complementare: "Non esce mai il 6".
  2. Probabilità di non avere un 6 in un singolo lancio: $5/6$.
  3. Poiché i lanci sono indipendenti, la probabilità di non avere mai un 6 in 5 lanci è $(5/6)^5$.
  4. **Risultato**: $1 - (5/6)^5$.
- **Concetti Applicati**: Eventi complementari, indipendenza, potenze.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    *   **Cardinalità vs Probabilità**: Non si può usare il rapporto tra cardinalità se gli eventi non sono equiprobabili (es. dado truccato).
    *   **Confusione sulla Condizionalità**: Non confondere la probabilità a priori con quella a posteriori. La condizionalità "pulisce" il database eliminando gli esiti non conformi alla condizione.
- **Chiarimenti Metodologici**:
    *   L'approccio frequentista (limite della frequenza) è considerato dal docente come un modo intuitivo ma rigoroso di definire la probabilità.
    *   La probabilità è una **misura**: la somma delle probabilità di eventi disgiunti deve essere uguale alla probabilità della loro unione.
- **Punti Critici per l'Esame**:
    *   Il docente insiste sull'importanza della **formulazione logica**: "Non vi pretendo che ve le ricordi anche [le formule], ma che sappiate dove e perché usarle".
    *   Focus sulla distinzione tra eventi indipendenti (dove l'informazione non cambia la probabilità) e dipendenti.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Consigli di Studio Espliciti**:
    *   Ripercorrere i ragionamenti logici per la definizione della probabilità condizionata.
    *   Non focalizzarsi solo sulle formule, ma sulla logica sottostante.
    *   Familiarizzare con i termini "probabilità a priori" e "probabilità a posteriori".

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Popper, K.** (Citato dal docente come autore di un testo consigliato sulla teoria della probabilità e sulla transizione dagli assiomi di Kolmogorov a metodi più intuitivi).
- **Note sulla "Scuola Napoletana"**: Il docente accenna alla scuola probabilistica napoletana e alla distinzione tra approccio teorico astratto e approccio frequentista/intuitivo.