## Support Vector Machine (SVM)

SVM algorithms use a set of mathematical functions that are defined as the kernel. The function of kernel is to take data as input and transform it into the required form. Different SVM algorithms use different types of kernel functions, e.g. **linear**, **nonlinear**, **polynomial**, **radial basis function (RBF)**, and **sigmoid**.

**Kernel:** In ML, a “kernel” is usually used to refer to the kernel trick, a method of using a linear classifier to solve a non-linear problem. It entails transforming linearly inseparable data to linearly separable ones. The kernel function is what is applied on each data instance to map the original non-linear observations into a higher-dimensional space in which they become separable.

What makes SVM special?
  * Support vectors. Support vectors are instances that are very extreme. They are the closest members to the opposite class and they would be used to define the separator that classify our samples into different classes. 
  * Moreover, another special property of SVM is kernels, which gives you a lot of flexibility. For example, if you use linear kernel, your classifier becomes linear and if you use nonlinear kernel like radial basis function, it become nonlinear. 


-- Another good explanation:
  * **Mathematical definition:** K(x, y) = <f(x), f(y)>. Here K is the kernel function, x, y are n dimensional inputs. f is a map from n-dimension to m-dimension space. < x,y> denotes the dot product. usually m is much larger than n.
  * **Intuition:** normally calculating <f(x), f(y)> requires us to calculate f(x), f(y) first, and then do the dot product. These two computation steps can be quite expensive as they involve manipulations in m dimensional space, where m can be a large number. But after all the trouble of going to the high dimensional space, the result of the dot product is really a scalar: we come back to one-dimensional space again! Now, the question we have is: do we really need to go through all the trouble to get this one number? do we really have to go to the m-dimensional space? The answer is no, if you find a clever kernel. In other words, We don’t need to know the mapping function itself, as long as we know the Kernel function ; Kernel Trick. 
  
  
  Kernels:
  
![KernelFunctions](Kernels.png)


Tuning Parameter:
One of the popular Kernels in RBF (very similar to Guassian Kernel). One of our tuning parameters for RBF is gamma. RBF outcome depends on the Euclidean distance between two points. So, if two vectors are closer then the RBF value is small. As the variance is always positive, this means for closer vectors, the RBF kernel is widely spread than the farther vectors. When gamma parameter is high the value of kernel function will be less, even for two close by samples, and, this may cause complicated decision boundary or give rise to over-fitting. 

![RBF Gamma](gammatuning.png)


Some notes:
  * Polynomial Kernel is popular in image processing
  * RBF Kernel is a general-purpose kernel and is used when there is no prior knowledge about the data
  * Hyperbolic Tangent Kernel is used in NN
  * Sigmoid Kernel can be used as a proxy for neural networks
  * Linear Splines Kernel in one dimension is useful when dealing with large sparse data vectors. It is often used in text categorization. The splines kernel also performs well in regression problems.
