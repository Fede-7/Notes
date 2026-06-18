---
type: entity
title: TEB (Thread Environment Block)
tags: [windows, thread, user-space]
related: [ethread, kthread]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# TEB (Thread Environment Block)

Il **Thread Environment Block (TEB)** è una struttura dati nello spazio utente di Windows che contiene informazioni specifiche per il thread corrente, come l'ID del thread, lo stack e altre variabili di ambiente. È accessibile dal codice dell'applicazione per ottenere informazioni sul contesto di esecuzione del thread.