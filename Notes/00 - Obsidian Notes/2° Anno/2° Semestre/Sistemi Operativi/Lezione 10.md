---
date: 2026-04-08
corso: Sistemi Operativi
docente: N/D
lezione: "Valutazione algoritmi di scheduling e introduzione alla sincronizzazione"
tags: [SO, scheduling, valutazione, sincronizzazione, sezione-critica, peterson, test-and-set, compare-and-swap]
---

# SO — Lezione 10: Valutazione degli Algoritmi di Scheduling e Sincronizzazione

**Corso:** Sistemi Operativi

---

## Argomenti trattati

- Metodi di valutazione degli algoritmi di scheduling (deterministico, code, simulazione)
- Il problema del produttore-consumatore e le corse critiche
- Definizione formale di sezione critica e sue tre proprietà
- Soluzione di Peterson (2 processi) e generalizzazione a N
- Problema dell'ordinamento delle assegnazioni da parte del compilatore e memory barriers
- Supporto hardware: test-and-set e compare-and-swap
- Bounded waiting tramite compare-and-swap

---

## 1. Metodi di valutazione degli algoritmi di scheduling

Gli algoritmi di scheduling possono essere valutati con approcci di diverso livello di astrazione. È importante capire quale tipo di valutazione viene richiesta nei compiti (quella deterministica) e qual è invece il vero banco di prova pratico.

**Modelli deterministici** — Si assume un carico di lavoro specifico (una distribuzione di arrivi, di CPU burst, ecc.) e si applica l'algoritmo in modo deterministico a quel caso. Gli esercizi proposti a lezione e all'esame rientrano in questa categoria: si fotografa una situazione di processi in arrivo e si calcola il comportamento, i tempi di attesa, il turnaround, ecc. Da un singolo caso non si può inferire il comportamento generale, ma su un dataset di casi dà una prima idea.

**Modelli di coda** — Si modella ogni risorsa come una coda con proprietà statistiche sugli arrivi. In stato stazionario (tanti processi entrano, tanti ne escono, le code restano stabili) valgono leggi come la formula di Little: $N = \lambda \cdot W$, dove $N$ è il numero medio di processi in coda, $\lambda$ la frequenza degli arrivi e $W$ il tempo medio di attesa. Questi modelli sono però troppo astratti per un'analisi accurata degli algoritmi reali.

**Simulazione** — Si simulano gli arrivi e i tempi di elaborazione con generatori casuali. Più realistico, ma pur sempre limitato. Il vero banco di prova è l'implementazione diretta nel kernel.

> [!info] Il vero banco di prova
> L'unico modo per valutare davvero un algoritmo di scheduling sofisticato è inserirlo nel kernel e osservarne il comportamento nel sistema completo. L'algoritmo vive in un ecosistema e interagisce con tutto il resto: un algoritmo teoricamente ottimo può risultare non performante in pratica. Ad esempio, l'EEVDF di Linux è stato proposto come lavoro scientifico diversi anni prima di essere integrato nel kernel, proprio per la cautela necessaria nel sostituire un algoritmo già in produzione.

> [!quote]
> "Finché si trattano algoritmi molto semplici, si possono modellare in astratto, però poi per valutare effettivamente l'impatto reale bisogna immergerlo dentro il kernel."

---

## 2. Il problema della sincronizzazione: motivazione

I thread condividono lo stesso spazio di indirizzamento: possono lavorare su stesse strutture dati senza overhead di comunicazione interprocesso, ma devono sincronizzarsi per evitare le **corse critiche** (race condition).

### Il problema produttore-consumatore con buffer circolare

Un buffer circolare ha un produttore che scrive in `IN` e un consumatore che legge da `OUT`. Se si usano due thread, sia il buffer che i puntatori `IN` e `OUT` sono variabili condivise soggette a conflitti.

La soluzione con contatore esplicita il problema in modo ancora più chiaro: un thread fa `counter++` e l'altro `counter--`. A livello macchina ogni operazione si traduce in più istruzioni assembly (leggi da memoria, modifica nel registro, scrivi in memoria). Se lo scheduler interviene a metà di questa sequenza, i thread si interfogliano.

> [!example] Corsa critica sul contatore
> Supponiamo `counter = 5`. Il thread 1 legge 5 nel registro R1, aggiorna R1 a 6. Prima di scrivere in memoria, lo scheduler cede la parola al thread 2, che legge 5 nel registro R2, aggiorna R2 a 4, scrive 4 in memoria. Poi il thread 1 scrive 6. Il risultato finale è 6 invece di 5. Se avessero operato atomicamente, qualunque ordine avrebbe prodotto 5.

> [!quote]
> "Voi che cosa state ipotizzando, lanciando due thread? Che tutte queste siano operazioni atomiche. Se fossero atomiche, chi arriva prima, chi arriva dopo... non è un problema."

Il problema si amplifica su sistemi **multicore** dove c'è parallelismo reale: i thread girano su core distinti e accedono a memoria condivisa contemporaneamente. In più, le cache possono introdurre ulteriori problemi di consistenza: una modifica tenuta in cache può non essere ancora propagata in memoria globale.

