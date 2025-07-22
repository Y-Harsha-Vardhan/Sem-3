# Week 6

# Swaps

## What?

A swap is a non-contingent derivative contract where cash flow streams are exchanged through OTC between two parties over a series of specified future dates according to certain specified rules.

The parties determine the cash flows with the help of a notional principal amount, where each stream of cash flows is called a ‘leg.’ 

A swap can be of different financial instruments.

- **Interest rate swap**: The parties decide to switch one type of interest rate payment for another type of interest rate payment. A popular type of interest rate swap is a plain vanilla swap
    - **Plain vanilla swap:** Cash flow with a variable interest rate (**floating leg)** is swapped with a fixed interest (**fixed leg)** rate without the underlying principal amount ****left as it is. In some cases, LIBOR serves as the floating leg reference rate. The parties decide beforehand the intervals or times when they will be exchanging the interest rate during the contract life.
        
        ![Screenshot 2025-07-11 112457.png](Screenshot_2025-07-11_112457.png)
        
    - **Basis swap:** This swap comes into play if both legs have a floating rate. In such a case, parties would be able to swap the floating rates by using benchmark rates as the standard.
    - **Amortising swap:** A party can offer a drop in the notional amount equaling the amortisation of a loan.
    - **Step-up swap:** This swap is the exact opposite of the amortising swap. In this, the notional amount rises.
    - **Differential swap:** In this swap, one leg involves the payment of an interest rate in a currency different from the initial principal amount. The other leg, however, involves the payment of an interest rate in the currency of the initial principal.
- **Currency swap:** It involves the exchange of interest and principal payments in one currency for the interest and principal in another currency. Such swaps have more credit exposure in comparison to the interest rate swap. These swaps are practiced basically to hedge the currency exchange rate fluctuations
- **Commodity swap:** It enables the parties to swap floating cash flows depending upon the spot rate of a commodity with the fixed cash flows, which are based on the commodity’s pre-determined price.
- **Credit default swap:** It is like an insurance policy and offers protection against the default of a debt instrument. The buyer will make a premium payment to the seller of the swap. And, if there is a default, the seller will reimburse the buyer an amount equal to the face value of that asset. Also, the buyer transfers the ownership of that asset to the seller.

Swaps are used for hedging risks, such as interest rate risk or currency exchange rate risk, or for speculation.

## The vanilla interest swap rate

Consider a borrower A who swaps a random interest rate (from Bank-V) with a fixed one (from Bank-F). That is, the cash flow of $(0, -v_1, -v_2, \dots , -v_n)$ where $v_i = r_i \times P_n$ ($P_n$ is the notional principal) is swapped with $(0, -s, -s, \dots , -s)$ where $s = r_s \times P_n \times \Delta t_k$ where $r_s$ is the fixed interest rate per annum (called the ***swap rate*) and** $\Delta t_k = t_k - t_{k-1}$.  

$P_n$ is the amount borrowed by the borrower A from the Bank-V.  Hence, the per-period interest rate of the swap is, 

$$
\rho_k = ( r_k - r_s ) \times \Delta t_k \quad , k = 1, 2, \dots, n
$$

That is, at every time $t=t_k$ Bank-F pays $\rho_k P_n$ to the borrower-A. The present value of $\rho_k p_n$ at $t=0$ is given as

$$
PV(0) = \Sigma_{k=1}^{n}PV(0, t_k)  \\ PV(0, t_k) = d(0, t_k) \times \rho_k P_n \\ \text{ where } d(0, t_k) = \exp (- \Sigma_{j=1}^{k} r_j \Delta t_k) \\ \text{ for continuous discounting}
$$

But a swap is a **non-contingent claim,** so it can’t have a price at $t=0$, hence, 

$$
PV(0)=0
$$

Solving for $r_s$, we get

$$
r_s = \frac{ \Sigma_{k=1}^{n} d(0, t_k) \Delta t_k r_k }{ \Sigma_{k=1}^{n}d(0, t_k) \Delta t_k}
$$

### Example

Suppose we enter a five-year interest rate swap on August 4, 2006, with semi-annual payments. We agree to pay a fixed 6% annually (i.e., 3% every six months) on a notional $100 million, while receiving six-month LIBOR from the counterparty.

