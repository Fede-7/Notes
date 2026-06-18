---
type: concept
title: Modalità Operativa Duale
tags: [protezione, sicurezza]
related: [trap-exception, kernel]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione1-AA25-26.txt"]
---
# Modalità Operativa Duale

La **Modalità Operativa Duale** è un meccanismo di protezione hardware che distingue tra:
- **User Mode** (Modalità Utente): Privilegi limitati, dove vengono eseguiti i programmi applicativi.
- **Kernel Mode** (Modalità Privilegiata): Accesso totale all'hardware, riservato al nucleo del sistema operativo.

Il passaggio tra le due modalità avviene tramite interruzioni o chiamate di sistema.