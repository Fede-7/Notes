---
date: 2026-03-07
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 1
tags:
  - MSI
  - probabilità
  - combinatoria
  - frequenza
  - probabilità-condizionata
  - indipendenza
  - misura
  - poker
Professore: Marco Lops
---

# MSI — Lezione 1: Probabilità Frequentistica e Proprietà Fondamentali

**Docente:** Prof. Marco Lops | **Corso:** Metodi Statistici per l'Informazione | **CFU:** 6

---

## Argomenti trattati

- Completamento esercizi di analisi combinatoria (cinquine da poker)
- Sequenze binarie con esattamente $k$ uni: coefficiente multinomiale
- Definizione frequentistica di probabilità
- Critica e vantaggi dell'approccio frequentistico
- Proprietà della probabilità derivate dalla frequenza (senza assiomi)
- Evento complementare, subadditività, evento $A \setminus B$
- Probabilità condizionata: definizione e intuizione sul database
- Indipendenza stocastica

---

## Completamento: Analisi Combinatoria sul Poker

**Mazzo da poker francese:** 32 carte (7, 8, 9, 10, J, Q, K, A in 4 semi = 8 valori × 4 semi).

Lo spazio dei campioni ha cardinalità:

$$|\Omega| = \binom{32}{5} = \frac{32!}{5! \cdot 27!} = 201.376$$

> [!tip] L'ordinamento non conta nel poker
> Una mano di poker è un sottoinsieme non ordinato: avere A♠ K♥ Q♦ J♣ 10♠ o K♥ A♠ Q♦ J♣ 10♠ è la stessa mano. Si usano sempre i coefficienti binomiali, non le disposizioni.

### Cinquine con esattamente due assi

$$|C_2| = \underbrace{\binom{4}{2}}_{\text{scegli 2 assi tra 4}} \cdot \underbrace{\binom{28}{3}}_{\text{scegli 3 carte non-asso tra 28}} = 6 \cdot 3276 = 69.184$$

$$P(\text{2 assi}) = \frac{69.184}{201.376} \approx 0{,}097 \approx 9{,}7\%$$

Nota: questo include doppie coppie e full (tre tra le altre carte uguali). Se si vuole solo la coppia d'assi come punteggio massimo:

$$|C_{\text{coppia assi}}| = \binom{4}{2} \cdot 28 \cdot \frac{24 \cdot 20}{3!} \qquad \Rightarrow \qquad P \approx 6{,}3\%$$

### Almeno tre assi

$$|C_{\geq 3}| = \underbrace{\binom{4}{3} \cdot \binom{28}{2}}_{\text{tre assi}} + \underbrace{\binom{4}{4} \cdot 28}_{\text{quattro assi}} = 4 \cdot 378 + 28 = 1.540$$

$$P(\geq 3 \text{ assi}) = \frac{1.540}{201.376} \approx 0{,}76\%$$

### Tris di un valore specifico (es. tre 7, senza full né poker)

$$|C_{3\text{sette}}| = \binom{4}{3} \cdot 28 \cdot \frac{24}{2} = 4 \cdot 28 \cdot 12 = 1.344$$

$$P(\text{tris qualsiasi}) = 8 \cdot \frac{1.344}{201.376} \approx 5{,}3\%$$

### Colore di picche

$$|C_{\text{picche}}| = \binom{8}{5} = 56 \qquad \Rightarrow \qquad P(\text{colore picche}) = \frac{56}{201.376} \approx 0{,}11\%$$

$$P(\text{colore qualsiasi}) = 4 \cdot \frac{56}{201.376} \approx 0{,}44\%$$

---

## Sequenze Binarie con Esattamente $k$ Uni

**Domanda:** data una sequenza di $n$ bit, quante sequenze hanno esattamente $k$ uni?

**Ragionamento senza formula:**

Se tutti i bit fossero distinti, ci sarebbero $n!$ permutazioni. Ma nella nostra sequenza ci sono $k$ uni (indistinguibili tra loro) e $n-k$ zeri (indistinguibili tra loro). Le $k!$ permutazioni degli uni tra di loro danno la stessa sequenza, e lo stesso vale per le $(n-k)!$ permutazioni degli zeri.

