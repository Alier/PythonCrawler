class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None:
            return 0
            
        if len(A) <= 2:
            return len(A)
        
        curVal = A[0]
        count = 1
        i = 1
        while i < len(A):
            if A[i] == curVal:
                if count == 2:#remove from A[i] same curVal
                    A.remove(curVal)
                else:
                    count = count + 1
                    i = i + 1
            else: #A[i] > curVal
                curVal = A[i]
                count = 1
                i = i + 1
                
        return len(A)
           
        