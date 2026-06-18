---
type: concept
title: signal
tags: [semaforo, sincronizzazione]
related: [wait, semaforo]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 11.txt"]
---
# signal

L'operazione `signal` (storicamente indicata con la lettera **V**) è un'operazione atomica utilizzata nei semafori.

Essa incrementa il valore del semaforo $S$. Se ci sono processi in attesa, il semaforo "risveglia" uno di essi, permettendogli di procedere.