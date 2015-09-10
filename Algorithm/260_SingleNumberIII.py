import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
        return [ans, ans ^ xor]
        
x = Solution()
print x.singleNumber([1,5,6,0,1,0])