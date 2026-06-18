---
type: source
title: "Lezione FS1 - Sistemi Operativi I"
tags: [SO1, file-system, lezione]
related: [strutture-delle-directory, file-locking, open-file-table, file-control-block-fcb]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
authors: []
year: 2026
url: ""
venue: ""
---
# Lezione FS1 - Sistemi Operativi I

Questa lezione fornisce le basi teoriche e pratiche sulla gestione dei **File System** in ambito Unix/Linux. I temi principali trattati includono:

- **Concetti Fondamentali**: Definizione del file come unità logica di immagazzinamento, attributi (nome, identificatore, tipo, posizione, dimensione, protezione, timestamp) e operazioni standard (*Create, Open, Close, Read, Write, Seek, Delete, Truncate*).
- **Gestione dei File Aperti**: Analisi della struttura delle tabelle dei descrittori di file, distinguendo tra la tabella per-processo (contenente i [[file-descriptor]]) e la tabella di sistema (contenente i riferimenti ai [[file-control-block-fcb]]).
- **Strutture delle Directory**: Evoluzione delle organizzazioni gerarchiche per risolvere problemi di naming e grouping, passando da strutture a singolo livello a strutture ad albero, grafi aciclici e grafi generali.
- **Link e Accesso**: Differenze tra link simbolici e link hard, e modelli di accesso sequenziale (modello nastro) vs accesso diretto (modello disco).
- **Sincronizzazione e Protezione**: Meccanismi di [[file-locking]] (Shared vs Exclusive) e modelli di protezione basati su classi di utenti (Proprietario, Gruppo, Pubblico).
- **File Speciali**: Il principio "everything is a file" e il trattamento uniforme di dispositivi (carattere, blocchi, socket, pipe).