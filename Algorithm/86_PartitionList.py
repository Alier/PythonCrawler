#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

#You should preserve the original relative order of the nodes in each of the two partitions.

#For example,
#Given 1->4->3->2->5->2 and x = 3,
#return 1->2->2->4->3->5.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        lastSmall = None

        if head.val < x:
            lastSmall = head
        
        p = head
        while p.next:
            if p.next.val < x:
                if p == lastSmall:
                    lastSmall = p.next
                    p = p.next
                    continue
                
                # delete from current position
                nodeToMove = p.next
                p.next = nodeToMove.next
                if lastSmall is None: # head >= x
                    #insert before firstLarge
                    lastSmall = nodeToMove
                    lastSmall.next = head
                    head = lastSmall
                else: # lastSmall is not None
                    nodeToMove.next = lastSmall.next
                    lastSmall.next = nodeToMove
                    lastSmall = nodeToMove
            else:
                p = p.next
    
        return head
        

                