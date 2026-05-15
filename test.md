# **Fondamenti di Probabilità**
*Docente: Marco Lops (IINF-03/A, "Telecomunicazioni")*
*Contatti: [lops@unina.it](mailto:lops@unina.it) | [Sito web](https://docenti.unina.it/marco.lops)*

---

---

## **📌 Informazioni Generali**

### **Orario delle lezioni**

Orario delle lezioni


| **Giorno**   | **Ora**         | **Aula** |
|--------------|-----------------|----------|
| Martedì      | 14:00 - 16:00   | B-6      |
| Giovedì      | 08:45 - 10:45   | B-6      |

---

### **Modalità di interazione**
- **Orari ufficiali** per spiegazioni.
- **Al termine delle lezioni**.
- **Su appuntamento** via **Microsoft Teams** (codice Team: **`8b1fgjq`**).
- **Su appuntamento dal vivo**.

> ⚠️ **Importante**:
> - Iscriversi al **Team "Calcolo delle Probabilità e Statistica"** (codice: **`8b1fgjq`**).
> - Iscriversi al corso sul **sito web dei docenti**.

---

---

## **📚 Organizzazione del Corso**
- **CFU**: 6 (48 ore di lezione).
  - **32 ore** di lezioni **teoriche**.
  - **16 ore** di lezioni **applicative**.
- **Verifica finale**:
  - Prova **scritta** + **colloquio orale**.

---

---

## **📖 Materiale Didattico**
- **Slide** del docente (scaricabili dal Team **"Metodi Statistici per l'Informazione"**, codice: **`7p3013g`**).
- **Formati PDF delle lavagne** (quando disponibili, scaricabili dal Team **"Calcolo delle Probabilità e Statistica"**).
- **Libri di testo consigliati**:
  - **Teoria della Probabilità**:
    - Testi generici (non specificati).
  - **Statistica Inferenziale e Descrittiva**:
    - *Sheldon M. Ross*, **"Introduction to Probability and Statistics for Engineers and Scientists"**, Elsevier.

---

---

## **🎯 Programma del Corso**

### **1. Teoria della Probabilità**
- Analisi Combinatoria
- Probabilità su spazi finiti
- Variabili aleatorie discrete
- Variabili continue
- Variabili multiple
- **Processi Aleatori**

---

### **2. Informazione e sua Misura**
- Entropia
- Compressione dati
- Mutua informazione
- Divergenza

---
### **3. Statistica**
- Statistica inferenziale
- Teoria della decisione
- Inferenza Bayesiana e non Bayesiana
- Stima ricorsiva

---
### **4. Integrazione tra**
- Teoria dell’Informazione
- Statistica Inferenziale

---

---

# **📐 Elementi di Teoria della Probabilità**

---

## **🔹 Definizioni Fondamentali**

- **Esperimento**: Operazione o insieme di operazioni il cui esito produce uno tra molti risultati possibili.
- **Spazio dei campioni (Ω)**: Insieme di **tutti i risultati possibili** di un esperimento (può essere **continuo** o **discreto**).
  - **Discreto**: Finito o numerabile (es. lancio di un dado).
  - **Continuo**: Non numerabile (es. misurazione di un segnale).
- **Evento**: Sottoinsieme di Ω, definito matematicamente da un insieme di elementi e lessicalmente da una proposizione.
- **Evento elementare**: Uno dei possibili elementi di Ω (es. `ω ∈ Ω`).
  - **Nota**: Un evento è **univocamente determinato** dagli elementi che lo compongono, ma la proposizione che lo definisce **non è unica**.

---

---

## **🎲 Esempi di Spazi Campione**

### **1. Lancio di una moneta**
- **Singolo lancio**:
  - Ω = {Testa (T), Croce (C)} → |Ω| = 2.
  - Eventi:
    - A = {T} (Testa)
    - B = {C} (Croce)
    - A ∪ B = {T, C} (Testa o Croce).

- **Doppio lancio**:
  - Ω = {TT, TC, CT, CC} = {T, C}² → |Ω| = 4.
  - Eventi:
    - A = {TC, CT} (numero dispari di croci).
    - B = {TT} (nessuna croce).

---

### **2. Lancio di un dado**
- Ω = {1, 2, 3, 4, 5, 6} → |Ω| = 6.
- Eventi:
  - A = {1, 3, 5} (risultato dispari).
  - B = {2, 4, 6} (risultato pari).
  - C = {1, 3} (dispari e ≤ 4).
  - D = {6} (risultato = 6).

> ⚠️ **Nota Bene**: La proposizione che definisce un evento **non è univoca** (es. "dispari" o "1 o 3 o 5").

---
### **3. Numero di pacchetti in coda a un router**
- Ω = {0, 1, 2, 3, ...} = ℕ₀ → |Ω| = ∞.
- Eventi:
  - A = {0, 1, 2, 3, 4, 5} (meno di 6 pacchetti).
  - B = {1, 3, 5, ...} (numero dispari di pacchetti).
  - C = A ∩ B = {1, 3, 5} (dispari e < 6).
  - D = {pacchetti pari **o** ≤ 4} = {0, 1, 2, 3, 4, 6, 8, ...}.

> 🔹 **Osservazione**: Gli eventi possono essere **combinati** usando operazioni insiemistiche (unione, intersezione, complemento).

---

---

## **🔢 Richiami di Insiemistica**

Siano {Aᵢ}ₙ₌₁ᴹ sottoinsiemi di Ω. Definiamo:

- **Unione**: A₁ ∪ A₂ = {x ∈ Ω | x ∈ A₁ **o** x ∈ A₂}.
- **Complemento**: \(\overline{A_1}\) = Ω \ A₁ (tutti gli elementi di Ω **non** in A₁).
  - \(\overline{Ω} = ∅\), \(\overline{\overline{A_1}} = A_1\), \(A_1 ∪ \overline{A_1} = Ω\).
- **Intersezione**: A₁ ∩ A₂ = {x ∈ Ω | x ∈ A₁ **e** x ∈ A₂}.
- **Sottrazione**: A₁ \ A₂ = A₁ ∩ \(\overline{A_2}\) (elementi in A₁ **non** in A₂).

---

### **Leggi di De Morgan**
\[
\overline{A_1 ∪ A_2} = \overline{A_1} ∩ \overline{A_2} \quad \text{e} \quad \overline{A_1 ∩ A_2} = \overline{A_1} ∪ \overline{A_2}
\]

### **Proprietà Associativa**
\[
(A_1 ∪ A_2) ∪ A_3 = A_1 ∪ (A_2 ∪ A_3) \quad \text{e} \quad (A_1 ∩ A_2) ∩ A_3 = A_1 ∩ (A_2 ∩ A_3)
\]

### **Proprietà Distributiva**
\[
A_1 ∪ (∩_{i=2}^M A_i) = ∩_{i=2}^M (A_1 ∪ A_i) \quad \text{e} \quad A_1 ∩ (∪_{i=2}^M A_i) = ∪_{i=2}^M (A_1 ∩ A_i)
\]

---

---

## **📌 Nomenclatura Probabilistica**
- **Ω**: Evento **certo**.
- **∅**: Evento **impossibile**.
- **A e \(\overline{A}\)**: Eventi **complementari**.
- **A e B incompatibili**: A ∩ B = ∅ (mutuamente esclusivi).
- **A ⊆ B**: A **implica** B (se A si verifica, allora si verifica anche B).

---

### **Esempi**
1. **Lancio singolo di una moneta**:
   - T = {Testa}, C = {Croce} → **complementari** e **incompatibili**.
   - \(\overline{T} ∩ \overline{C} = \overline{Ω} = ∅\) (evento impossibile).

2. **Lancio doppio di una moneta**:
   - D = {Almeno una croce} = {CC, TC, CT} = \(\overline{\{TT\}}\) = Ω \ {TT}.
   - D è **incompatibile** con {TT}.

3. **Lancio di un dado (Esempio #2)**:
   - A = {dispari}, B = {pari} → **complementari** e **incompatibili**.
   - C = {1, 3} ⊆ A → C **implica** A.

---

---

## **🎯 Spazi Finiti con Eventi Elementari Equivalenti**
- **Ipotesi**: Ω è **finito** e tutti gli eventi elementari sono **equivalenti** (nessuno è "privilegiato").
- **Frequenza di occorrenza**:
  \[
  f_n(A) = \frac{n_A}{n} \xrightarrow{n \to ∞} \frac{|A|}{|\Omega|}
  \]
  Dove:
  - \(n_A\) = numero di volte in cui A si verifica in \(n\) esperimenti.
  - \(|A|\) = cardinalità di A.

> 🔹 **Conclusione**: Per calcolare la probabilità, è **fondamentale saper contare** le cardinalità degli insiemi.
> → **Calcolo Combinatorio**.

---

---

## **🔢 Prodotti Cartesiani**
Dati \(k\) insiemi finiti \(A_1, A_2, ..., A_k\) (non necessariamente distinti), il **prodotto cartesiano** è:
\[
A^{(k)} = A_1 × A_2 × ... × A_k = \{(a_1, a_2, ..., a_k) | a_i ∈ A_i \forall i\}
\]
- **Cardinalità**:
  \[
  |A^{(k)}| = \prod_{i=1}^k |A_i|
  \]
  > 🔹 **Relazione fondamentale** del calcolo combinatorio.

---

---

## **🔢 \(k\)-ple Ordinate**

### **1. Senza ripetizione**
- **Definizione**: Stringhe di lunghezza \(k\) con elementi **distinti** da un insieme \(A = \{a_1, ..., a_n\}\).
- **Cardinalità**:
  \[
  |A^{(k)}| = n(n-1)(n-2)...(n-k+1) = \prod_{i=0}^{k-1} (n - i)
  \]

### **2. Con ripetizione**
- **Definizione**: Stringhe di lunghezza \(k\) con elementi **ripetibili** da \(A = \{a_1, ..., a_n\}\).
- **Cardinalità**:
  \[
  |A^{(k)}| = n^k
  \]
  > **Esempio**: Numero di \(k\)-ple binarie = \(2^k\) (da \(\{0, 1\}\)).

---

### **3. Permutazioni**
- **Definizione**: \(n\)-ple ordinate di \(n\) elementi distinti.
- **Cardinalità**:
  \[
  n! = n(n-1)...1
  \]

---
### **4. Combinazioni \(C_{n,k}\)**
- **Definizione**: Numero di \(k\)-ple **non ordinate** (sottoinsiemi di cardinalità \(k\)).
- **Formula**:
  \[
  C_{n,k} = \binom{n}{k} = \frac{n!}{k!(n-k)!}
  \]
  > **Nota**: \(k!\) permutazioni di una \(k\)-pla ordinata **collassano** in un'unica combinazione.

---

---

## **🃏 Problema: Estrazione di Carte**
**Testo**:
Si considerino **52 carte francesi** (4 semi: Cuori (C), Fiori (F), Picche (P), Quadri (Q)).
Si estraggono \(k\) carte **senza reimmissione**. Calcolare:
a) Numero di **quaterne ordinate**.
b) Numero di **quaterne non ordinate**.
c) Numero di **quaterne (C, F, P, Q)**.
d) Numero di **cinquine non ordinate** con **esattamente due assi**.

