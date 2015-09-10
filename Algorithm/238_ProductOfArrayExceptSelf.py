class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        retArray = []
        if len(nums) <= 1 :
            return retArray
        
        result = 1
        count = 0
        for n in nums:
            if n == 0:
                count = count + 1
            else :
                result = result * n
        
        if count > 1: #more than one zero
            for i in range(0, len(nums)):
                print i
                retArray.append(0)
        elif count == 1 :
            for i in range(0,len(nums)):
                if nums[i] == 0:
                    retArray.append(result)
                else:
                    retArray.append(0)
        else:
            for i in range(0, len(nums)):
                retArray.append(result/nums[i])
        
        return retArray