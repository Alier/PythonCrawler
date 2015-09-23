class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        
        for i in range(0,32):
            lowestDigit = n & 1
            n = n >> 1
            ret = ret << 1
            ret |= lowestDigit

        return ret
        
st = Solution()
st.reverseBits(1)