---
type: concept
title: Accesso Sequenziale vs. Diretto
tags: [file-system, storage]
related: []
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# Accesso Sequenziale vs. Diretto

I sistemi operativi supportano diversi modelli di accesso ai dati a seconda del supporto fisico sottostante e delle necessità applicative.

## Accesso Sequenziale
Segue un ordine lineare, tipico dei supporti come i nastri magnetici. Le operazioni principali sono:
- *Read next*
- *Write next*
- *Reset* (ritorno all'inizio)

## Accesso Diretto (Relativo)
Tipico dei dischi rigidi, permette di saltare a posizioni specifiche. Il file è assunto come composto da record logici di lunghezza fissata. Le operazioni includono:
- *Read n* / *Write n*
- *Position to n* (spostamento a un blocco relativo)
- *Rewrite n*

## Simulazione
È possibile simulare l'accesso sequenziale su un dispositivo a accesso diretto mantenendo un puntatore interno (*current position*) che viene incrementato ad ogni operazione di lettura o scrittura.