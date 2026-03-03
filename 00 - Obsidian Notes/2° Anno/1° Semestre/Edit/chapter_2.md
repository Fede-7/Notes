# Operazioni sulle funzioni e Paradigma Funzionale

## Paradigma Funzionale

Fino a ora abbiamo utilizzato un approccio *diretto* per la valutazione della calcolabilità di una funzione. Questo approccio presenta
svariati limiti, primo dei quali è la necessità di dimostrare come calcolabile una singola funzione alla volta, senza poter
trarre conclusioni  di carattere generale o di caratterizzare insiemi o classi di funzioni.

Per avere un approccio più generale e sistematico alla valutazione della calcolabilità delle funzioni è necessario dunque
approcciare il problema in maniera diversa, utilizzando un paradigma diverso che sfrutti[^1]
le proprietà e le operazioni delle funzioni stesse per valutarne la calcolabilità.

## Operazioni fondamentali e Classi PRC


Con **operazioni sulle funzioni** facciamo riferimento a operazioni algebriche definite nell'insieme delle funzioni, ovvero operazioni che hanno sia come operando che come risultato delle funzioni.
Definiamo dunque le due operazioni fondamentali sulle funzioni: la **composizione** e la **ricorsione primitiva**.

### Composizione


> [!definition] Composizione di Funzioni
> \label{Composizione di funzioni Def

> Sia $f$ una funzione $k\text{-aria}$ e $ g_1, g_2, \cdots,g_k$ funzioni $n\text{-arie}$. Allora la funzione $h$ $n\text{-aria}$ è **composizione** di $f, g_1, g_2, \cdots,g_k$ se:
$$
    h(x_1,\cdots,x_n)=f(g_1(x_1,\cdots,x_n),\cdots,g_k(x_1,\cdots,x_n))
$$


È importante notare che la composizione di funzioni è ben definita anche per *funzioni parziali*.
Infatti si avrà che, data $(x_1,\cdots,x_n) \in \mathbb{N}$:

$$
    h(x_1,\cdots,x_n)\uparrow \iff \exists i \in \{1,\cdots,k\}: g_i(x_1,\cdots,x_n)\uparrow \vee f(g_1(x_1,\cdots,x_n),\cdots,g_k(x_1,\cdots,x_n))\uparrow
$$


Con ragionamento simile è anche possibile dimostrare che la composizione di **funzioni parzialmente calcolabili** è necessariamente **parzialmente calcolabile**.

---


> [!theorem] Teorema di Composizione
> **Enunciato.** Sia $h$ ricavata per composizione di $f, g_1, g_2, \cdots,g_k$ **parzialmente calcolabili**, allora $h$ è **parzialmente calcolabile**.
>
>
> **Dimostrazione.** Per definizione di **composizione** si ha $h=\Psi_{\mathcal{P}}^{(n)}$, dove $\mathcal{P}$ è:
```ini
    Z1 <- g_1(x_1,\cdots,x_n)
    \vdots
    Zk <- g_k(x_1,\cdots,x_n)
    Y <- f(Z_1,\cdots,Z_k)
```


Inoltre come notato in precedenza il programma non arriva a terminazione *se e solo se* uno dei programmi $g_i$ o $f$ non termina, dunque:
$$
    h \text{ non totale } \implies \exists i \in \{1,\cdots,k\}: g_i \text{ non totale} \lor f \text{ non totale}
$$

Non è necessariamente vero il viceversa però. Infatti se il codominio di una funzione totale $f$ che compone $h$ è un sottoinsieme del dominio di un'altra parziale $g$ che compone a sinistra[^2],
la funzione composta sarà totale, poiché quella totale escluderà i casi gli input di non terminazione dalla prima.
Vediamo qualche esempio al riguardo per chiarire il concetto.

> [!example] Esempi
> - Sia $h_1(x)=2x$. Possiamo considerare $h$ come funzione composta da $f_1(x_1, x_2)=x_1 \cdot x_2$, $g_1(x)=2$ e $g_2(x)=x$, o alternativamente, notando che $h_1(x)=2x=x+x$ ovvero composizione di $f_2(x_1,x_2)=x_1+x_2$ e $g_2(x)=x$, dunque $h_1$ è calcolabile.
> - Sia $h_2(x)=4x^2$. Possiamo considerare $h_2$ come funzione composta dalle funzioni $f_1$ e $h_1$ sopracitate, infatti $h_2(x)=4x^2=2x\cdot 2x$, dunque $h_2$ è calcolabile.
> - Sia $h_3(x)=4x^2-2x$. Si ha $h_3(x)\downarrow \forall x \in \mathbb{N}$, dato che $\forall x \in \mathbb{N}, 4x^2 \geq 2x$. Abbiamo dunque che la funzione $h_3$ è totale. Ma $h_3(x)=f_3(h_2(x),h_1(x))$, dove $f_3(x_1,x_2)=x_1-x_2$ **non è totale**[^3]. Abbiamo dunque che l'implicazione non vale in entrambi i sensi come precedentemente detto.


### Ricorsione Primitiva


L'operazione di **ricorsione primitiva** è un'operazione che permette di definire una funzione in maniera ricorsiva, ovvero definendo un caso base e un passo ricorsivo, formalizzando matematicamente il concetto di algoritmo ricorsivo.
Nonostante sia definibile anche per le **funzioni parziali**, noi tratteremo solo il caso delle **funzioni totali**.

Per una funzione $h$ unaria diremo che è ricavata per **ricorsione primitiva** da $k\in\mathbb{N}$ e $g$ funzione binaria **totale** se:
$$
    \begin{cases}
    h(0)=k\\
    h(t+1)=g(t,h(t)), & \forall t\in\mathbb{N}^*
    \end{cases}
$$


Nonostante affronteremo prevalentemente funzioni unarie, è importante dare una definizione generale per qualsiasi funzione.

> [!definition] Ricorsione Primitiva
> \label{Ricorsione Primitiva Def

> Una funzione $h$ $n-aria$ si ricava per ricorsione primitiva da $f$ $(n-1)\text{-aria}$ e da $g$ $(n+1)\text{-aria}$, se $\forall x_1,\cdots,x_{n-1} \in \mathbb{N}$ vale:
$$
    \begin{cases}
    h(x_1,\cdots,x_{n-1}, 0)=f(x_1,\cdots,x_{n-1})\\
    h(x_1,\cdots,x_{n-1}, t+1)=g(x_1,\cdots,x_{n-1},t,h(x_1,\cdots,x_{n-1}, t)), & \forall t\in \mathbb{N}^*
    \end{cases}
$$


---


> [!theorem] Teorema di Ricorsione primitiva
> **Enunciato.** Sia $h$ ricavata per ricorsione primitiva da $f$ e $g$ calcolabili, allora $h$ è calcolabile.
>
>
> **Dimostrazione.** Per definizione di **ricorsione primitiva** si ha $h=\Psi_{\mathcal{P}}^{(n)}$, dove $\mathcal{P}$ è:
```ini
      Y <- f(X_1,\cdots,X_{n-1})
  [A] IF Xn == 0 GOTO E
      Y <- g(X_1,\cdots,X_{n-1},Y,Z)
      Z <- Z + 1
      Xn <- Xn - 1
      GOTO A
```


Questo programma calcola esattamente la funzione $h$ poiché, se ci trovassimo nel primo caso della definizione~*(ref: Ricorsione Primitiva Def)* l'output sarebbe dato dalle linee `1--2`, altrimenti, se ci trovassimo nel secondo caso, le linee `3--6` calcolerebbero ricorsivamente l'output di $h$, dimostrata così calcolabile.

### Classi PRC e Funzioni Ricorsive Primitive


Le due operazioni appena definite sono alla base del paradigma funzionale e definiscono, insieme ad alcune specifiche funzioni, una classe di funzioni chiamate **PRC**.

> [!definition] Classi PRC di funzioni
> \label{Classi PRC di funzioni Def

> Un insieme di funzioni totali $\mathcal{C}$ è detto **PRC** se è chiuso rispetto alle operazioni di composizione e ricorsione primitiva e contiene:
> \begin{itemize}
> \item La funzione nulla $n(x)=0$;
> \item La funzione successore $s(x)=x+1$;
> \item Le funzioni proiezione $u_i^{(n)}(x_1,\cdots,x_n)=x_i, \forall (n\geq 1 \land 1\leq i \leq n )$.
> \end{itemize}


Dato che le funzioni iniziali[^4] sono facilmente calcolabili e visti i risultati dei teoremi~*(ref: Teorema compozione)* e~*(ref: Teorema ricorsione primitiva)*, possiamo notare che l'insieme delle **funzioni calcolabili** è una **classe PRC**.

> [!definition] Funzioni Ricorsive Primitive
> \label{Funzioni Ricorsive Primitive Def

> Una funzione è detta **ricorsiva primitiva** se è ottenibile dalle funzioni iniziali mediante un numero finito di applicazioni di composizione e ricorsione primitiva.


È importante notare che, dalla definizione di **classe PRC** e dalle proprietà degli **insiemi chiusi**, l'insieme delle **funzioni ricorsive primitive** è contenuto in tutte le **classi PRC**, ed è dunque in particolare la più piccola **classe PRC**.

In particolare, essendo **l'insieme delle funzioni calcolabili** una **classe PRC**, si ha che **ogni funzione ricorsiva primitiva è calcolabile**.

---

Andiamo ora a elencare una serie di esempi significativi di funzioni ricorsive primitive, che verranno poi usate sia per definire nuove funzioni che per dimostrare l'appartenenza di altre funzioni alla stessa classe.

> [!example] Esempi
> 1. Consideriamo la funzione $a(x_1,x_2) = x_1+x_2$. Possiamo vedere che questa è **ricorsiva primitiva** da:
>   2. []
$$
    \begin{cases}
    a(x_1,0)=x_1=u_1^{(1)}(x)\\
    a(x_1,t+1)=x+t+1=a(x_1,t)+1=s(a(x_1,t))=g(t, a(x,t),x), & \forall t \in \mathbb{N}^*
    \end{cases}
$$

> Dove $g(x,y,z)=s(y)=s(u_2^{(3)}(x,y,z))$ è ottenuta per composizione di funzioni iniziali, ed è dunque **ricorsiva primitiva**.
> 3. Consideriamo la funzione $m(x,y)=x\cdot y$. Possiamo vedere che questa è **ricorsiva primitiva** da:
>   4. []
$$
    \begin{cases}
    m(x,0)=0=n(x)\\
    m(x, t+1)=m(x, t)+x=a(m(x,t),x)=g'(t, m(x, t),x), & \forall t \in \mathbb{N}^*
    \end{cases}
$$

> Dove $g'(x,y,z)=a(u_2^{(3)}(x,y,z),u_3^{(3)}(x,y,z))$ è ottenuta per composizione di funzioni iniziali, ed è dunque **ricorsiva primitiva**.
> 5. Consideriamo la funzione **fattoriale $x!$**, definita come:
>   6. []
$$
    x! =\begin{cases}
    1, & x=0\\
    x\cdot (x-1)!,&  x>0
    \end{cases}
$$

> Possiamo vedere che questa è **ricorsiva primitiva** da:
$$
    \begin{cases}
    0! =1=s(0)\\
    (t+1)! =(t+1)\cdot t! =m(t+1, t!)=g(t+1,t!), & \forall t \in \mathbb{N}^*
    \end{cases}
$$

> 7. Consideriamo la funzione **precedente**:
>   8. []
$$
    p(x)=\begin{cases}
    0, &  x=0\\
    x-1, & x>0
    \end{cases}
$$

> Possiamo vedere che questa è **ricorsiva primitiva** da:
$$
    \begin{cases}
    p(0)=0=n(x)\\
    p(t+1)=t=u_1^{(2)}(t,p(t))=g(t, p(t)), & \forall t \in \mathbb{N}^*
    \end{cases}
$$

> 9. Consideriamo ora un'alternativa alla funzione Sottrazione:
>   10. []
$$
    x\dot{-} y =  \begin{cases}
    0, & x<y \\
    x-y, & x\geq y
    \end{cases}
$$

> Possiamo vedere che questa è **ricorsiva primitiva** da:
$$
    \begin{cases}
    x\dot{-} 0=x=u_1^{(1)}(x)\\
    x\dot{-} (t+1)=p(x\dot{-} t)=g(x, x\dot{-} t,t), & \forall t \in \mathbb{N}^*
    \end{cases}
$$

> Dove $g(x,y,z)=p(u_2^{(3)}(x,y,z))$ è ottenuta per composizione di funzioni iniziali, ed è **ricorsiva primitiva**[^5].
> 11. Consideriamo ora il predicato[^6] $\alpha(x)\iff x=0$, esprimibile anche come:
>   12. []
$$
    \alpha(x)=\begin{cases}
    1, & x=0\\
    0, & x>0
    \end{cases} = 1\dot{-} x
$$

> Questo predicato è **ricorsivo primitivo**, essendo composizione di funzioni dimostrate come tali.
> 13. Consideriamo ora il predicato $\beta(x,y)\iff x=y$, esprimibile anche come[^7]:
>   14. []
$$
    \beta(x,y)=\begin{cases}
    1, & x=y\\
    0, & x\neq y
    \end{cases} = \alpha(\abs{x-y})
$$

> Questo predicato è ricorsivo primitivo, essendo composizione di funzioni dimostrate come tali[^8].


---

## Proprietà di chiusura delle Classi PRC


Definite le classi PRC e, notato che l'insieme delle funzioni calcolabili ne è un esempio, è naturale chiedersi se esse siano chiuse rispetto ad altre operazioni oltre a quelle che le definiscono.

Proprietà di chiusura di questo tipo sono importanti per poter caratterizzare le classi PRC e per poter dimostrare l'appartenenza di una funzione a una di esse, e dunque la sua calcolabilità.

Andiamo dunque a elencare e dimostrare le proprietà di chiusura delle classi PRC.

### Chiusura per congiunzione, disgiunzione e negazione


> [!theorem] Teorema di Chiusura per congiunzione$\text{,
> **Enunciato.** Siano $p$ e $q$ predicati n-ari appartenenti a $\mathcal{C}$ **classe PRC**, allora anche i predicati $p \land q$, $p \lor q$, $\neg p$, $\neg q$ appartengono a $\mathcal{C}$.
>
>
> **Dimostrazione. **
> - $(p \land q)(x_1,\cdots,x_n) = p(x_1,\cdots,x_n) \cdot q(x_1,\cdots,x_n)$, è dunque **ricorsivo primitivo** da composizione di funzioni ricorsive primitive.
> - $(\neg p)(x_1,\cdots,x_n)=\alpha(p(x_1,\cdots,x_n))$, è dunque **ricorsivo primitivo** da composizione di funzioni ricorsive primitive, vale il ragionamento analogo per $\neg q$.
> - $(p \lor q)(x_1,\cdots,x_n) \iff \neg(\neg p(x_1,\cdots,x_n) \land \neg q(x_1,\cdots,x_n))$, è dunque **ricorsivo primitivo** dalle leggi di De Morgan e dal ragionamento precedente.


Avendo dimostrato che i predicati $x \leq y$ e $x=y$ sono **ricorsivi primitivi** e utilizzando il teorema appena dimostrato, sappiamo che sono ricorsivi primitivi anche i **predicati** $x<y\iff x\leq y \land \neg (y= x)$, $x\geq y\iff\neg(x<y)$ e $x>y$, dalle precedenti.

### Definizione per Casi


Andiamo ora a individuare un ulteriore metodo per definire funzioni che, come vedremo, è una proprietà di chiusura per le classi PRC, ovvero la **definizione per casi**.

> [!definition] Definizione per Casi

> Siano $g$ e $h$ funzioni $n\text{-arie}$ e $p$ predicato $n\text{-ario}$ allora la funzione $n\text{-aria}$ $f$ è **definita per composizione** se definita come:
$$
    f(x_1,\cdots,x_n)=\begin{cases}
    g(x_1,\cdots,x_n), & p(x_1,\cdots,x_n)\\
    h(x_1,\cdots,x_n), & \neg p(x_1,\cdots,x_n)
    \end{cases}
    
$$


In altre parole una funzione **definita per casi** è una funzione la cui immagine dipende da un predicato, ovvero da una condizione che può essere vera o falsa riguardante le incognite della funzione stessa.
Possiamo trovare una proprietà di chiusura per le **Classi PRC** per la **definizione per casi** simile a quelle viste per composizione e ricorsione primitiva.

> [!theorem] Teorema di Definizione per Casi
> **Enunciato.** Siano g e h funzioni $n\text{-arie}$ in $\mathcal{C}$ **classe PRC** e $p$ predicato $n\text{-ario}$ in $\mathcal{C}$, allora a $\mathcal{C}$ appartiene anche la funzione $n\text{-aria}$ $f$ **definita per casi** da $g,h$ e $p$.
>
>
> **Dimostrazione.** Si ha:
$$
    f(x_1,\cdots,x_n)=g(x_1,\cdots,x_n)p(x_1,\cdots,x_n)+h(x_1,\cdots,x_n)(\neg p)(x_1,\cdots,x_n)
$$

> Per la proprietà di chiusura per **composizione** e **ricorsione primitiva** dimostrata in precedenza, $f\in\mathcal{C}$


È possibile generalizzare la definizione di **definizione per casi** a più casi, ovvero a più funzioni e più predicati, la cui proprietà di chiusura è  a sua volta dimostrabile[^9].

---


> [!theorem] Corollario al Teorema di Definizione per Casi
> **Enunciato.** Se $g_1,\cdots,g_k,h,p_1,\cdots,p_k$ sono funzioni e predicati n-ari in $\mathcal{C}$ **classe PRC**, allora a $\mathcal{C}$ appartiene anche la funzione $n\text{-aria}$ $f$ definita come:
$$
    f(x_1,\cdots,x_n)=\begin{cases}
    g_1(x_1,\cdots,x_n), & p_1(x_1,\cdots,x_n)\\
    \vdots \\
    g_k(x_1,\cdots,x_n), & p_k(x_1,\cdots,x_n)\\
    h(x_1,\cdots,x_n), & \text{altrimenti}
    \end{cases}
$$

>
>
> **Dimostrazione.** Si può dimostrare che $f$ è **ricorsiva primitiva** per **induzione** su $k$. Il **caso base** è rappresentato dal teorema precedente.
> Per quando riguarda il **passo induttivo** $k\implies k+1$, consideriamo la funzione $f'$ definita come:
$$
    f'(x_1,\cdots,x_n)=\begin{cases}
    g_k(x_1,\cdots,x_n), & p_k(x_1,\cdots,x_n)\\
    h(x_1,\cdots,x_n), & \text{altrimenti}
    \end{cases}
$$

> Per il teorema precedente $f' \in \mathcal{C}$.
> A questo punto possiamo riscrivere $f$ come:
$$
    f(x_1,\cdots,x_n)=\begin{cases}
    g_1(x_1,\cdots,x_n), & p_1(x_1,\cdots,x_n)\\
    \vdots\\
    g_{k-1}(x_1,\cdots,x_n), & p_{k-1}(x_1,\cdots,x_n)\\
    f'(x_1,\cdots,x_n), & \text{altrimenti}
    \end{cases}
$$

> Per ipotesi di induzione, essendo ora $f$ definita da $k$ funzioni appartenenti a $\mathcal{C}$ e $k$ predicati appartenenti a $\mathcal{C}$, $f \in \mathcal{C}$.


### Operatori di Sommatoria e Produttoria e Quantificatori Limitati


Come abbiamo già visto, la combinazione di funzioni $f\in\mathcal{C}$ **classe PRC**, mediante somma e prodotto appartiene ancora $\mathcal{C}$.
Possiamo generalizzare questo processo di composizione mediante gli operatori di **sommatoria e produttoria**.

> [!definition] Sommatoria e Produttoria di funzioni
> \label{Sommatoria e Produttoria di funzioni Def

> Sia $f$ una funzione $(n+1)\text{-aria}$, allora definiamo come **operatori di sommatoria e produttoria** le funzioni:
$$
    \begin{split}
    \sigma_f(x_1,\cdots,x_n,y)=\sum_{i=0}^{y}f(x_1,\cdots,x_n,i)\\
    \pi_f(x_1,\cdots,x_n,y)=\prod_{i=0}^{y}f(x_1,\cdots,x_n,i)
    \end{split}
$$


Come le operazioni precedenti, anche per gli **operatori di sommatoria e produttoria** è possibile dimostrare una proprietà di chiusura per le **classi PRC**.

> [!theorem] Teorema di chiusura per Sommatoria e Produttoria delle classi PRC
> **Enunciato. ** Sia $f$ una funzione $(n+1)\text{-aria}$ in $\mathcal{C}$ **classe PRC**, allora appartengono a $\mathcal{C}$ anche le funzioni $\sigma_f$ e $\pi_f$.
>
>
> **Dimostrazione. ** Dimostriamo per **ricorsione primitiva**. Si ha:
$$
    \begin{cases}
    \sigma_f(x_1,\cdots,x_n,0)=f(x_1,\cdots,x_n,0)\\
    \sigma_f(x_1,\cdots,x_n,t+1)=\sigma_f(x_1,\cdots,x_n,t)+f(x_1,\cdots,x_n,t+1), \forall t \in \mathbb{N}^*
    \end{cases}
$$

> Si può dunque vedere che $\sigma_f$ è **ricorsiva primitiva** da composizione di funzioni iniziali.
> Per ragionamento analogo si dimostra anche che $\pi_f$ è **ricorsiva primitiva**.


Gli **operatori di sommatoria e produttoria** sono utili per dimostrare come appartenente a **classi PRC** ulteriori costrutti matematici.
Un primo esempio sono i **quantificatori limitati esistenziale e universale**.

---


> [!definition] Quantificatori limitati
> \label{Quantificatori limitati Def

> Sia $p$ un predicato $(n+1)\text{-ario}$, allora definiamo i **quantificatori limitati esistenziale e universale** $E_p$ e $U_p$ come:
$$
    \begin{split}
    E_p(x_1,\cdots,x_n,y)\iff \exists t \leq y: p(x_1,\cdots,x_n,t)\\
    U_p(x_1,\cdots,x_n,y)\iff \forall t \leq y: p(x_1,\cdots,x_n,t)
    \end{split}
$$


È fondamentale definire questi quantificatori **limitati superiormente**, poiché altrimenti non sarebbe possibile dimostrare la proprietà di chiusura delle **classi PRC** a loro relativa.

> [!theorem] Teorema di chiusura per quantificatori limitati delle classi PRC
> **Enunciato. ** Sia $p$ una funzione $(n+1)\text{-ario}$ in $\mathcal{C}$ **classe PRC**, allora appartengono a $\mathcal{C}$ anche i predicati $E_p$ e $U_p$ $(n+1)\text{-ari}$ definiti come:
$$
    E_p(x_1,\cdots,x_n,y)\iff \exists t \leq y: p(x_1,\cdots,x_n,t)
    U_p(x_1,\cdots,x_n,y)\iff \forall t \leq y: p(x_1,\cdots,x_n,t)
$$

>
>
> **Dimostrazione. **  Per $E_p$ si ha che:
$$
    E_p(x_1,\cdots,x_n,y)\iff\sum_{t=0}^y p(x_1,\cdots,x_n,y)> 0
$$

> poiché la sommatoria darà $0$ nel caso non esista un $t$ tale che $p(x_1,\cdots,x_n,t)$, e viceversa un valore positivo nel caso esista.
> Per $U_p$ si ha che:
$$
    U_p(x_1,\cdots,x_n,y)=\prod_{t=0}^y p(x_1,\cdots,x_n,y)
$$

> poiché in caso esista un predicato che restituisce $0$ la produttoria verrebbe annullata.


> [!example] Esempi
> Grazie a questi quantificatori, è possibile caratterizzare altri predicati aritmetici come **ricorsive primitive**.
> 1. Predicato di divisibilità:
$$
    x|y \iff \exists z \leq y: x\cdot z = y
$$

> È possibile in questo caso **limitare superiormente** la ricerca di $z$ poiché per far si che $x|y$ sia vero, $z$ deve essere minore o uguale a $y$.
> 2. Predicato numero primo:
$$
    \text{Primo}(x) \iff x>1 \land \forall z \leq x: (\neg(z|x) \lor z=1 \lor z=x)
$$

> In questo modo esprimiamo proprio che $x$ è primo *se e solo se* ha come divisori solo $1$ e se stesso.


### Minimalizzazione limitata

Un ulteriore operazione per cui è dimostrabile una proprietà di chiusura delle **classi PRC** è la **minimalizzazione limitata**.
> [!definition] Minimalizzazione limitata
> \label{Minimalizzazione limitata Def

> Sia $p$ un predicato $(n+1)\text{-ario}$, allora la funzione $(n+1)\text{-aria}$ $\min_{t\leq y}$ è definita come:
$$
    \min_{t\leq y}(p(x_1,\cdots,x_n,y))=\begin{cases}
    \min(Z_y)=\{t\leq y| p(x_1,\cdots,x_n,t)\}, & \exists t \leq y: p(x_1,\cdots,x_n,t)\\
    0, & \text{altrimenti}
    \end{cases}
$$


Dove $\min(Z_y)$ è il minimo elemento dell'insieme $Z_y$, insieme dei valori $t\leq$ y per cui $p(x_1,\cdots,x_n,t)$ è vero.
Questa funzione dunque, dato un predicato $p$ e un **limite superiore** $y$ restituisce, se esiste[^10], il minimo $t \in \{0, \cdots, y\}$ per cui il predicato $p$ è vero, altrimenti restituisce $0$.

---


\begin{halfframedbox} {red!75!black}{Teorema di chiusura per minimalizzazione limitata delle classi PRC}
**Enunciato. ** Sia $p$ un predicato $(n+1)\text{-ario}$ in $\mathcal{C}$ **classe PRC**, allora appartiene a $\mathcal{C}$ anche la funzione $(n+1)\text{-aria}$ $\min_{t\leq y}$ definita per minimalizzazione limitata da $p$.


**Dimostrazione. ** Consideriamo la seguente funzione $g$:
$$
    g(x_1,\cdots,x_n,y)=\sum_{u=0}^y\prod_{t=0}^{u}\alpha(p(x_1,\cdots,x_n,t))
$$

Analizziamo $g$ dall'interno. La funzione $\alpha$ agisce sui predicati come negazione. Dunque si avrà:
$$
    \alpha(p(x_1,\cdots,x_n,t))= \begin{cases}
    1, & \neg p(x_1,\cdots,x_n,t)\\
    0, & p(x_1,\cdots,x_n,t)
    \end{cases}
$$

Inevitabilmente si avrà che la produttoria in $g$ si annullerà nel caso in cui $p(x_1,\cdots,x_n,t)$ sia vera per qualche $t\leq u$, ovvero:
$$
    \prod_{t=0}^{u}\alpha(p(x_1,\cdots,x_n,t))=1\iff\forall t \leq u, \neg p(x_1,\cdots,x_n,t)
$$


Di conseguenza, iterando su $u$, otterremo che le varie **produttorie** varranno $1$ fino a quando non si avrà il primo $u=t_0$ tale che $p(x_1,\cdots,x_n,u)$ risulti vera, e sarà nulla da quel momento in poi, essendoci l'iterazione $t_0$-esima ad annullarla.

Dovendo infine la **sommatoria esterna** fare esattamente $t_0$ passi prima di raggiungere tale $u$ minimo, si avrà che $g(x_1,\cdots,x_n,y)=t_0$, che abbiamo dimostrato essere il **minimo cercato**.

Si avrà dunque che la funzione $g=\text{min} Z_y\in\mathcal{C}$ essendo composizione di funzioni appartenenti a $\mathcal{C}$. Di conseguenza anche la funzione $\min_{t\leq y}\in\mathcal{C}$, poiché **definita per casi**.


> [!example] Esempi
> Grazie alla minimalizzazione limitata è possibile definire altri predicati aritmetici come **ricorsive primitive**.
> 1. **Divisione con resto $\left\lfloor \frac{x}{y} \right\rfloor$**. Questo predicato è definibile come:
>   2. []
$$
    \left\lfloor \frac{x}{y} \right\rfloor = \min_{t\leq x} ((t+1)y > x)
$$

> Infatti il minimo $t$ per cui $(t+1)y > x$ è proprio il quoziente cercato, poiché per $t$ più piccoli il prodotto con $y$ sarà minore di $x$ e dunque non potrà essere risultato della divisione.
> 3. **Operatore di resto $x \mod y$**. Questo predicato è definibile come:
>   4. []
$$
    x \mod y = x \dot{-} \left\lfloor \frac{x}{y} \right\rfloor y
$$

> 5. **$N\text{-esimo}$ primo.** Definiamo $P_0=0$ e sia per $n>0, P_n$ l'$n\text{-esimo}$ numero primo. Dimostriamo che questa funzione è **ricorsiva primitiva**.
> Consideriamo la funzione definita come:
>   6. []
$$
    P_{n+1}=\min_{t\leq P_{n}!+1}(\text{Primo}(t) \land t>P_n)
$$

> Questa restituisce il minimo numero primo maggiore di $P_n$, ovvero il successivo numero primo. Infatti si ha:
$$
    \forall i\in\{1,\cdots,n\}, \neg(P_i|(P_n!+1))
$$

> poiché[^11]   $(P_n!+1)\mod (P_i)=1$, ovvero nessun primo $\leq P_n$ divide $P_n!+1$. Dunque qualsiasi fattore primo di $P_n!+1$ sarà maggiore di $P_n$, e in particolare[^12]   si avrà $P_n!+1\geq P_{n+1}$.
>
> Definiamo dunque:
$$
    h(y,z) := \min_{t\leq y}(\text{Primo}(t) \land t>y)
$$

> questa è ricorsiva primitiva per il teorema di minimalizzazione limitata.
>
> Definiamo infine:
$$
    k(x):= h(x, x!+1)
$$

> Questa è ricorsiva primitiva per composizione di funzioni ricorsive primitive. Possiamo infine definire per ricorsione primitiva $P_n$ come:
$$
    \begin{cases}
    P_0=0\\
    P_{n+1}=k(P_n)
    \end{cases}
$$


---


## Funzioni parzialmente calcolabili


Abbiamo analizzato le **classi PRC** nelle loro proprietà poiché abbiamo dimostrato che la classe delle **funzioni calcolabili è PRC**.
Dal capitolo~*(ref: chapter 1)* però, sappiamo che le **funzioni calcolabili** non sono le uniche di cui si può valutare la calcolabilità, infatti esse sono un sotto insieme delle **funzioni parzialmente calcolabili**.
Queste però sono escluse dalle caratterizzazioni delle **classi PRC** poiché definite solo per funzioni totali.
Per ovviare a questa lacuna possiamo fornirci di un ulteriore operatore, quello di **minimalizzazione illimitata** che, come vedremo, ci permetterà di caratterizzare a pieno la classe delle **funzioni parzialmente calcolabili**.

### Minimalizzazione illimitata


> [!definition] Minimalizzazione illimitata
> \label{Minimalizzazione illimitata Def

> Sia $p$ un predicato $(n+1)\text{-ario}$, allora chiamiamo **minimalizzazione illimitata** la funzione $(n+1)\text{-aria}$ $\min_t$ definita come:
$$
    \min_t\; p(x_1,\cdots,x_n,t)= \begin{cases}
    \min\{t\in\mathbb{N} | p(x_1,\cdots,x_n,t)\} , & \exists t \in \mathbb{N}: p(x_1,\cdots,x_n,t)\\
    \uparrow, &\text{altrimenti}
    \end{cases}
$$


Per far si che quest'operatore sia utile nella caratterizzazione delle **funzioni parzialmente calcolabili** è necessario dimostrare che esso stesso è **parzialmente calcolabile**.

> [!theorem] Calcolabilità della Minimalizzazione illimitata
> **Enunciato.** Se p un predicato calcolabile. Allora $m$ **minimalizzazione illimitata** è parzialmente calcolabile.
>
>
> **Dimostrazione.** Non potendo utilizzare le proprietà delle **classi PRC** ricorriamo al seguente S-programa:
```ini
[A] IF p(X_1,\cdots,X_n,Y) GOTO E
    Y <- Y + 1
    GOTO A
```
>
> Si avrà infatti che se $p(x_1,\cdots,x_n,t)$ è vera per qualche $t$, il programma terminerà restituendo il minimo $t$  trovato, altrimenti il programma non terminerà mai.


### Caratterizzazione delle funzioni parzialmente calcolabili


Grazie all'operatore appena definito, possiamo infine caratterizzare le **funzioni parzialmente calcolabili** grazie a un teorema che, come vedremo, è molto importante per la teoria della calcolabilità.

> [!theorem] Caratterizzazione delle funzioni parzialmente calcolabili
> **Enunciato.** Una funzione è parzialmente calcolabile *se e solo se* si può ottenere dalle funzioni iniziali mediante un numero finito di **composizioni**, **ricorsioni primitive** (applicata solo a eventuali funzioni totali ottenute) e **minimalizzazioni illimitate**.


Questo teorema, che non dimostreremo, insieme alla tesi di **Church-Turing**[^13], che ci dice che ogni **funzione parzialmente calcolabile** è esprimibile mediante un **S-programma**, esprime un risultato teorico molto importante, ovvero che **ogni procedura algoritmica** può essere **ridotto alle funzioni iniziali** mediante questi **tre operatori**.
Per analizzare meglio questi programmi però, e farli valutare da delle funzioni, sarà necessario che anch'essi possano essere associati univocamente con dei numeri[^14].

---

[^1]: Il passaggio dall'approccio diretto a uno di carattere più generale per la valutazione della calcolabilità di una funzione è assimilabile al passaggio dal paradigma imperativo a quello funzionale.
[^2]: In notazione algebrica $f \circ g$ equivale a $f(g(x))$, dunque è l'operando sinistro a poter essere parziale, non essendo la composizione commutativa.
[^3]: In caso di dubbi controllare qui~*(ref: Funzione Sottrazione)*
[^4]: Si noti che le funzioni proiezioni sono un **insieme infinito** e non **una sola funzione**. Infatti ne esiste una $\forall (n,i)$ con $ n \in \mathbb{N}$ e $ i \in \{1,\cdots,n\}$.
[^5]: Per dimostrare che una funzione è **ricorsiva primitiva** è sufficiente dimostrare che è ottenuta da **funzioni ricorsive primitive**. Da ora in avanti non ci si ricondurrà più a funzioni iniziali per le dimostrazioni.
[^6]: Questo predicato è detto *rilevatore di zeri*, è applicato a un predicato può svolgere il ruolo della *negazione logica*
[^7]: Funzione *Sottrazione in Valore Assoluto*:~*(ref: Funzione Sottrazione Valore Assoluto Eq)*
[^8]: La funzione $f(x,y)=\abs{x-y}$ è definita e dimostrata come ricorsiva primitiva nell'esercizio~*(ref: Funzione Sottrazione Valore Assoluto Eq)*. Esercizi consigliati:~*(ref: Funzione Sottrazione Valore Assoluto Eq)*,~*(ref: Predicato Minore Uguale Eq)*
[^9]: Dimostrazione alternativa:~*(ref: Corollario al Teorema di Definizione per Casi AltDim)*. Esercizi consigliati:~*(ref: Funzione iterata n-esima di f Eq)*.
[^10]: È importante specificare nella definizione di minimalizzazione limitata i due casi possibili tramite il quantificatore esistenziale, poiché il **non esiste minimo dell'insieme vuoto**.
[^11]: Si noti che $P_n!+1=(1\cdot 2 \cdot \cdots \cdot P_i \cdot \cdots \cdot P_n)+1$, dunque $\forall i\in\{1,\cdots,n\}: P_i|P_n!$, e dunque si ha che $(P_n!+1)\mod (P_i)=1$.
[^12]: Questo limite superiore che imponiamo è molto più grande di quanto necessario, è dimostrabile che $P_{n+1}\leq2P_n$. Si è scelto questo limite superiore essendo più facile da mostrare.
[^13]: Enunciata nella definizione~*(ref: Tesi di Church-Turing Def)*
[^14]: Esercizi Consigliati:~*(ref: Funzione conta primi)*,~*(ref: Funzione floor di sqrt2 x)* e~*(ref: Massimalizzazione limitata Eq)*