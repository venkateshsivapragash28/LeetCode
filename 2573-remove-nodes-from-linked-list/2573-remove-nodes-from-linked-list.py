# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        res = []
        current = head
        while current:
            res.append(current.val)
            current = current.next

        stack = []
        for i in range(len(res)-1, -1, -1):
            if not stack:
                stack.append(res[i])
            elif res[i] >= stack[-1]:
                stack.append(res[i])
        stack = stack[::-1]
        head = ListNode(stack[0])
        current = head
        for i in stack[1:]:
            current.next = ListNode(i)
            current = current.next

        return head

