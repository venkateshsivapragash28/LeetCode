class Solution(object):
    def findMaxAverage(self, nums, k):
        current = sum(nums[:k])
        best = current*1.0 / k
        for i in range(k,len(nums)):
            current = current + nums[i] - nums[i-k]
            best = max(best, current*1.0/k)
        return best