# Lezione 15: Il livello di rete

## Dal trasporto alla rete

Il compito del livello di rete è permettere a host remoti di comunicare: l'**host mittente** prende i segmenti dal livello di trasporto, **li incapsula in datagram** e li invia in rete, mentre l'**host ricevente** riceve i datagram, **ne estrae i segmenti di trasporto** e li passa al livello superiore. A questo livello lavorano alcuni dei protocolli più importanti (**IP, DHCP, NAT**, ecc.) e dispositivi dedicati, i **router**. Dentro la rete ci sono **nodi che inoltrano i datagram ai nodi adiacenti** (router) fino all'host di destinazione; i router hanno uno **stack di protocolli troncato** e potenzialmente non eseguono né applicazioni né protocolli di trasporto. Il reindirizzamento di un datagram da parte di un router si chiama **hop**.

## Il livello di rete in Internet

Il livello di rete è responsabile della **consegna host-a-host**. I servizi che si potrebbero offrire insieme alla consegna sono: *consegna garantita* (un pacchetto inviato prima o poi arriva a destinazione), *consegna garantita con ritardo limitato* (entro un limite, es. 100 ms), *consegna in ordine*, *banda minima garantita* (possibilità di specificare un bit rate minimo tale che, se la velocità del mittente resta entro quel limite, tutti i pacchetti sono consegnati) e *sicurezza* (cifratura/decifratura dei datagram alla sorgente/destinazione).

In realtà **nessuno di questi servizi** è generalmente offerto dalle reti: il livello di rete di Internet fornisce **un solo servizio**, il **best-effort**, con cui la rete **fa del suo meglio** per consegnare un pacchetto dalla sorgente alla destinazione, senza garanzia di ordine né di consegna, e senza garanzie su ritardi o banda minima. Nonostante la semplicità, il best-effort **combinato con buona banda si è dimostrato adeguato**: Netflix, voice/video-over-IP, videoconferenze in tempo reale e Matrix funzionano tutti così.

## I router

Il ruolo primario del livello di rete è **la consegna host-a-host**, svolta dai **router**: nodi speciali con **più link in ingresso/uscita**, che forniscono due funzioni. Il **forwarding** consiste nello spostare, quando un pacchetto arriva sul link di input, il pacchetto sul link di output appropriato; è anche possibile **bloccare** un pacchetto (es. da/verso host malevoli o vietati), **scartare** un pacchetto scaduto, **duplicare** un pacchetto e inviarlo su più link, o **modificarlo** (es. per notificare congestione). Il **routing** consiste invece nel **decidere il cammino** seguito dai pacchetti da mittente a ricevente; gli algoritmi che calcolano i cammini si chiamano **algoritmi di routing**.

### Tipi di router

