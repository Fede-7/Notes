# Lezione 13: Congruenze Modulo m e Anelli Quoziente Zn

**Data:** 06/05/2025 (come da note)
**Argomenti:** Congruenze in Z, Compatibilità con somma e prodotto, Anello Quoziente Zm, Classi di Resto, Tavole di Cayley per Zm, Campi Zm (quando m è primo), Caratteristica di Zm, Invertibili e Divisori dello Zero in Zm (legame con MCD), Elementi Nilpotenti in Zm, Equazioni Congruenziali, Algoritmo Euclideo Esteso, Esercizi.

#tag/number-theory #tag/congruences #tag/modular-arithmetic #tag/rings #tag/quotient-rings #tag/fields #tag/zero-divisor #tag/nilpotent #tag/euclidean-algorithm #tag/algebra-avanzata

---

## 1. Congruenze in $\mathbb{Z}$

Introduciamo una relazione fondamentale sull'insieme degli interi $\mathbb{Z}$.

*   **Definizione:** Sia $m \in \mathbb{Z}$ un intero fissato (chiamato **modulo**). Dati $a, b \in \mathbb{Z}$, diciamo che $a$ è **congruo** a $b$ modulo $m$, e scriviamo $a \equiv b \pmod{m}$ (o $a \pmod{m} b$), se $m$ divide la differenza $(a-b)$.
    $$ a \equiv b \pmod{m} \iff m \mid (a-b) $$
    *   Questo significa che esiste un intero $k \in \mathbb{Z}$ tale che $a - b = m \cdot k$.
    *   Nota: La relazione di congruenza modulo $m$ è la stessa della congruenza modulo $-m$, quindi possiamo solitamente assumere $m \ge 0$.

*   **Casi Particolari:**
    *   **m = 0:** $a \equiv b \pmod{0} \iff 0 \mid (a-b)$. L'unico multiplo di 0 è 0 stesso. Quindi $a-b=0 \iff a=b$. La congruenza modulo 0 è semplicemente l'**uguaglianza**.
    *   **m = 1:** $a \equiv b \pmod{1} \iff 1 \mid (a-b)$. Poiché 1 divide qualsiasi intero, questa relazione è **sempre vera** per ogni $a, b \in \mathbb{Z}$. È la relazione totale.

*   **Equivalenza con i Resti (per m $\ge$ 2):**
    Sia $m \ge 2$. Allora $a \equiv b \pmod{m}$ se e solo se $a$ e $b$ hanno lo **stesso resto** nella divisione euclidea per $m$.
    $$ a \equiv b \pmod{m} \iff \text{rest}(a, m) = \text{rest}(b, m) $$
    *   **Dimostrazione (cenno):**
        *   ($\implies$) Se $a \equiv b \pmod{m}$, allora $a-b = mk$. Siano $a=mq_a+r_a$ e $b=mq_b+r_b$ con $0 \le r_a, r_b < m$. Allora $a-b = m(q_a-q_b) + (r_a-r_b)$. Poiché $a-b=mk$, abbiamo $mk = m(q_a-q_b) + (r_a-r_b)$, quindi $r_a-r_b = m(k-q_a+q_b)$. Dato che $0 \le r_a, r_b < m$, si ha $-m < r_a-r_b < m$. L'unico multiplo di $m$ in questo intervallo è 0. Quindi $r_a-r_b=0$, cioè $r_a=r_b$.
        *   ($\impliedby$) Se $r_a=r_b$, allora $a=mq_a+r_a$ e $b=mq_b+r_a$. $a-b = m(q_a-q_b)$. Quindi $m \mid (a-b)$, cioè $a \equiv b \pmod{m}$.

*   **Proprietà:** Per un $m$ fissato, la relazione $\equiv \pmod{m}$ è una **relazione di equivalenza** su $\mathbb{Z}$ (è riflessiva, simmetrica, transitiva).

[[Congruenza (teoria dei numeri)]] [[Divisione Euclidea]] [[Relazione di equivalenza]]

---

## 2. Compatibilità della Congruenza con le Operazioni

La relazione di congruenza si "comporta bene" rispetto alla somma e al prodotto in $\mathbb{Z}$.

