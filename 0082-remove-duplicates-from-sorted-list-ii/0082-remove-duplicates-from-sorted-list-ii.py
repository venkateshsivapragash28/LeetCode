# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head

        dick = {}
        current = head
        while current:
            if current.val in dick:
                dick[current.val] += 1
            else:
                dick[current.val] = 1
            current = current.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = prev.next
        while current:
            if dick[current.val] >= 2:
                prev.next = current.next
                current = prev.next
            else:
                prev = prev.next
                current = current.next

        return dummy.next