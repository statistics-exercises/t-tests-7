# One-tailed t-tests II

Lets do one more of these simple tests for completeness.  Now I would like you to __test whether the 8 points in the NumPy array called `data` are samples from a normal distribution with an expectation of 23 or if there is sufficient evidence to suppose that the expectation of the distribution is more than 23.__ 

To get you started in completing the exercise I have written two functions for you which you must complete: 
 
1. `testStatistic` - Two variables are passed to this function.  `data` is a NumPy array that contains N data points, `mu` is the value of the expectation for the distribution that is assumed under the null hypothesis.  This function should return the test statistic, which is calculated in the usual way.
2. `pvalue` - Two variables are passed to this function.  `data` is a NumPy array that contains N data points, `mu` is the value of the expectation for the distribution that is assumed under the null hypothesis.  The function calls `testStatistic` to compute the test statistic.  You should modify it so that the function returns the __p-value__ based on the value of the __statistic__.
