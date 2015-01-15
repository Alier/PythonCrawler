class Solution:
    # @return an integer
    def maxArea(self, height):
        if height is None or len(height) <= 1:
            return 0
        
        maxArea = 0
        n = len(height)
        maxLeftBar = 0
        for i in range(0,n-1):
            if height[i] > maxLeftBar: # if lower than previous bar, ignore
                maxLeftBar = height[i]
                # if end points is higher than left bar i, end points should be the right bar
                if height[n-1] >= height[i]:
                    curMax = height[i] *(n-1-i)
                else:# end point is shorter than left bar i, then calculate the max
                    curMax = self.getMaxArea(height,i,n-1)
                if curMax > maxArea:
                        maxArea = curMax
            
        return maxArea
    
    def getMaxArea(self,height,leftBar,rightEnd):
        result = 0
        for j in range(leftBar+1,rightEnd+1):
            if height[j] > height[leftBar]:
                curMax = height[leftBar]*(j-leftBar)
            else:
                curMax = height[j] *(j-leftBar)
                
            if curMax > result:
                result = curMax
            
        return result