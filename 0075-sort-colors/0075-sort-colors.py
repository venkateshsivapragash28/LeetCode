class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = 0
        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count0+=1
            elif nums[i] == 1:
                count1+=1
            else:
                count2 += 1
                
        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0+count1):
            nums[i] = 1
        for i in range(count0+count1, count0+count1+count2):
            nums[i] = 2

        return nums