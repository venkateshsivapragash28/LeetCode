class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        counter = {}
        max_element = 0
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for i in nums:
            if counter[i] > maxi:
                maxi = counter[i]
                max_element = i
        return max_element

