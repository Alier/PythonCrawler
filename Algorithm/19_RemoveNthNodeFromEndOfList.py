# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        
        if head.next is None and n == 1:
            return None
            
        p = head
        q = p
        for i in range(0,n):
            q = q.next
        
        # q already pointing beyond the list, then p is the head to be removed, given that n is always valid
        if q is None:
            return p.next
        
        while q.next is not None:
            p = p.next
            q = q.next
    
        #p is pointing to the one element before right element
        toRemove = p.next
        p.next = toRemove.next
        
        return head