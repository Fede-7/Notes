## Pagina 1

Elementi di Statistica inferenziale

Marco Lops

lops@unina.it
https://docenti.unina.it/marco.lops

---

## Pagina 2

Alcune definizioni

- Supponiamo di avere un campione di dimensione $n$, diciamo $x \in \mathbb{R}^n$;
- Supponiamo che questo campione sia il risultato di un esperimento casuale, il che significa che il ricampionamento porterebbe a un diverso insieme di risultati, diciamo $x' \in \mathbb{R}^n$;
- L'inferenza statistica è il processo che utilizza l'analisi dei dati per dedurre le proprietà di una distribuzione di probabilità sottostante, ovvero definire una legge a cui dovrebbe attenersi qualsiasi campione estratto casualmente;
- La statistica inferenziale può essere contrapposta alla statistica descrittiva. La statistica descrittiva riguarda esclusivamente le proprietà dei dati osservati e non si basa sul presupposto che i dati provengano da una popolazione più ampia.
- Gli obiettivi fondamentali dell'inferenza statistica sono la verifica delle ipotesi e la stima dei parametri.

---

## Pagina 3

Un esempio: la media campionaria

- Supponiamo di avere un set di dati $x^n \in \mathcal{X}^n \subseteq \mathbb{R}^n$;
- Sappiamo che la media campionaria è definita come
$$\bar{x}_n = \frac{1}{n} \sum_{i=1}^{n} x_i$$
- La legge dei grandi numeri ci dice che $\bar{X}_n \to \mathbb{E}[X]$ (il tipo di convergenza dipende dalla legge statistica sottostante), nel senso che, denotando $X^n$ un campione casuale estratto dalla popolazione, abbiamo
$$\frac{1}{n} \sum_{i=1}^{n} X_i \to \mathbb{E}[X]$$
- La convergenza debole (cioè la convergenza in probabilità) ci dice che la frequenza dei campioni la cui media campionaria si discosta significativamente da $\mathbb{E}[X]$ è piccola quanto vogliamo;
- La convergenza forte afferma che nel limite la probabilità di uscire da $\mathbb{E}[X]$ è zero;
- Lo afferma la convergenza medio-quadrata
$$\lim_{n \to \infty} \mathbb{E}\left[ \left( \bar{x}_n - \mathbb{E}[X] \right)^2 \right] = 0$$

---

## Pagina 4

La media del campione - continua

- Supponiamo che $x^n \in \mathcal{X}^n$, con $\mathcal{X} = (a_1, \ldots, a_M)$ discreto e finito;
- lo sappiamo
  $$\bar{x}_n = \sum_{i=1}^{M} a_i f_n(a_i)$$
  dove $f_n(a_i)$ è la frazione di valori del campione che dà $a_i$;
- Sappiamo che, se $X \in \mathcal{X}$ è una variabile casuale con pmf $\{p_X(a_i)\}_{i=1}^M$, allora:
  $$\mathbb{E}[X] = \sum_{i=1}^{M} a_i p_X(a_i)$$
- Di conseguenza, abbiamo
  $$|\bar{x}_n - \mathbb{E}[X]| \leq \sum_{i=1}^{M} |a_i| |f_n(a_i) - p_X(a_i)|$$
- Si noti che se possiamo affermare che $f_n(a_i) \rightarrow p_X(a_i)$ (in un certo senso), allora possiamo dedurre che $x^n$ è un campione di una popolazione i cui elementi sono estratti da un vettore casuale $X^n$ con densità marginale $\{p_X(a_i)\}_{i=1}^M$.

---

## Pagina 5

La distribuzione empirica

- Supponiamo che $x^n$ sia estratto da $X^n$, un insieme di variabili casuali iid $n$ con marginale sconosciuto $\{p_X(a_i)\}_{i=1}^M$;
- La frequenza con cui si verifica l'evento $X_k = a_i$ è di per sé casuale. Se $N_i$ è il numero di volte $X_k = a_i$ nel nostro campione $n$dimensionale, abbiamo:

$$\Pr\{N_i = k\} = \binom{n}{k} p_X(a_i)^k [1 - p_X(a_i)]^{n-k}$$

- Da allora

$$\mathbb{E}\left[\frac{N_i}{n}\right] = p_X(a_i), \quad \text{var}\left[\frac{N_i}{n}\right] = \frac{p_X(a_i)(1 - p_X(a_i))}{n}$$

abbiamo che $\frac{N_i}{n} \rightarrow p_X(a_i)$ nel quadrato medio, ovvero:

$$\lim_{n \to \infty} \mathbb{E}\left[\left(\frac{N_i}{n} - p_X(a_i)\right)^2\right] = 0$$

---

## Pagina 6

Convergenza quasi sicura

- Supponiamo che $\{q(a_i)\}$ sia qualsiasi altro pmf su $\mathcal{X}$ diverso dalla vera distribuzione $p_X(a_i)$ in almeno due elementi. Abbiamo:
  $$\Pr\{N_i = nq(a_i)\} = \binom{n}{nq(a_i)} p_X(a_i)^{nq(a_i)} [1 - p_X(a_i)]^{n(1 - q(a_i))}$$

- Usando il limite
  $$\sqrt{\frac{n}{8k(n - k)}} \leq \binom{n}{k} 2^{-nH\left(\frac{k}{n}\right)} \leq \sqrt{\frac{n}{\pi k(n - k)}}$$

abbiamo, ponendo $k = nq(a_i)$:
$$\sqrt{\frac{1}{8nq(a_i)(1 - q(a_i))}} \leq \binom{n}{nq(a_i)} 2^{-n\left[q(a_i) \log \frac{1}{q(a_i)} + (1 - q(a_i)) \log \frac{1}{1 - q(a_i)}\right]}$$
$$\leq \sqrt{\frac{1}{\pi nq(a_i)(1 - q(a_i))}}$$

abbiamo, per $n$ sempre più grandi:
$$\binom{n}{nq(a_i)} \sim 2^{nH_2(q(a_i), 1 - q(a_i))}$$

---

## Pagina 7

Consideriamo ora un valore $a_i$ per il quale $q(a_i) \neq p_X(a_i)$.

Quando $n$ diventa grande abbiamo:

$$\Pr \{N_i = nq(a_i)\} \sim 2^{nH_2(q(a_i), 1 - q(a_i))} p_X(a_i)^{nq(a_i)} [1 - p_X(a_i)]^{n(1 - q(a_i))}$$

$$= 2^{nH_2(q(a_i), 1 - q(a_i))} 2^{n[q(a_i) \log p_X(a_i) + (1 - q(a_i)) \log(1 - p_X(a_i))]}$$

$$= 2^{n\left[q(a_i) \log \frac{p_X(a_i)}{q(a_i)} + (1 - q(a_i)) \log \frac{1 - p_X(a_i)}{1 - q(a_i)}\right]} = 2^{-nD_i}$$

con

$$D_i = q(a_i) \log \frac{q(a_i)}{p_X(a_i)} + [1 - q(a_i)] \log \frac{1 - q(a_i)}{1 - p_X(a_i)} > 0$$

Concludiamo quindi che la probabilità che la frequenza di accadimento non sia uguale alla probabilità vera va a zero in modo esponenziale con $n$.

Ciò implica che $f_n(a_i) \rightarrow p_X(a_i)$ quasi sicuramente.

---

## Pagina 8

Supponiamo di avere un campione $x^n \in \mathcal{X}^n$, $\mathcal{X} = \{a_1, \ldots, a_M\}$ estratto da un vettore casuale $X^n$ di pmf sconosciuto;

Se calcoliamo le frequenze di occorrenza:

