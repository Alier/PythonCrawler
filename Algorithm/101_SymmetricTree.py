# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# this is iterative solution
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None :
            return True
        
        # no left/right child
        if root.left is None and root.right is None:
            return True
        
        # only left or right child tree
        if root.left is None and root.right is not None or root.right is None and root.left is not None:
            return False
          
        # both left and right tree
        st = list()
        st.append(root.left)
        st.append(root.right)
        
        while len(st) > 0:
            curLen = len(st)
            if self.isMirror(st) is False:
                return False
            else: # add each node's left/right child in sequence into the list and remove the root node investigated already
                for i in range(0,curLen):
                    curNode = st[i]
                    if curNode is not None:
                        st.append(curNode.left)
                        st.append(curNode.right)
                st = st[curLen:]
                
        return True
        
    #return True if nodes list is symmetrial for the nodes on same level, like [1], [2,2] or [3,4,4,3]
    def isMirror(self, nodes):
        n = len(nodes)
        if n % 2 == 1: # if n is not multiple of 2, has to be asymmetric
            return False
        
        i = 0
        j = n-1
        
        # compare pair nodes: i and j
        while i < j:
            if self.equalNode(nodes[i],nodes[j]) is False:
                return False
            i = i + 1
            j = j - 1
            
        return True
    
    def equalNode(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        
        if node1 is not None and node2 is not None and node1.val == node2.val:
            return True
        
        return False