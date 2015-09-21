class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.val.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        del self.val[0]

    def peek(self):
        """
        :rtype: int
        """
        return self.val[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.val) > 0:
            return False
        return True