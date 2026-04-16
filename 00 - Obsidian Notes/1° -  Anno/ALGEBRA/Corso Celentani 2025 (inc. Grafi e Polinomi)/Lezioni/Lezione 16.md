# Lezione 16: Relazioni di Equivalenza, Teoria dei Numeri, Calcolo Combinatorio

**Data:** 16/05/2025 (come da note)
**Argomenti:** Relazioni di Equivalenza (esempi, classi, quoziente), Esercizio Struttura Algebrica $\mathbb{Z}_{16}$, Equazioni Diofantee, Funzione di Eulero $\varphi(n)$, Teorema di Fermat-Eulero, Calcolo Combinatorio (fattoriale, binomiale, identità, applicazioni).

#tag/relations #tag/equivalence-relations #tag/quotient-set #tag/number-theory #tag/diophantine-equations #tag/euler-phi #tag/euler-fermat-theorem #tag/combinatorics #tag/algebra-avanzata

---

## 1. Relazioni di Equivalenza

Una relazione binaria $\mathcal{R}$ su un insieme $A$ si dice **relazione di equivalenza** se è:
1.  **Riflessiva:** $\forall x \in A, x \mathcal{R} x$.
2.  **Simmetrica:** $\forall x, y \in A, x \mathcal{R} y \implies y \mathcal{R} x$.
3.  **Transitiva:** $\forall x, y, z \in A, (x \mathcal{R} y \land y \mathcal{R} z) \implies x \mathcal{R} z$.

### 1.1 Esempio di Verifica (Pag 1)

Consideriamo le seguenti relazioni su $\mathbb{Z}$:
*   **$\alpha$**: $a \operatorname{\alpha} b \iff 5a+8 \equiv_{15} 5b-7$
*   **$\beta$**: $a \operatorname{\beta} b \iff 5a+8 \equiv_{15} 5b+7$
*   **$\gamma$**: $a \operatorname{\gamma} b \iff 5a+8 \equiv_{15} 8b+5$
*   **$\delta$**: $a \operatorname{\delta} b \iff \forall p \in \mathbb{P} (\text{primi}), (p \mid a \iff p \mid b)$ (cioè $a$ e $b$ hanno gli stessi divisori primi, o $a=\pm b$, o $a,b \in \{1,-1\}$ o $a=0 \iff b=0$).

**Quali definiscono una relazione di equivalenza?**

#### Analisi di $\alpha$ (Pag 1-3)

$a \operatorname{\alpha} b \iff 5a+8 \equiv_{15} 5b-7$
Questo significa $5a+8 - (5b-7)$ è un multiplo di 15.
$5a+8 - 5b+7 = 5a-5b+15 \equiv_{15} 5a-5b$.
Quindi, $a \operatorname{\alpha} b \iff 5a-5b \equiv_{15} 0 \iff 5(a-b) \equiv_{15} 0$.
Questo significa che $15 \mid 5(a-b)$, ovvero $3 \cdot 5 \mid 5(a-b)$.
Dividendo per 5 (poiché $\text{MCD}(5, 15)=5$), otteniamo $3 \mid (a-b)$.
Quindi, $a \operatorname{\alpha} b \iff a-b \equiv_3 0 \iff a \equiv_3 b$.
La relazione $\alpha$ è la **congruenza modulo 3**.

*   **Riflessiva:** $a \equiv_3 a$ (poiché $a-a=0$ è multiplo di 3). **SÌ**.
*   **Simmetrica:** Se $a \equiv_3 b$, allora $a-b = 3k$. Quindi $b-a = -3k = 3(-k)$. $b \equiv_3 a$. **SÌ**.
*   **Transitiva:** Se $a \equiv_3 b$ e $b \equiv_3 c$, allora $a-b=3k_1$ e $b-c=3k_2$. Sommando: $(a-b)+(b-c) = 3k_1+3k_2 \implies a-c = 3(k_1+k_2)$. Quindi $a \equiv_3 c$. **SÌ**.
*   **Conclusione:** $\alpha$ è una relazione di equivalenza.

