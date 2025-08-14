class Solution:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        arr.sort()
        close = float('inf')
        res = 0
        for i in range(len(arr)):
            left = i + 1
            right = len(arr)-1
            while left < right: 
                x = arr[left] + arr[i] + arr[right]
                if x <= target:
                    left += 1
                elif x > target:
                    right -= 1

                if abs(target - x) < close:
                    close = abs(target - x)
                    res = x

        return res