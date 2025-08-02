class Solution(object):
    def findLHS(self, nums):
        
        frequency = Counter(nums)
        len = 0

        for i in frequency:
            if i+1 in frequency:
                len  = max(len, frequency[i] + frequency[i+1])
        return len