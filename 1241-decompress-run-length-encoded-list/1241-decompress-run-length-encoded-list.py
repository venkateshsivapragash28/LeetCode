class Solution(object):
    def decompressRLElist(self, nums):
        arr = []

        for i in range(0, len(nums), 2):
            val = nums[i+1]
            freq = nums[i]
            arr.extend([val]*freq)
        return arr