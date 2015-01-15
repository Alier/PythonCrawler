# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        
        p = head
        while p.next is not None:
            q = p.next
            if p.val == q.val: # remove q pointed node
                p.next = q.next
            else: 
                p = p.next

        return head