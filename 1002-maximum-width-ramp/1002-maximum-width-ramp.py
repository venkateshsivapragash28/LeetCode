class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        stack = [[nums[0], 0]]
        for i in range(len(nums)):       
            if stack and stack[-1][0] > nums[i]:
                stack.append([nums[i], i])

        maxi = 0
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] >= stack[-1][0]:
                maxi = max(maxi, (i - stack[-1][1]))
                stack.pop()

        return maxi