---
type: concept
title: Strutture di Directory
tags: [file-system, os]
related: [file-system]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Strutture di Directory

Le strutture di directory definiscono come il sistema operativo organizza e mappa i nomi dei file ai loro identificatori fisici (come gli inode).

### Evoluzione delle Strutture
1. **Single-level**: Tutti i file sono in un'unica directory (limitato e poco pratico).
2. **Two-level**: Ogni utente ha la propria directory personale.
3. **Tree-structured**: Struttura ad albero gerarchica (standard moderno), dove le directory possono contenere file e altre directory.
4. **Acyclic-Graph**: Permette a un file o directory di essere condiviso (link multipli), ma proibisce i cicli.
5. **General Graph**: Permette cicli, richiedendo tecniche complesse di Garbage Collection per la gestione della memoria.
