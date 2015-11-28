class Solution(object):
    def getNextIndex(self, curIndex, totalLen):
        if curIndex == totalLen - 1:
            return 0
        else:
            return curIndex+1
            
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1 
            
        i = 0
        while i < len(gas) and (gas[i] - cost[i] < 0):
            i += 1 
        
        if i == len(gas):
            return -1
            
        startIndex = i
        curLeft = gas[i] - cost[i]
        j = self.getNextIndex(i,len(gas)) 
        while j != startIndex:
            curLeft += gas[j] - cost[j]
            if curLeft < 0: # find next positive start
                i = self.getNextIndex(j,len(gas)) 
                while i < len(gas) and (gas[i] - cost[i] < 0):
                    i += 1
                if i == len(gas):
                    return -1
                startIndex = i
                curLeft = gas[i] - cost[i]
                j = self.getNextIndex(i,len(gas)) 
            else:
                j = self.getNextIndex(j,len(gas)) 
                
                
        if j == startIndex:
            return startIndex
        
        return -1
                    
st = Solution()
print st.canCompleteCircuit([1,2,3,3],[2,1,5,1])