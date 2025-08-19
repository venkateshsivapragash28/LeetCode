class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        nums = nums + [1]
        count = 1
        summ = 0
        for i in range(len(nums)-1):
            if nums[i] == 0 and nums[i+1] == 0:
                count+=1
            elif nums[i] ==0 and nums[i+1] != 0:
                x = (count * (count + 1)) // 2
                summ = summ + x
                count = 1

        return summ