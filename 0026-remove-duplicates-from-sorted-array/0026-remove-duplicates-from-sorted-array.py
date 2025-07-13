class Solution(object):
    def removeDuplicates(self, nums):
        unique = []
        for i in nums:
            if i not in unique:
                unique.append(i)
        for i in range(len(unique)):
            nums[i] = unique[i]
        return len(unique)