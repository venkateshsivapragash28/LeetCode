class Solution(object):
    def isArraySpecial(self, nums):
        def sub(a, b):
            return abs(a-b)

        i = 0
        temp = 1
        if len(nums) == 1:
            return True


        while i < len(nums)-1:
            if sub(nums[i], nums[i+1]) % 2 == temp:
                i+=1
            else:
                return False
        return True