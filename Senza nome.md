# Ottima domanda! Ecco il collegamento

Vedi, la formula di Sherman-Morrison **non esce dal nulla**: è una **trasformazione algebrica furba** della soluzione base.

## Il passaggio chiave

Partiamo dalla soluzione LS base:
$$
\boldsymbol{a}_{\mathrm{LS}}(p) = (\boldsymbol{X}(p)\boldsymbol{X}^T(p))^{-1}\boldsymbol{X}(p)\boldsymbol{y}(p)
$$
Definisci:
$$
\boldsymbol{R}(p) = \boldsymbol{X}(p)\boldsymbol{X}^T(p)
$$
Allora:
$$
\boldsymbol{a}_{\mathrm{LS}}(p) = \boldsymbol{R}^{-1}(p)\boldsymbol{X}(p)\boldsymbol{y}(p)
$$
## Quando arriva un nuovo dato

Al passo $p+1$ aggiungi una nuova colonna a $\boldsymbol{X}$:
$$
\boldsymbol{X}(p+1) = [\boldsymbol{X}(p) \mid \boldsymbol{x}^n(p+1)]
$$
Allora:
$$
\boldsymbol{R}(p+1) = \boldsymbol{X}(p+1)\boldsymbol{X}^T(p+1) = \boldsymbol{X}(p)\boldsymbol{X}^T(p) + \boldsymbol{x}^n(p+1)\boldsymbol{x}^{nT}(p+1)
$$
$$
\boldsymbol{R}(p+1) = \boldsymbol{R}(p) + \boldsymbol{x}^n(p+1)\boldsymbol{x}^{nT}(p+1)
$$
**Questa è esattamente la forma** $\boldsymbol{R} + \boldsymbol{u}\boldsymbol{v}^T$ **del lemma di Sherman-Morrison!**

Con $\boldsymbol{u} = \boldsymbol{x}^n(p+1)$ e $\boldsymbol{v} = \boldsymbol{x}^n(p+1)$.

## Applicazione diretta del lemma

Il lemma di Sherman-Morrison dice:
$$
(\boldsymbol{R} + \boldsymbol{u}\boldsymbol{v}^T)^{-1} = \boldsymbol{R}^{-1} - \frac{\boldsymbol{R}^{-1}\boldsymbol{u}\boldsymbol{v}^T\boldsymbol{R}^{-1}}{1+\boldsymbol{v}^T\boldsymbol{R}^{-1}\boldsymbol{u}}
$$
Sostituisci:
$$
\boldsymbol{R}^{-1}(p+1) = \boldsymbol{R}^{-1}(p) - \frac{\boldsymbol{R}^{-1}(p)\boldsymbol{x}^n(p+1)\boldsymbol{x}^{nT}(p+1)\boldsymbol{R}^{-1}(p)}{1+\boldsymbol{x}^{nT}(p+1)\boldsymbol{R}^{-1}(p)\boldsymbol{x}^n(p+1)}
$$
## Aggiornamento di $\boldsymbol{a}$

Hai anche:
$$
\boldsymbol{X}(p+1)\boldsymbol{y}(p+1) = \boldsymbol{X}(p)\boldsymbol{y}(p) + \boldsymbol{x}^n(p+1)\theta(p+1)
$$
Quindi:
$$
\boldsymbol{a}(p+1) = \boldsymbol{R}^{-1}(p+1)[\boldsymbol{X}(p)\boldsymbol{y}(p) + \boldsymbol{x}^n(p+1)\theta(p+1)]
$$
Sostituendo la formula di Sherman-Morrison per $\boldsymbol{R}^{-1}(p+1)$ e semplificando, ottieni la formula complessa del documento.

---

## Riassunto della relazione

| Step | Formula |
$$
|------|---------|
$$
| **Base (todo a una volta)** | $\boldsymbol{a} = (\boldsymbol{X}\boldsymbol{X}^T)^{-1}\boldsymbol{X}\boldsymbol{y}$ |
| **Ricorsiva (con Sherman-Morrison)** | $\boldsymbol{a}(p+1) = \boldsymbol{R}^{-1}(p+1)[\boldsymbol{X}(p)\boldsymbol{y}(p) + \boldsymbol{x}^n(p+1)\theta(p+1)]$ |
| **Dove** | $\boldsymbol{R}^{-1}(p+1)$ si aggiorna tramite Sherman-Morrison invece di ricalcolare da zero |

**Non è magia**: è solo algebra che evita l'inversione completa, sfruttando il fatto che i dati arrivano **uno per volta** (rank-1 update).

Chiaro? 🎯