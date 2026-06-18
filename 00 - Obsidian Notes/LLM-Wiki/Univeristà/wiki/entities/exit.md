---
type: entity
title: exit()
tags: [unix, system-calls, processi, system-call, process-management]
related: [wait.md, SIGCHLD.md, fork, waitpid, execve]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-5-6-AA25-26.txt", "SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# exit()

La chiamata di sistema `exit()` viene utilizzata per terminare volontariamente l'esecuzione di un processo, liberando le risorse allocate e restituendo uno stato di uscita.

## Descrizione
- **Sintassi**: `exit(status)`

## Funzionamento
- **Liberazione Risorse**: Il sistema libera tutte le risorse allocate al processo durante la sua esecuzione.
- **Comunicazione**: Comunica lo stato finale al processo padre (se presente) e invia un segnale pertinente.
- **Stato di Uscita**: Restituisce un valore che indica l'esito della terminazione del processo.