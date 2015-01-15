class Solution:
    # @param A, a list of integers
    # @return an integer
    
    def maxSubArray(self, A):
        if A is None:
            return A
            
        #find all the >0 integer singles and their positions in the array
        #in subArrays would be pair like (startIndex, endIndex) and the corresponding item in subArraySums should be its sum
        maxSingle = A[0] # biggest single number
        firstPositiveIndex = -1
        i = 0
        while i < len(A):
            if A[i] > 0 and firstPositiveIndex == -1:
                firstPositiveIndex = i;
                break;
            if maxSingle < A[i]:
                maxSingle = A[i]
            i = i + 1
        
        # all negative array return the biggest single    
        if firstPositiveIndex == -1:
            return maxSingle
        
        # scan from first positive single, as long as the sum so far is positive, keep adding on, until the sum bigger than current max, set the new max, and record the index start and end
        maxSum = A[firstPositiveIndex]
        maxSubArrayStartI = firstPositiveIndex
        maxSubArrayEndI = firstPositiveIndex
        
        i = firstPositiveIndex
        curSum = 0
        while i < len(A) :
            curSum = curSum + A[i]
            if curSum > 0:
                if curSum > maxSum:
                    maxSum = curSum
                    maxSubArrayEndI = i
                    if maxSubArrayEndI+1 < i: #gap
                        maxSubArrayStartI = i
            else: #curSum <=0, reset i
                curSum = 0 
            
            i = i + 1
            
        return maxSum
            