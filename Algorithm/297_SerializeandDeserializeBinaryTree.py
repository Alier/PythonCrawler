'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

DELIMETER = ','

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
            
        listNodes = [root]
        lenAllNodes = 1
        idx = 0 
        while idx < len(listNodes):
            p = listNodes[idx]
            if p is not None:
                listNodes.append(p.left)
                listNodes.append(p.right)
            idx += 1
        
        listVals = []
        for node in listNodes:
            if node is None:
                listVals.append('None')
            else:
                listVals.append(str(node.val))
                
        return DELIMETER.join(listVals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None
        
        listVals = data.split(DELIMETER)
        root = TreeNode(int(listVals[0]))
        listNode = [root] 
        node_idx = 0
        leafs_idx = 1
        while leafs_idx < len(listVals):
            node = listNode[node_idx]
            if node is None:
                node_idx += 1
                continue
            
            leftLeaf_val = listVals[leafs_idx]
            rightLeaf_val = listVals[leafs_idx+1]
            if leftLeaf_val != 'None':
                leftLeaf = TreeNode(int(leftLeaf_val))
            else:
                leftLeaf = None
            if rightLeaf_val != 'None':
                rightLeaf = TreeNode(int(rightLeaf_val))
            else:
                rightLeaf = None
                    
            node.left = leftLeaf
            node.right = rightLeaf
            listNode.append(leftLeaf)
            listNode.append(rightLeaf)
            node_idx += 1
            leafs_idx += 2
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
