class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n == 3:
            return True
        while n > 0:
            n = n / 3
            if n == 3:
                return True
        return False