# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        if arr[::-1] == arr:
            return True 
        else:
            return False            

        