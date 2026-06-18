---
type: concept
title: Strutture delle Directory
tags: [file-system, data-structures]
related: [file-control-block-fcb]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# Strutture delle Directory

Le directory fungono da tabelle dei simboli che mappano i nomi dei file (mnemonici per l'utente) ai loro [[file-control-block-fcb]] (identificatori per il sistema). L'organizzazione logica delle directory mira a bilanciare efficienza, naming e grouping.

## Tipologie di Struttura
- **Single-Level Directory**: Una singola directory per tutti gli utenti. Soffre di problemi di collisione dei nomi e mancanza di raggruppamento.
- **Two-Level Directory**: Directory separate per ogni utente. Risolve il problema dei nomi tra utenti diversi ma non permette il raggruppamento logico.
- **Tree-Structured Directory**: Struttura gerarchica ad albero. Supporta il raggruppamento logico e la ricerca efficiente tramite percorsi (*pathnames*).
- **Acyclic-Graph Directory**: Permette la condivisione di file e sottodirectory tramite link. Introduce il problema dei *dangling pointers* (link rotti) e richiede contatori di riferimento per la cancellazione corretta.
- **General Graph Directory**: Permette cicli. Presenta problemi di ricerca infinita e richiede algoritmi complessi come la *Garbage Collection* o la *Cycle Detection* per la gestione dei file.

## Implementazione
Le directory possono essere implementate come:
- **Liste Lineari**: Semplici ma inefficienti (ricerca $O(n)$).
- **Hash Tables**: Abbassano i tempi di ricerca ma richiedono la gestione delle collisioni (es. *chained-overflow*).