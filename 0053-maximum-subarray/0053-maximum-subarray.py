class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float('-inf')
        summ = 0
        for i in nums:
            summ += i
            if summ > mx:
                mx = summ
            if summ < 0:
                summ = 0

        return mx