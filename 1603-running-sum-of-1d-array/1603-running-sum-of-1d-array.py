class Solution(object):
    def runningSum(self, arr):
        ls = []
        for i in range(len(arr)):
            sum = 0
            for j in range(i+1):
                sum = sum+arr[j]
            ls.append(sum)
        return ls