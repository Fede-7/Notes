---
type: concept
title: Processo di Avvio UEFI
tags: [boot, modern]
related: [uefi-unified-extensible-firmware-interface, efi-system-partition]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il processo di avvio in architetture moderne basate su **UEFI** segue una sequenza specifica:

1. **POST**: Test iniziale dell'hardware.
2. **Consultazione GPT**: Il firmware legge la tabella delle partizioni GPT.
3. **Localizzazione ESP**: Il firmware identifica la **EFI System Partition (ESP)**.
4. **Caricamento Boot Manager**: Viene caricato il boot manager dall'ESP.
5. **Caricamento Kernel**: Il boot manager carica il kernel del sistema operativo desiderato.
