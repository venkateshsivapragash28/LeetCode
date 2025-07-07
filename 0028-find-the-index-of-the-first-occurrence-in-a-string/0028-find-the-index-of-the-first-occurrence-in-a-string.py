class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        i = 0
        while i <= len(haystack) - n:
            if haystack[i:i+n] == needle:
                return i
            else:
                i = i+1
        return -1
