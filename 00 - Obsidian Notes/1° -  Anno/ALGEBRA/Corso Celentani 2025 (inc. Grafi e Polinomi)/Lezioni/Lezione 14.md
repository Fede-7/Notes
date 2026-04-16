# Lezione 14: Anelli $\mathbb{Z}_m$, Criteri di Divisibilità, Equazioni Congruenziali

**Data:** 09/05/2025 (come da note).
**Argomenti:** Proprietà di $\mathbb{Z}_m$ (divisori dello zero, invertibili, nilpotenti, idempotenti), Criteri di divisibilità (via aritmetica modulare), Equazioni congruenziali lineari.

#tag/number-theory #tag/modular-arithmetic #tag/zn-rings #tag/congruences #tag/algebra-avanzata

---

## 1. Proprietà dell'Anello delle Classi di Resto $(\mathbb{Z}_m, +, \cdot)$

Ricordiamo che $(\mathbb{Z}_m, +, \cdot)$ è un **anello commutativo unitario**. L'unità è $\bar{1}$ (se $m>1$).
Lo zero è $\bar{0}$.

*   **1. Divisori dello Zero in $\mathbb{Z}_m$ (Pag 1):**
    *   Un elemento $\bar{a} \in \mathbb{Z}_m$, con $\bar{a} \neq \bar{0}$, è un **divisore dello zero** se e solo se $\text{MCD}(a, m) \neq 1$.
    *   **Spiegazione:** Se $d = \text{MCD}(a, m) \neq 1$, allora $a = d \cdot a'$ e $m = d \cdot m'$ con $m' < m$. Consideriamo $\bar{b} = \overline{m'}$. Poiché $m'<m$, $\overline{m'} \neq \bar{0}$.
        *   $\bar{a} \cdot \overline{m'} = \overline{a \cdot m'} = \overline{(d \cdot a') \cdot m'} = \overline{a' \cdot (d \cdot m')} = \overline{a' \cdot m} = \bar{0}$.
        *   Poiché $\bar{a} \neq \bar{0}$ e $\overline{m'} \neq \bar{0}$ ma il loro prodotto è $\bar{0}$, $\bar{a}$ è divisore dello zero.
    *   Viceversa, se $\bar{a}$ è divisore dello zero, esiste $\bar{b} \neq \bar{0}$ tale che $\bar{a}\bar{b} = \bar{0}$, cioè $m \mid ab$. Se $\text{MCD}(a,m)=1$, allora $m \mid b$, il che implica $\bar{b}=\bar{0}$, contraddizione. Quindi $\text{MCD}(a,m) \neq 1$.

*   **2. Elementi Invertibili in $\mathbb{Z}_m$ (Pag 1):**
    *   Un elemento $\bar{a} \in \mathbb{Z}_m$ è **invertibile** (o simmetrizzabile rispetto al prodotto) se e solo se $\text{MCD}(a, m) = 1$.
    *   L'insieme degli elementi invertibili è $U(\mathbb{Z}_m) = \{ \bar{a} \in \mathbb{Z}_m \mid \text{MCD}(a, m) = 1 \}$.
    *   $(U(\mathbb{Z}_m), \cdot)$ è un gruppo abeliano (gruppo moltiplicativo degli invertibili).
    *   Il numero di elementi invertibili è $\phi(m)$ (Funzione toziente di Eulero).

*   **Corollario: $\mathbb{Z}_p$ è un Campo (Pag 1):**
    *   Se $p$ è un numero **primo**, allora per ogni $\bar{a} \in \mathbb{Z}_p$ con $\bar{a} \neq \bar{0}$ (cioè $p \nmid a$), si ha $\text{MCD}(a, p) = 1$.
    *   Quindi, tutti gli elementi non nulli di $\mathbb{Z}_p$ sono invertibili.
    *   Poiché $(\mathbb{Z}_p, +, \cdot)$ è un anello commutativo unitario in cui ogni elemento non nullo è invertibile, **$\mathbb{Z}_p$ è un campo per ogni $p$ primo.**

*   **3. Elementi Nilpotenti in $\mathbb{Z}_m$ (Pag 1):**
    *   Sia $m = p_1^{\alpha_1} p_2^{\alpha_2} \dots p_k^{\alpha_k}$ la fattorizzazione in primi distinti di $m$.
    *   Un elemento $\bar{a} \in \mathbb{Z}_m$ è **nilpotente** se e solo se $a$ è un multiplo di $rad(m) = p_1 p_2 \dots p_k$ (il radicale di $m$).
    *   Cioè, $\bar{a}$ è nilpotente $\iff p_i \mid a$ per ogni fattore primo $p_i$ di $m$.
    *   **Spiegazione:** Se $\bar{a}^N = \bar{0}$ per qualche $N \ge 1$, allora $m \mid a^N$. Questo implica che ogni fattore primo $p_i$ di $m$ deve dividere $a^N$, e quindi $p_i$ deve dividere $a$. Viceversa, se ogni $p_i$ divide $a$, allora $rad(m) \mid a$. Sia $N = \max(\alpha_i)$. Allora $(rad(m))^N$ sarà divisibile per $m$, e quindi $a^N$ sarà divisibile per $m$, da cui $\bar{a}^N = \bar{0}$.

*   **4. Elementi Idempotenti in $\mathbb{Z}_m$ (Pag 2):**
    *   Un elemento $\bar{a} \in \mathbb{Z}_m$ è **idempotente** se $\bar{a}^2 = \bar{a}$.
    *   Questo è equivalente a $a^2 \equiv a \pmod{m}$, cioè $m \mid (a^2 - a)$, ovvero $m \mid a(a-1)$.
    *   Sempre $\bar{0}$ e $\bar{1}$ sono idempotenti.
    *   **Esempio in $\mathbb{Z}_{10}$:**
        *   $\bar{0}^2 = \bar{0}$.
        *   $\bar{1}^2 = \bar{1}$.
        *   $\bar{5}^2 = \overline{25} = \bar{5}$ (poiché $25 \equiv 5 \pmod{10}$).
        *   $\bar{6}^2 = \overline{36} = \bar{6}$ (poiché $36 \equiv 6 \pmod{10}$).
        *   Idempotenti in $\mathbb{Z}_{10}$: $\{\bar{0}, \bar{1}, \bar{5}, \bar{6}\}$.

[[Anello Zm]] [[Divisori dello zero in Zm]] [[Elementi invertibili in Zm]] [[Campo Zp]] [[Elemento nilpotente]] [[Elemento idempotente]]

---

## 2. Esercizi su $\mathbb{Z}_m$ (Pag 2-3)

> [!EXERCISE] Esercizio (Pag 2)
> Determinare (se possibile) un $m \in \mathbb{N}, m > 1$ tale che $\mathbb{Z}_m$ soddisfi le seguenti condizioni:
>
> *   i) $\mathbb{Z}_m$ possiede esattamente 8 elementi invertibili e 6 divisori dello zero.
> *   ii) $\mathbb{Z}_m$ possiede esattamente 8 divisori dello zero e 6 elementi invertibili.
>
> *Suggerimenti:*
> * Il numero totale di elementi in $\mathbb{Z}_m$ è $m$.
> * Gli elementi di $\mathbb{Z}_m$ sono o invertibili, o divisori dello zero, oppure $\bar{0}$ (che non è invertibile e, per definizione, non è divisore dello zero se $m>1$).
> * Numero invertibili = $\phi(m)$.
> * Numero divisori dello zero = $m - \phi(m) - 1$ (per $m>1$).
>
> *Per i):*
> * $\phi(m) = 8$.
> * $m - \phi(m) - 1 = 6 \implies m - 8 - 1 = 6 \implies m - 9 = 6 \implies m = 15$.
> * Verifichiamo $\phi(15)$: $15 = 3 \cdot 5$. $\phi(15) = \phi(3)\phi(5) = (3-1)(5-1) = 2 \cdot 4 = 8$. Corrisponde!
> * Quindi $m=15$ è una soluzione per (i).
> * Divisori dello zero in $\mathbb{Z}_{15}$: elementi $\bar{a}$ tali che $\text{MCD}(a, 15) \neq 1$. I numeri coprimi con 15 (da 1 a 14) sono: 1, 2, 4, 7, 8, 11, 13, 14 (sono 8, come $\phi(15)$). I restanti (escluso 0) sono i divisori dello zero: 3, 5, 6, 9, 10, 12 (sono 6).
>
> *Per ii):*
> * Numero divisori dello zero = $8$.
> * Numero invertibili = $\phi(m) = 6$.
> * $m - \phi(m) - 1 = 8 \implies m - 6 - 1 = 8 \implies m - 7 = 8 \implies m = 15$.
> * Ma questo richiederebbe $\phi(15)=6$, mentre sappiamo che $\phi(15)=8$. C'è una contraddizione.
> * Quindi **non è possibile** trovare un tale $m$ per (ii).

