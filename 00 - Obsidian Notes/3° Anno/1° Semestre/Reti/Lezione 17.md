# Lezione 17: Livello di rete — gestione degli indirizzi

## Ripasso

Il livello di rete svolge soprattutto la **consegna host-a-host**: incapsulare i segmenti in datagram e decapsularli, oltre a **identificare gli host (indirizzi)** e **inoltrare** i messaggi verso l'host desiderato. Dentro la rete ci sono **nodi che inoltrano i datagram ai nodi adiacenti** (router), con più **porte in ingresso/uscita**, un **modulo di switching** che collega le porte e un **processore di controllo** che crea le **forwarding table**.

## Internet Protocol (IP)

L'**Internet Protocol (IP)** è il protocollo di livello rete che garantisce la consegna host-a-host; ne esistono due versioni in uso: **IPv4**, la più usata e comune, e **IPv6**, versione più recente proposta per sostituirla. La funzionalità più importante di IP è **identificare gli host** sulla rete (IP addressing): l'**IP addressing** è il processo di assegnare indirizzi IP ai dispositivi, che è **cruciale** e in Internet è piuttosto **complesso** (milioni o miliardi di host).

### Indirizzi IPv4

Gli indirizzi IP si scrivono in **notazione decimale puntata** (*dotted-decimal*): ogni byte in forma decimale, separato da punti.

| | Decimale puntata | Binario |
| --- | --- | --- |
| Indirizzo IP | 193.32.216.9 | 11000001 00100000 11011000 00001001 |

Ogni dispositivo nella rete globale deve avere un **IP globalmente univoco**. Un IP è lungo **32 bit (4 byte)**, quindi in totale esistono $2^{32}$ (circa 4 miliardi) di indirizzi possibili. Host e dispositivi sono connessi tramite **link** (cablati o wireless): un host ha tipicamente un solo link, mentre un dispositivo di rete (es. router) **può averne più di uno**. Il confine tra host e link fisico si chiama **interfaccia**; poiché ogni host e router invia e riceve datagram, IP richiede che **ogni interfaccia abbia il proprio IP**: un **indirizzo IP è tecnicamente associato all'interfaccia**, non all'host o al router che la contiene.

## Subnetting

Assegnare indirizzi IP **non è banale**: sarebbe imprudente assegnarli a caso, perché gli IP non dicono nulla sulla posizione (non sapremmo dove trovare gli host) e servirebbero **forwarding table enormi** nei router. L'indirizzamento assomiglia a quello *telefonico*: **le reti sono divise gerarchicamente in sotto-reti (subnet)** con prefissi diversi. Un IP si divide in **due parti**: la prima (a sinistra) identifica la **subnet** a cui il nodo è connesso, la seconda (a destra) identifica la **singola interfaccia**; il numero di bit di ciascuna parte **non è fisso**.

### Subnet mask

Per distinguere la parte di subnet da quella di interfaccia si usa una **subnet mask** che specifica quali bit appartengono alla subnet:

| | Decimale puntata | Binario |
| --- | --- | --- |
| Indirizzo IP | 193.32.216.9 | 11000001 00100000 11011000 00001001 |
| Subnet mask | 255.255.255.0 | 11111111 11111111 11111111 00000000 |

Un'altra notazione comune è quella **con slash**: `193.32.216.0/24` indica l'IP della subnet, dove /24 dice che i 24 bit più a sinistra sono dedicati alla subnet. La mask individua un prefisso, quindi gli "1" devono essere **i più a sinistra e contigui**:

| Decimale puntata | Binario | |
| --- | --- | --- |
| 255.255.255.0 | 11111111 11111111 11111111 00000000 | SUBNET MASK (/24) |
| 255.255.128.0 | 11111111 11111111 10000000 00000000 | SUBNET MASK (/17) |
| 255.224.0.0 | 11111111 11100000 00000000 00000000 | SUBNET MASK (/11) |
| 255.255.10.0 | 11111111 11111111 00001010 00000000 | NON È UNA MASK |
| 63.255.255.0 | 00111111 11111111 11111111 00000000 | NON È UNA MASK |

### Stessa subnet o no?

Due host sono sulla stessa subnet se i loro **prefissi di subnet coincidono**. Esempi:

| IP 1 | Subnet mask | IP 2 | |
| --- | --- | --- | --- |
| 231.23.11.117 | 255.255.255.0 | 231.23.11.9 | STESSA SUBNET |
| 10.54.32.1 | 255.255.128.0 | 10.54.60.203 | STESSA SUBNET |
| 110.32.100.10 | 255.224.0.0 | 110.64.100.11 | SUBNET DIVERSE |
| 121.50.79.4 | 255.0.0.0 | 121.10.36.240 | STESSA SUBNET |
| 121.50.79.4 | 255.0.0.0 | 120.50.79.5 | SUBNET DIVERSE |

