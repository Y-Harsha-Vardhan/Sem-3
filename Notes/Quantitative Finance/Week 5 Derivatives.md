# Week 5 

# Derivatives

## What are derivatives?

Derivatives are powerful financial tools whose value comes from an underlying asset's performance - the **primary instrument**- , such as stocks, bonds, commodities, currencies, interest rates, or market indices. They are agreements set between two or more parties that can be traded on an exchange or over the counter (OTC).

Having no intrinsic value, derivatives derive their worth from changes in the underlying asset. They're used to hedge risks, speculate on price movements, or access otherwise difficult markets. Derivatives can move risk levels (and the accompanying rewards) from the risk-averse to the risk-seekers.

## Why use derivatives?

1. **Hedging:** One of the most important uses is to reduce risk. For instance, a company expecting to receive payments in foreign currency may use derivatives to lock in an exchange rate.
2. **Speculation:** Traders often use derivatives to bet on the direction of market movements. While this can lead to big gains, it can also result in substantial losses.
3. **Market Access:** Sometimes, derivatives are the only practical way to gain exposure to certain markets or asset classes, especially when direct investment is restricted or inefficient.

## Types of Derivatives

There are two classes of derivative products: **lock and option**. Lock products are noncontingent claims (e.g., futures, forwards, or swaps) that bind the respective parties from the outset to the agreed-upon terms over the life of the contract. Option products are contingent claims (e.g., stock options); on the other hand, they offer the holder the right, but not the obligation, to buy or sell the underlying asset or security at a specific price on or before the option’s expiration date.

1. **Futures Contracts**
These are standardized agreements to buy or sell an asset at a predetermined price on a set future date. Futures are traded on exchanges and are commonly used for commodities like oil or wheat, as well as for financial instruments.
2. **Forward Contracts**
Similar to futures, but these are private and customized agreements between two parties. They're traded over the counter (OTC), offering more flexibility but also introducing higher counterparty risk.
3. **Options**
Options give the holder the right - but not the obligation -to buy or sell an asset at a specified price before a certain date. There are two main types: call options (for buying) and put options (for selling).
4. **Swaps**
Swaps involve exchanging cash flows or other financial variables. A common example is an interest rate swap, where one party exchanges a fixed rate for a floating rate to manage exposure to interest rate fluctuations.

## OTC and Exchange-Traded Derivatives

Derivatives can be traded in two primary ways: 

