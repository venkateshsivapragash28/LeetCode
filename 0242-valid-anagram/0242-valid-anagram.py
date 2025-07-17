class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s1 = []
        for i in s:
            s1.append(i)
        s2 = []
        for i in t:
            s2.append(i)

        count = 0
        for i in range(len(s2)):
            if s2[i] in s1 :
                count+=1
                s1.remove(s2[i])
        if len(s2) == count:
            return True
        return False