---

### **🔹 Soluzione**
a) **Quaterne ordinate senza ripetizione** (\(k=4, n=52\)):
\[
52 × 51 × 50 × 49 = 6.497.400
\]

b) **Quaterne non ordinate**:
\[
\frac{52 × 51 × 50 × 49}{4!} = \frac{6.497.400}{24} = 270.725
\]

c) **Quaterne (C, F, P, Q)**:
- Ogni seme ha 13 carte → \(13^4 = 28.561\).

d) **Cinquine con esattamente due assi**:
- **Assi**: \(\binom{4}{2} = 6\) modi per scegliere 2 assi su 4.
- **Altre carte**: \(\binom{48}{3} = 17.296\) modi per scegliere 3 carte tra le rimanenti 48.
- **Totale**:
  \[
  \binom{4}{2} × \binom{48}{3} = 6 × 17.296 = 103.776
  \]
  > **Correzione**: Il risultato nel documento originale era **69.184**, ma il calcolo corretto è **103.776** (probabile errore di battitura).

---

---

## **🔢 Insieme delle Parti di un Insieme Finito**
- **Definizione**: Dato un insieme \(A\) con \(n\) elementi, l’**insieme delle parti** \(\mathcal{P}(A)\) è l’insieme di **tutti i sottoinsiemi di \(A\)**.
- **Cardinalità**:
  \[
  |\mathcal{P}(A)| = \sum_{k=0}^n \binom{n}{k} = 2^n
  \]

---

---

## **📊 Prove Ripetute e Conteggio dei Successi**
**Problema**:
Quante stringhe binarie di lunghezza \(n\) hanno **esattamente \(k\) "1"**?

**Soluzione**:
- **Permutazioni totali**: \(n!\).
- **Permutazioni inefficaci**:
  - \(k!\) per i "1" (già in posizioni fisse).
  - \((n-k)!\) per gli "0".
- **Risultato**:
  \[
  \frac{n!}{k!(n-k)!} = \binom{n}{k}
  \]

---

---

## **📈 Dalla Frequenza alla Probabilità**
- **Definizione di probabilità**:
  \[
  \mathbb{P}(A) = \lim_{n \to ∞} \frac{n_A}{n}
  \]
  Dove \(n_A\) = numero di volte in cui \(A\) si verifica in \(n\) esperimenti.

- **Spazio finito con eventi elementari equiprobabili**:
  \[
  \mathbb{P}(A) = \frac{|\Omega_A|}{|\Omega|}
  \]
  Dove \(\Omega_A\) = sottoinsieme di Ω che soddisfa \(A\).

---

---

## **🎲 Esempio: Punteggi del Poker**
**Testo**:
Un giocatore estrae **5 carte** da un mazzo di **32 carte** (dal 7 all’asso, 8 valori × 4 semi).
Calcolare le probabilità di:
a) **Coppia di assi e coppia qualsiasi**.
b) **Almeno tre assi**.
c) **Un tris qualsiasi** (ma non full o poker).
d) **Colore di picche o colore qualsiasi**.

---

### **🔹 Soluzione [a]**
- **Spazio campione**:
  \[
  |\Omega| = \binom{32}{5} = 201.376
  \]

- **Coppia di assi**:
  - **2 assi su 4**: \(\binom{4}{2} = 6\).
  - **3 carte qualsiasi tra le rimanenti 28**: \(\binom{28}{3} = 3.276\).
  - **Totale**: \(6 × 3.276 = 19.656\).
  - **Probabilità**:
    \[
    \mathbb{P}(C_2) = \frac{19.656}{201.376} ≈ 0.097
    \]
  - **Escludendo full/doppie coppie**:
    \[
    |C_2'| = \binom{4}{2} × \frac{28 × 24 × 20}{3!} = 6 × 2.240 = 13.440 \quad \Rightarrow \mathbb{P}(C_2') ≈ 0.067
    \]
  - **Coppia qualsiasi**: Moltiplicare per 8 (numero di valori possibili per la coppia).

---

### **🔹 Soluzione [b]**
- **3 assi**:
  \[
  \binom{4}{3} × \binom{28}{2} = 4 × 378 = 1.512
  \]
- **4 assi**:
  \[
  \binom{4}{4} × \binom{28}{1} = 1 × 28 = 28
  \]
- **Totale**: \(1.512 + 28 = 1.540\).
- **Probabilità**:
  \[
  \mathbb{P}(C_3) = \frac{1.540}{201.376} ≈ 0.0076
  \]

