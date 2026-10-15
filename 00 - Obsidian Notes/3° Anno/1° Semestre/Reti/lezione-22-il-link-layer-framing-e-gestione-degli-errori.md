# Lezione 22 — Il Link Layer: framing e gestione degli errori

## Dal network al link e physical layer

Il network layer fornisce comunicazione tra due host **qualsiasi** della rete; link e physical layer forniscono comunicazione tra **due host connessi direttamente**:

- il **link layer** è la parte dello stack dedicata alla trasmissione di pacchetti sui link (canali di trasmissione), da nodo a nodo;
- il **physical layer** regola la **struttura dei link** (mezzo trasmissivo, connettori, tipi di cavo) e come i bit sono rappresentati/trasmessi lungo il link.

I due livelli sono **strettamente intrecciati** (spesso raggruppati in un unico livello detto *network access*); alcuni protocolli (es. Ethernet) coprono entrambi. Sono presenti in **tutti i componenti** dell'infrastruttura:

- **nodi**: host, router, switch, hub, access point WiFi, ecc.
- **link**: cablati (rame, fibra ottica) o wireless (radiofrequenze).

Per trasmettere un datagramma IP bisogna attraversare i singoli link lungo il percorso: i datagrammi vengono **incapsulati in frame di link layer**, che rappresentano **l'ultima incapsulazione** — i frame vengono poi convertiti in **segnali** (impulsi elettrici, luce, onde radio) e trasmessi secondo le specifiche del link.

## Servizi del link layer

Il link layer può offrire fino a 4 servizi:

1. **Framing**: incapsulare/decapsulare i datagrammi in frame con header/tailer specifici del protocollo.
2. **Link access**: regolare l'accesso al link tramite il protocollo **MAC** (Medium Access Control). Per i link **punto-punto** (un mittente, un destinatario) la regola è semplice (o assente): si invia appena il link è libero; per i link **broadcast** esiste il *multiple access problem* e il MAC coordina le trasmissioni dei molti nodi.
3. **Reliable delivery**: garantisce che i frame trasmessi sul link vengano ricevuti; utile su link a **alto tasso di errore** (es. wireless) per correggere localmente. Introdotte forte overhead e, essendo già affidabili altri protocolli (es. TCP), **non è sempre implementato**.
4. **Rilevazione e correzione degli errori**: l'hardware può subire il *bit flipping*; si implementano controlli (hardware-embedded) oltre a quelli dei livelli superiori. Non essendoci ulteriore incapsulamento, **coprono l'intero messaggio** e sono molto più veloci.

## Implementazione

Le funzionalità di link layer sono implementate **sia software che (soprattutto) hardware**:

- Negli end system operano le schede di rete (**NIC**, Network Interface Card), con un chip specializzato (**controller**) che implementa le funzionalità di link layer. Un tempo separate dalla scheda madre (slot PCI), oggi spesso integrate (*LAN-on-motherboard*).
- **Software** (sulla CPU): indirizzamento, gestione interrupt/hardware, gestione errori, incapsulamento/decapsulamento. A livello link c'è un indirizzo aggiuntivo, il **MAC address**, che identifica la NIC; i datagrammi vanno recuperati/memorizzati in memoria durante incapsulamento/decapsulamento.
- **Hardware**: come tipico dispositivo di I/O, converte i dati nel segnale da trasmettere secondo il protocollo fisico (Ethernet, wireless, ecc.).

## Tecnologie fisiche

Il protocollo di link layer (e quindi la struttura del frame) dipende dalla tecnologia del link fisico:

- **Ethernet 802.3**: impulsi elettrici su 4 doppini in rame (il più comune) o fotoni su fibra ottica.
- **WiFi 802.11**: radiofrequenze (2,4 GHz, 5 GHz, 6 GHz).
- **Bluetooth**: radiofrequenze (2,4 GHz).

| Tipo | Segnale | Distanza | Banda | Limiti |
| --- | --- | --- | --- | --- |
| Wireless | Radio | 30–50 m | 1,3 Gbps | Sicurezza, velocità |
| Doppino in rame | Elettricità | 30–100 m | 1–25 Gbps | Interferenze |
| Fibra ottica | Luce | 100–200 km | 1–400+ Gbps | Fragilità |

Le tecnologie evolvono continuamente e i confini di distanza/banda vengono aggiornati.

## Metodi di framing

Per incapsulare i datagrammi in frame servono **delimitatori** riconoscibili. I metodi principali:

### Byte count (mai usato)

Ogni frame inizia con il **conto dei byte** che contiene. Semplice, ma **difficile da risincronizzare** dopo un errore (un bit sbagliato nel contatore invalida tutti i frame successivi).

### Byte stuffing

Un **byte flag** speciale delimita i frame; le occorrenze del flag **nei dati** vengono "escaped" con un byte ESC.

Formato del frame:

| FLAG | Header | Payload | Trailer | FLAG |
| --- | --- | --- | --- | --- |

Esempi di stuffing:

