class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A is None or len(A) == 0:
            return [-1,-1]
        
        if len(A) == 1:
            if A[0] != target:
                return [-1,-1]
            else:
                return [0,0]
            
        if target < A[0] or target > A[-1]:
            return [-1,-1]
        
        midIdx = len(A)/2
        if target < A[midIdx]:
            return self.searchRange(A[:midIdx],target)
        elif target > A[midIdx]:
            tempIdxs = self.searchRange(A[midIdx+1:],target)
            if tempIdxs[0] == -1 :
                return tempIdxs
            return [tempIdxs[0]+midIdx+1,tempIdxs[1]+midIdx+1]
        else: #target == midIdx
            i = midIdx-1
            while i >= 0 :
                if A[i] != target:
                    break;
                else:
                    i = i - 1
            print i 
            j = midIdx+1
            while j < len(A):
                if A[j] != target:
                    break;
                else:
                    j = j + 1
            print j
            return [i+1, j-1]

st = Solution()
print st.searchRange([0,0,1,1,1,4,5,5],2)
