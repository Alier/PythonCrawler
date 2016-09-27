'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = 0
        nextIsland = '5'
        equals = []  # merged islands, [[5,6],[4,7,8]] meaning islands 5 and 6 are merged
        chgrid = [list(row) for row in grid]
        
        for i in xrange(len(grid)):  # row            
            for j in xrange(len(chgrid[i])): #column
                if chgrid[i][j] == '1':
                    if i == 0 and j == 0: #very first element, no up or left
                        count += 1
                        chgrid[i][j] = nextIsland
                        nextIsland = str(int(nextIsland)+1)
                    elif i == 0: # rest of first row, j != 0, check left only
                        if chgrid[i][j-1] == '0':
                            count += 1
                            chgrid[i][j] = nextIsland
                            nextIsland = str(int(nextIsland)+1)
                        else: # if left == '1', it would have been marked by now
                            chgrid[i][j] = chgrid[i][j-1]
                    elif j == 0: # rest of first column, i != 0, check up only
                        if chgrid[i-1][j] == '0':
                            count += 1
                            chgrid[i][j] = nextIsland
                            nextIsland = str(int(nextIsland)+1)
                        else: # if up == '1', it would have been marked by now
                            chgrid[i][j] = chgrid[i-1][j]
                    else: # i!= 0 and j!= 0, check up and left
                        if chgrid[i][j-1] == '0' and chgrid[i-1][j] == '0':
                            count += 1
                            chgrid[i][j] = nextIsland
                            nextIsland = str(int(nextIsland)+1)
                        elif chgrid[i][j-1] == '0': # left is 0
                            chgrid[i][j] = chgrid[i-1][j]
                        elif chgrid[i-1][j] == '0': # up is 0
                            chgrid[i][j] = chgrid[i][j-1]
                        else: # both up and left has been marked
                            chgrid[i][j] = chgrid[i][j-1]
                            if chgrid[i][j-1] != chgrid[i-1][j]:
                                # up and left belongs to two islands merged now
                                tag1 = chgrid[i][j-1]
                                tag2 = chgrid[i-1][j]
                                # should have at most one index in equals
                                tag1Idxs = [m for m in xrange(len(equals)) if tag1 in equals[m]]
                                tag2Idxs = [m for m in xrange(len(equals)) if tag2 in equals[m]]

                                # both islands have never merged any other islands
                                if len(tag1Idxs) == 0 and len(tag2Idxs) == 0:
                                    count -= 1
                                    equals.append([chgrid[i][j-1], chgrid[i-1][j]])
                                elif len(tag1Idxs) == 0: # tag2 already merged with some other island before
                                    count -= 1
                                    equals[tag2Idxs[0]].append(tag1)                                    
                                elif len(tag2Idxs) == 0: # tag1 already in equals
                                    count -= 1
                                    equals[tag1Idxs[0]].append(tag2)
                                elif tag1Idxs[0] != tag2Idxs[0]: #both are != 0 and doesn't belong to same islands
                                    count -= 1
                                    equals[tag1Idxs[0]] += equals[tag2Idxs[0]]
                                    del equals[tag2Idxs[0]]

        print "equals = %r" % equals
        print "grid: "
        for row in chgrid:
            print ''.join(row)
            
        return count
                
            
