---
type: concept
title: Prevenzione del Deadlock
tags: [deadlock, strategie]
related: [condizioni-di-coffman, lock-ordering]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Prevenzione del Deadlock

La prevenzione del deadlock consiste nell'imporre regole di sistema che impediscano il verificarsi di almeno una delle quattro **Condizioni di Coffman**.

Strategie comuni:
- **Mutual Exclusion**: Non applicabile a risorse condivisibili (es. file in sola lettura), ma non può essere eliminata per risorse esclusive.
- **Hold and Wait**: Imporre che un processo richieda tutte le risorse necessarie prima di iniziare l'esecuzione, o che rilasci tutte le risorse attuali prima di richiederne di nuove. *Svantaggio*: basso utilizzo delle risorse e possibile *starvation*.
- **No Preemption**: Se un processo richiede una risorsa non disponibile, deve rilasciare tutte le risorse attualmente detenute. Funziona solo per risorse facilmente recuperabili (CPU, DB).
- **Circular Wait**: Imporre un ordine totale sulle risorse. Ogni processo deve richiedere le risorse in un ordine di enumerazione crescente (es. $F(R_j) > F(R_i)$).
