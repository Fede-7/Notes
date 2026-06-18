---
type: concept
title: Mapping degli Indirizzi
tags: [memoria-di-massa, hardware]
related: [lba, chs]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# Mapping degli Indirizzi

Il **mapping degli indirizzi** è l'astrazione utilizzata per tradurre le richieste di accesso ai dati da coordinate fisiche a coordinate logiche.

Nei sistemi di memoria di massa, questo processo trasforma le coordinate **CHS** (Cylinder, Head, Sector), che descrivono la posizione meccanica dei dati, in **LBA** (Logical Block Address), che presentano il disco come una serie lineare di blocchi. Questa astrazione è fondamentale per permettere ai file system di operare indipendentemente dalla geometria fisica del disco.