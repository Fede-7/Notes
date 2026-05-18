## Pagina 1

Elementi di Statistica inferenziale

Marco Lops

lops@unina.it
https://docenti.unina.it/marco.lops

---

## Pagina 2

Some Definitions

- Assume we have a sample of size $n$, say $x \in \mathbb{R}^n$;
- Assume that this sample is the result of a random experiment, which means that re-sampling would lead to a different set of results, say $x' \in \mathbb{R}^n$;
- Statistical inference is the process of using data analysis to infer properties of an underlying distribution of probability, i.e. defining a law which any sample randomly drawn should abide with;
- Inferential statistics can be contrasted with descriptive statistics. Descriptive statistics is solely concerned with properties of the observed data, and it does not rest on the assumption that the data come from a larger population.
- Basic goals of Statistical inference are Hypothesis Testing and Parameter Estimation.

---

## Pagina 3

An example: the sample mean

- Assume we have a data set $x^n \in \mathcal{X}^n \subseteq \mathbb{R}^n$;
- We know that the sample mean is defined as
$$\bar{x}_n = \frac{1}{n} \sum_{i=1}^{n} x_i$$
- The law of large numbers tells us that $\bar{X}_n \to \mathbb{E}[X]$ (the type of convergence depending on the underlying statistical law), in the sense that, denoting $X^n$ a random sample drawn from the population, we have
$$\frac{1}{n} \sum_{i=1}^{n} X_i \to \mathbb{E}[X]$$
- Weak convergence (i.e., convergence in probability) tells us that the frequency of samples whose sample mean departs significantly from $\mathbb{E}[X]$ is as small as we want;
- Strong convergence states that in the limit the probability of departing from $\mathbb{E}[X]$ is zero;
- Mean-Square convergence states that
$$\lim_{n \to \infty} \mathbb{E}\left[ \left( \bar{x}_n - \mathbb{E}[X] \right)^2 \right] = 0$$

---

## Pagina 4

The Sample mean - cont’d

- Assume that $x^n \in \mathcal{X}^n$, with $\mathcal{X} = (a_1, \ldots, a_M)$ discrete and finite;
- we know that
  $$\bar{x}_n = \sum_{i=1}^{M} a_i f_n(a_i)$$
  where $f_n(a_i)$ is the fraction of values of the sample yielding $a_i$;
- We know that, if $X \in \mathcal{X}$ is a random variable with pmf $\{p_X(a_i)\}_{i=1}^M$, then:
  $$\mathbb{E}[X] = \sum_{i=1}^{M} a_i p_X(a_i)$$
- As a consequence, we have
  $$|\bar{x}_n - \mathbb{E}[X]| \leq \sum_{i=1}^{M} |a_i| |f_n(a_i) - p_X(a_i)|$$
- Notice that if we can claim that $f_n(a_i) \rightarrow p_X(a_i)$ (in some sense), then we may infer that $x^n$ is a sample from a population whose elements are drawn from a random vector $X^n$ with marginal density $\{p_X(a_i)\}_{i=1}^M$.

---

## Pagina 5

The Empirical distribution

- Assume that $x^n$ is drawn from $X^n$, a set of $n$ iid random variables with unknown marginal $\{p_X(a_i)\}_{i=1}^M$;
- The frequency of occurrence of the event $X_k = a_i$ is itself random. If $N_i$ is the number of times $X_k = a_i$ in our $n$-dimensional sample, we have:

$$\Pr\{N_i = k\} = \binom{n}{k} p_X(a_i)^k [1 - p_X(a_i)]^{n-k}$$

- Since

$$\mathbb{E}\left[\frac{N_i}{n}\right] = p_X(a_i), \quad \text{var}\left[\frac{N_i}{n}\right] = \frac{p_X(a_i)(1 - p_X(a_i))}{n}$$

we have that $\frac{N_i}{n} \rightarrow p_X(a_i)$ in mean square, i.e.:

$$\lim_{n \to \infty} \mathbb{E}\left[\left(\frac{N_i}{n} - p_X(a_i)\right)^2\right] = 0$$

---

## Pagina 6

Almost sure convergence

- Assume that $\{q(a_i)\}$ is any other pmf on $\mathcal{X}$ differing from the true distribution $p_X(a_i)$ in at least two elements. We have:
  $$\Pr\{N_i = nq(a_i)\} = \binom{n}{nq(a_i)} p_X(a_i)^{nq(a_i)} [1 - p_X(a_i)]^{n(1 - q(a_i))}$$

- Using the bound
  $$\sqrt{\frac{n}{8k(n - k)}} \leq \binom{n}{k} 2^{-nH\left(\frac{k}{n}\right)} \leq \sqrt{\frac{n}{\pi k(n - k)}}$$

we have, upon setting $k = nq(a_i)$:
$$\sqrt{\frac{1}{8nq(a_i)(1 - q(a_i))}} \leq \binom{n}{nq(a_i)} 2^{-n\left[q(a_i) \log \frac{1}{q(a_i)} + (1 - q(a_i)) \log \frac{1}{1 - q(a_i)}\right]}$$
$$\leq \sqrt{\frac{1}{\pi nq(a_i)(1 - q(a_i))}}$$

we have, for increasingly large $n$:
$$\binom{n}{nq(a_i)} \sim 2^{nH_2(q(a_i), 1 - q(a_i))}$$

---

## Pagina 7

Consider now a value $a_i$ for which $q(a_i) \neq p_X(a_i)$.

When $n$ grows large we have:

$$\Pr \{N_i = nq(a_i)\} \sim 2^{nH_2(q(a_i), 1 - q(a_i))} p_X(a_i)^{nq(a_i)} [1 - p_X(a_i)]^{n(1 - q(a_i))}$$

$$= 2^{nH_2(q(a_i), 1 - q(a_i))} 2^{n[q(a_i) \log p_X(a_i) + (1 - q(a_i)) \log(1 - p_X(a_i))]}$$

$$= 2^{n\left[q(a_i) \log \frac{p_X(a_i)}{q(a_i)} + (1 - q(a_i)) \log \frac{1 - p_X(a_i)}{1 - q(a_i)}\right]} = 2^{-nD_i}$$

with

$$D_i = q(a_i) \log \frac{q(a_i)}{p_X(a_i)} + [1 - q(a_i)] \log \frac{1 - q(a_i)}{1 - p_X(a_i)} > 0$$

We thus conclude that the probability that the frequency of occurrence does not equal the true probability goes to zero exponentially with $n$.

This implies that $f_n(a_i) \rightarrow p_X(a_i)$ almost surely.

---

## Pagina 8

Assume we have a sample $x^n \in \mathcal{X}^n$, $\mathcal{X} = \{a_1, \ldots, a_M\}$ drawn from a random vector $X^n$ of unknown pmf;

If we compute the frequencies of occurrence:

