class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = (left + right) // 2
            if mid == 0:
                if len(nums) == 1 or nums[mid] > nums[mid+1]:
                    return mid 
                else:
                    left = mid + 1

            if mid == len(nums) -1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1
            
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
                