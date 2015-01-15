# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        # set two pointers, one increase 1 each time, and one increase 2 each time. the faster one would be pointing to the slower one if there is a loop
        if head is None or head.next is None or head.next.next is None:
            return False
        
        i = head
        j = head
        
        while i.next is not None and j.next is not None and j.next.next is not None:
            i = i.next
            j = j.next.next
            if j == i :
                return True
        
        return False
            