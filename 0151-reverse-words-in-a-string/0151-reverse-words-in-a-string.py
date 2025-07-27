class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        s = s.split()
        count = 0
        n = len(s)
        for i in range(len(s)-1, -1, -1):
            res+=s[i]
            count+=1
            if count == n:
                return res
            res+=" "

        