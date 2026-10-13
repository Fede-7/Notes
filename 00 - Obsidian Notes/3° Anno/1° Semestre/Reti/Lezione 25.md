# Lezione 25: Sicurezza di rete — Fondamenti

## Richiamo: alcuni protocolli applicativi

Alcune applicazioni scambiano **informazioni sensibili** (credenziali utente, dati personali); poiché viaggiano su reti pubbliche, i messaggi devono essere protetti.

| Applicazione | Descrizione |
| --- | --- |
| DHCP | Dynamic Host Configuration Protocol, assegna indirizzi IP |
| DNS | Domain Name System, traduce i nomi dei siti in indirizzi IP |
| HTTP/HTTPS | HyperText Transfer Protocol (Secure), trasferisce pagine web |
| SMTP/SMTPS | Simple Mail Transfer Protocol (Secure), invia messaggi e-mail |
| SNMP | Simple Network Management Protocol, gestisce dispositivi di rete |
| Telnet/SSH | Teletype Network (Secure SHell), interfaccia a riga di comando con host remoti |
| FTP/FTPS | File Transfer Protocol (Secure), usato per trasferire file |

## Introduzione

La **sicurezza di rete** è il campo che studia i possibili attacchi alle reti e i modi di prevenirli. Poiché il networking è ormai parte della nostra vita — la connessione Internet è considerata quasi come acqua o elettricità — una grande quantità di dati sensibili viaggia sulle reti. Esistono diversi tipi di attacchi, con scopi e meccanismi differenti, che evolvono insieme alla tecnologia e all'audience delle reti.

## Attacchi: malware

Un **malware** è un software dannoso che può essere trasferito su un computer tramite la rete (file scaricato, allegato e-mail, ecc.). Una volta infettato il dispositivo, può danneggiarlo in diversi modi: forzare un sistema a mostrare pubblicità commerciali (**adware**); mostrare falsi messaggi di allarme per indurre l'utente a scaricare malware (**scareware**); cancellare (**wiper**) o cifrare (**ransomware**) i file; raccogliere informazioni private come password o numeri di sicurezza (**spyware**) — ad esempio i **keylogger** registrano i tasti premuti sulla tastiera; ottenere privilegi di root (**rootkit**); trasformare il dispositivo in uno "schiavo" o punto d'appoggio per attaccare altri dispositivi (**zombie** o **botnet**).

I malware odierni sono spesso **auto-replicanti**: infettato un host, da quello cercano di entrare in altri host su Internet, e da questi in ancora altri. Possono diffondersi come virus o worm. I **virus** richiedono una qualche interazione dell'utente per infettare il dispositivo (es. un allegato e-mail con codice eseguibile dannoso che si auto-replica inviando mail simili ai contatti) e sono tipicamente mascherati da software legittimo (**cavalli di Troia**). I **worm**, invece, entrano nel dispositivo senza alcuna interazione esplicita dell'utente: un'applicazione di rete vulnerabile accetta il worm senza intervento, e il worm poi scansiona la rete in cerca di host con la stessa applicazione.

## Attacchi: DoS

Gli attacchi **Denial-of-Service (DoS)** sono molto comuni e mirano a rendere inutilizzabile una rete, un host o un altro componente dell'infrastruttura (server web, DNS, ecc.) agli utenti legittimi. Esistono tre tipi di attacco DoS:

1. **Vulnerability attack**: invio di messaggi ad hoc ad applicazioni o sistemi operativi vulnerabili per farli bloccare o crashare.
2. **Bandwidth flooding**: invio di un'enorme quantità di pacchetti all'host bersaglio, impedendo ai pacchetti legittimi di raggiungere il server.
3. **Connection flooding**: apertura di un gran numero di connessioni TCP half-open o completamente aperte sull'host bersaglio, che smette di accettare connessioni legittime.

Una variante è il **DDoS** (Distributed DoS), che usa una **botnet** di zombie.

## Attacchi: packet sniffing