**Classi di Equivalenza per $\alpha$ (Congruenza modulo 3):**
*   $[0]_{\alpha} = \{ n \in \mathbb{Z} \mid n \equiv_3 0 \} = \{ ..., -3, 0, 3, 6, ... \} = [0]_3$.
*   $[1]_{\alpha} = \{ n \in \mathbb{Z} \mid n \equiv_3 1 \} = \{ ..., -2, 1, 4, 7, ... \} = [1]_3$.
*   $[2]_{\alpha} = \{ n \in \mathbb{Z} \mid n \equiv_3 2 \} = \{ ..., -1, 2, 5, 8, ... \} = [2]_3$.
L'insieme quoziente $\mathbb{Z}/\alpha = \mathbb{Z}_3 = \{[0]_3, [1]_3, [2]_3\}$.

#### Analisi di $\beta$ (Pag 4)

$a \operatorname{\beta} b \iff 5a+8 \equiv_{15} 5b+7$
$5a-5b \equiv_{15} 7-8 \implies 5(a-b) \equiv_{15} -1 \equiv_{15} 14$.
*   **Riflessiva?** $a \operatorname{\beta} a \implies 5(a-a) \equiv_{15} 14 \implies 0 \equiv_{15} 14$. Questo è **FALSO**.
*   **Conclusione:** $\beta$ non è riflessiva, quindi **non è una relazione di equivalenza**.

#### Analisi di $\gamma$ (Pag 5)

$a \operatorname{\gamma} b \iff 5a+8 \equiv_{15} 8b+5$
$5a-8b \equiv_{15} 5-8 \implies 5a-8b \equiv_{15} -3 \equiv_{15} 12$.
*   **Riflessiva?** $a \operatorname{\gamma} a \implies 5a-8a \equiv_{15} 12 \implies -3a \equiv_{15} 12$.
    *   Se $a=0$, $0 \equiv_{15} 12$. Falso.
*   **Conclusione:** $\gamma$ non è riflessiva, quindi **non è una relazione di equivalenza**.

#### Analisi di $\delta$ (Pag 5-6)

$a \operatorname{\delta} b \iff \forall p \in \mathbb{P}, (p \mid a \iff p \mid b)$. (Hanno gli stessi divisori primi).
*   **Riflessiva:** $\forall p, (p \mid a \iff p \mid a)$. Vero. **SÌ**.
*   **Simmetrica:** Se $(\forall p, p \mid a \iff p \mid b)$, allora $(\forall p, p \mid b \iff p \mid a)$. Vero. **SÌ**.
*   **Transitiva:** Se $(\forall p, p \mid a \iff p \mid b)$ e $(\forall p, p \mid b \iff p \mid c)$, allora $(\forall p, p \mid a \iff p \mid c)$. Vero. **SÌ**.
*   **Conclusione:** $\delta$ è una relazione di equivalenza.

**Classi di Equivalenza per $\delta$:**
*   $[0]_{\delta} = \{0\}$ (solo 0 non ha divisori primi / ha tutti i primi come divisori, a seconda della convenzione).
*   $[1]_{\delta} = \{1, -1\}$ (non hanno divisori primi).
*   $[6]_{\delta} = \{ \pm 2^n 3^m \mid n, m \ge 1 \}$. (Tutti i numeri i cui unici divisori primi sono 2 e 3).
*   $[p]_{\delta} = \{ \pm p^k \mid k \ge 1 \}$ per $p$ primo.

[[Relazione di equivalenza]] [[Classe di equivalenza]] [[Insieme quoziente]] [[Aritmetica Modulare]]

---

## 2. Esercizi su Strutture Algebriche

> [!EXERCISE] Esercizio 1 (Pag 7)
> Sia $(\mathbb{Z}_{16}, *)$ con $a * b = \overline{3}ab$.
> 1.  Verificare che è un monoide commutativo.
> 2.  Determinare l'elemento neutro.
> 3.  Determinare gli elementi invertibili (simmetrici).
> 4.  Sia $H = \{\overline{7}, \overline{11}\}$. Verificare se $H$ è una parte stabile di $(\mathbb{Z}_{16}, *)$.
> 5. Determinare il tipo di struttura $(\mathbb{H}, *)$

