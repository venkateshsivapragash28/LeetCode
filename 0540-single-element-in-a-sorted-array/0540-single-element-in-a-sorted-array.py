class Solution(object):
    def singleNonDuplicate(self, nums):
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if (mid == 0  or nums[mid] != nums[mid-1]) and (mid == len(nums)-1 or nums[mid+1] != nums[mid]):
                return nums[mid]

            elif nums[mid] == nums[mid+1]:
                if mid%2 != 0:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if mid%2 != 0:
                    left = mid + 1
                else:
                    right = mid - 1