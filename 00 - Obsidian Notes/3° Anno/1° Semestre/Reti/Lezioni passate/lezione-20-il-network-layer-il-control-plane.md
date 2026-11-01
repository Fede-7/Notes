# Lezione 20 — Il Network Layer: il control plane

## Routing: introduzione

Alla ricezione di un pacchetto un router può fare 3 cose:

1. **inoltrare** il pacchetto invariato a un vicino adatto;
2. inoltrare un pacchetto **modificato/sostituito** (es. frammentazione, masquerading);
3. **scartare** il pacchetto (es. se scaduto).

I router sono dotati di **tabelle di inoltro** che specificano la strategia locale (nel vicinato del router); tali tabelle possono essere create in modo centralizzato o decentralizzato, e all'avvio i router non hanno conoscenza del resto della rete.

I **routing algorithm** determinano i "buoni" percorsi (sequenze di router) da mittente a destinatario. Tipicamente "buono" = costo minimo (percorso più corto o più veloce), ma contano anche questioni di **politica** (es. regole su quali organizzazioni possono comunicare tra loro).

> [!info] Problema generale
> Trovare buoni percorsi su un grafo è rilevante oltre le reti: videogiochi, guida autonoma, robotica.

## Flooding

L'approccio più semplice: **ogni router inoltra tutti i pacchetti in ingresso su tutti i link, tranne quello di arrivo**.

