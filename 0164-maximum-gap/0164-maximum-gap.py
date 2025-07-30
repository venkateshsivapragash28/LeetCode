class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        else:
            nums.sort() 
            diff = 0
            max_diff = 0
            for i in range( len(nums)-1):
                diff = nums[i+1] - nums[i]
                if diff > max_diff:
                    max_diff = diff
            return max_diff
