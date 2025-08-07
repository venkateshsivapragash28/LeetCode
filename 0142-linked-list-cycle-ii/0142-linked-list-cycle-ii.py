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
        seen = set()
        current = head
        while current:
            if current in seen:
                return current
            else:
                seen.add(current)
            current = current.next
        return None

        # seen = set()
        # current = head
        # while current:
        #     seen.add(current)
        #     current = current.next
        
        # current = head
        # while current:
        #     if current in seen:
        #         return current
        #     current = current.next
        # return False