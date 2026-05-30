class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for index, value in enumerate(s):
            if value in seen:
                seen[value][1] += 1
            else:
                seen[value] = [index, 1]

        for i in seen:
            if seen[i][1] == 1:
                return seen[i][0]
        return -1

        