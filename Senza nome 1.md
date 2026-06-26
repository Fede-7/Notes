── PAGE 1 / 20 ──
Generalities - Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation
Almost sure convergence - cont'd
- Consider now a value \(a_{i}\) for which \(q(a_{i}) \neq p_{X}(a_{i})\).
- When \( n \) grows large we have:
\[
\begin{array}{l} \operatorname * {P r} \left\{N _ {i} = n q (a _ {i}) \right\} \sim 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} p _ {X} (a _ {i}) ^ {n q (a _ {i})} [ 1 - p _ {X} (a _ {i}) ] ^ {n (1 - q (a _ {i}))} \\ = 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} 2 ^ {n [ q (a _ {i}) \log p _ {X} (a _ {i}) + (1 - q (a _ {i})) \log (1 - p _ {X} (a _ {i})) ]} \\ = 2 ^ {n \left[ q (a _ {i}) \log \frac {p _ {X} (a _ {i})}{q (a _ {i})} + (1 - q (a _ {i})) \log \frac {1 - p _ {X} (a _ {i})}{1 - q (a _ {i})} \right]} = 2 ^ {- n D _ {i}} \\ \end{array}
\]
with
\[
D _ {i} = q (a _ {i}) \log \frac {q (a _ {i})}{p _ {X} (a _ {i})} + [ 1 - q (a _ {i}) ] \log \frac {1 - q (a _ {i})}{1 - p _ {X} (a _ {i})} > 0
\]
We thus conclude that the probability that the frequency of occurrence does not equal the true probability goes to zero exponentially with n.
This implies that  \( f_{n}(a_{i}) \rightarrow p_{X}(a_{i}) \)  almost surely.
Marco Lops lops@unina.it https://docenti.unina.it/marco.lops
Metodi Statistici per l'Informazione - Marco Lops
7/62
── PAGE 2 / 20 ──
Generalities - Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation
Binary classification: continuous data law
- Assume now that the data may be drawn from \(M\) possible continuous probability laws, whereby we are given a set of candidate conditional probability density functions \(\{f_{\mathbf{X}^n|H_i}(\mathbf{x}^n|H_i)\}_{i=1}^M\);
The only difference with the discrete case is case is that now
\[
\mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {1} | H _ {1} \right\} = \int_ {\Omega_ {1}} f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) d \boldsymbol {x} ^ {n} \quad \mathbb {P} \left\{\boldsymbol {X} ^ {n} \in \Omega_ {2} | H _ {2} \right\} = \int_ {\Omega_ {2}} f _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2}) d \boldsymbol {x} ^ {n}
\]
Thus, following the same line of thought as for the discrete case, we obtain that the minimum error probability test is written as
\[
\boldsymbol {x} ^ {n} \in \Omega_ {i} \text {   iff   } f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) P (H _ {1}) > f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} | H _ {2}) P (H _ {2})
\]
or equivalently
\[
L (\boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (\boldsymbol {x} ^ {n} | H _ {1}) \underset {\approx} {H _ {1}} P (H _ {2})}{f _ {\boldsymbol {X} ^ {n} | H _ {2}} (\boldsymbol {x} ^ {n} | H _ {2}) \underset {H _ {2}} {\approx} P (H _ {1})} = \eta
\]
- The quantity \( L(\boldsymbol{x}^n) \) on the LHS is again called likelihood ratio between the two alternative hypotheses.
Marco Lops lops@unina.it https://docenti.unina.it/marco.lops
Metodi Statistici per l'Informazione - Marco Lops
17/62
── PAGE 3 / 20 ──
Generalities - Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation
Neyman-Pearson Test
- Given the framework outlined in the previous slide, a Neyman-Pearson test is the result of the following constrained optimization:
\[
\text { Determine } \Omega_ {1}: \quad \left\{ \begin{array}{l l} 1 - \beta & \text { maximum } \\ \text { subject   to } & \text { type - 1   error } \leq \alpha \end{array} \right.
\]
- The existence of the solution of such a constrained problem is the bulk of the Neyman-Pearson lemma;
The resulting test is the likelihood ratio test
\[
L \left(\boldsymbol {x} ^ {n}\right) \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta L \left(\boldsymbol {x} ^ {n}\right) = \left\{ \begin{array}{c c} \frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} \left(\boldsymbol {x} ^ {n} | H _ {1}\right)}{f _ {\boldsymbol {X} ^ {n} | H _ {0}} \left(\boldsymbol {x} ^ {n} | H _ {0}\right)} & \text { Continuous   data } \\ \frac {p _ {\boldsymbol {X} ^ {n} | H _ {1}} \left(\boldsymbol {x} ^ {n} | H _ {1}\right)}{\frac {p _ {\boldsymbol {X} ^ {n} | H _ {0}} \left(\boldsymbol {x} ^ {n} | H _ {0}\right)}} & \text { Discrete   data } \end{array} \right.
\]
The threshold  \( \eta \)  should be chosen as the solution to the equation:
\[
\mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) > \eta | H _ {0} \right\} = \alpha
\]
Notice that applying any monotonically increasing function to both sides of the previous test does not alter its optimality, whereby we can equivalently introduce the log-likelihood  \( \ln L(\boldsymbol{x}^{n}) = \Lambda(\boldsymbol{x}^{n}) \)  and compare it to a newly determined threshold.
Marco Lops lop@unina.it https://docenti.unina.it/marco.lops
Metodi Statistici per l'Informazione - Marco Lops
22 / 62
── PAGE 4 / 20 ──
Generalities - Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation
Estimator Performance: Systematic error (Bias)
- Let us preliminarily notice that:
\[
\mathbb {E} [ B ] = \int_ {0} ^ {1} \beta d \beta = \frac {1}{2}, \quad \mathbb {E} [ B ^ {2} ] = \frac {1}{3}, \quad \sigma_ {B} ^ {2} = \frac {1}{1 2}
\]
Since
\[
\mathbb {E} \left[ w (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \overbrace {\mathbb {E} \left[ w (\boldsymbol {X} ^ {n}) | B \right]} ^ {n B} \right] = \frac {n}{2}, \quad \mathbb {E} \left[ w ^ {2} (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \overbrace {\mathbb {E} \left[ w (\hat {\boldsymbol {X}} ^ {n}) | B \right]} ^ {n B (1 - B) + n ^ {2} B ^ {2}} \right] = \frac {n}{6} + \frac {n ^ {2}}{3}
\]
whereby \(\sigma_{w(X^n)}^2 = \frac{n}{6}\left(1 + \frac{n}{2}\right)\).
For the MMSEE:
\[
\mathbb {E} \left[ \hat {B} _ {\mathrm{MMSE}} (\boldsymbol {X} ^ {n}) | B = \beta \right] = \frac {n \beta + 1}{n + 2}, \qquad \mathbb {E} \left[ \hat {B} _ {\mathrm{MMSE}} (\boldsymbol {X} ^ {n}) \right] = \frac {\frac {n}{2} + 1}{n + 2}
\]
For the MAPE:
\[
\mathbb {E} \left[ \hat {B} _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) | B = \beta \right] = \beta , \qquad \mathbb {E} \left[ \hat {B} _ {\mathrm{MAP}} (\boldsymbol {X} ^ {n}) \right] = \frac {\frac {n}{2}}{n} = \frac {1}{2}
\]
We conclude that the MMSEE is a biased estimator, while the MAP is not;
Notice that the MMSEE is asymptotically unbiased, since the systematic error vanishes as n grows large.
Marco Lops lop@unina.it https://docenti.unina.it/marco.lops
Metodi Statistici per l'Informazione - Marco Lops
31 / 62
── PAGE 5 / 20 ──
Generalities - Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation
Cramér-Rao Bound - Derivation
Let \(\widehat{\Theta} (\pmb {X}^n)\) be an estimator of the non-random parameter \(\theta\) with:
\[
\mathbb {E} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \int_ {\mathbb {R} ^ {n}} \widehat {\Theta} (\boldsymbol {X} ^ {n}) f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta) d \boldsymbol {x} ^ {n} = \theta + b _ {n} (\theta)
\]
Differentiating with respect to \(\theta\) the above identity we have
\[
\begin{array}{l} \int_ {\mathbb {R} ^ {n}} \Theta (\boldsymbol {x} ^ {n}) \frac {\partial f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} d \boldsymbol {x} ^ {n} = \overbrace {\int_ {\mathbb {R} ^ {n}} \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta) d \boldsymbol {x} ^ {n}} ^ {\mathbb {E} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right]} \\ \operatorname{COV} \left[ \Theta (\boldsymbol {x} ^ {n}), \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} \right] = 1 + b _ {n} ^ {\prime} (\theta) \end{array}
\]
Applying Cauchy-Schwart's inequality, we finally have
\[
\left| \operatorname{COV} \left[ \Theta (\boldsymbol {X} ^ {n}), \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] \right| ^ {2} = \left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2} \leq \operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] \operatorname{Var} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right]
\]
Marco Lops lops@unina.it https://docenti.unina.it/marco.lops
Metodi Statistici per l'Informazione - Marco Lops
40 / 62
── PAGE 6 / 20 ──
Generalities - Marco Lops Elements of Decision Theory Elements of estimation theory Linear MMSE Estimation
Generalization
- Assume now that, under the same conditions seen above, we want to find an LS in the more general form
\[
\widehat {\theta} \left(\boldsymbol {x} ^ {n}\right) = \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} + \boldsymbol {b}
\]
• Lengthy, albeit simple, calculations lead to the general LMS form
\[
\boldsymbol {a} _ {\mathrm{LMS}} = (\boldsymbol {X} _ {0} \boldsymbol {X} _ {0} ^ {T}) ^ {- 1} \boldsymbol {X} _ {0} \boldsymbol {y} _ {0}, \quad b _ {\mathrm{LMS}} = \underbrace {\frac {1}{p} \sum_ {i = 1} ^ {p} \theta (i)} _ {\overline {{\theta}}} - \frac {1}{p} \mathbf {1} _ {p} ^ {T} \boldsymbol {X} ^ {T} \boldsymbol {a} _ {\mathrm{LMS}}
\]
where  \( 1_{p} \)  is an all-one p-dimensional vector and
\[
\boldsymbol {X} _ {0} = \left[ \begin{array}{c c c} x _ {1} (1) - \overline {{x}} _ {1} & \dots & x _ {1} (p) - \overline {{x}} _ {1} \\ \dots & \dots & \dots \\ x _ {n} (1) - \overline {{x}} _ {n} & \dots & x _ {n} (p) - \overline {{x}} _ {n} \end{array} \right] \in \mathbb {R} ^ {n \times p}, \quad \boldsymbol {y} _ {0} = \left[ y _ {1} - \overline {{\theta}}, \dots , y _ {p} - \overline {{\theta}} \right] ^ {T}
\]
with
\[
\overline {{x}} _ {k} = \frac {1}{p} \sum_ {i = 1} ^ {p} x _ {k} (i) \Longleftrightarrow \overline {{\boldsymbol {x}}} = \frac {1}{p} \sum_ {i = 1} ^ {p} \boldsymbol {x} ^ {n} (i), \quad \boldsymbol {X} _ {0} = \boldsymbol {X} - \overline {{\boldsymbol {x}}} \mathbf {1} _ {p} ^ {T}
\]
Marco Lops lop@unina.it https://docenti.unina.it/marco.lops
Metodi Statistici per l'Informazione - Marco Lops
62 / 62
── PAGE 7 / 20 ──
4.2 Types of Random Variables
93
![](images/0.jpg)