*Soluzione Parziale (da completare):*
*   $\mathbb{Z}_{16} = \{\overline{0}, \overline{1}, ..., \overline{15}\}$.
*   **Associatività:** $(a*b)*c = \overline{3}(ab)c = \overline{3}abc$. $a*(b*c) = a*(\overline{3}bc) = \overline{3}a(\overline{3}bc) = \overline{9}abc$.
    *   Perché siano uguali, $\overline{3}abc \equiv_{16} \overline{9}abc \implies \overline{6}abc \equiv_{16} \overline{0}$. Questo deve valere per ogni $a,b,c$. Se $abc=1$, $\overline{6} \not\equiv_{16} \overline{0}$.
    *   **Attenzione:** L'operazione è definita come $\overline{3} \cdot a \cdot b$ (dove $a,b$ sono rappresentanti).
        *   $(a*b)*c = (\overline{3}ab)*c = \overline{3}(\overline{3}ab)c = \overline{9}abc$.
        *   $a*(b*c) = a*(\overline{3}bc) = \overline{3}a(\overline{3}bc) = \overline{9}abc$.
        *   **SÌ, è associativa** (il prodotto in $\mathbb{Z}_{16}$ è associativo).
*   **Commutatività:** $a*b = \overline{3}ab$. $b*a = \overline{3}ba$. Poiché $ab=ba$ in $\mathbb{Z}$. **SÌ**.
*   **Elemento Neutro $u$:** $a*u = a \implies \overline{3}au \equiv_{16} a$.
    *   Se $a$ è invertibile in $\mathbb{Z}_{16}$ (cioè $\text{MCD}(a, 16)=1$), possiamo dividere per $a$: $\overline{3}u \equiv_{16} \overline{1}$.
    *   Cerchiamo l'inverso di $\overline{3}$ mod 16: $3x \equiv_{16} 1$. $3 \cdot (-5) = -15 \equiv_{16} 1$. Quindi $x=-5 \equiv_{16} 11$.
    *   $u \equiv_{16} 11$. Verifichiamo: $a * \overline{11} = \overline{3}a(\overline{11}) = \overline{33}a \equiv_{16} \overline{1}a = a$.
    *   **Elemento neutro $u = \overline{11}$**.
