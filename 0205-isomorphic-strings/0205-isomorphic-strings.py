class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        i = 0
        while i < len(s):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            elif dict1[s[i]] != t[i]:
                return False
            i += 1
        i = 0
        dict2 = {}
        while i < len(t):
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
            elif dict2[t[i]] != s[i]:
                return False
            i += 1
        return True

