'''
Count the number of prime numbers less than a non-negative number, n.
'''
import sys

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        primeStatus = [True] * n
        primeStatus[0] = primeStatus[1] = False
        
        for x in xrange(2,n):
            if primeStatus[x] is True:     # if it's prime, mark all its products as NOT prime
                for y in xrange(x, (n-1)//x + 1):
                    primeStatus[x*y] = False
                    
        print [x for x in xrange(0,n) if primeStatus[x] is True]
        return sum(primeStatus)


if __name__ == '__main__':
    st = Solution()
    print sys.argv
    if len(sys.argv) > 1:
        print st.countPrimes(int(sys.argv[1]))
    else:
        print "Please input n for function to work"
    