*   **Monoide Commutativo:** Sì.
*   **Elementi Invertibili:** $a*a' = u \implies \overline{3}aa' \equiv_{16} \overline{11}$.
    *   Moltiplichiamo per $\overline{11}$ (inverso di $\overline{3}$ mod 16): $\overline{11} \cdot \overline{3}aa' \equiv_{16} \overline{11} \cdot \overline{11}$.
    *   $\overline{33}aa' \equiv_{16} \overline{121}$.
    *   $\overline{1}aa' \equiv_{16} \overline{121}$. $121 = 7 \cdot 16 + 9$. Quindi $\overline{121} \equiv_{16} \overline{9}$.
    *   $aa' \equiv_{16} \overline{9}$.
    *   $a'$ esiste se $a$ è invertibile in $(\mathbb{Z}_{16}, \cdot)$ (cioè $a$ dispari) e $a' = \overline{9}a^{-1}$ (dove $a^{-1}$ è l'inverso di $a$ in $\mathbb{Z}_{16}$ rispetto al prodotto standard).
    *   Gli invertibili di $\mathbb{Z}_{16}$ (rispetto al prodotto standard) sono i numeri dispari: $\{\overline{1}, \overline{3}, \overline{5}, \overline{7}, \overline{9}, \overline{11}, \overline{13}, \overline{15}\}$.
    *   Questi sono gli elementi invertibili per l'operazione $*$.
*   **Parte Stabile $H = \{\overline{7}, \overline{11}\}$:**
    *   $\overline{7} * \overline{7} = \overline{3} \cdot \overline{7} \cdot \overline{7} = \overline{3} \cdot \overline{49} \equiv_{16} \overline{3} \cdot \overline{1} = \overline{3}$. $\overline{3} \notin H$.
    *   **NO, $H$ non è una parte stabile.**

---

## 3. Teoria dei Numeri Elementare

### 3.1 Determinare Classi in $\mathbb{Z}_{2024}$ (Pag 8)

*   $\overline{2027}$ in $\mathbb{Z}_{2024}$: $2027 = 1 \cdot 2024 + 3$. Quindi $\overline{2027} = \overline{3}$.
*   $\overline{1024}$ in $\mathbb{Z}_{2024}$: $\overline{1024}$.
*   $\overline{-2}$ in $\mathbb{Z}_{2024}$: $-2 + 2024 = 2022$. Quindi $\overline{-2} = \overline{2022}$.
*   $\overline{1001!}$ in $\mathbb{Z}_{2024}$: Poiché $2024 = 8 \cdot 11 \cdot 23 = 2^3 \cdot 11 \cdot 23$. Nel prodotto $1001! = 1 \cdot 2 \cdot \dots \cdot 8 \cdot \dots \cdot 11 \cdot \dots \cdot 23 \cdot \dots \cdot 1001$, ci sono i fattori $2^3, 11, 23$. Quindi $2024 \mid 1001!$.
    *   Pertanto, $\overline{1001!} = \overline{0}$ in $\mathbb{Z}_{2024}$.

### 3.2 Equazioni Diofantee Lineari (Pag 9-10)

Un'equazione della forma $ax + by = c$, dove $a, b, c \in \mathbb{Z}$, e si cercano soluzioni intere $x, y$.
*   Ha soluzioni se e solo se $\text{MCD}(a, b) \mid c$.
*   **Algoritmo di Euclide Esteso** per trovare $\text{MCD}(a,b)$ e una soluzione particolare $(x_0, y_0)$ per $ax+by=\text{MCD}(a,b)$.

*   **Esempio: Risolvere $209x \equiv_{165} 44$ (Pag 9).**
    *   Equivalente a $209x - 165y = 44$ per qualche $y \in \mathbb{Z}$.
    *   Calcoliamo $\text{MCD}(209, 165)$:
        *   $209 = 1 \cdot 165 + 44$
        *   $165 = 3 \cdot 44 + 33$
        *   $44 = 1 \cdot 33 + 11$
        *   $33 = 3 \cdot 11 + 0$. Quindi $\text{MCD}(209, 165) = 11$.
    *   Poiché $11 \mid 44$ (infatti $44 = 4 \cdot 11$), l'equazione ha soluzioni.
    *   L'equazione $209x - 165y = 44$ è equivalente a (dividendo per 11): $19x - 15y = 4$.
    *   Cerchiamo una soluzione per $19x - 15y = 1$ (o $19x \equiv_{15} 1$).
        *   $19 = 1 \cdot 15 + 4$
        *   $15 = 3 \cdot 4 + 3$
        *   $4 = 1 \cdot 3 + 1$
        *   A ritroso:
            *   $1 = 4 - 1 \cdot 3$
            *   $1 = 4 - 1 \cdot (15 - 3 \cdot 4) = 4 - 15 + 3 \cdot 4 = 4 \cdot 4 - 1 \cdot 15$
            *   $1 = 4 \cdot (19 - 1 \cdot 15) - 1 \cdot 15 = 4 \cdot 19 - 4 \cdot 15 - 1 \cdot 15 = 4 \cdot 19 - 5 \cdot 15$.
        *   Abbiamo $19(4) - 15(5) = 1$. Una soluzione per $19x - 15y = 1$ è $x_0=4, y_0=5$.
    *   Per ottenere $19x - 15y = 4$, moltiplichiamo per 4: $19(4 \cdot 4) - 15(5 \cdot 4) = 4$.
        *   $19(16) - 15(20) = 4$. Una soluzione particolare è $x_p=16$.
    *   Le soluzioni della congruenza $19x \equiv_{15} 4$ sono $x \equiv_{15} 16 \equiv_{15} 1$.
    *   Quindi $x = 1 + 15k$ per $k \in \mathbb{Z}$.
    *   L'equazione originale era $209x \equiv_{165} 44$. Le soluzioni sono $x \equiv_{165/11} 1 \equiv_{15} 1$.
    *   Ci sono $\text{MCD}(209, 165)=11$ soluzioni distinte modulo 165.
    *   $x \in \{1, 1+15, 1+2\cdot15, ..., 1+10\cdot15\} \pmod{165}$.
    *   $x \in \{1, 16, 31, 46, 61, 76, 91, 106, 121, 136, 151\} \pmod{165}$.

[[Equazione diofantea lineare]] [[Algoritmo di Euclide]]

### 3.3 Funzione Totiente di Eulero $\varphi(n)$ (Pag 11-12)

*   $\varphi(n)$ conta il numero di interi positivi minori o uguali a $n$ che sono **coprimi** con $n$ (cioè $\text{MCD}(k, n)=1$ per $1 \le k \le n$).
*   $\varphi(n) = |U(\mathbb{Z}_n)| = |\{ k \in \{0, ..., n-1\} \mid \text{MCD}(k, n)=1 \}|$.
*   **Proprietà:**
    *   $\varphi(p) = p-1$ se $p$ è primo.
    *   $\varphi(p^k) = p^k - p^{k-1} = p^{k-1}(p-1)$ se $p$ è primo.
    *   $\varphi(ab) = \varphi(a)\varphi(b)$ se $\text{MCD}(a, b)=1$ (moltiplicativa).
*   **Esempi:**
    *   $\varphi(2)=1$ ({1})
    *   $\varphi(3)=2$ ({1, 2})
    *   $\varphi(4)=\varphi(2^2)=2^1(2-1)=2$ ({1, 3})
    *   $\varphi(5)=4$ ({1, 2, 3, 4})
    *   $\varphi(2^3)=\varphi(8)=2^2(2-1)=4$ ({1, 3, 5, 7})
    *   $\varphi(24) = \varphi(2^3 \cdot 3) = \varphi(2^3)\varphi(3) = 4 \cdot 2 = 8$.
    *   $\varphi(1500) = \varphi(15 \cdot 100) = \varphi(3 \cdot 5 \cdot 2^2 \cdot 5^2) = \varphi(2^2 \cdot 3^1 \cdot 5^3)$
        *   $= \varphi(2^2)\varphi(3)\varphi(5^3) = (2^1(2-1)) \cdot (3-1) \cdot (5^2(5-1))$
        *   $= (2 \cdot 1) \cdot 2 \cdot (25 \cdot 4) = 2 \cdot 2 \cdot 100 = 400$.

[[Funzione totiente di Eulero]]

### 3.4 Teorema di Fermat-Eulero (Pag 13)

*   Siano $a, n \in \mathbb{Z}$ con $n \ge 1$. Se $\text{MCD}(a, n) = 1$ (cioè $a$ e $n$ sono coprimi), allora:
    $$ a^{\varphi(n)} \equiv_n 1 $$
*   **Piccolo Teorema di Fermat:** Se $p$ è un numero primo e $p \nmid a$ (cioè $\text{MCD}(a, p)=1$), allora $a^{p-1} \equiv_p 1$.
    *   Corollario: Per ogni intero $a$ e primo $p$, $a^p \equiv_p a$.

[[Teorema di Eulero (aritmetica modulare)]] [[Piccolo teorema di Fermat]]

---

## 4. Calcolo Combinatorio

Studio dei modi di contare e arrangiare oggetti.

### 4.1 Fattoriale e Coefficiente Binomiale (Pag 14)

*   **Fattoriale:** $n! = n \cdot (n-1) \cdot \dots \cdot 2 \cdot 1$ per $n \ge 1$. $0! = 1$.
*   **Coefficiente Binomiale:** "n su k" o "n choose k".
    $$ \binom{n}{k} = \frac{n!}{k!(n-k)!} = \frac{n(n-1)\dots(n-k+1)}{k!} \quad \text{per } 0 \le k \le n $$
*   **Proprietà:**
    *   $\binom{n}{0} = 1$, $\binom{n}{n} = 1$.
    *   $\binom{n}{1} = n$, $\binom{n}{n-1} = n$.
    *   $\binom{n}{k} = \binom{n}{n-k}$ (Simmetria).

### 4.2 Identità Combinatorie (Pag 15-18)

1.  **Identità di Pascal (o Regola di Stiefel):** Per $1 \le k \le n$:
    $$ \binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k} $$
    *   **Dimostrazione (Pag 15):**
        *   $\frac{n!}{k!(n-k)!} + \frac{n!}{(k-1)!(n-k+1)!}$
        *   $= \frac{n!(n-k+1)}{k!(n-k+1)!} + \frac{n!k}{k!(n-k+1)!}$
        *   $= \frac{n!(n-k+1+k)}{k!(n-k+1)!} = \frac{n!(n+1)}{k!((n+1)-k)!} = \frac{(n+1)!}{k!((n+1)-k)!} = \binom{n+1}{k}$.