---
### **🔹 Soluzione [c]**
- **Tris di un valore specifico (es. 7)**:
  - **3 carte su 4**: \(\binom{4}{3} = 4\).
  - **2 carte diverse tra le rimanenti 28**: \(28 × 24 / 2 = 336\) (ordini non contano).
  - **Totale per un valore**: \(4 × 336 = 1.344\).
  - **Probabilità per un valore**:
    \[
    \mathbb{P}(C_3'(7)) = \frac{1.344}{201.376} ≈ 0.0067
    \]
- **Tris qualsiasi (8 valori possibili)**:
  \[
  8 × 1.344 = 10.752 \quad \Rightarrow \mathbb{P}(C_3') ≈ 0.053
  \]

---
### **🔹 Soluzione [d]**
- **Colore di picche**:
  - **5 carte su 8 di picche**: \(\binom{8}{5} = 56\).
  - **Probabilità**:
    \[
    \mathbb{P}(C_P) = \frac{56}{201.376} ≈ 0.00027
    \]
- **Colore qualsiasi (4 semi)**:
  \[
  \mathbb{P}(\text{colore}) = 4 × 0.00027 ≈ 0.0011
  \]
- **Escludendo scale reali**:
  - **Scale reali per seme**: 5 (es. A-7-8-9-10, 10-J-Q-K-A).
  - **Colore di picche senza scale**:
    \[
    \binom{8}{5} - 5 = 51 \quad \Rightarrow \mathbb{P}(C_P) ≈ 0.00025
    \]
  - **Colore qualsiasi senza scale**:
    \[
    \mathbb{P}(\text{colore}) ≈ 0.001
    \]

---

---

# **📉 Frequenza e Probabilità su Spazi Finiti**
- **Ipotesi**: Ω è **discreto** (finito o numerabile), ma gli eventi elementari **non sono equiprobabili**.
- **Definizione**:
  \[
  f_n(A) = \frac{n_A}{n}, \quad \mathbb{P}(A) = \lim_{n \to ∞} f_n(A)
  \]
- **Differenza chiave**: Non vale più \(n_A ≈ n|A|/|\Omega|\).

> 🔹 **Conclusione**: Due eventi con la stessa cardinalità possono avere **probabilità diverse**.

---

---

## **🎲 Esempio: Dado Truccato**
- **Spazio campione**: Ω = {1, 2, 3, 4, 5, 6}.
- **Probabilità**:
  - \(\mathbb{P}(\{1\}) = \frac{5}{6}\).
  - \(\mathbb{P}(\{i\}) = \frac{1}{30}\) per \(i = 2, 3, 4, 5, 6\).
- **Eventi**:
  - A = {2, 4, 6} (pari).
  - B = {1, 3, 5} (dispari).
- **Frequenze limite**:
  \[
  \mathbb{P}(A) = \frac{3}{30} = \frac{1}{10}, \quad \mathbb{P}(B) = \frac{5}{6} + \frac{2}{30} = \frac{9}{10}
  \]
  > **Confronta**: Con un dado onesto, \(\mathbb{P}(A) = \mathbb{P}(B) = 0.5\).

---

---

# **📌 Proprietà della Probabilità**

## **1. Eventi Complementari**
\[
\mathbb{P}(\overline{A}) = 1 - \mathbb{P}(A)
\]

## **2. Sub-additività (Unione)**
\[
\mathbb{P}(A ∪ B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A ∩ B)
\]

## **3. Sottrazione tra Insiemi**
\[
\mathbb{P}(A \setminus B) = \mathbb{P}(A) - \mathbb{P}(A ∩ B)
\]

## **4. Evento Certo e Impossibile**
\[
\mathbb{P}(Ω) = 1, \quad \mathbb{P}(∅) = 0
\]

---

---

## **🔄 Probabilità Condizionata**
- **Definizione**:
  \[
  \mathbb{P}(A|B) = \frac{\mathbb{P}(A ∩ B)}{\mathbb{P}(B)}
  \]
- **Legge della probabilità composta**:
  \[
  \mathbb{P}(A ∩ B) = \mathbb{P}(A|B)\mathbb{P}(B) = \mathbb{P}(B|A)\mathbb{P}(A)
  \]

---

## **📊 Legge della Probabilità Totale**
Sia \(\{E_i\}_{i=1}^M\) una **partizione** di Ω (cioè \(∪_{i=1}^M E_i = Ω\) e \(E_i ∩ E_j = ∅\) per \(i ≠ j\)).
Allora:
\[
\mathbb{P}(A) = \sum_{i=1}^M \mathbb{P}(A|E_i)\mathbb{P}(E_i)
\]

---

---

## **🔗 Eventi Indipendenti**
- **Definizione**: \(A\) e \(B\) sono **indipendenti** se:
  \[
  \mathbb{P}(A ∩ B) = \mathbb{P}(A)\mathbb{P}(B)
  \]
  Oppure:
  \[
  \mathbb{P}(A|B) = \mathbb{P}(A) \quad \text{e} \quad \mathbb{P}(B|A) = \mathbb{P}(B)
  \]
- **Esempio**: Lancio di un dado onesto due volte.
  \[
  \mathbb{P}(\{i, j\}) = \mathbb{P}(\{i\})\mathbb{P}(\{j\}) = \frac{1}{36}
  \]

---

---

# **📐 Approccio Assiomatico alla Probabilità**

## **1. Algebra di Eventi**
- **Definizione**: Una famiglia \(\mathcal{E}\) di sottoinsiemi di Ω è un’**algebra di eventi** se:
  1. **Chiusura rispetto all’unione**:
     \[
     A_1, A_2 ∈ \mathcal{E} ⇒ A_1 ∪ A_2 ∈ \mathcal{E}
     \]
  2. **Chiusura rispetto alla complementazione**:
     \[
     A_1 ∈ \mathcal{E} ⇒ \overline{A_1} ∈ \mathcal{E}
     \]

- **σ-algebra**: Se \(\mathcal{E}\) è chiusa anche rispetto all’unione **numerabile** di eventi.

---

## **2. Proprietà delle Algebre**
- **Intersezione**:
  \[
  A, B ∈ \mathcal{E} ⇒ A ∩ B = \overline{\overline{A} ∪ \overline{B}} ∈ \mathcal{E}
  \]
- **Sottrazione**:
  \[
  A, B ∈ \mathcal{E} ⇒ A \setminus B = A ∩ \overline{B} ∈ \mathcal{E}
  \]
- **Algebra minima**: Se \(A\) è un evento, la minima algebra che lo contiene è:
  \[
  \mathcal{E} = \{A, \overline{A}, Ω, ∅\}
  \]

---

## **3. Spazio di Probabilità**
- **Definizione**: Una **legge di probabilità** è una funzione:
  \[
  \mathbb{P}: \mathcal{E} → [0, 1]
  \]
  che soddisfa gli **assiomi di Kolmogorov**:
  1. **Non negatività**: \(\mathbb{P}(A) ≥ 0\) per ogni \(A ∈ \mathcal{E}\).
  2. **Normalizzazione**: \(\mathbb{P}(Ω) = 1\).
  3. **σ-additività**: Se \(\{B_n\}_{n∈ℕ}\) sono eventi **incompatibili**, allora:
     \[
     \mathbb{P}\left(∪_{n=1}^∞ B_n\right) = \sum_{n=1}^∞ \mathbb{P}(B_n)
     \]

- **Terna \((\Omega, \mathcal{E}, \mathbb{P})\)**: **Spazio di probabilità**.

---

---

## **📌 Proprietà delle Leggi di Probabilità**
1. **Eventi complementari**:
   \[
   \mathbb{P}(\overline{A}) = 1 - \mathbb{P}(A)
   \]
2. **Sottrazione tra insiemi**:
   \[
   \mathbb{P}(A \setminus B) = \mathbb{P}(A) - \mathbb{P}(A ∩ B)
   \]
3. **Unione di eventi non incompatibili**:
   \[
   \mathbb{P}(A ∪ B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A ∩ B)
   \]

---

---

## **🧩 Esercizio: Indipendenza dei Complementari**
**Testo**: Dimostrare che se \(A\) e \(B\) sono indipendenti, allora lo sono anche \(\overline{A}\) e \(\overline{B}\).

**Soluzione**:
1. **Ipotesi**: \(\mathbb{P}(A ∩ B) = \mathbb{P}(A)\mathbb{P}(B)\).
2. **Obiettivo**: Dimostrare \(\mathbb{P}(\overline{A} ∩ \overline{B}) = \mathbb{P}(\overline{A})\mathbb{P}(\overline{B})\).
3. **Passaggi**:
   - Per De Morgan: \(\overline{A ∩ B} = \overline{A} ∪ \overline{B}\) → \(\overline{A ∪ B} = \overline{A} ∩ \overline{B}\).
   - \(\mathbb{P}(\overline{A} ∩ \overline{B}) = 1 - \mathbb{P}(A ∪ B)\).
   - \(\mathbb{P}(A ∪ B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A ∩ B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A)\mathbb{P}(B)\).
   - Sostituendo:
     \[
     \mathbb{P}(\overline{A} ∩ \overline{B}) = 1 - \mathbb{P}(A) - \mathbb{P}(B) + \mathbb{P}(A)\mathbb{P}(B) = (1 - \mathbb{P}(A))(1 - \mathbb{P}(B)) = \mathbb{P}(\overline{A})\mathbb{P}(\overline{B})
     \]

---

---

# **🎯 Variabili Aleatorie**

## **🔹 Definizione**
- **Variabile aleatoria \(X\)**: Funzione che associa ogni evento elementare \(ω ∈ Ω\) a un numero reale:
  \[
  X: Ω → \mathcal{X} ⊆ ℝ
  \]
  - \(\mathcal{X}\) = **alfabeto** di \(X\) (insieme dei valori possibili).
  - **Esempio**:
    - Lancio di una moneta: \(X(ω) = 0\) (Croce), \(X(ω) = 1\) (Testa).
    - Doppio lancio: \(X(ω) ∈ \{0, 1, 2\}\) (numero di teste).

---
## **📊 Probability Mass Function (PMF)**
- **Definizione**: La sequenza \(p_X(x) = \mathbb{P}(X = x)\) per \(x ∈ \mathcal{X}\) è la **PMF** di \(X\).
- **Proprietà**:
  \[
  p_X(x) ≥ 0, \quad \sum_{x ∈ \mathcal{X}} p_X(x) = 1
  \]
- **Esempio**: \(\mathcal{X} = \{1, 2, 3, 4\}\), \(p_X = (0.5, 0.25, 0.125, 0.125)\).
  - Verifica: \(0.5 + 0.25 + 0.125 + 0.125 = 1\) → **valida**.

---
## **⚠️ Avvertenza sulle Notazioni**
- **Notazione corretta**:
  \[
  \mathbb{P}(X = x) = \mathbb{P}(\{ω ∈ Ω | X(ω) = x\})
  \]
- **Notazione semplificata**: \(\mathbb{P}(X = x)\) o \(\mathbb{P}(\{X = x\})\).

---
## **📈 Media Campionaria**
- **Definizione**: Dati \(n\) esperimenti con risultati \([X(ω_1), ..., X(ω_n)]\), la **media campionaria** è:
  \[
  \overline{X_n} = \frac{1}{n} \sum_{i=1}^n X(ω_i)
  \]

---
## **📊 Media Statistica (Valor Atteso)**
- **Definizione**:
  \[
  \mathbb{E}[X] = \sum_{x ∈ \mathcal{X}} x p_X(x)
  \]
- **Interpretazione**:
  - Media delle osservazioni al tendere di \(n → ∞\).
  - **Esempio**: \(X ~ \mathcal{U}(\{0, 1, 2\})\) → \(\mathbb{E}[X] = (0 + 1 + 2)/3 = 1\).

---
# **🎲 Esempio: Conteggio Bernoulliano**
- **Scenario**: Lancio di una moneta **\(N\) volte** con probabilità di testa \(p\) e croce \(q = 1 - p\).
- **Variabile aleatoria \(X_N\)**: Numero di teste in \(N\) lanci.
  - \(X_N: Ω → \{0, 1, ..., N\}\).
  - **Spazio campione**: Ω = \(\{T, C\}^N\) (tutte le sequenze di \(N\) lanci).

---
## **📌 PMF Binomiale**
- **Probabilità di una sequenza con \(k\) teste**:
  \[
  \mathbb{P}(ω) = p^k q^{N-k} \quad \text{(indipendenza dei lanci)}
  \]
- **Numero di sequenze con \(k\) teste**: \(\binom{N}{k}\).
- **PMF di \(X_N\)**:
  \[
  p_{X_N}(k) = \binom{N}{k} p^k q^{N-k} \quad \text{(Distribuzione Binomiale: \(X_N ~ \mathcal{B}(N, p)\))}
  \]
- **Verifica**:
  \[
  \sum_{k=0}^N p_{X_N}(k) = (p + q)^N = 1
  \]
- **Valor atteso**:
  \[
  \mathbb{E}[X_N] = Np
  \]

---
# **🎲 Altre Distribuzioni Discrete**

## **1. Distribuzione Uniforme**
- **Definizione**: \(X ~ \mathcal{U}(\mathcal{X})\) se:
  \[
  p_X(x) = \frac{1}{|\mathcal{X}|} \quad \forall x ∈ \mathcal{X}
  \]
- **Valor atteso**:
  \[
  \mathbb{E}[X] = \frac{1}{|\mathcal{X}|} \sum_{x ∈ \mathcal{X}} x
  \]
- **Esempio**: \(\mathcal{X} = \{0, 1, ..., M-1\}\) → \(\mathbb{E}[X] = \frac{M-1}{2}\).

---
## **2. Distribuzione di Poisson**
- **Definizione**: \(X ~ \mathcal{P}(λ)\) se:
  - \(\mathcal{X} = \mathbb{N}_0 = \{0, 1, 2, ...\}\).
  - PMF:
    \[
    p_X(k) = \frac{λ^k}{k!} e^{-λ}, \quad k ∈ \mathbb{N}_0
    \]
- **Verifica**:
  \[
  \sum_{k=0}^∞ p_X(k) = e^{-λ} \sum_{k=0}^∞ \frac{λ^k}{k!} = e^{-λ} e^{λ} = 1
  \]
- **Valor atteso**:
  \[
  \mathbb{E}[X] = λ
  \]

---
# **📊 PMF e Medie Condizionali**

## **🔹 PMF Condizionale**
- **Definizione**: Dati un evento \(A ⊆ Ω\) con \(\mathbb{P}(A) > 0\), la **PMF condizionale** di \(X\) dato \(A\) è:
  \[
  p_{X|A}(x) = \mathbb{P}(X = x | A) = \frac{\mathbb{P}(\{X = x\} ∩ A)}{\mathbb{P}(A)}
  \]
- **Esempio**: \(X ~ \mathcal{B}(16, 1/3)\), calcolare \(p_{X|X>4}(k)\).
  - **PMF condizionale**:
    \[
    p_{X|X>4}(k) = \frac{p_X(k)}{\mathbb{P}(X > 4)} \quad \text{per } k = 5, ..., 16
    \]
    \[
    p_{X|X>4}(k) = 0 \quad \text{per } k < 5
    \]

---
## **📈 Media Condizionale**
- **Definizione**:
  \[
  \mathbb{E}[X | A] = \sum_{x ∈ \mathcal{X}} x p_{X|A}(x)
  \]
- **Legge della probabilità totale per le medie**:
  \[
  \mathbb{E}[X] = \sum_{m=1}^M \mathbb{E}[X | E_m] \mathbb{P}(E_m)
  \]
  Dove \(\{E_m\}_{m=1}^M\) è una partizione di Ω.

---
# **🔄 Funzioni di Variabili Aleatorie**

## **🔹 Definizione**
- Sia \(X\) una variabile aleatoria con alfabeto \(\mathcal{X}\) e PMF \(p_X(x)\).
- Sia \(g: \mathcal{X} → \mathcal{Y}\) una funzione.
- **Nuova variabile aleatoria**:
  \[
  Y = g(X)
  \]
- **Obiettivo**: Trovare:
  1. PMF di \(Y\): \(p_Y(y)\).
  2. Valor atteso di \(Y\): \(\mathbb{E}[Y]\).

---
## **📌 Caso 1: Funzione Biunivoca**
- Se \(g\) è **biunivoca** (iniettiva e suriettiva), allora:
  \[
  p_Y(y) = p_X(g^{-1}(y))
  \]
  \[
  \mathbb{E}[Y] = \sum_{y ∈ \mathcal{Y}} y p_Y(y) = \sum_{x ∈ \mathcal{X}} g(x) p_X(x)
  \]

---
## **📌 Caso 2: Funzione Non Iniettiva**
- Se \(g\) **non è iniettiva** (più \(x\) mappano allo stesso \(y\)):
  \[
  p_Y(y) = \sum_{x: g(x)=y} p_X(x)
  \]
  \[
  \mathbb{E}[Y] = \sum_{y ∈ \mathcal{Y}} y p_Y(y) = \sum_{x ∈ \mathcal{X}} g(x) p_X(x)
  \]

> 🔹 **Teorema fondamentale per il calcolo della media**:
> \[
> \mathbb{E}[g(X)] = \sum_{x ∈ \mathcal{X}} g(x) p_X(x)
> \]

---
## **🎲 Esempio: Funzioni di Variabili Aleatorie**
- **Variabile**: \(X ~ \mathcal{U}(\{-2, -1, 0, 2\})\) (PMF: \(p_X(x) = 1/4\)).
- **Funzioni**:
  1. \(Y_1 = X^2\) → \(\mathcal{Y}_1 = \{0, 1, 4\}\).
     - \(p_{Y_1}(0) = \mathbb{P}(X=0) = 1/4\).
     - \(p_{Y_1}(1) = \mathbb{P}(X=-1) + \mathbb{P}(X=1) = 1/2\) (ma \(1 ∉ \mathcal{X}\) → **errore**).
       > **Correzione**: \(\mathcal{X} = \{-2, -1, 0, 2\}\) → \(Y_1 = X^2\) assume valori \(\{0, 1, 4\}\).
       - \(p_{Y_1}(0) = \mathbb{P}(X=0) = 1/4\).
       - \(p_{Y_1}(1) = \mathbb{P}(X=-1) = 1/4\) (ma \(-1 ∉ \mathcal{X}\) → **errore nel documento originale**).
       - **Corretto**: \(\mathcal{X} = \{-2, -1, 0, 1, 2\}\) (mancava 1).
       - **Assunzione**: Se \(\mathcal{X} = \{-2, -1, 0, 2\}\), allora:
         - \(Y_1 = X^2\) → \(\mathcal{Y}_1 = \{0, 1, 4\}\).
         - \(p_{Y_1}(0) = \mathbb{P}(X=0) = 1/4\).
         - \(p_{Y_1}(1) = \mathbb{P}(X=-1) = 1/4\) (ma \(-1 ∉ \mathcal{X}\) → **incoerenza**).
         - **Conclusione**: Probabile errore nel documento. Se \(\mathcal{X} = \{-2, -1, 0, 1, 2\}\), allora:
           - \(p_{Y_1}(0) = 1/5\).
           - \(p_{Y_1}(1) = \mathbb{P}(X=-1) + \mathbb{P}(X=1) = 2/5\).
           - \(p_{Y_1}(4) = \mathbb{P}(X=-2) + \mathbb{P}(X=2) = 2/5\).

  2. \(Y_2 = 3 \sin\left(\frac{2π}{5} X\right)\) → \(\mathcal{Y}_2 = \{-3 \sin(2π/5), -3 \sin(4π/5), 0, 3 \sin(4π/5)\}\).
     - \(|\mathcal{Y}_2| = 4 = |\mathcal{X}|\) → \(Y_2 ~ \mathcal{U}(\mathcal{Y}_2)\).

---
# **📊 Valore Quadratico Medio e Varianza**

## **🔹 Definizioni**
- **Valore quadratico medio (Mean Square)**:
  \[
  X_{\text{rms}}^2 = \mathbb{E}[X^2] = \sum_{x ∈ \mathcal{X}} x^2 p_X(x)
  \]
- **Valore efficace (RMS)**:
  \[
  X_{\text{rms}} = \sqrt{\mathbb{E}[X^2]}
  \]
- **Varianza**:
  \[
  \sigma_X^2 = \mathbb{E}[(X - \mu_X)^2] = \mathbb{E}[X^2] - \mu_X^2
  \]
  Dove \(\mu_X = \mathbb{E}[X]\).
- **Deviazione standard**:
  \[
  \sigma_X = \sqrt{\sigma_X^2}
  \]

---
## **🎲 Esempio: Distribuzione Binomiale**
- **Varianza**:
  \[
  \sigma_X^2 = Np(1 - p)
  \]
- **Deviazione standard**:
  \[
  \sigma_X = \sqrt{Np(1 - p)}
  \]
- **Valore quadratico medio**:
  \[
  X_{\text{rms}}^2 = Np(1 - p) + N^2 p^2
  \]

---
Se vuoi che aggiunga altre sezioni o che formatti ulteriormente il documento (ad esempio, aggiungendo indici o migliorando la leggibilità), fammi sapere!
---

# **📉 Varianza e Deviazione Standard per Altre Distribuzioni**

## **1. Distribuzione Uniforme**
- **Varianza**:
$$
\sigma_X^2 = \mathbb{E}[X^2] - \mu_X^2 = \frac{1}{M} \sum_{x \in \mathcal{X}} x^2 - \left( \frac{1}{M} \sum_{x \in \mathcal{X}} x \right)^2
$$
- **Esempio**: $\mathcal{X} = \{0, 1, ..., M-1\}$
$$
\mathbb{E}[X^2] = \frac{(M-1)(2M-1)}{6}, \quad \mu_X = \frac{M-1}{2}
$$
$$
\sigma_X^2 = \frac{(M^2 - 1)}{12}
$$

---

## **2. Distribuzione di Poisson**
- **Varianza**:
$$
\sigma_X^2 = \lambda
$$
- **Deviazione standard**:
$$
\sigma_X = \sqrt{\lambda}
$$

---

---

# **🔄 Variabili Aleatorie Doppie**

## **🔹 Definizione**
- **Variabile aleatoria doppia $(X, Y)$**: Funzione che associa ogni evento elementare $ω ∈ Ω$ a una coppia di numeri reali:
$$
(X, Y): Ω → \mathcal{X} × \mathcal{Y} ⊆ \mathbb{R}^2
$$
- **PMF congiunta**:
$$
p_{X,Y}(x, y) = \mathbb{P}(X = x, Y = y)
$$
- **Proprietà**:
$$
p_{X,Y}(x, y) ≥ 0, \quad \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p_{X,Y}(x, y) = 1
$$

---
## **📊 PMF Marginali**
- **PMF marginale di $X$**:
$$
p_X(x) = \sum_{y \in \mathcal{Y}} p_{X,Y}(x, y)
$$
- **PMF marginale di $Y$**:
$$
p_Y(y) = \sum_{x \in \mathcal{X}} p_{X,Y}(x, y)
$$

---
## **🔗 Indipendenza di Variabili Aleatorie**
- **Definizione**: $X$ e $Y$ sono **indipendenti** se:
$$
p_{X,Y}(x, y) = p_X(x) p_Y(y) \quad \forall x \in \mathcal{X}, y \in \mathcal{Y}
$$
- **Esempio**: Lancio di due dadi onesti.
  - $X$ = risultato del primo dado, $Y$ = risultato del secondo dado.
  - $p_{X,Y}(x, y) = $\frac{1}{36}$ = $\frac{1}{6}$ \cdot $\frac{1}{6}$ = p_X(x) p_Y(y)$.

---
## **📈 Valor Atteso Congiunto**
- **Valor atteso di $g(X, Y)$**:
$$
\mathbb{E}[g(X, Y)] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} g(x, y) p_{X,Y}(x, y)
$$
- **Esempio**: $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$.

---
## **📌 Covarianza e Correlazione**
- **Covarianza**:
$$
\text{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = \mathbb{E}[XY] - \mu_X \mu_Y
$$
- **Coefficiente di correlazione**:
$$
\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$
  - $-1 ≤ \rho_{X,Y} ≤ 1$.
  - $\rho_{X,Y} = 0$ → $X$ e $Y$ **non correlate** (ma non necessariamente indipendenti).

---
## **🔹 Proprietà della Covarianza**
1. $\text{Cov}(X, Y) = \text{Cov}(Y, X)$.
2. $\text{Cov}(X, X) = \sigma_X^2$.
3. $\text{Cov}(aX + b, cY + d) = ac \cdot \text{Cov}(X, Y)$.
4. Se $X$ e $Y$ sono indipendenti, allora $\text{Cov}(X, Y) = 0$.

---

---

# **🎯 Processi Aleatori**

## **🔹 Definizione**
- **Processo aleatorio**: Famiglia di variabili aleatorie $\{X_t\}_{t \in T}$ definite su uno stesso spazio di probabilità $(\Omega, \mathcal{E}, \mathbb{P})$.
  - $T$ = **insieme degli indici** (es. tempo discreto o continuo).
  - $X_t(ω)$ = **realizzazione del processo** al tempo $t$ per l’evento $ω$.

---
## **📌 Esempi di Processi Aleatori**
$$
1. **Passeggiata aleatoria (Random Walk)**:
$$
   - $X_0 = 0$.
   - $X_{n+1} = $X_n$ + Y_n$, dove $Y_n$ sono variabili aleatorie indipendenti e identicamente distribuite (i.i.d.).
   - **Esempio**: $Y_n = +1$ con probabilità $p$, $Y_n = -1$ con probabilità $1-p$.
$$
2. **Processo di Bernoulli**:
$$
   - Sequenza di prove indipendenti con esito "successo" (probabilità $p$) o "fallimento" (probabilità $1-p$).
   - $X_n$ = numero di successi nelle prime $n$ prove → $X_n ~ \mathcal{B}(n, p)$.
$$
3. **Processo di Poisson**:
$$
   - $X_t$ = numero di eventi che si verificano in un intervallo di tempo $[0, t]$.
   - **Proprietà**:
     - $X_0 = 0$.
     - Incrementi indipendenti: $X_{t+s} - X_t$ è indipendente da $X_u$ per $u ≤ t$.
     - $X_{t+s} - X_t ~ \mathcal{P}(\lambda (t+s))$.

---
## **📊 Media e Varianza di un Processo Aleatorio**
- **Media**:
$$
\mu_X(t) = \mathbb{E}[X_t]
$$
- **Funzione di autocorrelazione**:
$$
R_X(t_1, t_2) = \mathbb{E}[X_{t_1} X_{t_2}]
$$
- **Funzione di autocovarianza**:
$$
C_X(t_1, t_2) = \text{Cov}(X_{t_1}, X_{t_2}) = R_X(t_1, t_2) - \mu_X(t_1) \mu_X(t_2)
$$

---
## **🔹 Processi Stazionari**
- **Definizione**: Un processo aleatorio è **stazionario** se le sue statistiche non cambiano nel tempo.
  - **Stazionarietà in senso stretto**: La distribuzione congiunta di $(X_{t_1}, ..., X_{t_n})$ è la stessa di $(X_{$t_1$ + \tau}, ..., X_{$t_n$ + \tau})$ per ogni $\tau$.
  - **Stazionarietà in senso lato (debole)**:
    1. $\mu_X(t) = \mu_X$ (costante).
    2. $R_X($t_1$, $t_2$) = R_X($t_2$ - $t_1$)$ (dipende solo dalla differenza temporale).

---
## **📌 Esempio: Processo di Poisson Omogeneo**
- **Media**:
$$
\mathbb{E}[X_t] = \lambda t
$$
- **Varianza**:
$$
\text{Var}(X_t) = \lambda t
$$
- **Funzione di autocorrelazione**:
$$
R_X(t_1, t_2) = \lambda \min(t_1, t_2) + \lambda^2 t_1 t_2
$$

---

---

# **📚 Spazi Campione Continui**

## **🔹 Definizione**
- **Spazio campione continuo**: Ω è un sottoinsieme di $\mathbb{R}^n$ (es. intervalli, piani, ecc.).
- **Probabilità**: Non si può definire una PMF, ma si usa una **funzione di densità di probabilità (PDF)** $f_X(x)$.
  - **Proprietà**:
$$
f_X(x) ≥ 0, \quad \int_{-\infty}^{\infty} f_X(x) \, dx = 1
$$
  - **Probabilità di un evento $A$**:
$$
\mathbb{P}(A) = \int_A f_X(x) \, dx
$$

---
## **📊 Funzione di Distribuzione Cumulativa (CDF)**
- **Definizione**:
$$
F_X(x) = \mathbb{P}(X ≤ x) = \int_{-\infty}^x f_X(t) \, dt
$$
- **Proprietà**:
  1. $F_X(x)$ è **non decrescente**.
  2. $\lim_{x \to -\infty} F_X(x) = 0$, $\lim_{x \to \infty} F_X(x) = 1$.
  3. $f_X(x) = $\frac{d}{dx}$ F_X(x)$ (dove derivabile).

---
## **🎲 Esempi di Distribuzioni Continue**

### **1. Distribuzione Uniforme Continua**
- **PDF**:
$$
f_X(x) = \begin{cases}
  \frac{1}{b - a} & \text{se } a ≤ x ≤ b \\
  0 & \text{altrimenti}
  \end{cases}
$$
- **Media**:
$$
\mathbb{E}[X] = \frac{a + b}{2}
$$
- **Varianza**:
$$
\sigma_X^2 = \frac{(b - a)^2}{12}
$$

---
### **2. Distribuzione Normale (Gaussiana)**
- **PDF**:
$$
f_X(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}}
$$
  - $\mu$ = media, $\sigma^2$ = varianza.
- **Notazione**: $X ~ \mathcal{N}(\mu, \sigma^2)$.
- **Proprietà**:
  - $\mathbb{E}[X] = \mu$.
  - $\text{Var}(X) = \sigma^2$.
  - **Standardizzazione**: $Z = $\frac{X - \mu}{\sigma}$ ~ \mathcal{N}(0, 1)$.

---
### **3. Distribuzione Esponenziale**
- **PDF**:
$$
f_X(x) = \begin{cases}
  \lambda e^{-\lambda x} & \text{se } x ≥ 0 \\
  0 & \text{altrimenti}
  \end{cases}
$$
- **Media**:
$$
\mathbb{E}[X] = \frac{1}{\lambda}
$$
- **Varianza**:
$$
\sigma_X^2 = \frac{1}{\lambda^2}
$$
- **Proprietà senza memoria**:
$$
\mathbb{P}(X > s + t   X > s) = \mathbb{P}(X > t)
$$

---
## **📌 Variabili Aleatorie Continue Doppie**
- **PDF congiunta**: $f_{X,Y}(x, y)$.
  - **Proprietà**:
$$
f_{X,Y}(x, y) ≥ 0, \quad \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx \, dy = 1
$$
- **PDF marginali**:
$$
f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy
$$
$$
f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx
$$
- **Indipendenza**:
$$
f_{X,Y}(x, y) = f_X(x) f_Y(y)
$$
- **Valor atteso**:
$$
\mathbb{E}[g(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) f_{X,Y}(x, y) \, dx \, dy
$$

---
## **📊 Covarianza e Correlazione per Variabili Continue**
- **Covarianza**:
$$
\text{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = \mathbb{E}[XY] - \mu_X \mu_Y
$$
- **Coefficiente di correlazione**:
$$
\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$

---
---

# **📌 Teoremi Limite**

## **🔹 Legge dei Grandi Numeri (LLN)**
- **Versione debole**:
$$
\overline{X_n} = \frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{P} \mu \quad \text{per } n \to \infty
$$
  Dove $X_i$ sono variabili aleatorie **i.i.d.** con media $\mu$.
  - $\xrightarrow{P}$ = convergenza in probabilità.

- **Interpretazione**: La media campionaria **converge** al valor atteso al crescere di $n$.

---
## **🔹 Teorema Centrale del Limite (CLT)**
- **Enunciato**:
  Siano $X_1, $X_2$, ..., X_n$ variabili aleatorie **i.i.d.** con media $\mu$ e varianza $\sigma^2 < \infty$.
  Allora:
$$
Z_n = \frac{\overline{X_n} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1) \quad \text{per } n \to \infty
$$
  Dove $\xrightarrow{d}$ = convergenza in distribuzione.

- **Interpretazione**:
  La somma (o media) di un grande numero di variabili aleatorie indipendenti **tende a una distribuzione normale**, indipendentemente dalla distribuzione originale.

---
## **📌 Applicazione del CLT**
- **Esempio**: Lancio di un dado onesto $n$ volte.
  - $X_i$ = risultato del $i$-esimo lancio.
  - $\mu = 3.5$, $\sigma^2 = \frac{35}{12}$.
  - Per $n$ grande, la media campionaria $\overline{X_n}$ è approssimativamente normale:
$$
\overline{X_n} \sim \mathcal{N}\left(3.5, \frac{35}{12n}\right)
$$

---
---

# **📊 Stima dei Parametri**

## **🔹 Stima Puntuale**
- **Definizione**: Dati $n$ campioni $X_1, $X_2$, ..., X_n$ da una distribuzione con parametro $\theta$, uno **stimatore** $\hat{\theta}$ è una funzione dei campioni che approssima $\theta$.
- **Esempi di stimatori**:
$$
  1. **Media campionaria**:
$$
$$
\hat{\mu} = \overline{X_n} = \frac{1}{n} \sum_{i=1}^n X_i
$$
$$
  2. **Varianza campionaria**:
$$
$$
\hat{\sigma}^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \overline{X_n})^2
$$

---
## **📌 Proprietà degli Stimatori**
$$
1. **Non distorsione (Unbiasedness)**:
$$
$$
\mathbb{E}[\hat{\theta}] = \theta
$$
   - **Esempio**: $\mathbb{E}[\overline{X_n}] = \mu$ → stimatore non distorto per la media.
$$
2. **Consistenza**:
$$
$$
\hat{\theta}_n \xrightarrow{P} \theta \quad \text{per } n \to \infty
$$
   - **Esempio**: Per la LLN, $\overline{X_n}$ è consistente per $\mu$.
$$
3. **Efficienza**:
$$
   Uno stimatore è **efficiente** se ha la **varianza minima** tra tutti gli stimatori non distorti.

---
## **🔹 Metodo della Massima Verosimiglianza (MLE)**
- **Definizione**: Lo stimatore di massima verosimiglianza $\hat{\theta}_{MLE}$ è il valore di $\theta$ che **massimizza** la **funzione di verosimiglianza** $L(\theta)$.
  - **Funzione di verosimiglianza**:
$$
L(\theta) = \prod_{i=1}^n f_{X|\theta}(x_i | \theta)
$$
    Dove $f_{X|\theta}$ è la PDF (o PMF) della distribuzione parametrizzata da $\theta$.
  - **Log-verosimiglianza**:
$$
\ell(\theta) = \log L(\theta) = \sum_{i=1}^n \log f_{X|\theta}(x_i | \theta)
$$
    (Più facile da massimizzare).

- **Esempio**: Stimare $\mu$ per una distribuzione normale $\mathcal{N}(\mu, \sigma^2)$ con $\sigma^2$ noto.
  - **Verosimiglianza**:
$$
L(\mu) = \prod_{i=1}^n \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x_i - \mu)^2}{2 \sigma^2}}
$$
  - **Log-verosimiglianza**:
