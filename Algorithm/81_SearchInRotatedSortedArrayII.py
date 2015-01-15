class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if A is None or len(A) == 0:
            return False
        
        maxIndex = len(A)-1
        minIndex = 0 
        
        for i in range(0,len(A)-1):
            if target == A[i]:
                return True
            elif A[i] > A[i+1]: #rotate point
                maxIndex = i
                minIndex = i+1
                break;
            
        #if target is not found before rotate point, check the rest
        if target > A[maxIndex] or target < A[minIndex]:
            return False
        
        for i in range(minIndex,len(A)):
            if target == A[i]:
                return True
            
        return False