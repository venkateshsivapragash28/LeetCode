class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = -len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                if index >= 0 and abs(index - i) <= k:
                    return False
                else:
                    index = i

        return True