$$f_n(a_i) = \frac{\# \text{ of elements equal to } a_i}{n}, \quad i = 1, \ldots, M$$

we have:

$$\Pr \left\{ \lim_{n \to \infty} \frac{N_i}{n} = \lim_{n \to \infty} f_n(a_i) \right\} = 1$$

This implies that any other sample, $y^n$ say, drawn from the same population will exhibit, for $n \to \infty$, the same statistical behavior.

Needless to say, we’ll have that for any function $f(\cdot)$ of the data

$$\Pr \left\{ \lim_{n \to \infty} f(X^n) = \lim_{n \to \infty} f(x^n) \right\} = 1$$

Thus, the sample mean converges with probability one to the statistical average of the population.

This property is also referred to in inferential statistics as strong consistency.

---

## Pagina 9

The main idea is that, once we observe a sufficiently ample sample of a given data population, we may infer a number of characteristics any other sample should abide to;

Some prior knowledge as to the statistics of the population the sample is drawn from may be a priori known;

For example, we might assume that the sample is drawn from a population whose distribution is known up to a set of parameters;

To begin with, let us assume that the sample si known to be drawn from a family of distributions, indexed by a parameter $\theta$, which is to be estimated;

Question: How do we process the available dataset in order to infer the value of the parameter?

---

## Pagina 10

Bayesian Setting: Decision rule

- Assume that we have a dataset $x^n \in \mathcal{X}^n$ which is a realization of a random vector $X^n$;
- Assume that - based on the state of the nature - the data may come from any of $M$ different probability laws.
- We thus have a set of $M$ different, mutually exclusive hypotheses $\{H_i\}_{i=1}^M$, each defining a different conditional law for the data set, i.e.:

$$p_{X^n}(x^n|H_i), \quad i=1,\ldots,M$$

- Assume that the random vector $X^n$ is drawn from a distribution family with pmf $p_{X^n}|\Theta(x^n|\theta)$, where the value of $\theta$ is unknown;
- Assume also that the prior probabilities - $\{p(H_i)\}_{i=1}^M$ - of these states of the nature are assigned;
- A Decision rule is a map:

$$D : x^n \in \mathcal{X}^n \implies D(x^n) \in \{1,\ldots,M\}$$

which allows us to decide which one of the possible states of the nature is the one actually in force.

---

## Pagina 11

Bayes costs

- Assume that we define the following $M \times M$ cost matrix
  $$C = \begin{bmatrix}
    C_{1,1} & C_{1,2} & \ldots & C_{1,M} \\
    \ldots & \ldots & \ldots & \ldots \\
    C_{M,1} & C_{M,2} & \ldots & C_{M,M}
  \end{bmatrix}$$
  where $C_{i,j}$ is the cost associated to the event we make decision $D(x^n) = i$ and the state of the nature is $H_j$;
- We define the average Bayesian risk as:
  $$\mathcal{R} = \sum_{i=1}^{M} \sum_{j=1}^{M} C_{i,j} \mathbb{P}\{D(x^n) = i, H = H_j\}$$

- Given a cost matrix $C$, an optimal decision rule is a map $D(x^n)$ which minimizes the Bayes risk;
- Notice that, if $C_{i,j} = 0$ if $i = 1, \ldots, M$ and $C_{i,j} = 1$ if $\forall i \neq j$, then
  $$\mathcal{R} = \sum_{i=1}^{M} \sum_{j \neq i} \mathbb{P}\{D(x^n) = i, H = H_j\} = \mathbb{P}(e)$$
  namely the average Bayes risk coincides with the probability of committing a classification error.

---

## Pagina 12

Binary Classification problem

Assume for the moment that $M = 2$, that $C_{1,1} = C_{2,2} = 0$ and $C_{1,2} = C_{2,1} = 1$, so that

$$\mathcal{R} = \mathbb{P}\{D(\mathbf{x}^n) = 2, H_1\} + \mathbb{P}\{D(\mathbf{x}^n) = 1, H_2\} = \mathbb{P}(e)$$

Designing a decision rule implies determining a partition of $\mathcal{X}^n$ in two subsets, $\Omega_1$ and $\Omega_2$, such that

$$D(\mathbf{x}^n) = \begin{cases} 
1 & \text{if } \mathbf{x}^n \in \Omega_1 \\
2 & \text{if } \mathbf{x}^n \in \Omega_2 
\end{cases}$$

The corresponding error probability is thus written as:

$$\mathbb{P}(e) = \mathbb{P}\{X^n \in \Omega_1, H_2\} + \mathbb{P}\{X^n \in \Omega_2, H_1\}$$

We want to determine the optimum (i.e., with minimum error probability) decision law for this binary classification problem.

---

## Pagina 13

Binary classification: discrete data laws

- Assume that the observations $X^n$ are a discrete random vector with given conditional pmf’s $p(X^n|H_i)$;
- We obviously have $\mathbb{P}\{X^n \in \Omega_i; H_j\} = 1 - \sum_{x^n \in \Omega_i} p(H_i)\mathbb{P}\{X^n = x^n|H_i\}$ whereby the error probability is written as
$$\mathbb{P}(e) = 1 - \left[ \sum_{x^n \in \Omega_1} p(H_1)\mathbb{P}\{X^n = x^n|H_1\} + \sum_{x^n \in \Omega_2} p(H_2)\mathbb{P}\{X^n = x^n|H_2\} \right]$$
which is minumum when the quantity in brackets is maximum.

- We thus obtain the following optimum decision rule:
$$X^n \in \Omega_i \text{ iff } p(X^n|H_1)(X^n|H_1)P(H_1) > p(X^n|H_2)(X^n|H_2)P(H_2)$$
or equivalently
$$L(X^n) = \frac{p(X^n|H_1)}{p(X^n|H_2)} \geq \frac{P(H_2)}{P(H_1)} = \eta$$

- The quantity $L(X^n)$ on the LHS is called likelihood ratio between the two alternative hypotheses.

---

## Pagina 14

The previous decision rule is also known as Maximum A-posteriori Probability (MAP) decision rule, in that, by the Bayes’ law:

$$\mathbb{P}\{H = H_i | X^n = x^n\} = \frac{\mathbb{P}\{X^n = x^n | H_i\} P(H_i)}{\mathbb{P}\{X^n = x^n\}} = \frac{pX^n(x^n | H_i) P(H_i)}{pX^n(x^n)}$$

showing that the rule decides for the hypothesis whose posterior probability given the observed data is maximum.

In the special case that the two hypotheses are equally likely the threshold is $\eta = 1$ and the decision rule becomes a Maximum Likelihood (ML) decision rule.

Since the conditional error probabilities are:

$$P(e | H_1) = \mathbb{P}\{L(X^n) < \eta | H_1\} \quad P(e | H_2) = \mathbb{P}\{L(X^n) > \eta | H_2\}$$

the error probability is

$$\mathbb{P}(e) = P(H_1)P(e | H_1) + P(H_2)P(e | H_2)$$

---

## Pagina 15

Example: classifying binary sources

- Assume that the observations are iid binary variables that may come with equal probabilities from either a source with $\mathbb{P}\{X_i = 1\} = p_1$ or a source with $\mathbb{P}\{X_i = 1\} = p_2$, with $p_1 > p_2$;
- We thus have:
  $$p_X^n(x^n|H_i) = p_i^{w_H(x^n)}(1-p_i)^{n-w_H(x^n)}$$
- where $w_H(x^n)$ is the Hamming weight of the binary observed sequence $x^n$, coinciding with the number of its 1's.
- The minimum error probability test is
  $$\left(\frac{p_1}{p_2}\right)^{w_H(x^n)} \left[ \frac{(1-p_1)}{(1-p_2)} \right]^{n-w_H(x^n)} \gtrsim 1$$
- or, equivalently
  $$w_H(x^n) \ln \left(\frac{p_1}{p_2}\right) + (n-w_H(x^n)) \ln \left(\frac{1-p_1}{1-p_2}\right) \gtrsim 0$$
- which boils down to
  $$w_H(x^n) \left[ \ln \left(\frac{p_1}{1-p_1}\frac{1-p_2}{p_2}\right) \right]^{H_1} \gtrsim n \ln \left(\frac{1-p_2}{1-p_1}\right)$$

---

## Pagina 16

Evaluating the performance

- Notice that, since $p_1 > p_2$, all the logarithms are non-negative;
- The test can thus be re-written in the form

$$w_H(x^n) \gtrsim \frac{n}{\ln \left( \frac{1-p_2}{1-p_1} \right)} = \eta_1$$

- Assuming that $\eta_1$ is not integer, the conditional error probabilities under the two alternative hypotheses are written as:

$$\mathbb{P}(e|H_1) = \mathbb{P}\left\{ w_H(X^n) < \eta_1 | H_1 \right\} = \sum_{i=0}^{\lfloor \eta_1 \rfloor} \binom{n}{i} p_1^i (1-p_1)^{n-i}$$

$$\mathbb{P}(e|H_2) = \mathbb{P}\left\{ w_H(X^n) > \eta_1 | H_2 \right\} = \sum_{i=\lfloor \eta_1 \rfloor+1}^{n} \binom{n}{i} p_2^i (1-p_2)^{n-i}$$

whereby the error probability reads

$$\mathbb{P}(e) = \frac{1}{2} \mathbb{P}(e|H_1) + \frac{1}{2} \mathbb{P}(e|H_2)$$

---

## Pagina 17

Binary classification: continuous data law

Assume now that the data may be drawn from $M$ possible continuous probability laws, whereby we are given a set of candidate conditional probability density functions $\{f_{X^n|H_i}(x^n|H_i)\}_{i=1}^M$;

The only difference with the discrete case is case is that now

$$\mathbb{P}\{X^n \in \Omega_1|H_1\} = \int_{\Omega_1} f_{X^n|H_1}(x^n|H_1) \, dx^n \quad \mathbb{P}\{X^n \in \Omega_2|H_2\} = \int_{\Omega_2} f_{X^n|H_2}(x^n|H_2) \, dx^n$$

Thus, following the same line of thought as for the discrete case, we obtain that the minimum error probability test is written as

$$x^n \in \Omega_i \text{ iff } f_{X^n|H_1}(x^n|H_1) P(H_1) > f_{X^n}(x^n|H_2) P(H_2)$$

or equivalently

$$L(x^n) = \frac{f_{X^n|H_1}(x^n|H_1) H_1}{f_{X^n|H_2}(x^n|H_2) H_2} \geq \frac{P(H_2)}{P(H_1)} = \eta$$

The quantity $L(x^n)$ on the LHS is again called likelihood ratio between the two alternative hypotheses.

---

## Pagina 18

Example: testing the mean of a Gaussian population

- Assume that the data set $x^n$ is equally likely to be a realization of an independent Gaussian random vector whose elements have the same variance and different means $\mu_1$ and $\mu_2 < \mu_1$;
- Since $f_{x^n|H_i}(x^n|H_i) = \prod_{k=1}^{n} \frac{1}{\sqrt{2\pi}\sigma^2} e^{-\frac{(x_k - \mu_1)^2}{2\sigma^2}}$ the optimum test is written as
  $$L(x^n) = \frac{f_{x^n|H_1}(x^n|H_1)}{f_{x^n|H_2}(x^n|H_2)} = e^{\frac{\sum_{k=1}^{n}(x_k - \mu_2)^2 - (x_k - \mu_1)^2}{2\sigma^2}} \geq 1$$
- Taking the logarithm on both sides and elaborating we obtain the equivalent test
  $$\frac{1}{n} \sum_{k=1}^{n} x_k \geq \frac{\mu_1 + \mu_2}{2} = \eta$$
- The quantities $\sum x_k$ for this problem and $w_H(x^n)$ for the previous one are also referred to as sufficient statistics in inferential statistics parlance.

---

## Pagina 19

Notice that, under $H_i$, the test statistic $Z_n = \frac{1}{n} \sum_{i=1}^{n} X_i$ is Gaussian with mean and variance given by:

$$\mathbb{E}[Z_n|H_i] = \mu_i \quad \sigma_Z^2 = \frac{\sigma^2}{n} \quad \text{why?}$$

As a consequence the conditional error probabilities are

$$\mathbb{P}(e|H_1) = \mathbb{P}\{Z_n < \eta|H_1\} = 1 - Q\left(\frac{\eta - \mu_1}{\sigma_Z}\right) = 1 - Q\left(\sqrt{n}\frac{\mu_2 - \mu_1}{2\sigma}\right)$$

$$\mathbb{P}(e|H_2) = \mathbb{P}\{Z_n > \eta|H_2\} = Q\left(\frac{\eta - \mu_2}{\sigma_Z}\right) = Q\left(\sqrt{n}\frac{\mu_1 - \mu_2}{2\sigma}\right)$$

Since $\mu_1 - \mu_2 > 0$, we also have $$\mathbb{P}(e|H_1) = \mathbb{P}(e|H_2) = Q\left(\sqrt{n}\frac{\mu_1 - \mu_2}{2\sigma}\right),$$ whereby

$$\mathbb{P}(e) = Q\left(\sqrt{n}\frac{\mu_1 - \mu_2}{2\sigma}\right) \to 0 \quad \text{as } n \to \infty$$

---

## Pagina 20

Hypothesis testing: introduction

There are numerous situations where we have to make a decision between two hypotheses, but have no means to assign the cost matrix $C$ nor the prior probabilities;

Examples include a number of situations of practical interest, i.e.:

- Early detection of threats to the security of a patrolled area;
- Intrusion detection in protected servers/domains on the internet;
- Obstacle detection (and localization) in Advance Driver Assistance Systems (ADAS);
- Air traffic control;
- Uncountable military applications;
- ……

In all of the above situations, it is practically impossible to assign a cost to a misjudgement of the “state of the nature”, i.e. to a wrong decision between the two hypotheses “everything normal” or “something’s happening”;

It is also of little significance to assign a prior probability that “statistical anomalies” in the data set are present.

---

## Pagina 21

Definitions in hypothesis testing

- First of all, we define a null hypothesis, traditionally denoted $H_0$, that the observed data set $x^n$ are a realization of a random vector with a known conditional distribution, with pmf/pdf $p_{X^n|H_0}(x^n|H_0)/f_{X^n|H_0}(x^n|H_0)$;
- We want to decide whether or not, given the observed data $x^n$, the null hypothesis should be rejected in favour of a different law, say $p_{X^n|H_1}(x^n|H_1)/f_{X^n|H_1}(x^n|H_1)$;
- As for binary classification, we have to partition the domain $X^n$ in two decision regions, but the previous Bayes framework is no longer applicable here due to the lack of sufficient prior information;
- In designing a decision rule (i.e., a test), we thus define:
  - The test type-I error, or false alarm probability, as
    $$\mathbb{P}\{D(X^n) = 1|H_0\} = \begin{cases} 
    \int_{\Omega_1} f_{X^n|H_0}(x^n|H_0) dx^n & \text{Continous Data} \\
    \sum_{x^n \in \Omega_1} p_{X^n|H_0}(x^n|H_0) & \text{Discrete Data}
    \end{cases}$$
  - The test power, i.e.:
    $$1 - \beta = \mathbb{P}\{D(X^n) = 1|H_1\} = \begin{cases} 
    \int_{\Omega_1} f_{X^n|H_1}(x^n|H_1) dx^n & \text{Continous Data} \\
    \sum_{x^n \in \Omega_1} p_{X^n|H_1}(x^n|H_1) & \text{Discrete Data}
    \end{cases}$$

---

## Pagina 22

Neyman-Pearson Test

Given the framework outlined in the previous slide, a Neyman-Pearson test is the result of the following constrained optimization:

$$\text{Determine } \Omega_1: \begin{cases} 1 - \beta & \text{maximum} \\ \text{subject to} & \text{type-1 error} \leq \alpha \end{cases}$$

The existence of the solution of such a constrained problem is the bulk of the Neyman-Pearson lemma;

The resulting test is the likelihood ratio test

$$L(\mathbf{x}^n) \gtrsim \eta L(\mathbf{x}^n) = \begin{cases} \frac{f_{\mathbf{x}^n}|H_1(\mathbf{x}^n)|H_1}{f_{\mathbf{x}^n}|H_0(\mathbf{x}^n)|H_0} & \text{Continuous data} \\ \frac{p_{\mathbf{x}^n}|H_1(\mathbf{x}^n)|H_1}{p_{\mathbf{x}^n}|H_0(\mathbf{x}^n)|H_0} & \text{Discrete data} \end{cases}$$

The threshold $\eta$ should be chosen as the solution to the equation:

$$\mathbb{P}\{L(\mathbf{x}^n) > \eta|H_0\} = \alpha$$

Notice that applying any monotonically increasing function to both sides of the previous test does not alter its optimality, whereby we can equivalently introduce the log-likelihood $\ln L(\mathbf{x}^n) = \Lambda(\mathbf{x}^n)$ and compare it to a newly determined threshold.

---

## Pagina 23

Example: testing the mean of a Gaussian population

- Assume that the null hypothesis is that the observations are iid Gaussian with zero mean and given variance, i.e. $X_i \sim \mathcal{N}(0, \sigma^2)$, while its alternative is $X_i \sim \mathcal{N}(\mu, \sigma^2)$;
- Following the slide 18, the likelihood ratio test reads

$$L(x^n) = \frac{f_{X^n|H_1}(x^n|H_1)}{f_{X^n|H_0}(x^n|H_0)} = e^{\frac{\sum_{k=1}^{n}(x_k - \mu)^2 - x_k^2}{2\sigma^2}} \frac{H_1}{H_0} \eta$$

where now $\eta$ should be chosen so as to satisfy the constraint.

- Taking the logarithm on both sides, simplifying and absorbing in a new (unknown) threshold $\eta'$ all of the data-independent quantities we obtain the equivalent test

$$\frac{1}{n} \sum_{i=1}^{n} x_i \frac{H_1}{H_0} \eta'$$

where $\eta'$ should be chosen so as to ensure that the type-I error probability is equal to the design value $\alpha$.

---

## Pagina 24

We first have to set the detection threshold. Notice that the test statistic, under $H_0$, is Gaussian with zero mean and variance $\frac{\sigma^2}{n}$ (see slide 18). As a consequence:

$$\mathbb{P}\left\{\frac{1}{n} \sum_{i=1}^{n} X_i > \eta' | H_0\right\} = Q\left(\frac{\sqrt{n} \eta'}{\sigma}\right) = \alpha \implies \eta' = \frac{\sigma}{\sqrt{n}} Q^{-1}(\alpha)$$

