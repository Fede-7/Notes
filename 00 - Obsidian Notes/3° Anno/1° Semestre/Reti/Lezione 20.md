# Lezione 20: Livello di rete — piano di controllo e routing

## Introduzione al routing

Alla ricezione di un pacchetto, un **router può compiere tre azioni**: inoltrare il pacchetto tale e quale a un vicino adatto; inoltrare un pacchetto modificato o sostituito (ad esempio in caso di frammentazione o masquerading); oppure scartarlo, ad esempio perché scaduto. Esistono poi tipi diversi di router: alcuni molto semplici, usati dagli amministratori locali per connettere LAN e WAN, altri usati dagli ISP per inoltrare i pacchetti al dispositivo giusto in tutta Internet.

Ogni router possiede una **forwarding table** che specifica la strategia locale di inoltro nel proprio vicinato, e alla creazione delle tabelle si può procedere in modo centralizzato o decentralizzato. Poiché i router non hanno conoscenza del resto della rete, per decidere dove inoltrare i pacchetti si usano **algoritmi di routing**, che determinano buoni cammini (sequenze di rotte) da mittenti a riceventi. Tipicamente un "buon" cammino è quello a **costo minimo**, quindi più corto o più veloce; nel mondo reale, però, vanno considerati anche gli **aspetti di policy**, come le regole su quali organizzazioni possono comunicare tra loro. Il problema del routing è cruciale per le reti di calcolatori, ma trovare buoni cammini su un grafo è rilevante anche in molti altri ambiti (videogiochi, guida autonoma, robotica).

## Flooding

L'approccio più semplice è il **flooding**: ogni router inoltra tutti i pacchetti in arrivo su tutti i link, tranne quello da cui li ha ricevuti. Poiché vengono esplorati tutti i cammini, incluso l'ottimo, il pacchetto sarà consegnato di sicuro se esiste un cammino; i pacchetti che "non vanno da nessuna parte" raggiungono l'**hop limit** e vengono scartati. Grazie alla ridondanza l'approccio è **estremamente robusto**: anche se alcuni router sono offline, i cammini alternativi vengono comunque considerati. Il flooding è quindi adatto a situazioni specifiche in cui serve ridondanza (broadcast di messaggi, scenari militari), ma risulta **impraticabile in reti grandi e ad alte prestazioni** come Internet, per le quali servono algoritmi più raffinati.

## Formalizzazione del problema

La rete si formalizza come un **grafo G = (N, E)**, dove **N** è l'insieme dei nodi (i router della rete) ed **E** è l'insieme degli archi, cioè i link fisici, rappresentati come coppie di nodi. Ogni arco ha un valore di **costo**, che può riflettere la lunghezza fisica del link, la sua velocità o un costo monetario. Si definisce inoltre una funzione di costo c tale che, data una coppia di nodi (x,y): se (x,y) ∈ E, allora c(x,y) è il costo dell'arco; se (x,y) ∉ E, allora c(x,y) = ∞; e poiché il grafo è non orientato, se (x,y) ∈ E anche (y,x) ∈ E e c(x,y) = c(y,x).

Un **cammino** è una sequenza di nodi in cui tutti i nodi adiacenti sono collegati:

$$(x_1, x_2, \dots, x_p) \quad \text{con } (x_1,x_2), \dots, (x_{p-1},x_p) \in E$$

Il costo complessivo del cammino è la somma dei costi dei link. Detto $P_{uz}$ l'insieme di tutti i cammini possibili tra i nodi u e z, il cammino migliore è quello a **costo minimo**, e gli algoritmi che lo trovano si chiamano **algoritmi a costo minimo** (o shortest-path, quando tutti gli archi hanno lo stesso costo). Nelle reti di calcolatori interessa trovare il cammino ottimo **per tutte le coppie di nodi**: un algoritmo di routing **converge** quando il cammino più corto è stato trovato per ogni coppia. Le due famiglie tipiche sono il **Distance Vector** e il **Link State**.

## Algoritmo Distance-Vector (DV)

Il **Distance-Vector** è un approccio **decentralizzato** che sfrutta la conoscenza locale della rete, combinata con la comunicazione tra nodi, per trovare i cammini minimi; si basa sull'**algoritmo di Bellman-Ford**. Ogni nodo riceve informazioni da uno o più vicini direttamente collegati, esegue un calcolo e distribuisce il risultato ai vicini. Poiché non richiede che tutti i nodi siano coordinati tra loro, l'algoritmo è **asincrono**.

### L'equazione di Bellman

Detto $d_x(y)$ il costo del miglior cammino dal nodo x al nodo y:

$$d_x(y) = \min_v \{c(x,v) + d_v(y)\}$$

L'intuizione è che deve esistere un nodo adiacente v a x che sta sul miglior cammino da x a y: il costo di quel cammino è il costo per raggiungere v, più il miglior cammino tra v e y. Trovato tale v, lo si inserisce nella **forwarding table** e gli si inoltrano tutti i pacchetti diretti a y. Per farlo serve una stima di $d_v(y)$ per tutti i vicini: il **vettore di distanza** (distance vector).

### Esempio

Tra u e z il miglior cammino è:

$$u \rightarrow x \rightarrow y \rightarrow z$$

Lungo il cammino ottimo l'equazione di Bellman deve valere per tutti i nodi. Considerando u, che ha tre vicini w, v e x: per x valgono c(u,x) = 1 e $d_x(z) = 3$; per v valgono c(u,v) = 2 e $d_v(z) = 5$; per w valgono c(u,w) = 5 e $d_w(z) = 3$. Di conseguenza **x minimizza** c(u,v) + $d_v(z)$ ed è il prossimo nodo del cammino ottimo. Iterando sul nodo successivo, l'equazione continua a valere: y minimizza per x, e così via. Con il distance vector di tutti i nodi, l'equazione di Bellman permette quindi di calcolare il **next hop** per la forwarding table.

