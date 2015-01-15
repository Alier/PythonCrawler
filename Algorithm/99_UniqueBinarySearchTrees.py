class Solution:
    # @return an integer
    def numTrees(self, n):
        return self.numTreesRange(1,n)
        
    def numTreesRange(self,start,end):
        if start > end:
            return 0

        if start == end:
            return 1
           
        if start+1 == end:
            return 2
        
        if start+2 == end:
            return 5
            
        # when first element as root and last element as root
        num = self.numTreesRange(start+1,end)  + self.numTreesRange(start,end-1)
        # when second element and last second element as root
        num = num + self.numTreesRange(start+2,end) + self.numTreesRange(start,end-2)
        
        #for each integer, calculate how many unique BST trees when it's root
        i = start + 2 
        while i<=end-2: 
            leftTrees = self.numTreesRange(start,i-1) 
            rightTrees = self.numTreesRange(i+1,end)
            num = num + leftTrees * rightTrees
            i = i + 1

        return num