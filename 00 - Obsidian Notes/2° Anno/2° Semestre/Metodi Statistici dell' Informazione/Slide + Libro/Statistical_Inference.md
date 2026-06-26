## Elementi di Statistica inferenziale

Marco Lops 

lops@unina.it 

https://docenti.unina.it/marco.lops 

## Some Definitions

Assume we have a sample of size n, say $\pmb { x } \in \mathbb { R } ^ { n }$ 

Assume that this sample is the result of a random experiment, which means that re-sampling would lead to a diferent set of results, say $\pmb { x } ^ { \prime } \in \mathbb { R } ^ { n }$ ; 

Statistical inference is the process of using data analysis to infer properties of an underlying distribution of probability, i.e. defining a law which any sample - randomly drawn . should abide with; 

Inferential statistics can be contrasted with descriptive statistics. Descriptive statistics is solely concerned with properties of the observed data, and it does not rest on the assumption that the data come from a larger population 

Basic goals of Statistical inference are Hypothesis Testing and Paramete Estimation. 

## An example: the sample mean

Assume we have a data set $\pmb { x } ^ { n } \in \mathcal { X } ^ { n } \subseteq \mathbb { R } ^ { n }$ ; 

We know that the sample mean is defined as 

$$
\overline {{x}} _ {n} = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i}
$$

The law of large numbers tells us that ${ \overline { { X } } } _ { n } \to \mathbb { E } [ X ]$ (the type of convergence depending on the underlying statistical law), in the sense that, denoting $X ^ { n }$ a random sample drawn from the population, we have 

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} \to \mathbb {E} [ X ]
$$

Weak convergence (i.e., convergence in probability) tells us that the frequency of samples whose sample mean departs significantly from $\mathbb { E } [ X ]$ is as small as we want; 

Strong convergence states that in the limit the probability of departing from $\mathbb { E } [ X ]$  is zero; 

Mean-Square convergence states that 

$$
\lim _ {n} \mathbb {E} \left[ \left(\overline {{X}} _ {n} - \mathbb {E} [ X ]\right) ^ {2} \right] = 0
$$

## The Sample mean - cont’d

Assume that $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ , with $\mathcal { X } = ( a _ { 1 } , \dotsc , a _ { M } )$ discrete and finite; 

we know that 

$$
\overline {{x}} _ {n} = \sum_ {i = 1} ^ {M} a _ {i} f _ {n} (a _ {i})
$$

where $f _ { n } ( a _ { i } )$ is the fraction of values of the sample yielding $a _ { j }$ ; 

We know that, if $\boldsymbol { x } \in \mathcal { X }$ is a random variable with pmf $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$ , then: 

$$
\mathbb {E} [ X ] = \sum_ {i = 1} ^ {M} a _ {i} p _ {X} (a _ {i})
$$

As a consequence, we have 

$$
| \overline {{x}} _ {n} - \mathbb {E} [ X ] | \leq \sum_ {i = 1} ^ {M} | a _ {i} | | f _ {n} (a _ {i}) - p _ {X} (a _ {i}) |
$$

Notice that if we can claim that $f _ { n } ( a _ { i } ) \to p \chi ( a _ { i } )$ (in some sense), then we may infer that $\pmb { x } ^ { n }$ is a sample from a population whose elements are drawn from a random vector $X ^ { n }$ with marginal density $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$ 

## The Empirical distribution

Assume that $\pmb { x } ^ { n }$ is drawn from $X ^ { n }$ , a set of n iid random variables with unknown marginal $\{ p _ { X } ( a _ { i } ) \} _ { i = 1 } ^ { M }$ • 

The frequency of occurrence of the event $X _ { k } = a _ { i }$ is itself random. If $N _ { j }$ is the number of times $X _ { k } = a _ { i }$ in our n−dimensional sample, we have: 

$$
\operatorname * {P r} \left\{N _ {i} = k \right\} = \binom{n}{k} p _ {X} (a _ {i}) ^ {k} \left[ 1 - p _ {X} (a _ {i}) \right] ^ {n - k}
$$

Since 

$$
\mathbb {E} \left[ \frac {N _ {i}}{n} \right] = p _ {X} (a _ {i}), \quad \text { var } \left[ \frac {N _ {i}}{n} \right] = \frac {p _ {X} (a _ {i}) (1 - p _ {X} (a _ {i}))}{n}
$$

we have that $\begin{array} { r } { \frac { N _ { i } } { n }  p _ { X } ( a _ { i } ) } \end{array}$ in mean square, i.e.: 

$$
\lim _ {n \rightarrow \infty} \mathbb {E} \left[\left(\frac {N _ {i}}{n} - p _ {X} (a _ {i})\right) ^ {2} \right] = 0
$$

## Almost sure convergence

Assume that $\{ q ( a _ { i } ) \}$ is any other pmf on $\mathcal { X }$ difering from the true distribution $p _ { X } { \left( a _ { i } \right) }$ in at least two elements. We have: 

$$
\operatorname * {P r} \left\{N _ {i} = n q (a _ {i}) \right\} = \binom{n}{n q (a _ {i})} p _ {X} (a _ {i}) ^ {n q (a _ {i})} \left[ 1 - p _ {X} (a _ {i}) \right] ^ {n (1 - q (a _ {i}))}
$$

Using the bound 

$$
\sqrt {\frac {n}{8 k (n - k)}} \leq \binom{n}{k} 2 ^ {- n H \left(\frac {k}{n}\right)} \leq \sqrt {\frac {n}{\pi k (n - k)}}
$$

we have, upon setting $k = n q ( a _ { i } )$ 

$$
\begin{array}{c} \sqrt {\frac {1}{8 n q (a _ {i}) (1 - q (a _ {i}))}} \leq \binom{n}{n q (a _ {i})} 2 ^ {- n \left[ q (a _ {i}) \log \frac {1}{q (a _ {i})} + (1 - q (a _ {i})) \log \frac {1}{1 - q (a _ {i})} \right]} \\ \leq \sqrt {\frac {1}{\pi n q (a _ {i}) (1 - q (a _ {i}))}} \end{array}
$$

we have, for increasingly large n: 

$$
\binom{n}{n q (a _ {i})} \sim 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))}
$$

## Almost sure convergence - cont’d

Consider now a value $a _ { j }$ for which $q ( a _ { i } ) \neq p _ { X } ( a _ { i } )$ 

When n grows large we have: 

$$
\begin{array}{r l} \operatorname * {P r} \big \{N _ {i} = n q (a _ {i}) \big \} & \sim 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} p _ {X} (a _ {i}) ^ {n q (a _ {i})} \left[ 1 - p _ {X} (a _ {i}) \right] ^ {n (1 - q (a _ {i}))} \\ & = 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} 2 ^ {n [ q (a _ {i}) \log p _ {X} (a _ {i}) + (1 - q (a _ {i})) \log (1 - p _ {X} (a _ {i})) ]} \\ & = 2 ^ {n \left[ q (a _ {i}) \log \frac {p _ {X} (a _ {i})}{q (a _ {i})} + (1 - q (a _ {i})) \log \frac {1 - p _ {X} (a _ {i})}{1 - q (a _ {i})} \right]} = 2 ^ {- n D _ {i}} \end{array}
$$

with 

$$
D _ {i} = q (a _ {i}) \log \frac {q (a _ {i})}{p _ {X} (a _ {i})} + [ 1 - q (a _ {i}) ] \log \frac {1 - q (a _ {i})}{1 - p _ {X} (a _ {i})} > 0
$$

We thus conclude that the probability that the frequency of occurrence does not equal the true probability goes to zero exponentially with n. 

This implies that $f _ { n } ( a _ { i } ) \to p \chi ( a _ { i } )$ almost surely. 

## Comments

Assume we have a sample $\pmb { x } ^ { n } \in \mathcal { X } ^ { n } , \mathcal { X } = \{ a _ { 1 } , . . . , a _ { M } \}$ drawn from a random vector $X ^ { n }$ of unknown pmf; 

If we compute the frequencies of occurence: 

$$
f _ {n} (a _ {i}) = \frac {\# \text {   of   elements   equal   to   } a _ {i}}{n}, \qquad i = 1, \ldots , M
$$

we have: 

$$
\operatorname * {P r} \left\{\lim _ {n \rightarrow \infty} \frac {N _ {i}}{n} = \lim _ {n \rightarrow \infty} f _ {n} (a _ {i}) \right\} = 1
$$

This implies that any other sample, $\pmb { y } ^ { n }$ say, drawn from the same population wil exhibit, for $n  \infty$ , the same statistical behavior. 

Needless to say, we’ll have that for any function $f ( \cdot )$ of the data 

$$
\operatorname * {P r} \left\{\lim _ {n \rightarrow \infty} f (\boldsymbol {X} ^ {n}) = \lim _ {n \rightarrow \infty} f (\boldsymbol {x} ^ {n}) \right\} = 1
$$

Thus, the sample mean converges with probability one to the statistical average of the population. 

This property is also referred to in inferential statistics as strong consistency. 

## Inferential Statistics

The main idea is that, once we observe a suficiently ample sample of a given data population, we may infer a number of characteristics any other sample should abide to; 

Some prior knowledge as to the statistics of the population the sample is drawn from may be a priori known; 

For example, we might assume that the sample is drawn from a population whose distribution is known up to a set of parameters; 

To begin with, let us assume that the sample si known to be drawn from a family of distributions, indexed by a parameter θ, which is to be estimated; 

Question: How do we process the available dataset in order to infer the value of the parameter? 

## Bayesian Setting: Decision rule

Assume that we have a dataset $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ which is a realization of a random vector $X ^ { n }$ ; 

Assume that - based on the state of the nature - the data may come from any of M diferent probability laws. 

We thus have a set of M diferent, mutually exclusive hypotheses $\{ H _ { i } \} _ { i = 1 } ^ { M }$ , each defining a diferent conditional law for the data set, i.e.: 

$$
p _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {x} ^ {n} \mid H _ {i}\right), \quad i = 1, \dots , M
$$

