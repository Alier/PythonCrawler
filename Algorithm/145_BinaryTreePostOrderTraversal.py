# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = list()
        
        if root is None:
            return result
            
        stk = list()
        stk.append(root)
        
        while len(stk) > 0:
            curNode = stk.pop()
          
            if curNode.left is not None:
                leftRoot = curNode.left
                curNode.left = None
                stk.append(curNode)
                stk.append(leftRoot)
            elif curNode.left is None and curNode.right is not None:
                rightRoot = curNode.right
                curNode.right = None
                stk.append(curNode)
                stk.append(rightRoot)
            else: # no left nor right, direct print
                result.append(curNode.val)
                
        return result