---
type: concept
title: Sistema Stratificato
tags: [kernel, architettura, THE]
related: [strutture-del-kernel]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
---
# Sistema Stratificato

In un sistema operativo stratificato, il software è suddiviso in un numero di livelli (layers), dove ogni livello è costruito sopra quello inferiore.

## Struttura
- **Layer 0**: Rappresenta l'hardware fisico.
- **Layer N**: Rappresenta l'interfaccia utente.
- **Modularità**: Ogni strato utilizza le funzioni e i servizi forniti dai livelli sottostanti.

## Esempio Storico
Il sistema **THE**, realizzato da Dijkstra nel 1968 per il computer Electrologica X8, è un esempio classico di architettura stratificata.