*   **Tabella per $\mathbb{Z}_{15}$ (Pag 3):**
    *   **Divisori dello Zero:** $\bar{3}, \bar{5}, \bar{6}, \bar{9}, \overline{10}, \overline{12}$ (6 elementi)
    *   **Elementi Invertibili:** $\bar{1}, \bar{2}, \bar{4}, \bar{7}, \bar{8}, \overline{11}, \overline{13}, \overline{14}$ (8 elementi)

---

## 3. Criteri di Divisibilità (via Aritmetica Modulare)

Possiamo usare le congruenze per derivare i criteri di divisibilità. L'idea fondamentale è che un numero intero $n$ è divisibile per un modulo $m$ se e solo se il resto della divisione di $n$ per $m$ è $0$. In termini di aritmetica modulare, questo si scrive come:
$$ n \equiv 0 \pmod{m} $$

Consideriamo un numero intero positivo $n$ scritto in base 10 con cifre $c_k, c_{k-1}, \dots, c_1, c_0$. Questo significa che:
$$ n = c_k \cdot 10^k + c_{k-1} \cdot 10^{k-1} + \dots + c_1 \cdot 10^1 + c_0 \cdot 10^0 $$
(Qui $c_0$ è la cifra delle unità, $c_1$ quella delle decine, $c_2$ quella delle centinaia, e così via. Il pedice $i$ in $c_i$ e $10^i$ indica la posizione della cifra, partendo da $0$ per le unità).

Per verificare se $n$ è divisibile per $m$, calcoliamo $n$ modulo $m$. Usando le proprietà delle congruenze (la congruenza rispetta somma e prodotto), possiamo calcolare ogni termine separatamente:
$$ n \equiv (c_k \cdot 10^k + c_{k-1} \cdot 10^{k-1} + \dots + c_1 \cdot 10^1 + c_0 \cdot 10^0) \pmod{m} $$
$$ n \equiv (c_k \cdot (10^k \pmod{m}) + c_{k-1} \cdot (10^{k-1} \pmod{m}) + \dots + c_1 \cdot (10^1 \pmod{m}) + c_0 \cdot (10^0 \pmod{m})) \pmod{m} $$

Questa è la **formula generale** per calcolare il resto di un numero $n$ modulo $m$ basandosi sulle sue cifre.

**Il Criterio Generale di Divisibilità:**
Un numero $n$ è divisibile per $m$ se e solo se il risultato del calcolo:
$$ (c_k \cdot (10^k \pmod{m}) + c_{k-1} \cdot (10^{k-1} \pmod{m}) + \dots + c_1 \cdot (10^1 \pmod{m}) + c_0 \cdot (10^0 \pmod{m})) $$
è congruo a $0$ modulo $m$.

