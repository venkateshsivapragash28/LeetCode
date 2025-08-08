# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        current = head
        while current:
            if current.val in nums:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next

        return dummy.next        

        