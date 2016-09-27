'''
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        lastp = None
        p = head
        pn = p
        dup = False
        while pn.next is not None:
            if pn.next.val == p.val:
                pn = pn.next
                dup = True
            else:
                if dup:# nodes p to pn (inclusive) needs to be deleted
                    if lastp is None:
                        head = pn.next
                    else:
                        lastp.next = pn.next
                    dup = False
                else:
                    lastp = p 
                p = pn.next
                pn = p

        if dup: # nodes p to pn (inclusive) needs to be deleted
            if lastp is None:
                head = pn.next
            else:
                lastp.next = pn.next
            
        return head
