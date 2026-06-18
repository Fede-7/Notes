---
type: concept
title: Line Discipline
tags: [terminale, kernel, TTY]
related: [tty, canon-vs-raw-mode.md]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 26.txt"]
---
# Line Discipline

La **Line Discipline** è un interprete software che elabora i flussi di dati dei terminali. Il suo compito è eseguire l'editing locale (es. gestire il tasto backspace) e interpretare i segnali (es. trasformare `Ctrl+C` in `SIGINT`).

I terminali sono un'eccezione alla regola generale dei dispositivi a carattere perché il kernel esegua un pre-processing delle richieste di `read` e `write` tramite la Line Discipline prima di consegnarle all'applicazione.