*   **Compatibilità con la Somma (Pag 2):**
    Se $a \equiv c \pmod{m}$ e $b \equiv d \pmod{m}$, allora $(a+b) \equiv (c+d) \pmod{m}$.
    *   **Dimostrazione:**
        *   $a \equiv c \pmod{m} \implies a - c = m \cdot h$ per qualche $h \in \mathbb{Z}$.
        *   $b \equiv d \pmod{m} \implies b - d = m \cdot k$ per qualche $k \in \mathbb{Z}$.
        *   Sommiamo le due equazioni: $(a-c) + (b-d) = mh + mk$.
        *   Riorganizziamo: $(a+b) - (c+d) = m(h+k)$.
        *   Poiché $h+k \in \mathbb{Z}$, questo significa $m \mid ((a+b) - (c+d))$.
        *   Quindi, $(a+b) \equiv (c+d) \pmod{m}$.

*   **Compatibilità con il Prodotto (Pag 3):**
    Se $a \equiv c \pmod{m}$ e $b \equiv d \pmod{m}$, allora $(a \cdot b) \equiv (c \cdot d) \pmod{m}$.
    *   **Dimostrazione:**
        *   $a = c + mh$
        *   $b = d + mk$
        *   Moltiplichiamo: $a \cdot b = (c + mh)(d + mk) = cd + cmk + mhd + m^2hk$.
        *   $ab = cd + m(ck + hd + mhk)$.
        *   $ab - cd = m(ck + hd + mhk)$.
        *   Poiché $(ck + hd + mhk) \in \mathbb{Z}$, questo significa $m \mid (ab - cd)$.
        *   Quindi, $ab \equiv cd \pmod{m}$.

> [!IMPORTANT] La compatibilità della congruenza con somma e prodotto è ciò che permette di definire le operazioni sull'insieme quoziente $\mathbb{Z}_m$.

---

## 3. L'Anello Quoziente $\mathbb{Z}_m$

L'insieme delle classi di equivalenza della congruenza modulo $m$.

*   **Classe di Resto (o di Congruenza) (Pag 5):** Dato $a \in \mathbb{Z}$ e $m \ge 1$, la classe di resto di $a$ modulo $m$ è l'insieme di tutti gli interi congrui ad $a$ modulo $m$:
    $$ [a]_m = \{ b \in \mathbb{Z} \mid b \equiv a \pmod{m} \} = \{ a + mk \mid k \in \mathbb{Z} \} $$
    *   Proprietà: $[a]_m = [b]_m \iff a \equiv b \pmod{m}$.
    *   Se $r_a = \text{rest}(a, m)$, allora $[a]_m = [r_a]_m$. Ogni classe ha un unico rappresentante nell'intervallo $\{0, 1, ..., m-1\}$.

*   **Insieme Quoziente $\mathbb{Z}_m$ (Pag 4, 6):** L'insieme di tutte le classi di resto modulo $m$.
    $$ \mathbb{Z}_m = \mathbb{Z} / m\mathbb{Z} = \{ [a]_m \mid a \in \mathbb{Z} \} $$
    *   Poiché ogni classe è rappresentata univocamente da un resto $r$ con $0 \le r < m$, possiamo scrivere:
        $$ \mathbb{Z}_m = \{ [0]_m, [1]_m, \dots, [m-1]_m \} $$
    *   La cardinalità è $|\mathbb{Z}_m| = m$.

*   **Operazioni in $\mathbb{Z}_m$ (Pag 4):** Grazie alla compatibilità, possiamo definire somma e prodotto tra classi usando i rappresentanti:
    *   **Somma:** $[a]_m + [b]_m = [a+b]_m$
    *   **Prodotto:** $[a]_m \cdot [b]_m = [a \cdot b]_m$
    *   Queste operazioni sono **ben definite**, cioè il risultato non dipende dalla scelta dei rappresentanti $a$ e $b$ all'interno delle loro classi.

*   **Struttura Algebrica (Pag 4):** $(\mathbb{Z}_m, +, \cdot)$ è un **Anello Commutativo Unitario**.
    *   L'elemento neutro additivo è $[0]_m$. L'opposto di $[a]_m$ è $[-a]_m = [m-a]_m$.
    *   L'elemento neutro moltiplicativo (unità) è $[1]_m$ (per $m \ge 2$).
    *   Associatività, commutatività e distributività seguono dalle proprietà corrispondenti in $\mathbb{Z}$.

