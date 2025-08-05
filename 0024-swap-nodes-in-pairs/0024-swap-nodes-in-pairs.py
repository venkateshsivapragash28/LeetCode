# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, A):
        dummy = ListNode(0)
        dummy.next = A
        prev = dummy
        while A and A.next:
            first = A
            second = A.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            A = first.next
        return dummy.next