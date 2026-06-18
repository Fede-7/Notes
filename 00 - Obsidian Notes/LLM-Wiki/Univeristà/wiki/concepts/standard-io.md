---
type: concept
title: Standard I/O
tags: [linux, shell, flussi]
related: [ridirezione-e-pipe]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Standard I/O

In ambiente Unix, ogni programma opera normalmente su tre canali di comunicazione standard, identificati da codici numerici:

| Canale | Codice | Descrizione | Default |
|--------|--------|-------------|---------|
| Standard Input (stdin) | 0 | Da cui il programma acquisisce i dati di input. | Tastiera |
| Standard Output (stdout) | 1 | Dove il programma produce i dati di output. | Schermo |
| Standard Error (stderr) | 2 | Dove il programma invia i messaggi di errore. | Schermo |
