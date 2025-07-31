class Solution(object):
    def insert(self, arr, new):

        arr = arr + [new]
        arr.sort()

        i = 0
        while i < len(arr)-1:
            if arr[i][1] >= arr[i+1][0] and arr[i][1] <= arr[i+1][1]:
                arr[i] = [arr[i][0], arr[i+1][1]]
                arr.remove(arr[i+1])
            elif arr[i][1] >= arr[i+1][0] and arr[i][1] >= arr[i+1][1]:
                arr.remove(arr[i+1])
            else:
                i+=1
        return arr