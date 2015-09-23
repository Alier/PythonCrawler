class Solution(object):
    visited = {}
    
    def subsetsWithDupSorted(self, nums, startIndex, endIndex):
        if startIndex > endIndex:
            return None
        
        if (startIndex, endIndex) in self.visited:
            return self.visited[(startIndex, endIndex)]
            
        if startIndex == endIndex:
            return [[nums[startIndex]]]
        
        result = []
        for i in range(startIndex,endIndex+1):
            curNum = nums[i]
            if [curNum] not in result:
                result.append([curNum])
            tempR = self.subsetsWithDupSorted(nums,i+1,endIndex)
            if tempR is not None:
                for comb in tempR:
                    comb.insert(0,curNum)
                    if comb not in result:
                        result.append(comb)
        
        self.visited[(startIndex, endIndex)] = result
        return result   
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return None
        
        result = self.subsetsWithDupSorted(sorted(nums), 0, len(nums)-1) 
        if result is not None:
            result.append([])
            
        return result
        
st = Solution()
print st.subsetsWithDup([1,2])