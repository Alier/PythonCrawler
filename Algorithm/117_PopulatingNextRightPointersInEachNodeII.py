# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None or root.left is None and root.right is None:
            return
        
        if root.left is not None and root.right is None:
            root.left.next = self.getFirstChild(root.next)
            self.connect(root.left)
        elif root.left is None and root.right is not None:
            root.right.next = self.getFirstChild(root.next)
            self.connect(root.right)
        else:# left and right both not None
            root.left.next = root.right
            root.right.next = self.getFirstChild(root.next)
            self.connect(root.right)
            self.connect(root.left)
        
        return

    def getFirstChild(self, root):
        if root is None:
            return None
        
        if root.left is not None:
            return root.left
        elif root.right is not None:
            return root.right
        else: # root has no left or right child
            return self.getFirstChild(root.next)