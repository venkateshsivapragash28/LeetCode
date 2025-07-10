class Solution(object):
    def search(self, arr, target):
        left = 0
        right =len(arr)-1
        while left <= right:
            mid = (right+left)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid -1
            else:
                left = mid+1
        return -1