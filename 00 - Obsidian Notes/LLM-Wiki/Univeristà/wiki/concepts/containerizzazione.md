---
type: concept
title: Containerizzazione
tags: [docker, virtualizzazione, kernel, isolamento]
related: [docker, virtualizzazione]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt", "SO/Trascrizioni/Lezione 29.txt"]
---
# Containerizzazione

La **containerizzazione** è una tecnica di isolamento che permette di eseguire applicazioni in ambienti separati (container) che condividono il kernel del sistema operativo host. Questa tecnica si basa sulle proprietà del kernel, in particolare sui *namespace*.

## Confronto con la Virtualizzazione
A differenza della virtualizzazione completa, i container non replicano l'hardware né il sistema operativo. Mentre la virtualizzazione crea macchine virtuali complete, la containerizzazione isola specificamente:
- Lo spazio di lavoro
- Il file system
- Le risorse di rete

## Vantaggi
L'approccio basato sui container offre diversi vantaggi rispetto alla virtualizzazione delle macchine virtuali, rendendolo una soluzione più efficiente per la distribuzione di applicazioni:

- **Efficienza delle risorse:** Minore consumo di memoria e CPU grazie alla condivisione del kernel.
- **Velocità:** Tempi di avvio significativamente più rapidi.
- **Portabilità:** Permette di creare ambienti isolati e portabili, garantendo che l'applicazione funzioni in modo coerente su diversi sistemi.
- **Gestione:** Maggiore facilità di gestione, specialmente in ambienti di cluster.