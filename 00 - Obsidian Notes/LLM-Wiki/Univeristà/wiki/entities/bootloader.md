---
type: entity
title: Bootloader
tags: [boot, software]
related: [bootcode, uefi-unified-extensible-firmware-interface, system-daemon-init]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il **Bootloader** è un programma caricato in memoria RAM dal firmware (BIOS o UEFI) che ha il compito di caricare il kernel del sistema operativo in memoria e avviarlo.

### Esempi e Funzioni
- **GRUB**: Uno dei bootloader più comuni per sistemi Linux.
- **Multi-boot**: Permette all'utente di scegliere quale sistema operativo avviare se ne sono installati più di uno sullo stesso disco.
- **Transizione**: Segna il passaggio dal codice di avvio iniziale (bootcode) all'esecuzione del sistema operativo vero e proprio.