To evaluate the test power, we notice that, under $H_1$, the test statistic is Gaussian with mean $\mu$ and variance $\frac{\sigma^2}{n}$, whereby:

$$1 - \beta = \mathbb{P}\left\{\frac{1}{n} \sum_{i=1}^{n} X_i > \eta' | H_1\right\} = Q\left(\frac{\sqrt{n} \eta' - \mu}{\sigma}\right)$$

It is worth noticing that, for $n \to \infty$, $\eta' \to 0$ for any $\alpha$, so that

$$\lim_{n \to \infty} 1 - \beta = \lim_{n \to \infty} Q\left(\frac{\sqrt{n} \eta'(n) - \mu}{\sigma}\right) = 1$$

namely we get to the ideal performance $\alpha = 0$, $1 - \beta = 1$.

---

## Pagina 25

Parameter estimation: generalities

- Assume that we have a dataset $x^n \in \mathcal{X}^n$ which is a realization of a random vector $X^n$;
- Assume that the random vector $X^n$ is drawn from a distribution family with pmf/pdf $p_{X^n|\Theta}(x^n|\theta)/f_{X^n|\Theta}(x^n|\theta)$, where the value of $\theta$ is unknown;
- $\theta$ is a typically continuos parameter, which may be a realization of a continupos random variable $\Theta$ with known marginal $f_\Theta(\theta)$ (Bayesian setting) or an unknown deterministic quantity taking on values in a continuous set;
- Question: How do we estimate $\theta$ based on the collected sample?

Remark that, under Bayesian setting, direct application of the Bayes’ rule yields:

$$f_{\Theta|X^n}(\theta|x^n) = \begin{cases} 
\frac{p_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)}{\int p_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)d\theta} & \text{discrete data} \\
\frac{f_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)}{\int f_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)d\theta} & \text{continuous data}
\end{cases}$$

