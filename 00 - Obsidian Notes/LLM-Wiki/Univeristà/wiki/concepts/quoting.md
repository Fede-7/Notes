---
type: concept
title: Quoting
tags: [bash, shell, espansione]
related: [metacaratteri-e-wildcards]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Quoting

Il meccanismo del **quoting** viene utilizzato per inibire l'effetto speciale dei metacaratteri, trattandoli come caratteri ordinari.

## Meccanismi di Quoting
1.  **Escape (`\`)**: Inibisce l'effetto del carattere immediatamente successivo.
    - Esempio: `ls file\*` viene interpretato come il file con nome letterale `file*`.
2.  **Singoli Apici (`'`)**: Tutti i metacaratteri all'interno della stringa perdono il loro significato speciale.
3.  **Doppi Apici (`"`)**: I metacaratteri per l'abbreviazione del pathname perdono il loro significato speciale, ma altri metacaratteri della shell (come le variabili) possono ancora essere espansi.

**Nota**: Il quoting funziona in modo differente durante le assegnazioni di variabili rispetto all'esecuzione dei comandi.