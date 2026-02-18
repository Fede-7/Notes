# ESAME DI FISICA GENERALE I - 16/01/2026

---

## PROBLEMA 1: TERMODINAMICA

### Testo
Una mole di gas perfetto monoatomico a pressione $P_A = 1.2 \cdot 10^4 \text{ Pa}$ e volume $V_A = 0.1 \text{ m}^3$ compie un ciclo termodinamico composto dalle trasformazioni:
* **AB**: espansione isoterma fino a un volume $V_B = 8 V_A$.
* **BC**: decompressione isocora.
* **CA**: compressione adiabatica fino alle condizioni iniziali.

**a)** Disegnare il ciclo nel piano P-V e calcolare la temperatura dei punti A, B e C.
**b)** Calcolare calore e lavoro scambiati dal gas e la variazione di energia interna nelle tre trasformazioni e nel ciclo.

*(Dati: $\gamma = 5/3$, $c_v = 3/2 R$, $R = 8.314 \text{ J}/(\text{mol K})$)*

### Risoluzione

**Dati:**
$n = 1 \text{ mol}$
$P_A = 1.2 \cdot 10^4 \text{ Pa}$
$V_A = 0.1 \text{ m}^3$
$V_B = 0.8 \text{ m}^3$
$V_C = 0.8 \text{ m}^3$

**a) Temperature**
$$T_A = \frac{P_A V_A}{n R} = \frac{1200}{8.314} \approx 144.33 \text{ K}$$
$$T_B = T_A = 144.33 \text{ K}$$
$$T_C = T_A \left( \frac{V_A}{V_C} \right)^{\gamma - 1} = 144.33 \cdot \left( \frac{1}{8} \right)^{2/3} = \frac{144.33}{4} \approx 36.08 \text{ K}$$

**b) Calore (Q), Lavoro (W), Energia Interna ($\Delta U$)**

* **Trasformazione AB (Isoterma):**
    $$\Delta U_{AB} = 0 \text{ J}$$
    $$Q_{AB} = W_{AB} = n R T_A \ln\left(\frac{V_B}{V_A}\right) = 1200 \cdot \ln(8) \approx 2495.2 \text{ J}$$

* **Trasformazione BC (Isocora):**
    $$W_{BC} = 0 \text{ J}$$
    $$Q_{BC} = \Delta U_{BC} = n c_v (T_C - T_B) = 1 \cdot 1.5 \cdot 8.314 \cdot (36.08 - 144.33) \approx -1349.9 \text{ J}$$

* **Trasformazione CA (Adiabatica):**
    $$Q_{CA} = 0 \text{ J}$$
    $$W_{CA} = -\Delta U_{CA} = - n c_v (T_A - T_C) = - (12.471 \cdot 108.25) \approx -1349.9 \text{ J}$$
    $$\Delta U_{CA} \approx 1349.9 \text{ J}$$

* **Totale Ciclo:**
    $$\Delta U_{ciclo} = 0 \text{ J}$$
    $$W_{ciclo} = Q_{ciclo} = 2495.2 - 1349.9 \approx 1145.3 \text{ J}$$

---

## PROBLEMA 2: DINAMICA (PIANI INCLINATI E CARRUCOLA)

### Testo
Due blocchi rigidi A ($m_A = 4.0 \text{ kg}$) e B ($m_B = 6.0 \text{ kg}$) sono collegati da un filo inestensibile attraverso una carrucola (cilindro pieno, $M = 1.5 \text{ kg}$, $R = 0.2 \text{ m}$, $I = \frac{1}{2}MR^2$).
* Blocco A su piano inclinato $\theta_1 = 30^\circ$.
* Blocco B su piano inclinato $\theta_2 = 45^\circ$.
* No attriti.

**a)** Scrivere le equazioni del moto.
**b)** Calcolare l'accelerazione del sistema.
**c)** Determinare la tensione nei due tratti del filo.

### Risoluzione

**a) Equazioni del moto**
1.  $T_1 - m_A g \sin(30^\circ) = m_A a$
2.  $m_B g \sin(45^\circ) - T_2 = m_B a$
3.  $(T_2 - T_1) R = I \frac{a}{R} \Rightarrow T_2 - T_1 = \frac{1}{2} M a$

**b) Accelerazione ($a$)**
$$a = g \frac{m_B \sin(45^\circ) - m_A \sin(30^\circ)}{m_A + m_B + \frac{1}{2}M}$$
$$a = 9.81 \cdot \frac{6(0.707) - 4(0.5)}{4 + 6 + 0.75} = 9.81 \cdot \frac{2.242}{10.75} \approx 2.05 \text{ m/s}^2$$

