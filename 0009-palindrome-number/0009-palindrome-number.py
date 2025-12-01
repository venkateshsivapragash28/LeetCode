class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        res = 0
        while x:
            rem = x % 10
            res *= 10
            res += rem
            
            x = x//10
        return res == original