![Cashflows in an interest rate swap](Screenshot_2025-07-11_121216.png)

Cashflows in an interest rate swap

The first payment exchange occurs on February 4, 2007. We pay $3,000,000 (0.03 × $100 million). The floating payment we receive is based on the LIBOR rate set at the start of the period - August 4, 2006 - making the first floating payment known in advance.

The second exchange on August 4, 2007, again involves a $3 million fixed payment, but the floating amount is based on LIBOR from February 4, 2007. This pattern continues every six months until August 4, 2011.

LIBOR is set six months before it is paid because LIBOR represents the rate on a deposit made today and maturing in six months. This aligns with the swap payment schedule and is crucial for swap pricing.

There is also the **LIBOR in arrears swap** in which the LIBOR rate paid on the swap date is the six-month rate set that day, not the rate set six months before.

## Comparative Advantage

Swaps were originally created to exploit comparative advantage, where two companies can reduce borrowing costs by swapping interest payments based on their differing credit profiles.

### Example

Assume, companies A and B both need to borrow $50M for two years. Their borrowing rates are:

- **For A :**  7% fixed or LIBOR + 0.30%
- **For B:**  8.2% fixed or LIBOR + 1.00%

A prefers floating, B prefers fixed. If they each borrow directly, then they pay the following in total :

six-month LIBOR +30bps+8.2% = six-month LIBOR+8.5%.

However, if A borrowed at fixed and B at floating, they’d only be paying

six-month LIBOR + 100bps +7% = six-month LIBOR+8%

Using a swap where A pays LIBOR to B and receives 6.95% fixed, both save 0.25%.

In practice, an intermediary facilitates the swap and takes a small cut. While swaps started as a way to exploit comparative advantage, they’re now widely used for their flexibility and liquidity.

## Other features of swaps contracts

The above is a description of the vanilla interest rate swap. There are many features that can be added to the contract that make it more complicated, and most importantly, model-dependent.

### Callable and puttable swaps

A callable or puttable swap allows one side or the other to close out the swap at some time before its natural maturity. If you are receiving fixed and the floating rate rises more than you had expected, you would want to close the position. Mathematically, we are in the early exercise world of American-style options

### Extendible swaps

The holder of an extendible swap can extend the maturity of a vanilla swap at the original swap rate.

### Index amortising rate swaps

The principal in the vanilla swap is constant. In some swaps, the principal declines with time according to a prescribed schedule. The index amortizing rate swap is more complicated still  with the amortisation depending on the level of some index, say LIBOR, at the time of the
exchange of payments.

# Options

## Basic Concepts

Recall that options are contingent claims that is the writer has obligation but holder has only right but no obligation to exercise the contract. 

The holder has to pay a **premium** (or price of the option or option price) ****at the time of agreeing to the contract.

This introduces **leverage**, allowing traders to control bigger positions with less capital.

### Why trade options?

1. **Hedging risk:** Like an insurance policy on your stock portfolio
2. **Speculation**: Betting on price movements without owning the asset
3. **Income strategies**: Generating returns in sideways markets using smart positioning

### Types

1. **Call option:** A call option gives the holder of the option the right to **buy** the underlying asset for a strike price by a certain date.
2. **Put option**: A put option gives the holder the right to **sell** the underlying asset for a strike price by a certain date.

### Parameters

Consider:

$S_t = S(t) \rightarrow$ the current market price of the underlying asset

$K \rightarrow$ the strike price of the option

$[0, T] \rightarrow$  is the period of the option with $T$ as the expiration time

1. Contract size, also called the lot, is the number of units of the underlying assets to be exercised in a contract.
2. Intrinsic value, is the real value if exercised today.
3. Extrinsic value (or time value) is the added value from time left and market expectations.

### Some *jargons*

1. **In the money: ****An option is considered in the money if exercising it would be profitable. For a call option, this means the underlying asset's price is above the strike price. For a put option, it means the underlying asset's price is below the strike price.
    
    $$
    K \lt S_t \text{ where } t=T \text{ for a European option }
    $$
    
2. **Out-of-the-Money**: An option is out-of-the-money if exercising it would not be profitable. 
    
    $$
    K \gt S_t \text{ where } t=T \text{ for a European option }
    $$
    