Il **packet sniffing** prevede un ricevitore passivo (**sniffer**) che registra una copia dei pacchetti rilevanti da un host bersaglio per rubare informazioni sensibili (detto anche **eavesdropping**). Gli sniffer possono essere installati in ogni tipo di rete **broadcast**, cablata o wireless, semplicemente copiando i pacchetti destinati ad altri invece di scartarli. Nelle reti **non broadcast**, invece, uno sniffer può essere incorporato in un malware (spyware) e usato per infettare dispositivi di rete come i router, così che tutto il traffico inoltrato viene copiato. Poiché sono **passivi** — non iniettano alcun traffico aggiuntivo — gli sniffer sono molto difficili da rilevare. La contromisura principale è la **crittografia**. Un esempio noto di sniffer è **Wireshark** (ex Ethereal).

## Attacchi: IP spoofing

L'**IP spoofing** consente a host malevoli di iniettare in rete pacchetti con **indirizzi sorgente falsificati**. Può essere usato in combinazione con vulnerabilità delle applicazioni per attaccare host specifici mascherandosi da un altro utente, oppure per attacchi DoS come alternativa alle botnet: poiché i messaggi provengono da IP sorgente diversi, sono più difficili da filtrare. Spoofing e sniffing possono inoltre servire per attacchi **man-in-the-middle** (MitM): l'attaccante si pone tra due host in comunicazione spacciandosi per entrambi, quindi i due host credono di parlare tra loro ma comunicano in realtà con l'attaccante. Le contromisure sono le **verifiche di integrità dei messaggi** e l'**autenticazione degli endpoint**, che permettono di capire se il messaggio è stato modificato e se proviene dalla fonte giusta.

## Fondamenti della sicurezza di rete

Una **comunicazione sicura** dovrebbe garantire quattro proprietà:

- **Riservatezza** (*confidentiality*): solo mittente e destinatario previsto devono poter comprendere il contenuto del messaggio (contro lo sniffing).
- **Integrità dei messaggi**: il contenuto della comunicazione non deve essere alterato, né dolosamente né accidentalmente.
- **Autenticazione degli endpoint**: mittente e destinatario devono poter confermare l'identità dell'altra parte (contro lo spoofing).
- **Sicurezza operativa**: poter contare su un'infrastruttura di rete che impedisce a host malevoli di intrufolarsi nella comunicazione.

Le prime tre proprietà sono **software-based**, mentre la sicurezza operativa si basa tipicamente su **hardware dedicato** (firewall, intrusion detection systems).

## Crittografia

Una **tecnica crittografica** consente a un mittente di camuffare i dati rendendoli incomprensibili a un intruso, così che l'intruso non ricavi informazioni dai dati intercettati, mentre il destinatario deve poter recuperare i dati originali. Nella forma iniziale il messaggio si chiama **plaintext** (o cleartext), leggibile da chiunque; prima di immetterlo nel canale, l'host applica un algoritmo di cifratura che lo trasforma in una forma illeggibile, il **ciphertext**, che va decifrato alla ricezione.

### Chiavi

In molti sistemi crittografici moderni, inclusi quelli usati su Internet, la tecnica di cifratura è nota e standard per tutti, intruso compreso: la parte sconosciuta sono le **chiavi** di cifratura e decifratura. Una **chiave** è una stringa alfanumerica fornita all'algoritmo di cifratura/decifratura; le chiavi possono essere identiche (crittografia simmetrica) o diverse (asimmetrica).

### Crittografia simmetrica

Nella crittografia simmetrica esiste **una sola chiave** usata sia per cifrare che per decifrare. In cifratura, il plaintext e la chiave vengono dati all'algoritmo di cifratura, generando un ciphertext da inviare in rete in sicurezza; in decifratura, il ciphertext e la chiave vengono dati all'algoritmo di decifratura per ricostruire il plaintext iniziale. Il limite principale è il **problema dello scambio delle chiavi** (*key exchange problem*): la chiave segreta deve essere comunicata in qualche modo, usando un canale sicuro oppure un protocollo che permetta di "convergere" su una chiave condivisa. Se due parti non riescono a fare uno scambio iniziale sicuro, non potranno comunicare in sicurezza, poiché una terza parte che ottiene la chiave durante lo scambio può intercettare e decifrare i messaggi.

