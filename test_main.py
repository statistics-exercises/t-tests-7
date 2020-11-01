import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) :
        for n in range(1,21) :
           mu = -10 +n
           bessel = 20*n / (20*n - 1)
           samples = np.random.normal(mu, 1.0, size=20*n )
           samplemean = sum(samples) / (20*n)
           sigma2 = bessel*( sum(samples*samples) / (20*n) - samplemean*samplemean )
           stat = ( samplemean - mu ) / np.sqrt(sigma2/(20*n))
           self.assertTrue( np.abs( stat - testStatistic( samples, mu) )<1e-7, "your fucntion to calculate the test statistic is not working correctly" )
           
    def test_pvalue(self) : 
        for n in range(2,21) :
           mu, sigma = 10 + n, 0.1*n
           samples = np.random.normal(mu, sigma, size=n )
           stat = testStatistic( samples, mu )
           pval = 1-scipy.stats.t.cdf(stat,len(samples)-1)
           self.assertTrue( np.abs( pval - pvalue( samples, mu ) )<1e-7, "Your function to calculate the pvalue is not working correctly" )

        stat = testStatistic( data, 23 )
        pval = 1-scipy.stats.t.cdf(stat,len(data)-1)
        self.assertTrue( np.abs( pval - pvalue( data, 23 ) )<1e-7, "Your function to calculate the pvalue is not working correctly" )