$$f_n(a_i) = \frac{\# \text{ of elements equal to } a_i}{n}, \quad i = 1, \ldots, M$$

abbiamo:

$$\Pr \left\{ \lim_{n \to \infty} \frac{N_i}{n} = \lim_{n \to \infty} f_n(a_i) \right\} = 1$$

Ciò implica che qualsiasi altro campione, ad esempio $y^n$, estratto dalla stessa popolazione mostrerà, per $n \to \infty$, lo stesso comportamento statistico.

Inutile dire che lo avremo per qualsiasi funzione $f(\cdot)$ dei dati

$$\Pr \left\{ \lim_{n \to \infty} f(X^n) = \lim_{n \to \infty} f(x^n) \right\} = 1$$

Pertanto, la media campionaria converge con probabilità uno alla media statistica della popolazione.

Questa proprietà viene anche definita coerenza forte nelle statistiche inferenziali.

---

## Pagina 9

L'idea principale è che, una volta osservato un campione sufficientemente ampio di una data popolazione di dati, possiamo dedurre una serie di caratteristiche che qualsiasi altro campione dovrebbe rispettare;

Alcune conoscenze preliminari relative alle statistiche della popolazione da cui viene tratto il campione possono essere note a priori;

Ad esempio, potremmo assumere che il campione sia tratto da una popolazione la cui distribuzione è nota fino ad un insieme di parametri;

Per cominciare, supponiamo che il campione sia noto essere tratto da una famiglia di distribuzioni, indicizzate da un parametro $\theta$, che si intende stimare;

Domanda: Come elaboriamo il set di dati disponibile per dedurre il valore del parametro?

---

## Pagina 10

Impostazione bayesiana: regola decisionale

- Supponiamo di avere un dataset $x^n \in \mathcal{X}^n$ che è la realizzazione di un vettore casuale $X^n$;
- Supponiamo che, in base allo stato della natura, i dati possano provenire da una qualsiasi delle diverse leggi di probabilità di $M$.
- Abbiamo quindi un insieme di $M$ diverse ipotesi mutuamente esclusive $\{H_i\}_{i=1}^M$, ciascuna delle quali definisce una diversa legge condizionale per l'insieme di dati, ovvero:

$$p_{X^n}(x^n|H_i), \quad i=1,\ldots,M$$

- Supponiamo che il vettore casuale $X^n$ sia estratto da una famiglia di distribuzione con pmf $p_{X^n}|\Theta(x^n|\theta)$, dove il valore di $\theta$ è sconosciuto;
- Supponiamo anche che le probabilità a priori - $\{p(H_i)\}_{i=1}^M$ - di questi stati della natura siano assegnate;
- Una regola decisionale è una mappa:

$$D : x^n \in \mathcal{X}^n \implies D(x^n) \in \{1,\ldots,M\}$$

che ci permette di decidere quale tra i possibili stati della natura è quello effettivamente vigente.

---

## Pagina 11

I costi di Bayes

- Supponiamo di definire la seguente matrice dei costi $M \times M$
  $$C = \begin{bmatrix}
    C_{1,1} & C_{1,2} & \ldots & C_{1,M} \\
    \ldots & \ldots & \ldots & \ldots \\
    C_{M,1} & C_{M,2} & \ldots & C_{M,M}
  \end{bmatrice}$$
dove $C_{i,j}$ è il costo associato all'evento in cui prendiamo la decisione $D(x^n) = i$ e lo stato della natura è $H_j$;
- Definiamo il rischio bayesiano medio come:
  $$\mathcal{R} = \sum_{i=1}^{M} \sum_{j=1}^{M} C_{i,j} \mathbb{P}\{D(x^n) = i, H = H_j\}$$

- Data una matrice di costo $C$, una regola decisionale ottima è una mappa $D(x^n)$ che minimizza il rischio di Bayes;
- Si noti che, se $C_{i,j} = 0$ se $i = 1, \ldots, M$ e $C_{i,j} = 1$ se $\forall i \neq j$, allora
  $$\mathcal{R} = \sum_{i=1}^{M} \sum_{j \neq i} \mathbb{P}\{D(x^n) = i, H = H_j\} = \mathbb{P}(e)$$
  cioè il rischio Bayes medio coincide con la probabilità di commettere un errore di classificazione.

---

## Pagina 12

Problema di classificazione binaria

Supponiamo per il momento che $M = 2$, che $C_{1,1} = C_{2,2} = 0$ e $C_{1,2} = C_{2,1} = 1$, quindi che

$$\mathcal{R} = \mathbb{P}\{D(\mathbf{x}^n) = 2, H_1\} + \mathbb{P}\{D(\mathbf{x}^n) = 1, H_2\} = \mathbb{P}(e)$$

Progettare una regola decisionale implica determinare una partizione di $\mathcal{X}^n$ in due sottoinsiemi, $\Omega_1$ e $\Omega_2$, in modo tale che

$$D(\mathbf{x}^n) = \begin{cases} 
1 & \text{if } \mathbf{x}^n \in \Omega_1 \\
2 & \text{if } \mathbf{x}^n \in \Omega_2 
\end{casi}$$

La corrispondente probabilità di errore è quindi scritta come:

$$\mathbb{P}(e) = \mathbb{P}\{X^n \in \Omega_1, H_2\} + \mathbb{P}\{X^n \in \Omega_2, H_1\}$$

Vogliamo determinare la legge decisionale ottimale (cioè con la minima probabilità di errore) per questo problema di classificazione binaria.

---

## Pagina 13

Classificazione binaria: leggi dei dati discreti

- Supponiamo che le osservazioni $X^n$ siano un vettore casuale discreto con dati pmf condizionali $p(X^n|H_i)$;
- Ovviamente abbiamo $\mathbb{P}\{X^n \in \Omega_i; H_j\} = 1 - \sum_{x^n \in \Omega_i} p(H_i)\mathbb{P}\{X^n = x^n|H_i\}$ per cui la probabilità di errore è scritta come
$$\mathbb{P}(e) = 1 - \left[ \sum_{x^n \in \Omega_1} p(H_1)\mathbb{P}\{X^n = x^n|H_1\} + \sum_{x^n \in \Omega_2} p(H_2)\mathbb{P}\{X^n = x^n|H_2\} \right]$$
che è minimo quando la quantità tra parentesi è massima.

- Otteniamo così la seguente regola decisionale ottima:
$$X^n \in \Omega_i \text{ iff } p(X^n|H_1)(X^n|H_1)P(H_1) > p(X^n|H_2)(X^n|H_2)P(H_2)$$
o equivalente
$$L(X^n) = \frac{p(X^n|H_1)}{p(X^n|H_2)} \geq \frac{P(H_2)}{P(H_1)} = \eta$$

- La quantità $L(X^n)$ sul lato sinistro è detta rapporto di verosimiglianza tra le due ipotesi alternative.

---

## Pagina 14

La regola decisionale precedente è nota anche come regola decisionale della massima probabilità A-posteriori (MAP), in quanto, secondo la legge di Bayes:

$$\mathbb{P}\{H = H_i | X^n = x^n\} = \frac{\mathbb{P}\{X^n = x^n | H_i\} P(H_i)}{\mathbb{P}\{X^n = x^n\}} = \frac{pX^n(x^n | H_i) P(H_i)}{pX^n(x^n)}$$

dimostrando che la regola decide per l'ipotesi la cui probabilità a posteriori dati i dati osservati è massima.

Nel caso speciale in cui le due ipotesi siano ugualmente probabili la soglia è $\eta = 1$ e la regola decisionale diventa una regola decisionale di massima verosimiglianza (ML).

Poiché le probabilità di errore condizionale sono:

$$P(e | H_1) = \mathbb{P}\{L(X^n) < \eta | H_1\} \quad P(e | H_2) = \mathbb{P}\{L(X^n) > \eta | H_2\}$$

la probabilità di errore è

$$\mathbb{P}(e) = P(H_1)P(e | H_1) + P(H_2)P(e | H_2)$$

---

## Pagina 15

Esempio: classificazione delle fonti binarie

- Supponiamo che le osservazioni siano variabili binarie iid che possono provenire con uguale probabilità da una fonte con $\mathbb{P}\{X_i = 1\} = p_1$ o da una fonte con $\mathbb{P}\{X_i = 1\} = p_2$, con $p_1 > p_2$;
- Abbiamo quindi:
  $$p_X^n(x^n|H_i) = p_i^{w_H(x^n)}(1-p_i)^{n-w_H(x^n)}$$
- dove $w_H(x^n)$ è il peso di Hamming della sequenza binaria osservata $x^n$, coincidente con il numero dei suoi 1.
- Il test di probabilità di errore minimo è
  $$\left(\frac{p_1}{p_2}\right)^{w_H(x^n)} \left[ \frac{(1-p_1)}{(1-p_2)} \right]^{n-w_H(x^n)} \gtrsim 1$$
- o, in modo equivalente
  $$w_H(x^n) \ln \left(\frac{p_1}{p_2}\right) + (n-w_H(x^n)) \ln \left(\frac{1-p_1}{1-p_2}\right) \gtrsim 0$$
- il che si riduce a
  $$w_H(x^n) \left[ \ln \left(\frac{p_1}{1-p_1}\frac{1-p_2}{p_2}\right) \right]^{H_1} \gtrsim n \ln \left(\frac{1-p_2}{1-p_1}\right)$$

---

## Pagina 16

Valutazione della prestazione

- Si noti che, poiché $p_1 > p_2$, tutti i logaritmi sono non negativi;
- Il test può quindi essere riscritto nella forma

$$w_H(x^n) \gtrsim \frac{n}{\ln \left( \frac{1-p_2}{1-p_1} \right)} = \eta_1$$

- Supponendo che $\eta_1$ non sia intero, le probabilità di errore condizionale nelle due ipotesi alternative sono scritte come:

$$\mathbb{P}(e|H_1) = \mathbb{P}\left\{ w_H(X^n) < \eta_1 | H_1 \right\} = \sum_{i=0}^{\lfloor \eta_1 \rfloor} \binom{n}{i} p_1^i (1-p_1)^{n-i}$$

$$\mathbb{P}(e|H_2) = \mathbb{P}\left\{ w_H(X^n) > \eta_1 | H_2 \right\} = \sum_{i=\lfloor \eta_1 \rfloor+1}^{n} \binom{n}{i} p_2^i (1-p_2)^{n-i}$$

per cui la probabilità di errore è

$$\mathbb{P}(e) = \frac{1}{2} \mathbb{P}(e|H_1) + \frac{1}{2} \mathbb{P}(e|H_2)$$

---

## Pagina 17

Classificazione binaria: legge dei dati continui

Supponiamo ora che i dati possano essere ricavati da $M$ possibili leggi di probabilità continua, per cui ci viene fornito un insieme di funzioni di densità di probabilità condizionale candidate $\{f_{X^n|H_i}(x^n|H_i)\}_{i=1}^M$;

L'unica differenza con il caso discreto è che il caso è quello adesso

$$\mathbb{P}\{X^n \in \Omega_1|H_1\} = \int_{\Omega_1} f_{X^n|H_1}(x^n|H_1) \, dx^n \quad \mathbb{P}\{X^n \in \Omega_2|H_2\} = \int_{\Omega_2} f_{X^n|H_2}(x^n|H_2) \, dx^n$$

Quindi, seguendo la stessa linea di pensiero del caso discreto, otteniamo che il test di probabilità di errore minimo si scrive come

$$x^n \in \Omega_i \text{ iff } f_{X^n|H_1}(x^n|H_1) P(H_1) > f_{X^n}(x^n|H_2) P(H_2)$$

o equivalente

$$L(x^n) = \frac{f_{X^n|H_1}(x^n|H_1) H_1}{f_{X^n|H_2}(x^n|H_2) H_2} \geq \frac{P(H_2)}{P(H_1)} = \eta$$

La quantità $L(x^n)$ sul lato sinistro è nuovamente chiamata rapporto di verosimiglianza tra le due ipotesi alternative.

---

## Pagina 18

Esempio: testare la media di una popolazione gaussiana

- Supponiamo che l'insieme di dati $x^n$ abbia la stessa probabilità di essere la realizzazione di un vettore casuale gaussiano indipendente i cui elementi hanno la stessa varianza e medie diverse $\mu_1$ e $\mu_2 < \mu_1$;
- Poiché $f_{x^n|H_i}(x^n|H_i) = \prod_{k=1}^{n} \frac{1}{\sqrt{2\pi}\sigma^2} e^{-\frac{(x_k - \mu_1)^2}{2\sigma^2}}$ il test ottimo si scrive come
  $$L(x^n) = \frac{f_{x^n|H_1}(x^n|H_1)}{f_{x^n|H_2}(x^n|H_2)} = e^{\frac{\sum_{k=1}^{n}(x_k - \mu_2)^2 - (x_k - \mu_1)^2}{2\sigma^2}} \geq 1$$
- Prendendo il logaritmo da entrambi i membri ed elaborandolo si ottiene il test equivalente
  $$\frac{1}{n} \sum_{k=1}^{n} x_k \geq \frac{\mu_1 + \mu_2}{2} = \eta$$
- Le quantità $\sum x_k$ per questo problema e $w_H(x^n)$ per quello precedente sono anche chiamate statistiche sufficienti nel gergo della statistica inferenziale.

---

## Pagina 19

Si noti che, sotto $H_i$, la statistica test $Z_n = \frac{1}{n} \sum_{i=1}^{n} X_i$ è gaussiana con media e varianza date da:

$$\mathbb{E}[Z_n|H_i] = \mu_i \quad \sigma_Z^2 = \frac{\sigma^2}{n} \quad \text{why?}$$

Di conseguenza le probabilità di errore condizionale sono

$$\mathbb{P}(e|H_1) = \mathbb{P}\{Z_n < \eta|H_1\} = 1 - Q\left(\frac{\eta - \mu_1}{\sigma_Z}\right) = 1 - Q\left(\sqrt{n}\frac{\mu_2 - \mu_1}{2\sigma}\right)$$

$$\mathbb{P}(e|H_2) = \mathbb{P}\{Z_n > \eta|H_2\} = Q\left(\frac{\eta - \mu_2}{\sigma_Z}\right) = Q\left(\sqrt{n}\frac{\mu_1 - \mu_2}{2\sigma}\right)$$

Poiché $\mu_1 - \mu_2 > 0$, abbiamo anche $$\mathbb{P}(e|H_1) = \mathbb{P}(e|H_2) = Q\left(\sqrt{n}\frac{\mu_1 - \mu_2}{2\sigma}\right),$$ dove

$$\mathbb{P}(e) = Q\left(\sqrt{n}\frac{\mu_1 - \mu_2}{2\sigma}\right) \to 0 \quad \text{as } n \to \infty$$

---

## Pagina 20

Verifica di ipotesi: introduzione

Esistono numerose situazioni in cui dobbiamo prendere una decisione tra due ipotesi, ma non abbiamo i mezzi per assegnare la matrice dei costi $C$ né le probabilità a priori;

Gli esempi includono una serie di situazioni di interesse pratico, vale a dire:

- Individuazione precoce di minacce alla sicurezza di un'area pattugliata;
- Rilevamento intrusioni in server/domini protetti su Internet;
- Rilevamento (e localizzazione) degli ostacoli nei sistemi avanzati di assistenza alla guida (ADAS);
- Controllo del traffico aereo;
- Innumerevoli applicazioni militari;
- ……

In tutte le situazioni sopra descritte è praticamente impossibile attribuire un costo ad un errore di valutazione dello “stato di natura”, cioè ad una decisione sbagliata tra le due ipotesi “tutto normale” o “sta succedendo qualcosa”;

È inoltre poco significativo assegnare una probabilità a priori che siano presenti “anomalie statistiche” nel set di dati.

---

## Pagina 21

Definizioni nella verifica di ipotesi

- Innanzitutto, definiamo un'ipotesi nulla, tradizionalmente indicata con $H_0$, secondo cui l'insieme di dati osservato $x^n$ è la realizzazione di un vettore casuale con distribuzione condizionale nota, con pmf/pdf $p_{X^n|H_0}(x^n|H_0)/f_{X^n|H_0}(x^n|H_0)$;
- Vogliamo decidere se, dati i dati osservati $x^n$, l'ipotesi nulla debba essere rifiutata o meno in favore di una legge diversa, diciamo $p_{X^n|H_1}(x^n|H_1)/f_{X^n|H_1}(x^n|H_1)$;
- Per quanto riguarda la classificazione binaria, dobbiamo partizionare il dominio $X^n$ in due regioni decisionali, ma il precedente framework bayesiano qui non è più applicabile a causa della mancanza di informazioni preliminari sufficienti;
- Nel progettare una regola decisionale (cioè un test), definiamo quindi:
  - L'errore di tipo I del test, o probabilità di falso allarme, come
    $$\mathbb{P}\{D(X^n) = 1|H_0\} = \begin{cases} 
    \int_{\Omega_1} f_{X^n|H_0}(x^n|H_0) dx^n & \text{Dati continui} \\
    \sum_{x^n \in \Omega_1} p_{X^n|H_0}(x^n|H_0) & \text{Dati discreti}
    \end{casi}$$
  - La potenza di prova, ovvero:
    $$1 - \beta = \mathbb{P}\{D(X^n) = 1|H_1\} = \begin{cases} 
    \int_{\Omega_1} f_{X^n|H_1}(x^n|H_1) dx^n & \text{Dati continui} \\
\sum_{x^n \in \Omega_1} p_{X^n|H_1}(x^n|H_1) & \text{Dati discreti}
    \end{casi}$$

---

## Pagina 22

Test di Neyman-Pearson

Dato il quadro delineato nella diapositiva precedente, un test di Neyman-Pearson è il risultato della seguente ottimizzazione vincolata:

$$\text{Determine } \Omega_1: \begin{cases} 1 - \beta & \text{maximum} \\ \text{subject to} & \text{type-1 error} \leq \alpha \end{cases}$$

L'esistenza della soluzione di un problema così vincolato è la maggior parte del lemma di Neyman-Pearson;

Il test risultante è il test del rapporto di verosimiglianza

$$L(\mathbf{x}^n) \gtrsim \eta L(\mathbf{x}^n) = \begin{cases} \frac{f_{\mathbf{x}^n}|H_1(\mathbf{x}^n)|H_1}{f_{\mathbf{x}^n}|H_0(\mathbf{x}^n)|H_0} & \text{Continuous data} \\ \frac{p_{\mathbf{x}^n}|H_1(\mathbf{x}^n)|H_1}{p_{\mathbf{x}^n}|H_0(\mathbf{x}^n)|H_0} & \text{Discrete data} \end{cases}$$

Come soluzione dell’equazione va scelta la soglia $\eta$:

$$\mathbb{P}\{L(\mathbf{x}^n) > \eta|H_0\} = \alpha$$

Si noti che l'applicazione di qualsiasi funzione monotonicamente crescente a entrambi i membri del test precedente non ne altera l'ottimalità, per cui possiamo introdurre equivalentemente la log-verosimiglianza $\ln L(\mathbf{x}^n) = \Lambda(\mathbf{x}^n)$ e confrontarla con una soglia appena determinata.

---

## Pagina 23

Esempio: testare la media di una popolazione gaussiana

- Supponiamo che l'ipotesi nulla sia che le osservazioni siano iid gaussiane con media zero e varianza data, ovvero $X_i \sim \mathcal{N}(0, \sigma^2)$, mentre la sua alternativa è $X_i \sim \mathcal{N}(\mu, \sigma^2)$;
- Dopo la diapositiva 18, si legge il test del rapporto di verosimiglianza

$$L(x^n) = \frac{f_{X^n|H_1}(x^n|H_1)}{f_{X^n|H_0}(x^n|H_0)} = e^{\frac{\sum_{k=1}^{n}(x_k - \mu)^2 - x_k^2}{2\sigma^2}} \frac{H_1}{H_0} \eta$$

dove ora $\eta$ dovrebbe essere scelto in modo da soddisfare il vincolo.

- Prendendo il logaritmo da entrambi i membri, semplificando e assorbendo in una nuova soglia (sconosciuta) $\eta'$ tutte le quantità indipendenti dai dati si ottiene il test equivalente

$$\frac{1}{n} \sum_{i=1}^{n} x_i \frac{H_1}{H_0} \eta'$$

dove $\eta'$ va scelto in modo da garantire che la probabilità di errore di tipo I sia uguale al valore di progetto $\alpha$.

---

## Pagina 24

Dobbiamo prima impostare la soglia di rilevamento. Si noti che la statistica del test, sotto $H_0$, è gaussiana con media e varianza pari a zero $\frac{\sigma^2}{n}$ (vedere diapositiva 18). Di conseguenza:

$$\mathbb{P}\left\{\frac{1}{n} \sum_{i=1}^{n} X_i > \eta' | H_0\right\} = Q\left(\frac{\sqrt{n} \eta'}{\sigma}\right) = \alpha \implies \eta' = \frac{\sigma}{\sqrt{n}} Q^{-1}(\alpha)$$

