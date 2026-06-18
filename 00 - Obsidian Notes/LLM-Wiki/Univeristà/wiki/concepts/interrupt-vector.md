---
type: concept
title: Interrupt Vector
tags: [hardware, interruzioni]
related: [interrupt-service-routine, interrupt-request-line]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione1-AA25-26.txt"]
---
# Interrupt Vector

L'**interrupt vector** è una tabella di indirizzi utilizzata dalla CPU per gestire le interruzioni. Quando un dispositivo invia un codice di interruzione, la CPU usa tale codice come indice nel vettore per trovare l'indirizzo della relativa routine di servizio (ISR).