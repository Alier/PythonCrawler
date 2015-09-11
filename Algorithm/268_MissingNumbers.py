# the clue to this solution is : if a ^ b = c, then a ^ c = b and b ^ c = a
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lowest = nums[0]
        highest = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            result ^= nums[i]
            if nums[i] > highest:
                highest = nums[i]
            if nums[i] < lowest:
                lowest = nums[i]

        if lowest >= 1:
            return 0
                
        if len(nums) == (highest - lowest + 1) : # missing largest one
            return highest + 1
            
        else :
            for x in range(lowest, highest + 1):
                result ^= x
            return result