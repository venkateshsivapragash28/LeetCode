class Solution(object):
    def longestPalindrome(self, s):
        def ispalindrome(string):
            return string == string[::-1]

        max_count = 0
        string = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i + 1 <= max_count:
                    continue
                if ispalindrome(s[i:j+1]):
                    string = s[i:j+1]
                    max_count = j - i + 1
        return string