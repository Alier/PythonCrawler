# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None or head.next is None and head.val == val:
            return None
        
        while head is not None and head.val == val:
            head = head.next
        
        if head is None:
            return None
            
        p = head    
        while p is not None and p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        
        return head