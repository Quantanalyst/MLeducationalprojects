## Recurrent Neural Network (RNN)

Algorithm:
  * Importing the dataset
  * Feature scaling: It is recommended to use Normalization rather than Standardization for RNN since we are going to use Sigmoid activation function. 
  * creating a structure with X time steps and one output (X is the number of timesteps we want to look in the past to be able to predict one future output. If we determine the X wrongly, it might lead to overfit or underfit). 
  * Reshape: It is used to make a 3D tensor (batchsize, timestep, input_dim). Input dimension is the number of indicators we want to use for the prediction. RNN allows multiple indicators to be used for the purpose of training simultaneously.
  * Building the RNN model:
    * Adding the first LSTM layer and Dropout Regularization
    * Adding more LSTM layers, if needed
    * Adding the output layer
  * Compiling the RNN
  * Fitting the RNN to the training set
  * Making the prediction




## How to improve the RNN model:
  * Getting more training data: we trained our model on the past 5 years of the Google Stock Price but it would be even better to train it on the past 10 years.
  * Increasing the number of timesteps: the model remembered the stock prices from the 60 previous financial days to predict the stock price of the next day. That’s because we chose a number of 60 timesteps (3 months). You could try to increase the number of timesteps, by choosing for example 120 timesteps (6 months).
  * Adding some other indicators: if you have the financial instinct that the stock price of some other companies might be correlated to the one of Google, you could add this other stock price as a new indicator in the training data.
  * Adding more LSTM layers: we built a RNN with four LSTM layers but you could try with even more.
Adding more neurones in the LSTM layers: we highlighted the fact that we needed a high number of neurones in the LSTM layers to respond better to the complexity of the problem and we chose to include 50 neurones in each of our 4 LSTM layers. You could try an architecture with even more neurones in each of the 4 (or more) LSTM layers.