Remark that, if $\Theta$ is discrete, the above becomes a classification problem. Also notice that in the above equation we used the fact that

$$p_{X^n}(x^n) = \int p_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)d\theta \quad f_{X^n}(x^n) = \int f_{X^n|\Theta}(x^n|\theta)f_\Theta(\theta)d\theta$$

---

## Pagina 26

Parameter Estimation

- An estimator of the parameter $\theta$ is a random variable $\hat{\Theta}(X^n)$ - whose realizations are $\hat{\theta}(X^n)$ trying to "guess" the value of $\theta$ based on an observation $x^n \in \mathcal{X}^n$;
- In order to design an estimator, we first define an average Bayes Risk, i.e.:

$$\mathcal{R} = \mathbb{E} \left[ C(\hat{\Theta}(X^n) - \Theta) \right] = \mathbb{E}_{X^n} \left[ C(\hat{\Theta}(X^n) - \Theta) \mid X^n \right]$$

where $C(\cdot)$ is a suitably defined cost function.

- An optimum estimator is one which minimizes the Bayes risk, i.e.:

$$\hat{\Theta}_{\text{opt}}(X^n) = \arg \min \mathbb{E} \left[ C(\hat{\Theta}(X^n) - \Theta) \right]$$

- Since

$$\mathbb{E} \left[ C(\hat{\Theta}(X^n) - \Theta) \right] = \sum_{x^n \in \mathcal{X}^n} p_{X^n}(x^n) \int C(\hat{\theta}(x^n) - \theta) f_{\Theta|X^n}(\theta|x^n) d\theta$$

a Bayes-optimal estimate operating on an observed sample $x^n$ is defined as:

$$\hat{\theta}(x^n) = \arg \min \int C(\hat{\theta}(x^n) - \theta) f_{\Theta|X^n}(\theta|x^n) d\theta$$

---

## Pagina 27

Assume that $C(\hat{\Theta}(X^n) - \Theta) = (\hat{\Theta}(X^n) - \Theta)^2$;

The Bayes-optimal estimator can be derived as the solution to the equation

$$\frac{\partial}{\partial \hat{\theta}(x^n)} \int (\hat{\theta}(x^n) - \theta)^2 f_{\Theta|X^n}(\theta|x^n) d\theta = 0$$

We thus obtain the estimate

$$\hat{\theta}(x^n) = \int \theta f_{\Theta|X^n}(\theta|x^n) d\theta = \mathbb{E} [\Theta|X^n = x^n]$$

which corresponds for sure to a minimum given the convexity of the chosen Bayes risk.

---

## Pagina 28

Example: Compound Bernoulli

- Assume $X^n \in \{0, 1\}^n$ is conditionally Bernoulli with parameter $\beta$, with $B \sim \mathcal{U}(0, 1)$;
- The Hamming weight $w(x^n)$ of a binary sequence is the number of ones it contains. We have:
  $$p_{X^n|B}(x^n|\beta) = \beta^{w(x^n)}(1 - \beta)^{n-w(x^n)}$$

- Averaging over $B$ we have the unconditional law:
  $$p_{X^n}(x^n) = \int_0^1 \beta^{w(x^n)}(1 - \beta)^{n-w(x^n)} d\beta = \frac{\Gamma(w + 1)\Gamma(n - w + 1)}{\Gamma(n + 2)} = \frac{1}{\binom{n + 1}{w(x^n)}}$$

- The conditional law is thus
  $$f_{B|X^n}(\beta|x^n) = \frac{\beta^{w(x^n)}(1 - \beta)^{n-w(x^n)}}{p_{X^n}(x^n)} = \frac{\beta^{w(x^n)}(1 - \beta)^{n-w(x^n)}}{\binom{n + 1}{w(x^n)}}$$

---

## Pagina 29

Example: Compound Bernoulli - cont’d

- The MMSE estimate is thus
  $$\frac{1}{pX^n(x^n)} \int_0^1 \beta^{w(x^n)+1}(1-\beta)^{n-w(x^n)} d\beta$$
- Solving the integral thus yields
  $$\hat{\beta}_{\text{MMSE}}(x^n) = \frac{\Gamma(w+2)\Gamma(n-w+1)}{\Gamma(n+3)} \frac{1}{\binom{n+1}{w(x^n)}} = \frac{w(x^n)+1}{n+2}$$

which is the estimate obtained through the MMSE estimator:

