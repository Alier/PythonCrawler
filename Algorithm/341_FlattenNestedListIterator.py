'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.index = [] # list of indexs from outer to inner lists
        if  len(nestedList) > 0:
            temp = nestedList[0]
            self.index.append(0)
            while not temp.isInteger():
                temp = temp.getList()[0]
                self.index.append(0)

    def next(self):
        """
        :rtype: int
        """
        possibleNexts = []
        temp = self.nestedList
        for i in xrange(len(self.index)):
            elemIndexThisLayer = self.index[i]
            if elemIndexThisLayer < len(temp):
                possibleNexts.append(self.index[:i] + [elemIndexThisLayer+1])
            temp = temp[self.index[i]] 
        
        #next would be possibleNexts[-1] as it's deepest
        nextIndex = possibleNexts[-1]
        temp = self.nestedList
        for idx in nextIndex:
            temp = temp[idx]
        
        while not temp.isInteger():
            temp = temp[0]
            nextIndex.append(0)
        
        return temp.getInteger()
         
    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.index) == 0:
            return False
            
        if self.index[0] < len(self.nestedList)-1:
            return True
        
        temp = self.nestedList
        for i in xrange(len(self.index)-1): 
            idx = self.index[i]
            temp = temp[idx]
            elemIndexThisLayer = self.index[i+1]
            if elemIndexThisLayer < len(temp)-1:
                return True
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
