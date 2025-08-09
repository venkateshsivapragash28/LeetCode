class Solution(object):
    def nextGreaterElement(self, nums, arr):
        new = [0]* len(arr)
        stack = [float('-inf')]
        for i in range(len(arr)-1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack and stack[-1] > arr[i]:
                new[i] = stack[-1]
            else:
                new[i] = -1
            stack.append(arr[i])

        final = []

        for i in nums:
            idx = arr.index(i)
            final.append(new[idx])

        return final