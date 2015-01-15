# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
            
        p1 = l1
        p2 = l2
        
        head = l1
        if l1.val > l2.val:
            head = l2
        
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                if p1.next is None:
                    p1.next = p2
                    return head
                else: #p1.next is not None
                    if p1.next.val <= p2.val:
                        p1 = p1.next
                    else: #p1.next > p2.val, insert p2 after p1, move p1 to p1.next
                        temp = p1.next 
                        p1.next = p2
                        p1 = temp 
            else: #p1.val > p2.val
                if p2.next is None:
                    p2.next = p1
                    return head
                else: #p2.next is not None
                    if p1.val > p2.next.val:
                        p2 = p2.next
                    else: # p1.val <= p2.next.val, insert p1 after p2, move p2 to p2.next
                        temp = p2.next
                        p2.next = p1
                        p2 = temp
      
        return head
                
                