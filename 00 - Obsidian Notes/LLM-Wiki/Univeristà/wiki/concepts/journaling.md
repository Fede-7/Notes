---
type: concept
title: Journaling
tags: [file-system, consistency]
related: [ext3, ext4, copy-on-write]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Journaling

Il **Journaling** è un meccanismo di consistenza utilizzato dai file system per garantire che le modifiche ai metadati (e talvolta ai dati) siano applicate correttamente anche in caso di crash del sistema.

### Funzionamento
1. **Log delle transazioni**: Prima di modificare effettivamente la struttura del file system, il kernel registra l'intenzione della modifica in un log sequenziale (il *journal*).
2. **Commit**: Una volta registrata la transazione nel journal, essa viene considerata "committata".
3. **Applicazione**: Il kernel applica le modifiche ai blocchi reali del file system.
4. **Recupero**: In caso di crash, il sistema operativo controlla il journal all'avvio e riapplica le transazioni che erano state registrate ma non ancora completate.
