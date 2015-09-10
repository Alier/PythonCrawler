# Definition for singly-linked list.
#class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        h1 = head
        h2 = head.next
        
        while h2 is not None:
            temp = h2.next
            h2.next = h1
            if h1 is head:
            	h1.next = None
            h1 = h2
            h2 = temp
        
        return h1
        
#n1 = ListNode(1)
#n2 = ListNode(2)

#n1.next = n2
#st = Solution()
#h = st.reverseList(n1)
#while h is not None:
#	print h.val
#	h = h.next
