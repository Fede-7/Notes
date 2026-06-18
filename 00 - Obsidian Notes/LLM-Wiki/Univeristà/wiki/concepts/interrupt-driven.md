---
type: concept
title: Interrupt Driven
tags: [hardware, I/O]
related: [interrupt-request-line, interrupt-service-routine, polling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione1-AA25-26.txt"]
---
# Interrupt Driven

Un sistema moderno è definito **interrupt-driven**. Invece di interrogare continuamente i dispositivi (polling), la CPU esegue le proprie istruzioni finché un dispositivo non invia un segnale di interruzione per richiedere attenzione. Questo permette di sovrapporre le operazioni I/O e il processamento della CPU.