Per valutare la potenza del test, notiamo che, sotto $H_1$, la statistica del test è gaussiana con media $\mu$ e varianza $\frac{\sigma^2}{n}$, per cui:

$$1 - \beta = \mathbb{P}\left\{\frac{1}{n} \sum_{i=1}^{n} X_i > \eta' | H_1\right\} = Q\left(\frac{\sqrt{n} \eta' - \mu}{\sigma}\right)$$

Vale la pena notare che, per $n \to \infty$, $\eta' \to 0$ per qualsiasi $\alpha$, quindi che

$$\lim_{n \to \infty} 1 - \beta = \lim_{n \to \infty} Q\left(\frac{\sqrt{n} \eta'(n) - \mu}{\sigma}\right) = 1$$

ovvero arriviamo alla prestazione ideale $\alpha = 0$, $1 - \beta = 1$.

---

## Pagina 25

Stima dei parametri: generalità

- Supponiamo di avere un dataset $x^n \in \mathcal{X}^n$ che è la realizzazione di un vettore casuale $X^n$;
- Supponiamo che il vettore casuale $X^n$ sia estratto da una famiglia di distribuzione con pmf/pdf $p_{X^n|\Theta}(x^n|\theta)/f_{X^n|\Theta}(x^n|\theta)$, dove il valore di $\theta$ è sconosciuto;
- $\theta$ è un parametro tipicamente continuo, che può essere la realizzazione di una variabile casuale continua $\Theta$ con marginale nota $f_\Theta(\theta)$ (impostazione bayesiana) o una quantità deterministica sconosciuta che assume valori in un insieme continuo;
- Domanda: Come stimiamo $\theta$ in base al campione raccolto?

Si noti che, in ambito bayesiano, l’applicazione diretta della regola di Bayes produce:

$$f_{\Theta|X^n}(\theta|x^n) = \begin{cases} 
\frac{p_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)}{\int p_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)d\theta} & \text{dati discreti} \\
\frac{f_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)}{\int f_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)d\theta} & \text{dati continui}
\end{casi}$$

