# Classical Time Series Analysis

ML methods can be used for classification and forecasting on time series problems.

Before exploring ML methods for time series, it is a good idea to explore classical **linear** time series forecasting methods. Classical time series forecasting methods may be focused on linear relationships, nevertheless, they are sophisticated and perform well on a wide range of problems (subject to some assumptions). 

Here, a suite of classical methods for time series forecasting are explained that you can test on your forecasting problem prior to exploring to ML methods.

**Overview**
This cheat sheet demonstrates 11 different classical time series forecasting methods; they are:
  - Autoregression (AR)
  - Moving Average (MA)
  - Autoregressive Moving Average (ARMA)
  - Autoregressive Integrated Moving Average (ARIMA)
  - Seasonal Autoregressive Integrated Moving-Average (SARIMA)
  - Seasonal Autoregressive Integrated Moving-Average with Exogenous Regressors (SARIMAX)
  - Vector Autoregression (VAR)
  - Vector Autoregression Moving-Average (VARMA)
  - Vector Autoregression Moving-Average with Exogenous Regressors (VARMAX)
  - Simple Exponential Smoothing (SES)
  - Holt Winter’s Exponential Smoothing (HWES)


**Autoregression (AR)**
  * The AR method seeks to model the next step in the data sequence as a linear function of the observations at prior time steps.
  * The notation: AR(p). For example, AR(1) is a first-order autoregression model, i.e. y^(t) ~ y(t-1)
  * The method is suitable for univariate time series ```without trend``` and ```without seasonal components```.

**Moving Average (MA)**
  * The MA method seeks to model the next step in the sequence as a linear function of the **residual errors** from a mean process at prior time steps.
  * A moving-average model is different from the concept of moving average in statistics. 
  * The notation: MA(q). For example, MA(1) is a first-order moving average model, i.e. MA(1) y^(t) ~ error(t-1)
  * A moving-average model is conceptually a linear regression of the current value of the series against current and previous (observed) white noise error terms.
  * The method is suitable for univariate time series ```without trend``` and ```without seasonal components```.

**Autoregressive Moving Average (ARMA)**
  * The ARMA method seeks to model the next step in the sequence as a linear function of the **observations** and **resiudal errors** at prior time steps.
  * It combines both Autoregression (AR) and Moving Average (MA) models.
  * The notation: ARMA(p, q). An ARIMA model can be used to develop AR or MA models. For example, ARMA(1,0,1) is y^(t) ~ y(t-1), error(t-1)
  * The method is suitable for univariate time series ```without trend``` and ```without seasonal components```.


**Autoregressive Integrated Moving Average (ARIMA)**
  * The ARIMA method seeks to model the next step in the sequence as a linear function of the **differenced observations** and **residual errors** at prior time steps.
  * It combines both Autoregression (AR) and Moving Average (MA) models as well as a differencing pre-processing step of the sequence to make the sequence stationary, called integration (I).
  * In ARIMA, AR filter is responsible for finding the **long term** trends, Integration filter is responsible for **stochastic** trend, and MA filter is responsible for **short term** trends. 
  * The notation: ARIMA(p, d, q). An ARIMA model can also be used to develop AR, MA, and ARMA models. For example, ARIMA(1,1,1) is [y(t)-y(t-1)] ~ [y(t-1)-y(t-2)], error(t-1)
  * The method is suitable for univariate time series ```with trend``` and ```without seasonal components```.

**Seasonal Autoregressive Integrated Moving-Average (SARIMA)**
  * The Seasonal ARIMA method seeks to model the next step in the sequence as a linear function of the **differenced observations**,**residual errors**, **differenced seasonal observations**, and **seasonal errors** at prior time steps.
  * It combines the ARIMA model with the ability to perform the same autoregression, differencing, and moving average modeling at the seasonal level.
  * The notation for the model involves specifying the order for the AR(p), I(d), and MA(q) models as parameters to an ARIMA function and AR(P), I(D), MA(Q) and m parameters at the seasonal level, e.g. SARIMA(p, d, q)(P, D, Q)m where “m” is the number of time steps in each season (the seasonal period). A SARIMA model can be used to develop AR, MA, ARMA and ARIMA models.
  * The (P,D,Q,s) order of the seasonal component of the model for the AR parameters, differences, MA parameters, and periodicity. s is an integer giving the periodicity (number of periods in season), often it is 4 for quarterly data or 12 for monthly data. 
  * The method is suitable for univariate time series ```with trend``` and ```with seasonal components```.

