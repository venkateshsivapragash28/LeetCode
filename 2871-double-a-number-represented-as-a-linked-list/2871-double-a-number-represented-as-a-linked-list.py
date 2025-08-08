# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        values = ''
        current = head
        while current:
            values = values + str(current.val)
            current = current.next
        values = str(int(values)*2)
        head = ListNode(int(values[0]))
        current = head
        for i in values[1:]:
            current.next = ListNode(int(i))
            current = current.next
        
        return head