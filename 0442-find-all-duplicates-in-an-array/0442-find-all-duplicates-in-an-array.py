class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = {} 
        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i] = 1
        res = []
        for i in set(nums):
            if counter[i] == 2:
                res.append(i)

        return res