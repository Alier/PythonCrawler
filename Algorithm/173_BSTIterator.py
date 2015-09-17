class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root is not None:
            self.stack.append(root)
            leftRoot = root.left
            while leftRoot is not None:
                self.stack.append(leftRoot)
                leftRoot = leftRoot.left
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return False
            
        return True

    def next(self):
        """
        :rtype: int
        """
        curNode = self.stack[-1]
        del self.stack[-1]

        rightRoot = curNode.right
        while rightRoot is not None:
            self.stack.append(rightRoot)
            rightRoot = rightRoot.left
            
        return curNode.val
