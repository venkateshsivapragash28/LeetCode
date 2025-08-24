class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                res.append(abs(i))
            else:
                nums[index] = -nums[index]
        return res