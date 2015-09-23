# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    counted = {}
    
    def getSubTree(self, values): # values are a list with node values in ascending order
        if len(values) == 0:
            return []
            
        if len(values) == 1:
            return [TreeNode(values[0])]
        
        if (values[0],values[-1]) in self.counted:
            return self.counted[(values[0],values[-1])]
            
        if len(values) == 2:
            nodeBig = TreeNode(values[1])
            nodeSmall = TreeNode(values[0])
            nodeBig.left = TreeNode(values[0])
            nodeSmall.right = TreeNode(values[1]) 
            result = [nodeSmall, nodeBig]
            self.counted[(values[0],values[-1])] = result
            return result
        
        result = []
        for i in range(0,len(values)):
            leftTrees = self.getSubTree(values[0:i])
            rightTrees = self.getSubTree(values[i+1:])
            if len(leftTrees) == 0: # only right tree
                for rightRoot in rightTrees:
                    curRoot = TreeNode(values[i]) 
                    curRoot.right = rightRoot
                    result.append(curRoot)
            
            elif len(rightTrees) == 0 : # only left tree
                for leftRoot in leftTrees:
                    curRoot = TreeNode(values[i]) 
                    curRoot.left = leftRoot
                    result.append(curRoot)
                
            else:
                for leftRoot in leftTrees:
                    for rightRoot in rightTrees:
                        curRoot = TreeNode(values[i]) 
                        curRoot.left = leftRoot
                        curRoot.right = rightRoot
                        result.append(curRoot)
        
        self.counted[(values[0],values[-1])] = result         
        return result
            
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return [[]]
            
        return self.getSubTree([i for i in range(1,n+1)])
        
            