class Solution(object):
    def twoSum(self, nums, target):
        dick = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dick:
                return [dick[diff],i]
            else:
                dick[num] = i
        