Assume that the random vector $X ^ { n }$ is drawn from a distribution family with pmf $p _ { X ^ { n } | \Theta } ( { \pmb x } ^ { n } | \theta )$ , where the value of $\theta$ is unknown; 

Assume also that the prior probabilities - $\{ p ( H _ { i } ) \} _ { i = 1 } ^ { M }$ - of these states of the nature are assigned; 

A Decision rule is a map: 

$$
D: \mathbf {x} ^ {n} \in \mathcal {X} ^ {n} \Longrightarrow D (\mathbf {x} ^ {n}) \in \{1, \dots , M \}
$$

which allows us to decide which one of the possible states of the nature is the one actually in force. 

## Bayes costs

Assume that we define the following $M \times M$ cost matrix 

$$
\boldsymbol {C} = \left[ \begin{array}{c c c c} C _ {1, 1} & C _ {1, 2} & \ldots & C _ {1, M} \\ \ldots & \ldots & \ldots & \ldots \\ C _ {M, 1} & C _ {M, 2} & \ldots & C _ {M, M} \end{array} \right]
$$

where $C _ { i , j }$ is the cost associated to the event we make decision $D ( \pmb { x } ^ { n } ) = i$ and the state of the nature is $H _ { j }$ 

We define the average Bayesian risk as: 

$$
\mathcal {R} = \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {M} C _ {i, j} \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = i, H = H _ {j} \right\}
$$

Given a cost matrix C, an optimal decision rule is a map $D ( \pmb { x } ^ { n } )$ which minimizes the Bayes risk; 

Notice that, if $C _ { i , i } = 0 ~ i = 1 , . . .$ , M and $C _ { i , j } = 1 \forall i \neq j$ , then 

$$
\mathcal {R} = \sum_ {i = 1} ^ {M} \sum_ {j \neq} ^ {M} \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = i, H = H _ {j} \right\} = \mathbb {P} (e)
$$

namely the average Bayes risk coincides with the probability of committing a classification error. 

## Binary Classification problem

Assume for the moment that $M = 2$ , that $C _ { 1 , 1 } = C _ { 2 , 2 } = 0$ and $C _ { 1 , 2 } = C _ { 2 , 1 } = 1$ so that 

$$
\mathcal {R} = \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 2, H _ {1} \right\} + \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 1, H _ {2} \right\} = \mathbb {P} (e)
$$

Designing a decision rule implies determining a partition of $\mathcal { X } ^ { n }$ in two subsets, $\Omega _ { 1 }$ and $\Omega _ { 2 }$ , such that 

$$
D (\boldsymbol {x} ^ {n}) = \left\{ \begin{array}{l l} 1 & \text { if } \boldsymbol {x} ^ {n} \in \Omega_ {1} \\ 2 & \text { if } \boldsymbol {x} ^ {n} \in \Omega_ {2} \end{array} \right.
$$

The corresponding error probability is thus written as: 

$$
\mathbb {P} (e) = \mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {1}, H _ {2} \right\} + \mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {2}, H _ {1} \right\}
$$

We want to determine the optimum (i.e., with minimum error probability) decision law for this binary classification problem. 

## Binary classification: discrete data laws

Assume that the observations $X ^ { n }$ are a discrete random vector with given conditional pmf’s $p { \pmb X } ^ { m } \big ( { \pmb x } ^ { n } | H _ { i } \big )$ ; 

We obviously have $\begin{array} { r } { \mathbb { P } \left\{ \pmb { X } ^ { n } \in \Omega _ { i } , H _ { j } \right\} = \pmb { 1 } - \sum _ { \pmb { x } ^ { n } \in \Omega _ { i } } p ( H _ { i } ) \mathbb { P } \left\{ \pmb { X } ^ { n } = \pmb { x } ^ { n } | H _ { i } \right\} } \end{array}$ whereby the error probability is written as 

$$
\mathbb {P} (e) = 1 - \left[ \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {1}} p \left(H _ {1}\right) \mathbb {P} \left\{\boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \mid H _ {1} \right\} + \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {2}} p \left(H _ {2}\right) \mathbb {P} \left\{\boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \mid H _ {2} \right\} \right]
$$

which is minumum when the quantity in brackets is maximum. 

We thus obtain the following optimum decision rule: 

$$
\boldsymbol {x} ^ {n} \in \Omega_ {i} \text {   iff   } p _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) P (H _ {1}) > p _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2}) P (H _ {2})
$$

or equivalently 

$$
L (\boldsymbol {x} ^ {n}) = \frac {p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {1})}{p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {2})} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} \frac {P (H _ {2})}{P (H _ {1})} = \eta
$$

The quantity $L ( \pmb { x } ^ { n } )$ on the LHS is called likelihood ratio between the two alternative hypotheses. 

## Some comments

The previous decision rule is also known as Maximum A-posteriori Probability (MAP) decision rule, in that, by the Bayes’ law: 

$$
\mathbb {P} \left\{H = H _ {i} | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right\} = \frac {\mathbb {P} \left\{\boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \mid H _ {i} \right\} P (H _ {i})}{\mathbb {P} \left\{\boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right\}} = \frac {p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} \mid H _ {i}) P (H _ {i})}{p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})}
$$

showing that the rule decides for the hypothesis whose posterior probability given the observed data is maximum. 

In the special case that the two hypothese are equally likely the threshold is $\eta = 1$ and the decision rule becomes a Maximum Likelihood (ML) decision rule. 

Since the conditional error probabilities are: 

$$
P (e | H _ {1}) = \mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) <   \eta | H _ {1} \right\} \quad P (e | H _ {2}) = \mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) > \eta | H _ {2} \right\}
$$

the error probability is 

$$
\mathbb {P} (e) = P \left(H _ {1}\right) P \left(e \mid H _ {1}\right) + P \left(H _ {2}\right) P \left(e \mid H _ {2}\right)
$$

## Example: classifying binary sources

Assume that the observations are iid binary variables that may come with equal probabilities from either a source with ${ \mathbb { P } } \left\{ X _ { i } = 1 \right\} = p _ { 1 }$ or a source with ${ \mathbb { P } } \left\{ X _ { i } = 1 \right\} = p _ { 2 }$ , with $p _ { 1 } > p _ { 2 }$ 

We thus have: 

$$
p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {i}) = p _ {i} ^ {w _ {H} (\boldsymbol {x} ^ {n})} (1 - p _ {i}) ^ {n - w _ {H} (\boldsymbol {x} ^ {n})}
$$

where $w _ { H } ( \pmb { x } ^ { n } )$ is the Hamming weight of the binary observed sequence $\pmb { x } ^ { n }$ coinciding with the number of its 1’s. 

The minimum error probability test is 

$$
\left(\frac {p _ {1}}{p _ {2}}\right) ^ {w _ {H} (x ^ {n})} \left[ \frac {(1 - p _ {1})}{(1 - p _ {2})} \right] ^ {n - w _ {H} (x ^ {n})} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 1
$$

or, equivalently 

$$
w _ {H} (\boldsymbol {x} ^ {n}) \ln \left(\frac {p _ {1}}{p _ {2}}\right) + (n - w _ {H} (\boldsymbol {x} ^ {n})) \ln \left(\frac {1 - p _ {1}}{1 - p _ {2}}\right) \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 0
$$

which boils down to 

$$
w _ {H} \big (\boldsymbol {x} ^ {n} \big) \left[ \ln \left(\frac {p _ {1}}{1 - p _ {1}} \frac {1 - p _ {2}}{p _ {2}}\right) \right] \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} n \ln \left(\frac {1 - p _ {2}}{1 - p _ {1}}\right)
$$

## Evaluating the performance

Notice that, since $p _ { 1 } > p _ { 2 }$ , all the logarithms are non-negative; 

The test can thus be re-written in the form 

$$
w _ {H} (x ^ {n}) \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} n \frac {\ln \left(\frac {1 - p _ {2}}{1 - p _ {1}}\right)}{\ln \left(\frac {p _ {1}}{1 - p _ {1}} \frac {1 - p _ {2}}{p _ {2}}\right)} = \eta_ {1}
$$

Assuming that $\eta _ { 1 }$ is not integer, the conditional error probabilities under the two alternative hypotheses are written as: 

$$
\mathbb {P} (e | H _ {1}) = \mathbb {P} \left\{  w _ {H} (\boldsymbol {X} ^ {n}) <   \eta_ {1}   |   H _ {1} \right\} = \sum_ {i = 0} ^ {\lfloor \eta_ {1} \rfloor} \binom{n}{i} p _ {1} ^ {i} (1 - p _ {1}) ^ {n - i}
$$

