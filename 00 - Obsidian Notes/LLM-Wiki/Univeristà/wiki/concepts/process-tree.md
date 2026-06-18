---
type: concept
title: Process Tree
tags: [process-management, architecture]
related: [fork, waitpid, execve]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# Process Tree

Il **Process Tree** è la rappresentazione gerarchica delle relazioni padre-figlio tra i processi in esecuzione.
- Un processo può generare processi figli (es. Processo A crea B e C).
- I figli possono a loro volta generare ulteriori processi figli, creando una struttura ad albero.