- **Over-the-Counter (OTC):** They are privately negotiated contracts between two parties, offering high flexibility in terms, structure, and settlement. They're commonly used by institutions for customised risk management, but they also carry **counterparty risk** due to the absence of a central clearinghouse.
    - Market Tiers:
        - OTCQX is the top tier, featuring blue-chip stocks from countries like Europe, Canada, Brazil, and Russia. Companies must meet high financial standards, follow good governance, comply with U.S. laws, and maintain current disclosures.
        - OTCQB, the middle tier or "venture market," includes early-stage U.S. and international firms. Companies must be current in reporting, pass annual verification, meet a $0.01 bid test, and not be in bankruptcy.
        - OTC Pink is the lowest tier, with no reporting or SEC registration requirements. It includes both legitimate companies and high-risk entities such as shell companies.
    - Looser regulation means OTC markets can be riskier than national exchanges. Other risks of operating outside the full supervision of a formal exchange include less price transparency, fewer buyers and sellers, which can make exiting a position harder and lead to wider spreads, greater volatility, and the possibility that the other party to the transaction defaults and can’t make good on their side of the trade.
        
        [Over-the-Counter (OTC) Markets: Trading and Securities](https://www.investopedia.com/terms/o/otc.asp)
        
- **Organized exchanges:** Exchange-traded derivatives like futures and options are standardized contracts listed on regulated exchanges (e.g., NSE, CME), providing transparency, liquidity, and lower counterparty risk thanks to centralized clearing. While exchange-traded products suit traders seeking liquidity and lower credit risk, OTC contracts are preferred when bespoke solutions are needed.
    
    [Exchange-Traded Derivative: Definition, Examples, Vs. OTC](https://www.investopedia.com/terms/e/exchange-traded-derivative.asp)
    

[Five Differences Between OTC and Exchange Traded Derivatives - HedgeStar](https://hedgestar.com/single-post/2024/06/27/five-differences-between-otc-and-exchange-traded-derivatives/)

# Futures

## What?

A futures contract is a standardized agreement to buy or sell a specific quantity of an asset at a predetermined price on a specified future date. These contracts are based on the future value of an individual company’s shares or a stock market index like the S&P 500, Dow Jones Industrial Average, or Nasdaq.

Futures are traded on regulated exchanges, which ensures their standardization and oversight.

They serve both hedging and speculative functions. They enhance market liquidity and facilitate price discovery across various markets, including commodities, currencies, and financial instruments.

[What are Futures Contracts?](https://youtu.be/9BQr-vxwqJs?si=vKnVrt0SlkCqGJ7f)

## How it works?

Futures contracts are standardised by quantity, quality, and asset delivery, making trading them on futures exchanges possible. They bind the buyer to purchasing and the other party to selling a stock or shares in an index at a previously fixed date and price, enhancing liquidity and transparency.

The contract with the nearest expiration date is known as the “front-month” contract, which often has the most trading activity. As a contract nears expiration, traders who want to maintain a position typically roll over to the next available contract month. Short-term traders often work with front-month contracts, while long-term investors might look further out

### Underlying Assets

- Commodity futures with underlying commodities such as crude oil, natural gas, corn, and wheat
- Cryptocurrency futures are based on moves in assets like Bitcoin or Ethereum
- Equities futures, which are based on stocks and groups of stocks traded in the market
- Interest rate futures
- Stock index futures with underlying assets such as the S&P 500 Index

Before expiration, the futures contract - the long position - can be sold at the current price, closing the long position.

[Long Position: Definition, Types, Example, Pros and Cons](https://www.investopedia.com/terms/l/long.asp)

### Margin

Suppose a trader chooses a futures contract on the S&P 500. The index is 5,000 points, and the futures contract is for delivery in three months. Each contract is $50 times the index level, so one is worth $250,000 (5,000 points × $50). Without leverage, traders would need $250k. In futures trading, traders only need to post a margin, a fraction of the contract’s total value.7 If the initial margin is 10% of the contract’s value, the trader deposits only $25,000 (10% of $250,000) to enter the futures contract. If the index falls by 10% to 4,500 points, the value of the futures contract decreases to $225,000 (4,500 points × $50). Traders face a loss of $25,000, which equals a 100% loss on the initial margin.

[https://youtu.be/deThGfn2CjA?si=D6M3tlhH1O-j4jwe](https://youtu.be/deThGfn2CjA?si=D6M3tlhH1O-j4jwe)

[Margin and Margin Trading Explained Plus Advantages and Disadvantages](https://www.investopedia.com/terms/m/margin.asp)

## Hedging

Futures trading can hedge the price moves of the underlying assets. 

The two main hedging strategies in the market are :

- Prefect Hedging
- Cross Hedging

### Perfect Hedging

Perfect hedging using futures is a strategy aimed at completely eliminating the risk of adverse price movements by taking an equal and opposite position in the futures market.

**For Example,**

Current market selling price for rice = $20/kg

Total available quantity = 1000 kgs

- In order to avoid the risk of price drop, the farmer takes a short position in the
future market deciding for a strike price of $20.50/kg

Now, assume the future spot price = $18/kg

Loss incurred on selling of rice = $2.5 × 1000 = $2500

Gains on future selling of assets = $2.5 × 1000 = $2500

- Therefore, this ensures that the seller isn’t at a loss in case of a price drop or at a profit in case of a rise.

### Cross Hedging

When the perfect instruments aren’t available, we use future contracts on one asset to hedge the risk on another asset. This is called cross-hedging and introduces a new type of risk, basis risk.

### Basis Risk

The risk which arises when the hedge on the futures’ asset might not completely offset the
risk we are trying to reduce, because the hedge and the underlying asset are not perfect substitutes. As a result, the price of this asset and the price of hedging instrument aren’t completely correlated.

- Basis risk is the unavoidable cost of cross hedging.
- It can be minimized using Minimum Variance Hedging Ratio(MVHR).

### Minimum Variance Hedging Ratio

It tells us the optimal number of future contracts to use for each unit of asset we are hedging.

                                                             $h=\rho \times \frac{\sigma_S}{\sigma_F}$

- $h:$  The hedge ratio we want to calculate
- $\rho:$ The Correlation Coefficient, which measures how strongly the spot and
futures price move together.
1. $\rho=1:$ The future price of the asset and the hedging instrument moves perfectly
in sync with each other.
2. $\rho=0:$ There’s no correlation between the two.
3. $\rho=-1:$ They move exactly opposite to each other. 
- $\sigma_S:$ The Standard Deviation of Spot Price Changes.
- $\sigma_F:$ The Standard Deviation of Spot Price Changes.

If,

- $\sigma_S>\sigma_F$, the volatility ratio is > 1 and thus, we will have to use more future assets
to hedge each unit of the original asset.
- $\sigma_S<\sigma_F$, the ratio is < 1 and hence, we use less than a 1-to-1 hedge.

**Example,**
Suppose an investor holds a portfolio of stocks worth $10,00,000 and wishes to hedge the market risk using index futures. Based on historical data, the following values are estimated :

- Correlation between spot and futures returns, $\rho = 0.85$
- Standard deviation of spot returns, $\sigma_S=0.03$
- Standard deviation of futures returns, $\sigma_F=0.04$
- Value of one futures contract = $2,00,000

### Step 1 : Compute the Optimal Hedge Ratio

Using the minimum variance hedge ratio formula :

                                                             $h^*=\rho \times \frac{\sigma_S}{\sigma_F}$

                          $\implies h^*=0.85 \times \frac{0.04}{0.04}=0.85\times 0.75= 0.6375$

### Step 2 : Compute the number of Future Contracts

                           $\text{Number of contracts} = h^* \cdot \frac{\text{Value of portfolio}}{\text{Value of one futures contract}}$

                                                                    $= 0.6375 \cdot \frac{10,00,000}{2,00,000} = 0.6375 \cdot 5 = 3.1875$

**Conclusion,**

The investor should take a short position in approximately 3 or 4 index futures contracts to hedge the portfolio using the minimum variance hedge strategy.

[Hedge: Definition and How It Works in Investing](https://www.investopedia.com/terms/h/hedge.asp)

## Trading Strategies

- **Going long:** Going long - buying a futures contract - is the most basic futures trading strategy. An investor buys a futures contract expecting the contract to rise in price by expiration. The futures contract offers a leveraged return on the underlying asset’s rise, so the trader expects a clear move higher in the near future.
- **Going short:** Going short - selling a futures contract - is the flip side of going long. An investor sells a futures contract expecting the contract to fall by expiration. Investors going short a contract want the full leveraged returns of an asset that is expected to fall.
- **Bull calendar spread:** A calendar spread is a strategy that has the trader buying and selling contracts on the same underlying asset but with different expirations. In a bull calendar spread, the trader goes long the short-term contract and goes short the long-term contract. A calendar spread reduces the risk in a position by eliminating the key driver of the contract’s value - the underlying asset. The goal of this futures trading strategy is to see the spread widen in favour of the long contract.
- **Bear calendar spread:** Like the bull calendar spread, the bear calendar spread has the trader buying and selling contracts on the same underlying asset but with different expirations. A calendar spread reduces the risk by neutralising the key driver of the contract’s value - the underlying asset. In a bear calendar spread, the trader sells the short-term contract and buys the long-term contract. The goal of this futures trading strategy is to see the spread widen in favour of the short contract.

[4 Popular Futures Trading Strategies](https://www.magnifymoney.com/investing/futures-trading-strategy/)

# Forwards

A forward contract is an agreement to buy or sell an asset at a specified future date for a price agreed upon today.

Forwards are customized, over-the-counter (OTC) contracts tailored to the specific needs of the contracting parties.

Their primary purpose is to hedge against price fluctuations in commodities, currencies, or financial assets.

[https://youtu.be/J0sKv8cples?si=35DccRZGexbAcmAf](https://youtu.be/J0sKv8cples?si=35DccRZGexbAcmAf)

## Difference from futures

Futures contracts are traded over the counter, which means there is no regulatory body, whereas Futures contracts are traded under the counter, that is, there is a body which makes sure that the other party does not default.

Futures contract was introduced to counter the different problems caused by the Forward contract, the major problem being the risk of default.

# Notations

- Issue time $t=0$
- Expiration time $t=T$
- Strike Price/Forward Price $F(0,T)$ : This may be different for the same expiration time due to the presence of other traders and the change in the underlying asset price.
- Spot Price (at any time $t \in [0, T]$) is $S(t)$
    
    Note that $F(T, T) = S(T)$
    
- Strike Price $F(t, T)$

The return associated with the forward is $R_f(t; 0, T) := F(t, T) - F(0, T)$

The payoff from a forward contract initiated at $t=0$ is the trader’s total return from the contract till its expiration. That is, $R_f(T; 0, T)$ or the long position and $-R_f(T; 0, T)$ for the short position.

- For a long position, the payoff is $S_T - K$ and it will benefit from a higher underlying price.
- For a short position, the payoff is $K-S_T$ and it will benefit from a lower underlying price.

The value of the physical delivery can be priced as 

$$
F = S_0e^{rt}
$$

# Pricing forward and futures

We make two assumptions:

1. The prevailing interest rate in a risk-free investment is the same for both lending and borrowing.
2. There is no arbitrage opportunity available in the market.

Before proceeding, let’s introduce a portfolio

### Portfolio

A portfolio is a collection of assets $(\mathbf{B, S, D})$ that is an ordered tuple of real numbers, each denoting a risk-free asset(like a bond), a risky asset(like stock of a company) and derivative instruments, respectively. 

$$
\Pi := (\mathbf{b, s, d})
$$

Once a portfolio is built, the value of the portfolio is defined as

$$
V(\Pi)(t) = \Sigma_{i=1}^{n_b}b_iB_i(t) + \Sigma_{i=1}^{n_s}s_iS_i(t) + \Sigma_{i=1}^{n_d}d_iD_i(t) \\ \implies V(\Pi)(t) = \mathbf{b}\cdot\mathbf{B(t)} + \mathbf{s}\cdot\mathbf{S(t)} + \mathbf{d}\cdot\mathbf{D(t)}
$$

assuming the portfolio is built at time $t=0$ and is held till time $t=T$.

A portfolio is an **arbitrage portfolio** if it satisfies :

- $V(\Pi)(0) = 0$
- $V(\Pi)(T)\ge 0$
- $P(V(\Pi)(T) \gt 0) \gt 0$

Our assumption is that arbitrage is not allowed.

## Forwards with no intermediate payments

> Suppose the underlying asset has no extra cost during the forward contract. Also assume no arbitrage exists and short selling is allowed. Then, the forward price $F(t, T)$ at time $t$ for maturity $T$ is:
> 
> 
> $$
> F(t, T) =
> \begin{cases}
> S(t) \left(1 + \frac{r}{m} \right)^n - AI(t), & \text{(discrete compounding)} \\
> S(t) e^{r(T - t)}, & \text{(continuous compounding)}
> \end{cases}
> $$
> 

**A sketch for the proof**

Let the current time be $t=0$, and let the futures contract expire at $t=T$.

Consider the following arbitrage portfolio:

$$
\begin{array}{l|cc}
\textbf{Transaction} & \textbf{Now} & \textbf{At Expiry} \\
\hline
\text{Buy Spot} & -S_0 & S_T \\
\text{Borrow at rate } r & +S_0 & -e^{rT} S_0 \\
\text{Sell Futures Contract} & 0 & F_0 - S_T \\
\hline
\text{Net Proceeds} & 0 & F_0 - e^{rT} S_0 \\
\end{array}
$$

We see that $V(\Pi)(0) = 0$ . This portfolio is designed to return $F_0 - e^{rT} S_0$ at time $T$, with no additional costs.

![](https://ds055uzetaobb.cloudfront.net/brioche/uploads/E5NpEpNBxG-31.png?width=2400)

If this value is positive, arbitrageurs would buy the spot and sell the future. If it's negative, they would sell the spot and buy the future. This trading activity forces the portfolio’s value to zero in equilibrium.

Therefore, to prevent arbitrage, the futures price must satisfy:

$$
F_0 = e^{rT} S_0
$$

## Forwards with cost

Assume that the underlying asset involves an additional cost of Rs. $C$ to maintain it during the forward contract period $(0, T)$. Further, assume that there is no arbitrage opportunity available in the market and the market allows short trades.
Then the fair forward price is given by:

$$
F(0, T) = (S(0) + C)e^{rT},
$$

## Forwards with dividend yield

Assume that the underlying asset pays a dividend continuously at the rate $r_d$. Further, assume that there is no arbitrage opportunity available in the market and the market allows short trades.

Then the fair forward price is given by:

$$
F(0, T) = S(0) e^{(r - r_d)T},
$$

where $r$ is the annual interest rate and the continuous compounding scheme is considered.

## Forwards with dividend

Assume that the underlying asset pays a dividend x rupees at time $t=\tau \in (0, T)$. Further, assume that there is no arbitrage opportunity available in the market and the market allows short trades.

![](https://ds055uzetaobb.cloudfront.net/brioche/uploads/iJhRJ0wlZO-34.png?width=2400)

Then the fair forward price is given by:

$$
F(0, T) = (S(0) - xe^{-r\tau}) e^{rT},
$$

where $r$ is the annual interest rate and the continuous compounding scheme is considered.

We can factor in other associated costs.

## Value of Forwards Contract

Assume that there is no arbitrage opportunity available in the market and the market allows short trades. Then the value of a long forward contract at any time $t\in [0, T]$ is given by 

$$
V(t) = (F(t, T) - F(0, T))e^{-r(T-t)}
$$

where the prevailing risk-less investment is assumed to provide continuous interest with annual interest rate r. The value of a short forward contract is given by $-V(t)$

## What about futures?

Assume that longs and shorts are allowed with fractional units, and the market doesn’t allow arbitrage. Then, if the prevailing interest is constant for the period $[0, T]$ of the future, then 

$$
f(t, T) = F(t, T)
$$

# **Netting & Mark-to-Market**

## Netting

Netting is a risk management technique used in financial markets to reduce the number of transactions and the overall exposure between parties. It involves offsetting the value of multiple positions or payments due between two or more parties, resulting in a single net payment obligation. 

There are several types of netting:

- **Bilateral Netting:** Two parties agree to offset their mutual obligations, resulting in a single net amount owed by one party to the other.
- **Multilateral Netting**: Multiple parties offset their obligations through a central clearinghouse, which simplifies the process and reduces the total number of transactions.
- **Payment Netting**: Only payment obligations are netted, reducing the number of individual payments made between parties.
- **Close-out Netting:** In the event of a default or termination, all outstanding transactions are netted to determine a single net payment obligation.

## Mark-to-Market (MTM)

Mark-to-market is an accounting practice that involves valuing financial instruments at their current market price, rather than at their historical cost. This provides a more accurate and up-to-date reflection of an entity's financial position.

- **Daily Valuation:** The value of assets and liabilities is updated daily to reflect market conditions.
- **Transparency:** Provides a clear and transparent view of an entity's financial health and exposure to market risks.
- **Risk Management**: Helps in managing risk by ensuring that financial statements reflect the current market value of positions.

Let’s understand the dynamics of Marking to Market!

- The two parties involved, Party A (Long) and Party B (Short), deposit $10\%$ of the strike price as a margin deposit with the exchange, which acts as a regulatory intermediary.
- On each trading day, based on the prevailing future price $f(t,T)$, the exchange adjusts the margin accounts of both parties using the price difference:
    
                                                            $\Delta C_t = f(t, T) - f(t - 1, T)$
    
- If $\Delta C_t>0$, the amount is deducted from the Short party’s margin account (Party B) and credited to the Long party’s margin account (Party A). Conversely, if $\Delta C_t<0$, the transfer is from Party A to Party B.
- This daily adjustment process is referred to as Marking to Market, ensuring that unrealized gains and losses are reflected and settled each day.
- If a party’s margin balance falls below a predefined maintenance margin, the exchange issues a margin call, requiring the party to top up their account to maintain the required margin level (typically 10% of the strike price).
- This process continues daily until the contract’s expiration or until one of the parties chooses to exit their position.
- If the Long party exits, it must sell the asset at the current future market price on the next trading day. If the Short party exits, it must buy the asset at the prevailing future price at that time.

[Margin & M2M – Varsity by Zerodha](https://zerodha.com/varsity/chapter/margin-m2m/)