import time
class Solution(object):
    calculated = {}
    
    def canJumpFromIndex(self, nums, index):
        #print "=====nums["+str(index) +"]:"+str(nums[index])+"========="
        
        if index == len(nums)-1:
            return True
        
        if nums[index] < 1:
            self.calculated[index] = False
            return False
            
        if index + nums[index] >= len(nums) - 1:
            self.calculated[index] = True
            return True

        if index in self.calculated:
            return self.calculated[index]
             
        maxJump = nums[index]
        canJ = False
        #print "range:["+str(maxJump+index)+"-"+str(index+1)+"]"
        for i in range(maxJump+index, index, -1):
            if i in self.calculated:
                thisCan = self.calculated[i]
            else:
        	    print "not found: i="+str(i)
        	    thisCan = self.canJumpFromIndex(nums,i)
        	    self.calculated[i] = thisCan
            canJ = canJ or thisCan
            if canJ is True:
        	    self.calculated[index] = True
        	    return True
        
        self.calculated[index] = False
        return False
        
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) <= 1 :
            return True
        
        i = 0
        while i < len(nums) and nums[i] == 1:
            i += 1
            
        if i == len(nums):
            return True
            
        self.calculated = {}
        return self.canJumpFromIndex(nums,i)

st = Solution()
a =[i for i in range(50,0,-1)]
a.append(0)
a.append(0)
print a
print len(a)
print time.time()
print st.canJump(a)
print time.time()
