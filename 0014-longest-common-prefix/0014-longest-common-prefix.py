class Solution(object):
    def longestCommonPrefix(self, words):
        string = words[0]
        res = words[0]
        for word in words:
            small = min(len(string), len(word))
            temp = ''
            for i in range(small):
                if string[i] == word[i]:
                    temp+=string[i]
                else:
                    break
            if len(temp) < len(res):
                res = temp
        return res