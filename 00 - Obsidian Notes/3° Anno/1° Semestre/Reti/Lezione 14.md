# Lezione 14 Trasferimento affidabile dei dati

## Il problema del trasferimento affidabile

Il problema generale è come ottenere un protocollo affidabile sopra un canale che non lo è, indipendentemente dallo strato considerato: le tecniche valgono anche per livelli diversi dal trasporto e servono da base per parlare di TCP.

- **Obiettivo**: garantire che i dati arrivino corretti, completi e nell'ordine originale.
- **Sfida**: il canale di comunicazione sottostante può corrompere bit o perdere pacchetti.
- **Astrazione**: fornire ai livelli superiori un servizio di comunicazione affidabile anche quando il canale sottostante è inaffidabile.
- **Ambito**: un problema fondamentale ai livelli link, trasporto e applicazione, non specifico di TCP; l'assunzione realistica è che il livello di rete sottostante sia inaffidabile, come IP sotto TCP.

![[Lezione 14-1793554680733.png|200]]

Nel caso ideale di un canale perfettamente affidabile (`rdt1.0`) non serve alcun meccanismo: il sender trasmette i pacchetti e il receiver li consegna immediatamente ai livelli superiori, senza complicazioni aggiuntive. Il controllo d'errore (es. con checksum) permette al receiver di capire se il messaggio è corrotto, ma non basta: la comunicazione affidabile richiede tre garanzie.

- Nessun bit trasmesso è **corrotto** (cambiato da 0 a 1 o viceversa).
- Nessun bit è **perso o ripetuto**.
- Tutti i bit sono consegnati nell'**ordine esatto** di invio.

Si considera il **trasferimento dati unidirezionale**, dal sender al receiver; i pacchetti di controllo (ACK/NACK) devono però viaggiare anche in direzione opposta: flusso unidirezionale ≠ comunicazione unidirezionale. Entrambe le parti usano servizi di trasmissione inaffidabile per inviare pacchetti sul canale inaffidabile.

La progressione da canale perfetto a canale reale riassume ciò che il protocollo deve aggiungere a ogni passo.

| Cosa fa il canale | Cosa deve aggiungere il protocollo |
|---|---|
| niente va storto | niente: si crea il pacchetto e lo si invia |
| i bit possono corrompersi | checksum, riconoscimenti, ritrasmissione |
| anche il riconoscimento può corrompersi | un numero di sequenza, per riconoscere una copia |
| i pacchetti possono perdersi | un timer al sender e la ritrasmissione che innesca |

L'ultima riga è il **protocollo alternating bit**: checksum, numero di sequenza a un bit, riconoscimenti numerati, un timer; è corretto su ogni canale descritto, e resta da misurare quanto sia lento.

## Stop-and-wait e ARQ

Primo caso: canale in cui i pacchetti possono solo **corrompersi**, non perdersi. La corruzione è un problema tipico, dovuto ai componenti fisici della rete: un pacchetto viene trasmesso, propagato o bufferizzato più volte durante la comunicazione.

> [!def] Stop-and-wait
> **Protocollo** in cui ogni messaggio deve essere riconosciuto prima di inviarne uno nuovo: si manda un messaggio alla volta e si attende il riscontro, **ACK** (messaggio ricevuto intatto) oppure **NACK** (errore occorso, il messaggio va ripetuto).

> [!aside]
> 
> > [!def] ARQ
> > **Famiglia di protocolli** basati sulla ritrasmissione, detti *Automatic Repeat reQuest*: se arriva un NACK, il messaggio viene rinviato. Per funzionare richiedono tre meccanismi, nessuno dei quali è opzionale, e i tre insieme non bastano ancora.
> > - **Error detection**: bit aggiuntivi (il checksum) perché il receiver noti che il messaggio è cambiato.
> > - **Receiver feedback**: il sender non vede la destinazione, può sapere solo se gli viene detto; in principio il feedback è un bit, un valore per sì e uno per no.
> > - **Retransmission**: ciò che è arrivato con errore viene rinviato; non esiste altra riparazione.
> 
> ---
> 
> ![[Lezione 14-1793554737733.png|100]]

