
# Descriptive Statistics

In an experiment, we basically collect **values** for one or more **attributes** or **variables** of each member of the sample.
![[Pasted image 20250626094544.png]]

The frequency table can be visualized using a **line graph** or a **bar graph** or a **frequency polygon**.

Relative frequency tables, when we are only interested in the *percentage* or *fraction* of those frequencies for each data value, i.e., *relative frequencies*.
These can be represented using **Pie Charts**, the area of each sector = relative frequency for that value. But they are only useful when there are only a small number of distinct data values.

Dealing with continuous data:
-  Let the sample points be {$x_i$}, i<=i<=N.
-  Let there be some K (K<<N) bins, where the jth bin has interval \[$a_j, b_j$).
-  Such frequency tables are also called **histograms** and they can be used to store relative frequency instead of frequency.
![[Pasted image 20250626100441.png]]

The histogram binning problem:
-  If you have too few bins (each bin is very wide), there is very little idea you get about the data distribution from the histogram.
-  Extreme: only one bin to represent whole data
-  If you have many bins (all will be narrow), then there are many points falling into each bin. Again there is very little idea you get about the data distribution from the histogram.
-  Extreme: one bin for each distinct value.

Cumulative Frequency Plot:
The **cumulative** (relative) **frequency plot** tells you the (proportion) number of sample points whose value is *less than or equal* to a given data value.
![[Pasted image 20250626101123.png]]

#### Summarizing a sample-set:
-  There are some values that can be considered "representative" of the entire sample-set. Such values are called as a "statistic"
-  The most common statistic is: the sample (arithmetic) **mean**, basically the "average value."
-  Another is the sample **median**, which is the "middle value".
-  We sort the data array **A** from smallest to largest, if N is odd, then median is the value at the (N+1)/2 position; if N is even, the median can take any value in the interval (A\[N/2], A\[N/2+1]).
-  If each sample point $x_i$ is replaced by a$x_i$+b, then mean and median becomes a$\bar{x}$+b

Consider a set of sample points x1, . . . , xN. For what value of y, is the sum total of the **squared** difference with every sample point, the least ? 
Total squared deviation (or total squared loss) is least when y = mean.
F(y) = $\sum_{i=1}^{N}$($x_i$-y)$^2$  => So for F(y) to be minimum, F'(y) = 0 -> y = mean 

For what value of y, is the sum total of the **absolute** difference with every sample point, the least ?
Total absolute deviation (or total absolute loss) is least when y = median.
F(y) = $\sum_{i=1}^{N}$|$x_i$-y|   =>  So, for F(y) to be minimum, y = median.

-  The mean need not be part of the original sample set, the median is always a member of the original sample-set if N is odd. If N is even, the median is not unique and will not be a member of the set.

##### Percentiles:
-  The sample 100p percentile (0<=p<=1) is defined as the data value y such that 100p% of the data have a value less than or equal to y, and 100(1-p)% of the data have a larger value.
-  For a data set with n sample points, the sample 100p percentile is that value such that at least np of the values are less than or equal to it. And at least n(1-p) of the values are greater than it.
##### Quantiles:
-  The sample 25 percentile = first quartile
-  The sample 50 percentile = second quartile
-  The sample 75 percentile = third quartile
-  Quantiles can be inferred from the cumulative relative frequency, or by sorting the data values.
![[Pasted image 20250626104052.png]]

Mode: The value that occurs with the highest frequency
-  It may not be unique, in which case all the highest frequency values are called **modal values**.
![[Pasted image 20250626104218.png]]

Variance and Standard Deviation:
-  The **variance** is (approximately) the average value of the squared distance between the sample points and the sample mean. The formula is: 
variance = $\sigma^2$ = $\sum_{i=1}^{N}$($\bar{x}-x_i$)$^2$ / (N-1).
-  The variance measures the "spread of the data around the sample mean"
-  Its positive square root is called the **standard deviation**.
-  If x$_i$ is replaced by ax$_i$+b, then variance is scaled by a factor of a$^2$.

#### Chebyshev's Inequality:
-  If we know that the average marks for the course is 75 and the variance is 25. Can we say something about how many students secured marks from 65 to 85 ?
Two-sided Chebyshev's Inequality:
The proportion of sample points k or more than k (k>0) standard deviations away from the sample mean is less than 1/k$^2$.
S$_k$ = { x$_i$ : |$x_i - \bar{x}$| $\geq$ k$\sigma$}
|S$_k$|/N < 1/k$^2$.

Applying Chebyshev's Inequality, the fraction of students who got less than 65 or more than 85 marks is:  less than 1/4 (k=2, $\sigma$ = 5).
So the fraction of students who got marks from 65 to 85 is more than 0.75.
The bounds predicted by this inequality are loose, but they are correct

One-Sided Chebyshev's Inequality:
The proportion of sample points k or more than k (k>0) standard deviations away from the sample mean **and greater than the sample mean** is less than or equal to 1/(1 + k$^2$).
S$_k$ = { x$_i$ : $x_i - \bar{x}$ $\geq$ k$\sigma$}  --> No absolute value.
|S$_k$|/N < 1/(1 + k$^2$).

#### Correlation between different data values
Sometimes each sample-point can have a pair of attributes. It may happen that large values of the first attribute are accompanied with large (or small) values of the second attribute for a larger number of sample points.
![[Pasted image 20250626110521.png]]

Visualizing such relationships:
-  Can be done by means of a scatter plot
-  X axis: values of attribute 1, Y axis: values of attribute 2
-  Plot a marker at each such data point. The marker may be a small circle, a +, a \*, and so on.
![[Pasted image 20250626110800.png]]

Correlation Coefficient:
-  Let the sample-points be given as (x$_i$, y$_i$), 1<= i <= N.
-  Let the sample standard deviations be $\sigma_x$ and $\sigma_y$, and the sample means be $\mu_x$ and $\mu_y$.
-  The **correlation coefficient** is given as:
![[Pasted image 20250626111108.png]]

-  r>0, **positively correlated** (one attribute being higher implies the other is higher). Similarly r<0, **negatively correlated**.
-  r=0 means the data are **uncorrelated**. And r is undefined if the standard deviation of either x or y  is 0.
-  -1 <= r <= 1 : always.
![[Pasted image 20250626111445.png]]

-  If y$_i$ = a + bx$_i$, then if b>0 => r(x, y) = 1. If b<0 => r(x, y) = -1.
-  So, if r is the correlation coefficient for (x$_i$, y$_i$) then it is also the correlation coefficient for (b + ax$_i$, d + cy$_i$) if a and c have the same sign. 
![[Pasted image 20250626111933.png]]

Anscombe's quartet:
-  The correlation coefficient can be a misleading value, and graphical examination of the data is important.
-  4 examples that appear graphically different, but have identical correlation coefficient.
![[Pasted image 20250626112138.png]]

Reflective (or Uncentered) correlation coefficient:
-  A version in which you do not deduct the mean values from the vectors.
![[Pasted image 20250626112308.png]]

-  Uncentered is not translational invariant, r$_{uncentered}$(x, y)  !=  r$_{uncentered}$(x + a, y +b) 
-  A high correlation coefficient between two attributes does not mean that one causes the other. It also does not mean that correlation is *never* associated with causation. It does not necessarily imply but it **may**.

****

# Elements of Probability

#### Probability in Computer Science:
-  Algorithmic Design
	-  Randomized algorithms: steers around unlikely situations
	-  Several hard problems that can only be solved efficiently with high probability
-  Performance Analysis
	-  What is the probability that you will find the next accessed page in cache ?
	-  What is the probability that the length of the queue will be greater than 5 when a job arrives at a server ?
-  Network Protocol Design
-  Machine Learning / AI : Is all about probability and statistics 

The set of all possible outcomes of an experiment is called the **sample space**.
Any subset of the sample space is called an **event**.
Given event E, the event E$^c$ is called the **complement** of E.
![[Pasted image 20250626113601.png]]

The notion of relative frequency of event E obeys the above axioms.

