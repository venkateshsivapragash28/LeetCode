class Solution(object):
    def searchMatrix(self, arr, target):
        i = 0
        j = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == target:
                    return True
        return False