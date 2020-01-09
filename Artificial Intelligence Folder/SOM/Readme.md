## Self Organizing Maps (SOMs)

Kohonen Self Organising Feature Maps, or SOMs provide a way of representing multidimensional data in much lower dimensional spaces - usually one or two dimensions. The Kohonen technique creates a network that stores information in such a way that any topological relationships within the training set are maintained.

One of the most interesting aspects of SOMs is that they learn to classify data without supervision. Another application, SOMs are commonly used as visualization aids. They can make it easy for us humans to see relationships between vast amounts of data.

Algorithm:
  * Each node's weights are initialized.
  * A vector is chosen at random from the set of training data and presented to the lattice.
  * Every node is examined to calculate which one's weights are most like the input vector. The winning node is commonly known as the Best Matching Unit (BMU).
  * The radius of the neighbourhood of the BMU is now calculated. This is a value that starts large, typically set to the 'radius' of the lattice,  but diminishes each time-step. Any nodes found within this radius are deemed to be inside the BMU's neighbourhood.
  * Each neighbouring node's (the nodes found in step 4) weights are adjusted to make them more like the input vector. The closer a node is to the BMU, the more its weights get altered.
  * Repeat step 2 for N iterations.

 
Different version of Algorithm:
  * STEP 1: we start with a dataset composed of n_features independent variables
  * STEP 2: we create a grid composed of nodes, each one having a weight vectors of n_features elements
  * STEP 3: randomly initialize the values of the weight vectors to small numbers close to 0 (but not 0)
  * STEP 4: select one random observation point from the dataset
  * STEP 5: compute the Euclidean distances from this point to the different neuorons in the network
  * STEP 6: select the neuron that has the minimum distance to the point. This neuron is called the winning node (BMU)
  * STEP 7: update the weights of the winning node to move it closer to the point
  * STEP 8: using a Gaussian neighborhood function of mean the winning node. Also update the weights of the winning node neighbors to move them closer to the point. The neighborhood radius is the sigma in the Gaussian function.
  * STEP 9: Repeat steps 1 to 5 and update the weights after each observation (Reinforcement learning) or after a batch of observation (Batch Learning), until the network converges to a point where the neighborhood stops decreasing. 


Tools:
  * MiniSom 1.0 


Important to know:
  * SOMs retain topology of the input
  * SOMs reveal correlations that are not easily identified
  * SOMs classify data without supervision
  * No target vector --> no backpropagation
  * No lateral connections between output nodes
