class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def ispalindrome(s):
            return s == s[::-1]
        if ispalindrome(s):
            return s
        res = ''
        x = s[::-1]
        while x:
            if ispalindrome(x + s):
                res = x + s
                x = x[:-1]
            else:
                x = x[:-1]
            
        return res