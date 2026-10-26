# Lezione 21 — Il Network Layer: Link-State e confronto DV vs LS

## Algoritmo Link-State (LS)

> [!def] Link-State
> Approccio **centralizzato** che sfrutta la conoscenza **completa** della rete per trovare i percorsi ottimali. Non soffre del problema del **count-to-infinity** ed è basato sull'algoritmo di **Dijkstra**.

La conoscenza globale si ottiene nella pratica facendo **broadcast a tutti i nodi** di *link-state packet* contenenti ID e costi dei link adiacenti. La versione base calcola i percorsi minimi **da un nodo sorgente verso tutte le destinazioni**, quindi va eseguita **su tutti i nodi**.

## Fase di scambio dei messaggi

Prima di calcolare i percorsi minimi, ogni router scopre i nodi circostanti e condivide l'informazione con gli altri, in 4 passi:

1. **Scoperta dei vicini**: il router invia un messaggio *"hello"* su tutti i link; gli altri router rispondono con i loro ID.
2. **Impostazione dei costi**: il router fissa la metrica di distanza verso ciascun vicino (in base ai costi reali: tempo, banda, ecc., o impostata dall'amministratore).
3. **Costruzione del pacchetto**: crea un pacchetto che riassume ID dei nodi adiacenti e i relativi costi.
4. **Scambio dei pacchetti**: invia il pacchetto in broadcast a tutti gli altri router e riceve i loro.

Al termine **ogni router possiede la conoscenza "completa" della topologia** della rete: può eseguire Dijkstra.

## Pseudocodice

```text
LinkState(x):
    N' = {x}
    per ogni nodo v:
        se v è vicino di x:   D(v) = c(x,v)
        altrimenti:           D(v) = ∞

    repeat:
        trova w ∉ N' tale che D(w) è minimo
        aggiungi w a N'
        per ogni vicino v di w non in N':
            D(v) = min( D(v), D(w) + c(w,v) )
    until N' = N
```

- $D(v)$: distanza dal nodo corrente verso tutte le destinazioni; si assume che **tutti i costi siano noti**.
- **Fase di costruzione**: si seleziona il nodo più vicino $w$ non ancora in $N'$, se ne esplora il vicinato controllando se il percorso **attraverso $w$** migliora quello attuale; si esce quando tutti i nodi sono stati esplorati.

### Recupero del percorso

Oltre a $D(v)$ si usa una funzione **$p(v)$** che memorizza il **nodo precedente** a quello selezionato: per ricostruire il percorso basta **risalire i predecessori** a ritroso fino al nodo corrente.

### Esempio di esecuzione (su nodo u)

| step | N' | D(v), p(v) | D(w), p(w) | D(x), p(x) | D(y), p(y) | D(z), p(z) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | u | 2, u | 5, u | 1, u | ∞ | ∞ |
| 1 | ux | 2, u | 4, x | | 2, x | ∞ |
| 2 | uxy | 2, u | 3, y | | | 4, y |
| 3 | uxyv | | 3, y | | | 4, y |
| 4 | uxyvw | | | | | 4, y |
| 5 | uxyvwz | | | | | |

## Complessità, pro e contro

- **Complessità**: a ogni iterazione si controllano tutti i nodi della rete, escludendone poi uno (la sorgente); si rimuove un nodo per iterazione → caso peggiore **$O(n^2)$**. Con strutture dati più sofisticate (es. **heap**) si raggiungono prestazioni migliori, tipicamente $O(n \log n)$.
- **Pro**:
  - **convergenza rapida**: tutte le comunicazioni avvengono simultaneamente;
  - **nessun count-to-infinity**: lo stato di tutti i link viene propagato.
- **Contro**:
  - **sincrono**: i nodi devono ricevere le informazioni dall'intera rete prima di iniziare.

## Distance-Vector vs Link-State

I due algoritmi adottano approcci **complementari**: il DV sfrutta informazione **locale** sui vicini, l'LS richiede informazione **globale** su tutti i nodi.

| Criterio | Distance-Vector | Link-State |
| --- | --- | --- |
| Informazione | Locale (vicini) | Globale (tutti i nodi) |
| Complessità dei messaggi | Comunicazione solo al cambio di un percorso ottimale | Più complesso: serve comunicazione sincrona tra tutti i nodi |
| Convergenza | Lenta; nel frattempo possibili percorsi subottimali; soffre di count-to-infinity | Rapida; nessun count-to-infinity |
| Robustezza | Le computazioni sono a catena: se una tabella è errata, **l'errore si propaga a tutte** | Più robusta: le tabelle sono calcolate separatamente da ogni nodo |

> [!warning] La lezione del 1997
> Un **router malfunzionante di un piccolo ISP** causò una reazione a catena: le sue tabelle corrotte vennero propagate inondando i router di backbone e **disconnettendo parte di Internet per diverse ore** — esempio classico della fragilità del DV.

> [!info] Conclusione
> In Internet **entrambe le soluzioni sono usate**.