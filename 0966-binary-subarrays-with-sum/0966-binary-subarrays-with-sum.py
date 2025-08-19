class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sums = {0:1}
        summ = 0
        count = 0
        for i in nums:
            summ = summ + i

            if summ - goal in prefix_sums:
                count += prefix_sums[summ - goal]
            if summ in prefix_sums:
                prefix_sums[summ] += 1
            else:
                prefix_sums[summ] = 1

        return count