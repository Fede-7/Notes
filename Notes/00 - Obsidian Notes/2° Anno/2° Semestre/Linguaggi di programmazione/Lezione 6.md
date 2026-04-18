---
date: 2026-03-26
corso: Linguaggi di Programmazione
docente: N/D
lezione: Stack di attivazione — esercizi con tutte le modalità di passaggio parametri
tags: [LP, passaggio-parametri, stack-attivazione, in-out, per-copia, per-riferimento]
---

# LP — Lezione 6: Esercizi sullo Stack di Attivazione con Tutte le Modalità di Passaggio

**Corso:** Linguaggi di Programmazione

---

## Argomenti trattati

- Esercizio 2 completo: analisi con 4 modalità di passaggio parametri
  - In per riferimento (errore)
  - Out per riferimento (errore)
  - In-out per riferimento
  - In-out per copia
- Confronto dei risultati tra le diverse modalità
- Metodologia generale per costruire lo stack di attivazione

---

## 1. Il programma dell'esercizio

Il programma da analizzare è un Pascal-like con due procedure annidate. Le procedure `P1` e `P2` hanno due parametri formali `A` e `B`, la cui modalità di passaggio varia a seconda del caso in esame.

```pascal
program Esercizio2;
  var a, b, c : integer;

  procedure P2(mode A, B : integer);
  begin
    A := A - B;
    if A = c then
      P1(B, A)
    else
      P1(A, B)
  end;

  procedure P1(mode A, B : integer);
  begin
    A := A * B;
    if c div B = A then
      { ramo then: non raggiunto negli esempi }
    else
      A := 100
  end;

begin
  a := 1; b := 5; c := 10;
  P2(c, b);
  write(a, b, c)
end.
```

*(Nota: `mode` è il segnaposto per la modalità di passaggio che varia tra i casi.)*

---

## 2. Metodologia: checklist prima di costruire lo stack

