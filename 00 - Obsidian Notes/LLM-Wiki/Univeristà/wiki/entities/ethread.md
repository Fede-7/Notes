---
type: entity
title: ETHREAD
tags: [windows, kernel, thread]
related: [kthread, teb]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# ETHREAD

In Windows, **ETHREAD** è il blocco di dati del thread nello spazio utente (user space). Contiene il contesto del thread dal punto di vista dell'applicazione, inclusi i dati necessari per l'esecuzione del thread nel contesto del processo.