*   **Esempi (Pag 8):**
    *   $\mathbb{Z}_2 = \{[0]_2, [1]_2\}$. $[0]_2$ sono i pari, $[1]_2$ sono i dispari.
    *   $\mathbb{Z}_3 = \{[0]_3, [1]_3, [2]_3\}$. $[0]_3 = \{..., -3, 0, 3, 6, ...\}$, $[1]_3 = \{..., -2, 1, 4, 7, ...\}$, $[2]_3 = \{..., -1, 2, 5, 8, ...\}$.

[[Aritmetica modulare]] [[Classe di resto]] [[Anello quoziente]]

---

## 4. Tavole di Cayley ed Esempi $\mathbb{Z}_m$

*   **Esempio $\mathbb{Z}_4 = \{\bar{0}, \bar{1}, \bar{2}, \bar{3}\}$ (Pag 9):** (Usiamo $\bar{a}$ come notazione per $[a]_4$)
    *   **Tavola Additiva (+):**

        | +         | $\bar{0}$ | $\bar{1}$ | $\bar{2}$ | $\bar{3}$ |
        | :-------- | :-------- | :-------- | :-------- | :-------- |
        | $\bar{0}$ | $\bar{0}$ | $\bar{1}$ | $\bar{2}$ | $\bar{3}$ |
        | $\bar{1}$ | $\bar{1}$ | $\bar{2}$ | $\bar{3}$ | $\bar{0}$ |
        | $\bar{2}$ | $\bar{2}$ | $\bar{3}$ | $\bar{0}$ | $\bar{1}$ |
        | $\bar{3}$ | $\bar{3}$ | $\bar{0}$ | $\bar{1}$ | $\bar{2}$ |
        *   $(\mathbb{Z}_4, +)$ è un gruppo abeliano.
    *   **Tavola Moltiplicativa ($\cdot$):**

        | $\cdot$   | $\bar{0}$ | $\bar{1}$ | $\bar{2}$ | $\bar{3}$ |
        | :-------- | :-------- | :-------- | :-------- | :-------- |
        | $\bar{0}$ | $\bar{0}$ | $\bar{0}$ | $\bar{0}$ | $\bar{0}$ |
        | $\bar{1}$ | $\bar{0}$ | $\bar{1}$ | $\bar{2}$ | $\bar{3}$ |
        | $\bar{2}$ | $\bar{0}$ | $\bar{2}$ | $\bar{0}$ | $\bar{2}$ |
        | $\bar{3}$ | $\bar{0}$ | $\bar{3}$ | $\bar{2}$ | $\bar{1}$ |
        *   $(\mathbb{Z}_4, \cdot)$ è un monoide commutativo (unità $\bar{1}$).
        *   **Divisori dello Zero:** $\bar{2} \cdot \bar{2} = \bar{0}$. Poiché $\bar{2} \neq \bar{0}$, $\bar{2}$ è un divisore dello zero.
        *   **Elementi Nilpotenti:** $\bar{2}^2 = \bar{0}$. $\bar{2}$ è nilpotente.
        *   **Elementi Invertibili:** Solo $\bar{1}$ e $\bar{3}$ hanno inverso ($\bar{1}^{-1}=\bar{1}$, $\bar{3}^{-1}=\bar{3}$ perché $\bar{3} \cdot \bar{3} = \bar{9} = \bar{1}$). $U(\mathbb{Z}_4) = \{\bar{1}, \bar{3}\}$.
        *   **Cancellabilità:** $\bar{2}$ non è cancellabile (es. $\bar{2} \cdot \bar{1} = \bar{2}$ e $\bar{2} \cdot \bar{3} = \bar{6} = \bar{2}$, ma $\bar{1} \neq \bar{3}$).