$$
\ell(\mu) = -\frac{n}{2} \log(2 \pi \sigma^2) - \frac{1}{2 \sigma^2} \sum_{i=1}^n (x_i - \mu)^2
$$
  - **Massimizzazione**:
$$
\frac{d\ell}{d\mu} = \frac{1}{\sigma^2} \sum_{i=1}^n (x_i - \mu) = 0 \implies \hat{\mu}_{MLE} = \overline{X_n}
$$

---
## **📌 Intervalli di Confidenza**
- **Definizione**: Un **intervallo di confidenza** per un parametro $\theta$ è un intervallo $[L, U]$ tale che:
$$
\mathbb{P}(L ≤ \theta ≤ U) = 1 - \alpha
$$
  Dove $1 - \alpha$ è il **livello di confidenza** (es. 95%).

- **Esempio**: Intervallo di confidenza per la media $\mu$ di una distribuzione normale con varianza nota $\sigma^2$.
  - **Statistica pivotale**:
$$
Z = \frac{\overline{X_n} - \mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0, 1)
$$
  - **Intervallo**:
$$
\left( \overline{X_n} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}}, \overline{X_n} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \right)
$$
    Dove $z_{\alpha/2}$ è il quantile della $\mathcal{N}(0, 1)$ tale che $\mathbb{P}(Z > z_{\alpha/2}) = \alpha/2$.

