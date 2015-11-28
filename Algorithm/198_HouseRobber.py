class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0],nums[1])
            
        if len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])
            
        maxRob = [nums[0], max(nums[0],nums[1])]
        for i in range(2, len(nums)):
            maxRob.append(max(maxRob[i-2]+nums[i], maxRob[i-1]))
        
        return maxRob[-1]
                      
st = Solution()
print st.rob([1,1,2,1])