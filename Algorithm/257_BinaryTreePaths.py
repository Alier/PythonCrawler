# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [str(root.val)]
    
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        result = []
        if len(leftPaths) > 0:
            for leftp in leftPaths:
                result.append(str(root.val)+"->"+leftp)
        if len(rightPaths) > 0:
            for rightp in rightPaths:
                result.append(str(root.val)+"->"+rightp)
                
        return result