---
## **🔹 Test di Ipotesi**
- **Definizione**: Un **test di ipotesi** è una procedura per decidere tra due ipotesi:
  - **Ipotesi nulla ($H_0$)**: $\theta = \theta_0$.
  - **Ipotesi alternativa ($H_1$)**: $\theta ≠ \theta_0$ (o $\theta > \theta_0$, $\theta < \theta_0$).

- **Statistica test**:
$$
T = \frac{\overline{X_n} - \theta_0}{\sigma / \sqrt{n}} \sim \mathcal{N}(0, 1) \quad \text{sotto } H_0
$$
- **Regione di rifiuto**:
  - Per un test **bidirezionale** (livello di significatività $\alpha$):
$$
|T| > z_{\alpha/2} \implies \text{Rifiuto } H_0
$$
  - Per un test **unidirezionale** (es. $H_1: \theta > \theta_0$):
$$
T > z_{\alpha} \implies \text{Rifiuto } H_0
$$

---
## **📌 Errori nei Test di Ipotesi**
1. **Errore di Tipo I** (falso positivo):
   - Rifiutare $H_0$ quando è vera.
   - Probabilità = $\alpha$ (livello di significatività).

2. **Errore di Tipo II** (falso negativo):
   - Non rifiutare $H_0$ quando è falsa.
   - Probabilità = $\beta$.