Lo schema ha però due problemi: cosa succede se si corrompe l'ACK/NACK stesso, e come fa il receiver a capire che un messaggio è la ripetizione di uno precedente e non uno nuovo? La risposta è aggiungere un **sequence number** all'header dei pacchetti.

- Nello stop-and-wait c'è sempre **un solo messaggio in transito**: non serve l'intera sequenza, basta distinguere il pacchetto corrente dal precedente.
- Si aggiunge un campo `S = 0/1` che **alterna**: un valore ripetuto segnala un messaggio ripetuto.
- Il riconoscimento riporta **lo stesso bit**, così indica a quale messaggio risponde; se un NACK arriva corrotto, il sender ritrasmette e il receiver riconosce dal numero di sequenza se la ritrasmissione riguarda il pacchetto vecchio o uno nuovo.

### ACK numerati

I riconoscimenti numerati rendono i NACK superflui.

- Un **ACK numerato** identifica l'ultimo pacchetto ricevuto con successo.
- Se il sender riceve un ACK per il pacchetto precedente, il pacchetto corrente non è stato riconosciuto.
- Il receiver risponde a pacchetti corrotti e duplicati **ripetendo l'ultimo ACK**: così l'ACK fornisce sia feedback positivo che negativo, eliminando i NACK espliciti.

## Perdita di pacchetti e timeout

Secondo caso: canale in cui i pacchetti possono anche **perdersi**, cosa plausibile perché i dispositivi di rete possono andare in buffer overflow sotto traffico intenso. Lo stop-and-wait ha un chiar problema di **loop**: perso un messaggio oppure un acknowledgment, il sender non riceve mai lo stimolo per inviare il successivo e la comunicazione resta ferma per sempre; restare in attesa all'infinito non ha via d'uscita.

> [!aside]
> 
> - **Timeout**: soluzione semplice ed efficace, un timer lato sender che, scaduto, permette di ritentare; il protocollo fa ritrasmettere lo stesso pacchetto, con lo stesso numero di sequenza.
> - Il duplicato è riconosciuto dal numero di sequenza, scartato, e riconosciuto di nuovo; il receiver sa di averlo già ricevuto e si limita a rimandare l'ACK.
> - Il meccanismo funziona sia nel caso di perdita del pacchetto sia dell'acknowledgment; una query DNS su UDP fa esattamente questo: nessuna risposta in tempo, si chiede di nuovo.
> 
> ---
> 
> ![[Lezione 14-1793554957551.png|200]]

La sfida è stimare un timeout adeguato, che dipende dall'**RTT** (*Round-Trip Time*), il tempo che un pacchetto impiega per andare e tornare.

- Un timeout **troppo lungo** rallenta la comunicazione: si aspetta inutilmente, con più sicurezza ma tempi peggiori.
- Un timeout **troppo breve** fa sovrapporre i pacchetti: si rinvia mentre l'ACK stava già tornando.
- Un timeout ragionevole deve quindi essere in qualche modo più lungo dell'RTT; in questi protocolli teorici è fisso: sono strumenti concettuali, che gli algoritmi reali poi usano in modo più mirato, e il protocollo deve restare robusto tenendo conto di tutto ciò che può avvenire.

> [!warning] Il paradosso del timeout breve
> Un timer più corto dell'andata e ritorno non lascia scampo: l'acknowledgment non può arrivare prima che il timer scatti, quindi ogni messaggio viene ritrasmesso su un canale che non sta perdendo nulla, come il timer da 50 ms su un percorso da 80 ms, dove tutto va due volte e il numero di sequenza al receiver è l'unica ragione per cui il programma funziona. L'effetto paradosso è che un timeout più breve può **ritardare** la sequenza: ogni ritrasmissione rimette la finestra d'attesa e, se l'ACK arriva sistematicamente in ritardo, il ciclo si ripete fin quasi ad allungare la faccenda all'infinito.

## Prestazioni dello stop-and-wait

