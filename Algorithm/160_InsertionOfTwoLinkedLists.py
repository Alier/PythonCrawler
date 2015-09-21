# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        #A only one node and B only one node
        if headA.next is None and headB.next is None:
            if headA != headB:
                return None
            return headA
        
        #A only one node
        if headA.next is None and headB.next is not None:
            p = headB
            while p != headA and p:
                p = p.next
            if p is None:
                return None
            return p
        
        #B only one node
        if headB.next is None and headA.next is not None:
            p = headA
            while p != headB and p:
                p = p.next
            if p is None:
                return None
            return p
        
        #A,B both have >= 2 nodes    
        #find tail first
        p = headA
        nodeCounts = 1
        while p.next:
            p = p.next
            nodeCounts += 1
        
        tail = p
        
        #connect this to headA to make a loop, the loop's length == A's nodeCounts
        p.next = headA
        
        #now this is a linkedlist with headB with cycle starting at the intersection. find the intersection
        p = headB
        q = p # point q to nodeCounts distance from p , so when p reaches intersection, q should be == p
        distance = nodeCounts
        while q is not None and distance != 0:
            q = q.next
            distance -= 1
       
        if q is None:
            tail.next = None
            return None
            
        while q is not None and p != q:
            p = p.next
            q = q.next
        
        if q is None:
            tail.next = None
            return None
            
        #remove cycle 
        tail.next = None
        return p
        
        
        
        
        