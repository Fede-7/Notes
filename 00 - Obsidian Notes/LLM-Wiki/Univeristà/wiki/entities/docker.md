---
type: entity
title: Docker
tags: [container, docker, virtualizzazione, containerizzazione, devops]
related: [containerizzazione, virtualizzazione]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt", "SO/Trascrizioni/Lezione 29.txt"]
---
# Docker

**Docker** è una piattaforma di containerizzazione utilizzata per isolare le applicazioni e le loro dipendenze in unità indipendenti chiamate container. 

A differenza della virtualizzazione completa (macchine virtuali), Docker sfrutta le proprietà e le primitive del kernel del sistema operativo host (come i *namespace*) per creare ambienti compartimentati. Poiché i container condividono il kernel dell'host, risultano più "light" e veloci rispetto alle macchine virtuali, garantendo al contempo stabilità e portabilità degli ambienti di esecuzione.

### Caratteristiche Tecniche e Isolamento
Docker utilizza le primitive del kernel per isolare specificamente i seguenti elementi:
- **Spazio di lavoro** (workspace)
- **File system**
- **Configurazioni di rete**

Questo approccio permette di garantire:
- **Portabilità**: Gli ambienti di esecuzione possono essere spostati facilmente tra diversi sistemi.
- **Isolamento delle risorse**: Ogni container opera in un ambiente compartimentato che protegge le risorse del sistema.
- **Efficienza**: La condivisione del kernel riduce l'overhead rispetto alla virtualizzazione tradizionale.