Host di subnet diverse **possono comunque comunicare**, ma gli amministratori possono trattare i messaggi in ingresso/uscita in modo diverso (es. bloccarli/filtrarli).

### Router e subnet

Il dispositivo che interconnette subnet diverse è il **router**: ha **più porte fisiche**, legate a **interfacce di rete diverse** con IP diversi. I router sono spesso al confine tra più subnet, gestendo i messaggi in ingresso/uscita (**gateway**). Grazie a questa posizione privilegiata, **i router offrono spesso più servizi** oltre al routing: IP masquerading (NAT), assegnazione dinamica degli IP (DHCP) e protezione (firewall).

### Esempi

Un router con tre interfacce interconnette 7 host, divisi in 3 subnet (sinistra, destra, sotto), ognuna collegata a un'interfaccia. La subnet di sinistra ha indirizzo 223.1.1.0/24, quindi tutte le interfacce hanno IP nella forma 223.1.1.XXX (223.1.1.1, 223.1.1.2, 223.1.1.3 per gli host, 223.1.1.4 per il router); le altre due subnet sono 223.1.2.0/24 e 223.1.3.0/24. Con **3 router** interconnessi da link punto-punto, ognuno con **3 interfacce** (una per link punto-punto, una per il link broadcast verso i suoi host), si ottengono **6 subnet**: 223.1.1.0/24 (R1-host), 223.1.2.0/24 (R2-host), 223.1.3.0/24 (R3-host), 223.1.9.0/24 (R1-R2), 223.1.8.0/24 (R2-R3) e 223.1.7.0/24 (R3-R1). Tipicamente le organizzazioni medie/grandi (aziende, atenei) hanno più subnet interconnesse.

### ifconfig

Su Linux si controlla il proprio indirizzo con `ifconfig` (equivalente Windows: `ipconfig`): `ifconfig` (*interface configuration*) elenca tutte le interfacce di rete della macchina con la loro configurazione (indirizzi, mask, ecc.); esistono anche comandi moderni come `ip`. Uso: `$ ifconfig`

```
eth0  Link encap:Ethernet  Hwaddr 00:0F:20:CF:8B:42
      inet addr:217.149.127.10  Bcast:217.149.127.63  Mask:255.255.255.192
      UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
      RX packets:2472694671 errors:1 dropped:0 overruns:0 frame:0
      TX packets:44641779 errors:0 dropped:0 overruns:0 carrier:0
      ...
```

## Indirizzamento in Internet

Spezzare reti grandi in reti più piccole è **particolarmente importante** su Internet, dove si collegano miliardi di dispositivi. Su Internet gli IP **vanno assegnati con cura** per evitare **forwarding table** dei router troppo grandi, interfacce diverse con **lo stesso indirizzo** e l'esaurimento degli indirizzi. L'approccio è dividere gli indirizzi **fornendo subnet alle organizzazioni** (ISP, aziende, istituzioni), in due modi: il **classful addressing** (vecchio, non più usato in pratica) e il **classless addressing** (attuale).

### Classful addressing

Gli indirizzi erano divisi in classi:

| | Formato | Esempio | IP per rete |
| --- | --- | --- | --- |
| Classe A | a.b.c.d/8 | 10.X.X.X | > 16 milioni |
| Classe B | a.b.c.d/16 | 10.10.X.X | 65535 |
| Classe C | a.b.c.d/24 | 10.10.10.X | 254 |

Se servivano 300 IP si assegnava **una classe B intera** (es. 241.115.0.0) con tutti i suoi IP. Il problema è evidente: servono solo 300 IP e **gli altri 65335 sono sprecati!**

### Classless addressing (CIDR)

L'approccio moderno, più flessibile, è il **Classless InterDomain Routing (CIDR)**: un'organizzazione può ricevere indirizzi di qualunque forma `a.b.c.d/X`. Se servono 300 IP si assegna a.b.c.d/23 (es. 241.115.2.0/23), che **fornisce 512 IP sprecandone solo 212**. Negli indirizzi "CIDRizzati" la parte di rete si chiama **prefisso** e l'insieme di IP riservati all'organizzazione si chiama **blocco**. I blocchi possono sovrapporsi, e in tal caso la lunghezza (X) del prefisso discrimina i blocchi: ad esempio l'IP 10.10.10.15/16 non è nello stesso blocco di 10.10.10.14/24. È inoltre possibile creare **subnet interne** a un blocco CIDR: il blocco 241.115.0.0/16 si può decomporre in 241.115.1.0/24, 241.115.2.0/24, 241.115.3.0/24, ecc.

