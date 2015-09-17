# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        del self.stack[len(self.stack)-1]
        
    def peek(self):
        return self.stack[len(self.stack)-1]
    
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        tempStack = Stack() # to save which one to check now
        valSequence = []
        #nodeSequence = []
        checkedLeft = [] # to keep track to see whether the current node's checked left child already
        
        if root is None:
            return 0
        
        tempStack.push(root) 
        while (len(tempStack.stack)) and len(valSequence) < k:
            curNode = tempStack.peek()
            if curNode in checkedLeft: # already checked left child, pop and push right child in if there is any
                tempStack.pop()
                #nodeSequence.append(curNode)
                valSequence.append(curNode.val)
                if curNode.right is not None:
                    tempStack.push(curNode.right)
            else: # check left child, if left child, push in, if no left child, pop out
                checkedLeft.append(curNode)
                if curNode.left is not None:
                    tempStack.push(curNode.left)
    
        return valSequence[k-1]
            
                    

        
        