FIGURE 4.1 Graph of \((p)x\), Example 4.2a.
![](images/1.jpg)

FIGURE 4.2 Graph of \( F(x) \).
For instance, suppose \( X \) has a probability mass function given (as in Example 4.2a) by
\[
p (1) = \frac {1}{2}, \qquad p (2) = \frac {1}{3}, \qquad p (3) = \frac {1}{6}
\]
then the cumulative distribution function \(F\) of \(X\) is given by
\[
F (a) = \left\{ \begin{array}{l l} 0 & a <   1 \\ \frac {1}{2} & 1 \leq a <   2 \\ \frac {3}{6} & 2 \leq a <   3 \\ 1 & 3 \leq a \end{array} \right.
\]
This is graphically presented in Figure 4.2.
Whereas the set of possible values of a discrete random variable is a sequence, we often must consider random variables whose set of possible values is an interval. Let \( X \) be such a random variable. We say that \( X \) is a continuous random variable if there exists a nonnegative function \( f(x) \), defined for all real \( x \in (-\infty, \infty) \), having the property that for any set \( B \) of real numbers
\[
P \{X \in B \} = \int_ {B} f (x) d x \tag {4.2.1}
\]
The function \( f(x) \) is called the probability density function of the random variable \( X \).
── PAGE 8 / 20 ──
94
Chapter 4: Random Variables and Expectation
In words, Equation 4.2.1 states that the probability that \( X \) will be in \( B \) may be obtained by integrating the probability density function over the set \( B \). Since \( X \) must assume some value, \( f(x) \) must satisfy
\[
1 = P \{X \in (- \infty , \infty) \} = \int_ {- \infty} ^ {\infty} f (x) d x
\]
All probability statements about \( X \) can be answered in terms of \( f(x) \). For instance, letting \( B = [a, b] \), we obtain from Equation 4.2.1 that
\[
P \{a \leq X \leq b \} = \int_ {a} ^ {b} f (x) d x \tag {4.2.2}
\]
If we let \( a = b \) in the above, then
\[
P \{X = a \} = \int_ {a} ^ {a} f (x) d x = 0
\]
In words, this equation states that the probability that a continuous random variable will assume any particular value is zero. (See Figure 4.3.)
The relationship between the cumulative distribution \( F(\cdot) \) and the probability density \( f(\cdot) \) is expressed by
\[
F (a) = P \{X \in (- \infty , a ] \} = \int_ {- \infty} ^ {a} f (x) d x
\]
Differentiating both sides yields
\[
\frac {d}{d a} F (a) = f (a)
\]
![](images/0.jpg)

FIGURE 4.3 The probability density function \( f(x) = \begin{cases} e^{-x} & x \geq 0 \\ 0 & x < 0 \end{cases} \).
── PAGE 9 / 20 ──
(no text detected)
── PAGE 10 / 20 ──
(no text detected)
── PAGE 11 / 20 ──
(no text detected)
── PAGE 12 / 20 ──
(no text detected)
── PAGE 13 / 20 ──
(no text detected)
── PAGE 14 / 20 ──
(no text detected)
── PAGE 15 / 20 ──
(no text detected)
── PAGE 16 / 20 ──
(no text detected)
── PAGE 17 / 20 ──
(no text detected)
── PAGE 18 / 20 ──
(no text detected)
── PAGE 19 / 20 ──
(no text detected)
── PAGE 20 / 20 ──
(no text detected)
