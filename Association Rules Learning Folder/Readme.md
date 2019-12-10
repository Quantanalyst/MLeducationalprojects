## Association Rule

Association Rules is one of the very important concepts of machine learning being used in market basket analysis. Rules consist of an antecedent and a consequent, both of which are a list of items. Note that implication here is **co-occurrence** and not causality. For a given rule, itemset is the list of all the items in the antecedent and the consequent.

![Association Rule](Rule.png)









* What is the difference b/w **Association Rule** and **Collaborative Filtering**?
  * Rules do not tie back a users’ different transactions __over time__ to identify relationships. List of items with unique transaction IDs (**from all users**) are studied as one group. **This is helpful in placement of products on aisles**. 
  * On the other hand, collaborative filtering ties back all transactions corresponding to a user ID to identify similarity between **users’ preferences**. **This is helpful in recommending items on e-commerce websites, recommending songs on spotify, etc**.



P.S. Rules do not extract an individual’s preference, rather find relationships between set of elements of every distinct transaction. This is what makes them different from collaborative filtering.
