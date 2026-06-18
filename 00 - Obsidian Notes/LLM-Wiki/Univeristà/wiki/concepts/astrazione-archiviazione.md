---
type: concept
title: Astrazione dell'Archiviazione
tags: [file-system, storage]
related: [file-system, gerarchia-di-memorie]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# Astrazione dell'Archiviazione

Il Sistema Operativo fornisce una rappresentazione logica e uniforme dell'archiviazione delle informazioni, nascondendo le proprietà fisiche del supporto.

- **Unità Logica**: Il **file** è l'unità logica di archiviazione.
- **Gestione del File-System**:
    - Organizzazione gerarchica in directory multilivello.
    - Controllo degli accessi (chi può accedere a cosa).
    - Creazione e cancellazione di file e directory.
    - Primitive per la modifica.
    - Mapping dei file nella memoria secondaria.
    - Backup su memorie non volatili.