$$\boxed{|\{x \in \{0,1\}^n : |x|_1 = k\}| = \frac{n!}{k! \cdot (n-k)!} = \binom{n}{k}}$$

**Generalizzazione al caso $m$-ario:** data una sequenza di lunghezza $n$ su un alfabeto di $m$ simboli, con $n_i$ occorrenze del simbolo $i$ (con $\sum_i n_i = n$), il numero di sequenze distinte è il **coefficiente multinomiale**:

$$\binom{n}{n_1, n_2, \ldots, n_m} = \frac{n!}{n_1! \cdot n_2! \cdots n_m!}$$

> [!example] Applicazione in teoria dell'informazione
> Questi conteggi sono fondamentali per il codice universale a lunghezza fissa: determinare quanti messaggi di lunghezza $n$ contengono esattamente $k$ simboli di un certo tipo è la base per calcolare la capacità di un canale.

---

## Definizione Frequentistica di Probabilità

Sia $\Omega$ uno spazio dei campioni discreto (finito o numerabile). Si eseguono $n$ prove indipendenti dello stesso esperimento.

> [!abstract] Definizione: Frequenza di successo
> $$f_n(A) = \frac{N_A}{n}$$
> dove $N_A$ è il numero di volte in cui l'evento $A$ si verifica su $n$ prove.

> [!abstract] Definizione frequentistica: Probabilità
> $$P(A) \stackrel{\text{def}}{=} \lim_{n \to \infty} f_n(A) = \lim_{n \to \infty} \frac{N_A}{n}$$

### Perché questa definizione è intuitiva ma imprecisa

Questa definizione è matematicamente "zoppicante" per due motivi:

**1.** Il limite non esiste sempre — le prove devono essere **indipendenti** (o il processo deve essere ergodico) perché la sequenza $f_n(A)$ converga. Con prove indipendenti la convergenza è **forte** (quasi certamente e in media quadratica).

**2.** Non si specifica il tipo di convergenza. Verrà precisato nel seguito del corso.

Nonostante ciò, l'approccio frequentistico è preferito da questo docente per una ragione pratica: **rende le proprietà della probabilità intuitive**, derivandole direttamente dalle proprietà degli insiemi, senza bisogno di assiomi astratti da dimostrare separatamente.

> [!quote]
> "Io do le carte napoletane, mi ha giocato a scopone, ho dieci carri per uno, poi la probabilità che gli do i sette carri... Con l'approccio teorico la gente cominciava a ragionare in percentuali assurde. Con quello frequentistico si ragiona automaticamente nel modo giusto."

### La probabilità come misura

La probabilità è un **modo diverso di misurare gli elementi di un insieme**. Ordinariamente, in un insieme discreto, ogni elemento "pesa" $\frac{1}{|\Omega|}$. Con la probabilità, alcuni elementi possono pesare molto più di altri.

> [!example] L'ape e la pianta
> Immagina un'aula di 50 m². Ogni metro quadro ha misura ordinaria $\frac{1}{50}$. Se metti una pianta fiorita su un metro quadro, l'ape sarà lì con probabilità $\approx 0{,}99$. Quel metro quadro ora pesa quasi 1 in termini di probabilità, anche se ha la stessa misura ordinaria degli altri 49.

---

## Proprietà della Probabilità (derivate dalla frequenza)

Tutte le seguenti proprietà si derivano senza assiomi, solo dalle proprietà degli insiemi.

### Limitazione

$$0 \leq P(A) \leq 1$$

Il numero di successi non può superare il numero di prove.

### Evento complementare

$$P(A^c) = 1 - P(A)$$

Su $n$ prove, se $A$ si verifica $N_A$ volte, allora $A^c$ si verifica $n - N_A$ volte. Quindi $f_n(A^c) = 1 - f_n(A)$.