#### Independence of Events:
Two events are independent if:
P(A) = P(A|B)
-> P(A$\cap$B) = P(A).P(B)

We say that n>2 events are mutually independent if and only if for every subset A of k $\leq$ n events, we have:
P($\bigcap_{i=1}^{k}$P(A$_i$)) = $\Pi_{i=1}^{k}$P(A$_i$)
Example: three events A, B, C. To show that they are independent we need to show that:
P(A$_1$, A$_2$, A$_3$) = P(A$_1$).P(A$_2$).P(A$_3$)
P(A$_1$, A$_2$) = P(A$_1$).P(A$_2$)
P(A$_2$, A$_3$) = P(A$_2$).P(A$_3$)
P(A$_1$, A$_3$) = P(A$_1$).P(A$_3$)

Only n-way independence of events does not imply that every pair of events are independent.
If A is independent of B, we can say that A is independent of B$^c$ if A and B are mutually exclusive.

Network Reliability: 
Consider the following parallel network:
-  n independent router, which each are working with probability p$_i$ (1 $\leq$ i $\leq$ n).
-  Let E be the event that a working path from A to B exists:
P(E) = 1 - $\Pi_{i=1}^{n}$(1 - p$_i$)

#### The Monty Hall Problem:
Behind one door is a prize (equally likely for each door). Behind the other two doors are goats.
How to play:
1.  We choose a door
2.  Host opens 1 of the other 2 doors, revealing a goat.
3.  We are given the option to switch to the other door.
Initially the P(win) = 1/3.
Now, we are comparing P(win) and P(win | switch). Let's say we picked A.
P(win | switch) = P(win | A prize, pick A, switch)\*P(A is prize) + 
				P(win | B prize, pick A, switch)\*P( B is prize) + 
				P(win | C prize, pick A, switch)\*P(C is prize) 
			 = 1/3x(0) + 1/3x(1) + 1/3x(1) = 2/3
But, the more intuitive way to think is that initially the door I chose, the probability of it being a prize is 1/3, and the probability that it is a goat was 2/3. But if I switch, the probability of it being a goat is 1/3 and it being a prize is 2/3. Thus, switching was the better option.

#### The Birthday Paradox !
-  Given n people in a room, what should be the least value of n such that the probability that at least 2 people in the room share the same birthday is greater than or equal to 99.9% ?
-  Each person can have his/her birthday on any of the 365 days. For n people, there are 365$^n$ outcomes.
-  The number of outcomes resulting in no two people sharing a birthday is (365).(365-1).(365-2) . . . (365-n+1).
-  So required probability is: 1 - (365).(365-1).(365-2) . . . (365-n+1) / (365)$^n$ $\geq$ 0.999
-  This is satisfied for n as small as 70.

**** 

# Random Variables:

A random variable is a variable whose value is uncertain
Random variables store the outcome of an experiment
Random variables can be described by their possible outcomes + probabilities.
*Random variables can only be numbers, not "heads" or "tails"*.
Random variables are an abstraction on top of events, they are *not* events.

**Probability Mass Function (PMF)**: The probability function we get, when we list out all possible outcomes + their probabilities.
The relationship between values a random variable can take on, and the corresponding probability, is a ***function*** 

Random variables can be discrete or continuous.

If X is continuous, it can take an infinite number of values. Probability Mass Function P(X=k) cannot be defined. Instead we ask for probability that x lies in an interval B of non-zero size: P(X $\epsilon$ B).
**Probability Density Function**: f(X) $\geq$ 0

**Cumulative Distribution Function**:
Assume R.V  X is ordered.
CDF of X is a function F(a) that takes a value a and returns P(X $\leq$ a)
CDF of a discrete distribution:  F(x) = $\sum_{x_i \leq x}$P(X = x$_i$)
CDF of a continuous distribution:  
P(X $\leq$ a)  = $\int_{-\inf}^{a}$ f(x)dx
![[Pasted image 20250627093738.png]]

#### Expected Value of a Random Variable:
For a discrete random variable X, is defined as:
E(X) = $\sum_{i}$x$_i$P(X = x$_i$)
For a continuous random variable X, it is defined as:
E(X) = $\int_{-\inf}^{+\inf}$ xf$_x$(x)dx

Expected value of a function of a random variable:
E(g(X)) =  $\sum_{i}$g(x$_i$)P(X = x$_i$)   for a discrete random variable
E(g(X)) =  $\int_{-\inf}^{+\inf}$ g(x)f$_x$(x)dx   for a continuous random variable.

E(ag(X) + b) = aE(g(X)) + b

#### Variance:
The definition of variance for a continuous r.v with mean $\mu$ is:
*Var(X) = E\[(X-$\mu$)$^2$]*  =  $\int_{-\inf}^{+\inf}$(x-$\mu$)$^2$f$_x$(x)dx
For a discrete r.v, 
*Var(X) = E\[(X-$\mu$)$^2$]*  =  $\sum_{i}$(x$_i$ - $\mu$)$^2$P(X=x$_i$)
Low-variance probability mass functions or probability densities tend to be concentrated around one point. High variance densities are spread out.
Var(X) = E(X$^2$) - \[E(X)]$^2$

#### Bernoulli Random Variable:
X $\epsilon$ {0, 1}
PMF of X, P(X=1) = $\theta$
P(X=x) = $\theta^x$(1 - $\theta$)$^{1-x}$
E\[X] = 0.(1 - $\theta$) + 1.($\theta$) = $\theta$  => $\mu$ = $\theta$
V(X) = (0 - $\theta$)$^2$(1 - $\theta$) + (1 - $\theta$)$^2$$\theta$  =  $\theta$(1 - $\theta$)

#### Binomial Random Variable:
X $\epsilon$ {0, 1, 2, 3, . . ., n}
![[Pasted image 20250627102217.png]]
![[Pasted image 20250627102231.png]]
![[Pasted image 20250627102240.png]]
![[Pasted image 20250627102248.png]]
![[Pasted image 20250627102306.png]]

The Binomial is a sum of Bernoulli random variables.
The Expectation of Binomial, is:
E\[X] = n.p    -> Sum n times, this is true for every binomial ever.
The variance of Binomial R.Vs:
Var(X) = n.p(1-p)

![[Pasted image 20250627102841.png]]

![[Pasted image 20250627103235.png]]
![[Pasted image 20250627103242.png]]
Which bucket a marble lands in corresponds to the number of times the marble went right.

#### The Geometric Random Variable:
Imagine flipping a coin *until you see your first heads*. Each coin flip is an independent trial, with probability *p* of getting heads.
How many flips until the first heads ?
Deriving the PMF:
P(heads on first flip) = *p*
P(tails, then heads) = (1-*p*)*p*
. . .
P(X = n) = (1 - *p*)$^{n-1}$*p*
E\[Y] = $\sum_{i=1}^{\inf}$ n.(1-p)$^{n-1}$.p  =  1/p

#### The Negative Binomial Random Variable:
Imagine flipping a coin until you see r heads. Each coin flip is an independent trial, with probability *p* of getting heads.
How many coin flips until ***r*** heads ?
X $\epsilon$ {r, r+1, . . . , $\inf$}
 P(X = n) = ${n-1} \choose {r-1}$ p$^r$(1-p)$^{n-r}$
 The Negative Binomial is a sum of Geometric Random Variables.
 E\[Y] = $\sum_{i=1}^{r}$ E\[X$_i$] = r/p    (where X$_i$ is a Geometric Random Variable)

#### St. Petersburg Paradox
The Game:
-  We have a fair coin (lands on heads with p=0.5)
-  Let n = number of coin flips (tails) to get the first heads
-  You will win: \$2$^n$
How much would you pay to play ?

Let X be your winnings:
E\[X] = (1/2)$^1$ 2$^1$ + (1/2)$^2$ 2$^2$ + (1/2)$^3$ 2$^3$ + . . .  = $\inf$
What if you could play this game for $1000, but just once ?

