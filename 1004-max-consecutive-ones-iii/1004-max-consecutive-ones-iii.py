class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # i = 0
        # j = 0
        # maxi = float('-inf')
        # zero_count = 0
        # while i < len(nums) and j < len(nums):
        #     if zero_count <= k:
        #         if nums[j] == 0:
        #             zero_count += 1
        #     j+=1
        #     while zero_count > k:
        #         if nums[i] == 0:
        #             zero_count -= 1
        #         i+=1
        #     maxi = max(maxi, (j - i))
        # return maxi


        i = 0
        j = 0
        zero = 0
        max_count = float('-inf')
        while i < len(nums) and j < len(nums):
            if nums[j] == 0 and zero <= k:
                zero += 1
            j += 1

            
            while zero > k:
                if nums[i] == 0:
                    zero -= 1
                i += 1
            max_count = max(max_count, (j - i))

        return max_count


