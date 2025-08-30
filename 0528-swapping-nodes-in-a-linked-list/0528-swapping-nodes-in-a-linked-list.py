# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        res = []
        current = head
        while current:
            res.append(current.val)
            current = current.next
        
        res[k-1], res[-k] = res[-k], res[k-1]
        head = ListNode(res[0])
        current = head
        for i in res[1:]:
            current.next = ListNode(i)
            current = current.next

        return head