Il tempo totale di consegna si ragiona con l'analogia dell'acqua: c'è il tempo `t` per versare l'acqua dal serbatoio nel tubo e il tempo `RTT/2` perché il fluido attraversi il tubo; il tempo di versata si conta **una sola volta**, perché emissione e ricezione si sovrappongono (simmetria tra i due lati): l'ultima goccia arriva al serbatoio di destinazione a `RTT/2 + t`.

![[Lezione 14-1793555071675.png|200]]

Il caso di scuola: due host sulle coste opposte degli Stati Uniti, con RTT alla velocità della luce di circa 30 ms, un canale con tasso di trasmissione R = 1 Gbps e un pacchetto di L = 1000 byte (8000 bit).

- Il tempo per trasmettere il pacchetto sul canale è $t = L/R = 8000/10^9 = 8$ µs.
- L'ultimo bit entra nel canale a `t0 + 0,000008` s e il pacchetto raggiunge il receiver a `RTT/2 + L/R = 0,015008` s.
- Con ACK di dimensione trascurabile (tempo di invio ignorato), l'ACK riemerge al sender a `RTT + L/R = 0,030008` s.
- In 0,030008 s di tempo totale, il sender ha trasmesso per soli 8 µs: è rimasto ad attendere il **99,973%** del tempo, senza sfruttare minimamente la banda disponibile.

**Formula**: l'utilizzazione è la frazione del tempo totale in cui il sender trasmette, `U = (L/R) / (RTT + L/R)`; su un percorso da 100 ms di RTT con un messaggio da 1 KB e un link a 100 Mbps, `L/R` = 80 µs, quindi `U = 0,0008` e la chat si muove intorno a 80 kbps. Su loopback e in rete locale l'RTT è una frazione di millisecondo e il problema non si vede; dieci messaggi al secondo vanno bene per una chat, ma non è un modo per muovere un file, e non è ciò che fa TCP.

## Pipelining

> [!def] Pipelining
> **Tecnica** in cui, invece dello stop-and-wait, al sender è permesso inviare **più pacchetti** senza attendere i riconoscimenti.

Il pipelining impone due cambiamenti rispetto allo stop-and-wait.

- Il **range dei numeri di sequenza deve aumentare**: ogni pacchetto in transito (escluse le ritrasmissioni) deve avere un numero di sequenza univoco, e possono esserci più pacchetti in transito non riconosciuti; i pacchetti sparati a raffica possono prendere strade diverse, quindi gli ACK devono riferirsi al pacchetto giusto.
- Servono **buffer** per memorizzare i pacchetti in arrivo: non si sa se sono corretti né se ci sono "buchi" nella trasmissione, e si vuole che dopo il primo arrivi il secondo, poi il terzo e così via.

![[Lezione 14-1793555273637.png|200]]

Già mandarne tre alla volta invece di uno dà un piccolo miglioramento: il sender inizia a `t0`, l'ultimo bit dell'ultimo pacchetto entra nel canale a `t0 + 3L/R = 0,000024` s e, con ACK trascurabile, l'ultimo riconoscimento torna al sender a `RTT + L/R = 0,030024` s; l'attesa scende dal 99,973% al 99,920%. Il guadagno è minimo, ma cambia il paradigma: ci si muove verso il pipelining. I due protocolli base che lo usano sono **Go-Back-N** e **Selective Repeat**, nell'ordine di complessità; nelle forme viste non sono implementati così in pratica, ma forniscono gli strumenti concettuali a cui i protocolli reali si rifanno.

## Go-Back-N

> [!def] Go-Back-N
> **Protocollo sliding window** (detto anche *sliding-window protocol*): il sender può trasmettere più pacchetti quando disponibili senza attendere l'acknowledgment, ma con il vincolo di avere **al massimo N pacchetti non riconosciuti**. La gestione della pipeline è tutta sul sender, mentre al receiver resta pochissimo.

Il sender mantiene una finestra di pacchetti descritta da due indici: la **base**, il numero di sequenza del pacchetto non riconosciuto più vecchio, e **nextseqnum**, il più piccolo numero di sequenza non ancora usato (prossimo da inviare).

