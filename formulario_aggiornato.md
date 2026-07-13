<table><tr><td colspan="2">Calcolo combinatorio</td><td colspan="5"><eq>k\text{-ple ordinate senza ripetizione}: |A^{(k)}| = n(n-1)\cdots(n-k+1) \quad k\text{-ple con ripetizione}: |A^{(k)}| = n^k \quad \text{Permutazioni}: n! \quad \binom{n}{k} = \frac{n!}{k!(n-k)!} \quad |\mathcal{P}(A)| = 2^n</eq></td></tr>
<tr><td colspan="2">Probabilità totale in una PMF</td><td colspan="5"><eq>p_X(x) = \sum_{m=1}^{|M|} \mathbb{P}(E_m)p_{X|E_m}(x), \bigcup_{i=1}^{m} E_i = \Omega \wedge (E_i \cap E_j = \emptyset, \forall i \neq j \in \{1,..,m\})</eq></td></tr>
<tr><td colspan="2">Probabilità Condizionata / Legge di Bayes</td><td colspan="5"><eq>p_X(x)p_{Y|X}(y|x) = p_{X,Y}(x,y) = p_Y(y)p_{X|Y}(x|y) \quad \Rightarrow \quad p_{X|Y}(x|y) = \frac{p_{Y|X}(y|x)p_X(x)}{p_Y(y)}</eq></td></tr>
<tr><td colspan="2">Variabili indipendenti</td><td colspan="5"><eq>p_{Y|X}(y|x) = p_Y(y) \quad p_{X|Y}(x|y) = p_X(x) \quad f_{X,Y}(x,y) = f_X(x)f_Y(y) \Leftrightarrow F_{X,Y}(x,y)=F_X(x)F_Y(y)</eq></td></tr>
<tr><td colspan="2">Regola della Catena</td><td colspan="5"><eq>p_{X,Y,Z}(x,y,z) = p_X(x)p_{Y|X}(y|x)p_{Z|X,Y}(z|x,y) \quad \Rightarrow \quad p_{\boldsymbol{X}}(\boldsymbol{x}) = \prod_{i=1}^n p_{X_i|X_{i-1},\dots,X_1}(x_i|x_{i-1},\dots,x_1) \text{ (anche per pdf)}</eq></td></tr>
<tr><td colspan="2">Linearità della Media</td><td colspan="5"><eq>\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y] \quad \Rightarrow \quad \mathbb{E}\left[\sum_i a_i X_i\right] = \sum_i a_i \mathbb{E}[X_i]</eq></td></tr>
<tr><td colspan="2">Media Condizionata (1 var)</td><td colspan="5"><eq>\mathbb{E}[X] = \sum_{m=1}^{|M|} \mathbb{P}(E_m) \sum_{x \in \mathcal{X}} x\, p_{X|E_m}(x) = \sum_{m=1}^{|M|} \mathbb{P}(E_m)\mathbb{E}[X|E_m]</eq></td></tr>
<tr><td colspan="2">Media Condizionata (2 var) / Teorema della media condizionata</td><td colspan="5"><eq>\mathbb{E}[g(X,Y)] = \sum_{y \in \mathcal{Y}} p_Y(y) \sum_{x \in \mathcal{X}} g(x,y)p_{X|Y}(x|y) = \mathbb{E}\big[\mathbb{E}[g(X,Y)|Y]\big]</eq></td></tr>
<tr><td colspan="2">Media di funzioni</td><td colspan="5"><eq>\mathbb{E}[g(X)] = \sum_{x \in \mathcal{X}} g(x)p_X(x)</eq></td></tr>
<tr><td colspan="2">Quantità importanti (1 var)</td><td colspan="5"><eq>X_{rms}^2 = \mathbb{E}[X^2] = \sum_{x \in \mathcal{X}} x^2 p_X(x) \quad \sigma_X^2 = \mathbb{E}\left[(X - \mu_X)^2\right] = X_{rms}^2 - \mu_X^2</eq></td></tr>
<tr><td colspan="2">Quantità importanti (2 var)</td><td colspan="5"><eq>R_{X,Y} = \mathbb{E}[XY] \quad COV[X,Y] = \mathbb{E}[(X-\mu_X)(Y-\mu_Y)] = R_{X,Y}-\mu_X\mu_Y \quad COV(X,Y)=\rho_{X,Y}\sigma_X\sigma_Y,\ \rho\in[-1,1] \quad p_{X,Y}=p_Xp_Y \Rightarrow COV=0</eq></td></tr>
<tr><td colspan="2">Combinazione lineare (2 var)</td><td colspan="5"><eq>Z = aX+bY+c,\quad \sigma_Z^2 = a^2\sigma_X^2+b^2\sigma_Y^2+2ab\,COV(X,Y)</eq></td></tr>
<tr><td colspan="2">Disuguaglianza di Chebyshev</td><td colspan="5"><eq>X>0,\quad \mathbb{P}\{|X-\mu_X|\le k\sigma_X\} \ge 1-\frac{1}{k^2}</eq></td></tr>
<tr><td colspan="2">PMF/pdf Congiunta ⇒ marginali</td><td colspan="5"><eq>p_X(x) = \sum_{y\in\mathcal{Y}} p_{X,Y}(x,y) \qquad f_X(x) = \int_{\mathbb{R}} f_{X,Y}(x,y)\,dy</eq></td></tr>
<tr><td colspan="2">Funzione gen. Momenti $M_X(s)$</td><td colspan="5"><eq>M_X(s)=\mathbb{E}[e^{sX}] \quad M_X(0)=1 \quad \frac{d^r}{ds^r}M_X(s)\Big|_{s=0}=\mathbb{E}[X^r] \qquad \text{(Lévy) } M_{X_n}(s)\to M_X(s) \Rightarrow X_n\xrightarrow{d}X</eq></td></tr>
<tr><td colspan="2">Nome</td><td colspan="2">PMF</td><td colspan="2"><eq>\mu \quad \sigma^2</eq></td><td>Proprietà</td></tr>
<tr><td colspan="2">Uniforme discreta <eq>X=\{0,\dots,M-1\}</eq></td><td colspan="2"><eq>p(k)=\frac{1}{M}</eq></td><td colspan="2"><eq>\mu=\frac{M-1}{2} \quad \sigma^2=\frac{M^2-1}{12}</eq></td><td></td></tr>
<tr><td colspan="2">Bernoulli <eq>X=\{0,1\}</eq></td><td colspan="2"><eq>p(k)=\begin{cases}1-p, & k=0\\ p, & k=1\end{cases}</eq></td><td colspan="2"><eq>\mu=p \quad \sigma^2=p(1-p)</eq></td><td><eq>I=\frac{1}{p(1-p)},\ I_n=\frac{n}{p(1-p)}</eq></td></tr>
<tr><td colspan="2">Binomiale <eq>X\sim B(n,p)</eq></td><td colspan="2"><eq>p(k)=\binom{n}{k}(1-p)^{n-k}p^k</eq></td><td colspan="2"><eq>\mu=np \quad \sigma^2=np(1-p)</eq></td><td></td></tr>
<tr><td colspan="2">Poisson <eq>X\sim P(\lambda)</eq></td><td colspan="2"><eq>p(k)=\frac{\lambda^k e^{-\lambda}}{k!},\ \lambda>0</eq></td><td colspan="2"><eq>\mu=\lambda \quad \sigma^2=\lambda</eq></td><td></td></tr>
<tr><td colspan="2">Nome</td><td colspan="2">PDF</td><td colspan="2"><eq>\mu \quad \sigma^2</eq></td><td>CDF</td></tr>
<tr><td colspan="2">Uniforme continua <eq>X\sim U(a,b)</eq></td><td colspan="2"><eq>f(x)=\frac{1}{b-a},\ a\le x\le b</eq></td><td colspan="2"><eq>\mu=\frac{a+b}{2} \quad \sigma^2=\frac{(b-a)^2}{12}</eq></td><td><eq>F(x)=\frac{x-a}{b-a},\ a\le x\le b</eq></td></tr>
<tr><td colspan="2">Esponenziale <eq>X\sim \mathcal{E}(\lambda)</eq></td><td colspan="2"><eq>f(x)=\lambda e^{-\lambda x}u(x)</eq></td><td colspan="2"><eq>\mu=\frac{1}{\lambda} \quad \sigma^2=\frac{1}{\lambda^2}</eq></td><td><eq>F(x)=(1-e^{-\lambda x})u(x)</eq></td></tr>
<tr><td colspan="2">Laplaciana <eq>X\sim \mathcal{L}(\lambda)</eq></td><td colspan="2"><eq>f(x)=\frac{\lambda}{2}e^{-\lambda|x|}</eq></td><td colspan="2"><eq>\mu=0 \quad \sigma^2=\frac{2}{\lambda^2}</eq></td><td><eq>F(x)=\frac12e^{\lambda x}\,(x\le0),\ 1-\frac12e^{-\lambda x}\,(x\ge0)</eq></td></tr>
<tr><td colspan="2">Cauchy <eq>X\sim \mathcal{C}(a,b)</eq></td><td colspan="2"><eq>f(x)=\frac{1}{\pi b}\frac{1}{1+\left(\frac{x-a}{b}\right)^2}</eq></td><td colspan="2"><eq>\mu,\sigma^2 \text{ non definite},\ Sym_{[-H,H]}=a</eq></td><td><eq>F(x)=\frac12+\frac1\pi\arctan\left(\frac{x-a}{b}\right)</eq></td></tr>
<tr><td>Gaussiana</td><td colspan="2"><eq>f_X(x)=\frac{1}{\sqrt{2\pi\sigma_X^2}}e^{-\frac{(x-\mu_X)^2}{2\sigma_X^2}}</eq></td><td><eq>X=\sigma_XX_0+\mu_X,\ X_0\sim N(0,1)</eq></td><td colspan="2"><eq>F_X(x)=1-Q(x),\ Q(x)=\mathbb{P}(X_0\ge x)</eq></td><td><eq>\mathbb{P}(X\ge x)=Q\!\left(\frac{x-\mu_X}{\sigma_X}\right),\ Q(-x)=1-Q(x),\ Q(x)\underset{x\to\infty}{\sim}\frac{e^{-x^2/2}}{x\sqrt{2\pi}}</eq></td></tr>
<tr><td colspan="4"><eq>Y=g(X),\ g</eq> continua e iniettiva (invertibile)</td><td colspan="2">PDF</td><td>CDF</td></tr>
<tr><td colspan="4">crescente</td><td colspan="2"><eq>f_Y(y)=\frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}</eq></td><td><eq>F_Y(y)=F_X(g^{-1}(y))</eq></td></tr>
<tr><td colspan="4">decrescente</td><td colspan="2"><eq>f_Y(y)=\frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}</eq></td><td><eq>F_Y(y)=1-F_X(g^{-1}(y))</eq></td></tr>
<tr><td colspan="4">non invertibile (somma su tutte le preimmagini <eq>x_i(y)</eq>)</td><td colspan="2"><eq>f_Y(y)=\sum_i \frac{f_X(x_i(y))}{|g'(x_i(y))|}</eq></td><td>—</td></tr>
</table>

Matrice di covarianza $\mathbf{K_X}$: $\mathbf{K_X} := \mathbb{E}\left[(\mathbf{X}-\boldsymbol{\mu_X})(\mathbf{X}-\boldsymbol{\mu_X})^T\right] = \begin{pmatrix}\sigma_1^2 & \sigma_1\sigma_2\rho_{1,2}\\ \sigma_1\sigma_2\rho_{1,2} & \sigma_2^2\end{pmatrix}$ — caso generale $n$-dim: $\mathbf{K_X}=\mathbb{E}[(\mathbf{X}-\boldsymbol{\mu_X})(\mathbf{X}-\boldsymbol{\mu_X})^T]$, matrice $n\times n$ simmetrica, con $\sigma_{X_i}^2$ in diagonale e $COV(X_i,X_j)$ fuori diagonale.

Proprietà della matrice di covarianza $\mathbf{K_X}$: $|\mathbf{K_X}|=\sigma_1^2\sigma_2^2(1-\rho_{1,2}^2)\ge0$. Se $\rho_{1,2}\neq\pm1$: $\mathbf{K_X}^{-1}=\dfrac{1}{\sigma_1^2\sigma_2^2(1-\rho_{1,2}^2)}\begin{pmatrix}\sigma_2^2 & -\sigma_1\sigma_2\rho_{1,2}\\ -\sigma_1\sigma_2\rho_{1,2} & \sigma_1^2\end{pmatrix}$. $\mathbf{z}^T\mathbf{K_X}^{-1}\mathbf{z}\ge0\ \forall \mathbf{z}$ (definita non negativa).

pdf congiunta Gaussiana: $f_{\mathbf{X}}(\mathbf{x})=\dfrac{1}{2\pi|\mathbf{K_X}|^{1/2}}\exp\left[-\frac12(\mathbf{x}-\boldsymbol{\mu_X})^T\mathbf{K_X}^{-1}(\mathbf{x}-\boldsymbol{\mu_X})\right]$ — caso $M$-dim: $f(\mathbf{x})=\dfrac{1}{\sqrt{(2\pi)^M|\Sigma|}}\exp\left(-\frac12(\mathbf{x}-\boldsymbol\mu)^T\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu)\right)$.