| Byte originali | | | → Dopo stuffing | | | |
| --- | --- | --- | --- | --- | --- | --- |
| A | FLAG | B | → A | ESC | FLAG | B |
| A | ESC | B | → A | ESC | ESC | B |
| A | ESC | FLAG | B | → A | ESC | ESC | ESC | FLAG |
| A | ESC | ESC | B | → A | ESC | ESC | ESC | ESC |

Risultato: frame più lunghi, ma **facile risincronizzazione dopo un errore**.

### Bit stuffing

- Il flag del frame è la sequenza di **sei 1 consecutivi** (`01111110`).
- In **trasmissione**: dopo cinque 1 nei dati si aggiunge uno **0**.
- In **ricezione**: uno 0 che segue cinque 1 viene **eliminato**.

### Coding violations (livello fisico)

Si sfrutta la **codifica della trasmissione fisica**: un simbolo **non-dato** viene usato per delimitare i frame. Non serve stuffing, perché il segnale delimitatore **non può comparire** nei dati.

## Rilevazione e correzione degli errori

A livello link è possibile fare rilevazione e correzione degli errori **a livello di bit**.

> [!def] Problema EDC
> Sia $D$ (di $d$ bit) il dato. Lo si protegge aggiungendo bit di **error detection and correction** ($EDC$). Il ricevitore controlla se il $D'$ e $EDC'$ ricevuti differiscono dagli originali e, in tal caso, cerca eventualmente di recuperare $D$.

> [!warning] Errori non rilevati
> Anche con bit di rilevamento **possono esistere errori non rilevati** (casi "patologici"): il ricevitore potrebbe non accorgersi della differenza.

### Parity check

La forma più semplice: si aggiunge **1 bit di parità** tale che il numero totale di 1 nei $d+1$ bit sia **pari** (schema even) o **dispari** (schema odd).

| Messaggio | Bit di parità (even) | Bit di parità (odd) |
| --- | --- | --- |
| 1 0 1 0 1 1 0 0 | 0 | 1 |
| 1 1 0 1 0 0 0 0 | 1 | 0 |

Il ricevitore **conta gli 1**: con parità pari, trova un numero dispari di 1 → almeno un errore.

**Limite**: funziona solo con un **numero dispari** di errori. In pratica gli errori sono **raggruppati in burst** (non indipendenti): in quelle condizioni la probabilità di errore non rilevato con la parità a bit singolo può avvicinarsi al **50%** — quindi poco utile.

### Parity check bidimensionale (2D)

Si usano **bit di parità multipli**: il messaggio è disposto su $n$ righe e $m$ colonne, ciascuna con il suo bit di parità.

- Il ricevitore può rilevare **quale bit** è errato e **tentare la correzione** (intersezione riga/colonna).
- Rileva (ma **non corregge**) qualsiasi combinazione di **due errori** in un pacchetto.

### CRC (Cyclic Redundancy Check)

Tecnica di rilevamento molto usata:

- Mittente e ricevitore si accordano su un **generatore $G$** di $r+1$ bit, con il bit più significativo a 1.
- Per il dato $D$ da $d$ bit, il mittente sceglie $r$ bit (**CRC**) da appendere tali che il messaggio $M = D \,\|\, CRC$ sia **divisibile modulo-2 per $G$** (resto 0).
- Il ricevitore **divide $M$ per $G$**: resto 0 → messaggio corretto; altrimenti errore.
- L'operazione si implementa **shifando $G$ verso l'1 più significativo del messaggio e facendo XOR bit-a-bit**.

```text
Esempio: d = 6, D = 101110, r = 3, G = 1001
Sender: M = D · 2^r XOR resto(D · 2^r / G)  →  M = 101110 011
Receiver: resto(M / G) = 0  →  messaggio intatto
```

> [!info] Standard CRC
> Esistono standard internazionali per generatori a 8, 12, 16 e 32 bit. Il **CRC-32** (usato in diversi protocolli IEEE di livello link) usa il generatore a 33 bit:
> $$G_{\text{CRC-32}} = 1000001001100000100011101101101111$$

- Ogni standard CRC rileva **con certezza** errori a burst **inferiori a $r+1$ bit**.
- Per errori più lunghi, la probabilità di rilevamento è:
> $$P = 1 - 0.5^r$$
> che cresce con $r$: più bit CRC, più errori rilevati.

## Hamming distance (codici correttivi)

Un codice correttivo trasforma dati di $n$ bit in **codeword** di $n+k$ bit.

> [!def] Distanza di Hamming
> È il numero **minimo** di bit flip necessari per trasformare una codeword valida in un'altra codeword valida qualsiasi.

Esempio con 4 codeword da 10 bit ($n=2$, $k=8$):

- `0000000000`, `0000011111`, `1111100000`, `1111111111` → distanza di Hamming **5**.

Limiti per un codice con distanza $d$:

- con distanza $d+1$ si possono **rilevare** $d$ errori;
- con distanza $2d+1$ si possono **correggere** $d$ errori.

I **codici di Hamming** si basano su questo principio (con costruzioni più raffinate).