---
type: entity
title: EXT2
tags: [linux, file-system]
related: [ext3, ext4, block-groups]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# EXT2

**EXT2** è un file system Linux che ha introdotto l'organizzazione del disco in **Block Groups**.

### Innovazioni
- **Block Groups**: Il disco è diviso in gruppi per mantenere vicini gli inode e i blocchi di dati dei file correlati, riducendo la frammentazione e migliorando la località dei dati.