Si noti che, se $\Theta$ è discreto, quanto sopra diventa un problema di classificazione. Nota anche che nell'equazione sopra abbiamo usato il fatto che

$$p_{X^n}(x^n) = \int p_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)d\theta \quad f_{X^n}(x^n) = \int f_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)d\theta$$

---

## Pagina 26

Stima dei parametri

- Uno stimatore del parametro $\theta$ è una variabile casuale $\hat{\Theta}(X^n)$ - le cui realizzazioni sono $\hat{\theta}(X^n)$ cercando di "indovinare" il valore di $\theta$ basandosi su un'osservazione $x^n \in \mathcal{X}^n$;
- Per progettare uno stimatore, definiamo innanzitutto un rischio Bayes medio, ovvero:

$$\mathcal{R} = \mathbb{E} \left[ C(\hat{\Theta}(X^n) - \Theta) \right] = \mathbb{E}_{X^n} \left[ C(\hat{\Theta}(X^n) - \Theta) \mid X^n \right]$$

dove $C(\cdot)$ è una funzione di costo opportunamente definita.

- Uno stimatore ottimo è quello che minimizza il rischio di Bayes, ovvero:

$$\hat{\Theta}_{\text{opt}}(X^n) = \arg \min \mathbb{E} \left[ C(\hat{\Theta}(X^n) - \Theta) \right]$$

- Da allora

$$\mathbb{E} \left[ C(\hat{\Theta}(X^n) - \Theta) \right] = \sum_{x^n \in \mathcal{X}^n} p_{X^n}(x^n) \int C(\hat{\theta}(x^n) - \theta) f_{\Theta|X^n}(\theta|x^n) d\theta$$

una stima ottimale di Bayes operante su un campione osservato $x^n$ è definita come:

$$\hat{\theta}(x^n) = \arg \min \int C(\hat{\theta}(x^n) - \theta) f_{\Theta|X^n}(\theta|x^n) d\theta$$

---

## Pagina 27

Supponiamo che $C(\hat{\Theta}(X^n) - \Theta) = (\hat{\Theta}(X^n) - \Theta)^2$;

Lo stimatore ottimale di Bayes può essere derivato come soluzione dell'equazione

$$\frac{\partial}{\partial \hat{\theta}(x^n)} \int (\hat{\theta}(x^n) - \theta)^2 f_{\Theta|X^n}(\theta|x^n) d\theta = 0$$

Otteniamo così la stima

$$\hat{\theta}(x^n) = \int \theta f_{\Theta|X^n}(\theta|x^n) d\theta = \mathbb{E} [\Theta|X^n = x^n]$$

che corrisponde sicuramente ad un minimo data la convessità del rischio Bayes prescelto.

---

## Pagina 28

Esempio: composto Bernoulli

- Supponiamo che $X^n \in \{0, 1\}^n$ sia condizionatamente Bernoulli con parametro $\beta$, con $B \sim \mathcal{U}(0, 1)$;
- Il peso di Hamming $w(x^n)$ di una sequenza binaria è il numero di unità che contiene. Abbiamo:
  $$p_{X^n|B}(x^n|\beta) = \beta^{w(x^n)}(1 - \beta)^{n-w(x^n)}$$

- Facendo una media su $B$ abbiamo la legge incondizionata:
  $$p_{X^n}(x^n) = \int_0^1 \beta^{w(x^n)}(1 - \beta)^{n-w(x^n)} d\beta = \frac{\Gamma(w + 1)\Gamma(n - w + 1)}{\Gamma(n + 2)} = \frac{1}{\binom{n + 1}{w(x^n)}}$$

- La legge condizionale è così
  $$f_{B|X^n}(\beta|x^n) = \frac{\beta^{w(x^n)}(1 - \beta)^{n-w(x^n)}}{p_{X^n}(x^n)} = \frac{\beta^{w(x^n)}(1 - \beta)^{n-w(x^n)}}{\binom{n + 1}{w(x^n)}}$$

---

## Pagina 29

Esempio: Composto Bernoulli - continua

- La stima del MMSE è così
  $$\frac{1}{pX^n(x^n)} \int_0^1 \beta^{w(x^n)+1}(1-\beta)^{n-w(x^n)} d\beta$$
