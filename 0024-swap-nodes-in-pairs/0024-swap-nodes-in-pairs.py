# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        first = head

        while first and first.next:

            second = first.next
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
            first = prev.next

        return dummy.next
