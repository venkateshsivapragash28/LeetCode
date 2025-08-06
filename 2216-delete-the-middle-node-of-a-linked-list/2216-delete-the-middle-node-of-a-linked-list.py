# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        if head.next is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        slow = head
        fast = head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next

        return head