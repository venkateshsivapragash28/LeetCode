# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        arr.sort()
        new = ListNode(0)
        current = new
        for i in arr:
            current.next = ListNode(i)
            current = current.next
        
        return new.next