- **Potenza del test**:
$$
1 - \beta = \mathbb{P}(\text{Rifiuto } H_0 | H_1 \text{ vera})
$$

---
---

# **📊 Inferenza Bayesiana**

## **🔹 Introduzione**
- **Approccio bayesiano**: Il parametro $\theta$ è una **variabile aleatoria** con una **distribuzione a priori** $p(\theta)$.
- **Obiettivo**: Aggiornare la distribuzione di $\theta$ alla luce dei dati osservati $X = x$ (distribuzione **a posteriori**).

---
## **📌 Teorema di Bayes**
- **Formula**:
$$
p(\theta | x) = \frac{p(x | \theta) p(\theta)}{p(x)}
$$
  Dove:
  - $p(x | \theta)$ = **verosimiglianza** (dati i parametri).
  - $p(\theta)$ = **prior** (distribuzione a priori di $\theta$).
  - $p(x)$ = **evidenza** (costante di normalizzazione):
$$
p(x) = \int p(x | \theta) p(\theta) \, d\theta
$$

---
## **🎲 Esempio: Stima Bayesiana della Media di una Normale**
- **Dati**: $X_1, $X_2$, ..., X_n \sim \mathcal{N}(\mu, \sigma^2)$ con $\sigma^2$ noto.
- **Prior**: $\mu \sim \mathcal{N}(\mu_0, \tau^2)$.
- **Posterior**:
$$
p(\mu | x_1, ..., x_n) \propto p(x_1, ..., x_n | \mu) p(\mu)
$$
  - **Verosimiglianza**:
