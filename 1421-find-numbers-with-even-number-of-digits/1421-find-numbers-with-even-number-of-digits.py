class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            num = str(num)
            if len(num)%2 == 0:
                count +=1
        return count


        