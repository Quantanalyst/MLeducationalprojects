# Epsilon Greedy

A common approach to balancing the exploitation-exploration tradeoff is the epilson- or e-greedy algorithm. After an initial period of exploration (for example 1000 trials), the algorithm greedily exploits the best option k, and explore the variant space e percent of the time. For example, if we set e=0.05, the algorithm will exploit the best variant 95% of the time and will explore random alternatives 5% of the time. This is actually quite effective in practice, but as we’ll come to see it can under explore the variant space before exploiting what it estimates to be the strongest variant. This means that e-greedy can get stuck exploiting a suboptimal variant. 

Algorithm:
Assuming you have k bandits. As you play the machines, you keep track of the average payout of each machine. Then, you select the machine with the highest current average payout with probability = (1 – epsilon) + (epsilon / k) where epsilon is a small value like 0.10. And you select machines that don’t have the highest current payout average with probability = epsilon / k.

