# Reinforcement Learning


Reinforcement Learning is a branch of Machine Learning, also called **Online Learning**. It is used to solve interacting problems where the data observed up to time t is considered to decide which action to take at time t + 1. It is also used for Artificial Intelligence when training machines to perform tasks such as walking. Desired outcomes provide the AI with reward, undesired with punishment. Machines learn through trial and error.

One of the popular problems in this space is "multi-armed bandit problem". Bandit is a slot machine in casinos. Assuming there are multiple bandit machines with different reward distribution, the problem is which one is better to pick without knowing the underlying distributions. The solution is to explore & exploit. However, the rate of exploration and exploitation must be decided in a way to maximize the profit. There are many modern renditions of "multi-armed bandit problem" which have similar nature. For example, advertising different ads and explore which one leads to higher clicks and exploit it. 

The online advertisement version of Multi-Armed Bandit Problem:
  * We have d arms. In this example, arms are ads that we display to users each time they connect to a web page.
  * Each time a user connects to this webpage, that makes a round.
  * At each round n, we choose one ad to display to the user.
  * At each round n, ad i gives reward ri(n):{0,1}, it is 1 if the user clicked on the ad i, 0 if the user didn't.
  * Our goal is to maximize the total reward we get over many rounds.

Bandit algorithms for balancing exploration vs. exploitation problem:
  * Epsilon greedy
  * Upper Confidence Bound (UCB)
  * Thompson Sampling



P.S. Reinforcement learning is different from A/B testing. A/B testing is only for exploration. So, during the A/B testing, you're not concerned about exploitation. When the exploration is finalized, then the A/B test result will be exploited. In other words, in A/B testing, the exploration and exploitation is done separately, which incur a lot of cost. On the other hand, reinforcement learning is seeking to optimize exploration and exploitation at the same time and combine the two together. 
