# Week 3: Time Series Analysis

# Time Series Analysis

## What?

Time series analysis is a crucial tool in financial markets used to study and forecast the behavior of various financial variables like stock prices, interest rates and exchange rates. 

A time series refers to a collection of data points recorded at different time intervals for a particular variable. Examples include a company’s quarterly sales, daily stock returns, or monthly currency exchange rates. What sets time series data apart is that each observation is tied to a specific point in time, maintaining a chronological order.

## Characteristics

Time series data often shows specific patterns that are important to recognize for accurate analysis and forecasting:

1. **Trends:** These are long-term movements in the data, showing a consistent rise or fall over time.
2. **Seasonality**: Time series may follow recurring patterns at fixed intervals, such as daily, weekly, or yearly, due to seasonal effects.
3. **Volatility**: Some time series fluctuate significantly and unpredictably, with sharp changes in values over short periods.
4. **Non-linearity**: The relationship between time and the variable may not follow a straight line, making it challenging to capture with simple linear models.

[https://youtu.be/GE3JOFwTWVM?si=ejA-RpfaKJ4nvE6s](https://youtu.be/GE3JOFwTWVM?si=ejA-RpfaKJ4nvE6s)

## Stationarity

### Types of Stationarity

Stationarity in time series comes in different forms, depending on which aspects of the data remain stable over time:

1. **Strict Stationarity**: This is the most rigid form. It means the entire distribution of the data, including the mean, variance, and even higher moments like skewness, stays exactly the same no matter when you observe it. In practice, it's extremely rare to find real-world data that meets this condition.
2. **First-Order Stationarity:** Here, only the average value (the mean) of the series remains fixed over time. Other properties, like variance or how spread out the values are, can still shift.
3. **Second-Order (Weak) Stationarity**: This is the most commonly used type. It assumes that the mean and variance stay the same throughout, and the relationship between data points (captured by autocovariance) depends only on how far apart they are in time, not when they occur.

### Why Stationarity Matters?

When working with time series data, one of the most important things to check is whether the data is stationary.  If the data is non-stationary, it can throw off the results leading to unreliable predictions.

[https://youtu.be/oY-j2Wof51c?si=WZJQ4I7wLxA-WFsd](https://youtu.be/oY-j2Wof51c?si=WZJQ4I7wLxA-WFsd)

### How to check?

There are a number of ways to test if your time series is stationary:

1. **Unit Root Tests**: Tests like the Augmented Dickey-Fuller (ADF) and Zivot-Andrews are used to see if the series has a unit root, which is a red flag for non-stationarity.
2. **KPSS Test**: This test works a bit differently - it checks if the series is stationary around a trend or needs differencing to become stationary.
3. **Run Sequence Plots**: A simple but effective visual method. These plots show the data over time and help spot trends or seasonal patterns.
4. **Less Common Tests**: There are more advanced methods like the Priestley-Subba Rao test or wavelet-based techniques, which are used in more specialized scenarios.

### How to make a time series stationary?

- **Differencing**: One of the most common methods. You take the difference between consecutive data points, which often stabilizes the mean.

[https://youtu.be/IKY_uDiSe8U?si=yer7ZHdWNCO6_UB3](https://youtu.be/IKY_uDiSe8U?si=yer7ZHdWNCO6_UB3)

- **Detrending**: Fit a trend line to your data (linear or nonlinear), then analyze the leftover part (the residuals), which is often stationary.
- **Smoothing and Transformations**: Techniques like taking the logarithm or square root of the data can help stabilise the variance and make the series more predictable.

### To learn more about stationarity, check out the following resources:

[Seasonality: What It Means in Business and Economics, Examples](https://www.investopedia.com/terms/s/seasonality.asp)

[Time Series Analysis](https://medium.com/swlh/time-series-analysis-7006ea1c3326)

## Seasonality

### Testing for seasonality

Once we’ve understood the foundational properties of time series, the next step is to analyse seasonality - whether patterns repeat at regular intervals. 

Other than checking it visually, one can do local versus global checks for $\mu$ and $\sigma$.

Several statistical tests are also commonly used. Some of them are:

- One of the most widely used methods is the **Augmented Dickey-Fuller (ADF) test**, which helps check for the presence of a unit root, indicating non-stationarity.

[Augmented Dickey-Fuller (ADF) Test - Must Read Guide - ML+](https://www.machinelearningplus.com/time-series/augmented-dickey-fuller-test/)

[https://youtu.be/warCSvy1DMk?si=H6cB1-XYORg2YojI](https://youtu.be/warCSvy1DMk?si=H6cB1-XYORg2YojI)

[https://youtu.be/1opjnegd_hA?si=1vbeHz2LqlLf12We](https://youtu.be/1opjnegd_hA?si=1vbeHz2LqlLf12We)

- Another approach is combining ADF with the KPSS test. While ADF checks for non-stationarity, KPSS checks for stationarity. Together they provide a more complete picture.

[Understanding Stationary Time Series Analysis](https://www.analyticsvidhya.com/blog/2021/06/statistical-tests-to-check-stationarity-in-time-series-part-1/)

## Time Series Forecasting

After identifying whether the data is stationary or seasonal, forecasting models like ARMA, ARIMA, SARIMA, and SARIMAX handle various combinations of autoregression, integration (differencing), and moving averages with or without seasonality.

- **ARIMA model** (Auto-Regressive Integrated Moving Average)**:** It is made of 3 components
    - **AR (Auto-Regressive):** Represented by ****AR(p), with the p parameter determining the number of lagged series that we use.
        
        $$
        y_t = c + \Sigma^{p}_{n=1}{\alpha_n\cdot t_{t-n}} + \epsilon_t
        $$
        
        **Note:** AR(0), that is, with no autoregressive terms, the time series is only white noise.
        
    - **I(Integrated):**  I(d) is the difference order, which is the number of transformations needed to make the data stationary.
        
        **Note: A**n ARIMA model is simply an ARMA model on the differenced time series.
        
    - **MA (Moving Average):** MA(q) is the moving average model, and q is the number of lagged forecasting error terms in the prediction.
    
    Finally, for example: ARIMA(1, 1, 1), $W_t = \omega + \phi_1 W_{t-1} + \theta_1 \epsilon_{t-1} + \epsilon_{t}$ where $Y_{t-1} - Y_t = W_t$
    
- **SARIMA(Seasonal ARIMA) model:** Look at the difference between the current point and the same point in the previous season $Y_t - Y_{t-s}$.
    
    Represented as ARIMA$(p, d, q) (P, D, Q)_s$ where P, D and Q represent the number of seasonal AR terms, seasonal differences and seasonal MA terms respectively where s is the length of the season.
    

[Time Series Forecasting with ARIMA , SARIMA and SARIMAX | Towards Data Science](https://towardsdatascience.com/time-series-forecasting-with-arima-sarima-and-sarimax-ee61099e78f6/)

Finally, for multivariate time series, where multiple related variables are considered, the **Vector Autoregressive (VAR) model** is a powerful tool.

[Introduction to the Fundamentals of Vector Autoregressive Models](https://www.aptech.com/blog/introduction-to-the-fundamentals-of-vector-autoregressive-models/)

[https://youtu.be/0-FKPJ5KxSo?si=mi9iqIBBNH5a_vqq](https://youtu.be/0-FKPJ5KxSo?si=mi9iqIBBNH5a_vqq)

# Few Trading Strategies

## 1. Exponential Smoothing Overview

Exponential smoothing is a fundamental trend-following technique used in time series analysis. The core concept revolves around **moving averages (MA)**, which help smooth out short-term fluctuations to reveal underlying trends.

### Key Concepts:

- **Purpose**: Reduce noise and identify trends in time series data
- **Method**: Apply weighted averages to historical data points
- **Result**: Smoother series that highlights significant patterns

## 2. Simple Moving Average (SMA)

### Definition

Simple Moving Average calculates the arithmetic mean of a specified number of past data points, treating each point equally.

### How it Works:

1. Choose a window size (e.g., 10, 20, 50 days)
2. Calculate the average of the most recent n data points
3. Move the window forward and repeat for each time step
4. Connect the averages to create a smoothed trend line

### Characteristics:

- **Equal weighting**: All data points in the window have equal importance
- **Lag effect**: Longer windows create smoother lines but increase lag
- **Initial data loss**: Cannot calculate MA for the first n-1 data points

**Resource**: [Investopedia - Moving Average](https://www.investopedia.com/terms/m/movingaverage.asp)

## 3. Exponential Moving Average (EMA)

### Concept

Unlike SMA, EMA gives more weight to recent data points, making it more responsive to current market conditions.

### Key Features:

- **Weighted approach**: Recent prices have more influence than older prices
- **Faster response**: More sensitive to price changes than SMA
- **Continuous calculation**: Uses all historical data with decreasing weights

### Formula Structure:

EMA = α × Current Price + (1-α) × Previous EMA

Where α (alpha) is the smoothing parameter (0 < α < 1)

**Resource**: [Investopedia - Exponential Moving Average](https://www.investopedia.com/terms/e/ema.asp)

## 4. Basic Trading Strategy: Moving Average Crossover

### Strategy Setup:

1. **Choose two time periods**: Short-term (e.g., 50 periods) and long-term (e.g., 100 periods)
2. **Calculate both EMAs/SMAs** for your chosen periods
3. **Monitor crossover points** between the two averages

### Trading Rules:

- **Buy Signal**: When short-term MA crosses above long-term MA (Golden Cross)
- **Sell Signal**: When short-term MA crosses below long-term MA (Death Cross)
- **Exit Strategy**: Close positions when signals reverse

### Logic:

- Short-term MA represents recent trend momentum
- Long-term MA represents overall market direction
- Crossovers indicate potential trend changes and trading opportunities

**Educational Resources**:

- [Moving Average Strategy Explained](https://www.youtube.com/watch?v=810jmf7drFw)
- [Implementation Tutorial](https://www.youtube.com/watch?v=PUk5E8G1r44)

## 5. Advanced Models: Holt's Linear Trend

### Simple Exponential Smoothing

$$
Base Model: ŷ_{t+1|t} = l_t
$$

**Level Equation**: $l_t = αy_t + (1-α)l_{t-1}$

Where:

- $l_t$ = level (smoothed estimate of the series)
- α = smoothing parameter
- y_t = actual observation at time t
    
    **Reference**: [Forecasting: Principles and Practice - Simple Exponential Smoothing](https://otexts.com/fpp2/ses.html)
    

### Holt's Linear Trend Model

Extends simple exponential smoothing by adding a trend component.

**Three Core Equations**:

1. **Forecast Equation**: $ŷ_{t+h|t} = l_t + hb_t$
2. **Level Equation**: $l_t = αy_t + (1-α)(l_{t-1} + b_{t-1})$
3. **Trend Equation**: $b_t = β(l_t - l_{t-1}) + (1-β)b_{t-1}$

**Parameters**:

- **h**: forecast horizon (number of steps ahead)
- **α**: level smoothing parameter
- **β**: trend smoothing parameter
- **l_t**: level at time t
- **b_t**: trend at time t

**Parameter Selection Guidelines**:

- Higher α values: More responsive to recent changes
- Lower α values: More stable, less reactive
- β controls trend component responsiveness

**Resources**:

- [Detailed Holt's Model Explanation](https://towardsdatascience.com/forecasting-with-holts-linear-trend-exponential-smoothing-af2aa4590c18)
- [Implementation Code](https://github.com/egorhowell/Youtube/blob/main/Time-Series-Crash-Course/11.%20Holt's%20Linear%20Trend%20Model.ipynb)

## 6. Holt-Winters Model (Triple Exponential Smoothing)

Adds seasonality component to capture recurring patterns in data.

### Four Core Equations:

1. **Forecast Equation**: $ŷ_{t+h|t} = l_t + hb_t + s_{t+h-m}$
2. **Level Equation**: $l_t = α(y_t - s_{t-m}) + (1-α)(l_{t-1} + b_{t-1})$
3. **Trend Equation**: $b_t = β(l_t - l_{t-1}) + (1-β)b_{t-1}$
4. **Seasonality Equation**: $s_t = γ(y_t - l_{t-1} - b_{t-1}) + (1-γ)s_{t-m}$

**Additional Parameters**:

- **γ (gamma)**: seasonality smoothing parameter
- **s_t**: seasonal component at time t
- **m**: length of seasonal cycle

**Use Cases**:

- Data with clear seasonal patterns (daily, weekly, monthly, yearly cycles)
- Sales forecasting with seasonal variations
- Economic indicators with cyclical behavior

**Resources**:

- [Holt-Winters Implementation](https://github.com/egorhowell/Youtube/blob/main/Time-Series-Crash-Course/12.%20Holt%20Winters%20Forecasting.ipynb)

[https://www.youtube.com/watch?v=FguKsUvL93o&list=PLKmQjl_R9bYd32uHImJxQSFZU5LPuXfQe&index=10](https://www.youtube.com/watch?v=FguKsUvL93o&list=PLKmQjl_R9bYd32uHImJxQSFZU5LPuXfQe&index=10)

[https://www.youtube.com/watch?v=s6aRM8gLXwU&list=PLKmQjl_R9bYd32uHImJxQSFZU5LPuXfQe&index=11](https://www.youtube.com/watch?v=s6aRM8gLXwU&list=PLKmQjl_R9bYd32uHImJxQSFZU5LPuXfQe&index=11)

[https://www.youtube.com/watch?v=LM6ynZc-KGI](https://www.youtube.com/watch?v=LM6ynZc-KGI)