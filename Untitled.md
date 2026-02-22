# Anello Prodotto $R \times S$ — Forma Compatta

> [!note] **Definizione**
> L'anello prodotto $R \times S = \{(r,s) \mid r \in R, s \in S\}$ con operazioni componente per componente:
> - $(r_1,s_1) + (r_2,s_2) = (r_1+r_2, s_1+s_2)$
> - $(r_1,s_1) \cdot (r_2,s_2) = (r_1 \cdot r_2, s_1 \cdot s_2)$
> - Zero: $\mathbf{0} = (0_R, 0_S)$
> - Unità: $\mathbf{1} = (1_R, 1_S)$ (se $R,S$ unitari)

> [!note] **Proprietà Fondamentali**
> 
> | Proprietà | Risultato |
> |---|---|
> | **Commutatività** | $R \times S$ comm. ⟺ $R$ e $S$ comm. |
> | **Invertibili** | $(r,s) \in U(R \times S)$ ⟺ $r \in U(R)$ e $s \in U(S)$ |
> | **Cardinalità invertibili** | $\|U(\mathbb{Z}_m \times \mathbb{Z}_n)\| = \varphi(m) \cdot \varphi(n)$ |
> | **Divisori dello zero** | **Sempre presenti** (anche se $R,S$ domini): $(1_R,0_S) \cdot (0_R,1_S) = \mathbf{0}$ |
> | **Caratteristica** | $\mathrm{char}(R \times S) = \mathrm{mcm}(\mathrm{char}(R), \mathrm{char}(S))$ |
> | **Campo** | Se $F,K$ campi ⟹ $F \times K$ **NON è campo** (ha divisori dello zero) |

> [!note] **Teorema Cinese dei Resti (TCR)**
> $$\mathbb{Z}_{mn} \cong \mathbb{Z}_m \times \mathbb{Z}_n \quad \Longleftrightarrow \quad \mathrm{MCD}(m,n) = 1$$
> 
> **Isomorfismo:** $\phi([a]_{mn}) = ([a]_m, [a]_n)$
> 
> **Utilità:** Spezzare calcoli modulo $mn$ (grande) in calcoli modulo $m$ e $n$ (piccoli).
> 
> **Esempio:** $\mathbb{Z}_{15} \cong \mathbb{Z}_3 \times \mathbb{Z}_5$ (poiché $\gcd(3,5)=1$)

> [!note] **Riassunto Critico**
> - ✓ Operazioni componente per componente funzionano perfettamente
> - ✗ Divisori dello zero sempre presenti (perdita proprietà integralità)
> - ✗ Non è mai un campo anche se fattori sono campi
> - ✓ TCR consente di fattorizzare calcoli complessi quando fattori sono coprimi
> - ✓ Invertibili sono il prodotto cartesiano di invertibili