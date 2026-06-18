---
type: concept
title: Identificazione Utenti e Gruppi
tags: [security, unix]
related: [protezioni-e-permessi]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# Identificazione Utenti e Gruppi

Per gestire la sicurezza e le protezioni, il sistema operativo identifica gli utenti e i gruppi tramite identificatori numerici univoci.

- **User ID (UID)**: Ogni nome utente (*user name*) assegnato dall'amministratore corrisponde biunivocamente a un UID numerico.
- **Group ID (GID)**: Ogni gruppo è identificato da un nome di gruppo (massimo 8 caratteri) associato a un GID numerico.

Un utente può appartenere a uno o più gruppi. Questa struttura permette di assegnare permessi granulari: un file può essere accessibile a un utente specifico, a un intero gruppo di lavoro, o a chiunque nel sistema.