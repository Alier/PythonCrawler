# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        leftMin = -1 
        rightMin = -1
        result = 0
        
        if root.left is not None:
            leftMin = self.minDepth(root.left)
        if root.right is not None:
            rightMin = self.minDepth(root.right)
        
        if leftMin == -1:
            result = rightMin + 1
        elif rightMin == -1:
            result = leftMin + 1
        else:
            if leftMin < rightMin:
                result = leftMin + 1
            else:
                result = rightMin + 1
            
        return result
    