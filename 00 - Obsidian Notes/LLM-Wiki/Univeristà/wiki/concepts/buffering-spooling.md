---
type: concept
title: Buffering e Spooling
tags: [I/O, efficienza]
related: [batch-processing]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione1-AA25-26.txt"]
---
# Buffering e Spooling

Tecniche utilizzate per disaccoppiare la velocità della CPU da quella dei dispositivi I/O:
- **Buffering**: Utilizzo di aree di memoria dedicate per ogni dispositivo periferico per parallelizzare le letture/scritture.
- **Spooling** (Simultaneous Peripheral Operation On Line): Consente a più job di accedere a una periferica non condivisibile (es. una stampante) scrivendo l'output in una coda su disco; lo spooler poi invia i dati alla periferica uno alla volta.