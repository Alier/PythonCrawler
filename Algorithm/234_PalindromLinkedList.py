'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
            
        tempList = list()
        p = head
        while p is not None:
            tempList.append(p.val)
            p = p.next
            
        numElems = len(tempList)
        forward = 0
        backward = len(tempList)-1
        
        while forward < backward:
            if tempList[forward] != tempList[backward]:
                return False
            else:
                forward += 1
                backward -= 1
                
        return True
