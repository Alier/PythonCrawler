'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
            return []
        
        result = []
        set1, set2 = set(nums1), set(nums2)
        
        if len(set1) >= len(set2):
            for s2 in set2:
                if s2 in set1:
                    result.append(s2)
        else:
            for s1 in set1:
                if s1 in set2:
                    result.append(s1)
        
        return result
