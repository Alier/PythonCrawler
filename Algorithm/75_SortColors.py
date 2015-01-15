class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A is None or len(A) <=1:
            return A
            
        #put red to the foremost and blue to the latest
        nextRed = 0
        nextBlue = len(A)-1 #start of blue
        
        i = nextRed
        while i <= nextBlue:
            if A[i] == 0 and i > nextRed: # SWAP A[i] and A[nextRed], don't modify i
                temp = A[nextRed] 
                A[nextRed] = A[i]
                A[i] = temp
                nextRed = nextRed + 1
            elif A[i] == 2 and i < nextBlue:# SWAP A[i] and A[nextBlue], don't modify i
                temp = A[nextBlue]
                A[nextBlue] = A[i]
                A[i] = temp
                nextBlue = nextBlue - 1
            else:    
                i = i + 1