![[Pasted image 20250627110335.png]]
![[Pasted image 20250627110947.png]]
![[Pasted image 20250627110342.png]]

#### Poisson Random Variable:

Expected number of autos in an hour = 10
Time interval = 5 minutes
Probability that one auto will arrive in the next 5 minutes is:

1 - $55 \choose 10$/$60 \choose 10$  (or)  1 - $3300 \choose 10$/$3600 \choose 10$    -->  approximately.

![[Pasted image 20250627111449.png]]

-  In all four discrete R.Vs so far (Bernoulli, Binomial, Geometric, Negative binomial) , we were counting some outcome from a set of possible options
	-  Multiple dice rolls
	-  Servers in operation
	-  Views of ads on YouTube
-  In many real-life applications, the substrate is continuous, example time.
	-  We are counting outcomes of interest in this continuous space.

**Case Study**: Ride Sharing Apps
![[Pasted image 20250627112121.png]]
![[Pasted image 20250627112135.png]]
![[Pasted image 20250627112150.png]]
![[Pasted image 20250627112157.png]]

A **Poisson** random variable models the number of occurrences that happen in a *fixed*
interval of time.
PMF:
P(X = k) = e$^{-\lambda}$$\lambda^k$/k!
X takes on values 0, 1, 2, . . . up to infinity

If we want to model events occurring over a given time interval.
-  Earthquakes, radioactive decay, queries to a web server, etc.
The events must follow a **Poisson Process**:
1.  Events happen *independently* of one another
2.  Events arrive at a *fixed* rate: $\lambda$ events per interval of time
If those conditions are met:
Let X be the number of events that happen in the time interval.   X ~ Poi($\lambda$)
E\[X] = $\lambda$ = Var(X)
![[Pasted image 20250627113030.png]]
![[Pasted image 20250627113038.png]]
![[Pasted image 20250627113048.png]]

![[Pasted image 20250627113125.png]]

The Poisson approximates the Binomial when n is large.

![[Pasted image 20250627113411.png]]
![[Pasted image 20250627113424.png]]
![[Pasted image 20250627113435.png]]
![[Pasted image 20250627113448.png]]

**** 

# Special Continuous Random Variables:

#### Uniform Random Variable:
X is uniformly distributed between $\alpha$ and $\beta$
X ~ U($\alpha$, $\beta$)
P(X) = 1/($\beta$ - $\alpha$)          P(X $\epsilon$ \[a, b])
E\[X] = ($\alpha$ + $\beta$)/2         Var(X) = ($\alpha$ - $\beta$)$^2$/12
**Application of Uniform R.Vs**
***Given a set of n elements x$_1$, . . . , x$_n$. You need to write an algorithm for selecting a random subset k of the n elements given access to a uniform random number generator U(0, 1).***
*Approaches:*
1.  Online Sampling Approach:
This method incrementally builds the random subset `R` by iterating over the elements and making probabilistic decisions.
![[Pasted image 20250628061317.png]]

2.  Full Enumeration:
This describes a completely different method — **generate all possible subsets of size `k`, then randomly select one**.
![[Pasted image 20250628061350.png]]

***Say you are hosting a webserver. You want to track the interaction of a random subset of k customers that arrive at the webserver. But you do not know the number of customers that will arrive in advance.***
***You have limited memory k and cannot store all possible customers data that arrive and then select a subset.***
***You can generate uniform random numbers between 0 and 1***
*Approach*: This is known as Reservoir Sampling
-  Initialize R with first k elements.
-  For each subsequent x$_i$
	-  Sample a uniform integer s from 1,2,3,. . . ,i
	-  If s $\leq$ k, R\[s] = x$_i$

***Prove that the probability with which we add element x$_j$ to R$_i$ after seeing i elements is k/i***
By Induction;
-  Base Case i=k holds
-  Assume that at i-1, P(x$_j$ $\epsilon$ R$_{i-1}$) = k/(i-1)  , j $\epsilon$ \[1, . . . , i -1]
-  P(x$_j$ $\epsilon$ R$_{i}$) = P(x$_j$ $\epsilon$ R$_{i-1}$) . (1 - k/i * 1/k)
Thus, P(x$_j$ $\epsilon$ R$_{i}$) = k/i

****

# Normal (Gaussian) Random Variable:
![[Pasted image 20250628062757.png]]
![[Pasted image 20250628062816.png]]

E\[X] = $\mu$       Var(X) = $\sigma ^2$

**Properties:**
If X ~ N( $\mu$, $\sigma ^2$ ) and if Y = aX + b, then Y ~ N( a$\mu$+b, a$^2 \sigma^2$ )
Median = Mean, because of symmetry of the PDF about the mean
Mode = Mean : Can be checked by setting the first derivative of the PDF to 0 and solving, and checking the sign of the second derivative.

**Why the Normal ?**
-  Common for natural phenomena: human height, weight, shoe sizes, etc.
-  A lot of noise in the world is Normal
	-  E.g., random errors in measurements, residuals in linear regression
-  The sum of many random variables often looks Normal
-  Sample means are distributed normally - important for statistics
-  Even things that aren't Normal might fit a normal-related distribution.
People also just assume things are normally distributed a lot.
-  They can do this in part because the Normal is so common
-  But there's a deeper reason to it . . .

#### When We Fit Models to Data, We Try To Keep It Simple:
![[Pasted image 20250628064115.png]]
![[Pasted image 20250628064137.png]]
![[Pasted image 20250628064145.png]]

#### Entropy:
-  Measures the amount of uncertainty associated with a distribution
-  High Entropy -> high uncertainty or chaos
-  Formula of Entropy:

**Continuous Entropy:**
For a **continuous random variable** $X$ with probability density function $f(x)$, the **differential entropy** is:

$$
\text{Entropy}(X) = - \int f(x) \log f(x) \, dx
$$

* This integral sums over all possible values of `x`.
* The log is typically base-2 for **bits**, or natural log for **naturals**.

**Discrete Entropy:**
* **If $X$ is discrete**, entropy is expressed using summations instead of integrals.
For a **discrete random variable** $X \in \{x_1, x_2, \dots, x_k\}$, with probability mass function $p(x_i)$:

$$
\text{Entropy}(X) = -\sum_{x_i} p(x_i) \log p(x_i)
$$

* **Minimum entropy** occurs when there's no uncertainty — one outcome has all the probability:

  $$
  p(x_i) = 1 \text{ for some } i, \quad p(x_j) = 0 \text{ for all } j \ne i
  $$
* **Maximum entropy** happens when all outcomes are equally likely:

  $$
  p(x_i) = \frac{1}{k} \text{ for all } i \in \{1, \dots, k\}
  $$

**Optimization Problem:**
> Find the distribution $p(x_i)$ that **maximizes entropy** under certain constraints.

##### Objective:

$$
\max -\sum p(x_i) \log p(x_i)
$$

###### Subject to:
1. $p(x_i) \ge 0$ for all $i$ (non-negativity)
2. $\sum_{i=1}^{k} p(x_i) = 1$ (valid probability distribution)

This maximization leads to the **uniform distribution**, where all $p(x_i) = \frac{1}{k}$. That’s why uniform distributions are the **most uncertain** (maximum entropy).


*Entropy for a continuous R.V is more precisely referred to as: Differential Entropy*
**The Differential Entropy describes the equivalent side length (in logs) of the set that contains most of the probability of the distribution.**

**Entropy of Gaussian Distribution:**
Entr(X) = 1/2 + log($\sqrt{2\pi}$ $\sigma$)

It is possible to derive the Gaussian Density function just starting from the desire to maximize entropy while matching a given mean $\mu$, and variance $\sigma ^2$

#### CDF of Standard Normal and General Normal Distributions:
Standard Normal Distribution: N(0, 1)
General Normal Distribution: N($\mu$, $\sigma ^2$) 

**Standard Normal Distribution:**
* Let $X \sim N(0, 1)$ — a standard normal variable.
* The **CDF** of $X$, denoted by $\Phi(x)$ or $F_X(x)$, is:

