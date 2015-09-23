class Solution(object):
    def subsetsWithDupSorted(self, nums):
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return [[],[nums[0]]]
        
        result = [[]]
        for i in range(0,len(nums)):
            curNum = nums[i]
            if [curNum] not in result:
                result.append([curNum])
            tempR = self.subsetsWithDup(nums[i+1:])
            if tempR is not None:
                for comb in tempR:
                    comb.insert(0,curNum)
                    if comb not in result:
                        result.append(comb)
        
        return result   
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return None
        
        return self.subsetsWithDupSorted(sorted(nums))
        
st = Solution()
print st.subsetsWithDup([1,2])