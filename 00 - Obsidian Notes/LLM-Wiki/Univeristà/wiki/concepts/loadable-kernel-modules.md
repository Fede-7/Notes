---
type: concept
title: Loadable Kernel Modules
tags: [kernel, linux, modularità]
related: [strutture-del-kernel, sistema-monolitico]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
---
# Loadable Kernel Modules (LKMs)

I **Loadable Kernel Modules (LKMs)** sono componenti del kernel che possono essere caricati e scaricati dinamicamente durante l'esecuzione del sistema operativo, senza necessità di riavvio.

## Caratteristiche
- **Modularità**: Ogni componente principale (driver, file system, ecc.) è separato.
- **Interfacce**: Ogni modulo comunica con gli altri tramite interfacce note.
- **Flessibilità**: Simile al sistema a livelli (perché il core espone interfacce), ma più flessibile del sistema a microkernel poiché non richiede necessariamente un passaggio di messaggi (message passing) continuo tra ogni operazione.
- **Utilizzo**: Utilizzati in sistemi come Linux, Solaris e macOS per estendere le funzionalità del kernel in modo dinamico.