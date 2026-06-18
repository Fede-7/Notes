---
type: query
title: "Come gestire efficacemente la popolazione di zombie?"
tags: [processi, kernel, server]
related: [gestione-zombie, wait]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# Come gestire efficacemente la popolazione di zombie?

In un server ad altissimo traffico, come si può gestire la popolazione di processi zombie senza bloccare il processo padre o esaurire la tabella dei processi? 
Esistono tecniche come l'uso di handler `SIGCHLD` o la creazione di un processo "zombie reaper" dedicato?

---FILE: wiki/queries/come-implementare-protocolli-di-comunicazione-complessi.md---
---
type: query
title: "Come implementare protocolli di comunicazione complessi?"
tags: [networking, socket, protocolli]
related: [modello-client-server, lettura-robusta]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# Come implementare protocolli di comunicazione complessi?

Oltre al semplice modello richiesta-risposta analizzato in lezione, quali sono le migliori pratiche per implementare protocolli di comunicazione complessi (es. gestione di stati, messaggi multi-parte, gestione degli errori di rete) utilizzando le primitive dei socket?