---
type: concept
title: Boot Process
tags: [hardware, boot-process]
related: [uefi, gpt, mbr]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# Boot Process

Il **boot process** è la sequenza di operazioni che permette al computer di passare dallo stato di spegnimento al caricamento del sistema operativo.

1. **Firmware**: All'accensione, il firmware (BIOS o UEFI) esegue il POST (Power-On Self-Test).
2. **Bootloader**: Il firmware identifica il dispositivo di avvio e carica il bootloader (es. GRUB).
3. **Kernel**: Il bootloader carica il kernel del sistema operativo in memoria e avvia il processo di inizializzazione.