$$\hat{\beta}_{\text{MMSE}}(X^n) = \frac{w(X^n)+1}{n+2}$$

---

## Pagina 30

Maximum A Posteriori Estimator (MAPE)

- Assume now the following cost function:
  $$C(\hat{\Theta}(X^n) - \Theta) = \Pi \left( \frac{\hat{\Theta}(X^n) - \Theta}{\epsilon} \right) = \begin{cases} 0 & \left| \hat{\Theta}(X^n) - \Theta \right| < \frac{\epsilon}{2} \\ 1 & \text{otherwise} \end{cases}$$

- It is obvious that, as $\epsilon$ is arbitrarily small, this results in the MAP estimator
  $$\hat{\theta}(x^n) = \arg \max f_{\Theta|X^n}(\theta|x^n)$$

- Applying this estimator to the previous problem (compound-Bernoulli) we have the estimate:
  $$\hat{\beta}_{\text{MAP}}(x^n) = \frac{w(x^n)}{n}$$

- As a consequence, the MAP estimator of the unknown parameter is
  $$\hat{B}_{\text{MAP}}(x^n) = \frac{w(x^n)}{n}$$

---

## Pagina 31

Estimator Performance: Systematic error (Bias)

- Let us preliminarily notice that:
  $$\mathbb{E}[B] = \int_{0}^{1} \beta d\beta = \frac{1}{2}, \quad \mathbb{E}[B^2] = \frac{1}{3}, \quad \sigma_B^2 = \frac{1}{12}$$

- Since
  $$\mathbb{E}[w(X^n)] = \mathbb{E}\left[ \overbrace{\mathbb{E}[w(X^n)|B]}^{nB} \right] = \frac{n}{2}, \quad \mathbb{E}[w^2(X^n)] = \mathbb{E}\left[ \overbrace{\mathbb{E}[w(X^n)|B]}^{nB(1-B)+n^2B^2} \right] = \frac{n}{6} + \frac{n^2}{3}$$

  whereby $\sigma_B^2 = \frac{n}{6} \left(1 + \frac{n}{2}\right)$.

- For the MMSE:
  $$\mathbb{E}\left[ \hat{B}_{\text{MMSE}}(X^n)|B = \beta \right] = \frac{n\beta + 1}{n+2}, \quad \mathbb{E}\left[ \hat{B}_{\text{MMSE}}(X^n) \right] = \frac{n^2 + 1}{n+2}$$

- For the MAP:
  $$\mathbb{E}\left[ \hat{B}_{\text{MAP}}(X^n)|B = \beta \right] = \beta, \quad \mathbb{E}\left[ \hat{B}_{\text{MAP}}(X^n) \right] = \frac{n^2}{n} = \frac{1}{2}$$

- We conclude that the MMSE is a biased estimator, while the MAP is not;
- Notice that the MMSE is asymptotically unbiased, since the systematic error vanishes as $n$ grows large.

---

## Pagina 32

Casual errors: Consistency

- After lenghty - albeit elementary - calculations, we find:

$$\mathbb{E} \left[ (B_{\text{MMSE}}(X^n) - B)^2 \right] = \overline{e^2}_{\text{MMSE}} = \frac{n - 2}{6(n + 2)^2}$$

$$\mathbb{E} \left[ (B_{\text{MAP}}(X^n) - B)^2 \right] = \overline{e^2}_{\text{MAP}} = \frac{1}{6n}$$

- Needless to say, we have $\overline{e^2}_{\text{MMSE}} < \overline{e^2}_{\text{MAP}} \forall n$.

- Since both MSE’s go to zero as $n$ grows large, we have that the two estimators are defined MS consistent, in the sense that the random error has asymptotically zero MS value;

- Exploiting Tchebyshev’s inequality, we have that both estimators tend to $B$ in probability (consistency, a.k.a. weak consistency). If $\hat{B}(X^n)$ is any of the two estimators, we thus have:

$$\forall \epsilon > 0 \quad \lim_{n \to \infty} \Pr \left\{ \left| \hat{B}(X^n) - B \right| > \epsilon \right\} = 0$$

- It can be shown that both estimators are strongly consistent, in the sense that $\hat{B}(X^n) \to B$ almost surely.

---

## Pagina 33

General definitions

- Consider a sample $x^n$ drawn from a random vector $X^n \in \mathcal{X}^n \subseteq \mathbb{R}^n$;
- $\mathcal{X}^n$ may be discrete or continuous, but we assume that $X^n$ has a pdf (pmf, in the discrete case) known to belong to a family with known prior. Thus, we assume knowledge of the joint pdf $f_{X^n,\Theta}(x^n,\theta)$ and of the parameter prior $f_\Theta(\theta)$.
- We want to infer the parameter value of $\theta$ for the observed realization $x^n$. The MMSE estimate and the MAP estimate are thus defined as

$$\hat{\theta}_{\text{MMSE}}(x^n) = \mathbb{E} \left[ \Theta|X^n = x^n \right] = \int \theta f_{\Theta|X^n}(\theta|x^n) \, d\theta, \quad \hat{\theta}_{\text{MAP}}(x^n) = \arg \max_{\theta} f_{\Theta|X^n}(\theta|x^n)

- An estimator is **unbiased** if $\mathbb{E} \left[ \hat{\Theta}(X^n) - \Theta \right] = 0$;
- An estimator is **asymptotically unbiased** if it is unbiased only in the limit of infinite sample size;
- An estimator is consistent if $\hat{\Theta}(X^n) \rightarrow \Theta$ **in probability**;
- An estimator is MS consistent if $\hat{\Theta}(X^n) \rightarrow \Theta$ **in mean square**;
- An estimator is strongly consistent if $\hat{\Theta}(X^n) \rightarrow \Theta$ **almost surely**.

---

## Pagina 34

An example: Gaussian observations with random mean

- Let $x^n$ be drawn from $X^n$ with:
  $$f_{X^n|M}(x^n|\mu) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-\frac{(x_i - \mu)^2}{2\sigma^2}\right]$$
- Let $\mu$ be a realization of $M \sim \mathcal{N}(0, \sigma_M^2)$;
- We want to infer the value $\mu$ of $M$ pertaining to the observation $x^n$ of $X^n$.
- Remark that the posterior density of the mean reads:
  $$f_{M|X^n}(\mu|x^n) = \frac{f_{X^n|M}(x^n|\mu) f_M(\mu)}{f_X^n(x^n)} = \mathcal{N}\left(\frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}}, \frac{1}{n + \frac{\sigma^2}{\sigma_M^2}}\right)$$
- Otherwise said, the conjugate prior of the mean of a Gaussian distribution is again Gaussian;
- We thus have that the MMSE estimate of the mean reads
  $$\hat{\mu}_{\text{MMSE}}(x^n) = \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}} \iff \hat{M}_{\text{MMSE}}(X^n) = \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}}$$

---

## Pagina 35

MAP Estimator

Let us now consider the MAP estimate. We can obviously write

$$\ln f_M(x^n) (\mu | x^n) = \ln f_{X^n}|M(x^n | \mu) + \ln f_M(\mu) - \ln f_{X^n}(x^n)$$

By maximizing with respect to $\mu$ we obtain the MAP estimator

$$\hat{\mu}_{\text{MAP}}(x^n) = \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}} \iff \hat{M}_{\text{MAP}}(X^n) = \frac{\sum_{i=1}^{n} X_i}{n + \frac{\sigma^2}{\sigma_M^2}}$$

which is coincident with the MMSE!!

Question: Is this casual or there is a deeper reason for the coincidence of these two estimators?

---

## Pagina 36

Uniqueness of Bayes estimators

- Let $C(\cdot)$ be an arbitrary cost function of the estimation error;
- Assume that $C(\cdot)$ is even and convex and that $f_{\Theta|X^n}(\theta|x^n)$ is symmetrical with respect to its mean $\mathbb{E}[\Theta|X^n = x^n]$, i.e.:
  $$f_{\Theta|X^n}(\theta - \mathbb{E}[\Theta|X^n = x^n])|x^n) = f_{\Theta|X^n}(-\theta + \mathbb{E}[\Theta|X^n = x^n])|x^n)$$
