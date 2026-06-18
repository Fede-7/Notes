---
type: concept
title: Sezione Critica
tags: ["sincronizzazione", "concorrenza", "thread"]
related: ["mutua-esclusione", "progresso", "bounded-waiting", "corsa-critica"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
# Sezione Critica

La [[sezione-critica]] è il segmento o la porzione di codice in cui un processo o un thread accede a risorse condivise (come variabili globali, file o strutture dati) o le modifica.

Per garantire la correttezza del sistema, l'esecuzione di queste sezioni deve essere esclusiva: solo un thread alla volta può trovarsi all'interno della propria sezione critica.

### Requisiti Fondamentali
Per garantire la correttezza del sistema, l'esecuzione delle sezioni critiche deve rispettare tre requisiti fondamentali:

- **Mutua esclusione**: Solo un processo o thread può trovarsi nella sezione critica contemporaneamente.
- **Progresso**: Se nessuna sezione critica è occupata e ci sono processi pronti a entrarvi, almeno uno di essi deve poterlo fare.
- **Bounded waiting**: Ogni processo che desidera entrare nella sezione critica deve poterlo fare entro un tempo limitato, evitando che un processo debba attendere indefinitamente.