---
date: 2026-04-01
corso: Sistemi Operativi
docente: N/D
lezione: Scheduling — SJF preemptive, Round-Robin, Priorità e Code Multiple
tags:
  - SO
  - scheduling
  - SJF
  - round-robin
  - priority
  - code-multiple
  - starvation
  - aging
---

# SO — Lezione 9: Scheduling — SJF Preemptive, Round-Robin, Priorità e Code Multiple

**Corso:** Sistemi Operativi

---

## Argomenti trattati

- Riepilogo SJF e stima via media esponenziale
- Shortest Remaining Time First (SJF preemptive)
- Scheduling con priorità: preemptive e non-preemptive
- Problema della starvation e meccanismo di aging
- Algoritmo Round-Robin (RR): quanto di tempo e trade-off
- Scheduling con priorità + Round-Robin
- Code multiple (Multi-Level Queue)
- Code multiple con feedback (Multi-Level Feedback Queue)
- Scheduling su sistemi multicore (cenni)

---

## 1. Riepilogo: SJF e media esponenziale

Lo **Shortest Job First** (SJF) dà la precedenza al processo con il burst di CPU stimato più breve. È ottimale per il tempo medio di attesa, ma richiede di stimare i burst futuri.

La **media esponenziale** permette di stimare il prossimo burst:

$$\tau_{n+1} = \alpha \cdot t_n + (1-\alpha) \cdot \tau_n$$

dove $t_n$ è il burst effettivo e $\tau_n$ la stima precedente. Con $\alpha = 0.5$, esempio:

| Stima $\tau_n$ | Burst reale $t_n$ | Nuova stima $\tau_{n+1}$ |
|---|---|---|
| 10 | 6 | 8 |
| 8 | 4 | 6 |
| 6 | ... | ... |

La formula espansa mostra un **exponential fading**: i burst più lontani nel tempo contribuiscono meno, pesati da $(1-\alpha)^k$.

---

## 2. Shortest Remaining Time First (SJF preemptive)

Variante preemptive di SJF: ogni volta che arriva un nuovo processo, lo scheduler confronta il suo burst con il **tempo rimanente** del processo in esecuzione. Se il nuovo processo richiede meno tempo, avviene la prelazione.

> [!example] Esempio SRTF con tempi di arrivo
> Processi: P1 (arr.0, burst 8), P2 (arr.1, burst 4), P3 (arr.2, burst 9), P4 (arr.3, burst 5).
>
> - T=0: solo P1 → P1 in CPU.
> - T=1: arriva P2 (burst 4 < P1 rimanente 7) → prelazione, parte P2.
> - T=2: arriva P3 (burst 9 > P2 rimanente 3) → P2 continua.
> - T=3: arriva P4 (burst 5 > P2 rimanente 2) → P2 continua e finisce a T=5.
> - T=5: confronto P1 (rimanente 7), P3 (9), P4 (5) → P4 prima.
> - P4 finisce a T=10. Poi P1 (7), poi P3 (9).
>
> **Formula generale per il tempo di attesa**: $\text{attesa} = \text{fine} - \text{arrivo} - \text{burst}$

> [!tip] Differenza tra SJF non-preemptive e SRTF
> SJF non-preemptive: quando parte un processo, finisce senza interruzioni. SRTF: ad ogni evento (arrivo, fine) lo scheduler rivaluta tutto. SRTF minimizza il tempo medio di attesa meglio di SJF non-preemptive.

---

## 3. Scheduling con priorità

Ad ogni processo viene assegnato un numero di priorità. Lo scheduler dà la CPU al processo con la priorità più alta.

- In Linux/POSIX: **numero più basso = priorità più alta** (priorità 1 è la massima).
- **Preemptive**: se arriva un processo a priorità più alta, prelaziona quello in esecuzione.
- **Non-preemptive**: il processo in esecuzione finisce il suo burst, poi si sceglie il prossimo.

> [!example] Gantt con priorità (non-preemptive)
> Processi (tutti arrivano a t=0): P1 (burst 10, pr.3), P2 (burst 1, pr.1), P3 (burst 2, pr.4), P4 (burst 1, pr.5), P5 (burst 5, pr.2).
>
> Ordine: P2 (pr.1), P5 (pr.2), P1 (pr.3), P3 (pr.4), P4 (pr.5).

> [!warning] Starvation
> Con priorità fissa, processi a bassa priorità possono aspettare indefinitamente se continuano ad arrivare processi ad alta priorità. Questo si chiama **starvation**.
>
> **Soluzione: aging** — la priorità di un processo aumenta col tempo di attesa. Dopo un tempo sufficiente, anche il processo a bassa priorità avrà una priorità abbastanza alta da essere schedulato.

---

## 4. Round-Robin (RR)

Ogni processo riceve un **quanto di tempo** (time quantum, tipicamente 10-100 ms). Alla scadenza del quanto, se il processo non è terminato, viene rimesso in fondo alla coda Ready e si schedula il successivo.

**Caratteristiche**:
- Nessuna starvation: ogni processo viene schedulato entro $n-1$ quanti (con $n$ processi).
- Non richiede stime dei burst time.
- Equo: tutti i processi ricevono lo stesso tempo di CPU.

> [!example] Gantt Round-Robin con quanto = 4
> P1 (burst 24), P2 (burst 3), P3 (burst 3). Tutti arrivano a t=0.
>
> ```
> | P1(4) | P2(3) | P3(3) | P1(4) | P1(4) | P1(4) | P1(4) | P1(4) |
> 0       4       7      10      14      18      22      26      30
> ```
> P2 e P3 finiscono dentro il loro quanto (non consumano i 4 ms interi).