- I pacchetti in `[0, base-1]` sono trasmessi e riconosciuti: storia passata, fuori dalla finestra.
- I pacchetti in `[base, nextseqnum-1]` sono inviati ma non ancora riconosciuti.
- I pacchetti in `[nextseqnum, base+N-1]` possono essere inviati.
- I pacchetti da `base+N` in poi non sono utilizzabili finché non arriva un nuovo acknowledgment: a finestra piena il sender si ferma in attesa.

![[Lezione 14-1793555335990.png|300]]

Lato sender valgono tre meccanismi.

- **ACK cumulativi**: l'acknowledgment per il pacchetto `n` significa che tutto fino a `n` incluso è arrivato correttamente; un acknowledgment perso si ripara da solo, perché l'ACK 5 rende superflui gli ACK 3 e 4 e la finestra salta avanti.
- **Timer unico**: appartiene al pacchetto non riconosciuto più vecchio, non a ogni singolo pacchetto; alla scadenza il sender rinvia **tutti** i pacchetti in attesa (da qui il nome Go-Back-N).
- **Finestra scorrevole**: quando arriva un acknowledgment la finestra avanza e il timer viene riavviato.

> [!aside]
> Il receiver mantiene un solo numero: **expectedseqnum**, il numero di sequenza del prossimo pacchetto che è disposto a consegnare ai livelli superiori.
> 
> - Pacchetto **corretto e in ordine**: consegnato all'applicazione, riconosciuto, e si avanza di uno.
> - **Qualsiasi altro pacchetto**: scartato, anche se perfettamente valido e arrivato in anticipo, buttato esattamente come se fosse danneggiato, e ri-riconosciuto l'ultimo pacchetto in ordine ricevuto.
> - **Nessun buffer**: la complessità è deliberatamente tutta da un lato, il sender tiene una finestra, il receiver tiene un intero.
> 
> ---
> 
> ![[Lezione 14-1793555494777.png|200]]
> 

Con una finestra di quattro i pacchetti 0–3 escono in raffica, poi il sender si ferma perché la finestra è piena. `pkt2` si perde: i pacchetti 3, 4 e 5 arrivano corretti ma vengono scartati, perché il 2 non è stato consegnato; il receiver continua a rispondere ACK1, l'ultimo effettivamente consegnato all'applicazione. Scaduto il timer di `pkt2`, il più vecchio in attesa, i quattro pacchetti in coda vengono ritrasmessi, tornando all'ultimo ricevuto con successo.

I limiti del protocollo sono pesanti.

- **Una perdita, N ritrasmissioni**: i pacchetti corretti buttati via li pagano sender, receiver e canale.
- **Reazione a catena**: gli out-of-order scartati forzano ritrasmissioni successive, e più è larga la finestra più costa una singola perdita; il comportamento è peggiore proprio dove il pipelining vale di più, cioè finestra grande su un percorso veloce e lungo.
- La **ritrasmissione stessa** può perdersi o corrompersi, richiedendo a sua volta altre ritrasmissioni; le ritrasmissioni continue finiscono inoltre per intasare la rete.

## Selective Repeat

> [!def] Selective Repeat
> **Protocollo sliding window** in cui il sender ritrasmette **solo i pacchetti probabilmente ricevuti con errore** (persi o corrotti); a differenza di Go-Back-N, il receiver **bufferizza e riconosce** i pacchetti fuori ordine invece di scartarli.

Si usano **due finestre di dimensione N** per limitare i pacchetti non riconosciuti, ciascuna con la propria base: **send_base**, il bordo inferiore della finestra del sender (posizione più vecchia non ancora riconosciuta), e **rcv_base**, il bordo inferiore della finestra del receiver (prossimo pacchetto necessario per la consegna in ordine).

![[Lezione 14-1793555607247.png|200]]

Lato sender valgono tre regole.

