class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None or len(A) <= 1:
            return len(A)
            
        lastIndex = 0
        i = lastIndex
        while i < len(A):
            if A[i] > A[lastIndex]:
                temp = A[lastIndex+1]
                A[lastIndex+1] = A[i]
                A[i] = temp
                lastIndex = lastIndex + 1
                
            i = i + 1
        
        A = A[:lastIndex+1]
        return len(A)