**c) Tensioni ($T_1, T_2$)**
$$T_1 = m_A (a + g \sin 30^\circ) = 4(2.05 + 4.905) \approx 27.82 \text{ N}$$
$$T_2 = m_B (g \sin 45^\circ - a) = 6(6.936 - 2.05) \approx 29.32 \text{ N}$$

---

## PROBLEMA 3: URTO E MOLLA

### Testo
Blocco $M = 300 \text{ g}$ collegato a molla ($K = 120 \text{ N/m}$) su piano con attrito $\mu_d = 0.3$. Colpito in modo anelastico da proiettile $m = 100 \text{ g}$ con $v_0 = 50 \text{ m/s}$.
1.  Velocità subito dopo l'urto.
2.  Massima compressione della molla.
3.  Lavoro forza attrito.

### Risoluzione

**1. Velocità sistema ($V_f$)**
$$m v_0 = (M + m) V_f$$
$$V_f = \frac{0.1 \cdot 50}{0.4} = 12.5 \text{ m/s}$$

**2. Compressione massima ($x$)**
$$\frac{1}{2}(M+m)V_f^2 - \mu_d (M+m) g x = \frac{1}{2} K x^2$$
$$0.5(0.4)(12.5)^2 - 0.3(0.4)(9.81)x = 60x^2$$
$$31.25 - 1.177x - 60x^2 = 0 \Rightarrow 60x^2 + 1.177x - 31.25 = 0$$
$$x = \frac{-1.177 + \sqrt{1.385 + 7500}}{120} \approx 0.712 \text{ m}$$

**3. Lavoro Attrito ($W_{attr}$) of**
$$W_{attr} = - \mu_d (M+m) g x$$
$$W_{attr} = - 0.3 \cdot 0.4 \cdot 9.81 \cdot 0.712 \approx -0.838 \text{ J}$$

---

## PROBLEMA 4: FLUIDI

### Testo
Cubo di ferro ($\rho_{Fe} = 7.87 \text{ g/cm}^3$) volume $V = 0.005 \cdot 10^{-2} \text{ dm}^3$ sospeso a molla ($K = 58 \text{ N/m}$) immerso in acqua ($\rho_{H2O} = 997 \text{ kg/m}^3$). Calcolare l'allungamento.

### Risoluzione

**Conversione Volume e Densità:**
$$V = 5 \cdot 10^{-5} \text{ dm}^3 = 5 \cdot 10^{-8} \text{ m}^3$$
$$\rho_{Fe} = 7870 \text{ kg/m}^3$$

**Allungamento ($\Delta x$)**
$$K \Delta x = F_p - F_A = V g (\rho_{Fe} - \rho_{H2O})$$
$$\Delta x = \frac{5 \cdot 10^{-8} \cdot 9.81 \cdot (7870 - 997)}{58}$$
$$\Delta x \approx 5.81 \cdot 10^{-5} \text{ m} \quad (0.058 \text{ mm})$$

---

## PROBLEMA 5: CORPO RIGIDO E FORZE APPARENTI

### Testo
Disco ($R = 30 \text{ cm}$, $m = 5 \text{ kg}$) ruota a 30 giri/s.
**a)** Quantità di moto, momento angolare, energia cinetica.
**b)** Forza centrifuga su insetto ($M = 30 \text{ g}$) a $D = 1 \text{ dm}$ dall'asse.
**c)** Forza di Coriolis se l'insetto si sposta lungo il raggio.
**d)** Piani e direzioni dei vettori.

### Risoluzione

**Dati:**
$\omega = 30 \cdot 2\pi \approx 188.5 \text{ rad/s}$
$I = 0.5 \cdot 5 \cdot 0.3^2 = 0.225 \text{ kg m}^2$

**a) Grandezze**
$$p = 0 \text{ kg m/s}$$
$$L = I \omega = 0.225 \cdot 188.5 \approx 42.41 \text{ kg m}^2/\text{s}$$
$$K = \frac{1}{2} I \omega^2 \approx 3996 \text{ J}$$

**b) Forza Centrifuga ($F_{cf}$)**
$$F_{cf} = M_{ins} \omega^2 D = 0.03 \cdot (188.5)^2 \cdot 0.1 \approx 106.6 \text{ N}$$

**c) Forza di Coriolis ($F_{cor}$)**
$$F_{cor} = 2 M_{ins} \omega v \approx 11.31 \cdot v \text{ N}$$

**d) Vettori**
* **Coriolis:** Piano del disco, direzione tangenziale.
* **Centrifuga:** Piano del disco, direzione radiale (verso esterno).