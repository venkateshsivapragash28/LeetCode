class Solution(object):
    def eraseOverlapIntervals(self, arr):
        def get_end(arr):
            return arr[1]
        original = arr[::]
        arr.sort(key = get_end)
        i = 0
        while i < len(arr)-1:
            if arr[i+1][0] < arr[i][1]:
                arr.remove(arr[i+1])
            else:
                i+=1
        return len(original) - len(arr)