---
type: entity
title: AF_LOCAL
tags: [socket, IPC, networking]
related: [comunicazione-locale-vs-di-rete, NamedPipe]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# AF_LOCAL

`AF_LOCAL` è una famiglia di indirizzi utilizzata per la creazione di socket locali. Questi socket permettono la comunicazione tra processi che risiedono sullo stesso host fisico, fungendo da alternativa più flessibile rispetto alle `NamedPipe`.

In questo contesto, i socket sono trattati dal kernel come file, condividendo la stessa tabella dei file aperti e le stesse primitive di I/O.