$$
\Phi(x) = F_X(x) = \mathbb{P}(X \leq x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-z^2 / 2} \, dz
$$

📌 **Key point:**
This integral **does not have a closed-form solution**, so in practice, we use **lookup tables or libraries** (like `scipy.stats.norm.cdf` in Python).

**General Normal Distribution:**
To compute the CDF of a general Gaussian $Y$, we reduce it to the standard normal:
###### ✅ Step-by-step:

1. Convert $Y$ to standard normal $X$:

$$
X = \frac{Y - \mu}{\sigma} \sim N(0, 1)
$$

2. Compute the CDF:

$$
F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}\left( \frac{Y - \mu}{\sigma} \leq \frac{y - \mu}{\sigma} \right) = \Phi\left( \frac{y - \mu}{\sigma} \right)
$$

✅ So, the CDF of any normal distribution reduces to computing $\Phi(z)$, which is already tabulated.

![[Pasted image 20250628072657.png]]
![[Pasted image 20250628072705.png]]

#### MGF of Standard Normal and General Normal Distribution:
For a random variable $X$, the **MGF** is defined as:

$$
M_X(t) = \mathbb{E}[e^{tX}]
$$

That is:
* For a **discrete** random variable:
  $$
  M_X(t) = \sum_{x} e^{t x} \cdot P(X = x)
  $$

* For a **continuous** random variable:
$$
  M_X(t) = \int_{-\infty}^{\infty} e^{t x} \cdot f_X(x) \, dx
  $$

where $f_X(x)$ is the PDF of $X$, and the MGF exists in some interval $t \in (-h, h)$ for $h > 0$.

#### Examples:
##### 1. MGF of Bernoulli($p$)
Let $X \in \{0, 1\}$ with $P(X=1)=p$, $P(X=0)=1-p$:
$$
M_X(t) = \mathbb{E}[e^{tX}] = e^{0} (1 - p) + e^{t} p = (1 - p) + p e^{t}
$$

##### 2. MGF of Normal($\mu, \sigma^2$)
Let $X \sim N(\mu, \sigma^2)$
$$
M_X(t) = \exp\left( \mu t + \frac{\sigma^2 t^2}{2} \right)
$$

##### 3. MGF of Exponential($\lambda$)
Let $X \sim \text{Exp}(\lambda)$ with PDF $f(x) = \lambda e^{-\lambda x}$
$$
M_X(t) = \int_0^\infty e^{t x} \cdot \lambda e^{-\lambda x} dx = \frac{\lambda}{\lambda - t} \quad \text{for } t < \lambda
$$


#### Sum of Gaussian Random Variables:
Let Y = X$_1$, . . ., X$_n$
Where each X$_i$ ~ N( $\mu _i$, $\sigma_i^2$ )
Then,   Y ~ N( $\sum_{i}$$\mu _i$,  $\sum_{i}$$\sigma_i^2$ )

**** 

# Exponential Random Variable:
![[Pasted image 20250628073844.png]]
![[Pasted image 20250628073856.png]]

**Relationship to Poisson distribution:**
-  Both are applicable when events occur continuously and independently at a constant average rate $\lambda$
-  Poisson R.V is discrete over the number of events in a given time
-  Exponential R.V is continuous and is the distance between two events

![[Pasted image 20250628074059.png]]

**Memoryless property of exponential distribution:**
P ( X > s + t | X > s) = P (X > t)
**Example:** lifetime T of a lamp if exponentially distributed, then remaining lifetime does not depend on how long lamp has been in use.
***This property is unique to exponential***

If  X$_1$, . . ., X$_n$  are independent exponential random variables having respectful parameters  $\lambda _1$, . . . , $\lambda_n$, then min(X$_1$, . . ., X$_n$) is exponential with parameter $\sum_{t=1}^{n}\lambda_i$ 
![[Pasted image 20250628074809.png]]

**Maximum Entropy Distribution:**
Among all continuous probability distributions with **support** \[0, $\inf$) and mean $\mu$, the exponential distribution with $\lambda$ = 1/$\mu$  has the largest **differential entropy**.
In other words, it is the **maximum entropy probability distribution** for a **random variate** X which is greater than or equal to zero and for which E\[X] is fixed.

****

# Multiple RVs

Often, all the random variables involved are not independent of each other. So, we can't just have a single distribution for each random variable - we need a way to talk about all the random variables at the same time.

#### The Joint Distribution of Multiple Random Variables:
For *discrete* random variables X and Y, we have **joint probability mass function:**
P ( X = x, Y = y )
For *continuous* random variables, we have a **joint probability density function:**
f ( X = x, Y = y )   =>  P{ (X, Y) $\epsilon$ C } = $\int_{(x, y) \epsilon C}\int$  f( x, y ) dx dy

#### Marginals:
P ( X = x ) = $\sum_{y}$ P ( X = x, Y = y )
This P(X = x) is called the marginal of the joint distribution P(X, Y).
f(X - x) = $\int_{y}$ f(x, y) dy

![[Pasted image 20250628080436.png]]
![[Pasted image 20250628080520.png]]

![[Pasted image 20250628080532.png]]
![[Pasted image 20250628080542.png]]

![[Pasted image 20250628080553.png]]
![[Pasted image 20250628080601.png]]

****

# Parameter Estimation:

![[Pasted image 20250628080716.png]]

Parameters differ based on the task and application

#### The Setup for parameter estimation in real-life:
##### Step 1: A real-life problem:
1.  Estimating the probability that at least 2 out of 4 servers will be alive next day
2.  The probability that stock price will raise by 10% in the next week
3.  The expected number of clicks on an advertisement in the next 3 hours

##### Step 2: Model the problem: Choose a functional form of the uncertainty
1.  Binomial ?
Assume that servers fail independently, X = # of failures in a day, X ~ Bin()
2.  Gaussian ?
X = change from one day to the next
3.  Poisson ?
X = # of clicks on the ad per hour

##### Step 3: Collect a training sample by observing over several days
1.  Sample server failure data observed over 3 days
2.  Stock price change over a 10 days
3.  Number of clicks on the ad over the last 20 hours

##### Step 4: Estimate the unknown parameters using the training sample

**The overall setup in parameter estimation:**
-  Given a density or distribution function with parameters f(x, $\theta$)
-  Given: sample: D = { x$_1$, . . . . , x$_N$ }
	-  The i$^{th}$ sample is a random variable X$_i$ assumed to be independently identically distributed as per the unknown f(x, $\theta$)
-  Find $\theta$

-  Since D is a finite sample, we cannot really know the actual $\theta$. Best we can do is obtain an estimate of $\theta$.
-  We will denote the estimate as $\hat{\theta}$

****
#### Types of Estimators:

-  **Maximum likelihood:** sample D is all you got.   ($\hat{\theta}$ point estimator)
-  **Bayesian estimation:** in addition to sample, we got prior beliefs.


#### Maximum Likelihood Estimation:
-  If $\theta$ were known, we could have calculated the probability of getting the N outcomes in D = { x$_1$, . . . , x$_N$ } from the distribution as
-  P( D | $\theta$ ) = P( x$_1$, . . . , x$_N$ | $\theta$ ) = $\prod_{i}$P( x$_i$ | $\theta$ ) = $\prod_{i}$f(x$_i$; $\theta$)
-  Likelihood refers to the above function. Often denoted as L($\theta$)
-  Maximum likelihood estimator: ***Choose the parameter $\theta$ for which the above likelihood is maximized.***
-  Use log-likelihood instead of likelihood to convert products into sums, then solve using numerical optimization methods applying calculus.

![[Pasted image 20250701093617.png]]
![[Pasted image 20250701093633.png]]

![[Pasted image 20250701093653.png]]

![[Pasted image 20250701093827.png]]
![[Pasted image 20250701093840.png]]

![[Pasted image 20250701094000.png]]

#### MLE for a new distribution: Gamma distribution
A random variable is said to have a gamma distribution with parameters ( $\alpha$, $\lambda$ ),       $\lambda$ > 0, $\alpha$ > 0, if its density function is given by:
![[Pasted image 20250701094245.png]]

