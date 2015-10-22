class Solution(object):
    # saving already searched subArray starting with index i, looking for j elements sum cloest to target, value is cloestSum
    # saving as (i,j) : cloestSum
    calculated = {}
    
    def sumClosest(self, nums, startIndex, target, numNodes):
    	#print self.calculated
        if (startIndex,numNodes) in self.calculated:
            return self.calculated[(startIndex,numNodes)]
            
        if len(nums) - startIndex == numNodes:
            closestSum = sum(nums[startIndex:])
            self.calculated[(startIndex,numNodes)] = closestSum
            return closestSum
            
        if numNodes == 1:
            closestSum = nums[startIndex]
            for i in range(startIndex+1, len(nums)):
                if abs(nums[i] - target) < abs(closestSum - target):
                    closestSum = nums[i]
            self.calculated[(startIndex,numNodes)] = closestSum
            return closestSum
        
        closestSum = target
        for i in range(startIndex,len(nums)-(numNodes-1)):
            curElem = nums[i]
            restSumClosest = self.sumClosest(nums, i+1, target-curElem, numNodes-1)
            curSumClosest = curElem + restSumClosest
            if closestSum == target or abs(curSumClosest - target) < abs(closestSum - target):
                closestSum = curSumClosest
        
        self.calculated[(startIndex,numNodes)] = closestSum
        return closestSum

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        
        self.calculated = {}
        result = self.sumClosest(nums, 0, target, 3)
        print self.calculated
        return result
        
st = Solution()
#print st.threeSumClosest([1,1,1,1], -100)
print st.threeSumClosest([84,58,16,-6,-34,72,96,56,-31,45,-6,53,-79,-43,-92,-88,3,16,-6,33,84,-62,0,-29,-88,58,-14,21,51,61,1,17,26,57,-55,39,95,50,-16,25,85,65,-25,23,-82,-85,-99,-20,34,89,67,93,60,-21,-87,47,62,-1,63,-96,75,94,81,-29,56,69,-78,49,36,-80,49,-26,3,-29,52,-77,38,31,-49,-100,-44,-60,62,-24,45,-88,63,-36,7,-99,22,18,77,11,9,-63,44,6,-30,71,-68,0,37,29,-68,71,-35,83,4,-3,-3,-100,-88,-19,3,92,-47,33,-61,-96,-23,51,87,2,26,72,38,-42,77,-43,17,83,-59,82,45,-81,-41,-58,30,-85,-67,51,-27,63,-54,83,-6,68,81,-17,24,-59,96,59,-78,48,-100,-81,25,-28,-82,15,-76,86,65,-48,-67,-20,90,-89,-89,9,1,46,-67,71,-51,69,-2,14,89,-89,-1,85,-20,-57,75,28,22,-35,81],
-48)