- Then the MMSEE minimizes the Bayes risk for any cost function in this class.
- The proof is simple, and is omitted here.
- Remark that, strictly speaking, the 0–1 cost function leading to a MAP estimator is not differentiable.
- Nonetheless, it can be shown that, under the above symmetry condition on the posterior, we have
  $$\hat{\mu}_{\text{MAP}}(x^n) = \hat{\mu}_{\text{MMSE}}(x^n)$$

---

## Pagina 37

Non-Bayesian inference: Non-random parameter estimation

- Assume now that the observations $x^n \in \mathcal{X}^n$ are drawn from a family of pdf’s, $f_{X^n}(x^n; \theta)$;
- Assume that $\theta$ is deterministic and unknown: equivalently, we may assume that we do not have enough prior information to assign a prior $f_\Theta(\theta)$;
- Assume that the parameter space is $S$;
- We define likelihood of the parameter $\theta$, given that the observations $x^n$ are available, the function:

$$L(\theta; x^n) = f_{X^n}(x^n; \theta)$$

or, equivalently, log-likelihood the function

$$\Lambda(\theta; x^n) = \log f_{X^n}(x^n; \theta)$$

- A Maximum Likelihood (ML) estimate of $\theta$ is

$$\hat{\theta}_{\text{ML}}(x^n) = \arg \max_{\theta \in S} \log f_{X^n}(x^n; \theta)$$

and it is a realization of the Maximum Likelihood Estimator (MLE):

$$\hat{\Theta}_{\text{ML}}(X^n) = \arg \max_{\theta \in S} \log f_{X^n}(X^n; \theta)$$

---

## Pagina 38

Given an estimator $\Theta(X^n)$ of the non-random parameter $\theta$, we have:

$$\mathbb{E}[\Theta(X^n)] = \theta + b_n(\theta)$$

with $b_n(\theta)$ the estimator bias;

The estimator is unbiased if $b_n(\theta) = 0$, while being only asymptotically unbiased if $b_n(\theta)$ becomes vanishingly small with $n$;

The casual error of the estimator is usually quantified via its Mean Square value, i.e.:

$$\mathbb{E}[(\Theta(X^n) - \theta)^2] = \frac{e_n^2}{2}$$

An unbiased MMSE estimator of $\theta$ is an estimator which minimizes the variance:

$$\text{Var}[\Theta(X^n)] = \mathbb{E}[\Theta^2(X^n)] - \theta^2$$

An estimator is weakly consistent if $\Theta(X^n) \to \theta$ in probability, strongly consistent if $\Theta(X^n) \to \theta$ almost surely, MS consistent if $\frac{e_n^2}{2} \to 0$.

---

## Pagina 39

Cramér-Rao Bound - Preliminary facts

- Let $x^n$ a sample drawn from a random vector $X^n \sim f_X(x^n; \theta)$ with $\theta$ non-random;
- Consider the identity
  $$\int_{\mathbb{R}^n} f_X(x^n; \theta) dx^n = 1$$
- Upon differentiation with respect to $\theta$ of the above we have
  $$\int_{\mathbb{R}^n} \frac{\partial f_X(x^n; \theta)}{\partial \theta} dx^n = \int_{\mathbb{R}^n} \frac{\partial \log f_X(x^n; \theta)}{\partial \theta} f_X(x^n; \theta) dx^n$$
  $$= \mathbb{E} \left[ \frac{\partial \log f_X(x^n; \theta)}{\partial \theta} \right] = 0$$
- Differentiating again we have:
  $$\mathbb{E} \left[ \left( \frac{\partial \log f_X(x^n; \theta)}{\partial \theta} \right)^2 \right] = \text{var} \left[ \frac{\partial \log f_X(x^n; \theta)}{\partial \theta} \right] = - \mathbb{E} \left[ \frac{\partial^2 \log f_X(x^n; \theta)}{\partial \theta^2} \right]$$

---

## Pagina 40

Cramér-Rao Bound - Derivation

- Let $\hat{\Theta}(X^n)$ be an estimator of the non-random parameter $\theta$ with:
  $$\mathbb{E} \left[ \Theta(X^n) \right] = \int_{\mathbb{R}^n} \hat{\Theta}(X^n) f_X^n(x^n; \theta) dx^n = \theta + b_n(\theta)

- Differentiating with respect to $\theta$ the above identity we have
  $$\int_{\mathbb{R}^n} \Theta(x^n) \frac{\partial f_X^n(x^n; \theta)}{\partial \theta} dx^n = \int_{\mathbb{R}^n} \frac{\partial \log f_X^n(x^n; \theta)}{\partial \theta} f_X^n(x^n; \theta) dx^n$$
  $$\text{COV} \left[ \Theta(X^n), \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right] = 1 + b_n'(\theta)

