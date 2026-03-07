---
tags:
  - "#tag/logica-predicati"
---

# Definizioni Teoriche
> [!PDF|] [[main.pdf#page=6&selection=19,0,26,1|main, p.6]]
> > Importante distinzione che va effettuata dunque è tra funzioni totali e funzioni parziali

> [!PDF|] [[main.pdf#page=6&selection=27,3,75,1|main, p.6]]
> > na funzione associata a un problema è detta totale se ha un valore di output definito ∀ak ∈ Nk, ovvero è definibile come: f ∶ Nk → N, k ∈ N (x1, x2, ⋯, xk) ↦ y

> [!PDF|] [[main.pdf#page=6&selection=77,3,133,1|main, p.6]]
> > na funzione associata a un problema è detta parziale se ha un valore di output definito ∀ak ∈ D ⊆ Nk, ovvero è definibile come: f ∶ D ⊆ Nk → N, k ∈ N (x1, x2, ⋯, xk) ↦ y

> [!PDF|] [[main.pdf#page=6&selection=158,0,166,109|main, p.6]]
> > Per definire dunque il concetto di calcolabilità di una funzione, è necessario enunciare la tesi di Church-Turing2. Tesi di Church-Turing (Versione S) Qualsiasi funzione che si possa determinare tramite qualche procedura algoritmica è parzialmente calcolabile.
> > > [!PDF|] [[main.pdf#page=6&selection=174,2,219,24|main, p.6]]
> > Una funzione f ∶ D ⊆ Nk → N, k ∈ N è parzialmente calcolabile se esiste un algoritmo che la rappresenta. • Una funzione è calcolabile se essa è totale e parzialmente calcolabile
> 
> 


> [!PDF|] [[main.pdf#page=6&selection=223,0,223,9|main, p.6]]
> > predicato
> 
> > [!PDF|] [[main.pdf#page=6&selection=225,0,303,1|main, p.6]]
> > una particolare funzione totale il cui codominio è l’insieme {0, 1} ∈ N. Codificando il valore di 0 come FALSO e di 1 come VERO, è possibile valutare la calcolabilità di predicati logici a valori booleani. p ∶ Nk → {0, 1} ⊂ N, k ∈ N (x1, x2, ⋯, xk) ↦ y ∈ {0, 1}

## Linguaggio S
> [!PDF|] [[main.pdf#page=7&selection=25,0,183,49|main, p.7]]
> > Sintassi Variabili. Nel linguaggio S le variabili si dividono in tre gruppi: 1. Variabili d’Input (X1,X2,.....), di numero potenzialmente infinito3 inizializzate con i valori dell’input di una data istanza; 2. Variabile di Output (Y), unica e inizializzata al valore 0; 3. Variabili Temporanee (Z1,Z2,.....), di numero potenzialmente infinito inizializzate col valore 0. Etichette. Il linguaggio S permette di utilizzare delle etichette alfabetiche, label, per demarcare specifiche linee su cui poter effettuare dei salti, jump. Vengono utilizzate le lettere dell’alfabeto dalla A alla D numerate, con il caso speciale dell’etichetta E, usata per la terminazione del programma, che spiegheremo meglio in seguito. Statement. Il linguaggio S contempla solo 4 tipi di statement, o asserzioni, che possono essere combinate o meno a etichette per formare istruzioni. Nello specifico questi statement sono: • Pigra: V<--V, asserzione nulla; • Incremento: V<--V+1, incrementa una variabile qualsiasi V di 1; • Decremento: V<--V−1, decrementa una variabile qualsiasi V di 1, se essa contiene il valore 0 l’istruzione viene ignorata; • Salto: IF V!!=0 GOTO L, passa alla prima linea etichettata dall’etichetta generica L se la variabile generica V è diversa da 0, altrimenti l’istruzione viene ignorata. Nel caso l’etichetta L non esista, il programma termina. Solitamente questo meccanismo è effettuato con l’etichetta E, che viene riservata allo scopo di terminazione.

> [!PDF|] [[main.pdf#page=8&selection=17,0,43,1|main, p.8]]
> > Macro Ogni programma associato a una funzione (parzialmente) calcolabile, con stato corrente iniziale, può essere riutilizzato per il calcolo di un’altra funzione, sostituito da un alias. Quest’ultimo viene detto macro

> [!PDF|] [[main.pdf#page=8&selection=160,0,201,17|main, p.8]]
> > Predicati La codifica di predicati invece può essere utilizzata per la definizione di macro di salto con condizione diversa da !!=0. Potendo infatti conservare in una variabile generica V l’output di una qualsiasi funzione k-aria (parzialmente) calcolabile grazie alla macro di assegnazione, è possibile definire la macro di salto generalizzato: 1 V <-- P(x1,x2, ..... , xk) 2 IF V !!= 0 GOTO L

> [!PDF|] [[main.pdf#page=10&selection=0,0,53,1|main, p.10]]
> > Stato di un Programma Per Stato di un Programma P si intende un insieme finito di equazioni della forma V = n, dove V è una variabile del linguaggio S e n ∈ N, contenente una e una sola equazione per ogni variabile che compare in P.



> > [!PDF|] [[main.pdf#page=10&selection=83,0,133,20|main, p.10]]
> > Istantanea Definiamo istantanea di un programma P di lunghezza l una qualsiasi coppia ordinata del tipo: (i, σ) con i ∈ {1, ⋯, l + 1} e σ ∈ Σ insieme degli stati.


