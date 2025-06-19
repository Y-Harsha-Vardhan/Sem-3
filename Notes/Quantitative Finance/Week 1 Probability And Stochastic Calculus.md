

# Day 1: Foundations of Probability Theory

---

## 1. Basic Probability Concepts and Definitions

### Sample Space and Events

- **Sample Space (Ω)**: The set of all possible outcomes of an experiment
- **Event (A)**: A subset of the sample space
- **Elementary Event**: A single outcome from the sample space

**Example:** Rolling a fair six-sided die

- Sample Space: Ω = {1, 2, 3, 4, 5, 6}
- Event A (rolling an even number): A = {2, 4, 6}
- Elementary Event: Rolling a 3

### Probability Axioms (Kolmogorov Axioms)

1. **Non-negativity**: P(A) ≥ 0 for all events A
2. **Normalization**: P(Ω) = 1
3. **Countable Additivity**: For mutually exclusive events A₁, A₂, ...:
$P(A₁ ∪ A₂ ∪ ...) = P(A₁) + P(A₂) + ...$

### Some Properties

- **Complement Rule**: $P(Aᶜ) = 1 - P(A)$
- **Addition Rule**: $P(A ∪ B) = P(A) + P(B) - P(A ∩ B)$
- **Empty Set**: $P(∅) = 0$

