---
type: entity
title: Slab Allocator
tags: [kernel, allocazione-memoria]
related: [slob, slab, slub, frammentazione-interna]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt"]
---
# Slab Allocator

Lo **Slab Allocator** è una tecnica di gestione della memoria kernel che pre-alloca oggetti di tipo specifico (come strutture dati del kernel) per eliminare la frammentazione interna causata dal Buddy System. Le varianti includono **SLOB** (per sistemi embedded), **SLAB** (standard) e **SLUB** (ottimizzato per multicore).