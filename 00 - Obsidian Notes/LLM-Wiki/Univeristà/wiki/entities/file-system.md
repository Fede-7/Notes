---
type: entity
title: File System
tags: [os, storage]
related: [inode, journaling, copy-on-write]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# File System

Il **File System** è il sistema responsabile dell'organizzazione, della gestione e dell'accesso ai dati memorizzati in memoria di massa (come i dischi rigidi). Esso fornisce un'astrazione logica dei dati, permettendo agli utenti e alle applicazioni di interagire con i file senza dover gestire direttamente i settori fisici del supporto di archiviazione.

### Funzioni Principali
- **Astrazione**: Rappresenta i dati come file e directory.
- **Gestione dello Spazio**: Traccia quali blocchi di memoria sono occupati e quali sono liberi.
- **Protezione**: Gestisce i permessi di accesso (chi può leggere, scrivere o eseguire).
- **Consistenza**: Garantisce che i dati rimangano integri anche in caso di interruzioni di alimentazione (tramite meccanismi come il [[journaling]]).
