# Lezione 22: Livello di collegamento — Framing e gestione degli errori

## Dal livello di rete ai livelli di collegamento e fisico

Il livello di rete fornisce fondamentalmente la comunicazione tra due host, ovunque si trovino, mentre i livelli di collegamento (*link*) e fisico forniscono la comunicazione tra **due host connessi direttamente**. Il **livello di collegamento** è la porzione dello stack dedicata alla trasmissione di pacchetti sui collegamenti (canali di trasmissione), da nodo a nodo della rete; il **livello fisico**, invece, regola la struttura dei collegamenti (mezzo trasmissivo, connettori, tipi di cavo) e il modo in cui i bit sono rappresentati e trasmessi lungo il collegamento. I due livelli sono **strettamente intrecciati** — spesso raggruppati in un unico livello detto *network access* — tanto che alcuni protocolli comuni, come Ethernet, coprono entrambi. A differenza dei livelli precedenti, questi due livelli sono **presenti in ogni componente** dell'infrastruttura di rete: nei nodi (host, router, switch, hub, access point WiFi) e nei collegamenti, sia cablati (rame, fibra ottica) sia wireless (radiofrequenze).

Per trasmettere un datagram IP bisogna trasferirlo dall'host sorgente all'host destinazione "saltando" di collegamento in collegamento lungo il percorso. Poiché ogni collegamento ha un proprio tipo, i **datagram vengono incapsulati in frame del livello di collegamento** specifici del collegamento su cui devono viaggiare. Questa è l'**ultima incapsulazione**: i frame vengono convertiti in segnali — impulsi elettrici, luce o onde radio — e trasferiti sul collegamento secondo la sua specifica. Ad esempio, per raggiungere Internet, i pacchetti di un host wireless devono attraversare 4/5 collegamenti (wireless e cablati), un access point, uno switch e 2/3 router.

## Servizi del livello di collegamento

Il livello di collegamento può offrire fino a quattro servizi, tra loro indipendenti:

1. **Framing**: incapsulare i datagram in frame del livello di collegamento, con il datagram dei livelli superiori come payload e un header/trailer specifici del protocollo; la struttura del frame dipende dai protocolli dei livelli di collegamento e fisico.
2. **Accesso al collegamento** (*link access*): definire le regole che governano l'accesso al collegamento mediante un protocollo **Medium Access Control (MAC)**, in base all'architettura del collegamento. Nei **collegamenti punto-a-punto** (un solo mittente e un solo destinatario) il protocollo MAC è semplice o inesistente, poiché il mittente può inviare un frame quando il collegamento è inattivo; nei **collegamenti broadcast** esiste invece il *problema degli accessi multipli*, e il protocollo MAC serve a coordinare le trasmissioni dei frame dei molti nodi.
3. **Consegna affidabile** (*reliable delivery*): garantire che i frame trasmessi sul collegamento vengano ricevuti. Il servizio è spesso usato su collegamenti soggetti a un alto tasso di errore (es. wireless), con l'obiettivo di correggere l'errore localmente; poiché comporta un forte overhead e altri protocolli (es. TCP) sono già affidabili, non è sempre implementato.
4. **Rilevamento e correzione degli errori**: l'hardware del livello di collegamento può essere soggetto all'**inversione dei bit** (*bit flipping*), quindi molti protocolli implementano strategie di verifica e correzione incorporate nell'hardware, oltre a quelle dei livelli superiori (checksum di TCP e IP). Poiché non esistono ulteriori incapsulamenti, queste verifiche coprono praticamente l'intero messaggio e, essendo incorporate nell'hardware, possono essere molto più rapide.

## Implementazione

Nei dispositivi di rete (sistemi finali, router, ecc.) le funzionalità del livello di collegamento sono implementate sia via software sia, soprattutto, via hardware. Nei computer esistono adattatori di rete detti **Network Interface Card (NIC)**, con un chip specializzato (il **controller**) che implementa le funzionalità del livello di collegamento. Un tempo queste schede erano separate dalla scheda madre e inserite in slot PCI; recentemente l'approccio sta cambiando verso la soluzione LAN-on-motherboard.

### Software

Il software esegue sulla CPU e fornisce le funzionalità di alto livello: indirizzamento, gestione di interrupt e hardware, gestione degli errori, incapsulamento e decapsulamento dei datagram. Al livello di collegamento esiste un indirizzo aggiuntivo, l'**indirizzo MAC**, che identifica la NIC. I datagram devono inoltre essere memorizzati in memoria per essere usati dal protocollo di livello superiore: vengono recuperati dalla memoria durante l'incapsulamento (lato mittente) e inseriti in memoria durante il decapsulamento (lato ricevente).

