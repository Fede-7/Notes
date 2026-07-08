import os
import shutil

# Mappatura esatta "Vecchio Titolo": "Nuovo Titolo" aggiornato fino a un max di 6 livelli
MAPPING = {
    "# Fondamenti Probabilità": "# 1. Fondamenti di Probabilità",
    "## Definizioni": "## Definizioni e Nomenclatura",
    "## Qualche richiamo di insiemistica": "### Insiemistica di base",
    "## Nomenclatura probabilistica": "## Definizioni e Nomenclatura",
    "## Spazi finiti con eventi elementari equivalenti": "### Spazi finiti ed eventi elementari",
    "## Prodotti cartesiani": "### Prodotti cartesiani e k-ple ordinate",
    "## k-ple ordinate senza ripetizione": "### Prodotti cartesiani e k-ple ordinate",
    "## Permutazioni": "### Permutazioni e Combinazioni",
    "## Combinazioni $( \\overline { { G } } _ { m } ) _ { s } ^ { s }$": "### Permutazioni e Combinazioni",
    "## Insieme delle parti di un insieme finito": "### Insieme delle parti",
    "# Discreto": "# 2. Variabili Aleatorie Discrete",
    "## Dalla frequenza alla probabilità": "## Frequenza e Probabilità",
    "## Frequenza di occorrenza e probabilità su Spazi finiti": "### Frequenza di occorrenza e Leggi probabilistiche",
    "## Alcune proprietà della frequenza di occorrenza e della probabilità": "### Proprietà: Complementari, Sub-additività, Sottrazione",
    "### a Eventi complementari": "### Proprietà: Complementari, Sub-additività, Sottrazione",
    "### b Sub-additività": "### Proprietà: Complementari, Sub-additività, Sottrazione",
    "### c Sottrazione tra insiemi": "### Proprietà: Complementari, Sub-additività, Sottrazione",
    "### d Evento certo ed evento impossibile": "### Evento certo e impossibile",
    "## Frequenze e probabilità condizionate": "### Frequenze e probabilità condizionate",
    "## Legge della probabilità totale": "### Legge della probabilità totale",
    "## Eventi Indipendenti": "### Eventi indipendenti",
    "## L’approccio assiomatico alla teoria della probabilità": "### Approccio assiomatico",
    "## Proprietà delle Algebre": "## Teoria dell'Assiomatica",
    "## Spazi di probabilità": "### Algebre e Spazi di probabilità",
    '## Proprietà delle leggi di probabilità ("""dimosrazioni""")': "### Proprietà operative di Media e Varianza",
    "### Eventi complementari": "### Proprietà: Complementari, Sub-additività, Sottrazione",
    "### Sottrazione tra insiemi": "### Proprietà: Complementari, Sub-additività, Sottrazione",
    "### Unione di eventi non incompatibili": "### Proprietà: Complementari, Sub-additività, Sottrazione",
    "## Variabile Aleatoria": "### Variabile Aleatoria (Definizione)",
    "## Strumenti per descrivere la distribuzione di X": "### PMF (Probability Mass Function)",
    "## La media campionaria": "### Valore atteso (Media statistica) e Media campionaria",
    "## La media statistica / Valore atteso": "### Valore atteso (Media statistica) e Media campionaria",
    "## La variabile Uniforme": "### Variabile Uniforme",
    "## La variabile Poissoniana": "### Variabile Poissoniana",
    "## PMF condizionali": "### Trasformazioni e PMF condizionali",
    "## Regola della probabilità totale per le pmf": "### Trasformazioni e PMF condizionali",
    "## Medie condizionali": "### Media di funzioni e LOTUS",
    "## Funzioni di variabili aleatorie": "## Funzioni di variabili aleatorie",
    "### PMF": "### PMF (Probability Mass Function)",
    "### Media di funzioni di variabili aleatorie": "### Media di funzioni e LOTUS",
    "### Valore quadratico medio e varianza di una variabile aleatoria": "### Varianza e Deviazione standard",
    "## Il significato della varianza e della deviazione standard": "### Varianza e Deviazione standard",
    "## La disuguaglianza di Chebyshev": "### Disuguaglianza di Chebyshev",
    "## Quadro sintetico delle proprietà di media e varianza": "### Proprietà operative di Media e Varianza",
    "### Proprietà della Media ($\\mathbb{E}$)": "### Proprietà operative di Media e Varianza",
    "### Proprietà della Varianza ($\\sigma^2$)": "### Proprietà operative di Media e Varianza",
    "### Relazioni Correlate": "### Proprietà operative di Media e Varianza",
    "## Definizione di variabili multiple": "# 3. Variabili Aleatorie Multiple",
    "### pmf/DF/pdf congiunta": "### PMF/CDF/PDF congiunta",
    "#### Proprietà": "### PMF/CDF/PDF congiunta",
    "##### Marginalizzazione": "### Marginalizzazione",
    "## Variabili indipendenti": "## Indipendenza",
    "### Generalizzazione a $m$ variabili aleatorie": "### Generalizzazione a $m$ variabili",
    "### Le pmf condizionate": "### Generalizzazione a $m$ variabili",
    "#### Alcune proprietà": "### Generalizzazione a $m$ variabili",
    "#### Generalizzazione": "### Generalizzazione a $m$ variabili",
    "## Funzioni di variabili doppie": "## Trasformazioni di variabili doppie",
    "#### 1. Trasformazione Biunivoca (Inversa Unica)": "### Caso biunivoco",
    "#### 2. Trasformazione Non Biunivoca (Collassamento delle Probabilità)": "### Caso non biunivoco (Collassamento)",
    "### Media / Valore Atteso": "### Media di funzioni e LOTUS",
    "#### Proprietà: Il caso della combinazione lineare": "### Proprietà operative di Media e Varianza",
    "#### Generalizzazione a $m$ variabili": "### Generalizzazione a $m$ variabili",
    "### Teorema della Media Condizionata": "### Media di funzioni e LOTUS",
    "## La covarianza tra due variabili aleatorie": "## Correlazione e Covarianza",
    "#### Rappresentazione della Covarianza": "### Covarianza: Definizione e proprietà",
    "#### Rappresentazione della Correlazione": "### Correlazione e Coefficiente di Pearson",
    "### Proprietà della covarianza": "### Covarianza: Definizione e proprietà",
    "#### a) Relazione tra momento di ordine 2 e covarianza": "### Covarianza: Definizione e proprietà",
    "#### b) Incorrelazione vs Indipendenza": "### Incorrelazione vs Indipendenza",
    "#### c) Coefficiente di Correlazione (Coefficiente di Pearson)": "### Correlazione e Coefficiente di Pearson",
    "#### b) Varianza di una combinazione lineare": "### Proprietà operative di Media e Varianza",
    "# Continuo": "# 4. Variabili Aleatorie Continue",
    "## Introduzione alle Variabili Continue": "## Introduzione e CDF",
    "## Frequenza e Probabilità negli Intervalli": "## Introduzione e CDF",
    "### Frequenza": "## Introduzione e CDF",
    "### PDF": "### PDF e vincoli fondamentali",
    "#### Vincoli fondamentali": "### PDF e vincoli fondamentali",
    "## Nota di raccordo": "## Introduzione e CDF",
    "## La Cumulative Distribution Function (CDF)": "### CDF (Cumulative Distribution Function) e proprietà",
    "### Proprietà": "### CDF (Cumulative Distribution Function) e proprietà",
    "## Media statistica di variabili continue": "## Introduzione e CDF",
    "## Tipi di Variabili": "## Modelli notevoli",
    "### Variabili Uniformi": "### Uniformi, Esponenziali, Laplaciane, Cauchy",
    "#### pdf e CDF di variabili uniformi": "### Uniformi, Esponenziali, Laplaciane, Cauchy",
    "### Variabili esponenziali": "### Uniformi, Esponenziali, Laplaciane, Cauchy",
    "#### pdf e CDF di variabili esponenziali": "### Uniformi, Esponenziali, Laplaciane, Cauchy",
    "### Variabili laplaciane": "### Uniformi, Esponenziali, Laplaciane, Cauchy",
    "#### pdf e CDF di variabili laplaciane": "### Uniformi, Esponenziali, Laplaciane, Cauchy",
    "### Variabili di Cauchy": "### Uniformi, Esponenziali, Laplaciane, Cauchy",
    "#### pdf e CDF di variabili di Cauchy": "### Uniformi, Esponenziali, Laplaciane, Cauchy",
    "## PDF Condizionata: $f_{X|A}(x)$": "## PDF Condizionata",
    "### 1. Definizione tramite Limite (Approccio locale)": "### Definizione locale (Limite) e operativa (CDF)",
    "### 2. Definizione tramite CDF (Approccio operativo)": "### Definizione locale (Limite) e operativa (CDF)",
    "## Legge della probabilità totale per PDF, CDF e Medie": "### Legge della probabilità totale",
    "## Funzioni di variabili aleatorie continue": "## Funzioni di variabili continue",
    "### Funzioni invertibili": "### Invertibili (crescenti/decrescenti)",
    "#### Funzione strettamente crescente": "### Invertibili (crescenti/decrescenti)",
    "#### Funzione strettamente decrescente": "### Invertibili (crescenti/decrescenti)",
    "### Funzioni non invertibili": "### Non invertibili (Procedura operativa)",
    "#### Procedura operativa": "### Non invertibili (Procedura operativa)",
    "#### Rappresentazione grafica": "### Non invertibili (Procedura operativa)",
    "# Conversione A/D di variabili aleatorie": "# 4. Variabili Aleatorie Continue",
    "## Media di funzioni di variabili aleatorie continue": "## Introduzione e CDF",
    "## Valore quadratico medio e varianza di variabili continue": "## Introduzione e CDF",
    "## Qualche esempio": "## Introduzione e CDF",
    "## Variabili continue multiple": "## Analisi multivariata continua",
    "## pdf congiunta di due variabili aleatorie": "### PDF congiunta e marginalizzazione",
    "## Proprietà della pdf congiunta": "### PDF congiunta e marginalizzazione",
    "### Proprietà di marginalizzazione": "### PDF congiunta e marginalizzazione",
    "### Indipendenza statistica": "### Indipendenza statistica",
    "## Le pdf condizionate": "## PDF Condizionata",
    "## Proprietà delle pdf condizionate": "## PDF Condizionata",
    "### Legge della probabilità totale per le pdf": "### Legge della probabilità totale",
    "### Leggi della probabilità composta e di Bayes per le densità": "### Leggi di Bayes per densità",
    "## Altre estensioni...": "## Analisi multivariata continua",
    "### Linearità della media": "### Proprietà operative di Media e Varianza",
    "### Teorema della media condizionata": "### Media di funzioni e LOTUS",
    "## Covarianza tra due variabili continue": "## Correlazione e Covarianza",
    "### Covarianza tra $X \\in Y ;$": "### Covarianza: Definizione e proprietà",
    "### Coefficiente di correlazione tra $X \\textsf { e Y }$": "### Correlazione e Coefficiente di Pearson",
    "### Incorrelazione tra $X \\textsf { e } Y \\colon { \\mathsf { C O V } } [ X , Y ] = 0$": "### Incorrelazione vs Indipendenza",
    "## Variabili Gaussiane: Caratterizzazione marginale": "# 5. Variabili Gaussiane e Processi Aleatori",
    "## Andamenti di pdf Gaussiane": "### Caratterizzazione marginale e andamenti",
    "## La funzione Q(x)": "### Funzione Q(x) e sue proprietà",
    "## Andamento di Q(x)": "### Funzione Q(x) e sue proprietà",
    "## Alcune utili proprietà della funzione Q(x)": "### Funzione Q(x) e sue proprietà",
    "### Simmetria": "### Funzione Q(x) e sue proprietà",
    "## Caratterizzazione congiunta di variabili Gaussiane": "### Caratterizzazione congiunta (Matrice di covarianza)",
    "## Alcune proprietà della matrice di covarianza": "### Caratterizzazione congiunta (Matrice di covarianza)",
    "## Variabili congiuntamente Gaussiane": "### Processi Gaussiani",
    "## Proprietà di chiusura rispetto a trasformazioni lineari": "### Trasformazioni lineari",
    "## Richiami sulle variabili aleatorie": "# 5. Variabili Gaussiane e Processi Aleatori",
    "## Vettori aleatori": "### Definizione e vettori aleatori",
    "## Legge di Bayes per vettori aleatori": "### Leggi di Bayes per densità",
    "## Processi aleatori tempo-discreti": "### Processi tempo-discreti e continui",
    "## Commenti e osservazioni": "# 5. Variabili Gaussiane e Processi Aleatori",
    "## Un altro esempio: processo Gaussiano tempo-discreto": "### Processi Gaussiani",
    "## Caratterizzazione del secondo ordine del processo": "### Caratterizzazione: Primo, secondo ordine e completa",
    "## Caratterizzazione completa di un processo": "### Caratterizzazione: Primo, secondo ordine e completa",
    "## Processi discreti": "### Processi tempo-discreti e continui",
    "## Un altro esempio: Un processo quaternario": "### Processi tempo-discreti e continui",
    "## Caratterizzazione di processi discreti": "### Caratterizzazione: Primo, secondo ordine e completa",
    "## Caratterizzazione sintetica dei vettori aleatori": "### Definizione e vettori aleatori",
    "## Processi Stazionari in Senso Lato (SSL)": "### Stazionarietà in senso lato (SSL)",
    "## Matrice di covarianza per processi SSL": "### Stazionarietà in senso lato (SSL)",
    "## Esercizio: La matrice di covarianza è sempre definita non-negativa": "### Stazionarietà in senso lato (SSL)",
    "## Estensione ai processi continui: definizioni": "### Processi tempo-discreti e continui",
    "## Un esempio: Processi Gaussiani": "### Processi Gaussiani",
    "## Proprietà dei processi Gaussiani": "### Processi Gaussiani",
    "## Tipi di convergenza": "### Tipi di convergenza",
    "## Convergenza in distribuzione": "### Tipi di convergenza",
    "## La funzione generatrice dei momenti": "### Funzione generatrice dei momenti",
    "# Elementi di Statistica inferenziale": "# 6. Statistica Inferenziale e Stima",
    "## Alcune Definizioni": "## Inferenza Bayesiana",
    "## Un esempio: la media campionaria": "## Inferenza Bayesiana",
    "## La media campionaria - cont.": "## Inferenza Bayesiana",
    "## La distribuzione empirica": "## Inferenza Bayesiana",
    "## Convergenza quasi certa": "### Tipi di convergenza",
    "## Convergenza quasi certa - cont.": "### Tipi di convergenza",
    "## Commenti": "# 6. Statistica Inferenziale e Stima",
    "## Statistiche Inferenziali": "## Inferenza Bayesiana",
    "## Impostazione Bayesiana: Regola di decisione": "### Teoria della decisione e Costi Bayesiani",
    "## Costi Bayesiani": "### Teoria della decisione e Costi Bayesiani",
    "## Problema di Classificazione Binaria": "### Classificazione Binaria (Discreta e Continua)",
    "# Classificazione Binaria: leggi di dati discreti": "### Classificazione Binaria (Discreta e Continua)",
    "## Alcuni commenti": "### Classificazione Binaria (Discreta e Continua)",
    "## Esempio: classificazione di sorgenti binarie": "### Classificazione Binaria (Discreta e Continua)",
    "## Valutazione delle prestazioni": "### Classificazione Binaria (Discreta e Continua)",
    "## Classificazione binaria: legge dei dati continui": "### Classificazione Binaria (Discreta e Continua)",
    "## Esempio: test della media di una popolazione Gaussiana": "### Test di ipotesi e Neyman-Pearson",
    "## Test di ipotesi: introduzione": "### Test di ipotesi e Neyman-Pearson",
    "## Definizioni nel test di ipotesi": "### Test di ipotesi e Neyman-Pearson",
    "### Dati Continui": "### Test di ipotesi e Neyman-Pearson",
    "### Dati Discreti": "### Test di ipotesi e Neyman-Pearson",
    "## Test di Neyman-Pearson": "### Test di ipotesi e Neyman-Pearson",
    "## Prestazioni del test": "### Test di ipotesi e Neyman-Pearson",
    "## Stima dei parametri: generalità": "## Inferenza Bayesiana",
    "## Stima dei Parametri": "## Inferenza Bayesiana",
    "## Estimatore del Minimo Errore Quadratico Medio (MMSEE)": "### Estimatori (MMSE, MAP)",
    "## Esempio: Bernoulli Composta": "### Estimatori (MMSE, MAP)",
    "## Esempio: Bernoulli Composta - cont.)": "### Estimatori (MMSE, MAP)",
    "## Estimatore Maximum A Posteriori (MAPE)": "### Estimatori (MMSE, MAP)",
    "## Prestazioni dell'Estimatore: Errore Sistematico (Bias)": "### Estimatori (MMSE, MAP)",
    "## Errori Casuali: Consistenza": "### Estimatori (MMSE, MAP)",
    "## Definizioni Generali": "## Inferenza Bayesiana",
    "## Un esempio: Osservazioni Gaussiane con media casuale": "### Estimatori (MMSE, MAP)",
    "## Unicità degli stimatori Bayesiani": "### Estimatori (MMSE, MAP)",
    "# Inferenza non Bayesiana: Stima di parametri non casuali": "## Inferenza non Bayesiana",
    "## Inferenza non Bayesiana: Misure di prestazione": "## Inferenza non Bayesiana",
    "## Limite di Cramér-Rao - Fatti preliminari": "### Limite di Cramér-Rao",
    "## Limite di Cramér-Rao - Derivazione": "### Limite di Cramér-Rao",
    "## Limite di Cramér-Rao - Ulteriori discussioni": "### Limite di Cramér-Rao",
    "## Limite di Cramér-Rao - Stimatori non distorti": "### Limite di Cramér-Rao",
    "## Un esempio: inferire la frequenza del cifrario di una sorgente senza memoria": "## Inferenza non Bayesiana",
    "## Frequenza di cifratura - cont.": "## Inferenza non Bayesiana",
    "## Parametri multipli - inferenza Bayesiana": "## Inferenza Bayesiana",
    "## L'estimatore MMSE": "### Estimatori (MMSE, MAP)",
    "## L'estimatore MAP": "### Estimatori (MMSE, MAP)",
    "## Stima non Bayesiana di parametri multipli": "## Inferenza non Bayesiana",
    "## Estimatori MMSE lineari": "## Inferenza non Bayesiana",
    "## Estimatori MMSE lineari (cont.)": "## Inferenza non Bayesiana",
    "## Risolvendo per b si ottiene": "## Inferenza non Bayesiana",
    "## L'algoritmo del gradiente": "### Adattività e Algoritmo del Gradiente",
    "## L'algoritmo del Gradiente - cont.": "### Adattività e Algoritmo del Gradiente",
    "## Un approccio diverso: statistica descrittiva": "## Inferenza non Bayesiana",
    "## L'estimatore dei Minimi Quadrati (Least Squares)": "### Minimi Quadrati (Least Squares)",
    "## L'estimatore dei Minimi Quadrati - cont.": "### Minimi Quadrati (Least Squares)",
    "## Apprendimento LS": "### Minimi Quadrati (Least Squares)",
    "## La Formula di Sherman-Morrison": "### Formula di Sherman-Morrison",
    "## Generalità": "## Inferenza non Bayesiana",
    "## Applicazione": "## Inferenza non Bayesiana",
    "## Notare che": "## Inferenza non Bayesiana",
    "## Applicazione - cont.": "## Inferenza non Bayesiana",
    "## D'altra parte abbiamo": "## Inferenza non Bayesiana",
    "## Adattività in LS": "### Minimi Quadrati (Least Squares)",
    "## Generalizzazione": "## Inferenza non Bayesiana"
}

