# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        ls = []
        current = head
        while current:
            ls.append(current.val)
            current = current.next

        if len(ls) <= 2:
            return [-1,-1]

        res = []

        for i in range(1,len(ls) - 1):
            if ls[i-1] < ls[i] > ls[i+1]:
                res.append(i+1)
            elif ls[i-1] >ls[i] < ls[i+1]:
                res.append(i+1)

        if len(res) <= 1:
            return [-1, -1]

        minima = float('inf')
        for i in range(len(res)-1):
            minima = min(minima, abs(res[i] - res[i+1]))
                
        return [minima, abs(res[0]- res[-1])]