*   **Esempio $\mathbb{Z}_5 = \{\bar{0}, \bar{1}, \bar{2}, \bar{3}, \bar{4}\}$ (Pag 10):**
    *   **Tavola Moltiplicativa ($\cdot$):**

        | $\cdot$   | $\bar{0}$ | $\bar{1}$ | $\bar{2}$ | $\bar{3}$ | $\bar{4}$ |
        | :-------- | :-------- | :-------- | :-------- | :-------- | :-------- |
        | $\bar{0}$ | $\bar{0}$ | $\bar{0}$ | $\bar{0}$ | $\bar{0}$ | $\bar{0}$ |
        | $\bar{1}$ | $\bar{0}$ | $\bar{1}$ | $\bar{2}$ | $\bar{3}$ | $\bar{4}$ |
        | $\bar{2}$ | $\bar{0}$ | $\bar{2}$ | $\bar{4}$ | $\bar{1}$ | $\bar{3}$ |
        | $\bar{3}$ | $\bar{0}$ | $\bar{3}$ | $\bar{1}$ | $\bar{4}$ | $\bar{2}$ |
        | $\bar{4}$ | $\bar{0}$ | $\bar{4}$ | $\bar{3}$ | $\bar{2}$ | $\bar{1}$ |
    *   **Osservazioni:**
        *   Non ci sono divisori dello zero (a parte $\bar{0}$). Ogni riga/colonna non nulla contiene $\bar{0}$ solo nella prima posizione.
        *   Tutti gli elementi non nulli $\{\bar{1}, \bar{2}, \bar{3}, \bar{4}\}$ sono invertibili: $\bar{1}^{-1}=\bar{1}$, $\bar{2}^{-1}=\bar{3}$, $\bar{3}^{-1}=\bar{2}$, $\bar{4}^{-1}=\bar{4}$.
        *   $U(\mathbb{Z}_5) = \mathbb{Z}_5 \setminus \{\bar{0}\}$.

---

## 5. Campi $\mathbb{Z}_m$ e Caratteristica

> [!TEOREM] Teorema: $\mathbb{Z}_m$ è un Campo se e solo se $m$ è Primo
> *   **Enunciato (Pag 11):** L'anello $(\mathbb{Z}_m, +, \cdot)$ è un **campo** se e solo se $m$ è un numero **primo**.
> *   **Idea Chiave:** Questo risultato collega la struttura algebrica di $\mathbb{Z}_m$ (essere un campo, dove la divisione per elementi non nulli è sempre possibile) a una proprietà fondamentale del modulo $m$ (essere primo).
> *   **Spiegazione (legata al Capitolo 6):** La dimostrazione completa si basa sulla caratterizzazione degli elementi invertibili in $\mathbb{Z}_m$. Un anello commutativo unitario è un campo se e solo se ogni suo elemento non nullo è invertibile. Come vedremo, un elemento $[a]_m$ (con $a \not\equiv 0 \pmod m$) è invertibile in $\mathbb{Z}_m$ se e solo se $\text{MCD}(a, m)=1$.
>     Quindi, $\mathbb{Z}_m$ è un campo
>     $\iff$ ogni $[a]_m$ con $a \in \{1, 2, \dots, m-1\}$ è invertibile
>     $\iff$ per ogni $a \in \{1, 2, \dots, m-1\}$, si ha $\text{MCD}(a, m)=1$
>     $\iff m$ non ha divisori propri (diversi da 1 e se stesso)
>     $\iff m$ è un numero primo.
> *   **Esempi:** $\mathbb{Z}_2, \mathbb{Z}_3, \mathbb{Z}_5, \mathbb{Z}_7, \mathbb{Z}_{11}, \dots$ sono campi. $\mathbb{Z}_4, \mathbb{Z}_6, \mathbb{Z}_8, \mathbb{Z}_9, \mathbb{Z}_{10}, \dots$ non sono campi.


> [!INFO] Caratteristica di $\mathbb{Z}_m$
> *   **Definizione (Pag 11-12):** La **caratteristica** di un anello unitario $R$, indicata con $char(R)$, è il più piccolo intero positivo $k$ tale che la somma di $k$ copie dell'elemento neutro moltiplicativo $1_R$ sia uguale all'elemento neutro additivo $0_R$. Se un tale $k$ non esiste, la caratteristica è 0.
> *   **Proposizione:** Per ogni $m \ge 1$, la caratteristica dell'anello $\mathbb{Z}_m$ è $m$.
>     $$ char(\mathbb{Z}_m) = m $$
> *   **Dimostrazione:**
>     1.  L'elemento neutro moltiplicativo (unità) in $\mathbb{Z}_m$ è $[1]_m$.
>     2.  L'elemento neutro additivo (zero) in $\mathbb{Z}_m$ è $[0]_m$.
>     3.  Dobbiamo trovare il più piccolo intero positivo $k$ tale che:
>         $$ \underbrace{[1]_m + [1]_m + \dots + [1]_m}_{k \text{ volte}} = [0]_m $$
>     4.  Per la definizione di somma in $\mathbb{Z}_m$, il lato sinistro è uguale a $[1+1+\dots+1]_m = [k]_m$.
>     5.  Quindi, cerchiamo il più piccolo intero positivo $k$ tale che $[k]_m = [0]_m$.
>     6.  La condizione $[k]_m = [0]_m$ è equivalente a $k \equiv 0 \pmod{m}$.
>     7.  Questo significa che $m$ deve dividere $k$.
>     8.  Il più piccolo intero *positivo* $k$ che è divisibile per $m$ è proprio $m$ stesso (assumendo $m \ge 1$).
>     9.  Pertanto, $char(\mathbb{Z}_m) = m$.