I criteri di divisibilità "classici" (per 2, 3, 5, 9, 10, 11, ecc.) sono semplicemente questa formula generale applicata a specifici valori di $m$, sfruttando il pattern dei resti di $10^i \pmod m$.

#### Criteri Derivati dalla Formula Generale:

*   **Divisibilità per $m=2, 5, 10$:**
    *   Osserviamo che $10 \equiv 0 \pmod{2}$, $10 \equiv 0 \pmod{5}$, $10 \equiv 0 \pmod{10}$.
    *   Questo implica che per $m \in \{2, 5, 10\}$, $10^i \equiv 0 \pmod{m}$ per ogni $i \geq 1$.
    *   La formula generale si semplifica notevolmente:
        $$ n \equiv (c_k \cdot 0 + c_{k-1} \cdot 0 + \dots + c_1 \cdot 0 + c_0 \cdot (10^0 \pmod{m})) \pmod{m} $$
        Poiché $10^0 = 1$ e $1 \equiv 1 \pmod{m}$ per $m>1$:
        $$ n \equiv (c_0 \cdot 1) \pmod{m} \implies n \equiv c_0 \pmod{m} $$
    *   **Criterio:** $n$ è divisibile per $m \in \{2, 5, 10\}$ se e solo se la sua ultima cifra $c_0$ è divisibile per $m$.
        *   Per 2: $c_0$ è pari.
        *   Per 5: $c_0$ è 0 o 5.
        *   Per 10: $c_0$ è 0.

*   **Divisibilità per $m=4, 25, 100$:**
    *   Osserviamo che $100 \equiv 0 \pmod{4}$, $100 \equiv 0 \pmod{25}$, $100 \equiv 0 \pmod{100}$.
    *   Questo implica che per $m \in \{4, 25, 100\}$, $10^i \equiv 0 \pmod{m}$ per ogni $i \geq 2$.
    *   La formula generale diventa:
        $$ n \equiv (c_k \cdot 0 + \dots + c_2 \cdot 0 + c_1 \cdot (10^1 \pmod{m}) + c_0 \cdot (10^0 \pmod{m})) \pmod{m} $$
        $$ n \equiv (c_1 \cdot 10 + c_0 \cdot 1) \pmod{m} $$
        $$ n \equiv (10c_1 + c_0) \pmod{m} $$
    *   **Criterio:** $n$ è divisibile per $m \in \{4, 25, 100\}$ se e solo se il numero formato dalle sue ultime due cifre ($10c_1+c_0$) è divisibile per $m$.
        *   Per 4: le ultime due cifre formano un numero divisibile per 4.
        *   Per 25: le ultime due cifre formano un numero divisibile per 25 (00, 25, 50, 75).
        *   Per 100: le ultime due cifre sono 00.

*   **Divisibilità per $m=3, 9$:**
    *   Osserviamo che $10 \equiv 1 \pmod{3}$ e $10 \equiv 1 \pmod{9}$.
    *   Questo implica che per $m \in \{3, 9\}$, $10^i \equiv 1^i \equiv 1 \pmod{m}$ per ogni $i \geq 0$.
    *   La formula generale diventa:
        $$ n \equiv (c_k \cdot 1 + c_{k-1} \cdot 1 + \dots + c_1 \cdot 1 + c_0 \cdot 1) \pmod{m} $$
        $$ n \equiv (c_k + c_{k-1} + \dots + c_1 + c_0) \pmod{m} $$
    *   **Criterio:** $n$ è divisibile per $m \in \{3, 9\}$ se e solo se la somma delle sue cifre è divisibile per $m$.

*   **Divisibilità per $m=11$:**
    *   Osserviamo che $10 \equiv -1 \pmod{11}$.
    *   Questo implica che per $m=11$, $10^i \equiv (-1)^i \pmod{11}$ per ogni $i \geq 0$.
    *   La formula generale diventa:
        $$ n \equiv (c_k \cdot (-1)^k + c_{k-1} \cdot (-1)^{k-1} + \dots + c_1 \cdot (-1)^1 + c_0 \cdot (-1)^0) \pmod{11} $$
        $$ n \equiv (c_0 - c_1 + c_2 - c_3 + \dots + (-1)^k c_k) \pmod{11} $$
    *   **Criterio:** $n$ è divisibile per $11$ se e solo se la somma a segni alterni delle sue cifre (partendo dalla cifra delle unità $c_0$ con segno positivo) è divisibile per $11$.

---

### Esempio Semplice: Verificare se 258 è divisibile per 3 (usando la formula generale)

Prendiamo il numero $n = 258$ e il modulo $m = 3$.

**Passo 1: Identificare le cifre e le loro posizioni.**
Il numero $258$ ha 3 cifre:
- $c_0 = 8$ (posizione 0, unità)
- $c_1 = 5$ (posizione 1, decine)
- $c_2 = 2$ (posizione 2, centinaia)
La posizione più alta è $k=2$.

**Passo 2: Scrivere il numero in forma polinomiale e impostare la congruenza modulo $m$.**
$$ n = 2 \cdot 10^2 + 5 \cdot 10^1 + 8 \cdot 10^0 $$
Vogliamo calcolare $n \pmod{3}$:
$$ 258 \equiv (2 \cdot 10^2 + 5 \cdot 10^1 + 8 \cdot 10^0) \pmod{3} $$