Chiusura Gaussiana per trasformazioni lineari: $\mathbf{X}\sim N(\boldsymbol\mu_X,\mathbf{K_X}) \Rightarrow \mathbf{Z}=\mathbf{A}\mathbf{X}+\mathbf{b}\sim N(\mathbf{A}\boldsymbol\mu_X+\mathbf{b},\ \mathbf{A}\mathbf{K_X}\mathbf{A}^T)$. Incorrelazione $\Leftrightarrow$ indipendenza solo per variabili congiuntamente Gaussiane. Incorrelazione (matrice di covarianza diagonale) $\Rightarrow$ indipendenza statistica per vettori/processi Gaussiani.

<table><tr><td>Derivata del Prodotto</td><td colspan="3"><eq>\frac{d}{dx}[f(x)g(x)]=f'(x)g(x)+f(x)g'(x)</eq></td></tr>
<tr><td>Derivata del Rapporto</td><td colspan="3"><eq>\frac{d}{dx}\frac{f(x)}{g(x)}=\frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2}</eq></td></tr>
<tr><td>Regola della Catena</td><td colspan="3"><eq>\frac{d}{dx}f[g(x)]=f'[g(x)]\cdot g'(x)</eq></td></tr>
<tr><td>Integrazione generale</td><td colspan="3"><eq>\int f[g(x)]\,g'(x)\,dx=F[g(x)]+c</eq></td></tr>
<tr><td>Integrazione per parti</td><td colspan="3"><eq>\int f(x)g(x)\,dx=F(x)g(x)-\int F(x)g'(x)\,dx</eq></td></tr>
<tr><td>Funzione Gamma</td><td colspan="3"><eq>\int_0^{+\infty}t^{x-1}e^{-at}dt=a^{-x}\Gamma(x),\quad \Gamma(x):=\int_0^{+\infty}t^{x-1}e^{-t}dt,\quad \Gamma(n)=(n-1)!,\ n\in\mathbb{N}</eq></td></tr>
<tr><td>Somme dei primi $n$ numeri</td><td colspan="3"><eq>\sum_{i=1}^n i=\frac{n(n+1)}{2} \quad \sum_{i=1}^n i^2=\frac{n(n+1)(2n+1)}{6} \quad \sum_{i=1}^n i^3=\left(\frac{n(n+1)}{2}\right)^2</eq></td></tr>
<tr><td>Serie geometrica</td><td colspan="3"><eq>\sum_{i\in\mathbb{N}_0}p^i=\frac{1}{1-p}\ (p<1) \quad \sum_{i=0}^{n-1}p^i=\frac{1-p^n}{1-p} \quad \sum_{n=1}^{\infty}np^{n-1}=\frac{1}{(1-p)^2}</eq></td></tr>
<tr><td colspan="2">Funzione</td><td>Derivata</td><td>Integrale</td></tr>
<tr><td colspan="2"><eq>x^n</eq></td><td><eq>nx^{n-1}</eq></td><td><eq>\frac{x^{n+1}}{n+1}+c,\ n\neq-1</eq></td></tr>
<tr><td colspan="2"><eq>\frac{1}{x}</eq></td><td><eq>-x^{-2}</eq></td><td><eq>\log|x|+c</eq></td></tr>
<tr><td colspan="2"><eq>e^x</eq></td><td><eq>e^x</eq></td><td><eq>e^x+c</eq></td></tr>
<tr><td colspan="2"><eq>a^x</eq></td><td><eq>a^x\log(a)</eq></td><td><eq>a^x\log_a(e)+c</eq></td></tr>
<tr><td colspan="2"><eq>\cos(x)</eq></td><td><eq>-\sin(x)</eq></td><td><eq>\sin(x)+c</eq></td></tr>
<tr><td colspan="2"><eq>\sin(x)</eq></td><td><eq>\cos(x)</eq></td><td><eq>-\cos(x)+c</eq></td></tr>
<tr><td colspan="2"><eq>\frac{1}{1+x^2}</eq></td><td><eq>-\frac{2x}{(1-x^2)^2}</eq></td><td><eq>\arctan(x)+c</eq></td></tr>
</table>

