class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = list()
        if n == 0 :
            return matrix
        
        if n == 1:
            matrix.append(list([1]))
            return matrix
            
        for i in range(0,n):
            matrix.append([0]*n)
            
        i = 0
        j = 0
        matrix[i][j] = 1
        filled = 1
        totalNodes = n**2
        
        while filled < totalNodes:
            nextVal = filled + 1
            #calculate nextI and nextJ:
            # if j is not last one in the swirl row in upper half, --> horizontally
            if j < (n-1)-i and j>= i - 1 and i <= (n-1)/2:
                nextI = i
                nextJ = j + 1
            # if j is not first one in the swirl row in lower half, <-- horizontally
            elif j > (n-1)-i and j<= i and i > (n-1)/2:
                nextI = i
                nextJ = j - 1
            # if i is not the lowest one in the swirl column in the right half, going down
            elif j > (n-1)/2 and i < j :
                nextI = i + 1
                nextJ = j
            # if i is not the highest one in the swirl column in the left half, going up
            elif j <= (n-1)/2 and i > j+1:
                nextI = i - 1
                nextJ = j
            else:
                break
            matrix[nextI][nextJ] = nextVal
            i = nextI
            j = nextJ
            filled = filled + 1

        return matrix