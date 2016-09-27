class Solution(object):
    #return 1 if bulb i is on after n round, or 0 if it's off after n round
    def bulbStatus(self, i, n):
        if n == 1:
            return 1
        
        statusI = 1 #n = 1
        for j in range(2,n+1):
            if i%j == 0:
                statusI = 1 - statusI
            
        return statusI        
            
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        if n == 1:
            return n
            
        count = 0
        status = []
        for i in range(1, n+1):
        	status.append(self.bulbStatus(i,n))
        	count += self.bulbStatus(i,n)
            
        print status
        return count
        
X = Solution()
print X.bulbSwitch(1)
print X.bulbSwitch(3)
print X.bulbSwitch(5)
print X.bulbSwitch(8)