**Seasonal Autoregressive Integrated Moving-Average with Exogenous Regressors (SARIMAX)**
  * The SARIMAX is an extension of the SARIMA model that also includes the modeling of exogenous variables.
  * Exogenous variables are also called covariates and can be thought of as parallel input sequences that have observations at the same time steps as the original series. The primary series may be referred to as endogenous data to contrast it from the exogenous sequence(s). The observations for exogenous variables are included in the model directly at each time step and are not modeled in the same way as the primary endogenous sequence (e.g. as an AR, MA, etc. process).
  * The SARIMAX method can also be used to model the subsumed models with exogenous variables, such as ARX, MAX, ARMAX, and ARIMAX.
  * The method is suitable for univariate time series ```with trend``` and/or ```with seasonal components``` and ```with exogenous variables```.

**Vector Autoregression (VAR)**
  * VAR is a stochastic process model used to capture the linear interdependencies among multiple time series. All variables in a VAR enter the model in the same way: each variable has an equation explaining its evolution based on its own lagged values, the lagged values of the other model variables, and an error term. 
  * VAR modeling does not require as much knowledge about the forces influencing a variable as do structural models with simultaneous equations: The only prior knowledge required is a list of variables which can be hypothesized to affect each other intertemporally.
  * The VAR method seeks to model the next step in each time series using an AR model. It is the generalization of AR to multiple parallel time series, e.g. multivariate time series.
  * The notation: VAR(p).
  * The method is suitable for multivariate time series ```without trend``` and ```without seasonal components```.
  * two-variable example: 
    - y1(t) = c1 + a11*y1(t-1) + a12*y2(t-1) + e1(t)
    - y2(t) = c2 + a21*y1(t-1) + a22*y2(t-1) + e2(t) 

**Vector Autoregression Moving-Average (VARMA)**
  * The VARMA method models the next step in each time series using an ARMA model. It is the generalization of ARMA to multiple parallel time series, e.g. multivariate time series.
  * The notation: VARMA(p, q). A VARMA model can also be used to develop VAR or VMA models.
  * The method is suitable for ```multivariate``` time series ```without trend``` and ```without seasonal components```.

**Vector Autoregression Moving-Average with Exogenous Regressors (VARMAX)**
  * The VARMAX is an extension of the VARMA model that also includes the modeling of exogenous variables. It is a multivariate version of the ARMAX method.
  * The observations for exogenous variables are included in the model directly at each time step and are not modeled in the same way as the primary endogenous sequence (e.g. as an AR, MA, etc. process).
  * The VARMAX method can also be used to model the subsumed models with exogenous variables, such as VARX and VMAX.
  * The method is suitable for ```multivariate``` time series ```without trend``` and ```without seasonal components``` and ```with exogenous variables```.

**Simple Exponential Smoothing (SES)**
  * The SES method seeks to model the next time step as an exponentially weighted linear function of observations at prior time steps.
  * The method is suitable for ```univariate``` time series ```without trend``` and ```without seasonal components```.
  * Exponential smoothing is a rule of thumb technique for smoothing time series data using the exponential window function. Whereas in the simple moving average the past observations are weighted equally, exponential functions are used to assign exponentially decreasing weights over time.
  * Exponential smoothing is one of many window functions commonly applied to smooth data in signal processing, acting as low-pass filters to remove high-frequency noise. 
  * simple example:
    - s(t) = a*x(t) + (1-a)*s(t-1)

**Holt Winter’s Exponential Smoothing (HWES)**
  * The HWES also called the Triple Exponential Smoothing method seeks to model the next time step as an exponentially weighted linear function of observations at prior time steps, taking trends and seasonality into account.
  * The method is suitable for ```univariate``` time series ```with trend``` and/or ```with seasonal components```.




**Moving average in statistics**
In statistics, a moving average (rolling average or running average) is a calculation to analyze data points by creating a series of averages of different subsets of the full data set. It is also a type of finite impulse response filter. Variations include: simple, and cumulative, or weighted forms.

Given a series of numbers and a fixed subset size, the first element of the moving average is obtained by taking the average of the initial fixed subset of the number series. Then the subset is modified by **"shifting forward"**; that is, excluding the first number of the series and including the next value in the subset.

A moving average is commonly used with time series data to **smooth out** short-term fluctuations and highlight longer-term trends or cycles. For example, it is often used in technical analysis of financial data, like stock prices, returns or trading volumes. Mathematically, a moving average is a type of **convolution** and so it can be viewed as an example of a **low-pass filter** used in signal processing. When used with non-time series data, a moving average filters higher frequency components without any specific connection to time, although typically some kind of ordering is implied. Viewed simplistically it can be regarded as smoothing the data.


