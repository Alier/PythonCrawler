'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # reverse just k length linked-list starting with head
    # return (newhead, newtail, next k head)
    def reverseK(self, head, k):
        p = head
        count = 1
        while p.next is not None:
            p = p.next
            count += 1
        
        if count < k:# should use original, tail is p
            return (head, p, None)
        
        newHead = head
        count = 1
        p = head.next
        head.next = None
        while p is not None and count < k:
            count += 1
            temp = p.next
            p.next = newHead
            newHead = p
            p = temp

        return (newHead, head, p)
            
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        if k == 1:
            return head
            
        newHead, curTail, nextStart = self.reverseK(head, k)
        
        while nextStart is not None:
            nextHead, nextTail, nextnextStart = self.reverseK(nextStart, k)
            curTail.next = nextHead
            curTail = nextTail
            nextStart = nextnextStart
    
        return newHead
        
