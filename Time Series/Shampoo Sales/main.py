
"""
Title: Shampoo Sales

@author: Saeed Mohajeryami, PhD

"""

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error


def parser(x):
	return pd.datetime.strptime('200'+x, '%Y-%m')

dataset = pd.read_csv('shampoo.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(dataset.head())
dataset.plot()
plt.show()

# From plot, We can see that the Shampoo Sales dataset has a clear trend.
# This suggests that the time series is not stationary and will require 
# differencing to make it stationary, at least a difference order of 1.

# Let's take a look at autocorrelation plot
pd.plotting.autocorrelation_plot(dataset)
# Running the example, we can see that there is a positive correlation with the
# first 10-to-12 lags that is perhaps significant for the first 5 lags.
# A good starting point for the AR parameter of the model may be 5.

# ARIMA algorithm
# An ARIMA model can be created using the statsmodels library as follows:
# 1. Define the model by calling ARIMA() and passing in the p, d, and q parameters.
# 2. The model is prepared on the training data by calling the fit() function.
# 3. Predictions can be made by calling the predict() function and specifying
# the index of the time or times to be predicted.

# First, we fit an ARIMA(5,1,0) model. This sets the lag value to 5 for 
# autoregression, uses a difference order of 1 to make the time series stationary,
# and uses a moving average model of 0.

# fit model
model = ARIMA(dataset, order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())
# Running the example prints a summary of the fit model. This summarizes the
# coefficient values used as well as the skill of the fit on the on the in-sample
# observations.

# plot residual errors
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
plt.show()
# First, we get a line plot of the residual errors, suggesting that there may
# still be some trend information not captured by the model.

residuals.plot(kind='kde')
plt.show()
# Next, we get a density plot of the residual error values, suggesting the errors
# are Gaussian, but may not be centered on zero.

print(residuals.describe())
# The distribution of the residual errors is displayed. The results show that 
# indeed there is a bias in the prediction (a non-zero mean in the residuals).

X = dataset.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(5,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
mse = mean_squared_error(test, predictions)
mae = mean_absolute_error(test, predictions)
mean = test.mean()
print(f'Test MSE: {mse} \nTest MAE: {mae} \nError Percent: {round(mae*100/mean,2)}%')
# plot
plt.plot(test)
plt.plot(predictions, color='red')
plt.show()
