class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        counterr = Counter(s)
        vowels = {'a','e','i','o','u'}
        vow = 0
        constant = 0

        for ch, c in counterr.items():
            if ch in vowels:
                if c > vow:
                    vow = c
            else:
                if c > constant:
                    constant = c

        return vow + constant
