# Lezione 25 — Sicurezza di rete: attacchi, crittografia, integrità

## Introduzione alla network security

> [!def] Network security
> Campo che studia i possibili **attacchi** alle reti e i modi per **prevenirli**. La rete è parte della vita quotidiana (la connessione è considerata quasi come acqua ed elettricità) e una grande quantità di dati sensibili viaggia sui network. Gli attacchi hanno scopi e meccanismi diversi ed **evolvono insieme alla tecnologia e al pubblico** delle reti.

In internet i protocolli pubblici e le reti condivise rendono necessario proteggere i messaggi.

| Applicazione | Descrizione |
| --- | --- |
| DHCP | Dynamic Host Configuration Protocol, assegna indirizzi IP |
| DNS | Domain Name System, traduce nomi di siti in indirizzi IP |
| HTTP/HTTPS | HyperText Transfer Protocol (Secure), trasferisce pagine web |
| SMTP/SMTPS | Simple Mail Transfer Protocol (Secure), invia messaggi e-mail |
| SNMP | Simple Network Management Protocol, gestisce dispositivi di rete |
| Telnet/SSH | Telnet / Secure SHEll, interfaccia a riga di comando con host remoti |
| FTP/FTPS | File Transfer Protocol (Secure), usato per trasferire file |

## Attacchi: malware

Un **malware** è software malevolo che può arrivare al computer via rete (file scaricato, allegato e-mail, ecc.). Una volta infettato il dispositivo, può nuocere in vari modi:

- **Adware**: forzare la visualizzazione di pubblicità;
- **Scareware**: falsi messaggi d'allarme per indurre a scaricare altri malware;
- **Wiper** (cancellazione) o **ransomware** (crittatura dei file);
- **Spyware**: raccolta di informazioni private (password, numeri di sicurezza...); es. **keylogger**, software che registra i tasti premuti sulla tastiera;
- **Rootkit**: ottenere i privilegi di root del sistema;
- **Zombie/botnet**: trasformare il dispositivo in "schiavo" o base d'appoggio per attaccare altri dispositivi.

I malware odierni sono spesso **autoréplicanti**: da un host infettato cercano entry in altri host su Internet, e dai nuovi infetti ne cercano altri ancora. Si diffondono come:

