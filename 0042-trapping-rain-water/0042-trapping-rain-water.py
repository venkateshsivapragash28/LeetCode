class Solution(object):
    def trap(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        nextt = [0]*len(arr)
        maxi = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            nextt[i] = maxi
            maxi = max(maxi, arr[i])

        prev = [0]*len(arr)
        maxi = arr[0]
        for i in range(len(arr)):
            prev[i] = maxi
            maxi = max(maxi, arr[i])

        mini = 0
        summ = 0
        for i in range(len(arr)):
            if nextt[i] > arr[i] < prev[i]:
                mini = min(nextt[i], prev[i])
                summ = summ + abs(mini - arr[i])
        
        return summ