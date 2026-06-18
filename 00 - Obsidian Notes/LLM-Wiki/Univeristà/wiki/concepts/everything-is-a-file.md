---
type: concept
title: Everything is a file
tags: [unix, philosophy]
related: [inode, file-system]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Everything is a file

Il principio **"Everything is a file"** è una filosofia di design fondamentale dei sistemi operativi Unix e Linux.

### Significato
Questo concetto implica che il sistema operativo fornisce un'interfaccia uniforme per diverse risorse hardware e software. Invece di avere API diverse per ogni dispositivo, il kernel espone quasi tutto come un file:
- Dispositivi di blocco (es. dischi rigidi).
- Dispositivi di caratteri (es. tastiere, terminali).
- Socket di rete.
- Pipe e pipe nome.
- Directory e file ordinari.

Grazie a questo approccio, i programmi possono utilizzare le stesse chiamate di sistema (come `read()`, `write()`, `open()`) per interagire con una vasta gamma di risorse.