$$
\mathbb {P} (e | H _ {2}) = \mathbb {P} \left\{w _ {H} (\boldsymbol {X} ^ {n}) > \eta_ {1} | H _ {2} \right\} = \sum_ {i = \lfloor \eta_ {1} \rfloor + 1} ^ {n} \binom{n}{i} p _ {2} ^ {i} (1 - p _ {2}) ^ {n - i}
$$

whereby the error probability read 

$$
\mathbb {P} (e) = \frac {1}{2} \mathbb {P} (e | H _ {1}) + \frac {1}{2} \mathbb {P} (e | H _ {2})
$$

## Binary classification: continuous data law

Assume now that the data may be drawn from M possible continuous probability laws, whereby we are given a set of candidate conditional probabilit density functions $\{ f _ { \pmb { X } ^ { n } | H _ { i } } ( \pmb { x } ^ { n } | \pmb { H } _ { i } ) \} _ { i = 1 } ^ { M }$ ; 

The only diference with the discrete case is case is that now 

$$
\mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {1} | H _ {1} \right\} = \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {1}} \left(\boldsymbol {x} ^ {n} | H _ {1}\right) d \boldsymbol {x} ^ {n} \quad \mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {2} | H _ {2} \right\} = \int_ {\Omega_ {2}} f _ {\boldsymbol {X} ^ {n} | H _ {2}} \left(\boldsymbol {x} ^ {n} | H _ {2}\right) d \boldsymbol {x} ^ {n}
$$

Thus, following the same line of thought as for the discrete case, we obtain that the minimumm error probability test is written as 

$$
\boldsymbol {x} ^ {n} \in \Omega_ {i} \text {   iff   } f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) P (H _ {1}) > f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {2}) P (H _ {2})
$$

or equivalently 

$$
L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2})} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} \frac {P (H _ {2})}{P (H _ {1})} = \eta
$$

The quantity $L ( \pmb { x } ^ { n } )$ on the LHS is again called likelihood ratio between the two alternative hypotheses. 

## Example: testing the mean of a Gaussian population

Assume that the data set $\pmb { x } ^ { n }$ is equally likely to be a realization of an independent Gaussian random vector whose elements have the same variance and diferent means $\mu _ { 1 }$ and $\mu _ { 2 } < \mu _ { 1 }$ ; 

Since $\begin{array} { r } { f _ { X ^ { n } | H _ { i } } ( x ^ { n } | H _ { i } ) = \prod _ { k = 1 } ^ { n } \frac { 1 } { \sqrt { 2 \pi \sigma ^ { 2 } } } e ^ { - \frac { ( x _ { k } - \mu _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } } } \end{array}$ the optimum test is written as 

$$
L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2})} = e ^ {\frac {\sum_ {k = 1} ^ {n} (x _ {k} - \mu_ {2}) ^ {2} - (x _ {k} - \mu_ {1}) ^ {2}}{2 \sigma^ {2}}} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} 1
$$

Taking the logarithm on both sides and elaborating we obtain the equivalent test 

$$
\frac {1}{n} \sum_ {k = 1} ^ {n} x _ {k} \underset {H _ {2}} {\overset {H _ {1}} {\gtrless}} \frac {\mu_ {1} + \mu_ {2}}{2} = \eta
$$

The quantities $\sum x _ { k }$ for this problem and $w _ { H } ( \pmb x ^ { n } )$ for the previous one are also referred to as suficient statistics in inferential statistics parlance. 

## Performance evaluation

Notice that, under $H _ { j }$ , the test statistic $\begin{array} { r } { Z _ { n } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } X _ { i } } \end{array}$ is Gaussian with mean and variance given by: 

$$
\mathbb {E} [ Z _ {n} | H _ {i} ] = \mu_ {i} \quad \sigma_ {Z _ {n}} ^ {2} = \frac {\sigma^ {2}}{n} \quad w h y?
$$

As a consequence the conditional error probabilities are 

$$
\mathbb {P} (e | H _ {1}) = \mathbb {P} \left\{Z _ {n} <   \eta | H _ {1} \right\} = 1 - Q \left(\frac {\eta - \mu_ {1}}{\sigma_ {Z _ {n}}}\right) = 1 - Q \left(\sqrt {n} \frac {\mu_ {2} - \mu_ {1}}{2 \sigma}\right)
$$

$$
\mathbb {P} (e | H _ {2}) = \mathbb {P} \left\{Z _ {n} > \eta | H _ {2} \right\} = Q \left(\frac {\eta - \mu_ {2}}{\sigma_ {Z _ {n}}}\right) = Q \left(\sqrt {n} \frac {\mu_ {1} - \mu_ {2}}{2 \sigma}\right)
$$

Since $\mu _ { 1 } - \mu _ { 2 } > 0$ , we also have $\mathbb { P } ( e | H _ { 1 } ) = \mathbb { P } ( e | H _ { 2 } ) = Q \left( { \sqrt { n } } { \frac { \mu _ { 1 } - \mu _ { 2 } } { 2 \sigma } } \right)$ , whereby 

$$
\mathbb {P} (e) = Q \left(\sqrt {n} \frac {\mu_ {1} - \mu_ {2}}{2 \sigma}\right)\rightarrow 0 \quad \text { as } n \rightarrow \infty
$$

## Hypothesis testing: introduction

There are numerous situations where we have to make a decision between two hypotheses, but have no means to assign the cost matrix C nor the prior probabilities; 

Examples include a number of situations of practical interest, i.e.: 

Early detection of threats to the security of a patrolled area; 

Intrusion detection in protected servers/domains on the internet; 

Obstacle detection (and localization) in Advance Driver Assistance Systems (ADAS); 

Air trafic control; 

Uncountable military applications; 

In all of the above situations, it is practically impossible to assign a cost to a misjudgement of the ”state of the nature”, i.e. to a wrong decision between the two hypotheses ”everything normal” or ”something’s happening”; 

It is also of little significance to assign a prior probability that ”statistical anomalies” in the data set are present. 

## Definitions in hypothesis testing

0 First of all, we define a null hypothesis, traditionally denoted $H _ { 0 }$ , that the observed data set $\pmb { x } ^ { n }$ are a realization of a random vector witn a known conditional distribution, with pmf/pdf $p _ { X ^ { n } | H _ { 0 } } ( { \pmb x } ^ { n } | H _ { 0 } ) / f _ { { \pmb X } ^ { n } | H _ { 0 } } ( { \pmb x } ^ { n } | H _ { 0 } )$ ; 

We want to decide whether or not, given the observed data $\pmb { x } ^ { n }$ , the nul hypothesis should be rejected in favour of a diferent law, say $p _ { X ^ { n } \mid H _ { 1 } } ( { \pmb x } ^ { n } | H _ { 1 } ) / f _ { { \pmb X } ^ { n } \mid H _ { 1 } } ( { \pmb x } ^ { n } | H _ { 1 } )$ ; 

As for binary classification, we have to partition the domain $\mathcal { X } ^ { n }$ in two decision regions, but the previous Bayes framework is no longer applicable here due to the lack of suficient prior information; 

In designing a decision rule (i.e., a test), we thus define: 

The test type-I error, or false alarm probability, as 

$$
\mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 1 | H _ {0} \right\} = \left\{ \begin{array}{l l} \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0}) d \boldsymbol {x} ^ {n} & \text { Continuous   Data } \\ \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {1}} p _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0}) & \text { Discrete   Data } \end{array} \right.
$$

The test power, i.e.: 

$$
1 - \beta = \mathbb {P} \left\{D (\boldsymbol {X} ^ {n}) = 1 | H _ {1} \right\} = \left\{ \begin{array}{l l} \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) d \boldsymbol {x} ^ {n} \\ \sum_ {\boldsymbol {x} ^ {n} \in \Omega_ {1}} p _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) \end{array} \right.
$$

Continous Data 

Discrete Data 

## Neyman-Pearson Test

Given the framework outlined in the previous slide, a Neyman-Pearson test is the result of the following constrained optimization: 

$$
\text { Determine } \Omega_ {1} \colon \left\{ \begin{array}{l l} 1 - \beta & \text { maximum } \\ \text { subject   to } & \text { type - 1   error } \leq \alpha \end{array} \right.
$$

The existence of the solution of such a constrained problem is the bulk of the Neyman-Pearson lemma; 

The resulting test is the likelihood ratio test 

$$
L \left(\boldsymbol {x} ^ {n}\right) \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta L \left(\boldsymbol {x} ^ {n}\right) = \left\{ \begin{array}{l l} \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (x ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {0}} (x ^ {n} | H _ {0})} & \text { Continuous   data } \\ \frac {p _ {\boldsymbol {X} ^ {n} | H _ {1}} (x ^ {n} | H _ {1})}{p _ {\boldsymbol {X} ^ {n} | H _ {0}} (x ^ {n} | H _ {0})} & \text { Discrete   data } \end{array} \right.
$$

The threshold $\eta$ should be chosen as the solution to the equation: 

$$
\mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) > \eta | H _ {0} \right\} = \alpha
$$