![](https://youtu.be/1uW3qMFA9Ho)

---

## 2. Conditional Probability and Independence

### Conditional Probability

P(A|B) = P(A ∩ B) / P(B), provided P(B) > 0

The probability of event A occurring given that event B has occurred is the probability 

of A and B both happening divided by the probability that event B happens which makes sense 

intuitionally as well .

### Law of Total Probability

If B₁, B₂, ..., Bₙ form a partition of Ω, then:
$P(A) = Σ P(A|Bᵢ) × P(Bᵢ)$

### Bayes' Theorem for conditional probability

$P(A|B) = [P(B|A) × P(A)] / P(B)$

### Independence

Events A and B are independent if:
$P(A ∩ B) = P(A) × P(B)$

Equivalently: $P(A|B) = P(A)$ and $P(B|A) = P(B)$

---

## 3. Random Variables

### Definition

A random variable X is a function from the sample space Ω to the real numbers ℝ:
X: Ω → ℝ

### Types of Random Variables

1. **Discrete Random Variables**: Countable range
2. **Continuous Random Variables**: Uncountable range

### Probability Mass Function (PMF)

For discrete random variable X:
$pₓ(x) = P(X = x)$

Properties:

- pₓ(x) ≥ 0 for all x
- Σ pₓ(x) = 1 (sum over all possible values)

### Probability Density Function (PDF)

For continuous random variable X:

- $P(a ≤ X ≤ b) = ∫ₐᵇ fₓ(x) dx$

Properties:

- $fₓ(x) ≥ 0 for all x$

$\int_{-\infty}^{\infty} f_x(x)\, dx = 1$

---

## 4. Some Common Probability Distributions

### Discrete Distributions

**Bernoulli Distribution**

- Parameter: p (success probability)
- PMF: $P(X = 1) = p, P(X = 0) = 1-p$
- Mean: μ = p
- Example is a single coin toss with Heads being probability p and tails 1-p

**Binomial Distribution**

- Parameters: n (trials), p (success probability)

$$
PMF: P(X = k) = C(n,k) × pᵏ × (1-p)ⁿ⁻ᵏ
$$

- Example is multiple coin tosses where each heads has probability p and tails 1-p

**Poisson Distribution**

- Parameter: λ (rate)
- PMF: $P(X = k) = (λᵏ × e⁻λ) / k!$

### Continuous Distributions

**Uniform Distribution**

- Parameters: a, b (interval endpoints)

PDF: $f(x) = 1/(b-a)$ for $a ≤ x ≤ b$

**Normal Distribution**

- Parameters: μ (mean), σ² (variance)
- PDF: $f(x) = (1/√(2πσ²)) × exp(-(x-μ)²/(2σ²))$

![](https://youtu.be/B5y6fy5iUtg)

---

## 5. Worked Examples

### Example 1: Conditional Probability

A bag contains 5 red balls and 3 blue balls. Two balls are drawn without replacement.

- Find P(second ball is red | first ball is red)

**Solution:**

- After drawing one red ball: 4 red, 3 blue remain (7 total)
- P(second red | first red) = 4/7

### Example 2: Bayes' Theorem

A medical test is 95% accurate for detecting a disease that affects 1% of the population.

- Find P(disease | positive test)

**Solution:**

- P(D) = 0.01, P(D') = 0.99
- P(+|D) = 0.95, P(+|D') = 0.05
- $P(+) = P(+|D)P(D) + P(+|D')P(D') = 0.95(0.01) + 0.05(0.99) = 0.059$
- $P(D|+)$ = $P(+|D)P(D) / P(+) = (0.95)(0.01) / 0.059 ≈ 0.161$

## Resources for Further Reading

- Ross, S. "A First Course in Probability"
- Grimmett, G. & Stirzaker, D. "Probability and Random Processes"
- Online: Khan Academy Probability and Statistics

# Day 2: Expectation, Variance, and Joint Distributions

---

## 1. Expectation and Moments

### Expected Value (Mean)

**Discrete Random Variable**: $E[X] = \sum_x x \cdot P(X = x)$
**Continuous Random Variable**: $E[X] = \int_{-\infty}^\infty x f(x) dx$

The expected value is ***the mean of the possible values a random variable can take***, weighted by the probability of those outcomes.

### Properties of Expectation

1. **Linearity**: $E[aX + bY] = aE[X] + bE[Y]$
2. **Constant**: $E[c] = c$ for any constant c
3. **Independence**: If X and Y are independent, $E[XY] = E[X]E[Y]$

### Law of the Unconscious Statistician (LOTUS)

For function g(X):
**Discrete**: $E[g(X)] = Σₓ g(x) · P(X = x)$
**Continuous**: $E[g(X)] = \int_{-\infty}^{\infty} g(x) f(x) dx$ where f is pdf

We are simply just extending the standard definition of expectation to functions

### Variance and Standard Deviation

**Variance**: $Var(X) = E[(X - μ)²] = E[X²] - (E[X])²$

The proof for this is very simple to do, try to do it by self.

**Standard Deviation**: $σ(X) = √Var(X)$

### Properties of Variance

1. **Constant**: $Var(aX + b) = a²Var(X)$
2. **Independence**: If X and Y are independent, $Var(X + Y) = Var(X) + Var(Y)$
3. **General case**: $Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)$

### Moments:

Moments in statistics are **quantitative measures (or a set of statistical parameters) that describe the specific characteristics of a probability distribution**. In simple terms, the moment measures how spread out or concentrated the number in a dataset is around the central value, such as the mean.

### Higher Moments

**k-th moment**: $E[Xᵏ]$
**k-th central moment**: $E[(X - μ)ᵏ]$

The following are terms you should remember:

**Skewness**: γ₁ = $E[(X - μ)³]/σ³$
**Kurtosis**: γ₂ = $E[(X - μ)⁴]/σ⁴$

---

## 2. Moment Generating Functions

### Definition

The **moment generating function (MGF)** of random variable X is:
$M_X(t) = E[e^{tX}]$ for t in some neighborhood of 0

### Properties of MGF

1. **Uniqueness**: MGF uniquely determines the distribution
2. **Moments**:  $E[X^n] = M_X^{(n)}(0)$      (n-th derivative at 0)
3. **Independence**: If X and Y are independent, $M_{X+Y}(t) = M_X(t)M_Y(t)$
4. **Linear transformation**: $M_{(aX+b)}(t) = e^{(bt)} · M_X(at)$

### Common MGFs

| **Distribution** | **MGF** |
| --- | --- |
| Bernoulli(p) | `$1 - p + pe^t$` |
| Binomial(n,p) | `$(1 - p + pe^t)^n$` |
| Poisson(λ) | `$exp(λ(e^t - 1))$` |
| Normal(μ,σ²) | `$exp(μt + σ²t²/2)$` |
| Exponential(λ) | `$λ/(λ - t), t < λ$` |

### Characteristic Functions

**Definition**: $φ_X(t) = E[e^{i*t*X}]$ (always exists)
**Properties**: Similar to MGF but using complex exponentials

---

## 3. Joint Distributions and Dependence

We can also define probability mass and distribution functions for more than 1 random variable:

### Joint Probability Mass Function (Discrete)

For discrete random variables X and Y:
$p_{X,Y}(x,y) = P(X = x, Y = y)$

### Joint Probability Density Function (Continuous)

For continuous random variables X and Y:
$P(a ≤ X ≤ b, c ≤ Y ≤ d) = ∫_c^d ∫_a^b f(X,Y)(x,y) dx dy$

### Marginal Distributions

This really refers to distributions of 1 random variable given no restriction/constraint on other

**Discrete**: $p_X(x) = Σ_y p_{(X,Y)}(x,y)$
**Continuous**: $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy$

### Conditional Distributions

**Discrete**: $P(Y = y | X = x) = p_(X,Y)(x,y) / p_X(x)$
**Continuous**: $f_(Y|X)(y|x) = f_(X,Y)(x,y) / f_X(x)$

### Independence of Random Variables

X and Y are said to be independent iff the following condition holds: 
**Discrete**: $p_{(X,Y)}(x,y) = p_X(x) · p_Y(y)$ for all $x,y$
**Continuous**: $f_{(X,Y)}(x,y) = f_X(x) · f_Y(y)$ for all x,y

---

## 4. Covariance and Correlation

### Covariance

$Cov(X,Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$ (due to linearity of expectation)

### Properties of Covariance

1. $Cov(X,X) = Var(X)$
2. $Cov(X,Y) = Cov(Y,X)$ (symmetric)
3. $Cov(aX + b, cY + d) = ac·Cov(X,Y)$
4. If X and Y are independent, $Cov(X,Y) = 0$ (converse not always true)

### Correlation Coefficient

$ρ(X,Y) = Cov(X,Y) / (σ_X · σ_Y)$ where $σ_X$ and $σ_Y$ refer to the standard deviations of random variables X and Y , NOT the variance keep this in mind.

### Properties of Correlation

1. $-1 ≤ ρ(X,Y) ≤ 1$
2. $|ρ(X,Y)| = 1$ if and only if $Y = aX + b$ for some constants a,b
3. $ρ(X,Y) = 0$ implies X and Y are uncorrelated (but not necessarily independent)

---

## 5. Advanced Distributions

### Multivariate Normal Distribution

For random vector $X = (X₁, X₂, ..., Xₙ):$
$f(\mathbf{x}) = \frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\mu)^T \Sigma^{-1} (\mathbf{x}-\mu)\right)$

where **μ** is the mean vector and Σ is the covariance matrix.

### Bivariate Normal

For $X ~ N(μ₁, σ₁²)$ and $Y ~ N(μ₂, σ₂²)$ with correlation $ρ$:

$f(x,y) = 1/(2πσ₁σ₂√(1-ρ²)) exp(-Q/2(1-ρ²))$

where $Q = (x-μ₁)²/σ₁² - 2ρ(x-μ₁)(y-μ₂)/(σ₁σ₂) + (y-μ₂)²/σ₂²$

### Gamma Distribution

X ~ Gamma(α, β) has PDF:
$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}, \quad x > 0$

**Mean**: $E[X] = α/β$
**Variance**: $Var(X) = α/β²$
**MGF**: $M(t) = (β/(β-t))^α$ for $t < β$

### Beta Distribution

X ~ Beta(α, β) has PDF:
$f(x) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} x^{\alpha-1} (1-x)^{\beta-1}, \quad 0 < x < 1$ for 0 < x < 1

