class Solution(object):
    def dailyTemperatures(self, arr):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        new = [0]* len(arr)
        stack = [[float('-inf'), -1]]

        for i in range(len(arr)-1, -1, -1):
            while stack and stack[-1][0] <= arr[i]:
                stack.pop()
            if stack and stack[-1][0] > arr[i]:
                new[i] = abs(i - stack[-1][1])
            else:
                new[i] = 0
            stack.append([arr[i], i])

        return new