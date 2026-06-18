---
type: concept
title: Politica vs Meccanismo
tags: [design, kernel, architettura]
related: [strutture-del-kernel]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
---
# Politica vs Meccanismo

Nel design dei sistemi operativi, è fondamentale distinguere tra la **politica** e il **meccanismo**. Questa separazione è un principio di progettazione che mira a massimizzare la flessibilità e la modularità del sistema.

## Definizioni
- **Politica (Cosa fare)**: Definisce le decisioni di alto livello, le regole e le scelte strategiche. Ad esempio, la lunghezza del timer per la protezione della CPU è una decisione politica.
- **Meccanismo (Come farlo)**: Fornisce le funzioni tecniche e le strutture necessarie per implementare le decisioni politiche. Il timer stesso è il meccanismo.

## Vantaggi della Separazione
1. **Flessibilità**: Le decisioni politiche possono essere modificate o aggiornate senza dover riscrivere il codice del meccanismo sottostante.
2. **Riutilizzabilità**: Un singolo meccanismo può supportare molteplici politiche diverse semplicemente cambiando i parametri di configurazione.
3. **Modularità**: Favorisce architetture più pulite, come quelle dei microkernel, dove le politiche sono spesso spostate nello spazio utente.