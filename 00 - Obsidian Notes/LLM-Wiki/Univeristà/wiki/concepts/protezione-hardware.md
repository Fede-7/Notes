---
type: concept
title: Protezione Hardware
tags: [sicurezza, architettura]
related: [dual-mode, protezione-memoria, protezione-temporale]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione1-AA25-26.txt"]
---
# Protezione Hardware

La sicurezza del sistema operativo non dipende solo dal software, ma richiede supporto hardware per impedire ai processi utenti di sovrascrivere il kernel o accedere a risorse non autorizzate. I meccanismi includono:
- **Bit di modalità** per distinguere User e Kernel mode.
- **Timer** per prevenire la monopolizzazione della CPU.
- **Registri Base e Limite** per definire i range di memoria accessibili.