# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m == n:
            return head
        
        p = head
        i = 1
        pointers = [None]
        while i <= n:
            pointers.append(p)
            p = p.next
            i += 1
        
        # exchange m and n:
        while m != n and m!= n+1:
            pM = pointers[m]
            pN = pointers[n]
            temp = pM.val
            pM.val = pN.val
            pN.val = temp
            m += 1
            n -= 1
        
        return head
        