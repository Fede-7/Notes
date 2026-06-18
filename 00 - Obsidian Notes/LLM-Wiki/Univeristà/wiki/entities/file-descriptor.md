---
type: entity
title: File Descriptor
tags: [linux, unix, programming]
related: [file-control-block-fcb, file-system]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# File Descriptor

Un **File Descriptor** è un identificatore numerico assegnato da un sistema operativo a un processo per ogni file aperto.

### Funzionamento
- Quando un programma effettua una chiamata di sistema `open()`, il kernel assegna il più piccolo numero disponibile come file descriptor.
- Questo numero funge da indice in una tabella di file aperti specifica del processo.
- Permette al programma di interagire con il file tramite chiamate standard (es. `read(fd, ...)`), dove `fd` è il descrittore.
