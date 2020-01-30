
"""
Title: Explore classical time-series forecasting models

@author: Saeed Mohajeryami, PhD

"""
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.tsa.statespace.varmax import VARMAX
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from random import random #gives a random value in the interval [0,1]


## ---------------------- Autoregression (AR) -------------------------------

# contrived dataset
data = [x + random() for x in range(1, 100)]

plt.plot(data)
plt.show()

# fit model
model = AR(data)   # AR(1) y^(t) ~ y(t-1)
model_fit = model.fit()

# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)

## ---------------------- Moving Average (MA) -------------------------------

# fit model
model = ARMA(data, order=(0, 1))  # MA(1) y^(t) ~ error(t-1)
model_fit = model.fit(disp=False)

# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)

## ---------------- Autoregressive Moving Average (ARMA) --------------------

# contrived dataset
data = [random() for x in range(1, 100)]
# Note: previous data doesn't work here.

plt.plot(data)
plt.show()

# fit model
model = ARMA(data, order=(2, 1))  # AR(2), MA(1) y^(t) ~ y(t-1), y(t-2), error(t-1)
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)

## --------- Autoregressive Integrated Moving Average (ARIMA) -----------------

# contrived dataset
data = [x + random() for x in range(1, 100)]

plt.plot(data)
plt.show()

# fit model
model = ARIMA(data, order=(1, 1, 1)) # [y(t)-y(t-1)] ~ [y(t-1)-y(t-2)], error(t-1)
# ARIMA (1,1,1) --> Delta(y(t)) ~ Delta(y(t-1)), error(t-1)
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data), typ='levels')
print(yhat)

## ----- Seasonal Autoregressive Integrated Moving Average (SARIMA) ----------

model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 1))
# seasonal order: The (P,D,Q,s) order of the seasonal component of the model for 
# the AR parameters, differences, MA parameters, and periodicity. d must be an 
# integer indicating the integration order of the process, while p and q may
#  either be an integers indicating the AR and MA orders (so that all lags up to
# those orders are included) or else iterables giving specific AR and / or MA lags
# to include. s is an integer giving the periodicity (number of periods in season),
# often it is 4 for quarterly data or 12 for monthly data. Default is no seasonal
# effect.
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)

## ------------Seasonal ARIMA with Exogenous Regressor (SARIMAX) --------------

# contrived dataset
data1 = [x + random() for x in range(1, 100)]
data2 = [x + random() for x in range(101, 200)]
# fit model
model = SARIMAX(data1, exog=data2, order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
model_fit = model.fit(disp=False)
# make prediction
exog2 = [200 + random()]
yhat = model_fit.predict(len(data1), len(data1), exog=[exog2])
print(yhat)

# ---------------- Vector Autoregression (VAR) -----------------------------

# contrived dataset with dependency
data = list()
for i in range(100):
    v1 = i + random()
    v2 = v1 + random()
    row = [v1, v2]
    data.append(row)
# fit model
model = VAR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.forecast(model_fit.y, steps=1)
print(yhat)

# ----------- Vector Autoregression Moving Average (VARMA) -----------------

# contrived dataset with dependency
data = list()
for i in range(100):
    v1 = random()
    v2 = v1 + random()
    row = [v1, v2]
    data.append(row)
# fit model
model = VARMAX(data, order=(1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.forecast()
print(yhat)

# -------------- VARMA with Exogenous Regressors (VARMAX) --------------------

# contrived dataset with dependency
data = list()
for i in range(100):
    v1 = random()
    v2 = v1 + random()
    row = [v1, v2]
    data.append(row)
data_exog = [x + random() for x in range(100)]
# fit model
model = VARMAX(data, exog=data_exog, order=(1, 1))
model_fit = model.fit(disp=False)
# make prediction
data_exog2 = [[100]]
yhat = model_fit.forecast(exog=data_exog2)
print(yhat)

# -------------------- Simple Exponential Smoothing (SES) --------------------

# contrived dataset
data = [x + random() for x in range(1, 100)]

plt.plot(data)
plt.show()

# fit model
model = SimpleExpSmoothing(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)

# ------------ Holt Winter’s Exponential Smoothing (HWES) -------------------

# contrived dataset
data = [x + random() for x in range(1, 100)]
# fit model
model = ExponentialSmoothing(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)