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
        lenA = m
        while j < n and i < lenA:
            #compare B[j] with A[i] and A[i+1]
            if B[j] < A[i]: #insert ahead of A[i], keep i unchanged.
                #A.insert(i,B[j])
                self.insertIntoIndex(A,lenA,i,B[j])
                lenA = lenA + 1
                j = j + 1
            else:
                if B[j] < A[i+1]: # insert in between A[i] and A[i+1], change i to where B[j] is inserted
                    #A.insert(i+1,B[j])
                    self.insertIntoIndex(A,lenA,i+1,B[j])
                    lenA = lenA + 1
                    j = j + 1
                i = i + 1
        
        # adding rest of B to end of A
        if i == lenA :
            for t in range(j,n):
                A[i] = B[t]
                i = i + 1

        return  
                                    
    def insertIntoIndex(self,arrayA,lenA,index,val):
        i = lenA - 1
        while i >= index:
            arrayA[i+1] = arrayA[i]
            i = i - 1
            
        arrayA[index] = val
        return
            