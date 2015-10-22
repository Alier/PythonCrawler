#Note: This is an extension of House Robber.

#After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    calculated = {}
    
    def getMax(self, nums, startI, endI):
    	print self.calculated
        if startI > endI:
            return 0
            
        if startI == endI:
            return nums[startI]
        
        if (startI, endI) in self.calculated:
            return self.calculated[(startI, endI)]
            
        if startI + 1 == endI:
            if nums[startI] > nums[endI]:
                result = nums[startI]
            else:
                result = nums[endI]
            self.calculated[(startI, endI)] = result
            return result
                
        for i in range(startI, endI+1):
        	if startI == 0:
        		curMax = nums[startI] + self.getMax(nums, startI+2, endI-1)    
        	else:
        		curMax = nums[startI] + self.getMax(nums, startI+2, endI)            
        	
        	nextMax = self.getMax(nums, startI+1, endI)
        	print "curMax="+str(curMax) +" nextMax="+str(nextMax)
        	if curMax > nextMax:
        		result = curMax
        	else:
        		result = nextMax
        	self.calculated[(startI, endI)] = result
        	return result
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        if nums is None or len(nums) == 0:
            return 0
            
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
                   
        if len(nums) == 3:
            result = nums[0]
            if nums[1] > result:
                result = nums[1]
            if nums[2] > result:
                result = nums[2]
            return result
            
        result = self.getMax(nums, 0, len(nums)-1)
        print self.calculated
        return result
    
st = Solution()
#a = [1,1,2,1]
#b = [1,1,1,2]
#c = [1,2,1,2]
#d = [2,1,1,2]
#e = [0,3,2,0]
#a = [1,7,9,4]
#a = [2,9,7,1]
#a =[1,3,1,3,100]
a = [1,1,1,1]
print st.rob(a)
#print st.rob([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72])