Notice that applying any monotonically increasing function to both sides of the previous test does not alter its optimality, whereby we can equivalently introduce the log-likelihood ln $L \left( \pmb { x } ^ { n } \right) = \Lambda ( \pmb { x } ^ { n } )$ and compare it to a newl determined threshold. 

## Example: testing the mean of a Gaussian population

Assume that the null hypothesis is that the observations are iid Gaussian with zero mean and given variance, i.e. $X _ { i } \sim \mathcal { N } ( 0 , \sigma ^ { 2 } )$ , while its alternative is $X _ { i } \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ ; 

Following the slide 18, the likelihood ratio test reads 

$$
L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {0}} (\boldsymbol {x} ^ {n} | H _ {0})} = e ^ {\frac {\sum_ {k = 1} ^ {n} (x _ {k} - \mu) ^ {2} - x _ {k} ^ {2}}{2 \sigma^ {2}}} \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta
$$

where now η should be chosen so as to satisfy the constraint. 

Taking the logarithm on both sides, simplifying and absorbing in a new (unknown) threshold $\eta ^ { \prime }$ all of the data-independent quantities we obtain the equivalent test 

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta^ {\prime}
$$

where $\eta ^ { \prime }$ should be chosen so as to ensure that the type-I error probability is equal to the design value α. 

## Test performance

We first have to set the detection threshold. Notice that the test statistic, under $H _ { 0 }$ , is Gaussian with zero mean and variance $\frac { \sigma ^ { 2 } } { n }$ (see slide 18). As a consequence: 

$$
\mathbb {P} \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} > \eta^ {\prime} | H _ {0} \right\} = Q \left(\frac {\sqrt {n} \eta^ {\prime}}{\sigma}\right) = \alpha \Longrightarrow \eta^ {\prime} = \frac {\sigma}{\sqrt {n}} Q ^ {- 1} (\alpha)
$$

To evaluate the test power, we notice that, under $H _ { 1 }$ , the test statistic is Gaussian with mean $\mu$ and variance $\frac { \sigma ^ { 2 } } { n }$ , whereby: 

$$
1 - \beta = \mathbb {P} \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} > \eta^ {\prime} | H _ {1} \right\} = Q \left(\sqrt {n} \frac {\eta^ {\prime} - \mu}{\sigma}\right)
$$

It is worth noticing that, for $n  \infty , \eta ^ { \prime }  0$ for any $\alpha ,$ so that 

$$
\lim _ {n \rightarrow \infty} 1 - \beta = \lim _ {n \rightarrow \infty} Q \left(\sqrt {n} \frac {\eta^ {\prime} (n) - \mu}{\sigma}\right) = 1
$$

namely we get to the ideal performance $\alpha = 0 , 1 - \beta = 1$ 

## Parameter estimation: generalities

Assume that we have a dataset $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ which is a realization of a random vector $X ^ { n }$ ; 

Assume that the random vector $X ^ { n }$ is drawn from a distribution family with pmf/pdf $p _ { X ^ { n } | \Theta } ( \pmb { x } ^ { n } | \theta ) / f _ { \pmb { X } ^ { n } | \Theta } ( \pmb { x } ^ { n } | \theta )$ , where the value of $\theta$ is unknown; 

θ is a typically continupos parameter, which may be a realization of a continupos random variable Θ with known marginal $f _ { \Theta } ( \theta )$ (Bayesian setting) or an unknown deterministic quantity taking on values in a continuous set; 

Question: How do we estimate θ based on the collected sample? 

Remark that, under Bayesian setting, direct application of the Bayes’ rule yields: 

$$
f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) = \left\{ \begin{array}{c} p _ {\boldsymbol {X} ^ {n} | \Theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) \\ \hline \int p _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \\ f _ {\boldsymbol {X} ^ {n} | \Theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) \\ \hline \int f _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \end{array} \right.
$$

discrete data 

continuous data 

Remark that, if $\Theta$ is discrete, the above becomes a classification problem. Also notice that in the above equation we used the fact that 

$$
p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \int p _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta \quad f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \int f _ {\boldsymbol {X} ^ {n} | \theta} (\boldsymbol {x} ^ {n} | \theta) f _ {\Theta} (\theta) d \theta
$$

## Parameter Estimation

An estimator of the parameter $\theta$ is a random variale ${ \widehat { \Theta } } ( X ^ { n } )$ - whose realizations are $\widehat { \theta } ( { \pmb x } ^ { n } )$ trying to ”guess” the value of $\theta$ based on an observation $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ 

In order to design an estimator, we first define an average Bayes Risk, i.e.: 

$$
\mathcal {R} = \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right] = \mathbb {E} _ {\boldsymbol {X} ^ {n}} \left[ \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \mid \boldsymbol {X} ^ {n} \right] \right]
$$

where $C ( \cdot )$ is a suitably defined cost function. 

An optimum estimator is one which minimizes the Bayes risk, i.e.: 

$$
\widehat {\Theta} _ {\text { opt }} (\boldsymbol {X} ^ {n}) = \arg \min \mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right]
$$

Since 

$$
\mathbb {E} \left[ C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) \right] = \sum_ {\boldsymbol {x} ^ {n} \in \mathcal {X} ^ {n}} p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) \int C (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta
$$

a Bayes-optimal estimate operating on an observed sample $\pmb { x } ^ { n }$ is defined as: 

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \arg \min \int C (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta
$$

## Minimum Mean Square Error Estimator (MMSEE)

Assume that $C ( \widehat { \Theta } ( X ^ { n } ) - \Theta ) = ( \widehat { \Theta } ( X ^ { n } ) - \Theta ) ^ { 2 }$ 

The Bayes-optimal estimator can be derived as the solution to the equation 

$$
\frac {\partial}{\partial \widehat {\theta} (\boldsymbol {x} ^ {n})} \int (\widehat {\theta} (\boldsymbol {x} ^ {n}) - \theta) ^ {2} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta = 0
$$

We thus obtain the estimate 

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \int \theta f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta = \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ]
$$

which corresponds for sure to a minimum given the convexity of the chosen Bayes risk. 

## Example: Compound Bernoulli

Assume $X ^ { n } \in \{ 0 , 1 \} ^ { n }$ is conditionally Bernoulli with parameter $\beta ,$ , with $B \sim \mathcal { U } ( 0 , 1 )$ 

The Hamming weight $w ( \pmb { x } ^ { n } )$ of a binary sequence is the number of ones it contains. We have: 

$$
p _ {\boldsymbol {X} ^ {n} | B} (\boldsymbol {x} ^ {n} | \beta) = \beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}
$$

Averaging over B we have the unconditional law: 

$$
p \mathbf {x} ^ {n} (\mathbf {x} ^ {n}) = \int_ {0} ^ {1} \beta^ {w (\mathbf {x} ^ {n})} (1 - \beta) ^ {n - w (\mathbf {x} ^ {n})} d \beta = \frac {\Gamma (w + 1) \Gamma (n - w + 1)}{\Gamma (n + 2)} = \frac {1}{\binom{n + 1}{w (\mathbf {x} ^ {n})}}
$$

The conditional law is thus 

$$
f _ {B | \boldsymbol {X} ^ {n}} (\beta | \boldsymbol {x} ^ {n}) = \frac {\beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}}{p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})} = \frac {\beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}}{\binom{n + 1}{w (\boldsymbol {x} ^ {n})}}
$$

## Example: Compound Bernoulli - cont’d

The MMSE estimate is thus 

$$
\frac {1}{p \boldsymbol {x} ^ {n} (\boldsymbol {x} ^ {n})} \int_ {0} ^ {1} \beta^ {w (\boldsymbol {x} ^ {n}) + 1} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})} d \beta
$$

## Solving the integral thus yields

$$
\hat {\beta} _ {\text {MMSE}} (\boldsymbol {x} ^ {n}) = \frac {\Gamma (w + 2) \Gamma (n - w + 1)}{\Gamma (n + 3)} \frac {1}{\binom{n + 1}{w (\boldsymbol {x} ^ {n})}} = \frac {w (\boldsymbol {x} ^ {n}) + 1}{n + 2}
$$

which is the estimate obtained through the MMSE estimator: 

$$
\hat {B} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) = \frac {w (\boldsymbol {X} ^ {n}) + 1}{n + 2}
$$

## Maximum A Posteriori Estimator (MAPE)

Assume now the following cost function: 

$$
C (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) = \Pi \left(\frac {\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta}{\epsilon}\right) = \left\{ \begin{array}{l l} 0 & \left| \widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta \right| <   \frac {\epsilon}{2} \\ 1 & \text { otherwise } \end{array} \right.
$$

It is obvious that, as  is arbitrarily small, this results in the MAP estimator 

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \arg \max f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n})
$$

Applying this estimator to the previous problem (compound-Bernoulli) we have the estimate: 

$$
\widehat {\beta} _ {\mathrm{MAP}} (\pmb {x} ^ {n}) = \frac {w (\pmb {x} ^ {n})}{n}
$$

As a consequence, the MAP estimator of the unknown parameter is 

$$
\widehat {B} _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) = \frac {w (\boldsymbol {X} ^ {n})}{n}
$$

## Estimator Performance: Systematic error (Bias)

Let us preliminarily notice that: 