### Pseudocodice

```
DistanceVector(x):
  per ogni nodo v:
      se v è vicino di x:  D_x(v) = c(x,v)
      altrimenti:           D_x(v) = ∞
  per ogni vicino w e destinazione y:  D_w(y) = ?
  invia D_x(·) iniziale a tutti i vicini

  repeat:
      se il costo verso un vicino si aggiorna:
          per ogni nodo y:  D_x(y) = min_v { c(x,v) + D_v(y) }
          se D_x(y) è cambiato per qualche destinazione y:
              invia D_x(·) aggiornato a tutti i vicini
  until false  // per sempre
```

La struttura dati $D_w(v)$ memorizza i vettori di distanza da tutti i nodi w verso le destinazioni v. In fase di **inizializzazione** sono impostate solo le distanze verso i vicini. Nella **fase online**, invece, si ricevono le novità dal vicinato, i vettori di distanza vengono aggiornati tramite l'equazione di Bellman e i cambiamenti locali vengono comunicati ai nodi adiacenti.

### Esempio sul cammino u-z

1. All'inizio u conosce solo i vicini, quindi il costo verso z è infinito ($D_u(z) = \infty$).
2. y si "sveglia" e scopre un miglior cammino verso z, cioè il link diretto y-z di costo 2 ($D_y(z) = c(y,z) = 2$), e comunica la buona notizia a x.
3. x scopre che il miglior cammino verso z passa per y con costo 3 ($D_x(z) = c(x,y) + D_y(z) = 1 + 2$) e comunica la notizia a u.
4. u riceve la notizia: ora esiste un cammino verso z che costa meno di infinito, passando per x ($D_u(z) = c(u,x) + D_x(z) = 1 + 3$).

Lo stesso processo avviene per tutti i nodi e cammini della rete.

### Complessità, pro e contro

A ogni aggiornamento del costo di un nodo, tutti i nodi rivalutano i propri archi, quindi la complessità è **quadratica nel caso peggiore**. Il vantaggio principale è che l'algoritmo è **asincrono**: i router possono adattarsi online, in qualunque fase, a costi aggiornati. I contro riguardano invece la **convergenza lenta**, poiché gli aggiornamenti si diffondono lentamente e tutti i nodi devono rilevare il cambiamento e comunicarlo agli adiacenti, e il **count-to-infinity**: i miglioramenti sono riconosciuti e adottati subito, ma i guasti vengono rilevati lentamente e possono produrre **loop**.

## Il problema del count-to-infinity

Il problema nasce dalla natura **locale** dell'algoritmo DV, che è però anche la sua forza. Il vettore locale $D_x(y)$ è calcolato direttamente dai vettori degli altri nodi ($D_v(y)$), ma non c'è alcuna indicazione su quali nodi si trovino nei cammini migliori scelti dai nodi adiacenti. Ne deriva la domanda cruciale: posso essere sicuro di non essere nel "miglior cammino" dei miei vicini?

### Esempio semplificato

Il link x-y subisce un improvviso **aumento di costo**, e **solo y se ne accorge**. Nella situazione iniziale, con c(x,y) = 4, i vettori sono:

- $D_y(x) = 4$, $D_y(z) = 1$;
- $D_x(y) = 4$, $D_x(z) = 4 + D_y(z) = 5$;
- $D_z(x) = 1 + D_y(x) = 5$, $D_z(y) = 1$.

I passi successivi mostrano il loop:

1. y rileva l'aumento e aggiorna il vettore verso x:

$$D_y(x) = \min\{60,\ 1 + D_z(x)\} = 1 + D_z(x) = 6$$

2. Poiché il vettore $D_y(x)$ è usato da z per calcolare il cammino verso x, anche $D_z(x)$ va aggiornato: $D_z(x) = 1 + D_y(x) = 7$.
3. A sua volta, $D_z(x)$ è usato da y per il proprio calcolo, quindi $D_y(x)$ va aggiornato di nuovo: $D_y(x) = 1 + D_z(x) = 8$.
4. Si instaura così un **loop**: i due vettori vengono aggiornati in continuazione, con distanze che crescono (5, 6, 7, 8, 9...) finché non si raggiunge una configurazione stabile alla convergenza.

### Come evitarlo

Il problema si sarebbe evitato se anche **x avesse notato e comunicato** il cambio di costo del link x-y. Se x è malfunzionante o in ritardo — ad esempio, costi alti dei link di x possono indicare un suo malfunzionamento — la convergenza richiede tempo. Quando invece x rileva il cambiamento, la convergenza è corretta:

$$\begin{aligned}
D_y(x) &= \min\{c(y,x),\ c(y,z) + D_z(x)\} = 1 + 50 = 51 \\
D_y(z) &= \min\{c(y,z),\ c(y,x) + D_x(z)\} = 1 \\
D_x(y) &= \min\{c(x,y),\ c(x,z) + D_z(y)\} = 50 + 1 = 51 \\
D_x(z) &= \min\{c(x,z),\ c(x,y) + D_y(z)\} = 50 \\
D_z(x) &= \min\{c(z,x),\ c(z,y) + D_y(x)\} = 50 \\
D_z(y) &= \min\{c(z,y),\ c(z,x) + D_x(y)\} = 1
\end{aligned}$$