class Solution:
    # @param A, a list of integer
    # @return an integer
    def getSum(self,A):
        sum = 0
        for a in A:
            sum = sum + a
        
        return sum
        
    def singleNumber(self, A):
        if A is None or len(A) == 0:
            return 0
            
        B = set(A)
        return (3 * self.getSum(B) - self.getSum(A))/2