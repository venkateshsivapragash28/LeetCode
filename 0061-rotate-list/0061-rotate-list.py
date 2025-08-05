# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def find_tail(head):
            current = head
            while current:
                if current.next == None:
                    return current 
                current = current.next

        if not head or not head.next or k == 0:
            return head 
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k = k % length
        if k == 0:
            return head
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail = find_tail(new_head)
        tail.next = head

        return new_head

        