# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        # paths would be a list of list of list, each element in paths is a list of same level paths
        # example:
        # [[[1]],[[1,2],[1,3]]]
        # layer one has one node 1
        # layer two has two nodes 2,3. 1->2 and 1->3 are root to leaf paths
        levels = list()
        result = 0
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.val
        
        levels.append([[root]])
        # always look at last layer
        while len(levels[0]) > 0:
            newLevel = list()
            for path in levels[0]:
                #check the end node of this path to see if it has child trees
                curNode = path[-1]
                if curNode.left is None and curNode.right is None:
                    result = result + self.listSum(path)
                elif curNode.left is None and curNode.right is not None:
                    newPath = list(path)
                    newPath.append(curNode.right)
                    newLevel.append(newPath)
                elif curNode.left is not None and curNode.right is None:
                    newPath = list(path)
                    newPath.append(curNode.left)
                    newLevel.append(newPath)
                elif curNode.left is not None and curNode.right is not None:
                    newPath1 = list(path)
                    newPath1.append(curNode.left)
                    newPath2 = list(path)
                    newPath2.append(curNode.right)
                    newLevel.append(newPath1)
                    newLevel.append(newPath2)
                levels.remove(levels[0])
                levels.append(newLevel)
        
        return result
        
    def listSum(self,nodes):
        if len(nodes) == 1:
            return nodes[0].val
        
        result = nodes[-1].val
        # adding up all pos except last digit which is calculated above
        for i in range(len(nodes)-1,0,-1):
            result = result + (nodes[len(nodes)-1-i].val)*(10**i)
            
        return result