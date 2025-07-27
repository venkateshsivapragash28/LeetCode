class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1 and target != nums[0]:
            return [-1,-1]
        arr = []
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
                break
        if not arr:
            arr.append(-1)
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                arr.append(i)
                break
        if len(arr) == 1:
            arr.append(-1)
        
        return arr