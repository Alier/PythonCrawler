# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # from node on, move every node forward one spot, and remove the tail
        if node is None or node.next is None:
            return
        
        while node.next.next:
            node.val = node.next.val
            node = node.next
        
        # node.next.next is None, which means node.next is Tail
        node.val = node.next.val
        node.next = None
        
        return 
        
        