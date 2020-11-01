import numpy as np
import scipy.stats

def testStatistic( data, mu ) : 
  # Your code to compute the testStatistic that is described
  # in the text on the right should be calculated here
  
  
def pvalue( data, mu ) :
  T = testStatistic(data, mu )
  # You should add code here that uses the T value that is returned from 
  # testStatistic to determine the p-value for the hypothesis test.
  

# The code from here should not need to be modified
data = np.array([24.80, 23.86, 24.98, 22.73, 23.62, 24.21, 24.78, 24.23])
print("The null hypothesis is that the data is a set of samples from a distribution")
print("with an expectation of 23")
print("The alternative hypothsis is that the data is a set of samples from a distribution")
print("with an expectation that is greater than 23")
print("The p-value for this hypothesis test is", pvalue(data, 23) )
