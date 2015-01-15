class Solution:
    # @param n, an integer
    # @return an integer
    def calcMethods(self,num2s,totalN):
        #num2S = 0, method = 1
        #num2S = 1, method = (totalN-1)/1
        #num2S = 2, method = (totalN-2)(totalN-3)/2*1
        #num2S = 3, method = (totalN-3)(totalN-4)(totalN-5)/3*2*1
        if num2s == 0:
            return totalN
        
        toDiv = 1
        div = 1
        for i in range(1,num2s+1):
            toDiv = toDiv *(totalN - (2*num2s-i))
            div = div * i

        return toDiv/div
    
    def climbStairs(self, n):
        # n = 1 : 1 way: (1)
        # n = 2 : 2 ways: (1,1)  or (2)
        # n = 3 : 3 ways: (1,1,1) or (1,2) or (2,1)
        # n = 4 : 5 ways: (1,1,1,1) or (2,1,1) or (1,2,1) or (1,1,2) or (2,2)
        # n/2 = max2times
        # total n, if there is one 2, total elements would be n-1, so total methonds would be : n-1
        # if there are two 2, total elements would be n-2, methods to put these two 2s in n-2 locations is : (n-2)(n-3)/2
        # if there are three 2, total elements would be n-3, methods to put these three 2s in n-3 locations is : (n-3)(n-4)(n-5)/3*2 
        
        # for 4, when only 1s, methond: 1
        # when only one 2, method: n-1 = 3
        # when two 2s, method: 1 
        # total: 1+3+1 = 5
        
        # for 5, when only 1s, i=0, methond: 1
        # when only one 2, methond: n-1 = 4
        # when two 2s, method: (n-2)(n-3)/2 = 3
        # total: 1+4+3 = 8
        
        # for 6: 1 + (n-1)/1 + (n-2)(n-3)/2 +(n-3)(n-4)(n-5)/3*2 =  1 + 5 + 6 + 1 = 13
        # (1,1,1,1,1,1) 
        # (2,1,1,1,1)(1,2,1,1,1)(1,1,2,1,1)(1,1,1,2,1)(1,1,1,1,2)
        # (1,1,2,2)(1,2,1,2)(2,1,1,2)(2,2,1,1)(1,2,2,1)(2,1,2,1)
        # (2,2,2)
        max2num = n / 2
        res = n % 2
        method = 1
        
        for i in range(1,n/2+1):
            # total spots: n-i , total 2s: i
            method = method + self.calcMethods(i,n)
        
        return method