2.  **Numero di Sottoinsiemi (Pag 16):** Un insieme $S$ con $|S|=n$ elementi possiede esattamente $\binom{n}{k}$ sottoinsiemi di cardinalità $k$.
    *   **Dimostrazione per induzione su $n$ (Pag 16-18):**
        *   Base $n=0$: $S=\emptyset$, $|S|=0$. Unico sottoinsieme è $\emptyset$ (cardinalità 0). $\binom{0}{0}=1$. Vero.
        *   Passo induttivo: Assumiamo $P_n$ vera (per ogni insieme di $n$ elementi, il numero di sottoinsiemi di card $k$ è $\binom{n}{k}$).
            Consideriamo $T$ con $|T|=n+1$. Sia $a \in T$. Sia $S' = T \setminus \{a\}$, quindi $|S'|=n$.
            I sottoinsiemi $C \subseteq T$ di cardinalità $k$ si dividono in due tipi:
            *   Tipo $\mathcal{A}$: $C$ non contiene $a$. Allora $C \subseteq S'$. Per ipotesi induttiva, ce ne sono $\binom{n}{k}$.
            *   Tipo $\mathcal{B}$: $C$ contiene $a$. Allora $C = C' \cup \{a\}$ dove $C' \subseteq S'$ e $|C'|=k-1$. Per ipotesi induttiva, ce ne sono $\binom{n}{k-1}$.
            *   Il numero totale di sottoinsiemi di $T$ di cardinalità $k$ è $|\mathcal{A}| + |\mathcal{B}| = \binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$ (per Identità di Pascal). $P_{n+1}$ è vera.

