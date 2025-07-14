class Solution(object):
    def sortArrayByParity(self, nums):
        odd = []
        even = []
        if len(nums) == 1 and nums[0] == 0:
            return [0]
        else:
            for i in nums:
                if i%2 != 0:
                    odd.append(i)
                else:
                    even.append(i)
            return even+odd
