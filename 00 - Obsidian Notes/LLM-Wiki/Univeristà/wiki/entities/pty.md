---
type: entity
title: PTY
tags: [kernel, I/O, terminale, pseudo-terminale]
related: [tty, line-discipline, disaccoppiamento-tty-pty, comunicazione-master-slave]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 25.txt", "SO/Trascrizioni/Lezione 26.txt"]
---
# PTY

Un **PTY** (Pseudo-terminale) è un dispositivo virtuale e un'emulazione software utilizzato per simulare un terminale fisico. Permette a processi non interattivi e applicazioni (come la shell) di comunicare con software che si aspettano un terminale reale, risultando fondamentale negli ambienti grafici.

### Architettura Master-Slave
Il PTY opera con un modello di accoppiamento master-slave che permette il [[disaccoppiamento-tty-pty]]:

- **PTY Master**: Associato all'ambiente grafico (GUI). È responsabile della gestione della finestra, della cattura dell'input della tastiera e della visualizzazione dell'output.
- **PTY Slave**: Associato al driver del terminale. È l'interfaccia con cui la shell (es. Bash) comunica, simulando il comportamento di un terminale fisico.

In questo meccanismo, la shell interagisce con lo slave mentre la GUI gestisce il master.