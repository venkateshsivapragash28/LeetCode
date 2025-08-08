# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        arr = []
        current = head
        summ = 0
        while current and current.next:
            if current.next.val != 0:
                summ = summ + current.next.val
            else:
                arr.append(summ)
                summ = 0
            current = current.next
        
        head = ListNode(arr[0])
        current = head
        for i in arr[1:]:
            current.next = ListNode(i)
            current = current.next
        return head