- **Invio**: se il numero di sequenza cade nella finestra, il pacchetto viene creato e inviato, fino a finestra piena.
- **Un timer per pacchetto**: alla scadenza si rinvia quel solo pacchetto, e solo quello.
- **ACK `n`**: marca `n` come ricevuto; se `n` era la base della finestra, questa scorre fino al prossimo numero non riconosciuto, saltando in avanti di tutti i pacchetti consecutivi già riconosciuti.

Lato receiver valgono tre regole complementari.

- Un pacchetto **dentro la finestra** viene riconosciuto e, se nuovo, bufferizzato.
- Se è la **base** della finestra, viene consegnato all'applicazione insieme a tutti i pacchetti consecutivi già bufferizzati, e la finestra scorre fino a dove la contiguità è garantita.
- Un pacchetto **poco sotto la finestra** viene riconosciuto di nuovo e scartato.

> [!info] Perché riconoscere ciò che è già sotto la finestra
> Il receiver ha già quel pacchetto, consegnato tempo fa: perché rispondere? Perché il sender non sa che è arrivato. Se l'acknowledgment del pacchetto più vecchio non riconosciuto si è perso, il sender continuerebbe a ritrasmetterlo e la sua finestra non avanzerebbe mai. Le due parti non condividono la vista di ciò che è arrivato e, in Selective Repeat, questo scarto è permanente, non temporaneo: il silenzio non è mai una risposta accettabile a una ritrasmissione, perché è indistinguibile da una seconda perdita. Quindi il receiver ri-riconosce e scarta.

![[Lezione 14-1793555625703.png|200]]

In presenza di pacchetti persi il comportamento è il seguente: il receiver bufferizza `pkt3`, `pkt4` e `pkt5` mentre attende il `pkt2` perduto; solo il `pkt2` viene ritrasmesso, sul proprio timer, e nient'altro esce due volte; quando arriva, quattro pacchetti salgono all'applicazione in un colpo solo, in ordine, evitando di rinviare 3, 4 e 5 e quindi ulteriori perdite o errori di trasmissione.

### Dimensione della finestra e ambiguità

Un problema del Selective Repeat è che la finestra è vincolata allo spazio dei numeri di sequenza, e questo spazio è **finito**.

![[Lezione 14-1793555682502.png|200]]

Scenario con quattro numeri di sequenza (massimo 3) e finestra di dimensione 3: i pacchetti da 0 a 2 arrivano correttamente e i relativi ACK vengono inviati ma non ancora ricevuti; la finestra del receiver avanza comunque fino al sesto pacchetto, cioè su `[3, 0, 1]`.

- **Caso a**: gli ACK dei primi tre pacchetti si perdono e il sender li ritrasmette, il pacchetto 0 è nuovo o vecchio?
- **Caso b**: gli ACK arrivano, il sender invia 3, 0, 1 e il pacchetto 3 si perde; il receiver vede un pacchetto numerato 0 dentro la sua finestra e questa volta è dato nuovo, il pacchetto 0 è nuovo o vecchio?

I due casi producono la stessa sequenza di arrivi e sono indistinguibili: il receiver non può "vedere" il sender, quindi non può decidere se acquisire o scartare il pacchetto. Il protocollo non deve avere ambiguità di questo tipo.

Il vincolo che risolve il problema è il **massimo disallineamento delle finestre**.

- Il sender può trasmettere al più N pacchetti non riconosciuti.
- Se tutti gli N pacchetti arrivano ma i loro ACK si perdono, il receiver avanza di N posizioni mentre il sender resta bloccato sulla sua base.
- Il receiver non può avanzare oltre: senza ACK il sender non trasmette nuovi pacchetti, e il blocco del sender non alimenta lo spostamento del receiver.
- Quindi la massima distanza tra le due finestre è di **N posizioni**.

Per evitare la sovrapposizione tra finestre vecchie e nuove, lo spazio dei numeri di sequenza M deve coprire due finestre: **`M ≥ 2N`**. Con finestre di dimensione 4 servono così numeri da 0 a 7: solo quando lo 0 è uscito dalla finestra può ricomparirne uno davanti, e i due casi diventano distinguibili.

![[Lezione 14-1793555733331.png|300]]