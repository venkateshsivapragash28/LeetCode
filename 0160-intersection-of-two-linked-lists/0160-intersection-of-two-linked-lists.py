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
        seen = set()
        current = headA
        while current:
            seen.add(current)
            current = current.next
        
        current = headB
        while current:
            if current in seen:
                return current
            current = current.next
        return None