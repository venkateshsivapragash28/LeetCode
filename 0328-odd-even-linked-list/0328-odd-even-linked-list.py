# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        odd = head
        even_head = head.next
        current = head.next
        while current and current.next:
            temp = current.next
            current.next = temp.next
            odd.next = temp
            temp.next = even_head
            odd = odd.next
            current = current.next
        
        return head

