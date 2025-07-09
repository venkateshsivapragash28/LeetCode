class Solution(object):
    def findSpecialInteger(self, arr):
        i = 0
        count = 1
        max_count = 1
        element = arr[0]
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                count = count + 1
            else:
                count = 1
            if count > max_count:
                max_count = count
                element = arr[i]
        return element