**Passo 3: Calcolare i resti delle potenze di 10 modulo $m$ (cioè modulo 3).**
- $10^0 \pmod{3}$: $10^0 = 1$. $1 \equiv 1 \pmod{3}$.
- $10^1 \pmod{3}$: $10^1 = 10$. $10 = 3 \cdot 3 + 1$, quindi $10 \equiv 1 \pmod{3}$.
- $10^2 \pmod{3}$: $10^2 = 100$. $100 = 3 \cdot 33 + 1$, quindi $100 \equiv 1 \pmod{3}$.
In generale, per $m=3$, $10^i \equiv 1 \pmod{3}$ per ogni $i \geq 0$.

**Passo 4: Sostituire i resti trovati nella formula generale.**
Usiamo la formula: $n \equiv (c_k \cdot (10^k \pmod{m}) + \dots + c_0 \cdot (10^0 \pmod{m})) \pmod{m}$.
Nel nostro caso ($n=258, m=3$, $k=2$):
$$ 258 \equiv (c_2 \cdot (10^2 \pmod{3}) + c_1 \cdot (10^1 \pmod{3}) + c_0 \cdot (10^0 \pmod{3})) \pmod{3} $$
Sostituiamo i valori delle cifre ($c_2=2, c_1=5, c_0=8$) e i resti delle potenze di 10 (tutti 1):
$$ 258 \equiv (2 \cdot \mathbf{1} + 5 \cdot \mathbf{1} + 8 \cdot \mathbf{1}) \pmod{3} $$

**Passo 5: Eseguire i calcoli.**
$$ 258 \equiv (2 + 5 + 8) \pmod{3} $$
Sommiamo i numeri: $2 + 5 + 8 = 15$.
$$ 258 \equiv 15 \pmod{3} $$

**Passo 6: Verificare se il risultato finale è congruo a 0 modulo $m$.**
Dobbiamo vedere se $15 \equiv 0 \pmod{3}$.
$15 \div 3 = 5$ con resto $0$.
Sì, $15 \equiv 0 \pmod{3}$.

**Passo 7: Concludere.**
Poiché $258 \equiv 15 \pmod{3}$ e $15 \equiv 0 \pmod{3}$, per la proprietà transitiva della congruenza, $258 \equiv 0 \pmod{3}$.
Questo significa che 258 è divisibile per 3.

Questo approccio formale mostra che il "trucco" della somma delle cifre per la divisibilità per 3 (o 9) non è magico, ma deriva direttamente dal fatto che le potenze di 10 hanno resto 1 quando divise per 3 (o 9).

[[Criteri di divisibilità]] [[Aritmetica modulare]]

---

## 4. Equazioni Congruenziali Lineari

Si tratta di equazioni della forma $ax \equiv b \pmod{m}$.
Cercare le soluzioni per $x$ significa trovare le classi di resto $\bar{x} \in \mathbb{Z}_m$ tali che $[a]_m [x]_m = [b]_m$.

> [!TEOREM] Esistenza e Numero di Soluzioni per $ax \equiv b \pmod{m}$
> Sia data l'equazione congruenziale lineare:
> $$ ax \equiv b \pmod{m} $$
> dove $a, b$ sono interi e $m$ è un intero positivo ($m > 1$). Sia $d = \text{MCD}(a, m)$.
>
> Allora:
>
> 1.  **Esistenza delle Soluzioni:** L'equazione $ax \equiv b \pmod{m}$ ammette soluzione se e solo se $d$ divide $b$ (scritto $d \mid b$).
> 2.  **Numero delle Soluzioni:** Se $d \mid b$ (cioè se le soluzioni esistono), allora l'equazione ammette esattamente $d$ soluzioni distinte modulo $m$.
>
> **In parole semplici:**
>
> Questo teorema ci dice due cose cruciali prima ancora di iniziare a risolvere l'equazione:
>
> *   **Prima cosa da controllare:** Calcola il Massimo Comun Divisore (MCD) tra il coefficiente della $x$ ($a$) e il modulo ($m$). Chiamiamo questo MCD "$d$". Se questo $d$ *non* divide il termine noto ($b$), allora non c'è nessuna soluzione. Puoi smettere subito!
> *   **Se invece $d$ divide $b$:** Allora sai per certo che le soluzioni esistono. E non solo, sai anche *quante* ce ne sono: ce ne sono esattamente $d$ soluzioni distinte se le consideriamo modulo $m$.
>
> Questo teorema ti dice subito se vale la pena cercare soluzioni e quante te ne devi aspettare.

*   **Procedimento Risolutivo (Pag 10-14):**
    1.  Sia $d = \text{MCD}(a, m)$. Se $d \nmid b$, non ci sono soluzioni.
    2.  Se $d \mid b$, dividiamo tutto per $d$:
        *   $a = a_1 d$, $m = m_1 d$, $b = b_1 d$.
        *   L'equazione $ax \equiv b \pmod{m}$ (*) è equivalente a $a_1 d x \equiv b_1 d \pmod{m_1 d}$.
        *   Che si semplifica a $a_1 x \equiv b_1 \pmod{m_1}$ (**).
        *   Importante: $\text{MCD}(a_1, m_1) = \text{MCD}(a/d, m/d) = \text{MCD}(a,m)/d = d/d = 1$.
    3.  Ora dobbiamo risolvere $a_1 x \equiv b_1 \pmod{m_1}$, con $\text{MCD}(a_1, m_1)=1$.
        *   Questo significa che $\overline{a_1}$ è invertibile in $\mathbb{Z}_{m_1}$. Troviamo l'inverso $[\overline{a_1}]^{-1}_{m_1} = [\overline{c_1}]_{m_1}$.
        *   Possiamo trovare $c_1$ risolvendo $a_1 x \equiv 1 \pmod{m_1}$ (***) usando l'algoritmo di Euclide esteso per l'identità di Bézout.
    4.  Moltiplichiamo (**) per $c_1$: $c_1 a_1 x \equiv c_1 b_1 \pmod{m_1}$.
        *   Poiché $c_1 a_1 \equiv 1 \pmod{m_1}$, otteniamo $1 \cdot x \equiv c_1 b_1 \pmod{m_1}$.
        *   Quindi $x \equiv c_1 b_1 \pmod{m_1}$. Sia $c = c_1 b_1 \pmod{m_1}$.
        *   La soluzione generale per (**) è $x = c + h \cdot m_1$ per $h \in \mathbb{Z}$.
    5.  Le soluzioni distinte modulo $m$ per l'equazione originale (*) sono:
        *   $x_0 = c$
        *   $x_1 = c + m_1$
        *   $x_2 = c + 2m_1$
        *   ...
        *   $x_{d-1} = c + (d-1)m_1$
        *   Sono $d$ soluzioni: $[c]_{m_1} = [c]_m \cup [c+m_1]_m \cup \dots \cup [c+(d-1)m_1]_m$.

