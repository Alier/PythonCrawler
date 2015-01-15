# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        levels = list()
        vals = list()
        
        if root is None:
            return levels

        levels.append([root])
        
        while len(levels[0]) > 0:
            newLevel = list()
            newVals = list()
            for node in levels[-1]:
                newVals.append(node.val)
                if node.left is not None:
                    newLevel.append(node.left)
                if node.right is not None:
                    newLevel.append(node.right)
            levels.remove(levels[0])    
            levels.append(newLevel)
            vals.append(newVals)
        
        return vals
            