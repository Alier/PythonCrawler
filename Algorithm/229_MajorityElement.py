'''
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []

        counts = dict()
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

        return [m for m in counts.keys() if counts[m] > len(nums)/3]
