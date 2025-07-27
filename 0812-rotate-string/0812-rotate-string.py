class Solution(object):
    def rotateString(self, s, goal):
        
        for i in range(len(s)):
            if s == goal:
                return True
            else:
                s = s[1:] + s[:1]
        return False