$$
\mathbb {E} \left[ B \right] = \int_ {0} ^ {1} \beta d \beta = \frac {1}{2}, \quad \mathbb {E} \left[ B ^ {2} \right] = \frac {1}{3}, \quad \sigma_ {B} ^ {2} = \frac {1}{1 2}
$$

Since 

$$
\mathbb {E} \left[ w (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \overbrace {\mathbb {E} \left[ w (\boldsymbol {X} ^ {n}) | B \right]} ^ {n B} \right] = \frac {n}{2}, \quad \mathbb {E} \left[ w ^ {2} (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \overbrace {\mathbb {E} \left[ w (\boldsymbol {X} ^ {n}) | B \right]} ^ {n B (1 - B) + n ^ {2} B ^ {2}} \right] = \frac {n}{6} + \frac {n ^ {2}}{3}
$$

whereby $\begin{array} { r } { \sigma _ { w ( X ^ { n } ) } ^ { 2 } = \frac { n } { 6 } \left( 1 + \frac { n } { 2 } \right) } \end{array}$ 

For the MMSEE: 

$$
\mathbb {E} \left[ \hat {B} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) | B = \beta \right] = \frac {n \beta + 1}{n + 2}, \quad \mathbb {E} \left[ \hat {B} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) \right] = \frac {\frac {n}{2} + 1}{n + 2}
$$

For the MAPE: 

$$
\mathbb {E} \left[ \hat {B} _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) | B = \beta \right] = \beta ,
$$

$$
\mathbb {E} \left[ \hat {B} _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) \right] = \frac {\frac {n}{2}}{n} = \frac {1}{2}
$$

We conclude that the MMSEE is a biased estimator, while the MAP is not; 

Notice that the MMSEE is asymptotically unbiased, since the systematic erro vanishes as n grows large. 

## Casual errors: Consistency

After lenghty - albeit elementary - calculations, we find: 

$$
\mathbb {E} \left[ (B _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) - B) ^ {2} \right] = \overline {{e ^ {2}}} _ {\text { MMSE }} = \frac {n - 2}{6 (n + 2) ^ {2}}
$$

$$
\mathbb {E} \left[ (B _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) - B) ^ {2} \right] = \overline {{e ^ {2}}} _ {\mathrm{MAP}} = \frac {1}{6 n}
$$

Needless to say, we have $\overline { { e ^ { 2 } } } _ { \mathsf { M M S E } } < \overline { { e ^ { 2 } } } _ { \mathsf { M A P } } \ \forall n$ 

Since both MSE’s go to zero as n grows large, we have that the two estimators are defined MS consistent, in the sense that the random error has asymptotically zero MS value; 

Exploiting Tchebyshev’s inequality, we have that both estimators tend to B in probability (consistency, a.k.a. weak consistency). If ${ \widehat { B } } ( X ^ { n } )$ is any of the two estimators, we thus have: 

$$
\forall \epsilon > 0 \quad \lim _ {n \rightarrow \infty} \operatorname * {P r} \left\{\left| \widehat {B} (\boldsymbol {X} ^ {n}) - B \right| > \epsilon \right\} = 0
$$

It can be shown that both estimators are strongly consistent, in the sense that ${ \widehat { B } } ( X ^ { n } ) \to B$ almost surely. 

## General definitions

Consider a sample $\pmb { x } ^ { n }$ drawn from a random vector $\pmb { X } ^ { n } \in \mathcal { X } ^ { n } \subseteq \mathbb { R } ^ { n }$ 

$\mathcal { X } ^ { n }$ may be discrete or continuous, but we assume that $X ^ { n }$ has a pdf (pmf, in the discrete case) known to belong to a family with known prior. Thus, we assume knowledge of the joint pdf $f _ { \pmb { X } ^ { n } , \Theta } ( \pmb { x } ^ { n } , \theta )$ and of the parameter prio $f _ { \Theta } ( \theta )$ 

We want to infer the parameter value of $\theta$ for the observed realization $\pmb { x } ^ { n }$ . The MMSE estimate and the MAP estimate are thus defined as 

$$
\widehat {\theta} _ {\mathrm{MMSE}} (\boldsymbol {x} ^ {n}) = \mathbb {E} \left[ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right] = \int \theta f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta , \quad \widehat {\theta} _ {\mathrm{MAP}} (\boldsymbol {x} ^ {n}) = \arg \max _ {\theta} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n})
$$

An estimator is unbiased if $\mathbb { E } \left[ \widehat { \Theta } ( \pmb { \cal X } ^ { n } ) - \Theta \right] = 0 ;$ 

An estimator is asymptotically unbiased if it is unbiased only in the limit of infinite sample size; 

An estimator is consistent if ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ in probability; 

An estimator is MS consistent if ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ in mean square; 

An estimator is strongly consistent if ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ almost surely. 

## An example: Gaussian observations with random mean

Let $\pmb { x } ^ { n }$ be drawn from $X ^ { n }$ with: 

$$
f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \exp \left[ - \frac {(x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}} \right]
$$

Let $\mu$ be a realization of $M \sim \mathcal N ( 0 , \sigma _ { M } ^ { 2 } )$ 

We want to infer the value $\mu$ of M pertaining to the observation $\pmb { x } ^ { n }$ of $X ^ { n }$ 

Remark that the posterior density of the mean reads: 

$$
f _ {M | \boldsymbol {X} ^ {n}} (\mu | \boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) f _ {M} (\mu)}{f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})} = \mathcal {N} \left(\frac {\sum_ {i = 1} ^ {n} x _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}, \frac {1}{\frac {n}{\sigma^ {2}} + \frac {1}{\sigma_ {M} ^ {2}}}\right)
$$

Otherwise said, the conjugate prior of the mean of a Gaussian distribution is again Gaussian; 

We thus have that the MMSE estimate of the mean reads 

$$
\widehat {\mu} _ {\text { MMSE }} (\boldsymbol {x} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} x _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}} \Longleftrightarrow \widehat {M} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}
$$

Let us now consider the MAP estimate. We can obviously write 

$$
\ln f _ {M | \boldsymbol {X} ^ {n}} (\mu | \boldsymbol {x} ^ {n}) = \ln f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) + \ln f _ {M} (\mu) - \ln f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})
$$

By maximizing with respect to $\mu$ we obtain the MAP estimator 

$$
\widehat {\mu} _ {\text {MAP}} (\boldsymbol {x} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}} \Longleftrightarrow \widehat {M} _ {\text {MAP}} (\boldsymbol {X} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}
$$

which is coincident with the MMSEE!! 

Question: Is this casual or there is a deeper reason for the coincidence of these two estimators? 

## Uniqueness of Bayes estimators

Let C (·) be an arbitrary cost function of the estimation error; 

Assume that C(·) is even and convex and that $f _ { \Theta | , X ^ { n } } ( \theta | \pmb { x } ^ { n } )$ is symmetrical with respect to its mean $\mathbb { E } \left[ \Theta | \pmb { X } ^ { n } = \pmb { x } ^ { n } \right]$ , i.e.: 

$$
f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta - \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ] | \boldsymbol {x} ^ {n}) = f _ {\Theta | \boldsymbol {X} ^ {n}} (- \theta + \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ] | \boldsymbol {x} ^ {n})
$$

Then the MMSEE minimizes the Bayes risk for any cost function in this class. 

The proof is simple, and is omitted here. 

Remark that, strictly speaking, the 0 − 1 cost function leading to a MAP estimator is not diferentiable. 

Nonetheless, it can be shown that, under the above symmetry condition on the posterior, we have 

$$
\widehat {\mu} _ {\text { MAP }} (\boldsymbol {x} ^ {n}) = \widehat {\mu} _ {\text { MMSE }} (\boldsymbol {x} ^ {n})
$$

## Non-Bayesian inference: Non-random parameter estimation

Assume now that the observations $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ are drawn from a family of pdf’s, $f _ { { \pmb X } ^ { n } } \big ( { \pmb x } ^ { n } ; { \boldsymbol \theta } \big )$ ; 

Assume that θ is deterministic and unknown: equivalently, we may assume tha we do not have enough prior information to assign a prior $f _ { \Theta } ( \theta )$ ); 

Assume that the parameter space is S; 

We define likelihood of the parameter θ, given that the observations $\pmb { x } ^ { n }$ are available, the function: 

$$
L (\theta ; \boldsymbol {x} ^ {n}) = f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta)
$$

or, equivalently, log-likelihood the function 

$$
\Lambda (\theta ; \boldsymbol {x} ^ {n}) = \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta)
$$

A Maximum Likelihood (ML) estimate of $\theta$ is 

$$
\widehat {\theta} _ {\mathrm{ML}} \left(\boldsymbol {x} ^ {n}\right) = \arg \max _ {\theta \in \mathcal {S}} \log f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {x} ^ {n}; \theta\right)
$$

and it is a realization of the Maximum Likelihood Estimator (MLE): 

$$
\widehat {\Theta} _ {M L} \left(\boldsymbol {X} ^ {n}\right) = \arg \max _ {\theta \in \mathcal {S}} \log f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {X} ^ {n}; \theta\right)
$$

## Non-Bayesian Inference: Performance measures

Given an estimator $\Theta ( { \pmb x } ^ { n } )$ of the non-random parameter $\theta ,$ , we have: 

