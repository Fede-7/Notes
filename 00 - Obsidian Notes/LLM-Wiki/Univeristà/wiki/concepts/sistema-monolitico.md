---
type: concept
title: Sistema Monolitico
tags: [kernel, architettura]
related: [strutture-del-kernel]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
---
# Sistema Monolitico

Un sistema operativo monolitico è costituito da una collezione di procedure, ognuna delle quali può chiamare qualsiasi altra. È spesso definito come un sistema "strettamente accoppiato" (*tightly coupled*).

## Caratteristiche
- **Esecuzione**: Tutte le procedure sono linkate in un unico eseguibile.
- **Efficienza**: È molto efficace ed efficiente poiché le chiamate tra componenti non richiedono passaggi complessi tra diversi spazi di memoria.
- **Svantaggi**: Poca modularità, rendendo il sistema difficile da sviluppare, estendere e mantenere man mano che cresce di complessità.
- **Esempi**: UNIX originale, MS-DOS (struttura semplice).