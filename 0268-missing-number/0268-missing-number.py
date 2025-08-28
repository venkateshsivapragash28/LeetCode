class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_all = 0
        xor_missing = 0
        for i in nums:
            xor_all ^= i
        for i in range(len(nums)):
            xor_missing ^= i

        return xor_all ^ xor_missing ^ len(nums)