[[Campo finito]] [[Caratteristica (algebra)]]

---

## 6. Invertibili e Divisori dello Zero in $\mathbb{Z}_m$

Sia $m \ge 2$. Consideriamo $\bar{a} \in \mathbb{Z}_m$ con $\bar{a} \neq \bar{0}$.

*   **Proposizione (Pag 13):**
    1.  $\bar{a}$ è un **divisore dello zero** in $\mathbb{Z}_m \iff \text{MCD}(a, m) > 1$.
    2.  $\bar{a}$ è **invertibile** in $\mathbb{Z}_m \iff \text{MCD}(a, m) = 1$.

*   **Dimostrazione 1 ($\impliedby$):** Se $d = \text{MCD}(a, m) > 1$. Allora $a=d \cdot a_1$ e $m=d \cdot m_1$ con $1 \le m_1 < m$. Consideriamo $\bar{b} = \bar{m_1}$. Poiché $m_1 < m$, $\bar{m_1} \neq \bar{0}$. Calcoliamo $\bar{a} \cdot \bar{b} = \bar{a} \cdot \bar{m_1} = \overline{a \cdot m_1} = \overline{(da_1)m_1} = \overline{a_1(dm_1)} = \overline{a_1 m} = \bar{0}$. Abbiamo trovato $\bar{b} \neq \bar{0}$ tale che $\bar{a}\bar{b}=\bar{0}$. Quindi $\bar{a}$ è divisore dello zero.
    *   **Esempio (Pag 15):** $\bar{6} \in \mathbb{Z}_{15}$. $\text{MCD}(6, 15)=3 > 1$. $m_1 = 15/3 = 5$. Allora $\bar{6} \cdot \bar{5} = \overline{30} = \bar{0}$ in $\mathbb{Z}_{15}$.

*   **Dimostrazione 1 ($\implies$):** Se $\bar{a}$ è divisore dello zero, esiste $\bar{b} \neq \bar{0}$ tale che $\bar{a}\bar{b}=\bar{0}$. Questo significa $ab \equiv 0 \pmod{m}$, cioè $m \mid ab$. Se fosse $\text{MCD}(a, m)=1$, allora per una proprietà della divisibilità (generalizzazione Lemma Euclide), dovremmo avere $m \mid b$. Ma se $m \mid b$, allora $\bar{b}=\bar{0}$, che contraddice l'ipotesi $\bar{b} \neq \bar{0}$. Quindi deve essere $\text{MCD}(a, m) > 1$.

*   **Dimostrazione 2 ($\impliedby$):** Se $\text{MCD}(a, m)=1$. Per il **Teorema di Bézout**, esistono interi $h, k$ tali che $a \cdot h + m \cdot k = 1$. Considerando questa equazione modulo $m$: $ah + mk \equiv 1 \pmod{m}$. Poiché $mk \equiv 0 \pmod{m}$, otteniamo $ah \equiv 1 \pmod{m}$. Questo significa $\bar{a} \cdot \bar{h} = \bar{1}$ in $\mathbb{Z}_m$. Quindi $\bar{h}$ è l'inverso di $\bar{a}$. $\bar{a}$ è invertibile.

*   **Dimostrazione 2 ($\implies$):** Se $\bar{a}$ è invertibile, esiste $\bar{b}$ tale che $\bar{a}\bar{b}=\bar{1}$. Questo significa $ab \equiv 1 \pmod{m}$, cioè $ab - 1 = mk$ per qualche $k$. Riscrivendo: $ab - mk = 1$. Questa è un'identità di Bézout. Poiché esiste una combinazione lineare di $a$ e $m$ che dà 1, il loro massimo comun divisore deve essere 1. $\text{MCD}(a, m)=1$.

