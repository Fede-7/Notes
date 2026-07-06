Ecco il testo ottimizzato. Ho pulito il codice LaTeX (che presentava molti spazi superflui e comandi non necessari), migliorato la fluidità della spiegazione e reso più rigorosa la definizione di $h(y)$.

### Teorema della Media Condizionata

Considerando la variabile casuale $Z = g(X, Y)$, possiamo esprimere il suo valore atteso utilizzando la legge di probabilità congiunta $p_{X,Y}(x, y)$ e la sua scomposizione in termini condizionali:
$$
\mathbb{E}[g(X, Y)] = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} g(x, y) \underbrace{p_{X,Y}(x, y)}_{p_{X|Y}(x|y) p_Y(y)}
$$
Riorganizzando le sommatorie, otteniamo:
$$
\mathbb{E}[g(X, Y)] = \sum_{y \in \mathcal{Y}} p_Y(y) \sum_{x \in \mathcal{X}} g(x, y) p_{X|Y}(x|y) = \sum_{y \in \mathcal{Y}} h(y) p_Y(y)
$$
In questa espressione, $h(y)$ rappresenta il valore atteso della funzione $g$ condizionato a un valore fissato di $Y$:
$$
h(y) = \mathbb{E}[g(X, Y) | Y = y] \implies h(Y) = \mathbb{E}[g(X, Y) | Y]
$$
Sostituendo questa definizione nell'equazione precedente, si ottiene la formula fondamentale:
$$
\mathbb{E}[g(X, Y)] = \mathbb{E}\left[ \mathbb{E}[g(X, Y) | Y] \right]
$$
Questa relazione è nota come **Teorema della Media Condizionata** (o *Law of Iterated Expectations*), poiché dimostra che il valore atteso globale può essere calcolato come il valore atteso del valore atteso condizionato. È possibile scambiare i ruoli di $X$ e $Y$ analogamente, ottenendo $\mathbb{E}[g(X, Y)] = \mathbb{E}[\mathbb{E}[g(X, Y) | X]]$.

---

### Miglioramenti apportati:

1.  **Pulizia LaTeX:** Ho rimosso i comandi `\boldsymbol`, `\mathrm` e gli spazi bianchi eccessivi (`\ `) che rendevano il codice difficile da leggere e potenzialmente problematico in alcuni renderer di Obsidian.
2.  **Precisione Logica:** Ho sostituito *"che prende il nome di"* con una struttura più formale, introducendo il termine inglese *Law of Iterated Expectations*, spesso usato nei testi accademici per identificare questo teorema.
$$
3.  **Fluidità Sintattica:**
$$
    *   Ho cambiato *"Con riferimento a..."* (leggermente arcaico) con *"Considerando la variabile casuale..."*.
    *   Ho reso più esplicito il passaggio logico tra la somma doppia e la funzione $h(y)$.
4.  **Correzione Simbologia:** Ho usato `\implies` per la derivazione logica, che è lo standard matematico per indicare "implica".