**Mean**: $E[X] = α/(α+β)$
**Variance**: $Var(X) = αβ/[(α+β)²(α+β+1)]$

### Chi-Square Distribution

If $Z₁, Z₂, ..., Zₙ$ are independent $N(0,1)$, then $X = Z₁² + Z₂² + ... + Zₙ² ∼ χ²(n)$

**Mean**: $E[X] = n$
**Variance**: $Var(X) = 2n$
**MGF**: $M(t) = (1-2t)$ raised to the $(-n/2)$ for $t < 1/2$

---

## 6. Transformations of Random Variables

### Function of One Random Variable

If Y = g(X) where g is monotonic:
$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|$

### Linear Transformation

If $Y = aX + b:$

- $E[Y] = aE[X] + b$
- $Var(Y) = a²Var(X)$
- $M_Y(t) = e^(bt) M_X(at)$ where M is moment generating function

### Sum of Independent Random Variables

If X and Y are independent:

- $E[X + Y] = E[X] + E[Y]$
- $Var(X + Y) = Var(X) + Var(Y)$
- $M_{X+Y}(t) = M_X(t) · M_Y(t)$

### Special Cases

**Sum of Normals**: If $X ∼ N(μ₁, σ₁²)$ and $Y ∼ N(μ₂, σ₂²)$ are independent,
then $X+Y∼N(μ₁ + μ₂, σ₁² + σ₂²)$

**Sum of Poissons**: If $X ∼ Poisson(λ₁)$ and $Y ∼ Poisson(λ₂)$ are independent,
then $X + Y ∼ Poisson(λ₁ + λ₂)$

---

## 7. Few problems on Expectations and Variances

Do try the problems before reading the solution for maximum benefit!

### Problem 1: Expected Stock Returns

A stock has the following return distribution:

- +20% with probability 0.3
- +10% with probability 0.4
- 5% with probability 0.2
- 15% with probability 0.1

Find the expected return and risk (standard deviation).

**Solution:**
$E[R] = 0.3(0.20) + 0.4(0.10) + 0.2(-0.05) + 0.1(-0.15) = 0.06 + 0.04 - 0.01 - 0.015 = 0.075 = 7.5%$

$E[R²] = 0.3(0.20)² + 0.4(0.10)² + 0.2(-0.05)² + 0.1(-0.15)² = 0.012 + 0.004 + 0.0005 + 0.00225 = 0.01875$

$Var(R) = E[R²] - (E[R])² = 0.01875 - (0.075)² = 0.01875 - 0.005625 = 0.013125$

$σ(R) = √0.013125 ≈ 11.46$

### Problem 2: Expected Coin Flips

How many flips do you expect before getting your first heads?

**Solution**:
Let E = expected number of flips.

**Thinking step by step**:

- First flip: If heads (prob 1/2), we're done → 1 flip
- First flip: If tails (prob 1/2), we start over → 1 + E flips

**Setting up the equation**:
E = (1/2) × 1 + (1/2) × (1 + E)
E = 1/2 + 1/2 + E/2
E = 1 + E/2
E - E/2 = 1
E/2 = 1
**E = 2**

**Intuition**: On average, you need 2 flips to get your first heads. Makes sense because half the time you get it immediately, half the time you need to "start over."

### Problem 3: Dice Expected Value Puzzle

Roll a fair six-sided die repeatedly. What's the expected number of rolls to see all six faces?

**Solution:**
This is the "Coupon Collector Problem."

Let $T_k$ = number of additional rolls needed to see a new face when you've already seen k distinct faces.

$T_k$ ~ $Geometric(p_k)$ where $p_k = (6-k)/6$

$E[T_k] = 1/p_k = 6/(6-k)$

Total expected rolls: $E[T] = E[T_0] + E[T_1] + ... + E[T_5]$
$= 6/6 + 6/5 + 6/4 + 6/3 + 6/2 + 6/1
= 6(1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6)
= 6 × H_6 ≈ 6 × 2.45 ≈ 14.7 rolls$

### Problem 4: Expected Winnings

Start with $0. Flip a coin repeatedly:

- Heads: win $1
- Tails: lose $1

What are your expected winnings after n flips?

**Solution**:
Let $X_i$ = winnings from flip i

- $X_i$= +1 with probability 1/2
- $X_i$= -1 with probability 1/2

$E[X_i] = (1/2)(1) + (1/2)(-1) = 0$

Total winnings after n flips $=X_1 + X_2 + ... + X_n$

$E[Total] = E[X_1] + E[X_2] + ... + E[X_n] = 0 + 0 + ... + 0 = 0$

**Intuition**: Fair game means zero expected winnings. You're equally likely to be ahead or behind.

---

## Quick Recap

**Expectation**: $E[X] = Σx·P(X=x) or ∫x·f(x)dx$

**Variance**: $Var(X) = E[X²] - (E[X])²$

**MGF**: $M_X(t) = E[e^(tX)], E[Xⁿ] = M_X^(n)(0)$

**Covariance**: $Cov(X,Y) = E[XY] - E[X]E[Y]$

**Correlation**: $ρ(X,Y)$ = $Cov(X,Y)/(σ_X σ_Y)$

**Portfolio Variance**: $σ_P²$ = $w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂$

---

## Distribution Reference Table

