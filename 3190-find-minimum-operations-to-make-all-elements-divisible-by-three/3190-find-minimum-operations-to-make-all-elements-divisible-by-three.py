class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            i = i % 3
            if i != 0:
                count += 1

        return count