*   **Osservazione (Pag 13):** In $\mathbb{Z}_m$, ogni elemento $\bar{a} \neq \bar{0}$ o è invertibile (se $\text{MCD}(a,m)=1$) o è un divisore dello zero (se $\text{MCD}(a,m)>1$).

*   **Esempio $\mathbb{Z}_{15}$ (Pag 19):**
    *   Invertibili: $\text{MCD}(a, 15)=1$. $a \in \{1, 2, 4, 7, 8, 11, 13, 14\}$. $U(\mathbb{Z}_{15}) = \{\bar{1}, \bar{2}, \bar{4}, \bar{7}, \bar{8}, \overline{11}, \overline{13}, \overline{14}\}$.
    *   Divisori dello Zero: $\text{MCD}(a, 15)>1$. $a \in \{3, 5, 6, 9, 10, 12\}$. Divisori: $\{\bar{3}, \bar{5}, \bar{6}, \bar{9}, \overline{10}, \overline{12}\}$.

[[Gruppo moltiplicativo degli interi modulo n]] [[Teorema di Bézout]]

---

## 7. Elementi Nilpotenti in $\mathbb{Z}_m$

*   **Proposizione (Pag 20):** Sia $m = p_1^{\alpha_1} \cdots p_t^{\alpha_t}$ la fattorizzazione in primi distinti di $m$. Sia $a = p_1^{\beta_1} \cdots p_t^{\beta_t}$ con $1 \le \beta_i$ per ogni $i$ (cioè $a$ è multiplo di ogni primo che divide $m$). Allora $\bar{a} \in \mathbb{Z}_m$ è **nilpotente**. (Senza dimostrazione qui).
*   **Esempio $\mathbb{Z}_{40}$ (Pag 21):** $40 = 2^3 \cdot 5^1$. Gli elementi nilpotenti (oltre a $\bar{0}$) sono multipli di $2 \cdot 5 = 10$. Quindi $\overline{10}, \overline{20}, \overline{30}$. Verifichiamo $\overline{10}$: $\overline{10}^2 = \overline{100} = \overline{2 \cdot 40 + 20} = \overline{20}$. $\overline{10}^3 = \overline{10} \cdot \overline{20} = \overline{200} = \overline{5 \cdot 40 + 0} = \bar{0}$. Sì. Verifichiamo $\overline{20}$: $\overline{20}^2 = \overline{400} = \overline{10 \cdot 40 + 0} = \bar{0}$. Sì.
*   **Esempio $\mathbb{Z}_{162}$ (Pag 21):** $162 = 2 \cdot 81 = 2^1 \cdot 3^4$. Gli elementi nilpotenti (oltre a $\bar{0}$) sono multipli di $2 \cdot 3 = 6$. Es. $\bar{6}, \overline{12}, \overline{18}, ...$

[[Elemento Nilpotente]]

---

## 8. Equazioni Congruenziali

Risolvere equazioni della forma $\bar{a} \cdot X = \bar{b}$ in $\mathbb{Z}_m$.

*   Equivalente a: $ax \equiv b \pmod{m}$.
*   **Teorema di Risolubilità** (Pag 24):** L'equazione congruenziale $ax \equiv b \pmod{m}$ ammette soluzione $x \in \mathbb{Z}$ se e solo se $d \mid b$, dove $d = \text{MCD}(a, m)$.
    *   Se la soluzione esiste, ci sono esattamente $d$ soluzioni distinte modulo $m$.
    *   Se $d=1$ (cioè $\bar{a}$ è invertibile in $\mathbb{Z}_m$), la soluzione è unica modulo $m$ ed è data da $x \equiv a^{-1}b \pmod{m}$.

*   **Esempio $2x \equiv 5 \pmod{10}$ (Pag 23):** $\text{MCD}(2, 10)=2$. Poiché $2 \nmid 5$, non ci sono soluzioni.
*   **Esempio $2x \equiv 6 \pmod{8}$ (Pag 23):** $\text{MCD}(2, 8)=2$. Poiché $2 \mid 6$, ci sono soluzioni (esattamente 2). Dividendo tutto per $d=2$: $x \equiv 3 \pmod{4}$. Le soluzioni sono $x \equiv 3 \pmod{8}$ e $x \equiv 3+4 = 7 \pmod{8}$. Soluzioni in $\mathbb{Z}_8$: $\{\bar{3}, \bar{7}\}$.

