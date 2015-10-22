# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
    
        # only two element
        if head.next.next is None:
            if head.val > head.next.val:
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
            return head
            
        biggest = head
        p = head.next
        while(p):
            if p.val >= biggest.val:
                biggest = p
                p = p.next
            else: # p.val < biggest.val
                biggest.next = p.next
                if p.val <= head.val: # insert to the very front
                    p.next = head
                    head = p
                else: # p.val between head, and biggest
                    q = head
                    while (q.next.val < p.val):
                        q = q.next
                    
                    # between q and q.next is where p should insert to
                    p.next = q.next
                    q.next = p
                    
                p = biggest.next    
                
        return head