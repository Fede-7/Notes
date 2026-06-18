---
type: concept
title: Sistema Ibrido
tags: [kernel, architettura, macOS, Windows]
related: [strutture-del-kernel, sistema-monolitico, sistema-microkernel]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
---
# Sistema Ibrido

Un sistema operativo ibrido combina diversi approcci architettonici (monolitico e microkernel) per bilanciare le esigenze di prestazioni, sicurezza e usabilità.

## Caratteristiche
- **Combinazione**: Non è un modello "puro". Ad esempio, può avere un kernel che appare monolitico ma che utilizza strutture di microkernel per alcune parti critiche.
- **Esempi Moderni**:
    - **Windows**: Per lo più monolitico, ma utilizza strutture di microkernel per diverse parti del sottosistema.
    - **macOS**: Basato sul kernel XNU, che combina Mach (microkernel) e BSD (monolitico).
- **Obiettivo**: Ottimizzare le prestazioni riducendo i context switch tipici dei microkernel puri, mantenendo al contempo una certa modularità.