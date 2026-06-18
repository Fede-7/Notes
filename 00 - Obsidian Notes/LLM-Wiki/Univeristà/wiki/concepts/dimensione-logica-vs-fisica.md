---
type: concept
title: Dimensione logica vs. fisica
tags: [file-system, storage]
related: [stat, lseek, file-hole]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
Esiste una distinzione fondamentale tra la dimensione di un file e lo spazio che occupa effettivamente sul disco:
- **Dimensione Logica**: La distanza totale tra l'inizio e la fine del file (mantenuta nell'inode). È il valore visualizzato da comandi come `ls -lh`.
- **Dimensione Fisica**: Lo spazio effettivamente allocato sui blocchi del disco. È il valore visualizzato da comandi come `du -h`.

Questa distinzione permette la creazione di "buchi" nei file.