*   **Esempio (Pag 11-12):** $10x \equiv 8 \pmod{14}$ (*)
    1.  $a=10, b=8, m=14$. $d = \text{MCD}(10, 14) = 2$.
    2.  $d=2 \mid b=8$. Ci sono $d=2$ soluzioni.
    3.  Dividiamo per $d=2$: $5x \equiv 4 \pmod{7}$ (**). ($a_1=5, b_1=4, m_1=7$). $\text{MCD}(5, 7)=1$.
    4.  Risolviamo $5x \equiv 1 \pmod{7}$ (***) per trovare l'inverso di 5 mod 7.
        *   $7 = 5 \cdot 1 + 2$
        *   $5 = 2 \cdot 2 + 1 \implies 1 = 5 - 2 \cdot 2$
        *   $1 = 5 - 2 \cdot (7 - 5 \cdot 1) = 5 - 2 \cdot 7 + 2 \cdot 5 = 3 \cdot 5 - 2 \cdot 7$.
        *   Quindi $3 \cdot 5 - 2 \cdot 7 = 1 \implies 3 \cdot 5 \equiv 1 \pmod{7}$. L'inverso di $\bar{5}$ è $\bar{3}$ in $\mathbb{Z}_7$. $c_1=3$.
    5.  Moltiplichiamo (**) per $c_1=3$: $3 \cdot 5x \equiv 3 \cdot 4 \pmod{7} \implies x \equiv 12 \pmod{7} \implies x \equiv 5 \pmod{7}$.
        *   $c=5$. La soluzione generale di (**) è $x = 5 + h \cdot 7$.
    6.  Le $d=2$ soluzioni modulo $m=14$ sono:
        *   $x_0 = c = 5$. Sol: $\bar{5}_{14}$.
        *   $x_1 = c + m_1 = 5 + 7 = 12$. Sol: $\overline{12}_{14}$.
        *   Soluzioni: $[5]_{14}, [12]_{14}$.

[[Equazione congruenziale lineare]] [[Algoritmo di Euclide Esteso]]

---

## 5. Esercizi Proposti (Pag 15-21)

> [!EXERCISE] Esercizio 1 (Pag 15)
> Risolvere $135x \equiv 10 \pmod{192}$.
> *  $d = \text{MCD}(135, 192)$. $192 = 135 \cdot 1 + 57$; $135 = 57 \cdot 2 + 21$; $57 = 21 \cdot 2 + 15$; $21 = 15 \cdot 1 + 6$; $15 = 6 \cdot 2 + 3$; $6 = 3 \cdot 2 + 0$. $d=3$.
> *  $b=10$. $d=3 \nmid b=10$. **Nessuna soluzione.**

> [!EXERCISE] Esercizio 2 (Pag 16-18)
> Risolvere $135x \equiv 12 \pmod{192}$ (*).
> *  $a=135, b=12, m=192$. $d = \text{MCD}(135, 192) = 3$.
> *  $d=3 \mid b=12$. Esistono $d=3$ soluzioni.
> *  Dividiamo per $d=3$: $45x \equiv 4 \pmod{64}$ (**). ($a_1=45, b_1=4, m_1=64$). $\text{MCD}(45, 64)=1$.
> *  Risolviamo $45x \equiv 1 \pmod{64}$ (***) per l'inverso di 45 mod 64.
>     *   $64 = 45 \cdot 1 + 19 \implies 19 = 64 - 45$
>     *   $45 = 19 \cdot 2 + 7 \implies 7 = 45 - 2 \cdot 19$
>     *   $19 = 7 \cdot 2 + 5 \implies 5 = 19 - 2 \cdot 7$
>     *   $7 = 5 \cdot 1 + 2 \implies 2 = 7 - 1 \cdot 5$
>     *   $5 = 2 \cdot 2 + 1 \implies 1 = 5 - 2 \cdot 2$
>     *   $1 = 5 - 2(7-5) = 3 \cdot 5 - 2 \cdot 7$
>     *   $1 = 3(19-2 \cdot 7) - 2 \cdot 7 = 3 \cdot 19 - 6 \cdot 7 - 2 \cdot 7 = 3 \cdot 19 - 8 \cdot 7$
>     *   $1 = 3 \cdot 19 - 8(45 - 2 \cdot 19) = 3 \cdot 19 - 8 \cdot 45 + 16 \cdot 19 = 19 \cdot 19 - 8 \cdot 45$
>     *   $1 = 19(64 - 45) - 8 \cdot 45 = 19 \cdot 64 - 19 \cdot 45 - 8 \cdot 45 = 19 \cdot 64 - 27 \cdot 45$.
>     *   Quindi $-27 \cdot 45 \equiv 1 \pmod{64}$. L'inverso $c_1 = -27 \equiv -27+64 \equiv 37 \pmod{64}$.
> *  Moltiplichiamo (**) per $c_1=37$: $x \equiv 37 \cdot 4 \pmod{64}$.
>     *   $37 \cdot 4 = 148$. $148 = 2 \cdot 64 + 20$. Quindi $148 \equiv 20 \pmod{64}$.
>     *   $c=20$. Soluzione generale di (**): $x = 20 + h \cdot 64$.
> *  Le $d=3$ soluzioni modulo $m=192$ sono:
>     *   $x_0 = 20$.
>     *   $x_1 = 20 + 64 = 84$.
>     *   $x_2 = 20 + 2 \cdot 64 = 20 + 128 = 148$.
>     *   Soluzioni: $[20]_{192}, [84]_{192}, [148]_{192}$.

