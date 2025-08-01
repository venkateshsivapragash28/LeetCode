class Solution(object):
    def largestNumber(self, nums):
        arr = [str(x) for x in nums]
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] < arr[j] + arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]

        res = "".join(arr)
        return '0' if res[0] == '0' else res