### Hardware

L'hardware funziona come un tipico dispositivo di I/O, convertendo i dati nel segnale da trasmettere in base al protocollo fisico (Ethernet, wireless, ecc.).

## Tecnologie fisiche

Il protocollo del livello di collegamento, e quindi la struttura del frame risultante, dipende dalla tecnologia del collegamento fisico. Le tecnologie comuni sono tre:

- **Ethernet 802.3**: connessione cablata basata su impulsi elettrici su 4 doppini intrecciati in rame (la più comune) oppure su fotoni tramite cavo in fibra ottica.
- **WiFi 802.11**: connessione wireless basata su radiofrequenza (2,4 GHz, 5 GHz, 6 GHz).
- **Bluetooth**: connessione wireless basata su radiofrequenza (2,4 GHz).

Le tecnologie fisiche evolvono continuamente e i loro limiti in termini di distanza e banda vengono aggiornati spesso; ogni tecnologia ha pro e contro:

| Tipo | Segnale | Distanza | Banda | Criticità |
| --- | --- | --- | --- | --- |
| Wireless | Radio | 30–50 m | 1,3 Gbps | Sicurezza, velocità |
| Doppino in rame | Elettricità | 30–100 m | 1–25 Gbps | Interferenze |
| Fibra ottica | Luce | 100–200 km | 1–400+ Gbps | Fragilità |

## Frame (richiamo)

Il livello di collegamento accetta i pacchetti dal livello di rete, li incapsula in frame e li invia tramite il livello fisico; la ricezione è il processo opposto.

## Metodi di framing

Gli approcci possibili, logici o fisici, sono quattro:

- Conteggio di byte (*byte count*).
- Byte di flag con *byte stuffing*.
- Bit di flag con *bit stuffing*.
- Violazioni della codifica del livello fisico (uso di simboli non-dato per indicare il frame).

### Conteggio di byte (mai usato)

Ogni frame inizia con un **contatore del numero di byte** che contiene. L'approccio è semplice, ma dopo un errore è difficile risincronizzarsi: poiché il ricevitore usa il contatore per delimitare i frame, se il contatore viene corrotto perde l'allineamento anche sui frame successivi.

### Byte stuffing

Un **byte di flag speciale** delimita i frame, e le occorrenze del flag nei dati devono essere "riempite" o mascherate (*stuffed*) tramite byte di escape. I frame risultano più lunghi, ma dopo un errore è facile risincronizzarsi, perché il ricevitore cerca semplicemente il flag successivo.

Formato del frame:

| FLAG | Header | Campo payload | Trailer | FLAG |
| --- | --- | --- | --- | --- |

Esempi (ESC = byte di escape):

| Byte originali |  |  | → | Byte dopo stuffing |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | FLAG | B | → | A | ESC | FLAG | B |
| A | ESC | B | → | A | ESC | ESC | B |
| A | ESC | FLAG | B | → | A | ESC | ESC | ESC | FLAG |

### Bit stuffing

Il flag del frame è la sequenza di **sei 1 consecutivi** (`01111110`). In trasmissione, dopo **cinque 1** nei dati viene aggiunto uno **0**; in ricezione, uno **0** dopo cinque 1 viene **eliminato**, ricostruendo i dati originali.

### Violazione fisica

Questo metodo si affida alla codifica della trasmissione fisica, usando un byte (o parola) **non-dato** al livello fisico. Poiché i segnali delimitatori non possono apparire nei dati, le violazioni della codifica delimitano i frame e non serve alcuno stuffing.

## Rilevamento e correzione degli errori

### Formulazione del problema

A livello di collegamento è possibile eseguire **rilevamento e correzione degli errori a livello di bit**. Sia $D$, di dimensione $d$, il dato da proteggere: per difenderlo da errori di bit si includono nel messaggio alcuni bit di rilevamento e correzione, detti **EDC**. L'obiettivo è capire se i $D'$ e $EDC'$ ricevuti differiscono dagli originali $D$ ed $EDC$ e, in tal caso, eventualmente recuperare gli originali. Bisogna tuttavia ricordare che, anche usando bit di rilevamento, possono comunque esserci errori non rilevati (in casi "patologici").

### Parity check

