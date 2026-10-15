# Lezione 24 — Il Link Layer: CSMA/CD, switch, ARP, frame Ethernet

## CSMA e collisioni (seguito)

Anche con il carrier sensing le collisioni avvengono per il **ritardo di propagazione del segnale**: la propagazione, pur prossima alla velocità della luce, impiega tempo; un secondo nodo rileva la trasmissione solo dopo il suo inizio e nel frattempo può considerare libero un canale in uso.

### Pure CSMA

Molto semplice:

```text
1. Controlla se il canale è occupato.
2. Se il canale è libero, invia un frame.
```

Le collisioni **non vengono rilevate** ma restano possibili: si capisce che un frame è perso solo perché **non arriva l'ACK**.

### CSMA/CD (attuale implementazione Ethernet)

Più sofisticato:

```text
1. Controlla se il canale è occupato.
2. Se il canale è libero, invia un frame.
3. Mentre trasmetti, controlla eventuali collisioni.
4. Se rilevi una collisione, interrompi la trasmissione
   e attendi un periodo casuale K ∈ {0, ..., 2^n - 1}
   dove n è il numero di collisioni rilevate sul frame corrente
   (binary exponential backoff).
```

> [!def] Binary exponential backoff
> L'intervallo del ritardo casuale **raddoppia a ogni collisione** ($K \in \{0,\dots,2^n-1\}$ con $n$ = numero di collisioni sul frame): la probabilità di trasmettere con successo **cresce** con il numero di collisioni subite.

## Protocolli taking-turns

### Polling protocol

- Un **nodo master** seleziona a **round-robin** un nodo per volta, autorizzato a trasmettere (fino al massimo throughput).
- Il processo si ripete ogni volta che la trasmissione si ferma (es. **Bluetooth**).
- ✔ Nessuna collisione.
- ✘ Esiste un **polling delay** (tempo per selezionare i nodi) e l'approccio è **centralizzato**: singolo punto di guasto.

### Token-passing protocol

- Non c'è un master: i nodi si passano un frame speciale, il **token**; chi riceve il token è autorizzato a trasmettere, poi lo passa ad altro nodo.
- ✔ Nessuna collisione; approccio **decentralizzato**.
- ✘ Problemi se un nodo "dimentica" di rilasciare il token (**monopolizzando il link**).

## Indirizzi MAC

A livello link i dispositivi sono identificati dagli **indirizzi MAC**:

- ogni interfaccia di rete ha il suo MAC address (progettato come fisso, ma modificabile);
- ogni produttore ha il proprio insieme di MAC;
- l'indirizzo MAC (o *physical address*) è composto da **6 byte** ($2^{48}$ indirizzi), spesso in notazione esadecimale: `1A:23:F9:CD:06:9B` o `1A-23-F9-CD-06-9B`;
- gli indirizzi MAC sono **locali** (usati solo dentro la LAN), mentre gli IP fuori dalla LAN sono globali.

### Comunicazione in una LAN

Per far comunicare le interfacce A e B:

1. A inserisce il MAC di B nel frame e lo trasmette;
2. B riceve il frame e **confronta il MAC destinazione con il proprio**;
3. se coincidono, il frame è accettato; altrimenti è **rifiutato** (il resto dello stack non è coinvolto).

> [!info] Broadcast
> Per LAN con indirizzi a 6 byte (Ethernet, 802.11) l'indirizzo di broadcast è una stringa di **48 uni consecutivi**: `FF-FF-FF-FF-FF-FF`. I frame broadcast sono accettati da qualunque interfaccia.

In una LAN è frequente ricevere frame diretti ad altri: il ruolo del MAC è **filtrare i frame non intesi** senza disturbare l'host.

## Switch

> [!def] Switch
> Controparte di livello link dei router. Riceve i frame in ingresso e li inoltra sui link in uscita. Caratteristiche: **nessun algoritmo di routing**, usa **solo indirizzi MAC** (non gli IP), è **trasparente** agli host e ai router della subnet, ha buffer sulle interfacce.

Le switch hanno **tabelle di inoltro** che associano MAC → interfaccia, aggiornate **automaticamente e dinamicamente** (*self-learning*) man mano che si scoprono nuovi dispositivi.

### Switched LAN

Le LAN usano tipicamente uno o più switch per collegare i dispositivi locali. Rispetto ai router, gli switch sono **veloci e plug-and-play**:

- nessun algoritmo di routing coinvolto;
- considerano solo 2 livelli dello stack.

D'altro canto le switched LAN sono **limitate in dimensione** e con struttura **ad albero**:

- i MAC sono difficili da raggruppare → le tabelle di inoltro crescono rapidamente;
- non c'è routing → i **loop** sono difficili da evitare.

## ARP (Address Resolution Protocol)

I protocolli di livello superiore lavorano con **indirizzi IP**: serve tradurre IP in MAC.

> [!def] ARP
> L'**Address Resolution Protocol** gestisce la conversione IP ↔ MAC. Ogni interfaccia ha un modulo ARP con una **tabella ARP** che associa ogni IP della LAN al MAC corrispondente, con un **TTL** dopo il quale la voce è cancellata (tipicamente 5–20 minuti). Essendo i MAC locali, **ARP funziona solo su reti locali (LAN)**.

| IP Address | MAC Address | TTL |
| --- | --- | --- |
| 222.222.222.221 | 88-B2-2F-54-1A-0F | 13:45:00 |
| 222.222.222.223 | 5C-66-AB-90-75-B1 | 13:52:00 |

### Richiesta e risposta

Se l'IP del destinatario non è in tabella:

1. si invia in **broadcast** un pacchetto di **"ARP request"** a tutti i dispositivi della rete, cercando il giusto IP;
2. **tutti** i nodi lo ricevono, ma risponde solo il nodo con l'IP cercato, con un messaggio diretto di **"ARP reply"** (unicast).

> [!warning] ARP poisoning
> Un host malevolo può **intercettare la richiesta** e rispondere con un reply **"falsificato"**: una delle tecniche d'attacco più comuni sulle LAN.

### Oltre la rete locale (gateway)

Se l'IP destinatario è **fuori dalla rete**, il router che collega le due reti deve avere **almeno 2 interfacce** (2 IP, 2 MAC, 2 tabelle ARP), ciascuna dentro la propria subnet. I frame diretti fuori dalla subnet vengono:

1. inviati alla **prima interfaccia del router**;
2. spostati alla **seconda interfaccia**;
3. instradati verso l'host giusto usando la **seconda tabella ARP**.

## Frame Ethernet

| Campo | Dimensione | Contenuto |
| --- | --- | --- |
| Data | 46–1500 byte | Il datagramma IP; il limite è la **MTU** di Ethernet (datagrammi più grandi vengono frammentati) |
| Destination address | 6 byte | MAC dell'adattatore di destinazione |
| Source address | 6 byte | MAC dell'adattatore che trasmette il frame sulla LAN |
| Type | 2 byte | Protocollo di network layer del contenuto (es. ARP ha tipo `0x0806`) |
| CRC | 4 byte | Numero CRC |
| Preamble | 8 byte | Blocco di bit di "sveglia" per sincronizzare gli orologi degli adattatori di destinazione e sorgente |