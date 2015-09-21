class Solution(object):
    maxRob = {}
    
    def getMaxRob(self, nums, lowIndex):
        highIndex = len(nums) - 1 
        
        if lowIndex == highIndex:
            return nums[lowIndex]
        
        if lowIndex in self.maxRob:
            return self.maxRob[lowIndex]
        
        curMax = 0
        
        if highIndex - lowIndex == 1: #[a,b]
            curMax = nums[lowIndex]
            if curMax < nums[highIndex]:
                curMax = nums[highIndex]
            
        elif highIndex - lowIndex == 2: # [a,b,c]
            curMax = nums[lowIndex] + nums[highIndex]
            if nums[lowIndex+1] > curMax:
                curMax = nums[lowIndex+1]
        
        else: # highIndex - lowIndex >= 3 .[a,b,c,d,...]
            curMax = nums[lowIndex] + self.getMaxRob(nums,lowIndex+2)  
            maxFromNext = nums[lowIndex+1] + self.getMaxRob(nums, lowIndex+3)
            if maxFromNext > curMax:
                curMax = maxFromNext
        
        self.maxRob[lowIndex] = curMax
        return curMax

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        
        curIndex = 0
        while curIndex <= len(nums)-1 and nums[curIndex] == 0:
            curIndex += 1
        
        if curIndex == len(nums):  # all elements are 0
            return 0
            
        self.maxRob = {}
        return self.getMaxRob(nums,curIndex)
                
st = Solution()
print st.rob([1,1,2,1])