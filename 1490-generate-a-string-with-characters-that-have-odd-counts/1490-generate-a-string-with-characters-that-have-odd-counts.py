class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'a'
        if n % 2 == 0:
            s = 'a' 
            s = s * (n-1)
            s = s + 'b'
        if n % 2 == 1:
            s = 'a'
            s = (s * n)
        return s