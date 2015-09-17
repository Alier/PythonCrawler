# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
            
        p1 = head
        p2 = head.next
        while p2 != p1 and p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        
        if p2 is None:
            return None
        
        if p2.next is None:
            return None
            
        if p2 == p1 : # p1 is pointing at one node on the ring
            count = 1
            while p2.next != p1:
                p2 = p2.next
                count += 1
            
            if count == 1:
                return p1
            else:
                p1 = head
                p2 = head
                # make p2 point to a node with count distance from p1
                for i in range(0,count):
                    p2 = p2.next
                while p2 != p1:
                    p1 = p1.next
                    p2 = p2.next
                
                return p1