# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        count = 0
        current = list1
        while current:
            if count == a-1:
                first_node = current
            elif count == b:
                second_node = current.next
                break
            count+=1
            current = current.next

        current = list2
        while current and current.next:
            current = current.next
        tail = current

        tail.next = second_node
        first_node.next = list2

        return list1
            
        