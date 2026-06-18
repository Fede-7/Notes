---
type: concept
title: busy-waiting
tags: [sincronizzazione, spin-lock, performance]
related: [spin-lock, context-switch, atomicità]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 11.txt"]
---
# busy-waiting

Il *busy waiting* è uno stato in cui un processo occupa la CPU eseguendo un ciclo continuo per monitorare una condizione (es. la liberazione di un lock).

- **Vantaggio**: Evita il *context switch* se l'attesa è molto breve.
- **Svantaggio**: Spreca cicli di CPU se l'attesa è lunga o se il sistema è a core singolo.
È la tecnica alla base degli *spinlock*.