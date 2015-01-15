class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if A is None or len(A) <= 2:
            return 0
            
        peakIdxs = list()
        for i in range(0,len(A)):
            if i == 0 and A[i] > A[i+1]:
                peakIdxs.append(i)
            elif i == len(A) - 1 and A[i] > A[i-1]:
                peakIdxs.append(i)
            elif i > 0 and i < len(A) - 1 and A[i] >= A[i-1] and A[i] >= A[i+1]:
                peakIdxs.append(i)
        
        print peakIdxs
        #merge peaks, if  last peak > peak < next peak , then delete this peak, first and last peak can't be
        i = 1
        while i < len(peakIdxs)-1:
            curIdx = peakIdxs[i]
            lastIdx = peakIdxs[i-1]
            nextIdx = peakIdxs[i+1]
            if A[curIdx] <= A[lastIdx] and A[curIdx] <= A[nextIdx]:
                peakIdxs.remove(curIdx)
                if i > 1:
                    i = i - 1
            else:
                i = i + 1
        
        print peakIdxs
        if len(peakIdxs) <= 1:
            return 0
            
        totalWater = 0
        for i in range(0,len(peakIdxs)-1):
            leftBarIdx = peakIdxs[i]
            rightBarIdx = peakIdxs[i+1]
            lowBar = A[leftBarIdx]
            if A[rightBarIdx] < lowBar:
                lowBar = A[rightBarIdx]
            curWater = lowBar * (rightBarIdx-leftBarIdx-1) - self.SumBarsUnderWater(A,leftBarIdx+1,rightBarIdx-1,lowBar)
            totalWater = totalWater + curWater
            
        return totalWater
    
    # calculate the sum of all areas taken by bars that's under water surface. 
    # e.g for [5,4,1,2], areas between 5 and 2 taken by bar which could be used for water should be : 2 + 1 = 3 instead of 4+1 
    def SumBarsUnderWater(self, A, leftIndex,rightIndex,waterBar):
        result = 0
        for i in range(leftIndex,rightIndex+1):
            if A[i] > waterBar:
                result = result + waterBar
            else:
                result = result + A[i]
        print result
        return result

st = Solution()
#A = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
#A = [5,3,7,7]
A = [8,8,1,5,6,2,5,3,3,9]
print st.trap(A)
