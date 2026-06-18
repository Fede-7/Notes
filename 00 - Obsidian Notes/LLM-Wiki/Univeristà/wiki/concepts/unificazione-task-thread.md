---
type: concept
title: Unificazione Task-Thread
tags: [linux, kernel, architettura]
related: [clone, task_struct]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Unificazione Task-Thread

L'**unificazione task-thread** è un modello architetturale adottato dal kernel Linux in cui i processi e i thread non sono trattati come entità distinte a livello di schedulazione. Entrambi sono considerati "tasks". Un thread è semplicemente un task che condivide lo spazio di indirizzamento e altre risorse con altri task (i suoi "parent" o "siblings") tramite la chiamata di sistema `clone()`. Questo semplifica la gestione del kernel, che deve gestire un unico tipo di struttura dati (`task_struct`) per tutte le unità di esecuzione.