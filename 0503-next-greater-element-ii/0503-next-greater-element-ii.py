class Solution(object):
    def nextGreaterElements(self, arr):

        new = [0]* len(arr)
        stack = [float('-inf')]
        for i in range(2*len(arr)-1, -1, -1):
            current = i%len(arr)
            while stack and stack[-1] <= arr[current]:
                stack.pop()
            if stack and stack[-1] > arr[current]:
                new[current] = stack[-1]
            else:
                new[current] = -1
            stack.append(arr[current])
        
        return new


