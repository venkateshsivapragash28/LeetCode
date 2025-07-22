class Solution(object):
    def check(self, arr):
        for i in range(len(arr)-1):
            if arr[i] <= arr[i+1]:
                continue
            else:
                arr = arr[i+1:] + arr[:i+1]
        for i in range(len(arr)- 1):
            if arr[i] <= arr[i+1]:
                continue
            else:
                return False
        return True