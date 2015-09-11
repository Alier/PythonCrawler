class Solution(object):
    #global variable, to keep the past result. It could be infinite loop if it's not happy number
    pastSingleDigitSum = []
    
    # return list of digits for n, for example:n = 23, return [2,3], n would be >= 10 already
    def getDigits(self,n):
        result = []
        
        divResult = n
        divResidue = 0
        while divResult >= 10:
            divResidue = divResult % 10       
            divResult /= 10
            if divResidue != 0:
                result.append(divResidue)
        
        result.append(divResult)
        return result
            
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        
        if n == 1:
            return True
        
        digits = self.getDigits(n)
            
        summ = 0
        for num in digits:
            summ = summ + num*num
        
        if summ == 1:
            return True
            
        #print summ
        if summ < 10:
            if summ in self.pastSingleDigitSum:
                return False
            else:
                self.pastSingleDigitSum.append(summ)

        return self.isHappy(summ)
        
st = Solution()
st.isHappy(1398)