class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        if min(nums) > 1:
            return 1
        if max(nums) < 1:
            return 1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] > 0 :
                if (nums[i + 1] - nums[i]) > 1:
                    return nums[i] + 1
        return nums[-1] + 1