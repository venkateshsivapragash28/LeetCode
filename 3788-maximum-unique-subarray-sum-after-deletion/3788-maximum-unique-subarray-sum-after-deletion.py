class Solution(object):
    def maxSum(self, ls):
        ls = set(ls)
        ls = list(ls)
        nums = []
        for i in ls:
            if i > 0:
                nums.append(i)
        if len(nums) == 0:
            return max(ls)
        return sum(nums)