-  Can look like Gaussian for positive random variables
-  Reduces to exponential when $\alpha$ = 1
-  More flexible than exponential since mode is not at 0
-  Useful to model one-sided long tails, e.g., blue curve here.
  ![[Pasted image 20250701094429.png]]

![[Pasted image 20250701094500.png]]
![[Pasted image 20250701094516.png]]
![[Pasted image 20250701094528.png]]

#### Evaluating a point estimator:
-  Given sample D = { x$_1$, . . . , x$_N$ } and density/PMF = f(x, $\theta$)
-  Let $\hat{\theta _D}$ be an estimated value of $\theta$, example maximum likelihood estimate
-  How do we measure quality of the estimate ?
	-  Square difference from actual parameter.
	-  Square Error ($\hat{\theta _D}$) = ( $\hat{\theta _D}$ - $\theta$ )$^2$
This error is a function of a specific data sample D.
Often, we want the expected square error where expectation is over all possible Ds.

#### Expected square error of the mean estimate
A common estimated parameter is a mean of the distribution.
$\theta$ = $\mu$ = E$_f$(X),   $\hat{\theta}$ = (X$_1$, . . . . , X$_N$)/N
-  Expected square error of the above estimate E$_f$( $\sum_{i}$ X$_i$/N  -  $\theta$ )$^2$  =  $\sigma ^2$/N
where $\sigma ^2$ = E$_f$(X - $\mu$)$^2$
![[Pasted image 20250701102036.png]]

#### Biased and Unbiased Estimator:
-  The estimated parameter $\hat{\theta _D}$ is a random variable since it depends on D which is a random sample.
-  For example: |D| = 3
-  Two different sample and means.
-  An interesting question: what is the expected value $\hat{\theta _D}$ over different random samples D ? How does that compare with true $\theta$ ?
	-  Unbiased: E$_D$($\hat {\theta _D}$) = $\theta$
	-  Biased: E$_D$($\hat {\theta _D}$) $\neq$ $\theta$

![[Pasted image 20250701102639.png]]
![[Pasted image 20250701102650.png]]

![[Pasted image 20250701102702.png]]

#### Consistent Estimator
-  An estimator is consistent if the estimation error goes to zero as N (size of D) goes to infinity.
$\hat {\theta _D}$ $\to$ $\theta$  as  |D| $\to$ $\inf$ 
Example of an unbiased estimator that is not consistent.
-  Parameter $\theta$ = $\mu$ of Gaussian distribution, Lame estimator: just take first element: $\hat {\theta _D}$ = X$_1$
Example of an unbiased, consistent estimator:
-  Parameter $\theta$ = mean of a distribution. $\hat \theta$ = (X$_1$ + . . . + X$_N$ )/N
Example of a biased, consistent estimator:
-  Parameter $\theta$ = $\sigma$ of Gaussian distribution, $\hat \sigma$ is a sample variance.

#### Limitation of MLE:
-  Over-reliance on data sample D. If data is limited, estimates may be very wrong.
	-  Example: Bernoulli p could be 0 if there are no 1's in 10 trials
-  No indication on the uncertainty of the estimated parameters
	-  Example: for a Bernoulli parameters whether estimation is made from two with 50% heads or 1000 examples with 50% heads, the estimated parameter is the same.
-  No mechanism to specify human's prior knowledge of the parameters.

#### Bayesian Estimation:
-  Treat the parameters as a random variable which has a distribution.
-  Step 1: Humans specify their prior knowledge of the values of the parameters as a distribution f$_{pr}$($\theta$) 
	-  Example: f$_{pr}$($\theta$) ~ U(0, 1) where $\theta$ denotes the parameter p of a Bernoulli
	-  Example for Gaussian:
Temperature of CPU on your laptop, T ~ G($\theta$, $\theta ^2$)
f$_{pr}$($\theta$) ~ N(30, 10)
Also called prior probability.

-  Calculate the posterior distribution of parameters after observing data D following Bayes Rule.
![[Pasted image 20250703103916.png]]

#### Using Bayesian estimates:
-  Exact Bayesian probability computation:
	-  Given a new x, calculate f(X | D)
![[Pasted image 20250703104035.png]]

Expected value of parameters: calculate expected value of f($\theta$/D)
![[Pasted image 20250703104229.png]]

Map estimate: use max f($\theta$ | D)
![[Pasted image 20250703104318.png]]

![[Pasted image 20250703104333.png]]

#### Example: Bayesian estimation of Bernoulli/Binomial parameter p
![[Pasted image 20250703104447.png]]
![[Pasted image 20250703104507.png]]

![[Pasted image 20250703104603.png]]
![[Pasted image 20250703104625.png]]
			***Beta distribution is the distribution of probabilities***

![[Pasted image 20250703104733.png]]
![[Pasted image 20250703104745.png]]

#### Overview of parameter estimation
-  We have a density function f(X; $\theta$) whose parameters $\theta$ are unknown
-  We have a dataset D of n independent observations from f
	-  D is random variable denoting X$_1$, X$_2$, . . . , X$_n$ where each X$_i$ ~ f(X; $\theta$)
-  We use any method to get an estimate $\hat \theta$ = A(D),  as some function of D. Thus $\hat \theta$ is also a R.V
	-  Alternative notations $\hat \theta _n$ , $\hat \theta _D$ to stress that estimate depends on D.
![[Pasted image 20250703105414.png]]

![[Pasted image 20250703105428.png]]

![[Pasted image 20250703105438.png]]
![[Pasted image 20250703105451.png]]

![[Pasted image 20250703105507.png]]

![[Pasted image 20250703105524.png]]
![[Pasted image 20250703105535.png]]

****
# Non-Parametric Density Estimation:

#### Motivation:
-  D = { X$_1$, X$_2$, . . . , X$_n$ } sampled i.i.d from an unknown f(X)
-  Estimate $\hat f$ (x) without committing on a specific parametric form of f(X)
-  Why not use empirical CDF ?
	-  Too inefficient to maintain. Need to store entire data
	-  Too jerky. Non-zero density at observed points, zero elsewhere.
-  Density estimation: assume some form of smoothness of f(X)
![[Pasted image 20250704063824.png]]

![[Pasted image 20250704063929.png]]

![[Pasted image 20250704064007.png]]

#### Histogram:
![[Pasted image 20250704064056.png]]
**Example:**
*Figure 20.3 shows three different histograms based on n = 1,266 data points from an astronomical sky survey. Each data point represents the distance from us to a galaxy. The galaxies lie in a "pencilbeam" pointing directly from the Earth out into space. Because of the finite speed of light, looking at galaxies farther and father away corresponds to looking back in time. Choosing the right number of bins involves finding a good tradeoff between bias and variance. We shall see later that top left histogram has too few bins resulting in oversmoothing and too much bias. The bottom left histogram has too many bins resulting in undersmoothing and too few bins. The right histogram is just right. The histogram reveals the presence of clusters of galaxies. Seeing how the size and number of galaxy clusters varies with time, helps cosmologists understand the evolution of the universe.*
![[Pasted image 20250704064920.png]]

![[Pasted image 20250704064952.png]]
![[Pasted image 20250704065006.png]]
![[Pasted image 20250704065018.png]]

#### Kernel Density Estimation:
-  One of the most convenient and accurate ways to estimate any density.
-  Given data sample, D = { X$_1$, X$_2$, . . . . , X$_n$ }
-  Assume a special function called kernel that puts a density mass around each training point:
	-  K(x) is symmetric
	-  $\int _x$ K(x)dx = 1
	-  lim$_{x \to-\inf}$ K(x) = lim$_{x\to+\inf}$K(x) = 0
-  Examples of Kernels:
![[Pasted image 20250704065448.png]]

![[Pasted image 20250704065500.png]]
![[Pasted image 20250704065512.png]]

