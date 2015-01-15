class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        
        lowPattern = [0,1,1,0]
        
        #from high pos to low pos, the middle point dividing 0 and 1 on that bit is defined 2**n, n is the pos
        count = 0
        result = list()
        total = 2 ** n
        
        #from low to high
        while count < total:
            val = 0
            for i in range(0,n):
                curParam = 2 ** i
                curDigit = lowPattern[(count/curParam) % 4]
                val = val + curDigit * curParam
                
            result.append(val)
            count = count  + 1
        
        return result
        