# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        
        result = list()
        nodes = list()
        
        nodes.append([root])
        while len(nodes[0]) > 0:
            vals = list()
            nextLevelNodes = list()
            for node in nodes[0]:
                vals.append(node.val)
                if node.left is not None:
                    nextLevelNodes.append(node.left)
                if node.right is not None:
                    nextLevelNodes.append(node.right)
            nodes.remove(nodes[0])
            nodes.append(nextLevelNodes)
            result.insert(0,vals)
            
        return result