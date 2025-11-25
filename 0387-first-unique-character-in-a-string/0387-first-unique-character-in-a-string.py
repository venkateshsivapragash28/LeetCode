class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        q = {}
        seen = {}
        for index, value in enumerate(s):
            if value in q:
                seen[value] = 1
            else:
                q[value] = 1


        for index, value in enumerate(s):
            if value not in seen:
                return index

        return -1