$$
\mathbb {E} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \theta + b _ {n} (\theta)
$$

with $b _ { n } ( \theta )$ the estimator bias; 

The estimator is unbiased if $b _ { n } ( \theta ) = 0$ , while being only asymptotically unbiased if $b _ { n } ( \theta )$ becomes vanishingly small with $n ;$ 

The casual error of the estimator is usually quantified via its Mean Square value, i.e.: 

$$
\mathbb {E} \left[ (\Theta (\boldsymbol {X} ^ {n}) - \theta) ^ {2} \right] = \overline {{e _ {n} ^ {2}}}
$$

An unbiased MMSE estimator of $\theta$ is an estimator which minimizes the variance: 

$$
\operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \Theta^ {2} (\boldsymbol {X} ^ {n}) \right] - \theta^ {2}
$$

An estimator is weakly consistent if $\Theta ( { \pmb x } ^ { n } ) \to \theta$ in probability, strongly consistent if $\Theta ( { \pmb x } ^ { n } ) \to \theta$ almost surely, MS consistent if $\overline { { e _ { n } ^ { 2 } } } \to 0$ 

## Cram´er-Rao Bound - Preliminary facts

Let $\pmb { x } ^ { n }$ a sample drawn from a random vecto ${ \pmb X } ^ { n } \sim f _ { { \pmb X } ^ { n } } ( { \pmb x } ^ { n } ; { \pmb \theta } )$ with $\theta$ non-random; 

Consider the identity 

$$
\int_ {\mathbb {R} ^ {n}} f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {x} ^ {n}; \theta\right) d \boldsymbol {x} ^ {n} = 1
$$

Upon diferentiation with respect to $\theta$ of the above we have 

$$
\begin{array}{c} \int_ {\mathbb {R} ^ {n}} \frac {\partial f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} d \boldsymbol {x} ^ {n} = \int_ {\mathbb {R} ^ {n}} \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta) d \boldsymbol {x} ^ {n} \\ = \mathbb {E} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = 0 \end{array}
$$

Diferentiating again we have: 

$$
\begin{array}{c} \mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right] = \text {var} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = \\ = - \mathbb {E} \left[ \frac {\partial^ {2} \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta^ {2}} \right] \end{array}
$$

## Cram´er-Rao Bound - Derivation

Let $\widehat { \Theta } ( X ^ { n } )$ be an estimator of the non-random parameter $\theta$ with: 

$$
\mathbb {E} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \int_ {\mathbb {R} ^ {n}} \widehat {\Theta} (\boldsymbol {X} ^ {n}) f _ {\boldsymbol {X} ^ {n}} (x ^ {n}; \theta) d x ^ {n} = \theta + b _ {n} (\theta)
$$

Diferentiating with respect to $\theta$ the above identity we have 

$$
\begin{array}{l} \mathbb {E} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] \\ \int_ {\mathbb {R} ^ {n}} \Theta (x ^ {n}) \frac {\partial f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)}{\partial \theta}   d x ^ {n} = \overbrace {\int_ {\mathbb {R} ^ {n}} \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)}{\partial \theta} f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)   d x ^ {n}} \\ \text { COV } \left[ \Theta (\boldsymbol {X} ^ {n}), \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = 1 + b _ {n} ^ {\prime} (\theta) \end{array}
$$

Applying Cauchy-Schwart’s inequality, we finaly have 

$$
\left| \operatorname{COV} \left[ \Theta (\boldsymbol {X} ^ {n}), \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] \right| ^ {2} = \left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2} \leq \operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] \operatorname{Var} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right]
$$

## Cram´er-Rao Bound - Further Discussion

Elaborating the previous derivations, we obtain an unbeatable lower bound to the variance of any estimator of the non-random parameter $\theta$ in the form: 

$$
\operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] \geq \frac {\left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2}}{\mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right]} = \frac {\left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2}}{I _ {n} (\theta)}
$$

The quantity $I _ { n } ( \theta )$ is defined as the Fisher Information, and obeys the following identity: 

$$
I _ {n} (\theta) = \mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right] = - \mathbb {E} \left[ \frac {\partial^ {2} \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta^ {2}} \right]
$$

## Cram´er-Rao Bound - Unbiased Estimators

As anticipated, the estimator $\Theta ( { \pmb x } ^ { n } )$ is unbiased if <sup>E</sup> $[ \Theta ( { \pmb x } ^ { n } ) ] = \theta$ 

In this situation, we have that 

$$
\mathbb {E} \left[ (\Theta (\boldsymbol {X} ^ {n}) - \theta) ^ {2} \right] = \operatorname{Var} [ \Theta (\boldsymbol {X} ^ {n}) ] \geq \frac {1}{I _ {n} (\theta)}
$$

Thus the Cram´er-Rao Bound (CRB) becomes an unbeatable lower bound to the MSE of any estimator. 

An unbiased estimator whose MSE is equal to the CRB is defined eficient 

Important fact: If an eficient estimator for a given non-Bayesian estimation problem exists, this necessarily coincides with the ML estimator. 

## An example: inferring the cipher frequency of a memoryless source

Let us consider initially $\pmb { x } ^ { n } \in \{ 0 , 1 \} ^ { n }$ , drawn from $\pmb { X } ^ { n } \sim  { \mathcal { B } } ( 1 , \beta )$ , $\beta$ uknown; 

We saw that, ilf $w ( \pmb { x } ^ { n } )$ is the Hamming weight of the observed sequence, then: 

$$
p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}
$$

The ML estimate is thus found as: 

$$
\frac {\partial \log p _ {X ^ {n}} (x ^ {n})}{\partial \beta} = 0 \Longrightarrow \widehat {\beta} _ {\mathrm{ML}} (x ^ {n}) = \frac {w (x ^ {n})}{n}
$$

The estimator $\begin{array} { r } { \beta ( \pmb { X } ^ { n } ) = \frac { w ( \pmb { X } ^ { n } ) } { n } } \end{array}$ is such that: 

$$
\mathbb {E} \left[ \frac {w (\boldsymbol {X} ^ {n})}{n} \right] = \beta  ,
$$

$$
\operatorname{var} \left[ \frac {w (\boldsymbol {X} ^ {n})}{n} \right] = \frac {\beta (1 - \beta)}{n}
$$

As a consequence, it is unbiased and MS consistent. Is it eficient? 

## Cipher frequency - cont’d

Notice that we have: 

$$
\log p _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {X} ^ {n}; \beta\right) = w \left(\boldsymbol {X} ^ {n}\right) \log \beta + [ n - w \left(\boldsymbol {X} ^ {n}\right) ] \log (1 - \beta)
$$

Thus we have: 

$$
\frac {\partial p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \beta)}{\partial \beta} = \frac {w (\boldsymbol {X} ^ {n})}{\beta} - \frac {n - w (\boldsymbol {X} ^ {n})}{1 - \beta}
$$

$$
\frac {\partial^ {2} p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \beta)}{\partial \beta^ {2}} = - \frac {w (\boldsymbol {X} ^ {n})}{\beta^ {2}} - \frac {n - w (\boldsymbol {X} ^ {n})}{(1 - \beta) ^ {2}}
$$

Since $\mathbb { E } [ w ( \pmb { X } ^ { n } ) ] = \pmb { n } \beta$ , we have: 

$$
I _ {n} (\beta) = \frac {n}{\beta} + \frac {n}{1 - \beta} = \frac {n}{\beta (1 - \beta)} \Longrightarrow \mathrm{CRB} = \frac {\beta (1 - \beta)}{n}
$$

We conclude that the MLE of the cipher frequency is eficient. 

## Multiple parameters - Bayesian inference

Assume now that we have m random parameters, $\pmb { \theta } [ \theta _ { 1 } , \ldots , \theta _ { m } ] ^ { T }$ drawn from a known pdf $f _ { \Theta } ( \pmb { \theta } )$ and a data set $\pmb { x } ^ { n }$ drawn from a conditional pdf $f _ { { \pmb X } ^ { n } | \pmb \theta } ( { \pmb x } ^ { n } | \pmb \theta )$ 

Define a cost function 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = C \left(\theta_ {1} - \widehat {\theta} _ {1}, \dots , \theta_ {m} - \widehat {\theta} _ {m}\right)
$$

A Bayes-optimal estimator can be found by solving the minimization problem: 

$$
\widehat {\boldsymbol {\theta}} (\boldsymbol {x} ^ {n}): \quad \mathbb {E} \left[ C (\boldsymbol {\Theta} - \widehat {\boldsymbol {\Theta}} (\boldsymbol {X} ^ {n})) \right] = 0
$$

Using the same procedure as for the single-parameter case we thus obtain: 

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \arg \min \int_ {\mathbb {R} ^ {m}} C \left(\boldsymbol {\theta} - \widehat {\theta} \left(\boldsymbol {X} ^ {n}\right)\right) f _ {\Theta | \boldsymbol {X} ^ {n}} \left(\boldsymbol {\theta} \mid \boldsymbol {X} ^ {n}\right) d \boldsymbol {\theta}
$$

## The MMSE estimator

Assume that the cost function is 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = \sum_ {i = 1} ^ {m} \left(\theta_ {i} - \widehat {\theta} _ {i} (\boldsymbol {x} ^ {n}))\right)
$$

