class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if not A:
            return 0
        
        result = 0
        for a in A:
            result ^= a
        
        return result