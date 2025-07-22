class Solution(object):
    def longestConsecutive(self, arr):
        arr.sort()
        max_count = 0
        count = 1
        if len(arr) == 0:
            return 0
        for i in range(len(arr)-1):
            if arr[i+1] == arr[i]+1:
                count+=1
            elif arr[i+1] == arr[i]:
                continue
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        return max_count