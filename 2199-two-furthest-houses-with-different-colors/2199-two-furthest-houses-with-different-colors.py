class Solution(object):
    def maxDistance(self, arr):
        max_dist = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] != arr[j]:
                    max_dist = max(max_dist, abs(i-j))
        return max_dist
