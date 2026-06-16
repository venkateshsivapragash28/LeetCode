class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        mx = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                mx = max(mx, count)
                count = 0
        mx = max(count, mx)

        return mx