---

## 3. Il problema della sezione critica

Ogni thread o processo ha porzioni di codice dove accede a dati condivisi: queste si chiamano **sezioni critiche**. Quando un processo è in sezione critica, nessun altro dovrebbe poterci entrare contemporaneamente.

La struttura del codice di ogni processo è:

```
entry section       ← richiesta di ingresso
critical section    ← accesso esclusivo
exit section        ← notifica di uscita
remainder section   ← eseguibile concorrentemente
```

> [!abstract] Definizione: Sezione critica
> Una **sezione critica** è una porzione di codice in cui vengono letti o scritti dati condivisi tra più processi o thread. Occorre che al più un processo alla volta esegua la propria sezione critica.

### Le tre proprietà richieste

Perché un meccanismo di sincronizzazione per la sezione critica sia corretto, deve soddisfare tre proprietà:

**1. Mutua esclusione** — Al più un processo alla volta può essere in sezione critica. È il minimo sindacale, ma da solo non basta.

**2. Progresso** — Se nessun processo è in sezione critica e alcuni vogliono entrarvi, la decisione su chi entra deve dipendere solo dai processi che aspettano, non da altri, e deve avvenire in tempo finito. Impedisce il caso in cui tutti aspettano indefinitamente senza che nessuno entri.

**3. Bounded waiting (attesa limitata)** — Dopo che un processo ha fatto richiesta di entrare in sezione critica, esiste un limite al numero di volte in cui altri processi possono entrare prima che a lui venga concesso l'accesso. Impedisce la starvation.

> [!warning] Mutua esclusione non è sufficiente
> Un meccanismo che garantisce solo la mutua esclusione può portare a situazioni in cui nessuno entra mai (viola il progresso) o un processo aspetta all'infinito (viola il bounded waiting). I semafori e i mutex a disposizione del programmatore garantiscono tipicamente la mutua esclusione e il progresso, ma il bounded waiting deve essere garantito dal programmatore.

---

## 4. Soluzione di Peterson

La soluzione di Peterson è una soluzione **teorica** per due processi che, nell'ipotesi di operazioni atomiche, soddisfa tutte e tre le proprietà.

**Variabili condivise:**
- `turn` — indica il processo che ha il turno (valore 0 o 1)
- `flag[2]` — array booleano: `flag[i] = true` significa che $P_i$ vuole entrare in sezione critica

**Codice per il processo $P_i$ (con $j = 1 - i$):**

```python
# Entry section
flag[i] = True          # dichiaro di voler entrare
turn = j                # cedo gentilmente il turno all'altro

while flag[j] and turn == j:   # aspetto finché l'altro vuole e ha il turno
    pass                        # busy waiting

# Critical section
# ...

# Exit section
flag[i] = False
```

> [!example] Come funziona la "gentilezza"
> Ogni processo dice: "Voglio entrare, ma ti do la precedenza." Il trucco è che l'ultimo a cedere il turno è quello che poi effettivamente aspetta. Se sia P0 che P1 cedono il turno quasi contemporaneamente, solo l'ultima assegnazione a `turn` conta: il processo che ha assegnato per ultimo ha ceduto davvero il turno all'altro, che quindi può entrare.
>
> Esempio: P0 mette `flag[0]=true`, `turn=1`. P1 mette `flag[1]=true`, `turn=0`. `turn` è ora 0, quindi P1 è bloccato nel while. P0 trova `turn==1` falso, esce dal while ed entra. Quando esce, mette `flag[0]=false` e sblocca P1.

Si può dimostrare che questo algoritmo soddisfa mutua esclusione, progresso e bounded waiting.

### Generalizzazione a N processi

La soluzione di Peterson si può estendere a N processi introducendo $N-1$ livelli di competizione. Ogni processo ha un livello che va da 0 (non interessato) a $N-1$ (accede alla sezione critica). In ogni livello c'è una "vittima" che si sacrifica lasciando avanzare gli altri. Il processo che raggiunge il livello $N-1$ entra in sezione critica. Anche questa generalizzazione soddisfa tutte e tre le proprietà, ma rimane teorica per le ragioni hardware discusse di seguito.

---

## 5. Il problema dell'ordinamento delle istruzioni: memory barriers

Anche assumendo l'atomicità delle singole operazioni, la soluzione di Peterson non è implementabile direttamente su hardware moderno perché **il compilatore non garantisce l'ordine delle assegnazioni**. Se nel codice si fa `x = 1; flag = true`, il compilatore può invertire l'ordine, perché dal suo punto di vista le due operazioni non sono correlate e può ottimizzare liberamente.

> [!example] Sincronizzazione casalinga che può fallire
> Thread 1: `while not flag: pass; print(x)` — aspetta finché flag è true, poi stampa x.
> Thread 2: `x = 100; flag = true` — scrive 100 in x, poi sblocca.
>
> Se il compilatore inverte le istruzioni del thread 2, `flag` potrebbe diventare `true` prima che `x = 100` sia scritto. Thread 1 si sblocca e stampa il vecchio valore di x.

