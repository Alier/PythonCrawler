'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.
'''
class Solution(object):
    def maxAsElement(self, a):
        if a <= 4:
            return a
        return self.integerBreak(a)
    
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1

        a, b = divmod(n, 2)
        if b == 0:
            return max(self.maxAsElement(a) * self.maxAsElement(a), self.maxAsElement(a-1) * self.maxAsElement(a+1))
        else:
            return max(self.maxAsElement(a) * self.maxAsElement(a+1), self.maxAsElement(a-1) * self.maxAsElement(a+2))


        
        


            