> [!EXERCISE] Esercizio 3 (Pag 19-20)
> Risolvere $39x \equiv b \pmod{90}$ per $b \in \{10, 15, 17\}$.
> *  $a=39, m=90$. $d = \text{MCD}(39, 90)$. $90 = 39 \cdot 2 + 12$; $39 = 12 \cdot 3 + 3$; $12 = 3 \cdot 4 + 0$. $d=3$.
> *  Caso $b=10$: $d=3 \nmid b=10$. **Nessuna soluzione.**
> *  Caso $b=17$: $d=3 \nmid b=17$. **Nessuna soluzione.**
> *  Caso $b=15$: $d=3 \mid b=15$. Esistono $d=3$ soluzioni.
>     *   Dividiamo $39x \equiv 15 \pmod{90}$ (*) per $d=3$: $13x \equiv 5 \pmod{30}$ (**). ($a_1=13, b_1=5, m_1=30$).
>     *   Risolviamo $13x \equiv 1 \pmod{30}$ (***).
>         *   $30 = 13 \cdot 2 + 4 \implies 4 = 30 - 2 \cdot 13$
>         *   $13 = 4 \cdot 3 + 1 \implies 1 = 13 - 3 \cdot 4$
>         *   $1 = 13 - 3(30 - 2 \cdot 13) = 13 - 3 \cdot 30 + 6 \cdot 13 = 7 \cdot 13 - 3 \cdot 30$.
>         *   $7 \cdot 13 \equiv 1 \pmod{30}$. Inverso $c_1=7$.
>     *   Moltiplichiamo (**) per $c_1=7$: $x \equiv 7 \cdot 5 \pmod{30} \implies x \equiv 35 \pmod{30} \implies x \equiv 5 \pmod{30}$.
>     *   $c=5$. Soluzione generale di (**): $x = 5 + h \cdot 30$.
>     *   Le $d=3$ soluzioni modulo $m=90$ sono:
>         *   $x_0 = 5$.
>         *   $x_1 = 5 + 30 = 35$.
>         *   $x_2 = 5 + 2 \cdot 30 = 65$.
>         *   Soluzioni per $b=15$: $[5]_{90}, [35]_{90}, [65]_{90}$.

> [!EXERCISE] Esercizio 4 (Pag 21-23)
> In $\mathbb{Z}_{100}$, con operazione $a * b = \overline{7}ab + \overline{25}(a+b)$, determinare gli $a \in \mathbb{Z}_{100}$ tali che $a * \bar{4} = \bar{4}$.
> *  $a * \bar{4} = \overline{7}a\bar{4} + \overline{25}(a+\bar{4}) = \overline{28}a + \overline{25}a + \overline{100} = \overline{53}a + \bar{0} = \overline{53}a$.
> *  Vogliamo $\overline{53}a = \bar{4}$, cioè $53a \equiv 4 \pmod{100}$ (*).
> *  $d = \text{MCD}(53, 100)$. $100 = 53 \cdot 1 + 47$; $53 = 47 \cdot 1 + 6$; $47 = 6 \cdot 7 + 5$; $6 = 5 \cdot 1 + 1$. $d=1$.
> *  Poiché $d=1 \mid b=4$, esiste $d=1$ soluzione.
> *  Risolviamo $53x \equiv 1 \pmod{100}$ (***).
>     *   $1 = 6 - 5 = 6 - (47 - 7 \cdot 6) = 8 \cdot 6 - 47$
>     *   $1 = 8(53 - 47) - 47 = 8 \cdot 53 - 8 \cdot 47 - 47 = 8 \cdot 53 - 9 \cdot 47$
>     *   $1 = 8 \cdot 53 - 9(100 - 53) = 8 \cdot 53 - 9 \cdot 100 + 9 \cdot 53 = 17 \cdot 53 - 9 \cdot 100$.
>     *   $17 \cdot 53 \equiv 1 \pmod{100}$. Inverso $c_1=17$.
> *  Moltiplichiamo (*) per $c_1=17$: $a \equiv 17 \cdot 4 \pmod{100} \implies a \equiv 68 \pmod{100}$.
> *  Soluzione: $a = \overline{68}$.