Since the minimization problem is disjoint (i.e., separable), we have: 

$$
\widehat {\theta} _ {i} (\boldsymbol {x} ^ {n}) = \mathbb {E} \left[ \Theta_ {i} | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right] = \int \theta_ {i} f _ {\theta_ {i} | \boldsymbol {X} ^ {n}} (\theta_ {i} | \boldsymbol {x} ^ {n}) d \theta_ {i}
$$

whereby the vector MMSE estimator reads: 

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \mathbb {E} \left[ \Theta | \boldsymbol {X} ^ {n} \right]
$$

## The MAP estimator

If we assume 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = \sum_ {i = 1} ^ {m} \Pi \left(\frac {\theta_ {i} - \widehat {\theta} _ {i} (\boldsymbol {x} ^ {n})}{\epsilon}\right)
$$

considering the same procedure we have 

$$
\widehat {\theta} _ {i} \left(\boldsymbol {x} ^ {n}\right): \quad \frac {\partial f _ {\Theta | \boldsymbol {X} ^ {n}} \left(\boldsymbol {\theta} \mid \boldsymbol {x} ^ {n}\right)}{\partial \theta_ {i}} \Bigg | _ {\theta_ {i} = \widehat {\theta} _ {i} \left(\boldsymbol {x} ^ {n}\right)} = 0
$$

Equivalently, we have that the MAP estimate solves the equation: 

$$
\nabla_ {\boldsymbol {\theta}} f _ {\boldsymbol {\Theta} | \boldsymbol {X} ^ {n}} (\boldsymbol {\theta} | \boldsymbol {x} ^ {n}) \big | _ {\boldsymbol {\theta} = \widehat {\boldsymbol {\theta}} (x ^ {n})} = 0
$$

## Non-Bayesian estimation of multiple parameters

Assume now that the parameter vector $\pmb { \theta }$ is real and deterministic; 

We may define the log-likelihood function of the observed data, assumed drawn from a distribution family $f _ { \pmb { X } ^ { n } } ( \pmb { x } ^ { n } ; \pmb { \theta } )$ as: 

$$
\Lambda (\boldsymbol {\theta}; \boldsymbol {x} ^ {n}) = \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}, \boldsymbol {\theta})
$$

We define Maximum-Likelihood estimate of the vector $\pmb { \theta }$ the solution to the equation: 

$$
\nabla_ {\boldsymbol {\theta}} \Lambda (\boldsymbol {\theta}; \boldsymbol {x} ^ {n}) | _ {\boldsymbol {\theta} = \widehat {\boldsymbol {\theta}} (\boldsymbol {x} ^ {n})} = 0
$$

The corresponding estimator $\widehat { \Theta } ( X ^ { n } )$ is again defined a Maximum Likelihood (ML) estimator and enjoys a number of fundamental properties. 

## Linear MMSE estimators

0 Let us start with a simple scalar problem. Assume $\pmb { x } ^ { n }$ is the observed sample, drawn from $X ^ { n }$ , and assume that we want to design a linear estimator of a random parameter $\Theta ,$ , distributed according a known law, in the form: 

$$
\widehat {\Theta} (\boldsymbol {X} ^ {n}) = \boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b \quad \boldsymbol {a} \in \mathbb {R} ^ {n}
$$

A Linear MMSE (LMMSE) estimator selects the vector a and the constant b so as to minimize the MMSE 

$$
\mathbb {E} \left[ (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) ^ {2} \right] = \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right]
$$

which is equal to 

$$
\boldsymbol {a} ^ {T} \boldsymbol {R} \boldsymbol {a} + b ^ {2} + \mathbb {E} [ \Theta^ {2} ] - 2 b (\overline {{{\Theta}}}) - 2 \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} \Theta ] - 2 b \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ]
$$

where $\pmb { R } = \mathbb { E } \left[ \pmb { X } ^ { n } \pmb { X } ^ { n T } \right]$ is the correlation matrix of the random vector $X ^ { n }$ 

## Linear MMSE estimators (cont’d)

Nullifying the gradient with respect to a and the derivative with respect to $b$ we obtain: 

$$
\nabla_ {\boldsymbol {a}} \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \mathbb {E} [ \boldsymbol {X} ^ {n} \Theta ] = 0
$$

$$
\frac {\partial \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right]}{\partial b} = 2 b - 2 \overline {{\Theta}} - 2 \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ] = 0
$$

## Solving for b yields

$$
b _ {\text { LMMSE }} = \mathbb {E} [ \Theta ] - \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ]
$$

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \boldsymbol {a} ^ {T} \left(\boldsymbol {X} ^ {n} - \mathbb {E} \left[ \boldsymbol {X} ^ {n} \right]\right) + \mathbb {E} [ \Theta ]
$$

which, placed back into the MSE demonstrates that a should minimize 

$$
\left\| \boldsymbol {a} ^ {T} \left(\boldsymbol {X} ^ {n} - \mathbb {E} \left[ \boldsymbol {X} ^ {n} \right]\right) + (\Theta - \mathbb {E} [ \Theta ]) \right\| ^ {2}
$$

As a consequence, denoting $\pmb { M } = \mathbb { E } \left[ ( \pmb { X } ^ { n } - \mathbb { E } [ \pmb { X } ^ { n } ] ) ( \pmb { X } ^ { n } - \mathbb { E } [ \pmb { X } ^ { n } ] ) ^ { T } \right]$ the covariance matrix of $X ^ { n }$ , the LMMSE estimator reads 

$$
\boldsymbol {a} _ {\text { LMMSE }} = \boldsymbol {M} ^ {- 1} \mathbb {E} \left[ \left(\boldsymbol {X} ^ {n} - \mathbb {E} [ \boldsymbol {X} ^ {n} ]\right) (\Theta - \mathbb {E} [ \Theta ]) \right] = \boldsymbol {M} ^ {- 1} \boldsymbol {s}
$$

## The gradient algorithm

Assume that we want to solve iteratively the LMMSE problem outlined before; 

We saw that the gradient of the MSE is written as 

$$
\nabla_ {a} \mathbb {E} \left[ \left(\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta\right) ^ {2} \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \mathbb {E} \left[ \boldsymbol {X} ^ {n} \Theta \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \boldsymbol {s}
$$

with $\mathbb { E } \left[ \pmb { X } ^ { n } \Theta \right] = \pmb { s }$ known; 

Consider the following iteration to determine $\pmb { \alpha } _ { \mathrm { L M M S E } }$ 

$$
\boldsymbol {a} ^ {(n + 1)} = \boldsymbol {a} ^ {(n)} - \gamma (\boldsymbol {M a} ^ {(n)} - \boldsymbol {s})
$$

which can be rewritten as 

$$
\boldsymbol {a} ^ {(n + 1)} = \boldsymbol {a} ^ {(n)} - \gamma \boldsymbol {M} \left(\boldsymbol {a} ^ {(n)} - \underbrace {\boldsymbol {M} ^ {- 1} \boldsymbol {s}} _ {\boldsymbol {a} _ {\text { LMMSE }}}\right)
$$

## The Gradient algorithm - cont’d

The error at the (n + 1)−th iteration reads 

$$
\boldsymbol {\epsilon} ^ {(n + 1)} = \boldsymbol {a} ^ {(n + 1)} - \boldsymbol {a} _ {\text { LMMSE }} = \boldsymbol {a} ^ {(n)} - \boldsymbol {a} _ {\text { LMMSE }} - \gamma \boldsymbol {M} (\boldsymbol {a} ^ {(n)} - \boldsymbol {a} _ {\text { LMMSE }}) = (\boldsymbol {I} - \gamma \boldsymbol {M}) \boldsymbol {\epsilon} ^ {(n)}
$$

As a consequence we have 

$$
\boldsymbol {\epsilon} ^ {(n + 1)} = (\boldsymbol {I} - \gamma \boldsymbol {M}) ^ {n} \boldsymbol {\epsilon} ^ {(1)} = \boldsymbol {U} (\boldsymbol {I} - \gamma \boldsymbol {\Lambda}) ^ {n} \boldsymbol {U} ^ {T}
$$

where Λ is the diagonal matrix of the eigenvalues of M and U contains its eigenvectors. 

The error thus converges to zero if the maximum modulus of the eigenvalues o $\pmb { I } - \gamma \pmb { M }$ is smaller than one, i.e.: 

$$
- 1 <   1 - \gamma \lambda_ {M A X} <   1 \Longrightarrow 0 <   \gamma <   \frac {2}{\lambda_ {M A X}}
$$

## A diferent approach: descriptive statistics

Let us now forget about probability. Let us assume instead to shift to descriptive statistics, wherein the samples count for what they are and are not considered realizations of random vectors: 

We define a training dataset as a collection of p n−dimensional samples, which can be organized in the $n \times p$ matrix: 

$$
\boldsymbol {X} = \left[ \begin{array}{c c c} x _ {1} (1) & \dots & x _ {1} (p) \\ \dots & \dots & \dots \\ x _ {n} (1) & \dots & x _ {n} (p) \end{array} \right] \in \mathbb {R} ^ {n \times p}
$$

Assume we know p measured values of the parameter $\theta _ { r }$ , each corresponding to one of the p n−dimensional samples of the training set, i.e.: 

$$
\boldsymbol {y} = [ \theta (1), \dots , \theta (p) ] \in \mathbb {R} ^ {p}
$$

We want to fit the data to a linear model in the form 

$$
\theta (i) = \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) + \epsilon_ {n}
$$

with $\epsilon _ { n }$ encapsulating the error. 

## The Least Squares estimator

Since we have a p−dimensional dataset, we want to select a in such a way to minimize: 

$$
\parallel \epsilon_ {n} \parallel^ {2} = \sum_ {i = 1} ^ {p} \left[ \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) - \theta (i) \right] ^ {2}
$$

