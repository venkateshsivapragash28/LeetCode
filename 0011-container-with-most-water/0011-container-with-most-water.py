class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        maxi = 0
        right = len(height) - 1
        while left < right:
            maxi = max(maxi, (min(height[left], height[right]) * (right-left)))
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1

            else:
                left += 1
                right -= 1

        return maxi