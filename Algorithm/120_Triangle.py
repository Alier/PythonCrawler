class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
            
        if len(triangle) == 1: # only one node
            return triangle[0][0]
        
        for i in range(1, len(triangle)) : #going down each row from second row, as first row is one point
            triangle[i][0] += triangle[i-1][0] # first node on this level
            triangle[i][-1] += triangle[i-1][-1] # last node on this level
            for j in range(1,len(triangle[i])-1): # for middle nodes in this level
                if triangle[i-1][j-1] <= triangle[i-1][j]:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]
        
        return (sorted(triangle[-1]))[0]