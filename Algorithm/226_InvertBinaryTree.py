# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        if root.left is None and root.right is None:
            return root
        
        leftSubTree = root.left
        rightSubTree = root.right
        
        root.left = self.invertTree(rightSubTree)
        root.right = self.invertTree(leftSubTree)
    
        return root
        