def normalizza_spazi(testo):
    # Rimuove spazi vuoti multipli o invisibili (come gli spazi unificatori \xa0)
    return " ".join(testo.split())

def aggiorna_file(filepath):
    backup_path = filepath + ".bak"
    # Crea backup temporaneo
    shutil.copy2(filepath, backup_path)

    with open(filepath, 'r', encoding='utf-8') as f:
        linee = f.readlines()

    nuove_linee = []
    modificato = False

    for linea in linee:
        linea_pulita = linea.strip()
        linea_normalizzata = normalizza_spazi(linea_pulita)

        # Cerca la corrispondenza esatta nel dizionario
        if linea_normalizzata in MAPPING:
            nuovo_titolo = MAPPING[linea_normalizzata]
            # Mantiene il tipo di a capo originale (\n o \r\n)
            newline_char = "\r\n" if linea.endswith("\r\n") else "\n"
            nuove_linee.append(nuovo_titolo + newline_char)
            modificato = True
        else:
            nuove_linee.append(linea)

    if modificato:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(nuove_linee)
        print(f"[OK] Modificato: {filepath} (Copia originale salvata in {backup_path})")
    else:
        # Se non c'è stato bisogno di cambiare nulla, eliminiamo il backup pulito
        os.remove(backup_path)

def main():
    print("=== Sostitutore Automatico di Intestazioni per Obsidian ===")
    percorso = input("Trascina qui il file .md o la cartella del Vault e premi Invio: ").strip()

    # Pulisce le virgolette inserite dal drag&drop del terminale
    percorso = percorso.strip("'\"")

    if os.path.isfile(percorso):
        aggiorna_file(percorso)
        print("Operazione conclusa con successo sul file.")
    elif os.path.isdir(percorso):
        print("Analisi della cartella in corso...")
        for root, _, files in os.walk(percorso):
            for file in files:
                if file.endswith(".md"):
                    aggiorna_file(os.path.join(root, file))
        print("Operazione conclusa su tutte le note della cartella.")
    else:
        print("[ERRORE] Percorso non valido o inesistente.")

if __name__ == "__main__":
    main()
