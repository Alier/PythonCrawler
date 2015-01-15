class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if A is None or m == 0:
            for idx in xrange(n):
                A[idx] = B[idx]
            return
        
        if B is None or n == 0:
            return
         
        i = 0
        j = 0
        while j < n and i < len(A) -1:
            #compare B[j] with A[i] and A[i+1]
            if B[j] < A[i]: #insert ahead of A[i], keep i unchanged.
                A.insert(i,B[j])
                j = j + 1
            else:
                if B[j] < A[i+1]: # insert in between A[i] and A[i+1], change i to where B[j] is inserted
                    A.insert(i+1,B[j])
                    j = j + 1
                i = i + 1
        
        if i == len(A) - 1:
            for t in range(j,n):
                A.append(B[t])
            
        return  
                 