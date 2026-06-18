---
type: concept
title: gestione-zombie
tags: [processi, kernel, IPC]
related: [wait, SIGPIPE]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# gestione-zombie

La gestione degli zombie è necessaria per prevenire l'accumulo di processi figli terminati che rimangono nella tabella dei processi del sistema. Un processo "zombie" occupa una voce nella tabella dei processi finché il processo padre non legge il suo stato di uscita tramite la chiamata `wait()` o non gestisce il segnale `SIGCHLD`. In un server ad alto traffico, la mancata gestione può portare all'esaurimento delle risorse del sistema.