### Calibrazione del quanto

Il quanto di tempo deve essere calibrato con attenzione:

| Quanto troppo grande | Quanto troppo piccolo |
|---|---|
| Degrada a FCFS (tutti finiscono nel quanto) | Troppi context switch → overhead elevato |
| Nessun overhead | Se quanto ≈ context switch, la CPU spreca il 50% del tempo |

> [!abstract] Regola empirica
> Se l'80% dei CPU burst è più corto del quanto, il quanto è ben calibrato: la maggior parte dei processi finisce senza dover essere prerilasciata, minimizzando i context switch.

**Turnaround vs. quanto**: aumentare il quanto non riduce sempre il turnaround medio — dipende dalla distribuzione dei burst. Il turnaround medio può variare in modo non monotono con il quanto.

---

## 5. Priorità + Round-Robin

I processi sono divisi in classi di priorità. Processi con la stessa priorità si alternano in Round-Robin.

> [!example] Gantt con priorità + RR (quanto = 2)
> P1 (burst 4, pr.3), P2 (burst 7, pr.2), P3 (burst 3, pr.2), P4 (burst 2, pr.1), P5 (burst 4, pr.3).
>
> - P4 (pr.1) prima: esegue da 0 a 2 e finisce.
> - P2 e P3 (pr.2, stessa priorità) in Round-Robin: P2 fa 2, P3 fa 2, P2 fa 2, P3 fa 1 e finisce, P2 fa 2 e finisce.
> - P1 e P5 (pr.3) in Round-Robin.

---

## 6. Code multiple (Multi-Level Queue)

Invece di un'unica coda Ready, si usano **code separate per ogni livello di priorità**. Ogni coda può avere il proprio algoritmo di scheduling interno.

```
Priorità 0 (sistema)   ─── Round-Robin
Priorità 1 (interattivi) ─ Round-Robin  
Priorità 2 (batch)     ─── FCFS
Priorità 3 (background)─── FCFS
```

**Schedulazione tra code**: la coda a priorità più alta viene servita prima. Solo quando è vuota si serve la successiva (rischio di starvation per le code basse).

**Alternativa**: time slice per ogni coda — si assegna a ciascuna coda una percentuale del tempo di CPU (es. pr.0 → 80%, pr.1 → 15%, pr.2 → 5%).

> [!warning] Problema delle code multiple fisse
> I processi sono assegnati a una coda in modo permanente (come le caste). Non c'è possibilità di promozione o declassamento. Il rischio di starvation per le code basse rimane.

---

## 7. Code multiple con feedback (Multi-Level Feedback Queue)

Variante più flessibile: i processi possono **muoversi tra le code** in base al loro comportamento.

**Criteri di movimento**:
- **Promozione** (aging): un processo che aspetta troppo viene spostato a una coda a priorità più alta.
- **Declassamento**: un processo che usa troppo CPU (CPU-bound) viene spostato a una coda a priorità più bassa.

> [!example] Schema con 3 code e declassamento
> - Q0: RR con quanto = 8 ms
> - Q1: RR con quanto = 16 ms
> - Q2: FCFS
>
> Un nuovo processo entra in Q0. Se non termina in 8 ms, viene spostato in Q1. Se non termina in 16 ms, va in Q2 (FCFS, nessuna prelazione). Questo favorisce naturalmente i processi brevi (I/O bound) che finiscono nelle code alte, mentre i processi lunghi (CPU-bound) "affondano" nelle code basse.

**Lo scheduler MLFQ è il più flessibile e complesso**: deve gestire il numero di code, gli algoritmi per ciascuna, i criteri di promozione e declassamento, e il metodo di assegnazione iniziale.

---

## 8. Scheduling su sistemi multicore (cenni)

Con più core, lo scheduler deve anche decidere **su quale core** eseguire ogni thread.

**Approcci**:
- **Coda comune**: tutti i core pescano dalla stessa coda Ready. Semplice, ma può creare contention sulla struttura dati.
- **Code private per core** (più comune): ogni core ha la propria coda Ready. Migliora la località della cache (affinity), ma richiede bilanciamento del carico tra le code.

**Load balancing**:
- **Push migration**: un processo verifica periodicamente i carichi e sposta task dai core sovraccarichi.
- **Pull migration**: un core idle va a "rubare" task dalla coda di un core occupato.

> [!important] Affinità del processore (CPU affinity)
> Un thread che ha già eseguito su un core ha i suoi dati in quella cache. Migrarlo su un altro core implica invalidare la cache → costo. Lo scheduler tende a mantenere un thread sullo stesso core (soft affinity) o può forzarlo (hard affinity).

---

> [!summary] Punti chiave della lezione
> - SRTF (SJF preemptive) prelaziona quando arriva un processo con burst rimanente più breve; minimizza il tempo di attesa medio meglio di SJF non-preemptive.
> - La priorità fissa causa starvation; l'aging la previene alzando la priorità dei processi che aspettano.
> - Round-Robin è equo e senza starvation; il quanto deve essere abbastanza grande rispetto al context switch ma abbastanza piccolo per garantire reattività.
> - Le code multiple permettono politiche diverse per classi diverse di processi.
> - Le code multiple con feedback aggiungono promozione e declassamento per adattarsi al comportamento osservato.

## Prossimi argomenti

- [ ] Scheduling real-time: Rate Monotonic e Earliest Deadline First
- [ ] Scheduling su Linux (CFS e EEVDF)
- [ ] Esercitazione pratica sullo scheduling

#SO #scheduling #SJF #round-robin #priority #starvation #aging #code-multiple