- Risolvendo l'integrale si ottiene quindi
  $$\hat{\beta}_{\text{MMSE}}(x^n) = \frac{\Gamma(w+2)\Gamma(n-w+1)}{\Gamma(n+3)} \frac{1}{\binom{n+1}{w(x^n)}} = \frac{w(x^n)+1}{n+2}$$

che è la stima ottenuta tramite lo stimatore MMSE:

$$\hat{\beta}_{\text{MMSE}}(X^n) = \frac{w(X^n)+1}{n+2}$$

---

## Pagina 30

Stimatore massimo A posteriori (MAPE)

- Assumiamo ora la seguente funzione di costo:
  $$C(\hat{\Theta}(X^n) - \Theta) = \Pi \left( \frac{\hat{\Theta}(X^n) - \Theta}{\epsilon} \right) = \begin{cases} 0 & \left| \hat{\Theta}(X^n) - \Theta \right| < \frac{\epsilon}{2} \\ 1 & \text{otherwise} \end{cases}$$

- È ovvio che, poiché $\epsilon$ è arbitrariamente piccolo, ciò risulta nello stimatore MAP
  $$\hat{\theta}(x^n) = \arg \max f_{\Theta|X^n}(\theta|x^n)$$

- Applicando questo stimatore al problema precedente (composto di Bernoulli) si ha la stima:
  $$\hat{\beta}_{\text{MAP}}(x^n) = \frac{w(x^n)}{n}$$

- Di conseguenza, lo stimatore MAP del parametro sconosciuto lo è
  $$\hat{B}_{\text{MAP}}(x^n) = \frac{w(x^n)}{n}$$

---

## Pagina 31

Performance dello stimatore: Errore sistematico (Bias)

- Notiamo preliminarmente che:
  $$\mathbb{E}[B] = \int_{0}^{1} \beta d\beta = \frac{1}{2}, \quad \mathbb{E}[B^2] = \frac{1}{3}, \quad \sigma_B^2 = \frac{1}{12}$$

- Da allora
  $$\mathbb{E}[w(X^n)] = \mathbb{E}\left[ \overbrace{\mathbb{E}[w(X^n)|B]}^{nB} \right] = \frac{n}{2}, \quad \mathbb{E}[w^2(X^n)] = \mathbb{E}\left[ \overbrace{\mathbb{E}[w(X^n)|B]}^{nB(1-B)+n^2B^2} \right] = \frac{n}{6} + \frac{n^2}{3}$$

  dove $\sigma_B^2 = \frac{n}{6} \left(1 + \frac{n}{2}\right)$.

- Per il MMSE:
  $$\mathbb{E}\left[ \hat{B}_{\text{MMSE}}(X^n)|B = \beta \right] = \frac{n\beta + 1}{n+2}, \quad \mathbb{E}\left[ \hat{B}_{\text{MMSE}}(X^n) \right] = \frac{n^2 + 1}{n+2}$$

- Per la MAPPA:
  $$\mathbb{E}\left[ \hat{B}_{\text{MAP}}(X^n)|B = \beta \right] = \beta, \quad \mathbb{E}\left[ \hat{B}_{\text{MAP}}(X^n) \right] = \frac{n^2}{n} = \frac{1}{2}$$

- Concludiamo che il MMSE è uno stimatore distorto, mentre il MAP non lo è;
- Si noti che il MMSE è asintoticamente imparziale, poiché l'errore sistematico svanisce quando $n$ cresce.

---

## Pagina 32

Errori casuali: coerenza

- Dopo lunghi, anche se elementari, calcoli, troviamo:

$$\mathbb{E} \left[ (B_{\text{MMSE}}(X^n) - B)^2 \right] = \overline{e^2}_{\text{MMSE}} = \frac{n - 2}{6(n + 2)^2}$$

$$\mathbb{E} \left[ (B_{\text{MAP}}(X^n) - B)^2 \right] = \overline{e^2}_{\text{MAP}} = \frac{1}{6n}$$

- Inutile dire che abbiamo $\overline{e^2}_{\text{MMSE}} < \overline{e^2}_{\text{MAP}} \forall n$.

- Poiché entrambi gli MSE vanno a zero al crescere di $n$, abbiamo che i due stimatori sono definiti MS coerenti, nel senso che l’errore casuale ha valore MS asintoticamente nullo;

- Sfruttando la disuguaglianza di Tchebyshev, abbiamo che entrambi gli stimatori tendono a $B$ in probabilità (coerenza, ovvero consistenza debole). Se $\hat{B}(X^n)$ è uno qualsiasi dei due stimatori, abbiamo quindi:

$$\forall \epsilon > 0 \quad \lim_{n \to \infty} \Pr \left\{ \left| \hat{B}(X^n) - B \right| > \epsilon \right\} = 0$$

- Si può dimostrare che entrambi gli stimatori sono fortemente coerenti, nel senso che $\hat{B}(X^n) \to B$ quasi sicuramente.

---

## Pagina 33

Definizioni generali

- Consideriamo un campione $x^n$ estratto da un vettore casuale $X^n \in \mathcal{X}^n \subseteq \mathbb{R}^n$;
- $\mathcal{X}^n$ può essere discreto o continuo, ma assumiamo che $X^n$ abbia un pdf (pmf, nel caso discreto) noto per appartenere a una famiglia con precedenti noti. Assumiamo quindi la conoscenza del pdf congiunto $f_{X^n,\Theta}(x^n,\theta)$ e del parametro a priori $f_\Theta(\theta)$.
- Vogliamo dedurre il valore del parametro $\theta$ per la realizzazione osservata $x^n$. La stima MMSE e la stima MAP sono quindi definite come

$$\hat{\theta}_{\text{MMSE}}(x^n) = \mathbb{E} \left[ \Theta|X^n = x^n \right] = \int \theta f_{\Theta|X^n}(\theta|x^n) \, d\theta, \quad \hat{\theta}_{\text{MAP}}(x^n) = \arg \max_{\theta} f_{\Theta|X^n}(\theta|x^n)

- Uno stimatore è **imparziale** se $\mathbb{E} \left[ \hat{\Theta}(X^n) - \Theta \right] = 0$;
- Uno stimatore è **asintoticamente imparziale** se lo è solo nel limite della dimensione campionaria infinita;
- Uno stimatore è consistente se $\hat{\Theta}(X^n) \rightarrow \Theta$ **in probabilità**;
- Uno stimatore è MS consistente se $\hat{\Theta}(X^n) \rightarrow \Theta$ **nel quadrato medio**;
- Uno stimatore è fortemente consistente se $\hat{\Theta}(X^n) \rightarrow \Theta$ **quasi sicuramente**.

---

## Pagina 34

Un esempio: osservazioni gaussiane con media casuale

- Sia ricavato $x^n$ da $X^n$ con:
  $$f_{X^n|M}(x^n|\mu) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-\frac{(x_i - \mu)^2}{2\sigma^2}\right]$$
- Sia $\mu$ una realizzazione di $M \sim \mathcal{N}(0, \sigma_M^2)$;
- Vogliamo dedurre il valore $\mu$ di $M$ relativo all'osservazione $x^n$ di $X^n$.
- Osservare che la densità a posteriori della media è:
  $$f_{M|X^n}(\mu|x^n) = \frac{f_{X^n|M}(x^n|\mu) f_M(\mu)}{f_X^n(x^n)} = \mathcal{N}\left(\frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}}, \frac{1}{n + \frac{\sigma^2}{\sigma_M^2}}\right)$$
- Detto altrimenti, il priore coniugato della media di una distribuzione gaussiana è ancora gaussiano;
- Abbiamo così che si legge la stima MMSE della media
  $$\hat{\mu}_{\text{MMSE}}(x^n) = \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}} \iff \hat{M}_{\text{MMSE}}(X^n) = \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}}$$

---

## Pagina 35

Stimatore MAP

Consideriamo ora la stima MAP. Ovviamente possiamo scrivere

$$\ln f_M(x^n) (\mu | x^n) = \ln f_{X^n}|M(x^n | \mu) + \ln f_M(\mu) - \ln f_{X^n}(x^n)$$

Massimizzando rispetto a $\mu$ si ottiene lo stimatore MAP

$$\hat{\mu}_{\text{MAP}}(x^n) = \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}} \iff \hat{M}_{\text{MAP}}(X^n) = \frac{\sum_{i=1}^{n} X_i}{n + \frac{\sigma^2}{\sigma_M^2}}$$

che coincide con il MMSE!!

Domanda: Ciò è casuale o c'è una ragione più profonda per la coincidenza di questi due stimatori?

---

## Pagina 36

Unicità degli stimatori di Bayes

