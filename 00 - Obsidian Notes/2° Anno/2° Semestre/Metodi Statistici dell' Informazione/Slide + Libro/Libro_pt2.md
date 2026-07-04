or, equivalently, 

$$
P \left\{\overline {{X}} - \overline {{Y}} - z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}} <   \mu_ {1} - \mu_ {2} <   \overline {{X}} - \overline {{Y}} + z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}} \right\} = 1 - \alpha
$$

Hence, if X and $\overline { { Y } }$ are observed to equal x and y, respectively, then a 100(1 − α) twosided confidence interval estimate for $\mu _ { 1 } - \mu _ { 2 }$ is 

$$
\mu_ {1} - \mu_ {2} \in \left(\bar {x} - \bar {y} - z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}}, \bar {x} - \bar {y} + z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}}\right)
$$

One-sided confidence intervals for $\mu _ { 1 } - \mu _ { 2 }$ are obtained in a similar fashion, and we leave it for the reader to verify that a $1 0 0 ( 1 - \alpha )$ percent one-sided interval is given by 

$$
\mu_ {1} - \mu_ {2} \in \left(- \infty , \overline {{x}} - \overline {{y}} + z _ {\alpha} \sqrt {\sigma_ {1} ^ {2} / n + \sigma_ {2} ^ {2} / m}\right)
$$

Program 7.4.1 will compute both one- and two-sided confidence intervals for $\mu _ { 1 } - \mu _ { 2 }$ 

EXAMPLE 7.4a Two different types of electrical cable insulation have recently been tested to determine the voltage level at which failures tend to occur. When specimens were subjected to an increasing voltage stress in a laboratory experiment, failures for the two types of cable insulation occurred at the following voltages: 

<table><tr><td colspan="2">Type A</td><td colspan="2">Type B</td></tr><tr><td>36</td><td>54</td><td>52</td><td>60</td></tr><tr><td>44</td><td>52</td><td>64</td><td>44</td></tr><tr><td>41</td><td>37</td><td>38</td><td>48</td></tr><tr><td>53</td><td>51</td><td>68</td><td>46</td></tr><tr><td>38</td><td>44</td><td>66</td><td>70</td></tr><tr><td>36</td><td>35</td><td>52</td><td>62</td></tr><tr><td>34</td><td>44</td><td></td><td></td></tr></table>

Suppose that it is known that the amount of voltage that cables having type A insulation can withstand is normally distributed with unknown mean $\mu _ { A }$ and known variance $\sigma _ { A } ^ { 2 } = 4 0$ , whereas the corresponding distribution for type B insulation is normal with unknown mean $\mu _ { B }$ and known variance $\sigma _ { B } ^ { 2 } = 1 0 0$ . Determine a 95 percent confidence interval for $\mu _ { A } - \mu _ { B }$ . Determine a value that we can assert, with 95 percent confidence, exceed $\mu _ { A } - \mu _ { B } .$ 

SOLUTION We run Program 7.4.1 to obtain the solution (see Figure 7.4). ■ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/463ab9c9ffd514c83d2b0b50c0c2b3a4acdcae1ed1d454f5477461000087e40b.jpg)



(a)



FIGURE 7.4 (a) Two-sided and (b) lower 95 percent confidence intervals for Example 7.4a.


Let us suppose now that we again desire an interval estimator of $\mu _ { 1 } - \mu _ { 2 }$ but that the population variances $\sigma _ { 1 } ^ { 2 }$ and $\sigma _ { 2 } ^ { 2 }$ are unknown. In this case, it is natural to try to replace $\bar { \sigma } _ { 1 } ^ { 2 }$ and $\sigma _ { 2 } ^ { 2 }$ in Equation 7.4.1 by the sample variance 

$$
S _ {1} ^ {2} = \sum_ {i = 1} ^ {n} \frac {(X _ {i} - \overline {{X}}) ^ {2}}{n - 1}
$$

$$
S _ {2} ^ {2} = \sum_ {i = 1} ^ {m} \frac {(Y _ {i} - \overline {{Y}}) ^ {2}}{m - 1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/df7fdf48ffcb7fb7c780c77f473b19623b1c91a1b5353f69175e9b61056f4e8d.jpg)



(b)



FIGURE 7.4 (continued)



That is, it is natural to base our interval estimate on something like


$$
\frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sqrt {S _ {1} ^ {2} / n + S _ {2} ^ {2} / m}}
$$

However, to utilize the foregoing to obtain a confidence interval, we need its distribution and it must not depend on any of the unknown parameters $\sigma _ { 1 } ^ { 2 }$ and $\sigma _ { 2 } ^ { 2 }$ . Unfortunately, this distribution is both complicated and does indeed depend on the unknown parameters $\sigma _ { 1 } ^ { 2 }$ and $\sigma _ { 2 } ^ { 2 }$ . In fact, it is only in the special case when $\sigma _ { 1 } ^ { \dot { 2 } } = \sigma _ { 2 } ^ { 2 }$ that we will be able to obtain an interval estimator. So let us suppose that the population variances, though unknown, are equal and let $\sigma ^ { 2 }$ denote their common value. Now, from Theorem 6.5.1 it follows that 

$$
(n - 1) \frac {S _ {1} ^ {2}}{\sigma^ {2}} \sim \chi_ {n - 1} ^ {2}
$$

and 

$$
(m - 1) \frac {S _ {2} ^ {2}}{\sigma^ {2}} \sim \chi_ {m - 1} ^ {2}
$$

Also, because the samples are independent, it follows that these two chi-square random variables are independent. Hence, from the additive property of chi-square random variables, which states that the sum of independent chi-square random variables is also chi-square with a degree of freedom equal to the sum of their degrees of freedom, it follows that 

$$
(n - 1) \frac {S _ {1} ^ {2}}{\sigma^ {2}} + (m - 1) \frac {S _ {2} ^ {2}}{\sigma^ {2}} \sim \chi_ {n + m - 2} ^ {2}\tag{7.4.2}
$$

Also, since 

$$
\overline {{{X}}} - \overline {{{Y}}} \sim \mathcal {N} \left(\mu_ {1} - \mu_ {2}, \frac {\sigma^ {2}}{n} + \frac {\sigma^ {2}}{m}\right)
$$

we see that 

$$
\frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma^ {2}}{n} + \frac {\sigma^ {2}}{m}}} \sim \mathcal {N} (0, 1)\tag{7.4.3}
$$

Now it follows from the fundamental result that in normal sampling $\overline { { X } }$ and $S ^ { 2 }$ are independent (Theorem 6.5.1), that $\overline { { X } } _ { 1 } , S _ { 1 } ^ { 2 } , \overline { { X } } _ { 2 } , S _ { 2 } ^ { 2 }$ are independent random variables. Hence, using the definition of a t-random variable (as the ratio of two independent random vari ables, the numerator being a standard normal and the denominator being the square root of a chi-square random variable divided by its degree of freedom parameter), it follows from Equations 7.4.2 and 7.4.3 that if we let 

$$
S _ {p} ^ {2} = \frac {(n - 1) S _ {1} ^ {2} + (m - 1) S _ {2} ^ {2}}{n + m - 2}
$$

then 

$$
\frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sqrt {\sigma^ {2} (1 / n + 1 / m)}} \div \sqrt {S _ {p} ^ {2} / \sigma^ {2}} = \frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sqrt {S _ {p} ^ {2} (1 / n + 1 / m)}}
$$

has a t -distribution with $n + m - 2$ degrees of freedom. Consequently, 

$$
P \left\{- t _ {\alpha / 2, n + m - 2} \leq \frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{S _ {p} \sqrt {1 / n + 1 / m}} \leq t _ {\alpha / 2, n + m - 2} \right\} = 1 - \alpha
$$

Therefore, when the data result in the values $\overline { { { X } } } = \overline { { { x } } } , \overline { { { Y } } } = \overline { { { y } } } , S _ { \phi } = s _ { p } ,$ , we obtain the following $1 0 0 ( 1 - \alpha )$ percent confidence interval for $\mu _ { 1 } - \mu _ { 2 } { \mathrm { : } }$ 

$$
\left(\overline {{x}} - \overline {{y}} - t _ {\alpha / 2, n + m - 2} s _ {p} \sqrt {1 / n + 1 / m}, \quad \overline {{x}} - \overline {{y}} + t _ {\alpha / 2, n + m - 2} s _ {p} \sqrt {1 / n + 1 / m}\right)\tag{7.4.4}
$$

One-sided confidence intervals are similarly obtained. 

Program 7.4.2 can be used to obtain both one- and two-sided confidence intervals for the difference in means in two normal populations having unknown but equal variances. 

EXAMPLE 7.4b There are two different techniques a given manufacturer can employ to produce batteries. A random selection of 12 batteries produced by technique I and of 14 produced by technique II resulted in the following capacities (in ampere hours): 

<table><tr><td colspan="2">Technique I</td><td colspan="2">Technique II</td></tr><tr><td>140</td><td>132</td><td>144</td><td>134</td></tr><tr><td>136</td><td>142</td><td>132</td><td>130</td></tr><tr><td>138</td><td>150</td><td>136</td><td>146</td></tr><tr><td>150</td><td>154</td><td>140</td><td>128</td></tr><tr><td>152</td><td>136</td><td>128</td><td>131</td></tr><tr><td>144</td><td>142</td><td>150</td><td>137</td></tr><tr><td></td><td></td><td>130</td><td>135</td></tr></table>

Determine a 90 percent level two-sided confidence interval for the difference in means, assuming a common variance. Also determine a 95 percent upper confidence interval for $\mu _ { \mathrm { I } } - \mu _ { \mathrm { I I } }$ 

SOLUTION We run Program 7.4.2 to obtain the solution (see Figure 7.5). ■ 

## REMARK

The confidence interval given by Equation 7.4.4 was obtained under the assumption that the population variances are equal; with $\sigma ^ { 2 }$ as their common value, it follows that 

$$
\frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sqrt {\sigma^ {2} / n + \sigma^ {2} / m}} = \frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sigma \sqrt {1 / n + 1 / m}}
$$

has a standard normal distribution. However, since $\sigma ^ { 2 }$ is unknown this result cannot be immediately applied to obtain a confidence interval; $\sigma ^ { 2 }$ must first be estimated. To do so, note that both sample variances are estimators of $\cdot \sigma ^ { 2 }$ ; moreover, since $S _ { 1 } ^ { 2 }$ has $n - 1$ degrees of freedom and $S _ { 2 } ^ { 2 }$ has $m - 1$ , the appropriate estimator is to take a weighted average of the two sample variances, with the weights proportional to these degrees of freedom. That is, 

the estimator of $\sigma ^ { 2 }$ is the pooled estimator 

$$
S _ {p} ^ {2} = \frac {(n - 1) S _ {1} ^ {2} + (m - 1) S _ {2} ^ {2}}{n + m - 2}
$$

and the confidence interval is then based on the statistic 

$$
\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})
$$

$$
\sqrt {S _ {p} ^ {2}} \sqrt {1 / n + 1 / m}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/f375df66631bf20963fe3d702f7a9687c9d2965d60c0e8d5866eb16533f23e16.jpg)



(a)



FIGURE 7.5 (a) Two-sided and (b) upper 90 percent confidence intervals for Example 7.4b.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/cb3c4ccae6fde03e95120f483cb61beab810ee1c364faab6ed2a2d8de554015a.jpg)



(b)



FIGURE 7.5 (continued)


which, by our previous analysis, has a t-distribution with n + m − 2 degrees of freedom. The results of this section are summarized up in Table 7.2. 

## 7.5 APPROXIMATE CONFIDENCE INTERVAL FOR THE MEAN OF A BERNOULLI RANDOM VARIABLE

Consider a population of items, each of which independently meets certain standards with some unknown probability p. If n of these items are tested to determine whether they meet the standards, how can we use the resulting data to obtain a confidence interval for p? 

If we let X denote the number of the n items that meet the standards, then X is a binomial random variable with parameters n and p. Thus, when n is large, it follows by 

TABLE 7.2 $1 0 0 ( 1 - \sigma )$ Percent Confidence Intervals for $\mu _ { 1 } - \mu _ { 2 }$ 

$$
X _ {1}, \ldots , X _ {n} \sim N (\mu_ {1}, \sigma_ {1} ^ {2})
$$

$$
Y _ {1}, \ldots , Y _ {m} \sim N (\mu_ {2}, \sigma_ {2} ^ {2})
$$

$$
\overline {{X}} = \sum_ {i = 1} ^ {n} X _ {i} / n, S _ {1} ^ {2} = \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2} / (n - 1)
$$

$$
\overline {{Y}} = \sum_ {i = 1} ^ {m} Y _ {i} / n, \qquad S _ {2} ^ {2} = \sum_ {i = 1} ^ {m} (Y _ {i} - \overline {{Y}}) ^ {2} / (m - 1)
$$

## Assumption

$\sigma _ { 1 } , \sigma _ { 2 }$ known 

$$
\overline {{X}} - \overline {{Y}} \pm z _ {\alpha / 2} \sqrt {\sigma_ {1} ^ {2} / n + \sigma_ {2} ^ {2} / m}
$$

σ<sub>1</sub>, σ<sub>2</sub> unknown but equal 

$$
\overline {{X}} - \overline {{Y}} \pm t _ {\alpha / 2, n + m - 2} \sqrt {\left(\frac {1}{n} + \frac {1}{m}\right) \frac {(n - 1) S _ {1} ^ {2} + (m - 1) S _ {2} ^ {2}}{n + m - 2}}
$$

## Assumption

$\sigma _ { 1 } , \sigma _ { 2 }$ known 

$$
(- \infty , \overline {{X}} - \overline {{Y}} + z _ {\alpha} \sqrt {\sigma_ {1} ^ {2} / n + \sigma_ {2} ^ {2} / m})
$$

$\sigma _ { 1 } , \sigma _ { 2 }$ unknown but equal 

$$
\left(- \infty , \overline {{X}} - \overline {{Y}} + t _ {\alpha , n + m - 2} \sqrt {\left(\frac {1}{n} + \frac {1}{m}\right) \frac {(n - 1) S _ {1} ^ {2} + (m - 1) S _ {2} ^ {2}}{n + m - 2}}\right)
$$

Note: Upper confidence intervals for $\mu _ { 1 } - \mu _ { 2 }$ are obtained from lower confidence intervals fo $\mu _ { 2 } - \mu _ { 1 }$ 

the normal approximation to the binomial that X is approximately normally distributed with mean np and variance $n p ( 1 - p )$ . Hence, 

$$
\frac {X - n p}{\sqrt {n p (1 - p)}} \dot {\sim} \mathcal {N} (0, 1)\tag{7.5.1}
$$

where $\dot { \sim }$ means “is approximately distributed as.” Therefore, for any $\alpha \in ( 0 , 1 )$ ), 

$$
P \left\{- z _ {\alpha / 2} <   \frac {X - n p}{\sqrt {n p (1 - p)}} <   z _ {\alpha / 2} \right\} \approx 1 - \alpha
$$

and so if X is observed to equal $x ,$ then an approximate $1 0 0 ( 1 - \alpha )$ percent confidence region for $\boldsymbol { \mathscr { P } }$ is 

$$
\left\{p: - z _ {\alpha / 2} <   \frac {x - n p}{\sqrt {n p (1 - p)}} <   z _ {\alpha / 2} \right\}
$$

The foregoing region, however, is not an interval. To obtain a confidence interval for ${ \boldsymbol { p } } ,$ let ${ \hat { p } } = X / n$ be the fraction of the items that meet the standards. From Example 7.2a, $\hat { \boldsymbol { p } }$ is the maximum likelihood estimator of ${ \boldsymbol { p } } ,$ , and so should be approximately equal to $\scriptstyle { \boldsymbol { p } } .$ . As a result, $\sqrt { n \hat { p } ( 1 - \hat { p } ) }$ will be approximately equal to $\sqrt { n p ( 1 - p ) }$ and so from Equation 7.5.1 we see that 

$$
\frac {X - n p}{\sqrt {n \hat {p} (1 - \hat {p})}} \dot {\sim} \mathcal {N} (0, 1)
$$

Hence, for any $\alpha \in ( 0 , 1 )$ we have that 

$$
P \left\{- z _ {\alpha / 2} <   \frac {X - n p}{\sqrt {n \hat {p} (1 - \hat {p})}} <   z _ {\alpha / 2} \right\} \approx 1 - \alpha
$$

or, equivalently, 

$$
P \{- z _ {\alpha / 2} \sqrt {n \hat {p} (1 - \hat {p})} <   n p - X <   z _ {\alpha / 2} \sqrt {n \hat {p} (1 - \hat {p})} \} \approx 1 - \alpha
$$

Since ${ \hat { p } } = X / n ,$ the preceding can be written as 

$$
P \{\hat {p} - z _ {\alpha / 2} \sqrt {\hat {p} (1 - \hat {p}) / n} <   p <   \hat {p} + z _ {\alpha / 2} \sqrt {\hat {p} (1 - \hat {p}) / n} \} \approx 1 - \alpha
$$

which yields an approximate $1 0 0 ( 1 - \alpha )$ percent confidence interval for $\boldsymbol { \underline b }$ 

EXAMPLE 7.5a A sample of 100 transistors is randomly chosen from a large batch and tested to determine if they meet the current standards. If 80 of them meet the standards, then an approximate 95 percent confidence interval for $\scriptstyle { \dot { \boldsymbol { p } } } ,$ , the fraction of all the transistors that meet the standards, is given by 

$$
(. 8 - 1. 9 6 \sqrt {. 8 (. 2) / 1 0 0},. 8 + 1. 9 6 \sqrt {. 8 (. 2) / 1 0 0}) = (. 7 2 1 6,. 8 7 8 4)
$$

That is, with $^ { \mathfrak { a } } 9 5$ percent confidence,” between 72.16 and 87.84 percent of all transistors meet the standards. ■ 

EXAMPLE 7.5b On October 14, 2003, the New York Times reported that a recent poll indicated that 52 percent of the population was in favor of the job performance of President Bush, with a margin of error of ±4 percent. What does this mean? Can we infer how many people were questioned? 

SOLUTION It has become common practice for the news media to present 95 percent confidence intervals. Since $z _ { . 0 2 5 } ~ = ~ 1 . 9 6 , \mathrm { ~ a ~ } 9 5$ percent confidence interval for ${ \boldsymbol { p } } ,$ the percentage of the population that is in favor of President Bush’s job performance, is given by 

$$
\hat {p} \pm 1. 9 6 \sqrt {\hat {p} (1 - \hat {p}) / n} = . 5 2 \pm 1. 9 6 \sqrt {. 5 2 (. 4 8) / n}
$$

where n is the size of the sample. Since the “margin of error” is $\pm 4$ percent, it follows that 

$$
1. 9 6 \sqrt {. 5 2 (. 4 8) / n} = . 0 4
$$

or 

$$
n = \frac {(1 . 9 6) ^ {2} (. 5 2) (. 4 8)}{(. 0 4) ^ {2}} = 5 9 9. 2 9
$$

That is, approximately 599 people were sampled, and 52 percent of them reported favorably on President Bush’s job performance. ■ 

We often want to specify an approximate 100(1 − α) percent confidence interval for $\boldsymbol { \mathit { p } }$ that is no greater than some given length, say b. The problem is to determine the appropriate sample size n to obtain such an interval. To do so, note that the length of the approximate $1 0 0 ( 1 - \alpha )$ percent confidence interval for $\boldsymbol { \mathit { p } }$ from a sample of size n is 

$$
2 z _ {\alpha / 2} \sqrt {\hat {p} (1 - \hat {p}) / n}
$$

which is approximately equal to $2 z _ { \alpha / 2 } \sqrt { p ( 1 - p ) / n }$ . Unfortunately, $\boldsymbol { \mathscr { P } }$ is not known in advance, and so we cannot just set $2 z _ { \alpha / 2 } \sqrt { p ( 1 - p ) / n }$ equal to $b$ to determine the necessary sample size n. What we can do, however, is to first take a preliminary sample to obtain a rough estimate o $\dot { \mathbf { \rho } } _ { p } ,$ and then use this estimate to determine $n .$ . That is, we use $\boldsymbol { p } ^ { * }$ , the proportion of the preliminary sample that meets the standards, as a preliminary estimate of ${ \dot { p } } ;$ we then determine the total sample size n by solving the equation 

$$
2 z _ {\alpha / 2} \sqrt {p ^ {*} (1 - p ^ {*}) / n} = b
$$

Squaring both sides of the preceding yields that 

$$
(2 z _ {\alpha / 2}) ^ {2} p ^ {*} (1 - p ^ {*}) / n = b ^ {2}
$$

or 

$$
n = \frac {(2 z _ {\alpha / 2}) ^ {2} p ^ {*} (1 - p ^ {*})}{b ^ {2}}
$$

That is, if $k$ items were initially sampled to obtain the preliminary estimate of ${ \dot { \mathbf { \rho } } } _ { P } ,$ , then an additional $n - k$ (or 0 if $n \leq k )$ items should be sampled. 

EXAMPLE 7.5c A certain manufacturer produces computer chips; each chip is independently acceptable with some unknown probability $\cdot \mathbf { \nabla } { \hat { P } } \cdot$ . To obtain an approximate 99 percent confidence interval for ${ \boldsymbol { p } } ,$ whose length is approximately .05, an initial sample of 30 chips has been taken. If 26 of these chips are of acceptable quality, then the prelimi nary estimate of $\dot { \boldsymbol { p } }$ is 26/30. Using this value, a 99 percent confidence interval of length approximately .05 would require an approximate sample of size 

$$
n = \frac {4 (z _ {. 0 0 5}) ^ {2}}{(. 0 5) ^ {2}} \frac {2 6}{3 0} \left(1 - \frac {2 6}{3 0}\right) = \frac {4 (2 . 5 8) ^ {2}}{(. 0 5) ^ {2}} \frac {2 6}{3 0} \frac {4}{3 0} = 1, 2 3 1
$$

Hence, we should now sample an additional 1,201 chips and if, for instance, 1,040 of them are acceptable, then the final 99 percent confidence interval for $\boldsymbol { \underline { P } }$ is 

$$
\left(\frac {1 , 0 6 6}{1 , 2 3 1} - \sqrt {1 , 0 6 6 \left(1 - \frac {1 , 0 6 6}{1 , 2 3 1}\right)} \frac {z _ {. 0 0 5}}{1 , 2 3 1}, \frac {1 , 0 6 6}{1 , 2 3 1} + \sqrt {1 , 0 6 6 \left(1 - \frac {1 , 0 6 6}{1 , 2 3 1}\right) \frac {z _ {. 0 0 5}}{1 , 2 3 1}}\right)
$$

or 

$$
p \in (. 8 4 0 9 1,. 8 9 1 0 1)
$$

REMARK 

As shown, a 100(1 − α) percent confidence interval for $\boldsymbol { \mathscr { P } }$ will be of approximate length b when the sample size is 

$$
n = \frac {(2 z _ {\alpha / 2}) ^ {2}}{b ^ {2}} p (1 - p)
$$

Now it is easily shown that the function $g ( \boldsymbol { p } ) = p ( 1 - \boldsymbol { p } )$ attains its maximum value of $\frac { 1 } { 4 }$ , in the interval $0 \leq  { p } \leq 1$ , when $\textstyle { p = { \frac { 1 } { 2 } } }$ . Thus an upper bound on n is 

$$
n \leq \frac {(z _ {\alpha / 2}) ^ {2}}{b ^ {2}}
$$

and so by choosing a sample whose size is at least as large as $( z _ { \alpha / 2 } ) ^ { 2 } / b ^ { 2 }$ , one can be assured of obtaining a confidence interval of length no greater than $b$ without need of any additional sampling. ■ 

One-sided approximate confidence intervals for $\boldsymbol { \mathscr { P } }$ are also easily obtained; Table 7.3 gives the results. 


TABLE 7.3 Approximate 100(1 − α) Percent Confidence Intervals for p



X Is a Binomial $( n , p )$ Random Variable ${ \hat { p } } = X / n$


<table><tr><td>Type of Interval</td><td>Confidence Interval</td></tr><tr><td>Two-sided</td><td><eq>\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}</eq></td></tr><tr><td>One-sided lower</td><td><eq>(-\infty, \hat{p} + z_{\alpha}\sqrt{\hat{p}(1-\hat{p})/n})</eq></td></tr><tr><td>One-sided upper</td><td><eq>(\hat{p} - z_{\alpha}\sqrt{\hat{p}(1-\hat{p})/n}, \infty)</eq></td></tr></table>

## *7.6 CONFIDENCE INTERVAL OF THE MEAN OF THE EXPONENTIAL DISTRIBUTION

$\operatorname { I f } X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ are independent exponential random variables each having mean $\theta _ { i }$ , then it can be shown that the maximum likelihood estimator of θ is the sample mean $\textstyle \sum _ { i = 1 } ^ { n } X _ { i } / n$ To obtain a confidence interval estimator of $\theta _ { ; }$ , recall from Section $5 . 7$ that $\sum _ { i = 1 } ^ { n } X _ { i }$ has a gamma distribution with parameters $^ { n , }$ , 1/θ . This in turn implies (from the relationship between the gamma and chi-square distribution shown in Section 5.8.1.1) tha 

$$
\frac {2}{\theta} \sum_ {i = 1} ^ {n} X _ {i} \sim \chi_ {2 n} ^ {2}
$$

Hence, for any $\alpha \in ( 0 , 1 )$ 

$$
P \left\{\chi_ {1 - \alpha / 2, 2 n} ^ {2} <   \frac {2}{\theta} \sum_ {i = 1} ^ {n} X _ {i} <   \chi_ {\alpha / 2, 2 n} ^ {2} \right\} = 1 - \alpha
$$

or, equivalently, 

$$
P \left\{\frac {2 \sum_ {i = 1} ^ {n} X _ {i}}{\chi_ {\alpha / 2 , 2 n} ^ {2}} <   \theta <   \frac {2 \sum_ {i = 1} ^ {n} X _ {i}}{\chi_ {1 - \alpha / 2 , 2 n} ^ {2}} \right\} = 1 - \alpha
$$

Hence, a 100(1 − α) percent confidence interval for $\theta$ is 

$$
\theta \in \left(\frac {2 \sum_ {i = 1} ^ {n} X _ {i}}{\chi_ {\alpha / 2 , 2 n} ^ {2}}, \frac {2 \sum_ {i = 1} ^ {n} X _ {i}}{\chi_ {1 - \alpha / 2 , 2 n} ^ {2}}\right)
$$

EXAMPLE 7.6a The successive items produced by a certain manufacturer are assumed to have useful lives that (in hours) are independent with a common density function 

$$
f (x) = \frac {1}{\theta} e ^ {- x / \theta}, 0 <   x <   \infty
$$

If the sum of the lives of the first 10 items is equal to 1,740, what is a 95 percent confidence interval for the population mean θ ? 

SOLUTION From Program 5.8.1b (or Table A2), we see that 

$$
\chi_ {. 0 2 5, 2 0} ^ {2} = 3 4. 1 6 9, \qquad \chi_ {. 9 7 5, 2 0} ^ {2} = 9. 6 6 1
$$

and so we can conclude, with 95 percent confidence, that 

$$
\theta \in \left(\frac {3 4 8 0}{3 4 . 1 6 9}, \frac {3 4 8 0}{9 . 6 6 1}\right)
$$

or, equivalently, 

$$
\theta \in (1 0 1. 8 4 7, 3 6 0. 2 1 1)
$$

## *7.7 EVALUATING A POINT ESTIMATOR

Let $\mathbf { X } = ( X _ { 1 } , \ldots , X _ { n } )$ be a sample from a population whose distribution is specified up to an unknown parameter $\theta _ { i }$ , and let $d = d ( \mathbf { X } )$ be an estimator of θ . How are we to determine its worth as an estimator of θ ? One way is to consider the square of the difference between $d ( \mathbf { X } )$ and $\theta .$ . However, since $( d ( \mathbf { X } ) - \theta ) ^ { 2 }$ is a random variable, let us agree to consider $r ( d , \theta )$ , the mean square error of the estimator $d ,$ , which is defined by 

$$
r (d, \theta) = E [ (d (\mathbf {X}) - \theta) ^ {2} ]
$$

as an indication of the worth of $d$ as an estimator of $\theta$ . 

It would be nice if there were a single estimator d that minimized $r ( d , \theta )$ for all possible values of $\mathbf { \nabla } \cdot \theta .$ . However, except in trivial situations, this will never be the case. For example, consider the estimator $d ^ { * }$ defined by 

$$
d ^ {*} (X _ {1}, \ldots , X _ {n}) = 4
$$

That is, no matter what the outcome of the sample data, the estimator $d ^ { * }$ chooses 4 as its estimate of θ . While this seems like a silly estimator (since it makes no use of the data), it is, however, true that when $\theta$ actually equals $^ { 4 , }$ , the mean square error of this estimator is 0. Thus, the mean square error of any estimator different than $d ^ { * }$ must, in most situations, be larger than the mean square error of $d ^ { * }$ when $\theta = 4$ 

Although minimum mean square estimators rarely exist, it is sometimes possible to find an estimator having the smallest mean square error among all estimators that satisfy a certain property. One such property is that of unbiasedness. 

## Definition

Let $d = d ( \mathbf { X } )$ be an estimator of the parameter θ . Then 

$$
b _ {\theta} (d) = E [ d (\mathbf {X}) ] - \theta
$$

is called the bias of d as an estimator of θ . If $b _ { \theta } ( d ) = 0$ for all $\theta ,$ , then we say that d is an unbiased estimator of θ . In other words, an estimator is unbiased if its expected value always equals the value of the parameter it is attempting to estimate. 

EXAMPLE 7.7a Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ be a random sample from a distribution having unknown mean θ. Then 

$$
d _ {1} (X _ {1}, X _ {2}, \ldots , X _ {n}) = X _ {1}
$$

and 

$$
d _ {2} (X _ {1}, X _ {2}, \ldots , X _ {n}) = \frac {X _ {1} + X _ {2} + \cdots + X _ {n}}{n}
$$

are both unbiased estimators of θ since 

$$
E [ X _ {1} ] = E \left[ \frac {X _ {1} + X _ {2} + \cdots + X _ {n}}{n} \right] = \theta
$$

More generally, $\begin{array} { r } { d _ { 3 } ( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } ) = \sum _ { i = 1 } ^ { n } \lambda _ { i } X _ { i } } \end{array}$ is an unbiased estimator of θ whenever $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \lambda _ { i } = 1 } \end{array}$ . This follows since 

$$
\begin{array}{r l} E \left[ \sum_ {i = 1} ^ {n} \lambda_ {i} X _ {i} \right] & = \sum_ {i = 1} ^ {n} E [ \lambda_ {i} X _ {i} ] \\ & = \sum_ {i = 1} ^ {n} \lambda_ {i} E (X _ {i}) \\ & = \theta \sum_ {i = 1} ^ {n} \lambda_ {i} \\ & = \theta \quad \blacksquare \end{array}
$$

$\operatorname { I f } d ( X _ { 1 } , \ldots , X _ { n } )$ is an unbiased estimator, then its mean square error is given by 

$$
\begin{array}{r l} r (d, \theta) & = E [ (d (\mathbf {X}) - \theta) ^ {2} ] \\ & = E [ (d (\mathbf {X}) - E [ d (\mathbf {X}) ]) ^ {2} ] \qquad \text { since } d \text { is unbiased } \\ & = \operatorname{Var} (d (\mathbf {X})) \end{array}
$$

Thus the mean square error of an unbiased estimator is equal to its variance. 

EXAMPLE 7.7b Combining Independent Unbiased Estimators. Let $d _ { 1 }$ and $d _ { 2 }$ denote inde pendent unbiased estimators of $\theta _ { ; }$ , having known variances $\sigma _ { 1 } ^ { 2 }$ and $\sigma _ { 2 } ^ { 2 }$ . That is, for $i = 1 , 2$ , 

$$
E [ d _ {i} ] = \theta , \qquad \mathrm{Var} (d _ {i}) = \sigma_ {i} ^ {2}
$$

Any estimator of the form 

$$
d = \lambda d _ {1} + (1 - \lambda) d _ {2}
$$

will also be unbiased. To determine the value of λ that results in d having the smallest possible mean square error, note that 

$$
\begin{array}{l} r (d, \theta) = \operatorname{Var} (d) \\ \qquad = \lambda^ {2} \operatorname{Var} (d _ {1}) + (1 - \lambda) ^ {2} \operatorname{Var} (d _ {2}) \\ \qquad \text { by   the   independence   of } d _ {1} \text { and } d _ {2} \\ \qquad = \lambda^ {2} \sigma_ {1} ^ {2} + (1 - \lambda) ^ {2} \sigma_ {2} ^ {2} \end{array}
$$

Differentiation yields that 

$$
\frac {d}{d \lambda} r (d, \theta) = 2 \lambda \sigma_ {1} ^ {2} - 2 (1 - \lambda) \sigma_ {2} ^ {2}
$$

To determine the value of $\lambda$ that minimizes $r ( d , \theta ) - \mathrm { c a l l }$ it $\hat { \lambda } -$ set this equal to 0 and solve for λ to obtain 

$$
2 \hat {\lambda} \sigma_ {1} ^ {2} = 2 (1 - \hat {\lambda}) \sigma_ {2} ^ {2}
$$

or 

$$
\hat {\lambda} = \frac {\sigma_ {2} ^ {2}}{\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}} = \frac {1 / \sigma_ {1} ^ {2}}{1 / \sigma_ {1} ^ {2} + 1 / \sigma_ {2} ^ {2}}
$$

In words, the optimal weight to give an estimator is inversely proportional to its variance (when all the estimators are unbiased and independent). 

For an application of the foregoing, suppose that a conservation organization wants to determine the acidity content of a certain lake. To determine this quantity, they draw some water from the lake and then send samples of this water to n different laboratories. These laboratories will then, independently, test for acidity content by using their respective titration equipment, which is of differing precision. Specifically, suppose that $d _ { i } ,$ , the result of a titration test at laboratory $i ,$ is a random variable having mean $\theta _ { ; }$ , the true acidity of the sample water, and variance $\sigma _ { i } ^ { 2 } , i = 1 , \ldots , n .$ . If the quantities $\sigma _ { i } ^ { 2 } , i = 1 , . . . , n$ are known to the conservation organization, then they should estimate the acidity of the sampled water from the lake by 

$$
d = \frac {\sum_ {i = 1} ^ {n} d _ {i} / \sigma_ {i} ^ {2}}{\sum_ {i = 1} ^ {n} 1 / \sigma_ {i} ^ {2}}
$$

The mean square error of d is as follows: 

$$
\begin{array}{l} r (d, \theta) = \operatorname{Var} (d) \qquad \text { since } d \text { is unbiased } \\ \qquad = \left(\sum_ {i = 1} ^ {n} 1 / \sigma_ {i} ^ {2}\right) ^ {- 2} \sum_ {i = 1} ^ {n} \left(\frac {1}{\sigma_ {i} ^ {2}}\right) ^ {2} \sigma_ {i} ^ {2} \\ \qquad = \frac {1}{\sum_ {i = 1} ^ {n} 1 / \sigma_ {i} ^ {2}} \quad \blacksquare \end{array}
$$

A generalization of the result that the mean square error of an unbiased estimator is equal to its variance is that the mean square error of any estimator is equal to its variance plus the square of its bias. This follows since 

$$
\begin{array}{r l} r (d, \theta) & = E [ (d (\mathbf {X}) - \theta) ^ {2} ] \\ & = E [ (d - E [ d ] + E [ d ] - \theta) ^ {2} ] \\ & = E [ (d - E [ d ]) ^ {2} + (E [ d ] - \theta) ^ {2} + 2 (E [ d ] - \theta) (d - E [ d ]) ] \\ & = E [ (d - E [ d ]) ^ {2} ] + E [ (E [ d ] - \theta) ^ {2} ] \\ & \quad + 2 E [ (E [ d ] - \theta) (d - E [ d ]) ] \\ & = E [ (d - E [ d ]) ^ {2} ] + (E [ d ] - \theta) ^ {2} + 2 (E [ d ] - \theta) E [ d - E [ d ] ] \\ & \quad \text { since } E [ d ] - \theta \text { is   constant } \\ & = E [ (d - E [ d ]) ^ {2} ] + (E [ d ] - \theta) ^ {2} \end{array}
$$

The last equality follows since 

$$
E [ d - E [ d ] ] = 0
$$

Hence 

$$
r (d, \theta) = \mathrm{Var} (d) + b _ {\theta} ^ {2} (d)
$$

EXAMPLE 7.7c Let $X _ { 1 } , \ldots , X _ { n }$ denote a sample from a uniform (0, θ ) distribution, where θ is assumed unknown. Since 

$$
E [ X _ {i} ] = \frac {\theta}{2}
$$

a “natural” estimator to consider is the unbiased estimator 

$$
d _ {1} = d _ {1} (\mathbf {X}) = \frac {2 \sum_ {i = 1} ^ {n} X _ {i}}{n}
$$

Since $E [ d _ { 1 } ] = \theta$ , it follows that 

$$
\begin{array}{r l} r (d _ {1}, \theta) & = \operatorname{Var} (d _ {1}) \\ & = \frac {4}{n} \operatorname{Var} (X _ {i}) \\ & = \frac {4}{n} \frac {\theta^ {2}}{1 2} \quad \text { since } \operatorname{Var} (X _ {i}) = \frac {\theta^ {2}}{1 2} \\ & = \frac {\theta^ {2}}{3 n} \end{array}
$$

A second possible estimator of $\cdot _ { \theta }$ is the maximum likelihood estimator, which, as shown in Example 7.2d, is given by 

$$
d _ {2} = d _ {2} (\mathbf {X}) = \max _ {i} X _ {i}
$$

To compute the mean square error of $d _ { 2 }$ as an estimator of $\theta ,$ , we need to first compute its mean (so as to determine its bias) and variance. To do so, note that the distribution function of $d _ { 2 }$ is as follows: 

$$
\begin{array}{l} F _ {2} (x) \equiv P \{d _ {2} (\mathbf {X}) \leq x \} \\ = P \{\underset {i} {\max} X _ {i} \leq x \} \\ = P \{X _ {i} \leq x \quad \text { for   all } i = 1, \ldots , n \} \\ = \prod_ {i = 1} ^ {n} P \{X _ {i} \leq x \} \quad \text { by   independence } \\ = \left(\frac {x}{\theta}\right) ^ {n} \quad x \leq \theta \end{array}
$$

Hence, upon differentiating, we obtain that the density function of $d _ { 2 }$ , is 

$$
f _ {2} (x) = \frac {n x ^ {n - 1}}{\theta^ {n}}, x \leq \theta
$$

*7.7 Evaluating a Point Estimator 

Therefore, 

$$
E [ d _ {2} ] = \int_ {0} ^ {\theta} x \frac {n x ^ {n - 1}}{\theta^ {n}} d x = \frac {n}{n + 1} \theta\tag{7.7.1}
$$

Also 

$$
E [ d _ {2} ^ {2} ] = \int_ {0} ^ {\theta} x ^ {2} \frac {n x ^ {n - 1}}{\theta^ {n}} d x = \frac {n}{n + 2} \theta^ {2}
$$

and so 

$$
\begin{array}{c} \operatorname{Var} (d _ {2}) = \frac {n}{n + 2} \theta^ {2} - \left(\frac {n}{n + 1} \theta\right) ^ {2} \\ = n \theta^ {2} \left[ \frac {1}{n + 2} - \frac {n}{(n + 1) ^ {2}} \right] = \frac {n \theta^ {2}}{(n + 2) (n + 1) ^ {2}} \end{array}\tag{7.7.2}
$$

Hence 

$$
\begin{array}{r l} & r (d _ {2}, \theta) = (E (d _ {2}) - \theta) ^ {2} + \operatorname{Var} (d _ {2}) \\ & \qquad = \frac {\theta^ {2}}{(n + 1) ^ {2}} + \frac {n \theta^ {2}}{(n + 2) (n + 1) ^ {2}} \\ & \qquad = \frac {\theta^ {2}}{(n + 1) ^ {2}} \left[ 1 + \frac {n}{n + 2} \right] \\ & \qquad = \frac {2 \theta^ {2}}{(n + 1) (n + 2)} \end{array}\tag{7.7.3}
$$

Since 

$$
\frac {2 \theta^ {2}}{(n + 1) (n + 2)} \leq \frac {\theta^ {2}}{3 n} \quad n = 1, 2, \dots
$$

it follows that $d _ { 2 }$ is a more superior estimator of $\cdot _ { \theta }$ than is $d _ { 1 }$ . 

Equation 7.7.1 suggests the use of even another estimator — namely, the unbiased estimator $( 1 + 1 / n ) d _ { 2 } ( \mathbf { X } ) = ( 1 + 1 / n )$ max $X _ { i }$ . However, rather than considering thi estimator directly, let us consider all estimators of the form 

$$
d _ {c} (\mathbf {X}) = c \max _ {i} X _ {i} = c d _ {2} (\mathbf {X})
$$

where $c$ is a given constant. The mean square error of this estimator is 

$$
\begin{array}{r l} & {r (d _ {c} (\mathbf {X}), \theta) = \mathrm{Var} (d _ {c} (\mathbf {X})) + (E [ d _ {c} (\mathbf {X}) ] - \theta) ^ {2}} \\ & {\qquad = c ^ {2} \mathrm{Var} (d _ {2} (\mathbf {X})) + (c E [ d _ {2} (\mathbf {X}) ] - \theta) ^ {2}} \\ & {\qquad = \frac {c ^ {2} n \theta^ {2}}{(n + 2) (n + 1) ^ {2}} + \theta^ {2} \left(\frac {c n}{n + 1} - 1\right) ^ {2}} \end{array}
$$

by Equations 7.7.2 and 7.7.1 

(7.7.4) 

To determine the constant c resulting in minimal mean square error, we differentiate to obtain 

$$
\frac {d}{d c} r (d _ {c} (\mathbf {X}), \theta) = \frac {2 c n \theta^ {2}}{(n + 2) (n + 1) ^ {2}} + \frac {2 \theta^ {2} n}{n + 1} \left(\frac {c n}{n + 1} - 1\right)
$$

Equating this to 0 shows that the best constant c — call it $c ^ { * } -$ is such that 

$$
\frac {c ^ {*}}{n + 2} + c ^ {*} n - (n + 1) = 0
$$

or 

$$
c ^ {*} = \frac {(n + 1) (n + 2)}{n ^ {2} + 2 n + 1} = \frac {n + 2}{n + 1}
$$

Substituting this value of c into Equation 7.7.4 yields that 

$$
\begin{array}{r l} r \left(\frac {n + 2}{n + 1} \max _ {i} X _ {i}, \theta\right) & = \frac {(n + 2) n \theta^ {2}}{(n + 1) ^ {4}} + \theta^ {2} \left(\frac {n (n + 2)}{(n + 1) ^ {2}} - 1\right) ^ {2} \\ & = \frac {(n + 2) n \theta^ {2}}{(n + 1) ^ {4}} + \frac {\theta^ {2}}{(n + 1) ^ {4}} \\ & = \frac {\theta^ {2}}{(n + 1) ^ {2}} \end{array}
$$

A comparison with Equation 7.7.3 shows that the (biased) estimator $( n \mathrm { ~ + ~ } 2 ) /$ $( n + 1 ) \operatorname* { m a x } _ { i } X _ { i }$ has about half the mean square error of the maximum likelihood estimator max $X _ { i }$ . ■ 

## *7.8 THE BAYES ESTIMATOR

In certain situations it seems reasonable to regard an unknown parameter θ as being the value of a random variable from a given probability distribution. This usually arises when, prior to the observance of the outcomes of the data $X _ { 1 } , \dots , X _ { n } $ , we have some information about the value of θ and this information is expressible in terms of a probability distribution (called appropriately the prior distribution of θ ). For instance, suppose that from past experience we know that θ is equally likely to be near any value in the interval (0, 1). Hence, we could reasonably assume that θ is chosen from a uniform distribution on (0, 1). 

Suppose now that our prior feelings about $\theta$ are that it can be regarded as being the value of a continuous random variable having probability density function ${ \boldsymbol { p } } ( { \boldsymbol { \theta } } )$ ; and suppose that we are about to observe the value of a sample whose distribution depends on θ . Specifically, suppose that $f ( x | \theta )$ represents the likelihood — that is, it is the probability mass function in the discrete case or the probability density function in the continuous case — that a data value is equal to x when θ is the value of the parameter. If the observed data values are $X _ { i } = x _ { i } , i = 1 , \ldots , n ,$ , then the updated, or conditional, probability density function of θ is as follows: 

$$
\begin{array}{c} f (\theta | x _ {1}, \ldots , x _ {n}) = \frac {f (\theta , x _ {1} , \ldots , x _ {n})}{f (x _ {1} , \ldots , x _ {n})} \\ = \frac {p (\theta) f (x _ {1} , \ldots , x _ {n} | \theta)}{\int f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta) d \theta} \end{array}
$$

The conditional density function $f ( \theta | x _ { 1 } , \ldots , x _ { n } )$ is called the posterior density function. (Thus, before observing the data, one’s feelings about $\theta$ are expressed in terms of the prior distribution, whereas once the data are observed, this prior distribution is updated to yield the posterior distribution.) 

Now we have shown that whenever we are given the probability distribution of a random variable, the best estimate of the value of that random variable, in the sense of minimizing the expected squared error, is its mean. Therefore, it follows that the best estimate of θ, given the data values $X _ { i } = x _ { i } , i = 1 , \ldots , n ,$ is the mean of the posterior distribution $f ( \theta | x _ { 1 } , \ldots , x _ { n } )$ . This estimator, called the Bayes estimator, is written as $E [ \theta | X _ { 1 } , \ldots , X _ { n } ]$ That is, $\mathrm { i f } X _ { i } = x _ { i } , i = 1 , . . . , n $ , then the value of the Bayes estimator is 

$$
E [ \theta | X _ {1} = x _ {1}, \ldots , X _ {n} = x _ {n} ] = \int \theta f (\theta | x _ {1}, \ldots , x _ {n}) d \theta
$$

EXAMPLE 7.8a Suppose that $X _ { 1 } , \ldots , X _ { n }$ are independent Bernoulli random variables, each having probability mass function given by 

$$
f (x | \theta) = \theta^ {x} (1 - \theta) ^ {1 - x}, \qquad x = 0, 1
$$

where $\theta$ is unknown. Further, suppose that $\theta$ is chosen from a uniform distribution on (0, 1). Compute the Bayes estimator of θ . 

SOLUTION We must compute $E [ \theta | X _ { 1 } , \ldots , X _ { n } ]$ . Since the prior density of $\cdot _ { \theta }$ is the uniform density 

$$
p (\theta) = 1, \qquad 0 <   \theta <   1
$$

we have that the conditional density of θ given $X _ { 1 } , \ldots , X _ { n }$ is given by 

$$
\begin{array}{r l} f (\theta | x _ {1}, \ldots , x _ {n}) & = \frac {f (x _ {1} , \ldots , x _ {n} , \theta)}{f (x _ {1} , \ldots , x _ {n})} \\ & = \frac {f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta)}{\int_ {0} ^ {1} f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta) d \theta} \\ & = \frac {\theta^ {\Sigma_ {1} ^ {n} x _ {i}} (1 - \theta) ^ {n - \Sigma_ {1} ^ {n} x _ {i}}}{\int_ {0} ^ {1} \theta^ {\Sigma_ {1} ^ {n} x _ {i}} (1 - \theta) ^ {n - \Sigma_ {1} ^ {n} x _ {i}} d \theta} \end{array}
$$

Now it can be shown that for integral values m and r 

$$
\int_ {0} ^ {1} \theta^ {m} (1 - \theta) ^ {r} d \theta = \frac {m ! r !}{(m + r + 1) !}\tag{7.8.1}
$$

Hence, upon letting $x = \textstyle \sum _ { i = 1 } ^ { n }$ x<sub>i</sub> 

$$
f (\theta | x _ {1}, \ldots , x _ {n}) = \frac {(n + 1) ! \theta^ {x} (1 - \theta) ^ {n - x}}{x ! (n - x) !}\tag{7.8.2}
$$

Therefore, 

$$
\begin{array}{l} E [ \theta | x _ {1}, \dots , x _ {n} ] = \frac {(n + 1) !}{x ! (n - x) !} \int_ {0} ^ {1} \theta^ {1 + x} (1 - \theta) ^ {n - x} d \theta \\ = \frac {(n + 1) !}{x ! (n - x) !} \frac {(1 + x) ! (n - x) !}{(n + 2) !} \quad \text { from   Equation   7.8.1 } \\ = \frac {x + 1}{n + 2} \end{array}
$$

Thus, the Bayes estimator is given by 

$$
E [ \theta | X _ {1}, \ldots , X _ {n} ] = \frac {\sum_ {i = 1} ^ {n} X _ {i} + 1}{n + 2}
$$

As an illustration, if 10 independent trials, each of which results in a success with probability $\theta ,$ result in $^ 6$ successes, then assuming a uniform (0, 1) prior distribution on $\theta ,$ , the Bayes estimator of $\theta$ is 7/12 (as opposed, for instance, to the maximum likelihood estimator of 6/10). ■ 

## REMARK

The conditional distribution of θ given that $X _ { i } = x _ { i } , i = 1 , \dots , n$ , whose density function is given by Equation 7.8.2, is called the beta distribution with parameters $\textstyle \sum _ { i = 1 } ^ { n } x _ { i } + 1$ $\textstyle n - \sum _ { i = 1 } ^ { n } x _ { i } + 1$ ■ 

EXAMPLE 7.8b Suppose $X _ { 1 } , \ldots , X _ { n }$ are independent normal random variables, each having unknown mean $\theta$ and known variance $\sigma _ { 0 } ^ { 2 }$ . If θ is itself selected from a normal population having known mean $\mu$ and known variance $\sigma ^ { 2 }$ , what is the Bayes estimator of θ ? 

SOLUTION In order to determine $E [ \theta | X _ { 1 } , \ldots , X _ { n } ]$ , the Bayes estimator, we need first determine the conditional density of $\cdot \theta$ given the values of $X _ { 1 } , \ldots , X _ { n }$ . Now 

$$
f (\theta | x _ {1}, \ldots , x _ {n}) = \frac {f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta)}{f (x _ {1} , \ldots , x _ {n})}
$$

where 

$$
f (x _ {1}, \ldots , x _ {n} | \theta) = \frac {1}{(2 \pi) ^ {n / 2} \sigma_ {0} ^ {n}} \exp \left\{- \sum_ {i = 1} ^ {n} (x _ {i} - \theta) ^ {2} / 2 \sigma_ {0} ^ {2} \right\}
$$

$$
p (\theta) = \frac {1}{\sqrt {2 \pi} \sigma} \exp \{- (\theta - \mu) ^ {2} / 2 \sigma^ {2} \}
$$

and 

$$
f (x _ {1}, \ldots , x _ {n}) = \int_ {- \infty} ^ {\infty} f (x _ {1}, \ldots , x _ {n} | \theta) p (\theta) d \theta
$$

With the help of a little algebra, it can now be shown that this conditional density is a normal density with mean 

$$
\begin{array}{r} E [ \theta | X _ {1}, \ldots , X _ {n} ] = \frac {n \sigma^ {2}}{n \sigma^ {2} + \sigma_ {0} ^ {2}} \overline {{X}} + \frac {\sigma_ {0} ^ {2}}{n \sigma^ {2} + \sigma_ {0} ^ {2}} \mu \\ = \frac {\frac {n}{\sigma_ {0} ^ {2}}}{\frac {n}{\sigma_ {0} ^ {2}} + \frac {1}{\sigma^ {2}}} \overline {{X}} + \frac {\frac {1}{\sigma^ {2}}}{\frac {n}{\sigma_ {0} ^ {2}} + \frac {1}{\sigma^ {2}}} \mu \end{array}\tag{7.8.3}
$$

and variance 

$$
\operatorname{Var} (\theta | X _ {1}, \ldots , X _ {n}) = \frac {\sigma_ {0} ^ {2} \sigma^ {2}}{n \sigma^ {2} + \sigma_ {0} ^ {2}}
$$

Writing the Bayes estimator as we did in Equation 7.8.3 is informative, for it shows that it is a weighted average of X , the sample mean, and $\mu _ { ; }$ , the a priori mean. In fact, the weights given to these two quantities are in proportion to the inverses of $\sigma _ { 0 } ^ { 2 } / n$ (the conditional variance of the sample mean $\overline { { X } }$ given θ) and $\sigma ^ { 2 }$ (the variance of the prior distribution). ■ 

## REMARK: ON CHOOSING A NORMAL PRIOR

As illustrated by Example 7.8b, it is computationally very convenient to choose a normal prior for the unknown mean θ of a normal distribution — for then the Bayes estimator is simply given by Equation 7.8.3. This raises the question of how one should go about determining whether there is a normal prior that reasonably represents one’s prior feelings about the unknown mean. 

To begin, it seems reasonable to determine the value — call it $\mu$ — that you a priori feel is most likely to be near θ . That is, we start with the mode (which equals the mean when the distribution is normal) of the prior distribution. We should then try to ascertain whether or not we believe that the prior distribution is symmetric about $\mu$ . That is, for each $a > 0$ do we believe that it is just as likely that θ will lie between $\mu - a$ and $\mu$ as it is that it will be between $\mu$ and $\mu + a ?$ If the answer is positive, then we accept, as a working hypothesis, that our prior feelings about $\theta$ can be expressed in terms of a prior distribution that is normal with mean $\mu .$ . To determine $\sigma$ , the standard deviation of the normal prior, think of an interval centered about $\mu$ that you a priori feel is 90 percent certain to contain $\theta .$ . For instance, suppose you feel 90 percent (no more and no less) certain that $\theta$ will lie between $\mu - a$ and $\mu + a$ . Then, since a normal random variable $\theta$ with mean $\mu$ and variance $\sigma ^ { 2 }$ is such that 

$$
P \left\{- 1. 6 4 5 <   \frac {\theta - \mu}{\sigma} <   1. 6 4 5 \right\} = . 9 0
$$

or 

$$
P \{\mu - 1. 6 4 5 \sigma <   \theta <   \mu + 1. 6 4 5 \sigma \} = . 9 0
$$

it seems reasonable to take 

$$
1. 6 4 5 \sigma = a \quad \text { or } \quad \sigma = \frac {a}{1 . 6 4 5}
$$

Thus, if your prior feelings can indeed be reasonably described by a normal distribution, then that distribution would have mean $\mu$ and standard deviation $\sigma = a / 1$ .645. As a test of whether this distribution indeed fits your prior feelings you might ask yourself such questions as whether you are 95 percent certain that $\theta$ will fall between $\mu - 1 . 9 6 \sigma$ and $\mu + 1 . 9 6 \sigma$ , or whether you are 99 percent certain that $\theta$ will fall between $\mu - 2 . 5 8 \sigma$ and $\mu + 2 . 5 8 \sigma$ , where these intervals are determined by the equalities 

$$
\begin{array}{l} P \left\{- 1. 9 6 <   \frac {\theta - \mu}{\sigma} <   1. 9 6 \right\} = . 9 5 \\ P \left\{- 2. 5 8 <   \frac {\theta - \mu}{\sigma} <   2. 5 8 \right\} = . 9 9 \end{array}
$$

which hold when $\theta$ is normal with mean $\mu$ and variance $\sigma ^ { 2 }$ . 

EXAMPLE 7.8c Consider the likelihood function $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ and suppose that $\theta$ is uniformly distributed over some interval $( a , b )$ . The posterior density of θ given $X _ { 1 } , \ldots , X _ { n }$ equals 

$$
\begin{array}{r l} f (\theta | x _ {1}, \ldots , x _ {n}) & = \frac {f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta)}{\int_ {a} ^ {b} f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta) d \theta} \\ & = \frac {f (x _ {1} , \ldots , x _ {n} | \theta)}{\int_ {a} ^ {b} f (x _ {1} , \ldots , x _ {n} | \theta) d \theta} \quad a <   \theta <   b \end{array}
$$

Now the mode of a density $f ( \theta )$ was defined to be that value of $\theta$ that maximizes $f ( \theta )$ By the foregoing, it follows that the mode of the density $f ( \theta | x _ { 1 } , \ldots , x _ { n } )$ is that value of $\overrightharpoon { \theta }$ maximizing $f ( x _ { 1 } , \ldots , x _ { n } | \theta )$ ; that is, it is just the maximum likelihood estimate of θ [when it is constrained to be in $( a , b ) ]$ ]. In other words, the maximum likelihood estimate equals the mode of the posterior distribution when a uniform prior distribution is assumed. ■ 

If, rather than a point estimate, we desire an interval in which θ lies with a specified probability — say $1 - \alpha -$ we can accomplish this by choosing values a and b such that 

$$
\int_ {a} ^ {b} f (\theta | x _ {1}, \ldots , x _ {n}) d \theta = 1 - \alpha
$$

EXAMPLE 7.8d Suppose that if a signal of value s is sent from location A, then the signal value received at location B is normally distributed with mean s and variance 60. Suppose also that the value of a signal sent at location A is, a priori, known to be normally distributed with mean 50 and variance 100. If the value received at location B is equal to 40, determine an interval that will contain the actual value sent with probability .90. 

SOLUTION It follows from Example 7.8b that the conditional distribution of S, the signa value sent, given that 40 is the value received, is normal with mean and variance given by 

$$
\begin{array}{l} E [ S | \text {data} ] = \frac {1 / 6 0}{1 / 6 0 + 1 / 1 0 0} 4 0 + \frac {1 / 1 0 0}{1 / 6 0 + 1 / 1 0 0} 5 0 = 4 3. 7 5 \\ \operatorname{Var} (S | \text {data}) = \frac {1}{1 / 6 0 + 1 / 1 0 0} = 3 7. 5 \end{array}
$$

Hence, given that the value received is 40, $( S - 4 3 . 7 5 ) / \sqrt { 3 7 . 5 }$ has a unit standard distribution and so 

$$
P \left\{- 1. 6 4 5 <   \frac {S - 4 3 . 7 5}{\sqrt {3 7 . 5}} <   1. 6 4 5 | \text { data } \right\} = . 9 0
$$

or 

$$
P \{4 3. 7 5 - 1. 6 4 5 \sqrt {3 7 . 5} <   S <   4 3. 7 5 + 1. 6 4 5 \sqrt {3 7 . 5} | \mathrm{data} \} = . 9 5
$$

That is, with probability .90, the true signal sent lies within the interval (33.68, 53.82). ■ 

## Problems

1. Let $X _ { 1 } , \ldots , X _ { n }$ be a sample from the distribution whose density function is 

$$
f (x) = \left\{ \begin{array}{l l} e ^ {- (x - \theta)} & x \geq \theta \\ 0 & \text { otherwise } \end{array} \right.
$$

Determine the maximum likelihood estimator of θ . 

2. Determine the maximum likelihood estimator of $\theta$ when $X _ { 1 } , \ldots , X _ { n }$ is a sample with density function 

$$
f (x) = \frac {1}{2} e ^ {- | x - \theta |}, \qquad - \infty <   x <   \infty
$$

3. Let $X _ { 1 } , \ldots , X _ { n }$ be a sample from a normal $\mu , \sigma ^ { 2 }$ population. Determine the maximum likelihood estimator of $\sigma ^ { 2 }$ when $\mu$ is known. What is the expected value of this estimator? 

4. The height of a radio tower is to be measured by measuring both the horizontal distance X from the center of its base to a measuring instrument and the vertical angle of the measuring device (see the following figure). If five measurements of the distance L give (in feet) values 

$$
1 5 0. 4 2, 1 5 0. 4 5, 1 5 0. 4 9, 1 5 0. 5 2, 1 5 0. 4 0
$$

and four measurements of the angle $\theta$ give (in degrees) values 

40.26, 40.27, 40.29, 40.26 

estimate the height of the tower. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/cc165448ea25d45abd1023ccf868eb87b23a11757052853d9a7ef26ccd163780.jpg)


5. Suppose that $X _ { 1 } , \ldots , X _ { n }$ are normal with mean $\mu _ { 1 } ; Y _ { 1 } , \ldots , Y _ { n }$ are normal with mean $\mu _ { 2 } ;$ and $W _ { 1 } , \ldots , W _ { n }$ are normal with mean $\mu _ { 1 } + \mu _ { 2 }$ . Assuming that all 3n random variables are independent with a common variance, find the maximum likelihood estimators of $\mu _ { 1 }$ and $\mu _ { 2 }$ 

6. River floods are often measured by their discharges (in units of feet cubed per second). The value v is said to be the value of a 100-year flood if 

$$
P \{D \geq v \} = . 0 1
$$

where D is the discharge of the largest flood in a randomly chosen year. The following table gives the flood discharges of the largest floods of the Blackstone River in Woonsocket, Rhode Island, in each of the years from 1929 to 1965. Assuming that these discharges follow a lognormal distribution, estimate the value of a 100-year flood. 


Annual Floods of the Blackstone River (1929–1965)


<table><tr><td>Year</td><td>Flood Discharge (ft3/s)</td></tr><tr><td>1929</td><td>4,570</td></tr><tr><td>1930</td><td>1,970</td></tr><tr><td>1931</td><td>8,220</td></tr><tr><td>1932</td><td>4,530</td></tr><tr><td>1933</td><td>5,780</td></tr><tr><td>1934</td><td>6,560</td></tr><tr><td>1935</td><td>7,500</td></tr><tr><td>1936</td><td>15,000</td></tr><tr><td>1937</td><td>6,340</td></tr><tr><td>1938</td><td>15,100</td></tr><tr><td>1939</td><td>3,840</td></tr><tr><td>1940</td><td>5,860</td></tr><tr><td>1941</td><td>4,480</td></tr><tr><td>1942</td><td>5,330</td></tr><tr><td>1943</td><td>5,310</td></tr><tr><td>1944</td><td>3,830</td></tr><tr><td>1945</td><td>3,410</td></tr><tr><td>1946</td><td>3,830</td></tr><tr><td>1947</td><td>3,150</td></tr><tr><td>1948</td><td>5,810</td></tr><tr><td>1949</td><td>2,030</td></tr><tr><td>1950</td><td>3,620</td></tr><tr><td>1951</td><td>4,920</td></tr><tr><td>1952</td><td>4,090</td></tr><tr><td>1953</td><td>5,570</td></tr><tr><td>1954</td><td>9,400</td></tr><tr><td>1955</td><td>32,900</td></tr><tr><td>1956</td><td>8,710</td></tr><tr><td>1957</td><td>3,850</td></tr><tr><td>1958</td><td>4,970</td></tr><tr><td>1959</td><td>5,398</td></tr><tr><td>1960</td><td>4,780</td></tr><tr><td>1961</td><td>4,020</td></tr><tr><td>1962</td><td>5,790</td></tr><tr><td>1963</td><td>4,510</td></tr><tr><td>1964</td><td>5,520</td></tr><tr><td>1965</td><td>5,300</td></tr></table>

7. A manufacturer of heat exchangers requires that the plate spacings of its exchang ers be between .240 and .260 inches. A quality control engineer sampled 20 exchangers and measured the spacing of the plates on each exchanger. If the sample mean and sample standard deviation of these 20 measurements are .254 and .005, estimate the fraction of all exchangers whose plate spacings fall outside the specified region. Assume that the plate spacings have a normal distribution. 

8. An electric scale gives a reading equal to the true weight plus a random error that is normally distributed with mean 0 and standard deviation $\sigma = . 1$ mg. Suppose that the results of five successive weighings of the same object are as follows: 3.142, 3.163, 3.155, 3.150, 3.141. 

(a) Determine a 95 percent confidence interval estimate of the true weight. 

(b) Determine a 99 percent confidence interval estimate of the true weight. 

9. The PCB concentration of a fish caught in Lake Michigan was measured by a technique that is known to result in an error of measurement that is normally distributed with a standard deviation of .08 ppm (parts per million). Suppose the results of 10 independent measurements of this fish are 

11.2, 12.4, 10.8, 11.6, 12.5, 10.1, 11.0, 12.2, 12.4, 10.6 

(a) Give a 95 percent confidence interval for the PCB level of this fish. 

(b) Give a 95 percent lower confidence interval. 

(c) Give a 95 percent upper confidence interval. 

10. The standard deviation of test scores on a certain achievement test is 11.3. If a random sample of 81 students had a sample mean score of 74.6, find a 90 percent confidence interval estimate for the average score of all students. 

11. Let $X _ { 1 } , \dots , X _ { n } , X _ { n + 1 }$ be a sample from a normal population having an unknown mean µ and variance 1. Let $\begin{array} { r } { \bar { X } _ { n } = \sum _ { i = 1 } ^ { n } X _ { i } / n } \end{array}$ be the average of the first n of them. 

(a) What is the distribution of $X _ { n + 1 } - { \bar { X } } _ { n } ?$ 

(b) If $\bar { X } _ { n } = 4 .$ , give an interval that, with 90 percent confidence, will contain the value of $X _ { n + 1 }$ 

12. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population whose mean µ is unknown but whose variance $\sigma ^ { 2 }$ is known, show that $( - \infty , { \overline { { X } } } + z _ { \alpha } \sigma / { \sqrt { n } } )$ is a $1 0 0 ( 1 - \alpha )$ percent lower confidence interval for $\mu .$ . 

13. A sample of 20 cigarettes is tested to determine nicotine content and the average value observed was 1.2 mg. Compute a 99 percent two-sided confidence interval for the mean nicotine content of a cigarette if it is known that the standard deviation of a cigarette’s nicotine content is $\sigma = . 2 \mathrm { m g }$ 

14. In Problem 13, suppose that the population variance is not known in advance of the experiment. If the sample variance is .04, compute a 99 percent two-sided confidence interval for the mean nicotine content. 

15. In Problem 14, compute a value c for which we can assert “with 99 percent confidence” that c is larger than the mean nicotine content of a cigarette. 

16. Suppose that when sampling from a normal population having an unknown mean $\mu$ and unknown variance $\sigma ^ { 2 }$ , we wish to determine a sample size n so as to guarantee that the resulting $1 0 0 ( 1 \textrm { -- } \alpha )$ percent confidence interval for $\mu$ will be of size no greater than A, for given values α and A. Explain how we can approximately do this by a double sampling scheme that first takes a subsample of size 30 and then chooses the total sample size by using the results of the first subsample. 

17. The following data resulted from 24 independent measurements of the melting point of lead. 

<table><tr><td>330°C</td><td>322°C</td><td>345°C</td></tr><tr><td>328.6°C</td><td>331°C</td><td>342°C</td></tr><tr><td>342.4°C</td><td>340.4°C</td><td>329.7°C</td></tr><tr><td>334°C</td><td>326.5°C</td><td>325.8°C</td></tr><tr><td>337.5°C</td><td>327.3°C</td><td>322.6°C</td></tr><tr><td>341°C</td><td>340°C</td><td>333°C</td></tr><tr><td>343.3°C</td><td>331°C</td><td>341°C</td></tr><tr><td>329.5°C</td><td>332.3°C</td><td>340°C</td></tr></table>

Assuming that the measurements can be regarded as constituting a normal sample whose mean is the true melting point of lead, determine a 95 percent two-sided confidence interval for this value. Also determine a 99 percent two-sided confidence interval. 

18. The following are scores on IQ tests of a random sample of 18 students at a large eastern university. 

130, 122, 119, 142, 136, 127, 120, 152, 141, 

132, 127, 118, 150, 141, 133, 137, 129, 142 

(a) Construct a 95 percent confidence interval estimate of the average IQ score of all students at the university. 

(b) Construct a 95 percent lower confidence interval estimate. 

(c) Construct a 95 percent upper confidence interval estimate. 

19. Suppose that a random sample of nine recently sold houses in a certain city resulted in a sample mean price of $222,000, with a sample standard deviation of $22,000. Give a 95 percent upper confidence interval for the mean price of all recently sold houses in this city. 

20. A company self-insures its large fleet of cars against collisions. To determine its mean repair cost per collision, it has randomly chosen a sample of 16 accidents. If the average repair cost in these accidents is $2,200 with a sample standard deviation of $800, find a 90 percent confidence interval estimate of the mean cost per collision. 

21. A standardized test is given annually to all sixth-grade students in the state of Washington. To determine the average score of students in her district, a school supervisor selects a random sample of 100 students. If the sample mean of these students’ scores is 320 and the sample standard deviation is 16, give a 95 percent confidence interval estimate of the average score of students in that supervisor’s district. 

22. Each of 20 science students independently measured the melting point of lead. The sample mean and sample standard deviation of these measurements were (in degrees centigrade) 330.2 and 15.4, respectively. Construct (a) a 95 percent and (b) a 99 percent confidence interval estimate of the true melting point of lead. 

23. A random sample of 300 CitiBank VISA cardholder accounts indicated a sample mean debt of $1,220 with a sample standard deviation of $840. Construct a 95 percent confidence interval estimate of the average debt of all cardholders. 

24. In Problem 23, find the smallest value v that “with 90 percent confidence,” exceeds the average debt per cardholder. 

25. Verify the formula given in Table 7.1 for the 100(1 − α) percent lower confidence interval for µ when σ is unknown. 

26. The range of a new type of mortar shell is being investigated. The observed ranges, in meters, of 20 such shells are as follows: 

<table><tr><td>2,100</td><td>1,984</td><td>2,072</td><td>1,898</td></tr><tr><td>1,950</td><td>1,992</td><td>2,096</td><td>2,103</td></tr><tr><td>2,043</td><td>2,218</td><td>2,244</td><td>2,206</td></tr><tr><td>2,210</td><td>2,152</td><td>1,962</td><td>2,007</td></tr><tr><td>2,018</td><td>2,106</td><td>1,938</td><td>1,956</td></tr></table>

Assuming that a shell’s range is normally distributed, construct (a) a 95 percent and (b) a 99 percent two-sided confidence interval for the mean range of a shell. (c) Determine the largest value v that, “with 95 percent confidence,” will be less than the mean range. 

27. Studies were conducted in Los Angeles to determine the carbon monoxide concentration near freeways. The basic technique used was to capture air samples in special bags and to then determine the carbon monoxide concentration by using a spectrophotometer. The measurements in ppm (parts per million) over a sampled period during the year were 102.2, 98.4, 104.1, 101, 102.2, 100.4, 98.6, 88.2, 78.8, 83, 84.7, 94.8, 105.1, 106.2, 111.2, 108.3, 105.2, 103.2, 99, 

98.8. Compute a 95 percent two-sided confidence interval for the mean carbon monoxide concentration. 

28. A set of 10 determinations, by a method devised by the chemist Karl Fischer, of the percentage of water in a methanol solution yielded the following data. 

.50, .55, .53, .56, .54, .57, .52, .60, .55, .58 

Assuming normality, use these data to give a 95 percent confidence interval for the actual percentage. 

29. Suppose that $U _ { 1 } , U _ { 2 } , \dots$ is a sequence of independent uniform (0,1) random variables, and define N by 

$$
N = \min \{n: U _ {1} + \dots + U _ {n} > 1 \}
$$

That is, N is the number of uniform (0, 1) random variables that need be summed to exceed 1. Use random numbers to determine the value of 36 random variables having the same distribution as N , then use these data to obtain a 95 percent confidence interval estimate of E [N ]. Based on this interval, guess the exact value of E [N ]. 

30. An important issue for a retailer is to decide when to reorder stock from a supplier. A common policy used to make the decision is of a type called s, S: The retailer orders at the end of a period if the on-hand stock is less than s, and orders enough to bring the stock up to S. The appropriate values of s and S depend on different cost parameters, such as inventory holding costs and the profit per item sold, as well as the distribution of the demand during a period. Consequently, it is important for the retailer to collect data relating to the parameters of the demand distribution. Suppose that the following data give the numbers of a certain type of item sold in each of 30 weeks. 

14, 8, 12, 9, 5, 22, 15, 12, 16, 7, 10, 9, 15, 15, 12, 

9, 11, 16, 8, 7, 15, 13, 9, 5, 18, 14, 10, 13, 7, 11 

Assuming that the numbers sold each week are independent random variables from a common distribution, use the data to obtain a 95 percent confidence interval for the mean number sold in a week. 

31. A random sample of 16 full professors at a large private university yielded a sample mean annual salary of $90,450 with a sample standard deviation of $9,400. Determine a 95 percent confidence interval of the average salary of all full professors at that university. 

32. Let $X _ { 1 } , \dots , X _ { n } , X _ { n + 1 }$ denote a sample from a normal population whose mean µ and variance $\sigma ^ { 2 }$ are unknown. Suppose that we are interested in using the observed values of $X _ { 1 } , \ldots , X _ { n }$ to determine an interval, called a prediction interval, that we predict will contain the value of $X _ { n + 1 }$ with $1 0 0 ( 1 - \alpha )$ percent confidence. Let ${ \overline { { X } } } _ { n }$ and $S _ { n } ^ { 2 }$ be the sample mean and sample variance of $X _ { 1 } , \ldots , X _ { n }$ 

(a) Determine the distribution of 

$$
X _ {n + 1} - \overline {{X}} _ {n}
$$

(b) Determine the distribution of 

$$
\underline {{X _ {n + 1} - \overline {{X}} _ {n}}}
$$

$$
S _ {n} \sqrt {1 + \frac {1}{n}}
$$

(c) Give the prediction interval for $X _ { n + 1 }$ 

(d) The interval in part (c) will contain the value of $X _ { n + 1 }$ with 100(1 − α) percent confidence. Explain the meaning of this statement. 

33. National Safety Council data show that the number of accidental deaths due to drowning in the United States in the years from 1990 to 1993 were (in units of one thousand) 5.2, 4.6, 4.3, 4.8. Use these data to give an interval that will, with 95 percent confidence, contain the number of such deaths in 1994. 

34. The daily dissolved oxygen concentration for a water stream has been recorded over 30 days. If the sample average of the 30 values is 2.5 mg/liter and the sample standard deviation is 2.12 mg/liter, determine a value which, with 90 percent confidence, exceeds the mean daily concentration. 

35. Verify the formulas given in Table 7.1 for the 100(1 − α) percent lower and upper confidence intervals for $\sigma ^ { 2 }$ 

36. The capacities (in ampere-hours) of 10 batteries were recorded as follows: 

$$
\begin{array}{l} 1 4 0, 1 3 6, 1 5 0, 1 4 4, 1 4 8, 1 5 2, 1 3 8, 1 4 1, 1 4 3, 1 5 1 \end{array}
$$

(a) Estimate the population variance $\sigma ^ { 2 }$ 

(b) Compute a 99 percent two-sided confidence interval for $\sigma ^ { 2 }$ . 

(c) Compute a value v that enables us to state, with 90 percent confidence, that $\sigma ^ { 2 }$ is less than v. 

37. Find a 95 percent two-sided confidence interval for the variance of the diameter of a rivet based on the data given here. 

<table><tr><td>6.68</td><td>6.66</td><td>6.62</td><td>6.72</td></tr><tr><td>6.76</td><td>6.67</td><td>6.70</td><td>6.72</td></tr><tr><td>6.78</td><td>6.66</td><td>6.76</td><td>6.72</td></tr><tr><td>6.76</td><td>6.70</td><td>6.76</td><td>6.76</td></tr><tr><td>6.74</td><td>6.74</td><td>6.81</td><td>6.66</td></tr><tr><td>6.64</td><td>6.79</td><td>6.72</td><td>6.82</td></tr><tr><td>6.81</td><td>6.77</td><td>6.60</td><td>6.72</td></tr><tr><td>6.74</td><td>6.70</td><td>6.64</td><td>6.78</td></tr><tr><td>6.70</td><td>6.70</td><td>6.75</td><td>6.79</td></tr></table>

Assume a normal population. 

38. The following are independent samples from two normal populations, both of which have the same standard deviation σ . 

$$
\begin{array}{l} 1 6, 1 7, 1 9, 2 0, 1 8 \quad \text { and } \quad 3, 4, 8 \end{array}
$$

Use them to estimate σ . 

39. The amount of beryllium in a substance is often determined by the use of a photometric filtration method. If the weight of the beryllium is µ, then the value given by the photometric filtration method is normally distributed with mean µ and standard deviation σ . A total of eight independent measurements of 3.180 mg of beryllium gave the following results. 

3.166, 3.192, 3.175, 3.180, 3.182, 3.171, 3.184, 3.177 

Use the preceding data to 

(a) estimate σ ; 

(b) find a 90 percent confidence interval estimate of $\sigma$ . 

40. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population, explain how to obtain a 100(1 − α) percent confidence interval for the population variance $\sigma ^ { 2 }$ when the population mean µ is known. Explain in what sense knowledge of $\dot { \mu }$ improves the interval estimator compared with when it is unknown. 

Repeat Problem 38 if it is known that the mean burning time is 53.6 seconds. 

41. A civil engineer wishes to measure the compressive strength of two different types of concrete. A random sample of 10 specimens of the first type yielded the following data (in psi) 

$$
\begin{array}{r l} \text {Type 1:} & 3, 2 5 0, \quad 3, 2 6 8, \quad 4, 3 0 2, \quad 3, 1 8 4, \quad 3, 2 6 6 \\ & 3, 2 9 7, \quad 3, 3 3 2, \quad 3, 5 0 2, \quad 3, 0 6 4, \quad 3, 1 1 6 \end{array}
$$

whereas a sample of 10 specimens of the second yielded the data 

<table><tr><td>Type 2:</td><td>3,094,</td><td>3,106,</td><td>3,004,</td><td>3,066,</td><td>2,984,</td></tr><tr><td></td><td>3,124,</td><td>3,316,</td><td>3,212,</td><td>3,380,</td><td>3,018</td></tr></table>

If we assume that the samples are normal with a common variance, determine 

(a) a 95 percent two-sided confidence interval for $\mu _ { 1 } - \mu _ { 2 }$ , the difference in means; 

(b) a 95 percent one-sided upper confidence interval for $\mu _ { 1 } - \mu _ { 2 } ;$ 

(c) a 95 percent one-sided lower confidence interval for $\mu _ { 1 } - \mu _ { 2 }$ 

42. Independent random samples are taken from the output of two machines on a production line. The weight of each item is of interest. From the first machine, a sample of size 36 is taken, with sample mean weight of 120 grams and a sample variance of 4. From the second machine, a sample of size 64 is taken, with a sample mean weight of 130 grams and a sample variance of 5. It is assumed that the weights of items from the first machine are normally distributed with mean $\mu _ { 1 }$ and variance $\sigma ^ { 2 }$ , and that the weights of items from the second machine are normally distributed with mean $\mu _ { 2 }$ and variance $\sigma ^ { 2 }$ (that is, the variances are assumed to be equal). Find a 99 percent confidence interval for $\mu _ { 1 } - \mu _ { 2 }$ , the difference in population means. 

43. Do Problem 42 when it is known in advance that the population variances are 4 and 5. 

44. The following are the burning times in seconds of floating smoke pots of two different types. 

<table><tr><td colspan="2">Type I</td><td colspan="2">Type II</td></tr><tr><td>481</td><td>572</td><td>526</td><td>537</td></tr><tr><td>506</td><td>561</td><td>511</td><td>582</td></tr><tr><td>527</td><td>501</td><td>556</td><td>605</td></tr><tr><td>661</td><td>487</td><td>542</td><td>558</td></tr><tr><td>501</td><td>524</td><td>491</td><td>578</td></tr></table>

Find a 99 percent confidence interval for the mean difference in burning times assuming normality with unknown but equal variances. 

45. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population having known mean $\mu _ { 1 }$ and unknown variance $\sigma _ { 1 } ^ { 2 }$ , and $Y _ { 1 } , \dots , Y _ { m }$ is an independent sample from a normal population having known mean $\mu _ { 2 }$ and unknown variance $\sigma _ { 2 } ^ { 2 }$ determine a $1 0 0 ( 1 - \alpha )$ percent confidence interval for $\sigma _ { 1 } ^ { 2 } / \sigma _ { 2 } ^ { 2 }$ 

46. Two analysts took repeated readings on the hardness of city water. Assuming that the readings of analyst i constitute a sample from a normal population having variance $\sigma _ { i } ^ { 2 } , i = 1 , 2$ , compute a 95 percent two-sided confidence interval for $\sigma _ { 1 } ^ { 2 } / \sigma _ { 2 } ^ { 2 }$ when the data are as follows: 

<table><tr><td colspan="2">Coded Measures of Hardness</td></tr><tr><td>Analyst 1</td><td>Analyst 2</td></tr><tr><td>.46</td><td>.82</td></tr><tr><td>.62</td><td>.61</td></tr><tr><td>.37</td><td>.89</td></tr><tr><td>.40</td><td>.51</td></tr><tr><td>.44</td><td>.33</td></tr><tr><td>.58</td><td>.48</td></tr><tr><td>.48</td><td>.23</td></tr><tr><td>.53</td><td>.25</td></tr><tr><td></td><td>.67</td></tr><tr><td></td><td>.88</td></tr></table>

47. A problem of interest in baseball is whether a sacrifice bunt is a good strategy when there is a man on first base and no outs. Assuming that the bunter will be out but will be successful in advancing the man on base, we could compare the probability of scoring a run with a player on first base and no outs with the probability of scoring a run with a player on second base and one out. The following data resulted from a study of randomly chosen major league baseball games played in 1959 and 1960. 

(a) Give a 95 percent confidence interval estimate for the probability of scoring at least one run when there is a man on first and no outs. 

(b) Give a 95 percent confidence interval estimate for the probability of scoring at least one run when there is a man on second and one out. 

<table><tr><td>Base Occupied</td><td>Number of Outs</td><td>Number of Cases in Which 0 Runs Are Scored</td><td>Total Number of Cases</td></tr><tr><td>First</td><td>0</td><td>1,044</td><td>1,728</td></tr><tr><td>Second</td><td>1</td><td>401</td><td>657</td></tr></table>

48. A random sample of 1,200 engineers included 48 Hispanic Americans, 80 African Americans, and 204 females. Determine 90 percent confidence intervals for the proportion of all engineers that are 

(a) female; 

(b) Hispanic Americans or African Americans. 

49. To estimate p, the proportion of all newborn babies that are male, the gender of 10,000 newborn babies was noted. If 5,106 of them were male, determine (a) a 90 percent and (b) a 99 percent confidence interval estimate of p. 

50. An airline is interested in determining the proportion of its customers who are flying for reasons of business. If they want to be 90 percent certain that their estimate will be correct to within 2 percent, how large a random sample should they select? 

51. A recent newspaper poll indicated that Candidate A is favored over Candidate B by a 53 to 47 percentage, with a margin of error of ±4 percent. The newspaper then stated that since the 6-point gap is larger than the margin of error, its readers can be certain that Candidate A is the current choice. Is this reasoning correct? 

52. A market research firm is interested in determining the proportion of households that are watching a particular sporting event. To accomplish this task, they plan on using a telephone poll of randomly chosen households. How large a sample is needed if they want to be 90 percent certain that their estimate is correct to within ±.02? 

53. In a recent study, 79 of 140 meteorites were observed to enter the atmosphere with a velocity of less than 25 miles per second. If we take $\hat { p } = 7 9 / 1 4 0$ as an estimate of the probability that an arbitrary meteorite that enters the atmosphere will have a speed less than 25 miles per second, what can we say, with 99 percent confidence, about the maximum error of our estimate? 

54. A random sample of 100 items from a production line revealed 17 of them to be defective. Compute a 95 percent two-sided confidence interval for the probability that an item produced is defective. Determine also a 99 percent upper confidence interval for this value. What assumptions are you making? 

55. Of 100 randomly detected cases of individuals having lung cancer, 67 died within 5 years of detection. 

(a) Estimate the probability that a person contracting lung cancer will die within 5 years. 

(b) How large an additional sample would be required to be 95 percent confident that the error in estimating the probability in part (a) is less than .02? 

56. Derive 100(1 − α) percent lower and upper confidence intervals for p, when the data consist of the values of n independent Bernoulli random variables with parameter p. 

57. Suppose the lifetimes of batteries are exponentially distributed with mean θ . If the average of a sample of 10 batteries is 36 hours, determine a 95 percent two-sided confidence interval for θ. 

58. Determine $1 0 0 ( 1 - \alpha )$ percent one-sided upper and lower confidence intervals for θ in Problem 57. 

59. Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ denote a sample from a population whose mean value θ is unknown. Use the results of Example 7.7b to argue that among all unbiased estimators of θ of the form $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \lambda _ { i } \bar { X _ { i } } , \sum _ { i = 1 } ^ { n } \lambda _ { i } = \bar { 1 } } \end{array}$ , the one with minimal mean square error has $\lambda _ { i } \equiv 1 / n , i = 1 , \ldots , n .$ 

60. Consider two independent samples from normal populations having the same variance $\sigma ^ { 2 }$ , of respective sizes n and m. That is, $X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { m }$ are independent samples from normal populations each having variance $\sigma ^ { 2 }$ . Let $S _ { x } ^ { 2 }$ and $\mathsf { \bar { S } } _ { y } ^ { 2 }$ denote the respective sample variances. Thus both $S _ { x } ^ { 2 }$ and $S _ { y } ^ { 2 }$ are unbiased estimators of $\sigma ^ { 2 }$ . Show by using the results of Example 7.7b along with the fac that 

$$
\mathrm{Var} (\chi_ {k} ^ {2}) = 2 k
$$

where $\chi _ { k } ^ { 2 }$ is chi-square with k degrees of freedom, that the minimum mean square estimator of $\sigma ^ { 2 }$ of the form $\lambda S _ { x } ^ { 2 } + ( 1 - \lambda ) S _ { y } ^ { 2 }$ is 

$$
S _ {p} ^ {2} = \frac {(n - 1) S _ {x} ^ {2} + (m - 1) S _ {y} ^ {2}}{n + m - 2}
$$

This is called the pooled estimator of $\sigma ^ { 2 }$ . 

61. Consider two estimators $d _ { 1 }$ and $d _ { 2 }$ of a parameter θ . If $E [ d _ { 1 } ] ~ = ~ \theta$ $\mathrm { V a r } ( d _ { 1 } ) = 6$ and $E [ d _ { 2 } ] = \theta + 2 , { \mathrm { V a r } } ( d _ { 2 } ) = 2$ , which estimator should be preferred? 

62. Suppose that the number of accidents occurring daily in a certain plant has a Poisson distribution with an unknown mean λ. Based on previous experience in similar industrial plants, suppose that a statistician’s initial feelings about the possible value of λ can be expressed by an exponential distribution with parameter 1. That is, the prior density is 

$$
p (\lambda) = e ^ {- \lambda}, \qquad 0 <   \lambda <   \infty
$$

Determine the Bayes estimate of λ if there are a total of 83 accidents over the next 10 days. What is the maximum likelihood estimate? 

63. The functional lifetimes in hours of computer chips produced by a certain semiconductor firm are exponentially distributed with mean $1 / \lambda$ . Suppose that the prior distribution on λ is the gamma distribution with density function 

$$
g (x) = \frac {e ^ {- x} x ^ {2}}{2}, \qquad 0 <   x <   \infty
$$

If the average life of the first 20 chips tested is 4.6 hours, compute the Bayes estimate of $\gimel$ . 

64. Each item produced will, independently, be defective with probability $\scriptstyle { \boldsymbol { p } } .$ . If the prior distribution on $\boldsymbol { \underline { P } }$ is uniform on (0, 1), compute the posterior probability that $\boldsymbol { \underline { P } }$ is less than .2 given 

(a) a total of 2 defectives out of a sample of size 10; 

(b) a total of 1 defective out of a sample of size 10; 

(c) a total of 10 defectives out of a sample of size 10. 

65. The breaking strength of a certain type of cloth is to be measured for 10 spec imens. The underlying distribution is normal with unknown mean θ but with a standard deviation equal to 3 psi. Suppose also that based on previous experience we feel that the unknown mean has a prior distribution that is normally dis tributed with mean 200 and standard deviation 2. If the average breaking strength of a sample of 20 specimens is 182 psi, determine a region that contains θ with probability .95. 

# HYPOTHESIS TESTING

## 8.1 INTRODUCTION

As in the previous chapter, let us suppose that a random sample from a population distri bution, specified except for a vector of unknown parameters, is to be observed. However, rather than wishing to explicitly estimate the unknown parameters, let us now suppose that we are primarily concerned with using the resulting sample to test some particular hypothesis concerning them. As an illustration, suppose that a construction firm has just purchased a large supply of cables that have been guaranteed to have an average breaking strength of at least 7,000 psi. To verify this claim, the firm has decided to take a random sample of 10 of these cables to determine their breaking strengths. They will then use the result of this experiment to ascertain whether or not they accept the cable manufacturer’s hypothesis that the population mean is at least 7,000 pounds per square inch. 

A statistical hypothesis is usually a statement about a set of parameters of a population distribution. It is called a hypothesis because it is not known whether or not it is true. A primary problem is to develop a procedure for determining whether or not the values of a random sample from this population are consistent with the hypothesis. For instance, consider a particular normally distributed population having an unknown mean value θ and known variance 1. The statement “θ is less than 1” is a statistical hypothesis that we could try to test by observing a random sample from this population. If the random sample is deemed to be consistent with the hypothesis under consideration, we say that the hypothesis has been “accepted”; otherwise we say that it has been “rejected.” 

Note that in accepting a given hypothesis we are not actually claiming that it is true but rather we are saying that the resulting data appear to be consistent with it. For instance, in the case of a normal (θ , 1) population, if a resulting sample of size 10 has an average value of 1.25, then although such a result cannot be regarded as being evidence in favor of the hypothesis $^ { \infty } \theta \ < 1 , ^ { \infty }$ it is not inconsistent with this hypothesis, which would thus be accepted. On the other hand, if the sample of size 10 has an average value of 3, then even though a sample value that large is possible when $\theta < 1$ , it is so unlikely that it seem inconsistent with this hypothesis, which would thus be rejected. 

## 8.2 SIGNIFICANCE LEVELS

Consider a population having distribution $F _ { \theta }$ , where $\theta$ is unknown, and suppose we want to test a specific hypothesis about $\theta .$ . We shall denote this hypothesis by $H _ { 0 }$ and call it the null hypothesis. For example, if $F _ { \theta }$ is a normal distribution function with mean $\theta$ and variance equal to 1, then two possible null hypotheses about $\theta$ are 

$$
\begin{array}{l} \text {(a)} H _ {0}: \theta = 1 \\ \text {(b)} H _ {0}: \theta \leq 1 \end{array}
$$

Thus the first of these hypotheses states that the population is normal with mean 1 and variance 1, whereas the second states that it is normal with variance 1 and a mean less than or equal to 1. Note that the null hypothesis in (a), when true, completely specifies the population distribution; whereas the null hypothesis in (b) does not. A hypothesis that, when true, completely specifies the population distribution is called a simple hypothesis; one that does not is called a composite hypothesis. 

Suppose now that in order to test a specific null hypothesis $H _ { 0 }$ , a population sample of size $n { \longrightarrow } \operatorname* { s a y } X _ { 1 } , \dotsc , X _ { n } -$ is to be observed. Based on these n values, we must decide whether or not to accept $H _ { 0 }$ . A test for $H _ { 0 }$ can be specified by defining a region $C$ in n-dimensional space with the proviso that the hypothesis is to be rejected if the random sample $X _ { 1 } , \ldots , X _ { n }$ turns out to lie in $C$ and accepted otherwise. The region $C$ is called the critical region. In other words, the statistical test determined by the critical region $C$ is the one that 

$$
\text { accepts } \quad H _ {0} \quad \text { if } \quad (X _ {1}, X _ {2}, \ldots , X _ {n}) \not \in C
$$

and 

$$
\text { rejects } \quad H _ {0} \quad \text { if } \quad (X _ {1}, \ldots , X _ {n}) \in C
$$

For instance, a common test of the hypothesis that $\theta _ { ; }$ , the mean of a normal population with variance 1, is equal to 1 has a critical region given by 

$$
C = \left\{(X _ {1}, \dots , X _ {n}): \left| \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n} - 1 \right| > \frac {1 . 9 6}{\sqrt {n}} \right\}\tag{8.2.1}
$$

Thus, this test calls for rejection of the null hypothesis that $\theta = 1$ when the sample average differs from 1 by more than 1.96 divided by the square root of the sample size. 

It is important to note when developing a procedure for testing a given null hypothesis $H _ { 0 }$ that, in any test, two different types of errors can result. The first of these, called a type I error, is said to result if the test incorrectly calls for rejecting $H _ { 0 }$ when it is indeed correct. The second, called a type II error, results if the test calls for accepting $H _ { 0 }$ when it is false. 

Now, as was previously mentioned, the objective of a statistical test of $\dot { H } _ { 0 }$ is not to explicitly determine whether or not $H _ { 0 }$ is true but rather to determine if its validity is consistent with the resultant data. Hence, with this objective it seems reasonable that $H _ { 0 }$ should only be rejected if the resultant data are very unlikely when $H _ { 0 }$ is true. The classical way of accomplishing this is to specify a value $\alpha$ and then require the test to have the property that whenever $H _ { 0 }$ is true its probability of being rejected is never greater than $\alpha .$ . The value $\alpha _ { ; }$ , called the level of significance of the test, is usually set in advance, with commonly chosen values being $\alpha = . 1 , . 0 5 , . 0 0 5$ . In other words, the classical approach to testing $H _ { 0 }$ is to fix a significance level α and then require that the test have the property that the probability of a type I error occurring can never be greater than $\alpha .$ 

Suppose now that we are interested in testing a certain hypothesis concerning $\theta ,$ , an unknown parameter of the population. Specifically, for a given set of parameter values $w ,$ suppose we are interested in testing 

$$
H _ {0}: \theta \in w
$$

A common approach to developing a test of $H _ { 0 } ,$ , say at level of significance $\alpha ,$ , is to start by determining a point estimator of $\theta - s a y d ( \mathbf { X } )$ . The hypothesis is then rejected if $d ( \mathbf { X } )$ is “far away” from the region $w .$ . However, to determine how “far away” it need be to justify rejection of $H _ { 0 }$ , we need to determine the probability distribution of $d ( \mathbf { X } )$ when $H _ { 0 }$ is true since this will usually enable us to determine the appropriate critical region so as to make the test have the required significance level $\alpha .$ . For example, the test of the hypothesis that the mean of a normal (θ , 1) population is equal to 1, given by Equation 8.2.1, call for rejection when the point estimate of θ — that is, the sample average — is farther than $1 . 9 6 / \sqrt { n }$ away from 1. As we will see in the next section, the value $1 . 9 6 / \sqrt { n }$ was chosen to meet a level of significance of $\alpha = . 0 5$ 

## 8.3 TESTS CONCERNING THE MEAN OF A NORMAL POPULATION

## 8.3.1 Case of Known Variance

Suppose that $X _ { 1 } , \ldots , X _ { n }$ is a sample of size n from a normal distribution having an unknown mean $\mu$ and a known variance $\sigma ^ { 2 }$ and suppose we are interested in testing the null hypothesis 

$$
H _ {0}: \mu = \mu_ {0}
$$

against the alternative hypothesis 

$$
H _ {1}: \mu \neq \mu_ {0}
$$

where $\mu _ { 0 }$ is some specified constant. 

Since $\textstyle { \overline { { X } } } = \sum _ { i = 1 } ^ { n } X _ { i } / n$ is a natural point estimator of ${ \bf \dot { \mu } } _ { \mu }$ , it seems reasonable to accept $H _ { 0 }$ if X is not too far from $\mu _ { 0 }$ . That is, the critical region of the test would be of the form 

$$
C = \{X _ {1}, \ldots , X _ {n}: | \overline {{X}} - \mu_ {0} | > c \}\tag{8.3.1}
$$

for some suitably chosen value $c .$ 

If we desire that the test has significance level $\alpha ,$ , then we must determine the critical value $c$ in Equation 8.3.1 that will make the type I error equal to $\alpha .$ . That is, c must be such that 

$$
P _ {\mu_ {0}} \{| \overline {{X}} - \mu_ {0} | > c \} = \alpha\tag{8.3.2}
$$

where we write $P _ { \mu _ { 0 } }$ to mean that the preceding probability is to be computed under the assumption that $\mu = \mu _ { 0 }$ . However, when $\mu = \mu _ { 0 } , { \overline { { X } } }$ will be normally distributed with mean $\mu _ { 0 }$ and variance $\sigma ^ { 2 } / n$ and so $Z _ { i }$ , defined by 

$$
Z \equiv \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}}
$$

will have a standard normal distribution. Now Equation 8.3.2 is equivalent to 

$$
P \left\{| Z | > \frac {c \sqrt {n}}{\sigma} \right\} = \alpha
$$

or, equivalently, 

$$
2 P \left\{Z > \frac {c \sqrt {n}}{\sigma} \right\} = \alpha
$$

where $Z$ is a standard normal random variable. However, we know that 

$$
P \{Z > z _ {\alpha / 2} \} = \alpha / 2
$$

and so 

$$
\frac {c \sqrt {n}}{\sigma} = z _ {\alpha / 2}
$$

or 

$$
c = \frac {z _ {\alpha / 2} \sigma}{\sqrt {n}}
$$

Thus, the significance level $\alpha$ test is to reject H if $| \overline { { X } } - \mu _ { 0 } | > z _ { \alpha / 2 } \sigma / \sqrt { n }$ and accept otherwise; or, equivalently, to 

$$
\text { reject } \quad H _ {0} \quad \text { if } \quad \frac {\sqrt {n}}{\sigma} | \overline {{X}} - \mu_ {0} | > z _ {\alpha / 2}\tag{8.3.3}
$$

$$
\text {   accept   } \quad H _ {0} \quad \text {   if   } \quad \frac {\sqrt {n}}{\sigma} | \overline {{X}} - \mu_ {0} | \leq z _ {\alpha / 2}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/21fdcbc97156c863a5154ea75a6e5b22435d315c7722498ba4c5445b4b4911ba.jpg)



FIGURE 8.1


This can be pictorially represented as shown in Figure 8.1, where we have superim posed the standard normal density function [which is the density of the test statistic ${ \sqrt { n } } ( { \overline { { X } } } - \mu _ { 0 } ) /$ /σ when $H _ { 0 }$ is true]. 

EXAMPLE 8.3a It is known that if a signal of value $\mu$ is sent from location $\mathsf { A } ,$ then the value received at location B is normally distributed with mean $\mu$ and standard deviation 2. That is, the random noise added to the signal is an $N ( 0 , 4 )$ random variable. There i reason for the people at location B to suspect that the signal value $\mu = 8$ will be sent today. Test this hypothesis if the same signal value is independently sent five times and the average value received at location B is ${ \overline { { \overline { { X } } } } } = 9 . 5$ 

SOLUTION Suppose we are testing at the 5 percent level of significance. To begin, we compute the test statistic 

$$
\frac {\sqrt {n}}{\sigma} | \overline {{X}} - \mu_ {0} | = \frac {\sqrt {5}}{2} (1. 5) = 1. 6 8
$$

Since this value is less than $z _ { . 0 2 5 } = 1 . 9 6$ , the hypothesis is accepted. In other words, the data are not inconsistent with the null hypothesis in the sense that a sample average as far from the value 8 as observed would be expected, when the true mean is 8, over 5 percent of the time. Note, however, that if a less stringent significance level were chosen — say $\alpha = . 1$ — then the null hypothesis would have been rejected. This follows since $z _ { . 0 5 } = 1 . 6 4 5$ , which is less than 1.68. Hence, if we would have chosen a test that had a 10 percent chance of rejecting $H _ { 0 }$ when $H _ { 0 }$ was true, then the null hypothesis would have been rejected. 

The “correct” level of significance to use in a given situation depends on the individ ual circumstances involved in that situation. For instance, if rejecting a null hypothesis $H _ { 0 }$ would result in large costs that would thus be lost if $H _ { 0 }$ were indeed true, then we might elect to be quite conservative and so choose a significance level of .05 or .01. Also, if we initially feel strongly that $H _ { 0 }$ was correct, then we would require very stringent data evidence to the contrary for us to reject $H _ { 0 }$ . (That is, we would set a very low significance level in this situation.) ■ 

The test given by Equation 8.3.3 can be described as follows: For any observed value of the test statistic ${ \sqrt { n } } | { \overline { { X } } } - \mu _ { 0 } | / \sigma$ , call it $\nu ,$ the test calls for rejection of the null hypothesis if the probability that the test statistic would be as large as v when $H _ { 0 }$ is true is less than or equal to the significance level α. From this, it follows that we can determine whether or not to accept the null hypothesis by computing, first, the value of the test statistic and, second, the probability that a unit normal would (in absolute value) exceed that quantity. This probability — called the $\scriptstyle { p \cdotp }$ -value of the test — gives the critical significance level in the sense that $H _ { 0 }$ will be accepted if the significance level $\alpha$ is less than the $\scriptstyle { p - { \frac { } { } } }$ -value and rejected if it is greater than or equal. 

In practice, the significance level is often not set in advance but rather the data are looked at to determine the resultant p-value. Sometimes, this critical significance level is clearly much larger than any we would want to use, and so the null hypothesis can be readily accepted. At other times the $\scriptstyle { p \cdotp }$ -value is so small that it is clear that the hypothesis should be rejected. 

EXAMPLE 8.3b In Example 8.3a, suppose that the average of the 5 values received is $\overline { { X } } = 8 . 5$ . In this case, 

$$
\frac {\sqrt {n}}{\sigma} | \overline {{{X}}} - \mu_ {0} | = \frac {\sqrt {5}}{4} = . 5 5 9
$$

Since 

$$
\begin{array}{r l} P \{| Z | >. 5 5 9 \} & = 2 P \{Z >. 5 5 9 \} \\ & = 2 \times . 2 8 8 = . 5 7 6 \end{array}
$$

it follows that the p-value is .576 and thus the null hypothesis $H _ { 0 }$ that the signal sent has value 8 would be accepted at any significance level $\alpha < . 5 7 6$ . Since we would clearly never want to test a null hypothesis using a significance level as large as $. 5 7 6 , H _ { 0 }$ would be accepted. 

On the other hand, if the average of the data values were 11.5, then the p-value of the test that the mean is equal to 8 would be 

$$
\begin{array}{c} P \{| Z | > 1. 7 5 \sqrt {5} \} = P \{| Z | > 3. 9 1 3 \} \\ \approx . 0 0 0 0 5 \end{array}
$$

For such a small $\scriptstyle { p \cdotp }$ -value, the hypothesis that the value 8 was sent is rejected. ■ 

We have not yet talked about the probability of a type II error — that is, the probability of accepting the null hypothesis when the true mean $\mu$ is unequal to $\mu _ { 0 }$ . This probability will depend on the value of $\mu _ { ; }$ , and so let us define $\beta ( \mu )$ by 

$$
\begin{array}{l} \beta (\mu) = P _ {\mu} \{\text { acceptance   of } H _ {0} \} \\ \qquad = P _ {\mu} \left\{\left| \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} \right| \leq z _ {\alpha / 2} \right\} \\ \qquad = P _ {\mu} \left\{- z _ {\alpha / 2} \leq \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} \leq z _ {\alpha / 2} \right\} \end{array}
$$

The function $\beta ( \mu )$ is called the operating characteristic (or OC) curve and represents the probability that $H _ { 0 }$ will be accepted when the true mean is $\mu$ . 

To compute this probability, we use the fact that $\overline { { X } }$ is normal with mean $\mu$ and variance $\sigma ^ { 2 } / n$ and so 

$$
Z \equiv \frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} \sim \mathcal {N} (0, 1)
$$

Hence, 

$$
\begin{array}{l} \beta (\mu) = P _ {\mu} \left\{- z _ {\alpha / 2} \leq \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} \leq z _ {\alpha / 2} \right\} \\ = P _ {\mu} \left\{- z _ {\alpha / 2} - \frac {\mu}{\sigma / \sqrt {n}} \leq \frac {\overline {{X}} - \mu_ {0} - \mu}{\sigma / \sqrt {n}} \leq z _ {\alpha / 2} - \frac {\mu}{\sigma / \sqrt {n}} \right\} \\ = P _ {\mu} \left\{- z _ {\alpha / 2} - \frac {\mu}{\sigma / \sqrt {n}} \leq Z - \frac {\mu_ {0}}{\sigma / \sqrt {n}} \leq z _ {\alpha / 2} - \frac {\mu}{\sigma / \sqrt {n}} \right\} \\ = P \left\{\frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} - z _ {\alpha / 2} \leq Z \leq \frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} + z _ {\alpha / 2} \right\} \\ = \Phi \left(\frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} + z _ {\alpha / 2}\right) - \Phi \left(\frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} - z _ {\alpha / 2}\right) \end{array}\tag{8.3.4}
$$

where $\Phi$ is the standard normal distribution function. 

For a fixed significance level $\alpha _ { ; }$ , the OC curve given by Equation 8.3.4 is symmetric about $\mu _ { 0 }$ and indeed will depend on $\mu$ only through $( \sqrt { n } / \sigma ) | \mu - \mu _ { 0 } |$ . This curve with the abscissa changed from $\mu$ to $d = ( { \sqrt { n } } / \sigma ) | \mu - \mu _ { 0 } |$ is presented in Figure 8.2 when $\alpha = . 0 5$ 

EXAMPLE 8.3c For the problem presented in Example 8.3a, let us determine the probability of accepting the null hypothesis that $\mu = 8$ when the actual value sent is 10. To do so, we compute 

$$
\frac {\sqrt {n}}{\sigma} (\mu_ {0} - \mu) = - \frac {\sqrt {5}}{2} \times 2 = - \sqrt {5}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/fba2b0306e27179100b91aaf808d02a3ca64dd01ead55a9a8172062d4c97f019.jpg)



FIGURE 8.2 The OC curve for the two-sided normal test for significance level $\alpha = . 0 5$



$\mathrm { A } s z _ { . 0 2 5 } = 1 . 9 6$ , the desired probability is, from Equation 8.3.4,


$$
\begin{array}{r l} & {\Phi (- \sqrt {5} + 1. 9 6) - \Phi (- \sqrt {5} - 1. 9 6)} \\ & {\quad = 1 - \Phi (\sqrt {5} - 1. 9 6) - [ 1 - \Phi (\sqrt {5} + 1. 9 6) ]} \\ & {\quad = \Phi (4. 1 9 6) - \Phi (. 2 7 6)} \\ & {\quad = . 3 9 2 \quad \blacksquare} \end{array}
$$

## REMARK

The function $1 - \beta ( \mu )$ is called the power-function of the test. Thus, for a given value $\mu ,$ the power of the test is equal to the probability of rejection when $\mu$ is the true value. ■ 

The operating characteristic function is useful in determining how large the random sample need be to meet certain specifications concerning type II errors. For instance, suppose that we desire to determine the sample size n necessary to ensure that the probability of accepting $H _ { 0 } : \mu = \mu _ { 0 }$ when the true mean is actually $\mu _ { 1 }$ is approximately $\beta .$ . That is, we want n to be such that 

$$
\beta (\mu_ {1}) \approx \beta
$$

But from Equation 8.3.4, this is equivalent to 

$$
\Phi \left(\frac {\sqrt {n} (\mu_ {0} - \mu_ {1})}{\sigma} + z _ {\alpha / 2}\right) - \Phi \left(\frac {\sqrt {n} (\mu_ {0} - \mu_ {1})}{\sigma} - z _ {\alpha / 2}\right) \approx \beta\tag{8.3.5}
$$

Although the foregoing cannot be analytically solved for n, a solution can be obtained by using the standard normal distribution table. In addition, an approximation for n can be derived from Equation 8.3.5 as follows. To start, suppose that $\mu _ { 1 } > \mu _ { 0 }$ . Then, because this implies that 

$$
\frac {\mu_ {0} - \mu_ {1}}{\sigma / \sqrt {n}} - z _ {\alpha / 2} \leq - z _ {\alpha / 2}
$$

it follows, since $\Phi$ is an increasing function, that 

$$
\Phi \left(\frac {\mu_ {0} - \mu_ {1}}{\sigma / \sqrt {n}} - z _ {\alpha / 2}\right) \leq \Phi (- z _ {\alpha / 2}) = P \{Z \leq - z _ {\alpha / 2} \} = P \{Z \geq z _ {\alpha / 2} \} = \alpha / 2
$$

Hence, we can take 

$$
\Phi \left(\frac {\mu_ {0} - \mu_ {1}}{\sigma / \sqrt {n}} - z _ {\alpha / 2}\right) \approx 0
$$

and so from Equation 8.3.5 

$$
\beta \approx \Phi \left(\frac {\mu_ {0} - \mu_ {1}}{\sigma / \sqrt {n}} + z _ {\alpha / 2}\right)\tag{8.3.6}
$$

or, since 

$$
\beta = P \{Z > z _ {\beta} \} = P \{Z <   - z _ {\beta} \} = \Phi (- z _ {\beta})
$$

we obtain from Equation 8.3.6 that 

$$
- z _ {\beta} \approx (\mu_ {0} - \mu_ {1}) \frac {\sqrt {n}}{\sigma} + z _ {\alpha / 2}
$$

or 

$$
n \approx \frac {(z _ {\alpha / 2} + z _ {\beta}) ^ {2} \sigma^ {2}}{(\mu_ {1} - \mu_ {0}) ^ {2}}\tag{8.3.7}
$$

In fact, the same approximation would result when $\mu _ { 1 } ~ < ~ \mu _ { 0 }$ (the details are left as an exercise) and so Equation 8.3.7 is in all cases a reasonable approximation to the sample size necessary to ensure that the type II error at the value $\mu = \mu _ { 1 }$ is approximately equal to $\beta$ . 

EXAMPLE 8.3d For the problem of Example 8.3a, how many signals need be sent so that the .05 level test of $H _ { 0 } : \mu = 8$ has at least a 75 percent probability of rejection when $\mu = 9 . 2 ?$ 

SOLUTION Since $z _ { . 0 2 5 } = 1 . 9 6 , z _ { . 2 5 } = . 6 7$ , the approximation 8.3.7 yields 

$$
n \approx \frac {(1 . 9 6 + . 6 7) ^ {2}}{(1 . 2) ^ {2}} 4 = 1 9. 2 1
$$

Hence a sample of size 20 is needed. From Equation 8.3.4, we see that with $n = 2 0$ 

$$
\begin{array}{l} \beta (9. 2) = \Phi \left(- \frac {1 . 2 \sqrt {2 0}}{2} + 1. 9 6\right) - \Phi \left(- \frac {1 . 2 \sqrt {2 0}}{2} - 1. 9 6\right) \\ = \Phi (-. 7 2 3) - \Phi (- 4. 6 4 3) \end{array}
$$

$$
\begin{array}{l} \approx 1 - \Phi (. 7 2 3) \\ \approx . 2 3 5 \end{array}
$$

Therefore, if the message is sent 20 times, then there is a 76.5 percent chance that the null hypothesis $\mu = 8$ will be rejected when the true mean is 9.2. ■ 

## ONE-SIDED TESTS

In testing the null hypothesis that $\mu = \mu _ { 0 }$ , we have chosen a test that calls for rejection when $\overline { { \boldsymbol X } }$ is far from $\mu _ { 0 }$ . That is, a very small value of $\overline { { \boldsymbol X } }$ or a very large value appears to make it unlikely that $\mu$ (which $\overline { { \boldsymbol X } }$ is estimating) could equal $\mu _ { 0 }$ . However, what happens when the only alternative to $\mu$ being equal to $\mu _ { 0 }$ is for $\mu$ to be greater than $\mu _ { 0 } ?$ That is, what happens when the alternative hypothesis to $H _ { 0 } : \mu = \mu _ { 0 }$ is $H _ { 1 } : \mu > \mu _ { 0 } ?$ Clearly, in this latter case we would not want to reject $H _ { 0 }$ when X is small (since a small X is more likely when $H _ { 0 }$ is true than when $H _ { 1 }$ is true). Thus, in testing 

$$
H _ {0}: \mu = \mu_ {0} \quad \text { versus } \quad H _ {1}: \mu > \mu_ {0}\tag{8.3.8}
$$

we should reject $H _ { 0 }$ when ${ \overline { { X } } } ,$ , the point estimate of $\mu _ { 0 }$ , is much greater than $\mu _ { 0 }$ . That is, the critical region should be of the following form: 

$$
C = \{(X _ {1}, \ldots , X _ {n}): \overline {{X}} - \mu_ {0} > c \}
$$

Since the probability of rejection should equal α when $H _ { 0 }$ is true (that is, when $\mu = \mu _ { 0 } )$ we require that c be such that 

$$
P _ {\mu_ {0}} \{\overline {{X}} - \mu_ {0} > c \} = \alpha\tag{8.3.9}
$$

But since 

$$
Z = \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}}
$$

has a standard normal distribution when $H _ { 0 }$ is true, Equation 8.3.9 is equivalent to 

$$
P \left\{Z > \frac {c \sqrt {n}}{\sigma} \right\} = \alpha
$$

when $Z$ is a standard normal. But since 

$$
P \{Z > z _ {\alpha} \} = \alpha
$$

we see that 

$$
c = \frac {z _ {\alpha} \sigma}{\sqrt {n}}
$$

Hence, the test of the hypothesis 8.3.8 is to reject $H _ { 0 }$ i $: \overline { { X } } - \mu _ { 0 } > z _ { \alpha } \sigma / \sqrt { n } ;$ , and accept otherwise; or, equivalently, to 

$$
\begin{array}{l l l l} \text {accept} & H _ {0} & \text {if} & \frac {\sqrt {n}}{\sigma} (\overline {{X}} - \mu_ {0}) \leq z _ {\alpha} \\ \text {reject} & H _ {0} & \text {if} & \frac {\sqrt {n}}{\sigma} (\overline {{X}} - \mu_ {0}) > z _ {\alpha} \end{array}\tag{8.3.10}
$$

This is called a one-sided critical region (since it calls for rejection only when $\overline { { X } }$ is large). Correspondingly, the hypothesis testing problem 

$$
\begin{array}{l} {H _ {0}: \mu = \mu_ {0}} \\ {H _ {1}: \mu > \mu_ {0}} \end{array}
$$

is called a one-sided testing problem (in contrast to the two-sided problem that results when the alternative hypothesis is $H _ { 1 } : \mu \neq \mu _ { 0 } )$ 

To compute the p-value in the one-sided test, Equation 8.3.10, we first use the data to determine the value of the statistic ${ \sqrt { n } } ( { \overline { { X } } } - \mu _ { 0 } ) / \sigma$ . The p-value is then equal to the probability that a standard normal would be at least as large as this value. 

EXAMPLE 8.3e Suppose in Example 8.3a that we know in advance that the signal value is at least as large as 8. What can be concluded in this case? 

SOLUTION To see if the data are consistent with the hypothesis that the mean is 8, we test 

$$
H _ {0}: \mu = 8
$$

against the one-sided alternative 

$$
H _ {1}: \mu > 8
$$

The value of the test statistic is ${ \sqrt { n } } ( { \overline { { X } } } - \mu _ { 0 } ) / \sigma = { \sqrt { 5 } } ( 9 . 5 - 8 ) / 2 = 1 . 6 8$ , and the p-value is the probability that a standard normal would exceed 1.68, namely, 

$$
p \text {-value} = 1 - \Phi (1. 6 8) = . 0 4 6 5
$$

Since the test would call for rejection at all significance levels greater than or equal to .0465, it would, for instance, reject the null hypothesis at the $\alpha = . 0 5$ level of significance. ■ 

The operating characteristic function of the one-sided test, Equation 8.3.10, 

$$
\beta (\mu) = P _ {\mu} \{\mathrm{accepting} H _ {0} \}
$$

can be obtained as follows: 

$$
\begin{array}{r l} & {\beta (\mu) = P _ {\mu} \left\{\overline {{X}} \leq \mu_ {0} + z _ {\alpha} \frac {\sigma}{\sqrt {n}} \right\}} \\ & {\quad = P \left\{\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} \leq \frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} + z _ {\alpha} \right\}} \\ & {\quad = P \left\{Z \leq \frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} + z _ {\alpha} \right\}, Z \sim \mathcal {N} (0, 1)} \end{array}
$$

where the last equation follows since ${ \sqrt { n } } ( { \overline { { X } } } - \mu ) / \sigma$ has a standard normal distribution Hence we can write 

$$
\beta (\mu) = \Phi \left(\frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} + z _ {\alpha}\right)
$$

Since $\Phi ,$ , being a distribution function, is increasing in its argument, it follows that $\beta ( \mu )$ decreases in $\mu ;$ which is intuitively pleasing since it certainly seems reasonable that the larger the true mean $\mu ,$ , the less likely it should be to conclude that $\mu \leq \mu _ { 0 }$ . Also since $\Phi ( z _ { \alpha } ) = 1 - \alpha$ , it follows that 

$$
\beta (\mu_ {0}) = 1 - \alpha
$$

The test given by Equation 8.3.10, which was designed to test $H _ { 0 } : \mu = \mu _ { 0 }$ versus $H _ { 1 } : \mu > \mu _ { 0 }$ can also be used to test, at level of significance $\alpha ,$ , the one-sided hypothesis 

$$
H _ {0}: \mu \leq \mu_ {0}
$$

versus 

$$
H _ {1}: \mu > \mu_ {0}
$$

To verify that it remains a level α test, we need show that the probability of rejection is never greater than α when $H _ { 0 }$ is true. That is, we must verify that 

$$
1 - \beta (\mu) \leq \alpha \quad \text {   for   all   } \mu \leq \mu_ {0}
$$

or 

$$
\beta (\mu) \geq 1 - \alpha \quad \text {   for   all   } \mu \leq \mu_ {0}
$$

But it has previously been shown that for the test given by Equation 8.3.10, $\beta ( \mu )$ decreases in $\mu$ and $\beta ( \mu _ { 0 } ) = 1 - \alpha$ . This gives that 

$$
\beta (\mu) \geq \beta (\mu_ {0}) = 1 - \alpha \quad \mathrm{forall} \mu \leq \mu_ {0}
$$

which shows that the test given by Equation 8.3.10 remains a level α test for $H _ { 0 } : \mu \le \mu _ { 0 }$ against the alternative hypothesis $H _ { 1 } : \mu \leq \mu _ { 0 }$ 

## REMARK

We can also test the one-sided hypothesis 

$$
H _ {0}: \mu = \mu_ {0} \quad (\text { or } \mu \geq \mu_ {0}) \quad \text { versus } \quad H _ {1}: \mu <   \mu_ {0}
$$

at significance level α by 

$$
\begin{array}{l l} \text {   accepting   } & H _ {0} \quad \text {   if   } \quad \frac {\sqrt {n}}{\sigma} (\overline {{X}} - \mu_ {0}) \geq - z _ {\alpha} \\ \text {   rejecting   } & H _ {0} \quad \text {   otherwise   } \end{array}
$$

This test can alternatively be performed by first computing the value of the test statistic ${ \sqrt { n } } ( { \overline { { X } } } - \mu _ { 0 } ) / \sigma$ . The p-value would then equal the probability that a standard normal would be less than this value, and the hypothesis would be rejected at any significance level greater than or equal to this p-value. 

EXAMPLE 8.3f All cigarettes presently on the market have an average nicotine content of at least 1.6 mg per cigarette. A firm that produces cigarettes claims that it has discovered a new way to cure tobacco leaves that will result in the average nicotine content of a cigarette being less than 1.6 mg. To test this claim, a sample of 20 of the firm’s cigarettes were analyzed. If it is known that the standard deviation of a cigarette’s nicotine content is .8 mg, what conclusions can be drawn, at the 5 percent level of significance, if the average nicotine content of the 20 cigarettes is 1.54? 

Note: The above raises the question of how we would know in advance that the standard deviation is .8. One possibility is that the variation in a cigarette’s nicotine content is due to variability in the amount of tobacco in each cigarette and not on the method of curing that is used. Hence, the standard deviation can be known from previous experience. 

SOLUTION We must first decide on the appropriate null hypothesis. As was previously noted, our approach to testing is not symmetric with respect to the null and the alternative hypotheses since we consider only tests having the property that their probability of reject ing the null hypothesis when it is true will never exceed the significance level α. Thus, whereas rejection of the null hypothesis is a strong statement about the data not being consistent with this hypothesis, an analogous statement cannot be made when the nul hypothesis is accepted. Hence, since in the preceding example we would like to endorse the producer’s claims only when there is substantial evidence for it, we should take this claim as the alternative hypothesis. 

That is, we should test 

$$
H _ {0}: \mu \geq 1. 6 \quad \text { versus } \quad H _ {1}: \mu <   1. 6
$$

Now, the value of the test statistic is 

$$
\sqrt {n} (\overline {{X}} - \mu_ {0}) / \sigma = \sqrt {2 0} (1. 5 4 - 1. 6) /. 8 = -. 3 3 6
$$

and so the p-value is given by 

$$
\begin{array}{r l} p \text {-value} & = P \{Z <   -. 3 3 6 \}, \qquad Z \sim N (0, 1) \\ & = . 3 6 8 \end{array}
$$

Since this value is greater than .05, the foregoing data do not enable us to reject, at the .05 percent level of significance, the hypothesis that the mean nicotine content exceeds 1.6 mg. In other words, the evidence, although supporting the cigarette producer’s claim, is not strong enough to prove that claim. ■ 

## REMARKS

(a) There is a direct analogy between confidence interval estimation and hypothesis testing For instance, for a normal population having mean $\mu$ and known variance $\sigma ^ { 2 }$ , we have shown in Section 7.3 that $\mathrm { ~ a ~ } 1 0 0 ( 1 - \alpha )$ percent confidence interval for $\mu$ is given by 

$$
\mu \in \left(\overline {{x}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \overline {{x}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right)
$$

where $\overline { { x } }$ is the observed sample mean. More formally, the preceding confidence interval statement is equivalent to 

$$
P \left\{\mu \in \left(\overline {{X}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \overline {{X}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right) \right\} = 1 - \alpha
$$

Hence, if $\mu = \mu _ { 0 }$ , then the probability that $\mu _ { 0 }$ will fall in the interval 

$$
\left(\overline {{X}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \overline {{X}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right)
$$

is $1 - \alpha ,$ , implying that a significance level $\alpha$ test of $H _ { 0 } : \mu = \mu _ { 0 }$ versus $H _ { 1 } : \mu \neq \mu _ { 0 }$ is to reject $H _ { 0 }$ when 

$$
\mu_ {0} \notin \left(\overline {{X}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \overline {{X}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right)
$$

Similarly, since a $1 0 0 ( 1 - \alpha )$ percent one-sided confidence interval for $\mu$ is given by 

$$
\mu \in \left(\overline {{X}} - z _ {\alpha} \frac {\sigma}{\sqrt {n}}, \infty\right)
$$

it follows that an α-level significance test of $H _ { 0 } : \mu \le \mu _ { 0 }$ versus $H _ { 1 } : \mu > \mu _ { 0 }$ is to reject $H _ { 0 }$ when $\mu _ { 0 } \not \in ( { \overline { { X } } } - z _ { \alpha } \sigma / { \sqrt { n } } , \infty )$ — that is, when $\mu _ { 0 } < \overline { { X } } - z _ { \alpha } \sigma / \sqrt { n } .$ 


TABLE 8.1 $X _ { 1 } , \ldots , X _ { n }$ Is a Sample from $a \mathcal { N } ( \mu , \sigma ^ { 2 } )$ Population $\sigma ^ { 2 }$ Is Known $\overline { { X } } = \sum _ { i = 1 } ^ { n } X _ { i } / n$


<table><tr><td><eq>H_0</eq></td><td><eq>H_1</eq></td><td>Test Statistic TS</td><td>Significance Level α Test</td><td>p-Value if <eq>TS = t</eq></td></tr><tr><td><eq>\mu = \mu_0</eq></td><td><eq>\mu \neq \mu_0</eq></td><td><eq>\sqrt{n(\overline{X} - \mu_0)/\sigma}</eq></td><td>Reject if <eq>|TS| &gt; z_{\alpha/2}</eq></td><td><eq>2P\{Z \geq |t|\}</eq></td></tr><tr><td><eq>\mu \leq \mu_0</eq></td><td><eq>\mu &gt; \mu_0</eq></td><td><eq>\sqrt{n(\overline{X} - \mu_0)/\sigma}</eq></td><td>Reject if <eq>TS &gt; z_{\alpha}</eq></td><td><eq>P\{Z \geq t\}</eq></td></tr><tr><td><eq>\mu \geq \mu_0</eq></td><td><eq>\mu &lt; \mu_0</eq></td><td><eq>\sqrt{n(\overline{X} - \mu_0)/\sigma}</eq></td><td>Reject if <eq>TS &lt; -z_{\alpha}</eq></td><td><eq>P\{Z \leq t\}</eq></td></tr></table>


Z is a standard normal random variable. 


(b) A Remark on Robustness A test that performs well even when the underlying assumptions on which it is based are violated is said to be robust. For instance, the tests of Sections 8.3.1 and 8.3.1.1 were derived under the assumption that the underlying population distribution is normal with known variance $\sigma ^ { 2 }$ . However, in deriving these tests, this assumption was used only to conclude that $\overline { { X } }$ also has a normal distribution. But, by the central limit theorem, it follows that for a reasonably large sample size, $\overline { { X } }$ will approximately have a normal distribution no matter what the underlying distribution. Thu we can conclude that these tests will be relatively robust for any population distribution with variance $\sigma ^ { 2 }$ 

Table 8.1 summarizes the tests of this subsection. 

## 8.3.2 Case of Unknown Variance: The <sub>t</sub>-Test

Up to now we have supposed that the only unknown parameter of the normal population distribution is its mean. However, the more common situation is one where the mean $\mu$ and variance $\sigma ^ { 2 }$ are both unknown. Let us suppose this to be the case and again consider a test of the hypothesis that the mean is equal to some specified value $\mu _ { 0 }$ . That is, consider a test of 

$$
H _ {0}: \mu = \mu_ {0}
$$

versus the alternative 

$$
H _ {1}: \mu \neq \mu_ {0}
$$

It should be noted that the null hypothesis is not a simple hypothesis since it does not specify the value of $\sigma ^ { 2 }$ . 

As before, it seems reasonable to reject $H _ { 0 }$ when the sample mean $\overline { { X } }$ is far from $\mu _ { 0 }$ However, how far away it need be to justify rejection will depend on the variance $\sigma ^ { 2 }$ Recall that when the value of $\cdot \sigma ^ { 2 }$ was known, the test called for rejecting $H _ { 0 }$ when $| \overline { { X } } - \mu _ { 0 } |$ exceeded $z _ { \alpha / 2 } \sigma / \sqrt { n }$ or, equivalently, when 

$$
\left| \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} \right| > z _ {\alpha / 2}
$$

Now when $\sigma ^ { 2 }$ is no longer known, it seems reasonable to estimate it by 

$$
S ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{n - 1}
$$

and then to reject $H _ { 0 }$ when 

$$
\left| \frac {\overline {{X}} - \mu_ {0}}{S / \sqrt {n}} \right|
$$

is large. 

To determine how large a value of the statistic 

$$
\left| \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \right|
$$

to require for rejection, in order that the resulting test have significance level $\alpha ,$ , we must determine the probability distribution of this statistic when $H _ { 0 }$ is true. However, as shown in Section 6.5, the statistic $T _ { ; }$ , defined by 

$$
T = \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S}
$$

has, when $\mu = \mu _ { 0 }$ , a t -distribution with $n - 1$ degrees of freedom. Hence, 

$$
P _ {\mu_ {0}} \left\{- t _ {\alpha / 2, n - 1} \leq \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \leq t _ {\alpha / 2, n - 1} \right\} = 1 - \alpha\tag{8.3.11}
$$

where $t _ { \alpha / 2 , n - 1 }$ is the 100 α/2 upper percentile value of the t-distribution with $n - 1$ degrees of freedom. (That is, $P \{ T _ { n - 1 } \ge t _ { \alpha / 2 , n - 1 } \} = P \{ T _ { n - 1 } \le - t _ { \alpha / 2 , n - 1 } \} = \alpha / 2$ when $T _ { n - 1 }$ has a t -distribution with $n - 1$ degrees of freedom.) From Equation 8.3.11 we see that the appropriate significance level α test of 

$$
H _ {0}: \mu = \mu_ {0} \qquad \text { versus } \qquad H _ {1}: \mu \neq \mu_ {0}
$$

is, when $\sigma ^ { 2 }$ is unknown, to 

$$
\text {   accept   } \quad H _ {0} \quad \text {   if   } \quad \left| \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \right| \leq t _ {\alpha / 2, n - 1}\tag{8.3.12}
$$

$$
\text { reject } \quad H _ {0} \quad \text { if } \quad \left| \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \right| > t _ {\alpha / 2, n - 1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/1ba9ef066ee36b8808f9ad74dbd0978b8df20a5316dde20f0cd7bd2306468d3e.jpg)



FIGURE 8.3 The two-sided t -test.


The test defined by Equation 8.3.12 is called a two-sided t-test. It is pictorially illustrated in Figure 8.3. 

If we let t denote the observed value of the test statistic $T = \sqrt { n } ( \overline { { X } } - \mu _ { 0 } ) / S$ , then the p-value of the test is the probability that $\lvert T \rvert$ would exceed $| t |$ when $H _ { 0 }$ is true. That is, the p-value is the probability that the absolute value of a t-random variable with $n - 1$ degrees of freedom would exceed |t|. The test then calls for rejection at all significance levels higher than the p-value and acceptance at all lower significance levels. 

Program 8.3.2 computes the value of the test statistic and the corresponding p-value. It can be applied both for one- and two-sided tests. (The one-sided material will be presented shortly.) 

EXAMPLE 8.3g Among a clinic’s patients having blood cholesterol levels ranging in the medium to high range (at least 220 milliliters per deciliter of serum), volunteers were recruited to test a new drug designed to reduce blood cholesterol. A group of 50 volunteers was given the drug for 1 month and the changes in their blood cholesterol levels were noted. If the average change was a reduction of 14.8 with a sample standard deviation of 6.4, what conclusions can be drawn? 

SOLUTION Let us start by testing the hypothesis that the change could be due solely to chance — that is, that the 50 changes constitute a normal sample with mean 0. Because the value of the t -statistic used to test the hypothesis that a normal mean is equal to 0 is 

$$
T = \sqrt {n} \overline {{X}} / S = \sqrt {5 0} 1 4. 8 / 6. 4 = 1 6. 3 5 2
$$

it is clear that we should reject the hypothesis that the changes were solely due to chance. Unfortunately, however, we are not justified at this point in concluding that the changes were due to the specific drug used and not to some other possibility. For instance, it is well known that any medication received by a patient (whether or not this medication is directly relevant to the patient’s suffering) often leads to an improvement in the patient’s condition — the so-called placebo effect. Also, another possibility that may need to be taken into account would be the weather conditions during the month of testing, for it is certainly conceivable that this affects blood cholesterol level. Indeed, it must be concluded that the foregoing was a very poorly designed experiment, for in order to test whether a specific treatment has an effect on a disease that may be affected by many things, we should try to design the experiment so as to neutralize all other possible causes. The accepted approach for accomplishing this is to divide the volunteers at random into two groups — one group to receive the drug and the other to receive a placebo (that is, a tablet that looks and tastes like the actual drug but has no physiological effect). The volunteers should not be told whether they are in the actual or control group, and indeed it is best if even the clinicians do not have this information (the so-called double-blind test) so as not to allow their own biases to play a role. Since the two groups are chosen at random from among the volunteers, we can now hope that on average all factors affecting the two groups will be the same except that one received the actual drug and the other a placebo. Hence, any difference in performance between the groups can be attributed to the drug. ■ 

EXAMPLE 8.3h A public health official claims that the mean home water use is 350 gallons a day. To verify this claim, a study of 20 randomly selected homes was instigated with the result that the average daily water uses of these 20 homes were as follows: 

<table><tr><td>340</td><td>344</td><td>362</td><td>375</td></tr><tr><td>356</td><td>386</td><td>354</td><td>364</td></tr><tr><td>332</td><td>402</td><td>340</td><td>355</td></tr><tr><td>362</td><td>322</td><td>372</td><td>324</td></tr><tr><td>318</td><td>360</td><td>338</td><td>370</td></tr></table>


Do the data contradict the official’s claim? 


SOLUTION To determine if the data contradict the official’s claim, we need to test 

$$
H _ {0}: \mu = 3 5 0 \quad \text { versus } \quad H _ {1}: \mu \neq 3 5 0
$$

This can be accomplished by running Program 8.3.2 or, if it is incovenient to utilize, by noting first that the sample mean and sample standard deviation of the preceding data set are 

$$
\overline {{X}} = 3 5 3. 8, \qquad S = 2 1. 8 4 7 8
$$

Thus, the value of the test statistic is 

$$
T = \frac {\sqrt {2 0} (3 . 8)}{2 1 . 8 4 7 8} = . 7 7 7 8
$$

Because this is less than $t _ { . 0 5 , 1 9 } = 1 . 7 3 0$ , the null hypothesis is accepted at the 10 percent level of significance. Indeed, the p-value of the test data is 

$$
p \text {-value} = P \{| T _ {1 9} | >. 7 7 7 8 \} = 2 P \{T _ {1 9} >. 7 7 7 8 \} = . 4 4 6 2
$$

indicating that the null hypothesis would be accepted at any reasonable significance level, and thus that the data are not inconsistent with the claim of the health official. ■ 

We can use a one-sided t-test to test the hypothesis 

$$
H _ {0}: \mu = \mu_ {0} \qquad (\mathrm{or} H _ {0}: \mu \leq \mu_ {0})
$$

against the one-sided alternative 

$$
H _ {1}: \mu > \mu_ {0}
$$

The significance level α test is to 

$$
\begin{array}{l l} \text {   accept   } & H _ {0} \quad \text {   if   } \quad \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \leq t _ {\alpha , n - 1} \\ \text {   reject   } & H _ {0} \quad \text {   if   } \quad \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} > t _ {\alpha , n - 1} \end{array}\tag{8.3.13}
$$

$\mathrm { I f ~ } \sqrt { n } ( \overline { { X } } - \mu _ { 0 } ) / S = \nu ,$ then the p-value of the test is the probability that a t -random variable with n − 1 degrees of freedom would be at least as large as v. 

The significance level α test of 

$$
H _ {0}: \mu = \mu_ {0} \qquad (\mathrm{or} H _ {0}: \mu \geq \mu_ {0})
$$

versus the alternative 

$$
H _ {1}: \mu <   \mu_ {0}
$$

is to 

$$
\begin{array}{l l} \text {   accept   } & H _ {0} \quad \text {   if   } \quad \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \geq - t _ {\alpha , n - 1} \\ \text {   reject   } & H _ {0} \quad \text {   if   } \quad \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} <   - t _ {\alpha , n - 1} \end{array}
$$

The p-value of this test is the probability that a t-random variable with $n - 1$ degrees of freedom would be less than or equal to the observed value of $\sqrt { n } ( \overline { { X } } - \mu _ { 0 } ) / S$ 

EXAMPLE 8.3i The manufacturer of a new fiberglass tire claims that its average life will be at least 40,000 miles. To verify this claim a sample of 12 tires is tested, with their lifetimes (in 1,000s of miles) being as follows: 

$$
\begin{array}{c c c c c c c c c c c c c} \text {Tire} & \underline {{1}} & \underline {{2}} & \underline {{3}} & \underline {{4}} & \underline {{5}} & \underline {{6}} & \underline {{7}} & \underline {{8}} & \underline {{9}} & \underline {{1 0}} & \underline {{1 1}} & \underline {{1 2}} \\ \text {Life} & 3 6. 1 & 4 0. 2 & 3 3. 8 & 3 8. 5 & 4 2 & 3 5. 8 & 3 7 & 4 1 & 3 6. 8 & 3 7. 2 & 3 3 & 3 6 \end{array}
$$

Test the manufacturer’s claim at the 5 percent level of significance. 

SOLUTION To determine whether the foregoing data are consistent with the hypothesis that the mean life is at least 40,000 miles, we will test 

$$
H _ {0}: \mu \geq 4 0, 0 0 0 \quad \text { versus } \quad H _ {1}: \mu <   4 0, 0 0 0
$$

A computation gives that 

$$
\overline {{{X}}} = 3 7. 2 8 3 3, \qquad S = 2. 7 3 1 9
$$

and so the value of the test statistic is 

$$
T = \frac {\sqrt {1 2} (3 7 . 2 8 3 3 - 4 0)}{2 . 7 3 1 9} = - 3. 4 4 4 8
$$

Since this is less than $- t _ { \cdot 0 5 , 1 1 } = - 1 . 7 9 6$ , the null hypothesis is rejected at the 5 percent level of significance. Indeed, the p-value of the test data is 

$$
p \text {-value} = P \{T _ {1 1} <   - 3. 4 4 4 8 \} = P \{T _ {1 1} > 3. 4 4 4 8 \} = . 0 0 2 8
$$

indicating that the manufacturer’s claim would be rejected at any significance level greater than .003. ■ 

The preceding could also have been obtained by using Program 8.3.2, as illustrated in Figure 8.4. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/a674ba67cd793d5095dd9c7e9123e4b02ea21c4a5042da08cbba9c47dbc41950.jpg)



FIGURE 8.4


EXAMPLE 8.3j In a single-server queueing system in which customers arrive according to a Poisson process, the long-run average queueing delay per customer depends on the service distribution through its mean and variance. Indeed, if $\dot { \mu }$ is the mean service time, and $\sigma ^ { 2 }$ is the variance of a service time, then the average amount of time that a customer spends waiting in queue is given by 

$$
\frac {\lambda (\mu^ {2} + \sigma^ {2})}{2 (1 - \lambda \mu)}
$$

provided that $\lambda \mu ~ < ~ 1$ , where λ is the arrival rate. (The average delay is infinite if $\lambda \mu \geq 1 . )$ As can be seen by this formula, the average delay is quite large when $\mu$ is only slightly smaller than 1/λ, where, since λ is the arrival rate, 1/λ is the average time between arrivals. 

Suppose that the owner of a service station will hire a second server if it can be shown that the average service time exceeds 8 minutes. The following data give the service times (in minutes) of 28 customers of this queueing system. Do they indicate that the mean service time is greater than 8 minutes? 

8.6, 9.4, 5.0, 4.4, 3.7, 11.4, 10.0, 7.6, 14.4, 12.2, 11.0, 14.4, 9.3, 10.5, 

10.3, 7.7, 8.3, 6.4, 9.2, 5.7, 7.9, 9.4, 9.0, 13.3, 11.6, 10.0, 9.5, 6.6 

SOLUTION Let us use the preceding data to test the null hypothesis that the mean service time is less than or equal to 8 minutes. A small p-value will then be strong evidence that the mean service time is greater than 8 minutes. Running Program 8.3.2 on these data shows that the value of the test statistic is 2.257, with a resulting p-value of .016. Such a small p-value is certainly strong evidence that the mean service time exceeds 8 minutes. ■ 

Table 8.2 summarizes the tests of this subsection. 


TABLE 8.2 $X _ { 1 } , \ldots , X _ { n }$ Is a Sample from a $\mathcal { N } ( \mu , \sigma ^ { 2 } )$ Population $\sigma ^ { 2 }$ Is Unknown $\overline { { { X } } } = \sum _ { i = 1 } ^ { n } X _ { i } / n$ $S ^ { 2 } = \sum _ { i = 1 } ^ { n } ( X _ { i } - { \overline { { X } } } ) ^ { 2 } / ( n - 1 )$


<table><tr><td><eq>H_0</eq></td><td><eq>H_1</eq></td><td>TestStatistic TS</td><td>SignificanceLevel α Test</td><td>p-Value ifTS = t</td></tr><tr><td>μ = μ0</td><td>μ ≠ μ0</td><td><eq>\sqrt{n}(\overline{X} - \mu_0)/S</eq></td><td>Reject if |TS| &gt; <eq>t_{\alpha/2,n-1}</eq></td><td><eq>2P\{T_{n-1} \geq |t|\}</eq></td></tr><tr><td>μ ≤ μ0</td><td>μ &gt; μ0</td><td><eq>\sqrt{n}(\overline{X} - \mu_0)/S</eq></td><td>Reject if TS &gt; <eq>t_{\alpha,n-1}</eq></td><td><eq>P\{T_{n-1} \geq t\}</eq></td></tr><tr><td>μ ≥ μ0</td><td>μ &lt; μ0</td><td><eq>\sqrt{n}(\overline{X} - \mu_0)/S</eq></td><td>Reject if TS &lt; <eq>-t_{\alpha,n-1}</eq></td><td><eq>P\{T_{n-1} \leq t\}</eq></td></tr></table>


$T _ { n - 1 }$ is a t-random variable with n − 1 degrees of freedom: $P \{ T _ { n - 1 } > t _ { \alpha , n - 1 } \} = \alpha .$ 


## 8.4 TESTING THE EQUALITY OF MEANS OF TWO NORMAL POPULATIONS

A common situation faced by a practicing engineer is one in which she must decide whether two different approaches lead to the same solution. Often such a situation can be modeled as a test of the hypothesis that two normal populations have the same mean value. 

## 8.4.1 Case of Known Variances

Suppose that $X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { m }$ are independent samples from normal populations having unknown means $\mu _ { x }$ and $\mu _ { y }$ but known variances $\sigma _ { x } ^ { 2 }$ and $\sigma _ { y } ^ { 2 }$ . Let us consider the problem of testing the hypothesis 

$$
H _ {0}: \mu_ {x} = \mu_ {y}
$$

versus the alternative 

$$
H _ {1}: \mu_ {x} \neq \mu_ {y}
$$

Since $\overline { { X } }$ is an estimate of $\mu _ { x }$ and $\overline { { Y } }$ of $\mu _ { y }$ , it follows that ${ \overline { { X } } } - { \overline { { Y } } }$ can be used to estimate $\mu _ { x } - \mu _ { y }$ . Hence, because the null hypothesis can be written as $H _ { 0 } : \mu _ { x } - \mu _ { y } = 0$ , it seems reasonable to reject it when ${ \overline { { X } } } - { \overline { { Y } } }$ is far from zero. That is, the form of the test should be to 

$$
\begin{array}{l l l l} \text { reject } & H _ {0} & \text { if } & | \overline {{X}} - \overline {{Y}} | > c \\ \text { accept } & H _ {0} & \text { if } & | \overline {{X}} - \overline {{Y}} | \leq c \end{array}\tag{8.4.1}
$$

for some suitably chosen value c. 

To determine that value of $c$ that would result in the test in Equations 8.4.1 having a significance level α, we need determine the distribution of ${ \overline { { X } } } - { \overline { { Y } } }$ when $H _ { 0 }$ is true. However, as was shown in Section 7.3.2, 

$$
\overline {{X}} - \overline {{Y}} \sim \mathcal {N} \left(\mu_ {x} - \mu_ {y}, \frac {\sigma_ {x} ^ {2}}{n} + \frac {\sigma_ {y} ^ {2}}{m}\right)
$$

which implies that 

$$
\frac {\overline {{X}} - \overline {{Y}} - (\mu_ {x} - \mu_ {y})}{\sqrt {\frac {\sigma_ {x} ^ {2}}{n} + \frac {\sigma_ {y} ^ {2}}{m}}} \sim \mathcal {N} (0, 1)\tag{8.4.2}
$$

Hence, when $H _ { 0 }$ is true (and so $\mu _ { x } - \mu _ { y } = 0 )$ , it follows that 

$$
(\overline {{X}} - \overline {{Y}}) \left/ \sqrt {\frac {\sigma_ {x} ^ {2}}{n} + \frac {\sigma_ {y} ^ {2}}{m}} \left. \right.
$$

has a standard normal distribution; and thu 

$$
P _ {H _ {0}} \left\{- z _ {\alpha / 2} \leq \frac {\overline {{X}} - \overline {{Y}}}{\sqrt {\frac {\sigma_ {x} ^ {2}}{n} + \frac {\sigma_ {y} ^ {2}}{m}}} \leq z _ {\alpha / 2} \right\} = 1 - \alpha\tag{8.4.3}
$$

From Equation 8.4.3, we obtain that the significance level α test of $H _ { 0 } : \mu _ { x } = \mu _ { y }$ versus $H _ { 1 } : \mu _ { x } \neq \mu _ { y }$ is 

$$
\begin{array}{l l l l} \text {accept} & H _ {0} & \text {if} & \frac {| \overline {{X}} - \overline {{Y}} |}{\sqrt {\sigma_ {x} ^ {2} / n + \sigma_ {y} ^ {2} / m}} \leq z _ {\alpha / 2} \\ \text {reject} & H _ {0} & \text {if} & \frac {| \overline {{X}} - \overline {{Y}} |}{\sqrt {\sigma_ {x} ^ {2} / n + \sigma_ {y} ^ {2} / m}} \geq z _ {\alpha / 2} \end{array}
$$

Program 8.4.1 will compute the value of the test statistic $( \overline { { X } } - \overline { { Y } } ) \big / \sqrt { \sigma _ { x } ^ { 2 } / n + \sigma _ { y } ^ { 2 } / m } .$ 

EXAMPLE 8.4a Two new methods for producing a tire have been proposed. To ascertain which is superior, a tire manufacturer produces a sample of 10 tires using the first method and a sample of 8 using the second. The first set is to be road tested at location A and the second at location B. It is known from past experience that the lifetime of a tire that is road tested at one of these locations is normally distributed with a mean life due to the tire but with a variance due (for the most part) to the location. Specifically, it is known that the lifetimes of tires tested at location A are normal with standard deviation equal to 4,000 kilometers, whereas those tested at location B are normal with $\sigma = 6 { , } 0 0 0$ kilometers. If the manufacturer is interested in testing the hypothesis that there is no appreciable difference in the mean life of tires produced by either method, what conclusion should be drawn at the 5 percent level of significance if the resulting data are as given in Table 8.3? 


TABLE 8.3 Tire Lives in Units of 100 Kilometer


<table><tr><td>Tires Tested at A</td><td>Tires Tested at B</td></tr><tr><td>61.1</td><td>62.2</td></tr><tr><td>58.2</td><td>56.6</td></tr><tr><td>62.3</td><td>66.4</td></tr><tr><td>64</td><td>56.2</td></tr><tr><td>59.7</td><td>57.4</td></tr><tr><td>66.2</td><td>58.4</td></tr><tr><td>57.8</td><td>57.6</td></tr><tr><td>61.4</td><td>65.4</td></tr><tr><td>62.2</td><td></td></tr><tr><td>63.6</td><td></td></tr></table>

SOLUTION A simple computation (or the use of Program 8.4.1) shows that the value of the test statistic is .066. For such a small value of the test statistic (which has a standard normal distribution when $H _ { 0 }$ is true), it is clear that the null hypothesis is accepted. ■ 

It follows from Equation 8.4.1 that a test of the hypothesis $H _ { 0 } : \mu _ { x } = \mu _ { y }$ (or $H _ { 0 }$ : $\mu _ { x } \leq \mu _ { y } )$ against the one-sided alternative $H _ { 1 } : \mu _ { x } > \mu _ { y }$ would be to 

$$
\text {   accept   } \quad H _ {0} \quad \text {   if   } \quad \overline {{X}} - \overline {{Y}} \leq z _ {\alpha} \sqrt {\frac {\sigma_ {x} ^ {2}}{n} + \frac {\sigma_ {y} ^ {2}}{m}}
$$

$$
\text { reject } \quad H _ {0} \quad \text { if } \quad \overline {{X}} - \overline {{Y}} > z _ {\alpha} \sqrt {\frac {\sigma_ {x} ^ {2}}{n} + \frac {\sigma_ {y} ^ {2}}{m}}
$$

## 8.4.2 Case of Unknown Variances

Suppose again that $X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { m }$ are independent samples from normal populations having respective parameters $( \mu _ { x } , \sigma _ { x } ^ { 2 } )$ ) and $( \mu _ { y } , \sigma _ { y } ^ { 2 } )$ , but now suppose that all four parameters are unknown. We will once again consider a test of 

$$
H _ {0}: \mu_ {x} = \mu_ {y} \quad \text { versus } \quad H _ {1}: \mu_ {x} \neq \mu_ {y}
$$

To determine a significance level α test of $H _ { 0 }$ we will need to make the additional assumption that the unknown variances $\sigma _ { x } ^ { 2 }$ and $\sigma _ { y } ^ { 2 }$ are equal. Let $\sigma ^ { 2 }$ denote their value — that is, 

$$
\sigma^ {2} = \sigma_ {x} ^ {2} = \sigma_ {y} ^ {2}
$$

As before, we would like to reject $H _ { 0 }$ when ${ \overline { { X } } } - { \overline { { Y } } } { \mathrm { ~ i s ~ } } ^ { \infty } { \mathrm { f a r } } ^ { \infty }$ from zero. To determine how far from zero it need be, let 

$$
S _ {x} ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{n - 1}
$$

$$
S _ {y} ^ {2} = \frac {\sum_ {i = 1} ^ {m} (Y _ {i} - \overline {{Y}}) ^ {2}}{m - 1}
$$

denote the sample variances of the two samples. Then, as was shown in Section 7.3.2, 

$$
\frac {\overline {{X}} - \overline {{Y}} - (\mu_ {x} - \mu_ {y})}{\sqrt {S _ {p} ^ {2} (1 / n + 1 / m)}} \sim t _ {n + m - 2}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/52c69262be4c446eaa7fa7378504119372d95423a2f9c6038119f2a15b9c54f3.jpg)



FIGURE 8.5 Density of a t -random variable with k degrees of freedom.


where $S _ { \ / p } ^ { 2 }$ , the pooled estimator of the common variance $\sigma ^ { 2 } { } _ { ; }$ , is given by 

$$
S _ {p} ^ {2} = \frac {(n - 1) S _ {x} ^ {2} + (m - 1) S _ {y} ^ {2}}{n + m - 2}
$$

Hence, when $H _ { 0 }$ is true, and so $\mu _ { x } - \mu _ { y } = 0$ , the statistic 

$$
T \equiv \frac {\overline {{X}} - \overline {{Y}}}{\sqrt {S _ {p} ^ {2} (1 / n + 1 / m)}}
$$

has a t -distribution with $n + m - 2$ degrees of freedom. From this, it follows that we can test the hypothesis that $\mu _ { x } = \mu _ { y }$ as follows: 

$$
\begin{array}{l l l l} \text {accept} & H _ {0} & \text {if} & | T | \leq t _ {\alpha / 2, n + m - 2} \\ \text {reject} & H _ {0} & \text {if} & | T | > t _ {\alpha / 2, n + m - 2} \end{array}
$$

where $t _ { \alpha / 2 , n + m - 2 }$ is the 100 $\alpha / 2$ percentile point of a t-random variable with $n + m - 2$ degrees of freedom (see Figure 8.5). 

Alternatively, the test can be run by determining the p-value. If $T$ is observed to equal v, then the resulting p-value of the test of $H _ { 0 }$ against $H _ { 1 }$ is given by 

$$
\begin{array}{c} p \text {-value} = P \{| T _ {n + m - 2} | \geq | v | \} \\ = 2 P \{T _ {n + m - 2} \geq | v | \} \end{array}
$$

where $T _ { n + m - 2 }$ is a t-random variable having $n + m - 2$ degrees of freedom. 

If we are interested in testing the one-sided hypothesis 

$$
H _ {0}: \mu_ {x} \leq \mu_ {y} \quad \text { versus } \quad H _ {1}: \mu_ {x} > \mu_ {y}
$$

then $H _ { 0 }$ will be rejected at large values of $T .$ . Thus the significance level α test is to 

$$
\mathrm{reject} H _ {0} \mathrm{if} T \geq t _ {\alpha , n + m - 2}
$$

not reject H otherwise 

If the value of the test statistic T is v, then the p-value is given by 

$$
p \text {-value} = P \{T _ {n + m - 2} \geq \nu \}
$$

Program 8.4.2 computes both the value of the test statistic and the corresponding p-value. 


EXAMPLE 8.4b Twenty-two volunteers at a cold research institute caught a cold after having been exposed to various cold viruses. A random selection of 10 of these volunteers was given tablets containing 1 gram of vitamin C. These tablets were taken four times a day. The control group consisting of the other 12 volunteers was given placebo tablets that looked and tasted exactly the same as the vitamin C tablets. This was continued for each volunteer until a doctor, who did not know if the volunteer was receiving the vitamin C or the placebo tablets, decided that the volunteer was no longer suffering from the cold. The length of time the cold lasted was then recorded.



At the end of this experiment, the following data resulted.


<table><tr><td>Treated with Vitamin C</td><td>Treated with Placebo</td></tr><tr><td>5.5</td><td>6.5</td></tr><tr><td>6.0</td><td>6.0</td></tr><tr><td>7.0</td><td>8.5</td></tr><tr><td>6.0</td><td>7.0</td></tr><tr><td>7.5</td><td>6.5</td></tr><tr><td>6.0</td><td>8.0</td></tr><tr><td>7.5</td><td>7.5</td></tr><tr><td>5.5</td><td>6.5</td></tr><tr><td>7.0</td><td>7.5</td></tr><tr><td>6.5</td><td>6.0</td></tr><tr><td></td><td>8.5</td></tr><tr><td></td><td>7.0</td></tr></table>

Do the data listed prove that taking 4 grams daily of vitamin C reduces the mean length of time a cold lasts? At what level of significance? 

SOLUTION To prove the above hypothesis, we would need to reject the null hypothesis in a test of 

$$
H _ {0}: \mu_ {p} \leq \mu_ {c} \quad \text { versus } \quad H _ {1}: \mu_ {p} > \mu_ {c}
$$

where $\mu _ { c }$ is the mean time a cold lasts when the vitamin C tablets are taken and $\mu _ { \ / p }$ is the mean time when the placebo is taken. Assuming that the variance of the length of the cold is the same for the vitamin C patients and the placebo patients, we test the above by running Program 8.4.2. This yields the information shown in Figure 8.6. Thus $H _ { 0 }$ would be rejected at the 5 percent level of significance. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/5806cf4e510b4afe232f0e028f131fc391d58986b07976774d101baaeedc4037.jpg)



FIGURE 8.6


Of course, if it were not convenient to run Program 8.4.2 then we could have performed the test by first computing the values of the statistics X , $\overline { { Y } } , S _ { x } ^ { 2 } , S _ { y } ^ { 2 }$ , and $S _ { \ / P } ^ { 2 }$ . where the X sample corresponds to those receiving vitamin C and the $Y$ sample to those receiving a placebo. These computations would give the value 

$$
\begin{array}{l l} \overline {{X}} = 6. 4 5 0, & \overline {{Y}} = 7. 1 2 5 \\ S _ {x} ^ {2} = . 5 8 1, & S _ {y} ^ {2} = . 7 7 8 \end{array}
$$

Therefore, 

$$
S _ {p} ^ {2} = \frac {9}{2 0} S _ {x} ^ {2} + \frac {1 1}{2 0} S _ {y} ^ {2} = . 6 8 9
$$

and the value of the test statistic is 

$$
T S = \frac {- . 6 7 5}{\sqrt {. 6 8 9 (1 / 1 0 + 1 / 1 2)}} = - 1. 9 0
$$

Since $t _ { 0 . 5 , 2 0 } = 1 . 7 2 5$ , the null hypothesis is rejected at the 5 percent level of significance That is, at the 5 percent level of significance the evidence is significant in establishing that vitamin C reduces the mean time that a cold persists. ■ 

EXAMPLE 8.4c Reconsider Example 8.4a, but now suppose that the population variances are unknown but equal. 

SOLUTION Using Program 8.4.2 yields that the value of the test statistic is 1.028, and the resulting p-value is 

$$
p \text {-value} = P \{T _ {1 6} > 1. 0 2 8 \} = . 3 1 9 2
$$

Thus, the null hypothesis is accepted at any significance level less than .3192 ■ 

## 8.4.3 Case of Unknown and Unequal Variances

Let us now suppose that the population variances $\sigma _ { x } ^ { 2 }$ and $\sigma _ { \gamma } ^ { 2 }$ are not only unknown but also cannot be considered to be equal. In this situation, since $S _ { x } ^ { 2 }$ is the natural estimator of $\sigma _ { x } ^ { 2 }$ and $S _ { y } ^ { 2 }$ of $\sigma _ { y } ^ { 2 }$ , it would seem reasonable to base our test of 

$$
H _ {0}: \mu_ {x} = \mu_ {y} \quad \text { versus } \quad H _ {1}: \mu_ {x} \neq \mu_ {y}
$$

on the test statistic 

$$
\frac {\overline {{X}} - \overline {{Y}}}{\sqrt {\frac {S _ {x} ^ {2}}{n} + \frac {S _ {y} ^ {2}}{m}}}\tag{8.4.4}
$$

However, the foregoing has a complicated distribution, which, even when $H _ { 0 }$ is true, depends on the unknown parameters, and thus cannot be generally employed. The one situation in which we can utilize the statistic of Equation 8.4.4 is when n and m are both large. In such a case, it can be shown that when $H _ { 0 }$ is true Equation 8.4.4 will have approximately a standard normal distribution. Hence, when n and m are large an approximate level α test of $H _ { 0 } : \mu _ { x } = \mu _ { y }$ versus $H _ { 1 } : \mu _ { x } \neq \mu _ { y }$ is to 

$$
\text { accept } \quad H _ {0} \quad \text { if } \quad - z _ {\alpha / 2} \leq \frac {\overline {{X}} - \overline {{Y}}}{\sqrt {\frac {S _ {x} ^ {2}}{n} + \frac {S _ {y} ^ {2}}{m}}} \leq z _ {\alpha / 2}
$$

reject otherwise 

The problem of determining an exact level α test of the hypothesis that the means of two normal populations, having unknown and not necessarily equal variances, are equal is known as the Behrens-Fisher problem. There is no completely satisfactory solution known. 

Table 8.4 presents the two-sided tests of this section. 


TABLE 8.4 $X _ { 1 } , \ldots , X _ { n }$ Is a Sample from a $\mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } )$ Population; $Y _ { 1 } , \dots , Y _ { m }$ Is a Sample from $\mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$ Population



The Two Population Samples Are Independent To Test



$H _ { 0 } : \mu _ { 1 } = \mu _ { 2 }$ versus $H _ { 0 } : \mu _ { 1 } \neq \mu _ { 2 }$


<table><tr><td>Assumption</td><td>Test Statistic TS</td><td>Significance Level <eq>\alpha</eq> Test</td><td><eq>p</eq>-Value if <eq>TS = t</eq></td></tr><tr><td><eq>\sigma_1, \sigma_2</eq> known</td><td><eq>\frac{\overline{X}-\overline{Y}}{\sqrt{\sigma_1^2/n+\sigma_2^2/m}}</eq></td><td>Reject if <eq>|TS| &gt; z_{\alpha/2}</eq></td><td><eq>2P\{Z \geq |t|\}</eq></td></tr><tr><td><eq>\sigma_1 = \sigma_2</eq></td><td><eq>\frac{\overline{X}-\overline{Y}}{\sqrt{\frac{(n-1)S_1^2+(m-1)S_2^2}{n+m-2}\sqrt{1/n+1/m}}}</eq></td><td>Reject if <eq>|TS| &gt; t_{\alpha/2,n+m-2}</eq></td><td><eq>2P\{T_{n+m-2} \geq |t|\}</eq></td></tr><tr><td><eq>n, m</eq> large</td><td><eq>\frac{\overline{X}-\overline{Y}}{\sqrt{S_1^2/n+S_2^2/m}}</eq></td><td>Reject if <eq>|TS| &gt; z_{\alpha/2}</eq></td><td><eq>2P\{Z \geq |t|\}</eq></td></tr></table>

## 8.4.4 The Paired <sub>t</sub>-Test

Suppose we are interested in determining whether the installation of a certain antipollution device will affect a car’s mileage. To test this, a collection of n cars that do not have this device are gathered. Each car’s mileage per gallon is then determined both before and after the device is installed. How can we test the hypothesis that the antipollution control has no effect on gas consumption? 

The data can be described by the n pairs $( X _ { i } , Y _ { i } ) , i = 1 , . . . , n $ , where $X _ { i }$ is the gas consumption of the ith car before installation of the pollution control device, and $Y _ { i }$ of the same car after installation. It is important to note that, since each of the n cars will be inherently different, we cannot treat $X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { n }$ as being independen samples. For example, if we know that $X _ { 1 }$ is large (say, 40 miles per gallon), we would certainly expect that $Y _ { 1 }$ would also probably be large. Thus, we cannot employ the earlier methods presented in this section. 

One way in which we can test the hypothesis that the antipollution device does not affect gas mileage is to let the data consist of each car’s difference in gas mileage. That is, let $W _ { i } = X _ { i } - Y _ { i } , i = 1 , . . . , n .$ . Now, if there is no effect from the device, it should follow that the $W _ { i }$ would have mean 0. Hence, we can test the hypothesis of no effect by testing 

$$
H _ {0}: \mu_ {w} = 0 \qquad \text { versus } \qquad H _ {1}: \mu_ {w} \neq 0
$$

where $W _ { 1 } , \ldots , W _ { n }$ are assumed to be a sample from a normal population having unknown mean $\mu _ { w }$ and unknown variance $\sigma _ { w } ^ { 2 }$ . But the t-test described in Section 8.3.2 shows that 

this can be tested by 

$$
\begin{array}{l l} \text {   accepting   } & H _ {0} \quad \text {   if   } - t _ {\alpha / 2, n - 1} <   \sqrt {n} \frac {\overline {{W}}}{S _ {w}} <   t _ {\alpha / 2, n - 1} \\ \text {   rejecting   } & H _ {0} \quad \text {   otherwise   } \end{array}
$$


EXAMPLE 8.4d An industrial safety program was recently instituted in the computer chip industry. The average weekly loss (averaged over 1 month) in man-hours due to accidents in 10 similar plants both before and after the program are as follows:


<table><tr><td>Plant</td><td>Before</td><td>After</td><td>A-B</td></tr><tr><td>1</td><td>30.5</td><td>23</td><td>-7.5</td></tr><tr><td>2</td><td>18.5</td><td>21</td><td>2.5</td></tr><tr><td>3</td><td>24.5</td><td>22</td><td>-2.5</td></tr><tr><td>4</td><td>32</td><td>28.5</td><td>-3.5</td></tr><tr><td>5</td><td>16</td><td>14.5</td><td>-1.5</td></tr><tr><td>6</td><td>15</td><td>15.5</td><td>.5</td></tr><tr><td>7</td><td>23.5</td><td>24.5</td><td>1</td></tr><tr><td>8</td><td>25.5</td><td>21</td><td>-4.5</td></tr><tr><td>9</td><td>28</td><td>23.5</td><td>-4.5</td></tr><tr><td>10</td><td>18</td><td>16.5</td><td>-1.5</td></tr></table>

Determine, at the 5 percent level of significance, whether the safety program has been proven to be effective. 

SOLUTION To determine this, we will test 

$$
H _ {0}: \mu_ {A} - \mu_ {B} \geq 0 \quad \text { versus } \quad H _ {1}: \mu_ {A} - \mu_ {B} <   0
$$

because this will enable us to see whether the null hypothesis that the safety program has not had a beneficial effect is a reasonable possibility. To test this, we run Program 8.3.2, which gives the value of the test statistic as −2.266, with 

$$
p \text {-value} = P \{T _ {q} \le - 2. 2 6 6 \} = . 0 2 5
$$

Since the p-value is less than .05, the hypothesis that the safety program has not been effective is rejected and so we can conclude that its effectiveness has been established (at least for any significance level greater than .025). ■ 

Note that the paired-sample t-test can be used even though the samples are not independent and the population variances are unequal. 

## 8.5 HYPOTHESIS TESTS CONCERNING THE VARIANCE OF A NORMAL POPULATION

Let $X _ { 1 } , \ldots , X _ { n }$ denote a sample from a normal population having unknown mean $\mu$ and unknown variance $\sigma ^ { 2 }$ , and suppose we desire to test the hypothesis 

$$
H _ {0}: \sigma^ {2} = \sigma_ {0} ^ {2}
$$

versus the alternative 

$$
H _ {1}: \sigma^ {2} \neq \sigma_ {0} ^ {2}
$$

for some specified value $\sigma _ { 0 } ^ { 2 }$ 

To obtain a test, recall (as was shown in Section 6.5) that $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 }$ has a chi-square distribution with $n - 1$ degrees of freedom. Hence, when $H _ { 0 }$ is true 

$$
\frac {(n - 1) S ^ {2}}{\sigma_ {0} ^ {2}} \sim \chi_ {n - 1} ^ {2}
$$

and so 

$$
P _ {H _ {0}} \left\{\chi_ {1 - \alpha / 2, n - 1} ^ {2} \leq \frac {(n - 1) S ^ {2}}{\sigma_ {0} ^ {2}} \leq \chi_ {\alpha / 2, n - 1} ^ {2} \right\} = 1 - \alpha
$$

Therefore, a significance level $\alpha$ test is to 

$$
\begin{array}{l l} \text {   accept   } & H _ {0} \quad \text {   if   } \quad \chi_ {1 - \alpha / 2, n - 1} ^ {2} \leq \frac {(n - 1) S ^ {2}}{\sigma_ {0} ^ {2}} \leq \chi_ {\alpha / 2, n - 1} ^ {2} \\ \text {   reject   } & H _ {0} \quad \text {   otherwise   } \end{array}
$$

The preceding test can be implemented by first computing the value of the test statistic $( n - 1 ) \bar { S } ^ { 2 } / \sigma _ { 0 } ^ { 2 }$ — call it $c .$ . Then compute the probability that a chi-square random variable with $n - 1$ degrees of freedom would be (a) less than and (b) greater than $c .$ If either of these probabilities is less than $\alpha / 2$ , then the hypothesis is rejected. In other words, the p-value of the test data is 

$$
p \mathrm{-value} = 2 \min (P \{\chi_ {n - 1} ^ {2} <   c \}, 1 - P \{\chi_ {n - 1} ^ {2} <   c \})
$$

The quantity $P \{ \chi _ { n - 1 } ^ { 2 } ~ < ~ c \}$ can be obtained from Program 5.8.1.A. The $\phi \mathrm { \cdot }$ -value for a one-sided test is similarly obtained. 

EXAMPLE 8.5a A machine that automatically controls the amount of ribbon on a tape ha recently been installed. This machine will be judged to be effective if the standard deviation $\sigma$ of the amount of ribbon on a tape is less than .15 cm. If a sample of 20 tapes yields a sample variance of $S ^ { 2 } = . 0 2 5 \mathrm { c m } ^ { 2 }$ , are we justified in concluding that the machine is ineffective? 

SOLUTION $\mathbb { W } \mathrm { e }$ will test the hypothesis that the machine is effective, since a rejection of this hypothesis will then enable us to conclude that it is ineffective. Since we are thus interested in testing 

$$
H _ {0}: \sigma^ {2} \leq . 0 2 2 5 \quad \text { versus } \quad H _ {1}: \sigma^ {2} >. 0 2 2 5
$$

it follows that we would want to reject $H _ { 0 }$ when $S ^ { 2 }$ is large. Hence, the $\scriptstyle { p - { \frac { } { } } }$ -value of the preceding test data is the probability that a chi-square random variable with 19 degrees of freedom would exceed the observed value of $1 9 S ^ { 2 } / . 0 2 2 5 = 1 9 \times . 0 2 5 / . 0 2 2 5 = 2 1 . 1 1 1$ That is, 

$$
\begin{array}{r l} p \text {-value} & = P \{\chi_ {1 9} ^ {2} > 2 1. 1 1 1 \} \\ & = 1 -. 6 6 9 3 = . 3 3 0 7 \quad \text {from Program 5.8.1.A} \end{array}
$$

Therefore, we must conclude that the observed value of $S ^ { 2 } = . 0 2 5$ is not large enough to reasonably preclude the possibility that $\sigma ^ { 2 } \leq . 0 2 2 5$ , and so the null hypothesis is accepted. ■ 

## 8.5.1 Testing for the Equality of Variances of Two Normal Populations

Let $X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { m }$ denote independent samples from two normal populations having respective (unknown) parameters $\mu _ { x } , \sigma _ { x } ^ { 2 }$ and $\bar { \mu _ { y } , \sigma _ { y } ^ { 2 } }$ and consider a test of 

$$
H _ {0}: \sigma_ {x} ^ {2} = \sigma_ {y} ^ {2} \qquad \text { versus } \qquad H _ {1}: \sigma_ {x} ^ {2} \neq \sigma_ {y} ^ {2}
$$

If we let 

$$
S _ {x} ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{n - 1}
$$

$$
S _ {y} ^ {2} = \frac {\sum_ {i = 1} ^ {m} (Y _ {i} - \overline {{Y}}) ^ {2}}{m - 1}
$$

denote the sample variances, then as shown in Section $6 . 5 , ( n - 1 ) S _ { x } ^ { 2 } / \sigma _ { x } ^ { 2 }$ and $( m - 1 ) S _ { y } ^ { 2 } / \sigma _ { y } ^ { 2 }$ are independent chi-square random variables with $n - 1$ and $m - 1$ degrees of freedom, respectively. Therefore, $( S _ { x } ^ { 2 } / \sigma _ { x } ^ { 2 } ) / ( S _ { y } ^ { 2 } / \sigma _ { y } ^ { 2 } )$ has an $F .$ -distribution with parameters $n - 1$ and $m - 1$ . Hence, when $H _ { 0 }$ is true 

$$
S _ {x} ^ {2} / S _ {y} ^ {2} \sim F _ {n - 1, m - 1}
$$

and so 

$$
P _ {H _ {0}} \{F _ {1 - \alpha / 2, n - 1, m - 1} \leq S _ {x} ^ {2} / S _ {y} ^ {2} \leq F _ {\alpha / 2, n - 1, m - 1} \} = 1 - \alpha
$$

Thus, a significance level α test of $H _ { 0 }$ against $H _ { 1 }$ is to 

$$
\begin{array}{l l} \text {   accept   } & H _ {0} \quad \text {   if   } \quad F _ {1 - \alpha / 2, n - 1, m - 1} <   S _ {x} ^ {2} / S _ {y} ^ {2} <   F _ {\alpha / 2, n - 1, m - 1} \\ \text {   reject   } & H _ {0} \quad \text {   otherwise   } \end{array}
$$

The preceding test can be effected by first determining the value of the test statistic $S _ { x } ^ { 2 } / S _ { y } ^ { 2 }$ , say its value is $\nu ,$ and then computing $P \{ F _ { n - 1 , m - 1 } \ \leq \ \nu \}$ where $F _ { n - 1 , m - 1 }$ is an F -random variable with parameters $n - 1 , m - 1$ . If this probability is either less than α/2 (which occurs when $\hat { S } _ { x } ^ { 2 }$ is significantly less than $S _ { y } ^ { 2 } )$ or greater than $1 - \alpha / 2$ (which occurs when $S _ { x } ^ { 2 }$ is significantly greater than $S _ { y } ^ { 2 } )$ ), then the hypothesis is rejected. In other words, the $\scriptstyle { p - { \frac { } { } } }$ -value of the test data is 

$$
p \text {-value} = 2 \min (P \{F _ {n - 1, m - 1} <   v \}, 1 - P \{F _ {n - 1, m - 1} <   v \})
$$

The test now calls for rejection whenever the significance level $\alpha$ is at least as large as the p-value. 

EXAMPLE 8.5b There are two different choices of a catalyst to stimulate a certain chemica process. To test whether the variance of the yield is the same no matter which catalyst is used, a sample of 10 batches is produced using the first catalyst, and 12 using the second. If the resulting data is $S _ { 1 } ^ { 2 } = . 1 \bar { 4 }$ and $S _ { 2 } ^ { 2 } = . 2 8$ , can we reject, at the 5 percent level, the hypothesis of equal variance? 

SOLUTION Program 5.8.3, which computes the F cumulative distribution function, yields that 

$$
P \{F _ {9, 1 1} \leq . 5 \} = . 1 5 3 9
$$

Hence, 

$$
\begin{array}{r l} p \text {-value} & = 2 \min \{. 1 5 3 9,. 8 4 6 1 \} \\ & = . 3 0 7 4 \end{array}
$$

and so the hypothesis of equal variance cannot be rejected. ■ 

## 8.6 HYPOTHESIS TESTS IN BERNOULLI POPULATIONS

The binomial distribution is frequently encountered in engineering problems. For a typical example, consider a production process that manufactures items that can be classified in one of two ways — either as acceptable or as defective. An assumption often made is that each item produced will, independently, be defective with probability $\mathbf { \nabla } ^ { p ; }$ and so the number of defects in a sample of n items will thus have a binomial distribution with parameters $( n , p )$ . We will now consider a test of 

$$
H _ {0}: p \leq p _ {0} \quad \text { versus } \quad H _ {1}: p > p _ {0}
$$

where $\mathit { p 0 }$ is some specified value. 

If we let $X$ denote the number of defects in the sample of size n, then it is clear that we wish to reject $H _ { 0 }$ when X is large. To see how large it need be to justify rejection at the α level of significance, note that 

$$
P \{X \geq k \} = \sum_ {i = k} ^ {n} P \{X = i \} = \sum_ {i = k} ^ {n} {\binom {n} {i}} p ^ {i} (1 - p) ^ {n - i}
$$

Now it is certainly intuitive (and can be proven) that $P \{ X \geq k \}$ is an increasing function of $\dot { \boldsymbol { p } }$ — that is, the probability that the sample will contain at least $k$ errors increases in the defect probability $\scriptstyle { \boldsymbol { p } } .$ . Using this, we see that when $H _ { 0 }$ is true (and so $ { \boldsymbol { p } } \leq p _ { 0 } )$ ), 

$$
P \{X \geq k \} \leq \sum_ {i = k} ^ {n} {\binom {n} {i}} p _ {0} ^ {i} (1 - p _ {0}) ^ {n - i}
$$

Hence, a significance level α test of $H _ { 0 } : p \leq p _ { 0 }$ versus $H _ { 1 } : p > p _ { 0 }$ is to reject $H _ { 0 }$ when 

$$
X \geq k ^ {*}
$$

where $k ^ { * }$ is the smallest value of k for which $\begin{array} { r } { \sum _ { i = k } ^ { n } \binom { n } { i } \mathcal { P } _ { 0 } ^ { i } ( 1 - \mathcal { p } _ { 0 } ) ^ { n - i } \le \alpha } \end{array}$ . That is, 

$$
k ^ {*} = \min \left\{k: \sum_ {i = k} ^ {n} {\binom {n} {i}} p _ {0} ^ {i} (1 - p _ {0}) ^ {n - i} \leq \alpha \right\}
$$

This test can best be performed by first determining the value of the test statistic — say, $X = x -$ and then computing the p-value given by 

$$
\begin{array}{l} p \text {-value} = P \{B (n, p _ {0}) \geq x \} \\ = \sum_ {i = x} ^ {n} \binom {n} {i} p _ {0} ^ {i} (1 - p _ {0}) ^ {n - i} \end{array}
$$

EXAMPLE 8.6a A computer chip manufacturer claims that no more than 2 percent of the chips it sends out are defective. An electronics company, impressed with this claim, has purchased a large quantity of such chips. To determine if the manufacturer’s claim can be taken literally, the company has decided to test a sample of 300 of these chips. If 10 of these 300 chips are found to be defective, should the manufacturer’s claim be rejected? 

SOLUTION Let us test the claim at the 5 percent level of significance. To see if rejection is called for, we need to compute the probability that the sample of size 300 would have resulted in 10 or more defectives when $\boldsymbol { \mathscr { P } }$ is equal to .02. (That is, we compute the p-value.) If this probability is less than or equal to .05, then the manufacturer’s claim 

should be rejected. Now 

$$
\begin{array}{l} P _ {. 0 2} \{X \geq 1 0 \} = 1 - P _ {. 0 2} \{X <   1 0 \} \\ \qquad = 1 - \sum_ {i = 0} ^ {9} \binom {3 0 0} {i} (. 0 2) ^ {i} (. 9 8) ^ {3 0 0 - i} \\ \qquad = . 0 8 1 8 \quad \text { from   Program   3.1 } \end{array}
$$

and so the manufacturer’s claim cannot be rejected at the 5 percent level of significance. ■ 

When the sample size n is large, we can derive an approximate significance level α test of $H _ { 0 } : p \leq p _ { 0 }$ versus $H _ { 1 } : p > p _ { 0 }$ by using the normal approximation to the binomial. It works as follows: Because when n is large X will have approximately a normal distribution with mean and variance 

$$
E [ X ] = n p, \qquad \operatorname{Var} (X) = n p (1 - p)
$$

it follows that 

$$
\frac {X - n p}{\sqrt {n p (1 - p)}}
$$

will have approximately a standard normal distribution. Therefore, an approximate significance level α test would be to reject $H _ { 0 }$ if 

$$
\frac {X - n p _ {0}}{\sqrt {n p _ {0} (1 - p _ {0})}} \geq z _ {\alpha}
$$

Equivalently, one can use the normal approximation to approximate the p-value. 

EXAMPLE 8.6b In Example 8.6a, $n p _ { 0 } = 3 0 0 ( . 0 2 ) = 6 { } _ { ; }$ , and $\sqrt { n p _ { 0 } ( 1 - p _ { 0 } ) } = \sqrt { 5 . 8 8 } .$ Consequently, the p-value that results from the data $X = 1 0$ is 

$$
\begin{array}{r l} p \text {-value} & = P _ {. 0 2} \{X \geq 1 0 \} \\ & = P _ {. 0 2} \{X \geq 9. 5 \} \\ & = P _ {. 0 2} \left\{\frac {X - 6}{\sqrt {5 . 8 8}} \geq \frac {9 . 5 - 6}{\sqrt {5 . 8 8}} \right\} \\ & \approx P \{Z \geq 1. 4 4 3 \} \\ & = . 0 7 4 5 \end{array}
$$

Suppose now that we want to test the null hypothesis tha $\boldsymbol { \mathscr { P } }$ is equal to some specified value; that is, we want to test 

$$
H _ {0}: p = p _ {0} \quad \text { versus } \quad H _ {1}: p \neq p _ {0}
$$

If $X ,$ , a binomial random variable with parameters n and ${ \boldsymbol { p } } ,$ is observed to equal $x ,$ then a significance level α test would reject $H _ { 0 }$ if the value x was either significantly larger or significantly smaller than what would be expected when $\boldsymbol { \mathscr { P } }$ is equal to $\mathit { p 0 }$ . More precisely, the test would reject $H _ { 0 }$ if either 

$$
P \{\operatorname{Bin} (n, p _ {0}) \geq x \} \leq \alpha / 2 \quad \text { or } \quad P \{\operatorname{Bin} (n, p _ {0}) \leq x \} \leq \alpha / 2
$$

In other words, the p-value when $X = x$ is 

$$
p \text {-value} = 2 \min (P \{\operatorname{Bin} (n, p _ {0}) \geq x \}, P \{\operatorname{Bin} (n, p _ {0}) \leq x \})
$$

EXAMPLE 8.6c Historical data indicate that 4 percent of the components produced at a certain manufacturing facility are defective. A particularly acrimonious labor dispute has recently been concluded, and management is curious about whether it will result in any change in this figure of 4 percent. If a random sample of 500 items indicated 16 defectives (3.2 percent), is this significant evidence, at the 5 percent level of significance, to conclude that a change has occurred? 

SOLUTION To be able to conclude that a change has occurred, the data need to be strong enough to reject the null hypothesis when we are testing 

$$
H _ {0}: p = . 0 4 \quad \text { versus } \quad H _ {1}: p \neq . 0 4
$$

where $\boldsymbol { \underline { P } }$ is the probability that an item is defective. The p-value of the observed data of 16 defectives in 500 items is 

$$
p \text {-value} = 2 \min \{P \{X \leq 1 6 \}, P \{X \geq 1 6 \} \}
$$

where X is a binomial (500, .04) random variable. Since $5 0 0 \times . 0 4 = 2 0$ , we see that 

$$
p \text {-value} = 2 P \{X \leq 1 6 \}
$$

Since X has mean 20 and standard deviation ${ \sqrt { 2 0 ( . 9 6 ) } } = 4 . 3 8$ , it is clear that twice the probability that X will be less than or equal to $1 6 - { \bf a }$ value less than one standard deviation lower than the mean — is not going to be small enough to justify rejection. Indeed, it can be shown that 

$$
p \text {-value} = 2 P \{X \leq 1 6 \} = . 4 3 2
$$

and so there is not sufficient evidence to reject the hypothesis that the probability of a defective item has remained unchanged. ■ 

## 8.6.1 Testing the Equality of Parameters in Two Bernoulli Populations

Suppose there are two distinct methods for producing a certain type of transistor; and suppose that transistors produced by the first method will, independently, be defective with probability $\displaystyle { \phi _ { 1 } }$ , with the corresponding probability being $\hbar 2$ for those produced by the second method. To test the hypothesis that $p _ { 1 } = p _ { 2 }$ , a sample of $\displaystyle n _ { 1 }$ transistors is produced using method 1 and $\boldsymbol { n _ { 2 } }$ using method 2. 

Let $X _ { 1 }$ denote the number of defective transistors obtained from the first sample and $X _ { 2 }$ for the second. Thus, $X _ { 1 }$ and $X _ { 2 }$ are independent binomial random variables with respective parameters $( n _ { 1 } , p _ { 1 } )$ and $( n _ { 2 } , p _ { 2 } )$ . Suppose that $X _ { 1 } + X _ { 2 } = k$ and so there have been a total of $k$ defectives. Now, if $H _ { 0 }$ is true, then each of the $n _ { 1 } + n _ { 2 }$ transistors produced will have the same probability of being defective, and so the determination of the $k$ defectives will have the same distribution as a random selection of a sample of size $k$ from a population of $n _ { 1 } + n _ { 2 }$ items of which $\displaystyle n _ { 1 }$ are white and $\boldsymbol { n _ { 2 } }$ are black. In other words, given a total of $k$ defectives, the conditional distribution of the number of defective transistors obtained from method 1 will, when $H _ { 0 }$ is true, have the following hypergeometric distribution*: 

$$
P _ {H _ {0}} \{X _ {1} = i | X _ {1} + X _ {2} = k \} = \frac {\binom {n _ {1}} {i} \binom {n _ {2}} {k - i}}{\binom {n _ {1} + n _ {2}} {k}}, \quad i = 0, 1, \ldots , k\tag{8.6.1}
$$

Now, in testing 

$$
H _ {0}: p _ {1} = p _ {2} \quad \text { versus } \quad H _ {1}: p _ {1} \neq p _ {2}
$$

it seems reasonable to reject the null hypothesis when the proportion of defective transistors produced by method 1 is much different than the proportion of defectives obtained under method 2. Therefore, if there is a total of $k$ defectives, then we would expect, when $H _ { 0 }$ is true, that $X _ { 1 } / n _ { 1 }$ (the proportion of defective transistors produced by method 1) would be close to $( k - X _ { 1 } ) / n _ { 2 }$ (the proportion of defective transistors produced by method 2). Because $X _ { 1 } / n _ { 1 }$ and $( k - X _ { 1 } ) / n _ { 2 }$ will be farthest apart when $X _ { 1 }$ is either very small or very large, it thus seems that a reasonable significance level α test of Equation 8.6.1 is as follows. If $X _ { 1 } + X _ { 2 } = k$ , then one should 

$$
\begin{array}{l l} \text { reject } & H _ {0} \quad \text { if   either } \quad P \{X \leq x _ {1} \} \leq \alpha / 2 \quad \text { or } \quad P \{X \geq x _ {1} \} \leq \alpha / 2 \\ \text { accept } & H _ {0} \quad \text { otherwise } \end{array}
$$

where X is a hypergeometric random variable with probability mass function 

$$
P \{X = i \} = \frac {\binom {n _ {1}} {i} \binom {n _ {2}} {k - i}}{\binom {n _ {1} + n _ {2}} {k}} \quad i = 0, 1, \ldots , k\tag{8.6.2}
$$

In other words, this test will call for rejection if the significance level is at least as large as the p-value given by 

$$
p \text {-value} = 2 \min (P \{X \leq x _ {1} \}, P \{X \geq x _ {1} \})\tag{8.6.3}
$$

This is called the Fisher-Irwin test. 

## COMPUTATIONS FOR THE FISHER-IRWIN TEST

To utilize the Fisher-Irwin test, we need to be able to compute the hypergeometric distribution function. To do so, note that with X having mass function Equation 8.6.2, 

$$
\begin{array}{c} \frac {P \{X = i + 1 \}}{P \{X = i \}} = \frac {\binom {n _ {1}} {i + 1} \binom {n _ {2}} {k - i - 1}}{\binom {n _ {1}} {i} \binom {n _ {2}} {k - i}} \\ = \frac {(n _ {1} - i) (k - i)}{(i + 1) (n _ {2} - k + i + 1)} \end{array}\tag{8.6.4}
$$

(8.6.5) 

where the verification of the final equality is left as an exercise. 

Program 8.6.1 uses the preceding identity to compute the p-value of the data for the Fisher-Irwin test of the equality of two Bernoulli probabilities. The program will work best if the Bernoulli outcome that is called unsuccessful (or defective) is the one whose probability is less than .5. For instance, if over half the items produced are defective, then rather than testing that the defect probability is the same in both samples, one should test that the probability of producing an acceptable item is the same in both samples. 

EXAMPLE 8.6d Suppose that method 1 resulted in 20 unacceptable transistors out of 100 produced; whereas method 2 resulted in 12 unacceptable transistors out of 100 produced. Can we conclude from this, at the 10 percent level of significance, that the two methods are equivalent? 

SOLUTION Upon running Program 8.6.1, we obtain that 

$$
p \text {-value} = . 1 7 6 3
$$

Hence, the hypothesis that the two methods are equivalent cannot be rejected. ■ 

The ideal way to test the hypothesis that the results of two different treatments are identical is to randomly divide a group of people into a set that will receive the first treatment and one that will receive the second. However, such randomization is not always possible. For instance, if we want to study whether drinking alcohol increases the risk of prostate cancer, we cannot instruct a randomly chosen sample to drink alcohol. An alternative way to study the hypothesis is to use an observational study that begins by randomly choosing a set of drinkers and one of nondrinkers. These sets are followed for a period of time and the resulting data is then used to test the hypothesis that members of the two groups have the same risk for prostate cancer. 

Our next sample illustrates another way of performing an observational study. 

EXAMPLE 8.6e In 1970, the researchers Herbst, Ulfelder, and Poskanzer (H-U-P) sus pected that vaginal cancer in young women, a rather rare disease, might be caused by one’s mother having taken the drug diethylstilbestrol (usually referred to as DES) while pregnant. To study this possibility, the researchers could have performed an observational study by searching for a (treatment) group of women whose mothers took DES when pregnant and a (control) group of women whose mothers did not. They could then observe these groups for a period of time and use the resulting data to test the hypoth esis that the probabilities of contracting vaginal cancer are the same for both groups. However, because vaginal cancer is so rare (in both groups) such a study would require a large number of individuals in both groups and would probably have to continue for many years to obtain significant results. Consequently, H-U-P decided on a different type of observational study. They uncovered 8 women between the ages of 15 and 22 who had vaginal cancer. Each of these women (called cases) was then matched with 4 others, called referents or controls. Each of the referents of a case was free of the cancer and was born within 5 days in the same hospital and in the same type of room (either private or public) as the case. Arguing that if DES had no effect on vaginal cancer then the probability, call it $\mathit { p _ { c } }$ , that the mother of a case took DES would be the same as the probability, call it ${ \boldsymbol { p } } _ { r }$ , that the mother of a referent took DES, the researchers H-U-P decided to test 

$$
H _ {0}: p _ {c} = p _ {r} \quad \text { against } \quad H _ {1}: p _ {c} \neq p _ {r}
$$

Discovering that $7$ of the 8 cases had mothers who took DES while pregnant, while none of the 32 referents had mothers who took the drug, the researchers (see Herbst, A., Ulfelder, H., and Poskanzer, D., “Adenocarcinoma of the Vagina: Association of Maternal Stilbestrol Therapy with Tumor Appearance in Young Women,” New England Journal of Medicine, 284, 878–881, 1971) concluded that there was a strong association between DES and vaginal cancer. (The p-value for these data is approximately 0.) ■ 

When $n _ { 1 }$ and $n _ { 2 }$ are large, an approximate level α test of $H _ { 0 } : p _ { 1 } = p _ { 2 }$ , based on the normal approximation to the binomial, is outlined in Problem 63. 

## 8.7 TESTS CONCERNING THE MEAN OF A POISSON DISTRIBUTION

Let X denote a Poisson random variable having mean λ and consider a test of 

$$
H _ {0}: \lambda = \lambda_ {0} \quad \text { versus } \quad H _ {1}: \lambda \neq \lambda_ {0}
$$

If the observed value of X is $X = x ,$ , then a level α test would reject $H _ { 0 }$ if either 

$$
P _ {\lambda_ {0}} \{X \geq x \} \leq \alpha / 2 \quad \text { or } \quad P _ {\lambda_ {0}} \{X \leq x \} \leq \alpha / 2\tag{8.7.1}
$$

where $P _ { \lambda _ { 0 } }$ means that the probability is computed under the assumption that the Poisson mean is $\lambda _ { 0 }$ . It follows from Equation 8.7.1 that the p-value is given by 

$$
p \text {-value} = 2 \min (P _ {\lambda_ {0}} \{X \geq x \}, P _ {\lambda_ {0}} \{X \leq x \})
$$

The calculation of the preceding probabilities that a Poisson random variable with mean λ<sub>0</sub> is greater (less) than or equal to x can be obtained by using Program 5.2. 

EXAMPLE 8.7a Management’s claim that the mean number of defective computer chips produced daily is not greater than 25 is in dispute. Test this hypothesis, at the 5 percent level of significance, if a sample of 5 days revealed 28, 34, 32, 38, and 22 defective chips. 

SOLUTION Because each individual computer chip has a very small chance of being defective, it is probably reasonable to suppose that the daily number of defective chips is approximately a Poisson random variable, with mean, say, λ. To see whether or not the manufacturer’s claim is credible, we shall test the hypothesis 

$$
H _ {0}: \lambda \leq 2 5 \quad \text { versus } \quad H _ {1}: \lambda > 2 5
$$

Now, under $H _ { 0 }$ , the total number of defective chips produced over a 5-day period is Poisson distributed (since the sum of independent Poisson random variables is Poisson) with a mean no greater than 125. Since this number is equal to 154, it follows that the p-value of the data is given by 

$$
\begin{array}{r l} p \text {-value} & = P _ {1 2 5} \{X \geq 1 5 4 \} \\ & = 1 - P _ {1 2 5} \{X \leq 1 5 3 \} \\ & = . 0 0 6 6 \quad \text { from   Program   5.2 } \end{array}
$$

Therefore, the manufacture’s claim is rejected at the 5 percent (as it would be even at the 1 percent) level of significance. ■ 

## REMARK

If Program 5.2 is not available, one can use the fact that a Poisson random variable with mean λ is, for large λ approximately normally distributed with a mean and variance equal to λ. 

## 8.7.1 Testing the Relationship Between Two Poisson Parameters

Let $X _ { 1 }$ and $X _ { 2 }$ be independent Poisson random variables with respective means $\lambda _ { 1 }$ and $\lambda _ { 2 }$ , and consider a test of 

$$
H _ {0}: \lambda_ {2} = c \lambda_ {1} \quad \text { versus } \quad H _ {1}: \lambda_ {2} \neq c \lambda_ {1}
$$

for a given constant c. Our test of this is a conditional test (similar in spirit to the Fisher Irwin test of Section 8.6.1), which is based on the fact that the conditional distribution of $X _ { 1 }$ given the sum of $X _ { 1 }$ and $X _ { 2 }$ is binomial. More specifically, we have the following proposition. 

## PROPOSITION 8.7.1

$$
P \{X _ {1} = k | X _ {1} + X _ {2} = n \} = \binom {n} {k} [ \lambda_ {1} / (\lambda_ {1} + \lambda_ {2}) ] ^ {k} [ \lambda_ {2} / (\lambda_ {1} + \lambda_ {2}) ] ^ {n - k}
$$

Proof 

$$
\begin{array}{l} P \{X _ {1} = k | X _ {1} + X _ {2} = n \} \\ \qquad = \frac {P \{X _ {1} = k , X _ {1} + X _ {2} = n \}}{P \{X _ {1} + X _ {2} = n \}} \\ \qquad = \frac {P \{X _ {1} = k , X _ {2} = n - k \}}{P \{X _ {1} + X _ {2} = n \}} \\ \qquad = \frac {P \{X _ {1} = k \} P \{X _ {2} = n - k \}}{P \{X _ {1} + X _ {2} = n \}} \text {by independence} \\ \qquad = \frac {\exp \{- \lambda_ {1} \} \lambda_ {1} ^ {k} / k ! \exp \{- \lambda_ {2} \} \lambda_ {2} ^ {n - k} / (n - k) !}{\exp \{- (\lambda_ {1} + \lambda_ {2}) \} (\lambda_ {1} + \lambda_ {2}) ^ {n} / n !} \\ \qquad = \frac {n !}{(n - k) ! k !} [ \lambda_ {1} / (\lambda_ {1} + \lambda_ {2}) ] ^ {k} [ \lambda_ {2} / (\lambda_ {1} + \lambda_ {2}) ] ^ {n - k} \quad \square \end{array}
$$

It follows from Proposition 8.7.1 that, if $H _ { 0 }$ is true, then the conditional distribution of $X _ { 1 }$ given that $X _ { 1 } + X _ { 2 } = n$ is the binomial distribution with parameters n and $\displaystyle { \phi = 1 / ( 1 + c ) }$ From this we can conclude that if $X _ { 1 } + X _ { 2 } = n _ { \cdot }$ , then $H _ { 0 }$ should be rejected if the observed value of $X _ { 1 }$ , call it $x _ { 1 }$ , is such that either 

$$
P \{\operatorname{Bin} (n, 1 / (1 + c)) \geq x _ {1} \} \leq \alpha / 2
$$

or 

$$
P \{\mathrm{Bin} (n, 1 / (1 + c)) \leq x _ {1} \} \leq \alpha / 2
$$

EXAMPLE 8.7b An industrial concern runs two large plants. If the number of accident during the last 8 weeks at plant 1 were 16, 18, 9, 22, 17, 19, 24, 8 while the number of accidents during the last 6 weeks at plant 2 were 22, 18, 26, 30, 25, 28, can we conclude, at the 5 percent level of significance, that the safety conditions differ from plant to plant? 

SOLUTION Since there is a small probability of an industrial accident in any given minute, it would seem that the weekly number of such accidents should have approximately a Poisson distribution. If we let $X _ { 1 }$ denote the total number of accidents during an 8-week period at plant 1, and let $X _ { 2 }$ be the number during a 6-week period at plant 2, then if the safety conditions did not differ at the two plants we would have that 

$$
\lambda_ {2} = \frac {3}{4} \lambda_ {1}
$$

where $\lambda _ { i } \equiv E [ X _ { i } ] , i = 1 , 2$ . Hence, as $X _ { 1 } = 1 3 3 , X _ { 2 } = 1 4 9$ it follows that the p-value of the test of 

$$
H _ {0}: \lambda_ {2} = \frac {3}{4} \lambda_ {1} \quad \text { versus } \quad H _ {1}: \lambda_ {2} \neq \frac {3}{4} \lambda_ {1}
$$

is given by 

$$
\begin{array}{r l} p \text {-value} & = 2 \min \bigl (P \bigl \{\operatorname{Bin} \bigl (2 8 2, \frac {4}{7} \bigr) \geq 1 3 3 \bigr \}, P \bigl \{\operatorname{Bin} \bigl (2 8 2, \frac {4}{7} \bigr) \leq 1 3 3 \bigr \} \bigr) \\ & = 9. 4 0 8 \times 1 0 ^ {- 4} \end{array}
$$

Thus, the hypothesis that the safety conditions at the two plants are equivalent is rejected. ■ 

EXAMPLE 8.7c In an attempt to show that proofreader A is superior to proofreader B, both proofreaders were given the same manuscript to read. If proofreader A found 28 errors, and proofreader B found 18, with 10 of these errors being found by both, can we conclude that A is the superior proofreader? 

SOLUTION To begin, we need a model. So let us assume that each manuscript error is independently found by proofreader A with probability $P _ { A }$ and by proofreader B with probability $P _ { B }$ . To see if the data prove that A is the superior proofreader, we need to check if it would lead to rejecting the hypothesis that B is at least as good. That is, we need to test the null hypothesis 

$$
H _ {0}: P _ {A} \leq P _ {B}
$$

against the alternative hypothesis 

$$
H _ {1}: P _ {A} > P _ {B}
$$

To determine a test, note that each error can be classified as being of one of 4 types: it is type 1 if it is found by both proofreaders; it is type 2 if found by A but not by B; it i type 3 if found by B but not by $\operatorname { A } ;$ and it is type 4 if found by neither. Thus, under our independence assumptions, it follows that each error will independently be type i with probability $\mathbf { \nabla } _ { \mathbf { \mathit { p } } _ { i } }$ , where 

$$
p _ {1} = P _ {A} P _ {B}, \quad p _ {2} = P _ {A} (1 - P _ {B}), \quad p _ {3} = (1 - P _ {A}) P _ {B}, \quad p _ {4} = (1 - P _ {A}) (1 - P _ {B})
$$

Now, if we do our analysis under the assumption that N , the total number of errors in the manuscript, is a random variable that is Poisson distributed with some unknown mean $\lambda ,$ , then it follows from the results of Section 5.2 that the numbers of errors of types 1, 2, 3, 4 are independent Poisson random variables with respective means $\lambda p _ { 1 } , \lambda p _ { 2 } , \lambda p _ { 3 } , \lambda p _ { 4 }$ Now, because $\textstyle { \frac { x } { 1 - x } } = { \frac { 1 } { 1 / x - 1 } }$ is an increasing function of x in the region $0 \leq x \leq 1$ 

$$
P _ {A} > P _ {B} \Leftrightarrow \frac {P _ {A}}{1 - P _ {A}} > \frac {P _ {B}}{1 - P _ {B}} \Leftrightarrow P _ {A} (1 - P _ {B}) > (1 - P _ {A}) P _ {B}
$$

In other words, $P _ { A } > P _ { B }$ if and only $\mathrm { { f } } _ { \mathit { p } _ { 2 } } > _ { \mathit { p } _ { 3 } }$ . As a result, it suffices to use the data to test 

$$
H _ {0}: p _ {2} \leq p _ {3} \quad \text { versus } \quad H _ {1}: p _ {2} > p _ {3}
$$

Therefore, with $N _ { 2 }$ denoting the number of errors of type 2 (that is, the number of errors found by A but not by B), and $N _ { 3 }$ the number of errors of type 3 (that is, the number found by B but not by A), it follows that we need to test 

$$
H _ {0}: E [ N _ {2} ] \leq E [ N _ {3} ] \quad \text { versus } \quad H _ {1}: E [ N _ {2} ] > E [ N _ {3} ]\tag{8.7.2}
$$

where $N _ { 2 }$ and $N _ { 3 }$ are independent Poisson random variables. Now, by Proposition 8.7.1, the conditional distribution of $N _ { 2 }$ given $N _ { 2 } + N _ { 3 }$ is binomial $( n , p )$ ) where $n = N _ { 2 } + N _ { 3 }$ and $\begin{array} { r } { \hat { p } = ( E [ N _ { 2 } ] ) / ( E [ N _ { 2 } ] + E [ N _ { 3 } ] ) } \end{array}$ . Because Equation 8.7.2 is equivalent to 

$$
H _ {0}: p \leq 1 / 2 \quad \text { versus } \quad H _ {1}: p > 1 / 2
$$

it follows that the p-value that results when $N _ { 2 } = n _ { 2 } , N _ { 3 } = n _ { 3 }$ is 

$$
p \text {-value} = P \{\operatorname{Bin} (n _ {2} + n _ {3},. 5) \geq n _ {2} \}
$$

For the data given, $n _ { 2 } = 1 8 , n _ { 3 } = 8$ , yielding that 

$$
p \text {-value} = P \{\text { Bin } (2 6,. 5) \geq 1 8 \} = . 0 3 7 8
$$

Consequently, at the 5 percent level of significance, the null hypothesis is rejected leading to the conclusion that A is the superior proofreader. ■ 

<table><tr><td>8.18</td><td>8.17</td></tr><tr><td>8.16</td><td>8.15</td></tr><tr><td>8.17</td><td>8.21</td></tr><tr><td>8.22</td><td>8.16</td></tr><tr><td>8.19</td><td>8.18</td></tr></table>

## Problems

1. Consider a trial in which a jury must decide between the hypothesis that the defendant is guilty and the hypothesis that he or she is innocent. 

(a) In the framework of hypothesis testing and the U.S. legal system, which of the hypotheses should be the null hypothesis? 

(b) What do you think would be an appropriate significance level in this situation? 

2. A colony of laboratory mice consists of several thousand mice. The average weight of all the mice is 32 grams with a standard deviation of 4 grams. A laboratory assistant was asked by a scientist to select 25 mice for an experi ment. However, before performing the experiment the scientist decided to weigh the mice as an indicator of whether the assistant’s selection constituted a ran dom sample or whether it was made with some unconscious bias (perhaps the mice selected were the ones that were slowest in avoiding the assistant, which might indicate some inferiority about this group). If the sample mean of the 25 mice was 30.4, would this be significant evidence, at the 5 percent level of significance, against the hypothesis that the selection constituted a random sample? 

3. A population distribution is known to have standard deviation 20. Determine the p-value of a test of the hypothesis that the population mean is equal to 50, if the average of a sample of 64 observations is (a) 52.5; (b) 55.0; (c) 57.5. 

4. In a certain chemical process, it is very important that a particular solution that is to be used as a reactant have a pH of exactly 8.20. A method for determining pH that is available for solutions of this type is known to give measurements that are normally distributed with a mean equal to the actual pH and with a standard deviation of .02. Suppose 10 independent measurements yielded the following pH values: 

(a) What conclusion can be drawn at the α = .10 level of significance? 

(b) What about at the $\alpha = . 0 5$ level of significance? 

5. The mean breaking strength of a certain type of fiber is required to be at least 200 psi. Past experience indicates that the standard deviation of breaking strength is 5 psi. If a sample of 8 pieces of fiber yielded breakage at the following pressures, 

<table><tr><td>210</td><td>198</td></tr><tr><td>195</td><td>202</td></tr><tr><td>197.4</td><td>196</td></tr><tr><td>199</td><td>195.5</td></tr></table>

would you conclude, at the 5 percent level of significance, that the fiber is unacceptable? What about at the 10 percent level of significance? 

6. It is known that the average height of a man residing in the United States is 5 feet 10 inches and the standard deviation is 3 inches. To test the hypothesis that men in your city are “average,” a sample of 20 men have been chosen. The heights of the men in the sample follow: 

<table><tr><td>Man</td><td>Height in</td><td>Inches</td><td>Man</td></tr><tr><td>1</td><td>72</td><td>70.4</td><td>11</td></tr><tr><td>2</td><td>68.1</td><td>76</td><td>12</td></tr><tr><td>3</td><td>69.2</td><td>72.5</td><td>13</td></tr><tr><td>4</td><td>72.8</td><td>74</td><td>14</td></tr><tr><td>5</td><td>71.2</td><td>71.8</td><td>15</td></tr><tr><td>6</td><td>72.2</td><td>69.6</td><td>16</td></tr><tr><td>7</td><td>70.8</td><td>75.6</td><td>17</td></tr><tr><td>8</td><td>74</td><td>70.6</td><td>18</td></tr><tr><td>9</td><td>66</td><td>76.2</td><td>19</td></tr><tr><td>10</td><td>70.3</td><td>77</td><td>20</td></tr></table>


What do you conclude? Explain what assumptions you are making. 


7. Suppose in Problem 4 that we wished to design a test so that if the pH were really equal to 8.20, then this conclusion will be reached with probability equal to .95. On the other hand, if the pH differs from 8.20 by .03 (in either direction), we want the probability of picking up such a difference to exceed .95. 

(a) What test procedure should be used? 

(b) What is the required sample size? 

(c) If x = 8.31, what is your conclusion? 

(d) If the actual pH is 8.32, what is the probability of concluding that the pH i not 8.20, using the foregoing procedure? 

8. Verify that the approximation in Equation 8.3.7 remains valid even when $\mu _ { 1 } < \mu _ { 0 }$ 

9. A British pharmaceutical company, Glaxo Holdings, has recently developed a new drug for migraine headaches. Among the claims Glaxo made for its drug, called somatriptan, was that the mean time it takes for it to enter the bloodstream is less than 10 minutes. To convince the Food and Drug Administration of the validity of this claim, Glaxo conducted an experiment on a randomly chosen set of migraine sufferers. To prove its claim, what should they have taken as the null and what as the alternative hypothesis? 

10. The weights of salmon grown at a commercial hatchery are normally distributed with a standard deviation of 1.2 pounds. The hatchery claims that the mean weight of this year’s crop is at least 7.6 pounds. Suppose a random sample of 16 fish yielded an average weight of 7.2 pounds. Is this strong enough evidence to reject the hatchery’s claims at the 

(a) 5 percent level of significance; 

(b) 1 percent level of significance? 

(c) What is the p-value? 

11. Consider a test of $H _ { 0 } : \mu \le 1 0 0$ versus $H _ { 1 } : \mu > 1 0 0$ . Suppose that a sample of size 20 has a sample mean of $\overline { { X } } = 1 0 5$ . Determine the p-value of this outcome if the population standard deviation is known to equal (a) 5; (b) 10; (c) 15. 

12. An advertisement for a new toothpaste claims that it reduces cavities of children in their cavity-prone years. Cavities per year for this age group are normal with mean 3 and standard deviation 1. A study of 2,500 children who used this toothpaste found an average of 2.95 cavities per child. Assume that the standard deviation of the number of cavities of a child using this new toothpaste remains equal to 1. 

(a) Are these data strong enough, at the 5 percent level of significance, to establish the claim of the toothpaste advertisement? 

(b) Do the data convince you to switch to this new toothpaste? 

13. There is some variability in the amount of phenobarbitol in each capsule sold by a manufacturer. However, the manufacturer claims that the mean value is 20.0 mg. To test this, a sample of 25 pills yielded a sample mean of 19.7 with a sample standard deviation of 1.3. What inference would you draw from these data? In particular, are the data strong enough evidence to discredit the claim of the manufacturer? Use the 5 percent level of significance. 

14. Twenty years ago, entering male high school students of Central High could do an average of 24 pushups in 60 seconds. To see whether this remains true today, a random sample of 36 freshmen was chosen. If their average was 22.5 with a sample standard deviation of 3.1, can we conclude that the mean is no longer equal to 24? Use the 5 percent level of significance. 

15. The mean response time of a species of pigs to a stimulus is .8 seconds. Twentyeight pigs were given 2 oz of alcohol and then tested. If their average response time was 1.0 seconds with a standard deviation of .3 seconds, can we conclude that alcohol affects the mean response time? Use the 5 percent level of significance. 

16. Suppose that team A and team B are to play a National Football League game and that team A is favored by f points. Let S(A) and S(B) denote the scores of teams A and B, and let $X = S ( A ) - S ( B ) - f .$ . That is, X is the amount by which team A beats the point spread. It has been claimed that the distribution of X is normal with mean 0 and standard deviation 14. Use data from randomly chosen footbal games to test this hypothesis. 

17. A medical scientist believes that the average basal temperature of (outwardly) healthy individuals has increased over time and is now greater than 98.6 degrees Fahrenheit (37 degrees Celsius). To prove this, she has randomly selected 100 healthy individuals. If their mean temperature is 98.74 with a sample standard deviation of 1.1 degrees, does this prove her claim at the 5 percent level? What about at the 1 percent level? 

18. Use the results of a Sunday’s worth of NFL professional football games to test the hypothesis that the average number of points scored by winning teams is less than or equal to 28. Use the 5 percent level of significance. 

19. Use the results of a Sunday’s worth of major league baseball scores to test the hypothesis that the average number of runs scored by winning teams is at least 5.6. Use the 5 percent level of significance. 

20. A car is advertised as having a gas mileage rating of at least 30 miles/gallon in highway driving. If the miles per gallon obtained in 10 independent experiments are 26, 24, 20, 25, 27, 25, 28, 30, 26, 33, should you believe the advertisement? What assumptions are you making? 

21. A producer specifies that the mean lifetime of a certain type of battery is at least 240 hours. A sample of 18 such batteries yielded the following data. 

<table><tr><td>237</td><td>242</td><td>232</td></tr><tr><td>242</td><td>248</td><td>230</td></tr><tr><td>244</td><td>243</td><td>254</td></tr><tr><td>262</td><td>234</td><td>220</td></tr><tr><td>225</td><td>236</td><td>232</td></tr><tr><td>218</td><td>228</td><td>240</td></tr></table>

Assuming that the life of the batteries is approximately normally distributed, do the data indicate that the specifications are not being met? 

22. Use the data of Example 2.3i of Chapter 2 to test the null hypothesis that the average noise level directly outside of Grand Central Station is less than or equal to 80 decibels. 

23. An oil company claims that the sulfur content of its diesel fuel is at most .15 percent. To check this claim, the sulfur contents of 40 randomly chosen samples were determined; the resulting sample mean and sample standard deviation were .162 and .040. Using the 5 percent level of significance, can we conclude that the company’s claims are invalid? 

24. A company supplies plastic sheets for industrial use. A new type of plastic has been produced and the company would like to claim that the average stress resistance of this new product is at least 30.0, where stress resistance is measured in pounds per square inch (psi) necessary to crack the sheet. The following random sample was drawn off the production line. Based on this sample, would the claim clearly be unjustified? 

30.1 32.7 22.5 27.5 

27.7 29.8 28.9 31.4 

31.2 24.3 26.4 22.8 

29.1 33.4 32.5 21.7 

Assume normality and use the 5 percent level of significance. 

25. It is claimed that a certain type of bipolar transistor has a mean value of current gain that is at least 210. A sample of these transistors is tested. If the sample mean value of current gain is 200 with a sample standard deviation of 35, would the claim be rejected at the 5 percent level of significance if 

(a) the sample size is 25; 

(b) the sample size is 64? 

26. A manufacturer of capacitors claims that the breakdown voltage of these capacitors has a mean value of at least 100 V. A test of 12 of these capacitors yielded the following breakdown voltages: 

96, 98, 105, 92, 111, 114, 99, 103, 95, 101, 106, 97 

Do these results prove the manufacturer’s claim? Do they disprove them? 

27. A sample of 10 fish were caught at lake A and their PCB concentrations were measured using a certain technique. The resulting data in parts per million were 

Lake A: 11.5, 10.8, 11.6, 9.4, 12.4, 11.4, 12.2, 11, 10.6, 10.8 

In addition, a sample of 8 fish were caught at lake B and their levels of PCB were measured by a different technique than that used at lake A. The resultant data were 

Lake B: 11.8, 12.6, 12.2, 12.5, 11.7, 12.1, 10.4, 12.6 

If it is known that the measuring technique used at lake A has a variance of .09 whereas the one used at lake B has a variance of .16, could you reject (at the 5 percent level of significance) a claim that the two lakes are equally contaminated? 

28. A method for measuring the pH level of a solution yields a measurement value that is normally distributed with a mean equal to the actual pH of the solution and with a standard deviation equal to .05. An environmental pollution scientist claims that two different solutions come from the same source. If this were so, then the pH level of the solutions would be equal. To test the plausibility of this claim, 10 independent measurements were made of the pH level for both solutions, with the following data resulting. 

<table><tr><td>Measurements of Solution A</td><td>Measurements of Solution B</td></tr><tr><td>6.24</td><td>6.27</td></tr><tr><td>6.31</td><td>6.25</td></tr><tr><td>6.28</td><td>6.33</td></tr><tr><td>6.30</td><td>6.27</td></tr><tr><td>6.25</td><td>6.24</td></tr><tr><td>6.26</td><td>6.31</td></tr><tr><td>6.24</td><td>6.28</td></tr><tr><td>6.29</td><td>6.29</td></tr><tr><td>6.22</td><td>6.34</td></tr><tr><td>6.28</td><td>6.27</td></tr></table>

(a) Do the data disprove the scientist’s claim? Use the 5 percent level of significance. 

(b) What is the p-value? 

29. The following are the values of independent samples from two different populations. 

<table><tr><td>Sample 1</td><td>122, 114, 130, 165, 144, 133, 139, 142, 150</td></tr><tr><td>Sample 2</td><td>108, 125, 122, 140, 132, 120, 137, 128, 138</td></tr></table>

Let $\mu _ { 1 }$ and $\mu _ { 2 }$ be the respective means of the two populations. Find the p-value of the test of the null hypothesis 

$$
H _ {0}: \mu_ {1} \leq \mu_ {2}
$$

versus the alternative 

$$
H _ {1}: \mu_ {1} > \mu_ {2}
$$

<table><tr><td>Type 1</td><td>32,84,37,42,78,62,59,74</td></tr><tr><td>Type 2</td><td>39,111,55,106,90,87,85</td></tr></table>

when the population standard deviations are $\sigma _ { 1 } = 1 0$ and (a) $\sigma _ { 2 } = 5 ; \left( \mathbf { b } \right) \sigma _ { 2 } = 1 0 ; \left( \mathbf { c } \right) \sigma _ { 2 } = 2 0 .$ 

30. The data below give the lifetimes in hundreds of hours of samples of two types of electronic tubes. Past lifetime data of such tubes have shown that they can often be modeled as arising from a lognormal distribution. That is, the logarithms of the data are normally distributed. Assuming that variance of the logarithms is equal for the two populations, test, at the 5 percent level of significance, the hypothesis that the two population distributions are identical. 

31. The viscosity of two different brands of car oil is measured and the following data resulted: 

<table><tr><td>Brand 1</td><td>10.62, 10.58, 10.33, 10.72, 10.44, 10.74</td></tr><tr><td>Brand 2</td><td>10.50, 10.52, 10.58, 10.62, 10.55, 10.51, 10.53</td></tr></table>

Test the hypothesis that the mean viscosity of the two brands is equal, assuming that the populations have normal distributions with equal variances. 

32. It is argued that the resistance of wire A is greater than the resistance of wire B. You make tests on each wire with the following results. 

<table><tr><td>Wire A</td><td>Wire B</td></tr><tr><td>.140 ohm</td><td>.135 ohm</td></tr><tr><td>.138</td><td>.140</td></tr><tr><td>.143</td><td>.136</td></tr><tr><td>.142</td><td>.142</td></tr><tr><td>.144</td><td>.138</td></tr><tr><td>.137</td><td>.140</td></tr></table>

What conclusion can you draw at the 10 percent significance level? Explain what assumptions you are making. 

In Problems 33 through 40, assume that the population distributions are normal and have equal variances. 

33. Twenty-five men between the ages of 25 and 30, who were participating in a well known heart study carried out in Framingham, Massachusetts, were randomly selected. Of these, 11 were smokers and 14 were not. The following data refer to readings of their systolic blood pressure. 

<table><tr><td>Smokers</td><td>Nonsmokers</td></tr><tr><td>124</td><td>130</td></tr><tr><td>134</td><td>122</td></tr><tr><td>136</td><td>128</td></tr><tr><td>125</td><td>129</td></tr><tr><td>133</td><td>118</td></tr><tr><td>127</td><td>122</td></tr><tr><td>135</td><td>116</td></tr><tr><td>131</td><td>127</td></tr><tr><td>133</td><td>135</td></tr><tr><td>125</td><td>120</td></tr><tr><td>118</td><td>122</td></tr><tr><td></td><td>120</td></tr><tr><td></td><td>115</td></tr><tr><td></td><td>123</td></tr></table>

Use these data to test the hypothesis that the mean blood pressures of smokers and nonsmokers are the same. 

34. In a 1943 experiment (Whitlock and Bliss, “A Bioassay Technique for Antihelminthics,” Journal of Parasitology, 29, pp. 48–58) 10 albino rats were used to study the effectiveness of carbon tetrachloride as a treatment for worms. Each rat received an injection of worm larvae. After 8 days, the rats were randomly divided into two groups of 5 each; each rat in the first group received a dose of .032 cc of carbon tetrachloride, whereas the dosage for each rat in the second group was .063 cc. Two days later the rats were killed, and the number of adult worms in each rat was determined. The numbers detected in the group receiving the .032 dosage were 

## 421, 462, 400, 378, 413

whereas they were 

## 207, 17, 412, 74, 116

for those receiving the .063 dosage. Do the data prove that the larger dosage is more effective than the smaller? 

35. A professor claims that the average starting salary of industrial engineering graduating seniors is greater than that of civil engineering graduates. To study this claim, samples of 16 industrial engineers and 16 civil engineers, all of whom graduated in 1993, were chosen and sample members were queried about their starting salaries. If the industrial engineers had a sample mean salary of $47,700 and a sample standard deviation of $2,400, and the civil engineers had a sample mean salary of $46,400 and a sample standard deviation of $2,200, has the professor’s claim been verified? Find the appropriate p-value. 

36. In a certain experimental laboratory, a method A for producing gasoline from crude oil is being investigated. Before completing experimentation, a new method B is proposed. All other things being equal, it was decided to abandon A in favor of B only if the average yield of the latter was clearly greater. The yield of both processes is assumed to be normally distributed. However, there has been insufficient time to ascertain their true standard deviations, although there appears to be no reason why they cannot be assumed equal. Cost considerations impose size limits on the size of samples that can be obtained. If a 1 percent significance level is all that is allowed, what would be your recommendation based on the following random samples? The numbers represent percent yield of crude oil. 

A 23.2, 26.6, 24.4, 23.5, 22.6, 25.7, 25.5 

B 25.7, 27.7, 26.2, 27.9, 25.0, 21.4, 26.1 

37. A study was instituted to learn how the diets of women changed during the winter and the summer. A random group of 12 women were observed during the month of July and the percentage of each woman’s calories that came from fat was determined. Similar observations were made on a different randomly selected group of size 12 during the month of January. The results were as follows: 

July 32.2, 27.4, 28.6, 32.4, 40.5, 26.2, 29.4, 25.8, 36.6, 30.3, 28.5, 32.0 January 30.5, 28.4, 40.2, 37.6, 36.5, 38.8, 34.7, 29.5, 29.7, 37.2, 41.5, 37.0 

Test the hypothesis that the mean fat percentage intake is the same for both months. Use the (a) 5 percent level of significance and (b) 1 percent level of significance. 

38. To learn about the feeding habits of bats, 22 bats were tagged and tracked by radio. Of these 22 bats, 12 were female and 10 were male. The distances flown (in meters) between feedings were noted for each of the 22 bats, and the following summary statistics were obtained. 

<table><tr><td>Female Bats</td><td>Male Bats</td></tr><tr><td><eq>n = 12</eq></td><td><eq>m = 10</eq></td></tr><tr><td><eq>\overline{X} = 180</eq></td><td><eq>\overline{Y} = 136</eq></td></tr><tr><td><eq>S_x = 92</eq></td><td><eq>S_y = 86</eq></td></tr></table>

Test the hypothesis that the mean distance flown between feedings is the same for the populations of both male and of female bats. Use the 5 percent level of significance. 

39. The following data summary was obtained from a comparison of the lead content of human hair removed from adult individuals that had died between 1880 and 1920 with the lead content of present-day adults. The data are in units of micrograms, equal to one-millionth of a gram. 

<table><tr><td></td><td>1880–1920</td><td>Today</td></tr><tr><td>Sample size:</td><td>30</td><td>100</td></tr><tr><td>Sample mean:</td><td>48.5</td><td>26.6</td></tr><tr><td>Sample standard deviation:</td><td>14.5</td><td>12.3</td></tr></table>

(a) Do the above data establish, at the 1 percent level of significance, that the mean lead content of human hair is less today than it was in the years between 1880 and 1920? Clearly state what the null and alternative hypotheses are. 

(b) What is the p-value for the hypothesis test in part (a)? 

40. Sample weights (in pounds) of newborn babies born in two adjacent counties in Western Pennsylvania yielded the following data. 

$$
\begin{array}{c c} n = 5 3, & m = 4 4 \\ \overline {{X}} = 6. 8, & \overline {{Y}} = 7. 2 \\ S ^ {2} = 5. 2, & S ^ {2} = 4. 9 \end{array}
$$

Consider a test of the hypothesis that the mean weight of newborns is the same in both counties. What is the resulting p-value? 

41. To verify the hypothesis that blood lead levels tend to be higher for children whose parents work in a factory that uses lead in the manufacturing process, researchers examined lead levels in the blood of 33 children whose parents worked in a battery manufacturing factory. (Morton, D., Saah, A., Silberg, S., Owens, W., Roberts, M., and Saah, M., “Lead Absorption in Children of Employees in a Lead-Related Industry,” American Journal of Epidemiology, 115, 549–555, 1982.) Each of these children were then matched by another child who was of similar age, lived in a similar neighborhood, had a similar exposure to traffic, but whose parent did not work with lead. The blood levels of the 33 cases (sample 1) as well as those of the 33 controls (sample 2) were then used to test the hypothesis that the average blood levels of these groups are the same. If the resulting sample means and sample standard deviations were 

$$
\bar {x} _ {1} = . 0 1 5, \quad s _ {1} = . 0 0 4, \quad \bar {x} _ {2} = . 0 0 6, \quad s _ {2} = . 0 0 6
$$

find the resulting p-value. Assume a common variance. 

42. Ten pregnant women were given an injection of pitocin to induce labor. Their systolic blood pressures immediately before and after the injection were: 

<table><tr><td>Patient</td><td>Before</td><td>After</td><td>Patient</td><td>Before</td><td>After</td></tr><tr><td>1</td><td>134</td><td>140</td><td>6</td><td>140</td><td>138</td></tr><tr><td>2</td><td>122</td><td>130</td><td>7</td><td>118</td><td>124</td></tr><tr><td>3</td><td>132</td><td>135</td><td>8</td><td>127</td><td>126</td></tr><tr><td>4</td><td>130</td><td>126</td><td>9</td><td>125</td><td>132</td></tr><tr><td>5</td><td>128</td><td>134</td><td>10</td><td>142</td><td>144</td></tr></table>

Do the data indicate that injection of this drug changes blood pressure? 

43. A question of medical importance is whether jogging leads to a reduction in one’s pulse rate. To test this hypothesis, 8 nonjogging volunteers agreed to begin a 1-month jogging program. After the month their pulse rates were determined and compared with their earlier values. If the data are as follows, can we conclude that jogging has had an effect on the pulse rates? 

<table><tr><td>Subject</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>Pulse Rate Before</td><td>74</td><td>86</td><td>98</td><td>102</td><td>78</td><td>84</td><td>79</td><td>70</td></tr><tr><td>Pulse Rate After</td><td>70</td><td>85</td><td>90</td><td>110</td><td>71</td><td>80</td><td>69</td><td>74</td></tr></table>

44. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population having unknown parameters µ and $\sigma ^ { 2 }$ , devise a significance level α test of 

$$
H _ {0} = \sigma^ {2} \leq \sigma_ {0} ^ {2}
$$

versus the alternative 

$$
H _ {1} = \sigma^ {2} > \sigma_ {0} ^ {2}
$$

for a given positive value $\sigma _ { 0 } ^ { 2 }$ . 

45. In Problem 44, explain how the test would be modified if the population mean µ were known in advance. 

46. A gun-like apparatus has recently been designed to replace needles in administering vaccines. The apparatus can be set to inject different amounts of the serum, but because of random fluctuations the actual amount injected is normally distributed with a mean equal to the setting and with an unknown variance $\sigma ^ { 2 }$ . It has been decided that the apparatus would be too dangerous to use if σ exceeds .10. If a random sample of 50 injections resulted in a sample standard deviation of .08, should use of the new apparatus be discontinued? Suppose the level of significance is $\alpha = . 1 0$ . Comment on the appropriate choice of a significance level for this problem, as well as the appropriate choice of the null hypothesis. 

47. A pharmaceutical house produces a certain drug item whose weight has a standard deviation of .5 milligrams. The company’s research team has proposed a new method of producing the drug. However, this entails some costs and will be adopted only if there is strong evidence that the standard deviation of the weight of the items will drop to below .4 milligrams. If a sample of 10 items is produced and has the following weights, should the new method be adopted? 

<table><tr><td>5.728</td><td>5.731</td></tr><tr><td>5.722</td><td>5.719</td></tr><tr><td>5.727</td><td>5.724</td></tr><tr><td>5.718</td><td>5.726</td></tr><tr><td>5.723</td><td>5.722</td></tr></table>

48. The production of large electrical transformers and capacitators requires the use of polychlorinated biphenyls (PCBs), which are extremely hazardous when released into the environment. Two methods have been suggested to monitor the levels of PCB in fish near a large plant. It is believed that each method will result in a normal random variable that depends on the method. Test the hypothesis at the α = .10 level of significance that both methods have the same variance, if a given fish is checked 8 times by each method with the following data (in parts per million) recorded. 

<table><tr><td>Method 1</td><td>6.2, 5.8, 5.7, 6.3, 5.9, 6.1, 6.2, 5.7</td></tr><tr><td>Method 2</td><td>6.3, 5.7, 5.9, 6.4, 5.8, 6.2, 6.3, 5.5</td></tr></table>

49. In Problem 31, test the hypothesis that the populations have the same variances. 

50. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population with variance $\sigma _ { x } ^ { 2 }$ , and $Y _ { 1 } , \dots , Y _ { n }$ is an independent sample from normal population with variance $\sigma _ { y } ^ { 2 }$ develop a significance level α test of 

$$
H _ {0}: \sigma_ {x} ^ {2} <   \sigma_ {y} ^ {2} \quad \text { versus } \quad H _ {1}: \sigma_ {x} ^ {2} > \sigma_ {y} ^ {2}
$$

51. The amount of surface wax on each side of waxed paper bags is believed to be normally distributed. However, there is reason to believe that there is greater variation in the amount on the inner side of the paper than on the outside. A sample of 75 observations of the amount of wax on each side of these bags is obtained and the following data recorded. 

<table><tr><td colspan="2">Wax in Pounds per Unit Area of Sample</td></tr><tr><td>Outside Surface</td><td>Inside Surface</td></tr><tr><td><eq>\bar{x} = .948</eq></td><td><eq>\bar{y} = .652</eq></td></tr><tr><td><eq>\sum x_{i}^{2} = 91</eq></td><td><eq>\sum y_{i}^{2} = 82</eq></td></tr></table>

Conduct a test to determine whether or not the variability of the amount of wax on the inner surface is greater than the variability of the amount on the outer surface (α = .05). 

52. In a famous experiment to determine the efficacy of aspirin in preventing heart attacks, 22,000 healthy middle-aged men were randomly divided into two equal groups, one of which was given a daily dose of aspirin and the other a placebo that looked and tasted identical to the aspirin. The experiment was halted at a time when 104 men in the aspirin group and 189 in the control group had had heart attacks. Use these data to test the hypothesis that the taking of aspirin does not change the probability of having a heart attack. 

53. In the study of Problem 52, it also resulted that 119 from the aspirin group and 98 from the control group suffered strokes. Are these numbers significant to show that taking aspirin changes the probability of having a stroke? 

54. A standard drug is known to be effective in 72 percent of the cases in which it is used to treat a certain infection. A new drug has been developed and testing has found it to be effective in 42 cases out of 50. Is this strong enough evidence to prove that the new drug is more effective than the old one? Find the relevant p-value. 

55. Three independent news services are running a poll to determine if over half the population supports an initiative concerning limitations on driving automobiles in the downtown area. Each wants to see if the evidence indicates that over half the population is in favor. As a result, all three services will be testing 

$$
H _ {0}: p \leq . 5 \quad \text { versus } \quad H _ {1}: p >. 5
$$

where p is the proportion of the population in favor of the initiative. 

(a) Suppose the first news organization samples 100 people, of which 56 are in favor of the initiative. Is this strong enough evidence, at the 5 percent level of significance, to reject the null hypothesis and so establish that over half the population favors the initiative? 

(b) Suppose the second news organization samples 120 people, of which 68 are in favor of the initiative. Is this strong enough evidence, at the 5 percent level of significance, to reject the null hypothesis? 

(c) Suppose the third news organization samples 110 people, of which 62 are in favor of the initiative. Is this strong enough evidence, at the 5 percent level of significance, to reject the null hypothesis? 

(d) Suppose the news organizations combine their samples, to come up with a sample of 330 people, of which 186 support the initiative. Is this strong enough evidence, at the 5 percent level of significance, to reject the null hypothesis? 

56. According to the U.S. Bureau of the Census, 25.5 percent of the population of those age 18 or over smoked in 1990. A scientist has recently claimed that this percentage has since increased, and to prove her claim she randomly sampled 500 individuals from this population. If 138 of them were smokers, is her claim proved? Use the 5 percent level of significance. 

57. An ambulance service claims that at least 45 percent of its calls involve lifethreatening emergencies. To check this claim, a random sample of 200 calls was selected from the service’s files. If 70 of these calls involved life-threatening emergencies, is the service’s claim believable at the 

(a) 5 percent level of significance; 

(b) 1 percent level of significance? 

58. A standard drug is known to be effective in 75 percent of the cases in which it is used to treat a certain infection. A new drug has been developed and has been found to be effective in 42 cases out of 50. Based on this, would you accept, at the 5 percent level of significance, the hypothesis that the two drugs are of equal effectiveness? What is the p-value? 

59. Do Problem 58 by using a test based on the normal approximation to the binomial. 

60. In a recently conducted poll, 54 out of 200 people surveyed claimed to have a firearm in their homes. In a similar survey done earlier, 30 out of 150 people made that claim. Is it possible that the proportion of the population having firearms has not changed and the foregoing is due to the inherent randomness in sampling? 

61. Let $X _ { 1 }$ denote a binomial random variable with parameters $( n _ { 1 } , p _ { 1 } )$ and $X _ { 2 }$ an independent binomial random variable with parameters $( n _ { 2 } , p _ { 2 } )$ . Develop a test, using the same approach as in the Fisher-Irwin test, of 

$$
H _ {0}: p _ {1} \leq p _ {2}
$$

versus the alternative 

$$
H _ {1}: p _ {1} > p _ {2}
$$

62. Verify that Equation 8.6.5 follows from Equation 8.6.4. 

63. Let $X _ { 1 }$ and $X _ { 2 }$ be binomial random variables with respective parameters $n _ { 1 } , p _ { 1 }$ and $n _ { 2 } , \hbar _ { 2 }$ . Show that when $n _ { 1 }$ and $n _ { 2 }$ are large, an approximate level α test of $H _ { 0 } : p _ { 1 } = p _ { 2 }$ versus $H _ { 1 } : p _ { 1 } \neq p _ { 2 }$ is as follows: 

$$
\text { reject } \quad H _ {0} \quad \text { if } \quad \frac {| X _ {1} / n _ {1} - X _ {2} / n _ {2} |}{\sqrt {\frac {X _ {1} + X _ {2}}{n _ {1} + n _ {2}} \left(1 - \frac {X _ {1} + X _ {2}}{n _ {1} + n _ {2}}\right) \left(\frac {1}{n _ {1}} + \frac {1}{n _ {2}}\right)}} > z _ {\alpha / 2}
$$

Hint: (a) Argue first that when $n _ { 1 }$ and $n _ { 2 }$ are large 

$$
\frac {\frac {X _ {1}}{n _ {1}} - \frac {X _ {2}}{n _ {2}} - (p _ {1} - p _ {2})}{\sqrt {\frac {p _ {1} (1 - p _ {1})}{n _ {1}} + \frac {p _ {2} (1 - p _ {2})}{n _ {2}}}} \dot {\sim} N (0, 1)
$$

where $\sim$ means “approximately has the distribution.” 

(b) Now argue that when $H _ { 0 }$ is true and so $\ b { \mathscr { P } } 1 = \ b { \mathscr { p } } 2$ , their common value can be best estimated by $( X _ { 1 } + X _ { 2 } ) / ( n _ { 1 } + n _ { 2 } )$ 

64. Use the approximate test given in Problem 63 on the data of Problem 60. 

65. Patients suffering from cancer must often decide whether to have their tumors treated with surgery or with radiation. A factor in their decision is the 5-year survival rates for these treatments. Surprisingly, it has been found that patient’s decisions often seem to be affected by whether they are told the 5-year survival rates or the 5-year death rates (even though the information content is identical). For instance, in an experiment a group of 200 male prostate cancer patients were randomly divided into two groups of size 100 each. Each member of the first group was told that the 5-year survival rate for those electing surgery was $7 7$ percent, whereas each member of the second group was told that the 5-year death rate for those electing surgery was 23 percent. Both groups were given the same information about radiation therapy. If it resulted that 24 members of the first group and 12 of the second group elected to have surgery, what conclusions would you draw? 

66. The following data refer to Larry Bird’s results when shooting a pair of free throws in basketball. During two consecutive seasons in the National Basketball Association, Bird shot a pair of free throws on 338 occasions. On 251 occasions he made both shots; on 34 occasions he made the first shot but missed the second one; on 48 occasions he missed the first shot but made the second one; on 5 occasions he missed both shots. 

(a) Use these data to test the hypothesis that Bird’s probability of making the first shot is equal to his probability of making the second shot. 

(b) Use these data to test the hypothesis that Bird’s probability of making the second shot is the same regardless of whether he made or missed the first one. 

67. In the nineteen seventies, the U.S. Veterans Administration (Murphy, 1977) conducted an experiment comparing coronary artery bypass surgery with medical drug therapy as treatments for coronary artery disease. The experiment involved 596 patients, of whom 286 were randomly assigned to receive surgery, with the remaining 310 assigned to drug therapy. A total of 252 of those receiving surgery, and a total of 270 of those receiving drug therapy were still alive three years after treatment. Use these data to test the hypothesis that the survival probabilities are equal. 

68. Test the hypothesis, at the .05 level of significance, that the yearly number of earthquakes felt on a certain island has mean 52 if the readings for the last 8 years are 46, 62, 60, 58, 47, 50, 59, 49. Assume an underlying Poisson distribution and give an explanation to justify this assumption. 

69. The following table gives the number of fatal accidents of U.S. commercial airline carriers in the 16 years from 1980 to 1995. Do these data disprove, at the 5 percent level of significance, the hypothesis that the mean number of accidents in a year is greater than or equal to 4.5? What is the p-value? (Hint: First formulate a model for the number of accidents.) 


U.S. Airline Safety, Scheduled Commercial Carriers, 1980–1995


<table><tr><td></td><td>Departures (millions)</td><td>Fatal Accidents</td><td colspan="3">Fatal Accidents per 100,000 Departures</td><td>Departures (millions)</td><td>Fatal Accidents</td><td>Fatalities</td></tr><tr><td>1980 ....</td><td>5.4</td><td>0</td><td>0</td><td>.000</td><td>1988 ....</td><td>6.7</td><td>3</td><td>285</td></tr><tr><td>1981 ....</td><td>5.2</td><td>4</td><td>4</td><td>.077</td><td>1989 ....</td><td>6.6</td><td>11</td><td>278</td></tr><tr><td>1982 ....</td><td>5.0</td><td>4</td><td>233</td><td>.060</td><td>1990...</td><td>6.9</td><td>6</td><td>39</td></tr><tr><td>1983 ....</td><td>5.0</td><td>4</td><td>15</td><td>.079</td><td>1991 ....</td><td>6.8</td><td>4</td><td>62</td></tr><tr><td>1984 ....</td><td>5.4</td><td>1</td><td>4</td><td>.018</td><td>1992 ....</td><td>7.1</td><td>4</td><td>33</td></tr><tr><td>1985 ....</td><td>5.8</td><td>4</td><td>197</td><td>.069</td><td>1993 ....</td><td>7.2</td><td>1</td><td>1</td></tr><tr><td>1986 ....</td><td>6.4</td><td>2</td><td>5</td><td>.016</td><td>1994 ....</td><td>7.5</td><td>4</td><td>239</td></tr><tr><td>1987 ....</td><td>6.6</td><td>4</td><td>231</td><td>.046</td><td>1995 ....</td><td>8.1</td><td>2</td><td>166</td></tr></table>


Source: National Transportation Safety Board 


70. For the following data, sample 1 is from a Poisson distribution with mean $\lambda _ { 1 }$ and sample 2 is from a Poisson distribution with mean $\lambda _ { 2 }$ . Test the hypothesis that $\lambda _ { 1 } = \lambda _ { 2 }$ 

<table><tr><td>Sample 1</td><td>24, 32, 29, 33, 40, 28, 34, 36</td></tr><tr><td>Sample 2</td><td>42, 36, 41</td></tr></table>

71. A scientist looking into the effect of smoking on heart disease has chosen a large random sample of smokers and of nonsmokers. She plans to study these two groups for 5 years to see if the number of heart attacks among the members of the smokers’ group is significantly greater than the number among the nonsmokers. Such a result, the scientist feels, should be strong evidence of an association between 

smoking and heart attacks. Given that 

1. Older people are at greater risk of heart disease than are younger people; and 2. As a group, smokers tend to be somewhat older than nonsmokers; 

would the scientist be justified in her conclusion? Explain how the experi mental design can be improved so that meaningful conclusions can be drawn. 

72. A researcher wants to analyze the average yearly increase in a stock over a 20 year period. To do so, she plans to randomly choose 100 stocks from the listing of current stocks, discarding any that were not in existence 20 years ago. She will then compare the current price of each stock with its price 20 years ago to determine its percentage increase. Do you think this is a valid method to study the average increase in the price of a stock? 

# REGRESSION

## 9.1 INTRODUCTION

Many engineering and scientific problems are concerned with determining a relationship between a set of variables. For instance, in a chemical process, we might be interested in the relationship between the output of the process, the temperature at which it occurs, and the amount of catalyst employed. Knowledge of such a relationship would enable us to predict the output for various values of temperature and amount of catalyst. 

In many situations, there is a single response variable Y , also called the dependent vari able, which depends on the value of a set of input, also called independent, variables $x _ { 1 } , \ldots , x _ { r }$ . The simplest type of relationship between the dependent variable Y and the input variables $x _ { 1 } , \ldots , x _ { r }$ is a linear relationship. That is, for some constants $\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { r }$ the equation 

$$
Y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {r} x _ {r}\tag{9.1.1}
$$

would hold. If this was the relationship between Y and the $x _ { i } , i = 1 , \ldots , r ,$ , then it would be possible (once the $\beta _ { i }$ were learned) to exactly predict the response for any set of input values. However, in practice, such precision is almost never attainable, and the most that one can expect is that Equation 9.1.1 would be valid subject to random error. By this we mean that the explicit relationship is 

$$
Y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {r} x _ {r} + e\tag{9.1.2}
$$

where $^ { e , }$ representing the random error, is assumed to be a random variable having mean 0. Indeed, another way of expressing Equation 9.1.2 is as follows: 

$$
E [ Y | \mathbf {x} ] = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {r} x _ {r}
$$

where $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { r } )$ is the set of independent variables, and $E [ Y | \mathbf { x } ]$ is the expected response given the inputs x. 

Equation 9.1.2 is called a linear regression equation. We say that it describes the regression of Y on the set of independent variables $x _ { 1 } , \ldots , x _ { r }$ . The quantities $\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { r }$ are called the regression coefficients, and must usually be estimated from a set of data. A regression equation containing a single independent variable — that is, one in which $r = 1 -$ is called a simple regression equation, whereas one containing many independent variables is called a multiple regression equation. 

Thus, a simple linear regression model supposes a linear relationship between the mean response and the value of a single independent variable. It can be expressed as 

$$
Y = \alpha + \beta x + e
$$

where $_ x$ is the value of the independent variable, also called the input level, Y is the response, and $e ,$ representing the random error, is a random variable having mean 0. 

EXAMPLE 9.1a Consider the following 10 data pairs $( x _ { i } , y _ { i } ) , i = 1 , \dotsc , 1 0$ , relating y, the percent yield of a laboratory experiment, to x, the temperature at which the experiment was run. 

$$
\begin{array}{c c c c c c} i & x _ {i} & y _ {i} & i & x _ {i} & y _ {i} \\ 1 & 1 0 0 & 4 5 & 6 & 1 5 0 & 6 8 \\ 2 & 1 1 0 & 5 2 & 7 & 1 6 0 & 7 5 \\ 3 & 1 2 0 & 5 4 & 8 & 1 7 0 & 7 6 \\ 4 & 1 3 0 & 6 3 & 9 & 1 8 0 & 9 2 \\ 5 & 1 4 0 & 6 2 & 1 0 & 1 9 0 & 8 8 \end{array}
$$

A plot of $\dot { y } _ { i }$ versus x — called a scatter diagram — is given in Figure 9.1. As this scatter diagram appears to reflect, subject to random error, a linear relation between y and $x ,$ it seems that a simple linear regression model would be appropriate. ■ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/02b436b5420c116e736e8954a6b1cc2d13bf06fc7a2640db0e15540e28313e8e.jpg)



FIGURE 9.1 Scatter plot.


## 9.2 LEAST SQUARES ESTIMATORS OF THE REGRESSION PARAMETERS

Suppose that the responses $Y _ { i }$ corresponding to the input values $x _ { i } , i = 1 , \dotsc , n$ are to be observed and used to estimate α and $\beta$ in a simple linear regression model. To determine estimators of α and $\beta$ we reason as follows: If A is the estimator of α and B of $\dot { \boldsymbol { \beta } }$ , then the estimator of the response corresponding to the input variable $x _ { i }$ would be $A + B x _ { i }$ . Since the actual response is $Y _ { i : }$ , the squared difference is $( Y _ { i } - A - B x _ { i } ) ^ { 2 }$ , and so if A and B are the estimators of α and $\beta _ { i }$ , then the sum of the squared differences between the estimated responses and the actual response values — call it SS — is given by 

$$
S S = \sum_ {i = 1} ^ {n} (Y _ {i} - A - B x _ {i}) ^ {2}
$$

The method of least squares chooses as estimators of $\alpha$ and $\beta$ the values of $A$ and $B$ that minimize SS. To determine these estimators, we differentiate SS first with respect to A and then to $B$ as follows: 

$$
\begin{array}{l} \frac {\partial S S}{\partial A} = - 2 \sum_ {i = 1} ^ {n} (Y _ {i} - A - B x _ {i}) \\ \frac {\partial S S}{\partial B} = - 2 \sum_ {i = 1} ^ {n} x _ {i} (Y _ {i} - A - B x _ {i}) \end{array}
$$

Setting these partial derivatives equal to zero yields the following equations for the minimizing values A and $B \colon$ 

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} Y _ {i} = n A + B \sum_ {i = 1} ^ {n} x _ {i} \\ \sum_ {i = 1} ^ {n} x _ {i} Y _ {i} = A \sum_ {i = 1} ^ {n} x _ {i} + B \sum_ {i = 1} ^ {n} x _ {i} ^ {2} \end{array}\tag{9.2.1}
$$

The Equations 9.2.1 are known as the normal equations. If we let 

$$
\overline {{Y}} = \sum_ {i} Y _ {i} / n, \qquad \overline {{x}} = \sum_ {i} x _ {i} / n
$$

then we can write the first normal equation as 

$$
A = \overline {{Y}} - B \overline {{x}}\tag{9.2.2}
$$

Substituting this value of A into the second normal equation yields 

$$
\sum_ {i} x _ {i} Y _ {i} = (\overline {{Y}} - B \overline {{x}}) n \overline {{x}} + B \sum_ {i} x _ {i} ^ {2}
$$

or 

$$
B \left(\sum_ {i} x _ {i} ^ {2} - n \overline {{{x}}} ^ {2}\right) = \sum_ {i} x _ {i} Y _ {i} - n \overline {{{x}}} \overline {{{Y}}}
$$

or 

$$
B = \frac {\sum_ {i} x _ {i} Y _ {i} - n \overline {{x}} \overline {{Y}}}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}}
$$

Hence, using Equation 9.2.2 and the fact that $\begin{array} { r } { n \overline { { Y } } ~ = ~ \sum _ { i = 1 } ^ { n } Y _ { i } } \end{array}$ , we have proven the following proposition. 

PROPOSITION 9.2.1 The least squares estimators of $\beta$ and α corresponding to the data set $x _ { i } , Y _ { i } , i = 1 , \dotsc , n { \mathrm { ~ a r e } } .$ , respectively, 

$$
B = \frac {\sum_ {i = 1} ^ {n} x _ {i} Y _ {i} - \overline {{{x}}} \sum_ {i = 1} ^ {n} Y _ {i}}{\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{{x}}} ^ {2}}
$$

$$
A = \overline {{Y}} - B \overline {{x}}
$$

The straight line $A + B x$ is called the estimated regression line. 

Program 9.2 computes the least squares estimators A and B. It also gives the user the option of computing some other statistics whose values will be needed in the following sections. 


EXAMPLE 9.2a The raw material used in the production of a certain synthetic fiber is stored in a location without a humidity control. Measurements of the relative humidity in the storage location and the moisture content of a sample of the raw material were taken over 15 days with the following data (in percentages) resulting.


<table><tr><td>Relative humidity</td><td>46</td><td>53</td><td>29</td><td>61</td><td>36</td><td>39</td><td>47</td><td>49</td><td>52</td><td>38</td><td>55</td><td>32</td><td>57</td><td>54</td><td>44</td></tr><tr><td>Moisture content</td><td>12</td><td>15</td><td>7</td><td>17</td><td>10</td><td>11</td><td>11</td><td>12</td><td>14</td><td>9</td><td>16</td><td>8</td><td>18</td><td>14</td><td>12</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/6bc60452d25f74d730a70ff6443ba5d51c41e8275e268b3052fcd0d034970e10.jpg)



FIGURE 9.2 Example 9.2a.


These data are plotted in Figure 9.2. To compute the least squares estimator and the estimated regression line, we run Program 9.2; results are shown in Figure 9.3. ■ 

## 9.3 DISTRIBUTION OF THE ESTIMATORS

To specify the distribution of the estimators A and $B ,$ it is necessary to make additional assumptions about the random errors aside from just assuming that their mean is 0. The usual approach is to assume that the random errors are independent normal random variables having mean 0 and variance $\sigma ^ { 2 }$ . That is, we suppose that if $Y _ { i }$ is the response corresponding to the input value $x _ { i } ,$ , then $Y _ { i } , \ldots , Y _ { n }$ are independent and 

$$
Y _ {i} \sim \mathcal {N} (\alpha + \beta x _ {i}, \sigma^ {2})
$$

Note that the foregoing supposes that the variance of the random error does not depend on the input value but rather is a constant. This value $\sigma ^ { 2 }$ is not assumed to be known but rather must be estimated from the data. 

Since the least squares estimator B of $\dot { \boldsymbol { { \beta } } }$ can be expressed as 

$$
B = \frac {\sum_ {i} (x _ {i} - \overline {{x}}) Y _ {i}}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}}\tag{9.3.1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/6c3b801d1a14ec3626fcda9733793a4ecc2b73506de19cd38a042add62ca9a6b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/7352daa3b71d1fa8cee326306c566f433d6474fa828c263a85e57198b91ed006.jpg)



FIGURE 9.3


we see that it is a linear combination of the independent normal random variables $Y _ { i } ,$ $i = 1 , \ldots , n$ and so is itself normally distributed. Using Equation 9.3.1, the mean and variance of B are computed as follows: 

$$
\begin{array}{r} E [ B ] = \frac {\sum_ {i} (x _ {i} - \overline {{x}}) E [ Y _ {i} ]}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \\ = \frac {\sum_ {i} (x _ {i} - \overline {{x}}) (\alpha + \beta x _ {i})}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \end{array}
$$

$$
\begin{array}{r l} & = \frac {\alpha \sum_ {i} (x _ {i} - \overline {{x}}) + \beta \sum_ {i} x _ {i} (x _ {i} - \overline {{x}})}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \\ & = \beta \frac {\left[ \sum_ {i} x _ {i} ^ {2} - \overline {{x}} \sum_ {i} x _ {i} \right]}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \quad \text {since} \sum_ {i} (x _ {i} - \overline {{x}}) = 0 \\ & = \beta \end{array}
$$

Thus $E [ B ] = \beta$ and so $B$ is an unbiased estimator of $\beta .$ . We will now compute the variance of $B .$ 

$$
\begin{array}{l} \operatorname{Var} (B) = \frac {\operatorname{Var} \left(\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) Y _ {i}\right)}{\left(\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}\right) ^ {2}} \\ = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} \operatorname{Var} (Y _ {i})}{\left(\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}\right) ^ {2}} \text { by independence } \\ = \frac {\sigma^ {2} \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2}}{\left(\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}\right) ^ {2}} \\ = \frac {\sigma^ {2}}{\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \end{array}\tag{9.3.2}
$$

where the final equality results from the use of the identity 

$$
\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}
$$

Using Equation 9.3.1 along with the relationship 

$$
A = \sum_ {i = 1} ^ {n} \frac {Y _ {i}}{n} - B \overline {{x}}
$$

shows that $A$ can also be expressed as a linear combination of the independent normal random variables $Y _ { i } , i = 1 , \dots , n$ and is thus also normally distributed. Its mean is obtained from 

$$
\begin{array}{r l} & E [ A ] = \sum_ {i = 1} ^ {n} \frac {E [ Y _ {i} ]}{n} - \overline {{x}} E [ B ] \\ & \qquad = \sum_ {i = 1} ^ {n} \frac {(\alpha + \beta x _ {i})}{n} - \overline {{x}} \beta \\ & \qquad = \alpha + \beta \overline {{x}} - \overline {{x}} \beta \\ & \qquad = \alpha \end{array}
$$

Thus $A$ is also an unbiased estimator. The variance of $A$ is computed by first expressing $A$ as a linear combination of the $Y _ { i }$ . The result (whose details are left as an exercise) is that 

$$
\operatorname{Var} (A) = \frac {\sigma^ {2} \sum_ {i = 1} ^ {n} x _ {i} ^ {2}}{n \left(\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \bar {x} ^ {2}\right)}\tag{9.3.3}
$$

The quantities $Y _ { i } - A - B x _ { i } , i = 1 , \dots , n ,$ , which represent the differences between the actual responses (that is, the $Y _ { i } )$ and their least squares estimators (that is, $A + B x _ { i } )$ are called the residuals. The sum of squares of the residuals 

$$
S S _ {R} = \sum_ {i = 1} ^ {n} (Y _ {i} - A - B x _ {i}) ^ {2}
$$

can be utilized to estimate the unknown error variance $\sigma ^ { 2 }$ . Indeed, it can be shown that 

$$
\frac {S S _ {R}}{\sigma^ {2}} \sim \chi_ {n - 2} ^ {2}
$$

That is, $S S _ { R } / \sigma ^ { 2 }$ has a chi-square distribution with $n - 2$ degrees of freedom, which implies that 

$$
E \left[ \frac {S S _ {R}}{\sigma^ {2}} \right] = n - 2
$$

or 

$$
E \left[ \frac {S S _ {R}}{n - 2} \right] = \sigma^ {2}
$$

Thus $S S _ { R } / ( n - 2 )$ is an unbiased estimator of $\sigma ^ { 2 }$ . In addition, it can be shown that $S S _ { R }$ is independent of the pair A and B. 

## REMARKS

A plausibility argument as to why $S S _ { R } / \sigma ^ { 2 }$ might have a chi-square distribution with $n - 2$ degrees of freedom and be independent of A and $B$ runs as follows. Because the $Y _ { i }$ are independent normal random variables, it follows that $( Y _ { i } - E [ Y _ { i } ] ) / { \sqrt { \operatorname { V a r } ( Y _ { i } ) } } , i = 1 , \dots , n$ are independent standard normals and so 

$$
\sum_ {i = 1} ^ {n} \frac {(Y _ {i} - E [ Y _ {i} ]) ^ {2}}{\operatorname{Var} (Y _ {i})} = \sum_ {i = 1} ^ {n} \frac {(Y _ {i} - \alpha - \beta x _ {i}) ^ {2}}{\sigma^ {2}} \sim \chi_ {n} ^ {2}
$$

Now if we substitute the estimators A and B for α and $\beta _ { ; }$ , then 2 degrees of freedom are lost, and so it is not an altogether surprising result that $S S _ { R } / \sigma ^ { 2 }$ has a chi-square distribution with n − 2 degrees of freedom. 

The fact that $S S _ { R }$ is independent of A and B is quite similar to the fundamental result that in normal sampling $\overline { { X } }$ and $S ^ { 2 }$ are independent. Indeed this latter result states that if $Y _ { 1 } , \dots , Y _ { n }$ is a normal sample with population mean $\mu$ and variance $\sigma _ { 2 }$ , then if in the sum of squares $\textstyle \sum _ { i = 1 } ^ { n } ( Y _ { i } - { \bar { \mu } } ) ^ { 2 } / \sigma ^ { 2 }$ , which has a chi-square distribution with n degrees of freedom, one substitutes the estimator $\overline { { Y } }$ for $\mu$ to obtain the new sum of squares $\textstyle \sum _ { i } ( Y _ { i } - { \overline { { Y } } } ) ^ { 2 } / \sigma ^ { 2 }$ , then this quantity [equal to $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } ]$ will be independent of Y and will have a chi-square distribution with $n - 1$ degrees of freedom. Since $S S _ { R } / \sigma ^ { 2 }$ is obtained by substituting the estimators A and B for α and $\beta$ in the sum of squares $\textstyle \sum _ { i = 1 } ^ { n } ( Y _ { i } - { \dot { \alpha } } - \beta x _ { i } ) ^ { 2 } / \sigma ^ { 2 }$ , it is not unreasonable to expect that this quantity might be independent of A and B. 

When the $Y _ { i }$ are normal random variables, the least square estimators are also the maximum likelihood estimators. To verify this remark, note that the joint density of $Y _ { 1 } , \dots , Y _ { n }$ is given by 

$$
\begin{array}{l} f _ {Y _ {1}, \ldots , Y _ {n}} (y _ {1}, \ldots , y _ {n}) = \prod_ {i = 1} ^ {n} f _ {Y _ {i}} (y _ {i}) \\ \qquad = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} e ^ {- (y _ {i} - \alpha - \beta x _ {i}) ^ {2} / 2 \sigma^ {2}} \\ \qquad = \frac {1}{(2 \pi) ^ {n / 2} \sigma^ {n}} e ^ {- \sum_ {i = 1} ^ {n} (y _ {i} - \alpha - \beta x _ {i}) ^ {2} / 2 \sigma^ {2}} \end{array}
$$

Consequently, the maximum likelihood estimators of α and $\beta$ are precisely the values of α and $\beta$ that minimize $\textstyle \sum _ { i = 1 } ^ { n } ( y _ { i } - \alpha - \beta x _ { i } ) ^ { 2 }$ . That is, they are the least squares estimators. 

## Notation

If we let 

$$
S _ {x Y} = \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) (Y _ {i} - \overline {{Y}}) = \sum_ {i = 1} ^ {n} x _ {i} Y _ {i} - n \overline {{x}} \overline {{Y}}
$$

$$
S _ {x x} = \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}
$$

$$
S _ {Y Y} = \sum_ {i = 1} ^ {n} (Y _ {i} - \overline {{Y}}) ^ {2} = \sum_ {i = 1} ^ {n} Y _ {i} ^ {2} - n \overline {{Y}} ^ {2}
$$

then the least squares estimators can be expressed as 

$$
\begin{array}{l} {B = \frac {S _ {x Y}}{S _ {x x}}} \\ {A = \overline {{Y}} - B \overline {{x}}} \end{array}
$$

The following computational identity for $S S _ { R }$ , the sum of squares of the residuals, can be established. 

## Computational Identity for $\pmb { S } \pmb { S } _ { \pmb { R } }$

$$
S S _ {R} = \frac {S _ {x x} S _ {Y Y} - S _ {x Y} ^ {2}}{S _ {x x}}\tag{9.3.4}
$$

The following proposition sums up the results of this section. 

PROPOSITION 9.3.1 Suppose that the responses $Y _ { i } , i = 1 , \dots , n$ are independent normal random variables with means $\alpha + \beta x _ { i }$ and common variance $\sigma ^ { 2 }$ . The least squares estimators of $\beta$ and $\alpha$ 

$$
B = \frac {S _ {x Y}}{S _ {x x}}, \qquad A = \overline {{Y}} - B \overline {{x}}
$$

are distributed as follows: 

$$
A \sim \mathcal {N} \left(\alpha , \frac {\sigma^ {2} \sum_ {i} x _ {i} ^ {2}}{n S _ {x x}}\right)
$$

$$
B \sim \mathcal {N} (\beta , \sigma^ {2} / S _ {x x})
$$

In addition, if we let 

$$
S S _ {R} = \sum_ {i} (Y _ {i} - A - B x _ {i}) ^ {2}
$$

denote the sum of squares of the residuals, then 

$$
\frac {S S _ {R}}{\sigma^ {2}} \sim \chi_ {n - 2} ^ {2}
$$

and $S S _ { R }$ is independent of the least squares estimators A and B. Also, $S S _ { R }$ can be computed from 

$$
S S _ {R} = \frac {S _ {x x} S _ {Y Y} - (S _ {x Y}) ^ {2}}{S _ {x x}}
$$

Program 9.2 will compute the least squares estimators A and B as well as $\overline { { x } } , \sum _ { i } x _ { i } ^ { 2 }$ $S _ { x x } , S _ { x Y } , S _ { Y Y }$ , and $S S _ { R }$ 

EXAMPLE 9.3a The following data relate x, the moisture of a wet mix of a certain product, to $Y ,$ the density of the finished product. 

<table><tr><td>xi</td><td>yi</td></tr><tr><td>5</td><td>7.4</td></tr><tr><td>6</td><td>9.3</td></tr><tr><td>7</td><td>10.6</td></tr><tr><td>10</td><td>15.4</td></tr><tr><td>xi</td><td>yi</td></tr><tr><td>12</td><td>18.1</td></tr><tr><td>15</td><td>22.2</td></tr><tr><td>18</td><td>24.1</td></tr><tr><td>20</td><td>24.8</td></tr></table>

Fit a linear curve to these data. Also determine $S S _ { R }$ 

SOLUTION A plot of the data and the estimated regression line is shown in Figure 9.4. 

To solve the foregoing, run Program 9.2; results are shown in Figure 9.5. ■ 

## 9.4 STATISTICAL INFERENCES ABOUT THE REGRESSION PARAMETERS

Using Proposition 9.3.1, it is a simple matter to devise hypothesis tests and confidence intervals for the regression parameters. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/64537d2bde70b48956e3caff86054b6591c880f4b9f8c58d069f4bc9a22d7c33.jpg)



FIGURE 9.4 Example 9.3a.


## 9.4.1 Inferences Concerning $\beta$

An important hypothesis to consider regarding the simple linear regression model 

$$
Y = \alpha + \beta x + e
$$

is the hypothesis that $\beta = 0$ . Its importance derives from the fact that it is equivalent to stating that the mean response does not depend on the input, or, equivalently, that there is no regression on the input variable. To test 

$$
H _ {0}: \beta = 0 \qquad \text { versus } \qquad H _ {1}: \beta \neq 0
$$

note that, from Proposition 9.3.1, 

$$
\frac {B - \beta}{\sqrt {\sigma^ {2} / S _ {x x}}} = \sqrt {S _ {x x}} \frac {(B - \beta)}{\sigma} \sim \mathcal {N} (0, 1)\tag{9.4.1}
$$

and is independent of 

$$
\frac {S S _ {R}}{\sigma^ {2}} \sim \chi_ {n - 2} ^ {2}
$$

Hence, from the definition of a t-random variable it follows that 

$$
\frac {\sqrt {S _ {x x}} (B - \beta) / \sigma}{\sqrt {\frac {S S _ {R}}{\sigma^ {2} (n - 2)}}} = \sqrt {\frac {(n - 2) S _ {x x}}{S S _ {R}}} (B - \beta) \sim t _ {n - 2}\tag{9.4.2}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/33874bd619e20c20249ceebb4817d71e76c0cbc463310124a3fd86ef1c59585e.jpg)


```txt
The least squares estimators are as follows:
a = 2.46    Average x value = 11.63
b = 1.21    Sum of squares of the x values = 1303.0 
```


FIGURE 9.5


That is, $\sqrt { ( n - 2 ) S _ { x x } / S S _ { R } } ( B - \beta )$ has a t-distribution with n − 2 degrees of freedom. Therefore, if $H _ { 0 }$ is true (and so $\beta = 0 )$ , then 

$$
\sqrt {\frac {(n - 2) S _ {x x}}{S S _ {R}}} B \sim t _ {n - 2}
$$

which gives rise to the following test of $H _ { 0 }$ . 

## Hypothesis Test of $H _ { 0 } \colon \beta = 0$

A significance level $\gamma$ test of $H _ { 0 }$ is to 

$$
\begin{array}{l l} \text { reject } & H _ {0} \quad \text { if } \sqrt {\frac {(n - 2) S _ {x x}}{S S _ {R}}} | B | > t _ {\gamma / 2, n - 2} \\ \text { accept } & H _ {0} \quad \text { otherwise } \end{array}
$$

This test can be performed by first computing the value of the test statistic $\sqrt { ( n - 2 ) S _ { x x } / S S _ { R } } | B | -$ call its value v — and then rejecting $H _ { 0 }$ if the desired significance level is at least as large as 

$$
\begin{array}{c} p \text {-value} = P \{| T _ {n - 2} | > v \} \\ = 2 P \{T _ {n - 2} > v \} \end{array}
$$

where $T _ { n - 2 }$ is a t-random variable with $n - 2$ degrees of freedom. This latter probability can be obtained by using Program 5.8.2a. 

EXAMPLE 9.4a An individual claims that the fuel consumption of his automobile does not depend on how fast the car is driven. To test the plausibility of this hypothesis, the car was tested at various speeds between 45 and $7 0$ miles per hour. The miles per gallon attained at each of these speeds was determined, with the following data resulting: 

<table><tr><td>Speed</td><td>Miles per Gallon</td></tr><tr><td>45</td><td>24.2</td></tr><tr><td>50</td><td>25.0</td></tr><tr><td>55</td><td>23.3</td></tr><tr><td>60</td><td>22.0</td></tr><tr><td>65</td><td>21.5</td></tr><tr><td>70</td><td>20.6</td></tr><tr><td>75</td><td>19.8</td></tr></table>

Do these data refute the claim that the mileage per gallon of gas is unaffected by the speed at which the car is being driven? 

SOLUTION Suppose that a simple linear regression model 

$$
Y = \alpha + \beta x + e
$$

relates ${ \cal Y } ,$ the miles per gallon of the car, to x, the speed at which it is being driven. Now, the claim being made is that the regression coefficient $\beta$ is equal to 0. To see if the data are strong enough to refute this claim, we need to see if it leads to a rejection of the null hypothesis when testing 

$$
H _ {0}: \beta = 0 \qquad \text { versus } \qquad H _ {1}: \beta \neq 0
$$

To compute the value of the test statistic, we first compute the values of $S _ { x x } , S _ { Y Y }$ , and $S _ { x Y }$ . A hand calculation yields that 

$$
S _ {x x} = 7 0 0, \qquad S _ {Y Y} = 2 1. 7 5 7, \qquad S _ {x Y} = - 1 1 9
$$

Using Equation 9.3.4 gives 

$$
\begin{array}{c} S S _ {R} = [ S _ {x x} S _ {Y Y} - S _ {x Y} ^ {2} ] / S _ {x x} \\ = [ 7 0 0 (2 1. 7 5 7) - (1 1 9) ^ {2} ] / 7 0 0 = 1. 5 2 7 \end{array}
$$

Because 

$$
B = S _ {x Y} / S _ {x x} = - 1 1 9 / 7 0 0 = -. 1 7
$$

the value of the test statistic is 

$$
T S = \sqrt {5 (7 0 0) / 1 . 5 2 7} (. 1 7) = 8. 1 3 9
$$

Since, from Table A2 of the Appendix, $t _ { . 0 0 5 , 5 } = 4 . 0 3 2$ , it follows that the hypothesis $\beta = 0$ is rejected at the 1 percent level of significance. Thus, the claim that the mileage does not depend on the speed at which the car is driven is rejected; there is strong evidence that increased speeds lead to decreased mileages. ■ 

A confidence interval estimator for $\beta$ is easily obtained from Equation 9.4.2. Indeed, it follows from Equation 9.4.2 that for any $a , 0 < a < 1$ , 

$$
P \left\{- t _ {a / 2, n - 2} <   \sqrt {\frac {(n - 2) S _ {x x}}{S S _ {R}}} (B - \beta) <   t _ {a / 2, n - 2} \right\} = 1 - a
$$

or, equivalently, 

$$
P \left\{B - \sqrt {\frac {S S _ {R}}{(n - 2) S _ {x x}}} t _ {a / 2, n - 2} <   \beta <   B + \sqrt {\frac {S S _ {R}}{(n - 2) S _ {x x}}} t _ {a / 2, n - 2} \right\} = 1 - a
$$

which yields the following. 

Confidence Interval for $\beta$ 

1 $\mathrm { ~ i ~ } 1 0 0 ( 1 - a )$ percent confidence interval estimator of $\beta$ is 

$$
\left(B - \sqrt {\frac {S S _ {R}}{(n - 2) S _ {x x}}} t _ {a / 2, n - 2}, B + \sqrt {\frac {S S _ {R}}{(n - 2) S _ {x x}}} t _ {a / 2, n - 2}\right)
$$

## REMARK

The result that 

$$
\frac {B - \beta}{\sqrt {\sigma^ {2} / S _ {x x}}} \sim \mathcal {N} (0, 1)
$$

cannot be immediately applied to make inferences about $\beta$ since it involves the unknown parameter $\sigma ^ { 2 }$ . Instead, what we do is use the preceding statistic with $\sigma ^ { 2 }$ replaced by its estimator $S S _ { R } / ( n - 2 )$ , which has the effect of changing the distribution of the statistic from the standard normal to the t-distribution with n − 2 degrees of freedom. 

EXAMPLE 9.4b Derive a 95 percent confidence interval estimate of $\mu$ in Example 9.4a 

SOLUTION Since $t _ { . 0 2 5 , 5 } = 2 . 5 7 1$ , it follows from the computations of this example that the 95 percent confidence interval is 

$$
-. 1 7 0 \pm 2. 5 7 1 \sqrt {\frac {1 . 5 2 7}{3 5 0 0}} = -. 1 7 0 \pm . 0 5 4
$$

That is, we can be 95 percent confident that $\beta$ lies between −.224 and −.116. ■ 

## 9.4.1.1 REGRESSION TO THE MEAN

The term regression was originally employed by Francis Galton while describing the laws of inheritance. Galton believed that these laws caused population extremes to “regress toward the mean.” By this he meant that children of individuals having extreme values of a certain characteristic would tend to have less extreme values of this characteristic than their parent. 

If we assume a linear regression relationship between the characteristic of the off spring (Y ), and that of the parent (x), then a regression to the mean will occur when the regression parameter $\beta$ is between 0 and 1. That is, if 

$$
E [ Y ] = \alpha + \beta x
$$

and $0 ~ < ~ \beta ~ < ~ 1$ , then E [Y ] will be smaller than x when x is large and greater than x when x is small. That this statement is true can be easily checked either algebraically or by plotting the two straight lines 

$$
y = \alpha + \beta x
$$

and 

$$
y = x
$$

A plot indicates that, when $0 < \beta < 1$ , the line $y = \alpha + \beta x$ is above the line $y = x$ for small values of x and is below it for large values of x. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/e931253d759528a035a6cf92cd614bcf1ae83f2588b8a98689a649842404a810.jpg)



FIGURE 9.6 Scatter diagram of son’s height versus father’s height.



EXAMPLE 9.4c To illustrate Galton’s thesis of regression to the mean, the British statistician Karl Pearson plotted the heights of 10 randomly chosen sons versus that of their fathers. The resulting data (in inches) were as follows.


<table><tr><td>Fathers&#x27; height</td><td>60</td><td>62</td><td>64</td><td>65</td><td>66</td><td>67</td><td>68</td><td>70</td><td>72</td><td>74</td></tr><tr><td>Sons&#x27; height</td><td>63.6</td><td>65.2</td><td>66</td><td>65.5</td><td>66.9</td><td>67.1</td><td>67.4</td><td>68.3</td><td>70.1</td><td>70</td></tr></table>


A scatter diagram representing these data is presented in Figure 9.6. 


Note that whereas the data appear to indicate that taller fathers tend to have taller sons, it also appears to indicate that the sons of fathers that are either extremely short or extremely tall tend to be more “average” than their fathers — that is, there is a “regression toward the mean. 

We will determine whether the preceding data are strong enough to prove that there is a regression toward the mean by taking this statement as the alternative hypothesis. That is, we will use the above data to test 

$$
H _ {0}: \beta \geq 1 \quad \text { versus } \quad H _ {1}: \beta <   1
$$

which is equivalent to a test of 

$$
H _ {0}: \beta = 1 \quad \text { versus } \quad H _ {1}: \beta <   1
$$

It now follows from Equation 9.4.2 that when $\beta = 1$ , the test statistic 

$$
T S = \sqrt {8 S _ {x x} / S S _ {R}} (B - 1)
$$

has a t-distribution with 8 degrees of freedom. The significance level α test will rejec $H _ { 0 }$ when the value of TS is sufficiently small (since this will occur when $B ,$ the estimator of $\beta ,$ , is sufficiently smaller than 1). Specifically, the test is to 

$$
\mathrm{reject} H _ {0} \mathrm{if} \sqrt {8 S _ {x x} / S S _ {R}} (B - 1) <   - t _ {\alpha , 8}
$$

Program 9.2 gives that 

$$
\sqrt {8 S _ {x x} / S S _ {R}} (B - 1) = 3 0. 2 7 9 4 (. 4 6 4 6 - 1) = - 1 6. 2 1
$$

Since $t _ { . 0 1 , 8 } = 2 . 8 9 6$ , we see that 

$$
T S <   - t _ {. 0 1, 8}
$$

and so the null hypothesis that $\beta \geq 1$ is rejected at the 1 percent level of significance. In fact, the p-value is 

$$
p \text {-value} = P \{T _ {8} \leq - 1 6. 2 1 3 \} \approx 0
$$

and so the null hypothesis that $\beta \geq 1$ is rejected at almost any significance level, thus establishing a regression toward the mean (see Figure 9.7). 

A modern biological explanation for the regression to the mean phenomenon would roughly go along the lines of noting that as an offspring obtains a random selection of one-half of its parents’ genes, it follows that the offspring of, say, a very tall parent would, by chance, tend to have fewer “tall” genes than its parent. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/75561d40b456e833770f232dfdbd33585c58310658056eb3587aff8c88502d32.jpg)



FIGURE 9.7 Example 9.4c for x small, y > x. For x large, y < x.


While the most important applications of the regression to the mean phenomenon concern the relationship between the biological characteristics of an offspring and that of its parents, this phenomenon also arises in situations where we have two sets of data referring to the same variables. ■ 

EXAMPLE 9.4d The data of Table 9.1 relate the number of motor vehicle deaths occurring in 12 counties in the northwestern United States in the years 1988 and 1989. 

A glance at Figure 9.8 indicates that in 1989 there was, for the most part, a reduction in the number of deaths in those counties that had a large number of motor deaths in 1988. Similarly, there appears to have been an increase in those counties that had a low value in 1988. Thus, we would expect that a regression to the mean is in effect. In fact, running Program 9.2 yields that the estimated regression equation is 

$$
y = 7 4. 5 8 9 +. 2 7 6 x
$$

showing that the estimated value of β indeed appears to be less than 1. 

One must be careful when considering the reason behind the regression to the mean phenomenon in the preceding data. For instance, it might be natural to suppose that those counties that had a large number of deaths caused by motor vehicles in 1988 would have made a large effort — perhaps by improving the safety of their roads or by making people more aware of the potential dangers of unsafe driving — to reduce this number. In addition, we might suppose that those counties that had the fewest number of deaths in 1988 might have “rested on their laurels” and not made much of an effort to further improve their numbers — and as a result had an increase in the number of casualties the following year. 


TABLE 9.1 Motor Vehicle Deaths, Northwestern United States, 1988 and 1989


<table><tr><td>County</td><td>Deaths in 1988</td><td>Deaths in 1989</td></tr><tr><td>1</td><td>121</td><td>104</td></tr><tr><td>2</td><td>96</td><td>91</td></tr><tr><td>3</td><td>85</td><td>101</td></tr><tr><td>4</td><td>113</td><td>110</td></tr><tr><td>5</td><td>102</td><td>117</td></tr><tr><td>6</td><td>118</td><td>108</td></tr><tr><td>7</td><td>90</td><td>96</td></tr><tr><td>8</td><td>84</td><td>102</td></tr><tr><td>9</td><td>107</td><td>114</td></tr><tr><td>10</td><td>112</td><td>96</td></tr><tr><td>11</td><td>95</td><td>88</td></tr><tr><td>12</td><td>101</td><td>106</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/e9a2bf30ebedb1106cf3d0cc420bcd844beb801a7fa53899905c97a919d6e553.jpg)



FIGURE 9.8 Scatter diagram of 1989 deaths versus 1988 deaths.


While the above supposition might be correct, it is important to realize that a regression to the mean would probably have occurred even if none of the counties had done anything out of the ordinary. Indeed, it could very well be the case that those counties having large numbers of casualties in 1988 were just very unlucky in that year and thus a decrease in the next year was just a return to a more normal result for them. (For an analogy, if 9 heads results when 10 fair coins are flipped then it is quite likely that another flip of these 10 coins will result in fewer than 9 heads.) Similarly, those counties having few deaths in 1988 might have been “lucky” that year and a more normal result in 1989 would thus lead to an increase. 

The mistaken belief that regression to the mean is due to some outside influence when it is in reality just due to “chance” occurs frequently enough that it is often referred to as the regression fallacy. ■ 

## 9.4.2 Inferences Concerning <sub>α</sub>

The determination of confidence intervals and hypothesis tests for α is accomplished in exactly the same manner as was done for $\beta .$ . Specifically, Proposition 9.3.1 can be used to show that 

$$
\sqrt {\frac {n (n - 2) S _ {x x}}{\sum_ {i} x _ {i} ^ {2} S S _ {R}}} (A - \alpha) \sim t _ {n - 2}\tag{9.4.3}
$$

which leads to the following confidence interval estimator of α. 

## Confidence Interval Estimator of α

The $1 0 0 ( 1 - a )$ percent confidence interval for α is the interval 

$$
A \pm \sqrt {\frac {\sum_ {i} x _ {i} ^ {2} S S _ {R}}{n (n - 2) S _ {x x}}} t _ {a / 2, n - 2}
$$

Hypothesis tests concerning α are easily obtained from Equation 9.4.3, and their development is left as an exercise. 

## 9.4.3 Inferences Concerning the Mean Response $\alpha + \beta x _ { 0 }$

It is often of interest to use the data pairs $( x _ { i } , Y _ { i } ) , i = 1 , \ldots , n ,$ , to estimate $\alpha + \beta x _ { 0 }$ , the mean response for a given input level x<sub>0</sub>. If it is a point estimator that is desired, then the natural estimator is $A + B x _ { 0 }$ , which is an unbiased estimator since 

$$
E [ A + B x _ {0} ] = E [ A ] + x _ {0} E [ B ] = \alpha + \beta x _ {0}
$$

However, if we desire a confidence interval, or are interested in testing some hypothesi about this mean response, then it is necessary to first determine the probability distribution of the estimator $A + B _ { x _ { 0 } }$ . We now do so. 

Using the expression for B given by Equation 9.3.1 yields that 

$$
B = c \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) Y _ {i}
$$

where 

$$
c = \frac {1}{\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} = \frac {1}{S _ {x x}}
$$

Since 

$$
A = \overline {{Y}} - B \overline {{x}}
$$

we see that 

$$
\begin{array}{c} A + B x _ {0} = \frac {\sum_ {i = 1} ^ {n} Y _ {i}}{n} - B (\overline {{x}} - x _ {0}) \\ = \sum_ {i = 1} ^ {n} Y _ {i} \left[ \frac {1}{n} - c (x _ {i} - \overline {{x}}) (\overline {{x}} - x _ {0}) \right] \end{array}
$$

Since the $Y _ { i }$ are independent normal random variables, the foregoing equation shows that $A + B x _ { 0 }$ can be expressed as a linear combination of independent normal random variables and is thus itself normally distributed. Because we already know its mean, we need only compute its variance, which is accomplished as follows: 

$$
\begin{array}{r l} & {\mathrm{Var} (A + B x _ {0}) = \sum_ {i = 1} ^ {n} \left[ \frac {1}{n} - c (x _ {i} - \overline {{x}}) (\overline {{x}} - x _ {0}) \right] ^ {2} \mathrm{Var} (Y _ {i})} \\ & {\qquad = \sigma^ {2} \sum_ {i = 1} ^ {n} \left[ \frac {1}{n ^ {2}} - c ^ {2} (\overline {{x}} - x _ {0}) ^ {2} (x _ {i} - \overline {{x}}) ^ {2} - 2 c (x _ {i} - \overline {{x}}) \frac {(\overline {{x}} - x _ {0})}{n} \right]} \\ & {\qquad = \sigma^ {2} \left[ \frac {1}{n} + c ^ {2} (\overline {{x}} - x _ {0}) ^ {2} \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} - 2 c (\overline {{x}} - x _ {0}) \sum_ {i = 1} ^ {n} \frac {(x _ {i} - \overline {{x}})}{n} \right]} \\ & {\qquad = \sigma^ {2} \left[ \frac {1}{n} + \frac {(\overline {{x}} - x _ {0}) ^ {2}}{S _ {x x}} \right]} \end{array}
$$

where the last equality followed from 

$$
\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{{{x}}}}) ^ {2} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{{{x}}}} ^ {2} = 1 / c = S _ {x x}, \qquad \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{{{x}}}}) = 0
$$

Hence, we have shown that 

$$
A + B x _ {0} \sim \mathcal {N} \left(\alpha + \beta x _ {0}, \sigma^ {2} \left[ \frac {1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}} \right]\right)\tag{9.4.4}
$$

In addition, because $A + B x _ { 0 }$ is independent of 

$$
S S _ {R} / \sigma^ {2} \sim \chi_ {n - 2} ^ {2}
$$

it follows that 

$$
\frac {A + B x _ {0} - (\alpha + \beta x _ {0})}{\sqrt {\frac {1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}}} \sqrt {\frac {S S _ {R}}{n - 2}}} \sim t _ {n - 2}\tag{9.4.5}
$$

Equation 9.4.5 can now be used to obtain the following confidence interval estimator of $\alpha + \beta x _ { 0 }$ 

## Confidence Interval Estimator of $\alpha + \beta x _ { 0 }$

With $1 0 0 ( 1 - a )$ percent confidence, $\alpha + \beta x _ { 0 }$ will lie within 

$$
A + B x _ {0} \pm \sqrt {\frac {1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}}} \sqrt {\frac {S S _ {R}}{n - 2}} t _ {a / 2, n - 2}
$$

EXAMPLE 9.4e Using the data of Example $9 . 4 \mathsf { c } .$ , determine a 95 percent confidence interval for the average height of all males whose fathers are 68 inches tall. 

SOLUTION Since the observed values are 

$$
n = 1 0, \quad x _ {0} = 6 8, \quad \bar {x} = 6 6. 8, \quad S _ {x x} = 1 7 1. 6, \quad S S _ {R} = 1. 4 9 7 2 1
$$

we see that 

$$
\sqrt {\frac {1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}}} \sqrt {\frac {S S _ {R}}{n - 2}} = . 1 4 2 4 2 7 6
$$

Also, because 

$$
t _ {. 0 2 5, 8} = 2. 3 0 6, \qquad A + B x _ {0} = 6 7. 5 6 7 5 1
$$

we obtain the following 95 percent confidence interval, 

$$
\alpha + \beta x _ {0} \in (6 7. 2 3 9, 6 7. 8 9 6)
$$

## 9.4.4 Prediction Interval of a Future Response

It is often the case that it is more important to estimate the actual value of a future response rather than its mean value. For instance, if an experiment is to be performed at temperature level $x _ { 0 }$ , then we would probably be more interested in predicting $Y ( x _ { 0 } )$ , the yield from this experiment, than we would be in estimating the expected yield — $E [ Y ( x _ { 0 } ) ] = \alpha + \beta x _ { 0 }$ (On the other hand, if a series of experiments were to be performed at input level $x _ { 0 }$ , then we would probably want to estimate $\alpha + \beta x _ { 0 }$ , the mean yield.) 

Suppose first that we are interested in a single value (as opposed to an interval) to use as a predictor of $Y ( x _ { 0 } )$ , the response at level $x _ { 0 }$ . Now, it is clear that the best predictor of $Y ( x _ { 0 } )$ is its mean value $\alpha + \beta x _ { 0 }$ . [Actually, this is not so immediately obvious since one could argue that the best predictor of a random variable is (1) its mean — which minimizes the expected square of the difference between the predictor and the actual value; or (2) its median — which minimizes the expected absolute difference between the predictor and the actual value; or (3) its mode — which is the most likely value to occur. However, as the mean, median, and mode of a normal random variable are all equal — and the response is, by assumption, normally distributed — there is no doubt in this situation.] Since α and $\beta$ are not known, it seems reasonable to use their estimators A and B and thus use $A + B x _ { 0 }$ as the predictor of a new response at input level $x _ { 0 }$ 

Let us now suppose that rather than being concerned with determining a single value to predict a response, we are interested in finding a prediction interval that, with a given degree of confidence, will contain the response. To obtain such an interval, let Y denote the future response whose input level is $x _ { 0 }$ and consider the probability distribution of the response minus its predicted value — that is, the distribution of $Y - A - B x _ { 0 }$ . Now, 

$$
Y \sim \mathcal {N} (\alpha + \beta x _ {0}, \sigma^ {2})
$$

and, as was shown in Section 9.4.3, 

$$
A + B x _ {0} \sim \mathcal {N} \left(\alpha + \beta x _ {0}, \sigma^ {2} \left[ \frac {1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}} \right]\right)
$$

Hence, because Y is independent of the earlier data values $Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { n }$ that were used to determine A and $B ,$ it follows that Y is independent of $A + B x _ { 0 }$ and so 

$$
Y - A - B x _ {0} \sim \mathcal {N} \left(0, \sigma^ {2} \left[ 1 + \frac {1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}} \right]\right)
$$

or, equivalently, 

$$
\frac {Y - A - B x _ {0}}{\sigma \sqrt {\frac {n + 1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}}}} \sim \mathcal {N} (0, 1)\tag{9.4.6}
$$

Now, using once again the result that $S S _ { R }$ is independent of A and B (and also of Y ) and 

$$
\frac {S S _ {R}}{\sigma^ {2}} \sim \chi_ {n - 2} ^ {2}
$$

we obtain, by the usual argument, upon replacing $\sigma ^ { 2 }$ in Equation 9.4.6 by its estimator $S S _ { R } / ( n - 2 )$ that 

$$
\frac {Y - A - B x _ {0}}{\sqrt {\frac {n + 1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}}} \sqrt {\frac {S S _ {R}}{n - 2}}} \sim t _ {n - 2}
$$

and so, for any value $a , 0 < a < 1$ , 

$$
p \left\{- t _ {a / 2, n - 2} <   \frac {Y - A - B x _ {0}}{\sqrt {\frac {n + 1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}}} \sqrt {\frac {S S _ {R}}{n - 2}}} <   t _ {a / 2, n - 2} \right\} = 1 - a
$$

That is, we have just established the following. 

## Prediction Interval for a Response at the Input Level x

Based on the response values $Y _ { i }$ corresponding to the input values $x _ { i } , i = 1 , 2 , \ldots ,$ , n: With $1 0 0 ( 1 - a )$ percent confidence, the response $Y$ at the input level $x _ { 0 }$ will be contained in the interval 

$$
A + B x _ {0} \pm t _ {a / 2, n - 2} \sqrt {\left[ \frac {n + 1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}} \right] \frac {S S _ {R}}{n - 2}}
$$

EXAMPLE 9.4f In Example $9 . 4 \mathsf { c } ,$ suppose we want an interval that we can “be 95 percent certain” will contain the height of a given male whose father is 68 inches tall. A simple computation now yields the prediction interval 

$$
Y (6 8) \in 6 7. 5 6 8 \pm 1. 0 5 0
$$

or, with 95 percent confidence, the person’s height will be between 66.518 and 68.618. ■ 

## REMARKS

(a) There is often some confusion about the difference between a confidence and a pre diction interval. A confidence interval is an interval that does contain, with a given degree of confidence, a fixed parameter of interest. A prediction interval, on the other hand, is an interval that will contain, again with a given degree of confidence, a random variable of interest. 

(b) One should not make predictions about responses at input levels that are far from those used to obtain the estimated regression line. For instance, the data of Example 9.4c should not be used to predict the height of a male whose father is 42 inches tall. 

## 9.4.5 Summary of Distributional Results

We now summarize the distributional results of this section. 

$$
M o d e l: Y = \alpha + \beta x + e, \quad e \sim \mathcal {N} (0, \sigma^ {2})
$$

$$
D a t a: (x _ {i}, Y _ {i}), \quad i = 1, 2, \ldots , n
$$

<table><tr><td>Inferences About</td><td>Use the Distributional Result</td></tr><tr><td>$ \beta $</td><td>$ \sqrt{\frac{(n-2)S_{xx}}{SS_r}}(B-\beta)\sim t_{n-2} $</td></tr><tr><td>$ \alpha $<eq>\alpha + \beta x_0</eq></td><td>$ \sqrt{\frac{n(n-2)S_{xx}}{\sum_i x_i^2 SS_R}}(A-\alpha)\sim t_{n-2} $<eq>\frac{A + Bx_0 - \alpha - \beta x_0}{\sqrt{\left(\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right)\left(\frac{SS_R}{n-2}\right)}} \sim t_{n-2}</eq></td></tr><tr><td><eq>Y(x_0)</eq></td><td><eq>\frac{Y(x_0) - A - Bx_0}{\sqrt{\left(1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right)\left(\frac{SS_R}{n-2}\right)}} \sim t_{n-2}</eq></td></tr></table>

## 9.5 THE COEFFICIENT OF DETERMINATION AND THE SAMPLE CORRELATION COEFFICIENT

Suppose we wanted to measure the amount of variation in the set of response values $Y _ { 1 } , \dots , Y _ { n }$ corresponding to the set of input values $x _ { 1 } , \ldots , x _ { n }$ . A standard measure in statistics of the amount of variation in a set of values $Y _ { 1 } , \dots , Y _ { n }$ is given by the quantity 

$$
S _ {Y Y} = \sum_ {i = 1} ^ {n} (Y _ {i} - \overline {{Y}}) ^ {2}
$$

For instance, if all the $Y _ { i }$ are equal — and thus are all equal to $\overline { r } -$ then $S _ { Y Y }$ would equal 0. 

The variation in the values of the $Y _ { i }$ arises from two factors. First, because the input values $x _ { i }$ are different, the response variables $Y _ { i }$ all have different mean values, which will result in some variation in their values. Second, the variation also arises from the fact that even when the differences in the input values are taken into account, each of the response variables $Y _ { i }$ has variance $\sigma ^ { 2 }$ and thus will not exactly equal the predicted value at its input $x _ { i }$ . 

Let us consider now the question as to how much of the variation in the values of the response variables is due to the different input values, and how much is due to the inherent variance of the responses even when the input values are taken into account. To answer this question, note that the quantity 

$$
S S _ {R} = \sum_ {i = 1} ^ {n} (Y _ {i} - A - B x _ {i}) ^ {2}
$$

measures the remaining amount of variation in the response values after the different input values have been taken into account. Thus, 

$$
S _ {Y Y} - S S _ {R}
$$

represents the amount of variation in the response variables that is explained by the different input values; and so the quantity $R ^ { 2 }$ defined by 

$$
\begin{array}{r} R ^ {2} = \frac {S _ {Y Y} - S S _ {R}}{S _ {Y Y}} \\ = 1 - \frac {S S _ {R}}{S _ {Y Y}} \end{array}
$$

represents the proportion of the variation in the response variables that is explained by the different input values. $R ^ { 2 }$ is called the coefficient of determination. 

The coefficient of determination $R ^ { 2 }$ will have a value between 0 and 1. A value of $R ^ { 2 }$ near 1 indicates that most of the variation of the response data is explained by the different input values, whereas a value of $R ^ { 2 }$ near 0 indicates that little of the variation is explained by the different input values. 

EXAMPLE 9.5a In Example 9.4c, which relates the height of a son to that of his father, the output from Program 9.2 yielded that 

$$
S _ {Y Y} = 3 8. 5 2 1, \qquad S S _ {R} = 1. 4 9 7
$$

Thus, 

$$
R ^ {2} = 1 - \frac {1 . 4 9 7}{3 8 . 5 3 1} = . 9 6 1
$$

In other words, 96 percent of the variation of the heights of the 10 individuals is explained by the heights of their fathers. The remaining (unexplained) 4 percent of the variation is due to the variance of a son’s height even when the father’s height is taken into account. (That is, it is due to $\sigma ^ { 2 }$ , the variance of the error random variable.) ■ 

The value of $R ^ { 2 }$ is often used as an indicator of how well the regression model fits the data, with a value near 1 indicating a good fit, and one near 0 indicating a poor fit. In other words, if the regression model is able to explain most of the variation in the response data, then it is considered to fit the data well. 

Recall that in Section 2.6 we defined the sample correlation coefficient r of the set of data pairs $( x _ { i } , Y _ { i } ) , i = 1 , \ldots , n ,$ , by 

$$
r = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) (Y _ {i} - \overline {{Y}})}{\sqrt {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} \sum_ {i = 1} ^ {n} (Y _ {i} - \overline {{Y}}) ^ {2}}}
$$

It was noted that r provided a measure of the degree to which high values of x are paired with high values of Y and low values of x with low values of Y . A value of r near +1 indicated that large x values were strongly associated with large Y values and small x values were strongly associated with small Y values, whereas a value near −1 indicated that large x values were strongly associated with small Y values and small x values with large Y values. 

In the notation of this chapter, 

$$
r = \frac {S _ {x Y}}{\sqrt {S _ {x x} S _ {Y Y}}}
$$

Upon using identity (9.3.4): 

$$
S S _ {R} = \frac {S _ {x x} S _ {Y Y} - S _ {x Y} ^ {2}}{S _ {x x}}
$$

we see that 

$$
\begin{array}{r l} r ^ {2} & = \frac {S _ {x Y} ^ {2}}{S _ {x x} S _ {Y Y}} \\ & = \frac {S _ {x x} S _ {Y Y} - S S _ {R} S _ {x x}}{S _ {x x} S _ {Y Y}} \\ & = 1 - \frac {S S _ {R}}{S _ {Y Y}} \\ & = R ^ {2} \end{array}
$$

That is, 

$$
| r | = \sqrt {R ^ {2}}
$$

and so, except for its sign indicating whether it is positive or negative, the sample correlation coefficient is equal to the square root of the coefficient of determination. The sign of r is the same as that of B. 

The above gives additional meaning to the sample correlation coefficient. For instance, if a data set has its sample correlation coefficient r equal to .9, then this implies that a simple linear regression model for these data explains 81 percent (since $R ^ { 2 } = \overset { \vartriangle } { \cdot } \mathbf { 9 } ^ { 2 } = . 8 1 )$ of the variation in the response values. That is, 81 percent of the variation in the response values is explained by the different input values. 

## 9.6 ANALYSIS OF RESIDUALS: ASSESSING THE MODEL

The initial step for ascertaining whether or not the simple linear regression model 

$$
Y = \alpha + \beta x + e, \qquad e \sim \mathcal {N} (0, \sigma^ {2})
$$

(a) 

is appropriate in a given situation is to investigate the scatter diagram. Indeed, this is often sufficient to convince one that the regression model is or is not correct. When the scatter diagram does not by itself rule out the preceding model, then the least square estimators A and B should be computed and the residual $Y _ { i } - ( A + B x _ { i } ) , i = 1 , \dots , n$ analyzed. The analysis begins by normalizing, or standardizing, the residuals by dividing them by $\sqrt { S S _ { R } / ( n - 2 ) }$ ), the estimate of the standard deviation of the $Y _ { i }$ . The resulting quantities 

$$
\frac {Y _ {i} - (A + B x _ {i})}{\sqrt {S S _ {R} / (n - 2)}}, \qquad i = 1, \ldots , n
$$

are called the standardized residuals. 

When the simple linear regression model is correct, the standardized residuals are approximately independent standard normal random variables, and thus should be randomly distributed about 0 with about 95 percent of their values being between −2 and +2 (since $P \{ - 1 . 9 6 < Z < 1 . 9 6 \} = . 9 5 )$ . In addition, a plot of the standardized residual should not indicate any distinct pattern. Indeed, any indication of a distinct pattern should make one suspicious about the validity of the assumed simple linear regression model. 

Figure 9.9 presents three different scatter diagrams and their associated standardized residuals. The first of these, as indicated both by its scatter diagram and the random nature of its standardized residuals, appears to fit the straight-line model quite well. The second 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/bf9520bebd46c346677cbbb6181e9430d4a0df0b170d506483ee0459b8e777d3.jpg)



FIGURE 9.9


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/54521ae65b28e38d30957eb993beadec766402aa0648354e8d9042ea5fa8934f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/a0da45851fc9dca2c173348b43c9ce0048700550adf4bd55fc69c6436da086bb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/559400176ccd1cc5489672346753f0ac36c2e89fa263fc15837517973ac4d718.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/1fb362eb4719f69500345ee328d4bc3f00fd84e3e9f181a0a5184dd133d79d76.jpg)



FIGURE 9.9 (continued )


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/7852b9fe14767dabfef9842ce6f401fcc39104cd4bd447257b6f24ed7ddddde6.jpg)


residual plot shows a discernible pattern, in that the residuals appear to be first decreasing and then increasing as the input level increases. This often means that higher-order (than just linear) terms are needed to describe the relationship between the input and response. Indeed, this is also indicated by the scatter diagram in this case. The third standardized residual plot also shows a pattern, in that the absolute value of the residuals, and thus their squares, appear to be increasing, as the input level increases. This often indicates that the variance of the response is not constant but, rather, increases with the input level. 

## 9.7 TRANSFORMING TO LINEARITY

In many situations, it is clear that the mean response is not a linear function of the input level. In such cases, if the form of the relationship can be determined it is sometime possible, by a change of variables, to transform it into a linear form. For instance, in certain applications it is known that $W ( t )$ , the amplitude of a signal a time t after its origination, is approximately related to t by the functional form 

$$
W (t) \approx c e ^ {- d t}
$$

On taking logarithms, this can be expressed as 

$$
\log W (t) \approx \log c - d t
$$

If we now let 

$$
\begin{array}{l} {Y = \log W (t)} \\ {\alpha = \log c} \\ {\beta = - d} \end{array}
$$

then the foregoing can be modeled as a regression of the form 

$$
Y = \alpha + \beta t + e
$$

The regression parameters α and $\beta$ would then be estimated by the usual least squares approach and the original functional relationships can be predicted from 

$$
W (t) \approx e ^ {A + B t}
$$


EXAMPLE 9.7a The following table gives the percentages of a chemical that were used up when an experiment was run at various temperatures (in degrees celsius). Use it to estimate the percentage of the chemical that would be used up if the experiment were to be run at 350 degrees.


<table><tr><td>Temperature</td><td>Percentage</td></tr><tr><td><eq>5^{\circ}</eq></td><td>.061</td></tr><tr><td><eq>10^{\circ}</eq></td><td>.113</td></tr><tr><td><eq>20^{\circ}</eq></td><td>.192</td></tr><tr><td><eq>30^{\circ}</eq></td><td>.259</td></tr><tr><td><eq>40^{\circ}</eq></td><td>.339</td></tr><tr><td><eq>50^{\circ}</eq></td><td>.401</td></tr><tr><td><eq>60^{\circ}</eq></td><td>.461</td></tr><tr><td><eq>80^{\circ}</eq></td><td>.551</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/65aaa1a8f1b4bc53b26da47ca2112c3eb96f245d79bea558d584bd00081f5e77.jpg)



FIGURE 9.10 Example 9.7a.


SOLUTION Let $P ( x )$ be the percentage of the chemical that is used up when the experiment is run at 10x degrees. Even though a plot of $P ( x )$ looks roughly linear (see Figure 9.10), we can improve upon the fit by considering a nonlinear relationship between x and $P ( x )$ Specifically, let us consider a relationship of the form 

$$
1 - P (x) \approx c (1 - d) ^ {x}
$$

That is, let us suppose that the percentage of the chemical that survives an experiment run at temperature x approximately decreases at an exponential rate when x increases. Taking logs, the preceding can be written as 

$$
\log (1 - P (x)) \approx \log (c) + x \log (1 - d)
$$

Thus, setting 

$$
\begin{array}{l} {Y = - \log (1 - P)} \\ {\alpha = - \log c} \\ {\beta = - \log (1 - d)} \end{array}
$$

we obtain the usual regression equation 

$$
Y = \alpha + \beta x + e
$$


TABLE 9.2


<table><tr><td>Temperature</td><td><eq>-\log(1 - P)</eq></td></tr><tr><td><eq>5^{\circ}</eq></td><td>.063</td></tr><tr><td><eq>10^{\circ}</eq></td><td>.120</td></tr><tr><td><eq>20^{\circ}</eq></td><td>.213</td></tr><tr><td><eq>30^{\circ}</eq></td><td>.300</td></tr><tr><td><eq>40^{\circ}</eq></td><td>.414</td></tr><tr><td><eq>50^{\circ}</eq></td><td>.512</td></tr><tr><td><eq>60^{\circ}</eq></td><td>.618</td></tr><tr><td><eq>80^{\circ}</eq></td><td>.801</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/4038217c7cc71fa1e65bb78406bb4d3f82a74584220213f7dbd9f2e93b5517c8.jpg)



FIGURE 9.11


To see whether the data support this model, we can plot $- \mathrm { l o g } ( 1 - P )$ versus x. The transformed data are presented in Table 9.2 and the graph in Figure 9.11. 

Running Program 9.2 yields that the least square estimates of α and $\beta$ are 

$$
A = . 0 1 5 4
$$

$$
B = . 0 0 9 9
$$


TABLE 9.3


<table><tr><td>x</td><td>P</td><td><eq>\hat{P}</eq></td><td><eq>P - \hat{P}</eq></td></tr><tr><td>5</td><td>.061</td><td>.063</td><td>-.002</td></tr><tr><td>10</td><td>.113</td><td>.109</td><td>.040</td></tr><tr><td>20</td><td>.192</td><td>.193</td><td>-.001</td></tr><tr><td>30</td><td>.259</td><td>.269</td><td>-.010</td></tr><tr><td>40</td><td>.339</td><td>.339</td><td>.000</td></tr><tr><td>50</td><td>.401</td><td>.401</td><td>.000</td></tr><tr><td>60</td><td>.461</td><td>.458</td><td>.003</td></tr><tr><td>80</td><td>.551</td><td>.556</td><td>-.005</td></tr></table>

Transforming this back into the original variable gives that the estimates of c and d are 

$$
\hat {c} = e ^ {- A} = . 9 8 4 7
$$

$$
1 - \hat {d} = e ^ {- B} = . 9 9 0 1
$$

and so the estimated functional relationship is 

$$
\hat {P} = 1 -. 9 8 4 7 (. 9 9 0 1) ^ {x}
$$

The residuals $P - \hat { P }$ are presented in Table 9.3. ■ 

## 9.8 WEIGHTED LEAST SQUARES

In the regression model 

$$
Y = \alpha + \beta x + e
$$

it often turns out that the variance of a response is not constant but rather depends on it input level. If these variances are known — at least up to a proportionality constant — then the regression parameters α and $\beta$ should be estimated by minimizing a weighted sum of squares. Specifically, if 

$$
\mathrm{Var} (Y _ {i}) = \frac {\sigma^ {2}}{w _ {i}}
$$

then the estimators A and B should be chosen to minimize 

$$
\sum_ {i} \frac {[ Y _ {i} - (A + B x _ {i}) ] ^ {2}}{\mathrm{Var} (Y _ {i})} = \frac {1}{\sigma^ {2}} \sum_ {i} w _ {i} (Y _ {i} - A - B x _ {i}) ^ {2}
$$

On taking partial derivatives with respect to $A$ and B and setting them equal to 0, we obtain the following equations for the minimizing A and $B .$ 

$$
\begin{array}{c} {\sum_ {i} w _ {i} Y _ {i} = A \sum_ {i} w _ {i} + B \sum_ {i} w _ {i} x _ {i}} \\ {\sum_ {i} w _ {i} x _ {i} Y _ {i} = A \sum_ {i} w _ {i} x _ {i} + B \sum_ {i} w _ {i} x _ {i} ^ {2}} \end{array}\tag{9.8.1}
$$

These equations are easily solved to yield the least squares estimators. 

EXAMPLE 9.8a To develop a feel as to why the estimators should be obtained by mini mizing the weighted sum of squares rather than the ordinary sum of squares, consider the following situation. Suppose that $X _ { 1 } , \ldots , X _ { n }$ are independent normal random vari ables each having mean $\mu$ and variance $\sigma ^ { 2 }$ . Suppose further that the $X _ { i }$ are not directly observable but rather only $Y _ { 1 }$ and $Y _ { 2 }$ , defined by 

$$
Y _ {1} = X _ {1} + \dots + X _ {k}, \qquad Y _ {2} = X _ {k + 1} + \dots + X _ {n}, \qquad k <   n
$$

are directly observable. Based on $Y _ { 1 }$ and $Y _ { 2 } ,$ , how should we estimate $\mu     \vdots$ 

Whereas the best estimator of $\mu$ is clearly $\begin{array} { r } { \overline { { X } } = \sum _ { i = 1 } ^ { n } X _ { i } / n = ( Y _ { 1 } + Y _ { 2 } ) / n } \end{array}$ , let us see what the ordinary least squares estimator would be. Since 

$$
E [ Y _ {1} ] = k \mu , \qquad E [ Y _ {2} ] = (n - k) \mu
$$

the least squares estimator of $\mu$ would be that value of $\mu$ that minimize 

$$
(Y _ {1} - k \mu) ^ {2} + (Y _ {2} - [ n - k ] \mu) ^ {2}
$$

$\mathrm { O n }$ differentiating and setting equal to zero, we see that the least squares estimator of µ — call it $\hat { \mu }$ — is such that 

$$
- 2 k (Y _ {1} - k \hat {\mu}) - 2 (n - k) [ Y _ {2} - (n - k) \hat {\mu} ] = 0
$$

or 

$$
[ k ^ {2} + (n - k) ^ {2} ] \hat {\mu} = k Y _ {1} + (n - k) Y _ {2}
$$

or 

$$
\hat {\mu} = \frac {k Y _ {1} + (n - k) Y _ {2}}{k ^ {2} + (n - k) ^ {2}}
$$

Thus we see that while the ordinary least squares estimator is an unbiased estimator of µ — since 

$$
E [ \hat {\mu} ] = \frac {k E [ Y _ {1} ] + (n - k) E [ Y _ {2} ]}{k ^ {2} + (n - k) ^ {2}} = \frac {k ^ {2} \mu + (n - k) ^ {2} \mu}{k ^ {2} + (n - k) ^ {2}} = \mu
$$

it is not the best estimator $\overline { { X } }$ 

Now let us determine the estimator produced by minimizing the weighted sum of squares. That is, let us determine the value of $\mu -$ call it $\mu _ { w }$ — that minimizes 

$$
\frac {(Y _ {1} - k \mu) ^ {2}}{\operatorname{Var} (Y _ {1})} + \frac {[ Y _ {2} - (n - k) \mu ] ^ {2}}{\operatorname{Var} (Y _ {2})}
$$

Since 

$$
\operatorname{Var} (Y _ {1}) = k \sigma^ {2}, \qquad \operatorname{Var} (Y _ {2}) = (n - k) \sigma^ {2}
$$

this is equivalent to choosing µ to minimize 

$$
\frac {(Y _ {1} - k \mu) ^ {2}}{k} + \frac {[ Y _ {2} - (n - k) \mu ] ^ {2}}{n - k}
$$

Upon differentiating and then equating to 0, we see that $\mu _ { w } .$ , the minimizing value, satisfies 

$$
\frac {- 2 k (Y _ {1} - k \mu_ {w})}{k} - \frac {2 (n - k) [ Y _ {2} - (n - k) \mu_ {w} ]}{n - k} = 0
$$

or 

$$
Y _ {1} + Y _ {2} = n \mu_ {w}
$$

or 

$$
\mu_ {w} = \frac {Y _ {1} + Y _ {2}}{n}
$$

That is, the weighted least squares estimator is indeed the preferred estimator $( Y _ { 1 } + Y _ { 2 } ) / n = \overline { { X } }$ ■ 

## REMARKS

(a) Assuming normally distributed data, the weighted least squares estimators are precisely the maximum likelihood estimators. This follows because the joint density of the data $Y _ { 1 } , \dots , Y _ { n }$ is 

$$
\begin{array}{c} f _ {Y _ {1}, \ldots , Y _ {n}} (y _ {1}, \ldots , y _ {n}) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} (\sigma / \sqrt {w _ {i}})} e ^ {- (y _ {i} - \alpha - \beta x _ {i}) ^ {2} / (2 \sigma^ {2} / w _ {i})} \\ = \frac {\sqrt {w _ {1} \ldots w _ {n}}}{(2 \pi) ^ {n / 2} \sigma^ {n}} e ^ {- \sum_ {i = 1} ^ {n} w _ {i} (y _ {i} - \alpha - \beta x _ {i}) ^ {2} / 2 \sigma^ {2}} \end{array}
$$

Consequently, the maximum likelihood estimators of α and $\beta$ are precisely the values of α and $\beta$ that minimize the weighted sum of squares $\textstyle \sum _ { i = 1 } ^ { n } w _ { i } ( y _ { i } - \alpha - \beta x _ { i } ) ^ { 2 }$ 

(b) The weighted sum of squares can also be seen as the relevant quantity to be minimized by multiplying the regression equation 

$$
Y = \alpha + \beta x + e
$$

by ${ \sqrt { u } } .$ . This results in the equation 

$$
Y \sqrt {w} = \alpha \sqrt {w} + \beta x \sqrt {w} + e \sqrt {w}
$$

Now, in this latter equation the error term $e \sqrt { w }$ has mean 0 and constant variance. Hence, the natural least squares estimators of α and $\beta$ would be the values of A and B tha minimize 

$$
\sum_ {i} (Y _ {i} \sqrt {w _ {i}} - A \sqrt {w _ {i}} - B x _ {i} \sqrt {w _ {i}}) ^ {2} = \sum_ {i} w _ {i} (Y _ {i} - A - B x _ {i}) ^ {2}
$$

(c) The weighted least squares approach puts the greatest emphasis on those data pairs having the greatest weights (and thus the smallest variance in their error term). ■ 

At this point it might appear that the weighted least squares approach is not particularly useful since it requires a knowledge, up to a constant, of the variance of a response at an arbitrary input level. However, by analyzing the model that generates the data, it is often possible to determine these values. This will be indicated by the following two examples. 


EXAMPLE 9.8b The following data represent travel times in a downtown area of a certain city. The independent, or input, variable is the distance to be traveled.


<table><tr><td>Distance (miles)</td><td>.5</td><td>1</td><td>1.5</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>8</td><td>10</td></tr><tr><td>Travel time (minutes)</td><td>15.0</td><td>15.1</td><td>16.5</td><td>19.9</td><td>27.7</td><td>29.7</td><td>26.7</td><td>35.9</td><td>42</td><td>49.4</td></tr></table>

Assuming a linear relationship of the form 

$$
Y = \alpha + \beta x + e
$$

between Y , the travel time, and x, the distance, how should we estimate α and $\beta \ ?$ To utilize the weighted least squares approach we need to know, up to a multiplicative constant, the variance of Y as a function of x. We will now present an argument that $\mathrm { V a r } ( Y )$ should be proportional to x. 

SOLUTION Let d denote the length of a city block. Thus a trip of distance x will consist of x/d blocks. If we let $Y _ { i } , i = 1 , \dots , x / d$ , denote the time it takes to traverse block i, then the total travel time can be expressed as 

$$
Y = Y _ {1} + Y _ {2} + \dots + Y _ {x / d}
$$

Now in many applications it is probably reasonable to suppose that the $Y _ { i }$ are independent random variables with a common variance, and thus, 

$$
\begin{array}{r l} \operatorname{Var} (Y) & = \operatorname{Var} (Y _ {1}) + \dots + \operatorname{Var} (Y _ {x / d}) \\ & = (x / d) \operatorname{Var} (Y _ {1}) \qquad \text { since } \operatorname{Var} (Y _ {i}) = \operatorname{Var} (Y _ {1}) \\ & = x \sigma^ {2}, \qquad \text { where } \sigma^ {2} = \operatorname{Var} (Y _ {1}) / d \end{array}
$$

Thus, it would seem that the estimators A and B should be chosen so as to minimize 

$$
\sum_ {i} \frac {(Y _ {i} - A - B x _ {i}) ^ {2}}{x _ {i}}
$$

Using the preceding data with the weights $w _ { i } = 1 / x _ { i }$ , the least squares Equations 9.8.1 are 

$$
1 0 4. 2 2 = 5. 3 4 A + 1 0 B
$$

$$
2 7 7. 9 = 1 0 A + 4 1 B
$$

which yield the solution 

$$
A = 1 2. 5 6 1, \qquad B = 3. 7 1 4
$$

A graph of the estimated regression line $1 2 . 5 6 1 + 3 . 7 1 4 x$ along with the data points is presented in Figure 9.12. As a qualitative check of our solution, note that the regression line fits the data pairs best when the input levels are small, which is as it should be since the weights are inversely proportional to the inputs. ■ 

EXAMPLE 9.8c Consider the relationship between ${ \cal Y } ,$ , the number of accidents on a heavily traveled highway, and x, the number of cars traveling on the highway. After a little thought it would probably seem to most that the linear model 

$$
Y = \alpha + \beta x + e
$$

would be appropriate. However, as there does not appear to be any a priori reason why $\mathrm { V a r } ( Y )$ should not depend on the input level x, it is not clear that we would be justified in using the ordinary least squares approach to estimate $\alpha$ and $\beta .$ . Indeed, we will now argue that a weighted least squares approach with weights 1/x should be employed — that is, we should choose A and $B$ to minimize 

$$
\sum_ {i} \frac {(Y _ {i} - A - B x _ {i}) ^ {2}}{x _ {i}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/99c14744dedeba7ac14a848d892663bf8736bd2fd5e8ed91276abcb46052e8f0.jpg)



FIGURE 9.12 Example 9.8b.


The rationale behind this claim is that it seems reasonable to suppose that Y has approximately a Poisson distribution. This is so since we can imagine that each of the x cars will have a small probability of causing an accident and so, for large x, the number of accidents should be approximately a Poisson random variable. Since the variance of a Poisson random variable is equal to its mean, we see that 

$$
\begin{array}{l} \operatorname{Var} (Y) \simeq E [ Y ] \quad \text { since } Y \text { is   approximately   Poisson } \\ \quad = \alpha + \beta x \\ \quad \simeq \beta x \quad \text { for   large } x \quad \blacksquare \end{array}
$$

## REMARKS

(a) Another technique that is often employed when the variance of the response depends on the input level is to attempt to stabilize the variance by an appropriate transformation. For example, if Y is a Poisson random variable with mean λ, then it can be shown [see Remark (b)] that $\sqrt { Y }$ has approximate variance .25 no matter what the value of λ. Based on this fact, one might try to model $E [ { \sqrt { Y } } ]$ as a linear function of the input. That is, one might consider the model 

$$
\sqrt {Y} = \alpha + \beta x + e
$$

(b) Proof that $\mathrm { V a r } \sqrt { Y } \approx$ .25 when Y is Poisson with mean λ. Consider the Taylor series expansion of $g ( y ) = \sqrt { y }$ about the value λ. By ignoring all terms beyond the second derivative term, we obtain that 

$$
g (y) \approx g (\lambda) + g ^ {\prime} (\lambda) (y - \lambda) + \frac {g ^ {\prime \prime} (\lambda) (y - \lambda) ^ {2}}{2}\tag{9.8.2}
$$

Since 

$$
g ^ {\prime} (\lambda) = \frac {1}{2} \lambda^ {- 1 / 2}, \qquad g ^ {\prime \prime} (\lambda) = - \frac {1}{4} \lambda^ {- 3 / 2}
$$

we obtain, on evaluating Equation 9.8.2 at $y = Y$ , that 

$$
\sqrt {Y} \approx \sqrt {\lambda} + \frac {1}{2} \lambda^ {- 1 / 2} (Y - \lambda) - \frac {1}{8} \lambda^ {- 3 / 2} (Y - \lambda) ^ {2}
$$

Taking expectations, and using the results that 

$$
E [ Y - \lambda ] = 0, E [ (Y - \lambda) ^ {2} ] = \mathrm{Var} (Y) = \lambda
$$

yields that 

$$
E [ \sqrt {Y} ] \approx \sqrt {\lambda} - \frac {1}{8 \sqrt {\lambda}}
$$

Hence 

$$
\begin{array}{r} (E [ \sqrt {Y} ]) ^ {2} \approx \lambda + \frac {1}{6 4 \lambda} - \frac {1}{4} \\ \approx \lambda - \frac {1}{4} \end{array}
$$

and so 

$$
\begin{array}{c} \operatorname{Var} (\sqrt {Y}) = E [ Y ] - (E [ \sqrt {Y} ]) ^ {2} \\ \approx \lambda - \left(\lambda - \frac {1}{4}\right) \\ = \frac {1}{4} \end{array}
$$

## 9.9 POLYNOMIAL REGRESSION

In situations where the functional relationship between the response Y and the independent variable x cannot be adequately approximated by a linear relationship, it is sometimes possible to obtain a reasonable fit by considering a polynomial relationship. That is, we might try to fit to the data set a functional relationship of the form 

$$
Y = \beta_ {0} + \beta_ {1} x + \beta_ {2} x ^ {2} + \dots + \beta_ {r} x ^ {r} + e
$$

where $\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { r }$ are regression coefficients that would have to be estimated. If the data set consists of the n pairs $( x _ { i } , Y _ { i } ) , i = 1 , \ldots , n .$ , then the least square estimators of $\beta _ { 0 } , \ldots , \beta _ { r }$ — call them $B _ { 0 } , \ldots , B _ { r } -$ are those values that minimize 

$$
\sum_ {i = 1} ^ {n} (Y _ {i} - B _ {0} - B _ {1} x _ {i} - B _ {2} x _ {i} ^ {2} - \dots - B _ {r} x _ {i} ^ {r}) ^ {2}
$$

To determine these estimators, we take partial derivatives with respect to $B _ { 0 } \ldots B _ { r }$ of the foregoing sum of squares, and then set these equal to 0 so as to determine the minimizing values. On doing so, and then rearranging the resulting equations, we obtain that the least square estimators $B _ { 0 } , B _ { 1 } , \ldots , B _ { r }$ satisfy the following set of $r + 1$ linear equations called the normal equations. 

$$
\sum_ {i = 1} ^ {n} Y _ {i} = B _ {0} n + B _ {1} \sum_ {i = 1} ^ {n} x _ {i} + B _ {2} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} + \dots + B _ {r} \sum_ {i = 1} ^ {n} x _ {i} ^ {r}
$$

$$
\sum_ {i = 1} ^ {n} x _ {i} Y _ {i} = B _ {0} \sum_ {i = 1} ^ {n} x _ {i} + B _ {1} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} + B _ {2} \sum_ {i = 1} ^ {n} x _ {i} ^ {3} + \dots + B _ {r} \sum_ {i = 1} ^ {n} x _ {i} ^ {r + 1}
$$

$$
\sum_ {i = 1} ^ {n} x _ {i} ^ {2} Y _ {i} = B _ {0} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} + B _ {1} \sum_ {i = 1} ^ {n} x _ {i} ^ {3} + \dots + B _ {r} \sum_ {i = 1} ^ {n} x _ {i} ^ {r + 2}
$$

$$
\sum_ {i = 1} ^ {n} x _ {i} ^ {r} Y _ {i} = B _ {0} \sum_ {i = 1} ^ {n} x _ {i} ^ {r} + B _ {1} \sum_ {i = 1} ^ {n} x _ {i} ^ {r + 1} + \dots + B _ {r} \sum_ {i = 1} ^ {n} x _ {i} ^ {2 r}
$$

In fitting a polynomial to a set of data pairs, it is often possible to determine the necessary degree of the polynomial by a study of the scatter diagram. We emphasize that one should always use the lowest possible degree that appears to adequately describe the data. [Thus, for instance, whereas it is usually possible to find a polynomial of degree n that passes through all the n pairs $( x _ { i } , Y _ { i } ) , i = 1 , \ldots , n .$ , it would be hard to ascribe much confidence to such a fit.] 

Even more so than in linear regression, it is extremely risky to use a polynomial fit to predict the value of a response at an input level $x _ { 0 }$ that is far away from the input levels $x _ { i } , i = 1 , \dotsc , n$ used in finding the polynomial fit. (For one thing, the polynomial fit may be valid only in a region around the $x _ { i } , i = 1 , \dotsc , n$ and not including x<sub>0</sub>.) 


EXAMPLE 9.9a Fit a polynomial to the following data.


<table><tr><td>x</td><td>Y</td></tr><tr><td>1</td><td>20.6</td></tr><tr><td>2</td><td>30.8</td></tr><tr><td>3</td><td>55</td></tr><tr><td>4</td><td>71.4</td></tr><tr><td>5</td><td>97.3</td></tr><tr><td>6</td><td>131.8</td></tr><tr><td>7</td><td>156.3</td></tr><tr><td>8</td><td>197.3</td></tr><tr><td>9</td><td>238.7</td></tr><tr><td>10</td><td>291.7</td></tr></table>

SOLUTION A plot of these data (see Figure 9.13) indicates that a quadratic relationship 

$$
Y = \beta_ {0} + \beta_ {1} x + \beta_ {2} x ^ {2} + e
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/ef2c526c5b62e013b08e1806e4e1330d38c7738b033b866272137cdba950c03c.jpg)


might hold. Since 

$$
\begin{array}{l} \sum_ {i} x _ {i} = 5 5, \quad \sum_ {i} x _ {i} ^ {2} = 3 8 5, \quad \sum_ {i} x _ {i} ^ {3} = 3, 0 2 5, \quad \sum_ {i} x _ {i} ^ {4} = 2 5, 3 3 3 \\ \sum_ {i} Y _ {i} = 1, 2 9 1. 1, \quad \sum_ {i} x _ {i} Y _ {i} = 9, 5 4 9. 3, \quad \sum_ {i} x _ {i} ^ {2} Y _ {i} = 7 7, 7 5 8. 9 \end{array}
$$

the least squares estimates are the solution of the following set of equations. 

$$
\begin{array}{l} 1, 2 9 1. 1 = 1 0 B _ {0} + 5 5 B _ {1} + 3 8 5 B _ {2} \\ 9, 5 4 9. 3 = 5 5 B _ {0} + 3 8 5 B _ {1} + 3, 0 2 5 B _ {2} \\ 7 7, 7 5 8. 9 = 3 8 5 B _ {0} + 3, 0 2 5 B _ {1} + 2 5, 3 3 3 B _ {2} \end{array}\tag{9.9.1}
$$

Solving these equations (see the remark following this example) yields that the least squares estimates are 

$$
B _ {0} = 1 2. 5 9 3 2 6, \quad B _ {1} = 6. 3 2 6 1 7 2, \quad B _ {2} = 2. 1 2 2 8 1 8
$$

Thus, the estimated quadratic regression equation is 

$$
Y = 1 2. 5 9 + 6. 3 3 x + 2. 1 2 x ^ {2}
$$

This equation, along with the data, is plotted in Figure 9.14. ■ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/43c0c0893ce9b911b3c39fd79175361ba6b2e1b542a357db5c9be3939aa1a522.jpg)



FIGURE 9.14


REMARK 

In matrix notation Equation 9.9.1 can be written as 

$$
\left[ \begin{array}{c} 1, 2 9 1. 1 \\ 9, 5 4 9. 3 \\ 7 7, 7 5 8. 9 \end{array} \right] = \left[ \begin{array}{c c c} 1 0 & 5 5 & 3 8 5 \\ 5 5 & 3 8 5 & 3, 0 2 5 \\ 3 8 5 & 3, 0 2 5 & 2 5, 3 3 3 \end{array} \right] \left[ \begin{array}{c} B _ {0} \\ B _ {1} \\ B _ {2} \end{array} \right]
$$

which has the solution 

$$
\left[ \begin{array}{c} B _ {0} \\ B _ {1} \\ B _ {2} \end{array} \right] = \left[ \begin{array}{c c c} 1 0 & 5 5 & 3 8 5 \\ 5 5 & 3 8 5 & 3, 0 2 5 \\ 3 8 5 & 3, 0 2 5 & 2 5, 3 3 3 \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 1, 2 9 1. 1 \\ 9, 5 4 9. 3 \\ 7 7, 7 5 8. 9 \end{array} \right]
$$

## *9.10 MULTIPLE LINEAR REGRESSION

In the majority of applications, the response of an experiment can be predicted more adequately not on the basis of a single independent input variable but on a collection of such variables. Indeed, a typical situation is one in which there are a set of, say, k input variables and the response Y is related to them by the relation 

$$
Y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {k} x _ {k} + e
$$

where $x _ { j } , j = 1 , \dotsc , k$ is the level of the jth input variable and $e$ is a random error that we shall assume is normally distributed with mean 0 and (constant) variance $\sigma ^ { 2 }$ . The parameters $\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { k }$ and $\sigma ^ { 2 }$ are assumed to be unknown and must be estimated from the data, which we shall suppose will consist of the values of $Y _ { 1 } , \dots , Y _ { n }$ where $Y _ { i }$ is the response level corresponding to the $k$ input levels $x _ { i 1 } , \ldots , x _ { i 2 } , \ldots , x _ { i k }$ . That is, the $Y _ { i }$ are related to these input levels through 

$$
E [ Y _ {i} ] = \beta_ {0} + \beta_ {1} x _ {i 1} + \beta_ {2} x _ {i 2} + \dots + \beta_ {k} x _ {i k}
$$

If we let $B _ { 0 } , B _ { 1 } , \ldots , B _ { k }$ denote estimators of $\beta _ { 0 } , \ldots , \beta _ { k }$ , then the sum of the squared differences between the $Y _ { i }$ and their estimated expected values is 

$$
\sum_ {i = 1} ^ {n} (Y _ {i} - B _ {0} - B _ {1} x _ {i 1} - B _ {2} x _ {i 2} - \dots - B _ {k} x _ {i k}) ^ {2}
$$

The least squares estimators are those values of $B _ { 0 } , B _ { 1 } , \ldots , B _ { k }$ that minimize the foregoing. 

To determine the least squares estimators, we repeatedly take partial derivatives of the preceding sum of squares first with respect to $B _ { 0 }$ , then to $B _ { 1 } , \ldots ,$ , then to $B _ { k }$ . On equating these $k + 1$ equations to 0, we obtain the following set of equations: 

$$
\begin{array}{c} \sum_ {i = 1} ^ {n} (Y _ {i} - B _ {0} - B _ {1} x _ {i 1} - B _ {2} x _ {i 2} - \dots - B _ {k} x _ {i k}) = 0 \\ \sum_ {i = 1} ^ {n} x _ {i 1} (Y _ {i} - B _ {0} - B _ {1} x _ {i 1} - \dots - B _ {k} x _ {i k}) = 0 \\ \sum_ {i = 1} ^ {n} x _ {i 2} (Y _ {i} - B _ {0} - B _ {1} x _ {i 1} - \dots - B _ {k} x _ {i k}) = 0 \\ \vdots \\ \sum_ {i = 1} ^ {n} x _ {i k} (Y _ {i} - B _ {0} - B _ {1} x _ {i 1} - \dots - B _ {i} x _ {i k}) = 0 \end{array}
$$

Rewriting these equations yields that the least squares estimators $B _ { 0 } , B _ { 1 } , \ldots , B _ { k }$ satisfy the following set of linear equations, called the normal equations: 

$$
\begin{array}{c} \sum_ {i = 1} ^ {n} Y _ {i} = n B _ {0} + B _ {1} \sum_ {i = 1} ^ {n} x _ {i 1} + B _ {2} \sum_ {i = 1} ^ {n} x _ {i 2} + \dots + B _ {k} \sum_ {i = 1} ^ {n} x _ {i k} \\ \sum_ {i = 1} ^ {n} x _ {i 1} Y _ {i} = B _ {0} \sum_ {i = 1} ^ {n} x _ {i 1} + B _ {1} \sum_ {i = 1} ^ {n} x _ {i 1} ^ {2} + B _ {2} \sum_ {i = 1} ^ {n} x _ {i 1} x _ {i 2} + \dots + B _ {k} \sum_ {i = 1} ^ {n} x _ {i 1} x _ {i k} \\ \vdots \\ \sum_ {i = 1} ^ {k} x _ {i k} Y _ {i} = B _ {0} \sum_ {i = 1} ^ {n} x _ {i k} + B _ {1} \sum_ {i = 1} ^ {n} x _ {i k} x _ {i 1} + B _ {2} \sum_ {i = 1} ^ {n} x _ {i k} x _ {i 2} + \dots + B _ {k} \sum_ {i = 1} ^ {n} x _ {i k} ^ {2} \end{array}\tag{9.10.1}
$$

Before solving the normal equations, it is convenient to introduce matrix notation. If we let 

$$
\mathbf {Y} = \left[ \begin{array}{c} Y _ {1} \\ Y _ {2} \\ \vdots \\ Y _ {n} \end{array} \right], \qquad \mathbf {X} = \left[ \begin{array}{c c c c c} 1 & x _ {1 1} & x _ {1 2} & \dots & x _ {1 k} \\ 1 & x _ {2 1} & x _ {2 2} & \dots & x _ {2 k} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & x _ {n 1} & x _ {n 2} & \dots & x _ {n k} \end{array} \right]
$$

$$
\boldsymbol {\beta} = \left[ \begin{array}{c} \beta_ {0} \\ \beta_ {1} \\ \vdots \\ \beta_ {k} \end{array} \right], \quad \mathbf {e} = \left[ \begin{array}{c} e _ {1} \\ e _ {2} \\ \vdots \\ e _ {n} \end{array} \right]
$$

then Y is an $n \times 1 , \mathbf { X }$ an $n \times p , \beta \mathrm { ~ a ~ } p \times 1$ , and e an $n \times 1$ matrix where $p \equiv k + 1$ 

The multiple regression model can now be written as 

$$
\mathbf {Y} = \mathbf {X} \boldsymbol {\beta} + \mathbf {e}
$$

In addition, if we let 

$$
\mathbf {B} = \left[ \begin{array}{c} B _ {0} \\ B _ {1} \\ \vdots \\ B _ {k} \end{array} \right]
$$

be the matrix of least squares estimators, then the normal Equations 9.10.1 can be written as 

$$
\mathbf {X} ^ {\prime} \mathbf {X B} = \mathbf {X} ^ {\prime} \mathbf {Y}\tag{9.10.2}
$$

where $\mathbf { X } ^ { \prime }$ is the transpose of X. 

To see that Equation 9.10.2 is equivalent to the normal Equations 9.10.1, note that 

$$
\begin{array}{r l} \mathbf {X} ^ {\prime} \mathbf {X} & = \left[ \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ x _ {1 1} & x _ {2 1} & \dots & x _ {n 1} \\ x _ {1 2} & x _ {2 2} & \dots & x _ {n 2} \\ \vdots & \vdots & & \vdots \\ x _ {1 k} & x _ {2 k} & \dots & x _ {n k} \end{array} \right] \left[ \begin{array}{c c c c c} 1 & x _ {1 1} & x _ {1 2} & \dots & x _ {1 k} \\ 1 & x _ {2 1} & x _ {2 2} & \dots & x _ {2 k} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & x _ {n 1} & x _ {n 2} & \dots & x _ {n k} \end{array} \right] \\ & = \left[ \begin{array}{c c c c c} n & \sum_ {i} x _ {i 1} & \sum_ {i} x _ {i 2} & \dots & \sum_ {i} x _ {i k} \\ \sum_ {i} x _ {i 1} & \sum_ {i} x _ {i 1} ^ {2} & \sum_ {i} x _ {i 1} x _ {i 2} & \dots & \sum_ {i} x _ {i 1} x _ {i k} \\ \vdots & \vdots & \vdots & & \vdots \\ \sum_ {i} x _ {i k} & \sum_ {i} x _ {i k} x _ {i 1} & \sum_ {i} x _ {i k} x _ {i 2} & \dots & \sum_ {i} x _ {i k} ^ {2} \end{array} \right] \end{array}
$$

and 

$$
\mathbf {X} ^ {\prime} \mathbf {Y} = \left[ \begin{array}{c} \sum_ {i} Y _ {i} \\ \sum_ {i} x _ {i 1} Y _ {i} \\ \vdots \\ \sum_ {i} x _ {i k} Y _ {i} \end{array} \right]
$$