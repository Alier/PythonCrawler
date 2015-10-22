# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if p.left == q or p.right == q:
            return p
        
        if q.left == p or q.right == p:
            return q
                
        parentP = []
        parentQ = []
        curStack = [root]
        
        leftChecked = []
        rightChecked = []
        
        parentPfound = False
        parentQfound = False
        
        #search the whole tree to find p and q's parent path from top down
        while len(curStack):
            #print curStack
            #print parentPfound
            #print parentQfound
            curPop = curStack[-1]
           
            if (not parentPfound) and (curPop == p): # ending of p's parents
                parentP = [node for node in curStack]
                parentPfound = True
                if parentPfound and parentQfound:
                    break
           
            if (not parentQfound) and (curPop == q): # ending of q's parents
                parentQ = [node for node in curStack]
                parentQfound = True
                if parentPfound and parentQfound:
                    break
           
            if curPop.left and curPop not in leftChecked:
                curStack.append(curPop.left)
                leftChecked.append(curPop)
            elif curPop.right and curPop not in rightChecked:
                curStack.append(curPop.right)
                rightChecked.append(curPop)
            else:
                del curStack[-1]
        
        #print parentP
        #print parentQ
        if (not parentPfound) or (not parentQfound) : #one of the node not in the tree
            return None
            
        shortPath = len(parentP)
        if len(parentQ) < shortPath:
            shortPath = len(parentQ)
            
        for i in range(0, shortPath):
            if parentP[i] != parentQ[i]: # split happens, last node is common root
                return parentP[i-1]
         
        return parentP[i]
       
tn1 = TreeNode(1) 
tn2 = TreeNode(2)
tn2.right = tn1

st = Solution()
print st.lowestCommonAncestor(tn2,tn2,tn1)