# Lezione 15: Congruenze Lineari, Studio $\mathbb{Z}_n$, Anelli Prodotto, Relazioni di Equivalenza

**Data:** 13/05/2025 (come da note)
**Argomenti:** Risoluzione congruenze lineari, Divisori dello zero ed elementi nilpotenti in $\mathbb{Z}_n$, Funzioni su $\mathbb{Z}_n$ (iniettività/biettività), Strutture prodotto $(\mathbb{Z}_m \times \mathbb{Z}_n)$, Relazioni di equivalenza (introduzione).

#tag/number-theory #tag/modular-arithmetic #tag/linear-congruences #tag/zn #tag/rings #tag/zero-divisor #tag/nilpotent #tag/product-rings #tag/equivalence-relations #tag/algebra-avanzata

---

## 1. Congruenze Lineari

Una congruenza lineare è un'equazione della forma $ax \equiv b \pmod{n}$.

*   **Teorema di Risolubilità:** La congruenza lineare $ax \equiv b \pmod{n}$ ammette soluzioni se e solo se $d \mid b$, dove $d = \text{MCD}(a, n)$.
*   Se $d \mid b$, allora ci sono esattamente **$d$ soluzioni distinte modulo $n$**.
*   **Procedimento Risolutivo (Esempio Pag 1-4):**
    Consideriamo la congruenza $[45]_{51} \cdot [x]_{51} = [18]_{51}$, cioè $45x \equiv 18 \pmod{51}$.
    1.  **Calcolare $d = \text{MCD}(a, n)$:**
        $d = \text{MCD}(45, 51)$.
        $51 = 1 \cdot 45 + 6$
        $45 = 7 \cdot 6 + 3$
        $6 = 2 \cdot 3 + 0$
        Quindi $d = 3$.
    2.  **Verificare se $d \mid b$:**
        $b=18$. $3 \mid 18$ (poiché $18 = 3 \cdot 6$). **SÌ, la congruenza ammette soluzioni.**
        Ci saranno $d=3$ soluzioni distinte modulo 51.
    3.  **Dividere tutto per $d$:**
        Dividiamo $a, b, n$ per $d=3$:
        $(45/3)x \equiv (18/3) \pmod{51/3}$
        $15x \equiv 6 \pmod{17}$. Chiamiamo questa $(* *)$.
        Le soluzioni di $(*)$ sono le stesse di $(* *)$, ma quest'ultima è più semplice.
    4.  **Risolvere la congruenza ridotta $a'x \equiv b' \pmod{n'}$:**
        Ora dobbiamo risolvere $15x \equiv 6 \pmod{17}$. Poiché $\text{MCD}(15, 17) = 1$ (che divide 6), esiste un'unica soluzione modulo 17.
        Per trovare una soluzione particolare, possiamo risolvere $15x \equiv 1 \pmod{17}$ e poi moltiplicare per 6.
        Usiamo l'algoritmo di Euclide per trovare l'identità di Bézout per 15 e 17:
        $17 = 1 \cdot 15 + 2 \implies 2 = 17 - 1 \cdot 15$
        $15 = 7 \cdot 2 + 1 \implies 1 = 15 - 7 \cdot 2$
        Sostituiamo l'espressione di 2 nella seconda equazione:
        $1 = 15 - 7 \cdot (17 - 1 \cdot 15)$
        $1 = 15 - 7 \cdot 17 + 7 \cdot 15$
        $1 = 8 \cdot 15 - 7 \cdot 17$
        Prendendo questa equazione modulo 17:
        $8 \cdot 15 - 7 \cdot 17 \equiv 1 \pmod{17}$
        $8 \cdot 15 - 0 \equiv 1 \pmod{17}$
        $8 \cdot 15 \equiv 1 \pmod{17}$.
        Quindi, una soluzione a $15x \equiv 1 \pmod{17}$ è $x_0 = 8$.
        Per ottenere la soluzione di $15x \equiv 6 \pmod{17}$, moltiplichiamo $x_0$ per 6:
        $x_p = x_0 \cdot 6 = 8 \cdot 6 = 48$.
        Riduciamo modulo 17: $48 \equiv 14 \pmod{17}$ (perché $48 = 2 \cdot 17 + 14$).
        Quindi $x \equiv 14 \pmod{17}$ è l'unica soluzione di $15x \equiv 6 \pmod{17}$.
    5.  **Trovare tutte le $d$ soluzioni modulo $n$:**
        La soluzione generale di $15x \equiv 6 \pmod{17}$ è $x = 14 + 17h$, con $h \in \mathbb{Z}$.
        Queste sono anche le soluzioni di $45x \equiv 18 \pmod{51}$.
        Vogliamo le $d=3$ soluzioni distinte modulo 51. Le otteniamo dando a $h$ i valori $0, 1, \dots, d-1$ (cioè $0, 1, 2$):
        *   $h=0 \implies x_1 = 14 + 17 \cdot 0 = 14$.  Soluzione: $[14]_{51}$.
        *   $h=1 \implies x_2 = 14 + 17 \cdot 1 = 31$.  Soluzione: $[31]_{51}$.
        *   $h=2 \implies x_3 = 14 + 17 \cdot 2 = 14 + 34 = 48$. Soluzione: $[48]_{51}$.
        *   (Se $h=3$, $x_4 = 14 + 17 \cdot 3 = 14 + 51 = 65 \equiv 14 \pmod{51}$, si ripetono).
    *   **Insieme delle soluzioni:** $\text{Sol}(45x \equiv 18 \pmod{51}) = \{[14]_{51}, [31]_{51}, [48]_{51}\}$.

[[Congruenza Lineare]] [[Algoritmo di Euclide Esteso]] [[Identità di Bézout]]

---

## 2. Studio di $\mathbb{Z}_n$

### 2.1 Divisori dello Zero in $\mathbb{Z}_n$

*   Un elemento $[a]_n \in \mathbb{Z}_n$, con $[a]_n \neq [0]_n$, è **divisore dello zero** se esiste $[b]_n \in \mathbb{Z}_n$, $[b]_n \neq [0]_n$, tale che $[a]_n \cdot [b]_n = [0]_n$.
*   **Teorema:** $[a]_n$ è divisore dello zero in $\mathbb{Z}_n \iff \text{MCD}(a, n) \neq 1$.
*   **Corollario:** $\mathbb{Z}_n$ è un dominio di integrità (privo di divisori dello zero non nulli) $\iff n$ è un numero **primo**. Se $n$ è primo, $\mathbb{Z}_n$ è un campo.

*   **Esempio $\mathbb{Z}_{60}$ (Pag 5):**
    *   $60 = 2^2 \cdot 3 \cdot 5$.
    *   $[a]_{60}$ è divisore dello zero $\iff \text{MCD}(a, 60) \neq 1$.
    *   Cioè, $a$ è multiplo di 2, o di 3, o di 5 (e $a \not\equiv 0 \pmod{60}$).
    *   Gli **elementi invertibili** (unità) $U(\mathbb{Z}_{60})$ sono le classi $[a]_{60}$ tali che $\text{MCD}(a, 60) = 1$. Cioè $a$ non è multiplo di 2, né di 3, né di 5.
    *   Numero di invertibili: $\phi(60) = \phi(2^2 \cdot 3 \cdot 5) = \phi(2^2)\phi(3)\phi(5) = (2^2-2^1)(3-1)(5-1) = (4-2)(2)(4) = 2 \cdot 2 \cdot 4 = 16$. Ci sono 16 elementi invertibili in $\mathbb{Z}_{60}$.

### 2.2 Elementi Nilpotenti in $\mathbb{Z}_n$

*   Un elemento $[a]_n \in \mathbb{Z}_n$ è **nilpotente** se esiste $k \ge 1$ tale che $([a]_n)^k = [a^k]_n = [0]_n$.
*   **Teorema:** $[a]_n$ è nilpotente in $\mathbb{Z}_n \iff$ ogni fattore primo di $n$ è anche un fattore primo di $a$.
    *   Più precisamente, se $n = p_1^{e_1} \dots p_r^{e_r}$ è la fattorizzazione di $n$, allora $[a]_n$ è nilpotente $\iff p_1 \mid a, \dots, p_r \mid a$. Cioè $a$ è un multiplo di $\text{rad}(n) = p_1 p_2 \dots p_r$.
*   **Esempio $\mathbb{Z}_{60}$ (Pag 6):**
    *   $n=60 = 2^2 \cdot 3 \cdot 5$. I fattori primi di 60 sono 2, 3, 5.
    *   $[a]_{60}$ è nilpotente $\iff a$ è un multiplo di $2 \cdot 3 \cdot 5 = 30$.
    *   Gli elementi nilpotenti sono $[0]_{60}$ e $[30]_{60}$.
        *   $[30]^1 = [30] \neq [0]$.
        *   $[30]^2 = [900]$. $900 = 15 \cdot 60$, quindi $[900]_{60} = [0]_{60}$.
        *   $[0]^1 = [0]$.

[[Anello Zn]] [[Divisore dello zero in Zn]] [[Elemento Nilpotente in Zn]] [[Funzione di Eulero]]

---

## 3. Esercizi su Funzioni e Strutture

> [!EXERCISE] Esercizio 1 (Pag 7-10 - Funzione su $\mathbb{Z}_{15}$)
> Sia $f: \mathbb{Z}_{15} \to \mathbb{Z}_{15}$ definita da:
> $$ f([a]_{15}) = \begin{cases} ([a]_{15})^{-1} & \text{se } [a]_{15} \in U(\mathbb{Z}_{15}) \\ [a]_{15} & \text{se } [a]_{15} \notin U(\mathbb{Z}_{15}) \end{cases} $$
> Determinare se $f$ è iniettiva e/o suriettiva (e quindi biettiva).
>
> *   **Passo 1: Determinare $U(\mathbb{Z}_{15})$ e i non invertibili.**
>     *   $15 = 3 \cdot 5$.
>     *   $U(\mathbb{Z}_{15}) = \{ [a] \mid \text{MCD}(a, 15)=1 \} = \{[1], [2], [4], [7], [8], [11], [13], [14]\}$. $|\phi(15) = (3-1)(5-1)=8|$.
>     *   Non Invertibili (Divisori di zero + [0]): $\{[0], [3], [5], [6], [9], [10], [12]\}$.
> *   **Passo 2: Verificare Iniettività.**
>     Consideriamo $f([a])=f([b])$. Dobbiamo mostrare che $[a]=[b]$.
>     *   **Caso i:** $[a], [b] \in U(\mathbb{Z}_{15})$.
>         $f([a]) = [a]^{-1}$, $f([b]) = [b]^{-1}$. Se $[a]^{-1} = [b]^{-1}$, allora prendendo l'inverso di entrambi i lati, $([a]^{-1})^{-1} = ([b]^{-1})^{-1}$, che implica $[a]=[b]$. OK.
>     *   **Caso ii:** $[a], [b] \notin U(\mathbb{Z}_{15})$.
>         $f([a]) = [a]$, $f([b]) = [b]$. Se $[a]=[b]$, allora $[a]=[b]$. OK.
>     *   **Caso iii:** $[a] \in U(\mathbb{Z}_{15})$, $[b] \notin U(\mathbb{Z}_{15})$.
>         $f([a]) = [a]^{-1}$, $f([b]) = [b]$. Se $f([a])=f([b])$, allora $[a]^{-1} = [b]$.
>         Questo implicherebbe che $[b]$ è invertibile (perché è uguale a $[a]^{-1}$ che è invertibile). Ma avevamo supposto che $[b] \notin U(\mathbb{Z}_{15})$. Questo è un assurdo. Quindi questo caso non può portare a $f([a])=f([b])$.
>     *   Pertanto, $f([a])=f([b])$ implica che o sono entrambi invertibili e uguali, o sono entrambi non invertibili e uguali. In ogni caso, $[a]=[b]$.
>     *   **Conclusione: $f$ è iniettiva.**
> *   **Passo 3: Verificare Suriettività (o Biettività).**
>     *   Poiché $\mathbb{Z}_{15}$ è un insieme **finito**, e $f: \mathbb{Z}_{15} \to \mathbb{Z}_{15}$ è **iniettiva**, allora $f$ è anche **suriettiva** e quindi **biettiva**.
>     *   *Dimostrazione alternativa suriettività:*
>         *   Per ogni $[y] \in U(\mathbb{Z}_{15})$, vogliamo trovare $[x]$ t.c. $f([x])=[y]$. Se prendiamo $[x]=[y]^{-1}$ (che è in $U(\mathbb{Z}_{15})$), allora $f([x]) = ([y]^{-1})^{-1} = [y]$.
>         *   Per ogni $[y] \notin U(\mathbb{Z}_{15})$, vogliamo trovare $[x]$ t.c. $f([x])=[y]$. Se prendiamo $[x]=[y]$ (che non è in $U(\mathbb{Z}_{15})$), allora $f([x]) = [x] = [y]$.
>         *   **Conclusione: $f$ è suriettiva.**

> [!EXERCISE] Esercizio 2 (Pag 11-13 - Struttura $(\mathbb{Z}_{15}, *)$)
> Studiare la struttura $(\mathbb{Z}_{15}, *)$ dove $a * b = a + b + 2ab$.
> *   **Associatività e Commutatività:** Valgono perché le operazioni base ($+, \cdot$) in $\mathbb{Z}_{15}$ le hanno, e la forma è la stessa dell'Esercizio 4 della Lezione 8.
> *   **Elemento Neutro $u$:**
>     $a * u = a \implies a+u+2au = a \implies u+2au = \bar{0} \implies u(1+2a) = \bar{0}$.
>     Questo deve valere per ogni $a \in \mathbb{Z}_{15}$. In particolare per $a=\bar{0}$, $u(1) = \bar{0} \implies u = \bar{0}$.
>     Verifica: $a * \bar{0} = a+\bar{0}+2a\bar{0} = a$. **SÌ, $u=\bar{0}$ è l'elemento neutro.**
>     Quindi $(\mathbb{Z}_{15}, *, \bar{0})$ è un **monoide commutativo**.
> *   **Elementi Invertibili (Simmetrici) $a'$ per $a$:**
>     $a * a' = \bar{0} \implies a+a'+2aa' = \bar{0} \implies a'(1+2a) = -a$.
>     $a'$ esiste $\iff (1+2a)$ è invertibile in $(\mathbb{Z}_{15}, \cdot)$. Cioè $1+2a \in U(\mathbb{Z}_{15})$.
>     $U(\mathbb{Z}_{15}) = \{[1], [2], [4], [7], [8], [11], [13], [14]\}$.
>     Testiamo i valori di $a \in \mathbb{Z}_{15}$ per vedere quando $1+2a$ è invertibile:
>     *   $a=0 \implies 1+2(0)=1 \in U$. $0'$ esiste ($0' = -0 \cdot 1^{-1} = 0$).
>     *   $a=1 \implies 1+2(1)=3 \notin U$. $1$ non è invertibile per $*$.
>     *   $a=2 \implies 1+2(2)=5 \notin U$. $2$ non è invertibile per $*$.
>     *   $a=3 \implies 1+2(3)=7 \in U$. $3'$ esiste. $3' = -3 \cdot 7^{-1}$. $7 \cdot x \equiv 1 \pmod{15}$. $7 \cdot (-2) = -14 \equiv 1 \pmod{15}$. Quindi $7^{-1}=-2 \equiv 13$. $3' = -3 \cdot 13 = -39 \equiv -39+3 \cdot 15 = -39+45 = 6$. Verif: $3*6 = 3+6+2 \cdot 3 \cdot 6 = 9+36 = 45 \equiv 0 \pmod{15}$. OK.
>     *   ... e così via. Bisogna testare tutti gli $a$.
>     *   $U(\mathbb{Z}_{15}, *) = \{ a \in \mathbb{Z}_{15} \mid \text{MCD}(1+2a, 15)=1 \}$.