![pdf e CDF di Esponenziale, Laplaciana e Cauchy](assets/distribuzioni_continue_pdf_cdf.png)

<table><tr><td colspan="2">Media e Autocorrelazione</td><td colspan="5"><eq>\mu(t)=\mathbb{E}[X(t)] \qquad R(t_1,t_2)=\mathbb{E}[X(t_1)X(t_2)]</eq></td></tr>
<tr><td colspan="2">Stazionarietà stretta (ordine M)</td><td colspan="5"><eq>f_{X(n_1),\dots,X(n_M)}(x_1,\dots,x_M)=f_{X(n_1+h),\dots,X(n_M+h)}(x_1,\dots,x_M)\ \forall h</eq></td></tr>
<tr><td colspan="2">Stazionarietà in Senso Lato (SSL)</td><td colspan="5"><eq>\mu_X(n)=\mu_X\ \forall n \qquad R_X(n_1,n_2)=\mathbb{E}[X(n_1)X(n_2)]=R_X(n_2-n_1)</eq></td></tr>
<tr><td colspan="2">Matrice di covarianza (processo SSL)</td><td colspan="5"><eq>\mathbf{C_X}=\sigma_X^2\begin{pmatrix}1 & \rho_{1,2} & \cdots\\ \rho_{1,2} & 1 & \cdots\\ \vdots & \vdots & \ddots\end{pmatrix},\ \rho_{i,j}=\frac{COV(X_i,X_j)}{\sigma_X^2}\ \text{(Toeplitz se passo costante)}</eq></td></tr>
<tr><td colspan="2">Processo Gaussiano</td><td colspan="5"><eq>\text{ogni vettore campionato è Gaussiano} \qquad \text{SSL} \Rightarrow \text{stazionario in senso stretto}</eq></td></tr>
<tr><td colspan="2">Tipi di convergenza (dalla più debole alla più forte)</td><td colspan="5"><eq>\text{distribuzione } (\lim F_n(x)=F(x)) \prec \text{probabilità} \prec \text{media quadratica} \prec \text{quasi certa}</eq></td></tr>
</table>