> [!EXERCISE] Esercizio 5 (Pag 24-26)
> In $(\mathbb{Z}_{50}, *)$ con $a * b = \overline{3}ab$.
> *   Determinare l'elemento neutro $u$.
> *   Determinare $U(\mathbb{Z}_{50})$ rispetto a $*$.
> *   Determinare l'inverso di $\bar{8}$ e $\bar{9}$ (se esistono).
>
> *Elemento Neutro $u$:*
> * $a * u = a \implies \overline{3}au = a$. Questa deve valere per ogni $a \in \mathbb{Z}_{50}$.
> * Se $a=\bar{1}$, $\overline{3}u = \bar{1} \implies 3u \equiv 1 \pmod{50}$.
> * Risolviamo $3x \equiv 1 \pmod{50}$. $\text{MCD}(3, 50)=1$.
>   $50 = 3 \cdot 16 + 2 \implies 2 = 50 - 16 \cdot 3$.
>   $3 = 2 \cdot 1 + 1 \implies 1 = 3 - 1 \cdot 2$.
>   $1 = 3 - (50 - 16 \cdot 3) = 3 - 50 + 16 \cdot 3 = 17 \cdot 3 - 1 \cdot 50$.
>   $17 \cdot 3 \equiv 1 \pmod{50}$. Quindi $x=\overline{17}$.
> *   L'elemento neutro è $u = \overline{17}$.
>
> *Elementi Invertibili $U(\mathbb{Z}_{50}, \cdot)$*:
> * $\bar{a}$ è invertibile se esiste $\bar{a}'$ tale che $\bar{a} * \bar{a}' = u = \overline{17}$.
> * $\overline{3}a a' = \overline{17} \implies 3aa' \equiv 17 \pmod{50}$.
> * Questa equazione ha soluzione per $a'$ se $\text{MCD}(3a, 50) \mid 17$.
> * Poiché 17 è primo, $\text{MCD}(3a, 50)$ deve essere 1.
> * Affinché $\text{MCD}(3a, 50)=1$, $a$ non deve essere multiplo di 2 né di 5 (i fattori di 50), e $3a$ non deve essere multiplo di 2 né di 5. Dato che 3 non è mult. di 2 né 5, basta che $a$ non sia mult. di 2 né 5.
> * Quindi $\bar{a}$ è invertibile $\iff \text{MCD}(a, 50)=1$. (Questi sono gli invertibili di $\mathbb{Z}_{50}$ rispetto al prodotto standard).
> * $U(\mathbb{Z}_{50}, *) = U(\mathbb{Z}_{50}, \cdot) = \{ \bar{a} \mid \text{MCD}(a, 50)=1 \}$.
>
> *Inverso di $\bar{8}$:*
> * $\text{MCD}(8, 50) = 2 \neq 1$. $\bar{8}$ non è invertibile rispetto al prodotto standard, quindi non sarà invertibile neanche qui. Non esiste.
>
> *Inverso di $\bar{9}$ ($c$):*
> * $\text{MCD}(9, 50)=1$. Esiste. Vogliamo $\bar{9} * \bar{c} = \overline{17} \implies \overline{3 \cdot 9 \cdot c} = \overline{17} \implies \overline{27}c = \overline{17}$.
> * $27c \equiv 17 \pmod{50}$. $d=\text{MCD}(27, 50)=1$. Esiste soluzione unica.
> * Risolviamo $27x \equiv 1 \pmod{50}$.
>   $50 = 27 \cdot 1 + 23 \implies 23 = 50 - 27$
>   $27 = 23 \cdot 1 + 4 \implies 4 = 27 - 23$
>   $23 = 4 \cdot 5 + 3 \implies 3 = 23 - 5 \cdot 4$
>   $4 = 3 \cdot 1 + 1 \implies 1 = 4 - 1 \cdot 3$
>   $1 = 4 - (23 - 5 \cdot 4) = 6 \cdot 4 - 23$
>   $1 = 6(27 - 23) - 23 = 6 \cdot 27 - 6 \cdot 23 - 23 = 6 \cdot 27 - 7 \cdot 23$
>   $1 = 6 \cdot 27 - 7(50 - 27) = 6 \cdot 27 - 7 \cdot 50 + 7 \cdot 27 = 13 \cdot 27 - 7 \cdot 50$.
>   $13 \cdot 27 \equiv 1 \pmod{50}$. Inverso di $\overline{27}$ è $\overline{13}$.
> *  $c \equiv 13 \cdot 17 \pmod{50}$. $13 \cdot 17 = 221$.
>   $221 = 4 \cdot 50 + 21$. $221 \equiv 21 \pmod{50}$.
> *  L'inverso di $\bar{9}$ è $\bar{c} = \overline{21}$.

