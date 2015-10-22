class Solution(object):
    # count is total count of numbers in range(lowBond, highBond+1) 
    countDown = 10
    def findDuplicateInRange(self, nums, count, lowBond, highBond):
    	if self.countDown < 0:
    		return -1
    	print "count/lowBond/highBond ="+str(count)+"/"+str(lowBond)+"/"+str(highBond)
    	self.countDown -= 1
        # only lowBond, highBond two digits might be candidates for duplicate
        if lowBond + 1 == highBond:
            equalLowBond = 0
            equalHighBond = 0
            for num in nums:
                if num == lowBond:
                    equalLowBond += 1
                elif num == highBond:
                    equalHighBond += 1
                
                if equalLowBond > 1:
                    return lowBond
                
                if equalHighBond > 1:
                    return highBond
            
        mid = (lowBond + highBond)/2
        smaller = 0
        larger = 0
        equal = 0
        
        for num in nums:
            if num < lowBond or num > highBond:
                continue
            
            if num < mid:
                smaller += 1
            elif num == mid:
                equal += 1
            else: #num > mid
                larger  += 1
            
            if smaller + equal + larger == count :
                break
        
        if equal > 1:
            return mid
        
        # if no duplicate, counts of numbers in range (lowBond,mid) should be equal to (mid-1)-lowBond+1 = mid-lowBond
        if smaller > mid-lowBond: # duplicate must be in range(lowBond, mid)
            return self.findDuplicateInRange(nums, smaller, lowBond, mid-1)
        else: # duplicate in range(mid+1,highBond+1)
            return self.findDuplicateInRange(nums, larger, mid+1, highBond)
            
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
            
        
        return self.findDuplicateInRange(nums, len(nums), 1, len(nums)-1)
            
st = Solution()
print st.findDuplicate([1,2,2,3,4,2,2,6,2,2,8,2,2,2,22,2,2,2,2,2,2,2,2,2,17,19,18,9,7,5,20,16,15,14,13])
                
        
        
        