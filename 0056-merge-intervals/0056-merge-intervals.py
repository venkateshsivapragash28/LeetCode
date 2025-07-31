class Solution(object):
    def merge(self, arr):
        i = 0
        def get_start(arr):
            return arr[0]
        arr.sort(key = get_start)

        while i < len(arr)-1:
            if arr[i][1] >= arr[i+1][0] and arr[i][1] <= arr[i+1][1]:
                arr[i] = [arr[i][0], arr[i+1][1]]
                arr.remove(arr[i+1])
            elif arr[i][1] >= arr[i+1][0] and arr[i][1] >= arr[i+1][1]:
                arr.remove(arr[i+1])
            else:
                i+=1
        return arr