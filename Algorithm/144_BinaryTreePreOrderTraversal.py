# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = list()
        
        if root is None:
            return result
            
        stk = list()
        
        #put root in first
        stk.append(root)
        while len(stk) > 0:
            curNode = stk.pop()
            
            if curNode.left is not None:
                leftRoot = curNode.left
                curNode.left = None
                stk.append(curNode)
           
            if(visited is False): #first time, print this, check left/right child trees
                result.append(curNode.val)
                visited = True
                if curNode.left is not None:# has left tree, put it back and put left childtree root in
                    stk.append((curNode,visited))
                    stk.append((curNode.left, False))
                elif curNode.left is None and curNode.right is not None:# only right tree, just put right childtree root in
                    stk.append((curNode.right,False))
                #no left tree no right tree, don't do anything
            else: # visited already, then should have checked at least left tree
                if curNode.right is not None: # only put right tree root in as it would not be visited again
                    stk.append((curNode.right,False))
            
        return result