---
type: concept
title: Segmentazione
tags: [memoria, architettura]
related: [paginazione, indirizzi-logici-vs-fisici]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt"]
---
# Segmentazione

La **segmentazione** è un modello di gestione della memoria basato su unità logiche visibili all'utente, come procedure, stack, funzioni o oggetti. 

A differenza della paginazione (che è una divisione fisica arbitraria), la segmentazione riflette la struttura logica del programma. In molti sistemi moderni, la segmentazione viene combinata con la paginazione (**segmentazione paginata**) per ottenere i vantaggi di entrambi i modelli: la visione logica della segmentazione e l'efficienza della paginazione.