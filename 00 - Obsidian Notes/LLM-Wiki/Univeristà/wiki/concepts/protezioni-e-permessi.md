---
type: concept
title: Protezioni e Permessi
tags: [security, unix, file-system]
related: [identificazione-utenti-e-gruppi]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# Protezioni e Permessi

Il sistema operativo gestisce l'accesso alle risorse attraverso un modello di protezione basato su tre classi di utenti e tre tipi di operazioni.

## Classi di Utenti
1.  **Owner (Proprietario)**: L'utente che ha creato il file.
2.  **Group (Gruppo)**: Un insieme di utenti a cui il file è associato.
3.  **Public (Altro)**: Tutti gli altri utenti del sistema.

## Tipi di Accesso
- **Read (R)**: Permesso di lettura.
- **Write (W)**: Permesso di scrittura.
- **Execute (X)**: Permesso di esecuzione.
- **Append/Delete/List**: Operazioni aggiuntive spesso gestite a livello di directory o attributi specifici.

## Gestione
I permessi iniziali sono assegnati al momento della creazione. L'amministratore o il proprietario possono modificare tali attributi tramite comandi come `chmod` (cambia permessi), `chown` (cambia proprietario) e `chgrp` (cambia gruppo).