- Applying Cauchy-Schwartt’s inequality, we finally have
  $$\left| \text{COV} \left[ \Theta(X^n), \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right] \right|^2 = \left[ 1 + b_n'(\theta) \right]^2 \leq \text{Var} \left[ \Theta(X^n) \right] \text{Var} \left[ \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right]$$

---

## Pagina 41

Elaborating the previous derivations, we obtain an unbeatable lower bound to the variance of any estimator of the non-random parameter $\theta$ in the form:

$$\text{Var} \left[ \Theta(X^n) \right] \geq \frac{[1 + b'_n(\theta)]^2}{\mathbb{E} \left[ \left( \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right)^2 \right]} = \frac{[1 + b'_n(\theta)]^2}{I_n(\theta)}$$

The quantity $I_n(\theta)$ is defined as the Fisher Information, and obeys the following identity:

$$I_n(\theta) = \mathbb{E} \left[ \left( \frac{\partial \log f_X^n(X^n; \theta)}{\partial \theta} \right)^2 \right] = -\mathbb{E} \left[ \frac{\partial^2 \log f_X^n(X^n; \theta)}{\partial \theta^2} \right]$$

---

## Pagina 42

Cramér-Rao Bound - Unbiased Estimators

- As anticipated, the estimator $\Theta(X^n)$ is **unbiased** if $\mathbb{E}[\Theta(X^n)] = \theta$;
- In this situation, we have that
$$\mathbb{E}[(\Theta(X^n) - \theta)^2] = \text{Var}[\Theta(X^n)] \geq \frac{1}{l_n(\theta)}$$

- Thus the Cramér-Rao Bound (CRB) becomes an unbeatable lower bound to the MSE of any estimator.
- An unbiased estimator whose MSE is equal to the CRB is defined **efficient**.
- **Important fact**: If an efficient estimator for a given non-Bayesian estimation problem exists, this necessarily coincides with the ML estimator.

---

## Pagina 43

An example: inferring the cipher frequency of a memoryless source

- Let us consider initially $x^n \in \{0,1\}^n$, drawn from $X^n \sim \mathcal{B}(1,\beta)$, $\beta$ unknown;
- We saw that, if $w(x^n)$ is the Hamming weight of the observed sequence, then:
  $$p_{X^n}(x^n) = \beta^{w(x^n)}(1 - \beta)^{n-w(x^n)}$$

- The ML estimate is thus found as:
  $$\frac{\partial \log p_{X^n}(x^n)}{\partial \beta} = 0 \implies \hat{\beta}_{\text{ML}}(x^n) = \frac{w(x^n)}{n}$$

- The estimator $\beta(X^n) = \frac{w(X^n)}{n}$ is such that:
  $$\mathbb{E}\left[\frac{w(X^n)}{n}\right] = \beta, \quad \text{var}\left[\frac{w(X^n)}{n}\right] = \frac{\beta(1-\beta)}{n}$$

As a consequence, it is unbiased and MS consistent. Is it efficient?

---

## Pagina 44

Notice that we have:

$$\log p_{X^n}(X^n; \beta) = w(X^n) \log \beta + [n - w(X^n)] \log(1 - \beta)$$

Thus we have:

$$\frac{\partial p_{X^n}(X^n; \beta)}{\partial \beta} = \frac{w(X^n)}{\beta} - \frac{n - w(X^n)}{1 - \beta}$$

$$\frac{\partial^2 p_{X^n}(X^n; \beta)}{\partial \beta^2} = -\frac{w(X^n)}{\beta^2} - \frac{n - w(X^n)}{(1 - \beta)^2}$$

Since $\mathbb{E}[w(X^n)] = n\beta$, we have:

$$l_n(\beta) = \frac{n}{\beta} + \frac{n}{1 - \beta} = \frac{n}{\beta(1 - \beta)} \implies \text{CRB} = \frac{\beta(1 - \beta)}{n}$$

We conclude that the MLE of the cipher frequency is efficient.

---

## Pagina 45

Assume now that we have $m$ random parameters, $\theta[\theta_1, \ldots, \theta_m]^T$ drawn from a known pdf $f_{\Theta}(\theta)$ and a data set $x^n$ drawn from a conditional pdf $f_{X^n|\theta}(x^n|\theta)$;

Define a cost function

$$C(\theta - \hat{\theta}) = C(\theta_1 - \hat{\theta}_1, \ldots, \theta_m - \hat{\theta}_m)$$

A Bayes-optimal estimator can be found by solving the minimization problem:

$$\hat{\theta}(x^n) : \mathbb{E}\left[C(\Theta - \hat{\Theta}(X^n))\right] = 0$$

Using the same procedure as for the single-parameter case we thus obtain:

$$\hat{\Theta}(X^n) = \arg \min_{\mathbb{R}^m} C(\theta - \hat{\theta}(X^n))f_{\Theta|X^n}(\theta|X^n)d\theta$$

---

## Pagina 46

The MMSE estimator

- Assume that the cost function is
  $$C(\theta - \hat{\theta}) = \sum_{i=1}^{m} \left( \theta_i - \hat{\theta}_i(x^n) \right)$$
- Since the minimization problem is disjoint (i.e., separable), we have:
  $$\hat{\theta}_i(x^n) = \mathbb{E} \left[ \Theta_i | X^n = x^n \right] = \int \theta_i f_{\theta_i} x^n \left( \theta_i | x^n \right) d\theta_i$$
  whereby the vector MMSE estimator reads:
  $$\hat{\Theta}(X^n) = \mathbb{E} \left[ \Theta | X^n \right]$$

---

## Pagina 47

The MAP estimator

- If we assume
  $$C(\theta - \hat{\theta}) = \sum_{i=1}^{m} \Pi \left( \frac{\theta_i - \hat{\theta}_i(x^n)}{\epsilon} \right)$$
- considering the same procedure we have
  $$\hat{\theta}_i(x^n) : \left. \frac{\partial f_{\Theta}|x^n(\theta|x^n)}{\partial \theta_i} \right|_{\theta_i = \hat{\theta}_i(x^n)} = 0$$
- Equivalently, we have that the MAP estimate solves the equation:
  $$\nabla_{\theta} f_{\Theta}|x^n(\theta|x^n) |_{\theta = \hat{\theta}(x^n)} = 0$$

---

## Pagina 48

Non-Bayesian estimation of multiple parameters

- Assume now that the parameter vector $\theta$ is real and deterministic;
- We may define the log-likelihood function of the observed data, assumed drawn from a distribution family $f_{X^n}(x^n; \theta)$ as:
  $$\Lambda(\theta; x^n) = \log f_{X^n}(x^n, \theta)$$
- We define Maximum-Likelihood estimate of the vector $\theta$ the solution to the equation:
  $$\nabla_\theta \Lambda(\theta; x^n)|_{\theta = \hat{\theta}(x^n)} = 0$$
- The corresponding estimator $\hat{\Theta}(X^n)$ is again defined a Maximum Likelihood (ML) estimator and enjoys a number of fundamental properties.

---

## Pagina 49

Linear MMSE estimators

- Let us start with a simple scalar problem. Assume $x^n$ is the observed sample, drawn from $X^n$, and assume that we want to design a linear estimator of a random parameter $\Theta$, distributed according a known law, in the form:

$$\hat{\Theta}(X^n) = a^T X^n + b \quad a \in \mathbb{R}^n$$

- A Linear MMSE (LMMSE) estimator selects the vector $a$ and the constant $b$ so as to minimize the MMSE

$$\mathbb{E} \left[ (\hat{\Theta}(X^n) - \Theta)^2 \right] = \mathbb{E} \left[ (a^T X^n + b - \Theta)^2 \right]

which is equal to

$$a^T Ra + b^2 + \mathbb{E} \left[ \Theta^2 \right] - 2b(\overline{\Theta}) - 2a^T \mathbb{E} \left[ X^n \Theta \right] - 2ba^T \mathbb{E} \left[ X^n \right]

where $R = \mathbb{E} \left[ X^n X^{nT} \right]$ is the correlation matrix of the random vector $X^n$.

---

## Pagina 50

Nullifying the gradient with respect to $a$ and the derivative with respect to $b$ we obtain:

$$\nabla_a \mathbb{E} \left[ \left( a^T X^n + b - \Theta \right)^2 \right] = 2 M a - 2 \mathbb{E} \left[ X^n \Theta \right] = 0$$

$$\frac{\partial \mathbb{E} \left[ \left( a^T X^n + b - \Theta \right)^2 \right]}{\partial b} = 2 b - 2 \overline{\Theta} - 2 a^T \mathbb{E} \left[ X^n \right] = 0$$

Solving for $b$ yields

$$b_{\text{LMMSE}} = \mathbb{E} \left[ \Theta \right] - a^T \mathbb{E} \left[ X^n \right]$$

$$\widehat{\Theta} \left( X^n \right) = a^T \left( X^n - \mathbb{E} \left[ X^n \right] \right) + \mathbb{E} \left[ \Theta \right]$$

which, placed back into the MSE demonstrates that $a$ should minimize

$$\| a^T \left( X^n - \mathbb{E} \left[ X^n \right] \right) + \left( \Theta - \mathbb{E} \left[ \Theta \right] \right) \|^2$$

As a consequence, denoting $M = \mathbb{E} \left[ \left( X^n - \mathbb{E} \left[ X^n \right] \right) \left( X^n - \mathbb{E} \left[ X^n \right] \right)^T \right]$ the covariance matrix of $X^n$, the LMMSE estimator reads

$$a_{\text{LMMSE}} = M^{-1} \mathbb{E} \left[ \left( X^n - \mathbb{E} \left[ X^n \right] \right) \left( \Theta - \mathbb{E} \left[ \Theta \right] \right) \right] = M^{-1} s$$

---

## Pagina 51

The gradient algorithm

- Assume that we want to solve iteratively the LMMSE problem outlined before;
- We saw that the gradient of the MSE is written as
  $$\nabla_a \mathbb{E} \left[ (a^T X^n + b - \Theta)^2 \right] = 2Ma - 2s$$
  with $\mathbb{E}[X^n \Theta] = s$ known;
- Consider the following iteration to determine $a_{\text{LMMSE}}$:
  $$a^{(n+1)} = a^{(n)} - \gamma \left( Ma^{(n)} - s \right)$$
  which can be rewritten as
  $$a^{(n+1)} = a^{(n)} - \gamma M \left( a^{(n)} - \underbrace{M^{-1} s}_{a_{\text{LMMSE}}} \right)$$

---

## Pagina 52

The Gradient algorithm - cont’d

- The error at the $(n+1)$-th iteration reads
  $$\epsilon^{(n+1)} = a^{(n+1)} - a_{\text{LMMSE}} = a^{(n)} - a_{\text{LMMSE}} - \gamma M \left( a^{(n)} - a_{\text{LMMSE}} \right) = (I - \gamma M) \epsilon^{(n)}$$

- As a consequence we have
  $$\epsilon^{(n+1)} = (I - \gamma M)^n \epsilon^{(1)} = U (I - \gamma \Lambda)^n U^T$$

where $\Lambda$ is the diagonal matrix of the eigenvalues of $M$ and $U$ contains its eigenvectors.

- The error thus converges to zero if the maximum modulus of the eigenvalues of $I - \gamma M$ is smaller than one, i.e.:
  $$-1 < 1 - \gamma \lambda_{\text{MAX}} < 1 \implies 0 < \gamma < \frac{2}{\lambda_{\text{MAX}}}$$

---

## Pagina 53

A different approach: descriptive statistics

- Let us now forget about probability. Let us assume instead to shift to descriptive statistics, wherein the samples count for what they are and are not considered realizations of random vectors:
- We define a training dataset as a collection of $p$ $n$-dimensional samples, which can be organized in the $n \times p$ matrix:

$$X = \begin{bmatrix}
x_1(1) & \cdots & x_1(p) \\
\cdots & \cdots & \cdots \\
x_n(1) & \cdots & x_n(p)
\end{bmatrix} \in \mathbb{R}^{n \times p}$$

- Assume we know $p$ measured values of the parameter $\theta$, each corresponding to one of the $p$ $n$-dimensional samples of the training set, i.e.:

$$y = [\theta(1), \ldots, \theta(p)] \in \mathbb{R}^p$$

- We want to fit the data to a linear model in the form:

$$\theta(i) = a^T x^n(i) + \epsilon_n$$

with $\epsilon_n$ encapsulating the error.

---

## Pagina 54

The Least Squares estimator

Since we have a $p$-dimensional dataset, we want to select $a$ in such a way to minimize:

$$\|\epsilon_n\|^2 = \sum_{i=1}^{p} \left[ a^T x^n(i) - \theta(i) \right]^2$$

Our problem is to select $a$ and $b$ in an optimized way. Notice preliminarily that

$$\sum_{i=1}^{p} \left[ a^T x^n(i) - \theta(i) \right]^2 = \| X^T a - y \|^2$$

Notice that

$$\| X^T a - y \|^2 = a^T X X^T a + \| y \|^2 - 2 a^T X y$$

---

## Pagina 55

The Least Squares estimator - cont’d

- Differentiating with respect to $a$ thus yields
  $$\nabla_a \| X^T a - y \|^2 = 2 X X^T a - 2 X y = 0$$
  which yields
  $$a_{\text{LS}} = (X X^T)^{-1} X y$$
  requiring $(X X^T)$ to be invertible (i.e., $p \ge n$).

- For future reference, let us denote this estimate based on a $p$-dimensional sample as
  $$a_{\text{LS}}(p) = (X(p) X^T(p))^{-1} X(p) y(p)$$

---

## Pagina 56

Assume that we have an infinite-horizon observation of the environment, so that the sample size $p$ may increase;

We consider two scenarios, i.e.:

a. We want to progressively improve our estimate by adding more observations;

b. We want to adapt to possibly changing conditions by "forgetting" old observations in order to weigh new observations more significantly.

We can adjust the LS estimator in such a way as to account for both situations above, and we can do it with limited complexity.

---

## Pagina 57

Assume $p \geq n$ and assume we have evaluated

$$a_{LS}(p) = \left[ X(p) X^T(p) \right]^{-1} X(p) y(p)$$

Assume we have a new vector in the dataset, $x^n(p+1)$ say, and a new observation, $\theta(p+1)$.

The new estimate would be

$$a_{LS}(p+1) = \left[ X(p+1) X^T(p+1) \right]^{-1} X(p+1) y(p+1)$$

Question: Do we have to recompute everything from scratch?

Notice that the inversion operation involves a $\mathcal{O}(n^3)$ complexity, while the matrix product operation has a complexity $\mathcal{O}(np)$ (in terms of multiplications).

---

## Pagina 58

The Sherman-Morrison Formula

- Let $R$ be an invertible matrix of order $n$;
- Let $u$ and $v$ be $n$-dimensional column vectors;
- We have the following matrix inversion lemma with rank-1 update:

$$\left( R + uv^T \right)^{-1} = R^{-1} - \frac{R^{-1}uv^T R^{-1}}{1 + u^T R^{-1}v}$$

---

## Pagina 59

Notice that

$$\underbrace{X(p+1)X^T(p+1)}_{R(p+1)} = \sum_{i=1}^{p+1} x^n(i)x^{nT}(i) = \underbrace{X(p)X^T(p)}_{R(p)} + x^n(p+1)x^{nT}(p+1)$$

As a consequence

$$R^{-1}(p+1) = R^{-1}(p) - \frac{R^{-1}(p)x^n(p+1)x^{nT}(p+1)R^{-1}(p)}{1 + K(p+1)}$$

with

$$K(p+1) = x^{nT}(p+1)R^{-1}(p)x^n(p+1)$$

---

## Pagina 60

On the other hand we have

$$X(p+1) = [X(p) x^n(p+1)] , \quad y(p+1) = [y(p) \theta(p+1)]^T$$

implying

$$X(p+1) y(p+1) = X(p) y(p) + \theta(p+1) x^n(p+1)$$

Since $a(p+1) = R^{-1}(p+1)X(p+1)y(p+1)$, we have

$$a(p+1) = \left[ I_n - \frac{R^{-1}(p) x^n(p+1)}{1 + K(p+1)} x^n T(p+1) \right]$$

$$\left[ a(p) + \theta(p+1) R^{-1}(p) x^n(p+1) \right]$$

which has complexity $\mathcal{O}(n^2)$, independent (and not scaling with $p$).

---

## Pagina 61

In order to cope with situations where the surrounding environment may be (slowly) time-varying, we may want to force "old data" to weigh less than "fresh" data.

A possible way to do so is via exponential smoothing, whose main idea is to adopt the following cost function:

$$\sum_{i=1}^{p} w^{p-i} \left[ a^T x^n(i) - \theta(i) \right]^2$$

The weight $w < 1$ regulates how fast the past is forgotten.

Minimizing with respect to $a$ yields the exponentially smoothed LS:

$$a = \left[ \sum_{i=1}^{p} w^{p-i} x^n(i) x^{nT}(i) \right]^{-1} \sum_{i=1}^{p} w^{p-i} x^n(i) \theta(i)$$

itself amenable to a recursive implementation in the light of Sherman-Morrison lemma.

---

## Pagina 62

Generalization

Assume now that, under the same conditions seen above, we want to find an LS in the more general form

$$\widehat{\theta}(\mathbf{x}^n) = \mathbf{a}^T \mathbf{x}^n + b$$

Lengthy, albeit simple, calculations lead to the general LMS form

$$\mathbf{a}_{\text{LMS}} = \left( X_0 X_0^T \right)^{-1} X_0 y_0, \quad b_{\text{LMS}} = \underbrace{\frac{1}{p} \sum_{i=1}^{p} \theta(i)}_{\widehat{\theta}} - \frac{1}{p} \mathbf{1}_p^T \mathbf{X}^T \mathbf{a}_{\text{LMS}}$$

where $\mathbf{1}_p$ is an all-one $p$-dimensional vector and

$$\mathbf{X}_0 = \begin{bmatrix} x_1(1) - \bar{x}_1 & \dots & x_1(p) - \bar{x}_1 \\ \dots & \dots & \dots \\ x_n(1) - \bar{x}_n & \dots & x_n(p) - \bar{x}_n \end{bmatrix} \in \mathbb{R}^{n \times p}, \quad \mathbf{y}_0 = \left[ y_1 - \bar{\theta}, \dots, y_p - \bar{\theta} \right]^T$$

with

$$\bar{x}_k = \frac{1}{p} \sum_{i=1}^{p} x_k(i) \iff \bar{x} = \frac{1}{p} \sum_{i=1}^{p} x^n(i), \quad \mathbf{X}_0 = \mathbf{X} - \bar{x} \mathbf{1}_p^T$$

---

