class Solution(object):
    # return True if this cell need to flip its status, either from 0 - > 1 or from 1-> 0, return False otherwise.
    def needFlip(self, board, row, col):
        liveNeighborCount = 0 
        
        # upper neighbor: a[row-1][col-1], a[row-1][col], a[row-1][col+1]  
        # same level neighbor: a[row][col-1], a[row][col+1]
        # lower neighbor: a[row+1][col-1], a[row+1][col], a[row+1][col+1] 
        neighbors = [(row-1, col-1),(row-1,col),(row-1,col+1),
                    (row,col-1),(row,col+1),
                    (row+1, col-1),(row+1, col),(row+1, col+1)]
        
        for n in neighbors:
            r = n[0]
            c = n[1]
            if r >= 0 and r <= len(board)-1 and c >= 0 and c <= len(board[0])-1:
                if board[r][c] > 0:
                    liveNeighborCount += 1
        
        if board[row][col] == 1 and (liveNeighborCount < 2 or liveNeighborCount > 3):
            return True
        
        if board[row][col] == 0 and liveNeighborCount == 3:
            return True
            
        return False
        
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return 
        
        m = len(board)
        n = len(board[0])
        
        toFlip = []
        
        for i in range(0,m):
            for j in range(0,n):
                if self.needFlip(board,i,j):
                    toFlip.append((i,j))
                    
        for f in toFlip:
            i = f[0]
            j = f[1]
            board[i][j] = 1 - board[i][j] 
        
        return