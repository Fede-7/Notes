# Lezione 15 Network Layer

## Dal trasporto alla rete

Il compito del livello di rete è permettere la comunicazione tra **host remoti**:

- Sull'host mittente: prende i segmenti dal livello trasporto, **incapsula** ciascuno in un **datagram** e spedisce i datagram nella rete.
- Sull'host ricevente: riceve i datagram, **estrae** i segmenti e li consegna al livello trasporto.

A questo livello lavorano alcuni dei protocolli più importanti (IP, DHCP, NAT, ecc.) e dispositivi speciali, i **router**, che inoltrano i datagram ai nodi adiacenti fino all'host destinatario.

- I router sono mostrati con uno **stack di protocolli troncato**: in linea di principio non eseguono applicazioni né protocolli di trasporto.
- Il reindirizzo di un datagram da parte di un router è detto **hop**.

## Il servizio di Internet best-effort

Il livello di rete è responsabile della consegna **host-to-host**. Servizi che potrebbero essere offerti insieme alla consegna:

- **Consegna garantita**: un pacchetto spedito arriva prima o poi a destinazione.
- **Consegna garantita con ritardo limitato**: consegna entro un tetto di ritardo host-to-host (es. 100 ms).
- **Consegna in ordine**: i pacchetti arrivano nell'ordine di invio.
- **Banda minima garantita**: possibilità di specificare un bit rate minimo (es. 1 Mbps) al di sotto del quale la consegna è garantita.
- **Sicurezza**: cifratura/decifratura di tutti i datagram a sorgente e destinazione.

> [!info] Best-effort
> **In pratica nessuno** di questi servizi è offerto: la rete Internet fornisce **un solo servizio**, il **best-effort** — la rete fa del suo meglio per consegnare il pacchetto, senza garanzie di ordine, di consegna, di ritardo o di banda minima.

Nonostante la semplicità, il modello best-effort combinato con buona banda si è dimostrato **adeguato** per applicazioni come Netflix, voice-and-video-over-IP, conferenze real-time, ecc.

## Router e piani di lavoro

Il ruolo primario del livello di rete è muovere pacchetti da un host mittente a uno ricevente; lo fanno i **router**, nodi con più link in entrata e uscita, che forniscono due funzioni:

- **Forwarding**: quando un pacchetto arriva sul link di ingresso, il router lo sposta sul link di uscita appropriato. Azioni ulteriori possibili:
  1. **Bloccare** un pacchetto (es. da un host malevolo o verso un host vietato).
  2. **Scartare** un pacchetto scaduto.
  3. **Duplicare** il pacchetto e inviarlo su più link in uscita.
  4. **Modificare** il pacchetto (es. per segnalare congestione).
- **Routing**: decidere il percorso (*path*) che i pacchetti seguiranno da mittente a ricevente; gli algoritmi che calcolano i percorsi sono detti **routing algorithms**.

Distinzioni tra router:

