class Solution(object):
    def smallestDistance(self, indices):
        smallest = indices[1] - indices[0]
        for i in range(1, len(indices)-1):
            print smallest
            if indices[i+1] - indices[i] < smallest:
                smallest = indices[i+1] - indices[i]
        
        return smallest
        
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums is None or len(nums) < 2:
            return False
            
        if k == 0:
            return False
            
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return True
            else:
                return False
        
        locations ={}
        for i in range(0, len(nums)):
            print locations
            if nums[i] in locations:
                locations[nums[i]].append(i)
            else:
                locations[nums[i]]=[i]
        
        for locKey in locations:
        	print locKey
        	print locations[locKey]
        	#print self.smallestDistance(locations[locKey])
        	if len(locations[locKey]) > 1 and self.smallestDistance(locations[locKey]) <= k:
        		return True
                
        return False
        
st = Solution()
print st.containsNearbyDuplicate([1,0,1,1],1)