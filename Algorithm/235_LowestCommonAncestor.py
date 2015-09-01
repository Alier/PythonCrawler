# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root is None or p is None or q is None:
            return root
        
        # p,q not on same subtree. Root would be the lowest common ancestor
        if ( p.val <= root.val and q.val >= root.val ) or (q.val <= root.val and p.val >= root.val) :
            return root
            
        # both at left sub tree    
        if ( p.val < root.val and q.val < root.val ) :
            return self.lowestCommonAncestor(root.left, p, q)
        
        # both at right sub tree
        if (p.val > root.val and q.val > root.val) :
            return self.lowestCommonAncestor(root.right, p, q)
            