3.  **Somma dei Coefficienti Binomiali (Corollario di 2, Pag 18):**
    $$ \sum_{k=0}^{n} \binom{n}{k} = \binom{n}{0} + \binom{n}{1} + \dots + \binom{n}{n} = 2^n $$
    *   Questo è il numero totale di sottoinsiemi di un insieme di $n$ elementi, cioè $|P(S)| = 2^{|S|}$.

4.  **Numero di Applicazioni Iniettive (Pag 18-20):**
    Il numero di applicazioni iniettive $f: S \to T$ con $|S|=n$ e $|T|=m$ (e $n \le m$) è:
    $$ m \cdot (m-1) \cdot \dots \cdot (m-n+1) = \frac{m!}{(m-n)!} = P(m, n) \quad (\text{Disposizioni semplici}) $$
    *   **Dimostrazione per induzione su $n$ (Pag 19-20):**
        *   Base $n=1$: $S=\{s_1\}$. Per $f(s_1)$ ci sono $m$ scelte in $T$. Numero app. iniettive = $m$. Formula: $m$. Vero.
        *   Passo induttivo: Assumiamo $P_n$ vera. Consideriamo $S'$ con $|S'|=n+1$. Sia $a_{n+1} \in S'$. Sia $S = S' \setminus \{a_{n+1}\}$, $|S|=n$.
            *   Per $f(a_{n+1})$ ci sono $m$ scelte in $T$. Sia $b_i = f(a_{n+1})$.
            *   Ora dobbiamo definire $f$ sul resto di $S$ in modo iniettivo su $T \setminus \{b_i\}$ (che ha $m-1$ elementi).
            *   Per ipotesi induttiva, ci sono $(m-1)(m-2)\dots((m-1)-n+1)$ modi per farlo.
            *   Numero totale: $m \cdot [(m-1)(m-2)\dots(m-n)] = m(m-1)\dots(m-(n+1)+1)$. $P_{n+1}$ è vera.
    *   Se $n=m$, il numero di applicazioni biettive (permutazioni di T se S è un insieme di riferimento) è $n!$.

### 4.3 Binomio di Newton (Pag 21-22)

