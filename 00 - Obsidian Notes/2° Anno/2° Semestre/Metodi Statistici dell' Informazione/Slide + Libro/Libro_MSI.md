# INTRODUCTION TO PROBABILITY AND STATISTICS FOR ENGINEERS AND SCIENTISTS

Third Edition 

# ELEMENTS OF PROBABILITY

## 3.1 INTRODUCTION

The concept of the probability of a particular event of an experiment is subject to various meanings or interpretations. For instance, if a geologist is quoted as saying that “there is a 60 percent chance of oil in a certain region,” we all probably have some intuitive idea as to what is being said. Indeed, most of us would probably interpret this statement in one of two possible ways: either by imagining that 

1. the geologist feels that, over the long run, in 60 percent of the regions whose outward environmental conditions are very similar to the conditions that prevai in the region under consideration, there will be oil; or, by imagining that 

2. the geologist believes that it is more likely that the region will contain oil than it is that it will not; and in fact .6 is a measure of the geologist’s belief in the hypothesis that the region will contain oil. 

The two foregoing interpretations of the probability of an event are referred to as being the frequency interpretation and the subjective (or personal) interpretation of probability. In the frequency interpretation, the probability of a given outcome of an experiment is considered as being a “property” of that outcome. It is imagined that this property can be operationally determined by continual repetition of the experiment — the probability of the outcome will then be observable as being the proportion of the experiments that result in the outcome. This is the interpretation of probability that is most prevalent among scientists. 

In the subjective interpretation, the probability of an outcome is not thought of as being a property of the outcome but rather is considered a statement about the beliefs of the person who is quoting the probability, concerning the chance that the outcome will occur. Thus, in this interpretation, probability becomes a subjective or personal concept and ha no meaning outside of expressing one’s degree of belief. This interpretation of probability is often favored by philosophers and certain economic decision makers. 

Regardless of which interpretation one gives to probability, however, there is a general consensus that the mathematics of probability are the same in either case. For instance, if you think that the probability that it will rain tomorrow is .3 and you feel that the probability that it will be cloudy but without any rain is .2, then you should feel that the probability that it will either be cloudy or rainy is .5 independently of your individual interpretation of the concept of probability. In this chapter, we present the accepted rules, or axioms, used in probability theory. As a preliminary to this, however, we need to study the concept of the sample space and the events of an experiment. 

## 3.2 SAMPLE SPACE AND EVENTS

Consider an experiment whose outcome is not predictable with certainty in advance. Although the outcome of the experiment will not be known in advance, let us suppose that the set of all possible outcomes is known. This set of all possible outcomes of an experiment is known as the sample space of the experiment and is denoted by S. Some examples are the following. 

1. If the outcome of an experiment consists in the determination of the sex of a newborn child, then 

$$
S = \{g, b \}
$$

where the outcome g means that the child is a girl and b that it is a boy. 

2. If the experiment consists of the running of a race among the seven horses having post positions 1, 2, 3, 4, 5, 6, 7, then 

$$
S = \{\text { all   orderings   of } (1, 2, 3, 4, 5, 6, 7) \}
$$

The outcome (2, 3, 1, 6, 5, 4, 7) means, for instance, that the number 2 horse is first, then the number 3 horse, then the number 1 horse, and so on. 

3. Suppose we are interested in determining the amount of dosage that must be given to a patient until that patient reacts positively. One possible sample space for this experiment is to let S consist of all the positive numbers. That is, let 

$$
S = (0, \infty)
$$

where the outcome would be x if the patient reacts to a dosage of value x but not to any smaller dosage. 

Any subset E of the sample space is known as an event. That is, an event is a set consisting of possible outcomes of the experiment. If the outcome of the experiment is contained in E, then we say that E has occurred. Some examples of events are the following. 

In Example 1 if $E = \{ g \}$ , then E is the event that the child is a girl. Similarly, if $F = \{ b \}$ , then F is the event that the child is a boy. 

In Example 2 if 

## E = {all outcomes in S starting with a 3}

then E is the event that the number 3 horse wins the race. 

For any two events E and F of a sample space S, we define the new event $E \cup F _ { : }$ , called the union of the events E and F, to consist of all outcomes that are either in E or in F or in both $E$ and F. That is, the event $E \cup F$ will occur if either E or $F$ occurs. For instance, in Example 1 if $E = \{ g \}$ and $F = \{ b \}$ , then $E \cup F = \{ g , b \}$ . That is,$E \cup F$ would be the whole sample space S. In Example 2 if E = {all outcomes starting with 6} is the event that the number 6 horse wins and $F = \{ { \mathrm { a l l } }$ outcomes having 6 in the second position} is the event that the number 6 horse comes in second, then $E \cup F$ is the event that the number 6 horse comes in either first or second. 

Similarly, for any two events E and $F ,$ we may also define the new event EF, called the intersection of E and $F ,$ to consist of all outcomes that are in both E and F. That is, the event EF will occur only if both E and F occur. For instance, in Example 3 if $E = ( 0 , 5 )$ is the event that the required dosage is less than 5 and $F = ( 2 , 1 0 )$ is the event that it i between 2 and 10, then $E F = ( 2 , 5 )$ is the event that the required dosage is between 2 and 5. In Example 2 if $E =$ {all outcomes ending in 5} is the event that horse number 5 comes in last and $F = \{ { \mathrm { a l l } }$ outcomes starting with 5} is the event that horse number 5 comes in first, then the event $E F$ does not contain any outcomes and hence cannot occur. To give such an event a name, we shall refer to it as the null event and denote it by ∅. Thus ∅ refers to the event consisting of no outcomes. If $E F = \emptyset$ , implying that E and F cannot both occur, then E and F are said to be mutually exclusive. 

For any event $E ,$ we define the event $E ^ { c }$ , referred to as the complement of $E ,$ to consist of all outcomes in the sample space S that are not in E. That is,$E ^ { c }$ will occur if and only if E does not occur. In Example 1 if ${ \cal E } = \{ b \}$ is the event that the child is a boy, then $E ^ { c } = \{ g \}$ is the event that it is a girl. Also note that since the experiment must result in some outcome, it follows that $S ^ { c } = \emptyset$ 

For any two events E and F, if all of the outcomes in E are also in F, then we say that E is contained in F and write $E \subset F$ (or equivalently,$F \supset E )$ . Thus if $E \subset F$ , then the occurrence of E necessarily implies the occurrence of F. If $E \subset F$ and $F \subset E$ , then we say that E and F are equal (or identical) and we write $E = F$ 

We can also define unions and intersections of more than two events. In particular, the union of the events $E _ { 1 } , E _ { 2 } , \ldots , E _ { n }$ , denoted either by $E _ { 1 } \cup E _ { 2 } \cup \ldots \cup E _ { n }$ or by$\cup _ { 1 } ^ { n } E _ { i }$ , is defined to be the event consisting of all outcomes that are in $E _ { i }$ for at least one $i = 1 , 2 , \ldots , n .$ . Similarly, the intersection of the events $E _ { i } , i = 1 , 2 , \ldots , n ,$ , denoted by $E _ { 1 } E _ { 2 } \cdots E _ { n } ,$ is defined to be the event consisting of those outcomes that are in all of the events $E _ { i } , i = 1 , 2 , \ldots , n$ . In other words, the union of the $E _ { i }$ occurs when at least one of the events $E _ { i }$ occurs; the intersection occurs when all of the events $E _ { i }$ occur. 

## 3.3 VENN DIAGRAMS AND THE ALGEBRA OF EVENTS

A graphical representation of events that is very useful for illustrating logical relations among them is the Venn diagram. The sample space S is represented as consisting of all the points in a large rectangle, and the events $E , F , G , \ldots$ , are represented as consisting of all the points in given circles within the rectangle. Events of interest can then be indicated by shading appropriate regions of the diagram. For instance, in the three Venn diagrams shown in Figure 3.1, the shaded areas represent respectively the events $E \cup F , E F ,$ and $E ^ { c }$ The Venn diagram of Figure 3.2 indicates that $E \subset F .$ 

The operations of forming unions, intersections, and complements of events obey certain rules not dissimilar to the rules of algebra. We list a few of these. 

$$
\begin{array}{l l l} \text {Commutative law} & E \cup F = F \cup E & E F = F E \\ \text {Associative law} & (E \cup F) \cup G = E \cup (F \cup G) & (E F) G = E (F G) \\ \text {Distributive law} & (E \cup F) G = E G \cup F G & E F \cup G = (E \cup G) (F \cup G) \end{array}
$$

These relations are verified by showing that any outcome that is contained in the event on the left side of the equality is also contained in the event on the right side and vice versa. One way of showing this is by means of Venn diagrams. For instance, the distributive law may be verified by the sequence of diagrams shown in Figure 3.3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/86c9ad5b3f7130e632f6e07c390840684d67e5e4a32b48dfc81caec2149d2ff0.jpg)



(a) Shaded region: E F



FIGURE 3.1 Venn diagrams.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/53971b6ad96d49db4bf4ab3d75c975618c0b29ef4114eaec28b9c8939d26dc76.jpg)



(b) Shaded region: EF


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/e5cf66ae65b562d3ce8847d57e4f584414963a191388085618e385f0582f4ed9.jpg)



(c) Shaded region: E<sup>c</sup>


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/663b8d2437a1645c3333e5128bb1d62d51defee939f34a292b5340f6f91b4e0d.jpg)



FIGURE 3.2 Venn diagram.



E ⊂F


## 3.4 Axioms of Probability

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/f02d8a0fab141bc89aa0eb577736d46602d207954853357d048048ccee7c154c.jpg)



(a) Shaded region: EG


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5921b4b7eb6ac9a7dca7d6a0968b0a68103e75808c10296af1b6f53e7e0d7fe0.jpg)



(b) Shaded region: FG


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/02746014b2ea44c173a19b29547b259987bffc0a4962a6143ad0baf7ca1350a9.jpg)



(c) Shaded region: (E F)G (E F)G = EG FG



FIGURE 3.3 Proving the distributive law.


The following useful relationship between the three basic operations of forming unions, intersections, and complements of events is known as DeMorgan’s laws. 

$$
\begin{array}{c} (E \cup F) ^ {c} = E ^ {c} F ^ {c} \\ (E F) ^ {c} = E ^ {c} \cup F ^ {c} \end{array}
$$

## 3.4 AXIOMS OF PROBABILITY

It appears to be an empirical fact that if an experiment is continually repeated under the exact same conditions, then for any event E, the proportion of time that the outcome is contained in E approaches some constant value as the number of repetitions increases. For instance, if a coin is continually flipped, then the proportion of flips resulting in heads will approach some value as the number of flips increases. It is this constant limiting frequency that we often have in mind when we speak of the probability of an event. 

From a purely mathematical viewpoint, we shall suppose that for each event E of an experiment having a sample space S there is a number, denoted by $P ( E )$ ), that is in accord with the following three axioms. 

AXIOM 1 

$$
0 \leq P (E) \leq 1
$$

AXIOM 2 

$$
P (S) = 1
$$

AXIOM 3 

For any sequence of mutually exclusive events $E _ { 1 } , E _ { 2 } , \ldots$ . (that is, events for which $E _ { i } E _ { j } = \theta$ when $i \neq j )$ , 

$$
P \left(\bigcup_ {i = 1} ^ {n} E _ {i}\right) = \sum_ {i = 1} ^ {n} P (E _ {i}), \quad n = 1, 2, \dots , \infty
$$

We call P(E ) the probability of the event E. 

Thus, Axiom 1 states that the probability that the outcome of the experiment is contained in E is some number between 0 and 1. Axiom 2 states that, with probability 1, the outcome will be a member of the sample space S. Axiom 3 states that for any set of mutually exclusive events the probability that at least one of these events occurs is equal to the sum of their respective probabilities. 

It should be noted that if we interpret $P ( E )$ as the relative frequency of the event E when a large number of repetitions of the experiment are performed, then $P ( E )$ would indeed satisfy the above axioms. For instance, the proportion (or frequency) of time that the outcome is in E is clearly between 0 and 1, and the proportion of time that it is in S is 1 (since all outcomes are in S ). Also, if E and F have no outcomes in common, then the proportion of time that the outcome is in either E or F is the sum of their respective frequencies. As an illustration of this last statement, suppose the experiment consists of the rolling of a pair of dice and suppose that E is the event that the sum is 2, 3, or 12 and F is the event that the sum is 7 or 11. Then if outcome E occurs 11 percent of the time and outcome F 22 percent of the time, then 33 percent of the time the outcome will be either 2, 3, 12, 7, or 11. 

These axioms will now be used to prove two simple propositions concerning probabilities. We first note that E and $E ^ { c }$ are always mutually exclusive, and since $E \cup E ^ { c } = S$ we have by Axioms 2 and 3 that 

$$
1 = P (S) = P (E \cup E ^ {c}) = P (E) + P (E ^ {c})
$$

Or equivalently, we have the following: 

## PROPOSITION 3.4.1

$$
P (E ^ {c}) = 1 - P (E)
$$

In other words, Proposition 3.4.1 states that the probability that an event does not occur is 1 minus the probability that it does occur. For instance, if the probability of obtaining a head on the toss of a coin is$\frac { 3 } { 8 }$ , the probability of obtaining a tail must be$\frac { 5 } { 8 }$ . 

Our second proposition gives the relationship between the probability of the union of two events in terms of the individual probabilities and the probability of the intersection 

## PROPOSITION 3.4.2

$$
P (E \cup F) = P (E) + P (F) - P (E F)
$$

## Proof

This proposition is most easily proven by the use of a Venn diagram as shown in Figure 3.4. As the regions I, II, and III are mutually exclusive, it follows that 

$$
\begin{array}{c} P (E \cup F) = P (\mathrm{I}) + P (\mathrm{II}) + P (\mathrm{III}) \\ P (E) = P (\mathrm{I}) + P (\mathrm{II}) \\ P (F) = P (\mathrm{II}) + P (\mathrm{III}) \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/564d23373d2c0461d4a181506e183073e81d52491e8f4cc8d6ee0d6c3e63f838.jpg)


## FIGURE 3.4

which shows that 

$$
P (E \cup F) = P (E) + P (F) - P (\mathrm{II})
$$

and the proof is complete since$\mathrm { I I } = E F .$ 

EXAMPLE 3.4a A total of 28 percent of American males smoke cigarettes, 7 percent smoke cigars, and 5 percent smoke both cigars and cigarettes. What percentage of males smoke neither cigars nor cigarettes? 

SOLUTION Let E be the event that a randomly chosen male is a cigarette smoker and let B be the event that he is a cigar smoker. Then, the probability this person is either a cigarette or a cigar smoker is 

$$
P (E \cup F) = P (E) + P (F) - P (E F) = . 0 7 +. 2 8 -. 0 5 = . 3
$$

Thus the probability that the person is not a smoker is .7, implying that 70 percent of American males smoke neither cigarettes nor cigars. ■ 

The odds of an event A is defined by 

$$
\frac {P (A)}{P (A ^ {c})} = \frac {P (A)}{1 - P (A)}
$$

Thus the odds of an event A tells how much more likely it is that A occurs than that it does not occur. For instance if $P ( A ) = 3 / 4$ , then $P ( A ) / ( 1 - P ( A ) ) = 3$ , so the odds is 3. Consequently, it is 3 times as likely that A occurs as it is that it does not. 

## 3.5 SAMPLE SPACES HAVING EQUALLY LIKELY OUTCOMES

For a large number of experiments, it is natural to assume that each point in the sample space is equally likely to occur. That is, for many experiments whose sample space S is a finite set, say $S = \{ 1 , 2 , \dots , N \}$ , it is often natural to assume that 

$$
P (\{1 \}) = P (\{2 \}) = \dots = P (\{N \}) = p \quad (\text { say })
$$

Now it follows from Axioms 2 and 3 that 

$$
1 = P (S) = P (\{1 \}) + \dots + P (\{N \}) = N p
$$

which shows that 

$$
P (\{i \}) = p = 1 / N
$$

From this it follows from Axiom 3 that for any event E, 

$$
P (E) = \frac {\text { Number   of   points   in } E}{N}
$$

In words, if we assume that each outcome of an experiment is equally likely to occur, then the probability of any event E equals the proportion of points in the sample space that are contained in E. 

Thus, to compute probabilities it is often necessary to be able to effectively count the number of different ways that a given event can occur. To do this, we will make use of the following rule. 

## BASIC PRINCIPLE OF COUNTING

Suppose that two experiments are to be performed. Then if experiment 1 can result in any one of m possible outcomes and if, for each outcome of experiment 1, there are n possible outcomes of experiment 2, then together there are mn possible outcomes of the two experiments. 

## Proof of the Basic Principle

The basic principle can be proven by enumerating all the possible outcomes of the two experiments as follows: 

$$
\begin{array}{c} (1, 1), (1, 2), \ldots , (1, n) \\ (2, 1), (2, 2), \ldots , (2, n) \\ \vdots \\ (m, 1), (m, 2), \ldots , (m, n) \end{array}
$$

where we say that the outcome is (i, j) if experiment 1 results in its ith possible outcome and experiment 2 then results in the jth of its possible outcomes. Hence, the set of possible outcomes consists of m rows, each row containing n elements, which proves the result. ■ 

EXAMPLE 3.5a Two balls are “randomly drawn” from a bowl containing 6 white and 5 black balls. What is the probability that one of the drawn balls is white and the other black? 

SOLUTION If we regard the order in which the balls are selected as being significant, then as the first drawn ball may be any of the 11 and the second any of the remaining 10, it follows that the sample space consists of $1 1 \cdot 1 0 = 1 1 0$ points. Furthermore, there are $6 \cdot 5 = 3 0$ ways in which the first ball selected is white and the second black, and similarly there are $5 \cdot 6 = 3 0$ ways in which the first ball is black and the second white. Hence, assuming that “randomly drawn” means that each of the 110 points in the sample space is equally likely to occur, then we see that the desired probability is 

$$
\frac {3 0 + 3 0}{1 1 0} = \frac {6}{1 1}
$$

When there are more than two experiments to be performed the basic principle can be generalized as follows: 

## Generalized Basic Principle of Counting

If r experiments that are to be performed are such that the first one may result in any of$\cdot _ { n _ { 1 } }$ possible outcomes, and if for each of these$\displaystyle n _ { 1 }$ possible outcomes there are $_ { n 2 }$ possible outcomes of the second experiment, and if for each of the possible outcomes of the first two experiments there are $n _ { 3 }$ possible outcomes of the third experiment, and$\operatorname { i f } , \ldots$ , then there are a total of $n _ { 1 } \cdot n _ { 2 } \cdot \cdot \cdot n _ { r }$ possible outcomes of the r experiments. 

As an illustration of this, let us determine the number of different ways n distinct objects can be arranged in a linear order. For instance, how many different ordered arrangements of the letters a, b, c are possible? By direct enumeration we see that there are $6 ;$ namely, abc, acb, bac, bca, cab, cba. Each one of these ordered arrangements is known as a permutation. Thus, there are 6 possible permutations of a set of 3 objects. This result could also have been obtained from the basic principle, since the first object in the permutation can be any of the 3, the second object in the permutation can then be chosen from any of the remaining 2, and the third object in the permutation is then chosen from the remaining one. Thus, there are $3 \cdot 2 \cdot 1 = 6$ possible permutations. 

Suppose now that we have n objects. Similar reasoning shows that there are 

$$
n (n - 1) (n - 2) \cdot \cdot \cdot 3 \cdot 2 \cdot 1
$$

different permutations of the n objects. It is convenient to introduce the notation n!, which is read $^ { * } n$ factorial,” for the foregoing expression. That is, 

$$
n! = n (n - 1) (n - 2) \cdot \cdot \cdot 3 \cdot 2 \cdot 1
$$

Thus, for instance,$1 ! = 1 , 2 ! = 2 \cdot 1 = 2 , 3 ! = 3 \cdot 2 \cdot 1 = 6 , 4 ! = 4 \cdot 3 \cdot 2 \cdot 1 = 2 4$ , and so on. It is convenient to define 0! = 1. 

EXAMPLE 3.5b Mr. Jones has 10 books that he is going to put on his bookshelf. Of these, 4 are mathematics books, 3 are chemistry books, 2 are history books, and 1 is a language book. Jones wants to arrange his books so that all the books dealing with the same subject are together on the shelf. How many different arrangements are possible? 

SOLUTION There are 4! 3! 2! 1! arrangements such that the mathematics books are first in line, then the chemistry books, then the history books, and then the language book. Similarly, for each possible ordering of the subjects, there are 4! 3! 2! 1! possible arrangements. Hence, as there are 4! possible orderings of the subjects, the desired answer is 4! 4! 3! 2! 1! = 6,912. ■ 

EXAMPLE 3.5c A class in probability theory consists of 6 men and 4 women. An exam is given and the students are ranked according to their performance. Assuming that no two students obtain the same score, (a) how many different rankings are possible? (b) If all rankings are considered equally likely, what is the probability that women receive the top 4 scores? 

## SOLUTION

(a) Because each ranking corresponds to a particular ordered arrangement of the 10 people, we see the answer to this part is $1 0 ! = 3 \mathrm { , } 6 2 8 \mathrm { , } 8 0 0$ 

(b) Because there are 4! possible rankings of the women among themselves and 6! possible rankings of the men among themselves, it follows from the basic principle that there are $( 6 ! ) ( 4 ! ) = ( 7 2 0 ) ( 2 4 ) = 1 7 { , } 2 8 0$ possible rankings in which the women receive the top 4 scores. Hence, the desired probability is 

$$
\frac {6 ! 4 !}{1 0 !} = \frac {4 \cdot 3 \cdot 2 \cdot 1}{1 0 \cdot 9 \cdot 8 \cdot 7} = \frac {1}{2 1 0}
$$

Suppose now that we are interested in determining the number of different groups of r objects that could be formed from a total of n objects. For instance, how many different groups of three could be selected from the five items A, B, C , D, E ? To answer this, reason as follows. Since there are 5 ways to select the initial item, 4 ways to then select the next item, and 3 ways to then select the final item, there are thus 5 · 4 · 3 ways of selecting the group of 3 when the order in which the items are selected is relevant. However, since every group of 3, say the group consisting of items A, B, and C, will be counted 6 times (that is, all of the permutations ABC, ACB, BAC, BCA, CAB, CBA will be counted when the order of selection is relevant), it follows that the total number of different groups that can be formed is $( 5 \cdot 4 \cdot 3 ) / ( 3 \cdot 2 \cdot 1 ) = 1 0$ 

In general, as $n ( n - 1 ) \cdots ( n - r + 1 )$ represents the number of different ways that a group of r items could be selected from n items when the order of selection is considered relevant (since the first one selected can be any one of the n, and the second selected any one of the remaining n − 1, etc.), and since each group of r items will be counted r! times in this count, it follows that the number of different groups of r items that could be formed from a set of n items is 

$$
{\frac {n (n - 1) \cdots (n - r + 1)}{r !}} = {\frac {n !}{(n - r) ! r !}}
$$

## NOTATION AND TERMINOLOGY

We define <sup>n</sup>, for $r \leq n ,$ by 

$$
\binom {n} {r} = \frac {r !}{(n - r) ! r !}
$$

and call$\binom { n } { r }$ the number of combinations of n objects taken r at a time. 

Thus <sup>n</sup> represents the number of different groups of size r that can be selected from a set of size n when the order of selection is not considered relevant. For example, there are 

$$
\binom {8} {2} = \frac {8 \cdot 7}{2 \cdot 1} = 2 8
$$

different groups of size 2 that can be chosen from a set of 8 people, and 

$$
\binom {1 0} {2} = \frac {1 0 \cdot 9}{2 \cdot 1} = 4 5
$$

different groups of size 2 that can be chosen from a set of 10 people. Also, since $0 ! = 1$ note that 

$$
\binom {n} {0} = \binom {n} {n} = 1
$$

EXAMPLE 3.5d A committee of size 5 is to be selected from a group of 6 men and 9 women. If the selection is made randomly, what is the probability that the committee consists of 3 men and 2 women? 

SOLUTION Let us assume that “randomly selected” means that each of the$\binom { 1 5 } { 5 }$ possible combinations is equally likely to be selected. Hence, since there are$\binom { 6 } { 3 }$ possible choices of 3 men and$\binom { 9 } { 2 }$ possible choices of 2 women, it follows that the desired probability is given by 

$$
\frac {\binom {6} {3} \binom {9} {2}}{\binom {1 5} {5}} = \frac {2 4 0}{1 0 0 1}
$$

EXAMPLE 3.5e From a set of n items a random sample of size k is to be selected. What is the probability a given item will be among the k selected? 

SOLUTION The number of different selections that contain the given item is ${ \binom { 1 } { 1 } } { \binom { n - 1 } { k - 1 } }$ Hence, the probability that a particular item is among the k selected is 

$$
\binom {n - 1} {k - 1} \bigg / \binom {n} {k} = \frac {(n - 1) !}{(n - k) ! (k - 1) !} \bigg / \frac {n !}{(n - k) ! k !} = \frac {k}{n}
$$

EXAMPLE 3.5f A basketball team consists of 6 black and 6 white players. The players are to be paired in groups of two for the purpose of determining roommates. If the pairings are done at random, what is the probability that none of the black players will have a white roommate? 

SOLUTION Let us start by imagining that the 6 pairs are numbered — that is, there is a first pair, a second pair, and so on. Since there are$\binom { 1 2 } { 2 }$ different choices of a first pair; and for each choice of a first pair there are$\textstyle { \binom { 1 0 } { 2 } }$ different choices of a second pair; and for each choice of the first 2 pairs there are$\binom { 8 } { 2 }$ choices for a third pair; and so on, it follows from the generalized basic principle of counting that there are 

$$
\binom {1 2} {2} \binom {1 0} {2} \binom {8} {2} \binom {6} {2} \binom {4} {2} \binom {2} {2} = \frac {1 2 !}{(2 !) ^ {6}}
$$

ways of dividing the players into a first pair, a second pair, and so on. Hence there are $( 1 2 ) ! / 2 ^ { 6 } 6 !$ ways of dividing the players into 6 (unordered) pairs of 2 each. Furthermore, since there are, by the same reasoning,$6 ! / 2 ^ { 3 } 3 !$ ways of pairing the white players among themselves and $6 ! / 2 ^ { 3 } 3 !$ ways of pairing the black players among themselves, it follows that there are $( 6 ! / 2 ^ { 3 } 3 ! ) ^ { 2 }$ pairings that do not result in any black–white roommate pairs. Hence, if the pairings are done at random (so that all outcomes are equally likely), then the desired probability is 

$$
\left(\frac {6 !}{2 ^ {3} 3 !}\right) ^ {2} / \frac {(1 2) !}{2 ^ {6} 6 !} = \frac {5}{2 3 1} = . 0 2 1 6
$$

Hence, there are roughly only two chances in a hundred that a random pairing will not result in any of the white and black players rooming together. ■ 

EXAMPLE 3.5g If n people are present in a room, what is the probability that no two of them celebrate their birthday on the same day of the year? How large need n be so that this probability is less than$\begin{array} { l } { { \displaystyle { \frac { 1 } { 2 } } ? } } \end{array}$ 

SOLUTION Because each person can celebrate his or her birthday on any one of 365 days, there are a total of $( 3 6 5 ) ^ { n }$ possible outcomes. (We are ignoring the possibility of someone having been born on February 29.) Furthermore, there are (365)(364)(363)·(365−n+1) possible outcomes that result in no two of the people having the same birthday. This is so because the first person could have any one of 365 birthdays, the next person any of the remaining 364 days, the next any of the remaining 363, and so on. Hence, assuming tha each outcome is equally likely, we see that the desired probability is 

$$
\frac {(3 6 5) (3 6 4) (3 6 3) \cdots (3 6 5 - n + 1)}{(3 6 5) ^ {n}}
$$

It is a rather surprising fact that when $n \geq 2 3$ , this probability is less than$\frac { 1 } { 2 }$ . That is, if there are 23 or more people in a room, then the probability that at least two of them have the same birthday exceeds$\frac { 1 } { 2 }$ . Many people are initially surprised by this result, since 23 seems so small in relation to 365, the number of days of the year. However, every pair of individuals has probability$\begin{array} { r } { \frac { 3 6 5 } { ( 3 6 5 ) ^ { 2 } } = \frac { 1 } { 3 6 5 } } \end{array}$ of having the same birthday, and in a group of 23 people there are ${ \binom { 2 3 } { 2 } } = 2 5 3$ different pairs of individuals. Looked at this way, the result no longer seems so surprising. ■ 

## 3.6 CONDITIONAL PROBABILITY

In this section, we introduce one of the most important concepts in all of probability theory — that of conditional probability. Its importance is twofold. In the first place, we are often interested in calculating probabilities when some partial information concerning the result of the experiment is available, or in recalculating them in light of additional information. In such situations, the desired probabilities are conditional ones. Second, as a kind of a bonus, it often turns out that the easiest way to compute the probability of an event is to first “condition” on the occurrence or nonoccurrence of a secondary event. 

As an illustration of a conditional probability, suppose that one rolls a pair of dice. The sample space S of this experiment can be taken to be the following set of 36 outcomes 

$$
S = \{(i, j), \quad i = 1, 2, 3, 4, 5, 6, \quad j = 1, 2, 3, 4, 5, 6 \}
$$

where we say that the outcome is $( i , j )$ if the first die lands on side i and the second on side $j .$ Suppose now that each of the 36 possible outcomes is equally likely to occur and thus has probability$\frac { 1 } { 3 6 }$ . (In such a situation we say that the dice are fair.) Suppose further that we observe that the first die lands on side 3. Then, given this information, what is the probability that the sum of the two dice equals 8? To calculate this probability, we reason as follows: Given that the initial die is a 3, there can be at most 6 possible outcomes of our experiment, namely, (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), and (3, 6). In addition, because each of these outcomes originally had the same probability of occurring, they should stil have equal probabilities. That is, given that the first die is a 3, then the (conditional) probability of each of the outcomes $( 3 , 1 ) , ( 3 , 2 ) , ( 3 , 3 ) , ( 3 , 4 ) , ( 3 , 5 ) , ( 3 , 6 ) { \mathrm { i s } } { \frac { 1 } { 6 } } ,$ , whereas the (conditional) probability of the other 30 points in the sample space is 0. Hence, the desired probability will be$\frac { 1 } { 6 }$ 

If we let E and F denote, respectively, the event that the sum of the dice is 8 and the event that the first die is a 3, then the probability just obtained is called the conditional probability of E given that F has occurred, and is denoted by 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/fd3fed21a61bc7559d0beaa1204b9c4871bff13bba4eca9bbfcef3754586d272.jpg)



FIGURE 3.5$\begin{array} { r } { \overline { { P ( E | F ) } } = \frac { P ( E F ) } { P ( F ) } , } \end{array}$


$$
P (E | F)
$$

A general formula for $P ( E | F )$ that is valid for all events E and F is derived in the same manner as just described. Namely, if the event F occurs, then in order for E to occur it is necessary that the actual occurrence be a point in both E and $F ;$ that is, it must be in EF. Now, since we know that F has occurred, it follows that F becomes our new (reduced) sample space and hence the probability that the event $E F$ occurs will equal the probability of EF relative to the probability of F. That is, 

$$
P (E | F) = \frac {P (E F)}{P (F)}\tag{3.6.1}
$$

Note that Equation 3.6.1 is well defined only when $P ( F ) > 0$ and hence $P ( E | F )$ is defined only when $P ( F ) > 0$ . (See Figure 3.5.) 

The definition of conditional probability given by Equation 3.6.1 is consistent with the interpretation of probability as being a long-run relative frequency. To see this, suppose that a large number n of repetitions of the experiment are performed. Then, since $P ( F )$ is the long-run proportion of experiments in which F occurs, it follows that F will occur approximately $n P ( F )$ times. Similarly, in approximately nP(EF ) of these experiments, both E and F will occur. Hence, of the approximately $n P ( F )$ experiments whose outcome is in F, approximately $n P ( E F )$ of them will also have their outcome in E. That is, for those experiments whose outcome is in F, the proportion whose outcome is also in E is approximately 

$$
\frac {n P (E F)}{n P (F)} = \frac {P (E F)}{P (F)}
$$

Since this approximation becomes exact as n becomes larger and larger, it follows that (3.6.1) gives the appropriate definition of the conditional probability of E given that F has occurred. 

EXAMPLE 3.6a A bin contains 5 defective (that immediately fail when put in use), 10 partially defective (that fail after a couple of hours of use), and 25 acceptable transistors. A transistor is chosen at random from the bin and put into use. If it does not immediately fail, what is the probability it is acceptable? 

SOLUTION Since the transistor did not immediately fail, we know that it is not one of the 5 defectives and so the desired probability is: 

$$
\begin{array}{r l} & P \{\text { acceptable } | \text { not   defective } \} \\ & = \frac {P \{\text { acceptable,   not   defective } \}}{P \{\text { not   defective } \}} \\ & = \frac {P \{\text { acceptable } \}}{P \{\text { not   defective } \}} \end{array}
$$

where the last equality follows since the transistor will be both acceptable and not defective if it is acceptable. Hence, assuming that each of the 40 transistors is equally likely to be chosen, we obtain that 

$$
P \{\text { acceptable } | \text { not   defective } \} = \frac {2 5 / 4 0}{3 5 / 4 0} = 5 / 7
$$

It should be noted that we could also have derived this probability by working directly with the reduced sample space. That is, since we know that the chosen transistor is not defective, the problem reduces to computing the probability that a transistor, chosen at random from a bin containing 25 acceptable and 10 partially defective transistors, is acceptable. This is clearly equal to$\frac { 2 5 } { 3 5 }$ . ■ 

EXAMPLE 3.6b The organization that Jones works for is running a father–son dinner for those employees having at least one son. Each of these employees is invited to attend along with his youngest son. If Jones is known to have two children, what is the conditional probability that they are both boys given that he is invited to the dinner? Assume that the sample space S is given by $S = \{ ( b , b ) , ( b , g ) , ( g , b ) , ( g , g ) \}$ and all outcomes are equally likely $[ ( b , g )$ means, for instance, that the younger child is a boy and the older child is a girl]. 

SOLUTION The knowledge that Jones has been invited to the dinner is equivalent to knowing that he has at least one son. Hence, letting B denote the event that both children are boys, and A the event that at least one of them is a boy, we have that the desired probability $P ( B | A )$ is given by 

$$
\begin{array}{r l} P (B | A) & = \frac {P (B A)}{P (A)} \\ & = \frac {P (\{(b , b) \})}{P (\{(b , b) , (b , g) , (g , b) \})} \\ & = \frac {\frac {1}{4}}{\frac {3}{4}} = \frac {1}{3} \end{array}
$$

Many readers incorrectly reason that the conditional probability of two boys given at least one is$\frac { 1 } { 2 }$ , as opposed to the correct$\frac 1 3$ , since they reason that the Jones child not attending the dinner is equally likely to be a boy or a girl. Their mistake, however, is in assuming that these two possibilities are equally likely. Remember that initially there were four equally likely outcomes. Now the information that at least one child is a boy is equivalent to knowing that the outcome is not $( g , g )$ . Hence we are left with the three equally likely outcomes $( b , b ) , ( b , g ) , ( g , b )$ , thus showing that the Jones child not attending the dinne is twice as likely to be a girl as a boy. ■ 

By multiplying both sides of Equation 3.6.1 by P(F ) we obtain that 

$$
P (E F) = P (F) P (E | F)\tag{3.6.2}
$$

In words, Equation 3.6.2 states that the probability that both E and F occur is equal to the probability that F occurs multiplied by the conditional probability of E given that F occurred. Equation 3.6.2 is often quite useful in computing the probability of the intersection of events. This is illustrated by the following example. 

EXAMPLE 3.6c Ms. Perez figures that there is a 30 percent chance that her company will set up a branch office in Phoenix. If it does, she is 60 percent certain that she will be made manager of this new operation. What is the probability that Perez will be a Phoenix branch office manager? 

SOLUTION If we let B denote the event that the company sets up a branch office in Phoenix and M the event that Perez is made the Phoenix manager, then the desired probability is P(BM), which is obtained as follows: 

$$
\begin{array}{r l} P (B M) & = P (B) P (M | B) \\ & = (. 3) (. 6) \\ & = . 1 8 \end{array}
$$

Hence, there is an 18 percent chance that Perez will be the Phoenix manager. ■ 

## 3.7 BAYES’ FORMULA

Let E and F be events. We may express E as 

$$
E = E F \cup E F ^ {c}
$$

for, in order for a point to be in E, it must either be in both E and F or be in E but not in F. (See Figure 3.6.) As EF and $E F ^ { c }$ are clearly mutually exclusive, we have by Axiom 3 that 

$$
\begin{array}{r l} & P (E) = P (E F) + P (E F ^ {c}) \\ & \quad = P (E | F) P (F) + P (E | F ^ {c}) P (F ^ {c}) \\ & \quad = P (E | F) P (F) + P (E | F ^ {c}) [ 1 - P (F) ] \end{array}\tag{3.7.1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/644dc66b5fd178d7cc1ec2ea5982f6c5ccb1a35a6c941e0c9f1aaa0e59a2ff3e.jpg)



FIGURE 3.6 E = EF ∪ EF <sup>c</sup> .


Equation 3.7.1 states that the probability of the event E is a weighted average of the conditional probability of E given that F has occurred and the conditional probability of E given that F has not occurred: Each conditional probability is given as much weight as the event it is conditioned on has of occurring. It is an extremely useful formula, for its use often enables us to determine the probability of an event by first “conditioning” on whether or not some second event has occurred. That is, there are many instances where it is difficult to compute the probability of an event directly, but it is straightforward to compute it once we know whether or not some second event has occurred. 

EXAMPLE 3.7a An insurance company believes that people can be divided into two classes — those that are accident prone and those that are not. Their statistics show that an accident-prone person will have an accident at some time within a fixed 1-yea period with probability .4, whereas this probability decreases to .2 for a non-accident-prone person. If we assume that 30 percent of the population is accident prone, what is the prob ability that a new policy holder will have an accident within a year of purchasing a policy? 

SOLUTION We obtain the desired probability by first conditioning on whether or not the policy holder is accident prone. Let $A _ { 1 }$ denote the event that the policy holder will have an accident within a year of purchase; and let A denote the event that the policy holder i accident prone. Hence, the desired probability,$P ( A _ { 1 } )$ ), is given by 

$$
\begin{array}{c} P (A _ {1}) = P (A _ {1} | A) P (A) + P (A _ {1} | A ^ {c}) P (A ^ {c}) \\ = (. 4) (. 3) + (. 2) (. 7) = . 2 6 \quad \blacksquare \end{array}
$$

In the next series of examples, we will indicate how to reevaluate an initial probability assessment in the light of additional (or new) information. That is, we will show how to incorporate new information with an initial probability assessment to obtain an updated probability. 

EXAMPLE 3.7b Reconsider Example 3.7a and suppose that a new policy holder has an accident within a year of purchasing his policy. What is the probability that he is accident prone? 

SOLUTION Initially, at the moment when the policy holder purchased his policy, we assumed there was a 30 percent chance that he was accident prone. That is,$P ( A ) = . 3 .$ 

However, based on the fact that he has had an accident within a year, we now reevaluate his probability of being accident prone as follows. 

$$
\begin{array}{r l} P (A | A _ {1}) & = \frac {P (A A _ {1})}{P (A _ {1})} \\ & = \frac {P (A) P (A _ {1} | A)}{P (A _ {1})} \\ & = \frac {(. 3) (. 4)}{. 2 6} = \frac {6}{1 3} = . 4 6 1 5 \end{array}
$$

EXAMPLE 3.7c In answering a question on a multiple-choice test, a student either knows the answer or she guesses. Let$\boldsymbol { \underline { P } }$ be the probability that she knows the answer and $1 - p$ the probability that she guesses. Assume that a student who guesses at the answer will be correct with probability 1/m, where m is the number of multiple-choice alternatives. What is the conditional probability that a student knew the answer to a question given that she answered it correctly? 

SOLUTION Let $C$ and K denote, respectively, the events that the student answers the question correctly and the event that she actually knows the answer. To compute 

$$
P (K | C) = \frac {P (K C)}{P (C)}
$$

we first note that 

$$
\begin{array}{r l} P (K C) & = P (K) P (C | K) \\ & = p \cdot 1 \\ & = p \end{array}
$$

To compute the probability that the student answers correctly, we condition on whether or not she knows the answer. That is, 

$$
\begin{array}{c} {P (C) = P (C | K) P (K) + P (C | K ^ {c}) P (K ^ {c})} \\ {= p + (1 / m) (1 - p)} \end{array}
$$

Hence, the desired probability is given by 

$$
P (K | C) = \frac {p}{p + (1 / m) (1 - p)} = \frac {m p}{1 + (m - 1) p}
$$

Thus, for example, if$\begin{array} { r } { m = 5 , p = \frac { 1 } { 2 } } \end{array}$ , then the probability that a student knew the answer to a question she correctly answered is ${ \frac { 5 } { 6 } } .$ . ■ 

EXAMPLE 3.7d A laboratory blood test is 99 percent effective in detecting a certain disease when it is, in fact, present. However, the test also yields a “false positive” result for 1 percent of the healthy persons tested. (That is, if a healthy person is tested, then, with probability .01, the test result will imply he or she has the disease.) If .5 percent of the population actually has the disease, what is the probability a person has the disease given that his test result is positive? 

SOLUTION Let D be the event that the tested person has the disease and E the event that his test result is positive. The desired probability $P ( D | E )$ is obtained by 

$$
\begin{array}{r l} P (D | E) & = \frac {P (D E)}{P (E)} \\ & = \frac {P (E | D) P (D)}{P (E | D) P (D) + P (E | D ^ {c}) P (D ^ {c})} \\ & = \frac {(. 9 9) (. 0 0 5)}{(. 9 9) (. 0 0 5) + (. 0 1) (. 9 9 5)} \\ & = . 3 3 2 2 \end{array}
$$

Thus, only 33 percent of those persons whose test results are positive actually have the disease. Since many students are often surprised at this result (because they expected this figure to be much higher since the blood test seems to be a good one), it is probably worthwhile to present a second argument which, though less rigorous than the foregoing, is probably more revealing. We now do so. 

Since .5 percent of the population actually has the disease, it follows that, on the average, 1 person out of every 200 tested will have it. The test will correctly confirm that this person has the disease with probability .99. Thus, on the average, out of every 200 persons tested, the test will correctly confirm that .99 person has the disease. On the other hand, out of the (on the average) 199 healthy people, the test will incorrectly state that (199) (.01) of these people have the disease. Hence, for every .99 diseased person that the test correctly states is ill, there are (on the average) 1.99 healthy persons that the test incorrectly states are ill. Hence, the proportion of time that the test result is correct when it states that a person is ill is 

$$
\frac {. 9 9}{. 9 9 + 1 . 9 9} = . 3 3 2 2 \quad \blacksquare
$$

Equation 3.7.1 is also useful when one has to reassess one’s (personal) probabilities in the light of additional information. For instance, consider the following examples. 

EXAMPLE 3.7e At a certain stage of a criminal investigation, the inspector in charge is 60 percent convinced of the guilt of a certain suspect. Suppose now that a new piece of evidence that shows that the criminal has a certain characteristic (such as left-handedness, baldness, brown hair, etc.) is uncovered. If 20 percent of the population possesses thi characteristic, how certain of the guilt of the suspect should the inspector now be if it turns out that the suspect is among this group? 

SOLUTION Letting G denote the event that the suspect is guilty and C the event that he possesses the characteristic of the criminal, we have 

$$
P (G | C) = \frac {P (G C)}{P (C)}
$$

Now 

$$
\begin{array}{r l} & P (G C) = P (G) P (C | G) \\ & \qquad = (. 6) (1) \\ & \qquad = . 6 \end{array}
$$

To compute the probability that the suspect has the characteristic, we condition on whether or not he is guilty. That is, 

$$
\begin{array}{r l} P (C) & = P (C | G) P (G) + P (C | G ^ {c}) P (G ^ {c}) \\ & = (1) (. 6) + (. 2) (. 4) \\ & = . 6 8 \end{array}
$$

where we have supposed that the probability of the suspect having the characteristic if he is, in fact, innocent is equal to .2, the proportion of the population possessing the characteristic. Hence 

$$
P (G | C) = \frac {6 0}{6 8} = . 8 8 2
$$

and so the inspector should now be 88 percent certain of the guilt of the suspect. ■ 

EXAMPLE 3.7e (continued) Let us now suppose that the new evidence is subject to different possible interpretations, and in fact only shows that it is 90 percent likely that the criminal possesses this certain characteristic. In this case, how likely would it be that the suspect is guilty (assuming, as before, that he has this characteristic)? 

SOLUTION In this case, the situation is as before with the exception that the probability of the suspect having the characteristic given that he is guilty is now .9 (rather than 1). Hence, 

$$
\begin{array}{c} P (G | C) = \frac {P (G C)}{P (C)} \\ = \frac {P (G) P (C | G)}{P (C | G) P (G) + P (C | G ^ {c}) P (G ^ {c})} \end{array}
$$

$$
\begin{array}{l} = \frac {(. 6) (. 9)}{(. 9) (. 6) + (. 2) (. 4)} \\ = \frac {5 4}{6 2} = . 8 7 1 \end{array}
$$

which is slightly less than in the previous case (why?). ■ 

Equation 3.7.1 may be generalized in the following manner. Suppose that $F _ { 1 } , F _ { 2 } , \ldots , F _ { n }$ are mutually exclusive events such that 

$$
\bigcup_ {i = 1} ^ {n} F _ {i} = S
$$

In other words, exactly one of the events $F _ { 1 } , F _ { 2 } , \ldots , F _ { n }$ must occur. By writing 

$$
E = \bigcup_ {i = 1} ^ {n} E F _ {i}
$$

and using the fact that the events $E F _ { i } , i = 1 , \dots , n$ are mutually exclusive, we obtain that 

$$
\begin{array}{c} P (E) = \sum_ {i = 1} ^ {n} P (E F _ {i}) \\ = \sum_ {i = 1} ^ {n} P (E | F _ {i}) P (F _ {i}) \end{array}\tag{3.7.2}
$$

Thus, Equation 3.7.2 shows how, for given events $F _ { 1 } , F _ { 2 } , \ldots , F _ { n }$ of which one and only one must occur, we can compute $P ( E )$ by first “conditioning” on which one of the $F _ { i }$ occurs. That is, it states that $P ( E )$ is equal to a weighted average of $P ( E | F _ { i } )$ , each term being weighted by the probability of the event on which it is conditioned 

Suppose now that $E$ has occurred and we are interested in determining which one of $F _ { j }$ also occurred. By Equation 3.7.2, we have that 

$$
\begin{array}{c} P (F _ {j} | E) = \frac {P (E F _ {j})}{P (E)} \\ = \frac {P (E | F _ {j}) P (F _ {j})}{\sum_ {i = 1} ^ {n} P (E | F _ {i}) P (F _ {i})} \end{array}\tag{3.7.3}
$$

Equation 3.7.3 is known as Bayes’ formula, after the English philosopher Thomas Bayes. If we think of the events $F _ { j }$ as being possible “hypotheses” about some subject matter, then 

Bayes’ formula may be interpreted as showing us how opinions about these hypotheses held before the experiment [that is, the $P ( F _ { j } ) ]$ ] should be modified by the evidence of the experiment. 

EXAMPLE 3.7f A plane is missing and it is presumed that it was equally likely to have gone down in any of three possible regions. Let $1 - \alpha _ { i }$ denote the probability the plane will be found upon a search of the ith region when the plane ${ \mathrm { i } } s ,$ in fact, in that region,$i = 1 , 2 , 3$ . (The constants$\alpha _ { i }$ are called overlook probabilities because they represent the probability of overlooking the plane; they are generally attributable to the geographical and environmental conditions of the regions.) What is the conditional probability that the plane is in the ith region, given that a search of region 1 is unsuccessful,$i = 1 , 2 , 3 ?$ 

SOLUTION Let $R _ { i } , i = 1 , 2 , 3$ , be the event that the plane is in region i; and let E be the event that a search of region 1 is unsuccessful. From Bayes’ formula, we obtain 

$$
\begin{array}{l} P (R _ {1} | E) = \frac {P (E R _ {1})}{P (E)} \\ \qquad = \frac {P (E | R _ {1}) P (R _ {1})}{\sum_ {i = 1} ^ {3} P (E | R _ {i}) P (R _ {i})} \\ \qquad = \frac {(\alpha_ {1}) (1 / 3)}{(\alpha_ {1}) (1 / 3) + (1) (1 / 3) + (1) (1 / 3)} \\ \qquad = \frac {\alpha_ {1}}{\alpha_ {1} + 2} \end{array}
$$

For $j = 2 ,$ 3, 

$$
\begin{array}{r l} P (R _ {j} | E) & = \frac {P (E | R _ {j}) P (R _ {j})}{P (E)} \\ & = \frac {(1) (1 / 3)}{(\alpha_ {1}) 1 / 3 + 1 / 3 + 1 / 3} \\ & = \frac {1}{\alpha_ {1} + 2}, \qquad j = 2, 3 \end{array}
$$

Thus, for instance, if$\alpha _ { 1 } = . 4 _ { \mathrm { : } }$ , then the conditional probability that the plane is in region 1 given that a search of that region did not uncover it is ${ \frac { 1 } { 6 } } .$ . ■ 

## 3.8 INDEPENDENT EVENTS

The previous examples in this chapter show that $P ( E | F )$ , the conditional probability of $E$ given $F ,$ is not generally equal to $P ( E )$ ), the unconditional probability of E. In other words, knowing that F has occurred generally changes the chances of $E ' s$ occurrence. In the special cases where $P ( E | F )$ does in fact equal $P ( E )$ ), we say that E is independent of F. That is, E is independent of F if knowledge that F has occurred does not change the probability that E occurs. 

Since $P ( E | F ) = P ( E F ) / P ( F )$ , we see that E is independent of F if 

$$
P (E F) = P (E) P (F)\tag{3.8.1}
$$

Since this equation is symmetric in E and F, it shows that whenever E is independent of F so is F of E. We thus have the following. 

## Definition

Two events E and F are said to be independent if Equation 3.8.1 holds. Two events E and F that are not independent are said to be dependent. 

EXAMPLE 3.8a A card is selected at random from an ordinary deck of 52 playing cards. If A is the event that the selected card is an ace and H is the event that it is a heart, then A and H are independent, since$\begin{array} { r } { P ( A H ) = \frac { 1 } { 5 2 } } \end{array}$ , while$\textstyle P ( A ) = { \frac { 4 } { 5 2 } }$ and$\begin{array} { r } { P ( H ) = \frac { 1 3 } { 5 2 } } \end{array}$ ■ 

EXAMPLE 3.8b If we let E denote the event that the next president is a Republican and F the event that there will be a major earthquake within the next year, then most people would probably be willing to assume that E and F are independent. However, there would probably be some controversy over whether it is reasonable to assume that E is independent of G, where G is the event that there will be a recession within the next two years. ■ 

We now show that if E is independent of F then E is also independent of $F ^ { c }$ . 

PROPOSITION 3.8.1 If E and F are independent, then so are E and $F ^ { c }$ . 

## Proof

Assume that E and F are independent. Since $E = E F \cup E F ^ { c }$ , and EF and $E F ^ { c }$ are obviously mutually exclusive, we have that 

$$
\begin{array}{r l} P (E) & = P (E F) + P (E F ^ {c}) \\ & = P (E) P (F) + P (E F ^ {c}) \quad \text { by   the   independence   of } E \text { and } F \end{array}
$$

or equivalently, 

$$
\begin{array}{c} {P (E F ^ {c}) = P (E) (1 - P (F))} \\ {= P (E) P (F ^ {c})} \end{array}
$$

and the result is proven.  

Thus if E is independent of $F ,$ then the probability of $E ' s$ occurrence is unchanged by information as to whether or not $F$ has occurred. 

Suppose now that E is independent of $F$ and is also independent of $G .$ Is E then necessarily independent of $F G ?$ The answer, somewhat surprisingly, is no. Consider the following example. 

EXAMPLE 3.8c Two fair dice are thrown. Let $E _ { 7 }$ denote the event that the sum of the dice is 7. Let F denote the event that the first die equals 4 and let $T$ be the event that the second die equals 3. Now it can be shown (see Problem 36) that $E _ { 7 }$ is independent of F and that $E _ { 7 }$ is also independent of $T ;$ but clearly $E _ { 7 }$ is not independent of $F T$ [since $P ( E _ { 7 } | F T ) = 1 ]$ ■ 

It would appear to follow from the foregoing example that an appropriate definition of the independence of three events E, F, and $G$ would have to go further than merely assuming that all of the$\binom { 3 } { 2 }$ pairs of events are independent. We are thus led to the following definition. 

## Definition

The three events E, F, and G are said to be independent if 

$$
\begin{array}{c} {P (E F G) = P (E) P (F) P (G)} \\ {P (E F) = P (E) P (F)} \\ {P (E G) = P (E) P (G)} \\ {P (F G) = P (F) P (G)} \end{array}
$$

It should be noted that if the events E, F, G are independent, then E will be independent of any event formed from $F$ and G. For instance, E is independent of $F \cup G$ since 

$$
\begin{array}{r l} & P (E (F \cup G)) = P (E F \cup E G) \\ & \qquad = P (E F) + P (E G) - P (E F G) \\ & \qquad = P (E) P (F) + P (E) P (G) - P (E) P (F G) \\ & \qquad = P (E) [ P (F) + P (G) - P (F G) ] \\ & \qquad = P (E) P (F \cup G) \end{array}
$$

Of course we may also extend the definition of independence to more than three events. The events $E _ { 1 } , E _ { 2 } , \ldots , E _ { n }$ are said to be independent if for every subset $E _ { 1 ^ { \prime } } , E _ { 2 ^ { \prime } } , \ldots , E _ { r ^ { \prime } } , r \leq n _ { ! }$ , of these events 

$$
P (E _ {1 ^ {\prime}} E _ {2 ^ {\prime}} \cdot \cdot \cdot E _ {r ^ {\prime}}) = P (E _ {1 ^ {\prime}}) P (E _ {2 ^ {\prime}}) \cdot \cdot \cdot P (E _ {r ^ {\prime}})
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/caa38dcbcec1f6283bd404ec03a8228e93fdb49cd6e5df85ec23e25db7a788b0.jpg)



FIGURE 3.7 Parallel system: functions if current flows from A to B.


It is sometimes the case that the probability experiment under consideration consists of performing a sequence of subexperiments. For instance, if the experiment consists of continually tossing a coin, then we may think of each toss as being a subexperiment. In many cases it is reasonable to assume that the outcomes of any group of the subexperiment have no effect on the probabilities of the outcomes of the other subexperiments. If such is the case, then we say that the subexperiments are independent. 

EXAMPLE 3.8d A system composed of n separate components is said to be a parallel system if it functions when at least one of the components functions. (See Figure 3.7.) For such a system, if component i, independent of other components, functions with probability $p _ { i } , i = 1 , \ldots , n ,$ what is the probability the system functions? 

SOLUTION Let $A _ { i }$ denote the event that component i functions. Then 

$$
\begin{array}{l} P \{\text {system functions} \} = 1 - P \{\text {system does not function} \} \\ \qquad = 1 - P \{\text {all components do not function} \} \\ \qquad = 1 - P \big (A _ {1} ^ {c} A _ {2} ^ {c} \dots A _ {n} ^ {c} \big) \\ \qquad = 1 - \prod_ {i = 1} ^ {n} (1 - p _ {i}) \quad \text {by independence} \end{array}
$$

EXAMPLE 3.8e A set of k coupons, each of which is independently a type $j$ coupon with probability$\begin{array} { r } { p _ { j } , \sum _ { j = 1 } ^ { n } \ p _ { j } \ = \ 1 } \end{array}$ , is collected. Find the probability that the set contains a type j coupon given that it contains a type $i , i \neq j$ 

SOLUTION Let $A _ { r }$ be the event that the set contains a type r coupon. Then 

$$
P (A _ {j} | A _ {i}) = \frac {P (A _ {j} A _ {i})}{P (A _ {i})}
$$

To compute $P ( A _ { i } )$ and $P ( A _ { j } A _ { i } )$ , consider the probability of their complements: 

$$
\begin{array}{r l} & P (A _ {i}) = 1 - P (A _ {i} ^ {c}) \\ & \quad = 1 - P \{\text {no coupon is type} i \} \\ & \quad = 1 - (1 - p _ {i}) ^ {k} \end{array}
$$

$$
\begin{array}{r l} & P (A _ {i} A _ {j}) = 1 - P (A _ {i} ^ {c} \cup A _ {j} ^ {c}) \\ & \quad = 1 - [ P (A _ {i} ^ {c}) + P (A _ {j} ^ {c}) - P (A _ {i} ^ {c} A _ {j} ^ {c}) ] \\ & \quad = 1 - (1 - p _ {i}) ^ {k} - (1 - p _ {j}) ^ {k} + P \{\text { no   coupon   is   type } i \text { or   type } j \} \\ & \quad = 1 - (1 - p _ {i}) ^ {k} - (1 - p _ {j}) ^ {k} + (1 - p _ {i} - p _ {j}) ^ {k} \end{array}
$$

where the final equality follows because each of the k coupons is, independently, neither of type i or of type j with probability $1 - p _ { i } - p _ { j }$ . Consequently, 

$$
P (A _ {j} | A _ {i}) = \frac {1 - (1 - p _ {i}) ^ {k} - (1 - p _ {j}) ^ {k} + (1 - p _ {i} - p _ {j}) ^ {k}}{1 - (1 - p _ {i}) ^ {k}} \quad \blacksquare
$$

## Problems

1. A box contains three marbles — one red, one green, and one blue. Consider an experiment that consists of taking one marble from the box, then replacing it in the box and drawing a second marble from the box. Describe the sample space. Repeat for the case in which the second marble is drawn without first replacing the first marble. 

2. An experiment consists of tossing a coin three times. What is the sample space of this experiment? Which event corresponds to the experiment resulting in more heads than tails? 

3. Let $S = \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 \} , E = \{ 1 , 3 , 5 , 7 \} , F = \{ 7 , 4 , 6 \} , G = \{ 1 , 4 \}$ . Find (a) EF; (c)$E G ^ { c } ;$ (e)$E ^ { c } ( F \cup G )$ ; (b)$E \cup F G ,$ (d)$E F ^ { c } \cup G ;$ (f )$E G \cup F G .$ 

4. Two dice are thrown. Let E be the event that the sum of the dice is odd, let F be the event that the first die lands on 1, and let G be the event that the sum is 5. Describe the events EF $E \cup F , F G , E F ^ { c } , E F G .$ 

5. A system is composed of four components, each of which is either working or failed. Consider an experiment that consists of observing the status of each component, and let the outcome of the experiment be given by the vector $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } )$ where x<sub>i</sub> is equal to 1 if component i is working and is equal to 0 if component i is failed. 

(a) How many outcomes are in the sample space of this experiment? 

(b) Suppose that the system will work if components 1 and 2 are both working, or if components 3 and 4 are both working. Specify all the outcomes in the event that the system works. 

(c) Let E be the event that components 1 and 3 are both failed. How many outcomes are contained in event E ? 

## Problems

6. Let E, F, G be three events. Find expressions for the events that of E, F, G 

(a) only E occurs; 

(b) both E and G but not F occur; 

(c) at least one of the events occurs; 

(d) at least two of the events occur; 

(e) all three occur; 

(f ) none of the events occurs; 

(g) at most one of them occurs; 

(h) at most two of them occur; 

(i) exactly two of them occur; 

( j) at most three of them occur. 

7. Find simple expressions for the events 

(a)$E \cup E ^ { c } ;$ 

(b)$E E ^ { c } ;$ 

(c)$( E \cup F ) ( E \cup F ^ { c } ) ;$ 

(d)$( E \cup F ) ( E ^ { c } \cup F ) E \cup F ^ { c } ) ;$ 

(e)$( E \cup F ) ( F \cup G ) .$ 

8. Use Venn diagrams (or any other method) to show that 

(a)$E F \subset E , E \subset E \cup F ;$ 

(b)$\mathsf { i f } E \subset F \mathrm { ~ t h e n ~ } F ^ { c } \subset E ^ { c } ;$ 

(c) the commutative laws are valid; 

(d) the associative laws are valid; 

(e)$F = F E \cup F E ^ { c } ;$ 

(f )$E \cup F = E \cup E ^ { c } F ;$ 

(g) DeMorgan’s laws are valid. 

9. For the following Venn diagram, describe in terms of E, F, and G the events denoted in the diagram by the Roman numerals I through VII. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/c538e5321e194847fee6158dcba932ea4282d4d7ed7f9f7c31d1517ab210ddec.jpg)


10. Show that if $E \subset F$ then $P ( E ) \leq P ( F )$ . (Hint: Write F as the union of two mutually exclusive events, one of them being E.) 

11. Prove Boole’s inequality, namely that 

$$
P \left(\bigcup_ {i = 1} ^ {n} E _ {i}\right) \leq \sum_ {i = 1} ^ {n} P (E _ {i})
$$

12. If $P ( E ) ~ = ~ . 9$ and $P ( F ) ~ = ~ . 9  \it$ , show that $P ( E F ) \ge . 8$ . In general, prove Bonferroni’s inequality, namely that 

$$
P (E F) \geq P (E) + P (F) - 1
$$

13. Prove that 

(a)$P ( E F ^ { c } ) = P ( E ) - P ( E F )$ 

(b)$P ( E ^ { c } F ^ { c } ) = 1 - P ( E ) - P ( F ) + P ( E F )$ 

14. Show that the probability that exactly one of the events E or F occurs is equal to $P ( E ) + P ( F ) - 2 P ( E F )$ 

15. Calculate ${ \binom { 9 } { 3 } } , { \binom { 9 } { 6 } } , { \binom { 7 } { 2 } } , { \binom { 7 } { 5 } } , { \binom { 1 0 } { 7 } }$ 

16. Show that 

$$
\binom{n}{r} = \binom{n}{n - r}
$$

Now present a combinatorial argument for the foregoing by explaining why a choice of r items from a set of size n is equivalent to a choice of $n - r$ items from that set. 

17. Show that 

$$
\binom {n} {r} = \binom {n - 1} {r - 1} + \binom {n - 1} {r}
$$

For a combinatorial argument, consider a set of n items and fix attention on one of these items. How many different sets of size r contain this item, and how many do not? 

18. A group of 5 boys and 10 girls is lined up in random order — that is, each of the 15! permutations is assumed to be equally likely. 

(a) What is the probability that the person in the 4th position is a boy? 

(b) What about the person in the 12th position? 

(c) What is the probability that a particular boy is in the 3rd position? 

19. Consider a set of 23 unrelated people. Because each pair of people shares the same birthday with probability 1/365, and there are ${ \binom { 2 3 } { 2 } } = 2 5 3$ pairs, why isn’t the probability that at least two people have the same birthday equal to 253/365? 

20. A town contains 4 television repairmen. If 4 sets break down, what is the probabil ity that exactly 2 of the repairmen are called? What assumptions are you making? 

21. A woman has n keys, of which one will open her door. If she tries the keys at random, discarding those that do not work, what is the probability that she will open the door on her kth try? What if she does not discard previously tried keys? 

22. A closet contains 8 pairs of shoes. If 4 shoes are randomly selected, what is the probability that there will be (a) no complete pair and (b) exactly 1 complete pair? 

23. Of three cards, one is painted red on both sides; one is painted black on both sides; and one is painted red on one side and black on the other. A card is randomly chosen and placed on a table. If the side facing up is red, what is the probability that the other side is also red? 

24. A couple has 2 children. What is the probability that both are girls if the eldest is a girl? 

25. Fifty-two percent of the students at a certain college are females. Five percent of the students in this college are majoring in computer science. Two percent of the students are women majoring in computer science. If a student is selected at random, find the conditional probability that 

(a) this student is female, given that the student is majoring in computer science; (b) this student is majoring in computer science, given that the student is female. 

26. A total of 500 married working couples were polled about their annual salaries, with the following information resulting. 

<table><tr><td rowspan="2">Wife</td><td colspan="2">Husband</td></tr><tr><td>Less than $25,000</td><td>More than $25,000</td></tr><tr><td>Less than $25,000</td><td>212</td><td>198</td></tr><tr><td>More than $25,000</td><td>36</td><td>54</td></tr></table>

Thus, for instance, in 36 of the couples the wife earned more and the husband earned less than $25,000. If one of the couples is randomly chosen, what is 

(a) the probability that the husband earns less than $25,000; 

(b) the conditional probability that the wife earns more than $25,000 given that the husband earns more than this amount; 

(c) the conditional probability that the wife earns more than $25,000 given that the husband earns less than this amount? 

27. There are two local factories that produce radios. Each radio produced at factory A is defective with probability .05, whereas each one produced at factory B is defective with probability .01. Suppose you purchase two radios that were produced at the same factory, which is equally likely to have been either factory A or factory B. If the first radio that you check is defective, what is the conditional probability that the other one is also defective? 

28. A red die, a blue die, and a yellow die (all six-sided) are rolled. We are interested in the probability that the number appearing on the blue die is less than that appearing on the yellow die which is less than that appearing on the red die. (That is, if B (R) [Y ] is the number appearing on the blue (red) [yellow] die, then we are interested in $P ( B < Y < R )$ . ) 

(a) What is the probability that no two of the dice land on the same number? 

(b) Given that no two of the dice land on the same number, what is the conditional probability that $B < Y < R \Rsh$ 

(c) What is $P ( B < Y < R ) \vdots$ 

(d) If we regard the outcome of the experiment as the vector B, R, Y, how many outcomes are there in the sample space? 

(e) Without using the answer to (c), determine the number of outcomes that result in $B < Y < R$ 

(f ) Use the results of parts (d) and (e) to verify your answer to part (c). 

29. You ask your neighbor to water a sickly plant while you are on vacation. Without water it will die with probability .8; with water it will die with probability .15. You are 90 percent certain that your neighbor will remember to water the plant. 

(a) What is the probability that the plant will be alive when you return? 

(b) If it is dead, what is the probability your neighbor forgot to water it? 

30. Two balls, each equally likely to be colored either red or blue, are put in an urn. At each stage one of the balls is randomly chosen, its color is noted, and it is then returned to the urn. If the first two balls chosen are colored red, what is the probability that 

(a) both balls in the urn are colored red; 

(b) the next ball chosen will be red? 

31. A total of 600 of the 1,000 people in a retirement community classify themselves as Republicans, while the others classify themselves as Democrats. In a local election in which everyone voted, 60 Republicans voted for the Democratic candidate, and 50 Democrats voted for the Republican candidate. If a randomly chosen community member voted for the Republican, what is the probability that she or he is a Democrat? 

32. Each of 2 balls is painted black or gold and then placed in an urn. Suppose that each ball is colored black with probability <sup>1</sup> , and that these events are independent. 

(a) Suppose that you obtain information that the gold paint has been used (and thus at least one of the balls is painted gold). Compute the conditional probability that both balls are painted gold. 

(b) Suppose, now, that the urn tips over and 1 ball falls out. It is painted gold. What is the probability that both balls are gold in this case? Explain. 

33. Each of 2 cabinets identical in appearance has 2 drawers. Cabinet A contains a silver coin in each drawer, and cabinet B contains a silver coin in one of its drawers and a gold coin in the other. A cabinet is randomly selected, one of its drawers is opened, and a silver coin is found. What is the probability that there is a silver coin in the other drawer? 

34. Prostate cancer is the most common type of cancer found in males. As an indicator of whether a male has prostate cancer, doctors often perform a test that measures the level of the PSA protein (prostate specific antigen) that is produced only by the prostate gland. Although higher PSA levels are indicative of cancer, the test is notoriously unreliable. Indeed, the probability that a noncancerous man will have an elevated PSA level is approximately .135, with this probability increasing to approximately .268 if the man does have cancer. If, based on other factors, a physician is 70 percent certain that a male has prostate cancer, what is the conditional probability that he has the cancer given that 

(a) the test indicates an elevated PSA level; 

(b) the test does not indicate an elevated PSA level? 

Repeat the preceding, this time assuming that the physician initially believes there is a 30 percent chance the man has prostate cancer. 

35. Suppose that an insurance company classifies people into one of three classes — good risks, average risks, and bad risks. Their records indicate that the probabilities that good, average, and bad risk persons will be involved in an accident over a 1-year span are, respectively, .05, .15, and .30. If 20 percent of the population are “good risks,” 50 percent are “average risks,” and 30 percent are “bad risks,” what proportion of people have accidents in a fixed year? If policy holder A had no accidents in 1987, what is the probability that he or she is a good (average) risk? 

36. A pair of fair dice is rolled. Let E denote the event that the sum of the dice is equal to 7. 

(a) Show that E is independent of the event that the first die lands on 4. (b) Show that E is independent of the event that the second die lands on 3. 

37. The probability of the closing of the ith relay in the circuits shown is given by$\mathbf { \Delta } _ { p { i } } , { i } = 1 , 2 , 3 , 4 , 5$ . If all relays function independently, what is the probability that a current flows between A and B for the respective circuits? 

38. An engineering system consisting of n components is said to be a k-out-of n system$\left( k \ \leq \ n \right)$ if the system functions if and only if at least k of the n components function. Suppose that all components function independently of each other. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/3864db524bc1917b99c227ebcff0d2bcfef7fd35ea63ab05b11358da2d24e045.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/0460829353ef97530aecaba3063925e34255d28429312fa031e03725079edfdd.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/9cb1eb4034665234f86b6ecd0c2a1c5a15698db5eb563adb83bd18c84dc727ef.jpg)



(c)


(a) If the ith component functions with probability $P _ { i } , i = 1 , 2 , 3 , 4 ,$ , compute the probability that a 2-out-of-4 system functions. 

(b) Repeat (a) for a 3-out-of-5 system. 

39. Five independent flips of a fair coin are made. Find the probability that 

(a) the first three flips are the same; 

(b) either the first three flips are the same, or the last three flips are the same; 

(c) there are at least two heads among the first three flips, and at least two tails among the last three flips. 

40. Suppose that n independent trials, each of which results in any of the outcomes 0, 1, or 2, with respective probabilities .3, .5, and .2, are performed. Find the probability that both outcome 1 and outcome 2 occur at least once. (Hint: Consider the complementary probability.) 

41. A parallel system functions whenever at least one of its components works. Consider a parallel system of n components, and suppose that each component independently works with probability <sup>1</sup> . Find the conditional probability that component 1 works, given that the system is functioning. 

42. A certain organism possesses a pair of each of 5 different genes (which we will designate by the first 5 letters of the English alphabet). Each gene appears in 2 forms (which we designate by lowercase and capital letters). The capital letter will be assumed to be the dominant gene in the sense that if an organism possesses the gene pair xX, then it will outwardly have the appearance of the X gene. For instance, if X stands for brown eyes and x for blue eyes, then an individual having either gene pair XX or xX will have brown eyes, whereas one having gene pair xx will be blue-eyed. The characteristic appearance of an organism is called its phenotype, whereas its genetic constitution is called its genotype. (Thus 2 organisms with respective genotypes aA, bB, cc, dD, ee and AA, BB, cc, DD, ee would have different genotypes but the same phenotype.) In a mating between 2 organisms each one contributes, at random, one of its gene pairs of each type. The 5 contributions of an organism (one of each of the 5 types) are assumed to be independent and are also independent of the contributions of its mate. In a mating between organisms having genotypes aA, bB,$c C ,$ dD, eE, and aa, bB, cc, Dd, ee, what is the probability that the progeny will (1) phenotypically, (2) genotypically resemble 

(a) the first parent; 

(b) the second parent; 

(c) either parent; 

(d) neither parent? 

43. Three prisoners are informed by their jailer that one of them has been chosen at random to be executed, and the other two are to be freed. Prisoner A asks the jailer to tell him privately which of his fellow prisoners will be set free, claiming that there would be no harm in divulging this information because he already knows that at least one of the two will go free. The jailer refuses to answer this question, pointing out that if A knew which of his fellow prisoners were to be set free, then his own probability of being executed would rise from$\frac 1 3$ to$\frac { 1 } { 2 }$ because he would then be one of two prisoners. What do you think of the jailer’s reasoning? 

44. Although both my parents have brown eyes, I have blue eyes. What is the probability that my sister has blue eyes? 

45. A set of k coupons, each of which is independently a type j coupon with probability p<sub>j</sub> ,$\textstyle \sum _ { j = 1 } ^ { n } p _ { j } = 1$ , is collected. Find the probability that the set contains eithe a type i or a type j coupon. 

This Page Intentionally Left Blank 

# RANDOM VARIABLES AND EXPECTATION

## 4.1 RANDOM VARIABLES

When a random experiment is performed, we are often not interested in all of the detail of the experimental result but only in the value of some numerical quantity determined by the result. For instance, in tossing dice we are often interested in the sum of the two dice and are not really concerned about the values of the individual dice. That is, we may be interested in knowing that the sum is 7 and not be concerned over whether the actual outcome was (1, 6) or (2, 5) or (3, 4) or (4, 3) or (5, 2) or (6, 1). Also, a civil engineer may not be directly concerned with the daily risings and declines of the water level of a reservoir (which we can take as the experimental result) but may only care about the level at the end of a rainy season. These quantities of interest that are determined by the result of the experiment are known as random variables. 

Since the value of a random variable is determined by the outcome of the experiment, we may assign probabilities of its possible values. 

EXAMPLE 4.1a Letting X denote the random variable that is defined as the sum of two fair dice, then 

$$
\begin{array}{r l} & P \{X = 2 \} = P \{(1, 1) \} = \frac {1}{3 6} \\ & P \{X = 3 \} = P \{(1, 2), (2, 1) \} = \frac {2}{3 6} \\ & P \{X = 4 \} = P \{(1, 3), (2, 2), (3, 1) \} = \frac {3}{3 6} \\ & P \{X = 5 \} = P \{(1, 4), (2, 3), (3, 2), (4, 1) \} = \frac {4}{3 6} \\ & P \{X = 6 \} = P \{(1, 5), (2, 4), (3, 3), (4, 2), (5, 1) \} = \frac {5}{3 6} \\ & P \{X = 7 \} = P \{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1) \} = \frac {6}{3 6} \end{array}\tag{4.1.1}
$$

$$
P \{X = 8 \} = P \{(2, 6), (3, 5), (4, 4), (5, 3), (6, 2) \} = \frac {5}{3 6}
$$

$$
P \{X = 9 \} = P \{(3, 6), (4, 5), (5, 4), (6, 3) \} = \frac {4}{3 6}
$$

$$
P \{X = 1 0 \} = P \{(4, 6), (5, 5), (6, 4) \} = \frac {3}{3 6}
$$

$$
P \{X = 1 1 \} = P \{(5, 6), (6, 5) \} = \frac {2}{3 6}
$$

$$
P \{X = 1 2 \} = P \{(6, 6) \} = \frac {1}{3 6}
$$

In other words, the random variable X can take on any integral value between 2 and 12 and the probability that it takes on each value is given by Equation 4.1.1. Since X must take on some value, we must have 

$$
1 = P (S) = P \left(\bigcup_ {i = 2} ^ {1 2} \{X = i \}\right) = \sum_ {i = 2} ^ {1 2} P \{X = i \}
$$

which is easily verified from Equation 4.1.1. 

Another random variable of possible interest in this experiment is the value of the first die. Letting Y denote this random variable, then Y is equally likely to take on any of the values 1 through 6. That is, 

$$
P \{Y = i \} = 1 / 6, \qquad i = 1, 2, 3, 4, 5, 6
$$

EXAMPLE 4.1b Suppose that an individual purchases two electronic components each of which may be either defective or acceptable. In addition, suppose that the four possible results $- \ ( d , d ) , \ ( d , a ) , \ ( a , \ d ) , \ ( a , \ a )$ — have respective probabilities .09, .21, .21, .49 [where (d, d ) means that both components are defective, (d, a) that the first component is defective and the second acceptable, and so on]. If we let X denote the number of acceptable components obtained in the purchase, then X is a random variable taking on one of the values 0, 1, 2 with respective probabilities 

$$
\begin{array}{l} {P \{X = 0 \} = . 0 9} \\ {P \{X = 1 \} = . 4 2} \\ {P \{X = 2 \} = . 4 9} \end{array}
$$

If we were mainly concerned with whether there was at least one acceptable component, we could define the random variable I by 

$$
I = \left\{ \begin{array}{l l} 1 & \text { if } X = 1 \text { or } 2 \\ 0 & \text { if } X = 0 \end{array} \right.
$$

If A denotes the event that at least one acceptable component is obtained, then the random variable I is called the indicator random variable for the event A, since I will equal 

## 4.1 Random Variables

or 0 depending upon whether A occurs. The probabilities attached to the possible values of I are 

$$
\begin{array}{l} P \{I = 1 \} = . 9 1 \\ P \{I = 0 \} = . 0 9 \end{array}
$$

In the two foregoing examples, the random variables of interest took on a finite number of possible values. Random variables whose set of possible values can be written either as a finite sequence $x _ { 1 } , \ldots , x _ { n } ,$ , or as an infinite sequence $x _ { 1 } , . . .$ . are said to be discrete. For instance, a random variable whose set of possible values is the set of nonnegative integers is a discrete random variable. However, there also exist random variables that take on a continuum of possible values. These are known as continuous random variables. One example is the random variable denoting the lifetime of a car, when the car’s lifetime is assumed to take on any value in some interval $( a , b )$ 

The cumulative distribution function, or more simply the distribution function, F of the random variable X is defined for any real number x by 

$$
F (x) = P \{X \leq x \}
$$

That is,$F ( x )$ is the probability that the random variable X takes on a value that is less than or equal to x. 

Notation: We will use the notation $X \sim F$ to signify that F is the distribution function of X . 

All probability questions about X can be answered in terms of its distribution function F . For example, suppose we wanted to compute $P \{ a < X \leq b \}$ }. This can be accomplished by first noting that the event$\{ X \leq b \}$ can be expressed as the union of the two mutually exclusive events$\{ X \leq a \}$ and$\{ a < X \leq b \}$ . Therefore, applying Axiom 3, we obtain that 

$$
P \{X \leq b \} = P \{X \leq a \} + P \{a <   X \leq b \}
$$

or 

$$
P \{a <   X \leq b \} = F (b) - F (a)
$$

EXAMPLE 4.1c Suppose the random variable X has distribution function 

$$
F (x) = \left\{ \begin{array}{l l} 0 & x \leq 0 \\ 1 - \exp \{- x ^ {2} \} & x > 0 \end{array} \right.
$$

What is the probability that X exceeds 1? 

SOLUTION The desired probability is computed as follows: 

$$
\begin{array}{r l} P \{X > 1 \} & = 1 - P \{X \leq 1 \} \\ & = 1 - F (1) \\ & = e ^ {- 1} \\ & = . 3 6 8 \quad \blacksquare \end{array}
$$

## 4.2 TYPES OF RANDOM VARIABLES

As was previously mentioned, a random variable whose set of possible values is a sequence is said to be discrete. For a discrete random variable X , we define the probability mass function $p ( a )$ of X by 

$$
p (a) = P \{X = a \}
$$

The probability mass function $p ( a )$ is positive for at most a countable number of values of ${ \dot { \mathbf { \theta } } } _ { a . }$ That is, if X must assume one of the values $x _ { 1 } , x _ { 2 } , \dotsc , x _ { 2 } ,$ , then 

$$
\begin{array}{l l} p (x _ {i}) > 0, & \quad i = 1, 2, \ldots \\ p (x) = 0, & \quad \text { all   other   values   of } x \end{array}
$$

Since X must take on one of the values $x _ { i }$ , we have 

$$
\sum_ {i = 1} ^ {\infty} p (x _ {i}) = 1
$$

EXAMPLE 4.2a Consider a random variable X that is equal to 1, 2, or 3. If we know that 

$$
p (1) = \frac {1}{2} \qquad \mathrm{and} \qquad p (2) = \frac {1}{3}
$$

then it follows (since$\begin{array} { r } { p ( 1 ) + p ( 2 ) + p ( 3 ) = 1 ) } \end{array}$ that 

$$
p (3) = \frac {1}{6}
$$

A graph of ${ p ( x ) }$ is presented in Figure 4.1. ■ 

The cumulative distribution function F can be expressed in terms o$\dot { p } ( \boldsymbol { x } )$ by 

$$
F (a) = \sum_ {\text { all } x \leq a} p (x)
$$

If X is a discrete random variable whose set of possible values are $x _ { 1 } , x _ { 2 } , x _ { 3 } , . . . ,$ where $x _ { 1 } < x _ { 2 } < x _ { 3 } < \cdots$ , then its distribution function F is a step function. That is, the value of F is constant in the intervals $[ x _ { i - 1 } , x _ { i } )$ and then takes a step (or jump) of siz$ { p } ^ { (  { \boldsymbol { { x } } } _ { i } ) }$ ) at x<sub>i</sub> . 

## 4.2 Types of Random Variables

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/dd3884710344ac26139dcf40aaea00dccdce06a3e22608fc27a7ded098d6b49a.jpg)



FIGURE 4.1 Graph of ( p)x, Example 4.2a.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/81535f5e479030e3402cf932872c032b9c2270aa9eac9202ba92b8c79b31a491.jpg)



FIGURE 4.2 Graph of F (x).


For instance, suppose X has a probability mass function given (as in Example 4.2a) by 

$$
p (1) = \frac {1}{2}, \qquad p (2) = \frac {1}{3}, \qquad p (3) = \frac {1}{6}
$$

then the cumulative distribution function F of X is given by 

$$
F (a) = \left\{ \begin{array}{l l} 0 & a <   1 \\ \frac {1}{2} & 1 \leq a <   2 \\ \frac {5}{6} & 2 \leq a <   3 \\ 1 & 3 \leq a \end{array} \right.
$$

This is graphically presented in Figure 4.2. 

Whereas the set of possible values of a discrete random variable is a sequence, we often must consider random variables whose set of possible values is an interval. Let X be such a random variable. We say that X is a continuous random variable if there exists a nonnegative function $f ( x )$ , defined for all real $x \in ( - \infty , \infty )$ , having the property tha for any set B of real numbers 

$$
P \{X \in B \} = \int_ {B} f (x) d x\tag{4.2.1}
$$

The function $f ( x )$ is called the probability density function of the random variable X . 

In words, Equation 4.2.1 states that the probability that X will be in B may be obtained by integrating the probability density function over the set B. Since X must assume some value,$f ( x )$ must satisfy 

$$
1 = P \{X \in (- \infty , \infty) \} = \int_ {- \infty} ^ {\infty} f (x) d x
$$

All probability statements about X can be answered in terms of $f ( x )$ . For instance, letting$\boldsymbol { B } = [ a , b ]$ , we obtain from Equation 4.2.1 that 

$$
P \{a \leq X \leq b \} = \int_ {a} ^ {b} f (x) d x\tag{4.2.2}
$$

If we let $a = b$ in the above, then 

$$
P \{X = a \} = \int_ {a} ^ {a} f (x) d x = 0
$$

In words, this equation states that the probability that a continuous random variable will assume any particular value is zero. (See Figure 4.3.) 

The relationship between the cumulative distribution $F ( \cdot )$ and the probability density $f ( \cdot )$ is expressed by 

$$
F (a) = P \{X \in (- \infty , a ] \} = \int_ {- \infty} ^ {a} f (x) d x
$$

Differentiating both sides yields 

$$
\frac {d}{d a} F (a) = f (a)
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/3330f23a1ea932505be76bbcec6ec6178b67c25e4ea227aa71daf3940c027c68.jpg)


$$
\text { FIGURE   4.3 } \quad \text { The   probability   density   function   } f (x) = \left\{ \begin{array}{l l} e ^ {- x} & x \geq 0 \\ 0 & x <   0 \end{array} \right..
$$

That is, the density is the derivative of the cumulative distribution function. A somewhat more intuitive interpretation of the density function may be obtained from Equation 4.2.2 as follows: 

$$
P \left\{a - \frac {\varepsilon}{2} \leq X \leq a + \frac {\varepsilon}{2} \right\} = \int_ {a - \varepsilon / 2} ^ {a + \varepsilon / 2} f (x) d x \approx \varepsilon f (a)
$$

when ε is small. In other words, the probability that X will be contained in an interval of length$\varepsilon$ around the point a is approximately$\varepsilon f ( a )$ . From this, we see that $f ( a )$ is a measure of how likely it is that the random variable will be near a. 

EXAMPLE 4.2b Suppose that $X$ is a continuous random variable whose probability density function is given by 

$$
f (x) = \left\{ \begin{array}{l l} C (4 x - 2 x ^ {2}) & 0 <   x <   2 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) What is the value of C ? 

(b) Find $P \{ X > 1 \}$ 

SOLUTION (a) Since $f$ is a probability density function, we must have that$\textstyle \int _ { - \infty } ^ { \infty } f ( x ) d x = 1$ , implying that 

$$
C \int_ {0} ^ {2} (4 x - 2 x ^ {2}) d x = 1
$$

or 

$$
C \left[ 2 x ^ {2} - \frac {2 x ^ {3}}{3} \right] \Big | _ {x = 0} ^ {x = 2} = 1
$$

or 

$$
C = \frac {3}{8}
$$

(b) Hence 

$$
P \{X > 1 \} = \int_ {1} ^ {\infty} f (x) d x = \frac {3}{8} \int_ {1} ^ {2} (4 x - 2 x ^ {2}) d x = \frac {1}{2}
$$

## 4.3 JOINTLY DISTRIBUTED RANDOM VARIABLES

For a given experiment, we are often interested not only in probability distribution functions of individual random variables but also in the relationships between two or more random variables. For instance, in an experiment into the possible causes of cancer, we might be interested in the relationship between the average number of cigarettes smoked daily and the age at which an individual contracts cancer. Similarly, an engi neer might be interested in the relationship between the shear strength and the diameter of a spot weld in a fabricated sheet steel specimen. 

To specify the relationship between two random variables, we define the joint cumulative probability distribution function of X and Y by 

$$
F (x, y) = P \{X \leq x, Y \leq y \}
$$

A knowledge of the joint probability distribution function enables one, at least in theory, to compute the probability of any statement concerning the values of X and Y . For instance, the distribution function of X — call it $F _ { X } -$ can be obtained from the joint distribution function F of X and Y as follows: 

$$
\begin{array}{r l} & F _ {X} (x) = P \{X \leq x \} \\ & \quad = P \{X \leq x, Y <   \infty \} \\ & \quad = F (x, \infty) \end{array}
$$

Similarly, the cumulative distribution function of Y is given by 

$$
F _ {Y} (y) = F (\infty , y)
$$

In the case where X and Y are both discrete random variables whose possible values are, respectively,$x _ { 1 } , x _ { 2 } , . . . ,$ and $y _ { 1 } , y _ { 2 } , . . . ,$ we define the joint probability mass function of X and $Y , p ( x _ { i } , y _ { j } )$ , by 

$$
p (x _ {i}, y _ {j}) = P \{X = x _ {i}, Y = y _ {j} \}
$$

The individual probability mass functions of X and Y are easily obtained from the joint probability mass function by the following reasoning. Since Y must take on some value y<sub>j</sub>, it follows that the event$\{ X = x _ { i } \}$ can be written as the union, over al $j ,$ of the mutually exclusive events$\{ X = x _ { i } , Y = y _ { j } \}$ . That is, 

$$
\{X = x _ {i} \} = \bigcup_ {j} \{X = x _ {i}, Y = y _ {j} \}
$$

and so, using Axiom 3 of the probability function, we see that 

$$
\begin{array}{c} P \{X = x _ {i} \} = P \left(\bigcup_ {j} \{X = x _ {i}, Y = y _ {j} \}\right) \\ = \sum_ {j} P \{X = x _ {i}, Y = y _ {j} \} \\ = \sum_ {j} p (x _ {i}, y _ {j}) \end{array}\tag{4.3.1}
$$

Similarly, we can obtain $P \{ Y = y _ { j } \}$ by summing $/ ( x _ { i } , y _ { j } )$ over all possible values of $x _ { i } ;$ , that is, 

$$
\begin{array}{c} {P \{Y = y _ {j} \} =  \sum_ {i} P \{X = x _ {i}, Y = y _ {j} \}} \\ {=  \sum_ {i} p (x _ {i}, y _ {j})} \end{array}\tag{4.3.2}
$$

Hence, specifying the joint probability mass function always determines the individual mass functions. However, it should be noted that the reverse is not true. Namely, knowledge of $P \{ X = x _ { i } \}$ and $P \{ Y = y _ { j } \}$ does not determine the value of $P \{ X = x _ { i } , Y = y _ { j } \}$ 

EXAMPLE 4.3a Suppose that 3 batteries are randomly chosen from a group of 3 new, 4 used but still working, and 5 defective batteries. If we let X and Y denote, respectively, the number of new and used but still working batteries that are chosen, then the joint probability mass function of X and $Y , _ { \mathcal { P } } ( i , j ) = \mathcal { P } \{ X = i , Y = j \}$ }, is given by 

$$
\begin{array}{l} p (0, 0) = \binom {5} {3} \bigg / \binom {1 2} {3} = 1 0 / 2 2 0 \\ p (0, 1) = \binom {4} {1} \binom {5} {2} \bigg / \binom {1 2} {3} = 4 0 / 2 2 0 \\ p (0, 2) = \binom {4} {2} \binom {5} {1} \bigg / \binom {1 2} {3} = 3 0 / 2 2 0 \\ p (0, 3) = \binom {4} {3} \bigg / \binom {1 2} {3} = 4 / 2 2 0 \\ p (1, 0) = \binom {3} {1} \binom {5} {2} \bigg / \binom {1 2} {3} = 3 0 / 2 2 0 \\ p (1, 1) = \binom {3} {1} \binom {4} {1} \binom {5} {1} \bigg / \binom {1 2} {3} = 6 0 / 2 2 0 \\ p (1, 2) = \binom {3} {1} \binom {4} {2} \bigg / \binom {1 2} {3} = 1 8 / 2 2 0 \\ p (2, 0) = \binom {3} {2} \binom {5} {1} \bigg / \binom {1 2} {3} = 1 5 / 2 2 0 \\ p (2, 1) = \binom {3} {2} \binom {4} {1} \bigg / \binom {1 2} {3} = 1 2 / 2 2 0 \\ p (3, 0) = \binom {3} {3} \bigg / \binom {1 2} {3} = 1 / 2 2 0 \end{array}
$$

These probabilities can most easily be expressed in tabular form as shown in Table 4.1. 

<table><tr><td colspan="6">TABLE 4.1 <eq>P\{X = i, Y = j\}</eq></td></tr><tr><td><eq>i</eq></td><td>0</td><td>1</td><td>2</td><td>3</td><td>Row Sum= <eq>P\{X = i\}</eq></td></tr><tr><td>0</td><td><eq>\frac{10}{220}</eq></td><td><eq>\frac{40}{220}</eq></td><td><eq>\frac{30}{220}</eq></td><td><eq>\frac{4}{220}</eq></td><td><eq>\frac{84}{220}</eq></td></tr><tr><td>1</td><td><eq>\frac{30}{220}</eq></td><td><eq>\frac{60}{220}</eq></td><td><eq>\frac{18}{220}</eq></td><td>0</td><td><eq>\frac{108}{220}</eq></td></tr><tr><td>2</td><td><eq>\frac{15}{220}</eq></td><td><eq>\frac{12}{220}</eq></td><td>0</td><td>0</td><td><eq>\frac{27}{220}</eq></td></tr><tr><td>3</td><td><eq>\frac{1}{220}</eq></td><td>0</td><td>0</td><td>0</td><td><eq>\frac{1}{220}</eq></td></tr><tr><td>Column Sums = <eq>P\{Y = j\}</eq></td><td><eq>\frac{56}{220}</eq></td><td><eq>\frac{112}{220}</eq></td><td><eq>\frac{48}{220}</eq></td><td><eq>\frac{4}{220}</eq></td><td></td></tr></table>

The reader should note that the probability mass function of X is obtained by computing the row sums, in accordance with the Equation 4.3.1, whereas the probability mass function of Y is obtained by computing the column sums, in accordance with Equation 4.3.2. Because the individual probability mass functions of X and Y thus appear in the margin of such a table, they are often referred to as being the marginal probability mass functions of X and Y , respectively. It should be noted that to check the correctness of such a table we could sum the marginal row (or the marginal column) and verify that its sum is 1. (Why must the sum of the entries in the marginal row (or column) equal 1?) ■ 


EXAMPLE 4.3b Suppose that 15 percent of the families in a certain community have no children, 20 percent have 1, 35 percent have 2, and 30 percent have 3 children; suppose further that each child is equally likely (and independently) to be a boy or a girl. If a family is chosen at random from this community, then B, the number of boys, and G, the number of girls, in this family will have the joint probability mass function shown in Table 4.2.



TABLE 4.2 P {B = i, G = j }


<table><tr><td>i\j</td><td>0</td><td>1</td><td>2</td><td>3</td><td>Row Sum = P{B=i}</td></tr><tr><td>0</td><td>.15</td><td>.10</td><td>.0875</td><td>.0375</td><td>.3750</td></tr><tr><td>1</td><td>.10</td><td>.175</td><td>.1125</td><td>0</td><td>.3875</td></tr><tr><td>2</td><td>.0875</td><td>.1125</td><td>0</td><td>0</td><td>.2000</td></tr><tr><td>3</td><td>.0375</td><td>0</td><td>0</td><td>0</td><td>.0375</td></tr><tr><td>Column</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sum =</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P{G=j}</td><td>.3750</td><td>.3875</td><td>.2000</td><td>.0375</td><td></td></tr></table>

These probabilities are obtained as follows: 

$$
\begin{array}{c} P \{B = 0, G = 0 \} = P \{\text {no children} \} \\ = . 1 5 \end{array}
$$

$$
\begin{array}{r l} P \{B = 0, G = 1 \} & = P \{1 \text {   girl   and   total   of   1   child } \} \\ & = P \{1 \text {   child } \} P \{1 \text {   girl   |   1   child } \} \\ & = (. 2 0) \left(\frac {1}{2}\right) = . 1 \end{array}
$$

$$
\begin{array}{r l} P \{B = 0, G = 2 \} & = P \{2 \text {   girls   and   total   of   } 2 \text {   children } \} \\ & = P \{2 \text {   children } \} P \{2 \text {   girls   } | 2 \text {   children } \} \\ & = (. 3 5) \left(\frac {1}{2}\right) ^ {2} = . 0 8 7 5 \end{array}
$$

$$
\begin{array}{r l} P \{B = 0, G = 3 \} & = P \{3 \text {   girls   and   total   of   } 3 \text {   children } \} \\ & = P \{3 \text {   children } \} P \{3 \text {   girls   } | 3 \text {   children } \} \\ & = (. 3 0) \left(\frac {1}{2}\right) ^ {3} = . 0 3 7 5 \end{array}
$$

We leave it to the reader to verify the remainder of Table 4.2, which tells us, among other things, that the family chosen will have at least 1 girl with probability .625. ■ 

We say that X and $Y$ are jointly continuous if there exists a function $f ( x , y )$ defined for all real x and $y ,$ having the property that for every set $C$ of pairs of real numbers (that is, C is a set in the two-dimensional plane) 

$$
P \{(X, Y) \in C \} = \iint_ {(x, y) \in C} f (x, y) d x d y\tag{4.3.3}
$$

The function $f ( x , y )$ is called the joint probability density function of X and Y . If A and B are any sets of real numbers, then by defining $C = \{ ( x , y ) : x \in A , y \in B \}$ , we see from Equation 4.3.3 that 

$$
P \{X \in A, Y \in B \} = \int_ {B} \int_ {A} f (x, y) d x d y\tag{4.3.4}
$$

Because 

$$
\begin{array}{c} F (a, b) = P \{X \in (- \infty , a ], Y \in (- \infty , b ] \} \\ = \int_ {- \infty} ^ {b} \int_ {- \infty} ^ {a} f (x, y)   d x   d y \end{array}
$$

it follows, upon differentiation, that 

$$
f (a, b) = \frac {\partial^ {2}}{\partial a \partial b} F (a, b)
$$

wherever the partial derivatives are defined. Another interpretation of the joint density function is obtained from Equation 4.3.4 as follows: 

$$
\begin{array}{c} P \{a <   X <   a + d a, b <   Y <   b + d b \} = \int_ {b} ^ {d + d b} \int_ {a} ^ {a + d a} f (x, y) d x d y \\ \approx f (a, b) d a d b \end{array}
$$

when da and $d b$ are small and $f ( x , y )$ is continuous at $a , b .$ . Hence $f ( a , b )$ is a measure of how likely it is that the random vector $( X , Y )$ will be near $( a , b )$ 

If X and Y are jointly continuous, they are individually continuous, and their probability density functions can be obtained as follows: 

$$
\begin{array}{r l} & P \{X \in A \} = P \{X \in A, Y \in (- \infty , \infty) \} \\ & \qquad = \int_ {A} \int_ {- \infty} ^ {\infty} f (x, y) d y d x \\ & \qquad = \int_ {A} f _ {X} (x) d x \end{array}\tag{4.3.5}
$$

where 

$$
f _ {X} (x) = \int_ {- \infty} ^ {\infty} f (x, y) d y
$$

is thus the probability density function of X . Similarly, the probability density function of Y is given by 

$$
f _ {Y} (y) = \int_ {- \infty} ^ {\infty} f (x, y) d x\tag{4.3.6}
$$

EXAMPLE 4.3c The joint density function of X and Y is given by 

$$
f (x, y) = \left\{ \begin{array}{l l} 2 e ^ {- x} e ^ {- 2 y} & 0 <   x <   \infty , 0 <   y <   \infty \\ 0 & \text { otherwise } \end{array} \right.
$$

Compute (a)$P \{ X > 1 , Y < 1 \}$ }; (b)$P \{ X < Y \}$ ; and (c)$P \{ X < a \}$ 

SOLUTION 

(a) 

$$
\begin{array}{l} P \{X > 1, Y <   1 \} = \int_ {0} ^ {1} \int_ {1} ^ {\infty} 2 e ^ {- x} e ^ {- 2 y} d x d y \\ \qquad = \int_ {0} ^ {1} 2 e ^ {- 2 y} (- e ^ {- x} | _ {1} ^ {\infty}) d y \\ \qquad = e ^ {- 1} \int_ {0} ^ {1} 2 e ^ {- 2 y} d y \\ \qquad = e ^ {- 1} (1 - e ^ {- 2}) \end{array}\tag{b}
$$

$$
\begin{array}{l} P \{X <   Y \} = \iint_ {(x, y): x <   y} 2 e ^ {- x} e ^ {- 2 y} d x d y \\ \qquad = \int_ {0} ^ {\infty} \int_ {0} ^ {y} 2 e ^ {- x} e ^ {- 2 y} d x d y \\ \qquad = \int_ {0} ^ {\infty} 2 e ^ {- 2 y} (1 - e ^ {- y}) d y \\ \qquad = \int_ {0} ^ {\infty} 2 e ^ {- 2 y} d y - \int_ {0} ^ {\infty} 2 e ^ {- 3 y} d y \\ \qquad = 1 - \frac {2}{3} \\ \qquad = \frac {1}{3} \end{array}
$$

(c) 

$$
\begin{array}{r l} P \{X <   a \} & = \int_ {0} ^ {a} \int_ {0} ^ {\infty} 2 e ^ {- 2 y} e ^ {- x} d y d x \\ & = \int_ {0} ^ {a} e ^ {- x} d x \\ & = 1 - e ^ {- a} \quad \blacksquare \end{array}
$$

## 4.3.1 Independent Random Variables

The random variables X and Y are said to be independent if for any two sets of real numbers A and B 

$$
P \{X \in A, Y \in B \} = P \{X \in A \} P \{Y \in B \}\tag{4.3.7}
$$

In other words, X and Y are independent if, for all A and B, the event $E _ { A } = \{ X \in A \}$ and $F _ { B } = \{ Y \in B \}$ are independent. 

It can be shown by using the three axioms of probability that Equation 4.3.7 will follow if and only if for all $a , b$ 

$$
P \{X \leq a, Y \leq b \} = P \{X \leq a \} P \{Y \leq b \}
$$

Hence, in terms of the joint distribution function F of X and ${ \cal Y } ,$ , we have that X and Y are independent if 

$$
F (a, b) = F _ {X} (a) F _ {Y} (b) \qquad \mathrm{forall} a, b
$$

When X and Y are discrete random variables, the condition of independence Equation 4.3.7 is equivalent to 

$$
p (x, y) = p _ {X} (x) p _ {Y} (y) \quad \text {   for   all   } x, y\tag{4.3.8}
$$

where$\hbar X$ and$\hbar Y$ are the probability mass functions of X and Y . The equivalence follows because, if Equation 4.3.7 is satisfied, then we obtain Equation 4.3.8 by letting A and B be, respectively, the one-point sets $A = \{ x \} , B = \{ y \}$ . Furthermore, if Equation 4.3.8 is valid, then for any sets A, B 

$$
\begin{array}{r l} & P \{X \in A, Y \in B \} = \sum_ {y \in B} \sum_ {x \in A} p (x, y) \\ & \qquad = \sum_ {y \in B} \sum_ {x \in A} p _ {X} (x) p _ {Y} (y) \\ & \qquad = \sum_ {y \in B} p _ {Y} (y) \sum_ {x \in A} p _ {X} (x) \\ & \qquad = P \{Y \in B \} P \{X \in A \} \end{array}
$$

and thus Equation 4.3.7 is established. 

In the jointly continuous case, the condition of independence is equivalent to 

$$
f (x, y) = f _ {X} (x) f _ {Y} (y) \quad \text {   for   all   } x, y
$$

Loosely speaking, X and Y are independent if knowing the value of one does not change the distribution of the other. Random variables that are not independent are said to be dependent. 

EXAMPLE 4.3d Suppose that X and Y are independent random variables having the common density function 

$$
f (x) = \left\{ \begin{array}{l l} e ^ {- x} & x > 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

Find the density function of the random variable $X / Y$ 

SOLUTION We start by determining the distribution function of X /Y . For $a > 0$ 

$$
\begin{array}{l} F _ {X / Y} (a) = P \{X / Y \leq a \} \\ = \iint_ {x / y \leq a} f (x, y) d x d y \\ = \iint_ {x / y \leq a} e ^ {- x} e ^ {- y} d x d y \\ = \int_ {0} ^ {\infty} \int_ {0} ^ {a y} e ^ {- x} e ^ {- y} d x d y \\ = \int_ {0} ^ {\infty} (1 - e ^ {- a y}) e ^ {- y} d y \\ = \left[ - e ^ {- y} + \frac {e ^ {- (a + 1) y}}{a + 1} \right] \Big | _ {0} ^ {\infty} \\ = 1 - \frac {1}{a + 1} \end{array}
$$

Differentiation yields that the density function of X /Y is given by 

$$
f _ {X / Y} (a) = 1 / (a + 1) ^ {2}, \qquad 0 <   a <   \infty
$$

We can also define joint probability distributions for n random variables in exactly the same manner as we did for $n = 2$ . For instance, the joint cumulative probability distribution function $F ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$ of the n random variables $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ is defined by 

$$
F (a _ {1}, a _ {2}, \dots , a _ {n}) = P \{X _ {1} \leq a _ {1}, X _ {2} \leq a _ {2}, \dots , X _ {n} \leq a _ {n} \}
$$

If these random variables are discrete, we define their joint probability mass function$\ p ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ by 

$$
p (x _ {1}, x _ {2}, \dots , x _ {n}) = P \{X _ {1} = x _ {1}, X _ {2} = x _ {2}, \dots , X _ {n} = x _ {n} \}
$$

Further, the n random variables are said to be jointly continuous if there exists a function $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ , called the joint probability density function, such that for any set C in n-space 

$$
P \{(X _ {1}, X _ {2}, \dots , X _ {n}) \in C \} = \int \int_ {(x _ {1}, \dots , x _ {n}) \in C} \dots \int f (x _ {1}, \dots , x _ {n}) d x _ {1} d x _ {2} \dots d x _ {n}
$$

In particular, for any n sets of real numbers $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ 

$$
\begin{array}{l} P \{X _ {1} \in A _ {1}, X _ {2} \in A _ {2}, \ldots , X _ {n} \in A _ {n} \} \\ = \int_ {A _ {n}} \int_ {A _ {n - 1}} \ldots \int_ {A _ {1}} f (x _ {1}, \ldots , x _ {n}) d x _ {1} d x _ {2} \ldots d x _ {n} \end{array}
$$

The concept of independence may, of course, also be defined for more than two random variables. In general, the n random variables $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ are said to be independent if, for all sets of real numbers $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ 3 

$$
P \{X _ {1} \in A _ {1}, X _ {2} \in A _ {2}, \ldots , X _ {n} \in A _ {n} \} = \prod_ {i = 1} ^ {n} P \{X _ {i} \in A _ {i} \}
$$

As before, it can be shown that this condition is equivalent to 

$$
\begin{array}{l} P \{X _ {1} \leq a _ {1}, X _ {2} \leq a _ {2}, \dots , X _ {n} \leq a _ {n} \} \\ = \prod_ {i = 1} ^ {n} P \{X _ {1} \leq a _ {i} \} \quad \text { for   all } a _ {1}, a _ {2}, \dots , a _ {n} \end{array}
$$

Finally, we say that an infinite collection of random variables is independent if every finite subcollection of them is independent. 

EXAMPLE 4.3e Suppose that the successive daily changes of the price of a given stock are assumed to be independent and identically distributed random variables with probability mass function given by 

$$
P \{\text {daily change is} i \} = \left\{ \begin{array}{l l} - 3 & \text {with probability .05} \\ - 2 & \text {with probability .10} \\ - 1 & \text {with probability .20} \\ 0 & \text {with probability .30} \\ 1 & \text {with probability .20} \\ 2 & \text {with probability .10} \\ 3 & \text {with probability .05} \end{array} \right.
$$

Then the probability that the stock’s price will increase successively by 1, 2, and 0 points in the next three days is 

$$
P \{X _ {1} = 1, X _ {2} = 2, X _ {3} = 0 \} = (. 2 0) (. 1 0) (. 3 0) = . 0 0 6
$$

where we have let $X _ { i }$ denote the change on the ith day. ■ 

## *4.3.2 Conditional Distributions

The relationship between two random variables can often be clarified by consideration of the conditional distribution of one given the value of the other. 

Recall that for any two events E and F , the conditional probability of E given F is defined, provided that $P ( F ) > 0$ , by 

$$
P (E | F) = \frac {P (E F)}{P (F)}
$$

Hence, if X and Y are discrete random variables, it is natural to define the conditiona probability mass function of X given that $Y = y ,$ , by 

$$
\begin{array}{c} p _ {X | Y} (x | y) = P \{X = x | Y = y \} \\ = \frac {P \{X = x , Y = y \}}{P \{Y = y \}} \\ = \frac {p (x , y)}{p _ {Y} (y)} \end{array}
$$

for all values of y such that $/ { Y } ( y ) > 0$ 

EXAMPLE 4.3f If we know, in Example 4.3b, that the family chosen has one girl, compute the conditional probability mass function of the number of boys in the family. 

SOLUTION We first note from Table 4.2 that 

$$
P \{G = 1 \} = . 3 8 7 5
$$

Hence, 

$$
P \{B = 0 | G = 1 \} = \frac {P \{B = 0 , G = 1 \}}{P \{G = 1 \}} = \frac {. 1 0}{. 3 8 7 5} = 8 / 3 1
$$

$$
P \{B = 1 | G = 1 \} = \frac {P \{B = 1 , G = 1 \}}{P \{G = 1 \}} = \frac {. 1 7 5}{. 3 8 7 5} = 1 4 / 3 1
$$

$$
P \{B = 2 | G = 1 \} = \frac {P \{B = 2 , G = 1 \}}{P \{G = 1 \}} = \frac {. 1 1 2 5}{. 3 8 7 5} = 9 / 3 1
$$

$$
P \{B = 3 | G = 1 \} = \frac {P \{B = 3 , G = 1 \}}{P \{G = 1 \}} = 0
$$

Thus, for instance, given 1 girl, there are 23 chances out of 31 that there will also be at least 1 boy. ■ 

EXAMPLE 4.3g Suppose that$\phi ( x , y )$ , the joint probability mass function of X and ${ \cal Y } ,$ , is given by 

$$
p (0, 0) = . 4, \quad p (0, 1) = . 2, \quad p (1, 0) = . 1, \quad p (1, 1) = . 3.
$$

Calculate the conditional probability mass function of X given that $Y = 1$ 

SOLUTION We first note that 

$$
P \{Y = 1 \} = \sum_ {x} p (x, 1) = p (0, 1) + p (1, 1) = . 5
$$

Hence, 

$$
P \{X = 0 | Y = 1 \} = \frac {p (0 , 1)}{P \{Y = 1 \}} = 2 / 5
$$

$$
P \{X = 1 | Y = 1 \} = \frac {p (1 , 1)}{P \{Y = 1 \}} = 3 / 5
$$

If X and Y have a joint probability density function $f ( x , y )$ , then the conditional probability density function of $X _ { i }$ , given that $Y = y$ , is defined for all values of y such that $f _ { Y } ( y ) > 0$ , by 

$$
f _ {X | Y} (x | y) = \frac {f (x , y)}{f _ {Y} (y)}
$$

To motivate this definition, multiply the left-hand side by dx and the right-hand side by (dx $d y ) / d y$ to obtain 

$$
\begin{array}{c} f _ {X | Y} (x | y) d x = \frac {f (x , y) d x d y}{f _ {Y} (y) d y} \\ \approx \frac {P \{x \leq X \leq x + d x , y \leq Y \leq y + d y \}}{P \{y \leq Y \leq y + d y \}} \\ = P \{x \leq X \leq x + d y | y \leq Y \leq y + d y \} \end{array}
$$

In other words, for small values of dx and $d y , f _ { X | Y } ( x | y )$ dx represents the conditional probability that X is between x and $x + d x$ , given that Y is between y and $y + d y$ 

The use of conditional densities allows us to define conditional probabilities of events associated with one random variable when we are given the value of a second random variable. That is, if X and Y are jointly continuous, then, for any set A, 

$$
P \{X \in A | Y = y \} = \int_ {A} f _ {X | Y} (x | y) d x
$$

EXAMPLE 4.3h The joint density of X and Y is given by 

$$
f (x, y) = \left\{ \begin{array}{l l} \frac {1 2}{5} x (2 - x - y) & 0 <   x <   1, 0 <   y <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Compute the conditional density of X , given that $Y = y ,$ , where $0 < y < 1$ 

SOLUTION For $0 < x < 1 , 0 < y < 1$ , we have 

$$
\begin{array}{r l} f _ {X | Y} (x | y) & = \frac {f (x , y)}{f _ {Y} (y)} \\ & = \frac {f (x , y)}{\int_ {- \infty} ^ {\infty} f (x , y) d x} \\ & = \frac {x (2 - x - y)}{\int_ {0} ^ {1} x (2 - x - y) d x} \\ & = \frac {x (2 - x - y)}{\frac {2}{3} - y / 2} \\ & = \frac {6 x (2 - x - y)}{4 - 3 y} \end{array}
$$

## 4.4 EXPECTATION

One of the most important concepts in probability theory is that of the expectation of a random variable. If X is a discrete random variable taking on the possible values $x _ { 1 } , x _ { 2 } , . . . ,$ then the expectation or expected value of X , denoted by $E [ X ]$ , is defined by 

$$
E [ X ] = \sum_ {i} x _ {i} P \{X = x _ {i} \}
$$

In words, the expected value of X is a weighted average of the possible values that X can take on, each value being weighted by the probability that X assumes it. For instance, if the probability mass function of X is given by 

$$
p (0) = \frac {1}{2} = p (1)
$$

then 

$$
E [ X ] = 0 \left(\frac {1}{2}\right) + 1 \left(\frac {1}{2}\right) = \frac {1}{2}
$$

is just the ordinary average of the two possible values 0 and 1 that X can assume. On the other hand, if 

$$
p (0) = \frac {1}{3}, \quad p (1) = \frac {2}{3}
$$

then 

$$
E [ X ] = 0 \left(\frac {1}{3}\right) + 1 \left(\frac {2}{3}\right) = \frac {2}{3}
$$

is a weighted average of the two possible values 0 and 1 where the value 1 is given twice as much weight as the value 0 since$\rho ( 1 ) = 2 \rho ( 0 )$ 

Another motivation of the definition of expectation is provided by the frequency interpretation of probabilities. This interpretation assumes that if an infinite sequence of independent replications of an experiment is performed, then for any event $E ,$ , the proportion of time that E occurs will be $P ( E )$ . Now, consider a random variable X that must take on one of the values $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ with respective probabilities ${ \mathfrak { p } } ( x _ { 1 } ) , { \mathfrak { p } } ( x _ { 2 } ) , \dots , { \mathfrak { p } } ( x _ { n } )$ ; and think of X as representing our winnings in a single game of chance. That is, with probability$ { p } ^ { (  { \boldsymbol { { x } } } _ { i } ) }$ we shall win $x _ { i }$ units $i = 1 , 2 , \dots , n$ . Now by the frequency interpretation, it follows that if we continually play this game, then the proportion of time that we win $x _ { i }$ will be$ { p } (  { \boldsymbol { { x } } } _ { i } )$ . Since this is true for all $i , i = 1 , 2 , \ldots , n ,$ it follows that our average winnings per game will be 

$$
\sum_ {i = 1} ^ {n} x _ {i} p (x _ {i}) = E [ X ]
$$

To see this argument more clearly, suppose that we play N games where N is very large. Then in approximately $N p ( x _ { i } )$ of these games, we shall win $x _ { i }$ , and thus our total winnings in the N games will be 

$$
\sum_ {i = 1} ^ {n} x _ {i} N _ {p} (x _ {i})
$$

implying that our average winnings per game are 

$$
\sum_ {i = 1} ^ {n} \frac {x _ {i} N _ {p} (x _ {i})}{N} = \sum_ {i = 1} ^ {n} x _ {i} p (x _ {i}) = E [ X ]
$$

EXAMPLE 4.4a Find E [X ] where X is the outcome when we roll a fair die. 

SOLUTION Since$\begin{array} { r } { p ( 1 ) = p ( 2 ) = p ( 3 ) = p ( 4 ) = p ( 5 ) = p ( 6 ) = \frac { 1 } { 6 } } \end{array}$ , we obtain that 

$$
E [ X ] = 1 \left(\frac {1}{6}\right) + 2 \left(\frac {1}{6}\right) + 3 \left(\frac {1}{6}\right) + 4 \left(\frac {1}{6}\right) + 5 \left(\frac {1}{6}\right) + 6 \left(\frac {1}{6}\right) = \frac {7}{2}
$$

The reader should note that, for this example, the expected value of X is not a value that X could possibly assume. (That is, rolling a die cannot possibly lead to an outcome of 7/2.) Thus, even though we call $E [ X ]$ the expectation of $X _ { i }$ , it should not be interpreted as the value that we expect X to have but rather as the average value of X in a large number of repetitions of the experiment. That is, if we continually roll a fair die, then after a large number of rolls the average of all the outcomes will be approximately 7/2. (The interested reader should try this as an experiment.) ■ 

EXAMPLE 4.4b If I is an indicator random variable for the event A, that is, if 

$$
I = \left\{ \begin{array}{l l} 1 & \text { if   } A \text {   occurs } \\ 0 & \text { if   } A \text {   does   not   occur } \end{array} \right.
$$

then 

$$
E [ I ] = 1 P (A) + 0 P (A ^ {c}) = P (A)
$$

Hence, the expectation of the indicator random variable for the event A is just the probability that A occurs. ■ 

EXAMPLE 4.4c Entropy For a given random variable X , how much information is conveyed in the message that $X = x ?$ Let us begin our attempts at quantifying this statement by agreeing that the amount of information in the message that $X = x$ should depend on how likely it was that X would equal x. In addition, it seems reasonable that the more unlikely it was that X would equal x, the more informative would be the message. For instance, if X represents the sum of two fair dice, then there seems to be more information in the message that X equals 12 than there would be in the message that X equals 7, since the former event has probability$\frac { 1 } { 3 6 }$ and the latter$\frac { 1 } { 6 }$ 

Let us denote by $I ( \boldsymbol { p } )$ the amount of information contained in the message that an event, whose probability is ${ \boldsymbol { p } } ,$ , has occurred. Clearly $I ( \boldsymbol { p } )$ should be a nonnegative, decreasing function of ${ \dot { \mathbf { \gamma } } } _ { \phi } .$ To determine its form, let X and Y be independent random variables, and suppose that $P \{ X = x \} = p$ and $P \{ Y = y \} = q$ . How much information is contained in the message that X equals x and Y equals $y { \boldsymbol { ? } }$ To answer this, note first that the amount of information in the statement that X equals x is $I ( \boldsymbol { p } )$ . Also, since knowledge of the fact that X is equal to x does not affect the probability that Y will equa $y$ (since $X$ and $Y$ are independent), it seems reasonable that the additional amount of information contained in the statement that $Y = y$ should equal $I ( q )$ . Thus, it seems that the amount of information in the message that X equals x and Y equals y is $I ( p ) + I ( q )$ . On the other hand, however, we have that 

$$
P \{X = x, Y = y \} = P \{X = x \} P \{Y = y \} = p q
$$

which implies that the amount of information in the message that X equals x and Y equals $y$ is $I ( \phi q )$ . Therefore, it seems that the function I should satisfy the identity 

$$
I (p q) = I (p) + I (q)
$$

However, if we define the function G by 

$$
G (p) = I (2 ^ {- p})
$$

then we see from the above that 

$$
\begin{array}{r l} & G (p + q) = I (2 ^ {- (p + q)}) \\ & \qquad = I (2 ^ {- p} 2 ^ {- q}) \\ & \qquad = I (2 ^ {- p}) + I (2 ^ {- q}) \\ & \qquad = G (p) + G (q) \end{array}
$$

However, it can be shown that the only (monotone) functions G that satisfy the foregoing functional relationship are those of the form 

$$
G (p) = c p
$$

for some constant c. Therefore, we must have that 

$$
I (2 ^ {- p}) = c p
$$

or, letting $q = 2 ^ { - p }$ 

$$
I (q) = - c \log_ {2} (q)
$$

for some positive constant c. It is traditional to let $c = 1$ and to say that the information is measured in units of bits (short for binary digits). 

Consider now a random variable X , which must take on one of the values $x _ { 1 } , \ldots , x _ { n }$ with respective probabilities$\ p _ { 1 } , \ldots , \ p _ { n }$ . As$\log _ { 2 } ( \rho _ { i } )$ represents the information conveyed by the message that X is equal to $x _ { i } ,$ , it follows that the expected amount of information that will be conveyed when the value of X is transmitted is given by 

$$
H (X) = - \sum_ {i = 1} ^ {n} p _ {i} \log_ {2} (p _ {i})
$$

The quantity $H ( X )$ is known in information theory as the entropy of the random variable X . ■ 

We can also define the expectation of a continuous random variable. Suppose that X is a continuous random variable with probability density function f . Since, for dx small 

$$
f (x) d x \approx P \{x <   X <   x + d x \}
$$

it follows that a weighted average of all possible values of X , with the weight given to x equal to the probability that X is near x, is just the integral over all $x \operatorname { o f } x f ( x )$ dx. Hence, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/8b4f0ec7a7dc15b9084049b7b275c0221662d3143c1a5d82048e6a77d18da8de.jpg)


## 4.5 Properties of the Expected Value

it is natural to define the expected value of X by 

$$
E [ X ] = \int_ {- \infty} ^ {\infty} x f (x) d x
$$

EXAMPLE 4.4d Suppose that you are expecting a message at some time past 5 P.M. From experience you know that X , the number of hours after 5 P.M. until the message arrives, is a random variable with the following probability density function: 

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{1 . 5} & \text { if } 0 <   x <   1. 5 \\ 0 & \text { otherwise } \end{array} \right.
$$

The expected amount of time past 5 P.M. until the message arrives is given by 

$$
E [ X ] = \int_ {0} ^ {1. 5} {\frac {x}{1 . 5}} d x = . 7 5
$$

Hence, on average, you would have to wait three-fourths of an hour. ■ 

## REMARKS

(a) The concept of expectation is analogous to the physical concept of the center of gravity of a distribution of mass. Consider a discrete random variable X having probability mass function $P ( x _ { i } ) , i \geq 1$ . If we now imagine a weightless rod in which weights with mass $P ( x _ { i } ) , i \geq 1$ are located at the points $x _ { i } , i \geq 1$ (see Figure 4.4), then the point at which the rod would be in balance is known as the center of gravity. For those readers acquainted with elementary statics, it is now a simple matter to show that this point is at E [X ].* (b) E [X ] has the same units of measurement as does X . 

## 4.5 PROPERTIES OF THE EXPECTED VALUE

Suppose now that we are given a random variable X and its probability distribution (that is, its probability mass function in the discrete case or its probability density function in the continuous case). Suppose also that we are interested in calculating, not the expected value of X , but the expected value of some function of $X ,$ , say $g ( X )$ . How do we go about doing this? One way is as follows. Since $g ( X )$ ) is itself a random variable, it must have a probability distribution, which should be computable from a knowledge of the distribution of X . Once we have obtained the distribution of $g ( X )$ , we can then compute $E [ g ( X ) ]$ by the definition of the expectation. 

EXAMPLE 4.5a Suppose X has the following probability mass function 

$$
p (0) = . 2, \quad p (1) = . 5, \quad p (2) = . 3
$$

Calculate $E [ X ^ { 2 } ]$ 

SOLUTION Letting $Y = X ^ { 2 }$ , we have that Y is a random variable that can take on one of the values $0 ^ { 2 } , 1 ^ { 2 } , \bar { 2 } ^ { 2 }$ with respective probabilities 

$$
\begin{array}{r} p _ {Y} (0) = P \{Y = 0 ^ {2} \} = . 2 \\ p _ {Y} (1) = P \{Y = 1 ^ {2} \} = . 5 \\ p _ {Y} (4) = P \{Y = 2 ^ {2} \} = . 3 \end{array}
$$

Hence, 

$$
E [ X ^ {2} ] = E [ Y ] = 0 (. 2) + 1 (. 5) + 4 (. 3) = 1. 7
$$

EXAMPLE 4.5b The time, in hours, it takes to locate and repair an electrical breakdown in a certain factory is a random variable — call it X — whose density function is given by 

$$
f _ {X} (x) = \left\{ \begin{array}{l l} 1 & \text { if } 0 <   x <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

If the cost involved in a breakdown of duration x is $x ^ { 3 }$ , what is the expected cost of such a breakdown? 

SOLUTION Letting $Y = X ^ { 3 }$ denote the cost, we first calculate its distribution function as follows. For $0 \leq a \leq 1$ 

$$
\begin{array}{r l} F _ {Y} (a) & = P \{Y \leq a \} \\ & = P \{X ^ {3} \leq a \} \\ & = P \{X \leq a ^ {1 / 3} \} \\ & = \int_ {0} ^ {a ^ {1 / 3}} d x \\ & = a ^ {1 / 3} \end{array}
$$

By differentiating $F _ { Y } ( a )$ , we obtain the density of $Y$ , 

$$
f _ {Y} (a) = \frac {1}{3} a ^ {- 2 / 3}, \quad 0 \leq a <   1
$$

Hence, 

$$
\begin{array}{r l} E [ X ^ {3} ] & = E [ Y ] = \int_ {- \infty} ^ {\infty} a f _ {Y} (a) d a \\ & = \int_ {0} ^ {1} a \frac {1}{3} a ^ {- 2 / 3} d a \\ & = \frac {1}{3} \int_ {0} ^ {1} a ^ {1 / 3} d a \\ & = \frac {1}{3} \frac {3}{4} a ^ {4 / 3} | _ {0} ^ {1} \\ & = \frac {1}{4} \quad \blacksquare \end{array}
$$

While the foregoing procedure will, in theory, always enable us to compute the expec tation of any function of $X$ from a knowledge of the distribution of $X ,$ , there is an easier way of doing this. Suppose, for instance, that we wanted to compute the expected value of $g ( X )$ . Since $g ( X )$ takes on the value $g ( X )$ when $X = x ,$ , it seems intuitive that $E [ g ( X ) ]$ should be a weighted average of the possible values $g ( X )$ with, for a given $x ,$ the weight given to $g ( x )$ being equal to the probability (or probability density in the continuous case) that X will equal x. Indeed, the foregoing can be shown to be true and we thus have the following proposition. 

## PROPOSITION 4.5.1 EXPECTATION OF A FUNCTION OF A RANDOM VARIABLE

(a) If X is a discrete random variable with probability mass function ${ p ( x ) }$ ), then for any real-valued function $g$ , 

$$
E [ g (X) ] = \sum_ {x} g (x) p (x)
$$

(b) If X is a continuous random variable with probability density function $f ( x )$ , then for any real-valued function $g ,$ , 

$$
E [ g (X) ] = \int_ {- \infty} ^ {\infty} g (x) f (x) d x
$$

EXAMPLE 4.5c Applying Proposition 4.5.1 to Example 4.5a yields 

$$
E [ X ^ {2} ] = 0 ^ {2} (0. 2) + (1 ^ {2}) (0. 5) + (2 ^ {2}) (0. 3) = 1. 7
$$

which, of course, checks with the result derived in Example 4.5a. ■ 

EXAMPLE 4.5d Applying the proposition to Example 4.5b yields 

$$
\begin{array}{l} E [ X ^ {3} ] = \int_ {0} ^ {1} x ^ {3} d x \quad (\text { since } f (x) = 1, 0 <   x <   1) \\ = \frac {1}{4} \quad \blacksquare \end{array}
$$

An immediate corollary of Proposition 4.5.1 is the following. 

## Corollary 4.5.2

If a and b are constants, then 

$$
E [ a X + b ] = a E [ X ] + b
$$

Proof 

In the discrete case, 

$$
\begin{array}{r l} & E [ a X + b ] = \sum_ {x} (a x + b) p (x) \\ & \qquad = a \sum_ {x} x p (x) + b \sum_ {x} p (x) \\ & \qquad = a E [ X ] + b \end{array}
$$

In the continuous case, 

$$
\begin{array}{r l} E [ a X + b ] & = \int_ {- \infty} ^ {\infty} (a x + b) f (x) d x \\ & = a \int_ {- \infty} ^ {\infty} x f (x) d x + b \int_ {- \infty} ^ {\infty} f (x) d x \\ & = a E [ X ] + b \quad \square \end{array}
$$

If we take $a = 0$ in Corollary 4.5.2, we see that 

$$
E [ b ] = b
$$

That is, the expected value of a constant is just its value. (Is this intuitive?) Also, if we take $b = 0$ , then we obtain 

$$
E [ a X ] = a E [ X ]
$$

or, in words, the expected value of a constant multiplied by a random variable is just the constant times the expected value of the random variable. The expected value of a random variable X , E [X ], is also referred to as the mean or the first moment of X . The quantity $E [ X ^ { n } ] , n \geq 1$ , is called the nth moment of X . By Proposition 4.5.1, we note that 

$$
E [ X ^ {n} ] = \left\{ \begin{array}{l l} \sum_ {x} x ^ {n} p (x) & \text { if   } X \text {   is   discrete } \\ \int_ {- \infty} ^ {x} x ^ {n} f (x) d x & \text { if   } X \text {   is   continuous } \end{array} \right.
$$

## 4.5.1 Expected Value of Sums of Random Variables

The two-dimensional version of Proposition 4.5.1 states that if X and Y are random variables and $g$ is a function of two variables, then 

$$
\begin{array}{l l} E [ g (X, Y) ] = \sum_ {y} \sum_ {x} g (x, y) p (x, y) & \text { in   the   discrete   case } \\ = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} g (x, y) f (x, y) d x d y & \text { in   the   continuous   case } \end{array}
$$

For example,${ \mathrm { i f } } g ( X , Y ) = X + Y$ , then, in the continuous case, 

$$
\begin{array}{l} E [ X + Y ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} (x + y) f (x, y) d x d y \\ \qquad = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} x f (x, y) d x d y + \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} y f (x, y) d x d y \\ \qquad = E [ X ] + E [ Y ] \end{array}
$$

A similar result can be shown in the discrete case and indeed, for any random variables X and $Y _ { i }$ , 

$$
E [ X + Y ] = E [ X ] + E [ Y ]\tag{4.5.1}
$$

By repeatedly applying Equation 4.5.1 we can show that the expected value of the sum of any number of random variables equals the sum of their individual expectations. 

For instance, 

$$
\begin{array}{r l} E [ X + Y + Z ] = E [ (X + Y) + Z ] & \\ = E [ X + Y ] + E [ Z ] & \text {by Equation 4.5.1} \\ = E [ X ] + E [ Y ] + E [ Z ] & \text {again by Equation 4.5.1} \end{array}
$$

And in general, for any n, 

$$
E [ X _ {1} + X _ {2} \dots + X _ {n} ] = E [ X _ {1} ] + E [ X _ {2} ] + \dots + E [ X _ {n} ]\tag{4.5.2}
$$

Equation 4.5.2 is an extremely useful formula whose utility will now be illustrated by a series of examples. 

EXAMPLE 4.5e A construction firm has recently sent in bids for 3 jobs worth (in profits) 10, 20, and 40 (thousand) dollars. If its probabilities of winning the jobs are respectively .2, .8, and .3, what is the firm’s expected total profit? 

SOLUTION Letting $X _ { i } , i = 1 , 2 , 3$ denote the firm’s profit from job i, then 

$$
\mathrm{totalprofit} = X _ {1} + X _ {2} + X _ {3}
$$

and so 

$$
E [ \mathrm{totalprofit} ] = E [ X _ {1} ] + E [ X _ {2} ] + E [ X _ {3} ]
$$

Now 

$$
\begin{array}{l} E [ X _ {1} ] = 1 0 (. 2) + 0 (. 8) = 2 \\ E [ X _ {2} ] = 2 0 (. 8) + 0 (. 2) = 1 6 \\ E [ X _ {3} ] = 4 0 (. 3) + 0 (. 7) = 1 2 \end{array}
$$

and thus the firm’s expected total profit is 30 thousand dollars. ■ 

EXAMPLE 4.5f A secretary has typed N letters along with their respective envelopes. The envelopes get mixed up when they fall on the floor. If the letters are placed in the mixed-up envelopes in a completely random manner (that is, each letter is equally likely to end up in any of the envelopes), what is the expected number of letters that are placed in the correct envelopes? 

SOLUTION Letting X denote the number of letters that are placed in the correct envelope, we can most easily compute E [X ] by noting that 

$$
X = X _ {1} + X _ {2} + \dots + X _ {N}
$$

where 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   letter   is   placed   in   its   proper   envelope } \\ 0 & \text { otherwise } \end{array} \right.
$$

Now, since the ith letter is equally likely to be put in any of the N envelopes, it follows that 

$$
P \{X _ {i} = 1 \} = P \{i t h l e t t e r i s i n i t s p r o p e r e n v e l o p e \} = 1 / N
$$

and so 

$$
E [ X _ {i} ] = 1 P \{X _ {i} = 1 \} + 0 P \{X _ {i} = 0 \} = 1 / N
$$

Hence, from Equation 4.5.2 we obtain that 

$$
E [ X ] = E \left[ X _ {1} \right] + \dots + E \left[ X _ {N} \right] = \left(\frac {1}{N}\right) N = 1
$$

Hence, no matter how many letters there are, on the average, exactly one of the letters will be in its own envelope. ■ 

EXAMPLE 4.5g Suppose there are 20 different types of coupons and suppose that each time one obtains a coupon it is equally likely to be any one of the types. Compute the expected number of different types that are contained in a set for 10 coupons. 

SOLUTION Let X denote the number of different types in the set of 10 coupons. We compute E [X ] by using the representation 

$$
X = X _ {1} + \dots + X _ {2 0}
$$

where 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   at   least   one   type } i \text { coupon   is   contained   in   the   set   of } 1 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

Now 

$$
\begin{array}{r l} E [ X _ {i} ] & = P \{X _ {i} = 1 \} \\ & = P \{\text { at   least   one   type } i \text { coupon   is   in   the   set   of } 1 0 \} \\ & = 1 - P \{\text { no   type } i \text { coupons   are   contained   in   the   set   of } 1 0 \} \\ & = 1 - \left(\frac {1 9}{2 0}\right) ^ {1 0} \end{array}
$$

when the last equality follows since each of the 10 coupons will (independently) not be a type i with probability$\frac { 1 9 } { 2 0 }$ . Hence, 

$$
E [ X ] = E \left[ X _ {1} \right] + \dots + E \left[ X _ {2 0} \right] = 2 0 \left[ 1 - \left(\frac {1 9}{2 0}\right) ^ {1 0} \right] = 8. 0 2 5
$$

An important property of the mean arises when one must predict the value of a random variable. That is, suppose that the value of a random variable X is to be predicted. If we predict that X will equal $^ { c , }$ then the square of the “error” involved will be $( X - c ) ^ { 2 }$ We will now show that the average squared error is minimized when we predict that X will equal its mean$\mu .$ . To see this, note that for any constant c 

$$
\begin{array}{r l} & E [ (X - c) ^ {2} ] = E [ (X - \mu + \mu - c) ^ {2} ] \\ & \qquad = E [ (X - \mu) ^ {2} + 2 (\mu - c) (X - \mu) + (\mu - c) ^ {2} ] \\ & \qquad = E [ (X - \mu) ^ {2} ] + 2 (\mu - c) E [ X - \mu ] + (\mu - c) ^ {2} \\ & \qquad = E [ (X - \mu) ^ {2} ] + (\mu - c ^ {2}) \quad \text {since} \quad E [ X - \mu ] = E [ X ] - \mu = 0 \\ & \qquad \geq E [ (X - \mu) ^ {2} ] \end{array}
$$

Hence, the best predictor of a random variable, in terms of minimizing its mean square error, is just its mean. 

## 4.6 VARIANCE

Given a random variable X along with its probability distribution function, it would be extremely useful if we were able to summarize the essential properties of the mass function by certain suitably defined measures. One such measure would be E [X ], the expected value of X . However, while E [X ] yields the weighted average of the possible values of X , it does not tell us anything about the variation, or spread, of these values. For instance, while the following random variables W, Y, and Z having probability mass functions determined by 

$$
W = 0 \quad \mathrm{withprobability1}
$$

$$
Y = \left\{ \begin{array}{c l} - 1 & \text {with probability} \frac {1}{2} \\ 1 & \text {with probability} \frac {1}{2} \end{array} \right.
$$

$$
Z = \left\{ \begin{array}{c l} - 1 0 0 & \text {with probability} \frac {1}{2} \\ 1 0 0 & \text {with probability} \frac {1}{2} \end{array} \right.
$$

all have the same expectation — namely, 0 — there is much greater spread in the possible values of Y than in those of W (which is a constant) and in the possible values of $Z$ than in those of $Y$ . 

Because we expect X to take on values around its mean $E [ X ]$ , it would appear that a reasonable way of measuring the possible variation of X would be to look at how far apart X would be from its mean on the average. One possible way to measure this would be to consider the quantity $E [ | X - \mu | ]$ , where$\mu = E [ X ]$ , and $[ X - \mu ]$ represents the absolute value of $X - \mu$ . However, it turns out to be mathematically inconvenient to deal with this quantity and so a more tractable quantity is usually considered — namely, the expectation of the square of the difference between X and its mean. We thus have the following definition. 

## Definition

If X is a random variable with mean$\mu _ { ; }$ , then the variance of $X ,$ , denoted by$\mathrm { V a r } ( X )$ , is defined by 

$$
\operatorname{Var} (X) = E [ (X - \mu) ^ {2} ]
$$

An alternative formula for$\mathrm { V a r } ( X )$ can be derived as follows: 

$$
{ \begin{array}{r l} & {\operatorname{Var} (X) = E [ (X - \mu) ^ {2} ]} \\ & {\qquad = E [ X ^ {2} - 2 \mu X + \mu^ {2} ]} \\ & {\qquad = E [ X ^ {2} ] - E [ 2 \mu X ] + E [ \mu^ {2} ]} \\ & {\qquad = E [ X ^ {2} ] - 2 \mu E [ X ] + \mu^ {2}} \\ & {\qquad = E [ X ^ {2} ] - \mu^ {2}} \end{array} }
$$

That is, 

$$
\operatorname{Var} (X) = E [ X ^ {2} ] - (E [ X ]) ^ {2}\tag{4.6.1}
$$

or, in words, the variance of X is equal to the expected value of the square of X minus the square of the expected value of X . This is, in practice, often the easiest way to compute$\mathrm { V a r } ( X )$ 

EXAMPLE 4.6a Compute$\mathrm { V a r } ( X )$ when X represents the outcome when we roll a fair die. 

SOLUTION Since$\begin{array} { r } { P \{ X = i \} = \frac { 1 } { 6 } , i = 1 , 2 , 3 , 4 , 5 , 6 , } \end{array}$ , we obtain 

$$
\begin{array}{r l} E [ X ^ {2} ] & = \sum_ {i - 1} ^ {6} i ^ {2} P \{X = i \} \\ & = 1 ^ {2} \left(\frac {1}{6}\right) + 2 ^ {2} \left(\frac {1}{6}\right) + 3 ^ {2} \left(\frac {1}{6}\right) + 4 ^ {2} \left(\frac {1}{6}\right) + 5 ^ {2} \left(\frac {1}{6}\right) + 6 ^ {2} \left(\frac {1}{6}\right) \\ & = \frac {9 1}{6} \end{array}
$$

Hence, since it was shown in Example 4.4a that$\begin{array} { r } { E [ X ] = \frac { 7 } { 2 } } \end{array}$ , we obtain from Equation 4.6.1 that 

$$
\begin{array}{r l} \operatorname{Var} (X) & = E [ X ^ {2} ] - (E [ X ]) ^ {2} \\ & = \frac {9 1}{6} - \left(\frac {7}{2}\right) ^ {2} = \frac {3 5}{1 2} \end{array}
$$

EXAMPLE 4.6b Variance of an Indicator Random Variable. If, for some event A, 

$$
I = \left\{ \begin{array}{l l} 1 & \text { if   event   A   occurs } \\ 0 & \text { if   event   A   does   not   occur } \end{array} \right.
$$

then 

$$
\begin{array}{r l} \operatorname{Var} (I) & = E [ I ^ {2} ] - (E [ I ]) ^ {2} \\ & = E [ I ] - (E [ I ]) ^ {2} \quad \text { since } I ^ {2} = I (\text { as } 1 ^ {2} = 1 \text { and } 0 ^ {2} = 0) \\ & = E [ I ] (1 - E [ I ]) \\ & = P (A) [ 1 - P (A) ] \quad \text { since } E [ I ] = P (A) \text { from   Example   4.4b } \end{array}
$$

A useful identity concerning variances is that for any constants a and $b ,$ 

$$
\operatorname{Var} (a X + b) = a ^ {2} \operatorname{Var} (X)\tag{4.6.2}
$$

To prove Equation 4.6.2, let$\mu = E [ X ]$ and recall that $E [ a X + b ] = a \mu + b .$ . Thus, by the definition of variance, we have 

$$
\begin{array}{r l} & {\mathrm{Var} (a X + b) = E [ (a X + b - E [ a X + b ]) ^ {2} ]} \\ & {\qquad = E [ (a X + b - a \mu - b) ^ {2} ]} \\ & {\qquad = E [ (a X - a \mu) ^ {2} ]} \\ & {\qquad = E [ a ^ {2} (X - \mu) ^ {2} ]} \\ & {\qquad = a ^ {2} E [ (X - \mu) ^ {2} ]} \\ & {\qquad = a ^ {a} \mathrm{Var} (X)} \end{array}
$$

Specifying particular values for a and $b$ in Equation 4.6.2 leads to some interesting corollaries. For instance, by setting $a = 0$ in Equation 4.6.2 we obtain that 

$$
\operatorname{Var} (b) = 0
$$

That is, the variance of a constant is 0. (Is this intuitive?) Similarly, by setting $a = 1$ we obtain 

$$
\operatorname{Var} (X + b) = \operatorname{Var} (X)
$$

That is, the variance of a constant plus a random variable is equal to the variance of the random variable. (Is this intuitive? Think about it.) Finally, setting $b = 0$ yields 

$$
\operatorname{Var} (a X) = a ^ {2} \operatorname{Var} (X)
$$

The quantity$\sqrt { \operatorname { V a r } ( X ) }$ is called the standard deviation of X . The standard deviation has the same units as does the mean. 

## REMARK

Analogous to the mean’s being the center of gravity of a distribution of mass, the variance represents, in the terminology of mechanics, the moment of inertia. 

## 4.7 COVARIANCE AND VARIANCE OF SUMS OF RANDOM VARIABLES

We showed in Section 4.5 that the expectation of a sum of random variables is equal to the sum of their expectations. The corresponding result for variances is, however, not generally valid. Consider 

$$
\begin{array}{r l} \operatorname{Var} (X + X) & = \operatorname{Var} (2 X) \\ & = 2 ^ {2} \operatorname{Var} (X) \\ & = 4 \operatorname{Var} (X) \\ & \neq \operatorname{Var} (X) + \operatorname{Var} (X) \end{array}
$$

There is, however, an important case in which the variance of a sum of random variables is equal to the sum of the variances; and this is when the random variables are independent. Before proving this, however, let us define the concept of the covariance of two random variables. 

## Definition

The covariance of two random variables X and Y , written Cov(X , Y ) is defined by 

$$
\operatorname{Cov} (X, Y) = E [ (X - \mu_ {x}) (Y - \mu_ {y}) ]
$$

where$\mu _ { x }$ and$\mu _ { y }$ are the means of X and Y , respectively. 

A useful expression for$\operatorname { C o v } ( X , Y )$ can be obtained by expanding the right side of the definition. This yields 

$$
\begin{array}{r} \operatorname{Cov} (X, Y) = E [ X Y - \mu_ {x} Y - \mu_ {y} X + \mu_ {x} \mu_ {y} ] \\ = E [ X Y ] - \mu_ {x} E [ Y ] - \mu_ {y} E [ X ] + \mu_ {x} \mu_ {y} \end{array}
$$

$$
\begin{array}{l} {= E [ X Y ] - \mu_ {x} \mu_ {y} - \mu_ {y} \mu_ {x} + \mu_ {x} \mu_ {y}} \\ {= E [ X Y ] - E [ X ] E [ Y ]} \end{array}\tag{4.7.1}
$$

From its definition we see that covariance satisfies the following properties: 

$$
\operatorname{Cov} (X, Y) = \operatorname{Cov} (Y, X)\tag{4.7.2}
$$

and 

$$
\operatorname{Cov} (X, X) = \operatorname{Var} (X)\tag{4.7.3}
$$

Another property of covariance, which immediately follows from its definition, is that, for any constant a, 

$$
\operatorname{Cov} (a X, Y) = a \operatorname{Cov} (X, Y)\tag{4.7.4}
$$

The proof of Equation 4.7.4 is left as an exercise. 

Covariance, like expectation, possesses an additive property. 

## Lemma 4.7.1

$$
\operatorname{Cov} (X + Z, Y) = \operatorname{Cov} (X, Y) + \operatorname{Cov} (Z, Y)
$$

Proof 

$$
\begin{array}{r l} \operatorname{Cov} (X + Z, Y) & = E [ (X + Z) Y ] - E [ X + Z ] E [ Y ] \quad \text { from   Equation   4.7.1 } \\ & = E [ X Y ] + E [ Z Y ] - (E [ X ] + E [ Z ]) E [ Y ] \\ & = E [ X Y ] - E [ X ] E [ Y ] + E [ Z Y ] - E [ Z ] E [ Y ] \\ & = \operatorname{Cov} (X, Y) + \operatorname{Cov} (Z, Y) \quad \square \end{array}
$$

Lemma 4.7.1 can be easily generalized (see Problem 48) to show that 

$$
\operatorname{Cov} \left(\sum_ {i = 1} ^ {n} X _ {i}, Y\right) = \sum_ {i = 1} ^ {n} \operatorname{Cov} (X _ {i}, Y)\tag{4.7.5}
$$

which gives rise to the following. 

PROPOSITION 4.7.2 

$$
\operatorname{Cov} \left(\sum_ {i = 1} ^ {n} X _ {i}, \sum_ {j = 1} ^ {m} Y _ {j}\right) = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \operatorname{Cov} (X _ {i}, Y _ {j})
$$

Proof 

$$
\begin{array}{l} \text {   Proof   } \\ \operatorname{Cov} \left(\sum_ {i = 1} ^ {n} X _ {i}, \sum_ {j = 1} ^ {m} Y _ {j}\right) \\ = \sum_ {i = 1} ^ {n} \operatorname{Cov} \left(X _ {i}, \sum_ {j = 1} ^ {m} Y _ {j}\right) \quad \text { from   Equation   4.7.5 } \\ = \sum_ {i = 1} ^ {n} \operatorname{Cov} \left(\sum_ {j = 1} ^ {m} Y _ {j}, X _ {i}\right) \quad \text { by   the   symmetry   property   Equation   4.7.2 } \\ = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \operatorname{Cov} (Y _ {j}, X _ {i}) \quad \text { again   from   Equation   4.7.5 } \end{array}
$$

and the result now follows by again applying the property Equation 4.7.2.  

Using Equation 4.7.3 gives rise to the following formula for the variance of a sum of random variables. 

Corollary 4.7.3 

$$
\operatorname{Var}\left(\sum_{i = 1}^{n}X_{i}\right) = \sum_{i = 1}^{n}\operatorname{Var}(X_{i}) + \sum_{i = 1}^{n}\sum_{\substack{j = 1\\ j\neq i}}^{n}\operatorname{Cov}(X_{i},X_{j})
$$

## Proof

The proof follows directly from Proposition 4.7.2 upon setting $m = n ,$ , and $Y _ { j } = X _ { j }$ for $j = 1 , \dotsc , n .$  

In the case of n = 2, Corollary 4.7.3 yields that 

$$
\operatorname{Var} (X + Y) = \operatorname{Var} (X) + \operatorname{Var} (Y) + \operatorname{Cov} (X, Y) + \operatorname{Cov} (Y, X)
$$

or, using Equation 4.7.2, 

$$
\operatorname{Var} (X + Y) = \operatorname{Var} (X) + \operatorname{Var} (Y) + 2 \operatorname{Cov} (X, Y)\tag{4.7.6}
$$

## Theorem 4.7.4

If X and Y are independent random variables, then 

$$
\operatorname{Cov} (X, Y) = 0
$$

and so for independent $X _ { 1 } , \dots , X _ { n }$ 

$$
\operatorname{Var} \left(\sum_ {i = 1} ^ {n} X _ {i}\right) = \sum_ {i = 1} ^ {n} \operatorname{Var} (X _ {i})
$$

## Proof

We need to prove that $E [ X Y ] = E [ X ] E [ Y ]$ . Now, in the discrete case, 

$$
\begin{array}{l} E [ X Y ] = \sum_ {j} \sum_ {i} x _ {i} y _ {j} P \{X = x _ {i}, Y = y _ {j} \} \\ \qquad = \sum_ {j} \sum_ {i} x _ {i} y _ {j} P \{X = x _ {i} \} P \{Y = y _ {j} \} \quad \text { by   independence } \\ \qquad = \sum_ {y} y _ {j} P \{Y = y _ {j} \} \sum_ {i} x _ {i} P \{X = x _ {i} \} \\ \qquad = E [ Y ] E [ X ] \end{array}
$$

Because a similar argument holds in all other cases, the result is proven.  

EXAMPLE 4.7a Compute the variance of the sum obtained when 10 independent rolls of a fair die are made. 

SOLUTION Letting $X _ { i }$ denote the outcome of the ith roll, we have that 

$$
\begin{array}{r l} \operatorname{Var} \left(\sum_ {1} ^ {1 0} X _ {i}\right) & = \sum_ {1} ^ {1 0} \operatorname{Var} (X _ {i}) \\ & = 1 0 \frac {3 5}{1 2} \quad \text { from   Example   4.6a } \\ & = \frac {1 7 5}{6} \quad \blacksquare \end{array}
$$

EXAMPLE 4.7b Compute the variance of the number of heads resulting from 10 independent tosses of a fair coin. 

SOLUTION Letting 

$$
I _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   the   } j \text { th   toss   lands   heads } \\ 0 & \text { if   the   } j \text { th   toss   lands   tails } \end{array} \right.
$$

then the total number of heads is equal to 

$$
\sum_ {j = 1} ^ {1 0} I _ {j}
$$

Hence, from Theorem 4.7.4, 

$$
\operatorname{Var} \left(\sum_ {j = 1} ^ {1 0} I _ {j}\right) = \sum_ {j = 1} ^ {1 0} \operatorname{Var} (I _ {j})
$$

Now, since $I _ { j }$ is an indicator random variable for an event having probability$\frac { 1 } { 2 }$ , it follows from Example 4.6b that 

$$
\operatorname{Var} (I _ {j}) = \frac {1}{2} \left(1 - \frac {1}{2}\right) = \frac {1}{4}
$$

and thus 

$$
\operatorname{Var} \left(\sum_ {j = 1} ^ {1 0} I _ {j}\right) = \frac {1 0}{4} \quad \blacksquare
$$

The covariance of two random variables is important as an indicator of the relationship between them. For instance, consider the situation where X and Y are indicator variable for whether or not the events A and B occur. That is, for events A and B, define 

$$
X = \left\{ \begin{array}{l l} 1 & \text { if   } A \text {   occurs } \\ 0 & \text { otherwise } \end{array} \right., \qquad Y = \left\{ \begin{array}{l l} 1 & \text { if   } B \text {   occurs } \\ 0 & \text { otherwise } \end{array} \right.
$$

and note that 

$$
X Y = \left\{ \begin{array}{l l} 1 & \text { if } X = 1, Y = 1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Thus, 

$$
\begin{array}{r l} & {\operatorname{Cov} (X, Y) = E [ X Y ] - E [ X ] E [ Y ]} \\ & {\qquad = P \{X = 1, Y = 1 \} - P \{X = 1 \} P \{Y = 1 \}} \end{array}
$$

From this we see that 

$$
\operatorname{Cov} (X, Y) > 0 \Leftrightarrow P \{X = 1, Y = 1 \} > P \{X = 1 \} P \{Y = 1 \}
$$

$$
\begin{array}{l} \Leftrightarrow \frac {P \{X = 1 , Y = 1 \}}{P \{X = 1 \}} > P \{Y = 1 \} \\ \Leftrightarrow P \{Y = 1 | X = 1 \} > P \{Y = 1 \} \end{array}
$$

That is, the covariance of X and Y is positive if the outcome $X = 1$ makes it more likely that $Y = 1$ (which, as is easily seen by symmetry, also implies the reverse). 

In general, it can be shown that a positive value of$\operatorname { C o v } ( X , Y )$ is an indication tha Y tends to increase as X does, whereas a negative value indicates that Y tends to decrease as X increases. The strength of the relationship between X and Y is indicated by the correlation between X and Y , a dimensionless quantity obtained by dividing the covari ance by the product of the standard deviations of X and Y . That is, 

$$
\operatorname{Corr} (X, Y) = \frac {\operatorname{Cov} (X , Y)}{\sqrt {\operatorname{Var} (X) \operatorname{Var} (Y)}}
$$

It can be shown (see Problem 49) that this quantity always has a value between −1 and +1. 

## 4.8 MOMENT GENERATING FUNCTIONS

The moment generating function$\phi ( t )$ of the random variable X is defined for all values t by 

$$
\phi (t) = E [ e ^ {t X} ] = \left\{ \begin{array}{l l} \sum_ {x} e ^ {t x} p (x) & \text { if   } X \text {   is   discrete } \\ \int_ {- \infty} ^ {\infty} e ^ {t x} f (x)   d x & \text { if   } X \text {   is   continuous } \end{array} \right.
$$

We call$\phi ( t )$ the moment generating function because all of the moments of X can be obtained by successively differentiating$\phi ( t )$ . For example, 

$$
\begin{array}{r} \phi^ {\prime} (t) = \frac {d}{d t} E [ e ^ {t X} ] \\ = E \left[ \frac {d}{d t} (e ^ {t X}) \right] \\ = E [ X e ^ {t X} ] \end{array}
$$

Hence, 

$$
\phi^ {\prime} (0) = E [ X ]
$$

Similarly, 

$$
\begin{array}{r} \phi^ {\prime \prime} (t) = \frac {d}{d t} \phi^ {\prime} (t) \\ = \frac {d}{d t} E [ X e ^ {t X} ] \end{array}
$$

$$
= E \left[ \frac {d}{d t} (X e ^ {t X}) \right]
$$

$$
= E [ X ^ {2} e ^ {t X} ]
$$

and so 

$$
\phi^ {\prime \prime} (0) = E [ X ^ {2} ]
$$

In general, the nth derivative of$\phi ( t )$ evaluated at $t = 0$ equals $E [ X ^ { n } ]$ ; that is, 

$$
\phi^ {n} (0) = E [ X ^ {n} ], \quad n \geq 1
$$

An important property of moment generating functions is that the moment generating function of the sum of independent random variables is just the product of the individual moment generating functions. To see this, suppose that X and Y are independent and have moment generating functions$\phi _ { X } ( t )$ and$\phi _ { Y } ( t )$ , respectively. Then$\phi _ { X + Y } ( t )$ , the moment generating function of $X + Y$ , is given by 

$$
\begin{array}{r l} & {\phi_ {X + Y} (t) = E [ e ^ {t (X + Y)} ]} \\ & {\qquad = E [ e ^ {t X} e ^ {t Y} ]} \\ & {\qquad = E [ e ^ {t X} ] E [ e ^ {t Y} ]} \\ & {\qquad = \phi_ {X} (t) \phi_ {Y} (t)} \end{array}
$$

where the next to the last equality follows from Theorem 4.7.4 since X and ${ \cal Y } ,$ , and thu $e ^ { t X }$ and $e ^ { t Y }$ , are independent. 

Another important result is that the moment generating function uniquely determines the distribution. That is, there exists a one-to-one correspondence between the moment generating function and the distribution function of a random variable. 

## 4.9 CHEBYSHEV’S INEQUALITY AND THE WEAK LAW OF LARGE NUMBERS

We start this section by proving a result known as Markov’s inequality. 

## PROPOSITION 4.9.1 MARKOV’S INEQUALITY

If X is a random variable that takes only nonnegative values, then for any value $a > 0$ 

$$
P \{X \geq a \} \leq \frac {E [ X ]}{a}
$$

## Proof

We give a proof for the case where X is continuous with density f . 

$$
\begin{array}{l} E [ X ] = \int_ {0} ^ {\infty} x f (x) d x \\ \qquad = \int_ {0} ^ {a} x f (x) d x + \int_ {a} ^ {\infty} x f (x) d x \\ \qquad \geq \int_ {a} ^ {\infty} x f (x) d x \\ \qquad \geq \int_ {a} ^ {\infty} a f (x) d x \\ \qquad = a \int_ {a} ^ {\infty} f (x) d x \\ \qquad = a P \{X \geq a \} \end{array}
$$

and the result is proved.  

As a corollary, we obtain Proposition 4.9.2. 

## PROPOSITION 4.9.2 CHEBYSHEV’S INEQUALITY

If X is a random variable with mean$\mu$ and variance$\sigma ^ { 2 }$ , then for any value $k > 0$ 

$$
P \{| X - \mu | \geq k \} \leq \frac {\sigma^ {2}}{k ^ {2}}
$$

## Proof

Since $( X - \mu ) ^ { 2 }$ is a nonnegative random variable, we can apply Markov’s inequality (with $a = k ^ { 2 } )$ to obtain 

$$
P \{(X - \mu) ^ {2} \geq k ^ {2} \} \leq \frac {E [ (X - \mu) ^ {2} ]}{k ^ {2}}\tag{4.9.1}
$$

But since $( X - \mu ) \geq k ^ { 2 }$ if and only$\mathrm { i f } \left| X - \mu \right| \geq k$ , Equation 4.9.1 is equivalent to 

$$
P \{| X - \mu | \geq k \} \leq \frac {E [ (X - \mu) ^ {2} ]}{k ^ {2}} = \frac {\sigma^ {2}}{k ^ {2}}
$$

and the proof is complete.  

The importance of Markov’s and Cheybyshev’s inequalities is that they enable us to derive bounds on probabilities when only the mean, or both the mean and the variance, of the probability distribution are known. Of course, if the actual distribution were known, then the desired probabilities could be exactly computed and we would not need to resort to bounds. 

EXAMPLE 4.9a Suppose that it is known that the number of items produced in a factory during a week is a random variable with mean 50. 

(a) What can be said about the probability that this week’s production will exceed 75? 

(b) If the variance of a week’s production is known to equal 25, then what can be said about the probability that this week’s production will be between 40 and 60? 

SOLUTION Let X be the number of items that will be produced in a week: 

(a) By Markov’s inequality 

$$
P \{X > 7 5 \} \leq \frac {E [ X ]}{7 5} = \frac {5 0}{7 5} = \frac {2}{3}
$$

(b) By Chebyshev’s inequality 

$$
P \{| X - 5 0 | \geq 1 0 \} \leq \frac {\sigma^ {2}}{1 0 ^ {2}} = \frac {1}{4}
$$

Hence 

$$
P \{| X - 5 0 | <   1 0 \} \geq 1 - \frac {1}{4} = \frac {3}{4}
$$

and so the probability that this week’s production will be between 40 and 60 is at least .75. ■ 

By replacing k by kσ in Equation 4.9.1, we can write Chebyshev’s inequality as 

$$
P \{| X - \mu | > k \sigma \} \leq 1 / k ^ {2}
$$

Thus it states that the probability a random variable differs from its mean by more than k standard deviations is bounded by $1 / k ^ { 2 }$ 

We will end this section by using Chebyshev’s inequality to prove the weak law of large numbers, which states that the probability that the average of the first n terms in a sequence of independent and identically distributed random variables differs by its mean by more than ε goes to 0 as n goes to infinity. 

## Theorem 4.9.3 The Weak Law of Large Numbers

Let $X _ { 1 } , X _ { 2 } , \ldots$ , be a sequence of independent and identically distributed random variables, each having mean $E [ X _ { i } ] = \mu$ . Then, for any$\varepsilon > 0$ , 

$$
P \left\{\left| \frac {X _ {1} + \cdots + X _ {n}}{n} - \mu \right| > \varepsilon \right\}\rightarrow 0 \quad \text { as } n \rightarrow \infty
$$

## Proof

We shall prove the result only under the additional assumption that the random variables have a finite variance$\sigma ^ { 2 }$ . Now, as 

$$
E \left[ \frac {X _ {1} + \cdots + X _ {n}}{n} \right] = \mu \quad \text { and } \quad \operatorname{Var} \left(\frac {X _ {1} + \cdots + X _ {n}}{n}\right) = \frac {\sigma^ {2}}{n}
$$

it follows from Chebyshev’s inequality that 

$$
P \left\{\left| \frac {X _ {1} + \cdots + X _ {n}}{n} - \mu \right| > \epsilon \right\} \leq \frac {\sigma^ {2}}{n \epsilon^ {2}}
$$

and the result is proved.  

For an application of the above, suppose that a sequence of independent trials is performed. Let E be a fixed event and denote by $P ( E )$ the probability that E occurs on a given trial. Letting 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   } E \text {   occurs   on   trial   } i \\ 0 & \text { if   } E \text {   does   not   occur   on   trial   } i \end{array} \right.
$$

it follows that $X _ { 1 } + X _ { 2 } + \cdots + X _ { n }$ represents the number of times that E occurs in the first n trials. Because $E [ X _ { i } ] = P ( E )$ , it thus follows from the weak law of large numbers that for any positive number ε, no matter how small, the probability that the proportion of the first n trials in which E occurs differs from $P ( E )$ by more than ε goes to 0 as n increases. 

## Problems

1. Five men and 5 women are ranked according to their scores on an examination. Assume that no two scores are alike and all 10! possible rankings are equally likely. Let X denote the highest ranking achieved by a woman (for instance,$X = 2$ if the top-ranked person was male and the next-ranked person was female). Find$\textstyle P \{ X = i \} , i = 1 , 2 , 3 , \dotsc , 8 , 9 , 1 0 .$ 

2. Let X represent the difference between the number of heads and the number of tails obtained when a coin is tossed n times. What are the possible values of X ? 

3. In Problem 2, if the coin is assumed fair, for $n = 3$ , what are the probabilities associated with the values that X can take on? 

4. The distribution function of the random variable X is given 

$$
F (x) = \left\{ \begin{array}{l l} 0 & x <   0 \\ \frac {x}{2} & 0 \leq x <   1 \\ \frac {2}{3} & 1 \leq x <   2 \\ \frac {1 1}{1 2} & 2 \leq x <   3 \\ 1 & 3 \leq x \end{array} \right.
$$

(a) Plot this distribution function. 

(b) What is$\begin{array} { r } { P \{ X > \frac { 1 } { 2 } \} ; } \end{array}$ 

(c) What is $P \{ 2 < \bar { X } \leq 4 \} \ddagger$ 

(d) What is $P \{ X < 3 \} \colon$ 

(e) What is $P \{ X = 1 \} \colon$ 

5. Suppose you are given the distribution function F of a random variable X . Explain how you could determine $P \{ X = 1 \}$ }. (Hint: You will need to use the concept of a limit.) 

6. The amount of time, in hours, that a computer functions before breaking down is a continuous random variable with probability density function given by 

$$
f (x) = \left\{ \begin{array}{l l} \lambda e ^ {- x / 1 0 0} & x \geq 0 \\ 0 & x <   0 \end{array} \right.
$$

What is the probability that a computer will function between 50 and 150 hours before breaking down? What is the probability that it will function less than 100 hours? 

7. The lifetime in hours of a certain kind of radio tube is a random variable having a probability density function given by 

$$
f (x) = \left\{ \begin{array}{l l} 0 & x \leq 1 0 0 \\ \frac {1 0 0}{x ^ {2}} & x > 1 0 0 \end{array} \right.
$$

What is the probability that exactly 2 of 5 such tubes in a radio set will have to be replaced within the first 150 hours of operation? Assume that the events $E _ { i } , i = 1 , 2 , 3 , 4 , 5$ , that the ith such tube will have to be replaced within this time are independent. 

8. If the density function of X equals 

$$
f (x) = \left\{ \begin{array}{l l} c e ^ {- 2 x} & 0 <   x <   \infty \\ 0 & x <   0 \end{array} \right.
$$

find c. What is $P \{ X > 2 \} \colon$ 

9. A bin of 5 transistors is known to contain 3 that are defective. The transistors are to be tested, one at a time, until the defective ones are identified. Denote by $N _ { 1 }$ the number of tests made until the first defective is spotted and by $N _ { 2 }$ the number of additional tests until the second defective is spotted; find the joint probability mass function of $N _ { 1 }$ and $N _ { 2 }$ 

10. The joint probability density function of X and Y is given by 

$$
f (x, y) = \frac {6}{7} \left(x ^ {2} + \frac {x y}{2}\right), \quad 0 <   x <   1, \quad 0 <   y <   2
$$

(a) Verify that this is indeed a joint density function. 

(b) Compute the density function of X . 

(c) Find $P \{ X > Y \}$ 

11. Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ be independent random variables, each having a uniform distribution over (0, 1). Let M = maximum $( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } )$ . Show that the distribution function of $M , F _ { M } ( \cdot )$ , is given by 

$$
F _ {M} (x) = x ^ {n}, \quad 0 \leq x \leq 1
$$

What is the probability density function of M ? 

12. The joint density of X and Y is given by 

$$
f (x, y) = \left\{ \begin{array}{l l} x e ^ {(- x + y)} & x > 0, y > 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Compute the density of X . 

(b) Compute the density of Y . 

(c) Are X and Y independent? 

13. The joint density of X and Y is 

$$
f (x, y) = \left\{ \begin{array}{l l} 2 & 0 <   x <   y, 0 <   y <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Compute the density of X . 

(b) Compute the density of Y . 

(c) Are X and Y independent? 

14. If the joint density function of X and Y factors into one part depending only on x and one depending only on y, show that X and Y are independent. That is, if 

$$
f (x, y) = k (x) l (y), \quad - \infty <   x <   \infty , \quad - \infty <   y <   \infty
$$

show that X and Y are independent. 

15. Is Problem 14 consistent with the results of Problems 12 and 13? 

16. Suppose that X and Y are independent continuous random variables. Show that 

$$
(\mathbf {a}) P \{X + Y \leq a \} = \int_ {- \infty} ^ {\infty} F _ {X} (a - y) f _ {Y} (y) d y
$$

(b)$P \{ X \leq Y \} = \int _ { - \infty } ^ { \infty } F _ { X } ( y ) f _ { Y } ( y ) d y$ 

where $f _ { Y }$ is the density function of $Y ,$ , and $F _ { X }$ is the distribution function of $X .$ . 

17. When a current I (measured in amperes) flows through a resistance R (measured in ohms), the power generated (measured in watts) is given by $W = I ^ { 2 } R$ . Suppose that I and R are independent random variables with densities 

$$
\begin{array}{l} f _ {I} (x) = 6 x (1 - x) \quad 0 \leq x \leq 1 \\ f _ {R} (x) = 2 x \quad 0 \leq x \leq 1 \end{array}
$$

Determine the density function of $W .$ . 

18. In Example 4.3b, determine the conditional probability mass function of the size of a randomly chosen family containing 2 girls. 

19. Compute the conditional density function of X given $Y = y$ in (a) Problem 10 and (b) Problem 13. 

20. Show that X and Y are independent if and only if 

(a)${ P _ { X / Y } } ^ { ( x / y ) } = p _ { X } ( x )$ in the discrete case 

(b)$f _ { X / Y } { } ^ { ( x / y ) } = f _ { X } ( x )$ in the continuous case 

21. Compute the expected value of the random variable in Problem 1. 

22. Compute the expected value of the random variable in Problem 3. 

23. Each night different meteorologists give us the “probability” that it will rain the next day. To judge how well these people predict, we will score each of them as follows: If a meteorologist says that it will rain with probability ${ \boldsymbol { p } } ,$ then he or she will receive a score of 

$$
\begin{array}{l l} 1 - (1 - p) ^ {2} & \text {if it does rain} \\ 1 - p ^ {2} & \text {if it does not rain} \end{array}
$$

We will then keep track of scores over a certain time span and conclude that the meteorologist with the highest average score is the best predictor of weather. Suppose now that a given meteorologist is aware of this and so wants to maximize his or her expected score. If this individual truly believes that it will rain tomorrow with probability$\boldsymbol { p } ^ { * }$ , what value of p should he or she assert so as to maximize the expected score? 

24. An insurance company writes a policy to the effect that an amount of money A must be paid if some event E occurs within a year. If the company estimates that E will occur within a year with probability ${ \boldsymbol { p } } ,$ what should it charge the customer so that its expected profit will be 10 percent of A? 

25. A total of 4 buses carrying 148 students from the same school arrive at a football stadium. The buses carry, respectively, 40, 33, 25, and 50 students. One of the students is randomly selected. Let X denote the number of students that were on the bus carrying this randomly selected student. One of the 4 bus drivers is also randomly selected. Let Y denote the number of students on her bus. 

(a) Which of E [X ] or E [Y ] do you think is larger? Why? 

(b) Compute E[X ] and E[Y ]. 

26. Suppose that two teams play a series of games that end when one of them has won i games. Suppose that each game played is, independently, won by team A with probability$\mathbf { \nabla } ^ { p . }$ Find the expected number of games that are played when $i = 2$ Also show that this number is maximized when$\textstyle { p = { \frac { 1 } { 2 } } }$ 

27. The density function of X is given by 

$$
f (x) = \left\{ \begin{array}{l l} a + b x ^ {2} & 0 \leq x \leq 1 \\ 0 & \text { otherwise } \end{array} \right.
$$

If$\begin{array} { r } { E [ X ] = \frac { 3 } { 5 } } \end{array}$ , find $a , b .$ 

28. The lifetime in hours of electronic tubes is a random variable having a probability density function given by 

$$
f (x) = a ^ {2} x e ^ {- a x}, \quad x \geq 0
$$

Compute the expected lifetime of such a tube. 

29. Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ be independent random variables having the common density function 

$$
f (x) = \left\{ \begin{array}{l l} 1 & 0 <   x <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Find (a)$E [ \operatorname { M a x } ( X _ { i } , \dots , X _ { n } ) ]$ and (b)$E [ \mathrm { M i n } ( X _ { 1 } , \dots , X _ { n } ) ]$ 

30. Suppose that X has density function 

$$
f (x) = \left\{ \begin{array}{l l} 1 & 0 <   x <   1 \\ 0 & \text { otherwise } \end{array} \right.
$$

Compute $E [ X ^ { n } ] \left( \mathbf { a } \right)$ by computing the density of $X _ { n }$ and then using the definition of expectation and (b) by using Proposition 4.5.1. 

31. The time it takes to repair a personal computer is a random variable whose density, in hours, is given by 

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{2} & 0 <   x <   2 \\ 0 & \text { otherwise } \end{array} \right.
$$

The cost of the repair depends on the time it takes and is equal to $4 0 + 3 0 { \sqrt { x } }$ when the time is x. Compute the expected cost to repair a personal computer. 

32. If $E [ X ] = 2$ and $E [ X ^ { 2 } ] = 8$ , calculate (a)$E [ ( 2 + 4 X ) ^ { 2 } ) ]$ and (b)$E [ X ^ { 2 } + ( X + 1 ) ^ { 2 } ]$ 

33. Ten balls are randomly chosen from an urn containing 17 white and 23 black balls. Let X denote the number of white balls chosen. Compute $E [ X ]$ 

(a) by defining appropriate indicator variables $X _ { i } , i = 1 , \dotsc , 1 0$ so that 

$$
X = \sum_ {i = 1} ^ {1 0} X _ {i}
$$

(b) by defining appropriate indicator variables $Y _ { i } , = 1 , \dots , 1 7$ so that 

$$
X = \sum_ {i = 1} ^ {1 7} Y _ {i}
$$

34. If X is a continuous random variable having distribution function $F _ { ; }$ , then it median is defined as that value of m for which 

$$
F (m) = 1 / 2
$$

Find the median of the random variables with density function 

(a)$f ( x ) = e ^ { - x } , \quad x \geq 0 ;$ 

(b)$f ( x ) = 1 , \quad 0 \leq x \leq 1 .$ 

35. The median, like the mean, is important in predicting the value of a random variable. Whereas it was shown in the text that the mean of a random variable is the best predictor from the point of view of minimizing the expected value of the square of the error, the median is the best predictor if one wants to minimize the expected value of the absolute error. That is,$E [ | X - c | ]$ is minimized when $c$ is the median of the distribution function of X . Prove this result when X is continuous with distribution function $F$ and density function $f .$ . (Hint: Write 

$$
\begin{array}{r l} & E [ | X - c | ] = \int_ {- \infty} ^ {\infty} | x - c | f (x) d x \\ & \qquad = \int_ {- \infty} ^ {c} | x - c | f (x) d x + \int_ {c} ^ {\infty} | x - c | f (x) d x \\ & \qquad = \int_ {- \infty} ^ {c} (c - x) f (x) d x + \int_ {c} ^ {\infty} (x - c) f (x) d x \\ & \qquad = c F (c) - \int_ {- \infty} ^ {c} x f (x) d x + \int_ {c} ^ {\infty} x f (x) d x - c [ 1 - F (c) ] \end{array}
$$

Now, use calculus to find the minimizing value of $c . )$ 

36. We say that $m _ { \phi }$ is the 100p percentile of the distribution function F if 

$$
F (m _ {p}) = p
$$

Find $m _ { \phi }$ for the distribution having density function 

$$
f (x) = 2 e ^ {- 2 x}, \quad x \geq 0
$$

37. A community consists of 100 married couples. If during a given year 50 of the members of the community die, what is the expected number of marriages that remain intact? Assume that the set of people who die is equally likely to be any of the$\left( { 2 0 0 } \atop 5 0 \right)$ groups of size 50. (Hint: For i = 1, . . . , 100 let 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   neither   member   of   couple } i \text { dies } \\ 0 & \text { otherwise } \end{array} \right.
$$

38. Compute the expectation and variance of the number of successes in n independent trials, each of which results in a success with probability$\scriptstyle { \boldsymbol { p } } .$ Is independence necessary? 

39. Suppose that X is equally likely to take on any of the values 1, 2, 3, 4. Compute (a) E [X ] and (b) Var(X ). 

40. Let $p _ { i } = P \{ X = i \}$ and suppose that $p _ { 1 } + p _ { 2 } + p _ { 3 } = 1$ . If $E [ X ] = 2$ , what values of$\cdot _ { p 1 } , _ { \ l } p _ { 2 } , _ { \ l } p _ { 3 }$ (a) maximize and (b) minimize Var(X )? 

41. Compute the mean and variance of the number of heads that appear in 3 flips of a fair coin. 

42. Argue that for any random variable X 

$$
E [ X ^ {2} ] \geq (E [ X ]) ^ {2}
$$

When does one have equality? 

43. A random variable X , which represents the weight (in ounces) of an article, has density function given by f (z), 

$$
f (z) = \left\{ \begin{array}{l l} (z - 8) & \text { for } 8 \leq z \leq 9 \\ (1 0 - z) & \text { for } 9 <   z \leq 1 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Calculate the mean and variance of the random variable X . 

(b) The manufacturer sells the article for a fixed price of $2.00. He guarantees to refund the purchase money to any customer who finds the weight of his article to be less than 8.25 oz. His cost of production is related to the weight of the article by the relation x/15 + .35. Find the expected profit per article. 

44. Suppose that the Rockwell hardness X and abrasion loss Y of a specimen (coded data) have a joint density given by 

$$
f _ {X Y} (u, v) = \left\{ \begin{array}{l l} u + v & \text { for } 0 \leq u, v \leq 1 \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Find the marginal densities of X and $Y .$ 

(b) Find E(X ) and$\mathrm { V a r } ( X )$ 

45. A product is classified according to the number of defects it contains and the factory that produces it. Let $X _ { 1 }$ and $X _ { 2 }$ be the random variables that represent the number of defects per unit (taking on possible values of 0, 1, 2, or 3) and the factory number (taking on possible values 1 or 2), respectively. The entries in the table represent the joint possibility mass function of a randomly chosen product. 

<table><tr><td><eq>X_1</eq></td><td><eq>X_2</eq></td><td>1</td><td>2</td></tr><tr><td>0</td><td></td><td><eq>\frac{1}{8}</eq></td><td><eq>\frac{1}{16}</eq></td></tr><tr><td>1</td><td></td><td><eq>\frac{1}{16}</eq></td><td><eq>\frac{1}{16}</eq></td></tr><tr><td>2</td><td></td><td><eq>\frac{3}{16}</eq></td><td><eq>\frac{1}{8}</eq></td></tr><tr><td>3</td><td></td><td><eq>\frac{1}{8}</eq></td><td><eq>\frac{1}{4}</eq></td></tr></table>

(a) Find the marginal probability distributions of $X _ { 1 }$ and $X _ { 2 }$ . 

(b) Find E [(X )], E [(X )], Var(X ), Var(X ), and$\mathrm { C o v } ( X _ { 1 } , X _ { 2 } )$ 

46. A machine makes a product that is screened (inspected 100 percent) before being shipped. The measuring instrument is such that it is difficult to read between 1 and $1 { \frac { 1 } { 3 } }$ (coded data). After the screening process takes place, the measured dimension has density 

$$
f (z) = \left\{ \begin{array}{l l} k z ^ {2} & \text { for } 0 \leq z \leq 1 \\ 1 & \text { for } 1 <   z \leq 1 \frac {1}{3} \\ 0 & \text { otherwise } \end{array} \right.
$$

(a) Find the value of $k .$ 

(b) What fraction of the items will fall outside the twilight zone (fall between 0 and 1)? 

(c) Find the mean and variance of this random variable. 

47. Verify Equation 4.7.4. 

48. Prove Equation 4.7.5 by using mathematical induction. 

49. Let X have variance$\sigma _ { x } ^ { 2 }$ and let Y have variance$\sigma _ { y } ^ { 2 }$ . Starting with 

$$
0 \leq \operatorname{Var} (X / \sigma_ {x} + Y / \sigma_ {y})
$$

show that 

$$
- 1 \leq \operatorname{Corr} (X, Y)
$$

Now using that 

$$
0 \leq \operatorname{Var} (X / \sigma_ {x} - Y / \sigma_ {y})
$$

conclude that 

$$
- 1 \leq \operatorname{Corr} (X, Y) \leq 1
$$

Using the result that$\mathrm { V a r } ( Z ) ~ = ~ 0$ implies that $Z$ is constant, argue that if$\operatorname { C o r r } ( X , Y ) = 1 \ \mathrm { o r } - 1$ then X and Y are related by 

$$
Y = a + b x
$$

where the sign of $b$ is positive when the correlation is 1 and negative when it is −1. 

50. Consider n independent trials, each of which results in any of the outcomes $i , i =$ 1, 2, 3, with respective probabilities$\begin{array} { r } { p _ { 1 } , p _ { 2 } , p _ { 3 } , \sum _ { i = 1 } ^ { 3 } \gamma _ { i } = 1 } \end{array}$ . Let $N _ { i }$ denote the number of trials that result in outcome i, and show that$\operatorname { C o v } ( N _ { 1 } , N _ { 2 } ) = - n p _ { 1 } p _ { 2 }$ Also explain why it is intuitive that this covariance is negative. (Hint: For $i =$$1 , \ldots , n ,$ , let 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   trial   } i \text {   results   in   outcome   } 1 \\ 0 & \text { if   trial   } i \text {   does   not   result   in   outcome   } 1 \end{array} \right.
$$

Similarly, for $j = 1 , \dots , n ,$ , let 

$$
Y _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   trial   } j \text {   results   in   outcome   } 2 \\ 0 & \text { if   trial   } j \text {   does   not   result   in   outcome   } 2 \end{array} \right.
$$

Argue that 

$$
N _ {1} = \sum_ {i = 1} ^ {n} X _ {i}, \quad N _ {2} = \sum_ {j = 1} ^ {n} Y _ {j}
$$

Then use Proposition 4.7.2 and Theorem 4.7.4.) 

51. In Example 4.5f, compute$\operatorname { C o v } ( X _ { i } , X _ { j } )$ and use this result to show that$\mathrm { V a r } ( X ) = 1$ 

52. If $X _ { 1 }$ and $X _ { 2 }$ have the same probability distribution function, show that 

$$
\operatorname{Cov} (X _ {1} - X _ {2}, X _ {1} + X _ {2}) = 0
$$

Note that independence is not being assumed. 

53. Suppose that X has density function 

$$
f (x) = e ^ {- x}, \quad x > 0
$$

Compute the moment generating function of X and use your result to determine its mean and variance. Check your answer for the mean by a direct calculation. 

54. If the density function of X is 

$$
f (x) = 1, \quad 0 <   x <   1
$$

determine $E [ e ^ { t X } ]$ . Differentiate to obtain $E [ X ^ { n } ]$ and then check your answer. 

55. Suppose that X is a random variable with mean and variance both equal to 20. What can be said about $P \{ 0 \leq X \leq 4 0 \}$ ? 

56. From past experience, a professor knows that the test score of a student taking her final examination is a random variable with mean 75. 

(a) Give an upper bound to the probability that a student’s test score will exceed 85. 

Suppose in addition the professor knows that the variance of a student’s test score is equal to 25. 

(b) What can be said about the probability that a student will score between 65 and 85? 

(c) How many students would have to take the examination so as to ensure, with probability at least .9, that the class average would be within 5 of 75? 

57. Let X and Y have respective distribution functions $F _ { X }$ and $F _ { Y }$ , and suppose that for some constants a and $b > 0$ 

$$
F _ {X} (x) = F _ {Y} \left(\frac {x - a}{b}\right)
$$

(a) Determine E [X ] in terms of E [Y ]. 

(b) Determine Var(X ) in terms of$\mathrm { V a r } ( Y )$ 

Hint: X has the same distribution as what other random variable? 

# SPECIAL RANDOM VARIABLES

Certain types of random variables occur over and over again in applications. In this chapter, we will study a variety of them. 

## 5.1 THE BERNOULLI AND BINOMIAL RANDOM VARIABLES

Suppose that a trial, or an experiment, whose outcome can be classified as either a “success” or as a “failure” is performed. If we let X = 1 when the outcome is a success and $X = 0$ when it is a failure, then the probability mass function of X is given by 

$$
\begin{array}{l} {P \{X = 0 \} = 1 - p} \\ {P \{X = 1 \} = p} \end{array}\tag{5.1.1}
$$

where$\phi , 0 \le { \cal P } \le 1$ , is the probability that the trial is a “success.” 

A random variable X is said to be a Bernoulli random variable (after the Swiss mathe matician James Bernoulli) if its probability mass function is given by Equations 5.1.1 for some ${ \boldsymbol { p } } \in ( 0 , 1 )$ . Its expected value is 

$$
E [ X ] = 1 \cdot P \{X = 1 \} + 0 \cdot P \{X = 0 \} = p
$$

That is, the expectation of a Bernoulli random variable is the probability that the random variable equals 1. 

Suppose now that n independent trials, each of which results in a “success” with prob ability p and in a “failure” with probability $1 - p ,$ are to be performed. If X represents the number of successes that occur in the n trials, then X is said to be a binomial random variable with parameters $( n , p )$ 

The probability mass function of a binomial random variable with parameters n and$\boldsymbol { \mathscr { P } }$ is given by 

$$
P \{X = i \} = \binom {n} {i} p ^ {i} (1 - p) ^ {n - i}, \quad i = 0, 1, \ldots , n\tag{5.1.2}
$$

where$\binom { n } { i } = n ! / [ i ! ( n - i ) ! ]$ is the number of different groups of $i$ objects that can be chosen from a set of n objects. The validity of Equation 5.1.2 may be verified by first noting that the probability of any particular sequence of the n outcomes containing $i$ successes and $n - i$ failures is, by the assumed independence of trials,$p ^ { i } ( 1 - p ) ^ { n - i }$ Equation 5.1.2 then follows since there are$\binom { n } { i }$ different sequences of the n outcomes leading to i successes and $n - i$ failures — which can perhaps most easily be seen by noting that there are$\binom { n } { i }$ different selections of the i trials that result in successes. For instance, if $n = 5 , i = 2$ , then there are$\textstyle { \binom { 5 } { 2 } }$ choices of the two trials that are to result in successes — namely, any of the outcomes 

$$
\begin{array}{l l l} (s, s, f, f, f) & (f, s, s, f, f) & (f, f, s, f, s) \\ (s, f, s, f, f) & (f, s, f, s, f) \\ (s, f, f, s, f) & (f, s, f, f, s) & (f, f, f, s, s) \\ (s, f, f, f, s) & (f, f, s, s, f) \end{array}
$$

where the outcome $( f , s , f , s , f )$ means, for instance, that the two successes appeared on trials 2 and 4. Since each of the$\textstyle { \binom { 5 } { 2 } }$ outcomes has probability$ { p ^ { 2 } ( 1 - p ) ^ { 3 } }$ , we see that the probability of a total of 2 successes in 5 independent trials is ${ \binom { 5 } { 2 } } p ^ { 2 } ( 1 - p ) ^ { 3 }$ . Note that, by the binomial theorem, the probabilities sum to 1, that is, 

$$
\sum_ {i = 0} ^ {\infty} p (i) = \sum_ {i = 0} ^ {n} {\binom {n} {i}} p ^ {i} (1 - p) ^ {n - i} = [ p + (1 - p) ] ^ {n} = 1
$$

The probability mass function of three binomial random variables with respective parameters (10, .5), (10, .3), and (10, .6) are presented in Figure 5.1. The first of these is symmetric about the value .5, whereas the second is somewhat weighted, or skewed, to lower values and the third to higher values. 

EXAMPLE 5.1a It is known that disks produced by a certain company will be defective with probability .01 independently of each other. The company sells the disks in packages of 10 and offers a money-back guarantee that at most 1 of the 10 disks is defective. What proportion of packages is returned? If someone buys three packages, what is the probability that exactly one of them will be returned? 

SOLUTION If X is the number of defective disks in a package, then assuming that customers always take advantage of the guarantee, it follows that X is a binomial random variable with parameters (10, .01). Hence the probability that a package will have to be replaced is 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5d1d72e949afd376f7f0f7e5d263bdb4706e2ea49a1e361c458661793f90412c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/0eeb9633576b2d79af4b76b46d6f400cc7b53ad8c707049b38551f201b923ee8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/3cd5c6dd1e6515523c6f072d9465228f14dff2ee76b560199e2af608f9bc9988.jpg)



FIGURE 5.1 Binomial probability mass functions.


$$
\begin{array}{l} P \{X > 1 \} = 1 - P \{X = 0 \} - P \{X = 1 \} \\ \qquad = 1 - \binom {1 0} {0} (. 0 1) ^ {0} (. 9 9) ^ {1 0} - \binom {1 0} {1} (. 0 1) ^ {1} (. 9 9) ^ {9} \approx . 0 0 5 \end{array}
$$

Because each package will, independently, have to be replaced with probability .005, it follows from the law of large numbers that in the long run .5 percent of the packages will have to be replaced. 

It follows from the foregoing that the number of packages that the person will have to return is a binomial random variable with parameters $n = 3$ and$\begin{array} { r } { \ p = . 0 0 5 } \end{array}$ . Therefore, the probability that exactly one of the three packages will be returned i$\left( { \begin{array} { l } { 3 } \\ { 1 } \end{array} } \right) ( . 0 0 5 ) ( . 9 9 5 ) ^ { 2 } =$ .015. ■ 

EXAMPLE 5.1b The color of one’s eyes is determined by a single pair of genes, with the gene for brown eyes being dominant over the one for blue eyes. This means that an individual having two blue-eyed genes will have blue eyes, while one having either two brown-eyed genes or one brown-eyed and one blue-eyed gene will have brown eyes. When two people mate, the resulting offspring receives one randomly chosen gene from each of its parents gene pair. If the eldest child of a pair of brown-eyed parents has blue eyes, what is the probability that exactly two of the four other children (none of whom is a twin) of this couple also have blue eyes? 

SOLUTION To begin, note that since the eldest child has blue eyes, it follows that both parents must have one blue-eyed and one brown-eyed gene. (For if either had two browneyed genes, then each child would receive at least one brown-eyed gene and would thus have brown eyes.) The probability that an offspring of this couple will have blue eyes is equal to the probability that it receives the blue-eyed gene from both parents, which is$\textstyle { \left( { \frac { 1 } { 2 } } \right) } \left( { \frac { 1 } { 2 } } \right) = { \frac { 1 } { 4 } }$ . Hence, because each of the other four children will have blue eyes with probability$\textstyle { \frac { 1 } { 4 } } ;$ , it follows that the probability that exactly two of them have this eye color is 

$$
\binom {4} {2} (1 / 4) ^ {2} (3 / 4) ^ {2} = 2 7 / 1 2 8 \quad \blacksquare
$$

EXAMPLE 5.1c A communications system consists of n components, each of which will, independently, function with probability$\scriptstyle { \boldsymbol { \phi } } .$ . The total system will be able to operate effectively if at least one-half of its components function. 

(a) For what values of$\boldsymbol { \mathscr { P } }$ is a 5-component system more likely to operate effectively than a 3-component system? 

(b) In general, when is a $2 k + 1$ component system better than a $2 k - 1$ component system? 

## SOLUTION

(a) Because the number of functioning components is a binomial random variable with parameters $( n , p )$ , it follows that the probability that a 5-component system will be effective is 

$$
\binom {5} {3} p ^ {3} (1 - p) ^ {2} + \binom {5} {4} p ^ {4} (1 - p) + p ^ {5}
$$

whereas the corresponding probability for a 3-component system is 

$$
\binom {3} {2} p ^ {2} (1 - p) + p ^ {3}
$$

Hence, the 5-component system is better if 

$$
1 0 p ^ {3} (1 - p) ^ {2} + 5 p ^ {4} (1 - p) + p ^ {5} \geq 3 p ^ {2} (1 - p) + p ^ {3}
$$

which reduces to 

$$
3 (p - 1) ^ {2} (2 p - 1) \geq 0
$$

or 

$$
p \geq \frac {1}{2}
$$

(b) In general, a system with $2 k + 1$ components will be better than one with $2 k - 1$ components if (and only if)$\begin{array} { r } { p \geq \frac { 1 } { 2 } } \end{array}$ . To prove this, consider a system of $2 k + 1$ components and let X denote the number of the first $2 k - 1$ that function. Then 

$$
P _ {2 k + 1} (\mathrm{effective}) = P \{X \geq k + 1 \} + P \{X = k \} (1 - (1 - p) ^ {2}) + P \{X = k - 1 \} p ^ {2}
$$

which follows since the $2 k + 1$ component system will be effective if either (1)$X \geq k + 1$ ; 

(2)$X = k$ and at least one of the remaining 2 components function; or 

(3)$X = k - 1$ and both of the next 2 function. 

Because 

$$
\begin{array}{c} P _ {2 k - 1} (\text { effective }) = P \{X \geq k \} \\ = P \{X = k \} + P \{X \geq k + 1 \} \end{array}
$$

we obtain that 

$$
\begin{array}{l} P _ {2 k + 1} (\text {effective}) - P _ {2 k - 1} (\text {effective}) \\ \quad = P \{X = k - 1 \} p ^ {2} - (1 - p) ^ {2} P \{X = k \} \\ \quad = \binom {2 k - 1} {k - 1} p ^ {k - 1} (1 - p) ^ {k} p ^ {2} - (1 - p) ^ {2} \binom {2 k - 1} {k} p ^ {k} (1 - p) ^ {k - 1} \\ \quad = \binom {2 k - 1} {k} p ^ {k} (1 - p) ^ {k} [ p - (1 - p) ] \qquad \text {since} \binom {2 k - 1} {k - 1} = \binom {2 k - 1} {k} \\ \quad \geq 0 \Leftrightarrow p \geq \frac {1}{2} \quad \blacksquare \end{array}
$$

EXAMPLE 5.1d Suppose that 10 percent of the chips produced by a computer hardware manufacturer are defective. If we order 100 such chips, will X, the number of defective ones we receive, be a binomial random variable? 

SOLUTION The random variable X will be a binomial random variable with parameters (100, .1) if each chip has probability .9 of being functional and if the functioning of successive chips is independent. Whether this is a reasonable assumption when we know that 10 percent of the chips produced are defective depends on additional factors. For instance, suppose that all the chips produced on a given day are always either functional or defective (with 90 percent of the days resulting in functional chips). In this case, if we know that all of our 100 chips were manufactured on the same day, then X will not be a binomial random variable. This is so since the independence of successive chips is not valid. In fact, in this case, we would have 

$$
\begin{array}{c} P \{X = 1 0 0 \} = . 1 \\ P \{X = 0 \} = . 9 \end{array}
$$

Since a binomial random variable X, with parameters n and ${ \boldsymbol { p } } ,$ represents the number of successes in n independent trials, each having success probability ${ \boldsymbol { p } } ,$ , we can represent X as follows: 

$$
X = \sum_ {i = 1} ^ {n} X _ {i}\tag{5.1.3}
$$

where 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   trial   is   a   success } \\ 0 & \text { otherwise } \end{array} \right.
$$

Because the $X _ { i } , i = 1 , \dotsc , n$ are independent Bernoulli random variables, we have that 

$$
\begin{array}{c} {E [ X _ {i} ] = P \{X _ {i} = 1 \} = p} \\ {\mathrm{Var} (X _ {i}) = E [ X _ {i} ^ {2} ] - p ^ {2}} \\ {= p (1 - p)} \end{array}
$$

where the last equality follows since $X _ { i } ^ { 2 } = X _ { i } ;$ , and so $E [ X _ { i } ^ { 2 } ] = E [ X _ { i } ] = p ,$ 

Using the representation Equation 5.1.3, it is now an easy matter to compute the mean and variance of X: 

$$
\begin{array}{c} E [ X ] = \sum_ {i = 1} ^ {n} E [ X _ {i} ] \\ = n p \end{array}
$$

$$
\begin{array}{l l} \operatorname{Var} (X) = \sum_ {i = 1} ^ {n} \operatorname{Var} (X _ {i}) & \text { since   the } X _ {i} \text { are   independent } \\ = n p (1 - p) \end{array}
$$

If $X _ { 1 }$ and $X _ { 2 }$ are independent binomial random variables having respective parameters $( n _ { i } , p ) , i = 1 , 2$ , then their sum is binomial with parameters $( n _ { 1 } + n _ { 2 } , p )$ . This can most easily be seen by noting that because $X _ { i } , i = 1 , 2$ , represents the number of successes in $n _ { i }$ independent trials each of which is a success with probability ${ \boldsymbol { p } } ,$ then $X _ { 1 } + X _ { 2 }$ represents the number of successes in $n _ { 1 } + n _ { 2 }$ independent trials each of which is a success with probability$\mathbf { \nabla } ^ { p . }$ Therefore,$X _ { 1 } + X _ { 2 }$ is binomial with parameters $( n _ { 1 } + n _ { 2 } , p )$ 

## 5.1.1 Computing the Binomial Distribution Function

Suppose that X is binomial with parameters $( n , p )$ . The key to computing its distribution function 

$$
P \{X \leq i \} = \sum_ {k = 0} ^ {i} {\binom {n} {k}} p ^ {k} (1 - p) ^ {n - k}, \qquad i = 0, 1, \ldots , n
$$

is to utilize the following relationship between $P \{ X = k + 1 \}$ and $P \{ X = k \}$ : 

$$
P \{X = k + 1 \} = \frac {p}{1 - p} \frac {n - k}{k + 1} P \{X = k \}\tag{5.1.4}
$$

The proof of this equation is left as an exercise. 

EXAMPLE 5.1e Let X be a binomial random variable with parameters $n = 6 , \phi = . 4$ . Then, starting with $P \{ X = 0 \} = ( . 6 ) ^ { 6 }$ and recursively employing Equation 5.1.4, we obtain 

$$
\begin{array}{l} P \{X = 0 \} = (. 6) ^ {6} = . 0 4 6 7 \\ P \{X = 1 \} = \frac {4}{6} \frac {6}{1} P \{X = 0 \} = . 1 8 6 6 \\ P \{X = 2 \} = \frac {4}{6} \frac {5}{2} P \{X = 1 \} = . 3 1 1 0 \\ P \{X = 3 \} = \frac {4}{6} \frac {4}{3} P \{X = 2 \} = . 2 7 6 5 \\ P \{X = 4 \} = \frac {4}{6} \frac {3}{4} P \{X = 3 \} = . 1 3 8 2 \\ P \{X = 5 \} = \frac {4}{6} \frac {2}{5} P \{X = 4 \} = . 0 3 6 9 \\ P \{X = 6 \} = \frac {4}{6} \frac {1}{6} P \{X = 5 \} = . 0 0 4 1. \end{array}
$$

The text disk uses Equation 5.1.4 to compute binomial probabilities. In using it, one enters the binomial parameters n and$\boldsymbol { \mathscr { P } }$ and a value i and the program computes the probabilities that a binomial $( n , p )$ random variable is equal to and is less than or equal to i. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/c760367d170666d6fe0108a81cc617d241f69497684645f25af6a9bb4b2bbec2.jpg)



FIGURE 5.2


EXAMPLE 5.1f If X is a binomial random variable with parameters $n = 1 0 0$ and$ p = . 7 5$ find $P \{ X = 7 0 \}$ and $P \{ X \leq 7 0 \}$ 

SOLUTION The text disk gives the answers shown in Figure 5.2. ■ 

## 5.2 THE POISSON RANDOM VARIABLE

A random variable X, taking on one of the values 0, 1,$2 , \ldots ,$ is said to be a Poisson random variable with parameter$\lambda , \lambda > 0$ , if its probability mass function is given by 

$$
P \{X = i \} = e ^ {- \lambda} \frac {\lambda^ {i}}{i !}, \qquad i = 0, 1, \ldots\tag{5.2.1}
$$

The symbol e stands for a constant approximately equal to 2.7183. It is a famous constant in mathematics, named after the Swiss mathematician L. Euler, and it is also the base of the so-called natural logarithm. 

Equation 5.2.1 defines a probability mass function, since 

$$
\sum_ {i = 0} ^ {\infty} p (i) = e ^ {- \lambda} \sum_ {i = 0} ^ {\infty} \lambda^ {i} / i! = e ^ {- \lambda} e ^ {\lambda} = 1
$$

A graph of this mass function when$\lambda = 4$ is given in Figure 5.3. 

The Poisson probability distribution was introduced by S. D. Poisson in a book he wrote dealing with the application of probability theory to lawsuits, criminal trials, and the like. This book, published in 1837, was entitled Recherches sur la probabilité des jugements en matière criminelle et en matière civile. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5c04de0ee9e3ebb27466fb2a39c621eb39a86a081e40ae8e2fd59f9be16acd37.jpg)



FIGURE 5.3 The Poisson probability mass function with$\lambda = 4 .$


As a prelude to determining the mean and variance of a Poisson random variable, let us first determine its moment generating function. 

$$
\begin{array}{l} \phi (t) = E [ e ^ {t X} ] \\ \qquad = \sum_ {i = 0} ^ {\infty} e ^ {t i} e ^ {- \lambda} \lambda^ {i} / i! \\ \qquad = e ^ {- \lambda} \sum_ {i = 0} ^ {\infty} (\lambda e ^ {t}) ^ {i} / i! \\ \qquad = e ^ {- \lambda} e ^ {\lambda e ^ {t}} \\ \qquad = \exp \{\lambda (e ^ {t} - 1) \} \end{array}
$$

Differentiation yields 

$$
\begin{array}{r l} & {\phi^ {\prime} (t) = \lambda e ^ {t} \exp \{\lambda (e ^ {t} - 1) \}} \\ & {\phi^ {\prime \prime} (t) = (\lambda e ^ {t}) ^ {2} \exp \{\lambda (e ^ {t} - 1) \} + \lambda e ^ {t} \exp \{\lambda (e ^ {t} - 1) \}} \end{array}
$$

Evaluating at $t = 0$ gives that 

$$
E [ X ] = \phi^ {\prime} (0) = \lambda
$$

$$
\begin{array}{r} \operatorname{Var} (X) = \phi^ {\prime \prime} (0) - (E [ X ]) ^ {2} \\ = \lambda^ {2} + \lambda - \lambda^ {2} = \lambda \end{array}
$$

Thus both the mean and the variance of a Poisson random variable are equal to the parameter λ. 

The Poisson random variable has a wide range of applications in a variety of areas because it may be used as an approximation for a binomial random variable with parameters $( n , p )$ when n is large and$\boldsymbol { \underline { P } }$ is small. To see this, suppose that X is a binomial random variable with parameters $( n , p )$ and let$\lambda = n p$ . Then 

$$
\begin{array}{r l} P \{X = i \} & = \frac {n !}{(n - 1) ! i !} p ^ {i} (1 - p) ^ {n - i} \\ & = \frac {n !}{(n - 1) ! i !} \left(\frac {\lambda}{n}\right) ^ {i} \left(1 - \frac {\lambda}{n}\right) ^ {n - i} \\ & = \frac {n (n - 1) \ldots (n - i + 1)}{n ^ {i}} \frac {\lambda^ {i}}{i !} \frac {(1 - \lambda / n) ^ {n}}{(1 - \lambda / n) ^ {i}} \end{array}
$$

Now, for n large and$\boldsymbol { \mathscr { P } }$ small, 

$$
\left(1 - \frac {\lambda}{n}\right) ^ {n} \approx e ^ {- \lambda} \quad \frac {n (n - 1) \ldots (n - i + 1)}{n ^ {i}} \approx 1 \quad \left(1 - \frac {\lambda}{n}\right) ^ {i} \approx 1
$$

Hence, for n large and$\boldsymbol { \underline { P } }$ small, 

$$
P \{X = i \} \approx e ^ {- \lambda} \frac {\lambda^ {i}}{i !}
$$

In other words, if n independent trials, each of which results in a “success” with probability ${ \boldsymbol { p } } ,$ are performed, then when n is large and$\boldsymbol { \underline { P } }$ small, the number of successes occurring is approximately a Poisson random variable with mean$\lambda = n p$ 

Some examples of random variables that usually obey, to a good approximation, the Poisson probability law (that is, they usually obey Equation 5.2.1 for some value of λ) are: 

1. The number of misprints on a page (or a group of pages) of a book. 

2. The number of people in a community living to 100 years of age. 

3. The number of wrong telephone numbers that are dialed in a day. 

4. The number of transistors that fail on their first day of use. 

5. The number of customers entering a post office on a given day. 

6. The number of α-particles discharged in a fixed period of time from some radioactive particle. 

Each of the foregoing, and numerous other random variables, is approximately Poisson for the same reason — namely, because of the Poisson approximation to the binomial. For instance, we can suppose that there is a small probability p that each letter typed on a page will be misprinted, and so the number of misprints on a given page will be approximately Poisson with mean$\lambda = n p$ where n is the (presumably) large number of letters on that page. Similarly, we can suppose that each person in a given community, independently, has a small probability p of reaching the age 100, and so the number of people that do will have approximately a Poisson distribution with mean np where n is the large number of people in the community. We leave it for the reader to reason out why the remaining random variables in examples 3 through 6 should have approximately a Poisson distribution. 

EXAMPLE 5.2a Suppose that the average number of accidents occurring weekly on a particular stretch of a highway equals 3. Calculate the probability that there is at least one accident this week. 

SOLUTION Let X denote the number of accidents occurring on the stretch of highway in question during this week. Because it is reasonable to suppose that there are a large number of cars passing along that stretch, each having a small probability of being involved in an accident, the number of such accidents should be approximately Poisson distributed. Hence, 

$$
\begin{array}{r l} P \{X \geq 1 \} & = 1 - P \{X = 0 \} \\ & = 1 - e ^ {- 3} \frac {3 ^ {0}}{0 !} \\ & = 1 - e ^ {- 3} \\ & \approx . 9 5 0 2 \quad \blacksquare \end{array}
$$

EXAMPLE 5.2b Suppose the probability that an item produced by a certain machine will be defective is .1. Find the probability that a sample of 10 items will contain at most one defective item. Assume that the quality of successive items is independent. 

SOLUTION The desired probability is$\textstyle { \binom { 1 0 } { 0 } } ( . 1 ) ^ { 0 } ( . 9 ) ^ { 1 0 } + { \binom { 1 0 } { 1 } } ( . 1 ) ^ { 1 } ( . 9 ) ^ { 9 } = . 7 3 6 1$ , whereas the Poisson approximation yields the value 

$$
e ^ {- 1} \frac {1 ^ {0}}{0 !} + e ^ {- 1} \frac {1 ^ {1}}{1 !} = 2 e ^ {- 1} \approx . 7 3 5 8
$$

EXAMPLE 5.2c Consider an experiment that consists of counting the number of α parti cles given off in a one-second interval by one gram of radioactive material. If we know from past experience that, on the average, 3.2 such α-particles are given off, what is a good approximation to the probability that no more than 2 α-particles will appear? 

SOLUTION If we think of the gram of radioactive material as consisting of a large number n of atoms each of which has probability 3.2/n of disintegrating and sending off an α-particle during the second considered, then we see that, to a very close approximation, the number of α-particles given off will be a Poisson random variable with parameter$\lambda = 3 . 2$ . Hence the desired probability is 

$$
\begin{array}{r l} P \{X \leq 2 \} & = e ^ {- 3. 2} + 3. 2 e ^ {- 3. 2} + \frac {(3 . 2) ^ {2}}{2} e ^ {- 3. 2} \\ & = . 3 8 2 \quad \blacksquare \end{array}
$$

EXAMPLE 5.2d If the average number of claims handled daily by an insurance company is 5, what proportion of days have less than 3 claims? What is the probability that there will be 4 claims in exactly 3 of the next 5 days? Assume that the number of claims on different days is independent. 

SOLUTION Because the company probably insures a large number of clients, each having a small probability of making a claim on any given day, it is reasonable to suppose that the number of claims handled daily, call it X, is a Poisson random variable. Since $E ( X ) = 5$ , the probability that there will be fewer than 3 claims on any given day is 

$$
\begin{array}{r l} P \{X \leq 3 \} & = P \{X = 0 \} + P \{X = 1 \} + P \{X = 2 \} \\ & = e ^ {- 5} + e ^ {- 5} \frac {5 ^ {1}}{1 !} + e ^ {- 5} \frac {5 ^ {2}}{2 !} \\ & = \frac {3 7}{2} e ^ {- 5} \\ & \approx . 1 2 4 7 \end{array}
$$

Since any given day will have fewer than 3 claims with probability .125, it follows, from the law of large numbers, that over the long run 12.5 percent of days will have fewer than 3 claims. 

It follows from the assumed independence of the number of claims over successive days that the number of days in a 5-day span that has exactly 4 claims is a binomial random variable with parameters 5 and $P \{ X = 4 \}$ }. Because 

$$
P \{X = 4 \} = e ^ {- 5} \frac {5 ^ {4}}{4 !} \approx . 1 7 5 5
$$

it follows that the probability that 3 of the next 5 days will have 4 claims is equal to 

$$
\binom {5} {3} (. 1 7 5 5) ^ {3} (. 8 2 4 5) ^ {2} \approx . 0 3 6 7 \quad \blacksquare
$$

The Poisson approximation result can be shown to be valid under even more general conditions than those so far mentioned. For instance, suppose that n independent trials are to be performed, with the ith trial resulting in a success with probability $p _ { i } , i = 1 , \ldots , n .$ Then it can be shown that if n is large and each$\mathbf { \nabla } \phi _ { i }$ is small, then the number of successful trials is approximately Poisson distributed with mean equal to$\sum _ { i = 1 } ^ { n } p _ { i }$ . In fact, thi result will sometimes remain true even when the trials are not independent, provided tha their dependence is “weak.” For instance, consider the following example. 

EXAMPLE 5.2e At a party n people put their hats in the center of a room, where the hats are mixed together. Each person then randomly chooses a hat. If X denotes the number of people who select their own hat then, for large $^ { n , }$ it can be shown that X has approximately a Poisson distribution with mean 1. To see why this might be true, let 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   person   selects   his   or   her   own   hat } \\ 0 & \text { otherwise } \end{array} \right.
$$

Then we can express X as 

$$
X = X _ {1} + \dots + X _ {n}
$$

and so X can be regarded as representing the number of “successes” in n “trials” where trial i is said to be a success if the ith person chooses his own hat. Now, since the ith person is equally likely to end up with any of the n hats, one of which is his own, it follows that 

$$
P \{X _ {i} = 1 \} = \frac {1}{n}\tag{5.2.2}
$$

Suppose now that $i \neq j$ and consider the conditional probability that the ith person chooses his own hat given that the jth person does — that is, consider $P \{ X _ { i } = 1 | X _ { j } = 1 \}$ Now given that the jth person indeed selects his own hat, it follows that the ith individual is equally likely to end up with any of the remaining $n - 1$ , one of which is his own. Hence, it follows that 

$$
P \{X _ {i} = 1 | X _ {j} = 1 \} = \frac {1}{n - 1}\tag{5.2.3}
$$

Thus, we see from Equations 5.2.2 and 5.2.3 that whereas the trials are not independent, their dependence is rather weak [since, if the above conditional probability were equal to 1/n rather than $1 / ( n - 1 )$ ), then trials i and j would be independent]; and thus it is not at all surprising that X has approximately a Poisson distribution. The fact that $E [ X ] = 1$ follows since 

$$
\begin{array}{r l} E [ X ] & = E [ X _ {1} + \dots + X _ {n} ] \\ & = E [ X _ {1} ] + \dots + E [ X _ {n} ] \\ & = n \left(\frac {1}{n}\right) = 1 \end{array}
$$

The last equality follows since, from Equation 5.2.2, 

$$
E [ X _ {i} ] = P \{X _ {i} = 1 \} = \frac {1}{n}
$$

The Poisson distribution possesses the reproductive property that the sum of independent Poisson random variables is also a Poisson random variable. To see this, suppose that $X _ { 1 }$ and $X _ { 2 }$ are independent Poisson random variables having respective means$\lambda _ { 1 }$ and$\lambda _ { 2 }$ . Then the moment generating function of $X _ { 1 } + X _ { 2 }$ is as follows: 

$$
\begin{array}{l} E [ e ^ {t (X _ {1} + X _ {2})} ] = E [ e ^ {t X _ {1}} e ^ {t X _ {2}} ] \\ \qquad = E [ e ^ {t X _ {1}} ] E [ e ^ {t} X _ {2} ] \qquad \text { by   independence } \\ \qquad = \exp \{\lambda_ {1} (e ^ {t} - 1) \} \exp \{\lambda_ {2} (e ^ {t} - 1) \} \\ \qquad = \exp \{(\lambda_ {1} + \lambda_ {2}) (e ^ {t} - 1) \} \end{array}
$$

Because exp$\{ ( \lambda _ { 1 } + \lambda _ { 2 } ) ( e ^ { t } - 1 ) \}$ is the moment generating function of a Poisson random variable having mean$\lambda _ { 1 } + \lambda _ { 2 }$ , we may conclude, from the fact that the moment generating function uniquely specifies the distribution, that $X _ { 1 } + X _ { 2 }$ is Poisson with mean$\lambda _ { 1 } + \lambda _ { 2 }$ 

EXAMPLE 5.2f It has been established that the number of defective stereos produced daily at a certain plant is Poisson distributed with mean $4 .$ . Over a 2-day span, what is the probability that the number of defective stereos does not exceed 3? 

SOLUTION Assuming that $X _ { 1 }$ , the number of defectives produced during the first day, is independent of $X _ { 2 }$ , the number produced during the second day, then $X _ { 1 } + X _ { 2 }$ is Poisson with mean 8. Hence, 

$$
P \{X _ {1} + X _ {2} \leq 3 \} = \sum_ {i = 0} ^ {3} e ^ {- 8} \frac {8 ^ {i}}{i !} = . 0 4 2 3 8
$$

Consider now a situation in which a random number, call it N, of events will occur, and suppose that each of these events will independently be a type 1 event with probabilit$\cdot \mathbf { \nabla } _ { \mathbf { \phi } } ^ { p }$ or a type 2 event with probability $1 - p$ . Let $N _ { 1 }$ and $N _ { 2 }$ denote, respectively, the numbers of type 1 and type 2 events that occur. (So $N = N _ { 1 } + N _ { 2 } . )$ If N is Poisson distributed with mean$\lambda _ { i }$ , then the joint probability mass function of $N _ { 1 }$ and $N _ { 2 }$ is obtained as follows. 

$$
\begin{array}{r l} & P \{N _ {1} = n, N _ {2} = m \} = P \{N _ {1} = n, N _ {2} = m, N = n + m \} \\ & \qquad = P \{N _ {1} = n, N _ {2} = m | N = n + m \} P \{N = n + m \} \\ & \qquad = P \{N _ {1} = n, N _ {2} = m | N = n + m \} e ^ {- \lambda} \frac {\lambda^ {n + m}}{(n + m) !} \end{array}
$$

Now, given a total of $n + m$ events, because each one of these events is independently type 1 with probability ${ \boldsymbol { p } } ,$ it follows that the conditional probability that there are exactly n type 1 events (and m type 2 events) is the probability that a binomial $( n + m , p )$ random variable is equal to n. Consequently, 

$$
\begin{array}{c} P \{N _ {1} = n, N _ {2} = m \} = \frac {(n + m) !}{n ! m !} p ^ {n} (1 - p) ^ {m} e ^ {- \lambda} \frac {\lambda^ {n + m}}{(n + m) !} \\ = e ^ {- \lambda p} \frac {(\lambda p) ^ {n}}{n !} e ^ {- \lambda (1 - p)} \frac {(\lambda (1 - p)) ^ {m}}{m !} \end{array}\tag{5.2.4}
$$

The probability mass function of $N _ { 1 }$ is thus 

$$
\begin{array}{l} P \{N _ {1} = n \} = \sum_ {m = 0} ^ {\infty} P \{N _ {1} = n, N _ {2} = m \} \\ \qquad = e ^ {- \lambda p} \frac {(\lambda p) ^ {n}}{n !} \sum_ {m = 0} ^ {\infty} e ^ {- \lambda (1 - p)} \frac {(\lambda (1 - p)) ^ {m}}{m !} \\ \qquad = e ^ {- \lambda p} \frac {(\lambda p) ^ {n}}{n !} \end{array}\tag{5.2.5}
$$

Similarly, 

$$
P \{N _ {2} = m \} = \sum_ {n = 0} ^ {\infty} P \{N _ {1} = n, N _ {2} = m \} = e ^ {- \lambda (1 - p)} \frac {(\lambda (1 - p)) ^ {m}}{m !}\tag{5.2.6}
$$

It now follows from Equations 5.2.4, 5.2.5, and 5.2.6, that $N _ { 1 }$ and $N _ { 2 }$ are independent Poisson random variables with respective means$\lambda _ { P }$ and$\lambda ( 1 - p )$ 

The preceding result generalizes when each of the Poisson number of events can be classified into any of r categories, to yield the following important property of the Poisson distribution: If each of a Poisson number of events having mean λ is independently classified as being of one of the types $1 , \ldots , r ,$ with respective probabilities$\begin{array} { r } { p 1 , \dotsc , \dotsc , \dotsc , \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc } \end{array}$ , then the numbers of type $1 , \ldots , r$ events are independent Poisson random variables with respective means$\lambda p _ { 1 } , \ldots , \lambda p _ { r }$ 

## 5.2.1 Computing the Poisson Distribution Function

If X is Poisson with mean λ, then 

$$
\frac {P \{X = i + 1 \}}{P \{X = i \}} = \frac {e ^ {- \lambda} \lambda^ {i + 1} / (i + 1) !}{e ^ {- \lambda} \lambda^ {i} / i !} = \frac {\lambda}{i + 1}\tag{5.2.7}
$$

Starting with $P \{ X = 0 \} = e ^ { - \lambda }$ , we can use Equation 5.2.7 to successively compute 

$$
P \{X = 1 \} = \lambda P \{X = 0 \}
$$

$$
P \{X = 2 \} = \frac {\lambda}{2} P \{X = 1 \}
$$

$$
P \{X = i + 1 \} = \frac {\lambda}{i + 1} P \{X = i \}
$$

The text disk includes a program that uses Equation 5.2.7 to compute Poisson probabilities. 

## 5.3 THE HYPERGEOMETRIC RANDOM VARIABLE

A bin contains $N + M$ batteries, of which N are of acceptable quality and the other M are defective. A sample of size n is to be randomly chosen (without replacements) in the sense that the set of sampled batteries is equally likely to be any of the$\scriptstyle { \binom { \lambda - M + M } { n } }$ subsets of size n. If we let X denote the number of acceptable batteries in the sample, then 

$$
P \{X = i \} = \frac {\binom {N} {i} \binom {M} {n - i}}{\binom {N + M} {n}}, \qquad i = 0, 1, \ldots , \min (N, n) ^ {*}\tag{5.3.1}
$$

Any random variable X whose probability mass function is given by Equation 5.3.1 is said to be a hypergeometric random variable with parameters $N , M , n .$ 

EXAMPLE 5.3a The components of a 6-component system are to be randomly chosen from a bin of 20 used components. The resulting system will be functional if at least 4 of its 6 components are in working condition. If 15 of the 20 components in the bin are in working condition, what is the probability that the resulting system will be functional? 

SOLUTION If X is the number of working components chosen, then X is hypergeometric with parameters 15, 5, 6. The probability that the system will be functional is 

$$
\begin{array}{l} P \{X \geq 4 \} = \sum_ {i = 4} ^ {6} P \{X = i \} \\ = \frac {\binom {1 5} {4} \binom {5} {2} + \binom {1 5} {5} \binom {5} {1} + \binom {1 5} {6} \binom {5} {0}}{\binom {2 0} {6}} \\ \approx . 8 6 8 7 \quad \blacksquare \end{array}
$$

To compute the mean and variance of a hypergeometric random variable whose prob ability mass function is given by Equation 5.3.1, imagine that the batteries are drawn sequentially and let 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   selection   is   acceptable } \\ 0 & \text { otherwise } \end{array} \right.
$$

Now, since the ith selection is equally likely to be any of the $N + M$ batteries, of which N are acceptable, it follows that 

$$
P \{X _ {i} = 1 \} = \frac {N}{N + M}\tag{5.3.2}
$$

Also, for $i \neq j$ 

$$
\begin{array}{r} P \{X _ {i} = 1, X _ {j} = 1 \} = P \{X _ {i} = 1 \} P \{X _ {j} = 1 | X _ {i} = 1 \} \\ = \frac {N}{N + M} \frac {N - 1}{N + M - 1} \end{array}\tag{5.3.3}
$$

which follows since, given that the ith selection is acceptable, the jth selection is equally likely to be any of the other $N + M - 1$ batteries of which $N - 1$ are acceptable. 

To compute the mean and variance of $X ,$ the number of acceptable batteries in the sample of size n, use the representation 

$$
X = \sum_ {i = 1} ^ {n} X _ {i}
$$

This gives 

$$
E [ X ] = \sum_ {i = 1} ^ {n} E [ X _ {i} ] = \sum_ {i = 1} ^ {n} P \{X _ {i} = 1 \} = \frac {n N}{N + M}\tag{5.3.4}
$$

Also, Corollary 4.7.3 for the variance of a sum of random variables gives 

$$
\operatorname{Var} (X) = \sum_ {i = 1} ^ {n} \operatorname{Var} \left(X _ {i}\right) + 2 \sum_ {1 \leq i <   j \leq n} \operatorname{Cov} \left(X _ {i}, X _ {j}\right)\tag{5.3.5}
$$

Now,$X _ { i }$ is a Bernoulli random variable and so 

$$
\operatorname{Var} (X _ {i}) = P \{X _ {i} = 1 \} (1 - P \{X _ {i} = 1 \}) = \frac {N}{N + M} \frac {M}{N + M}\tag{5.3.6}
$$

Also, for $i < j$ 

$$
\operatorname{Cov} (X _ {i}, X _ {j}) = E [ X _ {i} X _ {j} ] - E [ X _ {i} ] E [ X _ {j} ]
$$

Now, because both $X _ { i }$ and $X _ { j }$ are Bernoulli (that is, 0 − 1) random variables, it follows that $X _ { i } X _ { j }$ is a Bernoulli random variable, and so 

$$
\begin{array}{r l} E [ X _ {i} X _ {j} ] & = P \{X _ {i} X _ {j} = 1 \} \\ & = P \{X _ {i} = 1, X _ {j} = 1 \} \\ & = \frac {N (N - 1)}{(N + M) (N + M - 1)} \quad \text { from   Equation   5.3.3 } \end{array}\tag{5.3.7}
$$

So from Equation 5.3.2 and the foregoing we see that for $i \neq j ,$ 

$$
\begin{array}{r} \mathrm{Cov} (X _ {i}, X _ {j}) = \frac {N (N - 1)}{(N + M) (N + M - 1)} - \left(\frac {N}{N + M}\right) ^ {2} \\ = \frac {- N M}{(N + M) ^ {2} (N + M - 1)} \end{array}
$$

Hence, since there are$\textstyle { \binom { n } { 2 } }$ terms in the second sum on the right side of Equation 5.3.5, we obtain from Equation 5.3.6 

$$
\begin{array}{c} \operatorname{Var} (X) = \frac {n N M}{(N + M) ^ {2}} - \frac {n (n - 1) N M}{(N + M) ^ {2} (N + M - 1)} \\ = \frac {n N M}{(N + M) ^ {2}} \left(1 - \frac {n - 1}{N + M - 1}\right) \end{array}\tag{5.3.8}
$$

If we let$ p = N / ( N + M )$ denote the proportion of batteries in the bin that are acceptable, we can rewrite Equations 5.3.4 and 5.3.8 as follows. 

$$
\begin{array}{c} {E (X) = n p} \\ {\mathrm{Var} (X) = n p (1 - p) \left[ 1 - \frac {n - 1}{N + M - 1} \right]} \end{array}
$$

It should be noted that, for fixed ${ \boldsymbol { p } } ,$ as $N + M$ increases to ∞,$\mathrm { V a r } ( X )$ converges to $n p ( 1 - p )$ , which is the variance of a binomial random variable with parameters $( n , p )$ (Why was this to be expected?) 

EXAMPLE 5.3b An unknown number, say $N ,$ of animals inhabit a certain region. To obtain some information about the population size, ecologists often perform the following experiment: They first catch a number, say $r ,$ of these animals, mark them in some manner, and release them. After allowing the marked animals time to disperse throughout the region, a new catch of size, say, n is made. Let X denote the number of marked animals in this second capture. If we assume that the population of animals in the region remained fixed between the time of the two catches and that each time an animal was caught it was equally likely to be any of the remaining uncaught animals, it follows that X is a hypergeometric random variable such that 

$$
P \{X = i \} = \frac {\binom {r} {i} \binom {N - r} {n - i}}{\binom {N} {n}} \equiv P _ {i} (N)
$$

Suppose now that X is observed to equal i. That is, the fraction i/n of the animals in the second catch were marked. By taking this as an approximation of r/N , the proportion of animals in the region that are marked, we obtain the estimate rn/i of the number of animals in the region. For instance, if $r = 5 0$ animals are initially caught, marked, and then released, and a subsequent catch of $n = 1 0 0$ animals revealed $X = 2 5$ of them that were marked, then we would estimate the number of animals in the region to be about 200. ■ 

There is a relationship between binomial random variables and the hypergeometric distribution that will be useful to us in developing a statistical test concerning two binomial populations. 

EXAMPLE 5.3c Let X and Y be independent binomial random variables having respective parameters $( n , p )$ and $( m , p )$ . The conditional probability mass function of X given that $X + Y = k$ is as follows. 

$$
\begin{array}{l} P \{X = i | X + Y = k \} = \frac {P \{X = i , X + Y = k \}}{P \{X + Y = k \}} \\ \qquad = \frac {P \{X = i , Y = k - i \}}{P \{X + Y = k \}} \\ \qquad = \frac {P \{X = i \} P \{Y = k - i \}}{P \{X + Y = k \}} \\ \qquad = \frac {\binom {n} {i} p ^ {i} (1 - p) ^ {n - i} \binom {m} {k - i} p ^ {k - i} (1 - p) ^ {m - (k - i)}}{\binom {n + m} {k} p ^ {k} (1 - p) ^ {n + m - k}} \\ \qquad = \frac {\binom {n} {i} \binom {m} {k - i}}{\binom {n + m} {k}} \end{array}
$$

where the next-to-last equality used the fact that $X + Y$ is binomial with parameters $( n + m , p )$ . Hence, we see that the conditional distribution of X given the value of $X + Y$ is hypergeometric. 

It is worth noting that the preceding is quite intuitive. For suppose that $n + m$ independent trials, each of which has the same probability of being a success, are performed; let X be the number of successes in the first n trials, and let Y be the number of successes in the final m trials. Given a total of k successes in the $n + m$ trials, it is quite intuitive that each subgroup of $k$ trials is equally likely to consist of those trials that resulted in successes. That is, the k success trials are distributed as a random selection of k of the $n + m$ trials, and so the number that are from the first n trials is hypergeometric. ■ 

## 5.4 THE UNIFORM RANDOM VARIABLE

A random variable X is said to be uniformly distributed over the interval $[ \alpha , \beta ]$ if its probability density function is given by 

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{\beta - \alpha} & \text { if } \alpha \leq x \leq \beta \\ 0 & \text { otherwise } \end{array} \right.
$$

A graph of this function is given in Figure 5.4. Note that the foregoing meets the requirements of being a probability density function since 

$$
\frac {1}{\beta - \alpha} \int_ {\alpha} ^ {\beta} d x = 1
$$

The uniform distribution arises in practice when we suppose a certain random variable is equally likely to be near any value in the interval $[ \alpha , \beta ]$ 

The probability that X lies in any subinterval of $[ \alpha , \beta ]$ is equal to the length of that subinterval divided by the length of the interval $[ \alpha , \beta ]$ . This follows since when $[ a , \ b ]$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/4d1e9a34841b6c1eede31a835566690337c565714db16fa79a6523d582139589.jpg)



FIGURE 5.4 Graph of f (x) for a uniform [α, β].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/97a977f1d044c78b50fbc6f89bd2e5eed1929b318da0217ce9c2be8079784cf6.jpg)



FIGURE 5.5 Probabilities of a uniform random variable.


is a subinterval of $[ \alpha , \beta ]$ (see Figure 5.5), 

$$
\begin{array}{c} {P \{a <   X <   b \} = \frac {1}{\beta - \alpha} \int_ {a} ^ {b} d x} \\ {= \frac {b - a}{\beta - \alpha}} \end{array}
$$

EXAMPLE 5.4a If X is uniformly distributed over the interval [0, 10], compute the probability that (a)$2 < X < 9 .$ , (b) 1 < X < 4, (c) X < 5, (d) X > 6. 

SOLUTION The respective answers are (a) 7/10, (b) 3/10, (c) 5/10, (d) 4/10. ■ 

EXAMPLE 5.4b Buses arrive at a specified stop at 15-minute intervals starting at 7 A.M. That is, they arrive at 7, 7:15, 7:30, 7:45, and so on. If a passenger arrives at the stop at a time that is uniformly distributed between 7 and 7:30, find the probability that he waits 

(a) less than 5 minutes for a bus; 

(b) at least 12 minutes for a bus. 

SOLUTION Let X denote the time in minutes past 7 A.M. that the passenger arrives at the stop. Since X is a uniform random variable over the interval (0, 30), it follows that the passenger will have to wait less than 5 minutes if he arrives between 7:10 and 7:15 or between 7:25 and 7:30. Hence, the desired probability for (a) is 

$$
P \{1 0 <   X <   1 5 \} + P \{2 5 <   X <   3 0 \} = \frac {5}{3 0} + \frac {5}{3 0} = \frac {1}{3}
$$

Similarly, he would have to wait at least 12 minutes if he arrives between 7 and 7:03 or between 7:15 and 7:18, and so the probability for (b) is 

$$
P \{0 <   X <   3 \} + P \{1 5 <   X <   1 8 \} = \frac {3}{3 0} + \frac {3}{3 0} = \frac {1}{5}
$$

The mean of a uniform $[ \alpha , \beta ]$ random variable is 

$$
\begin{array}{r l} E [ X ] & = \int_ {\alpha} ^ {\beta} \frac {x}{\beta - \alpha} d x \\ & = \frac {\beta^ {2} - \alpha^ {2}}{2 (\beta - \alpha)} \\ & = \frac {(\beta - \alpha) (\beta + \alpha)}{2 (\beta - \alpha)} \end{array}
$$

or 

$$
E [ X ] = \frac {\alpha + \beta}{2}
$$

$\mathrm { O r } ,$ in other words, the expected value of a uniform $[ \alpha , \beta ]$ random variable is equal to the midpoint of the interval $[ \alpha , \beta ]$ , which is clearly what one would expect. (Why?) 

The variance is computed as follows. 

$$
\begin{array}{r l} E [ X ^ {2} ] & = \frac {1}{\beta - \alpha} \int_ {\alpha} ^ {\beta} x ^ {2} d x \\ & = \frac {\beta^ {3} - \alpha^ {3}}{3 (\beta - \alpha)} \\ & = \frac {\beta^ {2} + \alpha \beta + \alpha^ {2}}{3} \end{array}
$$

and so 

$$
\begin{array}{r l} \operatorname{Var} (X) & = \frac {\beta^ {2} + \alpha \beta + \alpha^ {2}}{3} - \left(\frac {\alpha + \beta}{2}\right) ^ {2} \\ & = \frac {\alpha^ {2} + \beta^ {2} - 2 \alpha \beta}{1 2} \\ & = \frac {(\beta - \alpha) ^ {2}}{1 2} \end{array}
$$

EXAMPLE 5.4c The current in a semiconductor diode is often measured by the Shockley equation 

$$
I = I _ {0} (e ^ {a V} - 1)
$$

where V is the voltage across the diode;$I _ { 0 }$ is the reverse current;$^ { a }$ is a constant; and I is the resulting diode current. Find $E [ I ]$ if $a = 5 , I _ { 0 } = 1 0 ^ { - 6 }$ , and V is uniformly distributed over (1, 3). 

SOLUTION 

$$
\begin{array}{r l} & E [ I ] = E [ I _ {0} (e ^ {a V} - 1) ] \\ & \quad = I _ {0} E [ e ^ {a V} - 1 ] \\ & \quad = I _ {0} (E [ e ^ {a V} ] - 1) \\ & \quad = 1 0 ^ {- 6} \int_ {1} ^ {3} e ^ {5 x} \frac {1}{2} d x - 1 0 ^ {- 6} \\ & \quad = 1 0 ^ {- 7} (e ^ {1 5} - e ^ {5}) - 1 0 ^ {- 6} \\ & \approx . 3 2 6 9 \quad \blacksquare \end{array}
$$

The value of a uniform (0, 1) random variable is called a random number. Most com puter systems have a built-in subroutine for generating (to a high level of approximation) sequences of independent random numbers — for instance, Table 5.1 presents a set of independent random numbers generated by an IBM personal computer. Random numbers are quite useful in probability and statistics because their use enables one to empirically estimate various probabilities and expectations. 


TABLE 5.1 A Random Number Table


<table><tr><td>.68587</td><td>.25848</td><td>.85227</td><td>.78724</td><td>.05302</td><td>.70712</td><td>.76552</td><td>.70326</td><td>.80402</td><td>.49479</td></tr><tr><td>.73253</td><td>.41629</td><td>.37913</td><td>.00236</td><td>.60196</td><td>.59048</td><td>.59946</td><td>.75657</td><td>.61849</td><td>.90181</td></tr><tr><td>.84448</td><td>.42477</td><td>.94829</td><td>.86678</td><td>.14030</td><td>.04072</td><td>.45580</td><td>.36833</td><td>.10783</td><td>.33199</td></tr><tr><td>.49564</td><td>.98590</td><td>.92880</td><td>.69970</td><td>.83898</td><td>.21077</td><td>.71374</td><td>.85967</td><td>.20857</td><td>.51433</td></tr><tr><td>.68304</td><td>.46922</td><td>.14218</td><td>.63014</td><td>.50116</td><td>.33569</td><td>.97793</td><td>.84637</td><td>.27681</td><td>.04354</td></tr><tr><td>.76992</td><td>.70179</td><td>.75568</td><td>.21792</td><td>.50646</td><td>.07744</td><td>.38064</td><td>.06107</td><td>.41481</td><td>.93919</td></tr><tr><td>.37604</td><td>.27772</td><td>.75615</td><td>.51157</td><td>.73821</td><td>.29928</td><td>.62603</td><td>.06259</td><td>.21552</td><td>.72977</td></tr><tr><td>.43898</td><td>.06592</td><td>.44474</td><td>.07517</td><td>.44831</td><td>.01337</td><td>.04538</td><td>.15198</td><td>.50345</td><td>.65288</td></tr><tr><td>.86039</td><td>.28645</td><td>.44931</td><td>.59203</td><td>.98254</td><td>.56697</td><td>.55897</td><td>.25109</td><td>.47585</td><td>.59524</td></tr><tr><td>.28877</td><td>.84966</td><td>.97319</td><td>.66633</td><td>.71350</td><td>.28403</td><td>.28265</td><td>.61379</td><td>.13886</td><td>.78325</td></tr><tr><td>.44973</td><td>.12332</td><td>.16649</td><td>.88908</td><td>.31019</td><td>.33358</td><td>.68401</td><td>.10177</td><td>.92873</td><td>.13065</td></tr><tr><td>.42529</td><td>.37593</td><td>.90208</td><td>.50331</td><td>.37531</td><td>.72208</td><td>.42884</td><td>.07435</td><td>.58647</td><td>.84972</td></tr><tr><td>.82004</td><td>.74696</td><td>.10136</td><td>.35971</td><td>.72014</td><td>.08345</td><td>.49366</td><td>.68501</td><td>.14135</td><td>.15718</td></tr><tr><td>.67090</td><td>.08493</td><td>.47151</td><td>.06464</td><td>.14425</td><td>.28381</td><td>.40455</td><td>.87302</td><td>.07135</td><td>.04507</td></tr><tr><td>.62825</td><td>.83809</td><td>.37425</td><td>.17693</td><td>.69327</td><td>.04144</td><td>.00924</td><td>.68246</td><td>.48573</td><td>.24647</td></tr><tr><td>.10720</td><td>.89919</td><td>.90448</td><td>.80838</td><td>.70997</td><td>.98438</td><td>.51651</td><td>.71379</td><td>.10830</td><td>.69984</td></tr><tr><td>.69854</td><td>.89270</td><td>.54348</td><td>.22658</td><td>.94233</td><td>.08889</td><td>.52655</td><td>.83351</td><td>.73627</td><td>.39018</td></tr><tr><td>.71460</td><td>.25022</td><td>.06988</td><td>.64146</td><td>.69407</td><td>.39125</td><td>.10090</td><td>.08415</td><td>.07094</td><td>.14244</td></tr><tr><td>.69040</td><td>.33461</td><td>.79399</td><td>.22664</td><td>.68810</td><td>.56303</td><td>.65947</td><td>.88951</td><td>.40180</td><td>.87943</td></tr><tr><td>.13452</td><td>.36642</td><td>.98785</td><td>.62929</td><td>.88509</td><td>.64690</td><td>.38981</td><td>.99092</td><td>.91137</td><td>.02411</td></tr><tr><td>.94232</td><td>.91117</td><td>.98610</td><td>.71605</td><td>.89560</td><td>.92921</td><td>.51481</td><td>.20016</td><td>.56769</td><td>.60462</td></tr><tr><td>.99269</td><td>.98876</td><td>.47254</td><td>.93637</td><td>.83954</td><td>.60990</td><td>.10353</td><td>.13206</td><td>.33480</td><td>.29440</td></tr><tr><td>.75323</td><td>.86974</td><td>.91355</td><td>.12780</td><td>.01906</td><td>.96412</td><td>.61320</td><td>.47629</td><td>.33890</td><td>.22099</td></tr><tr><td>.75003</td><td>.98538</td><td>.63622</td><td>.94890</td><td>.96744</td><td>.73870</td><td>.72527</td><td>.17745</td><td>.01151</td><td>.47200</td></tr></table>

For an illustration of the use of random numbers, suppose that a medical center is planning to test a new drug designed to reduce its users’ blood cholesterol levels. To test its effectiveness, the medical center has recruited 1,000 volunteers to be subjects in the test. To take into account the possibility that the subjects’ blood cholesterol levels may be affected by factors external to the test (such as changing weather conditions), it has been decided to split the volunteers into 2 groups of size 500 — a treatment group that will be given the drug and a control group that will be given a placebo. Both the volunteers and the administrators of the drug will not be told who is in each group (such a test is called a double-blind test). It remains to determine which of the volunteers should be chosen to constitute the treatment group. Clearly, one would want the treatment group and the control group to be as similar as possible in all respects with the exception that members in the first group are to receive the drug while those in the other group receive a placebo; then it will be possible to conclude that any difference in response between the groups is indeed due to the drug. There is general agreement that the best way to accomplish this is to choose the 500 volunteers to be in the treatment group in a completely random fashion. That is, the choice should be made so that each of the$\dot { ( } _ { 5 0 0 } ^ { 1 0 0 0 } )$ subsets of 500 volunteers is equally likely to constitute the control group. How can this be accomplished? 

*EXAMPLE 5.4d Choosing a Random Subset From a set of n elements — numbered $1 , 2 , \ldots , n -$ suppose we want to generate a random subset of size k that is to be chosen in such a manner that each of the <sup>n</sup> subsets is equally likely to be the subset chosen. How can we do this? 

To answer this question, let us work backwards and suppose that we have indeed randomly generated such a subset of size k. Now for each $j = 1 , \dotsc , n ;$ , we set 

$$
I _ {j} = \left\{ \begin{array}{l l} 1 & \text { if   element   } j \text {   is   in   the   subset } \\ 0 & \text { otherwise } \end{array} \right.
$$

and compute the conditional distribution of $I _ { j }$ given $I _ { 1 } , \ldots , I _ { j - 1 }$ . To start, note that the probability that element 1 is in the subset of size k is clearly k/n (which can be seen either by noting that there is probability 1/n that element 1 would have been the jth element chosen,$j = 1 , \dotsc , k ;$ or by noting that the proportion of outcomes of the random selection that results in element 1 being chosen is$\begin{array} { r } { \left( \mathbf { \Phi } _ { 1 } ^ { 1 } \right) \left( \mathbf { \Phi } _ { k - 1 } ^ { n - 1 } \right) / \left( \mathbf { \Phi } _ { k } ^ { n } \right) = k / n ) } \end{array}$ . Therefore, we have that 

$$
P \{I _ {1} = 1 \} = k / n\tag{5.4.1}
$$

To compute the conditional probability that element 2 is in the subset given $I _ { 1 }$ , note that if $I _ { 1 } = 1$ , then aside from element 1 the remaining $k - 1$ members of the subse would have been chosen “at random” from the remaining n − 1 elements (in the sense tha each of the subsets of size $k - 1$ of the numbers $2 , \ldots , n$ is equally likely to be the othe elements of the subset). Hence, we have that 

$$
P \{I _ {2} = 1 | I _ {1} = 1 \} = \frac {k - 1}{n - 1}\tag{5.4.2}
$$

Similarly, if element 1 is not in the subgroup, then the k members of the subgroup would have been chosen “at random” from the other $n - 1$ elements, and thus 

$$
P \{I _ {2} = 1 | I _ {1} = 0 \} = \frac {k}{n - 1}\tag{5.4.3}
$$

From Equations 5.4.2 and 5.4.3, we see that 

$$
P \{I _ {2} = 1 | I _ {1} \} = \frac {k - I _ {1}}{n - 1}
$$

In general, we have that 

$$
P \{I _ {j} = 1 | I _ {1}, \ldots , I _ {j - 1} \} = \frac {k - \sum_ {i = 1} ^ {j - 1} I _ {i}}{n - j + 1}, \quad j = 2, \ldots , n\tag{5.4.4}
$$

The preceding formula follows since$\begin{array} { r } { \sum _ { i = 1 } ^ { j - 1 } I _ { i } } \end{array}$ represents the number of the first $j - 1$ elements that are included in the subset, and so given $I _ { 1 } , \ldots , I _ { j - 1 }$ there remain $k - \sum _ { i = 1 } ^ { j - 1 } I _ { i }$ elements to be selected from the remaining $n - ( j - 1 )$ 

Since $P \{ U < a \} = a , 0 \leq a \leq 1$ , when U is a uniform (0, 1) random variable, Equations 5.4.1 and 5.4.4 lead to the following method for generating a random subset of size k from a set of n elements: Namely, generate a sequence of (at most n) random numbers $U _ { 1 } , U _ { 2 } , . . .$ . and set 

$$
I _ {1} = \left\{ \begin{array}{l l} 1 & \text { if } U _ {1} <   \frac {k}{n} \\ 0 & \text { otherwise } \end{array} \right.
$$

$$
I _ {2} = \left\{ \begin{array}{l l} 1 & \text { if } U _ {2} <   \frac {k - I _ {1}}{n - 1} \\ 0 & \text { otherwise } \end{array} \right.
$$

$$
I _ {j} = \left\{ \begin{array}{l l} 1 & \text { if } U _ {j} <   \frac {k - I _ {1} - \cdots - I _ {j - 1}}{n - j + 1} \\ 0 & \text { otherwise } \end{array} \right.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/bd825c6087892ed4277daf3e33f005d20da2a786e9df87d7bce84e907e472e7f.jpg)



FIGURE 5.6 Tree diagram.


This process stops when $I _ { 1 } + \cdot \cdot \cdot + I _ { j } = k$ and the random subset consists of the k elements whose I-value equals 1. That is,${ \cal { S } } \doteq \{ i : I _ { i } = 1 \}$ is the subset. 

For instance, if $k = 2 , n = 5$ , then the tree diagram of Figure 5.6 illustrates the foregoing technique. The random subset S is given by the final position on the tree. Note that the probability of ending up in any given final position is equal to $1 / 1 0$ , which can be seen by multiplying the probabilities of moving through the tree to the desired endpoint. For instance, the probability of ending at the point labeled $S \ = \ \{ 2 , 4 \}$ is $P \{ U _ { 1 } \ >$$. 4 ) P \{ U _ { 2 } < . 5 \} P \{ \hat { U _ { 3 } } > \textstyle { \frac { 1 } { 3 } } \} P \{ U _ { 4 } > \textstyle { \frac { 1 } { 2 } } \} = ( . 6 ) ( . 5 ) \hat { \left( \frac { 2 } { 3 } \right) } \left( \textstyle { \frac { 1 } { 2 } } \right) = . 1$ 

As indicated in the tree diagram (see the rightmost branches that result in $S = \{ 4 , 5 \} )$ we can stop generating random numbers when the number of remaining places in the subset to be chosen is equal to the remaining number of elements. That is, the general procedure would stop whenever either$\begin{array} { r } { \sum _ { i = 1 } ^ { j } I _ { i } = k \mathrm { ~ o r ~ } \sum _ { i = 1 } ^ { j } I _ { i } = k - ( n - j ) } \end{array}$ . In the latter case,$S = \{ i \leq j : I _ { i } = 1 , j + 1 , \ldots , n \}$ ■ 

EXAMPLE 5.4e The random vector X, Y is said to have a uniform distribution over the two-dimensional region R if its joint density function is constant for points in R, and is 0 for points outside of R. That is, if 

$$
f (x, y) = \left\{ \begin{array}{l l} c & \text { if } (x, y) \in R \\ 0 & \text { if   otherwise } \end{array} \right.
$$

Because 

$$
\begin{array}{l} 1 = \int_ {R} f (x, y) d x d y \\ = \int_ {R} c d x d y \\ = c \times \text {Area of} R \end{array}
$$

it follows that 

$$
c = \frac {1}{\mathrm{Areaof} R}
$$

For any region $A \subset R ,$ 

$$
\begin{array}{l} P \{(X, Y) \in A \} = \int \int_ {(x, y) \in A} f (x, y) d x d y \\ = \int \int_ {(x, y) \in A} c d x d y \\ = \frac {\text { Area   of } A}{\text { Area   of } R} \end{array}
$$

Suppose now that X, Y is uniformly distributed over the following rectangular region R: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/4d29ee76ff5246f39ef92efb22b8f828fb9c87b153f280761c7e2a5fffe29dea.jpg)


Its joint density function is 

$$
f (x, y) = \left\{ \begin{array}{l l} c & \text { if } 0 \leq x \leq a,   0 \leq y \leq b \\ 0 & \text { otherwise } \end{array} \right.
$$

where$\begin{array} { r } { c = { \frac { 1 } { \mathrm { A r e a } \ o f \ r e c t a n g l e } } = { \frac { 1 } { a b } } } \end{array}$ . In this case, X and Y are independent uniform random variables. To show this, note that for $0 \leq x \leq a , 0 \leq y \leq b$ 

$$
P \{X \leq x, Y \leq y \} = c \int_ {0} ^ {x} \int_ {0} ^ {y} d y d x = \frac {x y}{a b}\tag{5.4.5}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/e9356d1795e37dc4fd15f1b4082edafc40d814a0e60460b553f4fbbfd569294c.jpg)



FIGURE 5.7 The normal density function $( a )$ with$\mu = 0 , \sigma = 1$ and (b) with arbitrary$\mu$ and$\sigma ^ { 2 }$ .


First letting $y = b ;$ , and then letting $x = a ;$ , in the preceding shows that 

$$
P \{X \leq x \} = \frac {x}{a}, P \{Y \leq y \} = \frac {y}{b}\tag{5.4.6}
$$

Thus, from Equations 5.4.5 and 5.4.6 we can conclude that X and Y are independent, with X being uniform on $( 0 , a )$ and Y being uniform on $( 0 , b )$ ■ 

## 5.5 NORMAL RANDOM VARIABLES

A random variable is said to be normally distributed with parameters$\mu$ and$\sigma ^ { 2 }$ , and we write $X \sim { \mathcal { N } } ( \mu , \sigma ^ { 2 } )$ , if its density is 

$$
f (x) = \frac {1}{\sqrt {2 \pi} \sigma} e ^ {- (x - \mu) ^ {2} / 2 \sigma^ {2}}, \qquad - \infty <   x <   \infty^ {*}
$$

The normal density $f ( x )$ is a bell-shaped curve that is symmetric about$\mu$ and that attains its maximum value of 1/σ$\sqrt { 2 \pi } \approx 0 . 3 9 9 / \sigma$ at $x = \mu$ (see Figure 5.7). 

The normal distribution was introduced by the French mathematician Abraham de Moivre in 1733 and was used by him to approximate probabilities associated with binomial random variables when the binomial parameter n is large. This result was later extended by Laplace and others and is now encompassed in a probability theorem known as the central limit theorem, which gives a theoretical base to the often noted empirical observation that, in practice, many random phenomena obey, at least approximately, a normal probability distribution. Some examples of this behavior are the height of a person, the velocity in any direction of a molecule in gas, and the error made in measuring a physical quantity. 

The moment generating function of a normal random variable with parameters$\mu$ and$\sigma ^ { 2 }$ is derived as follows: 

$$
\begin{array}{l} \phi (t) = E [ e ^ {t X} ] \\ \quad = \frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} e ^ {t x} e ^ {- (x - \mu) ^ {2} / 2 \sigma^ {2}} d x \\ \quad = \frac {1}{\sqrt {2 \pi}} e ^ {\mu t} \int_ {- \infty} ^ {\infty} e ^ {t \sigma y} e ^ {- y ^ {2} / 2} d y \qquad \text { by   letting } y = \frac {x - \mu}{\sigma} \\ \quad = \frac {e ^ {\mu t}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \exp \left\{- \left[ \frac {y ^ {2} - 2 t \sigma y}{2} \right] \right\} d y \\ \quad = \frac {e ^ {\mu t}}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \exp \left\{- \frac {(y - t \sigma) ^ {2}}{2} + \frac {t ^ {2} \sigma^ {2}}{2} \right\} d y \\ \quad = \exp \left\{\mu t + \frac {\sigma^ {2} t ^ {2}}{2} \right\} \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} e ^ {- (y - t \sigma) ^ {2} / 2} d y \\ \quad = \exp \left\{\mu t + \frac {\sigma^ {2} t ^ {2}}{2} \right\} \end{array}\tag{5.5.1}
$$

where the last equality follows since 

$$
\frac {1}{\sqrt {2 \pi}} e ^ {- (y - t \sigma) ^ {2} / 2}
$$

is the density of a normal random variable (having parameters tσ and 1) and its integral must thus equal 1. 

Upon differentiating Equation 5.5.1, we obtain 

$$
\begin{array}{l} \phi^ {\prime} (t) = (\mu + t \sigma^ {2}) \exp \left\{\mu t + \sigma^ {2} \frac {t ^ {2}}{2} \right\} \\ \phi^ {\prime \prime} (t) = \sigma^ {2} \exp \left\{\mu t + \sigma^ {2} \frac {t ^ {2}}{2} \right\} + \exp \left\{\mu t + \sigma^ {2} \frac {t ^ {2}}{2} \right\} (\mu + t \sigma^ {2}) ^ {2} \end{array}
$$

Hence, 

$$
\begin{array}{c} {E [ X ] = \phi^ {\prime} (0) = \mu} \\ {E [ X ^ {2} ] = \phi^ {\prime \prime} (0) = \sigma^ {2} + \mu^ {2}} \end{array}
$$

and so 

$$
\begin{array}{c} {E [ X ] = \mu} \\ {\mathrm{Var} (X) = E [ X ^ {2} ] - (E [ X ]) ^ {2} = \sigma^ {2}} \end{array}
$$

Thus$\mu$ and$\sigma ^ { 2 }$ represent respectively the mean and variance of the distribution. 

An important fact about normal random variables is that if X is normal with mean$\mu$ and variance$\sigma ^ { 2 }$ , then $Y = \alpha X + \beta$ is normal with mean$\alpha \mu + \beta$ and variance$\alpha ^ { 2 } \sigma ^ { 2 }$ That this is so can easily be seen by using moment generating functions as follows. 

$$
\begin{array}{r l} & E [ e ^ {t (\alpha X + \beta)} ] = e ^ {t \beta} E [ e ^ {\alpha t X} ] \\ & \qquad = e ^ {t \beta} \exp \{\mu \alpha t + \sigma^ {2} (\alpha t) ^ {2} / 2 \} \quad \mathrm{fromEquation5.5.1} \\ & \qquad = \exp \{(\beta + \mu \alpha) t + \alpha^ {2} \sigma^ {2} t ^ {2} / 2 \} \end{array}
$$

Because the final equation is the moment generating function of the normal random variable with mean$\beta + \mu \alpha$ and variance$\alpha ^ { 2 } \bar { \sigma } ^ { 2 }$ , the result follows. 

It follows from the foregoing that if $X \sim { \mathcal { N } } ( \mu , \sigma ^ { 2 } )$ , then 

$$
Z = \frac {X - \mu}{\sigma}
$$

is a normal random variable with mean 0 and variance 1. Such a random variable $Z$ is said to have a standard, or unit, normal distribution. Let$\Phi ( \cdot )$ denote its distribution function. That is, 

$$
\Phi (x) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} e ^ {- y ^ {2} / 2} d y, \qquad - \infty <   x <   \infty
$$

This result that $Z = ( X - \mu ) / \sigma$ has a standard normal distribution when X is normal with parameters$\mu$ and$\sigma ^ { 2 }$ is quite important, for it enables us to write all probability statements about X in terms of probabilities for Z. For instance, to obtain $P \{ X < b \}$ , we note that X will be less than b if and only if $( X - \mu ) / \sigma$ is less than $( b - \mu ) / \sigma$ , and so 

$$
\begin{array}{c} P \{X <   b \} = P \left\{\frac {X - \mu}{\sigma} <   \frac {b - \mu}{\sigma} \right\} \\ = \Phi \left(\frac {b - \mu}{\sigma}\right) \end{array}
$$

Similarly, for any $a < b _ { ; }$ 

$$
\begin{array}{r l} P \{a <   X <   b \} & = P \left\{\frac {a - \mu}{\sigma} <   \frac {X - \mu}{\sigma} <   \frac {b - \mu}{\sigma} \right\} \\ & = P \left\{\frac {a - \mu}{\sigma} <   Z <   \frac {b - \mu}{\sigma} \right\} \\ & = P \left\{Z <   \frac {b - \mu}{\sigma} \right\} - P \left\{Z <   \frac {a - \mu}{\sigma} \right\} \\ & = \Phi \left(\frac {b - \mu}{\sigma}\right) - \Phi \left(\frac {a - \mu}{\sigma}\right) \end{array}
$$

## 5.5 Normal Random Variables

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/7e8686cc4d542af30f85ea6d4f7a0fc6d6357167d986706b3a1bd472bd68d0df.jpg)



FIGURE 5.8 Standard normal probabilities.


It remains for us to compute$\Phi ( x )$ . This has been accomplished by an approximation and the results are presented in Table A1 of the Appendix, which tabulates$\Phi ( x )$ (to a 4-digi level of accuracy) for a wide range of nonnegative values of x. In addition, Program 5.5a of the text disk can be used to obtain (x). 

While Table A1 tabulates (x) only for nonnegative values of x, we can also obtain$\Phi ( - x )$ from the table by making use of the symmetry (about 0) of the standard normal probability density function. That is, for $x > 0$ , if Z represents a standard normal random variable, then (see Figure 5.8) 

$$
\begin{array}{r l} \Phi (- x) & = P \{Z <   - x \} \\ & = P \{Z > x \} \quad \text { by   symmetry } \\ & = 1 - \Phi (x) \end{array}
$$

Thus, for instance, 

$$
P \{Z <   - 1 \} = \Phi (- 1) = 1 - \Phi (1) = 1 -. 8 4 1 3 = . 1 5 8 7
$$

EXAMPLE 5.5a If X is a normal random variable with mean$\mu ~ = ~ 3$ and variance$\sigma ^ { 2 } = 1 6 ,$ find 

(a)$P \{ X < 1 1 \}$ ; 

(b)$P \{ X > - 1 \}$ ; 

(c)$P \{ 2 < X < 7 \}$ 

SOLUTION 

(a) 

$$
\begin{array}{c} P \{X <   1 1 \} = P \left\{\frac {X - 3}{4} <   \frac {1 1 - 3}{4} \right\} \\ = \Phi (2) \\ = . 9 7 7 2 \end{array}\tag{b}
$$

$$
\begin{array}{c} P \{X > - 1 \} = P \left\{\frac {X - 3}{4} > \frac {- 1 - 3}{4} \right\} \\ = P \{Z > - 1 \} \end{array}
$$

$$
\begin{array}{l} {= P \{Z <   1 \}} \\ {= . 8 4 1 3} \end{array}\tag{c}
$$

$$
\begin{array}{r l} P \{2 <   X <   7 \} & = P \left\{\frac {2 - 3}{4} <   \frac {X - 3}{4} <   \frac {7 - 3}{4} \right\} \\ & = \Phi (1) - \Phi (- 1 / 4) \\ & = \Phi (1) - (1 - \Phi (1 / 4)) \\ & = . 8 4 1 3 +. 5 9 8 7 - 1 = . 4 4 0 0 \end{array}
$$

EXAMPLE 5.5b Suppose that a binary message — either “0” or “1” — must be transmitted by wire from location A to location B. However, the data sent over the wire are subject to a channel noise disturbance and so to reduce the possibility of error, the value 2 is sent over the wire when the message is “1” and the value −2 is sent when the message is “0.” If $x , x = \pm 2$ , is the value sent at location A then R, the value received at location B, is given by $R = x + N$ , where N is the channel noise disturbance. When the message is received at location B, the receiver decodes it according to the following rule: 

$$
\begin{array}{l} \text { if } R \geq . 5, \text { then   ``1'' is concluded } \\ \text { if } R <  . 5, \text { then   ``0'' is concluded } \end{array}
$$

Because the channel noise is often normally distributed, we will determine the error probabilities when N is a standard normal random variable. 

There are two types of errors that can occur: One is that the message “1” can be incorrectly concluded to be “0” and the other that “0” is incorrectly concluded to be “1.” The first type of error will occur if the message is $^ { \mathfrak { s } } 1 ^ { \mathfrak { p } }$ and $2 + N < . 5$ , whereas the second will occur if the message is $^ { \ast } 0 ^ { \ast }$ and $- 2 + N \ge . 5$ 

Hence, 

$$
\begin{array}{r l} P \{\text {error} | \text {message is "1"} \} & = P \{N <   - 1. 5 \} \\ & = 1 - \Phi (1. 5) = . 0 6 6 8 \end{array}
$$

and 

$$
\begin{array}{r l} P \{\text { error } | \text { message   is   ``0'' } \} & = P \{N > 2. 5 \} \\ & = 1 - \Phi (2. 5) = . 0 0 6 2 \end{array}
$$

EXAMPLE 5.5c The power W dissipated in a resistor is proportional to the square of the voltage V. That is, 

$$
W = r V ^ {2}
$$

where r is a constant.$\operatorname { I f } r = 3$ , and V can be assumed (to a very good approximation) to be a normal random variable with mean 6 and standard deviation 1, find 

(a)$E [ W ]$ 

(b)$P \{ W > 1 2 0 \}$ 

SOLUTION 

(a) 

$$
\begin{array}{r l} & E [ W ] = E [ 3 V ^ {2} ] \\ & \quad = 3 E [ V ^ {2} ] \\ & \quad = 3 (\mathrm{Var} [ V ] + E ^ {2} [ V ]) \\ & \quad = 3 (1 + 3 6) = 1 1 1 \end{array}
$$

(b) 

$$
\begin{array}{r l} P \{W > 1 2 0 \} & = P \{3 V ^ {2} > 1 2 0 \} \\ & = P \{V > \sqrt {4 0} \} \\ & = P \{V - 6 > \sqrt {4 0} - 6 \} \\ & = P \{Z >. 3 2 4 6 \} \\ & = 1 - \Phi (. 3 2 4 6) \\ & = . 3 7 2 7 \quad \blacksquare \end{array}
$$

Another important result is that the sum of independent normal random variables is also a normal random variable. To see this, suppose that $X _ { i } , i = 1 , \dotsc , n ,$ , are independent, with $X _ { i }$ being normal with mean$\mu _ { i }$ and variance$\sigma _ { i } ^ { 2 }$ . The moment generating function of$\sum _ { i = 1 } ^ { n } X _ { i }$ is as follows. 

$$
\begin{array}{l} E \left[ \exp \left\{t \sum_ {i = 1} ^ {n} X _ {i} \right\} \right] = E \big [ e ^ {t X _ {1}} e ^ {t X _ {2}} \dots e ^ {t X _ {n}} \big ] \\ = \prod_ {i = 1} ^ {n} E \big [ e ^ {t X _ {i}} \big ] \quad \text { by   independence } \\ = \prod_ {i = 1} ^ {n} e ^ {\mu_ {i} t + \sigma_ {i} ^ {2} t ^ {2} / 2} \\ = e ^ {\mu t + \sigma^ {2} t ^ {2} / 2} \end{array}
$$

where 

$$
\mu = \sum_ {i = 1} ^ {n} \mu_ {i}, \quad \sigma^ {2} = \sum_ {i = 1} ^ {n} \sigma_ {i} ^ {2}
$$

Therefore,$\sum _ { i = 1 } ^ { n } X _ { i }$ has the same moment generating function as a normal random variable having mean$\mu$ and variance$\sigma ^ { 2 }$ . Hence, from the one-to-one correspondence between moment generating functions and distributions, we can conclude that$\sum _ { i = 1 } ^ { n } X _ { i }$ is normal with mean$\textstyle \sum _ { i = 1 } ^ { n } \mu _ { i }$ and variance$\textstyle \sum _ { i = 1 } ^ { n } \sigma _ { i } ^ { 2 }$ 

EXAMPLE 5.5d Data from the National Oceanic and Atmospheric Administration indicate that the yearly precipitation in Los Angeles is a normal random variable with a mean of 12.08 inches and a standard deviation of 3.1 inches. 

(a) Find the probability that the total precipitation during the next 2 years will exceed 25 inches. 

(b) Find the probability that next year’s precipitation will exceed that of the following year by more than 3 inches. 

Assume that the precipitation totals for the next 2 years are independent. 

SOLUTION Let $X _ { 1 }$ and $X _ { 2 }$ be the precipitation totals for the next 2 years. 

(a) Since $X _ { 1 } + X _ { 2 }$ is normal with mean 24.16 and variance $2 ( 3 . 1 ) ^ { 2 } = 1 9 . 2 2$ , it follows that 

$$
\begin{array}{r l} P \{X _ {1} + X _ {2} > 2 5 \} & = P \left\{\frac {X _ {1} + X _ {2} - 2 4 . 1 6}{\sqrt {1 9 . 2 2}} > \frac {2 5 - 2 4 . 1 6}{\sqrt {1 9 . 2 2}} \right\} \\ & = P \{Z >. 1 9 1 6 \} \\ & \approx . 4 2 4 0 \end{array}
$$

(b) Since $- X _ { 2 }$ is a normal random variable with mean −12.08 and variance $( - 1 ) ^ { 2 } ( 3 . 1 ) ^ { 2 }$ , it follows that $X _ { 1 } - X _ { 2 }$ is normal with mean 0 and variance 19.22. Hence, 

$$
\begin{array}{r l} P \{X _ {1} > X _ {2} + 3 \} & = P \{X _ {1} - X _ {2} > 3 \} \\ & = P \left\{\frac {X _ {1} - X _ {2}}{\sqrt {1 9 . 2 2}} > \frac {3}{\sqrt {1 9 . 2 2}} \right\} \\ & = P \{Z >. 6 8 4 3 \} \\ & \approx . 2 4 6 9 \end{array}
$$

Thus there is a 42.4 percent chance that the total precipitation in Los Angeles during the next 2 years will exceed 25 inches, and there is a 24.69 percent chance that next year’s precipitation will exceed that of the following year by more than 3 inches. ■ 

For$\alpha \in ( 0 , 1 )$ , let ${ z } _ { \alpha }$ be such that 

$$
P \{Z > z _ {\alpha} \} = 1 - \Phi (z _ {\alpha}) = \alpha
$$

That is, the probability that a standard normal random variable is greater than $z _ { \alpha }$ is equal to α (see Figure 5.9.) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/21186f20f3756c61f29db59e0da56e21ae44525ef85bb7e4dd4eb4c31128f67d.jpg)



FIGURE 5.9 $P \{ Z > z _ { \alpha } \} = \alpha .$


The value of $z _ { \alpha }$ can, for any α, be obtained from Table A1. For instance, since 

$$
\begin{array}{r l} & 1 - \Phi (1. 6 4 5) = . 0 5 \\ & 1 - \Phi (1. 9 6) = . 0 2 5 \\ & 1 - \Phi (2. 3 3) = . 0 1 \end{array}
$$

it follows that 

$$
z _ {. 0 5} = 1. 6 4 5, \qquad z _ {. 0 2 5} = 1. 9 6, \qquad z _ {. 0 1} = 2. 3 3
$$

Program 5.5b on the text disk can also be used to obtain the value of $z _ { \alpha }$ . Since 

$$
P \{Z <   z _ {\alpha} \} = 1 - \alpha
$$

it follows that 100(1 − α) percent of the time a standard normal random variable will be less than ${ z } _ { \alpha }$ . As a result, we call ${ z } _ { \alpha }$ the $1 0 0 ( 1 - \alpha )$ percentile of the standard normal distribution. 

## 5.6 EXPONENTIAL RANDOM VARIABLES

A continuous random variable whose probability density function is given, for some$\lambda > 0$ , by 

$$
f (x) = \left\{ \begin{array}{l l} \lambda e ^ {- \lambda x} & \text {if} x \geq 0 \\ 0 & \text {if} x <   0 \end{array} \right.
$$

is said to be an exponential random variable (or, more simply, is said to be exponentially distributed) with parameter λ. The cumulative distribution function $F ( x )$ of an exponential random variable is given by 

$$
\begin{array}{l} F (x) = P \{X \leq x \} \\ = \int_ {0} ^ {x} \lambda e ^ {- \lambda y} d y \\ = 1 - e ^ {- \lambda x}, \qquad x \geq 0 \end{array}
$$

The exponential distribution often arises, in practice, as being the distribution of the amount of time until some specific event occurs. For instance, the amount of time (starting from now) until an earthquake occurs, or until a new war breaks out, or until a telephone call you receive turns out to be a wrong number are all random variables that tend in practice to have exponential distributions (see Section 5.6.1 for an explanation). 

The moment generating function of the exponential is given by 

$$
\begin{array}{r l} & {\phi (t) = E [ e ^ {t X} ]} \\ & {\qquad = \int_ {0} ^ {\infty} e ^ {t x} \lambda e ^ {- \lambda x} d x} \\ & {\qquad = \lambda \int_ {0} ^ {\infty} e ^ {- (\lambda - t) x} d x} \\ & {\qquad = \frac {\lambda}{\lambda - t}, \qquad t <   \lambda} \end{array}
$$

Differentiation yields 

$$
\begin{array}{r} \phi^ {\prime} (t) = \frac {\lambda}{(\lambda - t) ^ {2}} \\ \phi^ {\prime \prime} (t) = \frac {2 \lambda}{(\lambda - t) ^ {3}} \end{array}
$$

and so 

$$
\begin{array}{c} {E [ X ] = \phi^ {\prime} (0) = 1 / \lambda} \\ {\mathrm{Var} (X) = \phi^ {\prime \prime} (0) - (E [ X ]) ^ {2}} \\ {= 2 / \lambda^ {2} - 1 / \lambda^ {2}} \\ {= 1 / \lambda^ {2}} \end{array}
$$

Thus λ is the reciprocal of the mean, and the variance is equal to the square of the mean. 

The key property of an exponential random variable is that it is memoryless, where we say that a nonnegative random variable X is memoryless if 

$$
P \{X > s + t | X > t \} = P \{X > s \} \quad \text {   for   all   } s, t \geq 0\tag{5.6.1}
$$

To understand why Equation 5.6.1 is called the memoryless property, imagine that X represents the length of time that a certain item functions before failing. Now let us consider the probability that an item that is still functioning at age t will continue to function for at least an additional time s. Since this will be the case if the total functiona lifetime of the item exceeds $t + s$ given that the item is still functioning at t , we see that 

$$
\begin{array}{r l} & P \{\text { additional   functional   life   of } t \text {-unit - old   item   exceeds } s \} \\ & = P \{X > t + s | X > t \} \end{array}
$$

Thus, we see that Equation 5.6.1 states that the distribution of additional functional life of an item of age t is the same as that of a new item — in other words, when Equation 5.6.1 is satisfied, there is no need to remember the age of a functional item since as long as it is still functional it is “as good as new.” 

The condition in Equation 5.6.1 is equivalent to 

$$
\frac {P \{X > s + t , X > t \}}{P \{X > t \}} = P \{X > s \}
$$

or 

$$
P \{X > s + t \} = P \{X > s \} P \{X > t \}\tag{5.6.2}
$$

When X is an exponential random variable, then 

$$
P \{X > x \} = e ^ {- \lambda x}, \qquad x > 0
$$

and so Equation 5.6.2 is satisfied (since $e ^ { - \lambda ( s + t ) } = e ^ { - \lambda s } e ^ { - \lambda t } )$ ). Hence, exponentially distributed random variables are memoryless (and in fact it can be shown that they are the only random variables that are memoryless). 

EXAMPLE 5.6a Suppose that a number of miles that a car can run before its battery wears out is exponentially distributed with an average value of 10,000 miles. If a person desires to take a 5,000-mile trip, what is the probability that she will be able to complete her trip without having to replace her car battery? What can be said when the distribution is not exponential? 

SOLUTION It follows, by the memoryless property of the exponential distribution, that the remaining lifetime (in thousands of miles) of the battery is exponential with parameter$\lambda = 1 / 1 0$ . Hence the desired probability is 

$$
\begin{array}{r l} P \{\text {remaining lifetime} > 5 \} & = 1 - F (5) \\ & = e ^ {- 5 \lambda} \\ & = e ^ {- 1 / 2} \approx . 6 0 4 \end{array}
$$

However, if the lifetime distribution F is not exponential, then the relevant probability is 

$$
P \{\text { lifetime } > t + 5 | \text { lifetime } > t \} = \frac {1 - F (t + 5)}{1 - F (t)}
$$

where t is the number of miles that the battery had been in use prior to the start of the trip. Therefore, if the distribution is not exponential, additional information is needed (namely, t) before the desired probability can be calculated. ■ 

For another illustration of the memoryless property, consider the following example. 

EXAMPLE 5.6b A crew of workers has 3 interchangeable machines, of which 2 must be working for the crew to do its job. When in use, each machine will function for an exponentially distributed time having parameter λ before breaking down. The workers decide to initially use machines A and B and keep machine C in reserve to replace whichever of A or B breaks down first. They will then be able to continue working until one of the remaining machines breaks down. When the crew is forced to stop working because only one of the machines has not yet broken down, what is the probability that the still operable machine is machine C? 

SOLUTION This can be easily answered, without any need for computations, by invoking the memoryless property of the exponential distribution. The argument is as follows: Consider the moment at which machine C is first put in use. At that time either A or B would have just broken down and the other one — call it machine 0 — will still be functioning. Now even though 0 would have already been functioning for some time, by the memoryless property of the exponential distribution, it follows that its remaining lifetime has the same distribution as that of a machine that is just being put into use. Thus, the remaining lifetimes of machine 0 and machine C have the same distribution and so, by symmetry, the probability that 0 will fail before C is$\frac { 1 } { 2 }$ . ■ 

The following proposition presents another property of the exponential distribution. 

PROPOSITION 5.6.1 If $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ are independent exponential random variables having respective parameters$\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ , then min $( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } )$ is exponential with parameter$\sum _ { t = 1 } ^ { n } \lambda _ { i }$ 

## Proof

Since the smallest value of a set of numbers is greater than x if and only if all values are greater than x, we have 

$$
\begin{array}{l} P \{\min (X _ {1}, X _ {2}, \ldots , X _ {n}) > x \} = P \{X _ {1} > x, X _ {2} > x, \ldots , X _ {n} > x \} \\ = \prod_ {i = 1} ^ {n} P \{X _ {i} > x \} \quad \text { by   independence } \end{array}
$$

$$
\begin{array}{l} = \prod_ {i = 1} ^ {n} e ^ {- \lambda_ {i} x} \\ = e ^ {- \sum_ {i = 1} ^ {n} \lambda_ {i} x} \quad \square \end{array}
$$

EXAMPLE 5.6c A series system is one that needs all of its components to function in order for the system itself to be functional. For an n-component series system in which the component lifetimes are independent exponential random variables with respective parameters$\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ , what is the probability that the system survives for a time $t ?$ 

SOLUTION Since the system life is equal to the minimal component life, it follows from Proposition 5.6.1 that 

$$
P \{\text { system   life   exceeds } t \} = e ^ {- \sum_ {i} \lambda_ {i} t}
$$

Another useful property of exponential random variables is that cX is exponential with parameter$\lambda / c$ when X is exponential with parameter$\lambda ,$ , and $c > 0$ . This follows since 

$$
\begin{array}{r} P \{c X \leq x \} = P \{X \leq x / c \} \\ = 1 - e ^ {- \lambda x / c} \end{array}
$$

The parameter λ is called the rate of the exponential distribution. 

## *5.6.1 The Poisson Process

Suppose that “events” are occurring at random time points, and let N (t) denote the number of events that occurs in the time interval [0, t]. These events are said to constitute a Poisson process having rate$\lambda , \lambda > 0$ , if 

(a)$N ( 0 ) = 0$ 

(b) The numbers of events that occur in disjoint time intervals are independent. 

(c) The distribution of the number of events that occur in a given interval depend only on the length of the interval and not on its location. 

$$
\text {(d)} \lim _ {b \to 0} \frac {P \{N (b) = 1 \}}{b} = \lambda
$$

$$
\text {(e)} \lim _ {b \to 0} \frac {P \{N (b) \geq 2 \}}{b} = 0
$$

Thus, Condition (a) states that the process begins at time 0. Condition (b), the independent increment assumption, states for instance that the number of events by time t [that is,$N ( t ) ]$ is independent of the number of events that occurs between t and $t + s$ [that is,$N ( t + s ) - N ( t ) ]$ . Condition (c), the stationary increment assumption, states that probability distribution of $N ( t + s ) - N ( t )$ is the same for all values of t . Conditions (d) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/f544095cf7a49c6dd9a7b2160d65a1ba64441b04ba77dfa4b3487a5a7c9885bc.jpg)



FIGURE 5.10


and (e) state that in a small interval of length h, the probability of one event occurring is approximately λh, whereas the probability of 2 or more is approximately 0. 

We will now show that these assumptions imply that the number of events occurring in any interval of length t is a Poisson random variable with parameter λt. To be precise, let us call the interval [0, t] and denote by $N ( t )$ the number of events occurring in that interval. To obtain an expression for $P \{ N ( t ) = k \}$ , we start by breaking the interval [0, t] into n nonoverlapping subintervals each of length t/n (Figure 5.10). Now there will be k events in [0, t] if either 

(i) N (t ) equals k and there is at most one event in each subinterval; 

(ii) N (t ) equals k and at least one of the subintervals contains 2 or more events. 

Since these two possibilities are clearly mutually exclusive, and since Condition (i) is equivalent to the statement that k of the n subintervals contain exactly 1 event and the other $n - k$ contain 0 events, we have that 

$$
\begin{array}{r l} P \{N (t) = k \} & = P \{k \text {   of   the   } n \text {   subintervals   contain   exactly   1   event } \\ & \quad \text { and   the   other   } n - k \text {   contain   0   events } \} + P \{N (t) = k \\ & \quad \text { and   at   least   1   subinterval   contains   2   or   more   events } \} \end{array}\tag{5.6.3}
$$

Now it can be shown, using Condition (e), that 

$$
\begin{array}{r l} P \{N (t) = k \text {   and   at   least   1   subinterval   contains   2   or   more   events } \} \\ & \longrightarrow 0 \text {   as   } n \to \infty \end{array}\tag{5.6.4}
$$

Also, it follows from Conditions (d) and (e) that 

$$
\begin{array}{c} P \{\text {   exactly   1   event   in   a   subinterval   } \} \approx \frac {\lambda t}{n} \\ P \{0 \text {   events   in   a   subinterval   } \} \approx 1 - \frac {\lambda t}{n} \end{array}
$$

Hence, since the numbers of events that occur in different subintervals are independent [from Condition (b)], it follows that 

P{k of the subintervals contain exactly 1 event and the other $n - k$ contain 0 events} 

$$
\approx \binom {n} {k} \left(\frac {\lambda t}{n}\right) ^ {k} \left(1 - \frac {\lambda t}{n}\right) ^ {n - k}\tag{5.6.5}
$$

with the approximation becoming exact as the number of subintervals, n, goes to ∞. However, the probability in Equation 5.6.5 is just the probability that a binomial random variable with parameters n and $p = \lambda t / n$ equals k. Hence, as n becomes larger and larger, this approaches the probability that a Poisson random variable with mean $n \lambda t / n = \lambda t$ equals k. Hence, from Equations 5.6.3, 5.6.4, and 5.6.5, we see upon letting n approach ∞ that 

$$
P \{N (t) = k \} = e ^ {- \lambda t} \frac {(\lambda t) ^ {k}}{k !}
$$

We have shown: 

PROPOSITION 5.6.2 For a Poisson process having rate$\lambda$ 

$$
P \{N (t) = k \} = e ^ {- \lambda t} \frac {(\lambda t) ^ {k}}{k !}, \quad k = 0, 1, \ldots
$$

That is, the number of events in any interval of length t has a Poisson distribution with mean$\lambda t$ 

For a Poisson process, let $X _ { 1 }$ denote the time of the first event. Further, for $n > 1$ let $X _ { n }$ denote the elapsed time between $( n - 1 ) s \mathrm { t }$ and the nth events. The sequence$\{ X _ { n } , n = 1 , 2 , \ldots \}$ is called the sequence of interarrival times. For instance, if $X _ { 1 } = 5$ and $X _ { 2 } = 1 0$ , then the first event of the Poisson process would have occurred at time 5 and the second at time 15. 

We now determine the distribution of the $X _ { n }$ . To do so, we first note that the event$\{ X _ { 1 } \ > \ t \}$ takes place if and only if no events of the Poisson process occur in the interval [0, t] and thus, 

$$
P \{X _ {1} > t \} = P \{N (t) = 0 \} = e ^ {- \lambda t}
$$

Hence,$X _ { 1 }$ has an exponential distribution with mean $1 / \lambda$ . To obtain the distribution of $X _ { 2 }$ , note that 

$$
\begin{array}{c} P \{X _ {2} > t | X _ {1} = s \} = P \{0 \text {   events   in   } (s, s + t ] | X _ {1} = s \} \\ = P \{0 \text {   events   in   } (s, s + t ] \} \\ = e ^ {- \lambda t} \end{array}
$$

where the last two equations followed from independent and stationary increments. Therefore, from the foregoing we conclude that $X _ { 2 }$ is also an exponential random variable with mean $1 / \lambda$ , and furthermore, that $X _ { 2 }$ is independent of $X _ { 1 }$ . Repeating the same argument yields: 

PROPOSITION 5.6.3 $X _ { 1 } , X _ { 2 } , . . .$ . are independent exponential random variables each with mean $1 / \lambda$ 

## *5.7 THE GAMMA DISTRIBUTION

A random variable is said to have a gamma distribution with parameters $( \alpha , \lambda ) , \lambda > 0$$\alpha > 0$ , if its density function is given by 

$$
f (x) = \left\{ \begin{array}{l l} \frac {\lambda e ^ {- \lambda x} (\lambda x) ^ {\alpha - 1}}{\Gamma (\alpha)} & x \geq 0 \\ 0 & x <   0 \end{array} \right.
$$

where 

$$
\begin{array}{l} \Gamma (\alpha) = \int_ {0} ^ {\infty} \lambda e ^ {- \lambda x} (\lambda x) ^ {\alpha - 1} d x \\ = \int_ {0} ^ {\infty} e ^ {- y} y ^ {\alpha - 1} d y \quad \text {(by letting y = \lambda x)} \end{array}
$$

The integration by parts formula $u d \nu = u \nu - \int$ v du yields, with $u = y ^ { \alpha - 1 } , d \nu = e ^ { - y } d y$$\nu = - e ^ { - y }$ , that for$\alpha > 1$ 

$$
\begin{array}{c} \int_ {0} ^ {\infty} e ^ {- y} y ^ {\alpha - 1} d y = - e ^ {- y} y ^ {\alpha - 1} \Big | _ {y = 0} ^ {y = \infty} + \int_ {0} ^ {\infty} e ^ {- y} (\alpha - 1) y ^ {\alpha - 2} d y \\ = (\alpha - 1) \int_ {0} ^ {\infty} e ^ {- y} y ^ {\alpha - 2} d y \end{array}
$$

or 

$$
\Gamma (\alpha) = (\alpha - 1) \Gamma (\alpha - 1)\tag{5.7.1}
$$

When α is an integer — say, α = n — we can iterate the foregoing to obtain that 

$$
\begin{array}{l l} \Gamma (n) = (n - 1) \Gamma (n - 1) \\ \quad = (n - 1) (n - 2) \Gamma (n - 2) & \text { by   letting } \alpha = n - 1 \text { in   Eq.5.7.1 } \\ \quad = (n - 1) (n - 2) (n - 3) \Gamma (n - 3) & \text { by   letting } \alpha = n - 2 \text { in   Eq.5.7.1 } \\ \vdots \\ \quad = (n - 1)! \Gamma (1) \end{array}
$$

Because 

$$
\Gamma (1) = \int_ {0} ^ {\infty} e ^ {- y} d y = 1
$$

we see that 

$$
\Gamma (n) = (n - 1)!
$$

The function$\Gamma ( \alpha )$ is called the gamma function. 

It should be noted that when$\alpha = 1$ , the gamma distribution reduces to the exponential with mean $1 / \lambda$ 

The moment generating function of a gamma random variable X with parameters $( \alpha , \lambda )$ is obtained as follows: 

$$
\begin{array}{l} \phi (t) = E [ e ^ {t X} ] \\ \quad = \frac {\lambda^ {\alpha}}{\Gamma (\alpha)} \int_ {0} ^ {\infty} e ^ {t x} e ^ {- \lambda x} x ^ {\alpha - 1} d x \\ \quad = \frac {\lambda^ {\alpha}}{\Gamma (\alpha)} \int_ {0} ^ {\infty} e ^ {- (\lambda - t) x} x ^ {\alpha - 1} d x \\ \quad = \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha} \frac {1}{\Gamma (\alpha)} \int_ {0} ^ {\infty} e ^ {- y} y ^ {\alpha - 1} d y \quad [ \text { by } y = (\lambda - t) x ] \\ \quad = \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha} \end{array}\tag{5.7.2}
$$

Differentiation of Equation 5.7.2 yields 

$$
\begin{array}{c} \phi^ {\prime} (t) = \frac {\alpha \lambda^ {\alpha}}{(\lambda - t) ^ {\alpha + 1}} \\ \phi^ {\prime \prime} (t) = \frac {\alpha (\alpha + 1) \lambda^ {\alpha}}{(\lambda - t) ^ {\alpha + 2}} \end{array}
$$

Hence, 

$$
\begin{array}{c} E [ X ] = \phi^ {\prime} (0) = \frac {\alpha}{\lambda} \\ \operatorname{Var} (X) = E [ X ^ {2} ] - (E [ X ]) ^ {2} \\ = \phi^ {\prime \prime} (0) - \left(\frac {\alpha}{\lambda}\right) ^ {2} \\ = \frac {\alpha (\alpha + 1)}{\lambda^ {2}} - \frac {\alpha^ {2}}{\lambda^ {2}} = \frac {\alpha}{\lambda^ {2}} \end{array}\tag{5.7.3}
$$

(5.7.4) 

An important property of the gamma is that if $X _ { 1 }$ and $X _ { 2 }$ are independent gamma random variables having respective parameters $( \alpha _ { 1 } , \lambda )$ and $( \alpha _ { 2 } , \lambda )$ , then $X _ { 1 } + X _ { 2 }$ is a gamma random variable with parameters $( \alpha _ { 1 } + \alpha _ { 2 } , \lambda )$ . This result easily follows since 

$$
\begin{array}{r} \phi_ {X _ {1} + X _ {2}} (t) = E [ e ^ {t (X _ {1} + X _ {2})} ] \\ = \phi_ {X _ {1}} (t) \phi_ {X _ {2}} (t) \end{array}\tag{5.7.5}
$$

$$
\begin{array}{l} = \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha_ {1}} \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha_ {2}} \quad \text { from   Equation   5.7.2 } \\ = \left(\frac {\lambda}{\lambda - t}\right) ^ {\alpha_ {1} + \alpha_ {2}} \end{array}
$$

which is seen to be the moment generating function of a gamma $( \alpha _ { 1 } + \alpha _ { 2 } , \lambda )$ random variable. Since a moment generating function uniquely characterizes a distribution, the result entails. 

The foregoing result easily generalizes to yield the following proposition. 

PROPOSITION 5.7.1 If $X _ { i } , i = 1 , \ldots , n$ are independent gamma random variables with respective parameters $( \alpha _ { i } , \lambda )$ , then$\sum _ { i = 1 } ^ { n } X _ { i }$ is gamma with parameters$\textstyle \sum _ { i = 1 } ^ { n } \alpha _ { i } , \lambda$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/f2d6f093d358647bfea2150453f366649c165decf9f4c2f21581fb72721ac2ce.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/271939ccec2414e7d9810692d667065edfdcb37bfb11b6326f127e6de772d055.jpg)



FIGURE 5.11 Graphs of the gamma (α, 1) density for (a) α = .5, 2, 3, 4, 5 and (b) α = 50.


Since the gamma distribution with parameters (1, λ) reduces to the exponential with the rate λ, we have thus shown the following useful result. 

## Corollary 5.7.2

If $X _ { 1 } , \ldots , X _ { n }$ are independent exponential random variables, each having rate$\lambda ,$ , then$\sum _ { i = 1 } ^ { n } X _ { i }$ is a gamma random variable with parameters $( n , \lambda )$ 

EXAMPLE 5.7a The lifetime of a battery is exponentially distributed with rate λ. If a stereo cassette requires one battery to operate, then the total playing time one can obtain from a total of n batteries is a gamma random variable with parameters $( n , \lambda )$ ■ 

Figure 5.11 presents a graph of the gamma (α, 1) density for a variety of values of α. It should be noted that as α becomes large, the density starts to resemble the normal density. This is theoretically explained by the central limit theorem, which will be presented in the next chapter. 

## 5.8 DISTRIBUTIONS ARISING FROM THE NORMAL

## 5.8.1 The Chi-Square Distribution

## Definition

If $Z _ { 1 } , Z _ { 2 } , \ldots , Z _ { n }$ are independent standard normal random variables, then X , defined by 

$$
X = Z _ {1} ^ {2} + Z _ {2} ^ {2} + \dots + Z _ {n} ^ {2}\tag{5.8.1}
$$

is said to have a chi-square distribution with n degrees of freedom. We will use the notation 

$$
X \sim \chi_ {n} ^ {2}
$$

to signify that X has a chi-square distribution with n degrees of freedom. 

The chi-square distribution has the additive property that if $X _ { 1 }$ and $X _ { 2 }$ are independent chi-square random variables with $n _ { 1 }$ and $n _ { 2 }$ degrees of freedom, respectively, then $X _ { 1 } + X _ { 2 }$ is chi-square with $n _ { 1 } + n _ { 2 }$ degrees of freedom. This can be formally shown either by the use of moment generating functions or, most easily, by noting that $X _ { 1 } + X _ { 2 }$ is the sum of squares of $n _ { 1 } + n _ { 2 }$ independent standard normals and thus has a chi-square distribution with $n _ { 1 } + n _ { 2 }$ degrees of freedom. 

If X is a chi-square random variable with n degrees of freedom, then for any$\alpha \in ( 0 , 1 )$ ), the quantity$\chi _ { \alpha , n } ^ { 2 }$ is defined to be such that 

$$
P \{X \geq \chi_ {\alpha , n} ^ {2} \} = \alpha
$$

This is illustrated in Figure 5.12. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/dbe728258b553b28165702ac84d80f4b59096faaa5ab4a41375a84c7198d0e73.jpg)



FIGURE 5.12 The chi-square density function with 8 degrees of freedom.


In Table A2 of the Appendix, we list$\chi _ { \alpha , n } ^ { 2 }$ for a variety of values of α and n (including all those needed to solve problems and examples in this text). In addition, Programs 5.8.1a and 5.8.1b on the text disk can be used to obtain chi-square probabilities and the values of$\chi _ { \alpha , n } ^ { 2 } .$ 

EXAMPLE 5.8a Determine $P \{ \chi _ { 2 6 } ^ { 2 } \leq 3 0 \}$ when$\chi _ { 2 6 } ^ { 2 }$ is a chi-square random variable with 26 degrees of freedom. 

SOLUTION Using Program 5.8.1a gives the result 

$$
P \{\chi_ {2 6} ^ {2} \leq 3 0 \} = . 7 3 2 5
$$

EXAMPLE 5.8b Find$\chi _ { . 0 5 , 1 5 } ^ { 2 }$ 

SOLUTION Use Program 5.8.1b to obtain: 

$$
\chi_ {. 0 5, 1 5} ^ {2} = 2 4. 9 9 6 \quad \blacksquare
$$

EXAMPLE 5.8c Suppose that we are attempting to locate a target in three-dimensional space, and that the three coordinate errors (in meters) of the point chosen are independent normal random variables with mean 0 and standard deviation 2. Find the probability that the distance between the point chosen and the target exceeds 3 meters. 

SOLUTION If D is the distance, then 

$$
D ^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2} + X _ {3} ^ {2}
$$

where $X _ { i }$ is the error in the ith coordinate. Since $Z _ { i } = X _ { i } / 2 , i = 1 , 2 , 3$ , are all standard normal random variables, it follows that 

$$
\begin{array}{r l} P \{D ^ {2} > 9 \} & = P \{Z _ {1} ^ {2} + Z _ {2} ^ {2} + Z _ {3} ^ {2} > 9 / 4 \} \\ & = P \{\chi_ {3} ^ {2} > 9 / 4 \} \\ & = . 5 2 2 2 \end{array}
$$

where the final equality was obtained from Program 5.8.1a. ■ 

## *5.8.1.1 THE RELATION BETWEEN CHI-SQUARE AND GAMMA RANDOM VARIABLES

Let us compute the moment generating function of a chi-square random variable with n degrees of freedom. To begin, we have, when $n = 1$ , that 

$$
\begin{array}{l} E [ e ^ {t X} ] = E [ e ^ {t Z ^ {2}} ] \text {where} Z \sim \mathcal {N} (0, 1) \\ \qquad = \int_ {- \infty} ^ {\infty} e ^ {t x ^ {2}} f _ {Z} (x) d x \\ \qquad = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} e ^ {t x ^ {2}} e ^ {- x ^ {2} / 2} d x \\ \qquad = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} (1 - 2 t) / 2} d x \\ \qquad = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} / 2 \bar {\sigma} ^ {2}} d x \quad \text {where} \bar {\sigma} ^ {2} = (1 - 2 t) ^ {- 1} \\ \qquad = (1 - 2 t) ^ {- 1 / 2} \frac {1}{\sqrt {2 \pi} \bar {\sigma}} \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} / 2 \bar {\sigma} ^ {2}} d x \\ \qquad = (1 - 2 t) ^ {- 1 / 2} \end{array}\tag{5.8.2}
$$

where the last equality follows since the integral of the normal $( 0 , \bar { \sigma } ^ { 2 } )$ density equals 1. Hence, in the general case of n degrees of freedom 

$$
\begin{array}{l} E [ e ^ {t X} ] = E \left[ e ^ {t \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}} \right] \\ \qquad = E \left[ \prod_ {i = 1} ^ {n} e ^ {t Z _ {i} ^ {2}} \right] \\ \qquad = \prod_ {i = 1} ^ {n} E [ e ^ {t Z _ {i} ^ {2}} ] \quad \text { by   independence   of   the } Z _ {i} \\ \qquad = (1 - 2 t) ^ {- n / 2} \quad \text { from   Equation   5.8.2 } \end{array}
$$

However, we recognize $[ 1 / ( 1 - 2 t ) ] ^ { n / 2 }$ as being the moment generating function of a gamma random variable with parameters (n/2, 1/2). Hence, by the uniqueness of moment generating functions, it follows that these two distributions — chi-square with n degrees of freedom and gamma with parameters $_ { n / 2 }$ and 1/2 — are identical, and thus we can 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/a709b691f0bc6bc90e20882bda502c0eb4ff099e49270c000222d274e914ec31.jpg)



FIGURE 5.13 The chi-square density function with n degrees of freedom


conclude that the density of X is given by 

$$
f (x) = \frac {\frac {1}{2} e ^ {- x / 2} \left(\frac {x}{2}\right) ^ {(n / 2) - 1}}{\Gamma \left(\frac {n}{2}\right)}, \quad x > 0
$$

The chi-square density functions having 1, 3, and 10 degrees of freedom, respectively, are plotted in Figure 5.13. 

Let us reconsider Example 5.8c, this time supposing that the target is located in the two-dimensional plane. 

EXAMPLE 5.8d When we attempt to locate a target in two-dimensional space, suppose that the coordinate errors are independent normal random variables with mean 0 and standard deviation 2. Find the probability that the distance between the point chosen and the target exceeds 3. 

SOLUTION If D is the distance and $X _ { i } , i = 1 , 2$ are the coordinate errors, then 

$$
D ^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2}
$$

Since $Z _ { i } = X _ { i } / 2 , i = 1$ , 2, are standard normal random variables, we obtain 

$$
P \{D ^ {2} > 9 \} = P \{Z _ {1} ^ {2} + Z _ {2} ^ {2} > 9 / 4 \} = P \{\chi_ {2} ^ {2} > 9 / 4 \} = e ^ {- 9 / 8} \approx . 3 2 4 7
$$

where the preceding calculation used the fact that the chi-square distribution with 2 degrees of freedom is the same as the exponential distribution with parameter 1/2. ■ 

Since the chi-square distribution with n degrees of freedom is identical to the gamma distribution with parameters$\alpha = n / 2$ and$\lambda = 1 / 2$ , it follows from Equations 5.7.3 and 5.7.4 that the mean and variance of a random variable X having this distribution i 

$$
E [ X ] = n, \qquad \operatorname{Var} (X) = 2 n
$$

## 5.8.2 The <sub>t</sub>-Distribution

If Z and$\chi _ { n } ^ { 2 }$ are independent random variables, with Z having a standard normal distribution and$\chi _ { n } ^ { 2 }$ having a chi-square distribution with n degrees of freedom, then the random variable $T _ { n }$ defined by 

$$
T _ {n} = \frac {Z}{\sqrt {\chi_ {n} ^ {2} / n}}
$$

is said to have a t-distribution with n degrees of freedom. A graph of the density function of $T _ { n }$ is given in Figure 5.14 for $n = 1 , 5 ,$ , and 10. 

Like the standard normal density, the t-density is symmetric about zero. In addition, as n becomes larger, it becomes more and more like a standard normal density. To understand why, recall that$\chi _ { n } ^ { 2 }$ can be expressed as the sum of the squares of n standard normals, and so 

$$
\frac {\chi_ {n} ^ {2}}{n} = \frac {Z _ {1} ^ {2} + \cdots + Z _ {n} ^ {2}}{n}
$$

where $Z _ { 1 } , \ldots , Z _ { n }$ are independent standard normal random variables. It now follows from the weak law of large numbers that, for large $n , \ \chi _ { n } ^ { 2 } / n$ will, with probability close to 1, be approximately equal to $E [ Z _ { i } ^ { 2 } ] = 1$ . Hence, for n large,$T _ { n } \stackrel { \cdot } { = } Z / \sqrt { \chi _ { n } ^ { 2 } / n }$ will have approximately the same distribution as $Z$ 

Figure 5.15 shows a graph of the t-density function with 5 degrees of freedom compared with the standard normal density. Notice that the t-density has thicker “tails,” indicating greater variability, than does the normal density. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/dcee156f28f299d9f86fefeb4f847d2c23b37b8d55468cbea9af52ba1a99e6b9.jpg)



FIGURE 5.14 Density function of T<sub>n</sub>.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/9ff37b85b1c11232d33116a455497c5a47afa221bfb3e1205607a763c2640612.jpg)



FIGURE 5.15 Comparing standard normal density with the density $o f T _ { 5 }$


The mean and variance of $T _ { n }$ can be shown to equal 

$$
\begin{array}{c} {E [ T _ {n} ] = 0, \qquad n > 1} \\ {\mathrm{Var} (T _ {n}) = \frac {n}{n - 2}, \qquad n > 2} \end{array}
$$

Thus the variance of $T _ { n }$ decreases to 1 — the variance of a standard normal random variable — as n increases to ∞. For$\alpha , 0 < \alpha < 1$ , let $t _ { \alpha , n }$ be such that 

$$
P \{T _ {n} \geq t _ {\alpha , n} \} = \alpha
$$

It follows from the symmetry about zero of the t -density function that $- T _ { n }$ has the same distribution as $T _ { n } ,$ , and so 

$$
\begin{array}{r l} & {\alpha = P \{- T _ {n} \geq t _ {\alpha , n} \}} \\ & {\quad = P \{T _ {n} \leq - t _ {\alpha , n} \}} \\ & {\quad = 1 - P \{T _ {n} > - t _ {\alpha , n} \}} \end{array}
$$

Therefore, 

$$
P \{T _ {n} \geq - t _ {\alpha , n} \} = 1 - \alpha
$$

leading to the conclusion that 

$$
- t _ {\alpha , n} = t _ {1 - \alpha , n}
$$

which is illustrated in Figure 5.16. 

The values of $t _ { \alpha , n }$ for a variety of values of n and α have been tabulated in Table A3 in the Appendix. In addition, Programs 5.8.2a and 5.8.2b on the text disk compute the t-distribution function and the values $t _ { \alpha , n }$ , respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/48052340fb4d4c9da8b3f3dd80b680e4dc01fff68c3b352b03f0b19f7a3e02f9.jpg)


FIGURE 5.16 $t _ { 1 - \alpha , n } = - t _ { \alpha , n } .$ 

EXAMPLE 5.8e Find (a)$P \{ T _ { 1 2 } \leq 1 . 4 \}$ and (b) t<sub>.025,9</sub>. 

SOLUTION Run Programs 5.8.2a and 5.8.2b to obtain the results. 

(a) .9066 (b) 2.2625 ■ 

## 5.8.3 The <sub>F</sub>-Distribution

$\operatorname { I f } \chi _ { n } ^ { 2 }$ and$\chi _ { m } ^ { 2 }$ are independent chi-square random variables with n and m degrees of freedom, respectively, then the random variable $F _ { n , m }$ defined by 

$$
F _ {n, m} = \frac {\chi_ {n} ^ {2} / n}{\chi_ {m} ^ {2} / m}
$$

is said to have an F-distribution with n and m degrees of freedom. 

For any$\alpha \in ( 0 , 1 )$ , let $F _ { \alpha , n , m }$ be such that 

$$
P \{F _ {n, m} > F _ {\alpha , n, m} \} = \alpha
$$

This is illustrated in Figure 5.17. 

The quantities $F _ { \alpha , n , m }$ are tabulated in Table A4 of the Appendix for different values of n, m, and$\alpha \leq \frac { 1 } { 2 }$ . If $F _ { \alpha , n , m }$ is desired when$\alpha > \frac { 1 } { 2 }$ , it can be obtained by using the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/316ba6076bd80bc49a2af871cbc0f6598fd7fb0485652f93b9556cb71f4eb065.jpg)



FIGURE 5.17 Density function of F<sub>n,m</sub>.


following equalities: 

$$
\begin{array}{r l} & {\alpha = P \left\{\frac {\chi_ {n} ^ {2} / n}{\chi_ {m} ^ {2} / m} > F _ {\alpha , n, m} \right\}} \\ & {\qquad = P \left\{\frac {\chi_ {m} ^ {2} / m}{\chi_ {n} ^ {2} / n} <   \frac {1}{F _ {\alpha , n , m}} \right\}} \\ & {\qquad = 1 - P \left\{\frac {\chi_ {m} ^ {2} / m}{\chi_ {n} ^ {2} / n} \geq \frac {1}{F _ {\alpha , n , m}} \right\}} \end{array}
$$

or, equivalently, 

$$
P \left\{\frac {\chi_ {m} ^ {2} / m}{\chi_ {n} ^ {2} / n} \geq \frac {1}{F _ {\alpha , n , m}} \right\} = 1 - \alpha\tag{5.8.3}
$$

But because $( \chi _ { m } ^ { 2 } / m ) / ( \chi _ { n } ^ { 2 } / n )$ has an F -distribution with degrees of freedom m and n, it follows that 

$$
1 - \alpha = P \left\{\frac {\chi_ {m} ^ {2} / m}{\chi_ {n} ^ {2} / n} \geq F _ {1 - \alpha , m, n} \right\}
$$

implying, from Equation 5.8.3, that 

$$
\frac {1}{F _ {\alpha , n , m}} = F _ {1 - \alpha , m, n}
$$

Thus, for instance,$F _ { \cdot 9 , 5 , 7 } = 1 / F _ { \cdot 1 , 7 , 5 } = 1 / 3 . 3 7 = . 2 9 6 7$ where the value of $F _ { . 1 , 7 , 5 }$ was obtained from Table A4 of the Appendix. 

Program 5.8.3 computes the distribution function of $F _ { n , m }$ 

EXAMPLE 5.8f Determine $P \{ F _ { 6 , 1 4 } \leq 1 . 5 \}$ 

SOLUTION Run Program 5.8.3 to obtain the solution .7518. ■ 

## *5.9 THE LOGISTICS DISTRIBUTION

A random variable X is said to have a logistics distribution with parameters$\mu$ and$\nu > 0$ if its distribution function is 

$$
F (x) = \frac {e ^ {(x - \mu) / v}}{1 + e ^ {(x - \mu) / v}}, \qquad - \infty <   x <   \infty
$$

Differentiating $F ( x ) = 1 - 1 / ( 1 + e ^ { ( x - \mu ) / \nu } )$ yields the density function 

$$
f (x) = \frac {e ^ {(x - \mu) / \nu}}{\nu (1 + e ^ {(x - \mu) / \nu}) ^ {2}}, \qquad - \infty <   x <   \infty
$$

To obtain the mean of a logistics random variable, 

$$
E [ X ] = \int_ {- \infty} ^ {\infty} x \frac {e ^ {(x - \mu) / \nu}}{\nu (1 + e ^ {(x - \mu) / \nu}) ^ {2}} d x
$$

make the substitution $y = ( x - \mu ) / \nu$ . This yields 

$$
\begin{array}{c} E [ X ] = \nu \int_ {- \infty} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y + \mu \int_ {- \infty} ^ {\infty} \frac {e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y \\ = \nu \int_ {- \infty} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y + \mu \end{array}\tag{5.9.1}
$$

where the preceding equality used that $e ^ { y } / ( ( 1 + e ^ { y } ) ^ { 2 } )$ is the density function of a logistic random variable with parameters$\mu = 0 , \upsilon = 1$ (such a random variable is called a standard logistic) and thus integrates to 1. Now, 

$$
\begin{array}{r l} & {\int_ {- \infty} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y = \int_ {- \infty} ^ {0} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y + \int_ {0} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y} \\ & {\qquad = - \int_ {0} ^ {\infty} \frac {x e ^ {- x}}{(1 + e ^ {- x}) ^ {2}} d x + \int_ {0} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y} \\ & {\qquad = - \int_ {0} ^ {\infty} \frac {x e ^ {x}}{(e ^ {x} + 1) ^ {2}} d x + \int_ {0} ^ {\infty} \frac {y e ^ {y}}{(1 + e ^ {y}) ^ {2}} d y} \\ & {\qquad = 0} \end{array}\tag{5.9.2}
$$

where the second equality is obtained by making the substitution $x = - y$ , and the third by multiplying the numerator and denominator by $e ^ { 2 x }$ . From Equations 5.9.1 and 5.9.2 we obtain 

$$
E [ X ] = \mu
$$

Thus$\mu$ is the mean of the logistic; v is called the dispersion parameter. 

## Problems

1. A satellite system consists of 4 components and can function adequately if at least 2 of the 4 components are in working condition. If each component is, independently, in working condition with probability .6, what is the probability that the system functions adequately? 

2. A communications channel transmits the digits 0 and 1. However, due to static, the digit transmitted is incorrectly received with probability .2. Suppose that we want to transmit an important message consisting of one binary digit. To reduce the chance of error, we transmit 00000 instead of 0 and 11111 instead of 1. If the receiver of the message uses “majority” decoding, what is the probability that the message will be incorrectly decoded? What independence assumptions are you making? (By majority decoding we mean that the message is decoded as $^ { \mathfrak { e } } 0 ^ { \mathfrak { p } }$ if there are at least three zeros in the message received and as $^ { \mathfrak { s } } 1 ^ { \mathfrak { p } }$ otherwise.) 

3. If each voter is for Proposition A with probability .7, what is the probability that exactly 7 of 10 voters are for this proposition? 

4. Suppose that a particular trait (such as eye color or left-handedness) of a person is classified on the basis of one pair of genes, and suppose that d represents a dominant gene and r a recessive gene. Thus, a person with dd genes is pure dominance, one with rr is pure recessive, and one with rd is hybrid. The pure dominance and the hybrid are alike in appearance. Children receive 1 gene from each parent. If, with respect to a particular trait, 2 hybrid parents have a total of 4 children, what is the probability that 3 of the 4 children have the outward appearance of the dominant gene? 

5. At least one-half of an airplane’s engines are required to function in order for it to operate. If each engine independently functions with probability p, for what values of p is a 4-engine plane more likely to operate than a 2-engine plane? 

6. Let X be a binomial random variable with 

$$
E [ X ] = 7 \quad \mathrm{and} \quad \operatorname{Var} (X) = 2. 1
$$

Find 

(a)$P \{ X = 4 \} ;$ 

(b)$P \{ X > 1 2 \} .$ 

7. If X and Y are binomial random variables with respective parameters $( n , p )$ and $( n , 1 - p )$ , verify and explain the following identities: 

(a)$P \{ X \leq i \} = P \{ Y \geq n - i \}$ ; 

(a)$P \{ X = k \} = P \{ Y = n - k \}$ 

8. If X is a binomial random variable with parameters n and ${ \boldsymbol { p } } ,$ , where $0 < p < 1$ show that 

$$
P \{X = k + 1 \} = \frac {p}{1 - p} \frac {n - k}{k + 1} P \{X = k \}, k = 0, 1, \dots , n - 1.
$$

(b) As k goes from 0 to $n , P \{ X = k \}$ first increases and then decreases, reaching its largest value when k is the largest integer less than or equal to $( n + 1 ) p$ 

9. Derive the moment generating function of a binomial random variable and then use your result to verify the formulas for the mean and variance given in the text. 

10. Compare the Poisson approximation with the correct binomial probability for the following cases: 

(a)$P \{ X = 2 \} { \mathrm { w h e n } } n = 1 0 , p = . 1 ;$ 

(b)$P \{ X = 0 \}$ when n = 10, p = .1; 

(c)$P \{ X = 4 \}$ when $n = 9 , p = . 2 .$ 

11. If you buy a lottery ticket in 50 lotteries, in each of which your chance of winning a prize is$\frac { 1 } { 1 0 0 }$ , what is the (approximate) probability that you will win a prize (a) at least once, (b) exactly once, and (c) at least twice? 

12. The number of times that an individual contracts a cold in a given year is a Poisson random variable with parameter$\lambda = 3$ . Suppose a new wonder drug (based on large quantities of vitamin C) has just been marketed that reduces the Poisson parameter to$\lambda = 2$ for 75 percent of the population. For the other 25 percent of the population, the drug has no appreciable effect on colds. If an individual tries the drug for a year and has 0 colds in that time, how likely is it that the drug is beneficial for him or her? 

13. In the 1980s, an average of 121.95 workers died on the job each week. Give estimates of the following quantities: 

(a) the proportion of weeks having 130 deaths or more; 

(b) the proportion of weeks having 100 deaths or less. 

Explain your reasoning. 

14. Approximately 80,000 marriages took place in the state of New York last year. Estimate the probability that for at least one of these couples 

(a) both partners were born on April 30; 

(b) both partners celebrated their birthday on the same day of the year. 

State your assumptions. 

15. The game of frustration solitaire is played by turning the cards of a randomly shuffled deck of 52 playing cards over one at a time. Before you turn over the first card, say ace; before you turn over the second card, say two, before you turn over the third card, say three. Continue in this manner (saying ace again before turning over the fourteenth card, and so on.) You lose if you ever turn over a card that matches what you have just said. Use the Poisson paradigm to approximate the probability of winning. (The actual probability is .01623.) 

16. The probability of error in the transmission of a binary digit over a communication channel is $1 / 1 0 ^ { 3 }$ . Write an expression for the exact probability of more than 3 errors when transmitting a block of $1 0 ^ { 3 }$ bits. What is its approximate value? Assume independence. 

17. If X is a Poisson random variable with mean λ, show that $P \{ X = i \}$ first increases and then decreases as i increases, reaching its maximum value when i is the largest integer less than or equal to λ. 

18. A contractor purchases a shipment of 100 transistors. It is his policy to test 10 of these transistors and to keep the shipment only if at least 9 of the 10 are in working condition. If the shipment contains 20 defective transistors, what is the probability it will be kept? 

19. Let X denote a hypergeometric random variable with parameters n, m, and k. That is, 

$$
P \{X = i \} = \frac {\binom {n} {i} \binom {m} {k - i}}{\binom {n + m} {k}}, \qquad i = 0, 1, \ldots , \min (k, n)
$$

(a) Derive a formula for $P \{ X = i \}$ in terms of $P \{ X = i - 1 \}$ 

(b) Use part (a) to compute $P \{ X = i \}$ for $i = { 0 , 1 , 2 , 3 , 4 , 5 }$ when $n = m = 1 0$$k = 5$ , by starting with $P \{ X = 0 \}$ 

(c) Based on the recursion in part (a), write a program to compute the hypergeometric distribution function. 

(d) Use your program from part (c) to compute $P \{ X \leq 1 0 \}$ when $n = m = 3 0$$k = 1 5$ 

20. Independent trials, each of which is a success with probability p, are successively performed. Let X denote the first trial resulting in a success. That is, X will equal k if the first $k - 1$ trials are all failures and the kth a success. X is called a geometric random variable. Compute 

(a)$P \{ X = k \} , k = 1 , 2 , . . . ;$ 

(b) E[X]. 

Let Y denote the number of trials needed to obtain r successes. Y is called a negative binomial random variable. Compute 

(c)$P \{ Y = k \} , k = r , r + 1 , \dots .$ 

(Hint: In order for Y to equal k, how many successes must result in the first $k - 1$ trials and what must be the outcome of trial k?) 

(d) Show that 

$$
E [ Y ] = r / p
$$

(Hint: Write $Y = Y _ { 1 } + \dots + Y _ { r }$ where $Y _ { i }$ is the number of trials needed to go from a total of i − 1 to a total of i successes.) 

21. If U is uniformly distributed on (0, 1), show that $a + ( b - a ) U$ is uniform on $( a , b )$ 

22. You arrive at a bus stop at 10 o’clock, knowing that the bus will arrive at some time uniformly distributed between 10 and 10:30. What is the probability that you will have to wait longer than 10 minutes? If at 10:15 the bus has not yet arrived, what is the probability that you will have to wait at least an additional 10 minutes? 

23. If X is a normal random variable with parameters$\mu = 1 0 , \sigma ^ { 2 } = 3 6$ , compute (a)$P \{ X > 5 \}$ ; (b)$P \{ 4 < X < 1 6 \}$ ; (c)$P \{ X < 8 \} ;$ (d)$P \{ X < 2 0 \} ;$ (e)$P \{ X > 1 6 \}$ 

24. The Scholastic Aptitude Test mathematics test scores across the population of high school seniors follow a normal distribution with mean 500 and standard deviation 100. If five seniors are randomly chosen, find the probability that (a) all scored below 600 and (b) exactly three of them scored above 640. 

25. The annual rainfall (in inches) in a certain region is normally distributed with$\mu = 4 0 , \sigma = 4$ . What is the probability that in 2 of the next 4 years the rainfall will exceed 50 inches? Assume that the rainfalls in different years are independent. 

26. The width of a slot of a duralumin forging is (in inches) normally distributed with$\mu = . 9 0 0 0$ and$\sigma = . 0 0 3 0$ . The specification limits were given as $. 9 0 0 0 { \scriptstyle \pm . 0 0 5 0 }$ What percentage of forgings will be defective? What is the maximum allowable value of σ that will permit no more than 1 in 100 defectives when the widths are normally distributed with$\mu = . 9 0 0 0$ and$\sigma = . 0 0 3 0 ?$ 

27. A certain type of lightbulb has an output that is normally distributed with mean 2,000 end foot candles and standard deviation 85 end foot candles. Determine a lower specification limit L so that only 5 percent of the lightbulbs produced will be defective. (That is, determine L so that $P \{ X \ge L \} = . 9 5$ , where X is the output of a bulb.) 

28. A manufacturer produces bolts that are specified to be between 1.19 and 1.21 inches in diameter. If its production process results in a bolt’s diameter being normally distributed with mean 1.20 inches and standard deviation .005, what percentage of bolts will not meet specifications? 

29. Let$\begin{array} { r } { I = \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } / 2 } d x } \end{array}$ 

(a) Show that for any$\mu$ and$\sigma$ 

$$
\frac {1}{\sqrt {2 \pi} \sigma} \int_ {- \infty} ^ {\infty} e ^ {- (x - \mu) ^ {2} / 2 \sigma^ {2}} d x = 1
$$

is equivalent to $I = \sqrt { 2 \pi }$ 

(b) Show that $I = \sqrt { 2 \pi }$ by writing 

$$
I ^ {2} = \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} / 2} d x \int_ {- \infty} ^ {\infty} e ^ {- y ^ {2} / 2} d y = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} e ^ {- (x ^ {2} + y ^ {2}) / 2} d x d y
$$

and then evaluating the double integral by means of a change of variables to polar coordinates. (That is, let $x = r \cos \theta , y = r \sin \theta , d x d y = r d r d \theta . )$ 

30. A random variable X is said to have a lognormal distribution if log X is normally distributed. If X is lognormal with $E [ \log X ] = \mu$ and$\mathrm { V a r } ( \log \bar { X } ) = \sigma ^ { 2 }$ determine the distribution function of X. That is, what is $P \{ X \leq x \} \colon$ 

31. The lifetimes of interactive computer chips produced by a certain semiconductor manufacturer are normally distributed having mean $4 . 4 \times 1 0 ^ { 6 }$ hours with a standard deviation of $3 \times 1 0 ^ { 5 }$ hours. If a mainframe manufacturer requires that at least 90 percent of the chips from a large batch will have lifetimes of at least $4 . 0 \times 1 0 ^ { 6 }$ hours, should he contract with the semiconductor firm? 

32. In Problem 31, what is the probability that a batch of 100 chips will contain at least 4 whose lifetimes are less than $3 . 8 \times 1 0 ^ { 6 }$ hours? 

33. The lifetime of a color television picture tube is a normal random variable with mean 8.2 years and standard deviation 1.4 years. What percentage of such tubes lasts 

(a) more than 10 years; 

(b) less than 5 years; 

(c) between 5 and 10 years? 

34. The annual rainfall in Cincinnati is normally distributed with mean 40.14 inches and standard deviation 8.7 inches. 

(a) What is the probability this year’s rainfall will exceed 42 inches? 

(b) What is the probability that the sum of the next 2 years’ rainfall will exceed 84 inches? 

(c) What is the probability that the sum of the next 3 years’ rainfall will exceed 126 inches? 

(d) For parts (b) and (c), what independence assumptions are you making? 

35. The height of adult women in the United States is normally distributed with mean 64.5 inches and standard deviation 2.4 inches. Find the probability that a randomly chosen woman is 

(a) less than 63 inches tall; 

(b) less than 70 inches tall; 

(c) between 63 and 70 inches tall. 

(d) Alice is 72 inches tall. What percentage of women is shorter than Alice? 

(e) Find the probability that the average of the heights of two randomly chosen women exceeds 66 inches. 

(f ) Repeat part (e) for four randomly chosen women. 

36. An IQ test produces scores that are normally distributed with mean value 100 and standard deviation 14.2. The top 1 percent of all scores are in what range? 

37. The time (in hours) required to repair a machine is an exponentially distributed random variable with parameter$\lambda = 1$ 

(a) What is the probability that a repair time exceeds 2 hours? 

(b) What is the conditional probability that a repair takes at least 3 hours, given that its duration exceeds 2 hours? 

38. The number of years a radio functions is exponentially distributed with parameter$\begin{array} { r } { \lambda = \frac { 1 } { 8 } } \end{array}$ . If Jones buys a used radio, what is the probability that it will be working after an additional 10 years? 

39. Jones figures that the total number of thousands of miles that a used auto can be driven before it would need to be junked is an exponential random variable with parameter$\frac { 1 } { 2 0 }$ . Smith has a used car that he claims has been driven only 10,000 miles. If Jones purchases the car, what is the probability that she would get at least 20,000 additional miles out of it? Repeat under the assumption that the lifetime mileage of the car is not exponentially distributed but rather is (in thousands of miles) uniformly distributed over (0, 40). 

*40. Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ denote the first n interarrival times of a Poisson process and set$\begin{array} { r } { S _ { n } = \sum _ { i = 1 } ^ { n } X _ { i } } \end{array}$ 

(a) What is the interpretation of $S _ { n } ?$ 

(b) Argue that the two events$\{ S _ { n } \leq t \}$ and$\{ N ( t ) \geq n \}$ are identical. 

(c) Use part (b) to show that 

$$
P \{S _ {n} \leq t \} = 1 - \sum_ {j = 0} ^ {n - 1} e ^ {- \lambda t} (\lambda t) ^ {j} / j!
$$

(d) By differentiating the distribution function of $S _ { n }$ given in part (c), conclude that $S _ { n }$ is a gamma random variable with parameters n and λ. (This result also follows from Corollary 5.7.2.) 

*41. Earthquakes occur in a given region in accordance with a Poisson process with rate 5 per year. 

(a) What is the probability there will be at least two earthquakes in the first half of 2010? 

(b) Assuming that the event in part (a) occurs, what is the probability that there will be no earthquakes during the first 9 months of 2011? 

(c) Assuming that the event in part (a) occurs, what is the probability that there will be at least four earthquakes over the first 9 months of the year 2010? 

*42. When shooting at a target in a two-dimensional plane, suppose that the horizontal miss distance is normally distributed with mean 0 and variance 4 and is independent of the vertical miss distance, which is also normally distributed with mean 0 and variance 4. Let D denote the distance between the point at which the shot lands and the target. 

Find $E [ D ]$ 

43. If X is a chi-square random variable with 6 degrees of freedom, find 

(a)$P \{ X \leq 6 \} ;$ 

(b)$P \{ 3 \leq X \leq 9 \}$ 

44. If X and Y are independent chi-square random variables with 3 and 6 degrees of freedom, respectively, determine the probability that $X + Y$ will exceed 10. 

45. Show that$\Gamma ( 1 / 2 ) = { \sqrt { \pi } }$ (Hint: Evaluate$\int _ { 0 } ^ { \infty } e ^ { - x } x ^ { - 1 / 2 }$ dx by letting $x = y ^ { 2 } / 2$$d x = y d y . )$ 

46. If T has a t-distribution with 8 degrees of freedom, find (a)$P \{ T \geq 1 \}$ (b)$P \{ T \leq 2 \}$ , and (c)$P \{ - 1 < T < 1 \}$ 

47. If $T _ { n }$ has a t-distribution with n degrees of freedom, show that $T _ { n } ^ { 2 }$ has an F -distribution with 1 and n degrees of freedom. 

48. Let be the standard normal distribution function. If, for constants a and $b > 0$ 

$$
P \{X \leq x \} = \Phi \left(\frac {x - a}{b}\right)
$$

characterize the distribution of X. 

# DISTRIBUTIONS OF SAMPLING STATISTICS

## 6.1 INTRODUCTION

The science of statistics deals with drawing conclusions from observed data. For instance, a typical situation in a technological study arises when one is confronted with a large collection, or population, of items that have measurable values associated with them. By suitably sampling from this collection, and then analyzing the sampled items, one hopes to be able to draw some conclusions about the collection as a whole. 

To use sample data to make inferences about an entire population, it is necessary to make some assumptions about the relationship between the two. One such assumption, which is often quite reasonable, is that there is an underlying (population) probability distribution such that the measurable values of the items in the population can be thought of as being independent random variables having this distribution. If the sample data are then chosen in a random fashion, then it is reasonable to suppose that they too are independent values from the distribution. 

## Definition

If $X _ { 1 } , \ldots , X _ { n }$ are independent random variables having a common distribution F, then we say that they constitute a sample (sometimes called a random sample) from the distribution F. 

In most applications, the population distribution F will not be completely specified and one will attempt to use the data to make inferences about F. Sometimes it will be supposed that F is specified up to some unknown parameters (for instance, one might suppose that F was a normal distribution function having an unknown mean and variance, or that it is a Poisson distribution function whose mean is not given), and at other times it migh be assumed that almost nothing is known about F (except maybe for assuming that it is a continuous, or a discrete, distribution). Problems in which the form of the underlying distribution is specified up to a set of unknown parameters are called parametric inference problems, whereas those in which nothing is assumed about the form of $F$ are called nonparametric inference problems. 

EXAMPLE 6.1a Suppose that a new process has just been installed to produce computer chips, and suppose that the successive chips produced by this new process will have useful lifetimes that are independent with a common unknown distribution $F .$ Physical reasons sometimes suggest the parametric form of the distribution $F ;$ for instance, it may lead us to believe that $F$ is a normal distribution, or that $F$ is an exponential distribution. In such cases, we are confronted with a parametrical statistical problem in which we would want to use the observed data to estimate the parameters of $F .$ For instance, if $F$ were assumed to be a normal distribution, then we would want to estimate its mean and variance; if $F$ were assumed to be exponential, we would want to estimate its mean. In other situations, there might not be any physical justification for supposing that $F$ has any particular form; in this case the problem of making inferences about F would constitute a nonparametric inference problem. ■ 

In this chapter, we will be concerned with the probability distributions of certain statistics that arise from a sample, where a statistic is a random variable whose value is determined by the sample data. Two important statistics that we will discuss are the sample mean and the sample variance. In Section 6.2, we consider the sample mean and derive its expectation and variance. We note that when the sample size is at least moderately large, the distribution of the sample mean is approximately normal. This follows from the central limit theorem, one of the most important theoretical results in probability, which is discussed in Section 6.3. In Section $6 . 4 ,$ , we introduce the sample variance and determine its expected value. In Section 6.5, we suppose that the population distribution is normal and present the joint distribution of the sample mean and the sample variance. In Section $6 . 6 ,$ we suppose that we are sampling from a finite population of elements and explain what it means for the sample to be a “random sample.” When the population size is large in relation to the sample size, we often treat it as if it were of infinite size; this is illustrated and its consequences are discussed. 

## 6.2 THE SAMPLE MEAN

Consider a population of elements, each of which has a numerical value attached to it. For instance, the population might consist of the adults of a specified community and the value attached to each adult might be his or her annual income, or height, or age, and so on. We often suppose that the value associated with any member of the population can be regarded as being the value of a random variable having expectation$\mu$ and variance$\sigma ^ { 2 }$ . The quantities$\mu$ and$\sigma ^ { 2 }$ are called the population mean and the population variance, respectively. Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ be a sample of values from this population. The sample mean is defined by 

$$
\overline {{X}} = \frac {X _ {1} + \cdots + X _ {n}}{n}
$$

Since the value of the sample mean$\overline { { X } }$ is determined by the values of the random variable in the sample, it follows that$\overline { { X } }$ is also a random variable. Its expected value and variance are obtained as follows: 

$$
\begin{array}{r l} & E [ \overline {{X}} ] = E \left[ \frac {X _ {1} + \cdots + X _ {n}}{n} \right] \\ & \qquad = \frac {1}{n} (E [ X _ {1} ] + \dots + E [ X _ {n} ]) \\ & \qquad = \mu \end{array}
$$

and 

$$
\begin{array}{l} \operatorname{Var} (\overline {{X}}) = \operatorname{Var} \left(\frac {X _ {1} + \cdots + X _ {n}}{n}\right) \\ \qquad = \frac {1}{n ^ {2}} [ \operatorname{Var} (X _ {1}) + \dots + \operatorname{Var} (X _ {n}) ] \quad \text { by   independence } \\ \qquad = \frac {n \sigma^ {2}}{n ^ {2}} \\ \qquad = \frac {\sigma^ {2}}{n} \end{array}
$$

where$\mu$ and$\sigma ^ { 2 }$ are the population mean and variance, respectively. Hence, the expected value of the sample mean is the population mean$\mu$ whereas its variance is $1 / n$ times the population variance. As a result, we can conclude that X is also centered about the population mean$\mu _ { ; }$ , but its spread becomes more and more reduced as the sample size increases. Figure 6.1 plots the probability density function of the sample mean from a standard normal population for a variety of sample sizes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/4914d03d97fcba5f3903a8266833452c61d67fcb38bb2ae3d6ac272f10020e02.jpg)



FIGURE 6.1 Densities of sample means from a standard normal population.


## 6.3 THE CENTRAL LIMIT THEOREM

In this section, we will consider one of the most remarkable results in probability — namely, the central limit theorem. Loosely speaking, this theorem asserts that the sum of a large number of independent random variables has a distribution that is approximately normal. Hence, it not only provides a simple method for computing approximate probabilities for sums of independent random variables, but it also helps explain the remarkable fact that the empirical frequencies of so many natural populations exhibit a bell-shaped (that is, a normal) curve. 

In its simplest form, the central limit theorem is as follows: 

## Theorem 6.3.1 The Central Limit Theorem

Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ be a sequence of independent and identically distributed random variables each having mean µ and variance$\sigma ^ { 2 }$ . Then for n large, the distribution of 

$$
X _ {1} + \dots + X _ {n}
$$

is approximately normal with mean nµ and variance $n \sigma ^ { 2 }$ 

It follows from the central limit theorem that 

$$
\frac {X _ {1} + \cdots + X _ {n} - n \mu}{\sigma \sqrt {n}}
$$

is approximately a standard normal random variable; thus, for n large, 

$$
P \left\{\frac {X _ {1} + \cdots + X _ {n} - n \mu}{\sigma \sqrt {n}} <   x \right\} \approx P \{Z <   x \}
$$

where Z is a standard normal random variable. 

EXAMPLE 6.3a An insurance company has 25,000 automobile policy holders. If the yearly claim of a policy holder is a random variable with mean 320 and standard deviation 540, approximate the probability that the total yearly claim exceeds 8.3 million. 

SOLUTION Let X denote the total yearly claim. Number the policy holders, and let $X _ { i }$ denote the yearly claim of policy holder i. With $n = 2 5 , 0 0 0$ , we have from the central limit theorem that$\begin{array} { r } { X = \sum _ { i = 1 } ^ { n } X _ { i } } \end{array}$ will have approximately a normal distribution with mean $3 2 0 \times 2 5 , 0 0 0 = 8 \times 1 0 ^ { 6 }$ and standard deviation $5 4 0 { \sqrt { 2 5 , 0 0 0 } } = 8 . 5 3 8 1 \times 1 0 ^ { 4 }$ Therefore, 

$$
\begin{array}{c} P \{X > 8. 3 \times 1 0 ^ {6} \} = P \left\{\frac {X - 8 \times 1 0 ^ {6}}{8 . 5 3 8 1 \times 1 0 ^ {4}} > \frac {8 . 3 \times 1 0 ^ {6} - 8 \times 1 0 ^ {6}}{8 . 5 3 8 1 \times 1 0 ^ {4}} \right\} \\ = P \left\{\frac {X - 8 \times 1 0 ^ {6}}{8 . 5 3 8 1 \times 1 0 ^ {4}} > \frac {. 3 \times 1 0 ^ {6}}{8 . 5 3 8 1 \times 1 0 ^ {4}} \right\} \end{array}
$$

$$
\begin{array}{l l} \approx P \{Z > 3. 5 1 \} & \text { where } Z \text { is   a   standard   normal } \\ \approx . 0 0 0 2 3 \end{array}
$$

Thus, there are only 2.3 chances out of 10,000 that the total yearly claim will exceed 8.3 million. ■ 

EXAMPLE 6.3b Civil engineers believe that W, the amount of weight (in units of 1,000 pounds) that a certain span of a bridge can withstand without structural dam age resulting, is normally distributed with mean 400 and standard deviation 40. Suppose that the weight (again, in units of 1,000 pounds) of a car is a random variable with mean 3 and standard deviation .3. How many cars would have to be on the bridge span for the probability of structural damage to exceed .1? 

SOLUTION Let $P _ { n }$ denote the probability of structural damage when there are n cars on the bridge. That is, 

$$
\begin{array}{c} {P _ {n} = P \{X _ {1} + \dots + X _ {n} \geq W \}} \\ {= P \{X _ {1} + \dots + X _ {n} - W \geq 0 \}} \end{array}
$$

where $X _ { i }$ is the weight of the ith car,$i = 1 , \ldots , n .$ . Now it follows from the centra limit theorem that$\textstyle \sum _ { i = 1 } ^ { n } X _ { i }$ is approximately normal with mean $3 n$ and variance .09n. Hence, since W is independent of the $X _ { i } , i = 1 , \dotsc , n ,$ and is also normal, it follows tha$\textstyle \sum _ { i = 1 } ^ { n } X _ { i } - W$ is approximately normal, with mean and variance given by 

$$
\begin{array}{l} E \left[ \sum_ {1} ^ {n} X _ {i} - W \right] = 3 n - 4 0 0 \\ \operatorname{Var} \left(\sum_ {1} ^ {n} X _ {i} - W\right) = \operatorname{Var} \left(\sum_ {1} ^ {n} X _ {i}\right) + \operatorname{Var} (W) = . 0 9 n + 1, 6 0 0 \end{array}
$$

Therefore, if we let 

$$
Z = \frac {\sum_ {i = 1} ^ {n} X _ {i} - W - (3 n - 4 0 0)}{\sqrt {. 0 9 n + 1 , 6 0 0}}
$$

then 

$$
P _ {n} = P \left\{Z \geq \frac {- (3 n - 4 0 0)}{\sqrt {. 0 9 n + 1 , 6 0 0}} \right\}
$$

where $Z$ is approximately a standard normal random variable. Now $P \{ Z \ge 1 . 2 8 \} \approx . 1$ and so if the number of cars n is such that 

$$
\frac {4 0 0 - 3 n}{\sqrt {. 0 9 n + 1 , 6 0 0}} \leq 1. 2 8
$$

or 

$$
n \geq 1 1 7
$$

then there is at least 1 chance in 10 that structural damage will occur. ■ 

The central limit theorem is illustrated by Program 6.1 on the text disk. This program plots the probability mass function of the sum of n independent and identically distributed random variables that each take on one of the values 0, 1, 2, 3, 4. When using it, one enters the probabilities of these five values, and the desired value of n. Figures 6.2(a)–(f ) give the resulting plot for a specified set of probabilities when $n = 1 , 3 , 5 , 1 0 , 2 5 , 1 0 0$ 

One of the most important applications of the central limit theorem is in regard to binomial random variables. Since such a random variable X having parameters $( n , p )$ represents the number of successes in n independent trials when each trial is a success with probability ${ \boldsymbol { p } } ,$ we can express it as 

$$
X = X _ {1} + \dots + X _ {n}
$$

where 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   trial   is   a   success } \\ 0 & \text { otherwise } \end{array} \right.
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/df1add087b00aa8ea4aa2fd6a4af72a577067dedd810bf88dd37ada06147264a.jpg)



(a)



FIGURE 6.2 (a) n = 1, (b) n = 3, (c) n = 5, (d ) n = 10, (e) n = 25, ( f ) n = 100.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/1e62daf8c43226eb6fa46fdf5ea92c68d806cfab1bd97c9c38328c372775341a.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/7ae7a934eb43ec268f761e4ac39b80621b00c91fddad7797273e240598a263e0.jpg)



(c)



FIGURE 6.2 (continued)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/e09a03ab5f2c9165eca3cc63b48cbc182efb0ec0884f58fe944ef2cfdd404c8b.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5ace1d5a76beefcede8a8bb0e2439477fdeb82ab332b7533970e32ffb46f2737.jpg)



(e)



FIGURE 6.2 (continued)


(f) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/b9c56511932d7857d69d3d112714eab8ffd5ebce361a9ae4fb5b0a9a112a2c27.jpg)



FIGURE 6.2 (continued)


Because 

$$
E [ X _ {i} ] = p, \quad \operatorname{Var} (X _ {i}) = p (1 - p)
$$

it follows from the central limit theorem that for n large 

$$
\frac {X - n p}{\sqrt {n p (1 - p)}}
$$

will approximately be a standard normal random variable [see Figure 6.3, which graphically illustrates how the probability mass function of a binomial $( n , p )$ random variable become more and more “normal” as n becomes larger and larger]. 

EXAMPLE 6.3c The ideal size of a first-year class at a particular college is 150 students. The college, knowing from past experience that, on the average, only 30 percent of those accepted for admission will actually attend, uses a policy of approving the applications of 450 students. Compute the probability that more than 150 first-year students attend thi college. 

SOLUTION Let X denote the number of students that attend; then assuming that each accepted applicant will independently attend, it follows that X is a binomial random variable with parameters $n = 4 5 0$ and$ { p } = . 3$ . Since the binomial is a discrete and the normal a continuous distribution, it is best to compute $P \{ X = i \} \arg \{ i - . 5 < X < i + . 5 \}$ when applying the normal approximation (this is called the continuity correction). This yields the approximation 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/9e5920d005804034f91605b7f9bc82c397319e321e85dfa4bb8c5fedefe0235b.jpg)



FIGURE 6.3 Binomial probability mass functions converging to the normal density.


$$
\begin{array}{c} P \{X > 1 5 0. 5 \} = P \left\{\frac {X - (4 5 0) (. 3)}{\sqrt {4 5 0 (. 3) (. 7)}} \geq \frac {1 5 0 . 5 - (4 5 0) (. 3)}{\sqrt {4 5 0 (. 3) (. 7)}} \right\} \\ \approx P \{Z > 1. 5 9 \} = . 0 6 \end{array}
$$

Hence, only $^ 6$ percent of the time do more than 150 of the first 450 accepted actually attend. ■ 

It should be noted that we now have two possible approximations to binomial probabilities: The Poisson approximation, which yields a good approximation when n is large and$\boldsymbol { \mathit { p } }$ small, and the normal approximation, which can be shown to be quite good when $n p ( 1 - p )$ is large. [The normal approximation will, in general, be quite good for values of n satisfying $n p ( 1 - p ) \geq 1 0 . ]$ 

## 6.3.1 Approximate Distribution of the Sample Mean

Let $X _ { 1 } , \ldots , X _ { n }$ be a sample from a population having mean$\mu$ and variance$\sigma ^ { 2 }$ . The central limit theorem can be used to approximate the distribution of the sample mean 

$$
\overline {{X}} = \sum_ {i = 1} ^ {n} X _ {i} / n
$$

Since a constant multiple of a normal random variable is also normal, it follows from the central limit theorem that X will be approximately normal when the sample size n is large. Since the sample mean has expected value$\mu$ and standard deviation$\sigma / { \sqrt { n } }$ , it then follows that 

$$
\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}}
$$

has approximately a standard normal distribution. 

EXAMPLE 6.3d The weights of a population of workers have mean 167 and standard deviation 27. 

(a) If a sample of 36 workers is chosen, approximate the probability that the sample mean of their weights lies between 163 and 170. 

(b) Repeat part (a) when the sample is of size 144. 

SOLUTION Let $Z$ be a standard normal random variable. 

(a) It follows from the central limit theorem that$\overline { { X } }$ is approximately normal with mean 167 and standard deviation $2 7 / \sqrt { 3 6 } = 4 . 5$ . Therefore, 

$$
\begin{array}{l} P \{1 6 3 <   \overline {{X}} <   1 7 0 \} = P \left\{\frac {1 6 3 - 1 6 7}{4 . 5} <   \frac {\overline {{X}} - 1 6 7}{4 . 5} <   \frac {1 7 0 - 1 6 7}{4 . 5} \right\} \\ = P \left\{-. 8 8 8 9 <   \frac {\overline {{X}} - 1 6 7}{4 . 5} <  . 8 8 8 9 \right\} \\ \approx 2 P \{Z <  . 8 8 8 9 \} - 1 \\ \approx . 6 2 5 9 \end{array}
$$

(b) For a sample of size 144, the sample mean will be approximately normal with mean 167 and standard deviation $2 7 / \sqrt { 1 4 4 } = 2 . 2 5$ . Therefore, 

$$
\begin{array}{l} P \{1 6 3 <   \overline {{X}} <   1 7 0 \} = P \left\{\frac {1 6 3 - 1 6 7}{2 . 2 5} <   \frac {\overline {{X}} - 1 6 7}{2 . 2 5} <   \frac {1 7 0 - 1 6 7}{2 . 2 5} \right\} \\ \qquad = P \left\{- 1. 7 7 7 8 <   \frac {\overline {{X}} - 1 6 7}{4 . 5} <   1. 7 7 7 8 \right\} \\ \qquad \approx 2 P \{Z <   1. 7 7 7 8 \} - 1 \\ \qquad \approx . 9 2 4 6 \end{array}
$$

Thus increasing the sample size from 36 to 144 increases the probability from .6259 to .9246. ■ 

EXAMPLE 6.3e An astronomer wants to measure the distance from her observatory to a distant star. However, due to atmospheric disturbances, any measurement will not yield the exact distance d. As a result, the astronomer has decided to make a series of measurements and then use their average value as an estimate of the actual distance. If the astronomer believes that the values of the successive measurements are independent random variables with a mean of d light years and a standard deviation of 2 light years, how many measurements need she make to be at least 95 percent certain that her estimate is accurate to within ± .5 light years? 

SOLUTION If the astronomer makes n measurements, then ${ \overline { { X } } } ,$ , the sample mean of these measurements, will be approximately a normal random variable with mean d and standard deviation $2 / { \sqrt { n } } .$ . Thus, the probability that it will lie between $d \pm . 5$ is obtained as follows: 

$$
\begin{array}{r l r} & & P \{-. 5 <   \overline {{X}} - d <  . 5 \} = P \left\{\frac {- . 5}{2 / \sqrt {n}} <   \frac {\overline {{X}} - d}{2 / \sqrt {n}} <   \frac {. 5}{2 / \sqrt {n}} \right\} \\ & & \approx P \{- \sqrt {n} / 4 <   Z <   \sqrt {n} / 4 \} \\ & & = 2 P \{Z <   \sqrt {n} / 4 \} - 1 \end{array}
$$

where $Z$ is a standard normal random variable. 

Thus, the astronomer should make n measurements, where n is such that 

$$
2 P \{Z <   \sqrt {n} / 4 \} - 1 \geq . 9 5
$$

or, equivalently, 

$$
P \{Z <   \sqrt {n} / 4 \} \geq . 9 7 5
$$

Since $P \{ Z < 1 . 9 6 \} = . 9 7 5$ , it follows that n should be chosen so tha 

$$
\sqrt {n} / 4 \geq 1. 9 6
$$

That is, at least 62 observations are necessary. ■ 

## 6.3.2 How Large a Sample Is Needed?

The central limit theorem leaves open the question of how large the sample size n needs to be for the normal approximation to be valid, and indeed the answer depends on the population distribution of the sample data. For instance, if the underlying population distribution is normal, then the sample mean X will also be normal regardless of the sample size. A general rule of thumb is that one can be confident of the normal approximation whenever the sample size n is at least 30. That is, practically speaking, no matter how nonnormal the underlying population distribution is, the sample mean of a sample of size at least 30 will be approximately normal. In most cases, the normal approximation is valid for much smaller sample sizes. Indeed, a sample of size 5 will often suffice for the approximation to be valid. Figure 6.4 presents the distribution of the sample means from an exponential population distribution for samples of sizes $n = 1 , 5 , 1 0$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/ae7fa3269a062370e8a0296dc26c2da70a35da6c159af771c113a31137267ee7.jpg)



FIGURE 6.4 Densities of the average of n exponential random variables having mean 1.


## 6.4 THE SAMPLE VARIANCE

Let $X _ { 1 } , \ldots , X _ { n }$ be a random sample from a distribution with mean$\mu$ and variance$\sigma ^ { 2 }$ . Let$\overline { { X } }$ be the sample mean, and recall the following definition from Section 2.3.2. 

## Definition

The statistic $S ^ { 2 }$ , defined by 

$$
S ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{n - 1}
$$

is called the sample variance.$S = \sqrt { S ^ { 2 } }$ is called the sample standard deviation. 

To compute $E [ S ^ { 2 } ]$ , we use an identity that was proven in Section 2.3.2: For any numbers $x _ { 1 } , \ldots , x _ { n }$ 

$$
\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \overline {{x}} ^ {2}
$$

where$\textstyle { \overline { { x } } } = \sum _ { i = 1 } ^ { n } x _ { i } / n$ . It follows from this identity that 

$$
(n - 1) S ^ {2} = \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - n \overline {{X}} ^ {2}
$$

Taking expectations of both sides of the preceding yields, upon using the fact that for any random variable $W , E [ W ^ { 2 } ] = \mathrm { V a r } ( W ) \mathbf { \hat { \mu } } + ( E [ W ] ) ^ { 2 }$ 

$$
\begin{array}{r l} (n - 1) E [ S ^ {2} ] & = E \left[ \sum_ {i = 1} ^ {n} X _ {i} ^ {2} \right] - n E [ \overline {{X}} ^ {2} ] \\ & = n E [ X _ {1} ^ {2} ] - n E [ \overline {{X}} ^ {2} ] \\ & = n \mathrm{Var} (X _ {1}) + n (E [ X _ {1} ]) ^ {2} - n \mathrm{Var} (\overline {{X}}) - n (E [ \overline {{X}} ]) ^ {2} \\ & = n \sigma^ {2} + n \mu^ {2} - n (\sigma^ {2} / n) - n \mu^ {2} \\ & = (n - 1) \sigma^ {2} \end{array}
$$

or 

$$
E [ S ^ {2} ] = \sigma^ {2}
$$

That is, the expected value of the sample variance $S ^ { 2 }$ is equal to the population variance$\sigma ^ { 2 }$ . 

## 6.5 SAMPLING DISTRIBUTIONS FROM A NORMAL POPULATION

Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ be a sample from a normal population having mean$\mu$ and variance$\sigma ^ { 2 }$ That is, they are independent and $X _ { i } \sim \mathcal { N } ( \mu , \sigma ^ { 2 } ) , i = 1 , . . . , n .$ . Also let 

$$
\overline {{X}} = \sum_ {i = 1} ^ {n} X _ {i} / n
$$

and 

$$
S ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{n - 1}
$$

denote the sample mean and sample variance, respectively. We would like to compute their distributions. 

## 6.5.1 Distribution of the Sample Mean

Since the sum of independent normal random variables is normally distributed, it follows that$\overline { { X } }$ is normal with mean 

$$
E [ \overline {{X}} ] = \sum_ {i = 1} ^ {n} \frac {E [ X _ {i} ]}{n} = \mu
$$

and variance 

$$
\operatorname{Var} (\overline {{X}}) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \operatorname{Var} (X _ {i}) = \sigma^ {2} / n
$$

That is,${ \overline { { X } } } ,$ , the average of the sample, is normal with a mean equal to the population mean but with a variance reduced by a factor of $1 / n$ . It follows from this that 

$$
\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}}
$$

is a standard normal random variable. 

## 6.5.2 Joint Distribution of$\bar { \pmb { \chi } }$ and$\pmb { S } ^ { 2 }$

In this section, we not only obtain the distribution of the sample variance $S ^ { 2 }$ , but we also discover a fundamental fact about normal samples — namely, that$\overline { { X } }$ and $S ^ { 2 }$ are independent with $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 }$ having a chi-square distribution with $n - 1$ degrees of freedom. 

To start, for numbers $x _ { 1 } , \ldots , x _ { n }$ , let $y _ { i } = x _ { i } - \mu , i = 1 , \ldots , n ,$ . Then as ${ \overline { { y } } } = { \overline { { x } } } - \mu$ it follows from the identity 

$$
\sum_ {i = 1} ^ {n} (y _ {i} - \bar {y}) ^ {2} = \sum_ {i = 1} ^ {n} y _ {i} ^ {2} - n \bar {y} ^ {2}
$$

that 

$$
\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} = \sum_ {i = 1} ^ {n} (x _ {i} - \mu) ^ {2} - n (\overline {{x}} - \mu) ^ {2}
$$

Now, if $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population having mean$\mu$ variance$\sigma ^ { 2 }$ , then we obtain from the preceding identity that 

$$
\frac {\sum_ {i = 1} ^ {n} (X _ {i} - \mu) ^ {2}}{\sigma^ {2}} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{\sigma^ {2}} + \frac {n (\overline {{X}} - \mu) ^ {2}}{\sigma^ {2}}
$$

or, equivalently, 

$$
\sum_ {i = 1} ^ {n} \left(\frac {X _ {i} - \mu}{\sigma}\right) ^ {2} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}{\sigma^ {2}} + \left[ \frac {\sqrt {n} (\overline {{X}} - \mu)}{\sigma} \right] ^ {2}\tag{6.5.1}
$$

Because $( X _ { i } - \mu ) / \sigma , i = 1 , \ldots , n$ are independent standard normals, it follows that the left side of Equation 6.5.1 is a chi-square random variable with n degrees of freedom. Also, as shown in Section 6.5.1,$\bar { \sqrt { n } } ( \overline { { X } } - \mu ) / \sigma$ is a standard normal random vari able and so its square is a chi-square random variable with 1 degree of freedom. Thus Equation 6.5.1 equates a chi-square random variable having n degrees of freedom to the sum of two random variables, one of which is chi-square with 1 degree of freedom. But it has been established that the sum of two independent chi-square random variables is also chi-square with a degree of freedom equal to the sum of the two degrees of freedom. Thus, it would seem that there is a reasonable possibility that the two terms on the right side of Equation 6.5.1 are independent, with$\scriptstyle \sum _ { i = 1 } ^ { n } ( X _ { i } - { \overline { { X } } } ) ^ { 2 } / \sigma ^ { 2 }$ having a chi-square distribution with $n - 1$ degrees of freedom. Since this result can indeed be established, we have the following fundamental result. 

## Theorem 6.5.1

If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population having mean$\mu$ and variance$\sigma ^ { 2 }$ , then$\overline { { X } }$ and $S ^ { 2 }$ are independent random variables, with$\overline { { X } }$ being normal with mean$\mu$ and variance$\sigma ^ { 2 } / n$ and$\ C n - 1 ) S ^ { 2 } / \sigma ^ { 2 }$ being chi-square with $n - 1$ degrees of freedom. 

Theorem 6.5.1 not only provides the distributions of$\overline { { X } }$ and $S ^ { 2 }$ for a normal population but also establishes the important fact that they are independent. In fact, it turns out that this independence of$\hat { \overline { { X } } }$ and $S ^ { 2 }$ is a unique property of the normal distribution. Its importance will become evident in the following chapters. 

EXAMPLE 6.5a The time it takes a central processing unit to process a certain type of job is normally distributed with mean 20 seconds and standard deviation 3 seconds. If a sample of $1 5$ such jobs is observed, what is the probability that the sample variance will exceed 12? 

SOLUTION Since the sample is of size $n = 1 5$ and$\sigma ^ { 2 } = 9$ , write 

$$
\begin{array}{r l} P \{S ^ {2} > 1 2 \} & = P \left\{\frac {1 4 S ^ {2}}{9} > \frac {1 4}{9}. 1 2 \right\} \\ & = P \{\chi_ {1 4} ^ {2} > 1 8. 6 7 \} \\ & = 1 -. 8 2 2 1 \quad \text { from   Program   5.8.1a } \\ & = . 1 7 7 9 \quad \blacksquare \end{array}
$$

The following corollary of Theorem 6.5.1 will be quite useful in the following chapters. 

## Corollary 6.5.2

Let $X _ { i } , \ldots , X _ { n }$ be a sample from a normal population with mean$\mu$ . If$\overline { { X } }$ denotes the sample mean and S the sample standard deviation, then 

$$
\sqrt {n} \frac {(\overline {{X}} - \mu)}{S} \sim t _ {n - 1}
$$

That is,${ \sqrt { n } } ( { \overline { { X } } } - \mu ) / S$ has a t-distribution with $n - 1$ degrees of freedom. 

## Proof

Recall that a t-random variable with n degrees of freedom is defined as the distribution of 

$$
\frac {Z}{\sqrt {\chi_ {n} ^ {2} / n}}
$$

where $Z$ is a standard normal random variable that is independent of$\chi _ { n } ^ { 2 } ,$ , a chi-square random variable with n degrees of freedom. It then follows from Theorem 6.5.1 tha 

$$
\frac {\sqrt {n} (\overline {{X}} - \mu) / \sigma}{\sqrt {S ^ {2} / \sigma^ {2}}} = \sqrt {n} \frac {(\overline {{X}} - \mu)}{S}
$$

is a t-random variable with $n - 1$ degrees of freedom.  

## 6.6 SAMPLING FROM A FINITE POPULATION

Consider a population of N elements, and suppose that$\boldsymbol { \mathit { p } }$ is the proportion of the population that has a certain characteristic of interest; that is,$N p$ elements have this characteristic, and $N ( 1 - p )$ do not. A sample of size n from this population is said to be a random sample if it is chosen in such a manner that each of the$\binom { \bar { N } } { n }$ population subsets of size n is equally likely to be the sample. For instance, if the population consists of the three elements $a , b , c ,$ then a random sample of size 2 is one that is chosen so that each of the subsets$\{ a , b \} , \{ a , c \}$ , and$\{ b , c \}$ is equally likely to be the sample. A random subset can be chosen sequentially by letting its first element be equally likely to be any of the N elements of the population, then letting its second element be equally likely to be any of the remaining $N - 1$ elements of the population, and so on. 

Suppose now that a random sample of size n has been chosen from a population of size N. For $i = 1 , \ldots , n ,$ , let 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   the   } i \text { th   member   of   the   sample   has   the   characteristic } \\ 0 & \text { otherwise } \end{array} \right.
$$

Consider now the sum of the $X _ { i } ;$ that is, consider 

$$
X = X _ {1} + X _ {2} + \dots + X _ {n}
$$

Because the term $X _ { i }$ contributes 1 to the sum if the ith member of the sample has the characteristic and 0 otherwise, it follows that X is equal to the number of members of the sample that possess the characteristic. In addition, the sample mean 

$$
\overline {{X}} = X / n = \sum_ {i = 1} ^ {n} X _ {i} / n
$$

is equal to the proportion of the members of the sample that possess the characteristic. 

Let us now consider the probabilities associated with the statistics X and ${ \overline { { X } } } .$ . To begin, note that since each of the $N$ members of the population is equally likely to be the ith member of the sample, it follows that 

$$
P \{X _ {i} = 1 \} = \frac {N p}{N} = p
$$

Also, 

$$
P \{X _ {i} = 0 \} = 1 - P \{X _ {i} = 1 \} = 1 - p
$$

That is, each $X _ { i }$ is equal to either 1 or 0 with respective probabilities$\boldsymbol { \mathscr { P } }$ and $1 - p .$ 

It should be noted that the random variables $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ are not independent. For instance, since the second selection is equally likely to be any of the N members of the population, of which $N p$ have the characteristic, it follows that the probability that the second selection has the characteristic is $N p / N = p .$ . That is, without any knowledge of the outcome of the first selection, 

$$
P \{X _ {2} = 1 \} = p
$$

However, the conditional probability that $X _ { 2 } = 1$ , given that the first selection has the characteristic, is 

$$
P \{X _ {2} = 1 | X _ {1} = 1 \} = \frac {N p - 1}{N - 1}
$$

which is seen by noting that if the first selection has the characteristic, then the second selection is equally likely to be any of the remaining $N - 1$ elements, of which $N p - 1$ have the characteristic. Similarly, the probability that the second selection has the characteristic given that the first one does not is 

$$
P \{X _ {2} = 1 | X _ {1} = 0 \} = \frac {N p}{N - 1}
$$

Thus, knowing whether or not the first element of the random sample has the character istic changes the probability for the next element. However, when the population size N is large in relation to the sample size n, this change will be very slight. For instance, if $N = 1 , 0 0 0 , { \mathrm { } } p = . 4$ , then 

$$
P \{X _ {2} = 1 | X _ {1} = 1 \} = \frac {3 9 9}{9 9 9} = . 3 9 9 4
$$

which is very close to the unconditional probability that $X _ { 2 } = 1$ ; namely, 

$$
P \{X _ {2} = 1 \} = . 4
$$

Similarly, the probability that the second element of the sample has the characteristic given that the first does not is 

$$
P \{X _ {2} = 1 | X _ {1} = 0 \} = \frac {4 0 0}{9 9 9} = . 4 0 0 4
$$

which is again very close to$\cdot ^ { 4 . }$ 

Indeed, it can be shown that when the population size N is large with respect to the sample size $^ { n , }$ then $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ are approximately independent. Now if we think of each $X _ { i }$ as representing the result of a trial that is a success if $X _ { i }$ equals 1 and a failure otherwise, it follows that$\textstyle X = \sum _ { i = 1 } ^ { n } X _ { i }$ can be thought of as representing the total number of successes in$\mathscr { n }$ trials. Hence, if the $X _ { i }$ were independent, then X would be a binomia random variable with parameters n and$\scriptstyle { \boldsymbol { p } } .$ In other words, when the population size N is large in relation to the sample size $^ { n , }$ then the distribution of the number of members of the sample that possess the characteristic is approximately that of a binomial random variable with parameters n and$\scriptstyle { \boldsymbol { \hat { p } } } .$ . 

## REMARK

Of course, X is a hypergeometric random variable (Section 5.4); and so the preceding shows that a hypergeometric can be approximated by a binomial random variable when the number chosen is small in relation to the total number of elements. 

For the remainder of this text, we will suppose that the underlying population is large in relation to the sample size and we will take the distribution of X to be binomial. 

By using the formulas given in Section 5.1 for the mean and standard deviation of a binomial random variable, we see tha 

$$
E [ X ] = n p \quad \mathrm{and} \quad S D (X) = \sqrt {n p (1 - p)}
$$

Since ${ \overline { { X } } } _ { i }$ , the proportion of the sample that has the characteristic, is equal to $X / n ,$ , we see from the preceding that 

$$
E [ \overline {{X}} ] = E [ X ] / n = p
$$

and 

$$
S D (\overline {{X}}) = S D (X) / n = \sqrt {p (1 - p) / n}
$$

EXAMPLE 6.6a Suppose that 45 percent of the population favors a certain candidate in an upcoming election. If a random sample of size 200 is chosen, find 

(a) the expected value and standard deviation of the number of members of the sample that favor the candidate; 

(b) the probability that more than half the members of the sample favor the candidate. 

SOLUTION 

(a) The expected value and standard deviation of the proportion that favor the candidate are 

$$
E [ X ] = 2 0 0 (. 4 5) = 9 0, \quad S D (X) = \sqrt {2 0 0 (. 4 5) (1 - . 4 5)} = 7. 0 3 5 6
$$

(b) Since X is binomial with parameters 200 and .45, the text disk gives the solution 

$$
P \{X \geq 1 0 1 \} = . 0 6 8 1
$$

If this program were not available, then the normal approximation to the binomial (Section 6.3) could be used: 

$$
\begin{array}{r l} P \{X \geq 1 0 1 \} & = P \{X \geq 1 0 0. 5 \} \quad (\text { the   continuity   correction }) \\ & = P \left\{\frac {X - 9 0}{7 . 0 3 5 6} \geq \frac {1 0 0 . 5 - 9 0}{7 . 0 3 5 6} \right\} \\ & \approx P \{Z \geq 1. 4 9 2 4 \} \\ & \approx . 0 6 7 8 \end{array}
$$

The solution obtained by the normal approximation is correct to 3 decimal places. ■ 

Even when each element of the population has more than two possible values, it still remains true that if the population size is large in relation to the sample size, then the sample data can be regarded as being independent random variables from the population distribution. 

EXAMPLE 6.6b According to the U.S. Department of Agriculture’s World Livestock Situation, the country with the greatest per capita consumption of pork is Denmark. In 1994, the amount of pork consumed by a person residing in Denmark had a mean value of 147 pounds with a standard deviation of 62 pounds. If a random sample of 25 Danes is chosen, approximate the probability that the average amount of pork consumed by the members of this group in 1994 exceeded 150 pounds. 

SOLUTION If we let $X _ { i }$ be the amount consumed by the ith member of the sample,$i = 1 , \ldots , 2 5$ , then the desired probability is 

$$
P \left\{\frac {X _ {1} + \cdots + X _ {2 5}}{2 5} > 1 5 0 \right\} = P \{\overline {{{X}}} > 1 5 0 \}
$$

where$\overline { { X } }$ is the sample mean of the 25 sample values. Since we can regard the $X _ { i }$ as being independent random variables with mean $1 4 7$ and standard deviation $6 2 ,$ , it follows from the central limit theorem that their sample mean will be approximately normal with mean $1 4 7$ and standard deviation 62/5. Thus, with $Z$ being a standard normal random variable, we have 

$$
\begin{array}{c} P \{\overline {{X}} > 1 5 0 \} = P \left\{\frac {\overline {{X}} - 1 4 7}{1 2 . 4} > \frac {1 5 0 - 1 4 7}{1 2 . 4} \right\} \\ \approx P \{Z >. 2 4 2 \} \\ \approx . 4 0 4 \quad \blacksquare \end{array}
$$

## Problems

1. Plot the probability mass function of the sample mean of $X _ { 1 } , \ldots , X _ { n }$ , when 

(a)$n = 2 ;$ 

(a)$n = 3 .$ 

Assume that the probability mass function of the $X _ { i }$ is 

$$
P \{X = 0 \} = . 2, P \{X = 1 \} = . 3, P \{X = 3 \} = . 5
$$

In both cases, determine $E [ { \overline { { X } } } ]$ and$\mathrm { V a r } ( { \overline { { X } } } )$ 

2. If 10 fair dice are rolled, approximate the probability that the sum of the values obtained (which ranges from 20 to 120) is between 30 and 40 inclusive. 

3. Approximate the probability that the sum of 16 independent uniform (0, 1) random variables exceeds 10. 

4. A roulette wheel has 38 slots, numbered 0, 00, and 1 through 36. If you bet 1 on a specified number, you either win 35 if the roulette ball lands on that number or lose 1 if it does not. If you continually make such bets, approximate the 

probability that 

(a) you are winning after 34 bets; 

(b) you are winning after 1,000 bets; 

(c) you are winning after 100,000 bets. 

Assume that each roll of the roulette ball is equally likely to land on any of the 38 numbers. 

5. A highway department has enough salt to handle a total of 80 inches of snowfall. Suppose the daily amount of snow has a mean of 1.5 inches and a standard deviation of .3 inches. 

(a) Approximate the probability that the salt on hand will suffice for the next 50 days. 

(b) What assumption did you make in solving part (a)? 

(c) Do you think this assumption is justified? Explain briefly. 

6. Fifty numbers are rounded off to the nearest integer and then summed. If the individual roundoff errors are uniformly distributed between −.5 and .5, what is the approximate probability that the resultant sum differs from the exact sum by more than 3? 

7. A six-sided die, in which each side is equally likely to appear, is repeatedly rolled until the total of all rolls exceeds 400. Approximate the probability that this will require more than 140 rolls. 

8. The amount of time that a certain type of battery functions is a random variable with mean 5 weeks and standard deviation 1.5 weeks. Upon failure, it is immediately replaced by a new battery. Approximate the probability that 13 or more batteries will be needed in a year. 

9. The lifetime of a certain electrical part is a random variable with mean 100 hours and standard deviation 20 hours. If 16 such parts are tested, find the probability that the sample mean is 

(a) less than 104; 

(b) between 98 and 104 hours. 

10. A tobacco company claims that the amount of nicotine in its cigarettes is a random variable with mean 2.2 mg and standard deviation .3 mg. However, the sample mean nicotine content of 100 randomly chosen cigarettes was 3.1 mg. What is the approximate probability that the sample mean would have been as high or higher than 3.1 if the company’s claims were true? 

11. The lifetime (in hours) of a type of electric bulb has expected value 500 and standard deviation 80. Approximate the probability that the sample mean of n such bulbs is greater than 525 when 

(a)$n = 4 ;$ 

(b)$n = 1 6 ;$ 

(c)$n = 3 6 ;$ 

(d)$n = 6 4 .$ 

12. An instructor knows from past experience that student exam scores have mean 77 and standard deviation 15. At present the instructor is teaching two separate classes — one of size 25 and the other of size 64. 

(a) Approximate the probability that the average test score in the class of size 25 lies between 72 and 82. 

(b) Repeat part (a) for a class of size 64. 

(c) What is the approximate probability that the average test score in the class of size 25 is higher than that of the class of size 64? 

(d) Suppose the average scores in the two classes are 76 and 83. Which class, the one of size 25 or the one of size 64, do you think was more likely to have averaged 83? 

13. If X is binomial with parameters $n = 1 5 0 , \mathrm { { } } p = . 6 ,$ , compute the exact value of $P \{ X \leq 8 0 \}$ and compare with its normal approximation both (a) making use of and (b) not making use of the continuity correction. 

14. Each computer chip made in a certain plant will, independently, be defective with probability .25. If a sample of 1,000 chips is tested, what is the approximate probability that fewer than 200 chips will be defective? 

15. A club basketball team will play a 60-game season. Thirty-two of these game are against class A teams and 28 are against class B teams. The outcomes of all the games are independent. The team will win each game against a class A opponent with probability .5, and it will win each game against a class B opponent with probability .7. Let X denote its total number of victories in the season. 

(a) Is X a binomial random variable? 

(b) Let $X _ { A }$ and $X _ { B }$ denote, respectively, the number of victories against class A and class B teams. What are the distributions of $X _ { A }$ and $X _ { B } ?$ 

(c) What is the relationship between $X _ { A } , X _ { B }$ , and X ? 

(d) Approximate the probability that the team wins 40 or more games. 

16. Argue, based on the central limit theorem, that a Poisson random variable having mean λ will approximately have a normal distribution with mean and variance both equal to λ when λ is large. If X is Poisson with mean 100, compute the exact probability that X is less than or equal to 116 and compare it with its normal approximation both when a continuity correction is utilized and when it is not. The convergence of the Poisson to the normal is indicated in Figure 6.5. 

17. Use the text disk to compute $P \{ X \leq 1 0 \}$ when X is a binomial random variable with parameters $n = 1 0 0 , p = . 1$ . Now compare this with its (a) Poisson and (b) normal approximation. In using the normal approximation, write the desired probability as $P \{ X < 1 0 . 5 \}$ so as to utilize the continuity correction. 


Poisson (10)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/5505e6e79df55a10d19c04620cbe5a93568b584f985db361c371053b4f9b71b5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/ad60f52045dfa08e1b78361134df0ddc9c58eb1a1060a38e29f9501bc8f943da.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/1c09cefaa01eb84b74c74bc73d11388f9af8ed848286867c0cca733aaffb549b.jpg)



FIGURE 6.5 Poisson probability mass functions.


18. The temperature at which a thermostat goes off is normally distributed with variance$\scriptstyle { \hat { \sigma } } ^ { 2 }$ . If the thermostat is to be tested five times, find 

(a)$P \{ S ^ { 2 } / \sigma ^ { 2 } \le 1 . 8 \}$ 

(b)$P \{ . 8 5 \leq S ^ { 2 } / \sigma ^ { 2 } \leq 1 . 1 5 \}$ 

where $S ^ { 2 }$ is the sample variance of the five data values. 

19. In Problem 18, how large a sample would be necessary to ensure that the probability in part (a) is at least .95? 

20. Consider two independent samples — the first of size 10 from a normal population having variance 4 and the second of size 5 from a normal population having variance 2. Compute the probability that the sample variance from the second sample exceeds the one from the first. (Hint: Relate it to the F-distribution.) 

21. Twelve percent of the population is left-handed. Find the probability that there are between 10 and 14 left-handers in a random sample of 100 members of this population. That is, find $P \{ 1 0 \leq X \leq 1 4 \}$ , where X is the number of left-handers in the sample. 

22. Fifty-two percent of the residents of a certain city are in favor of teaching evolution in high school. Find or approximate the probability that at least 50 percent of a random sample of size n is in favor of teaching evolution, when 

(a) n = 10; 

(b)$n = 1 0 0 ;$ 

(c)$n = 1 , 0 0 0 ;$ 

(d)$n = 1 0 , 0 0 0 .$ 

23. The following table gives the percentages of individuals, categorized by gender, that follow certain negative health practices. Suppose a random sample of 300 men is chosen. Approximate the probability that 

(a) at least 150 of them rarely eat breakfast; 

(b) fewer than 100 of them smoke. 

<table><tr><td></td><td>Sleeps 6 Hours or Less per Night</td><td>Smoker</td><td>Rarely Eats Breakfast</td><td>Is 20 Percent or More Overweight</td></tr><tr><td>Men</td><td>22.7</td><td>28.4</td><td>45.4</td><td>29.6</td></tr><tr><td>Women</td><td>21.4</td><td>22.8</td><td>42.0</td><td>25.6</td></tr></table>


Source: US National Center for Health Statistics. Health Promotion and Disease Prevention. 1990 


24. (Use the table from Problem 23.) Suppose a random sample of 300 women is chosen. Approximate the probability that 

(a) at least 60 of them are overweight by 20 percent or more; 

(b) fewer than 50 of them sleep 6 hours or less nightly. 

25. (Use the table from Problem 23.) Suppose random samples of 300 women and of 300 men are chosen. Approximate the probability that more women than men rarely eat breakfast. 

26. The following table uses 1989 data concerning the percentages of male and female full-time workers whose annual salaries fall in different salary groupings. Suppose random samples of 1,000 men and 1,000 women were chosen. Use the table to approximate the probability that 

(a) at least half of the women earned less than $20,000; 

(b) more than half of the men earned $20,000 or more; 

(c) more than half of the women and more than half of the men earned $20,000 or more; 

(d) 250 or fewer of the women earned at least $25,000; 

(e) at least 200 of the men earned $50,000 or more; 

(f) more women than men earned between $20,000 and $24,999 

<table><tr><td>Earnings Range</td><td>Percentage of Women</td><td>Percentage of Men</td></tr><tr><td>$4,999 or less</td><td>2.8</td><td>1.8</td></tr><tr><td>$5,000 to $9,999</td><td>10.4</td><td>4.7</td></tr><tr><td>$10,000 to $19,999</td><td>41.0</td><td>23.1</td></tr><tr><td>$20,000 to $25,000</td><td>16.5</td><td>13.4</td></tr><tr><td>$25,000 to $49,999</td><td>26.3</td><td>42.1</td></tr><tr><td>$50,000 and over</td><td>3.0</td><td>14.9</td></tr></table>


Source: U.S. Department of Commerce, Bureau of the Census.


27. In 1995 the percentage of the labor force that belonged to a union was 14.9. If five workers had been randomly chosen in that year, what is the probability that none of them would have belonged to a union? Compare your answer to what it would be for the year 1945, when an all time high of 35.5 percent of the labor force belonged to a union. 

28. The sample mean and sample standard deviation of all San Francisco student scores on the most recent Scholastic Aptitude Test examination in mathematics were 517 and 120. Approximate the probability that a random sample of 144 students would have an average score exceeding 

(a) 507; 

(b) 517; 

(c) 537; 

(d) 550. 

29. The average salary of newly graduated students with bachelor’s degrees in chemical engineering is $43,600, with a standard deviation of $3,200. Approximate the probability that the average salary of a sample of 12 recently graduated chemical engineers exceeds $45,000. 

30. A certain component is critical to the operation of an electrical system and must be replaced immediately upon failure. If the mean lifetime of this type of component is 100 hours and its standard deviation is 30 hours, how many of the components must be in stock so that the probability that the system is in continual operation for the next 2000 hours is at least .95? 

This Page Intentionally Left Blank 

## PARAMETER ESTIMATION

## 7.1 INTRODUCTION

Let $X _ { 1 } , \ldots , X _ { n }$ be a random sample from a distribution $F _ { \theta }$ that is specified up to a vector of unknown parameters θ . For instance, the sample could be from a Poisson distribution whose mean value is unknown; or it could be from a normal distribution having an unknown mean and variance. Whereas in probability theory it is usual to suppose that all of the parameters of a distribution are known, the opposite is true in statistics, where a central problem is to use the observed data to make inferences about the unknown parameters. 

In Section 7.2, we present the maximum likelihood method for determining estimators of unknown parameters. The estimates so obtained are called point estimates, because they specify a single quantity as an estimate of θ . In Section 7.3, we consider the problem of obtaining interval estimates. In this case, rather than specifying a certain value as our estimate of θ , we specify an interval in which we estimate that θ lies. Additionally, we consider the question of how much confidence we can attach to such an interval estimate. We illustrate by showing how to obtain an interval estimate of the unknown mean of a normal distribution whose variance is specified. We then consider a variety of interval estimation problems. In Section 7.3.1, we present an interval estimate of the mean of a normal distribution whose variance is unknown. In Section 7.3.2, we obtain an interval estimate of the variance of a normal distribution. In Section 7.4, we determine an interval estimate for the difference of two normal means, both when their variances are assumed to be known and when they are assumed to be unknown (although in the latter case we suppose that the unknown variances are equal). In Sections 7.5 and the optional Section 7.6, we present interval estimates of the mean of a Bernoulli random variable and the mean of an exponential random variable. 

In the optional Section 7.7, we return to the general problem of obtaining point esti mates of unknown parameters and show how to evaluate an estimator by considering its mean square error. The bias of an estimator is discussed, and its relationship to the mean square error is explored. 

In the optional Section $7 . 8 ,$ , we consider the problem of determining an estimate of an unknown parameter when there is some prior information available. This is the Bayesian approach, which supposes that prior to observing the data, information about θ is always available to the decision maker, and that this information can be expressed in terms of a probability distribution on$\theta$ . In such a situation, we show how to compute the Bayes estimator, which is the estimator whose expected squared distance from$\theta$ is minimal. 

## 7.2 MAXIMUM LIKELIHOOD ESTIMATORS

Any statistic used to estimate the value of an unknown parameter θ is called an estimator of θ . The observed value of the estimator is called the estimate. For instance, as we shall see, the usual estimator of the mean of a normal population, based on a sample $X _ { 1 } , \ldots , X _ { n }$ from that population, is the sample mean$\overline { { X } } = \textstyle \sum _ { i } X _ { i } / n$ . If a sample of size 3 yields the data $X _ { 1 } = 2 , X _ { 2 } = 3 , X _ { 3 } = 4$ , then the estimate of the population mean, resulting from the estimator X , is the value 3. 

Suppose that the random variables $X _ { 1 } , \ldots , X _ { n }$ , whose joint distribution is assumed given except for an unknown parameter θ, are to be observed. The problem of interest is to use the observed values to estimate$\theta .$ . For example, the$\vec { X _ { i } ^ { \ : \prime } s }$ might be independent, exponential random variables each having the same unknown mean$\theta .$ . In this case, the joint density function of the random variables would be given by 

$$
\begin{array}{l} f (x _ {1}, x _ {2}, \dots , x _ {n}) \\ = f _ {X _ {1}} (x _ {1}) f _ {X _ {2}} (x _ {2}) \dots f _ {X _ {n}} (x _ {n}) \\ = \frac {1}{\theta} e ^ {- x _ {1} / \theta} \frac {1}{\theta} e ^ {- x _ {2} / \theta} \dots \frac {1}{\theta} e ^ {- x _ {n} / \theta}, \quad 0 <   x _ {i} <   \infty , i = 1, \dots , n \\ = \frac {1}{\theta^ {n}} \exp \left\{- \sum_ {1} ^ {n} x _ {i} / \theta \right\}, \quad 0 <   x _ {i} <   \infty , i = 1, \dots , n \end{array}
$$

and the objective would be to estimate θ from the observed data $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ 

A particular type of estimator, known as the maximum likelihood estimator, is widely used in statistics. It is obtained by reasoning as follows.$\operatorname { L e t } f ( x _ { 1 } , \dots , x _ { n } | \theta )$ ) denote the joint probability mass function of the random variables $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ when they are discrete, and let it be their joint probability density function when they are jointly continuous random variables. Because$\theta$ is assumed unknown, we also write $f$ as a function of$\theta .$ . Now since $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ represents the likelihood that the values $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ will be observed when θ is the true value of the parameter, it would seem that a reasonable estimate of$\theta$ would be that value yielding the largest likelihood of the observed values. In other words, the maximum likelihood estimate$\hat { \theta }$ is defined to be that value of$\theta$ maximizing $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ where $x _ { 1 } , \ldots , x _ { n }$ are the observed values. The function $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ is often referred to as the likelihood function of θ . 

In determining the maximizing value of$\theta ,$ , it is often useful to use the fact that $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ and log[$f ( x _ { 1 } , \dots , x _ { n } | \theta ) ]$ have their maximum at the same value of$\theta$ . Hence, we may also obtain$\hat { \theta }$ by maximizing log$\mathcal { f } ( x _ { 1 } , \dots , x _ { n } | \theta ) ]$ 

EXAMPLE 7.2a Maximum Likelihood Estimator of a Bernoulli Parameter Suppose that n independent trials, each of which is a success with probability ${ \boldsymbol { p } } ,$ are performed. What is the maximum likelihood estimator of$\dot { \boldsymbol { p } } \colon$ 

SOLUTION The data consist of the values of $X _ { 1 } , \ldots , X _ { n }$ where 

$$
X _ {i} = \left\{ \begin{array}{l l} 1 & \text { if   trial   } i \text {   is   a   success } \\ 0 & \text { otherwise } \end{array} \right.
$$

Now 

$$
P \{X _ {i} = 1 \} = p = 1 - P \{X _ {i} = 0 \}
$$

which can be succinctly expressed as 

$$
P \{X _ {i} = x \} = p ^ {x} (1 - p) ^ {1 - x}, \quad x = 0, 1
$$

Hence, by the assumed independence of the trials, the likelihood (that is, the joint probability mass function) of the data is given by 

$$
\begin{array}{r l} & f (x _ {1}, \ldots , x _ {n} | p) = P \{X _ {1} = x _ {1}, \ldots , X _ {n} = x _ {n} | p \} \\ & \qquad = p ^ {x _ {1}} (1 - p) ^ {1 - x _ {1}} \dots p ^ {x _ {n}} (1 - p) ^ {1 - x _ {n}} \\ & \qquad = p ^ {\Sigma_ {1} ^ {n} x _ {i}} (1 - p) ^ {n - \Sigma_ {1} ^ {n} x _ {i}}, \quad x _ {i} = 0, 1, \quad i = 1, \ldots , n \end{array}
$$

To determine the value of$\dot { \mathbf { \rho } } _ { p }$ that maximizes the likelihood, first take logs to obtain 

$$
\log f (x _ {1}, \dots , x _ {n} | p) = \sum_ {1} ^ {n} x _ {i} \log p + \left(n - \sum_ {1} ^ {n} x _ {i}\right) \log (1 - p)
$$

Differentiation yields 

$$
\frac {d}{d p} \log f (x _ {1}, \dots , x _ {n} | p) = \frac {\sum_ {1} ^ {n} x _ {i}}{p} - \frac {(n - \sum_ {1} ^ {n} x _ {i})}{1 - p}
$$

Upon equating to zero and solving, we obtain that the maximum likelihood estimate$\hat { \boldsymbol { p } }$ satisfies 

$$
\frac {\sum_ {1} ^ {n} x _ {i}}{\hat {p}} = \frac {n - \sum_ {1} ^ {n} x _ {i}}{1 - \hat {p}}
$$

or 

$$
\hat {p} = \frac {\sum_ {i = 1} ^ {n} x _ {i}}{n}
$$

Hence, the maximum likelihood estimator of the unknown mean of a Bernoulli distribution is given by 

$$
d (X _ {1}, \ldots , X _ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}
$$

Since$\sum _ { i = 1 } ^ { n } X _ { i }$ is the number of successful trials, we see that the maximum likelihood estimator of$\dot { \mathbf { \Omega } } _ { p }$ is equal to the proportion of the observed trials that result in successes. For an illustration, suppose that each RAM (random access memory) chip produced by a certain manufacturer is, independently, of acceptable quality with probability$\scriptstyle { \boldsymbol { p } } .$ . Then if out of a sample of 1,000 tested 921 are acceptable, it follows that the maximum likelihood estimate of$\dot { \boldsymbol { p } }$ is .921. ■ 

EXAMPLE 7.2b Two proofreaders were given the same manuscript to read. If proofreader 1 found $n _ { 1 }$ errors, and proofreader 2 found $n _ { 2 }$ errors, with $_ { n _ { 1 , 2 } }$ of these errors being found by both proofreaders, estimate $N ,$ the total number of errors that are in the manuscript. 

SOLUTION Before we can estimate N we need to make some assumptions about the underlying probability model. So let us assume that the results of the proofreaders are independent, and that each error in the manuscript is independently found by proofreader i with probability$\ p _ { i } , i = 1 , 2$ 

To estimate $N ,$ we will start by deriving an estimator of$\displaystyle { \phi _ { 1 } }$ . To do so, note that each of the $n _ { 2 }$ errors found by reader 2 will, independently, be found by proofreader 1 with probability$\mathbf { \nabla } \phi _ { i } .$ . Because proofreader 1 found $_ { n _ { 1 , 2 } }$ of those $n _ { 2 }$ errors, a reasonable estimate of$\dot { p } _ { 1 }$ is given by 

$$
\hat {p} _ {1} = \frac {n _ {1 , 2}}{n _ {2}}
$$

However, because proofreader 1 found $n _ { 1 }$ of the N errors in the manuscript, it is reasonable to suppose that$\displaystyle { \phi _ { 1 } }$ is also approximately equal to$\textstyle { \frac { n _ { 1 } } { N } }$ . Equating this to$\hat { p } _ { 1 }$ gives that 

$$
\frac {n _ {1 , 2}}{n _ {2}} \approx \frac {n _ {1}}{N}
$$

or 

$$
N \approx \frac {n _ {1} n _ {2}}{n _ {1 , 2}}
$$

Because the preceding estimate is symmetric in $n _ { 1 }$ and $n _ { 2 }$ , it follows that it is the same no matter which proofreader is designated as proofreader 1. 

An interesting application of the preceding occurred when two teams of researchers recently announced that they had decoded the human genetic code sequence. As part of their work both teams estimated that the human genome consisted of approximately 33,000 genes. Because both teams independently arrived at the same number, many scientists found this number believable. However, most scientists were quite surprised by this relatively small number of genes; by comparison it is only about twice as many as a fruit fly has. However, a closer inspection of the findings indicated that the two group only agreed on the existence of about 17,000 genes. (That is, 17,000 genes were found by both teams.) Thus, based on our preceding estimator, we would estimate that the actual number of genes, rather than being 33,000, is 

$$
\frac {n _ {1} n _ {2}}{n _ {1 , 2}} = \frac {3 3 , 0 0 0 \times 3 3 , 0 0 0}{1 7 , 0 0 0} \approx 6 4, 0 0 0
$$

(Because there is some controversy about whether some of genes claimed to be found are actually genes, 64,000 should probably be taken as an upper bound on the actual number of genes.) 

The estimation approach used when there are two proofreaders does not work when there are m proofreaders, when $m > 2$ . For, if for each $i ,$ we let$\hat { \ b { p } } _ { i }$ be the fraction of the errors found by at least one of the other proofreader $j ,$$( j \neq i )$ , that are also found by $i ,$ and then set that equal to$\frac { n _ { i } } { N }$ , then the estimate of $N ,$ namely$\frac { n _ { i } } { \hat { \rho } _ { i } }$ , would differ for different values of $i .$ Moreover, with this approach it is possible that we may have that$\hat { p } _ { i } > \hat { p } _ { j }$ even if proofreader i finds fewer errors than does proofreader $j .$ . For instance, for $m = 3$ suppose proofreaders 1 and 2 find exactly the same set of 10 errors whereas proofreader 3 finds 20 errors with only 1 of them in common with the set of errors found by the others. Then, because proofreader 1 (and 2) found 10 of the 29 errors found by at least one of the other proofreaders,$\hat { p } _ { i } = 1 0 / 2 9 , i = 1 , 2$ . On the other hand, because proofreader 3 only found 1 of the 10 errors found by the others,$\hat { p } _ { 3 } = 1 / 1 0$ . Therefore, although proofreader 3 found twice the number of errors as did proofreader 1, the estimate of$\mathit { p 3 }$ is less than that of$\dot { p } _ { 1 }$ . To obtain more reasonable estimates, we could take the preceding values of$\hat { p } _ { i } , i = 1 , \ldots , m$ , as preliminary estimates of the$\mathbf { \nabla } \phi _ { i }$ . Now, let $n _ { f }$ be the number of errors that are found by at least one proofreader. Because n<sub>f</sub> /N is the fraction of errors that are found by at least one proofreader, this should approximately equal$\textstyle 1 - \prod _ { i = 1 } ^ { m } ( 1 - p _ { i } )$ , the probability that an error is found by at least one proofreader. Therefore, we have 

$$
{\frac {n _ {f}}{N}} \approx 1 - \prod_ {i = 1} ^ {m} (1 - p _ {i})
$$

suggesting that $N \approx \hat { N }$ , where 

$$
\hat {N} = \frac {n _ {f}}{1 - \prod_ {i = 1} ^ {m} (1 - \hat {p} _ {i})}\tag{7.2.1}
$$

With this estimate of N, we can then reset our estimates of the$\mathbf { \nabla } _ { \mathbf { \beta } } ^ { \mathbf { \gamma } _ { \mathbf { \beta } } ^ { \mathbf { \gamma } _ { \mathbf { \hat { \varepsilon } } } ^ { \mathbf { \varepsilon } } } }$ by using 

$$
\hat {p} _ {i} = \frac {n _ {i}}{\hat {N}}, \quad i = 1, \ldots , m\tag{7.2.2}
$$

We can then reestimate N by using the new value (7.2.1). (The estimation need not stop here; each time we obtain a new estimate$\hat { N }$ of N we can use (7.2.2) to obtain new estimates of the$\mathbf { \nabla } _ { \mathbf { \mathit { p } } _ { i } }$ , which can then be used to obtain a new estimate of $N ,$ and so on.) ■ 

EXAMPLE 7.2c Maximum Likelihood Estimator of a Poisson Parameter Suppose $X _ { 1 } , \ldots , X _ { n }$ are independent Poisson random variables each having mean$\lambda .$ . Determine the maximum likelihood estimator of$\lambda$ . 

SOLUTION The likelihood function is given by 

$$
\begin{array}{c} f (x _ {1}, \ldots , x _ {n} | \lambda) = \frac {e ^ {- \lambda} \lambda^ {x _ {1}}}{x _ {1} !} \dots \frac {e ^ {- \lambda} \lambda^ {x _ {n}}}{x _ {n} !} \\ = \frac {e ^ {- n \lambda} \lambda^ {\sum_ {1} ^ {n} x _ {i}}}{x _ {1} ! \ldots x _ {n} !} \end{array}
$$

Thus, 

$$
\log f (x _ {1}, \dots , x _ {n} | \lambda) = - n \lambda + \sum_ {1} ^ {n} x _ {i} \log \lambda - \log c
$$

where $c = \prod _ { i = 1 } ^ { n }$ x ! does not depend on$\lambda ,$ and 

$$
{\frac {d}{d \lambda}} \log f (x _ {1}, \ldots , x _ {n} | \lambda) = - n + {\frac {\sum_ {1} ^ {n} x _ {i}}{\lambda}}
$$

By equating to zero, we obtain that the maximum likelihood estimate$\hat { \lambda }$ equal 

$$
\hat {\lambda} = \frac {\sum_ {1} ^ {n} x _ {i}}{n}
$$

and so the maximum likelihood estimator is given by 

$$
d (X _ {1}, \ldots , X _ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}
$$

For example, suppose that the number of people that enter a certain retail establishment in any day is a Poisson random variable having an unknown mean λ, which must be estimated. If after 20 days a total of 857 people have entered the establishment, then the maximum likelihood estimate of λ is $8 5 7 / 2 0 \ = \ 4 2 . 8 5$ . That is, we estimate that on average, 42.85 customers will enter the establishment on a given day. ■ 

EXAMPLE 7.2d The number of traffic accidents in Berkeley, California, in 10 randomly chosen nonrainy days in 1998 is as follows: 

$$
4, 0, 6, 5, 2, 1, 2, 0, 4, 3
$$

Use these data to estimate the proportion of nonrainy days that had 2 or fewer accidents that year. 

SOLUTION Since there are a large number of drivers, each of whom has a small probability of being involved in an accident in a given day, it seems reasonable to assume that the daily number of traffic accidents is a Poisson random variable. Since 

$$
\overline {{{X}}} = \frac {1}{1 0} \sum_ {i = 1} ^ {1 0} X _ {i} = 2. 7
$$

it follows that the maximum likelihood estimate of the Poisson mean is 2.7. Since the long-run proportion of nonrainy days that have 2 or fewer accidents is equal to $P \{ X \leq 2 \}$ where X is the random number of accidents in a day, it follows that the desired estimate is 

$$
e ^ {- 2. 7} (1 + 2. 7 + (2. 7) ^ {2} / 2) = . 4 9 3 6
$$

That is, we estimate that a little less than half of the nonrainy days had 2 or fewer accidents. ■ 

EXAMPLE 7.2e Maximum Likelihood Estimator in a Normal Population Suppose $X _ { 1 } , \ldots , X _ { n }$ are independent, normal random variables each with unknown mean$\mu$ and unknown standard deviation$\sigma$ . The joint density is given by 

$$
\begin{array}{c} f (x _ {1}, \ldots , x _ {n} | \mu , \sigma) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} \exp \left[ \frac {- (x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}} \right] \\ = \left(\frac {1}{2 \pi}\right) ^ {n / 2} \frac {1}{\sigma^ {n}} \exp \left[ \frac {- \sum_ {1} ^ {n} (x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}} \right] \end{array}
$$

The logarithm of the likelihood is thus given by 

$$
\log f (x _ {1}, \ldots , x _ {n} | \mu , \sigma) = - \frac {n}{2} \log (2 \pi) - n \log \sigma - \frac {\sum_ {1} ^ {n} (x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}}
$$

In order to find the value of ${ \bf \dot { \boldsymbol \mu } } _ { \mu }$ and$\sigma$ maximizing the foregoing, we compute 

$$
\begin{array}{l} \frac {\partial}{\partial \mu} \log f (x _ {1}, \ldots , x _ {n} | \mu , \sigma) = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \mu)}{\sigma^ {2}} \\ \frac {\partial}{\partial \sigma} \log f (x _ {1}, \ldots , x _ {n} | \mu , \sigma) = - \frac {n}{\sigma} + \frac {\sum_ {1} ^ {n} (x _ {i} - \mu) ^ {2}}{\sigma^ {3}} \end{array}
$$

Equating these equations to zero yields that 

$$
\hat {\mu} = \sum_ {i = 1} ^ {n} x _ {i} / n
$$

and 

$$
\hat {\sigma} = \left[ \sum_ {i = 1} ^ {n} (x _ {i} - \hat {\mu}) ^ {2} / n \right] ^ {1 / 2}
$$

Hence, the maximum likelihood estimators of$\mu$ and$\sigma$ are given, respectively, by 

$$
\overline {{X}} \quad \text { and } \quad \left[ \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2} / n \right] ^ {1 / 2}\tag{7.2.3}
$$

It should be noted that the maximum likelihood estimator of the standard deviation$\sigma$ differs from the sample standard deviation 

$$
S = \left[ \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2} / (n - 1) \right] ^ {1 / 2}
$$

in that the denominator in Equation 7.2.3 is$\sqrt { n }$ rather than$\sqrt { n - 1 }$ . However, for n of reasonable size, these two estimators of$\dot { } \sigma$ will be approximately equal. ■ 

EXAMPLE 7.2f Kolmogorov’s law of fragmentation states that the size of an individual particle in a large collection of particles resulting from the fragmentation of a mineral compound will have an approximate lognormal distribution, where a random variable X is said to have a lognormal distribution if log(X ) has a normal distribution. The law, which was first noted empirically and then later given a theoretical basis by Kolmogorov, has been applied to a variety of engineering studies. For instance, it has been used in the analysis of the size of randomly chosen gold particles from a collection of gold sand. A less obvious application of the law has been to a study of the stress release in earthquake fault zone (see Lomnitz, C., “Global Tectonics and Earthquake Risk,” Developments in Geotectonics, Elsevier, Amsterdam, 1979). 

Suppose that a sample of 10 grains of metallic sand taken from a large sand pile have respective lengths (in millimeters): 

$$
2. 2, 3. 4, 1. 6, 0. 8, 2. 7, 3. 3, 1. 6, 2. 8, 2. 5, 1. 9
$$

Estimate the percentage of sand grains in the entire pile whose length is between 2 and 3 mm. 

SOLUTION Taking the natural logarithm of these 10 data values, the following transformed data set results 

$$
. 7 8 8 5, 1. 2 2 3 8,. 4 7 0 0, -. 2 2 3 1,. 9 9 3 3, 1. 1 9 3 9,. 4 7 0 0, 1. 0 2 9 6,. 9 1 6 3,. 6 4 1 9
$$

Because the sample mean and sample standard deviation of these data are 

$$
\overline {{{{x}}}} = . 7 5 0 4, \quad s = . 4 3 5 1
$$

it follows that the logarithm of the length of a randomly chosen grain has a normal distribution with mean approximately equal to .7504 and with standard deviation approximately equal to .4351. Hence, if X is the length of the grain, then 

$$
\begin{array}{l} P \{2 <   X <   3 \} = P \{\log (2) <   \log (X) <   \log (3) \} \\ \qquad = P \left\{\frac {\log (2) - . 7 5 0 4}{. 4 3 5 1} <   \frac {\log (X) - . 7 5 0 4}{. 4 3 5 1} <   \frac {\log (3) - . 7 5 0 4}{. 4 3 5 1} \right\} \\ \qquad = P \left\{-. 1 3 1 6 <   \frac {\log (X) - . 7 5 0 4}{. 4 3 5 1} <  . 8 0 0 3 \right\} \\ \qquad \approx \Phi (. 8 0 0 3) - \Phi (-. 1 3 1 6) \\ \qquad = . 3 4 0 5 \quad \blacksquare \end{array}
$$

In all of the foregoing examples, the maximum likelihood estimator of the population mean turned out to be the sample mean$\overline { { X } }$ . To show that this is not always the situation, consider the following example. 

EXAMPLE 7.2g Estimating the Mean of a Uniform Distribution Suppose $X _ { 1 } , \ldots , X _ { n }$ constitute a sample from a uniform distribution on $( 0 , \theta )$ ), where$\theta$ is unknown. Their joint density is thus 

$$
f (x _ {1}, x _ {2}, \dots , x _ {n} | \theta) = \left\{ \begin{array}{l l} \frac {1}{\theta^ {n}} & 0 <   x _ {i} <   \theta , \quad i = 1, \dots , n \\ 0 & \text { otherwise } \end{array} \right.
$$

This density is maximized by choosing$\theta$ as small as possible. Since$\theta$ must be at least as large as all of the observed values $x _ { i } ,$ , it follows that the smallest possible choice of$\ni$ is equal to max $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ . Hence, the maximum likelihood estimator of$\cdot _ { \theta }$ is 

$$
\hat {\theta} = \max (X _ {1}, X _ {2}, \ldots , X _ {n})
$$

It easily follows from the foregoing that the maximum likelihood estimator of$\theta / 2 ,$ , the mean of the distribution, is max $( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } ) / 2$ ■ 

## *7.2.1 Estimating Life Distributions

Let X denote the age at death of a randomly chosen child born today. That is,$X = i$ if the newborn dies in its ith year,$i \geq 1$ . To estimate the probability mass function of X, let$\lambda _ { i }$ denote the probability that a newborn who has survived his or her first $i - 1$ years 

dies in year i. That is, 

$$
\lambda_ {i} = P \{X = i | X > i - 1 \} = \frac {P \{X = i \}}{P \{X > i - 1 \}}
$$

Also, let 

$$
s _ {i} = 1 - \lambda_ {i} = \frac {P \{X > i \}}{P \{X > i - 1 \}}
$$

be the probability that a newborn who survives her first $i - 1$ years also survives year i. The quantity$\lambda _ { i }$ is called the failure rate, and $s _ { i }$ is called the survival rate, of an individual who is entering his or her ith year. Now, 

$$
\begin{array}{c} s _ {1} s _ {2} \dots s _ {i} = P \{X > 1 \} \frac {P \{X > 2 \} P \{X > 3 \}}{P \{X > 1 \} P \{X > 2 \}} \dots \frac {P \{X > i \}}{P \{X > i - 1 \}} \\ = P \{X > i \} \end{array}
$$

Therefore, 

$$
P \{X = n \} = P \{X > n - 1 \} \lambda_ {n} = s _ {1} \dots s _ {n - 1} (1 - s _ {n})
$$

Consequently, we can estimate the probability mass function of X by estimating the quantities $s _ { i } , i = 1 , \ldots , n .$ . The value $s _ { i }$ can be estimated by looking at all individual in the population who reached age i one year ago, and then letting the estimate$\hat { s } _ { i }$ be the fraction of them who are alive today. We would then use$\hat { s } _ { 1 } \hat { s } _ { 2 } \cdot \cdot \cdot \hat { s } _ { n - 1 } \big ( 1 - \hat { s } _ { n } \big )$ as the estimate of $P \{ X = n \}$ . (Note that although we are using the most recent possible data to estimate the quantities $s _ { i } ,$ , our estimate of the probability mass function of the lifetime of a newborn assumes that the survival rate of the newborn when it reaches age i will be the same as last year’s survival rate of someone of age $i . )$ 

The use of the survival rate to estimate a life distribution is also of importance in health studies with partial information. For instance, consider a study in which a new drug is given to a random sample of 12 lung cancer patients. Suppose that after some time we have the following data on the number of months of survival after starting the new drug: 

$$
4, 7 ^ {*}, 9, 1 1 ^ {*}, 1 2, 3, 1 4 ^ {*}, 1, 8, 7, 5, 3 ^ {*}
$$

where x means that the patient died in month x after starting the drug treatment, and $x ^ { * }$ means that the patient has taken the drug for x months and is still alive. 

Let X equal the number of months of survival after beginning the drug treatment, and let 

$$
s _ {i} = P \{X > i | X > i - 1 \} = \frac {P \{X > i \}}{P \{X > i - 1 \}}
$$

To estimate $s _ { i } ,$ , the probability that a patient who has survived the first $i - 1$ months will also survive month $i ,$ we should take the fraction of those patients who began their ith month of drug taking and survived the month. For instance, because 11 of the 12 patients survived month 1,$\hat { s } _ { 1 } = 1 1 / 1 2$ . Because all 11 patients who began month 2 survived,$\hat { s } _ { 2 } = 1 1 / 1 1$ . Because 10 of the 11 patients who began month 3 survived,$\hat { s } _ { 3 } = 1 0 / 1 1$ Because 8 of the 9 patients who began their fourth month of taking the drug (all but the ones labelled 1, 3, and 3<sup>∗</sup>) survived month 4,$\hat { s } _ { 4 } = 8 / 9$ . Similar reasoning holds for the others, giving the following survival rate estimates: 

$$
\begin{array}{r l} & {\hat {s} _ {1} = 1 1 / 1 2} \\ & {\hat {s} _ {2} = 1 1 / 1 1} \\ & {\hat {s} _ {3} = 1 0 / 1 1} \\ & {\hat {s} _ {4} = 8 / 9} \\ & {\hat {s} _ {5} = 7 / 8} \\ & {\hat {s} _ {6} = 7 / 7} \\ & {\hat {s} _ {7} = 6 / 7} \\ & {\hat {s} _ {8} = 4 / 5} \\ & {\hat {s} _ {9} = 3 / 4} \\ & {\hat {s} _ {1 0} = 3 / 3} \\ & {\hat {s} _ {1 1} = 3 / 3} \\ & {\hat {s} _ {1 2} = 1 / 2} \\ & {\hat {s} _ {1 3} = 1 / 1} \\ & {\hat {s} _ {1 4} = 1 / 2} \end{array}
$$

We can now use$\textstyle \prod _ { i = 1 } ^ { j } { \widehat { s } } _ { i }$ to estimate the probability that a drug taker survives at least j time periods,$j = 1 , \dotsc , 1 4$ . For instance, our estimate of $P \{ X > 6 \}$ is 35/54. 

## 7.3 INTERVAL ESTIMATES

Suppose that $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population having unknown mean$\mu$ and known variance$\sigma ^ { 2 }$ . It has been shown that$\textstyle { \overline { { X } } } = { \dot { \sum } } _ { i = 1 } ^ { \widehat { n } } X _ { i } / n$ is the maximum likelihood estimator for$\mu .$ . However, we don’t expect that the sample mean$\overline { { X } }$ will exactly equal$\mu ,$ , but rather that it will “be close.” Hence, rather than a point estimate, it is sometimes more valuable to be able to specify an interval for which we have a certain degree of confidence that$\mu$ lies within. To obtain such an interval estimator, we make use of the probability distribution of the point estimator. Let us see how it works for the preceding situation. 

## 7.3 Interval Estimates

In the foregoing, since the point estimator$\overline { { X } }$ is normal with mean$\mu$ and variance$\sigma ^ { 2 } / n _ { ; }$ it follows that 

$$
\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} = \sqrt {n} \frac {(\overline {{X}} - \mu)}{\sigma}
$$

has a standard normal distribution. Therefore, 

$$
P \left\{- 1. 9 6 <   \sqrt {n} \frac {(\overline {{{X}}} - \mu)}{\sigma} <   1. 9 6 \right\} = . 9 5
$$

or, equivalently, 

$$
P \left\{- 1. 9 6 \frac {\sigma}{\sqrt {n}} <   \overline {{{X}}} - \mu <   1. 9 6 \frac {\sigma}{\sqrt {n}} \right\} = . 9 5
$$

Multiplying through by −1 yields the equivalent statement 

$$
P \left\{- 1. 9 6 \frac {\sigma}{\sqrt {n}} <   \mu - \overline {{X}} <   1. 9 6 \frac {\sigma}{\sqrt {n}} \right\} = . 9 5
$$

or, equivalently, 

$$
P \left\{\overline {{{X}}} - 1. 9 6 \frac {\sigma}{\sqrt {n}} <   \mu <   \overline {{{X}}} + 1. 9 6 \frac {\sigma}{\sqrt {n}} \right\} = . 9 5
$$

That is, 95 percent of the time$\mu$ will lie within 1.96σ$I \sqrt { n }$ units of the sample average. If we now observe the sample and it turns out that ${ \overline { { X } } } = { \overline { { x } } }$ , then we say that “with 95 percent confidence” 

$$
\overline {{{x}}} - 1. 9 6 \frac {\sigma}{\sqrt {n}} <   \mu <   \overline {{{x}}} + 1. 9 6 \frac {\sigma}{\sqrt {n}}\tag{7.3.1}
$$

That is, “with 95 percent confidence” we assert that the true mean lies within 1. 96σ$I \sqrt { n }$ of the observed sample mean. The interval 

$$
\left(\overline {{x}} - 1. 9 6 \frac {\sigma}{\sqrt {n}}, \overline {{x}} + 1. 9 6 \frac {\sigma}{\sqrt {n}}\right)
$$

is called a 95 percent confidence interval estimate of$\mu$ . 

EXAMPLE 7.3a Suppose that when a signal having value$\mu$ is transmitted from location A the value received at location B is normally distributed with mean$\mu$ and variance $4 .$ . That is, if$\mu$ is sent, then the value received is$\mu + N$ where N , representing noise, is normal with mean $_ 0$ and variance $4 .$ . To reduce error, suppose the same value is sent 9 times. If the successive values received are 5, 8.5, 12, 15, 7, 9, 7.5, 6.5, 10.5, let us construct a 95 percent confidence interval for$\mu$ 

Since 

$$
\overline {{{x}}} = \frac {8 1}{9} = 9
$$

It follows, under the assumption that the values received are independent, that a 95 percent confidence interval for$\mu$ is 

$$
\left(9 - 1. 9 6 \frac {\sigma}{3}, 9 + 1. 9 6 \frac {\sigma}{3}\right) = (7. 6 9, 1 0. 3 1)
$$

Hence, we are $^ { \mathfrak { a } } 9 5$ percent confident” that the true message value lies between 7.69 and 10.31. ■ 

The interval in Equation 7.3.1 is called a two-sided confidence interval. Sometimes, however, we are interested in determining a value so that we can assert with, say, 95 percent confidence, that$\mu$ is at least as large as that value. 

To determine such a value, note that if Z is a standard normal random variable then 

$$
P \{Z <   1. 6 4 5 \} = . 9 5
$$

As a result, 

$$
P \left\{\sqrt {n} \frac {(\overline {{{X}}} - \mu)}{\sigma} <   1. 6 4 5 \right\} = . 9 5
$$

or 

$$
P \left\{\overline {{{X}}} - 1. 6 4 5 \frac {\sigma}{\sqrt {n}} <   \mu \right\} = . 9 5
$$

Thus, a 95 percent one-sided upper confidence interval for$\mu$ is 

$$
\left(\overline {{x}} - 1. 6 4 5 \frac {\sigma}{\sqrt {n}}, \infty\right)
$$

where$\overline { { x } }$ is the observed value of the sample mean. 

A one-sided lower confidence interval is obtained similarly; when the observed value of the sample mean is ${ \overline { { x } } } ,$ then the 95 percent one-sided lower confidence interval for$\mu$ is 

$$
\left(- \infty , \overline {{x}} + 1. 6 4 5 \frac {\sigma}{\sqrt {n}}\right)
$$

EXAMPLE 7.3b Determine the upper and lower 95 percent confidence interval estimates of$\dot { \mu }$ in Example 7.3a. 

7.3 Interval Estimates 

SOLUTION Since 

$$
1. 6 4 5 \frac {\sigma}{\sqrt {n}} = \frac {3 . 2 9}{3} = 1. 0 9 7
$$

the 95 percent upper confidence interval is 

$$
(9 - 1. 0 9 7, \infty) = (7. 9 0 3, \infty)
$$

and the 95 percent lower confidence interval is 

$$
(- \infty , 9 + 1. 0 9 7) = (- \infty , 1 0. 0 9 7)
$$

We can also obtain confidence intervals of any specified level of confidence. To do $s 0 ;$ , recall that ${ z } _ { \alpha }$ is such that 

$$
P \{Z > z _ {\alpha} \} = \alpha
$$

when $Z$ is a standard normal random variable. But this implies (see Figure 7.1) that for any α 

$$
P \{- z _ {\alpha / 2} <   Z <   z _ {\alpha / 2} \} = 1 - \alpha
$$

As a result, we see that 

$$
P \left\{- z _ {\alpha / 2} <   \sqrt {n} \frac {(\overline {{X}} - \mu)}{\sigma} <   z _ {\alpha / 2} \right\} = 1 - \alpha
$$

or 

$$
P \left\{- z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}} <   \overline {{X}} - \mu <   z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}} \right\} = 1 - \alpha
$$

or 

$$
P \left\{- z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}} <   \mu - \overline {{X}} <   z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}} \right\} = 1 - \alpha
$$

That is, 

$$
P \left\{\overline {{X}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}} <   \mu <   \overline {{X}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}} \right\} = 1 - \alpha
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/93064a3121114bdf6d4288c31598ae7c95de3c37e36809e36e7a56e99c6263c8.jpg)



FIGURE 7.1 ${ \cal P } \{ - z _ { \alpha / 2 } < Z < z _ { \alpha / 2 } \} = 1 - \alpha .$


Hence, a $1 0 0 ( 1 - \alpha )$ percent two-sided confidence interval for$\mu$ is 

$$
\left(\overline {{x}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \quad \overline {{x}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right)
$$

where$\overline { { x } }$ is the observed sample mean. 

Similarly, knowing that $Z = { \sqrt { n } } { \frac { ( { \overline { { X } } } - \mu ) } { \sigma } }$ is a standard normal random variable, along with the identities 

$$
P \{Z > z _ {\alpha} \} = \alpha
$$

and 

$$
P \{Z <   - z _ {\alpha} \} = \alpha
$$

results in one-sided confidence intervals of any desired level of confidence. Specifically, we obtain that 

$$
\left(\overline {{x}} - z _ {\alpha} \frac {\sigma}{\sqrt {n}}, \infty\right)
$$

and 

$$
\left(- \infty , \overline {{x}} + z _ {\alpha} \frac {\sigma}{\sqrt {n}}\right)
$$

are, respectively,$1 0 0 ( 1 - \alpha )$ percent one-sided upper and $1 0 0 ( 1 - \alpha )$ percent one-sided lower confidence intervals for$\mu$ 

EXAMPLE 7.3c Use the data of Example 7.3a to obtain a 99 percent confidence interval estimate of$\dot { \mathbf { \Omega } } _ { \mu }$ , along with 99 percent one-sided upper and lower intervals. 

SOLUTION Since $z _ { . 0 0 5 } = 2 . 5 8$ , and 

$$
2. 5 8 \frac {\alpha}{\sqrt {n}} = \frac {5 . 1 6}{3} = 1. 7 2
$$

it follows that a 99 percent confidence interval for$\mu$ is 

$$
9 \pm 1. 7 2
$$

That is, the 99 percent confidence interval estimate is (7.28, 10.72). 

Also, since $z _ { . 0 1 } = 2 . 3 3 , \mathrm { a }$ 99 percent upper confidence interval is 

$$
(9 - 2. 3 3 (2 / 3), \infty) = (7. 4 4 7, \infty)
$$

Similarly, a 99 percent lower confidence interval is 

$$
(- \infty , 9 + 2. 3 3 (2 / 3)) = (- \infty , 1 0. 5 5 3)
$$

Sometimes we are interested in a two-sided confidence interval of a certain level, say $1 - \alpha _ { \mathrm { { i } } }$ , and the problem is to choose the sample size n so that the interval is of a certain size. For instance, suppose that we want to compute an interval of length .1 that we can assert, with 99 percent confidence, contains$\mu .$ . How large need n be? To solve this, note that as $z _ { . 0 0 5 } = 2 . 5 8$ it follows that the 99 percent confidence interval for$\mu$ from a sample of size n is 

$$
\left(\overline {{x}} - 2. 5 8 \frac {\alpha}{\sqrt {n}}, \quad \overline {{x}} + 2. 5 8 \frac {\alpha}{\sqrt {n}}\right)
$$

Hence, its length is 

$$
5. 1 6 \frac {\sigma}{\sqrt {n}}
$$

Thus, to make the length of the interval equal to .1, we must choose 

$$
5. 1 6 \frac {\sigma}{\sqrt {n}} = . 1
$$

or 

$$
n = (5 1. 6 \sigma) ^ {2}
$$

## REMARK

The interpretation of$\mathfrak { a } \ 1 0 0 ( 1 - \alpha )$ percent confidence interval” can be confusing. It should be noted that we are not asserting that the probability that$\mu \in ( { \overline { { x } } } - 1 . 9 6 \sigma / { \sqrt { n } } , { \overline { { x } } } +$$1 . 9 6 \sigma / { \sqrt { n } } )$ is .95, for there are no random variables involved in this assertion. What we are asserting is that the technique utilized to obtain this interval is such that 95 percent of the time that it is employed it will result in an interval in which$\mu$ lies. In other words, before the data are observed we can assert that with probability .95 the interval that will be obtained will contain$\mu ,$ , whereas after the data are obtained we can only assert that the resultant interval indeed contains$\mu$ “with confidence .95.” 

EXAMPLE 7.3d From past experience it is known that the weights of salmon grown at a commercial hatchery are normal with a mean that varies from season to season but with a standard deviation that remains fixed at 0.3 pounds. If we want to be 95 percent certain that our estimate of the present season’s mean weight of a salmon is correct to within$\pm 0 . 1$ pounds, how large a sample is needed? 

SOLUTION A 95 percent confidence interval estimate for the unknown mean$\mu ,$ , based on a sample of size $^ { n , }$ is 

$$
\mu \in \left(\overline {{x}} - 1. 9 6 \frac {\sigma}{\sqrt {n}}, \overline {{x}} + 1. 9 6 \frac {\sigma}{\sqrt {n}}\right)
$$

Because the estimate$\overline { { x } }$ is within $1 . 9 6 ( \sigma / \sqrt { n } ) = . 5 8 8 / \sqrt { n }$ of any point in the interval, it follows that we can be 95 percent certain that x is within 0.1 of$\dot { \mathbf { \Omega } } _ { \mu }$ provided that 

$$
\frac {. 5 8 8}{\sqrt {n}} \leq 0. 1
$$

That is, provided that 

$$
\sqrt {n} \geq 5. 8 8
$$

or 

$$
n \geq 3 4. 5 7
$$

That is, a sample size of 35 or larger will suffice. ■ 

## 7.3.1 Confidence Interval for a Normal Mean When the Variance Is Unknown

Suppose now that $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal distribution with unknown mean$\mu$ and unknown variance$\sigma ^ { 2 }$ , and that we wish to construct a $1 0 0 ( 1 { - } \alpha )$ percent confidence interval for$\mu .$ . Since$\sigma$ is unknown, we can no longer base our interval on the fact that ${ \sqrt { n } } ( { \overline { { X } } } - \mu )$ /σ is a standard normal random variable. However, by letting$\begin{array} { r } { S ^ { 2 } = \sum _ { i = 1 } ^ { n } ( X _ { i } - } \end{array}$${ \overline { { X } } } ) ^ { 2 } / ( n - 1 )$ denote the sample variance, then from Corollary 6.5.2 it follows that 

$$
\sqrt {n} \frac {(\overline {{X}} - \mu)}{S}
$$

is a t-random variable with $n - 1$ degrees of freedom. Hence, from the symmetry of the t-density function (see Figure 7.2), we have that for any$\alpha \in ( 0 , 1 / 2 )$ , 

$$
P \left\{- t _ {\alpha / 2, n - 1} <   \sqrt {n} \frac {(\overline {{X}} - \mu)}{S} <   t _ {\alpha / 2, n - 1} \right\} = 1 - \alpha
$$

or, equivalently, 

$$
P \left\{\overline {{X}} - t _ {\alpha / 2, n - 1} \frac {S}{\sqrt {n}} <   \mu <   \overline {{X}} + t _ {\alpha / 2, n - 1} \frac {S}{\sqrt {n}} \right\} = 1 - \alpha
$$

Thus, if it is observed that ${ \overline { { X } } } = { \overline { { x } } }$ and $S = s ,$ then we can say that “with $1 0 0 ( 1 - \alpha )$ percent confidence” 

$$
\mu \in \left(\overline {{x}} - t _ {\alpha / 2, n - 1} \frac {s}{\sqrt {n}}, \overline {{x}} + t _ {\alpha / 2, n - 1} \frac {s}{\sqrt {n}}\right)
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/844d9b068a3b2a11d80a8ca8901f8384b2b2d9cf5b85cf73babcffec68611c4f.jpg)



FIGURE 7.2 t -density function.


EXAMPLE 7.3e Let us again consider Example 7.3a but let us now suppose that when the value$\mu$ is transmitted at location A then the value received at location B is normal with mean µ and variance$\sigma ^ { 2 }$ but with$\sigma ^ { 2 }$ being unknown. If 9 successive values are, as in Example 7.3a, 5, 8.5, 12, 15, 7, 9, 7.5, 6.5, 10.5, compute a 95 percent confidence interval for$\mu$ . 

SOLUTION A simple calculation yields that 

$$
\overline {{x}} = 9
$$

and 

$$
s ^ {2} = \frac {\sum x _ {i} ^ {2} - 9 (\overline {{{x}}}) ^ {2}}{8} = 9. 5
$$

or 

$$
s = 3. 0 8 2
$$

Hence, as $t _ { . 0 2 5 , 8 } = 2 . 3 0 6 ,$ , a 95 percent confidence interval for$\mu$ is 

$$
\left[ 9 - 2. 3 0 6 \frac {(3 . 0 8 2)}{3}, 9 + 2. 3 0 6 \frac {(3 . 0 8 2)}{3} \right] = (6. 6 3, 1 1. 3 7)
$$

a larger interval than obtained in Example 7.3a. The reason why the interval just obtained is larger than the one in Example 7.3a is twofold. The primary reason is that we have a larger estimated variance than in Example 7.3a. That is, in Example 7.3a we assumed that$\sigma ^ { 2 }$ was known to equal 4, whereas in this example we assumed it to be unknown and our estimate of it turned out to be 9.5, which resulted in a larger confidence interval. In fact, the confidence interval would have been larger than in Example 7.3a even if our estimate of$\sigma ^ { 2 }$ was again 4 because by having to estimate the variance we need to utilize the t-distribution, which has a greater variance and thus a larger spread than the standard normal (which can be used when$\sigma ^ { 2 }$ is assumed known). For instance, if it had turned out that$\overline { { x } } = 9$ and $s ^ { 2 } = 4$ , then our confidence interval would have been 

$$
(9 - 2. 3 0 6 \cdot \frac {2}{3}, 9 + 2. 3 0 6 \cdot \frac {2}{3}) = (7. 4 6, 1 0. 5 4)
$$

which is larger than that obtained in Example 7.3a. ■ 

## REMARKS

(a) The confidence interval for µ when σ is known is based on the fact that ${ \sqrt { n } } ( { \overline { { X } } } -$$\mu ) / \sigma$ has a standard normal distribution. When σ is unknown, the foregoing approach is to estimate it by S and then use the fact that ${ \sqrt { n } } ( { \overline { { X } } } - \mu ) / S$ has a t -distribution with $n - 1$ degrees of freedom. 

(b) The length of a $1 0 0 ( 1 - \alpha )$ percent confidence interval for$\mu$ is not always larger when the variance is unknown. For the length of such an interval is $2 z _ { \alpha } \sigma / { \sqrt { n } }$ when$\sigma$ is known, whereas it is $2 t _ { \alpha , n - 1 } S / \sqrt { n }$ when$\sigma$ is unknown; and it is certainly possible that the sample standard deviation S can turn out to be much smaller than σ . However, it can be shown that the mean length of the interval is longer when σ is unknown. That is, it can be shown that 

$$
t _ {\alpha , n - 1} E [ S ] \geq z _ {\alpha} \sigma
$$

Indeed, E [S] is evaluated in Chapter 14 and it is shown, for instance, that 

$$
E [ S ] = \left\{ \begin{array}{l l}. 9 4 \sigma & \text { when } n = 5 \\ . 9 7 \sigma & \text { when } n = 9 \end{array} \right.
$$

Since 

$$
z _ {. 0 2 5} = 1. 9 6, \quad t _ {. 0 2 5, 4} = 2. 7 8, \quad t _ {. 0 2 5, 8} = 2. 3 1
$$

the length of a 95 percent confidence interval from a sample of size 5 is $2 \times 1 . 9 6 \sigma / \sqrt { 5 } ~ = ~ 1 . 7 5 \sigma$ when$\sigma$ is known, whereas its expected length is $2 \times 2 . 7 8 \times . 9 4 \sigma / \sqrt { 5 } = 2 . 3 4 \sigma$ when σ is unknown — an increase of 33.7 percent. If the sample is of size 9, then the two values to compare are 1.31σ and 1.49σ — a gain of 13.7 percent. ■ 

A one-sided upper confidence interval can be obtained by noting that 

$$
P \left\{\sqrt {n} \frac {(\overline {{X}} - \mu)}{S} <   t _ {\alpha , n - 1} \right\} = 1 - \alpha
$$

## 7.3 Interval Estimates

or 

$$
P \left\{\overline {{{X}}} - \mu <   \frac {S}{\sqrt {n}} t _ {\alpha , n - 1} \right\} = 1 - \alpha
$$

or 

$$
P \left\{\mu > \overline {{{X}}} - \frac {S}{\sqrt {n}} t _ {\alpha , n - 1} \right\} = 1 - \alpha
$$

Hence, if it is observed that ${ \overline { { X } } } = { \overline { { x } } } , S = s .$ , then we can assert “with $1 0 0 ( 1 - \alpha )$ percent confidence” that 

$$
\mu \in \left(\overline {{x}} - \frac {s}{\sqrt {n}} t _ {\alpha , n - 1}, \infty\right)
$$

Similarly, a 100(1 − α) lower confidence interval would be 

$$
\mu \in \left(- \infty , \overline {{x}} + \frac {s}{\sqrt {n}} t _ {\alpha , n - 1}\right)
$$

Program 7.3.1 will compute both one- and two-sided confidence intervals for the mean of a normal distribution when the variance is unknown. 

EXAMPLE 7.3f Determine a 95 percent confidence interval for the average resting pulse of the members of a health club if a random selection of 15 members of the club yielded the data 54, 63, 58, 72, 49, 92, 70, 73, 69, 104, 48, 66, 80, 64, 77. Also determine a 95 percent lower confidence interval for this mean. 

SOLUTION We use Program 7.3.1 to obtain the solution (see Figure 7.3). ■ 

Our derivations of the $1 0 0 ( 1 - \alpha )$ percent confidence intervals for the population mean$\mu$ have assumed that the population distribution is normal. However, even when this is not the case, if the sample size is reasonably large then the intervals obtained will still be approximate $1 0 0 ( 1 - \alpha )$ percent confidence intervals for$\mu .$ . This is true because, by the central limit theorem,${ \sqrt { n } } ( { \overline { { X } } } - \mu ) / \sigma$ will have approximately a normal distribution, and ${ \sqrt { n } } ( { \overline { { X } } } - \mu ) / S$ will have approximately a t -distribution. 

EXAMPLE 7.3g Simulation provides a powerful method for evaluating single and multi dimensional integrals. For instance, let f be a function of an r-valued vector $( y _ { 1 } , \ldots , y _ { r } )$ and suppose that we want to estimate the quantity$\theta ,$ , defined by 

$$
\theta = \int_ {0} ^ {1} \int_ {0} ^ {1} \dots \int_ {0} ^ {1} f (y _ {1}, y _ {2}, \dots , y _ {r}) d y _ {1} d y _ {2}, \dots , d y _ {r}
$$

To accomplish this, note that if $U _ { 1 } , U _ { 2 } , \dots , U _ { r }$ are independent uniform random variables on (0, 1), then 

$$
\theta = E [ f (U _ {1}, U _ {2}, \ldots , U _ {r}) ]
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/199331431905f0889ac6745bd09a217666c0093f6cfe9c86defa711563ab367c.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/3a1de4eb-4f0d-4d87-8734-d2eb432d165a/b53c0c4f29a4a895fa08e095253c57e87b5f7e93b5f6da414d075ebbbc315fd7.jpg)



(b)



FIGURE 7.3 (a) Two-sided and (b) lower 95 percent confidence intervals for Example 7.3f.


Now, the values of independent uniform (0, 1) random variables can be approximated on a computer (by so-called pseudo random numbers); if we generate a vector of r of them, and evaluate f at this vector, then the value obtained, call it $X _ { 1 }$ , will be a random variable with mean θ . If we now repeat this process, then we obtain another value, call it $X _ { 2 }$ which will have the same distribution as $X _ { 1 }$ . Continuing on, we can generate a sequence $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ of independent and identically distributed random variables with mean$\theta ;$ we then use their observed values to estimate$\theta .$ . This method of approximating integral is called Monte Carlo simulation. 

For instance, suppose we wanted to estimate the one-dimensional integra 

$$
\theta = \int_ {0} ^ {1} \sqrt {1 - y ^ {2}} d y = E [ \sqrt {1 - U ^ {2}} ]
$$

where $U$ is a uniform (0, 1) random variable. To do so, let $U _ { 1 } , \ldots , U _ { 1 0 0 }$ be independent uniform (0, 1) random variables, and set 

$$
X _ {i} = \sqrt {1 - U _ {i} ^ {2}}, \qquad i = 1, \ldots , 1 0 0
$$

In this way, we have generated a sample of 100 random variables having mean θ. Suppose that the computer generated values of $U _ { 1 } , \ldots , U _ { 1 0 0 }$ , resulting in $X _ { 1 } , \ldots , X _ { 1 0 0 }$ having sample mean .786 and sample standard deviation .03. Consequently, since $t _ { . 0 2 5 , 9 9 } ~ =$ 1.985, it follows that a 95 percent confidence interval for$\theta$ would be given by 

$$
. 7 8 6 \pm 1. 9 8 5 (. 0 0 3)
$$

As a result, we could assert, with 95 percent confidence, that$\theta$ (which can be shown to equal$\pi / 4 )$ is between .780 and .792. ■ 

## 7.3.2 Confidence Intervals for the Variance of a Normal Distribution

$\operatorname { I f } X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal distribution having unknown parameters$\mu$ and$\sigma ^ { 2 }$ , then we can construct a confidence interval for$\sigma ^ { 2 }$ by using the fact that 

$$
(n - 1) \frac {S ^ {2}}{\sigma^ {2}} \sim \chi_ {n - 1} ^ {2}
$$

Hence, 

$$
P \left\{\chi_ {1 - \alpha / 2, n - 1} ^ {2} \leq (n - 1) \frac {S ^ {2}}{\sigma^ {2}} \leq \chi_ {\alpha / 2, n - 1} ^ {2} \right\} = 1 - \alpha
$$

or, equivalently, 

$$
P \left\{\frac {(n - 1) S ^ {2}}{\chi_ {\alpha / 2 , n - 1} ^ {2}} \leq \sigma^ {2} \leq \frac {(n - 1) S ^ {2}}{\chi_ {1 - \alpha / 2 , n - 1} ^ {2}} \right\} = 1 - \alpha
$$

Hence when $S ^ { 2 } = s ^ { 2 } , \mathrm { ~ a ~ } 1 0 0 ( 1 - \alpha )$ percent confidence interval for$\sigma ^ { 2 }$ is 

$$
\left\{\frac {(n - 1) s ^ {2}}{\chi_ {\alpha / 2 , n - 1} ^ {2}}, \frac {(n - 1) s ^ {2}}{\chi_ {1 - \alpha / 2 , n - 1} ^ {2}} \right\}
$$

EXAMPLE 7.3h A standardized procedure is expected to produce washers with very small deviation in their thicknesses. Suppose that 10 such washers were chosen and measured. If the thicknesses of these washers were, in inches, 

<table><tr><td>.123</td><td>.133</td></tr><tr><td>.124</td><td>.125</td></tr><tr><td>.126</td><td>.128</td></tr><tr><td>.120</td><td>.124</td></tr><tr><td>.130</td><td>.126</td></tr></table>

what is a 90 percent confidence interval for the standard deviation of the thickness of a washer produced by this procedure? 

SOLUTION A computation gives that 

$$
S ^ {2} = 1. 3 6 6 \times 1 0 ^ {- 5}
$$

Because$\chi _ { . 0 5 , 9 } ^ { 2 } = 1 6 . 9 1 7$ and$\chi _ { . 9 5 , 9 } ^ { 2 } = 3 . 3 3 4$ , and because 

$$
\frac {9 \times 1 . 3 6 6 \times 1 0 ^ {- 5}}{1 6 . 9 1 7} = 7. 2 6 7 \times 1 0 ^ {- 6}, \quad \frac {9 \times 1 . 3 6 6 \times 1 0 ^ {- 5}}{3 . 3 3 4} = 3 6. 8 7 5 \times 1 0 ^ {- 6}
$$

TABLE 7.1 100(1 − α) Percent Confidence Intervals 

$$
X _ {1}, \ldots , X _ {n} \sim \mathcal {N} (\mu , \sigma^ {2})
$$

$$
\overline {{X}} = \sum_ {i = 1} ^ {n} X _ {i} / n, \qquad S = \sqrt {\sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2} / (n - 1)}
$$

<table><tr><td>Assumption</td><td>Parameter</td><td>Confidence Interval</td><td>Lower Interval</td><td>Upper Interval</td></tr><tr><td><eq>\sigma^2</eq> known</td><td><eq>\mu</eq></td><td><eq>\overline{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}</eq></td><td><eq>\left(-\infty, \overline{X} + z_\alpha \frac{\sigma}{\sqrt{n}}\right)</eq></td><td><eq>\left(\overline{X} + z_\alpha \frac{\sigma}{\sqrt{n}}, \infty\right)</eq></td></tr><tr><td><eq>\sigma^2</eq> unknown</td><td><eq>\mu</eq></td><td><eq>\overline{X} \pm t_{\alpha/2,n-1} \frac{S}{\sqrt{n}}</eq></td><td><eq>\left(-\infty, \overline{X} + t_{\alpha,n-1} \frac{S}{\sqrt{n}}\right)</eq></td><td><eq>\left(\overline{X} - t_{\alpha,n-1} \frac{S}{\sqrt{n}}, \infty\right)</eq></td></tr><tr><td><eq>\mu</eq> unknown</td><td><eq>\sigma^2</eq></td><td><eq>\left(\frac{(n-1)S^2}{\chi_{\alpha/2,n-1}^2}, \frac{(n-1)S^2}{\chi_{1-\alpha/2,n-1}^2}\right)</eq></td><td><eq>\left(0, \frac{(n-1)S^2}{\chi_{1-\alpha,n-1}^2}\right)</eq></td><td><eq>\left(\frac{(n-1)S^2}{\chi_{\alpha,n-1}^2}, \infty\right)</eq></td></tr></table>

it follows that, with confidence .90, 

$$
\sigma^ {2} \in (7. 2 6 7 \times 1 0 ^ {- 6}, \quad 3 6. 8 7 5 \times 1 0 ^ {- 6})
$$

Taking square roots yields that, with confidence .90, 

$$
\sigma \in (2. 6 9 6 \times 1 0 ^ {- 3}, \quad 6. 0 7 2 \times 1 0 ^ {- 3})
$$

One-sided confidence intervals for$\sigma ^ { 2 }$ are obtained by similar reasoning and are presented in Table 7.1, which sums up the results of this section. 

## 7.4 ESTIMATING THE DIFFERENCE IN MEANS OF TWO NORMAL POPULATIONS

Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ be a sample of size n from a normal population having mean$\mu _ { 1 }$ and variance$\sigma _ { 1 } ^ { 2 }$ and let $Y _ { 1 } , \dots , Y _ { m }$ be a sample of size m from a different normal population having mean$\mu _ { 2 }$ and variance$\sigma _ { 2 } ^ { 2 }$ and suppose that the two samples are independent of each other. We are interested in estimating$\mu _ { 1 } - \mu _ { 2 }$ 

Since$\textstyle { \overline { { X } } } = \sum _ { i = 1 } ^ { n } X _ { i } / n$ and ${ \overline { { Y } } } = \textstyle \sum _ { i = 1 } ^ { m }$ Y /m are the maximum likelihood estimators of$\mu _ { 1 }$ and$\mu _ { 2 }$ it seems intuitive (and can be proven) that ${ \overline { { X } } } - { \overline { { Y } } }$ is the maximum likelihood estimator of$\mu _ { 1 } - \mu _ { 2 }$ 

To obtain a confidence interval estimator, we need the distribution of ${ \overline { { X } } } - { \overline { { Y } } }$ . Because 

$$
\begin{array}{l} \overline {{X}} \sim \mathcal {N} (\mu_ {1}, \sigma_ {1} ^ {2} / n) \\ \overline {{Y}} \sim \mathcal {N} (\mu_ {2}, \sigma_ {2} ^ {2} / m) \end{array}
$$

it follows from the fact that the sum of independent normal random variables is also normal, that 

$$
\overline {{X}} - \overline {{Y}} \sim \mathcal {N} \left(\mu_ {1} - \mu_ {2}, \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}\right)
$$

Hence, assuming$\sigma _ { 1 } ^ { 2 }$ and$\sigma _ { 2 } ^ { 2 }$ are known, we have that 

$$
\frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}}} \sim \mathcal {N} (0, 1)\tag{7.4.1}
$$

and so 

$$
P \left\{- z _ {\alpha / 2} <   \frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}}} <   z _ {\alpha / 2} \right\} = 1 - \alpha
$$

or, equivalently, 

$$
P \left\{\overline {{X}} - \overline {{Y}} - z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}} <   \mu_ {1} - \mu_ {2} <   \overline {{X}} - \overline {{Y}} + z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}} \right\} = 1 - \alpha
$$

Hence, if X and$\overline { { Y } }$ are observed to equal x and y, respectively, then a 100(1 − α) twosided confidence interval estimate for$\mu _ { 1 } - \mu _ { 2 }$ is 

$$
\mu_ {1} - \mu_ {2} \in \left(\bar {x} - \bar {y} - z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}}, \bar {x} - \bar {y} + z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}}\right)
$$

One-sided confidence intervals for$\mu _ { 1 } - \mu _ { 2 }$ are obtained in a similar fashion, and we leave it for the reader to verify that a $1 0 0 ( 1 - \alpha )$ percent one-sided interval is given by 

$$
\mu_ {1} - \mu_ {2} \in \left(- \infty , \overline {{x}} - \overline {{y}} + z _ {\alpha} \sqrt {\sigma_ {1} ^ {2} / n + \sigma_ {2} ^ {2} / m}\right)
$$

Program 7.4.1 will compute both one- and two-sided confidence intervals for$\mu _ { 1 } - \mu _ { 2 }$ 

EXAMPLE 7.4a Two different types of electrical cable insulation have recently been tested to determine the voltage level at which failures tend to occur. When specimens were subjected to an increasing voltage stress in a laboratory experiment, failures for the two types of cable insulation occurred at the following voltages: 

<table><tr><td colspan="2">Type A</td><td colspan="2">Type B</td></tr><tr><td>36</td><td>54</td><td>52</td><td>60</td></tr><tr><td>44</td><td>52</td><td>64</td><td>44</td></tr><tr><td>41</td><td>37</td><td>38</td><td>48</td></tr><tr><td>53</td><td>51</td><td>68</td><td>46</td></tr><tr><td>38</td><td>44</td><td>66</td><td>70</td></tr><tr><td>36</td><td>35</td><td>52</td><td>62</td></tr><tr><td>34</td><td>44</td><td></td><td></td></tr></table>

Suppose that it is known that the amount of voltage that cables having type A insulation can withstand is normally distributed with unknown mean$\mu _ { A }$ and known variance$\sigma _ { A } ^ { 2 } = 4 0$ , whereas the corresponding distribution for type B insulation is normal with unknown mean$\mu _ { B }$ and known variance$\sigma _ { B } ^ { 2 } = 1 0 0$ . Determine a 95 percent confidence interval for$\mu _ { A } - \mu _ { B }$ . Determine a value that we can assert, with 95 percent confidence, exceed$\mu _ { A } - \mu _ { B } .$ 

SOLUTION We run Program 7.4.1 to obtain the solution (see Figure 7.4). ■ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/463ab9c9ffd514c83d2b0b50c0c2b3a4acdcae1ed1d454f5477461000087e40b.jpg)



(a)



FIGURE 7.4 (a) Two-sided and (b) lower 95 percent confidence intervals for Example 7.4a.


Let us suppose now that we again desire an interval estimator of$\mu _ { 1 } - \mu _ { 2 }$ but that the population variances$\sigma _ { 1 } ^ { 2 }$ and$\sigma _ { 2 } ^ { 2 }$ are unknown. In this case, it is natural to try to replace$\bar { \sigma } _ { 1 } ^ { 2 }$ and$\sigma _ { 2 } ^ { 2 }$ in Equation 7.4.1 by the sample variance 

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

However, to utilize the foregoing to obtain a confidence interval, we need its distribution and it must not depend on any of the unknown parameters$\sigma _ { 1 } ^ { 2 }$ and$\sigma _ { 2 } ^ { 2 }$ . Unfortunately, this distribution is both complicated and does indeed depend on the unknown parameters$\sigma _ { 1 } ^ { 2 }$ and$\sigma _ { 2 } ^ { 2 }$ . In fact, it is only in the special case when$\sigma _ { 1 } ^ { \dot { 2 } } = \sigma _ { 2 } ^ { 2 }$ that we will be able to obtain an interval estimator. So let us suppose that the population variances, though unknown, are equal and let$\sigma ^ { 2 }$ denote their common value. Now, from Theorem 6.5.1 it follows that 

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

Now it follows from the fundamental result that in normal sampling$\overline { { X } }$ and $S ^ { 2 }$ are independent (Theorem 6.5.1), that$\overline { { X } } _ { 1 } , S _ { 1 } ^ { 2 } , \overline { { X } } _ { 2 } , S _ { 2 } ^ { 2 }$ are independent random variables. Hence, using the definition of a t-random variable (as the ratio of two independent random vari ables, the numerator being a standard normal and the denominator being the square root of a chi-square random variable divided by its degree of freedom parameter), it follows from Equations 7.4.2 and 7.4.3 that if we let 

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

Therefore, when the data result in the values$\overline { { { X } } } = \overline { { { x } } } , \overline { { { Y } } } = \overline { { { y } } } , S _ { \phi } = s _ { p } ,$ , we obtain the following $1 0 0 ( 1 - \alpha )$ percent confidence interval for$\mu _ { 1 } - \mu _ { 2 } { \mathrm { : } }$ 

$$
\left(\overline {{x}} - \overline {{y}} - t _ {\alpha / 2, n + m - 2} s _ {p} \sqrt {1 / n + 1 / m}, \quad \overline {{x}} - \overline {{y}} + t _ {\alpha / 2, n + m - 2} s _ {p} \sqrt {1 / n + 1 / m}\right)\tag{7.4.4}
$$

One-sided confidence intervals are similarly obtained. 

Program 7.4.2 can be used to obtain both one- and two-sided confidence intervals for the difference in means in two normal populations having unknown but equal variances. 

EXAMPLE 7.4b There are two different techniques a given manufacturer can employ to produce batteries. A random selection of 12 batteries produced by technique I and of 14 produced by technique II resulted in the following capacities (in ampere hours): 

<table><tr><td colspan="2">Technique I</td><td colspan="2">Technique II</td></tr><tr><td>140</td><td>132</td><td>144</td><td>134</td></tr><tr><td>136</td><td>142</td><td>132</td><td>130</td></tr><tr><td>138</td><td>150</td><td>136</td><td>146</td></tr><tr><td>150</td><td>154</td><td>140</td><td>128</td></tr><tr><td>152</td><td>136</td><td>128</td><td>131</td></tr><tr><td>144</td><td>142</td><td>150</td><td>137</td></tr><tr><td></td><td></td><td>130</td><td>135</td></tr></table>

Determine a 90 percent level two-sided confidence interval for the difference in means, assuming a common variance. Also determine a 95 percent upper confidence interval for$\mu _ { \mathrm { I } } - \mu _ { \mathrm { I I } }$ 

SOLUTION We run Program 7.4.2 to obtain the solution (see Figure 7.5). ■ 

## REMARK

The confidence interval given by Equation 7.4.4 was obtained under the assumption that the population variances are equal; with$\sigma ^ { 2 }$ as their common value, it follows that 

$$
\frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sqrt {\sigma^ {2} / n + \sigma^ {2} / m}} = \frac {\overline {{X}} - \overline {{Y}} - (\mu_ {1} - \mu_ {2})}{\sigma \sqrt {1 / n + 1 / m}}
$$

has a standard normal distribution. However, since$\sigma ^ { 2 }$ is unknown this result cannot be immediately applied to obtain a confidence interval;$\sigma ^ { 2 }$ must first be estimated. To do so, note that both sample variances are estimators of$\cdot \sigma ^ { 2 }$ ; moreover, since $S _ { 1 } ^ { 2 }$ has $n - 1$ degrees of freedom and $S _ { 2 } ^ { 2 }$ has $m - 1$ , the appropriate estimator is to take a weighted average of the two sample variances, with the weights proportional to these degrees of freedom. That is, 

the estimator of$\sigma ^ { 2 }$ is the pooled estimator 

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

TABLE 7.2 $1 0 0 ( 1 - \sigma )$ Percent Confidence Intervals for$\mu _ { 1 } - \mu _ { 2 }$ 

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

Note: Upper confidence intervals for$\mu _ { 1 } - \mu _ { 2 }$ are obtained from lower confidence intervals fo$\mu _ { 2 } - \mu _ { 1 }$ 

the normal approximation to the binomial that X is approximately normally distributed with mean np and variance $n p ( 1 - p )$ . Hence, 

$$
\frac {X - n p}{\sqrt {n p (1 - p)}} \dot {\sim} \mathcal {N} (0, 1)\tag{7.5.1}
$$

where$\dot { \sim }$ means “is approximately distributed as.” Therefore, for any$\alpha \in ( 0 , 1 )$ ), 

$$
P \left\{- z _ {\alpha / 2} <   \frac {X - n p}{\sqrt {n p (1 - p)}} <   z _ {\alpha / 2} \right\} \approx 1 - \alpha
$$

and so if X is observed to equal $x ,$ then an approximate $1 0 0 ( 1 - \alpha )$ percent confidence region for$\boldsymbol { \mathscr { P } }$ is 

$$
\left\{p: - z _ {\alpha / 2} <   \frac {x - n p}{\sqrt {n p (1 - p)}} <   z _ {\alpha / 2} \right\}
$$

The foregoing region, however, is not an interval. To obtain a confidence interval for ${ \boldsymbol { p } } ,$ let ${ \hat { p } } = X / n$ be the fraction of the items that meet the standards. From Example 7.2a,$\hat { \boldsymbol { p } }$ is the maximum likelihood estimator of ${ \boldsymbol { p } } ,$ , and so should be approximately equal to$\scriptstyle { \boldsymbol { p } } .$ . As a result,$\sqrt { n \hat { p } ( 1 - \hat { p } ) }$ will be approximately equal to$\sqrt { n p ( 1 - p ) }$ and so from Equation 7.5.1 we see that 

$$
\frac {X - n p}{\sqrt {n \hat {p} (1 - \hat {p})}} \dot {\sim} \mathcal {N} (0, 1)
$$

Hence, for any$\alpha \in ( 0 , 1 )$ we have that 

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

which yields an approximate $1 0 0 ( 1 - \alpha )$ percent confidence interval for$\boldsymbol { \underline b }$ 

EXAMPLE 7.5a A sample of 100 transistors is randomly chosen from a large batch and tested to determine if they meet the current standards. If 80 of them meet the standards, then an approximate 95 percent confidence interval for$\scriptstyle { \dot { \boldsymbol { p } } } ,$ , the fraction of all the transistors that meet the standards, is given by 

$$
(. 8 - 1. 9 6 \sqrt {. 8 (. 2) / 1 0 0},. 8 + 1. 9 6 \sqrt {. 8 (. 2) / 1 0 0}) = (. 7 2 1 6,. 8 7 8 4)
$$

That is, with $^ { \mathfrak { a } } 9 5$ percent confidence,” between 72.16 and 87.84 percent of all transistors meet the standards. ■ 

EXAMPLE 7.5b On October 14, 2003, the New York Times reported that a recent poll indicated that 52 percent of the population was in favor of the job performance of President Bush, with a margin of error of ±4 percent. What does this mean? Can we infer how many people were questioned? 

SOLUTION It has become common practice for the news media to present 95 percent confidence intervals. Since $z _ { . 0 2 5 } ~ = ~ 1 . 9 6 , \mathrm { ~ a ~ } 9 5$ percent confidence interval for ${ \boldsymbol { p } } ,$ the percentage of the population that is in favor of President Bush’s job performance, is given by 

$$
\hat {p} \pm 1. 9 6 \sqrt {\hat {p} (1 - \hat {p}) / n} = . 5 2 \pm 1. 9 6 \sqrt {. 5 2 (. 4 8) / n}
$$

where n is the size of the sample. Since the “margin of error” is$\pm 4$ percent, it follows that 

$$
1. 9 6 \sqrt {. 5 2 (. 4 8) / n} = . 0 4
$$

or 

$$
n = \frac {(1 . 9 6) ^ {2} (. 5 2) (. 4 8)}{(. 0 4) ^ {2}} = 5 9 9. 2 9
$$

That is, approximately 599 people were sampled, and 52 percent of them reported favorably on President Bush’s job performance. ■ 

We often want to specify an approximate 100(1 − α) percent confidence interval for$\boldsymbol { \mathit { p } }$ that is no greater than some given length, say b. The problem is to determine the appropriate sample size n to obtain such an interval. To do so, note that the length of the approximate $1 0 0 ( 1 - \alpha )$ percent confidence interval for$\boldsymbol { \mathit { p } }$ from a sample of size n is 

$$
2 z _ {\alpha / 2} \sqrt {\hat {p} (1 - \hat {p}) / n}
$$

which is approximately equal to $2 z _ { \alpha / 2 } \sqrt { p ( 1 - p ) / n }$ . Unfortunately,$\boldsymbol { \mathscr { P } }$ is not known in advance, and so we cannot just set $2 z _ { \alpha / 2 } \sqrt { p ( 1 - p ) / n }$ equal to $b$ to determine the necessary sample size n. What we can do, however, is to first take a preliminary sample to obtain a rough estimate o$\dot { \mathbf { \rho } } _ { p } ,$ and then use this estimate to determine $n .$ . That is, we use$\boldsymbol { p } ^ { * }$ , the proportion of the preliminary sample that meets the standards, as a preliminary estimate of ${ \dot { p } } ;$ we then determine the total sample size n by solving the equation 

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

EXAMPLE 7.5c A certain manufacturer produces computer chips; each chip is independently acceptable with some unknown probability$\cdot \mathbf { \nabla } { \hat { P } } \cdot$ . To obtain an approximate 99 percent confidence interval for ${ \boldsymbol { p } } ,$ whose length is approximately .05, an initial sample of 30 chips has been taken. If 26 of these chips are of acceptable quality, then the prelimi nary estimate of$\dot { \boldsymbol { p } }$ is 26/30. Using this value, a 99 percent confidence interval of length approximately .05 would require an approximate sample of size 

$$
n = \frac {4 (z _ {. 0 0 5}) ^ {2}}{(. 0 5) ^ {2}} \frac {2 6}{3 0} \left(1 - \frac {2 6}{3 0}\right) = \frac {4 (2 . 5 8) ^ {2}}{(. 0 5) ^ {2}} \frac {2 6}{3 0} \frac {4}{3 0} = 1, 2 3 1
$$

Hence, we should now sample an additional 1,201 chips and if, for instance, 1,040 of them are acceptable, then the final 99 percent confidence interval for$\boldsymbol { \underline { P } }$ is 

$$
\left(\frac {1 , 0 6 6}{1 , 2 3 1} - \sqrt {1 , 0 6 6 \left(1 - \frac {1 , 0 6 6}{1 , 2 3 1}\right)} \frac {z _ {. 0 0 5}}{1 , 2 3 1}, \frac {1 , 0 6 6}{1 , 2 3 1} + \sqrt {1 , 0 6 6 \left(1 - \frac {1 , 0 6 6}{1 , 2 3 1}\right) \frac {z _ {. 0 0 5}}{1 , 2 3 1}}\right)
$$

or 

$$
p \in (. 8 4 0 9 1,. 8 9 1 0 1)
$$

REMARK 

As shown, a 100(1 − α) percent confidence interval for$\boldsymbol { \mathscr { P } }$ will be of approximate length b when the sample size is 

$$
n = \frac {(2 z _ {\alpha / 2}) ^ {2}}{b ^ {2}} p (1 - p)
$$

Now it is easily shown that the function $g ( \boldsymbol { p } ) = p ( 1 - \boldsymbol { p } )$ attains its maximum value of$\frac { 1 } { 4 }$ , in the interval $0 \leq  { p } \leq 1$ , when$\textstyle { p = { \frac { 1 } { 2 } } }$ . Thus an upper bound on n is 

$$
n \leq \frac {(z _ {\alpha / 2}) ^ {2}}{b ^ {2}}
$$

and so by choosing a sample whose size is at least as large as $( z _ { \alpha / 2 } ) ^ { 2 } / b ^ { 2 }$ , one can be assured of obtaining a confidence interval of length no greater than $b$ without need of any additional sampling. ■ 

One-sided approximate confidence intervals for$\boldsymbol { \mathscr { P } }$ are also easily obtained; Table 7.3 gives the results. 


TABLE 7.3 Approximate 100(1 − α) Percent Confidence Intervals for p



X Is a Binomial $( n , p )$ Random Variable ${ \hat { p } } = X / n$


<table><tr><td>Type of Interval</td><td>Confidence Interval</td></tr><tr><td>Two-sided</td><td><eq>\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}</eq></td></tr><tr><td>One-sided lower</td><td><eq>(-\infty, \hat{p} + z_{\alpha}\sqrt{\hat{p}(1-\hat{p})/n})</eq></td></tr><tr><td>One-sided upper</td><td><eq>(\hat{p} - z_{\alpha}\sqrt{\hat{p}(1-\hat{p})/n}, \infty)</eq></td></tr></table>

## *7.6 CONFIDENCE INTERVAL OF THE MEAN OF THE EXPONENTIAL DISTRIBUTION

$\operatorname { I f } X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ are independent exponential random variables each having mean$\theta _ { i }$ , then it can be shown that the maximum likelihood estimator of θ is the sample mean$\textstyle \sum _ { i = 1 } ^ { n } X _ { i } / n$ To obtain a confidence interval estimator of$\theta _ { ; }$ , recall from Section $5 . 7$ that$\sum _ { i = 1 } ^ { n } X _ { i }$ has a gamma distribution with parameters $^ { n , }$ , 1/θ . This in turn implies (from the relationship between the gamma and chi-square distribution shown in Section 5.8.1.1) tha 

$$
\frac {2}{\theta} \sum_ {i = 1} ^ {n} X _ {i} \sim \chi_ {2 n} ^ {2}
$$

Hence, for any$\alpha \in ( 0 , 1 )$ 

$$
P \left\{\chi_ {1 - \alpha / 2, 2 n} ^ {2} <   \frac {2}{\theta} \sum_ {i = 1} ^ {n} X _ {i} <   \chi_ {\alpha / 2, 2 n} ^ {2} \right\} = 1 - \alpha
$$

or, equivalently, 

$$
P \left\{\frac {2 \sum_ {i = 1} ^ {n} X _ {i}}{\chi_ {\alpha / 2 , 2 n} ^ {2}} <   \theta <   \frac {2 \sum_ {i = 1} ^ {n} X _ {i}}{\chi_ {1 - \alpha / 2 , 2 n} ^ {2}} \right\} = 1 - \alpha
$$

Hence, a 100(1 − α) percent confidence interval for$\theta$ is 

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

Let$\mathbf { X } = ( X _ { 1 } , \ldots , X _ { n } )$ be a sample from a population whose distribution is specified up to an unknown parameter$\theta _ { i }$ , and let $d = d ( \mathbf { X } )$ be an estimator of θ . How are we to determine its worth as an estimator of θ ? One way is to consider the square of the difference between $d ( \mathbf { X } )$ and$\theta .$ . However, since $( d ( \mathbf { X } ) - \theta ) ^ { 2 }$ is a random variable, let us agree to consider $r ( d , \theta )$ , the mean square error of the estimator $d ,$ , which is defined by 

$$
r (d, \theta) = E [ (d (\mathbf {X}) - \theta) ^ {2} ]
$$

as an indication of the worth of $d$ as an estimator of$\theta$ . 

It would be nice if there were a single estimator d that minimized $r ( d , \theta )$ for all possible values of$\mathbf { \nabla } \cdot \theta .$ . However, except in trivial situations, this will never be the case. For example, consider the estimator $d ^ { * }$ defined by 

$$
d ^ {*} (X _ {1}, \ldots , X _ {n}) = 4
$$

That is, no matter what the outcome of the sample data, the estimator $d ^ { * }$ chooses 4 as its estimate of θ . While this seems like a silly estimator (since it makes no use of the data), it is, however, true that when$\theta$ actually equals $^ { 4 , }$ , the mean square error of this estimator is 0. Thus, the mean square error of any estimator different than $d ^ { * }$ must, in most situations, be larger than the mean square error of $d ^ { * }$ when$\theta = 4$ 

Although minimum mean square estimators rarely exist, it is sometimes possible to find an estimator having the smallest mean square error among all estimators that satisfy a certain property. One such property is that of unbiasedness. 

## Definition

Let $d = d ( \mathbf { X } )$ be an estimator of the parameter θ . Then 

$$
b _ {\theta} (d) = E [ d (\mathbf {X}) ] - \theta
$$

is called the bias of d as an estimator of θ . If $b _ { \theta } ( d ) = 0$ for all$\theta ,$ , then we say that d is an unbiased estimator of θ . In other words, an estimator is unbiased if its expected value always equals the value of the parameter it is attempting to estimate. 

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

More generally,$\begin{array} { r } { d _ { 3 } ( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } ) = \sum _ { i = 1 } ^ { n } \lambda _ { i } X _ { i } } \end{array}$ is an unbiased estimator of θ whenever$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \lambda _ { i } = 1 } \end{array}$ . This follows since 

$$
\begin{array}{r l} E \left[ \sum_ {i = 1} ^ {n} \lambda_ {i} X _ {i} \right] & = \sum_ {i = 1} ^ {n} E [ \lambda_ {i} X _ {i} ] \\ & = \sum_ {i = 1} ^ {n} \lambda_ {i} E (X _ {i}) \\ & = \theta \sum_ {i = 1} ^ {n} \lambda_ {i} \\ & = \theta \quad \blacksquare \end{array}
$$

$\operatorname { I f } d ( X _ { 1 } , \ldots , X _ { n } )$ is an unbiased estimator, then its mean square error is given by 

$$
\begin{array}{r l} r (d, \theta) & = E [ (d (\mathbf {X}) - \theta) ^ {2} ] \\ & = E [ (d (\mathbf {X}) - E [ d (\mathbf {X}) ]) ^ {2} ] \qquad \text { since } d \text { is unbiased } \\ & = \operatorname{Var} (d (\mathbf {X})) \end{array}
$$

Thus the mean square error of an unbiased estimator is equal to its variance. 

EXAMPLE 7.7b Combining Independent Unbiased Estimators. Let $d _ { 1 }$ and $d _ { 2 }$ denote inde pendent unbiased estimators of$\theta _ { ; }$ , having known variances$\sigma _ { 1 } ^ { 2 }$ and$\sigma _ { 2 } ^ { 2 }$ . That is, for $i = 1 , 2$ , 

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

To determine the value of$\lambda$ that minimizes $r ( d , \theta ) - \mathrm { c a l l }$ it$\hat { \lambda } -$ set this equal to 0 and solve for λ to obtain 

$$
2 \hat {\lambda} \sigma_ {1} ^ {2} = 2 (1 - \hat {\lambda}) \sigma_ {2} ^ {2}
$$

or 

$$
\hat {\lambda} = \frac {\sigma_ {2} ^ {2}}{\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}} = \frac {1 / \sigma_ {1} ^ {2}}{1 / \sigma_ {1} ^ {2} + 1 / \sigma_ {2} ^ {2}}
$$

In words, the optimal weight to give an estimator is inversely proportional to its variance (when all the estimators are unbiased and independent). 

For an application of the foregoing, suppose that a conservation organization wants to determine the acidity content of a certain lake. To determine this quantity, they draw some water from the lake and then send samples of this water to n different laboratories. These laboratories will then, independently, test for acidity content by using their respective titration equipment, which is of differing precision. Specifically, suppose that $d _ { i } ,$ , the result of a titration test at laboratory $i ,$ is a random variable having mean$\theta _ { ; }$ , the true acidity of the sample water, and variance$\sigma _ { i } ^ { 2 } , i = 1 , \ldots , n .$ . If the quantities$\sigma _ { i } ^ { 2 } , i = 1 , . . . , n$ are known to the conservation organization, then they should estimate the acidity of the sampled water from the lake by 

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

A second possible estimator of$\cdot _ { \theta }$ is the maximum likelihood estimator, which, as shown in Example 7.2d, is given by 

$$
d _ {2} = d _ {2} (\mathbf {X}) = \max _ {i} X _ {i}
$$

To compute the mean square error of $d _ { 2 }$ as an estimator of$\theta ,$ , we need to first compute its mean (so as to determine its bias) and variance. To do so, note that the distribution function of $d _ { 2 }$ is as follows: 

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

it follows that $d _ { 2 }$ is a more superior estimator of$\cdot _ { \theta }$ than is $d _ { 1 }$ . 

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

A comparison with Equation 7.7.3 shows that the (biased) estimator $( n \mathrm { ~ + ~ } 2 ) /$$( n + 1 ) \operatorname* { m a x } _ { i } X _ { i }$ has about half the mean square error of the maximum likelihood estimator max $X _ { i }$ . ■ 

## *7.8 THE BAYES ESTIMATOR

In certain situations it seems reasonable to regard an unknown parameter θ as being the value of a random variable from a given probability distribution. This usually arises when, prior to the observance of the outcomes of the data $X _ { 1 } , \dots , X _ { n }$ , we have some information about the value of θ and this information is expressible in terms of a probability distribution (called appropriately the prior distribution of θ ). For instance, suppose that from past experience we know that θ is equally likely to be near any value in the interval (0, 1). Hence, we could reasonably assume that θ is chosen from a uniform distribution on (0, 1). 

Suppose now that our prior feelings about$\theta$ are that it can be regarded as being the value of a continuous random variable having probability density function ${ \boldsymbol { p } } ( { \boldsymbol { \theta } } )$ ; and suppose that we are about to observe the value of a sample whose distribution depends on θ . Specifically, suppose that $f ( x | \theta )$ represents the likelihood — that is, it is the probability mass function in the discrete case or the probability density function in the continuous case — that a data value is equal to x when θ is the value of the parameter. If the observed data values are $X _ { i } = x _ { i } , i = 1 , \ldots , n ,$ , then the updated, or conditional, probability density function of θ is as follows: 

$$
\begin{array}{c} f (\theta | x _ {1}, \ldots , x _ {n}) = \frac {f (\theta , x _ {1} , \ldots , x _ {n})}{f (x _ {1} , \ldots , x _ {n})} \\ = \frac {p (\theta) f (x _ {1} , \ldots , x _ {n} | \theta)}{\int f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta) d \theta} \end{array}
$$

The conditional density function $f ( \theta | x _ { 1 } , \ldots , x _ { n } )$ is called the posterior density function. (Thus, before observing the data, one’s feelings about$\theta$ are expressed in terms of the prior distribution, whereas once the data are observed, this prior distribution is updated to yield the posterior distribution.) 

Now we have shown that whenever we are given the probability distribution of a random variable, the best estimate of the value of that random variable, in the sense of minimizing the expected squared error, is its mean. Therefore, it follows that the best estimate of θ, given the data values $X _ { i } = x _ { i } , i = 1 , \ldots , n ,$ is the mean of the posterior distribution $f ( \theta | x _ { 1 } , \ldots , x _ { n } )$ . This estimator, called the Bayes estimator, is written as $E [ \theta | X _ { 1 } , \ldots , X _ { n } ]$ That is,$\mathrm { i f } X _ { i } = x _ { i } , i = 1 , . . . , n$ , then the value of the Bayes estimator is 

$$
E [ \theta | X _ {1} = x _ {1}, \ldots , X _ {n} = x _ {n} ] = \int \theta f (\theta | x _ {1}, \ldots , x _ {n}) d \theta
$$

EXAMPLE 7.8a Suppose that $X _ { 1 } , \ldots , X _ { n }$ are independent Bernoulli random variables, each having probability mass function given by 

$$
f (x | \theta) = \theta^ {x} (1 - \theta) ^ {1 - x}, \qquad x = 0, 1
$$

where$\theta$ is unknown. Further, suppose that$\theta$ is chosen from a uniform distribution on (0, 1). Compute the Bayes estimator of θ . 

SOLUTION We must compute $E [ \theta | X _ { 1 } , \ldots , X _ { n } ]$ . Since the prior density of$\cdot _ { \theta }$ is the uniform density 

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

As an illustration, if 10 independent trials, each of which results in a success with probability$\theta ,$ result in $^ 6$ successes, then assuming a uniform (0, 1) prior distribution on$\theta ,$ , the Bayes estimator of$\theta$ is 7/12 (as opposed, for instance, to the maximum likelihood estimator of 6/10). ■ 

## REMARK

The conditional distribution of θ given that $X _ { i } = x _ { i } , i = 1 , \dots , n$ , whose density function is given by Equation 7.8.2, is called the beta distribution with parameters$\textstyle \sum _ { i = 1 } ^ { n } x _ { i } + 1$$\textstyle n - \sum _ { i = 1 } ^ { n } x _ { i } + 1$ ■ 

EXAMPLE 7.8b Suppose $X _ { 1 } , \ldots , X _ { n }$ are independent normal random variables, each having unknown mean$\theta$ and known variance$\sigma _ { 0 } ^ { 2 }$ . If θ is itself selected from a normal population having known mean$\mu$ and known variance$\sigma ^ { 2 }$ , what is the Bayes estimator of θ ? 

SOLUTION In order to determine $E [ \theta | X _ { 1 } , \ldots , X _ { n } ]$ , the Bayes estimator, we need first determine the conditional density of$\cdot \theta$ given the values of $X _ { 1 } , \ldots , X _ { n }$ . Now 

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

Writing the Bayes estimator as we did in Equation 7.8.3 is informative, for it shows that it is a weighted average of X , the sample mean, and$\mu _ { ; }$ , the a priori mean. In fact, the weights given to these two quantities are in proportion to the inverses of$\sigma _ { 0 } ^ { 2 } / n$ (the conditional variance of the sample mean$\overline { { X } }$ given θ) and$\sigma ^ { 2 }$ (the variance of the prior distribution). ■ 

## REMARK: ON CHOOSING A NORMAL PRIOR

As illustrated by Example 7.8b, it is computationally very convenient to choose a normal prior for the unknown mean θ of a normal distribution — for then the Bayes estimator is simply given by Equation 7.8.3. This raises the question of how one should go about determining whether there is a normal prior that reasonably represents one’s prior feelings about the unknown mean. 

To begin, it seems reasonable to determine the value — call it$\mu$ — that you a priori feel is most likely to be near θ . That is, we start with the mode (which equals the mean when the distribution is normal) of the prior distribution. We should then try to ascertain whether or not we believe that the prior distribution is symmetric about$\mu$ . That is, for each $a > 0$ do we believe that it is just as likely that θ will lie between$\mu - a$ and$\mu$ as it is that it will be between$\mu$ and$\mu + a ?$ If the answer is positive, then we accept, as a working hypothesis, that our prior feelings about$\theta$ can be expressed in terms of a prior distribution that is normal with mean$\mu .$ . To determine$\sigma$ , the standard deviation of the normal prior, think of an interval centered about$\mu$ that you a priori feel is 90 percent certain to contain$\theta .$ . For instance, suppose you feel 90 percent (no more and no less) certain that$\theta$ will lie between$\mu - a$ and$\mu + a$ . Then, since a normal random variable$\theta$ with mean$\mu$ and variance$\sigma ^ { 2 }$ is such that 

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

Thus, if your prior feelings can indeed be reasonably described by a normal distribution, then that distribution would have mean$\mu$ and standard deviation$\sigma = a / 1$ .645. As a test of whether this distribution indeed fits your prior feelings you might ask yourself such questions as whether you are 95 percent certain that$\theta$ will fall between$\mu - 1 . 9 6 \sigma$ and$\mu + 1 . 9 6 \sigma$ , or whether you are 99 percent certain that$\theta$ will fall between$\mu - 2 . 5 8 \sigma$ and$\mu + 2 . 5 8 \sigma$ , where these intervals are determined by the equalities 

$$
\begin{array}{l} P \left\{- 1. 9 6 <   \frac {\theta - \mu}{\sigma} <   1. 9 6 \right\} = . 9 5 \\ P \left\{- 2. 5 8 <   \frac {\theta - \mu}{\sigma} <   2. 5 8 \right\} = . 9 9 \end{array}
$$

which hold when$\theta$ is normal with mean$\mu$ and variance$\sigma ^ { 2 }$ . 

EXAMPLE 7.8c Consider the likelihood function $f ( x _ { 1 } , \dots , x _ { n } | \theta )$ and suppose that$\theta$ is uniformly distributed over some interval $( a , b )$ . The posterior density of θ given $X _ { 1 } , \ldots , X _ { n }$ equals 

$$
\begin{array}{r l} f (\theta | x _ {1}, \ldots , x _ {n}) & = \frac {f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta)}{\int_ {a} ^ {b} f (x _ {1} , \ldots , x _ {n} | \theta) p (\theta) d \theta} \\ & = \frac {f (x _ {1} , \ldots , x _ {n} | \theta)}{\int_ {a} ^ {b} f (x _ {1} , \ldots , x _ {n} | \theta) d \theta} \quad a <   \theta <   b \end{array}
$$

Now the mode of a density $f ( \theta )$ was defined to be that value of$\theta$ that maximizes $f ( \theta )$ By the foregoing, it follows that the mode of the density $f ( \theta | x _ { 1 } , \ldots , x _ { n } )$ is that value of$\overrightharpoon { \theta }$ maximizing $f ( x _ { 1 } , \ldots , x _ { n } | \theta )$ ; that is, it is just the maximum likelihood estimate of θ [when it is constrained to be in $( a , b ) ]$ ]. In other words, the maximum likelihood estimate equals the mode of the posterior distribution when a uniform prior distribution is assumed. ■ 

If, rather than a point estimate, we desire an interval in which θ lies with a specified probability — say $1 - \alpha -$ we can accomplish this by choosing values a and b such that 

$$
\int_ {a} ^ {b} f (\theta | x _ {1}, \ldots , x _ {n}) d \theta = 1 - \alpha
$$

EXAMPLE 7.8d Suppose that if a signal of value s is sent from location A, then the signal value received at location B is normally distributed with mean s and variance 60. Suppose also that the value of a signal sent at location A is, a priori, known to be normally distributed with mean 50 and variance 100. If the value received at location B is equal to 40, determine an interval that will contain the actual value sent with probability .90. 

SOLUTION It follows from Example 7.8b that the conditional distribution of S, the signa value sent, given that 40 is the value received, is normal with mean and variance given by 

$$
\begin{array}{l} E [ S | \text {data} ] = \frac {1 / 6 0}{1 / 6 0 + 1 / 1 0 0} 4 0 + \frac {1 / 1 0 0}{1 / 6 0 + 1 / 1 0 0} 5 0 = 4 3. 7 5 \\ \operatorname{Var} (S | \text {data}) = \frac {1}{1 / 6 0 + 1 / 1 0 0} = 3 7. 5 \end{array}
$$

Hence, given that the value received is 40,$( S - 4 3 . 7 5 ) / \sqrt { 3 7 . 5 }$ has a unit standard distribution and so 

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

2. Determine the maximum likelihood estimator of$\theta$ when $X _ { 1 } , \ldots , X _ { n }$ is a sample with density function 

$$
f (x) = \frac {1}{2} e ^ {- | x - \theta |}, \qquad - \infty <   x <   \infty
$$

3. Let $X _ { 1 } , \ldots , X _ { n }$ be a sample from a normal$\mu , \sigma ^ { 2 }$ population. Determine the maximum likelihood estimator of$\sigma ^ { 2 }$ when$\mu$ is known. What is the expected value of this estimator? 

4. The height of a radio tower is to be measured by measuring both the horizontal distance X from the center of its base to a measuring instrument and the vertical angle of the measuring device (see the following figure). If five measurements of the distance L give (in feet) values 

$$
1 5 0. 4 2, 1 5 0. 4 5, 1 5 0. 4 9, 1 5 0. 5 2, 1 5 0. 4 0
$$

and four measurements of the angle$\theta$ give (in degrees) values 

40.26, 40.27, 40.29, 40.26 

estimate the height of the tower. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/cc165448ea25d45abd1023ccf868eb87b23a11757052853d9a7ef26ccd163780.jpg)


5. Suppose that $X _ { 1 } , \ldots , X _ { n }$ are normal with mean$\mu _ { 1 } ; Y _ { 1 } , \ldots , Y _ { n }$ are normal with mean$\mu _ { 2 } ;$ and $W _ { 1 } , \ldots , W _ { n }$ are normal with mean$\mu _ { 1 } + \mu _ { 2 }$ . Assuming that all 3n random variables are independent with a common variance, find the maximum likelihood estimators of$\mu _ { 1 }$ and$\mu _ { 2 }$ 

6. River floods are often measured by their discharges (in units of feet cubed per second). The value v is said to be the value of a 100-year flood if 

$$
P \{D \geq v \} = . 0 1
$$

where D is the discharge of the largest flood in a randomly chosen year. The following table gives the flood discharges of the largest floods of the Blackstone River in Woonsocket, Rhode Island, in each of the years from 1929 to 1965. Assuming that these discharges follow a lognormal distribution, estimate the value of a 100-year flood. 


Annual Floods of the Blackstone River (1929–1965)


<table><tr><td>Year</td><td>Flood Discharge (ft3/s)</td></tr><tr><td>1929</td><td>4,570</td></tr><tr><td>1930</td><td>1,970</td></tr><tr><td>1931</td><td>8,220</td></tr><tr><td>1932</td><td>4,530</td></tr><tr><td>1933</td><td>5,780</td></tr><tr><td>1934</td><td>6,560</td></tr><tr><td>1935</td><td>7,500</td></tr><tr><td>1936</td><td>15,000</td></tr><tr><td>1937</td><td>6,340</td></tr><tr><td>1938</td><td>15,100</td></tr><tr><td>1939</td><td>3,840</td></tr><tr><td>1940</td><td>5,860</td></tr><tr><td>1941</td><td>4,480</td></tr><tr><td>1942</td><td>5,330</td></tr><tr><td>1943</td><td>5,310</td></tr><tr><td>1944</td><td>3,830</td></tr><tr><td>1945</td><td>3,410</td></tr><tr><td>1946</td><td>3,830</td></tr><tr><td>1947</td><td>3,150</td></tr><tr><td>1948</td><td>5,810</td></tr><tr><td>1949</td><td>2,030</td></tr><tr><td>1950</td><td>3,620</td></tr><tr><td>1951</td><td>4,920</td></tr><tr><td>1952</td><td>4,090</td></tr><tr><td>1953</td><td>5,570</td></tr><tr><td>1954</td><td>9,400</td></tr><tr><td>1955</td><td>32,900</td></tr><tr><td>1956</td><td>8,710</td></tr><tr><td>1957</td><td>3,850</td></tr><tr><td>1958</td><td>4,970</td></tr><tr><td>1959</td><td>5,398</td></tr><tr><td>1960</td><td>4,780</td></tr><tr><td>1961</td><td>4,020</td></tr><tr><td>1962</td><td>5,790</td></tr><tr><td>1963</td><td>4,510</td></tr><tr><td>1964</td><td>5,520</td></tr><tr><td>1965</td><td>5,300</td></tr></table>

7. A manufacturer of heat exchangers requires that the plate spacings of its exchang ers be between .240 and .260 inches. A quality control engineer sampled 20 exchangers and measured the spacing of the plates on each exchanger. If the sample mean and sample standard deviation of these 20 measurements are .254 and .005, estimate the fraction of all exchangers whose plate spacings fall outside the specified region. Assume that the plate spacings have a normal distribution. 

8. An electric scale gives a reading equal to the true weight plus a random error that is normally distributed with mean 0 and standard deviation$\sigma = . 1$ mg. Suppose that the results of five successive weighings of the same object are as follows: 3.142, 3.163, 3.155, 3.150, 3.141. 

(a) Determine a 95 percent confidence interval estimate of the true weight. 

(b) Determine a 99 percent confidence interval estimate of the true weight. 

9. The PCB concentration of a fish caught in Lake Michigan was measured by a technique that is known to result in an error of measurement that is normally distributed with a standard deviation of .08 ppm (parts per million). Suppose the results of 10 independent measurements of this fish are 

11.2, 12.4, 10.8, 11.6, 12.5, 10.1, 11.0, 12.2, 12.4, 10.6 

(a) Give a 95 percent confidence interval for the PCB level of this fish. 

(b) Give a 95 percent lower confidence interval. 

(c) Give a 95 percent upper confidence interval. 

10. The standard deviation of test scores on a certain achievement test is 11.3. If a random sample of 81 students had a sample mean score of 74.6, find a 90 percent confidence interval estimate for the average score of all students. 

11. Let $X _ { 1 } , \dots , X _ { n } , X _ { n + 1 }$ be a sample from a normal population having an unknown mean µ and variance 1. Let$\begin{array} { r } { \bar { X } _ { n } = \sum _ { i = 1 } ^ { n } X _ { i } / n } \end{array}$ be the average of the first n of them. 

(a) What is the distribution of $X _ { n + 1 } - { \bar { X } } _ { n } ?$ 

(b) If$\bar { X } _ { n } = 4 .$ , give an interval that, with 90 percent confidence, will contain the value of $X _ { n + 1 }$ 

12. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population whose mean µ is unknown but whose variance$\sigma ^ { 2 }$ is known, show that $( - \infty , { \overline { { X } } } + z _ { \alpha } \sigma / { \sqrt { n } } )$ is a $1 0 0 ( 1 - \alpha )$ percent lower confidence interval for$\mu .$ . 

13. A sample of 20 cigarettes is tested to determine nicotine content and the average value observed was 1.2 mg. Compute a 99 percent two-sided confidence interval for the mean nicotine content of a cigarette if it is known that the standard deviation of a cigarette’s nicotine content is$\sigma = . 2 \mathrm { m g }$ 

14. In Problem 13, suppose that the population variance is not known in advance of the experiment. If the sample variance is .04, compute a 99 percent two-sided confidence interval for the mean nicotine content. 

15. In Problem 14, compute a value c for which we can assert “with 99 percent confidence” that c is larger than the mean nicotine content of a cigarette. 

16. Suppose that when sampling from a normal population having an unknown mean$\mu$ and unknown variance$\sigma ^ { 2 }$ , we wish to determine a sample size n so as to guarantee that the resulting $1 0 0 ( 1 \textrm { -- } \alpha )$ percent confidence interval for$\mu$ will be of size no greater than A, for given values α and A. Explain how we can approximately do this by a double sampling scheme that first takes a subsample of size 30 and then chooses the total sample size by using the results of the first subsample. 

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

32. Let $X _ { 1 } , \dots , X _ { n } , X _ { n + 1 }$ denote a sample from a normal population whose mean µ and variance$\sigma ^ { 2 }$ are unknown. Suppose that we are interested in using the observed values of $X _ { 1 } , \ldots , X _ { n }$ to determine an interval, called a prediction interval, that we predict will contain the value of $X _ { n + 1 }$ with $1 0 0 ( 1 - \alpha )$ percent confidence. Let ${ \overline { { X } } } _ { n }$ and $S _ { n } ^ { 2 }$ be the sample mean and sample variance of $X _ { 1 } , \ldots , X _ { n }$ 

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

35. Verify the formulas given in Table 7.1 for the 100(1 − α) percent lower and upper confidence intervals for$\sigma ^ { 2 }$ 

36. The capacities (in ampere-hours) of 10 batteries were recorded as follows: 

$$
\begin{array}{l} 1 4 0, 1 3 6, 1 5 0, 1 4 4, 1 4 8, 1 5 2, 1 3 8, 1 4 1, 1 4 3, 1 5 1 \end{array}
$$

(a) Estimate the population variance$\sigma ^ { 2 }$ 

(b) Compute a 99 percent two-sided confidence interval for$\sigma ^ { 2 }$ . 

(c) Compute a value v that enables us to state, with 90 percent confidence, that$\sigma ^ { 2 }$ is less than v. 

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

(b) find a 90 percent confidence interval estimate of$\sigma$ . 

40. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population, explain how to obtain a 100(1 − α) percent confidence interval for the population variance$\sigma ^ { 2 }$ when the population mean µ is known. Explain in what sense knowledge of$\dot { \mu }$ improves the interval estimator compared with when it is unknown. 

Repeat Problem 38 if it is known that the mean burning time is 53.6 seconds. 

41. A civil engineer wishes to measure the compressive strength of two different types of concrete. A random sample of 10 specimens of the first type yielded the following data (in psi) 

$$
\begin{array}{r l} \text {Type 1:} & 3, 2 5 0, \quad 3, 2 6 8, \quad 4, 3 0 2, \quad 3, 1 8 4, \quad 3, 2 6 6 \\ & 3, 2 9 7, \quad 3, 3 3 2, \quad 3, 5 0 2, \quad 3, 0 6 4, \quad 3, 1 1 6 \end{array}
$$

whereas a sample of 10 specimens of the second yielded the data 

<table><tr><td>Type 2:</td><td>3,094,</td><td>3,106,</td><td>3,004,</td><td>3,066,</td><td>2,984,</td></tr><tr><td></td><td>3,124,</td><td>3,316,</td><td>3,212,</td><td>3,380,</td><td>3,018</td></tr></table>

If we assume that the samples are normal with a common variance, determine 

(a) a 95 percent two-sided confidence interval for$\mu _ { 1 } - \mu _ { 2 }$ , the difference in means; 

(b) a 95 percent one-sided upper confidence interval for$\mu _ { 1 } - \mu _ { 2 } ;$ 

(c) a 95 percent one-sided lower confidence interval for$\mu _ { 1 } - \mu _ { 2 }$ 

42. Independent random samples are taken from the output of two machines on a production line. The weight of each item is of interest. From the first machine, a sample of size 36 is taken, with sample mean weight of 120 grams and a sample variance of 4. From the second machine, a sample of size 64 is taken, with a sample mean weight of 130 grams and a sample variance of 5. It is assumed that the weights of items from the first machine are normally distributed with mean$\mu _ { 1 }$ and variance$\sigma ^ { 2 }$ , and that the weights of items from the second machine are normally distributed with mean$\mu _ { 2 }$ and variance$\sigma ^ { 2 }$ (that is, the variances are assumed to be equal). Find a 99 percent confidence interval for$\mu _ { 1 } - \mu _ { 2 }$ , the difference in population means. 

43. Do Problem 42 when it is known in advance that the population variances are 4 and 5. 

44. The following are the burning times in seconds of floating smoke pots of two different types. 

<table><tr><td colspan="2">Type I</td><td colspan="2">Type II</td></tr><tr><td>481</td><td>572</td><td>526</td><td>537</td></tr><tr><td>506</td><td>561</td><td>511</td><td>582</td></tr><tr><td>527</td><td>501</td><td>556</td><td>605</td></tr><tr><td>661</td><td>487</td><td>542</td><td>558</td></tr><tr><td>501</td><td>524</td><td>491</td><td>578</td></tr></table>

Find a 99 percent confidence interval for the mean difference in burning times assuming normality with unknown but equal variances. 

45. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population having known mean$\mu _ { 1 }$ and unknown variance$\sigma _ { 1 } ^ { 2 }$ , and $Y _ { 1 } , \dots , Y _ { m }$ is an independent sample from a normal population having known mean$\mu _ { 2 }$ and unknown variance$\sigma _ { 2 } ^ { 2 }$ determine a $1 0 0 ( 1 - \alpha )$ percent confidence interval for$\sigma _ { 1 } ^ { 2 } / \sigma _ { 2 } ^ { 2 }$ 

46. Two analysts took repeated readings on the hardness of city water. Assuming that the readings of analyst i constitute a sample from a normal population having variance$\sigma _ { i } ^ { 2 } , i = 1 , 2$ , compute a 95 percent two-sided confidence interval for$\sigma _ { 1 } ^ { 2 } / \sigma _ { 2 } ^ { 2 }$ when the data are as follows: 

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

53. In a recent study, 79 of 140 meteorites were observed to enter the atmosphere with a velocity of less than 25 miles per second. If we take$\hat { p } = 7 9 / 1 4 0$ as an estimate of the probability that an arbitrary meteorite that enters the atmosphere will have a speed less than 25 miles per second, what can we say, with 99 percent confidence, about the maximum error of our estimate? 

54. A random sample of 100 items from a production line revealed 17 of them to be defective. Compute a 95 percent two-sided confidence interval for the probability that an item produced is defective. Determine also a 99 percent upper confidence interval for this value. What assumptions are you making? 

55. Of 100 randomly detected cases of individuals having lung cancer, 67 died within 5 years of detection. 

(a) Estimate the probability that a person contracting lung cancer will die within 5 years. 

(b) How large an additional sample would be required to be 95 percent confident that the error in estimating the probability in part (a) is less than .02? 

56. Derive 100(1 − α) percent lower and upper confidence intervals for p, when the data consist of the values of n independent Bernoulli random variables with parameter p. 

57. Suppose the lifetimes of batteries are exponentially distributed with mean θ . If the average of a sample of 10 batteries is 36 hours, determine a 95 percent two-sided confidence interval for θ. 

58. Determine $1 0 0 ( 1 - \alpha )$ percent one-sided upper and lower confidence intervals for θ in Problem 57. 

59. Let $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ denote a sample from a population whose mean value θ is unknown. Use the results of Example 7.7b to argue that among all unbiased estimators of θ of the form$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \lambda _ { i } \bar { X _ { i } } , \sum _ { i = 1 } ^ { n } \lambda _ { i } = \bar { 1 } } \end{array}$ , the one with minimal mean square error has$\lambda _ { i } \equiv 1 / n , i = 1 , \ldots , n .$ 

60. Consider two independent samples from normal populations having the same variance$\sigma ^ { 2 }$ , of respective sizes n and m. That is,$X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { m }$ are independent samples from normal populations each having variance$\sigma ^ { 2 }$ . Let $S _ { x } ^ { 2 }$ and$\mathsf { \bar { S } } _ { y } ^ { 2 }$ denote the respective sample variances. Thus both $S _ { x } ^ { 2 }$ and $S _ { y } ^ { 2 }$ are unbiased estimators of$\sigma ^ { 2 }$ . Show by using the results of Example 7.7b along with the fac that 

$$
\mathrm{Var} (\chi_ {k} ^ {2}) = 2 k
$$

where$\chi _ { k } ^ { 2 }$ is chi-square with k degrees of freedom, that the minimum mean square estimator of$\sigma ^ { 2 }$ of the form$\lambda S _ { x } ^ { 2 } + ( 1 - \lambda ) S _ { y } ^ { 2 }$ is 

$$
S _ {p} ^ {2} = \frac {(n - 1) S _ {x} ^ {2} + (m - 1) S _ {y} ^ {2}}{n + m - 2}
$$

This is called the pooled estimator of$\sigma ^ { 2 }$ . 

61. Consider two estimators $d _ { 1 }$ and $d _ { 2 }$ of a parameter θ . If $E [ d _ { 1 } ] ~ = ~ \theta$$\mathrm { V a r } ( d _ { 1 } ) = 6$ and $E [ d _ { 2 } ] = \theta + 2 , { \mathrm { V a r } } ( d _ { 2 } ) = 2$ , which estimator should be preferred? 

62. Suppose that the number of accidents occurring daily in a certain plant has a Poisson distribution with an unknown mean λ. Based on previous experience in similar industrial plants, suppose that a statistician’s initial feelings about the possible value of λ can be expressed by an exponential distribution with parameter 1. That is, the prior density is 

$$
p (\lambda) = e ^ {- \lambda}, \qquad 0 <   \lambda <   \infty
$$

Determine the Bayes estimate of λ if there are a total of 83 accidents over the next 10 days. What is the maximum likelihood estimate? 

63. The functional lifetimes in hours of computer chips produced by a certain semiconductor firm are exponentially distributed with mean $1 / \lambda$ . Suppose that the prior distribution on λ is the gamma distribution with density function 

$$
g (x) = \frac {e ^ {- x} x ^ {2}}{2}, \qquad 0 <   x <   \infty
$$

If the average life of the first 20 chips tested is 4.6 hours, compute the Bayes estimate of$\gimel$ . 

64. Each item produced will, independently, be defective with probability$\scriptstyle { \boldsymbol { p } } .$ . If the prior distribution on$\boldsymbol { \underline { P } }$ is uniform on (0, 1), compute the posterior probability that$\boldsymbol { \underline { P } }$ is less than .2 given 

(a) a total of 2 defectives out of a sample of size 10; 

(b) a total of 1 defective out of a sample of size 10; 

(c) a total of 10 defectives out of a sample of size 10. 

65. The breaking strength of a certain type of cloth is to be measured for 10 spec imens. The underlying distribution is normal with unknown mean θ but with a standard deviation equal to 3 psi. Suppose also that based on previous experience we feel that the unknown mean has a prior distribution that is normally dis tributed with mean 200 and standard deviation 2. If the average breaking strength of a sample of 20 specimens is 182 psi, determine a region that contains θ with probability .95. 

# HYPOTHESIS TESTING

## 8.1 INTRODUCTION

As in the previous chapter, let us suppose that a random sample from a population distri bution, specified except for a vector of unknown parameters, is to be observed. However, rather than wishing to explicitly estimate the unknown parameters, let us now suppose that we are primarily concerned with using the resulting sample to test some particular hypothesis concerning them. As an illustration, suppose that a construction firm has just purchased a large supply of cables that have been guaranteed to have an average breaking strength of at least 7,000 psi. To verify this claim, the firm has decided to take a random sample of 10 of these cables to determine their breaking strengths. They will then use the result of this experiment to ascertain whether or not they accept the cable manufacturer’s hypothesis that the population mean is at least 7,000 pounds per square inch. 

A statistical hypothesis is usually a statement about a set of parameters of a population distribution. It is called a hypothesis because it is not known whether or not it is true. A primary problem is to develop a procedure for determining whether or not the values of a random sample from this population are consistent with the hypothesis. For instance, consider a particular normally distributed population having an unknown mean value θ and known variance 1. The statement “θ is less than 1” is a statistical hypothesis that we could try to test by observing a random sample from this population. If the random sample is deemed to be consistent with the hypothesis under consideration, we say that the hypothesis has been “accepted”; otherwise we say that it has been “rejected.” 

Note that in accepting a given hypothesis we are not actually claiming that it is true but rather we are saying that the resulting data appear to be consistent with it. For instance, in the case of a normal (θ , 1) population, if a resulting sample of size 10 has an average value of 1.25, then although such a result cannot be regarded as being evidence in favor of the hypothesis $^ { \infty } \theta \ < 1 , ^ { \infty }$ it is not inconsistent with this hypothesis, which would thus be accepted. On the other hand, if the sample of size 10 has an average value of 3, then even though a sample value that large is possible when$\theta < 1$ , it is so unlikely that it seem inconsistent with this hypothesis, which would thus be rejected. 

## 8.2 SIGNIFICANCE LEVELS

Consider a population having distribution $F _ { \theta }$ , where$\theta$ is unknown, and suppose we want to test a specific hypothesis about$\theta .$ . We shall denote this hypothesis by $H _ { 0 }$ and call it the null hypothesis. For example, if $F _ { \theta }$ is a normal distribution function with mean$\theta$ and variance equal to 1, then two possible null hypotheses about$\theta$ are 

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

For instance, a common test of the hypothesis that$\theta _ { ; }$ , the mean of a normal population with variance 1, is equal to 1 has a critical region given by 

$$
C = \left\{(X _ {1}, \dots , X _ {n}): \left| \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n} - 1 \right| > \frac {1 . 9 6}{\sqrt {n}} \right\}\tag{8.2.1}
$$

Thus, this test calls for rejection of the null hypothesis that$\theta = 1$ when the sample average differs from 1 by more than 1.96 divided by the square root of the sample size. 

It is important to note when developing a procedure for testing a given null hypothesis $H _ { 0 }$ that, in any test, two different types of errors can result. The first of these, called a type I error, is said to result if the test incorrectly calls for rejecting $H _ { 0 }$ when it is indeed correct. The second, called a type II error, results if the test calls for accepting $H _ { 0 }$ when it is false. 

Now, as was previously mentioned, the objective of a statistical test of$\dot { H } _ { 0 }$ is not to explicitly determine whether or not $H _ { 0 }$ is true but rather to determine if its validity is consistent with the resultant data. Hence, with this objective it seems reasonable that $H _ { 0 }$ should only be rejected if the resultant data are very unlikely when $H _ { 0 }$ is true. The classical way of accomplishing this is to specify a value$\alpha$ and then require the test to have the property that whenever $H _ { 0 }$ is true its probability of being rejected is never greater than$\alpha .$ . The value$\alpha _ { ; }$ , called the level of significance of the test, is usually set in advance, with commonly chosen values being$\alpha = . 1 , . 0 5 , . 0 0 5$ . In other words, the classical approach to testing $H _ { 0 }$ is to fix a significance level α and then require that the test have the property that the probability of a type I error occurring can never be greater than$\alpha .$ 

Suppose now that we are interested in testing a certain hypothesis concerning$\theta ,$ , an unknown parameter of the population. Specifically, for a given set of parameter values $w ,$ suppose we are interested in testing 

$$
H _ {0}: \theta \in w
$$

A common approach to developing a test of $H _ { 0 } ,$ , say at level of significance$\alpha ,$ , is to start by determining a point estimator of$\theta - s a y d ( \mathbf { X } )$ . The hypothesis is then rejected if $d ( \mathbf { X } )$ is “far away” from the region $w .$ . However, to determine how “far away” it need be to justify rejection of $H _ { 0 }$ , we need to determine the probability distribution of $d ( \mathbf { X } )$ when $H _ { 0 }$ is true since this will usually enable us to determine the appropriate critical region so as to make the test have the required significance level$\alpha .$ . For example, the test of the hypothesis that the mean of a normal (θ , 1) population is equal to 1, given by Equation 8.2.1, call for rejection when the point estimate of θ — that is, the sample average — is farther than $1 . 9 6 / \sqrt { n }$ away from 1. As we will see in the next section, the value $1 . 9 6 / \sqrt { n }$ was chosen to meet a level of significance of$\alpha = . 0 5$ 

## 8.3 TESTS CONCERNING THE MEAN OF A NORMAL POPULATION

## 8.3.1 Case of Known Variance

Suppose that $X _ { 1 } , \ldots , X _ { n }$ is a sample of size n from a normal distribution having an unknown mean$\mu$ and a known variance$\sigma ^ { 2 }$ and suppose we are interested in testing the null hypothesis 

$$
H _ {0}: \mu = \mu_ {0}
$$

against the alternative hypothesis 

$$
H _ {1}: \mu \neq \mu_ {0}
$$

where$\mu _ { 0 }$ is some specified constant. 

Since$\textstyle { \overline { { X } } } = \sum _ { i = 1 } ^ { n } X _ { i } / n$ is a natural point estimator of ${ \bf \dot { \mu } } _ { \mu }$ , it seems reasonable to accept $H _ { 0 }$ if X is not too far from$\mu _ { 0 }$ . That is, the critical region of the test would be of the form 

$$
C = \{X _ {1}, \ldots , X _ {n}: | \overline {{X}} - \mu_ {0} | > c \}\tag{8.3.1}
$$

for some suitably chosen value $c .$ 

If we desire that the test has significance level$\alpha ,$ , then we must determine the critical value $c$ in Equation 8.3.1 that will make the type I error equal to$\alpha .$ . That is, c must be such that 

$$
P _ {\mu_ {0}} \{| \overline {{X}} - \mu_ {0} | > c \} = \alpha\tag{8.3.2}
$$

where we write $P _ { \mu _ { 0 } }$ to mean that the preceding probability is to be computed under the assumption that$\mu = \mu _ { 0 }$ . However, when$\mu = \mu _ { 0 } , { \overline { { X } } }$ will be normally distributed with mean$\mu _ { 0 }$ and variance$\sigma ^ { 2 } / n$ and so $Z _ { i }$ , defined by 

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

Thus, the significance level$\alpha$ test is to reject H if $| \overline { { X } } - \mu _ { 0 } | > z _ { \alpha / 2 } \sigma / \sqrt { n }$ and accept otherwise; or, equivalently, to 

$$
\text { reject } \quad H _ {0} \quad \text { if } \quad \frac {\sqrt {n}}{\sigma} | \overline {{X}} - \mu_ {0} | > z _ {\alpha / 2}\tag{8.3.3}
$$

$$
\text {   accept   } \quad H _ {0} \quad \text {   if   } \quad \frac {\sqrt {n}}{\sigma} | \overline {{X}} - \mu_ {0} | \leq z _ {\alpha / 2}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/21fdcbc97156c863a5154ea75a6e5b22435d315c7722498ba4c5445b4b4911ba.jpg)



FIGURE 8.1


This can be pictorially represented as shown in Figure 8.1, where we have superim posed the standard normal density function [which is the density of the test statistic ${ \sqrt { n } } ( { \overline { { X } } } - \mu _ { 0 } ) /$ /σ when $H _ { 0 }$ is true]. 

EXAMPLE 8.3a It is known that if a signal of value$\mu$ is sent from location$\mathsf { A } ,$ then the value received at location B is normally distributed with mean$\mu$ and standard deviation 2. That is, the random noise added to the signal is an $N ( 0 , 4 )$ random variable. There i reason for the people at location B to suspect that the signal value$\mu = 8$ will be sent today. Test this hypothesis if the same signal value is independently sent five times and the average value received at location B is ${ \overline { { \overline { { X } } } } } = 9 . 5$ 

SOLUTION Suppose we are testing at the 5 percent level of significance. To begin, we compute the test statistic 

$$
\frac {\sqrt {n}}{\sigma} | \overline {{X}} - \mu_ {0} | = \frac {\sqrt {5}}{2} (1. 5) = 1. 6 8
$$

Since this value is less than $z _ { . 0 2 5 } = 1 . 9 6$ , the hypothesis is accepted. In other words, the data are not inconsistent with the null hypothesis in the sense that a sample average as far from the value 8 as observed would be expected, when the true mean is 8, over 5 percent of the time. Note, however, that if a less stringent significance level were chosen — say$\alpha = . 1$ — then the null hypothesis would have been rejected. This follows since $z _ { . 0 5 } = 1 . 6 4 5$ , which is less than 1.68. Hence, if we would have chosen a test that had a 10 percent chance of rejecting $H _ { 0 }$ when $H _ { 0 }$ was true, then the null hypothesis would have been rejected. 

The “correct” level of significance to use in a given situation depends on the individ ual circumstances involved in that situation. For instance, if rejecting a null hypothesis $H _ { 0 }$ would result in large costs that would thus be lost if $H _ { 0 }$ were indeed true, then we might elect to be quite conservative and so choose a significance level of .05 or .01. Also, if we initially feel strongly that $H _ { 0 }$ was correct, then we would require very stringent data evidence to the contrary for us to reject $H _ { 0 }$ . (That is, we would set a very low significance level in this situation.) ■ 

The test given by Equation 8.3.3 can be described as follows: For any observed value of the test statistic ${ \sqrt { n } } | { \overline { { X } } } - \mu _ { 0 } | / \sigma$ , call it$\nu ,$ the test calls for rejection of the null hypothesis if the probability that the test statistic would be as large as v when $H _ { 0 }$ is true is less than or equal to the significance level α. From this, it follows that we can determine whether or not to accept the null hypothesis by computing, first, the value of the test statistic and, second, the probability that a unit normal would (in absolute value) exceed that quantity. This probability — called the$\scriptstyle { p \cdotp }$ -value of the test — gives the critical significance level in the sense that $H _ { 0 }$ will be accepted if the significance level$\alpha$ is less than the$\scriptstyle { p - { \frac { } { } } }$ -value and rejected if it is greater than or equal. 

In practice, the significance level is often not set in advance but rather the data are looked at to determine the resultant p-value. Sometimes, this critical significance level is clearly much larger than any we would want to use, and so the null hypothesis can be readily accepted. At other times the$\scriptstyle { p \cdotp }$ -value is so small that it is clear that the hypothesis should be rejected. 

EXAMPLE 8.3b In Example 8.3a, suppose that the average of the 5 values received is$\overline { { X } } = 8 . 5$ . In this case, 

$$
\frac {\sqrt {n}}{\sigma} | \overline {{{X}}} - \mu_ {0} | = \frac {\sqrt {5}}{4} = . 5 5 9
$$

Since 

$$
\begin{array}{r l} P \{| Z | >. 5 5 9 \} & = 2 P \{Z >. 5 5 9 \} \\ & = 2 \times . 2 8 8 = . 5 7 6 \end{array}
$$

it follows that the p-value is .576 and thus the null hypothesis $H _ { 0 }$ that the signal sent has value 8 would be accepted at any significance level$\alpha < . 5 7 6$ . Since we would clearly never want to test a null hypothesis using a significance level as large as $. 5 7 6 , H _ { 0 }$ would be accepted. 

On the other hand, if the average of the data values were 11.5, then the p-value of the test that the mean is equal to 8 would be 

$$
\begin{array}{c} P \{| Z | > 1. 7 5 \sqrt {5} \} = P \{| Z | > 3. 9 1 3 \} \\ \approx . 0 0 0 0 5 \end{array}
$$

For such a small$\scriptstyle { p \cdotp }$ -value, the hypothesis that the value 8 was sent is rejected. ■ 

We have not yet talked about the probability of a type II error — that is, the probability of accepting the null hypothesis when the true mean$\mu$ is unequal to$\mu _ { 0 }$ . This probability will depend on the value of$\mu _ { ; }$ , and so let us define$\beta ( \mu )$ by 

$$
\begin{array}{l} \beta (\mu) = P _ {\mu} \{\text { acceptance   of } H _ {0} \} \\ \qquad = P _ {\mu} \left\{\left| \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} \right| \leq z _ {\alpha / 2} \right\} \\ \qquad = P _ {\mu} \left\{- z _ {\alpha / 2} \leq \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} \leq z _ {\alpha / 2} \right\} \end{array}
$$

The function$\beta ( \mu )$ is called the operating characteristic (or OC) curve and represents the probability that $H _ { 0 }$ will be accepted when the true mean is$\mu$ . 

To compute this probability, we use the fact that$\overline { { X } }$ is normal with mean$\mu$ and variance$\sigma ^ { 2 } / n$ and so 

$$
Z \equiv \frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} \sim \mathcal {N} (0, 1)
$$

Hence, 

$$
\begin{array}{l} \beta (\mu) = P _ {\mu} \left\{- z _ {\alpha / 2} \leq \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} \leq z _ {\alpha / 2} \right\} \\ = P _ {\mu} \left\{- z _ {\alpha / 2} - \frac {\mu}{\sigma / \sqrt {n}} \leq \frac {\overline {{X}} - \mu_ {0} - \mu}{\sigma / \sqrt {n}} \leq z _ {\alpha / 2} - \frac {\mu}{\sigma / \sqrt {n}} \right\} \\ = P _ {\mu} \left\{- z _ {\alpha / 2} - \frac {\mu}{\sigma / \sqrt {n}} \leq Z - \frac {\mu_ {0}}{\sigma / \sqrt {n}} \leq z _ {\alpha / 2} - \frac {\mu}{\sigma / \sqrt {n}} \right\} \\ = P \left\{\frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} - z _ {\alpha / 2} \leq Z \leq \frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} + z _ {\alpha / 2} \right\} \\ = \Phi \left(\frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} + z _ {\alpha / 2}\right) - \Phi \left(\frac {\mu_ {0} - \mu}{\sigma / \sqrt {n}} - z _ {\alpha / 2}\right) \end{array}\tag{8.3.4}
$$

where$\Phi$ is the standard normal distribution function. 

For a fixed significance level$\alpha _ { ; }$ , the OC curve given by Equation 8.3.4 is symmetric about$\mu _ { 0 }$ and indeed will depend on$\mu$ only through $( \sqrt { n } / \sigma ) | \mu - \mu _ { 0 } |$ . This curve with the abscissa changed from$\mu$ to $d = ( { \sqrt { n } } / \sigma ) | \mu - \mu _ { 0 } |$ is presented in Figure 8.2 when$\alpha = . 0 5$ 

EXAMPLE 8.3c For the problem presented in Example 8.3a, let us determine the probability of accepting the null hypothesis that$\mu = 8$ when the actual value sent is 10. To do so, we compute 

$$
\frac {\sqrt {n}}{\sigma} (\mu_ {0} - \mu) = - \frac {\sqrt {5}}{2} \times 2 = - \sqrt {5}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/fba2b0306e27179100b91aaf808d02a3ca64dd01ead55a9a8172062d4c97f019.jpg)



FIGURE 8.2 The OC curve for the two-sided normal test for significance level$\alpha = . 0 5$



$\mathrm { A } s z _ { . 0 2 5 } = 1 . 9 6$ , the desired probability is, from Equation 8.3.4,


$$
\begin{array}{r l} & {\Phi (- \sqrt {5} + 1. 9 6) - \Phi (- \sqrt {5} - 1. 9 6)} \\ & {\quad = 1 - \Phi (\sqrt {5} - 1. 9 6) - [ 1 - \Phi (\sqrt {5} + 1. 9 6) ]} \\ & {\quad = \Phi (4. 1 9 6) - \Phi (. 2 7 6)} \\ & {\quad = . 3 9 2 \quad \blacksquare} \end{array}
$$

## REMARK

The function $1 - \beta ( \mu )$ is called the power-function of the test. Thus, for a given value$\mu ,$ the power of the test is equal to the probability of rejection when$\mu$ is the true value. ■ 

The operating characteristic function is useful in determining how large the random sample need be to meet certain specifications concerning type II errors. For instance, suppose that we desire to determine the sample size n necessary to ensure that the probability of accepting $H _ { 0 } : \mu = \mu _ { 0 }$ when the true mean is actually$\mu _ { 1 }$ is approximately$\beta .$ . That is, we want n to be such that 

$$
\beta (\mu_ {1}) \approx \beta
$$

But from Equation 8.3.4, this is equivalent to 

$$
\Phi \left(\frac {\sqrt {n} (\mu_ {0} - \mu_ {1})}{\sigma} + z _ {\alpha / 2}\right) - \Phi \left(\frac {\sqrt {n} (\mu_ {0} - \mu_ {1})}{\sigma} - z _ {\alpha / 2}\right) \approx \beta\tag{8.3.5}
$$

Although the foregoing cannot be analytically solved for n, a solution can be obtained by using the standard normal distribution table. In addition, an approximation for n can be derived from Equation 8.3.5 as follows. To start, suppose that$\mu _ { 1 } > \mu _ { 0 }$ . Then, because this implies that 

$$
\frac {\mu_ {0} - \mu_ {1}}{\sigma / \sqrt {n}} - z _ {\alpha / 2} \leq - z _ {\alpha / 2}
$$

it follows, since$\Phi$ is an increasing function, that 

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

In fact, the same approximation would result when$\mu _ { 1 } ~ < ~ \mu _ { 0 }$ (the details are left as an exercise) and so Equation 8.3.7 is in all cases a reasonable approximation to the sample size necessary to ensure that the type II error at the value$\mu = \mu _ { 1 }$ is approximately equal to$\beta$ . 

EXAMPLE 8.3d For the problem of Example 8.3a, how many signals need be sent so that the .05 level test of $H _ { 0 } : \mu = 8$ has at least a 75 percent probability of rejection when$\mu = 9 . 2 ?$ 

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

Therefore, if the message is sent 20 times, then there is a 76.5 percent chance that the null hypothesis$\mu = 8$ will be rejected when the true mean is 9.2. ■ 

## ONE-SIDED TESTS

In testing the null hypothesis that$\mu = \mu _ { 0 }$ , we have chosen a test that calls for rejection when$\overline { { \boldsymbol X } }$ is far from$\mu _ { 0 }$ . That is, a very small value of$\overline { { \boldsymbol X } }$ or a very large value appears to make it unlikely that$\mu$ (which$\overline { { \boldsymbol X } }$ is estimating) could equal$\mu _ { 0 }$ . However, what happens when the only alternative to$\mu$ being equal to$\mu _ { 0 }$ is for$\mu$ to be greater than$\mu _ { 0 } ?$ That is, what happens when the alternative hypothesis to $H _ { 0 } : \mu = \mu _ { 0 }$ is $H _ { 1 } : \mu > \mu _ { 0 } ?$ Clearly, in this latter case we would not want to reject $H _ { 0 }$ when X is small (since a small X is more likely when $H _ { 0 }$ is true than when $H _ { 1 }$ is true). Thus, in testing 

$$
H _ {0}: \mu = \mu_ {0} \quad \text { versus } \quad H _ {1}: \mu > \mu_ {0}\tag{8.3.8}
$$

we should reject $H _ { 0 }$ when ${ \overline { { X } } } ,$ , the point estimate of$\mu _ { 0 }$ , is much greater than$\mu _ { 0 }$ . That is, the critical region should be of the following form: 

$$
C = \{(X _ {1}, \ldots , X _ {n}): \overline {{X}} - \mu_ {0} > c \}
$$

Since the probability of rejection should equal α when $H _ { 0 }$ is true (that is, when$\mu = \mu _ { 0 } )$ we require that c be such that 

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

This is called a one-sided critical region (since it calls for rejection only when$\overline { { X } }$ is large). Correspondingly, the hypothesis testing problem 

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

Since the test would call for rejection at all significance levels greater than or equal to .0465, it would, for instance, reject the null hypothesis at the$\alpha = . 0 5$ level of significance. ■ 

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

Since$\Phi ,$ , being a distribution function, is increasing in its argument, it follows that$\beta ( \mu )$ decreases in$\mu ;$ which is intuitively pleasing since it certainly seems reasonable that the larger the true mean$\mu ,$ , the less likely it should be to conclude that$\mu \leq \mu _ { 0 }$ . Also since$\Phi ( z _ { \alpha } ) = 1 - \alpha$ , it follows that 

$$
\beta (\mu_ {0}) = 1 - \alpha
$$

The test given by Equation 8.3.10, which was designed to test $H _ { 0 } : \mu = \mu _ { 0 }$ versus $H _ { 1 } : \mu > \mu _ { 0 }$ can also be used to test, at level of significance$\alpha ,$ , the one-sided hypothesis 

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

But it has previously been shown that for the test given by Equation 8.3.10,$\beta ( \mu )$ decreases in$\mu$ and$\beta ( \mu _ { 0 } ) = 1 - \alpha$ . This gives that 

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

(a) There is a direct analogy between confidence interval estimation and hypothesis testing For instance, for a normal population having mean$\mu$ and known variance$\sigma ^ { 2 }$ , we have shown in Section 7.3 that$\mathrm { ~ a ~ } 1 0 0 ( 1 - \alpha )$ percent confidence interval for$\mu$ is given by 

$$
\mu \in \left(\overline {{x}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \overline {{x}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right)
$$

where$\overline { { x } }$ is the observed sample mean. More formally, the preceding confidence interval statement is equivalent to 

$$
P \left\{\mu \in \left(\overline {{X}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \overline {{X}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right) \right\} = 1 - \alpha
$$

Hence, if$\mu = \mu _ { 0 }$ , then the probability that$\mu _ { 0 }$ will fall in the interval 

$$
\left(\overline {{X}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \overline {{X}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right)
$$

is $1 - \alpha ,$ , implying that a significance level$\alpha$ test of $H _ { 0 } : \mu = \mu _ { 0 }$ versus $H _ { 1 } : \mu \neq \mu _ { 0 }$ is to reject $H _ { 0 }$ when 

$$
\mu_ {0} \notin \left(\overline {{X}} - z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}, \overline {{X}} + z _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right)
$$

Similarly, since a $1 0 0 ( 1 - \alpha )$ percent one-sided confidence interval for$\mu$ is given by 

$$
\mu \in \left(\overline {{X}} - z _ {\alpha} \frac {\sigma}{\sqrt {n}}, \infty\right)
$$

it follows that an α-level significance test of $H _ { 0 } : \mu \le \mu _ { 0 }$ versus $H _ { 1 } : \mu > \mu _ { 0 }$ is to reject $H _ { 0 }$ when$\mu _ { 0 } \not \in ( { \overline { { X } } } - z _ { \alpha } \sigma / { \sqrt { n } } , \infty )$ — that is, when$\mu _ { 0 } < \overline { { X } } - z _ { \alpha } \sigma / \sqrt { n } .$ 


TABLE 8.1 $X _ { 1 } , \ldots , X _ { n }$ Is a Sample from $a \mathcal { N } ( \mu , \sigma ^ { 2 } )$ Population$\sigma ^ { 2 }$ Is Known$\overline { { X } } = \sum _ { i = 1 } ^ { n } X _ { i } / n$


<table><tr><td><eq>H_0</eq></td><td><eq>H_1</eq></td><td>Test Statistic TS</td><td>Significance Level α Test</td><td>p-Value if <eq>TS = t</eq></td></tr><tr><td><eq>\mu = \mu_0</eq></td><td><eq>\mu \neq \mu_0</eq></td><td><eq>\sqrt{n(\overline{X} - \mu_0)/\sigma}</eq></td><td>Reject if <eq>|TS| &gt; z_{\alpha/2}</eq></td><td><eq>2P\{Z \geq |t|\}</eq></td></tr><tr><td><eq>\mu \leq \mu_0</eq></td><td><eq>\mu &gt; \mu_0</eq></td><td><eq>\sqrt{n(\overline{X} - \mu_0)/\sigma}</eq></td><td>Reject if <eq>TS &gt; z_{\alpha}</eq></td><td><eq>P\{Z \geq t\}</eq></td></tr><tr><td><eq>\mu \geq \mu_0</eq></td><td><eq>\mu &lt; \mu_0</eq></td><td><eq>\sqrt{n(\overline{X} - \mu_0)/\sigma}</eq></td><td>Reject if <eq>TS &lt; -z_{\alpha}</eq></td><td><eq>P\{Z \leq t\}</eq></td></tr></table>


Z is a standard normal random variable. 


(b) A Remark on Robustness A test that performs well even when the underlying assumptions on which it is based are violated is said to be robust. For instance, the tests of Sections 8.3.1 and 8.3.1.1 were derived under the assumption that the underlying population distribution is normal with known variance$\sigma ^ { 2 }$ . However, in deriving these tests, this assumption was used only to conclude that$\overline { { X } }$ also has a normal distribution. But, by the central limit theorem, it follows that for a reasonably large sample size,$\overline { { X } }$ will approximately have a normal distribution no matter what the underlying distribution. Thu we can conclude that these tests will be relatively robust for any population distribution with variance$\sigma ^ { 2 }$ 

Table 8.1 summarizes the tests of this subsection. 

## 8.3.2 Case of Unknown Variance: The <sub>t</sub>-Test

Up to now we have supposed that the only unknown parameter of the normal population distribution is its mean. However, the more common situation is one where the mean$\mu$ and variance$\sigma ^ { 2 }$ are both unknown. Let us suppose this to be the case and again consider a test of the hypothesis that the mean is equal to some specified value$\mu _ { 0 }$ . That is, consider a test of 

$$
H _ {0}: \mu = \mu_ {0}
$$

versus the alternative 

$$
H _ {1}: \mu \neq \mu_ {0}
$$

It should be noted that the null hypothesis is not a simple hypothesis since it does not specify the value of$\sigma ^ { 2 }$ . 

As before, it seems reasonable to reject $H _ { 0 }$ when the sample mean$\overline { { X } }$ is far from$\mu _ { 0 }$ However, how far away it need be to justify rejection will depend on the variance$\sigma ^ { 2 }$ Recall that when the value of$\cdot \sigma ^ { 2 }$ was known, the test called for rejecting $H _ { 0 }$ when $| \overline { { X } } - \mu _ { 0 } |$ exceeded $z _ { \alpha / 2 } \sigma / \sqrt { n }$ or, equivalently, when 

$$
\left| \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} \right| > z _ {\alpha / 2}
$$

Now when$\sigma ^ { 2 }$ is no longer known, it seems reasonable to estimate it by 

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

to require for rejection, in order that the resulting test have significance level$\alpha ,$ , we must determine the probability distribution of this statistic when $H _ { 0 }$ is true. However, as shown in Section 6.5, the statistic $T _ { ; }$ , defined by 

$$
T = \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S}
$$

has, when$\mu = \mu _ { 0 }$ , a t -distribution with $n - 1$ degrees of freedom. Hence, 

$$
P _ {\mu_ {0}} \left\{- t _ {\alpha / 2, n - 1} \leq \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \leq t _ {\alpha / 2, n - 1} \right\} = 1 - \alpha\tag{8.3.11}
$$

where $t _ { \alpha / 2 , n - 1 }$ is the 100 α/2 upper percentile value of the t-distribution with $n - 1$ degrees of freedom. (That is,$P \{ T _ { n - 1 } \ge t _ { \alpha / 2 , n - 1 } \} = P \{ T _ { n - 1 } \le - t _ { \alpha / 2 , n - 1 } \} = \alpha / 2$ when $T _ { n - 1 }$ has a t -distribution with $n - 1$ degrees of freedom.) From Equation 8.3.11 we see that the appropriate significance level α test of 

$$
H _ {0}: \mu = \mu_ {0} \qquad \text { versus } \qquad H _ {1}: \mu \neq \mu_ {0}
$$

is, when$\sigma ^ { 2 }$ is unknown, to 

$$
\text {   accept   } \quad H _ {0} \quad \text {   if   } \quad \left| \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \right| \leq t _ {\alpha / 2, n - 1}\tag{8.3.12}
$$

$$
\text { reject } \quad H _ {0} \quad \text { if } \quad \left| \frac {\sqrt {n} (\overline {{X}} - \mu_ {0})}{S} \right| > t _ {\alpha / 2, n - 1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/1ba9ef066ee36b8808f9ad74dbd0978b8df20a5316dde20f0cd7bd2306468d3e.jpg)



FIGURE 8.3 The two-sided t -test.


The test defined by Equation 8.3.12 is called a two-sided t-test. It is pictorially illustrated in Figure 8.3. 

If we let t denote the observed value of the test statistic $T = \sqrt { n } ( \overline { { X } } - \mu _ { 0 } ) / S$ , then the p-value of the test is the probability that$\lvert T \rvert$ would exceed $| t |$ when $H _ { 0 }$ is true. That is, the p-value is the probability that the absolute value of a t-random variable with $n - 1$ degrees of freedom would exceed |t|. The test then calls for rejection at all significance levels higher than the p-value and acceptance at all lower significance levels. 

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

The p-value of this test is the probability that a t-random variable with $n - 1$ degrees of freedom would be less than or equal to the observed value of$\sqrt { n } ( \overline { { X } } - \mu _ { 0 } ) / S$ 

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


EXAMPLE 8.3j In a single-server queueing system in which customers arrive according to a Poisson process, the long-run average queueing delay per customer depends on the service distribution through its mean and variance. Indeed, if$\dot { \mu }$ is the mean service time, and$\sigma ^ { 2 }$ is the variance of a service time, then the average amount of time that a customer spends waiting in queue is given by 

$$
\frac {\lambda (\mu^ {2} + \sigma^ {2})}{2 (1 - \lambda \mu)}
$$

provided that$\lambda \mu ~ < ~ 1$ , where λ is the arrival rate. (The average delay is infinite if$\lambda \mu \geq 1 . )$ As can be seen by this formula, the average delay is quite large when$\mu$ is only slightly smaller than 1/λ, where, since λ is the arrival rate, 1/λ is the average time between arrivals. 

Suppose that the owner of a service station will hire a second server if it can be shown that the average service time exceeds 8 minutes. The following data give the service times (in minutes) of 28 customers of this queueing system. Do they indicate that the mean service time is greater than 8 minutes? 

8.6, 9.4, 5.0, 4.4, 3.7, 11.4, 10.0, 7.6, 14.4, 12.2, 11.0, 14.4, 9.3, 10.5, 

10.3, 7.7, 8.3, 6.4, 9.2, 5.7, 7.9, 9.4, 9.0, 13.3, 11.6, 10.0, 9.5, 6.6 

SOLUTION Let us use the preceding data to test the null hypothesis that the mean service time is less than or equal to 8 minutes. A small p-value will then be strong evidence that the mean service time is greater than 8 minutes. Running Program 8.3.2 on these data shows that the value of the test statistic is 2.257, with a resulting p-value of .016. Such a small p-value is certainly strong evidence that the mean service time exceeds 8 minutes. ■ 

Table 8.2 summarizes the tests of this subsection. 


TABLE 8.2 $X _ { 1 } , \ldots , X _ { n }$ Is a Sample from a$\mathcal { N } ( \mu , \sigma ^ { 2 } )$ Population$\sigma ^ { 2 }$ Is Unknown$\overline { { { X } } } = \sum _ { i = 1 } ^ { n } X _ { i } / n$$S ^ { 2 } = \sum _ { i = 1 } ^ { n } ( X _ { i } - { \overline { { X } } } ) ^ { 2 } / ( n - 1 )$


<table><tr><td><eq>H_0</eq></td><td><eq>H_1</eq></td><td>TestStatistic TS</td><td>SignificanceLevel α Test</td><td>p-Value ifTS = t</td></tr><tr><td>μ = μ0</td><td>μ ≠ μ0</td><td><eq>\sqrt{n}(\overline{X} - \mu_0)/S</eq></td><td>Reject if |TS| &gt; <eq>t_{\alpha/2,n-1}</eq></td><td><eq>2P\{T_{n-1} \geq |t|\}</eq></td></tr><tr><td>μ ≤ μ0</td><td>μ &gt; μ0</td><td><eq>\sqrt{n}(\overline{X} - \mu_0)/S</eq></td><td>Reject if TS &gt; <eq>t_{\alpha,n-1}</eq></td><td><eq>P\{T_{n-1} \geq t\}</eq></td></tr><tr><td>μ ≥ μ0</td><td>μ &lt; μ0</td><td><eq>\sqrt{n}(\overline{X} - \mu_0)/S</eq></td><td>Reject if TS &lt; <eq>-t_{\alpha,n-1}</eq></td><td><eq>P\{T_{n-1} \leq t\}</eq></td></tr></table>


$T _ { n - 1 }$ is a t-random variable with n − 1 degrees of freedom:$P \{ T _ { n - 1 } > t _ { \alpha , n - 1 } \} = \alpha .$ 


## 8.4 TESTING THE EQUALITY OF MEANS OF TWO NORMAL POPULATIONS

A common situation faced by a practicing engineer is one in which she must decide whether two different approaches lead to the same solution. Often such a situation can be modeled as a test of the hypothesis that two normal populations have the same mean value. 

## 8.4.1 Case of Known Variances

Suppose that $X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { m }$ are independent samples from normal populations having unknown means$\mu _ { x }$ and$\mu _ { y }$ but known variances$\sigma _ { x } ^ { 2 }$ and$\sigma _ { y } ^ { 2 }$ . Let us consider the problem of testing the hypothesis 

$$
H _ {0}: \mu_ {x} = \mu_ {y}
$$

versus the alternative 

$$
H _ {1}: \mu_ {x} \neq \mu_ {y}
$$

Since$\overline { { X } }$ is an estimate of$\mu _ { x }$ and$\overline { { Y } }$ of$\mu _ { y }$ , it follows that ${ \overline { { X } } } - { \overline { { Y } } }$ can be used to estimate$\mu _ { x } - \mu _ { y }$ . Hence, because the null hypothesis can be written as $H _ { 0 } : \mu _ { x } - \mu _ { y } = 0$ , it seems reasonable to reject it when ${ \overline { { X } } } - { \overline { { Y } } }$ is far from zero. That is, the form of the test should be to 

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

Hence, when $H _ { 0 }$ is true (and so$\mu _ { x } - \mu _ { y } = 0 )$ , it follows that 

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

EXAMPLE 8.4a Two new methods for producing a tire have been proposed. To ascertain which is superior, a tire manufacturer produces a sample of 10 tires using the first method and a sample of 8 using the second. The first set is to be road tested at location A and the second at location B. It is known from past experience that the lifetime of a tire that is road tested at one of these locations is normally distributed with a mean life due to the tire but with a variance due (for the most part) to the location. Specifically, it is known that the lifetimes of tires tested at location A are normal with standard deviation equal to 4,000 kilometers, whereas those tested at location B are normal with$\sigma = 6 { , } 0 0 0$ kilometers. If the manufacturer is interested in testing the hypothesis that there is no appreciable difference in the mean life of tires produced by either method, what conclusion should be drawn at the 5 percent level of significance if the resulting data are as given in Table 8.3? 


TABLE 8.3 Tire Lives in Units of 100 Kilometer


<table><tr><td>Tires Tested at A</td><td>Tires Tested at B</td></tr><tr><td>61.1</td><td>62.2</td></tr><tr><td>58.2</td><td>56.6</td></tr><tr><td>62.3</td><td>66.4</td></tr><tr><td>64</td><td>56.2</td></tr><tr><td>59.7</td><td>57.4</td></tr><tr><td>66.2</td><td>58.4</td></tr><tr><td>57.8</td><td>57.6</td></tr><tr><td>61.4</td><td>65.4</td></tr><tr><td>62.2</td><td></td></tr><tr><td>63.6</td><td></td></tr></table>

SOLUTION A simple computation (or the use of Program 8.4.1) shows that the value of the test statistic is .066. For such a small value of the test statistic (which has a standard normal distribution when $H _ { 0 }$ is true), it is clear that the null hypothesis is accepted. ■ 

It follows from Equation 8.4.1 that a test of the hypothesis $H _ { 0 } : \mu _ { x } = \mu _ { y }$ (or $H _ { 0 }$ :$\mu _ { x } \leq \mu _ { y } )$ against the one-sided alternative $H _ { 1 } : \mu _ { x } > \mu _ { y }$ would be to 

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

To determine a significance level α test of $H _ { 0 }$ we will need to make the additional assumption that the unknown variances$\sigma _ { x } ^ { 2 }$ and$\sigma _ { y } ^ { 2 }$ are equal. Let$\sigma ^ { 2 }$ denote their value — that is, 

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


where $S _ { \ / p } ^ { 2 }$ , the pooled estimator of the common variance$\sigma ^ { 2 } { } _ { ; }$ , is given by 

$$
S _ {p} ^ {2} = \frac {(n - 1) S _ {x} ^ {2} + (m - 1) S _ {y} ^ {2}}{n + m - 2}
$$

Hence, when $H _ { 0 }$ is true, and so$\mu _ { x } - \mu _ { y } = 0$ , the statistic 

$$
T \equiv \frac {\overline {{X}} - \overline {{Y}}}{\sqrt {S _ {p} ^ {2} (1 / n + 1 / m)}}
$$

has a t -distribution with $n + m - 2$ degrees of freedom. From this, it follows that we can test the hypothesis that$\mu _ { x } = \mu _ { y }$ as follows: 

$$
\begin{array}{l l l l} \text {accept} & H _ {0} & \text {if} & | T | \leq t _ {\alpha / 2, n + m - 2} \\ \text {reject} & H _ {0} & \text {if} & | T | > t _ {\alpha / 2, n + m - 2} \end{array}
$$

where $t _ { \alpha / 2 , n + m - 2 }$ is the 100$\alpha / 2$ percentile point of a t-random variable with $n + m - 2$ degrees of freedom (see Figure 8.5). 

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

where$\mu _ { c }$ is the mean time a cold lasts when the vitamin C tablets are taken and$\mu _ { \ / p }$ is the mean time when the placebo is taken. Assuming that the variance of the length of the cold is the same for the vitamin C patients and the placebo patients, we test the above by running Program 8.4.2. This yields the information shown in Figure 8.6. Thus $H _ { 0 }$ would be rejected at the 5 percent level of significance. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/5806cf4e510b4afe232f0e028f131fc391d58986b07976774d101baaeedc4037.jpg)



FIGURE 8.6


Of course, if it were not convenient to run Program 8.4.2 then we could have performed the test by first computing the values of the statistics X ,$\overline { { Y } } , S _ { x } ^ { 2 } , S _ { y } ^ { 2 }$ , and $S _ { \ / P } ^ { 2 }$ . where the X sample corresponds to those receiving vitamin C and the $Y$ sample to those receiving a placebo. These computations would give the value 

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

Let us now suppose that the population variances$\sigma _ { x } ^ { 2 }$ and$\sigma _ { \gamma } ^ { 2 }$ are not only unknown but also cannot be considered to be equal. In this situation, since $S _ { x } ^ { 2 }$ is the natural estimator of$\sigma _ { x } ^ { 2 }$ and $S _ { y } ^ { 2 }$ of$\sigma _ { y } ^ { 2 }$ , it would seem reasonable to base our test of 

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


TABLE 8.4 $X _ { 1 } , \ldots , X _ { n }$ Is a Sample from a$\mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } )$ Population;$Y _ { 1 } , \dots , Y _ { m }$ Is a Sample from$\mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$ Population



The Two Population Samples Are Independent To Test



$H _ { 0 } : \mu _ { 1 } = \mu _ { 2 }$ versus $H _ { 0 } : \mu _ { 1 } \neq \mu _ { 2 }$


<table><tr><td>Assumption</td><td>Test Statistic TS</td><td>Significance Level <eq>\alpha</eq> Test</td><td><eq>p</eq>-Value if <eq>TS = t</eq></td></tr><tr><td><eq>\sigma_1, \sigma_2</eq> known</td><td><eq>\frac{\overline{X}-\overline{Y}}{\sqrt{\sigma_1^2/n+\sigma_2^2/m}}</eq></td><td>Reject if <eq>|TS| &gt; z_{\alpha/2}</eq></td><td><eq>2P\{Z \geq |t|\}</eq></td></tr><tr><td><eq>\sigma_1 = \sigma_2</eq></td><td><eq>\frac{\overline{X}-\overline{Y}}{\sqrt{\frac{(n-1)S_1^2+(m-1)S_2^2}{n+m-2}\sqrt{1/n+1/m}}}</eq></td><td>Reject if <eq>|TS| &gt; t_{\alpha/2,n+m-2}</eq></td><td><eq>2P\{T_{n+m-2} \geq |t|\}</eq></td></tr><tr><td><eq>n, m</eq> large</td><td><eq>\frac{\overline{X}-\overline{Y}}{\sqrt{S_1^2/n+S_2^2/m}}</eq></td><td>Reject if <eq>|TS| &gt; z_{\alpha/2}</eq></td><td><eq>2P\{Z \geq |t|\}</eq></td></tr></table>

## 8.4.4 The Paired <sub>t</sub>-Test

Suppose we are interested in determining whether the installation of a certain antipollution device will affect a car’s mileage. To test this, a collection of n cars that do not have this device are gathered. Each car’s mileage per gallon is then determined both before and after the device is installed. How can we test the hypothesis that the antipollution control has no effect on gas consumption? 

The data can be described by the n pairs $( X _ { i } , Y _ { i } ) , i = 1 , . . . , n$ , where $X _ { i }$ is the gas consumption of the ith car before installation of the pollution control device, and $Y _ { i }$ of the same car after installation. It is important to note that, since each of the n cars will be inherently different, we cannot treat $X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { n }$ as being independen samples. For example, if we know that $X _ { 1 }$ is large (say, 40 miles per gallon), we would certainly expect that $Y _ { 1 }$ would also probably be large. Thus, we cannot employ the earlier methods presented in this section. 

One way in which we can test the hypothesis that the antipollution device does not affect gas mileage is to let the data consist of each car’s difference in gas mileage. That is, let $W _ { i } = X _ { i } - Y _ { i } , i = 1 , . . . , n .$ . Now, if there is no effect from the device, it should follow that the $W _ { i }$ would have mean 0. Hence, we can test the hypothesis of no effect by testing 

$$
H _ {0}: \mu_ {w} = 0 \qquad \text { versus } \qquad H _ {1}: \mu_ {w} \neq 0
$$

where $W _ { 1 } , \ldots , W _ { n }$ are assumed to be a sample from a normal population having unknown mean$\mu _ { w }$ and unknown variance$\sigma _ { w } ^ { 2 }$ . But the t-test described in Section 8.3.2 shows that 

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

Let $X _ { 1 } , \ldots , X _ { n }$ denote a sample from a normal population having unknown mean$\mu$ and unknown variance$\sigma ^ { 2 }$ , and suppose we desire to test the hypothesis 

$$
H _ {0}: \sigma^ {2} = \sigma_ {0} ^ {2}
$$

versus the alternative 

$$
H _ {1}: \sigma^ {2} \neq \sigma_ {0} ^ {2}
$$

for some specified value$\sigma _ { 0 } ^ { 2 }$ 

To obtain a test, recall (as was shown in Section 6.5) that $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 }$ has a chi-square distribution with $n - 1$ degrees of freedom. Hence, when $H _ { 0 }$ is true 

$$
\frac {(n - 1) S ^ {2}}{\sigma_ {0} ^ {2}} \sim \chi_ {n - 1} ^ {2}
$$

and so 

$$
P _ {H _ {0}} \left\{\chi_ {1 - \alpha / 2, n - 1} ^ {2} \leq \frac {(n - 1) S ^ {2}}{\sigma_ {0} ^ {2}} \leq \chi_ {\alpha / 2, n - 1} ^ {2} \right\} = 1 - \alpha
$$

Therefore, a significance level$\alpha$ test is to 

$$
\begin{array}{l l} \text {   accept   } & H _ {0} \quad \text {   if   } \quad \chi_ {1 - \alpha / 2, n - 1} ^ {2} \leq \frac {(n - 1) S ^ {2}}{\sigma_ {0} ^ {2}} \leq \chi_ {\alpha / 2, n - 1} ^ {2} \\ \text {   reject   } & H _ {0} \quad \text {   otherwise   } \end{array}
$$

The preceding test can be implemented by first computing the value of the test statistic $( n - 1 ) \bar { S } ^ { 2 } / \sigma _ { 0 } ^ { 2 }$ — call it $c .$ . Then compute the probability that a chi-square random variable with $n - 1$ degrees of freedom would be (a) less than and (b) greater than $c .$ If either of these probabilities is less than$\alpha / 2$ , then the hypothesis is rejected. In other words, the p-value of the test data is 

$$
p \mathrm{-value} = 2 \min (P \{\chi_ {n - 1} ^ {2} <   c \}, 1 - P \{\chi_ {n - 1} ^ {2} <   c \})
$$

The quantity $P \{ \chi _ { n - 1 } ^ { 2 } ~ < ~ c \}$ can be obtained from Program 5.8.1.A. The$\phi \mathrm { \cdot }$ -value for a one-sided test is similarly obtained. 

EXAMPLE 8.5a A machine that automatically controls the amount of ribbon on a tape ha recently been installed. This machine will be judged to be effective if the standard deviation$\sigma$ of the amount of ribbon on a tape is less than .15 cm. If a sample of 20 tapes yields a sample variance of $S ^ { 2 } = . 0 2 5 \mathrm { c m } ^ { 2 }$ , are we justified in concluding that the machine is ineffective? 

SOLUTION$\mathbb { W } \mathrm { e }$ will test the hypothesis that the machine is effective, since a rejection of this hypothesis will then enable us to conclude that it is ineffective. Since we are thus interested in testing 

$$
H _ {0}: \sigma^ {2} \leq . 0 2 2 5 \quad \text { versus } \quad H _ {1}: \sigma^ {2} >. 0 2 2 5
$$

it follows that we would want to reject $H _ { 0 }$ when $S ^ { 2 }$ is large. Hence, the$\scriptstyle { p - { \frac { } { } } }$ -value of the preceding test data is the probability that a chi-square random variable with 19 degrees of freedom would exceed the observed value of $1 9 S ^ { 2 } / . 0 2 2 5 = 1 9 \times . 0 2 5 / . 0 2 2 5 = 2 1 . 1 1 1$ That is, 

$$
\begin{array}{r l} p \text {-value} & = P \{\chi_ {1 9} ^ {2} > 2 1. 1 1 1 \} \\ & = 1 -. 6 6 9 3 = . 3 3 0 7 \quad \text {from Program 5.8.1.A} \end{array}
$$

Therefore, we must conclude that the observed value of $S ^ { 2 } = . 0 2 5$ is not large enough to reasonably preclude the possibility that$\sigma ^ { 2 } \leq . 0 2 2 5$ , and so the null hypothesis is accepted. ■ 

## 8.5.1 Testing for the Equality of Variances of Two Normal Populations

Let $X _ { 1 } , \ldots , X _ { n }$ and $Y _ { 1 } , \dots , Y _ { m }$ denote independent samples from two normal populations having respective (unknown) parameters$\mu _ { x } , \sigma _ { x } ^ { 2 }$ and$\bar { \mu _ { y } , \sigma _ { y } ^ { 2 } }$ and consider a test of 

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

denote the sample variances, then as shown in Section $6 . 5 , ( n - 1 ) S _ { x } ^ { 2 } / \sigma _ { x } ^ { 2 }$ and $( m - 1 ) S _ { y } ^ { 2 } / \sigma _ { y } ^ { 2 }$ are independent chi-square random variables with $n - 1$ and $m - 1$ degrees of freedom, respectively. Therefore,$( S _ { x } ^ { 2 } / \sigma _ { x } ^ { 2 } ) / ( S _ { y } ^ { 2 } / \sigma _ { y } ^ { 2 } )$ has an $F .$ -distribution with parameters $n - 1$ and $m - 1$ . Hence, when $H _ { 0 }$ is true 

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

The preceding test can be effected by first determining the value of the test statistic $S _ { x } ^ { 2 } / S _ { y } ^ { 2 }$ , say its value is$\nu ,$ and then computing $P \{ F _ { n - 1 , m - 1 } \ \leq \ \nu \}$ where $F _ { n - 1 , m - 1 }$ is an F -random variable with parameters $n - 1 , m - 1$ . If this probability is either less than α/2 (which occurs when$\hat { S } _ { x } ^ { 2 }$ is significantly less than $S _ { y } ^ { 2 } )$ or greater than $1 - \alpha / 2$ (which occurs when $S _ { x } ^ { 2 }$ is significantly greater than $S _ { y } ^ { 2 } )$ ), then the hypothesis is rejected. In other words, the$\scriptstyle { p - { \frac { } { } } }$ -value of the test data is 

$$
p \text {-value} = 2 \min (P \{F _ {n - 1, m - 1} <   v \}, 1 - P \{F _ {n - 1, m - 1} <   v \})
$$

The test now calls for rejection whenever the significance level$\alpha$ is at least as large as the p-value. 

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

The binomial distribution is frequently encountered in engineering problems. For a typical example, consider a production process that manufactures items that can be classified in one of two ways — either as acceptable or as defective. An assumption often made is that each item produced will, independently, be defective with probability$\mathbf { \nabla } ^ { p ; }$ and so the number of defects in a sample of n items will thus have a binomial distribution with parameters $( n , p )$ . We will now consider a test of 

$$
H _ {0}: p \leq p _ {0} \quad \text { versus } \quad H _ {1}: p > p _ {0}
$$

where$\mathit { p 0 }$ is some specified value. 

If we let $X$ denote the number of defects in the sample of size n, then it is clear that we wish to reject $H _ { 0 }$ when X is large. To see how large it need be to justify rejection at the α level of significance, note that 

$$
P \{X \geq k \} = \sum_ {i = k} ^ {n} P \{X = i \} = \sum_ {i = k} ^ {n} {\binom {n} {i}} p ^ {i} (1 - p) ^ {n - i}
$$

Now it is certainly intuitive (and can be proven) that $P \{ X \geq k \}$ is an increasing function of$\dot { \boldsymbol { p } }$ — that is, the probability that the sample will contain at least $k$ errors increases in the defect probability$\scriptstyle { \boldsymbol { p } } .$ . Using this, we see that when $H _ { 0 }$ is true (and so$ { \boldsymbol { p } } \leq p _ { 0 } )$ ), 

$$
P \{X \geq k \} \leq \sum_ {i = k} ^ {n} {\binom {n} {i}} p _ {0} ^ {i} (1 - p _ {0}) ^ {n - i}
$$

Hence, a significance level α test of $H _ { 0 } : p \leq p _ { 0 }$ versus $H _ { 1 } : p > p _ { 0 }$ is to reject $H _ { 0 }$ when 

$$
X \geq k ^ {*}
$$

where $k ^ { * }$ is the smallest value of k for which$\begin{array} { r } { \sum _ { i = k } ^ { n } \binom { n } { i } \mathcal { P } _ { 0 } ^ { i } ( 1 - \mathcal { p } _ { 0 } ) ^ { n - i } \le \alpha } \end{array}$ . That is, 

$$
k ^ {*} = \min \left\{k: \sum_ {i = k} ^ {n} {\binom {n} {i}} p _ {0} ^ {i} (1 - p _ {0}) ^ {n - i} \leq \alpha \right\}
$$

This test can best be performed by first determining the value of the test statistic — say,$X = x -$ and then computing the p-value given by 

$$
\begin{array}{l} p \text {-value} = P \{B (n, p _ {0}) \geq x \} \\ = \sum_ {i = x} ^ {n} \binom {n} {i} p _ {0} ^ {i} (1 - p _ {0}) ^ {n - i} \end{array}
$$

EXAMPLE 8.6a A computer chip manufacturer claims that no more than 2 percent of the chips it sends out are defective. An electronics company, impressed with this claim, has purchased a large quantity of such chips. To determine if the manufacturer’s claim can be taken literally, the company has decided to test a sample of 300 of these chips. If 10 of these 300 chips are found to be defective, should the manufacturer’s claim be rejected? 

SOLUTION Let us test the claim at the 5 percent level of significance. To see if rejection is called for, we need to compute the probability that the sample of size 300 would have resulted in 10 or more defectives when$\boldsymbol { \mathscr { P } }$ is equal to .02. (That is, we compute the p-value.) If this probability is less than or equal to .05, then the manufacturer’s claim 

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

EXAMPLE 8.6b In Example 8.6a,$n p _ { 0 } = 3 0 0 ( . 0 2 ) = 6 { } _ { ; }$ , and$\sqrt { n p _ { 0 } ( 1 - p _ { 0 } ) } = \sqrt { 5 . 8 8 } .$ Consequently, the p-value that results from the data $X = 1 0$ is 

$$
\begin{array}{r l} p \text {-value} & = P _ {. 0 2} \{X \geq 1 0 \} \\ & = P _ {. 0 2} \{X \geq 9. 5 \} \\ & = P _ {. 0 2} \left\{\frac {X - 6}{\sqrt {5 . 8 8}} \geq \frac {9 . 5 - 6}{\sqrt {5 . 8 8}} \right\} \\ & \approx P \{Z \geq 1. 4 4 3 \} \\ & = . 0 7 4 5 \end{array}
$$

Suppose now that we want to test the null hypothesis tha$\boldsymbol { \mathscr { P } }$ is equal to some specified value; that is, we want to test 

$$
H _ {0}: p = p _ {0} \quad \text { versus } \quad H _ {1}: p \neq p _ {0}
$$

If $X ,$ , a binomial random variable with parameters n and ${ \boldsymbol { p } } ,$ is observed to equal $x ,$ then a significance level α test would reject $H _ { 0 }$ if the value x was either significantly larger or significantly smaller than what would be expected when$\boldsymbol { \mathscr { P } }$ is equal to$\mathit { p 0 }$ . More precisely, the test would reject $H _ { 0 }$ if either 

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

where$\boldsymbol { \underline { P } }$ is the probability that an item is defective. The p-value of the observed data of 16 defectives in 500 items is 

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

Suppose there are two distinct methods for producing a certain type of transistor; and suppose that transistors produced by the first method will, independently, be defective with probability$\displaystyle { \phi _ { 1 } }$ , with the corresponding probability being$\hbar 2$ for those produced by the second method. To test the hypothesis that $p _ { 1 } = p _ { 2 }$ , a sample of$\displaystyle n _ { 1 }$ transistors is produced using method 1 and$\boldsymbol { n _ { 2 } }$ using method 2. 

Let $X _ { 1 }$ denote the number of defective transistors obtained from the first sample and $X _ { 2 }$ for the second. Thus,$X _ { 1 }$ and $X _ { 2 }$ are independent binomial random variables with respective parameters $( n _ { 1 } , p _ { 1 } )$ and $( n _ { 2 } , p _ { 2 } )$ . Suppose that $X _ { 1 } + X _ { 2 } = k$ and so there have been a total of $k$ defectives. Now, if $H _ { 0 }$ is true, then each of the $n _ { 1 } + n _ { 2 }$ transistors produced will have the same probability of being defective, and so the determination of the $k$ defectives will have the same distribution as a random selection of a sample of size $k$ from a population of $n _ { 1 } + n _ { 2 }$ items of which$\displaystyle n _ { 1 }$ are white and$\boldsymbol { n _ { 2 } }$ are black. In other words, given a total of $k$ defectives, the conditional distribution of the number of defective transistors obtained from method 1 will, when $H _ { 0 }$ is true, have the following hypergeometric distribution*: 

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

EXAMPLE 8.6e In 1970, the researchers Herbst, Ulfelder, and Poskanzer (H-U-P) sus pected that vaginal cancer in young women, a rather rare disease, might be caused by one’s mother having taken the drug diethylstilbestrol (usually referred to as DES) while pregnant. To study this possibility, the researchers could have performed an observational study by searching for a (treatment) group of women whose mothers took DES when pregnant and a (control) group of women whose mothers did not. They could then observe these groups for a period of time and use the resulting data to test the hypoth esis that the probabilities of contracting vaginal cancer are the same for both groups. However, because vaginal cancer is so rare (in both groups) such a study would require a large number of individuals in both groups and would probably have to continue for many years to obtain significant results. Consequently, H-U-P decided on a different type of observational study. They uncovered 8 women between the ages of 15 and 22 who had vaginal cancer. Each of these women (called cases) was then matched with 4 others, called referents or controls. Each of the referents of a case was free of the cancer and was born within 5 days in the same hospital and in the same type of room (either private or public) as the case. Arguing that if DES had no effect on vaginal cancer then the probability, call it$\mathit { p _ { c } }$ , that the mother of a case took DES would be the same as the probability, call it ${ \boldsymbol { p } } _ { r }$ , that the mother of a referent took DES, the researchers H-U-P decided to test 

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

where $P _ { \lambda _ { 0 } }$ means that the probability is computed under the assumption that the Poisson mean is$\lambda _ { 0 }$ . It follows from Equation 8.7.1 that the p-value is given by 

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

Let $X _ { 1 }$ and $X _ { 2 }$ be independent Poisson random variables with respective means$\lambda _ { 1 }$ and$\lambda _ { 2 }$ , and consider a test of 

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

It follows from Proposition 8.7.1 that, if $H _ { 0 }$ is true, then the conditional distribution of $X _ { 1 }$ given that $X _ { 1 } + X _ { 2 } = n$ is the binomial distribution with parameters n and$\displaystyle { \phi = 1 / ( 1 + c ) }$ From this we can conclude that if $X _ { 1 } + X _ { 2 } = n _ { \cdot }$ , then $H _ { 0 }$ should be rejected if the observed value of $X _ { 1 }$ , call it $x _ { 1 }$ , is such that either 

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

where$\lambda _ { i } \equiv E [ X _ { i } ] , i = 1 , 2$ . Hence, as $X _ { 1 } = 1 3 3 , X _ { 2 } = 1 4 9$ it follows that the p-value of the test of 

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

To determine a test, note that each error can be classified as being of one of 4 types: it is type 1 if it is found by both proofreaders; it is type 2 if found by A but not by B; it i type 3 if found by B but not by$\operatorname { A } ;$ and it is type 4 if found by neither. Thus, under our independence assumptions, it follows that each error will independently be type i with probability$\mathbf { \nabla } _ { \mathbf { \mathit { p } } _ { i } }$ , where 

$$
p _ {1} = P _ {A} P _ {B}, \quad p _ {2} = P _ {A} (1 - P _ {B}), \quad p _ {3} = (1 - P _ {A}) P _ {B}, \quad p _ {4} = (1 - P _ {A}) (1 - P _ {B})
$$

Now, if we do our analysis under the assumption that N , the total number of errors in the manuscript, is a random variable that is Poisson distributed with some unknown mean$\lambda ,$ , then it follows from the results of Section 5.2 that the numbers of errors of types 1, 2, 3, 4 are independent Poisson random variables with respective means$\lambda p _ { 1 } , \lambda p _ { 2 } , \lambda p _ { 3 } , \lambda p _ { 4 }$ Now, because$\textstyle { \frac { x } { 1 - x } } = { \frac { 1 } { 1 / x - 1 } }$ is an increasing function of x in the region $0 \leq x \leq 1$ 

$$
P _ {A} > P _ {B} \Leftrightarrow \frac {P _ {A}}{1 - P _ {A}} > \frac {P _ {B}}{1 - P _ {B}} \Leftrightarrow P _ {A} (1 - P _ {B}) > (1 - P _ {A}) P _ {B}
$$

In other words,$P _ { A } > P _ { B }$ if and only$\mathrm { { f } } _ { \mathit { p } _ { 2 } } > _ { \mathit { p } _ { 3 } }$ . As a result, it suffices to use the data to test 

$$
H _ {0}: p _ {2} \leq p _ {3} \quad \text { versus } \quad H _ {1}: p _ {2} > p _ {3}
$$

Therefore, with $N _ { 2 }$ denoting the number of errors of type 2 (that is, the number of errors found by A but not by B), and $N _ { 3 }$ the number of errors of type 3 (that is, the number found by B but not by A), it follows that we need to test 

$$
H _ {0}: E [ N _ {2} ] \leq E [ N _ {3} ] \quad \text { versus } \quad H _ {1}: E [ N _ {2} ] > E [ N _ {3} ]\tag{8.7.2}
$$

where $N _ { 2 }$ and $N _ { 3 }$ are independent Poisson random variables. Now, by Proposition 8.7.1, the conditional distribution of $N _ { 2 }$ given $N _ { 2 } + N _ { 3 }$ is binomial $( n , p )$ ) where $n = N _ { 2 } + N _ { 3 }$ and$\begin{array} { r } { \hat { p } = ( E [ N _ { 2 } ] ) / ( E [ N _ { 2 } ] + E [ N _ { 3 } ] ) } \end{array}$ . Because Equation 8.7.2 is equivalent to 

$$
H _ {0}: p \leq 1 / 2 \quad \text { versus } \quad H _ {1}: p > 1 / 2
$$

it follows that the p-value that results when $N _ { 2 } = n _ { 2 } , N _ { 3 } = n _ { 3 }$ is 

$$
p \text {-value} = P \{\operatorname{Bin} (n _ {2} + n _ {3},. 5) \geq n _ {2} \}
$$

For the data given,$n _ { 2 } = 1 8 , n _ { 3 } = 8$ , yielding that 

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

(b) What about at the$\alpha = . 0 5$ level of significance? 

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

8. Verify that the approximation in Equation 8.3.7 remains valid even when$\mu _ { 1 } < \mu _ { 0 }$ 

9. A British pharmaceutical company, Glaxo Holdings, has recently developed a new drug for migraine headaches. Among the claims Glaxo made for its drug, called somatriptan, was that the mean time it takes for it to enter the bloodstream is less than 10 minutes. To convince the Food and Drug Administration of the validity of this claim, Glaxo conducted an experiment on a randomly chosen set of migraine sufferers. To prove its claim, what should they have taken as the null and what as the alternative hypothesis? 

10. The weights of salmon grown at a commercial hatchery are normally distributed with a standard deviation of 1.2 pounds. The hatchery claims that the mean weight of this year’s crop is at least 7.6 pounds. Suppose a random sample of 16 fish yielded an average weight of 7.2 pounds. Is this strong enough evidence to reject the hatchery’s claims at the 

(a) 5 percent level of significance; 

(b) 1 percent level of significance? 

(c) What is the p-value? 

11. Consider a test of $H _ { 0 } : \mu \le 1 0 0$ versus $H _ { 1 } : \mu > 1 0 0$ . Suppose that a sample of size 20 has a sample mean of$\overline { { X } } = 1 0 5$ . Determine the p-value of this outcome if the population standard deviation is known to equal (a) 5; (b) 10; (c) 15. 

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

Let$\mu _ { 1 }$ and$\mu _ { 2 }$ be the respective means of the two populations. Find the p-value of the test of the null hypothesis 

$$
H _ {0}: \mu_ {1} \leq \mu_ {2}
$$

versus the alternative 

$$
H _ {1}: \mu_ {1} > \mu_ {2}
$$

<table><tr><td>Type 1</td><td>32,84,37,42,78,62,59,74</td></tr><tr><td>Type 2</td><td>39,111,55,106,90,87,85</td></tr></table>

when the population standard deviations are$\sigma _ { 1 } = 1 0$ and (a)$\sigma _ { 2 } = 5 ; \left( \mathbf { b } \right) \sigma _ { 2 } = 1 0 ; \left( \mathbf { c } \right) \sigma _ { 2 } = 2 0 .$ 

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

44. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population having unknown parameters µ and$\sigma ^ { 2 }$ , devise a significance level α test of 

$$
H _ {0} = \sigma^ {2} \leq \sigma_ {0} ^ {2}
$$

versus the alternative 

$$
H _ {1} = \sigma^ {2} > \sigma_ {0} ^ {2}
$$

for a given positive value$\sigma _ { 0 } ^ { 2 }$ . 

45. In Problem 44, explain how the test would be modified if the population mean µ were known in advance. 

46. A gun-like apparatus has recently been designed to replace needles in administering vaccines. The apparatus can be set to inject different amounts of the serum, but because of random fluctuations the actual amount injected is normally distributed with a mean equal to the setting and with an unknown variance$\sigma ^ { 2 }$ . It has been decided that the apparatus would be too dangerous to use if σ exceeds .10. If a random sample of 50 injections resulted in a sample standard deviation of .08, should use of the new apparatus be discontinued? Suppose the level of significance is$\alpha = . 1 0$ . Comment on the appropriate choice of a significance level for this problem, as well as the appropriate choice of the null hypothesis. 

47. A pharmaceutical house produces a certain drug item whose weight has a standard deviation of .5 milligrams. The company’s research team has proposed a new method of producing the drug. However, this entails some costs and will be adopted only if there is strong evidence that the standard deviation of the weight of the items will drop to below .4 milligrams. If a sample of 10 items is produced and has the following weights, should the new method be adopted? 

<table><tr><td>5.728</td><td>5.731</td></tr><tr><td>5.722</td><td>5.719</td></tr><tr><td>5.727</td><td>5.724</td></tr><tr><td>5.718</td><td>5.726</td></tr><tr><td>5.723</td><td>5.722</td></tr></table>

48. The production of large electrical transformers and capacitators requires the use of polychlorinated biphenyls (PCBs), which are extremely hazardous when released into the environment. Two methods have been suggested to monitor the levels of PCB in fish near a large plant. It is believed that each method will result in a normal random variable that depends on the method. Test the hypothesis at the α = .10 level of significance that both methods have the same variance, if a given fish is checked 8 times by each method with the following data (in parts per million) recorded. 

<table><tr><td>Method 1</td><td>6.2, 5.8, 5.7, 6.3, 5.9, 6.1, 6.2, 5.7</td></tr><tr><td>Method 2</td><td>6.3, 5.7, 5.9, 6.4, 5.8, 6.2, 6.3, 5.5</td></tr></table>

49. In Problem 31, test the hypothesis that the populations have the same variances. 

50. If $X _ { 1 } , \ldots , X _ { n }$ is a sample from a normal population with variance$\sigma _ { x } ^ { 2 }$ , and $Y _ { 1 } , \dots , Y _ { n }$ is an independent sample from normal population with variance$\sigma _ { y } ^ { 2 }$ develop a significance level α test of 

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

where$\sim$ means “approximately has the distribution.” 

(b) Now argue that when $H _ { 0 }$ is true and so$\ b { \mathscr { P } } 1 = \ b { \mathscr { p } } 2$ , their common value can be best estimated by $( X _ { 1 } + X _ { 2 } ) / ( n _ { 1 } + n _ { 2 } )$ 

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


70. For the following data, sample 1 is from a Poisson distribution with mean$\lambda _ { 1 }$ and sample 2 is from a Poisson distribution with mean$\lambda _ { 2 }$ . Test the hypothesis that$\lambda _ { 1 } = \lambda _ { 2 }$ 

<table><tr><td>Sample 1</td><td>24, 32, 29, 33, 40, 28, 34, 36</td></tr><tr><td>Sample 2</td><td>42, 36, 41</td></tr></table>

71. A scientist looking into the effect of smoking on heart disease has chosen a large random sample of smokers and of nonsmokers. She plans to study these two groups for 5 years to see if the number of heart attacks among the members of the smokers’ group is significantly greater than the number among the nonsmokers. Such a result, the scientist feels, should be strong evidence of an association between 

smoking and heart attacks. Given that 

1. Older people are at greater risk of heart disease than are younger people; and 2. As a group, smokers tend to be somewhat older than nonsmokers; 

would the scientist be justified in her conclusion? Explain how the experi mental design can be improved so that meaningful conclusions can be drawn. 

72. A researcher wants to analyze the average yearly increase in a stock over a 20 year period. To do so, she plans to randomly choose 100 stocks from the listing of current stocks, discarding any that were not in existence 20 years ago. She will then compare the current price of each stock with its price 20 years ago to determine its percentage increase. Do you think this is a valid method to study the average increase in the price of a stock? 

# REGRESSION

## 9.1 INTRODUCTION

Many engineering and scientific problems are concerned with determining a relationship between a set of variables. For instance, in a chemical process, we might be interested in the relationship between the output of the process, the temperature at which it occurs, and the amount of catalyst employed. Knowledge of such a relationship would enable us to predict the output for various values of temperature and amount of catalyst. 

In many situations, there is a single response variable Y , also called the dependent vari able, which depends on the value of a set of input, also called independent, variables $x _ { 1 } , \ldots , x _ { r }$ . The simplest type of relationship between the dependent variable Y and the input variables $x _ { 1 } , \ldots , x _ { r }$ is a linear relationship. That is, for some constants$\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { r }$ the equation 

$$
Y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {r} x _ {r}\tag{9.1.1}
$$

would hold. If this was the relationship between Y and the $x _ { i } , i = 1 , \ldots , r ,$ , then it would be possible (once the$\beta _ { i }$ were learned) to exactly predict the response for any set of input values. However, in practice, such precision is almost never attainable, and the most that one can expect is that Equation 9.1.1 would be valid subject to random error. By this we mean that the explicit relationship is 

$$
Y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {r} x _ {r} + e\tag{9.1.2}
$$

where $^ { e , }$ representing the random error, is assumed to be a random variable having mean 0. Indeed, another way of expressing Equation 9.1.2 is as follows: 

$$
E [ Y | \mathbf {x} ] = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {r} x _ {r}
$$

where$\mathbf { x } = ( x _ { 1 } , \ldots , x _ { r } )$ is the set of independent variables, and $E [ Y | \mathbf { x } ]$ is the expected response given the inputs x. 

Equation 9.1.2 is called a linear regression equation. We say that it describes the regression of Y on the set of independent variables $x _ { 1 } , \ldots , x _ { r }$ . The quantities$\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { r }$ are called the regression coefficients, and must usually be estimated from a set of data. A regression equation containing a single independent variable — that is, one in which $r = 1 -$ is called a simple regression equation, whereas one containing many independent variables is called a multiple regression equation. 

Thus, a simple linear regression model supposes a linear relationship between the mean response and the value of a single independent variable. It can be expressed as 

$$
Y = \alpha + \beta x + e
$$

where $_ x$ is the value of the independent variable, also called the input level, Y is the response, and $e ,$ representing the random error, is a random variable having mean 0. 

EXAMPLE 9.1a Consider the following 10 data pairs $( x _ { i } , y _ { i } ) , i = 1 , \dotsc , 1 0$ , relating y, the percent yield of a laboratory experiment, to x, the temperature at which the experiment was run. 

$$
\begin{array}{c c c c c c} i & x _ {i} & y _ {i} & i & x _ {i} & y _ {i} \\ 1 & 1 0 0 & 4 5 & 6 & 1 5 0 & 6 8 \\ 2 & 1 1 0 & 5 2 & 7 & 1 6 0 & 7 5 \\ 3 & 1 2 0 & 5 4 & 8 & 1 7 0 & 7 6 \\ 4 & 1 3 0 & 6 3 & 9 & 1 8 0 & 9 2 \\ 5 & 1 4 0 & 6 2 & 1 0 & 1 9 0 & 8 8 \end{array}
$$

A plot of$\dot { y } _ { i }$ versus x — called a scatter diagram — is given in Figure 9.1. As this scatter diagram appears to reflect, subject to random error, a linear relation between y and $x ,$ it seems that a simple linear regression model would be appropriate. ■ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/02b436b5420c116e736e8954a6b1cc2d13bf06fc7a2640db0e15540e28313e8e.jpg)



FIGURE 9.1 Scatter plot.


## 9.2 LEAST SQUARES ESTIMATORS OF THE REGRESSION PARAMETERS

Suppose that the responses $Y _ { i }$ corresponding to the input values $x _ { i } , i = 1 , \dotsc , n$ are to be observed and used to estimate α and$\beta$ in a simple linear regression model. To determine estimators of α and$\beta$ we reason as follows: If A is the estimator of α and B of$\dot { \boldsymbol { \beta } }$ , then the estimator of the response corresponding to the input variable $x _ { i }$ would be $A + B x _ { i }$ . Since the actual response is $Y _ { i : }$ , the squared difference is $( Y _ { i } - A - B x _ { i } ) ^ { 2 }$ , and so if A and B are the estimators of α and$\beta _ { i }$ , then the sum of the squared differences between the estimated responses and the actual response values — call it SS — is given by 

$$
S S = \sum_ {i = 1} ^ {n} (Y _ {i} - A - B x _ {i}) ^ {2}
$$

The method of least squares chooses as estimators of$\alpha$ and$\beta$ the values of $A$ and $B$ that minimize SS. To determine these estimators, we differentiate SS first with respect to A and then to $B$ as follows: 

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

Hence, using Equation 9.2.2 and the fact that$\begin{array} { r } { n \overline { { Y } } ~ = ~ \sum _ { i = 1 } ^ { n } Y _ { i } } \end{array}$ , we have proven the following proposition. 

PROPOSITION 9.2.1 The least squares estimators of$\beta$ and α corresponding to the data set $x _ { i } , Y _ { i } , i = 1 , \dotsc , n { \mathrm { ~ a r e } } .$ , respectively, 

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

To specify the distribution of the estimators A and $B ,$ it is necessary to make additional assumptions about the random errors aside from just assuming that their mean is 0. The usual approach is to assume that the random errors are independent normal random variables having mean 0 and variance$\sigma ^ { 2 }$ . That is, we suppose that if $Y _ { i }$ is the response corresponding to the input value $x _ { i } ,$ , then $Y _ { i } , \ldots , Y _ { n }$ are independent and 

$$
Y _ {i} \sim \mathcal {N} (\alpha + \beta x _ {i}, \sigma^ {2})
$$

Note that the foregoing supposes that the variance of the random error does not depend on the input value but rather is a constant. This value$\sigma ^ { 2 }$ is not assumed to be known but rather must be estimated from the data. 

Since the least squares estimator B of$\dot { \boldsymbol { { \beta } } }$ can be expressed as 

$$
B = \frac {\sum_ {i} (x _ {i} - \overline {{x}}) Y _ {i}}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}}\tag{9.3.1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/6c3b801d1a14ec3626fcda9733793a4ecc2b73506de19cd38a042add62ca9a6b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/7352daa3b71d1fa8cee326306c566f433d6474fa828c263a85e57198b91ed006.jpg)



FIGURE 9.3


we see that it is a linear combination of the independent normal random variables $Y _ { i } ,$$i = 1 , \ldots , n$ and so is itself normally distributed. Using Equation 9.3.1, the mean and variance of B are computed as follows: 

$$
\begin{array}{r} E [ B ] = \frac {\sum_ {i} (x _ {i} - \overline {{x}}) E [ Y _ {i} ]}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \\ = \frac {\sum_ {i} (x _ {i} - \overline {{x}}) (\alpha + \beta x _ {i})}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \end{array}
$$

$$
\begin{array}{r l} & = \frac {\alpha \sum_ {i} (x _ {i} - \overline {{x}}) + \beta \sum_ {i} x _ {i} (x _ {i} - \overline {{x}})}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \\ & = \beta \frac {\left[ \sum_ {i} x _ {i} ^ {2} - \overline {{x}} \sum_ {i} x _ {i} \right]}{\sum_ {i} x _ {i} ^ {2} - n \overline {{x}} ^ {2}} \quad \text {since} \sum_ {i} (x _ {i} - \overline {{x}}) = 0 \\ & = \beta \end{array}
$$

Thus $E [ B ] = \beta$ and so $B$ is an unbiased estimator of$\beta .$ . We will now compute the variance of $B .$ 

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

The quantities $Y _ { i } - A - B x _ { i } , i = 1 , \dots , n ,$ , which represent the differences between the actual responses (that is, the $Y _ { i } )$ and their least squares estimators (that is,$A + B x _ { i } )$ are called the residuals. The sum of squares of the residuals 

$$
S S _ {R} = \sum_ {i = 1} ^ {n} (Y _ {i} - A - B x _ {i}) ^ {2}
$$

can be utilized to estimate the unknown error variance$\sigma ^ { 2 }$ . Indeed, it can be shown that 

$$
\frac {S S _ {R}}{\sigma^ {2}} \sim \chi_ {n - 2} ^ {2}
$$

That is,$S S _ { R } / \sigma ^ { 2 }$ has a chi-square distribution with $n - 2$ degrees of freedom, which implies that 

$$
E \left[ \frac {S S _ {R}}{\sigma^ {2}} \right] = n - 2
$$

or 

$$
E \left[ \frac {S S _ {R}}{n - 2} \right] = \sigma^ {2}
$$

Thus $S S _ { R } / ( n - 2 )$ is an unbiased estimator of$\sigma ^ { 2 }$ . In addition, it can be shown that $S S _ { R }$ is independent of the pair A and B. 

## REMARKS

A plausibility argument as to why $S S _ { R } / \sigma ^ { 2 }$ might have a chi-square distribution with $n - 2$ degrees of freedom and be independent of A and $B$ runs as follows. Because the $Y _ { i }$ are independent normal random variables, it follows that $( Y _ { i } - E [ Y _ { i } ] ) / { \sqrt { \operatorname { V a r } ( Y _ { i } ) } } , i = 1 , \dots , n$ are independent standard normals and so 

$$
\sum_ {i = 1} ^ {n} \frac {(Y _ {i} - E [ Y _ {i} ]) ^ {2}}{\operatorname{Var} (Y _ {i})} = \sum_ {i = 1} ^ {n} \frac {(Y _ {i} - \alpha - \beta x _ {i}) ^ {2}}{\sigma^ {2}} \sim \chi_ {n} ^ {2}
$$

Now if we substitute the estimators A and B for α and$\beta _ { ; }$ , then 2 degrees of freedom are lost, and so it is not an altogether surprising result that $S S _ { R } / \sigma ^ { 2 }$ has a chi-square distribution with n − 2 degrees of freedom. 

The fact that $S S _ { R }$ is independent of A and B is quite similar to the fundamental result that in normal sampling$\overline { { X } }$ and $S ^ { 2 }$ are independent. Indeed this latter result states that if $Y _ { 1 } , \dots , Y _ { n }$ is a normal sample with population mean$\mu$ and variance$\sigma _ { 2 }$ , then if in the sum of squares$\textstyle \sum _ { i = 1 } ^ { n } ( Y _ { i } - { \bar { \mu } } ) ^ { 2 } / \sigma ^ { 2 }$ , which has a chi-square distribution with n degrees of freedom, one substitutes the estimator$\overline { { Y } }$ for$\mu$ to obtain the new sum of squares$\textstyle \sum _ { i } ( Y _ { i } - { \overline { { Y } } } ) ^ { 2 } / \sigma ^ { 2 }$ , then this quantity [equal to $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } ]$ will be independent of Y and will have a chi-square distribution with $n - 1$ degrees of freedom. Since $S S _ { R } / \sigma ^ { 2 }$ is obtained by substituting the estimators A and B for α and$\beta$ in the sum of squares$\textstyle \sum _ { i = 1 } ^ { n } ( Y _ { i } - { \dot { \alpha } } - \beta x _ { i } ) ^ { 2 } / \sigma ^ { 2 }$ , it is not unreasonable to expect that this quantity might be independent of A and B. 

When the $Y _ { i }$ are normal random variables, the least square estimators are also the maximum likelihood estimators. To verify this remark, note that the joint density of $Y _ { 1 } , \dots , Y _ { n }$ is given by 

$$
\begin{array}{l} f _ {Y _ {1}, \ldots , Y _ {n}} (y _ {1}, \ldots , y _ {n}) = \prod_ {i = 1} ^ {n} f _ {Y _ {i}} (y _ {i}) \\ \qquad = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} e ^ {- (y _ {i} - \alpha - \beta x _ {i}) ^ {2} / 2 \sigma^ {2}} \\ \qquad = \frac {1}{(2 \pi) ^ {n / 2} \sigma^ {n}} e ^ {- \sum_ {i = 1} ^ {n} (y _ {i} - \alpha - \beta x _ {i}) ^ {2} / 2 \sigma^ {2}} \end{array}
$$

Consequently, the maximum likelihood estimators of α and$\beta$ are precisely the values of α and$\beta$ that minimize$\textstyle \sum _ { i = 1 } ^ { n } ( y _ { i } - \alpha - \beta x _ { i } ) ^ { 2 }$ . That is, they are the least squares estimators. 

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

## Computational Identity for$\pmb { S } \pmb { S } _ { \pmb { R } }$

$$
S S _ {R} = \frac {S _ {x x} S _ {Y Y} - S _ {x Y} ^ {2}}{S _ {x x}}\tag{9.3.4}
$$

The following proposition sums up the results of this section. 

PROPOSITION 9.3.1 Suppose that the responses $Y _ { i } , i = 1 , \dots , n$ are independent normal random variables with means$\alpha + \beta x _ { i }$ and common variance$\sigma ^ { 2 }$ . The least squares estimators of$\beta$ and$\alpha$ 

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

and $S S _ { R }$ is independent of the least squares estimators A and B. Also,$S S _ { R }$ can be computed from 

$$
S S _ {R} = \frac {S _ {x x} S _ {Y Y} - (S _ {x Y}) ^ {2}}{S _ {x x}}
$$

Program 9.2 will compute the least squares estimators A and B as well as$\overline { { x } } , \sum _ { i } x _ { i } ^ { 2 }$$S _ { x x } , S _ { x Y } , S _ { Y Y }$ , and $S S _ { R }$ 

EXAMPLE 9.3a The following data relate x, the moisture of a wet mix of a certain product, to $Y ,$ the density of the finished product. 

<table><tr><td>xi</td><td>yi</td></tr><tr><td>5</td><td>7.4</td></tr><tr><td>6</td><td>9.3</td></tr><tr><td>7</td><td>10.6</td></tr><tr><td>10</td><td>15.4</td></tr><tr><td>xi</td><td>yi</td></tr><tr><td>12</td><td>18.1</td></tr><tr><td>15</td><td>22.2</td></tr><tr><td>18</td><td>24.1</td></tr><tr><td>20</td><td>24.8</td></tr></table>

Fit a linear curve to these data. Also determine $S S _ { R }$ 

SOLUTION A plot of the data and the estimated regression line is shown in Figure 9.4. 

To solve the foregoing, run Program 9.2; results are shown in Figure 9.5. ■ 

## 9.4 STATISTICAL INFERENCES ABOUT THE REGRESSION PARAMETERS

Using Proposition 9.3.1, it is a simple matter to devise hypothesis tests and confidence intervals for the regression parameters. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/56af5e11-fc02-4f02-8da8-bda2bc719bbc/64537d2bde70b48956e3caff86054b6591c880f4b9f8c58d069f4bc9a22d7c33.jpg)



FIGURE 9.4 Example 9.3a.


## 9.4.1 Inferences Concerning$\beta$

An important hypothesis to consider regarding the simple linear regression model 

$$
Y = \alpha + \beta x + e
$$

is the hypothesis that$\beta = 0$ . Its importance derives from the fact that it is equivalent to stating that the mean response does not depend on the input, or, equivalently, that there is no regression on the input variable. To test 

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


That is,$\sqrt { ( n - 2 ) S _ { x x } / S S _ { R } } ( B - \beta )$ has a t-distribution with n − 2 degrees of freedom. Therefore, if $H _ { 0 }$ is true (and so$\beta = 0 )$ , then 

$$
\sqrt {\frac {(n - 2) S _ {x x}}{S S _ {R}}} B \sim t _ {n - 2}
$$

which gives rise to the following test of $H _ { 0 }$ . 

## Hypothesis Test of $H _ { 0 } \colon \beta = 0$

A significance level$\gamma$ test of $H _ { 0 }$ is to 

$$
\begin{array}{l l} \text { reject } & H _ {0} \quad \text { if } \sqrt {\frac {(n - 2) S _ {x x}}{S S _ {R}}} | B | > t _ {\gamma / 2, n - 2} \\ \text { accept } & H _ {0} \quad \text { otherwise } \end{array}
$$

This test can be performed by first computing the value of the test statistic$\sqrt { ( n - 2 ) S _ { x x } / S S _ { R } } | B | -$ call its value v — and then rejecting $H _ { 0 }$ if the desired significance level is at least as large as 

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

relates ${ \cal Y } ,$ the miles per gallon of the car, to x, the speed at which it is being driven. Now, the claim being made is that the regression coefficient$\beta$ is equal to 0. To see if the data are strong enough to refute this claim, we need to see if it leads to a rejection of the null hypothesis when testing 

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

Since, from Table A2 of the Appendix,$t _ { . 0 0 5 , 5 } = 4 . 0 3 2$ , it follows that the hypothesis$\beta = 0$ is rejected at the 1 percent level of significance. Thus, the claim that the mileage does not depend on the speed at which the car is driven is rejected; there is strong evidence that increased speeds lead to decreased mileages. ■ 

A confidence interval estimator for$\beta$ is easily obtained from Equation 9.4.2. Indeed, it follows from Equation 9.4.2 that for any $a , 0 < a < 1$ , 

$$
P \left\{- t _ {a / 2, n - 2} <   \sqrt {\frac {(n - 2) S _ {x x}}{S S _ {R}}} (B - \beta) <   t _ {a / 2, n - 2} \right\} = 1 - a
$$

or, equivalently, 

$$
P \left\{B - \sqrt {\frac {S S _ {R}}{(n - 2) S _ {x x}}} t _ {a / 2, n - 2} <   \beta <   B + \sqrt {\frac {S S _ {R}}{(n - 2) S _ {x x}}} t _ {a / 2, n - 2} \right\} = 1 - a
$$

which yields the following. 

Confidence Interval for$\beta$ 

1$\mathrm { ~ i ~ } 1 0 0 ( 1 - a )$ percent confidence interval estimator of$\beta$ is 

$$
\left(B - \sqrt {\frac {S S _ {R}}{(n - 2) S _ {x x}}} t _ {a / 2, n - 2}, B + \sqrt {\frac {S S _ {R}}{(n - 2) S _ {x x}}} t _ {a / 2, n - 2}\right)
$$

## REMARK

The result that 

$$
\frac {B - \beta}{\sqrt {\sigma^ {2} / S _ {x x}}} \sim \mathcal {N} (0, 1)
$$

cannot be immediately applied to make inferences about$\beta$ since it involves the unknown parameter$\sigma ^ { 2 }$ . Instead, what we do is use the preceding statistic with$\sigma ^ { 2 }$ replaced by its estimator $S S _ { R } / ( n - 2 )$ , which has the effect of changing the distribution of the statistic from the standard normal to the t-distribution with n − 2 degrees of freedom. 

EXAMPLE 9.4b Derive a 95 percent confidence interval estimate of$\mu$ in Example 9.4a 

SOLUTION Since $t _ { . 0 2 5 , 5 } = 2 . 5 7 1$ , it follows from the computations of this example that the 95 percent confidence interval is 

$$
-. 1 7 0 \pm 2. 5 7 1 \sqrt {\frac {1 . 5 2 7}{3 5 0 0}} = -. 1 7 0 \pm . 0 5 4
$$

That is, we can be 95 percent confident that$\beta$ lies between −.224 and −.116. ■ 

## 9.4.1.1 REGRESSION TO THE MEAN

The term regression was originally employed by Francis Galton while describing the laws of inheritance. Galton believed that these laws caused population extremes to “regress toward the mean.” By this he meant that children of individuals having extreme values of a certain characteristic would tend to have less extreme values of this characteristic than their parent. 

If we assume a linear regression relationship between the characteristic of the off spring (Y ), and that of the parent (x), then a regression to the mean will occur when the regression parameter$\beta$ is between 0 and 1. That is, if 

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

It now follows from Equation 9.4.2 that when$\beta = 1$ , the test statistic 

$$
T S = \sqrt {8 S _ {x x} / S S _ {R}} (B - 1)
$$

has a t-distribution with 8 degrees of freedom. The significance level α test will rejec $H _ { 0 }$ when the value of TS is sufficiently small (since this will occur when $B ,$ the estimator of$\beta ,$ , is sufficiently smaller than 1). Specifically, the test is to 

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

and so the null hypothesis that$\beta \geq 1$ is rejected at the 1 percent level of significance. In fact, the p-value is 

$$
p \text {-value} = P \{T _ {8} \leq - 1 6. 2 1 3 \} \approx 0
$$

and so the null hypothesis that$\beta \geq 1$ is rejected at almost any significance level, thus establishing a regression toward the mean (see Figure 9.7). 

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

The determination of confidence intervals and hypothesis tests for α is accomplished in exactly the same manner as was done for$\beta .$ . Specifically, Proposition 9.3.1 can be used to show that 

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

## 9.4.3 Inferences Concerning the Mean Response$\alpha + \beta x _ { 0 }$

It is often of interest to use the data pairs $( x _ { i } , Y _ { i } ) , i = 1 , \ldots , n ,$ , to estimate$\alpha + \beta x _ { 0 }$ , the mean response for a given input level x<sub>0</sub>. If it is a point estimator that is desired, then the natural estimator is $A + B x _ { 0 }$ , which is an unbiased estimator since 

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

Equation 9.4.5 can now be used to obtain the following confidence interval estimator of$\alpha + \beta x _ { 0 }$ 

## Confidence Interval Estimator of$\alpha + \beta x _ { 0 }$

With $1 0 0 ( 1 - a )$ percent confidence,$\alpha + \beta x _ { 0 }$ will lie within 

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

It is often the case that it is more important to estimate the actual value of a future response rather than its mean value. For instance, if an experiment is to be performed at temperature level $x _ { 0 }$ , then we would probably be more interested in predicting $Y ( x _ { 0 } )$ , the yield from this experiment, than we would be in estimating the expected yield —$E [ Y ( x _ { 0 } ) ] = \alpha + \beta x _ { 0 }$ (On the other hand, if a series of experiments were to be performed at input level $x _ { 0 }$ , then we would probably want to estimate$\alpha + \beta x _ { 0 }$ , the mean yield.) 

Suppose first that we are interested in a single value (as opposed to an interval) to use as a predictor of $Y ( x _ { 0 } )$ , the response at level $x _ { 0 }$ . Now, it is clear that the best predictor of $Y ( x _ { 0 } )$ is its mean value$\alpha + \beta x _ { 0 }$ . [Actually, this is not so immediately obvious since one could argue that the best predictor of a random variable is (1) its mean — which minimizes the expected square of the difference between the predictor and the actual value; or (2) its median — which minimizes the expected absolute difference between the predictor and the actual value; or (3) its mode — which is the most likely value to occur. However, as the mean, median, and mode of a normal random variable are all equal — and the response is, by assumption, normally distributed — there is no doubt in this situation.] Since α and$\beta$ are not known, it seems reasonable to use their estimators A and B and thus use $A + B x _ { 0 }$ as the predictor of a new response at input level $x _ { 0 }$ 

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

we obtain, by the usual argument, upon replacing$\sigma ^ { 2 }$ in Equation 9.4.6 by its estimator $S S _ { R } / ( n - 2 )$ that 

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

<table><tr><td>Inferences About</td><td>Use the Distributional Result</td></tr><tr><td>$ \beta $</td><td>$ \sqrt{\frac{(n-2)S_{xx}}{SS_r}}(B-\beta)\sim t_{n-2}$</td></tr><tr><td>$ \alpha $<eq>\alpha + \beta x_0</eq></td><td>$ \sqrt{\frac{n(n-2)S_{xx}}{\sum_i x_i^2 SS_R}}(A-\alpha)\sim t_{n-2}$<eq>\frac{A + Bx_0 - \alpha - \beta x_0}{\sqrt{\left(\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right)\left(\frac{SS_R}{n-2}\right)}} \sim t_{n-2}</eq></td></tr><tr><td><eq>Y(x_0)</eq></td><td><eq>\frac{Y(x_0) - A - Bx_0}{\sqrt{\left(1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right)\left(\frac{SS_R}{n-2}\right)}} \sim t_{n-2}</eq></td></tr></table>

## 9.5 THE COEFFICIENT OF DETERMINATION AND THE SAMPLE CORRELATION COEFFICIENT

Suppose we wanted to measure the amount of variation in the set of response values $Y _ { 1 } , \dots , Y _ { n }$ corresponding to the set of input values $x _ { 1 } , \ldots , x _ { n }$ . A standard measure in statistics of the amount of variation in a set of values $Y _ { 1 } , \dots , Y _ { n }$ is given by the quantity 

$$
S _ {Y Y} = \sum_ {i = 1} ^ {n} (Y _ {i} - \overline {{Y}}) ^ {2}
$$

For instance, if all the $Y _ { i }$ are equal — and thus are all equal to$\overline { r } -$ then $S _ { Y Y }$ would equal 0. 

The variation in the values of the $Y _ { i }$ arises from two factors. First, because the input values $x _ { i }$ are different, the response variables $Y _ { i }$ all have different mean values, which will result in some variation in their values. Second, the variation also arises from the fact that even when the differences in the input values are taken into account, each of the response variables $Y _ { i }$ has variance$\sigma ^ { 2 }$ and thus will not exactly equal the predicted value at its input $x _ { i }$ . 

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

represents the proportion of the variation in the response variables that is explained by the different input values.$R ^ { 2 }$ is called the coefficient of determination. 

The coefficient of determination $R ^ { 2 }$ will have a value between 0 and 1. A value of $R ^ { 2 }$ near 1 indicates that most of the variation of the response data is explained by the different input values, whereas a value of $R ^ { 2 }$ near 0 indicates that little of the variation is explained by the different input values. 

EXAMPLE 9.5a In Example 9.4c, which relates the height of a son to that of his father, the output from Program 9.2 yielded that 

$$
S _ {Y Y} = 3 8. 5 2 1, \qquad S S _ {R} = 1. 4 9 7
$$

Thus, 

$$
R ^ {2} = 1 - \frac {1 . 4 9 7}{3 8 . 5 3 1} = . 9 6 1
$$

In other words, 96 percent of the variation of the heights of the 10 individuals is explained by the heights of their fathers. The remaining (unexplained) 4 percent of the variation is due to the variance of a son’s height even when the father’s height is taken into account. (That is, it is due to$\sigma ^ { 2 }$ , the variance of the error random variable.) ■ 

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

is appropriate in a given situation is to investigate the scatter diagram. Indeed, this is often sufficient to convince one that the regression model is or is not correct. When the scatter diagram does not by itself rule out the preceding model, then the least square estimators A and B should be computed and the residual $Y _ { i } - ( A + B x _ { i } ) , i = 1 , \dots , n$ analyzed. The analysis begins by normalizing, or standardizing, the residuals by dividing them by$\sqrt { S S _ { R } / ( n - 2 ) }$ ), the estimate of the standard deviation of the $Y _ { i }$ . The resulting quantities 

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

The regression parameters α and$\beta$ would then be estimated by the usual least squares approach and the original functional relationships can be predicted from 

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

Running Program 9.2 yields that the least square estimates of α and$\beta$ are 

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

it often turns out that the variance of a response is not constant but rather depends on it input level. If these variances are known — at least up to a proportionality constant — then the regression parameters α and$\beta$ should be estimated by minimizing a weighted sum of squares. Specifically, if 

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

EXAMPLE 9.8a To develop a feel as to why the estimators should be obtained by mini mizing the weighted sum of squares rather than the ordinary sum of squares, consider the following situation. Suppose that $X _ { 1 } , \ldots , X _ { n }$ are independent normal random vari ables each having mean$\mu$ and variance$\sigma ^ { 2 }$ . Suppose further that the $X _ { i }$ are not directly observable but rather only $Y _ { 1 }$ and $Y _ { 2 }$ , defined by 

$$
Y _ {1} = X _ {1} + \dots + X _ {k}, \qquad Y _ {2} = X _ {k + 1} + \dots + X _ {n}, \qquad k <   n
$$

are directly observable. Based on $Y _ { 1 }$ and $Y _ { 2 } ,$ , how should we estimate$\mu     \vdots$ 

Whereas the best estimator of$\mu$ is clearly$\begin{array} { r } { \overline { { X } } = \sum _ { i = 1 } ^ { n } X _ { i } / n = ( Y _ { 1 } + Y _ { 2 } ) / n } \end{array}$ , let us see what the ordinary least squares estimator would be. Since 

$$
E [ Y _ {1} ] = k \mu , \qquad E [ Y _ {2} ] = (n - k) \mu
$$

the least squares estimator of$\mu$ would be that value of$\mu$ that minimize 

$$
(Y _ {1} - k \mu) ^ {2} + (Y _ {2} - [ n - k ] \mu) ^ {2}
$$

$\mathrm { O n }$ differentiating and setting equal to zero, we see that the least squares estimator of µ — call it$\hat { \mu }$ — is such that 

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

it is not the best estimator$\overline { { X } }$ 

Now let us determine the estimator produced by minimizing the weighted sum of squares. That is, let us determine the value of$\mu -$ call it$\mu _ { w }$ — that minimizes 

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

Upon differentiating and then equating to 0, we see that$\mu _ { w } .$ , the minimizing value, satisfies 

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

Consequently, the maximum likelihood estimators of α and$\beta$ are precisely the values of α and$\beta$ that minimize the weighted sum of squares$\textstyle \sum _ { i = 1 } ^ { n } w _ { i } ( y _ { i } - \alpha - \beta x _ { i } ) ^ { 2 }$ 

(b) The weighted sum of squares can also be seen as the relevant quantity to be minimized by multiplying the regression equation 

$$
Y = \alpha + \beta x + e
$$

by ${ \sqrt { u } } .$ . This results in the equation 

$$
Y \sqrt {w} = \alpha \sqrt {w} + \beta x \sqrt {w} + e \sqrt {w}
$$

Now, in this latter equation the error term $e \sqrt { w }$ has mean 0 and constant variance. Hence, the natural least squares estimators of α and$\beta$ would be the values of A and B tha minimize 

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

between Y , the travel time, and x, the distance, how should we estimate α and$\beta \ ?$ To utilize the weighted least squares approach we need to know, up to a multiplicative constant, the variance of Y as a function of x. We will now present an argument that$\mathrm { V a r } ( Y )$ should be proportional to x. 

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

would be appropriate. However, as there does not appear to be any a priori reason why$\mathrm { V a r } ( Y )$ should not depend on the input level x, it is not clear that we would be justified in using the ordinary least squares approach to estimate$\alpha$ and$\beta .$ . Indeed, we will now argue that a weighted least squares approach with weights 1/x should be employed — that is, we should choose A and $B$ to minimize 

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

(a) Another technique that is often employed when the variance of the response depends on the input level is to attempt to stabilize the variance by an appropriate transformation. For example, if Y is a Poisson random variable with mean λ, then it can be shown [see Remark (b)] that$\sqrt { Y }$ has approximate variance .25 no matter what the value of λ. Based on this fact, one might try to model $E [ { \sqrt { Y } } ]$ as a linear function of the input. That is, one might consider the model 

$$
\sqrt {Y} = \alpha + \beta x + e
$$

(b) Proof that$\mathrm { V a r } \sqrt { Y } \approx$ .25 when Y is Poisson with mean λ. Consider the Taylor series expansion of $g ( y ) = \sqrt { y }$ about the value λ. By ignoring all terms beyond the second derivative term, we obtain that 

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

where$\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { r }$ are regression coefficients that would have to be estimated. If the data set consists of the n pairs $( x _ { i } , Y _ { i } ) , i = 1 , \ldots , n .$ , then the least square estimators of$\beta _ { 0 } , \ldots , \beta _ { r }$ — call them $B _ { 0 } , \ldots , B _ { r } -$ are those values that minimize 

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

where $x _ { j } , j = 1 , \dotsc , k$ is the level of the jth input variable and $e$ is a random error that we shall assume is normally distributed with mean 0 and (constant) variance$\sigma ^ { 2 }$ . The parameters$\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { k }$ and$\sigma ^ { 2 }$ are assumed to be unknown and must be estimated from the data, which we shall suppose will consist of the values of $Y _ { 1 } , \dots , Y _ { n }$ where $Y _ { i }$ is the response level corresponding to the $k$ input levels $x _ { i 1 } , \ldots , x _ { i 2 } , \ldots , x _ { i k }$ . That is, the $Y _ { i }$ are related to these input levels through 

$$
E [ Y _ {i} ] = \beta_ {0} + \beta_ {1} x _ {i 1} + \beta_ {2} x _ {i 2} + \dots + \beta_ {k} x _ {i k}
$$

If we let $B _ { 0 } , B _ { 1 } , \ldots , B _ { k }$ denote estimators of$\beta _ { 0 } , \ldots , \beta _ { k }$ , then the sum of the squared differences between the $Y _ { i }$ and their estimated expected values is 

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

where$\mathbf { X } ^ { \prime }$ is the transpose of X. 

To see that Equation 9.10.2 is equivalent to the normal Equations 9.10.1, note that 

$$
\begin{array}{r l} \mathbf {X} ^ {\prime} \mathbf {X} & = \left[ \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ x _ {1 1} & x _ {2 1} & \dots & x _ {n 1} \\ x _ {1 2} & x _ {2 2} & \dots & x _ {n 2} \\ \vdots & \vdots & & \vdots \\ x _ {1 k} & x _ {2 k} & \dots & x _ {n k} \end{array} \right] \left[ \begin{array}{c c c c c} 1 & x _ {1 1} & x _ {1 2} & \dots & x _ {1 k} \\ 1 & x _ {2 1} & x _ {2 2} & \dots & x _ {2 k} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & x _ {n 1} & x _ {n 2} & \dots & x _ {n k} \end{array} \right] \\ & = \left[ \begin{array}{c c c c c} n & \sum_ {i} x _ {i 1} & \sum_ {i} x _ {i 2} & \dots & \sum_ {i} x _ {i k} \\ \sum_ {i} x _ {i 1} & \sum_ {i} x _ {i 1} ^ {2} & \sum_ {i} x _ {i 1} x _ {i 2} & \dots & \sum_ {i} x _ {i 1} x _ {i k} \\ \vdots & \vdots & \vdots & & \vdots \\ \sum_ {i} x _ {i k} & \sum_ {i} x _ {i k} x _ {i 1} & \sum_ {i} x _ {i k} x _ {i 2} & \dots & \sum_ {i} x _ {i k} ^ {2} \end{array} \right] \end{array}
$$

and 

$$
\mathbf {X} ^ {\prime} \mathbf {Y} = \left[ \begin{array}{c} \sum_ {i} Y _ {i} \\ \sum_ {i} x _ {i 1} Y _ {i} \\ \vdots \\ \sum_ {i} x _ {i k} Y _ {i} \end{array} \right]
$$