Il **controllo di parità** è forse la forma più semplice di rilevamento degli errori: si aggiunge **un solo bit di parità** al messaggio, tale che il numero totale di 1 tra gli $d+1$ bit sia pari (schema a parità pari) o dispari (schema a parità dispari).

| Messaggio | Bit di parità (pari) | Bit di parità (dispari) |
| --- | --- | --- |
| 1 0 1 0 1 1 0 0 | 0 | 1 |
| 1 1 0 1 0 0 0 0 | 1 | 0 |

Il ricevitore deve solo contare il numero di 1 nei $d+1$ bit ricevuti: se con schema a parità pari trova un numero dispari di bit a 1 (o viceversa), sa che è avvenuto almeno un errore. L'approccio funziona quindi solo con un numero dispari di errori. Se la probabilità di errore sui bit fosse piccola e gli errori fossero indipendenti l'uno dall'altro, la probabilità di errori multipli sarebbe minima — ma non è il caso delle reti di calcolatori: in pratica gli errori tendono a **raggrupparsi in "burst"**. In condizioni di burst error la probabilità di errori non rilevati con la parità a bit singolo può avvicinarsi al **50%**, quindi la tecnica non è davvero utile.

### Parity check bidimensionale

Un modo per migliorare l'approccio è usare più bit di parità. La **parità bidimensionale** divide il messaggio in $n$ righe e $m$ colonne, ciascuna con un proprio bit di parità. In questo modo il ricevitore può rilevare l'errore e individuare il bit errato, potendo quindi tentare la correzione. La parità bidimensionale può inoltre rilevare (ma non correggere) qualsiasi combinazione di due errori in un pacchetto.

### Cyclic Redundancy Check (CRC)

Il **CRC** è una tecnica di rilevamento errori molto usata. Mittente e destinatario concordano un **pattern di $r+1$ bit chiamato generatore** ($G$), con il bit più significativo (il più a sinistra) a 1. Per un dato $D$ di $d$ bit, il mittente sceglie **$r$ bit aggiuntivi (bit CRC)** da appendere al messaggio, in modo che il messaggio $M$ — cioè $D$ concatenata con i bit CRC — sia divisibile modulo-2 per $G$ (resto = 0). Il ricevitore divide $M$ per $G$: se il resto è zero il messaggio è corretto, altrimenti si assume un errore. L'operazione si implementa spostando $G$ in corrispondenza dell'1 più significativo del messaggio ed eseguendo uno XOR bit-a-bit.

#### Esempio

Con un messaggio di 6 bit e un CRC di 3 bit: $d = 6$, $D = 101110$, $r = 3$, $G = 1001$.

**Lato mittente** si calcola il CRC da $D$ e $G$, tramite la divisione modulo-2 di $D$ seguito da $r$ zeri per $G$: gli ultimi $r$ bit del resto sono i bit CRC, che vengono attaccati al messaggio e trasmessi. **Lato ricevente** si divide per $G$ il messaggio ricevuto ($D$ + CRC): se il resto è 0, il messaggio è intatto.

#### Standard e prestazioni

Sono stati definiti **standard internazionali** per generatori a 8, 12, 16 e 32 bit (cioè $r = 8, 12, 16, 32$). Lo **standard CRC-32 a 32 bit**, adottato in diversi protocolli IEEE di livello di collegamento, usa il seguente generatore (33 bit):

$$G_{\text{CRC-32}} = 100000100110000010001110110110111$$

Ogni standard CRC rileva con certezza burst error di meno di $r+1$ bit; per errori più lunghi di $r+1$ esiste una probabilità $P$ di individuare l'errore:

$$P = 1 - 0.5^r$$

La probabilità di trovare l'errore cresce quindi con $r$.

## Distanza di Hamming

Un codice di correzione degli errori trasforma dati di $n$ bit in **codeword di $n+k$ bit**. La **distanza di Hamming** è il minimo numero di inversioni di bit necessarie per trasformare una codeword valida in un'altra qualsiasi codeword valida.

Esempio con 4 codeword di 10 bit ($n=2$, $k=8$):

```
0000000000, 0000011111, 1111100000, 1111111111
```

La distanza di Hamming è **5**. Per un codice con distanza $d$ valgono i seguenti limiti:

- $2d+1$ bit permettono di **correggere** $d$ errori (nell'esempio, 2 errori).
- $d+1$ bit permettono di **rilevare** $d$ errori (nell'esempio, 4 errori).

I **codici di Hamming** si basano su questo principio, ma sono più complessi.