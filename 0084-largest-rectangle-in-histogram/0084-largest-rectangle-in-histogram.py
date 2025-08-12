class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nextt = [0]*len(heights)
        stack = []
        prev = [0]*len(heights)
        maxi = 0
        for i in range(len(heights)-1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack and stack[-1][0] < heights[i]:
                nextt[i] = stack[-1][1] - i
            else:
                nextt[i] = len(heights) - i
            stack.append([heights[i],i])


        stack.clear()
        for i in range(len(heights)):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack and stack[-1][0] < heights[i]:
                prev[i] = i - stack[-1][1] - 1
            else:
                prev[i] = i
            stack.append([heights[i], i])

        for i in range(len(heights)):
            x = (nextt[i] + prev[i]) * heights[i]
            maxi = max(maxi, x)

        return maxi