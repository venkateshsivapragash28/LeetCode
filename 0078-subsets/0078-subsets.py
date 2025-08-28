class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(0, (2 ** len(nums))):
            x = bin(i)[2:].zfill(len(nums))
            z = []
            for j in range(len(str(x))):
                if x[j] == '1':
                    z.append(nums[j])
            arr.append(z)

        return arr