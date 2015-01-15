# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        
        p = head
        while p is not None and p.next is not None:
            temp = p.val
            p.val = p.next.val
            p.next.val = temp
            
            p = p.next.next
        
        return head
       