*   **Esempio $21x \equiv 10 \pmod{64}$ (Pag 25):**
    1.  Calcoliamo $d = \text{MCD}(21, 64)$.
        *   $64 = 3 \cdot 21 + 1$.
        *   $21 = 21 \cdot 1 + 0$.
        *   $d=1$.
    2.  Poiché $d=1$ divide $b=10$, esiste una soluzione unica modulo 64.
    3.  Dobbiamo trovare l'inverso di $21$ modulo $64$. Usiamo l'algoritmo esteso a ritroso:
        *   $1 = 64 - 3 \cdot 21$.
        *   Questa è già nella forma $ah+mk=1$ con $a=21, m=64$. Abbiamo $h=-3, k=1$.
        *   L'inverso di $\overline{21}$ in $\mathbb{Z}_{64}$ è $\bar{h} = \overline{-3}$.
        *   $\overline{-3} \equiv \overline{-3+64} = \overline{61}$. Quindi $\overline{21}^{-1} = \overline{61}$.
    4.  La soluzione è $x \equiv a^{-1}b \pmod{m}$:
        *   $x \equiv 61 \cdot 10 \pmod{64}$
        *   $x \equiv 610 \pmod{64}$.
        *   Dividiamo 610 per 64: $610 = 9 \cdot 64 + 34$. ($9 \times 64 = 576$).
        *   $x \equiv 34 \pmod{64}$.
    *   Soluzione: $X = \overline{34}$ in $\mathbb{Z}_{64}$.

[[Equazione congruenziale lineare]] [[Algoritmo di Euclide Esteso]]

---

### 8.1 Esistenza e Numero delle Soluzioni

**Guida Passo-Passo per Risolvere $ax \equiv b \pmod{m}$**

1.  **Identifica i Valori:**
    *   Scrivi chiaramente i valori di $a$, $b$ e $m$ dalla tua equazione.

2.  **Calcola il MCD:**
    *   Calcola $d = \text{gcd}(a, m)$ (il Massimo Comun Divisore tra $a$ e $m$). Puoi usare l'Algoritmo di Euclide.

3.  **Verifica l'Esistenza delle Soluzioni:**
    *   **Se $d$ non divide $b$ ($d \nmid b$):** L'equazione **non ha soluzioni**. Fermati qui.
    *   **Se $d$ divide $b$ ($d \mid b$):** L'equazione ha esattamente **$d$ soluzioni distinte modulo $m$**. Procedi al passo successivo.