- **Virus**: richiedono una qualche **interazione dell'utente** per infettare (es. allegato e-mail con codice eseguibile che si réplica inviando mail simili ai contatti); spesso camuffati da componenti legittimi (**cavalli di Troia**);
- **Worm**: entrano nel dispositivo **senza interazione esplicita** (es. sfruttando un'applicazione di rete vulnerabile, poi scansionando la rete in cerca di host con la stessa vulnerabilità).

## Attacchi: DoS

> [!def] DoS
> Le **Denial-of-Service** rendono inutilizzabile una rete, un host o un'infrastruttura (Web server, DNS, ecc.) per gli utenti legittimi. I 3 tipi sono:
> 1. **Vulnerability attack**: messaggi mirati ad applicazioni o OS vulnerabili per farli bloccare o crashare;
> 2. **Bandwidth flooding**: ingente quantità di pacchetti verso l'host bersaglio, impedendo ai pacchetti legittimi di arrivare;
> 3. **Connection flooding**: aprire un numero enorme di connessioni TCP **half-open o fully-open** verso il bersaglio, che smette di accettare connessioni legittime.

Nella variante **DDoS (Distributed DoS)** l'attacco usa una **botnet di zombie** (host infettati).

## Attacchi: packet sniffing

- Uno **sniffer** è un ricevitore **passivo** che registra una copia dei pacchetti rilevanti per un host bersaglio, cercando di rubare informazioni sensibili (*eavesdropping*).
- Nelle reti broadcast (cablate o wireless) basta **copiare i pacchetti diretti ad altre destinazioni** invece di scartarli; nelle reti non broadcast, uno sniffer può essere incorporato in malware (spyware) e infettare dispositivi di rete (es. router), così che anche il traffico inoltrato viene copiato.
- Essendo **passivi** (nessun traffico iniettato), gli sniffer sono **molto difficili da rilevare**. Esempio notevole: **Wireshark** (ex Ethereal).
- Contromisura: **crittografia**.

## Attacchi: IP spoofing

- Tecnica che permette a host malevoli di iniettare in rete pacchetti con **indirizzi sorgente falsificati** (forged).
- Può combinarsi con vulnerabilità applicative per attaccare host **spacciandosi per un altro utente**;
- può servire per **DoS** (alternativa alle botnet: messaggi da IP sorgenti diversi sono più difficili da filtrare);
- con lo sniffing consente attacchi **man-in-the-middle (MitM/MiM)**: l'attaccante si frappone tra due host **fingendosi entrambi** — i due pensano di comunicare tra loro ma parlano con l'attaccante.
- Contromisure: **controlli di integrità dei messaggi** e **autenticazione degli endpoint**, per verificare che il messaggio non sia stato modificato e che provenga dalla sorgente giusta.

## Proprietà di una comunicazione sicura

Data la tassonomia degli attacchi, una comunicazione sicura dovrebbe garantire:

| Proprietà | Significato | Evita |
| --- | --- | --- |
| **Confidenzialità** | Solo mittente e destinatario devono comprendere il contenuto del messaggio trasmesso | Sniffing |
| **Integrità dei messaggi** | Il contenuto non deve essere alterato, né maliziosamente né accidentalmente | — |
| **Autenticazione degli endpoint** | Mittente e destinatario devono poter confermare l'identità dell'altro | Spoofing |
| **Operational security** | Potersi affidare a un'infrastruttura di rete che impedisca a host malevoli di intrufolarsi nella comunicazione | — |

Le prime 3 proprietà sono **software-based**; l'ultima si affida tipicamente a **hardware dedicato** (firewall, intrusion detection systems).

## Crittografia

> [!def] Crittografia
> Tecnica che permette al mittente di **camuffare** i dati così che diventino incomprensibili per un intruso, mentre il destinatario deve poter **recuperare i dati originali** da quelli camuffati.

Terminologia:

- **Plaintext** (o cleartext): il messaggio nella forma originale, leggibile da chiunque.
- Il mittente applica un **algoritmo di cifratura** che lo trasforma in **ciphertext**, da decifrare alla ricezione.

### Chiavi

Nei sistemi moderni (inclusi quelli usati su Internet) l'**algoritmo è noto e standard** per tutti (intruso compreso): la parte segreta sono le **chiavi** di cifratura/decifratura — stringhe alfanumeriche fornite all'algoritmo per cifrare/decifrare.

Le chiavi possono essere **identiche** (simmetriche) o **diverse** (asimmetriche).

### Crittografia simmetrica

Esiste **una sola chiave** per cifrare e decifrare:

- **Cifratura**: plaintext + chiave → algoritmo → ciphertext, inviabile in sicurezza;
- **Decifratura**: ciphertext + chiave → algoritmo → plaintext leggibile.

> [!warning] Key exchange problem
> Il tallone d'Achille della crittografia simmetrica: la chiave segreta va **comunicata**. Soluzioni: un canale sicuro per lo scambio, o un protocollo che fa "convergere" le parti su una chiave condivisa. Senza uno scambio iniziale sicuro, un terzo può acquisire la chiave e decifrare i messaggi.

### Crittografia asimmetrica

Sistema a **due chiavi** (pubblica e privata): un messaggio cifrato con una chiave **deve** essere decifrato con l'altra (e viceversa).

- La chiave **pubblica** viaggia su canali insicuri o è condivisa pubblicamente; quella **privata** è nota solo al proprietario.
- Approccio tipico: **chiave pubblica per cifrare, chiave privata per decifrare**:
  - anche se l'intruso sniffa la chiave pubblica, **non può decifrare** i messaggi;
  - A cifra con la *B-pubblica* → solo la *B-privata* (in mano a B) può leggere.

## Certification Authority

Nella crittografia a chiave pubblica serve **verificare che una chiave pubblica appartenga davvero** all'entità con cui si vuole comunicare: altrimenti si può usare la chiave dell'attaccante, rendendo leggibili i messaggi a entità illegittime.

Il **binding** tra chiave pubblica ed entità è fatto da una **Certification Authority (CA)**, il cui lavoro è validare identità ed emettere certificati:

1. **Verifica dell'identità**: la CA verifica che l'entità sia chi dice di essere. Non c'è un protocollo: bisogna **fidarsi** che la CA abbia fatto una verifica rigorosa (selezione naturale: una CA inaffidabile non si fida nessuno; esistono CA federali/statali ragionevolmente affidabili — ma resta una fiducia).
2. **Emissione del certificato**: la CA crea un certificato che **lega la chiave pubblica all'identità**, contenente la chiave pubblica e un identificatore globalmente univoco del proprietario (es. nome o indirizzo IP).

## Integrità dei messaggi

> [!def] Message integrity
> Problema di verificare che: (1) il messaggio **non sia stato manomesso**; (2) il messaggio **provienga davvero** dall'host atteso. È detta anche *message authentication*.

### Hash

- La strategia base è aggiungere un elemento di controllo, analogo a **checksum o CRC**, tipicamente prodotto da una **hash function**: una funzione che mappa dati di dimensione arbitraria in valori a dimensione fissa.
- Una **hash crittografica** è una funzione $H$ che converte un messaggio $x$ in una stringa a dimensione fissata $H(x)$, tale che sia **computazionalmente improbabile** trovare un altro messaggio $y$ con $H(y) = H(x)$.

Approccio ingenuo:

1. A crea il messaggio $m$ e calcola $h = H(m)$;
2. A invia a B il messaggio esteso $(m, h)$;
3. B ricalcola $H(m)$: se coincide con $h$, il messaggio è intatto.

> [!warning] Approccio fallibile
> Un intruso può **spoofare l'intero messaggio** $(m,h)$ creandone uno nuovo "ad hoc" $(m', h')$, perfettamente consistente con $H$. Serve un segreto condiviso.

### MAC (Message Authentication Code)

A e B condividono un **segreto** $s$ (chiave condivisa o password) noto solo a loro — di fatto una cifratura simmetrica dove $s$ è l'unica chiave privata:

1. A calcola $h = H(m + s)$ (hash di messaggio concatenato al segreto): il **MAC**;
2. A invia il messaggio esteso $(m,\ H(m+s))$;
3. B, conoscendo $s$, ricalcola il MAC: se $H(m+s) = h$ il messaggio è intatto.

L'intrudo, non conoscendo $s$, non può più forgiare una coppia consistente.

> [!info] Scambio del segreto
> Come in ogni schema simmetrico, anche qui il segreto va scambiato: si può fare **combinando crittografia asimmetrica e certificati**.