3. **At-the-Money (ATM) :** An option is at-the-money if the underlying asset's price is exactly equal to the strike price. 
    
    $$
    K = S_t \text{ where } t=T \text{ for a European option }
    $$
    
    At this point, there is no intrinsic value, but the option may still have time value. In practice, the exact equal condition is rarely satisfied, so all the options with strike nearly equal to the Spot/Market price are ATM.
    
4. **Time Value:** Time value is the portion of the option's premium that exceeds its intrinsic value. It reflects the possibility that the option may gain intrinsic value before expiration due to movements in the underlying asset's price. The Greek theta helps measure the effect of time on the options premium.
    
    $$
    \text{Option premium = Intrinsic Value + Time Value }
    $$
    
    $$
    \text{TV}(t) = \begin{cases}C^e(t) - \max(0, S(t) - K), & \text{for European call} \\P^e(t) - \max(0, K - S(t)), & \text{for European put} \\C^a(t) - \max(0, S(t) - K), & \text{for American call} \\P^a(t) - \max(0, K - S(t)), & \text{for American put}\end{cases}
    $$
    
    Here, $C^e / P^e$ is the Option price and $\max(K/S(t) - S(t)/K)$ is the Intrinsic Value.
    
5. **Volatility:** Volatility refers to the degree of variation in the price of the underlying asset over time. Higher volatility increases the potential for an option to become profitable and, therefore, increases the option's premium. 
    1. **Historical Volatility:**  Based on past price movements of the underlying asset. It is calculated as the standard deviation of returns over a specific time period.
    2. **Implied Volatility:** The market’s expectation of future volatility. Represents the market participants’ take on volatility and is reflected in the ***premium***.
    3. **Realised Volatility:** The actual volatility reflected in the market