### Aggregazione degli indirizzi

L'indirizzamento a prefissi è utilissimo per i dispositivi che connettono prefissi diversi: un router può ricordare (nella forwarding table) **solo i prefissi**, e ricevuto un messaggio con un certo prefisso lo inoltra a un router più specifico, e così via. Questo approccio si chiama **address aggregation** (o *route summarization*), ed è più efficace finché i blocchi sono **raggruppati (clustered)**.

### Ottenere un blocco

Per **ottenere un blocco di IP** per la subnet di un'organizzazione ci sono due modi: contattare un **ISP**, che fornisce indirizzi da un blocco più grande già allocatogli (es. l'ISP può aver ricevuto 200.23.16.0/20, suddiviso in sotto-blocchi di dimensione variabile secondo la sua politica), oppure chiedere alla **Internet Corporation for Assigned Names and Numbers (ICANN)**, autorità globale no-profit che gestisce lo spazio degli indirizzi IP allocando blocchi agli ISP; ICANN gestisce anche i root server DNS, assegnando nomi di dominio e risolvendo le dispute.

## Il datagram IPv4

Il pacchetto di livello rete di Internet si chiama **datagram** (come in UDP). I campi chiave sono:

- **Version** (4 bit): la **versione di IP** (v4 o v6); il formato dipende dalla versione.
- **Header length** (4 bit): **dimensione dell'header** (non fissa, opzioni a dimensione variabile); serve a sapere dove inizia il payload (senza opzioni l'header è 20 byte).
- **Type of Service (TOS, 8 bit)**: **proprietà** specifiche del datagram (es. real-time/non-real-time); i tipi sono **definiti dagli amministratori di rete** dei router.
- **Datagram length** (16 bit): lunghezza in **byte del datagram** (header + dati); raramente oltre 1500 byte (su 65535 max).
- **Identifier** (16 bit): numero progressivo che identifica univocamente un datagram (usato nella frammentazione).
- **Flags + fragmentation offset** (3+13 bit): proprietà e offset del frammento (usati nella frammentazione).
- **Time-to-live (TTL, 8 bit)**: garantisce che i datagram **non girino per sempre** nella rete; è decrementato di 1 a ogni router e a 0 il datagram va scartato.
- **Upper-layer protocol** (8 bit): il **protocollo di trasporto** cui passare il payload (es. 6 per TCP, 17 per UDP).
- **Header checksum** (16 bit): rilevamento errori, calcolato come complemento a 1 della somma a 2 byte dell'header. **I router verificano** il valore e **i datagram errati sono tipicamente scartati**; il checksum va **ricalcolato e ri-memorizzato a ogni router**, perché TTL e opzioni possono cambiare.
- **Indirizzi IP sorgente e destinazione** (32+32 bit).
- **Options** (dimensione variabile): estendono l'header IP (**funzionalità aggiuntive**); aggiungono complessità (dimensione sconosciuta) e **non esistono in IPv6**.
- **Data**: il **messaggio effettivo (payload)**, tipicamente un segmento TCP/UDP.

## Frammentazione IPv4

I datagram IP possono essere **frammentati a livello di link**, perché alcuni protocolli di collegamento trasportano datagram di **dimensioni diverse** (es. i frame Ethernet trasportano al massimo 1500 byte di dati). I datagram IP sono incapsulati in frame di livello link per essere trasportati di nodo in nodo, e la quantità massima di dati che un frame può trasportare è la **MTU** (*Maximum Transmission Unit*). Un router che interconnette due link con MTU diverse **può ricevere un datagram dall'input che non entra nel link di output**: in tal caso **il router deve dividere il payload** del datagram in due o più datagram IP più piccoli (**frammenti**), che sono **incapsulati in frame di livello link** e inoltrati.

Quando un router frammenta un datagram, copia in ogni frammento **lo stesso identificatore, indirizzo sorgente e destinazione**, imposta il campo **fragment offset** di tutti i frammenti a numeri progressivi, e imposta il flag dell'**ultimo frammento** a 1 (segnalando che i frammenti sono finiti). I frammenti vanno **riassemblati prima di arrivare al livello di trasporto** a destinazione, perché TCP e UDP si aspettano segmenti completi dal livello di rete. I progettisti di IPv4 ritenevano che riassemblare nei router avrebbe complicato il protocollo e rallentato i router, quindi in IPv4 il **riassemblaggio avviene nei sistemi finali**: se arrivano più datagram con **stessi indirizzi e identificatore**, il datagram originale era frammentato e l'host deve **ricostruire il datagram originale** dai frammenti.