4.  **Risolvi l'Equazione (se esistono soluzioni):**

    **CASO A: $d = 1$ (Soluzione Unica Modulo $m$)**
    *   L'equazione è $ax \equiv b \pmod{m}$ con $\text{gcd}(a, m) = 1$.
    *   **Passo A1: Trova l'inverso di $a$ modulo $m$.**
        *   Usa l'Algoritmo di Euclide Esteso per trovare due interi $s$ e $t$ tali che $as + mt = 1$.
        *   Da questa equazione, $as \equiv 1 \pmod{m}$. Quindi, l'inverso di $a$ modulo $m$ è $a^{-1} \equiv s \pmod{m}$.
        *   Assicurati che $s$ sia il rappresentante positivo più piccolo (tra $0$ e $m-1$). Se $s$ è negativo, aggiungi $m$ finché non diventa positivo. Se $s > m-1$, prendi il resto $s \pmod m$.
    *   **Passo A2: Calcola la soluzione.**
        *   La soluzione unica è $x \equiv a^{-1} \cdot b \pmod{m}$.
    *   **Passo A3: Riduci il risultato.**
        *   Calcola il valore di $a^{-1} \cdot b$ e poi riducilo modulo $m$ per ottenere la soluzione $x_0$ nell'intervallo $[0, m-1]$.

    **CASO B: $d > 1$ ($d$ Soluzioni Distinte Modulo $m$)**
    *   L'equazione è $ax \equiv b \pmod{m}$ con $\text{gcd}(a, m) = d > 1$ e $d \mid b$.
    *   **Passo B1: Semplifica l'equazione.**
        *   Dividi $a$, $b$ e $m$ per $d$:
            *   $a' = a/d$
            *   $b' = b/d$
            *   $m' = m/d$
        *   La nuova equazione (equivalente) è $a'x \equiv b' \pmod{m'}$.
        *   *Importante:* Ora, $\text{gcd}(a', m') = 1$.
    *   **Passo B2: Risolvi l'equazione semplificata.**
        *   Risolvi $a'x \equiv b' \pmod{m'}$ usando la procedura del **CASO A** (trova l'inverso di $a'$ modulo $m'$, moltiplica per $b'$, riduci modulo $m'$).
        *   Chiama la soluzione di questa equazione semplificata $x_0$. Quindi $x_0 \equiv (a')^{-1}b' \pmod{m'}$. Assicurati che $x_0$ sia nell'intervallo $[0, m'-1]$.
    *   **Passo B3: Trova tutte le $d$ soluzioni modulo $m$.**
        *   La prima soluzione (modulo $m$) è $x_0$.
        *   Le altre $d-1$ soluzioni si ottengono aggiungendo multipli di $m'$ a $x_0$:
            $x_1 = x_0 + m'$
            $x_2 = x_0 + 2m'$
            ...
            $x_{d-1} = x_0 + (d-1)m'$
        *   Tutte queste $d$ soluzioni ($x_0, x_1, \dots, x_{d-1}$) sono le soluzioni distinte modulo $m$ dell'equazione originale.

5.  **Verifica (Opzionale ma Consigliato):**
    *   Sostituisci ciascuna delle soluzioni trovate nell'equazione originale $ax \equiv b \pmod{m}$ per assicurarti che la congruenza sia soddisfatta.

---

## 9. Esercizi Assegnati (Pag 26 e Foto)

> [!EXERCISE] Esercizio 1 (Pag 26)
> Determinare gli elementi invertibili, i divisori dello zero e gli elementi nilpotenti di $\mathbb{Z}_{40}$.
> *Suggerimento: $40 = 2^3 \cdot 5$. Usare le proposizioni basate su $\text{MCD}(a, 40)$ e sulla fattorizzazione.*

> [!EXERCISE] Esercizio 2 (Pag 26)
> Determinare l'inverso di $\bar{25}$ in $\mathbb{Z}_{192}$.
> *Suggerimento: Calcolare $\text{MCD}(25, 192)$ con l'algoritmo di Euclide. Se è 1, usare l'algoritmo esteso a ritroso per trovare l'identità di Bézout $25h + 192k = 1$. L'inverso sarà $\bar{h}$.*

> [!EXERCISE] Esercizio 3 (dalla Foto 1)
> Calcolare l'inverso di $\bar{16}$ in $\mathbb{Z}_{125}$.
> *Suggerimento: Calcolare $\text{MCD}(16, 125)$ e usare l'algoritmo esteso.*

> [!EXERCISE] Esercizio 4 (dalla Foto 1)
> Calcolare l'inverso di $\bar{17}$ in $\mathbb{Z}_{42}$.
> *Suggerimento: Calcolare $\text{MCD}(17, 42)$ e usare l'algoritmo esteso.*

---

> [!SUMMARY] Riepilogo Veloce Lezione 13
> *   Abbiamo definito la **congruenza modulo m** e visto la sua compatibilità con somma e prodotto.
> *   Abbiamo costruito l'**anello quoziente** $(\mathbb{Z}_m, +, \cdot)$ delle classi di resto.
> *   Abbiamo visto che $\mathbb{Z}_m$ è un **campo** $\iff m$ è primo.
> *   Abbiamo determinato la **caratteristica** di $\mathbb{Z}_m$.
> *   Abbiamo caratterizzato gli elementi **invertibili** ($\text{MCD}(a,m)=1$) e i **divisori dello zero** ($\text{MCD}(a,m)>1$) in $\mathbb{Z}_m$.
> *   Abbiamo introdotto gli elementi **nilpotenti** in $\mathbb{Z}_m$.
> *   Abbiamo studiato le **equazioni congruenziali** $ax \equiv b \pmod{m}$ e il teorema sulla loro risolubilità.

> [!TIP] Prossimi Passi
> *   Fai pratica con l'algoritmo di Euclide esteso per trovare gli inversi in $\mathbb{Z}_m$.
> *   Risolvi gli esercizi assegnati su $\mathbb{Z}_{40}$ e $\mathbb{Z}_{192}$.
> *   Potremmo approfondire le proprietà degli omomorfismi di anelli o iniziare a studiare i sottogruppi e le loro proprietà.