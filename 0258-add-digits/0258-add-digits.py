class Solution(object):
    def addDigits(self, nums):
        sum = 0
        n = len(str(nums))
        while n >= 2:
            sum = 0
            for i in str(nums):
                sum = sum + int(i)
            nums = sum
            n = len(str(nums))
        return nums