- Sia $C(\cdot)$ una funzione di costo arbitraria dell'errore di stima;
- Supponiamo che $C(\cdot)$ sia pari e convesso e che $f_{\Theta|X^n}(\theta|x^n)$ sia simmetrico rispetto alla sua media $\mathbb{E}[\Theta|X^n = x^n]$, ovvero:
  $$f_{\Theta|X^n}(\theta - \mathbb{E}[\Theta|X^n = x^n])|x^n) = f_{\Theta|X^n}(-\theta + \mathbb{E}[\Theta|X^n = x^n])|x^n)$$
- Quindi il MMSEE minimizza il rischio di Bayes per qualsiasi funzione di costo in questa classe.
- La dimostrazione è semplice e qui viene omessa.
- Si osservi che, in senso stretto, la funzione di costo 0–1 che porta ad uno stimatore MAP non è differenziabile.
- Tuttavia si può dimostrare che, nella condizione di simmetria sul posteriore di cui sopra, abbiamo
  $$\hat{\mu}_{\text{MAP}}(x^n) = \hat{\mu}_{\text{MMSE}}(x^n)$$

---

## Pagina 37

Inferenza non bayesiana: stima dei parametri non casuali

- Supponiamo ora che le osservazioni $x^n \in \mathcal{X}^n$ siano tratte da una famiglia di pdf, $f_{X^n}(x^n; \theta)$;
- Supponiamo che $\theta$ sia deterministico e sconosciuto: equivalentemente, possiamo assumere di non avere informazioni a priori sufficienti per assegnare un $f_\Theta(\theta)$ a priori;
- Supponiamo che lo spazio dei parametri sia $S$;
- Definiamo verosimiglianza del parametro $\theta$, dato che sono disponibili le osservazioni $x^n$, la funzione:

$$L(\theta; x^n) = f_{X^n}(x^n; \theta)$$

o, in modo equivalente, log-verosimiglianza della funzione

$$\Lambda(\theta; x^n) = \log f_{X^n}(x^n; \theta)$$

- Una stima della probabilità massima (ML) di $\theta$ è

$$\hat{\theta}_{\text{ML}}(x^n) = \arg \max_{\theta \in S} \log f_{X^n}(x^n; \theta)$$

ed è una realizzazione del Maximum Likelihood Estimator (MLE):

$$\hat{\Theta}_{\text{ML}}(X^n) = \arg \max_{\theta \in S} \log f_{X^n}(X^n; \theta)$$

---

## Pagina 38

Dato uno stimatore $\Theta(X^n)$ del parametro non casuale $\theta$, abbiamo:

$$\mathbb{E}[\Theta(X^n)] = \theta + b_n(\theta)$$

con $b_n(\theta)$ la distorsione dello stimatore;

Lo stimatore è imparziale se $b_n(\theta) = 0$, mentre è solo asintoticamente imparziale se $b_n(\theta)$ diventa infinitamente piccolo con $n$;

L'errore casuale dello stimatore viene solitamente quantificato tramite il suo valore quadratico medio, ovvero:

$$\mathbb{E}[(\Theta(X^n) - \theta)^2] = \frac{e_n^2}{2}$$

Uno stimatore MMSE imparziale di $\theta$ è uno stimatore che minimizza la varianza:

$$\text{Var}[\Theta(X^n)] = \mathbb{E}[\Theta^2(X^n)] - \theta^2$$

Uno stimatore è debolmente coerente se $\Theta(X^n) \to \theta$ in probabilità, fortemente coerente se $\Theta(X^n) \to \theta$ quasi sicuramente, MS coerente se $\frac{e_n^2}{2} \to 0$.

---

## Pagina 39

Cramér-Rao Bound - Fatti preliminari

- Sia $x^n$ un campione estratto da un vettore casuale $X^n \sim f_X(x^n; \theta)$ con $\theta$ non casuale;
- Considera l'identità
  $$\int_{\mathbb{R}^n} f_X(x^n; \theta) dx^n = 1$$
- Dopo la differenziazione rispetto a $\theta$ di quanto sopra abbiamo
  $$\int_{\mathbb{R}^n} \frac{\partial f_X(x^n; \theta)}{\partial \theta} dx^n = \int_{\mathbb{R}^n} \frac{\partial \log f_X(x^n; \theta)}{\partial \theta} f_X(x^n; \theta) dx^n$$
  $$= \mathbb{E} \left[ \frac{\partial \log f_X(x^n; \theta)}{\partial \theta} \right] = 0$$
- Differenziando ancora abbiamo:
  $$\mathbb{E} \left[ \left( \frac{\partial \log f_X(x^n; \theta)}{\partial \theta} \right)^2 \right] = \text{var} \left[ \frac{\partial \log f_X(x^n; \theta)}{\partial \theta} \right] = - \mathbb{E} \left[ \frac{\partial^2 \log f_X(x^n; \theta)}{\partial \theta^2} \right]$$

---

## Pagina 40

Cramér-Rao Bound - Derivazione

- Sia $\hat{\Theta}(X^n)$ uno stimatore del parametro non casuale $\theta$ con:
  $$\mathbb{E} \left[ \Theta(X^n) \right] = \int_{\mathbb{R}^n} \hat{\Theta}(X^n) f_X^n(x^n; \theta) dx^n = \theta + b_n(\theta)

- Differenziando rispetto a $\theta$ si ha l'identità di cui sopra
  $$\int_{\mathbb{R}^n} \Theta(x^n) \frac{\partial f_X^n(x^n; \theta)}{\partial \theta} dx^n = \int_{\mathbb{R}^n} \frac{\partial \log f_X^n(x^n; \theta)}{\partial \theta} f_X^n(x^n; \theta) dx^n$$
  $$\text{COV} \left[ \Theta(X^n), \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right] = 1 + b_n'(\theta)