![[Pasted image 20250704065522.png]]
![[Pasted image 20250704065532.png]]
![[Pasted image 20250704065543.png]]
Resources: [IPYNB Journal](https://colab.research.google.com/github/fbeilstein/machine_learning/blob/master/lecture_15_kernel_density_estimation.ipynb#scrollTo=pGU9KIkxe-FY)

![[Pasted image 20250704070017.png]]
![[Pasted image 20250704070041.png]]
![[Pasted image 20250704070103.png]]
![[Pasted image 20250704070127.png]]
![[Pasted image 20250704070141.png]]
![[Pasted image 20250704070154.png]]

**Comparing Histograms and KDE:**
-  Risk of histogram reduces at rate O(n$^{-2/3}$)
-  Risk of KDE reduces at rate O(n$^{-4/5}$)

![[Pasted image 20250704070331.png]]

****

# Regression:

#### Problem Definition:
-  So far, we have been estimating the density of single random variables f(X)
-  In many applications, we need to reason about the distribution of values of a continuous random variable Y but as a function of some other variables                  x = ( x$_1$, . . . , x$_k$ )
	-  Y is called output of response or dependent variable
	-  ( x$_1$, . . . , x$_k$ ) are called input or covariance or independent variables.
-  We want to estimate the conditional density: f( Y |  x$_1$, . . . , x$_k$ )
-  We are given data samples D of the form:
-  D = {(x$_1$, y$_1$) , . . . , (x$_k$, y$_k$)} = { ( x$_{i1}$, . . . , x$_{ik}$, y$_i$) : i = 1, 2, . . . , n }

#### Motivating Examples:
-  How does errors in assembled circuits (Y) depend on temperature (x1), percentage of copper (x2), humidity (x3)
-  Predict stock price tomorrow (Y) as a function of stock price in the last 7 days     ( x$_1$, . . . , x$_7$ )
-  Express CPU temperature (Y) as a function of workload (x1), ambient temperature (x2), fan-speed (x3), chip model (x4), etc.

![[Pasted image 20250704071430.png]]
![[Pasted image 20250704071442.png]]

![[Pasted image 20250704071457.png]]

![[Pasted image 20250704071511.png]]
![[Pasted image 20250704071524.png]]
![[Pasted image 20250704071548.png]]
![[Pasted image 20250704071555.png]]

![[Pasted image 20250704071612.png]]
![[Pasted image 20250704071624.png]]
![[Pasted image 20250704071636.png]]
![[Pasted image 20250704071646.png]]
![[Pasted image 20250704071658.png]]

#### Estimating $\sigma ^2$
-  Calculate the sum of square of residuals
	-  Residuals = difference between actual y$_i$ and predicted value Bx$_i$ + A
		![[Pasted image 20250704071839.png]]
	-  The MLE estimate would be:
		-  The above biased like for normal Gaussian parameters
		-  We will use a different method:
![[Pasted image 20250704072021.png]]
![[Pasted image 20250704072030.png]]
![[Pasted image 20250704072039.png]]
![[Pasted image 20250704072051.png]]
![[Pasted image 20250704072102.png]]
![[Pasted image 20250704072112.png]]

![[Pasted image 20250704072123.png]]

#### Multi-variable Linear Regression:
![[Pasted image 20250704072212.png]]
![[Pasted image 20250704072224.png]]

![[Pasted image 20250704072234.png]]
![[Pasted image 20250704072243.png]]

![[Pasted image 20250704072253.png]]

![[Pasted image 20250704072306.png]]

![[Pasted image 20250704072406.png]]

![[Pasted image 20250704072438.png]]

![[Pasted image 20250704072538.png]]
![[Pasted image 20250704072552.png]]
Resource: [IPYNB Notebook](https://colab.research.google.com/github/rafiag/DTI2020/blob/main/0  02a_Multi_Linear_Regression_(EN).ipynb)

****

# Non-parametric Regression:

#### Motivation:
-  Linear regression fits a linear line, which might be a poor fit for general datasets.
-  Need a powerful estimator of E(Y | X) without making any assumption about the functional form
-  E( Y | x$_1$, . . . , x$_k$ ) = m(x) where **x =** (x$_1$, . . . , x$_k$)
-  The function m(x) we will derive under the assumption that f(X, Y) and f(X) are both estimated using kernels.
![[Pasted image 20250704073254.png]]
![[Pasted image 20250704073307.png]]

![[Pasted image 20250704073320.png]]
![[Pasted image 20250704073330.png]]
Resource : [IPYNB Notebook](https://colab.research.google.com/github/tufts-ml-courses/cs135-23f-assignments/blob/main/labs/day20-KernelRegression.ipynb)

![[Pasted image 20250704073426.png]]
![[Pasted image 20250704073439.png]]

#### Summary of regression:
-  Linear regression (1-D data)
	-  MLE estimates of slope and intercept
	-  Unbiased chi-squared distribution based estimate of $\sigma ^2$
-  Distribution of parameters
-  Linear Regression (Arbitrary k)
	-  Just the derivation of MLE estimate
-  Kernel regression
	-  Just the final estimate

****

# Time Series:

#### What is time-series ?
Sequence of values recorded at regular time intervals
-  Time interval: E.g. Weekly, monthly, daily, hourly, annually, etc.
-  Values recorded:
	-  Scalar: single value like sales
	-  Vector of values

#### Motivation:
-  Daily traffic on individual webpages from different regions in Wikipedia
-  Hourly load on various servers of different services in a Data center
-  Monthly demand for products from different regions in Flipkart
-  Stock price of various companies
-  Rice production in Maharashtra each year
-  Consumer price index of various food items

#### Objective of time series analysis:
-  Identify characteristics if the time-series
	-  Provide a model of the data (e.g., test specific hypothesis)
-  Forecasting 
	-  Predict future values as a function of past values
![[Pasted image 20250705110117.png]]
-  Finding outliers and filling in missing values
-  Provide a compact description of the data (data compression)

#### Important characteristics of time-series
-  Is there a **trend**, meaning that, on an average, the measurements tend to increase (or decrease) over time ?
-  Is there **seasonality**, meaning that there is a regularly repeating pattern of highs and lows related to calendar time such as seasons, quarters, months, days of the week, and so on ?
-  Are there **outliers** ? In regression, outliers are far away from your line. With time series data, your outliers are far away from your other data.
-  Is there a **cycle**: data rises and falls but without a fixed frequency
-  Is there **constant variance** over time, or is the variance non-constant ?
-  Are there any **abrupt changes** to either the level of the series or the variance ?
![[Pasted image 20250705111731.png]]
![[Pasted image 20250705111811.png]]

![[Pasted image 20250705111823.png]]

![[Pasted image 20250705111850.png]]
![[Pasted image 20250705111932.png]]

![[Pasted image 20250705111943.png]]

#### Limitation of regression models
-  Does not account for strong temporal correlation among values
-  Predicts each value independent of its neighbors
-  Need a model that can directly exploit correlations within a series

![[Pasted image 20250705112352.png]]

![[Pasted image 20250705112403.png]]
![[Pasted image 20250705112414.png]]


![[Pasted image 20250705112426.png]]
![[Pasted image 20250705112436.png]]

#### Models for time-series:
-  Auto-regressive models AR(p):
-  Moving average models MA
-  ARIMA models (Combines the above two)
-  SARIMA: Generalization of ARIMA to handle seasonality

![[Pasted image 20250705112609.png]]

![[Pasted image 20250705144922.png]]

![[Pasted image 20250705144931.png]]
![[Pasted image 20250705144939.png]]

![[Pasted image 20250705144950.png]]
![[Pasted image 20250705145003.png]]
![[Pasted image 20250705145016.png]]

![[Pasted image 20250705145029.png]]

![[Pasted image 20250705145043.png]]

![[Pasted image 20250705145052.png]]

![[Pasted image 20250705145103.png]]

#### Moving average models (MA models)
-  A value x$_t$ in a time-series sometimes cannot be explained just in terms of its past vales.
-  External (unknown) variables might be influencing the values:
	-  Example: Total wheat export of India in 2023 can be determined by wheat export in 2022, but also other external factors like weather patterns, wars, exchange rates, etc.
-  External variables are also time-varying $\to$ errors at each position cannot be independent.
-  Moving average models capture dependency on such external unknowns.
![[Pasted image 20250705145545.png]]

![[Pasted image 20250705145557.png]]
![[Pasted image 20250705145605.png]]
![[Pasted image 20250705145723.png]]

![[Pasted image 20250705145615.png]]

![[Pasted image 20250705145645.png]]
![[Pasted image 20250705145759.png]]

![[Pasted image 20250705145813.png]]
![[Pasted image 20250705145828.png]]

#### Choosing p, q:
Data may follow an ARIMA(p, d, 0) model if the ACF and PACF plots of the differenced data show the following patterns:
-  the ACF is exponentially decaying or sinusoidal
-  there is a significant spike at lag p in the PACF, but none beyond lag p
The data may follow an ARIMA(0, d, q) model if the ACF and PACF plots of the differenced data show the following patterns:
-  The PACF is exponentially decaying or sinusoidal
-  There is a significant spike at lag q in the ACF; but none beyond lag q
Tips : [Link](https://otexts.com/fpp3/non-seasonal-arima.html#acf-and-pacf-plots)

![[Pasted image 20250705151324.png]]
![[Pasted image 20250705151334.png]]
![[Pasted image 20250705151344.png]]

#### ARIMA(p, d, q) models
-  p is the order of the autoregressive part,
-  d is the degree of first difference involved,
-  q is the order of the moving average part.
Example: ARIMA(2, 1, 1) model

#### Incorporating Seasonality
Seasonality in a time series is a regular pattern that repeats over S time periods.
-  Example: monthly seasonality repeats over S = 12 (months of the year)
-  Example: quarter seasonality repeats over S = 4 period
Extending ARIMA to handle seasonality. One or more of the above might work
-  Introduce a AR term x$_{t-s}$ in the model for every period S
-  Introduce MA term w$_{t-s}$ in the model for every period S
-  Create seasonal differences y$_t$ = x$_t$ - x$_{t-s}$
Refer: [Notes](https://colab.research.google.com/drive/1Z4zNI_bVXoFQBsCHUtxBDCBno6yhXceB?usp=sharing#scrollTo=deWKK_D1mNlr)

****

# Multivariate Analysis

#### Multivariate Data:
**Data reduction or summarization** - Studying data as simply as possible without sacrificing useful information
**Sorting and grouping** - Clustering similar object together
**Investigating dependence among variables** - Mutual independence, conditional independence, etc. (already done)
**Prediction** - Regression (already done)
**Hypothesis testing** - Validate assumptions

![[Pasted image 20250706094328.png]]
![[Pasted image 20250706094345.png]]
![[Pasted image 20250706094358.png]]

![[Pasted image 20250706094410.png]]
![[Pasted image 20250706094422.png]]

![[Pasted image 20250706094439.png]]
![[Pasted image 20250706094453.png]]


![[Pasted image 20250706094536.png]]

![[Pasted image 20250706094645.png]]
![[Pasted image 20250706094657.png]]

![[Pasted image 20250706094708.png]]

![[Pasted image 20250706094721.png]]
![[Pasted image 20250706094733.png]]
![[Pasted image 20250706094744.png]]
![[Pasted image 20250706094755.png]]

![[Pasted image 20250706094807.png]]

![[Pasted image 20250706094823.png]]
![[Pasted image 20250706094831.png]]

![[Pasted image 20250706094841.png]]
![[Pasted image 20250706094855.png]]

#### Multidimensional Gaussian Distribution:
![[Pasted image 20250706094933.png]]
![[Pasted image 20250706094942.png]]
![[Pasted image 20250706094950.png]]
![[Pasted image 20250706094959.png]]
![[Pasted image 20250706095012.png]]
![[Pasted image 20250706095022.png]]
![[Pasted image 20250706095031.png]]
![[Pasted image 20250706095040.png]]
![[Pasted image 20250706095052.png]]
![[Pasted image 20250706095100.png]]


![[Pasted image 20250706095120.png]]
![[Pasted image 20250706095128.png]]
![[Pasted image 20250706095139.png]]

Reading Material: [Notes]([Lesson 2: Linear Combinations of Random Variables | STAT 505](https://online.stat.psu.edu/stat505/lesson/2))

![[Pasted image 20250706095230.png]]
![[Pasted image 20250706095241.png]]
![[Pasted image 20250706095253.png]]

![[Pasted image 20250706095304.png]]
![[Pasted image 20250706095313.png]]

![[Pasted image 20250706095326.png]]

More Examples: [Examples]([4.1 - Comparing Distribution Types | STAT 505](https://online.stat.psu.edu/stat505/lesson/4/4.1#paragraph--384))

![[Pasted image 20250706095441.png]]
![[Pasted image 20250706095457.png]]
![[Pasted image 20250706113425.png]]

#### Conditional distribution for bivariate case:
![[Pasted image 20250706113501.png]]

![[Pasted image 20250706113522.png]]

Demos: [Link](https://colab.research.google.com/github/goodboychan/goodboychan.github.io/blob/main/_notebooks/2021-08-11-Multivariate-distribution.ipynb)

![[Pasted image 20250706113636.png]]
![[Pasted image 20250706113648.png]]
![[Pasted image 20250706113705.png]]
![[Pasted image 20250706113719.png]]

Notes: [Link]([4.5 - Eigenvalues and Eigenvectors | STAT 505](https://online.stat.psu.edu/stat505/lesson/4/4.5#paragraph--388))

![[Pasted image 20250706113758.png]]

![[Pasted image 20250706113812.png]]

## Principal component analysis:
#### Projecting high-dimensional data:
-  When multivariate dataset has a large number of variables, analysis and interpretation of the data may be hard.
-  Too many variable pairs, so pairwise correlation may be hard to grasp.
-  For convenient visualization and interpretation 
	-  Reduce the number of variables
-  How to reduce number of variables while capturing most of the information in the data
	-  Information == variance
![[Pasted image 20250706114145.png]]

#### How to reduce number of variables: many methods
-  Principal component analysis
-  Factor analysis
-  Other embedding methods
	-  Ransom projection
	-  T-SNE
![[Pasted image 20250706114256.png]]

![[Pasted image 20250706114314.png]]

![[Pasted image 20250706114531.png]]

![[Pasted image 20250706114542.png]]

![[Pasted image 20250706114552.png]]

![[Pasted image 20250706115010.png]]
![[Pasted image 20250706115022.png]]

![[Pasted image 20250706115036.png]]
![[Pasted image 20250706115048.png]]
![[Pasted image 20250706115057.png]]

![[Pasted image 20250706114652.png]]

Notes: [IPYNB Notes](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.09-Principal-Component-Analysis.ipynb)

![[Pasted image 20250706115141.png]]

#### T-SNE: T-distributed stochastic neighborhood embedding

Reading Material: [Notes](https://www.dailydoseofds.com/formulating-and-implementing-the-t-sne-algorithm-from-scratch/)

-  Another data projection method, specifically designed for visualizing high dimensional data in 2 dimensions.
-  Preserves local similarities and clusters better than PCA
-  Creates non-linear projection

Demos:
-  https://projector.tensorflow.org
-  https://distill.pub/2016/misread-tsne/

![[Pasted image 20250706115935.png]]
![[Pasted image 20250706115947.png]]

![[Pasted image 20250706115959.png]]

****

# Hypothesis Testing

#### Introduction:
-  Hypothesis testing is key to scientific inquiry
-  We just have some hypothesis H
-  To check it we collect data D
-  We check if H is consistent with D
	-  Consistency is probabilistic, and there is no 0/1 answer
-  Example:
	-  Say you got a shipment of cables, and average breaking strength is claimed to be at least 7000 pounds per square inch (PSI)
	-  D = You tested 10 random cables and record PSI of each
	-  Hypothesis: PSI >= 7000
	-  Hypothesis testing: Is the hypothesis consistent with observed data ?
-  More Real World Examples:
	-  Number of clicks on the video is at least 100
	-  Average order value has increased since last financial year
	-  Investing in A brings a higher return than investing in B
	-  The new user interface converts more users into customers than the expected 30%
#### Types of hypothesis testing:

**Parametric vs. Non-parametric:**
Parametric
-  Assume that the underlying data distribution has a known parametric form. E.g., Normal or exponential
Non-Parametric
-  Unknown functional form of the distribution

**One-sample vs. Two-sample:**
-  One-sample: D = sample of one distribution
-  Two-sample: D1, D2 = samples from 2 different distributions. Hypothesis is comparing them

**Paired vs. Unpaired:**


#### Parametric Hypothesis Testing for a single population:
![[Pasted image 20250707081612.png]]
![[Pasted image 20250707081624.png]]
![[Pasted image 20250707081635.png]]
![[Pasted image 20250707081644.png]]
![[Pasted image 20250707081654.png]]
![[Pasted image 20250707081708.png]]
![[Pasted image 20250707081719.png]]
![[Pasted image 20250707081729.png]]
![[Pasted image 20250707081743.png]]
![[Pasted image 20250707081757.png]]
![[Pasted image 20250707081811.png]]

![[Pasted image 20250707081824.png]]
![[Pasted image 20250707081836.png]]
![[Pasted image 20250707081847.png]]
![[Pasted image 20250707081857.png]]
![[Pasted image 20250707081911.png]]

Resources: [Link](http://courses.atlas.illinois.edu/spring2016/STAT/STAT200/pt.html)

![[Pasted image 20250707081959.png]]
![[Pasted image 20250707082014.png]]
![[Pasted image 20250707082034.png]]
![[Pasted image 20250707082044.png]]

![[Pasted image 20250707082057.png]]

#### Parametric Hypothesis Testing for two populations:
![[Pasted image 20250707082143.png]]
![[Pasted image 20250707082155.png]]
![[Pasted image 20250707082203.png]]

![[Pasted image 20250707082215.png]]
![[Pasted image 20250707082223.png]]

![[Pasted image 20250707082237.png]]
![[Pasted image 20250707082246.png]]
![[Pasted image 20250707082258.png]]

![[Pasted image 20250707082311.png]]
![[Pasted image 20250707082324.png]]
![[Pasted image 20250707082337.png]]

****

# Non-Parametric Hypothesis Testing

#### Non-Parametric Tests
-  We make no assumptions of the form of the distribution function unlike previous cases where we assume Normal or Binomial
-  Generically denote distribution as F(X). Note form of F(X) is unknown
-  Possible hypothesis that can be tested in such cases
	-  What is the median of F(X) ?  - Sign test
	-  Is the distribution around the median similar  - Sign rank test
	-  Given samples of two distributions: Are they likely to be from the same or different distributions ?  - Two sample test
![[Pasted image 20250707082733.png]]
![[Pasted image 20250707082744.png]]
![[Pasted image 20250707082757.png]]

![[Pasted image 20250707082808.png]]
![[Pasted image 20250707082818.png]]
![[Pasted image 20250707082830.png]]
![[Pasted image 20250707082841.png]]
![[Pasted image 20250707082850.png]]
![[Pasted image 20250707082900.png]]

****
### How to extend paired t-test to the non-parametric case ?
****

#### Are two distributions equal ?
Let F and G be two continuous distributions of unknown form 
Given
-  n samples X$_1$, X$_2$, . . . , X$_n$  from F
-  m samples Y$_1$, Y$_2$, . . . , Y$_n$  from G
Null hypothesis: H$_0$ : F = G
Test is called: Rank-sum test, Mann-Whitney test, Wilcoxon test 
Rank order the n + m items
	R$_i$ = rank of the data value X$_i$
Test statistic:
	T = $\sum_{i = 1}^{n}$ R$_i$

![[Pasted image 20250707083553.png]]

![[Pasted image 20250707083604.png]]
![[Pasted image 20250707083612.png]]
![[Pasted image 20250707083621.png]]

#### Errors in Hypothesis Testing
**Type-I error:**  Rejecting H$_0$ even when H$_0$ is true.
-  The probability with which it happens is called significant level $\alpha$
**Type-II error:**  Accepting H$_0$ when it is false

#### Summary of Hypothesis Testing:
Follow this framework:
-  Formulate null and alternative hypothesis
-  Collect data
-  Decide on test static
-  Identify distribution of test static under null hypothesis
-  Apply p-value or critical region test to accept or reject null hypothesis
We applied this framework on
-  Mean of Gaussian with unknown variance is $\mu_0$ 
-  Are means of two normal distributions with shared variance same ?
-  Difference in means of two normal with unknown variance from paired observations

#### Summary . .
Parameter p of Bernoulli is p$_0$
Non-parametric tests
-  Median is a given value
-  Distribution is symmetric around a median
-  Are two distributions equal

#### Topics not covered.
-  Goodness of fit tests
-  Test on sequences

****

# Robust Statistics

#### Motivation
-  Real world data often contains outliers or extreme values
-  Most methods discussed so far on inferring models or parameter values from data can be adversely affected by outliers 
	-  Example: estimates of mean and variance from data
	-  Estimation of linear regression parameters
-  Robust statistics attempts to fit models that are largely unaffected by outliers, and fit based on "majority" of normal data
-  Robust fit enable better detection of outliers, as values that deviate from the fitted model.
![[Pasted image 20250707085855.png]]
![[Pasted image 20250707085904.png]]
![[Pasted image 20250707085918.png]]

![[Pasted image 20250707085927.png]]
![[Pasted image 20250707085944.png]]
![[Pasted image 20250707085953.png]]

**Robustness:** being less influenced by outliers
**Efficiency:** being precise at uncontained data
***Robust estimators aim to combine high robustness with high efficiency***

![[Pasted image 20250707090134.png]]

#### Characterizing robustness
-  Breakdown value
-  Sensitivity curve
-  Influence function

![[Pasted image 20250707090226.png]]
![[Pasted image 20250707090247.png]]

![[Pasted image 20250707090257.png]]
![[Pasted image 20250707090306.png]]

![[Pasted image 20250707090322.png]]
![[Pasted image 20250707090333.png]]

![[Pasted image 20250707090342.png]]
![[Pasted image 20250707090353.png]]
![[Pasted image 20250707090401.png]]
![[Pasted image 20250707090422.png]]
![[Pasted image 20250707090431.png]]
![[Pasted image 20250707090439.png]]

![[Pasted image 20250707090500.png]]
Notes: [Link](https://online.stat.psu.edu/stat501/lesson/t/t.1/t.1.1-robust-regression-methods)

![[Pasted image 20250707090543.png]]
![[Pasted image 20250707090556.png]]
![[Pasted image 20250707090608.png]]
![[Pasted image 20250707090620.png]]

Resource Notes: [IPYNB Notes](https://colab.research.google.com/github/pymc-devs/pymc-examples/blob/main/examples/generalized_linear_models/GLM-robust.ipynb#scrollTo=285a756b)

![[Pasted image 20250707090726.png]]
![[Pasted image 20250707090736.png]]

****

# Revision on Geometry of Multivariate Gaussian

![[Pasted image 20250707090824.png]]
![[Pasted image 20250707090834.png]]
![[Pasted image 20250707090844.png]]

![[Pasted image 20250707090854.png]]
![[Pasted image 20250707090906.png]]
![[Pasted image 20250707090915.png]]
![[Pasted image 20250707090926.png]]

# Course Summary

![[Pasted image 20250707090959.png]]
![[Pasted image 20250707091006.png]]
![[Pasted image 20250707091016.png]]
![[Pasted image 20250707091024.png]]
![[Pasted image 20250707091035.png]]
![[Pasted image 20250707091044.png]]
![[Pasted image 20250707091051.png]]
![[Pasted image 20250707091059.png]]
![[Pasted image 20250707091108.png]]

****
