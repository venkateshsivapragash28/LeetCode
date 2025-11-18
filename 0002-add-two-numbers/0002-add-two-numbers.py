# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        current = l1
        while current:
            str1 += str(current.val)
            current = current.next
        str1 = str1[::-1]
        str2 = ''
        current = l2
        while current:
            str2 += str(current.val)
            current = current.next
        str2 = str2[::-1]
        res = str(int(str1) + int(str2))[::-1]

        if len(res) == 0:
            return ListNode(0)
        l3 = ListNode(int(res[0]))
        res = res[1:]
        current = l3
        for i in res:
            current.next = ListNode(int(i))
            current = current.next

        return l3