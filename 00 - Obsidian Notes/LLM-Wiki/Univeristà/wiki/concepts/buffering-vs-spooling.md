---
type: concept
title: Buffering vs. Spooling
tags: [io, systems]
related: [caching, gestione-risorse]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# Buffering vs. Spooling

Entrambe le tecniche sono utilizzate per gestire l'I/O, ma con scopi differenti:

- **Buffering**: Consiste nella memorizzazione temporanea dei dati durante il trasferimento tra due dispositivi o tra un dispositivo e la memoria principale. Serve a gestire differenze di velocità o di dimensione dei blocchi di dati.
- **Spooling**: Permette la sovrapposizione dell'accesso a una periferica da parte di più job. I dati vengono inviati a un dispositivo di memorizzazione intermedia (spool) prima di essere elaborati dalla periferica finale.