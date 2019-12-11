# Thompson Sampling

There are many empirical evidence that Thompson Sampling performs better than UCB algorihm. 

Algorithm:

![Thompson Sampling](Thompson_Sampling_Slide.png)

What are the differences b/w Thompson Sampling and UCB?
1. UCB is deterministic but Thompson is probabilistic. It means that in UCB, the outcome of the algorithm, i.e. which bandit to play, is constant as the bandit with maximum upper bound is determined. On the other hand, in Thompson Sampling, the outcome of Beta distribution, i.e. which bandit to play, changes if we repeat the steps.
2. UCB requires update at every round; otherwise it won't change and it might get stuck. On the other hand, Thompson Sampling can accomodate delayed feedback. 
3. There are empirical evidences that Thompson Sampling outperforms UCB algorithm. 



P.S. Keep in mind that Beta distribution is the conjugate prior of the Bernoulli distribution. 
