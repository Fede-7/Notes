# Esercizi numerici dello scritto

Raccolta delle tipologie di esercizi numerici e analitici dello scritto, ordinate per lezione: per ciascuna sono riportati i dati forniti dalla traccia, le formule e il metodo di risoluzione. Nelle lezioni L01–L03 (introduzione, modelli Client-Server/P2P, incapsulamento, User Space e Kernel Space) non sono presenti esercizi numerici puntuali.

## Tempi di trasferimento in HTTP (L04)

### Conteggio dei Round Trip Time

Una pagina web è composta da un file HTML di base e $N$ oggetti incorporati: il tempo totale di scaricamento si conta in **Round Trip Time** (RTT) e dipende dalla modalità di funzionamento di HTTP. Il tempo totale per un oggetto vale $T \approx 2\,\text{RTT} + L/R$, dove $L/R$ è il tempo di trasmissione del file.

Con un HTML di base e $10$ immagini ($11$ oggetti totali):

- **Non-persistente sequenziale**: ogni oggetto richiede 1 RTT per l'handshake TCP e 1 RTT per richiesta e risposta HTTP $\implies 2 \times 11 = 22$ RTT.
- **Non-persistente con connessioni parallele**: le immagini si scaricano in lotti paralleli; con $K = 5$ connessioni si hanno 2 RTT per l'HTML più due round da 5 immagini $\implies 2 + 2 \times 2 = 6$ RTT.
- **Persistente senza pipelining**: 1 RTT per l'handshake TCP iniziale più 1 RTT per ciascuno degli 11 oggetti sulla stessa connessione aperta $\implies 1 + 11 = 12$ RTT.
- **Persistente con pipelining**: 1 RTT per l'handshake, 1 per l'HTML e 1 unico per il lotto in pipeline di tutte le immagini $\implies 1 + 1 + 1 = 3$ RTT.

## Web cache e link di accesso (L05)

Una rete istituzionale genera un flusso costante di richieste HTTP verso Internet attraverso un link di accesso: l'introduzione di una **Web Cache** riduce traffico e tempo medio di risposta in funzione del tasso di hit. I dati tipici sono $r = 15$ req/s, $L = 1$ Mbit, $R_{access} = 15$ Mbps, tempo di fetching da Internet $T_{internet} = 2$ s, hit rate $h = 0.4$.

- **Senza cache**: la domanda di banda $r \cdot L = 15$ Mbps eguaglia la capacità del link $\implies$ utilizzazione al 100% e code crescenti.
- **Con cache**: solo la frazione $(1-h)$ delle richieste attraversa il link verso l'origine.
- **Traffico residuo sul link**: $r \cdot L \cdot (1 - h) = 15 \times 0.6 = 9$ Mbps.
- **Utilizzazione del link**: $9 / 15 = 60\%$ $\implies$ saturazione e code eliminate.
- **Tempo medio di risposta**: $(h \cdot 0) + ((1-h) \cdot T_{internet}) = 0.4 \cdot 0 + 0.6 \cdot 2 = 1.2$ s.

## Interazione testuale con i protocolli applicativi (L06)

SMTP e HTTP si possono esercitare inviando comandi diretti via socket o `telnet`: per la posta i comandi sono `HELO`, `MAIL FROM`, `RCPT TO`, `DATA`.

## DNS e utility `dig` (L07–L08)

### Catena CNAME e record A

Un hostname può essere un **alias** delegato a un CDN o provider esterno, risolto tramite una catena di record CNAME fino al record A finale: si contano gli hop di alias e si identifica l'hostname che possiede l'A record finale.

> [!info] Catena CNAME di esempio
> ```text
> www.university.edu.  300 IN CNAME web.provider.net.
> web.provider.net.    300 IN CNAME node42.network.net.
> node42.network.net.   120 IN A     203.0.113.42
> ```
>
> Due hop di CNAME prima dell'A record, posseduto da `node42.network.net` (`203.0.113.42`).

### Reverse DNS (record PTR)

Il reverse lookup mappa un indirizzo IP in un nome tramite record PTR sotto la gerarchia `.in-addr.arpa.`:

1. Invertire l'ordine dei quattro ottetti dell'indirizzo IPv4: `192.0.2.10` $\implies$ `10.2.0.192`.
2. Appendere il dominio infrastrutturale $\implies$ `10.2.0.192.in-addr.arpa.`
3. La query corrispondente è `dig -x 192.0.2.10 +noall +answer`.

### Mail server via record MX

Il record MX identifica il mail server responsabile di un dominio con il relativo valore di preferenza; per ricavarne gli indirizzi si risolve l'hostname del mail server con query `A` (IPv4) e `AAAA` (IPv6). Per `mit.edu. 65 IN MX 100 mit-edu.mail.protection.outlook.com.` il server è `mit-edu.mail.protection.outlook.com` (preferenza $100$).

### Risoluzione iterativa manuale

Disabilitando la ricorsione con `+norecurse` si ripercorre manualmente l'albero gerarchico DNS: root server, TLD, server di dominio e server autoritativo finale, che risponde con il flag `aa` (Authoritative Answer).

```bash
# Root: referral per la zona .jp
dig +norecurse @c.root-servers.net hyoka.ofc.kyushu-u.ac.jp A
# TLD: referral per kyushu-u.ac.jp
dig +norecurse @b.dns.jp hyoka.ofc.kyushu-u.ac.jp A
# Server di dominio: referral per ofc.kyushu-u.ac.jp
dig +norecurse @ns2.kyushu-u.ac.jp hyoka.ofc.kyushu-u.ac.jp A
# Server autoritativo finale: A record con flag aa
dig +norecurse @ns.jimu.kyushu-u.ac.jp hyoka.ofc.kyushu-u.ac.jp A
```

## Programmazione socket in C (L09–L13)

### Byte order

I valori interi vanno convertiti in **Network Byte Order** prima dell'invio e riconvertiti in host order alla ricezione, con le funzioni `htons()`/`htonl()` e `ntohs()`/`ntohl()`. Lato client si converte prima di `send()`, lato server si riconverte dopo `recv()`:

```c
uint32_t net_val = htonl((uint32_t) x);
send(s, &net_val, sizeof(net_val), 0);

recv(s, &net_val, sizeof(net_val), 0);
uint32_t res = ntohl(net_val);
```

> [!warning] Letture e scritture parziali
> `send()` e `recv()` possono trasferire meno byte di quelli richiesti e venire interrotti: vanno gestiti con cicli di lettura/scrittura sicuri (`safe_read`/`safe_write`) per evitare letture parziali e gestire `EINTR`.

### Multiplexing dell'I/O con `select()`

Un server concorrente single-threaded monitora simultaneamente più file descriptor (listening socket, socket connesse, `stdin`) tramite le maschere `fd_set` e le macro `FD_ZERO()`, `FD_SET()`, `FD_ISSET()`, `FD_CLR()`. Il ciclo di multiplexing segue questi passaggi:

1. Inizializzare la maschera di ascolto con `FD_ZERO(&allset)` e `FD_SET(listensd, &allset)`.
2. A ogni iterazione copiare la maschera (`rset = allset`) prima della chiamata, perché `select()` la sovrascrive.
3. Eseguire `select(maxd + 1, &rset, NULL, NULL, NULL)`.
4. Se `FD_ISSET(listensd, &rset)` è vero: eseguire `accept()` e registrare la nuova connessione in `allset`.
5. Per ogni socket client attiva con `FD_ISSET` vero: leggere i dati; su EOF (lettura di $0$) chiudere il socket e rimuoverlo con `FD_CLR` o impostandolo a `-1`.

## Checksum UDP (L14)

### Calcolo a complemento a 1

Il **checksum UDP** si calcola sommando le parole a 16 bit del segmento a complemento a 1 e trasmettendo il complemento a 1 della somma.

> [!def] End-around carry
> **Tecnica di somma** in cui il bit di overflow prodotto da una somma a 16 bit viene ripiegato e riaddizionato al bit meno significativo del risultato.

Con le tre parole `0110011001100000`, `0101010101010101`, `1000111100001100`:

