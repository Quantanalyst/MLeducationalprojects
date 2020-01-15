## Auto Encoders

Algorithm:
  * STEP 1: We start with an array where the lines (the observation) corrospond to the users and the columns (the features) corrosponds to the movies. Each cell (u,i) contains the rating (from 1 to 5, 0 if no rating) of the movie i by the user u.
  * STEP 2: The first user goes into the network. The input vector x = (r1, r2, ..., rm) contains all its ratings for all the movies.
  * STEP 3: The input vector x is encoded into a vector z of lower dimensions by a mapping function f (e.g. sigmoid function): z = f(Wx+b) where W is the vector of input weights and b the bias
  * STEP 4: z is then decoded into the output vector y of same dimensions as x, aiming to replicate the input vector x. 
  * STEP 5: The reconstruction error d(x,y) = ||x-y|| is computed. The goal is to minimize it.
  * STEP 6: Back Propagation: from right to left, the error is back-propagated. The weights are updated according to how much they are responsible for the error. The learning rate decideds by how much we update the weights.
  * STEP 7: Repeat steps 1 to 6 and update the weights after each observation (Reinforcement Learning) or repeat them and update the weights only after a batch of observations (Batch Learning). 
  * STEP 8: When the whole training set passed through the ANN. that makes an epoch. Redo more epochs.

Different Auto Encoders:
  * Overcomplete Auto Encoders: When the number of hidden layers is higher than the number of input layers. This AE is useful for feature extraction. The problem with this AE is overfitting (cheating).
  * Sparse Auto Encoders: Same as Overcomplte AE, but it introduces a regularization technique. The penalty function forces the AE to use only a few hidden nodes for each pass. It penalizes high number of hidden nodes. In another way, the regularization forces AE to act as a not overcomplete network for each pass. 
  * Denoising Auto Encoders: Same as overcomplete AE, however, it does a simple trick. It forces randomly some elements of inputs to zero during each epoch. Introducing this noise to the system prevents the network from memorizing the inputs and overfitting. 
  * Contractive Auto Encoders: Same as overcomplete AE. It introduces a regularization function into the loss function to prevent overfitting. 
  * Stacked Auto Encoders: Auto encoders with more than one hidden layers. It has been shown that sometimes stacked AE supercedes even Deep Belief Network (DBN)
  * Deep Auto Encoders
