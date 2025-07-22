class Solution(object):
    def moveZeroes(self, arr):
        for i in range(len(arr)):
            if arr[i] == 0:
                arr.append(arr[i])
                arr.remove(arr[i])
        return arr