I router sono molto **diversi** per uso e tecnologia: domestici o aziendali, wireless o cablati. Una distinzione importante è quella tra **edge router**, che distribuiscono pacchetti tra reti diverse (es. collegano una rete all'ISP) e sono la tipologia più comune, e **core router**, che distribuiscono pacchetti **dentro la stessa rete** e sono usati **sul backbone di Internet** per trasferimenti di dati pesanti.

### Piano dati e piano di controllo

Il lavoro dei router è tipicamente un processo **a due piani**. Il **forwarding** (piano dati) è un'azione **locale al router**, che trasferisce un pacchetto da un'interfaccia di input all'output appropriata: è un'operazione **veloce** (pochi nanosecondi), tipicamente implementata in hardware. Il **routing** (piano di controllo) è invece un processo **a livello di rete** che determina i cammini end-to-end: un processo **più lento** (secondi), spesso implementato via software.

Nel piano dati c'è la **forwarding table**: una tabella che associa link di output a possibili indirizzi di destinazione. Il router inoltra un pacchetto **esaminando il valore di uno o più campi dell'header**, e il valore nella forwarding table indica **l'interfaccia in uscita**. Poiché si attraversano più router, il contenuto della forwarding table è determinato **raccogliendo informazioni da router diversi**, tramite le **tabelle di routing** (piano di controllo) che portano alla creazione della forwarding table (piano dati). La creazione delle tabelle avviene in due modi:

- **Decentralizzato (distribuito)**: ogni router ha un componente di routing che comunica con i componenti degli altri router (approccio dominante storicamente).
- **Centralizzato**: un controller remoto, fisicamente separato dai router, calcola e distribuisce le forwarding table.

Nel caso centralizzato il controller può stare in un **data center remoto** (con alta affidabilità e ridondanza), gestito dall'ISP o da terzi. Questo approccio è alla base del **software-defined networking** (SDN): la rete è "definita via software" perché il controller è un software centralizzato (a volte open source).

### Componenti principali di un router

- **Porte di input** (diverse dalle "porte" di trasporto): le **interfacce fisiche di input**, che operano con il livello di collegamento del link connesso. Devono consultare la forwarding table (**lookup**) e preparare lo switching fabric per la porta di output, e **inoltrare i pacchetti di controllo** (es. con informazioni di routing) al processore di routing. Le porte vanno da decine a centinaia (es. Juniper MX2020 supporta fino a 960 porte Ethernet da 10 Gbps).
- **Switching fabric**: collega le porte di input alle porte di output.
- **Porte di output**: memorizzano i pacchetti ricevuti dallo switching fabric e li trasmettono sul link in uscita; le porte possono essere **bidirezionali** (input/output accoppiati).
- **Processore di routing**: esegue i protocolli di routing, mantiene informazioni di stato sui link, calcola/aggiorna la forwarding table.

## Forwarding

La **forwarding table associa indirizzi IP a porte di output**, così i pacchetti sono inoltrati sul link giusto verso il nodo successivo. Un **indirizzo IP è un numero di 4 byte (32 bit)**, di solito in notazione decimale (ma si può vedere anche in binario). Ricevuto un pacchetto su una porta di input si esegue una **lookup**: **ogni porta ha una copia della forwarding table** (dal processore di routing, via bus dedicato, es. PCI), per evitare il collo di bottiglia di invocare il processore centralizzato per ogni pacchetto, e **più indirizzi possono essere associati alla stessa porta**.

Esempio di tabella a 4 porte:

| Prefisso di indirizzi IP | Interfaccia |
| --- | --- |
| 11001000 00010111 00010\*\*\* \*\*\* | 0 |
| 11001000 00010111 00011000 \*\*\* | 1 |
| 11001000 00010111 00011\*\*\* \*\*\* | 2 |
| altrimenti | 3 |

Le voci **non sono mutuamente esclusive** (es. `11001000 00010111 00011000 10101010` corrisponde sia al link 1 che al link 2), quindi il router sceglie la **voce con il prefisso più lungo** (*longest prefix matching*): il match col Link 1 vale 24 bit e il match col Link 2 vale 21 bit, quindi **vince il Link 1**. La lookup è tipicamente eseguita **in hardware**, per essere più veloce possibile (nanosecondi per trasmissioni in Gigabit), e coinvolge memorie incorporate e algoritmi di ricerca avanzati.

Determinata la porta di output, **il pacchetto entra nello switching fabric**; in alcuni dispositivi può essere messo temporaneamente in coda se altre porte stanno usando la fabric. L'operazione in due passi — **cercare l'indirizzo di destinazione (match)** e **inoltrare (action)** — si chiama **match-plus-action**, ed è svolta in molti dispositivi: negli **switch** l'azione è simile ai router, nei **firewall** l'azione è **filtrare** specifici pacchetti in arrivo, nel **NAT** l'azione è **riscrivere il numero di porta** prima dell'inoltro.

## Switching fabric

Lo switching si può fare in tre modi:

1. **Switching via memoria**: le porte sono viste come dispositivi di I/O che scrivono i pacchetti in celle di memoria; il processo di routing copia il messaggio sulla porta di output come indicato dalla forwarding table. È un approccio un po' lento (accesso alla memoria), comune nei primi router (calcolatori normali).
2. **Switching via bus**: la porta di input trasferisce il pacchetto direttamente alla porta di output su un bus condiviso, senza intervento del processore di routing. Solo una porta per volta è servita, ma spesso è sufficiente per router in piccole reti locali.
3. **Switching via interconnection network**: le porte di input/output sono collegate da una rete con punti d'incrocio (*crossbar*) che si aprono/chiudono per reindirizzare i pacchetti. **Più pacchetti possono essere inoltrati in parallelo**; è usato in molti router moderni.

## Code sulle porte

Poiché **lo switching richiede tempo**, le porte di input e output hanno **code per memorizzare temporaneamente i pacchetti** (come auto ai semafori). L'**entità delle code non è fissa**: dipende dal carico di traffico, dalla velocità della fabric e dalla velocità di linea; i pacchetti possono arrivare o partire più velocemente o lentamente dello switching, accumulandosi nei buffer (che possono **traboccare**).

### Scenario worst-case

Si consideri un router con **N porte di input e N di output**, tutte le porte che ricevono pacchetti contemporaneamente, tutte le linee alla stessa velocità $R_{line}$ pacchetti/s, e **tutti i pacchetti che devono andare sulla stessa porta di output**. Con velocità della fabric $R_{switch}$:

- Se $R_{switch} \cong N R_{line}$: **code trascurabili sulle porte di input** (la fabric smista tutto in tempo), ma **code significative sulla porta di output** (i pacchetti in arrivo sono N volte la velocità del link in uscita).
- Se $R_{line} < R_{switch} < N R_{line}$: **code su entrambe** (l'input aspetta la fabric, l'output aspetta il link).
- Se $R_{switch} \cong R_{line}$: **code trascurabili sull'output** ma **significative sulle porte di input**.

## Scheduling dei pacchetti

È ragionevole che **più pacchetti** (anche da più porte) debbano uscire **dalla stessa porta di output**: l'accesso dei pacchetti in coda al link di output va quindi **pianificato (scheduled)**. Tre approcci celebri sono il **First-come-first-served (FCFS / FIFO)**, basato sul tempo, il **priority queuing**, basato sull'importanza dei pacchetti, e il **round-robin queuing**, in cui i pacchetti sono divisi in classi e ogni classe è servita a turno.

### FIFO

Se il **link di output è occupato**, i pacchetti in arrivo vanno **bufferizzati**; se **lo spazio di buffer è insufficiente**, serve una **politica di scarto**: tipicamente si scartano i pacchetti appena arrivati (*drop-tail*), mentre in approcci più sofisticati si possono rimuovere anche pacchetti già in coda per far spazio ai nuovi. Un pacchetto esce dalla coda **solo quando è stato trasmesso completamente** sul link in uscita, e nello **scheduling FIFO** i pacchetti sono trasmessi **nello stesso ordine di arrivo**.

### Priority queuing

I pacchetti in arrivo sono **classificati** (es. per porte TCP/UDP) in classi di priorità al loro arrivo in coda. Un **operatore di rete può configurare la coda** così che specifici pacchetti (es. management di rete, voice-over-IP in tempo reale) abbiano priorità sul traffico utente o sui pacchetti non real-time. **Ogni classe di priorità può avere la propria coda**: si trasmettono prima i pacchetti della classe a priorità più alta non vuota, e dentro la stessa classe la scelta è tipicamente **FIFO**.

### Round-robin

Anche nel round-robin i pacchetti sono ordinati in classi, ma **le classi si alternano** anziché essere scelte per priorità. Un'implementazione comune è la **weighted fair queuing (WFQ)**: i pacchetti sono classificati e messi in coda nell'area di attesa appropriata, e ogni classe ha un **peso** che detta la **frequenza con cui la classe è selezionata** rispetto alle altre.