### Subadditività (unione di eventi)

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Su $n$ prove, il numero di volte in cui si verifica $A \cup B$ è $N_A + N_B - N_{A \cap B}$ (si somma, ma si sottrae l'intersezione contata due volte).

Caso speciale — eventi **disgiunti** ($A \cap B = \emptyset$):

$$P(A \cup B) = P(A) + P(B)$$

> [!tip] La probabilità è una misura
> Proprio come la misura di due insiemi che si sovrappongono non è la somma delle misure (si conta due volte l'intersezione), la probabilità di $A \cup B$ non è la semplice somma. La probabilità è subadditiva esattamente come lo è qualsiasi misura.

### Differenza di eventi

$$P(A \setminus B) = P(A) - P(A \cap B)$$

Il numero di volte in cui si verifica $A$ ma non $B$ è $N_A - N_{A \cap B}$.

### Evento certo e impossibile

$$P(\Omega) = 1 \qquad P(\emptyset) = 0$$

L'evento certo si verifica tutte le $n$ volte; $f_n(\Omega) = n/n = 1$.

> [!warning] Probabilità nulla ≠ evento impossibile
> Un evento con probabilità 0 può comunque verificarsi (infinite volte, ma con frequenza che tende a 0). Esempio: se un evento si verifica $\sqrt{n}$ volte su $n$ prove, si verifica infinite volte, ma $P = \lim_{n \to \infty} \frac{\sqrt{n}}{n} = 0$.
>
> Si dice allora che l'evento si verifica **quasi certamente** (quasi ovunque, nel linguaggio della teoria della misura).

---

## Dado Truccato: Esempio di Probabilità Non Equiprobabili

Supponiamo che il dado sia truccato così: il risultato 1 esce 5 volte più spesso degli altri risultati (tra loro equiprobabili).

Allora: $N_1 = 5 \cdot (N_2 + N_3 + N_4 + N_5 + N_6)/5$, da cui:

$$P(1) = \frac{5}{10} = \frac{5}{6}^\star \qquad P(i) = \frac{1}{30} \text{ per } i = 2,\ldots,6$$

> [!warning] Correzione: ricalcolo esatto
> Con il dado truccato dove $N_1 = 5 \cdot N_i$ per ogni $i \neq 1$, e $\sum P = 1$:
> $$5x + 5x = 1 \Rightarrow x = \frac{1}{10}, \quad P(1) = \frac{5}{10} = \frac{1}{2}, \quad P(i) = \frac{1}{10} \text{ per } i \neq 1$$
>
> Quindi: $P(\text{pari}) = P(2) + P(4) + P(6) = 3 \cdot \frac{1}{10} = 30\%$, mentre $P(\text{dispari}) = P(1) + P(3) + P(5) = \frac{1}{2} + \frac{1}{10} + \frac{1}{10} = 70\%$.
>
> Morale: **quando gli eventi elementari non sono equiprobabili**, calcolare la probabilità di un evento come rapporto di cardinalità **non ha senso**. Si deve usare la definizione frequentistica o la misura di probabilità corretta.

---

## Probabilità Condizionata

### Intuizione: il database

Immagina un database con tutti i residenti in Italia, con colonne altezza, peso, colore occhi.

$P(\text{peso} \geq 70 \text{ kg})$: conto quanti pesano almeno 70 kg, divido per il totale.

$P(\text{peso} \geq 70 \text{ kg} \mid \text{altezza} \geq 170 \text{ cm})$: **restringo il database** alle sole persone alte almeno 170 cm (elimino tutti gli altri), poi conto quanti di questi pesano almeno 70 kg, divido per la dimensione del database ristretto.

$$f_n(B \mid A) = \frac{N_{A \cap B}}{N_A} = \frac{N_{A \cap B}/n}{N_A/n} = \frac{f_n(A \cap B)}{f_n(A)}$$

Passando al limite:

> [!abstract] Definizione: Probabilità condizionata
> $$P(B \mid A) = \frac{P(A \cap B)}{P(A)}, \qquad P(A) > 0$$
>
> "La probabilità che si verifichi $B$, dato che si è verificato $A$, è il rapporto tra la probabilità che si verifichino entrambi e la probabilità di $A$."

Il condizionamento cambia lo spazio dei campioni: da $\Omega$ si passa a $A$ come nuovo universo di riferimento.

**Da questa definizione si ricava:**

$$P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)$$

### Probabilità a priori vs a posteriori

La **probabilità a priori** $P(\text{peso} \geq 70 \text{ kg})$ include tutti gli italiani (bambini, donne anziane, ...). La **probabilità a posteriori** $P(\text{peso} \geq 70 \text{ kg} \mid \text{altezza} \geq 170 \text{ cm})$ è più alta: filtrando per altezza, si esclude una porzione di persone che mediamente pesano meno.

---

## Indipendenza Stocastica

$P(\text{peso} \geq 70 \text{ kg} \mid \text{altezza} \geq 170 \text{ cm})$ è diversa da $P(\text{peso} \geq 70 \text{ kg})$: sapere l'altezza dà informazione sul peso.

Ma $P(\text{occhi chiari} \mid \text{altezza} \geq 170 \text{ cm}) = P(\text{occhi chiari})$: sapere l'altezza non dà alcuna informazione sul colore degli occhi.

> [!abstract] Definizione: Indipendenza stocastica
> Due eventi $A$ e $B$ sono **indipendenti** se e solo se:
> $$P(B \mid A) = P(B) \qquad \Longleftrightarrow \qquad P(A \cap B) = P(A) \cdot P(B)$$
>
> Il verificarsi di $A$ non fornisce alcuna informazione sul verificarsi di $B$.

> [!example] Dadi indipendenti
> Se lancio due dadi onesti, il risultato del secondo non dipende dal primo. Quindi:
> $$P(\text{primo} = 5 \text{ e secondo} = 2) = P(\text{primo} = 5) \cdot P(\text{secondo} = 2) = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$$

---

## Regola pratica: "Almeno uno" → pensare al complementare

> [!tip] Strategia: usare il complementare
> Quando il problema chiede "almeno uno / almeno due / almeno $k$", conviene calcolare la probabilità del complementare ("nessuno / meno di $k$") e sottrarre da 1.

**Esempio:** probabilità di ottenere almeno un 6 lanciando un dado onesto 5 volte.

$P(\text{almeno un 6}) = 1 - P(\text{nessun 6})$

I lanci sono **indipendenti**, quindi:

$$P(\text{nessun 6 in 5 lanci}) = \left(\frac{5}{6}\right)^5 \approx 0{,}402$$

$$P(\text{almeno un 6}) = 1 - \left(\frac{5}{6}\right)^5 \approx 0{,}598 \approx 60\%$$

**Esempio classico (paradosso del compleanno):** probabilità che in una classe di 30 persone ci siano almeno due con lo stesso compleanno.

$$P(\text{almeno due stessi}) = 1 - P(\text{tutti diversi}) = 1 - \prod_{k=0}^{29} \frac{365-k}{365}$$

Il risultato è circa 70% — molto più alto di quanto l'intuizione suggerisce.

---

> [!summary] Punti chiave della lezione
> - Il coefficiente binomiale $\binom{n}{k}$ conta le sequenze binarie di lunghezza $n$ con esattamente $k$ uni: si deriva solo dal ragionamento sulle permutazioni degli indistinguibili.
> - La probabilità frequentistica $P(A) = \lim_{n \to \infty} N_A/n$ è intuitiva e permette di derivare tutte le proprietà dalle operazioni sugli insiemi.
> - Quando gli eventi elementari non sono equiprobabili, non si può usare il rapporto di cardinalità.
> - La probabilità è una **misura**: subadditiva per l'unione, additiva per eventi disgiunti.
> - La probabilità condizionata $P(B \mid A) = P(A \cap B)/P(A)$ corrisponde al restringimento dello spazio dei campioni ad $A$.
> - Due eventi sono indipendenti se $P(A \cap B) = P(A) \cdot P(B)$.
> - Per "almeno uno", usare il complementare è quasi sempre la strategia migliore.

## Prossimi argomenti

- [ ] Teorema della probabilità totale
- [ ] Teorema di Bayes
- [ ] Variabili aleatorie discrete
- [ ] Esercizi su probabilità condizionata, indipendenza e Bayes

---

#MSI #probabilità #frequenza #probabilità-condizionata #indipendenza #misura #combinatoria #complementare #Bayes
