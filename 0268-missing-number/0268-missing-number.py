class Solution(object):
    def missingNumber(self, arr):
        
        maximum = max(arr)
        actual_sum = 0
        arr_sum = 0
        for i in range(len(arr)+1):
            actual_sum = actual_sum + i
        for i in range(len(arr)):
            arr_sum = arr_sum + arr[i]

        return abs(actual_sum - arr_sum)