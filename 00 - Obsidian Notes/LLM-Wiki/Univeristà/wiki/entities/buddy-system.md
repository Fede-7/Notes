---
type: entity
title: Buddy System
tags: [kernel, allocazione-memoria]
related: [frammentazione-interna]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt"]
---
# Buddy System

Il **Buddy System** è un algoritmo di allocazione della memoria kernel che divide i blocchi di memoria in potenze di 2. Se un blocco di dimensione richiesta non è disponibile, un blocco più grande viene diviso in due "buddies". Questo sistema aiuta a gestire la memoria fisica contigua ma soffre di [[frammentazione-interna]].