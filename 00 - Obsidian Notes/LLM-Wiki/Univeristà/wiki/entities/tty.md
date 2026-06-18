---
type: entity
title: TTY
tags: ["kernel", "I/O", "terminale", "dispositivo-a-carattere"]
related: ["line-discipline", "pty", "canon-vs-raw-mode", "disaccoppiamento-tty-pty"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 25.txt", "SO/Trascrizioni/Lezione 26.txt"]
---
# TTY

Il **TTY** (Teletype o Teletypewriter) è un dispositivo terminale storico, trattato nei sistemi Unix-like come un **dispositivo a carattere**. Originariamente utilizzato per l'interazione tra l'utente e il sistema operativo tramite tastiera e schermo, il TTY fisico è oggi raramente utilizzato direttamente.

## Evoluzione e Simulazione
In un ambiente moderno, la funzione del TTY fisico è stata assorbita da:
- Emulatori di terminale.
- Pseudo-terminali (pty).

## Elaborazione del Kernel
I terminali rappresentano un'eccezione alla regola generale dei dispositivi a carattere. Questo perché il kernel esegue un pre-processing delle richieste di `read` e `write` tramite la [[line-discipline]].