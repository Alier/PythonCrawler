# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num is None or len(num) == 0:
            return None
        
        if len(num) == 1:
            return TreeNode(num[0])
       
        if len(num) == 2:
            root = TreeNode(num[1])
            root.left = TreeNode(num[0])
            return root

        #find the middle point as root
        middleIndex = len(num)/2
        root = TreeNode(num[middleIndex])
        root.left = self.sortedArrayToBST(num[:middleIndex])
        root.right = self.sortedArrayToBST(num[middleIndex+1:])
        
        return root
        