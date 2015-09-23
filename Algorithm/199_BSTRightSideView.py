# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
            
        #put nodes in same level from right to left, every loop, take the first node in that level to put in result
        allNodes = []
        result = []
        allNodes.append(root)
        curLevelStartIndex = 0 # index in the list where the nodes in current level starts
         
        while curLevelStartIndex < len(allNodes): # there is node in current level, tree not done
            result.append(allNodes[curLevelStartIndex].val)
            curLevelEndIndex = len(allNodes) - 1
            for i in range(curLevelStartIndex, curLevelEndIndex+1):# for each node, put its children from right to left to end
                curNode = allNodes[i]
                if curNode.right is not None:
                    allNodes.append(curNode.right)
                if curNode.left is not None:
                    allNodes.append(curNode.left)
            curLevelStartIndex = curLevelEndIndex + 1
        
        return result
            