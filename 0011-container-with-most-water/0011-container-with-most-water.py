class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) - 1
        left = 0
        right = n
        volume = 0
        while left < right:
            x = min(height[left], height[right])
            volume = max(volume, x*(n))
            if height[left] < height[right]:
                left += 1
                n = n-1
            elif height[right] < height[left]:
                right -= 1
                n = n-1
            else:
                left += 1
                right -= 1
                n = n-2 
        return volume
