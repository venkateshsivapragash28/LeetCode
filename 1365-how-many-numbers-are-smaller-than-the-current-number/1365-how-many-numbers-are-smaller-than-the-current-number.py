class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = nums.copy()
        sorted_nums.sort()
        rank = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in rank:
                rank[sorted_nums[i]] = i

        output = []
        for i in range(len(nums)):
            output.append(rank[nums[i]])

        return output


