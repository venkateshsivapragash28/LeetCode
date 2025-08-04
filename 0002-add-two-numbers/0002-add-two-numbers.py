# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        digit = ''
        current = l1
        while current:
            digit = digit + str(current.val)
            current = current.next

        digit1 = ''
        current = l2
        while current:
            digit1 = digit1 + str(current.val)
            current = current.next
        digit = str(digit[::-1])
        digit1 = str(digit1[::-1])
        res = str(int(digit) + int(digit1))
        res = res[::-1]
        dummy = ListNode(0)
        current = dummy
        for i in str(res):
            current.next = ListNode(int(i))
            current = current.next
        result = dummy.next

        return result
        