Our problem is to select a and $b$ in an optimized way. Notice preliminarily that 

$$
\sum_ {i = 1} ^ {p} \left[ \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) - \theta (i) \right] ^ {2} = \| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \| ^ {2}
$$

Notice that 

$$
\| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \| ^ {2} = \boldsymbol {a} ^ {T} \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {a} + \| \boldsymbol {y} \| ^ {2} - 2 \boldsymbol {a} ^ {T} \boldsymbol {X} \boldsymbol {y}
$$

## The Least Squares estimator - cont’d

Diferentiating with respect to a thus yields 

$$
\nabla_ {a} \left\| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \right\| ^ {2} = 2 \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {a} - 2 \boldsymbol {X} \boldsymbol {y} = 0
$$

which yields 

$$
\boldsymbol {a} _ {\mathrm{LS}} = \left(\boldsymbol {X} \boldsymbol {X} ^ {T}\right) ^ {- 1} \boldsymbol {X} \boldsymbol {y}
$$

requiring $( { \pmb x } { \pmb x } ^ { T } )$ to be invertible $( \mathsf { i . e . , } \ p \geq n )$ 

For future reference, let us denote this estimate based on a p−dimensiona sample as 

$$
\boldsymbol {a} _ {\mathrm{LS}} (p) = \left(\boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p)\right) ^ {- 1} \boldsymbol {X} (p) \boldsymbol {y} (p)
$$

Assume that we have an infinite-horizon observation of the environment, so that the sample size p may increase; 

We consider two scenarios, i.e.: 

a We want to progressively improve our estimate by adding more observations; 

b We want to adapt to possibly changing conditions by ”forgetting” old observations in order to weigh new observations more significantly. 

We can adjust the LS estimator in such a way as to account for both situations above, and we can do it with limited complexity. 

## Learning LS

Assume $p \geq n$ and assume we have evaluated 

$$
\boldsymbol {a} _ {\mathrm{LS}} (p) = \left[ \boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p) \right] ^ {- 1} \boldsymbol {X} (p) \boldsymbol {y} (p)
$$

Assume we have a new vector in the dataset, $\pmb { x } ^ { n } ( p + 1 )$ say, and a new observation, $\theta ( p + 1 )$ . 

The new estimate would be 

$$
\boldsymbol {a} _ {\mathrm{LS}} (p + 1) = \left[ \boldsymbol {X} (p + 1) \boldsymbol {X} ^ {T} (p + 1) \right] ^ {- 1} \boldsymbol {X} (p + 1) \boldsymbol {y} (p + 1)
$$

Question: Do we have to recompute everything from scratch? 

Notice that the inversion operation involves a $\mathcal { O } ( n ^ { 3 } )$ complexity, while the matrix product operation has a complexity $\mathcal { O } ( n p )$ (in terms of multiplications). 

## The Sherman-Morrison Formula

Let R be an invertible matrix of order $n ;$ 

Let u and v be n−dimensional column vectors; 

We have the following matrix inversion lemma with rank-1 update: 

$$
\left(\boldsymbol {R} + \boldsymbol {u v} ^ {T}\right) ^ {- 1} = \boldsymbol {R} ^ {- 1} - \frac {\boldsymbol {R} ^ {- 1} \boldsymbol {u v} ^ {T} \boldsymbol {R} ^ {- 1}}{1 + \boldsymbol {u} ^ {T} \boldsymbol {R} ^ {- 1} \boldsymbol {v}}
$$

## Generalities - Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation

## Application

## Notice that

$$
\underbrace {\boldsymbol {X} (p + 1) \boldsymbol {X} ^ {T} (p + 1)} _ {\boldsymbol {R} (p + 1)} = \sum_ {i = 1} ^ {p + 1} \boldsymbol {x} ^ {n} (i) \boldsymbol {x} ^ {n T} (i) = \underbrace {\boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p)} _ {\boldsymbol {R} (p)} + \boldsymbol {x} ^ {n} (p + 1) \boldsymbol {x} ^ {n T} (p + 1)
$$

As a consequence 

$$
\boldsymbol {R} ^ {- 1} (p + 1) = \boldsymbol {R} ^ {- 1} (p) - \frac {\boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1) \boldsymbol {x} ^ {n T} (p + 1) \boldsymbol {R} ^ {- 1} (p)}{1 + K (p + 1)}
$$

with 

$$
K (p + 1) = \boldsymbol {x} ^ {n T} (p + 1) \boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1)
$$

## Application - cont’d

## On the other hand we have

$$
\boldsymbol {X} (p + 1) = \left[ \boldsymbol {X} (p) \boldsymbol {x} ^ {n} (p + 1) \right], \quad \boldsymbol {y} (p + 1) = \left[ \boldsymbol {y} (p) \theta (p + 1) \right] ^ {T}
$$

implying 

$$
\boldsymbol {X} (p + 1) \boldsymbol {y} (p + 1) = \boldsymbol {X} (p) \boldsymbol {y} (p) + \theta (p + 1) \boldsymbol {x} ^ {n} (p + 1)
$$

Since ${ \pmb a } ( p + 1 ) = { \pmb R } ^ { - 1 } ( p + 1 ) { \pmb X } ( p + 1 ) { \pmb y } ( p + 1 )$ , we have 

$$
\boldsymbol {a} (p + 1) = \left[ \boldsymbol {I} _ {n} - \frac {\boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1)}{1 + K (p + 1)} \boldsymbol {x} ^ {n T} (p + 1) \right]
$$

$$
\left[ \boldsymbol {a} (p) + \theta (p + 1) \boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1) \right]
$$

which has complexity $\mathcal { O } ( n ^ { 2 } )$ , independent (and not scaling with) $p .$ 

## Adaptivity in LS

In order to cope with situations where the surrounding environment may be (slowly) time-varying, we may want to force ”old data” to weigh less than ”fresh” data. 

A possible way to do so is via exponential smoothing, whose main idea is to adopt the following cost function: 

$$
\sum_ {i = 1} ^ {p} w ^ {p - i} \left[ \pmb {\mathscr {a}} ^ {T} \pmb {x} ^ {n} (i) - \theta (i) \right] ^ {2}
$$

The weight $w < 1$ regulates how fast the past is forgotten. 

Minimizing with respect to a yields the exponentially smoothed LS: 

$$
\boldsymbol {a} = \left[ \sum_ {i = 1} ^ {p} w ^ {p - i} \boldsymbol {x} ^ {n} (i) \boldsymbol {x} ^ {n T} (i) \right] ^ {- 1} \sum_ {i = 1} ^ {p} w ^ {p - i} \boldsymbol {x} ^ {n} (i) \theta (i)
$$

itself amenable to a recursive implementation in the light of Sherman-Morrison lemma. 

## Generalization

Assume now that, under the same conditions seen above, we want to find an LS in the more general form 

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} + b
$$

Lengthy, albeit simple, calculations lead to the general LMS form 

$$
\boldsymbol {a} _ {\text { LMS }} = (\boldsymbol {X} _ {0} \boldsymbol {X} _ {0} ^ {T}) ^ {- 1} \boldsymbol {X} _ {0} \boldsymbol {y} _ {0}, \qquad b _ {\text { LMS }} = \underbrace {\frac {1}{p} \sum_ {i = 1} ^ {p} \theta (i)} _ {\widetilde {\theta}} - \frac {1}{p} \boldsymbol {1} _ {p} ^ {T} \boldsymbol {X} ^ {T} \boldsymbol {a} _ {\text { LMS }}
$$

where ${ \bf 1 } _ { p }$ is an all-one $p -$ dimensional vector and 

$$
\boldsymbol {X} _ {0} = \left[ \begin{array}{c c c} x _ {1} (1) - \overline {{x}} _ {1} & \dots & x _ {1} (p) - \overline {{x}} _ {1} \\ \dots & \dots & \dots \\ x _ {n} (1) - \overline {{x}} _ {n} & \dots & x _ {n} (p) - \overline {{x}} _ {n} \end{array} \right] \in \mathbb {R} ^ {n \times p}, \quad \boldsymbol {y} _ {0} = \left[ y _ {1} - \overline {{\theta}}, \ldots , y _ {p} - \overline {{\theta}} \right] ^ {T}
$$

with 

$$
\overline {{x}} _ {k} = \frac {1}{p} \sum_ {i = 1} ^ {p} x _ {k} (i) \Longleftrightarrow \overline {{\mathbf {x}}} = \frac {1}{p} \sum_ {i = 1} ^ {p} \mathbf {x} ^ {n} (i), \quad \mathbf {X} _ {0} = \mathbf {X} - \overline {{\mathbf {x}}} \mathbf {1} _ {p} ^ {T}
$$