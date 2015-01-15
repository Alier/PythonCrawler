class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        newLen = 0
        totalLen = len(A)
        
        for a in range(0,totalLen):
            if A[a] != elem:
                A.append(A[a])
                newLen = newLen + 1
            a = a + 1
            
        A = A[totalLen:totalLen+newLen]
        
        return newLen
        