> [!tip] Procedura obbligatoria
> **Prima** di disegnare qualsiasi record di attivazione, rispondere a queste domande:
> 1. La modalità causa errori (a compile-time o runtime)?
>    - **In**: il parametro è mai a sinistra di un assegnamento? → errore a compile-time.
>    - **Out**: il parametro è mai letto prima di essere scritto? → errore a runtime.
>    - **In-out**: nessun errore a priori.
> 2. Solo se non ci sono errori: costruire lo stack.
> 3. Seguire rigorosamente lo **scoping statico** (puntatori all'ambiente non locale basati su dove la procedura è definita).

---

## 3. Caso 1: In per riferimento → **ERRORE**

Con modalità `in per riferimento`, il parametro è un alias della variabile del chiamante, ma può essere solo letto (non scritto).

Già la prima istruzione di P2 è `A := A - B`, che scrive nel parametro `A`. Questo viola la modalità `in`. **Errore a compile-time**: inutile costruire lo stack.

---

## 4. Caso 2: Out per riferimento → **ERRORE**

Con modalità `out`, il parametro non è inizializzato all'ingresso nella procedura (il suo valore è "spazzatura"). Leggerlo prima di scriverlo è un errore.

La prima istruzione di P2 è `A := A - B`, che legge sia `A` che `B` prima di averli inizializzati. **Errore**: almeno due parametri vengono letti prima di essere scritti.

> [!warning] Riconoscere gli errori out
> Per la modalità `out`, non è sufficiente che il parametro venga inizializzato durante la procedura: deve essere inizializzato **prima di ogni lettura**. Se la prima operazione è una lettura, è sempre un errore.

---

## 5. Caso 3: In-out per riferimento

### Costruzione dello stack

Chiamata iniziale: `P2(c, b)` con `c=10`, `b=5`.

**Record di Esercizio2**:
```
Esercizio2:
  ENV non locale: (nessuno — blocco più esterno)
  a = 1
  b = 5
  c = 10
```

**Record di P2** (parametri per riferimento → alias):
```
P2:
  ENV non locale → Esercizio2
  chiamata: P2(c, b)
  A alias→ c (di Esercizio2)
  B alias→ b (di Esercizio2)
```

> [!info] Notazione per il passaggio per riferimento
> Non riscrivere il valore del parametro nel record di P2. Annotate esplicitamente l'alias, ad es. `A ≡ c (Esercizio2)`. Se li duplicate con il valore, dimenticate di aggiornare entrambe le copie quando il valore cambia.

### Esecuzione di P2

- `A := A - B` → `c = 10 - 5 = 5`. Il valore di `c` in Esercizio2 diventa 5.
- `if A = c` → `A` è `c`, e `c` è la stessa locazione. Quindi `A = c` è sempre vero (aliasing!). Ramo `then`.
- `P1(B, A)` → `P1(b, c)` dove `b=5`, `c=5`.

**Record di P1**:
```
P1:
  ENV non locale → Esercizio2
  chiamata: P1(B_P2, A_P2) = P1(b, c)
  A alias→ b (di Esercizio2)
  B alias→ c (di Esercizio2)  ← aliasing: B_P1 e c sono la stessa locazione!
```

### Esecuzione di P1

- `A := A * B` → `A` è `b` (=5), `B` è `c` (=5). Quindi `b = 5 * 5 = 25`.
- `if c div B = A` → `c` e `B` sono la stessa variabile! `c div c = 1`. `A` è `b = 25`. `1 ≠ 25` → ramo `else`.
- `A := 100` → `b = 100`.

**Uscita da P1** (nessuna copia — passaggio per riferimento).

**Uscita da P2** (nessuna copia).

**Stato finale**: `a=1`, `b=100`, `c=5`.

**Output: `1 100 5`**

---

## 6. Caso 4: In-out per copia

### Costruzione dello stack

Chiamata iniziale: `P2(c, b)` con `c=10`, `b=5`.

**Record di Esercizio2**:
```
Esercizio2: a=1, b=5, c=10
```

**Record di P2** (parametri per copia → variabili locali nel record di P2):
```
P2:
  ENV non locale → Esercizio2
  A = 10  [copia di c; da copiare su c all'uscita]
  B = 5   [copia di b; da copiare su b all'uscita]
```

### Esecuzione di P2

- `A := A - B` → `A_P2 = 10 - 5 = 5`.
- `if A = c` → `A` è locale (`= 5`); `c` si trova seguendo ENV non locale → `c = 10`. `5 ≠ 10` → ramo `else`.
- `P1(A, B)` → passa `A_P2=5`, `B_P2=5`.

**Record di P1**:
```
P1:
  ENV non locale → Esercizio2
  A = 5   [copia di A_P2; da copiare su A_P2 all'uscita]
  B = 5   [copia di B_P2; da copiare su B_P2 all'uscita]
```

### Esecuzione di P1

- `A := A * B` → `A_P1 = 5 * 5 = 25`.
- `if c div B = A` → `c` (da ENV non locale) = 10; `B_P1` = 5; `10 div 5 = 2`. `A_P1 = 25`. `2 ≠ 25` → ramo `else`.
- `A := 100` → `A_P1 = 100`.

**Uscita da P1** — copia-out: `A_P2 = 100`, `B_P2 = 5` (invariato).

**Uscita da P2** — copia-out: `c = 100`, `b = 5` (invariato).

**Output: `1 5 100`**

---

## 7. Riepilogo: confronto tra le 4 modalità

| Modalità | Errore? | Output |
|---|---|---|
| In per riferimento | ✗ errore compile-time (`A :=` è scrittura) | — |
| Out per riferimento | ✗ errore runtime (lettura prima di scrittura) | — |
| In-out per riferimento | ✓ | `1 100 5` |
| In-out per copia | ✓ | `1 5 100` |

> [!example] Perché i risultati differiscono tra riferimento e copia
> Nel passaggio per riferimento, la modifica di `c` dentro P2 (da 10 a 5) è immediatamente visibile nel test `if A = c` (aliasing → sempre vero), portando all'esecuzione del ramo `then` e a una catena di alias diversa. Nel passaggio per copia, `c` rimane 10 durante l'esecuzione di P2, il test è `5 ≠ 10`, si prende il ramo `else`, e la modifica si propaga solo all'uscita.

---

## 8. Note metodologiche per l'esame

> [!tip] Consigli pratici
> 1. **Non duplicare** le variabili nel record per il passaggio per riferimento: annotate solo l'alias. Duplicare crea errori di disallineamento.
> 2. **Annotare le copie-out** subito alla costruzione del record per in-out per copia: scrivete "da copiare su X all'uscita" accanto a ogni parametro.
> 3. **Seguire sempre il puntatore ENV non locale** per trovare le variabili non locali (scoping statico): non andate nel record immediatamente precedente nello stack (quello sarebbe lo scoping dinamico).
> 4. L'ordine della copia-out (da sinistra a destra o destra a sinistra) può influenzare il risultato in presenza di aliasing tra parametri attuali. Il linguaggio non lo specifica: è una fonte di comportamento indefinito.

---

> [!abstract] Punti chiave della lezione
> - Modalità `in` e `out` devono essere controllate per errori prima di costruire lo stack.
> - Il passaggio per riferimento crea alias: modifiche a un parametro si riflettono immediatamente sulla variabile originale, incluse eventuali successive letture dello stesso valore tramite altri nomi.
> - Il passaggio per copia isola le modifiche fino all'uscita dalla procedura (copia-out).
> - Stesse procedure, stessi valori iniziali, modalità diverse → output diversi: conoscere la modalità di passaggio è fondamentale per capire il comportamento del programma.

## Prossimi argomenti

- [ ] Esercizi inversi: ricostruire la struttura del programma dallo stack
- [ ] Esercizio: scrivere un programma che distingue sperimentalmente passaggio per copia da passaggio per riferimento
- [ ] Linguaggio ML: introduzione ai linguaggi funzionali

#LP #passaggio-parametri #stack-attivazione #in-out #per-copia #per-riferimento #aliasing
