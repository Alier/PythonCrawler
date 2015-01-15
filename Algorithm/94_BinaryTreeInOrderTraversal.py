# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = list()
        
        if root is None:
            return result
            
        # stk would be list of pair (node, visited_flag)
        stk = list()
        stk.append((root,False))

        while len(stk) > 0:
            curPair = stk.pop()
            curNode = curPair[0]
            visited = curPair[1]
            
            if visited is False:# first time, check if it has left tree
                visited = True
                if curNode.left is not None: # left tree, push self in , push left root in
                    stk.append((curNode,visited))
                    stk.append((curNode.left,False))
                elif curNode.left is None and curNode.right is not None: # only right tree, print self, push right root in
                    result.append(curNode.val)
                    stk.append((curNode.right,False))
                else: # no left or right tree, print itself
                    result.append(curNode.val)
            else:#already visited so if it has left tree , already visited. Print itself, if it has right tree, push right root 
                result.append(curNode.val)
                if curNode.right is not None:
                    stk.append((curNode.right,False))
                    
        return result
                
                