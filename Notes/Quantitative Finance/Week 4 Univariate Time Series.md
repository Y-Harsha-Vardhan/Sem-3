# Week 4

# Univariate Time Series: Extended

Before proceeding it’s important to be familiar with OLS regression, in case you aren’t check this:

[https://www.sfu.ca/~dsignori/buec333/lecture%208.pdf](https://www.sfu.ca/~dsignori/buec333/lecture%208.pdf)

### Wold Representation Theorem

Any zero-mean covariance stationary time series ${X_t}$ can be decomposed as $X_t = V_t + S_t$, where

- $V_t$ is a linearly deterministic process
- $S_t = \Sigma_{i=0}^{\infty}\Psi_i\eta_{t-i}$ is an infinite moving average process of error terms, where
    - $\Psi_0 = 1$,  $\Sigma_{i=0}^{\infty}\Psi_i^2 < \infty$
    - $\{\eta_t\}$ is linearly unpredictable white noise and $\{\eta_t\}$ is uncorrelated with $\{V_t\}$  (In case you forgot correlation [check](https://youtu.be/xZ_z8KWkhXE?si=wQxwPPwReDv9_evN)).
        
        So $E(\eta_t) = 0, \quad E(\eta_t^2) = \sigma^2, \quad E(\eta_t\eta_s) = 0, \quad \forall t,s\ne t \\ E(\eta_tV_s) = 0 \quad\forall t,s$
        

**Using Lag Operator $L()$**

The lag operator L() shifts a time series back by one time increment. Recursively, $L^n(X_t) = L(L^{n-1}(X_t)) = X_{t-n}$

Expressing Wold Representation using lag operator, $X_t = \psi(L)\eta_t + V_t$ 

### Some Definitions

- **Impulse Response Function:** The Impulse Response function of the covariance stationary process $\{X_t\}$ is $IR(j) = \frac{\delta X_t}{\delta \eta_{t-j}} = \psi_j$. The **long-run cumulative response** of $\{X_t\}$ is $\Sigma_{i=0}^{\infty}IR(j) = \Sigma_{i=0}^{\infty}\Psi_i = \Psi(L)$ with L=1.
- **Invertible time series:** When $\Psi^{-1}(L)$ exists, the time series $\{X_t\}$ is Invertible and has an auto-regressive representation $X_t = (\Sigma_{i=0}^{\infty}\Psi_i^*X_{t-i}) + \eta_t$

## ARMA$(p,q)$ Models

The time series ${X_t}$ follows the ARMA(p, q) Model with auto-regressive order p and moving-average order q if

$$
X_t = \mu + \phi_1(X_{t-1} - \mu) + \phi_2(X_{t-2} - \mu) + \dots \phi_p(X_{t-p} - \mu) + \eta_t + \theta_1\eta_{t-1} + \theta_2\eta_{t-2} + \dots \theta_q\eta_{t-q}
$$

where $\{\eta_t\}$ is $WN(0, \sigma^2)$ with

$E(\eta_t) = 0, \forall t \quad; \quad E(\eta_t^2) = \sigma^2 < \infty, \forall t, \text{ and } E(\eta_t\eta_s) = 0, \forall t \ne s$  

### Yule-Walker Equations & Toeplitz Matrix

For an AR(p) model:

$$
(X_t - \mu) = \phi_1(X_{t-1} - \mu) + \phi_2(X_{t-2} - \mu) + \dots \phi_p(X_{t-p} - \mu) +\eta_t 
$$

we can write the Yule-Walker Equations $(j=0, 1, \dots)$

$$
E[(X_t - \mu)(X_{t-j} - \mu)] = \phi_1E[(X_{t-1} - \mu)(X_{t-j} - \mu)] + \phi_2E[(X_{t-2} - \mu)(X_{t-j} - \mu)] + \dots \phi_pE[(X_{t-p} - \mu)(X_{t-j} - \mu)] +E[\eta_t(X_{t-j} - \mu)] \\ \gamma(j) = \phi_1\gamma(j-1) + \phi_2\gamma(j-2) + \dots \phi_p\gamma(j-p) + \delta_{0,j}\sigma^2
$$

Equations $j = 1, 2, . . . p$ yield a system of p linear equations in $\phi_j$:

$$
\begin{pmatrix} \gamma(1) \\ \gamma(2) \\ . \\ . \\ . \\ \gamma(p)\end{pmatrix} = \begin{bmatrix} \gamma(0) \quad \gamma(-1) \quad \gamma(-2) \quad \dots \quad \gamma(-p+1) \\ \gamma(1) \quad\gamma(0) \quad \gamma(-1) \quad  \dots \quad \gamma(-p+2) \\ . \quad . \quad . \quad \dots \quad . \\ . \quad . \quad . \quad \dots \quad . \\ . \quad . \quad . \quad \dots \quad. \\ \gamma(p-1) \quad \gamma(p-2) \quad \gamma(p-3) \quad \dots \quad \gamma(0) \end{bmatrix} \begin{pmatrix} \phi(1) \\ \phi(2) \\ . \\ . \\ . \\ \phi(p)\end{pmatrix}
$$

Notice that the $p \times p$ matrix is a Toeplitz matrix. This allows us to use its to compute $\mathbf\phi_p$ faster as it’s inverse has lesser complexity using the **Levinson-Durbin recursion.** 

Check this video out:

[https://youtu.be/1230arWETzY?si=SSkcH_14XJVt48x6](https://youtu.be/1230arWETzY?si=SSkcH_14XJVt48x6)

## ARIMA(p, d, q) Models

Many economic time series exhibit non-stationary behavior
consistent with random walks. Box and Jenkins advocate the removal of non-stationary trending behaviour using differencing operators ($\Delta^k = (1-L)^k$)

## ACF & PACF

[https://youtu.be/ZE_WGBe0_VU?si=Eeb9u9UhLo6Vgdha](https://youtu.be/ZE_WGBe0_VU?si=Eeb9u9UhLo6Vgdha)

[https://youtu.be/DeORzP0go5I?si=aSlBuHmo1yCVGFFN](https://youtu.be/DeORzP0go5I?si=aSlBuHmo1yCVGFFN)

*But, how to estimate the values for parameters?*

## Estimation of ARMA Models

An $ARMA(p,q)$ model 

$$
x_t - \phi_1x_{t-1} - \dots - \phi_px_{t-p} = u_t + \theta_1 u_{t-1} + \dots + \theta_q u_{t-q} \quad \quad u_t \sim WN(0, \sigma^2)
$$

is characterised by p+q+1 parameters

- $\phi = (\phi_1, \phi_2, \dots, \phi_p)’$
- $\theta = (\theta_1, \theta_2, \dots, \theta_q)’$
- $\sigma^2$

that need to be estimated. Various techniques that exist are:

- Two-Step Regression Estimation
- Yule-Walker Estimation (Already Discussed)
- Maximum Likelihood Estimation

[https://www.lem.sssup.it/phd/documents/Lesson12.pdf](https://www.lem.sssup.it/phd/documents/Lesson12.pdf)

## Testing for Stationarity

**Dickey-Fuller Test:** Suppose $\{X_t\}$ follows the AR(1) model so

$X_t = \phi X_{t-1} + \eta_t$ with $\{\eta_t\}$ a $WN(0, \sigma^2)$

Consider testing the following hypotheses:

$H_0$: $\phi=1$ (unit root, non-stationarity) which is exactly a random walk. 

$H_1$: $|\phi|$<1  (stationarity)

Fit the AR(1) model by least squares and define the test statistic 

$t_{\phi=1} = \frac{\hat\phi-1}{se(\hat\phi)}$ 

where $\hat\phi$ is the least-squares estimate of $\phi$ and $se(\hat\phi)$ is the least-squares estimate of the standard error of $\hat\phi$. 

- If $|\phi|<1$ then $\sqrt{T}(\hat\phi - \phi) \xrightarrow[]{d} N(0, (1-\phi^2))$ : If the series is truly stationary, then the estimated coefficient $\hat\phi$ behaves well. As T gets larger, $\sqrt{T}(\hat\phi - \phi)$ will follow a standard normal distribution
- If $\phi = 1$ then $\hat\phi$  is super-consistent with rate $1/T$, $\sqrt{T}t_{\phi = 1}$ has DF distribution : If the series has a unit root, the estimate $\hat\phi$ converges to true value

# Multivariate Time Series

## Stationarity

Let $\{X_t\} = \{..., X_{t-1}, X_t, X_{t+1}, ...\}$ be an m-dimensional stochastic process consisting of random m-vectors $\mathbf{X_t} = (X_{1,t}, X_{2,t}, ..., X_{m, t})'$ (a random vector on $R^m$). 

$\{\mathbf{X_t}\}$ consists of m component time-series $\{X_{1,t}\}, \{X_{2,t}\}, ... \{X_{m,t}\}$. $\{\mathbf{X_t}\}$ is covariance stationary if every component time series is covariance stationary.

- $\mathbf{\mu} = E[\mathbf{X_t}]$ ( $m \times 1$ matrix)

$\Phi_1, \Phi_2, \dots \Phi_p$ are $( m \times m )$ matrices of coefficients  $\{\eta_t\}$  is multivariate white noise $MVN(0_m, \Sigma)$ 

- $\Gamma_0 = Var(\mathbf{X_t}) = E[(X_t - \mu ) (X_t - \mu )']$
- $\mathbf{R_0} = corr(\mathbf{X_t})=\mathbf{D}^{-1/2} \Gamma_0 \mathbf{D}^{1/2}$  where $\mathbf{D} = diag(\Gamma_0)$
- Cross-Covariance and cross-correlation matrices with lag k
    - $\Gamma_k = Cov(\mathbf{X_t}, X_{t-k}) = E[(X_t - \mu)(X_{t-k} - \mu)']$
    - $\mathbf{R_k} = corr(\mathbf{X_t}) = \mathbf{D}^{-1/2} \Gamma_k \mathbf{D}^{1/2}$

**Note that :** 

- $\mathbf{
\Gamma_0, R_0 }$ are $m \times m$ symmetric matrices
- $\mathbf{
\Gamma_k, R_k }$ are $m \times m$ matrices but not symmetric. In fact, $\Gamma_k = \Gamma_{-k}^T$

## Wold Representation Theorem

For a multivariate time series, which is covariant stationary, $\{X_t\}$ can be decomposed as

$X_t = \mathbf{V_t} + \mathbf{\eta_t} + \mathbf{\psi_t}\mathbf{\eta_{t-1}} + ... = \mathbf{V_t} + \Sigma_{k=0}^{\infty}\mathbf{\psi_k}\mathbf{\eta_{t-k}}$

Here, $\{\mathbf{V_t}\}$ is an m-dimensional linearly deterministic process and $\{\mathbf{\eta_t}\}$ is multivariate white noise. $\{\mathbf{\psi_k}\}$ is an $m \times m$ matrix such that $\mathbf{\psi_0} = \mathbf{I_m}, \Sigma_{k=0}^{\infty}\{\mathbf{\psi_k}\}\{\mathbf{\psi_k}\}^T$ converges

## VAR Processes

The m-dimensional multivariate time series $\{Xt\}$ follows the
VAR(p) model with auto-regressive order p if

$$
⁍
$$

where 

$C = (c_1, c_2, \dots c_m)'$

A VAR(p) process is equivalent to a VAR(1) process. Define:

$Z_{t} = (X_t', X_{t-1}', \dots X_{t-p+1}')'$

$Z_{t-1}=(X_{t-1}’,X_{t-2}’,\dots X_{t-p}’)'$

The (mpx1) multivariate time series process $\{Z_T\}$ satistifes

$Z_t = D + A Z_{t-1} + F$   where D and F are ($mp \times 1$) and A is ($mp \times mp$):

$$
D = \begin{bmatrix} C \\0_m\\0_m\\.\\.\\.\\0_m\\0_m\end{bmatrix}, A = \begin{bmatrix}\phi_1 &\phi_2 & \phi_3 & \dots & \dots & \phi_p \\ I_m & 0 & 0 &\dots &\dots& 0\\ 0 & I_m & 0 &\dots &\dots & 0\\. &. &. & \dots &\dots & .\\0 & 0 & 0 &\dots &\dots& I_m\\ \end{bmatrix}, F = \begin{bmatrix} \eta_t \\ 0_m \\0_m\\.\\.\\.\\0_m\\0_m\end{bmatrix}
$$

A VAR(p) model is stationary if either:

- All eigen values of the companion matrix A have modulus less than 1
- All roots of $det(I_m - \phi_1z - \phi_2z^2 - \dots - \phi_pz^p) = 0$ as a function of the complex variable z, are outside the complex unit circle $|z| \le 1$.

# Cointegration

## What?

A cointegration test is used to establish if there is a correlation between several time series in the long term. Cointegration tests identify scenarios where two or more non-stationary time series are integrated together in a way that they cannot deviate from equilibrium in the long term. The tests are used to identify the degree of sensitivity of two variables to the same average price over a specified period of time.

## Testing for cointegration

There are three main methods of testing for cointegration. They are used to identify the long-term relationships between two or more sets of variables.

- **Engle-Granger Two-Step Method:**
    - It starts by creating residuals based on the static regression and then testing the residuals for the presence of unit roots using ADF.
    - The limitation is that if there are more than two variables, the method may show more than two cointegrating relationships. Another limitation is that it is a single-equation model.
- **Johansen Test:**
    - Unlike the Engle-Granger method, it allows for more than one cointegrating relationship.
        - **Trace Tests:**
            - It evaluates the number of linear combinations in a time series data, i.e., K, to be equal to the value $K_0$, and the hypothesis for the value K to be greater than $K_0$.
            - When using the trace test to test for cointegration in a sample, we set K0 to zero to test whether the null hypothesis will be rejected.
            - If it is rejected, we can deduce that there exists a cointegration relationship in the sample. Therefore, the null hypothesis should be rejected to confirm the existence of a cointegration relationship in the sample.
        - **Maximum Eigenvalue test:**
            - It is similar to the Johansen’s trace test. The key difference between the two is the null hypothesis.  $H_0: K = K_0 H_0: K = K_0 + 1$
            - In a scenario where $K=K_0$ and the null hypothesis is rejected, it means that there is only one possible outcome of the variable to produce a stationary process.
            - However, in a scenario where $K_0 = m-1$ and the null hypothesis is rejected, it means that there are M possible linear combinations. Such a scenario is impossible unless the variables in the time series are stationary.

[A Guide to Conducting Cointegration Tests](https://www.aptech.com/blog/a-guide-to-conducting-cointegration-tests/)

<aside>
💡

**For further reading:**

- **VECM (Vector Error Correction) :**

[Vector Error Correction (VECM) and Trend Specification](https://spureconomics.com/vector-error-correction-vecm-theory/)

- **Cointegrated VAR Models :**

[An Introduction to the Cointegrated VAR Model](https://youtu.be/2aaGlgi0pM8?si=5z3iATYTr4-tClZf)

- **Kalman Filter**
</aside>

For this section, the following lecture is a great resource (though the math is a little rigorous):

[https://youtu.be/9G1IDAqrWkg?si=o2gtkYFw-U6PAoPU](https://youtu.be/9G1IDAqrWkg?si=o2gtkYFw-U6PAoPU)

# Week 4: Assignment

[Week 4: Time Series Analysis](https://forms.gle/PdfLGHkCcgkgjd6v9)