| Distribution | Parameters | Mean | Variance | MGF |
| --- | --- | --- | --- | --- |
| Bernoulli | $p$ | $p$ | $p(1-p)$ | $1-p+pe^t$ |
| Binomial | n,p | $np$ | $np(1-p)$ | $(1-p+pe^t)ⁿ$ |
| Poisson | λ | λ | λ | $exp(λ(e^t-1))$ |
| Geometric | p | 1/p | $(1-p)/p²$ | $pe^t/(1-(1-p)e^t)$ |
| Uniform | a,b | $(a+b)/2$ | $(b-a)²/12$ | $(exp(bt)-exp(at))/(t(b-a))$ |
| Normal | $μ,σ²$ | μ | $σ²$ | $exp(μt+σ²t²/2)$ |
| Exponential | $λ$ | 1/λ | $1/λ²$ | $λ/(λ-t)$ |
| Gamma | $α,β$ | $α/β$ | $α/β²$ | $(β/(β-t))^α$ |

---

Practice Problems and further resources:

### Brainstellar

- Probability and Expectation problems

### **MIT OpenCourseWare**

- 18.22 [**Introduction to Probability and Statistics](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/) by Jeremy Orloff**

### **"A First Course in Probability" by Sheldon Ross**

- **Chapters for practice**:
    - Ch 1: Combinatorics (counting problems)
    - Ch 2: Basic probability axioms
    - Ch 3: Conditional probability and independence
    - Ch 4: Random variables and expectation
    - Ch 5: Continuous random variables

# Day 3: Probability Inequalities and Convergence

---

## 1. Fundamental Probability Inequalities

### Markov's Inequality

**Statement**: For non-negative random variable X and a > 0:
$P(X ≥ a) ≤ E[X]/a$

**Proof**:
$E[X] = ∫₀^∞ x f(x) dx ≥ ∫ₐ^∞ x f(x) dx ≥ a ∫ₐ^∞ f(x) dx = a P(X ≥ a)$

**Applications**:

- Provides upper bound when only mean is known
- Foundation for other inequalities
- Used in algorithm analysis

