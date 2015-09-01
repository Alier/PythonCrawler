class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = dict()
        for num in nums:
            if num in counts:
                return True
            else:
                counts[num] = 1
        
        return False