### Crittografia asimmetrica

La crittografia asimmetrica è un sistema a **due chiavi**, pubblica e privata: un messaggio cifrato con una chiave va decifrato con l'altra, e viceversa. La **chiave pubblica** può essere trasmessa su canali non sicuri o condivisa pubblicamente, mentre la **chiave privata** è disponibile solo al proprietario. L'approccio tipico è usare la **chiave pubblica per cifrare e la chiave privata per decifrare**: se l'intruso intercetta la chiave pubblica, non può comunque decifrare i messaggi; A usa infatti la chiave pubblica di B per cifrare messaggi leggibili solo tramite la chiave privata di B, che è solo nelle mani di B.

### Certification Authority (CA)

Nella crittografia a chiave pubblica è utile **verificare che una chiave pubblica appartenga davvero all'entità** con cui si vuole comunicare: altrimenti potremmo avere la chiave di un attaccante e cifrare messaggi leggibili da entità illegittime. Il legame tra chiave pubblica ed entità è stabilito da una **Certification Authority (CA)**, il cui lavoro è validare le identità ed emettere certificati:

1. La CA **verifica che un'entità sia chi dice di essere**: non esiste un protocollo per questo, quindi bisogna fidarsi della CA — funziona come una selezione naturale, poiché una CA inaffidabile non è più fidata. Esistono diverse CA federali e statali ragionevolmente affidabili, ma resta necessario fidarsi.
2. Verificata l'identità, la CA **crea un certificato che lega la chiave pubblica dell'entità alla sua identità**: il certificato contiene la chiave pubblica e un identificatore globalmente univoco del proprietario (es. un nome o un indirizzo IP).

## Integrità dei messaggi

L'**integrità dei messaggi** (o **autenticazione dei messaggi**) è il problema di verificare che il messaggio non sia stato manomesso e che provenga davvero dall'host atteso. Si può creare un "codice di controllo" in modo analogo a checksum o CRC; tipicamente si usa una **funzione hash**. Una funzione hash mappa dati di dimensione arbitraria in valori a dimensione fissa; una **funzione hash crittografica** è una funzione $H$ che converte un messaggio $x$ in una stringa a dimensione fissa $H(x)$, tale che sia computazionalmente improbabile trovare un altro messaggio $y$ con $H(y) = H(x)$.

### Hash semplice (approccio fallace)

1. A crea il messaggio $m$ e calcola l'hash $h = H(m)$.
2. A appende $h$ al messaggio, creando il messaggio esteso $(m, h)$, e lo invia a B.
3. B riceve $(m, h)$ e calcola $H(m)$: se $H(m) = h$, il messaggio è intatto.

L'approccio è ovviamente fallace: un intruso può falsificare l'intero messaggio, creandone uno "ad hoc" $(m', h')$ comunque consistente con $H$.

### Message Authentication Code (MAC)

Per evitare ciò, A e B hanno bisogno di un **segreto condiviso** $s$ (**chiave condivisa** o **password**), noto solo a loro — di fatto funziona come una cifratura simmetrica dove $s$ è l'unica chiave privata. La procedura è la seguente:

1. A crea il messaggio $m + s$ (concatenazione di messaggio e segreto) e calcola l'hash $h = H(m + s)$, detto **message authentication code (MAC)**.
2. A appende il MAC al messaggio, creando il messaggio esteso $(m, H(m + s))$, e lo invia a B.
3. B riceve $(m, h)$ e, conoscendo $s$, calcola il MAC $H(m + s)$: se $H(m + s) = h$, il messaggio è intatto.

Come in tutti gli approcci simmetrici, bisogna scambiare il segreto; lo scambio può avvenire combinando crittografia asimmetrica e certificati.