
"""
Created on Tue Jan 28 22:30:29 2020

@author: Saeed Mohajeryami, PhD

"""

# Importing libraries
import os
import warnings
warnings.filterwarnings('ignore')
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight') 
from pylab import rcParams
from plotly import tools
import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.figure_factory as ff
import statsmodels.api as sm
from numpy.random import normal, seed
from scipy.stats import norm
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima_model import ARIMA
import math
from sklearn.metrics import mean_squared_error
print(os.listdir("/home/saeed/On Github/ML-AI Projects/MLeducationalprojects/Time Series/input"))


# import data
google = pd.read_csv('/home/saeed/On Github/ML-AI Projects/MLeducationalprojects/Time Series/input/stock-time-series-20050101-to-20171231/GOOGL_2006-01-01_to_2018-01-01.csv', index_col='Date', parse_dates=['Date'])
google.head()

humidity = pd.read_csv('/home/saeed/On Github/ML-AI Projects/MLeducationalprojects/Time Series/input/historical-hourly-weather-data/humidity.csv', index_col='datetime', parse_dates=['datetime'])
humidity.tail()

# address missing value problem
humidity = humidity.iloc[1:] # the first row is empty, so better to get rid of it.
humidity = humidity.fillna(method='ffill') # fillna() method with ffill parameter which propagates last valid observation to fill gaps
humidity.head()

# visualizing the data
humidity["Kansas City"].asfreq('M').plot() # asfreq method is used to convert a time series to a specified frequency. Here it is monthly frequency.
plt.title('Humidity in Kansas City over time(Monthly frequency)')
plt.show()

google['2008':'2010'].plot(subplots=True, figsize=(10,12))
plt.title('Google stock attributes from 2008 to 2010')
plt.savefig('stocks.png')
plt.show()

# Upsampling vs. Downsampling
# Let's use pressure data to demonstrate this
pressure = pd.read_csv('/home/saeed/On Github/ML-AI Projects/MLeducationalprojects/Time Series/input/historical-hourly-weather-data/pressure.csv', index_col='datetime', parse_dates=['datetime'])
pressure.tail()

pressure = pressure.iloc[1:]
pressure = pressure.fillna(method='ffill')
pressure = pressure.fillna(method='bfill')
# First, we used ffill parameter which propagates last valid observation to fill
# gaps. Then we use bfill to propogate next valid observation to fill gaps.