1. Sommare le prime due parole: `0110011001100000 + 0101010101010101 = 1011101110110101`.
2. Sommare la terza: il risultato ha 17 bit $\implies$ overflow; ripiegando il bit di riporto si ottiene `0100101011000010`.
3. Complementare a 1 (invertire tutti i bit) $\implies$ checksum = `1011010100111101`.

> [!info] Verifica del ricevitore
> Sommando tutti i bit ricevuti, checksum incluso, il risultato deve essere composto interamente da `1` (`1111111111111111`).

## Stop-and-Wait e utilizzo del canale (L15)

### Tempo di trasmissione e utilizzazione

> [!def] Utilizzazione del canale
> **Rapporto** fra il tempo di trasmissione del pacchetto e il tempo totale del ciclo di Stop-and-Wait: $U = \frac{d_{trans}}{RTT + d_{trans}}$, con $d_{trans} = \frac{L}{R}$.

Con $R = 1$ Gbps ($10^9$ bit/s), $RTT = 30$ ms e $L = 1000$ byte ($8000$ bit):

- **Tempo di trasmissione**: $d_{trans} = \frac{8000}{10^9} = 8\ \mu\text{s} = 0.008$ ms.
- **Tempo totale del ciclo**: $RTT + d_{trans} = 30 + 0.008 = 30.008$ ms.
- **Utilizzazione**: $U = \frac{0.008}{30.008} \approx 0.0002668 \implies 0.027\%$.

### Finestra e spazio dei numeri di sequenza

In **Selective Repeat** il ricevitore non deve confondere un pacchetto nuovo con uno ritrasmesso: lo spazio dei numeri di sequenza $2^k$ deve essere almeno il doppio della dimensione della finestra $N$.

$$2^k \ge 2N \implies N \le 2^{k-1}$$

> [!warning] Ambiguità con finestra troppo grande
> Con $k = 2$ bit ($2^k = 4$ numeri) e $N = 3$ la condizione $4 \ge 2 \cdot 3$ **fallisce**: il ricevitore non distingue il pacchetto $0$ nuovo dal pacchetto $0$ ritrasmesso. Per funzionare senza errori con finestra $N = 4$ servono almeno $8$ numeri di sequenza ($k = 3$ bit).

## Meccanismi TCP (L16)

### Numeri di sequenza e ACK

Data una sequenza di scambi tra Host A e Host B, i campi dei segmenti successivi si determinano dai numeri di sequenza iniziali e dai byte trasmessi: il campo **ACK** è il numero di sequenza del prossimo byte atteso dal ricevente. Con $\text{SEQ}_A = 42$, $\text{SEQ}_B = 79$ e 1 byte di dati inviati da A:

- **Segmento da A a B**: `SEQ = 42`, `ACK = 79`, dati = 1 byte.
- **Risposta con ACK piggyback da B ad A**: `SEQ = 79`, `ACK = 43` ($\text{SEQ}_A + 1$ byte).
- **ACK puro da A a B**: `SEQ = 43`, `ACK = 80`.

### Stima del timeout di ritrasmissione (EWMA)

TCP stima il RTT con una media mobile esponenziale dei campioni `SampleRTT` e imposta il timeout come somma della stima e di quattro deviazioni:

- **EstimatedRTT**: $\text{EstimatedRTT} = (1 - \alpha) \cdot \text{EstimatedRTT} + \alpha \cdot \text{SampleRTT}$, con $\alpha = 0.125$.
- **DevRTT**: $\text{DevRTT} = (1 - \beta) \cdot \text{DevRTT} + \beta \cdot |\text{SampleRTT} - \text{EstimatedRTT}|$, con $\beta = 0.25$.
- **TimeoutInterval**: $\text{TimeoutInterval} = \text{EstimatedRTT} + 4 \cdot \text{DevRTT}$.

Con `EstimatedRTT` $= 200$ ms, `DevRTT` $= 20$ ms e `SampleRTT` $= 260$ ms:

- **Nuovo EstimatedRTT**: $(0.875 \times 200) + (0.125 \times 260) = 175 + 32.5 = 207.5$ ms.
- **Nuovo DevRTT**: $(0.75 \times 20) + (0.25 \times |260 - 200|) = 15 + 15 = 30$ ms.
- **TimeoutInterval**: $207.5 + 4 \times 30 = 327.5$ ms.