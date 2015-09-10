# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        Next = head.next
        if Next.next is None:
            Next.next = head
            head.next = None
            return Next
            
        newHead = self.reverseList(head.next)
        head.next = None
        
        p = newHead.next
        while p is not None:
            tail = p
            p = p.next
            
        tail.next = head
        
        return newHead