- Esplora **tutti i percorsi** (incluso l'ottimale): se esiste un percorso, il pacchetto arriva sicuramente.
- I pacchetti "senza destinazione" raggiungono il **hop limit** e vengono scartati.
- È **robustissimo** grazie alla ridondanza (se alcuni router sono offline, esistono sempre percorsi alternativi).
- È **impraticabile** in reti grandi e ad alte prestazioni come Internet; utile solo in contesti particolari (broadcast, scenari militari).

Serve un algoritmo più raffinato.

## Formalizzazione del problema

> [!def] Grafo della rete
> La rete si modella come grafo $G = (N, E)$ dove $N$ è l'insieme dei **nodi** (i router) ed $E$ l'insieme degli **archi** (i link fisici), con un **costo** che può riflettere lunghezza fisica del link, velocità o costo monetario.

Data la funzione di costo $c$, per una coppia di nodi $(x, y)$:

- se $(x,y) \in E$, $c(x,y)$ è il costo dell'arco;
- se $(x,y) \notin E$, $c(x,y) = \infty$;
- il grafo è **non orientato**: $(x,y) \in E \iff (y,x) \in E$ e $c(x,y) = c(y,x)$.

Un **percorso** è una sequenza di nodi con archi consecutivi:

$$
(x_1, x_2, \dots, x_p) \quad \text{con} \quad (x_1, x_2), \dots, (x_{p-1}, x_p) \in E
$$

Il costo complessivo è la somma dei costi degli archi; il **percorso migliore** tra $u$ e $z$ è quello a **costo minimo**.

Gli algoritmi che trovano percorsi ottimali si chiamano **least-cost path algorithms** (*shortest path* se tutti gli archi hanno lo stesso costo). Nelle reti interessa trovarli **per tutte le coppie** di nodi: un algoritmo di routing **converge** quando il percorso minimo è stato trovato per ogni coppia. Le due famiglie usate sono **Distance-Vector** e **Link-State**.

## Algoritmo Distance-Vector (DV)

Approccio **decentralizzato** che sfrutta conoscenza locale + comunicazione tra nodi. È basato sull'equazione di **Bellman-Ford**. Ogni nodo riceve informazioni dai vicini **diretti**, fa un calcolo e ridistribuisce il risultato ai vicini. È **asincrono**: nessuna coordinazione globale richiesta.

Indicando con $d_x(y)$ il costo del percorso migliore da $x$ a $y$, vale l'**equazione di Bellman**:

$$
d_x(y) = \min_v \big\{ c(x,v) + d_v(y) \big\}
$$

Intuizione: sul percorso ottimale da $x$ a $y$ esiste un nodo adiacente $v$; il costo del percorso è il costo per raggiungere $v$ più il percorso migliore da $v$ a $y$. Trovato $v$, lo si inserisce nella tabella di inoltro e vi si dirigono tutti i pacchetti per $y$.

La **stima** $D_x(y)$ per tutte le destinazioni forma il *distance vector* del nodo.

### Pseudocodice

```text
DistanceVector(x):
    per ogni nodo v:
        se v è vicino di x:   D_x(v) = c(x,v)
        altrimenti:           D_x(v) = ∞
    per ogni vicino w e destinazione y:
        D_w(y) = ?
    invia il vettore iniziale D_x(·) a tutti i vicini

    repeat:
        se il costo di un vicino cambia:
            per ogni nodo y:
                D_x(y) = min_v { c(x,v) + D_v(y) }
            se D_x(y) è cambiato per qualche y:
                invia D_x(·) aggiornato a tutti i vicini
    until false  // per sempre
```

- **Fase di inizializzazione**: si impostano solo le distanze verso i vicini; i vettori dei vicini sono sconosciuti (`?`).
- **Fase online**: si ricevono le novità dal vicinato, si aggiornano i vettori (equazione di Bellman) e si comunicano le variazioni ai nodi adiacenti.

> [!info] Buone notizie viaggiano veloci
> Esempio: $y$ scopre il link diretto $y\!\to\!\!z$ di costo 2 e lo comunica a $x$; $x$ scopre che il percorso ottimale per $z$ passa da $y$ con costo $1+2=3$ e lo comunica a $u$; $u$ scopre un percorso finito ($1+3=4$) verso $z$. I **miglioramenti si propagano rapidamente**.

### Complessità, pro e contro

- **Complessità**: a ogni aggiornamento di un costo, i nodi rivalutano i loro archi → caso peggiore **quadratico**.
- **Pro**: asincrono, i router si adattano online in qualsiasi fase ai costi aggiornati.
- **Contro**:
  - **convergenza lenta**: gli aggiornamenti si diffondono lentamente (ogni nodo deve rilevare il cambiamento e avvisare gli adiacenti);
  - **count-to-infinity**: i percorsi migliorati vengono adottati subito, ma i guasti sono rilevati lentamente e possono generare **loop**.

## Count-to-infinity

Il problema nasce dalla natura **locale** del DV (che è anche la sua forza):

- il vettore locale $D_x(y)$ è calcolato direttamente dai vettori degli altri nodi;
- **nessuna indicazione su quali nodi compongono i percorsi ottimali dei vicini**: un nodo non può sapere se è lui stesso nel "percorso migliore" del vicino.

> [!warning] Esempio classico
> Si consideri la catena x–y–z con $c(x,y)=4$ e $c(y,z)=1$, situazione iniziale:
> $D_y(x)=4$, $D_y(z)=1$, $D_x(y)=4$, $D_x(z)=5$, $D_z(x)=5$, $D_z(y)=1$.
> Se il costo dell'arco $x\!-\!y$ **sale improvvisamente a 60** e solo $y$ se ne accorge:
> 1. $y$ aggiorna: $D_y(x) = \min\{60,\ 1 + D_z(x)\} = 1 + 5 = 6$;
> 2. ma $D_z(x)$ dipende da $D_y(x)$: $D_z(x) = 1 + D_y(x) = 7$;
> 3. e $D_y(x)$ dipende a sua volta di $D_z(x)$: $D_y(x) = 8$; e così via...

Le due stime si incrementano a vicenda **senza fine** (o fino a una configurazione stabile): le stime "contano fino all'infinito" mentre i pacchetti **ping-pongano** tra y e z.

Il problema si evita se **anche x comunica** l'incremento del costo: in tal caso le stime convergono subito ai valori corretti ($D_y(x) = 51$, $D_z(x) = 50$). Se però x è malfunzionante o lento, la convergenza richiede tempo.