Per garantire l'ordine si usano le **memory barriers** (`__atomic_thread_fence` in C con `memory_order_release`/`memory_order_acquire`): creano punti di sincronizzazione che forzano la propagazione delle scritture in memoria prima di procedere. Queste sono meccanismi a basso livello che il programmatore di sistema deve conoscere, ma che in genere sono incapsulati nelle primitive di sincronizzazione di alto livello.

---

## 6. Supporto hardware: test-and-set e compare-and-swap

Per costruire meccanismi di lock affidabili servono istruzioni che fanno **due cose atomicamente**. Se si fa solo una cosa alla volta, un altro thread può intromettersi nel mezzo.

### Test-and-set

```python
# Operazione atomica
def test_and_set(target: bool) -> bool:
    rv = target          # salva il vecchio valore
    target = True        # setta sempre a True
    return rv            # restituisce il vecchio valore
```

Fa due cose in una sola istruzione non interrompibile: legge il valore attuale e lo setta a `True`. Questo permette di implementare un lock:

```python
# lock inizializzato a False (aperto)
while test_and_set(lock):   # se era True (chiuso), aspetta
    pass
# --- sezione critica ---
lock = False                # sblocca
```

Il primo processo che arriva trova `lock = False`, lo legge (falso → esce dal while), e contemporaneamente lo setta a `True`, sbarrando la strada a tutti gli altri che troveranno `True` e rimarranno nel ciclo. Quando il processo in sezione critica esce, setta `lock = False` e sblocca il primo che riesce a fare il test.

Questa implementazione garantisce mutua esclusione e progresso, ma **non** il bounded waiting.

### Compare-and-swap (CAS)

Versione più generale e flessibile, disponibile come istruzione hardware su x86 (`LOCK CMPXCHG`):

```python
# Operazione atomica
def compare_and_swap(value, expected, new_val) -> int:
    rv = value
    if value == expected:
        value = new_val
    return rv    # restituisce il VECCHIO valore
```

Confronta `value` con `expected` e, solo se sono uguali, lo setta a `new_val`. Restituisce sempre il vecchio valore. Si usa analogamente al test-and-set per costruire lock (con 0 per falso e 1 per vero).

> [!tip] Differenza tra test-and-set e compare-and-swap
> Il test-and-set è binario e setta sempre a True. Il compare-and-swap è più flessibile: lo swap avviene solo se il valore attuale è quello atteso. Questo permette usi più sofisticati, come gli aggiornamenti lock-free e la costruzione di meccanismi di bounded waiting.

---

## 7. Bounded waiting tramite compare-and-swap

Per ottenere il bounded waiting con CAS si introduce un array `waiting[N]` e una rotazione circolare. Ogni processo $i$ imposta `waiting[i] = True` per dichiarare che vuole entrare, poi cerca di prendere il lock con CAS. Quando un processo esce dalla sezione critica, invece di sbloccare direttamente il lock, scorre circolarmente i processi in attesa e, trovandone uno, mette `waiting[j] = False` senza sbloccare il lock: passa il testimone al prossimo in ordine. Solo se nessuno è in attesa sblocca il lock.

Questo garantisce che ogni processo che aspetta verrà servito nell'ordine circolare, evitando la starvation.

> [!warning] Limite pratico del bounded waiting
> Questa soluzione assume di conoscere a priori il numero N di processi in competizione. In pratica, con mutex e semafori standard, il bounded waiting non è sempre garantito formalmente: lo è statisticamente, o quando il programmatore introduce esplicitamente meccanismi di turnazione. Garantire rigorosamente tutte e tre le proprietà è possibile con soluzioni teoriche come Peterson, ma richiede meccanismi hardware precisi.

---

> [!abstract] Punti chiave della lezione
> - La valutazione deterministica degli algoritmi di scheduling è quella richiesta ai compiti; il vero banco di prova è l'implementazione nel kernel.
> - Le corse critiche nascono dall'interfogliamento di istruzioni macchina su variabili condivise: anche `counter++` non è atomica.
> - Un corretto meccanismo per la sezione critica deve garantire mutua esclusione, progresso e bounded waiting.
> - La soluzione di Peterson soddisfa tutte e tre le proprietà (per due processi), ma non è implementabile direttamente senza memory barriers perché il compilatore può riordinare le assegnazioni.
> - Test-and-set e compare-and-swap sono istruzioni hardware che fanno due operazioni atomicamente: sono le fondamenta di tutti i meccanismi di sincronizzazione di alto livello.

## Prossimi argomenti

- [ ] Spin lock e mutex lock di alto livello
- [ ] Semafori: binari e contatori
- [ ] Monitor e variabili di condizione
- [ ] Deadlock e priority inversion

#SO #scheduling #valutazione #sincronizzazione #sezione-critica #peterson #test-and-set #compare-and-swap
