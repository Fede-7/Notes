---
type: concept
title: Fasi del Processo di Avvio
tags: [boot, hardware]
related: [bootloader, firmware, system-daemon-init]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il processo di avvio del sistema operativo segue una sequenza gerarchica di caricamento:

1. **Firmware**: All'accensione, il firmware esegue il POST e cerca il codice di avvio.
2. **Bootcode**: Un piccolo frammento di codice (es. nell'MBR) viene caricato per localizzare il bootloader.
3. **Bootloader**: Il bootloader viene caricato in RAM e gestisce il caricamento del kernel.
4. **Kernel**: Il kernel viene caricato in memoria e inizia a gestire le risorse di sistema.
5. **System Daemon (Init)**: Il kernel avvia il primo processo di sistema (es. `systemd` o `init`), che avvia tutti i servizi e le applicazioni utente.
