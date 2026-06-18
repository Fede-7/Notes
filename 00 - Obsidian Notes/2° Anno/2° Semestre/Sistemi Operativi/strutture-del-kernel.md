---
type: concept
title: Strutture del Kernel
tags: [kernel, architettura, SO]
related: [sistema-monolitico, sistema-microkernel, sistema-ibrido, sistema-stratificato]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
---
# Strutture del Kernel

La struttura del kernel definisce come le procedure del sistema operativo sono organizzate e come interagiscono tra loro.

## Modelli Principali
- **Monolitico**: Tutte le procedure del kernel sono linkate in un unico eseguibile. Ogni procedura può chiamare qualsiasi altra. È molto efficiente ma può essere difficile da mantenere e meno modulare.
- **Stratificato**: Il sistema è suddiviso in livelli gerarchici. Ogni livello utilizza le funzioni dei livelli inferiori. Esempio storico: THE.
- **Microkernel**: Sposta la maggior parte dei servizi (file system, driver, ecc.) nello spazio utente, mantenendo nel kernel solo le funzioni essenziali: IPC (Inter-Process Communication), gestione della memoria e gestione dei processi.
- **Ibrido**: Combina elementi di diversi modelli per bilanciare prestazioni e modularità. Molti sistemi moderni (Windows, macOS) sono ibridi.

## Moduli del Kernel (LKMs)
Molti sistemi moderni utilizzano i **Loadable Kernel Modules (LKMs)**. Questi permettono di caricare e scaricare componenti del kernel dinamicamente durante l'esecuzione, offrendo una flessibilità simile ai microkernel ma mantenendo l'efficienza del modello monolitico.