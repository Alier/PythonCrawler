class Solution(object):
    counted = {}
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.counted:
            return self.counted[n]
        
        if n <= 1:
            return n
            
        minCounts = n
        
        floor = int(math.floor(math.sqrt(n)))
        
        for i in range(1, floor+1):
            minTemp = 1 + self.numSquares( n - i*i )
            if minTemp < minCounts:
                minCounts = minTemp
        
        self.counted[n] = minCounts
        return minCounts
