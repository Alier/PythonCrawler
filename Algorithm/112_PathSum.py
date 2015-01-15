# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        
        if root.val == sum and root.left is None and root.right is None:
            return True
            
        newSum = sum - root.val
        return self.hasPathSum(root.left,newSum) or self.hasPathSum(root.right,newSum)