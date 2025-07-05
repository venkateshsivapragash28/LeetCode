class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        while current:
            t = current.next
            current.next = prev
            prev = current
            current = t
        return prev