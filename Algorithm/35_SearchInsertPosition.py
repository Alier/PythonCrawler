class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A is None or len(A) == 0:
            return 0
      
        i = 0
        while i < len(A):
            if target <= A[i]:
                return i
           
            #target > A(i), keep going
            i = i+1
        
        #j is last and target > A(j), return last index
        return i