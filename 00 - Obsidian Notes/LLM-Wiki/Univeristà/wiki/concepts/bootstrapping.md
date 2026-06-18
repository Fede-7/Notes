---
type: concept
title: Bootstrapping
tags: [firmware, architettura-computer]
related: [uefi, mbr, gpt]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 24.txt"]
---
# Bootstrapping
Il **bootstrapping** è la fase iniziale di caricamento del codice dal disco prima dell'avvio del kernel. Durante questa fase, il sistema operativo non è ancora attivo e le strutture dati complesse non sono disponibili; il processo è gestito dal firmware (BIOS/UEFI).