> [!EXERCISE] Esercizio 3 (Pag 14 - Funzione $f: \mathbb{Z}_3 \times \mathbb{Z}_5 \to \mathbb{Z}_{15}$)
> È definita una funzione $f: (\bar{a}, \tilde{b}) \mapsto [a \cdot b]_{15}$? (dove $\bar{a} \in \mathbb{Z}_3, \tilde{b} \in \mathbb{Z}_5$).
> *   Una funzione deve essere ben definita. Se prendiamo rappresentanti diversi per la stessa classe, il risultato deve essere lo stesso.
> *   Sia $(\bar{a}, \tilde{b}) = (\bar{a'}, \tilde{b'})$. Questo significa $a \equiv a' \pmod 3$ e $b \equiv b' \pmod 5$.
> *   Dobbiamo verificare se $a \cdot b \equiv a' \cdot b' \pmod{15}$.
> *   Controesempio: $(\bar{1}, \tilde{2}) \in \mathbb{Z}_3 \times \mathbb{Z}_5$. $f(\bar{1}, \tilde{2}) = [1 \cdot 2]_{15} = [2]_{15}$.
> *   Un altro rappresentante per $\bar{1}$ è $4$ ($4 \equiv 1 \pmod 3$).
> *   Consideriamo $(\bar{4}, \tilde{2})$. $f(\bar{4}, \tilde{2}) = [4 \cdot 2]_{15} = [8]_{15}$.
> *   Poiché $[2]_{15} \neq [8]_{15}$, ma $(\bar{1}, \tilde{2})$ e $(\bar{4}, \tilde{2})$ rappresentano la stessa coppia se il primo componente è pensato in $\mathbb{Z}_3$ (cioè $\bar{1}=\bar{4}$ in $\mathbb{Z}_3$), la funzione **NON è ben definita** come scritta.
> *   (La prof probabilmente intendeva una mappa basata sul Teorema Cinese del Resto, che è un isomorfismo $ \mathbb{Z}_{15} \cong \mathbb{Z}_3 \times \mathbb{Z}_5 $. La mappa $x \mapsto (x \pmod 3, x \pmod 5)$ è un isomorfismo. L'inversa è più complicata da scrivere direttamente come $a \cdot b$).

---

## 4. Anello Prodotto $\mathbb{Z}_m \times \mathbb{Z}_n$ (Esempio Pratico)

> [!EXERCISE] Esercizio 4 (Pag 17-22 - Studio $\mathbb{Z}_4 \times \mathbb{Z}_6$)
> Sia $R = \mathbb{Z}_4 \times \mathbb{Z}_6$. Definiamo $+$ e $\cdot$ componente per componente:
> $(\bar{a}, \tilde{b}) + (\bar{c}, \tilde{d}) = (\overline{a+c}, \widetilde{b+d})$
> $(\bar{a}, \tilde{b}) \cdot (\bar{c}, \tilde{d}) = (\overline{a \cdot c}, \widetilde{b \cdot d})$
> Allora $(R, +, \cdot)$ è un **anello commutativo unitario**.
>
> 1.  **Cardinalità $|R|$**:
>     $|R| = |\mathbb{Z}_4| \cdot |\mathbb{Z}_6| = 4 \cdot 6 = 24$.
> 2.  **Elemento Neutro Additivo $0_R$ e Moltiplicativo $1_R$**:
>     $0_R = ([0]_4, [0]_6)$.
>     $1_R = ([1]_4, [1]_6)$.
> 3.  **Elementi Invertibili $U(R)$, Divisori dello Zero, Nilpotenti, Idempotenti**:
>     *   $(\bar{a}, \tilde{b}) \in U(R) \iff \bar{a} \in U(\mathbb{Z}_4) \land \tilde{b} \in U(\mathbb{Z}_6)$.
>         *   $U(\mathbb{Z}_4) = \{[1]_4, [3]_4\}$.
>         *   $U(\mathbb{Z}_6) = \{[1]_6, [5]_6\}$.
>         *   $U(R) = \{ ([1], [1]), ([1], [5]), ([3], [1]), ([3], [5]) \}$. Ce ne sono $2 \cdot 2 = 4$.
>         *   Esempio: $([3]_4, [5]_6)^{-1} = ([3]_4^{-1}, [5]_6^{-1}) = ([3]_4, [5]_6)$ (poiché $3 \cdot 3 = 9 \equiv 1 \pmod 4$ e $5 \cdot 5 = 25 \equiv 1 \pmod 6$).
>     *   **Nilpotenti**: $(\bar{a}, \tilde{b})$ è nilpotente $\iff \bar{a}$ è nilpotente in $\mathbb{Z}_4$ E $\tilde{b}$ è nilpotente in $\mathbb{Z}_6$.
>         *   Nilpotenti in $\mathbb{Z}_4$: $4=2^2$. Multipli di 2: $\{[0]_4, [2]_4\}$.
>         *   Nilpotenti in $\mathbb{Z}_6$: $6=2 \cdot 3$. Multipli di $2 \cdot 3 = 6$: $\{[0]_6\}$.
>         *   Nilpotenti in $R$: $(\{[0], [2]\}, \{[0]\}) = \{ ([0], [0]), ([2], [0]) \}$.
>     *   **Idempotenti**: $(\bar{a}, \tilde{b})$ è idempotente $\iff (\bar{a}, \tilde{b})^2 = (\bar{a}, \tilde{b}) \iff \bar{a}^2 = \bar{a}$ in $\mathbb{Z}_4$ E $\tilde{b}^2 = \tilde{b}$ in $\mathbb{Z}_6$.
>         *   Idempotenti in $\mathbb{Z}_4$: $[0]^2=0, [1]^2=1, [2]^2=4 \equiv 0, [3]^2=9 \equiv 1$. Sono $\{[0], [1]\}$.
>         *   Idempotenti in $\mathbb{Z}_6$: $[0]^2=0, [1]^2=1, [2]^2=4, [3]^2=9 \equiv 3, [4]^2=16 \equiv 4, [5]^2=25 \equiv 1$. Sono $\{[0], [1], [3], [4]\}$.
>         *   Idempotenti in $R$: $2 \cdot 4 = 8$ elementi. Es: $([1]_4, [0]_6), ([0]_4, [1]_6), ([1]_4, [3]_6)$, ecc.
>     *   **Divisori dello Zero**: Tutti gli elementi non invertibili e non nulli.
> 4.  **$R$ è un Dominio di Integrità? NO**, perché ha divisori dello zero (es. $([2]_4, [0]_6) \cdot ([0]_4, [1]_6) = ([0]_4, [0]_6)$ ma i fattori non sono $0_R$).
> 5.  bis. **Caratteristica di $R$, $char(R)$**:
>     $char(R) = \text{mcm}(char(\mathbb{Z}_4), char(\mathbb{Z}_6)) = \text{mcm}(4, 6) = 12$.
>
> 6.  Sia $M = \mathbb{Z}_4 \times \{[0]_6, [3]_6\}$. Studiare la stabilità di $M$ rispetto a $+$ e $\cdot$. Che struttura hanno $(M, +)$ e $(M, \cdot)$?
>     *   L'insieme $M$ è costituito dalle coppie $(\bar{a}, \tilde{b})$ dove $\bar{a} \in \mathbb{Z}_4$ e $\tilde{b} \in \{[0]_6, [3]_6\}$.
>     *   **Stabilità per l'addizione (+):**
>         Prendiamo due elementi generici da $M$: $(\bar{a}, \tilde{b})$ e $(\bar{c}, \tilde{d})$, con $\tilde{b}, \tilde{d} \in \{[0]_6, [3]_6\}$.
>         La loro somma è $(\overline{a+c}, \widetilde{b+d})$.
>         $\overline{a+c}$ è sempre in $\mathbb{Z}_4$. Dobbiamo verificare $\widetilde{b+d} \in \{[0]_6, [3]_6\}$.
>         Le possibili somme in $\{[0]_6, [3]_6\}$ sono: $[0]_6+[0]_6=[0]_6$, $[0]_6+[3]_6=[3]_6$, $[3]_6+[0]_6=[3]_6$, $[3]_6+[3]_6=[6]_6=[0]_6$.
>         Tutti i risultati sono in $\{[0]_6, [3]_6\}$. Quindi **$M$ è stabile per l'addizione**.
>     *   **Struttura di $(M, +)$:**
>         L'addizione in $M$ è associativa e commutativa (ereditata da $R$).
>         L'elemento neutro additivo di $R$, $0_R = ([0]_4, [0]_6)$, appartiene a $M$ (poiché $[0]_4 \in \mathbb{Z}_4$ e $[0]_6 \in \{[0]_6, [3]_6\}$). Quindi $0_R$ è l'elemento neutro di $(M, +)$.
>         Per ogni elemento $(\bar{a}, \tilde{b}) \in M$, il suo opposto additivo è $(-\bar{a}, -\tilde{b})$. $-\bar{a}$ è sempre in $\mathbb{Z}_4$. Se $\tilde{b} \in \{[0]_6, [3]_6\}$, allora $-\tilde{b} \in \{[0]_6, [3]_6\}$ (infatti $-[0]_6=[0]_6$ e $-[3]_6=[3]_6$). Quindi l'opposto è in $M$.
>         Pertanto, $(M, +)$ è un **gruppo abeliano**.
>     *   **Stabilità per la moltiplicazione ( $\cdot$ ):**
>         Prendiamo due elementi generici da $M$: $(\bar{a}, \tilde{b})$ e $(\bar{c}, \tilde{d})$, con $\tilde{b}, \tilde{d} \in \{[0]_6, [3]_6\}$.
>         Il loro prodotto è $(\overline{a \cdot c}, \widetilde{b \cdot d})$.
>         $\overline{a \cdot c}$ è sempre in $\mathbb{Z}_4$. Dobbiamo verificare $\widetilde{b \cdot d} \in \{[0]_6, [3]_6\}$.
>         I possibili prodotti in $\{[0]_6, [3]_6\}$ sono: $[0]_6 \cdot [0]_6=[0]_6$, $[0]_6 \cdot [3]_6=[0]_6$, $[3]_6 \cdot [0]_6=[0]_6$, $[3]_6 \cdot [3]_6=[9]_6=[3]_6$.
>         Tutti i risultati sono in $\{[0]_6, [3]_6\}$. Quindi **$M$ è stabile per la moltiplicazione**.
>     *   **Struttura di $(M, \cdot)$:**
>         La moltiplicazione in $M$ è associativa e commutativa (ereditata da $R$).
>         Cerchiamo un elemento neutro $([e_1]_4, [e_2]_6) \in M$ tale che moltiplicato per ogni elemento di $M$ lo lasci invariato. Abbiamo trovato che questo elemento è $([1]_4, [3]_6)$. Questo elemento appartiene a $M$ (poiché $[1]_4 \in \mathbb{Z}_4$ e $[3]_6 \in \{[0]_6, [3]_6\}$). Quindi $([1]_4, [3]_6)$ è l'elemento neutro di $(M, \cdot)$. Nota che questo *non* è l'elemento neutro moltiplicativo dell'anello $R$, che è $([1]_4, [1]_6)$.
>         Non tutti gli elementi in $M$ hanno un inverso moltiplicativo *dentro M* (ad esempio, $([0]_4, [0]_6)$ non ha inverso).
>         Pertanto, $(M, \cdot)$ è un **monoide commutativo**.
>     *   **Conclusione aggiuntiva:** Poiché $M$ è stabile per entrambe le operazioni, ma non contiene l'elemento neutro moltiplicativo di $R$, $M$ non è un sottoanello di $R$.

---


## 5. Esercizio su Funzione e Invertibilità Modulare (Pag 23)

> [!EXERCISE] Esercizio 5 (Pag 23 - Funzione e Invertibilità Modulare)
> Sia $f: \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$ data da $f(a, b) = 30a+b$.
> 1. È iniettiva? È suriettiva?
> 2. Sia $T = \{c \in \mathbb{Z} \mid 60 \le c \le 70\}$. Determinare gli elementi $(n,a) \in \mathbb{Z} \times T$ (con $n \ge 0$) tali che $f(n,a)$ sia invertibile modulo 45.
>
> *   1. **Iniettività:** $f(0, 30) = 30 \cdot 0 + 30 = 30$. $f(1, 0) = 30 \cdot 1 + 0 = 30$. Poiché $(0,30) \neq (1,0)$ ma $f(0,30)=f(1,0)$, la funzione **NON è iniettiva**.
>        **Suriettività:** Per ogni $z \in \mathbb{Z}$, possiamo trovare $(a,b) \in \mathbb{Z} \times \mathbb{Z}$ tale che $f(a,b) = z$? Sì, ad esempio, prendendo $a=0$, abbiamo $f(0,b) = 30 \cdot 0 + b = b$. Quindi, per ottenere qualsiasi intero $z$, possiamo semplicemente scegliere la coppia $(0, z)$. Dunque, **È suriettiva**.
> *   2. Vogliamo che $f(n,a) = 30n+a$ sia invertibile modulo 45. Questo significa che $\text{MCD}(30n+a, 45)=1$.
>        Sappiamo che $a \in T = \{60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70\}$ e $n \ge 0$.
>        Un numero è invertibile modulo 45 se e solo se non ha fattori primi in comune con 45. I fattori primi di $45$ sono $3$ e $5$ ($45 = 3^2 \cdot 5$).
>        Quindi, vogliamo che $30n+a$ non sia divisibile per 3 e non sia divisibile per 5.
>        *   Modulo 3: $30n+a \equiv 0 \cdot n + a \equiv a \pmod 3$. Vogliamo $a \not\equiv 0 \pmod 3$.
>        *   Modulo 5: $30n+a \equiv 0 \cdot n + a \equiv a \pmod 5$. Vogliamo $a \not\equiv 0 \pmod 5$.
>        Dobbiamo quindi esaminare i valori di $a$ nell'insieme $T$ e vedere quali non sono multipli di 3 e non sono multipli di 5.
>
>        | $a$ | $a \pmod 3$ | $a \pmod 5$ | Condizioni ($\text{MCD}(a, 45)=1$)? |
>        |:----|:------------|:------------|:-----------------------------------|
>        | 60  | 0           | 0           | NO (divisibile per 3 e 5)          |
>        | 61  | 1           | 1           | SÌ                                 |
>        | 62  | 2           | 2           | SÌ                                 |
>        | 63  | 0           | 3           | NO (divisibile per 3)              |
>        | 64  | 1           | 4           | SÌ                                 |
>        | 65  | 2           | 0           | NO (divisibile per 5)              |
>        | 66  | 0           | 1           | NO (divisibile per 3)              |
>        | 67  | 1           | 2           | SÌ                                 |
>        | 68  | 2           | 3           | SÌ                                 |
>        | 69  | 0           | 4           | NO (divisibile per 3)              |
>        | 70  | 1           | 0           | NO (divisibile per 5)              |
>
>        Gli unici valori di $a$ in $T$ che soddisfano le condizioni ($a \not\equiv 0 \pmod 3$ e $a \not\equiv 0 \pmod 5$) sono: $61, 62, 64, 67, 68$.
>        Per questi valori di $a$, $\text{MCD}(a, 45) = 1$. Poiché $30n+a \equiv a \pmod{15}$ (e quindi anche modulo 3 e modulo 5), la condizione $\text{MCD}(30n+a, 45)=1$ si riduce a $\text{MCD}(a, 45)=1$.
>        La condizione su $n$ ($n \ge 0$) non influenza l'invertibilità modulo 45, dato che $30n$ è sempre un multiplo sia di 3 che di 5.
>
>        Gli elementi $(n, a) \in \mathbb{Z} \times T$ con $n \ge 0$ tali che $f(n,a)$ è invertibile modulo 45 sono tutte le coppie $(n, a)$ dove $n$ è un qualsiasi intero non negativo ($n \in \{0, 1, 2, \dots\}$) e $a$ è uno dei valori $\{61, 62, 64, 67, 68\}$.
>        L'insieme delle soluzioni è: $\{ (n, a) \in \mathbb{Z}_{\ge 0} \times \{61, 62, 64, 67, 68\} \}$.

---

## 6. Relazioni di Equivalenza (Cenno)

> [!EXERCISE] Esercizio 6 (Pag 15-16 - Relazione di Equivalenza)
> Sia $A = \{ n \in \mathbb{N} \mid n \le 7 \} = \{0, 1, 2, 3, 4, 5, 6, 7\}$.
> Sia $\rho$ una relazione di equivalenza su $A$. Sappiamo che:
> *   $0 \rho 7$
> *   $(1, 4) \in G_\rho$ (cioè $1 \rho 4$)
> *   $\{3, 4, 7\} \subseteq [2]_\rho$ (la classe di equivalenza di 2 contiene 3, 4, 7)
> *   Se $1 \rho 3$.
>
> Determinare le classi di equivalenza di $\rho$.
>
> *   Sappiamo che le classi di equivalenza formano una partizione di $A$.
> *   Da $\{3, 4, 7\} \subseteq [2]_\rho$, per simmetria e transitività, $2, 3, 4, 7$ sono tutti nella stessa classe. $[2]_\rho$ contiene almeno $\{2, 3, 4, 7\}$.
> *   $0 \rho 7$. Poiché $7 \in [2]_\rho$, allora $0 \in [2]_\rho$. Ora $[2]_\rho$ contiene almeno $\{0, 2, 3, 4, 7\}$.
> *   $1 \rho 4$. Poiché $4 \in [2]_\rho$, allora $1 \in [2]_\rho$. Ora $[2]_\rho$ contiene almeno $\{0, 1, 2, 3, 4, 7\}$.
> *   Se $1 \rho 3$ (questa info era già implicata da $1 \rho 4$ e $3 \rho 4 \implies 1 \rho 3$).
> *   Elementi rimasti: $5, 6$.
> *   Se la domanda "se $1 \rho 3$" è una condizione aggiuntiva che *potrebbe* non essere vera e va considerata come un "se", allora abbiamo due scenari. Ma le altre condizioni la implicano.
> *   Assumendo che le prime 3 condizioni siano vere, $[2]_\rho = \{0, 1, 2, 3, 4, 7\}$.
> *   Gli elementi $5$ e $6$ devono appartenere a qualche classe.
>     *   **Scenario 1:** $[5]_\rho = \{5\}$, $[6]_\rho = \{6\}$.
>         Partizione: $\{\{0, 1, 2, 3, 4, 7\}, \{5\}, \{6\}\}$.
>     *   **Scenario 2:** $5 \rho 6$. $[5]_\rho = \{5, 6\}$.
>         Partizione: $\{\{0, 1, 2, 3, 4, 7\}, \{5, 6\}\}$.
> *   La nota dice "[2] = {0,1,2,3,4,5,6,7}" oppure "{6} (isolato)". Se la classe di 2 è tutto A, allora tutti sono in relazione con tutti.
> *   Se invece la classe di 2 è $\{0,1,2,3,4,7\}$, e vogliamo che $1 \rho 3$ sia vera (come lo è), allora dobbiamo capire il significato di "determinare le relazioni di equivalenza". Se l'esercizio chiede di trovare la *più fine* partizione che soddisfa le condizioni o la *più grossolana*.
> *   Dato che $\{3,4,7\} \subseteq [2]_\rho$, e $1 \rho 4$, e $0 \rho 7$, allora $0,1,2,3,4,7$ sono tutti nella stessa classe. Se questa è $[2]_\rho$, allora $[2]_\rho = \{0,1,2,3,4,7\}$. Gli elementi restanti sono $\{5,6\}$. Possono formare classi separate $\{5\}, \{6\}$ o una classe unica $\{5,6\}$. L'esercizio presenta due possibili soluzioni per $[2]_\rho$ a seconda di come si interpreta "se $1 \rho 3$". Tuttavia, $1\rho4$ e $4\rho3$ (da $3 \in [2]$ e $4 \in [2]$) implica $1\rho3$ per transitività. Quindi $1,2,3,4,7,0$ sono tutti in relazione.
> *   Le classi di equivalenza sono una partizione.
>     Soluzione 1: $C_1=\{0,1,2,3,4,7\}, C_2=\{5\}, C_3=\{6\}$.
>     Soluzione 2: $C_1=\{0,1,2,3,4,5,7\}, C_2=\{6\}$ (se $2 \rho 5$).
>     Soluzione 3: $C_1=\{0,1,2,3,4,6,7\}, C_2=\{5\}$ (se $2 \rho 6$).
>     Soluzione 4: $C_1=\{0,1,2,3,4,7\}, C_2=\{5,6\}$ (se $5 \rho 6$ ma non con gli altri).
>     Soluzione 5: $C_1=\{0,1,2,3,4,5,6,7\}$ (tutti in relazione).
>     L'informazione nelle note indicano che $[2] = \{0,1,2,3,4,5,6,7\}$ o $[2]$ e $\{6\}$ come classe separata.
>     Se $[2]_\rho = \{0,1,2,3,4,5,7\}$ e $\{6\}$, questa è una partizione.
>     Se $[2]_\rho = \{0,1,2,3,4,7\}$ e $\{5\}$ e $\{6\}$, questa è una partizione.
>     L'esercizio è un po' vago senza specificare se si cerca la partizione più fine o grossolana che soddisfa le condizioni. Le condizioni date implicano che $\{0,1,2,3,4,7\}$ sono nella stessa classe.

[[Relazione di equivalenza]] [[Classe di equivalenza]]

---

> [!SUMMARY] Riepilogo Veloce Lezione 10 (15)
> *   Abbiamo imparato a **risolvere congruenze lineari** $ax \equiv b \pmod n$.
> *   Abbiamo caratterizzato i **divisori dello zero** ($MCD(a,n) \neq 1$) e gli **elementi nilpotenti** (multipli di $\text{rad}(n)$) in $\mathbb{Z}_n$.
> *   Abbiamo svolto esercizi sulla **biettività di funzioni** definite su $\mathbb{Z}_n$.
> *   Abbiamo analizzato la struttura dell'**anello prodotto** $\mathbb{Z}_m \times \mathbb{Z}_n$, determinando unità, nilpotenti, idempotenti, caratteristica.
> *   Abbiamo introdotto il concetto di **relazione di equivalenza** e classi di equivalenza.
> *   Sono stati proposti numerosi **esercizi** per consolidare questi concetti.

> [!TIP] Prossimi Passi
> *   Assicurati di padroneggiare la risoluzione delle congruenze lineari.
> *   Comprendi bene come identificare gli elementi speciali (invertibili, divisori dello zero, nilpotenti, idempotenti) negli anelli $\mathbb{Z}_n$ e negli anelli prodotto.
> *   Le relazioni di equivalenza sono fondamentali e portano al concetto di insiemi quoziente.