- Applicando la disuguaglianza di Cauchy-Schwartt, finalmente abbiamo
  $$\left| \text{COV} \left[ \Theta(X^n), \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right] \right|^2 = \left[ 1 + b_n'(\theta) \right]^2 \leq \text{Var} \left[ \Theta(X^n) \right] \text{Var} \left[ \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right]$$

---

## Pagina 41

Elaborando le derivazioni precedenti, otteniamo un limite inferiore imbattibile alla varianza di qualsiasi stimatore del parametro non casuale $\theta$ nella forma:

$$\text{Var} \left[ \Theta(X^n) \right] \geq \frac{[1 + b'_n(\theta)]^2}{\mathbb{E} \left[ \left( \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right)^2 \right]} = \frac{[1 + b'_n(\theta)]^2}{I_n(\theta)}$$

La quantità $I_n(\theta)$ è definita come Informazione di Fisher e obbedisce alla seguente identità:

$$I_n(\theta) = \mathbb{E} \left[ \left( \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right)^2 \right] = -\mathbb{E} \left[ \frac{\partial^2 \log f_X^n(X^n; \theta)}{\partial \theta^2} \right]$$

---

## Pagina 42

Cramér-Rao Bound - Stimatori imparziali

- Come anticipato, lo stimatore $\Theta(X^n)$ è **imparziale** se $\mathbb{E}[\Theta(X^n)] = \theta$;
- In questa situazione, abbiamo quello
$$\mathbb{E}[(\Theta(X^n) - \theta)^2] = \text{Var}[\Theta(X^n)] \geq \frac{1}{l_n(\theta)}$$

- Pertanto il Cramér-Rao Bound (CRB) diventa un limite inferiore imbattibile per l'MSE di qualsiasi stimatore.
- Uno stimatore imparziale il cui MSE è pari al CRB è definito **efficiente**.
- **Fatto importante**: Se esiste uno stimatore efficiente per un dato problema di stima non bayesiano, questo necessariamente coincide con lo stimatore ML.

---

## Pagina 43

Un esempio: dedurre la frequenza di cifratura di una fonte senza memoria

- Consideriamo inizialmente $x^n \in \{0,1\}^n$, tratto da $X^n \sim \mathcal{B}(1,\beta)$, $\beta$ sconosciuto;
- Abbiamo visto che, se $w(x^n)$ è il peso di Hamming della successione osservata, allora:
  $$p_{X^n}(x^n) = \beta^{w(x^n)}(1 - \beta)^{n-w(x^n)}$$

- La stima ML risulta quindi come:
  $$\frac{\partial \log p_{X^n}(x^n)}{\partial \beta} = 0 \implies \hat{\beta}_{\text{ML}}(x^n) = \frac{w(x^n)}{n}$$

- Lo stimatore $\beta(X^n) = \frac{w(X^n)}{n}$ è tale che:
  $$\mathbb{E}\left[\frac{w(X^n)}{n}\right] = \beta, \quad \text{var}\left[\frac{w(X^n)}{n}\right] = \frac{\beta(1-\beta)}{n}$$

Di conseguenza, è imparziale e coerente con la SM. È efficiente?

---

## Pagina 44

Notiamo che abbiamo:

$$\log p_{X^n}(X^n; \beta) = w(X^n) \log \beta + [n - w(X^n)] \log(1 - \beta)$$

Quindi abbiamo:

$$\frac{\partial p_{X^n}(X^n; \beta)}{\partial \beta} = \frac{w(X^n)}{\beta} - \frac{n - w(X^n)}{1 - \beta}$$

$$\frac{\partial^2 p_{X^n}(X^n; \beta)}{\partial \beta^2} = -\frac{w(X^n)}{\beta^2} - \frac{n - w(X^n)}{(1 - \beta)^2}$$

Poiché $\mathbb{E}[w(X^n)] = n\beta$, abbiamo:

$$l_n(\beta) = \frac{n}{\beta} + \frac{n}{1 - \beta} = \frac{n}{\beta(1 - \beta)} \implies \text{CRB} = \frac{\beta(1 - \beta)}{n}$$

Concludiamo che l'MLE della frequenza di cifratura è efficiente.

---

## Pagina 45

Supponiamo ora di avere parametri casuali $m$, $\theta[\theta_1, \ldots, \theta_m]^T$ estratti da un pdf noto $f_{\Theta}(\theta)$ e un set di dati $x^n$ estratto da un pdf condizionale $f_{X^n|\theta}(x^n|\theta)$;

Definire una funzione di costo

$$C(\theta - \hat{\theta}) = C(\theta_1 - \hat{\theta}_1, \ldots, \theta_m - \hat{\theta}_m)$$

Uno stimatore ottimale di Bayes può essere trovato risolvendo il problema di minimizzazione:

$$\hat{\theta}(x^n) : \mathbb{E}\left[C(\Theta - \hat{\Theta}(X^n))\right] = 0$$

Utilizzando la stessa procedura del caso a parametro singolo otteniamo quindi:

$$\hat{\Theta}(X^n) = \arg \min_{\mathbb{R}^m} C(\theta - \hat{\theta}(X^n))f_{\Theta|X^n}(\theta|X^n)d\theta$$

---

## Pagina 46

Lo stimatore MMSE

- Supponiamo che la funzione di costo sia
  $$C(\theta - \hat{\theta}) = \sum_{i=1}^{m} \left( \theta_i - \hat{\theta}_i(x^n) \right)$$
- Poiché il problema di minimizzazione è disgiunto (cioè separabile), abbiamo:
  $$\hat{\theta}_i(x^n) = \mathbb{E} \left[ \Theta_i | X^n = x^n \right] = \int \theta_i f_{\theta_i} x^n \left( \theta_i | x^n \right) d\theta_i$$
  per cui lo stimatore vettoriale MMSE recita:
  $$\hat{\Theta}(X^n) = \mathbb{E} \left[ \Theta | X^n \right]$$

---

## Pagina 47

Lo stimatore MAP

- Se assumiamo
  $$C(\theta - \hat{\theta}) = \sum_{i=1}^{m} \Pi \left( \frac{\theta_i - \hat{\theta}_i(x^n)}{\epsilon} \right)$$
- considerando la stessa procedura che abbiamo
  $$\hat{\theta}_i(x^n) : \left. \frac{\partial f_{\Theta}|x^n(\theta|x^n)}{\partial \theta_i} \right|_{\theta_i = \hat{\theta}_i(x^n)} = 0$$
- Equivalentemente, abbiamo che la stima MAP risolve l'equazione:
  $$\nabla_{\theta} f_{\Theta}|x^n(\theta|x^n) |_{\theta = \hat{\theta}(x^n)} = 0$$

---

## Pagina 48

Stima non bayesiana di più parametri

- Supponiamo ora che il vettore dei parametri $\theta$ sia reale e deterministico;
- Possiamo definire la funzione di log-verosimiglianza dei dati osservati, assunti tratti da una famiglia di distribuzione $f_{X^n}(x^n; \theta)$ come:
  $$\Lambda(\theta; x^n) = \log f_{X^n}(x^n, \theta)$$
- Definiamo la stima di massima verosimiglianza del vettore $\theta$ la soluzione dell'equazione:
  $$\nabla_\theta \Lambda(\theta; x^n)|_{\theta = \hat{\theta}(x^n)} = 0$$
- Il corrispondente stimatore $\hat{\Theta}(X^n)$ è nuovamente definito stimatore di Massima Verosimiglianza (ML) e gode di alcune proprietà fondamentali.

---

## Pagina 49

Stimatori MMSE lineari

- Cominciamo con un semplice problema scalare. Supponiamo che $x^n$ sia il campione osservato, estratto da $X^n$, e supponiamo di voler progettare uno stimatore lineare di un parametro casuale $\Theta$, distribuito secondo una legge nota, nella forma:

$$\hat{\Theta}(X^n) = a^T X^n + b \quad a \in \mathbb{R}^n$$

- Uno stimatore MMSE lineare (LMMSE) seleziona il vettore $a$ e la costante $b$ in modo da minimizzare il MMSE

$$\mathbb{E} \left[ (\hat{\Theta}(X^n) - \Theta)^2 \right] = \mathbb{E} \left[ (a^T X^n + b - \Theta)^2 \right]

che è uguale a

$$a^T Ra + b^2 + \mathbb{E} \left[ \Theta^2 \right] - 2b(\overline{\Theta}) - 2a^T \mathbb{E} \left[ X^n \Theta \right] - 2ba^T \mathbb{E} \left[ X^n \right]

dove $R = \mathbb{E} \left[ X^n X^{nT} \right]$ è la matrice di correlazione del vettore casuale $X^n$.

---

## Pagina 50

Annullando il gradiente rispetto a $a$ e la derivata rispetto a $b$ otteniamo:

$$\nabla_a \mathbb{E} \left[ \left( a^T X^n + b - \Theta \right)^2 \right] = 2 M a - 2 \mathbb{E} \left[ X^n \Theta \right] = 0$$

$$\frac{\partial \mathbb{E} \left[ \left( a^T X^n + b - \Theta \right)^2 \right]}{\partial b} = 2 b - 2 \overline{\Theta} - 2 a^T \mathbb{E} \left[ X^n \right] = 0$$

Risolvendo per $b$ si ottiene

$$b_{\text{LMMSE}} = \mathbb{E} \left[ \Theta \right] - a^T \mathbb{E} \left[ X^n \right]$$

$$\widehat{\Theta} \left( X^n \right) = a^T \left( X^n - \mathbb{E} \left[ X^n \right] \right) + \mathbb{E} \left[ \Theta \right]$$

che, ricollocato nell'MSE, dimostra che $a$ dovrebbe minimizzarsi

$$\| a^T \left( X^n - \mathbb{E} \left[ X^n \right] \right) + \left( \Theta - \mathbb{E} \left[ \Theta \right] \right) \|^2$$

Di conseguenza, denotando $M = \mathbb{E} \left[ \left( X^n - \mathbb{E} \left[ X^n \right] \right) \left( X^n - \mathbb{E} \left[ X^n \right] \right)^T \right]$ la matrice di covarianza di $X^n$, lo stimatore LMMSE legge

$$a_{\text{LMMSE}} = M^{-1} \mathbb{E} \left[ \left( X^n - \mathbb{E} \left[ X^n \right] \right) \left( \Theta - \mathbb{E} \left[ \Theta \right] \right) \right] = M^{-1} s$$

---

## Pagina 51

L'algoritmo del gradiente

- Supponiamo di voler risolvere iterativamente il problema LMMSE delineato prima;
- Abbiamo visto che il gradiente dell'MSE si scrive come
  $$\nabla_a \mathbb{E} \left[ (a^T X^n + b - \Theta)^2 \right] = 2Ma - 2s$$
con $\mathbb{E}[X^n \Theta] = s$ noto;
- Considera la seguente iterazione per determinare $a_{\text{LMMSE}}$:
  $$a^{(n+1)} = a^{(n)} - \gamma \left( Ma^{(n)} - s \right)$$
  che può essere riscritto come
  $$a^{(n+1)} = a^{(n)} - \gamma M \left( a^{(n)} - \underbrace{M^{-1} s}_{a_{\text{LMMSE}}} \right)$$

---

## Pagina 52

L'algoritmo del gradiente - continua

- Viene visualizzato l'errore alla $(n+1)$-esima iterazione
  $$\epsilon^{(n+1)} = a^{(n+1)} - a_{\text{LMMSE}} = a^{(n)} - a_{\text{LMMSE}} - \gamma M \left( a^{(n)} - a_{\text{LMMSE}} \right) = (I - \gamma M) \epsilon^{(n)}$$

- Di conseguenza abbiamo
  $$\epsilon^{(n+1)} = (I - \gamma M)^n \epsilon^{(1)} = U (I - \gamma \Lambda)^n U^T$$

dove $\Lambda$ è la matrice diagonale degli autovalori di $M$ e $U$ contiene i suoi autovettori.

- L'errore converge quindi a zero se il modulo massimo degli autovalori di $I - \gamma M$ è minore di uno, ovvero:
  $$-1 < 1 - \gamma \lambda_{\text{MAX}} < 1 \implies 0 < \gamma < \frac{2}{\lambda_{\text{MAX}}}$$

---

## Pagina 53

Un approccio diverso: la statistica descrittiva

- Dimentichiamoci ora della probabilità. Ipotizziamo invece di passare alla statistica descrittiva, in cui i campioni contano per quello che sono e non sono considerati realizzazioni di vettori casuali:
- Definiamo un dataset di training come una raccolta di campioni $p$ $n$-dimensionali, che possono essere organizzati nella matrice $n \times p$:

$$X = \begin{bmatrix}
x_1(1) & \cdots & x_1(p) \\
\cdots & \cdots & \cdots \\
x_n(1) & \cdots & x_n(p)
\end{bmatrice} \in \mathbb{R}^{n \times p}$$

- Supponiamo di conoscere i valori misurati $p$ del parametro $\theta$, ciascuno corrispondente a uno dei campioni $p$ $n$-dimensionali del training set, ovvero:

$$y = [\theta(1), \ldots, \theta(p)] \in \mathbb{R}^p$$

- Vogliamo adattare i dati a un modello lineare nella forma:

$$\theta(i) = a^T x^n(i) + \epsilon_n$$

con $\epsilon_n$ che incapsula l'errore.

---

## Pagina 54

Lo stimatore dei minimi quadrati

Poiché abbiamo un set di dati $p$-dimensionale, vogliamo selezionare $a$ in modo tale da ridurre al minimo:

$$\|\epsilon_n\|^2 = \sum_{i=1}^{p} \left[ a^T x^n(i) - \theta(i) \right]^2$$

Il nostro problema è selezionare $a$ e $b$ in modo ottimizzato. Notatelo preliminarmente

$$\sum_{i=1}^{p} \left[ a^T x^n(i) - \theta(i) \right]^2 = \| X^T a - y \|^2$$

Notalo

$$\| X^T a - y \|^2 = a^T X X^T a + \| y \|^2 - 2 a^T X y$$

---

## Pagina 55

Lo stimatore dei minimi quadrati - continua

- Differenziando rispetto a $a$ quindi si ottiene
  $$\nabla_a \| X^T a - y \|^2 = 2 X X^T a - 2 X y = 0$$
  che cede
  $$a_{\text{LS}} = (X X^T)^{-1} X y$$
  richiedendo che $(X X^T)$ sia invertibile (cioè $p \ge n$).

- Per riferimento futuro, chiameremo questa stima basata su un campione $p$-dimensionale
  $$a_{\text{LS}}(p) = (X(p) X^T(p))^{-1} X(p) y(p)$$

---

## Pagina 56

Supponiamo di avere un'osservazione dell'ambiente con orizzonte infinito, in modo che la dimensione del campione $p$ possa aumentare;

Consideriamo due scenari, ovvero:

un. Vogliamo migliorare progressivamente la nostra stima aggiungendo più osservazioni;

B. Vogliamo adattarci alle condizioni che possono cambiare "dimenticando" le vecchie osservazioni per valutare in modo più significativo le nuove osservazioni.

Possiamo aggiustare lo stimatore LS in modo tale da tenere conto di entrambe le situazioni sopra descritte, e possiamo farlo con una complessità limitata.

---

## Pagina 57

Supponiamo $p \geq n$ e supponiamo di aver valutato

$$a_{LS}(p) = \left[ X(p) X^T(p) \right]^{-1} X(p) y(p)$$

Supponiamo di avere un nuovo vettore nel set di dati, diciamo $x^n(p+1)$, e una nuova osservazione, $\theta(p+1)$.

La nuova stima sarebbe

$$a_{LS}(p+1) = \left[ X(p+1) X^T(p+1) \right]^{-1} X(p+1) y(p+1)$$

Domanda: dobbiamo ricalcolare tutto da zero?

Si noti che l'operazione di inversione comporta una complessità $\mathcal{O}(n^3)$, mentre l'operazione di prodotto di matrici ha una complessità $\mathcal{O}(np)$ (in termini di moltiplicazioni).

---

## Pagina 58

La formula di Sherman-Morrison

- Sia $R$ una matrice invertibile di ordine $n$;
- Siano $u$ e $v$ vettori colonna $n$-dimensionali;
- Abbiamo il seguente lemma di inversione di matrice con aggiornamento di rango 1:

$$\left( R + uv^T \right)^{-1} = R^{-1} - \frac{R^{-1}uv^T R^{-1}}{1 + u^T R^{-1}v}$$

---

## Pagina 59

Notalo

$$\underbrace{X(p+1)X^T(p+1)}_{R(p+1)} = \sum_{i=1}^{p+1} x^n(i)x^{nT}(i) = \underbrace{X(p)X^T(p)}_{R(p)} + x^n(p+1)x^{nT}(p+1)$$

Di conseguenza

$$R^{-1}(p+1) = R^{-1}(p) - \frac{R^{-1}(p)x^n(p+1)x^{nT}(p+1)R^{-1}(p)}{1 + K(p+1)}$$

con

$$K(p+1) = x^{nT}(p+1)R^{-1}(p)x^n(p+1)$$

---

## Pagina 60

D'altra parte abbiamo

$$X(p+1) = [X(p) x^n(p+1)] , \quad y(p+1) = [y(p) \theta(p+1)]^T$$

implicando

$$X(p+1) y(p+1) = X(p) y(p) + \theta(p+1) x^n(p+1)$$

Poiché $a(p+1) = R^{-1}(p+1)X(p+1)y(p+1)$, abbiamo

$$a(p+1) = \left[ I_n - \frac{R^{-1}(p) x^n(p+1)}{1 + K(p+1)} x^n T(p+1) \right]$$

$$\left[ a(p) + \theta(p+1) R^{-1}(p) x^n(p+1) \right]$$

che ha complessità $\mathcal{O}(n^2)$, indipendente (e non scalabile con $p$).

---

## Pagina 61

Per far fronte a situazioni in cui l'ambiente circostante può variare (lentamente) nel tempo, potremmo voler forzare i "vecchi dati" a pesare meno dei dati "freschi".

Un modo possibile per farlo è tramite il livellamento esponenziale, la cui idea principale è quella di adottare la seguente funzione di costo:

$$\sum_{i=1}^{p} w^{p-i} \left[ a^T x^n(i) - \theta(i) \right]^2$$

Il peso $w < 1$ regola la velocità con cui il passato viene dimenticato.

Minimizzando rispetto a $a$ si ottiene il LS esponenzialmente livellato:

$$a = \left[ \sum_{i=1}^{p} w^{p-i} x^n(i) x^{nT}(i) \right]^{-1} \sum_{i=1}^{p} w^{p-i} x^n(i) \theta(i)$$

esso stesso suscettibile di un'implementazione ricorsiva alla luce del lemma di Sherman-Morrison.

---

## Pagina 62

Generalizzazione

Supponiamo ora che, nelle stesse condizioni viste sopra, vogliamo trovare un LS nella forma più generale

$$\widehat{\theta}(\mathbf{x}^n) = \mathbf{a}^T \mathbf{x}^n + b$$

Calcoli lunghi, anche se semplici, portano al modulo LMS generale

$$\mathbf{a}_{\text{LMS}} = \left( X_0 X_0^T \right)^{-1} X_0 y_0, \quad b_{\text{LMS}} = \underbrace{\frac{1}{p} \sum_{i=1}^{p} \theta(i)}_{\widehat{\theta}} - \frac{1}{p} \mathbf{1}_p^T \mathbf{X}^T \mathbf{a}_{\text{LMS}}$$

dove $\mathbf{1}_p$ è un vettore monodimensionale $p$ e

$$\mathbf{X}_0 = \begin{bmatrix} x_1(1) - \bar{x}_1 & \dots & x_1(p) - \bar{x}_1 \\ \dots & \dots & \dots \\ x_n(1) - \bar{x}_n & \dots & x_n(p) - \bar{x}_n \end{bmatrix} \in \mathbb{R}^{n \times p}, \quad \mathbf{y}_0 = \left[ y_1 - \bar{\theta}, \dots, y_p - \bar{\theta} \right]^T$$

con

$$\bar{x}_k = \frac{1}{p} \sum_{i=1}^{p} x_k(i) \iff \bar{x} = \frac{1}{p} \sum_{i=1}^{p} x^n(i), \quad \mathbf{X}_0 = \mathbf{X} - \bar{x} \mathbf{1}_p^T$$

---

