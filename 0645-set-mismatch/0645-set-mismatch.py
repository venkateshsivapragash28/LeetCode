class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
                res.append(i)
            else:
                dic[i] = 1

        for i in range(len(nums)):
            if i+1 not in dic:
                res.append(i+1)


        return res