> [!EXERCISE] Esercizio 6 (Pag 27-29)
> In $\mathbb{Z}_{10}$ con l'operazione $a \oplus b = a + \overline{6}b$.
> *   È associativa? È commutativa?
> *   Determinare elementi neutri a destra e a sinistra.
> *   Considerare i sottoinsiemi $P = \{\overline{2k} \mid k \in \mathbb{Z}\}$ (pari) e $D = \{\overline{2k+1} \mid k \in \mathbb{Z}\}$ (dispari). $(P, \oplus)$ è stabile? È un gruppo? $(D, \oplus)$ è stabile?
>
> *Associatività:*
> * $a \oplus (b \oplus c) = a \oplus (b + \overline{6}c) = a + \overline{6}(b + \overline{6}c) = a + \overline{6}b + \overline{36}c = a + \overline{6}b + \overline{6}c$.
> * $(a \oplus b) \oplus c = (a + \overline{6}b) \oplus c = (a + \overline{6}b) + \overline{6}c = a + \overline{6}b + \overline{6}c$.
> * **SÌ, è associativa.**
>
> *Commutatività:*
> * $a \oplus b = a + \overline{6}b$.
> * $b \oplus a = b + \overline{6}a$.
> * Non sono uguali in generale. Es: $\bar{1} \oplus \bar{0} = \bar{1} + \bar{0} = \bar{1}$. $\bar{0} \oplus \bar{1} = \bar{0} + \overline{6} \cdot \bar{1} = \bar{6}$.
> * **NO, non è commutativa.**
>
> *Elemento Neutro a Destra $u_R$:* $a \oplus u_R = a \implies a + \overline{6}u_R = a \implies \overline{6}u_R = \bar{0}$.
> * In $\mathbb{Z}_{10}$, $6u_R \equiv 0 \pmod{10}$. $\text{MCD}(6, 10)=2$. $2 \mid 0$. Ci sono 2 soluzioni.
> * $3u_R \equiv 0 \pmod{5}$. $\text{MCD}(3, 5)=1$. Unica soluzione $u_R \equiv 0 \pmod 5$.
> * In $\mathbb{Z}_{10}$, $u_R = \bar{0}$ o $u_R = \bar{5}$.
> * Infatti, $a \oplus \bar{0} = a + \bar{0} = a$. $a \oplus \bar{5} = a + \overline{6} \cdot \bar{5} = a + \overline{30} = a + \bar{0} = a$.
> * **Neutri a destra: $\bar{0}, \bar{5}$.**
>
> *Elemento Neutro a Sinistra $u_L$:* $u_L \oplus a = a \implies u_L + \overline{6}a = a \implies u_L = a - \overline{6}a = a(\overline{1}-\overline{6}) = a(-\overline{5}) = \overline{5}a$.
> * Questo dipende da $a$. Non esiste un $u_L$ unico. **Nessun neutro a sinistra.**
> * Di conseguenza, non c'è elemento neutro bilatero. Non è un monoide.
>
> *Stabilità di $P = \{\bar{0}, \bar{2}, \bar{4}, \bar{6}, \bar{8}\}$:*
> * Sia $a = \overline{2h}, b = \overline{2k}$ elementi di $P$.
> * $a \oplus b = \overline{2h} + \overline{6}(\overline{2k}) = \overline{2h} + \overline{12k} = \overline{2h} + \overline{2k} = \overline{2(h+k)}$. Questo è un elemento pari.
> * **SÌ, $(P, \oplus)$ è stabile.**
> * $(P, \oplus)$ è un semigruppo (associatività ereditata). Ha neutro a destra $\bar{0} \in P$ e $\bar{5} \notin P$? No, $\bar{0}$ è neutro a dx. Se $a \in P$, $a \oplus \bar{0} = a$.
> * $u_R=\bar{0}$ è in $P$. Verifichiamo se è neutro bilatero in $P$. $u_L \oplus a = a \implies u_L = \overline{5}a$. Se $a \in P$, $a$ è pari. $\overline{5} \cdot (\text{pari})$ è $\overline{0}$ o $\overline{5 \cdot \text{pari}}$. Se $a=\bar{2}$, $\overline{5}\bar{2}=\overline{10}=\bar{0}$. Se $a=\bar{4}$, $\overline{5}\bar{4}=\overline{20}=\bar{0}$. Se $a=\bar{6}$, $\overline{5}\bar{6}=\overline{30}=\bar{0}$. Se $a=\bar{8}$, $\overline{5}\bar{8}=\overline{40}=\bar{0}$. Se $a=\bar{0}$, $\overline{5}\bar{0}=\bar{0}$.
> * Quindi, per $a \in P$, $u_L = \bar{0}$ funziona come neutro a sinistra!
> * $(P, \oplus, \bar{0})$ è un monoide. È un gruppo? Inverso di $a \in P$: $a \oplus a' = \bar{0} \implies a + \overline{6}a' = \bar{0} \implies \overline{6}a' = -a$.
>   Se $a=\bar{2}$, $\overline{6}a' = -\bar{2} = \bar{8}$. $6a' \equiv 8 \pmod{10}$. $\text{MCD}(6,10)=2 \mid 8$. Soluzioni: $3a' \equiv 4 \pmod 5$. $a' \equiv 3 \cdot 4 = 12 \equiv 2 \pmod 5$. $a' = \bar{2}, \bar{7}$. Solo $\bar{2} \in P$. Inverso di $\bar{2}$ è $\bar{2}$.
>   Se $a=\bar{4}$, $\overline{6}a' = -\bar{4} = \bar{6}$. $6a' \equiv 6 \pmod{10}$. $3a' \equiv 3 \pmod 5$. $a' \equiv 1 \pmod 5$. $a' = \bar{1}, \bar{6}$. Solo $\bar{6} \in P$. Inverso di $\bar{4}$ è $\bar{6}$.
>   $(P, \oplus, \bar{0})$ è un **gruppo abeliano** (la commutatività va verificata su P, ma $a+\overline{6}b = a+b+ \overline{5}b$. $a \oplus b - b \oplus a = \overline{5}(b-a)$. Non è abeliano in generale).
>
> *Stabilità di $D$ (dispari):*
> * Sia $a = \overline{2h+1}, b = \overline{2k+1}$ elementi di $D$.
> * $a \oplus b = a + \overline{6}b = (\text{dispari}) + \overline{6}(\text{dispari}) = (\text{dispari}) + (\text{pari}) = (\text{dispari})$.
> * **SÌ, $(D, \oplus)$ è stabile.**

---

> [!SUMMARY] Riepilogo Veloce Lezione 14
> *   Abbiamo analizzato a fondo le proprietà dell'anello $\mathbb{Z}_m$: divisori dello zero ($\text{MCD}(a,m) \neq 1$), invertibili ($\text{MCD}(a,m) = 1$), nilpotenti ($rad(m) \mid a$), idempotenti ($m \mid a(a-1)$).
> *   Abbiamo visto che $\mathbb{Z}_p$ è un campo se $p$ è primo.
> *   Abbiamo derivato i **criteri di divisibilità** usando l'aritmetica modulare.
> *   Abbiamo studiato il teorema e il metodo risolutivo per le **equazioni congruenziali lineari** $ax \equiv b \pmod{m}$.
> *   Sono stati proposti diversi esercizi su $\mathbb{Z}_m$ e la risoluzione di congruenze.

> [!TIP] Prossimi Passi
> *   Assicurati di aver compreso bene come determinare gli elementi speciali (div. zero, invertibili, etc.) in $\mathbb{Z}_m$.
> *   Fai pratica con la risoluzione delle equazioni congruenziali, specialmente con l'algoritmo di Euclide esteso.
> *   Il prossimo argomento, gli anelli dei polinomi, costruirà su queste fondamenta.