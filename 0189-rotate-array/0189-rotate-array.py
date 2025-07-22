class Solution(object):
    def rotate(self, arr, k):
        if k > len(arr):
            k = k%len(arr)
        arr[:] = arr[-k:] + arr[:-k]
        return arr