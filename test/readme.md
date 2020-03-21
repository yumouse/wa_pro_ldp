#### 5. PrivKVM and PrivKVM+ based on total cost

We define the cost of algorithm as two parts, the accuracy cost and the communication cost. Accuracy cost is the difference between the mean start vector and the origin mean vector. Communication cost represents the iteration times in the algorithm. Smaller cost means better result.

We could observe from the figure that while epsilon increases,  cost on PrivmKVM is decreasing.

However, our result about PrivmKVM  Plus is different from the paper's. Their PrivmKVM plus algorithm's cost is smaller than normal privmKVM algorithm in any epsilon  and it's linear. Our privmKVMplus' cost function is nonlinear. The cost in some epsilon  are smaller  than the privmKVM's but some are not. (后续应该说明为什么我们的privkvm plus的结果和人家的实验结果不一样，但我不知道咋说明)

#### 6.  PrivKVM and PrivKVM+ based on user number

We use synthetic data of different user-numbers and plot the MSE. PrivKVM-plus outperforms the PrivKVM which has six iterations.  We could see from figure that the log(MSE) is decreasing with the increasing of  user-numbers. 