$$
p(x_1, ..., x_n | \mu) = \prod_{i=1}^n \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x_i - \mu)^2}{2 \sigma^2}}
$$
  - **Prior**:
$$
p(\mu) = \frac{1}{\sqrt{2 \pi \tau^2}} e^{-\frac{(\mu - \mu_0)^2}{2 \tau^2}}
$$
  - **Posterior**:
$$
\mu | x_1, ..., x_n \sim \mathcal{N}\left( \frac{\frac{n \overline{x}}{\sigma^2} + \frac{\mu_0}{\tau^2}}{\frac{n}{\sigma^2} + \frac{1}{\tau^2}}, \frac{1}{\frac{n}{\sigma^2} + \frac{1}{\tau^2}} \right)
$$
    Dove $\overline{x}$ è la media campionaria.

---
## **📌 Stimatori Bayesiani**
1. **Stimatore a posteriori medio (Bayes Estimator)**:
$$
\hat{\theta}_{\text{Bayes}} = \mathbb{E}[\theta | x]
$$
$$
2. **Stimatore a posteriori modale (MAP)**:
$$
$$
\hat{\theta}_{\text{MAP}} = \arg\max_{\theta} p(\theta | x)
$$

---
## **🔹 Confronto tra Approccio Classico e Bayesiano**
 | **Caratteristica**       | **Approccio Classico**               | **Approccio Bayesiano**               |
