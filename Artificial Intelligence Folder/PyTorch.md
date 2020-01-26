# PyTorch

**Introduction:**\
It’s a Python based scientific computing package targeted at two sets of audiences:
  * A replacement for NumPy to use the power of GPUs
  * Deep learning research platform that provides maximum flexibility and speed

**Advantages of PyTorch:**\
  * Interactively debugging PyTorch. Many users who have used both frameworks would argue that makes pytorch significantly easier to debug and visualize.
  * Clean support for dynamic graphs
  * Organizational backing from Facebook
  * Blend of high level and low level APIs

**Disadvantages of PyTorch:**\
  * Much less mature than alternatives
  * Limited references / resources outside of the official documentation

**PyTorch and Numpy**\
These two are very similar, one is created to be used with GPU and the other with CPU. 
Conversion b/w the two: 
  * torch.from_numpy(): from numpy to tensor
  * numpy(): from tensor to numpy


**Basic Math with Pytorch**\
  * Resize: view()
  * Addition: torch.add(a,b) = a + b (a and b are tensors)
  * Subtraction: a.sub(b) = a - b
  * Element wise multiplication: torch.mul(a,b) = a * b
  * Element wise division: torch.div(a,b) = a / b
  * Mean: a.mean()
  * Standart Deviation (std): a.std()

**Variables**\
It accumulates gradients. It is necessary to use it for deep learning as we need these gradients for backpropagation. Difference between variables and tensor is variable accumulates gradients. We can make math operations with variables, too. In order to make backward propagation we need variables. 