<table><tr><td colspan="2">Bias/unbias</td><td colspan="5"><eq>\hat{\Theta} \text{ unbiased/corretto} \iff \mathbb{E}[\hat{\Theta}(X^n)|\Theta=\theta]=\theta \quad \left(b_n(\theta)=\mathbb{E}[\hat{\Theta}(X^n)]-\theta\right)</eq></td></tr>
<tr><td colspan="2">unbias/corretto asintotico</td><td colspan="5"><eq>\lim_{n\to\infty}\mathbb{E}[\hat{\Theta}(X^n)|\Theta=\theta]=\theta</eq></td></tr>
<tr><td colspan="2">Consistenza in probabilità</td><td colspan="5"><eq>\lim_{n\to\infty}\mathbb{P}\{|\hat{\Theta}(X^n)-\Theta|>\epsilon\}=0,\ \forall\epsilon>0</eq></td></tr>
<tr><td colspan="2">Consistenza in media quadratica</td><td colspan="5"><eq>\lim_{n\to\infty}\overline{e}^2=0,\quad \overline{e}^2=\mathbb{E}[(\hat{\Theta}(X^n)-\Theta)^2]\ \left(=Var(\hat{\Theta}(X^n))\text{ se unbiased}\right)</eq></td></tr>
<tr><td colspan="2">Consistenza forte</td><td colspan="5"><eq>\hat{\Theta}(X^n)\to\Theta \text{ quasi certamente}</eq></td></tr>
<tr><td colspan="2">Informazione di Fisher</td><td colspan="5"><eq>I_n=\mathbb{E}\left[\left(\frac{d\log f_{X^n}(x^n;\theta)}{d\theta}\right)^2\right]=-\mathbb{E}\left[\frac{d^2\log f_{X^n}(x^n;\theta)}{d^2\theta}\right]</eq></td></tr>
<tr><td colspan="2">Limite di Cramér-Rao</td><td colspan="5"><eq>Var[\hat{\Theta}(X^n)]\ge\frac{[1+b_n'(\theta)]^2}{I_n(\theta)} \ \xrightarrow{b_n=0}\ Var[\hat{\Theta}(X^n)]\ge\frac{1}{I_n(\theta)}\ \text{(efficiente se '=')}</eq></td></tr>
</table>

<table><tr><td>Tipo inf</td><td colspan="2">Cose note</td><td colspan="2">Regola decisione/Stimatore</td></tr>
<tr><td>Decisione Bayesiana</td><td colspan="2"><eq>\mathcal{R}=\sum_{i=1}^M\sum_{j=1}^M C_{i,j}\,\mathbb{P}\{D(X^n)=i,H=H_j\}</eq></td><td colspan="2"><eq>D(x^n)=i \Leftrightarrow \mathbb{P}\{X^n=x^n,H_i\}>\mathbb{P}\{X^n=x^n,H_j\}\ \forall j\neq i</eq> — 2 ipotesi: <eq>L(x^n)=\frac{\mathbb{P}\{X^n=x^n|H_1\}}{\mathbb{P}\{X^n=x^n|H_2\}}\underset{H_2}{\overset{H_1}{\gtrless}}\frac{\mathbb{P}\{H_2\}}{\mathbb{P}\{H_1\}}</eq></td></tr>
<tr><td>Neyman-Pearson</td><td colspan="2"><eq>\alpha=\mathbb{P}\{L(x^n)>\eta|H_0\} \quad 1-\beta=\mathbb{P}\{L(x^n)>\eta|H_1\}</eq></td><td colspan="2"><eq>L(x^n)=\frac{\mathbb{P}\{X^n=x^n|H_1\}}{\mathbb{P}\{X^n=x^n|H_0\}}\underset{H_0}{\overset{H_1}{\gtrless}}\eta,\ \eta:\ \mathbb{P}\{L(X^n)>\eta|H_0\}=\alpha</eq></td></tr>
<tr><td>Stima Bayesiana parametro continuo</td><td colspan="2"><eq>f_{\Theta|X^n}(\theta|x^n)=\frac{f_\Theta(\theta)p_{X^n|\Theta}(x^n|\theta)}{p_{X^n}(x^n)},\ p_{X^n}(x^n)=\int f_\Theta(\theta)p_{X^n|\Theta}(x^n|\theta)d\theta</eq> <eq>\mathcal{R}=\mathbb{E}[C(\hat\Theta(X^n)-\Theta)]=\mathbb{E}_{X^n}\big[\mathbb{E}[C(\hat\Theta(X^n)-\Theta)|X^n]\big]</eq></td><td colspan="2"><eq>\hat\theta_{opt}(x^n)=\arg\min\int C(\hat\theta(x^n)-\theta)f_{\Theta|X^n}(\theta|x^n)d\theta</eq> <eq>C(x)=x^2\Rightarrow\hat\theta_{mmse}(x^n)=\mathbb{E}[\Theta|X^n=x^n]</eq> <eq>C(x)=\Pi(x/\epsilon)\Rightarrow\hat\theta_{map}(x^n)=\arg\max f_{\Theta|X^n}(\theta|x^n)</eq></td></tr>
<tr><td>Non Bayes (ML)</td><td colspan="2">—</td><td colspan="2"><eq>\hat\theta_{ML}(x^n)=\arg\max\log\big(f_{X^n}(x^n;\theta)\big) \quad \nabla_{\boldsymbol\theta}\Lambda(\boldsymbol\theta;x^n)\big|_{\boldsymbol\theta=\hat{\boldsymbol\theta}(x^n)}=0</eq></td></tr>
<tr><td>Bernoulli (stima frequenza)</td><td colspan="2"><eq>w(x^n)=\text{peso di Hamming (numero di 1)}</eq></td><td colspan="2"><eq>\hat\beta_{ML}(x^n)=\frac{w(x^n)}{n} \quad I_n(\beta)=\frac{n}{\beta(1-\beta)} \quad CRB=\frac{\beta(1-\beta)}{n}\ \text{(ML efficiente)}</eq></td></tr>
</table>

<table><tr><td colspan="2">Estimatore LMMSE (lineare)</td><td colspan="5"><eq>\hat\Theta(X^n)=\mathbf{a}^TX^n+b,\ \mathbf{a}_{LMMSE}=\mathbf{M}^{-1}\mathbf{s},\ b_{LMMSE}=\mathbb{E}[\Theta]-\mathbf{a}^T\mathbb{E}[X^n]\ \left(\mathbf{M}=COV(X^n),\ \mathbf{s}=\mathbb{E}[(X^n-\mathbb{E}[X^n])(\Theta-\mathbb{E}[\Theta])]\right)</eq></td></tr>
<tr><td colspan="2">Algoritmo del gradiente</td><td colspan="5"><eq>\mathbf{a}^{(n+1)}=\mathbf{a}^{(n)}-\gamma(\mathbf{M}\mathbf{a}^{(n)}-\mathbf{s}),\quad 0<\gamma<\frac{2}{\lambda_{MAX}}</eq></td></tr>
<tr><td colspan="2">Stimatore ai Minimi Quadrati (LS)</td><td colspan="5"><eq>\mathbf{a}_{LS}=(\mathbf{X}\mathbf{X}^T)^{-1}\mathbf{X}\mathbf{y}\quad \text{(richiede } \mathbf{X}\mathbf{X}^T \text{ invertibile, } p\ge n\text{)}</eq></td></tr>
<tr><td colspan="2">Formula di Sherman-Morrison</td><td colspan="5"><eq>(\mathbf{R}+\mathbf{u}\mathbf{v}^T)^{-1}=\mathbf{R}^{-1}-\frac{\mathbf{R}^{-1}\mathbf{u}\mathbf{v}^T\mathbf{R}^{-1}}{1+\mathbf{u}^T\mathbf{R}^{-1}\mathbf{v}}</eq></td></tr>
<tr><td colspan="2">LS esponenzialmente pesato (adattivo)</td><td colspan="5"><eq>\mathbf{a}=\left[\sum_i w^{p-i}\mathbf{x}^n(i)\mathbf{x}^{nT}(i)\right]^{-1}\sum_i w^{p-i}\mathbf{x}^n(i)\theta(i),\quad w<1 \ \text{(ricorsivo via Sherman-Morrison)}</eq></td></tr>
<tr><td colspan="2">LMS generale (con intercetta, dati centrati)</td><td colspan="5"><eq>\mathbf{a}_{LMS}=(\mathbf{X}_0\mathbf{X}_0^T)^{-1}\mathbf{X}_0\mathbf{y}_0,\quad b_{LMS}=\overline\theta-\frac1p\mathbf{1}_p^T\mathbf{X}^T\mathbf{a}_{LMS},\quad \mathbf{X}_0=\mathbf{X}-\overline{\mathbf{x}}\mathbf{1}_p^T</eq></td></tr>
</table>

NOTA: Se in uno stimatore Bayesiano $C(\cdot)\ge0$ è convessa e pari, e $f_{\Theta|X^n}(\theta|x^n)$ è simmetrica rispetto a $\mathbb{E}[\Theta|X^n=x^n]$, allora tutti gli stimatori che ottimizzano $C(\cdot)$ coincidono: $\hat\Theta_{mmse}(X^n)=\hat\Theta_{map}(X^n)$.

NOTA: l'applicazione di una funzione monotona crescente (es. il logaritmo naturale) a entrambi i lati di un test/disequazione non ne altera il verso né l'ottimalità (consente il passaggio a log-verosimiglianza).
