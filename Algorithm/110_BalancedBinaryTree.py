# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
            
        if root.left is None and (root.right.left is not None or root.right.right is not None):
            return False
            
        if root.right is None and (root.left.left is not None or root.left.right is not None):
            return False
            
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            diff = self.getDepth(root.left) - self.getDepth(root.right)
            if diff <= 1 and diff >= -1:
                return True
        
        return False
            
    def getDepth(self,root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
            
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        
        if leftDepth > rightDepth:
            return 1+leftDepth
        else:
            return 1+rightDepth