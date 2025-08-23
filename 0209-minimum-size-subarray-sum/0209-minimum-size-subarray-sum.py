class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i = 0
        j = 0
        kootal = 0
        mini_len = float('inf')
        while i < len(nums) and j < len(nums):
            kootal = kootal + nums[j]

            while kootal >= target:
                mini_len = min(mini_len, j - i)
                kootal = kootal - nums[i]
                i += 1
            j += 1

        if mini_len < float('inf'):
            return mini_len + 1
        else:
            return 0