![](https://www.youtube.com/watch?v=vjYanZ1nsZg&pp=ygU3cHJvYmFiaWxpdHkgaW5lcXVhbGl0aWVzIGFuZCBjb252ZXJnZW5jZSBhbmQgZGl2ZXJnZW5jZQ%3D%3D)

### Chebyshev's Inequality

**Statement**: For any random variable X with finite mean μ and variance σ²:
$P(|X - μ| ≥ kσ) ≤ 1/k² \quad for \quad k > 0$

**Equivalent forms**:

- $P(|X - μ| < kσ) ≥ 1 - 1/k²$
- $P(|X - μ| ≥ ε) ≤ σ²/ε² \quad for\quad ε > 0$

**Proof**: Apply Markov's inequality to $Y = (X - μ)²$ with $a = k²σ²$

**Key Insights**:

- At least 75% of data within 2 standard deviations
- At least 89% of data within 3 standard deviations
- Works for ANY distribution with finite variance

### One-Sided Chebyshev (Cantelli's Inequality)

**Statement**: For random variable X with mean μ and variance σ²:
$P(X - μ ≥ kσ) ≤ 1/(1 + k²) \quad for \quad k > 0$

**Advantage**: Tighter bound for one-sided deviations

### Chernoff Bounds

**Statement**: For random variable X with MGF $M_X(t)$:
$P(X ≥ a) ≤ e^{(-ta)} {M_X(t)}$ 

**Method**: Choose t to minimize the bound
$P(X ≥ a) ≤ inf_{(t>0)} e^{(-ta)} {M_X(t)}$

**Applications**: Exponentially decreasing bounds for sums of independent random variables

---

## 2. Types of Convergence

### What is Convergence?

Convergence describes how a sequence of random variables X₁, X₂, X₃, ... behaves as n approaches infinity. We want to know if and how these random variables approach some target value or distribution.

---

### 1. Convergence in Probability

**Definition**: Xₙ converges in probability to X if:
$P(|Xₙ - X| > ε) → 0$ as n → ∞, for any $ε > 0$

**What it means**: The probability that Xₙ is far from X becomes arbitrarily small.

**Example**: Let Xₙ = (number of heads in n flips)/n. Then Xₙ converges in probability to 0.5 by the Law of Large Numbers.

---

### 2. Almost Sure Convergence

**Definition**: Xₙ converges almost surely to X if:
P(Xₙ → X as n → ∞) = 1

**What it means**: In virtually every realization of the sequence, Xₙ actually approaches X.

**Key difference**: This is stronger than convergence in probability. Here the sequence itself converges, not just the probabilities.

**Example**: The sample mean of coin flips converges almost surely to 0.5.

---

### 3. Convergence in Distribution

**Definition**: Xₙ converges in distribution to X if the CDF of Xₙ approaches the CDF of X at all continuity points.

**What it means**: The probability distributions become similar, even if individual values don't get close.

**Key point**: The random variables themselves don't need to approach each other, only their distributions.

**Example**: Central Limit Theorem - standardized sums converge in distribution to normal, regardless of the original distribution.

---

### 4. Convergence in Mean (L¹)

**Definition**: $E[|Xₙ - X|] → 0$  as  $n → ∞$

**What it means**: The expected absolute difference between Xₙ and X approaches zero.

**Focus**: Average behavior of the differences.

---

### 5. Convergence in Mean Square (L²)

**Definition**: $E[(Xₙ - X)²] → 0 \quad as \quad n → ∞$

**What it means**: The expected squared difference approaches zero.

**Stronger than L¹**: This penalizes large deviations more heavily and implies convergence of both means and variances.

![](https://www.youtube.com/watch?v=Ajar_6MAOLw&t=402s&pp=ygU3cHJvYmFiaWxpdHkgaW5lcXVhbGl0aWVzIGFuZCBjb252ZXJnZW5jZSBhbmQgZGl2ZXJnZW5jZQ%3D%3D)

---

## 3. Laws of Large Numbers

### Weak Law of Large Numbers (WLLN)

**Statement**: Let X₁, X₂, ... be independent random variables with E[Xᵢ] = μ and Var(Xᵢ) = σ² < ∞.
Then $X̄ₙ = (X₁ + ... + Xₙ)/n → μ$

**Proof using Chebyshev**:

- $E[X̄ₙ] = μ$
- $Var(X̄ₙ) = σ²/n$
- $P(|X̄ₙ - μ| ≥ ε) ≤ σ²/(nε²) → 0$  as  $n → ∞$

### Strong Law of Large Numbers (SLLN)

**Statement**: Under same conditions as WLLN:
$X̄ₙ → μ$

**Kolmogorov's SLLN**: $If E[Xᵢ] = μ$ and $Σᵢ Var(Xᵢ)/i² < ∞$, then $X̄ₙ → μ$

**Interpretation**:

- Sample averages converge to population mean
- Foundation of statistical inference
- Justifies Monte Carlo methods

### Applications of LLN

1. **Casino profits**: Long-run house edge realization
2. **Quality control**: Sample proportion → true defect rate
3. **Insurance**: Claim frequency → expected frequency
4. **Polling**: Sample proportion → population proportion

---

# Central Limit Theorem (CLT)

## What is the Central Limit Theorem?

The CLT states that when you average many independent random variables, the distribution of that average approaches a normal distribution, regardless of the original distribution shape.

**Key insight**: The "magic" of CLT is that it works for ANY original distribution - uniform, exponential, discrete, continuous, even weird distributions.

---

![](https://www.youtube.com/watch?v=YAlJCEDH2uY)

## Standard Form of CLT

**Setup**: Let $X₁, X₂, ..., Xₙ$ be independent, identically distributed random variables with:

- Mean: $E[Xᵢ] = μ$
- Variance: $Var[Xᵢ] = σ² < ∞$

**Sample mean**: $X̄ₙ = (X₁ + X₂ + ... + Xₙ)/n$

**Standardized form**: $Zₙ = √n(X̄ₙ - μ)/σ$

**CLT Statement**: As n → ∞, Zₙ converges in distribution to N(0,1)

**Practical form**: For large n, $X̄ₙ ≈ N(μ, σ²/n)$

---

## Key Components Explained

### Why the √n factor?

- $Var[X̄ₙ] = σ²/n$
- Standard deviation of $X̄ₙ$ is $σ/√n$
- To standardize, we multiply by √n to get unit variance

### Why σ²/n for the variance?

- $Var[X₁ + ... + Xₙ] = nσ²$ (for independent variables)
- $Var[(X₁ + ... + Xₙ)/n] = nσ²/n² = σ²/n$

### What "large n" means

- Depends on original distribution
- Symmetric distributions: n ≥ 30 often sufficient
- Skewed distributions: may need n ≥ 100+
- Already normal: any n works

---

## 6. Few Examples

### Example 1: Chebyshev Application

A machine produces items with mean weight 100g and standard deviation 5g. What can we say about the probability that a randomly chosen item weighs between 85g and 115g?

**Solution:**
$μ = 100, σ = 5$, interval is $μ ± 3σ (k = 3)$

Using Chebyshev: $P(|X - 100| < 15) ≥ 1 - 1/3² = 1 - 1/9 = 8/9 ≈ 89%$

**If normally distributed**: $P(|X - 100| < 15) ≈ 99.7%$

**Key insight**: Chebyshev gives conservative bound for any distribution

### Example 2: Law of Large Numbers Verification

Simulate coin flips to verify WLLN. $Let X₁, X₂$, ... be Bernoulli(0.5).

**Theoretical**: $E[Xᵢ] = 0.5, so X̄ₙ →ᵖ 0.5$

**Simulation approach**:

- Generate n coin flips
- Calculate running average X̄ₖ for k = 1, 2, ..., n
- Plot X̄ₖ vs k to show convergence to 0.5

**Chebyshev bound**: $P(|X̄ₙ - 0.5| ≥ ε) ≤ 0.25/(nε²)$

This simulation can be done by simple code

### Theory and problems:

- **ProbabilityCourse.com - Markov and Chebyshev Inequalities** [Markov and Chebyshev Inequalities](https://www.probabilitycourse.com/chapter6/6_2_2_markov_chebyshev_inequalities.php)
- **Stanford University Theory Notes**  [Probability - The Markov and Chebyshev Inequalities](https://theory.stanford.edu/~blynn/pr/markov.html)
- **CMU Statistics 36-705 Lecture Notes**
- **ProbabilityCourse.com CLT Chapter** - [Central Limit Theorem](https://www.probabilitycourse.com/chapter7/7_1_2_central_limit_theorem.php)
- **MIT 18.05 Class Notes**

# Day 4 :  Stochastic Processes and Calculus

---

## 1. Stochastic Processes: Definition and Classification

### Definition

A **stochastic process** {X(t), t ∈ T} is a collection of random variables indexed by a parameter t, where:

- **X(t)**: Random variable at time/index t
- **T**: Index set (parameter space)
- **S**: State space (range of X(t))

### Classification by Index Set

**Discrete-time processes**: T is countable (e.g., T = {0, 1, 2, ...})

- Notation: ${Xₙ, n = 0, 1, 2, ...}$ or ${X₀, X₁, X₂, ...}$

**Continuous-time processes**: T is uncountable (e.g., T = [0, ∞))

- Notation: ${X(t), t ≥ 0}$

### Classification by State Space

**Discrete state space**: S is countable (e.g., S = {0, 1, 2, ...})
**Continuous state space**: S is uncountable (e.g., S = ℝ)

### Examples

1. **Stock price over time**: Continuous-time, continuous state
2. **Number of customers in queue**: Discrete-time, discrete state
3. **Brownian motion**: Continuous-time, continuous state
4. **Random walk**: Discrete-time, discrete state

---

# Markov Chains

### Mathematical Definition

A discrete-time stochastic process {Xₙ, n ≥ 0} is a Markov chain if:
$P(Xₙ₊₁ = j | X₀ = i₀, X₁ = i₁, ..., Xₙ = i) = P(Xₙ₊₁ = j | Xₙ = i)$

**Key Insight:** The future depends only on the present state, not the past history.

### Transition Probability Matrix P

**Definition:** $P_{ij} = P(Xₙ₊₁ = j | Xₙ = i)$

**Properties:**

- $P_{ij} ≥ 0$ for all i, j
- $Σⱼ P_{ij} = 1$ for all i (each row sums to 1)
- P is called a stochastic matrix

### Simple Example: Weather Model

States: {Sunny, Rainy}

- If sunny today: 70% chance sunny tomorrow, 30% chance rainy
- If rainy today: 40% chance sunny tomorrow, 60% chance rainy

**Transition Matrix:**

$$
P = \begin{bmatrix}
P(S \to S) & P(S \to R) \\
P(R \to S) & P(R \to R)
\end{bmatrix}
= \begin{bmatrix}
0.7 & 0.3 \\
0.4 & 0.6
\end{bmatrix}
$$

**Reading the Matrix:**

- P₁₁ = 0.7: P(tomorrow sunny | today sunny)
- P₁₂ = 0.3: P(tomorrow rainy | today sunny)
- P₂₁ = 0.4: P(tomorrow sunny | today rainy)
- P₂₂ = 0.6: P(tomorrow rainy | today rainy)

![](https://youtu.be/IkbkEtOOC1Y)

---

### Chapman-Kolmogorov Equations

**Fundamental Equation:**
$P_{ij}^{(n)} = \sum_k P_{ik}^{(m)} \times P_{kj}^{(n-m)} \quad \text{for } 0 < m < n$

**Matrix Form:**

$P^{(n)} = P^n \quad (\text{n-th power of matrix } P)$

### Computing $P^n$

**Method 1: Direct Multiplication**
$P² = P × P, P³ = P² × P,$ etc.

**Method 2: Eigenvalue Decomposition**
If $P = QΛQ⁻¹$, then $P^n = QΛ^nQ⁻¹$

**Finding Eigenvalues:**
$det(P - λI) = 0$

For weather example:

$$
det([0.7-λ  0.3  ]) = (0.7-λ)(0.6-λ) - 0.12 = λ² - 1.3λ + 0.3
   ([0.4    0.6-λ])

$$

Eigenvalues: λ₁ = 1, λ₂ = 0.3

---

### Communication Between States

**Definition:** State i communicates with state j (i ↔ j) if:

- $P_{ij}^{(n)}$ for some n ≥ 0, AND
- $P_{ji}^{(m)}$ for some m ≥ 0

### Recurrence vs Transience

**First Return Probability:**
$f_{ii}$ = P(ever return to state i | start in state i)

**Classification:**

- **Recurrent:** $f_{ii} = 1$ (will definitely return)
- **Transient:** $f_{ii} < 1$ (may never return)

**Mathematical Test:**
State i is recurrent ⟺ $Σₙ₌₁^∞ P_{ii}^{(n)} = ∞$

### Periodicity

**Period of state i:**
$d(i) = gcd{(n ≥ 1: P_{ii}^{(n)} > 0)}$

- **Aperiodic:** d(i) = 1
- **Periodic:** d(i) > 1

### Example: Random Walk

States: {..., -2, -1, 0, 1, 2, ...}
$P(Xₙ₊₁ = i+1 | Xₙ = i) = p$
$P(Xₙ₊₁ = i-1 | Xₙ = i) = q = 1-p$

**Properties:**

- All states communicate
- Period = 2 (can only return to starting state in even number of steps)
- Recurrent if p = 1/2, transient if p ≠ 1/2

---

### Definition

A probability distribution $π = (π₁, π₂, ...)$ is stationary if:
π = πP

This says that when you multiply the stationary distribution π by the transition matrix P, you get back the same distribution π.

**Component Form:**
$πⱼ = Σᵢ πᵢPᵢⱼ$ for all j

**Plus Normalization:**
$Σⱼ πⱼ = 1$

### Finding Stationary Distribution

**Method:** Solve the system $πP = π$ with $Σⱼ πⱼ = 1$

**Alternative Form:** Solve $(P^T - I)π = 0$

### Weather Example Solution

$$
π₁(0.7) + π₂(0.4) = π₁ \\
π₁(0.3) + π₂(0.6) = π₂\\
π₁ + π₂ = 1

$$

From first equation: $π₂(0.4) = π₁(0.3)$
So $π₂ = (3/4)π₁$

Substituting: $π₁ + (3/4)π₁ = 1$
Therefore: $π₁ = 4/7, π₂ = 3/7$

**Stationary Distribution:** $π = (4/7, 3/7)$

These numbers tell us **what happens in the long run**:

1. **No matter what the weather is today**, if we wait long enough:
    - 57.1% of all days will be sunny
    - 42.9% of all days will be rainy
2. **On any random day far in the future**:
    - Probability of sunny = 57.1%
    - Probability of rainy = 42.9%
3. **If you observe for many years**:
    - Roughly 4 out of every 7 days will be sunny
    - Roughly 3 out of every 7 days will be rainy

### Theory References:

- **Sheldon Ross - "Introduction to Probability Models" (Chapter 4)** - Widely regarded as having "a readable chapter on Markov chains and many nice examples" [Markov Chains](http://www.statslab.cam.ac.uk/~rrw1/markov/M.pdf) and making difficult concepts accessible
- **Mathematics LibreTexts** - Comprehensive introduction covering stochastic processes and Markov chains
- YouTube:

### Practice Problems:

- MIT OCW 18.445 Practice Problemset
- Grimmett, G. & Stirzaker, D. "Probability and Random Processes" Back exercises

# **Brownian Motion and Martingales**

## **1. Brownian Motion (Wiener Process)**

### **Definition**

Brownian motion $(B_t)_{t \geq 0}$ is a continuous-time stochastic process with $B_0 = 0$, characterized by having independent and normally distributed increments. Specifically, for any $s < t$, the increment $B_t - B_s$ is normally distributed with mean zero and variance $t - s$. Its paths are continuous but nowhere differentiable, reflecting highly irregular motion. Brownian motion models random fluctuations and serves as a building block in stochastic calculus, physics, and financial mathematics.

A stochastic process `${Wₜ : t ≥ 0}$` satisfying:

1. **W₀ = 0** (almost surely)
2. **Independent increments**: `$Wₜ - Wₛ ⟂ Wᵥ - Wᵤ$` for `$t > s ≥ v > u$`
3. **Gaussian increments**: `$Wₜ - Wₛ = N(0, t-s)$`
4. **Continuous paths**: `$t ↦ Wₜ$` is continuous a.s.

### **Key Properties**

$$
E[Wₜ] = 0, \\ Var(Wₜ) = t, \\ Cov(Wₜ, Wₛ) = min(t,s)

$$

---

## **2. Path Properties**

| Property | Mathematical Expression | Interpretation |
| --- | --- | --- |
| Continuity | `lim_{h→0} W_{t+h} = Wₜ` | No jumps |
| Non-differentiability | `dWₜ/dt` DNE everywhere | Fractal-like paths |
| Quadratic Variation | `∑(W_{t_i} - W_{t_{i-1}})^2 → t` | Fundamental for Itô calculus |

### **Markov Property**

$$
P(Wₜ ∈ A | ℱₛ) = P(Wₜ ∈ A | Wₛ) \quad  \forall \quad t > s

$$

where `ℱₛ = σ(Wᵤ : u ≤ s)`

![](https://youtu.be/VNTfgqJQlnk)

![](https://youtu.be/fIM_AQbBOm4)

---

## **3. Martingales**

### **Definition**

A process `${Xₜ}$` is a martingale if:

1. **Integrability**: `$E[|Xₜ|] < ∞ \quad ∀ \quad t$`
2. **Adapted**: `$Xₜ ∈ ℱₜ$`
3. **Martingale property**:

$$
E[Xₜ | ℱₛ] = Xₛ \quad \forall t > s

$$

### **Examples**

1. **Standard Brownian Motion**: `$Wₜ$`
2. **Brownian Motion with Drift**: `$Xₜ = Wₜ + μt$` (only if `$μ=0$`)
3. **Exponential Martingale**: `$exp(σWₜ - σ²t/2)$`

---

## **4. Stopping Times (Optional)**

### **Definition**

A random time `τ` is a stopping time if:

$$
\{\tau ≤ t\} ∈ ℱₜ \quad \forall t ≥ 0

$$

### **Optional Stopping Theorem**

If `{Xₜ}` is a martingale and `τ` is a stopping time with `E[τ] < ∞`, then:

$$
E[X_τ] = E[X₀]

$$

---

## **5. Exercises**

### **Brownian Motion**

1. Simulate 3 paths of `$Wₜ$` on `$t ∈ [0,1]$` (use Δt=0.01)
    - Plot and compare their quadratic variations
2. Show that `$Wₜ² - t$` is a martingale:
    - Verify `$E[Wₜ² - t | ℱₛ] = Wₜ² - s$`

### **Martingales**

1. For `$Xₙ = ∑ᵢ₌₁ⁿ ξᵢ$` (i.i.d. `$ξᵢ$` with `$E[ξᵢ]=0$`):
    - Prove `${Xₙ}$` is a martingale
    - Find `$E[Xₙ²]$` (variance)

---

## **Summary**

- **Brownian motion**: The canonical continuous stochastic process
- **Martingales**: Fair games with conditional expectations
- **Stopping times**: Rule-constrained random times
- **Applications**: Finance (Black-Scholes), physics, bioinformatics

### Resources:

- Steven Shreve Stochastic Calculus part 1

---

# **Day 5: Stochastic Calculus continued**

## **1. Itô's Lemma**

### **The Fundamental Theorem of Stochastic Calculus**

For an Itô process:

$$
dX_t = \mu_t dt + \sigma_t dW_t

$$

and any twice-differentiable function `f(t, X_t)`, we have:

$$
df(t, X_t) = \left(\frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial x} + \frac{1}{2}\sigma_t^2 \frac{\partial^2 f}{\partial x^2}\right)dt + \sigma_t \frac{\partial f}{\partial x}dW_t

$$

### **Key Intuition**

| Term | Interpretation | Ordinary Calculus? |
| --- | --- | --- |
| `∂f/∂t dt` | Time drift | Yes |
| `∂f/∂x dX_t` | First-order change | Yes |
| `½ ∂²f/∂x² (dX_t)²` | Volatility correction (Itô term) | No |

![](https://www.youtube.com/watch?v=Z5yRMMVUC5w&t=2s&pp=ygUSaXRvcyBsZW1tYSBtaXQgb2N3)

---

## **2. Stochastic Differential Equations (SDEs)**

### **General Form**

$$
dX_t = \mu(X_t,t)dt + \sigma(X_t,t)dW_t

$$

### **Existence & Uniqueness**

Solutions exist if:

1. **Lipschitz condition**: `|μ(x,t)-μ(y,t)| + |σ(x,t)-σ(y,t)| ≤ K|x-y|`
2. **Linear growth**: `|μ(x,t)| + |σ(x,t)| ≤ K(1+|x|)`

---

## **3. Important SDE Examples**

### **Geometric Brownian Motion**

A GBM is a continuous-time stochastic process that is widely used in finance to model stock prices and other financial assets. It's a particular type of stochastic process where the logarithmic changes in the asset price are normally distributed and independent of each other.

In a GBM, the asset price follows an exponential growth rate plus some random noise. This exponential growth represents the average return of the financial asset, while the random noise represents the volatility or risk of the asset. The GBM model is a key component of the Black-Scholes-Merton formula for option pricing.

It's important to note that while GBM is a popular model in finance due to its mathematical tractability, it makes some simplifying assumptions that may not hold in real-world financial markets, such as constant returns and volatility, and log-normal price distribution.

$$
dS_t = \mu S_t dt + \sigma S_t dW_t

$$

- **Solution**:

$$
S_t = S_0 \exp\left((\mu-\frac{1}{2}\sigma^2)t + \sigma W_t\right)

$$

- Used in Black-Scholes model

### **Ornstein-Uhlenbeck Process**

$$
dX_t = \theta(\mu - X_t)dt + \sigma dW_t

$$

- **Solution**:

$$
X_t = X_0 e^{-\theta t} + \mu(1-e^{-\theta t}) + \sigma \int_0^t e^{-\theta(t-s)}dW_s

$$

- Models mean-reverting systems (e.g., interest rates)

---

## **4. Exercises**

### **Itô's Lemma Practice**

1. For `Y_t = W_t^3`, compute `dY_t` using Itô's Lemma
2. Given:

$$
dX_t = 2X_t dt + 3X_t dW_t

$$

Find the SDE for:

- `$Z_t = ln(X_t)$`
- `$U_t = X_t^{-1}$`

### **SDE Solutions**

1. Solve the SDE:

$$
dY_t = \frac{1}{Y_t}dt + \alpha Y_t dW_t

$$

(Hint: Try `$Z_t = Y_t^2$`)

1. For the Ornstein-Uhlenbeck process:
    - Verify the solution satisfies the SDE
    - Compute  $E[X_t]$ and `$Var(X_t)$`

---

## **Summary**

- **Itô's Lemma**: Stochastic chain rule with volatility correction
- **SDEs**: Model systems with random shocks
- **Analytical Solutions**: Possible for linear/transformable cases
- **Applications**: Finance (options), physics, biology

---

# **Financial Applications of Stochastic Calculus**

## **1. Black-Scholes Model**

The **Black-Scholes Model** is a mathematical model for pricing European call and put options. This model was developed by economists Fisher Black and Myron Scholes, with contributions from Robert Merton. The model assumes that financial markets are efficient, and it also assumes that the return on the security follows a geometric Brownian motion with constant volatility.

The Black-Scholes model's key concept is the Black-Scholes equation, a differential equation that describes how, under a certain set of assumptions, the value of an option changes with respect to changes in the underlying asset's price and time. This equation's solution, known as the Black-Scholes formula, gives the price of a European option on a non-dividend paying stock.

In finance, the Black-Scholes model is extensively used to price European options and assess their sensitivity to market factors, often referred to as the Greeks. These include Delta, which measures the rate of change of the option price with respect to changes in the underlying asset's price, and Vega, which measures the sensitivity of the option price to changes in the underlying asset's volatility.

### **Derivation of the PDE**

For stock price `S_t` following GBM:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t

$$

The option price `V(S,t)` satisfies:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0

$$

**Key Steps:**

1. Construct risk-free portfolio: `$Π = V - ΔS$`
2. Apply Itô's Lemma to `$dΠ$`
3. Eliminate randomness (hedging)
4. Set return equal to risk-free rate `$r$`

![](https://youtu.be/TnS8kI_KuJc)

---

## **2. Option Pricing Basics**

### **European Call Option**

$$
C(S_t,t) = S_tN(d_1) - Ke^{-r(T-t)}N(d_2)

$$

where:

$$
d_1 = \frac{\ln(S_t/K) + (r+\sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}

$$

$$
d_2 = d_1 - \sigma\sqrt{T-t}

$$

| Greek | Formula | Interpretation |
| --- | --- | --- |
| Delta (Δ) | `$N(d_1)$` | Price sensitivity to underlying |
| Gamma (Γ) | `$N'(d_1)/(S_tσ√(T-t))$` | Convexity effect |
| Theta (Θ) | `$-S_tN'(d_1)σ/(2√(T-t)) - rKe^{-r(T-t)}N(d_2)$` | Time decay |

---

## **3. Risk-Neutral Valuation**

### **Fundamental Theorem**

$$
V_0 = e^{-rT}\mathbb{E}^Q[V_T]

$$

where:

- `Q` is the risk-neutral measure
- Drift becomes `r` under `Q`:

$$
dS_t = rS_t dt + σS_t dW_t^Q

$$

### **Monte Carlo Pricing**

```python
import numpy as np
def european_call(S0, K, T, r, sigma, N_sims):
    ST = S0 * np.exp((r-0.5*sigma**2)*T + sigma*np.sqrt(T)*np.random.normal(size=N_sims))
    return np.exp(-r*T) * np.mean(np.maximum(ST-K, 0))

```

---

## **4. Exercises**

### **Black-Scholes**

1. Derive the put option price `P(S,t)` using put-call parity
2. Verify that the call price formula satisfies the Black-Scholes PDE

### **Numerical Methods**

1. Price a European call with:
    - `S0=100`, `K=110`, `T=1`, `r=0.05`, `σ=0.2`
    - Compare analytical vs. Monte Carlo (10,000 paths)
2. Simulate 100 GBM paths with:
    - `μ=0.1`, `σ=0.3`, `T=1`, `S0=50`
    - Plot the 5th and 95th percentiles

---

## **Summary**

- **Black-Scholes**: Connects PDEs with option pricing
- **Risk-Neutral Pricing**: Expected payoffs under `Q` measure
- **Numerical Methods**: Monte Carlo for complex derivatives

---

### Resources:

- Steven Shreve Stochastic Calculus Parts 1 and 2

## Week 1 Assignment: [https://forms.gle/upK7VcBypjTG9ix36](https://forms.gle/upK7VcBypjTG9ix36)
