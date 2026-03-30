---
Date: 2026-03-26
Professore:
tags:
  - nota
---
Sulla base delle dispense e del file delle domande, ecco un approfondimento strutturato sulle domande "calde" identificate dall'oratore, con i riferimenti formali necessari per l'esame con il Prof. De Luca.

### 1. Ricorsività e Insiemi
[cite_start]L'oratore suggerisce di studiare la definizione più generica possibile (pagine 11-14 delle dispense)[cite: 356, 381].
* [cite_start]**Definizione di Funzione Parzialmente Calcolabile:** Una funzione $f: D \subseteq \mathbb{N}^k \to \mathbb{N}$ è parzialmente calcolabile se esiste un algoritmo (S-programma) che la rappresenta[cite: 366]. [cite_start]Se l'input non appartiene al dominio $D$, il programma non termina (diverge)[cite: 395, 397].
* [cite_start]**Insiemi Ricorsivi:** Un insieme $A$ è ricorsivo se la sua funzione caratteristica $C_A(x)$ è calcolabile (ovvero è totale e parzialmente calcolabile)[cite: 366].
* **Dimostrazione di Chiusura (Unione e Intersezione):**
    * [cite_start]**Unione:** Se $A$ e $B$ sono ricorsivi, le loro funzioni caratteristiche $C_A$ e $C_B$ sono calcolabili[cite: 366]. La funzione caratteristica dell'unione $A \cup B$ è data da $C_{A \cup B}(x) = \max(C_A(x), C_B(x))$. [cite_start]Poiché il $\max$ è una funzione ricorsiva primitiva (PRC), l'unione è un insieme ricorsivo[cite: 252].
    * **Intersezione:** La funzione caratteristica è $C_{A \cap B}(x) = C_A(x) \cdot C_B(x)$. [cite_start]Essendo il prodotto una funzione PRC, l'intersezione è ricorsiva[cite: 252].

### 2. Funzione di Pairing e Numeri di Gödel
[cite_start]Questa parte riguarda la codifica di coppie di numeri in un unico intero (pagg. 22-23 del file domande e 27-28 delle dispense)[cite: 253, 1402].
* [cite_start]**Funzione "Angoletto":** Definita come $\langle x, y \rangle = 2^x(2y + 1) - 1$[cite: 253].
* [cite_start]**Proprietà:** È una funzione biunivoca (biiettiva) tra $\mathbb{N}^2$ e $\mathbb{N}$[cite: 253].
* [cite_start]**Funzioni Inverse:** Esistono due funzioni calcolabili, solitamente indicate come $l(z)$ e $r(z)$, tali che $l(\langle x, y \rangle) = x$ e $r(\langle x, y \rangle) = y$[cite: 253, 1402]. [cite_start]Queste permettono di decodificare la coppia originale dall'unico numero di Gödel[cite: 253].

### 3. Linguaggi Regolari e Automi
[cite_start]L'oratore sottolinea l'importanza delle definizioni formali e del Pumping Lemma[cite: 354, 355].
* **Pumping Lemma:** Se un linguaggio $L$ è regolare, esiste un intero $n$ (numero di stati del DFA) tale che ogni stringa $x \in L$ con $|x| [cite_start]\ge n$ può essere divisa in $uvw$ soddisfacendo[cite: 125, 181]:
    1. [cite_start]$x = uvw$ [cite: 125, 181]
    2. [cite_start]$v \neq \epsilon$ [cite: 125, 181]
    3. $|uv| [cite_start]\le n$ [cite: 181]
    4. [cite_start]$\forall i \ge 0, uv^iw \in L$[cite: 125, 181].
* **Chiusura (Concatenazione e Iterazione):**
    * [cite_start]**Concatenazione:** Se $L_1$ e $L_2$ sono regolari, lo è anche $L_1 \cdot L_2$[cite: 255]. [cite_start]La dimostrazione si basa sulla costruzione di un NFA che, arrivato agli stati finali di $L_1$, può passare (tramite $\epsilon$-transizioni) allo stato iniziale di $L_2$[cite: 255].
    * [cite_start]**Iterazione (Star):** La chiusura per l'operazione di stella di Kleene ($L^*$) si dimostra aggiungendo transizioni che riportano dagli stati finali allo stato iniziale[cite: 255].
* [cite_start]**DFA/NFA:** Devi conoscere la quintupla formale $M = (Q, \Sigma, \delta, $q_0$, F)$[cite: 212, 254].

### 4. Dagli Automi alle Grammatiche
[cite_start]Se un linguaggio è accettato da un DFA, è possibile costruire una **Grammatica Regolare** (Tipo 3) equivalente[cite: 207, 212].
* **Costruzione:**
    * [cite_start]Ogni stato $q_i$ del DFA diventa un non-terminale $A_i$ della grammatica[cite: 213].
    * [cite_start]Se nel DFA c'è una transizione $\delta($q_i$, a) = q_j$, nella grammatica si aggiunge la produzione $A_i \to aA_j$[cite: 208, 218].
    * [cite_start]Se $q_i$ è uno stato finale ($q_i \in F$), si aggiunge la produzione $A_i \to \epsilon$[cite: 208, 219].
* [cite_start]Questa costruzione dimostra che ogni linguaggio regolare è context-free[cite: 210, 221].