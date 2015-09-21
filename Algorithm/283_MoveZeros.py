class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        p = 0 # p points to first 0
        q = 0 # q points to first non-0
        
        while p < len(nums):         	
        	while p < len(nums) and nums[p] != 0:
        	    p += 1
        	    
        	if p == len(nums):
        		return
        	
        	q = p + 1   
 
        	while q < len(nums) and nums[q] == 0:
        		q += 1
        	
        	if q == len(nums):
        	    return
        	
        	# exchange p and q:
        	print "p="+str(p)+" q="+str(q)
        	nums[p] = nums[q]
        	nums[q] = 0
        	print nums
        	if q == len(nums) - 1: # last positive
        		return 
        	p += 1
        
        return 
        
st = Solution()
a = [0,0,1,0,3,12,0,0,0,0]
st.moveZeroes(a)
#print a