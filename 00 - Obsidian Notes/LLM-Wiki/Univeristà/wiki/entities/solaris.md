---
type: entity
title: Solaris
tags: [os, unix-like]
related: [second-chance-solaris]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
# Solaris
Solaris implementa un meccanismo di sostituzione delle pagine basato su una variante del sistema a "due lancette", descritto come [[second-chance-solaris]]. Questo sistema utilizza due puntatori (*front-end* e *back-end*) per scansionare le pagine e determinare la loro "seconda possibilità" di permanenza in memoria.