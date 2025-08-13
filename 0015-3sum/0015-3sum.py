class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # res = []

        # for i in range(len(nums)):
        #     left = i+1
        #     right = len(nums)-1
        #     while left < right:
        #         if nums[i] + nums[left] + nums[right] == 0:
        #             if [nums[i], nums[left], nums[right]] not in res:
        #                 res.append([nums[i], nums[left], nums[right]])
        #             right -= 1
        #             left += 1
        #         elif nums[i] + nums[left] + nums[right] > 0:
        #             right -= 1
        #         elif nums[i] + nums[left] + nums[right] < 0:
        #             left += 1

        # return res

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left+=1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

        return res