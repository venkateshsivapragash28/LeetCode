class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # prefix = {0:1}
        # summ = 0
        # count = 0

        # for i in range(len(nums)):

        #     summ = summ + nums[i] % 2

        #     if summ - k in prefix:
        #         count += prefix[summ - k]
        #     if summ in prefix:
        #         prefix[summ]+= 1
        #     else:   
        #         prefix[summ] = 1

        # return count



        summ = 0
        prefix = {0:1}
        count = 0

        for i in nums:

            summ = summ + i % 2

            if summ - k in prefix:
                count += prefix[summ - k]
            if summ in prefix:
                prefix[summ] += 1
            else:
                prefix[summ] = 1


        return count

























