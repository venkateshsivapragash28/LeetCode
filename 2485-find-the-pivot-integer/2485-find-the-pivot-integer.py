class Solution:
    def pivotInteger(self, n: int) -> int:
        total = 0

        for i in range(1,n+1):
            total = total + i
        summ = 0
        for i in range(1, n+1):
            if summ + i == total - summ:
                return i
            summ += i
        return -1