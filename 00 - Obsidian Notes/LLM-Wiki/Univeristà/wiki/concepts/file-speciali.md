---
type: concept
title: File Speciali
tags: [unix, file-system]
related: [everything-is-a-file]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# File Speciali

In Unix, vige la filosofia "**everything is a file**": se qualcosa non è un file, è un processo. Questo significa che il sistema operativo fornisce un'interfaccia uniforme per accedere a diversi tipi di risorse.

I **File Speciali** permettono ai programmi di interagire con hardware e servizi di sistema utilizzando le stesse chiamate di sistema (*read, write, open*) utilizzate per i file ordinari. Tra questi troviamo:
- **Character Special Files**: Dispositivi che trasmettono dati carattere per carattere (es. terminali, tastiere).
- **Block Special Files**: Dispositivi che trasmettono dati in blocchi (es. dischi rigidi).
- **Socket Files**: Utilizzati per la comunicazione tra processi (IPC).
- **Named Pipes**: Canali di comunicazione unidirezionali.