class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                return abs(arr[i])
            else:
                arr[index] = -arr[index]
            