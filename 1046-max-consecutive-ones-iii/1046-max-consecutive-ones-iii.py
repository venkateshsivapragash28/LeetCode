class Solution(object):
    def longestOnes(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right= 0 
        zero = 0
        maxi = 0
        while left < len(arr) and right < len(arr):
            if arr[right] == 0:
                zero += 1
            while zero > k:
                if arr[left] == 0:
                    zero -= 1
                left += 1
            
            maxi = max(maxi, right - left + 1)
            right += 1
        return maxi