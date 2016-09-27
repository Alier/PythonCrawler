'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        
        if len(nums) > 0:
            self.rangeSumsFromZero = [None] * len(nums)
        
            # [0] -->(0,0), [1] -->(0,1), [2] -->(0,2)
            self.rangeSumsFromZero[0] = self.nums[0]
            for j in xrange(1,len(nums)):
                self.rangeSumsFromZero[j] = self.rangeSumsFromZero[j-1] + self.nums[j]
            
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.nums is None or len(self.nums) == 0:
            return 0
            
        if i > j:
            return 0
        
        if i == j:
            return self.nums[i]
            
        if i == 0:
            return self.rangeSumsFromZero[j]
            
        return self.rangeSumsFromZero[j] - self.rangeSumsFromZero[i-1]
        
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
