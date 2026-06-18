---
type: entity
title: pipe
tags: [unix, system-calls, pipes, ipc, communication, synchronization]
related: [mkfifo.md, SIGPIPE.md, read, write, lseek, ereditarietà-dei-file-descriptor]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-5-6-AA25-26.txt", "SO/Trascrizioni/Lezione 23.txt"]
---
# pipe
La chiamata di sistema `pipe` crea una pipe ordinaria (anonima), un meccanismo di comunicazione tra processi (IPC) che fornisce una sincronizzazione implicita. L'operazione restituisce due descrittori di file (uno per la lettura e uno per la scrittura), utilizzati tipicamente per la comunicazione tra processi padre e figlio.

A differenza dei file standard, la lettura da una `pipe` blocca il processo finché non arrivano nuovi dati, rendendole più efficienti per la comunicazione diretta tra processi rispetto all'uso di file come memoria condivisa.