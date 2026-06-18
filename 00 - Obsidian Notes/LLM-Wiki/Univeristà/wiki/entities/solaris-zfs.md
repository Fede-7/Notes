---
type: entity
title: Solaris ZFS
tags: [software, file-system, storage]
related: [raid]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# Solaris ZFS

**ZFS** è un file system e un gestore di storage avanzato sviluppato originariamente da Sun Microsystems.

### Caratteristiche Principali
- **Pooled Storage**: Gestisce lo spazio di archiviazione come un pool condiviso, simile all'allocazione della memoria (`malloc`/`free`).
- **Checksum**: Utilizza checksum per rilevare e correggere errori sia sui dati che sui metadati.
- **Snapshot**: Permette di creare istantanee del file system a un determinato istante di tempo.