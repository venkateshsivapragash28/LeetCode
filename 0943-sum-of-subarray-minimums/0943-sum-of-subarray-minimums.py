class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        new = [0]* len(arr)
        stack = []
        new2 = [0]* len(arr)
        stack2 = []

        for i in range(len(arr)-1, -1, -1):
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if stack:
                new[i] = stack[-1][1] - i
            else:
                new[i] = len(arr) - i
            stack.append([arr[i],i])


        for i in range(len(arr)):
            while stack2 and stack2[-1][0] > arr[i]:
                stack2.pop()
            if stack2:
                new2[i] = i - stack2[-1][1]
            else:
                new2[i] = i+1
            stack2.append([arr[i],i])

        res = 0
        for i in range(len(arr)):
            res = (res + (arr[i] * new[i] * new2[i])) % mod
        
        return res