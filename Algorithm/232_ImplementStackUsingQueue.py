class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        del self.stack[len(self.stack)-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return True
        else:
            return False