class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if A is None or len(A) == 0:
            return -1

        for i in range(0,len(A)-1):
            if A[i] == target:
                return i;
                
            if A[i+1] < A[i]:
                maxVal = A[i]
                minVal = A[i+1]
                if target > maxVal or target < minVal:
                    return -1
                
        # i == len(A)-1 now
        if target == A[-1]:
            return len(A)-1
        
        return -1