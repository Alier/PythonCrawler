class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]
        
        result = list()
        result.append([1])
        result.append([1,1])
        for i in range(2,numRows):
            row = list()
            for j in range(0,i+1):
                row.append(0)
            result.append(row)
        
        for i in range(2,numRows):
            rowLen = i+1
            # first and last are 1
            result[i][0] = 1
            result[i][rowLen-1] = 1
            
            # anything in between is sum of last row's two numbers
            for j in range(1,rowLen-1): 
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        
        return result