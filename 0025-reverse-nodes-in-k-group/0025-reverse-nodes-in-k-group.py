# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            current = head

            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            return prev


        dummy = ListNode(0)
        temp = dummy
        dummy.next = head

        while True:
            kth = temp
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_node = kth.next
            kth.next = None
            new_head = reverse(temp.next)

            old_head = temp.next
            temp.next = new_head
            old_head.next = next_node

            temp = old_head

            
