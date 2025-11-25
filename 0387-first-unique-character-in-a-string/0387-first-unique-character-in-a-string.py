class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dict = {}

        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1



        for index, value in enumerate(s):
            if dict[value] == 1:
                return index
        
        return -1