class Solution(object):
    def minSubArrayLen(self, target, nums):
       
       
        summ = 0
        i = 0
        j = 0
        max_len = float('inf')
        while j < len(nums):
            summ = summ + nums[j]

            while summ >= target:
                max_len = min(max_len, (j - i) + 1)
                summ = summ - nums[i]
                i += 1
            j += 1 

        return max_len if max_len != float('inf') else 0