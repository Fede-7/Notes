---
type: concept
title: Block Groups
tags: [linux, file-system, optimization]
related: [ext2, ext4]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Block Groups

L'organizzazione in **Block Groups** è una tecnica di layout del disco introdotta con EXT2 per migliorare le prestazioni del file system.

### Concetto
Invece di trattare il disco come un unico grande spazio di blocchi, il disco viene suddiviso in gruppi. Ogni gruppo contiene:
- Una propria area per gli **inode**.
- Un'area per i **blocchi di dati**.
- Metadati specifici del gruppo.

### Vantaggi
- **Località dei dati**: Il sistema operativo cerca di allocare i blocchi di dati di un file all'interno dello stesso gruppo in cui risiede il suo inode.
- **Riduzione della frammentazione**: Mantenendo i dati vicini ai loro metadati, si riducono i movimenti della testina del disco e si migliora l'efficienza della cache.
