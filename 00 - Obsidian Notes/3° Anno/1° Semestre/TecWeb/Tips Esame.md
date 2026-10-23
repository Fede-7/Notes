# TIPS d'esame
## JavaScript
### Funzionamento dell'Ereditarietà

> *"A volte ci sono delle domande che chiedono 'descrivi il funzionamento dell'ereditarietà'... secondo voi la risposta che io voglio quando dico 'scrivetemi...' è che ci stanno le classi e la parola chiave extends?"*

#### Cosa NON vuole (l'errore classico da evitare)

Il professore spiega che **non le basta** sentirsi dire semplicemente che in JavaScript esistono le classi e che si usa la sintassi `class ... extends ...`. Chi scrive solo questo dimostra di non aver capito come funziona davvero il linguaggio sotto il cofano.

#### La risposta che si ASPETTA (e che premia all'esame)

Per ottenere il massimo del punteggio, la risposta deve articolarsi su questi punti fondamentali:

1. **Il meccanismo prototipale**: Spiegare che l'ereditarietà in JavaScript **non è basata sulle classi, ma sui prototipi**. Ogni oggetto possiede una proprietà speciale interna che punta al suo oggetto "antenato" (o a `null`).
2. **La risalita della catena dei prototipi (*Prototype Chain*)**: Quando si accede in lettura a una proprietà o a un metodo su un oggetto, se l'interprete non li trova sull'oggetto stesso, **risale la catena dei prototipi** fino a trovarli o fino a raggiungere `null`.
3. **Ereditarietà fatta a mano con i costruttori**: Dimostrare che l'ereditarietà si può implementare interamente **senza usare la parola chiave `class`**, sfruttando le funzioni costruttore e la proprietà `.prototype` (es. impostando `FunzioneCostruttore.prototype = oggettoPadre`).
4. **`class` ed `extends` come zucchero sintattico**: Concludere precisando che le parole chiave `class` ed `extends` (introdotte in ES6) sono soltanto un'astrazione superficiale (*syntactic sugar*) che, sotto il cofano, si limita a creare la medesima struttura di prototipi e funzioni costruttore.

---

- Explain, step by step, what is going on under the hood when the greet method is invoked on a Student object created by the Student constructo

- Explain, step by step, whatis going on under the hoodwhen the greet method is invoked on an object created using the Student constructor and what happens when the greet method is invoked on an object created using thePerson constructor.