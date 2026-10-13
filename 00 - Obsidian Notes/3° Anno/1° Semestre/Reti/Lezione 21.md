# Lezione 21: Livello di rete — algoritmo Link-State

## L'algoritmo Link-State (LS)

Il **Link-State** è un approccio **centralizzato** che sfrutta la conoscenza completa della rete per trovare il cammino migliore; si basa sull'**algoritmo di Dijkstra** e, poiché lo stato di tutti i link viene propagato, **non soffre del count-to-infinity**. Questo livello di conoscenza si ottiene in pratica facendo in modo che ogni nodo invii in broadcast **pacchetti link-state**, contenenti ID e costi dei propri link, a tutti gli altri nodi della rete. La versione base calcola i cammini minimi da un nodo di partenza verso tutte le possibili destinazioni, quindi va eseguito su tutti i nodi.

### La fase di scambio dei messaggi

Prima di calcolare i cammini minimi, ogni router deve scoprire i nodi circostanti e condividere le informazioni. La fase si svolge in quattro passaggi rigorosi:

1. **Scoperta dei vicini**: il router invia un messaggio "hello" su tutti i link, e gli altri router rispondono con i propri ID.
2. **Impostazione dei costi**: il router imposta la distanza verso ciascun vicino, che può dipendere dai costi effettivi (tempo, banda) o essere impostata dall'amministratore.
3. **Costruzione del pacchetto**: il router crea un pacchetto che riassume gli ID dei nodi adiacenti e i relativi costi.
4. **Scambio dei pacchetti**: il router invia il proprio pacchetto in broadcast a tutti gli altri router e riceve pacchetti analoghi da tutti.

Completato il processo, ogni router possiede la conoscenza completa della topologia della rete e può quindi eseguire l'algoritmo dei cammini minimi (Dijkstra).

### Pseudocodice

```
LinkState(x):
    N' = {x}
    per ogni nodo v:
        se v è vicino di x:  D(v) = c(x,v)
        altrimenti:           D(v) = ∞
    repeat:
        trova w non in N' tale che D(w) è minimo
        aggiungi w a N'
        per ogni vicino v di w che non è in N':
            D(v) = min( D(v), D(w) + c(w,v) )
    until N' = N
```

La struttura dati **D(v)** memorizza la distanza dal nodo corrente verso tutte le destinazioni. In **inizializzazione** si assume che tutti i costi siano noti e vengono impostate solo le distanze verso i vicini. Nella **fase di costruzione** si seleziona il nodo più vicino w, si esplora il suo vicinato controllando se il cammino attraverso w è migliore di quello corrente, e si esce quando tutti i nodi sono stati esplorati.

### Esempio (6 nodi, algoritmo invocato su u)

Si usa una funzione aggiuntiva **p(v)** per memorizzare il nodo che precede quello selezionato: per ricostruire il cammino basta risalire a ritroso tutti i predecessori fino al nodo corrente.

| step | N' | D(v), p(v) | D(w), p(w) | D(x), p(x) | D(y), p(y) | D(z), p(z) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | u | 2, u | 5, u | 1, u | ∞ | ∞ |
| 1 | ux | 2, u | 4, x | — | 2, x | ∞ |
| 2 | uxy | 2, u | 3, y | — | — | 4, y |
| 3 | uxyv | — | 3, y | — | — | 4, y |
| 4 | uxyvw | — | — | — | — | 4, y |
| 5 | uxyvwz | — | — | — | — | — |

Al passo 0 si parte da u con i costi verso i vicini diretti; a ogni iterazione si aggiunge il nodo con distanza minima a N' e si aggiornano le distanze dei suoi vicini. Alla fine, risalendo i predecessori (ad esempio z ← y ← x ← u), si ottengono i cammini minimi.

### Complessità, pro e contro

A ogni iterazione si controllano tutti i nodi non ancora in N'; poiché a ogni iterazione un nodo esce, le iterazioni totali sono $O(n^2)$ nel caso peggiore. Con strutture dati più sofisticate, come gli **heap**, le prestazioni migliorano fino a $O(n \log n)$. Il **pro** principale è la **convergenza più rapida**, poiché tutte le comunicazioni avvengono contemporaneamente, unito all'assenza di count-to-infinity. Il **contro** è che l'algoritmo è **sincrono**: i nodi devono ricevere le informazioni dall'intera rete prima di iniziare.

## DV vs. LS

I due algoritmi adottano approcci **complementari**: DV sfrutta informazioni locali sui vicini, mentre LS richiede informazioni globali su tutti i nodi. Per quanto riguarda la **complessità dei messaggi**, LS è più complesso da implementare perché serve comunicazione sincrona tra tutti i nodi, mentre in DV la comunicazione avviene solo se cambia un miglior cammino. Per la **velocità di convergenza**, DV richiede tempo per convergere e nel frattempo si possono avere cammini subottimali; inoltre soffre del count-to-infinity. Per la **robustezza**, LS è considerato più robusto poiché le forwarding table sono calcolate separatamente: ogni nodo riceve le informazioni da tutti gli altri e crea la propria tabella. In DV, invece, tutti i calcoli sono a catena, quindi ogni nodo dipende dalle tabelle degli altri e se una tabella è sbagliata l'errore si propaga a tutte. Nel 1997, ad esempio, un router malfunzionante di un piccolo ISP causò una reazione a catena che inondò i router del backbone e disconnesse parte di Internet per diverse ore. Alla fine, entrambe le soluzioni sono usate in Internet.