$$
 |-------------------------|--------------------------------------|--------------------------------------|
$$
 | **Parametri**           | Fissi (incogniti)                    | Variabili aleatorie                 |
 | **Inferenza**           | Basata solo sui dati                 | Combina dati e prior                 |
 | **Intervalli di confidenza** | Basati su frequenza           | Basati su distribuzione a posteriori |
 | **Interpretazione**     | Probabilità frequentista             | Probabilità soggettiva              |

---
---

# **📚 Riassunto e Conclusioni**

## **🔹 Concetti Chiave**
$$
1. **Probabilità**:
$$
   - Definizione assiomatica (Kolmogorov).
   - Spazi discreti e continui.
   - Eventi, variabili aleatorie, distribuzioni.
$$
2. **Variabili Aleatorie**:
$$
   - Discrete (Binomiale, Poisson, Uniforme).
   - Continue (Normale, Esponenziale, Uniforme).
   - Medie, varianze, covarianze.
$$
3. **Processi Aleatori**:
$$
   - Definizione e esempi (Bernoulli, Poisson, Random Walk).
   - Stazionarietà.
$$
4. **Inferenza Statistica**:
$$
   - Stima puntuale (MLE, metodo dei momenti).
   - Intervalli di confidenza.
   - Test di ipotesi.
   - Inferenza bayesiana.

---
## **📌 Applicazioni Pratiche**
- **Telecomunicazioni**: Modelli di rumore, codifica di canale.
- **Informatica**: Algoritmi probabilistici, machine learning.
- **Finanza**: Modelli stocastici per i mercati.
- **Biologia**: Analisi di dati sperimentali.

---
## **🎯 Consigli per lo Studio**
1. **Esercizi**: Praticare con problemi di calcolo combinatorio e probabilità.
2. **Applicazioni**: Provare a modellare situazioni reali con variabili aleatorie.
3. **Strumenti**: Utilizzare software come **Python (SciPy, NumPy)** o **R** per simulazioni.
$$
4. **Risorse**:
$$
   - Libri: *Sheldon M. Ross, "Introduction to Probability and Statistics for Engineers and Scientists"*.
   - Online: Khan Academy, Coursera (corsi di probabilità e statistica).

---
## **📅 Prossimi Passi**
- **Esame**: Prepararsi sulla teoria e sugli esercizi.
- **Progetti**: Applicare i concetti a dati reali (es. analisi di dataset).
- **Approfondimenti**:
  - Teoria dell’informazione (Shannon, entropia).
  - Processi stocastici avanzati (catene di Markov, processi di Wiener).

---
---

# **📜 Appendice: Formule Utili**

## **🔢 Calcolo Combinatorio**
$$
 | **Formula**                     | **Descrizione**                          |
$$
$$
 |--------------------------------|------------------------------------------|
$$
 | $n!$                         | Fattoriale di $n$                      |
 | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Coefficiente binomiale          |
 | $P(n, k) = \frac{n!}{(n-k)!}$ | Permutazioni di $k$ su $n$          |

---
## **📊 Distribuzioni di Probabilità**
 | **Distribuzione**       | **PMF/PDF**                          | **Media**       | **Varianza**          |
$$
 |-------------------------|--------------------------------------|-----------------|-----------------------|
$$
 | **Binomiale** $\mathcal{B}(n, p)$ | $\binom{n}{k} p^k (1-p)^{n-k}$ | $np$          | $np(1-p)$           |
 | **Poisson** $\mathcal{P}(\lambda)$ | $\frac{\lambda^k}{k!} e^{-\lambda}$ | $\lambda$    | $\lambda$           |
 | **Uniforme Discreta** $\mathcal{U}(\mathcal{X})$ | $\frac{1}{|\mathcal{X}|}$ | Media di $\mathcal{X}$ | Varianza di $\mathcal{X}$ |
 | **Normale** $\mathcal{N}(\mu, \sigma^2)$ | $\frac{1}{$\sqrt{2 \pi \sigma^2}$} e^{-$\frac{(x-\mu)^2}{2 \sigma^2}$}$ | $\mu$ | $\sigma^2$ |
 | **Esponenziale** $\text{Exp}(\lambda)$ | $\lambda e^{-\lambda x}$ (per $x ≥ 0$) | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |

---
## **📈 Teoremi Limite**
$$
 | **Teorema**               | **Enunciato**                                                                 |
$$
$$
 |---------------------------|-----------------------------------------------------------------------------|
$$
 | **Legge dei Grandi Numeri** | $\overline{X_n} \xrightarrow{P} \mu$ per $n \to \infty$               |
 | **Teorema Centrale del Limite** | $\frac{\overline{X_n} - \mu}{\sigma / $\sqrt{n}$} \xrightarrow{d} \mathcal{N}(0, 1)$ |

---
## **🔍 Inferenza Statistica**
$$
 | **Concetto**               | **Formula**                                                                 |
$$
$$
 |----------------------------|-----------------------------------------------------------------------------|
$$
 | **Media campionaria**      | $\overline{X_n} = $\frac{1}{n}$ \sum_{i=1}^n X_i$                          |
 | **Varianza campionaria**   | $S^2 = $\frac{1}{n-1}$ \sum_{i=1}^n ($X_i$ - \overline{X_n})^2$            |
 | **Intervallo di confidenza per $\mu$** | $\overline{X_n} \pm z_{\alpha/2} \frac{\sigma}{$\sqrt{n}$}$ (varianza nota) |
 | **Statistica test (Z-test)** | $Z = \frac{\overline{X_n} - \mu_0}{\sigma / $\sqrt{n}$}$                |

---
---