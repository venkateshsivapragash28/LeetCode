class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # flag = False
        # flag2 = False

        # for i in range(len(nums) - 2):
        #     if nums[i] < nums[i + 1] < nums[i + 2]:
        #         flag = True

        # nums.sort()
        # for i in range(len(nums) - 2):
        #     if nums[i] < nums[i + 1] < nums[i + 2]:
        #         flag2 = True

        # if flag == True or flag2 == True:
        #     return True
        
        # return False
        
        first = float('inf')
        second = float('inf')

        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False