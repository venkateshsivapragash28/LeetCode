# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        listu = []
        for i in lists:
            current = i
            while current:
                listu.append(current.val)
                current = current.next
        listu.sort()
        if listu:
            head = ListNode(listu[0])
            current = head
            for i in listu[1:]:
                current.next = ListNode(i)
                current = current.next

            return head