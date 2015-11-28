# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        
        result = []
        if root.left is not None:
            leftPath = self.pathSum(root.left, sum-root.val)
            if len(leftPath) :
                for path in leftPath:
                    path.insert(0,root.val)
                    result.append(path)
        
        if root.right is not None:
            rightPath = self.pathSum(root.right, sum-root.val)
            if len(rightPath):
                for path in rightPath:
                    path.insert(0, root.val)
                    result.append(path)
        
        return result
    