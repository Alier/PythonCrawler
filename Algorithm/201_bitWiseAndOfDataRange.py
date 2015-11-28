import math

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
           
        if m == n:
            return m
           
        floorLowPow = math.floor(math.log(m, 2))
        floorHighPow = math.floor(math.log(n, 2))
            
        if floorHighPow - floorLowPow >= 1:
            return 0
        
        highResult = int(math.pow(2,floorLowPow))
        result = highResult + self.rangeBitwiseAnd(m-highResult, n-highResult)
        
        return result
        
        
st = Solution()
print st.rangeBitwiseAnd(6,7)