dataset = read.csv('Ads_CTR_Optimisation.csv')

# Benchmark Random Selection
N = 10000
d = 10
ads_selected = integer(0)
total_reward = 0
for (n in 1:N) {
  ad = sample(1:10, 1)
  ads_selected = append(ads_selected, ad)
  reward = dataset[n, ad]
  total_reward = total_reward + reward
}

# Visualising the results
hist(ads_selected,
     col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected')

## Thompson Sampling Algorithm
## step 1
d = 10
N = 10000
number_of_rewards_1 = integer(d)
number_of_rewards_0 = integer(d)
ads_selected = integer(0)
total_reward = 0
reward = 0

for (n in (1:N)) 
{
  max_random = 0
  ad = 0
  for (i in (1:d))
  {
    random_beta = rbeta(n=1,
                        shape1 = number_of_rewards_1[i]+1,
                        shape2 = number_of_rewards_0[i]+1)
    if (random_beta > max_random)
    {
      max_random = random_beta
      ad = i
    }
  }
  ads_selected = append(ads_selected,ad)
  reward = dataset[n,ad]
  if (reward == 1) {
    number_of_rewards_1[ad]=number_of_rewards_1[ad]+1
  } else {
    number_of_rewards_0[ad]=number_of_rewards_0[ad]+1
  }
  total_reward = total_reward + reward
}

# Visualising the results
hist(ads_selected,
     col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected')