6. **Option Chain:** An option chain is a listing of all available option contracts for a particular underlying asset, typically presented in a table format. It includes various strike prices, expiration dates, and premiums for both call and put options.
    
    Analysing the option chain helps traders understand where market participants expect the stock to move and which strike prices are most popular.
    
    - **Strike Price Column**.
    - **Call Options on the Left**, **Put Options on the Right**
    - **Volume.**
    - **Open Interest** is the number of outstanding contracts, reflecting liquidity.
    - **Premiums** help you understand what the market is willing to pay for specific strikes.
    
    [Options Chain: What It Is and How To Read and Analyze It](https://www.investopedia.com/terms/o/optionchain.asp)
    
7. **Open Interest:** Open interest represents the total number of outstanding option contracts that have not been settled or closed. It gives an indication of the market's interest in a particular option.
    
    [Basic Option Jargons – Varsity by Zerodha](https://zerodha.com/varsity/chapter/basic-option-jargons/)
    

### Categorization

1. **American option:** In the American option, the contract can be exercised at any time up to the expiration date.
2. **European option**: In a European option, the contract is allowed to be exercised only on the expiration date.

### Payoff structures & Breakeven Point

1. **Long (Buy) call option:** The call owner is bullish (expects the stock price to rise) on the stock price movement. It will be exercised if and only if $K \lt S_t$ ($t=T$  for the European option)
    
    $$
    \text{IV} = \text{MAX} (S_t - K, 0)
    $$
    
    $$
    \text{Payoff} = C_t = \text{MAX(} S_t \text{ - K - premium, -premium)}
    $$
    
2. **Short (Sell) Call option:** You earn the premium if the price stays below the strike. The payoff is the negative of a long call option.
3. **Long (Buy) Put option:** The put owner is bearish (expects the stock price to fall) on the stock price movement
    
    $$
    \text{Payoff} = P_t = \text{MAX (Strike Price - Stock Price, 0)} - \text{premium}
    $$
    
4. **Short (Sell) Put option:** Profit if price stays above strike. The payoff is the negative of a long put. The owner will exercise it if and only if $K \gt S_t$ ($t=T$ if it is a European option)
    
    ![image.png](image.png)
    

> Check [this](https://youtu.be/48VEFNn2gbo?si=f0Q1aavk1FxOoAif) for a call option example and [this](https://youtu.be/48VEFNn2gbo?si=a7B8zeOe7h7aivzF) for a put option example.
> 

### Gain (and loss)

Consider a continuously compounded rate of interest $r$. Let $X$ be the premium paid by the owner, then the gain/loss at maturity for an option is

$$
G_T =
\begin{cases}
C_T - Xe^{rT} & \text{for long call} \\
Xe^{rT} - C_T & \text{for short call} \\ P_T - Xe^{rT} & \text{for long put} \\
Xe^{rT} - P_T & \text{for short put}
\end{cases}
$$

## Trading Strategies

### Protective Put:

A protective put involves holding a long position in the underlying asset (e.g., stock) and purchasing a put option with a strike price equal or close to the current price of the underlying asset. A protective put strategy is also known as a **synthetic call.**

> Long stock and long put position
> 

![Screenshot 2025-07-12 115403.png](Screenshot_2025-07-12_115403.png)

The net payoff is given as:

$$
N(S_t) = \text{stock payoff} + \text{long put gain}  = (S_T - S_0) + G_T = (S_T - S_0) + \text{MAX}(0, K - S_T) - X 
$$

### Protective Call

A Protective Call strategy is used to hedge the short position of a stock by purchasing an ATM or slightly OTM Call Option. This strategy works well in a scenario when you short the stock and want to protect yourself from the upside movement of the stock.

It’s like a bearish version of a protective put. 

> Short stock and long call position
> 

### Covered Call

A covered call involves holding a long position in the underlying asset (e.g., stock) and selling (writing) a call option on the underlying asset. The strategy is usually employed by investors who believe that the underlying asset will experience only minor price fluctuations.

> Long stock and short call position
> 

![Screenshot 2025-07-12 122408.png](Screenshot_2025-07-12_122408.png)

$$
N(S_t) = \text{stock payoff} + \text{short call gain}  = (S_T - S_0) + G_T = (S_T - S_0) + X -\text{MAX}(0,S_T - K)
$$

### Spreads

A spread is a portfolio consisting of options of the same type (either all calls or all puts). There are 3 kinds of spreads:

1. A **vertical spread or price spread** is a portfolio in which the options have the same expiration date but different strike prices
2. A **horizontal spread or calendar spread** is a portfolio in which the options have the same strike price but different expiration dates 
3. A **diagonal spread** is a portfolio in which the options have different strike prices in different expiration dates.

We introduce three popular spreads

1. **Bull spread:** Buying a call option at $K_1$-strike and writing another call option of the same type at $K_2$-strike with the same expiration, and $K_1 < K_2$, leads to a bull spread.
    
    ![](https://upload.wikimedia.org/wikipedia/commons/0/06/Bull_spread_using_calls.png)
    
    The net gain function for bull spread is given by :
    
    $$
    \mathcal{N}(S_T) = 
    \left[\max(0, S_T - K_1) - C_1\right] - \left[\max(0, S_T - K_2) - C_2\right] \\
    \textbf{Payoff:}
    \\
    \mathcal{N}(S_T) = 
    \begin{cases}
    -C_1 + C_2, & S_T \leq K_1 \\
    S_T - K_1 - C_1 + C_2, & K_1 < S_T < K_2 \\
    K_2 - K_1 - C_1 + C_2, & S_T \geq K_2
    \end{cases}
    $$
    
2. **Bear spread:** Buying a put option at $K_2$-strike and writing another put option of the same type at $K_2$-strike with the same expiration, and $K_1 < K_2$, leads to a bull spread.
    
    ![](https://upload.wikimedia.org/wikipedia/commons/0/0f/Bear_spread_using_puts.png)
    
    The net gain payoff function is the negative for a bull spread 
    
    $$
    \mathcal{N}(S_T) = \left[\max(0, K_2 - S_T) - P_2\right] - \left[\max(0, K_1 - S_T) - P_1\right]\\
    \textbf{Payoff:}\\
    \mathcal{N}(S_T) = \begin{cases}K_2 - K_1 - P_2 + P_1, & S_T \leq K_1 \\K_2 - S_T - P_2 + P_1, & K_1 < S_T < K_2 \\- P_2 + P_1, & S_T \geq K_2\end{cases}
    $$
    
3. **Butterfly spread:** Let $K_1 < K_2 < K_3$, and $K_2 \in [S_0 - \epsilon, S_0 + \epsilon]$ for some sufficiently small $\epsilon > 0$. Buy two call options, one in each of $K_1$-strike and $K_3$-strike. Write two call options with $K_2$-strike. All options have the same expiration. The resulting portfolio is a butterfly spread.
    
    $$
    \begin{align*}\mathcal{N}(S_T) &= \text{Gain in Long call-1} + \cancel{2} \times \text{Gain in Short put-2} + \text{Gain in Long call-3} \\&= \left( \max(0, S_T - K_1) - X_1 \right) + \cancel{2} \left( X_2 - \max(0, S_T - K_2) \right) + \left( \max(0, S_T - K_3) - X_3 \right) \\&= \begin{cases}-X_1 + 2X_2 - X_3, & \text{if } S_T \leq K_1 \\S_T - K_1 - X_1 + 2X_2 - X_3, & \text{if } K_1 \leq S_T \leq K_2 \\- S_T + K_1 + 2(K_2 + X_2) - X_1 - X_3, & \text{if } K_2 \leq S_T \leq K_3 \\- K_1 + 2K_2 - K_3 - X_1 + 2X_2 - X_3, & \text{if } K_3 \leq S_T\end{cases}\end{align*}
    $$
    
    ![](https://upload.wikimedia.org/wikipedia/commons/5/52/Butterfly_spread_with_calls.png)
    

> Check out more option strategies
> 
> 
> [10 Options Strategies Every Investor Should Know](https://www.investopedia.com/trading/options-strategies/)
> 

## Bounds for Option Prices

### European Options

1. **European Call on Non-Dividend-Paying Stock:**  Consider the European call option:
    1. $K$ - strike;
    2. period $[0, T]$;
    3. premium $C^e$,
    
    where the underlying stock with spot price $S_0$ pays no dividend during the option period. If the market does not allow arbitrage, then
    
    $$
    \max \left(0, S_0 - K e^{-rT} \right) \leq C^e \leq S_0,
    $$
    
    where $r$ is the prevailing annual interest rate continuously compounded.
    
2. **European Put on No Dividend Paying Stock:** Consider
    1. $K -$ Strike Price
    2. $P^e -$ Premium for Put Option
    3. Time Period $\in [0, T]$
    
    The spot price of the asset is $S$ and no dividend is paid during the period. Then,
    
    $$
    \max(0, Ke^{-rT} - S) \leq P^e \leq Ke^{-rT}
    $$
    
    $K > S$ in order to profitably exercise a put option.
    
3. **European Options on Dividend-Paying Stock:** Consider
    1.  $K$- strike;
    2. period $[0, T]$;
    3. premium $C^e$ for call and $P^e$ for put,
    
    The spot price of the stock is $S$ , and the stock pays a dividend $D_0$ at some time during the option period. Market does not allow arbitrage conditions.
    
    $$
    \max \left(0, S_0 - D_0 - K e^{-rT} \right) \leq C^e \leq S_0 - D_0, \quad \text{(call option)}
    $$
    
    $$
    \max \left(0, K e^{-rT} + D_0 - S_0 \right) \leq P^e \leq K e^{-rT}, \quad \text{(put option)}
    $$
    
    where $r$ is the annual interest rate compounded continuously.
    

### American options

1.  **American Call with No Dividend Payment:** With all the same parameters, consider 2 call options where:
    1. European Call option price = $C^e$
    2. American Call option price = $C^a$
    
    If the underlying stock does not pay dividend and the annual interest rate $r > 0$, then $C^a = C^e$.  Hence,
    
    $$
    \max(0, S - K e^{-rT}) \leq C^a \leq S
    $$
    
2. **American Put with No Dividend Payment:** Consider American put option with same parameters and assumptions. If the market does not allow arbitrage, then:
    
    $$
    \max(0, K - S) \leq P^a \leq K
    $$
    
3. **American Options on Dividend Paying Stock:** Consider an American option where the underlying stock has a spot price $S$ and pays a dividend $D_0$ at some time during the option period, then:
    
    $$
    \max \left( 0,\; S_0 - D_0 - K e^{-rT},\; S_0 - K \right) \leq C^a \leq S_0, \quad \text{for call option;}
    $$
    
    $$
     \max \left( 0,\; K e^{-rT} + D_0 - S_0,\; K - S_0 \right) \leq P^a \leq K, \quad \text{for put option;}
    $$
    
    Where $r$ is the annual interest rate compounded continuously and $K$ is the Strike price and $S_0$ is the spot price of the underlying stock.
    

## Put-Call Parity

### For European options

$$
C^e - P^e = S_0 - K e^{-rT}
$$

### For American options

$$
S_0 - K \leq C^a - P^a \leq S_0 - K e^{-rT}
$$

# Greeks

Option Greeks are a set of risk measures that describe how the price of an option is expected to change in response to different variables. Each Greek isolates one factor that affects an option's price, such as stock price movement, time decay, or volatility, so traders can manage their risk with precision.

### Delta ($\Delta = \frac{\delta f}{\delta S}$)

Delta measures how much the price of an option will change for a ₹1 move in the underlying asset. It tells you the **directional sensitivity of an option**. 

- For a European call with dividend yield: $\Delta = e^{-y\tau}N(d_1)$
- For a European put with dividend yield: $\Delta = e^{-y\tau}[1 - N(d_1)]$

It is also defined as the **hedge ratio of an option**.  

Delta of option $\times$ Quantity of options $+$ (Any other options $+$ Futures already in position) $\implies$Delta of position

![Screenshot 2025-07-13 230115.png](Screenshot_2025-07-13_230115.png)

Traders also use delta to estimate the probability of an option **expiring in the money.**

### Gamma ($\Gamma = \frac{\delta^2f}{\delta S^2}$)

Gamma tells you how much **delta will change** for every ₹1 move in the underlying asset. It is the *second derivative.* When the underlying asset moves, delta changes, and gamma tells you how quickly. High gamma values mean the option’s behaviour is more reactive to price movements, especially for ATM options close to expiry.

For a European call/put with dividend yield y: $\Gamma = \frac{N'(d_1)e^{-y\tau}}{S_0 \sigma \sqrt{\tau}}$

Gamma is crucial for **managing risk**, especially for traders with large delta exposures. It helps you understand how volatile your position might become.

![Screenshot 2025-07-13 225841.png](Screenshot_2025-07-13_225841.png)

### Theta

Theta measures **time decay -** how much value an option loses as it gets closer to expiry, assuming all other variables remain constant. Theta is always **negative** for long options (buyers lose value daily), but it is **positive** for option sellers (they gain value with time)

- For a European call option: $\Theta = -\frac{S N'(d_1) \sigma e^{-y \tau}}{2\sqrt{\tau}} + y S e^{-y \tau} N(d_1) - r K e^{-r \tau} N(d_2)$
- For a European put option: $\Theta = -\frac{S N'(d_1) \sigma e^{-y \tau}}{2\sqrt{\tau}} - y S e^{-y \tau} N(-d_1) + r K e^{-r \tau} N(-d_2)$

![Screenshot 2025-07-13 230229.png](Screenshot_2025-07-13_230229.png)

### Vega

Vega measures how much the price of an option changes with a **1% change in implied volatility**. 

For European options $\nu = \frac{\delta c}{\delta \sigma} = \frac{\delta p}{\delta \sigma} = S e^{-y\tau}\sqrt{\tau}N'(d_1)$. At-the-money options are most sensitive to volatility change, so they have higher vegas than either in-the-money or out-of-the-money options. The vegas of all options decrease as time to expiration becomes shorter

Options thrive on volatility - when the market expects big movements, option premiums rise. Vega shows how responsive your option is to those changes. Higher Vega means more sensitivity to volatility shifts. Longer-dated options tend to have higher vega. If implied volatility spikes, the price of all options - calls and puts - generally increases, even if the underlying stock doesn’t move. Vega is a friend to buyers during earnings season or major news events.

### Rho

Rho measures how much an option’s value will change with a **1% change in interest rates**. It’s usually the least impactful Greek but becomes important for long-term options. **Call options** have positive rho (they gain when rates rise) but p**ut options** have negative rho (they lose when rates rise).

In times of significant monetary policy changes, rho may start playing a larger role in pricing models.

## Volatility

Volatility is one of the most important factors affecting a options pricing. The simplest approach to determine the volatility of a security is to calculate the standard deviation of its prices over a period of time. 

Check the respective resources for 

1. Volume vs liquidity:
    
    [Volume vs Liquidity](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/volume-vs-liquidity/)
    
2. VIX:
    
    [CBOE Volatility Index (VIX): What Does It Measure in Investing?](https://www.investopedia.com/terms/v/vix.asp)
    
3. Fear and greed index:
    
    [Fear and Greed Index](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/fear-and-greed-index/)
    
4. Effect on option prices:
    
    [How Does Implied Volatility Impact Options Pricing?](https://www.investopedia.com/ask/answers/062415/how-does-implied-volatility-impact-pricing-options.asp)
    
5. Volatility skew :
    
    [Implied Volatility, Volatility Skew, and the Term Structure of Volatility](https://youtu.be/qTNvt8w7yjE?si=y3FxmzXgXPjC8GE9)
    

# Time models

[Option Pricing Models](https://corporatefinanceinstitute.com/resources/derivatives/option-pricing-models/)

## Discrete-time model: Binomial model

Let the period of the option be $[0, T]$. Let $T_n = \{t_0, t_1, \dots , t_n\}$ where $t_k=kh$ (with $h=T/n$). Then, in discrete time models, the transactions are assumed to occur only at times $t \in T_n$. At $t=t_k$ the stock price is denoted as $S(t_k)$. Let $s_k = \{U, D\}$ denote $S(t_k) \ge S(t_{k-1})$ and $S(t_k) \lt S(t_{k-1})$ respectively. 

Let $S = \{s= (s_1, s_2, \dots, s_n) | s_k \in {U, D}\}$. 

Define, at $t=t_k$, $B_{s_k} = \{s \in S | \text{the first k components of} s=s_k\}$

> **Filtration:**  A collection $\{F_t | t\ge 0\}$ of $\sigma$-fields on S is called a filtration if $F_s \subseteq F_t \forall 0 \le s \le t$
> 

Consider a portfolio $\Pi = (\phi, \theta, 0).$ The *finance market*  is defined as $(B, S)$

> **Trading Strategy:** The stochastic process of portfolios $\{\Pi_k | k = 1, 2, \dots, n\}$ where $\Pi_k$ corresponds to the period $[t_{k-1}, t_k]$ is called a trading strategy if each component of $\Pi_k$ is $F_{k-1}$-measurable.
> 

**Value Process of Portfolio:** Value process deals with the value of the portfolio at the time of closing it. 

$$
V(\Pi_k)(t_k) = \phi_k \times B_k + \theta_k \times S_k
$$

**Discounted Finance Market:**  Define the discounted stock price: $\tilde{S}_k = \frac{S_k}{B_k}, \quad B_k > 0$
Thus, the financial market becomes $(1, \tilde{S}_k)$ and portfolio value is: $V(\Pi_k)(t_k) = \phi_k B_k + \theta_k S_k = \phi_k + \theta_k \tilde{S}_k$

**Self-Financing Strategy:** A strategy is self-financing if: $V(\Pi_k)(t_k) = V(\Pi_{k+1})(t_k)$

$$
\Rightarrow (\phi_{k+1} - \phi_k)B_k + (\theta_{k+1} - \theta_k)S_k = 0
\Rightarrow \Delta\phi_k B_k + \Delta\theta_k S_k = 0
$$

**Replicating Strategy:** A self-financing strategy that replicates the payoff $H_T$: $V_n = H_T$

### Single Step Binomial Model

- $t_0 = 0$, $t_1 = T$
- $S_1 = S_0 U$ or $S_0 D$; $B_1 = B_0(1 + r)$
- $H_T = \max(0, S_1 - K)$ for call option

**Replicating Portfolio:**  Solve: $\phi_1 B_1 + \theta_1 S_1 = H_T
\Rightarrow
\begin{cases}
\phi_1 B_0(1 + r) + \theta_1 S_0 U = H_T^U \\
\phi_1 B_0(1 + r) + \theta_1 S_0 D = H_T^D
\end{cases}$

Solving: $\theta_1 = \frac{H_T^U - H_T^D}{S_0(U - D)}, \quad
\phi_1 = \frac{U H_T^D - D H_T^U}{B_0(1 + r)(U - D)}$

**Option Price:** 

$$
V_0 = \phi_1 B_0 + \theta_1 S_0
= \frac{1}{1 + r} \left[ p^* H_T^U + (1 - p^) H_T^D \right]
$$

where $p^* = \frac{1 + r - D}{U - D}, \quad H_T^* = \frac{H_T}{1 + r}
\Rightarrow V_0 = \mathbb{E}^[H_T^]$

**Two-Step Binomial Model:**

$$
H_0 = \frac{{p*}^2 H_{UU} + 2p^(1 - p^) H_{UD} + (1 - p*)^2 H_{DD}}{(1 + r)^2}
$$

### Multi-Step Binomial Model

**(CRR - (Cox, Ross, and Rubinstein)):** 

For an n-sub-interval partitioned option time period [0,T], the price of an attainable option is,

$$
H_0 = \frac{1}{(1 + r)^n} \sum_{j = 0}^{n}
\binom{n}{j} (p*)^j (1 - p*)^{n - j} H_{n, j}
$$

### **American Options (Backwards Induction)**

At each time $t_k$:

$$
V_k = \mathbb{E}^[H_{k+1}^a | \mathcal{F}_k], \quad
H_k^a = \max(H_k, V_k)
$$

Fair price at $t_k$ is: $H_k^a = \max\left(H_k, \mathbb{E}^[H_{k+1}^a | \mathcal{F}_k]\right)$. Exercise when $H_k \geq V_k$.

## Continuous time model: Black-Scholes model

Market Dynamics:

 $\begin{aligned}
dS_t &= \mu S_t dt + \sigma S_t dW_t \quad \text{(stock)} \\
dB_t &= r B_t dt \quad \text{(risk-free bond)} \\
S_t, B_t &> 0,\quad \mu, \sigma, r \in \mathbb{R},\ \sigma > 0
\end{aligned}$
Discounted stock: $\tilde{S}_t = \frac{S_t}{B_t} \Rightarrow d\tilde{S}_t = \tilde{S}_t(\sigma dW_t + (\mu - r) dt)$

### Self-Financing Portfolio

Portfolio value: $V_t = \phi_t B_t + \theta_t S_t$

Self-financing: $dV_t = \phi_t dB_t + \theta_t dS_t
\Rightarrow dV_t = r\phi_t B_t dt + \theta_t(\mu S_t dt + \sigma S_t dW_t)$ 

Discounted portfolio: $\tilde{V}_t = \frac{V_t}{B_t},\quad d\tilde{V}_t = \theta_t d\tilde{S}_t\Rightarrow \tilde{V}_t = \tilde{V}_0 + \int_0^t \theta_u d\tilde{S}_u$

**No-Arbitrage and Risk-Neutral Measure:**
There exists a probability measure $\mathbb{Q}$ under which: $\frac{S_t}{B_t} \text{ is a martingale} \Rightarrow dS_t = r S_t dt + \sigma S_t dW_t^{\mathbb{Q}}$. Option pricing under $\mathbb{Q}$: $V_0 = e^{-rT} \mathbb{E}^{\mathbb{Q}}[H_T]$. 

**Martingale Pricing:** Let $X_t = \frac{V_t}{B_t}$ be the discounted value process. Then, $X_t = \mathbb{E}^{\mathbb{Q}}[X_T | \mathcal{F}_t]$

### Replication and Completeness

Every European contingent claim $H_T$ (measurable w.r.t. $\mathcal{F}_T$) can be replicated by a self-financing strategy $\Pi = (\phi_t, \theta_t)$ if and only if the market is complete.

In Black-Scholes: completeness holds $\Rightarrow$ unique price: $V_0 = e^{-rT} \mathbb{E}^{\mathbb{Q}}[H_T]$

### Black-Scholes PDE

Let $V = V(S, t)$ be the price of a derivative. Then for option price $V(S, t)$: $\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0$.

Terminal condition for European call: $V(S, T) = \max(S - K, 0)$

**Black-Scholes Formula (Call)**
$C = S_0 N(d_1) - K e^{-rT} N(d_2)$
$d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \quad
d_2 = d_1 - \sigma\sqrt{T}$

$N(\cdot)$ is the standard normal cumulative distribution function.

### Delta-Hedging:

Delta of the option $\Delta = \frac{\partial V}{\partial S}$ evolves as a self-financing replicating portfolio. To hedge perfectly  hold $\theta_t = \Delta_t$ shares of the sto