class Solution:
    # @return an integer
    def reverse(self, x):
        if x/10 == 0:
            return x
            
        curNum = x
        flag = 1
        if x < 0:
            curNum = 0 - curNum
            flag = -1
            
        digits = list()
        
        while curNum != 0:
            resultDivide = curNum / 10
            resultResidue = curNum % 10
            curNum = resultDivide
            digits.append(resultResidue)

        result = 0
        i = 0
        times = len(digits) - 1
        while i < len(digits):
            result = result + digits[i] * (10**times)
            times = times - 1
            i = i + 1
            
        if result > 0x7fffffff:
            return 0
        
        return result*flag
            