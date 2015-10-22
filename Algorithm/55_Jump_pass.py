class Solution(object):
    count = 10
    
    def maxJump(self, nums, startI, endI):
        if self.count < 0:
            return
        
        self.count -= 1
        print "range: "+str(startI) +" -- "+str(endI)
        result = startI + nums[startI]
        for i in range(startI+1,endI+1):
            if i + nums[i] > result:
                result = i + nums[i]
        return result

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) <= 1 :
            return True
        
        if nums[0] < 1:
            return False
       
        i = 0
        # if steping, find the first jumping
        while i < len(nums) and nums[i] == 1:
            i += 1
        
        if i == len(nums):
            return True
        if i + nums[i] >= len(nums) - 1:
            return True
        
        startI = i
        endI = startI+nums[startI]
        maxJumpTo = self.maxJump(nums, startI, endI)
        while maxJumpTo < len(nums) - 1:
            if maxJumpTo == endI and nums[maxJumpTo] == 0:
                return False
            print "maxJumpTo= "+ str(maxJumpTo)
            startI = endI + 1
            endI = maxJumpTo
            maxJumpTo = self.maxJump(nums, startI, endI)
       
        print "final,maxJump="+str(maxJumpTo)
        if maxJumpTo >= len(nums) - 1:
            return True
       
        return False
        
st = Solution()
a =[5,9,3,2,1,0,2,3,3,1,0,0]
print len(a)
print st.canJump(a)