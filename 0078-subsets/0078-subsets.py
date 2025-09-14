class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Using Bit Manipulation !!!
        #----------------------------- !!!!
        # arr = []
        # for i in range(0, (2 ** len(nums))):
        #     x = bin(i)[2:].zfill(len(nums))
        #     z = []
        #     for j in range(len(str(x))):
        #         if x[j] == '1':
        #             z.append(nums[j])
        #     arr.append(z)

        # return arr
        #----------------------------- !!!!

        # Using recursion ------------------------------------ !!!! fuck youself behehe
        res = []
        n = len(nums)
        def f(index, li):

            if index >= n:
                res.append(li[:])
                return
            
            li.append(nums[index])

            f(index + 1, li)

            li.pop()

            f(index + 1, li)

        f(0, [])

        return res