Per ogni $a, b$ in un anello commutativo (o anche solo elementi che commutano, $ab=ba$) e $n \in \mathbb{N}$:
$$ (a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \dots + \binom{n}{n}b^n $$
*   **Dimostrazione per induzione su $n$ (Pag 21-22):**
    *   Base $n=1$: $(a+b)^1 = a+b$. $\binom{1}{0}a^1b^0 + \binom{1}{1}a^0b^1 = 1a+1b = a+b$. Vero.
    *   Passo induttivo: Assumiamo $P_n$ vera.
        *   $(a+b)^{n+1} = (a+b)^n (a+b) = (\sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k) (a+b)$
        *   $= \sum \binom{n}{k} a^{n-k+1} b^k + \sum \binom{n}{k} a^{n-k} b^{k+1}$
        *   Riorganizzando le somme e usando l'identità di Pascal si ottiene la formula per $n+1$.

*   **Triangolo di Tartaglia (o di Pascal):** Fornisce i coefficienti binomiali.

[[Coefficiente binomiale]] [[Identità di Pascal]] [[Binomio di Newton]] [[Triangolo di Tartaglia]]

### 4.4 Disuguaglianza $n! \ge 2^n$ (Pag 23)

Verificare per quali $n \in \mathbb{N}$ vale $n! \ge 2^n$.
*   $n=0: 0!=1, 2^0=1$. $1 \ge 1$. Vero.
*   $n=1: 1!=1, 2^1=2$. $1 \ge 2$. Falso.
*   $n=2: 2!=2, 2^2=4$. $2 \ge 4$. Falso.
*   $n=3: 3!=6, 2^3=8$. $6 \ge 8$. Falso.
*   $n=4: 4!=24, 2^4=16$. $24 \ge 16$. Vero.
*   **Ipotesi:** Vale per $n=0$ e per $n \ge 4$.
*   **Dimostrazione per induzione per $n \ge 4$:**
    *   Base $P_4$: $4! = 24 \ge 2^4 = 16$. Vero.
    *   Passo induttivo: Assumiamo $P_k$ vera per $k \ge 4$, cioè $k! \ge 2^k$.
        Vogliamo dimostrare $P_{k+1}$: $(k+1)! \ge 2^{k+1}$.
        *   $(k+1)! = (k+1) \cdot k!$.
        *   Per ipotesi induttiva, $k! \ge 2^k$. Quindi $(k+1)! \ge (k+1) \cdot 2^k$.
        *   Poiché $k \ge 4$, allora $k+1 \ge 5 > 2$.
        *   Quindi $(k+1) \cdot 2^k > 2 \cdot 2^k = 2^{k+1}$.
        *   Dunque $(k+1)! \ge 2^{k+1}$. $P_{k+1}$ è vera.

---

> [!SUMMARY] Riepilogo Veloce Lezione 16
> *   Abbiamo definito le **Relazioni di Equivalenza** (riflessiva, simmetrica, transitiva) e visto come la congruenza modulo n ne sia un esempio.
> *   Abbiamo analizzato le **classi di equivalenza** e l'**insieme quoziente**.
> *   Abbiamo svolto un esercizio su una **struttura algebrica in $\mathbb{Z}_{16}$**.
> *   Abbiamo rivisto le **Equazioni Diofantee Lineari** e l'uso dell'Algoritmo di Euclide.
> *   Abbiamo introdotto la **Funzione Totiente di Eulero $\varphi(n)$** e le sue proprietà.
> *   Abbiamo enunciato il **Teorema di Fermat-Eulero**.
> *   Abbiamo esplorato il **Calcolo Combinatorio**: fattoriale, coefficiente binomiale, Identità di Pascal, numero di sottoinsiemi, numero di applicazioni iniettive, Binomio di Newton.
> *   Abbiamo dimostrato la disuguaglianza $n! \ge 2^n$ per $n=0$ e $n \ge 4$.

> [!TIP] Prossimi Passi
> *   Assicurati di aver compreso bene come si dimostrano le proprietà di una relazione per verificarne l'equivalenza.
> *   Fai pratica con il calcolo di $\varphi(n)$ e l'applicazione del Teorema di Fermat-Eulero.
> *   Gli esercizi di calcolo combinatorio sono fondamentali per molte aree della matematica.