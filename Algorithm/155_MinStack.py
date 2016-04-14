'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

'''
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minV = 0
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if(len(self.stack) == 1):
            self.minV = x
        elif x < self.getMin():
            self.minV = x
            
    def pop(self):
        """
        :rtype: nothing
        """
        topV = self.top()
        # if remove the smallest need to get next smallest
        del self.stack[-1]
        if topV == self.minV and len(self.stack) > 0:
            self.minV = sorted(self.stack)[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minV
