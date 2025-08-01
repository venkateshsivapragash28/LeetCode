class Solution(object):
    def subarraySum(self, nums, k):
        # FIRST TRY ----------------------
        # count = 0
        # if arr is None:
        #     print(0)
        # for i in range(len(arr)):
        #     total = 0
        #     for j in range(i, len(arr)):
        #         total = total + arr[j]
        #         if total == k:
        #             count+=1
        # return count
        # FIRST TRY ----------------------

        #2 TRY ------------------------25-07-2025
        # ls = []
        # sum = 0
        # count = 0
        # for i in arr:
        #     sum+=i
        #     ls.append(sum)

        # for i in range(len(ls)):
        #     for j in range(i, len(ls)):
        #         if abs(ls[i] - ls[j]) == k:
        #             count+=1
        # return count
        #3rd Try --------------------------------------
        # i = 0
        # count = 0
        # j = 0
        # summ = 0
        # while j < len(nums):
        #     summ += nums[i]
        #     if summ == k:
        #         count += 1
        #     i += 1
        #     if i == len(nums):
        #         j += 1
        #         i = j
        #         summ = 0
        # return count

        #4th try ----------------------------------------------------

        # nums = [0] + nums
        # summ = 0
        # count = 0
        # prefix = []


        # for i in range(len(nums)):
        #     summ = summ + nums[i]
        #     prefix.append(summ)

        # count = 0
        # for i in range(len(prefix)):
        #     if prefix[i] - k in prefix[:i+1]:
        #         count += 1

        # return count


        #5th try 01 - 07 - 2025

        nums = [0] + nums
        summ = 0
        count = 0
        prefix = []

        for i in range(len(nums)):
            summ = summ + nums[i]
            prefix.append(summ)


        freq = {}

        for p in prefix:
            if p - k in freq:
                count += freq[p - k]

            if p in freq:
                freq[p] += 1
            else:
                freq[p] = 1

        return count