- **Edge router**: distribuisce i pacchetti tra una o più reti (es. connette una rete all'ISP); tipologia più comune.
- **Core router**: distribuisce pacchetti **dentro la stessa rete** piuttosto che tra reti diverse; usati nel backbone di Internet per trasferimenti pesanti.

### Data plane e control plane

Il lavoro del router è tipicamente realizzato come processo **a due piani**:

- **Forwarding (data plane)**: azione locale del router, che trasferisce un pacchetto da un'interfaccia di ingresso a quella di uscita appropriata; operazione **veloce** (pochi nanosecondi), tipicamente implementata **in hardware**.
- **Routing (control plane)**: processo a scala di rete che determina i percorsi end-to-end dei pacchetti; processo **lento** (secondi), spesso via software.

Al data plane appartiene la **forwarding table**: tabella che associa indirizzi (di possibili destinazione) a link di uscita; il router inoltra un pacchetto esaminando il valore di uno o più campi della sua header (match) e usando il valore in tabella per scegliere il link di uscita (action).

La creazione delle tabelle di routing/control plane (e quindi della forwarding table) può avvenire in due modi:

- **Decentralizzato**: ogni router ha un componente di routing che comunica con quello degli altri router (approccio storicamente dominante).
- **Centralizzato**: un **controller remoto**, fisicamente separato dai router, calcola le forwarding table e le distribuisce ai router; l'approccio è alla base del **SDN** (*Software-Defined Networking*): il controller è un software centralizzato, anche open source, tipicamente collocato in un data center ad alta affidabilità e ridondanza, gestito dall'ISP o da terzi.

### Componenti di un router

- **Input port** (diverse dalle porte di trasporto): interfacce fisiche di ingresso che operano col livello link del collegamento; consultano la forwarding table (**lookup**) e preparano il switching fabric per la porta di uscita; inoltrano i pacchetti di controllo (informazioni di routing) al processore. Possono variare da decine a centinaia.
- **Switching fabric**: collega le input port alle output port.
- **Output port**: memorizzano i pacchetti ricevuti dal fabric e li trasmettono sul link in uscita; le porte possono essere bidirezionali (ingresso/uscita accoppiati).
- **Routing processor**: esegue i protocolli di routing, mantiene informazioni di stato sui link, calcola/aggiorna la forwarding table.

## Forwarding

> [!info] Indirizzo IP
> **Numero a 4 byte (32 bit)** rappresentato in notazione decimata puntata (es. `192.168.1.1` = `11000000 10101000 00000001 00000001`); nella forwarding table gli IP sono associati a numeri di porta di uscita per il reindirizzo.

Il meccanismo:

- Ricevuto un pacchetto sul link, sulla input port si esegue il **lookup**; ogni porta ha una **copia della forwarding table** (ricevuta dal processore su un bus dedicato, es. PCI), per evitare il collo di bottiglia di interrogare il processore centralizzato a ogni pacchetto.
- Più indirizzi possono essere associati alla stessa porta, e le voci possono **non** escludersi a vicenda (un IP può corrispondere a più voci): il router applica la regola del **longest prefix matching** (corrispondenza del prefisso più lungo), scegliendo la voce con più bit coincidenti.
- Il lookup è eseguito in hardware il più rapidamente possibile (nanosecondi per trasmissioni Gigabit), con memorie incorporate e algoritmi avanzati di ricerca in tabella.
- Determinata la porta di uscita, il pacchetto attraversa lo switching fabric; in alcuni dispositivi può essere messo in **coda** (bufferato) se altre porte occupano il fabric.

Questa operazione in due passi — cercare l'indirizzo di destinazione (*match*) e inoltrare (*action*) — è detta **match-plus-action**, presente anche in altri dispositivi:

- **Switch**: azione analoga ai router.
- **Firewall**: l'azione è filtrare pacchetti in arrivo specifici.
- **NAT**: l'azione è riscrivere il numero di porta di specifici pacchetti prima di inoltrarli.

## Switching fabric

Lo switching può avvenire in tre modi:

1. **Via memoria**: le porte sono viste come dispositivi di I/O che scrivono i pacchetti in celle di memoria; il processo di routing copia il messaggio sulla porta di uscita indicata dalla forwarding table. Approccio lento (accessi alla memoria), tipico dei primi router (calcolatori standard).
2. **Via bus**: la porta di ingresso trasferisce il pacchetto direttamente sulla porta di uscita attraverso un bus **condiviso**, senza l'intervento del processore; una sola porta per volta è servita, ma il metodo basta per router in aree locali piccole.
3. **Via interconnection network**: porte di ingresso/uscita connesse da una rete con punti di incrocio (*cross-point*) che aprono/chiudono e reindirizzano i pacchetti; più pacchetti possono essere inoltrati **in parallelo**; usato in molti router moderni.

## Code e scheduling dei pacchetti

Poiché lo switching richiede tempo, le porte di ingresso e uscita hanno **code** per memorizzare temporaneamente i pacchetti (come auto al semaforo); l'entità dell'accodamento dipende dal carico di traffico, dalla velocità del fabric e dalla velocità delle linee.

Con un router a N porte, tutte le linee con velocità $R_{line}$ pacchetti/s e ricezione simultanea:

- Se $R_{switch} \cong N \cdot R_{line}$: accodamento **trascurabile sulle porte di ingresso**, ma **significativo sulla porta di uscita** nel caso peggiore (tutti i pacchetti diretti alla stessa porta: il traffico in arrivo è N volte la velocità del link di uscita).
- Se $R_{line} < R_{switch} < N \cdot R_{line}$: accodamento **su entrambe** le porte (l'ingresso aspetta il fabric, l'uscita aspetta il link).
- Se $R_{switch} \cong R_{line}$: accodamento trascurabile in uscita ma **significativo sulle porte di ingresso**.

Con più pacchetti diretti a una singola porta di uscita, l'accesso al link va **pianificato**; tre approcci tipici:

- **FIFO** (*First-Come-First-Served*, o *first-in-first-out*): selezione temporale semplice; se il link di uscita è occupato i pacchetti in arrivo vengono bufferati; se lo spazio è insufficiente si applica una politica di scarto, tipicamente **drop-tail** (si scartano i pacchetti appena arrivati; approcci più sofisticati possono rimuovere pacchetti già in coda); un pacchetto esce dalla coda solo dopo essere stato trasmesso integralmente sul link.
- **Priority queuing**: i pacchetti sono classificati all'arrivo (es. per porte TCP/UDP) in **classi di priorità**; l'operatore può dare priorità a pacchetti specifici (gestione di rete, voice-over-IP) sul traffico utente; ogni classe ha la propria coda, si trasmette prima la classe non vuota più prioritaria e, dentro la stessa classe, in stile FIFO.
- **Round-robin**: i pacchetti sono ordinati in classi, ma le classi si **alternano** invece che essere scelte per priorità; un'implementazione comune è il **WFQ** (*weighted fair queuing*): ogni classe ha un **peso** che detta il ritmo con cui la classe è selezionata rispetto alle altre.